/* wire.js — Ref-link wiring, auto-tagging, highlights, bookmarks, inline verses.
 *
 * This module handles everything that turns static HTML into interactive
 * Bible-reference links. Its main responsibilities:
 *
 *   wireRefEl(el, parsed)      — attaches hover/click/keyboard behaviour to a
 *                                single element that already has a parsed ref.
 *   wireRefLinks(root)         — queries all [data-ref] elements under root and
 *                                calls wireRefEl on each unwired one.
 *   autoTagRefs()              — walks all text nodes in the document and wraps
 *                                recognised "Book Ch:V" patterns in clickable links.
 *   wireInlineVerses()         — populates .bsw-verse[data-ref] elements with live
 *                                verse text fetched from the current version.
 *   applyHighlights(container) — reads stored note highlights and applies colour
 *                                classes to reader verses.
 *   applyBookmarks(container)  — marks bookmarked verses with a CSS class.
 */
'use strict';

import {
  getVersion, parseRef, resolveVerses, normalizeBook, metaBooks, bookLookup, bookOrder,
  escHtml, callScheduleShow, callOpenModal
} from './core.js';
import { getNotes, getNote, saveNote, getBookmarks, isBookmarked, toggleBookmark } from './storage.js';
import { scheduleHide, cancelShow, hideTooltip } from './tooltip.js';

// ── wireRefEl ─────────────────────────────────────────────────────────────
// INTENT: Attach tooltip-on-hover + modal-on-click to one [data-ref] element.
//   <a> elements have their href stripped and get role="button" so they don't
//   navigate while remaining keyboard accessible. hover/focus → preview tooltip
//   via callScheduleShow; click/Enter → full verse modal via callOpenModal.
// CHANGE? callScheduleShow and callOpenModal are injected by app.js via
//   setTooltipFn / setModalFn (bottom of this file). If either registration
//   function is removed or renamed in app.js, all ref hover/click interactions
//   will silently do nothing. If tooltip delay constants change in tooltip.js,
//   the hover feel changes without any change here.
// VERIFY: Open any topic page → hover a ref link → preview tooltip appears after
//   ~300ms; click → verse modal opens. Keyboard: Tab to ref, press Enter → modal.
export function wireRefEl(el, parsed) {
  if (el.tagName === 'A') {
    el.removeAttribute('href');
    el.setAttribute('role', 'button');
    if (!el.getAttribute('tabindex')) el.setAttribute('tabindex', '0');
  }
  el.addEventListener('mouseenter', function () { callScheduleShow(el, parsed); });
  el.addEventListener('mouseleave', function () { scheduleHide(); });
  el.addEventListener('focus',      function () { callScheduleShow(el, parsed); });
  el.addEventListener('blur',       function () { scheduleHide(); });
  el.addEventListener('click', function (e) {
    e.preventDefault();
    cancelShow();
    hideTooltip();
    callOpenModal(parsed);
  });
  el.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      callOpenModal(parsed);
    }
  });
}

// ── wireRefLinks ──────────────────────────────────────────────────────────
// INTENT: Wire all unwired [data-ref] elements under root (defaults to document).
//   Uses el._refWired flag to make the call idempotent — safe to call again after
//   dynamic content injection (e.g. search results, modal verse lists).
// CHANGE? Called by app.js on initial page load AND by search.js after rendering
//   results. If search.js stops passing its results container as root, ref links
//   inside search results will lose interactivity. If the [data-ref] attribute
//   is renamed, update this querySelectorAll and the wireRefEl/autoTagRefs callers.
// VERIFY: Open /search/ → type a query → hover a ref link in results → tooltip shows.
//   Reload page → hovering original-page refs still works (not double-wired).
export function wireRefLinks(root) {
  var container = root || document;
  var els = container.querySelectorAll('[data-ref]');
  els.forEach(function (el) {
    if (el._refWired) return; // idempotent — skip already-wired elements
    el._refWired = true;
    var parsed = parseRef(el.dataset.ref);
    if (parsed) wireRefEl(el, parsed);
  });
}

