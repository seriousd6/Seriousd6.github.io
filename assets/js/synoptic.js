/* synoptic.js — Synoptic parallel-passage panel injected into the reader */
'use strict';

import {
  getVersion, resolveVerses, parseRef, loadParallels, escHtml
} from './core.js';

// ── Parallels toggle ──────────────────────────────────────────────────────────
var _SYNOPTIC_KEY = 'bsw_parallels';

export function isParallelsEnabled()  { return localStorage.getItem(_SYNOPTIC_KEY) === '1'; }
export function setParallelsEnabled(on) {
  try { localStorage.setItem(_SYNOPTIC_KEY, on ? '1' : '0'); } catch (e) {}
}

// INTENT: Inject the ⇔ Parallels button into the reader browse bar.
//   Toggling on re-runs doLookup (which calls injectParallelPanels);
//   toggling off removes all existing synoptic panels without reloading.
// VERIFY: Navigate to Matthew 3 — button appears; click to enable — synoptic panel
//   shows below verse text with John Baptist parallel columns; click again — panel removed.
export function initParallelsToggle() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-parallels-btn')) return;
  var on = isParallelsEnabled();
  var btn = document.createElement('button');
  btn.id = 'reader-parallels-btn';
  btn.type = 'button';
  btn.className = 'reader-parallels-btn' + (on ? ' reader-parallels-btn--on' : '');
  btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  btn.title = 'Show synoptic parallel passages side by side';
  btn.textContent = '⇔ Parallels';
  // Prefer the 📖 Study Tools popover (interlinear.js); fall back to inline.
  var stPop = document.getElementById('reader-studytools-popover');
  if (stPop) {
    stPop.appendChild(btn);
  } else {
    var hint = browseBar.querySelector('.reader-browse-hint');
    browseBar.insertBefore(btn, hint || null);
  }

  btn.addEventListener('click', function () {
    on = !on;
    setParallelsEnabled(on);
    btn.classList.toggle('reader-parallels-btn--on', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) {
      if (typeof window._readerLookupFn === 'function') window._readerLookupFn();
    } else {
      document.querySelectorAll('.reader-synoptic-panel').forEach(function (p) { p.remove(); });
    }
  });
}

// INTENT: For each reader result group that has ≥1 type:parallel pericope overlapping
//   its rendered verses, append a synoptic panel below the group's text. Each pericope
//   gets its own panel: column 0 = primary passage (from already-loaded group verses),
//   columns 1..N = parallel passages fetched async via resolveVerses.
// CHANGE? Only type:"parallel" entries are shown here. type:"prophecy-source" and
//   type:"quotation" remain in the Connections (echoes) panel.
// VERIFY: Matthew 3 — panel appears with 3 columns (Matt/Mark/Luke); John 6 — 4 columns
//   (John/Matt/Mark/Luke); clicking ‹ on any column collapses it to a 36px strip with
//   vertical ref label; clicking › expands it again.
export function injectParallelPanels(groups, resultsEl) {
  if (!isParallelsEnabled()) return;
  var domGroups = resultsEl.querySelectorAll('.reader-result-group');
  var ver = getVersion();

  domGroups.forEach(function (groupEl, gIdx) {
    var g = groups[gIdx];
    if (!g || !g.verses || !g.ref || !g.ref.bookId) return;

    loadParallels(g.ref.bookId).then(function (parallelsData) {
      if (!parallelsData) return;

      var startCh = g.ref.ch   || 1;
      var endCh   = g.ref.endCh || startCh;

      // Collect pericopes whose verse range overlaps any verse currently on screen
      var pericopes = [];
      for (var ch = startCh; ch <= endCh; ch++) {
        var chData = parallelsData[String(ch)];
        if (!chData) continue;
        Object.keys(chData).forEach(function (vStr) {
          var entries = chData[vStr];
          if (!Array.isArray(entries)) return;
          entries.forEach(function (entry) {
            if (!entry || entry.type !== 'parallel') return;
            if (!entry.refs || !entry.refs.length) return;
            var startV = parseInt(vStr, 10);
            var endV   = entry.end || startV;
            var overlaps = g.verses.some(function (vObj) {
              return vObj.chapter === ch && vObj.verse >= startV && vObj.verse <= endV;
            });
            if (overlaps) {
              pericopes.push({ ch: ch, startV: startV, endV: endV, label: entry.label, refs: entry.refs });
            }
          });
        });
      }
      if (!pericopes.length) return;

      // Remove stale panels from a previous navigation to this group
      groupEl.querySelectorAll('.reader-synoptic-panel').forEach(function (p) { p.remove(); });

      pericopes.forEach(function (pericope) {
        var panel = _buildPanel(pericope, g, ver);
        var bottomNav = groupEl.querySelector('.reader-chapter-nav--bottom');
        if (bottomNav) groupEl.insertBefore(panel, bottomNav);
        else groupEl.appendChild(panel);
      });
    }).catch(function () {});
  });
}

