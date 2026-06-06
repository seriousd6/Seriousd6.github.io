/* modal.js — Verse viewer modal, cross-reference panels, share/copy, shortcuts */
'use strict';

import {
  getVersion, resolveVerses, loadCrossRefs, loadCommentary,
  parseCrossRefEntry, _compareCanonical, parseRef,
  escHtml, READER_URL, VERSE_STUDY_URL, COMPARE_URL,
  COMMENTARY_SOURCES, getCommentarySource, setCommentarySource,
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
  var s = COMMENTARY_SOURCES.filter(function (x) { return x.id === source; })[0];
  return s ? s.attr : source;
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
      '<a class="bsw-modal__verse-study-link" href="#" hidden>Verse Study ↗</a>' +
      '<a class="bsw-modal__compare-link" href="#" hidden>All translations ↗</a>' +
      '<button class="bsw-modal__memory-btn" hidden aria-label="Add to memory">☆ Memorize</button>' +
      '<button class="bsw-modal__copy-quote-btn" hidden aria-label="Copy verse as quote">Quote</button>' +
      '<button class="bsw-modal__copy-ref-btn" hidden aria-label="Copy verse reference">Reference</button>' +
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
      '<button class="bsw-modal__tab" data-tab="commentary" role="tab" aria-selected="false">Commentary</button>' +
      '<button class="bsw-modal__tab" data-tab="wordstudy" role="tab" aria-selected="false">Word Study</button>' +
      '<button class="bsw-modal__tab" data-tab="topics" role="tab" aria-selected="false">Topics</button>' +
      '<button class="bsw-modal__tab" data-tab="confessions" role="tab" aria-selected="false">Confessions</button>' +
      '<button class="bsw-modal__tab" data-tab="fathers" role="tab" aria-selected="false">Fathers</button>' +
      '<button class="bsw-modal__tab" data-tab="dictionary" role="tab" aria-selected="false">Dictionary</button>' +
      '<button class="bsw-modal__tab" data-tab="crossrefs" role="tab" aria-selected="false">Cross Refs</button>' +
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
    '<div class="bsw-modal__commentary-panel" hidden></div>' +
    '<div class="bsw-modal__wordstudy-panel" hidden></div>' +
    '<div class="bsw-modal__topics-panel" hidden></div>' +
    '<div class="bsw-modal__confessions-panel" hidden></div>' +
    '<div class="bsw-modal__fathers-panel" hidden></div>' +
    '<div class="bsw-modal__dictionary-panel" hidden></div>' +
    '<div class="bsw-modal__crossrefs-panel" hidden></div>';

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
  modal.querySelector('.bsw-modal__copy-quote-btn').addEventListener('click', function () {
    _copyModalVerse(this, 'plain');
  });
  modal.querySelector('.bsw-modal__copy-ref-btn').addEventListener('click', function () {
    _copyModalVerse(this, 'cite');
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
    var splitEl    = modal.querySelector('.bsw-modal__split');
    var notesEl    = modal.querySelector('.bsw-modal__notes-panel');
    var commEl     = modal.querySelector('.bsw-modal__commentary-panel');
    var wsEl       = modal.querySelector('.bsw-modal__wordstudy-panel');
    var topicsEl   = modal.querySelector('.bsw-modal__topics-panel');
    var confEl     = modal.querySelector('.bsw-modal__confessions-panel');
    var fathersEl  = modal.querySelector('.bsw-modal__fathers-panel');
    var dictEl     = modal.querySelector('.bsw-modal__dictionary-panel');
    var xrefsEl    = modal.querySelector('.bsw-modal__crossrefs-panel');
    var allPanels  = [splitEl, notesEl, commEl, wsEl, topicsEl, confEl, fathersEl, dictEl, xrefsEl];
    allPanels.forEach(function (p) { if (p) p.setAttribute('hidden', ''); });

    if (tab === 'verse') {
      if (splitEl) splitEl.removeAttribute('hidden');
    } else if (tab === 'notes') {
      if (notesEl) { notesEl.removeAttribute('hidden'); _renderNotesPanel(_modalEl._parsedRef, notesEl); }
    } else if (tab === 'commentary') {
      if (commEl) { commEl.removeAttribute('hidden'); if (!commEl._commentaryLoaded) renderCommentary(_modalEl._parsedRef, commEl); }
    } else if (tab === 'wordstudy') {
      if (wsEl) { wsEl.removeAttribute('hidden'); if (!wsEl._wsLoaded && _renderModalWordStudyFn) _renderModalWordStudyFn(_modalEl._parsedRef, wsEl); }
    } else if (tab === 'topics') {
      if (topicsEl) { topicsEl.removeAttribute('hidden'); if (!topicsEl._topicsLoaded && _renderModalTopicsFn) _renderModalTopicsFn(_modalEl._parsedRef, topicsEl); }
    } else if (tab === 'confessions') {
      if (confEl) { confEl.removeAttribute('hidden'); if (!confEl._confLoaded && _renderModalConfessionsFn) _renderModalConfessionsFn(_modalEl._parsedRef, confEl); }
    } else if (tab === 'fathers') {
      if (fathersEl) { fathersEl.removeAttribute('hidden'); if (!fathersEl._fathersLoaded && _renderModalFathersFn) _renderModalFathersFn(_modalEl._parsedRef, fathersEl); }
    } else if (tab === 'dictionary') {
      if (dictEl) { dictEl.removeAttribute('hidden'); if (!dictEl._dictLoaded && _renderModalDictionaryFn) _renderModalDictionaryFn(_modalEl._parsedRef, dictEl); }
    } else if (tab === 'crossrefs') {
      if (xrefsEl) {
        xrefsEl.removeAttribute('hidden');
        if (!xrefsEl._xrefsLoaded) {
          var _xVer = document.getElementById('bsw-modal-version');
          renderModalCrossRefsTab(_modalEl._parsedRef, xrefsEl,
            (_xVer && _xVer.value) ? _xVer.value : getVersion());
        }
      }
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
  var commEl  = _modalEl.querySelector('.bsw-modal__commentary-panel');
  var wsEl    = _modalEl.querySelector('.bsw-modal__wordstudy-panel');
  if (bodyEl)  bodyEl.removeAttribute('hidden');
  if (attrElR) attrElR.removeAttribute('hidden');
  if (splitEl) splitEl.removeAttribute('hidden');
  if (notesEl) { notesEl.setAttribute('hidden', ''); notesEl.innerHTML = ''; }
  if (commEl)  { commEl.setAttribute('hidden', '');  commEl._commentaryLoaded = false; }
  if (wsEl)    { wsEl.setAttribute('hidden', '');    wsEl._wsLoaded = false; }

  var topicsEl2 = _modalEl.querySelector('.bsw-modal__topics-panel');
  if (topicsEl2) { topicsEl2.setAttribute('hidden', ''); topicsEl2._topicsLoaded = false; }
  var confEl = _modalEl.querySelector('.bsw-modal__confessions-panel');
  if (confEl)  { confEl.setAttribute('hidden', '');  confEl._confLoaded = false; }
  var fathersPanelEl = _modalEl.querySelector('.bsw-modal__fathers-panel');
  if (fathersPanelEl) { fathersPanelEl.setAttribute('hidden', ''); fathersPanelEl._fathersLoaded = false; }
  var dictPanelEl = _modalEl.querySelector('.bsw-modal__dictionary-panel');
  if (dictPanelEl) { dictPanelEl.setAttribute('hidden', ''); dictPanelEl._dictLoaded = false; }
  var xrefsPanelEl = _modalEl.querySelector('.bsw-modal__crossrefs-panel');
  if (xrefsPanelEl) { xrefsPanelEl.setAttribute('hidden', ''); xrefsPanelEl._xrefsLoaded = false; }
  var copyQuoteReset = _modalEl.querySelector('.bsw-modal__copy-quote-btn');
  if (copyQuoteReset) { copyQuoteReset.setAttribute('hidden', ''); copyQuoteReset.textContent = 'Quote'; }
  var copyRefReset = _modalEl.querySelector('.bsw-modal__copy-ref-btn');
  if (copyRefReset) { copyRefReset.setAttribute('hidden', ''); copyRefReset.textContent = 'Reference'; }

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
    if (isSingleVerse) { vsLink.href = VERSE_STUDY_URL + '?ref=' + singleRef; vsLink.removeAttribute('hidden'); }
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
  var copyQuoteBtn = _modalEl.querySelector('.bsw-modal__copy-quote-btn');
  if (copyQuoteBtn) copyQuoteBtn.removeAttribute('hidden');
  var copyRefBtn = _modalEl.querySelector('.bsw-modal__copy-ref-btn');
  if (copyRefBtn) copyRefBtn.removeAttribute('hidden');
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
      attr.textContent = ATTRIBUTION[versionId] || '';
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

// ── renderCrossRefs ───────────────────────────────────────────────────────
export function renderCrossRefs(parsed, container) {
  if (!parsed) {
    container.innerHTML = '<p class="bsw-modal__xrefs-empty">No reference selected.</p>';
    return;
  }
  container._xrefLoaded = true;
  container.innerHTML = '<p class="bsw-modal__loading">Loading cross-references…</p>';
  var isSingle = !parsed.wholeChapter && (parsed.ch === parsed.endCh) && (parsed.v === parsed.endV);

  loadCrossRefs(parsed.bookId).then(function (data) {
    if (!data) {
      container.innerHTML = '<p class="bsw-modal__xrefs-empty">No cross-references available for this book.</p>';
      return;
    }
    var groups = [];
    for (var c = parsed.ch; c <= Math.min(parsed.endCh, parsed.ch + 4); c++) {
      var chData = data[String(c)];
      if (!chData) continue;
      var startV = (c === parsed.ch)   ? parsed.v   : 1;
      var stopV  = (c === parsed.endCh) ? Math.min(parsed.endV, 9999) : 9999;
      var keys   = Object.keys(chData).map(Number)
        .filter(function (n) { return n >= startV && n <= stopV; })
        .sort(function (a, b) { return a - b; });
      keys.forEach(function (vNum) {
        var rawRefs = chData[String(vNum)];
        if (!rawRefs || !rawRefs.length) return;
        var entries = rawRefs.map(parseCrossRefEntry);
        if (!isSingle) {
          entries.sort(function (a, b) { return b.votes - a.votes; });
          entries = entries.slice(0, XREF_CHAPTER_LIMIT);
        }
        entries.sort(_compareCanonical);
        groups.push({ ch: c, v: vNum, entries: entries });
      });
    }
    if (!groups.length) {
      container.innerHTML = '<p class="bsw-modal__xrefs-empty">No cross-references found for this passage.</p>';
      return;
    }
    var hasScores = groups.some(function (g) { return g.entries.some(function (e) { return e.votes > 1; }); });
    var html = '';
    groups.forEach(function (g) {
      if (!isSingle) {
        html += '<div class="bsw-modal__xref-verse-label">' + escHtml(parsed.bookName) + ' ' + g.ch + ':' + g.v + '</div>';
      }
      html += '<div class="bsw-modal__xref-list">';
      g.entries.forEach(function (entry) {
        var tierClass = '';
        if (hasScores) {
          tierClass = entry.votes >= 15 ? ' bsw-xref--high' : entry.votes >= 6 ? ' bsw-xref--med' : ' bsw-xref--low';
        }
        html += '<a class="bsw-modal__xref-link' + tierClass + '" data-ref="' + escHtml(entry.ref) + '" role="button" tabindex="0">' + escHtml(entry.ref) + '</a>';
      });
      html += '</div>';
    });
    container.innerHTML = html;
    container.querySelectorAll('.bsw-modal__xref-link').forEach(function (el) {
      var p = parseRef(el.getAttribute('data-ref'));
      if (p) wireRefEl(el, p);
    });
  }).catch(function () {
    container.innerHTML = '<p class="bsw-modal__xrefs-empty">Could not load cross-reference data.</p>';
  });
}

// ── renderModalCrossRefsTab ───────────────────────────────────────────────
export function renderModalCrossRefsTab(parsed, container, versionId) {
  container._xrefsLoaded = true;
  container.innerHTML = '<p class="bsw-modal__loading">Loading cross-references…</p>';
  var isSingle = !parsed.wholeChapter && parsed.ch === parsed.endCh && parsed.v === parsed.endV;

  loadCrossRefs(parsed.bookId).then(function (xdata) {
    if (!xdata) {
      container.innerHTML = '<p class="bsw-modal__xrefs-empty">No cross-references available for this book.</p>';
      return;
    }
    var allEntries = [];
    for (var c = parsed.ch; c <= Math.min(parsed.endCh, parsed.ch + 4); c++) {
      var chData = xdata[String(c)];
      if (!chData) continue;
      var startV = (c === parsed.ch)   ? parsed.v   : 1;
      var stopV  = (c === parsed.endCh) ? Math.min(parsed.endV, 9999) : 9999;
      Object.keys(chData).map(Number)
        .filter(function (n) { return n >= startV && n <= stopV; })
        .sort(function (a, b) { return a - b; })
        .forEach(function (vNum) {
          var rawRefs = chData[String(vNum)];
          if (!rawRefs || !rawRefs.length) return;
          var entries = rawRefs.map(parseCrossRefEntry);
          if (!isSingle) {
            entries.sort(function (a, b) { return b.votes - a.votes; });
            entries = entries.slice(0, XREF_CHAPTER_LIMIT);
          }
          entries.sort(_compareCanonical);
          entries.forEach(function (e) { allEntries.push(e); });
        });
    }
    if (!allEntries.length) {
      container.innerHTML = '<p class="bsw-modal__xrefs-empty">No cross-references found for this passage.</p>';
      return;
    }
    container.innerHTML =
      '<div class="bsw-modal__xref-tab-hdr">' + escHtml(parsed.display) + '</div>' +
      '<div class="bsw-modal__xref-tab-scroll"></div>';
    var scrollEl = container.querySelector('.bsw-modal__xref-tab-scroll');

    resolveVerses(parsed, versionId).then(function (srcVerses) {
      var srcText = srcVerses ? srcVerses.map(function (vr) { return vr.text; }).join(' — ') : '';
      var srcEl   = container.querySelector('.bsw-modal__xref-tab-hdr');
      if (srcEl && srcText) {
        srcEl.innerHTML = escHtml(parsed.display) +
          '<span class="bsw-modal__xref-tab-src-text">' + escHtml(srcText) + '</span>';
      }
    }).catch(function () {});

    allEntries.forEach(function (entry) {
      var p = parseRef(entry.ref);
      if (!p) return;
      var item     = document.createElement('div');
      item.className = 'bsw-modal__xref-tab-item';
      var refLabel = document.createElement('div');
      refLabel.className = 'bsw-modal__xref-tab-ref';
      refLabel.textContent = entry.ref;
      refLabel.setAttribute('role', 'button');
      refLabel.setAttribute('tabindex', '0');
      wireRefEl(refLabel, p);
      item.appendChild(refLabel);
      var textEl = document.createElement('div');
      textEl.className = 'bsw-modal__xref-tab-text';
      textEl.textContent = '…';
      item.appendChild(textEl);
      scrollEl.appendChild(item);
      resolveVerses(p, versionId).then(function (verses) {
        if (!verses || !verses.length) { textEl.textContent = ''; return; }
        // VM-G: prefix verse number when result spans multiple verses
        textEl.textContent = verses.length === 1
          ? verses[0].text
          : verses.map(function (vr) { return vr.verse + ' ' + vr.text; }).join(' ');
      }).catch(function () { textEl.textContent = ''; });
    });
  }).catch(function () {
    container.innerHTML = '<p class="bsw-modal__xrefs-empty">Could not load cross-reference data.</p>';
  });
}

// ── _buildCommPicker ──────────────────────────────────────────────────────
function _buildCommPicker(currentSrc) {
  var opts = COMMENTARY_SOURCES.map(function (s) {
    return '<option value="' + s.id + '"' + (s.id === currentSrc ? ' selected' : '') + '>' + s.label + '</option>';
  }).join('');
  return '<div class="bsw-modal__comm-picker">' +
    '<label class="bsw-modal__comm-label">Source:</label>' +
    '<select class="bsw-modal__comm-select">' + opts + '</select>' +
    '</div>';
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

// ── renderCommentary ──────────────────────────────────────────────────────
export function renderCommentary(parsed, container) {
  if (!parsed) {
    container.innerHTML = '<p class="bsw-modal__commentary-empty">No reference selected.</p>';
    return;
  }
  container._commentaryLoaded = true;

  function loadAndRender(src) {
    var bodyEl = container.querySelector('.bsw-modal__comm-body');
    if (bodyEl) bodyEl.innerHTML = '<p class="bsw-modal__loading">Loading commentary…</p>';
    loadCommentary(parsed.bookId, src).then(function (data) {
      var result  = _extractCommHtml(data, parsed, src); // VM-H: now returns { html, foundV }
      var bodyEl2 = container.querySelector('.bsw-modal__comm-body');
      if (!bodyEl2) return;
      if (!result.html) {
        bodyEl2.innerHTML = '<p class="bsw-modal__commentary-empty">No commentary found for this verse.</p>';
        return;
      }
      // VM-H: prepend muted notice when commentary is a section that includes, not targets, the verse
      var notice = '';
      if (!parsed.wholeChapter && result.foundV !== null && result.foundV !== parsed.v) {
        notice = '<p class="bsw-modal__comm-section-note">▸ This section covers verse ' + result.foundV + ' and following</p>';
      }
      bodyEl2.innerHTML = notice + result.html + '<p class="bsw-modal__commentary-attr">' + _commAttr(src) + '</p>';
      wireRefLinks(bodyEl2);
    }).catch(function () {
      var bodyEl3 = container.querySelector('.bsw-modal__comm-body');
      if (bodyEl3) bodyEl3.innerHTML = '<p class="bsw-modal__commentary-empty">Could not load commentary.</p>';
    });
  }

  container.innerHTML = _buildCommPicker(getCommentarySource()) +
    '<div class="bsw-modal__comm-body"><p class="bsw-modal__loading">Loading commentary…</p></div>';
  var sel = container.querySelector('.bsw-modal__comm-select');
  sel.addEventListener('change', function () {
    setCommentarySource(sel.value);
    loadAndRender(sel.value);
  });
  loadAndRender(getCommentarySource());
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

// ── _copyModalVerse ───────────────────────────────────────────────────────
function _copyModalVerse(btn, fmt) {
  var parsed  = _modalEl && _modalEl._parsedRef;
  if (!parsed) return;
  var body    = _modalEl.querySelector('.bsw-modal__body');
  var version = (document.getElementById('bsw-modal-version') || {}).value || getVersion();
  // VM-A: read from .bsw-modal__verse-text spans to skip verse-number sups and xref sups
  var textSpans = body ? body.querySelectorAll('.bsw-modal__verse-text') : [];
  var texts    = [];
  textSpans.forEach(function (el) {
    var t = el.textContent.trim();
    if (t) texts.push(t);
  });
  if (!texts.length) return;
  var text  = texts.join(' ');
  var ref   = parsed.display;
  var plain = '"' + text + '" — ' + ref + ' (' + version.toUpperCase() + ')';
  var toCopy = fmt === 'cite' ? (ref + ' (' + version.toUpperCase() + ')') : plain;
  var origLabel = btn.textContent;

  function _onCopied() {
    btn.textContent = 'Copied!';
    setTimeout(function () { btn.textContent = origLabel; }, 1800);
  }

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(toCopy).then(_onCopied).catch(function () {});
  } else {
    var ta = document.createElement('textarea');
    ta.value = toCopy; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    _onCopied();
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
    ctx.fillText('Bible Study', 60, 52);

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

export function _injectPrintBtn() {
  var browseBar = document.querySelector('.reader-browse-bar');
  if (!browseBar || document.getElementById('reader-print-btn')) return;
  var btn = document.createElement('button');
  btn.id        = 'reader-print-btn';
  btn.className = 'reader-print-btn';
  btn.title     = 'Print chapter';
  btn.setAttribute('aria-label', 'Print chapter');
  btn.textContent = '⎙ Print';
  btn.addEventListener('click', function () { window.print(); });
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
