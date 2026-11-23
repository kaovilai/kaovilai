#!/usr/bin/env python3
"""One layout engine, one scene, every platform cover.

The scene (name block, 4 backup pods, Velero shield, danger rays, waves) is
laid out from a single set of ratios applied to each platform's SAFE BOX --
the rectangle that survives every crop the platform applies. Add a platform by
adding a preset; nothing else changes.

Run from a directory that has the local-only inputs:
  assets/fonts/paths.json, assets/velero/icon-color.svg, assets/avatar/kaovilai.jpg
  (see tools/branding/README.md), then copy the written out/*.svg into assets/.
"""
import base64
import json
import math
import os
import re

RED, BLUE, DEEP, NAVY = '#ee0000', '#239de0', '#041a2c', '#062238'
CYAN, WARN, INK = '#00c1d5', '#f0ab00', '#0b1622'
NAME_INK, SUB_INK, CAP_INK, LABEL_INK = '#eaf6fb', '#8fb4c6', '#5f8ba1', '#7fb4cf'

# OpenShift technology-icon glyph (2 red arcs + 4 white ticks), tight-crop 26-unit box
OS_GLYPH = [
    (RED, 'm18.95117,28.63379c-2.19141,0-4.35352-.75586-6.12207-2.21777-.26562-.21973-.30273-.61328-.08301-.87988s.6123-.30273.87988-.08301c2.46875,2.04102,5.82129,2.49902,8.74805,1.19727,2.9248-1.30273,4.82715-4.10059,4.96387-7.30273.01465-.34473.29297-.6543.65039-.59766.34473.01465.6123.30566.59766.65039-.15625,3.67969-2.3418,6.89551-5.7041,8.39258-1.26758.56445-2.60449.84082-3.93066.84082Z'),
    (RED, 'm9.97363,19.22656c-.00879,0-.01855,0-.02832-.00098-.34473-.01562-.61133-.30762-.5957-.6543.16602-3.66797,2.35156-6.87402,5.70312-8.36621,3.36328-1.49609,7.21484-.96875,10.05273,1.37695.26562.21973.30273.61328.08301.87988s-.61328.30371-.87988.08301c-2.46973-2.04102-5.82227-2.5-8.74805-1.19727-2.91602,1.29785-4.81738,4.08789-4.96289,7.28027-.01465.33496-.29102.59668-.62402.59668Z'),
    ('#ffffff', 'm10.09863,22.19043c-.23926,0-.4668-.1377-.57129-.37109-.13965-.31445.00195-.68457.31738-.8252l2.74023-1.2207c.3125-.13867.68359.00098.8252.31738.13965.31445-.00195.68457-.31738.8252l-2.74023,1.2207c-.08203.03613-.16895.05371-.25391.05371Z'),
    ('#ffffff', 'm8.83105,25.49023c-.23926,0-.46777-.1377-.57129-.37109-.13965-.31543.00195-.68457.31738-.8252l2.74121-1.21973c.3125-.1377.68457.00098.8252.31738.13965.31543-.00195.68457-.31738.8252l-2.74121,1.21973c-.08203.03613-.16895.05371-.25391.05371Z'),
    ('#ffffff', 'm26.42773,14.91992c-.23926,0-.46777-.1377-.57129-.37109-.13965-.31543.00195-.68457.31738-.8252l2.74121-1.2207c.3125-.13672.68457.00098.8252.31738.13965.31543-.00195.68457-.31738.8252l-2.74121,1.2207c-.08203.03613-.16895.05371-.25391.05371Z'),
    ('#ffffff', 'm25.16113,18.2207c-.23926,0-.4668-.1377-.57129-.37109-.13965-.31445.00195-.68457.31738-.8252l2.74023-1.2207c.31348-.1377.68359.00098.8252.31738.13965.31445-.00195.68457-.31738.8252l-2.74023,1.2207c-.08203.03613-.16895.05371-.25391.05371Z'),
]

