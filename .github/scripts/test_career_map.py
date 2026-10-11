#!/usr/bin/env python3
"""Career-map regressions. Run: python3 -I -B .github/scripts/test_career_map.py."""
import copy
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".github/scripts/career_map.py"
RENDER = runpy.run_path(str(SCRIPT))
DATA = json.loads((ROOT / "career-map.json").read_text(encoding="utf-8"))
saved = sys.argv
sys.argv = ["generator", str(ROOT)]
try:
    GEN = runpy.run_path(str(SCRIPT.with_name("generate-profile-svgs.py")))
finally:
    sys.argv = saved
THEMES = GEN["THEMES"]
NS = "{http://www.w3.org/2000/svg}"


class PageParser(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids, self.fragments, self.scripts, self.external_scripts = [], [], [], []
        self.in_script = False
        self.table_rows, self.row, self.cell = [], [], None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr":
            self.row = []
        if tag in ("th", "td"):
            self.cell = []
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if attrs.get("href", "").startswith("#"):
            self.fragments.append(attrs["href"][1:])
        if tag == "script":
            self.in_script = True
            if "src" in attrs:
                self.external_scripts.append(attrs["src"])

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False
        if tag in ("th", "td") and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        if tag == "tr":
            self.table_rows.append(self.row)

    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)
        if self.cell is not None:
            self.cell.append(data)


def expected_text_rows(data):
    return [[" ".join(value.split()) for value in (name, detail, ", ".join(skills) or "—")]
            for _, name, detail, skills in RENDER["detail_rows"](data)]


def readme_text_rows():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    fallback = readme.split("<summary><b>Career details — text version</b></summary>", 1)[1].split("</details>", 1)[0]
    lines = [line for line in fallback.splitlines() if line.startswith("|")]
    return [[" ".join(cell.split()) for cell in line.strip("|").split("|")] for line in lines[2:]]


