#!/usr/bin/env python3
"""Generate the animated SVGs embedded in README.md from the repo's own JSON data.

Inputs (repo root):  workstream-archive.json, open-prs.json, activity.json, repo-languages.json
Outputs:             assets/profile/{hero,ticker,impact,orbit,languages,pipeline,acct-*,bojangles}-{dark,light}.svg

Stdlib only. Output is deterministic for identical input (no timestamps from the
clock, seeded randomness), so the scheduled workflow only commits on real change.
Animations are pure CSS keyframes (no JS, which GitHub strips) and are disabled
under prefers-reduced-motion.
"""
import json
import math
import sys
from collections import Counter
from datetime import datetime, timedelta
from html import escape
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUT = ROOT / "assets" / "profile"
OWNER = "kaovilai"  # personal-namespace repos are excluded from the counts

FONT = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "dark": dict(
        bg1="#0d1117", bg2="#161b22", border="#30363d", text="#e6edf3",
        muted="#8b949e", grid="#21262d", accent="#ee0000", accent2="#ff6b6b",
        glow="#ee0000", chip="#21262d",
    ),
    "light": dict(
        bg1="#ffffff", bg2="#f6f8fa", border="#d0d7de", text="#1f2328",
        muted="#59636e", grid="#e6eaef", accent="#cc0000", accent2="#ee0000",
        glow="#ee0000", chip="#eaeef2",
    ),
}

LANE_COLORS = {
    "Velero": "#2ea8e0",
    "OADP": "#ee0000",
    "KubeVirt Data Mover": "#a371f7",
    "Kubernetes": "#326ce5",
    "Other": "#8b949e",
}

LANG_COLORS = {  # GitHub linguist colours; anything else gets a stable hashed hue
    "Go": "#00ADD8", "Shell": "#89e051", "Python": "#3572A5", "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a", "HTML": "#e34c26", "Java": "#b07219", "Kotlin": "#A97BFF",
    "Jinja": "#a52a22", "Makefile": "#427819", "Dockerfile": "#384d54", "Rust": "#dea584",
    "Ruby": "#701516", "C": "#555555", "C++": "#f34b7d", "Swift": "#F05138",
    "Dart": "#00B4AB", "Vue": "#41b883", "CSS": "#663399", "Starlark": "#76d275",
}

STATUS_COLORS = [  # (status, label, color)
    ("ready", "ready", "#3fb950"),
    ("waiting-merge", "waiting to merge", "#58a6ff"),
    ("ci-pending", "CI running", "#d29922"),
    ("failing-ci", "failing CI", "#f85149"),
    ("needs-attention", "needs attention", "#db6d28"),
    ("hold", "on hold", "#a371f7"),
    ("draft", "draft", "#6e7681"),
    ("stale", "stale", "#484f58"),
]


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def lane_for(repo, lane_votes):
    """Map a repo to a display lane: majority workstream vote, then name heuristics."""
    votes = lane_votes.get(repo)
    if votes:
        lane = votes.most_common(1)[0][0]
        if lane in LANE_COLORS:
            return lane
    low = repo.lower()
    if "velero" in low:
        return "Velero"
    if "oadp" in low:
        return "OADP"
    if "kubevirt" in low or "datamover" in low:
        return "KubeVirt Data Mover"
    return "Other"


def shell(w, h, t, body, title, desc, extra_css="", radius=16):
    """Common SVG wrapper: rounded card, shared CSS, reduced-motion guard."""
    css = f"""
    text {{ font-family: {FONT}; fill: {t['text']}; }}
    .mono {{ font-family: {MONO}; }}
    .muted {{ fill: {t['muted']}; }}
    .roll {{ transform: translateY(var(--to)); animation: roll 1.4s cubic-bezier(.2,.8,.2,1) backwards; }}
    @keyframes roll {{ from {{ transform: translateY(0); }} }}
    {extra_css}
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; }}
    }}"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
  <title id="t">{escape(title)}</title>
  <desc id="d">{escape(desc)}</desc>
  <defs>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
    <linearGradient id="hot" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/>
    </linearGradient>
    <radialGradient id="aura"><stop offset="0" stop-color="{t['glow']}" stop-opacity=".35"/><stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/></radialGradient>
    <clipPath id="clip"><rect width="{w}" height="{h}" rx="{radius}"/></clipPath>
  </defs>
  <style>{css}</style>
  <rect width="{w}" height="{h}" rx="{radius}" fill="url(#card)"/>
  <g clip-path="url(#clip)">
{body}
  </g>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{radius}" fill="none" stroke="{t['border']}"/>
</svg>
"""


def odometer(x, y, text, size, fill, delay, uid):
    """Digits that roll up to their final value. The resting state IS the final
    value, so with animations disabled the real number shows."""
    cw, lh = size * 0.62, size * 1.3
    out = []
    for i, ch in enumerate(text):
        px = x + i * cw
        style = f'class="mono" font-size="{size}" font-weight="700" text-anchor="middle" style="fill:{fill}"'
        if not ch.isdigit():
            out.append(f'<text {style} x="{px + cw / 2:.1f}" y="{y}">{escape(ch)}</text>')
            continue
        cid = f"{uid}{i}"
        digits = "".join(f'<text {style} x="{px + cw / 2:.1f}" y="{y + k * lh:.1f}">{k}</text>' for k in range(10))
        out.append(
            f'<clipPath id="{cid}"><rect x="{px:.1f}" y="{y - size * 0.85:.1f}" width="{cw:.1f}" height="{lh:.1f}"/></clipPath>'
            f'<g clip-path="url(#{cid})"><g class="roll" style="--to:{-int(ch) * lh:.1f}px;'
            f'animation-duration:{1.0 + 0.25 * (len(text) - i):.2f}s;animation-delay:{delay:.2f}s">{digits}</g></g>'
        )
    return "".join(out)


def ago(iso, now):
    secs = int((now - datetime.fromisoformat(iso.replace("Z", "+00:00"))).total_seconds())
    if secs < 3600:
        return f"{max(secs // 60, 1)}m ago"
    if secs < 86400:
        return f"{secs // 3600}h ago"
    return f"{secs // 86400}d ago"


