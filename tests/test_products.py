import re
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import product_frontmatter as fm
from product_taxonomy import (
    DESCRIPTION_MAX, DESCRIPTION_MIN, ECOSYSTEMS, PRODUCT_TYPES, REMOVED_DIRS,
    REMOVED_LISTINGS, REQUIRED_KEYS, TAXONOMY, colpermalink,
)

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_ROOT = ROOT / "content" / "product"
URL_RE = re.compile(r"^/product/[a-z0-9-]+\.html$")


def product_files():
    return sorted(p for p in PRODUCT_ROOT.glob("*/*.md") if p.name != "_index.md")


def split_list(value):
    return [item for item in str(value).split(", ") if item]


def redirect_rules():
    rules = {}
    for line in (ROOT / "static" / "_redirects").read_text().splitlines():
        parts = line.split()
        if len(parts) >= 3 and not line.startswith("#"):
            rules[parts[0]] = parts[1]
    return rules


def master_product_urls():
    listing = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "origin/master", "content/product"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.split()
    urls = set()
    for path in listing:
        if path.endswith("_index.md") or not path.endswith(".md"):
            continue
        text = subprocess.run(["git", "show", f"origin/master:{path}"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        match = re.search(r"^url:\s*(\S+)", text, re.M)
        if match:
            urls.add(match.group(1))
    return urls


class ProductFilesTest(unittest.TestCase):
    def test_directories_match_taxonomy(self):
        dirs = {p.name for p in PRODUCT_ROOT.iterdir() if p.is_dir()}
        self.assertEqual(dirs, set(TAXONOMY))
        for gone in REMOVED_DIRS:
            self.assertFalse((PRODUCT_ROOT / gone).exists(), gone)

    def test_every_product_is_valid(self):
        seen = {}
        for path in product_files():
            meta, _ = fm.load(path)
            directory = path.parent.name
            with self.subTest(file=str(path.relative_to(ROOT))):
                for key in REQUIRED_KEYS:
                    self.assertIn(key, meta)
                self.assertRegex(meta["url"], URL_RE)
                if fm.is_rendering(meta):
                    self.assertNotIn(meta["url"], seen, f"also rendered by {seen.get(meta['url'])}")
                    seen[meta["url"]] = path.name
                self.assertTrue((ROOT / "static" / meta["image"].lstrip("/")).is_file(), meta["image"])
                self.assertEqual(meta["coltitle"], TAXONOMY[directory]["coltitle"])
                self.assertEqual(meta["colpermalink"], colpermalink(directory))
                self.assertIn(meta["product-type"], PRODUCT_TYPES)
                filters = split_list(meta["filter"])
                self.assertTrue(filters, "filter is empty")
                self.assertTrue(set(filters) <= set(TAXONOMY[directory]["filters"]), filters)
                self.assertTrue(set(split_list(meta["ecosystem"])) <= ECOSYSTEMS, meta["ecosystem"])
                description = str(meta["product-description"])
                self.assertGreaterEqual(len(description), DESCRIPTION_MIN)
                self.assertLessEqual(len(description), DESCRIPTION_MAX)
                self.assertNotIn("\u2014", description)
                if "rank" in meta:
                    self.assertIsInstance(meta["rank"], int)
                    self.assertGreaterEqual(meta["rank"], 1)

    def test_listing_pages_match_taxonomy(self):
        listings = {}
        for path in (ROOT / "content").glob("*.md"):
            meta, _ = fm.load(path)
            if "cards" in meta:
                listings[meta["cards"]] = (path.name, meta)
        self.assertEqual(set(listings), set(TAXONOMY))
        for directory, spec in TAXONOMY.items():
            name, meta = listings[directory]
            with self.subTest(directory=directory):
                self.assertEqual(name, spec["listing"])
                self.assertEqual(meta["url"], spec["url"])
                self.assertEqual(meta["title"], spec["title"])
                self.assertEqual(meta["h1title"], spec["h1title"])
                self.assertEqual(meta["category"], "products")
                self.assertTrue(120 <= len(str(meta["metadescription"])) <= 160, len(str(meta["metadescription"])))

    def test_redirects_cover_removed_paths(self):
        rules = redirect_rules()
        for old, new in REMOVED_LISTINGS.items():
            self.assertEqual(rules.get(old), new)
            self.assertEqual(rules.get(old + ".html"), new)
        current = {fm.load(p)[0]["url"] for p in product_files()}
        listing_urls = {spec["url"].removesuffix(".html") for spec in TAXONOMY.values()}
        for url in master_product_urls() - current:
            bare = url.removesuffix(".html")
            with self.subTest(url=url):
                self.assertIn(rules.get(bare), listing_urls)
                self.assertEqual(rules.get(url), rules.get(bare))


if __name__ == "__main__":
    unittest.main()