# ---- platform presets -------------------------------------------------------
# box = (x0, x1, y0, y1): the safe area that every crop of this platform keeps.
# ms = optional per-platform vertical scale for the waves (dense 4:1 covers).
PRESETS = {
    'linkedin': dict(
        W=1584, H=396, box=(300, 1568, 30, 366), figure=True,
        out='assets/linkedin/header-1584x396.svg',
        desc='LinkedIn cover: full bleed, profile photo overlaps bottom-left'),
    'x': dict(
        W=1500, H=500, box=(250, 1250, 60, 440),
        out='assets/x/header-1500x500.svg',
        desc="X header: 60px cropped top/bottom, 2:1 mobile copies cut 250px/side"),
    'facebook': dict(
        W=1640, H=856, box=(200, 1570, 214, 642),
        out='assets/facebook/cover-1640x856.svg',
        desc='Facebook cover: 16:9 desktop crops 59px off each side, 2.4:1 mobile keeps the central band'),
    'youtube': dict(
        W=2560, H=1440, box=(507, 2053, 508, 932), figure=True, ray_run=.45,
        out='assets/youtube/banner-2560x1440.svg',
        desc='YouTube banner: TV/desktop/mobile all show the central 1546x423 safe area'),
}

# ---- scene ratios (all relative to the safe box height) ---------------------
K = dict(
    shield_r=.40,          # shield radius
    name=.16, sub=.052, cap=.031,
    name_dy=-.15, sub_dy=-.025, cap_dy=.115,
    pod=.126, pod_gap=.30, pod_dy=.30,
    contact_dx=.92, contact_dy=-.23,
    head_dx=-.62, head_dy=-.10, head_r=.112,
    ray_run=.24,          # canvas kept clear right of the shield for the beams
    pad=.02,               # box padding for text starts
)


def layout(p):
    x0, x1, y0, y1 = p['box']
    bh = y1 - y0
    cy = (y0 + y1) / 2
    L = dict(W=p['W'], H=p['H'], bh=bh, cy=cy, y0=y0, y1=y1, x0=x0)
    L['R'] = K['shield_r'] * bh
    L['shx'] = x1 - L['R'] - p.get('ray_run', K['ray_run']) * bh
    L['shy'] = cy
    L['tx'] = x0 + K['pad'] * p['W']
    L['name_sz'] = K['name'] * bh
    L['sub_sz'] = K['sub'] * bh
    L['cap_sz'] = K['cap'] * bh
    L['name_y'] = cy + K['name_dy'] * bh
    L['sub_y'] = cy + K['sub_dy'] * bh
    L['cap_y'] = cy + K['cap_dy'] * bh
    L['pod_sz'] = K['pod'] * bh
    L['pod_gap'] = K['pod_gap'] * bh
    L['pod_y'] = cy + K['pod_dy'] * bh
    L['contact'] = (L['shx'] + K['contact_dx'] * L['R'], cy + K['contact_dy'] * L['R'])
    L['head'] = (L['shx'] + K['head_dx'] * bh, cy + K['head_dy'] * bh, K['head_r'] * bh)
    return L


# ---- glyph / asset helpers --------------------------------------------------
def velero_inline(cx, cy, size, fill_a=BLUE, fill_b=NAVY):
    src = open('assets/velero/icon-color.svg').read()
    paths = []
    for m in re.finditer(r'<path class="(cls-\d)" d="([^"]+)"/>', src):
        paths.append(f'<path fill="{fill_a if m.group(1) == "cls-2" else fill_b}" d="{m.group(2)}"/>')
    k = size / 1080.0
    return f'<g transform="translate({cx - size/2:.1f},{cy - size/2:.1f}) scale({k:.6f})">' + ''.join(paths) + '</g>'


def os_ring(cx, cy, face_r):
    """Inlined OpenShift technology-icon glyph, hole-centred, swaying."""
    body = ''.join(f'<path fill="{c}" d="{d}"/>' for c, d in OS_GLYPH)
    box = face_r * 1.25 * 26 / 9
    return (f'<g transform="translate({cx},{cy})">'
            f'<animateTransform attributeName="transform" type="rotate" values="-10;10;-10" '
            f'keyTimes="0;0.5;1" dur="12s" repeatCount="indefinite" additive="sum"/>'
            f'<svg viewBox="5.98 6.08 26 26" x="{-box/2:.1f}" y="{-box/2:.1f}" '
            f'width="{box:.1f}" height="{box:.1f}">{body}</svg></g>')


