#!/usr/bin/env python3
"""Tests for the Bojangles SVG in generate-profile-svgs.py.

Run: python3 -I .github/scripts/test_bojangles.py   (any cwd)
Renders the SVG in-process (no repo data needed) and checks it is well-formed,
self-contained, deterministic, in sync with the committed assets, and that the
CSS timeline tells the story: nibble, leap, wall slip, paws-first landing, walk on.
"""
import importlib.util
import json
import re
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parent / "generate-profile-svgs.py"
REPO = SCRIPT.parents[2]
SIZE_BUDGET = 150_000  # bytes per theme, including photo-derived vector contours
NS = "{http://www.w3.org/2000/svg}"


def load_generator():
    sys.dont_write_bytecode = True
    saved = sys.argv
    sys.argv = [str(SCRIPT)]  # the generator reads ROOT from argv at import time
    try:
        spec = importlib.util.spec_from_file_location("generate_profile_svgs", SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.argv = saved
    return mod


GEN = load_generator()
THEMES = sorted(GEN.THEMES)
RENDERS = {mode: GEN.bojangles(GEN.THEMES[mode], None) for mode in THEMES}
DURATION = GEN.BOJANGLES_STORY[-1][0]


def parse_blocks(css):
    """Split CSS into top-level (prelude, body) blocks, keeping nested braces in body."""
    blocks, depth, start, prelude_start = [], 0, 0, 0
    for i, ch in enumerate(css):
        if ch == "{":
            if depth == 0:
                prelude, start = css[prelude_start:i].strip(), i + 1
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                blocks.append((prelude, css[start:i]))
                prelude_start = i + 1
    assert depth == 0, "unbalanced braces in CSS"
    return blocks


def style_of(svg):
    root = ET.fromstring(svg)
    styles = [e.text or "" for e in root.iter(NS + "style")]
    assert len(styles) == 1
    return styles[0]


def keyframes(css, name):
    """[(percent, declarations)] for a single-percentage-per-frame @keyframes block."""
    for prelude, body in parse_blocks(css):
        if prelude == f"@keyframes {name}":
            frames = []
            for sel, decl in re.findall(r"([^{}]+)\{([^}]*)\}", body):
                for part in sel.split(","):
                    part = part.strip()
                    pct = {"from": 0.0, "to": 100.0}.get(part)
                    if pct is None:
                        assert part.endswith("%"), f"{name}: bad selector {part!r}"
                        pct = float(part[:-1])
                    frames.append((pct, decl.strip()))
            return frames
    raise AssertionError(f"@keyframes {name} not defined")


def animation_rules(css):
    """[(classes, name, duration_s, value)] for every top-level rule with an animation."""
    rules = []
    for prelude, body in parse_blocks(css):
        m = re.search(r"animation:\s*([^;}]+)", body)
        if prelude.startswith(".") and m:
            value = m.group(1).strip()
            tokens = value.split()
            classes = [s.strip().lstrip(".") for s in prelude.split(",")]
            rules.append((classes, tokens[0], float(tokens[1].rstrip("s")), value))
    return rules


def class_set(svg):
    classes = set()
    for e in ET.fromstring(svg).iter():
        classes.update(e.get("class", "").split())
    return classes


def num_args(value):
    return [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", value)]


def track_samples(css, name):
    """[(seconds, first-number-list)] for a story-clock transform track."""
    return [(pct * DURATION / 100, num_args(decl)) for pct, decl in keyframes(css, name)]


def value_at(samples, sec):
    """Piecewise-linear value at `sec` (numbers per sample)."""
    prev = samples[0]
    for cur in samples[1:]:
        if cur[0] >= sec:
            span = cur[0] - prev[0]
            f = 0 if span == 0 else (sec - prev[0]) / span
            return [a + (b - a) * f for a, b in zip(prev[1], cur[1])]
        prev = cur
    return samples[-1][1]


class RenderTests(unittest.TestCase):
    def test_both_themes_render_and_parse(self):
        self.assertEqual(THEMES, ["dark", "light"])
        for mode, svg in RENDERS.items():
            with self.subTest(mode):
                root = ET.fromstring(svg)
                self.assertEqual(root.tag, NS + "svg")
                self.assertEqual(root.get("role"), "img")
                self.assertEqual(root.get("viewBox"), "0 0 900 340")
                self.assertNotRegex(svg, r"\b(?:nan|inf|None)\b")

    def test_themes_differ_but_share_the_story(self):
        dark, light = RENDERS["dark"], RENDERS["light"]
        self.assertNotEqual(dark, light)
        self.assertIn(GEN.THEMES["dark"]["bg1"], dark)
        self.assertIn(GEN.THEMES["light"]["bg1"], light)
        self.assertEqual(
            keyframes(style_of(dark), "bj-travel"), keyframes(style_of(light), "bj-travel")
        )

    def test_size_budget(self):
        for mode, svg in RENDERS.items():
            with self.subTest(mode):
                self.assertLessEqual(len(svg.encode("utf-8")), SIZE_BUDGET)

    def test_accessibility_labels(self):
        for mode, svg in RENDERS.items():
            with self.subTest(mode):
                root = ET.fromstring(svg)
                ids = {e.get("id"): e for e in root.iter() if e.get("id")}
                labelled = root.get("aria-labelledby").split()
                self.assertEqual(len(labelled), 2)
                for ref in labelled:
                    self.assertIn(ref, ids)
                    self.assertTrue((ids[ref].text or "").strip())
                self.assertIn("Bojangles", ids[labelled[0]].text)
                desc = ids[labelled[1]].text.lower()
                for word in ("catnip", "fish", "wall", "paws", "reduced motion"):
                    self.assertIn(word, desc)

    def test_ids_unique_and_references_local(self):
        for mode, svg in RENDERS.items():
            with self.subTest(mode):
                root = ET.fromstring(svg)
                ids = [e.get("id") for e in root.iter() if e.get("id")]
                self.assertEqual(len(ids), len(set(ids)), "duplicate id")
                refs = re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", svg)
                self.assertTrue(refs)
                for ref in refs:
                    self.assertTrue(ref.startswith("#"), f"non-local url({ref})")
                    self.assertIn(ref[1:], ids, f"dangling url({ref})")
                for e in root.iter():
                    for key, value in e.attrib.items():
                        if key.endswith("href"):
                            self.assertTrue(value.startswith("#") and value[1:] in ids, f"bad {key}={value}")

    def test_self_contained_and_static_safe(self):
        banned_tags = {"script", "image", "foreignObject", "animate", "set", "animateTransform",
                       "animateMotion", "mpath", "feImage", "iframe", "object", "embed",
                       "video", "audio"}
        for mode, svg in RENDERS.items():
            with self.subTest(mode):
                root = ET.fromstring(svg)
                for e in root.iter():
                    self.assertNotIn(e.tag.replace(NS, ""), banned_tags)
                    for key in e.attrib:
                        self.assertFalse(key.lower().startswith("on"), f"event handler {key}")
                stripped = svg.replace('xmlns="http://www.w3.org/2000/svg"', "")
                for needle in ("http:", "https:", "//", "data:", "@import", "@font-face",
                               "javascript:", "<?xml-stylesheet", "base64"):
                    self.assertNotIn(needle, stripped)


class FaceArtworkTests(unittest.TestCase):
    def test_unreadable_artwork_has_context(self):
        for error in (FileNotFoundError("missing"), json.JSONDecodeError("invalid", "{", 1)):
            with self.subTest(error=type(error).__name__):
                with patch.object(Path, "read_text", side_effect=error):
                    with self.assertRaisesRegex(ValueError, r"Cannot load Bojangles vector artwork.*bojangles-face\.json"):
                        GEN.bojangles(GEN.THEMES["dark"], None)

    def test_source_contains_only_vector_geometry(self):
        face = json.loads((REPO / ".github/artwork/bojangles-face.json").read_text(encoding="utf-8"))
        self.assertEqual(set(face), {"viewBox", "outline", "base", "regions", "layers"})
        self.assertEqual(face["viewBox"], [0, 0, 200, 200])
        self.assertEqual(set(face["regions"]), {"ear", "eye-near", "eye-far", "jaw"})
        # Traced paths use nonnegative integer polygons, not decimals or curve commands.
        for d in [face["outline"], face["base"], *face["regions"].values()]:
            self.assertRegex(d, r"^M[0-9, MZ]+Z$")
        self.assertEqual([layer["name"] for layer in face["layers"]],
                         ["head", "ear", "eye-near", "eye-far", "jaw"])
        for layer in face["layers"]:
            self.assertEqual(set(layer), {"name", "paths"})
            self.assertTrue(layer["paths"])
            for path in layer["paths"]:
                self.assertEqual(set(path), {"fill", "d"})
                self.assertRegex(path["fill"], r"^#[0-9a-f]{6}$")
                self.assertRegex(path["d"], r"^M[0-9, MZ]+Z$")

    def test_blink_has_closed_lids_behind_each_eye(self):
        for svg in RENDERS.values():
            root = ET.fromstring(svg)
            for side in ("near", "far"):
                eye = root.find(f".//{NS}g[@id='bj-eye-{side}']")
                self.assertIsNotNone(eye)
                self.assertEqual([e.tag for e in eye], [NS + "path", NS + "path", NS + "g"])
                self.assertNotEqual(eye[0].get("fill"), "none")
                self.assertEqual(eye[2].get("class"), "bj-blink")
                self.assertGreater(len(list(eye[2].iter(NS + "path"))), 1)

    def test_ear_and_jaw_contain_independent_vector_layers(self):
        for svg in RENDERS.values():
            root = ET.fromstring(svg)
            head = root.find(f".//{NS}g[@class='bj-head']")
            self.assertIsNotNone(head)
            for name in ("ear", "jaw"):
                joint = head.find(f".//{NS}g[@class='bj-{name}']")
                self.assertIsNotNone(joint)
                self.assertGreater(len(list(joint.iter(NS + "path"))), 1)


class DeterminismTests(unittest.TestCase):
    def test_repeat_render_identical(self):
        for mode in THEMES:
            with self.subTest(mode):
                self.assertEqual(GEN.bojangles(GEN.THEMES[mode], None), RENDERS[mode])

    def test_fresh_isolated_processes_match(self):
        code = ("import importlib.util,sys;sys.argv=['g'];"
                "s=importlib.util.spec_from_file_location('g',%r);"
                "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
                "sys.stdout.write(m.bojangles(m.THEMES['dark'],None))" % str(SCRIPT))
        outs = []
        for _ in range(2):
            run = subprocess.run([sys.executable, "-I", "-B", "-S", "-c", code], capture_output=True,
                                 text=True, check=True)
            outs.append(run.stdout)
        self.assertEqual(outs[0], outs[1])
        self.assertEqual(outs[0], RENDERS["dark"])

    def test_committed_assets_match_renderer(self):
        for mode, svg in RENDERS.items():
            path = REPO / "assets" / "profile" / f"bojangles-{mode}.svg"
            with self.subTest(mode):
                self.assertTrue(path.exists(), f"{path} missing; run generate-profile-svgs.py")
                self.assertEqual(path.read_text(encoding="utf-8"), svg,
                                 f"{path.name} is stale; regenerate")


class StoryTests(unittest.TestCase):
    def setUp(self):
        self.css = style_of(RENDERS["dark"])
        self.travel = track_samples(self.css, "bj-travel")  # [(sec, [x, y])]
        self.pitch = track_samples(self.css, "bj-pitch")

    def test_story_table_is_chronological_and_loops(self):
        times = [row[0] for row in GEN.BOJANGLES_STORY]
        self.assertEqual(times[0], 0)
        self.assertEqual(times[-1], 40)
        self.assertEqual(times, sorted(times))
        self.assertEqual(len(times), len(set(times)), "duplicate story times")
        first, last = GEN.BOJANGLES_STORY[0], GEN.BOJANGLES_STORY[-1]
        self.assertEqual(first[1:3], last[1:3], "loop must end where it begins")
        self.assertEqual(first[3], last[3])

    def test_css_keyframes_chronological_for_every_story_track(self):
        tracks = [r for r in animation_rules(self.css) if r[2] == DURATION]
        self.assertGreaterEqual(len(tracks), 20)
        for _, name, _, value in tracks:
            with self.subTest(name):
                pcts = [p for p, _ in keyframes(self.css, name)]
                self.assertEqual(pcts[0], 0)
                self.assertEqual(pcts[-1], 100)
                self.assertEqual(pcts, sorted(pcts))
                self.assertEqual(len(pcts), len(set(pcts)), "duplicate keyframe percent")
                self.assertIn("infinite", value)

    def test_transform_tracks_loop_seamlessly(self):
        for classes, name, dur, _ in animation_rules(self.css):
            if dur != DURATION:
                continue
            frames = keyframes(self.css, name)
            if "transform" not in frames[0][1]:
                continue
            with self.subTest(name):
                self.assertEqual(frames[0][1], frames[-1][1])

    def test_travel_matches_story_table(self):
        story = [(r[0], [r[1], r[2]]) for r in GEN.BOJANGLES_STORY]
        self.assertEqual(len(story), len(self.travel))
        for (s_sec, s_val), (c_sec, c_val) in zip(story, self.travel):
            self.assertAlmostEqual(s_sec, c_sec, delta=.01)
            self.assertEqual(s_val, c_val)
        self.assertEqual(self.travel[0][1], self.travel[-1][1])

    def test_nibble_catnip(self):
        flowers_x = 299  # flower bed origin in the SVG
        row = [r for r in GEN.BOJANGLES_STORY if r[4] == "nibble"]
        self.assertTrue(row)
        for _, x, y, _, _ in row:
            self.assertLess(abs(x - flowers_x), 120, "nibbling away from the catnip")
            self.assertEqual(y, 0)
        start, end = row[0][0], row[-1][0]
        # flowers sway and jaw chews only while nibbling, head dips down
        jaw = track_samples(self.css, "bj-jaw")
        self.assertTrue(any(v[0] > 0 for s, v in jaw if start <= s <= end))
        self.assertTrue(all(v[0] == 0 for s, v in jaw if s < start - .01 or s > end + .5))
        flowers = track_samples(self.css, "bj-flowers")
        self.assertTrue(any(v[0] != 0 for s, v in flowers if start <= s <= end))
        self.assertTrue(all(v[0] == 0 for s, v in flowers if s < start - .21 or s > end + .01))
        head = track_samples(self.css, "bj-head")
        self.assertGreater(value_at(head, (start + end) / 2)[0], 5)

    def test_leap_for_fish_toy(self):
        fish_x = 540
        window = [(s, v) for s, v in self.travel if 14 <= s <= 17]
        peak_sec, (peak_x, peak_y) = min(window, key=lambda sv: sv[1][1])
        self.assertLess(peak_y, -50, "no real leap")
        self.assertLess(abs(peak_x + 80 - fish_x), 100, "leap peak not under the fish")
        after = [v for s, v in self.travel if s > peak_sec]
        self.assertEqual(next(v[1] for v in after if v[1] >= 0), 0, "leap must come back to the ground")
        # Leap is announced and landed with a crouch.
        crouch = [r for r in GEN.BOJANGLES_STORY if r[4] == "crouch"]
        self.assertGreaterEqual(len(crouch), 2)

    def test_fish_toy_moves_and_cycle_fits_story(self):
        rules = {name: (dur, value) for _, name, dur, value in animation_rules(self.css)}
        dur, value = rules["bj-fish-sway"]
        cycle = dur * 2 if "alternate" in value else dur
        reps = DURATION / cycle
        self.assertAlmostEqual(reps, round(reps), places=6,
                               msg=f"fish cycle {cycle}s does not divide {DURATION}s loop")
        frames = keyframes(self.css, "bj-fish-sway")
        self.assertNotEqual(frames[0][1], frames[-1][1])

    def test_thin_wall_slip_fall_and_paws_first_landing(self):
        wall_x = 766  # left edge of the drawn wall
        rows = GEN.BOJANGLES_STORY
        cling = [r for r in rows if r[4] == "cling"]
        self.assertTrue(cling)
        for _, x, y, ang, _ in cling:
            self.assertLess(y, -20)
            self.assertLessEqual(ang, -45, "body should be vertical-ish on the wall")
            self.assertLess(wall_x - (x + 80), 20, "paws/head not at the wall")
            self.assertGreater(wall_x - (x + 80), -80)
        top = min(cling, key=lambda r: r[2])
        after = [r for r in rows if r[0] >= top[0]]
        land = next(r for r in after if r[2] == 0)
        slide = [r for r in after if r[0] <= land[0]]
        ys = [r[2] for r in slide]
        self.assertEqual(ys, sorted(ys), "slide must be monotonic down (y rising to ground)")
        self.assertTrue([r for r in rows if r[4] == "fall"])
        self.assertEqual(land[3], 0, "lands level, paws first")
        self.assertEqual(land[4], "stand")
        pitches = [r[3] for r in rows]
        self.assertTrue(all(-90 <= p <= 0 for p in pitches), "cat must never flip over")
        # after landing, a crouch absorbs the impact
        idx = rows.index(land)
        self.assertEqual(rows[idx + 1][4], "crouch")

    def test_walk_windows_face_travel_and_move_at_walking_speed(self):
        facing = keyframes(self.css, "bj-facing")
        def facing_at(sec):
            pct = sec / DURATION * 100
            val = [d for p, d in facing if p <= pct + 1e-6][-1]
            return -1 if "-1" in val else 1
        self.assertEqual(len(GEN.BOJANGLES_WALKS), 4)
        for start, end in GEN.BOJANGLES_WALKS:
            with self.subTest((start, end)):
                x0, x1 = value_at(self.travel, start)[0], value_at(self.travel, end)[0]
                speed = abs(x1 - x0) / (end - start)
                self.assertTrue(15 < speed < 120, f"walk speed {speed:.0f}px/s")
                self.assertEqual(facing_at((start + end) / 2), 1 if x1 > x0 else -1)
                xs = [v[0] for s, v in self.travel if start <= s <= end]
                self.assertEqual(xs, sorted(xs, reverse=x1 < x0))
                for name in ("fore-near", "hind-near"):
                    legs = track_samples(self.css, f"bj-{name}")
                    swings = [v[0] for s, v in legs if start <= s <= end]
                    self.assertGreater(max(swings) - min(swings), 30, "legs do not stride")
                    self.assertAlmostEqual(swings[0], 0, delta=.1)
                    self.assertAlmostEqual(swings[-1], 0, delta=.1)

    def test_return_walk_resumes_after_landing(self):
        walks = GEN.BOJANGLES_WALKS
        land_sec = next(r[0] for r in GEN.BOJANGLES_STORY if r[4] == "stand" and r[1] == 662)
        self.assertLessEqual(land_sec, walks[-1][0])
        self.assertGreater(walks[-1][1] - walks[-1][0], 5, "return walk too short to read as resumed")
        self.assertEqual(value_at(self.travel, walks[-1][1])[0], GEN.BOJANGLES_STORY[0][1])
        self.assertGreater(value_at(self.travel, walks[-1][0])[0], 600)
        # Walk resumes after the wall episode, not before it.
        self.assertGreater(walks[-1][0], max(r[0] for r in GEN.BOJANGLES_STORY if r[4] == "fall"))

    def test_captions_follow_story_order(self):
        css, svg = self.css, RENDERS["dark"]
        root = ET.fromstring(svg)
        caps = sorted(
            (int(c.rsplit("-", 1)[1]), "".join(e.itertext()), c)
            for e in root.iter(NS + "text")
            for c in e.get("class", "").split() if re.fullmatch(r"bj-caption-\d+", c)
        )
        self.assertEqual([i for i, _, _ in caps], list(range(len(caps))))
        starts = []
        for i, text, cls in caps:
            frames = keyframes(css, cls)
            pcts = [p for p, d in frames if "opacity:1" in d.replace(" ", "")]
            self.assertEqual(len(pcts), 1, f"{cls} should show exactly once per loop")
            starts.append(pcts[0])
        self.assertEqual(starts, sorted(starts))
        text = " ".join(t for _, t, _ in caps).lower()
        order = [text.find(w) for w in ("catnip", "fishy", "ledge", "slide", "meant to do that")]
        self.assertNotIn(-1, order)
        self.assertEqual(order, sorted(order))


class CssWiringTests(unittest.TestCase):
    def test_every_bj_animation_has_keyframes_and_target(self):
        for mode, svg in RENDERS.items():
            css = style_of(svg)
            classes = class_set(svg)
            with self.subTest(mode):
                rules = [r for r in animation_rules(css) if any(c.startswith("bj-") for c in r[0])]
                self.assertGreaterEqual(len(rules), 25)
                for cls_list, name, _, _ in rules:
                    keyframes(css, name)  # raises if undefined
                    for cls in cls_list:
                        self.assertIn(cls, classes, f".{cls} animated but no element carries it")
                defined = {p[len("@keyframes "):] for p, _ in parse_blocks(css)
                           if p.startswith("@keyframes bj-")}
                used = {r[1] for r in rules}
                self.assertEqual(defined - used, set(), "keyframes defined but never used")

    def test_no_orphan_bj_classes(self):
        # every bj-* class on an element is styled somewhere
        for mode, svg in RENDERS.items():
            css = style_of(svg)
            with self.subTest(mode):
                for cls in sorted(c for c in class_set(svg) if c.startswith("bj-")):
                    self.assertRegex(css, r"\." + re.escape(cls) + r"\b", f"{cls} unstyled")

    def test_reduced_motion_guard_and_static_pose(self):
        for mode, svg in RENDERS.items():
            css = style_of(svg)
            blocks = parse_blocks(css)
            reduced = [b for p, b in blocks if p.startswith("@media") and "prefers-reduced-motion" in p
                       and "reduce" in p]
            with self.subTest(mode):
                self.assertTrue(reduced)
                joined = " ".join(reduced)
                self.assertRegex(joined, r"\*\s*\{\s*animation:\s*none\s*!important")
                self.assertRegex(joined, r"\.bj-caption\s*\{\s*display:\s*none")
                self.assertRegex(joined, r"\.bj-still\s*\{\s*opacity:\s*1")
                # Outside the media query: captions/still hidden by default, still is the one
                # static label, and the cat/shadow rest at the start of the walk.
                base = " ".join(f"{p}{{{b}}}" for p, b in blocks if not p.startswith("@"))
                self.assertRegex(base, r"\.bj-caption,\s*\.bj-still\s*\{opacity:0;\}")
                start_x = GEN.BOJANGLES_STORY[0][1]
                self.assertRegex(base, r"\.bj-travel,\s*\.bj-shadow-travel\s*\{transform:translateX\(" + str(start_x) + r"px\);\}")
                start = keyframes(css, "bj-travel")[0][1]
                self.assertIn(f"translate({start_x}px,0px)", start.replace(" ", ""))
                self.assertIn("Backyard patrol", svg)
                still = [e for e in ET.fromstring(svg).iter(NS + "text") if "bj-still" in e.get("class", "")]
                self.assertEqual(len(still), 1)
                # Nothing else is hidden at rest: only captions + still carry opacity:0.
                hidden = [p for p, b in blocks if not p.startswith("@")
                          and re.search(r"(?:^|;)\s*opacity:\s*0\s*;", b + ";")]
                self.assertEqual(hidden, [".bj-caption, .bj-still"])

    def test_animated_rules_are_not_reduced_motion_exempt(self):
        # Every animation rule sits outside the media query, so the blanket
        # `* {animation:none !important}` is the only thing that must disable them.
        for svg in RENDERS.values():
            for prelude, body in parse_blocks(style_of(svg)):
                if prelude.startswith("@media"):
                    self.assertNotRegex(re.sub(r"animation:\s*none\s*!important", "", body), r"animation\s*:")


if __name__ == "__main__":
    unittest.main()
