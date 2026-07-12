/* terms.js — Term hover tooltip system (site-wide noun/concept linking)
 *
 * Loads data/biblepedia/index.json (single fetch replacing 4 separate source indexes)
 * to power .term-link hover tooltips. All links resolve to /biblepedia/.
 */
'use strict';

import { escHtml, _resolve } from './core.js';
import { wireRefLinks } from './wire.js';
import { BIBLEPEDIA_URL } from './library.js';

var BP_IDX_URL = _resolve('../../data/biblepedia/index.json');

var _termTipEl     = null;
var _termTipTimer  = null;
var _termTipHide   = null;
var _termMap2      = null;
var _termById      = null;   // id -> entry, for resolving alias redirects to their canonical
var _termMapReady  = null;
var _termMultiRe   = null;
var _termSingleSet = null;

export function getTermMap2() { return _termMap2; }

function _buildTermTooltipDOM() {
  if (_termTipEl) return;
  var el = document.createElement('div');
  el.id        = 'bsw-term-tooltip';
  el.className = 'bsw-term-tooltip';
  el.setAttribute('aria-hidden', 'true');
  document.body.appendChild(el);
  _termTipEl = el;
  el.addEventListener('mouseenter', function () { cancelTermHide(); });
  el.addEventListener('mouseleave', function () { _scheduleTermHide(); });
}

function _scheduleTermShow(anchor, key) {
  cancelTermHide();
  if (_termTipTimer) clearTimeout(_termTipTimer);
  _termTipTimer = setTimeout(function () { _showTermTip(anchor, key); }, 250);
}

function _scheduleTermHide() {
  if (_termTipTimer) { clearTimeout(_termTipTimer); _termTipTimer = null; }
  _termTipHide = setTimeout(function () { _hideTermTip(); }, 180);
}

export function cancelTermHide() {
  if (_termTipHide) { clearTimeout(_termTipHide); _termTipHide = null; }
}

function _hideTermTip() {
  if (_termTipEl) {
    _termTipEl.classList.remove('bsw-term-tooltip--visible');
    _termTipEl.setAttribute('aria-hidden', 'true');
  }
}

// For the reader's word-tap popover, which takes over term taps: cancels any
// pending show (a tap fires mouseenter first, arming the 250ms timer) and
// hides the tooltip so it can't appear over the popover.
export function hideTermTip() {
  if (_termTipTimer) { clearTimeout(_termTipTimer); _termTipTimer = null; }
  _hideTermTip();
}

function _positionTermTip(anchor) {
  if (!_termTipEl) return;
  var r  = anchor.getBoundingClientRect();
  var tt = _termTipEl.getBoundingClientRect();
  var vw = window.innerWidth;
  var vh = window.innerHeight;
  var top  = r.bottom + 8;
  var left = r.left;
  if (top + tt.height > vh - 8)  top  = r.top - tt.height - 8;
  if (left + tt.width > vw - 8)  left = vw - tt.width - 8;
  if (left < 8) left = 8;
  _termTipEl.style.top  = top  + 'px';
  _termTipEl.style.left = left + 'px';
}

// Returns true when two term strings contain the same set of significant words
// (case-insensitive, ignoring punctuation and the joiners "of"/"the"), i.e. one is a
// reordering of the other. Used to hide a redundant "(aka …)" for forward place aliases.
function _sameWordSet(a, b) {
  function sig(s) {
    return s.toLowerCase().split(/[^a-z]+/).filter(function (w) {
      return w && w !== 'of' && w !== 'the';
    }).sort().join(' ');
  }
  return sig(a) === sig(b);
}

function _srcLabel(entry) {
  // AUD-22: cover every category the index emits (incl. singular variants and the
  // event/father/commentator categories) so the tooltip source label is never blank.
  switch (entry.category) {
    case 'people':                 return 'Person';
    case 'places':  case 'place':  return 'Place';
    case 'concepts': case 'concept': return 'Concept';
    case 'names':   case 'name':   return 'Name';
    case 'events':  case 'event':  return 'Event';
    case 'father':                 return 'Church Father';
    case 'commentator':            return 'Commentator';
    default:                       return '';
  }
}

