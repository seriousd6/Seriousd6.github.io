/* core-boot.js — Shared boot sequence for the per-page entry split (Phase 2/2.5).
 *
 * Replaces the monolithic app.js: every page loads a thin entry module from
 * assets/js/entries/ which imports boot() and passes its page-specific init
 * callback. core-boot owns exactly the work app.js ran on EVERY page — theme,
 * PWA, storage migrations, Bible metadata, tooltip/modal/ref wiring, version
 * picker, sidebar Search button + hotkeys, history widget, deferred term/place
 * tagging, and the window.BibleUI public API.
 *
 * Phase 2.5 — the eager import set is only what the first paint truly needs:
 * core, storage, tooltip, modal, wire, pwa, mem. Everything else is loaded on
 * demand via dynamic import():
 *   - terms.js / places.js  → at requestIdleCallback time (same slots the
 *     tagging already ran in; the modal's term-tag guard tolerates the gap
 *     exactly as it tolerated the term-map fetch before)
 *   - apocrypha-reader.js   → fire-and-forget right after wireRefLinks
 *     (wireApoRefLinks awaits its own abbrev-map fetch anyway)
 *   - ol-companion.js / places.js on window.BibleUI → lazy async wrappers;
 *     the only initOLSection caller (verse-study.js) already chains .catch on
 *     the returned promise, and autoTagPlacesIn callers are fire-and-forget
 *   - search.js             → never loaded here; the sidebar Search button and
 *     hotkeys are inlined below (buildSearchNav), and the search page's own
 *     entry imports the engine statically
 *
 * boot(pageInit, opts):
 *   pageInit   — optional; runs once Bible metadata + shared UI are ready.
 *   opts.early — run pageInit BEFORE autoTagRefs/wireInlineVerses. Only the
 *                reader entry uses this, preserving app.js's original order.
 */
'use strict';

import {
  getVersion, setVersion, metaBooks,
  loadVersions, loadBooks, populateVersionPicker, wireVersionPicker,
  initTheme, READER_URL, SEARCH_URL, onVersionChange, _fireBibleReady
} from './core.js';
import { _runStorageMigrations } from './storage.js';
import { buildTooltipDOM } from './tooltip.js';
import {
  buildModalDOM, openModal, syncModalVersionPicker,
  registerMemHelpers, registerAutoTagTerms,
  _showShortcutsOverlay, initHistoryWidget
} from './modal.js';
import {
  wireRefLinks, autoTagRefs, wireInlineVerses, updateInlineVerses
} from './wire.js';
import { initPWA } from './pwa.js';
import { _memHas, _memAdd, _memRemove, _memRefreshModalBtn } from './mem.js';
import { initDeskFrame } from './desk-frame.js';

// ── Register cross-module callbacks ───────────────────────────────────────
// Give the modal access to the memorisation helpers so it can show the
// "Add to memory" button and react to changes. (mem.js is the thin storage
// module split out of daily.js — the modal needs sync answers, so these
// stay eager; they cost ~3 KB.)
registerMemHelpers(_memHas, _memAdd, _memRemove, _memRefreshModalBtn);
// registerAutoTagTerms happens lazily when terms.js loads at idle — until
// then the modal's term-tag guard (_autoTagTermsFn == null) skips tagging,
// exactly as it did while the term map was still fetching.

// ── Version-change side effects ───────────────────────────────────────────
// When the user switches translations, update any inline verse elements and
// keep the modal's version picker in sync.
onVersionChange(function (id) {
  updateInlineVerses(id);
  syncModalVersionPicker();
  // Note: the search page re-runs its own search via its internal version-change
  // hook wired inside initSearchPage — no action needed here.
});

// ── Public API ────────────────────────────────────────────────────────────
// window.BibleUI is available to non-module scripts (topic pages, inline scripts).
// Keep this surface small — it's the only intentional global.
// CHANGE? Consumers of each key — removing or renaming any of these silently
//   breaks the listed callers with no JS error until runtime:
//   - openModal:       topic-page inline <script> blocks on all 10 topic pages
//   - openReader:      topic-page inline <script> blocks (pass bookId string)
//   - autoTagPlacesIn: timeline.js after dynamic re-renders; reader.js on lookup
//                      (lazy: fire-and-forget wrapper importing places.js)
//   - initOLSection:   verse-study.js word-study sections (lazy: returns the
//                      import().then(...) promise; the caller chains .catch)
//   - getVersion/setVersion: version picker in topics/_template inline script
//   Do not add new window.* state outside this object; use entry callbacks instead.
// VERIFY: From any topic page DevTools console, confirm `window.BibleUI.openModal`
//   is a function; call `window.BibleUI.openReader('john', 3, 16)` and verify the
//   reader navigates to John 3:16.
window.BibleUI = {
  getVersion:      getVersion,
  setVersion:      setVersion,
  openModal:       openModal,
  initOLSection:   function () {
    var args = arguments;
    return import('./ol-companion.js').then(function (m) {
      return m.initOLSection.apply(null, args);
    });
  },
  autoTagPlacesIn: function (el) {
    import('./places.js').then(function (m) { m.autoTagPlacesIn(el); });
  },
  // INTENT: Resolves bookId (e.g. "genesis") to its display name (e.g. "Genesis")
  //   via metaBooks before building the reader URL. Falls back to the raw bookId
  //   string if metaBooks hasn't loaded yet, which produces a URL the reader can
  //   still parse but with lower fidelity (ID string rather than canonical name).
  openReader:   function (bookId, ch, v) {
    var bkData = metaBooks && metaBooks.find(function (b) { return b.id === bookId; });
    var bkName = bkData ? bkData.name : bookId;
    var ref    = bkName + ' ' + (ch || 1) + (v ? ':' + v : '');
    window.location.href = READER_URL + '?ref=' + encodeURIComponent(ref);
  }
};

