/* lib-reader.js — Unified library document reader (library/read/index.html) */
'use strict';

import { _resolve, escHtml } from './core.js';
import { wireRefLinks, autoTagRefs } from './wire.js';
import { autoTagTermsWhenReady } from './terms.js';

var LIB_INDEX_URL = _resolve('../../data/library/index.json');
var LIB_DOCS_ROOT = _resolve('../../data/library/docs/');
var LIB_HTML_ROOT = _resolve('../../data/library/html/');

var _PAGINATE_THRESHOLD = 1;   // all multi-section docs load one section at a time
var _TAB_BAR_MAX        = 7;   // ≤ this many sections → show tab strip; more → dropdown
var _SUBPAGE_SIZE       = 50;  // paragraphs per sub-page within a long section
var _LIB_POS_PREFIX     = 'bsw_lbpos_';
var _libIndex           = null;  // full catalog index (set on load, used for vol switcher)
var _keyListener        = null;  // paginated-mode arrow-key listener
var _subPageState       = null;  // { goTo, current, total } — set by _wireSubPager; arrow keys check this first

var _findTerm      = '';    // active in-reader search term (persists across paginated re-renders)
var _findMatchSecs = [];    // section indices containing the term (paginated mode)
var _findCurrMatch = 0;     // which match index is currently shown
var _findMarks     = [];    // scroll-mode: the <mark> nodes for the current term, in order
var _findBarWired  = false; // header find bar only gets event listeners once per document

// INTENT: Read saved section position from localStorage; handles both the legacy bare-integer
//   format (stored before the {idx, ts} shape was introduced) and current JSON shape.
// CHANGE? If the _savePos schema changes, update the /^\d+$/ legacy branch accordingly.
// VERIFY: Navigate to any doc, advance a few sections, reload the page — same section loads.
function _loadPos(docId) {
  try {
    var raw = localStorage.getItem(_LIB_POS_PREFIX + docId);
    if (!raw) return 0;
    if (/^\d+$/.test(raw)) return parseInt(raw, 10) || 0; // legacy bare int
    return JSON.parse(raw).idx || 0;
  } catch(e) { return 0; }
}
// INTENT: Persist current section index as { idx, ts } under `bsw_lbpos_{docId}`;
//   the `ts` timestamp is used by _evictStalePositions to expire old entries.
// CHANGE? _loadPos reads this exact shape; `_LIB_POS_PREFIX` must match in both functions.
// VERIFY: After navigating to section 3 of any doc, open DevTools → Application → Local Storage
//   and confirm a `bsw_lbpos_<docId>` key with `{"idx":2,"ts":...}` exists.
function _savePos(docId, idx) {
  try { localStorage.setItem(_LIB_POS_PREFIX + docId, JSON.stringify({ idx: idx, ts: Date.now() })); } catch(e) {}
}

// INTENT: Remove `bsw_lbpos_*` localStorage entries older than 90 days to prevent unbounded
//   growth if a user reads many different documents over time. Iterates in reverse so that
//   `localStorage.length` index stays valid after each `removeItem` call.
// CHANGE? `_LIB_POS_PREFIX` must match `_loadPos`/`_savePos`; legacy bare-int entries are
//   skipped (no `ts` field) and not evicted — they are overwritten on next section advance.
// VERIFY: In DevTools console: manually set a `bsw_lbpos_test` key with a stale ts, reload —
//   the key should be gone after the next `initLibReaderPage` call.
function _evictStalePositions() {
  try {
    var cutoff = Date.now() - 90 * 24 * 60 * 60 * 1000;
    for (var i = localStorage.length - 1; i >= 0; i--) {
      var key = localStorage.key(i);
      if (!key || key.indexOf(_LIB_POS_PREFIX) !== 0) continue;
      var raw = localStorage.getItem(key);
      if (!raw || /^\d+$/.test(raw)) continue;
      try { var d = JSON.parse(raw); if (d.ts && d.ts < cutoff) localStorage.removeItem(key); } catch(ex) {}
    }
  } catch(e) {}
}

