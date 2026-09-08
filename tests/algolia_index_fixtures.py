import importlib.util
import json
import os
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, os.pardir, "scripts", "algolia-index.py")
APP_HOST = "https://18BDKQYV27.algolia.net"


def load_module():
    spec = importlib.util.spec_from_file_location("algolia_index", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


class RecordingHttp:
    def __init__(self):
        self.calls = []

    def __call__(self, method, url, headers, body=None):
        payload = json.loads(body.decode("utf-8")) if body else None
        self.calls.append((method, url, payload))
        if method == "POST":
            return {"taskID": 1}
        return {"status": "published"}

    def posts(self):
        return [call for call in self.calls if call[0] == "POST"]

    def paths(self):
        return [call[1][len(APP_HOST):] for call in self.posts()]
