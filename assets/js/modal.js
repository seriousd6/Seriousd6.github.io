/* modal.js — Verse viewer modal, cross-reference panels, share/copy, shortcuts */
'use strict';

import {
  getVersion, resolveVerses, loadCrossRefs, loadCommentary,
  parseCrossRefEntry, _compareCanonical, parseRef,
  escHtml, READER_URL, VERSE_STUDY_URL, COMPARE_URL,
  COMMENTARY_SOURCES, getCommentarySource, setCommentarySource, decorateCatena, buildCatenaFilter, loadMktAll, decorateMkt,
  ATTRIBUTION, metaVersions, metaBooks,
  registerOpenModal, _resolve, NOTES_URL
} from './core.js';
import {
  getNotes, getNote, saveNote, toggleHighlight, getTags, addTag, removeTag,
  _HL_COLORS, createNoteV2, updateNoteV2, deleteNoteV2,
  getNotesForVerse, _noteRelTime, _historyPush, _recordReadingDay
} from './storage.js';
import { wireRefEl, wireRefLinks, applyHighlights, applyModalHighlights } from './wire.js';

var _backdropEl  = null;
var _modalEl     = null;
var _lastFocused = null;
var _lastTab     = 'verse'; // VM-F: persists last active tab within session

// ── Cross-reference tab constants ─────────────────────────────────────────
var XREF_CHAPTER_LIMIT = 5;

// ── Connections tab (biblepedia badges) ───────────────────────────────────
// The Connections tab replaces the old Topics tab: it surfaces the Biblepedia
// articles whose key_refs land on the open reference, as clickable badges. Data
// comes from the shared encyclopedia index (same file the reader study desk uses).
// The index is ~1.7MB so it's fetched once on first activation and cached for the
// page session; per-verse matching is cheap once it's in memory.
var _BP_INDEX_URL = new URL('../../data/biblepedia/index.json', import.meta.url).href;
var _BP_PAGE_URL  = new URL('../../biblepedia/', import.meta.url).href;   // article reader (?a=slug)
var _bpIndexCache = null;
function _loadBPIndex() {
  if (_bpIndexCache) return Promise.resolve(_bpIndexCache);
  return fetch(_BP_INDEX_URL).then(function (r) { return r.ok ? r.json() : []; })
    .then(function (d) { _bpIndexCache = Array.isArray(d) ? d : []; return _bpIndexCache; })
    .catch(function () { _bpIndexCache = []; return _bpIndexCache; });
}
// True when the parsed reference `p` (a key_ref, which may itself be a verse range or span
// chapters) overlaps the passage `parsed` is showing. Compares (chapter, verse) pairs
// lexicographically: two ranges overlap when each starts no later than the other ends.
function _refInParsed(p, parsed) {
  if (!p || p.bookId !== parsed.bookId) return false;
  function cmp(c1, v1, c2, v2) { return c1 !== c2 ? c1 - c2 : v1 - v2; }
  var aSc = p.ch, aSv = p.v, aEc = p.endCh || p.ch, aEv = p.endV || p.v;
  var bSc = parsed.ch, bSv = parsed.wholeChapter ? 1 : parsed.v;
  var bEc = parsed.endCh || parsed.ch, bEv = parsed.wholeChapter ? 9999 : parsed.endV;
  return cmp(aSc, aSv, bEc, bEv) <= 0 && cmp(bSc, bSv, aEc, aEv) <= 0;
}

// ── Memory helpers (bridged from daily.js via registration) ───────────────
var _memHasFn     = null;
var _memAddFn     = null;
var _memRemoveFn  = null;
var _memRefreshFn = null;
// CHANGE? Called by app.js after importing daily.js (which provides the four functions).
//   If this registration call is removed from app.js, the Memorize tab in the verse modal
//   renders empty with no error — the add/remove/refresh helpers are just silently null.
//   If daily.js renames any of the four exported functions, update the app.js call site.
export function registerMemHelpers(hasFn, addFn, removeFn, refreshFn) {
  _memHasFn = hasFn; _memAddFn = addFn; _memRemoveFn = removeFn; _memRefreshFn = refreshFn;
}

// ── Term-tagging bridge (from wire.js) ───────────────────────────────────
var _autoTagTermsFn = null;
var _termMap2Ref    = null;
export function registerAutoTagTerms(fn, termMap2Ref) {
  _autoTagTermsFn  = fn;
  _termMap2Ref     = termMap2Ref;
}
function _maybeAutoTag(el) {
  if (_autoTagTermsFn && _termMap2Ref && _termMap2Ref()) {
    el._termsTagged = false;
    _autoTagTermsFn(el);
  }
}

// ── Word study + confessions/fathers/topics/dictionary bridges ────────────
var _renderModalWordStudyFn  = null;
var _renderModalTopicsFn     = null;
var _renderModalConfessionsFn = null;
var _renderModalFathersFn    = null;
var _renderModalDictionaryFn = null;

// CHANGE? All five register* functions below are called by app.js after the relevant
//   modules are imported (verse-study.js for word study, daily.js for topics/confessions/
//   fathers/dictionary). If any registration is skipped, that modal tab silently renders
//   empty — no error is thrown. If a module's render function is renamed, update both the
//   app.js import and the corresponding registerModal* call here.
export function registerModalWordStudy(fn)     { _renderModalWordStudyFn   = fn; }
export function registerModalTopics(fn)        { _renderModalTopicsFn      = fn; }
export function registerModalConfessions(fn)   { _renderModalConfessionsFn = fn; }
export function registerModalFathers(fn)       { _renderModalFathersFn     = fn; }
export function registerModalDictionary(fn)    { _renderModalDictionaryFn  = fn; }

// ── Commentary source state ───────────────────────────────────────────────
// Reads are always fresh via getCommentarySource() (see core.js) so that changes
// made on the verse-study page are visible here without a page reload.

export function _commAttr(source) {
  // INTENT: Returns attribution HTML for the given commentary source ID.
  //   AI-assisted sources (isAI: true) get a .src-badge--ai chip linking to /about/;
  //   public-domain sources get plain italic text. HTML output is safe because all
  //   content comes from the hardcoded COMMENTARY_SOURCES array, never user input.
  // CHANGE? If COMMENTARY_SOURCES moves to core.js or isAI semantics change, update here.
  // VERIFY: Select "MKT Commentary" in verse study — attribution shows gold AI badge.
  var s = COMMENTARY_SOURCES.filter(function (x) { return x.id === source; })[0];
  if (!s) return source;
  if (s.isAI) {
    return '<span class="src-badge src-badge--ai">' + s.label +
           ' · AI-assisted · <a href="/about/">methods &amp; prompts</a></span>';
  }
  return s.attr;
}

