#!/usr/bin/env python3
"""X (Twitter) header (1500x500). Same shield scene as the FB cover, re-laid
out for X's crops: keep content in the middle 380px band (y 60..440), live
area x 250..1250 (2:1 mobile copies cut ~250px/side), lower-left calm for the
profile photo overlap. Static PNG only - X does not animate headers."""
import base64
import importlib.util
import json
import math

spec = importlib.util.spec_from_file_location('gl', 'gen_linkedin.py')
gl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gl)

W, H = 1500, 500
SAFE_TOP, SAFE_BOT = 60, 440          # X: up to 60px cropped top and bottom
RED, BLUE, DEEP, NAVY = '#ee0000', '#239de0', '#041a2c', '#062238'
CYAN, WARN, INK = '#00c1d5', '#f0ab00', '#0b1622'

SH = (1085, 235, 150)
CONTACT = (SH[0] + 138, SH[1] - 34)


def rays():
    tx, ty = CONTACT
    beams = [((W, 10), 36, .55, 3.4), ((W, 140), 42, .5, 4.2),
             ((W, 300), 32, .5, 3.8), ((W - 40, 450), 24, .4, 4.6)]
    out = []
    for (sx, sy), wdt, op, dur in beams:
        out.append(f'''<g opacity="{op}">
  <path d="M{sx},{sy} L{tx},{ty - wdt/2:.0f} L{tx},{ty + wdt/2:.0f} Z" fill="url(#dangerGrad)">
    <animate attributeName="opacity" values="1;.55;1" dur="{dur}s" repeatCount="indefinite"/>
  </path>
  <path d="M{sx},{sy} L{tx},{ty:.0f}" stroke="{WARN}" stroke-width="{max(2, wdt/7):.0f}" stroke-linecap="round"
        stroke-dasharray="16 30" opacity=".5">
    <animate attributeName="stroke-dashoffset" from="0" to="-184" dur="{dur}s" repeatCount="indefinite"/>
  </path>
</g>''')
    sparks = []
    for k in range(8):
        a = math.radians(-118 + k * 22)
        r1, r2 = 6, 22 + (k % 4) * 12
        sparks.append(f'<line x1="{tx + math.cos(a)*r1:.0f}" y1="{ty + math.sin(a)*r1:.0f}" '
                      f'x2="{tx + math.cos(a)*r2:.0f}" y2="{ty + math.sin(a)*r2:.0f}" stroke="{WARN}" '
                      f'stroke-width="2.4" stroke-linecap="round" opacity="0">'
                      f'<animate attributeName="opacity" values="0;.95;0" dur="{1.5 + k*.19:.2f}s" repeatCount="indefinite"/></line>')
    return '\n'.join(out), '\n'.join(sparks)


def shield():
    cx, cy, R = SH
    kr = R * .60
    crest = gl.velero_inline(cx, cy, kr * 2, BLUE, '#062a45')
    return f'''<g>
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{BLUE}" stroke-width="5">
    <animate attributeName="stroke-opacity" values="1;.5;1" dur="4.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{cx}" cy="{cy}" r="{R-8}" fill="url(#shieldGrad)" stroke="#0f4a6d" stroke-width="2"/>
  <g clip-path="url(#shieldClip)">{crest}
    <rect x="{cx - R*2:.0f}" y="{cy - R*.9:.0f}" width="{R*4:.0f}" height="{R*.8:.0f}"
          fill="url(#shimmer)" transform="rotate(-24 {cx} {cy})">
      <animateTransform attributeName="transform" type="translate" values="-280 0;280 0" dur="5.2s" repeatCount="indefinite" additive="sum"/>
    </rect>
  </g>
</g>'''


def waves():
    rows = [(H-96, BLUE, 7, .6, 12), (H-68, '#1d428a', 12, .8, 16), (H-42, '#7fd4e4', 5, .4, 10)]
    out = []
    for y, c, wd, op, dur in rows:
        d = (f'M-360,{y} Q-270,{y-20} -180,{y} T0,{y} T180,{y} T360,{y} T540,{y} T720,{y} '
             f'T900,{y} T1080,{y} T1260,{y} T1440,{y} T1620,{y} T1800,{y} T1980,{y}')
        out.append(f'<g opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                   f'values="0 0;-360 0" dur="{dur}s" repeatCount="indefinite"/>'
                   f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{wd}" stroke-linecap="round"/></g>')
    return '\n'.join(out)


def text_group(body, x, y, size, fill):
    return f'<g transform="translate({x},{y}) scale({size/1000:.4f},-{size/1000:.4f})" fill="{fill}">{body}</g>'


def main():
    tx = json.load(open('assets/fonts/paths.json'))
    beam_svg, spark_svg = rays()
    name_w = tx['li_name']['width'] * 0.062
    sub_w = tx['li_sub']['width'] * 0.020
    cap_w = tx['li_cap']['width'] * 0.012
    right = 918  # right edge of the text block, clear of the shield rim (x=935)
    nx = right - name_w
    sx = right - sub_w
    t_name = text_group(tx['li_name']['body'], nx, 190, 62, '#eaf6fb')
    t_sub = text_group(tx['li_sub']['body'], sx, 238, 20, '#8fb4c6')
    t_cap = text_group(tx['li_cap']['body'], nx + name_w / 2 - cap_w / 2, 292, 12, '#5f8ba1')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
  aria-label="Tiger Kaovilai raises a glowing Velero shield, deflecting red danger rays from space away from Kubernetes and OpenShift workloads">
  <defs>
    <radialGradient id="bg" cx=".35" cy=".05" r="1.15"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{DEEP}"/></radialGradient>
    <radialGradient id="dangerGrad" cx="1" cy=".5" r="1"><stop offset="0" stop-color="{RED}" stop-opacity=".9"/><stop offset=".5" stop-color="{RED}" stop-opacity=".45"/><stop offset="1" stop-color="{WARN}" stop-opacity="0"/></radialGradient>
    <radialGradient id="safeGlow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{BLUE}" stop-opacity=".2"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
    <radialGradient id="impact" cx="1" cy=".5" r=".6"><stop offset="0" stop-color="{RED}" stop-opacity=".55"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></radialGradient>
    <radialGradient id="shieldGrad" cx=".35" cy=".3" r=".85"><stop offset="0" stop-color="#0d3350"/><stop offset="1" stop-color="#04141f"/></radialGradient>
    <linearGradient id="shimmer" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#dff6ff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="shieldClip"><circle cx="{SH[0]}" cy="{SH[1]}" r="{SH[2]*.6:.0f}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <ellipse cx="640" cy="H-50" rx="700" ry="290" fill="url(#safeGlow)"/>

  {beam_svg}

  {t_name}
  {t_sub}
  {t_cap}

  {waves()}
  <ellipse cx="{CONTACT[0]+26}" cy="{CONTACT[1]}" rx="160" ry="200" fill="url(#impact)" opacity=".8"/>
  {shield()}
  {spark_svg}
</svg>'''
    open('x-header.svg', 'w').write(svg)
    print('x-header.svg', len(svg), 'bytes')


if __name__ == '__main__':
    main()