class CareerMapTests(unittest.TestCase):
    def renders(self):
        for mode, theme in THEMES.items():
            for compact in (False, True):
                yield mode, compact, RENDER["render_career_svg"](theme, DATA, compact)

    def test_well_formed_accessible_variants(self):
        for mode, compact, svg in self.renders():
            with self.subTest(mode=mode, compact=compact):
                root = ET.fromstring(svg)
                self.assertEqual(root.tag, NS + "svg")
                self.assertEqual(root.get("viewBox"), "0 0 480 1450" if compact else "0 0 900 654")
                self.assertEqual(root.get("role"), "img")
                ids = {e.get("id"): e for e in root.iter() if e.get("id")}
                for ref in root.get("aria-labelledby").split():
                    self.assertTrue(ids[ref].text)
                self.assertLess(len(svg.encode()), 22_000)

    def test_six_named_cards_and_three_identity_shapes(self):
        for mode, compact, svg in self.renders():
            with self.subTest(mode=mode, compact=compact):
                root = ET.fromstring(svg)
                cards = list(root.iter(NS + "a"))
                self.assertEqual([a.get("data-detail") for a in cards],
                                 ["bangkok", "invercargill", "raleigh", "education", "industry", "community"])
                for card in cards:
                    self.assertTrue(card.find(NS + "title").text)
                for label in ("Education", "Industry", "Community"):
                    self.assertIn(label, svg)
                marks = [e for e in root.iter(NS + "g") if "cm-mark" in e.get("class", "")]
                self.assertEqual({list(e)[0].tag for e in marks}, {NS + "circle", NS + "rect", NS + "path"})

    def test_svg_is_self_contained(self):
        for _, _, svg in self.renders():
            root = ET.fromstring(svg)
            banned = {"script", "image", "foreignObject", "animate", "animateMotion", "feImage"}
            for e in root.iter():
                self.assertNotIn(e.tag.removeprefix(NS), banned)
                self.assertFalse(any(k.lower().startswith("on") for k in e.attrib))
                if "href" in e.attrib:
                    self.assertTrue(e.get("href").startswith("#detail-"))
            for bad in ("data:", "base64", "@import", "<iframe"):
                self.assertNotIn(bad, svg)

    def test_motion_is_css_and_reduced_motion_is_static(self):
        for _, _, svg in self.renders():
            self.assertIn("@keyframes cm-flow", svg)
            self.assertIn("@keyframes cm-beacon", svg)
            self.assertIn("prefers-reduced-motion:reduce", svg)
            self.assertIn("animation:none!important", svg)
            self.assertNotIn("opacity:0;", svg)  # disabling motion must not hide nodes
            self.assertIn("animation:cm-flow 4s linear 1;", svg)
            self.assertIn("animation:cm-beacon 4s ease-in-out 1;", svg)
            self.assertNotIn("infinite", svg)

    def test_continuous_motion_requires_working_page_controls(self):
        page = RENDER["render_career_page"](DATA, THEMES)
        self.assertIn('[data-motion="on"] .career-viz .cm-flow {animation:cm-flow 8s linear infinite;}', page)
        self.assertIn('[data-motion="on"] .career-viz .cm-beacon {animation:cm-beacon 4s ease-in-out infinite;}', page)
        self.assertNotRegex(page, r'<html[^>]*data-motion=')
        script = PageParser(page).scripts[0]
        enabled = script.index("root.dataset.motion = 'on'")
        self.assertLess(script.index("getElementById('motion').addEventListener('click'"), enabled)
        self.assertLess(script.index("querySelector('.controls').hidden = false"), enabled)

    def test_page_exposes_interactive_svg_groups(self):
        page = RENDER["render_career_page"](DATA, THEMES)
        for svg in re.findall(r"<svg\b.*?</svg>", page, re.DOTALL):
            root = ET.fromstring(svg)
            self.assertEqual(root.get("role"), "group")
            self.assertEqual(len(list(root.iter(NS + "a"))), 6)
        self.assertEqual(len(re.findall(r'<svg\b', page)), 2)

    def test_assets_and_page_match_renderer(self):
        for mode, compact, svg in self.renders():
            name = f"career{'-mobile' if compact else ''}-{mode}.svg"
            self.assertEqual((ROOT / "assets/profile" / name).read_text(encoding="utf-8"), svg)
        self.assertEqual((ROOT / "career/index.html").read_text(encoding="utf-8"),
                         RENDER["render_career_page"](DATA, THEMES))

    def test_theme_changes_color_not_facts(self):
        light = ET.fromstring(RENDER["render_career_svg"](THEMES["light"], DATA))
        dark = ET.fromstring(RENDER["render_career_svg"](THEMES["dark"], DATA))
        self.assertEqual([e.text for e in light.iter(NS + "text")], [e.text for e in dark.iter(NS + "text")])
        self.assertNotEqual(light.find(NS + "style").text, dark.find(NS + "style").text)

    def test_facts_and_tools_survive_in_both_text_views(self):
        page = RENDER["render_career_page"](DATA, THEMES)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        expected = expected_text_rows(DATA)
        self.assertEqual(PageParser(page).table_rows[1:], expected)
        self.assertEqual(readme_text_rows(), expected)
        for dates in ("2010–2012", "2012–2015", "2018–2021", "2016–2021", "2015"):
            self.assertIn(dates, page)
            self.assertIn(dates, readme)
        self.assertTrue(all("dates" not in job for job in DATA["industry"]))
        self.assertIn("Employment dates are unspecified", readme)

    def test_fallback_comparison_catches_semantic_drift(self):
        for key, fields in (("education", ("name", "qualification", "dates")),
                            ("industry", ("role", "context", "focus")),
                            ("community", ("role", "focus")),
                            ("places", ("country", "summary"))):
            for field in fields:
                data = copy.deepcopy(DATA)
                data[key][0][field] = "Changed fact"
                with self.subTest(key=key, field=field):
                    self.assertNotEqual(readme_text_rows(), expected_text_rows(data))
        data = copy.deepcopy(DATA)
        data["projects"]["focus"] = "Changed project focus"
        self.assertNotEqual(readme_text_rows(), expected_text_rows(data))

    def test_new_branches_require_explicit_layout_change(self):
        for key in ("places", "education", "industry", "community"):
            data = copy.deepcopy(DATA)
            data[key].append(copy.deepcopy(data[key][0]))
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "update the layout"):
                RENDER["render_career_svg"](THEMES["light"], data)

    def test_curated_source_drives_visual_roles_and_dates(self):
        data = copy.deepcopy(DATA)
        data["industry"][0]["role"] = "Example role"
        data["education"][0]["dates"] = "Example dates"
        data["community"][0]["role"] = "Example maintainer"
        svg = RENDER["render_career_svg"](THEMES["light"], data)
        for value in ("Example role", "Example dates", "example maintainer"):
            self.assertIn(value, svg)

    def test_page_ids_and_fragment_targets_work_without_js(self):
        parser = PageParser(RENDER["render_career_page"](DATA, THEMES))
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        self.assertTrue(parser.fragments)
        for fragment in parser.fragments:
            self.assertIn(fragment, parser.ids)
        self.assertFalse(parser.external_scripts)

    def test_input_labels_are_escaped(self):
        data = copy.deepcopy(DATA)
        data["places"][0]["city"] = '<script>alert("x")</script> & city'
        data["places"][0]["id"] = 'test"><script>alert("x")</script>'
        svg = RENDER["render_career_svg"](THEMES["light"], data)
        self.assertIn("&lt;script&gt;", svg)
        ET.fromstring(svg)
        page = RENDER["render_career_page"](data, THEMES)
        self.assertEqual(len(PageParser(page).scripts), 1)
        self.assertNotIn('alert("x")</script>', page)

    def test_isolated_stdlib_only_generation(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "career-map.json").write_text(json.dumps(DATA), encoding="utf-8")
            code = ("import runpy,sys;sys.argv=['g',%r];m=runpy.run_path(%r);"
                    "m['generate_career_assets']()" % (td, str(SCRIPT.with_name("generate-profile-svgs.py"))))
            subprocess.run([sys.executable, "-I", "-B", "-S", "-c", code], check=True, capture_output=True)
            for path in (Path(td) / "assets/profile").glob("*.svg"):
                self.assertEqual(path.read_bytes(), (ROOT / "assets/profile" / path.name).read_bytes())
            self.assertEqual((Path(td) / "career/index.html").read_bytes(), (ROOT / "career/index.html").read_bytes())


if __name__ == "__main__":
    unittest.main()
