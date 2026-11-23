# Branding art generators

Source for `assets/profile/openshift-velero-border.svg`, `assets/linkedin/header-1584x396.svg`,
`assets/profile/profile-square.svg` and the `exports/*.png` rasters.

```
python3 build.py            # index.html demo + assets/profile/openshift-velero-border.svg (from border.template.svg)
python3 gen_linkedin.py     # linkedin-header.svg   -> copy to assets/linkedin/header-1584x396.svg
python3 gen_square.py       # profile-square.svg    -> copy to assets/profile/profile-square.svg
```

Rasters (PNG) need a renderer, e.g.:

```
python3 -m pip install resvg-py
python3 -c "import resvg_py; open('exports/linkedin-cover-1584x396.png','wb').write(
    resvg_py.svg_to_bytes(svg_path='linkedin-header.svg', width=1584, height=396, background='#041a2c'))"
```

Local-only inputs the scripts expect (not committed here — licensing/size):
`assets/avatar/kaovilai.jpg`, `assets/fonts/RedHatDisplay-{Bold,Medium}.woff2`,
`assets/velero/icon-color.svg`, `assets/osicon/Technology_icon-Red_Hat-OpenShift-Standard-RGB.svg`.

Text is rendered as outlines (`paths.json`, built with fonttools+brotli via `gen_textpaths.py`)
so the SVGs need no fonts at view time.
