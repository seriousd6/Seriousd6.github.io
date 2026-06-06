/* workshop.js — MKT Translation Workshop
 * Private tool at translation/workshop/index.html.
 *
 * Loading strategy: nothing is fetched upfront. Each phase bundle is loaded
 * on first selection and cached for the session. This keeps the initial paint
 * instant and avoids locking the browser with 11MB of synchronous JSON parsing.
 *
 *   phase1  → data/translation/phase1.json       (248 KB — top 200 NT Greek)
 *   phase2  → data/translation/phase2.json       (238 KB — top 200 OT Hebrew)
 *   phase5  → data/translation/phase5.json        (23 KB — contested terms)
 *   all-*   → data/translation/index-{lang}.json (2-3 MB — slim index, on demand)
 */
'use strict';

import { _resolve, initTheme } from './core.js';

/* ── URLs ──────────────────────────────────────────────────── */
const PHASE_URLS = {
  phase1:       _resolve('../../data/translation/phase1.json'),
  phase2:       _resolve('../../data/translation/phase2.json'),
  phase5:       _resolve('../../data/translation/phase5.json'),
  'all-greek':  _resolve('../../data/translation/index-greek.json'),
  'all-hebrew': _resolve('../../data/translation/index-hebrew.json'),
};

/* ── Totals (from seed script) ─────────────────────────────── */
const TOTAL_GREEK  = 5523;
const TOTAL_HEBREW = 8674;

/* ── localStorage keys ─────────────────────────────────────── */
const SK_DECISIONS = 'bsw_ws_decisions';
const SK_UI        = 'bsw_ws_ui';

/* ── Book order (full name → display abbreviation) ─────────── */
const BOOK_ORDER_OT = [
  ['genesis','Gen'],['exodus','Exod'],['leviticus','Lev'],['numbers','Num'],['deuteronomy','Deut'],
  ['joshua','Josh'],['judges','Judg'],['ruth','Ruth'],['1samuel','1Sam'],['2samuel','2Sam'],
  ['1kings','1Kgs'],['2kings','2Kgs'],['1chronicles','1Chr'],['2chronicles','2Chr'],
  ['ezra','Ezra'],['nehemiah','Neh'],['esther','Esth'],['job','Job'],['psalms','Ps'],
  ['proverbs','Prov'],['ecclesiastes','Eccl'],['songofsolomon','Song'],['isaiah','Isa'],
  ['jeremiah','Jer'],['lamentations','Lam'],['ezekiel','Ezek'],['daniel','Dan'],
  ['hosea','Hos'],['joel','Joel'],['amos','Amos'],['obadiah','Obad'],['jonah','Jonah'],
  ['micah','Mic'],['nahum','Nah'],['habakkuk','Hab'],['zephaniah','Zeph'],
  ['haggai','Hag'],['zechariah','Zech'],['malachi','Mal'],
];
const BOOK_ORDER_NT = [
  ['matthew','Matt'],['mark','Mark'],['luke','Luke'],['john','John'],['acts','Acts'],
  ['romans','Rom'],['1corinthians','1Cor'],['2corinthians','2Cor'],['galatians','Gal'],
  ['ephesians','Eph'],['philippians','Phil'],['colossians','Col'],['1thessalonians','1Th'],
  ['2thessalonians','2Th'],['1timothy','1Tim'],['2timothy','2Tim'],['titus','Tit'],
  ['philemon','Phm'],['hebrews','Heb'],['james','Jas'],['1peter','1Pet'],['2peter','2Pet'],
  ['1john','1Jn'],['2john','2Jn'],['3john','3Jn'],['jude','Jude'],['revelation','Rev'],
];

/* ── Phase definitions ─────────────────────────────────────── */
const PHASES = [
  { id: 'dashboard',  label: 'Dashboard',               icon: '📊' },
  { id: 'primer',     label: 'Language Primers',         icon: '📖' },
  { id: 'phase1',     label: 'Phase 1 — Top NT Greek',  icon: '①' },
  { id: 'phase2',     label: 'Phase 2 — Top OT Hebrew', icon: '②' },
  { id: 'phase5',     label: 'Contested Terms',          icon: '⚑' },
  { id: 'all-greek',  label: 'All Greek',                icon: '🔤' },
  { id: 'all-hebrew', label: 'All Hebrew',               icon: '🔤' },
];

/* ── Module state ──────────────────────────────────────────── */
const  _cache     = {};          // phaseId → {code: entry}
let    _decisions = {};          // localStorage overrides
let    _uiState   = { phase: 'dashboard', activeCode: null };
let    _queue     = [];          // code array for current phase
let    _filtered  = [];          // after search
let    _page      = 0;
const  PAGE_SIZE  = 80;

/* ── DOM refs ──────────────────────────────────────────────── */
let $nav, $queue, $count, $dossier, $search, $layout, $loading, $loadingText, $topbarStats;

/* ── Storage ───────────────────────────────────────────────── */
function _loadDecisions() {
  try { _decisions = JSON.parse(localStorage.getItem(SK_DECISIONS) || '{}'); } catch { _decisions = {}; }
}
function _saveDecisions() {
  try { localStorage.setItem(SK_DECISIONS, JSON.stringify(_decisions)); } catch(e) {}
}
function _loadUiState() {
  try {
    const s = JSON.parse(localStorage.getItem(SK_UI) || '{}');
    if (s.phase)      _uiState.phase      = s.phase;
    if (s.activeCode) _uiState.activeCode = s.activeCode;
  } catch {}
}
function _saveUiState() {
  try { localStorage.setItem(SK_UI, JSON.stringify(_uiState)); } catch {}
}

