#!/usr/bin/env python3
"""linkedin-header.svg v2: Tiger raises a Velero shield against space danger,
Kubernetes + OpenShift clusters sheltered behind. Inline art only (no symbol
refs), SMIL animation, self-contained."""
import base64
import math
import re

W, H = 1584, 396
RED, BLUE, DEEP, NAVY = '#ee0000', '#239de0', '#041a2c', '#062238'
CYAN, WARN, INK = '#00c1d5', '#f0ab00', '#0b1622'

SH_X, SH_Y, SH_R = 1130, 150, 118
CONTACT = (SH_X + 115, SH_Y - 26)   # shield rim, right side
HEAD_X, HEAD_Y, HEAD_R = 950, 176, 42
SHOULDER = (HEAD_X + 20, HEAD_Y + 76)
GRIP = (SH_X - SH_R*0.62, SH_Y + SH_R*0.80)

OS_GLYPH = [
    (RED, 'm18.95117,28.63379c-2.19141,0-4.35352-.75586-6.12207-2.21777-.26562-.21973-.30273-.61328-.08301-.87988s.6123-.30273.87988-.08301c2.46875,2.04102,5.82129,2.49902,8.74805,1.19727,2.9248-1.30273,4.82715-4.10059,4.96387-7.30273.01465-.34473.29297-.6543.65039-.59766.34473.01465.6123.30566.59766.65039-.15625,3.67969-2.3418,6.89551-5.7041,8.39258-1.26758.56445-2.60449.84082-3.93066.84082Z'),
    (RED, 'm9.97363,19.22656c-.00879,0-.01855,0-.02832-.00098-.34473-.01562-.61133-.30762-.5957-.6543.16602-3.66797,2.35156-6.87402,5.70312-8.36621,3.36328-1.49609,7.21484-.96875,10.05273,1.37695.26562.21973.30273.61328.08301.87988s-.61328.30371-.87988.08301c-2.46973-2.04102-5.82227-2.5-8.74805-1.19727-2.91602,1.29785-4.81738,4.08789-4.96289,7.28027-.01465.33496-.29102.59668-.62402.59668Z'),
    ('#ffffff', 'm10.09863,22.19043c-.23926,0-.4668-.1377-.57129-.37109-.13965-.31445.00195-.68457.31738-.8252l2.74023-1.2207c.3125-.13867.68359.00098.8252.31738.13965.31445-.00195.68457-.31738.8252l-2.74023,1.2207c-.08203.03613-.16895.05371-.25391.05371Z'),
    ('#ffffff', 'm8.83105,25.49023c-.23926,0-.46777-.1377-.57129-.37109-.13965-.31543.00195-.68457.31738-.8252l2.74121-1.21973c.3125-.1377.68457.00098.8252.31738.13965.31543-.00195.68457-.31738.8252l-2.74121,1.21973c-.08203.03613-.16895.05371-.25391.05371Z'),
    ('#ffffff', 'm26.42773,14.91992c-.23926,0-.46777-.1377-.57129-.37109-.13965-.31543.00195-.68457.31738-.8252l2.74121-1.2207c.3125-.13672.68457.00098.8252.31738.13965.31543-.00195.68457-.31738.8252l-2.74121,1.2207c-.08203.03613-.16895.05371-.25391.05371Z'),
    ('#ffffff', 'm25.16113,18.2207c-.23926,0-.4668-.1377-.57129-.37109-.13965-.31445.00195-.68457.31738-.8252l2.74023-1.2207c.31348-.1377.68359.00098.8252.31738.13965.31445-.00195.68457-.31738.8252l-2.74023,1.2207c-.08203.03613-.16895.05371-.25391.05371Z'),
]


def velero_inline(cx, cy, size, fill_a=BLUE, fill_b=NAVY):
    src = open('assets/velero/icon-color.svg').read()
    paths = []
    for m in re.finditer(r'<path class="(cls-\d)" d="([^"]+)"/>', src):
        paths.append(f'<path fill="{fill_a if m.group(1)=="cls-2" else fill_b}" d="{m.group(2)}"/>')
    k = size / 1080.0
    return f'<g transform="translate({cx - size/2:.1f},{cy - size/2:.1f}) scale({k:.6f})">' + ''.join(paths) + '</g>'


def os_glyph(cx, cy, size, a=RED):
    k = size / 26.0
    body = ''.join(f'<path fill="{a if c==RED else c}" d="{d}"/>' for c, d in OS_GLYPH)
    return (f'<g transform="translate({cx - size/2:.1f},{cy - size/2:.1f}) scale({k:.4f}) '
            f'translate(-5.98,-6.08)">' + body + '</g>')