// INTENT: Entry point for `library/read/index.html`; reads `?doc=` and optional `?section=`
//   URL params, fetches the document (JSON from `data/library/docs/` or legacy HTML from
//   `data/library/html/`), restores the saved section position, and renders the full reader.
// CHANGE? Called by `app.js:249` when `#lib-reader-content` is present on the page.
//   URL param names (`doc`, `section`) are also used by `lib-browser.js:_openDoc` (fullscreen link)
//   and `lib-progress.js` (reading-history links) — change all three together.
// VERIFY: Navigate to `library/read/?doc=heidelberg-catechism` → doc loads with TOC + paginated
//   sections; arrow keys advance sections; position is restored on reload.
export function initLibReaderPage() {
  var content = document.getElementById('lib-reader-content');
  if (!content) return;

  _evictStalePositions();

  var _params = new URLSearchParams(window.location.search);
  var docId   = _params.get('doc');
  if (!docId) {
    content.innerHTML = '<p class="lr-error">No document specified. <a href="../">Return to Library</a></p>';
    return;
  }

  content.innerHTML = '<p class="lr-loading">Loading…</p>';

  // Retry up to 2 times with 900ms delay — handles transient network errors on large files
  function fetchRetry(url, retries) {
    return fetch(url).then(function(r) {
      if (r.ok) return r;
      return Promise.reject(r.status);
    }).catch(function(err) {
      if (retries > 0) {
        return new Promise(function(res) { setTimeout(res, 900); })
          .then(function() { return fetchRetry(url, retries - 1); });
      }
      return Promise.reject(err);
    });
  }

  // Fetch the catalog index first so we can resolve html_url and build the vol switcher
  fetchRetry(LIB_INDEX_URL, 2)
    .then(function(r) { return r.json(); })
    .then(function(index) {
      _libIndex = index;
      var entry   = index.find(function(d) { return d.id === docId; });
      var htmlUrl = entry && entry.html_url;

      var fetchPromise = htmlUrl
        ? fetchRetry(LIB_HTML_ROOT + htmlUrl, 2)
            .then(function(r) { return r.text(); })
            .then(function(html) { return _parseHtmlDoc(docId, html, entry); })
        : fetchRetry(LIB_DOCS_ROOT + docId + '.json', 2)
            .then(function(r) { return r.json(); });

      return fetchPromise.then(function(doc) { return { doc: doc, entry: entry }; });
    })
    .then(function(result) { _render(result.doc, docId, content, result.entry); })
    .catch(function(err) {
      console.error('[LibReader]', err);
      content.innerHTML = '<p class="lr-error">Could not load document — please try again. <a href="../">Return to Library</a></p>';
    });
}

// Parse a standalone HTML file into the same {id, title, type, sections} shape the renderer expects.
// Mirrors the equivalent function in lib-browser.js.
function _parseHtmlDoc(docId, html, entry) {
  var wrap = document.createElement('div');
  wrap.innerHTML = html;
  var sections = [];
  wrap.querySelectorAll('section[data-heading]').forEach(function(el) {
    sections.push({ ref: String(sections.length + 1), heading: el.getAttribute('data-heading'), html: el.innerHTML });
  });
  if (!sections.length) sections.push({ ref: '1', heading: '', html: html });
  return {
    id:            docId,
    title:         (entry && entry.title)      || docId,
    type:          (entry && entry.type)       || '',
    year:          (entry && entry.year)       || null,
    tradition:     (entry && entry.tradition)  || '',
    totalSections: sections.length,
    sections:      sections
  };
}

var _TYPE_BADGE = {
  creed: 'ecumenical', confession: 'reformed', catechism: 'reformed', canons: 'reformed',
  council: 'ecumenical', encyclical: 'roman-catholic', father: 'patristic',
  apologetics: 'patristic', commentary: 'reformed', devotional: 'ecumenical',
  history: 'ecumenical', liturgy: 'ecumenical', sermon: 'ecumenical'
};
var _TYPE_LABEL = {
  creed: 'Creed', confession: 'Confession', catechism: 'Catechism', canons: 'Canons',
  council: 'Council', encyclical: 'Encyclical', father: 'Church Father',
  apologetics: 'Apologetics', commentary: 'Commentary', devotional: 'Devotional',
  history: 'History', liturgy: 'Liturgy', sermon: 'Sermon'
};

function _volHtml(doc, entry) {
  if (!entry || !entry.series || !_libIndex) return '';
  var siblings = _libIndex
    .filter(function(d) { return d.series === entry.series; })
    .sort(function(a, b) { return (a.volume || 0) - (b.volume || 0); });
  if (siblings.length < 2) return '';
  var html = '<div class="lr-reader-volumes">';
  siblings.forEach(function(sib) {
    var active = sib.id === doc.id ? ' lr-vol-chip--active' : '';
    html += '<a class="lr-vol-chip' + active + '" href="?doc=' + encodeURIComponent(sib.id) + '">' +
              escHtml(sib.volume_label || sib.title) +
            '</a>';
  });
  return html + '</div>';
}


