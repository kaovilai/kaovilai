# Travel map data

Commit your imported, city-level Timeline data here as **`data/places.json`**.

Generate it with the [browser page](https://github.tig.pw/gmap-timeline-replaysvg/)
(choose **Anonymize: one day apart** under Dates), or from a clone of
[gmap-timeline-replaysvg](https://github.com/kaovilai/gmap-timeline-replaysvg):

```sh
python3 -I -B worldmap.py import ~/Downloads/Timeline.json \
  --dates synthetic --out data/places.json
```

`--dates synthetic` replaces real years with fake days one apart in route
order, so nothing about when you travelled is published. `--dates none` omits
dates entirely.

Pushing this file makes the **Update travel map** workflow render the flat
animated SVGs (`assets/worldmap-animated-light.svg` and `-dark.svg`, ~0.6 MB
each at 1280 px) and point `README.md` at them. SVG is used instead of GIF
because a GIF of the same map is tens of megabytes.

The file contains gazetteer city names, regions, countries, city-centre
coordinates, synthetic dates, and per-city `visits` and `days` counts (travel
frequency). Never commit the raw export.
