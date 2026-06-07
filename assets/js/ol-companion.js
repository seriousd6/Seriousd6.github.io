/* ol-companion.js — Original Language Companion for Verse Study
 *
 * Adds an "Original Language" section to every Verse Study page, showing:
 *   — Word-by-word token grid (lemma · transliteration · MKT rendering)
 *     Click any token → expanded panel with semantic range, all three tiers,
 *     dispute flag explanation, and tier divergence note
 *   — Dispute flags for theologically contested vocabulary in the verse
 *   — MKT three-tier comparison (Literal / Mediating / Thought)
 *   — Sentence structure note
 *
 * Data sources (all lazy, cached by book):
 *   data/translation/notes/{bookId}.json       — per-verse token analysis
 *   data/translation/draft/literal/{book}.json  — MKT Literal tier draft
 *   data/translation/draft/mediating/{book}.json
 *   data/translation/draft/thought/{book}.json
 */
'use strict';

import { _resolve } from './core.js';

/* ── URL builders ──────────────────────────────────────────────── */
// INTENT: Builds path to the per-chapter notes file — chapter granularity keeps each fetch
//   to ~20–50 KB instead of the 3–5 MB whole-book file that was fetched previously (PERF-5).
// CHANGE? If the chapter-split layout changes, update scripts/split-notes.py and _loadNotes cache key.
// VERIFY: Network tab shows data/translation/notes/john/3.json (not notes/john.json) on John 3:16 load.
function _notesUrl(bookId, ch) {
  return _resolve('../../data/translation/notes/' + bookId + '/' + ch + '.json');
}
function _tierUrl(tier, bookId) {
  return _resolve('../../data/translation/draft/' + tier + '/' + bookId + '.json');
}

/* ── In-memory cache ───────────────────────────────────────────── */
var _notesCache = {};   // "bookId:ch" → chapter verses object (one entry per chapter, not per book)
var _tierCache  = {};   // tier+bookId → verse text object

/* ── Fetch helpers ─────────────────────────────────────────────── */
// INTENT: Fetches a single chapter's token-analysis file from data/translation/notes/{bookId}/{ch}.json.
//   Cache key is "bookId:ch" so navigating from John 3 → John 4 costs exactly one extra fetch,
//   and revisiting John 3 is free. Previously the whole book was fetched (3–5 MB per book).
// CHANGE? Cache key format must stay "bookId:ch" (colon-separated); if you change it, clear stale
//   entries or users will re-fetch on every chapter visit. If _notesUrl layout changes, update here.
// VERIFY: Open verse-study for John 3:16 → Network shows notes/john/3.json (~20-50 KB, not 3.86 MB).
//   Navigate to John 4:1 → exactly one more fetch for notes/john/4.json, not a full re-fetch.
async function _loadNotes(bookId, ch) {
  var key = bookId + ':' + ch;
  if (key in _notesCache) return _notesCache[key];
  try {
    var res = await fetch(_notesUrl(bookId, ch));
    if (!res.ok) throw new Error(res.status);
    _notesCache[key] = await res.json();
  } catch(e) {
    _notesCache[key] = null;
  }
  return _notesCache[key];
}

// INTENT: Loads one MKT tier draft (literal/mediating/thought) for a whole book per call,
//   since tier files are ~300 KB and already per-book (no chapter split needed at this size).
// CHANGE? Cache key is "tier:bookId" (e.g. "literal:john"). If tier names change in _tierUrl
//   or if per-chapter tier files are introduced, the key format and lookup must change to match.
// VERIFY: Network tab on verse-study load shows three tier fetches (literal/mediating/thought)
//   for the current book; revisiting the same book should show no tier re-fetches.
async function _loadTier(tier, bookId) {
  var key = tier + ':' + bookId;
  if (_tierCache[key] !== undefined) return _tierCache[key];
  try {
    var res = await fetch(_tierUrl(tier, bookId));
    if (!res.ok) throw new Error(res.status);
    _tierCache[key] = await res.json();
  } catch(e) {
    _tierCache[key] = null;
  }
  return _tierCache[key];
}

/* ── Dispute level labels ──────────────────────────────────────── */
var DISP_LABELS = ['', 'minor debate', 'moderate debate', 'contested', 'major debate'];
var DISP_COLORS = ['', 'olc-disp-1', 'olc-disp-2', 'olc-disp-3', 'olc-disp-4'];