function _render(doc, docId, content, entry) {
  document.title = doc.title + ' — Library — Bible Study';

  _findTerm      = '';
  _findMatchSecs = [];
  _findCurrMatch = 0;
  _findBarWired  = false;

  var sections  = doc.sections || [];
  var paginated = sections.length > _PAGINATE_THRESHOLD;
  var badge     = (entry && entry.tradition) || _TYPE_BADGE[doc.type] || 'ecumenical';
  var label     = _TYPE_LABEL[doc.type] || doc.type;
  var author    = entry && entry.author;

  var header = document.getElementById('lib-reader-header');
  if (header) {
    header.innerHTML =
      '<a class="lr-back" href="../">← Library</a>' +
      '<div class="lr-title-row">' +
        '<h1 class="lr-doc-title">' + escHtml(doc.title) + '</h1>' +
        '<button class="lr-find-btn" id="lr-find-btn" title="Find in document" aria-label="Find in document">&#x1F50D;</button>' +
      '</div>' +
      '<div class="lib-meta">' +
        '<span class="lib-badge lib-badge--' + escHtml(badge) + '">' + escHtml(label) + '</span>' +
        (doc.year   ? '<span>' + escHtml(String(doc.year)) + '</span>' : '') +
        (author     ? '<span>' + escHtml(author) + '</span>'            : '') +
        (sections.length > 1
          ? '<span>' + sections.length + ' ' + escHtml(_sectionLabel(doc.type, sections.length)) + '</span>'
          : '') +
        '<span class="lr-section-counter" id="lr-section-counter"></span>' +
      '</div>' +
      _volHtml(doc, entry) +
      '<div class="lr-find-bar" id="lr-find-bar" hidden>' +
        '<input class="lr-find-input" id="lr-find-input" type="search" placeholder="Find in document…" autocomplete="off" aria-label="Find text">' +
        '<button class="lr-find-submit" id="lr-find-submit">Find</button>' +
        '<button class="lr-find-nav lr-find-prev" id="lr-find-prev" aria-label="Previous match" hidden>&#x2191;</button>' +
        '<button class="lr-find-nav lr-find-next" id="lr-find-next" aria-label="Next match" hidden>&#x2193;</button>' +
        '<span class="lr-find-result" id="lr-find-result"></span>' +
        '<button class="lr-find-close" id="lr-find-close" aria-label="Close find bar">&#x2715;</button>' +
      '</div>';
  }

  if (paginated) {
    var sidebar = document.getElementById('lib-reader-toc');
    if (sidebar) { var sb = sidebar.closest('.lr-sidebar'); if (sb) sb.hidden = true; }
    // URL section param takes priority over localStorage position (enables deep links)
    var urlSec = parseInt(new URLSearchParams(window.location.search).get('section') || '0', 10) || 0;
    var idx = urlSec > 0 ? urlSec : _loadPos(docId);
    idx = Math.max(0, Math.min(idx, sections.length - 1));
    _renderPaged(doc, docId, sections, idx, content, entry);
  } else {
    if (_keyListener) { document.removeEventListener('keydown', _keyListener); _keyListener = null; }
    _renderScroll(doc, docId, sections, content, entry);
  }

  _saveLibProgress(docId, doc.title, sections.length, (entry && entry.tradition) || '');
}

/* ── Text highlighting helpers (mirrors lib-browser.js) ─────────────────── */

function _highlightInEl(el, term) {
  if (!term) return [];
  var marks  = [];
  var lterm  = term.toLowerCase();
  var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null, false);
  var nodes  = [];
  var node;
  while ((node = walker.nextNode())) nodes.push(node);
  nodes.forEach(function(textNode) {
    var text = textNode.nodeValue;
    var ltxt = text.toLowerCase();
    var pos  = ltxt.indexOf(lterm);
    if (pos === -1) return;
    var frag   = document.createDocumentFragment();
    var cursor = 0;
    while (pos !== -1) {
      if (pos > cursor) frag.appendChild(document.createTextNode(text.slice(cursor, pos)));
      var mark = document.createElement('mark');
      mark.className = 'lr-find-mark';
      mark.textContent = text.slice(pos, pos + term.length);
      frag.appendChild(mark);
      marks.push(mark);
      cursor = pos + term.length;
      pos = ltxt.indexOf(lterm, cursor);
    }
    if (cursor < text.length) frag.appendChild(document.createTextNode(text.slice(cursor)));
    textNode.parentNode.replaceChild(frag, textNode);
  });
  return marks;
}

function _clearHighlights(el) {
  el.querySelectorAll('mark.lr-find-mark').forEach(function(m) {
    var parent = m.parentNode;
    if (parent) { parent.replaceChild(document.createTextNode(m.textContent), m); parent.normalize(); }
  });
}

/* ── Find bar wiring ─────────────────────────────────────────────────────── */

// header: the #lib-reader-header element (contains find bar UI; persists across renders)
// body:   the content element to search (same persistent DOM node; innerHTML changes per page)
// goToFn: null in scroll mode; the paginated goTo(idx) closure in paginated mode.
//         Stored as a module var so the wired listeners can always call the latest goTo.
var _findGoTo = null;

// INTENT: Step the active scroll-mode highlight to mark index i (wrapping), give it the
//   --current class, scroll it into view, and update the "x / N" counter. Paginated mode
//   steps whole sections instead (handled in the prev/next handlers), so this is scroll-only.
// CHANGE? Relies on _findMarks being repopulated by doSearch on each new search; if the
//   highlight class name lr-find-mark changes, update _highlightInEl/_clearHighlights too.
// VERIFY: Search a common word in a single-section doc, click ▼ repeatedly — the active
//   (orange) highlight advances through every match and the counter reads "2 / N", "3 / N"…
function _findGotoMark(i, result) {
  if (!_findMarks.length) return;
  var n = _findMarks.length;
  _findCurrMatch = (i % n + n) % n;
  _findMarks.forEach(function (m, j) { m.classList.toggle('lr-find-mark--current', j === _findCurrMatch); });
  _findMarks[_findCurrMatch].scrollIntoView({ behavior: 'smooth', block: 'center' });
  if (result) result.textContent = (_findCurrMatch + 1) + ' / ' + n;
}