def icon_bucket():
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
            '<path d="M-17,-12 L17,-12 L12,18 L-12,18 Z"/>'
            '<ellipse cx="0" cy="-12" rx="17" ry="6"/>'
            '<path d="M-13,-2 L13,-2 M-11,8 L11,8" opacity=".65"/></g>')


def icon_disk():
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
            '<rect x="-19" y="-13" width="38" height="26" rx="4"/>'
            '<circle cx="0" cy="0" r="6.5"/>'
            '<path d="M12,-19 L9,-12 L14,-12 L10,-4" stroke="#7fd4e4"/></g>')


def icon_pod():
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round">'
            '<path d="M0,-18 L16,-9 L16,9 L0,18 L-16,9 L-16,-9 Z"/>'
            '<path d="M0,-9 L8,-4.5 L8,4.5 L0,9 L-8,4.5 L-8,-4.5 Z" opacity=".65"/></g>')


def icon_config():
    return ('<g fill="none" stroke="#239de0" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
            '<path d="M-12,-16 L6,-16 L14,-8 L14,16 L-12,16 Z"/>'
            '<path d="M6,-16 L6,-8 L14,-8"/>'
            '<path d="M-6,-3 L8,-3 M-6,5 L8,5 M-6,12 L2,12" opacity=".65"/></g>')


def pod(cx, cy, size, inner, label, label_w, label_sz):
    """Backup pod tile, scaled from the safe box; label sits a fixed ratio below."""
    k = size / 48.0                       # icons are drawn for a 48px tile
    w = size * 1.5
    lw, lh = size * .42, size * .22
    ly = cy + lh / 2 + label_sz * 1.9
    return f'''<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0"
     dur="{6.2 + (cx % 5) * .4:.1f}s" begin="-{(cx % 7) / 2:.1f}s" repeatCount="indefinite"/>
  <ellipse cx="{cx}" cy="{cy + lh*2.2:.0f}" rx="{w*.52:.0f}" ry="{lh*.55:.0f}" fill="#010d18" opacity=".75"/>
  <path d="M{cx-w/2:.0f},{cy} L{cx:.0f},{cy-lh:.0f} L{cx+w/2:.0f},{cy} L{cx:.0f},{cy+lh:.0f} Z"
        fill="#0a2436" stroke="#14405c" stroke-width="1.5"/>
  <g transform="translate({cx},{cy}) scale({k:.4f})">{inner}</g>
</g>
<g transform="translate({cx - label_w/2:.1f},{ly:.0f}) scale({label_sz/1000:.4f},-{label_sz/1000:.4f})" fill="{LABEL_INK}">{label}</g>'''


def shield(L):
    cx, cy, R = L['shx'], L['shy'], L['R']
    kr = R * .60
    crest = velero_inline(cx, cy, kr * 2, BLUE, '#062a45')
    return f'''<g>
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{BLUE}" stroke-width="{R*.033:.1f}">
    <animate attributeName="stroke-opacity" values="1;.5;1" dur="4.2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{cx}" cy="{cy}" r="{R*.94:.1f}" fill="url(#shieldGrad)" stroke="#0f4a6d" stroke-width="{R*.013:.1f}"/>
  <circle cx="{cx}" cy="{cy}" r="{R*1.07:.1f}" fill="none" stroke="{CYAN}" stroke-width="{R*.009:.1f}" opacity=".45"/>
  <g clip-path="url(#shieldClip)">{crest}
    <rect x="{cx - R*2:.0f}" y="{cy - R*.9:.0f}" width="{R*4:.0f}" height="{R*.8:.0f}"
          fill="url(#shimmer)" transform="rotate(-24 {cx} {cy})">
      <animateTransform attributeName="transform" type="translate" values="-{R*2.2:.0f} 0;{R*2.2:.0f} 0"
        dur="5.2s" repeatCount="indefinite" additive="sum"/>
    </rect>
  </g>
</g>'''


