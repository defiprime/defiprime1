#!/usr/bin/env python3
import unittest

from sync_content_fixtures import load_module

sync_content = load_module()


class StripCarriageReturnTests(unittest.TestCase):
    def test_strips_every_carriage_return(self):
        self.assertEqual(
            sync_content.strip_cr("---\r\npermalink: aave\r\n---\r\nbody\r\n"),
            "---\npermalink: aave\n---\nbody\n",
        )

    def test_leaves_clean_text_alone(self):
        self.assertEqual(sync_content.strip_cr("a\nb\n"), "a\nb\n")

    def test_front_matter_of_crlf_file_parses_after_stripping(self):
        raw = "---\r\nlayout: [blog]\r\npermalink: aave\r\n---\r\nbody\r\n"
        fm, body = sync_content.split_front_matter(sync_content.strip_cr(raw))
        entries = sync_content.parse_front_matter(fm)
        self.assertEqual([key for key, _ in entries], ["layout", "permalink"])
        self.assertEqual(body, "body\n")


class PermalinkToUrlTests(unittest.TestCase):
    def test_bare_slug_gains_slash_and_html(self):
        self.assertEqual(sync_content.permalink_to_url("aave"), "/aave.html")

    def test_leading_slash_is_not_doubled(self):
        self.assertEqual(sync_content.permalink_to_url("/aave"), "/aave.html")

    def test_existing_html_suffix_is_kept(self):
        self.assertEqual(sync_content.permalink_to_url("404.html"), "/404.html")

    def test_surrounding_quotes_are_stripped(self):
        self.assertEqual(sync_content.permalink_to_url('"aave"'), "/aave.html")
        self.assertEqual(sync_content.permalink_to_url("'aave'"), "/aave.html")

    def test_trailing_slash_permalink_keeps_the_slash(self):
        self.assertEqual(sync_content.permalink_to_url("/blog/"), "/blog/")
        self.assertEqual(sync_content.permalink_to_url("/alternatives/"), "/alternatives/")


class NameSlugTests(unittest.TestCase):
    def test_dot_becomes_a_single_dash(self):
        self.assertEqual(sync_content.name_slug("1inch.exchange"), "1inch-exchange")

    def test_uppercase_is_lowered(self):
        self.assertEqual(sync_content.name_slug("APY.Vision"), "apy-vision")

    def test_runs_collapse_and_edges_are_trimmed(self):
        self.assertEqual(sync_content.name_slug("Summer.fi"), "summer-fi")
        self.assertEqual(sync_content.name_slug("--Kamino  Finance--"), "kamino-finance")


class YoutubeIdTests(unittest.TestCase):
    def test_plain_watch_url(self):
        self.assertEqual(
            sync_content.youtube_id("https://www.youtube.com/watch?v=qQQkn361niI"),
            "qQQkn361niI",
        )

    def test_watch_url_with_extra_parameters(self):
        self.assertEqual(
            sync_content.youtube_id(
                "https://www.youtube.com/watch?v=T_P4ZiLzF64&list=PLzdnEGRLbpgZ&index=6&t=471s"
            ),
            "T_P4ZiLzF64",
        )

    def test_short_youtu_be_url(self):
        self.assertEqual(sync_content.youtube_id("https://youtu.be/c04eIt3FQ5I"), "c04eIt3FQ5I")

    def test_unrecognised_url_raises(self):
        with self.assertRaises(sync_content.SyncError):
            sync_content.youtube_id("https://vimeo.com/12345")


class ShortcodeConversionTests(unittest.TestCase):
    def test_youtube_tag_becomes_hugo_shortcode(self):
        body = 'before\n{% youtube "https://youtu.be/c04eIt3FQ5I" %}\nafter\n'
        self.assertEqual(
            sync_content.convert_shortcodes(body),
            "before\n{{< youtube c04eIt3FQ5I >}}\nafter\n",
        )

    def test_single_line_figure_include(self):
        body = '{% include figure.html image="/images/a.png" position="center" height="300" %}\n'
        self.assertEqual(
            sync_content.convert_shortcodes(body),
            '{{< figure image="/images/a.png" position="center" height="300" >}}\n',
        )

    def test_multi_line_figure_include(self):
        body = (
            "intro\n\n"
            "{% include figure.html\n"
            '  image="/images/blog/saving-account-future-idea.png"\n'
            '  position="center"\n'
            '  height="300"\n'
            "%}\n\n"
            "outro\n"
        )
        self.assertEqual(
            sync_content.convert_shortcodes(body),
            "intro\n\n"
            '{{< figure image="/images/blog/saving-account-future-idea.png" '
            'position="center" height="300" >}}\n\n'
            "outro\n",
        )

    def test_multi_line_tweet_include_becomes_tweetcard(self):
        body = (
            "{% include tweet.html\n"
            '  name="Dima Gusakov"\n'
            '  handle="d_gusakov"\n'
            '  date="April 28, 2026"\n'
            '  link="https://x.com/d_gusakov/status/2049089784459543008"\n'
            '  body="If we cut @ethereum staking issuance, we will likely kill LSTs."\n'
            "%}\n"
        )
        self.assertEqual(
            sync_content.convert_shortcodes(body),
            '{{< tweetcard name="Dima Gusakov" handle="d_gusakov" date="April 28, 2026" '
            'link="https://x.com/d_gusakov/status/2049089784459543008" '
            'body="If we cut @ethereum staking issuance, we will likely kill LSTs." >}}\n',
        )

    def test_conversion_output_carries_no_liquid(self):
        body = '{% youtube "https://youtu.be/abc" %}\n{% include tweet.html name="a" %}\n'
        self.assertNotIn("{%", sync_content.convert_shortcodes(body))


class FrontMatterConversionTests(unittest.TestCase):
    def render(self, text, **kwargs):
        entries = sync_content.parse_front_matter(text)
        return sync_content.render_front_matter(sync_content.convert_entries(entries, **kwargs))

    def test_layout_list_form_is_flattened(self):
        self.assertIn("layout: blog\n", self.render("layout: [blog]\ntitle: A"))

    def test_redirect_from_becomes_aliases_with_the_list_intact(self):
        out = self.render("title: A\nredirect_from:\n  - posbakerz\n  - /sdpsaver\n")
        self.assertIn("aliases:\n  - /posbakerz\n  - /sdpsaver\n", out)
        self.assertNotIn("redirect_from", out)

    def test_permalink_becomes_url(self):
        out = self.render("permalink: aave\ntitle: A")
        self.assertIn("url: /aave.html\n", out)
        self.assertNotIn("permalink", out)

    def test_type_is_renamed_only_when_asked(self):
        kept = self.render("type: non-custodial\n")
        renamed = self.render("type: non-custodial\n", rename_type=True)
        self.assertIn("type: non-custodial\n", kept)
        self.assertNotIn("product-type", kept)
        self.assertIn("product-type: non-custodial\n", renamed)

    def test_filter_by_type_token_is_renamed(self):
        out = self.render("filter-by: ecosystem, platform, type, filter\n", rename_type=True)
        self.assertIn("filter-by: ecosystem, platform, product-type, filter\n", out)

    def test_pagination_block_is_dropped_when_asked(self):
        out = self.render(
            "title: A\npagination:\n  enabled: true\n  category: blog\nurl: /blog/\n",
            drop_pagination=True,
        )
        self.assertNotIn("pagination", out)
        self.assertIn("title: A\n", out)
        self.assertIn("url: /blog/\n", out)


if __name__ == "__main__":
    unittest.main()