function _wireFindBar(header, body, doc, goToFn) {
  var btn    = header.querySelector('#lr-find-btn');
  var bar    = header.querySelector('#lr-find-bar');
  var input  = header.querySelector('#lr-find-input');
  var submit = header.querySelector('#lr-find-submit');
  var prev   = header.querySelector('#lr-find-prev');
  var next   = header.querySelector('#lr-find-next');
  var result = header.querySelector('#lr-find-result');
  var close  = header.querySelector('#lr-find-close');
  if (!btn || !bar) return;

  // Keep the goTo reference current so the wired doSearch always uses the right closure
  _findGoTo = goToFn;

  // Toggle prev/next visibility for a given match count (≥2 to be useful)
  function showNav(total) {
    var on = total > 1;
    if (prev) prev.hidden = !on;
    if (next) next.hidden = !on;
  }

  // Restore search state after a paginated re-render (body innerHTML just changed)
  if (_findTerm) {
    input.value = _findTerm;
    bar.hidden  = false;
    var restored = _highlightInEl(body, _findTerm);
    _findMarks = restored;
    if (goToFn) {
      // Paginated: matches are counted by section; show position within _findMatchSecs.
      if (result && _findMatchSecs.length) {
        result.textContent = (_findCurrMatch + 1) + ' / ' + _findMatchSecs.length;
      }
      showNav(_findMatchSecs.length);
      if (restored.length) restored[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
      // Scroll: step through the in-page marks directly.
      showNav(restored.length);
      if (restored.length) _findGotoMark(0, result);
    }
  }

  // Header elements persist across paginated re-renders — only wire listeners once per document
  if (_findBarWired) return;
  _findBarWired = true;

  btn.addEventListener('click', function() {
    bar.hidden = !bar.hidden;
    if (!bar.hidden) { input.focus(); input.select(); }
  });

  close.addEventListener('click', function() {
    bar.hidden         = true;
    _findTerm          = '';
    _findMatchSecs     = [];
    _findMarks         = [];
    input.value        = '';
    result.textContent = '';
    showNav(0);
    _clearHighlights(body);
  });

  function doSearch() {
    var term = input.value.trim();
    _findTerm = term;
    _clearHighlights(body);
    _findMarks = [];
    if (!term) { result.textContent = ''; showNav(0); return; }

    if (_findGoTo) {
      // Paginated: search section strings, navigate to first matching section
      _findMatchSecs = [];
      _findCurrMatch = 0;
      doc.sections.forEach(function(s, i) {
        if (s.html.toLowerCase().indexOf(term.toLowerCase()) !== -1) _findMatchSecs.push(i);
      });
      if (!_findMatchSecs.length) { result.textContent = 'Not found'; showNav(0); return; }
      // _findGoTo re-renders content synchronously; the _wireFindBar restore handles highlight+counter+nav
      _findGoTo(_findMatchSecs[0]);
    } else {
      var marks = _highlightInEl(body, term);
      _findMarks = marks;
      if (!marks.length) { result.textContent = 'Not found'; showNav(0); return; }
      showNav(marks.length);
      _findGotoMark(0, result);
    }
  }

  // UX-19: step to the next/previous match. Scroll mode walks the in-page marks; paginated
  // mode advances the matching-section index and re-renders (restore re-highlights + recounts).
  function step(delta) {
    if (_findGoTo) {
      var n = _findMatchSecs.length;
      if (n < 2) return;
      _findCurrMatch = ((_findCurrMatch + delta) % n + n) % n;
      _findGoTo(_findMatchSecs[_findCurrMatch]);
    } else {
      if (_findMarks.length < 2) return;
      _findGotoMark(_findCurrMatch + delta, result);
    }
  }

  if (prev) prev.addEventListener('click', function() { step(-1); });
  if (next) next.addEventListener('click', function() { step(1); });

  submit.addEventListener('click', doSearch);
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      // Enter re-runs a new search; once a term is active, Enter steps to the next match
      // (Shift+Enter steps back) so repeated Enter cycles through results like a browser find.
      var active = _findTerm === input.value.trim() && (_findMarks.length || _findMatchSecs.length);
      if (!active)        doSearch();
      else if (e.shiftKey) step(-1);
      else                step(1);
    }
    if (e.key === 'Escape') { bar.hidden = true; }
  });
}

/* ── Scroll-spy with section counter ─────────────────────────────────────── */

