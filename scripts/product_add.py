import argparse
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))
import product_frontmatter as fm
from product_taxonomy import ECOSYSTEMS, PRODUCT_TYPES, TAXONOMY, colpermalink

ROOT = Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CAPTURE_SIZE = (1600, 800)
IMAGE_SIZE = (800, 400)
MAX_BYTES = 300_000
NEW_DESCRIPTION_MIN = 80
NEW_DESCRIPTION_MAX = 240
REQUIRED = ["dir", "slug", "title", "url", "ecosystem", "description", "filter"]
UPDATABLE = {"rank": "rank", "filter": "filter", "ecosystem": "ecosystem", "description": "product-description", "twitter": "twitter", "github": "github"}
COPY_KEEP = ["url", "product-url", "image", "product-title", "ecosystem", "product-description", "product-type", "twitter", "github", "git-date"]


def image_host(url):
    name = urlparse(url).hostname or ""
    if name.startswith("www."):
        name = name[4:]
    if name.startswith("app."):
        name = name[4:]
    return name


def validate(entry):
    for key in REQUIRED:
        if not entry.get(key):
            raise ValueError(f"{entry.get('slug', '?')}: missing {key}")
    directory = entry["dir"]
    if directory not in TAXONOMY:
        raise ValueError(f"{entry['slug']}: unknown dir {directory}")
    filters = entry["filter"].split(", ")
    unknown = set(filters) - set(TAXONOMY[directory]["filters"])
    if unknown:
        raise ValueError(f"{entry['slug']}: unknown filter {sorted(unknown)}")
    chains = set(entry["ecosystem"].split(", ")) - ECOSYSTEMS
    if chains:
        raise ValueError(f"{entry['slug']}: unknown ecosystem {sorted(chains)}")
    length = len(entry["description"])
    if not NEW_DESCRIPTION_MIN <= length <= NEW_DESCRIPTION_MAX or "\u2014" in entry["description"]:
        raise ValueError(f"{entry['slug']}: description length {length} or em dash")
    if entry.get("product_type", "non-custodial") not in PRODUCT_TYPES:
        raise ValueError(f"{entry['slug']}: bad product_type")


def build_meta(entry, today=None):
    validate(entry)
    today = today or date.today().isoformat()
    directory = entry["dir"]
    meta = {
        "url": f"/product/{entry['slug']}.html",
        "git-date": f"{today}T12:00:00-04:00",
        "product-title": entry["title"],
        "product-url": entry["url"],
        "image": f"/images/output_md/{image_host(entry['url'])}.png",
        "ecosystem": entry["ecosystem"],
        "product-description": entry["description"],
        "coltitle": TAXONOMY[directory]["coltitle"],
        "colpermalink": colpermalink(directory),
        "product-type": entry.get("product_type", "non-custodial"),
        "filter": entry["filter"],
    }
    if entry.get("rank") is not None:
        meta["rank"] = int(entry["rank"])
    for key in ("twitter", "github", "ticker", "contract", "decimals", "platform"):
        if entry.get(key):
            meta[key] = entry[key]
    return fm.ordered(meta)


def capture_screenshot(url, path):
    with tempfile.TemporaryDirectory() as profile:
        raw = Path(profile) / "raw.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={CAPTURE_SIZE[0]},{CAPTURE_SIZE[1]}", f"--screenshot={raw}", "--virtual-time-budget=8000", f"--user-data-dir={profile}/chrome", url], check=True, capture_output=True, timeout=120)
        image = Image.open(raw).convert("RGB").resize(IMAGE_SIZE, Image.LANCZOS)
        image.save(path, optimize=True)
        if path.stat().st_size > MAX_BYTES:
            image.quantize(256).save(path, optimize=True)


def build_copy_meta(entry, root, today=None):
    source_dir, source_slug = entry["copy_of"].split("/")
    source = root / "content" / "product" / source_dir / f"{source_slug}.md"
    source_meta, _ = fm.load(source)
    directory = entry["dir"]
    meta = {key: source_meta[key] for key in COPY_KEEP if key in source_meta}
    meta["coltitle"] = TAXONOMY[directory]["coltitle"]
    meta["colpermalink"] = colpermalink(directory)
    meta["filter"] = entry["filter"]
    if entry.get("rank") is not None:
        meta["rank"] = int(entry["rank"])
    meta["build"] = {"render": "link", "list": "always"}
    return fm.ordered(meta)


def apply_entry(entry, root=ROOT, today=None, capture=capture_screenshot):
    target = root / "content" / "product" / entry["dir"] / f"{entry['slug']}.md"
    if entry.get("update"):
        meta, body = fm.load(target)
        for key, field in UPDATABLE.items():
            if key in entry:
                meta[field] = entry[key]
        fm.dump(target, meta, body)
        return target
    if entry.get("copy_of"):
        meta = build_copy_meta(entry, root, today=today)
        fm.dump(target, meta)
        return target
    meta = build_meta(entry, today=today)
    image = root / "static" / meta["image"].lstrip("/")
    if not image.exists():
        capture(entry.get("screenshot_url") or entry["url"], image)
    fm.dump(target, meta)
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("entries", nargs="+")
    args = parser.parse_args()
    for source in args.entries:
        for entry in yaml.safe_load(Path(source).read_text()) or []:
            print(apply_entry(entry).relative_to(ROOT))


if __name__ == "__main__":
    main()
