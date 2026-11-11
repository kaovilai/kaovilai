#!/usr/bin/env python3
"""Rebuild the vendored basemap data used by worldmap.py.

Downloads two public-domain Natural Earth datasets, strips them down to what
the renderer needs, simplifies coastlines and rounds coordinates, then writes
compact files into map/data/:

  world-land.json    coastline/land polygons (Natural Earth 1:50m land)
  world-borders.json country boundary lines (Natural Earth 1:110m)
  cities.json        populated places used for city-level PII stripping

Run this only when the upstream Natural Earth data needs refreshing; the
generated files are committed so day-to-day map regeneration needs no network.

    python3 -I -B .github/scripts/build-mapdata.py
"""

from __future__ import annotations

import json
import pathlib
import sys
import urllib.request

NE_BASE = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"
)
LAND_URL = NE_BASE + "ne_50m_land.geojson"
BORDERS_URL = NE_BASE + "ne_110m_admin_0_boundary_lines_land.geojson"
PLACES_URL = NE_BASE + "ne_10m_populated_places_simple.geojson"

OUT_DIR = pathlib.Path(__file__).resolve().parents[2] / "map" / "data"

# Douglas-Peucker tolerance in degrees. 0.07 is well under one pixel at README
# width (~0.28 deg/px) and keeps small islands while cutting the coastline
# roughly in half.
SIMPLIFY_DEGREES = 0.07
# Rings smaller than this bounding box are dropped (sub-2 km islands).
MIN_BOX_DEGREES = 0.03


def fetch(url: str) -> dict:
    print(f"fetching {url}", file=sys.stderr)
    with urllib.request.urlopen(url, timeout=120) as resp:  # noqa: S310 - fixed host
        return json.load(resp)


def _perp_distance(pt, start, end) -> float:
    if start == end:
        return ((pt[0] - start[0]) ** 2 + (pt[1] - start[1]) ** 2) ** 0.5
    dx, dy = end[0] - start[0], end[1] - start[1]
    t = ((pt[0] - start[0]) * dx + (pt[1] - start[1]) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    px, py = start[0] + t * dx, start[1] + t * dy
    return ((pt[0] - px) ** 2 + (pt[1] - py) ** 2) ** 0.5


def simplify(points, tolerance: float):
    """Douglas-Peucker on a closed ring, keeping first/last point."""
    if len(points) <= 4:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        start, end = stack.pop()
        worst, index = 0.0, None
        for i in range(start + 1, end):
            dist = _perp_distance(points[i], points[start], points[end])
            if dist > worst:
                worst, index = dist, i
        if index is not None and worst > tolerance:
            keep[index] = True
            stack.append((start, index))
            stack.append((index, end))
    return [p for p, k in zip(points, keep) if k]


def _round_ring(ring):
    out = []
    for lon, lat in ring:
        pt = (round(lon, 2), round(lat, 2))
        if not out or out[-1] != pt:
            out.append(pt)
    if out and out[0] != out[-1]:
        out.append(out[0])
    return out


def _round_line(line):
    out = []
    for lon, lat in line:
        pt = (round(lon, 2), round(lat, 2))
        if not out or out[-1] != pt:
            out.append(pt)
    return out


def _ring_box(ring):
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return max(xs) - min(xs), max(ys) - min(ys)


def clean_polygon(rings):
    cleaned = []
    for i, ring in enumerate(rings):
        if len(ring) < 4:
            continue
        simplified = simplify(ring, SIMPLIFY_DEGREES)
        simplified = _round_ring(simplified)
        if len(simplified) < 4:
            continue
        # Outer ring may collapse to nothing; holes are only kept when the
        # outer ring survived.
        if i > 0 and not cleaned:
            continue
        w, h = _ring_box(simplified)
        if i == 0 and max(w, h) < MIN_BOX_DEGREES:
            return None
        cleaned.append(simplified)
    if not cleaned:
        return None
    return cleaned


def build_land(raw: dict):
    polygons = []
    for feature in raw["features"]:
        geom = feature.get("geometry") or {}
        if geom.get("type") == "Polygon":
            clean = clean_polygon(geom["coordinates"])
            if clean:
                polygons.append(clean)
        elif geom.get("type") == "MultiPolygon":
            for poly in geom["coordinates"]:
                clean = clean_polygon(poly)
                if clean:
                    polygons.append(clean)
    polygons.sort(key=lambda p: (round(p[0][0][1], 2), round(p[0][0][0], 2)))
    return {"type": "MultiPolygon", "coordinates": polygons}


def build_borders(raw: dict):
    lines = []
    for feature in raw["features"]:
        geom = feature.get("geometry") or {}
        if geom.get("type") == "LineString":
            parts = [geom["coordinates"]]
        elif geom.get("type") == "MultiLineString":
            parts = geom["coordinates"]
        else:
            continue
        for line in parts:
            simplified = _round_line(simplify(line, SIMPLIFY_DEGREES))
            if len(simplified) >= 2:
                lines.append(simplified)
    lines.sort(key=lambda line: (round(line[0][1], 2), round(line[0][0], 2)))
    return lines


def build_cities(raw: dict):
    """Return array rows: [name, region, country, iso2, population, lat, lon].

    Array rows instead of objects keep the committed file ~35% smaller; the
    field order is documented in worldmap.py.
    """
    cities = []
    seen = set()
    for feature in raw["features"]:
        props = feature["properties"]
        lon, lat = feature["geometry"]["coordinates"][:2]
        name = (props.get("name") or "").strip()
        if not name:
            continue
        region = (props.get("adm1name") or "").strip()
        country = (props.get("adm0name") or "").strip()
        iso2 = (props.get("iso_a2") or "").strip()
        key = (name, iso2, round(lon, 2), round(lat, 2))
        if key in seen:
            continue
        seen.add(key)
        cities.append(
            [
                name,
                region,
                country,
                iso2,
                int(props.get("pop_max") or 0),
                round(lat, 3),
                round(lon, 3),
            ]
        )
    cities.sort(key=lambda c: (c[2], c[1], c[0], c[6], c[5]))
    return cities


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    land = build_land(fetch(LAND_URL))
    land_path = OUT_DIR / "world-land.json"
    land_path.write_text(
        json.dumps(land, separators=(",", ":"), sort_keys=False) + "\n",
        encoding="utf-8",
    )
    points = sum(len(ring) for poly in land["coordinates"] for ring in poly)
    print(f"wrote {land_path} ({len(land['coordinates'])} polygons, {points} points)")

    borders = build_borders(fetch(BORDERS_URL))
    borders_path = OUT_DIR / "world-borders.json"
    borders_path.write_text(
        json.dumps(borders, separators=(",", ":")) + "\n", encoding="utf-8"
    )
    print(f"wrote {borders_path} ({len(borders)} border lines)")

    cities = build_cities(fetch(PLACES_URL))
    cities_path = OUT_DIR / "cities.json"
    cities_path.write_text(
        json.dumps(cities, separators=(",", ":")) + "\n", encoding="utf-8"
    )
    print(f"wrote {cities_path} ({len(cities)} places)")


if __name__ == "__main__":
    main()
