#!/usr/bin/env python3
"""Square 1:1 profile avatar (1080x1080 design): face in the OpenShift ring,
Velero waves filling the square behind. Self-contained SVG."""
import base64
import re

S = 1080
RED, BLUE, DEEP, NAVY = '#ee0000', '#239de0', '#041a2c', '#062238'
CYAN = '#00c1d5'
CX, CY = 540, 540
FACE_R = 300          # face circle
RING_BOX = 860        # OpenShift glyph box (hole-centred crop)


def ring_glyph_paths():
    import importlib.util
    spec = importlib.util.spec_from_file_location('b', 'build.py')
    b = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b)
    return b.ring_paths()


def waves():
    """Velero-colour wave rows across the square, period 320."""
    rows = []
    ys = list(range(-40, S + 80, 130))
    for i, y in enumerate(ys):
        col = '#239de0' if i % 2 == 0 else '#1d428a'
        op = .8 if i % 2 == 0 else .9
        wd = 22 if i % 3 == 0 else 16
        d = (f'M-320,{y} Q-240,{y-30} -160,{y} T0,{y} T160,{y} T320,{y} T480,{y} '
             f'T640,{y} T800,{y} T960,{y} T1120,{y} T1280,{y} T1440,{y}')
        rows.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{wd}" '
                    f'stroke-linecap="round" opacity="{op}"/>')
    # faint light layer
    for j, y in enumerate(range(25, S + 60, 130)):
        d = (f'M-320,{y} Q-240,{y-24} -160,{y} T0,{y} T160,{y} T320,{y} T480,{y} '
             f'T640,{y} T800,{y} T960,{y} T1120,{y} T1280,{y} T1440,{y}')
        rows.append(f'<path d="{d}" fill="none" stroke="#7fd4e4" stroke-width="9" '
                    f'stroke-linecap="round" opacity=".28"/>')
    return '\n'.join(rows)


def main():
    avatar = base64.b64encode(open('assets/avatar/kaovilai.jpg', 'rb').read()).decode()
    glyph = ring_glyph_paths()
    half = RING_BOX / 2
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" role="img"
  aria-label="kaovilai — OpenShift ring and Velero waves around a profile photo">
  <defs>
    <radialGradient id="bg" cx=".3" cy=".2" r="1.2"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{DEEP}"/></radialGradient>
    <clipPath id="face"><circle cx="{CX}" cy="{CY}" r="{FACE_R}"/></clipPath>
    <pattern id="wv" width="320" height="{S}" patternUnits="userSpaceOnUse">
      <g>{waves()}</g>
    </pattern>
  </defs>

  <rect width="{S}" height="{S}" fill="url(#bg)"/>
  <rect width="{S}" height="{S}" fill="url(#wv)" opacity=".85"/>

  <!-- openShift ring, hole-centred on the face -->
  <svg viewBox="5.98 6.08 26 26" x="{CX - half:.0f}" y="{CY - half:.0f}" width="{RING_BOX}" height="{RING_BOX}">{glyph}</svg>

  <!-- face -->
  <circle cx="{CX}" cy="{CY}" r="{FACE_R + 14}" fill="#0a2233" stroke="{CYAN}" stroke-width="6"/>
  <image href="data:image/jpeg;base64,{avatar}" x="{CX - FACE_R}" y="{CY - FACE_R}"
         width="{2 * FACE_R}" height="{2 * FACE_R}" clip-path="url(#face)"/>
  <circle cx="{CX}" cy="{CY}" r="{FACE_R}" fill="none" stroke="#ffffff" stroke-opacity=".8" stroke-width="5"/>
</svg>'''
    open('profile-square.svg', 'w').write(svg)
    print('profile-square.svg', len(svg), 'bytes')


if __name__ == '__main__':
    main()
