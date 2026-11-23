#!/usr/bin/env python3
"""Convert strings to SVG path outlines with Red Hat fonts (no font dependency).
Uses /tmp/fontenv (fonttools+brotli). Returns path data in font units.
"""
import subprocess
import sys

try:
    from fontTools.ttLib import TTFont
    from fontTools.pens.svgPathPen import SVGPathPen
except ImportError:
    sys.exit('run with /tmp/fontenv/bin/python')

_cache = {}


def _font(path):
    if path not in _cache:
        _cache[path] = TTFont(path)
    return _cache[path]


def upm_of(font_path):
    return _font(font_path)['head'].unitsPerEm


def text_width_units(text, font_path, size, letter_spacing=0.0):
    """Width in FONT UNITS (letter_spacing given in px, converted to units)."""
    f = _font(font_path)
    upm = f['head'].unitsPerEm
    cmap = f.getBestCmap()
    hmtx = f['hmtx']
    ls = letter_spacing * upm / size
    w = 0.0
    for ch in text:
        g = cmap.get(ord(ch))
        if g:
            w += hmtx[g][0]
        w += ls
    return w - (ls if text else 0)


def text_paths(text, font_path, size, letter_spacing=0.0):
    """Return (list_of (path_d, x_offset_units, 0), total_width_units).
    All coordinates in FONT UNITS, y-up. Caller renders with
    transform="translate(x,y) scale(s,-s)" where s = size / upm."""
    f = _font(font_path)
    upm = f['head'].unitsPerEm
    cmap = f.getBestCmap()
    hmtx = f['hmtx']
    gs = f.getGlyphSet()
    ls = letter_spacing * upm / size
    x = 0.0
    out = []
    for ch in text:
        g = cmap.get(ord(ch))
        if g:
            pen = SVGPathPen(gs)
            gs[g].draw(pen)
            cmds = pen.getCommands()
            if cmds:
                out.append((cmds, x, 0.0))
            x += hmtx[g][0]
        x += ls
    return out, x - (ls if text else 0)


def text_svg(text, font_path, size, x, y, fill, letter_spacing=0.0, extra=''):
    """SVG markup placing text at baseline (x, y) in a y-down coordinate system."""
    parts, w = text_paths(text, font_path, size, letter_spacing)
    body = ''.join(f'<path d="{d}" transform="translate({gx:.3f},0)"/>' for d, gx, _ in parts)
    return (f'<g transform="translate({x},{y}) scale(1,-1)" fill="{fill}"{extra}>'
            f'{body}</g>'), w
