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

import { _resolve, initTheme, parseRef, loadBooks, loadVersions, loadInterlinear, loadStrongs, loadBook, getVersion, setVersion, loadCommentary, COMMENTARY_SOURCES, getCommentarySource, setCommentarySource, loadCrossRefs, parseCrossRefEntry, escHtml, INTERLINEAR_ROOT } from './core.js';
import {
  _authorFreqCache, _cognatesFamilies, _cognatesIndex, _culturalCache, _debatesByCode, _debatesCache, _idiomsData, _idiomsIndex,
  _literaryCache, _morphSigCache, _otInNtByRef, _otInNtCache, _particlesCache, _semanticCache, _stContextCache, _synthesisCache,
  _loadParticles, _loadMorphSig, _loadLiterary, _loadDebates, _loadCultural, _loadIdioms, _loadCognates, _loadOTinNT,
  _loadAuthorFreq, _loadSemanticFields, _loadSTContext, _loadSynthesis,
} from './ol-data.js';
import { autoTagTermsWhenReady } from './terms.js';

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
const SK_DEPTH     = 'bsw_ws_depth';

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
// INTENT: O(1) NT book membership test derived from BOOK_ORDER_NT so that language
//   detection in _studyPassage() stays in sync with the book-order definition above.
// CHANGE? If a book is added to BOOK_ORDER_NT, this Set updates automatically.
const NT_BOOKS = new Set(BOOK_ORDER_NT.map(function([id]) { return id; }));

/* ── Phase definitions ─────────────────────────────────────── */
const PHASES = [
  { id: 'dashboard',  label: 'Dashboard',               icon: '' },
  { id: 'primer',     label: 'Language Primers',         icon: '' },
  { id: 'phase1',     label: 'Phase 1 — Top NT Greek',  icon: '①' },
  { id: 'phase2',     label: 'Phase 2 — Top OT Hebrew', icon: '②' },
  { id: 'phase5',     label: 'Contested Terms',          icon: '⚑' },
  { id: 'all-greek',  label: 'All Greek',                icon: '' },
  { id: 'all-hebrew', label: 'All Hebrew',               icon: '' },
];

/* ── Module state ──────────────────────────────────────────── */
const  _cache     = {};          // phaseId → {code: entry}
let    _decisions = {};          // localStorage overrides
let    _uiState   = { phase: 'dashboard', activeCode: null };
let    _queue     = [];          // code array for current phase
let    _filtered  = [];          // after search
let    _page      = 0;
const  PAGE_SIZE  = 80;

// INTENT: Passage study mode state — when true, column 2 shows interlinear tiles
//   instead of the vocabulary queue. Depth and translationMode apply to the dossier.
// CHANGE? If additional passage-mode views are added (SW-B/C/D), extend _passageRef
//   to carry chapter range info so tabs can query the right data.
// VERIFY: Type "John 1:1" in the passage input, click Study → sw-passage-view is
//   shown, ws-browse-panel is hidden, tiles appear.
let _passageMode     = false;
let _studyMode       = 'verse';   // 'verse' | 'word' | 'book'
let _passageRef      = null;      // parsed ref object (bookId, ch, v, endCh, endV)
let _translationMode = false;     // false = hides translator-only sections in dossier
let _depth           = 2;         // 1=Reader, 2=Student, 3=Scholar
let _lastWordCode    = null;      // last word opened in verse mode (for dossier tab re-render)
let _originalWordOrder = false;  // when true, Hebrew tiles flow RTL (original language direction)

// INTENT: Track the 8 most-recently studied passage refs in localStorage so the nav
//   column can show a quick-access history list in study mode. Most recent first.
// CHANGE? If localStorage key bsw_ws_recent_passages changes, update _renderNav too.
// VERIFY: Study 3 passages → nav left column shows all 3 as clickable ref buttons.
var _LS_RECENT = 'bsw_ws_recent_passages';
var _MAX_RECENT = 8;

function _pushRecentPassage(refStr) {
  var list = _getRecentPassages();
  list = list.filter(function(r) { return r !== refStr; });
  list.unshift(refStr);
  if (list.length > _MAX_RECENT) list = list.slice(0, _MAX_RECENT);
  try { localStorage.setItem(_LS_RECENT, JSON.stringify(list)); } catch(e) {}
}

function _getRecentPassages() {
  try {
    var raw = localStorage.getItem(_LS_RECENT);
    return raw ? JSON.parse(raw) : [];
  } catch(e) { return []; }
}

// P21 Phase 1 (OL-DESK-PLAN.md): the OL reference caches and their loaders
// moved to ol-data.js so the coming /ol/ desk pages share one data layer.
let _interData      = null; // last-loaded interlinear book data; set by _studyPassage, read by _renderWordStudyPanel concordance

