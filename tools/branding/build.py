#!/usr/bin/env python3
"""Build index.html + kaovilai-border.svg from templates, injecting logo paths and fonts."""
import base64
import json
import re

RING_MAP = {
    '#eb2126': '#ee0000',
    '#db212e': '#cc0000',
    '#c22133': '#a60000',
    '#ba2133': '#a60000',
    '#ad213b': '#8f0000',
}


RING_IDS = ('path44560', 'path44564', 'path44572', 'path44576', 'path44584', 'path44588')

OSICON = 'assets/osicon/Technology_icon-Red_Hat-OpenShift-Standard-RGB.svg'
OSICON_RED = 'uuid-5e11f11b-3126-4566-8f81-fea0df077e5d'
OSICON_WHITE = 'uuid-67f9f3e7-b465-44b3-8fd2-3cbfa62cad35'
OSICON_GRAY = 'uuid-498079cb-8749-435b-92e1-7b9cc8be4a84'


def ring_paths():
    """OpenShift technology-icon glyph: red-50 arcs + white tick strokes (fills recolored)."""
    src = open(OSICON).read()
    paths = re.findall(r'<path class="(uuid-[0-9a-f-]+)" d="([^"]+)"/>', src)
    red = [d for c, d in paths if c == OSICON_RED]
    white = [d for c, d in paths if c == OSICON_WHITE]
    assert len(red) == 2 and len(white) == 4, f'glyph paths red={len(red)} white={len(white)}'
    grey = [d for c, d in paths if c == OSICON_GRAY]
    assert len(grey) == 1, 'expected one grey rounded-rect outline path'
    out = ([f'<path fill="#ee0000" d="{d}"/>' for d in red] +
           [f'<path fill="#ffffff" d="{d}"/>' for d in white])
    return ''.join(out)


def velero_pairs():
    src = open('assets/velero/icon-color.svg').read()
    pairs = re.findall(r'<path class="(cls-\d)" d="([^"]+)"/>', src)
    assert len(pairs) == 11, f'expected 11 velero paths, got {len(pairs)}'
    return pairs


def vel_paths(color_a, color_b):
    out = []
    for cls, d in velero_pairs():
        fill = color_a if cls == 'cls-2' else color_b
        out.append(f'<path fill="{fill}" d="{d}"/>')
    return ''.join(out)


def vel_mask_groups():
    """Velero silhouette as ink (blue bands) minus knockout (white separators)."""
    ink, cut = [], []
    for cls, d in velero_pairs():
        (ink if cls == 'cls-2' else cut).append(f'<path d="{d}"/>')
    return ''.join(ink), ''.join(cut)


def vel_lines():
    """Unused: separator gaps come from the mask's widened cut strokes."""
    return ''


def css_mask_svg():
    ink, cut = vel_mask_groups()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080">'
           '<mask id="m"><g fill="#fff">' + ink + '</g>'
           '<g fill="#000" stroke="#000" stroke-width="9" stroke-linejoin="round">' + cut + '</g></mask>'
           '<rect width="1080" height="1080" fill="#fff" mask="url(#m)"/></svg>')
    return base64.b64encode(svg.encode()).decode()


def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()


def main():
    rp = ring_paths()
    vel_var = vel_paths('var(--vel-a,#239de0)', 'var(--vel-b,#062238)')
    vel_lit = vel_paths('#239de0', '#062238')
    vel_ink, vel_cut = vel_mask_groups()
    avatar = b64('assets/avatar/kaovilai.jpg')

    html = open('index.template.html').read()
    html = (html.replace('@@F700@@', b64('assets/fonts/RedHatDisplay-Bold.woff2'))
                .replace('@@F500@@', b64('assets/fonts/RedHatDisplay-Medium.woff2'))
                .replace('@@F400@@', b64('assets/fonts/RedHatText-Regular.woff2'))
                .replace('@@RING_PATHS@@', rp)
                .replace('@@VEL_PATHS_VAR@@', vel_var)
                .replace('@@VELMASK@@', css_mask_svg())
                .replace('@@AVATAR@@', avatar))
    open('index.html', 'w').write(html)

    tx = json.load(open('assets/fonts/paths.json'))
    svg = open('border.template.svg').read()
    svg = (svg.replace('@@TX_BN_NAME@@', tx['bn_name']['body'])
              .replace('@@TX_BN_SUB1@@', tx['bn_sub1']['body'])
              .replace('@@TX_BN_SUB2@@', tx['bn_sub2']['body'])
              .replace('@@RING_PATHS@@', rp)
              .replace('@@VEL_PATHS_LIT@@', vel_lit)
              .replace('@@VEL_INK@@', vel_ink)
              .replace('@@VEL_CUT@@', vel_cut)
              .replace('@@AVATAR@@', avatar))
    open('kaovilai-border.svg', 'w').write(svg)
    print('index.html', len(html), 'bytes; kaovilai-border.svg', len(svg), 'bytes')


if __name__ == '__main__':
    main()
