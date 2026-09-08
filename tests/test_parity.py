import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import parity


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


PAGE_A = """<!doctype html>
<html><head>
<title>Page A</title>
<meta name=description content="Description A">
<link rel=canonical href=https://defiprime.com/a>
<meta property="og:title" content="Page A">
<meta name=twitter:card content="summary">
<script type="application/ld+json">{"@type": "WebPage"}</script>
</head><body>
<h1>Heading A</h1>
<a href="/a">self</a>
<a href="/b">to b</a>
</body></html>
"""


def page_og(url="https://defiprime.com/page", image="https://defiprime.com/images/a.png", card="summary_large_image"):
    return (
        "<!doctype html>\n"
        "<html><head>\n"
        "<title>Page OG</title>\n"
        '<link rel=canonical href=https://defiprime.com/page>\n'
        '<meta property="og:url" content="%s">\n'
        '<meta property="og:image" content="%s">\n'
        '<meta name=twitter:card content="%s">\n'
        "</head><body>\n"
        "<h1>Heading OG</h1>\n"
        "</body></html>\n"
    ) % (url, image, card)


PAGE_OG = page_og()


class BuildTree(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.golden = os.path.join(self.tmp.name, "golden")
        self.public = os.path.join(self.tmp.name, "public")
        os.makedirs(self.golden)
        os.makedirs(self.public)

    def tearDown(self):
        self.tmp.cleanup()


class TestMissing(BuildTree):
    def test_missing_path_reported(self):
        write(os.path.join(self.golden, "only-golden.html"), PAGE_A)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(result.missing, ["only-golden.html"])
        self.assertEqual(result.missing_suppressed, 0)
        self.assertEqual(result.exit_code, 1)


class TestExtra(BuildTree):
    def test_extra_path_reported(self):
        write(os.path.join(self.public, "only-public.html"), PAGE_A)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(result.extra, ["only-public.html"])
        self.assertEqual(result.extra_suppressed, 0)
        self.assertEqual(result.exit_code, 1)


class TestMetaDifference(BuildTree):
    def test_title_difference_reported(self):
        write(os.path.join(self.golden, "page.html"), PAGE_A)
        hugo_page = PAGE_A.replace("Page A</title>", "Page A Renamed</title>")
        write(os.path.join(self.public, "page.html"), hugo_page)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        fields = [f for (p, f, g, h) in result.meta]
        self.assertIn("title", fields)
        self.assertEqual(result.exit_code, 1)

    def test_og_and_twitter_differences_reported_per_key(self):
        write(os.path.join(self.golden, "page.html"), PAGE_OG)
        write(os.path.join(self.public, "page.html"), page_og(url="https://defiprime.com/other"))
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        fields = [f for (p, f, g, h) in result.meta]
        self.assertEqual(fields, ["og:url"])
        self.assertEqual(
            result.meta[0],
            ("page.html", "og:url", "https://defiprime.com/page", "https://defiprime.com/other"),
        )
        self.assertEqual(result.exit_code, 1)

    def test_twitter_key_named_in_full(self):
        write(os.path.join(self.golden, "page.html"), PAGE_OG)
        write(os.path.join(self.public, "page.html"), page_og(card="summary"))
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        fields = [f for (p, f, g, h) in result.meta]
        self.assertEqual(fields, ["twitter:card"])
        self.assertEqual(result.exit_code, 1)


class TestLinksDifference(BuildTree):
    def test_link_set_difference_reported(self):
        write(os.path.join(self.golden, "page.html"), PAGE_A)
        hugo_page = PAGE_A.replace('<a href="/b">to b</a>', '<a href="/c">to c</a>')
        write(os.path.join(self.public, "page.html"), hugo_page)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(len(result.links), 1)
        path, missing, extra = result.links[0]
        self.assertEqual(path, "page.html")
        self.assertEqual(missing, ["/b"])
        self.assertEqual(extra, ["/c"])
        self.assertEqual(result.exit_code, 1)


class TestAllowlistSuppression(BuildTree):
    def test_allowlisted_finding_suppressed_with_reason(self):
        write(os.path.join(self.golden, "only-golden.html"), PAGE_A)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "MISSING only-golden.html *  # known gap, tracked in task 4\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(result.missing, [])
        self.assertEqual(result.missing_suppressed, 1)
        self.assertEqual(result.exit_code, 0)


class TestAllowlistSuppressesOneMetaKey(BuildTree):
    def test_og_url_entry_leaves_og_image_reported(self):
        write(os.path.join(self.golden, "page.html"), PAGE_OG)
        write(
            os.path.join(self.public, "page.html"),
            page_og(url="https://defiprime.com/other", image="https://defiprime.com/images/b.png"),
        )
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "META page.html og:url  # golden emits site.url here\n")
        result = parity.run(self.golden, self.public, allow_path)
        fields = [f for (p, f, g, h) in result.meta]
        self.assertEqual(fields, ["og:image"])
        self.assertEqual(result.meta_suppressed, 1)
        self.assertEqual(result.exit_code, 1)


class TestAllowlistRejectsMissingReason(unittest.TestCase):
    def test_entry_without_reason_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            allow_path = os.path.join(tmp, "allow.txt")
            write(allow_path, "MISSING only-golden.html *\n")
            with self.assertRaises(parity.AllowlistError):
                parity.load_allowlist(allow_path)


class TestIdenticalPairIsClean(BuildTree):
    def test_identical_pair_exits_zero(self):
        write(os.path.join(self.golden, "page.html"), PAGE_A)
        write(os.path.join(self.public, "page.html"), PAGE_A)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(result.missing, [])
        self.assertEqual(result.extra, [])
        self.assertEqual(result.meta, [])
        self.assertEqual(result.links, [])
        self.assertEqual(result.exit_code, 0)


class TestPathFiltering(BuildTree):
    def test_ignored_top_level_dirs_and_extensions_excluded(self):
        write(os.path.join(self.golden, "keep.html"), PAGE_A)
        write(os.path.join(self.golden, "assets", "skip.html"), PAGE_A)
        write(os.path.join(self.golden, "CLAUDE.md"), "internal notes")
        write(os.path.join(self.golden, "keep.css"), "body{}")
        write(os.path.join(self.public, "keep.html"), PAGE_A)
        write(os.path.join(self.public, "assets", "skip.html"), PAGE_A)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(result.missing, [])
        self.assertEqual(result.extra, [])
        self.assertEqual(result.exit_code, 0)


class TestEntityDecoding(BuildTree):
    def test_entities_normalized_before_comparison(self):
        golden_page = PAGE_A.replace("Page A</title>", "Fish &amp; Chips</title>")
        hugo_page = PAGE_A.replace("Page A</title>", "Fish & Chips</title>")
        write(os.path.join(self.golden, "page.html"), golden_page)
        write(os.path.join(self.public, "page.html"), hugo_page)
        allow_path = os.path.join(self.tmp.name, "allow.txt")
        write(allow_path, "# header\n")
        result = parity.run(self.golden, self.public, allow_path)
        self.assertEqual(result.meta, [])
        self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
