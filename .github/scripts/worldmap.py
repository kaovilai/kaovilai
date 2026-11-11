#!/usr/bin/env python3
"""Regenerate the profile travel map from a Google Maps Timeline export.

Google retired Timeline in the cloud, so the only source is the on-device
export (Maps app -> Settings -> Location & privacy -> Location services ->
Timeline -> Export timeline data). That file is private and must never be
committed. This script turns it into two things that are safe to publish:

  data/places.json      city-level only: city name, region, country and the
                        city centre's coordinates. Nearest-city lookups come
                        from a vendored Natural Earth populated-places list.
                        Raw positions, addresses, place names/IDs and the
                        original timestamps never reach this file.
  worldmap-light.svg    the README map, drawn from data/places.json only.
  worldmap-dark.svg

Usage:
    python3 -I -B .github/scripts/worldmap.py import ~/Downloads/Timeline.json
    python3 -I -B .github/scripts/worldmap.py render
    python3 -I -B .github/scripts/worldmap.py all ~/Downloads/Timeline.json

The export can be a file or a directory (Takeout archives are searched
recursively). Supported shapes:

  * Android on-device Timeline.json (semanticSegments / rawSignals)
  * iPhone location-history.json (bare array of visit/activity/timelinePath)
  * Legacy Takeout Records.json / "Location History.json" (locations[])
  * Legacy Takeout Semantic Location History JSON (timelineObjects[])

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import math
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
# Shared with the browser page in map/; served by GitHub Pages too.
MAPDATA_DIR = REPO_ROOT / "map" / "data"

PLACES_SCHEMA = "worldmap-places/v1"
DEFAULT_DATA = REPO_ROOT / "data" / "places.json"
DEFAULT_MAX_CITY_KM = 75.0
DEFAULT_MAX_PATH_KM = 25.0

# cities.json rows: [name, region, country, iso2, population, lat, lon]
CITY_NAME, CITY_REGION, CITY_COUNTRY, CITY_ISO2, CITY_POP, CITY_LAT, CITY_LON = range(7)

_GEORE = re.compile(r"(-?\d+(?:\.\d+)?)")
_YEAR = re.compile(r"(\d{4})")


# ---------------------------------------------------------------------------
# Coordinate helpers


def parse_latlng(value):
    """Return (lat, lon) from any coordinate shape Google exports use.

    Accepts "geo:37.4,-122.0", "50.05°, 14.34°", {"latLng": ...},
    {"latitudeE7": int, "longitudeE7": int} and {"latitude": .., "longitude": ..}.
    """
    if value is None:
        return None
    if isinstance(value, str):
        nums = _GEORE.findall(value)
        if len(nums) >= 2:
            lat, lon = float(nums[0]), float(nums[1])
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return lat, lon
        return None
    if isinstance(value, dict):
        for key in ("latLng", "LatLng", "latlng"):
            if key in value:
                return parse_latlng(value[key])
        if "latitudeE7" in value and "longitudeE7" in value:
            return value["latitudeE7"] / 1e7, value["longitudeE7"] / 1e7
        if "latitude" in value and "longitude" in value:
            return float(value["latitude"]), float(value["longitude"])
        for key in ("location", "point", "latLng"):
            if key in value:
                parsed = parse_latlng(value[key])
                if parsed:
                    return parsed
    return None


def year_of(value):
    """Extract a 4-digit year from an ISO string, epoch millis or seconds."""
    if value is None:
        return None
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.isdigit():
            return year_of(int(stripped))
        match = _YEAR.search(stripped)
        return int(match.group(1)) if match else None
    if isinstance(value, (int, float)):
        if value > 1e14:  # microseconds
            seconds = value / 1e6
        elif value > 1e11:  # milliseconds
            seconds = value / 1e3
        else:
            seconds = value
        try:
            return _dt.datetime.fromtimestamp(seconds, tz=_dt.timezone.utc).year
        except (OverflowError, OSError, ValueError):
            return None
    return None


def day_of(value):
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.isdigit():
            number = int(stripped)
            if number > 10**14:  # microseconds
                number /= 10**6
            elif number > 10**11:  # milliseconds
                number /= 10**3
            stamp = _dt.datetime.fromtimestamp(number, tz=_dt.timezone.utc)
            return stamp.strftime("%Y-%m-%d")
        match = re.match(r"(\d{4}-\d{2}-\d{2})", stripped)
        if match:
            return match.group(1)
    return None


def haversine_km(lat1, lon1, lat2, lon2):
    radius = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = p2 - p1
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
    return 2 * radius * math.asin(min(1.0, math.sqrt(a)))


# ---------------------------------------------------------------------------
# Export parsing


class Sample:
    """One observed position, reduced to what aggregation needs."""

    __slots__ = ("lat", "lon", "kind", "year", "day")

    def __init__(self, lat, lon, kind, year=None, day=None):
        self.lat = lat
        self.lon = lon
        self.kind = kind  # "visit" | "transit" | "path" | "raw"
        self.year = year
        self.day = day


def _load_documents(path):
    """Yield every JSON document in a file or directory.

    The Android export concatenates one object per year with no separator, so
    a plain json.load is not enough; raw_decode lets us read them in sequence.
    """
    path = pathlib.Path(path).expanduser()
    if path.is_dir():
        files = sorted(p for p in path.rglob("*.json") if p.is_file())
    else:
        files = [path]
    for file in files:
        text = file.read_text(encoding="utf-8-sig", errors="replace")
        decoder = json.JSONDecoder()
        index = 0
        length = len(text)
        while index < length:
            while index < length and text[index].isspace():
                index += 1
            if index >= length:
                break
            try:
                document, index = decoder.raw_decode(text, index)
            except json.JSONDecodeError as error:
                # A truncated or corrupt export would otherwise silently
                # publish a partial history; refuse instead of guessing.
                raise SystemExit(
                    f"{file}: invalid JSON at offset {index} ({error.msg}); "
                    "re-export Timeline from the phone"
                ) from None
            yield document


def _visit_points(visit):
    """Yield the coordinate candidates inside a visit object."""
    if not isinstance(visit, dict):
        return
    top = visit.get("topCandidate") or {}
    candidates = [
        top.get("placeLocation"),
        top.get("location"),
        visit.get("location"),
        visit.get("placeLocation"),
    ]
    for candidate in candidates:
        parsed = parse_latlng(candidate)
        if parsed:
            yield parsed
            return


def _activity_points(activity):
    if not isinstance(activity, dict):
        return
    for key in ("start", "end"):
        parsed = parse_latlng(activity.get(key))
        if parsed:
            yield parsed


def _path_points(timeline_path):
    if not isinstance(timeline_path, list):
        return
    for point in timeline_path:
        parsed = parse_latlng(point)
        if parsed:
            yield parsed


def samples_from_document(document):
    """Yield Samples from any supported export document."""
    if isinstance(document, list):
        # iPhone location-history.json
        for entry in document:
            if not isinstance(entry, dict):
                continue
            year = year_of(entry.get("startTime") or entry.get("endTime"))
            day = day_of(entry.get("startTime") or entry.get("endTime"))
            for lat, lon in _visit_points(entry.get("visit")):
                yield Sample(lat, lon, "visit", year, day)
            for lat, lon in _activity_points(entry.get("activity")):
                yield Sample(lat, lon, "transit", year, day)
            for lat, lon in _path_points(entry.get("timelinePath")):
                yield Sample(lat, lon, "path", year, day)
        return

    if not isinstance(document, dict):
        return

    if "semanticSegments" in document:
        # Android on-device export
        for segment in document.get("semanticSegments") or []:
            if not isinstance(segment, dict):
                continue
            year = year_of(segment.get("startTime") or segment.get("endTime"))
            day = day_of(segment.get("startTime") or segment.get("endTime"))
            for lat, lon in _visit_points(segment.get("visit")):
                yield Sample(lat, lon, "visit", year, day)
            for lat, lon in _activity_points(segment.get("activity")):
                yield Sample(lat, lon, "transit", year, day)
            for lat, lon in _path_points(segment.get("timelinePath")):
                yield Sample(lat, lon, "path", year, day)
        # rawSignals adds position fixes the semantic pass skipped; they are
        # subject to the tighter path cutoff, so they only add cities the phone
        # was actually near.
        for signal in document.get("rawSignals") or []:
            if not isinstance(signal, dict):
                continue
            position = signal.get("position")
            if not isinstance(position, dict):
                continue
            parsed = parse_latlng(position)
            if not parsed:
                continue
            stamp = (
                position.get("timestamp")
                or signal.get("timestamp")
                or position.get("time")
            )
            yield Sample(*parsed, "raw", year_of(stamp), day_of(stamp))
        return

    if "locations" in document:
        # Legacy Takeout Records.json / Location History.json
        for record in document.get("locations") or []:
            parsed = parse_latlng(record)
            if not parsed:
                continue
            stamp = record.get("timestampMs") or record.get("timestamp")
            yield Sample(*parsed, "raw", year_of(stamp), day_of(stamp))
        return

    if "timelineObjects" in document:
        # Legacy Takeout Semantic Location History
        for obj in document.get("timelineObjects") or []:
            if not isinstance(obj, dict):
                continue
            visit = obj.get("placeVisit") or {}
            duration = visit.get("duration") or {}
            stamp = duration.get("startTimestampMs") or duration.get("startTimestamp")
            year, day = year_of(stamp), day_of(stamp)
            for lat, lon in _visit_points(visit):
                yield Sample(lat, lon, "visit", year, day)
            segment = obj.get("activitySegment") or {}
            seg_duration = segment.get("duration") or {}
            stamp = seg_duration.get("startTimestampMs") or seg_duration.get(
                "startTimestamp"
            )
            year, day = year_of(stamp), day_of(stamp)
            for key in ("startLocation", "endLocation"):
                parsed = parse_latlng(segment.get(key))
                if parsed:
                    yield Sample(*parsed, "transit", year, day)


def iter_samples(path):
    for document in _load_documents(path):
        yield from samples_from_document(document)


# ---------------------------------------------------------------------------
# City lookup


class CityIndex:
    """Nearest-city lookup over the vendored Natural Earth populated places."""

    def __init__(self, rows):
        self.rows = rows
        self.cells = {}
        for index, row in enumerate(rows):
            self.cells.setdefault(self._cell(row[CITY_LAT], row[CITY_LON]), []).append(
                index
            )
        self._cache = {}

    @staticmethod
    def _cell(lat, lon):
        return int(math.floor(lat)), int(math.floor(lon))

    def nearest(self, lat, lon, max_km):
        """Return (row, distance_km) or None when nothing is close enough."""
        # The cached answer depends on the search radius, so both go in the key.
        key = (round(lat * 20), round(lon * 20), max_km)
        if key in self._cache:
            row = self._cache[key]
            if row is None:
                return None
            # Recompute the distance for this exact point; the cached cell is
            # only ~5 km wide, but a shared distance could flip the cutoff.
            km = haversine_km(lat, lon, row[CITY_LAT], row[CITY_LON])
            return None if km > max_km else (row, km)

        best = None
        best_km = float("inf")
        base_lat, base_lon = self._cell(lat, lon)
        # A degree of latitude is ~111 km everywhere, but a degree of longitude
        # shrinks with cos(latitude); without that, high-latitude searches miss
        # cities to the east and west.
        lat_span = int(max_km / 111.0) + 1
        cos_lat = max(0.15, math.cos(math.radians(lat)))
        lon_span = int(max_km / (111.0 * cos_lat)) + 1
        for dlat in range(-lat_span, lat_span + 1):
            # The nearest point of this row of cells is at least this far away.
            if best is not None and (abs(dlat) - 1) * 111.0 > best_km:
                continue
            for dlon in range(-lon_span, lon_span + 1):
                # Longitude cells wrap at the antimeridian, so a city just
                # across +/-180 is still found.
                cell_lon = ((base_lon + dlon + 180) % 360) - 180
                for index in self.cells.get((base_lat + dlat, cell_lon), ()):
                    row = self.rows[index]
                    km = haversine_km(lat, lon, row[CITY_LAT], row[CITY_LON])
                    if km < best_km:
                        best, best_km = row, km
        self._cache[key] = best
        return None if best is None or best_km > max_km else (best, best_km)


def load_cities(index_path=None):
    path = pathlib.Path(index_path) if index_path else MAPDATA_DIR / "cities.json"
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


# ---------------------------------------------------------------------------
# Aggregation


class CityAggregate:
    __slots__ = ("row", "visits", "days", "first_year", "last_year")

    def __init__(self, row):
        self.row = row
        self.visits = 0
        self.days = set()
        self.first_year = None
        self.last_year = None

    def add(self, sample):
        new_day = bool(sample.day) and sample.day not in self.days
        if sample.kind in ("visit", "transit"):
            self.visits += 1
        elif new_day:
            # Raw position/path samples count once per city per day, so a long
            # stay does not outweigh a single airport connection.
            self.visits += 1
        if sample.day:
            self.days.add(sample.day)
        if sample.year:
            if self.first_year is None or sample.year < self.first_year:
                self.first_year = sample.year
            if self.last_year is None or sample.year > self.last_year:
                self.last_year = sample.year


def build_places(
    samples,
    city_index,
    max_km=DEFAULT_MAX_CITY_KM,
    min_visits=1,
    max_path_km=DEFAULT_MAX_PATH_KM,
):
    aggregates = {}
    resolved = skipped = 0
    for sample in samples:
        if not (-90 <= sample.lat <= 90 and -180 <= sample.lon <= 180):
            continue
        # Path/raw samples are dense; a looser cutoff would snap every rural
        # point to some distant town and invent stops along every highway.
        limit = max_path_km if sample.kind in ("path", "raw") else max_km
        match = city_index.nearest(sample.lat, sample.lon, limit)
        if not match:
            skipped += 1
            continue
        row = match[0]
        # Same-name cities in one country (Portland OR/ME, Springfield...) are
        # different rows; the coordinates keep them apart.
        key = (row[CITY_NAME], row[CITY_REGION], row[CITY_ISO2], row[CITY_LAT], row[CITY_LON])
        aggregate = aggregates.get(key)
        if aggregate is None:
            aggregate = aggregates[key] = CityAggregate(row)
        aggregate.add(sample)
        resolved += 1

    cities = []
    for aggregate in aggregates.values():
        if aggregate.visits < min_visits:
            continue
        row = aggregate.row
        cities.append(
            {
                "city": row[CITY_NAME],
                "region": row[CITY_REGION],
                "country": row[CITY_COUNTRY],
                "country_code": row[CITY_ISO2],
                # City centre from the gazetteer, rounded to ~1 km. The input
                # coordinate that produced this hit is never stored.
                "lat": round(row[CITY_LAT], 2),
                "lon": round(row[CITY_LON], 2),
                "visits": aggregate.visits,
                "days": len(aggregate.days),
                "first_year": aggregate.first_year,
                "last_year": aggregate.last_year,
            }
        )
    cities.sort(key=lambda c: (c["country"], c["region"], c["city"], c["lon"]))
    stats = {"samples": resolved + skipped, "resolved": resolved, "unmatched": skipped}
    return cities, stats


def write_places(cities, stats, output_path, max_km, max_path_km):
    document = {
        "schema": PLACES_SCHEMA,
        "note": (
            "City-level only, generated by .github/scripts/worldmap.py from a "
            "private Google Timeline export. Raw positions, addresses and place "
            "names are discarded at import time; coordinates are gazetteer city "
            "centres, not the original samples (visit cutoff %g km, path cutoff "
            "%g km)." % (max_km, max_path_km)
        ),
        "max_city_km": max_km,
        "max_path_km": max_path_km,
        "stats": stats,
        "cities": cities,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Rendering

THEMES = {
    "light": {
        "ocean": "#aadaff",
        "land": "#f2efe9",
        "coast": "#c9c3b4",
        "border": "#ddd8cb",
        "dot": "#e8453c",
        "dot_edge": "#ffffff",
        "glow": "#ff5a3c",
        "halo": "#e8453c",
    },
    "dark": {
        "ocean": "#0b1a2a",
        "land": "#1b2a3a",
        "coast": "#3d5268",
        "border": "#2b3d51",
        "dot": "#ff6b5e",
        "dot_edge": "#0b1a2a",
        "glow": "#ff8f6b",
        "halo": "#ff6b5e",
    },
}

MAX_MERCATOR_LAT = 85.0


def _mercator_y(lat):
    lat = max(-MAX_MERCATOR_LAT, min(MAX_MERCATOR_LAT, lat))
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


def load_land(path=None):
    land_path = pathlib.Path(path) if path else MAPDATA_DIR / "world-land.json"
    with land_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_borders(path=None):
    borders_path = pathlib.Path(path) if path else MAPDATA_DIR / "world-borders.json"
    if not borders_path.exists():
        return []
    with borders_path.open(encoding="utf-8") as handle:
        return json.load(handle)


class Projection:
    def __init__(self, width, west=-180.0, east=180.0, south=-58.0, north=78.0):
        self.width = width
        self.west = west
        self.east = east
        self.south_lat = south
        self.north_lat = north
        self.north = _mercator_y(north)
        self.south = _mercator_y(south)
        self.height = round(width * (self.north - self.south) / (2 * math.pi), 2)

    def point(self, lat, lon):
        x = (lon - self.west) / (self.east - self.west) * self.width
        y = (self.north - _mercator_y(lat)) / (self.north - self.south) * self.height
        return x, y


def _ring_path(ring, projection):
    """Project one ring of [lon, lat] pairs, splitting at the antimeridian."""
    subpaths = []
    current = []
    previous_lon = None
    for lon, lat in ring:
        if previous_lon is not None and abs(lon - previous_lon) > 180:
            if current:
                subpaths.append(current)
            current = []
        x, y = projection.point(lat, lon)
        current.append((x, y))
        previous_lon = lon
    if current:
        subpaths.append(current)

    parts = []
    for subpath in subpaths:
        if len(subpath) < 3:
            continue
        parts.append(
            "M "
            + " L ".join("%.1f %.1f" % (x, y) for x, y in subpath)
            + " Z"
        )
    return " ".join(parts)


def _land_paths(land, projection):
    """Yield SVG path data per polygon, clipped to the projection bounds."""
    west, east = projection.west, projection.east
    south, north = projection.south_lat, projection.north_lat
    for polygon in land["coordinates"]:
        segments = []
        for ring in polygon:
            if not ring:
                continue
            lons = [pt[0] for pt in ring]
            lats = [pt[1] for pt in ring]
            if max(lons) < west or min(lons) > east:
                continue
            if max(lats) < south or min(lats) > north:
                continue
            path = _ring_path(ring, projection)
            if path:
                segments.append(path)
        if segments:
            yield " ".join(segments)


def _lines_path(lines, projection):
    """Project border polylines, splitting at the antimeridian."""
    parts = []
    for line in lines:
        current = []
        previous_lon = None
        for lon, lat in line:
            if previous_lon is not None and abs(lon - previous_lon) > 180:
                if len(current) >= 2:
                    parts.append(
                        "M " + " L ".join("%.1f %.1f" % (x, y) for x, y in current)
                    )
                current = []
            current.append(projection.point(lat, lon))
            previous_lon = lon
        if len(current) >= 2:
            parts.append("M " + " L ".join("%.1f %.1f" % (x, y) for x, y in current))
    return " ".join(parts)


def render_svg(cities, land, theme_name="light", width=1280, borders=None):
    theme = THEMES[theme_name]
    projection = Projection(width)
    height = projection.height

    paths = list(_land_paths(land, projection))
    border_path = _lines_path(borders or [], projection)
    dots = []
    for city in sorted(cities, key=lambda c: (c["lat"], c["lon"])):
        x, y = projection.point(city["lat"], city["lon"])
        dots.append(
            '<circle cx="%.1f" cy="%.1f" r="4.2" fill="%s" stroke="%s" stroke-width="1.2"/>'
            % (x, y, theme["dot"], theme["dot_edge"])
        )

    title = "Travel map"
    description = (
        "World map with red dots marking cities the owner has lived in, visited "
        "or transited through, generated at city level."
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%.2f" '
        'viewBox="0 0 %d %.2f" role="img" aria-labelledby="map-title map-desc">\n'
        "  <title id=\"map-title\">%s</title>\n"
        "  <desc id=\"map-desc\">%s</desc>\n"
        '  <rect width="%d" height="%.2f" fill="%s"/>\n'
        '  <g fill="%s" stroke="%s" stroke-width="0.7" fill-rule="evenodd">\n'
        "    <path d=\"%s\"/>\n"
        "  </g>\n"
        '  <g fill="none" stroke="%s" stroke-width="0.6">\n'
        "    <path d=\"%s\"/>\n"
        "  </g>\n"
        "  <g>\n    %s\n  </g>\n"
        "</svg>\n"
        % (
            width,
            height,
            width,
            height,
            title,
            description,
            width,
            height,
            theme["ocean"],
            theme["land"],
            theme["coast"],
            " ".join(paths),
            theme["border"],
            border_path,
            "\n    ".join(dots),
        )
    )


def _arc_points(start, end, step_km=180.0):
    """Interpolate a great-circle arc between two (lat, lon) points.

    Straight Mercator lines between distant cities cut across continents; a
    geodesic reads as a flight path and looks right on a travel map.
    """
    lat1, lon1 = map(math.radians, start)
    lat2, lon2 = map(math.radians, end)
    x1, y1, z1 = (
        math.cos(lat1) * math.cos(lon1),
        math.cos(lat1) * math.sin(lon1),
        math.sin(lat1),
    )
    x2, y2, z2 = (
        math.cos(lat2) * math.cos(lon2),
        math.cos(lat2) * math.sin(lon2),
        math.sin(lat2),
    )
    dot = max(-1.0, min(1.0, x1 * x2 + y1 * y2 + z1 * z2))
    angle = math.acos(dot)
    if angle < 1e-9:
        return [start, end]
    distance_km = angle * 6371.0088
    steps = max(2, min(600, int(distance_km / step_km) + 1))
    points = []
    sin_angle = math.sin(angle)
    for index in range(steps + 1):
        t = index / steps
        a = math.sin((1 - t) * angle) / sin_angle
        b = math.sin(t * angle) / sin_angle
        x, y, z = (a * x1 + b * x2, a * y1 + b * y2, a * z1 + b * z2)
        norm = math.sqrt(x * x + y * y + z * z) or 1.0
        points.append(
            (
                math.degrees(math.asin(max(-1.0, min(1.0, z / norm)))),
                math.degrees(math.atan2(y, x)),
            )
        )
    return points


def _route_lines(cities):
    """Projected-agnostic polylines for consecutive cities in route order."""
    lines = []
    for start, end in zip(cities, cities[1:]):
        lines.append(
            _arc_points(
                (start["lat"], start["lon"]),
                (end["lat"], end["lon"]),
            )
        )
    return [[(lon, lat) for lat, lon in line] for line in lines]


def _route_order(cities):
    """Chronological order for the animated route; unknown years go last."""
    return sorted(
        cities,
        key=lambda c: (
            c["first_year"] if c.get("first_year") is not None else 9999,
            -(c.get("visits") or 0),
            c["country_code"],
            c["city"],
            c["lon"],
        ),
    )


def _route_legs(cities, projection):
    """One (path, length_px) pair per drawn arc segment.

    A leg that crosses the antimeridian is split into separate legs, because SVG
    restarts the dash pattern at each subpath and a single path with two ``M``
    commands would show two comets at once. Lengths are in projected user units
    because browsers apply stroke-dasharray in user units.
    """
    legs = []
    for start, end in zip(cities, cities[1:]):
        points = _arc_points((start["lat"], start["lon"]), (end["lat"], end["lon"]))
        subpaths = []
        current = []
        previous_lon = None
        for lat, lon in points:
            if previous_lon is not None and abs(lon - previous_lon) > 180:
                if len(current) >= 2:
                    subpaths.append(current)
                current = []
            current.append(projection.point(lat, lon))
            previous_lon = lon
        if len(current) >= 2:
            subpaths.append(current)

        for subpath in subpaths:
            path = "M " + " L ".join("%.1f %.1f" % (x, y) for x, y in subpath)
            length = sum(
                math.hypot(x2 - x1, y2 - y1)
                for (x1, y1), (x2, y2) in zip(subpath, subpath[1:])
            )
            if length > 4:
                legs.append((path, length))
    return legs


def _fmt_percent(fraction):
    text = ("%.4f" % (fraction * 100.0)).rstrip("0").rstrip(".")
    return text or "0"


def _leg_keyframes(index, legs, dashes):
    """One ping-pong pass of the comet along a single leg.

    The dash is parked just past either end of the leg so each leg is dark
    except during its own slot: forward in the first half of the cycle,
    backward in the second half.
    """
    length = legs[index][1]
    dash = dashes[index]
    n = max(1, len(legs))
    park = int(dash + 1)
    end = int(-(length + 1))
    times = (
        0.0,
        index / (2 * n),
        (index + 1) / (2 * n),
        0.5 + (n - 1 - index) / (2 * n),
        0.5 + (n - index) / (2 * n),
        1.0,
    )
    values = (park, park, end, end, park, park)
    steps = "".join(
        "%s%%{stroke-dashoffset:%d}" % (_fmt_percent(t), v)
        for t, v in zip(times, values)
    )
    return "@keyframes leg%d{%s}" % (index, steps)


def render_animated_svg(
    cities, land, theme_name="dark", width=1280, borders=None, duration=90.0
):
    """Animated map: glowing dashes ping-pong along the chronological route.

    Everything is inline (CSS keyframes plus an SVG blur) so the file still works
    as an <img> in a README: no scripts, no external references. Motion lives
    inside prefers-reduced-motion: no-preference, so the still route and dots are
    the fallback, and the file is byte-for-byte deterministic.
    """
    theme = THEMES[theme_name]
    projection = Projection(width)
    height = projection.height

    land_paths = " ".join(_land_paths(land, projection))
    border_path = _lines_path(borders or [], projection)
    ordered = _route_order(cities)
    route = _lines_path(_route_lines(ordered), projection)
    legs = _route_legs(ordered, projection)

    halos, dots = [], []
    total = max(1, len(ordered) - 1)
    half = duration / 2.0
    for index, city in enumerate(ordered):
        x, y = projection.point(city["lat"], city["lon"])
        # Flare each halo roughly when the comet reaches its city.
        delay = ((index / total) * half) % 4.5
        halos.append(
            '<circle class="halo" cx="%.1f" cy="%.1f" r="12" fill="%s" '
            'style="animation-delay:%.2fs"/>'
            % (x, y, theme["halo"], delay)
        )
        dots.append(
            '<circle cx="%.1f" cy="%.1f" r="4.2" fill="%s" stroke="%s" stroke-width="1.2"/>'
            % (x, y, theme["dot"], theme["dot_edge"])
        )

    leg_markup = []
    for index, (leg, _length) in enumerate(legs):
        leg_markup.append(
            '<path class="leg leg%d glow" d="%s"/>' % (index, leg)
        )
        leg_markup.append('<path class="leg leg%d" d="%s"/>' % (index, leg))

    dash = [max(20.0, min(46.0, length * 0.35)) for _path, length in legs]
    keyframes = "".join(_leg_keyframes(i, legs, dash) for i in range(len(legs)))
    leg_names = "".join(
        ".leg%d{animation-name:leg%d;stroke-dasharray:%d %d;stroke-dashoffset:%d}"
        % (i, i, dash[i], int(length + dash[i]), int(dash[i] + 1))
        for i, (_path, length) in enumerate(legs)
    )
    style = (
        "<style>\n"
        ".leg{fill:none;stroke:%(glow)s;stroke-width:2.2;stroke-linecap:round}\n"
        ".leg.glow{stroke-width:7;opacity:.5;filter:url(#soft)}\n"
        ".halo{opacity:.10}\n"
        "@media (prefers-reduced-motion:no-preference){\n"
        ".leg{animation-duration:%(duration).1fs;animation-timing-function:linear;"
        "animation-iteration-count:infinite}\n"
        "%(leg_names)s\n"
        ".halo{animation:twinkle 4.5s ease-in-out infinite}\n"
        "%(keyframes)s\n"
        "@keyframes twinkle{0%%,100%%{opacity:.10}50%%{opacity:.5}}\n"
        "}\n"
        "</style>\n"
    ) % {
        "glow": theme["glow"],
        "duration": duration,
        "leg_names": leg_names,
        "keyframes": keyframes,
    }

    title = "Travel map"
    description = (
        "World map of cities the owner has lived in, visited or transited "
        "through, with glowing route lines that travel through them in "
        "chronological order and back."
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%.2f" '
        'viewBox="0 0 %d %.2f" role="img" aria-labelledby="map-title map-desc">\n'
        "  <title id=\"map-title\">%s</title>\n"
        "  <desc id=\"map-desc\">%s</desc>\n"
        "  %s"
        "  <defs>\n"
        '    <filter id="soft" x="-30%%" y="-30%%" width="160%%" height="160%%">\n'
        '      <feGaussianBlur stdDeviation="3.2"/>\n'
        "    </filter>\n"
        "  </defs>\n"
        '  <rect width="%d" height="%.2f" fill="%s"/>\n'
        '  <g fill="%s" stroke="%s" stroke-width="0.7" fill-rule="evenodd">\n'
        "    <path d=\"%s\"/>\n"
        "  </g>\n"
        '  <g fill="none" stroke="%s" stroke-width="0.6">\n'
        "    <path d=\"%s\"/>\n"
        "  </g>\n"
        '  <g fill="none" stroke="%s" stroke-opacity="0.18" stroke-width="1.2">\n'
        "    <path d=\"%s\"/>\n"
        "  </g>\n"
        "  <g>\n    %s\n  </g>\n"
        "  <g>\n    %s\n  </g>\n"
        "  <g>\n    %s\n  </g>\n"
        "</svg>\n"
        % (
            width,
            height,
            width,
            height,
            title,
            description,
            style,
            width,
            height,
            theme["ocean"],
            theme["land"],
            theme["coast"],
            land_paths,
            theme["border"],
            border_path,
            theme["glow"],
            route,
            "\n    ".join(halos),
            "\n    ".join(leg_markup),
            "\n    ".join(dots),
        )
    )





def _read_places(path):
    with pathlib.Path(path).open(encoding="utf-8") as handle:
        document = json.load(handle)
    if document.get("schema") != PLACES_SCHEMA:
        raise SystemExit(f"{path}: not a {PLACES_SCHEMA} document")
    return document


def command_import(args):
    index = CityIndex(load_cities(args.cities))
    samples = iter_samples(args.input)
    cities, stats = build_places(
        samples,
        index,
        max_km=args.max_city_km,
        min_visits=args.min_visits,
        max_path_km=args.max_path_km,
    )
    if not cities:
        raise SystemExit(
            "no cities resolved - is this a Timeline export, and is --max-city-km large enough?"
        )
    write_places(
        cities, stats, pathlib.Path(args.out), args.max_city_km, args.max_path_km
    )
    print(
        "wrote %s: %d cities from %d samples (%d unmatched, dropped)"
        % (args.out, len(cities), stats["samples"], stats["unmatched"]),
        file=sys.stderr,
    )
    return 0


def command_render(args):
    document = _read_places(args.data)
    cities = document["cities"]
    land = load_land()
    borders = load_borders()
    out_dir = pathlib.Path(args.out_dir)
    themes = ["light", "dark"] if args.theme == "both" else [args.theme]
    for theme in themes:
        svg = render_svg(cities, land, theme, width=args.width, borders=borders)
        out = out_dir / f"worldmap-{theme}.svg"
        out.write_text(svg, encoding="utf-8")
        print(f"wrote {out} ({len(cities)} cities, {len(svg)} bytes)", file=sys.stderr)
        if args.animated:
            animated = render_animated_svg(
                cities,
                land,
                theme,
                width=args.width,
                borders=borders,
                duration=args.duration,
            )
            out = out_dir / f"worldmap-animated-{theme}.svg"
            out.write_text(animated, encoding="utf-8")
            print(
                f"wrote {out} ({len(cities)} cities, {len(animated)} bytes)",
                file=sys.stderr,
            )
    return 0


def command_all(args):
    args.out = str(pathlib.Path(args.data_dir) / "places.json")
    command_import(args)
    args.data = args.out
    command_render(args)
    return 0


def build_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    def import_options(p):
        p.add_argument("input", help="Timeline export file or directory")
        p.add_argument(
            "--out", default=str(DEFAULT_DATA), help="city-level JSON to write"
        )
        p.add_argument(
            "--max-city-km",
            type=float,
            default=DEFAULT_MAX_CITY_KM,
            help="drop visit samples farther than this from a populated place",
        )
        p.add_argument(
            "--max-path-km",
            type=float,
            default=DEFAULT_MAX_PATH_KM,
            help=(
                "drop position/path samples farther than this from a populated "
                "place (keeps highway noise out; default %(default)s)"
            ),
        )
        p.add_argument(
            "--min-visits",
            type=int,
            default=1,
            help="drop cities with fewer visits (default: 1)",
        )
        p.add_argument("--cities", help="override the vendored city gazetteer")

    def render_options(p):
        p.add_argument(
            "data", nargs="?", default=str(DEFAULT_DATA), help="city-level JSON to draw"
        )
        p.add_argument("--out-dir", default=str(REPO_ROOT), help="where SVGs go")
        p.add_argument("--theme", choices=["light", "dark", "both"], default="both")
        p.add_argument("--width", type=int, default=1280)
        p.add_argument(
            "--animated",
            action=argparse.BooleanOptionalAction,
            default=True,
            help="also write worldmap-animated-<theme>.svg (default: yes)",
        )
        p.add_argument(
            "--duration",
            type=float,
            default=90.0,
            help="seconds for one ping-pong cycle of the animated map",
        )

    p_import = sub.add_parser("import", help="export -> data/places.json (PII-stripped)")
    import_options(p_import)
    p_import.set_defaults(func=command_import)

    p_render = sub.add_parser("render", help="data/places.json -> worldmap-*.svg")
    render_options(p_render)
    p_render.set_defaults(func=command_render)

    p_all = sub.add_parser("all", help="import then render")
    import_options(p_all)
    p_all.add_argument(
        "--data-dir", default=str(DEFAULT_DATA.parent), help="where places.json goes"
    )
    p_all.add_argument("--out-dir", default=str(REPO_ROOT), help="where SVGs go")
    p_all.add_argument("--theme", choices=["light", "dark", "both"], default="both")
    p_all.add_argument("--width", type=int, default=1280)
    p_all.add_argument(
        "--animated",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="also write worldmap-animated-<theme>.svg (default: yes)",
    )
    p_all.add_argument(
        "--duration",
        type=float,
        default=90.0,
        help="seconds for one ping-pong cycle of the animated map",
    )
    p_all.set_defaults(func=command_all)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