function _wireScrollSpy(sections, tocLinks, counter) {
  var main = document.querySelector('.lr-main');
  if (!main || !sections.length || !tocLinks.length) return;

  function spy() {
    var top       = main.getBoundingClientRect().top;
    var threshold = top + 120;
    var activeHref = null;
    var activeIdx  = -1;
    sections.forEach(function(s, i) {
      if (s.getBoundingClientRect().top <= threshold) { activeHref = '#lrs-' + i; activeIdx = i; }
    });
    if (counter && activeIdx !== -1) {
      counter.textContent = '§ ' + (activeIdx + 1) + ' of ' + sections.length;
    }
    tocLinks.forEach(function(a) {
      var on = a.getAttribute('href') === activeHref;
      a.classList.toggle('lr-toc-active', on);
    });
  }

  document.addEventListener('scroll', spy, { passive: true });
  spy();
}

function _renderScroll(doc, docId, sections, content, entry) {
  var toc = document.getElementById('lib-reader-toc');
  var multiSection = sections.length > 1;
  if (toc) {
    if (multiSection) {
      var tocHtml = '<div class="lr-toc-heading">Contents</div><ul class="lr-toc-list">';
      sections.forEach(function(s, i) {
        tocHtml += '<li><a href="#lrs-' + i + '">' + escHtml(s.heading) + '</a></li>';
      });
      toc.innerHTML = tocHtml + '</ul>';
    } else {
      var sidebar = toc.closest('.lr-sidebar');
      if (sidebar) sidebar.hidden = true;
    }
  }

  var html = '';
  sections.forEach(function(s, i) {
    // Apply sub-pagination to long single sections in scroll mode
    var body = (sections.length === 1) ? _buildSectionBody(s, 0, 0) : s.html;
    html += '<section class="lr-section" id="lrs-' + i + '">' + body + '</section>';
  });
  html += _buildMarkRow(docId, doc, entry);
  content.innerHTML = html;
  wireRefLinks(content);
  autoTagRefs();
  autoTagTermsWhenReady(content);
  _wireMarkBtn(content, docId, doc, entry);

  // Wire sub-pager for single long-section docs
  if (sections.length === 1) _wireSubPager(content, sections[0], 0);

  var header = document.getElementById('lib-reader-header');
  if (header) _wireFindBar(header, content, doc, null);

  // Wire scroll-spy for TOC highlighting + section counter
  if (multiSection) {
    var sectionEls = content.querySelectorAll('.lr-section');
    var tocLinks   = toc ? toc.querySelectorAll('.lr-toc-list a') : [];
    var counter    = header ? header.querySelector('#lr-section-counter') : null;
    _wireScrollSpy(Array.prototype.slice.call(sectionEls), Array.prototype.slice.call(tocLinks), counter);
  }
}

