# Branding art generators

Source for `assets/profile/openshift-velero-border.svg`, `assets/profile/profile-square.svg`,
the platform cover SVGs (`assets/linkedin/`, `assets/x/`, `assets/facebook/`, `assets/youtube/`)
and the `exports/*.png` rasters.

```
python3 build.py            # index.html demo + assets/profile/openshift-velero-border.svg (from border.template.svg)
python3 gen_platform.py     # every platform cover -> out/*.svg  (see presets below)
python3 gen_square.py       # profile-square.svg    -> copy to assets/profile/profile-square.svg
python3 gen_gif.py          # profile-square-animated.gif (Google profile animation)
```

## Platform covers: one engine, one scene

`gen_platform.py` draws the same scene (name block, 4 backup pods, Velero shield,
danger rays, waves) from ratios applied to each platform's **safe box** — the
rectangle that survives every crop that platform applies. Adding a platform
means adding one preset; no layout code changes.

| preset | canvas | safe box | why that box |
| --- | --- | --- | --- |
| `linkedin` | 1584x396 | x 300–1568, y 30–366 | profile photo overlaps bottom-left |
| `x` | 1500x500 | x 250–1250, y 60–440 | 60 px cropped top/bottom, 2:1 copies cut 250 px/side |
| `facebook` | 1640x856 | x 200–1570, y 214–642 | 16:9 desktop crops 59 px/side, 2.4:1 mobile keeps centre band |
| `youtube` | 2560x1440 | x 507–2053, y 508–932 | TV/desktop/mobile all show the central 1546x423 area |

Scene ratios live in `K` (all relative to safe-box height), so every platform
gets the same shield/name/pod proportions. `figure=True` adds the cloaked
guardian (LinkedIn only — other crops leave no room).

Rasters (PNG) need a renderer, e.g.:

```
python3 -m pip install resvg-py
python3 -c "import resvg_py; open('exports/x-header-1500x500.png','wb').write(
    resvg_py.svg_to_bytes(svg_path='out/header-1500x500.svg', width=1500, height=500, background='#041a2c'))"
```

Local-only inputs the scripts expect (not committed here — licensing/size):
`assets/avatar/kaovilai.jpg`, `assets/fonts/RedHatDisplay-{Bold,Medium}.woff2`,
`assets/velero/icon-color.svg`, `assets/osicon/Technology_icon-Red_Hat-OpenShift-Standard-RGB.svg`.

Text is rendered as outlines (`paths.json`, built with fonttools+brotli via `gen_textpaths.py`)
so the SVGs need no fonts at view time. The OpenShift glyph paths are inlined in
`gen_platform.py` (`OS_GLYPH`), so covers need no osicon file to rebuild.
