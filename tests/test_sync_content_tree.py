#!/usr/bin/env python3
import os
import shutil
import tempfile
import unittest

from sync_content_fixtures import DEST_FILES, SOURCE_FILES, build_tree, load_module, snapshot

sync_content = load_module()


class SyncTreeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.source = os.path.join(self.tmp, "source")
        self.dest = os.path.join(self.tmp, "dest")
        build_tree(self.source, SOURCE_FILES)
        build_tree(self.dest, DEST_FILES)
        self.report = sync_content.sync(self.source, self.dest)
        self.after_first = snapshot(self.dest)

    def read(self, rel):
        with open(os.path.join(self.dest, rel), "r", encoding="utf-8") as handle:
            return handle.read()

    def exists(self, rel):
        return os.path.exists(os.path.join(self.dest, rel))

    def test_running_twice_changes_nothing(self):
        sync_content.sync(self.source, self.dest)
        self.assertEqual(snapshot(self.dest), self.after_first)

    def test_blog_post_conversions(self):
        text = self.read("content/blog/2020-01-01-hello.md")
        self.assertNotIn("\r", text)
        self.assertIn("layout: blog\n", text)
        self.assertIn("url: /hello.html\n", text)
        self.assertIn("aliases:\n  - /old-hello\n", text)
        self.assertIn("{{< youtube qQQkn361niI >}}", text)
        self.assertNotIn("permalink", text)
        self.assertNotIn("redirect_from", text)

    def test_listing_post_goes_to_its_permalink(self):
        text = self.read("content/decentralized-lending.md")
        self.assertIn("url: /decentralized-lending.html\n", text)
        self.assertIn("filter-by: ecosystem, platform, product-type, filter\n", text)
        self.assertIn("aliases:\n  - /decentralized_lending\n", text)
        self.assertFalse(self.exists("content/blog/2019-04-01-lending.md"))

    def test_product_file_is_lowercased_and_slugged(self):
        text = self.read("content/product/lending/apy.vision.md")
        self.assertIn("url: /product/apy-vision.html\n", text)
        self.assertIn("product-type: non-custodial\n", text)

    def test_duplicate_url_is_won_by_the_last_collection_in_config_order(self):
        winner = self.read("content/product/perps/aevo.md")
        loser = self.read("content/product/lending/aevo.md")
        self.assertIn("url: /product/aevo.html\n", winner)
        self.assertIn("url: /product/aevo.html\n", loser)
        self.assertIn("perps copy", winner)
        self.assertNotIn("build:", winner)
        self.assertIn("build:\n  render: link\n  list: always\n", loser)
        self.assertEqual(
            self.report.duplicate_urls,
            [("/product/aevo.html", "content/product/perps/aevo.md",
              "content/product/lending/aevo.md")],
        )

    def test_alternatives_use_their_own_permalink(self):
        self.assertIn("url: /1inch-alternatives.html\n", self.read("content/alternatives/1inch.md"))

    def test_events_are_copied_with_crlf_stripped(self):
        text = self.read("content/events/2025-01-01-devcon.md")
        self.assertNotIn("\r", text)
        self.assertIn('product-title: "Devcon"\n', text)

    def test_liquid_bodied_page_keeps_branch_body_and_branch_layout(self):
        text = self.read("content/ethereum.md")
        self.assertIn("layout: ecosystem\n", text)
        self.assertIn("url: /ethereum.html\n", text)
        self.assertIn("stats_ecosystems:\n", text)
        self.assertNotIn("{%", text)
        self.assertNotIn("{{", text)

    def test_404_keeps_the_branch_layout_name(self):
        text = self.read("content/404.md")
        self.assertIn('layout: "404"\n', text)
        self.assertIn("url: /404.html\n", text)
        self.assertNotIn("{%", text)

    def test_liquid_free_page_takes_the_master_body(self):
        text = self.read("content/about.md")
        self.assertIn("Plain prose, no template tags.", text)
        self.assertNotIn("Old prose.", text)

    def test_home_index_takes_master_front_matter_and_branch_body(self):
        text = self.read("content/_index.md")
        self.assertIn("aliases:\n  - /product\n", text)
        self.assertNotIn("layout:", text)
        self.assertNotIn("{%", text)

    def test_blog_index_drops_the_pagination_block(self):
        text = self.read("content/blog/_index.md")
        self.assertIn("url: /blog/\n", text)
        self.assertNotIn("pagination", text)
        self.assertNotIn("{%", text)

    def test_alternatives_listing_becomes_the_section_index(self):
        text = self.read("content/alternatives/_index.md")
        self.assertIn("layout: alternatives\n", text)
        self.assertIn("url: /alternatives/\n", text)
        self.assertIn("title: DeFi Alternatives\n", text)
        self.assertIn("Filter by category and explore the ecosystem.", text)
        self.assertFalse(self.exists("content/alternatives.md"))
        self.assertIn("content/alternatives/_index.md", self.report.rewritten_indexes)

    def test_section_indexes_are_left_alone(self):
        for rel in ("content/product/_index.md", "content/events/_index.md",
                    "content/product/lending/_index.md",
                    "content/product/perps/_index.md"):
            self.assertEqual(self.read(rel), DEST_FILES[rel])

    def test_removed_content_is_deleted(self):
        for rel in ("content/stale-page.md", "content/blog/2018-01-01-removed.md",
                    "content/product/lending/stale.md", "content/events/2025-01-01-gone.md",
                    "content/airdrop", "content/crypto-airdrops.md",
                    "content/solana-airdrops.md", "scripts/migrate-content.sh"):
            self.assertFalse(self.exists(rel), rel)

    def test_excluded_root_files_are_not_pages(self):
        for rel in ("content/README.md", "content/CLAUDE.md", "content/llms.txt",
                    "content/blog.md", "content/index.md"):
            self.assertFalse(self.exists(rel), rel)

    def test_assets_and_data(self):
        self.assertEqual(self.read("data/authors.yaml"), "sawinyh:\n  name: Sergej\n")
        self.assertEqual(self.read("static/robots.txt"), "User-agent: *\nAllow: /\n")
        self.assertEqual(self.read("static/images/og.png"), "PNGDATA")
        self.assertEqual(self.read("static/images/blog/new.png"), "NEWPNG")
        self.assertFalse(self.exists("static/images/gone.png"))
        self.assertEqual(self.read("images/og.png"), "LEGACY")
        self.assertEqual(self.read("defiprime.tokenlist.json"), '{"name": "defiprime"}\n')

    def test_llms_txt_with_liquid_is_not_written(self):
        self.assertFalse(self.exists("static/llms.txt"))
        self.assertIn("llms.txt", self.report.needs_template)

    def test_report_counts(self):
        self.assertEqual(self.report.youtube, [("content/blog/2020-01-01-hello.md", 1)])
        self.assertEqual(self.report.unparseable, [])
        self.assertIn("content/ethereum.md", self.report.body_diffs)


if __name__ == "__main__":
    unittest.main()
