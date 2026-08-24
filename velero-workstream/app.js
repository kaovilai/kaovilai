"use strict";

/* ==========================================================================
   Velero Workstream Dashboard — vanilla JS, no build step, no deps.
   ========================================================================== */

const REPO_COLORS = {
  "velero-io/velero": { color: "var(--repo-velero)", label: "velero" },
  "velero-io/velero-plugin-for-aws": { color: "var(--repo-aws)", label: "aws" },
  "velero-io/velero-plugin-for-gcp": { color: "var(--repo-gcp)", label: "gcp" },
  "velero-io/velero-plugin-for-microsoft-azure": { color: "var(--repo-azure)", label: "azure" },
  "openshift/openshift-velero-plugin": { color: "var(--repo-other)", label: "openshift-plugin" },
};

const DEFAULT_REPO = { color: "var(--repo-other)", label: null };

const PR_STATUS_META = {
  ready: { pill: "good", icon: "✅", label: "ready" },
  "waiting-merge": { pill: "warning", icon: "⏳", label: "waiting merge" },
  hold: { pill: "warning", icon: "✋", label: "hold" },
  "failing-ci": { pill: "critical", icon: "❌", label: "failing CI" },
  draft: { pill: "neutral", icon: "📝", label: "draft" },
  stale: { pill: "neutral", icon: "🕸️", label: "stale" },
};

const ISSUE_STATUS_META = {
  open: null,
  stale: { pill: "neutral", icon: "🕸️", label: "stale" },
};

function repoMeta(repo) {
  return REPO_COLORS[repo] || { ...DEFAULT_REPO, label: shortRepoLabel(repo) };
}

function shortRepoLabel(repo) {
  const parts = repo.split("/");
  return parts[parts.length - 1] || repo;
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

/**
 * Buckets items into the four fixed groups per the milestone contract,
 * omitting empty buckets. `recognizedMilestones[0]` is current release,
 * `[1]` (if present) is next release.
 */
function bucketize(items, recognizedMilestones) {
  const current = recognizedMilestones[0];
  const next = recognizedMilestones[1];
  const buckets = {
    current: { key: "current", label: current ? `🚀 ${current} · current release` : null, items: [], isCurrentRelease: true },
    next: { key: "next", label: next ? `🔭 ${next} · next release` : null, items: [] },
    other: { key: "other", label: "📌 other milestone", items: [] },
    none: { key: "none", label: "◌ no milestone", items: [] },
  };

  for (const item of items) {
    const m = item.milestone;
    if (m && m === current) {
      buckets.current.items.push(item);
    } else if (m && next && m === next) {
      buckets.next.items.push(item);
    } else if (m) {
      buckets.other.items.push(item);
    } else {
      buckets.none.items.push(item);
    }
  }

  for (const bucket of Object.values(buckets)) {
    bucket.items.sort((a, b) => new Date(a.updatedAt) - new Date(b.updatedAt));
  }

  return [buckets.current, buckets.next, buckets.other, buckets.none].filter(
    (b) => b.items.length > 0
  );
}

function renderRepoTag(repo) {
  const meta = repoMeta(repo);
  return `<span class="repo-tag">
    <span class="repo-dot" style="background:${meta.color}" aria-hidden="true"></span>
    <span>${escapeHtml(meta.label)}</span>
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

function renderIssueCard(issue) {
  const meta = ISSUE_STATUS_META[issue.status] || null;
  const cardId = cardIdFor(issue.repo, issue.number);
  const showMilestoneNote = issue._bucketKey === "other" && issue.milestone;
  return `<a class="card" id="${cardId}" href="${escapeHtml(issue.url)}" target="_blank" rel="noopener"
      title="${escapeHtml(issue.title)}" data-repo="${escapeHtml(issue.repo)}" data-number="${issue.number}">
    <p class="card-title">${escapeHtml(issue.title)}</p>
    <div class="card-meta-row">
      ${renderRepoTag(issue.repo)}
      <span class="number-tag">#${issue.number}</span>
      ${renderPill(meta)}
      <span class="age">${escapeHtml(relativeAge(issue.updatedAt))}</span>
      ${showMilestoneNote ? `<span class="milestone-tag">${escapeHtml(issue.milestone)}</span>` : ""}
    </div>
  </a>`;
}

function renderPrCard(pr) {
  const meta = PR_STATUS_META[pr.status] || null;
  const cardId = cardIdFor(pr.repo, pr.number);
  const showMilestoneNote = pr._bucketKey === "other" && pr.milestone;
  const isBlockedOnReview = pr.status === "waiting-merge";
  return `<a class="card${isBlockedOnReview ? " is-blocked" : ""}" id="${cardId}" href="${escapeHtml(pr.url)}" target="_blank" rel="noopener"
      title="${escapeHtml(pr.title)}" data-repo="${escapeHtml(pr.repo)}" data-number="${pr.number}">
    <p class="card-title">${escapeHtml(pr.title)}</p>
    <div class="card-meta-row">
      ${renderRepoTag(pr.repo)}
      <span class="number-tag">#${pr.number}</span>
      ${renderPill(meta)}
      <span class="age">${escapeHtml(relativeAge(pr.updatedAt))}</span>
      ${showMilestoneNote ? `<span class="milestone-tag">${escapeHtml(pr.milestone)}</span>` : ""}
      ${isBlockedOnReview ? renderBlockedGraphic() : ""}
    </div>
  </a>`;
}

function cardIdFor(repo, number) {
  return `card--${repo.replace(/[^a-zA-Z0-9]/g, "-")}--${number}`;
}

function renderGroups(containerEl, buckets, cardRenderer, sectionKind) {
  containerEl.innerHTML = "";
  for (const bucket of buckets) {
    const groupEl = document.createElement("div");
    groupEl.className = "group" + (bucket.isCurrentRelease ? " is-current-release" : "");

    const labelEl = document.createElement("p");
    labelEl.className = "group-label";
    labelEl.innerHTML = `${bucket.label} <span class="group-count">(${bucket.items.length})</span>`;
    groupEl.appendChild(labelEl);

    const gridEl = document.createElement("div");
    gridEl.className = "card-grid";
    for (const item of bucket.items) {
      item._bucketKey = bucket.key;
    }
    gridEl.innerHTML = bucket.items.map(cardRenderer).join("");
    groupEl.appendChild(gridEl);

    containerEl.appendChild(groupEl);
  }
}

/* ---------- arrows ---------- */

function computeArrowPairs(prs, issues) {
  const issueByKey = new Map();
  for (const issue of issues) {
    issueByKey.set(`${issue.repo}#${issue.number}`, issue);
  }

  const pairs = [];
  for (const pr of prs) {
    const refs = pr.closingIssuesReferences || [];
    for (const ref of refs) {
      const key = `${ref.repo}#${ref.number}`;
      if (issueByKey.has(key)) {
        pairs.push({ pr, issue: issueByKey.get(key) });
      }
    }
  }
  return pairs;
}

