"""Career-map artwork and Pages companion, generated from career-map.json.

Stdlib only; no live resume scraping, invented employment dates, or external UI
libraries. The README SVGs work without JavaScript. The optional Pages view adds
keyboard-friendly detail previews while keeping all facts in a text table.
"""
from html import escape

PALETTES = {
    "light": ("#2a78d6", "#eb6834", "#1baf7a"),
    "dark": ("#3987e5", "#d95926", "#199e70"),
}


def variables(theme):
    colors = PALETTES["dark" if theme["bg1"] == "#0d1117" else "light"]
    return dict(zip(("bg", "panel", "ink", "muted", "line", "edu", "work", "oss"),
                    (theme["bg1"], theme["bg2"], theme["text"], theme["muted"], theme["border"], *colors)))


def tokens(theme):
    return ";".join(f"--cm-{key}:{value}" for key, value in variables(theme).items())


def validate_career_data(data):
    for key, count in (("places", 3), ("education", 3), ("industry", 3), ("community", 1)):
        items = data.get(key)
        if not isinstance(items, list) or len(items) != count:
            raise ValueError(f"Career-map layout expects {count} {key} entries; update the layout for new branches")


def render_career_svg(theme, data, compact=False):
    validate_career_data(data)
    w, h = (480, 1450) if compact else (900, 654)
    variant = "mobile" if compact else "desktop"
    parts = []

    def text(x, y, value, size=14, cls="", weight=400):
        return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" class="{cls}">{escape(value)}</text>'

    def marker(x, y, kind, size=6):
        if kind == "work":
            shape = f'<rect x="{x-size}" y="{y-size}" width="{size*2}" height="{size*2}" rx="2"/>'
        elif kind == "edu":
            shape = f'<path d="M{x},{y-size-1} l{size+1},{size+1} l{-size-1},{size+1} l{-size-1},{-size-1} Z"/>'
        else:
            shape = f'<circle cx="{x}" cy="{y}" r="{size}"/>'
        return f'<g class="cm-mark {kind}" stroke="var(--cm-bg)" stroke-width="2">{shape}</g>'

    def card(x, y, width, height, kind, key, label, lines):
        detail = ". ".join([label, *[line[0] for line in lines]])
        return (f'<a class="cm-node" href="#detail-{escape(key, quote=True)}" data-detail="{escape(key, quote=True)}">'
                f'<title>{escape(detail)}</title><rect class="cm-card" x="{x}" y="{y}" width="{width}" height="{height}" rx="12"/>'
                + marker(x + 22, y + 26, kind)
                + text(x + 40, y + 31, label, 18, weight=650)
                + "".join(text(x + 18, y + 59 + i * 24, value, size, cls, weight)
                          for i, (value, size, cls, weight) in enumerate(lines)) + '</a>')

    parts.append(f'<rect class="cm-bg" x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16"/>')
    parts.append(text(28, 36, "Career map", 23, weight=650))
    headings = (["From first programs", "to upstream leadership"] if compact else
                ["From first programs to upstream leadership"])
    for i, heading in enumerate(headings):
        parts.append(text(28, 72 + i * 31, heading, 26, weight=650))
    parts.append(text(28, 132 if compact else 96, "Connections, not a time scale", 12, "cm-muted"))

    # Geography is a schematic route, not a duration or distance axis.
    for i, place in enumerate(data["places"]):
        x, y, width = (54, 190 + i * 156, 398) if compact else (28 + i * 294, 170, 256)
        point_x, point_y = (30, y + 26) if compact else (x + 22, 146)
        if i < 2:
            path = (f'M30,{point_y} V{point_y+156}' if compact else f'M{point_x},{point_y} h294')
            parts.append(f'<path class="cm-route" d="{path}"/>')
            parts.append(f'<path class="cm-flow" d="{path}" style="animation-delay:{-i*1.2}s"/>')
        parts.append(marker(point_x, point_y, "edu"))
        school_lines = []
        for school in place["schools"]:
            name = school["name"].replace("North Carolina State University", "NC State University")
            school_lines.append((name, 13, "", 400))
            if school["dates"]:
                school_lines.append((school["dates"], 12, "cm-muted", 400))
        if place["skills"]:
            school_lines.append((" + ".join(place["skills"]), 13, "cm-muted", 400))
        # Raleigh's qualification dates belong to their degrees, not a residence range.
        parts.append(card(x, y, width, 140, "edu", place["id"], place["city"],
                          [(place["country"], 12, "cm-muted", 400), *school_lines]))

    branch_y = 684 if compact else 374
    branch_w = 424 if compact else 272
    degree, minor, cs50 = data["education"]
    current, marketing, bank = data["industry"]
    community = data["community"][0]
    branches = [
        ("edu", "education", "Engineering foundation", [
            (f'NC State · {degree["qualification"]}', 13, "", 500),
            (degree["dates"], 12, "cm-muted", 400),
            (f'{minor["qualification"]} · {minor["dates"]}', 12, "", 400),
            (f'{cs50["name"]} · {cs50["dates"]}', 13, "", 400),
            ("Human factors + software systems", 12, "cm-muted", 400),
        ]),
        ("work", "industry", "Building systems", [
            (f'{current["name"]} · {current["role"]}', 13, "", 500),
            (current["focus"], 13, "", 400),
            (f'{marketing["name"]} · {marketing["role"]}', 11, "cm-muted", 400),
            (f'{bank["name"]} · {bank["role"]}', 12, "cm-muted", 400),
            ("Go · Kubernetes · delivery automation", 12, "cm-muted", 400),
        ]),
        ("oss", "community", "Upstream leadership", [
            (f'{community["name"]} {community["role"].lower()}', 15, "", 600),
            (community["focus"], 13, "", 400),
            *[(skill, 13, "cm-muted", 400) for skill in community["skills"]],
        ]),
    ]
    for i, (kind, key, label, lines) in enumerate(branches):
        x, y = (28, branch_y + i * 220) if compact else (28 + i * 286, branch_y)
        if not compact:
            parts.append(f'<path class="cm-link" d="M{x+136},342 V{y}"/>')
        parts.append(card(x, y, branch_w, 194, kind, key, label, lines))
        if kind == "oss":
            parts.append(f'<circle class="cm-beacon" cx="{x+22}" cy="{y+26}" r="11"/>')
    if not compact:
        parts.append('<path class="cm-link" d="M164,342 H736 M736,310 V342"/>')
    footer_y = 1378 if compact else 604
    parts.append(text(28, footer_y, "Alongside the day job", 13, weight=650))
    parts.append(text(28, footer_y + 24, " · ".join(data["projects"]["skills"]), 12, "cm-muted"))
    legend_y = 165 if compact else 126
    for i, (label, kind) in enumerate((("Education", "edu"), ("Industry", "work"), ("Community", "oss"))):
        x = 36 + i * (141 if compact else 134)
        parts.append(marker(x, legend_y - 4, kind, 5))
        parts.append(text(x + 13, legend_y, label, 12, "cm-muted"))
    css = f"""
      .career-viz {{{tokens(theme)};font-family:system-ui,-apple-system,'Segoe UI',sans-serif;}}
      .career-viz text {{fill:var(--cm-ink);}}
      .career-viz .cm-muted {{fill:var(--cm-muted);}}
      .cm-bg {{fill:var(--cm-bg);stroke:var(--cm-line);}}
      .cm-card {{fill:var(--cm-panel);stroke:var(--cm-line);stroke-width:1;}}
      .edu {{fill:var(--cm-edu);}} .work {{fill:var(--cm-work);}} .oss {{fill:var(--cm-oss);}}
      .cm-route {{fill:none;stroke:var(--cm-line);stroke-width:2;}}
      .cm-link {{fill:none;stroke:var(--cm-line);stroke-width:1;}}
      .cm-flow {{fill:none;stroke:var(--cm-edu);stroke-width:2;stroke-dasharray:12 282;animation:cm-flow 8s linear infinite;}}
      @keyframes cm-flow {{to {{stroke-dashoffset:-294;}}}}
      .cm-beacon {{fill:none;stroke:var(--cm-oss);stroke-width:2;opacity:.5;animation:cm-beacon 4s ease-in-out infinite;}}
      @keyframes cm-beacon {{50% {{opacity:.15;r:15;}}}}
      .cm-node:hover .cm-card,.cm-node:focus .cm-card {{stroke:var(--cm-ink);}}
      @media(prefers-reduced-motion:reduce) {{.career-viz * {{animation:none!important;}}}}
      @media(forced-colors:active) {{.cm-mark {{fill:CanvasText;}} .cm-card,.cm-bg {{fill:Canvas;stroke:CanvasText;}} .career-viz text {{fill:CanvasText;}}}}
    """
    description = ("Career connections from Bangkok, Thailand, through Invercargill, New Zealand, to Raleigh, North Carolina. "
                   "NC State Industrial Engineering and Computer Science; Red Hat Senior Software Engineer working on OADP; "
                   "Red Hat Technical Marketing and Deutsche Bank dbAchieve internships; Velero maintainer and community mentor. "
                   "Personal projects use Flutter/Dart, Vue/NextJS, GitHub Actions and CircleCI. Education dates are documented; "
                   "employment dates are unspecified. Lines show connections, not measured time or geographic distance.")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="career-viz" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="cm-{variant}-title cm-{variant}-desc">'
            f'<title id="cm-{variant}-title">Tiger Kaovilai · career map</title>'
            f'<desc id="cm-{variant}-desc">{escape(description)}</desc><style>{css}</style>'
            + "".join(parts) + '</svg>\n')