/* ── Phase loading ─────────────────────────────────────────── */
async function _loadPhase(phaseId) {
  if (_cache[phaseId]) return;
  const url = PHASE_URLS[phaseId];
  if (!url) return;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to load ${url}: ${res.status}`);
  _cache[phaseId] = await res.json();
}

/* ── Entry lookup ──────────────────────────────────────────── */
// Returns best available data for a code, merged with user decisions.
function _getEntry(code) {
  // Search all cached phase data for this code
  let src = null;
  for (const data of Object.values(_cache)) {
    if (data && data[code]) { src = data[code]; break; }
  }
  if (!src) return null;

  const dec = _decisions[code] || {};
  return {
    ...src,
    _code:        code,
    _lang:        code.startsWith('G') ? 'greek' : 'hebrew',
    _status:      dec.status       || src.status       || 'draft',
    _tiers:       dec.tiers        || src.tiers         || {},
    _notes:       dec.notes        || src.user_notes    || '',
    _decLog:      dec.log          || src.decision_log  || [],
    _bookFreq:    src.book_freq    || {},
    _bookDefaults: dec.book_defaults || {},
  };
}

/* ── Stats ─────────────────────────────────────────────────── */
function _stats() {
  let gConf = 0, hConf = 0, disputed = 0, locked = 0, deferred = 0;
  for (const [code, dec] of Object.entries(_decisions)) {
    const s = dec.status;
    if (!s || s === 'draft') continue;
    const done = s === 'confirmed' || s === 'override' || s === 'locked';
    if (code.startsWith('G') && done) gConf++;
    if (code.startsWith('H') && done) hConf++;
    if (s === 'disputed') disputed++;
    if (s === 'locked')   locked++;
    if (s === 'deferred') deferred++;
  }
  return { gConf, gTotal: TOTAL_GREEK, hConf, hTotal: TOTAL_HEBREW, disputed, locked, deferred };
}

function _phaseStats(phaseId) {
  const data = _cache[phaseId];
  if (!data) return { total: null, done: 0 };   // null = not yet loaded
  const codes = Object.keys(data);
  const done  = codes.filter(c => {
    const s = (_decisions[c] || {}).status;
    return s && s !== 'draft' && s !== 'deferred';
  }).length;
  return { total: codes.length, done };
}

/* ── Queue building ────────────────────────────────────────── */
function _buildQueue(phaseId) {
  const data = _cache[phaseId];
  if (!data) return [];
  const codes = Object.keys(data);

  if (phaseId === 'phase1' || phaseId === 'all-greek') {
    return codes.sort((a, b) => (data[b].nt_freq || 0) - (data[a].nt_freq || 0));
  }
  if (phaseId === 'phase2' || phaseId === 'all-hebrew') {
    return codes.sort((a, b) => (data[b].ot_freq || 0) - (data[a].ot_freq || 0));
  }
  if (phaseId === 'phase5') {
    return codes.sort((a, b) => (data[b].dispute_level || 0) - (data[a].dispute_level || 0));
  }
  return codes;
}

/* ── Nav ───────────────────────────────────────────────────── */
function _renderNav() {
  const st = _stats();
  let html = '';

  // Progress bars
  html += '<div class="ws-nav-progress">';
  const gPct = Math.round(st.gConf / st.gTotal * 100);
  const hPct = Math.round(st.hConf / st.hTotal * 100);
  html += `<div class="ws-prog-row">
    <div class="ws-prog-label"><span>Greek</span><strong>${st.gConf} / ${st.gTotal}</strong></div>
    <div class="ws-prog-bar"><div class="ws-prog-fill" style="width:${gPct}%"></div></div>
  </div>`;
  html += `<div class="ws-prog-row">
    <div class="ws-prog-label"><span>Hebrew</span><strong>${st.hConf} / ${st.hTotal}</strong></div>
    <div class="ws-prog-bar"><div class="ws-prog-fill" style="width:${hPct}%"></div></div>
  </div>`;
  html += '</div>';
  html += '<hr class="ws-nav-divider" />';
  html += '<div class="ws-nav-section">Phases</div>';

  for (const ph of PHASES) {
    const active = _uiState.phase === ph.id ? ' active' : '';
    let badge = '';
    if (ph.id !== 'dashboard') {
      const ps = _phaseStats(ph.id);
      if (ps.total !== null) {
        badge = `<span class="ws-nav-btn__count">${ps.done}/${ps.total}</span>`;
      }
    }
    html += `<button class="ws-nav-btn${active}" data-phase="${ph.id}">
      <span class="ws-nav-btn__icon">${ph.icon}</span>
      <span class="ws-nav-btn__label">${ph.label}</span>
      ${badge}
    </button>`;
  }

  if (st.disputed || st.locked || st.deferred) {
    html += '<hr class="ws-nav-divider" />';
    html += '<div class="ws-nav-section">Flagged</div>';
    if (st.disputed) html += `<div class="ws-nav-flag ws-nav-flag--dispute">⚑ Disputed: ${st.disputed}</div>`;
    if (st.deferred) html += `<div class="ws-nav-flag ws-nav-flag--defer">⟳ Deferred: ${st.deferred}</div>`;
    if (st.locked)   html += `<div class="ws-nav-flag ws-nav-flag--lock">🔒 Locked: ${st.locked}</div>`;
  }

  $nav.innerHTML = html;
  $nav.querySelectorAll('.ws-nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      _uiState.phase = btn.dataset.phase;
      _uiState.activeCode = null;
      _saveUiState();
      _activatePhase();
    });
  });
}

/* ── Phase activation ──────────────────────────────────────── */
async function _activatePhase() {
  _renderNav();

  if (_uiState.phase === 'dashboard') {
    _renderDashboard();
    return;
  }

  if (_uiState.phase === 'primer') {
    _renderPrimerNav();
    return;
  }

  // Show queue-level loading spinner while fetching
  $queue.innerHTML = '<p class="ws-queue-loading">Loading…</p>';
  $count.textContent = '';
  $dossier.innerHTML = '<p class="ws-placeholder">← Select an entry to begin reviewing</p>';

  try {
    await _loadPhase(_uiState.phase);
  } catch (err) {
    $queue.innerHTML = `<p class="ws-queue-error">Failed to load: ${_esc(err.message)}</p>`;
    return;
  }

  _queue = _buildQueue(_uiState.phase);
  _page  = 0;
  _renderNav();   // update badge counts now that data is loaded
  _applyFilter();

  // Restore previously selected entry
  if (_uiState.activeCode && _cache[_uiState.phase]?.[_uiState.activeCode]) {
    _renderDossier(_uiState.activeCode);
  }
}

/* ── Queue rendering ───────────────────────────────────────── */
function _applyFilter() {
  const q = ($search?.value || '').toLowerCase().trim();
  const phaseData = _cache[_uiState.phase] || {};

  _filtered = q
    ? _queue.filter(code => {
        const e = phaseData[code];
        if (!e) return false;
        return code.toLowerCase().includes(q)
          || (e.lemma    || '').toLowerCase().includes(q)
          || (e.translit || '').toLowerCase().includes(q)
          || (e.tiers?.literal?.primary  || '').toLowerCase().includes(q)
          || (e.tiers?.mediating?.primary|| '').toLowerCase().includes(q);
      })
    : _queue;

  _page = 0;
  _renderQueue();
}

function _renderQueue() {
  const phaseData = _cache[_uiState.phase] || {};
  const slice     = _filtered.slice(0, (_page + 1) * PAGE_SIZE);
  const hasMore   = _filtered.length > slice.length;

  $count.textContent = `${_filtered.length} entries`;

  let html = '';
  for (const code of slice) {
    const src    = phaseData[code];
    if (!src) continue;
    const dec    = _decisions[code] || {};
    const status = dec.status || src.status || 'draft';
    const gloss  = src.tiers?.literal?.primary || src.primary || '';
    const active = code === _uiState.activeCode ? ' active' : '';

    html += `<div class="ws-queue-item${active}" data-code="${code}">
      <span class="ws-queue-item__code">${_esc(code)}</span>
      <span class="ws-queue-item__lemma">${_esc(src.lemma || '')}</span>
      <span class="ws-queue-item__gloss">${_esc(gloss)}</span>
      <span class="ws-queue-item__status ws-status--${status}">${status}</span>
    </div>`;
  }

  if (hasMore) {
    html += `<button class="ws-queue-load-more" id="ws-load-more">
      Show more (${_filtered.length - slice.length} remaining)
    </button>`;
  }

  if (!html) html = '<p class="ws-queue-loading">No entries match.</p>';

  $queue.innerHTML = html;
  $queue.querySelectorAll('.ws-queue-item').forEach(el => {
    el.addEventListener('click', () => {
      _uiState.activeCode = el.dataset.code;
      _saveUiState();
      _renderQueueActive();
      _renderDossier(el.dataset.code);
    });
  });

  document.getElementById('ws-load-more')?.addEventListener('click', () => { _page++; _renderQueue(); });

  $queue.querySelector('.ws-queue-item.active')?.scrollIntoView({ block: 'nearest' });
}

function _renderQueueActive() {
  $queue.querySelectorAll('.ws-queue-item').forEach(el => {
    el.classList.toggle('active', el.dataset.code === _uiState.activeCode);
  });
}

/* ── Dossier ───────────────────────────────────────────────── */
function _renderDossier(code) {
  const entry = _getEntry(code);
  if (!entry) { $dossier.innerHTML = '<p class="ws-placeholder">Entry not found.</p>'; return; }

  const src         = entry;
  const hasSrcData  = !!(src.source_data);
  const dodson      = src.source_data?.dodson || {};
  const thayer      = src.source_data?.thayer || {};
  const hebrew      = src.source_data?.hebrew || {};
  const bdb         = src.source_data?.bdb    || {};
  const freq        = src.nt_freq ?? src.ot_freq ?? 0;
  const freqLabel   = entry._lang === 'greek' ? 'NT' : 'OT';
  const dispute     = src.dispute_level || 0;
  const dispLabels  = ['', 'minor', 'moderate', 'contested', 'major debate'];

  let html = '<div class="ws-dossier">';

  // ── Header
  html += `<div class="ws-dossier-head">
    <div class="ws-dossier-head__top">
      <span class="ws-dossier__code">${_esc(code)}</span>
      <span class="ws-dossier__lemma">${_esc(src.lemma || '')}</span>
      ${src.translit ? `<span class="ws-dossier__translit">${_esc(src.translit)}</span>` : ''}
      ${src.pos      ? `<span class="ws-dossier__pos">${_esc(src.pos)}</span>` : ''}
      ${dispute > 0  ? `<span class="ws-dossier__dispute ws-dispute-${dispute}">⚑ ${dispLabels[dispute]}</span>` : ''}
    </div>
    <div class="ws-dossier-head__meta">
      ${freq > 0 ? `<span>${freqLabel} frequency: <strong>${freq.toLocaleString()}×</strong></span>` : ''}
      <span>Status: <span class="ws-dossier-head__status ws-status--${entry._status}">${entry._status}</span></span>
    </div>
  </div>`;

  // ── Attested Range (primary content — what the lexical sources actually document)
  if (src.semantic_range) {
    html += `<div class="ws-section ws-section--range">
      <div class="ws-section-title">Attested Range <span class="ws-section-note">— what lexical sources document across all uses</span></div>
      <p class="ws-semantic ws-semantic--headline">${_esc(src.semantic_range)}</p>
    </div>`;
  }

  // ── Lexical Sources (supporting detail, subordinate to the range)
  if (hasSrcData) {
    html += '<div class="ws-section ws-section--sources"><div class="ws-section-title">Lexical Sources</div>';
    html += '<div class="ws-sources">';
    if (entry._lang === 'greek') {
      if (dodson.gloss || dodson.def) html += _sourceCard('Dodson (CC0)', dodson.gloss, dodson.def, dodson.deriv);
      if (thayer.short || thayer.long) html += _sourceCard('Thayer (1889)', thayer.short, thayer.long, '');
    } else {
      if (hebrew.gloss || hebrew.def)  html += _sourceCard("Strong's Hebrew", hebrew.gloss, hebrew.def, hebrew.deriv);
      if (bdb.short || bdb.long)       html += _sourceCard('BDB (1906)', bdb.short, bdb.long, '');
    }
    html += '</div></div>';
  }

  // ── Book distribution map (shows where this word actually clusters)
  html += _renderBookDistribution(entry._bookFreq, entry._lang);

  // ── Default Rendering Tendency (your starting-point per tier — not a decided meaning)
  html += '<div class="ws-section ws-section--tiers" id="ws-tiers-section">';
  html += '<div class="ws-section-title">Default Rendering Tendency <span class="ws-section-note">— your starting point; context below is where meaning is actually decided</span></div>';
  html += _renderTiersView(entry._tiers);
  html += '</div>';

  // ── Per-book defaults (middle tier between global default and passage overrides)
  html += _renderBookDefaults(code, entry);

  // ── Contextual Renderings (the primary work surface — where translation actually happens)
  const overrides = ((_decisions[code] || {}).context_overrides) || src.context_overrides || [];
  html += `<div class="ws-section ws-section--contextual" id="ws-overrides-section">
    <div class="ws-section-title ws-section-title--contextual">Contextual Renderings
    </div>
    <button class="ws-add-contextual-btn" data-code="${_esc(code)}">+ Add contextual rendering</button>`;
  if (!overrides.length) {
    html += '<p class="ws-log-empty ws-contextual-hint">Translation decisions live here, not in the default above. Add a rendering whenever a specific passage, book, genre, or grammatical construction clearly calls for a different gloss.</p>';
  } else {
    html += '<div class="ws-overrides-list">';
    for (let i = 0; i < overrides.length; i++) {
      const ov = overrides[i];
      html += `<div class="ws-override-card">
        <div class="ws-override-card__condition">${_esc(ov.condition || '')}</div>
        <div class="ws-override-card__tiers">
          <span class="ws-tier-label--lit">L:</span> ${_esc(ov.literal || '—')}
          &nbsp;·&nbsp;
          <span class="ws-tier-label--med">M:</span> ${_esc(ov.mediating || '—')}
          &nbsp;·&nbsp;
          <span class="ws-tier-label--tho">T:</span> ${_esc(ov.thought || '—')}
        </div>
        <button class="ws-remove-override-btn" data-code="${_esc(code)}" data-idx="${i}">✕</button>
      </div>`;
    }
    html += '</div>';
  }
  html += '</div>';

  // ── Decision log
  const log = entry._decLog;
  html += '<div class="ws-section"><div class="ws-section-title">Decision Log</div>';
  if (!log.length) {
    html += '<p class="ws-log-empty">No decisions recorded yet.</p>';
  } else {
    html += '<ul class="ws-log">';
    for (const item of [...log].reverse()) {
      html += `<li class="ws-log-item">
        <div class="ws-log-item__meta">${_esc(item.action || '')} · ${_esc(item.date || '')}</div>
        <div>${_esc(item.note || '')}</div>
      </li>`;
    }
    html += '</ul>';
  }
  html += '</div>';

  // ── Actions (labels reframed — internal action values unchanged for pipeline compatibility)
  const isLocked    = entry._status === 'locked';
  const isConfirmed = entry._status === 'confirmed' || entry._status === 'override';
  html += `<div class="ws-actions" id="ws-actions">
    <button class="ws-action-btn ws-action-btn--confirm" data-action="confirm" ${isLocked ? 'disabled' : ''}>✓ Set Default</button>
    <button class="ws-action-btn ws-action-btn--override" data-action="override" ${isLocked ? 'disabled' : ''}>✎ Edit Default</button>
    <button class="ws-action-btn ws-action-btn--inform"   data-action="inform"   ${isLocked ? 'disabled' : ''}>💬 Note</button>
    <button class="ws-action-btn ws-action-btn--dispute"  data-action="dispute"  ${isLocked ? 'disabled' : ''}>⚑ Flag Range</button>
    <button class="ws-action-btn ws-action-btn--defer"    data-action="defer"    ${isLocked ? 'disabled' : ''}>⟳ Defer</button>
    <button class="ws-action-btn ws-action-btn--lock"     data-action="lock"     ${!isConfirmed || isLocked ? 'disabled' : ''}>★ Anchor</button>
  </div>`;

  html += '</div>';
  $dossier.innerHTML = html;

  $dossier.querySelectorAll('[data-action]').forEach(btn => {
    btn.addEventListener('click', () => _handleAction(btn.dataset.action, code));
  });

  // Contextual rendering buttons (renamed class; old ws-add-override-btn alias kept for safety)
  ($dossier.querySelector('.ws-add-contextual-btn') || $dossier.querySelector('.ws-add-override-btn'))
    ?.addEventListener('click', () => _showAddOverrideForm(code));
  $dossier.querySelectorAll('.ws-remove-override-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const idx = parseInt(btn.dataset.idx, 10);
      const dec = _decisions[code] || {};
      const ovs = [...(dec.context_overrides || src.context_overrides || [])];
      ovs.splice(idx, 1);
      _setDecision(code, { context_overrides: ovs });
      _renderDossier(code);
    });
  });

  // Per-book default inputs — debounced blur-save so typing isn't interrupted
  // INTENT: On blur, collect all book-default inputs for this entry and persist to _decisions.
  // CHANGE? _setDecision merges at the top level; book_defaults must be the full object each save.
  // VERIFY: Edit a per-book input, tab away; reload the entry — the value should persist.
  $dossier.querySelectorAll('.ws-bookdef-input').forEach(inp => {
    inp.addEventListener('blur', () => {
      const c    = inp.dataset.bdCode;
      const book = inp.dataset.bdBook;
      const tier = inp.dataset.bdTier;
      const val  = inp.value.trim();
      const existing = (_decisions[c] || {}).book_defaults || {};
      const updated  = { ...existing, [book]: { ...(existing[book] || {}), [tier]: val || undefined } };
      // Prune empty book entries so JSON stays clean
      if (updated[book] && !Object.values(updated[book]).some(Boolean)) delete updated[book];
      _setDecision(c, { book_defaults: updated });
    });
  });
}

// INTENT: Render a compact book-distribution heat map so the user can see at a glance
//   where a word clusters (e.g. a Pauline hapax vs. a synoptic staple) before setting defaults.
// CHANGE? If BOOK_ORDER_OT / BOOK_ORDER_NT are changed, the cells rendered here will shift order.
// VERIFY: Open a high-frequency entry (e.g. G3056 λόγος); OT and NT rows should show coloured
//   cells for every book with occurrences; hover titles should show book abbreviation + count.
function _renderBookDistribution(bookFreq, lang) {
  if (!bookFreq || !Object.keys(bookFreq).length) return '';
  const max = Math.max(...Object.values(bookFreq), 1);
  const cell = ([key, abbr]) => {
    const n = bookFreq[key] || 0;
    if (!n) return `<span class="ws-bdist-cell ws-bdist-cell--zero" title="${abbr}"></span>`;
    const intensity = Math.ceil((n / max) * 4); // 1–4 heat levels
    return `<span class="ws-bdist-cell ws-bdist-cell--h${intensity}" title="${abbr}: ${n}×"></span>`;
  };
  const showOT = lang === 'hebrew' || Object.keys(bookFreq).some(k => BOOK_ORDER_OT.some(([bk]) => bk === k && bookFreq[bk] > 0));
  const showNT = lang === 'greek'  || Object.keys(bookFreq).some(k => BOOK_ORDER_NT.some(([bk]) => bk === k && bookFreq[bk] > 0));
  let html = '<div class="ws-section ws-section--bdist"><div class="ws-section-title">Bible Distribution</div><div class="ws-bdist">';
  if (showOT) html += `<div class="ws-bdist-row"><span class="ws-bdist-label">OT</span><div class="ws-bdist-cells">${BOOK_ORDER_OT.map(cell).join('')}</div></div>`;
  if (showNT) html += `<div class="ws-bdist-row"><span class="ws-bdist-label">NT</span><div class="ws-bdist-cells">${BOOK_ORDER_NT.map(cell).join('')}</div></div>`;
  html += '</div></div>';
  return html;
}

// INTENT: Render a collapsible per-book defaults editor so the user can override the global
//   default rendering for specific books/authors without needing a passage-level override.
// CHANGE? Saving calls _setDecision({book_defaults}); _getEntry() reads dec.book_defaults back.
//   If _setDecision's merge strategy changes, verify saves aren't overwriting sibling keys.
// VERIFY: Set a per-book default for "romans"; run translate-bible.py and confirm that book's
//   output uses that rendering instead of the global tier default.
function _renderBookDefaults(code, entry) {
  const lang     = entry._lang;
  const bookFreq = entry._bookFreq || {};
  const defs     = entry._bookDefaults || {};
  const books    = (lang === 'greek' ? BOOK_ORDER_NT : BOOK_ORDER_OT)
    .filter(([key]) => (bookFreq[key] || 0) > 0);
  if (!books.length) return '';

  const open = Object.keys(defs).length > 0;
  let html = `<div class="ws-section ws-section--bookdefs">
    <details class="ws-bookdefs-details" ${open ? 'open' : ''}>
      <summary class="ws-section-title ws-bookdefs-summary">Per-book Defaults
        <span class="ws-section-note">— override the global default for a specific book or author</span>
      </summary>
      <div class="ws-bookdefs-grid">`;

  for (const [key, abbr] of books) {
    const bd = defs[key] || {};
    const n  = bookFreq[key] || 0;
    html += `<div class="ws-bookdef-row">
      <span class="ws-bookdef-abbr" title="${key} (${n}×)">${abbr}</span>
      <input class="ws-bookdef-input" data-bd-code="${_esc(code)}" data-bd-book="${_esc(key)}" data-bd-tier="literal"
             placeholder="Literal" value="${_esc(bd.literal || '')}">
      <input class="ws-bookdef-input" data-bd-code="${_esc(code)}" data-bd-book="${_esc(key)}" data-bd-tier="mediating"
             placeholder="Mediating" value="${_esc(bd.mediating || '')}">
      <input class="ws-bookdef-input" data-bd-code="${_esc(code)}" data-bd-book="${_esc(key)}" data-bd-tier="thought"
             placeholder="Thought" value="${_esc(bd.thought || '')}">
    </div>`;
  }
  html += '</div></details></div>';
  return html;
}

function _renderTiersView(tiers) {
  const lit = tiers?.literal   || {};
  const med = tiers?.mediating || {};
  const tho = tiers?.thought   || {};
  return `<table class="ws-tiers"><tbody>
    ${_tierRow('Literal',   'lit', lit.primary, lit.notes)}
    ${_tierRow('Mediating', 'med', med.primary, med.notes)}
    ${_tierRow('Thought',   'tho', tho.primary, tho.notes)}
  </tbody></table>`;
}

function _tierRow(label, cls, primary, notes) {
  return `<tr>
    <th class="ws-tier-label--${cls}">${label}</th>
    <td class="ws-tier-primary">${_esc(primary || '—')}</td>
    <td class="ws-tier-notes">${notes ? _esc(notes) : ''}</td>
  </tr>`;
}

function _sourceCard(label, gloss, def, deriv) {
  return `<div class="ws-source-card">
    <div class="ws-source-card__label">${_esc(label)}</div>
    ${gloss ? `<div class="ws-source-card__gloss">${_esc(gloss)}</div>` : ''}
    ${def   ? `<div class="ws-source-card__def">${_esc(def)}</div>` : ''}
    ${deriv ? `<div class="ws-source-card__deriv">${_esc(deriv)}</div>` : ''}
  </div>`;
}

/* ── Actions ───────────────────────────────────────────────── */
function _handleAction(action, code) {
  if      (action === 'confirm')  _doConfirm(code);
  else if (action === 'override') _showOverrideForm(code);
  else if (action === 'inform')   _showInformForm(code);
  else if (action === 'dispute')  _doSetStatus(code, 'disputed', 'Marked as disputed');
  else if (action === 'defer')  { _doSetStatus(code, 'deferred', 'Deferred for later review'); _advanceQueue(code); }
  else if (action === 'lock') {
    const entry = _getEntry(code);
    if (entry?._status === 'confirmed' || entry?._status === 'override')
      _doSetStatus(code, 'locked', 'Locked — rendering is final');
  }
}

function _doConfirm(code) {
  const now = new Date().toISOString().slice(0, 10);
  const dec = _decisions[code] || {};
  const log = [...(dec.log || []), { action: 'confirmed', date: now, note: 'Set as default rendering tendency' }];
  _setDecision(code, { status: 'confirmed', log });
  _afterAction(code);
  _advanceQueue(code);
}

function _doSetStatus(code, status, note) {
  const now = new Date().toISOString().slice(0, 10);
  const dec = _decisions[code] || {};
  const log = [...(dec.log || []), { action: status, date: now, note }];
  _setDecision(code, { status, log });
  _afterAction(code);
}

function _setDecision(code, patch) {
  if (!_decisions[code]) _decisions[code] = {};
  Object.assign(_decisions[code], patch);
  _saveDecisions();
}

function _afterAction(code) {
  _renderNav();
  _renderDossier(code);
  _updateQueueItem(code);
  _updateTopbarStats();
}

function _showOverrideForm(code) {
  const entry = _getEntry(code);
  if (!entry) return;
  const t = entry._tiers || {};
  const lit = t.literal?.primary   || '';
  const med = t.mediating?.primary || '';
  const tho = t.thought?.primary   || '';

  const section = document.getElementById('ws-tiers-section');
  if (!section) return;

  section.innerHTML = `<div class="ws-section-title">Override Renderings</div>
    <div class="ws-override-form">
      <div class="ws-override-row"><label class="ws-tier-label--lit">Literal</label><input id="ws-ov-lit" type="text" value="${_esc(lit)}" /></div>
      <div class="ws-override-row"><label class="ws-tier-label--med">Mediating</label><input id="ws-ov-med" type="text" value="${_esc(med)}" /></div>
      <div class="ws-override-row"><label class="ws-tier-label--tho">Thought</label><input id="ws-ov-tho" type="text" value="${_esc(tho)}" /></div>
      <div class="ws-reasoning-label">Your reasoning <span>(required)</span></div>
      <textarea class="ws-reasoning" id="ws-ov-reason" rows="3" placeholder="Why are you overriding? 1–3 sentences."></textarea>
    </div>`;

  const bar = document.getElementById('ws-actions');
  if (!bar) return;
  bar.innerHTML = `
    <button class="ws-action-btn ws-action-btn--save" id="ws-ov-save">Save Override</button>
    <button class="ws-action-btn ws-action-btn--cancel" id="ws-ov-cancel">Cancel</button>`;

  document.getElementById('ws-ov-save').addEventListener('click', () => {
    const reason = (document.getElementById('ws-ov-reason')?.value || '').trim();
    if (!reason) {
      document.getElementById('ws-ov-reason').style.borderColor = '#c0392b';
      return;
    }
    const now = new Date().toISOString().slice(0, 10);
    const dec = _decisions[code] || {};
    const newTiers = {
      literal:   { primary: document.getElementById('ws-ov-lit')?.value || '', notes: null },
      mediating: { primary: document.getElementById('ws-ov-med')?.value || '', notes: null },
      thought:   { primary: document.getElementById('ws-ov-tho')?.value || '', notes: null },
    };
    const log = [...(dec.log || []), { action: 'override', date: now, note: reason }];
    _setDecision(code, { status: 'override', tiers: newTiers, log });
    _afterAction(code);
  });

  document.getElementById('ws-ov-cancel').addEventListener('click', () => _renderDossier(code));
}

function _showInformForm(code) {
  const bar = document.getElementById('ws-actions');
  if (!bar) return;
  const prev = bar.innerHTML;
  bar.innerHTML = `
    <div class="ws-inform-wrap" style="width:100%">
      <div class="ws-inform-label">Add context or reasoning (saved to decision log):</div>
      <textarea class="ws-reasoning" id="ws-inform-text" rows="3" placeholder="e.g. Moulton & Milligan shows this word in papyri meaning…"></textarea>
    </div>
    <button class="ws-action-btn ws-action-btn--save" id="ws-inform-save">Save Note</button>
    <button class="ws-action-btn ws-action-btn--cancel" id="ws-inform-cancel">Cancel</button>`;

  document.getElementById('ws-inform-save').addEventListener('click', () => {
    const note = (document.getElementById('ws-inform-text')?.value || '').trim();
    if (!note) return;
    const now = new Date().toISOString().slice(0, 10);
    const dec = _decisions[code] || {};
    const log = [...(dec.log || []), { action: 'inform', date: now, note }];
    _setDecision(code, { log });
    _afterAction(code);
  });
  document.getElementById('ws-inform-cancel').addEventListener('click', () => _renderDossier(code));
}

function _showAddOverrideForm(code) {
  const section = document.getElementById('ws-overrides-section');
  if (!section) return;
  const existing = section.innerHTML;

  section.innerHTML += `
    <div class="ws-override-form ws-add-override-form" id="ws-aof">
      <div class="ws-reasoning-label">Condition — describe when this override applies</div>
      <input id="ws-aof-cond" class="ws-reasoning" style="height:auto;padding:.3rem .5rem"
             placeholder="e.g. In Romans 7–8 soteriological context · When preceded by πνεῦμα · Genesis 1 creation narrative" />
      <div class="ws-override-row" style="margin-top:.5rem">
        <label class="ws-tier-label--lit">Literal</label>
        <input id="ws-aof-lit" type="text" placeholder="override or leave blank to keep default" />
      </div>
      <div class="ws-override-row">
        <label class="ws-tier-label--med">Mediating</label>
        <input id="ws-aof-med" type="text" placeholder="override or leave blank" />
      </div>
      <div class="ws-override-row">
        <label class="ws-tier-label--tho">Thought</label>
        <input id="ws-aof-tho" type="text" placeholder="override or leave blank" />
      </div>
      <div style="display:flex;gap:.4rem;margin-top:.5rem">
        <button class="ws-action-btn ws-action-btn--save" id="ws-aof-save">Save Override</button>
        <button class="ws-action-btn ws-action-btn--cancel" id="ws-aof-cancel">Cancel</button>
      </div>
    </div>`;

  document.getElementById('ws-aof-save').addEventListener('click', () => {
    const condition = (document.getElementById('ws-aof-cond')?.value || '').trim();
    if (!condition) { document.getElementById('ws-aof-cond').style.borderColor = '#c0392b'; return; }
    const newOv = {
      condition,
      literal:   document.getElementById('ws-aof-lit')?.value.trim() || '',
      mediating: document.getElementById('ws-aof-med')?.value.trim() || '',
      thought:   document.getElementById('ws-aof-tho')?.value.trim() || '',
    };
    const entry = _getEntry(code);
    const existing = ((_decisions[code] || {}).context_overrides) || entry?.context_overrides || [];
    _setDecision(code, { context_overrides: [...existing, newOv] });
    _renderDossier(code);
  });
  document.getElementById('ws-aof-cancel').addEventListener('click', () => _renderDossier(code));
}

function _advanceQueue(code) {
  const idx = _filtered.indexOf(code);
  if (idx < 0 || idx >= _filtered.length - 1) return;
  const next = _filtered[idx + 1];
  _uiState.activeCode = next;
  _saveUiState();
  _renderQueueActive();
  _renderDossier(next);
}

function _updateQueueItem(code) {
  const el = $queue.querySelector(`[data-code="${code}"]`);
  if (!el) return;
  const status = (_decisions[code] || {}).status || 'draft';
  const badge  = el.querySelector('.ws-queue-item__status');
  if (badge) { badge.className = `ws-queue-item__status ws-status--${status}`; badge.textContent = status; }
}

/* ── Primers ───────────────────────────────────────────────── */
const PRIMER_GROUPS = [
  {
    label: 'Biblical Greek',
    sections: [
      { id: 'greek-alphabet',    label: 'Alphabet & Script',       icon: 'α' },
      { id: 'greek-grammar',     label: 'Grammar Foundations',     icon: 'γ' },
      { id: 'greek-verbs',       label: 'Verbs & Aspect',          icon: 'V' },
      { id: 'greek-sentence',    label: 'Sentence Structure',       icon: '⇢' },
      { id: 'greek-particles',   label: 'Particles & Discourse',   icon: '…' },
      { id: 'greek-idioms',      label: 'Idioms & Figures',        icon: '💬' },
    ],
  },
  {
    label: 'Biblical Hebrew',
    sections: [
      { id: 'heb-alphabet',      label: 'Alphabet & Vowels',       icon: 'א' },
      { id: 'heb-roots',         label: 'The Root System',         icon: '⊥' },
      { id: 'heb-binyanim',      label: 'Verb Stems (Binyanim)',   icon: 'B' },
      { id: 'heb-sentence',      label: 'Sentence Structure',       icon: '⇢' },
      { id: 'heb-poetry',        label: 'Hebrew Poetry',           icon: '✦' },
      { id: 'heb-idioms',        label: 'Idioms & Body Language',  icon: '✋' },
    ],
  },
  {
    label: 'World of the Bible',
    sections: [
      { id: 'world-honor',       label: 'Honor & Shame Culture',   icon: '🏛' },
      { id: 'world-covenant',    label: 'Covenant & Treaty Forms', icon: '📜' },
      { id: 'world-secondtemple',label: 'Second Temple Judaism',   icon: '🕍' },
      { id: 'world-roman',       label: 'The Roman World',         icon: '⚔' },
      { id: 'world-ant',         label: 'Ancient Near East',       icon: '🌙' },
    ],
  },
  {
    label: 'How to Translate',
    sections: [
      { id: 'tr-philosophy',     label: 'Translation Philosophy',  icon: '⚖' },
      { id: 'tr-polysemy',       label: 'One Word, Many Meanings', icon: '🔀' },
      { id: 'tr-genre',          label: 'Genre & How to Read It',  icon: '📚' },
      { id: 'tr-intertextuality',label: 'Intertextuality & LXX',   icon: '🔗' },
      { id: 'tr-textcrit',       label: 'Textual Criticism',       icon: '🔬' },
      { id: 'tr-method',         label: 'Exegetical Method',       icon: '🗺' },
    ],
  },
];

const PRIMER_CONTENT = {
  'greek-alphabet': `
<h3>The Greek Alphabet & Script</h3>
<p>Biblical Greek uses 24 letters. The New Testament was written in <strong>uncials</strong> (all capitals, no spaces, no punctuation) in the oldest manuscripts. Later manuscripts added lowercase letters, accents, and breathing marks. You'll see the lowercase forms in lexicons and this workshop.</p>
<table class="ws-primer-table">
  <tr><th>Uppercase</th><th>Lowercase</th><th>Name</th><th>Sound</th></tr>
  <tr><td>Α</td><td>α</td><td>Alpha</td><td>"a" as in father</td></tr>
  <tr><td>Β</td><td>β</td><td>Beta</td><td>"b"</td></tr>
  <tr><td>Γ</td><td>γ</td><td>Gamma</td><td>"g" (before κ/γ/χ/ξ = "ng")</td></tr>
  <tr><td>Δ</td><td>δ</td><td>Delta</td><td>"d"</td></tr>
  <tr><td>Ε</td><td>ε</td><td>Epsilon</td><td>short "e" as in bed</td></tr>
  <tr><td>Ζ</td><td>ζ</td><td>Zeta</td><td>"dz" or "z"</td></tr>
  <tr><td>Η</td><td>η</td><td>Eta</td><td>long "e" as in hey</td></tr>
  <tr><td>Θ</td><td>θ</td><td>Theta</td><td>"th" as in thin</td></tr>
  <tr><td>Ι</td><td>ι</td><td>Iota</td><td>"i" as in machine or sit</td></tr>
  <tr><td>Κ</td><td>κ</td><td>Kappa</td><td>"k"</td></tr>
  <tr><td>Λ</td><td>λ</td><td>Lambda</td><td>"l"</td></tr>
  <tr><td>Μ</td><td>μ</td><td>Mu</td><td>"m"</td></tr>
  <tr><td>Ν</td><td>ν</td><td>Nu</td><td>"n"</td></tr>
  <tr><td>Ξ</td><td>ξ</td><td>Xi</td><td>"x" as in fox</td></tr>
  <tr><td>Ο</td><td>ο</td><td>Omicron</td><td>short "o"</td></tr>
  <tr><td>Π</td><td>π</td><td>Pi</td><td>"p"</td></tr>
  <tr><td>Ρ</td><td>ρ</td><td>Rho</td><td>rolled "r"</td></tr>
  <tr><td>Σ</td><td>σ/ς</td><td>Sigma</td><td>"s" (ς used at end of word)</td></tr>
  <tr><td>Τ</td><td>τ</td><td>Tau</td><td>"t"</td></tr>
  <tr><td>Υ</td><td>υ</td><td>Upsilon</td><td>"u" (French) or "oo"</td></tr>
  <tr><td>Φ</td><td>φ</td><td>Phi</td><td>"ph" as in phone</td></tr>
  <tr><td>Χ</td><td>χ</td><td>Chi</td><td>"ch" as in Bach (guttural)</td></tr>
  <tr><td>Ψ</td><td>ψ</td><td>Psi</td><td>"ps" as in lips</td></tr>
  <tr><td>Ω</td><td>ω</td><td>Omega</td><td>long "o" as in tone</td></tr>
</table>
<h4>Breathing Marks</h4>
<p>Every Greek word beginning with a vowel has a breathing mark. A <strong>smooth breathing</strong> (ἀ) is silent. A <strong>rough breathing</strong> (ἁ) adds an "h" sound. So ἁμαρτία (sin) = "hamartia." The word ὁ (the) has smooth breathing; ὃς (who) has smooth breathing — but εἷς (one) has rough.</p>
<h4>Accents</h4>
<p>Greek has three accents (acute ά, grave ὰ, circumflex ᾶ). In ancient Greek they indicated pitch. For translation purposes, accents help you distinguish words that otherwise look identical: ἐστίν (he is) vs. ἔστιν (there is); τίς (who?) vs. τις (someone).</p>`,

  'greek-grammar': `
<h3>Greek Grammar Foundations — Nouns, Cases & the Article</h3>
<h4>The Greek Article</h4>
<p>Greek has a definite article (ὁ/ἡ/τό = the) but <em>no indefinite article</em>. When there is no article, English translators must decide whether to supply "a," "an," or nothing. This matters theologically: John 1:1 ends "καὶ θεὸς ἦν ὁ λόγος" — the Word is "θεὸς" without the article. Jehovah's Witnesses translate this "a god." Mainstream scholarship reads it as a qualitative statement: "the Word was divine in nature" (not a second god, but not lacking divinity).</p>
<h4>The Five Cases</h4>
<p>Greek nouns change their ending (inflection) to show their grammatical role. The parse codes in the interlinear always tell you the case:</p>
<ul>
  <li><strong>Nominative (NOM)</strong> — the subject: "<em>God</em> so loved." Also used for predicate nouns: "The Word was <em>God</em>."</li>
  <li><strong>Genitive (GEN)</strong> — possession, source, relationship, or description: "love <em>of God</em>," "faith <em>of Christ</em>" (a major debate — see Polysemy section). Also used after many prepositions (ἐκ, ἀπό, διά).</li>
  <li><strong>Dative (DAT)</strong> — indirect object, instrument, sphere, or manner: "gave <em>to us</em>," "saved <em>by grace</em>," "pure <em>in heart</em>." Used after ἐν, σύν.</li>
  <li><strong>Accusative (ACC)</strong> — direct object or extent: "loved <em>the world</em>," "walked <em>two miles</em>." Used after εἰς, κατά, παρά.</li>
  <li><strong>Vocative (VOC)</strong> — direct address: "<em>Lord</em>, have mercy."</li>
</ul>
<h4>Gender, Number, Agreement</h4>
<p>Every Greek noun has a fixed gender — masculine, feminine, or neuter — that often has nothing to do with biological sex. πνεῦμα (spirit) is <strong>neuter</strong>, even though Jesus uses a masculine pronoun (ἐκεῖνος) for the Holy Spirit in John 14–16, signalling personhood. Articles, adjectives, and participles must agree with the noun they modify in <em>gender, number, and case</em>.</p>
<h4>Pronouns</h4>
<p>Greek pronouns are highly specific. αὐτός (G846) is the most common and can mean: he, she, it, they, him, her, them — <em>or</em> "the same" (when used with the article). Context and gender/number always disambiguate. The intensive αὐτός without the article means "himself/herself/itself."</p>`,

  'greek-verbs': `
<h3>Greek Verbs — Aspect, Tense & Mood</h3>
<h4>The Most Important Insight: Aspect First</h4>
<p>The single most important thing to grasp about Greek verbs: <strong>aspect is primary, time is secondary.</strong> Greek verb "tenses" encode the <em>shape</em> of an action — not primarily when it happened. This is why the same "present tense" form can be translated as present, future, or even past in English, depending on context.</p>
<h4>The Three Aspects</h4>
<ul>
  <li><strong>Perfective aspect (Aorist)</strong> — the action viewed as a single, complete whole, like a snapshot. "He believed," "she stood up," "God spoke." The aorist says nothing about duration or repetition — only that the action is viewed as a unit. Most common NT verb form. Parse: V-AAI, V-AAS, V-AAP, etc.</li>
  <li><strong>Imperfective aspect (Present & Imperfect)</strong> — the action viewed as ongoing, repeated, or in progress, like a video. Present: "he is believing/keeps believing." Imperfect: "he was (continuously) believing." The present imperative often means "keep doing this" or "stop doing this (ongoing action)." Parse: V-PAI, V-IAI, etc.</li>
  <li><strong>Stative aspect (Perfect & Pluperfect)</strong> — a past action whose effects persist into the present, like a photograph with caption. "It is written" (γέγραπται) — someone wrote it, and it still stands. "I have been crucified with Christ" (Gal 2:20) — a past event with present ongoing reality. Theologically vital in Hebrews ("he has sat down," "he has offered"). Parse: V-RAI, V-RPI, etc.</li>
</ul>
<h4>Voice</h4>
<ul>
  <li><strong>Active</strong> — subject performs the action: "God <em>loved</em>."</li>
  <li><strong>Passive</strong> — subject receives the action: "we <em>are justified</em>." The agent (by whom) uses ὑπό + genitive.</li>
  <li><strong>Middle</strong> — subject acts with special interest or for itself. Often translated as active: "he <em>repented</em>" (μετενόησεν, middle). The middle voice is subtle and often signals the subject's deep involvement.</li>
</ul>
<h4>Mood</h4>
<ul>
  <li><strong>Indicative</strong> — stating a fact (real or assumed real): "He died." "You are sinners."</li>
  <li><strong>Subjunctive</strong> — possibility, purpose, or condition: "that you <em>may believe</em>," "if anyone <em>sins</em>." The most common non-indicative mood.</li>
  <li><strong>Imperative</strong> — command or prohibition: "<em>Repent!</em>" "<em>Do not sin.</em>" Aorist imperative = do it (once, decisively). Present imperative = keep doing it / stop doing it.</li>
  <li><strong>Optative</strong> — wish or very remote possibility: "May it never be!" (μὴ γένοιτο — Paul's rhetorical "God forbid!"). Rare in NT.</li>
  <li><strong>Infinitive</strong> — verbal noun: "to believe," "to love." Often used in purpose clauses.</li>
  <li><strong>Participle</strong> — verbal adjective, extremely common in Greek. "The one believing," "having been raised," "while walking." Participles agree with their noun in gender, number, case.</li>
</ul>
<h4>Parse Code Reading</h4>
<p>Workshop parse codes follow the pattern <strong>V-[Tense][Voice][Mood]-[Person][Number]</strong>:</p>
<ul>
  <li>Tense: A=Aorist, P=Present, R=Perfect, I=Imperfect, F=Future, L=Pluperfect</li>
  <li>Voice: A=Active, M=Middle, P=Passive, D=Middle/Passive (deponent)</li>
  <li>Mood: I=Indicative, S=Subjunctive, M=Imperative, O=Optative, N=Infinitive, P=Participle</li>
  <li>Person: 1=First, 2=Second, 3=Third &nbsp;|&nbsp; Number: S=Singular, P=Plural</li>
</ul>
<p>So <strong>V-AAI-3S</strong> = Verb, Aorist, Active, Indicative, 3rd Singular = "he/she/it [verb-ed]."<br>
<strong>V-PMP-NMS</strong> = Verb, Present, Middle/Passive, Participle, Nominative Masculine Singular = "the one being [verb-ed]."</p>`,

  'greek-sentence': `
<h3>Greek Sentence Structure</h3>
<h4>Word Order Is Flexible — But Not Random</h4>
<p>Unlike English (which requires Subject-Verb-Object), Greek can arrange words in almost any order because <em>case endings</em> show grammatical role. However, word order in Greek carries <strong>emphasis</strong>: moved-forward elements are stressed. The first word in a sentence or clause typically gets the most emphasis.</p>
<p>Example: "τὸν υἱὸν αὐτοῦ τὸν μονογενῆ ἔδωκεν" (John 3:16) — "his <em>only Son</em> he gave." The object (Son) is fronted for emphasis: the gift, the Son, is the point.</p>
<h4>Postpositive Particles</h4>
<p>Several Greek words <em>cannot</em> appear first in a clause despite being logically first. They are called postpositives and always appear in second position:</p>
<ul>
  <li><strong>δέ</strong> — "but/and/now" — the most common sentence connector; signals a shift or contrast.</li>
  <li><strong>γάρ</strong> — "for/because" — always explains the previous statement. "He loved us — <em>for</em> he is love."</li>
  <li><strong>οὖν</strong> — "therefore/so then" — draws an inference. "He is risen; <em>therefore</em> seek the things above."</li>
  <li><strong>μέν…δέ</strong> — "on the one hand…on the other hand" — sets up a contrast. Often left untranslated in English.</li>
</ul>
<h4>Subordinate Clauses</h4>
<ul>
  <li><strong>ἵνα + subjunctive</strong> — purpose: "that/in order that." John 3:16: "ἵνα πᾶς ὁ πιστεύων" = "in order that all who believe."</li>
  <li><strong>ὅτι</strong> — "that" (introducing content) or "because." Context determines which: "I know <em>that</em> he rose" vs. "I rejoice <em>because</em> you believed."</li>
  <li><strong>εἰ + indicative</strong> — first or second class condition (assumed true or assumed false): "If God is for us (and he is)..." vs. "If God were for us (but he's not)..."</li>
  <li><strong>ἐάν + subjunctive</strong> — third class condition (possible): "If anyone confesses his sins (he may or may not), he is faithful..."</li>
</ul>
<h4>The Genitive Absolute</h4>
<p>A dangling participial phrase in the genitive case, disconnected from the main sentence, used to set the scene: "While he was still speaking (genitive absolute), the crowd arrived." Common in narrative. Parse: genitive participle with its own noun.</p>
<h4>Articular Infinitive</h4>
<p>Greek can make an infinitive a noun by putting the article before it. τοῦ + infinitive (genitive) often expresses purpose or result. τὸ + infinitive (nominative/accusative) makes the action itself the subject or object: "To live is Christ; <em>the dying</em> is gain" (Phil 1:21).</p>`,

  'greek-particles': `
<h3>Greek Particles & Discourse Structure</h3>
<p>Greek particles are small, often untranslated words that structure argument and mark transitions. Mastering them lets you see the skeleton of Paul's logic, John's nested structure, and the Gospels' narrative flow.</p>
<h4>Connectives — How Sentences Link</h4>
<ul>
  <li><strong>καί</strong> — "and/also/even." When intensive: "even he" or "namely." John loves καί; Paul prefers δέ.</li>
  <li><strong>δέ</strong> — mild contrast or simple continuation: "but/and/now." The most flexible connector.</li>
  <li><strong>ἀλλά</strong> — strong contrast: "but/on the contrary." Paul uses ἀλλά when he means serious opposition.</li>
  <li><strong>γάρ</strong> — "for/because." Always grounds or explains. "Rejoice! <em>For</em> (γάρ) the Lord is near."</li>
  <li><strong>οὖν</strong> — "therefore/then/so." Inferential. After a doctrinal section, Paul pivots to ethics with οὖν: "Therefore (οὖν) I urge you..." (Romans 12:1).</li>
  <li><strong>εἰ μή / ἐκτὸς εἰ μή</strong> — "except/unless." Marks an exception or qualification.</li>
</ul>
<h4>Emphasis Particles</h4>
<ul>
  <li><strong>μέν</strong> — "indeed/on the one hand." Sets up a contrast with a following δέ.</li>
  <li><strong>γε</strong> — "indeed/at least/even." Adds emphasis or concession: "even so."</li>
  <li><strong>ναί / ἀμήν</strong> — "yes/verily/truly." Jesus's "Amen, amen I say to you" (double ἀμήν in John) is unique — no other rabbi introduced his own words with this formula. It's a claim to unique authority.</li>
</ul>
<h4>Reading Paul's Argument Structure</h4>
<p>Paul's letters follow a recognizable pattern. Recognizing the particles unlocks the structure:</p>
<ol>
  <li><strong>Thesis</strong> — stated as an indicative: "You have been justified by faith."</li>
  <li><strong>Objection</strong> — raised with τί οὖν or μὴ γένοιτο: "What then? Shall we sin?"</li>
  <li><strong>Rebuttal</strong> — introduced with ἀλλά or οὐδαμῶς: "By no means!"</li>
  <li><strong>Proof</strong> — using γάρ or citing Scripture: "For it is written..."</li>
  <li><strong>Inference</strong> — using οὖν or ἄρα: "Therefore no condemnation..."</li>
</ol>
<h4>Reading John's Discourse Structure</h4>
<p>John uses a spiral structure: he introduces a theme (light, life, water), develops it in narrative, then returns and deepens it. His characteristic ἀμὴν ἀμὴν ("truly, truly") always introduces a solemn, important statement. The repeated ἐγώ εἰμι (I AM) sayings deliberately echo Exodus 3:14 and Isaiah 43.</p>`,

  'greek-idioms': `
<h3>Greek Idioms & Figures of Speech</h3>
<h4>Hendiadys</h4>
<p>Two nouns joined by "and" that express one complex idea: "grace <em>and</em> truth" (χάρις καὶ ἀλήθεια, John 1:14) = gracious truth / covenant faithfulness. "Power <em>and</em> coming" (2 Pet 1:16) = powerful coming. Identifying hendiadys prevents woodenly separating two aspects of one reality.</p>
<h4>Merism</h4>
<p>Two opposites that together mean "everything": "heaven and earth" = the entire created order. "Morning and evening" = all day. "Alpha and Omega" = the complete span. Merisms lose their force if translated too literally.</p>
<h4>The Divine Passive</h4>
<p>Jewish writers avoided using God's name directly. They used passive voice to imply God as the unnamed agent: "Blessed are those who mourn, for they <em>shall be comforted</em>" — comforted by God. "Sins <em>are forgiven</em> you" — by God. Recognizing the divine passive recovers the theological weight that the passive construction carries.</p>
<h4>The Plural of Majesty vs. Trinity</h4>
<p>Hebrew אֱלֹהִים is grammatically plural but normally takes singular verbs. Genesis 1:26 "Let <em>us</em> make man" — is this the Trinity? A heavenly council? The plural of majesty? Translators must note this without resolving it prematurely.</p>
<h4>Hyperbole</h4>
<p>"If your right eye causes you to sin, tear it out." Not literal instruction — hyperbole for radical seriousness about sin. "All Judea and Jerusalem" going to John's baptism (Mark 1:5) — large numbers, not a census. Failure to recognize hyperbole produces bizarre or misleading translations.</p>
<h4>Irony & Rhetorical Questions</h4>
<p>Paul uses irony constantly in 1–2 Corinthians: "You are already rich! You have become kings!" (1 Cor 4:8) — dripping sarcasm. "Who has known the mind of the Lord?" (Rom 11:34) — expects the answer "No one." Translating irony straight produces the opposite of the intended meaning.</p>
<h4>Key Greek Idiom List</h4>
<ul>
  <li><strong>κατὰ σάρκα</strong> — "according to the flesh" = from a merely human or sinful perspective.</li>
  <li><strong>ἐν Χριστῷ</strong> — "in Christ" = union with Christ; Paul's most common expression for the Christian's position. Occurs 83× in Paul.</li>
  <li><strong>εἰς ὄνομα</strong> — "into the name" = into the ownership/allegiance of. "Baptized into the name of Jesus."</li>
  <li><strong>υἱοὶ τοῦ θεοῦ</strong> — "sons of God" — in Jewish idiom, those who share God's character or are in special relationship, not biological descent.</li>
  <li><strong>πᾶς ὁ + participle</strong> — "everyone who [does X]" — a universal conditional: "everyone who believes."</li>
</ul>`,

  'heb-alphabet': `
<h3>The Hebrew Alphabet & Vowel System</h3>
<p>Biblical Hebrew uses 22 consonants, reads <strong>right to left</strong>, and was originally written without vowels. The vowel pointing system (nikud) was added by Jewish scholars called the <strong>Masoretes</strong> between AD 500–1000, based on oral tradition. This is the text you see in your Bible — the <strong>Masoretic Text (MT)</strong>.</p>
<table class="ws-primer-table">
  <tr><th>Letter</th><th>Name</th><th>Sound</th><th>Notes</th></tr>
  <tr><td>א</td><td>Alef</td><td>silent (glottal stop)</td><td>Often silent carrier for a vowel</td></tr>
  <tr><td>ב</td><td>Bet</td><td>b / v</td><td>With dot (דָּגֵשׁ): b. Without: v</td></tr>
  <tr><td>ג</td><td>Gimel</td><td>g</td><td></td></tr>
  <tr><td>ד</td><td>Dalet</td><td>d</td><td></td></tr>
  <tr><td>ה</td><td>He</td><td>h (often silent at end)</td><td>Final ה often indicates feminine noun</td></tr>
  <tr><td>ו</td><td>Vav</td><td>v / w</td><td>Also functions as vowel letter (ō/ū)</td></tr>
  <tr><td>ז</td><td>Zayin</td><td>z</td><td></td></tr>
  <tr><td>ח</td><td>Het</td><td>ch (guttural, like Bach)</td><td>Guttural — affects surrounding vowels</td></tr>
  <tr><td>ט</td><td>Tet</td><td>t (emphatic)</td><td></td></tr>
  <tr><td>י</td><td>Yod</td><td>y / consonant i</td><td>Also vowel letter (ī)</td></tr>
  <tr><td>כ/ך</td><td>Kaf</td><td>k / kh</td><td>Final form ך. With dagesh: k. Without: kh</td></tr>
  <tr><td>ל</td><td>Lamed</td><td>l</td><td></td></tr>
  <tr><td>מ/ם</td><td>Mem</td><td>m</td><td>Final form ם</td></tr>
  <tr><td>נ/ן</td><td>Nun</td><td>n</td><td>Final form ן</td></tr>
  <tr><td>ס</td><td>Samek</td><td>s</td><td></td></tr>
  <tr><td>ע</td><td>Ayin</td><td>voiced guttural (like clearing throat)</td><td>Untranslatable to English</td></tr>
  <tr><td>פ/ף</td><td>Pe</td><td>p / f</td><td>Final form ף. With dagesh: p. Without: f</td></tr>
  <tr><td>צ/ץ</td><td>Tsade</td><td>ts (emphatic)</td><td>Final form ץ</td></tr>
  <tr><td>ק</td><td>Qof</td><td>k (emphatic, from back of throat)</td><td></td></tr>
  <tr><td>ר</td><td>Resh</td><td>r (uvular, like French r)</td><td>Guttural — cannot take dagesh</td></tr>
  <tr><td>שׂ/שׁ</td><td>Sin/Shin</td><td>s / sh</td><td>Dot on left = Sin (s); dot on right = Shin (sh)</td></tr>
  <tr><td>ת</td><td>Tav</td><td>t</td><td></td></tr>
</table>
<h4>Five Final Letters</h4>
<p>Five letters have a different form when they appear at the end of a word: כ→ך, מ→ם, נ→ן, פ→ף, צ→ץ. These are called <em>final forms</em>.</p>
<h4>The Gutturals</h4>
<p>Four letters — א, ה, ח, ע — are gutturals (formed in the throat). They resist taking certain vowel patterns and affect surrounding vowels. They cannot take a dagesh (strengthening dot). When you see unusual vowel patterns, gutturals are often the cause.</p>
<h4>Reading Without Vowels</h4>
<p>Advanced Hebrew study often uses unpointed text. The consonants alone are called the <em>ketiv</em>. Sometimes the Masoretes wrote what should be read differently from what is written — the written form (<em>ketiv</em>) vs. the reading (<em>qere</em>). The most important example: יהוה (YHWH) is always read as <em>Adonai</em> — its vowels are borrowed from Adonai as a reminder not to pronounce the Name.</p>`,

  'heb-roots': `
<h3>The Hebrew Root System</h3>
<p>This is the most foreign concept for English speakers and the most important to grasp for reading Hebrew. <strong>Almost every Hebrew word is built from a root of three consonants</strong>, and words sharing a root share a family of meaning.</p>
<h4>How It Works</h4>
<p>The root <strong>שׁ-פ-ט (Š-P-Ṭ)</strong> carries the idea of judging/governing:</p>
<ul>
  <li>שָׁפַט — to judge (verb, Qal)</li>
  <li>שֹׁפֵט — judge (noun — a person who judges; also the title of the Judges era leaders)</li>
  <li>מִשְׁפָּט — justice, judgment, ordinance (the word used for God's righteous law)</li>
</ul>
<p>When you see these three words in a passage, you know they are related. Psalm 119's multiple synonyms for God's law (מִשְׁפָּטִים, חֻקִּים, עֵדֹת, etc.) each carry distinct shades from their roots.</p>
<h4>The Root שׁ-ל-מ (Š-L-M) — Wholeness</h4>
<p>English has four words where Hebrew has one root:</p>
<ul>
  <li>שָׁלֵם — to be complete, whole, at peace</li>
  <li>שָׁלוֹם — peace, wholeness, well-being (more than absence of conflict)</li>
  <li>שִׁלֵּם — to repay, make restitution (restore to wholeness)</li>
  <li>שָׁלְמָה — Salma/Solomon — "his peace"</li>
  <li>יְרוּשָׁלַיִם — Jerusalem — possibly "city of wholeness/peace"</li>
</ul>
<h4>Using the Root in the Workshop</h4>
<p>In each dossier entry, the Strong's code links to a lemma. The lemma is usually the simplest verb form (Qal infinitive or perfect). From there, BDB will show you the root (marked with a dagger †) and related words. Reading these connections reveals the semantic field — the family of meaning — around every word.</p>
<h4>Weak Roots</h4>
<p>Roots where one of the three consonants is a guttural (א,ה,ח,ע), a ו, or a י are called <em>weak roots</em> and behave irregularly. The most common weak root changes:</p>
<ul>
  <li>Roots with initial י (Pe-Yod): the י often drops in certain forms. יָלַד (to bear/beget) → הוֹלִיד (Hiphil).</li>
  <li>Roots with ו or י as middle radical (Ayin-Vav/Yod): the middle radical becomes a vowel in many forms. קוּם (to rise) → יָקוּם.</li>
  <li>Roots with identical second and third consonants (Ayin-Ayin): סָבַב (to turn/surround).</li>
</ul>`,

  'heb-binyanim': `
<h3>Hebrew Verb Stems — The Binyan System</h3>
<p>The binyanim (singular: binyan) are the seven grammatical stem patterns applied to any root. The same root through different binyanim produces related but distinct meanings. This is the most powerful — and most foreign — aspect of Hebrew grammar.</p>
<table class="ws-primer-table">
  <tr><th>Binyan</th><th>Function</th><th>Example (root ק-ד-שׁ, holiness)</th><th>Translation</th></tr>
  <tr><td><strong>Qal</strong></td><td>Simple active — the basic meaning</td><td>קָדַשׁ</td><td>to be holy</td></tr>
  <tr><td><strong>Niphal</strong></td><td>Simple passive or reflexive</td><td>נִקְדַּשׁ</td><td>to be sanctified / to sanctify oneself</td></tr>
  <tr><td><strong>Piel</strong></td><td>Intensive/causative active; often factitive (makes something what the Qal simply is)</td><td>קִדֵּשׁ</td><td>to consecrate / to sanctify (another)</td></tr>
  <tr><td><strong>Pual</strong></td><td>Passive of Piel</td><td>קֻדַּשׁ</td><td>to be consecrated</td></tr>
  <tr><td><strong>Hiphil</strong></td><td>Causative active</td><td>הִקְדִּישׁ</td><td>to cause to be holy / to treat as holy / to declare holy</td></tr>
  <tr><td><strong>Hophal</strong></td><td>Causative passive</td><td>הָקְדַּשׁ</td><td>to be caused to be holy</td></tr>
  <tr><td><strong>Hithpael</strong></td><td>Reflexive of Piel; sometimes reciprocal or iterative</td><td>הִתְקַדֵּשׁ</td><td>to sanctify oneself; to show oneself holy</td></tr>
</table>
<h4>Why This Matters for Translation</h4>
<p>Translating "God <strong>qidesh</strong> the Sabbath" (Piel) and "God <strong>qadash</strong>" (Qal) are different claims. The Piel means God actively <em>made</em> the Sabbath holy — a creative act of consecration. The Qal would say God simply <em>is</em> or <em>was</em> holy. Getting the binyan right is getting the theological claim right.</p>
<h4>The Hiphil and Causative Theology</h4>
<p>Many key theological verbs appear in the Hiphil when describing God's acts:</p>
<ul>
  <li>הֶאֱמִין (Hiphil of אמן) — to cause faith, to trust — this is the word in Genesis 15:6: "Abraham trusted [Hiphil] God."</li>
  <li>הִצְדִּיק (Hiphil of צדק) — to justify/declare righteous. This is a legal, declarative act — not "make righteous" but "declare to be in the right." The same Hiphil nuance is crucial for Paul's doctrine of justification.</li>
  <li>הוֹשִׁיעַ (Hiphil of ישׁע) — to save/deliver. The root from which יֵשׁוּעַ (Jesus/Yeshua/Joshua) comes: "the one who causes salvation."</li>
</ul>
<h4>Parse Codes for Hebrew Verbs</h4>
<p>Interlinear parse codes for Hebrew verbs follow: <strong>[Binyan]-[Stem Form]-[Person][Gender][Number]</strong></p>
<ul>
  <li>Qal-PERF-3MS = Qal Perfect, 3rd person masculine singular = "he [did]"</li>
  <li>Piel-IMPF-1CP = Piel Imperfect, 1st person common plural = "we will [intensively do]"</li>
  <li>Hiphil-PTCP-MS = Hiphil Participle, masculine singular = "the one who causes [x]"</li>
</ul>`,

  'heb-sentence': `
<h3>Hebrew Sentence Structure</h3>
<h4>The Typical Word Order: Verb First</h4>
<p>Biblical Hebrew narrative typically follows <strong>Verb-Subject-Object</strong> order — opposite to English. "And he said God…" in Hebrew becomes "And God said…" in English. The verb leading is the default narrative stance.</p>
<h4>The Waw-Consecutive — The Engine of Hebrew Narrative</h4>
<p>The most important grammatical feature for reading Hebrew narrative is the <strong>waw-consecutive</strong> (also called waw-conversive). A ו (waw = "and") prefixed to an imperfect verb form often carries perfective meaning — it narrates a sequence of completed past actions:</p>
<p style="background:var(--color-surface);padding:.5rem .75rem;border-radius:4px;font-style:italic">"And he said (וַיֹּאמֶר)… and he went (וַיֵּלֶךְ)… and he saw (וַיַּרְא)…" — Genesis narrative rolls forward in sequence.</p>
<p>This is why Genesis 1 is not: "In the beginning, God <em>will create</em>." The waw-consecutive turns what looks like an imperfect verb into past narrative. English translations flatten this into simple past tense, hiding the grammatical driving force of the story.</p>
<h4>Verb-Subject Agreement</h4>
<p>Hebrew verbs agree with their subject in person, gender, and number. Collective nouns (like עַם, "people") can take either singular or plural verbs. When a plural subject takes a singular verb (or vice versa), it is usually theologically significant: "The LORD your God, the LORD is <em>one</em>" — the oneness of God expressed in singular predication.</p>
<h4>The Construct Chain (Smikut)</h4>
<p>Hebrew expresses "X of Y" by placing X in the <em>construct state</em> directly before Y, with no word for "of." The construct noun loses its definite article and sometimes changes its form:</p>
<ul>
  <li>דְּבַר יהוה — "word of the LORD" (not הַדָּבָר but דְּבַר)</li>
  <li>בֵּית לֶחֶם — "house of bread" = Bethlehem</li>
  <li>מֶלֶךְ מְלָכִים — "king of kings"</li>
  <li>קֹדֶשׁ הַקֳּדָשִׁים — "holy of holies" = the most holy place (superlative using a construct of a noun with itself)</li>
</ul>
<p>The construct chain is often used for the Hebrew superlative: "song of songs" = the greatest song; "vanity of vanities" = absolute emptiness.</p>
<h4>Fronting for Emphasis</h4>
<p>When a non-verb element appears <em>before</em> the verb, it receives emphasis — the opposite of default VSO order. "In the beginning <em>God</em> created" — אֱלֹהִים comes after the temporal phrase but before the verb, emphasizing that it was specifically <em>God</em> who acted.</p>`,

  'heb-poetry': `
<h3>Hebrew Poetry — How to Read It</h3>
<p>Roughly one-third of the Old Testament is poetry: all of Psalms, Proverbs, Job, Song of Solomon, Lamentations, and large portions of the Prophets. Hebrew poetry is not rhyme-based — it works through <strong>parallelism</strong>, <strong>imagery</strong>, and <strong>rhythm</strong>.</p>
<h4>The Three Types of Parallelism</h4>
<p>The defining feature of Hebrew poetry is that lines pair with each other in structured relationships:</p>
<ul>
  <li><strong>Synonymous parallelism</strong> — the second line restates the first in different words: "The LORD is my shepherd / I shall not want." (Ps 23:1) The repetition is <em>not</em> redundancy — it deepens and focuses. The second line often advances or specifies the first.</li>
  <li><strong>Antithetic parallelism</strong> — the second line contrasts with the first: "A wise son makes a glad father / but a foolish son is a sorrow to his mother." (Prov 10:1) Common in Proverbs.</li>
  <li><strong>Synthetic parallelism</strong> — the second line completes or extends the first: "He is like a tree planted by streams of water / that yields its fruit in its season." (Ps 1:3) The second line adds new content.</li>
</ul>
<h4>Chiasm — The Architectural Structure</h4>
<p>Hebrew (and sometimes Greek) thought structures material in mirror patterns: <strong>A B C B' A'</strong>. The central element (C) is the main point; the outer elements frame it. Recognizing chiasm often unlocks the meaning of a passage:</p>
<p style="background:var(--color-surface);padding:.5rem .75rem;border-radius:4px">
  A — "Blessed is the man who walks not in the counsel of the wicked"<br>
  B — "nor stands in the way of sinners"<br>
  C — "nor sits in the seat of scoffers"<br>
  B' — "but his delight is in the law of the LORD"<br>
  A' — "and on his law he meditates day and night" (Ps 1:1-2)
</p>
<h4>Acrostic Poems</h4>
<p>Several Psalms and the whole of Lamentations are acrostics — each verse or stanza begins with the next letter of the Hebrew alphabet. Psalm 119 has 176 verses, 8 verses per letter, 22 stanzas. This conveys completeness (A to Z of devotion to God's word) and is a mnemonic device. English translations cannot reproduce this without footnotes.</p>
<h4>Imagery and Metaphor</h4>
<p>Hebrew poetry is concrete and physical — it thinks in images, not abstractions. "The LORD is my <em>rock</em>" is not saying God is rocklike; it's saying he is the rock behind you when enemies come. "Lovingkindness reaches to the heavens" — not metaphysics, but spatial awe. Translators must preserve the image, not replace it with the abstraction the image implies.</p>
<h4>Lament Structure</h4>
<p>The most common Psalm genre is the <strong>individual lament</strong>, following a predictable structure: (1) Address to God, (2) Complaint, (3) Confession of trust, (4) Petition, (5) Vow of praise. Many Psalms make no sense until you recognize the genre — they are not doctrinal statements but prayers in extremis, and their raw honesty is intentional.</p>`,

  'heb-idioms': `
<h3>Hebrew Idioms & Body Language</h3>
<p>Biblical Hebrew thinks concretely through the body. Abstract concepts are expressed through physical, embodied language. Understanding these idioms is essential — translating them literally produces nonsense; ignoring them loses the depth.</p>
<h4>Heart (לֵב / לֵבָב)</h4>
<p>In English, the heart is the seat of emotion. In Hebrew, <strong>לֵב</strong> is the seat of the <em>mind, will, and intention</em> — what we'd call the inner person or the rational soul. "With all your heart" (Deut 6:5) = with your whole mind, will, and being. "His heart was not fully devoted" = his commitment/intention was divided. "God looks at the heart" = God evaluates intention, not appearance. Translating "heart" as emotion alone misses the Hebrew meaning.</p>
<h4>Hand (יָד)</h4>
<p><strong>יָד</strong> (hand) = power, agency, control. "Into his hand" = into his power. "The hand of the LORD" = God's direct action. "Under his hand" = under his authority. "He stretched out his hand" = he acted with power. "A high hand" = arrogance, defiance. The hand is agency personified.</p>
<h4>Face (פָּנִים)</h4>
<p><strong>פָּנִים</strong> (face, always plural in Hebrew) = presence, favor, or anger. "Before his face" = in his presence. "Seek his face" = seek his presence/favor. "His face was set against them" = he opposed them. The Aaronic blessing: "The LORD make his face shine upon you" = may he look on you with favor. "He hid his face" = he withdrew his favor/attention.</p>
<h4>Bowels / Kidneys (מֵעִים / כְּלָיוֹת)</h4>
<p>These are the Hebrew seat of emotion — what English calls "heart-feeling." When Joseph "was moved in his bowels" (Gen 43:30, KJV) = he felt deep emotion, compassion. God's "tender mercies" (רַחֲמִים) comes from רֶחֶם (womb) — maternal compassion. The NLT "I yearn for him with all my heart" translates what Hebrew says as "my bowels churn for him."</p>
<h4>Common Idioms</h4>
<ul>
  <li><strong>"To know" (יָדַע) someone</strong> — intimate, relational knowing; sometimes euphemism for sexual union (Gen 4:1). "I never knew you" (Matt 7:23, Hebrew idiom through Greek) = I had no covenant relationship with you.</li>
  <li><strong>"To find grace/favor in the eyes of"</strong> — חֵן in someone's eyes = to be approved by, welcomed by.</li>
  <li><strong>"To lift up the face"</strong> — to show favor, accept. "To fall on the face" = submission, worship, terror.</li>
  <li><strong>"A stiff neck"</strong> (עֹרֶף קָשֶׁה) — stubbornness, refusal to bow to God's yoke.</li>
  <li><strong>"Uncircumcised lips/ears"</strong> — unable to function properly; Moses: "I am of uncircumcised lips" = I cannot speak fluently.</li>
  <li><strong>"To eat bread"</strong> — to share a meal = to enter covenant relationship. Eating with someone is covenantal.</li>
  <li><strong>Day and night / morning and evening</strong> — merism for "always, completely."</li>
</ul>`,

  'world-honor': `
<h3>Honor & Shame Culture — The Social World of the Bible</h3>
<p>The biblical world was an <strong>honor-shame culture</strong>, not the guilt-innocence culture of modern Western individualism. This affects almost everything — family structure, social interaction, the nature of sin, the meaning of forgiveness, and why Jesus's actions were so scandalous.</p>
<h4>What Honor Means</h4>
<p>In the ancient Mediterranean, <strong>honor</strong> (Greek: τιμή; Hebrew: כָּבוֹד) was the most valuable social currency. It was your public reputation — what your community said about you. Everything was done publicly, before an audience. Shame was not just guilt — it was <em>public disgrace</em>. You were your community's assessment of you, not your private self-image.</p>
<h4>Patron-Client Relations</h4>
<p>Society was organized vertically through patron-client networks. A <em>patron</em> had resources and status; a <em>client</em> had loyalty and service. The patron gave beneficia (gifts, protection, access); the client gave gratitude, loyalty, and public honor. This is the social background of:</p>
<ul>
  <li><strong>Grace (χάρις)</strong> — a patron's gift, expected to create loyal clients. Paul's subversion: God's grace creates loyalty not through obligation but through love.</li>
  <li><strong>Debt/forgiveness</strong> — cancelling a social debt meant releasing someone from patronal obligation. "Forgive us our debts" is socioeconomically concrete.</li>
  <li><strong>The prodigal son</strong> — the son has shamed the father publicly. The father running to meet him (undignified for a patriarch) is an act of absorbing the son's shame before the village can respond.</li>
</ul>
<h4>Purity & Pollution</h4>
<p>Ancient societies maintained sharp boundaries between clean and unclean, insider and outsider. Eating with sinners (Mark 2:16) was not just bad social etiquette — it was a statement about identity boundaries. Jesus eating with tax collectors was a public challenge to the entire social mapping of holiness.</p>
<h4>The Crucifixion as Shame</h4>
<p>Crucifixion was designed to maximize shame — public, naked, on a roadside, with a criminal's titulus. The early church's proclamation of "a crucified Messiah" was, to both Jews and Greeks, a claim about someone utterly dishonored. Paul's "word of the cross is foolishness" (1 Cor 1:18) is not rhetorical — it was literally scandalous. Hebrews 12:2: Jesus "endured the cross, <em>despising the shame</em>."</p>`,

  'world-covenant': `
<h3>Covenant & Treaty Forms</h3>
<p>The Hebrew word בְּרִית (covenant, H1285) is the organizing concept of the entire Bible. The two-testament structure is itself covenantal: Old Covenant / New Covenant. Understanding what a covenant was in the ancient world transforms how you read both Testaments.</p>
<h4>The Ancient Near Eastern Suzerainty Treaty Form</h4>
<p>Scholars have identified that God's covenant at Sinai (and the book of Deuteronomy as a whole) follows the structure of Hittite suzerainty treaties — the great king's treaty with vassal nations:</p>
<ol>
  <li><strong>Preamble</strong> — identifying the great king: "I am the LORD your God..."</li>
  <li><strong>Historical prologue</strong> — recounting what the king has done: "...who brought you out of Egypt."</li>
  <li><strong>Stipulations</strong> — the treaty's requirements: the Ten Commandments / the law.</li>
  <li><strong>Deposit & reading</strong> — the treaty is written and read periodically.</li>
  <li><strong>Witnesses</strong> — heaven and earth called as witnesses (Deut 32).</li>
  <li><strong>Blessings and curses</strong> — consequences for faithfulness or breach (Deut 28–29).</li>
</ol>
<p>Recognizing this structure shows that the Law is not a means of earning salvation but a <em>response</em> to prior grace (the exodus comes before Sinai) — structured exactly like a vassal's grateful loyalty to a king who freed them.</p>
<h4>Blood Covenant</h4>
<p>The cutting of animals (Gen 15) was a standard ancient covenant ratification ceremony. The parties walked between the cut pieces, saying: "May what was done to these animals be done to me if I break this covenant." In Genesis 15, God alone passes through — the covenant is unconditional, unilateral. Abraham does not walk through; God binds himself alone.</p>
<h4>Covenant Vocabulary to Know</h4>
<ul>
  <li><strong>חֶסֶד</strong> — the loyal love owed within a covenant relationship; what the stronger party owes the weaker.</li>
  <li><strong>אֱמֶת</strong> — faithfulness, reliability; covenant keeping in practice.</li>
  <li><strong>שָׁלוֹם</strong> — the wholeness that a functioning covenant produces.</li>
  <li><strong>עֵד</strong> — witness to a covenant.</li>
  <li><strong>כָּרַת בְּרִית</strong> — "to cut a covenant" — the standard idiom for making one.</li>
</ul>`,

  'world-secondtemple': `
<h3>Second Temple Judaism</h3>
<p>The <strong>Second Temple period</strong> (roughly 516 BC to AD 70) is the world Jesus and Paul lived in. The NT cannot be understood without knowing the Jewish religious landscape of this period — the parties, their debates, their expectations, and the literature they wrote.</p>
<h4>The Main Groups</h4>
<ul>
  <li><strong>Pharisees</strong> — committed to applying the Torah to all of life through an "oral Torah" — interpretive traditions that fenced the written law. Believed in resurrection, angels, and divine providence. Jesus debates them constantly because they share much common ground. Paul was a Pharisee (Phil 3:5).</li>
  <li><strong>Sadducees</strong> — priestly aristocracy controlling the Temple. Accepted only the Pentateuch as authoritative. Rejected resurrection, angels, and most supernatural elements. Pro-Roman politically. Died out after AD 70 when the Temple was destroyed.</li>
  <li><strong>Essenes</strong> — separatist purity movement, likely the community at Qumran (Dead Sea Scrolls). Believed the Jerusalem priesthood was corrupt. Practiced ritual bathing, held property in common, awaited two messiahs and an eschatological war.</li>
  <li><strong>Zealots</strong> — Jewish revolutionaries who believed the Kingdom would only come through military uprising against Rome. Their movement led to the Jewish War (AD 66–70) and the Temple's destruction.</li>
</ul>
<h4>Messianic Expectations</h4>
<p>First-century Jews expected multiple things from a "messiah" (anointed one): a Davidic king who would restore the kingdom, a priestly figure who would purify worship, a prophet like Moses who would give new Torah, or an apocalyptic "son of man" figure from Daniel 7. Jesus confounds all of these expectations simultaneously — which is why both his followers and opponents were confused about who he was.</p>
<h4>The Dead Sea Scrolls</h4>
<p>Discovered in 1947, the DSS (100 BC to AD 70) contain the oldest Hebrew OT manuscripts (1000 years older than the Masoretic Text) and the Qumran community's own writings. Key findings for translators:</p>
<ul>
  <li>The Masoretic Text is largely confirmed as reliable.</li>
  <li>Some passages in the DSS align with the Septuagint (LXX) where the MT differs — important for textual criticism.</li>
  <li>The Qumran community's pesher (commentary) method shows how Jews read scripture eschatologically — applying OT texts to their own present moment. This is exactly how the NT authors read the OT.</li>
</ul>`,

  'world-roman': `
<h3>The Roman Imperial World</h3>
<p>The NT was written under Roman domination. Understanding Rome is not optional background — it shapes the meaning of key NT words and the stakes of the early Christian proclamation.</p>
<h4>The Imperial Cult</h4>
<p>Augustus Caesar was declared "Son of God" (divi filius), "Lord" (Kyrios/Dominus), and "Savior" (Soter) after Julius Caesar's deification. When Paul announces "Jesus is Lord" or calls the gospel εὐαγγέλιον (good news — a word used for announcements of imperial victories and births), he is making a political claim. The early Christians' refusal to say "Caesar is Lord" was the primary reason for persecution — it was sedition.</p>
<h4>Key Terms Hijacked from Imperial Language</h4>
<ul>
  <li><strong>εὐαγγέλιον (gospel)</strong> — announcements of military victories, the emperor's birthday, his accession. Paul takes this imperial proclamation genre and redirects it: "the gospel of God" (not Caesar).</li>
  <li><strong>κύριος (Lord)</strong> — Caesar's title. "Jesus is Lord" is the earliest Christian creed and a direct counter-claim.</li>
  <li><strong>σωτήρ (Savior)</strong> — attributed to emperors who brought peace (Pax Romana). The NT's "Savior" language claims Jesus does what emperors claimed to do — but actually accomplishes it.</li>
  <li><strong>παρουσία (coming/presence)</strong> — the technical term for an emperor's royal visit to a city. Paul uses it for Christ's return — a coming of a true King, eclipsing imperial visits.</li>
  <li><strong>ἐκκλησία (church)</strong> — the civic assembly of free male citizens. Paul calls his communities by this civic, political term — counter-assemblies to Rome's assemblies.</li>
</ul>
<h4>Slavery</h4>
<p>Estimates suggest 30-40% of Italy's population were enslaved in the first century. Paul's letters are full of slave/master language that had enormous social weight. "Slave of Christ" (δοῦλος Χριστοῦ) — which most translations soften to "servant" — was a claim of radical belonging and also a paradoxical honor: belonging to the highest Lord.</p>`,

  'world-ant': `
<h3>The Ancient Near Eastern World</h3>
<p>The OT did not fall from the sky — it was written to people in a specific cultural world shared with Babylon, Egypt, Canaan, and Assyria. Understanding that world explains why Genesis is written the way it is, why Leviticus has the laws it has, and why the Prophets use the imagery they do.</p>
<h4>Creation Accounts</h4>
<p>Genesis 1 shares vocabulary and themes with Mesopotamian creation texts (Enuma Elish) and Egyptian creation theology — but systematically subverts them. Where Babylon's gods create humans as slaves to feed the gods, Genesis's God creates humans in his image to rule with him. The subversion is the point: Genesis is not borrowed mythology but a polemical counter-narrative.</p>
<h4>The Flood Accounts</h4>
<p>Flood narratives exist across many ancient cultures (Gilgamesh Epic, Atrahasis). The biblical account shares the basic structure but differs theologically: the cause (human sin vs. divine capriciousness), the hero's character, and the covenant outcome are all distinctive.</p>
<h4>Sacrifice and the Tabernacle</h4>
<p>Israel's sacrificial system is not unique in its form — sacrifices, priests, and sanctuaries existed throughout the ANE. What is unique is the <em>theological framework</em>: the God who does not need food, who cannot be manipulated by ritual, who forgives based on grace with sacrifice as the appointed vehicle. Leviticus only makes sense against the ANE background it is responding to.</p>
<h4>Covenant as Treaty (see Covenant section)</h4>
<p>The suzerainty treaty form (see Covenant & Treaty Forms section) was common in the Hittite and Assyrian worlds. God speaking Israel's covenantal language does not diminish its authority — it maximizes communication. The form was chosen to be unmistakably clear to its original audience.</p>`,

  'tr-philosophy': `
<h3>Translation Philosophy</h3>
<h4>The Fundamental Tension</h4>
<p>Every translation involves two competing loyalties: <strong>loyalty to the source</strong> (accuracy, precision, faithfulness to the original) and <strong>loyalty to the reader</strong> (clarity, naturalness, communicability). You cannot maximize both simultaneously. Every translation choice trades one for the other.</p>
<h4>Formal Equivalence (Word-for-Word)</h4>
<p>Attempts to represent each source word with a consistent English word, preserving source language structure as much as possible. The reader needs to do interpretive work. Examples: NASB, ESV, KJV, Young's Literal. Best for: word studies, teaching, verse-by-verse preaching where the specific words matter.</p>
<h4>Dynamic Equivalence (Thought-for-Thought)</h4>
<p>Translates the meaning of each phrase or sentence into natural English, even if individual words do not correspond. The translator does the interpretive work. Examples: NLT, GNB, CEV. Best for: first-time Bible readers, cross-cultural mission, communicating meaning without assuming biblical literacy.</p>
<h4>Functional Equivalence (the Middle)</h4>
<p>Attempts accuracy at the phrase level, aiming for natural English without overly paraphrasing. Most modern translations: NIV, CSB, NET. The NET Bible includes extensive translation notes explaining thousands of interpretive choices — invaluable for understanding where translations diverge.</p>
<h4>The Concordance Debate</h4>
<p>Should you translate the same Greek/Hebrew word with the same English word every time? The NASB and ESV aim for this. The advantage: readers can trace word usage. The disadvantage: one English word rarely covers a Greek/Hebrew word's full range — concordance forces a single-sense reading onto a polysemous word. MKT aims for <em>principled consistency</em>: the same primary rendering in similar contexts, with documented departures for specific reasons.</p>
<h4>The Meaning Unit Question</h4>
<p>What is the unit of translation? A word? A phrase? A sentence? A discourse unit? Formal equivalence translates word by word. Dynamic equivalence translates discourse units. The right unit depends on the passage: poetry requires attention to image and rhythm; narrative can be phrase-level; legal material requires precision at the word level.</p>`,

  'tr-polysemy': `
<h3>One Word, Many Meanings</h3>
<p>The glossary's "primary" rendering is a <em>default</em> — what the translation script uses when no context override applies. For theologically dense vocabulary, forcing one English word across all occurrences is wrong.</p>
<h4>Case Studies</h4>
<p><strong>σάρξ (G4561) — flesh / body / sinful nature</strong><br>
John 1:14: "The Word became flesh" — physical human nature, nothing morally loaded. Romans 7–8 and Galatians 5: the fallen human drive opposing the Spirit. 1 Corinthians 15:50: physical material existence. <em>No single English word covers all three.</em> Use context overrides for the Romans/Galatians usage.</p>
<p><strong>רוּחַ (H7307) — spirit / Spirit / wind / breath</strong><br>
Genesis 1:2: "the Spirit/wind/breath of God over the waters" — the ambiguity may be intentional. Ezekiel 37:9: Come from the four winds, O breath/Spirit — all three meanings simultaneously. Capitalisation is a translation decision, not a grammatical fact.</p>
<p><strong>חֶסֶד (H2617) — steadfast love / lovingkindness / mercy / loyalty</strong><br>
There is no English word for חֶסֶד. It combines loyalty, covenant faithfulness, and active kindness. "Mercy" is too weak. "Love" too general. "Steadfast love" (ESV) captures constancy but loses covenantal weight. Your Thought-tier rendering may expand to "covenant faithfulness" in some contexts and "tender loyalty" in others.</p>
<h4>Using Context Overrides</h4>
<ol>
  <li>Set the primary rendering for the majority of occurrences.</li>
  <li>Add overrides for specific books, genres, or syntactic constructions where the word clearly means something different.</li>
  <li>Document your reasoning in the decision log.</li>
  <li>Use the Thought tier for meaning-driven renderings of idioms and rich terms.</li>
</ol>`,

  'tr-genre': `
<h3>Genre & How to Read Each Type</h3>
<p>The most important interpretive question for any Bible passage is: <em>what kind of text is this?</em> Genre determines the rules of interpretation. Reading apocalyptic as straightforward history, or narrative as if it were law, produces serious misreadings.</p>
<h4>Narrative (Genesis–Esther, Gospels, Acts)</h4>
<p>Narrative shows rather than tells. It selects and arranges events to make theological points, but does not always make those points explicit. The narrator's perspective is implicit. Translation principle: preserve the narrative's concreteness and pace; don't add interpretive commentary the narrator withheld.</p>
<h4>Law (Exodus–Deuteronomy sections)</h4>
<p>Ancient Near Eastern law collections (Hammurabi, etc.) used case law: "if X, then Y." Hebrew law does the same. <strong>Apodictic law</strong> (absolute: "You shall not murder") and <strong>casuistic law</strong> (conditional: "If a man does X, then...") work differently. Translation must preserve the form because the form is part of the meaning.</p>
<h4>Prophecy</h4>
<p>Hebrew prophecy is primarily <em>forth-telling</em> (announcing God's word to the present situation) and secondarily <em>fore-telling</em> (announcing future events). Prophetic poetry uses images, not precise prediction schedules. The "fulfillment" language in the NT is often typological — the OT pattern is completed and surpassed — not always predictive prophecy. "This happened <em>to fulfill</em>" (Matthew) often means "this is what that was pointing to."</p>
<h4>Wisdom (Proverbs, Job, Ecclesiastes, Song of Solomon)</h4>
<p>Proverbs are generalizations, not guarantees: "Train up a child in the way he should go; even when he is old he will not depart from it" — a tendency, not an absolute promise. Job deconstructs simplistic retribution theology. Ecclesiastes is a philosophical exploration, not Solomonic heresy. The Song of Solomon is erotic poetry — treat it as such.</p>
<h4>Psalms — A Special Case</h4>
<p>The Psalms are Israel's prayer book — they model honest speech to God, not propositional doctrine about God. Imprecatory Psalms (calling down judgment on enemies) are prayers, not commandments. They must be translated preserving the rawness of the lament, not softened into polite petitions.</p>
<h4>Epistles (Paul, Peter, John, James, Hebrews)</h4>
<p>Real letters written to real communities addressing specific problems. The "occasional" nature means we only hear one side of the conversation. Translators must be careful not to over-systematize what was situational response. Paul's instructions about women in 1 Corinthians 14 and 1 Timothy 2 are applied to specific community problems; the translation must preserve what the text says, not what we wish it said.</p>
<h4>Apocalyptic (Daniel, Revelation, portions of Ezekiel and Zechariah)</h4>
<p>Apocalyptic is a specific genre with conventions: heavenly visions, symbolic numbers, beasts representing empires, cosmic conflict behind earthly events. <strong>The images are not meant to be decoded literally.</strong> The number 666 is symbolic (numerical value of Nero Caesar in Hebrew gematria, in one major interpretation). "The beast from the sea" is a power system, not a literal monster. Translation: preserve the symbolic language; resist the urge to decode in footnotes.</p>`,

  'tr-intertextuality': `
<h3>Intertextuality & the Septuagint</h3>
<p>The New Testament authors were thoroughly Jewish scholars who read, memorized, and interpreted the Old Testament. Understanding <em>how</em> they read it is essential for translating what they wrote.</p>
<h4>The Septuagint (LXX)</h4>
<p>The Greek translation of the Hebrew OT, made in Alexandria roughly 250–100 BC. When NT authors quote the OT, they overwhelmingly quote the <strong>LXX</strong>, not the Hebrew. This matters for translators because:</p>
<ul>
  <li>Some NT quotes don't match the Hebrew OT (MT) — they match the LXX. Matthew 1:23 quotes Isaiah 7:14 using the LXX's παρθένος (virgin) where the Hebrew uses עַלְמָה (young woman).</li>
  <li>The LXX's translation choices shaped the NT's vocabulary. ἐκκλησία (church) comes from the LXX's translation of קָהָל (assembly). The NT's use of ἱλαστήριον (propitiation/mercy seat) comes from its LXX usage.</li>
  <li>Paul's argument in Romans 4 (Abraham justified before circumcision) depends on the LXX and the MT agreeing on the Genesis sequence.</li>
</ul>
<h4>Four Ways the NT Uses the OT</h4>
<ul>
  <li><strong>Direct quotation</strong> — explicit "it is written" formulas. The easiest to identify.</li>
  <li><strong>Allusion</strong> — deliberate evocation without explicit quotation. John 1:1 ("In the beginning") alludes to Genesis 1:1 with no quote marker. Hebrews is built almost entirely of allusions.</li>
  <li><strong>Typology</strong> — an OT person, event, or institution is a "type" (prefiguration) fulfilled by the NT antitype. Adam → Christ (Romans 5). The Exodus → Baptism (1 Cor 10). The Tabernacle → Christ's body (Hebrews). Typology is not allegory — it argues that history itself has a pattern.</li>
  <li><strong>Analogy</strong> — the OT principle applies in a new situation. James on prayer (James 5:17) uses Elijah as an example of effective prayer, not as a type of Christ.</li>
</ul>
<h4>Pesher Interpretation</h4>
<p>The Qumran community (and early Christians) used <em>pesher</em> — "this means that" — interpretation, applying OT texts to their own immediate situation. "This is that which was spoken by the prophet Joel" (Acts 2:16). The NT authors believed they were living in the fulfillment of the OT story. This shapes their entire reading practice.</p>`,

  'tr-textcrit': `
<h3>Textual Criticism</h3>
<p>We do not have the original manuscripts (autographs) of any biblical book. What we have are thousands of handwritten copies (manuscripts) made over 1500 years. <strong>Textual criticism</strong> is the science of determining what the original text most likely said, by comparing manuscript evidence.</p>
<h4>The Good News</h4>
<p>The NT is by far the best-attested ancient text — over 5,800 Greek manuscripts, plus translations into Latin, Syriac, Coptic, etc. Homer's Iliad has ~1,800 manuscripts; Caesar's Gallic Wars has ~10. The sheer volume of NT manuscripts means variants are easy to identify and evaluate.</p>
<h4>Manuscript Families</h4>
<ul>
  <li><strong>Alexandrian</strong> — oldest and generally most accurate family. Manuscripts: Papyrus 66, Papyrus 75, Codex Sinaiticus (א), Codex Vaticanus (B). Used by NA28/UBS5 (the standard critical Greek text) and most modern translations (ESV, NIV, NASB).</li>
  <li><strong>Byzantine</strong> — later, numerous, and the basis for the <em>Textus Receptus</em> (received text) behind the KJV and NKJV. Not as old but represents broad early church usage.</li>
  <li><strong>Western</strong> — distinctive readings, sometimes longer. Codex Bezae (D). Often paraphrastic expansions.</li>
</ul>
<h4>Key Variants to Know</h4>
<ul>
  <li><strong>Mark 16:9–20</strong> — the "longer ending" is absent from Sinaiticus and Vaticanus. Most scholars believe it was added later. Critical editions bracket it.</li>
  <li><strong>John 7:53–8:11</strong> — the woman caught in adultery. Absent from the earliest manuscripts, appears in different locations in different manuscripts. Almost certainly not original to John.</li>
  <li><strong>1 John 5:7</strong> — the Comma Johanneum ("the Father, the Word, and the Holy Ghost, and these three are one") — present in only a handful of very late Latin manuscripts. Not original. KJV included it; modern translations bracket or footnote.</li>
  <li><strong>Romans 16:24</strong>, <strong>Acts 8:37</strong> — present in TR/KJV, absent from critical editions.</li>
</ul>
<h4>Principles for Evaluating Variants</h4>
<ul>
  <li><strong>Prefer the harder reading</strong> — scribes tended to smooth difficulties, not create them. The more difficult reading is usually original.</li>
  <li><strong>Prefer the shorter reading</strong> — scribes tended to add explanations, not remove content.</li>
  <li><strong>Prefer the reading that explains the others</strong> — if one reading could produce all the variants, it is likely original.</li>
  <li><strong>External evidence matters</strong> — earlier manuscripts, geographically diverse agreement, agreement of independent traditions.</li>
</ul>`,

  'tr-method': `
<h3>Exegetical Method — How to Approach a Passage</h3>
<p>Exegesis means "drawing out" — discovering what the text actually says in its original context. Eisegesis means "reading in" — importing your own assumptions. Good translation requires rigorous exegesis first.</p>
<h4>Step 1: Establish the Text</h4>
<p>Check the textual apparatus. Are there significant variants in this passage? If so, which reading has the best manuscript support? Note any variants in the dossier's decision log.</p>
<h4>Step 2: Translate Word by Word</h4>
<p>Use the interlinear. Parse every verb — tense, voice, mood, person, number. Identify every case — why is this noun genitive? Dative? Look up every word you are not certain about in Thayer (Greek) or BDB (Hebrew). Do not rush this step.</p>
<h4>Step 3: Identify the Sentence Structure</h4>
<p>Diagram the relationships: What is the main verb? What are the subordinate clauses? Where are the participles and what do they modify? In Paul especially, one sentence can run for multiple verses (Ephesians 1:3–14 is one Greek sentence). Identifying the main verb and the subordinate structures reveals the argument's spine.</p>
<h4>Step 4: Identify the Genre</h4>
<p>Is this narrative, law, prophecy, wisdom, epistle, apocalyptic? (See Genre section.) The genre determines the interpretive rules. Do not apply prose rules to poetry, or legal precision to narrative generalization.</p>
<h4>Step 5: Investigate the Historical-Cultural Context</h4>
<p>Who wrote this? To whom? When? What was the occasion? What would the original audience have understood? Commentaries (JFB, Barnes, Matthew Henry, Calvin) are your friends here — they bring centuries of accumulated contextual knowledge.</p>
<h4>Step 6: Identify Intertextual Connections</h4>
<p>Is the author quoting the OT? Alluding to it? Using typology? What is the significance of the allusion? (See Intertextuality section.)</p>
<h4>Step 7: Determine the Meaning Unit</h4>
<p>What is the author's main claim in this passage? What are the subordinate claims that support it? How does this unit fit into the broader argument of the book? Meaning is contextual — a verse ripped from its context is not the same as that verse in context.</p>
<h4>Step 8: Translate and Document</h4>
<p>Now produce your translation. For every significant word choice, note your reasoning in the decision log. Record contested readings, alternative translations, and context overrides. This documentation is what distinguishes a translation from a paraphrase — it shows your reasoning so it can be reviewed and challenged.</p>
<h4>Step 9: Check Against Other Translations</h4>
<p>Where do major translations (NASB, ESV, NIV, NLT) agree and disagree? Disagreement is a flag that interpretation is at stake. Understand <em>why</em> they disagree before finalizing your rendering.</p>
<h4>Resources a Translator Uses</h4>
<ul>
  <li><strong>Greek text</strong>: NA28 (Nestle-Aland 28th ed.) or UBS5 with textual apparatus</li>
  <li><strong>Hebrew text</strong>: BHS (Biblia Hebraica Stuttgartensia) with Masoretic notes</li>
  <li><strong>Greek lexicon</strong>: BDAG (Bauer-Danker-Arndt-Gingrich) — the standard; Thayer (public domain)</li>
  <li><strong>Hebrew lexicon</strong>: BDB (Brown-Driver-Briggs, public domain); HALOT (comprehensive, not free)</li>
  <li><strong>Grammar</strong>: Wallace's Greek Grammar Beyond the Basics; Gesenius' Hebrew Grammar</li>
  <li><strong>Theological dictionary</strong>: TDNT (Greek), TDOT (Hebrew) — articles on key words across all their occurrences</li>
  <li><strong>Commentaries</strong>: genre-specific; always use ones that engage the original languages</li>
</ul>`,
};

let _primerSection = 'greek-alphabet';

function _renderPrimerNav() {
  $count.textContent = '';
  let html = '';
  for (const group of PRIMER_GROUPS) {
    html += `<div class="ws-primer-group-label">${group.label}</div>`;
    for (const sec of group.sections) {
      const active = _primerSection === sec.id ? ' active' : '';
      html += `<div class="ws-queue-item ws-primer-item${active}" data-primer="${sec.id}">
        <span class="ws-primer-item__icon">${sec.icon}</span>
        <span class="ws-primer-item__label">${sec.label}</span>
      </div>`;
    }
  }
  $queue.innerHTML = html;
  $queue.querySelectorAll('[data-primer]').forEach(el => {
    el.addEventListener('click', () => {
      _primerSection = el.dataset.primer;
      $queue.querySelectorAll('[data-primer]').forEach(e =>
        e.classList.toggle('active', e.dataset.primer === _primerSection)
      );
      _renderPrimerContent();
    });
  });
  _renderPrimerContent();
}

function _renderPrimerContent() {
  const content = PRIMER_CONTENT[_primerSection] || '<p>Section coming soon.</p>';
  $dossier.innerHTML = `<div class="ws-primer-body">${content}</div>`;
  $dossier.scrollTop = 0;
}

/* ── Dashboard ─────────────────────────────────────────────── */
function _renderDashboard() {
  $queue.innerHTML   = '';
  $count.textContent = '';
  const st = _stats();
  const p1 = _phaseStats('phase1');
  const p2 = _phaseStats('phase2');
  const p5 = _phaseStats('phase5');

  const phaseRow = (label, ps) =>
    ps.total !== null
      ? `<strong>${ps.done}/${ps.total}</strong> ${label}`
      : `${label} <em style="opacity:.5">(not loaded yet)</em>`;

  $dossier.innerHTML = `<div class="ws-dashboard">
    <h2 style="margin:0 0 .5rem;font-size:1.1rem">Dashboard</h2>
    <p class="ws-dash-premise">
      Every word has an <strong>attested semantic range</strong> — the full spread of meanings
      documented across all its uses in the corpus. That range is not a decision to be made;
      it is what the lexicons record. What you <em>are</em> deciding is which rendering best fits
      <em>a specific passage</em>. Use the <strong>Default Rendering Tendency</strong> as a
      starting point for each lemma, then add <strong>Contextual Renderings</strong> wherever
      a passage, book, or construction calls for something different.
      Per-author tendencies live in <strong>Per-book Defaults</strong>.
    </p>
    <div class="ws-dash-grid">
      <div class="ws-dash-card">
        <div class="ws-dash-card__label">Greek Reviewed</div>
        <div class="ws-dash-card__value">${st.gConf}</div>
        <div class="ws-dash-card__sub">of ${st.gTotal.toLocaleString()} · ${Math.round(st.gConf/st.gTotal*100)}%</div>
      </div>
      <div class="ws-dash-card">
        <div class="ws-dash-card__label">Hebrew Reviewed</div>
        <div class="ws-dash-card__value">${st.hConf}</div>
        <div class="ws-dash-card__sub">of ${st.hTotal.toLocaleString()} · ${Math.round(st.hConf/st.hTotal*100)}%</div>
      </div>
      <div class="ws-dash-card">
        <div class="ws-dash-card__label">Phase 1 (NT Greek)</div>
        <div class="ws-dash-card__sub" style="font-size:1rem;margin-top:.35rem">${phaseRow('reviewed', p1)}</div>
      </div>
      <div class="ws-dash-card">
        <div class="ws-dash-card__label">Phase 2 (OT Hebrew)</div>
        <div class="ws-dash-card__sub" style="font-size:1rem;margin-top:.35rem">${phaseRow('reviewed', p2)}</div>
      </div>
      <div class="ws-dash-card">
        <div class="ws-dash-card__label">Contested Terms</div>
        <div class="ws-dash-card__sub" style="font-size:1rem;margin-top:.35rem">${phaseRow('reviewed', p5)}</div>
      </div>
      <div class="ws-dash-card">
        <div class="ws-dash-card__label">Flagged / Locked</div>
        <div class="ws-dash-card__value">${st.disputed} / ${st.locked}</div>
        <div class="ws-dash-card__sub">${st.deferred} deferred</div>
      </div>
    </div>
    <p style="font-size:.82rem;color:var(--color-muted);max-width:560px;line-height:1.6;margin-top:1rem">
      <strong>Start with Phase 1</strong> (top 200 NT Greek, covering ~80% of NT occurrences), then Phase 2
      (top 200 OT Hebrew). Phase 5 (Contested Terms) should be reviewed last.
    </p>

    <div class="ws-workflow">
      <div class="ws-workflow__title">How decisions become a translation</div>
      <ol class="ws-workflow__steps">
        <li>
          <strong>Review entries here</strong> — Confirm, Override, Dispute, or Defer each lemma.
          Decisions are saved to your browser's localStorage instantly.
        </li>
        <li>
          <strong>Export</strong> — Click <em>Export JSON</em> in the top bar to download
          <code>mkt-decisions-YYYY-MM-DD.json</code>.
        </li>
        <li>
          <strong>Apply to glossary files</strong> — Run in terminal:
          <code>python3 scripts/apply-decisions.py mkt-decisions-YYYY-MM-DD.json</code><br>
          This writes your confirmed statuses into <code>data/translation/glossary-*.json</code>.
        </li>
        <li>
          <strong>Regenerate phase bundles</strong> (so the workshop shows updated statuses):
          <code>python3 scripts/seed-glossary.py</code>
        </li>
        <li>
          <strong>Generate the draft translation</strong>:
          <code>python3 scripts/translate-bible.py --tier all --testament nt</code><br>
          Output goes to <code>data/translation/draft/{tier}/{book}.json</code>.
        </li>
        <li>
          <strong>Commit</strong> — <code>git add data/translation/ && git commit</code>
        </li>
      </ol>
      <p class="ws-workflow__note">
        Your localStorage decisions survive browser restarts and are the live working state.
        The Export → Apply cycle is only needed when you want to run the translation script
        or share decisions across devices.
      </p>
    </div>
  </div>`;
}

/* ── Topbar stats ──────────────────────────────────────────── */
function _updateTopbarStats() {
  const st = _stats();
  const gP = Math.round(st.gConf / st.gTotal * 100);
  const hP = Math.round(st.hConf / st.hTotal * 100);
  $topbarStats.innerHTML = `
    <span>Greek <strong>${gP}%</strong></span>
    <span>Hebrew <strong>${hP}%</strong></span>
    ${st.disputed ? `<span style="color:#856404">⚑ ${st.disputed}</span>` : ''}`;
}

/* ── Export / Import ───────────────────────────────────────── */
function _doExport() {
  const blob = new Blob([JSON.stringify({ version: 1, exported: new Date().toISOString(), decisions: _decisions }, null, 2)], { type: 'application/json' });
  const url  = URL.createObjectURL(blob);
  const a    = Object.assign(document.createElement('a'), { href: url, download: `mkt-decisions-${new Date().toISOString().slice(0,10)}.json` });
  a.click();
  URL.revokeObjectURL(url);
}

function _doImport(file) {
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const data     = JSON.parse(e.target.result);
      const incoming = data.decisions || data;
      let   count    = 0;
      for (const [code, dec] of Object.entries(incoming)) {
        _decisions[code] = Object.assign(_decisions[code] || {}, dec);
        count++;
      }
      _saveDecisions();
      _renderNav();
      _updateTopbarStats();
      _activatePhase();
      alert(`Imported ${count} decisions.`);
    } catch { alert('Import failed: invalid JSON.'); }
  };
  reader.readAsText(file);
}

/* ── Utility ───────────────────────────────────────────────── */
function _esc(str) {
  return String(str ?? '')
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

/* ── Init ──────────────────────────────────────────────────── */
export async function initWorkshopPage() {
  $nav         = document.getElementById('ws-nav');
  $queue       = document.getElementById('ws-queue');
  $count       = document.getElementById('ws-count');
  $dossier     = document.getElementById('ws-dossier');
  $search      = document.getElementById('ws-search');
  $layout      = document.getElementById('ws-layout');
  $loading     = document.getElementById('ws-loading');
  $loadingText = document.getElementById('ws-loading-text');
  $topbarStats = document.getElementById('ws-topbar-stats');

  _loadDecisions();
  _loadUiState();

  // Show UI immediately — no upfront fetch needed
  $loading.hidden = true;
  $layout.hidden  = false;

  // Wire search
  let _searchTimer;
  $search.addEventListener('input', () => {
    clearTimeout(_searchTimer);
    _searchTimer = setTimeout(_applyFilter, 200);
  });

  // Export / Import
  document.getElementById('ws-export-btn').addEventListener('click', _doExport);
  document.getElementById('ws-import-btn').addEventListener('click', () =>
    document.getElementById('ws-import-file').click()
  );
  document.getElementById('ws-import-file').addEventListener('change', e => {
    const file = e.target.files?.[0];
    if (file) _doImport(file);
    e.target.value = '';
  });

  _updateTopbarStats();
  _renderNav();
  _activatePhase();
}