// ── buildModalDOM ─────────────────────────────────────────────────────────
// INTENT: Creates the single global #bsw-modal-backdrop / #bsw-modal DOM tree and
//   caches references in module-level _backdropEl / _modalEl. Idempotent — if the
//   backdrop already exists (e.g. buildModalDOM called twice, or the page pre-renders it),
//   it just re-reads the existing elements and returns. All modal state (_lastTab,
//   _lastFocused, registered helpers) is module-level and persists across open/close
//   cycles for the lifetime of the page session — closing the modal does not reset them.
// CHANGE? If the modal's HTML structure changes (IDs, class names, or child elements),
//   also audit openModal, closeModal, and every _renderModal* function that calls
//   _modalEl.querySelector(...) directly — they all rely on this DOM shape.
export function buildModalDOM() {
  if (document.getElementById('bsw-modal-backdrop')) {
    _backdropEl = document.getElementById('bsw-modal-backdrop');
    _modalEl    = document.getElementById('bsw-modal');
    return;
  }

  var backdrop = document.createElement('div');
  backdrop.id        = 'bsw-modal-backdrop';
  backdrop.className = 'bsw-modal-backdrop bsw-modal-backdrop--hidden';
  backdrop.setAttribute('aria-hidden', 'true');

  var modal = document.createElement('div');
  modal.id = 'bsw-modal';
  modal.className = 'bsw-modal';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.setAttribute('aria-labelledby', 'bsw-modal-title');
  modal.innerHTML =
    '<div class="bsw-modal__header">' +
      '<h2 class="bsw-modal__title" id="bsw-modal-title"></h2>' +
      '<a class="bsw-modal__read-ch" href="#">Read chapter</a>' +
      '<a class="bsw-modal__verse-study-link" href="#" hidden>📖 Study this verse</a>' +
      '<a class="bsw-modal__compare-link" href="#" hidden>All translations ↗</a>' +
      '<button class="bsw-modal__memory-btn" hidden aria-label="Add to memory">☆ Memorize</button>' +
      '<button class="bsw-modal__share-btn" hidden aria-label="Share verse as image">Share</button>' +
      '<button class="bsw-modal__close" aria-label="Close verse viewer">✕</button>' +
    '</div>' +
    '<div class="bsw-modal__version-bar">' +
      '<label for="bsw-modal-version">Version:</label>' +
      '<select id="bsw-modal-version"></select>' +
    '</div>' +
    '<div class="bsw-modal__tabs" role="tablist">' +
      '<button class="bsw-modal__tab bsw-modal__tab--active" data-tab="verse" role="tab" aria-selected="true">Verse</button>' +
      '<button class="bsw-modal__tab" data-tab="notes" role="tab" aria-selected="false">Notes</button>' +
      '<button class="bsw-modal__tab" data-tab="connections" role="tab" aria-selected="false">Connections</button>' +
    '</div>' +
    '<div class="bsw-modal__split">' +
      '<button class="bsw-modal__prev-verse" hidden aria-label="Previous verse" title="Previous verse (k)">‹</button>' +
      '<div class="bsw-modal__verse-col">' +
        '<div class="bsw-modal__body" aria-live="polite"></div>' +
        '<div class="bsw-modal__attribution"></div>' +
      '</div>' +
      '<button class="bsw-modal__next-verse" hidden aria-label="Next verse" title="Next verse (j)">›</button>' +
    '</div>' +
    '<div class="bsw-modal__notes-panel" hidden></div>' +
    '<div class="bsw-modal__connections-panel" hidden></div>';

  backdrop.appendChild(modal);
  document.body.appendChild(backdrop);

  _backdropEl = backdrop;
  _modalEl    = modal;

  modal.querySelector('.bsw-modal__close').addEventListener('click', hideModal);
  modal.querySelector('.bsw-modal__memory-btn').addEventListener('click', function () {
    var ref = this._memRef;
    if (!ref) return;
    if (_memHasFn && _memHasFn(ref)) {
      if (_memRemoveFn) _memRemoveFn(ref);
    } else {
      if (_memAddFn) _memAddFn(ref);
    }
    if (_memRefreshFn) _memRefreshFn(ref);
  });
  backdrop.addEventListener('click', function (e) {
    if (e.target === backdrop) hideModal();
  });
  // Prevent iOS scroll-behind: block touchmove on the backdrop itself (not on modal content)
  backdrop.addEventListener('touchmove', function (e) {
    if (!_modalEl || !_modalEl.contains(e.target)) e.preventDefault();
  }, { passive: false });

  // VM-M2: swipe-down-to-dismiss on mobile bottom sheet
  var _swipeStartY = 0, _swipeDelta = 0, _activePanel = null;
  modal.addEventListener('touchstart', function (e) {
    if (window.innerWidth > 767) return;
    _swipeStartY = e.touches[0].clientY;
    _swipeDelta  = 0;
    _activePanel = modal.querySelector('[class*="-panel"]:not([hidden])') ||
                   modal.querySelector('.bsw-modal__verse-col');
    modal.style.transition = 'none';
  }, { passive: true });
  modal.addEventListener('touchmove', function (e) {
    if (window.innerWidth > 767) return;
    _swipeDelta = e.touches[0].clientY - _swipeStartY;
    if (_swipeDelta > 0 && (!_activePanel || _activePanel.scrollTop === 0))
      modal.style.transform = 'translateY(' + _swipeDelta + 'px)';
  }, { passive: true });
  modal.addEventListener('touchend', function () {
    if (window.innerWidth > 767) return;
    modal.style.transition = '';
    modal.style.transform  = '';
    if (_swipeDelta > 100) hideModal();
  });

  modal.querySelector('#bsw-modal-version').addEventListener('change', function () {
    var ref = _modalEl._parsedRef;
    if (ref) renderModal(ref, this.value);
  });
  modal.querySelector('.bsw-modal__share-btn').addEventListener('click', function () {
    _shareModalVerseAsImage();
  });
  // VM-I: prev/next verse navigation
  modal.querySelector('.bsw-modal__prev-verse').addEventListener('click', function () {
    var ref = _modalEl && _modalEl._parsedRef;
    if (ref && ref.v > 1) openModal(parseRef(ref.bookName + ' ' + ref.ch + ':' + (ref.v - 1)));
  });
  modal.querySelector('.bsw-modal__next-verse').addEventListener('click', function () {
    var ref  = _modalEl && _modalEl._parsedRef;
    var maxV = _modalEl && _modalEl._chapterMaxV;
    if (ref && (!maxV || ref.v < maxV)) openModal(parseRef(ref.bookName + ' ' + ref.ch + ':' + (ref.v + 1)));
  });
  // VM-M2: swipe-down-to-dismiss gesture
  var _swipeStartY = 0, _swipeDelta = 0, _activePanel = null;
  modal.addEventListener('touchstart', function (e) {
    if (window.innerWidth > 767) return;
    _swipeStartY = e.touches[0].clientY;
    _swipeDelta  = 0;
    _activePanel = modal.querySelector('[class*="-panel"]:not([hidden])') ||
                   modal.querySelector('.bsw-modal__verse-col');
    modal.style.transition = 'none';
  }, { passive: true });
  modal.addEventListener('touchmove', function (e) {
    if (window.innerWidth > 767) return;
    _swipeDelta = e.touches[0].clientY - _swipeStartY;
    if (_swipeDelta > 0 && (!_activePanel || _activePanel.scrollTop === 0))
      modal.style.transform = 'translateY(' + _swipeDelta + 'px)';
  }, { passive: true });
  modal.addEventListener('touchend', function () {
    modal.style.transition = '';
    modal.style.transform  = '';
    if (_swipeDelta > 100) hideModal();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' &&
        _backdropEl && !_backdropEl.classList.contains('bsw-modal-backdrop--hidden')) {
      hideModal();
    }
    // VM-I: j/k navigate verses when modal is open
    if (_backdropEl && !_backdropEl.classList.contains('bsw-modal-backdrop--hidden')) {
      var tag = document.activeElement && document.activeElement.tagName;
      if (tag === 'TEXTAREA' || tag === 'INPUT' || tag === 'SELECT') return;
      var ref = _modalEl && _modalEl._parsedRef;
      var isSingle = ref && !ref.wholeChapter && ref.ch === ref.endCh && ref.v === ref.endV;
      if (!isSingle || !ref) return;
      if (e.key === 'j' || e.key === 'ArrowRight') {
        var maxV = _modalEl && _modalEl._chapterMaxV;
        if (!maxV || ref.v < maxV) { e.preventDefault(); openModal(parseRef(ref.bookName + ' ' + ref.ch + ':' + (ref.v + 1))); }
      } else if (e.key === 'k' || e.key === 'ArrowLeft') {
        if (ref.v > 1) { e.preventDefault(); openModal(parseRef(ref.bookName + ' ' + ref.ch + ':' + (ref.v - 1))); }
      }
    }
  });

  // Tab switching
  modal.querySelector('.bsw-modal__tabs').addEventListener('click', function (e) {
    var btn = e.target.closest('.bsw-modal__tab');
    if (!btn) return;
    var tab = btn.getAttribute('data-tab');
    _lastTab = tab; // VM-F: remember last tab within session
    modal.querySelectorAll('.bsw-modal__tab').forEach(function (b) {
      var active = b === btn;
      b.classList.toggle('bsw-modal__tab--active', active);
      b.setAttribute('aria-selected', active ? 'true' : 'false');
    });
    var splitEl  = modal.querySelector('.bsw-modal__split');
    var notesEl  = modal.querySelector('.bsw-modal__notes-panel');
    var connEl   = modal.querySelector('.bsw-modal__connections-panel');
    [splitEl, notesEl, connEl].forEach(function (p) { if (p) p.setAttribute('hidden', ''); });

    if (tab === 'verse') {
      if (splitEl) splitEl.removeAttribute('hidden');
    } else if (tab === 'notes') {
      if (notesEl) { notesEl.removeAttribute('hidden'); _renderNotesPanel(_modalEl._parsedRef, notesEl); }
    } else if (tab === 'connections') {
      if (connEl) { connEl.removeAttribute('hidden'); if (!connEl._connLoaded) _renderConnectionsPanel(_modalEl._parsedRef, connEl); }
    }
  });
}

