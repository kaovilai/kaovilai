"use strict";

/* ==========================================================================
   Workstream Dashboard — vanilla JS, no build step, no deps.
   Renders two real Sankey diagrams (Milestone -> Workstream -> Status) for
   issues assigned to me and PRs opened by me, across every repo/org.
   ========================================================================== */

/* ---------- workstream identity (colorblind-validated, do not change hues) ---------- */

/* Fixed node identity + stacking order for the Workstream column. Every
   issue/PR is pre-classified by the data-fetch script into exactly one of
   these keys — identity is never re-ranked by count, and an unrecognized
   key falls back to "Uncategorized". */
const WORKSTREAM_NODE_ORDER = [
  { key: "Velero", label: "Velero", color: "var(--ws-velero)" },
  { key: "OADP", label: "OADP", color: "var(--ws-oadp)" },
  { key: "KubeVirt Data Mover", label: "KubeVirt Data Mover", color: "var(--ws-kubevirt-dm)" },
  { key: "Kubernetes", label: "Kubernetes", color: "var(--ws-kubernetes)" },
  { key: "CNCF Landscape", label: "CNCF Landscape", color: "var(--ws-cncf)" },
  { key: "Uncategorized", label: "Uncategorized", color: "var(--ws-uncategorized)" },
];
const KNOWN_WORKSTREAM_KEYS = new Set(WORKSTREAM_NODE_ORDER.map((w) => w.key));

function workstreamKeyFor(item) {
  return KNOWN_WORKSTREAM_KEYS.has(item.workstream) ? item.workstream : "Uncategorized";
}

function workstreamColor(key) {
  const def = WORKSTREAM_NODE_ORDER.find((w) => w.key === key);
  return def ? def.color : "var(--ws-uncategorized)";
}

const PR_STATUS_META = {
  ready: { pill: "good", icon: "✅", label: "mergeable" },
  conflicts: { pill: "critical", icon: "💥", label: "conflicts" },
  "missing-checks": { pill: "warning", icon: "⏳", label: "missing checks" },
  "missing-reviews": { pill: "warning", icon: "👀", label: "missing reviews" },
  "unresolved-conversations": { pill: "warning", icon: "💬", label: "unresolved conversations" },
  blocked: { pill: "warning", icon: "🚧", label: "blocked (other)" },
  hold: { pill: "warning", icon: "✋", label: "hold" },
  "failing-ci": { pill: "critical", icon: "❌", label: "failing CI" },
  draft: { pill: "neutral", icon: "📝", label: "draft" },
  stale: { pill: "neutral", icon: "🕸️", label: "stale" },
};

const ISSUE_STATUS_META = {
  open: { pill: "good", icon: "🟢", label: "open" },
  stale: { pill: "neutral", icon: "🕸️", label: "stale" },
};

/* Fixed status column order per section — never sorted by count. */
const ISSUE_STATUS_ORDER = ["open", "stale"];
const PR_STATUS_ORDER = [
  "ready",
  "conflicts",
  "missing-checks",
  "missing-reviews",
  "unresolved-conversations",
  "blocked",
  "hold",
  "failing-ci",
  "draft",
  "stale",
];

function shortRepoLabel(repo) {
  const parts = repo.split("/");
  return parts[parts.length - 1] || repo;
}

function statusLabel(key, metaMap) {
  return (metaMap[key] && metaMap[key].label) || key;
}

