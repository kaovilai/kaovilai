#!/usr/bin/env python3
"""Facebook cover (1640x856). Same scene as the LinkedIn header, re-laid out for
Facebook's crops: 16:9 on desktop, 2.4:1 on mobile, both left-aligned, profile
photo overlapping the left edge. All key content sits in the central 2.4:1 band
(y 210..640) and right of x=200."""
import base64
import importlib.util
import json
import math

spec = importlib.util.spec_from_file_location('gl', 'gen_linkedin.py')
gl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gl)

W, H = 1640, 856
BAND_TOP, BAND_BOT = H * 0.25, H * 0.75        # safe band for the 2.4:1 mobile crop
RED, BLUE, DEEP, NAVY = '#ee0000', '#239de0', '#041a2c', '#062238'
CYAN, WARN, INK = '#00c1d5', '#f0ab00', '#0b1622'

HEAD = (1030, 330, 46)
SH = (1235, 360, 190)
CONTACT = (SH[0] + 182, SH[1] - 44)


def rays():
    tx, ty = CONTACT
    beams = [((W, -40), 40, .6, 3.4), ((W, 140), 46, .5, 4.2),
             ((W, 330), 34, .55, 3.8), ((W - 60, 520), 26, .4, 4.6)]
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
        r1, r2 = 7, 26 + (k % 4) * 14
        sparks.append(f'<line x1="{tx + math.cos(a)*r1:.0f}" y1="{ty + math.sin(a)*r1:.0f}" '
                      f'x2="{tx + math.cos(a)*r2:.0f}" y2="{ty + math.sin(a)*r2:.0f}" stroke="{WARN}" '
                      f'stroke-width="2.6" stroke-linecap="round" opacity="0">'
                      f'<animate attributeName="opacity" values="0;.95;0" dur="{1.5 + k*.19:.2f}s" repeatCount="indefinite"/></line>')
    return '\n'.join(out), '\n'.join(sparks)


FEET = 712


def character(avatar, x, y, r):
    """Hooded guardian: broad shoulders, tapered cloak, photo in the hood."""
    sx, sy = x + 26, y + 80
    sh_y = y + 74
    cape = (f'M{x-52},{sh_y+6} C{x-118},{sh_y+52} {x-146},{FEET-150} {x-150},{FEET} '
            f'L{x-58},{FEET} C{x-56},{FEET-110} {x-44},{sh_y+90} {x-30},{sh_y+30} Z')
    torso = (f'M{x-46},{sh_y+8} C{x-52},{sh_y+60} {x-50},{sh_y+140} {x-48},{sh_y+162} '
             f'L{x+40},{sh_y+162} C{x+42},{sh_y+132} {x+50},{sh_y+56} {x+42},{sh_y+4} Z')
    legs = (f'M{x-44},{sh_y+158} L{x-38},{FEET} L{x-6},{FEET} L{x-4},{sh_y+158} Z '
            f'M{x+4},{sh_y+158} L{x+8},{FEET} L{x+44},{FEET} L{x+38},{sh_y+158} Z')
    return f'''<g>
  <path d="{cape}" fill="#08161f"/>
  <path d="{legs}" fill="{INK}"/>
  <path d="{torso}" fill="{INK}"/>
  <circle cx="{x-40}" cy="{sh_y+6}" r="21" fill="{INK}"/>
  <circle cx="{x+38}" cy="{sh_y+6}" r="21" fill="{INK}"/>
  <path d="{torso}" fill="none" stroke="#1b4f70" stroke-width="1.8" opacity=".85"/>
  <line x1="{sx}" y1="{sy}" x2="{CONTACT[0]-26}" y2="{CONTACT[1]+24}" stroke="{INK}"
        stroke-width="30" stroke-linecap="round"/>
  <circle cx="{x}" cy="{y}" r="{r*1.045:.1f}" fill="#0a2233" stroke="{CYAN}" stroke-width="2.6"/>
  <image href="{avatar}" x="{x-r}" y="{y-r}" width="{2*r}" height="{2*r}" clip-path="url(#headClip)"/>
  <circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{CYAN}" stroke-width="1.6" opacity=".75"/>
</g>'''