// ── syncModalVersionPicker ────────────────────────────────────────────────
export function syncModalVersionPicker() {
  var sel = document.getElementById('bsw-modal-version');
  if (!sel || !metaVersions) return;
  if (sel.options.length > 0) return;  // already populated
  var current = getVersion();
  sel.innerHTML = '';
  metaVersions.forEach(function (v) {
    if (v.stub) return;  // no data files — would 404 on every book load
    var opt = document.createElement('option');
    opt.value       = v.id;
    opt.textContent = v.id + ' — ' + v.name;
    opt.title       = v.name;
    sel.appendChild(opt);
  });
  sel.value = current;
  if (!sel.value) sel.selectedIndex = 0;
}

// INTENT: Show the verse modal for `parsed`, focus the close button, and lock page scroll.
//   Builds the modal DOM on first call, syncs the version picker, and registers trapFocus.
// CHANGE? `document.documentElement.classList.add('bsw-modal-open')` suppresses body scroll;
//   this must be reversed in `hideModal()` or the page stays locked after modal closes.
//   Callers: `wire.js` → `.ref` link click; `reader.js` verse click; `verse-study.js` cross-link.
// VERIFY: Click any `.ref` link → modal opens, focus lands on close button, background
//   scroll is suppressed; press Escape → modal closes and focus returns to trigger element.
// ── openModal ─────────────────────────────────────────────────────────────
export function openModal(parsed) {
  if (!_modalEl || !_backdropEl) buildModalDOM();
  _lastFocused = document.activeElement;

  syncModalVersionPicker();

  _backdropEl.classList.remove('bsw-modal-backdrop--hidden');
  _backdropEl.setAttribute('aria-hidden', 'false');

  var versionSel = document.getElementById('bsw-modal-version');
  var version    = (versionSel && versionSel.value) ? versionSel.value : getVersion();

  renderModal(parsed, version).then(function () {
    var closeBtn = _modalEl.querySelector('.bsw-modal__close');
    if (closeBtn) closeBtn.focus();
  });

  _modalEl.addEventListener('keydown', trapFocus);
  document.documentElement.classList.add('bsw-modal-open');
  document.body.classList.add('bsw-modal-open');
}

// INTENT: Primary render dispatcher — fetches verse text, fires all 5 registered render
//   functions (verse text, cross-refs, notes, commentary, attribution), and sets shared modal
//   state (`_modalEl._parsedRef`, `_modalEl._chapterMaxV`) used by tab-switching and prev/next nav.
// CHANGE? Each render function is registered via `registerModalRenderer` in `core.js` — adding
//   a new panel requires a registration there; order of registration is render order.
//   `_modalEl._chapterMaxV` is set by `resolveVerses` and read by modal nav prev/next arrows.
// VERIFY: Open John 3:16 → verse text, cross-ref count badge, and commentary tab all populate;
//   switch version → `renderModal` re-fires with new versionId; prev/next chapter arrows work.
// ── renderModal ───────────────────────────────────────────────────────────
export function renderModal(parsed, versionId) {
  _modalEl._parsedRef    = parsed;
  _modalEl._chapterMaxV  = null; // reset until resolveVerses resolves

  var bodyEl  = _modalEl.querySelector('.bsw-modal__body');
  var attrElR = _modalEl.querySelector('.bsw-modal__attribution');
  _modalEl.querySelectorAll('.bsw-modal__tab').forEach(function (b) {
    var isVerse = b.getAttribute('data-tab') === 'verse';
    b.classList.toggle('bsw-modal__tab--active', isVerse);
    b.setAttribute('aria-selected', isVerse ? 'true' : 'false');
  });
  _refreshModalNotesBadge(parsed);

  var splitEl = _modalEl.querySelector('.bsw-modal__split');
  var notesEl = _modalEl.querySelector('.bsw-modal__notes-panel');
  var connResetEl = _modalEl.querySelector('.bsw-modal__connections-panel');
  if (bodyEl)  bodyEl.removeAttribute('hidden');
  if (attrElR) attrElR.removeAttribute('hidden');
  if (splitEl) splitEl.removeAttribute('hidden');
  if (notesEl) { notesEl.setAttribute('hidden', ''); notesEl.innerHTML = ''; }
  // Connections (biblepedia badges) reload per verse — drop the cached flag so the
  // next activation re-matches against the new reference.
  if (connResetEl) { connResetEl.setAttribute('hidden', ''); connResetEl._connLoaded = false; }

  var title  = _modalEl.querySelector('.bsw-modal__title');
  var body   = _modalEl.querySelector('.bsw-modal__body');
  var attr   = _modalEl.querySelector('.bsw-modal__attribution');
  var vSel   = document.getElementById('bsw-modal-version');

  title.textContent = parsed.display;
  if (vSel) vSel.value = versionId;
  body.innerHTML = '<div class="bsw-modal__loading">Loading…</div>';
  attr.textContent = '';

  var readCh = _modalEl.querySelector('.bsw-modal__read-ch');
  if (readCh) {
    if (parsed.wholeChapter && parsed.endCh !== parsed.ch) {
      readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
      readCh.textContent = 'Open in Reader ↗';
    } else {
      readCh.href = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch);
      readCh.textContent = 'Read chapter ↗';
    }
  }

  var vsLink  = _modalEl.querySelector('.bsw-modal__verse-study-link');
  var cmpLink = _modalEl.querySelector('.bsw-modal__compare-link');
  var isSingleVerse = !parsed.wholeChapter && parsed.ch === parsed.endCh && parsed.v === parsed.endV;
  var singleRef = encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + parsed.v);
  if (vsLink) {
    // "Study this verse" now opens the passage in the reader with the study desk and the
    // inline study modes (commentary, interlinear, parallels) auto-enabled — see the
    // `study=1` handler in reader.js. The dedicated verse-study page is being retired.
    if (isSingleVerse) { vsLink.href = READER_URL + '?ref=' + singleRef + '&study=1'; vsLink.removeAttribute('hidden'); }
    else { vsLink.setAttribute('hidden', ''); }
  }
  if (cmpLink) {
    if (isSingleVerse) { cmpLink.href = COMPARE_URL + '?ref=' + singleRef; cmpLink.removeAttribute('hidden'); }
    else { cmpLink.setAttribute('hidden', ''); }
  }

  var memBtn = _modalEl.querySelector('.bsw-modal__memory-btn');
  if (memBtn) {
    if (isSingleVerse && _memHasFn) {
      var memRef = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
      memBtn._memRef    = memRef;
      memBtn.textContent = _memHasFn(memRef) ? '⭐ Memorizing' : '☆ Memorize';
      memBtn.classList.toggle('bsw-modal__memory-btn--active', _memHasFn(memRef));
      memBtn.removeAttribute('hidden');
    } else {
      memBtn.setAttribute('hidden', '');
    }
  }
  var shareBtn = _modalEl.querySelector('.bsw-modal__share-btn');
  if (shareBtn) shareBtn.removeAttribute('hidden');
  // VM-I: show prev/next buttons only for single verse
  var prevBtn = _modalEl.querySelector('.bsw-modal__prev-verse');
  var nextBtn = _modalEl.querySelector('.bsw-modal__next-verse');
  if (prevBtn) {
    if (isSingleVerse && parsed.v > 1) prevBtn.removeAttribute('hidden');
    else prevBtn.setAttribute('hidden', '');
  }
  if (nextBtn) {
    if (isSingleVerse) nextBtn.removeAttribute('hidden');
    else nextBtn.setAttribute('hidden', '');
  }
  // VM-F: restore last tab (lazy-load on activation handles fresh data)
  if (_lastTab && _lastTab !== 'verse') {
    var lastTabBtn = _modalEl.querySelector('.bsw-modal__tab[data-tab="' + _lastTab + '"]');
    if (lastTabBtn) lastTabBtn.click();
  }

  return resolveVerses(parsed, versionId)
    .then(function (verses) {
      if (!verses || !verses.length) {
        body.innerHTML = '<p class="bsw-modal__error">Verse not found in ' + escHtml(versionId) + '.</p>';
        return;
      }

      var html = '';
      if (parsed.wholeChapter && parsed.endCh !== parsed.ch) {
        for (var c = parsed.ch; c <= parsed.endCh; c++) {
          var chVerses = verses.filter(function (vr) { return vr.chapter === c; });
          var chRef2   = READER_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + c);
          html += '<div class="bsw-modal__chapter-section">';
          html += '<div class="bsw-modal__chapter-label">' +
            escHtml(parsed.bookName) + ' ' + c +
            '<a class="bsw-modal__chapter-read" href="' + chRef2 + '">Read chapter ↗</a></div>';
          chVerses.slice(0, 2).forEach(function (vr) {
            html += '<div class="bsw-modal__verse" data-ch="' + c + '" data-v="' + vr.verse + '">' +
              '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
              '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span></div>';
          });
          html += '</div>';
        }
      } else if (parsed.wholeChapter) {
        var PREVIEW_LIMIT = 5;
        var shown     = verses.slice(0, PREVIEW_LIMIT);
        var remaining = verses.length - shown.length;
        html = shown.map(function (vr) {
          return '<div class="bsw-modal__verse" data-ch="' + parsed.ch + '" data-v="' + vr.verse + '">' +
            '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
            '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span></div>';
        }).join('');
        if (remaining > 0) {
          var chRef = parsed.bookName + ' ' + parsed.ch;
          html += '<div class="bsw-modal__chapter-more">…and ' + remaining + ' more verse' +
            (remaining === 1 ? '' : 's') +
            ' — <a class="bsw-modal__chapter-more-link" href="' +
            READER_URL + '?ref=' + encodeURIComponent(chRef) + '">Read full chapter in Reader ↗</a></div>';
        }
      } else {
        html = verses.map(function (vr) {
          return '<div class="bsw-modal__verse" data-ch="' + (vr.chapter || parsed.ch) + '" data-v="' + vr.verse + '">' +
            '<sup class="bsw-modal__verse-num">' + vr.verse + '</sup>' +
            '<span class="bsw-modal__verse-text">' + escHtml(vr.text) + '</span></div>';
        }).join('');
      }

      body.innerHTML = html;
      attr.innerHTML = ATTRIBUTION[versionId] || '';
      applyModalHighlights(body, parsed);
      _maybeAutoTag(body);
      _injectModalFootnotes(parsed, body);
      // VM-I: cap next-verse at chapter boundary once verse data is loaded
      if (isSingleVerse && verses.chapterMaxV) {
        _modalEl._chapterMaxV = verses.chapterMaxV;
        var nextBtnPost = _modalEl.querySelector('.bsw-modal__next-verse');
        if (nextBtnPost && parsed.v >= verses.chapterMaxV) nextBtnPost.setAttribute('hidden', '');
      }
    })
    .catch(function () {
      body.innerHTML = '<p class="bsw-modal__error">Could not load ' + escHtml(versionId) + ' data.</p>';
    });
}