// ── autoTagRefs ──────────────────────────────────────────────────────────
// INTENT: Walks all text nodes in the document body and turns plain-text Bible
//   references into clickable .ref links. The TreeWalker's acceptNode filter
//   skips any node already inside a [data-ref] element, so calling this function
//   more than once on the same page is safe — already-tagged nodes are never
//   double-wrapped. No-ops immediately if bookLookup is null (called before
//   books.json finishes loading); app.js re-calls after the books load.
// CHANGE? If the SKIP tag list changes, also audit autoTagChapterRefs which uses
//   the same skip set. If bookLookup's structure changes (currently an object keyed
//   by lowercase name), the parseRef() call inside this function will silently
//   produce null and skip the match rather than tagging it.
// VERIFY: Open any topic page; after books.json loads, plain text like "See John 3:16"
//   should become <a class="ref" data-ref="John 3:16">. Hovering shows the tooltip;
//   clicking opens the verse modal. Run autoTagRefs() a second time — no duplicate links.
// Walks all text nodes in the document body and turns plain-text Bible
// references (e.g. "See John 3:16") into clickable .ref links.
//
// Skips text inside script, style, code, pre, textarea, existing links/buttons,
// and anything already inside a .ref element or the tooltip/modal.
//
// After tagging "Book Ch:V" patterns, also handles:
//   - Continuation refs: "John 3:16, 17" → both verses become links.
//   - Chapter refs: "John 3" → whole-chapter link.
//   - Bare chapter mentions: "Chap. 3" or "ch. 3" on a book-specific page
//     (requires data-bible-book attribute on <body>).
export function autoTagRefs() {
  if (!bookLookup) return;

  // Matches "Book Ch:V" with optional verse range.
  var REF_RE = /\b((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+){0,3})\s+(\d+):(\d+)(?:[-–](?:(\d+):)?(\d+))?/g;
  // Tags to skip — we don't want to nest links or tag code samples.
  var SKIP   = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

  var walker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_TEXT,
    {
      acceptNode: function (node) {
        var el = node.parentElement;
        if (!el) return NodeFilter.FILTER_REJECT;
        if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
        // Don't tag inside existing ref links, the tooltip, or the modal backdrop.
        if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    }
  );

  var nodes = [];
  var n;
  while ((n = walker.nextNode())) { if (n.nodeValue.length > 4) nodes.push(n); }

  nodes.forEach(function (textNode) {
    var text = textNode.nodeValue;
    REF_RE.lastIndex = 0;
    if (!REF_RE.test(text)) return;
    REF_RE.lastIndex = 0;

    var parent = textNode.parentNode;
    var frag   = document.createDocumentFragment();
    var last   = 0;
    var m;

    while ((m = REF_RE.exec(text)) !== null) {
      var raw    = m[0].trim();
      var parsed = parseRef(raw);
      if (!parsed) continue;

      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      var a = document.createElement('a');
      a.className = 'ref';
      a.setAttribute('data-ref', raw);
      a.textContent = raw;
      wireRefEl(a, parsed);
      frag.appendChild(a);

      var contPos = m.index + m[0].length;
      var curCh   = parsed.ch;

      // Consume continuation references separated by commas/semicolons
      // (e.g. "John 3:16, 17, 18" — all three become links using the same book/chapter).
      for (;;) {
        var cm = text.slice(contPos).match(/^([,;]\s*)((?:(\d+):)?(\d+)(?:[-–](?:(\d+):)?(\d+))?)/);
        if (!cm) break;
        var ccCh = cm[3] ? parseInt(cm[3], 10) : curCh;
        var ccV  = parseInt(cm[4], 10);
        // If no explicit chapter and the next token looks like a new book name, stop.
        if (!cm[3]) { var after = text.slice(contPos + cm[0].length); if (/^\s+[A-Za-z]/.test(after)) break; }
        var cDataRef = parsed.bookName + ' ' + ccCh + ':' + ccV;
        if (cm[6]) cDataRef += '-' + (cm[5] ? cm[5] + ':' : '') + cm[6];
        var cParsed = parseRef(cDataRef);
        if (!cParsed) break;
        frag.appendChild(document.createTextNode(cm[1]));
        var ca = document.createElement('a');
        ca.className = 'ref'; ca.setAttribute('data-ref', cDataRef); ca.textContent = cm[2];
        wireRefEl(ca, cParsed);
        frag.appendChild(ca);
        if (cm[3]) curCh = ccCh;
        contPos += cm[0].length;
      }

      last = contPos;
      REF_RE.lastIndex = contPos;
    }

    if (last > 0) {
      if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      parent.replaceChild(frag, textNode);
    }
  });

  // On book-specific topic pages (data-bible-book on <body>), also tag bare
  // "3:16" and "Chap. 3" patterns using the page's book as implicit context.
  var pageBook = document.body && document.body.getAttribute('data-bible-book');
  if (pageBook) {
    var pbId   = normalizeBook(pageBook);
    var pbData = pbId && metaBooks && metaBooks.find(function (b) { return b.id === pbId; });
    if (pbData) {
      autoTagBareRefs(pbData.id, pbData.name);
      autoTagBareChapters(pbData.id, pbData.name);
    }
  }
  autoTagChapterRefs();
}

