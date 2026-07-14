/* desk-frame.js — the framed-page half of the Desk protocol (assets/js/desk.js
 * is the surface half). Loaded by core-boot on every page; everything here
 * no-ops unless the page is actually inside an iframe whose parent is the
 * Desk (the Desk announces itself with a 'bsw-desk-hello' postMessage).
 *
 * Two jobs:
 *  1. CROSS-RESOURCE CLICKS OPEN PANELS, NOT REPLACE CONTENT. Inside a
 *     reader panel, a link to the maps page, a biblepedia article, an
 *     answers page, … used to navigate the iframe away (or pop a browser
 *     tab for target=_blank). Under the Desk, those clicks post
 *     'bsw-desk-open' and the Desk opens the destination as a new panel.
 *     Same-resource navigation (next chapter, another article) stays
 *     in-panel; modified clicks (ctrl/cmd/shift) keep browser behavior.
 *  2. READER LINKING. reader.js calls emitDeskNav(ref) whenever a lookup
 *     lands; the Desk forwards it to other link-toggled reader panels as
 *     'bsw-desk-goto', which arrives here and is re-dispatched as a
 *     window CustomEvent('bsw:desk-goto') for reader.js to act on.
 */
'use strict';

var _framed = false;
try { _framed = window.self !== window.top; } catch (e) { _framed = true; }

var _underDesk = false;

// First path segment = the resource a URL belongs to ("read", "biblepedia",
// "maps", …). Same segment → in-panel navigation; different → new panel.
export function resourcePrefix(pathname) {
  var m = /^\/([^/]+)/.exec(pathname || '/');
  return m ? m[1] : '';
}

export function emitDeskNav(ref) {
  if (!_underDesk || !ref) return;
  try { window.parent.postMessage({ type: 'bsw-desk-nav', ref: ref }, location.origin); } catch (e) {}
}

// Reader → Desk: the tagged places of the rendered chapter (reader-rail.js),
// forwarded by the Desk to link-toggled maps panels.
export function emitDeskPlaces(ref, ids, mapId) {
  if (!_underDesk || !ids || !ids.length) return;
  try { window.parent.postMessage({ type: 'bsw-desk-places', ref: ref, ids: ids, mapId: mapId || null }, location.origin); } catch (e) {}
}

// P22 word lock: a linked dossier panel follows word taps anywhere.
export function emitDeskWord(code, lang) {
  if (!_underDesk || !code) return;
  try { window.parent.postMessage({ type: 'bsw-desk-word', code: code, lang: lang || null }, location.origin); } catch (e) {}
}

// P19: linked readers scroll together. The leading panel emits a verse
// anchor (first visible verse + its viewport offset) so followers align by
// CONTENT, not pixel ratio — verse heights differ between panels; the ratio
// rides along as a fallback. _scrollFollowUntil suppresses re-emitting while
// an incoming sync is being applied (feedback-loop guard).
var _scrollFollowUntil = 0;

function _wireScrollSync() {
  if (resourcePrefix(location.pathname) !== 'read') return;
  var pending = false;
  window.addEventListener('scroll', function () {
    if (!_underDesk || pending || Date.now() < _scrollFollowUntil) return;
    pending = true;
    requestAnimationFrame(function () {
      pending = false;
      if (Date.now() < _scrollFollowUntil) return;
      var anchor = null;
      var verses = document.querySelectorAll('.reader-verse[data-v]');
      for (var i = 0; i < verses.length; i++) {
        var r = verses[i].getBoundingClientRect();
        if (r.bottom > 60) {
          anchor = { ch: verses[i].getAttribute('data-ch'), v: verses[i].getAttribute('data-v'), off: Math.round(r.top) };
          break;
        }
      }
      var doc = document.documentElement;
      var max = doc.scrollHeight - doc.clientHeight;
      try {
        window.parent.postMessage({
          type: 'bsw-desk-scroll', anchor: anchor,
          ratio: max > 0 ? doc.scrollTop / max : 0
        }, location.origin);
      } catch (e) {}
    });
  }, { passive: true });
}

