import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))
from product_taxonomy import KEY_ORDER


class RawLoader(yaml.SafeLoader):
    pass


RawLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in RawLoader.yaml_implicit_resolvers.items()
}


def split(text):
    if not text.startswith("---\n"):
        raise ValueError("missing front matter")
    end = text.index("\n---", 4)
    return text[4:end], text[end + 4:].lstrip("\n")


def load(path):
    front, body = split(Path(path).read_text(encoding="utf-8"))
    return yaml.load(front, Loader=RawLoader) or {}, body


def ordered(meta):
    known = [(key, meta[key]) for key in KEY_ORDER if key in meta]
    extra = [(key, value) for key, value in meta.items() if key not in KEY_ORDER]
    return dict(known + extra)


def dump(path, meta, body=""):
    front = yaml.safe_dump(ordered(meta), sort_keys=False, allow_unicode=True, width=10000)
    text = f"---\n{front}---\n"
    if body:
        text += "\n" + body.rstrip("\n") + "\n"
    Path(path).write_text(text, encoding="utf-8")


def is_rendering(meta):
    build = meta.get("build") or {}
    return build.get("render") != "link"
