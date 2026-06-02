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
function _notesUrl(bookId) {
  return _resolve('../../data/translation/notes/' + bookId + '.json');
}
function _tierUrl(tier, bookId) {
  return _resolve('../../data/translation/draft/' + tier + '/' + bookId + '.json');
}

/* ── In-memory cache ───────────────────────────────────────────── */
var _notesCache = {};   // bookId → notes object
var _tierCache  = {};   // tier+bookId → verse text object

/* ── Fetch helpers ─────────────────────────────────────────────── */
async function _loadNotes(bookId) {
  if (_notesCache[bookId]) return _notesCache[bookId];
  try {
    var res = await fetch(_notesUrl(bookId));
    if (!res.ok) throw new Error(res.status);
    _notesCache[bookId] = await res.json();
  } catch(e) {
    _notesCache[bookId] = null;
  }
  return _notesCache[bookId];
}

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
var _expandedCode = null;

function _renderTokenGrid(tokens, container, ch, v) {
  var grid = document.createElement('div');
  grid.className = 'olc-grid';

  var expandPanel = document.createElement('div');
  expandPanel.className = 'olc-expand-panel';
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
          return;
        }
        // collapse previous
        grid.querySelectorAll('.olc-token--open')
          .forEach(function(el) { el.classList.remove('olc-token--open'); });
        _expandedCode = t.code;
        card.classList.add('olc-token--open');
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
export async function initOLSection(parsed, vsCreateSection, vsRebuildNav) {
  if (!parsed || !parsed.bookId || !parsed.ch || !parsed.v) return;

  var sec = vsCreateSection(document.getElementById('vs-sections-container'), 'vs-ol-companion', 'Original Language');
  if (!sec) return;

  var body = sec.bodyEl;
  body.innerHTML = '<p class="olc-loading">Loading original language data…</p>';
  sec.el.removeAttribute('hidden');
  vsRebuildNav();

  var notes = await _loadNotes(parsed.bookId);
  body.innerHTML = '';

  if (!notes) {
    body.innerHTML = '<p class="olc-empty">Original language notes not available for this book. Run <code>python3 scripts/generate-notes.py</code> to generate them.</p>';
    return;
  }

  var chData = notes[String(parsed.ch)];
  var vData  = chData && chData[String(parsed.v)];

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
