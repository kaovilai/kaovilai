# Travel map (`worldmap-light.svg`, `worldmap-dark.svg`)

The README's "Places" map is generated from Google Maps Timeline data that
never leaves this machine. Google retired the cloud copy of Timeline, so the
only current source is the export made inside the Maps app on the phone that has
Timeline enabled.

Three files are involved:

| File | Visibility | Contents |
| --- | --- | --- |
| Google export (`Timeline.json` / `location-history.json`) | **private** | raw positions, visits, addresses, place IDs |
| `data/places.json` | public | city name, region, country and gazetteer city centre only |
| `worldmap-light.svg`, `worldmap-dark.svg` (and animated variants) | public | the rendered map |

## 1. Export Timeline from the phone

Android (Google Maps app):

1. Profile picture → **Settings** → **Location & privacy** → **Location
   services** → **Timeline**.
2. **Export timeline data** → choose "all" → save the `.zip`.
3. Unzip it; the file inside is `Timeline.json`. It can be tens of megabytes and
   is several concatenated JSON objects, not one document.

iPhone (Google Maps app): **Settings** → **Location & privacy** → **Location
services** → **Timeline** → **Export timeline data**. The file is
`location-history.json`.

Older Google Takeout archives still work too: `Records.json`, `Location
History.json` and `Semantic Location History/YYYY/*.json`.

**Do not commit the export.** The `.gitignore` entries `Timeline.json`,
`location-history.json`, `Records.json` and `Semantic Location History/` are
there for exactly that reason.

## 2. Import and render

The script has no third-party dependencies:

```sh
python3 -I -B .github/scripts/worldmap.py all ~/Downloads/Timeline.json
```

This writes `data/places.json` plus four SVGs: static and animated, light and
dark. Then review the diff — it should contain only city-level data — and
commit:

```sh
git add data/places.json worldmap-*.svg
git commit -s -m "Refresh travel map from Timeline export"
```

Individual steps, when you only need one of them:

```sh
python3 -I -B .github/scripts/worldmap.py import ~/Downloads/Timeline.json
python3 -I -B .github/scripts/worldmap.py render
```

`render` flags: `--no-animated` skips the animated variants, `--theme dark`
renders one theme only, and `--duration 120` slows the ping-pong cycle
(default 90 seconds).

## 3. What counts as "city level"

Every sample in the export — visit, activity endpoint or path point — is
resolved to the nearest populated place in a vendored Natural Earth gazetteer
(7,342 places worldwide). `data/places.json` then stores:

- the gazetteer city name, region, country and ISO code;
- the **city centre** coordinates from the gazetteer, rounded to 2 decimals
  (~1 km) — never the original sample;
- visit count, distinct days, and first/last year.

Samples farther than `--max-city-km` (default 75 km) from any populated place
are dropped, so flight paths over oceans and remote wilderness do not turn into
fake stops. Position/path samples use the tighter `--max-path-km` (default
25 km) so a highway drive does not snap to a town 70 km away. Raise either
cutoff or use `--min-visits 2` to keep only places visited more than once.

Raw coordinates, addresses, place names/IDs and exact timestamps are discarded
during import and never written to disk by the script. `test_worldmap.py`
asserts that none of them can appear in the output.

## 4. Drawing

`render` uses a Web Mercator projection with a vendored, simplified Natural
Earth coastline. Output is deterministic: the same `data/places.json` always
produces byte-identical SVGs, and the test suite verifies that the committed
SVGs match the committed data.

Two variants are written per theme:

- `worldmap-<theme>.svg` — static dots on the map.
- `worldmap-animated-<theme>.svg` — same map, plus faint great-circle arcs
  between cities in chronological order (by first visit year) and a glowing
  dash that ping-pongs along them, one hop at a time. It is pure inline CSS
  and SVG filters: no scripts, no external references, so it animates as an
  `<img>` in a README. All motion sits inside
  `@media (prefers-reduced-motion: no-preference)`, so reduced-motion readers
  get the still map.

README wiring for the animated map:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="worldmap-animated-dark.svg">
  <img alt="Animated world map of places lived, visited and transited through" src="worldmap-animated-light.svg" width="100%">
</picture>
```

Basemap data in `map/data/` is public domain
([Natural Earth](https://www.naturalearthdata.com/)) and is only rebuilt when
upstream data needs refreshing:

```sh
python3 -I -B .github/scripts/build-mapdata.py
```

## 5. Tests

```sh
python3 -I -B .github/scripts/test_worldmap.py
```

They cover every supported export shape, coordinate parsing, PII stripping,
deterministic rendering, animated output being self-contained, and staleness
between `data/places.json` and the committed SVGs.