def detail_rows(data):
    rows = []
    for place in data["places"]:
        entries = "; ".join(s["name"] + (f' ({s["dates"]})' if s["dates"] else " (dates unspecified)")
                            for s in place["schools"])
        rows.append((place["id"], place["city"], entries, place["skills"]))
    for item in data["education"]:
        rows.append(("education", item["name"], f'{item["qualification"]} · {item["dates"]}', item["skills"]))
    for item in data["industry"]:
        rows.append(("industry", item["name"], f'{item["role"]} · {item["context"]} · {item["focus"]} · dates unspecified', item["skills"]))
    for item in data["community"]:
        rows.append(("community", item["name"], f'{item["role"]} · {item["focus"]}', item["skills"]))
    rows.append(("projects", data["projects"]["name"], data["projects"]["focus"], data["projects"]["skills"]))
    return rows


def render_career_page(data, themes):
    # Inline both layouts, each with unique accessibility IDs. CSS selects layout and theme.
    desktop = render_career_svg(themes["light"], data)
    mobile = render_career_svg(themes["light"], data, True)
    rows, seen = [], set()
    for key, name, detail, skills in detail_rows(data):
        safe_key = escape(key, quote=True)
        anchor = f' id="detail-{safe_key}"' if key not in seen else ""
        seen.add(key)
        rows.append(f'<tr data-group="{safe_key}"{anchor}><th scope="row">{escape(name)}</th><td>{escape(detail)}</td>'
                    f'<td>{escape(", ".join(skills)) or "—"}</td></tr>')
    table = "".join(rows)
    links = " · ".join(f'<a href="{escape(data["links"][key], quote=True)}">{label}</a>'
                       for key, label in (("resume", "Resume"), ("linkedin", "LinkedIn"), ("oadp", "OADP"), ("velero", "Velero")))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tiger Kaovilai · career map</title><meta name="description" content="Education, engineering and upstream leadership: Tiger Kaovilai's career connections.">