/* ── Helpers ───────────────────────────────────────────────────── */
function _esc(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function _pos_label(pos) {
  var MAP = {
    verb:'verb', noun:'noun', adjective:'adj.', adverb:'adv.',
    preposition:'prep.', conjunction:'conj.', pronoun:'pron.',
    article:'art.', particle:'part.',
  };
  return MAP[pos] || pos || '';
}

/* ── Token grid rendering ──────────────────────────────────────── */
// INTENT: _expandedCode tracks which token is currently open across the single expand panel.
//   Module-level so collapse-previous logic in the click handler can find any open button.
// CHANGE? Only one token grid per page is supported — if multiple grids are ever rendered
//   simultaneously (e.g., a split-verse view), refactor _expandedCode into a Map keyed by panelId
//   so each grid manages its own open/closed state independently.
// VERIFY: Click one token, then a different one — the first should close (aria-expanded="false"),
//   the second should open (aria-expanded="true"). No two tokens should be open simultaneously.
var _expandedCode = null;

// INTENT: Builds the clickable word-token grid for a single verse and inserts a shared expand
//   panel below it. Each token button uses an IIFE closure `(function(t){...})(tok)` so the
//   click handler captures `t` by value — without the IIFE, all handlers would close over the
//   same mutable loop variable and expand the last token only.
// CHANGE? panelId is derived from ch+v; if initOLSection is ever called for multiple verses on
//   one page, ensure each call produces a distinct ch/v pair, or generate a unique panel suffix.
// VERIFY: Click any token → expand panel appears below the grid with the token's semantic data.
//   Clicking the same token again collapses it. DevTools → Accessibility: aria-expanded toggles.
function _renderTokenGrid(tokens, container, ch, v) {
  var grid = document.createElement('div');
  grid.className = 'olc-grid';

  // INTENT: Single shared expand panel per verse grid; ID ties card aria-controls to this element.
  // CHANGE? If _renderTokenGrid is ever called for multiple simultaneous verses, make the ID unique per call.
  // VERIFY: DevTools → Elements: #olc-exp-{ch}-{v} exists; each .olc-token has aria-controls matching it.
  var panelId = 'olc-exp-' + ch + '-' + v;
  var expandPanel = document.createElement('div');
  expandPanel.className = 'olc-expand-panel';
  expandPanel.id = panelId;
  expandPanel.hidden = true;

  tokens.forEach(function(tok) {
    if (!tok.code) {
      // punctuation / unlabelled
      var sep = document.createElement('span');
      sep.className = 'olc-sep';
      sep.textContent = tok.text || '';
      grid.appendChild(sep);
      return;
    }

    var card = document.createElement('button');
    card.className = 'olc-token';
    if (tok.disp >= 2) card.classList.add(DISP_COLORS[tok.disp] || '');
    card.dataset.code = tok.code;
    card.setAttribute('aria-expanded', 'false');
    card.setAttribute('aria-controls', panelId);

    var lemma = document.createElement('span');
    lemma.className = 'olc-token__lemma';
    lemma.textContent = tok.lemma || tok.code;

    var translit = document.createElement('span');
    translit.className = 'olc-token__translit';
    translit.textContent = tok.translit || '';

    var med = document.createElement('span');
    med.className = 'olc-token__med';
    med.textContent = tok.med || tok.text || '';

    card.appendChild(lemma);
    if (tok.translit) card.appendChild(translit);
    card.appendChild(med);

    (function(t) {
      card.addEventListener('click', function() {
        if (_expandedCode === t.code) {
          _expandedCode = null;
          expandPanel.hidden = true;
          card.classList.remove('olc-token--open');
          card.setAttribute('aria-expanded', 'false');
          return;
        }
        // collapse previous
        grid.querySelectorAll('.olc-token--open').forEach(function(el) {
          el.classList.remove('olc-token--open');
          el.setAttribute('aria-expanded', 'false');
        });
        _expandedCode = t.code;
        card.classList.add('olc-token--open');
        card.setAttribute('aria-expanded', 'true');
        _renderExpandPanel(t, expandPanel);
        expandPanel.hidden = false;
        // Insert expand panel after the grid row
        if (expandPanel.parentNode !== container) {
          container.appendChild(expandPanel);
        }
        expandPanel.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      });
    })(tok);

    grid.appendChild(card);
  });

  container.appendChild(grid);
  container.appendChild(expandPanel);
}

function _renderExpandPanel(tok, panel) {
  var disp = tok.disp || 0;

  var html = '<div class="olc-exp">';

  // Header
  html += '<div class="olc-exp__head">';
  html += '<span class="olc-exp__lemma">' + _esc(tok.lemma || tok.code) + '</span>';
  if (tok.translit) html += ' <span class="olc-exp__translit">' + _esc(tok.translit) + '</span>';
  html += ' <span class="olc-exp__code">' + _esc(tok.code) + '</span>';
  if (tok.pos)  html += ' <span class="olc-exp__pos">' + _esc(_pos_label(tok.pos)) + '</span>';
  if (disp > 0) html += ' <span class="olc-exp__disp ' + DISP_COLORS[disp] + '">⚑ ' + _esc(DISP_LABELS[disp]) + '</span>';
  html += '</div>';

  // Interlinear rendering in this verse
  html += '<div class="olc-exp__row"><span class="olc-exp__label">In this verse:</span>'
        + '<span class="olc-exp__val">' + _esc(tok.text || '') + '</span></div>';

  // MKT tiers
  html += '<div class="olc-exp__tiers">';
  html += '<div class="olc-exp__tier-label">MKT Renderings</div>';
  html += '<table class="olc-exp__tier-table"><tbody>';
  html += '<tr><th class="olc-tier-lit">Literal</th><td>' + _esc(tok.lit || tok.med || tok.text || '—') + '</td></tr>';
  html += '<tr><th class="olc-tier-med">Mediating</th><td>' + _esc(tok.med || tok.text || '—') + '</td></tr>';
  html += '<tr><th class="olc-tier-tho">Thought</th><td>' + _esc(tok.tho || tok.med || tok.text || '—') + '</td></tr>';
  html += '</tbody></table>';
  html += '</div>';

  // Tier divergence note
  if (tok.lit && tok.tho && tok.lit !== tok.tho) {
    html += '<div class="olc-exp__note olc-exp__note--div">';
    html += '<strong>Tier spread:</strong> The Literal renders this "' + _esc(tok.lit)
          + '" while the Thought tier renders it "' + _esc(tok.tho)
          + '". This gap represents the range of legitimate interpretive choice.';
    html += '</div>';
  }

  // Semantic range
  if (tok.range) {
    html += '<div class="olc-exp__section-label">Semantic Range</div>';
    html += '<p class="olc-exp__range">' + _esc(tok.range) + '</p>';
  }

  html += '</div>'; // .olc-exp
  panel.innerHTML = html;
}

/* ── Flags (high-dispute terms) ────────────────────────────────── */
function _renderFlags(flags, container) {
  if (!flags || !flags.length) return;

  var heading = document.createElement('div');
  heading.className = 'olc-subhead';
  heading.textContent = 'Theologically Contested Vocabulary in This Verse';
  container.appendChild(heading);

  flags.forEach(function(f) {
    var card = document.createElement('div');
    card.className = 'olc-flag-card ' + (DISP_COLORS[f.disp] || '');

    var title = document.createElement('div');
    title.className = 'olc-flag-card__title';
    title.innerHTML = '<span class="olc-flag-lemma">' + _esc(f.lemma || '') + '</span>'
                    + ' <span class="olc-flag-code">(' + _esc(f.code) + ')</span>'
                    + ' <span class="olc-flag-disp">⚑ ' + _esc(DISP_LABELS[f.disp] || '') + '</span>';

    var note = document.createElement('p');
    note.className = 'olc-flag-card__note';
    note.textContent = f.note || '';

    card.appendChild(title);
    card.appendChild(note);
    container.appendChild(card);
  });
}

/* ── Tier comparison ───────────────────────────────────────────── */
async function _renderTierComparison(parsed, container) {
  var table = document.createElement('table');
  table.className = 'olc-tier-cmp';

  var tiers = [
    { id: 'literal',   label: 'Literal',   cls: 'olc-tier-lit' },
    { id: 'mediating', label: 'Mediating', cls: 'olc-tier-med' },
    { id: 'thought',   label: 'Thought',   cls: 'olc-tier-tho' },
  ];

  var heading = document.createElement('div');
  heading.className = 'olc-subhead';
  heading.textContent = 'MKT Three-Tier Rendering';
  container.appendChild(heading);

  var note = document.createElement('p');
  note.className = 'olc-tier-note';
  note.textContent = 'These are first-draft interlinear renderings. Accuracy improves as glossary entries are reviewed in the Translation Workshop.';
  container.appendChild(note);

  var tbody = document.createElement('tbody');
  table.appendChild(tbody);
  container.appendChild(table);

  await Promise.all(tiers.map(async function(tier) {
    var data = await _loadTier(tier.id, parsed.bookId);
    var text = data && data[String(parsed.ch)] && data[String(parsed.ch)][String(parsed.v)];
    var tr = document.createElement('tr');
    tr.innerHTML = '<th class="' + tier.cls + '">' + tier.label + '</th>'
                 + '<td>' + _esc(text || '(not yet generated)') + '</td>';
    tbody.appendChild(tr);
  }));
}

/* ── Tier divergences summary ──────────────────────────────────── */
function _renderDivergences(divergences, container) {
  if (!divergences || !divergences.length) return;

  var heading = document.createElement('div');
  heading.className = 'olc-subhead';
  heading.textContent = 'Translation Range — Where Tiers Diverge';
  container.appendChild(heading);

  var p = document.createElement('p');
  p.className = 'olc-div-intro';
  p.textContent = 'These words have different renderings across the three tiers, showing the range of legitimate interpretive choice:';
  container.appendChild(p);

  var list = document.createElement('ul');
  list.className = 'olc-div-list';
  divergences.forEach(function(d) {
    var li = document.createElement('li');
    li.innerHTML = '<strong>' + _esc(d.lemma || d.code) + '</strong>'
      + ': Literal "' + _esc(d.lit) + '" → Thought "' + _esc(d.tho) + '"';
    list.appendChild(li);
  });
  container.appendChild(list);
}

/* ── Structure note ────────────────────────────────────────────── */
function _renderStructureNote(struct, container) {
  if (!struct) return;
  var p = document.createElement('p');
  p.className = 'olc-struct-note';
  p.innerHTML = '<strong>Verse character:</strong> ' + _esc(struct);
  container.appendChild(p);
}

/* ── Main section init ─────────────────────────────────────────── */
// INTENT: Entry point called by verse-study.js after the focal verse resolves. Orchestrates
//   four async loads (per-chapter notes, plus Literal/Mediating/Thought tier drafts) and builds
//   the full Original Language section DOM, including token grid, dispute flags, tier comparison,
//   and structure note.
// CHANGE? Caller is verse-study.js (window.BibleUI.initOLSection). The vsCreateSection and
//   vsRebuildNav callbacks come from verse-study.js — if that API changes, update both sides.
//   If parsed.bookId or parsed.ch format changes, the cache key in _loadNotes must also change.
// VERIFY: Open verse-study for John 3:16 — "Original Language" section appears in the nav and
//   body with the word-by-word grid. Selecting a token shows its semantic range. No console errors.
export async function initOLSection(parsed, vsCreateSection, vsRebuildNav) {
  if (!parsed || !parsed.bookId || !parsed.ch || !parsed.v) return;

  var sec = vsCreateSection(document.getElementById('vs-sections-container'), 'vs-ol-companion', 'Original Language');
  if (!sec) return;

  var body = sec.bodyEl;
  body.innerHTML = '<p class="olc-loading">Loading original language data…</p>';
  sec.el.removeAttribute('hidden');
  vsRebuildNav();

  // Chapter file schema: { "v": { tokens, flags, div, struct } } — no outer chapter key.
  var notes = await _loadNotes(parsed.bookId, parsed.ch);
  body.innerHTML = '';

  if (!notes) {
    body.innerHTML = '<p class="olc-empty">Original language notes not available for ' + (parsed.bookId || 'this book') + ' chapter ' + parsed.ch + '. The interlinear source may not have data for this chapter.</p>';
    return;
  }

  var vData = notes[String(parsed.v)];

  if (!vData) {
    body.innerHTML = '<p class="olc-empty">No notes available for this verse.</p>';
    return;
  }

  // Structure note
  _renderStructureNote(vData.struct, body);

  // Token grid
  if (vData.tokens && vData.tokens.length) {
    var gridHead = document.createElement('div');
    gridHead.className = 'olc-subhead';
    gridHead.textContent = 'Word-by-Word Analysis';
    body.appendChild(gridHead);

    var gridNote = document.createElement('p');
    gridNote.className = 'olc-grid-note';
    gridNote.textContent = 'Click any word for its semantic range, all three MKT tier renderings, and notes on its translation.';
    body.appendChild(gridNote);

    _renderTokenGrid(vData.tokens, body, parsed.ch, parsed.v);
  }

  // Flags
  _renderFlags(vData.flags, body);

  // Tier divergences
  _renderDivergences(vData.div, body);

  // Three-tier comparison (async)
  await _renderTierComparison(parsed, body);
}
