#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

DEFAULT_APP_ID = "18BDKQYV27"
DEFAULT_INDEX = "defiprime2"
DEFAULT_INPUT = "public/searchindex.json"
DEFAULT_KEY_FILE = "_algolia_api_key"
MAX_RECORD_BYTES = 20000
MAX_BATCH_BYTES = 8_000_000
MAX_BATCH_RECORDS = 1000
COPY_SCOPE = ["settings", "synonyms", "rules"]
TASK_POLL_SECONDS = 1.0
TASK_POLL_LIMIT = 300


class MissingKeyError(Exception):
    pass


class AlgoliaError(Exception):
    pass


def encode_record(record):
    return json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def record_size(record):
    return len(encode_record(record))


def load_records(path):
    with open(path, encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, list):
        raise ValueError(f"{path}: expected a JSON list of records")
    seen = set()
    for position, record in enumerate(payload):
        if not isinstance(record, dict):
            raise ValueError(f"{path}: record {position} is not an object")
        object_id = record.get("objectID")
        if not object_id:
            raise ValueError(f"{path}: record {position} has no objectID")
        if object_id in seen:
            raise ValueError(f"{path}: duplicate objectID {object_id!r}")
        seen.add(object_id)
    return payload


def total_bytes(records):
    return sum(record_size(record) for record in records)


def largest_record(records):
    biggest = None
    biggest_size = 0
    for record in records:
        size = record_size(record)
        if biggest is None or size > biggest_size:
            biggest = record
            biggest_size = size
    if biggest is None:
        return (None, 0)
    return (biggest, biggest_size)


def oversized_records(records, cap):
    found = []
    for record in records:
        size = record_size(record)
        if size > cap:
            found.append((record.get("objectID"), size))
    return found


def batch_records(records, max_bytes, max_records):
    batches = []
    current = []
    current_bytes = 0
    for record in records:
        size = record_size(record)
        if current and (
            len(current) >= max_records or current_bytes + size > max_bytes
        ):
            batches.append(current)
            current = []
            current_bytes = 0
        current.append(record)
        current_bytes += size
    if current:
        batches.append(current)
    return batches


def batch_body(records):
    requests = [{"action": "addObject", "body": record} for record in records]
    return json.dumps(
        {"requests": requests}, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")


def read_admin_key(key_file, env):
    from_env = env.get("ALGOLIA_ADMIN_KEY", "").strip()
    if from_env:
        return from_env
    if os.path.exists(key_file):
        with open(key_file, encoding="utf-8") as handle:
            from_file = handle.read().strip()
        if from_file:
            return from_file
    raise MissingKeyError(
        f"no admin key: set ALGOLIA_ADMIN_KEY or write it to {key_file}"
    )


def http_request(method, url, headers, body=None):
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")
        raise AlgoliaError(f"{method} {url} -> {error.code}: {detail}") from error


class Client:
    def __init__(self, app_id, admin_key, http):
        self.app_id = app_id
        self.http = http
        self.headers = {
            "X-Algolia-Application-Id": app_id,
            "X-Algolia-API-Key": admin_key,
            "Content-Type": "application/json",
        }

    def url(self, path):
        return f"https://{self.app_id}.algolia.net{path}"

    def post(self, path, payload):
        return self.http("POST", self.url(path), self.headers, payload)

    def get(self, path):
        return self.http("GET", self.url(path), self.headers, None)

    def wait(self, index, task_id, sleep=time.sleep):
        for _ in range(TASK_POLL_LIMIT):
            status = self.get(f"/1/indexes/{index}/task/{task_id}").get("status")
            if status == "published":
                return
            sleep(TASK_POLL_SECONDS)
        raise AlgoliaError(f"task {task_id} on {index} never published")

    def operation(self, source, operation, destination, scope=None):
        payload = {"operation": operation, "destination": destination}
        if scope is not None:
            payload["scope"] = scope
        response = self.post(
            f"/1/indexes/{source}/operation",
            json.dumps(payload, separators=(",", ":")).encode("utf-8"),
        )
        self.wait(source, response["taskID"])

    def add_objects(self, index, batches, report=print):
        for position, batch in enumerate(batches, 1):
            response = self.post(f"/1/indexes/{index}/batch", batch_body(batch))
            self.wait(index, response["taskID"])
            report(f"batch {position}/{len(batches)}: {len(batch)} records")


def push(client, index, records, temp_index, report=print):
    report(f"copying settings, synonyms and rules from {index} to {temp_index}")
    client.operation(index, "copy", temp_index, scope=COPY_SCOPE)
    batches = batch_records(records, MAX_BATCH_BYTES, MAX_BATCH_RECORDS)
    report(f"uploading {len(records)} records in {len(batches)} batches")
    client.add_objects(temp_index, batches, report=report)
    report(f"moving {temp_index} onto {index}")
    client.operation(temp_index, "move", index)
    report(f"done: {index} now holds {len(records)} records")


def dry_run_report(records, index, app_id, cap):
    biggest, biggest_size = largest_record(records)
    batches = batch_records(records, MAX_BATCH_BYTES, MAX_BATCH_RECORDS)
    lines = [
        f"target index: {index} (app {app_id})",
        f"records: {len(records)}",
        f"total bytes: {total_bytes(records)}",
        f"batches: {len(batches)} (max {MAX_BATCH_RECORDS} records, {MAX_BATCH_BYTES} bytes)",
        f"record byte cap: {cap}",
        "largest record: {} bytes ({})".format(
            biggest_size, biggest.get("objectID") if biggest else "none"
        ),
        "first record:",
        json.dumps(records[0], ensure_ascii=False, indent=2) if records else "none",
    ]
    return "\n".join(lines)


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Build and push the defiprime Algolia search index."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--index", default=DEFAULT_INDEX)
    parser.add_argument("--app-id", default=DEFAULT_APP_ID)
    parser.add_argument("--key-file", default=DEFAULT_KEY_FILE)
    parser.add_argument("--max-record-bytes", type=int, default=MAX_RECORD_BYTES)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv=None, http=http_request):
    args = parse_args(argv)
    try:
        records = load_records(args.input)
    except (OSError, ValueError) as error:
        print(f"algolia-index: {error}", file=sys.stderr)
        return 1

    if not records:
        print(f"algolia-index: {args.input} holds no records", file=sys.stderr)
        return 1

    oversized = oversized_records(records, args.max_record_bytes)
    if oversized:
        for object_id, size in oversized:
            print(
                f"algolia-index: {object_id} is {size} bytes, over the "
                f"{args.max_record_bytes} byte cap",
                file=sys.stderr,
            )
        return 1

    if args.dry_run:
        print(dry_run_report(records, args.index, args.app_id, args.max_record_bytes))
        return 0

    try:
        admin_key = read_admin_key(args.key_file, os.environ)
    except MissingKeyError as error:
        print(f"algolia-index: {error}", file=sys.stderr)
        return 1

    client = Client(args.app_id, admin_key, http)
    temp_index = f"{args.index}_tmp_{os.getpid()}"
    try:
        push(client, args.index, records, temp_index)
    except AlgoliaError as error:
        print(f"algolia-index: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