function _renderPaged(doc, docId, sections, idx, content, entry) {
  _subPageState = null;   // clear until _wireSubPager sets it for the new section
  var total  = sections.length;
  var s      = sections[idx];
  var isLast = idx >= total - 1;
  var useTabBar = (total <= _TAB_BAR_MAX);

  // ── Build navigation UI ───────────────────────────────────────────────────
  var navHtml;
  if (useTabBar) {
    // Horizontal tab strip for small section counts
    var tabs = sections.map(function(sec, i) {
      var label = sec.heading || ('Section ' + (i + 1));
      // Abbreviate long headings in the tab
      if (label.length > 28) label = label.slice(0, 25) + '…';
      return '<button class="lr-tab' + (i === idx ? ' lr-tab--active' : '') + '" role="tab" aria-selected="' + (i === idx ? 'true' : 'false') + '" data-idx="' + i + '">' +
               escHtml(label) +
             '</button>';
    }).join('');
    navHtml =
      '<div class="lr-tab-bar" role="tablist" aria-label="Document sections">' + tabs + '</div>';
  } else {
    // Dropdown select for larger section counts
    var options = sections.map(function(sec, i) {
      return '<option value="' + i + '"' + (i === idx ? ' selected' : '') + '>' +
               escHtml(sec.heading || ('Section ' + (i + 1))) + '</option>';
    }).join('');
    navHtml =
      '<nav class="lr-pager" aria-label="Section navigation">' +
        '<button class="lr-pager-btn lr-pager-prev"' + (idx === 0 ? ' disabled' : '') + '>&#8592;</button>' +
        '<select class="lr-pager-select" aria-label="Jump to section">' + options + '</select>' +
        '<button class="lr-pager-btn lr-pager-next"' + (isLast ? ' disabled' : '') + '>&#8594;</button>' +
        '<span class="lr-pager-of">' + (idx + 1) + ' / ' + total + '</span>' +
      '</nav>';
  }

  // ── Build section HTML with optional sub-pagination ───────────────────────
  var sectionBody = _buildSectionBody(s, idx, 0);

  // Tab bar shows heading in the tab; dropdown mode shows full heading below
  var progressHtml = useTabBar
    ? '<div class="lr-pager-progress"><span class="lr-pager-pos">' + (idx + 1) + ' / ' + total + '</span></div>'
    : '<div class="lr-pager-progress">' + (s.heading ? '<span class="lr-pager-heading">' + escHtml(s.heading) + '</span>' : '') + '</div>';

  content.innerHTML =
    navHtml +
    progressHtml +
    '<section class="lr-section" id="lrs-0">' + sectionBody + '</section>' +
    (isLast ? _buildMarkRow(docId, doc, entry) : '');

  window.scrollTo(0, 0);

  // ── goTo: navigate to section index ──────────────────────────────────────
  function goTo(newIdx) {
    newIdx = Math.max(0, Math.min(newIdx, total - 1));
    _savePos(docId, newIdx);
    var p = new URLSearchParams(window.location.search);
    p.set('doc', docId);
    if (newIdx > 0) { p.set('section', String(newIdx)); } else { p.delete('section'); }
    history.replaceState(null, '', '?' + p.toString());
    _renderPaged(doc, docId, sections, newIdx, content, entry);
  }

  // Wire tab bar buttons
  content.querySelectorAll('.lr-tab').forEach(function(btn) {
    btn.addEventListener('click', function() { goTo(parseInt(btn.dataset.idx, 10)); });
  });

  // Wire dropdown
  var sel = content.querySelector('.lr-pager-select');
  if (sel) sel.addEventListener('change', function() { goTo(parseInt(sel.value, 10)); });

  // Wire prev/next
  var prevBtn = content.querySelector('.lr-pager-prev');
  var nextBtn = content.querySelector('.lr-pager-next');
  if (prevBtn) prevBtn.addEventListener('click', function() { goTo(idx - 1); });
  if (nextBtn) nextBtn.addEventListener('click', function() { goTo(idx + 1); });

  // Wire sub-pager within section (if present)
  _wireSubPager(content, s, idx);

  // Arrow-key navigation: sub-pages (chapters) take priority over section (book) nav
  if (_keyListener) document.removeEventListener('keydown', _keyListener);
  _keyListener = function(e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (e.target && e.target.matches('input, select, textarea, [contenteditable]')) return;
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    e.preventDefault();

    var sp = _subPageState;
    if (sp && sp.total > 1) {
      // Navigate chapters within the current section
      if (e.key === 'ArrowLeft') {
        if (sp.current > 0)          { sp.goTo(sp.current - 1); }
        else                          { goTo(idx - 1); }          // beginning of section → prev section
      } else {
        if (sp.current < sp.total - 1) { sp.goTo(sp.current + 1); }
        else                            { goTo(idx + 1); }        // end of section → next section
      }
    } else {
      // No active sub-pages — navigate sections directly
      if (e.key === 'ArrowLeft')  goTo(idx - 1);
      else                        goTo(idx + 1);
    }
  };
  document.addEventListener('keydown', _keyListener);

  wireRefLinks(content);
  autoTagRefs();
  autoTagTermsWhenReady(content);
  if (isLast) _wireMarkBtn(content, docId, doc, entry);

  var header = document.getElementById('lib-reader-header');
  if (header) _wireFindBar(header, content, doc, goTo);
}

/* ── Sub-pagination for very long sections ──────────────────────────────────── */

var _BLOCK_TAGS = { P:1, BLOCKQUOTE:1, H3:1, H4:1, UL:1, OL:1, TABLE:1, H2:1 };

// Collect groups of elements split at h3 boundaries.
// Each group = [h3, ...following siblings up to next h3].
// Pre-h3 content (if any) becomes group 0 with label null.
function _splitAtH3(wrap) {
  var groups  = [];   // [{label, els}]
  var current = { label: null, els: [] };

  Array.prototype.forEach.call(wrap.children, function(el) {
    if (el.tagName === 'H3') {
      if (current.els.length || current.label !== null) groups.push(current);
      current = { label: el.textContent.trim(), els: [el] };
    } else {
      current.els.push(el);
    }
  });
  if (current.els.length || current.label !== null) groups.push(current);
  return groups;
}

function _buildSubPagerHtml(secIdx, subPage, numPages, label) {
  var pos = label
    ? escHtml(label) + ' <span class="lr-subpager-count">(' + (subPage + 1) + '/' + numPages + ')</span>'
    : 'Page ' + (subPage + 1) + ' of ' + numPages;
  return '<div class="lr-subpager" data-sec="' + secIdx + '" data-pages="' + numPages + '" data-current="' + subPage + '">' +
    '<button class="lr-subpager-btn lr-subpager-prev"' + (subPage === 0 ? ' disabled' : '') + '>&#8592;</button>' +
    '<span class="lr-subpager-pos">' + pos + '</span>' +
    '<button class="lr-subpager-btn lr-subpager-next"' + (subPage >= numPages - 1 ? ' disabled' : '') + '>&#8594;</button>' +
  '</div>';
}