// INTENT: Vocabulary flashcard state for SW-N. Deck is a Set of Strong's codes persisted
//   in localStorage; progress tracks SRS due-dates and intervals per code.
//   _fcQueue is the list of due codes for the current flashcard session (rebuilt on open).
// CHANGE? If localStorage keys change (SK_FC_DECK, SK_FC_PROGRESS), migrate old data.
// VERIFY: Add G3056 to deck (☆→★), open flashcards → λόγος appears as due card.
const SK_FC_DECK     = 'bsw_ws_fc_deck';      // JSON: { greek: [...], hebrew: [...] }
const SK_FC_PROGRESS = 'bsw_ws_fc_progress';  // JSON: { code: { due, interval, ease } }
// INTENT: FC_INTERVALS are seed intervals for the first review only.
//   After the first rating, _fcRate() computes subsequent intervals using the ease factor
//   (SM-2-style): Good = prev_interval × ease; Easy = prev_interval × ease × 1.3.
const FC_INTERVALS   = { again: 1, hard: 3, good: 7, easy: 21 };  // first-review seeds only
let _fcDeck    = { greek: new Set(), hebrew: new Set() };  // loaded from localStorage on init
let _fcProgress = {};   // code → { due: ISO string, interval: days }
let _fcQueue   = [];    // current session due codes (shuffled)
let _fcIdx     = 0;     // position in _fcQueue
let _fcReviewed = 0;    // count reviewed this session

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
// INTENT: Render the left nav column. In study mode (default), shows study shortcuts:
//   recent passages, flashcard deck count, frequency-sorted vocabulary links. In translation
//   mode, shows the original phase nav with progress bars and flagged-entry counts.
// CHANGE? If _translationMode or PHASES change, update both branches. Recent-passage history
//   is stored in localStorage key 'bsw_ws_recent_passages' as a JSON array of refStrings.
// VERIFY: Load fresh → study nav shows. Click ⚙ → enable Translation mode → phase nav appears.
function _renderNav() {
  if (!_translationMode) {
    // INTENT: Study mode nav shows recent passage history for quick re-study.
    // CHANGE? If _pushRecentPassage or _LS_RECENT key changes, update here.
    // VERIFY: Study John 1:1, then Romans 8:1 → nav shows both as clickable buttons.
    var recents = _getRecentPassages();
    if (!recents.length) { $nav.innerHTML = ''; return; }
    var html = '<div class="ws-nav-section ws-nav-section--recent">Recent</div>';
    recents.forEach(function(ref) {
      html += '<button class="ws-nav-btn ws-nav-btn--recent" data-ref="' + _esc(ref) + '">'
        + '<span class="ws-nav-btn__label">' + _esc(ref) + '</span></button>';
    });
    $nav.innerHTML = html;
    $nav.querySelectorAll('.ws-nav-btn--recent[data-ref]').forEach(function(btn) {
      btn.addEventListener('click', function() { _studyPassage(btn.dataset.ref); });
    });
    return;
  }

  // ── Translation nav ───────────────────────────────────────────────────────
  const st = _stats();
  var html = '';

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
  $nav.querySelectorAll('.ws-nav-btn[data-phase]').forEach(btn => {
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

/* ── SW-B: Grammar Significance section ───────────────────── */
// INTENT: Build the Grammar Significance HTML for the dossier. If the word is a
//   recognized discourse particle, show a function card explaining what it does
//   in plain English. If it is a verb or noun, show applicable morphology notes
//   from the preloaded morphology-significance cache (best-effort; may be empty).
// CHANGE? If particle/morphology JSON schemas change, update field references here.
//   If new POS categories are added, extend the POS → morph-key mapping below.
// VERIFY: Click G1063 (γάρ) → "Ground / Reason" card appears in red/amber with
//   plain explanation. Click G3056 (λόγος, noun) → morphology section shows genitive
//   and dative case notes. Click G3004 (λέγω, verb) → aspect notes appear.
function _renderGrammarSection(code, lang) {
  const particles = _particlesCache[lang] || {};
  const morphSig  = _morphSigCache[lang]  || {};
  const particle  = particles[code];

  let inner = '';

  // ── Particle function card
  if (particle) {
    inner += '<div class="sw-particle-card sw-particle--' + particle.function + '" style="border-color:currentColor">'
      + '<div class="sw-particle-card__fn">'
      + '<span class="sw-particle-card__word">' + _esc(particle.word) + '</span>'
      + '<strong>' + _esc(particle.function_label) + '</strong>'
      + '</div>'
      + '<p class="sw-particle-card__plain">' + _esc(particle.plain) + '</p>';
    if (particle.example) {
      inner += '<div class="sw-particle-card__example">'
        + '<span class="sw-particle-card__example-ref">' + _esc(particle.example.ref) + '</span>'
        + _esc(particle.example.note)
        + '</div>';
    }
    inner += '</div>';
  }

  // ── Morphology significance hints (verb/noun — POS-keyed)
  // Pull entries whose key starts with the likely POS prefix, so verb → verb_aspect_*
  // We cannot know the token's actual parsed form, so we show all categories for the POS.
  const POS_PREFIXES = {
    'verb': ['verb_aspect_aorist','verb_aspect_perfect','verb_aspect_imperfect','verb_aspect_present',
             'verb_voice_passive','verb_mood_subjunctive','verb_mood_imperative'],
    'noun': ['noun_case_genitive','noun_case_dative'],
    'adj':        ['noun_case_genitive','noun_case_dative'],
    'adjective':  ['noun_case_genitive','noun_case_dative'],
    'participle': ['participle_substantival','participle_hebrew'],
    'article':    ['article_absence'],
    'infinitive': ['infinitive_purpose'],
  };
  // Hebrew-specific
  const HEB_POS_PREFIXES = {
    'verb': ['binyan_piel','binyan_niphal','binyan_hiphil','binyan_hitpael',
             'aspect_perfect','aspect_imperfect','waw_consecutive'],
    'noun': ['construct_chain'],
    'participle': ['participle_hebrew'],
  };

  // Use entry's pos field if available from the dossier entry
  const entry = _getEntry(code);
  const rawPos = (entry && (entry.pos || (entry.source_data && entry.source_data.pos))) || '';
  const posKey = rawPos.toLowerCase().replace(/[^a-z]/g, '');
  const prefixes = (lang === 'hebrew' ? HEB_POS_PREFIXES[posKey] : POS_PREFIXES[posKey]) || [];

  if (prefixes.length > 0) {
    const rows = prefixes.map(function(k) { return morphSig[k]; }).filter(Boolean);
    if (rows.length > 0) {
      inner += '<div class="sw-morph-hints">';
      rows.forEach(function(m) {
        inner += '<div class="sw-morph-hint">'
          + '<div class="sw-morph-hint__label">' + _esc(m.label) + '</div>'
          + '<div class="sw-morph-hint__sig">' + _esc(m.significance) + '</div>';
        if (m.debate) {
          inner += '<div class="sw-morph-hint__debate">📌 ' + _esc(m.debate) + '</div>';
        }
        if (m.examples && m.examples.length) {
          inner += '<ul class="sw-morph-hint__examples">';
          m.examples.forEach(function(ex) { inner += '<li>' + _esc(ex) + '</li>'; });
          inner += '</ul>';
        }
        inner += '</div>';
      });
      inner += '</div>';
    }
  }

  if (!inner) return '';

  return '<div class="sw-grammar-section" data-depth-min="1">'
    + '<div class="sw-grammar-section__title">Grammar Significance</div>'
    + inner
    + '</div>';
}

/* ── Dossier ───────────────────────────────────────────────── */
// INTENT: Renders lexical dossier for a Strong's code. When targetEl is supplied,
//   writes to that element instead of $dossier — used by the verse-mode "Word" tab.
//   compact=true renders a trimmed set (range + grammar + disputes + idioms + 3 uses + sources)
//   and adds a "→ Full Word Study" button; skips deep-dive sections not needed for verse reading.
//   The mobile bottom sheet behavior is skipped when a custom targetEl is provided.
// CHANGE? If $dossier element ID changes, update the querySelector fallback below.
//   If compact sections change, update SW-U5 notes in TODO.md.
// VERIFY: Click any tile in verse mode → "Word" tab shows compact dossier + "Full Word Study" btn.
//   Click the "Full Word Study" btn → switches to Word Study mode with the full dossier.
function _renderDossier(code, targetEl, compact) {
  var $el = targetEl || $dossier;
  const entry = _getEntry(code);
  if (!entry) { $el.innerHTML = '<p class="ws-placeholder">Entry not found.</p>'; return; }

  const src         = entry;
  const hasSrcData  = !!(src.source_data);
  const dodson      = src.source_data?.dodson    || {};
  const thayer      = src.source_data?.thayer    || {};
  const abbott      = src.source_data?.abbott    || {};
  const hebrew      = src.source_data?.hebrew    || {};
  const bdb         = src.source_data?.bdb       || {};
  const gesenius    = src.source_data?.gesenius  || {};
  const freq        = src.nt_freq ?? src.ot_freq ?? 0;
  const freqLabel   = entry._lang === 'greek' ? 'NT' : 'OT';
  const dispute     = src.dispute_level || 0;
  const dispLabels  = ['', 'minor', 'moderate', 'contested', 'major debate'];

  let html = '<div class="ws-dossier">';

  // ── Header + depth toggle (compact mode omits depth toggle, adds "Full Word Study" link)
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
      ${!compact ? `<span>Status: <span class="ws-dossier-head__status ws-status--${entry._status}">${entry._status}</span></span>` : ''}
    </div>
    <div class="ws-dossier-head__actions">
      ${!compact ? `<div class="sw-depth-toggle" id="sw-depth-toggle">
        <span class="sw-depth-label">Depth:</span>
        <button type="button" class="sw-depth-btn${_depth === 1 ? ' sw-depth-btn--active' : ''}" data-depth="1" title="Reader — essential summary">Reader</button>
        <button type="button" class="sw-depth-btn${_depth === 2 ? ' sw-depth-btn--active' : ''}" data-depth="2" title="Student — all lexical sources">Student</button>
        <button type="button" class="sw-depth-btn${_depth === 3 ? ' sw-depth-btn--active' : ''}" data-depth="3" title="Scholar — all sources including M&amp;M and LXX bridge">Scholar</button>
      </div>` : ''}
      <button type="button" class="sw-link-word-btn" data-code="${_esc(code)}" title="Copy link to this word">&#128279;</button>
      <button type="button" class="sw-add-deck-btn" data-code="${_esc(code)}" title="${_isInDeck(code) ? 'Remove from flashcard deck' : 'Add to flashcard deck'}">${_isInDeck(code) ? '★' : '☆'}</button>
    </div>
  </div>`;

  // ── Attested Range (primary content — what the lexical sources actually document)
  if (src.semantic_range) {
    html += `<div class="ws-section ws-section--range" data-depth-min="1">
      <div class="ws-section-title">Attested Range <span class="ws-section-note">— what lexical sources document across all uses</span></div>
      <p class="ws-semantic ws-semantic--headline">${_esc(src.semantic_range)}</p>
    </div>`;
  }
  // INTENT: Attested uses show the word in its actual textual contexts — evidence that the
  //   semantic range is real, not just asserted. Rendered below the range headline, before
  //   the lexical source cards, so evidence leads explanation.
  // CHANGE? If attested_uses schema changes in build-attested-uses.py, update field names here.
  // VERIFY: Open G26 (ἀγάπη) — verse samples from John, Paul, and at least one other NT author
  //   appear below the semantic range headline and above the Lexical Sources section.
  if (src.attested_uses && src.attested_uses.length) {
    html += _renderAttestedUses(compact ? src.attested_uses.slice(0, 3) : src.attested_uses);
  }

  // ── SW-B: Grammar Significance (particle function card + POS morphology hints)
  // INTENT: Surface grammar significance right after the attested range so the user
  //   understands what this word does structurally before diving into lexical sources.
  //   Uses the preloaded _particlesCache and _morphSigCache — no additional fetch needed
  //   since particles are loaded during passage study before tile click.
  // CHANGE? If grammar section should move (e.g. after Lexical Sources), cut this line
  //   and paste it at the new position in _renderDossier. _renderGrammarSection is stateless.
  // VERIFY: Click a particle tile in passage view → Grammar Significance section appears
  //   with colored card. Click a non-particle tile → section is absent or shows morph hints only.
  html += _renderGrammarSection(code, entry._lang || (code.startsWith('G') ? 'greek' : 'hebrew'));

  // ── SW-C: Contested Interpretation (grammar debates panel)
  // INTENT: Surface active scholarly debates tied to this Strong's code and current passage.
  //   Only visible at Student+ depth (data-depth-min="2"). Shown after grammar significance
  //   but before lexical sources — the debate is about the word's meaning in context,
  //   which should be visible before the reader dives into dictionary definitions.
  // CHANGE? If _renderDebateSection is moved or debates.json schema changes, update both
  //   _renderDebateSection() and _debateTriggerMatches().
  // VERIFY: Study Gal 2:16, click πίστεως tile → "Contested Interpretation" section with
  //   the πίστις Χριστοῦ debate card. In browse mode, clicking G4102 shows all triggers.
  html += _renderDebateSection(code);

  // ── SW-E: Idiom Alert (culturally loaded expressions that English readers miss)
  // INTENT: Surface idiom alerts directly after debates so the user sees cultural context
  //   before diving into lexical sources. Checks _idiomsIndex (pre-loaded in _studyPassage)
  //   for the clicked code — renders a card only when there is a real idiom match.
  // CHANGE? If idiom data schema changes, update _renderIdiomAlertSection(). If this section
  //   should only show in passage mode (not browse mode), add a _passageMode guard here.
  // VERIFY: Click G5207 (υἱός) → "Idiom Alert" shows "Son of X" and "Son of Man" entries
  //   with plain-English explanation and expandable cultural details. Click G3056 (λόγος) →
  //   no idiom alert (λόγος has no idiom entry). In browse mode, idioms still show.
  html += _renderIdiomAlertSection(code);

  // ── SW-J: Author Frequency
  // INTENT: Show which NT/OT author uses this word most intensively (per 1000 words)
  //   so the reader can spot characteristic vocabulary (Pauline δικαιοσύνη, Johannine ἀγαπάω).
  // CHANGE? If _authorFreqCache[lang] is null (no study passage loaded yet), returns empty.
  //   Pre-warm by adding _loadAuthorFreq(lang) to _studyPassage() Promise.all.
  // VERIFY: Study Romans, click G1343 (δικαιοσύνη) → "Author Frequency" at Student depth
  //   shows Paul with peak badge; other authors have smaller heat-bar cells.
  if (!compact) html += _renderAuthorFreqSection(code, entry._lang || (code.startsWith('G') ? 'greek' : 'hebrew'));

  // ── SW-I: Semantic Neighborhood (PMI co-occurrence)
  // INTENT: Show words that cluster with this word across the biblical corpus via PMI.
  //   Scholar depth only — PMI is a statistical tool that requires interpretive sophistication.
  // CHANGE? If the semantic fields data should be accessible at Student depth, change
  //   data-depth-min to "2" in _renderSemanticSection().
  // VERIFY: Study John 1, click G3056 (λόγος) → "Semantic Neighborhood" appears at Scholar
  //   depth with co-occurring words as chips. Click a chip → dossier navigates there.
  if (!compact) html += _renderSemanticSection(code, entry._lang || (code.startsWith('G') ? 'greek' : 'hebrew'));

  // ── SW-H: Word Family (cognate roots)
  // INTENT: Show the root word and sibling family members as clickable chips so the user
  //   can see how a word's meaning derives from its root and travel to related entries.
  //   Depends on _cognatesFamilies + _cognatesIndex pre-loaded by _loadCognates() in
  //   _studyPassage(). In browse mode the data may not be loaded — renders empty string.
  // CHANGE? If cognate data files change schema, update _renderCognateSection(). If this
  //   section should appear before debates/idioms, move this line up in _renderDossier.
  // VERIFY: Click H3519 (כָּבוֹד) → "Word Family" section at Student depth shows root
  //   H3513 callout and sibling chips. Click a chip → dossier updates to that entry.
  if (!compact) html += _renderCognateSection(code);

  // ── SW-L: Second Temple Context (Jewish background at Scholar depth)
  // INTENT: Surface relevant Second Temple Jewish background documents for the clicked word.
  //   Scholar-depth only (data-depth-min="3") since this requires more specialist interest.
  //   Checks both strongs_keys (word-level) and trigger_passages (passage-level overlap).
  // CHANGE? If _stContextCache is not pre-loaded when clicking in browse mode, this will
  //   render empty — to show ST context in browse mode, add _loadSTContext() to initWorkshopPage.
  // VERIFY: In Scholar mode, click G3056 (λόγος) → "Second Temple Context" card shows Philo
  //   Logos entry with source, date, context paragraph, significance, and representative quote.
  if (!compact) html += _renderSTContext(code);

  // INTENT: Extrabiblical uses (M&M papyri) follow biblical attestation — showing the same
  //   word in ordinary Koine Greek outside the Bible, the strongest evidence against
  //   over-theological readings. Rendered only when data exists (requires fetch-moulton-milligan.py).
  // CHANGE? If extrabiblical_uses schema changes in seed-glossary.py or fetch-moulton-milligan.py
  //   (field names: source, citation, text, note), update _renderExtrabib accordingly.
  // VERIFY: Open G3056 (λόγος) after running fetch-moulton-milligan.py — Extrabiblical
  //   section appears with M&M badge and papyri citation(s) showing commercial/ordinary use.
  if (!compact && entry._lang === 'greek' && src.extrabiblical_uses && src.extrabiblical_uses.length) {
    html += _renderExtrabib(src.extrabiblical_uses);
  }

  // ── Lexical Sources (supporting detail, subordinate to the range)
  // INTENT: Manifest-driven source cards — one entry per source, filtered to those with content.
  //   Wrapped in <details> defaulting to closed when verse samples are present so the dossier
  //   stays scannable; open by default when no verse samples exist yet.
  // CHANGE? To add a new source: add one entry to SOURCES_MANIFEST and ensure seed-glossary.py
  //   populates the corresponding source_data field and includes the source key in sources[].
  // VERIFY: Open G3056 (λόγος) — Lexical Sources section is collapsed (verse samples present).
  //   Expand it: three source cards appear (Dodson, Thayer, Abbott-Smith). For H2617 (חֶסֶד):
  //   three Hebrew cards appear (Strong's Hebrew, BDB, Gesenius).
  if (hasSrcData) {
    var SOURCES_MANIFEST = entry._lang === 'greek' ? [
      { label: 'Dodson (CC0)',        gloss: dodson.gloss,    def: dodson.def,    extra: dodson.deriv          },
      { label: 'Thayer (1889)',       gloss: thayer.short,    def: thayer.long,   extra: ''                    },
      { label: 'Abbott-Smith (1922)', gloss: abbott.gloss,    def: abbott.def,    extra: abbott.classical_note || '' },
    ] : [
      { label: "Strong's Hebrew",     gloss: hebrew.gloss,    def: hebrew.def,    extra: hebrew.deriv          },
      { label: 'BDB (1906)',          gloss: bdb.short,       def: bdb.long,      extra: ''                    },
      { label: 'Gesenius (1857)',     gloss: gesenius.gloss,  def: gesenius.def,  extra: gesenius.cognates || '' },
    ];
    var activeCards = SOURCES_MANIFEST.filter(function(s) { return s.gloss || s.def; });
    var sourcesOpen = !(src.attested_uses && src.attested_uses.length);
    html += '<div class="ws-section ws-section--sources" data-depth-min="2">';
    html += '<details class="ws-sources-details"' + (sourcesOpen ? ' open' : '') + '>';
    html += '<summary class="ws-section-title ws-sources-summary">Lexical Sources <span class="ws-section-note">(' + activeCards.length + ' source' + (activeCards.length === 1 ? '' : 's') + ')</span></summary>';
    html += '<div class="ws-sources">';
    activeCards.forEach(function(s) { html += _sourceCard(s.label, s.gloss, s.def, s.extra); });
    html += '</div></details></div>';
  }

  // ── LXX Bridge (Hebrew only — how Septuagint translators rendered this word)
  // INTENT: Renders after Lexical Sources so the user sees the scholarly dictionary
  //   entries first, then the evidence of ancient translation decisions. The LXX bridge
  //   shows that the semantic range problem is not new — the translators of the LXX faced
  //   the same choices and their decisions shaped the NT's theological vocabulary.
  // CHANGE? If lxx_bridge schema changes in build-lxx-bridge.py (field names: greek_code,
  //   greek_lemma, frequency, note), update _renderLxxBridge accordingly.
  // VERIFY: Open H2617 (חֶסֶד) — LXX Bridge section appears below Lexical Sources showing
  //   ἔλεος (170×) as dominant rendering, χάρις (12×) secondary, with semantic notes.
  if (!compact && entry._lang === 'hebrew' && src.lxx_bridge && src.lxx_bridge.length) {
    html += _renderLxxBridge(src.lxx_bridge);
  }

  if (!compact) {
    // ── Book distribution map (shows where this word actually clusters)
    html += _renderBookDistribution(entry._bookFreq, entry._lang);

    // ── Default Rendering Tendency (your starting-point per tier — not a decided meaning)
    html += '<div class="ws-section ws-section--tiers sw-trans-section" id="ws-tiers-section">';
    html += '<div class="ws-section-title">Default Rendering Tendency <span class="ws-section-note">— your starting point; context below is where meaning is actually decided</span></div>';
    html += _renderTiersView(entry._tiers);
    html += '</div>';
  }

  // ── Per-book defaults (middle tier between global default and passage overrides)
  if (!compact) html += _renderBookDefaults(code, entry);

  // ── Contextual Renderings (the primary work surface — where translation actually happens)
  if (!compact) {
  const overrides = ((_decisions[code] || {}).context_overrides) || src.context_overrides || [];
  html += `<div class="ws-section ws-section--contextual sw-trans-section" id="ws-overrides-section">
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
  } // end contextual renderings

  if (!compact) {
  // ── Decision log (translation mode only)
  const log = entry._decLog;
  html += '<div class="ws-section sw-trans-section"><div class="ws-section-title">Decision Log</div>';
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
  html += `<div class="ws-actions sw-trans-section" id="ws-actions">
    <button class="ws-action-btn ws-action-btn--confirm" data-action="confirm" ${isLocked ? 'disabled' : ''}>✓ Set Default</button>
    <button class="ws-action-btn ws-action-btn--override" data-action="override" ${isLocked ? 'disabled' : ''}>✎ Edit Default</button>
    <button class="ws-action-btn ws-action-btn--inform"   data-action="inform"   ${isLocked ? 'disabled' : ''}>💬 Note</button>
    <button class="ws-action-btn ws-action-btn--dispute"  data-action="dispute"  ${isLocked ? 'disabled' : ''}>⚑ Flag Range</button>
    <button class="ws-action-btn ws-action-btn--defer"    data-action="defer"    ${isLocked ? 'disabled' : ''}>⟳ Defer</button>
    <button class="ws-action-btn ws-action-btn--lock"     data-action="lock"     ${!isConfirmed || isLocked ? 'disabled' : ''}>★ Anchor</button>
  </div>`;
  } // end !compact

  // ── Compact: "Full Word Study →" button
  if (compact) {
    html += '<div class="sw-dossier-full-link">'
      + '<button type="button" class="ws-btn ws-btn--sm sw-open-word-study-btn" data-code="' + _esc(code) + '">'
      + '&#8594; Full Word Study'
      + '</button></div>';
  }

  html += '</div>';
  $el.innerHTML = html;

  // INTENT: On narrow screens, slide the dossier up as a bottom sheet when a word is opened.
  //   Only applies to the primary dossier column, not the tab-embedded version (targetEl).
  // CHANGE? If $dossier element ID changes from ws-dossier, update querySelector here.
  // VERIFY: On mobile viewport (< 760px), click any interlinear tile — dossier slides up
  //   from the bottom; tap backdrop or ✕ to dismiss.
  if (!targetEl && window.innerWidth < 760) {
    var existingHandle = $dossier.querySelector('.sw-dossier-handle');
    if (!existingHandle) {
      var handle = document.createElement('div');
      handle.className = 'sw-dossier-handle';
      handle.innerHTML = '<div class="sw-dossier-handle__pill"></div>'
        + '<button class="sw-dossier-handle__close" aria-label="Close word panel">✕</button>';
      $dossier.insertBefore(handle, $dossier.firstChild);
    }
    $dossier.classList.add('sw-dossier--open');
    var backdrop = document.getElementById('sw-dossier-backdrop') || (function() {
      var el = document.createElement('div');
      el.id = 'sw-dossier-backdrop';
      el.className = 'sw-dossier-backdrop';
      document.getElementById('workshop-container').appendChild(el);
      return el;
    })();
    backdrop.style.display = 'block';
    function _closeDossierSheet() {
      $dossier.classList.remove('sw-dossier--open');
      backdrop.style.display = 'none';
    }
    $dossier.querySelector('.sw-dossier-handle__close').onclick = _closeDossierSheet;
    backdrop.onclick = _closeDossierSheet;
  }

  $el.querySelectorAll('[data-action]').forEach(btn => {
    btn.addEventListener('click', () => _handleAction(btn.dataset.action, code));
  });

  // SW-N: "Link to this word" button — copies workshop URL with ?s=G3056 to clipboard
  // INTENT: Generates a direct deep-link to the current word's dossier so the user can
  //   share or bookmark it. Uses navigator.clipboard if available; falls back to prompt().
  // CHANGE? If the workshop URL structure changes (no longer at translation/workshop/), update path.
  // VERIFY: Click the 🔗 button in the dossier header — browser shows "Copied!" toast; paste
  //   into address bar → page loads and auto-opens the word.
  const linkBtn = $el.querySelector('.sw-link-word-btn[data-code]');
  if (linkBtn) {
    linkBtn.addEventListener('click', function() {
      const wordCode = linkBtn.dataset.code;
      const url = (location.origin + location.pathname).replace(/\/+$/, '') + '/?s=' + encodeURIComponent(wordCode);
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(function() {
          linkBtn.textContent = '✓';
          setTimeout(function() { linkBtn.textContent = '🔗'; }, 1500);
        });
      } else {
        prompt('Copy this link:', url);
      }
    });
  }

  // Contextual rendering buttons (renamed class; old ws-add-override-btn alias kept for safety)
  ($el.querySelector('.ws-add-contextual-btn') || $el.querySelector('.ws-add-override-btn'))
    ?.addEventListener('click', () => _showAddOverrideForm(code));
  $el.querySelectorAll('.ws-remove-override-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const idx = parseInt(btn.dataset.idx, 10);
      const dec = _decisions[code] || {};
      const ovs = [...(dec.context_overrides || src.context_overrides || [])];
      ovs.splice(idx, 1);
      _setDecision(code, { context_overrides: ovs });
      _renderDossier(code, targetEl);
    });
  });

  // Per-book default inputs — debounced blur-save so typing isn't interrupted
  // INTENT: On blur, collect all book-default inputs for this entry and persist to _decisions.
  // CHANGE? _setDecision merges at the top level; book_defaults must be the full object each save.
  // VERIFY: Edit a per-book input, tab away; reload the entry — the value should persist.
  $el.querySelectorAll('.ws-bookdef-input').forEach(inp => {
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

  // SW-H: Cognate chip click — navigate dossier to that family member's entry
  // INTENT: Each chip in the Word Family section carries data-code; clicking it should
  //   update the active entry to that word's dossier without requiring the user to scroll
  //   the queue or search for the entry. Uses _getEntry() to confirm the entry exists first.
  // CHANGE? If the dossier should open in a second panel instead, update this handler.
  // VERIFY: Open H3519 (כָּבוֹד) → Word Family section → click H3513 chip → dossier
  //   refreshes showing H3513 (כָּבַד) as the active entry with its own word family.
  $el.querySelectorAll('.sw-cognate-chip[data-code]').forEach(function(chip) {
    chip.addEventListener('click', function() {
      var targetCode = chip.dataset.code;
      if (!targetCode || !_getEntry(targetCode)) return;
      _uiState.activeCode = targetCode;
      _saveUiState();
      _renderDossier(targetCode, targetEl);
    });
    chip.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); chip.click(); }
    });
  });

  $el.querySelectorAll('.sw-semantic-chip[data-code]').forEach(function(chip) {
    chip.addEventListener('click', function() {
      var targetCode = chip.dataset.code;
      if (!targetCode) return;
      if (_getEntry(targetCode)) {
        _uiState.activeCode = targetCode;
        _saveUiState();
        _renderDossier(targetCode, targetEl);
      } else {
        _openWord(targetCode);
      }
    });
    chip.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); chip.click(); }
    });
  });

  // INTENT: Wire every verse-sample and echo .ref link inside the dossier to open as a
  //   workshop passage study instead of the main-site Bible Gateway popup.
  // CHANGE? If wireRefLinks signature changes in main wire.js, update this parallel impl.
  // VERIFY: Open G3056 → click a verse sample ref (e.g. "John 1:1") → passage study opens.
  $el.querySelectorAll('a.ref[data-ref], span.ref[data-ref]').forEach(function(refEl) {
    refEl.style.cursor = 'pointer';
    refEl.removeAttribute('href');
    refEl.addEventListener('click', function(e) {
      e.preventDefault();
      var ref = refEl.dataset.ref;
      if (ref) _studyPassage(ref);
    });
  });

  // INTENT: "Full Word Study →" button (compact dossier only) switches to Word Study mode
  //   and opens the full dossier for the same code so the user can explore without leaving verse mode.
  // CHANGE? If _setStudyMode or _openWord signature changes, update call below.
  // VERIFY: In verse mode Word tab, click "Full Word Study →" → switches to Word Study mode, full dossier loads.
  var openWsBtn = $el.querySelector('.sw-open-word-study-btn[data-code]');
  if (openWsBtn) {
    openWsBtn.addEventListener('click', function() {
      var c = openWsBtn.dataset.code;
      if (c) {
        _setStudyMode('word');
        _openWord(c);
      }
    });
  }
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
  let html = '<div class="ws-section ws-section--bdist" data-depth-min="2"><div class="ws-section-title">Bible Distribution</div><div class="ws-bdist">';
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
  let html = `<div class="ws-section ws-section--bookdefs sw-trans-section">
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

// INTENT: Render a collapsible list of biblical verse samples that show the word in its
//   actual textual contexts across different authors and genres. Provides evidence-first
//   presentation — the range is real because these verses exist, not just because a lexicon
//   asserts it. Notes (if present) flag differing semantic registers between uses.
// CHANGE? If attested_uses schema changes in build-attested-uses.py or seed-glossary.py
//   (field names: ref, text, note, context), update the template literals below.
// VERIFY: Open G3056 (λόγος) — collapsible "Verse Samples" section appears. Each item shows
//   a ref badge, truncated verse text, and context label. Expand/collapse toggle works.
function _renderAttestedUses(uses) {
  if (!uses || !uses.length) return '';
  var items = uses.map(function (u) {
    return `<li class="ws-attestation-item">
      <span class="ws-attestation-ref">${_esc(u.ref || '')}</span>
      ${u.context ? `<span class="ws-attestation-ctx">${_esc(u.context)}</span>` : ''}
      <span class="ws-attestation-quote">${_esc((u.text || '').slice(0, 200))}</span>
      ${u.note ? `<span class="ws-attestation-note">${_esc(u.note)}</span>` : ''}
    </li>`;
  }).join('');
  return `<details class="ws-attestation-details">
    <summary class="ws-attestation-summary">Verse Samples <span class="ws-section-note">(${uses.length} uses)</span></summary>
    <ul class="ws-attestation-list">${items}</ul>
  </details>`;
}

// INTENT: Render a collapsible list of extrabiblical (papyri/secular Koine) attestations,
//   showing the word in ordinary non-religious use — the strongest available argument
//   against over-theologising NT vocabulary. Source badge identifies M&M vs. other sources.
// CHANGE? If extrabiblical_uses schema changes in seed-glossary.py or fetch-moulton-milligan.py
//   (field names: source, citation, text, note), update the template literals here.
// VERIFY: Open G3056 (λόγος) after running fetch-moulton-milligan.py — collapsible
//   "Extrabiblical Uses" section appears with M&M badge and a papyri citation.
function _renderExtrabib(uses) {
  if (!uses || !uses.length) return '';
  var items = uses.map(function(u) {
    return '<div class="ws-extrabib-item">'
      + (u.source   ? '<span class="ws-extrabib-source">'   + _esc(u.source)                       + '</span>' : '')
      + (u.citation ? '<span class="ws-extrabib-citation">' + _esc(u.citation)                     + '</span>' : '')
      + (u.text     ? '<div class="ws-extrabib-text">'      + _esc((u.text || '').slice(0, 300))   + '</div>'  : '')
      + (u.note     ? '<div class="ws-extrabib-note">'      + _esc(u.note)                         + '</div>'  : '')
      + '</div>';
  }).join('');
  return '<div data-depth-min="3"><details class="ws-extrabib-details">'
    + '<summary class="ws-extrabib-summary">Extrabiblical Uses <span class="ws-section-note">(papyri · secular Koine)</span></summary>'
    + '<div class="ws-extrabib-list">' + items + '</div>'
    + '</details></div>';
}

// INTENT: Render the LXX Bridge as a concise set of Greek-rendering chips for a Hebrew entry,
//   showing frequency and a note explaining what the Greek choice captures vs. misses.
//   Evidence that the semantic range problem is ancient — the LXX translators faced it too.
// CHANGE? If lxx_bridge schema changes in build-lxx-bridge.py (field names: greek_code,
//   greek_lemma, frequency, note), update the template literals here.
// VERIFY: Open H2617 (חֶסֶד) — LXX Bridge section shows ἔλεος chip (170×) as dominant,
//   χάρις (12×) secondary, each with a note. Section title and layout match ws-lxx-bridge CSS.
function _renderLxxBridge(bridge) {
  if (!bridge || !bridge.length) return '';
  var items = bridge.map(function(p) {
    return '<div class="ws-lxx-pair">'
      + '<span class="ws-lxx-pair__lemma">' + _esc(p.greek_lemma || '') + '</span>'
      + '<span class="ws-lxx-pair__code">'  + _esc(p.greek_code  || '') + '</span>'
      + (p.frequency ? '<span class="ws-lxx-pair__freq">' + p.frequency + '×</span>' : '')
      + (p.note      ? '<span class="ws-lxx-pair__note">' + _esc(p.note) + '</span>'      : '')
      + '</div>';
  }).join('');
  return '<div class="ws-section ws-section--lxx" data-depth-min="3">'
    + '<div class="ws-section-title">LXX Bridge <span class="ws-section-note">— how Septuagint translators rendered this word</span></div>'
    + '<div class="ws-lxx-bridge">' + items + '</div>'
    + '</div>';
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
      Every word has an <strong>attested semantic range</strong> — documented across biblical
      and extrabiblical use. Each dossier shows <strong>verse samples</strong> (the word in its
      actual contexts), <strong>lexical sources</strong> (Dodson/Thayer/Abbott-Smith for Greek;
      Strong's/BDB/Gesenius for Hebrew), and for Hebrew terms a <strong>LXX Bridge</strong>
      showing how the Septuagint translators rendered the same word — and what their Greek
      choice captured or missed. What you <em>are</em> deciding is which rendering best fits
      <em>a specific passage</em>. Use the <strong>Default Rendering Tendency</strong> as a
      starting point, then add <strong>Contextual Renderings</strong> wherever a passage, book,
      or construction calls for something different.
    </p>
    ${(st.gConf || st.hConf || st.disputed || st.locked || st.deferred) ? `
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
    </div>` : `
    <div class="ws-dash-card" style="max-width:560px">
      <div class="ws-dash-card__label">Getting started</div>
      <div class="ws-dash-card__sub" style="font-size:.9rem;line-height:1.6;margin-top:.35rem">
        Look up any word or verse above to open its dossier — your review
        progress across the ${st.gTotal.toLocaleString()} Greek and
        ${st.hTotal.toLocaleString()} Hebrew lemmas will appear here once you
        rate your first entry.
      </div>
    </div>`}
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
  if (!_translationMode) { $topbarStats.innerHTML = ''; return; }
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
// Use the shared escaper from core.js (imported above) rather than a local duplicate.
// escHtml also escapes single quotes and guards null; aliased so existing _esc() calls stand.
var _esc = escHtml;

/* ── Depth toggle (SW-A/SW-G) ──────────────────────────────── */
// INTENT: Depth controls how much of the dossier is shown. Reader (1) = essential
//   summary only; Student (2) = all lexical sources; Scholar (3) = all including
//   M&M papyri and LXX bridge. Applied by setting a CSS class on ws-page.
// CHANGE? If new depth levels are added, update SW_DEPTH_LABELS and the CSS
//   sw-depth-1/2/3 rules in workshop.css that hide [data-depth-min].
// VERIFY: At depth 1, open the dossier for G26 — Lexical Sources section is hidden.
//   At depth 2, it is visible. At depth 3, LXX Bridge is also visible.
const SK_DEPTH_PROMPTED = 'bsw_ws_depth_set';
function _initDepth() {
  const raw = localStorage.getItem(SK_DEPTH);
  if (!raw) {
    // First visit — show depth chooser; default to Student until they choose
    _depth = 2;
    _applyDepth(2);
    _showDepthPrompt();
    return;
  }
  try { _depth = parseInt(raw, 10) || 2; } catch { _depth = 2; }
  if (_depth < 1 || _depth > 3) _depth = 2;
  _applyDepth(_depth);
}

// INTENT: Render a one-time first-visit depth chooser above the passage entry area.
//   Dismissed permanently by choosing a level (stores both SK_DEPTH and SK_DEPTH_PROMPTED).
//   Allows users who don't know what to expect to understand the three depth levels before
//   diving into the dossier.
// CHANGE? If the three depth levels change (SW-G), update the label/description text below.
//   If the passage-entry area ID changes from 'sw-depth-prompt-host', update the querySelector.
// VERIFY: Clear localStorage, reload workshop — depth chooser banner appears above the passage
//   input. Click "Student" → banner disappears, depth is set, page reload shows no banner.
function _showDepthPrompt() {
  const host = document.querySelector('.ws-page');
  if (!host || document.getElementById('sw-depth-prompt')) return;

  const banner = document.createElement('div');
  banner.id = 'sw-depth-prompt';
  banner.className = 'sw-depth-prompt';
  banner.innerHTML = '<div class="sw-depth-prompt__title">Choose your study depth</div>'
    + '<p class="sw-depth-prompt__sub">You can change this any time in the dossier.</p>'
    + '<div class="sw-depth-prompt__choices">'
    + '<button class="sw-depth-prompt__btn" data-pick="1">'
    + '<span class="sw-depth-prompt__btn-label">Reader</span>'
    + '<span class="sw-depth-prompt__btn-desc">Word summary, verse samples, and idiom alerts — no lexical jargon</span>'
    + '</button>'
    + '<button class="sw-depth-prompt__btn sw-depth-prompt__btn--rec" data-pick="2">'
    + '<span class="sw-depth-prompt__btn-label">Student <span class="sw-depth-prompt__rec">recommended</span></span>'
    + '<span class="sw-depth-prompt__btn-desc">All lexical sources, grammar significance, contested interpretations, cultural context</span>'
    + '</button>'
    + '<button class="sw-depth-prompt__btn" data-pick="3">'
    + '<span class="sw-depth-prompt__btn-label">Scholar</span>'
    + '<span class="sw-depth-prompt__btn-desc">Everything — M&M papyri, LXX bridge, semantic fields, Second Temple context</span>'
    + '</button>'
    + '</div>';

  banner.addEventListener('click', function(e) {
    const btn = e.target.closest('[data-pick]');
    if (!btn) return;
    const level = parseInt(btn.dataset.pick, 10);
    _applyDepth(level);
    try { localStorage.setItem(SK_DEPTH_PROMPTED, '1'); } catch(e) {}
    banner.remove();
  });

  // Above the passage-entry area (the thing it explains) — NOT at the top of
  // .ws-page, which put it above the app's own topbar as a detached floating
  // card. Falls back to page-top only if the entry area is ever renamed.
  var anchor = document.getElementById('sw-passage-entry');
  if (anchor && anchor.parentNode) anchor.parentNode.insertBefore(banner, anchor);
  else host.insertBefore(banner, host.firstChild);
}
function _applyDepth(level) {
  _depth = level;
  try { localStorage.setItem(SK_DEPTH, String(level)); } catch (e) {}
  const page = document.querySelector('.ws-page');
  if (page) {
    page.classList.remove('sw-depth-1', 'sw-depth-2', 'sw-depth-3');
    page.classList.add('sw-depth-' + level);
  }
  // Update depth toggle buttons
  document.querySelectorAll('.sw-depth-btn').forEach(function (btn) {
    btn.classList.toggle('sw-depth-btn--active', parseInt(btn.dataset.depth, 10) === level);
  });
}

/* ── Translation mode toggle (SW-A) ────────────────────────── */
// INTENT: In study mode (default), translator-only UI (tier inputs, status buttons,
//   decision log, contextual overrides) is hidden so the dossier reads as a clean
//   reference card. Translation mode reveals those controls for workflow use.
// CHANGE? If new translator sections are added to _renderDossier, add the class
//   sw-trans-section to their opening element so this toggle picks them up.
// VERIFY: On load, #ws-tiers-section and #ws-actions should not be visible. Click
//   "Translation mode" → they appear. Click again → they hide.
function _applyTransMode() {
  // INTENT: Toggle translation-mode CSS class on the page root so the 3-column grid (with nav)
  //   is shown in translation mode and the 2-column grid (no nav) in study mode.
  // CHANGE? If the ws-page element ID/class changes, update the querySelector below.
  // VERIFY: Click ⚙ → Translation mode → nav column appears with phase list; toggle off → hides.
  const page = document.querySelector('.ws-page');
  if (page) page.classList.toggle('ws-page--translation', _translationMode);

  const dossier = document.getElementById('ws-dossier');
  if (dossier) dossier.classList.toggle('sw-trans-on', _translationMode);
  const btn = document.getElementById('sw-trans-toggle-btn');
  if (btn) {
    btn.classList.toggle('ws-btn--active', _translationMode);
    btn.setAttribute('aria-pressed', _translationMode ? 'true' : 'false');
  }
  if ($nav) _renderNav();
  if ($topbarStats) _updateTopbarStats();
}

/* ── Passage study mode (SW-A) ─────────────────────────────── */

// INTENT: Render the "Word Family" section for the dossier (SW-H). Looks up the clicked
//   code in _cognatesIndex to find its root, then finds the full family in _cognatesFamilies.
//   Each family member renders as a clickable chip — click navigates to that word's dossier.
//   Shows the root meaning callout to make the etymology visually prominent.
// CHANGE? If chip click behavior should differ (e.g. open in a new panel), update the
//   onclick handler on .sw-cognate-chip. If max chips should change, adjust the slice limit.
// VERIFY: Click H3519 (כָּבוֹד) → "Word Family" shows root H3513 callout "כָּבַד — heavy/honor"
//   + chips for all family members. Click a chip → dossier navigates to that entry.
//   Click G25 (ἀγαπάω) → family shows G26 ἀγάπη and G27 ἀγαπητός chips.
function _renderCognateSection(code) {
  var prefix = code.startsWith('G') ? 'G' : 'H';
  var index  = _cognatesIndex[prefix];
  var fams   = _cognatesFamilies[prefix];
  if (!index || !fams) return '';  // data not loaded (shouldn't happen — pre-warmed)

  var rootCode = index[code];
  if (!rootCode) return '';  // not in any family

  // Find the family object
  var family = null;
  for (var i = 0; i < fams.length; i++) {
    if (fams[i].root === rootCode) { family = fams[i]; break; }
  }
  if (!family || family.members.length < 2) return '';

  // Build chip HTML — members sorted by is_root first, then others
  var rootMember  = family.members.find(function(m) { return m.is_root; }) || family.members[0];
  var otherMembers= family.members.filter(function(m) { return m.code !== code && !m.is_root; });
  var selfMember  = family.members.find(function(m) { return m.code === code && !m.is_root; });

  function chip(m) {
    var isActive = m.code === code ? ' sw-cognate-chip--active' : '';
    var isRoot   = m.is_root       ? ' sw-cognate-chip--root'   : '';
    return '<span class="sw-cognate-chip' + isActive + isRoot + '" data-code="' + _esc(m.code) + '" title="' + _esc(m.gloss) + '" role="button" tabindex="0">'
      + '<span class="sw-cognate-chip__lemma">' + _esc(m.lemma) + '</span>'
      + '<span class="sw-cognate-chip__gloss">' + _esc(m.gloss.split(',')[0]) + '</span>'
      + '<span class="sw-cognate-chip__code">' + _esc(m.code) + '</span>'
      + '</span>';
  }

  // Show root callout + all chips (cap at 12 members to keep dossier scannable)
  var allChips = family.members.slice(0, 12).map(chip).join('');

  var rootCallout = '<div class="sw-cognate-root-callout">'
    + '<span class="sw-cognate-root-callout__lemma">' + _esc(rootMember.lemma) + '</span>'
    + (rootMember.translit ? '<span class="sw-cognate-root-callout__translit">' + _esc(rootMember.translit) + '</span>' : '')
    + ' <span class="sw-cognate-root-callout__dash">—</span> '
    + '<span class="sw-cognate-root-callout__meaning">' + _esc(family.root_meaning) + '</span>'
    + '</div>';

  return '<div class="ws-section sw-cognate-section" data-depth-min="2">'
    + '<div class="ws-section-title">Word Family <span class="ws-section-note">— share root meaning with ' + _esc(family.root_meaning) + '</span></div>'
    + rootCallout
    + '<div class="sw-cognate-chips">' + allChips + '</div>'
    + '</div>';
}

// INTENT: Find quotation entries relevant to the current passage (NT side) or the OT ref
//   being studied. In passage mode, matches any quotation whose nt_ref overlaps with the
//   current study passage range. Returns array of matching quotation objects.
// CHANGE? If _passageRef format changes, update the ch/v comparison logic here.
// VERIFY: Study Matt 1:23 → _findRelevantQuotations() returns the Isa 7:14 entry.
//   Study John 1:1-18 → no OT-in-NT entries (John 1 has no explicit formal quotations).
function _findRelevantQuotations() {
  if (!_otInNtCache || !_passageRef) return [];
  var results = [];
  _otInNtCache.forEach(function(q) {
    var parsed = parseRef(q.nt_ref);
    if (!parsed) return;
    if (parsed.bookId !== _passageRef.bookId) return;
    // Check verse overlap
    var qCh = parsed.ch;
    var qV  = parsed.v;
    if (qCh < _passageRef.ch || qCh > _passageRef.endCh) return;
    if (qCh === _passageRef.ch && qV < _passageRef.v) return;
    if (qCh === _passageRef.endCh && qV > _passageRef.endV) return;
    results.push(q);
  });
  return results;
}

// INTENT: Render the OT-in-NT three-column comparison panel for the passage view.
//   Shows all formal quotations in the current passage with MT | LXX | NT columns,
//   key differences highlighted, and an interpretation note.
//   Called from _renderPassageTiles() (or _studyPassage) after tiles are rendered.
// CHANGE? If the passage tab system is refactored, move this rendering to the Intertextual tab.
//   If quotations.json gains more fields (e.g. commentary_refs), add them here.
// VERIFY: Study Matt 1:22-23 → "Intertextual" tab → OT-in-NT panel shows Isa 7:14 with
//   three columns, עַלְמָה/παρθένος difference card highlighted gold, fulfillment type badge.
function _renderOTinNTPanel(quotations) {
  if (!quotations || !quotations.length) return '';

  var typeLabels = {
    'direct-predictive':     { label: 'Direct prediction', cls: 'sw-nt-type--direct' },
    'typological':           { label: 'Typological',        cls: 'sw-nt-type--typology' },
    'typological-predictive':{ label: 'Typological + predictive', cls: 'sw-nt-type--both' },
    'applicational':         { label: 'Applicational',      cls: 'sw-nt-type--apply' },
  };

  var html = '<div class="sw-ot-in-nt-panel">';
  html += '<div class="ws-section-title">OT Quotations in This Passage</div>';

  quotations.forEach(function(q) {
    var typeInfo = typeLabels[q.fulfillment_type] || { label: q.fulfillment_type, cls: '' };
    html += '<div class="sw-ot-block">';

    // Header
    html += '<div class="sw-ot-block__header">'
      + '<span class="sw-ot-block__refs"><a class="ref" data-ref="' + _esc(q.nt_ref) + '">' + _esc(q.nt_ref) + '</a>'
      + ' ← <a class="ref" data-ref="' + _esc(q.ot_ref) + '">' + _esc(q.ot_ref) + '</a></span>'
      + (q.quotation_marker ? '<span class="sw-ot-block__marker">"' + _esc(q.quotation_marker) + '"</span>' : '')
      + '<span class="sw-ot-type-badge ' + typeInfo.cls + '">' + typeInfo.label + '</span>'
      + '</div>';

    // Three-column compare
    html += '<div class="sw-triple-compare">'
      + '<div class="sw-triple-col sw-triple-col--mt"><div class="sw-triple-col__header">Hebrew MT</div>'
      + '<div class="sw-triple-col__text sw-triple-col__text--heb">' + _esc(q.mt_hebrew || '—') + '</div></div>'
      + '<div class="sw-triple-col sw-triple-col--lxx"><div class="sw-triple-col__header">Greek LXX</div>'
      + '<div class="sw-triple-col__text">' + _esc(q.lxx_greek || '—') + '</div></div>'
      + '<div class="sw-triple-col sw-triple-col--nt"><div class="sw-triple-col__header">NT Text</div>'
      + '<div class="sw-triple-col__text">' + _esc(q.nt_greek || '—') + '</div></div>'
      + '</div>';

    // Key differences
    if (q.key_differences && q.key_differences.length) {
      html += '<div class="sw-ot-diffs">';
      q.key_differences.forEach(function(diff) {
        html += '<div class="sw-diff-highlight"><span class="sw-diff-highlight__word">' + _esc(diff.word) + '</span>'
          + '<span class="sw-diff-highlight__note">' + _esc(diff.note) + '</span></div>';
      });
      html += '</div>';
    }

    // Interpretation note
    if (q.interpretation_note) {
      html += '<div class="sw-ot-block__note">' + _esc(q.interpretation_note) + '</div>';
    }

    html += '</div>';
  });

  html += '</div>';
  return html;
}

// INTENT: Render the Author Frequency section (SW-J) in the dossier. Shows per-author
//   normalized rates as a small heat map with peak-author badge. Only rendered at Student+.
//   Authors with zero rate are hidden to keep the display compact.
// CHANGE? If author group labels change in build-author-frequencies.py, update NT_AUTHORS
//   and OT_AUTHORS maps here so labels match the JSON keys.
// VERIFY: Click G1343 (δικαιοσύνη) → Paul has highlighted peak badge; relative rates visible.
function _renderAuthorFreqSection(code, lang) {
  var key    = lang === 'greek' ? 'greek' : 'hebrew';
  var cache  = _authorFreqCache[key];
  if (!cache) return '';
  var entry  = cache[code];
  if (!entry || !entry.rates) return '';

  var NT_AUTHORS = ['Paul', 'John', 'Luke', 'Matthew', 'Mark', 'Peter', 'Hebrews', 'James', 'Jude'];
  var OT_AUTHORS = ['Moses', 'Historical', 'Wisdom', 'Major', 'Minor'];
  var authors    = lang === 'greek' ? NT_AUTHORS : OT_AUTHORS;

  var maxRate = Math.max.apply(null, Object.values(entry.rates));
  if (maxRate === 0) return '';

  var cells = '';
  authors.forEach(function(author) {
    var rate = entry.rates[author] || 0;
    if (!rate) return;
    var intensity = Math.ceil((rate / maxRate) * 4);
    var isPeak    = author === entry.peak;
    cells += '<div class="sw-author-cell' + (isPeak ? ' sw-author-cell--peak' : '') + '" title="' + _esc(author) + ': ' + rate.toFixed(2) + '/1000 words">'
      + '<div class="sw-author-cell__bar sw-author-heat--' + intensity + '"></div>'
      + '<span class="sw-author-cell__label">' + _esc(author.slice(0, 4)) + '</span>'
      + (isPeak ? '<span class="sw-author-cell__peak-badge">★</span>' : '')
      + '</div>';
  });

  if (!cells) return '';
  return '<div class="ws-section sw-author-freq-section" data-depth-min="2">'
    + '<div class="ws-section-title">Author Frequency <span class="ws-section-note">— normalized per 1,000 words</span></div>'
    + '<div class="sw-author-grid">' + cells + '</div>'
    + '</div>';
}

// INTENT: Render the Semantic Neighborhood section (SW-I) in the dossier. Shows the top
//   PMI co-occurring words as clickable chips — clicking navigates to that word's dossier.
//   Rendered at Scholar depth only since PMI requires interpretation to use correctly.
// CHANGE? If the co-count threshold should appear in the display, add it to the chip title.
//   If chip click should also update the queue highlight, call _renderQueueActive() after.
// VERIFY: Click H2617 (חֶסֶד hesed) → "Semantic Neighborhood" chips include אֱמֶת, אֱמוּנָה.
//   Click one of those chips → dossier navigates to that entry.
function _renderSemanticSection(code, lang) {
  var key      = lang === 'greek' ? 'greek' : 'hebrew';
  var cache    = _semanticCache[key];
  if (!cache) return '';
  var neighbors = cache[code];
  if (!neighbors || !neighbors.length) return '';

  var html = '<div class="ws-section sw-semantic-section" data-depth-min="3">'
    + '<div class="ws-section-title">Semantic Neighborhood <span class="ws-section-note">— words that travel together in the corpus (PMI)</span></div>'
    + '<div class="sw-semantic-chips">';

  // Show top 8 neighbors
  var topN = neighbors.slice(0, 8);
  topN.forEach(function(n) {
    var entry = _getEntry(n.code);
    var lemma = entry ? (entry.lemma || '') : '';
    var gloss = entry ? (entry.gloss || '').split(',')[0] : n.code;
    html += '<span class="sw-semantic-chip" data-code="' + _esc(n.code) + '" role="button" tabindex="0"'
      + ' title="' + _esc(n.code) + ' ' + _esc(lemma) + ' — PMI ' + n.pmi + '">'
      + (lemma ? '<span class="sw-semantic-chip__lemma">' + _esc(lemma) + '</span>' : '')
      + '<span class="sw-semantic-chip__gloss">' + _esc(gloss) + '</span>'
      + '<span class="sw-semantic-chip__code">' + _esc(n.code) + '</span>'
      + '</span>';
  });

  html += '</div>'
    + '<p class="sw-semantic-note">PMI = pointwise mutual information. Higher = these words co-occur more than random chance across the biblical corpus.</p>'
    + '</div>';
  return html;
}

// INTENT: Render the "Second Temple Context" dossier section for a clicked Strong's code.
//   Finds all context entries where strongs_keys[] includes the code. If the current passage
//   is active, also includes entries whose trigger_passages overlap with the passage.
//   Rendered at Scholar depth (data-depth-min="3") since this is specialist background.
// CHANGE? If this should show at Student depth for key entries, change data-depth-min to "2".
//   If the section should appear only in passage mode, add a _passageMode guard.
// VERIFY: Click G3056 (λόγος) → "Second Temple Context" card appears with Philo entry.
//   Click G5207 (υἱός) → Son of Man (1 Enoch) and son-of-x idiom context entries appear.
function _renderSTContext(code) {
  if (!_stContextCache || !_stContextCache.length) return '';

  // Find entries matching this Strong's code
  var matches = _stContextCache.filter(function(e) {
    return (e.strongs_keys || []).indexOf(code) >= 0;
  });

  // Also include trigger_passages matches if in passage mode
  if (_passageRef) {
    _stContextCache.forEach(function(e) {
      if (matches.indexOf(e) >= 0) return;  // already in
      var tps = e.trigger_passages || [];
      for (var i = 0; i < tps.length; i++) {
        var parsed = parseRef(tps[i]);
        if (!parsed) continue;
        if (parsed.bookId !== _passageRef.bookId) continue;
        if (parsed.ch < _passageRef.ch || parsed.ch > _passageRef.endCh) continue;
        matches.push(e);
        break;
      }
    });
  }

  if (!matches.length) return '';

  var html = '<div class="ws-section sw-st-section" data-depth-min="3">'
    + '<div class="ws-section-title">Second Temple Context <span class="ws-section-note">— Jewish background for this word/passage</span></div>';

  matches.forEach(function(e) {
    html += '<div class="sw-st-card">'
      + '<div class="sw-st-card__header">'
      + '<span class="sw-st-source-chip">' + _esc(e.source) + '</span>'
      + '<span class="sw-st-work">' + _esc(e.source_work || '') + '</span>'
      + (e.source_date ? '<span class="sw-st-date">' + _esc(e.source_date) + '</span>' : '')
      + '</div>'
      + '<p class="sw-st-context">' + _esc(e.context) + '</p>'
      + '<p class="sw-st-significance">' + _esc(e.significance) + '</p>'
      + (e.representative_quote
          ? '<blockquote class="sw-st-quote">' + _esc(e.representative_quote) + '</blockquote>'
          : '')
      + '</div>';
  });

  html += '</div>';
  return html;
}

// INTENT: Check whether a debate's trigger_passages overlap with the current study passage.
//   Returns the matching trigger refs as strings (for display), or all triggers if no passage active.
// CHANGE? If _passageRef format changes (bookId/ch/v/endCh/endV), update comparison logic here.
// VERIFY: Study Rom 3:22 → πίστις Χριστοῦ debate shows "Active in this passage: Rom 3:22".
//   Study John 1 → pistis-christou debate does NOT appear (no trigger matches).
function _debateTriggerMatches(debate) {
  if (!_passageRef) return debate.trigger_passages || [];  // browse mode: show all triggers
  var matches = [];
  (debate.trigger_passages || []).forEach(function(trigStr) {
    var parsed = parseRef(trigStr);
    if (!parsed) return;
    if (parsed.bookId !== _passageRef.bookId) return;
    if (parsed.ch < _passageRef.ch || parsed.ch > _passageRef.endCh) return;
    if (parsed.ch === _passageRef.ch && parsed.v < _passageRef.v) return;
    if (parsed.ch === _passageRef.endCh && parsed.v > _passageRef.endV) return;
    matches.push(trigStr);
  });
  return matches;
}

// INTENT: Build the Contested Interpretation HTML for the dossier. If the clicked
//   word's code appears in any debate's strongs_keys AND the current passage contains
//   a trigger reference (or no passage is active), render a two-position debate card.
//   Shows position labels, renderings, named proponents, and why-it-matters callout.
// CHANGE? If the grammar-debates.json schema changes (position_c added, field renames),
//   update the HTML generation loop here. If the section should only show in Scholar depth,
//   add data-depth-min="3" to the wrapper.
// VERIFY: Study Gal 2:16 → click G4102 → "Contested Interpretation" card with πίστις
//   Χριστοῦ debate, both positions, proponents, and why-it-matters callout.
//   Study John 1:1 → click G2316 → θεὸς ἦν ὁ λόγος debate card appears.
function _renderDebateSection(code) {
  const debates = _debatesByCode[code];
  if (!debates || !debates.length) return '';

  const STATUS_LABELS = {
    'major-debate': { label: 'Major ongoing debate', cls: 'sw-debate-status--major' },
    'moderate':     { label: 'Significant debate',   cls: 'sw-debate-status--moderate' },
    'settled':      { label: 'Largely settled',      cls: 'sw-debate-status--settled' },
  };

  let html = '';
  debates.forEach(function(debate) {
    const triggers = _debateTriggerMatches(debate);
    // In passage mode, only show if there's a trigger match in the current passage
    if (_passageRef && triggers.length === 0) return;

    const status = STATUS_LABELS[debate.scholarly_status] || { label: debate.scholarly_status, cls: '' };
    const positions = [debate.position_a, debate.position_b, debate.position_c].filter(Boolean);

    html += '<div class="sw-debate-card" data-debate-id="' + _esc(debate.id) + '">'
      + '<div class="sw-debate-card__header">'
      + '<span class="sw-debate-card__icon">⚖</span>'
      + '<div class="sw-debate-card__title">' + _esc(debate.label) + '</div>'
      + '<span class="sw-debate-status ' + status.cls + '">' + _esc(status.label) + '</span>'
      + '</div>';

    if (debate.construction) {
      html += '<div class="sw-debate-card__construction">Construction: <em>' + _esc(debate.construction) + '</em></div>';
    }

    if (triggers.length > 0) {
      html += '<div class="sw-debate-card__triggers">Active in this passage: '
        + triggers.map(function(t) { return '<span class="sw-debate-trigger-ref">' + _esc(t) + '</span>'; }).join(', ')
        + '</div>';
    }

    html += '<div class="sw-debate-positions">';
    positions.forEach(function(pos, i) {
      const letters = ['A', 'B', 'C'];
      html += '<div class="sw-debate-position">'
        + '<div class="sw-debate-position__header">'
        + '<span class="sw-debate-position__letter">' + letters[i] + '</span>'
        + '<span class="sw-debate-position__label">' + _esc(pos.label) + '</span>'
        + '</div>'
        + '<div class="sw-debate-position__rendering">&ldquo;' + _esc(pos.rendering) + '&rdquo;</div>'
        + '<p class="sw-debate-position__arg">' + _esc(pos.argument) + '</p>';
      if (pos.proponents && pos.proponents.length) {
        html += '<div class="sw-debate-position__proponents">'
          + pos.proponents.map(function(p) {
              return '<span class="sw-proponent-chip">' + _esc(p) + '</span>';
            }).join('')
          + '</div>';
      }
      html += '</div>';
    });
    html += '</div>'; // .sw-debate-positions

    if (debate.why_it_matters) {
      html += '<div class="sw-debate-card__why"><strong>Why it matters:</strong> ' + _esc(debate.why_it_matters) + '</div>';
    }

    html += '</div>'; // .sw-debate-card
  });

  if (!html) return '';
  return '<div class="ws-section sw-debates-section" data-depth-min="2"><div class="ws-section-title">Contested Interpretation</div>' + html + '</div>';
}

// INTENT: Build the "Idiom Alert" dossier section for a clicked Strong's code.
//   If the code appears in _idiomsIndex, renders a card for each matching idiom entry
//   explaining what the idiom means and why English readers miss it. Returns '' if
//   no idioms match or if idiom data is not yet loaded.
// CHANGE? If idioms.json schema changes (cultural_meaning, plain_english, key_passages
//   fields), update the HTML template below. If this section should be depth-gated,
//   add data-depth-min="2" to the wrapper div.
// VERIFY: Study John 1 → click G5207 (υἱός) → "Idiom Alert" section appears with
//   "Son of X / Children of X" and "Son of Man" cards, each with plain-English explanation.
function _renderIdiomAlertSection(code) {
  if (!_idiomsIndex || !_idiomsData) return '';
  const ids = _idiomsIndex[code];
  if (!ids || !ids.length) return '';

  let html = '';
  ids.forEach(function(id) {
    const idiom = _idiomsData[id];
    if (!idiom) return;
    html += '<div class="sw-idiom-alert-card">';
    html += '<div class="sw-idiom-alert-card__phrase">' + _esc(idiom.phrase) + '</div>';
    if (idiom.plain_english) {
      html += '<div class="sw-idiom-alert-card__plain">' + _esc(idiom.plain_english) + '</div>';
    }
    if (idiom.cultural_meaning) {
      html += '<details class="sw-idiom-details"><summary>Full cultural explanation</summary>'
        + '<p class="sw-idiom-details__body">' + _esc(idiom.cultural_meaning) + '</p>';
      if (idiom.significance) {
        html += '<p class="sw-idiom-details__sig"><strong>Significance:</strong> ' + _esc(idiom.significance) + '</p>';
      }
      html += '</details>';
    }
    if (idiom.key_passages && idiom.key_passages.length) {
      html += '<div class="sw-idiom-alert-card__refs">Key passages: '
        + idiom.key_passages.map(function(r) {
            return '<a class="ref" data-ref="' + _esc(r) + '">' + _esc(r) + '</a>';
          }).join(' · ')
        + '</div>';
    }
    html += '</div>'; // .sw-idiom-alert-card
  });

  if (!html) return '';
  return '<div class="ws-section sw-idiom-alert-section" data-depth-min="1">'
    + '<div class="ws-section-title">Idiom Alert <span class="ws-section-note">— culturally loaded expression</span></div>'
    + html
    + '</div>';
}

// INTENT: Collect all idioms triggered by Strong's codes in the current passage tiles
//   and return HTML for a collapsible panel shown above the tiles. Each matching idiom
//   gets a compact chip in the panel; clicking one opens its details inline.
//   Returns '' if no idioms match any token in the passage or if idioms not loaded.
// CHANGE? If _renderPassageTiles HTML structure changes (tile data-strongs attribute),
//   the caller in _renderPassageTiles must still pass the collected code set.
// VERIFY: Study John 1:1-18 → collapsible "Idioms in This Passage" panel above tiles
//   shows chips for at least "Son of Man" and "Son of X" (G5207 appears in verse 51 if
//   in range, or G3056 Logos). Panel can be opened/closed via the details element.
function _renderPassageIdioms(codesInPassage) {
  if (!_idiomsIndex || !_idiomsData) return '';
  const seen = {};   // idiom id → true (dedup across multiple code triggers)
  codesInPassage.forEach(function(code) {
    const ids = _idiomsIndex[code];
    if (ids) ids.forEach(function(id) { seen[id] = true; });
  });
  const ids = Object.keys(seen);
  if (!ids.length) return '';

  let html = '<details class="sw-idiom-panel"><summary class="sw-idiom-panel__summary">'
    + '<span class="sw-idiom-panel__badge">' + ids.length + '</span>'
    + ' Idiom' + (ids.length > 1 ? 's' : '') + ' in This Passage'
    + '</summary><div class="sw-idiom-panel__body">';

  ids.forEach(function(id) {
    const idiom = _idiomsData[id];
    if (!idiom) return;
    html += '<div class="sw-idiom-panel__item">'
      + '<div class="sw-idiom-panel__item-phrase">' + _esc(idiom.phrase) + '</div>'
      + '<div class="sw-idiom-panel__item-plain">' + _esc(idiom.plain_english || idiom.cultural_meaning || '') + '</div>'
      + '</div>';
  });

  html += '</div></details>';
  return html;
}

// INTENT: Show passage tiles within verse-mode container; hide browse and empty-state panels.
// CHANGE? If new panels are added to sw-verse-mode, add them to the hidden list here.
// VERIFY: Study John 1:1 → tiles appear; browse panel and empty state are hidden.
function _switchToPassageMode() {
  _passageMode = true;
  document.getElementById('ws-browse-panel').hidden  = true;
  document.getElementById('sw-verse-empty').hidden   = true;
  document.getElementById('sw-passage-view').hidden  = false;
}

// INTENT: Return to the empty / entry state when a passage is closed.
//   Browse vocabulary has been replaced by the Word Study dictionary tab,
//   so closing a passage now returns to the blank entry prompt.
// CHANGE? If a new landing state is added to sw-verse-mode, show it here instead.
// VERIFY: Study John 1:1 → click ✕ Close → passage hides, entry prompt shows.
function _switchToBrowseMode() {
  _passageMode = false;
  document.getElementById('sw-passage-view').hidden     = true;
  document.getElementById('sw-verse-empty').hidden      = false;
  const actionsBar = document.getElementById('sw-passage-actions');
  if (actionsBar) actionsBar.hidden = true;
}

// INTENT: Navigate to the verse immediately before or after the currently loaded passage.
//   Uses _interData chapter keys to find chapter boundaries (no separate fetch needed).
//   Stops at the first/last verse of the book rather than overflowing into the next book.
// CHANGE? If _passageRef or _interData structure changes, update chapter/verse lookup here.
// VERIFY: Study John 1:51 → click Next → John 2:1 loads. Study John 1:1 → click Prev → button does nothing.
function _navVerse(delta) {
  if (!_passageRef || !_interData) return;
  var ch = _passageRef.ch;
  var v  = _passageRef.v;
  var bookId = _passageRef.bookId;

  var newV = v + delta;
  var newCh = ch;

  if (delta === 1) {
    var maxV = Math.max.apply(null, Object.keys(_interData[String(ch)] || {}).map(Number));
    if (newV > maxV) {
      var maxCh = Math.max.apply(null, Object.keys(_interData).map(Number));
      if (ch >= maxCh) return; // already at last verse of book
      newCh = ch + 1;
      newV = 1;
    }
  } else {
    if (newV < 1) {
      if (ch <= 1) return; // already at first verse of book
      newCh = ch - 1;
      var prevChData = _interData[String(newCh)] || {};
      newV = Math.max.apply(null, Object.keys(prevChData).map(Number));
    }
  }

  var bookName = _passageRef.bookName || bookId;
  _studyPassage(bookName + ' ' + newCh + ':' + newV);
}

async function _studyPassage(refStr) {
  // INTENT: loadBooks() populates bookLookup which parseRef() requires. It resolves
  //   from cache on repeat calls so there is no visible delay after the first study.
  //   Always switches to Verse Study mode first so the tiles column is visible.
  // CHANGE? If loadBooks() signature changes in core.js, update this await.
  // VERIFY: Type "John 1:1" on first page load and click Study Passage — tiles render.
  _setStudyMode('verse');
  await loadBooks();
  const parsed = parseRef(refStr);
  if (!parsed) {
    const header = document.getElementById('sw-passage-header');
    if (header) header.innerHTML = '<span class="sw-passage-err">Reference not recognised — try "John 1:1" or "Romans 8:1-4"</span>';
    _switchToPassageMode();
    return;
  }
  _passageRef = parsed;
  _pushRecentPassage(refStr.trim());
  _renderNav();

  // INTENT: Push the studied passage into the URL so refresh/share/back preserves it.
  //   ?ref= is already read on load (line ~5110); this closes the read-write symmetry.
  // CHANGE? If URL scheme changes from ?ref= to ?passage=, update both here and the load-time param read below.
  // VERIFY: Study John 1:1 → URL bar updates to ?ref=John+1%3A1; refresh → passage reloads.
  history.replaceState(null, '', '?ref=' + encodeURIComponent(refStr.trim()));

  _originalWordOrder = false;
  const isHebrew = !NT_BOOKS.has(parsed.bookId);
  const header = document.getElementById('sw-passage-header');
  if (header) header.innerHTML = '<span class="sw-passage-ref-label">' + _esc(parsed.display) + '</span>'
    + (isHebrew ? '<button type="button" class="sw-word-order-btn ws-btn ws-btn--sm" id="sw-word-order-btn" title="Toggle original Hebrew word order (right-to-left)">&#x2194; Order</button>' : '')
    + '<button type="button" class="sw-close-passage ws-btn ws-btn--sm" id="sw-close-passage-btn">✕ Close</button>';

  const tilesEl = document.getElementById('sw-ptiles');
  if (tilesEl) tilesEl.innerHTML = '<span class="sw-ptile-loading">Loading…</span>';

  _switchToPassageMode();

  // INTENT: Toggle Hebrew tile direction RTL/LTR so the user can view tokens in
  //   original right-to-left reading flow vs. English left-to-right presentation.
  // CHANGE? If tile container id changes from sw-ptiles, update selector here.
  // VERIFY: Study Genesis 1:1 → click Order button → tiles wrap right-to-left; click again → LTR restored.
  var wordOrderBtn = document.getElementById('sw-word-order-btn');
  if (wordOrderBtn) {
    wordOrderBtn.addEventListener('click', function () {
      _originalWordOrder = !_originalWordOrder;
      var tilesEl2 = document.getElementById('sw-ptiles');
      if (tilesEl2) tilesEl2.classList.toggle('sw-ptiles--rtl', _originalWordOrder);
      wordOrderBtn.classList.toggle('ws-btn--active', _originalWordOrder);
      wordOrderBtn.title = _originalWordOrder
        ? 'Showing original Hebrew order (RTL) — click for English order (LTR)'
        : 'Toggle original Hebrew word order (right-to-left)';
    });
  }

  // Wire close button
  const closeBtn = document.getElementById('sw-close-passage-btn');
  if (closeBtn) closeBtn.addEventListener('click', function () { _switchToBrowseMode(); });

  // INTENT: Show prev/next verse navigation bar. Verse bounds are checked against
  //   _interData after it loads; the bar is wired now and _updateVerseNavBar() refreshes
  //   disabled state after data resolves.
  // CHANGE? If _interData structure changes (chapter keys as strings), update _navVerse().
  // VERIFY: Study John 1:1 → nav bar visible; click Next → John 1:2 loads; at John 1:51 → John 2:1 loads.
  var verseNavBar = document.getElementById('sw-verse-nav-bar');
  var verseNavLabel = document.getElementById('sw-verse-nav-label');
  if (verseNavBar) {
    verseNavBar.hidden = false;
    if (verseNavLabel) verseNavLabel.textContent = parsed.display || '';
    var prevBtn = document.getElementById('sw-prev-verse-btn');
    var nextBtn = document.getElementById('sw-next-verse-btn');
    if (prevBtn) prevBtn.onclick = function() { _navVerse(-1); };
    if (nextBtn) nextBtn.onclick = function() { _navVerse(1); };
  }

  // INTENT: Load passage-specific notes from localStorage and wire auto-save on input.
  //   Each passage gets its own localStorage key so notes are not overwritten when switching passages.
  // CHANGE? If SK_DECISIONS key scheme changes, update the bsw_ws_notes_ prefix here.
  // VERIFY: Study John 1:1, type a note → reload page, study John 1:1 again → note persists.
  //   Study Romans 1:1 → notes field is empty (different passage key).
  const notesTa  = document.getElementById('sw-passage-notes-ta');
  const noteKey  = 'bsw_ws_notes_' + refStr.trim().toLowerCase().replace(/\s+/g, '_');
  if (notesTa) {
    try { notesTa.value = localStorage.getItem(noteKey) || ''; } catch(e) {}
    notesTa.oninput = function() {
      try { localStorage.setItem(noteKey, notesTa.value); } catch(e) {}
    };
  }

  // SW-N: Show export sheet button and wire it to _exportStudySheet(parsed, noteKey)
  // INTENT: Export button is only shown in passage mode. Click triggers window.print() after
  //   writing a print-only overlay with passage ref + interlinear HTML + active dossier + notes.
  //   Uses @media print CSS to hide the normal UI and show only sw-print-sheet.
  // CHANGE? If the dossier selector (#ws-dossier) changes, update the querySelector below.
  // VERIFY: Study Romans 8:1, click "Export Study Sheet" → print dialog opens; preview shows
  //   passage ref, word tiles, current dossier entry, user notes.
  const actionsBar = document.getElementById('sw-passage-actions');
  if (actionsBar) actionsBar.hidden = false;
  const exportBtn = document.getElementById('sw-export-sheet-btn');
  if (exportBtn) {
    exportBtn.onclick = function() { _exportStudySheet(parsed, noteKey); };
  }

  try {
    const lang = NT_BOOKS.has(parsed.bookId) ? 'greek' : 'hebrew';
    const [interData, strongsDict, particles, bibleBook] = await Promise.all([
      loadInterlinear(parsed.bookId),
      loadStrongs(lang),
      _loadParticles(lang),
      loadBook(getVersion(), parsed.bookId).catch(function() { return null; }),
      _loadMorphSig(lang),
      _loadDebates(),
      _loadLiterary(),
      _loadIdioms(),
      _loadCultural(),
      _loadCognates(lang),
      _loadOTinNT(),
      _loadSTContext(),
      _loadAuthorFreq(lang),
      _loadSemanticFields(lang),
    ]);
    _interData = interData;  // cache for Word Study concordance
    _renderPassageTiles(parsed, interData, strongsDict, particles, bibleBook);
  } catch (err) {
    if (tilesEl) tilesEl.innerHTML = '<span class="sw-ptile-loading">Could not load interlinear data.</span>';
  }
}

// INTENT: Render the Literary Structure tab content for the current passage.
//   Shows: (1) book genre badge + literary note, (2) structural diagram if a matching
//   structure entry exists for this pericope, (3) literary devices glossary intro.
//   All data comes from the preloaded _literaryCache — no additional fetch needed.
// CHANGE? If literary JSON schemas change (genre fields, structure element fields),
//   update this function. If the tab is renamed in the HTML, update the data-tab value.
// VERIFY: Study John 1:1–18 → Literary Structure tab → "gospel" badge, sub-genres listed,
//   chiasm diagram renders with color-coded element rows and the center highlighted.
function _renderLiteraryTab(parsed) {
  const genre      = (_literaryCache.genre || {})[parsed.bookId] || null;
  const structures = (_literaryCache.structures || []);

  // Find structural entries that overlap with the current passage
  const matchingStructures = structures.filter(function(s) {
    if (s.bookId !== parsed.bookId) return false;
    // Check if the structure range overlaps the current passage range
    const sStart = s.ch_start * 1000 + (s.v_start || 1);
    const sEnd   = s.ch_end   * 1000 + (s.v_end   || 999);
    const pStart = parsed.ch  * 1000 + parsed.v;
    const pEnd   = parsed.endCh * 1000 + parsed.endV;
    return sStart <= pEnd && sEnd >= pStart;
  });

  let html = '<div class="sw-literary-tab">';

  // ── Genre badge
  if (genre) {
    html += '<div class="sw-genre-block">'
      + '<span class="sw-genre-badge sw-genre-badge--' + _esc(genre.genre) + '">' + _esc(genre.genre) + '</span>';
    if (genre.sub && genre.sub.length) {
      html += genre.sub.map(function(s) {
        return '<span class="sw-genre-sub-badge">' + _esc(s) + '</span>';
      }).join('');
    }
    html += '</div>';
    if (genre.literary_note) {
      html += '<p class="sw-literary-note">' + _esc(genre.literary_note) + '</p>';
    }
    if (genre.structure_note) {
      html += '<p class="sw-structure-note"><strong>Structure:</strong> ' + _esc(genre.structure_note) + '</p>';
    }
  }

  // ── Structural diagrams for matching pericopes
  matchingStructures.forEach(function(s) {
    const TYPE_ICONS = {
      'chiasm':       '⊕',
      'hymn':         '♫',
      'narrative':    '◆',
      'discourse':    '→',
      'anaphora':     '≡',
      'parallel':     '∥',
      'lament':       '◐',
      'antithetical': '⟺',
      'intercalation':'⧖',
      'acrostic':     'א',
    };
    const icon = TYPE_ICONS[s.structure_type] || '◇';

    html += '<div class="sw-structure-block">'
      + '<div class="sw-structure-block__header">'
      + '<span class="sw-structure-icon">' + icon + '</span>'
      + '<span class="sw-structure-label">' + _esc(s.label) + '</span>'
      + '<span class="sw-structure-type-badge">' + _esc(s.structure_type) + '</span>'
      + '</div>';

    if (s.note) {
      html += '<p class="sw-structure-note-detail">' + _esc(s.note) + '</p>';
    }

    if (s.elements && s.elements.length) {
      html += '<div class="sw-structure-elements">';
      s.elements.forEach(function(el) {
        const isCenter = el.id === 'X' || el.id.includes('X') || el.label.includes('★');
        html += '<div class="sw-structure-el' + (isCenter ? ' sw-structure-el--center' : '') + '">'
          + '<span class="sw-structure-el__id">' + _esc(el.id) + '</span>'
          + '<span class="sw-structure-el__ref">' + _esc(el.ref) + '</span>'
          + '<span class="sw-structure-el__label">' + _esc(el.label) + '</span>'
          + '</div>';
      });
      html += '</div>';
    }

    html += '</div>'; // .sw-structure-block
  });

  if (!matchingStructures.length && !genre) {
    html += '<p class="sw-tab-stub">No literary structure data for this passage yet. More passages will be added progressively.</p>';
  }

  // ── Literary devices glossary (collapsible reference, always visible)
  const devices = _literaryCache.devices || [];
  if (devices.length) {
    html += '<details class="sw-devices-glossary">'
      + '<summary class="sw-devices-glossary__toggle">Literary Devices Reference (' + devices.length + ' terms)</summary>'
      + '<div class="sw-devices-glossary__body">';
    devices.forEach(function(d) {
      html += '<div class="sw-device-entry">'
        + '<span class="sw-device-entry__name">' + _esc(d.label || '') + '</span>';
      if (d.symbol) {
        html += '<code class="sw-device-entry__sym">' + _esc(d.symbol) + '</code>';
      }
      html += '<span class="sw-device-entry__def">' + _esc(d.plain || '') + '</span>';
      if (d.significance) {
        html += '<span class="sw-device-entry__sig">' + _esc(d.significance) + '</span>';
      }
      if (d.examples && d.examples.length) {
        html += '<span class="sw-device-entry__ex">'
          + d.examples.map(function(ex) {
            return '<strong>' + _esc(ex.ref) + '</strong> — ' + _esc(ex.note);
          }).join('; ')
          + '</span>';
      }
      html += '</div>';
    });
    html += '</div></details>';
  }

  html += '</div>'; // .sw-literary-tab
  return html;
}

// INTENT: Render the Cultural Context tab for the current passage (SW-F).
//   Shows: (1) applicable cultural frameworks for this book (from _culturalCache.frameworks),
//   (2) book-specific context notes (from _culturalCache.bookContext[bookId]),
//   (3) a symbols reference accordion. All data from _culturalCache — no additional fetch.
// CHANGE? If cultural data schema changes (key_cultural_notes, cultural_frameworks fields),
//   update the rendering logic below. If this tab should be depth-gated, add sw-depth-N
//   wrappers around individual sections.
// VERIFY: Study Romans 1:1 → "Cultural Context" tab shows "Honor and Shame" framework primer
//   + Romans-specific context notes about Jewish/Gentile tensions. Study John 1:1 →
//   shows "Second Temple Judaism" and "Temple, Presence..." frameworks.
function _renderCulturalTab(parsed) {
  const bookCtx    = (_culturalCache.bookContext || {})[parsed.bookId] || null;
  const frameworks = _culturalCache.frameworks  || [];
  const symbols    = _culturalCache.symbols     || {};

  let html = '<div class="sw-cultural-tab">';

  // ── Book context section
  if (bookCtx) {
    html += '<div class="sw-cultural-book-ctx">';
    html += '<div class="ws-section-title">' + _esc(parsed.bookId.charAt(0).toUpperCase() + parsed.bookId.slice(1)) + ' — Historical Context</div>';
    if (bookCtx.historical_context) {
      html += '<p class="sw-cultural-book-ctx__hist">' + _esc(bookCtx.historical_context) + '</p>';
    }
    if (bookCtx.key_cultural_notes && bookCtx.key_cultural_notes.length) {
      html += '<div class="sw-cultural-notes">';
      bookCtx.key_cultural_notes.forEach(function(note) {
        html += '<div class="sw-cultural-note">💡 ' + _esc(note) + '</div>';
      });
      html += '</div>';
    }
    html += '</div>';
  }

  // ── Applicable framework primers
  const applicableFrameworks = bookCtx && bookCtx.cultural_frameworks
    ? frameworks.filter(function(fw) {
        return bookCtx.cultural_frameworks.includes(fw.id);
      })
    : [];

  if (applicableFrameworks.length) {
    html += '<div class="ws-section-title" style="margin-top:.8rem;">Relevant Cultural Frameworks</div>';
    applicableFrameworks.forEach(function(fw) {
      html += '<details class="sw-framework-block"><summary class="sw-framework-block__summary">' + _esc(fw.title) + '</summary>';
      html += '<div class="sw-framework-block__body">';
      if (fw.summary) html += '<p class="sw-framework-block__summary-text">' + _esc(fw.summary) + '</p>';
      if (fw.what_it_means_for_reading) {
        html += '<div class="sw-framework-block__reading"><strong>For reading this passage:</strong> ' + _esc(fw.what_it_means_for_reading) + '</div>';
      }
      if (fw.key_concepts && fw.key_concepts.length) {
        html += '<div class="sw-framework-block__concepts">';
        fw.key_concepts.forEach(function(kc) {
          html += '<div class="sw-concept-row">'
            + '<span class="sw-concept-row__term">' + _esc(kc.term) + '</span>'
            + '<span class="sw-concept-row__def">' + _esc(kc.explanation) + '</span>'
            + '</div>';
        });
        html += '</div>';
      }
      if (fw.key_passages && fw.key_passages.length) {
        html += '<div class="sw-framework-block__passages">Key passages: '
          + fw.key_passages.map(function(r) {
              return '<a class="ref" data-ref="' + _esc(r) + '">' + _esc(r) + '</a>';
            }).join(' · ')
          + '</div>';
      }
      html += '</div></details>'; // .sw-framework-block
    });
  }

  // ── Symbols reference (collapsible)
  const symCategories = Object.keys(symbols);
  if (symCategories.length) {
    html += '<details class="sw-symbols-ref"><summary class="sw-symbols-ref__summary">Biblical Symbols Reference</summary>';
    html += '<div class="sw-symbols-ref__body">';
    const catLabels = { numbers: 'Numbers', colors: 'Colors', spatial: 'Spatial', cosmological: 'Light, Elements & Cosmos' };
    symCategories.forEach(function(cat) {
      const items = symbols[cat];
      if (!items || !items.length) return;
      html += '<div class="sw-symbol-cat"><div class="sw-symbol-cat__label">' + _esc(catLabels[cat] || cat) + '</div>';
      items.forEach(function(sym) {
        html += '<div class="sw-symbol-row">'
          + '<span class="sw-symbol-row__sym">' + _esc(sym.symbol) + '</span>'
          + '<div class="sw-symbol-row__info">'
          + '<span class="sw-symbol-row__meaning">' + _esc(sym.meaning) + '</span>'
          + (sym.note ? '<span class="sw-symbol-row__note">' + _esc(sym.note) + '</span>' : '')
          + '</div></div>';
      });
      html += '</div>'; // .sw-symbol-cat
    });
    html += '</div></details>';
  }

  if (!bookCtx && !applicableFrameworks.length) {
    html += '<p class="sw-tab-stub">Cultural context data coming soon for this book.</p>';
  }

  html += '</div>'; // .sw-cultural-tab
  return html;
}

// INTENT: Render a single synthesis pericope card for SW-M.
//   Shows: pericope label, literary note, key terms (clickable code chips), cultural notes,
//   intertextual connections, synthesis paragraph, and tradition map accordion. All sections
//   except key terms and synthesis body are depth-gated so Reader mode sees the essentials.
// CHANGE? If synthesis JSON schema changes (key_terms[], tradition_map fields), update here.
//   Depth gate: cultural_notes + tradition_map hidden at depth-1, revealed at depth 2+.
// VERIFY: Study John 1:1-18 → Synthesis tab → all sections render; click G3056 chip →
//   dossier opens for λόγος. Tradition map accordions open/close. Reader depth hides cultural.
function _renderSynthesisPericope(key, d) {
  var html = '<div class="sw-synthesis-pericope">';

  // ── Header
  html += '<div class="sw-synthesis-header">'
    + '<span class="sw-synthesis-ref">' + _esc(key) + '</span>'
    + '<h3 class="sw-synthesis-label">' + _esc(d.pericope_label || '') + '</h3>'
    + '</div>';

  // ── Literary note (all depths)
  if (d.literary_note) {
    html += '<section class="sw-synthesis-section">'
      + '<div class="sw-synthesis-section-title">Literary Note</div>'
      + '<p class="sw-synthesis-literary">' + _esc(d.literary_note) + '</p>'
      + '</section>';
  }

  // ── Key terms with clickable code chips (all depths)
  if (d.key_terms && d.key_terms.length) {
    html += '<section class="sw-synthesis-section"><div class="sw-synthesis-section-title">Key Terms</div>'
      + '<div class="sw-synthesis-kterm-list">';
    d.key_terms.forEach(function(kt) {
      html += '<div class="sw-synthesis-kterm">'
        + '<button class="sw-synthesis-kterm-chip" data-code="' + _esc(kt.code) + '">' + _esc(kt.code) + '</button>'
        + '<span class="sw-synthesis-kterm-note">' + _esc(kt.note) + '</span>'
        + '</div>';
    });
    html += '</div></section>';
  }

  // ── Synthesis paragraph (all depths — core payoff)
  if (d.synthesis) {
    html += '<section class="sw-synthesis-section sw-synthesis-main">'
      + '<div class="sw-synthesis-section-title">Synthesis</div>'
      + '<p class="sw-synthesis-body">' + _esc(d.synthesis) + '</p>'
      + '</section>';
  }

  // ── Cultural notes (Student+ depth)
  if (d.cultural_notes && d.cultural_notes.length) {
    html += '<section class="sw-synthesis-section" data-depth-min="2">'
      + '<div class="sw-synthesis-section-title">Cultural Background</div>';
    d.cultural_notes.forEach(function(note) {
      html += '<p class="sw-synthesis-note">' + _esc(note) + '</p>';
    });
    html += '</section>';
  }

  // ── Intertextual connections (all depths)
  if (d.intertextual_connections && d.intertextual_connections.length) {
    html += '<section class="sw-synthesis-section">'
      + '<div class="sw-synthesis-section-title">Intertextual Connections</div>'
      + '<ul class="sw-synthesis-connections">';
    d.intertextual_connections.forEach(function(conn) {
      html += '<li class="sw-synthesis-conn">' + _esc(conn) + '</li>';
    });
    html += '</ul></section>';
  }

  // ── Tradition map accordion (Student+ depth)
  if (d.tradition_map) {
    var tm = d.tradition_map;
    html += '<section class="sw-synthesis-section sw-tradition-block" data-depth-min="2">'
      + '<div class="sw-synthesis-section-title">Tradition Map</div>';
    if (tm.patristic) {
      html += '<details class="sw-tradition-details"><summary class="sw-tradition-era">Patristic</summary>'
        + '<p class="sw-tradition-text">' + _esc(tm.patristic) + '</p></details>';
    }
    if (tm.reformation) {
      html += '<details class="sw-tradition-details"><summary class="sw-tradition-era">Reformation</summary>'
        + '<p class="sw-tradition-text">' + _esc(tm.reformation) + '</p></details>';
    }
    if (tm.modern_debates && tm.modern_debates.length) {
      html += '<details class="sw-tradition-details"><summary class="sw-tradition-era">Modern Debates</summary>'
        + '<ul class="sw-tradition-debates">';
      tm.modern_debates.forEach(function(debate) {
        html += '<li class="sw-tradition-debate">' + _esc(debate) + '</li>';
      });
      html += '</ul></details>';
    }
    html += '</section>';
  }

  html += '</div>'; // .sw-synthesis-pericope
  return html;
}

// INTENT: Render the Synthesis tab for the current passage (SW-M).
//   Finds all pericopes in the loaded synthesis file that overlap the current passage
//   range using chapter:verse arithmetic. Shows "no synthesis" message for unmatched passages.
//   Delegates chip clicks to _openWord() so key term codes navigate the dossier.
// CHANGE? If more synthesis files are added (data/synthesis/*.json), they will be picked up
//   automatically — this function only looks at the already-loaded bookId entries.
// VERIFY: Study John 1:1-18 → Synthesis tab → "The Prologue" card renders.
//   Study John 5:1-15 → "no synthesis notes" message + list of available pericopes shows.
function _renderSynthesisTab(parsed) {
  var entries = _synthesisCache[parsed.bookId];
  if (!entries || !entries.length) {
    return '<p class="sw-tab-stub">No synthesis notes for this passage yet.</p>';
  }

  // Find pericopes that overlap the current passage
  var qStart = parsed.ch * 1000 + parsed.v;
  var qEnd   = parsed.endCh * 1000 + parsed.endV;
  var matches = entries.filter(function(e) {
    var pStart = e.ref.ch * 1000 + e.ref.v;
    var pEnd   = e.ref.endCh * 1000 + e.ref.endV;
    return pStart <= qEnd && qStart <= pEnd;
  });

  if (!matches.length) {
    var avail = entries.map(function(e) { return e.key; }).join(' · ');
    return '<p class="sw-tab-stub">No synthesis notes for this passage range. '
      + 'Available pericopes: <em>' + _esc(avail) + '</em>.</p>';
  }

  var html = '<div class="sw-synthesis-tab">';
  matches.forEach(function(e) { html += _renderSynthesisPericope(e.key, e.data); });
  html += '</div>';
  return html;
}

// INTENT: Build the "What to notice here" auto-summary banner (SW-O integration).
//   Scans the set of Strong's codes present in the passage against all pre-loaded caches
//   (particles, idioms, debates, literary) and produces a scannable list of analytical
//   observations the reader might miss. Returns '' if no notable items found.
// CHANGE? If a new cache (second-temple, OT-in-NT) is added to _studyPassage(), add a
//   corresponding detection block here. If the banner should only appear at Student+,
//   add a _depth check before building the html.
// VERIFY: Study Gal 2:16 → notice banner lists discourse markers, πίστις Χριστοῦ debate,
//   faith idiom. Study John 1:1-18 → lists chiasm structure, Logos debate, Son of Man idiom.
function _renderPassageNoticeBanner(parsed, codesInPassage, seenFunctions, particles) {
  const items = [];

  // ── Discourse markers present
  if (seenFunctions.size > 0) {
    const fnLabels = {
      'ground': 'ground/reason (γάρ / כִּי)', 'inference': 'inference (οὖν / לָכֵן)',
      'contrast': 'contrast (ἀλλά)', 'strong-contrast': 'strong contrast',
      'adversative': 'adversative', 'purpose': 'purpose (ἵνα)',
      'result': 'result (ὥστε)', 'condition': 'condition (εἰ)',
      'cause': 'cause', 'negation': 'negation', 'negation-prohibition': 'prohibition (μή)',
      'immediacy': 'immediacy (הִנֵּה)', 'focus': 'focus',
    };
    const uniqueFns = [];
    seenFunctions.forEach(function(fn) { if (fnLabels[fn]) uniqueFns.push(fnLabels[fn]); });
    if (uniqueFns.length) {
      items.push({ icon: '◉', label: 'Discourse markers', detail: uniqueFns.slice(0, 4).join(', ') + (uniqueFns.length > 4 ? '…' : '') });
    }
  }

  // ── Contested interpretations triggered
  if (_debatesByCode) {
    const triggeredDebates = [];
    codesInPassage.forEach(function(code) {
      const debates = _debatesByCode[code];
      if (!debates) return;
      debates.forEach(function(d) {
        const matches = _debateTriggerMatches(d);
        if (matches.length && !triggeredDebates.find(function(x) { return x.id === d.id; })) {
          triggeredDebates.push(d);
        }
      });
    });
    if (triggeredDebates.length) {
      items.push({ icon: '⚑', label: 'Contested interpretation' + (triggeredDebates.length > 1 ? 's' : ''), detail: triggeredDebates.map(function(d) { return d.label.split('—')[0].trim(); }).slice(0, 3).join(' · ') });
    }
  }

  // ── Idioms in passage
  if (_idiomsIndex) {
    const idiomIds = {};
    codesInPassage.forEach(function(code) {
      const ids = _idiomsIndex[code];
      if (ids) ids.forEach(function(id) { idiomIds[id] = true; });
    });
    const count = Object.keys(idiomIds).length;
    if (count) {
      const phrases = Object.keys(idiomIds).slice(0, 3).map(function(id) {
        return _idiomsData && _idiomsData[id] ? _idiomsData[id].phrase.split('(')[0].trim() : id;
      });
      items.push({ icon: '💬', label: count + ' culturally loaded idiom' + (count > 1 ? 's' : ''), detail: phrases.join(' · ') + (count > 3 ? '…' : '') });
    }
  }

  // ── Literary structure match
  if (_literaryCache.structures) {
    const matching = _literaryCache.structures.filter(function(s) {
      if (s.bookId !== parsed.bookId) return false;
      const sStart = s.ch_start * 1000 + (s.v_start || 0);
      const sEnd   = s.ch_end   * 1000 + (s.v_end   || 999);
      const pStart = parsed.ch  * 1000 + (parsed.v   || 0);
      const pEnd   = parsed.endCh * 1000 + (parsed.endV || 999);
      return sStart <= pEnd && sEnd >= pStart;
    });
    if (matching.length) {
      items.push({ icon: '📐', label: 'Literary structure', detail: matching.map(function(s) { return s.label; }).join(' · ') });
    }
  }

  // ── Cultural frameworks applicable to this book
  if (_culturalCache.bookContext && _culturalCache.frameworks) {
    const bookCtx = _culturalCache.bookContext[parsed.bookId];
    if (bookCtx && bookCtx.cultural_frameworks && bookCtx.cultural_frameworks.length) {
      const fwLabels = bookCtx.cultural_frameworks.slice(0, 3).map(function(id) {
        const fw = _culturalCache.frameworks.find(function(f) { return f.id === id; });
        return fw ? fw.title : id;
      });
      items.push({ icon: '🏛', label: 'Cultural lens', detail: fwLabels.join(' · ') });
    }
  }

  if (!items.length) return '';

  // INTENT: Open banner automatically on first study of a passage; collapse it on revisit
  //   so it doesn't push tiles below the fold when the user already knows what's there.
  // CHANGE? If parsed ref format changes, update the sessionStorage key construction below.
  // VERIFY: Study Gal 2:16 → banner opens automatically. Navigate away and re-study Gal 2:16 → banner starts collapsed.
  var refKey = 'bsw_ws_banner_seen_' + (parsed.bookId || '') + '_' + (parsed.ch || '') + '_' + (parsed.v || '');
  var seenBefore = sessionStorage.getItem(refKey);
  sessionStorage.setItem(refKey, '1');

  let html = '<details class="sw-notice-banner"' + (seenBefore ? '' : ' open') + '><summary class="sw-notice-banner__summary">'
    + '<span class="sw-notice-banner__icon">👁</span>'
    + '<span class="sw-notice-banner__title">What to notice in this passage</span>'
    + '<span class="sw-notice-banner__count">' + items.length + ' item' + (items.length !== 1 ? 's' : '') + '</span>'
    + '</summary><ul class="sw-notice-banner__list">';

  items.forEach(function(item) {
    html += '<li class="sw-notice-banner__item">'
      + '<span class="sw-notice-banner__item-icon">' + item.icon + '</span>'
      + '<span class="sw-notice-banner__item-body">'
      + '<span class="sw-notice-banner__item-label">' + _esc(item.label) + '</span>'
      + (item.detail ? '<span class="sw-notice-banner__item-detail">' + _esc(item.detail) + '</span>' : '')
      + '</span></li>';
  });

  html += '</ul></details>';
  return html;
}

// INTENT: Render interlinear token tiles for a passage reference, annotating any
//   discourse particles with a colored left-border and function badge (SW-B).
//   Particles arg may be null/empty — tiles still render without annotation.
// CHANGE? If tile HTML structure changes, update sw-ptile CSS selectors in workshop.css.
//   If particles JSON schema changes (color/function fields), update annotation logic here.
// VERIFY: Study Romans 8:1-11 → οὖν tile (G3767) has blue left-border + "inference" badge.
//   Study Ps 23 → כִּי tiles (H3588) have sienna left-border + "because/that" badge.
// INTENT: Render interlinear tiles for the given passage range. If bibleBook is supplied
//   (the versioned translation data), show the translation text above each verse's tiles so
//   the reader can correlate English rendering with original-language words immediately.
// CHANGE? If bibleBook data shape changes from {ch:{v:"text"}}, update the accessor below.
// VERIFY: Study John 1:1 → translation text "In the beginning was the Word…" appears above
//   the interlinear tiles. Verse number is clickable to open verse-study for that verse.
function _renderPassageTiles(parsed, interData, strongsDict, particles, bibleBook) {
  const tilesEl  = document.getElementById('sw-ptiles');
  const tabsEl   = document.getElementById('sw-passage-tabs');
  const tabCont  = document.getElementById('sw-tab-content');
  if (!tilesEl || !interData) {
    if (tilesEl) tilesEl.innerHTML = '<span class="sw-ptile-loading">No interlinear data for this passage.</span>';
    return;
  }

  // Build legend showing which particle functions appear in this passage
  const seenFunctions = new Set();
  const startCh = parsed.ch;
  const endCh   = parsed.endCh;

  // First pass: collect which particle functions appear (for legend) and all codes (for idioms)
  const codesInPassage = new Set();
  for (let ch = startCh; ch <= endCh; ch++) {
    const chData = interData[String(ch)];
    if (!chData) continue;
    const vStart = (ch === startCh) ? parsed.v    : 1;
    const vEnd   = (ch === endCh)   ? parsed.endV : 999;
    for (let v = vStart; v <= vEnd; v++) {
      const tokens = chData[String(v)];
      if (!tokens) continue;
      tokens.forEach(function(tok) {
        if (tok.s) codesInPassage.add(tok.s);
        if (particles && tok.s && particles[tok.s]) seenFunctions.add(particles[tok.s].function);
      });
    }
  }

  // Legend bar (only if particles are present in passage)
  const LEGEND_LABELS = {
    'ground': 'ground', 'inference': 'inference', 'contrast': 'contrast',
    'strong-contrast': 'contrast', 'adversative': 'contrast', 'limitation': 'contrast',
    'limitation-assurance': 'contrast', 'exception-contrast': 'contrast',
    'continue': 'continue', 'additive': 'continue', 'additive-temporal': 'continue',
    'additive-intensifier': 'continue', 'temporal-transition': 'continue',
    'contrast-setup': 'continue', 'relative': 'continue', 'entreaty': 'continue',
    'purpose': 'purpose', 'result': 'result', 'manner-result': 'result',
    'condition': 'condition', 'condition-possible': 'condition',
    'cause': 'cause', 'causal-or-means': 'cause', 'content-or-cause': 'cause',
    'negation': 'negation', 'negation-fact': 'negation', 'negation-process': 'negation',
    'negation-prohibition': 'negation', 'immediacy': 'immediacy', 'focus': 'focus',
  };
  const legendGroups = new Set();
  seenFunctions.forEach(function(fn) { if (LEGEND_LABELS[fn]) legendGroups.add(LEGEND_LABELS[fn]); });

  let legendHtml = '';
  if (legendGroups.size > 0) {
    legendHtml = '<div class="sw-markers-bar"><span class="sw-markers-bar__label">Discourse markers:</span>';
    legendGroups.forEach(function(g) {
      legendHtml += '<span class="sw-marker-legend sw-marker-legend--' + g + '">' + g + '</span>';
    });
    legendHtml += '</div>';
  }

  let html = '';
  for (let ch = startCh; ch <= endCh; ch++) {
    const chData = interData[String(ch)];
    if (!chData) continue;
    const vStart = (ch === startCh) ? parsed.v    : 1;
    const vEnd   = (ch === endCh)   ? parsed.endV : 999;

    for (var v = vStart; v <= vEnd; v++) {
      const tokens = chData[String(v)];
      if (!tokens || !tokens.length) continue;

      // Translation text for this verse (from loaded Bible version)
      var verseText = bibleBook && bibleBook[String(ch)] && bibleBook[String(ch)][String(v)];

      html += '<div class="sw-verse-row">';
      html += '<span class="sw-verse-num">' + ch + ':' + v + '</span>';
      if (verseText) {
        html += '<div class="sw-verse-translation">' + _esc(verseText) + '</div>';
      }
      html += '<span class="sw-tiles-wrap">';
      tokens.forEach(function (tok) {
        const sEntry    = strongsDict && tok.s && strongsDict[tok.s];
        const particle  = particles && tok.s && particles[tok.s];
        const lemma     = (sEntry && sEntry.lemma)  || '';
        const gloss     = tok.text || (sEntry && sEntry.gloss) || '';
        const pClass    = particle ? (' sw-particle--' + particle.function) : '';
        const pTitle    = particle ? (' — ' + particle.function_label) : '';
        html += '<span class="sw-ptile' + pClass + '" data-strongs="' + _esc(tok.s || '') + '"'
          + ' data-lemma="' + _esc(lemma) + '" data-gloss="' + _esc(gloss) + '"'
          + ' tabindex="0" role="button"'
          + (tok.s ? ' title="' + _esc(tok.s) + ' ' + _esc(lemma) + pTitle + '"' : '') + '>'
          + (lemma ? '<span class="sw-ptile__lemma">' + _esc(lemma) + '</span>' : '')
          + '<span class="sw-ptile__eng">' + _esc(gloss) + '</span>'
          + (tok.s ? '<span class="sw-ptile__s">' + _esc(tok.s) + '</span>' : '')
          + (particle ? '<span class="sw-ptile__badge" data-abbr="' + _esc(particle.function_label.charAt(0).toUpperCase()) + '">' + _esc(particle.function_label.split(' ')[0].toLowerCase()) + '</span>' : '')
          + '</span>';
      });
      html += '</span></div>';
    }
  }

  const noticeBanner = _renderPassageNoticeBanner(parsed, codesInPassage, seenFunctions, particles);
  const idiomPanel   = _renderPassageIdioms(codesInPassage);
  tilesEl.innerHTML = (noticeBanner + idiomPanel + legendHtml + html) || '<span class="sw-ptile-loading">No tokens found for this passage.</span>';
  tilesEl.querySelectorAll('.sw-verse-translation').forEach(autoTagTermsWhenReady);

  // Wire tile click → open dossier
  // Shared tooltip element for tile hover previews
  var _hoverTip = document.getElementById('sw-tile-tooltip');
  if (!_hoverTip) {
    _hoverTip = document.createElement('div');
    _hoverTip.id = 'sw-tile-tooltip';
    _hoverTip.className = 'sw-tile-tooltip';
    document.body.appendChild(_hoverTip);
  }
  var _hoverTimer = null;

  tilesEl.querySelectorAll('.sw-ptile[data-strongs]').forEach(function (tile) {
    tile.addEventListener('click', function () {
      const code = tile.dataset.strongs;
      if (code) {
        tilesEl.querySelectorAll('.sw-ptile').forEach(function (t) { t.classList.remove('sw-ptile--active'); });
        tile.classList.add('sw-ptile--active');
        _hoverTip.hidden = true;
        _openWord(code);
      }
    });
    tile.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); tile.click(); }
    });

    // INTENT: Show a micro-tooltip on hover with gloss + lemma — lets users scan
    //   word meanings without opening the full dossier for every word.
    // CHANGE? If tile data attributes change (data-strongs, data-gloss, data-lemma), update below.
    // VERIFY: Hover over a tile for 400ms → small tooltip appears with gloss text; move away → hides.
    tile.addEventListener('mouseenter', function () {
      clearTimeout(_hoverTimer);
      _hoverTimer = setTimeout(function() {
        var gloss = tile.dataset.gloss || '';
        var lemma = tile.dataset.lemma || '';
        if (!gloss && !lemma) return;
        var rect = tile.getBoundingClientRect();
        _hoverTip.innerHTML = (lemma ? '<span class="sw-tile-tooltip__lemma">' + _esc(lemma) + '</span>' : '')
          + (gloss ? '<span class="sw-tile-tooltip__gloss">' + _esc(gloss) + '</span>' : '');
        _hoverTip.hidden = false;
        // Position above the tile, centered
        var tipW = _hoverTip.offsetWidth || 120;
        var left = rect.left + rect.width / 2 - tipW / 2;
        _hoverTip.style.left = Math.max(4, Math.min(left, window.innerWidth - tipW - 4)) + 'px';
        _hoverTip.style.top  = (rect.top + window.scrollY - _hoverTip.offsetHeight - 6) + 'px';
      }, 380);
    });
    tile.addEventListener('mouseleave', function () {
      clearTimeout(_hoverTimer);
      _hoverTip.hidden = true;
    });
  });

  // Show passage tabs once tiles are rendered
  if (tabsEl)  tabsEl.hidden  = false;
  if (tabCont) tabCont.hidden = false;

  // Wire tab buttons — literary tab renders live data (SW-D); others still stub
  // INTENT: Tab click updates active state and renders the appropriate content.
  //   Literary tab is fully implemented (SW-D). Cultural/Intertextual/Synthesis are
  //   stubs until SW-F/K/M are implemented.
  // CHANGE? When implementing SW-F (cultural), replace the 'cultural' stub with a call
  //   to _renderCulturalTab(parsed). Same pattern for SW-K and SW-M.
  // VERIFY: Study John 1:1-18, click "Literary Structure" tab → genre badge + chiasm diagram.
  //   Click "Cultural Context" → stub message shows SW-F placeholder.
  if (tabsEl) {
    tabsEl.querySelectorAll('.sw-tab-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        tabsEl.querySelectorAll('.sw-tab-btn').forEach(function (b) { b.classList.remove('sw-tab-btn--active'); });
        btn.classList.add('sw-tab-btn--active');
        if (tabCont) {
          if (btn.dataset.tab === 'literary') {
            tabCont.innerHTML = _renderLiteraryTab(parsed);
          } else if (btn.dataset.tab === 'cultural') {
            tabCont.innerHTML = _renderCulturalTab(parsed);
          } else if (btn.dataset.tab === 'intertextual') {
            // SW-K: Render OT-in-NT panel for the current passage
            var quotations = _findRelevantQuotations();
            if (quotations.length) {
              tabCont.innerHTML = _renderOTinNTPanel(quotations);
              // Re-wire any .ref links the panel introduced
              if (window.wireRefLinks) window.wireRefLinks(tabCont);
            } else {
              tabCont.innerHTML = '<p class="sw-tab-stub">No formal OT quotations identified in this passage. '
                + 'See the Literary Structure tab for allusions and echoes.</p>';
            }
          } else if (btn.dataset.tab === 'synthesis') {
            // SW-M: Load per-book synthesis data lazily, then render
            // INTENT: Synthesis files are per-book and only fetched on first Synthesis tab click.
            //   _loadSynthesis returns immediately if already cached; await ensures render
            //   always sees populated _synthesisCache[bookId].
            // CHANGE? If synthesis becomes eager (pre-warmed in _studyPassage Promise.all),
            //   remove the _loadSynthesis call here and render synchronously.
            // VERIFY: Click Synthesis tab on Romans 1:16 → loading flashes, then pericope card appears.
            tabCont.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading synthesis…</p>';
            _loadSynthesis(parsed.bookId).then(function() {
              tabCont.innerHTML = _renderSynthesisTab(parsed);
              // Wire key term code chips → open dossier
              tabCont.querySelectorAll('.sw-synthesis-kterm-chip[data-code]').forEach(function(chip) {
                chip.addEventListener('click', function() { _openWord(chip.dataset.code); });
              });
              if (window.wireRefLinks) window.wireRefLinks(tabCont);

              // SW-N: User synthesis notes textarea — persisted per passage ref
              // INTENT: Appends an editable textarea to the synthesis tab so users can write
              //   their own synthesis alongside the curated content. Saves to localStorage
              //   per-passage on input so notes survive navigation.
              // CHANGE? If the synthesis tab is split across multiple render calls, move this
              //   to a separate function called at the end of each synthesis render.
              // VERIFY: Study John 1:1, click Synthesis, type a note → navigate away → return
              //   → synthesis tab re-renders and user note is pre-populated.
              var synNotesKey = 'bsw_ws_synthesis_' + (parsed.display || '').replace(/\s+/g, '_');
              var synNoteHtml = '<div class="sw-synthesis-user-notes">'
                + '<div class="sw-synthesis-section-title">My Synthesis Notes</div>'
                + '<textarea class="sw-synthesis-notes-ta" rows="4" placeholder="Write your own synthesis for this passage — your reading, applications, questions…"></textarea>'
                + '</div>';
              tabCont.insertAdjacentHTML('beforeend', synNoteHtml);
              var synTa = tabCont.querySelector('.sw-synthesis-notes-ta');
              if (synTa) {
                try { synTa.value = localStorage.getItem(synNotesKey) || ''; } catch(e) {}
                synTa.oninput = function() {
                  try { localStorage.setItem(synNotesKey, synTa.value); } catch(e) {}
                };
              }
            });
          } else if (btn.dataset.tab === 'crossrefs') {
            // INTENT: Load cross-references for each verse in the passage and render them
            //   as clickable ref chips that open a passage study when clicked.
            // CHANGE? If loadCrossRefs data shape changes ({ch_v: [...]}), update accessor below.
            // VERIFY: Study John 3:16 → Cross-refs tab → related verses listed; click one → passage opens.
            tabCont.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading cross-references…</p>';
            _renderCrossRefsTab(parsed, tabCont);
          } else if (btn.dataset.tab === 'commentary') {
            // INTENT: Load and display commentaries for individual verses in the passage range.
            //   Uses the same loadCommentary() infrastructure as verse-study.js but scoped
            //   to the passage. Shows one collapsible block per commentary source per verse.
            // CHANGE? If COMMENTARY_SOURCES changes in core.js, update the source list imported here.
            // VERIFY: Study Romans 8:1 → Commentary tab → Ellicott/Matthew Henry text appears.
            tabCont.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading commentaries…</p>';
            _renderCommentaryTab(parsed, tabCont);
          } else if (btn.dataset.tab === 'grammar') {
            // INTENT: Show layer-1 particle/morph tokens and layer-2 mkt-original prose notes.
            // CHANGE? If mkt-original JSON schema changes ({ch:{v:html}}), update _renderGrammarTab.
            // VERIFY: Study Romans 1:1 → Grammar tab → particle table + prose commentary appears.
            tabCont.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading grammar notes…</p>';
            _renderGrammarTab(parsed, tabCont);
          } else if (btn.dataset.tab === 'dossier') {
            // INTENT: Re-render the last opened word's dossier into the tab content area.
            //   If no word has been opened yet, show a prompt to click a tile.
            // CHANGE? If _lastWordCode variable is renamed, update reference below.
            // VERIFY: Click a tile → Word tab active with dossier. Click Literary → switch back.
            //   Click Word tab again → same word still shown.
            if (_lastWordCode && _getEntry(_lastWordCode)) {
              tabCont.innerHTML = '';
              _renderDossier(_lastWordCode, tabCont, !_translationMode);
            } else {
              tabCont.innerHTML = '<p class="sw-tab-stub">Click any word tile to see its lexical dossier here.</p>';
            }
          } else {
            tabCont.innerHTML = '';
          }
        }
      });
    });
    // Auto-render literary tab on first passage load (it's the default active tab)
    if (tabCont) tabCont.innerHTML = _renderLiteraryTab(parsed);
  }
}

// INTENT: Looks up a Strong's code in any loaded phase cache, then falls back to
//   loading the full all-greek/all-hebrew index. Opens the existing dossier once data
//   is available. This is the bridge between passage tile clicks and the translator dossier.
// CHANGE? If _getEntry() logic changes (e.g., reads from a new source), this function
//   may already find the entry without the fallback fetch.
// VERIFY: Click G3056 (λόγος) in a passage tile — dossier should show the full
//   lexical entry even if only phase1 is loaded (λόγος is a top-100 NT word).
// INTENT: Open a word's dossier. In verse study mode, renders into the "Word" tab of
//   the right panel. In translation mode or word study mode, renders into $dossier.
// CHANGE? If _studyMode values change, update the verse-mode branch condition below.
// VERIFY: In verse mode, click a tile → Word tab activates with full dossier content.
async function _openWord(code) {
  _lastWordCode = code;

  // Determine render target: verse mode → Word tab; otherwise → main dossier column
  var verseTabTarget = null;
  if (_studyMode === 'verse' && !_translationMode) {
    var tabCont = document.getElementById('sw-tab-content');
    var tabsEl  = document.getElementById('sw-passage-tabs');
    if (tabCont && tabsEl) {
      tabsEl.querySelectorAll('.sw-tab-btn').forEach(function(b) { b.classList.remove('sw-tab-btn--active'); });
      var dossierBtn = tabsEl.querySelector('[data-tab="dossier"]');
      if (dossierBtn) dossierBtn.classList.add('sw-tab-btn--active');
      tabCont.removeAttribute('hidden');
      verseTabTarget = tabCont;
    }
  }

  var isCompact = !!(verseTabTarget && !_translationMode);

  // Try cached phases first (fast path)
  if (_getEntry(code)) {
    _renderDossier(code, verseTabTarget, isCompact);
    _uiState.activeCode = code;
    _renderQueueActive();
    return;
  }
  // Load the appropriate full index and retry
  const fallback = code.startsWith('G') ? 'all-greek' : 'all-hebrew';
  try {
    await _loadPhase(fallback);
  } catch (e) { /* silent */ }
  if (_getEntry(code)) {
    _renderDossier(code, verseTabTarget, isCompact);
    _uiState.activeCode = code;
  } else {
    // Word not in any source — show minimal entry from Strongs data
    const lang = code.startsWith('G') ? 'greek' : 'hebrew';
    const sdict = await loadStrongs(lang).catch(function () { return null; });
    const sEntry = sdict && sdict[code];
    if (sEntry) {
      document.getElementById('ws-dossier').innerHTML =
        '<div class="ws-dossier"><div class="ws-dossier-head">'
        + '<div class="ws-dossier-head__top">'
        + '<span class="ws-dossier__code">' + _esc(code) + '</span>'
        + '<span class="ws-dossier__lemma">' + _esc(sEntry.lemma || '') + '</span>'
        + (sEntry.translit ? '<span class="ws-dossier__translit">' + _esc(sEntry.translit) + '</span>' : '')
        + '</div></div>'
        + '<div class="ws-section" data-depth-min="1"><div class="ws-section-title">Gloss</div>'
        + '<p>' + _esc(sEntry.gloss || '') + '</p></div>'
        + '<div class="ws-section" data-depth-min="1"><div class="ws-section-title">Definition</div>'
        + '<p>' + _esc(sEntry.def || '') + '</p></div>'
        + '<p class="ws-placeholder" style="font-size:.8rem;margin-top:1rem">Full dossier not available — word is outside the curated vocabulary sets.</p>'
        + '</div>';
    }
  }
}

/* ── SW-N: Vocabulary Flashcard System ────────────────────── */

// INTENT: Load flashcard deck and progress from localStorage on page init.
//   Deck is stored as { greek: [...codes], hebrew: [...codes] }. Progress is
//   { code: { due: ISOdate, interval: days } }. Called once during initWorkshopPage.
// CHANGE? If the deck format adds language auto-detection (by code prefix), update here.
// VERIFY: After adding G3056 to deck and reloading → _fcDeck.greek contains G3056.
function _fcLoadState() {
  try {
    var raw = JSON.parse(localStorage.getItem(SK_FC_DECK) || '{}');
    _fcDeck.greek   = new Set(raw.greek   || []);
    _fcDeck.hebrew  = new Set(raw.hebrew  || []);
  } catch(e) { _fcDeck = { greek: new Set(), hebrew: new Set() }; }
  try {
    _fcProgress = JSON.parse(localStorage.getItem(SK_FC_PROGRESS) || '{}');
  } catch(e) { _fcProgress = {}; }
}

function _fcSaveDeck() {
  try {
    localStorage.setItem(SK_FC_DECK, JSON.stringify({
      greek:  Array.from(_fcDeck.greek),
      hebrew: Array.from(_fcDeck.hebrew),
    }));
  } catch(e) {}
}

function _fcSaveProgress() {
  try { localStorage.setItem(SK_FC_PROGRESS, JSON.stringify(_fcProgress)); } catch(e) {}
}

function _isInDeck(code) {
  return code.startsWith('G') ? _fcDeck.greek.has(code) : _fcDeck.hebrew.has(code);
}

// INTENT: Toggle a word code in/out of the custom flashcard deck.
//   Updates the ★/☆ button state immediately and updates the nav badge count.
//   Saves the updated deck to localStorage.
// CHANGE? If deck has a max size or deduplication rule, add guard here.
// VERIFY: Click ☆ on G3056 → button becomes ★, nav badge count increases by 1.
function _fcToggleDeck(code) {
  var set = code.startsWith('G') ? _fcDeck.greek : _fcDeck.hebrew;
  if (set.has(code)) {
    set.delete(code);
  } else {
    set.add(code);
  }
  _fcSaveDeck();
  _fcUpdateBadge();
  // Re-render the ★/☆ button state in the dossier if it's open for this code
  var btn = document.querySelector('.sw-add-deck-btn[data-code="' + code + '"]');
  if (btn) {
    btn.textContent = _isInDeck(code) ? '★' : '☆';
    btn.title = _isInDeck(code) ? 'Remove from flashcard deck' : 'Add to flashcard deck';
  }
}

function _fcUpdateBadge() {
  var badge = document.getElementById('sw-fc-due-badge');
  if (!badge) return;
  var now = new Date();
  var dueCount = 0;
  var allCodes = [..._fcDeck.greek, ..._fcDeck.hebrew];
  allCodes.forEach(function(code) {
    var p = _fcProgress[code];
    if (!p || new Date(p.due) <= now) dueCount++;
  });
  badge.textContent = dueCount > 0 ? dueCount : '';
  badge.hidden = dueCount === 0;
}

// INTENT: Build the queue of due cards for this flashcard session.
//   A card is due if it has no progress record or its due date is in the past.
//   Shuffled for variety. Then renders the first card.
// CHANGE? If a "cram all" mode is added, bypass the due-date filter.
// VERIFY: After rating a card "Good" → it disappears from queue for 7 days.
function _fcOpenView() {
  var now = new Date();
  var allCodes = [..._fcDeck.greek, ..._fcDeck.hebrew];
  _fcQueue = allCodes.filter(function(code) {
    var p = _fcProgress[code];
    return !p || new Date(p.due) <= now;
  });
  // Shuffle
  for (var i = _fcQueue.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = _fcQueue[i]; _fcQueue[i] = _fcQueue[j]; _fcQueue[j] = tmp;
  }
  _fcIdx      = 0;
  _fcReviewed = 0;

  var view = document.getElementById('sw-flashcard-view');
  var layout = document.getElementById('ws-layout');
  if (view)   view.hidden   = false;
  if (layout) layout.hidden = true;

  var label = document.getElementById('sw-fc-deck-label');
  if (label) label.textContent = allCodes.length + ' words in deck';

  if (_fcQueue.length === 0) {
    _fcShowDone(allCodes.length);
  } else {
    _fcShowCard(_fcQueue[0]);
  }
}

function _fcCloseView() {
  var view   = document.getElementById('sw-flashcard-view');
  var layout = document.getElementById('ws-layout');
  if (view)   view.hidden   = true;
  if (layout) layout.hidden = false;
  _fcUpdateBadge();
}

// INTENT: Render the front face of a flashcard for the given Strong's code.
//   Looks up the entry in any loaded phase cache; falls back to Strongs data.
//   The back face (gloss, freq, samples) is hidden until the user taps "Reveal".
// CHANGE? If the dossier source changes (new phases), update the _getEntry fallback logic.
// VERIFY: Open flashcard for G26 → front shows ἀγαπάω; reveal → gloss + 3 verse samples appear.
async function _fcShowCard(code) {
  var front  = document.getElementById('sw-fc-front');
  var back   = document.getElementById('sw-fc-back');
  var done   = document.getElementById('sw-fc-done');
  var prog   = document.getElementById('sw-fc-progress-label');
  if (!front || !back) return;

  front.hidden = false;
  back.hidden  = true;
  if (done) done.hidden = true;

  var remaining = _fcQueue.length - _fcIdx;
  if (prog) prog.textContent = remaining + ' remaining · ' + _fcReviewed + ' reviewed';

  // Look up entry (try cached phases first)
  var entry = _getEntry(code);
  if (!entry) {
    try {
      await _loadPhase(code.startsWith('G') ? 'phase1' : 'phase2');
      entry = _getEntry(code);
    } catch(e) {}
  }

  var lemma    = entry ? (entry.lemma || entry.lemmas || code) : code;
  var translit = entry ? (entry.translit || '') : '';
  var pos      = entry ? (entry.pos || '') : '';
  var gloss    = entry ? (entry.gloss || entry.semantic_range || '') : '';
  var freq     = entry ? (entry._freq || 0) : 0;
  var samples  = entry ? (entry.attested_uses || []) : [];

  document.getElementById('sw-fc-word').textContent    = lemma;
  document.getElementById('sw-fc-translit').textContent = translit;

  // Back side content
  document.getElementById('sw-fc-back-word').textContent = lemma;
  document.getElementById('sw-fc-pos').textContent       = pos ? '[' + pos + ']' : '';
  document.getElementById('sw-fc-gloss').textContent     = gloss;
  document.getElementById('sw-fc-freq').textContent      = freq > 0 ? freq.toLocaleString() + '× in scripture' : '';

  var sampEl = document.getElementById('sw-fc-samples');
  if (sampEl && samples.length) {
    sampEl.innerHTML = samples.slice(0, 3).map(function(s) {
      return '<div class="sw-fc-sample">'
        + '<a class="ref" data-ref="' + _esc(s.ref) + '">' + _esc(s.ref) + '</a>'
        + ' — ' + _esc(s.gloss || s.note || '')
        + '</div>';
    }).join('');
    if (window.wireRefLinks) window.wireRefLinks(sampEl);
  } else if (sampEl) {
    sampEl.innerHTML = '';
  }

  // Update rating button labels to show the actual computed interval for this card.
  var prev  = _fcProgress[code] || {};
  var ease  = prev.ease     || 2.5;
  var previ = prev.interval || 0;
  function _nextDays(r) {
    if (previ === 0) return FC_INTERVALS[r] || 7;
    switch (r) {
      case 'again': return 1;
      case 'hard':  return Math.max(1, Math.round(previ * 1.2));
      case 'good':  return Math.max(1, Math.round(previ * ease));
      case 'easy':  return Math.max(1, Math.round(previ * ease * 1.3));
    }
    return 7;
  }
  function _dayLabel(d) { return d === 1 ? '1 day' : d < 31 ? d + ' days' : Math.round(d / 7) + ' wks'; }
  back.querySelectorAll('.sw-fc-rate-btn[data-rating]').forEach(function(btn) {
    var small = btn.querySelector('small');
    if (small) small.textContent = _dayLabel(_nextDays(btn.dataset.rating));
  });
}

function _fcReveal() {
  var front = document.getElementById('sw-fc-front');
  var back  = document.getElementById('sw-fc-back');
  if (front) front.hidden = true;
  if (back)  back.hidden  = false;
}

// INTENT: Record the user's rating using an SM-2-style ease algorithm. First review
//   uses FC_INTERVALS as seed days; subsequent reviews multiply the prior interval by
//   the entry's ease factor so well-known words graduate beyond the 21-day cap.
// CHANGE? If SRS constants change (ease floor/ceiling, Easy multiplier), update the three
//   numeric literals below and the FC_INTERVALS comment above.
// VERIFY: Rate G3056 "Easy" three consecutive sessions → intervals grow (e.g. 21 → 54 → 140
//   days) rather than capping at 21. Check bsw_ws_fc_progress in DevTools → Application.
function _fcRate(rating) {
  var code  = _fcQueue[_fcIdx];
  var prev  = _fcProgress[code] || {};
  var ease  = prev.ease     || 2.5;
  var previ = prev.interval || 0;   // 0 = first review

  var days;
  if (previ === 0) {
    // First review: use seed interval
    days = FC_INTERVALS[rating] || 7;
  } else {
    switch (rating) {
      case 'again': days = 1;                                       break;
      case 'hard':  days = Math.max(1, Math.round(previ * 1.2));   break;
      case 'good':  days = Math.max(1, Math.round(previ * ease));  break;
      case 'easy':  days = Math.max(1, Math.round(previ * ease * 1.3)); break;
      default:      days = Math.max(1, Math.round(previ * ease));
    }
  }

  // Update ease factor (SM-2 style)
  switch (rating) {
    case 'again': ease = Math.max(1.3, ease - 0.20); break;
    case 'hard':  ease = Math.max(1.3, ease - 0.15); break;
    case 'good':  /* unchanged */                     break;
    case 'easy':  ease = Math.min(3.0, ease + 0.15); break;
  }

  var due = new Date();
  due.setDate(due.getDate() + days);
  _fcProgress[code] = { due: due.toISOString(), interval: days, ease: ease };
  _fcSaveProgress();
  _fcReviewed++;
  _fcIdx++;

  if (_fcIdx >= _fcQueue.length) {
    _fcShowDone(_fcDeck.greek.size + _fcDeck.hebrew.size);
  } else {
    _fcShowCard(_fcQueue[_fcIdx]);
  }
}

function _fcShowDone(totalDeck) {
  var front = document.getElementById('sw-fc-front');
  var back  = document.getElementById('sw-fc-back');
  var done  = document.getElementById('sw-fc-done');
  if (front) front.hidden = true;
  if (back)  back.hidden  = true;
  if (!done) return;
  done.hidden = false;
  var msg = document.getElementById('sw-fc-done-msg');
  if (msg) msg.textContent = _fcReviewed > 0
    ? 'Session complete! Reviewed ' + _fcReviewed + ' card' + (_fcReviewed !== 1 ? 's' : '') + '.'
    : 'All ' + totalDeck + ' cards are up to date — nothing due right now.';
  var stats = document.getElementById('sw-fc-done-stats');
  if (stats) stats.textContent = 'Deck size: ' + totalDeck + ' words';
}

// INTENT: Keyboard shortcut handler for flashcard mode.
//   Space = reveal; 1/2/3/4 = Again/Hard/Good/Easy.
// CHANGE? If more rating levels are added, extend the key→rating map below.
// VERIFY: Study a card, press Space → back revealed; press 3 → "Good" recorded, next card shows.
function _fcKeyHandler(e) {
  var view = document.getElementById('sw-flashcard-view');
  if (!view || view.hidden) return;
  var backHidden = document.getElementById('sw-fc-back') && document.getElementById('sw-fc-back').hidden;
  if (e.key === ' ' || e.key === 'Spacebar') {
    e.preventDefault();
    if (backHidden) _fcReveal();
  } else if (!backHidden) {
    var map = { '1': 'again', '2': 'hard', '3': 'good', '4': 'easy' };
    if (map[e.key]) { e.preventDefault(); _fcRate(map[e.key]); }
  }
}

// INTENT: Generates a print-only study sheet for the current passage by collecting
//   the interlinear tile HTML, active dossier HTML, synthesis tab content, and user notes,
//   then writes them into a dedicated #sw-print-sheet div before calling window.print().
//   A @media print rule in workshop.css hides the normal layout and shows only the print sheet.
//   The print sheet is cleaned up after printing via the afterprint event.
// CHANGE? If passage tile or dossier selectors change, update querySelectorAll paths below.
//   If synthesis tab content should also print, pre-load _loadSynthesis before calling this.
// VERIFY: Study Romans 8:1, export study sheet → print preview shows: ref, tiles, notes.
//   Study John 1:1, open G3056 dossier, export → dossier content appears in print preview.
function _exportStudySheet(parsed, noteKey) {
  var tilesEl   = document.getElementById('sw-ptiles');
  var dossierEl = document.getElementById('ws-dossier');
  var tilesHtml   = tilesEl   ? tilesEl.innerHTML   : '';
  var dossierHtml = dossierEl ? dossierEl.innerHTML  : '';
  var notes = '';
  try { notes = localStorage.getItem(noteKey) || ''; } catch(e) {}

  // Synthesis content if loaded for this book
  var synEntries = _synthesisCache[parsed.bookId];
  var synHtml = '';
  if (synEntries && synEntries.length) {
    synHtml = _renderSynthesisTab(parsed);
  }

  var sheet = document.getElementById('sw-print-sheet') || document.createElement('div');
  sheet.id = 'sw-print-sheet';
  sheet.innerHTML =
    '<div class="swp-ref">' + _esc(parsed.display) + '</div>'
    + '<div class="swp-tiles">' + tilesHtml + '</div>'
    + (dossierHtml ? '<div class="swp-dossier"><h3>Word Study</h3>' + dossierHtml + '</div>' : '')
    + (synHtml     ? '<div class="swp-synthesis"><h3>Passage Synthesis</h3>' + synHtml + '</div>' : '')
    + (notes       ? '<div class="swp-notes"><h3>My Notes</h3><p>' + _esc(notes).replace(/\n/g, '<br>') + '</p></div>' : '');

  if (!document.getElementById('sw-print-sheet')) document.body.appendChild(sheet);

  window.print();
  window.addEventListener('afterprint', function cleanup() {
    window.removeEventListener('afterprint', cleanup);
    sheet.innerHTML = '';
  }, { once: true });
}

/* ── Cross-References Tab ───────────────────────────────────── */
// INTENT: Render cross-references for all verses in the passage. Each verse gets a
//   collapsible group of ref chips sorted by vote count. Clicking any chip calls
//   _studyPassage() to open that reference in the workshop.
// CHANGE? If loadCrossRefs data shape changes from {ch:{v:[[ref,votes],...]}} update accessors.
// VERIFY: Study Psalm 22:1 → Cross-refs tab → Matt 27:46, Heb 2:12 appear as chips.
async function _renderCrossRefsTab(parsed, container) {
  var data = await loadCrossRefs(parsed.bookId);
  if (!data) {
    container.innerHTML = '<p class="sw-tab-stub">No cross-references available for this book.</p>';
    return;
  }

  var html = '<div class="sw-xref-tab">';
  var anyFound = false;

  for (var ch = parsed.ch; ch <= parsed.endCh; ch++) {
    var chData = data[String(ch)];
    if (!chData) continue;
    var vStart = (ch === parsed.ch)    ? parsed.v    : 1;
    var vEnd   = (ch === parsed.endCh) ? parsed.endV : 999;

    for (var v = vStart; v <= vEnd; v++) {
      var entries = chData[String(v)];
      if (!entries || !entries.length) continue;
      anyFound = true;

      // Sort by votes desc, take top 12
      var sorted = entries.slice().sort(function(a, b) {
        return (parseCrossRefEntry(b).votes || 0) - (parseCrossRefEntry(a).votes || 0);
      }).slice(0, 12);

      html += '<div class="sw-xref-verse">'
        + '<div class="sw-xref-verse__ref">' + ch + ':' + v + '</div>'
        + '<div class="sw-xref-chips">';

      sorted.forEach(function(entry) {
        var e = parseCrossRefEntry(entry);
        if (!e.ref) return;
        var score = Math.min(100, Math.round((e.votes || 1) / 400 * 100));
        var intensity = score > 70 ? 'sw-xref-chip--hi' : (score > 35 ? 'sw-xref-chip--mid' : '');
        html += '<span class="sw-xref-chip ' + intensity + '" data-ref="' + _esc(e.ref) + '" role="button" tabindex="0">'
          + _esc(e.ref) + '</span>';
      });

      html += '</div></div>';
    }
  }

  html += '</div>';
  container.innerHTML = anyFound ? html : '<p class="sw-tab-stub">No cross-references for this verse range.</p>';

  // Wire chip clicks → _studyPassage
  container.querySelectorAll('.sw-xref-chip[data-ref]').forEach(function(chip) {
    chip.addEventListener('click', function() { _studyPassage(chip.dataset.ref); });
    chip.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); chip.click(); }
    });
  });
}

/* ── Commentary Tab (passage-level) ────────────────────────── */
// INTENT: Render all available commentary sources for each verse in the passage range.
//   Shows a source selector (persisted to localStorage), then one collapsible block per
//   verse with the commentary text from the selected source. Falls back gracefully when
//   a source has no data for the book.
// CHANGE? If COMMENTARY_SOURCES changes, the selector rerenders automatically. If the
//   commentary data schema changes ({ch:{v:html}}), update the accessor in the render loop.
// VERIFY: Study Romans 8:1 → Commentary tab → select Ellicott → verse 1 text appears.
//   Switch to Matthew Henry → different text replaces it without a page reload.
async function _renderCommentaryTab(parsed, container) {
  var src = getCommentarySource();

  // Source selector
  var selectorHtml = '<div class="sw-comm-selector">'
    + '<label class="sw-comm-selector__label">Commentary:</label>'
    + '<select class="sw-comm-selector__sel" id="sw-comm-src-sel">'
    + COMMENTARY_SOURCES.filter(function(s) { return s.id !== 'mkt' && !s.id.startsWith('mkt-'); })
        .map(function(s) {
          return '<option value="' + _esc(s.id) + '"' + (s.id === src ? ' selected' : '') + '>'
            + _esc(s.label) + '</option>';
        }).join('')
    + '</select></div>';

  container.innerHTML = selectorHtml + '<div id="sw-comm-body" class="sw-comm-body"><p class="sw-tab-stub sw-tab-stub--loading">Loading…</p></div>';

  // Wire source change
  var sel = container.querySelector('#sw-comm-src-sel');
  if (sel) {
    sel.addEventListener('change', function() {
      setCommentarySource(sel.value);
      _loadAndRenderCommentary(parsed, sel.value, container.querySelector('#sw-comm-body'));
    });
  }

  await _loadAndRenderCommentary(parsed, src, container.querySelector('#sw-comm-body'));
}

async function _loadAndRenderCommentary(parsed, srcId, bodyEl) {
  if (!bodyEl) return;
  bodyEl.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading…</p>';
  // loadCommentary now fetches one chapter at a time; this tab can span a chapter range, so
  // fetch each chapter in [parsed.ch, parsed.endCh] and merge back to the {ch:{v}} shape.
  var chList = [];
  for (var c = parsed.ch; c <= parsed.endCh; c++) chList.push(c);
  var parts = await Promise.all(chList.map(function (c) { return loadCommentary(parsed.bookId, srcId, c); }));
  var data = {};
  parts.forEach(function (part) { if (part) Object.keys(part).forEach(function (k) { data[k] = part[k]; }); });
  if (!Object.keys(data).length) {
    bodyEl.innerHTML = '<p class="sw-tab-stub">No commentary available for this book in the selected source.</p>';
    return;
  }

  var html = '';
  for (var ch = parsed.ch; ch <= parsed.endCh; ch++) {
    var chData = data[String(ch)];
    if (!chData) continue;
    var vStart = (ch === parsed.ch)    ? parsed.v    : 1;
    var vEnd   = (ch === parsed.endCh) ? parsed.endV : 999;
    for (var v = vStart; v <= vEnd; v++) {
      var text = chData[String(v)];
      if (!text) continue;
      html += '<div class="sw-comm-verse">'
        + '<div class="sw-comm-verse__ref">' + ch + ':' + v + '</div>'
        + '<div class="sw-comm-verse__text">' + text + '</div>'
        + '</div>';
    }
  }

  bodyEl.innerHTML = html || '<p class="sw-tab-stub">No commentary for this verse range.</p>';
  if (window.wireRefLinks) window.wireRefLinks(bodyEl);
}

// INTENT: Grammar tab — layer 1: per-verse particle/morphology token rows; layer 2:
//   mkt-original prose notes for the same verse range. Loads particles and mkt-original
//   in parallel; falls back gracefully when either is missing.
// CHANGE? If mkt-original JSON schema changes from {ch:{v:html}}, update accessor below.
//   If _particlesCache or _morphSigCache loading changes, update _loadParticles call.
// VERIFY: Study Romans 1:1 → Grammar tab → token rows show lemma + particle badge or POS hint;
//   prose block shows δοῦλος/ἀφωρισμένος commentary. Study Genesis 1:1 → prose block absent (no mkt-orig).
async function _renderGrammarTab(parsed, container) {
  var lang = NT_BOOKS.has(parsed.bookId) ? 'greek' : 'hebrew';
  var particles = _particlesCache[lang] || {};

  // Load particles if not yet cached
  var particlePromise = _particlesCache[lang]
    ? Promise.resolve(_particlesCache[lang])
    : _loadParticles(lang);

  // Load mkt-original prose notes (may 404 for OT — that's fine)
  var mktUrl = _resolve('../../data/commentary/mkt-original/' + parsed.bookId + '.json');
  var mktPromise = fetch(mktUrl).then(function(r) { return r.ok ? r.json() : null; }).catch(function() { return null; });

  var results = await Promise.all([particlePromise, mktPromise]);
  var particlesData = results[0] || {};
  var mktData       = results[1];

  // Build layer-1: per-verse token rows from already-loaded _interData
  var layer1Html = '';
  if (_interData) {
    for (var ch = parsed.ch; ch <= parsed.endCh; ch++) {
      var chData = _interData[String(ch)];
      if (!chData) continue;
      var vStart = (ch === parsed.ch)    ? parsed.v    : 1;
      var vEnd   = (ch === parsed.endCh) ? parsed.endV : 999;
      for (var v = vStart; v <= vEnd; v++) {
        var tokens = chData[String(v)];
        if (!tokens || !tokens.length) continue;
        layer1Html += '<div class="sw-grammar-verse">'
          + '<div class="sw-grammar-verse__ref">' + ch + ':' + v + '</div>'
          + '<table class="sw-grammar-table"><thead><tr>'
          + '<th>Word</th><th>Gloss</th><th>Code</th><th>Note</th>'
          + '</tr></thead><tbody>';
        tokens.forEach(function(tok) {
          if (!tok.s) return;
          var entry     = _getEntry(tok.s);
          var lemma     = (entry && entry.lemma)  || '';
          var gloss     = tok.text || (entry && entry.gloss) || tok.s;
          var particle  = particlesData[tok.s];
          var noteHtml  = particle
            ? '<span class="sw-grammar-particle sw-marker-legend--' + _esc(particle.function) + '">'
              + _esc(particle.function_label) + '</span>'
            : (entry && entry.pos ? '<span class="sw-grammar-pos">' + _esc(entry.pos) + '</span>' : '');
          layer1Html += '<tr>'
            + '<td class="sw-grammar-lemma">' + (lemma ? _esc(lemma) : '<span style="opacity:.5">' + _esc(tok.s) + '</span>') + '</td>'
            + '<td class="sw-grammar-gloss">' + _esc(gloss) + '</td>'
            + '<td class="sw-grammar-code">' + _esc(tok.s) + '</td>'
            + '<td class="sw-grammar-note">' + noteHtml + '</td>'
            + '</tr>';
        });
        layer1Html += '</tbody></table></div>';
      }
    }
  }

  // Build layer-2: mkt-original prose
  var layer2Html = '';
  if (mktData) {
    for (var ch2 = parsed.ch; ch2 <= parsed.endCh; ch2++) {
      var chData2 = mktData[String(ch2)];
      if (!chData2) continue;
      var vStart2 = (ch2 === parsed.ch)    ? parsed.v    : 1;
      var vEnd2   = (ch2 === parsed.endCh) ? parsed.endV : 999;
      for (var v2 = vStart2; v2 <= vEnd2; v2++) {
        var prose = chData2[String(v2)];
        if (!prose) continue;
        layer2Html += '<div class="sw-grammar-prose">'
          + '<div class="sw-grammar-prose__ref">' + ch2 + ':' + v2 + ' — Original Language Notes</div>'
          + prose
          + '</div>';
      }
    }
  }

  if (!layer1Html && !layer2Html) {
    container.innerHTML = '<p class="sw-tab-stub">No grammar data available for this passage.</p>';
    return;
  }

  container.innerHTML = (layer1Html || '') + (layer2Html
    ? '<div class="sw-grammar-prose-section">' + layer2Html + '</div>'
    : '<p class="sw-grammar-no-prose">Original language notes not yet available for this book.</p>');
}

/* ── Word Study Dictionary / Glossary ─────────────────────── */
// INTENT: Accent-forgiving full Strong's dictionary searchable by gloss (English),
//   lemma (original script), transliteration, or Strong's code. Loads both Greek and
//   Hebrew lazily on first open; filters are additive chips (all on = show everything).
// CHANGE? If loadStrongs() return shape changes (lemma/gloss/pos fields), update _dictNorm().
// VERIFY: Open Word Study → click Dictionary → type "love" → G25/G26/H157 appear.
//   Type "logos" → G3056 appears. Deselect "Hebrew" chip → only Greek entries show.

var _dictCache = { greek: null, hebrew: null };  // null = not loaded; {} = loaded
var _dictActiveFilters = new Set(['greek', 'hebrew', 'noun', 'verb', 'name', 'other']);
var _dictSearchTimer = null;

// Strip accents / diacritics from a string for accent-forgiving comparison
function _stripAccents(str) {
  return (str || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
}

// Map a POS string to a filter category
function _posToFilter(pos) {
  if (!pos) return 'other';
  var p = pos.toLowerCase();
  if (p.includes('noun') || p.includes('substantive')) return 'noun';
  if (p.includes('verb') || p.includes('participle'))   return 'verb';
  if (p.includes('name') || p.includes('proper'))       return 'name';
  return 'other';
}

// Load dictionaries lazily
async function _ensureDictLoaded(langs) {
  var tasks = [];
  if (langs.includes('greek') && !_dictCache.greek) {
    tasks.push(loadStrongs('greek').then(function(d) { _dictCache.greek = d || {}; }).catch(function() { _dictCache.greek = {}; }));
  }
  if (langs.includes('hebrew') && !_dictCache.hebrew) {
    tasks.push(loadStrongs('hebrew').then(function(d) { _dictCache.hebrew = d || {}; }).catch(function() { _dictCache.hebrew = {}; }));
  }
  if (tasks.length) await Promise.all(tasks);
}

// INTENT: Wire the dictionary toggle button and filter chips. Called once when Word Study
//   mode panel is first shown. Re-calls are safe (idempotent via _dictInited guard).
// CHANGE? If filter chip data-filter values change in HTML, update _dictActiveFilters init and _posToFilter().
// VERIFY: Click "Dictionary" button → dict panel slides in/out. Deselect "Verbs" → verb entries disappear.
var _dictInited = false;
function _initDictPanel() {
  if (_dictInited) return;
  _dictInited = true;

  var toggleBtn  = document.getElementById('sw-ws-dict-toggle');
  var dictCol    = document.getElementById('sw-ws-dict-col');
  var bodyArea   = document.getElementById('sw-ws-body-area');
  var wsInput    = document.getElementById('sw-ws-input');
  var filterBtns = document.querySelectorAll('.sw-ws-filter[data-filter]');

  // Filter chips — additive (all on by default; click toggles off/on)
  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var f = btn.dataset.filter;
      if (_dictActiveFilters.has(f)) {
        _dictActiveFilters.delete(f);
        btn.classList.remove('sw-ws-filter--active');
      } else {
        _dictActiveFilters.add(f);
        btn.classList.add('sw-ws-filter--active');
      }
      _runDictSearch();
    });
  });

  // INTENT: Dictionary toggle opens a 50/50 split: left=dict browser, right=word detail.
  //   Toggling off restores full-width word detail. Runs initial search on first open.
  // CHANGE? If sw-ws-dict-col or sw-ws-body-area IDs change, update selectors here.
  // VERIFY: Click Dictionary → left panel appears with filters + list; word detail stays on right.
  if (toggleBtn && dictCol && bodyArea) {
    toggleBtn.addEventListener('click', function() {
      var open = !dictCol.hidden;
      dictCol.hidden = open;
      bodyArea.classList.toggle('sw-ws-body-area--dict-open', !open);
      toggleBtn.classList.toggle('ws-btn--active', !open);
      if (!open) _runDictSearch();
    });
  }

  // Search input drives both the detail panel AND the dictionary list
  if (wsInput) {
    wsInput.addEventListener('input', function() {
      clearTimeout(_dictSearchTimer);
      _dictSearchTimer = setTimeout(_runDictSearch, 250);
    });
  }
}

// INTENT: Run an accent-forgiving search across both Strong's dictionaries.
//   Query matches against: gloss, lemma, transliteration, Strong's code.
//   Results are filtered by active chip set, then limited to 200 rows for performance.
// CHANGE? If _dictCache structure changes (greek/hebrew keys), update lang loop below.
// VERIFY: Search "agape" → G26 appears. Search "chesed" → H2617 appears.
//   Search "faith" → G4102, H530 both appear (if both lang filters active).
async function _runDictSearch() {
  var dictCol = document.getElementById('sw-ws-dict-col');
  if (!dictCol || dictCol.hidden) return;

  var q = ((document.getElementById('sw-ws-input') || {}).value || '').trim();
  var qStrip = _stripAccents(q);

  // Determine which language dicts to load based on active filters
  var langs = [];
  if (_dictActiveFilters.has('greek'))  langs.push('greek');
  if (_dictActiveFilters.has('hebrew')) langs.push('hebrew');
  if (!langs.length) { _renderDictResults([], q); return; }

  await _ensureDictLoaded(langs);

  var results = [];

  langs.forEach(function(lang) {
    var dict = _dictCache[lang] || {};
    Object.keys(dict).forEach(function(code) {
      var entry = dict[code];
      if (!entry) return;

      // POS filter check
      var posFilter = _posToFilter(entry.pos || entry.part_of_speech || '');
      if (!_dictActiveFilters.has(posFilter)) return;

      // If no query, include all (up to limit)
      if (!q) { results.push({ code: code, entry: entry, lang: lang, score: 0 }); return; }

      // Accent-forgiving matching
      var lemmaStrip   = _stripAccents(entry.lemma || '');
      var glossStrip   = _stripAccents(entry.gloss || entry.meaning || '');
      var translitStrip = _stripAccents(entry.translit || entry.transliteration || '');
      var codeStrip    = (code || '').toLowerCase();

      var score = 0;
      if (codeStrip === qStrip.toUpperCase() || codeStrip === qStrip)       score = 100; // exact code
      else if (codeStrip.startsWith(qStrip))                                 score = 90;
      else if (lemmaStrip.startsWith(qStrip))                                score = 85;
      else if (translitStrip.startsWith(qStrip))                             score = 80;
      else if (glossStrip.split(/\s+/).some(function(w) { return w.startsWith(qStrip); })) score = 75;
      else if (lemmaStrip.includes(qStrip))                                  score = 60;
      else if (translitStrip.includes(qStrip))                               score = 55;
      else if (glossStrip.includes(qStrip))                                  score = 50;
      else return; // no match

      results.push({ code: code, entry: entry, lang: lang, score: score });
    });
  });

  // Sort: exact/prefix matches first, then by score desc, then alphabetically by gloss
  results.sort(function(a, b) {
    if (b.score !== a.score) return b.score - a.score;
    return (a.entry.gloss || '').localeCompare(b.entry.gloss || '');
  });

  _renderDictResults(results.slice(0, 200), q);
}

function _renderDictResults(results, q) {
  var statusEl = document.getElementById('sw-dict-status');
  var listEl   = document.getElementById('sw-dict-list');
  if (!statusEl || !listEl) return;

  statusEl.textContent = results.length === 0 ? (q ? 'No matches' : 'Loading…')
    : results.length + ' entr' + (results.length === 1 ? 'y' : 'ies') + (results.length === 200 ? ' (showing first 200)' : '');

  if (!results.length) { listEl.innerHTML = ''; return; }

  var qStrip = _stripAccents(q);
  function _hi(str) {
    if (!q) return _esc(str || '');
    var s = _esc(str || '');
    var sLow = _stripAccents(str || '');
    var idx = sLow.indexOf(qStrip);
    if (idx < 0) return s;
    return _esc((str || '').slice(0, idx)) + '<em class="sw-dict-hi">' + _esc((str || '').slice(idx, idx + q.length)) + '</em>' + _esc((str || '').slice(idx + q.length));
  }

  var html = '';
  results.forEach(function(r) {
    var posClass = r.lang === 'greek' ? 'sw-dict-meta--greek' : 'sw-dict-meta--hebrew';
    var pos = (r.entry.pos || r.entry.part_of_speech || '').replace(/\b(\w)/g, function(m) { return m.toUpperCase(); });
    html += '<div class="sw-dict-entry" data-code="' + _esc(r.code) + '" role="button" tabindex="0">'
      + '<span class="sw-dict-word">' + _esc(r.entry.lemma || r.code) + '</span>'
      + '<span class="sw-dict-gloss">' + _hi(r.entry.gloss || r.entry.meaning || '') + '</span>'
      + '<span class="sw-dict-meta ' + posClass + '">' + _esc(r.code) + '</span>'
      + '</div>';
  });
  listEl.innerHTML = html;

  // Wire entry clicks → open word study for that code
  listEl.querySelectorAll('.sw-dict-entry[data-code]').forEach(function(row) {
    row.addEventListener('click', function() {
      listEl.querySelectorAll('.sw-dict-entry').forEach(function(r) { r.classList.remove('sw-dict-entry--active'); });
      row.classList.add('sw-dict-entry--active');
      _renderWordStudyPanel(row.dataset.code);
    });
    row.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); row.click(); }
    });
  });
}

/* ── Study Mode Switching ──────────────────────────────────── */
// INTENT: Switch between the three primary study modes (verse/word/book). Each mode
//   shows a different center column panel and adjusts the page CSS class so the dossier
//   column is hidden in word and book modes (giving the center panel full width).
// CHANGE? If new mode panel IDs are added to index.html, add them to the panel map here.
// VERIFY: Click "Word Study" tab → dossier column disappears; Word Study panel fills center.
function _setStudyMode(mode) {
  _studyMode = mode;

  // Update mode button states
  document.querySelectorAll('.sw-mode-btn').forEach(function(btn) {
    btn.classList.toggle('sw-mode-btn--active', btn.dataset.mode === mode);
  });

  // Toggle page-level CSS classes so grid layout adjusts
  var page = document.querySelector('.ws-page');
  if (page) {
    page.classList.toggle('ws-page--word-study', mode === 'word');
    page.classList.toggle('ws-page--book-study', mode === 'book');
  }

  // Show/hide panels
  var verseMode = document.getElementById('sw-verse-mode');
  var wordMode  = document.getElementById('sw-word-mode');
  var bookMode  = document.getElementById('sw-book-mode');
  if (verseMode) verseMode.hidden = (mode !== 'verse');
  if (wordMode)  wordMode.hidden  = (mode !== 'word');
  if (bookMode)  bookMode.hidden  = (mode !== 'book');

  if (mode === 'book') {
    _initBookStudyPanel();
  } else if (mode === 'word') {
    _initDictPanel();  // idempotent — safe to call on every entry to word mode
    if (_uiState.activeCode) {
      _renderWordStudyPanel(_uiState.activeCode);
    }
  }
}

/* ── Word Study Panel ──────────────────────────────────────── */
// INTENT: Full-page word study in the center column. Uses curated vocabulary entry if available
//   (rich dossier sections: grammar, debates, idioms, frequency, semantic neighborhood, cognates,
//   second-temple context, lexical sources) with concordance in a second column. Falls back to
//   Strongs-only data for words outside the curated set.
// CHANGE? If Strong's data format changes (loadStrongs return shape), update destructuring below.
//   If dossier rendering functions are renamed, update all calls inside this function.
// VERIFY: Click "Word Study", type G3056 → λόγος lemma card shows; scroll to see grammar,
//   idiom alerts, semantic neighborhood; right column shows usage from current book if loaded.
async function _renderWordStudyPanel(code) {
  var bodyEl = document.getElementById('sw-ws-body');
  if (!bodyEl) return;
  bodyEl.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading…</p>';

  var lang = code.startsWith('G') ? 'greek' : 'hebrew';

  // Load both curated entry and Strongs fallback in parallel
  var [strongsDict] = await Promise.all([
    loadStrongs(lang).catch(function() { return {}; })
  ]);

  var curatedEntry = _getEntry(code);  // may be null if word not in curated vocab set
  var sEntry = strongsDict[code];

  if (!curatedEntry && !sEntry) {
    bodyEl.innerHTML = '<p class="sw-ws-placeholder">No entry found for <strong>' + _esc(code) + '</strong>.</p>';
    return;
  }

  // Prefer curated data; fall back to Strongs fields
  var src    = curatedEntry || {};
  var lemma  = src.lemma    || sEntry?.lemma   || sEntry?.word   || code;
  var gloss  = src.gloss    || sEntry?.gloss   || sEntry?.meaning || '';
  var translit = src.translit || sEntry?.translit || sEntry?.transliteration || '';
  var pos    = src.pos      || sEntry?.pos     || sEntry?.part_of_speech || '';
  var freq   = src.nt_freq  ?? src.ot_freq     ?? sEntry?.frequency ?? 0;
  var freqLabel = lang === 'greek' ? 'NT' : 'OT';

  // ── Left column: lemma card + rich lexical sections ──────────────────
  var leftHtml = '<div class="sw-ws-lemma-card">'
    + '<div class="sw-ws-lemma-word">' + _esc(lemma) + '</div>'
    + (translit ? '<div class="sw-ws-lemma-translit">' + _esc(translit) + '</div>' : '')
    + '<div class="sw-ws-lemma-gloss">"' + _esc(gloss) + '"</div>'
    + (pos ? '<div class="sw-ws-lemma-pos">' + _esc(pos) + ' · ' + _esc(code) + '</div>' : '<div class="sw-ws-lemma-pos">' + _esc(code) + '</div>')
    + '</div>';

  // Add-to-deck button
  leftHtml += '<div style="margin-top:0.75rem;margin-bottom:0.5rem">'
    + '<button type="button" class="sw-add-deck-btn ws-btn ws-btn--sm" data-code="' + _esc(code) + '">'
    + (_isInDeck(code) ? '★ In Your Deck' : '☆ Add to Deck')
    + '</button></div>';

  if (curatedEntry) {
    // ── Rich sections from curated dossier data ─────────────────────────
    // Semantic range (attested range headline)
    if (src.semantic_range) {
      leftHtml += '<div class="sw-ws-section-head">Attested Range</div>'
        + '<div class="sw-ws-prose">' + _esc(src.semantic_range) + '</div>';
    }
    if (src.attested_uses && src.attested_uses.length) {
      leftHtml += _renderAttestedUses(src.attested_uses);
    }

    // Grammar significance (morphology hints, particle function card)
    leftHtml += _renderGrammarSection(code, lang);

    // Contested interpretations
    leftHtml += _renderDebateSection(code);

    // Idiom alerts
    leftHtml += _renderIdiomAlertSection(code);

    // Author frequency
    leftHtml += _renderAuthorFreqSection(code, lang);

    // Semantic neighborhood (PMI co-occurrence)
    leftHtml += _renderSemanticSection(code, lang);

    // Word family / cognates
    leftHtml += _renderCognateSection(code);

    // Second Temple context
    leftHtml += _renderSTContext(code);

    // Extrabiblical uses (M&M papyri — Greek only)
    if (lang === 'greek' && src.extrabiblical_uses && src.extrabiblical_uses.length) {
      leftHtml += _renderExtrabib(src.extrabiblical_uses);
    }

    // Frequency
    if (freq) {
      leftHtml += '<div class="sw-ws-section-head">Frequency</div>'
        + '<div class="sw-ws-prose">Appears <strong>' + freq + '</strong> time'
        + (freq === 1 ? '' : 's') + ' in the ' + freqLabel + '</div>';
    }

    // Lexical sources (Dodson/Thayer/BDB etc.)
    leftHtml += _renderLexicalSourcesSection(src);

    // LXX Bridge (Hebrew only — how Septuagint translators rendered this word)
    if (lang === 'hebrew' && src.lxx_bridge && src.lxx_bridge.length) {
      leftHtml += _renderLxxBridge(src.lxx_bridge);
    }

  } else {
    // ── Strongs-only fallback (word not in curated vocab set) ─────────────
    var definition = sEntry.def || sEntry.definition || sEntry.long_definition || '';
    if (definition) {
      leftHtml += '<div class="sw-ws-section-head">Definition</div>'
        + '<div class="sw-ws-prose">' + _esc(definition) + '</div>';
    }
    if (sEntry.semantic_range) {
      leftHtml += '<div class="sw-ws-section-head">Semantic Range</div>'
        + '<div class="sw-ws-prose">' + _esc(sEntry.semantic_range) + '</div>';
    }
    if (freq) {
      leftHtml += '<div class="sw-ws-section-head">Frequency</div>'
        + '<div class="sw-ws-prose">Appears <strong>' + freq + '</strong> time'
        + (freq === 1 ? '' : 's') + ' in the ' + freqLabel + '</div>';
    }
    // Cognate family from cached data even for Strongs-only entries
    var cognateFamily = _getCognateFamily(code, lang);
    if (cognateFamily && cognateFamily.members && cognateFamily.members.length > 1) {
      leftHtml += '<div class="sw-ws-section-head">Word Family</div><div>';
      cognateFamily.members.slice(0, 8).forEach(function(m) {
        if (m.code === code) return;
        leftHtml += '<span class="sw-xref-chip" style="margin-bottom:0.3rem" data-code="' + _esc(m.code) + '">'
          + _esc(m.lemma || m.code) + ' <em style="font-style:normal;opacity:0.7">' + _esc(m.gloss || '') + '</em></span> ';
      });
      leftHtml += '</div>';
    }
    leftHtml += '<p class="ws-placeholder" style="font-size:.8rem;margin-top:1rem">'
      + 'Full dossier unavailable — word is outside the curated vocabulary set.</p>';
  }

  // ── Right column: concordance from loaded interlinear book ────────────
  var rightHtml = '<div class="sw-ws-section-head">Usage in Scripture</div>';
  if (_interData && _passageRef) {
    var matches = [];
    Object.keys(_interData).forEach(function(ch) {
      var chData = _interData[ch];
      if (!chData || !chData.verses) return;
      Object.keys(chData.verses).forEach(function(v) {
        var verseWords = chData.verses[v];
        if (!Array.isArray(verseWords)) return;
        var hasCode = verseWords.some(function(w) {
          return w.strongs === code || (Array.isArray(w.strongs) && w.strongs.includes(code));
        });
        if (hasCode) {
          var ref = _passageRef.bookId + ' ' + ch + ':' + v;
          matches.push({ ch: parseInt(ch), v: parseInt(v), ref: ref, allWords: verseWords });
        }
      });
    });

    if (matches.length) {
      rightHtml += '<div style="font-size:0.78rem;color:var(--color-text-muted,#7a6a4a);margin-bottom:0.5rem">'
        + matches.length + ' occurrence' + (matches.length === 1 ? '' : 's') + ' in current book</div>';
      matches.slice(0, 20).forEach(function(m) {
        var verseGloss = m.allWords.map(function(w) {
          var g = w.gloss || '';
          return (w.strongs === code || (Array.isArray(w.strongs) && w.strongs.includes(code)))
            ? '<em>' + _esc(g) + '</em>' : _esc(g);
        }).join(' ');
        rightHtml += '<div class="sw-ws-usage-verse" data-ref="' + _esc(m.ref) + '">'
          + '<span class="sw-ws-usage-ref">' + _esc(m.ref.replace(/^\S+ /, '')) + '</span>'
          + '<span class="sw-ws-usage-text">' + verseGloss + '</span>'
          + '</div>';
      });
      if (matches.length > 20) {
        rightHtml += '<p style="font-size:0.78rem;color:var(--color-text-muted,#7a6a4a);margin-top:0.5rem">… and ' + (matches.length - 20) + ' more</p>';
      }
    } else {
      rightHtml += '<p style="font-size:0.87rem;color:var(--color-text-muted,#7a6a4a)">Not found in the currently loaded book.</p>';
    }
  } else {
    // INTENT: No passage loaded — show where the word appears across the Bible so
    //   the user has immediate value before loading a specific passage.
    // CHANGE? If _renderBookDistribution signature changes, update call below.
    var distEntry = _getEntry(code);
    if (distEntry && Object.keys(distEntry._bookFreq || {}).length) {
      rightHtml += '<div style="font-size:0.82rem;color:var(--color-text-muted,#7a6a4a);margin-bottom:0.5rem">'
        + 'Bible distribution (study a passage to see verse occurrences)</div>';
      rightHtml += _renderBookDistribution(distEntry._bookFreq, distEntry._lang);
    } else {
      rightHtml += '<p style="font-size:0.87rem;color:var(--color-text-muted,#7a6a4a)">'
        + 'Study a passage first — occurrences from that book will appear here.</p>';
    }
  }

  bodyEl.innerHTML = '<div class="sw-ws-detail"><div class="sw-ws-detail-left">' + leftHtml + '</div>'
    + '<div class="sw-ws-detail-right">' + rightHtml + '</div></div>';

  // Wire deck toggle
  var deckBtn = bodyEl.querySelector('.sw-add-deck-btn[data-code]');
  if (deckBtn) deckBtn.addEventListener('click', function() {
    _fcToggleDeck(deckBtn.dataset.code);
    deckBtn.textContent = _isInDeck(deckBtn.dataset.code) ? '★ In Your Deck' : '☆ Add to Deck';
  });

  // Wire cognate/family/semantic chips to navigate within word study
  bodyEl.querySelectorAll('[data-code]').forEach(function(chip) {
    chip.addEventListener('click', function(e) {
      var c = chip.dataset.code;
      if (c && c !== code) { e.stopPropagation(); _renderWordStudyPanel(c); }
    });
  });

  // Wire verse usage rows to switch to verse study
  bodyEl.querySelectorAll('.sw-ws-usage-verse[data-ref]').forEach(function(row) {
    row.addEventListener('click', function() {
      _setStudyMode('verse');
      _studyPassage(row.dataset.ref);
    });
  });
}

// INTENT: Render the Lexical Sources section (Dodson, Thayer, BDB, etc.) for the word study panel.
//   Pulls from src.source_data directly without <details> wrapping since the panel is full-width.
// CHANGE? If source_data field names change in seed-glossary.py, update the keys below.
// VERIFY: Word Study → type G26 (ἀγάπη) → Lexical Sources section shows Dodson and Thayer cards.
function _renderLexicalSourcesSection(src) {
  if (!src.source_data) return '';
  var sd = src.source_data;
  var isGreek = (src._lang === 'greek');
  var manifest = isGreek ? [
    { label: 'Dodson (CC0)',        gloss: sd.dodson?.gloss,   def: sd.dodson?.def,   extra: sd.dodson?.deriv },
    { label: 'Thayer (1889)',       gloss: sd.thayer?.short,   def: sd.thayer?.long,  extra: '' },
    { label: 'Abbott-Smith (1922)', gloss: sd.abbott?.gloss,   def: sd.abbott?.def,   extra: sd.abbott?.classical_note || '' },
  ] : [
    { label: "Strong's Hebrew",     gloss: sd.hebrew?.gloss,   def: sd.hebrew?.def,   extra: sd.hebrew?.deriv },
    { label: 'BDB (1906)',          gloss: sd.bdb?.short,      def: sd.bdb?.long,     extra: '' },
    { label: 'Gesenius (1857)',     gloss: sd.gesenius?.gloss, def: sd.gesenius?.def, extra: sd.gesenius?.cognates || '' },
  ];
  var active = manifest.filter(function(m) { return m.gloss || m.def; });
  if (!active.length) return '';
  var out = '<div class="sw-ws-section-head">Lexical Sources</div>';
  active.forEach(function(m) { out += _sourceCard(m.label, m.gloss, m.def, m.extra); });
  return out;
}

// _getCognateFamily: pull the current word's cognate family from the cached data.
function _getCognateFamily(code, lang) {
  var prefix = lang === 'greek' ? 'G' : 'H';
  var idx = _cognatesIndex[prefix];
  var families = _cognatesFamilies[prefix];
  if (!idx || !families) return null;
  var root = idx[code];
  if (!root) return null;
  return families.find(function(f) { return f.root === root; }) || null;
}

/* ── Book Study Panel ──────────────────────────────────────── */
// INTENT: Initialize the book selector dropdown once on first entry into book study mode.
//   Populates from data/bible/books.json so the user can pick any canonical book.
// CHANGE? If loadBooks() data shape changes (bookId, name), update the option-building here.
// VERIFY: Switch to Book Study mode → dropdown lists all 66 books alphabetically by order.
var _bookStudyInited = false;
async function _initBookStudyPanel() {
  if (_bookStudyInited) return;
  _bookStudyInited = true;
  await loadBooks();
  var sel = document.getElementById('sw-book-select');
  if (!sel) return;

  // loadBooks() populates the module-level metaBooks via bookOrder; re-fetch via loadBooks return
  var books = await loadBooks();
  books.forEach(function(b) {
    var opt = document.createElement('option');
    opt.value = b.id;
    opt.textContent = b.name;
    sel.appendChild(opt);
  });

  sel.addEventListener('change', function() {
    if (sel.value) _renderBookStudy(sel.value);
  });

  // Pre-select the current passage's book if one is loaded
  if (_passageRef) {
    sel.value = _passageRef.bookId;
    _renderBookStudy(_passageRef.bookId);
  }
}

// INTENT: Render book-level study content: introduction, themes, key vocabulary, and idioms
//   found in that book. Data sources: cultural/book-context.json, author-freq data, idioms.json.
// CHANGE? If cultural/book-context.json schema changes (intro/themes fields renamed), update accessors.
// VERIFY: Switch to Book Study, select Romans → intro paragraph, theme chips, key term list renders.
// INTENT: Load supplemental book study data from data/workshop/book-study/{bookId}.json.
//   This is the SW-V schema: key_vocabulary, language_notes, reception, reading_guide.
//   Falls back to empty object if file doesn't exist yet (most books not yet generated).
// CHANGE? If the book study data path or schema changes, update the fetch URL and field accessors below.
// VERIFY: Select Romans in Book Study → Vocabulary/Language/Reception/Reading tabs all render.
var _bookStudyCache = {};
async function _loadBookStudyData(bookId) {
  if (_bookStudyCache[bookId] !== undefined) return _bookStudyCache[bookId];
  try {
    var url = _resolve('../../data/workshop/book-study/' + bookId + '.json');
    var res = await fetch(url);
    _bookStudyCache[bookId] = res.ok ? await res.json() : {};
  } catch(e) { _bookStudyCache[bookId] = {}; }
  return _bookStudyCache[bookId];
}

async function _renderBookStudy(bookId) {
  var bodyEl = document.getElementById('sw-book-body');
  if (!bodyEl) return;
  bodyEl.innerHTML = '<p class="sw-tab-stub sw-tab-stub--loading">Loading…</p>';

  var lang = _bookLang(bookId);

  // Pre-warm caches — all populate module-level variables; return values vary.
  // Phase data is loaded so _getEntry() resolves lemma/gloss in the Key Terms tab.
  var [,,,, bsData] = await Promise.all([
    _loadCultural().catch(function() {}),
    (lang === 'greek' ? _loadAuthorFreq('greek') : _loadAuthorFreq('hebrew')).catch(function() {}),
    _loadIdioms().catch(function() {}),
    _loadPhase(lang === 'greek' ? 'phase1' : 'phase2').catch(function() {}),
    _loadBookStudyData(bookId),
  ]);

  // Access module-level caches directly after loading
  var bookCtx = _culturalCache && _culturalCache.bookContext && _culturalCache.bookContext[bookId];

  var html = '';

  // Introduction
  if (bookCtx && bookCtx.intro) {
    html += '<div class="sw-book-intro-card">' + _esc(bookCtx.intro) + '</div>';
  }

  // Determine which tabs to show based on available supplemental data
  var hasVocab    = bsData && Array.isArray(bsData.key_vocabulary) && bsData.key_vocabulary.length;
  var hasLangNote = bsData && bsData.language_notes;
  var hasReception = bsData && bsData.reception;
  var hasReadingGuide = bsData && bsData.reading_guide;

  // Build tab bar — supplemental tabs shown when data exists
  html += '<div class="sw-book-tabs">'
    + '<button type="button" class="sw-book-tab sw-book-tab--active" data-btab="overview">Overview</button>'
    + '<button type="button" class="sw-book-tab" data-btab="themes">Themes</button>'
    + '<button type="button" class="sw-book-tab" data-btab="terms">Key Terms</button>'
    + '<button type="button" class="sw-book-tab" data-btab="idioms">Idioms</button>'
    + (hasVocab      ? '<button type="button" class="sw-book-tab" data-btab="vocabulary">Vocabulary</button>' : '')
    + (hasLangNote   ? '<button type="button" class="sw-book-tab" data-btab="language">Language</button>' : '')
    + (hasReception  ? '<button type="button" class="sw-book-tab" data-btab="reception">Reception</button>' : '')
    + (hasReadingGuide ? '<button type="button" class="sw-book-tab" data-btab="reading">Reading Guide</button>' : '')
    + '</div>'
    + '<div id="sw-book-tab-content" class="sw-book-tab-content"></div>';

  bodyEl.innerHTML = html;

  var freqData  = _authorFreqCache[lang] || null;
  var idiomsArr = _idiomsData ? Object.values(_idiomsData) : [];

  // Wire tab switching
  var tabContent = bodyEl.querySelector('#sw-book-tab-content');
  bodyEl.querySelectorAll('.sw-book-tab').forEach(function(btn) {
    btn.addEventListener('click', function() {
      bodyEl.querySelectorAll('.sw-book-tab').forEach(function(b) { b.classList.remove('sw-book-tab--active'); });
      btn.classList.add('sw-book-tab--active');
      var tab = btn.dataset.btab;
      if (tab === 'vocabulary') {
        _renderBookVocabTab(bsData.key_vocabulary, tabContent);
      } else if (tab === 'language') {
        tabContent.innerHTML = '<div class="sw-book-html-content">' + (bsData.language_notes || '') + '</div>';
      } else if (tab === 'reception') {
        tabContent.innerHTML = '<div class="sw-book-html-content">' + (bsData.reception || '') + '</div>';
      } else if (tab === 'reading') {
        tabContent.innerHTML = '<div class="sw-book-html-content">' + (bsData.reading_guide || '') + '</div>';
      } else {
        _renderBookTab(tab, bookId, bookCtx, freqData, idiomsArr, tabContent, lang);
      }
    });
  });

  _renderBookTab('overview', bookId, bookCtx, freqData, idiomsArr, tabContent, lang);
}

// INTENT: Render the key_vocabulary array as clickable rows that open Word Study for each code.
//   Shows lemma, translit, gloss chip, and significance note for each entry.
// CHANGE? If key_vocabulary schema fields change (code/lemma/translit/gloss/significance), update row HTML.
// VERIFY: Romans Book Study → Vocabulary tab → 15 rows with lemma, gloss, and expandable significance.
function _renderBookVocabTab(vocab, container) {
  if (!vocab || !vocab.length) {
    container.innerHTML = '<p class="sw-ws-placeholder">No vocabulary data for this book yet.</p>';
    return;
  }
  var html = '<div style="font-size:0.78rem;color:var(--color-text-muted,#7a6a4a);margin-bottom:0.75rem">'
    + 'Characteristic vocabulary of this book. Click any row to open full Word Study.</div>';
  vocab.forEach(function(entry) {
    html += '<details class="sw-bookvoc-row" data-code="' + _esc(entry.code || '') + '">'
      + '<summary class="sw-bookvoc-summary">'
      + '<span class="sw-bookvoc-lemma">' + _esc(entry.lemma || entry.code || '') + '</span>'
      + (entry.translit ? '<span class="sw-bookvoc-translit">' + _esc(entry.translit) + '</span>' : '')
      + '<span class="sw-bookvoc-gloss">' + _esc(entry.gloss || '') + '</span>'
      + '<span class="sw-bookvoc-code">' + _esc(entry.code || '') + '</span>'
      + '</summary>'
      + '<div class="sw-bookvoc-sig">' + _esc(entry.significance || '') + '</div>'
      + '</details>';
  });
  container.innerHTML = html;
  container.querySelectorAll('.sw-bookvoc-row[data-code]').forEach(function(row) {
    row.querySelector('.sw-bookvoc-summary').addEventListener('click', function(e) {
      // Single click opens details; double-click or Ctrl+click opens Word Study
    });
    row.addEventListener('dblclick', function() {
      var code = row.dataset.code;
      if (code) { _setStudyMode('word'); _renderWordStudyPanel(code); }
    });
  });
}

function _bookLang(bookId) {
  // OT books are Hebrew; NT books are Greek
  var ntStart = ['matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1corinthians',
    '2corinthians', 'galatians', 'ephesians', 'philippians', 'colossians',
    '1thessalonians', '2thessalonians', '1timothy', '2timothy', 'titus', 'philemon',
    'hebrews', 'james', '1peter', '2peter', '1john', '2john', '3john', 'jude', 'revelation'];
  return ntStart.includes((bookId || '').toLowerCase()) ? 'greek' : 'hebrew';
}

function _renderBookTab(tab, bookId, bookCtx, freqData, idiomsArr, container, lang) {
  var html = '';

  if (tab === 'overview') {
    if (bookCtx) {
      if (bookCtx.historical_context) {
        html += '<p>' + _esc(bookCtx.historical_context) + '</p>';
      }
      if (bookCtx.key_cultural_notes && bookCtx.key_cultural_notes.length) {
        html += '<div class="sw-ws-section-head">Cultural Notes</div>';
        bookCtx.key_cultural_notes.forEach(function(note) {
          html += '<p>' + _esc(typeof note === 'string' ? note : String(note)) + '</p>';
        });
      }
    } else {
      html = '<p class="sw-ws-placeholder">No overview available for this book yet.</p>';
    }

  } else if (tab === 'themes') {
    var frameworks = (bookCtx && bookCtx.cultural_frameworks) || [];
    // INTENT: Look up each framework ID in the already-loaded _culturalCache.frameworks array
    //   so the Themes tab shows prose (summary + what_it_means_for_reading) rather than bare chip labels.
    // CHANGE? If frameworks.json schema changes (summary/what_it_means_for_reading renamed), update accessors here.
    var fwIndex = {};
    if (_culturalCache && Array.isArray(_culturalCache.frameworks)) {
      _culturalCache.frameworks.forEach(function(fw) { fwIndex[fw.id] = fw; });
    }
    if (frameworks.length) {
      frameworks.forEach(function(t) {
        var id  = typeof t === 'string' ? t : (t.name || String(t));
        var fw  = fwIndex[id];
        html += '<div class="sw-book-theme-block">'
          + '<span class="sw-book-theme-chip">' + _esc(fw ? fw.title : id) + '</span>';
        if (fw && fw.summary) {
          html += '<p class="sw-book-theme-summary">' + _esc(fw.summary) + '</p>';
        }
        if (fw && fw.what_it_means_for_reading) {
          html += '<p class="sw-book-theme-reading">' + _esc(fw.what_it_means_for_reading) + '</p>';
        }
        html += '</div>';
      });
    } else {
      html = '<p class="sw-ws-placeholder">No themes data for this book yet.</p>';
    }

  } else if (tab === 'terms') {
    // Map bookId to the author group name used in author-freq data
    var BOOK_TO_AUTHOR = {
      matthew: 'Matthew', mark: 'Mark', luke: 'Luke', acts: 'Luke',
      john: 'John', '1john': 'John', '2john': 'John', '3john': 'John', revelation: 'John',
      romans: 'Paul', '1corinthians': 'Paul', '2corinthians': 'Paul',
      galatians: 'Paul', ephesians: 'Paul', philippians: 'Paul',
      colossians: 'Paul', '1thessalonians': 'Paul', '2thessalonians': 'Paul',
      '1timothy': 'Paul', '2timothy': 'Paul', titus: 'Paul', philemon: 'Paul',
      hebrews: 'Hebrews', james: 'James',
      '1peter': 'Peter', '2peter': 'Peter',
      jude: 'Jude',
    };
    var authorGroup = BOOK_TO_AUTHOR[bookId] || null;

    if (freqData && authorGroup) {
      var entries = [];
      Object.keys(freqData).forEach(function(code) {
        var d = freqData[code];
        if (!d || !d.peak || !d.rates) return;
        if (d.peak === authorGroup) {
          var peakRate = d.rates[authorGroup] || 0;
          entries.push({ code: code, peakRate: peakRate });
        }
      });

      entries.sort(function(a, b) { return b.peakRate - a.peakRate; });
      var topEntries = entries.slice(0, 30);

      if (topEntries.length) {
        html += '<div style="font-size:0.78rem;color:var(--color-text-muted,#7a6a4a);margin-bottom:0.75rem">'
          + 'Characteristic vocabulary of ' + authorGroup + ' (peak usage vs. other NT authors). Click any term to open Word Study.</div>';
        topEntries.forEach(function(e) {
          var entry = _getEntry(e.code);
          var wordLabel = entry ? _esc(entry.lemma || e.code) : _esc(e.code);
          var glossLabel = entry ? _esc((entry._tiers && entry._tiers.literal && entry._tiers.literal.primary) || '') : '';
          html += '<div class="sw-book-term-row" data-code="' + _esc(e.code) + '">'
            + '<span class="sw-book-term-word">' + wordLabel + '</span>'
            + '<span class="sw-book-term-gloss">' + glossLabel + '</span>'
            + '<span class="sw-book-term-count">' + Math.round(e.peakRate * 10) / 10 + '/1k</span>'
            + '</div>';
        });
        html += '<p style="font-size:0.75rem;color:var(--color-text-muted,#7a6a4a);margin-top:0.75rem">'
          + 'Click any row to open full word study with gloss and concordance.</p>';
      } else {
        html = '<p class="sw-ws-placeholder">No distinctive term data for this author group.</p>';
      }
    } else if (!authorGroup) {
      html = '<p class="sw-ws-placeholder">Author group mapping not available for this book.<br><small>OT author frequency data is work in progress.</small></p>';
    } else {
      html = '<p class="sw-ws-placeholder">Vocabulary frequency data not available.</p>';
    }

  } else if (tab === 'idioms') {
    // Show idioms associated with this book
    var bookIdioms = [];
    // INTENT: Show idioms relevant to this book's language. The idioms schema uses
    //   strongs_trigger_gr / strongs_trigger_he arrays, not a `books` field.
    //   Greek books show idioms that have Greek trigger codes; Hebrew books show Hebrew ones.
    if (Array.isArray(idiomsArr)) {
      var triggerKey = lang === 'greek' ? 'strongs_trigger_gr' : 'strongs_trigger_he';
      bookIdioms = idiomsArr.filter(function(idiom) {
        return Array.isArray(idiom[triggerKey]) && idiom[triggerKey].length > 0;
      });
    }

    if (bookIdioms.length) {
      html += '<div style="font-size:0.78rem;color:var(--color-text-muted,#7a6a4a);margin-bottom:0.75rem">'
        + bookIdioms.length + ' idiom' + (bookIdioms.length === 1 ? '' : 's') + ' found in this book</div>';
      bookIdioms.forEach(function(idiom) {
        html += '<div class="sw-book-idiom-row">'
          + '<div class="sw-book-idiom-phrase">' + _esc(idiom.phrase || idiom.id || '') + '</div>'
          + '<div class="sw-book-idiom-mean">' + _esc(idiom.meaning || idiom.note || '') + '</div>'
          + '</div>';
      });
    } else {
      html = '<p class="sw-ws-placeholder">No idioms catalogued for this book yet.</p>';
    }
  }

  container.innerHTML = html;

  // Wire key term rows → open Word Study panel for that code
  container.querySelectorAll('.sw-book-term-row[data-code]').forEach(function(row) {
    row.addEventListener('click', function() {
      _setStudyMode('word');
      _renderWordStudyPanel(row.dataset.code);
    });
  });
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

  // ── Mode bar ── wire Verse/Word/Book Study tabs
  // INTENT: Mode tabs switch the center column between passage tiles, word study panel,
  //   and book study panel. CSS class on .ws-page controls the grid column count.
  // CHANGE? If new modes are added, add data-mode values here and in _setStudyMode().
  // VERIFY: Click "Word Study" → dossier column disappears; word search input is focused.
  document.querySelectorAll('.sw-mode-btn[data-mode]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      _setStudyMode(btn.dataset.mode);
      if (btn.dataset.mode === 'word') {
        _initDictPanel();
        var inp = document.getElementById('sw-ws-input');
        if (inp) inp.focus();
      }
    });
  });

  // Wire word study search input
  var $wsInput = document.getElementById('sw-ws-input');
  if ($wsInput) {
    var _wsTimer;
    $wsInput.addEventListener('input', function() {
      clearTimeout(_wsTimer);
      _wsTimer = setTimeout(function() {
        var val = ($wsInput.value || '').trim();
        if (/^[GH]\d+$/i.test(val)) {
          // Exact Strong's code — render detail directly
          _renderWordStudyPanel(val.toUpperCase());
        } else if (val.length >= 2) {
          // Text search — run dict search if dictionary is open, otherwise just show detail hint
          _runDictSearch();
        }
      }, 300);
    });
    $wsInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        var val = ($wsInput.value || '').trim();
        if (val) _renderWordStudyPanel(val.startsWith('G') || val.startsWith('H') ? val.toUpperCase() : val);
      }
    });
  }

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

  // INTENT: Initialize depth from localStorage and wire all SW-A controls (passage study,
  //   translation mode toggle, depth selector) so they are live before any phase data loads.
  // CHANGE? If SK_DEPTH key changes, update _initDepth and _applyDepth. If new topbar buttons
  //   are added, wire them here in the same block.
  // VERIFY: Reload workshop — depth buttons show correct active state. Typing a ref and clicking
  //   "Study Passage" switches the queue column to passage view; "browse vocabulary →" returns to it.
  _initDepth();

  // Passage entry — study button and Enter key
  const $studyBtn  = document.getElementById('sw-study-btn');
  const $refInput  = document.getElementById('sw-ref-input');
  const $transBtn  = document.getElementById('sw-trans-toggle-btn');

  // ── Version selector — populate from versions.json, re-study on change
  // INTENT: Lets users switch translation (BSB/KJV/ESV etc.) without leaving the workshop.
  //   On change, setVersion() persists the choice and _studyPassage() re-renders the tiles
  //   with the new translation text shown alongside interlinear.
  // CHANGE? If passage entry bar HTML structure changes, update getElementById('sw-version-sel').
  // VERIFY: Study John 1:1 in BSB → switch to KJV → passage re-renders with KJV translation text.
  var $versionSel = document.getElementById('sw-version-sel');
  if ($versionSel) {
    loadVersions().then(function(versions) {
      var current = getVersion();
      versions.forEach(function(v) {
        var opt = document.createElement('option');
        opt.value = v.id;
        opt.textContent = v.id + (v.name ? ' — ' + v.name.replace(/^The /, '') : '');
        if (v.id === current) opt.selected = true;
        $versionSel.appendChild(opt);
      });
    }).catch(function() {
      var opt = document.createElement('option'); opt.value = 'BSB'; opt.textContent = 'BSB'; $versionSel.appendChild(opt);
    });
    $versionSel.addEventListener('change', function() {
      setVersion($versionSel.value);
      if (_passageRef) _studyPassage(_passageRef.raw || _passageRef.display);
    });
  }

  function _doStudy() {
    const ref = ($refInput.value || '').trim();
    if (ref) _studyPassage(ref);
  }
  $studyBtn.addEventListener('click', _doStudy);
  $refInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') _doStudy();
  });

  // INTENT: Advanced panel toggle — shows/hides translation workflow tools (mode toggle,
  //   import/export). Hidden by default so the primary experience is pure study.
  // CHANGE? If the panel ID changes, update getElementById here.
  // VERIFY: Click ⚙ → advanced panel slides open showing translation tools; click again → hides.
  var $advancedToggle = document.getElementById('sw-advanced-toggle');
  var $advancedPanel  = document.getElementById('sw-advanced-panel');
  if ($advancedToggle && $advancedPanel) {
    $advancedToggle.addEventListener('click', function() {
      var isOpen = !$advancedPanel.hidden;
      $advancedPanel.hidden = isOpen;
      $advancedToggle.setAttribute('aria-expanded', String(!isOpen));
    });
  }

  // Translation mode toggle (in advanced panel)
  if ($transBtn) {
    $transBtn.addEventListener('click', function() {
      _translationMode = !_translationMode;
      _applyTransMode();
    });
  }
  _applyTransMode();

  // Depth toggle — delegated from the dossier column since depth buttons are rendered
  // inside _renderDossier HTML and may not exist at init time
  document.getElementById('ws-dossier').addEventListener('click', function(e) {
    const btn = e.target.closest('[data-depth]');
    if (btn) _applyDepth(parseInt(btn.dataset.depth, 10));
  });

  _updateTopbarStats();
  _renderNav();
  _activatePhase();

  // SW-N: Flashcard system init — load state, wire buttons, keyboard handler
  // INTENT: Load deck + progress on init; wire the nav button to open flashcard view;
  //   wire "Add to deck" clicks delegated from dossier; wire rating and reveal buttons
  //   delegated from the flashcard view; wire keyboard shortcuts.
  // CHANGE? If flashcard view HTML IDs change, update getElementById calls in _fcOpenView.
  // VERIFY: Click ★ on G3056 in dossier → nav badge shows 1; click "Flashcards" → view opens.
  _fcLoadState();
  _fcUpdateBadge();

  // INTENT: Override window.wireRefLinks with a workshop-aware version that routes .ref
  //   link clicks to _studyPassage() instead of the main-site Bible Gateway popup.
  //   Every passage tab and flashcard that calls wireRefLinks(el) benefits automatically.
  // CHANGE? If main wire.js changes the wireRefLinks API, update only this adapter.
  // VERIFY: Click any verse-sample link in the dossier or Synthesis tab → workshop
  //   passage study opens for that reference; no Bible Gateway popup appears.
  window.wireRefLinks = function(root) {
    (root || document).querySelectorAll('a.ref[data-ref], span.ref[data-ref]').forEach(function(el) {
      el.style.cursor = 'pointer';
      el.removeAttribute('href');
      el.addEventListener('click', function(e) {
        e.preventDefault();
        var ref = el.dataset.ref;
        if (ref) _studyPassage(ref);
      });
    });
  };

  var fcNavBtn = document.getElementById('sw-flashcard-nav-btn');
  if (fcNavBtn) fcNavBtn.addEventListener('click', _fcOpenView);

  var fcCloseBtn = document.getElementById('sw-fc-close-btn');
  if (fcCloseBtn) fcCloseBtn.addEventListener('click', _fcCloseView);

  var fcDoneClose = document.getElementById('sw-fc-done-close');
  if (fcDoneClose) fcDoneClose.addEventListener('click', _fcCloseView);

  var fcRevealBtn = document.getElementById('sw-fc-reveal-btn');
  if (fcRevealBtn) fcRevealBtn.addEventListener('click', _fcReveal);

  // Rating buttons
  var fcView = document.getElementById('sw-flashcard-view');
  if (fcView) {
    fcView.querySelectorAll('.sw-fc-rate-btn[data-rating]').forEach(function(btn) {
      btn.addEventListener('click', function() { _fcRate(btn.dataset.rating); });
    });
  }

  // Delegated "Add to deck" clicks from dossier (button rendered inside _renderDossier HTML)
  document.getElementById('ws-dossier').addEventListener('click', function(e) {
    var btn = e.target.closest('.sw-add-deck-btn[data-code]');
    if (btn) _fcToggleDeck(btn.dataset.code);
  });

  document.addEventListener('keydown', _fcKeyHandler);

  // SW-N: Auto-open word from URL param ?s=G3056 (set by the "Link to this word" button)
  // INTENT: If the page is loaded with ?s=<StrongsCode>, open the dossier for that code
  //   so sharing/bookmarking a direct word link works. Also supports ?ref=John+1:1 to
  //   pre-load a passage.
  // CHANGE? If URL scheme changes from ?s= to ?word=, update the key name here.
  // VERIFY: Navigate to translation/workshop/?s=G3056 → page loads, λόγος dossier opens.
  //   Navigate with ?ref=Romans+8:1 → passage study loads automatically.
  var params = new URLSearchParams(location.search);
  var autoCode = params.get('s');
  var autoRef  = params.get('ref');
  if (autoCode) {
    await loadBooks();
    _openWord(autoCode);
  } else if (autoRef) {
    await loadBooks();
    if ($refInput) $refInput.value = autoRef;
    _studyPassage(autoRef);
  }

  // P19: verse lock — a link-toggled workshop panel in the Desk follows the
  // linked reader's navigation (desk-frame.js dispatches bsw:desk-goto).
  window.addEventListener('bsw:desk-goto', async function (e) {
    var ref = e.detail && e.detail.ref;
    if (!ref) return;
    if (ref.indexOf(':') === -1) ref += ':1';
    await loadBooks();
    if ($refInput) $refInput.value = ref;
    _studyPassage(ref);
  });
}
