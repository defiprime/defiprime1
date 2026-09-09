import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import product_add as pa
import product_frontmatter as fm

ENTRY = {
    "dir": "lending", "slug": "dolomite", "title": "Dolomite", "url": "https://app.dolomite.io",
    "ecosystem": "arbitrum, berachain",
    "description": "Dolomite is a margin and lending protocol on Arbitrum and Berachain that accepts long-tail collateral.",
    "filter": "Lend, Borrow", "rank": 7, "twitter": "https://x.com/dolomite_io",
}


class BuildMetaTest(unittest.TestCase):
    def test_new_entry_meta(self):
        meta = pa.build_meta(ENTRY, today="2026-09-09")
        self.assertEqual(meta["url"], "/product/dolomite.html")
        self.assertEqual(meta["git-date"], "2026-09-09T12:00:00-04:00")
        self.assertEqual(meta["image"], "/images/output_md/dolomite.io.png")
        self.assertEqual(meta["coltitle"], "Lending")
        self.assertEqual(meta["colpermalink"], "decentralized-lending")
        self.assertEqual(meta["product-type"], "non-custodial")
        self.assertEqual(meta["rank"], 7)
        self.assertEqual(list(meta)[:3], ["url", "git-date", "product-title"])

    def test_rejects_unknown_filter(self):
        bad = dict(ENTRY, filter="Margin")
        with self.assertRaises(ValueError):
            pa.build_meta(bad, today="2026-09-09")

    def test_rejects_description_out_of_bounds(self):
        bad = dict(ENTRY, description="Too short.")
        with self.assertRaises(ValueError):
            pa.build_meta(bad, today="2026-09-09")

    def test_rejects_unknown_ecosystem(self):
        bad = dict(ENTRY, ecosystem="arbitrum, moonbase")
        with self.assertRaises(ValueError):
            pa.build_meta(bad, today="2026-09-09")


class WriteTest(unittest.TestCase):
    def test_writes_file_and_skips_screenshot_when_image_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content" / "product" / "lending").mkdir(parents=True)
            (root / "static" / "images" / "output_md").mkdir(parents=True)
            (root / "static" / "images" / "output_md" / "dolomite.io.png").write_bytes(b"x")
            captured = []
            pa.apply_entry(ENTRY, root=root, today="2026-09-09", capture=lambda url, path: captured.append(url))
            meta, _ = fm.load(root / "content" / "product" / "lending" / "dolomite.md")
            self.assertEqual(meta["product-title"], "Dolomite")
            self.assertEqual(captured, [])

    def test_update_only_touches_given_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "content" / "product" / "lending"
            target.mkdir(parents=True)
            fm.dump(target / "aave.md", {"url": "/product/aave.html", "git-date": "2020-01-11T11:30:54-08:00", "product-title": "Aave", "product-url": "https://app.aave.com/?referral=28", "image": "/images/output_md/aave.com.png", "ecosystem": "ethereum", "product-description": "Aave is a non-custodial lending protocol on multiple chains.", "coltitle": "Lending", "colpermalink": "decentralized-lending", "product-type": "non-custodial", "filter": "Lend, Borrow"})
            pa.apply_entry({"dir": "lending", "slug": "aave", "update": True, "rank": 1}, root=root, today="2026-09-09", capture=lambda url, path: None)
            meta, _ = fm.load(target / "aave.md")
            self.assertEqual(meta["rank"], 1)
            self.assertEqual(meta["product-url"], "https://app.aave.com/?referral=28")
            self.assertEqual(meta["git-date"], "2020-01-11T11:30:54-08:00")

    def test_copy_of_writes_list_only_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_dir = root / "content" / "product" / "assets-tokenization"
            source_dir.mkdir(parents=True)
            target_dir = root / "content" / "product" / "lending"
            target_dir.mkdir(parents=True)
            fm.dump(source_dir / "maple.md", {"url": "/product/maple.html", "git-date": "2026-01-05T12:00:00-04:00", "product-title": "Maple", "product-url": "https://maple.finance", "image": "/images/output_md/maple.finance.png", "ecosystem": "ethereum", "product-description": "Maple is an institutional capital marketplace for on-chain credit.", "coltitle": "Tokenization & RWA", "colpermalink": "assets-tokenization", "product-type": "non-custodial", "filter": "Private Credit", "featured": True})
            pa.apply_entry({"dir": "lending", "slug": "maple", "copy_of": "assets-tokenization/maple", "filter": "Lend, Borrow", "rank": 6}, root=root, today="2026-09-09", capture=lambda url, path: None)
            meta, _ = fm.load(target_dir / "maple.md")
            self.assertEqual(meta["build"]["render"], "link")
            self.assertEqual(meta["coltitle"], "Lending")
            self.assertEqual(meta["url"], "/product/maple.html")
            self.assertNotIn("featured", meta)


class GuardTest(unittest.TestCase):
    def test_refuses_existing_file_with_other_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "content" / "product" / "lending"
            target.mkdir(parents=True)
            (root / "static" / "images" / "output_md").mkdir(parents=True)
            (root / "static" / "images" / "output_md" / "dolomite.io.png").write_bytes(b"x")
            fm.dump(target / "dolomite.md", {"url": "/product/dolomite.html", "git-date": "2020-01-01T00:00:00-08:00", "product-title": "Dolomite", "product-url": "https://app.dolomite.io/?ref=1", "image": "/images/output_md/dolomite.io.png", "ecosystem": "arbitrum", "product-description": "Dolomite is a margin and lending protocol on Arbitrum.", "coltitle": "Lending", "colpermalink": "decentralized-lending", "product-type": "non-custodial", "filter": "Lend"})
            with self.assertRaises(ValueError):
                pa.apply_entry(ENTRY, root=root, today="2026-09-09", capture=lambda url, path: None)

    def test_refuses_second_rendering_copy_of_same_url(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content" / "product" / "lending").mkdir(parents=True)
            (root / "content" / "product" / "exchanges").mkdir(parents=True)
            (root / "static" / "images" / "output_md").mkdir(parents=True)
            (root / "static" / "images" / "output_md" / "dolomite.io.png").write_bytes(b"x")
            pa.apply_entry(ENTRY, root=root, today="2026-09-09", capture=lambda url, path: None)
            with self.assertRaises(ValueError):
                pa.apply_entry(dict(ENTRY, dir="exchanges", filter="Spot"), root=root, today="2026-09-09", capture=lambda url, path: None)

    def test_rerun_of_same_entry_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "content" / "product" / "lending").mkdir(parents=True)
            (root / "static" / "images" / "output_md").mkdir(parents=True)
            (root / "static" / "images" / "output_md" / "dolomite.io.png").write_bytes(b"x")
            pa.apply_entry(ENTRY, root=root, today="2026-09-09", capture=lambda url, path: None)
            pa.apply_entry(ENTRY, root=root, today="2026-09-09", capture=lambda url, path: None)
            meta, _ = fm.load(root / "content" / "product" / "lending" / "dolomite.md")
            self.assertEqual(meta["product-title"], "Dolomite")


if __name__ == "__main__":
    unittest.main()