def starfield():
    rand = lambda i: (math.sin(i * 12.9898) * 43758.5453) % 1
    out = []
    for i in range(110):
        x, y = rand(i) * W, rand(i + 500) * H * .82
        r = .5 + rand(i + 900) * 1.3
        dur, beg = 2.4 + rand(i + 80) * 3.4, -rand(i + 40) * 6
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.2f}" fill="#e6f7ff" opacity=".6">'
                   f'<animate attributeName="opacity" values=".1;.85;.1" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/></circle>')
    return '\n'.join(out)


def rays():
    """Four beams from the top-right tearing toward the shield face."""
    tx, ty = CONTACT                   # shield rim, right side
    beams = [
        ((1584, -60), 30, .55, 3.4),
        ((1584, 70), 36, .48, 4.2),
        ((1584, 190), 26, .55, 3.8),
        ((1500, 330), 22, .42, 4.6),
    ]
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
    return '\n'.join(out)


def sparks():
    """Impact sparks at the shield rim, drawn over the shield."""
    tx, ty = CONTACT
    out = []
    for k in range(8):
        a = math.radians(-118 + k * 22)
        r1, r2 = 6, 22 + (k % 4) * 12
        out.append(f'<line x1="{tx + math.cos(a)*r1:.0f}" y1="{ty + math.sin(a)*r1:.0f}" '
                   f'x2="{tx + math.cos(a)*r2:.0f}" y2="{ty + math.sin(a)*r2:.0f}" stroke="{WARN}" '
                   f'stroke-width="2.2" stroke-linecap="round" opacity="0">'
                   f'<animate attributeName="opacity" values="0;.95;0" dur="{1.5 + k*.19:.2f}s" repeatCount="indefinite"/></line>')
    return '\n'.join(out)


def k8s_wheel(cx, cy, r):
    spokes = ''.join(
        f'<line x1="{cx}" y1="{cy}" x2="{cx + math.cos(math.radians(360*k/7 - 90))*r*.7:.1f}" '
        f'y2="{cy + math.sin(math.radians(360*k/7 - 90))*r*.7:.1f}" stroke="{BLUE}" stroke-width="{max(2, r*.075):.1f}" stroke-linecap="round"/>'
        for k in range(7))
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="{r*.085:.1f}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*.34:.0f}" fill="none" stroke="{BLUE}" stroke-width="{r*.075:.1f}"/>' + spokes)




def icon_bucket():
    """Object store: bucket with data lines."""
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
            '<path d="M-17,-12 L17,-12 L12,18 L-12,18 Z"/>'
            '<ellipse cx="0" cy="-12" rx="17" ry="6"/>'
            '<path d="M-13,-2 L13,-2 M-11,8 L11,8" opacity=".65"/></g>')


def icon_disk():
    """Disk snapshot: drive platter with flash."""
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
            '<rect x="-19" y="-13" width="38" height="26" rx="4"/>'
            '<circle cx="0" cy="0" r="6.5"/>'
            '<path d="M12,-19 L9,-12 L14,-12 L10,-4" stroke="#7fd4e4"/></g>')


def icon_pod():
    """Pod backup: hex pod shell."""
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round">'
            '<path d="M0,-18 L16,-9 L16,9 L0,18 L-16,9 L-16,-9 Z"/>'
            '<path d="M0,-9 L8,-4.5 L8,4.5 L0,9 L-8,4.5 L-8,-4.5 Z" opacity=".65"/></g>')


def icon_config():
    """Config backup: document with fields."""
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
            '<path d="M-12,-16 L6,-16 L14,-8 L14,16 L-12,16 Z"/>'
            '<path d="M6,-16 L6,-8 L14,-8"/>'
            '<path d="M-6,-3 L8,-3 M-6,5 L8,5 M-6,12 L2,12" opacity=".65"/></g>')