def rays(L):
    """Beams defined by ANGLE through the contact point, so every canvas gets the
    same slopes; the canvas edge only decides how much of each beam is visible."""
    tx, ty = L['contact']
    bh, W = L['bh'], L['W']
    reach = 2.4 * W
    beams = [(38, .115, .55, 3.4), (14, .135, .50, 4.2),
             (-9, .095, .50, 3.8), (-27, .070, .40, 4.6)]
    out = []
    for ang, wfrac, op, dur in beams:
        a = math.radians(ang)
        dx, dy = math.cos(a), -math.sin(a)          # unit vector away from contact
        ex, ey = tx + dx * reach, ty + dy * reach   # far end (off-canvas)
        wdt = wfrac * bh
        px, py = -dy * wdt / 2, dx * wdt / 2        # perpendicular half-width
        out.append(f'''<g opacity="{op}">
  <path d="M{ex + px:.0f},{ey + py:.0f} L{tx:.0f},{ty:.0f} L{ex - px:.0f},{ey - py:.0f} Z" fill="url(#dangerGrad)">
    <animate attributeName="opacity" values="1;.55;1" dur="{dur}s" repeatCount="indefinite"/>
  </path>
  <path d="M{ex:.0f},{ey:.0f} L{tx:.0f},{ty:.0f}" stroke="{WARN}" stroke-width="{max(2, wdt/7):.0f}" stroke-linecap="round"
        stroke-dasharray="16 30" opacity=".5">
    <animate attributeName="stroke-dashoffset" from="0" to="-184" dur="{dur}s" repeatCount="indefinite"/>
  </path>
</g>''')
    return '\n'.join(out)


def sparks(L):
    tx, ty = L['contact']
    out = []
    for k in range(8):
        a = math.radians(-118 + k * 22)
        r1, r2 = L['R'] * .05, L['R'] * (.18 + (k % 4) * .10)
        out.append(f'<line x1="{tx + math.cos(a)*r1:.0f}" y1="{ty + math.sin(a)*r1:.0f}" '
                   f'x2="{tx + math.cos(a)*r2:.0f}" y2="{ty + math.sin(a)*r2:.0f}" stroke="{WARN}" '
                   f'stroke-width="{max(2, L["R"]*.018):.1f}" stroke-linecap="round" opacity="0">'
                   f'<animate attributeName="opacity" values="0;.95;0" dur="{1.5 + k*.19:.2f}s" repeatCount="indefinite"/></line>')
    return '\n'.join(out)


def stars(W, H):
    rand = lambda i: (math.sin(i * 12.9898) * 43758.5453) % 1
    out = []
    for i in range(int(W * H / 32000)):
        x, y = rand(i) * W, rand(i + 500) * H * .8
        r = .5 + rand(i + 900) * 1.3
        dur, beg = 2.4 + rand(i + 80) * 3.4, -rand(i + 40) * 6
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.2f}" fill="#e6f7ff" opacity=".6">'
                   f'<animate attributeName="opacity" values=".1;.85;.1" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/></circle>')
    return '\n'.join(out)