function isClippedByLane(el) {
  const lane = el.closest(".card-grid");
  if (!lane) return false;
  const laneRect = lane.getBoundingClientRect();
  const elRect = el.getBoundingClientRect();
  return elRect.right <= laneRect.left || elRect.left >= laneRect.right;
}

/* Quadratic bezier point + tangent at parameter t (0..1). */
function quadPoint(x0, y0, cx, cy, x1, y1, t) {
  const mt = 1 - t;
  const x = mt * mt * x0 + 2 * mt * t * cx + t * t * x1;
  const y = mt * mt * y0 + 2 * mt * t * cy + t * t * y1;
  const tx = 2 * mt * (cx - x0) + 2 * t * (x1 - cx);
  const ty = 2 * mt * (cy - y0) + 2 * t * (y1 - cy);
  return { x, y, tx, ty };
}

/**
 * Builds a Sankey-style flow ribbon: a filled band that follows the same
 * bow-curve as before, tapering to a point at each card (width ~ sin(pi*t))
 * rather than a thin stroked line. Returns an SVG path `d` string.
 */
function ribbonPath(x0, y0, cx, cy, x1, y1, maxWidth, steps = 20) {
  const top = [];
  const bottom = [];
  for (let i = 0; i <= steps; i++) {
    const t = i / steps;
    const { x, y, tx, ty } = quadPoint(x0, y0, cx, cy, x1, y1, t);
    const tlen = Math.sqrt(tx * tx + ty * ty) || 1;
    const nx = -ty / tlen;
    const ny = tx / tlen;
    const w = (maxWidth / 2) * Math.sin(Math.PI * t);
    top.push(`${x + nx * w} ${y + ny * w}`);
    bottom.push(`${x - nx * w} ${y - ny * w}`);
  }
  const d =
    `M ${top[0]} ` +
    top.slice(1).map((p) => `L ${p}`).join(" ") +
    " " +
    bottom.slice().reverse().map((p) => `L ${p}`).join(" ") +
    " Z";
  return d;
}