// ── _injectModalFootnotes ────────────────────────────────────────────────
function _injectModalFootnotes(parsed, bodyEl) {
  if (!parsed || !bodyEl) return;
  var gen = (bodyEl._footnoteGen = (bodyEl._footnoteGen || 0) + 1);
  loadCrossRefs(parsed.bookId).then(function (data) {
    if (bodyEl._footnoteGen !== gen) return;
    if (!data) return;
    var verseEls = bodyEl.querySelectorAll('.bsw-modal__verse[data-ch][data-v]');
    verseEls.forEach(function (verseEl) {
      var c      = +verseEl.getAttribute('data-ch');
      var v      = +verseEl.getAttribute('data-v');
      var chData = data[String(c)];
      if (!chData) return;
      var rawRefs = chData[String(v)];
      if (!rawRefs || !rawRefs.length) return;
      var entries = rawRefs.map(parseCrossRefEntry);
      entries.sort(function (a, b) { return b.votes - a.votes; });
      entries = entries.slice(0, XREF_CHAPTER_LIMIT);
      entries.sort(_compareCanonical);
      entries.forEach(function (entry, i) {
        var p = parseRef(entry.ref);
        if (!p) return;
        var sup = document.createElement('sup');
        sup.className = 'bsw-modal__xref-note';
        sup.setAttribute('data-ref', entry.ref);
        sup.setAttribute('aria-label', 'Cross-reference: ' + entry.ref);
        sup.setAttribute('tabindex', '0');
        sup.setAttribute('role', 'button');
        sup.textContent = String(i + 1);
        wireRefEl(sup, p);
        verseEl.appendChild(sup);
      });
    });
  }).catch(function () {});
}

// ── _extractCommHtml ──────────────────────────────────────────────────────
// VM-H: returns { html, foundV } so callers can show a "nearest section" notice
export function _extractCommHtml(data, parsed, source) {
  if (!data) return { html: null, foundV: null };
  var chData = data[String(parsed.ch)];
  if (!chData) return { html: null, foundV: null };
  var sectionKeys = Object.keys(chData).map(Number).sort(function (a, b) { return a - b; });
  var html   = '';
  var endV   = parsed.wholeChapter ? 9999 : parsed.endV;
  var startV = parsed.v;
  var foundV = null;
  if (parsed.wholeChapter) {
    sectionKeys.forEach(function (v) {
      html += '<div class="bsw-modal__commentary-section">' + chData[String(v)] + '</div>';
    });
  } else {
    for (var v = startV; v >= 1; v--) {
      if (chData[String(v)]) { foundV = v; break; }
    }
    if (foundV !== null) {
      html = '<div class="bsw-modal__commentary-section">' + chData[String(foundV)] + '</div>';
      sectionKeys.forEach(function (v) {
        if (v > startV && v <= endV && chData[String(v)]) {
          html += '<div class="bsw-modal__commentary-section">' + chData[String(v)] + '</div>';
        }
      });
    }
  }
  return { html: html || null, foundV: foundV };
}

// INTENT: Render the Connections tab — Biblepedia article badges for the open reference.
//   Matches index entries whose key_refs land inside `parsed` (via _refInParsed), groups
//   them by category (people → places → events → concepts → …), and renders each as a chip
//   linking to the article reader at /biblepedia/?a={id}. Lazy: only fires on first tab
//   activation (guarded by container._connLoaded in the tab-switch handler) and the 1.7MB
//   index is fetched once per session.
// CHANGE? Index shape is { id, term, category, brief, key_refs, has_article } — mirrors the
//   reader study desk's _bpMatches. If data/biblepedia/index.json changes, update both.
// VERIFY: Open John 1:1 → Connections shows badges (e.g. "Word (Logos)", "Jesus Christ");
//   click one → opens the Biblepedia article. A verse with no keyed articles shows an empty note.
var _BP_CAT_ORDER = { people: 0, person: 0, places: 1, place: 1, events: 2, event: 2, concepts: 3, concept: 3, names: 4, name: 4, father: 5, commentator: 6 };
export function _renderConnectionsPanel(parsed, container) {
  container._connLoaded = true;
  if (!parsed) { container.innerHTML = '<p class="bsw-modal__conn-empty">No reference selected.</p>'; return; }
  container.innerHTML = '<p class="bsw-modal__loading">Finding connected articles…</p>';

  _loadBPIndex().then(function (idx) {
    // Guard against a version/verse change that swapped the open ref while we were fetching.
    if (_modalEl && _modalEl._parsedRef !== parsed) return;
    var matches = [];
    idx.forEach(function (a) {
      if (!a || a.has_article === false) return;
      var refs = a.key_refs || [], hit = false;
      for (var i = 0; i < refs.length && !hit; i++) {
        var p = parseRef(refs[i]);
        if (p && _refInParsed(p, parsed)) hit = true;
      }
      if (hit) matches.push(a);
    });
    matches.sort(function (a, b) {
      var ca = _BP_CAT_ORDER[a.category] != null ? _BP_CAT_ORDER[a.category] : 9;
      var cb = _BP_CAT_ORDER[b.category] != null ? _BP_CAT_ORDER[b.category] : 9;
      if (ca !== cb) return ca - cb;
      return String(a.term || '').localeCompare(String(b.term || ''));
    });

    if (!matches.length) {
      container.innerHTML = '<p class="bsw-modal__conn-empty">No encyclopedia articles key to ' +
        escHtml(parsed.display) + '.</p>';
      return;
    }
    var n = matches.length;
    var html = '<p class="bsw-modal__conn-note">' + n + ' encyclopedia article' + (n === 1 ? '' : 's') +
      ' connected to ' + escHtml(parsed.display) + ':</p><div class="bsw-modal__conn-badges">';
    matches.forEach(function (a) {
      var href = _BP_PAGE_URL + '?a=' + encodeURIComponent(a.id);
      var cat  = a.category ? '<span class="bsw-modal__conn-cat">' + escHtml(a.category) + '</span>' : '';
      html += '<a class="bsw-modal__conn-badge" href="' + href + '" title="' +
        escHtml(a.brief || a.term || '') + '">' + escHtml(a.term || a.id) + cat + '</a>';
    });
    html += '</div>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML = '<p class="bsw-modal__conn-empty">Could not load encyclopedia index.</p>';
  });
}