function relativeAge(isoString) {
  if (!isoString) return "";
  const then = new Date(isoString).getTime();
  if (Number.isNaN(then)) return "";
  const diffMs = Date.now() - then;
  const diffSec = Math.round(diffMs / 1000);
  const abs = Math.abs(diffSec);

  const units = [
    ["y", 60 * 60 * 24 * 365],
    ["mo", 60 * 60 * 24 * 30],
    ["d", 60 * 60 * 24],
    ["h", 60 * 60],
    ["m", 60],
  ];
  for (const [suffix, secs] of units) {
    if (abs >= secs) {
      const val = Math.floor(abs / secs);
      return diffSec >= 0 ? `${val}${suffix} ago` : `in ${val}${suffix}`;
    }
  }
  return diffSec >= 0 ? "just now" : "shortly";
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function renderRepoTag(repo, workstream) {
  const color = workstreamColor(workstreamKeyFor({ workstream }));
  return `<span class="repo-tag">
    <span class="repo-dot" style="background:${color}" aria-hidden="true"></span>
    <span>${escapeHtml(shortRepoLabel(repo))}</span>
  </span>`;
}

function renderPill(meta) {
  if (!meta) return "";
  return `<span class="pill pill-${meta.pill}"><span aria-hidden="true">${meta.icon}</span>${escapeHtml(meta.label)}</span>`;
}

function renderBlockedGraphic() {
  return `<svg class="blocked-graphic" width="46" height="18" viewBox="0 0 46 18" aria-hidden="true">
    <title>blocked on review — arrow hits the wall</title>
    <line x1="1" y1="9" x2="29" y2="9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <polygon points="30,3.5 30,14.5 25,9" fill="currentColor"/>
    <line x1="30" y1="2" x2="34" y2="-1" stroke="currentColor" stroke-width="1" stroke-linecap="round" transform="translate(0,3)"/>
    <line x1="30" y1="16" x2="34" y2="19" stroke="currentColor" stroke-width="1" stroke-linecap="round" transform="translate(0,-3)"/>
    <g class="brick-wall" fill="none" stroke="currentColor" stroke-width="1.25">
      <rect x="33" y="1" width="12" height="16" rx="1.5"/>
      <line x1="33" y1="5.3" x2="45" y2="5.3"/>
      <line x1="33" y1="9" x2="45" y2="9"/>
      <line x1="33" y1="12.7" x2="45" y2="12.7"/>
      <line x1="39" y1="1" x2="39" y2="5.3"/>
      <line x1="35.5" y1="5.3" x2="35.5" y2="9"/>
      <line x1="42.5" y1="5.3" x2="42.5" y2="9"/>
      <line x1="39" y1="9" x2="39" y2="12.7"/>
      <line x1="35.5" y1="12.7" x2="35.5" y2="17"/>
      <line x1="42.5" y1="12.7" x2="42.5" y2="17"/>
    </g>
  </svg>`;
}

/* ==========================================================================
   Sankey data model
   ========================================================================== */

/**
 * Fixed milestone bucket order + labels. `recognizedMilestones[0]` is the
 * current release, `[1]` (if present) is the next release. Buckets with no
 * matching slot are omitted entirely (not just left empty).
 */
function milestoneBucketDefs(recognizedMilestones) {
  const current = recognizedMilestones[0] || null;
  const next = recognizedMilestones[1] || null;
  return [
    { key: "current", enabled: !!current, rawLabel: current ? `current release — ${current}` : null },
    { key: "next", enabled: !!next, rawLabel: next ? `next release — ${next}` : null },
    { key: "other", enabled: true, rawLabel: "other milestone" },
    { key: "none", enabled: true, rawLabel: "no milestone" },
  ].filter((d) => d.enabled);
}

function milestoneKeyFor(item, recognizedMilestones) {
  const current = recognizedMilestones[0];
  const next = recognizedMilestones[1];
  const m = item.milestone;
  if (m && current && m === current) return "current";
  if (m && next && m === next) return "next";
  if (m) return "other";
  return "none";
}

/**
 * Builds the three fixed-order node columns (Milestone -> Workstream ->
 * Status) and the two link sets between them, for one section (issues or
 * PRs). Column order and per-node sub-flow order are both driven by the
 * fixed category arrays — never re-ranked by count.
 */
function buildSankeyData(items, recognizedMilestones, statusOrder, statusMetaMap) {
  const milestoneNodes = [];
  for (const def of milestoneBucketDefs(recognizedMilestones)) {
    const subset = items.filter((it) => milestoneKeyFor(it, recognizedMilestones) === def.key);
    if (!subset.length) continue;
    milestoneNodes.push({ key: def.key, rawLabel: def.rawLabel, count: subset.length, items: subset });
  }

  const workstreamNodes = [];
  for (const wdef of WORKSTREAM_NODE_ORDER) {
    const subset = items.filter((it) => workstreamKeyFor(it) === wdef.key);
    if (!subset.length) continue;
    workstreamNodes.push({ key: wdef.key, rawLabel: wdef.label, color: wdef.color, count: subset.length, items: subset });
  }

  const statusNodes = [];
  for (const skey of statusOrder) {
    const subset = items.filter((it) => it.status === skey);
    if (!subset.length) continue;
    statusNodes.push({ key: skey, rawLabel: statusLabel(skey, statusMetaMap), count: subset.length, items: subset });
  }

  const linksMS = [];
  for (const mnode of milestoneNodes) {
    for (const wdef of WORKSTREAM_NODE_ORDER) {
      const subset = mnode.items.filter((it) => workstreamKeyFor(it) === wdef.key);
      if (!subset.length) continue;
      linksMS.push({
        source: mnode.key,
        sourceLabel: mnode.rawLabel,
        target: wdef.key,
        targetLabel: wdef.label,
        count: subset.length,
        items: subset,
        color: wdef.color,
      });
    }
  }

  const linksRS = [];
  for (const wnode of workstreamNodes) {
    for (const skey of statusOrder) {
      const subset = wnode.items.filter((it) => it.status === skey);
      if (!subset.length) continue;
      linksRS.push({
        source: wnode.key,
        sourceLabel: wnode.rawLabel,
        target: skey,
        targetLabel: statusLabel(skey, statusMetaMap),
        count: subset.length,
        items: subset,
        color: wnode.color,
      });
    }
  }

  return { milestoneNodes, workstreamNodes, statusNodes, linksMS, linksRS, total: items.length };
}

/* ==========================================================================
   Sankey layout
   ========================================================================== */

const VIEW_W = 1100;
const NODE_W = 16;
const NODE_GAP = 6;
const COL0_X = 210;
const COL2_X = VIEW_W - 210 - NODE_W;
const COL1_X = Math.round((COL0_X + NODE_W + COL2_X) / 2 - NODE_W / 2);
const PLOT_TOP = 46;
const PLOT_BOTTOM = 20;

function layoutColumn(nodes, total, plotTop, plotHeight, gap) {
  const usable = plotHeight - gap * Math.max(0, nodes.length - 1);
  let y = plotTop;
  for (const node of nodes) {
    const h = Math.max(2, (node.count / total) * usable);
    node.y = y;
    node.height = h;
    y += h + gap;
  }
}

function assignOutgoing(nodes, links, sourceProp) {
  for (const node of nodes) {
    const subset = links.filter((l) => l[sourceProp] === node.key);
    let y = node.y;
    for (const link of subset) {
      const h = (link.count / node.count) * node.height;
      link._srcY0 = y;
      link._srcY1 = y + h;
      y += h;
    }
  }
}

function assignIncoming(nodes, links, targetProp) {
  for (const node of nodes) {
    const subset = links.filter((l) => l[targetProp] === node.key);
    let y = node.y;
    for (const link of subset) {
      const h = (link.count / node.count) * node.height;
      link._tgtY0 = y;
      link._tgtY1 = y + h;
      y += h;
    }
  }
}

const SVG_NS = "http://www.w3.org/2000/svg";

function svgEl(tag, attrs) {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs || {})) el.setAttribute(k, v);
  return el;
}

