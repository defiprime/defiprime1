#!/usr/bin/env python3
import contextlib
import io
import os
import tempfile
import unittest

from algolia_index_fixtures import RecordingHttp, load_module, make_record, write_index

algolia_index = load_module()


class PushSequenceTests(unittest.TestCase):
    def setUp(self):
        self.http = RecordingHttp()
        self.client = algolia_index.Client("18BDKQYV27", "adminkey", self.http)
        self.records = [make_record("/a", 10), make_record("/b", 20)]

    def quiet(self, *args, **kwargs):
        return None

    def push(self):
        algolia_index.push(
            self.client,
            "defiprime2",
            self.records,
            "defiprime2_tmp_9",
            report=self.quiet,
        )

    def test_three_steps_run_in_copy_upload_move_order(self):
        self.push()
        self.assertEqual(
            self.http.paths(),
            [
                "/1/indexes/defiprime2/operation",
                "/1/indexes/defiprime2_tmp_9/batch",
                "/1/indexes/defiprime2_tmp_9/operation",
            ],
        )

    def test_copy_carries_the_settings_scope_and_the_temp_destination(self):
        self.push()
        _, _, payload = self.http.posts()[0]
        self.assertEqual(payload["operation"], "copy")
        self.assertEqual(payload["destination"], "defiprime2_tmp_9")
        self.assertEqual(payload["scope"], ["settings", "synonyms", "rules"])

    def test_records_are_uploaded_to_the_temp_index_only(self):
        self.push()
        _, url, payload = self.http.posts()[1]
        self.assertTrue(url.endswith("/1/indexes/defiprime2_tmp_9/batch"))
        self.assertEqual(
            [request["body"]["objectID"] for request in payload["requests"]],
            ["/a", "/b"],
        )
        self.assertTrue(
            all(request["action"] == "addObject" for request in payload["requests"])
        )

    def test_move_runs_last_and_targets_the_live_index(self):
        self.push()
        _, url, payload = self.http.posts()[-1]
        self.assertTrue(url.endswith("/1/indexes/defiprime2_tmp_9/operation"))
        self.assertEqual(payload, {"operation": "move", "destination": "defiprime2"})

    def test_the_live_index_is_only_ever_the_copy_source_and_the_move_target(self):
        self.push()
        paths = self.http.paths()
        live = [
            (position, path)
            for position, path in enumerate(paths)
            if path.startswith("/1/indexes/defiprime2/")
        ]
        self.assertEqual(live, [(0, "/1/indexes/defiprime2/operation")])
        self.assertEqual(self.http.posts()[0][2]["operation"], "copy")

    def test_every_write_is_awaited_before_the_next_one(self):
        self.push()
        self.assertEqual(
            [call[0] for call in self.http.calls],
            ["POST", "GET", "POST", "GET", "POST", "GET"],
        )
        for post, get in zip(self.http.calls[::2], self.http.calls[1::2]):
            index = post[1].rsplit("/1/indexes/", 1)[1].split("/")[0]
            self.assertTrue(get[1].endswith(f"/1/indexes/{index}/task/1"))

    def test_a_batch_split_uploads_every_batch_before_the_move(self):
        self.records = [make_record("/%d" % i, 100) for i in range(25)]
        original = algolia_index.MAX_BATCH_BYTES
        algolia_index.MAX_BATCH_BYTES = 900
        self.addCleanup(setattr, algolia_index, "MAX_BATCH_BYTES", original)
        self.push()
        paths = self.http.paths()
        batch_paths = [p for p in paths if p.endswith("/batch")]
        self.assertGreater(len(batch_paths), 1)
        self.assertTrue(
            all(p == "/1/indexes/defiprime2_tmp_9/batch" for p in batch_paths)
        )
        self.assertEqual(paths[-1], "/1/indexes/defiprime2_tmp_9/operation")
        uploaded = [
            request["body"]["objectID"]
            for _, path, payload in self.http.posts()
            if path.endswith("/batch")
            for request in payload["requests"]
        ]
        self.assertEqual(uploaded, [r["objectID"] for r in self.records])

    def test_wait_stops_at_published_without_sleeping(self):
        slept = []
        self.client.wait("defiprime2", 7, sleep=slept.append)
        self.assertEqual(slept, [])
        self.assertEqual(len(self.http.calls), 1)

    def test_the_admin_key_and_app_id_travel_on_every_call(self):
        self.push()
        self.assertEqual(self.client.headers["X-Algolia-API-Key"], "adminkey")
        self.assertEqual(self.client.headers["X-Algolia-Application-Id"], "18BDKQYV27")
        self.assertEqual(self.client.headers["Content-Type"], "application/json")

    def test_main_pushes_through_a_pid_named_temp_index(self):
        path = write_index(self.records)
        self.addCleanup(os.unlink, path)
        with tempfile.TemporaryDirectory() as tmp:
            key_file = os.path.join(tmp, "_algolia_api_key")
            with open(key_file, "w", encoding="utf-8") as handle:
                handle.write("adminkey\n")
            with contextlib.redirect_stdout(io.StringIO()):
                code = algolia_index.main(
                    ["--input", path, "--key-file", key_file], http=self.http
                )
        self.assertEqual(code, 0)
        temp_index = f"defiprime2_tmp_{os.getpid()}"
        self.assertEqual(
            self.http.paths(),
            [
                "/1/indexes/defiprime2/operation",
                f"/1/indexes/{temp_index}/batch",
                f"/1/indexes/{temp_index}/operation",
            ],
        )
        self.assertEqual(self.http.posts()[0][2]["destination"], temp_index)


if __name__ == "__main__":
    unittest.main()