// ── autoTagChapterRefs ────────────────────────────────────────────────────
// INTENT: Same TreeWalker/SKIP-set pattern as autoTagRefs; tags "Book Ch" and
//   "Book Ch–Ch" whole-chapter patterns, excluding tokens followed by `:digit`
//   so "John 3:16" is never double-tagged. Called from autoTagRefs() after it
//   tags verse refs, so verse refs take priority and won't be re-walked.
// CHANGE? If bookLookup/metaBooks structure changes (field names, array format)
//   or if the SKIP set diverges from the one in autoTagRefs, both functions
//   break silently — they share the same SKIP list but are separate copies.
//   autoTagRefs() calls this at its end; removing that call silently disables
//   whole-chapter linking on all pages.
// VERIFY: Open any topic page (e.g. topics/gospel-of-john/) with plain
//   "Romans 5–8" text; after load it should become a clickable .ref link
//   that opens the modal to Romans 5.
export function autoTagChapterRefs() {
  if (!bookLookup || !metaBooks) return;
  // Matches "Genesis 1" or "Romans 5-8" but NOT "John 3:16" (the :16 excludes it).
  var BOOK_CH_RE = /\b((?:[1-4]\s+)?[A-Za-z]+(?:\s+[A-Za-z]+){0,3})\s+(\d+)(?:\s*[-–]\s*(\d+))?(?!\s*[:\d])/g;
  var SKIP = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      var el = node.parentElement;
      if (!el) return NodeFilter.FILTER_REJECT;
      if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
      if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  var nodes = []; var n;
  while ((n = walker.nextNode())) { if (n.nodeValue.length > 3) nodes.push(n); }

  nodes.forEach(function (textNode) {
    var text = textNode.nodeValue;
    BOOK_CH_RE.lastIndex = 0;
    var hasValid = false; var tm;
    while ((tm = BOOK_CH_RE.exec(text)) !== null) { if (normalizeBook(tm[1])) { hasValid = true; break; } }
    if (!hasValid) return;
    BOOK_CH_RE.lastIndex = 0;

    var parent = textNode.parentNode;
    var frag   = document.createDocumentFragment();
    var last   = 0;
    var curBookId = null, curBookName = null;
    var m;

    while ((m = BOOK_CH_RE.exec(text)) !== null) {
      var bookId = normalizeBook(m[1]);
      if (!bookId) continue;
      var bk       = metaBooks.find(function (b) { return b.id === bookId; });
      var ch       = parseInt(m[2], 10);
      var endCh    = m[3] ? parseInt(m[3], 10) : ch;
      var bookName = bk ? bk.name : m[1];
      var display  = bookName + ' ' + ch + (endCh !== ch ? '–' + endCh : '');
      var parsed   = { bookId: bookId, bookName: bookName, ch: ch, v: 1, endCh: endCh, endV: 9999, display: display, raw: display, wholeChapter: true };

      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      var a = document.createElement('a');
      a.className = 'ref'; a.setAttribute('data-ref', display); a.textContent = m[0].trim();
      wireRefEl(a, parsed);
      frag.appendChild(a);

      curBookId   = bookId; curBookName = bookName;
      var contPos = m.index + m[0].length;
      // Consume continuation chapter numbers (e.g. "Romans 5, 6, 7").
      for (;;) {
        var cm = text.slice(contPos).match(/^([,;]\s*)(\d+)(?!\s*[:\d])/);
        if (!cm) break;
        if (/^\s+[A-Za-z]/.test(text.slice(contPos + cm[0].length))) break;
        var nextCh  = parseInt(cm[2], 10);
        var cDisp   = curBookName + ' ' + nextCh;
        var cParsed = { bookId: curBookId, bookName: curBookName, ch: nextCh, v: 1, endCh: nextCh, endV: 9999, display: cDisp, raw: cDisp, wholeChapter: true };
        frag.appendChild(document.createTextNode(cm[1]));
        var ca = document.createElement('a');
        ca.className = 'ref'; ca.setAttribute('data-ref', cDisp); ca.textContent = cm[2];
        wireRefEl(ca, cParsed);
        frag.appendChild(ca);
        contPos += cm[0].length;
      }

      last = contPos;
      BOOK_CH_RE.lastIndex = contPos;
    }

    if (last > 0) {
      if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      parent.replaceChild(frag, textNode);
    }
  });
}