def waves(L):
    y1 = L['y1']
    bh = L['bh']
    # tile runs to the canvas edge plus one full cycle (360) of travel each way,
    # so the -360 translate never exposes an edge on wide canvases
    end = L['W'] + 720
    rows = [(y1 - .095 * bh, BLUE, .016 * bh, .7, 14),
            (y1 + .020 * bh, '#1d428a', .030 * bh, .9, 18),
            (y1 + .090 * bh, '#7fd4e4', .011 * bh, .42, 11)]
    out = []
    for y, c, wd, op, dur in rows:
        d = (f'M-360,{y:.0f} Q-270,{y-20:.0f} -180,{y:.0f} '
             + ' '.join(f'T{x},{y:.0f}' for x in range(0, end + 1, 180)))
        out.append(f'<g opacity="{op}"><animateTransform attributeName="transform" type="translate" '
                   f'values="0 0;-360 0" dur="{dur}s" repeatCount="indefinite"/>'
                   f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{max(2, wd):.1f}" stroke-linecap="round"/></g>')
    return '\n'.join(out)


def figure(L, avatar):
    """Cloaked guardian raising the shield. Only where the crop model leaves room.
    Grounded at the band bottom (feet in the waves), since on YouTube the band is
    the only part shown on desktop and mobile."""
    hx, hy, hr = L['head']
    s = hr / 42.0                      # drawing was tuned at a 42px head
    yb = L['y1'] + .04 * L['bh']       # ground line, just inside the wave rows
    sx, sy = hx + 44 * s, hy + 66 * s
    grip = (L['shx'] - L['R'] * .62, L['shy'] + L['R'] * .80)
    cape = (f'M{hx-34*s:.0f},{hy+52*s:.0f} C{hx-110*s:.0f},{hy+92*s:.0f} {hx-150*s:.0f},{yb-102*s:.0f} {hx-164*s:.0f},{yb:.0f} '
            f'L{hx+6*s:.0f},{yb:.0f} C{hx+2*s:.0f},{yb-112*s:.0f} {hx+16*s:.0f},{hy+96*s:.0f} {hx+34*s:.0f},{hy+52*s:.0f} Z')
    body = (f'M{hx-40*s:.0f},{hy+62*s:.0f} C{hx-52*s:.0f},{hy+96*s:.0f} {hx-54*s:.0f},{yb-134*s:.0f} {hx-52*s:.0f},{yb:.0f} '
            f'L{hx+50*s:.0f},{yb:.0f} C{hx+52*s:.0f},{yb-134*s:.0f} {hx+52*s:.0f},{hy+96*s:.0f} {hx+40*s:.0f},{hy+62*s:.0f} '
            f'C{hx+22*s:.0f},{hy+46*s:.0f} {hx-22*s:.0f},{hy+46*s:.0f} {hx-40*s:.0f},{hy+62*s:.0f} Z')
    return f'''<g>
  <path d="{cape}" fill="#060f16"/>
  <path d="{body}" fill="#123043"/>
  <path d="{body}" fill="none" stroke="#1b4f70" stroke-width="{1.6*s:.1f}" opacity=".9"/>
  <line x1="{sx:.0f}" y1="{sy:.0f}" x2="{grip[0]:.0f}" y2="{grip[1]:.0f}" stroke="{INK}"
        stroke-width="{25*s:.1f}" stroke-linecap="round"/>
  <line x1="{sx:.0f}" y1="{sy:.0f}" x2="{grip[0]:.0f}" y2="{grip[1]:.0f}" stroke="#1b4f70"
        stroke-width="{1.4*s:.1f}" stroke-linecap="round" opacity=".6"/>
  {os_ring(hx, hy, hr)}
  <circle cx="{hx}" cy="{hy}" r="{hr*1.045:.1f}" fill="#0a2233" stroke="{CYAN}" stroke-width="{2.4*s:.1f}"/>
  <image href="{avatar}" x="{hx-hr:.0f}" y="{hy-hr:.0f}" width="{2*hr:.0f}" height="{2*hr:.0f}" clip-path="url(#headClip)"/>
  <circle cx="{hx}" cy="{hy}" r="{hr:.0f}" fill="none" stroke="{CYAN}" stroke-width="{1.5*s:.1f}" opacity=".75"/>
  <circle cx="{grip[0]:.0f}" cy="{grip[1]:.0f}" r="{13*s:.1f}" fill="{INK}" stroke="#1b4f70" stroke-width="1.5"/>
</g>'''


def text_group(body, x, y, size, fill):
    return f'<g transform="translate({x:.0f},{y:.0f}) scale({size/1000:.4f},-{size/1000:.4f})" fill="{fill}">{body}</g>'


def scene(p):
    L = layout(p)
    W, H = L['W'], L['H']
    tx = json.load(open('assets/fonts/paths.json'))
    avatar = 'data:image/jpeg;base64,' + base64.b64encode(open('assets/avatar/kaovilai.jpg', 'rb').read()).decode()
    wpx = lambda key, size: tx[key]['width'] * size / 1000

    name_w = wpx('li_name', L['name_sz'])
    sub_w = wpx('li_sub', L['sub_sz'])
    cap_w = wpx('li_cap', L['cap_sz'])
    label_sz = L['pod_sz'] * .21
    icons = [('li_obj', icon_bucket()), ('li_snap', icon_disk()),
             ('li_pod', icon_pod()), ('li_cfg', icon_config())]
    span = (len(icons) - 1) * L['pod_gap']
    block_w = max(name_w, sub_w, span + L['pod_sz'] * 1.5)
    pod0 = L['tx'] + block_w / 2 - span / 2
    pods = '\n'.join(
        pod(pod0 + i * L['pod_gap'], L['pod_y'], L['pod_sz'], inner,
            tx[key]['body'], wpx(key, label_sz), label_sz)
        for i, (key, inner) in enumerate(icons))

    hx, hy, hr = L['head']
    fig = figure(L, avatar) if p.get('figure') else ''
    head_defs = (f'<clipPath id="headClip"><circle cx="{hx:.0f}" cy="{hy:.0f}" r="{hr:.0f}"/></clipPath>'
                 if p.get('figure') else '')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
  aria-label="Tiger Kaovilai raises a glowing Velero shield, deflecting red danger rays from space away from Kubernetes and OpenShift backups">
  <defs>
    <radialGradient id="bg" cx=".3" cy=".05" r="1.15"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{DEEP}"/></radialGradient>
    <radialGradient id="dangerGrad" cx="1" cy=".5" r="1">
      <stop offset="0" stop-color="{RED}" stop-opacity=".9"/>
      <stop offset=".5" stop-color="{RED}" stop-opacity=".45"/>
      <stop offset="1" stop-color="{WARN}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="safeGlow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{BLUE}" stop-opacity=".2"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
    <radialGradient id="impact" cx="1" cy=".5" r=".6"><stop offset="0" stop-color="{RED}" stop-opacity=".55"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></radialGradient>
    <radialGradient id="shieldGrad" cx=".35" cy=".3" r=".85"><stop offset="0" stop-color="#0d3350"/><stop offset="1" stop-color="#04141f"/></radialGradient>
    <linearGradient id="shimmer" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#dff6ff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    {head_defs}
    <clipPath id="shieldClip"><circle cx="{L['shx']:.0f}" cy="{L['shy']:.0f}" r="{L['R']*.60:.0f}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <ellipse cx="{(L['x0'] + L['shx'])/2:.0f}" cy="{L['y1']:.0f}" rx="{L['bh']*1.9:.0f}" ry="{L['bh']*.82:.0f}" fill="url(#safeGlow)"/>
  {stars(W, H)}

  {rays(L)}

  {text_group(tx['li_name']['body'], L['tx'], L['name_y'], L['name_sz'], NAME_INK)}
  {text_group(tx['li_sub']['body'], L['tx'] + 2, L['sub_y'], L['sub_sz'], SUB_INK)}
  {text_group(tx['li_cap']['body'], L['tx'] + block_w/2 - cap_w/2, L['cap_y'], L['cap_sz'], CAP_INK)}

  {pods}

  {waves(L)}
  {fig}
  <ellipse cx="{L['contact'][0] + L['R']*.17:.0f}" cy="{L['contact'][1]:.0f}" rx="{L['R']*1.05:.0f}" ry="{L['R']*1.33:.0f}" fill="url(#impact)" opacity=".8"/>
  {shield(L)}
  {sparks(L)}
</svg>'''


def main():
    os.makedirs('out', exist_ok=True)
    for name, p in PRESETS.items():
        svg = scene(p)
        path = os.path.join('out', os.path.basename(p['out']))
        open(path, 'w').write(svg)
        print(f'{name:9s} {p["W"]}x{p["H"]:5d} -> {path}')


if __name__ == '__main__':
    main()
