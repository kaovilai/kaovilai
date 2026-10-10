#!/usr/bin/env python3
"""Generate the animated SVGs embedded in README.md from the repo's own JSON data.

Inputs (repo root):  workstream-archive.json, open-prs.json, activity.json
Outputs:             assets/profile/{hero,impact,orbit,pipeline}-{dark,light}.svg

Stdlib only. Output is deterministic for identical input (no timestamps from the
clock, seeded randomness), so the scheduled workflow only commits on real change.
Animations are pure CSS keyframes (no JS, which GitHub strips) and are disabled
under prefers-reduced-motion.
"""
import json
import math
import random
import sys
from collections import Counter
from datetime import datetime
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


# --------------------------------------------------------------------------- hero
def hero(t, s):
    w, h = 900, 250
    rng = random.Random(7)
    dots = []
    cols, rows, x0, y0, step = 14, 6, 590, 34, 21
    for r in range(rows):
        for c in range(cols):
            lvl = rng.random()
            delay = rng.uniform(0, 6)
            dur = rng.uniform(3, 6)
            size = 14
            opacity = 0.12 + 0.55 * lvl * lvl
            color = t["accent"] if lvl > 0.55 else t["muted"]
            dots.append(
                f'<rect class="dot" x="{x0 + c * step}" y="{y0 + r * step}" width="{size}" height="{size}" rx="3" '
                f'fill="{color}" style="opacity:{opacity:.2f};animation-delay:-{delay:.1f}s;animation-duration:{dur:.1f}s"/>'
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
    for val, label in chips:
        cw = max(150, 14 + len(label) * 7 + 14)
        chip_svg.append(
            f'<g transform="translate({cx},186)"><rect width="{cw}" height="44" rx="10" fill="{t["chip"]}" stroke="{t["border"]}"/>'
            f'<text class="mono" x="14" y="20" font-size="17" font-weight="700" style="fill:{t["accent2"]}">{val}</text>'
            f'<text class="muted" x="14" y="36" font-size="11">{escape(label)}</text></g>'
        )
        cx += cw + 12
    body = f"""
    <circle class="drift1" cx="150" cy="40" r="210" fill="url(#aura)"/>
    <circle class="drift2" cx="760" cy="230" r="190" fill="url(#aura)"/>
    {''.join(dots)}
    <text class="mono muted" x="48" y="50" font-size="13">~/kaovilai $ <tspan class="cursor" style="fill:{t['accent2']}">whoami</tspan></text>
    <text x="46" y="108" font-size="50" font-weight="800" letter-spacing="-1">Tiger Kaovilai</text>
    {phrase_svg}
    {''.join(chip_svg)}"""
    css = f"""
    .dot {{ animation: twinkle 4s ease-in-out infinite; }}
    @keyframes twinkle {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(.6); opacity: .9; }} }}
    .dot {{ transform-box: fill-box; transform-origin: center; }}
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
    bars = []
    for i, yr in enumerate(ys):
        v = years[yr]
        bh = max(2, ch * v / top)
        x = cx0 + i * slot + (slot - bw) / 2
        last = yr == ys[-1]
        fill = "url(#hot)" if last else t["muted"]
        op = "1" if last else ".55"
        delay = 0.15 + i * 0.12
        bars.append(
            f'<rect class="bar{" now" if last else ""}" x="{x:.1f}" y="{base - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="5" '
            f'fill="{fill}" style="opacity:{op};animation-delay:{delay:.2f}s"/>'
            f'<text class="mono pop" x="{x + bw / 2:.1f}" y="{base - bh - 8:.1f}" font-size="12" font-weight="700" text-anchor="middle" '
            f'style="animation-delay:{delay + .5:.2f}s;{"fill:" + t["accent2"] if last else ""}">{v}</text>'
            f'<text class="mono muted" x="{x + bw / 2:.1f}" y="{base + 20}" font-size="11" text-anchor="middle">{yr}{"*" if last else ""}</text>'
        )
    body = f"""
    <text x="32" y="38" font-size="18" font-weight="700">Merged PRs per year</text>
    <text class="muted" x="32" y="58" font-size="12">Public repos outside my personal namespace · {s['merged_all']:,} total · *{s['year']} is year-to-date</text>
    {''.join(grid)}
    {''.join(bars)}"""
    css = """
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
    w, h = 900, 400
    cx, cy = 600, 200
    repos = s["top_repos"][:9]
    peak = max(n for _, n, _ in repos)
    rings = [(88, repos[:4], 90, 1), (142, repos[4:], 140, -1)]
    ring_svg = []
    planets = []
    short = Counter(r.split("/")[1] for r, _, _ in repos)
    for radius, members, period, direction in rings:
        ring_svg.append(
            f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{t["border"]}" stroke-dasharray="3 6"/>'
        )
        for i, (repo, n, lane) in enumerate(members):
            angle = 360 * i / len(members) + (20 if direction < 0 else 0)
            pr = 8 + 15 * math.sqrt(n / peak)
            color = LANE_COLORS[lane]
            org, name = repo.split("/")
            if short[name] > 1:
                name = f"{org}/{name}"
            if len(name) > 22:
                name = name[:21] + "…"
            anim = "spin" if direction > 0 else "spinr"
            counter = "spinr" if direction > 0 else "spin"
            planets.append(
                f'<g transform="translate({cx},{cy}) rotate({angle:.0f})"><g class="o" style="animation-name:{anim};animation-duration:{period}s">'
                f'<g transform="translate({radius},0)">'
                f'<circle r="{pr + 5:.1f}" fill="{color}" opacity=".18"/>'
                f'<circle r="{pr:.1f}" fill="{color}"/>'
                f'<g class="o" style="animation-name:{counter};animation-duration:{period}s">'
                # the wrapping rotate() above is static, so cancel it with a fixed counter-rotation too
                f'<g transform="rotate({-angle:.0f})">'
                f'<text class="mono" y="{pr + 15:.1f}" font-size="10" text-anchor="middle" style="paint-order:stroke;stroke:{t["bg1"]};stroke-width:3px">{escape(name)}</text>'
                f'<text class="mono muted" y="{pr + 27:.1f}" font-size="10" text-anchor="middle" style="paint-order:stroke;stroke:{t["bg1"]};stroke-width:3px">{n}</text>'
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
    <text class="muted" x="32" y="58" font-size="12">Merged PRs by repository · size = volume · colour = workstream</text>
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
    .pulse { transform-box: fill-box; transform-origin: center; animation: breathe 4s ease-in-out infinite; }
    @keyframes breathe { 0%,100% { transform: scale(.85); opacity: .6; } 50% { transform: scale(1.35); opacity: 1; } }"""
    return shell(w, h, t, body, "Merged pull requests by repository",
                 "Orbit diagram: repositories sized by merged PR count, coloured by workstream.", css)


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
        segs.append(f'<rect class="{"ready" if key == "ready" else ""}" x="{x:.1f}" y="{by}" width="{sw:.1f}" height="{bh}" fill="{color}"/>')
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
    <g clip-path="url(#reveal)">{''.join(segs)}</g>
    {''.join(legend)}"""
    css = """
    .wipe { transform-box: fill-box; transform-origin: left; animation: wipe 1.4s cubic-bezier(.2,.8,.2,1) both; }
    @keyframes wipe { from { transform: scaleX(0); } to { transform: scaleX(1); } }
    .ready { animation: beat 2.6s ease-in-out 1.6s infinite; }
    @keyframes beat { 0%,100% { opacity: 1; } 50% { opacity: .6; } }"""
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
    top = [(r, n, lane_for(r, lane_votes)) for r, n in by_repo.most_common(9)]
    lane_totals = Counter()
    for r, n in by_repo.items():
        lane_totals[lane_for(r, lane_votes)] += n

    open_prs = [p for p in prs["prs"] if p["org"] != OWNER]
    rq = prs.get("reviewQueue", {})
    return dict(
        year=year,
        merged_all=len(merged),
        merged_ytd=by_year[str(year)],
        merged_by_year={int(y): n for y, n in by_year.items()},
        top_repos=top,
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
    for name, fn in (("hero", hero), ("impact", impact), ("orbit", orbit), ("pipeline", pipeline)):
        for mode, theme in THEMES.items():
            (OUT / f"{name}-{mode}.svg").write_text(fn(theme, s), encoding="utf-8")
    print(f"wrote {len(THEMES) * 4} SVGs to {OUT} ({s['merged_all']} merged PRs, {s['open_prs']} open)")


if __name__ == "__main__":
    main()