# --------------------------------------------------------------------------- hero
def hero(t, s):
    w, h = 900, 250
    heat = s["heat"]
    dots = []
    days = [d for d in heat["dates"] if d >= heat["from"]]  # only days the feeds fully cover
    rows, step, size = 7, 22, 18
    cols = -(-len(days) // rows)
    x0, y0 = 868 - cols * step, 24
    peak = max((heat["days"].get(d, 0) for d in days), default=1) or 1
    shades = [t["grid"], "#7a1515", "#b31b1b", t["accent"], t["accent2"]]
    for i, day in enumerate(days):
        col, row = divmod(i, rows)
        x, y = x0 + col * step, y0 + row * step
        n = heat["days"].get(day, 0)
        lvl = 0 if n == 0 else 1 + min(3, int(3 * (n - 1) / max(peak - 1, 1)))
        dots.append(
            f'<rect class="dot{" hot" if lvl else ""}" x="{x}" y="{y}" width="{size}" height="{size}" rx="4" fill="{shades[lvl]}" '
            f'style="animation-delay:{col * 0.07:.2f}s,{2 + col * 0.18:.2f}s"><title>{day}: {n}</title></rect>'
        )
    live = (
        f'<g transform="translate({868 - 190},12)"><circle class="ping" cx="4" cy="0" r="4" fill="#3fb950"/><circle cx="4" cy="0" r="3" fill="#3fb950"/>'
        f'<text class="mono muted" x="14" y="3" font-size="10">LIVE · data as of {heat["asof"]}</text></g>'
        f'<text class="mono muted" x="868" y="{y0 + rows * step + 14}" font-size="10" text-anchor="end">1 square = 1 day, last {len(days)}</text>'
    )
    phrases = [
        "Velero maintainer",
        "OpenShift API for Data Protection @ Red Hat",
        "Cloud-native data protection for Kubernetes",
    ]
    phrase_svg = "\n".join(
        f'<text class="phrase p{i}" x="48" y="146" font-size="22" style="animation-delay:-{13 - 4 * i}s">{escape(p)}</text>'
        for i, p in enumerate(phrases)
    )
    chips = [
        (f"{s['merged_all']:,}", "PRs merged, all time"),
        (f"{s['merged_ytd']:,}", f"merged in {s['year']}"),
        (f"{s['open_prs']:,}", "PRs open now"),
        (f"{s['reviewed']:,}", f"reviewed, last {s['period_days']} days"),
    ]
    chip_svg = []
    cx = 48
    for ci, (val, label) in enumerate(chips):
        cw = max(150, 14 + len(label) * 7 + 14)
        chip_svg.append(
            f'<g transform="translate({cx},190)"><rect width="{cw}" height="44" rx="10" fill="{t["chip"]}" stroke="{t["border"]}"/>'
            f'{odometer(14, 20, val, 17, t["accent2"], 0.3 + ci * 0.2, f"od{ci}_")}'
            f'<text class="muted" x="14" y="36" font-size="11">{escape(label)}</text></g>'
        )
        cx += cw + 12
    body = f"""
    <circle class="drift1" cx="150" cy="40" r="210" fill="url(#aura)"/>
    <circle class="drift2" cx="760" cy="230" r="190" fill="url(#aura)"/>
    {''.join(dots)}
    {live}
    <text class="mono muted" x="48" y="50" font-size="13">~/kaovilai $ <tspan class="cursor" style="fill:{t['accent2']}">whoami</tspan></text>
    <text x="46" y="108" font-size="50" font-weight="800" letter-spacing="-1">Tiger Kaovilai</text>
    {phrase_svg}
    {''.join(chip_svg)}"""
    css = f"""
    .dot {{ transform-box: fill-box; transform-origin: center; animation: pop .5s backwards; }}
    .dot.hot {{ animation: pop .5s backwards, wave 6s ease-in-out infinite; }}
    @keyframes pop {{ from {{ transform: scale(0); opacity: 0; }} }}
    @keyframes wave {{ 0%,12%,100% {{ transform: scale(1); }} 6% {{ transform: scale(1.3); filter: brightness(1.5); }} }}
    .ping {{ transform-box: fill-box; transform-origin: center; animation: ping 2s ease-out infinite; }}
    @keyframes ping {{ from {{ transform: scale(1); opacity: .8; }} to {{ transform: scale(3.2); opacity: 0; }} }}
    .drift1 {{ animation: drift 18s ease-in-out infinite alternate; }}
    .drift2 {{ animation: drift 24s ease-in-out infinite alternate-reverse; }}
    @keyframes drift {{ from {{ transform: translate(0,0); }} to {{ transform: translate(70px,24px); }} }}
    .phrase {{ opacity: 0; animation: swap 12s ease-in-out infinite; fill: {t['muted']}; }}
    @keyframes swap {{
      0% {{ opacity: 0; transform: translateY(8px); }}
      5%,28% {{ opacity: 1; transform: translateY(0); }}
      33%,100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: .25; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p0 {{ opacity: 1; }} }}"""
    return shell(w, h, t, body, "Tiger Kaovilai",
                 "Velero maintainer and OADP engineer at Red Hat. Live totals from my public PR history.", css)


# --------------------------------------------------------------------------- accounts
# One small SVG per account: links inside an <img>-embedded SVG are inert on GitHub, so the
# README wraps each pill in an ordinary link instead.
ACCOUNTS = [  # key, name, subtitle, brand colour, monogram
    ("github", "GitHub", "kaovilai", "#6e7681", "GH"),
    ("gitlab", "GitLab", "kaovilai", "#fc6d26", "GL"),
    ("freedesktop", "freedesktop.org", "GitLab · kaovilai", "#3b82c4", "fd"),
]


def account(t, idx, name, sub, color, mono):
    w, h = 210, 52
    d = idx * 0.12
    body = f"""
    <clipPath id="pill"><rect width="{w}" height="{h}" rx="14"/></clipPath>
    <linearGradient id="gleam" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <g class="enter" style="animation-delay:{d:.2f}s">
      <rect class="edge" x="1" y="1" width="{w - 2}" height="{h - 2}" rx="13" fill="none" stroke="{color}" stroke-width="1.5" opacity=".55"/>
      <g class="badge" style="animation-delay:{d + 0.6:.2f}s">
        <rect x="12" y="10" width="32" height="32" rx="9" fill="{color}"/>
        <text class="mono" x="28" y="31" font-size="13" font-weight="800" text-anchor="middle" style="fill:#fff">{escape(mono)}</text>
      </g>
      <text x="56" y="25" font-size="14" font-weight="700">{escape(name)}</text>
      <text class="mono muted" x="56" y="40" font-size="10.5">{escape(sub)}</text>
      <g clip-path="url(#pill)"><rect class="gleam" x="-80" y="0" width="80" height="{h}" fill="url(#gleam)" style="animation-delay:{d + 1.5:.2f}s"/></g>
    </g>"""
    css = f"""
    .enter {{ animation: rise .6s cubic-bezier(.2,.8,.2,1) backwards; }}
    @keyframes rise {{ from {{ transform: translateY(8px); opacity: 0; }} }}
    .edge {{ stroke-dasharray: 1000; animation: trace 1.4s ease-out backwards; }}
    @keyframes trace {{ from {{ stroke-dashoffset: 1000; }} }}
    .badge {{ transform-box: fill-box; transform-origin: center; animation: breathe 3.6s ease-in-out infinite; }}
    @keyframes breathe {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.08); }} }}
    .gleam {{ animation: sweep 5s ease-in-out infinite; }}
    @keyframes sweep {{ 0% {{ transform: translateX(0); }} 40%,100% {{ transform: translateX(310px); }} }}"""
    return shell(w, h, t, body, f"{name} ({sub})", f"Link to my {name} profile.", css, radius=14)


# -------------------------------------------------------------------------- ticker
def ticker(t, s):
    w, h = 900, 56
    items, x = [], 0.0
    for it in s["recent_merged"]:
        color = LANE_COLORS.get(it["lane"], LANE_COLORS["Other"])
        title = it["title"] if len(it["title"]) <= 56 else it["title"][:55] + "…"
        label = f'{it["repo"]}#{it["number"]}'
        tail = f'  {it["ago"]}'
        text_w = (len(label) + 2 + len(title) + len(tail)) * 6.6
        items.append(
            f'<g transform="translate({x:.0f},0)"><circle cx="0" cy="28" r="4" fill="{color}"/>'
            f'<text class="mono" x="12" y="32" font-size="11"><tspan style="fill:{color};font-weight:700">{escape(label)}</tspan>'
            f'<tspan class="muted">  {escape(title)}{escape(tail)}</tspan></text></g>'
        )
        x += text_w + 48
    total = x
    dur = max(total / 38, 20)
    body = f"""
    <clipPath id="belt"><rect x="150" y="0" width="{w - 150 - 16}" height="{h}"/></clipPath>
    <linearGradient id="fadeL"><stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg1']}" stop-opacity="0"/></linearGradient>
    <linearGradient id="fadeR"><stop offset="0" stop-color="{t['bg1']}" stop-opacity="0"/><stop offset="1" stop-color="{t['bg1']}"/></linearGradient>
    <circle class="ping" cx="30" cy="28" r="5" fill="#3fb950"/><circle cx="30" cy="28" r="4" fill="#3fb950"/>
    <text class="mono" x="44" y="32" font-size="12" font-weight="800">SHIPPED</text>
    <text class="mono muted" x="108" y="32" font-size="10">live</text>
    <line x1="146" x2="146" y1="14" y2="42" stroke="{t['border']}"/>
    <g clip-path="url(#belt)">
      <g class="belt" style="--w:-{total:.0f}px;animation-duration:{dur:.0f}s" transform="translate(150,0)">
        <g transform="translate(16,0)">{''.join(items)}</g>
        <g transform="translate({total + 16:.0f},0)">{''.join(items)}</g>
      </g>
    </g>
    <rect x="150" y="0" width="40" height="{h}" fill="url(#fadeL)"/>
    <rect x="{w - 56}" y="0" width="40" height="{h}" fill="url(#fadeR)"/>"""
    css = """
    .belt { animation: tick 60s linear infinite; }
    @keyframes tick { to { transform: translate(calc(150px + var(--w)), 0); } }
    .ping { transform-box: fill-box; transform-origin: center; animation: ping 2s ease-out infinite; }
    @keyframes ping { from { transform: scale(1); opacity: .8; } to { transform: scale(3.2); opacity: 0; } }"""
    return shell(w, h, t, body, "Recently merged pull requests",
                 "Scrolling ticker of my most recently merged public pull requests.", css)


# ------------------------------------------------------------------------- impact
def impact(t, s):
    w, h = 900, 310
    years = s["merged_by_year"]
    ys = sorted(years)
    peak = max(years.values())
    top = int(math.ceil(peak / 100.0) * 100)
    cx0, cx1, base, ch = 70, 860, 252, 170
    slot = (cx1 - cx0) / len(ys)
    bw = slot * 0.62
    grid = []
    for v in range(0, top + 1, 100):
        y = base - ch * v / top
        grid.append(f'<line x1="{cx0 - 10}" x2="{cx1}" y1="{y:.1f}" y2="{y:.1f}" stroke="{t["grid"]}"/>')
        grid.append(f'<text class="mono muted" x="{cx0 - 16}" y="{y + 4:.1f}" font-size="10" text-anchor="end">{v}</text>')
    bars, pts = [], []
    for i, yr in enumerate(ys):
        v = years[yr]
        bh = max(2, ch * v / top)
        x = cx0 + i * slot + (slot - bw) / 2
        last = yr == ys[-1]
        fill = "url(#hot)" if last else t["muted"]
        op = "1" if last else ".55"
        delay = 0.15 + i * 0.12
        pts.append((x + bw / 2, base - bh))
        bars.append(
            f'<rect class="bar{" now" if last else ""}" x="{x:.1f}" y="{base - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="5" '
            f'fill="{fill}" style="opacity:{op};animation-delay:{delay:.2f}s"/>'
            f'<text class="mono pop" x="{x + bw / 2:.1f}" y="{base - bh - 8:.1f}" font-size="12" font-weight="700" text-anchor="middle" '
            f'style="animation-delay:{delay + .5:.2f}s;{"fill:" + t["accent2"] if last else ""}">{v}</text>'
            f'<text class="mono muted" x="{x + bw / 2:.1f}" y="{base + 20}" font-size="11" text-anchor="middle">{yr}{"*" if last else ""}</text>'
        )
    path = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    ex, ey = pts[-1]
    trend = (
        f'<path class="trend" d="{path}" pathLength="1" fill="none" stroke="{t["accent2"]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
        + "".join(f'<circle class="vtx" cx="{px:.1f}" cy="{py:.1f}" r="3" fill="{t["accent2"]}" style="animation-delay:{1.2 + i * 0.12:.2f}s"/>' for i, (px, py) in enumerate(pts))
        + f'<circle class="endping" cx="{ex:.1f}" cy="{ey:.1f}" r="5" fill="{t["accent2"]}"/>'
    )
    body = f"""
    <text x="32" y="38" font-size="18" font-weight="700">Merged PRs per year</text>
    <text class="muted" x="32" y="58" font-size="12">Public repos outside my personal namespace · {s['merged_all']:,} total · *{s['year']} is year-to-date</text>
    {''.join(grid)}
    {''.join(bars)}
    {trend}"""
    css = """
    .trend { stroke-dasharray: 1; animation: trace 1.8s ease-in-out 1s backwards; }
    @keyframes trace { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
    .vtx { animation: fade .4s ease-out backwards; }
    .endping { transform-box: fill-box; transform-origin: center; animation: ping 2s ease-out 2.6s infinite; }
    @keyframes ping { from { transform: scale(1); opacity: .9; } to { transform: scale(3.4); opacity: 0; } }
    .bar { transform-box: fill-box; transform-origin: bottom; animation: rise 1s cubic-bezier(.2,.8,.2,1) both; }
    @keyframes rise { from { transform: scaleY(0); } to { transform: scaleY(1); } }
    .now { animation: rise 1s cubic-bezier(.2,.8,.2,1) both, glow 3s ease-in-out 2s infinite; }
    @keyframes glow { 0%,100% { filter: none; } 50% { filter: drop-shadow(0 0 8px rgba(238,0,0,.65)); } }
    .pop { opacity: 0; animation: fade .5s ease-out both; }
    @media (prefers-reduced-motion: reduce) { .pop { opacity: 1; } }
    @keyframes fade { from { opacity: 0; } to { opacity: 1; } }"""
    return shell(w, h, t, body, "Merged pull requests per year",
                 f"Bar chart of merged PRs per year, rising to {years[ys[-1]]} so far in {ys[-1]}.", css)


# -------------------------------------------------------------------------- orbit
def orbit(t, s):
    """Hub -> workstream repos, and for the Other lane hub -> org -> repos (orbiting moons)."""
    w, h = 900, 500
    cx, cy = 600, 250
    lane_repos, orgs = s["lane_repos"], s["other_orgs"]
    # planets: ("repo"|"org", label, count, color, moons)
    short = Counter(r.split("/")[1] for r, _, _ in lane_repos)  # same short name in two orgs -> keep the org prefix
    planets_in = [("repo", r if short[r.split("/")[1]] > 1 else r.split("/")[1], n, LANE_COLORS[lane], []) for r, n, lane in lane_repos]
    planets_in += [("org", org + "/", total, LANE_COLORS["Other"], moons) for org, total, moons in orgs]
    peak = max(p[2] for p in planets_in)
    rings = [(92, planets_in[:4], 90, 1), (160, planets_in[4:], 140, -1)]
    halo = f'paint-order:stroke;stroke:{t["bg1"]};stroke-width:3px'
    ring_svg, planets = [], []
    for radius, members, period, direction in rings:
        ring_svg.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{t["border"]}" stroke-dasharray="3 6"/>')
        anim, counter = ("spin", "spinr") if direction > 0 else ("spinr", "spin")
        for i, (kind, label, n, color, moons) in enumerate(members):
            angle = 360 * i / len(members) + (20 if direction < 0 else 0)
            pr = 8 + 15 * math.sqrt(n / peak)
            if len(label) > 22:
                label = label[:21] + "…"
            ring_style = f'stroke="{color}" stroke-width="1.5" stroke-dasharray="3 3" fill="none"' if kind == "org" else ""
            moon_svg = ""
            if moons:
                mrad = pr + 27
                mpeak = max(m for _, m in moons)
                moon_svg = f'<circle r="{mrad:.1f}" fill="none" stroke="{t["border"]}" stroke-dasharray="2 4"/>'
                for j, (mname, m) in enumerate(moons):
                    mangle = 360 * j / len(moons) + 40
                    mr = 3.5 + 4 * math.sqrt(m / mpeak)
                    mname = mname if len(mname) <= 16 else mname[:15] + "…"
                    moon_svg += (
                        f'<g transform="rotate({mangle:.0f})"><g class="o" style="animation-name:spin;animation-duration:22s">'
                        f'<g transform="translate({mrad:.1f},0)"><circle r="{mr:.1f}" fill="{color}" opacity=".85"/>'
                        # undo moon spin, moon offset, ring spin and ring offset so the text stays upright
                        f'<g class="o" style="animation-name:spinr;animation-duration:22s"><g transform="rotate({-mangle:.0f})">'
                        f'<g class="o" style="animation-name:{counter};animation-duration:{period}s"><g transform="rotate({-angle:.0f})">'
                        f'<text class="mono" y="{mr + 10:.1f}" font-size="9" text-anchor="middle" style="{halo}">{escape(mname)}</text>'
                        f'<text class="mono muted" y="{mr + 20:.1f}" font-size="9" text-anchor="middle" style="{halo}">{m}</text>'
                        f'</g></g></g></g></g></g></g>'
                    )
            planets.append(
                f'<g transform="translate({cx},{cy}) rotate({angle:.0f})"><g class="o" style="animation-name:{anim};animation-duration:{period}s">'
                f'<line class="flow" x1="32" y1="0" x2="{radius - pr - 6:.1f}" y2="0" stroke="{color}" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>'
                f'<g transform="translate({radius},0)">'
                f'{moon_svg}'
                f'<circle r="{pr + 5:.1f}" fill="{color}" opacity=".18"/>'
                f'<circle r="{pr:.1f}" fill="{color}"/>'
                + (f'<circle r="{pr + 5:.1f}" {ring_style}/>' if kind == "org" else "")
                + f'<g class="o" style="animation-name:{counter};animation-duration:{period}s">'
                # the wrapping rotate() above is static, so cancel it with a fixed counter-rotation too
                f'<g transform="rotate({-angle:.0f})">'
                f'<text class="mono" y="{-(pr + 9):.1f}" font-size="{11 if kind == "org" else 10}" font-weight="{700 if kind == "org" else 400}" text-anchor="middle" style="{halo}">{escape(label)}</text>'
                f'<text class="mono muted" y="{-(pr + 20):.1f}" font-size="10" text-anchor="middle" style="{halo}">{n}</text>'
                f'</g></g></g></g></g>'
            )
    legend = []
    ly = 128
    for lane, color in LANE_COLORS.items():
        n = s["lane_totals"].get(lane, 0)
        if n < 3:
            continue
        legend.append(
            f'<circle cx="40" cy="{ly - 4}" r="6" fill="{color}"/>'
            f'<text x="56" y="{ly}" font-size="14">{escape(lane)}</text>'
            f'<text class="mono muted" x="290" y="{ly}" font-size="13" text-anchor="end">{n:,}</text>'
        )
        ly += 28
    body = f"""
    <text x="32" y="38" font-size="18" font-weight="700">Where the work lands</text>
    <text class="muted" x="32" y="58" font-size="12">Merged PRs · size = volume · colour = workstream · Other groups by org, repos orbit their org</text>
    {''.join(legend)}
    <circle class="pulse" cx="{cx}" cy="{cy}" r="44" fill="url(#aura)"/>
    {''.join(ring_svg)}
    <circle cx="{cx}" cy="{cy}" r="30" fill="{t['chip']}" stroke="{t['accent']}" stroke-width="2"/>
    <text class="mono" x="{cx}" y="{cy + 6}" font-size="17" font-weight="800" text-anchor="middle">TK</text>
    {''.join(planets)}"""
    css = """
    .o { transform-origin: 0 0; animation-timing-function: linear; animation-iteration-count: infinite; }
    @keyframes spin { to { transform: rotate(360deg); } }
    @keyframes spinr { to { transform: rotate(-360deg); } }
    .flow { opacity: .55; animation: flow 1.1s linear infinite; }
    @keyframes flow { to { stroke-dashoffset: -9; } }
    .pulse { transform-box: fill-box; transform-origin: center; animation: breathe 4s ease-in-out infinite; }
    @keyframes breathe { 0%,100% { transform: scale(.85); opacity: .6; } 50% { transform: scale(1.35); opacity: 1; } }"""
    return shell(w, h, t, body, "Merged pull requests by repository",
                 "Orbit diagram: workstream repositories and orgs sized by merged PR count; repos in the Other lane orbit their org.", css)


# ----------------------------------------------------------------------- languages
def lang_color(name):
    if name in LANG_COLORS:
        return LANG_COLORS[name]
    hue = sum(ord(c) * (i + 1) for i, c in enumerate(name)) % 360
    return f"hsl({hue},55%,55%)"


def languages(t, s):
    w, h = 900, 330
    langs = s["languages"]
    if not langs:  # no repo has a known language yet (e.g. first run before the cache is seeded)
        return None
    top_name, _, top_pct = next((row for row in langs if row[0] != "Other"), langs[0])
    scale = max(pct for _, _, pct in langs)
    cx, cy, r, sw = 215, 185, 98, 30
    gap = 0.7  # visual gap between ring segments, in pathLength units
    segs, start = [], 0.0
    for i, (name, n, pct) in enumerate(langs):
        length = max(pct - gap, 0.3)
        segs.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" pathLength="100" fill="none" stroke="{lang_color(name)}" '
            f'stroke-width="{sw}" transform="rotate(-90 {cx} {cy})" '
            f'class="seg{" lead" if i == 0 else ""}" style="--len:{length:.2f};--rest:{100 - length:.2f};stroke-dashoffset:-{start:.2f};animation-delay:{0.2 + i * 0.18:.2f}s"/>'
        )
        start += pct
    legend, ly, bar_x, bar_w = [], 96, 440, 300
    for i, (name, n, pct) in enumerate(langs):
        delay = 0.4 + i * 0.18
        legend.append(
            f'<circle cx="{bar_x - 16}" cy="{ly - 4}" r="5" fill="{lang_color(name)}"/>'
            f'<text x="{bar_x}" y="{ly}" font-size="13" font-weight="600">{escape(name)}</text>'
            f'<text class="mono muted" x="{bar_x + bar_w + 70}" y="{ly}" font-size="12" text-anchor="end">{pct:.1f}%</text>'
            f'<rect x="{bar_x}" y="{ly + 7}" width="{bar_w + 70}" height="6" rx="3" fill="{t["grid"]}"/>'
            f'<rect class="lbar" x="{bar_x}" y="{ly + 7}" width="{max(pct / scale, 0.02) * (bar_w + 70):.1f}" height="6" rx="3" '
            f'fill="{lang_color(name)}" style="animation-delay:{delay:.2f}s"/>'
        )
        ly += 28
    body = f"""
    <text x="32" y="38" font-size="18" font-weight="700">Languages I ship in</text>
    <text class="muted" x="32" y="58" font-size="12">Merged PRs weighted by each repo's primary language · {s['lang_prs']:,} PRs across {s['lang_repos']} repos</text>
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{t['grid']}" stroke-width="{sw}"/>
    <g class="ring" style="transform-origin:{cx}px {cy}px">{''.join(segs)}</g>
    {odometer(cx - len(f"{top_pct:.0f}%") * 26 * 0.31, cy - 2, f"{top_pct:.0f}%", 26, t["text"], 0.6, "odl")}
    <text class="muted" x="{cx}" y="{cy + 20}" font-size="13" text-anchor="middle">{escape(top_name)}</text>
    {''.join(legend)}"""
    css = """
    .seg { stroke-dasharray: var(--len) var(--rest); animation: draw .9s cubic-bezier(.3,.7,.2,1) both; }
    @keyframes draw { from { stroke-dasharray: 0 100; } to { stroke-dasharray: var(--len) var(--rest); } }
    .ring { animation: orbit 90s linear infinite; }
    @keyframes orbit { to { transform: rotate(360deg); } }
    .lead { animation: draw .9s cubic-bezier(.3,.7,.2,1) both, glow 3s ease-in-out 2s infinite; }
    @keyframes glow { 0%,100% { filter: none; } 50% { filter: drop-shadow(0 0 6px rgba(0,173,216,.9)); } }
    .lbar { transform-box: fill-box; transform-origin: left; animation: wipe 1s cubic-bezier(.2,.8,.2,1) both; }
    @keyframes wipe { from { transform: scaleX(0); } to { transform: scaleX(1); } }"""
    return shell(w, h, t, body, "Languages by merged pull requests",
                 f"Donut and bar chart of merged PRs by repository language; {top_name} leads at {top_pct:.0f}%.", css)


