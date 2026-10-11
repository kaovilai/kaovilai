(function () {
  "use strict";

  const PX_PER_DAY_MIN = 1;
  const PX_PER_DAY_MAX = 4000;
  const DEFAULT_LANES = ["Velero", "OADP", "KubeVirt Data Mover", "Kubernetes", "CNCF Landscape", "Uncategorized"];
  const LANE_COLOR_VAR = {
    "Velero": "--lane-velero",
    "OADP": "--lane-oadp",
    "KubeVirt Data Mover": "--lane-datamover",
    "Kubernetes": "--lane-kubernetes",
    "CNCF Landscape": "--lane-cncf",
    "Uncategorized": "--lane-uncategorized",
  };

  const STATUS_META = {
    "ready": { colorVar: "--status-good", icon: "●", label: "Ready" },
    "waiting-merge": { colorVar: "--status-good", icon: "●", label: "Waiting to merge" },
    "ci-pending": { colorVar: "--status-warning", icon: "▲", label: "CI pending" },
    "needs-attention": { colorVar: "--status-warning", icon: "▲", label: "Needs attention" },
    "hold": { colorVar: "--status-critical", icon: "✕", label: "On hold" },
    "failing-ci": { colorVar: "--status-critical", icon: "✕", label: "Failing CI" },
    "draft": { colorVar: "--status-neutral", icon: "■", label: "Draft", parked: true },
    "stale": { colorVar: "--status-neutral", icon: "■", label: "Stale", parked: true },
    "open": { colorVar: "--status-good", icon: "●", label: "Open" },
    "merged": { colorVar: "--status-merged", icon: "◆", label: "Merged" },
    "closed": { colorVar: "--status-neutral", icon: "■", label: "Closed", parked: true },
    "reviewed": { colorVar: "--status-good", icon: "●", label: "Reviewed" },
    "commented": { colorVar: "--status-good", icon: "●", label: "Commented" },
  };
  const UNKNOWN_STATUS = { colorVar: "--status-neutral", icon: "■", label: "Unknown", parked: true };

  const state = {
    items: [],
    classification: {},
    layout: { laneOrder: DEFAULT_LANES.slice(), pinned: {} },
    pendingClassification: {},
    pendingLayout: null,
    serverOnline: false,
    saveToken: "",
    pxPerDay: 8,
  };

  async function fetchJson(path) {
    try {
      const res = await fetch(path, { cache: "no-store" });
      if (!res.ok) return null;
      return await res.json();
    } catch (e) {
      return null;
    }
  }

  function daysAgo(iso) {
    const d = new Date(iso).getTime();
    if (Number.isNaN(d)) return null;
    return (Date.now() - d) / 86400000;
  }

  function fmtAge(days) {
    if (days === null) return "";
    if (days < 1) return "today";
    if (days < 2) return "1d";
    if (days < 60) return Math.floor(days) + "d";
    if (days < 730) return Math.floor(days / 30) + "mo";
    return (days / 365).toFixed(1) + "y";
  }

  function ciSummary(ciChecks) {
    if (!ciChecks || !ciChecks.length) return null;
    const norm = (c) => (c.conclusion || "").toUpperCase();
    if (ciChecks.some((c) => ["FAILURE", "ERROR", "CANCELLED", "TIMED_OUT"].includes(norm(c)))) {
      return { colorVar: "--status-critical", icon: "✕", label: "CI failing" };
    }
    if (ciChecks.some((c) => ["IN_PROGRESS", "QUEUED", "PENDING", ""].includes(norm(c)))) {
      return { colorVar: "--status-warning", icon: "▲", label: "CI pending" };
    }
    return { colorVar: "--status-good", icon: "●", label: "CI passing" };
  }

  async function loadAll() {
    const [prsData, issuesData, activityData, archiveData, classData, layoutData] = await Promise.all([
      fetchJson("../open-prs.json"),
      fetchJson("../open-issues.json"),
      fetchJson("../activity.json"),
      fetchJson("../workstream-archive.json"),
      fetchJson("../workstream-classification.json"),
      fetchJson("../workstream-layout.json"),
    ]);

    state.classification = classData || {};
    if (layoutData && Array.isArray(layoutData.laneOrder)) {
      state.layout = layoutData;
    }

    // merge in any not-yet-published edits saved locally from a session without a server
    try {
      const local = JSON.parse(localStorage.getItem("workstream-pending") || "null");
      if (local) {
        Object.assign(state.pendingClassification, local.classification || {});
        if (local.layout) state.pendingLayout = local.layout;
      }
    } catch (e) { /* ignore corrupt local state */ }

    const items = [];
    const seenKeys = new Set();

    if (prsData && Array.isArray(prsData.prs)) {
      for (const p of prsData.prs) {
        const key = p.repo + "#" + p.number;
        seenKeys.add(key);
        items.push({
          key, repo: p.repo, org: p.org, number: p.number, title: p.title, url: p.url,
          date: p.updatedAt, kind: "pr", status: p.status, workstreamDefault: p.workstream,
          ciChecks: p.ciChecks || [], isDraft: p.isDraft,
        });
      }
      setFreshness(prsData.updatedAt);
    }

    if (issuesData && Array.isArray(issuesData.issues)) {
      for (const i of issuesData.issues) {
        const key = i.repo + "#" + i.number;
        seenKeys.add(key);
        items.push({
          key, repo: i.repo, org: i.org, number: i.number, title: i.title, url: i.url,
          date: i.updatedAt, kind: "issue", status: i.status, workstreamDefault: i.workstream, ciChecks: [],
        });
      }
    }

    if (archiveData && Array.isArray(archiveData.items)) {
      for (const a of archiveData.items) {
        const key = a.repo + "#" + a.number;
        if (seenKeys.has(key)) continue; // still live/open elsewhere, don't double-render
        items.push({
          key, repo: a.repo, org: a.org, number: a.number, title: a.title, url: a.url,
          date: a.updatedAt, kind: a.type, status: a.state, workstreamDefault: a.workstream, ciChecks: [],
          archived: true,
        });
      }
    }

    if (activityData) {
      for (const cat of ["prsReviewed", "issuesCommented"]) {
        const list = activityData[cat];
        if (!Array.isArray(list)) continue;
        const status = cat === "prsReviewed" ? "reviewed" : "commented";
        for (const a of list) {
          items.push({
            key: "activity:" + status + ":" + a.repo + "#" + a.number,
            repo: a.repo, org: a.org, number: a.number, title: a.title, url: a.url,
            date: a.date, kind: "activity", status, workstreamDefault: a.workstream, ciChecks: [],
            isActivity: true,
          });
        }
      }
    }

    state.items = items.filter((it) => it.date);
    render();
  }

  function setFreshness(updatedAt) {
    const el = document.getElementById("freshness");
    if (!updatedAt) { el.textContent = "No data yet — run workstream/refresh-data.sh"; return; }
    const mins = Math.round((Date.now() - new Date(updatedAt).getTime()) / 60000);
    const ago = mins < 60 ? mins + "m ago" : Math.round(mins / 60) + "h ago";
    el.textContent = "PR/CI status as of " + ago + " (hourly on weekday active hours, ~6h off-hours/weekends — see update-pr-badges.yml, or run workstream/refresh-data.sh)";
  }

  function resolveWorkstream(item) {
    const override = state.pendingClassification[item.key] || state.classification[item.key]
      || state.pendingClassification[item.repo] || state.classification[item.repo];
    if (override && override.workstream) {
      return { name: override.workstream, source: override.source || "manual", note: override.note || "" };
    }
    return { name: item.workstreamDefault || "Uncategorized", source: "default", note: "" };
  }

  function laneColorVar(name) {
    return LANE_COLOR_VAR[name] || "--lane-uncategorized";
  }

  function effectiveLayout() {
    return state.pendingLayout || state.layout;
  }

  function buildLegend() {
    const seen = new Map();
    for (const key of ["ready", "ci-pending", "hold", "draft", "closed", "merged"]) {
      const m = STATUS_META[key];
      if (!seen.has(m.label)) seen.set(m.label, m);
    }
    const legend = document.getElementById("legend");
    legend.innerHTML = "";
    for (const m of seen.values()) {
      const span = document.createElement("span");
      span.className = "legend-item";
      span.innerHTML = `<span style="color:var(${m.colorVar})">${m.icon}</span> ${m.label}`;
      legend.appendChild(span);
    }
  }

  function render() {
    buildLegend();

    const layout = effectiveLayout();
    const grouped = {};
    for (const item of state.items) {
      const ws = resolveWorkstream(item);
      item._resolved = ws;
      (grouped[ws.name] = grouped[ws.name] || []).push(item);
    }

    const laneNames = layout.laneOrder.slice();
    for (const name of Object.keys(grouped)) {
      if (!laneNames.includes(name)) laneNames.push(name);
    }

    for (const name of laneNames) {
      const list = grouped[name] || [];
      const pinned = (layout.pinned && layout.pinned[name]) || [];
      if (pinned.length) {
        const byKey = new Map(list.map((it) => [it.key, it]));
        const ordered = [];
        for (const k of pinned) { if (byKey.has(k)) { ordered.push(byKey.get(k)); byKey.delete(k); } }
        const rest = Array.from(byKey.values()).sort((a, b) => new Date(b.date) - new Date(a.date));
        grouped[name] = ordered.concat(rest);
      } else {
        list.sort((a, b) => new Date(b.date) - new Date(a.date));
      }
    }

    const cols = "100px " + laneNames.map(() => "minmax(230px, 1fr)").join(" ");

    const header = document.getElementById("lanes-header");
    header.style.gridTemplateColumns = cols;
    header.innerHTML = "<div class=\"ruler-title\">Time</div>" + laneNames.map((name) =>
      `<div class="lane-title"><span class="lane-swatch" style="background:var(${laneColorVar(name)})"></span>${escapeHtml(name)} (${(grouped[name] || []).length})</div>`
    ).join("");

    const timeline = document.getElementById("timeline");
    timeline.style.gridTemplateColumns = cols;
    timeline.innerHTML = "";

    const ruler = document.createElement("div");
    ruler.className = "ruler";
    timeline.appendChild(ruler);

    // Flat list of {item, card, connector} so zoom (relayout) can reposition
    // everything cheaply — recomputing top/height only — without rebuilding
    // ~thousands of DOM nodes and re-attaching listeners on every wheel tick.
    state.renderedEntries = [];

    for (const name of laneNames) {
      const laneEl = document.createElement("div");
      laneEl.className = "lane";
      laneEl.dataset.lane = name;
      laneEl.addEventListener("dragover", (e) => e.preventDefault());
      laneEl.addEventListener("drop", (e) => onDrop(e, name));

      const cardEls = [];

      for (const item of grouped[name] || []) {
        const meta = STATUS_META[item.status] || UNKNOWN_STATUS;
        const connector = document.createElement("div");
        connector.className = "connector";
        connector.style.left = "18px";
        connector.style.background = `var(${meta.colorVar})`;
        laneEl.appendChild(connector);

        const card = document.createElement("div");
        card.className = "card" + (meta.parked ? " parked" : "");
        card.draggable = !item.isActivity;
        card.dataset.key = item.key;
        card.dataset.lane = name;

        const ci = ciSummary(item.ciChecks);
        const overrideNote = (state.pendingClassification[item.key] || state.classification[item.key] || {}).note;

        card.innerHTML = `
          <span class="card-title">${escapeHtml(item.title)}</span>
          <div class="card-meta">
            <span class="status-pill" style="color:var(${meta.colorVar})">${meta.icon} ${meta.label}</span>
            <span>${escapeHtml(item.repo)}#${item.number}</span>
            <span class="age"></span>
            ${ci ? `<span class="ci-pill" style="color:var(${ci.colorVar})">${ci.icon} ${ci.label}</span>` : ""}
            ${overrideNote ? `<span class="note-flag" title="${escapeHtml(overrideNote)}">\u{1F4DD}</span>` : ""}
          </div>`;

        card.addEventListener("click", () => openPanel(item));
        card.addEventListener("dragstart", (e) => {
          e.dataTransfer.setData("text/plain", item.key);
        });
        const idx = cardEls.length;
        card.addEventListener("mouseenter", () => dockFocus(cardEls, idx));
        card.addEventListener("mouseleave", () => dockReset(cardEls));
        laneEl.appendChild(card);
        cardEls.push(card);
        state.renderedEntries.push({ item, card, connector, ageEl: card.querySelector(".age") });
      }

      timeline.appendChild(laneEl);
    }

    relayout();
  }

  // Cheap zoom-time update: recompute pixel positions on the already-built DOM
  // (state.renderedEntries) without touching classification/grouping/listeners.
  // This is what makes pinch/ctrl+scroll zoom smooth — render() rebuilds
  // thousands of nodes and is only needed when data or classification changes.
  function relayout() {
    let maxDays = 30;
    for (const item of state.items) {
      const d = daysAgo(item.date);
      if (d !== null && d > maxDays) maxDays = d;
    }
    const heightPx = Math.ceil(maxDays * state.pxPerDay) + 80;

    const timeline = document.getElementById("timeline");
    timeline.style.height = heightPx + "px";
    for (const lane of timeline.querySelectorAll(".lane, .ruler")) {
      lane.style.height = heightPx + "px";
    }

    for (const entry of state.renderedEntries) {
      const days = daysAgo(entry.item.date) || 0;
      const top = Math.max(0, days * state.pxPerDay);
      entry.card.style.top = top + "px";
      entry.connector.style.height = top + "px";
      if (entry.ageEl) entry.ageEl.textContent = fmtAge(days) + (entry.item.isActivity ? "" : " idle");
    }

    const ruler = timeline.querySelector(".ruler");
    ruler.innerHTML = "";
    ruler.appendChild(rulerTick(0, "now", true));
    const scrollEl = document.querySelector(".timeline-scroll");
    buildRulerTicks(ruler, new Date(), heightPx, state.pxPerDay, scrollEl.scrollTop, scrollEl.scrollTop + scrollEl.clientHeight);
  }

  // macOS-dock-style magnify: the hovered card lifts and scales slightly; its
  // immediate time-neighbors in the same lane nudge aside to make room. The full
  // title is shown via a floating tooltip (never reflows the card itself) —
  // wrapping the title inline used to spill over neighboring cards' fixed
  // positions, since those don't move to make room for taller text.
  // Only nudge a neighbor if it's actually close on screen — with items sparse
  // (zoomed in, or big time gaps), "next in the lane's date order" can be
  // hundreds of pixels away, and shifting it there would look like unrelated
  // cards randomly jumping.
  const DOCK_NEIGHBOR_MAX_PX = 60;

  function cardTop(el) {
    return parseFloat(el.style.top) || 0;
  }

  function dockFocus(cardEls, idx) {
    setDockStyle(cardEls[idx], 0, 1.06, 60);
    showTooltip(cardEls[idx]);
    const anchorTop = cardTop(cardEls[idx]);
    const prev = cardEls[idx - 1];
    const next = cardEls[idx + 1];
    if (prev && Math.abs(cardTop(prev) - anchorTop) <= DOCK_NEIGHBOR_MAX_PX) setDockStyle(prev, -16, 1, 55);
    if (next && Math.abs(cardTop(next) - anchorTop) <= DOCK_NEIGHBOR_MAX_PX) setDockStyle(next, 16, 1, 55);
  }

  function dockReset(cardEls) {
    for (const el of cardEls) setDockStyle(el, 0, 1, "");
    hideTooltip();
  }

  function setDockStyle(el, shift, scale, z) {
    el.style.setProperty("--dock-shift", shift + "px");
    el.style.setProperty("--dock-scale", scale);
    el.style.zIndex = z;
    el.style.boxShadow = (shift || scale !== 1) ? "0 6px 20px rgba(0,0,0,0.35)" : "";
  }

  function showTooltip(cardEl) {
    const title = cardEl.querySelector(".card-title");
    if (!title) return;
    const tip = document.getElementById("hover-tooltip");
    tip.textContent = title.textContent;
    tip.classList.add("show");

    const rect = cardEl.getBoundingClientRect();
    const tipRect = tip.getBoundingClientRect();
    let left = Math.min(rect.left, window.innerWidth - tipRect.width - 8);
    left = Math.max(8, left);
    let top = rect.top - tipRect.height - 8;
    if (top < 4) top = rect.bottom + 8;
    tip.style.left = left + "px";
    tip.style.top = top + "px";
  }

  function hideTooltip() {
    document.getElementById("hover-tooltip").classList.remove("show");
  }

  // Adaptive ruler granularity: pick the finest step (minute → hour → day → week →
  // month → quarter → year) whose spacing on screen at the current zoom clears
  // MIN_TICK_PX, so zooming in reveals minutes/hours and zooming out collapses to
  // years, all on the same fixed px-per-day scale.
  const MIN_TICK_PX = 56;
  const SUB_MONTH_STEPS_MS = [
    60e3, 5 * 60e3, 15 * 60e3, 30 * 60e3,
    3600e3, 3 * 3600e3, 6 * 3600e3, 12 * 3600e3,
    86400e3, 2 * 86400e3, 7 * 86400e3,
  ];
  // Intl.DateTimeFormat construction is expensive to repeat — building one per
  // tick (potentially hundreds, at fine zoom) was a measured hotspot. Reuse.
  const FMT_DATETIME = new Intl.DateTimeFormat(undefined, { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" });
  const FMT_DATE = new Intl.DateTimeFormat(undefined, { weekday: "short", month: "short", day: "numeric" });
  const FMT_MONTH = new Intl.DateTimeFormat(undefined, { month: "short", year: "numeric" });

  function fmtTick(d, stepMs) {
    return stepMs < 86400e3 ? FMT_DATETIME.format(d) : FMT_DATE.format(d);
  }

  // Only build ticks near the visible scroll viewport (+ a buffer), not across
  // the entire timeline height — at fine zoom the full range can call for
  // thousands of ticks even though at most a few dozen are ever on screen at
  // once. This is what keeps zoom/scroll smooth regardless of total history depth.
  function buildRulerTicks(ruler, now, heightPx, pxPerDay, viewTop, viewBottom) {
    const buffer = Math.max(400, (viewBottom - viewTop) || 0);
    const rangeTop = Math.max(0, (viewTop ?? 0) - buffer);
    const rangeBottom = Math.min(heightPx, (viewBottom ?? heightPx) + buffer);

    const subStep = SUB_MONTH_STEPS_MS.find((ms) => (ms / 86400000) * pxPerDay >= MIN_TICK_PX);

    if (subStep) {
      const stepPx = (subStep / 86400000) * pxPerDay;
      const nowMs = Math.floor(now.getTime() / subStep) * subStep;
      const startN = Math.max(0, Math.floor(rangeTop / stepPx));
      for (let n = startN; n * stepPx <= rangeBottom; n++) {
        const top = n * stepPx;
        if (top > 0.5) ruler.appendChild(rulerTick(top, fmtTick(new Date(nowMs - n * subStep), subStep), false));
      }
      return;
    }

    // Month/quarter/year: calendar-aligned (variable-length units), not epoch-stepped.
    const monthPx = 30 * pxPerDay, quarterPx = 91 * pxPerDay;
    const unit = monthPx >= MIN_TICK_PX ? 1 : quarterPx >= MIN_TICK_PX ? 3 : 12;
    const approxStepPx = 30.44 * unit * pxPerDay;
    const startI = Math.max(1, Math.floor(rangeTop / approxStepPx));
    for (let i = startI; ; i++) {
      const d = new Date(now.getFullYear(), now.getMonth() - i * unit, 1);
      const days = (now - d) / 86400000;
      const top = days * pxPerDay;
      if (top > rangeBottom) break;
      if (top < rangeTop) continue;
      const label = unit === 12 ? String(d.getFullYear()) : FMT_MONTH.format(d);
      ruler.appendChild(rulerTick(top, label, false));
    }
  }

  function rulerTick(top, label, isNow) {
    const el = document.createElement("div");
    el.className = "ruler-tick" + (isNow ? " now" : "");
    el.style.top = top + "px";
    el.textContent = label;
    return el;
  }

  function onDrop(e, targetLane) {
    e.preventDefault();
    const key = e.dataTransfer.getData("text/plain");
    if (!key) return;
    const item = state.items.find((it) => it.key === key);
    if (!item) return;
    const sourceLane = item._resolved.name;

    if (sourceLane !== targetLane) {
      // cross-lane drop = reclassify
      setPendingClassification(key, targetLane, currentNote(key));
    } else {
      // same-lane drop = manual reorder (pin this lane's order)
      const laneEl = e.currentTarget;
      const order = Array.from(laneEl.querySelectorAll(".card")).map((c) => c.dataset.key);
      const withoutKey = order.filter((k) => k !== key);
      withoutKey.unshift(key);
      const layout = clonePendingLayout();
      layout.pinned[targetLane] = withoutKey;
      state.pendingLayout = layout;
      markDirty();
    }
    render();
  }

  function currentNote(key) {
    return (state.pendingClassification[key] || state.classification[key] || {}).note || "";
  }

  function clonePendingLayout() {
    const base = state.pendingLayout || state.layout;
    return { laneOrder: base.laneOrder.slice(), pinned: Object.assign({}, base.pinned) };
  }

  function setPendingClassification(key, workstream, note) {
    state.pendingClassification[key] = { workstream, source: "manual", note: note || "" };
    markDirty();
  }

  function markDirty() {
    const btn = document.getElementById("publish-btn");
    btn.disabled = false;
    btn.dataset.pending = "true";
    btn.textContent = "Save & Publish *";
    persistLocalFallback();
  }

  function persistLocalFallback() {
    localStorage.setItem("workstream-pending", JSON.stringify({
      classification: state.pendingClassification,
      layout: state.pendingLayout,
    }));
  }

  // ---- annotate panel ----
  let activeItem = null;

  function openPanel(item) {
    activeItem = item;
    document.getElementById("panel-title").textContent = item.title;
    document.getElementById("panel-meta").textContent = item.repo + "#" + item.number + " • " + (item.status || "");
    document.getElementById("panel-link").href = item.url;

    const laneOptions = document.getElementById("lane-options");
    laneOptions.innerHTML = effectiveLayout().laneOrder.map((n) => `<option value="${escapeHtml(n)}">`).join("");
    document.getElementById("panel-workstream").value = item._resolved.name;
    document.getElementById("panel-note").value = currentNote(item.key);

    const ciList = document.getElementById("panel-ci");
    ciList.innerHTML = (item.ciChecks || []).map((c) => {
      const conc = (c.conclusion || "").toUpperCase();
      const bad = ["FAILURE", "ERROR", "CANCELLED", "TIMED_OUT"].includes(conc);
      const pending = ["IN_PROGRESS", "QUEUED", "PENDING", ""].includes(conc);
      const color = bad ? "--status-critical" : pending ? "--status-warning" : "--status-good";
      const icon = bad ? "✕" : pending ? "▲" : "●";
      return `<li><span style="color:var(${color})">${icon}</span> ${escapeHtml(c.name)} — ${escapeHtml(c.conclusion || "pending")}</li>`;
    }).join("");

    document.getElementById("panel").classList.add("open");
  }

  function closePanel() {
    document.getElementById("panel").classList.remove("open");
    activeItem = null;
  }

  function applyPanel() {
    if (!activeItem) return;
    const workstream = document.getElementById("panel-workstream").value.trim() || "Uncategorized";
    const note = document.getElementById("panel-note").value.trim();
    setPendingClassification(activeItem.key, workstream, note);
    closePanel();
    render();
    showToast("Staged — click Save & Publish to write it out.");
  }

  // ---- server / publish ----
  async function checkServer() {
    try {
      const res = await fetch("/api/health", { cache: "no-store" });
      state.serverOnline = res.ok;
      // Only a same-origin read can see this token, which is what authorises /api/save.
      state.saveToken = res.ok ? (await res.json()).token || "" : "";
    } catch (e) {
      state.serverOnline = false;
    }
    const el = document.getElementById("server-state");
    el.dataset.online = String(state.serverOnline);
    el.textContent = state.serverOnline ? "local server: connected" : "local server: not running";
  }

  async function publish() {
    const mergedClassification = Object.assign({}, state.classification, state.pendingClassification);
    const mergedLayout = state.pendingLayout || state.layout;

    if (!state.serverOnline) {
      persistLocalFallback();
      showToast("No local server — staged edits kept in this browser only. Run workstream/serve.sh, then Save & Publish again.");
      return;
    }

    try {
      const res = await fetch("/api/save", {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-Workstream-Token": state.saveToken || "" },
        body: JSON.stringify({ classification: mergedClassification, layout: mergedLayout }),
      });
      const body = await res.json();
      if (!res.ok || !body.ok) throw new Error(body.error || "save failed");

      state.classification = mergedClassification;
      state.layout = mergedLayout;
      state.pendingClassification = {};
      state.pendingLayout = null;
      localStorage.removeItem("workstream-pending");

      const btn = document.getElementById("publish-btn");
      btn.disabled = true;
      btn.dataset.pending = "false";
      btn.textContent = "Save & Publish";

      showToast(body.committed ? "Saved & pushed (" + body.sha + ")" : "Saved — no changes to commit.");
    } catch (e) {
      showToast("Publish failed: " + e.message);
    }
  }

  let toastTimer = null;
  function showToast(msg) {
    const el = document.getElementById("toast");
    el.textContent = msg;
    el.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => el.classList.remove("show"), 4000);
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;",
    }[c]));
  }

  document.getElementById("panel-close").addEventListener("click", closePanel);
  document.getElementById("panel-apply").addEventListener("click", applyPanel);
  document.getElementById("publish-btn").addEventListener("click", publish);

  // ---- zoom (pinch-to-zoom / ctrl+scroll / touch pinch) — rescales pxPerDay,
  // keeping the date under the cursor/gesture anchored so zooming doesn't jump ----
  const scrollEl = document.querySelector(".timeline-scroll");

  // pxPerDay updates instantly (cheap arithmetic) on every wheel/touch event so no
  // zoom "steps" are lost, but the expensive part — relayout() + the scrollTop
  // anchor correction — is coalesced to at most once per animation frame via rAF.
  // Without this, a fast trackpad pinch fires far more than 60 events/sec, each
  // one previously triggering a full DOM rebuild (render()), which is what made
  // zooming feel laggy.
  let zoomRAF = null;
  let zoomAnchorDay = 0;
  let zoomAnchorOffset = 0;

  function requestZoom(clientY, factor) {
    const rect = scrollEl.getBoundingClientRect();
    if (zoomRAF === null) {
      // First event of a new batch: capture the calendar day under the cursor
      // before any change, so it stays fixed however many events land before
      // the next paint.
      zoomAnchorDay = (scrollEl.scrollTop + (clientY - rect.top)) / state.pxPerDay;
    }
    zoomAnchorOffset = clientY - rect.top;
    state.pxPerDay = Math.min(PX_PER_DAY_MAX, Math.max(PX_PER_DAY_MIN, state.pxPerDay * factor));

    if (zoomRAF === null) {
      zoomRAF = requestAnimationFrame(() => {
        zoomRAF = null;
        relayout();
        scrollEl.scrollTop = zoomAnchorDay * state.pxPerDay - zoomAnchorOffset;
      });
    }
  }

  scrollEl.addEventListener("wheel", (e) => {
    // Trackpad pinch-to-zoom is delivered by Chrome/Safari as a wheel event with ctrlKey set.
    if (!e.ctrlKey) return;
    e.preventDefault();
    const factor = Math.exp(-e.deltaY * 0.01);
    requestZoom(e.clientY, factor);
  }, { passive: false });

  let pinchStartDist = null;
  let pinchStartPxPerDay = null;
  scrollEl.addEventListener("touchstart", (e) => {
    if (e.touches.length !== 2) return;
    pinchStartDist = Math.hypot(
      e.touches[0].clientX - e.touches[1].clientX,
      e.touches[0].clientY - e.touches[1].clientY
    );
    pinchStartPxPerDay = state.pxPerDay;
  }, { passive: true });
  scrollEl.addEventListener("touchmove", (e) => {
    if (e.touches.length !== 2 || pinchStartDist === null) return;
    e.preventDefault();
    const dist = Math.hypot(
      e.touches[0].clientX - e.touches[1].clientX,
      e.touches[0].clientY - e.touches[1].clientY
    );
    const midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
    requestZoom(midY, (pinchStartPxPerDay * (dist / pinchStartDist)) / state.pxPerDay);
  }, { passive: false });
  scrollEl.addEventListener("touchend", () => { pinchStartDist = null; });

  // Ruler ticks are windowed to the visible viewport (see buildRulerTicks), so
  // plain scrolling — with no zoom change — still needs to regenerate them for
  // the newly-visible range. Cheap (only rebuilds the ruler column) and
  // rAF-throttled the same way zoom is.
  let scrollRAF = null;
  scrollEl.addEventListener("scroll", () => {
    if (scrollRAF !== null) return;
    scrollRAF = requestAnimationFrame(() => {
      scrollRAF = null;
      const ruler = document.querySelector(".ruler");
      if (!ruler) return;
      const heightPx = parseFloat(document.getElementById("timeline").style.height) || 0;
      ruler.innerHTML = "";
      ruler.appendChild(rulerTick(0, "now", true));
      buildRulerTicks(ruler, new Date(), heightPx, state.pxPerDay, scrollEl.scrollTop, scrollEl.scrollTop + scrollEl.clientHeight);
    });
  }, { passive: true });

  checkServer().then(loadAll);
  setInterval(checkServer, 15000);
})();