// ── autoTagBareRefs ───────────────────────────────────────────────────────
// INTENT: Tags bare "Ch:V" patterns (e.g. "3:16") on book-specific pages where
//   the book is implied by `body[data-bible-book]`. bookId and bookName are
//   resolved upstream by autoTagRefs() which passes them in after reading the
//   data attribute — this function is never called directly from outside wire.js.
// CHANGE? If data-bible-book handling in autoTagRefs() changes (attribute name,
//   lookup method), this function stops being called and bare refs go untagged
//   silently. This function is called nowhere else — verify by searching callers.
// VERIFY: Open a book-specific topic page (e.g. topics/gospel-of-john/) and
//   confirm "3:16" (without "John") auto-links to the modal for John 3:16.
export function autoTagBareRefs(bookId, bookName) {
  var BARE_RE = /\b(\d+):(\d+)(?:[-–](?:(\d+):)?(\d+))?/g;
  var SKIP    = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      var el = node.parentElement;
      if (!el) return NodeFilter.FILTER_REJECT;
      if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
      if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  var nodes = []; var n;
  while ((n = walker.nextNode())) { if (n.nodeValue.length > 2) nodes.push(n); }

  nodes.forEach(function (textNode) {
    var text = textNode.nodeValue;
    BARE_RE.lastIndex = 0;
    if (!BARE_RE.test(text)) return;
    BARE_RE.lastIndex = 0;

    var parent = textNode.parentNode;
    var frag   = document.createDocumentFragment();
    var last   = 0; var m;

    while ((m = BARE_RE.exec(text)) !== null) {
      var pCh = parseInt(m[1], 10), pV = parseInt(m[2], 10);
      var dataRef = bookName + ' ' + pCh + ':' + pV;
      if (m[4]) dataRef += '-' + (m[3] ? m[3] + ':' : '') + m[4];
      var parsed = parseRef(dataRef);
      if (!parsed) continue;

      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      var a = document.createElement('a');
      a.className = 'ref'; a.setAttribute('data-ref', dataRef); a.textContent = m[0];
      wireRefEl(a, parsed);
      frag.appendChild(a);

      var contPos = m.index + m[0].length;
      var curCh   = pCh;
      for (;;) {
        var cm = text.slice(contPos).match(/^([,;]\s*)((?:(\d+):)?(\d+)(?:[-–](?:(\d+):)?(\d+))?)/);
        if (!cm) break;
        var ccCh = cm[3] ? parseInt(cm[3], 10) : curCh;
        var ccV  = parseInt(cm[4], 10);
        if (!cm[3]) { var after = text.slice(contPos + cm[0].length); if (/^\s+[A-Za-z]/.test(after)) break; }
        var cDataRef = bookName + ' ' + ccCh + ':' + ccV;
        if (cm[6]) cDataRef += '-' + (cm[5] ? cm[5] + ':' : '') + cm[6];
        var cParsed = parseRef(cDataRef);
        if (!cParsed) break;
        frag.appendChild(document.createTextNode(cm[1]));
        var ca = document.createElement('a');
        ca.className = 'ref'; ca.setAttribute('data-ref', cDataRef); ca.textContent = cm[2];
        wireRefEl(ca, cParsed);
        frag.appendChild(ca);
        if (cm[3]) curCh = ccCh;
        contPos += cm[0].length;
      }

      last = contPos;
      BARE_RE.lastIndex = contPos;
    }

    if (last > 0) {
      if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      parent.replaceChild(frag, textNode);
    }
  });
}