function makeInteractive(el, onActivate, ariaLabel) {
  el.setAttribute("tabindex", "0");
  el.setAttribute("role", "button");
  el.setAttribute("aria-label", ariaLabel);
  el.addEventListener("click", onActivate);
  el.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      onActivate();
    }
  });
}

function buildBlockedIcon(x, y) {
  const wrapper = document.createElement("div");
  wrapper.innerHTML = renderBlockedGraphic();
  const inner = wrapper.firstElementChild;
  inner.setAttribute("x", x);
  inner.setAttribute("y", y);
  return inner;
}

/**
 * Classic two-bezier Sankey link shape: an independent cubic curve along
 * the top edge and along the bottom edge (both using a mid-column control
 * x), so band thickness stays constant along its length instead of
 * tapering to a point.
 */
function sankeyLinkPath(sourceX, targetX, srcY0, srcY1, tgtY0, tgtY1) {
  const midX = (sourceX + targetX) / 2;
  return (
    `M ${sourceX} ${srcY0} ` +
    `C ${midX} ${srcY0} ${midX} ${tgtY0} ${targetX} ${tgtY0} ` +
    `L ${targetX} ${tgtY1} ` +
    `C ${midX} ${tgtY1} ${midX} ${srcY1} ${sourceX} ${srcY1} Z`
  );
}

function drawLinks(layer, links, xA, xB, onLinkActivate) {
  const sourceX = xA + NODE_W;
  const targetX = xB;
  for (const link of links) {
    const path = svgEl("path", {
      d: sankeyLinkPath(sourceX, targetX, link._srcY0, link._srcY1, link._tgtY0, link._tgtY1),
      fill: link.color,
      class: "sankey-link",
    });
    const label = `${link.sourceLabel} → ${link.targetLabel}: ${link.count} item${link.count === 1 ? "" : "s"}`;
    const title = svgEl("title", {});
    title.textContent = label;
    path.appendChild(title);
    makeInteractive(path, () => onLinkActivate(link), label);
    layer.appendChild(path);
  }
}