function _showTermTip(anchor, key) {
  _buildTermTooltipDOM();
  var entry = _termMap2 && _termMap2[key];
  if (!entry) return;

  // INTENT: A merged alias (entry.redirect set, has_article:false) carries no article of its
  //   own — pull the tooltip's details (brief, name-meaning, Biblepedia link) from the CANONICAL
  //   article, while keeping the hovered alias word as the heading with an "(aka Canonical)" tag.
  // CHANGE? Relies on _termById built in _loadTermMap and the redirect contract in
  //   data/biblepedia/merges.json; same behaviour as _akaHtml/_showArticle in biblepedia.js.
  // VERIFY: Hover "Calvary" anywhere in prose — tooltip heads "Calvary (aka Golgotha)", shows
  //   Golgotha's brief, and the "Biblepedia →" link opens ?a=golgotha.
  var hovered = entry;
  if (entry.redirect && _termById && _termById[entry.redirect]) {
    entry = _termById[entry.redirect];
  }
  // INTENT: Suppress the "(aka …)" tag when the hovered alias is merely a word-reordering
  //   of the canonical term — e.g. the forward place alias "Mount of Olives" redirecting to
  //   the inverted dictionary headword "Olives, Mount of". Showing "(aka Olives, Mount of)"
  //   there is noise; a genuinely different synonym (e.g. "Calvary" → "Golgotha") still shows.
  // VERIFY: Hover "Mount of Olives" in a chapter — heading reads "Mount of Olives" with no aka;
  //   hover "Mount Zion" — heading "Mount Zion (aka Zion)" still shows the real canonical.
  var akaHtml = (entry !== hovered && !_sameWordSet(hovered.term, entry.term))
    ? ' <span class="bsw-term-tooltip__aka">(aka ' + escHtml(entry.term) + ')</span>'
    : '';

  var html =
    '<div class="bsw-term-tooltip__head">' +
      '<span class="bsw-term-tooltip__term">' + escHtml(hovered.term) + akaHtml + '</span>' +
      '<span class="bsw-term-tooltip__src">' + escHtml(_srcLabel(entry)) + '</span>' +
    '</div>' +
    '<div class="bsw-term-tooltip__body">';

  if (entry.brief) {
    html += '<p class="bsw-term-tooltip__brief">' + escHtml(entry.brief) + '</p>';
  }

  if (entry.hitchcock_meaning) {
    html += '<p class="bsw-term-tooltip__hitch">' +
      '<span class="bsw-term-tooltip__hitch-label">Name: </span>' +
      escHtml(entry.hitchcock_meaning) + '</p>';
  }

  html += '<div class="bsw-term-tooltip__links">';
  if (entry.has_article) {
    html += '<a class="bsw-term-tooltip__link" href="' +
      escHtml(BIBLEPEDIA_URL + '?a=' + encodeURIComponent(entry.id)) +
      '">Biblepedia &#x2192;</a>';
  }
  html += '</div></div>';

  _termTipEl.innerHTML = html;
  _termTipEl.classList.add('bsw-term-tooltip--visible');
  _termTipEl.setAttribute('aria-hidden', 'false');
  _positionTermTip(anchor);
}