function _buildSectionBody(section, secIdx, subPage) {
  var wrap = document.createElement('div');
  wrap.innerHTML = section.html || '';

  // Strip the leading title h2 — heading is shown in tab/progress bar
  var first = wrap.firstElementChild;
  if (first && first.tagName === 'H2') {
    var cls = first.className || '';
    if (cls.indexOf('lib-section__title') !== -1 || cls.indexOf('lib-chapter__title') !== -1 ||
        first.textContent.trim() === (section.heading || '').trim()) {
      first.remove();
    }
  }

  // Prefer splitting at h3 chapter headings when present
  var hasH3 = !!wrap.querySelector(':scope > h3');
  if (hasH3) {
    var groups   = _splitAtH3(wrap);
    var numPages = groups.length;
    if (numPages <= 1) return wrap.innerHTML;
    subPage = Math.max(0, Math.min(subPage, numPages - 1));
    var group    = groups[subPage];
    var fragHtml = group.els.map(function(el) { return el.outerHTML; }).join('');
    var pager    = _buildSubPagerHtml(secIdx, subPage, numPages, group.label);
    return pager + fragHtml + pager;
  }

  // Fallback: split at every _SUBPAGE_SIZE block elements
  var allParas = Array.prototype.filter.call(wrap.children, function(el) {
    return _BLOCK_TAGS[el.tagName];
  });
  var total = allParas.length;
  if (total <= _SUBPAGE_SIZE) return wrap.innerHTML;

  var numPages2 = Math.ceil(total / _SUBPAGE_SIZE);
  subPage = Math.max(0, Math.min(subPage, numPages2 - 1));
  var start = subPage * _SUBPAGE_SIZE;
  var end   = Math.min(start + _SUBPAGE_SIZE, total);
  var fragHtml2 = '';
  for (var i = start; i < end; i++) fragHtml2 += allParas[i].outerHTML;
  var pager2 = _buildSubPagerHtml(secIdx, subPage, numPages2, null);
  return pager2 + fragHtml2 + pager2;
}