function drawNodes(nodeLayer, labelLayer, nodes, x, side, onNodeActivate) {
  for (const node of nodes) {
    const isWorkstreamCol = side === "middle";
    const rect = svgEl("rect", {
      x,
      y: node.y,
      width: NODE_W,
      height: Math.max(node.height, 1),
      rx: 2,
      class: "sankey-node" + (isWorkstreamCol ? " sankey-node-repo" : " sankey-node-neutral"),
    });
    if (isWorkstreamCol) rect.setAttribute("fill", node.color);

    const displayLabel = `${node.rawLabel} (${node.count})`;
    const title = svgEl("title", {});
    title.textContent = displayLabel;
    rect.appendChild(title);
    makeInteractive(rect, () => onNodeActivate(node, displayLabel), `${displayLabel} — show items`);
    nodeLayer.appendChild(rect);

    const centerY = node.y + node.height / 2;
    let iconOffset = 0;
    if (side === "right" && node.key === "missing-reviews") {
      labelLayer.appendChild(buildBlockedIcon(x + NODE_W + 10, centerY - 9));
      iconOffset = 46 + 6;
    }

    const text = svgEl("text", { class: "sankey-node-label" });
    if (side === "left") {
      text.setAttribute("x", x - 10);
      text.setAttribute("y", centerY);
      text.setAttribute("text-anchor", "end");
      text.setAttribute("dominant-baseline", "middle");
    } else if (side === "right") {
      text.setAttribute("x", x + NODE_W + 10 + iconOffset);
      text.setAttribute("y", centerY);
      text.setAttribute("text-anchor", "start");
      text.setAttribute("dominant-baseline", "middle");
    } else {
      text.setAttribute("x", x + NODE_W / 2);
      text.setAttribute("y", node.y - 6);
      text.setAttribute("text-anchor", "middle");
    }
    text.textContent = displayLabel;
    labelLayer.appendChild(text);
  }
}

function addColumnHeader(layer, x, text) {
  const t = svgEl("text", {
    x,
    y: PLOT_TOP - 22,
    "text-anchor": "middle",
    class: "sankey-col-header",
  });
  t.textContent = text;
  layer.appendChild(t);
}

function renderSankeySection({ svg, data, height, sectionLabel, onNodeActivate, onLinkActivate }) {
  const plotHeight = height - PLOT_TOP - PLOT_BOTTOM;
  layoutColumn(data.milestoneNodes, data.total, PLOT_TOP, plotHeight, NODE_GAP);
  layoutColumn(data.workstreamNodes, data.total, PLOT_TOP, plotHeight, NODE_GAP);
  layoutColumn(data.statusNodes, data.total, PLOT_TOP, plotHeight, NODE_GAP);

  assignOutgoing(data.milestoneNodes, data.linksMS, "source");
  assignIncoming(data.workstreamNodes, data.linksMS, "target");
  assignOutgoing(data.workstreamNodes, data.linksRS, "source");
  assignIncoming(data.statusNodes, data.linksRS, "target");

  svg.innerHTML = "";
  svg.setAttribute("viewBox", `0 0 ${VIEW_W} ${height}`);
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", `${sectionLabel} Sankey diagram: milestone to workstream to status`);

  const linkLayer = svgEl("g", { class: "sankey-link-layer" });
  const nodeLayer = svgEl("g", { class: "sankey-node-layer" });
  const labelLayer = svgEl("g", { class: "sankey-label-layer" });
  svg.appendChild(linkLayer);
  svg.appendChild(nodeLayer);
  svg.appendChild(labelLayer);

  addColumnHeader(labelLayer, COL0_X + NODE_W / 2, "Milestone");
  addColumnHeader(labelLayer, COL1_X + NODE_W / 2, "Workstream");
  addColumnHeader(labelLayer, COL2_X + NODE_W / 2, "Status");

  drawLinks(linkLayer, data.linksMS, COL0_X, COL1_X, onLinkActivate);
  drawLinks(linkLayer, data.linksRS, COL1_X, COL2_X, onLinkActivate);

  drawNodes(nodeLayer, labelLayer, data.milestoneNodes, COL0_X, "left", onNodeActivate);
  drawNodes(nodeLayer, labelLayer, data.workstreamNodes, COL1_X, "middle", onNodeActivate);
  drawNodes(nodeLayer, labelLayer, data.statusNodes, COL2_X, "right", onNodeActivate);
}

/* ==========================================================================
   Detail side panel
   ========================================================================== */

let lastFocusedEl = null;

