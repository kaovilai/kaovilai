#!/usr/bin/env python3
"""World-map regressions. Run: python3 -I -B .github/scripts/test_worldmap.py."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".github/scripts/worldmap.py"
DATA = ROOT / "data/places.json"


def load_module():
    spec = importlib.util.spec_from_file_location("worldmap", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WM = load_module()
NS = "{http://www.w3.org/2000/svg}"


def android_export(segments):
    return json.dumps({"semanticSegments": segments, "rawSignals": []})


def visit_segment(start, latlng, place_id="ChIJsecret", address="1 Secret Street"):
    return {
        "startTime": start,
        "endTime": start,
        "visit": {
            "hierarchyLevel": 0,
            "probability": 0.9,
            "topCandidate": {
                "placeId": place_id,
                "semanticType": "UNKNOWN",
                "probability": 0.9,
                "placeLocation": {"latLng": latlng},
                "address": address,
            },
        },
    }


class CoordinateTests(unittest.TestCase):
    def test_parse_shapes(self):
        cases = {
            "geo:37.4,-122.0": (37.4, -122.0),
            "50.0506312°, 14.3439906°": (50.0506312, 14.3439906),
            "geo:13.75,100.5": (13.75, 100.5),
        }
        for value, expected in cases.items():
            self.assertEqual(WM.parse_latlng(value), expected)
        self.assertAlmostEqual(
            WM.parse_latlng({"latitudeE7": 377718000, "longitudeE7": -1224194000})[0],
            37.7718,
        )
        self.assertAlmostEqual(
            WM.parse_latlng({"point": "geo:-46.4,168.35"})[0], -46.4
        )
        self.assertIsNone(WM.parse_latlng(None))
        self.assertIsNone(WM.parse_latlng("not a coordinate"))

    def test_year_shapes(self):
        self.assertEqual(WM.year_of("2019-06-01T10:00:00.000-04:00"), 2019)
        self.assertEqual(WM.year_of(1559408400000), 2019)
        self.assertEqual(WM.year_of("1559408400000"), 2019)
        self.assertIsNone(WM.year_of(None))


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def run_import(self, text, name="Timeline.json", extra=()):
        source = self.dir / name
        source.write_text(text, encoding="utf-8")
        out = self.dir / "places.json"
        WM.main(["import", str(source), "--out", str(out), *extra])
        return json.loads(out.read_text(encoding="utf-8"))

    def test_android_export_and_pii_stripping(self):
        document = android_export(
            [
                visit_segment("2019-06-01T10:00:00.000-04:00", "35.7796000°, -78.6382000°"),
                visit_segment("2019-06-03T10:00:00.000-04:00", "35.7796000°, -78.6382000°"),
                visit_segment("2021-03-01T10:00:00.000+13:00", "geo:-46.4132,168.3538"),
            ]
        )
        result = self.run_import(document)
        cities = {(c["city"], c["country_code"]): c for c in result["cities"]}
        self.assertIn(("Raleigh", "US"), cities)
        self.assertIn(("Invercargill", "NZ"), cities)
        self.assertEqual(cities[("Raleigh", "US")]["visits"], 2)
        self.assertEqual(cities[("Raleigh", "US")]["first_year"], 2019)

        raw = (self.dir / "places.json").read_text(encoding="utf-8")
        for leaked in ("35.7796", "-78.6382", "ChIJsecret", "1 Secret Street"):
            self.assertNotIn(leaked, raw)
        # Published coordinates are gazetteer city centres, not samples.
        self.assertEqual(cities[("Raleigh", "US")]["lat"], 35.77)

    def test_concatenated_yearly_objects(self):
        first = android_export(
            [visit_segment("2019-06-01T10:00:00.000-04:00", "geo:13.7563,100.5018")]
        )
        second = android_export(
            [visit_segment("2020-06-01T10:00:00.000-04:00", "geo:35.7796,-78.6382")]
        )
        result = self.run_import(first + "\n" + second)
        self.assertEqual(len(result["cities"]), 2)

    def test_iphone_export(self):
        document = [
            {
                "startTime": "2022-01-05T08:00:00.000-08:00",
                "endTime": "2022-01-05T09:00:00.000-08:00",
                "visit": {"topCandidate": {"placeLocation": "geo:37.7749,-122.4194"}},
            },
            {
                "startTime": "2022-01-06T08:00:00.000-08:00",
                "endTime": "2022-01-06T09:00:00.000-08:00",
                "activity": {"start": {"latLng": "geo:37.7749,-122.4194"}, "end": {"latLng": "geo:34.0522,-118.2437"}},
            },
        ]
        result = self.run_import(json.dumps(document), name="location-history.json")
        cities = {c["city"] for c in result["cities"]}
        self.assertIn("San Francisco", cities)
        self.assertIn("Los Angeles", cities)

    def test_legacy_records(self):
        document = {
            "locations": [
                {"latitudeE7": 357796000, "longitudeE7": -786382000, "timestampMs": "1559408400000"},
                {"latitudeE7": 357796000, "longitudeE7": -786382000, "timestampMs": "1559494800000"},
            ]
        }
        result = self.run_import(json.dumps(document), name="Records.json")
        cities = {c["city"]: c for c in result["cities"]}
        self.assertEqual(cities["Raleigh"]["days"], 2)

    def test_legacy_semantic_history(self):
        document = {
            "timelineObjects": [
                {
                    "placeVisit": {
                        "location": {
                            "latitudeE7": 137563000,
                            "longitudeE7": 1005018000,
                            "name": "Secret Place",
                            "address": "Secret Address",
                        },
                        "duration": {"startTimestampMs": "1559408400000"},
                    }
                }
            ]
        }
        result = self.run_import(
            json.dumps(document), name="2021_JANUARY.json"
        )
        self.assertEqual(result["cities"][0]["city"], "Bangkok")

    def test_unmatched_samples_are_dropped(self):
        document = android_export(
            [visit_segment("2019-06-01T10:00:00.000-04:00", "geo:0.0,-140.0")]
        )
        with self.assertRaises(SystemExit):
            self.run_import(document)

    def test_min_visits_filter(self):
        document = android_export(
            [
                visit_segment("2019-06-01T10:00:00.000-04:00", "geo:35.7796,-78.6382"),
                visit_segment("2019-06-02T10:00:00.000-04:00", "geo:13.7563,100.5018"),
                visit_segment("2019-06-03T10:00:00.000-04:00", "geo:13.7563,100.5018"),
            ]
        )
        result = self.run_import(document, extra=("--min-visits", "2"))
        self.assertEqual([c["city"] for c in result["cities"]], ["Bangkok"])


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.cities = [
            {
                "city": "Raleigh",
                "region": "North Carolina",
                "country": "United States of America",
                "country_code": "US",
                "lat": 35.77,
                "lon": -78.65,
                "visits": 3,
                "days": 2,
                "first_year": 2016,
                "last_year": 2026,
            },
            {
                "city": "Bangkok",
                "region": "Bangkok Metropolis",
                "country": "Thailand",
                "country_code": "TH",
                "lat": 13.75,
                "lon": 100.52,
                "visits": 1,
                "days": 1,
                "first_year": 2010,
                "last_year": 2012,
            },
        ]
        self.land = WM.load_land()
        self.borders = WM.load_borders()

    def test_svg_is_valid_and_has_a_dot_per_city(self):
        svg = WM.render_svg(self.cities, self.land, "light", borders=self.borders)
        root = ET.fromstring(svg)
        circles = list(root.iter(NS + "circle"))
        self.assertEqual(len(circles), len(self.cities))
        self.assertEqual(root.get("width"), "1280")
        self.assertIn("Travel map", ET.tostring(root, encoding="unicode"))

    def test_render_is_deterministic_and_themed(self):
        light = WM.render_svg(self.cities, self.land, "light", borders=self.borders)
        again = WM.render_svg(self.cities, self.land, "light", borders=self.borders)
        dark = WM.render_svg(self.cities, self.land, "dark", borders=self.borders)
        self.assertEqual(light, again)
        self.assertNotEqual(light, dark)
        self.assertIn(WM.THEMES["dark"]["ocean"], dark)

    def test_no_nan_in_output(self):
        svg = WM.render_svg(self.cities, self.land, "light", borders=self.borders)
        self.assertNotIn("nan", svg.lower())
        self.assertNotIn("inf", svg.lower())

    def test_animated_svg_is_valid_and_self_contained(self):
        svg = WM.render_animated_svg(
            self.cities, self.land, "dark", borders=self.borders
        )
        root = ET.fromstring(svg)
        # One halo + one dot per city, one leg per consecutive pair.
        self.assertEqual(len(list(root.iter(NS + "circle"))), 2 * len(self.cities))
        self.assertIn("@keyframes leg0", svg)
        self.assertIn("prefers-reduced-motion", svg)
        self.assertIn("animation-name:leg0", svg)
        self.assertNotIn("<script", svg.lower())
        self.assertNotIn("xlink:href", svg)
        # The only absolute URL allowed is the SVG namespace.
        for chunk in svg.split("http")[1:]:
            self.assertTrue(chunk.startswith("://www.w3.org/"), chunk[:40])

    def test_animated_render_is_deterministic(self):
        first = WM.render_animated_svg(
            self.cities, self.land, "dark", borders=self.borders
        )
        second = WM.render_animated_svg(
            self.cities, self.land, "dark", borders=self.borders
        )
        self.assertEqual(first, second)
        light = WM.render_animated_svg(
            self.cities, self.land, "light", borders=self.borders
        )
        self.assertNotEqual(first, light)

    def test_animated_single_city_has_no_legs(self):
        svg = WM.render_animated_svg(
            self.cities[:1], self.land, "dark", borders=self.borders
        )
        root = ET.fromstring(svg)
        self.assertEqual(len(list(root.iter(NS + "circle"))), 2)
        self.assertNotIn("@keyframes leg0", svg)


class CommittedArtifactTests(unittest.TestCase):
    def test_places_json_schema(self):
        if not DATA.exists():
            self.skipTest("data/places.json not generated yet")
        document = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(document["schema"], WM.PLACES_SCHEMA)
        for city in document["cities"]:
            self.assertLessEqual(abs(city["lat"]), 90)
            self.assertLessEqual(abs(city["lon"]), 180)
            self.assertEqual(city["lat"], round(city["lat"], 2))
            self.assertEqual(city["lon"], round(city["lon"], 2))

    def test_committed_svgs_match_data(self):
        if not DATA.exists():
            self.skipTest("data/places.json not generated yet")
        cities = json.loads(DATA.read_text(encoding="utf-8"))["cities"]
        land = WM.load_land()
        borders = WM.load_borders()
        for theme in ("light", "dark"):
            expected_files = {
                f"worldmap-{theme}.svg": WM.render_svg(
                    cities, land, theme, borders=borders
                ),
                f"worldmap-animated-{theme}.svg": WM.render_animated_svg(
                    cities, land, theme, borders=borders
                ),
            }
            for name, expected in expected_files.items():
                svg_path = ROOT / name
                if not svg_path.exists():
                    self.skipTest(f"{name} not generated yet")
                self.assertEqual(
                    svg_path.read_text(encoding="utf-8"),
                    expected,
                    f"{name} is stale; rerun worldmap.py render",
                )

    def test_gazetteer_is_consistent(self):
        cities = WM.load_cities()
        self.assertGreater(len(cities), 5000)
        for row in cities:
            self.assertEqual(len(row), 7)
            self.assertLessEqual(abs(row[WM.CITY_LAT]), 90)
            self.assertLessEqual(abs(row[WM.CITY_LON]), 180)


if __name__ == "__main__":
    unittest.main()