// ── autoTagBareChapters ───────────────────────────────────────────────────
// INTENT: Tags "Chap. 3", "ch. 3", and "chapter 3" patterns on book-specific
//   pages, producing whole-chapter refs using the page's implied book. Called
//   in sequence after autoTagBareRefs() from within autoTagRefs() — the three
//   functions run in order: verse refs → bare "Ch:V" → chapter-word patterns.
// CHANGE? CHAP_RE only matches "Chap." / "ch." prefix forms; "Chapter 3" (capital
//   C followed by lowercase h) also matches via the [Cc] class — verify edge cases
//   if the regex is widened. Called only from autoTagRefs(); not exported for
//   external use.
// VERIFY: Open a book-specific topic page that has "chap. 1" or "Chap. 3" text;
//   confirm they become clickable whole-chapter .ref links after load.
export function autoTagBareChapters(bookId, bookName) {
  var CHAP_RE = /\b[Cc]hap?\.?\s*(\d+)(?:\s*[-–]\s*(\d+))?/g;
  var SKIP    = { script:1, style:1, code:1, pre:1, textarea:1, a:1, button:1, select:1, option:1, label:1 };

  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      var el = node.parentElement;
      if (!el) return NodeFilter.FILTER_REJECT;
      if (SKIP[el.tagName.toLowerCase()]) return NodeFilter.FILTER_REJECT;
      if (el.closest('[data-ref], .bsw-tooltip, .bsw-modal-backdrop')) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  var nodes = []; var n;
  while ((n = walker.nextNode())) { if (n.nodeValue.length > 2) nodes.push(n); }

  nodes.forEach(function (textNode) {
    var text = textNode.nodeValue;
    CHAP_RE.lastIndex = 0;
    if (!CHAP_RE.test(text)) return;
    CHAP_RE.lastIndex = 0;

    var parent = textNode.parentNode;
    var frag   = document.createDocumentFragment();
    var last   = 0; var m;

    while ((m = CHAP_RE.exec(text)) !== null) {
      var startCh = parseInt(m[1], 10);
      var endCh   = m[2] ? parseInt(m[2], 10) : startCh;
      var display = bookName + ' ' + startCh + (endCh !== startCh ? '–' + endCh : '');
      var parsed  = { bookId: bookId, bookName: bookName, ch: startCh, v: 1, endCh: endCh, endV: 9999, display: display, raw: display, wholeChapter: true };

      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      var a = document.createElement('a');
      a.className = 'ref'; a.setAttribute('data-ref', display); a.textContent = m[0];
      wireRefEl(a, parsed);
      frag.appendChild(a);
      last = m.index + m[0].length;
    }

    if (last > 0) {
      if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      parent.replaceChild(frag, textNode);
    }
  });
}