// P19: shared text size. Applied at boot from localStorage (same origin as
// the desk) and live on broadcast.
function _applyDeskZoom(z) {
  z = Math.min(1.4, Math.max(0.8, parseFloat(z) || 1));
  document.documentElement.style.fontSize = z === 1 ? '' : (z * 100) + '%';
}

export function initDeskFrame() {
  if (!_framed) return;

  try {
    var z0 = localStorage.getItem('bsw_desk_zoom');
    if (z0) _applyDeskZoom(z0);
  } catch (e) {}
  _wireScrollSync();

  window.addEventListener('message', function (e) {
    if (e.origin !== location.origin || !e.data) return;
    if (e.data.type === 'bsw-desk-hello') { _underDesk = true; return; }
    if (e.data.type === 'bsw-desk-goto' && e.data.ref) {
      window.dispatchEvent(new CustomEvent('bsw:desk-goto', { detail: { ref: e.data.ref } }));
    }
    if (e.data.type === 'bsw-desk-scroll-to') {
      _scrollFollowUntil = Date.now() + 350;
      var a = e.data.anchor;
      var applied = false;
      if (a && a.v) {
        var el = document.querySelector('.reader-verse[data-ch="' + a.ch + '"][data-v="' + a.v + '"]');
        if (el) {
          window.scrollBy(0, el.getBoundingClientRect().top - (a.off || 0));
          applied = true;
        }
      }
      if (!applied && typeof e.data.ratio === 'number') {
        var doc = document.documentElement;
        doc.scrollTop = e.data.ratio * (doc.scrollHeight - doc.clientHeight);
      }
      return;
    }
    if (e.data.type === 'bsw-desk-zoom') {
      _applyDeskZoom(e.data.zoom);
      return;
    }
    if (e.data.type === 'bsw-desk-show-word' && e.data.code) {
      window.dispatchEvent(new CustomEvent('bsw:desk-word', { detail: { code: e.data.code, lang: e.data.lang || null } }));
    }
    if (e.data.type === 'bsw-desk-show-places' && e.data.ids) {
      window.dispatchEvent(new CustomEvent('bsw:desk-show-places', { detail: { ref: e.data.ref, ids: e.data.ids, mapId: e.data.mapId || null } }));
    }
  });

  // Desk keyboard shortcuts typed while this frame has focus — forwarded to
  // the surface, which acts on this panel. Same combo map as desk.js
  // deskKeyAction (keep in sync): Ctrl+Shift+→ split right, ↓ split down,
  // ⏎ maximize, ⌫ close. Skipped inside editable fields.
  document.addEventListener('keydown', function (e) {
    if (!_underDesk) return;
    if (!(e.ctrlKey || e.metaKey) || !e.shiftKey) return;
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
    var act = { ArrowRight: 'split-r', ArrowDown: 'split-d', Enter: 'max', Backspace: 'close' }[e.key];
    if (!act) return;
    e.preventDefault();
    try { window.parent.postMessage({ type: 'bsw-desk-key', act: act }, location.origin); } catch (err) {}
  }, true);

  // Document capture so this sees the click before any in-page handler that
  // stops propagation. Only ACTS on cross-resource anchor clicks under the
  // Desk; everything else falls through untouched.
  document.addEventListener('click', function (e) {
    if (!_underDesk) return;
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey || e.button !== 0) return;
    var a = e.target.closest('a[href]');
    if (!a || a.hasAttribute('download')) return;
    var url;
    try { url = new URL(a.href, location.href); } catch (err) { return; }
    if (url.origin !== location.origin) return;                     // external stays a browser tab
    if (url.pathname === location.pathname) return;                 // query/hash nav stays in-panel
    var from = resourcePrefix(location.pathname);
    var to   = resourcePrefix(url.pathname);
    if (to === 'desk') return;                                      // never nest the Desk
    if (to === from && a.target !== '_blank') return;               // same resource → in-panel
    e.preventDefault();
    e.stopPropagation();
    try {
      window.parent.postMessage({
        type: 'bsw-desk-open',
        url: url.pathname + url.search + url.hash,
      }, location.origin);
    } catch (err) {}
  }, true);
}