function drawArrows(pairs) {
  const svg = document.getElementById("arrow-overlay");
  const appEl = document.getElementById("app");
  svg.innerHTML = "";

  if (!pairs.length) return;

  const appRect = appEl.getBoundingClientRect();
  const scrollX = window.scrollX || window.pageXOffset;
  const scrollY = window.scrollY || window.pageYOffset;

  let drawn = 0;
  for (const { pr, issue } of pairs) {
    const prEl = document.getElementById(cardIdFor(pr.repo, pr.number));
    const issueEl = document.getElementById(cardIdFor(issue.repo, issue.number));
    if (!prEl || !issueEl) continue;
    if (isClippedByLane(prEl) || isClippedByLane(issueEl)) continue;

    const a = prEl.getBoundingClientRect();
    const b = issueEl.getBoundingClientRect();

    const x1 = a.left + a.width / 2 + scrollX - (appRect.left + scrollX);
    const y1 = a.top + a.height / 2 + scrollY - (appRect.top + scrollY);
    const x2 = b.left + b.width / 2 + scrollX - (appRect.left + scrollX);
    const y2 = b.top + b.height / 2 + scrollY - (appRect.top + scrollY);

    const midX = (x1 + x2) / 2;
    const midY = (y1 + y2) / 2;
    const dx = x2 - x1;
    const dy = y2 - y1;
    const dist = Math.sqrt(dx * dx + dy * dy) || 1;
    const curveAmount = Math.min(dist * 0.2, 60);
    const nx = -dy / dist;
    const ny = dx / dist;
    const ctrlX = midX + nx * curveAmount;
    const ctrlY = midY + ny * curveAmount;

    const flowColor = repoMeta(pr.repo).color;

    const ribbon = document.createElementNS("http://www.w3.org/2000/svg", "path");
    ribbon.setAttribute("d", ribbonPath(x1, y1, ctrlX, ctrlY, x2, y2, 26));
    ribbon.setAttribute("fill", flowColor);
    ribbon.setAttribute("fill-opacity", "0.32");
    svg.appendChild(ribbon);

    // small directional arrowhead where the flow meets the issue card
    const tip = quadPoint(x1, y1, ctrlX, ctrlY, x2, y2, 0.94);
    const end = quadPoint(x1, y1, ctrlX, ctrlY, x2, y2, 1);
    const tlen = Math.sqrt(tip.tx * tip.tx + tip.ty * tip.ty) || 1;
    const ux = tip.tx / tlen;
    const uy = tip.ty / tlen;
    const nxp = -uy;
    const nyp = ux;
    const headLen = 11;
    const headHalfWidth = 8;
    const baseX = end.x - ux * headLen;
    const baseY = end.y - uy * headLen;
    const head = document.createElementNS("http://www.w3.org/2000/svg", "path");
    head.setAttribute(
      "d",
      `M ${end.x} ${end.y} L ${baseX + nxp * headHalfWidth} ${baseY + nyp * headHalfWidth} L ${baseX - nxp * headHalfWidth} ${baseY - nyp * headHalfWidth} Z`
    );
    head.setAttribute("fill", flowColor);
    head.setAttribute("fill-opacity", "0.75");
    svg.appendChild(head);

    drawn++;
  }

  svg.style.width = `${appRect.width}px`;
  svg.style.height = `${appEl.scrollHeight}px`;
}


function debounce(fn, wait) {
  let t = null;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), wait);
  };
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

/* ---------- boot ---------- */

async function fetchJson(path) {
  const res = await fetch(path, { cache: "no-store" });
  if (!res.ok) throw new Error(`${path} responded ${res.status}`);
  return res.json();
}

async function main() {
  initTheme();

  let issuesData, prsData;
  try {
    [issuesData, prsData] = await Promise.all([
      fetchJson("../velero-open-issues.json"),
      fetchJson("../velero-open-prs.json"),
    ]);
  } catch (err) {
    const errEl = document.getElementById("load-error");
    errEl.hidden = false;
    errEl.textContent =
      "Couldn't load workstream data yet (velero-open-issues.json / velero-open-prs.json missing or unreadable). " +
      "The data-fetch workflow may not have run yet. Try again in a bit.";
    return;
  }

  const issues = issuesData.issues || [];
  const prs = prsData.prs || [];
  const recognizedMilestones = issuesData.recognizedMilestones || prsData.recognizedMilestones || [];

  if (!issues.length && !prs.length) {
    document.getElementById("empty-state").hidden = false;
    updateFreshness(issuesData.updatedAt || prsData.updatedAt);
    return;
  }

  const issuesSection = document.getElementById("issues-section");
  const prsSection = document.getElementById("prs-section");

  if (issues.length) {
    issuesSection.hidden = false;
    const issueBuckets = bucketize(issues, recognizedMilestones);
    renderGroups(document.getElementById("issues-groups"), issueBuckets, renderIssueCard, "issues");
  }

  if (prs.length) {
    prsSection.hidden = false;
    const prBuckets = bucketize(prs, recognizedMilestones);
    renderGroups(document.getElementById("prs-groups"), prBuckets, renderPrCard, "prs");
  }

  updateFreshness(issuesData.updatedAt || prsData.updatedAt);

  const pairs = computeArrowPairs(prs, issues);
  const redraw = () => drawArrows(pairs);

  const lanes = document.querySelectorAll(".card-grid");
  for (const lane of lanes) {
    lane.scrollLeft = lane.scrollWidth;
    lane.addEventListener("scroll", debounce(redraw, 80), { passive: true });
  }

  requestAnimationFrame(redraw);
  window.addEventListener("resize", debounce(redraw, 120));
  window.addEventListener("scroll", debounce(redraw, 120), { passive: true });
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