def pod(cx, cy, size, inner, label, label_w):
    w, h = size * 1.5, size * .42
    return f'''<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0"
     dur="{6.2 + (cx % 5) * .4:.1f}s" begin="-{(cx % 7) / 2:.1f}s" repeatCount="indefinite"/>
  <ellipse cx="{cx}" cy="{cy + h*1.1:.0f}" rx="{w*.52:.0f}" ry="{h*.26:.0f}" fill="#010d18" opacity=".75"/>
  <path d="M{cx-w/2:.0f},{cy} L{cx:.0f},{cy-h/2:.0f} L{cx+w/2:.0f},{cy} L{cx:.0f},{cy+h/2:.0f} Z"
        fill="#0a2436" stroke="#14405c" stroke-width="1.5"/>
  <path d="M{cx-w/2:.0f},{cy} L{cx:.0f},{cy+h/2:.0f} L{cx+w/2:.0f},{cy}" fill="none" stroke="#1c5a80" stroke-width="1.2" opacity=".8"/>
  <g transform="translate({cx},{cy})">{inner}</g>
</g>
<g transform="translate({cx - label_w/2:.1f},{cy + h/2 + 42:.0f}) scale(0.011,-0.011)" fill="#7fb4cf">{label}</g>'''


def shield():
    kr = SH_R * .60
    glow = f'<circle cx="{SH_X}" cy="{SH_Y}" r="{SH_R+10}" fill="none" stroke="{CYAN}" stroke-width="1.3" opacity=".45"/>'
    crest = velero_inline(SH_X, SH_Y, kr * 2, BLUE, '#04141f')
    return f'''<g>
  <circle cx="{SH_X}" cy="{SH_Y}" r="{SH_R}" fill="none" stroke="{BLUE}" stroke-width="5">
    <animate attributeName="stroke-opacity" values="1;.5;1" dur="4.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{SH_X}" cy="{SH_Y}" r="{SH_R-9}" fill="url(#shieldGrad)" stroke="#0f4a6d" stroke-width="1.8"/>
  {glow}
  <g clip-path="url(#shieldClip)">{crest}
    <rect x="{SH_X - SH_R*2:.0f}" y="{SH_Y - SH_R*.9:.0f}" width="{SH_R*4:.0f}" height="{SH_R*.8:.0f}"
          fill="url(#shimmer)" transform="rotate(-24 {SH_X} {SH_Y})">
      <animateTransform attributeName="transform" type="translate" values="-340 0;340 0" dur="5.2s" repeatCount="indefinite"
        additive="sum"/>
    </rect>
  </g>
</g>'''


def character(avatar):
    sx, sy = 996, 244
    cx0 = HEAD_X
    cape = (f'M{cx0-34},{HEAD_Y+46} C{cx0-112},{HEAD_Y+92} {cx0-146},{H-84} {cx0-158},{H-8} '
            f'L{cx0-66},{H-8} C{cx0-60},{H-120} {cx0-46},{HEAD_Y+96} {cx0-30},{HEAD_Y+62} Z')
    neck = f'M{cx0-13},{HEAD_Y+HEAD_R-4} L{cx0+13},{HEAD_Y+HEAD_R-4} L{cx0+15},{HEAD_Y+66} L{cx0-15},{HEAD_Y+66} Z'
    torso = (f'M{cx0-44},{HEAD_Y+58} C{cx0-52},{HEAD_Y+112} {cx0-54},{H-92} {cx0-52},{H-64} '
             f'L{cx0+40},{H-64} C{cx0+44},{H-96} {cx0+52},{HEAD_Y+108} {cx0+40},{HEAD_Y+62} Z')
    legs = (f'M{cx0-46},{H-70} L{cx0-38},{H-8} L{cx0-2},{H-8} L{cx0+2},{H-70} Z '
            f'M{cx0+8},{H-70} L{cx0+14},{H-8} L{cx0+50},{H-8} L{cx0+42},{H-70} Z')
    return f'''<g>
  <path d="{cape}" fill="#08161f"/>
  <path d="{legs}" fill="{INK}"/>
  <path d="{neck}" fill="{INK}"/>
  <path d="{torso}" fill="{INK}"/>
  <circle cx="{cx0-40}" cy="{HEAD_Y+70}" r="15" fill="{INK}"/>
  <circle cx="{cx0+38}" cy="{HEAD_Y+70}" r="15" fill="{INK}"/>
  <path d="{torso}" fill="none" stroke="#1b4f70" stroke-width="1.6" opacity=".9"/>
  <line x1="{sx}" y1="{sy}" x2="{GRIP[0]:.0f}" y2="{GRIP[1]:.0f}" stroke="{INK}"
        stroke-width="25" stroke-linecap="round"/>
  <line x1="{sx}" y1="{sy}" x2="{GRIP[0]:.0f}" y2="{GRIP[1]:.0f}" stroke="#1b4f70"
        stroke-width="1.4" stroke-linecap="round" opacity=".6"/>
  <circle cx="{HEAD_X}" cy="{HEAD_Y}" r="{HEAD_R+9}" fill="#0a2233" stroke="{CYAN}" stroke-width="2.4"/>
  <image href="{avatar}" x="{HEAD_X-HEAD_R}" y="{HEAD_Y-HEAD_R}" width="{2*HEAD_R}" height="{2*HEAD_R}" clip-path="url(#headClip)"/>
  <circle cx="{HEAD_X}" cy="{HEAD_Y}" r="{HEAD_R}" fill="none" stroke="{CYAN}" stroke-width="1.5" opacity=".75"/>
</g>'''