// ── wireInlineVerses / populateInlineVerse / updateInlineVerses ──────────
// wireInlineVerses: finds all .bsw-verse[data-ref] elements and populates them
// with live verse text. Used on topic pages and the home page to embed verses
// inline in content without hardcoding translation text.
// The element must have a valid data-ref attribute (e.g. data-ref="John 1:1").
// INTENT: Populate all .bsw-verse[data-ref] elements on page load with live verse
//   text from the user's current Bible version. Called once by app.js after
//   core data is ready; updateInlineVerses handles subsequent version changes.
// CHANGE? getVersion() reads bsw_version from localStorage (storage.js). If the
//   storage key changes, inline verses will silently default to the fallback version.
//   Also called implicitly via onVersionChange → updateInlineVerses (app.js).
// VERIFY: Load a topic page with `<span class="bsw-verse" data-ref="John 3:16">`.
//   The verse text should populate in the user's current version within ~1 second.
export function wireInlineVerses() {
  var els = document.querySelectorAll('.bsw-verse[data-ref]');
  if (!els.length) return;
  var version = getVersion();
  els.forEach(function (el) { populateInlineVerse(el, version); });
}

// populateInlineVerse: fetches and renders the verse text into a single .bsw-verse element.
// Shows a loading state via the bsw-verse--loading class while fetching.
export function populateInlineVerse(el, versionId) {
  var parsed = parseRef(el.getAttribute('data-ref'));
  if (!parsed) return;
  el.classList.add('bsw-verse--loading');
  resolveVerses(parsed, versionId).then(function (verses) {
    el.classList.remove('bsw-verse--loading');
    if (!verses || !verses.length) return;
    el.innerHTML = verses.map(function (vr) {
      return '<sup class="bsw-verse__num">' + vr.verse + '</sup>' +
             '<span class="bsw-verse__text">' + escHtml(vr.text) + '</span>';
    }).join(' ');
  }).catch(function () { el.classList.remove('bsw-verse--loading'); });
}

// updateInlineVerses: re-populates all inline verse elements with a new version.
// CHANGE? This function is wired as a version-change subscriber in app.js:
//   onVersionChange(updateInlineVerses)  — if that line is removed, version switches
//   will stop updating .bsw-verse embeds on every page. Inline verses also rely on
//   populateInlineVerse fetching from the DATA_CACHE_V path; if the data URL shape
//   changes in core.js, cached responses will serve stale content until sw.js is rebumped.
// Called by the version-change callback in app.js whenever the user switches translations.
export function updateInlineVerses(versionId) {
  document.querySelectorAll('.bsw-verse[data-ref]').forEach(function (el) {
    populateInlineVerse(el, versionId);
  });
}

// ── applyHighlights ───────────────────────────────────────────────────────
// Reads highlight colours from stored notes (localStorage) and applies
// the corresponding bsw-hl-<colour> CSS class to each .reader-verse element.
// CHANGE? Callers that must be updated if the note data format or CSS class prefix changes:
//   reader.js:doLookup — called after chapter verses are rendered
//   reader.js:injectComparePanel — called after the compare panel's secondary verses load
//   modal.js:applyModalHighlights — targets .bsw-modal__verse elements (separate class prefix)
//   Highlight colour is read from note.highlight (string or false); if that field is
//   renamed in storage.js, all three call sites silently lose their highlight colours.
//   CSS class pattern is "reader-verse--hl-<colour>"; if renamed, also update applyModalHighlights
//   which uses the different prefix "bsw-hl-<colour>".
// Called by the reader page after verses are rendered and after the user
// changes a highlight colour in the modal.
export function applyHighlights(container) {
  if (!container) return;
  container.querySelectorAll('.reader-verse[data-book][data-ch][data-v]').forEach(function (el) {
    var book = el.getAttribute('data-book');
    var ch   = el.getAttribute('data-ch');
    var v    = el.getAttribute('data-v');
    var ref  = book + ' ' + ch + ':' + v;
    var note = getNote(ref);
    var hl   = note && note.highlight;
    // Strip any existing highlight class before applying the current one.
    el.className = el.className.replace(/\breader-verse--hl-\S+/g, '').trim();
    if (hl && hl !== false) el.classList.add('reader-verse--hl-' + hl);
  });
}

