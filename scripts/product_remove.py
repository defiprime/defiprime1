import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))
import product_frontmatter as fm
from product_taxonomy import TAXONOMY

ROOT = Path(__file__).resolve().parent.parent
REDIRECTS = ROOT / "static" / "_redirects"


def redirect_lines(meta, directory):
    target = TAXONOMY[directory]["url"].removesuffix(".html")
    bare = str(meta["url"]).removesuffix(".html")
    return [f"{bare}  {target}  301", f"{bare}.html  {target}  301"]


def remove(path):
    meta, _ = fm.load(path)
    lines = redirect_lines(meta, path.parent.name)
    existing = REDIRECTS.read_text()
    additions = [line for line in lines if line not in existing]
    if additions:
        REDIRECTS.write_text(existing.rstrip("\n") + "\n" + "\n".join(additions) + "\n")
    subprocess.run(["git", "rm", "-q", str(path.relative_to(ROOT))], cwd=ROOT, check=True)
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", required=True)
    args = parser.parse_args()
    for line in Path(args.list).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            for rule in remove(ROOT / line):
                print(rule)


if __name__ == "__main__":
    main()