// INTENT: Update the "Notes" tab badge count by summing notes across the full verse range of
//   `parsed`; called by `renderModal` on every open and by `_renderNotesPanel`'s save handler.
// CHANGE? `getNotesForVerse` reads the `bsw_notes` localStorage key (managed in storage.js);
//   if the key or schema changes, update `getNotesForVerse` there and this badge will auto-follow.
// VERIFY: Open John 3:16 with an existing note → Notes tab shows badge with count; add a note
//   → badge increments without re-opening the modal.
// ── _refreshModalNotesBadge ───────────────────────────────────────────────
export function _refreshModalNotesBadge(parsed) {
  if (!_modalEl || !parsed) return;
  var noteBtn = _modalEl.querySelector('.bsw-modal__tab[data-tab="notes"]');
  if (!noteBtn) return;
  // VM-C: sum notes across the full verse range, not just v
  var count = 0;
  var _badgeEndV = (parsed.endV && parsed.endCh === parsed.ch) ? parsed.endV : parsed.v;
  for (var _vi = parsed.v; _vi <= _badgeEndV; _vi++) {
    count += getNotesForVerse(parsed.bookId, parsed.ch, _vi).length;
  }
  var badge = noteBtn.querySelector('.bsw-modal__tab-badge');
  if (count > 0) {
    if (!badge) {
      badge = document.createElement('span');
      badge.className = 'bsw-modal__tab-badge';
      noteBtn.appendChild(badge);
    }
    badge.textContent = String(count);
  } else {
    if (badge) badge.remove();
  }
}

// INTENT: Render the notes panel for `parsed`: loads existing notes from `bsw_notes` (via
//   storage.js), renders a textarea + save button, wires autosave on blur, and returns a
//   `refresh()` function called by the tab-switch handler to reload notes without re-opening the modal.
// CHANGE? Writes to the same `bsw_notes` key read by `_refreshModalNotesBadge`; the note
//   object schema `{ id, text, display, bookId, ch, v, ts }` is defined in storage.js —
//   any field addition must be mirrored there and in the badge-count summing logic.
// VERIFY: Open any verse → write a note → blur textarea → reopen modal for same verse
//   → note text persists; badge on Notes tab shows count matching saved notes.
// ── _renderNotesPanel ────────────────────────────────────────────────────
export function _renderNotesPanel(parsed, container) {
  if (!parsed) { container.innerHTML = '<p class="bsw-note-empty">No reference selected.</p>'; return function () {}; }

  function buildNoteItem(note) {
    var div  = document.createElement('div');
    div.className = 'bsw-note-item';
    div.setAttribute('data-note-id', note.id);

    var body = document.createElement('div');
    body.className  = 'bsw-note-body';
    body.textContent = note.text;
    div.appendChild(body);

    var meta = document.createElement('div');
    meta.className = 'bsw-note-meta';
    var rangeLabel = note.display !== parsed.display
      ? '<span class="bsw-note-range">' + escHtml(note.display) + '</span> · ' : '';
    meta.innerHTML = rangeLabel + '<span class="bsw-note-time">' + _noteRelTime(note.created) + '</span>';
    div.appendChild(meta);

    var actions  = document.createElement('div');
    actions.className = 'bsw-note-actions';
    var editBtn  = document.createElement('button');
    editBtn.className  = 'bsw-note-action-btn';
    editBtn.textContent = 'Edit';
    var delBtn   = document.createElement('button');
    delBtn.className   = 'bsw-note-action-btn bsw-note-action-btn--del';
    delBtn.textContent  = 'Delete';
    actions.appendChild(editBtn);
    actions.appendChild(delBtn);
    div.appendChild(actions);

    var editArea = document.createElement('div');
    editArea.className = 'bsw-note-edit-area';
    editArea.hidden    = true;
    var ta       = document.createElement('textarea');
    ta.className  = 'bsw-note-textarea';
    ta.value      = note.text;
    var saveBtn   = document.createElement('button');
    saveBtn.className  = 'vs-context-btn';
    saveBtn.textContent = 'Save';
    var cancelBtn = document.createElement('button');
    cancelBtn.className  = 'bsw-note-action-btn';
    cancelBtn.textContent = 'Cancel';
    var editBtnRow = document.createElement('div');
    editBtnRow.className = 'bsw-note-edit-btns';
    editBtnRow.appendChild(saveBtn);
    editBtnRow.appendChild(cancelBtn);
    editArea.appendChild(ta);
    editArea.appendChild(editBtnRow);
    div.appendChild(editArea);

    editBtn.addEventListener('click', function () {
      editArea.hidden = false; body.hidden = true; meta.hidden = true; actions.hidden = true;
      ta.focus();
    });
    cancelBtn.addEventListener('click', function () {
      editArea.hidden = true; body.hidden = false; meta.hidden = false; actions.hidden = false;
      ta.value = note.text;
    });
    saveBtn.addEventListener('click', function () {
      var t = ta.value.trim();
      if (!t) return;
      updateNoteV2(note.id, t);
      body.textContent = t; note.text = t;
      editArea.hidden = true; body.hidden = false; meta.hidden = false; actions.hidden = false;
    });
    delBtn.addEventListener('click', function () {
      deleteNoteV2(note.id);
      div.remove();
      _refreshModalNotesBadge(parsed);
    });

    return div;
  }

  function _innerRefresh() {
    container.innerHTML = '';

    var hlRef  = parsed.bookName + ' ' + parsed.ch + ':' + parsed.v;
    var hlRow  = document.createElement('div');
    hlRow.className = 'bsw-hl-row';
    var hlLbl  = document.createElement('span');
    hlLbl.className  = 'bsw-hl-label';
    hlLbl.textContent = 'Highlight:';
    hlRow.appendChild(hlLbl);
    var _curNote = getNote(hlRef);
    var _curHl   = _curNote && _curNote.highlight;
    if (_curHl === true) _curHl = 'yellow';
    _HL_COLORS.forEach(function (c) {
      var sw = document.createElement('button');
      sw.type = 'button';
      sw.className = 'bsw-hl-swatch bsw-hl-swatch--' + c + (_curHl === c ? ' bsw-hl-swatch--active' : '');
      sw.title = c.charAt(0).toUpperCase() + c.slice(1) + ' highlight';
      sw.setAttribute('aria-label', 'Highlight ' + c);
      sw.setAttribute('data-c', c);
      sw.addEventListener('click', function () {
        var newHl = toggleHighlight(hlRef, c);
        hlRow.querySelectorAll('.bsw-hl-swatch[data-c]').forEach(function (s) {
          s.classList.toggle('bsw-hl-swatch--active', !!(newHl && s.getAttribute('data-c') === newHl));
        });
        var re = document.getElementById('reader-results');
        if (re) applyHighlights(re);
      });
      hlRow.appendChild(sw);
    });
    var offSw = document.createElement('button');
    offSw.type = 'button';
    offSw.className = 'bsw-hl-swatch bsw-hl-swatch--off';
    offSw.title = 'Remove highlight';
    offSw.setAttribute('aria-label', 'Remove highlight');
    offSw.textContent = '✕';
    offSw.addEventListener('click', function () {
      var n2 = getNote(hlRef) || {};
      n2.highlight = false;
      saveNote(hlRef, n2);
      hlRow.querySelectorAll('.bsw-hl-swatch[data-c]').forEach(function (s) { s.classList.remove('bsw-hl-swatch--active'); });
      var re = document.getElementById('reader-results');
      if (re) applyHighlights(re);
    });
    hlRow.appendChild(offSw);
    container.appendChild(hlRow);

    var tagRow   = document.createElement('div');
    tagRow.className = 'bsw-tag-row';
    var tagChips = document.createElement('div');
    tagChips.className = 'bsw-tag-chips';
    var tagInput = document.createElement('input');
    tagInput.type        = 'text';
    tagInput.className   = 'bsw-tag-input';
    tagInput.placeholder = 'add tag…';
    tagInput.maxLength   = 40;
    tagRow.appendChild(tagChips);
    tagRow.appendChild(tagInput);
    function _refreshTagChips() {
      tagChips.innerHTML = '';
      getTags(hlRef).forEach(function (t) {
        var chip = document.createElement('span');
        chip.className = 'bsw-tag-chip';
        chip.appendChild(document.createTextNode(t));
        var rb = document.createElement('button');
        rb.type = 'button';
        rb.className = 'bsw-tag-chip__remove';
        rb.setAttribute('aria-label', 'Remove tag ' + t);
        rb.textContent = '×';
        rb.addEventListener('click', (function (tag) {
          return function () { removeTag(hlRef, tag); _refreshTagChips(); };
        })(t));
        chip.appendChild(rb);
        tagChips.appendChild(chip);
      });
    }
    _refreshTagChips();
    tagInput.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ',') return;
      e.preventDefault();
      var val = tagInput.value.trim();
      if (!val) return;
      addTag(hlRef, val);
      tagInput.value = '';
      _refreshTagChips();
    });
    container.appendChild(tagRow);

    var notes = getNotesForVerse(parsed.bookId, parsed.ch, parsed.v);
    if (notes.length) {
      var list = document.createElement('div');
      list.className = 'bsw-note-list';
      notes.forEach(function (n) { list.appendChild(buildNoteItem(n)); });
      container.appendChild(list);
    } else {
      var empty = document.createElement('p');
      empty.className  = 'bsw-note-empty';
      empty.textContent = 'No notes yet for ' + (parsed.display || 'this verse') + '.';
      container.appendChild(empty);
    }

    var compose = document.createElement('div');
    compose.className = 'bsw-note-compose';
    var cta     = document.createElement('textarea');
    cta.className   = 'bsw-note-textarea';
    cta.placeholder = 'Add a note for ' + (parsed.display || 'this verse') + '…';
    var footer  = document.createElement('div');
    footer.className = 'bsw-note-compose-footer';
    var refTag  = document.createElement('span');
    refTag.className  = 'bsw-note-ref-tag';
    refTag.textContent = parsed.display || '';
    var addBtn  = document.createElement('button');
    addBtn.className  = 'vs-context-btn';
    addBtn.textContent = 'Save note';
    footer.appendChild(refTag);
    footer.appendChild(addBtn);
    compose.appendChild(cta);
    compose.appendChild(footer);
    container.appendChild(compose);

    addBtn.addEventListener('click', function () {
      var t = cta.value.trim();
      if (!t) return;
      createNoteV2(parsed, t);
      cta.value = '';
      refresh();
    });

    // INTENT: NOTES_URL was exported from core.js but never surfaced — this link makes the
    //   standalone notes page discoverable from the verse modal after saving a note.
    // CHANGE? If NOTES_URL path changes in core.js the link href updates automatically.
    // VERIFY: Open verse study modal → Notes tab. "View all notes ↗" link appears below compose area.
    var viewAllNotes = document.createElement('a');
    viewAllNotes.className  = 'bsw-notes-viewall';
    viewAllNotes.href       = NOTES_URL;
    viewAllNotes.textContent = 'View all notes ↗';
    container.appendChild(viewAllNotes);
  }

  function refresh() {
    _refreshModalNotesBadge(parsed);
    _innerRefresh();
  }

  refresh();
  return refresh;
}