function renderPanelItem(item) {
  const metaMap = item._kind === "issue" ? ISSUE_STATUS_META : PR_STATUS_META;
  const meta = metaMap[item.status] || null;
  return `<li class="panel-item">
    <a href="${escapeHtml(item.url)}" target="_blank" rel="noopener">${escapeHtml(item.title)}</a>
    <div class="panel-item-meta">
      ${renderRepoTag(item.repo, item.workstream)}
      <span class="number-tag">#${item.number}</span>
      ${renderPill(meta)}
      <span class="age">${escapeHtml(relativeAge(item.updatedAt))}</span>
      ${item.milestone ? `<span class="milestone-tag">${escapeHtml(item.milestone)}</span>` : ""}
    </div>
  </li>`;
}

function openPanel(titleText, items) {
  lastFocusedEl = document.activeElement;
  const panel = document.getElementById("detail-panel");
  const backdrop = document.getElementById("detail-backdrop");

  document.getElementById("panel-title").textContent = titleText;
  const sorted = [...items].sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt));
  document.getElementById("panel-list").innerHTML = sorted.map(renderPanelItem).join("");
  document.getElementById("panel-count").textContent = `${sorted.length} item${sorted.length === 1 ? "" : "s"}`;

  panel.classList.add("open");
  backdrop.classList.add("open");
  panel.setAttribute("aria-hidden", "false");
  document.getElementById("panel-close").focus();
}

function closePanel() {
  const panel = document.getElementById("detail-panel");
  const backdrop = document.getElementById("detail-backdrop");
  panel.classList.remove("open");
  backdrop.classList.remove("open");
  panel.setAttribute("aria-hidden", "true");
  if (lastFocusedEl && typeof lastFocusedEl.focus === "function") lastFocusedEl.focus();
}

function initPanel() {
  document.getElementById("panel-close").addEventListener("click", closePanel);
  document.getElementById("detail-backdrop").addEventListener("click", closePanel);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && document.getElementById("detail-panel").classList.contains("open")) {
      closePanel();
    }
  });
}

function onNodeActivate(node, displayLabel) {
  openPanel(displayLabel, node.items);
}

function onLinkActivate(link) {
  openPanel(`${link.sourceLabel} → ${link.targetLabel}`, link.items);
}

/* ---------- workstream legend ---------- */

function renderLegend() {
  const el = document.getElementById("workstream-legend");
  el.innerHTML = WORKSTREAM_NODE_ORDER.map(
    (w) =>
      `<span class="repo-legend-item"><span class="repo-dot" style="background:${w.color}"></span>${escapeHtml(w.label)}</span>`
  ).join("");
}

/* ---------- theme toggle ---------- */

function initTheme() {
  const stored = localStorage.getItem("velero-workstream-theme");
  if (stored === "light" || stored === "dark") {
    document.documentElement.setAttribute("data-theme", stored);
  }
  const btn = document.getElementById("theme-toggle");
  btn.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const effectiveCurrent = current || (prefersDark ? "dark" : "light");
    const next = effectiveCurrent === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem("velero-workstream-theme", next);
    } catch (e) {
      /* storage unavailable; theme just won't persist */
    }
  });
}

/* ==========================================================================
   Filters: shared repo dropdown + per-section status chips
   ========================================================================== */

let allIssues = [];
let allPrs = [];
let selectedRepo = "";
const issuesDisabledStatuses = new Set();
const prsDisabledStatuses = new Set();

function populateRepoFilter() {
  const select = document.getElementById("repo-filter");
  const repos = Array.from(new Set([...allIssues, ...allPrs].map((it) => it.repo))).sort();
  for (const repo of repos) {
    const opt = document.createElement("option");
    opt.value = repo;
    opt.textContent = repo;
    select.appendChild(opt);
  }
  select.addEventListener("change", () => {
    selectedRepo = select.value;
    rerender();
  });
}

function repoFiltered(items) {
  return selectedRepo ? items.filter((it) => it.repo === selectedRepo) : items.slice();
}

/**
 * Renders one row of status-filter chips into `containerId`, populated from
 * whichever statuses are actually present in `items` (already repo-filtered,
 * but NOT yet status-filtered — so a toggled-off chip stays visible to be
 * re-enabled). Clicking a chip toggles its key in `disabledSet` and
 * triggers a full re-render.
 */