def shield():
    cx, cy, R = SH
    kr = R * .60
    crest = gl.velero_inline(cx, cy, kr * 2, BLUE, '#062a45')
    return f'''<g>
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{BLUE}" stroke-width="6">
    <animate attributeName="stroke-opacity" values="1;.5;1" dur="4.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{cx}" cy="{cy}" r="{R-10}" fill="url(#shieldGrad)" stroke="#0f4a6d" stroke-width="2"/>
  <g clip-path="url(#shieldClip)">{crest}
    <rect x="{cx - R*2:.0f}" y="{cy - R*.9:.0f}" width="{R*4:.0f}" height="{R*.8:.0f}"
          fill="url(#shimmer)" transform="rotate(-24 {cx} {cy})">
      <animateTransform attributeName="transform" type="translate" values="-340 0;340 0" dur="5.2s" repeatCount="indefinite" additive="sum"/>
    </rect>
  </g>
</g>'''


def waves():
    rows = [(H-150, BLUE, 8, .75, 14), (H-116, '#1d428a', 14, .95, 18), (H-82, '#7fd4e4', 6, .45, 11)]
    out = []
    for y, c, wd, op, dur in rows:
        d = (f'M-360,{y} Q-270,{y-22} -180,{y} T0,{y} T180,{y} T360,{y} T540,{y} T720,{y} '
             f'T900,{y} T1080,{y} T1260,{y} T1440,{y} T1620,{y} T1800,{y} T2000,{y}')
        out.append(f'<g opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                   f'values="0 0;-360 0" dur="{dur}s" repeatCount="indefinite"/>'
                   f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{wd}" stroke-linecap="round"/></g>')
    return '\n'.join(out)


def text_group(body, x, y, size, fill):
    return f'<g transform="translate({x},{y}) scale({size/1000:.4f},-{size/1000:.4f})" fill="{fill}">{body}</g>'


def main():
    tx = json.load(open('assets/fonts/paths.json'))
    avatar = 'data:image/jpeg;base64,' + base64.b64encode(open('assets/avatar/kaovilai.jpg', 'rb').read()).decode()
    beam_svg, spark_svg = rays()
    pods = '\n'.join([
        gl.pod(392, 556, 54, gl.icon_bucket(), tx['li_obj']['body'], tx['li_obj']['width'] * 0.011),
        gl.pod(532, 556, 54, gl.icon_disk(), tx['li_snap']['body'], tx['li_snap']['width'] * 0.011),
        gl.pod(672, 556, 54, gl.icon_pod(), tx['li_pod']['body'], tx['li_pod']['width'] * 0.011),
        gl.pod(812, 556, 54, gl.icon_config(), tx['li_cfg']['body'], tx['li_cfg']['width'] * 0.011),
    ])
    cap_w = tx['li_cap']['width'] * 0.013
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
  aria-label="Tiger Kaovilai raises a glowing Velero shield, deflecting red danger rays from space away from Kubernetes and OpenShift workloads">
  <defs>
    <radialGradient id="bg" cx=".3" cy=".05" r="1.15"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{DEEP}"/></radialGradient>
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
  <ellipse cx="700" cy="H-80" rx="760" ry="320" fill="url(#safeGlow)"/>

  {beam_svg}

  {text_group(tx['li_name']['body'], 200, 300, 68, '#eaf6fb')}
  {text_group(tx['li_sub']['body'], 202, 352, 22, '#8fb4c6')}
  {text_group(tx['li_cap']['body'], 602 - cap_w/2, 508, 13, '#5f8ba1')}

  {pods}

  {waves()}
  <ellipse cx="{CONTACT[0]+30}" cy="{CONTACT[1]}" rx="190" ry="230" fill="url(#impact)" opacity=".8"/>
  {shield()}
  {spark_svg}
</svg>'''
    open('facebook-cover.svg', 'w').write(svg)
    print('facebook-cover.svg', len(svg), 'bytes')


if __name__ == '__main__':
    main()