# ------------------------------------------------------------------------ pipeline
def pipeline(t, s):
    w, h = 900, 200
    counts = s["pr_status"]
    total = sum(counts.values()) or 1
    bx, bw, by, bh = 32, 836, 78, 30
    segs, x = [], bx
    for key, _, color in STATUS_COLORS:
        n = counts.get(key, 0)
        if not n:
            continue
        sw = bw * n / total
        segs.append(f'<rect class="seg-{key}" x="{x:.1f}" y="{by}" width="{sw:.1f}" height="{bh}" fill="{color}"/>')
        x += sw
    legend, lx, ly = [], 32, 140
    for i, (key, label, color) in enumerate(STATUS_COLORS):
        n = counts.get(key, 0)
        col, row = i % 4, i // 4
        px, py = 32 + col * 210, 138 + row * 26
        legend.append(
            f'<circle cx="{px + 5}" cy="{py - 4}" r="5" fill="{color}"/>'
            f'<text class="mono" x="{px + 18}" y="{py}" font-size="13" font-weight="700">{n}</text>'
            f'<text class="muted" x="{px + 18 + 8 * len(str(n)) + 8}" y="{py}" font-size="12">{escape(label)}</text>'
        )
    rq = s["review_queue"]
    body = f"""
    <text x="32" y="38" font-size="18" font-weight="700">Open PR pipeline</text>
    <text class="muted" x="32" y="58" font-size="12">{total} open PRs in public org repos · {rq['needs']} awaiting review · {rq['approved']} approved and waiting to land</text>
    <clipPath id="reveal"><rect class="wipe" x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="15"/></clipPath>
    <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="15" fill="{t['grid']}"/>
    <g clip-path="url(#reveal)">{''.join(segs)}<rect class="sheen" x="-160" y="{by}" width="160" height="{bh}" fill="url(#sheen)"/></g>
    <linearGradient id="sheen"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    {''.join(legend)}"""
    css = """
    .wipe { transform-box: fill-box; transform-origin: left; animation: wipe 1.4s cubic-bezier(.2,.8,.2,1) both; }
    @keyframes wipe { from { transform: scaleX(0); } to { transform: scaleX(1); } }
    .seg-ready { animation: beat 2.6s ease-in-out 1.6s infinite; }
    .seg-failing-ci { animation: alarm 1.2s ease-in-out 1.6s infinite; }
    .seg-ci-pending { animation: beat .9s ease-in-out 1.6s infinite; }
    @keyframes beat { 0%,100% { opacity: 1; } 50% { opacity: .55; } }
    @keyframes alarm { 0%,100% { opacity: 1; } 50% { opacity: .35; } }
    .sheen { animation: sweep 3.6s ease-in-out 1.8s infinite; }
    @keyframes sweep { from { transform: translateX(0); } to { transform: translateX(1100px); } }"""
    return shell(w, h, t, body, "Open pull request pipeline",
                 "Stacked bar of my open PRs by status: ready, waiting to merge, CI, drafts and stale.", css)