// ── hideModal ─────────────────────────────────────────────────────────────
export function hideModal() {
  if (!_backdropEl) return;
  _backdropEl.classList.add('bsw-modal-backdrop--hidden');
  _backdropEl.setAttribute('aria-hidden', 'true');
  if (_modalEl) {
    _modalEl.removeEventListener('keydown', trapFocus);
    // VM-M2: clear any in-progress swipe transform
    _modalEl.style.transform  = '';
    _modalEl.style.transition = '';
  }
  document.documentElement.classList.remove('bsw-modal-open');
  document.body.classList.remove('bsw-modal-open');
  if (_lastFocused) { try { _lastFocused.focus(); } catch (e) {} _lastFocused = null; }
}

// ── trapFocus ─────────────────────────────────────────────────────────────
export function trapFocus(e) {
  if (e.key !== 'Tab') return;
  var focusable = Array.prototype.slice.call(
    _modalEl.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
  ).filter(function (el) { return !el.disabled && el.offsetParent !== null; });
  if (!focusable.length) return;
  var first = focusable[0];
  var last  = focusable[focusable.length - 1];
  if (e.shiftKey) {
    if (document.activeElement === first) { e.preventDefault(); last.focus(); }
  } else {
    if (document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
}

// ── Share verse as image ──────────────────────────────────────────────────
var _shareOverlayEl = null;

var _SHARE_PRESETS = [
  { id: 'parchment', label: 'Parchment',  bg: '#f4ede1', text: '#2c1a0e', accent: '#7a5533' },
  { id: 'gold',      label: 'Warm Gold',  bg: '#fdf3d8', text: '#1c1000', accent: '#9a7010' },
  { id: 'stone',     label: 'Stone',      bg: '#f0f2f4', text: '#1a2030', accent: '#4a6080' },
  { id: 'white',     label: 'Minimal',    bg: '#ffffff', text: '#111111', accent: '#555555' },
  { id: 'sepia',     label: 'Candlelit',  bg: '#241508', text: '#f0e0c0', accent: '#c9925a' },
  { id: 'slate',     label: 'Slate',      bg: '#1a2330', text: '#e8e0d0', accent: '#8fb0d0' },
  { id: 'forest',    label: 'Forest',     bg: '#162218', text: '#cce8d4', accent: '#5a9a6a' },
  { id: 'twilight',  label: 'Twilight',   bg: '#1c1828', text: '#e0d8f4', accent: '#9878d0' }
];

var _SCENE_ROOT = _resolve('../../assets/share-scenes/');

var _SHARE_SCENES = [
  { id: 'dawn',      label: 'Dawn Sky',    overlay: 'rgba(0,0,0,0.32)', textColor: '#fff', accentColor: '#f6c96a', credit: 'Generated artwork' },
  { id: 'mountains', label: 'Mountains',   overlay: 'rgba(0,0,0,0.42)', textColor: '#fff', accentColor: '#cce0f5', credit: 'Generated artwork' },
  { id: 'sea',       label: 'Sea',         overlay: 'rgba(0,0,0,0.35)', textColor: '#fff', accentColor: '#a8d8ea', credit: 'Generated artwork' },
  { id: 'desert',    label: 'Desert',      overlay: 'rgba(0,0,0,0.38)', textColor: '#fff', accentColor: '#f5d98a', credit: 'Generated artwork' },
  { id: 'wheat',     label: 'Wheat Field', overlay: 'rgba(0,0,0,0.35)', textColor: '#fff', accentColor: '#f9e07a', credit: 'Generated artwork' },
  { id: 'olive',     label: 'Olive Grove', overlay: 'rgba(0,0,0,0.40)', textColor: '#fff', accentColor: '#b8d8a0', credit: 'Generated artwork' },
  { id: 'forestl',   label: 'Forest',      overlay: 'rgba(0,0,0,0.40)', textColor: '#fff', accentColor: '#a8e0b0', credit: 'Generated artwork' },
  { id: 'stars',     label: 'Starfield',   overlay: 'rgba(0,0,0,0.30)', textColor: '#fff', accentColor: '#a0c0f0', credit: 'Generated artwork' },
  { id: 'jerusalem', label: 'Jerusalem',   overlay: 'rgba(0,0,0,0.40)', textColor: '#fff', accentColor: '#f5d090', credit: 'Generated artwork' },
  { id: 'rain',      label: 'Storm',       overlay: 'rgba(0,0,0,0.38)', textColor: '#e8f0ff', accentColor: '#90b0d8', credit: 'Generated artwork' }
];

var _SHARE_FONTS = [
  { id: 'georgia',     label: 'Georgia',     stack: 'Georgia, serif' },
  { id: 'palatino',    label: 'Palatino',    stack: "'Palatino Linotype', Palatino, 'Book Antiqua', serif" },
  { id: 'times',       label: 'Times',       stack: "'Times New Roman', Times, serif" },
  { id: 'baskerville', label: 'Baskerville', stack: "'Baskerville Old Face', Baskerville, Georgia, serif" },
  { id: 'dancing',     label: 'Cursive',     stack: "'Dancing Script', cursive" }
];

function _wrapCanvasText(ctx, text, maxWidth) {
  var words = text.split(' ');
  var lines = [];
  var line  = '';
  for (var i = 0; i < words.length; i++) {
    var test = line ? line + ' ' + words[i] : words[i];
    if (ctx.measureText(test).width > maxWidth && line) { lines.push(line); line = words[i]; }
    else { line = test; }
  }
  if (line) lines.push(line);
  return lines;
}

/* Returns a Promise so callers can chain after the (possibly async) image load. */
function _drawShareCanvas(canvas, presetId, fontId, verseText, refDisplay, versionId) {
  var scene  = _SHARE_SCENES.filter(function (s) { return s.id === presetId; })[0];
  var preset = scene ? null : (_SHARE_PRESETS.filter(function (p) { return p.id === presetId; })[0] || _SHARE_PRESETS[0]);
  var font   = _SHARE_FONTS.filter(function (f) { return f.id === fontId; })[0] || _SHARE_FONTS[0];

  function _paint(bgReady) {
    var ctx = canvas.getContext('2d');
    var W = 1200, H = 630;
    ctx.clearRect(0, 0, W, H);

    if (scene) {
      /* cover-fit the scene image */
      var imgW = bgReady.naturalWidth, imgH = bgReady.naturalHeight;
      var scale = Math.max(W / imgW, H / imgH);
      var sw = imgW * scale, sh = imgH * scale;
      ctx.drawImage(bgReady, (W - sw) / 2, (H - sh) / 2, sw, sh);
      /* readability overlay */
      ctx.fillStyle = scene.overlay;
      ctx.fillRect(0, 0, W, H);
    } else {
      ctx.fillStyle = preset.bg;
      ctx.fillRect(0, 0, W, H);
    }

    var textColor   = scene ? scene.textColor   : preset.text;
    var accentColor = scene ? scene.accentColor  : preset.accent;

    /* accent bars */
    ctx.fillStyle = accentColor;
    ctx.fillRect(0, 0, W, 7);
    ctx.fillRect(0, H - 7, W, 7);

    /* header label */
    ctx.fillStyle = accentColor;
    ctx.font = '500 20px ' + font.stack;
    ctx.textAlign = 'left';
    ctx.fillText('Kingdom Bible Study', 60, 52);

    /* verse text — Dancing Script starts at 52px because it renders smaller */
    var maxW = W - 160;
    var fontSize = (fontId === 'dancing') ? 52 : 46;
    var lines;
    while (fontSize >= 24) {
      ctx.font = 'italic ' + fontSize + 'px ' + font.stack;
      lines = _wrapCanvasText(ctx, '“' + verseText + '”', maxW);
      if (lines.length * fontSize * 1.45 <= H - 230) break;
      fontSize -= 2;
    }
    var lineH  = fontSize * 1.45;
    var totalH = lines.length * lineH;
    var startY = Math.round((H - totalH) / 2) - 20;
    ctx.fillStyle = textColor;
    ctx.textAlign = 'center';
    ctx.font = 'italic ' + fontSize + 'px ' + font.stack;
    lines.forEach(function (ln, i) { ctx.fillText(ln, W / 2, startY + i * lineH + fontSize); });

    /* reference line */
    ctx.fillStyle = accentColor;
    ctx.font = '600 24px ' + font.stack;
    ctx.textAlign = 'right';
    ctx.fillText('— ' + refDisplay + '  (' + (versionId || 'BSB').toUpperCase() + ')', W - 60, H - 50);

    /* scene attribution */
    if (scene && scene.credit) {
      ctx.fillStyle = 'rgba(255,255,255,0.55)';
      ctx.font = '12px system-ui, sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(scene.credit, 14, H - 12);
    }
  }

  /* For Dancing Script, ensure font is loaded before drawing */
  var fontLoadPromise = (fontId === 'dancing' && document.fonts)
    ? document.fonts.load('40px "Dancing Script"')
    : Promise.resolve();

  if (scene) {
    return fontLoadPromise.then(function () {
      return new Promise(function (resolve) {
        var img = new Image();
        img.onload  = function () { _paint(img); resolve(); };
        img.onerror = function () {
          /* fallback to plain dark background if image fails */
          var ctx = canvas.getContext('2d');
          ctx.fillStyle = '#1a1a2e';
          ctx.fillRect(0, 0, 1200, 630);
          _paint({ naturalWidth: 1200, naturalHeight: 630 });
          resolve();
        };
        img.src = _SCENE_ROOT + scene.id + '.jpg';
      });
    });
  }
  return fontLoadPromise.then(function () { _paint(null); });
}

function _buildBgGallery() {
  var solidCards = _SHARE_PRESETS.map(function (p, i) {
    var checked = i === 0 ? ' checked' : '';
    return '<label class="bsw-share-bg-card">' +
      '<input type="radio" name="share-bg" value="' + p.id + '"' + checked + ' />' +
      '<div class="bsw-share-bg-thumb" style="background:' + p.bg + ';flex-direction:column;justify-content:space-between">' +
        '<div style="height:3px;background:' + p.accent + ';width:100%"></div>' +
        '<div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:1px;overflow:hidden">' +
          '<span style="font-family:Georgia,serif;font-style:italic;font-size:8px;line-height:1.2;color:' + p.text + '">He so loved</span>' +
          '<span style="font-family:Georgia,serif;font-size:7px;color:' + p.accent + '">— John 3:16</span>' +
        '</div>' +
        '<div style="height:3px;background:' + p.accent + ';width:100%"></div>' +
      '</div>' +
      '<span class="bsw-share-bg-label">' + escHtml(p.label) + '</span>' +
    '</label>';
  }).join('');

  var sceneSep = '<span class="bsw-share-gallery-sep">Scenery</span>';

  var sceneCards = _SHARE_SCENES.map(function (s) {
    return '<label class="bsw-share-bg-card">' +
      '<input type="radio" name="share-bg" value="' + s.id + '" />' +
      '<div class="bsw-share-bg-thumb bsw-share-bg-thumb--scene">' +
        '<img src="' + _SCENE_ROOT + s.id + '.jpg" alt="" loading="lazy" ' +
          'style="width:100%;height:100%;object-fit:cover;display:block" />' +
      '</div>' +
      '<span class="bsw-share-bg-label">' + escHtml(s.label) + '</span>' +
    '</label>';
  }).join('');

  return '<div class="bsw-share-bg-gallery" role="radiogroup" aria-label="Background">' +
    solidCards + sceneSep + sceneCards +
  '</div>';
}

function _buildFontGallery() {
  return '<div class="bsw-share-font-gallery" role="radiogroup" aria-label="Font">' +
    _SHARE_FONTS.map(function (f, i) {
      var checked = i === 0 ? ' checked' : '';
      return '<label class="bsw-share-font-card">' +
        '<input type="radio" name="share-font" value="' + f.id + '"' + checked + ' />' +
        '<div class="bsw-share-font-thumb">' +
          '<span style="font-family:' + f.stack + ';font-style:italic;font-size:14px;color:#2c1a0e;line-height:1.3">For God<br>so loved</span>' +
        '</div>' +
        '<span class="bsw-share-font-label">' + escHtml(f.label) + '</span>' +
      '</label>';
    }).join('') +
  '</div>';
}

export function _shareVerseAsImage(verseText, refDisplay, versionId) {
  if (!verseText || !refDisplay) return;
  if (!_shareOverlayEl) {
    _shareOverlayEl = document.createElement('div');
    _shareOverlayEl.className = 'bsw-share-overlay';
    _shareOverlayEl.setAttribute('role', 'dialog');
    _shareOverlayEl.setAttribute('aria-modal', 'true');
    _shareOverlayEl.setAttribute('aria-label', 'Share verse as image');
    document.body.appendChild(_shareOverlayEl);
  }
  _shareOverlayEl.innerHTML =
    '<div class="bsw-share-card">' +
      '<div class="bsw-share-header">' +
        '<span class="bsw-share-title">Share Verse</span>' +
        '<button class="bsw-share-close" aria-label="Close">✕</button>' +
      '</div>' +
      '<div class="bsw-share-section-label">Background</div>' +
      _buildBgGallery() +
      '<div class="bsw-share-section-label" style="margin-top:.6rem">Font</div>' +
      _buildFontGallery() +
      '<canvas class="bsw-share-canvas" width="1200" height="630"></canvas>' +
      '<div class="bsw-share-actions"><button class="bsw-share-download vs-context-btn">' + (navigator.share ? '⬆ Share' : '⬇ Download PNG') + '</button></div>' +
    '</div>';
  _shareOverlayEl.removeAttribute('hidden');
  var canvas    = _shareOverlayEl.querySelector('.bsw-share-canvas');
  function currentPreset() { var c = _shareOverlayEl.querySelector('[name="share-bg"]:checked');   return c ? c.value : 'parchment'; }
  function currentFont()   { var c = _shareOverlayEl.querySelector('[name="share-font"]:checked'); return c ? c.value : 'georgia';   }
  function draw() { _drawShareCanvas(canvas, currentPreset(), currentFont(), verseText, refDisplay, versionId); }
  draw();
  _shareOverlayEl.querySelectorAll('[name="share-bg"],[name="share-font"]').forEach(function (inp) {
    inp.addEventListener('change', draw);
  });
  _shareOverlayEl.querySelector('.bsw-share-close').addEventListener('click', function () { _shareOverlayEl.setAttribute('hidden', ''); });
  _shareOverlayEl.addEventListener('click', function (e) { if (e.target === _shareOverlayEl) _shareOverlayEl.setAttribute('hidden', ''); });
  // VM-J: Web Share API on supported mobile browsers; fall back to download
  _shareOverlayEl.querySelector('.bsw-share-download').addEventListener('click', function () {
    if (navigator.share) {
      canvas.toBlob(function (blob) {
        var file = new File([blob], 'verse.png', { type: 'image/png' });
        if (navigator.canShare && navigator.canShare({ files: [file] })) {
          navigator.share({ files: [file], title: refDisplay }).catch(function () {});
        } else {
          var a = document.createElement('a');
          a.download = 'verse-' + refDisplay.replace(/[^a-zA-Z0-9]/g, '-') + '.png';
          a.href = canvas.toDataURL('image/png');
          a.click();
        }
      }, 'image/png');
    } else {
      var a = document.createElement('a');
      a.download = 'verse-' + refDisplay.replace(/[^a-zA-Z0-9]/g, '-') + '.png';
      a.href = canvas.toDataURL('image/png');
      a.click();
    }
  });
}

function _shareModalVerseAsImage() {
  var parsed  = _modalEl && _modalEl._parsedRef;
  if (!parsed) return;
  var body    = _modalEl.querySelector('.bsw-modal__body');
  var version = (document.getElementById('bsw-modal-version') || {}).value || getVersion();
  var textEls = body ? body.querySelectorAll('.bsw-modal__verse-text') : [];
  var texts   = [];
  textEls.forEach(function (el) { var t = el.textContent.trim(); if (t) texts.push(t); });
  if (!texts.length) return;
  _shareVerseAsImage(texts.join(' '), parsed.display, version);
}

// ── Shortcuts overlay ─────────────────────────────────────────────────────
var _shortcutsEl = null;

export function _showShortcutsOverlay() {
  if (!_shortcutsEl) {
    var overlay = document.createElement('div');
    overlay.id        = 'bsw-shortcuts-overlay';
    overlay.className = 'bsw-shortcuts-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Keyboard shortcuts');
    overlay.innerHTML =
      '<div class="bsw-shortcuts-dialog">' +
        '<div class="bsw-shortcuts-header">' +
          '<h2 class="bsw-shortcuts-title">Keyboard Shortcuts</h2>' +
          '<button class="bsw-shortcuts-close" aria-label="Close">✕</button>' +
        '</div>' +
        '<div class="bsw-shortcuts-body">' +
          '<div class="bsw-shortcuts-group"><h3 class="bsw-shortcuts-group-label">Global</h3>' +
            '<dl class="bsw-shortcuts-list">' +
              '<dt><kbd>Ctrl</kbd>+<kbd>K</kbd></dt><dd>Open search</dd>' +
              '<dt><kbd>?</kbd></dt><dd>Show this help</dd>' +
            '</dl></div>' +
          '<div class="bsw-shortcuts-group"><h3 class="bsw-shortcuts-group-label">Reader</h3>' +
            '<dl class="bsw-shortcuts-list">' +
              '<dt><kbd>j</kbd> / <kbd>→</kbd></dt><dd>Next chapter</dd>' +
              '<dt><kbd>k</kbd> / <kbd>←</kbd></dt><dd>Previous chapter</dd>' +
              '<dt><kbd>Esc</kbd></dt><dd>Close modal or popup</dd>' +
            '</dl></div>' +
          '<div class="bsw-shortcuts-group"><h3 class="bsw-shortcuts-group-label">Verse Study</h3>' +
            '<dl class="bsw-shortcuts-list">' +
              '<dt><kbd>j</kbd> / <kbd>→</kbd></dt><dd>Next verse</dd>' +
              '<dt><kbd>k</kbd> / <kbd>←</kbd></dt><dd>Previous verse</dd>' +
            '</dl></div>' +
        '</div>' +
      '</div>';
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay || e.target.classList.contains('bsw-shortcuts-close')) _hideShortcutsOverlay();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !overlay.hidden) _hideShortcutsOverlay(); });
    document.body.appendChild(overlay);
    _shortcutsEl = overlay;
  }
  _shortcutsEl.hidden = false;
  var closeBtn = _shortcutsEl.querySelector('.bsw-shortcuts-close');
  if (closeBtn) closeBtn.focus();
}

