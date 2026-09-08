#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import json
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, os.pardir, "scripts", "algolia-index.py")


def load_module():
    spec = importlib.util.spec_from_file_location("algolia_index", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


algolia_index = load_module()


def make_record(object_id, filler_chars=0):
    return {
        "objectID": object_id,
        "title": object_id,
        "url": object_id,
        "content": "x" * filler_chars,
        "html": "<p>" + "x" * filler_chars + "</p>",
    }


def write_index(records):
    handle = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(records, handle, ensure_ascii=False)
    handle.close()
    return handle.name


class ExplodingHttp:
    def __init__(self):
        self.calls = []

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        raise AssertionError("network call attempted")


class EncodeRecordTests(unittest.TestCase):
    def test_size_is_compact_utf8_bytes(self):
        record = {"objectID": "/a", "title": "b"}
        self.assertEqual(
            algolia_index.encode_record(record),
            b'{"objectID":"/a","title":"b"}',
        )
        self.assertEqual(algolia_index.record_size(record), 29)

    def test_non_ascii_counted_as_utf8_bytes_not_escapes(self):
        record = {"objectID": "/a", "title": "é"}
        self.assertEqual(algolia_index.record_size(record), 30)

    def test_angle_brackets_are_not_unicode_escaped(self):
        record = {"html": "<p>a</p>"}
        self.assertNotIn(b"\\u003c", algolia_index.encode_record(record))


class LoadRecordsTests(unittest.TestCase):
    def test_reads_a_json_list(self):
        path = write_index([make_record("/a"), make_record("/b")])
        self.addCleanup(os.unlink, path)
        records = algolia_index.load_records(path)
        self.assertEqual([r["objectID"] for r in records], ["/a", "/b"])

    def test_rejects_a_non_list_payload(self):
        path = write_index({"objectID": "/a"})
        self.addCleanup(os.unlink, path)
        with self.assertRaises(ValueError):
            algolia_index.load_records(path)

    def test_rejects_a_record_without_an_object_id(self):
        path = write_index([{"title": "no id"}])
        self.addCleanup(os.unlink, path)
        with self.assertRaises(ValueError):
            algolia_index.load_records(path)

    def test_rejects_duplicate_object_ids(self):
        path = write_index([make_record("/a"), make_record("/a")])
        self.addCleanup(os.unlink, path)
        with self.assertRaises(ValueError):
            algolia_index.load_records(path)


class MeasurementTests(unittest.TestCase):
    def test_total_bytes_sums_every_record(self):
        records = [make_record("/a", 10), make_record("/b", 20)]
        expected = sum(algolia_index.record_size(r) for r in records)
        self.assertEqual(algolia_index.total_bytes(records), expected)

    def test_total_bytes_of_nothing_is_zero(self):
        self.assertEqual(algolia_index.total_bytes([]), 0)

    def test_largest_record_returns_the_biggest_and_its_size(self):
        small = make_record("/a", 10)
        big = make_record("/b", 500)
        record, size = algolia_index.largest_record([small, big, make_record("/c", 20)])
        self.assertEqual(record["objectID"], "/b")
        self.assertEqual(size, algolia_index.record_size(big))

    def test_largest_record_of_nothing_is_none(self):
        self.assertEqual(algolia_index.largest_record([]), (None, 0))

    def test_oversized_records_reports_object_id_and_size(self):
        small = make_record("/a", 10)
        big = make_record("/b", 500)
        found = algolia_index.oversized_records([small, big], 200)
        self.assertEqual([object_id for object_id, _ in found], ["/b"])
        self.assertEqual(found[0][1], algolia_index.record_size(big))

    def test_nothing_is_oversized_under_the_real_cap(self):
        self.assertEqual(algolia_index.MAX_RECORD_BYTES, 20000)
        records = [make_record("/a", 10), make_record("/b", 500)]
        self.assertEqual(
            algolia_index.oversized_records(records, algolia_index.MAX_RECORD_BYTES), []
        )


class BatchTests(unittest.TestCase):
    def test_every_record_survives_batching_in_order(self):
        records = [make_record("/%d" % i, 100) for i in range(25)]
        batches = algolia_index.batch_records(records, max_bytes=900, max_records=1000)
        flat = [r["objectID"] for batch in batches for r in batch]
        self.assertEqual(flat, [r["objectID"] for r in records])

    def test_no_batch_exceeds_the_byte_cap_when_records_fit(self):
        records = [make_record("/%d" % i, 100) for i in range(25)]
        batches = algolia_index.batch_records(records, max_bytes=900, max_records=1000)
        self.assertGreater(len(batches), 1)
        for batch in batches:
            self.assertLessEqual(algolia_index.total_bytes(batch), 900)

    def test_a_record_larger_than_the_cap_gets_its_own_batch(self):
        records = [make_record("/a", 10), make_record("/big", 5000), make_record("/b", 10)]
        batches = algolia_index.batch_records(records, max_bytes=900, max_records=1000)
        big_batches = [b for b in batches if any(r["objectID"] == "/big" for r in b)]
        self.assertEqual(len(big_batches), 1)
        self.assertEqual(len(big_batches[0]), 1)

    def test_record_count_cap_is_honoured(self):
        records = [make_record("/%d" % i) for i in range(10)]
        batches = algolia_index.batch_records(records, max_bytes=10 ** 9, max_records=3)
        self.assertEqual([len(b) for b in batches], [3, 3, 3, 1])

    def test_no_batches_for_no_records(self):
        self.assertEqual(algolia_index.batch_records([], 900, 10), [])

    def test_batch_body_wraps_records_in_add_object_actions(self):
        body = algolia_index.batch_body([make_record("/a")])
        parsed = json.loads(body.decode("utf-8"))
        self.assertEqual(parsed["requests"][0]["action"], "addObject")
        self.assertEqual(parsed["requests"][0]["body"]["objectID"], "/a")


class DryRunTests(unittest.TestCase):
    def setUp(self):
        self.records = [make_record("/a", 10), make_record("/b", 500)]
        self.path = write_index(self.records)
        self.addCleanup(os.unlink, self.path)
        self.http = ExplodingHttp()

    def run_main(self, argv):
        return algolia_index.main(argv, http=self.http)

    def test_dry_run_succeeds_and_never_touches_the_network(self):
        code = self.run_main(["--dry-run", "--input", self.path])
        self.assertEqual(code, 0)
        self.assertEqual(self.http.calls, [])

    def test_dry_run_report_states_count_bytes_largest_and_first_record(self):
        report = algolia_index.dry_run_report(
            self.records, "defiprime2", "18BDKQYV27", algolia_index.MAX_RECORD_BYTES
        )
        self.assertIn("records: 2", report)
        self.assertIn(
            "total bytes: %d" % algolia_index.total_bytes(self.records), report
        )
        self.assertIn("largest record: ", report)
        self.assertIn("/b", report)
        self.assertIn("first record:", report)
        first = report.split("first record:", 1)[1].strip()
        self.assertEqual(json.loads(first)["objectID"], "/a")

    def test_dry_run_report_names_the_target_index(self):
        report = algolia_index.dry_run_report(
            self.records, "staging-index", "18BDKQYV27", algolia_index.MAX_RECORD_BYTES
        )
        self.assertIn("staging-index", report)

    def test_index_override_reaches_printed_output(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = self.run_main(
                ["--dry-run", "--input", self.path, "--index", "staging-index"]
            )
        self.assertEqual(code, 0)
        self.assertIn("staging-index", buffer.getvalue())
        self.assertIn("records: 2", buffer.getvalue())

    def test_dry_run_does_not_read_the_admin_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = os.path.join(tmp, "_algolia_api_key")
            code = self.run_main(
                ["--dry-run", "--input", self.path, "--key-file", missing]
            )
            self.assertEqual(code, 0)
            self.assertEqual(self.http.calls, [])

    def test_dry_run_flags_an_oversized_record_and_fails(self):
        path = write_index([make_record("/huge", 25000)])
        self.addCleanup(os.unlink, path)
        code = self.run_main(["--dry-run", "--input", path])
        self.assertEqual(code, 1)
        self.assertEqual(self.http.calls, [])

    def test_dry_run_on_an_empty_index_fails(self):
        path = write_index([])
        self.addCleanup(os.unlink, path)
        code = self.run_main(["--dry-run", "--input", path])
        self.assertEqual(code, 1)
        self.assertEqual(self.http.calls, [])


class AdminKeyTests(unittest.TestCase):
    def test_env_var_wins_over_a_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = os.path.join(tmp, "_algolia_api_key")
            self.assertEqual(
                algolia_index.read_admin_key(missing, {"ALGOLIA_ADMIN_KEY": "envkey"}),
                "envkey",
            )

    def test_file_is_read_and_stripped(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "_algolia_api_key")
            with open(path, "w", encoding="utf-8") as f:
                f.write("filekey\n")
            self.assertEqual(algolia_index.read_admin_key(path, {}), "filekey")

    def test_missing_key_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = os.path.join(tmp, "_algolia_api_key")
            with self.assertRaises(algolia_index.MissingKeyError):
                algolia_index.read_admin_key(missing, {})


if __name__ == "__main__":
    unittest.main()