function _wireSubPager(container, section, secIdx) {
  // Reset state — will be set below if sub-pages exist
  _subPageState = null;

  var sp = container.querySelector('.lr-subpager');
  if (!sp) return;

  var numPages = parseInt(sp.dataset.pages, 10);
  var current  = parseInt(sp.dataset.current, 10);
  if (numPages <= 1) return;

  function goSubPage(newPage) {
    newPage = Math.max(0, Math.min(newPage, numPages - 1));
    var secEl = container.querySelector('.lr-section');
    if (secEl) {
      secEl.innerHTML = _buildSectionBody(section, secIdx, newPage);
      wireRefLinks(secEl);
      autoTagRefs();
      autoTagTermsWhenReady(secEl);
      _wireSubPager(container, section, secIdx);   // updates _subPageState with new current
      secEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  // Register in module state so the arrow-key listener can call this
  _subPageState = { goTo: goSubPage, current: current, total: numPages };

  // Wire all sub-pager instances in the container (top + bottom)
  container.querySelectorAll('.lr-subpager').forEach(function(el) {
    var prev = el.querySelector('.lr-subpager-prev');
    var next = el.querySelector('.lr-subpager-next');
    if (prev) prev.addEventListener('click', function() { goSubPage(current - 1); });
    if (next) next.addEventListener('click', function() { goSubPage(current + 1); });
  });
}

var _LIB_PROGRESS_KEY  = 'bsw_lib_progress';
var _LIB_COMPLETE_KEY  = 'bsw_lib_complete';

// INTENT: Record this doc as recently-read in `bsw_lib_progress` (capped at 10 entries,
//   oldest evicted) so `library/progress/` can show a reading history widget.
// CHANGE? `lib-progress.js` reads `bsw_lib_progress` via `_LIB_PROGRESS_KEY`; both keys
//   and the `{ title, href, lastRead, totalSections, tradition }` object shape must stay in sync.
// VERIFY: Read any library doc, open `library/progress/` → the doc should appear in "Recently Read".
function _saveLibProgress(docId, title, sectionCount, tradition) {
  try {
    var data  = JSON.parse(localStorage.getItem(_LIB_PROGRESS_KEY) || '{}');
    var today = new Date().toISOString().slice(0, 10);
    data[docId] = { title: title, href: location.href, lastRead: today, totalSections: sectionCount || 0, tradition: tradition || '' };
    var keys = Object.keys(data);
    if (keys.length > 10) {
      keys.sort(function(a, b) { return data[a].lastRead < data[b].lastRead ? -1 : 1; });
      delete data[keys[0]];
    }
    localStorage.setItem(_LIB_PROGRESS_KEY, JSON.stringify(data));
  } catch(e) { /* non-fatal */ }
}

/* ── Mark as complete (LR-A) ──────────────────────────────────────────────── */

var _TRAD_DISPLAY = {
  patristic: 'Church Fathers', reformed: 'Reformed', lutheran: 'Lutheran',
  anglican: 'Anglican', baptist: 'Baptist', orthodox: 'Orthodox',
  'roman-catholic': 'Roman Catholic', methodist: 'Methodist', ecumenical: 'Ecumenical'
};

var _TRAD_GAP_ORDER = ['orthodox', 'patristic', 'reformed', 'lutheran', 'roman-catholic', 'anglican', 'baptist'];

function _traditionNote(tradition, log, allTrads) {
  var keys = Object.keys(log);
  if (!keys.length) return 'Your first completed work — well done.';
  var tradCounts = {};
  keys.forEach(function(k) { var t = log[k].tradition || ''; tradCounts[t] = (tradCounts[t] || 0) + 1; });
  var count = tradCounts[tradition] || 0;
  var tradLabel = _TRAD_DISPLAY[tradition] || tradition;
  if (!count) return 'First ' + tradLabel + ' work you\'ve finished.';
  if (count < 3) return 'Growing in ' + tradLabel + ' reading.';
  // Find first tradition with 0 completions, in gap priority order
  var gap = null;
  for (var i = 0; i < _TRAD_GAP_ORDER.length; i++) {
    if (_TRAD_GAP_ORDER[i] !== tradition && !(tradCounts[_TRAD_GAP_ORDER[i]])) { gap = _TRAD_GAP_ORDER[i]; break; }
  }
  if (gap) return 'Strong ' + tradLabel + ' foundation — consider exploring ' + (_TRAD_DISPLAY[gap] || gap) + ' next.';
  return 'Growing in ' + tradLabel + ' reading.';
}

// INTENT: Write a completion record to `bsw_lib_complete` when the user clicks "Mark as Complete".
//   Returns today's ISO date string on success, null on failure; the return value is used by the
//   caller to update the UI without re-reading localStorage.
// CHANGE? `lib-progress.js` reads `bsw_lib_complete` via `_LIB_COMPLETE_KEY`; the entry shape
//   `{ title, author, tradition, completedDate, type }` must match the rendering in lib-progress.js.
// VERIFY: Click "Mark as Complete" on any library doc → open `library/progress/` →
//   the doc appears in the completion log with today's date and the correct tradition chip.
function _markDocComplete(docId, doc, entry) {
  try {
    var log   = JSON.parse(localStorage.getItem(_LIB_COMPLETE_KEY) || '{}');
    var today = new Date().toISOString().slice(0, 10);
    log[docId] = {
      title:         doc.title,
      author:        (entry && entry.author) || '',
      tradition:     (entry && entry.tradition) || '',
      completedDate: today,
      type:          (entry && entry.type) || ''
    };
    localStorage.setItem(_LIB_COMPLETE_KEY, JSON.stringify(log));
    return today;
  } catch(e) { return null; }
}

function _isDocComplete(docId) {
  try {
    var log = JSON.parse(localStorage.getItem(_LIB_COMPLETE_KEY) || '{}');
    return log[docId] ? log[docId].completedDate : null;
  } catch(e) { return null; }
}

function _buildMarkRow(docId, doc, entry) {
  var completedDate = _isDocComplete(docId);
  var tradition     = (entry && entry.tradition) || '';
  try {
    var log  = JSON.parse(localStorage.getItem(_LIB_COMPLETE_KEY) || '{}');
    var note = _traditionNote(tradition, log);
  } catch(e) { note = ''; }

  var btnHtml = completedDate
    ? '<button class="lib-mark-btn lib-mark-btn--done" disabled>✓ Completed ' + completedDate + '</button>'
    : '<button class="lib-mark-btn" data-doc-id="' + docId + '">Mark as read ✓</button>';

  return '<div class="lib-mark-row">' + btnHtml + (note ? '<p class="lib-mark-note">' + note + '</p>' : '') + '</div>';
}

function _wireMarkBtn(container, docId, doc, entry) {
  var btn = container.querySelector('.lib-mark-btn:not(.lib-mark-btn--done)');
  if (!btn) return;
  btn.addEventListener('click', function() {
    var date = _markDocComplete(docId, doc, entry);
    btn.textContent   = '✓ Completed ' + (date || '');
    btn.disabled      = true;
    btn.classList.add('lib-mark-btn--done');
    // Update encouragement note
    try {
      var log  = JSON.parse(localStorage.getItem(_LIB_COMPLETE_KEY) || '{}');
      var note = _traditionNote((entry && entry.tradition) || '', log);
      var noteEl = container.querySelector('.lib-mark-note');
      if (noteEl) noteEl.textContent = note;
      else if (note) { var p = document.createElement('p'); p.className = 'lib-mark-note'; p.textContent = note; btn.parentNode.appendChild(p); }
    } catch(e) {}
  });
}

function _sectionLabel(type, n) {
  if (type === 'catechism') return n === 1 ? 'Question' : 'Questions';
  if (type === 'father')    return n === 1 ? 'Selection' : 'Selections';
  return n === 1 ? 'Section' : 'Chapters';
}