function renderStatusChips(containerId, items, statusOrder, statusMetaMap, disabledSet) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";
  for (const key of statusOrder) {
    const count = items.filter((it) => it.status === key).length;
    if (!count) continue;
    const meta = statusMetaMap[key] || { icon: "", label: key };
    const active = !disabledSet.has(key);
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "status-chip" + (active ? " active" : "");
    btn.setAttribute("aria-pressed", String(active));
    btn.innerHTML = `<span aria-hidden="true">${meta.icon}</span>${escapeHtml(meta.label)} <span class="status-chip-count">${count}</span>`;
    btn.addEventListener("click", () => {
      if (disabledSet.has(key)) disabledSet.delete(key);
      else disabledSet.add(key);
      rerender();
    });
    container.appendChild(btn);
  }
}

function renderSection({ sectionId, chipsId, svgId, items, statusOrder, statusMetaMap, disabledSet, recognizedMilestones, height, sectionLabel }) {
  const section = document.getElementById(sectionId);
  const repoScoped = repoFiltered(items);
  renderStatusChips(chipsId, repoScoped, statusOrder, statusMetaMap, disabledSet);

  const finalItems = repoScoped.filter((it) => !disabledSet.has(it.status));
  const svg = document.getElementById(svgId);
  const noMatchEl = document.getElementById(svgId.replace("-sankey", "-no-match"));

  if (!finalItems.length) {
    svg.innerHTML = "";
    svg.removeAttribute("viewBox");
    if (noMatchEl) noMatchEl.hidden = false;
    return;
  }
  if (noMatchEl) noMatchEl.hidden = true;

  const data = buildSankeyData(finalItems, recognizedMilestones, statusOrder, statusMetaMap);
  renderSankeySection({ svg, data, height, sectionLabel, onNodeActivate, onLinkActivate });
}

let recognizedMilestonesGlobal = [];

function rerender() {
  if (allIssues.length) {
    renderSection({
      sectionId: "issues-section",
      chipsId: "issues-status-chips",
      svgId: "issues-sankey",
      items: allIssues,
      statusOrder: ISSUE_STATUS_ORDER,
      statusMetaMap: ISSUE_STATUS_META,
      disabledSet: issuesDisabledStatuses,
      recognizedMilestones: recognizedMilestonesGlobal,
      height: 460,
      sectionLabel: "Issues",
    });
  }
  if (allPrs.length) {
    renderSection({
      sectionId: "prs-section",
      chipsId: "prs-status-chips",
      svgId: "prs-sankey",
      items: allPrs,
      statusOrder: PR_STATUS_ORDER,
      statusMetaMap: PR_STATUS_META,
      disabledSet: prsDisabledStatuses,
      recognizedMilestones: recognizedMilestonesGlobal,
      height: 520,
      sectionLabel: "PRs",
    });
  }
}

/* ---------- boot ---------- */

async function fetchJson(path) {
  const res = await fetch(path, { cache: "no-store" });
  if (!res.ok) throw new Error(`${path} responded ${res.status}`);
  return res.json();
}

async function main() {
  initTheme();
  initPanel();
  renderLegend();

  let issuesData, prsData;
  try {
    [issuesData, prsData] = await Promise.all([
      fetchJson("../workstream-issues.json"),
      fetchJson("../workstream-prs.json"),
    ]);
  } catch (err) {
    const errEl = document.getElementById("load-error");
    errEl.hidden = false;
    errEl.textContent =
      "Couldn't load workstream data yet (workstream-issues.json / workstream-prs.json missing or unreadable). " +
      "The data-fetch workflow may not have run yet. Try again in a bit.";
    return;
  }

  allIssues = (issuesData.issues || []).map((i) => ({ ...i, _kind: "issue" }));
  allPrs = (prsData.prs || []).map((p) => ({ ...p, _kind: "pr" }));
  recognizedMilestonesGlobal = issuesData.recognizedMilestones || prsData.recognizedMilestones || [];

  if (!allIssues.length && !allPrs.length) {
    document.getElementById("empty-state").hidden = false;
    updateFreshness(issuesData.updatedAt || prsData.updatedAt);
    return;
  }

  populateRepoFilter();

  if (allIssues.length) document.getElementById("issues-section").hidden = false;
  if (allPrs.length) document.getElementById("prs-section").hidden = false;

  rerender();

  updateFreshness(issuesData.updatedAt || prsData.updatedAt);
}

function updateFreshness(isoString) {
  const el = document.getElementById("freshness");
  if (!isoString) {
    el.textContent = "";
    return;
  }
  el.textContent = `data as of ${relativeAge(isoString)}`;
  el.title = new Date(isoString).toLocaleString();
}

main();
