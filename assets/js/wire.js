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
// Attaches all interactive behaviour to a single ref element:
//   hover/focus  → schedules the verse preview tooltip (300 ms delay)
//   blur/leave   → schedules tooltip hide (200 ms delay)
//   click/Enter  → cancels any pending tooltip and opens the full verse modal
// If the element is an <a>, its href is removed so it behaves as a button
// (prevents navigating away) while remaining keyboard accessible via tabindex.
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
// Finds all [data-ref] elements under root (defaults to document) and wires
// each one that hasn't already been wired (guarded by el._refWired flag).
// Called by app.js after initial page load, and by search.js after rendering
// results so ref links in search output are also interactive.
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
// Tags "Book Ch" and "Book Ch-Ch" patterns (whole-chapter refs) that don't
// have a verse number. These are linked as whole-chapter refs so the modal
// and tooltip show the chapter opening verses.
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
// Tags bare "Ch:V" patterns (e.g. "3:16") on pages where a specific book is
// implied by the page context (body[data-bible-book]).
// The bookId and bookName are supplied by autoTagRefs() after it reads data-bible-book.
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
// Tags "Chap. 3", "ch. 3", or "chapter 3" patterns on book-specific pages,
// linking them as whole-chapter refs using the page's implied book context.
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
// Called by the version-change callback in app.js whenever the user switches translations.
export function updateInlineVerses(versionId) {
  document.querySelectorAll('.bsw-verse[data-ref]').forEach(function (el) {
    populateInlineVerse(el, versionId);
  });
}

// ── applyHighlights ───────────────────────────────────────────────────────
// Reads highlight colours from stored notes (localStorage) and applies
// the corresponding bsw-hl-<colour> CSS class to each .reader-verse element.
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
