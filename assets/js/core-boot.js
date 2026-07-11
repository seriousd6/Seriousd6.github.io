/* core-boot.js — Shared boot sequence for the per-page entry split (Phase 2).
 *
 * Replaces the monolithic app.js: every page now loads a thin entry module
 * from assets/js/entries/ which imports boot() and passes its page-specific
 * init callback. core-boot owns exactly the work app.js ran on EVERY page —
 * theme, PWA, storage migrations, Bible metadata, tooltip/modal/ref wiring,
 * version picker, sidebar Search button, history widget, deferred term/place
 * tagging, and the window.BibleUI public API. Page-feature modules (reader,
 * maps, workshop, …) are NOT imported here; each page's entry imports only
 * what that page uses.
 *
 * Modules that ARE imported here ship on every page because the universal
 * verse modal depends on their renderers (word study / topics / confessions /
 * fathers / dictionary tabs) and the memorisation helpers. Making those
 * lazy is a follow-up (dynamic import on first tab click), not Phase 2.
 *
 * boot(pageInit, opts):
 *   pageInit   — optional; runs once Bible metadata + shared UI are ready.
 *   opts.early — run pageInit BEFORE autoTagRefs/wireInlineVerses. Only the
 *                reader entry uses this, preserving app.js's original order
 *                (reader init preceded ref auto-tagging; all other page
 *                inits followed it).
 */
'use strict';

import {
  getVersion, setVersion, metaBooks,
  loadVersions, loadBooks, populateVersionPicker, wireVersionPicker,
  initTheme, READER_URL, onVersionChange, _fireBibleReady
} from './core.js';
import { _runStorageMigrations } from './storage.js';
import { buildTooltipDOM } from './tooltip.js';
import {
  buildModalDOM, openModal, syncModalVersionPicker,
  registerModalWordStudy, registerModalTopics, registerModalConfessions,
  registerModalFathers, registerModalDictionary,
  registerMemHelpers, registerAutoTagTerms,
  initHistoryWidget
} from './modal.js';
import {
  wireRefLinks, autoTagRefs, wireInlineVerses, updateInlineVerses
} from './wire.js';
import { initPWA } from './pwa.js';
import { buildSearchDOM } from './search.js';

// ── Modal-tab renderer dependencies (site-wide via the verse modal) ────────
import { renderModalWordStudy } from './verse-study.js';
import { _memHas, _memAdd, _memRemove, _memRefreshModalBtn } from './daily.js';
import { renderModalTopics, renderModalConfessions, renderModalFathers, renderModalDictionary } from './library.js';
import { runAutoTagTerms, autoTagTerms, getTermMap2 } from './terms.js';
import { runAutoTagPlaces, autoTagPlacesIn } from './places.js';
import { initOLSection } from './ol-companion.js';
import { wireApoRefLinks } from './apocrypha-reader.js';

// ── Register cross-module callbacks ───────────────────────────────────────
// These connect the modal to feature-module renderers without creating circular
// imports. The modal calls these registered functions when a user clicks a tab
// inside the verse modal (word study, topics, etc.).
registerModalWordStudy(renderModalWordStudy);
registerModalTopics(renderModalTopics);
registerModalConfessions(renderModalConfessions);
registerModalFathers(renderModalFathers);
registerModalDictionary(renderModalDictionary);
// Give the modal access to the memorisation helpers so it can show the
// "Add to memory" button and react to changes.
registerMemHelpers(_memHas, _memAdd, _memRemove, _memRefreshModalBtn);
// Give the modal's auto-tag feature access to the term map so theological
// terms inside verse text are underlined with definitions.
registerAutoTagTerms(autoTagTerms, getTermMap2);

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
//   - initOLSection:   ol-companion.js on verse-study page init
//   - getVersion/setVersion: version picker in topics/_template inline script
//   Do not add new window.* state outside this object; use entry callbacks instead.
// VERIFY: From any topic page DevTools console, confirm `window.BibleUI.openModal`
//   is a function; call `window.BibleUI.openReader('john', 3, 16)` and verify the
//   reader navigates to John 3:16.
window.BibleUI = {
  getVersion:      getVersion,
  setVersion:      setVersion,
  openModal:       openModal,
  initOLSection:   initOLSection,
  autoTagPlacesIn: autoTagPlacesIn,  // called by reader.js / timeline.js after dynamic renders
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
//   9. Term/place tagging — deferred to idle time so it doesn't block render.
export function boot(pageInit, opts) {
  opts = opts || {};

  function init() {
    initTheme();
    initPWA();
    _runStorageMigrations();

    Promise.all([loadVersions(), loadBooks()]).then(function () {
      populateVersionPicker();
      buildTooltipDOM();
      buildModalDOM();
      wireRefLinks();        // wire any static [data-ref] elements in the initial HTML
      wireApoRefLinks();     // second pass: wire apocryphal refs not handled by wireRefLinks
      wireVersionPicker();
      buildSearchDOM();      // adds the Search button to the sidebar on every page

      if (pageInit && opts.early) pageInit();

      // Auto-tag plain-text Bible refs and wire inline .bsw-verse elements
      // on every page (these are no-ops if there's nothing to tag/populate).
      autoTagRefs();
      wireInlineVerses();

      if (pageInit && !opts.early) pageInit();

      // History widget appears on the home page sidebar — tracks recently visited refs.
      initHistoryWidget();

      // Signal that metaBooks and metaVersions are ready — fires any callbacks
      // registered via onBibleReady() in other modules.
      _fireBibleReady();

      // Term auto-tagging is expensive (scans all text nodes); defer to browser idle time
      // to avoid blocking first interactive paint. Falls back to setTimeout on browsers
      // that don't support requestIdleCallback (e.g. older Safari).
      var _runTag = function () { runAutoTagTerms(); };
      if (typeof requestIdleCallback !== 'undefined') {
        requestIdleCallback(_runTag, { timeout: 3000 });
      } else {
        setTimeout(_runTag, 1200);
      }

      /* Place-name auto-tagging — deferred to a second idle slot so it doesn't
         compete with term tagging for the same idle window.                   */
      var _runPlaces = function () { runAutoTagPlaces(); };
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
