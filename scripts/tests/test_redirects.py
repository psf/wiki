"""Behavioral coverage for legacy wiki bookmarks (stdlib-only)."""

from __future__ import annotations

import json
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin

from scripts.gen_redirect_pages import generate_redirects


class _RedirectLink(HTMLParser):
    target: str | None = None

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.target = dict(attrs).get("href")


class LegacyRedirectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def generate(self, mappings, pages):
        (self.root / "_redirects.json").write_text(json.dumps(mappings))
        for name in pages:
            page = self.root / f"{name}.md"
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text("# Page\n")
        generate_redirects(self.root)

    def destination(self, source):
        parser = _RedirectLink()
        parser.feed((self.root / "_redirects_html" / f"{source}.html").read_text())
        self.assertIsNotNone(parser.target)
        return unquote(urljoin(f"https://wiki.python.org/{source}.html", parser.target))

    def test_public_bookmarks_follow_moves_to_final_destination(self):
        self.generate(
            {
                "python/BeginnersGuide/NonProgrammers": "python/getting-started/NonProgrammers",
                "python/BeginnersGuide(2f)NonProgrammers": "python/BeginnersGuide/NonProgrammers",
                "python/getting-started/NonProgrammers": "python/learn/NonProgrammers",
            },
            ["python/learn/NonProgrammers"],
        )
        for source in (
            "moin/BeginnersGuide/NonProgrammers",
            "moin/BeginnersGuide(2f)NonProgrammers",
            "python/BeginnersGuide/NonProgrammers",
        ):
            with self.subTest(source=source):
                self.assertEqual(self.destination(source), "https://wiki.python.org/python/learn/NonProgrammers.html")

    def test_unchanged_pages_and_wiki_root_get_public_aliases(self):
        self.generate({}, ["python/index", "python/UnmovedPage"])
        self.assertEqual(self.destination("moin/UnmovedPage"), "https://wiki.python.org/python/UnmovedPage.html")
        self.assertEqual(self.destination("moin/index"), "https://wiki.python.org/python/index.html")

    def test_explicit_public_alias_takes_precedence(self):
        self.generate(
            {"moin/SharedName": "psf/about/SharedName"},
            ["python/SharedName", "psf/about/SharedName"],
        )
        self.assertEqual(self.destination("moin/SharedName"), "https://wiki.python.org/psf/about/SharedName.html")

    def test_parent_bookmark_is_not_shadowed_by_subpage_directory(self):
        self.generate(
            {"python/Guide": "python/learn/Guide", "python/Guide/Child": "python/learn/Guide/Child"},
            ["python/learn/Guide", "python/learn/Guide/index", "python/learn/Guide/Child"],
        )
        self.assertEqual(self.destination("moin/Guide/index"), "https://wiki.python.org/python/learn/Guide.html")
        self.assertEqual(self.destination("moin/learn/Guide/index"), "https://wiki.python.org/python/learn/Guide.html")

    def test_special_characters_remain_part_of_the_target_path(self):
        target = "python/guides/Beginner's guide & café #1"
        self.generate({"python/SpecialPage": target}, [target])
        self.assertEqual(self.destination("moin/SpecialPage"), f"https://wiki.python.org/{target}.html")
        parser = _RedirectLink()
        parser.feed((self.root / "_redirects_html/moin/SpecialPage.html").read_text())
        self.assertNotIn("#", parser.target)
        self.assertNotIn("'", parser.target)


if __name__ == "__main__":
    unittest.main()
