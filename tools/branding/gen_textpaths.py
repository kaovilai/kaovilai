#!/usr/bin/env python3
"""Regenerate assets/fonts/paths.json (text outlines) for banner + LinkedIn.
Run with /tmp/fontenv/bin/python (fonttools+brotli)."""
import json
import sys

sys.path.insert(0, '/home/tkaovila/.t3/scratch/2026-11-22-create-for-me-a-border-8d1fd450')
import text2path as t

BOLD = 'assets/fonts/RedHatDisplay-Bold.woff2'
MED = 'assets/fonts/RedHatDisplay-Medium.woff2'

SPECS = {
    # key: (text, font, size, letter_spacing)
    'bn_name': ('kaovilai', BOLD, 66, -1),
    'bn_sub1': ('OPENSHIFT × VELERO — BACK UP THE CLUSTER,', MED, 20, 2),
    'bn_sub2': ('RESTORE IT ANYWHERE.', MED, 20, 2),
    'li_name': ('Tiger Kaovilai', BOLD, 60, -0.5),
    'li_sub': ('VELERO MAINTAINER · OADP ENGINEER, RED HAT', MED, 20, 2),
    'li_obj': ('OBJECT STORE', MED, 12, 1.5),
    'li_snap': ('DISK SNAPSHOTS', MED, 12, 1.5),
    'li_pod': ('POD BACKUP', MED, 12, 1.5),
    'li_cfg': ('CONFIG BACKUP', MED, 12, 1.5),
    'li_cap': ('PROTECTED BY VELERO', MED, 12, 2.5),
}

out = {}
for key, (text, font, size, ls) in SPECS.items():
    parts, w = t.text_paths(text, font, size, ls)
    body = ''.join(f'<path d="{d}" transform="translate({gx:.3f},0)"/>' for d, gx, _ in parts)
    out[key] = {'width': round(w, 2), 'upm': t.upm_of(font), 'size': size, 'body': body}
json.dump(out, open('assets/fonts/paths.json', 'w'))
print('wrote paths.json', sum(len(v['body']) for v in out.values()), 'bytes of outlines')