<style>
:root {{color-scheme:light;{tokens(themes['light'])};}}
@media(prefers-color-scheme:dark) {{:root {{{tokens(themes['dark'])};color-scheme:dark;}} :root:not([data-theme="light"]) .career-viz {{{tokens(themes['dark'])};}}}}
:root[data-theme="light"],:root[data-theme="light"] .career-viz {{{tokens(themes['light'])};color-scheme:light;}}
:root[data-theme="dark"],:root[data-theme="dark"] .career-viz {{{tokens(themes['dark'])};color-scheme:dark;}}
* {{box-sizing:border-box;}} body {{margin:0;background:var(--cm-bg);color:var(--cm-ink);font:15px/1.6 system-ui,-apple-system,'Segoe UI',sans-serif;}}
main {{max-width:1060px;margin:auto;padding:30px 24px 60px;}} nav {{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:22px;}}
a {{color:var(--cm-ink);text-underline-offset:4px;}} button,select {{font:inherit;padding:7px 12px;background:var(--cm-panel);color:var(--cm-ink);border:1px solid var(--cm-line);border-radius:8px;}}
.controls {{display:flex;align-items:center;gap:12px;flex-wrap:wrap;}} .controls[hidden] {{display:none;}}
button:focus-visible,select:focus-visible,a:focus-visible {{outline:2px solid var(--cm-ink);outline-offset:4px;}}
.visual {{position:relative;}} .career-viz {{display:block;width:100%;height:auto;}} .mobile {{display:none;}}
#tooltip {{position:absolute;z-index:2;max-width:310px;padding:14px 16px;border:1px solid var(--cm-line);border-radius:12px;background:var(--cm-bg);box-shadow:0 8px 30px #0003;font-size:13px;}}
#tooltip[hidden] {{display:none;}} .help,.note {{color:var(--cm-muted);}} .help {{font-size:13px;}}
[data-motion="off"] .career-viz * {{animation:none!important;}}
h1 {{font-size:23px;margin:28px 0 4px;}} table {{width:100%;border-collapse:collapse;font-size:14px;}} th,td {{text-align:left;vertical-align:top;padding:14px 12px;border-bottom:1px solid var(--cm-line);}} thead th {{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--cm-muted);}} tbody th {{width:22%;}} td:last-child {{width:35%;}} tr.is-highlighted {{background:var(--cm-panel);}} .table-wrap {{overflow-x:auto;}}
@media(max-width:600px) {{main {{padding:20px 14px 40px;}} .desktop {{display:none;}} .mobile {{display:block;}} table {{min-width:650px;}}}}
@media(prefers-reduced-motion:reduce) {{* {{scroll-behavior:auto!important;}}}}
@media print {{.controls,.help,#tooltip {{display:none;}} .career-viz * {{animation:none!important;}} main {{padding:0;}}}}
</style></head><body><main>
<nav aria-label="Career navigation"><a href="../">← Profile</a><div>{links}</div><div class="controls" hidden>
<label>Theme <select id="theme"><option value="system">System</option><option value="light">Light</option><option value="dark">Dark</option></select></label>
<button type="button" id="motion" aria-pressed="false">Pause animation</button></div></nav>
<div class="visual"><div class="desktop">{desktop}</div><div class="mobile">{mobile}</div><div id="tooltip" role="tooltip" hidden></div></div>
<p class="help">Hover or focus a map card for detail. Select a card to jump to its rows. Every fact is available below without animation or JavaScript.</p>
<h1>Career details</h1><p class="note">{escape(data['note'])}</p>
<div class="table-wrap" role="region" aria-label="Career facts" tabindex="0"><table><thead><tr><th scope="col">Place / organization</th><th scope="col">Study / role</th><th scope="col">Tools / themes</th></tr></thead><tbody>{table}</tbody></table></div>
</main><script>
const root = document.documentElement;
const tooltip = document.getElementById('tooltip');
const rows = [...document.querySelectorAll('tbody tr')];
document.querySelector('.controls').hidden = false;
document.getElementById('theme').addEventListener('change', event => {{
  if (event.target.value === 'system') delete root.dataset.theme;
  else root.dataset.theme = event.target.value;
}});
document.getElementById('motion').addEventListener('click', event => {{
  const paused = root.dataset.motion !== 'off';
  root.dataset.motion = paused ? 'off' : 'on';
  event.currentTarget.setAttribute('aria-pressed', String(paused));
  event.currentTarget.textContent = paused ? 'Resume animation' : 'Pause animation';
}});
let hideTimer;
function hide() {{clearTimeout(hideTimer);tooltip.hidden = true;}}
function laterHide() {{hideTimer = setTimeout(hide, 180);}}
tooltip.addEventListener('pointerenter', () => clearTimeout(hideTimer));
tooltip.addEventListener('pointerleave', hide);
function show(node) {{
  clearTimeout(hideTimer);
  const matches = rows.filter(row => row.dataset.group === node.dataset.detail);
  tooltip.textContent = matches.map(row => [...row.cells].map(cell => cell.textContent).join(' — ')).join('\\n\\n');
  tooltip.style.whiteSpace = 'pre-line';
  tooltip.hidden = false;
  const box = node.getBoundingClientRect();
  const area = document.querySelector('.visual').getBoundingClientRect();
  const maxLeft = Math.max(0, area.width - tooltip.offsetWidth);
  tooltip.style.left = Math.max(0, Math.min(box.left - area.left, maxLeft)) + 'px';
  tooltip.style.top = Math.max(0, box.top - area.top - tooltip.offsetHeight - 10) + 'px';
}}
for (const node of document.querySelectorAll('.cm-node')) {{
  node.setAttribute('aria-describedby', 'tooltip');
  node.addEventListener('pointerenter', () => show(node));
  node.addEventListener('pointerleave', laterHide);
  node.addEventListener('focus', () => show(node));
  node.addEventListener('blur', hide);
  node.addEventListener('click', () => {{
    hide();
    rows.forEach(row => row.classList.toggle('is-highlighted', row.dataset.group === node.dataset.detail));
  }});
}}
document.addEventListener('keydown', event => {{if (event.key === 'Escape') hide();}});
window.addEventListener('resize', hide);
</script></body></html>
"""