export function _hideShortcutsOverlay() {
  if (_shortcutsEl) _shortcutsEl.hidden = true;
}

export function _injectShortcutsBtn() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-shortcuts-btn')) return;
  var btn = document.createElement('button');
  btn.id        = 'reader-shortcuts-btn';
  btn.className = 'reader-shortcuts-btn';
  btn.title     = 'Keyboard shortcuts (?)';
  btn.setAttribute('aria-label', 'Keyboard shortcuts');
  btn.textContent = '?';
  btn.addEventListener('click', _showShortcutsOverlay);
  var hint = browseBar.querySelector('.reader-browse-hint');
  browseBar.insertBefore(btn, hint || null);
}

// ── History widget for daily page ─────────────────────────────────────────
export function initHistoryWidget() {
  var el = document.getElementById('daily-history-content');
  if (!el) return;
  var entries = (function () {
    try { return JSON.parse(localStorage.getItem('bsw_history') || '[]'); } catch (e) { return []; }
  })().slice(0, 3);
  if (!entries.length) return;
  var card = el.closest('.daily-card');
  if (card) card.removeAttribute('hidden');
  el.removeAttribute('hidden');
  // Add border between reader history and lib history when both are present
  var libEl = document.getElementById('daily-lib-history');
  if (libEl) libEl.style.borderTop = '1px solid var(--color-border)';
  var html = '';
  var _noteRelTimeFn = _noteRelTime;
  entries.forEach(function (e) {
    // history entries are plain strings (the ref); objects are an older format
    var ref = typeof e === 'string' ? e : (e.ref || '');
    var ver = typeof e === 'string' ? '' : (e.version || '');
    var ts  = typeof e === 'string' ? null : (e.ts || null);
    if (!ref) return;
    var url = READER_URL + '?ref=' + encodeURIComponent(ref);
    html += '<a class="daily-history-item" href="' + escHtml(url) + '">' +
      '<span class="daily-history-ref">' + escHtml(ref) + '</span>' +
      '<span class="daily-history-meta">' + escHtml(ver.toUpperCase()) +
        (ts ? ' · ' + _noteRelTimeFn(ts) : '') + '</span>' +
    '</a>';
  });
  el.innerHTML = html;
}

// Register openModal with core so wire.js can call it without circular imports
registerOpenModal(openModal);
