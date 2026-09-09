import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import product_frontmatter as fm

ROOT = Path(__file__).resolve().parent.parent
BLOCKED = {403, 429}
USER_AGENT = "Mozilla/5.0 (Macintosh) defiprime-directory-check/1.0"


def status(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return str(error)


def main():
    failures = []
    blocked = []
    for path in sorted((ROOT / "content" / "product").glob("*/*.md")):
        if path.name == "_index.md":
            continue
        meta, _ = fm.load(path)
        code = status(str(meta["product-url"]))
        if code in BLOCKED:
            blocked.append(f"{path.relative_to(ROOT)} {meta['product-url']} {code}")
        elif code != 200:
            failures.append(f"{path.relative_to(ROOT)} {meta['product-url']} {code}")
    for line in blocked:
        print(f"blocked {line}")
    for line in failures:
        print(line)
    print(f"{len(failures)} failures, {len(blocked)} bot-blocked")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
