#!/usr/bin/env python3
"""Generate the animated SVGs embedded in README.md from the repo's own JSON data.

Inputs (repo root):  workstream-archive.json, open-prs.json, activity.json, repo-languages.json
Outputs:             assets/profile/{hero,ticker,impact,orbit,languages,pipeline}-{dark,light}.svg

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


def shell(w, h, t, body, title, desc, extra_css=""):
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
    <clipPath id="clip"><rect width="{w}" height="{h}" rx="16"/></clipPath>
  </defs>
  <style>{css}</style>
  <rect width="{w}" height="{h}" rx="16" fill="url(#card)"/>
  <g clip-path="url(#clip)">
{body}
  </g>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="{t['border']}"/>
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
    planets_in = [("repo", r.split("/")[1], n, LANE_COLORS[lane], []) for r, n, lane in lane_repos]
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
        ((org, sum(n for _, n in rs), ([m for m in sorted(rs, key=lambda x: -x[1]) if m[1] >= 3] or sorted(rs, key=lambda x: -x[1]))[:3])
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


def main():
    s = build_stats()
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in (("hero", hero), ("ticker", ticker), ("impact", impact), ("orbit", orbit), ("languages", languages), ("pipeline", pipeline)):
        for mode, theme in THEMES.items():
            svg = fn(theme, s)
            if svg is None:
                print(f"skipping {name}-{mode}: no data")
                continue
            (OUT / f"{name}-{mode}.svg").write_text(svg, encoding="utf-8")
    print(f"wrote {len(THEMES) * 6} SVGs to {OUT} ({s['merged_all']} merged PRs, {s['open_prs']} open)")


if __name__ == "__main__":
    main()
