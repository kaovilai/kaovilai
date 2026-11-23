#!/usr/bin/env python3
"""Animated GIF of the square avatar for Google profile photos.
Google only animates GIF (JPEG/PNG are static), so frames come from the same
SVG with the wave pattern shifted and the ring swaying.
Run with /tmp/fontenv/bin/python (resvg-py + pillow)."""
import io
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import resvg_py
from PIL import Image

import gen_square

FRAMES = 24
LOOP_MS = 3200
TILE = 320  # wave period


def main():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        phase = -TILE * t                      # seamless: one full tile per loop
        angle = 10 * math.sin(2 * math.pi * t)  # ±10°, returns to start
        svg = gen_square.build(phase=phase, angle=angle)
        png = resvg_py.svg_to_bytes(svg_string=svg, width=512, height=512, background='#041a2c')
        frames.append(Image.open(io.BytesIO(png)).convert('RGB'))
    def save(fr, path, colors):
        base = fr[0].quantize(colors=colors, method=Image.MEDIANCUT)   # one shared palette
        pal = [f.quantize(palette=base, dither=Image.Dither.NONE) for f in fr]
        pal[0].save(path, save_all=True, append_images=pal[1:], duration=LOOP_MS // FRAMES,
                    loop=0, optimize=True, disposal=2)

    save(frames, 'exports/profile-square-animated.gif', 128)
    small = [f.resize((256, 256), Image.LANCZOS) for f in frames]
    save(small, 'exports/profile-square-animated-256.gif', 96)
    print('gifs written')


if __name__ == '__main__':
    main()
