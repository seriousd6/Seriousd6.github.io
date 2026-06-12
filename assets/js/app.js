/* app.js — Universal entry point for the Bible Study Website ES module split.
 *
 * Loaded as <script type="module" src="...app.js"> from every HTML page.
 * Imports all feature modules, wires cross-module callbacks, and runs init().
 *
 * Design:
 *   - All page-feature init calls are guarded by getElementById checks so that
 *     each module only activates on the page(s) that actually contain its DOM.
 *   - Static imports (not dynamic) keep things simple for GitHub Pages, which
 *     has no import maps or bundler — the browser loads what it needs.
 *   - The window.BibleUI public API lets non-module scripts (e.g. inline scripts
 *     on topic pages) call openModal() and similar without needing ES module syntax.
 */
'use strict';

import {
  getVersion, setVersion, metaVersions, metaBooks,
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
  _showShortcutsOverlay, _injectShortcutsBtn,
  initHistoryWidget
} from './modal.js';
import {
  wireRefLinks, autoTagRefs, wireInlineVerses, updateInlineVerses,
  applyHighlights, applyModalHighlights, applyBookmarks
} from './wire.js';
import { initPWA, _initOnboarding } from './pwa.js';

// ── Page-module imports ───────────────────────────────────────────────────
// Each module below is imported eagerly but its init function is guarded by a
// DOM check in init() so it only runs on the relevant page.
import { initSearchPage, buildSearchDOM } from './search.js';
import {
  initReaderPage, initCompareToggle, injectComparePanel,
  isCompareEnabled, getCompareVersion, setCompareVersion,
  initViewToggle, initFontSizeControls,
  initSidebarToggle, initXrefNotesToggle, initCommModeToggle,
  initColumnsToggle, initReaderModeToggle, initNotesPanelToggle
} from './reader.js';
import {
  initParallelToggle, getParallelsEnabled, setParallelsEnabled
} from './parallels.js';
import {
  initInterlinearToggle, initBookInfoToggle,
  getInterlinearEnabled, setInterlinearEnabled
} from './interlinear.js';
import {
  initVerseStudyPage, loadVerseStudyVerse, renderModalWordStudy
} from './verse-study.js';
import { initWordPage } from './word.js';
import { initDailyPage, initMemorizePage, initPlansHomeWidget, _memHas, _memAdd, _memRemove, _memRefreshModalBtn } from './daily.js';
import { initDictionaryPage, renderModalTopics, renderModalConfessions, renderModalFathers, renderModalDictionary } from './library.js';
import { initBiblepediaPage } from './biblepedia.js';
import { runAutoTagTerms, autoTagTerms, getTermMap2 } from './terms.js';
import { runAutoTagPlaces, autoTagPlacesIn } from './places.js';
import { initTimelinePage, initChurchTimelinePage } from './timeline.js';
import { initMapsPage } from './maps.js';
import { initTimelapsePage } from './timelapse-map.js?v=2';
import { initWordCloudPage } from './wordcloud.js';
import { initLibReaderPage } from './lib-reader.js';
import { initLibBrowserPage } from './lib-browser.js';
import { initLibProgressPage } from './lib-progress.js';
import { initWorkshopPage } from './workshop.js';
import { initOLSection } from './ol-companion.js';
import { initApocryphaReader, wireApoRefLinks } from './apocrypha-reader.js';

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
//   Do not add new window.* state outside this object; use app.js callbacks instead.
// VERIFY: From any topic page DevTools console, confirm `window.BibleUI.openModal`
//   is a function; call `window.BibleUI.openReader('john', 3, 16)` and verify the
//   reader navigates to John 3:16.
window.BibleUI = {
  init:            init,
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

// ── init ──────────────────────────────────────────────────────────────────
// Main boot sequence. Runs after DOMContentLoaded (or immediately if the DOM
// is already ready). Order matters:
//   1. Theme — applied before paint to avoid flash of wrong colours.
//   2. PWA registration — registers the service worker for offline support.
//   3. Storage migrations — upgrades any old localStorage data formats.
//   4. loadVersions() + loadBooks() in parallel — both must resolve before any
//      version picker, ref parsing, or search can function.
//   5. UI assembly — tooltip, modal, ref wiring, version picker, search button.
//   6. Page-specific init — each guarded by a landmark element check.
//   7. _fireBibleReady() — notifies any modules waiting on Bible metadata.
//   8. Term tagging — deferred to idle time so it doesn't block first render.
function init() {
  initTheme();

  // ── Workshop page (translation/workshop/index.html) ───────────────────────
  // Private tool; does not need Bible metadata. Init directly and skip the rest.
  if (document.getElementById('workshop-container')) {
    initWorkshopPage();
    return;
  }

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

    // ── Reader page (read/index.html) ─────────────────────────────────────
    // Detected by #reader-results — the container where chapter verses render.
    if (document.getElementById('reader-results')) {
      initReaderPage();
      initParallelToggle();
      initCompareToggle();
      initInterlinearToggle();
      initBookInfoToggle();
      initCommModeToggle();
      initNotesPanelToggle();
      initViewToggle();
      initSidebarToggle();
      initFontSizeControls();
      initXrefNotesToggle();
      initColumnsToggle();
      initReaderModeToggle();
      _injectShortcutsBtn();
    }

    // ── Verse Study page (verse-study/index.html) ─────────────────────────
    // Detected by #vs-sections-container.
    if (document.getElementById('vs-sections-container')) {
      initVerseStudyPage();
    }

    // ── Word Study page (word/index.html) ─────────────────────────────────
    // Detected by #wd-header.
    if (document.getElementById('wd-header')) {
      initWordPage();
    }

    // Auto-tag plain-text Bible refs and wire inline .bsw-verse elements
    // on every page (these are no-ops if there's nothing to tag/populate).
    autoTagRefs();
    wireInlineVerses();

    // ── Daily / Plans pages ───────────────────────────────────────────────
    // #daily-plan-select is on the daily reading plan page;
    // #home-plans-widget is the abbreviated widget on the home page.
    if (document.getElementById('daily-plan-select')) {
      initDailyPage();
    } else if (document.getElementById('home-plans-widget')) {
      initPlansHomeWidget();
    }

    // ── Memorisation page (memorize/index.html) ───────────────────────────
    if (document.getElementById('mem-list')) {
      initMemorizePage();
    }

    // ── Dictionary / Library page (dictionary/index.html) ─────────────────
    // initDictionaryPage handles both Smith's, Hitchcock's, Torrey's, and the
    // full library document viewer on the same page.
    if (document.getElementById('dict-list')) {
      initDictionaryPage();
    }

    // ── Biblepedia page (biblepedia/index.html) ───────────────────────────
    if (document.getElementById('bp-container')) {
      initBiblepediaPage();
    }

    // ── Timeline page (timeline/index.html) ──────────────────────────────
    if (document.getElementById('timeline-container')) {
      initTimelinePage();
    }

    // ── Church History Timeline (church-history/index.html) ───────────────
    if (document.getElementById('church-timeline-container')) {
      initChurchTimelinePage();
    }

    // ── Maps page (maps/index.html) ───────────────────────────────────────
    if (document.getElementById('maps-container')) {
      initMapsPage();
    }

    // ── Timelapse page (maps/timelapse/index.html) ────────────────────────
    if (document.getElementById('tl-map')) {
      initTimelapsePage();
    }

    // ── Word Cloud page (wordcloud/index.html) ────────────────────────────
    if (document.getElementById('wc-container')) {
      initWordCloudPage();
    }

    // ── Library reader (library/read/index.html) ──────────────────────────
    if (document.getElementById('lib-reader-content')) {
      initLibReaderPage();
    }

    // ── Library browser (library/index.html) ──────────────────────────────
    if (document.getElementById('lb-container')) {
      initLibBrowserPage();
    }

    // ── Library progress page (library/progress/index.html) ───────────────
    if (document.getElementById('lp-root')) {
      initLibProgressPage();
    }

    // ── Apocrypha reader (apocrypha/index.html) ───────────────────────────
    if (document.getElementById('apoc-reader-results')) {
      initApocryphaReader();
    }

    // History widget appears on the home page sidebar — tracks recently visited refs.
    initHistoryWidget();

    // Onboarding is shown to first-time visitors on the daily plan page.
    if (document.getElementById('daily-plan-select')) {
      _initOnboarding();
    }

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

// ── Bootstrap ─────────────────────────────────────────────────────────────
// Run init() after the DOM is ready. If the script is deferred or the document
// is already parsed (readyState !== 'loading'), run immediately.
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