// Build the full synoptic panel DOM for one pericope.
function _buildPanel(pericope, g, ver) {
  var panel = document.createElement('div');
  panel.className = 'reader-synoptic-panel';

  // INTENT: the label bar is a toggle so a reader can collapse a parallel they've
  //   finished reading — useful when several synoptic panels stack up and you don't
  //   want to scroll past read ones to reach the next passage.
  // CHANGE? Collapsed state = class `reader-synoptic-panel--collapsed` on the panel,
  //   which reader.css uses to hide `.reader-synoptic-grid` and rotate the chevron.
  //   Session-only (not persisted).
  // VERIFY: Open a chapter with synoptic parallels (e.g. Mark 1); click a panel's
  //   label — its columns collapse and the chevron points right; click again to expand.
  var labelRow = document.createElement('button');
  labelRow.type = 'button';
  labelRow.className = 'reader-synoptic-label';
  labelRow.setAttribute('aria-expanded', 'true');

  var chev = document.createElement('span');
  chev.className = 'reader-synoptic-chevron';
  chev.setAttribute('aria-hidden', 'true');
  chev.textContent = '▾';
  var lblText = document.createElement('span');
  lblText.className = 'reader-synoptic-label-text';
  // textContent escapes safely on its own; escHtml here would double-encode (an
  // apostrophe in a label like "John's proclamation" would display as "John&#39;s").
  lblText.textContent = pericope.label || 'Parallel Passage';
  labelRow.appendChild(chev);
  labelRow.appendChild(lblText);

  labelRow.addEventListener('click', function () {
    var collapsed = panel.classList.toggle('reader-synoptic-panel--collapsed');
    labelRow.setAttribute('aria-expanded', String(!collapsed));
  });
  panel.appendChild(labelRow);

  var grid = document.createElement('div');
  grid.className = 'reader-synoptic-grid';
  panel.appendChild(grid);

  // Column 0: primary (already-loaded verses from the group)
  var primaryRef = g.ref.bookName + ' ' +
    pericope.ch + ':' + pericope.startV +
    (pericope.endV !== pericope.startV ? '–' + pericope.endV : '');
  var colPrimary = _buildCol(primaryRef, true);
  var primaryVerses = g.verses.filter(function (vObj) {
    return vObj.chapter === pericope.ch &&
           vObj.verse >= pericope.startV &&
           vObj.verse <= pericope.endV;
  });
  _fillColText(colPrimary.textEl, primaryVerses);
  grid.appendChild(colPrimary.colEl);

  // Columns 1..N: parallel passages (async)
  pericope.refs.forEach(function (refEntry) {
    var passage = refEntry.passage || '';
    var col = _buildCol(passage, false);
    col.colEl.classList.add('reader-synoptic-col--loading');
    col.textEl.textContent = '…';
    grid.appendChild(col.colEl);

    var parsed = parseRef(passage);
    if (!parsed) {
      col.colEl.classList.remove('reader-synoptic-col--loading');
      col.textEl.innerHTML = '<span class="reader-synoptic-unavail">—</span>';
      return;
    }

    resolveVerses(parsed, ver)
      .then(function (verses) {
        col.colEl.classList.remove('reader-synoptic-col--loading');
        _fillColText(col.textEl, verses || []);
      })
      .catch(function () {
        col.colEl.classList.remove('reader-synoptic-col--loading');
        col.textEl.innerHTML = '<span class="reader-synoptic-unavail">Could not load.</span>';
      });
  });

  return panel;
}

// Build a column element with header (ref label + collapse button) and text area.
// Returns { colEl, textEl } so the caller can fill textEl separately.
function _buildCol(refStr, isPrimary) {
  var colEl = document.createElement('div');
  colEl.className = 'reader-synoptic-col' + (isPrimary ? ' reader-synoptic-col--primary' : '');

  var hdr = document.createElement('div');
  hdr.className = 'reader-synoptic-col-hdr';

  var refSpan = document.createElement('span');
  refSpan.className = 'reader-synoptic-col-ref';
  refSpan.textContent = refStr;

  var collapseBtn = document.createElement('button');
  collapseBtn.type = 'button';
  collapseBtn.className = 'reader-synoptic-col-collapse';
  collapseBtn.setAttribute('aria-expanded', 'true');
  collapseBtn.setAttribute('aria-label', 'Collapse ' + refStr);
  collapseBtn.textContent = '‹'; // ‹

  hdr.appendChild(refSpan);
  hdr.appendChild(collapseBtn);

  var textEl = document.createElement('div');
  textEl.className = 'reader-synoptic-col-text';

  colEl.appendChild(hdr);
  colEl.appendChild(textEl);

  collapseBtn.addEventListener('click', function () {
    var collapsed = colEl.classList.toggle('reader-synoptic-col--collapsed');
    collapseBtn.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
    collapseBtn.textContent = collapsed ? '›' : '‹'; // › / ‹
  });

  return { colEl: colEl, textEl: textEl };
}

// Render verses as flowing text with superscript verse numbers.
function _fillColText(textEl, verses) {
  textEl.innerHTML = '';
  if (!verses || !verses.length) {
    var miss = document.createElement('span');
    miss.className = 'reader-synoptic-unavail';
    miss.textContent = 'Not available in this version.';
    textEl.appendChild(miss);
    return;
  }
  var p = document.createElement('p');
  p.className = 'reader-synoptic-text';
  verses.forEach(function (vObj) {
    var sup = document.createElement('sup');
    sup.className = 'reader-synoptic-vnum';
    sup.textContent = String(vObj.verse);
    p.appendChild(sup);
    p.appendChild(document.createTextNode((vObj.text || '') + ' '));
  });
  textEl.appendChild(p);
}