// ── buildSearchNav ─────────────────────────────────────────────────────────
// Global search hotkeys, moved here from search.js so non-search pages don't
// load the 60 KB search engine for them. (The old injected sidebar Search
// button was removed in Phase 5: its `.version-picker` anchor disappeared in
// the Candlelight static-sidebar refactor, so it had been silently dead —
// the sidebar's 🔍 Explore link is the navigation affordance.)
function buildSearchNav() {
  // Ctrl+K: focus the search input if on the search page, otherwise navigate.
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      var inp = document.getElementById('bsw-search-input');
      if (inp) { inp.focus(); inp.select(); } else { window.location.href = SEARCH_URL; }
    }
  });

  // '?' opens the keyboard shortcuts overlay.
  // '/' focuses the reader search bar (only on the reader page).
  document.addEventListener('keydown', function (e) {
    if (e.key !== '?' && e.key !== '/') return;
    if (e.key === '/' && !document.getElementById('reader-results')) return;
    var tag = document.activeElement && document.activeElement.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
    if (e.key === '?') { e.preventDefault(); _showShortcutsOverlay(); }
  });
}

// ── boot ──────────────────────────────────────────────────────────────────
// Main boot sequence, formerly app.js init(). Runs after DOMContentLoaded (or
// immediately if the DOM is already ready). Order matters:
//   1. Theme — applied before paint to avoid flash of wrong colours.
//   2. PWA registration — registers the service worker for offline support.
//   3. Storage migrations — upgrades any old localStorage data formats.
//   4. loadVersions() + loadBooks() in parallel — both must resolve before any
//      version picker, ref parsing, or search can function.
//   5. UI assembly — tooltip, modal, ref wiring, version picker, search button.
//   6. Page-specific init — the entry's pageInit callback (opts.early moves it
//      before step 7, matching the reader's original position in app.js).
//   7. autoTagRefs + wireInlineVerses — no-ops if there's nothing to tag.
//   8. _fireBibleReady() — notifies any modules waiting on Bible metadata.
//   9. Term/place tagging — deferred to idle time; the modules themselves are
//      dynamic-imported in the same idle slot (Phase 2.5).
export function boot(pageInit, opts) {
  opts = opts || {};

  function init() {
    // Frame-lite boot (A1): embedded pages — Desk panels, ?minimal=1 hubs —
    // skip the PWA layer entirely. Each panel used to register the service
    // worker, inject manifest/meta, and fire the 66-book precache message
    // as if it were a standalone visit; the HOST page owns all of that.
    var _framed;
    try { _framed = window.self !== window.top; } catch (e) { _framed = true; }

    initTheme();
    if (!_framed) initPWA();
    _runStorageMigrations();
    initDeskFrame();   // no-op unless framed under the Desk (see desk-frame.js)

    Promise.all([loadVersions(), loadBooks()]).then(function () {
      populateVersionPicker();
      buildTooltipDOM();
      buildModalDOM();
      wireRefLinks();        // wire any static [data-ref] elements in the initial HTML
      // Second pass: wire apocryphal refs not handled by wireRefLinks. Lazy —
      // wireApoRefLinks awaits its own abbrev-map fetch internally, so arriving
      // a few ms later via dynamic import is indistinguishable.
      import('./apocrypha-reader.js').then(function (m) { m.wireApoRefLinks(); });
      wireVersionPicker();
      buildSearchNav();      // global search hotkeys (Ctrl+K, ?)

      if (pageInit && opts.early) pageInit();

      // Auto-tag plain-text Bible refs and wire inline .bsw-verse elements
      // on every page (these are no-ops if there's nothing to tag/populate).
      autoTagRefs();
      wireInlineVerses();

      if (pageInit && !opts.early) pageInit();

      // History widget appears on the home page sidebar — tracks recently
      // visited refs. Frames have no sidebar; skip the work.
      if (!_framed) initHistoryWidget();

      // Signal that metaBooks and metaVersions are ready — fires any callbacks
      // registered via onBibleReady() in other modules.
      _fireBibleReady();

      // Term auto-tagging is expensive (scans all text nodes); defer to browser idle
      // time so it doesn't block first interactive paint — and (Phase 2.5) load the
      // module itself in that idle slot too. Registration with the modal happens on
      // load; until then the modal skips term tagging, same as when the term map
      // hadn't fetched yet. Falls back to setTimeout on browsers without
      // requestIdleCallback (e.g. older Safari).
      var _runTag = function () {
        import('./terms.js').then(function (m) {
          registerAutoTagTerms(m.autoTagTerms, m.getTermMap2);
          m.runAutoTagTerms();
        });
      };
      if (typeof requestIdleCallback !== 'undefined') {
        requestIdleCallback(_runTag, { timeout: 3000 });
      } else {
        setTimeout(_runTag, 1200);
      }

      /* Place-name auto-tagging — deferred to a second idle slot so it doesn't
         compete with term tagging for the same idle window.                   */
      var _runPlaces = function () {
        import('./places.js').then(function (m) { m.runAutoTagPlaces(); });
      };
      if (typeof requestIdleCallback !== 'undefined') {
        requestIdleCallback(_runPlaces, { timeout: 5000 });
      } else {
        setTimeout(_runPlaces, 2000);
      }

    }).catch(function (err) {
      console.error('[BibleUI] init failed:', err);
    });
  }

  // Run init() after the DOM is ready. If the document is already parsed
  // (readyState !== 'loading'), run immediately.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}
