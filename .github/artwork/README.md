# Bojangles facial artwork

`bojangles-face.json` is the editable vector source for Bojangles's face. Its
colored contours were traced locally from a user-supplied close-up, then split
into head, ear, eyes, and jaw for animation. It contains only geometry and colors:
no original image, image metadata, local source path, or embedded raster data.

The daily profile generator reads this JSON using Python's standard library.
It adds eyelid underlays, eye highlights, whiskers, and CSS animation. It does not
need Pillow or the private reference photograph. Both generated theme SVGs remain
self-contained; their 150 KB budget includes the more detailed facial geometry.

For optional re-authoring, `.github/scripts/trace-bojangles-face.py` takes a private,
already oriented 600×600 face crop and an output JSON path. It requires Pillow;
its outline and feature masks are specific to this portrait. A different photo
requires new masks. Never commit the input photo or private crop. The committed
JSON can also be edited directly without any image-processing tools.

Validate generated assets with:

```sh
python3 -I -B .github/scripts/test_bojangles.py
```