def waves():
    """Period-320 wave rows, drawn well past both edges so the loop never shows a gap."""
    rows = [(350, BLUE, 6, .75, 14), (368, '#1d428a', 11, .95, 18), (386, '#7fd4e4', 4, .45, 11)]
    out = []
    for y, c, wd, op, dur in rows:
        d = (f'M-320,{y} Q-240,{y-16} -160,{y} T0,{y} T160,{y} T320,{y} T480,{y} T640,{y} '
             f'T800,{y} T960,{y} T1120,{y} T1280,{y} T1440,{y} T1600,{y} T1760,{y} T1920,{y} '
             f'T2080,{y} T2240,{y}')
        out.append(f'<g opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                   f'values="0 0;-320 0" dur="{dur}s" repeatCount="indefinite"/>'
                   f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{wd}" stroke-linecap="round"/></g>')
    return '\n'.join(out)


def main():
    import json
    tx = json.load(open('assets/fonts/paths.json'))
    avatar = 'data:image/jpeg;base64,' + base64.b64encode(open('assets/avatar/kaovilai.jpg', 'rb').read()).decode()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
  aria-label="Tiger Kaovilai raises a glowing Velero shield, deflecting red danger rays from space away from Kubernetes and OpenShift clusters">
  <defs>
    <radialGradient id="bg" cx=".3" cy=".05" r="1.15"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{DEEP}"/></radialGradient>
    <radialGradient id="dangerGrad" cx="1" cy=".5" r="1">
      <stop offset="0" stop-color="{RED}" stop-opacity=".9"/>
      <stop offset=".5" stop-color="{RED}" stop-opacity=".45"/>
      <stop offset="1" stop-color="{WARN}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="safeGlow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{BLUE}" stop-opacity=".2"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
    <radialGradient id="shieldGrad" cx=".35" cy=".3" r=".85"><stop offset="0" stop-color="#0d3350"/><stop offset="1" stop-color="#04141f"/></radialGradient>
    <linearGradient id="shimmer" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#dff6ff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="headClip"><circle cx="{HEAD_X}" cy="{HEAD_Y}" r="{HEAD_R}"/></clipPath>
    <clipPath id="shieldClip"><circle cx="{SH_X}" cy="{SH_Y}" r="{SH_R*.6:.0f}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <ellipse cx="520" cy="330" rx="640" ry="260" fill="url(#safeGlow)"/>
  {starfield()}

  {rays()}

  <g transform="translate({(366+750)/2 - tx['li_cap']['width']*0.012/2:.1f},198) scale(0.012,-0.012)" fill="#5f8ba1">{tx['li_cap']['body']}</g>
  {pod(366, 258, 48, icon_bucket(), tx['li_obj']['body'], tx['li_obj']['width']*0.011)}
  {pod(494, 258, 48, icon_disk(), tx['li_snap']['body'], tx['li_snap']['width']*0.011)}
  {pod(622, 258, 48, icon_pod(), tx['li_pod']['body'], tx['li_pod']['width']*0.011)}
  {pod(750, 258, 48, icon_config(), tx['li_cfg']['body'], tx['li_cfg']['width']*0.011)}

  {waves()}
  {character(avatar)}
  {shield()}
  {sparks()}
  <circle cx="{GRIP[0]:.0f}" cy="{GRIP[1]:.0f}" r="13" fill="{INK}" stroke="#1b4f70" stroke-width="1.5"/>

  <g transform="translate(56,78) scale(0.06,-0.06)" fill="#eaf6fb">{tx['li_name']['body']}</g>
  <g transform="translate(58,120) scale(0.02,-0.02)" fill="#8fb4c6">{tx['li_sub']['body']}</g>
</svg>'''
    open('linkedin-header.svg', 'w').write(svg)
    print('linkedin-header.svg', len(svg), 'bytes')


if __name__ == '__main__':
    main()