# --------------------------------------------------------------------------- main
def build_stats():
    archive = load("workstream-archive.json")
    prs = load("open-prs.json")
    activity = load("activity.json")

    merged = [i for i in archive["items"] if i["type"] == "pr" and i["state"] == "merged" and i["org"] != OWNER]
    year = int(archive["generatedAt"][:4])
    by_year = Counter(i["closedAt"][:4] for i in merged)
    by_year.setdefault(str(year), 0)

    lane_votes = {}
    for i in archive["items"]:
        lane_votes.setdefault(i["repo"], Counter())[i["workstream"]] += 1
    by_repo = Counter(i["repo"] for i in merged)
    lane_repos = [(r, n, lane_for(r, lane_votes)) for r, n in by_repo.most_common() if lane_for(r, lane_votes) != "Other"][:5]
    by_org = {}
    for r, n in by_repo.items():
        if lane_for(r, lane_votes) == "Other":
            org, name = r.split("/")
            by_org.setdefault(org, []).append((name, n))
    other_orgs = sorted(
        ((org, sum(n for _, n in rs), ([m for m in sorted(rs, key=lambda x: -x[1]) if m[1] >= 3][:3] or sorted(rs, key=lambda x: -x[1])[:1]))
         for org, rs in by_org.items()),
        key=lambda x: -x[1],
    )[:4]
    lane_totals = Counter()
    for r, n in by_repo.items():
        lane_totals[lane_for(r, lane_votes)] += n

    repo_langs = load("repo-languages.json")
    by_lang = Counter()
    for r, n in by_repo.items():
        if repo_langs.get(r):
            by_lang[repo_langs[r]] += n
    lang_total = sum(by_lang.values())
    ranked = by_lang.most_common()
    shown = ranked[:7]
    rest = sum(n for _, n in ranked[7:])
    if rest:
        shown.append(("Other", rest))
    lang_rows = [(name, n, 100.0 * n / lang_total) for name, n in shown] if lang_total else []

    now = datetime.fromisoformat(activity["generatedAt"].replace("Z", "+00:00"))
    feeds = [activity[k] for k in ("prsMerged", "prsOpened", "prsReviewed", "issuesCommented", "issuesClosed")]
    day_counts, truncated_from = Counter(), []
    for feed in feeds:
        dates = [x["date"][:10] for x in feed if x.get("date")]
        day_counts.update(dates)
        if len(feed) >= 100 and dates:  # the feed hit its page cap, so older days are incomplete
            truncated_from.append(min(dates))
    end = datetime.fromisoformat(activity["period"]["end"])
    dates = [(end - timedelta(days=90 - i)).strftime("%Y-%m-%d") for i in range(91)]
    heat = dict(
        dates=dates,
        days=day_counts,
        # first day every feed fully covers; earlier cells render as unknown, not zero
        **{"from": max(truncated_from + [activity["period"]["start"]])},
        asof=activity["generatedAt"][:10],
    )
    recent = sorted((x for x in activity["prsMerged"] if x["org"] != OWNER), key=lambda x: x["date"], reverse=True)[:10]
    recent_merged = [
        dict(repo=x["repo"], number=x["number"], title=x["title"], lane=x.get("workstream", "Other"), ago=ago(x["date"], now))
        for x in recent
    ]

    open_prs = [p for p in prs["prs"] if p["org"] != OWNER]
    rq = prs.get("reviewQueue", {})
    return dict(
        year=year,
        merged_all=len(merged),
        merged_ytd=by_year[str(year)],
        merged_by_year={int(y): n for y, n in by_year.items()},
        lane_repos=lane_repos,
        other_orgs=other_orgs,
        heat=heat,
        recent_merged=recent_merged,
        languages=lang_rows,
        lang_prs=lang_total,
        lang_repos=sum(1 for r in by_repo if repo_langs.get(r)),
        lane_totals=lane_totals,
        open_prs=len(open_prs),
        pr_status=Counter(p["status"] for p in open_prs),
        review_queue=dict(needs=len(rq.get("needsReview", [])), approved=len(rq.get("approvedWaitingToLand", []))),
        reviewed=activity["metrics"]["prsReviewed"],
        period_days=(datetime.fromisoformat(activity["period"]["end"]) - datetime.fromisoformat(activity["period"]["start"])).days,
    )


