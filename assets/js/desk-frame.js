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

export function initDeskFrame() {
  if (!_framed) return;

  window.addEventListener('message', function (e) {
    if (e.origin !== location.origin || !e.data) return;
    if (e.data.type === 'bsw-desk-hello') { _underDesk = true; return; }
    if (e.data.type === 'bsw-desk-goto' && e.data.ref) {
      window.dispatchEvent(new CustomEvent('bsw:desk-goto', { detail: { ref: e.data.ref } }));
    }
  });

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
