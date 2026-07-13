/* reader-wordtap.js — tap a word in scripture, get its lexeme (Heights audit
 * fix E, with H riding along).
 *
 * The verse modal gave verses the noun-hub treatment; this gives it to words.
 * Tapping a plain word in the reader opens a compact popover anchored at the
 * tap: the word, its Strong's lemma / transliteration / gloss (resolved by
 * matching the word against the verse's interlinear tokens), and actions —
 * open the full word study in the study desk (window.bswStudyDesk, the same
 * deep link interlinear.js uses), search all occurrences, and, when the word
 * names a Biblepedia article (people, places), read the article.
 *
 * Deliberately defers to every existing tap surface: refs, terms, places,
 * echo markers, verse numbers, and the interlinear view (which owns word taps
 * when active) are all excluded before this fires.
 */
'use strict';

import { loadInterlinear, loadStrongs, escHtml } from './core.js';
import { loadBPLite, loadBPTag } from './bp-lite.js';
import { _HL_COLORS, getNote, toggleHighlight } from './storage.js';
import { applyHighlights } from './wire.js';

var _pop = null;

function _navState() {
  return (typeof window !== 'undefined' && window._readerNavState) || null;
}

// ── Word extraction at the tap point ───────────────────────────────────────
function _wordAtPoint(x, y) {
  var pos = null;
  if (document.caretPositionFromPoint) {
    var cp = document.caretPositionFromPoint(x, y);
    if (cp && cp.offsetNode && cp.offsetNode.nodeType === 3) pos = { node: cp.offsetNode, offset: cp.offset };
  } else if (document.caretRangeFromPoint) {
    var cr = document.caretRangeFromPoint(x, y);
    if (cr && cr.startContainer && cr.startContainer.nodeType === 3) pos = { node: cr.startContainer, offset: cr.startOffset };
  }
  if (!pos) return null;
  var text = pos.node.textContent;
  var isWordCh = function (c) { return /[A-Za-z’']/.test(c); };
  var a = pos.offset, b = pos.offset;
  while (a > 0 && isWordCh(text[a - 1])) a--;
  while (b < text.length && isWordCh(text[b])) b++;
  var word = text.slice(a, b).replace(/[’']s$/, '').replace(/^[’']|[’']$/g, '');
  return word.length >= 2 ? word : null;
}

// ── Interlinear token match: which Strong's code covers this English word ──
function _matchToken(tokens, word) {
  var w = word.toLowerCase();
  var re = new RegExp('(^|[^a-z])' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '([^a-z]|$)', 'i');
  for (var i = 0; i < tokens.length; i++) {
    if (tokens[i].s && re.test(String(tokens[i].text || '').toLowerCase())) return tokens[i];
  }
  return null;
}

// ── Popover ────────────────────────────────────────────────────────────────
function _closePopover() {
  if (_pop) { _pop.remove(); _pop = null; }
  document.removeEventListener('click', _onDocClick, true);
  document.removeEventListener('keydown', _onKeydown, true);
}
function _onDocClick(e) { if (_pop && !_pop.contains(e.target)) _closePopover(); }
function _onKeydown(e) { if (e.key === 'Escape') _closePopover(); }

function _showPopover(word, rect) {
  _closePopover();
  _pop = document.createElement('div');
  _pop.className = 'bsw-wordtap';
  _pop.setAttribute('role', 'dialog');
  _pop.setAttribute('aria-label', 'Word study: ' + word);
  _pop.innerHTML =
    '<div class="bsw-wordtap__word">' + escHtml(word) + '</div>' +
    '<div class="bsw-wordtap__lex"><span class="bsw-wordtap__dim">Looking up…</span></div>' +
    '<div class="bsw-wordtap__actions"></div>';
  document.body.appendChild(_pop);
  var top  = window.scrollY + rect.bottom + 8;
  var left = Math.max(8, Math.min(window.scrollX + rect.left, window.scrollX + window.innerWidth - _pop.offsetWidth - 8));
  _pop.style.top = top + 'px';
  _pop.style.left = left + 'px';
  setTimeout(function () {
    document.addEventListener('click', _onDocClick, true);
    document.addEventListener('keydown', _onKeydown, true);
  }, 0);
  return _pop;
}

function _addAction(pop, label, onClick, href) {
  var row = pop.querySelector('.bsw-wordtap__actions');
  var el = document.createElement(href ? 'a' : 'button');
  el.className = 'bsw-wordtap__action';
  el.textContent = label;
  if (href) el.href = href; else { el.type = 'button'; el.addEventListener('click', onClick); }
  row.appendChild(el);
}

// ── Lookups ────────────────────────────────────────────────────────────────
function _fillLexeme(pop, word, verse) {
  var nav = _navState();
  var done = function (html) {
    var lex = pop && pop.querySelector('.bsw-wordtap__lex');
    if (lex) lex.innerHTML = html;
  };
  var fallback = function () {
    done('<span class="bsw-wordtap__dim">No original-language token matched — try the occurrence search.</span>');
  };
  if (!nav || !nav.bookId || !nav.ch || !verse) { fallback(); return; }
  loadInterlinear(nav.bookId).then(function (data) {
    var tokens = data && data[String(nav.ch)] && data[String(nav.ch)][String(verse)];
    var tok = tokens && _matchToken(tokens, word);
    if (!tok) { fallback(); return; }
    var testament = tok.s.charAt(0) === 'H' ? 'hebrew' : 'greek';
    loadStrongs(testament).then(function (dict) {
      if (!_pop || _pop !== pop) return;
      var entry = dict && dict[tok.s];
      if (!entry) { fallback(); return; }
      done(
        '<span class="bsw-wordtap__lemma">' + escHtml(entry.lemma || '') + '</span>' +
        (entry.translit ? ' <span class="bsw-wordtap__translit">' + escHtml(entry.translit) + '</span>' : '') +
        ' <span class="bsw-wordtap__code">' + escHtml(tok.s) + '</span>' +
        '<div class="bsw-wordtap__gloss">' + escHtml(String(entry.gloss || entry.def || '').split(';')[0]) + '</div>'
      );
      if (window.bswStudyDesk) {
        _addAction(pop, 'Full word study', function () {
          _closePopover();
          window.bswStudyDesk.open();
          window.bswStudyDesk.showWord(tok.s);
        });
      }
    }).catch(fallback);
  }).catch(fallback);
}

function _fillArticle(pop, word, termKey) {
  loadBPTag().then(function (idx) {
    if (!_pop || _pop !== pop || !idx) return;
    var k = (termKey || word).toLowerCase();
    var hit = idx.find(function (a) {
      return a.id === k || String(a.term || '').toLowerCase() === k;
    });
    if (!hit) return;
    // A merged alias (redirect set, no article of its own) borrows its
    // canonical entry's brief and article — same contract terms.js honors.
    var entry = hit.redirect ? (idx.find(function (a) { return a.id === hit.redirect; }) || hit) : hit;
    if (entry.has_article !== false && /^[a-z0-9.-]+$/.test(entry.id)) {
      _addAction(pop, 'Read the ' + (entry.term || word) + ' article', null, '/biblepedia/' + entry.id + '/');
    }
    // The tag index has no prose — fetch the brief-carrying index for the blurb.
    loadBPLite().then(function (full) {
      if (!_pop || _pop !== pop || !full) return;
      var fe = full.find(function (a) { return a.id === entry.id; });
      if (fe && fe.brief) {
        var b = document.createElement('div');
        b.className = 'bsw-wordtap__brief';
        b.textContent = fe.brief;
        pop.insertBefore(b, pop.querySelector('.bsw-wordtap__actions'));
      }
    }).catch(function () {});
  }).catch(function () {});
}

// ── Verse highlight row ─────────────────────────────────────────────────────
// The verse-text tap used to open reader.js's standalone highlight picker;
// this popover now owns that gesture (the tap stops propagating below), so it
// carries the swatch row too — same storage, same .bsw-hl-swatch classes the
// verse modal's Notes tab uses. Highlighting stays two taps: verse, swatch.
function _addHighlightRow(pop, verseEl, ref) {
  var row = document.createElement('div');
  row.className = 'bsw-wordtap__hl';
  var lbl = document.createElement('span');
  lbl.className = 'bsw-hl-label';
  lbl.textContent = 'Highlight verse:';
  row.appendChild(lbl);
  var note = getNote(ref);
  var cur = note && note.highlight;
  if (cur === true) cur = 'yellow';
  var refresh = function (active) {
    row.querySelectorAll('.bsw-hl-swatch[data-c]').forEach(function (s) {
      s.classList.toggle('bsw-hl-swatch--active', !!(active && s.getAttribute('data-c') === active));
    });
  };
  _HL_COLORS.forEach(function (c) {
    var sw = document.createElement('button');
    sw.type = 'button';
    sw.className = 'bsw-hl-swatch bsw-hl-swatch--' + c + (cur === c ? ' bsw-hl-swatch--active' : '');
    sw.title = c.charAt(0).toUpperCase() + c.slice(1) + ' highlight';
    sw.setAttribute('aria-label', 'Highlight ' + c);
    sw.setAttribute('data-c', c);
    sw.addEventListener('click', function () {
      refresh(toggleHighlight(ref, c));
      applyHighlights(verseEl.closest('#reader-results') || verseEl.parentElement);
    });
    row.appendChild(sw);
  });
  pop.appendChild(row);
}

// ── Init ───────────────────────────────────────────────────────────────────
// Shared popover assembly for both entry paths (tap, and the keyboard
// selection + W shortcut).
function _openWordPopover(word, termKey, verseEl, rect) {
  document.querySelectorAll('.reader-hl-picker').forEach(function (p) { p.hidden = true; });
  var book = verseEl && verseEl.getAttribute('data-book');
  var ch   = verseEl && verseEl.getAttribute('data-ch');
  var v    = verseEl && verseEl.getAttribute('data-v');
  var numEl = verseEl && verseEl.querySelector('.reader-verse__num');
  var verse = v ? parseInt(v, 10) : (numEl ? parseInt(numEl.textContent, 10) : null);

  var pop = _showPopover(word, rect);
  _addAction(pop, 'All occurrences', null, '/search/?q=' + encodeURIComponent(word.toLowerCase()));
  if (verse) _fillLexeme(pop, word, verse);
  else { var lexEl = pop.querySelector('.bsw-wordtap__lex'); if (lexEl) lexEl.remove(); }
  _fillArticle(pop, word, termKey);
  if (book && ch && v) _addHighlightRow(pop, verseEl, book + ' ' + ch + ':' + v);
}

export function initWordTap() {
  var results = document.getElementById('reader-results');
  if (!results) return;

  // Keyboard path (a11y): select a word — Shift+arrows works without a
  // pointer — and press W. Documented in the reader shortcuts overlay.
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'w' && e.key !== 'W') return;
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
    var sel = window.getSelection && window.getSelection();
    if (!sel || sel.isCollapsed || !sel.anchorNode || !results.contains(sel.anchorNode)) return;
    var word = String(sel.toString()).trim().split(/\s+/)[0].replace(/^[^A-Za-z’']+|[^A-Za-z’']+$/g, '');
    if (!word || word.length < 2) return;
    var rc = sel.getRangeAt(0).getBoundingClientRect();
    var anchorEl = sel.anchorNode.nodeType === 3 ? sel.anchorNode.parentElement : sel.anchorNode;
    e.preventDefault();
    _openWordPopover(word, null, anchorEl && anchorEl.closest('.reader-verse'), { left: rc.left, bottom: rc.bottom });
  });

  // Capture phase: reader.js's wireVerseTextHighlight listens on each verse
  // and stops propagation, so a bubble-phase listener here never fires. When
  // a word IS under the tap we stop propagation ourselves — this popover
  // (which includes the highlight row) replaces the standalone picker for
  // that tap; whitespace taps fall through to the picker unchanged.
  results.addEventListener('click', function (e) {
    // Term-links (biblepedia highlighted words) are hover-only spans — no tap
    // behavior of their own — so the popover takes their taps too, seeded
    // with the term key for an exact article match.
    var termEl = e.target.closest('.term-link');
    // Defer to every other existing interactive surface.
    if (!termEl &&
        e.target.closest('a, button, select, input, sup, [data-ref], .map-place, ' +
                         '.reader-echo-marker, .reader-verse__num, .reader-xref-note, [class*="il-"]')) return;
    var verseEl = e.target.closest('.reader-verse');
    if (!verseEl && !termEl) return;
    // The interlinear view owns word taps when active.
    var ilBtn = document.getElementById('reader-interlinear-btn');
    if (ilBtn && ilBtn.getAttribute('aria-pressed') === 'true') return;
    // Don't hijack text selection.
    var sel = window.getSelection && window.getSelection();
    if (sel && !sel.isCollapsed) return;

    var word, termKey = null;
    if (termEl) {
      word = termEl.textContent.trim();
      termKey = (termEl.dataset.termKey || word).toLowerCase();
      // terms.js is already loaded (it created the tag), so this resolves from
      // cache — cancel its pending tooltip before it can cover the popover.
      import('./terms.js').then(function (m) { m.hideTermTip(); }).catch(function () {});
    } else {
      word = _wordAtPoint(e.clientX, e.clientY);
    }
    if (!word) { _closePopover(); return; }

    e.stopPropagation();
    _openWordPopover(word, termKey, verseEl, { left: e.clientX, bottom: e.clientY + 4 });
  }, true);
}