// INTENT: Guard against loading the ~2MB BP index on pages with no taggable content.
// The index replaces 4 separate source fetches (Easton's, Smith's, Hitchcock's, Nave's).
// Only articles with has_article:true are used for the multi-word regex to avoid bloating
// the pattern with 2,000+ Nave-only stub phrases that rarely appear in prose.
function _loadTermMap() {
  if (_termMap2) return Promise.resolve(_termMap2);
  if (_termMapReady) return _termMapReady;
  _termMapReady = fetch(BP_IDX_URL)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
    .then(function (data) {
      var map = {};
      var byId = {};

      data.forEach(function (entry) {
        var k = entry.term.toLowerCase();
        if (!map[k]) map[k] = entry;
        byId[entry.id] = entry;
      });

      _termMap2 = map;
      _termById = byId;

      // Multi-word regex: full-article entries PLUS alias redirect pointers (so a merged
      // alias name like "Judas, the Lord's Brother" still tags and routes to its canonical).
      var multiKeys = Object.keys(map).filter(function (k) {
        return k.indexOf(' ') >= 0 && k.length >= 4 && (map[k].has_article || map[k].redirect);
      }).sort(function (a, b) { return b.length - a.length; });

      if (multiKeys.length) {
        var escaped = multiKeys.map(function (k) {
          return k.replace(/[-[\]{}()*+?.,\\^$|#]/g, '\\$&');
        });
        try {
          _termMultiRe = new RegExp('\\b(' + escaped.join('|') + ')\\b', 'gi');
        } catch (e) {
          _termMultiRe = null;
        }
      }

      _termSingleSet = new Set(Object.keys(map).filter(function (k) {
        return k.indexOf(' ') < 0 && k.length >= 3;
      }));

      return map;
    })
    .catch(function () {
      // UX-18: a failed index fetch must resolve to an empty map (not reject) so callers'
      // .then() chains run harmlessly and don't raise an unhandled rejection; term tagging
      // simply does nothing this load.
      _termMap2      = {};
      _termMultiRe   = null;
      _termSingleSet = new Set();
      return _termMap2;
    });
  return _termMapReady;
}

function _wireTermEl(el) {
  if (el._termWired) return;
  el._termWired = true;
  var key = (el.dataset.termKey || el.textContent || '').toLowerCase().trim();
  el.addEventListener('mouseenter', function () { _scheduleTermShow(el, key); });
  el.addEventListener('mouseleave', function () { _scheduleTermHide(); });
  el.addEventListener('click', function () {
    if (_termTipEl && _termTipEl.classList.contains('bsw-term-tooltip--visible')) {
      _hideTermTip();
    }
  });
}

export function autoTagTerms(root) {
  if (!_termMap2) return;
  if (!root) return;
  if (root._termsTagged) return;
  root._termsTagged = true;

  var skipTags = new Set(['script','style','svg','canvas','select','option','textarea','input','button','a']);

  var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      var p = node.parentElement;
      if (!p) return NodeFilter.FILTER_REJECT;
      var tag = p.tagName.toLowerCase();
      if (skipTags.has(tag)) return NodeFilter.FILTER_REJECT;
      if (p.closest('a, .term-link, [data-ref], .bsw-tooltip, .bsw-term-tooltip, .site-sidebar, nav, footer')) {
        return NodeFilter.FILTER_REJECT;
      }
      if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  var nodes = [];
  var node;
  while ((node = walker.nextNode())) nodes.push(node);

  nodes.forEach(function (textNode) {
    _tagTextNode(textNode);
  });

  root.querySelectorAll('.term, .term-link').forEach(_wireTermEl);
}

function _tagTextNode(textNode) {
  var text = textNode.textContent;
  if (text.length < 3) return;

  var modified = false;
  var html     = '';
  var last     = 0;

  if (_termMultiRe) {
    _termMultiRe.lastIndex = 0;
    var mResult;
    while ((mResult = _termMultiRe.exec(text)) !== null) {
      var matchStr = mResult[0];
      var pos      = mResult.index;
      var key      = matchStr.toLowerCase();
      if (_termMap2[key]) {
        html += escHtml(text.slice(last, pos));
        html += '<span class="term-link" data-term-key="' + escHtml(key) + '">' +
          escHtml(matchStr) + '</span>';
        last     = pos + matchStr.length;
        modified = true;
      }
    }
  }

  var remaining        = last === 0 ? text : text.slice(last);
  var remaining_offset = last;

  var wordRe = /\b([A-Z][a-z]{2,})\b/g;
  var wResult;
  var segLast = 0;
  var segHtml = '';
  var segMod  = false;

  wordRe.lastIndex = 0;
  while ((wResult = wordRe.exec(remaining)) !== null) {
    var word    = wResult[1];
    var wpos    = wResult.index;
    var key2    = word.toLowerCase();

    if (!_termSingleSet.has(key2)) continue;

    var absPos  = remaining_offset + wpos;
    var pre     = absPos > 0 ? text.charAt(absPos - 1) : '';
    if (absPos > 0 && /[.!?\n\r]/.test(pre)) continue;
    if (/["'"''""—]/.test(pre)) {
      var pre2 = absPos > 1 ? text.charAt(absPos - 2) : '';
      if (/[.!?\n]/.test(pre2)) continue;
    }

    segHtml += escHtml(remaining.slice(segLast, wpos));
    segHtml += '<span class="term-link" data-term-key="' + escHtml(key2) + '">' +
      escHtml(word) + '</span>';
    segLast  = wpos + word.length;
    segMod   = true;
  }

  if (segMod) {
    segHtml += escHtml(remaining.slice(segLast));
    html    += segHtml;
    modified = true;
  } else if (modified) {
    html += escHtml(text.slice(last));
  }

  if (!modified) return;

  var span = document.createElement('span');
  span.innerHTML = html;
  span.querySelectorAll('.term-link').forEach(_wireTermEl);
  textNode.parentNode.replaceChild(span, textNode);
}

var _AUTOTAG_SELECTORS = [
  '.scripture',
  '[data-autotag]',
  '.lib-chapter',
  '.lib-father-quote',
  '.lib-creed',
  '#vs-focal-text',
  '#vs-context-prev',
  '#vs-context-next',
  '.reader-result-group__text',
  '.reader-interlinear-text',
  '.bk-section',
  '.bk-note',
  '.bk-application',
  '.ri-body'
].join(', ');

// autoTagTermsWhenReady: for dynamically injected containers (e.g. the timeline
// detail panel). Loads the term map first if not yet built, then scopes tagging
// to root so the rest of the page is not re-scanned.
export function autoTagTermsWhenReady(root) {
  if (!root) return;
  _loadTermMap().then(function () { autoTagTerms(root); });
}

// INTENT: Guard against loading the ~2MB BP index on pages with no taggable content.
// Checks for .term elements AND any container matching _AUTOTAG_SELECTORS before
// triggering the network fetch. If a new page type gains autotag-eligible content,
// add its container selector to _AUTOTAG_SELECTORS so this guard allows the load.
// VERIFY: Open /maps/ with cache cleared — no request to data/biblepedia/index.json.
//   Open /topics/christology/ — index.json loads during idle.
export function runAutoTagTerms() {
  var hasTerms   = !!document.querySelector('.term');
  var hasContent = !!document.querySelector(_AUTOTAG_SELECTORS);
  if (!hasTerms && !hasContent) return;
  _loadTermMap().then(function () {
    document.querySelectorAll('.term').forEach(function (el) {
      var key = el.textContent.toLowerCase().trim();
      if (!el.classList.contains('term-link') && _termMap2 && _termMap2[key]) {
        el.classList.add('term-link');
        el.dataset.termKey = key;
      }
      _wireTermEl(el);
    });

    document.querySelectorAll(_AUTOTAG_SELECTORS).forEach(function (container) {
      autoTagTerms(container);
    });

    var backdrop = document.querySelector('.bsw-modal-backdrop');
    if (backdrop && !backdrop.classList.contains('bsw-modal-backdrop--hidden')) {
      var mb = document.querySelector('.bsw-modal__body');
      if (mb) { mb._termsTagged = false; autoTagTerms(mb); }
    }
  });
}
