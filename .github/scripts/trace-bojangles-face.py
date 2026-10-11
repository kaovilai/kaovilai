#!/usr/bin/env python3
"""Optional artwork authoring tool; NOT used by the daily profile renderer.

Requires Pillow. Pass a private, oriented 600×600 face crop and an output JSON
path. This mask is specific to Bojangles's portrait, not a general face detector.
Only palette colors and vector contours are saved, never image bytes or metadata.
The committed JSON is the editable artwork source; CI needs neither Pillow nor
any photograph. Run Python with -I when reading a supplied image.
"""
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

SIZE = 200
OUTLINE = [
    (85, 114), (109, 129), (148, 153), (190, 174), (230, 183), (276, 178),
    (313, 185), (368, 181), (399, 177), (426, 149), (466, 109), (504, 93),
    (535, 90), (550, 107), (550, 136), (546, 186), (520, 247), (500, 310),
    (485, 374), (458, 431), (400, 468), (350, 493), (294, 508), (239, 496),
    (199, 475), (159, 433), (136, 394), (135, 359), (143, 315), (154, 274),
    (145, 245), (120, 205),
]
REGIONS = {
    "ear": [(85, 114), (148, 153), (190, 174), (206, 197), (154, 274), (145, 245), (120, 205)],
    "eye-near": [(173, 311), (187, 302), (206, 305), (222, 314), (232, 328), (238, 339),
                 (228, 349), (211, 350), (193, 340), (180, 326)],
    "eye-far": [(322, 334), (336, 316), (353, 309), (377, 307), (403, 316), (391, 336),
                (368, 348), (345, 350), (329, 343)],
    "jaw": [(208, 465), (240, 477), (273, 478), (314, 466), (349, 464), (361, 484),
            (328, 500), (294, 508), (257, 502), (226, 491)],
}


def polygon(points):
    return "M" + " ".join(f"{round(x / 3)},{round(y / 3)}" for x, y in points) + "Z"


def mask(points):
    image = Image.new("L", (SIZE, SIZE))
    ImageDraw.Draw(image).polygon([(round(x / 3), round(y / 3)) for x, y in points], fill=1)
    return image.tobytes()


def simplify(points, tolerance=.65):
    if len(points) < 3:
        return points
    ax, ay = points[0]
    bx, by = points[-1]
    den = math.hypot(bx - ax, by - ay)
    distances = [abs((by - ay) * (x - ax) - (bx - ax) * (y - ay)) / den
                 if den else math.hypot(x - ax, y - ay) for x, y in points]
    k = max(range(len(points)), key=distances.__getitem__)
    if distances[k] <= tolerance:
        return [points[0], points[-1]]
    return simplify(points[:k + 1], tolerance)[:-1] + simplify(points[k:], tolerance)


def contours(pixels):
    edges = defaultdict(list)
    # Sorted traversal makes the authored geometry reproducible as well as CI output.
    for x, y in sorted(pixels):
        for neighbour, a, b in (
            ((x, y - 1), (x, y), (x + 1, y)),
            ((x + 1, y), (x + 1, y), (x + 1, y + 1)),
            ((x, y + 1), (x + 1, y + 1), (x, y + 1)),
            ((x - 1, y), (x, y + 1), (x, y)),
        ):
            if neighbour not in pixels:
                edges[a].append(b)
    paths = []
    while edges:
        start = next(iter(edges))
        ring, cur = [start], start
        while True:
            nxt = edges[cur].pop()
            if not edges[cur]:
                del edges[cur]
            ring.append(nxt)
            cur = nxt
            if cur == start:
                break
        if len(ring) < 5:
            continue
        mid = len(ring) // 2
        ring = simplify(ring[:mid + 1])[:-1] + simplify(ring[mid:])
        if len(ring) >= 4:
            paths.append("M" + " ".join(f"{x},{y}" for x, y in ring[:-1]) + "Z")
    return " ".join(paths)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: trace-bojangles-face.py PRIVATE_FACE_CROP.png OUTPUT.json")
    src, output = map(Path, sys.argv[1:3])
    with Image.open(src) as source:
        if source.size != (600, 600):
            raise ValueError("Expected an oriented, 600×600 facial crop matching the masks")
        image = source.convert("RGB").resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    image = ImageEnhance.Contrast(image).enhance(1.08).filter(ImageFilter.MedianFilter(3))
    quant = image.quantize(colors=24, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    palette = ["#%02x%02x%02x" % tuple(quant.getpalette()[i:i + 3]) for i in range(0, 72, 3)]
    data, full = quant.tobytes(), mask(OUTLINE)
    regions = {name: mask(points) for name, points in REGIONS.items()}
    layers = {name: defaultdict(set) for name in ("head", *REGIONS)}
    for idx, color in enumerate(data):
        if full[idx]:
            name = next((key for key, region in regions.items() if region[idx]), "head")
            layers[name][color].add((idx % SIZE, idx // SIZE))
    result = {
        "viewBox": [0, 0, SIZE, SIZE],
        "outline": polygon(OUTLINE),
        "base": polygon(OUTLINE[3:30] + [(206, 197)]),  # exclude the movable ear
        "regions": {name: polygon(points) for name, points in REGIONS.items()},
        "layers": [{"name": name, "paths": [{"fill": palette[color], "d": contours(pixels)}
                    for color, pixels in sorted(groups.items())]} for name, groups in layers.items()],
    }
    output.write_text(json.dumps(result, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Wrote vector geometry: {output.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