# ------------------------------------------------------------------------- bojangles
# Seconds, position above the ground, body angle, pose. All action tracks share this clock.
BOJANGLES_STORY = (
    (0, 126, 0, 0, "walk"), (4.5, 225, 0, 0, "walk"),
    (4.8, 225, 0, 0, "nibble"), (9, 225, 0, 0, "nibble"),
    (9.4, 225, 0, 0, "stand"), (13.5, 415, 0, 0, "walk"),
    (14.2, 415, 10, 0, "crouch"), (14.6, 425, -22, -12, "leap"),
    (15.2, 450, -58, -22, "reach"), (15.7, 470, -70, -12, "reach"),
    (16.2, 486, -45, 0, "leap"), (16.7, 500, 0, 0, "stand"),
    (17, 500, 10, 0, "crouch"), (17.4, 500, 0, 0, "stand"),
    (21, 650, 0, 0, "walk"), (21.7, 650, 10, 0, "crouch"),
    (22.2, 677, -35, -35, "leap"), (22.7, 697, -57, -60, "cling"),
    (23.7, 697, -57, -60, "cling"), (24.2, 697, -49, -60, "cling"),
    (24.8, 693, -32, -60, "cling"), (25.4, 681, -5, -45, "fall"),
    (25.9, 662, 0, 0, "stand"), (26.2, 662, 10, 0, "crouch"),
    (26.7, 662, 0, 0, "stand"), (27.4, 662, 0, 0, "stand"),
    (36.7, 126, 0, 0, "walk"), (37.4, 126, 0, 0, "stand"),
    (40, 126, 0, 0, "stand"),
)
BOJANGLES_WALKS = ((0, 4.5), (9.4, 13.5), (17.4, 21), (27.4, 36.7))