// ── applyModalHighlights ──────────────────────────────────────────────────
// Same as applyHighlights but targets .bsw-modal__verse elements inside the
// open verse modal so highlights are visible while the modal is open.
// CHANGE? CSS class prefix divergence: this function applies `bsw-hl-{colour}`
//   to `.bsw-modal__verse` elements; applyHighlights() applies
//   `reader-verse--hl-{colour}` to `.reader-verse` elements — the two prefixes
//   must not be swapped. Callers: modal.js:_renderModalVerseTab (on render) and
//   modal.js:_switchTab (on tab change). If the modal verse element class name
//   `.bsw-modal__verse` or the CSS prefix `bsw-hl-` is renamed, update both
//   here and in those two callers.
export function applyModalHighlights(bodyEl, parsed) {
  if (!bodyEl || !parsed) return;
  bodyEl.querySelectorAll('.bsw-modal__verse[data-ch][data-v]').forEach(function (el) {
    var ch  = el.getAttribute('data-ch');
    var v   = el.getAttribute('data-v');
    var ref = parsed.bookName + ' ' + ch + ':' + v;
    var note = getNote(ref);
    var hl   = note && note.highlight;
    el.className = el.className.replace(/\bbsw-hl-\S+/g, '').trim();
    if (hl && hl !== false) el.classList.add('bsw-hl-' + hl);
  });
}

// ── applyBookmarks ────────────────────────────────────────────────────────
// Adds/removes the reader-verse--bookmarked class on each verse element based
// on the current bookmarks stored in localStorage. Called after the reader
// renders verses and whenever a bookmark is toggled.
// CHANGE? Callers: reader.js:doLookup (after each render) and
//   reader.js:injectComparePanel (after compare panel renders). If isBookmarked()
//   in storage.js changes its ref key format (currently "Book Ch:V" string), or
//   if the class name `reader-verse__num--bookmarked` is renamed in reader.css,
//   both call sites silently show no bookmark state with no JS error.
// INTENT: Scan all .reader-verse elements in container and toggle the
//   .reader-verse__num--bookmarked CSS class to match the current bookmark set
//   (read from localStorage via isBookmarked). Called by reader.js after each
//   chapter render so the star indicator stays in sync without a full re-render.
// CHANGE? If the bookmark storage key (bsw_bookmarks in storage.js) changes, or
//   if isBookmarked() signature changes, update the call here. If the verse
//   data attributes (data-book, data-ch, data-v) are renamed in reader.js
//   templates, update the querySelectorAll selector and attribute reads.
// VERIFY: In the reader, bookmark a verse → verse number shows a star glyph.
//   Navigate to another chapter and back → star persists. Unbookmark → star disappears.
export function applyBookmarks(container) {
  if (!container) return;
  container.querySelectorAll('.reader-verse[data-book][data-ch][data-v]').forEach(function (el) {
    var book = el.getAttribute('data-book');
    var ch   = el.getAttribute('data-ch');
    var v    = el.getAttribute('data-v');
    var ref  = book + ' ' + ch + ':' + v;
    // Bookmark star renders on the verse-number sup, not the verse span itself.
    var numEl = el.querySelector('.reader-verse__num');
    if (numEl) numEl.classList.toggle('reader-verse__num--bookmarked', isBookmarked(ref));
  });
}