def bojangles(t, _s):
    """Photo-inspired tabby, articulated limbs and a CSS-only backyard story."""
    w, h, ground, duration = 900, 340, 290, BOJANGLES_STORY[-1][0]
    stripe, cream = "#292824", "#c9c1aa"
    # Upper/lower foreleg, upper/lower hind leg, head. Angles pivot at joints, not bounding boxes.
    poses = dict(stand=(0, 0, 0, 0, 0), walk=(0, 0, 0, 0, 0),
                 nibble=(0, 0, 0, 0, 13), crouch=(-42, 75, -52, 59, -5),
                 leap=(-48, -12, 40, -65, -9), reach=(-82, -20, 52, -72, -12),
                 cling=(0, 0, 36, -50, 9), fall=(-26, 30, -30, 45, 12))

    def track(name, frames, prop="transform", timing="linear"):
        """Map seconds to CSS percentages on the shared story clock."""
        rules = "".join(f"{sec / duration * 100:.4f}% {{{prop}:{value};}}" for sec, value in frames)
        return f".{name} {{animation:{name} {duration}s {timing} infinite;}} @keyframes {name} {{{rules}}}"

    css = track("bj-travel", [(s, f"translate({x}px,{y}px)") for s, x, y, _, _ in BOJANGLES_STORY])
    css += track("bj-pitch", [(s, f"rotate({angle}deg)") for s, _, _, angle, _ in BOJANGLES_STORY])
    css += track("bj-facing", [(0, "scaleX(1)"), (27, "scaleX(-1)"),
                                (37.1, "scaleX(1)"), (40, "scaleX(1)")], timing="steps(1, end)")
    css += track("bj-head", [(s, f"rotate({poses[pose][4]}deg)") for s, _, _, _, pose in BOJANGLES_STORY])
    # Quarter-stride samples keep gait on the same clock as the pauses and jumps.
    for name, index, phase in (("fore-near", 0, 0), ("fore-far", 0, math.pi),
                               ("hind-near", 2, math.pi), ("hind-far", 2, 0)):
        upper = {s: poses[pose][index] for s, _, _, _, pose in BOJANGLES_STORY}
        lower = {s: poses[pose][index + 1] for s, _, _, _, pose in BOJANGLES_STORY}
        for start, end in BOJANGLES_WALKS:
            steps = max(4, round((end - start) / .9) * 4)
            for step in range(steps + 1):
                sec = start + (end - start) * step / steps
                swing = math.sin(step * math.pi / 2 + phase)
                # Ease into and out of walking rather than snapping a planted paw.
                envelope = min(step, steps - step, 1)
                upper[sec] = 23 * swing * envelope
                lower[sec] = max(0, -swing) * 28 * envelope
        css += track(f"bj-{name}", [(s, f"rotate({a:.1f}deg)") for s, a in sorted(upper.items())])
        css += track(f"bj-{name}-lower", [(s, f"rotate({a:.1f}deg)") for s, a in sorted(lower.items())])

    torso = "M-51,-60 C-54,-78 -39,-88 -22,-87 C-5,-85 11,-89 29,-87 C44,-87 48,-74 44,-60 L39,-42 C27,-34 15,-40 1,-39 C-16,-34 -43,-35 -49,-47 Z"
    # Artwork is vector geometry only; the daily renderer never needs the private photo or Pillow.
    face_path = Path(__file__).resolve().parents[1] / "artwork" / "bojangles-face.json"
    try:
        face = json.loads(face_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot load Bojangles vector artwork from {face_path}: {exc}") from exc
    defs = f"""<defs>
      <linearGradient id="bj-coat" x1="0" y1="0" x2=".2" y2="1">
        <stop stop-color="#55544c"/><stop offset=".4" stop-color="#938b76"/>
        <stop offset=".76" stop-color="#a29980"/><stop offset="1" stop-color="#6a6659"/>
      </linearGradient>
      <linearGradient id="bj-limb" x1="0" y1="0" x2="1" y2="0">
        <stop stop-color="#57574e"/><stop offset=".48" stop-color="#a19a83"/><stop offset="1" stop-color="#777565"/>
      </linearGradient>
      <clipPath id="bj-torso-clip"><path d="{torso}"/></clipPath>
    </defs>"""

    def fur_patch(clip, count, x, y, width, height):
        # Deterministic short guard hairs; no raster photo, random seed, or SVG noise filter.
        hairs = []
        for i in range(count):
            hx, hy = x + (i * 37 % 101) / 101 * width, y + (i * 61 % 103) / 103 * height
            hairs.append(f'<path d="M{hx:.1f},{hy:.1f} l{1 + i % 3:.1f},{2 + i % 2}"/>')
        return f'<g clip-path="url(#{clip})" fill="none" stroke="{cream}" stroke-width=".55" opacity=".32">{"".join(hairs)}</g>'

    def leg(name, x, y, hind=False, far=False):
        thigh = ("M-9,-6 C-22,1 -18,18 -6,29 Q0,33 6,25 L9,1 Z" if hind else
                 "M-8,-5 Q-13,8 -6,29 Q0,34 6,28 L8,-3 Z")
        return f"""<g transform="translate({x},{y})"><g class="bj-{name}">
          <path d="{thigh}" fill="url(#bj-limb)"/>
          <path d="M-9,4 Q0,9 8,5 M-9,13 Q0,18 7,13 M-6,22 l11,1" fill="none" stroke="{stripe}" stroke-width="3.7"/>
          <g transform="translate(0,27)"><g class="bj-{name}-lower">
            <path d="M-5,-3 Q-8,10 -5,24 C-10,29 -7,33 0,33 L9,33 Q16,30 9,26 L5,23 L5,-2 Z" fill="url(#bj-limb)" stroke="#555348" stroke-width=".65"/>
            <path d="M-5,5 l10,1 M-5,12 l10,1 M-5,19 l10,1" stroke="{stripe}" stroke-width="3.2"/>
            <path d="M-2,28 v4 M3,28 v4 M8,28 l-1,4" stroke="#4e4a40" stroke-width=".8"/>
            <path d="M-3,24 l1,-3 M1,24 l1,-3 M5,24 v-3" stroke="{cream}" stroke-width=".7"/>
          </g></g>
        {'<path d="M-8,-4 L6,0 L4,27 L-5,27 Z" fill="#151815" opacity=".18"/>' if far else ''}</g></g>"""

    stripes = "".join(f'<path d="{d}"/>' for d in (
        "M-42,-86 Q-27,-80 -36,-64 L-40,-55 L-40,-65 Q-31,-78 -46,-82 Z",
        "M-30,-88 Q-16,-79 -24,-65 L-24,-54 L-29,-46 L-27,-61 Q-20,-76 -35,-83 Z",
        "M-17,-89 Q-3,-80 -12,-68 L-9,-58 L-13,-47 L-14,-60 L-18,-66 Q-9,-78 -23,-85 Z",
        "M-3,-89 Q9,-81 3,-70 L6,-64 L4,-55 L0,-60 L-1,-69 Q4,-79 -8,-86 Z",
        "M10,-90 Q25,-79 17,-66 L20,-55 L16,-45 L14,-58 L11,-68 Q17,-78 5,-85 Z",
        "M25,-88 Q37,-78 30,-69 L34,-59 L31,-49 L27,-56 L25,-69 Q30,-79 20,-85 Z",
        "M-20,-56 l4,5 l-1,6 l-4,-3 Z M-4,-49 l5,-3 l3,5 l-5,3 Z M8,-57 l4,3 l-1,5 l-4,-2 Z",
    ))
    face_layers = {}
    for layer in face["layers"]:
        # A tiny same-color stroke closes subpixel seams between simplified contours.
        face_layers[layer["name"]] = '<g fill-rule="evenodd" stroke-width=".35" stroke-linejoin="round">' + "".join(
            f'<path fill="{p["fill"]}" stroke="{p["fill"]}" d="{p["d"]}"/>' for p in layer["paths"]
        ) + '</g>'
    eyes = "".join(
        f'''<g id="bj-eye-{side}">
          <path d="{face['regions'][f'eye-{side}']}" fill="#756559"/>
          <path d="{lid}" fill="none" stroke="#3d342e" stroke-width="1"/>
          <g class="bj-blink">{face_layers[f'eye-{side}']}
            <ellipse cx="{x}" cy="{y}" rx=".65" ry="1" fill="#deded0" opacity=".7"/>
          </g>
        </g>''' for side, lid, x, y in (
            ("near", "M59,106 Q67,114 78,112", 68, 108),
            ("far", "M109,112 Q122,116 133,107", 121, 108),
        )
    )
    whiskers = " ".join(
        f'M{x},{y} Q{cx},{cy} {ex},{ey}'
        for x, y, cx, cy, ex, ey in (
            (77,149,51,132,17,137), (76,153,47,147,12,151),
            (77,157,44,160,17,169), (82,159,59,178,33,185),
            (104,151,139,128,174,137), (106,153,144,144,185,150),
            (107,155,151,158,185,175), (106,159,142,175,169,188),
        )
    )
    # Mirror the portrait's three-quarter view to match the right-facing body.
    cat_head = f"""<g class="bj-head"><g transform="translate(104,-142) scale(-.42,.42)">
      <g class="bj-ear">
        <path d="{face['regions']['ear']}" fill="#766b60"/>{face_layers['ear']}
      </g>
      <path d="{face['base']}" fill="#8b7961"/>{face_layers['head']}
      {eyes}
      <path d="{face['regions']['jaw']}" fill="#41332d"/>
      <g class="bj-jaw">{face_layers['jaw']}</g>
      <g fill="none" stroke="#ded9c8" stroke-width=".55" stroke-linecap="round" opacity=".8">
        <path d="{whiskers}"/>
        <path d="M64,101 Q51,77 34,71 M70,99 Q66,74 51,65 M119,99 Q140,70 158,70 M125,101 Q148,83 167,87"/>
      </g>
    </g></g>"""
    cat = f"""<g class="bj-pitch">
      <g transform="translate(-47,-65)"><g class="bj-tail">
        <path d="M0,0 C-29,-4 -52,-15 -50,-42 Q-49,-54 -44,-58" fill="none" stroke="#787767" stroke-width="10" stroke-linecap="round"/>
        <path d="M0,0 C-29,-4 -52,-15 -50,-42 Q-49,-54 -44,-58" fill="none" stroke="{stripe}" stroke-width="10.2" stroke-dasharray="5 7"/>
        <path d="M-5,-3 Q-36,-11 -43,-28" fill="none" stroke="{cream}" stroke-width="1.1" opacity=".5"/>
      </g></g>
      {leg('hind-far', -35, -60, True, True)}{leg('fore-far', 26, -60, far=True)}
      <path d="{torso}" fill="url(#bj-coat)"/>
      <g clip-path="url(#bj-torso-clip)">
        <path d="M-52,-81 Q-3,-98 43,-84" fill="none" stroke="{stripe}" stroke-width="11"/>
        <path d="M-37,-40 Q6,-28 35,-43" fill="none" stroke="{cream}" stroke-width="9" opacity=".65"/>
        <g fill="{stripe}" opacity=".93">{stripes}</g>
        <path d="M-44,-63 q17,-8 22,8 q0,14 -17,11 M-38,-59 q10,-3 11,5" fill="none" stroke="{stripe}" stroke-width="2.5"/>
      </g>
      {fur_patch('bj-torso-clip', 155, -54, -90, 104, 59)}
      {leg('hind-near', -32, -60, True)}
      <path d="M23,-79 Q30,-104 45,-102 L56,-77 Q50,-53 39,-45 L30,-58 Z" fill="url(#bj-coat)"/>
      <path d="M29,-80 l17,8 M26,-71 l19,8 M31,-59 l10,4" stroke="{stripe}" stroke-width="4.5"/>
      {leg('fore-near', 34, -60)}{cat_head}
    </g>"""

    flowers = []
    for x, top in ((286, 226), (299, 208), (312, 230)):
        petals = "".join(f'<ellipse cx="{x + side * 3}" cy="{top + i * 5}" rx="3.3" ry="2.3" fill="{color}"/>'
                         for i, color in enumerate(("#d9c1e6", "#b49dcd", "#987daf")) for side in (-1, 1))
        flowers.append(f'<path d="M{x},284 Q{x - 7},251 {x},{top}" stroke="#688969" stroke-width="2" fill="none"/>'
                       f'<path d="M{x - 2},262 q-18,-18 -14,-4 q6,11 14,4 M{x - 2},249 q16,-15 14,-3 q-6,10 -14,3" fill="#729477"/>{petals}')
    grass = "".join(f'<path d="M{x},291 l-3,-9 m3,9 l4,-13 m-3,11 l6,-5"/>' for x in (42, 168, 350, 580, 818, 851))
    captions = ((0, "Backyard patrol"), (4.8, "A little catnip nibble"), (9.4, "Something fishy…"),
                (14.2, "Almost got it!"), (17.4, "One more adventure"), (21.7, "That ledge looked wider"),
                (24.2, "No grip. Slow slide. Soft landing."), (26.7, "Meant to do that."),
                (37.4, "Backyard patrol"), (40, "Backyard patrol"))
    labels = []
    for i, (start, label) in enumerate(captions[:-1]):
        end = captions[i + 1][0]
        labels.append(f'<text class="bj-caption bj-caption-{i} muted" x="450" y="322" text-anchor="middle" font-size="12">{escape(label)}</text>')
        frames = [(0, "0"), (start, "1"), (end, "0"), (duration, "0")]
        css += track(f"bj-caption-{i}", sorted(dict(frames).items()), "opacity", "steps(1, end)")
    body = f"""{defs}
      <text x="28" y="33" font-size="19" font-weight="650">Bojangles</text>
      <text class="muted" x="28" y="52" font-size="11">chief nap officer · occasional adventurer</text>
      <path d="M28,292 H872" stroke="{t['border']}" fill="none"/>
      <g fill="none" stroke="#68816c" stroke-width="1.1" opacity=".65">{grass}</g>
      <g class="bj-flowers">{''.join(flowers)}</g>
      <path d="M282,284 H316 L312,292 H286 Z" fill="#806a59"/>
      <g transform="translate(540,68)"><g class="bj-fish">
        <path d="M0,0 Q-6,38 0,70" fill="none" stroke="{t['muted']}" stroke-width="1" stroke-dasharray="3 3"/>
        <g transform="translate(0,79)">
          <path d="M-13,0 L-27,-11 L-25,11 Z" fill="#739eae"/>
          <path d="M-18,0 Q0,-19 18,-1 Q4,18 -18,0 Z" fill="#94bdc3" stroke="#567986" stroke-width="1.2"/>
          <path d="M-8,1 Q1,5 0,10 L8,3 M-10,-4 l6,3 M-3,-7 l6,3" fill="none" stroke="#608a95" stroke-width="1.1"/>
          <circle cx="11" cy="-2" r="1.9" fill="#223d49"/>
          <path d="M-12,1 L10,1" stroke="#d8e6df" stroke-width=".8" stroke-dasharray="2 3"/>
        </g>
      </g></g>
      <path d="M766,171 H776 V291 H766 Z" fill="{t['grid']}" stroke="{t['border']}"/>
      <path d="M759,166 H781 V172 H759 Z" fill="{t['muted']}"/>
      <path d="M766,197 h10 M766,225 h10 M766,253 h10 M766,280 h10" stroke="{t['border']}"/>
      <g class="bj-shadow-travel"><ellipse class="bj-shadow" cy="292" rx="65" ry="5" fill="{t['muted']}" opacity=".16"/></g>
      <g transform="translate(0,{ground})"><g class="bj-travel"><g class="bj-facing">{cat}</g></g></g>
      {''.join(labels)}
      <text class="bj-still muted" x="450" y="322" text-anchor="middle" font-size="12">Backyard patrol · flowers, fish toys and questionable ledges</text>"""
    css += track("bj-shadow-travel", [(s, f"translateX({x}px)") for s, x, _, _, _ in BOJANGLES_STORY])
    css += track("bj-shadow", [(s, f"scaleX({max(.4, 1 + y / 150):.2f})") for s, _, y, _, _ in BOJANGLES_STORY])
    css += track("bj-flowers", [(0, "rotate(0deg)"), (4.8, "rotate(0deg)")] +
                 [(5 + i * .25, f"rotate({-2 if i % 2 else 2}deg)") for i in range(16)] + [(9, "rotate(0deg)"), (40, "rotate(0deg)")])
    css += track("bj-jaw", [(0, "translateY(0)")] +
                 [(4.8 + i * .2, f"translateY({3 if i % 2 else 0}px)") for i in range(22)] + [(9.2, "translateY(0)"), (40, "translateY(0)")])
    css += """
      .bj-travel, .bj-shadow-travel {transform:translateX(126px);}
      .bj-pitch {transform-origin:0px -65px;}
      .bj-head {transform-origin:40px -82px;}
      .bj-flowers {transform-origin:299px 284px;}
      .bj-fish {animation:bj-fish-sway 4s ease-in-out infinite alternate;}
      @keyframes bj-fish-sway {from {transform:rotate(-12deg);} to {transform:rotate(12deg);}}
      .bj-tail {animation:bj-tail-swish 3.4s ease-in-out infinite alternate;}
      @keyframes bj-tail-swish {from {transform:rotate(-5deg);} to {transform:rotate(7deg);}}
      .bj-blink {transform-box:fill-box;transform-origin:center;animation:bj-blink 5.3s infinite;}
      @keyframes bj-blink {0%,89%,96%,100% {transform:scaleY(1);} 92%,93% {transform:scaleY(.06);}}
      .bj-ear {transform-origin:57px 80px;animation:bj-ear-twitch 8.7s infinite;}
      @keyframes bj-ear-twitch {0%,91%,100% {transform:rotate(0deg);} 94% {transform:rotate(-7deg);} 97% {transform:rotate(2deg);}}
      .bj-caption, .bj-still {opacity:0;}
      @media (prefers-reduced-motion:reduce) {.bj-caption {display:none;} .bj-still {opacity:1;}}
    """
    return shell(w, h, t, body, "Bojangles · backyard adventures",
                 "A grey-brown tabby with a striped forehead, olive eyes and pale whiskers. "
                 "Bojangles nibbles catnip flowers, leaps for a moving toy fish, tries a narrow wall, "
                 "loses his grip, slides down, lands on his paws and walks on. "
                 "With reduced motion he stands quietly in the garden.", css)



def main():
    s = build_stats()
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [(name, fn) for name, fn in (("hero", hero), ("ticker", ticker), ("impact", impact), ("orbit", orbit), ("languages", languages), ("pipeline", pipeline), ("bojangles", bojangles))]
    jobs += [
        (f"acct-{key}", lambda th, _s, i=i, a=(nm, sub, col, mono): account(th, i, *a))
        for i, (key, nm, sub, col, mono) in enumerate(ACCOUNTS)
    ]
    live = {f"acct-{key}-{mode}.svg" for key, *_ in ACCOUNTS for mode in THEMES}
    for old in OUT.glob("acct-*.svg"):
        if old.name not in live:
            old.unlink()
    written = 0
    for name, fn in jobs:
        for mode, theme in THEMES.items():
            svg = fn(theme, s)
            if svg is None:
                print(f"skipping {name}-{mode}: no data")
                continue
            (OUT / f"{name}-{mode}.svg").write_text(svg, encoding="utf-8")
            written += 1
    print(f"wrote {written} SVGs to {OUT} ({s['merged_all']} merged PRs, {s['open_prs']} open)")


if __name__ == "__main__":
    main()
