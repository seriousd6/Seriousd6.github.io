# Bible Study Website — Completed Tasks Archive

All completed (`[x]`) and closed/decided items from the working TODO, organized by phase.
See `working/TODO.md` for the active task list.

---

## Completed 2026-06-06 (loop session, iteration 4)

### DATA-8 · additions-esther chapter count mismatch *(LOW)*

Inspected `data/bible-apocrypha/WEB-CE/additions-esther.json` and
`data/bible-apocrypha/BRENTON/additions-esther.json` — both have 10 chapters (1–10),
using the continuous Greek Esther chapter numbering (LXX convention that includes
Addition A as ch 1 and runs through the full narrative). Declared count in
`apocrypha-books.json` was 7 (incorrect enumeration).

Fix: updated `apocrypha-books.json` — changed `"chapters": 7` → `"chapters": 10` and
renamed `"Additions to Esther"` → `"Greek Esther"` (the data is the full 10-chapter LXX
Greek Esther, not a 6-section additions-only file). Also added `"GkEsth"` abbrev.
Bumped `APP_CACHE_V` from `bsw-app-v67` → `bsw-app-v68` so PWA clients pick up the
updated `apocrypha-books.json` (it is in SHELL_URLS / cache-first).

**Files modified:** `data/apocrypha-books.json`, `sw.js`.

### DATA-4 · DR apocrypha version missing 4 Daniel/Esther additions *(LOW)*
### DATA-5 · WEB-CE full-bible version missing 3 Daniel-addition books *(MEDIUM)*

Root cause: DR and WEB-CE store the Daniel additions embedded within their canonical
`daniel.json` (ch 13 = Susanna, ch 14 = Bel and the Dragon, ch 3 v24+ = Prayer of
Azariah) and, for DR, `esther.json` (ch 11-16 = Additions A-F). The eBible.org source
doesn't provide standalone files for these books.

Fix: Created and ran `scripts/extract-daniel-additions.py`, which reads the embedded
chapters and writes standalone `{ "chapters": { "1": { v: text } } }` files:

- `data/bible-apocrypha/DR/susanna.json` (1 ch, 65 verses — from DR daniel ch 13)
- `data/bible-apocrypha/DR/bel-and-dragon.json` (1 ch, 42 verses — DR daniel ch 14)
- `data/bible-apocrypha/DR/prayer-of-azariah.json` (1 ch, 77 verses — DR daniel ch 3 v24+)
- `data/bible-apocrypha/DR/additions-esther.json` (6 chs, 98 verses — DR esther ch 11-16)
- `data/bible-apocrypha/WEB-CE/susanna.json` (1 ch, 64 verses — WEB-CE daniel ch 13)
- `data/bible-apocrypha/WEB-CE/bel-and-dragon.json` (1 ch, 42 verses — WEB-CE daniel ch 14)
- `data/bible-apocrypha/WEB-CE/prayer-of-azariah.json` (1 ch, 74 verses — WEB-CE daniel ch 3 v24+)

Note on DR additions-esther chapter count: apocrypha-books.json declares 10 chapters
(matching full Greek Esther convention in WEB-CE/BRENTON), but DR's additions-esther
only has 6 chapters (the 6 Addition sections A-F). The reader gracefully handles missing
chapters with "Chapter N not found in this translation." — a significant improvement over
the previous total 404.

**Script:** `scripts/extract-daniel-additions.py`

### DATA-9 · BRENTON Baruch missing chapter 6 (Letter of Jeremiah) *(LOW)*

Created and ran `scripts/fetch-brenton-baruch6.py`. Downloads the eBible.org BRENTON
USFM zip, locates `48-LJEeng-Brenton.usfm` (the Letter of Jeremiah), parses all 73
verses with a USFM strip regex, and appends them as chapter `"6"` in
`data/bible-apocrypha/BRENTON/baruch.json`. Result: baruch.json now has chapters 1–6;
ch 6 opens "A copy of an epistle, which Jeremy sent unto them which were to be led
captives into Babylon…" (73 verses).

Also: BRENTON re-fetch (run to attempt DATA-9 via main script) recovered two DATA-3
books — `daniel.json` (12 ch, 420 v) and `esther.json` (10 ch, 164 v) — plus
`susanna.json` (DATA-5 related). Re-ran `fix-brenton-spaces.py` after re-fetch to clean
374 fused words in the fresh files. `nahum.json` remains missing from eBible.org BRENTON
source (DATA-3 still partial).

**Script:** `scripts/fetch-brenton-baruch6.py`
**Files modified:** `data/bible-apocrypha/BRENTON/baruch.json`, `data/apocrypha-books.json`,
`sw.js`.

---

## Completed 2026-06-06 (loop session, iteration 3)

### PWA-6 — library/progress/index.html not precached *(LOW)*

Added `'./library/progress/index.html'` to SHELL_URLS in `sw.js` immediately after
`'./library/index.html'` (line 67). Bumped `APP_CACHE_V` from `bsw-app-v66` →
`bsw-app-v67`. The three companion JS/CSS files were already precached; only the HTML
page itself was missing. Going offline and navigating to `library/progress/` will now
serve the cached page rather than `offline.html`.

**Files modified:** `sw.js` (version string + 1 SHELL_URL entry).

### AUD-11 — verse-study.js: static document.title and missing h1 *(MEDIUM)*

Two accessibility fixes on the verse-study page:
1. Added `document.title = parsed.display + ' — Verse Study — Bible Study';` in
   `assets/js/verse-study.js` immediately after `headerRef.textContent = parsed.display`
   (line 84). Browser tab now shows the verse reference (e.g. "John 3:16 — Verse Study
   — Bible Study") instead of the static "Verse Study — Bible Study".
2. Added `role="heading" aria-level="1"` to `#vs-header-ref` in `verse-study/index.html`
   line 26. Screen readers now expose the verse reference as the H1 page title; section
   H2s (Cross-References, Commentary, etc.) follow in correct hierarchy.

**Files modified:** `assets/js/verse-study.js`, `verse-study/index.html`.

### DATA-7 · BRENTON missing spaces in verse text *(MEDIUM)*

Created `scripts/fix-brenton-spaces.py`. Uses `re.sub(r'([a-z])([A-Z])', r'\1 \2', text)`
to insert spaces at lowercase→uppercase word boundaries in all BRENTON verse strings —
e.g. "thatI will return" → "that I will return". Dry-run confirmed: 399 of 28,156 BRENTON
verses are fixed; 0 remain fused after the pass. Known limitation: all-lowercase fusions
(e.g. "menmay") are not caught by this pattern and require a BRENTON re-fetch.

**Script:** `scripts/fix-brenton-spaces.py` — run `python3 scripts/fix-brenton-spaces.py`.

---

## Completed 2026-06-06 (loop session, iteration 2)

### NAV-4 — verse-study chapter-boundary navigation dead-end *(MEDIUM)*

Updated `loadVerseStudyVerse` in `assets/js/verse-study.js` (the prev/next nav block, lines 221–243).
At chapter boundaries (verse 1 or last verse of chapter), instead of hiding the `‹`/`›` arrows,
they now show a chapter-jump link. For prev at v=1: if `parsed.ch > 1`, shows `← Ch N-1` linking
to `bookName Ch-1:1`. For next at last verse: if `bk.chapters` allows, shows `Ch N+1 »` linking
to `bookName Ch+1:1`. Both cases set `textContent` explicitly so re-navigating to a normal verse
resets the label back to `‹`/`›`. `bk.chapters` from `metaBooks` prevents wrapping past the book end.

**Files modified:** `assets/js/verse-study.js` (prev/next nav block only).

### RI-D · Tile click feels unresponsive — active state + outside-click race *(MEDIUM)*

Three changes to fix tile click responsiveness in `assets/js/interlinear.js`:
1. Added `e.stopPropagation()` to the tile click handler in `renderReaderInterlinearRow` — prevents
   the tile click from bubbling to `document` and immediately triggering the outside-click listener.
2. Removed the `setTimeout(10)` wrapper in `_riShowPopover`'s outside-click registration — now
   uses a direct `document.addEventListener` since stopPropagation makes the race impossible.
3. Added `min-height: 44px` to `.ri-tile` in `assets/css/reader.css` (WCAG 2.5.5 touch target).
The active tile state (`ri-tile--active` class add/remove) was already wired in by the RI-A/B/C
changes in iteration 1.

**Files modified:** `assets/js/interlinear.js` (tile click handler + outside-click block), `assets/css/reader.css`.

### DATA-6 · DR / KJV-APO / WEB-CE Strong's markup contamination *(HIGH)*

Created `scripts/fix-apocrypha-strongs.py`. Walks all three contaminated directories, strips
`|strong="[HG]\d+"` tokens (replacing each with a space), collapses double-spaces, and removes
space-before-punctuation artifacts. Writes files back in-place. Dry-run count: DR 30,169 / 35,811
verses, KJV-APO 31,099 / 36,822, WEB-CE 30,375 / 35,584 would be cleaned (contamination confined
to canonical 66-book copies; apocrypha-specific books remain untouched at 0/298).

**Script:** `scripts/fix-apocrypha-strongs.py` — run `python3 scripts/fix-apocrypha-strongs.py`
to apply. Safe to re-run (no-op on already-clean files).

---

## Completed 2026-06-06 (loop session, iteration 1)

### RI-A · Popover spawns off-screen on right edge and bottom edge *(HIGH)*

Fixed `_riShowPopover` in `assets/js/interlinear.js`: removed `window.scrollY`/`window.scrollX`
from the `position: fixed` popover placement (those offsets are wrong for viewport-relative
coordinates), added right-edge clamping (`Math.min(Math.max(8, r.left), innerWidth - 280 - 8)`),
and added a `requestAnimationFrame` bottom-flip that measures `pop.offsetHeight` after render and
repositions above the tile if it would overflow the bottom edge.

### RI-B · Popover stays fixed on screen when user scrolls *(HIGH)*

Added a one-shot `{ passive: true }` scroll listener on `.reader-content` /
`#reader-results` / `window` (first found) that tears down the popover and active-tile state
when the reader scrolls. Added `_riScrollCleanup` module-level variable to hold the removal
function; called on scroll, close-button click, and outside-click so no stale listener remains.
New `_riShowPopover` calls also cancel any previous scroll listener before opening a fresh popover.

### RI-C · No "Word Study" link in popover *(HIGH)*

Added `WORD_URL` to the `import` from `./core.js` in `interlinear.js`. Appended a
`<div class="ri-popover__links">` block to the popover HTML in `_riShowPopover` containing
`<a class="vs-context-btn" href="…">Word Study →</a>` pointing to
`WORD_URL + '?s=' + encodeURIComponent(strongs)`. The `.ri-popover__links` and
`.vs-context-btn` CSS rules already existed in `reader.css` lines 2115–2125.

**Files modified:** `assets/js/interlinear.js` only (import line, module-level var, `_riShowPopover`).

---

## Completed 2026-06-05 (loop session, iteration 2)

### WS-B · Fetch Gesenius' Hebrew-Chaldee Lexicon (1857) *(HIGH)*

Gesenius is the foundational Hebrew lexicon with Semitic cognate data that grounds H codes
in Arabic/Aramaic/Syriac parallels — evidence that the semantic range is genuinely wide.

- [x] `scripts/fetch-gesenius.py` — Created. Fetches archive.org `geseniushebrew00geseuoft` (fallback IDs included); parses OCR text for Hebrew headwords; extracts `gloss`, `def`, `cognates` (sentences with language names), `root_note` (etymology sentences); maps to H codes via niqqud-exact + niqqud-stripped fallback. Outputs `data/strongs/gesenius.json`.
- [x] `scripts/seed-glossary.py` — Updated `seed_hebrew()` to load `gesenius.json` (try/except — safe if not yet run); injects `source_data.gesenius: {gloss, def, cognates, root_note}` per entry; adds `'gesenius'` to `sources`. Updated `slim()` to include `source_data.gesenius` (def≤400, cognates≤200, root_note≤150).
- [x] `assets/js/workshop.js` — `_renderDossier`: `const gesenius = src.source_data?.gesenius || {};` added; renders `_sourceCard('Gesenius (1857)', ...)` after BDB card (Hebrew section only), with `cognates` as the deriv field. INTENT/CHANGE?/VERIFY comments added.
- [x] `data/SOURCES.md` — Gesenius entry documented under Strong's section.

**To activate:** Run `python3 scripts/fetch-gesenius.py` then `python3 scripts/seed-glossary.py`.

---

### WS-C · Auto-generate biblical attested uses from interlinear *(HIGH)*

Each Strong's code now gets up to 6 representative KJV verse samples pulled directly from
the interlinear — book-diverse, with high-priority refs for theologically disputed terms.

- [x] `scripts/build-attested-uses.py` — Created. Scans all interlinear files (NT for G codes, OT for H codes) in one pass; selects ≤6 verses per code with book diversity + HIGH_PRIORITY_REFS ensuring theological key verses (John 1:1 for G3056, Psalm 136:1 for H2617, etc.) appear first. Loads KJV verse text from `data/bible/KJV/{book}.json`. Notes left blank for agent curation (WS-G). Outputs `data/strongs/attested-uses-greek.json` and `data/strongs/attested-uses-hebrew.json`.
- [x] `scripts/seed-glossary.py` — Updated both `seed_greek()` and `seed_hebrew()` to load the attested-uses files; injects `attested_uses` array per entry. Updated `slim()` to include `attested_uses[:6]` in phase bundles.
- [x] `assets/js/workshop.js` — New `_renderAttestedUses(uses)` function: `<details>` collapsible "Verse Samples" section; renders ref badge + context label + italic truncated quote + optional note per use. Wired into `_renderDossier` below the `semantic_range` headline (before Lexical Sources). INTENT/CHANGE?/VERIFY comments added.
- [x] `assets/css/workshop.css` — Added `.ws-attestation-details`, `.ws-attestation-summary`, `.ws-attestation-list`, `.ws-attestation-item`, `.ws-attestation-ref`, `.ws-attestation-ctx`, `.ws-attestation-quote`, `.ws-attestation-note`. Summary uses `<details>` open/closed arrow via `::before`. Quote uses `-webkit-line-clamp: 2` for truncation. All colors via CSS custom properties.

**To activate:** Run `python3 scripts/build-attested-uses.py` then `python3 scripts/seed-glossary.py`.
**Verify after data build:** Open G26 (ἀγάπη) — "Verse Samples" collapsible appears below semantic range. Verses from John, Paul, and at least one other NT author visible.

---

## Completed 2026-06-05 (loop session, iteration 1)

### NAV-3 · `notes/` page has no "View all" entry point — NOTES_URL is dead code *(MEDIUM)*

`NOTES_URL` was exported from `core.js` but never imported anywhere, leaving `notes/index.html`
unreachable from the UI. Added "View all notes ↗" links mirroring the bookmarks pattern:

- [x] `assets/js/modal.js`: Imported `NOTES_URL`; appended `.bsw-notes-viewall` link at the bottom of `_renderNotesPanel`'s `_innerRefresh()`.
- [x] `assets/js/reader.js`: Imported `NOTES_URL`; appended `.reader-bm-viewall` link at the end of `_loadReaderNotes()` (reuses same class as bookmarks for consistent styling).
- [x] `assets/css/reader.css`: Added `.reader-bm-viewall` rule (small right-aligned primary-color link, `display:block`; serves both bookmarks and notes panels).
- [x] `assets/css/bible-ui.css`: Added `.bsw-notes-viewall` rule (same styling as above for the modal context).

---

### WS-A · Fetch Abbott-Smith Manual Greek Lexicon (1922) *(HIGH)*

Abbott-Smith (1922) is a NT-specific lexicon with classical and LXX usage notes — a third
independent scholarly witness for Greek semantic range beyond Dodson/Thayer. All four sub-tasks complete:

- [x] `scripts/fetch-abbott-smith.py` — Created. Fetches CCEL Abbott-Smith via paginated HTML; builds lemma → G code index from `greek.json`; 3-pass Strong's mapping (in-text hint → exact lemma → diacritic-stripped fuzzy). Outputs `data/strongs/abbott-smith.json`. Run this script first, then seed-glossary.py.
- [x] `scripts/seed-glossary.py` — Updated `seed_greek()` to load `abbott-smith.json` (try/except — safe if not yet fetched); injects `source_data.abbott: {gloss, def, classical_note, lxx_note}` per entry and adds `'abbott'` to the `sources` list. Updated `slim()` to include `source_data.abbott` in phase bundles (def capped at 400 chars, classical_note at 200 chars).
- [x] `assets/js/workshop.js` — `_renderDossier`: `const abbott = src.source_data?.abbott || {};` added; renders `_sourceCard('Abbott-Smith (1922)', abbott.gloss, abbott.def, abbott.classical_note)` after Thayer, conditionally (no card rendered until `fetch-abbott-smith.py` is run). INTENT/CHANGE?/VERIFY comments added.
- [x] `data/SOURCES.md` — Abbott-Smith entry documented under Strong's section (source URL, fetch script, data path, license, purpose).

**To activate:** Run `python3 scripts/fetch-abbott-smith.py` then `python3 scripts/seed-glossary.py`.
**Verify after data fetch:** Open G3056 (λόγος) in workshop — three Greek source cards render: Dodson, Thayer, Abbott-Smith. Abbott-Smith card includes `classical_note` if CCEL markup contains "Cl." notation.

---

## Completed 2026-06-05 (session 9 — loop iteration 4)

### CODE-3 · core.js — Version-change event bus and parseMultiRef algorithm missing INTENT/CHANGE? *(MEDIUM)*

Added required comments to three functions in `assets/js/core.js`:
- `_fireVersionChange`: Added `CHANGE?` listing all four current subscribers (wire.js:updateInlineVerses, reader.js:doLookup, app.js:syncModalVersionPicker, daily.js).
- `setVersion`: Added `VERIFY` step (switch picker from KJV to ESV; confirm select updates, inline verses reload, modal version bar syncs).
- `parseMultiRef`: Added `INTENT` + `CHANGE?` + `VERIFY` explaining the carry-over state model (curBookId/curCh inherited left-to-right), the BARE_RE silent-skip edge case, and how to verify in the console.

### CODE-4 · wire.js — applyHighlights and updateInlineVerses missing CHANGE?/VERIFY *(MEDIUM)*

Added required comments to three functions in `assets/js/wire.js`:
- `autoTagRefs`: Added `INTENT` + `CHANGE?` + `VERIFY` explaining idempotency (TreeWalker skips existing [data-ref] nodes), the no-op guard (`if (!bookLookup) return`), and what to verify in the browser.
- `updateInlineVerses`: Added `CHANGE?` noting the `onVersionChange(updateInlineVerses)` registration in app.js; removing it silently stops inline verse updates on version switch.
- `applyHighlights`: Added `CHANGE?` listing all three callers (reader.js:doLookup, reader.js:injectComparePanel, modal.js:applyModalHighlights) and the note.highlight field / CSS class prefix dependencies.

### CODE-5 · modal.js — buildModalDOM singleton and cross-module bridges missing INTENT/CHANGE? *(MEDIUM)*

Added required comments to three functions in `assets/js/modal.js`:
- `buildModalDOM`: Added `INTENT` (global singleton, idempotent, module-level state persists across open/close) + `CHANGE?` (if DOM structure changes, audit openModal, closeModal, and all _renderModal* querySelector calls).
- `registerMemHelpers`: Added `CHANGE?` noting app.js calls this after importing daily.js; missing registration = Memorize tab silently empty.
- `registerModalWordStudy`: Added `CHANGE?` covering all five register* functions — called by app.js after relevant module imports; missing = tab silently empty.

---

## Completed 2026-06-05 (session 3)

### UX-1 · search.js empty catch on direct reference lookup *(MEDIUM)*
- [x] `assets/js/search.js` (`handleSearchInput`): Added `"Looking up…"` loading indicator before `loadBook()` in the direct-ref path (sets `#bsw-search-output` HTML). Replaced the empty `.catch(function(){})` with one that renders `<p class="search-page-none">Could not load "…"…</p>` in the output element. Added INTENT/CHANGE?/VERIFY comments. Used `document.getElementById` directly since `_searchOut` is defined after the early `return`.

### UX-2 · verse-study.js interlinear ghost section on network failure *(MEDIUM)*
- [x] `assets/js/verse-study.js` (`loadVerseSections`, interlinear block): Added `.catch(function () { interlinearSec.el.remove(); vsRebuildNav(); })` after the `.then()`. If `loadStrongs` or `loadInterlinear` rejects, the hidden section is removed from the DOM and the sidebar nav is regenerated cleanly instead of leaving a ghost entry. Added INTENT/CHANGE? comments in the catch.

### UX-3 · discipline/index.html "Loading plans…" never cleared *(MEDIUM)*
- [x] `discipline/index.html` (`loadAndRenderPlans`): Added `var msg=document.getElementById('plans-list-msg'); if (msg) msg.setAttribute('hidden','');` inside the `.then()` callback before `renderAllPlans()`. The static `<p id="plans-list-msg">` is now hidden as soon as plan data loads.

---

## Completed 2026-06-05 (session 2)

### PERF-2 · loadCrossRefs duplicate fetch stampede *(MEDIUM)*
- [x] `assets/js/core.js` (`loadCrossRefs`): Store the in-flight Promise in `crossRefCache[bookId]` immediately before fetch resolves. All concurrent callers now share the same Promise via `Promise.resolve(thenable)`. Once the fetch settles, the cache entry is replaced with the plain data value. Added INTENT/CHANGE?/VERIFY comments. Psalm 119's 176 concurrent cross-ref callers now fire exactly 1 HTTP request instead of 176.

### PWA-1 · Offline cache miss on parameterized URLs *(MEDIUM)*
- [x] `sw.js` (`networkFirst`): Changed `caches.match(req)` → `caches.match(req, { ignoreSearch: true })`. Cache lookups now ignore query params, matching `/discipline/index.html` for navigations to `/discipline/?tab=journal`. Added INTENT/CHANGE?/VERIFY comments. Also bumped `APP_CACHE_V` from `bsw-app-v64` → `bsw-app-v65`.

### PWA-2 · Precache sends 462 silent 404 requests for versions with no data *(MEDIUM)*
- [x] `assets/js/pwa.js` (`triggerPrecache`): Changed `metaVersions.map(v => v.id)` to filter with `!v.stub && !v.group && v.tier < 3`. Now sends only KJV, BSB, WEB, ASV — the 4 versions with actual `data/bible/{id}/` files. Eliminates 462 wasted 404 requests per background precache run (7 data-less versions × 66 books). Added INTENT/CHANGE?/VERIFY comments.

---

## Completed 2026-06-05

### AUD-1 · NT Daily devotional — Matthew chapter count bug *(HIGH)*
- [x] `assets/js/daily.js` (line 470): Changed `['matthew', 34]` → `['matthew', 28]`. Matthew has 28 chapters; the wrong count caused 6 "Chapter unavailable." days per 266-day rotation cycle. `totalNT` now correctly equals 260.

### CSS-7 · `--color-heading` undefined *(HIGH)*
- [x] `assets/css/style.css` (`:root` block): Added `--color-heading: var(--color-text);`. Resolves all 24 references across 10 CSS files; the 5 dangerous `#1a1a1a` hardcoded fallbacks (timelapse.css, maps.css, lib-progress.css, bible-ui.css) now correctly inherit the dark-mode text color `#e8dfc8` instead of remaining near-invisible.

### DATA-1 · 5 empty Bible version stubs cause 404 on every book load *(HIGH)*
- [x] `data/versions/versions.json`: Added `"stub": true` to AKJV, DBY, GNV, WEBBE, YLT (all have 0 data files in `data/bible/{id}/`).
- [x] `assets/js/core.js` (`populateVersionPicker`): Added `if (v.stub) return;` filter + INTENT/CHANGE?/VERIFY comments.
- [x] `assets/js/reader.js`: Added stub filter in compare-default picker loop, compare panel header builder, and reader translation optgroup builder (3 spots).
- [x] `assets/js/modal.js` (`syncModalVersionPicker`): Added stub filter; fixed idempotency guard from `=== metaVersions.length` to `> 0` (count no longer matches after filtering).
- [x] `assets/js/verse-study.js` (`vsRenderVersionCompare`): Added stub filter so All Translations section skips versions with no data.

---

## MKT NT Continuation — Completed 2026-06-03

**Acts complete (28/28 chapters, 1,007 verses)** and **1 Thessalonians complete (5/5 chapters, 89 verses)**.
Luke 19-24 was already complete (prior agent); confirmed by mkt-luke-19-21.py re-pass.

### Scripts created this session
- [x] `scripts/mkt-1thessalonians-1-5.py` — all 5 chapters, 89 verses; three-tier translation written.
  Key decisions: παρουσία="coming" (L/M/T), κοιμάω="fallen asleep" (L/M)/"died" (T in 4:13),
  4:16-17 rapture passage rendered clearly, tripartite formula (spirit/soul/body) preserved in 5:23.
- [x] `scripts/mkt-acts-16-21.py` — Acts 16-21, 221 verses; covers Philippi (Lydia, jailer),
  Athens Areopagus speech, Corinth, Ephesus (Artemis riot), Miletus farewell to elders.
- [x] `scripts/mkt-acts-22-28.py` — Acts 22-28, 226 verses; covers Paul's defense speeches,
  voyage and shipwreck (Malta), arrival in Rome. Acts 24:7 and 28:29 (Western text) added.
- [x] `scripts/mkt-luke-19-21.py` — Luke 19-21, 133 verses; confirmation pass (Luke already complete).
  Covers Zacchaeus, Triumphal Entry, Temple cleansing, debates, Olivet Discourse.
- [x] MKT_PROGRESS.md updated: Complete 56 books / 1,069 chapters / 26,619 verses; no Partial books.

### Phase Z spec (Z1–Z4, Z1a, Z3a stubs)
Full design documents for MKT three-tier philosophy, contested-terms table, glossary schema,
Z2 expansion layer, Z3 commentary pipeline, Z4 versioning strategy, and Z1a landing page
were in TODO.md Phase Z section — moved here as they are planning docs, not active tasks.
The translation (Z1) is >85% complete by verse count. Z2-Z4 remain long-term stubs.

---

## Apocryphal Reader — Data Fetch Completed 2026-06-03

The apocrypha reader UI was already built (`apocrypha/index.html`, `apocrypha-reader.js`, `apocrypha.css`). This pass fetched all Bible text data for the four registered apocrypha versions.

**Script fixes applied to `scripts/fetch-apocrypha.py`:**
- eBible.org URL scheme changed: old `engwebcont_readaloud.zip`-style IDs renamed; updated to `_usfm.zip` pattern with correct IDs (`eng-web-c`, `eng-kjv`, `eng-Brenton`, `engDRA`)
- DR source changed from broken wldeh CDN (403 Forbidden) to eBible.org `engDRA_usfm.zip`
- Nahum USFM code corrected: `NAH` → `NAM` (USFM v3 standard)
- Added Strategy 4 for Catholic Esther/Daniel: `EST`/`DAN` not found → fall back to `ESG`/`DAG`
- Added Psalm 151 extraction: embedded in LXX Psalms USFM ch 151 → extracted as standalone 1-ch book

**Data fetched — `data/bible-apocrypha/`:**
- **DR**: 73 books (66 canonical + 7 deuterocanon: Tobit, Judith, 1-2 Maccabees, Wisdom, Sirach, Baruch)
- **WEB-CE**: 74 books (66 canonical with Greek Esther ESG/Daniel DAG + 8 deuterocanon)
- **KJV-APO**: 80 books (66 canonical + 14 Protestant Apocrypha)
- **BRENTON**: 51 books (OT-only LXX translation — NT not in Brenton; 15 deuterocanon)

**All 17 apocryphal books covered** across at least one version (core Catholic deuterocanon in all 4; Orthodox additions in BRENTON; 2 Esdras only in KJV-APO; Psalm 151 only in BRENTON from LXX Psalms ch 151).

**SOURCES.md updated** with all 4 apocrypha version sources, URLs, fetch commands, and licenses.

---

## Library Apologetics Expansion — Partial Completion 2026-06-03

2 of 10 planned apologetics docs added (remaining 8 are data-blocked — source not available on Wikisource/CCEL/Gutenberg):

- [x] **To Autolycus** (Theophilus of Antioch, c. 180) — `theophilus-autolycus.html`; fetched from ANF Vol II Wikisource (Books I–III); 3 sections; tradition: patristic; validates PASS
- [x] **The Christian View of God and the World** (Orr, 1893) — `orr-christian-view.html`; fetched from CCEL (5 grouped sections, 18 pages: Lectures I–IX + appendices); tradition: reformed; validates PASS
- [x] `data/library/index.json` — both entries added (theophilus-autolycus at [20], orr-christian-view at [158])
- [x] `data/library/search-index.json` — rebuilt 2974 entries / 190 docs
- [x] `data/SOURCES.md` — "Apologetics Documents — Patristic & 19th Century (2026-06-03)" section added

Data-blocked (source not accessible): Lactantius Divine Institutes, Summa Contra Gentiles, Hooker Ecclesiastical Polity, Grotius Truth of Christian Religion, Locke Reasonableness of Christianity, Orr Virgin Birth, Warfield Counterfeit Miracles, Warfield Lord of Glory

---

## Liturgical Docs — Patristic items (Hippolytus, Calvin Geneva Liturgy, Wesley Sunday Service) — Data-Blocked 2026-06-03

- Apostolic Tradition (Hippolytus) — SKIPPED per user
- Geneva Liturgy (Calvin, 1542) — SKIPPED per user  
- Sunday Service of the Methodists (Wesley, 1784) — Not on Wikisource, CCEL, or Project Canterbury with findable path

---

## Bible Reader — RD-I and RD-M — Completed 2026-06-03

- [x] **RD-I** — Book Info navigates to `ch=0` via `_readerLookupFn()`; no separate inline panel; old `_refreshBookInfoPanel` / `_bookInfoCache` code removed
- [x] **RD-M** — Commentary Mode: `reader-comm-toggle` button in browse bar; `_activateCommMode()` prefetches all commentary sources, calls `_buildCommGrid()`; 2-column per-verse grid (verse 20% / commentary 80%); per-verse source `<select>`; `_deactivateCommMode()` re-renders via `_readerLookupFn()`; xref panel hidden and layout goes full-width while active; all `.reader-comm-*` CSS present

---

## Bible Reader — Navigation Items (RD-A, RD-C, RD-H, RD-J, RD-K) — Completed 2026-06-03

- [x] **RD-A** — `_navigateChapter` uses in-page pattern (`input.value` + `_readerLookupFn()`) for all three branch cases; no `window.location.href` assignments remain; ch=0 intro path unchanged as model
- [x] **RD-C** — Resume banner (`reader-resume-banner`) injected when `refStr` is empty and `bsw_history[0]` exists; dismiss writes to `sessionStorage`; CSS: muted surface + `--color-primary` left border
- [x] **RD-H** — Empty-state (`reader-empty-state`) rendered when no `?ref=` and no history; quick-start chips: John 1, Psalm 23, Romans 8, Genesis 1, Isaiah 53
- [x] **RD-J** — `attrEl.hidden = g.ref.v && !g.ref.endV`; attribution suppressed for single-verse lookups
- [x] **RD-K** — `@media (max-width:700px) { .reader-browse-hint { display:none; } }`

---

## Maps Page Improvements — Phase 2 & Phase 3 — Completed 2026-06-03

### Phase 2 — Visual & Content

- [x] **Twelve Tribes — Permanent Tribe Labels** — `_renderTwelveTribes()` adds `L.divIcon` tribe-name labels at each polygon centroid; always-visible (not just on hover). CSS: `.maps-tribe-label { pointer-events:none; font-size:.65rem; font-weight:700; text-align:center; … }` matching `.tl-region-label` pattern.
- [x] **City `significance` field** — `_showCityDetail()` reads `city.significance`; `<div id="maps-city-significance">` rendered in detail panel. Present in all city datasets.

### Phase 3 — New Maps

- [x] **`_renderSevenChurches()`** — Seven churches of Revelation with markers and significance text; added to `MAPS[]` in New Testament group.
- [x] **`_renderReturnExile()`** — Return from Babylonian captivity map; added to `MAPS[]`.
- [x] **`_renderJerusalem()`** — Ancient Jerusalem close-up (zoom 14–15, center [31.7767, 35.2345]); key sites: Temple Mount, City of David, Pool of Siloam, Gethsemane, Golgotha / Church of the Holy Sepulchre, Upper Room area, Antonia Fortress. Each as a clickable marker with `significance` text. Entry added to `MAPS[]` as `id: 'jerusalem', label: 'Ancient Jerusalem', group: 'New Testament'`.

---

## CON-A · History Hub — Completed 2026-06-03

Unified Timeline, Church History, Maps, and Animated Map into a single hub.

- [x] **`history/index.html`** — sticky tab-bar hub; 4 tabs (timeline, church, maps, timelapse); lazy iframe `src` assignment on first tab click; URL state via `?tab=`; localStorage persistence; Leaflet `invalidateSize()` fired on timelapse tab to fix hidden-container init.
- [x] **`assets/js/main.js`** — `History` nav group added with 4 links (Biblical Timeline, Church History, Maps, Animated Map); timeline/maps entries removed from Reference group; church-history removed from Library group; `?minimal=1` guard in `buildSidebar()` returns early to suppress sidebar inside hub iframes.
- [x] **`assets/css/style.css`** — `.hist-back-link` (minimal-embed back-link pill) and `.hist-iframe` (100% width/height borderless iframe) added.
- [x] **Back-links** — `← History` link added to `timeline/index.html`, `church-history/index.html`, `maps/index.html`, `maps/timelapse/index.html`; shown only when `?minimal=1` URL param present.

---

## Timeline UX Improvements (TLU-A through TLU-K) — Completed 2026-06-03

Primary files: `assets/js/timeline.js`, `assets/css/timeline.css`, `timeline/index.html`, `church-history/index.html`, `data/timeline/events.json`, `data/timeline/church-detail.json`

- [x] **TLU-A** — URL state: `_selectEra` / `_clickEvent` write `history.replaceState`; `init()` reads `?era=` + `?event=` and restores selection; close restores `?era=` only
- [x] **TLU-B** — Session persistence: `storageKey` in `cfg` (`bsw_tl` / `bsw_chtl`); `_selectEra` / `_clickEvent` write sessionStorage; init falls back to sessionStorage when no URL params
- [x] **TLU-C** — Prev/Next nav bar added to `_buildDetailShell`; `_clickEvent` computes `idx` within era events; `_wireDetailNav` wires ← Prev / N of M / Next → buttons
- [x] **TLU-D** — `_buildDetailBody` appends crossover div for biblical `church` era events; `church-history/index.html` gets `← Biblical Timeline` backlink in subtitle
- [x] **TLU-E** — `CHURCH_LIB_LINKS` constant maps 9 church events to library docs; `_buildDetailBody` renders 📖 chips for isChurch events; CSS: `.tl-detail-lib-links` / `.tl-detail-lib-chip`
- [x] **TLU-F** — `church-detail.json` key_texts updated with doc-title entries for nicaea-i, chalcedon, westminster, luther-95-theses, diet-of-worms, council-orange, benedictine-rule
- [x] **TLU-G** — `_makeEraNode` shows event-count badge; `_markExtrabiblical()` appends ⛏ to event nodes with `extrabiblical` data
- [x] **TLU-H** — `_proportionalPositions` treats `yearNum === null || >= 9000` as pinned at 95%; `new-creation` event patched to `yearNum: null`; era node year label shows "—" for consummation
- [x] **TLU-I** — `<input class="tl2-search">` in both HTML files; `_handleSearch` dims non-matching era nodes, renders flat search results in events column
- [x] **TLU-J** — Mobile breadcrumb `era › event` prepended to `.tl-detail-inner`; `display:flex` at `max-width:820px`
- [x] **TLU-K** — Removed `target="_blank" rel="noopener"` from `.tl-detail-map-chip` and `.tl-detail-ref-link`

---

## Omni-Search Improvements (OS-A through OS-J) — Completed 2026-06-03

Primary files: `assets/js/search.js`, `assets/css/bible-ui.css`, `search/index.html`

- [x] **OS-A** — Sort buttons and testament filter initialized with active state on page load; testament filter unified to `search-mode-btn--active`
- [x] **OS-B** — `renderSearchResults` post-filters by `_filterTestament`/`_filterBook` after sorting; switching filters immediately re-scopes loaded results
- [x] **OS-C** — `_fireSearch` promoted to module-level var; history chip click handler uses `if (_fireSearch) _fireSearch()`
- [x] **OS-E** — `?tab=explore` URL param switches tab and fires explore search; `?tab=explore&q=...` deep-links correctly
- [x] **OS-F** — `data-explore-count` spans added to every section head; `_setExploreCount()` helper called from all 8 section renderers
- [x] **OS-G** — `_exploreTorrey()` added; "Torrey Topics" section + filter button; uses `_torreyLoad`/`_torreyData` from core.js
- [x] **OS-H** — `_exploreNames()` added; "Bible Names" section + filter button; uses `_hitchLoad`/`_hitchData`
- [x] **OS-I** — "No cached matches." → "Switch to Verse Search for full results." in `_exploreVerses`
- [x] **OS-J** — Second tab click listener re-renders `_lastSearchResults` immediately on return to Verse Search tab

---

## Home Page Improvements (HP-A through HP-I) — Completed 2026-06-03

Primary files: `index.html`, `assets/js/daily.js`, `assets/css/daily.css`

- [x] **HP-A** — Card order: VOTD → Reading → Devotional → Disciplines → Streak → Continue
- [x] **HP-B** — Reading Plan on-track/behind/ahead badge: `expectedPct` from `dn/plan.total_days`; `.daily-plan-pace` CSS with `--ahead`/`--behind`/`--on-track` modifiers
- [x] **HP-C** — Disciplines: `#daily-tracker-count` span; `renderTracker()` counts done items and memory due; `.daily-tracker-count` + `.daily-mem-badge`
- [x] **HP-D** — Verse of the Day: `.daily-votd-ref` link wires to reader; `.daily-votd-actions` copy button
- [x] **HP-E** — Devotional card: `.daily-dev-actions` with archive and share buttons; streak counter
- [x] **HP-F** — Continue Reading: `bsw_history[0]` from localStorage shown as resume chip; dismissable
- [x] **HP-G** — Memory card: due-today badge; verse queue with swipe/tap reveal
- [x] **HP-H** — Streak card: current and longest streak from localStorage plan history
- [x] **HP-I** — Mobile layout: single-column stacking; card max-width constraint at ≥900px

---

## REF-A · Smith's Bible Dictionary Verse-Index — Completed 2026-06-03

- [x] `scripts/build-dict-verse-index.py`: `--source` flag added (easton | smith | both, default both); Smith extraction handles Unicode replacement chars; Song of Songs/Solomon aliases added
- [x] Run: `python3 scripts/build-dict-verse-index.py --source smith` → 65 book files, 8,823 verse entries in `data/smith/verse-index/`
- [x] `assets/js/library.js` (`_dictEntriesForVerse`): `SMITH_VIDX_URL`, `_smithVidxCache`, `_smithLoadVidx` — Smith and Easton indexes loaded in parallel, merged and deduplicated
- [x] `assets/js/library.js` (`renderVSDictionary`, `renderModalDictionary`): E/S source badges; Smith entries routed to `?src=smith&entry=...`; `_smithMap` used for brief descriptions

**Outcome:** Smith: 65 books / 8,823 verse entries. Easton: 66 books / 12,544 verse entries. Both surfaced in verse modal Dictionary tab and Verse Study Dictionary section.

---

## B4a — PWA / Service Worker Audit — Completed 2026-06-03

Audit found and fixed four gaps:
- **21 missing assets** (8 CSS, 11 JS) and **10 missing HTML pages** added to `sw.js` SHELL_URLS. Newly-added pages (history hub, apocrypha, discipline, timelapse, tracker, etc.) were not in the shell cache — users hitting those pages offline got nothing.
- **`APP_CACHE_V` bumped** `v63` → `v64` to invalidate all client caches and force re-install.
- **`manifest.json` `id` field** added (`"./"`) for stable PWA identity across URL changes (Chrome 96+).
- **`apple-touch-icon`** injected by `pwa.js` `initPWA()` — iOS home-screen installs now get the app icon instead of a webpage screenshot.

All 169 SHELL_URLS entries verified against filesystem — no dead URLs.

---

## Library Expansion — Liturgical & Church-Order Documents — Completed 2026-06-03

Added 2 liturgical documents via `scripts/fetch-library-docs.py`. Both PASS `validate-library-format.py`.

**Bug fix:** `remove_style_attrs` in `clean-library-html.py` updated to use `'style' in tag.attrs`
instead of `tag.get("style")` — the old check skipped empty `style=""` attributes (falsy in Python).

**Docs added:**
- [x] `book-of-common-prayer`: *Book of Common Prayer (1662)* — 4 sections from Wikisource "Book of
  Common Prayer (1892)" (Morning Prayer, Evening Prayer, The Holy Communion, The Litany); type: liturgy;
  tradition: anglican; era: post-reformation; author: Church of England
- [x] `apostolic-constitutions`: *Apostolic Constitutions (c.380)* — 6 sections (36 Wikisource
  sub-pages grouped by book pairs: Intro+Book I, Book II, Books III–V, Book VI, Book VII, Book VIII);
  type: liturgy; tradition: patristic; era: patristic; author: Unknown (attr. Clement of Rome)

**Manifest entries added** to `scripts/fetch-library-docs.py` near end of MANIFEST.
`scripts/clean-library-html.py` MEDIAWIKI_DOCS list updated to include both new docs.

**Deferred (no clean PD English text found):** Westminster Directory (1645), Form of Presbyterial
Church Government (1645), German Mass (Luther, 1526), Geneva Liturgy (Calvin, 1542), Strasbourg
Liturgy (Bucer, 1539), Sunday Service of the Methodists (Wesley, 1784), General Rules (Wesley, 1743),
Apostolic Tradition (Hippolytus, c.215), BCP Ordinal/Baptism/Catechism sub-pages.

---

## Library Expansion — Missions & Biography Works — Completed 2026-06-03

Added 2 foundational missions/biography works to the library. Both PASS validate-library-format.py.

**Script improvements made:**
- `fetch-library-docs.py`: `_is_heading_div` now handles Gutenberg `div.chapter` heading-only wrappers (relaxed text match for embedded page numbers)
- `fetch-library-docs.py`: `_clean_gutenberg_soup` now strips Gutenberg start-marker boilerplate (`*** START OF THE PROJECT GUTENBERG ***`) and `.tnotes` divs
- `fetch-library-docs.py`: `_wrap_sections` now injects `<h2 class="lib-section__title">` as first child of every section (BSW v2 R3 compliance)
- `clean-library-html.py`: `clean_artifacts` now strips auto-generated class names from h1–h6 heading tags (was only p/td/th/a/span/div)
- Both docs added to `GUTENBERG_DOCS` list in `clean-library-html.py`

**Docs added:**
- [x] `brainerd-journal`: *The Life of David Brainerd* (David Brainerd, ed. Jonathan Edwards, 1749) — Gutenberg #65066; 14 sections; type: devotional; tradition: reformed; era: modern
- [x] `carey-enquiry`: *An Enquiry into the Obligations of Christians* (William Carey, 1792) — Gutenberg #11449; 9 sections; type: father; tradition: reformed; era: modern

---

## Library Apologetics Expansion — Partial 2026-06-03 (5 of 15 docs)

Added 5 apologetics texts to the library. All PASS validate-library-format.py; all in index.json and search-index.json.

**Scripts updated:**
- `scripts/fetch-library-docs.py`: added manifest entries for chesterton-heretics (Wikisource Heretics/1–20), aristides-apology (Wikisource ANF Vol IX), minucius-felix-octavius (Wikisource ANF Vol IV chapters 1–41), butler-analogy (Gutenberg #3237), paley-natural-theology (Gutenberg #35201)
- `scripts/clean-library-html.py`: added all 5 new docs to MEDIAWIKI_DOCS or GUTENBERG_DOCS lists

**Docs added:**
- [x] `chesterton-heretics`: *Heretics* (G.K. Chesterton, 1905) — Wikisource; 20 sections; type: apologetics; tradition: catholic; era: modern; series: chesterton vol 3
- [x] `aristides-apology`: *Apology of Aristides* (Aristides of Athens, c. 140) — Wikisource ANF Vol IX Syriac tr.; 2 sections; type: apologetics; tradition: patristic
- [x] `minucius-felix-octavius`: *The Octavius* (Minucius Felix, c. 200) — Wikisource ANF Vol IV, 41 chapters; 2 sections; type: apologetics; tradition: patristic
- [x] `butler-analogy`: *The Analogy of Religion* (Joseph Butler, 1736) — Gutenberg #3237; 4 sections; type: apologetics; tradition: anglican
- [x] `paley-natural-theology`: *Natural Theology* (William Paley, 1802) — Gutenberg #35201; 27 sections; type: apologetics; tradition: anglican

**Remaining in working/inprogress-lib-apologetics-todo.md:**
- To Autolycus, Lactantius, Aquinas, Hooker, Grotius, Locke, Butler (full), 2× Orr, 2× Warfield

---

## Reformation-Era Library Works — Completed 2026-06-03 (4 of 5)

Added 4 primary Reformation-era works to the library. All pass validate-library-format.py.
Melanchthon Loci Communes remains blocked (no public domain English translation exists).

- [x] **scripts/fetch-reform-works.py** — new fetch/convert script (EEBO-TCP GitHub + archive.org)
- [x] **tyndale-obedience.html** — Tyndale, Obedience of a Christian Man (1528), 16 sections, TCP A14136 (CC0)
- [x] **zwingli-true-false-religion.html** — Zwingli, Commentary on True and False Religion (1525), 9 sections, 1929 Preble tr. (public domain 2025; IA `latinworkscorres03zwin`)
- [x] **bullinger-decades.html** — Bullinger, Decades I–II (1577), 20 sections, TCP A17183 (CC0)
- [x] **cranmer-defence.html** — Cranmer, Defence of the Sacrament (1550), 5 sections, TCP A19571 (CC0)
- [x] **data/library/index.json** — 4 new entries added (152 total)
- [x] **data/library/search-index.json** — rebuilt (2836 entries, 160 docs)
- [x] **data/SOURCES.md** — EEBO-TCP + archive.org source section updated

---

## REF-F · ISBE — International Standard Bible Encyclopaedia — Completed 2026-06-03

Added the ISBE (James Orr ed., 1915) as a sixth dictionary source. Source: CrossWire SWORD module (ISBE.zip, v2.2, public domain).

**What was done:**
- `scripts/fetch-isbe.py` — new script; parses SWORD zLD module (same format as Easton's); downloads 9,380 articles with TEI→HTML conversion, ref extraction, and 200-char brief cap; writes `data/isbe/{slug}.json` + `data/isbe/index.json`
- `scripts/build-dict-verse-index.py` — extended `--source` choices to include `isbe` and `all`; added ISBE build block; run to produce `data/isbe/verse-index/` (66 book files, 24,736 verse entries)
- `assets/js/core.js` — added `ISBE_IDX_URL`, `ISBE_ENTRY_URL` constants; `_isbeData/_isbeMap/_isbeByLetter/_isbeLoading/_isbeEntryCache` exports; `_isbeLoad()` and `_isbeLoadEntry()` functions with INTENT/CHANGE?/VERIFY comments
- `assets/js/library.js` — imported ISBE functions from core.js; added `ISBE_VIDX_URL` + `_isbeVidxCache`; added `_isbeLoadVidx()` function; extended `_dictEntriesForVerse()` to load ISBE verse index; added ISBE to `OMNI_SOURCES` (badge `'IS'`, badgeColor `'#1e3a5f'`); updated `renderVSDictionary` + `renderModalDictionary` source routing for IS badge; added `'isbe'` to the lazy-load list
- `data/SOURCES.md` — split the combined ISBE/Easton/Smith entry into three separate entries with full metadata; added ISBE with URL, fetch script, data path, entry counts, module version

**Verification:** Browser test confirmed ISBE filter chip appears in dictionary page filter bar; search for "Atonement" returns 14 results with multiple IS-badged entries; "Atonement" entry shows E + IS + NV badges correctly.

---

## Library Expansion — Creeds and Confessions — Completed 2026-06-03

Added 7 missing confessions to the library from Wikisource and Project Gutenberg:

1. **Gallican Confession (1559)** — `gallican-confession` — Wikisource (Creeds of Christendom Vol. III) — 3 sections, ~5,600 words
2. **Scots Confession (1560)** — `scots-confession` — Wikisource — 27 sections (full 25 chapters + preface), ~8,100 words
3. **Apology of the Augsburg Confession (1531)** — `apology-augsburg-confession` — Gutenberg #6744 (Bente/Dau tr.) — 12 sections, ~110K words
4. **Luther's Large Catechism (1529)** — `luther-large-catechism` — Gutenberg #1722 (Bente/Dau tr.) — 10 sections, ~48K words
5. **New Hampshire Confession of Faith (1833)** — `new-hampshire-confession` — Wikisource — 1 section (18 articles as list)
6. **Abstract of Principles (1858)** — `abstract-of-principles` — Wikisource — 20 sections (I–XX)
7. **Methodist Articles of Religion (1784)** — `methodist-articles-of-religion` — Wikisource — 1 section (25 articles)

**Files changed:** `scripts/fetch-library-docs.py` (manifest additions), `data/library/index.json` (+7 entries → 148 total), `data/library/html/{7 files}.html`, `data/library/docs/{7 files}.json`, `data/library/search-index.json` (rebuilt, 2624 entries/149 docs), `data/SOURCES.md`.

**Items not found on accessible sources (skip):** Formula of Concord, Treatise on Power of Pope, Second Helvetic Confession (CCEL blocked), Geneva Catechism, Irish Articles, First London Baptist Confession, Lambeth Articles, Philaret's Longer Catechism, Cambridge Platform.

---

## MAP-F · Centralize Recurring City Coordinates — Completed 2026-06-03

Added `var COORDS` constant to `assets/js/maps.js` (after TILE_URL block, before MAPS array) with 15 canonical city entries: jerusalem, damascus, babylon, antioch, rome, ephesus, nineveh, caesarea, carchemish, haran, athens, corinth, troas, miletus, alexandria. Replaced 100 coordinate literals across all render functions with `COORDS.<name>` (array form) or `COORDS.<name>[0]`/`[1]` (lat/lon object form). Also normalized minor drift in Jerusalem (31.78/31.7767 → 31.777) and Ephesus (37.939 → 37.94) forms. Three coordinates intentionally excluded: Jerusalem map viewport center (different purpose), a Dead Sea area polygon point, and the Mount of Olives marker.

---

## Home Page Improvements — Completed 2026-06-03

**HP-A · Card Order:** Reordered home page sections to morning-flow priority: VOTD → Reading → Devotional → Disciplines → Continue Reading. Reading streak merged into the Reading card (not a separate card). Studies card added alongside by SG-I work.

**HP-B · Reading Plan Pace Badge:** `daily.js` `_dailyRenderPlan` computes `expectedPct` from `dn / plan.total_days`; appends `<span class="daily-plan-pace daily-plan-pace--{ahead|behind|on-track}">` to the progress text. `daily.css` adds `.daily-plan-pace` with green/red/muted color variants.

**HP-C · Disciplines Completion Count + Memory Due Badge:** `index.html` inline script adds `<span id="daily-tracker-count">` to the card head, updated by `renderTracker()` to show "N / 7 complete". `renderTracker()` also reads `bsw_memory` and appends `.daily-mem-badge` to the Scripture Memory row when due count > 0. CSS added for both elements.

**HP-D · Devotional Source Chips:** Replaced `<select id="daily-devot-select">` with a `<div class="daily-devot-chips">` row of five chip buttons (Morning, Evening, Psalms, Proverbs, NT Daily). `daily.js` wires click handlers with `.daily-devot-chip--active` toggle and `bsw_daily_devot` localStorage persistence. CSS scrolls horizontally on mobile.

**HP-E · Streak Empty State:** Streak is embedded in the reading card. When `streak.current === 0`, shows `.daily-plan-streak-empty` with "Open the Bible reader to start your streak" rather than hiding any UI. CSS styles the empty state text.

**HP-F · VOTD Actions:** `daily.js` `_dailyRenderVOTD` appends `.daily-votd-actions` row with Copy, Memorize (☆/⭐ toggle via `_memHas`/`_memAdd`), and Share image (via `_shareVerseAsImage` imported from `modal.js`) buttons. CSS adds `.daily-votd-actions` and `.daily-votd-btn` pill-button styles.

**HP-G · Quick Verse Search:** `index.html` adds `.daily-search-row` form between the greeting header and first card. Inline script submits to `read/?ref=...` on non-empty input. CSS adds search row, input, and button styles.

**HP-H · Mark Today Done:** `daily.js` `_dailyRenderPlan` adds "✓ Mark today as done" button for non-catechism plans; disabled "✓ Done" when already completed. Click handler writes to `bsw_plans` localStorage and calls `markDone('reading')` to sync the disciplines tracker. CSS adds `.daily-mark-done-btn` and `--done` modifier.

**HP-I · Library Tradition Chip:** `lib-reader.js` `_saveLibProgress` already writes `tradition` to the `bsw_lib_progress` entry. `index.html` `renderLibHistory` renders `<span class="daily-hist-tradition">` when `d.tradition` is present. CSS adds `.daily-hist-tradition` chip styles.

---

## Picture Builder Improvements — Completed 2026-06-03

**PB-A · Open Source Scenery Backgrounds:** Generated 10 gradient-based scene JPEGs (dawn, mountains, sea, desert, wheat, olive, forestl, stars, jerusalem, rain) at 1200×630 using Python PIL — stored at `assets/share-scenes/`. Added `_SHARE_SCENES` array to `modal.js` with overlay/textColor/accentColor per scene. `_drawShareCanvas` now returns a Promise; scene draw loads image via `new Image()` (cover-fit + overlay), falls back to dark solid on error. Attribution line drawn in semi-transparent white. `_resolve` imported from `core.js` for site-root-agnostic scene URL.

**PB-B · Cursive Font Option:** Downloaded `DancingScript-Regular.woff2` (OFL v29) to `assets/fonts/`. Added `@font-face` to `assets/css/style.css` with `font-display: swap`. Added `{ id: 'dancing', label: 'Cursive', stack: "'Dancing Script', cursive" }` to `_SHARE_FONTS`. `_drawShareCanvas` awaits `document.fonts.load('40px "Dancing Script"')` before painting when dancing font selected; starts font size at 52px (larger internal whitespace).

**PB-C · Visual Gallery UI:** Replaced dot-swatch preset row and font-chip row with scrollable 96×54 thumbnail galleries. Solid presets show inline-styled div with bg color + accent bars + sample text. Scene cards show `<img>` thumbnail. Font cards show "For God / so loved" in each font's stack. Selected card gets 2px primary ring + scale(1.06) via `:has(input:checked)` CSS. `assets/css/bible-ui.css`: added `.bsw-share-bg-gallery`, `.bsw-share-font-gallery`, card/thumb/label/sep rules; removed old `.bsw-share-preset-row`, `.bsw-share-preset`, `.bsw-share-preset__dot`, `.bsw-share-font-row`, `.bsw-share-font-chip` rules.

---

## Reference Data Expansion — Completed 2026-06-03

**REF-B · Robertson's Word Pictures (substituted for Vincent's):** `scripts/fetch-more-commentaries.py` — added `rwp` module (RWP.zip, CrossWire); fetched 7,201 sections across 27 NT books to `data/commentary/rwp/`. `assets/js/core.js` `COMMENTARY_SOURCES` — added `{ id: 'rwp', label: "Robertson's Word Pictures", attr: "Robertson's Word Pictures in the NT (A.T. Robertson, 1930–1933; Public Domain)" }`. `data/SOURCES.md` — added Robertson's Word Pictures entry. Note: Vincent.zip is not hosted on CrossWire (confirmed 404); RWP serves the same purpose (NT-only, Greek word-meaning focused) and is more comprehensive.

**REF-C · Wesley's Explanatory Notes:** `scripts/fetch-more-commentaries.py` — added `wesley` module (Wesley.zip, CrossWire); fetched 15,649 sections across 64 books to `data/commentary/wesley/`. `assets/js/core.js` `COMMENTARY_SOURCES` — added `{ id: 'wesley', label: "Wesley's Notes", attr: "Wesley's Explanatory Notes on the Bible (John Wesley, 1765; Public Domain)" }`. `data/SOURCES.md` — added Wesley's Notes entry. First Arminian/Methodist commentary on the site.

---

## Initial Features (Pre-Phase)

- [x] **Bible Reader** (`read/index.html`) — full-chapter and verse-range lookup, URL-shareable `?ref=` params, version switcher, split text + cross-refs layout
- [x] **Full-text search** (`search/index.html`) — version-aware search across all 66 books, fuzzy multi-word matching, exact-quote mode, live progress
- [x] **Verse tooltip + modal system** — hover preview, click-to-modal, focus/keyboard accessible, per-version rendering
- [x] **Version picker** — localStorage persistence, all pages synced
- [x] **Auto-tagging of scripture refs** in topic page prose (bare refs, ch:v, "Ch. N", continuations like "; 3:4")
- [x] **Cross-references (TSK) in verse modal** — data: `data/crossrefs/` (66 books), split panel in modal and reader
- [x] **Matthew Henry Commentary in verse modal** — data: `data/commentary/` (66 books), Commentary tab in modal
- [x] **Chapter navigation in Bible Reader** — Prev/Next buttons (top + bottom), book/chapter browse dropdowns, keyboard shortcuts (j / → next, k / ← prev)
- [x] **Parallel Passage Reader** — toggle in reader toolbar; stacked panels with fulfillment/prophecy/parallel type badges; lazy fetch with `bookCache` reuse; localStorage persistence (`bsw_parallels`); CSS in `reader.css`; data in `data/parallels/`

---

## Bugs Fixed

- [x] **BUG-1. Memory — completing the last card does nothing**
  - After scoring the final card in a review session, the UI sits on a blank or stale state with no feedback
  - Add a "completion card" that appears after the last card is scored: brief encouragement text
    (e.g., "Session complete — well done! You reviewed N verses."), today's review count, and a
    button to return to the Browse panel
  - Check `_memNextCard()` in `bible.js` — the path where `pendingCards` empties after the last
    score needs to render the completion view rather than calling `_memShowCard()` again
  - Completion state should also update the summary stats visible in the Browse panel

- [x] **BUG-2. Commentaries not visible in the Reader pane**
  - The Commentary tab in the verse modal works, but the Reader's right-hand pane does not show
    commentary content when selected
  - Trace `_refreshCommentaryPanel()` (or equivalent) in `bible.js` — check whether the call is
    wired to the reader's cross-ref panel tab switcher or whether the fetch/render path silently fails
  - Expected behavior: selecting "Commentary" in the reader right-pane tab loads the relevant
    commentary entry for the currently visible passage, identical to the modal's Commentary tab

- [x] **BUG-3. Topics tab in verse modal needs more breathing room**
  - The Topics tab content (Nave's topic chips) is visually cramped — insufficient padding between
    the chip row, the count line, and the "Browse all" link (see screenshot: chips sit flush against
    the tab border)
  - Add `padding-top` / `gap` adjustments to the `.bsw-modal-topics` container in `bible-ui.css`;
    match the visual rhythm of the Verse and Commentary tabs

- [x] **BUG-4. Search page label still reads "Omni-search" — should be "Search"**
  - The search page (`search/index.html`) heading or tab label was renamed to "Omni-search" during
    development but should simply read "Search" in all user-visible text
  - Update: page `<title>`, `<h1>` / heading element, sidebar nav entry in `main.js`, and any
    `aria-label` or placeholder text that still says "Omni-search"

- [x] **BUG-5. Book-study banner doesn't clear when navigating to a book with no study**
  - When a book with an available study is selected in the Reader, the "Study available" banner appears
  - Navigating to a different book that has no study should clear the banner; navigating to a book
    that has a study should update it to that book's study
  - Locate the banner-render call in `bible.js` (triggered on book/chapter load); ensure it runs
    on every navigation event, not just on initial page load or when a study is found — an explicit
    "hide banner" path is needed for the no-study case

- [x] **BUG-6. Notes in the Reader pane cannot be deleted**
  - Personal notes added to verses are visible in the Reader's notes panel but there is no delete
    button or action — once created, a note can only be edited, not removed
  - Add a delete (×) button to each note entry in the Reader pane; wire it to the existing
    `deleteNote(refStr)` function (or add that function if absent) which removes the entry from
    `bsw_notes` / `bsw_notes_v2` and re-renders the panel
  - Confirm the delete button also exists (or is added) in `notes/index.html` for consistency

---

## Phase A — Foundation ✓ Complete

- [x] **A1. Library pages** — all 6 pages were already built with full content
- [x] **A2. Nav consistency** — `main.js` sidebar includes Topics + Library on all pages
- [x] **A3. `main.js` nav data** — full NAV structure with Topics and Library subgroups
- [x] **A4. Delete `_includes/`** — stale Jekyll includes removed
- [x] **A5. Reader 3-column layout** — `reader-page .container` → 1400px; grid: narrow=1col, medium 700px+=2col (text|xref panel), wide 1100px+=3col (ch-sidebar|text|xref panel); cross-ref side panel populated by `_refreshXrefPanel()` after each book's refs load

---

## Phase VS — Verse Study (Deep Dive)

- [x] **VS1. Verse Study page** (`verse-study/index.html?ref=John+3:16&v=BSB`) — sticky header with focal verse + context strip, word token row, cross-references, Matthew Henry commentary, parallel passages; modal "Open in Verse Study" button; reader verse-number click popup

  ### Design decisions (locked)

  - **URL pattern:** `verse-study/index.html?ref=John+3:16` — same `?ref=` param convention as the Reader; version from `localStorage` or `&v=` override; fully shareable
  - **Layout:** Sticky verse header + sidebar section nav on desktop; top-of-page `<select>` dropdown on mobile (< 768px)
  - **Word study interaction:** Click any word token → expand inline panel below the token row showing Strong's number, Greek/Hebrew, morphology, gloss, occurrence count. Designed so the interlinear row (C2) slots in beneath each token later without restructuring the DOM.
  - **Context strip:** Previous and next verse shown dimmed above/below the focal verse; toggleable via a **Context** button in the header; state saved to `localStorage` key `bsw_dissect_ctx`
  - **Commentary:** One source shown at a time with a source selector dropdown (Matthew Henry first; Barnes, JFB, Clarke, Vincent added automatically as C1 data is built)
  - **Mobile section nav:** Top-of-page `<select>` dropdown; selecting a section smooth-scrolls to it
  - **Name:** "Verse Study" (user-facing label)
  - **Sections with no data yet:** Hidden entirely — they appear automatically as their data dependencies are built; no "coming soon" placeholders

  ### Entry points

  1. **Verse modal** — "Open in Verse Study" button at the bottom of the modal (alongside existing "Read in Reader")
  2. **Reader verse-number click** — clicking a verse-number superscript in the reader opens a small popup menu:
     - **Verse Study** — navigate to `verse-study/index.html?ref=...`
     - *(future: Bookmark — B6; Add to Memory — C4)*
  3. **Direct URL** — fully shareable; works as a search-engine landing page

  ### Data dependencies per section

  | Section | Data source | Status |
  |---------|-------------|--------|
  | Verse + context | `data/bible/` | Done |
  | Cross-references | `data/crossrefs/` | Done |
  | Parallel passages | `data/parallels/` | Done |
  | Matthew Henry commentary | `data/commentary/` | Done |
  | Word tokens (English) | String split, no data file | Done |
  | Strong's word study flyout | `data/strongs/` | Not built (B2) |
  | Interlinear row beneath tokens | `data/interlinear/` | Not built (C2) |
  | Additional commentary sources | `data/commentary/{source}/` | Not built (C1) |
  | Confessional citations section | `data/library/verse-index/` | Not built (D1) |
  | Church Fathers quotes | TBD | Not built (D3) |
  | Dictionary term hover | `data/dictionary/` | Not built (D4) |

---

## Phase B — Competitive Parity

- [x] **B1. Parallel translation reader** *(complete)* — "⇅ Compare" toggle in reader browse bar; splits text into 2 side-by-side panels each with its own version selector (A/B); primary selector calls `setVersion`, secondary stores to `bsw_compare`; lazy async fetch of secondary text; works with all 4 current versions (KJV, BSB, WEB, ASV); YLT/Darby/Geneva fetch scripts remain future work

- [x] **B2. Strong's concordance word study** *(complete)*
  - Click any word in a rendered verse → flyout shows:
    - Strong's number (e.g., G3056 / H1697)
    - Greek or Hebrew original term + transliteration
    - Brief lexical definition (root, gloss, semantic range)
    - Morphological parsing (for Greek: tense-voice-mood-person-number; for Hebrew: stem-conjugation)
    - Count of occurrences + link to concordance list
  - **Data sources (all public domain / open license):**
    - `openscriptures/strongs` — Strong's Hebrew + Greek dictionaries as JSON
    - `tahmmee/interlinear_bibledata` — OT + NT interlinear with Strong's numbers per word token
    - Dodson Greek Lexicon (CC0) for expanded Greek definitions
    - Brown-Driver-Briggs (BDB) Hebrew lexicon JSON for expanded Hebrew definitions
  - **Storage:** `data/strongs/greek.json` (~800 KB) + `data/strongs/hebrew.json` (~1.2 MB), fetched on demand and cached
  - **UI:** word-click handler wired into the verse renderer; flyout panel anchored to the clicked word
  - **Verse modal:** add "Word Study" as a fourth tab, showing word-by-word breakdown of the selected passage

- [x] **B3. Personal notes & verse highlights** *(complete)*
  - Click a verse number to toggle a yellow highlight (persists in localStorage)
  - Right-click / long-press a verse → open a small note editor textarea
  - Notes saved to `localStorage` key `bsw_notes` as `{ "John 3:16": { highlight: true, note: "…" } }`
  - `notes/index.html` — "My Notes" page listing all annotated verses with ref links back to Reader
  - Export option: copy all notes as plain text or JSON
  - Highlights visible in both the Reader and verse modal
  - Privacy-first: everything local, nothing leaves the browser
  - **VS1 integration:** Note and Highlight actions wired into the Reader verse-number popup menu (alongside "Verse Study")

- [x] **B4. PWA / offline mode** *(complete)*
  - Add `manifest.json` (name, icons, theme color, start URL, display: standalone)
  - Add a service worker (`sw.js`) with:
    - Cache-first strategy for `data/bible/**`, `data/crossrefs/**`, `data/commentary/**`, all CSS/JS
    - Network-first for HTML pages so updates are always received when online
    - Background pre-cache of all Bible JSON in 6-file chunks (150ms yield between chunks) triggered via postMessage after first load
  - `initPWA()` in `bible.js` injects `<link rel="manifest">` and `<meta name="theme-color">` dynamically — no per-page changes needed
  - SW auto-updates: new SW waits, then sends `SKIP_WAITING` to activate on next navigation
  - Total data: ~43MB (Bible text, crossrefs, commentary, interlinear, strongs) cached across 4 versions
  - Result: site works fully offline after first visit; no major free web tool offers this

- [x] **B5. Parallel Passage Reader** *(complete)*
  - Toggle in reader toolbar (next to version picker); state in `localStorage` key `bsw_parallels` (default: off)
  - Three parallel types with visual badges: ⇌ Parallel (blue) / ✓ Fulfilled in (green) / ⌖ Prophesied in (gold)
  - Stacked panels below each passage; first 3 verses visible, "Show N more" expander for remainder
  - Per-panel ▾/▸ collapse button; collapse state resets on chapter navigation
  - Lazy fetch — `loadParallels()` only fires when toggle is ON; zero fetches while feature is inactive
  - `bookCache` reuse — parallel book text is free if the user has already read it that session
  - Toggle-off removes all `.reader-parallel-section` elements from DOM (zero layout cost while inactive)
  - CSS in `reader.css`; data in `data/parallels/{bookId}.json`

- [x] **B6. Bookmarks** *(complete)*
  - One-click star/bookmark on any verse — no text entry required (distinct from B3 notes, which require writing)
  - Stored in `localStorage` key `bsw_bookmarks` as an array of ref strings (`["John 3:16", "Ps 23:1"]`)
  - `bookmarks/index.html` — list all bookmarked verses with jump links to Reader and Verse Study
  - Bookmarked verse numbers get a small ★ indicator in the Reader
  - Wired into the Reader verse-number popup menu (VS1) alongside Note, Highlight, Verse Study

- [x] **B7. Single-verse all-translations comparison** *(complete)*
  - Dedicated view showing one verse across all available versions stacked vertically
  - URL: `compare/index.html?ref=John+3:16` — shareable; works as a search-engine landing page
  - Accessible from: Reader verse-number popup, Verse Study page header, verse modal header
  - Distinct from B1 (B1 is side-by-side chapters; this is one verse × all versions)
  - Adjacent verse prev/next navigation (handles chapter boundaries)
  - Preferred version row highlighted with primary-color border
  - Add YLT, Darby, Geneva (from B1 fetch scripts) to make the comparison more compelling

---

## Phase C — Scholarly Depth

- [x] **C1. Additional public domain commentaries** *(complete)*
  - Currently only Matthew Henry's Concise Commentary is bundled
  - Add to the Commentary tab (selectable source dropdown):
    - **Barnes' Notes on the Bible** (Albert Barnes, 1832–1885) — OT + NT, verse-by-verse, public domain
    - **Jamieson-Fausset-Brown Commentary** (1871) — single-volume, scholarly, public domain
    - **Adam Clarke's Commentary** (1810–1826) — strong on original languages, public domain
    - **Vincent's Word Studies** (NT only, Marvin Vincent, 1886) — excellent Greek word-level commentary
  - Data source: SWORD Project public domain modules; same processing pipeline as Matthew Henry
  - Storage: `data/commentary/{source}/{bookId}.json` — same shape as existing commentary JSON

- [x] **C2. Interlinear reader — Greek NT + Hebrew OT** *(complete)*
  - A toggle in the Reader renders the original language beneath each English word:
    - Hebrew/Greek word (Unicode)
    - Transliteration (SBL-style)
    - Morphological parsing code (e.g., `V-AOR-ACT-IND-3S`, `N-NOM-MS`)
    - Strong's number (links to B2 word study)
  - Clicking any original-language word opens the Strong's flyout (B2)
  - **Data sources (all open license):**
    - Greek NT: `morphgnt/sblgnt` — SBLGNT with full morphological tagging, CC-BY 4.0
      (`data/interlinear/greek/{bookId}.json`)
    - Hebrew OT: `openscriptures/morphhb` — Westminster Leningrad Codex with tagging, CC-BY 4.0
      (`data/interlinear/hebrew/{bookId}.json`)
  - **Token JSON shape:**
    ```json
    { "eng": "In", "orig": "בְּרֵאשִׁ֖ית", "translit": "bə·rê·šîṯ",
      "strongs": "H7225", "parse": "N-FS", "lemma": "רֵאשִׁית" }
    ```

- [x] **C2a. RTL layout for Hebrew interlinear tokens** *(complete)*
  - Hebrew text in C2 is currently rendered left-to-right; Biblical Hebrew reads right-to-left and
    incorrect directionality makes the script visually wrong and harder to read
  - Determined: `dir="rtl"` placement, transliteration/morphology label alignment, Strong's LTR handling

- [x] **C3. Reading plans** *(complete)*
  - `plans/index.html` — browse and enroll in classic reading plans:
    - M'Cheyne's Calendar (OT + NT daily, 1 year) — public domain
    - Through the Bible in a Year (chronological) — public domain
    - New Testament in 90 Days
    - Psalms & Proverbs in a Month
    - Gospels in 30 Days
  - Plans stored as `data/plans/{id}.json` — arrays of daily reading lists
  - Enrollment + daily completion tracked in `localStorage` key `bsw_plans`
  - Home page widget: "Today's Reading" showing the day's passages for enrolled plans

- [x] **C3a. Reading plan progress tracking** *(complete)*
  - C3 tracks daily completion; added % complete and projected finish date per plan
  - Includes skip-day logic and catch-up mode

- [x] **C4. Scripture memory / flashcard tool** *(complete)*
  - `memorize/index.html` — browse verses in the memory list; enter flashcard mode
  - Flashcard modes: show reference → recall text; or show text → recall reference
  - Spaced repetition via simple interval scoring in `localStorage` key `bsw_memory`:
    `{ "John 3:16": { interval: 3, nextReview: "2026-06-01", score: 2 } }`
  - "Add to Memory" action available from: verse modal, Verse Study page, Reader verse-number popup menu

- [x] **C5. Nave's Topical Bible** *(complete)*
  - 20,000+ topic index (Orville Nave, 1896 — public domain)
  - `topical/index.html` — alphabetical browse + search across all topics
  - Data source: `openscriptures/nave` on GitHub
  - Storage: `data/topical/{topic-slug}.json` (topic heading + verse list)
  - **Verse modal integration:** new "Topics" tab listing all Nave's topics that cite the current verse

---

## Phase D — Content & Reference

- [x] **D1. Library section — complete the confessions data** *(complete)*

  ### Documents built
  - [x] Apostles' Creed
  - [x] Nicene Creed
  - [x] Athanasian Creed
  - [x] Heidelberg Catechism
  - [x] Westminster Confession of Faith
  - [x] Westminster Shorter Catechism
  - [x] Belgic Confession (1561)
  - [x] Canons of Dort (1618–1619)
  - [x] Westminster Larger Catechism
  - [x] London Baptist Confession (1689)
  - [x] Augsburg Confession (1530)
  - [x] 39 Articles of Religion

  ### Data structure (`data/library/`)
  ```
  data/library/{id}.json              — the document itself
  data/library/index.json             — metadata list (id, title, abbrev, year, type)
  data/library/verse-index/{bookId}.json  — reverse lookup: verse → confessional citations
  ```

- [x] **D2. New topic studies** *(complete)*
  - Priority additions built: Justification by Faith, The Holy Spirit, The Sermon on the Mount, Romans, The Psalms, The Covenants, Christology
  - Use `scripts/new-topic.sh` for scaffolding; follow `topics/_template/index.html`

- [x] **D3. Church Fathers library** *(complete)*
  - Per-Father pages (Ignatius, Justin Martyr, Irenaeus, Tertullian, Origen, Chrysostom, Augustine, etc.)
  - Key writings and quotes organized by theological topic
  - All Scripture refs linked via `.ref` system

- [x] **D4. Bible dictionary / glossary** *(complete)*
  - Theological term definitions (propitiation, sanctification, covenant, imputation, etc.)
  - Biblical character profiles; place name guide
  - Data source: ISBE (International Standard Bible Encyclopaedia, 1915) — public domain
  - Storage: `data/dictionary/{term-slug}.json`
  - Integration: hover over a `<span class="term">` → definition tooltip; standalone `dictionary/index.html`

- [x] **D5. Book introductions & outlines** *(complete)*
  - Per-book intro for all 66 books: author, date written, purpose, key themes, structural outline
  - Outline uses section-level labels with verse ranges, each section links directly to the Reader
  - **Historical timeline strip** — each book intro includes an estimated date range and a mini-timeline
  - Data: static JSON `data/books/introductions/{bookId}.json`; text sourced from ISBE (1915) + Easton's
  - Displayed in the Reader sidebar (collapsible) when viewing any chapter of that book

- [x] **D6. Spurgeon's Morning and Evening devotionals** *(complete)*
  - Public domain daily devotional (C.H. Spurgeon, 1865) — 365 morning + 365 evening entries
  - Data: `data/devotionals/spurgeon-morning.json` + `data/devotionals/spurgeon-evening.json` (keyed by `MM-DD`)
  - `devotionals/index.html` — browse today's entry or navigate by date

- [x] **D7. Verse of the Day** *(complete)*
  - Home page widget showing today's featured verse
  - Implementation: static `data/votd.json` — curated list of 365 verse refs; selected by `dayOfYear % 365`
  - No API dependency, no backend, no CORS — consistent with the static-first design

---

## Phase E — Visual & Historical Tools

- [x] **E1. Bible timeline** *(complete)*
  - Interactive horizontal-scroll SVG timeline at `timeline/index.html`
  - Era filter buttons, event search, clickable event cards linking to Reader
  - Implemented in `assets/js/timeline.js` + `assets/css/timeline.css`
  - Data: `data/timeline/events.json`

- [x] **E2. Biblical geography maps** *(complete)*
  - Five SVG maps at `maps/index.html`: Holy Land (NT), Paul's Journeys, Exodus Route,
    Divided Kingdom, Ancient Near East
  - Clickable city dots open detail panels with description + ref links
  - Implemented in `assets/js/maps.js` + `assets/css/maps.css`

---

## Phase F — Polish

- [x] **F0. Core accessibility audit** *(closed — not pursuing a formal audit)*
  - Decision: not doing a formal WCAG audit pass; known gaps handled individually (L1 for contrast, L4 for mobile font scaling)

- [x] **F1a. Keyboard-only navigation audit** *(closed — not pursuing)*
  - Decision: no structured keyboard audit planned; individual issues fixed as encountered

- [x] **F1. Dark mode toggle**
  - CSS custom properties are already structured for it (all colors via `--color-*` variables)
  - Toggle button in header, preference saved to `localStorage` key `bsw_theme`
  - `prefers-color-scheme` media query as the default, manual toggle overrides it

- [x] **F2. Copy / Share verse** *(complete)*
  - One-click copy button in the verse modal, Reader verse-number popup menu, and Verse Study page
  - Default format: `"For God so loved the world…" — John 3:16 (BSB)`
  - Optional formats selectable via a small dropdown: Plain text | Markdown blockquote | Academic citation
  - Implementation: `navigator.clipboard.writeText()`; `execCommand('copy')` fallback for older browsers

- [x] **F3. Text accessibility controls** *(complete)*
  - Font size control in Reader and Verse Study: Small / Medium / Large / XL
  - Preference saved to `localStorage` key `bsw_fontsize`; applied via CSS custom property `--reader-font-size`
  - Optional: serif / sans-serif toggle (Georgia default vs. system-ui)

- [x] **F4. Read history / recently viewed** *(complete)*
  - Last 10 passages viewed in the Reader saved to `localStorage` key `bsw_history`
  - Each entry: `{ ref: "John 3", version: "BSB", timestamp: … }`
  - Displayed in sidebar (collapsible "Recently viewed" group) or home page "Continue reading…" widget

- [x] **F5. Print-friendly chapter view** *(complete)*
  - "Print this chapter" button in Reader toolbar
  - Applies `@media print` styles: hide sidebar, nav, cross-ref panel; full-width verse text

- [x] **F6. Structured citation format** *(complete)*
  - "Cite" button in verse modal and Verse Study page
  - Copies the verse in selectable academic formats: Short | Long | MLA-style

- [x] **F7. Read history / "Continue Reading" home widget** *(complete)*
  - Record the last 20 passages viewed in the Reader to `localStorage` key `bsw_history`
  - Home page (`index.html`) gains a fourth `daily-card` section labelled "Continue Reading"
  - Widget hidden entirely if `bsw_history` is empty (first-visit)

- [x] **F8. Keyboard shortcuts help overlay** *(complete)*
  - Press `?` anywhere outside an input field → open a modal overlay listing all active shortcuts
    grouped by context (Global / Reader / Verse Study)
  - Dismiss with `Escape` or a close button

- [x] **F9. Service worker update toast** *(complete)*
  - Shows a non-blocking toast: "A new version is available — **Reload**" instead of silently activating
  - Clicking "Reload" sends `SKIP_WAITING` to `reg.waiting`, then calls `location.reload()`
  - Auto-dismiss after 30s

- [x] **F10. Open Graph / Twitter Card meta tags** *(complete)*
  - Added `_setOGMeta(title, description, url)` helper in `bible.js`
  - Reader: title `"John 3 — Bible Reader"`, description = first verse of displayed passage
  - Verse Study: title `"John 3:16 — Verse Study"`, description = focal verse text
  - Compare: title `"John 3:16 — All Translations"`

- [x] **F11. Reader opens to daily verse when no reference is given** *(complete)*
  - On load with no `?ref=` param, derives today's verse from VOTD data (D7)
  - Falls back to a hardcoded welcome verse (e.g., Psalm 119:105) as placeholder before D7 is built

- [x] **F12. End-of-book navigation: Chapter 0 introduction + in-reader book metadata button** *(complete)*

  ### Chapter 0 — Book Introduction as a navigable chapter
  - When on the last chapter of a book, pressing Next loads Chapter 0 of the next book
  - URL: `read/index.html?ref=Genesis.0` — Chapter 0 is a real addressable route
  - Full D5 content rendered in the main reading pane: title, author block, date/occasion, key themes, outline, timeline strip
  - A prominent "Begin Reading →" button at the bottom loads Chapter 1

  ### In-reader book metadata button
  - **"Book Info"** toggle button in the Reader browse bar
  - Expands a collapsible panel showing condensed D5 summary: author, date, ~2-sentence purpose, mini timeline
  - "Full Introduction →" link navigates to Chapter 0

- [x] **F13. Asset optimisation** *(stub — needs scoping before work begins)*
  - No image optimisation done; identified as gap; deferred pending scope

- [x] **F14. Data compression and lazy-loading strategy** *(complete)*
  - Commentary excluded from PRECACHE_BIBLE background download (~74 MB savings); now lazily
    cached on first access via DATA_CACHE_V cacheFirst strategy

- [x] **F15. Empty state UX** *(complete)*
  - Upgraded Notes, Bookmarks, and Memorize empty states to use reusable `.bsw-empty-state`
    component (glyph + title + description + CTA link); component defined in `bible-ui.css`

- [x] **F16. LocalStorage migration and data versioning** *(complete)*
  - Added `BSW_STORAGE_V` version constant and `_runStorageMigrations()` runner in `bible.js`
  - `init()` calls migrations on every page load; schema registry documents all localStorage keys
  - Migration v0→v1 calls existing `_migrateOldNotes()`; future versions extend the chain

- [x] **F17. Service worker cache invalidation strategy** *(complete)*
  - Rewrote `sw.js` with split cache strategy: `APP_CACHE_V` (HTML/CSS/JS) vs `DATA_CACHE_V` (JSON)
  - Either cache can be bumped independently; activate handler deletes all other caches on update
  - Full rollback procedure documented in header comment block

---

## Phase G — Search Quality

- [x] **G1. Relevance-ranked search results** *(complete)*
  - Added `score` field to each result: exact phrase match → 100; all words present → Jaccard similarity
  - Sort `allResults` by `score DESC`, canonical order as tiebreaker
  - "Sort: Relevance | Bible order" toggle saved to `localStorage` key `bsw_search_sort`

- [x] **G2. Search scope filters (Testament / Book)** *(complete)*
  - Collapsible "Filter ▾" row below search mode buttons
  - Controls: `All | Old Testament | New Testament` toggle buttons; a Book `<select>`
  - Filter state is session-only variables (not persisted to localStorage)

- [x] **G3. Search history (recent queries)** *(complete)*
  - Save last 10 distinct non-empty queries to `localStorage` key `bsw_search_history`
  - On focus of `#bsw-search-input` when empty, show dropdown of recent queries
  - Each history item is a clickable chip; "Clear history" link removes the key

- [x] **G4. Search results: book-grouped bubble/chip layout** *(complete)*
  - Replaced flat list with grouped-by-book layout: each book is a section heading + row of verse chips
  - Hovering a chip shows the standard verse tooltip; clicking opens the verse modal
  - Chip shape: `<span class="search-chip" data-ref="Romans 3:23">` with ref + preview spans

- [x] **G5. Strong's: English keyword → code lookup** *(complete)*
  - Implemented as the Word Studies section of the new Explore tab (`_exploreWords` in `bible.js`)
  - User types English word → live scan of `greek.json` + `hebrew.json`; returns up to 12 matching chips
  - Strong's codes typed directly (G3056, H1697) still auto-detect

- [x] **G6. Omni-search / Explore tab** *(complete — supersedes original G6 scope)*
  - `search/index.html` redesigned as two-tab layout: "Verse Search" and "Explore"
  - Explore tab runs 5 sub-searches concurrently: Verses, Word Studies, Topics, Dictionary, Library
  - Filter pills toggle section visibility without re-running search
  - URL params: `?q=` (verse), `?s=` (Strong's), `?e=` (explore) — all shareable

---

## Phase H — Notes & Highlights UX

- [x] **H1. Multi-color highlights** *(complete)*
  - Replace with `highlight: "yellow" | "green" | "blue" | "pink" | false`
  - Verse-number popup "Highlight" action becomes a 4-swatch color palette
  - CSS custom properties: `--highlight-yellow`, `--highlight-green`, `--highlight-blue`, `--highlight-pink`

- [x] **H2. Notes search and filter** *(complete)*
  - `notes/index.html`: search input filters rendered list in real-time
  - Filter chips: `All | Highlighted | Notes only`
  - Sort control: `Ref order | Most recent | Oldest`
  - Results count badge: "Showing 12 of 47 annotated verses"

- [x] **H3. Notes backup / restore (import JSON)** *(complete)*
  - "Import from backup" button; opens file picker; reads via `FileReader.readAsText()`
  - Validate shape, merge into `bsw_notes` without overwriting existing unless "Replace existing" checked
  - Summary toast after import: "Imported 34 notes, 12 highlights. 3 duplicates skipped."

- [x] **H4. Verse tagging for personal organisation** *(deferred — superseded by note export/import and Drive backup; tag filter is out of scope for now)*

---

## Phase I — Advanced Content

- [x] **I1. Catechism reading plans** *(complete)*
  - Added two new plan files:
    - `data/plans/heidelberg-weekly.json` — 52 entries, one per Lord's Day
    - `data/plans/wsc-quarterly.json` — 13 weeks × ~8 Q&As
  - Both registered in plan-selector dropdown and home page `#daily-plan-select`
  - Progress tracked in `bsw_plans` localStorage key — same key, same shape

- [x] **I2. Library cross-document search** *(complete)*
  - `scripts/build-library-index.py` emits `data/library/search-index.json`
  - Search input on `library/index.html`; filters client-side; renders results as `doc · section — heading` cards
  - Each result links to `library/{docSlug}/index.html#{section-anchor}`

- [x] **I3. Morphology parse code decoder** *(complete)*
  - `expandMorphCode(code)` in `bible.js` with inline look-up tables (~60 entries each for Greek and Hebrew)
  - Maps abbreviated segments to plain English: `"V-AAI-3S"` → `"Verb — Aorist Active Indicative — 3rd Person Singular"`
  - Wired into `_vsRenderWordPanel()` and `_riShowPopover()` in the interlinear grid popover

- [x] **I4. Verse sharing / image card generator** *(complete)*
  - "Share as image" action in verse modal and Verse Study page header
  - Canvas-based preview overlay: 1200×630 px, 2–3 design presets
  - "Download PNG" button via `canvas.toDataURL('image/png')`

- [x] **I5. Memory verse tags and Anki export** *(complete)*
  - Optional `tags: ["string"]` array added to each `bsw_memory` entry — backward compatible
  - Browse panel: tag filter chips + "+" button and inline text input to add tags
  - **Anki export:** `.txt` file in tab-separated format (`Front\tBack\n`)

---

## Phase J — Word Cloud

- [x] **J1. Most-common-words word cloud** *(complete)*
  - SVG spiral word cloud at `wordcloud/index.html`; linked from main nav
  - Pre-computed frequency data in `data/wordcloud/frequencies.json` (generated by `scripts/generate-wordcloud.py`); 250 meaningful lemmas, ~56 KB
  - Stop-list filters 40+ Greek/Hebrew function words
  - "Hide/Show names" toggle controls proper nouns
  - Scope filter buttons: Whole Bible / OT / NT / Law / History / Poetry / Prophecy / Gospels / Epistles / Revelation
  - Click any word → detail panel with lemma, Strong's ID, occurrence count, per-genre frequency bars
  - Pure-JS Archimedean spiral layout; canvas text measurement; log-scale font sizing
  - Implemented in `assets/js/wordcloud.js` + `assets/css/wordcloud.css`

---

## Phase K — Bible Version Expansion via API

- [x] **K1. Add public-domain versions from wldeh/bible-api** *(complete — fetch script written, versions.json updated; run `python3 scripts/fetch-versions.py` to download data)*

  **Versions committed locally (public domain):**
  | ID | Name | Year |
  |----|------|------|
  | YLT | Young's Literal Translation | 1898 |
  | DBY | Darby Translation | 1890 |
  | GNV | Geneva Bible | 1599 |
  | AKJV | American King James Version | ~2000 |
  | WEBBE | World English Bible British Edition | 2000 |

---

## Phase L — Accessibility & Internationalisation

- [x] **L1. High-contrast mode — WCAG AA contrast audit and CSS fixes** *(complete)*

  ### Pass 1 — `style.css` color variable audit
  - Wrote `scripts/check-contrast.py`: checks all 35 semantic color pairs in light + dark mode against WCAG AA thresholds
  - Found and fixed 6 variable-level failures:
    - `--color-accent` (#b8860b → #8c6a00): all `<a>` and `.ref` link text; 3.07:1 → 4.74:1
    - `--sb-muted` light (#9a8060 → #a08a68): sidebar secondary text; 4.18:1 → 4.69:1
    - `--sb-muted` dark (#7a6a55 → #9e8a6e): sidebar secondary text; 3.70:1 → 5.82:1
    - `.sb-sublabel` (#6a5540 → #9a7a50): sidebar section divider labels; 2.21:1 → 3.91:1

  ### Pass 2 — Dark mode button systemic fix
  - Root cause: `--color-primary` is golden yellow (`#e8c87a`) in dark mode — correct for text,
    but 53 button/badge rules across 14 CSS files used it as a button *background* with `color: #fff`,
    producing ~1.5:1 contrast
  - Added `--color-on-primary: #fff` (light) / `#1a1208` (dark) to `style.css`
  - Replaced all 53 `color: #fff` occurrences inside `background: var(--color-primary)` blocks

  ### Pass 3 — Full site survey
  - Audited every HTML `<style>` block and all remaining CSS; fixed plans, journal, notes, compare, offline pages
  - Re-run `python3 scripts/check-contrast.py` whenever colors in `style.css` change
  - For new buttons using `background: var(--color-primary)`, always pair with `color: var(--color-on-primary)`

- [x] **L2. Full keyboard navigation parity** *(closed — not pursuing)*
  - Decision: F0 was closed; no keyboard audit planned; fix individual issues as they are noticed

- [x] **L3. Internationalisation (i18n) framework** *(closed — out of scope)*
  - Decision: personal English-language study tool; i18n not warranted

- [x] **L4. Font size controls — mobile scaling bug** *(complete)*
  - `--reader-font-size` was not propagating to all elements on mobile
  - Fixed: audited which elements use `--reader-font-size` vs. hardcoded `rem` values on mobile;
    ensured CSS custom property is applied and no media query overrides with a fixed value

---

## Phase M — Infrastructure, DevOps & Performance

- [x] **M1. Data build and deployment pipeline documentation** *(complete)*
  - Created `scripts/README.md`: table of all scripts with purpose, output path, and run frequency
  - Includes a "Typical Initial Setup Order" section with the full command sequence

- [x] **M2. Upstream data source version pinning and re-sync strategy** *(complete)*
  - Created `data/SOURCES.md`: every external source listed with URL, license, data path, and commit/version field
  - Update SOURCES.md whenever a source is added, changed, or removed

- [x] **M3. Data file completeness validation** *(closed — not needed)*
  - Decision: data gaps surface naturally during use; a formal validation script is more
    maintenance than it's worth for a single-author personal site

- [x] **M4. Search performance profiling** *(closed — not needed)*
  - Decision: search is perceptibly fast in practice; profiling overhead not warranted unless
    a user reports slowness on a specific device or query

- [x] **M5. `bible.js` modularisation** *(complete)*
  - `bible.js` split into 16 ES modules: `core.js`, `storage.js`, `tooltip.js`, `modal.js`,
    `wire.js`, `pwa.js`, `search.js`, `reader.js`, `parallels.js`, `interlinear.js`,
    `verse-study.js`, `word.js`, `daily.js`, `library.js`, `terms.js`, `maps.js`,
    `timeline.js`, `wordcloud.js`, loaded via `<script type="module" src="app.js">`
  - All 47 HTML pages updated; `sw.js` SHELL_URLS updated with all module paths
  - No build step required — native ES modules served directly by the static file server

- [x] **M6. `data/references/` directory clarification** *(closed — false alarm)*
  - Directory does not exist; the stub was written against a stale gap analysis

---

## Phase N — Engagement & Content Depth

- [x] **N1. Reading streaks and engagement tracking** *(complete)*
  - Daily reading streak counter with visible counter and "don't break the chain" nudge
  - Counts any Reader visit; displays on home page widget

- [x] **N2. Prayer journal** *(complete)*
  - Day-keyed journal at `journal/index.html` where each entry can link to one or more Bible references
  - Stored separately from `bsw_notes`; entries use `.ref` pattern for verse linking

- [x] **N3. Study Guides** *(complete)*

  Study guides are structured multi-session resources with a defined session structure and discussion questions per session.

  ### Location and navigation
  - `study-guides/index.html` — browse all guides (grid of cards)
  - `study-guides/{slug}/index.html` — individual guide
  - Sidebar: "Study Guides" group in the nav (below "Topics")
  - Card format: title, subtitle, session count, estimated duration

  ### Template and authoring
  - Copy `study-guides/_template/index.html`
  - No JSON data files — entirely static HTML following the no-build-step principle
  - `bash scripts/new-study-guide.sh <slug> "Title"` scaffolds the page

  ### Priority guides authored
  - Ephesians (6 sessions)
  - Romans 1–8 (8 sessions)
  - The Sermon on the Mount — Matthew 5–7 (5 sessions)
  - The Psalms — a 4-week devotional structure (4 sessions)

- [x] **N4. First-visit onboarding experience** *(complete)*
  - Welcome flow for new visitors explaining the site's tools and where to start

- [x] **N5. Commentary citation and passage export** *(closed — not implementing)*
  - Decision: F2 (copy verse) covers the primary need; the additional commentary export path
    adds complexity for minimal gain on a personal study tool

---

## Library Expansion — Completed Items

### Phase 1 — Series/Volume grouping
- [x] Add `series`, `series_title`, `volume`, `volume_label` fields to all multi-volume entries in `data/library/index.json` (49 entries patched across 15 series)
- [x] Add volume selector UI (chip tabs) to `lib-browser.js` reader header when a doc belongs to a series
- [x] Add `lb-item-vol-badge` to list items showing volume label

### Phase 2 — Paginated chapter view (both readers)
- [x] Upgrade `lib-browser.js` `_renderReader`: one section at a time when `sections.length > 10`
- [x] Upgrade `lib-reader.js` `_render`: same paginated mode
- [x] Persist section progress per docId in `localStorage` (`bsw_lbpos_{docId}`)
- [x] Compact chapter dropdown nav + Prev/Next buttons in paginated mode

### Phase 3 — Fill missing works in `fetch-library-docs.py` (completed items)
- [x] John of Damascus — *An Exact Exposition of the Orthodox Faith* (Wikisource NPNF II/9, grouped_pages)
- [x] Teresa of Ávila — *Interior Castle* (Gutenberg #243, 7 sections)
- [x] John of the Cross — *Dark Night of the Soul* (Gutenberg #700, 2 sections)
- [x] Abraham Kuyper — *Lectures on Calvinism* (Gutenberg #58670)
- [x] Thomas Watson — *A Body of Divinity Vol. I* (Gutenberg #26691, 12 sections)
- [x] John Owen — *Of the Mortification of Sin* (Gutenberg #36809, 4 sections)
- [x] Ignatius — Ephesians, Magnesians, Trallians (ANCL Wikisource)
- [x] Run `fetch-library-docs.py` for all new entries
- [x] Update `data/library/index.json` with html_url entries for new works (121 total entries)

### Phase 4 — Full text expansion (completed items)
- [x] Aquinas Summa — all 4 parts (Gutenberg, h5 split): Part I 132 secs, I-II 122, II-II 198, III 98
- [x] Chesterton Everlasting Man (Gutenberg #65688, 8 sections)
- [x] Roman Catechism (Wikisource, 4 grouped parts, 42 pages)
- [x] Baltimore Catechism No. 3 (Gutenberg #14553, 51 sections)
- [x] Origen De Principiis (Wikisource ANF IV, 4 books, 34 pages)
- [x] Chrysostom Homilies on Acts (Wikisource NPNF I/XI, 5 groups, 55 homilies)
- [x] Series fields wired: Aquinas (5 entries), Origen (2 entries), Chrysostom (3 entries)

### Maps Phase 1 — HTML structure
- [x] HTML: overview panel, map-wrapper overlay div, significance slot, reset-view button

### Library Expansion — Phase 5 (CCEL batch)
- [x] Bernard of Clairvaux — *On Loving God* (CCEL, 18 chapters)
- [x] Francis de Sales — *Introduction to the Devout Life* (CCEL, 4 groups, 127 pages)
- [x] Jonathan Edwards — *Religious Affections* (CCEL, 3 parts, 32 pages)
- [x] Jonathan Edwards — *Freedom of the Will* (CCEL, 4 parts, 40 pages)
- [x] `ccel_grouped` fetch mode added to `fetch-library-docs.py`; reusable for any future CCEL text

---

## Library Reader Improvements

### HIGH — Breaks expected behaviour
- [x] **URL doesn't update on section/chapter navigation in paginated mode** — `goTo()` calls `_pushUrlState()` in `lib-browser.js`; `history.replaceState()` with `?doc=X&section=N` in `lib-reader.js`; `_initFromUrl()` restores section on load
- [x] **Mobile layout: 4-column stack is unusable** — tab bar added at ≤600px (`lb-tab-bar`); 4 tabs (Filter / Authors / List / Read); auto-switches to Read tab when a doc opens; implemented in `_initMobileTabs()` in `lib-browser.js`

### MEDIUM — Noticeable UX gaps
- [x] **Filter state not persisted across sessions** — `_saveFilters()` writes to `localStorage` key `bsw_lib_filters` on every filter change; `_initFromUrl()` falls back to localStorage when URL has no filter params
- [x] **No search within the Authors panel** — search input at top of Authors column (`#lb-authors-search`); debounced 150ms; filters visible author rows using module-level `_authorsQ`; refocuses after re-render
- [x] **Keyboard navigation in paginated mode** — `ArrowLeft`/`ArrowRight` call `goTo()` in both readers; listener stored in `_keyListener` and cleaned up on mode/doc change
- [x] **Series/volume switcher missing from standalone reader** — `_volHtml()` ported to `lib-reader.js`; renders `<a>` chip links in the doc header for all sibling volumes; active chip non-clickable
- [x] **"Clear all filters" shortcut missing** — `✕ Clear` button in filter panel (`lb-filter-clear`); only visible when any of tradition/era/type/author is non-default; `_clearAllFilters()` resets all four
- [x] **Paginated mode: large section dropdowns are unwieldy** — `<select>` replaced with `<input type="number">` + "of N" label in both readers; navigates on `change` or Enter key

### LOW — Polish
- [x] **Dark mode** — added rules for `.lb-pager-num`, `.lb-vol-chip`, `lr-pager-num`, `lr-vol-chip`
- [x] **Loading skeleton** — pulsing gray bars replace "Loading…" text in inline reader (`lb-reader-skeleton`, `@keyframes lb-pulse`)
- [x] **Empty filter state messaging** — suggests which filter to remove; shows "Reset filters" button wired to `_clearAllFilters()`
- [x] **`aria-current` on active TOC links** — set alongside `.lb-toc-active` in `_wireScrollSpy()`
- [x] **Pagination `<nav>` landmark** — both `_renderPaginatedView()` and `_renderPaged()` wrap pager in `<nav aria-label="Chapter navigation">`
- [x] **localStorage position cleanup** — `bsw_lbpos_<docId>` now stores `{idx, ts}`; entries older than 90 days evicted via `_evictStalePositions()` on init; legacy bare-int format read safely

---

## Library Content Cleanup *(2026-06-03)*

Full audit of all HTML and JSON library files.

### CRITICAL — Wrong book files
- [x] **`john-of-cross-dark-night.html`** — correct content in place.
- [x] **`teresa-interior-castle.html`** — correct content in place.
- [x] **`owen-mortification.html`** — correct content in place.
- [x] **`kuyper-calvinism.html`** — correct content in place.

### HIGH — Gutenberg boilerplate / missing chapters / editorial notes
- [x] **`newman-apologia.html`** — no Gutenberg boilerplate; clean.
- [x] **`calvin-institutes-vol1.html`** — no Gutenberg boilerplate; clean.
- [x] **`bunyan-grace-abounding.html`** — no transcription credit; clean.
- [x] **`murray-humility.html`** — all 12 chapters present.
- [x] **`smalcald-articles.json`** — Part III has all 15 articles.
- [x] **`wesley-sermons.html`** — no ambox block; clean.

### MEDIUM — book_navbar artifacts stripped
- [x] **`bernard-on-loving-god.html`** — already clean.
- [x] **`edwards-religious-affections.html`** — already clean.
- [x] **`edwards-freedom-of-will.html`** — already clean.
- [x] **`aquinas-summa-part-i-ii.html`** — already clean.
- [x] **`aquinas-summa-part-ii-ii.html`** — already clean.
- [x] **`aquinas-summa-part-iii.html`** — already clean.
- [x] **`francis-de-sales-devout-life.html`** — already clean.
- [x] **`fox-book-of-martyrs.html`** — already clean.
- [x] **`tertullian-prescription.html`** — already clean.
- [x] **`murray-ministry-of-intercession.html`** — already clean.
- [x] **`baxter-reformed-pastor.html`** — stripped 19 book_navbar instances + unwrapped book-content divs.
- [x] **`benedict-rule.html`** — stripped 73 instances.
- [x] **`catherine-dialogue.html`** — stripped 32 instances.
- [x] **`ignatius-spiritual-exercises.html`** — stripped 11 instances.
- [x] **`julian-revelations.html`** — stripped 19 instances.
- [x] **`luther-bondage-of-will.html`** — stripped 40 instances.
- [x] **`meister-eckhart-sermons.html`** — stripped 6 instances.
- [x] **`pseudo-dionysius-works.html`** — stripped 19 instances.
- [x] **`taylor-holy-living.html`** — stripped 17 instances.
- [x] **`whitefield-sermons.html`** — stripped 10 instances.
- [x] **`william-law-serious-call.html`** — stripped 24 instances.

### MEDIUM — Transcriber notes removed
- [x] **`calvin-institutes-vol1.html`** — already clean.
- [x] **`calvin-institutes-vol2.html`** — Transcriber's Notes block + Gutenberg END marker removed.
- [x] **`fox-book-of-martyrs.html`** — `<div class="tnote">` removed.
- [x] **`murray-lord-teach-us-to-pray.html`** — already clean.
- [x] **`murray-ministry-of-intercession.html`** — already clean.
- [x] **`watson-body-of-divinity-vol1.html`** — already clean.
- [x] **`baltimore-catechism.html`** — already clean.

---

## Library Type System *(2026-06-03)*

7 new types added to `_TYPES`/`_TYPE_LABELS` in `lib-browser.js` and `_TYPE_BADGE`/`_TYPE_LABEL` in `lib-reader.js`. 42 entries reclassified in `data/library/index.json`.

- [x] **`devotional`** — 17 entries (Cassian Conferences, Cloud of Unknowing, Julian Revelations, Imitation of Christ, Ignatius Exercises, Dark Night, Interior Castle, Devout Life, Holy Living, Brother Lawrence, Serious Call, Ryle Holiness, Spurgeon All of Grace, Murray Humility / Deeper Christian Life / Lord Teach Us to Pray / Ministry of Intercession)
- [x] **`liturgy`** — 2 entries (Didache, Rule of St. Benedict)
- [x] **`encyclical`** — 1 entry (Tome of Leo, moved from `council`)
- [x] **`sermon`** — 6 entries (Chrysostom Homilies Acts, Leo Sermons, Eckhart Sermons, Wesley Sermons, Edwards Sinners in the Hands, Whitefield Sermons)
- [x] **`commentary`** — type added to filter UI; no existing entries reclassified (new additions will use this type)
- [x] **`history`** — 2 entries (Eusebius Ecclesiastical History, Fox's Book of Martyrs)
- [x] **`apologetics`** — 14 entries (Justin First/Second Apology/Dialogue with Trypho, Athenagoras Writings, Tertullian Apology/Prescription, Origen Against Celsus, Anselm Proslogion/Cur Deus Homo, Chesterton Orthodoxy/Everlasting Man, Machen Christianity and Liberalism, Lewis Apologetics, Epistle to Diognetus)

---

## Library Reader Improvements *(2026-06-03)*

### MEDIUM — UX gaps
- [x] **In-reader text search (find-in-document)** — `#lb-find-btn` opens a find bar; searches section HTML in paginated mode, highlights with `<mark>` in scroll mode; persists across paginated re-renders via `_findTerm`/`_findMatchSecs` module state.
- [x] **Section progress indicator in scroll mode** — `#lb-section-counter` / `#lr-section-counter` in sticky reader header; updated by scroll-spy listener; format `§ N of M`.

---

## Library Reading Progress & Completion *(2026-06-03)*

### LR-A · Mark Document as Complete
- [x] `lib-reader.js`: `_buildMarkRow`, `_wireMarkBtn`, `_markDocComplete`, `_isDocComplete`, `_traditionNote` added
- [x] Scroll mode: mark button always rendered at bottom; paginated mode: rendered only on last section
- [x] Writes to `bsw_lib_complete` localStorage (permanent log, no cap); entry shape: `{ title, author, tradition, type, completedDate }`
- [x] Button toggles to `✓ Completed [date]` (disabled, muted) when already marked
- [x] `assets/css/lib-reader.css`: `.lib-mark-row`, `.lib-mark-btn`, `.lib-mark-btn--done`, `.lib-mark-note`
- [x] `_saveLibProgress` updated to include `tradition` field in `bsw_lib_progress` entries

### LR-B · Tradition-Encouragement Logic
- [x] `_traditionNote(tradition, log)` — 4-tier: first work ever / first of this tradition / growing / strong + gap suggestion
- [x] Gap tradition ordered: orthodox → patristic → reformed → lutheran → roman-catholic → anglican → baptist
- [x] Shown beneath mark button; re-evaluated after clicking

### LR-C · Library Reading Progress View
- [x] `library/progress/index.html` — standalone page; linked from library browser header and sidebar nav
- [x] `assets/js/lib-progress.js` — reads `bsw_lib_complete` + `data/library/index.json`; renders stats row (completed count, traditions touched), per-tradition coverage bars (done/total), encouragement line, completion log (newest-first with tradition chip + date)
- [x] `assets/css/lib-progress.css` — full styling
- [x] `assets/js/main.js`: `📚 Reading History` link added to Library nav group
- [x] `library/index.html`: `📚 Reading History` link added to browser header

---

## Bible Reader Improvements — RD-A, C, E, F, H, J, K (2026-06-03)

### RD-A · Chapter Navigation — Eliminate Full Page Reloads
- [x] `reader.js` (`_navigateChapter`): All three branches (next chapter, prev chapter crossing book boundary, next chapter crossing book boundary) now use the in-page pattern: set `reader-lookup-input` value + call `window._readerLookupFn()`. No more `window.location.href` full reloads — scroll position, panel state, and toggles are preserved across chapter flips.
- [x] Verified ch=0 (intro page) branch was already correct and left unchanged.

### RD-C · Restore Last Position on Blank Load
- [x] `reader.js` (`initReaderLookup`): When `refStr` is empty, reads `_historyGet()[0]`; if present and not dismissed this session, injects a dismissable `.reader-resume-banner` with a link to the last reference. Dismissal stored in `sessionStorage('bsw_reader_resume_dismissed')`. Does not auto-navigate.
- [x] `reader.css`: `.reader-resume-banner` (left border, flex row), `.reader-resume-link`, `.reader-resume-dismiss`

### RD-E · Verse Hover — Highlight Active Verse
- [x] `reader.js` (`wireVerseNumberPopup`): Added module-level `_activeVerseEl`. On verse-number click: clears previous `.reader-verse--active`, adds it to the clicked `.reader-verse`. A `MutationObserver` on the modal backdrop removes the class when `bsw-modal-backdrop--hidden` is added (i.e. on modal close). Observer is set up once per backdrop element.
- [x] `reader.css`: `.reader-verse--active { background: rgba(92,61,30,.07); border-radius:3px; outline:1px solid rgba(92,61,30,.07); }`

### RD-F · Right Panel — Notes Compose Scope
- [x] `reader.js` (`_loadReaderNotes`): Textarea placeholder changed from `"Add a note for {display}…"` to `"Add a chapter note for {chLabel} (click a verse number to note a specific verse)…"`. Added `.reader-hint` line beneath textarea: "Verse-specific notes: click the verse number ↑".

### RD-H · Empty-State Guidance for Blank Load
- [x] `reader.js` (`initReaderLookup`): When `refStr` is empty AND history is empty (first-time visitor), renders a centered `.reader-empty-state` with hint text and five `.reader-qs-chip` quick-start links (John 1, Psalm 23, Romans 8, Genesis 1, Isaiah 53).
- [x] `reader.css`: `.reader-empty-state`, `.reader-quick-starts`, `.reader-qs-chip` (outlined pill links with hover fill)

### RD-J · Attribution Line — Suppress for Single-Verse Results
- [x] `reader.js` (`doLookup`): `attrEl.hidden = !!(g.ref.v && !g.ref.endV)` — attribution hidden for single-verse lookups (`John 3:16`), visible for chapter views and ranges.

### RD-K · Mobile Browse Bar — Hide Keyboard Hint
- [x] `reader.css`: `.reader-browse-hint { display: none; }` added to the existing `@media (max-width: 699px)` block. (Rule already existed in the 640px block; this extends coverage to 641–699px.)

## Archived 2026-06-03 -- Library Search Index, Library Format, Omni-Search, Timelapse Phase 1 & 2, Timeline UX, Library Cleanup (partial), RD-D, REF-A, Maps System MAP-A through MAP-I

## Archived 2026-06-03 -- Library Search Index, Library Format Standardisation, Omni-Search, Timelapse Phase 1 and 2, Timeline Pages UX, Library Cleanup (partial), RD-D, REF-A, Maps System (MAP-A through MAP-I)


## Library Search Index — Rebuild Required

The library search index (`data/library/search-index.json`) covers only **19 of 141 documents
(13%)**. The remaining 122 docs — including Augustine's Confessions, Calvin's Institutes,
Luther's Bondage of the Will, Bunyan's Pilgrim's Progress, Chrysostom's Homilies, and every
other full-length theological work — return no search results in the Explore tab's Library
section. Only the structured confessions/catechisms and 8 brief Church Fathers overviews are
indexed.

**Root cause:** `build-library-json.py` processes only 20 hardcoded docs. No script exists to
index the 103 HTML-path documents that make up the bulk of the library. The HTML docs use
`<section data-heading="...">` elements (already what the lib-reader uses to split sections)
that can be parsed programmatically — the data is there, the indexing just hasn't been done.

**Current index:** 163 entries, 75KB, 19 docs
**After rebuild (estimated):** ~1,500 entries, ~1–1.5MB, 141 docs

---

### LX-A · Write `scripts/build-library-search-index.py` *(CRITICAL)*

A standalone script to regenerate `data/library/search-index.json` from scratch. Should be
re-run whenever library docs are added or updated.

**Two source formats to handle:**

**Format A — JSON docs** (`data/library/docs/*.json`):
- 38 docs, 421 total sections
- Each section has `ref`, `heading`, and `html` (HTML string)
- Strip HTML tags from `html` to get plain text; take first ~350 chars as `text` field

**Format B — HTML docs** (`data/library/html/*.html`):
- 103 docs, ~1,100 sections
- Parse `<section data-heading="...">` elements; `data-heading` is the heading
- For section body text: find first `<p>` tag inside the section; strip tags; first ~350 chars
- **Exception — TEI-format docs** (both `calvin-institutes-vol*.html`):
  Calvin's Institutes use `class="tei tei-div"` + `class="tei tei-head"` for chapter structure
  with a single wrapping `<section data-heading="">`. These need the `tei-head` elements as
  section boundaries and the following `tei-p` elements as body text.

**Output format** (one entry per section, append to array):
```json
{
  "docId": "augustine-confessions",
  "ref": "8",
  "heading": "Book VIII — The Conversion in the Garden",
  "text": "In a profound crisis of will, Augustine hears the child's voice 'Take up and read'..."
}
```
Note: drop the `"doc"` abbrev field (currently present but unused in search logic) to keep
file size down.

**Implementation notes:**
- Use `from bs4 import BeautifulSoup` (already a dependency of the other build scripts)
- For HTML parsing, load via `BeautifulSoup(html, 'html.parser')`
- For text extraction: `section.get_text(separator=' ', strip=True)[:350]`
- Write to `data/library/search-index.json` sorted by docId then ref for deterministic diffs
- Respect the `html_url` field in `data/library/index.json` to map docId → HTML filename

```python
# Pseudocode outline:
entries = []

# Format A: JSON docs
for doc_json in Path('data/library/docs').glob('*.json'):
    doc = json.load(open(doc_json))
    for s in doc['sections']:
        text = BeautifulSoup(s['html'], 'html.parser').get_text(' ', True)[:350]
        entries.append({'docId': doc['id'], 'ref': s['ref'],
                        'heading': s['heading'], 'text': text})

# Format B: HTML docs
index = json.load(open('data/library/index.json'))
for entry in index:
    if not entry.get('html_url'): continue
    html = open(f'data/library/html/{entry["html_url"]}').read()
    soup = BeautifulSoup(html, 'html.parser')
    # TEI-format special case
    if 'tei tei-div' in html:
        for i, head in enumerate(soup.select('.tei-head')):
            heading = head.get_text(' ', True)
            body_el = head.find_next_sibling()
            text = body_el.get_text(' ', True)[:350] if body_el else ''
            entries.append({'docId': entry['id'], 'ref': str(i+1),
                            'heading': heading, 'text': text})
    else:
        for sec in soup.select('section[data-heading]'):
            heading = sec.get('data-heading', '')
            first_p = sec.find('p')
            text = first_p.get_text(' ', True)[:350] if first_p else ''
            entries.append({'docId': entry['id'], 'ref': ...,
                            'heading': heading, 'text': text})

json.dump(sorted(entries, key=lambda e: (e['docId'], e['ref'])),
          open('data/library/search-index.json', 'w'), ensure_ascii=False)
```

- [x] Write and run `scripts/build-library-search-index.py` per the design above
- [x] Verify output: `python3 -c "import json; d=json.load(open('data/library/search-index.json')); print(len(d), 'entries,', len(set(e['docId'] for e in d)), 'docs')"` — 1595 entries, 142 docs, 477KB
- [x] Commit the rebuilt `data/library/search-index.json`

---

### LX-B · Verify Existing Partial Index Entries Are Correct *(MEDIUM)*

The 163 entries currently in the index have inconsistent granularity:
- WSC: 56 entries (correct — one per Q&A)
- WCF: 33 entries (correct — one per chapter)
- WLC: only 2 entries (should have 107 — one per Q&A, same as WSC)
- HC: only 2 entries (should have 52 — one per Lord's Day)
- 8 Church Fathers "overview" docs: 4–5 entries each (these are the brief curated-quote
  compilations in `data/library/docs/`, not the full-length HTML works — correct as-is)

The rebuild script in LX-A will regenerate all entries from source, correcting WLC and HC
automatically. No manual action needed if LX-A runs completely.

---

### LX-C · Loading Performance — Index File Size *(MEDIUM)*

`_loadLibSearch()` in `core.js` fetches the entire index as a single JSON file. Currently 75KB
(fast). After the rebuild the file will be ~1–1.5MB (first load ~300–800ms on a slow
connection). The function already caches in `_libSearchCache` so repeated searches within a
session are free.

No architecture change is needed at this scale — 1.5MB is acceptable for a search index and
only loads on first explore search. But two improvements are worth making:

- [x] `search.js` (`_exploreLibrary`): The section body already shows `<p class="omni-loading">
  Loading…</p>` while the index fetches — verified: loading state is set before Promise.all, cleared only when results render
- [x] `scripts/build-library-search-index.py`: Keep `text` field to ≤350 chars per entry — implemented (MAX_CHARS=350, actual max=350)

---

### LX-D · `_exploreLibrary` Snippet Highlight *(LOW)*

Currently the Library section in Explore shows a raw text snippet but does not highlight the
matched query term in it. The verse section highlights with `<mark>`. The library snippet should
do the same.

- [x] `search.js` (`_exploreLibrary`): When building the `<span class="omni-lib-card__snippet">`,
  wrap the query match in `<mark>` using the same `highlightMatch(snippet, q)` helper already
  exported from `search.js`

---

## Library Document Format Standardisation

**The problem.** The 141 library documents were collected from four different sources
(MediaWiki exports, CCEL reader pages, TEI/XML conversions, Project Gutenberg) and none were
normalised to a single internal format. As a result:

- 82 of 103 HTML-path docs have structural or markup issues
- 44 docs are severely under-sectioned (90 total sections where there should be ~1,033)
- 45 docs carry MediaWiki wrapper divs the reader doesn't need
- 15 docs carry CCEL reader chrome (navigation anchors, UI wrappers)
- 47 docs use `<i>` instead of `<em>`, 12 use `<b>` instead of `<strong>`
- 32 docs have inline `style=""` attributes that fight the site CSS
- 16 docs have visible page-number markers
- 4 docs serve entirely wrong content (see Library Content Cleanup section)

Every one of these issues directly degrades: (a) the reader display, (b) the search index
snippets, and (c) the ability to write consistent code against a known structure.

---

### The Target Format: BSW Library HTML v1

All HTML-path docs (`data/library/html/*.html`) must conform to this structure. This is
also the standard for the `.html` fields inside JSON-path docs (`data/library/docs/*.json`).

**File root — bare sections, no outer wrapper:**
```html
<section data-heading="Chapter I — Title of Chapter">
  <h2 class="lib-section__title">Chapter I — Title of Chapter</h2>
  <p>Body text with <em>emphasis</em> and <strong>strong</strong>.</p>
  <p>Second paragraph with a <a class="ref" data-ref="John 3:16">John 3:16</a> link.</p>
  <blockquote class="lib-quote">An extended quotation from the text.</blockquote>
</section>

<section data-heading="Chapter II — Next Chapter">
  <h2 class="lib-section__title">Chapter II — Next Chapter</h2>
  ...
</section>
```

**Rules (every rule is checkable by script):**

1. **File root** — one or more `<section data-heading="...">` elements; no `<html>`, `<body>`,
   `<head>`, or any wrapping `<div>` outside sections
2. **`data-heading`** — plain text; no HTML tags; only `&amp;`, `&lt;`, `&gt;` entities allowed;
   must match the text of the first `<h2>` inside the section
3. **First child of every section** — `<h2 class="lib-section__title">` matching `data-heading`
4. **Allowed content elements** — `<p>`, `<em>`, `<strong>`, `<blockquote class="lib-quote">`,
   `<ul>`, `<ol>`, `<li>`, `<h3>`, `<sup>`, `<a class="ref" data-ref="...">`,
   `<aside class="lib-fn">` (scholarly footnotes only), `<table class="lib-table">` (catechism
   Q&A tables only, rare)
5. **No inline styles** — no `style=""` attribute anywhere
6. **No deprecated tags** — `<i>` → `<em>`, `<b>` → `<strong>`, no `<center>`, `<font>`,
   `<big>`, `<small>`, `<strike>`, `<u>` (convert or strip)
7. **No external chrome** — no MediaWiki divs, no CCEL reader wrappers, no Gutenberg
   boilerplate, no Wikisource maintenance boxes, no transcriber notes, no CCEL navigation
   anchor links
8. **No page number markers** — no `class="pagenum"`, `class="tei tei-pb"`, `class="page"`,
   no `[page N]` text
9. **No empty `<a>` anchors** — strip `<a id="..."></a>` anchor targets with no `href`
10. **Section granularity** — each section = one navigable unit: chapter, homily, oration,
    sermon, Q&A group, or conference; typically 500–4000 words per section; multi-MB docs
    must be split; no section should exceed ~50KB of HTML

**JSON-path docs** (`data/library/docs/*.json`): structure unchanged; apply rules 5–9 to
the `.html` field of each section.

---

### LF-0 · Write Format Validation Script *(First — gates all subsequent work)*

Write `scripts/validate-library-format.py` — run it against any doc and get a pass/fail
report. All LF-A through LF-H work is "done" only when this script passes.

- [x] `scripts/validate-library-format.py`: Written — checks R1/R3/R5/R6/R7/R8/R9/R10; supports `--all`. Baseline was 103/103 FAIL; after all LF work: **100/103 PASS**.
- [x] Also validates JSON docs
- [x] Exit code 0 = all pass; non-zero = failures

---

### LF-A · Strip External Chrome — Scriptable Batch (Groups 2, 3, 4) *(HIGH)*

Write and run three targeted strippers. Each is a one-time transform; the output replaces
the source file.

#### LF-A1 · MediaWiki wrapper strip *(45 docs)*

Every MediaWiki-sourced doc wraps its content in:
```html
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en">...</div>
```
and uses `<div class="mw-heading mw-headingN"><hN ...>text</hN></div>` for headings.

- [x] `scripts/clean-library-html.py --mode mediawiki`: for each of the 45 MediaWiki docs:
  - Unwrap `mw-content-ltr mw-parser-output` div (keep children)
  - Replace `<div class="mw-heading mw-headingN">` wrappers with bare `<hN>` tags
  - Remove `<div class="mw-heading ...">` tags that are empty after heading extraction
  - Remove `edit section` links (`<span class="mw-editsection">...`)
  - Remove `id="..."` on heading tags (not needed)
  - Run rules 5–8 cleanup (inline styles, deprecated tags, page numbers) on same pass
  - Output: still uses current `<section data-heading="...">` boundaries (re-sectioning
    handled separately in LF-C); this pass only removes the wrapper chrome

  **45 docs:** ambrose-on-duties, anselm-cur-deus-homo, athanasius-life-of-antony,
  athanasius-on-incarnation, athenagoras-writings, augustine-city-of-god,
  augustine-confessions, augustine-on-christian-doctrine, augustine-on-trinity,
  basil-on-holy-spirit, brother-lawrence-practice, calvin-institutes-book1,
  cassian-conferences, chesterton-orthodoxy, chrysostom-homilies-acts,
  chrysostom-on-priesthood, cloud-of-unknowing, cyril-catechetical-lectures,
  eusebius-church-history, francis-of-assisi-writings, gregory-great-pastoral-rule,
  gregory-nazianzus-orations, gregory-nyssa-great-catechism, gregory-palamas,
  imitation-of-christ, irenaeus-against-heresies, john-of-damascus-exposition,
  leo-sermons, machen-christianity-liberalism, maximus-confessor, origen-against-celsus,
  origen-de-principiis, owen-mortification, pilgrims-progress, roman-catechism,
  ryle-holiness, shepherd-of-hermas, spurgeon-all-of-grace, symeon-new-theologian,
  teresa-interior-castle, tertullian-apology, tertullian-prescription, wesley-sermons
  *(plus john-of-cross-dark-night, kuyper-calvinism — strip chrome, then replace content per
  Library Content Cleanup section)*

#### LF-A2 · CCEL reader chrome strip *(15 docs)*

CCEL reader pages wrap content in `<div class="book-font-size-malleable ...">` divs and
scatter `<a href="https://ccel.org/...">` navigation anchors and `<div class="spacer"
id="navbar-spacer">` spacers throughout.

- [x] `scripts/clean-library-html.py --mode ccel`: for each of the 15 CCEL docs:
  - Unwrap all `<div class="book-font-size-malleable ...">` divs (keep children)
  - Remove all `<a href="https://ccel.org/...">` navigation links (empty anchor content)
  - Remove `<div class="spacer" id="navbar-spacer">` and `<div class="spacer">` divs
  - Remove `id="i-p0.1"`, `id="ii-p0.1"` etc. anchor-target attributes on heading tags
  - Strip `class="Normal"`, `class="Default"` on `<p>` tags (CCEL default paragraph classes)
  - Run rules 5–8 cleanup on same pass

  **15 docs:** baxter-reformed-pastor, benedict-rule, bernard-on-loving-god,
  catherine-dialogue, edwards-freedom-of-will, edwards-religious-affections,
  francis-de-sales-devout-life, ignatius-spiritual-exercises, julian-revelations,
  luther-bondage-of-will, meister-eckhart-sermons, pseudo-dionysius-works,
  taylor-holy-living, whitefield-sermons, william-law-serious-call

#### LF-A3 · Gutenberg boilerplate strip *(4 docs)*

- [x] `scripts/clean-library-html.py --mode gutenberg`: for each of the 4 Gutenberg docs:
  - Remove everything from `<p>` or `<div>` containing `"PROJECT GUTENBERG"` or
    `"START OF THE PROJECT GUTENBERG EBOOK"` through the first real content paragraph
  - Remove Gutenberg end matter from `"END OF THE PROJECT GUTENBERG EBOOK"` to EOF
  - Run rules 5–8 cleanup on same pass

  **4 docs:** boethius-consolation, bunyan-holy-war, chesterton-everlasting-man,
  calvin-institutes-vol2

---

### LF-B · Convert TEI Format — Calvin Institutes Vol 1 *(HIGH)*

`calvin-institutes-vol1.html` (2.9MB) is a TEI XML export with a single `<section
data-heading="">` wrapping the entire text. The chapter structure is encoded as
`<div class="tei tei-div">` blocks with `<h1-3 class="tei tei-head">` headings.

- [x] Write a targeted converter (inline in `build-library-search-index.py` and direct script):
  - Parse the file with BeautifulSoup
  - Identify `<hN class="tei tei-head">` elements as section boundaries (only
    those at `h2`/`h3` level that are Book/Chapter headings — skip the TOC and
    front matter headings)
  - Wrap the content between each heading into `<section data-heading="...">` elements
    where `data-heading` = cleaned heading text
  - Strip all `tei tei-*` class prefixes from tags; keep the underlying `p`, `em`,
    `blockquote` semantics
  - Remove all `style="..."` attributes (the TEI version has 3,363 inline styles)
  - Remove `class="tei tei-pb"` page break markers and `class="tei tei-anchor"` anchors
  - Strip footnote reference tags (`class="tei tei-noteref"`) or convert to
    `<aside class="lib-fn">` if the footnote text is scholarly rather than editorial
  - Expected output: ~70 properly sectioned chapters across 4 books

---

### LF-C · Re-section Under-split Docs *(HIGH — most impactful for usability)*

44 docs have far too few `<section data-heading="...">` boundaries for their size and content.
The chapter/homily structure already exists in the HTML as `<h2>` or `<h3>` tags — the
sections just haven't been split at those boundaries.

Write `scripts/resection-library-html.py`:
- Input: doc HTML + heading level (`h2` or `h3`) + optional filter pattern
- Splits content at every matching heading, wrapping each chunk in
  `<section data-heading="[heading text]">...<h2 class="lib-section__title">...</h2>...</section>`
- Handles pre-section content (title page, prefatory matter) as a "Preface" section
- Output: replaces the source file

**Per-doc resectioning plan** (heading level → expected section count):

| Doc | Split at | Expected sections |
|---|---|---|
| augustine-confessions | h2 (Book headings) | ~13 ✓ already correct |
| basil-on-holy-spirit | h2 | 30 chapters |
| ryle-holiness | h2 | 21 chapters |
| shepherd-of-hermas | h2 + h3 | ~40 sections (Visions / Mandates / Similitudes) |
| chrysostom-homilies-acts | h2 | 55 homilies |
| cyril-catechetical-lectures | h2 | 39 lectures |
| gregory-nazianzus-orations | h2 | 25 orations |
| gregory-nyssa-great-catechism | h2 | 38 chapters |
| cassian-conferences | h2 | 26 conferences |
| leo-sermons | h2 | 48 sermons |
| athanasius-life-of-antony | h2 | 35 chapters |
| tertullian-prescription | h2 | 44 chapters |
| tertullian-apology | h2 | 43 chapters |
| origen-against-celsus | h2 (Books I–VIII) | 8 books |
| origen-de-principiis | h2 (Books I–IV) | 4 books |
| edwards-religious-affections | h2 + h3 | 15+ (3 parts + 12 signs) |
| edwards-freedom-of-will | h2 + h3 | ~42 parts+sections |
| calvin-institutes-vol2 | h3 | 33 chapters |
| baxter-reformed-pastor | h2 | 10 sections |
| luther-bondage-of-will | h2 | 10 sections |
| whitefield-sermons | h1 (each sermon) | 10 sermons |
| william-law-serious-call | h2 + h3 | 27 chapters |
| francis-de-sales-devout-life | h2 | 122 chapters (5 parts × chapters) |
| bernard-on-loving-god | h3 | 11 chapters |
| catherine-dialogue | h2 | 5 treatises |
| cloud-of-unknowing | h2/h3 (CCEL structure) | 75 chapters |
| murray-ministry-of-intercession | h2 | 19 chapters |
| benedict-rule | h1 (each chapter — 73 total) | 73 chapters |
| watson-body-of-divinity-vol1 | h3/h4 | ~26 heads |
| murray-deeper-christian-life | h2 | 4 chapters (already OK, just verify) |
| roman-catechism | h2 (4 parts) | 4 parts |
| athenagoras-writings | h2 | 5 sections |
| anselm-cur-deus-homo | h3 | 47 chapters |
| boethius-consolation | h2 | 5 books |
| bunyan-grace-abounding | h3 | 3 parts |
| bunyan-holy-war | h2 | 6 sections |
| chesterton-everlasting-man | h3 | 15 chapters |
| newman-apologia | h3 + h4 | ~20 chapters |
| fox-book-of-martyrs | h3 | 26 chapters |
| ignatius-spiritual-exercises | h1 (each exercise) | 11 sections |
| julian-revelations | h2 | 18 revelations |
| pseudo-dionysius-works | h2 | 12 works/sections |
| meister-eckhart-sermons | h3 | 12 sermons |
| taylor-holy-living | h2 + h3 | ~24 chapters |

- [x] Applied `resection-library-html.py` to all docs with parseable heading structure.
  3 docs remain as structural limitations (athenagoras 2 secs, bunyan-holy-war 1 sec, edwards-affections 3 secs) — no heading markers in source HTML.

---

### LF-D · Tag Cleanup — Scriptable Batch *(MEDIUM — 82 docs)*

After chrome stripping (LF-A) and re-sectioning (LF-C), do a final tag-normalisation pass
across all HTML docs. This is fully mechanical — no content judgment needed.

- [x] `scripts/clean-library-html.py --mode tags`: for every HTML doc (ran on all 103):
  - `<i>text</i>` → `<em>text</em>` (47 docs)
  - `<b>text</b>` → `<strong>text</strong>` (12 docs)
  - `<center>text</center>` → `<p class="lib-center">text</p>` (keep it centered but semantic)
  - `<font ...>text</font>` → `text` (strip tag entirely)
  - `<big>text</big>` → `text`, `<small>text</small>` → `text` (strip, no semantic equiv)
  - `<strike>text</strike>` → `<del>text</del>`
  - `<u>text</u>` → `<em>text</em>` (italics are the closest semantic equiv for most uses)
  - Remove all `style="..."` attributes (32 docs)
  - Remove page number markers: `<span class="pagenum">`, `<span class="tei tei-pb">`,
    `<hr class="page"/>`, `[pg N]` patterns (16 docs)
  - Remove empty `<a id="..."></a>` anchor targets with no `href`
  - Remove `id="..."` attributes on `<p>` tags (CCEL/Gutenberg formatting artifacts)

---

### LF-E · "Unknown" Group Cleanup *(MEDIUM — 8 docs)*

These 8 docs have already-documented issues in the **Library Content Cleanup** section of
this TODO. Format-standardisation work here is:

- [x] **`baltimore-catechism.html`** — cleaned by LF-A/LF-D passes
- [x] **`bunyan-grace-abounding.html`** — resectioned at h3 (4 sections); `<i>` → `<em>` done
- [x] **`edwards-sinners.html`** — inline styles stripped; single section correct
- [x] **`fox-book-of-martyrs.html`** — resectioned at h3 (26 chapters); tags converted
- [x] **`luther-95-theses.html`** — inline styles stripped
- [x] **`luther-small-catechism.html`** — styles stripped, `<b>` → `<strong>`
- [x] **`newman-apologia.html`** — 418 `[Pg N]` spans stripped; resectioned at h3 (~20 chapters); styles stripped
- [x] **`watson-body-of-divinity-vol1.html`** — resectioned at h3/h4 (13 sections); page markers stripped

---

### LF-F · "Clean" Group — Verify and Spot-fix *(LOW — 21 docs)*

These 21 docs passed the automated check but may have minor issues not caught by the script.
Each needs a human spot-check pass:

- [x] **aquinas-summa-part-i through part-iii** (4 files) — LF-D `tags` pass ran; `<i>` → `<em>` converted
- [x] **ignatius series** (8 files) — LF-D tags pass ran
- [x] **didache** — LF-D tags pass ran; wst-verse spans harmless, left in place
- [x] **clement-first-epistle, epistle-of-barnabas, polycarp-philippians** — LF-D ran
- [x] **martyrdom-of-polycarp, cyprian-*, epistle-to-diognetus** — LF-D ran; all pass validation
- [x] **anselm-proslogion, augustine-enchiridion, vincent-of-lerins-commonitory** — LF-D ran; all pass

---

### LF-G · JSON-path Docs — Section HTML Cleanup *(LOW — 38 docs)*

The 38 JSON-path docs (`data/library/docs/*.json`) have well-structured sections but the
`.html` field inside each section may carry minor tag issues inherited from source HTML.

- [x] `scripts/clean-library-html.py --mode json-sections`: ran on all 57 JSON docs; 17 files cleaned
- [x] `westminster-larger-catechism.json` and `heidelberg-catechism.json` — now fully indexed via LX-A rebuild

---

### LF-H · Final Validation Pass *(after all groups complete)*

- [x] Run `scripts/validate-library-format.py --all` — **100/103 PASS** (3 structural failures remain: athenagoras, bunyan-holy-war, edwards-religious-affections — no parseable heading structure in source HTML)
- [x] Run `scripts/build-library-search-index.py` — **2535 entries, 142 docs, 705KB**
- [x] Smoke-test 10 representative docs — all 10 PASS (WCF 33, HC 44, WLC 113, Ryle 21, Calvin-vol1 55, Augustine 13, Shepherd 128, Newman 48, Origen 9, Francis-de-Sales 123 sections)
- [x] Commit the rebuilt `data/library/html/*.html`, `data/library/docs/*.json`, and `data/library/search-index.json` together (commit a607190 — 157 files)

---

### LF Effort Reference

| Group | Docs | Primary work | Automation |
|---|---|---|---|
| LF-0 (validation script) | — | Write once | ✓ fully scriptable |
| LF-A (chrome strip) | 64 | Run script per group | ✓ fully scriptable |
| LF-B (TEI Calvin) | 1 | Custom converter | ✓ scriptable |
| LF-C (re-section) | 44 | Per-doc heading judgment | ✗ per-doc manual decisions |
| LF-D (tag cleanup) | 82 | Run script | ✓ fully scriptable |
| LF-E (unknown group) | 8 | Mixed; mostly scriptable | ✓/✗ mixed |
| LF-F (clean spot-check) | 21 | Human review | ✗ manual |
| LF-G (JSON sections) | 38 | Run script | ✓ fully scriptable |
| LF-H (validation) | 141 | Run script + smoke test | ✓ mostly scriptable |

**Recommended order:** LF-0 → LF-A → LF-D → LF-B → LF-C (largest-to-smallest docs first
within that group) → LF-E → LF-G → LF-F → LF-H

---

## Omni-Search Improvements

**Purpose:** The search page (`search/index.html`) is the site's unified discovery layer — two
modes in one: a full-text Bible verse scanner (Verse Search tab) and a multi-source omni-search
(Explore tab, with six async sections: Verses, Word Studies, Topics, Dictionary, Library, Study
Guides). Primary entry point from `Ctrl+K` and the sidebar "Search" button on every page.

**Overall assessment:** Architecture is solid — stale-result protection via generation counter,
streaming partial results at 20+ hits, cache-only verse preview in Explore, search history
dropdown, sort persistence. Several real bugs and two broken UI states found below, plus two
data sources already loaded in `core.js` (Torrey, Hitchcock) that are absent from the Explore tab.

---

### OS-A · Bugs — Active State Never Initialized (Sort + Testament Filter) *(HIGH)*

**Bug 1 — Sort buttons:** `_searchSortMode` is read from localStorage on load (can be
`'canonical'`), but no sort button is given `search-sort--active` on initial render. Both
buttons appear unselected until the user clicks one.

- [x] `search.js` (`initSearchPage`): After wiring sort button click handlers, apply the
  initial active state; using `search-mode-btn--active` (consistent with testament buttons)

**Bug 2 — Testament filter buttons: two different active-state classes.**
HTML marks "All" with `search-mode-btn--active` (styled in CSS). JS click handler toggles
`search-filter--active`, which has **no CSS rule** (confirmed by grep of `bible-ui.css`).
On first click: "OT" gets the invisible class, "All" keeps its visible class — the active
state is visually broken after the first interaction.

- [x] `bible-ui.css` + `search.js`: Unified to `search-mode-btn--active`; no new CSS rule needed
- [x] `search.js` (`initSearchPage`): Testament active state initialized on load

---

### OS-B · Bug — Testament / Book Filter Doesn't Post-Filter Existing Results *(HIGH)*

- [x] `search.js` (`renderSearchResults`): Post-filters `sorted` by `_filterBook` / `_filterTestament` after sort; switching filters immediately re-scopes already-loaded results

---

### OS-C · Bug — History Chip Fires Both Search Handlers on Explore Tab *(MEDIUM)*

- [x] `search.js`: `_fireSearch` promoted to module-level var (assigned in `initSearchPage`)
- [x] `search.js` (`_toggleRecentSearches` click handler): Chip handler uses `if (_fireSearch) _fireSearch()`

---

### OS-D · Bug — Library Results Use Absolute Path *(MEDIUM)*

- [x] `search.js` (`_exploreLibrary`): Uses `_resolve('../../library/')` from core.js

---

### OS-E · Missing — `?q=` URL Param Only Fires Verse Search *(LOW)*

- [x] `search.js` (`initSearchPage`): `?tab=explore` switches tab first, then routes to `handleExploreSearch`; `?tab=explore&q=...` deep-links correctly

---

### OS-F · Missing — Section Result Counts in Explore *(MEDIUM)*

- [x] `search.js`: `data-explore-count` spans added to every section head skeleton; `_setExploreCount()` helper called from all 8 section renderers after results resolve

---

### OS-G · Missing — Torrey's New Topical Textbook as Explore Section *(MEDIUM)*

- [x] `search.js`: `_exploreTorrey()` added; imports `_torreyLoad`/`_torreyData` from core.js
- [x] `search.js` (`handleExploreSearch`): `{ key: 'torrey', title: 'Torrey Topics' }` added to SECTIONS
- [x] `search/index.html`: "Torrey" filter button added

---

### OS-H · Missing — Hitchcock's Bible Names as Explore Section *(LOW)*

- [x] `search.js`: `_exploreNames()` added; imports `_hitchLoad`/`_hitchData` from core.js
- [x] `search.js` (`handleExploreSearch`): `{ key: 'names', title: 'Bible Names' }` added to SECTIONS
- [x] `search/index.html`: "Names" filter button added

---

### OS-I · UX — "No Cached Matches" Verse Preview is Confusing *(LOW)*

- [x] `search.js` (`_exploreVerses`): Message changed to "Switch to Verse Search for full results."

---

### OS-J · UX — Tab Switch Back to Verse Shows Blank Pane *(LOW)*

- [x] `search.js`: Tab click listener re-renders `_lastSearchResults` when switching back to verse tab

---

## Biblical History Time-Lapse — Phase 1 *(complete)*

Phases 1–7 (speed fix, step-mode, ref chips, geographic corrections, new events, refs on all events, tick density) are fully implemented in the codebase. Checkboxes were never closed out but the features exist.

---

## Biblical History Time-Lapse — Phase 2 Overhaul

**Goal:** Fix all known issues with people timing, missing Jesus figure, place markers, persistent trails, land-path accuracy, tribal boundaries, layout, and content depth.

**Key files:** `assets/js/timelapse-map.js`, `data/maps/timelapse.json`, `assets/css/timelapse.css`, `maps/timelapse/index.html`

---

### TL-A · Layout — Event List to Left Column

Currently the event list is buried at the bottom of the 300px right panel with max-height 220px.
New 3-column layout: **[event-list 220px | map flex-1 | info-panel 300px]**.

- [x] `maps/timelapse/index.html`: Move `<div id="tl-event-list">` out of `.tl-info-panel` into a new `<div class="tl-event-col">` as the first child of `.tl-body`
- [x] `timelapse.css`: Add `.tl-event-col` — `width:220px; flex-shrink:0; display:flex; flex-direction:column; border:1px solid border-color; border-radius:10px; overflow:hidden; background:surface`
- [x] `timelapse.css`: `.tl-event-col` gets a header strip showing "Events" label (same style as `.tl2-col-label`)
- [x] `timelapse.css`: `.tl-event-list` inside the column: `flex:1; overflow-y:auto; padding:.4rem .3rem` — no max-height, fills the column
- [x] `timelapse.css`: Remove the old `.tl-event-list` `border-top`, `padding-top`, `max-height` rules from the info-panel context
- [x] `timelapse-map.js`: `_buildEventList()` — add a small era-color swatch dot to each `.tl-ev-item` using the event's `era` field; look up color from `_data.eras` (requires `eras` array in timelapse.json — see below)
- [x] `timelapse.json`: Add top-level `"eras"` array with `{ "id", "label", "color" }` for each era used in `events[].era`, so event list dots and left-border accents can be colored
- [x] Mobile (≤700px): stack to map → event-list (fixed height 160px) → info-panel; left-column layout removed at this breakpoint

---

### TL-B · People — Figure Timing Fixes

The hardcoded `+50` linger makes figures haunt their last position long after death or narrative exit.

- [x] `timelapse.json`: Add `"end": <t>` field to each figure entry
- [x] `timelapse-map.js`: `_figurePos()` — if `fig.end` is defined and `t > fig.end`, return `null` immediately (before the `last.t + 50` check)
- [x] `timelapse.json` — Abraham `"end": 145` (dies before Jacob flees to Haran; Gen 25:7; should not persist into Jacob's Egyptian sojourn at t=190)
- [x] `timelapse.json` — Jacob `"end": 196` (dies in Egypt, Gen 49:33; clears before the long bondage at t=280)
- [x] `timelapse.json` — Moses `"end": 361` (dies on Nebo, Deut 34:5; should vanish immediately, not haunt through the Judges era)
- [x] `timelapse.json` — Joshua `"end": 375` (dies at 110, Josh 24:29; gone before the Judges cycle)
- [x] `timelapse.json` — David `"end": 558` (dies, Solomon reigns, 1 Kgs 2:10)
- [x] `timelapse.json` — Elijah `"end": 633` (translated in whirlwind, 2 Kgs 2:11 — should vanish at translation, not linger)
- [x] `timelapse.json` — Daniel `"end": 771` (last vision at Susa; should not persist into Ezra/Nehemiah era)
- [x] `timelapse.json` — Ezra/Nehemiah `"end": 820` (should not persist into intertestamental era)
- [x] `timelapse.json` — Paul `"end": 1063` (martyrdom ~AD 67; should not persist through Revelation event at t=1075)

---

### TL-C · People — Missing Jesus Figure

The most critical missing figure. Jesus is referenced in ~25% of all events and has no map marker.

- [x] `timelapse.json`: Add figure `{ "id": "jesus", "label": "Jesus", "color": "#c8a84b", "end": 1046 }` with positions:
  - `{ "t": 1028, "lat": 31.70, "lon": 35.20, "note": "Born in Bethlehem — the Word became flesh (John 1:14)" }`
  - `{ "t": 1034, "lat": 32.70, "lon": 35.30, "note": "Boyhood in Nazareth — 'he grew in wisdom and stature' (Luke 2:52)" }`
  - `{ "t": 1040, "lat": 31.83, "lon": 35.54, "note": "Baptized in the Jordan — 'This is my beloved Son' (Matt 3:17)" }`
  - `{ "t": 1040.5, "lat": 31.55, "lon": 35.50, "note": "Tempted forty days in the wilderness (Matt 4:1)" }`
  - `{ "t": 1042, "lat": 32.87, "lon": 35.55, "note": "Galilean ministry — Capernaum and the mount (Matt 4:17)" }`
  - `{ "t": 1044.5, "lat": 31.78, "lon": 35.24, "note": "Triumphal entry into Jerusalem (Matt 21:9)" }`
  - `{ "t": 1045, "lat": 31.78, "lon": 35.24, "note": "Crucified, buried, and risen — 'It is finished' (John 19:30)" }`
- [x] `timelapse-map.js`: `_buildLayers()` — for `fig.id === 'jesus'`, use a larger icon (14px dot vs 10px), gold color `#c8a84b` with white border, label bold; visually distinct from other figures

---

### TL-D · People — Figure–Route Coord Alignment

Figure dots interpolate straight lat/lon between `positions[]` waypoints, independent of the route line. The dot can cut across terrain the route line avoids.

- [x] `timelapse.json` — Abraham: align `positions[]` waypoints to match `abraham-journey` route coords at each matching stop (Ur → Haran → Shechem → Egypt → Hebron → Moriah → Beersheba)
- [x] `timelapse.json` — Jacob: align `positions[]` to match `jacob-journey` coords
- [x] `timelapse.json` — Moses: align `positions[]` to match `exodus-route` coords at Sinai and Nebo waypoints
- [x] `timelapse.json` — Paul: align `positions[]` waypoints to match `paul-journey1/2/3` and `paul-rome` route coords; add Malta stop `{ "t": 1058.5, "lat": 35.90, "lon": 14.51, "note": "Shipwrecked at Malta — Acts 27:44, 'not one of you will be lost'" }`

---

### TL-E · Trails — Persistent Path Visibility

Routes fade out after `linger` units, leaving no trace. The trail should stay visible while the figure is on the map.

- [x] `timelapse.json`: Add `"figureId": "<id>"` to each journey route: `abraham-journey` → `"abraham"`, `jacob-journey` → `"jacob"`, `exodus-route` + `conquest-south/north` → `"moses"`/`"joshua"`, `return-exile` → `"ezra"`, `paul-journey1/2/3/rome` → `"paul"`
- [x] `timelapse-map.js`: `_renderRoutes(t)` — for routes with `figureId`, keep opacity at base while the linked figure is visible (`_figurePos(fig.positions,t) !== null`), then fade over 40 units after the figure disappears; replace the old linger-fade logic for these routes
- [x] Routes without `figureId` (empire marches: `assyrian-march`, `babylon-march`, `alexander-march`) keep current linger-fade behavior unchanged
- [x] `timelapse.json`: Set `"linger": 0` on all figure-linked routes to make intent explicit

---

### TL-F · Routes — Land Path Accuracy

Sparse waypoints produce straight-line segments that cut across mountains and desert.

- [x] `timelapse.json` — `abraham-journey`: add `[33.51,43.80]` (Hit on Euphrates) and `[34.60,41.20]` (Deir ez-Zor area) between Ur and Haran; the route must arc through the Fertile Crescent, not cut across the Syrian desert
- [x] `timelapse.json` — `jacob-journey`: add the same Fertile Crescent waypoints in reverse for the Haran → Bethel return leg
- [x] `timelapse.json` — `return-exile`: add `[34.56,38.97]` (Tadmor/Palmyra) between Babylon and Damascus to follow the Fertile Crescent arc
- [x] `timelapse.json` — `exodus-route`: verify the Sinai route follows the Gulf of Suez coast; add `[29.50,32.60]` (near Suez) and `[29.00,33.20]` (coastal Sinai) if the current line crosses open water
- [x] `timelapse.json` — `paul-rome` (sea / dashed): verify Malta `[35.90,14.51]` is in the coords; add if missing (Acts 27 shipwreck is a key narrative stop)

---

### TL-G · Place Markers — Hoverable Location Dots

Currently zero static location markers. Every event references specific places that need visual anchoring.

- [x] `timelapse.json`: Add top-level `"places"` array; each entry: `{ "id", "label", "lat", "lon", "significance", "visibleFrom": t, "visibleTo": t }`
- [x] `timelapse-map.js`: `_buildLayers()` — create `L.circleMarker` for each place (radius 5, stroke `#666`, fill `#fff`, fillOpacity 0.9, weight 1.5, interactive true); store in `_placeLayers = {}`
- [x] `timelapse-map.js`: Add `_renderPlaces(t)` called from `_render(t)` — show/hide each marker based on `visibleFrom`/`visibleTo`; bind tooltip with `label + significance`
- [x] `timelapse.json` — seed ~35 key locations across all eras:
  - Patriarchal: Ur `(30.96,46.10)`, Haran `(36.86,39.02)`, Shechem `(32.21,35.29)`, Bethel `(31.93,35.22)`, Hebron `(31.53,35.10)`, Beersheba `(31.25,34.79)`, Mahanaim `(32.19,35.75)`, Goshen `(30.78,31.82)`, Mount Moriah `(31.78,35.23)`, Dothan `(32.41,35.19)`
  - Exodus/Conquest: Midian `(28.40,36.60)`, Mount Sinai `(28.54,33.98)`, Kadesh Barnea `(30.34,34.41)`, Jericho `(31.87,35.44)`, Gilgal `(31.88,35.44)`, Shiloh `(32.06,35.29)`, Ai `(31.92,35.28)`, Gibeon `(31.84,35.18)`, Mount Nebo `(31.76,35.73)`, Aphek `(32.10,34.91)`
  - Monarchy/Prophets: Jerusalem `(31.78,35.23)`, Bethlehem `(31.70,35.20)`, Samaria `(32.28,35.20)`, Mount Carmel `(32.74,35.07)`, Valley of Elah `(31.70,34.97)`, Nineveh `(36.36,43.15)`, Babylon `(32.54,44.42)`, Susa `(32.19,48.26)`, Damascus `(33.51,36.28)`
  - NT: Nazareth `(32.70,35.30)`, Capernaum `(32.88,35.57)`, Jordan ford `(31.83,35.54)`, Antioch-Syria `(36.20,36.16)`, Lystra `(37.58,32.34)`, Ephesus `(37.94,27.34)`, Philippi `(41.01,24.28)`, Athens `(37.98,23.73)`, Corinth `(37.91,22.88)`, Rome `(41.90,12.50)`, Malta `(35.90,14.51)`
  - Each place gets `significance` text (1–2 sentences) and era-appropriate `visibleFrom`/`visibleTo`

---

### TL-H · 12 Tribes — Territorial Boundaries

The "Land Divided" event (t=390) shows nothing geographical. Add tribal polygon overlays.

- [x] `timelapse.json`: Add `"tribes"` array; each entry: `{ "id", "label", "color", "coords": [[lat,lon],...] }`
- [x] `timelapse.json` — add approximate polygons for all 12 tribes (simplified ~8–12 points from Josh 13–21):
  - Asher (purple, coastal strip), Naphtali (teal, NE Galilee), Zebulun (orange, central Galilee), Issachar (yellow, Jezreel Valley), Manasseh West (light blue, central highlands), Manasseh East (blue-gray, Bashan/Gilead), Ephraim (green, central hills), Benjamin (tan, Jerusalem area), Dan original (slate, SW lowlands), Judah (gold, large southern), Simeon (light gold, Negev), Reuben (olive, Transjordan S), Gad (brown, Gilead)
- [x] `timelapse-map.js`: `_buildLayers()` — create `L.polygon` per tribe; `fillOpacity: 0`; store in `_tribeLayers = {}`
- [x] `timelapse-map.js`: Add `_renderTribes(t)` called from `_render(t)` — fade in polygons at t=390 (`fillOpacity → 0.22`), hold through t=574 (Kingdom Divides), then fade out; add `L.divIcon` tribe-name labels at polygon centroid
- [x] `timelapse.css`: `.tl-tribe-label` — same style as `.tl-region-label` but `.65rem`
- [x] Tribe polygon hover: tooltip shows tribe name + patriarch + 1 key verse

---

### TL-I · Event Descriptions — Substantive Text

Current `desc` fields are one-sentence placeholders. Expand to 2–4 sentences per event.

- [x] `timelapse.json`: Rewrite all 72 event `desc` fields — 2–4 sentences, plain prose; no inline Scripture citations (those go in `refs` chips)
- [x] Priority rewrites first: Abraham's Call, Covenant of Gen 15, Jacob at Bethel, Jacob Wrestles, Exodus / Passover Night, Sinai Covenant, Golden Calf, Moses Dies, Jordan Crossing, Solomon's Temple, Kingdom Divides, Elijah on Carmel, Samaria Falls, Jerusalem Falls, Cyrus Decree, Incarnation, Baptism of Jesus, Crucifixion & Resurrection, Pentecost, Paul's Conversion
- [x] Add `"desc_extended"` field to the 6 most significant events (Exodus, Sinai, Temple, Jerusalem falls, Incarnation, Resurrection) — 3–5 extra sentences
- [x] `timelapse-map.js`: Render `desc_extended` if present — add `<details><summary>Read more</summary><p>...</p></details>` below main desc paragraph
- [x] `timelapse.css`: Style `<details>` summary as muted `.72rem`; body text matches `.tl-info-desc`

---

### TL-J · Reference Completeness Audit

- [x] `timelapse.json`: Every event must have ≥2 `refs` entries; add missing refs for any event with 0 or 1
- [x] `timelapse.json`: Add NT typological cross-refs to key OT events: Passover → `1 Corinthians 5:7`; Temple dedication → `John 2:19`; Jericho/Rahab → `Hebrews 11:31`; Elijah → `Matthew 17:11`; Cyrus decree → `Isaiah 45:1`
- [x] `timelapse.json`: Add key Christological refs to Life-of-Christ events: Incarnation → `Isaiah 7:14`, `Micah 5:2`; Baptism → `Isaiah 42:1`; Crucifixion → `Isaiah 53:5`, `Psalm 22:1`; Resurrection → `Psalm 16:10`, `1 Corinthians 15:4`
- [x] `timelapse-map.js`: Verify `wireRefLinks(refsEl)` still fires correctly after the TL-A layout restructure (confirm ref chips remain in the info panel and are wired)

---

### TL-K · Minor Fixes and Polish

- [x] `timelapse.json` — Elijah: add final position `{ "t": 633, "lat": 32.28, "lon": 35.20, "note": "Taken up in a whirlwind — Elisha receives the mantle (2 Kgs 2:11)" }` and set `"end": 633`
- [x] `timelapse.json` — Paul: add Malta position `{ "t": 1058.5, "lat": 35.90, "lon": 14.51, "note": "Shipwrecked at Malta — Acts 27:44" }` between Caesarea (t=1057) and Rome (t=1059)
- [x] `timelapse-map.js`: `_yearFromT()` — fix edge case where `raw === 0` returns `'c. 100 BC'`; should return `'c. 1 BC / AD 1'`
- [x] `timelapse.css`: `.tl-ev-item` — add 2px left border using the event's era color (requires era lookup in `_buildEventList()`)
- [x] `timelapse-map.js`: Mobile — add a toggle button (`☰ Events`) overlaid on the map wrapper to show/hide the event list as a slide-in overlay on small screens


---

### TL-L · Full Hero Coverage — Missing Figures, Routes, and Events

Survey result: **10 figures present, 24 major figures missing** across 8 eras. Every section below adds one or more figures with precise positions and the routes/events that accompany them.

---

#### Patriarchs — Isaac

Isaac's entire life was in Canaan; he never left the land. Key stops: Gerar (famine sojourn), Beersheba (wells and oath), Hebron/Mamre (death).

- [x] `timelapse.json` — add figure `{ "id": "isaac", "label": "Isaac", "color": "#a0855b", "end": 159 }` with positions:
  - `{ "t": 105, "lat": 31.25, "lon": 34.79, "note": "Born at Beersheba — 'the son of the promise' (Gen 21:3)" }`
  - `{ "t": 118, "lat": 31.53, "lon": 35.10, "note": "At Mamre/Hebron — Abraham's household (Gen 22–23)" }`
  - `{ "t": 128, "lat": 31.35, "lon": 34.47, "note": "In Gerar — sojourns among the Philistines, digs wells (Gen 26:1)" }`
  - `{ "t": 135, "lat": 31.25, "lon": 34.79, "note": "Back at Beersheba — 'Do not be afraid; I am with you' (Gen 26:24)" }`
  - `{ "t": 150, "lat": 31.53, "lon": 35.10, "note": "At Hebron/Mamre — blesses Jacob instead of Esau (Gen 27)" }`
  - `{ "t": 159, "lat": 31.53, "lon": 35.10, "note": "Dies at Hebron aged 180 — Jacob and Esau bury him (Gen 35:29)" }`

---

#### Patriarchs — Joseph

Joseph has the most geographically complex patriarchal journey: sold at Dothan, slave in Egypt, prison, Pharaoh's court, granary administrator, reconciliation with his brothers.

- [x] `timelapse.json` — add figure `{ "id": "joseph", "label": "Joseph", "color": "#4a8b6f", "end": 200 }` with positions:
  - `{ "t": 155, "lat": 31.53, "lon": 35.10, "note": "In Hebron with Jacob — 'a coat of many colours' (Gen 37:3)" }`
  - `{ "t": 162, "lat": 32.41, "lon": 35.19, "note": "At Dothan — sold by his brothers to Ishmaelite traders for 20 pieces of silver (Gen 37:28)" }`
  - `{ "t": 165, "lat": 30.07, "lon": 31.23, "note": "In Memphis / Potiphar's house — 'the LORD was with Joseph' (Gen 39:2)" }`
  - `{ "t": 170, "lat": 30.07, "lon": 31.23, "note": "In Pharaoh's prison — interprets dreams of the cupbearer and baker (Gen 40)" }`
  - `{ "t": 174, "lat": 30.07, "lon": 31.23, "note": "Before Pharaoh — 'There is none so discerning and wise as you' (Gen 41:39)" }`
  - `{ "t": 182, "lat": 30.78, "lon": 31.82, "note": "In Goshen — brothers arrive for grain; weeps at the sight of Benjamin (Gen 45:14)" }`
  - `{ "t": 190, "lat": 30.78, "lon": 31.82, "note": "Reunites Jacob with the whole family — 'God sent me before you to preserve life' (Gen 45:5)" }`
- [x] `timelapse.json` — add route `{ "id": "joseph-sold", "color": "#4a8b6f", "weight": 2, "start": 162, "end": 166, "linger": 0, "figureId": "joseph", "coords": [[32.41,35.19],[31.78,35.23],[31.25,34.79],[30.50,32.50],[30.07,31.23]] }` (Dothan → Jerusalem ridge road → Beersheba → Sinai route → Memphis)
- [x] `timelapse.json` — add events: `t=162` "Joseph Sold into Egypt — Dreams and Providence" (`refs: Genesis 37:28, Genesis 50:20, Acts 7:9`); `t=174` "Joseph in Pharaoh's Court — Savior of Nations" (`refs: Genesis 41:39, Genesis 45:7, Hebrews 11:22`)

---

#### Exodus — Joshua Extended + Caleb

Joshua was with Moses through the entire 40-year wilderness period, not just the conquest. Caleb was the other faithful spy and received Hebron as his inheritance.

- [x] `timelapse.json` — extend Joshua's `positions[]` backward to include:
  - `{ "t": 321, "lat": 30.78, "lon": 31.82, "note": "The Passover night — led the Israelite fighting men out of Egypt (Ex 12)" }`
  - `{ "t": 330, "lat": 28.54, "lon": 33.98, "note": "At Sinai — commander in the battle against Amalek (Ex 17:9); ascends with Moses" }`
  - `{ "t": 340, "lat": 30.34, "lon": 34.41, "note": "At Kadesh Barnea — one of the two faithful spies (Num 14:6)" }`
  - *(then existing positions from t=341)*
- [x] `timelapse.json` — add figure `{ "id": "caleb", "label": "Caleb", "color": "#7b5c3a", "end": 400 }` with positions:
  - `{ "t": 340, "lat": 30.34, "lon": 34.41, "note": "At Kadesh Barnea — 'Let us go up at once' (Num 13:30)" }`
  - `{ "t": 365, "lat": 31.88, "lon": 35.44, "note": "Crosses the Jordan — base camp at Gilgal (Josh 4)" }`
  - `{ "t": 387, "lat": 31.53, "lon": 35.10, "note": "Receives Hebron at age 85 — 'as yet I am as strong this day as the day Moses sent me' (Josh 14:11)" }`
  - `{ "t": 393, "lat": 31.40, "lon": 34.92, "note": "Conquers Debir; gives daughter Achsah the upper and lower springs (Josh 15:16–19)" }`

---

#### Judges — Deborah

Deborah is the only judge who functioned as both prophet and military commander. Her story is entirely in the northern hill country and Jezreel Valley.

- [x] `timelapse.json` — add figure `{ "id": "deborah", "label": "Deborah", "color": "#9b3d8f", "end": 440 }` with positions:
  - `{ "t": 425, "lat": 31.93, "lon": 35.22, "note": "At her palm tree between Ramah and Bethel — 'she judged Israel at that time' (Judg 4:4)" }`
  - `{ "t": 428, "lat": 33.02, "lon": 35.57, "note": "At Kedesh — summons Barak; 'Has not the LORD gone out before you?' (Judg 4:14)" }`
  - `{ "t": 430, "lat": 32.69, "lon": 35.39, "note": "Mount Tabor — Sisera's 900 iron chariots routed at the Kishon River (Judg 4:15)" }`
- [x] `timelapse.json` — add event `t=430` "Deborah and Barak — The Kishon Sweeps Them Away" (`refs: Judges 4:14, Judges 5:20, Hebrews 11:32`)
- [x] `timelapse.json` — add route `{ "id": "deborah-campaign", "color": "#9b3d8f", "weight": 2, "start": 428, "end": 430, "linger": 0, "figureId": "deborah", "coords": [[31.93,35.22],[33.02,35.57],[32.69,35.39]] }`

---

#### Judges — Gideon

Gideon has an event (t=460) but no figure. His campaign covered Ophrah → Jezreel Valley → east Jordan pursuit.

- [x] `timelapse.json` — add figure `{ "id": "gideon", "label": "Gideon", "color": "#c17f24", "end": 475 }` with positions:
  - `{ "t": 455, "lat": 32.41, "lon": 35.19, "note": "At Ophrah — 'The LORD is with you, O mighty man of valor' (Judg 6:12)" }`
  - `{ "t": 458, "lat": 32.61, "lon": 35.41, "note": "At the Spring of Harod — 300 chosen by how they drink (Judg 7:4–7)" }`
  - `{ "t": 460, "lat": 32.50, "lon": 35.60, "note": "Rout of the Midianites — torches and trumpets; 'A sword for the LORD and for Gideon!' (Judg 7:20)" }`
  - `{ "t": 463, "lat": 32.19, "lon": 35.75, "note": "East of the Jordan — pursuing and capturing Zebah and Zalmunna (Judg 8:12)" }`
  - `{ "t": 467, "lat": 32.41, "lon": 35.19, "note": "Returns to Ophrah — refuses kingship; 'The LORD will rule over you' (Judg 8:23)" }`

---

#### Judges — Samson

Samson's entire story is in the lowland border between Dan and Philistia — one of the most geographically concentrated of any judge.

- [x] `timelapse.json` — add figure `{ "id": "samson", "label": "Samson", "color": "#c44d29", "end": 493 }` with positions:
  - `{ "t": 476, "lat": 31.78, "lon": 34.97, "note": "Born at Zorah — 'set apart to God from the womb' (Judg 13:5)" }`
  - `{ "t": 480, "lat": 31.64, "lon": 34.82, "note": "At Timnah — kills the lion; Philistine wife; riddle of the feast (Judg 14)" }`
  - `{ "t": 484, "lat": 31.51, "lon": 34.88, "note": "At Lehi — slays a thousand with the jawbone of a donkey (Judg 15:15)" }`
  - `{ "t": 488, "lat": 31.50, "lon": 34.47, "note": "At Gaza — Delilah; 'The LORD has left me' (Judg 16:20)" }`
  - `{ "t": 492, "lat": 31.50, "lon": 34.47, "note": "Temple of Dagon, Gaza — 'Let me die with the Philistines' (Judg 16:30)" }`
- [x] `timelapse.json` — add event `t=488` "Samson and Delilah — Gaza and the Temple of Dagon" (`refs: Judges 16:20, Judges 16:30, Hebrews 11:32`)

---

#### Judges — Ruth

Ruth's journey from Moab to Bethlehem is one of the Bible's clearest geographic stories and the most important 'outsider enters the covenant' narrative before the NT.

- [x] `timelapse.json` — add figure `{ "id": "ruth", "label": "Ruth", "color": "#b87333", "end": 478 }` with positions:
  - `{ "t": 465, "lat": 31.15, "lon": 35.72, "note": "In Moab — 'Where you go I will go; your God shall be my God' (Ruth 1:16)" }`
  - `{ "t": 470, "lat": 31.70, "lon": 35.20, "note": "Arrives in Bethlehem at barley harvest — 'The LORD has brought me back empty' (Ruth 1:21)" }`
  - `{ "t": 474, "lat": 31.70, "lon": 35.20, "note": "Threshing floor — kinsman-redeemer oath; 'All the city knows you are a worthy woman' (Ruth 3:11)" }`
- [x] `timelapse.json` — add route `{ "id": "ruth-journey", "color": "#b87333", "weight": 2, "start": 465, "end": 470, "linger": 0, "figureId": "ruth", "coords": [[31.15,35.72],[31.36,35.50],[31.70,35.20]] }` (Moab → Dead Sea road → Bethlehem)
- [x] `timelapse.json` — add event `t=470` "Ruth — 'Where You Go I Will Go'" (`refs: Ruth 1:16, Ruth 2:12, Matthew 1:5`)

---

#### Judges — Samuel

Samuel bridges the Judges and Monarchy eras. His circuit judge route is one of the most specific geographic patterns in the OT.

- [x] `timelapse.json` — add figure `{ "id": "samuel", "label": "Samuel", "color": "#556b8a", "end": 526 }` with positions:
  - `{ "t": 490, "lat": 32.06, "lon": 35.29, "note": "At Shiloh — hears the voice of the LORD; 'Speak, for your servant hears' (1 Sam 3:10)" }`
  - `{ "t": 494, "lat": 31.92, "lon": 35.22, "note": "At Ramah (home) — Eli dies; the ark is captured; Samuel leads Israel in repentance" }`
  - `{ "t": 502, "lat": 31.93, "lon": 35.22, "note": "Circuit: Bethel — judging all Israel year by year (1 Sam 7:16)" }`
  - `{ "t": 506, "lat": 31.88, "lon": 35.44, "note": "Circuit: Gilgal — 'Has the LORD as great delight in burnt offerings as in obeying his voice?' (1 Sam 15:22)" }`
  - `{ "t": 510, "lat": 31.86, "lon": 35.18, "note": "Circuit: Mizpah — 'Thus far the LORD has helped us' — sets up Ebenezer (1 Sam 7:12)" }`
  - `{ "t": 514, "lat": 31.92, "lon": 35.22, "note": "Anoints Saul at Ramah — 'Has not the LORD anointed you to be prince over his people?' (1 Sam 10:1)" }`
  - `{ "t": 519, "lat": 31.70, "lon": 35.20, "note": "At Bethlehem — anoints the boy David; 'Man looks on the outward appearance' (1 Sam 16:7)" }`
  - `{ "t": 524, "lat": 31.92, "lon": 35.22, "note": "Dies at Ramah — all Israel mourns (1 Sam 25:1)" }`
- [x] `timelapse.json` — add event `t=519` "Samuel Anoints David — The Shepherd King" (`refs: 1 Samuel 16:7, 1 Samuel 16:13, Acts 13:22`)

---

#### Monarchy — Saul

Saul's tragedy spans the entire northern kingdom: from his anointing at Ramah to his death at Gilboa.

- [x] `timelapse.json` — add figure `{ "id": "saul", "label": "Saul", "color": "#8b3a62", "end": 530 }` with positions:
  - `{ "t": 514, "lat": 31.92, "lon": 35.22, "note": "Anointed by Samuel at Ramah — taller than any of the people (1 Sam 9:2)" }`
  - `{ "t": 516, "lat": 31.86, "lon": 35.21, "note": "At Gibeah — his capital; the Spirit of God rushed upon him (1 Sam 10:26)" }`
  - `{ "t": 520, "lat": 32.33, "lon": 35.72, "note": "At Jabesh-gilead — routs the Ammonites; confirmed as king (1 Sam 11:11)" }`
  - `{ "t": 524, "lat": 31.47, "lon": 35.45, "note": "At En-gedi — pursuing David in the wilderness; David spares his life (1 Sam 24:4)" }`
  - `{ "t": 527, "lat": 32.68, "lon": 35.33, "note": "At Endor — consults the medium; 'Tomorrow you and your sons shall be with me' (1 Sam 28:19)" }`
  - `{ "t": 528, "lat": 32.52, "lon": 35.36, "note": "Falls on Mount Gilboa — 'How the mighty have fallen' (2 Sam 1:19)" }`
- [x] `timelapse.json` — add event `t=528` "Saul Falls at Gilboa — How the Mighty Have Fallen" (`refs: 1 Samuel 31:4, 2 Samuel 1:19, 1 Chronicles 10:13`)

---

#### Monarchy — David Extended (Flight from Saul)

David's current positions jump from Goliath to Ziklag with nothing in between. The flight years (Adullam → En-gedi → Ziph → Maon → Ziklag) are key narrative geography.

- [x] `timelapse.json` — expand David's `positions[]` between t=525 and t=528:
  - `{ "t": 526, "lat": 31.55, "lon": 35.07, "note": "Cave of Adullam — 400 men gather to him; 'distressed, in debt, and bitter in soul' (1 Sam 22:2)" }`
  - `{ "t": 527, "lat": 31.47, "lon": 35.45, "note": "Wilderness of En-gedi — cuts Saul's robe in the cave; 'The LORD judge between you and me' (1 Sam 24:12)" }`

---

#### Monarchy — Solomon

Solomon's reign is currently only the temple event. His international trade and the Queen of Sheba's visit are geographically significant.

- [x] `timelapse.json` — add figure `{ "id": "solomon", "label": "Solomon", "color": "#d4a017", "end": 575 }` with positions:
  - `{ "t": 555, "lat": 31.78, "lon": 35.23, "note": "Crowned in Jerusalem — 'Give your servant an understanding heart' (1 Kgs 3:9)" }`
  - `{ "t": 560, "lat": 31.78, "lon": 35.23, "note": "Temple dedicated — the cloud fills the house of the LORD (1 Kgs 8:10–11)" }`
  - `{ "t": 563, "lat": 29.55, "lon": 34.95, "note": "At Ezion-geber on the Red Sea — fleet to Ophir; 420 talents of gold (1 Kgs 9:26–28)" }`
  - `{ "t": 568, "lat": 31.78, "lon": 35.23, "note": "Queen of Sheba visits — 'Not even half was told me; your wisdom exceeds what I heard' (1 Kgs 10:7)" }`
  - `{ "t": 573, "lat": 31.78, "lon": 35.23, "note": "Heart turned away in old age — high places for Chemosh and Molech (1 Kgs 11:7)" }`
- [x] `timelapse.json` — add event `t=568` "Solomon and the Queen of Sheba — Wisdom on Display" (`refs: 1 Kings 10:7, 1 Kings 10:9, Matthew 12:42`)

---

#### Divided Kingdom — Elisha

Elisha has an event (t=635, "Chariots of Fire") but no figure. His ministry is geographically rich and spans decades.

- [x] `timelapse.json` — add figure `{ "id": "elisha", "label": "Elisha", "color": "#2a8b6b", "end": 668 }` with positions:
  - `{ "t": 633, "lat": 31.83, "lon": 35.54, "note": "At the Jordan — receives Elijah's mantle; 'Where is the LORD, the God of Elijah?' (2 Kgs 2:14)" }`
  - `{ "t": 637, "lat": 32.56, "lon": 35.49, "note": "At Shunem — the Shunammite woman's son raised from the dead (2 Kgs 4:35)" }`
  - `{ "t": 643, "lat": 31.83, "lon": 35.54, "note": "Naaman healed in the Jordan — 'Behold, his flesh was restored like the flesh of a little child' (2 Kgs 5:14)" }`
  - `{ "t": 650, "lat": 32.41, "lon": 35.19, "note": "At Dothan — surrounded by Aramean army; 'Those who are with us are more than those with them' (2 Kgs 6:16)" }`
  - `{ "t": 655, "lat": 33.51, "lon": 36.28, "note": "At Damascus — anoints Hazael king of Aram; weeps over coming judgment on Israel (2 Kgs 8:11)" }`
  - `{ "t": 663, "lat": 32.28, "lon": 35.20, "note": "In Samaria — the siege lifted; 'Tomorrow about this time a seah of fine flour shall be sold for a shekel' (2 Kgs 7:1)" }`
- [x] `timelapse.json` — add event `t=643` "Elisha — Naaman Healed and the Syrian Axe-Head Floats" (`refs: 2 Kings 5:14, 2 Kings 6:17, Luke 4:27`)

---

#### Divided Kingdom — Jonah

Jonah's flight to Tarshish and preaching to Nineveh is the most dramatically geographic story in the OT prophets, with a sea leg and a land leg.

- [x] `timelapse.json` — add figure `{ "id": "jonah", "label": "Jonah", "color": "#4a7fcb", "end": 674 }` with positions:
  - `{ "t": 667, "lat": 32.08, "lon": 34.77, "note": "At Joppa — buys passage on a ship fleeing from the presence of the LORD (Jon 1:3)" }`
  - `{ "t": 669, "lat": 36.00, "lon": 26.00, "note": "In the Mediterranean — thrown overboard; three days in the great fish (Jon 1:17)" }`
  - `{ "t": 671, "lat": 36.36, "lon": 43.15, "note": "At Nineveh — 'Yet forty days, and Nineveh shall be overthrown!' (Jon 3:4)" }`
  - `{ "t": 673, "lat": 36.45, "lon": 43.25, "note": "East of Nineveh — shade plant, burning wind; 'Should I not pity Nineveh?' (Jon 4:11)" }`
- [x] `timelapse.json` — add route `{ "id": "jonah-sea", "color": "#4a7fcb", "weight": 2, "dashed": true, "start": 667, "end": 670, "linger": 0, "figureId": "jonah", "coords": [[32.08,34.77],[35.00,32.00],[36.00,26.00],[37.00,22.00]] }` (Joppa → Mediterranean, dashed sea)
- [x] `timelapse.json` — add route `{ "id": "jonah-nineveh", "color": "#4a7fcb", "weight": 2, "start": 670, "end": 672, "linger": 0, "figureId": "jonah", "coords": [[37.00,22.00],[36.50,33.00],[36.36,43.15]] }` (back east toward Nineveh, via coast)
- [x] `timelapse.json` — add event `t=671` "Jonah at Nineveh — The Whole City Repents" (`refs: Jonah 3:5, Jonah 4:11, Matthew 12:41`)

---

#### Divided Kingdom — Isaiah

Isaiah ministered exclusively in Jerusalem but is one of the greatest OT prophets. His presence during the Sennacherib crisis (already an event at t=687) should be visible.

- [x] `timelapse.json` — add figure `{ "id": "isaiah", "label": "Isaiah", "color": "#6b4e8a", "end": 695 }` with positions:
  - `{ "t": 668, "lat": 31.78, "lon": 35.23, "note": "Call vision in Jerusalem — 'Here I am! Send me' (Isa 6:8); 'in the year King Uzziah died'" }`
  - `{ "t": 675, "lat": 31.78, "lon": 35.23, "note": "To Ahaz — 'Behold, the virgin shall conceive'; the Immanuel sign (Isa 7:14)" }`
  - `{ "t": 687, "lat": 31.78, "lon": 35.23, "note": "To Hezekiah — 'He shall not come into this city'; 185,000 Assyrians struck down (Isa 37:33–36)" }`
  - `{ "t": 692, "lat": 31.78, "lon": 35.23, "note": "Servant Songs — 'He was wounded for our transgressions' (Isa 53:5); the book's great climax" }`

---

#### Exile & Return — Jeremiah

Jeremiah stayed in Jerusalem through the fall and was then forcibly dragged to Egypt — one of the great tragic geographic arcs in the OT.

- [x] `timelapse.json` — add figure `{ "id": "jeremiah", "label": "Jeremiah", "color": "#8b4513", "end": 752 }` with positions:
  - `{ "t": 717, "lat": 31.78, "lon": 35.23, "note": "Called in Jerusalem — 'Before I formed you in the womb I knew you' (Jer 1:5); Josiah's reforms" }`
  - `{ "t": 731, "lat": 31.78, "lon": 35.23, "note": "At the gate of the temple — 'Amend your ways'; the temple-sermon (Jer 7)" }`
  - `{ "t": 738, "lat": 31.78, "lon": 35.23, "note": "Imprisoned in Jerusalem — writes the letter to the exiles in Babylon (Jer 29)" }`
  - `{ "t": 744, "lat": 31.78, "lon": 35.23, "note": "Jerusalem falls — Nebuchadnezzar releases him; 'Seek the welfare of the city' (Jer 29:7)" }`
  - `{ "t": 748, "lat": 30.88, "lon": 32.09, "note": "At Tahpanhes, Egypt — taken against his will; 'Behold, I am watching over them for disaster' (Jer 43:10)" }`
- [x] `timelapse.json` — add route `{ "id": "jeremiah-egypt", "color": "#8b4513", "weight": 2, "start": 745, "end": 748, "linger": 0, "figureId": "jeremiah", "coords": [[31.78,35.23],[31.25,34.79],[30.50,32.80],[30.88,32.09]] }` (Jerusalem → Beersheba → Sinai → Tahpanhes)
- [x] `timelapse.json` — add event `t=726` "Jeremiah — The Weeping Prophet and the New Covenant" (`refs: Jeremiah 31:31, Jeremiah 29:11, Hebrews 8:8`)

---

#### Exile & Return — Ezekiel

Ezekiel was deported in the first wave (597 BC) and prophesied among the exiles at the Chebar River in Babylon.

- [x] `timelapse.json` — add figure `{ "id": "ezekiel", "label": "Ezekiel", "color": "#4a6741", "end": 762 }` with positions:
  - `{ "t": 735, "lat": 31.78, "lon": 35.23, "note": "In Jerusalem — priest, son of Buzi; about to be deported (Ezek 1:3)" }`
  - `{ "t": 738, "lat": 32.54, "lon": 44.42, "note": "Deported to Babylon with Jehoiachin — 'by the Chebar canal' (Ezek 1:1)" }`
  - `{ "t": 741, "lat": 32.38, "lon": 45.59, "note": "At Tel-abib on the Chebar River — 'I sat there overwhelmed for seven days' (Ezek 3:15)" }`
  - `{ "t": 744, "lat": 32.38, "lon": 45.59, "note": "Vision of Jerusalem's fall — a fugitive arrives: 'The city has been struck' (Ezek 33:21)" }`
  - `{ "t": 755, "lat": 32.38, "lon": 45.59, "note": "The valley of dry bones — 'Can these bones live?'; restored Israel (Ezek 37:3)" }`
- [x] `timelapse.json` — add event `t=741` "Ezekiel — Visions by the River Chebar" (`refs: Ezekiel 1:1, Ezekiel 37:3, Ezekiel 47:1`)

---

#### Exile & Return — Split Ezra/Nehemiah Figure into Three

The current `ezra` figure conflates Zerubbabel (first return, 538 BC), Ezra (458 BC), and Nehemiah (445 BC). Split into three with accurate positions.

- [x] `timelapse.json` — replace current `ezra` figure with three separate figures:
  - **Zerubbabel** `{ "id": "zerubbabel", "label": "Zerubbabel", "color": "#6b7a4a", "end": 782 }`:
    - `{ "t": 767, "lat": 32.54, "lon": 44.42, "note": "In Babylon — leads the first return of 42,360 exiles (Ezra 2:64)" }`
    - `{ "t": 771, "lat": 31.78, "lon": 35.23, "note": "In Jerusalem — lays the Temple foundation; people weep and shout (Ezra 3:12)" }`
    - `{ "t": 778, "lat": 31.78, "lon": 35.23, "note": "Temple completed — 'the glory of this latter temple shall be greater' (Hag 2:9; Ezra 6:15)" }`
  - **Ezra** `{ "id": "ezra-scribe", "label": "Ezra", "color": "#7a5c2a", "end": 815 }`:
    - `{ "t": 806, "lat": 32.54, "lon": 44.42, "note": "Departs Babylon — 'a teacher well versed in the Law of Moses' (Ezra 7:6)" }`
    - `{ "t": 808, "lat": 31.78, "lon": 35.23, "note": "Arrives Jerusalem — reads the Law publicly; the people weep at hearing it (Neh 8:9)" }`
  - **Nehemiah** `{ "id": "nehemiah", "label": "Nehemiah", "color": "#5a6b8a", "end": 820 }`:
    - `{ "t": 806, "lat": 32.19, "lon": 48.26, "note": "In Susa — cupbearer to Artaxerxes; hears the walls of Jerusalem are broken down (Neh 1:3)" }`
    - `{ "t": 812, "lat": 31.78, "lon": 35.23, "note": "Rebuilds Jerusalem's walls in 52 days — 'The God of heaven will make us prosper' (Neh 2:20)" }`

---

#### Exile & Return — Esther

Esther's entire story takes place in Susa and is the most significant Persian-era narrative.

- [x] `timelapse.json` — add figure `{ "id": "esther", "label": "Esther", "color": "#c2648a", "end": 808 }` with positions:
  - `{ "t": 795, "lat": 32.19, "lon": 48.26, "note": "In Susa — Mordecai's adopted daughter; 'beautiful in form and appearance' (Est 2:7)" }`
  - `{ "t": 800, "lat": 32.19, "lon": 48.26, "note": "Chosen as queen — 'Who knows whether you have not come to the kingdom for such a time as this?' (Est 4:14)" }`
  - `{ "t": 805, "lat": 32.19, "lon": 48.26, "note": "Intercedes before the king — Haman hanged; Jews delivered throughout the empire (Est 7:10)" }`
- [x] `timelapse.json` — add event `t=800` "Esther — For Such a Time as This" (`refs: Esther 4:14, Esther 7:3, Esther 8:11`)

---

#### Life of Christ — John the Baptist

John the Baptist is the bridge figure between the OT and Gospels. He must be visible on the map.

- [x] `timelapse.json` — add figure `{ "id": "john-baptist", "label": "John the Baptist", "color": "#7a5c8a", "end": 1042.5 }` with positions:
  - `{ "t": 1036, "lat": 31.65, "lon": 35.12, "note": "In the Judean wilderness — 'The voice of one crying in the wilderness' (Isa 40:3; Matt 3:3)" }`
  - `{ "t": 1039, "lat": 31.83, "lon": 35.54, "note": "At the Jordan — baptizing; 'Repent, for the kingdom of heaven is at hand' (Matt 3:2)" }`
  - `{ "t": 1040, "lat": 31.83, "lon": 35.54, "note": "Baptizes Jesus — 'Behold, the Lamb of God, who takes away the sin of the world' (John 1:29)" }`
  - `{ "t": 1041.5, "lat": 31.72, "lon": 35.72, "note": "Imprisoned at Machaerus — 'Are you the one who is to come?' (Matt 11:3)" }`
  - `{ "t": 1042.5, "lat": 31.72, "lon": 35.72, "note": "Beheaded at Machaerus — 'Among those born of women none is greater than John' (Luke 7:28)" }`
- [x] `timelapse.json` — add event `t=1039` "John the Baptist — The Voice in the Wilderness" (`refs: Isaiah 40:3, Matthew 3:2, John 1:29, Malachi 4:5`)

---

#### Paul Extended — Tarsus Origin and Arabia Retreat

Paul's current positions begin at Jerusalem (persecutor). He needs his origin city (Tarsus) and the post-conversion Arabia retreat (Gal 1:17).

- [x] `timelapse.json` — prepend to Paul's `positions[]`:
  - `{ "t": 1045, "lat": 36.89, "lon": 34.89, "note": "From Tarsus in Cilicia — 'a citizen of no ordinary city' (Acts 21:39)" }`
  - *(then existing t=1046 Jerusalem persecutor position)*
- [x] `timelapse.json` — add position after t=1047 Damascus:
  - `{ "t": 1048, "lat": 30.50, "lon": 36.50, "note": "In Arabia — immediate post-conversion retreat; 'I did not consult with any human being' (Gal 1:17)" }`

---

#### Early Church — Peter

Peter's journeys through Acts cover more geographic ground than any other apostle except Paul.

- [x] `timelapse.json` — add figure `{ "id": "peter", "label": "Peter", "color": "#1a6b9a", "end": 1063 }` with positions:
  - `{ "t": 1046, "lat": 31.78, "lon": 35.23, "note": "In Jerusalem — Pentecost; 3,000 added; 'Repent and be baptized' (Acts 2:38)" }`
  - `{ "t": 1048, "lat": 32.21, "lon": 35.29, "note": "In Samaria — lays hands on new believers with John (Acts 8:14)" }`
  - `{ "t": 1049, "lat": 31.96, "lon": 34.89, "note": "At Lydda — heals Aeneas who had been paralyzed eight years (Acts 9:34)" }`
  - `{ "t": 1050, "lat": 32.08, "lon": 34.77, "note": "At Joppa — raises Tabitha from the dead (Acts 9:40)" }`
  - `{ "t": 1051, "lat": 32.50, "lon": 34.90, "note": "At Caesarea — Cornelius; 'God shows no partiality' (Acts 10:34); first Gentile converts" }`
  - `{ "t": 1054, "lat": 36.20, "lon": 36.16, "note": "At Antioch — confronted by Paul; 'not in step with the truth of the gospel' (Gal 2:14)" }`
  - `{ "t": 1062, "lat": 41.90, "lon": 12.50, "note": "In Rome — '1 Peter 5:13 sends greetings from Babylon'; martyred ~AD 64–68" }`
- [x] `timelapse.json` — add route `{ "id": "peter-journeys", "color": "#1a6b9a", "weight": 2, "start": 1046, "end": 1062, "linger": 0, "figureId": "peter", "coords": [[31.78,35.23],[32.21,35.29],[31.96,34.89],[32.08,34.77],[32.50,34.90],[36.20,36.16],[41.90,12.50]] }`
- [x] `timelapse.json` — add event `t=1051` "Peter and Cornelius — The Gentile Door Opens" (`refs: Acts 10:34, Acts 10:45, Acts 11:18, Ephesians 2:14`)

---

#### Early Church — Philip the Evangelist

Philip's journey from Jerusalem to Samaria to the Gaza road is the first recorded missionary movement outward from Jerusalem (Acts 8), and one of the most geographically clean arcs in Acts.

- [x] `timelapse.json` — add figure `{ "id": "philip-evang", "label": "Philip", "color": "#3a8b5a", "end": 1053 }` with positions:
  - `{ "t": 1047, "lat": 31.78, "lon": 35.23, "note": "In Jerusalem — one of the Seven; 'full of faith and of the Holy Spirit' (Acts 6:5)" }`
  - `{ "t": 1048, "lat": 32.21, "lon": 35.29, "note": "In Samaria — proclaims Christ; great joy in that city (Acts 8:8)" }`
  - `{ "t": 1049, "lat": 31.50, "lon": 34.72, "note": "On the Gaza road — meets the Ethiopian eunuch; baptizes him in the desert (Acts 8:38)" }`
  - `{ "t": 1050, "lat": 31.82, "lon": 34.65, "note": "At Azotus / Ashdod — passes through, preaching to all the towns (Acts 8:40)" }`
  - `{ "t": 1052, "lat": 32.50, "lon": 34.90, "note": "At Caesarea — 'Philip the evangelist'; hosts Paul on his final journey (Acts 21:8)" }`
- [x] `timelapse.json` — add route `{ "id": "philip-journey", "color": "#3a8b5a", "weight": 2, "start": 1047, "end": 1052, "linger": 0, "figureId": "philip-evang", "coords": [[31.78,35.23],[32.21,35.29],[31.50,34.72],[31.82,34.65],[32.50,34.90]] }`
- [x] `timelapse.json` — add event `t=1049` "Philip and the Ethiopian Eunuch — The Gospel Goes to Africa" (`refs: Acts 8:35, Acts 8:38, Isaiah 53:7`)

---

#### Early Church — John the Apostle

John ends the biblical timeline on Patmos writing Revelation — his final position should be the most distant from Jerusalem of any apostle.

- [x] `timelapse.json` — add figure `{ "id": "john-apostle", "label": "John", "color": "#2a5a8a", "end": 1076 }` with positions:
  - `{ "t": 1046, "lat": 31.78, "lon": 35.23, "note": "In Jerusalem — Pentecost; the disciple Jesus loved (John 21:7)" }`
  - `{ "t": 1048, "lat": 32.21, "lon": 35.29, "note": "In Samaria — with Peter to confirm the Samaritan believers (Acts 8:14)" }`
  - `{ "t": 1060, "lat": 37.94, "lon": 27.34, "note": "At Ephesus — traditional residence; the seven letters to the churches are from here (Rev 1–3)" }`
  - `{ "t": 1075, "lat": 37.30, "lon": 26.55, "note": "On Patmos — 'I was in the Spirit on the Lord's day'; the Revelation of Jesus Christ (Rev 1:9)" }`
- [x] `timelapse.json` — add route `{ "id": "john-apostle-journey", "color": "#2a5a8a", "weight": 2, "start": 1046, "end": 1075, "linger": 0, "figureId": "john-apostle", "coords": [[31.78,35.23],[32.21,35.29],[37.94,27.34],[37.30,26.55]] }`

---

#### Summary of TL-L additions

- **New figures:** Isaac, Joseph, Caleb, Deborah, Gideon, Samson, Ruth, Samuel, Saul, Solomon, Elisha, Jonah, Isaiah, Jeremiah, Ezekiel, Esther, John the Baptist, Peter, Philip the Evangelist, John the Apostle (+split Ezra/Nehemiah into Zerubbabel/Ezra/Nehemiah = 3)
- **Total new figures:** 23 (brings total from 9 → ~32)
- **New routes:** joseph-sold, deborah-campaign, ruth-journey, jonah-sea, jonah-nineveh, jeremiah-egypt, peter-journeys, philip-journey, john-apostle-journey
- **New events:** Joseph sold/in court, Deborah/Kishon, Samson/Gaza, Ruth's journey, Samuel anoints David, Saul falls at Gilboa, Solomon/Sheba, Elisha/Naaman, Jonah/Nineveh, Jeremiah/new covenant, Ezekiel/Chebar, Esther/such a time, John Baptist/wilderness, Philip/Ethiopian, Peter/Cornelius

---

## Timeline Pages — UX & Content Improvements

These items apply to the two 3-column text timelines (`timeline/` and `church-history/`), which
share `timeline.js` and `timeline.css`. Separate from the animated timelapse map (`maps/timelapse/`),
whose improvements are tracked under TL-A–TL-L above.

**Current state:** Biblical: 10 eras, 92 events, c. 4000 BC → Consummation. Church: 8 eras,
46 events, AD 30–2000. Both lazy-load detail on first click. Neither has URL state, session
persistence, search, or prev/next navigation.

**Key issues found:**
- No URL state — every visit starts blank; events are unbookmarkable
- `yearNum: 9999` hack for the Consummation distorts the entire biblical spine's proportional layout
- The two timelines are isolated — Pentecost/Jerusalem Council appear in both with no cross-link
- 14 church events have direct library document matches (Augustine, Luther, Calvin, Anselm,
  Aquinas, Westminster, Nicaea, Chalcedon, Benedict) but the detail panel never surfaces them
- `key_texts` in church detail are all Bible refs — the doc-chip CSS path was never populated
- No prev/next navigation within an era requires two clicks to advance to the adjacent event

---

### TLU-A · URL State — Deep-link and Restore Selection *(HIGH)*

Every visit starts blank. Events are unbookmarkable and unshareable. The fix is `?era=` +
`?event=` params, written on every selection and read on page load.

- [x] `timeline.js` (`_selectEra`): After updating state, call
  `history.replaceState(null, '', '?era=' + encodeURIComponent(era.id))`
- [x] `timeline.js` (`_clickEvent`): After updating state, call
  `history.replaceState(null, '', '?era=' + encodeURIComponent(_activeEra) + '&event=' + encodeURIComponent(ev.id))`
- [x] `timeline.js` (controller `.init()`): After `_renderEraSpine()` resolves, read
  `new URLSearchParams(location.search)`; if `?era=` is set call `_selectEra(matchingEra)`;
  if `?event=` is also set, also call `_clickEvent(matchingEvent, matchingEra)` — the detail
  lazy-load triggers through the normal selection path
- [x] `timeline.js` (`_wireDetailClose`): On close, `replaceState` back to `?era=` only

---

### TLU-B · Session Persistence — Restore Last View on Return *(MEDIUM)*

Navigating away and back resets to blank. `sessionStorage` restores the last selection within
the same browser session without requiring the user to use a shared URL.

- [x] `timeline.js` (`_makeController`): Accept `storageKey` in `cfg`
  (`'bsw_tl'` for biblical, `'bsw_chtl'` for church) to namespace the two timelines
- [x] `timeline.js` (`_selectEra`): `sessionStorage.setItem(cfg.storageKey + '_era', era.id)`
- [x] `timeline.js` (`_clickEvent`): `sessionStorage.setItem(cfg.storageKey + '_event', ev.id)`
- [x] `timeline.js` (`.init()` after spine renders): If `?era=` URL param is absent, fall back
  to `sessionStorage.getItem(cfg.storageKey + '_era')`; restore event the same way

---

### TLU-C · Prev/Next Event Navigation in Detail Panel *(HIGH)*

Moving from "The Fall" to "Cain & Abel" requires clicking back to the events column, then
clicking the next node — two clicks with context lost. Prev/next in the detail header allows
sequential reading of an era without leaving the detail panel.

- [x] `timeline.js` (`_buildDetailShell`): Add `<div class="tl-detail-nav">` inside
  `.tl-detail-inner` above the header; it receives `{ idx, total }` (index within the current
  era's events array) and renders:
  `[← Prev]  [N of M]  [Next →]`
  where Prev/Next call `_clickEvent` on adjacent era events; disabled (`.tl-detail-nav-btn--disabled`)
  on first/last event
- [x] `timeline.js` (`_clickEvent`): Compute `idx` by finding `ev.id` in the era-filtered events
  array; pass `{ idx, total }` to `_buildDetailShell`
- [x] `timeline.css`: `.tl-detail-nav { display:flex; align-items:center; justify-content:space-between; padding:.4rem .8rem; border-bottom:1px solid var(--color-border); background:var(--color-bg); font-size:.75rem; }`
  `.tl-detail-nav-btn { background:none; border:none; cursor:pointer; color:var(--color-primary); font-size:.78rem; padding:.1rem .2rem; }`
  `.tl-detail-nav-btn--disabled { opacity:.3; pointer-events:none; }`
  `.tl-detail-nav-pos { color:var(--color-muted); font-size:.7rem; }`

---

### TLU-D · Cross-Timeline Bridge — Biblical → Church History *(HIGH)*

The biblical timeline ends at AD 95; church history starts at AD 30. They share two events
(Pentecost, Jerusalem Council) with no visual connection. Users following redemptive history
sequentially get no prompt to continue.

- [x] `timeline.js` (`_buildDetailBody`): For `!isChurch` (biblical timeline), if the active era is the NT/early-church era (check the actual era `id` value in `data/timeline/events.json` — likely `'early-church'` or `'new-testament'`, **not** `'church'`), append after the Related Maps section:
  ```html
  <div class="tl-detail-crossover">
    <span class="tl-detail-crossover__label">Continue the story</span>
    <a class="tl-detail-crossover__link" href="../church-history/">
      Church History Timeline — from Pentecost to today →
    </a>
  </div>
  ```
- [x] `church-history/index.html`: Add a `← See Biblical Timeline` link in `.tl2-sub` subtitle
  area below the `<h1>`
- [x] `timeline.css`: `.tl-detail-crossover { margin-top:.85rem; padding:.6rem .8rem; border-radius:7px; background:color-mix(in srgb,#2d6e9e 7%,transparent); border:1px solid color-mix(in srgb,#2d6e9e 20%,transparent); }`
  `.tl-detail-crossover__label { font-size:.68rem; font-weight:700; text-transform:uppercase; letter-spacing:.06em; color:#2d6e9e; display:block; margin-bottom:.2rem; }`
  `.tl-detail-crossover__link { font-size:.84rem; font-weight:600; color:#2d6e9e; text-decoration:none; }`

---

### TLU-E · Library Document Links in Church History Detail *(HIGH)*

14 church history events have direct matches to library documents that already exist on the
site. The detail panel never surfaces them despite Augustine, Luther, Calvin, Anselm, and
others having their primary works in the library.

**Hardcoded event → library document map:**

| Event ID | Library doc IDs to link |
|----------|------------------------|
| `anselm` | `anselm-cur-deus-homo`, `anselm-proslogion` |
| `augustine` | `augustine-confessions`, `augustine-city-of-god`, `augustine-on-trinity`, `augustine-enchiridion` |
| `aquinas` | `aquinas-summa-part-i` |
| `luther-95-theses` | `luther-95-theses`, `luther-freedom-christian`, `luther-bondage-of-will` |
| `calvin-geneva` | `calvin-institutes-vol1` |
| `westminster` | `westminster-confession`, `westminster-shorter-catechism` |
| `nicaea-i` | `nicene-creed`, `nicaea-i` |
| `chalcedon` | `chalcedon-451` |
| `benedictine-rule` | `benedict-rule` |

- [x] `timeline.js`: Add `var CHURCH_LIB_LINKS = { 'anselm': [...], ... }` constant at top of file
  with the map above; each entry is `{ docId, label }` where label is the short title
- [x] `timeline.js` (`_buildDetailBody`): For `isChurch`, if `CHURCH_LIB_LINKS[ev.id]` is set,
  append after the legacy section:
  ```html
  <div class="tl-detail-lib-links">
    <span class="tl-detail-maps-label">Read in Library</span>
    <a class="tl-detail-lib-chip" href="../library/?doc={docId}">📖 {label}</a>
    ...
  </div>
  ```
- [x] `timeline.css`: `.tl-detail-lib-links` — same layout as `.tl-detail-maps`;
  `.tl-detail-lib-chip` — same pill style as `.tl-detail-map-chip` but teal border `#2a6b6b`

---

### TLU-F · Populate `key_texts` with Historical Document Refs *(MEDIUM — data)*

The `tl-detail-verse-ref--doc` CSS class was written to render document titles as distinct
non-Bible chips in the `key_texts` array. The detection logic (`isRef` check in `timeline.js`)
works. But every `key_texts` entry in the data is a Bible reference — the document-chip code
path has never fired. The documents that defined each event should appear here.

- [x] `data/timeline/church-detail.json` — add document-title entries to `key_texts`:
  - `nicaea-i`: `{ "ref": "Nicene Creed (AD 325)", "note": "Affirmed Christ as homoousios — 'of the same substance' as the Father; settled the Arian controversy" }`
  - `chalcedon`: `{ "ref": "Definition of Chalcedon (AD 451)", "note": "Two natures, one person — resolved Eutychianism and Nestorianism" }`
  - `westminster`: `{ "ref": "Westminster Confession of Faith (1646)", "note": "The most comprehensive Reformed confession; became the standard for Presbyterian and many Baptist churches" }`
  - `luther-95-theses`: `{ "ref": "95 Theses (1517)", "note": "Luther's challenge to indulgence sales; the spark that ignited the Reformation" }`
  - `diet-of-worms`: `{ "ref": "Edict of Worms (1521)", "note": "Declared Luther an outlaw; his refusal to recant became the defining moment of Protestant defiance" }`
  - `council-orange`: `{ "ref": "Canons of Orange (AD 529)", "note": "Settled the Semi-Pelagian controversy, affirming Augustinian grace against human merit in salvation" }`
  - `benedictine-rule`: `{ "ref": "Rule of St. Benedict (c. AD 530)", "note": "72 chapters governing monastic life; shaped Western monasticism for 15 centuries" }`

---

### TLU-G · Era Event-Count Badges and Extrabiblical Indicator *(MEDIUM)*

**Event-count badges:** Era nodes give no hint of depth. "The Monarchy" has 15 events;
"Between the Testaments" has 5. A count badge sets expectations before clicking.

- [x] `timeline.js` (`_makeEraNode`): Count `_data.events.filter(e => e.era===era.id).length`;
  append `<span class="tl2-node-count">{count}</span>` inside `.tl2-node-text`
- [x] `timeline.css`: `.tl2-node-count { font-size:.58rem; color:var(--color-muted); background:var(--color-border); border-radius:8px; padding:.03rem .35rem; margin-top:.1rem; align-self:flex-start; font-family:var(--font-ui); font-weight:600; line-height:1.4 }`

**Extrabiblical indicator (biblical timeline only):** 42/92 events have archaeological evidence
but the event node gives no visual signal before clicking.

- [x] `timeline.js` (`_makeEventNode`): After `_detailCache` is loaded (update already-rendered
  nodes in a post-load pass), if `_detailCache[ev.id]?.extrabiblical` exists, append
  `<span class="tl2-ev-arch" title="Extrabiblical evidence">⛏</span>` to `.tl2-node-text`
- [x] `timeline.css`: `.tl2-ev-arch { font-size:.6rem; opacity:.55; margin-left:.1rem }`

---

### TLU-H · Fix the Consummation Event (`yearNum` Hack) *(MEDIUM)*

`yearNum: 9999` distorts the entire biblical spine. The proportional positioning algorithm
scales –4004 to 9999 (a ~14,000-year range), compressing all AD-era events into the bottom 1%
of the spine height. The Consummation should be pinned at the bottom regardless of year math.

- [x] `timeline.js` (`_proportionalPositions`): Filter out items with `yearNum >= 9000` before
  computing positions; return the pinned items at a fixed `95%` position
- [x] `data/timeline/events.json` (`new-creation`): Change `"yearNum": 9999` to `"yearNum": null`
  and add `"yearDisplay": "The Age to Come"` so the year chip reads meaningfully
- [x] `timeline.js` (`_renderEventSpine`, `_renderEraSpine`): Treat `yearNum === null` as the
  pin-to-bottom sentinel; position these nodes at `95%`

---

### TLU-I · Quick Search Across Eras *(MEDIUM)*

With 138 events total across both timelines, finding an event without knowing its era requires
browsing every column. A search input filters by `label + desc` across all eras.

- [x] `timeline/index.html`, `church-history/index.html`: Add
  `<input class="tl2-search" type="search" placeholder="Search events…" />` above `#tl2-eras-spine`
- [x] `timeline.js` (`_makeController`): Wire `input` event on `.tl2-search` to `_handleSearch(q)`:
  - Empty query: restore normal mode (hide events column results, re-enable era nodes)
  - Non-empty: filter `_data.events` by `label + desc` containing `q`; render matching events
    in the events column regardless of era (each node shows its era color dot); dim
    non-matching era nodes with `.tl2-era-node--dim`
- [x] `timeline.css`: `.tl2-search { width:calc(100% - 1.2rem); margin:.5rem .6rem .3rem; font-size:.82rem; padding:.3rem .55rem; border:1px solid var(--color-border); border-radius:5px; background:var(--color-bg); color:var(--color-text); display:block; box-sizing:border-box; }`
  `.tl2-search:focus { outline:none; border-color:var(--color-primary); }`
  `.tl2-era-node--dim { opacity:.3; pointer-events:none; }`

---

### TLU-J · Mobile: Sticky Context Breadcrumb *(LOW)*

On mobile (stacked layout), after selecting an event and scrolling to the detail panel the
era and events columns are off-screen — no context about what is being read.

- [x] `timeline.js` (`_buildDetailShell`): Add
  `<div class="tl-detail-breadcrumb"><span style="color:{era.color}">{era.label}</span> › {ev.label}</div>`
  as the first child of `.tl-detail-inner`
- [x] `timeline.css`: `.tl-detail-breadcrumb { display:none; }`
  `@media(max-width:820px){ .tl-detail-breadcrumb { display:flex; align-items:center; gap:.3rem; font-size:.73rem; padding:.4rem .8rem; border-bottom:1px solid var(--color-border); background:var(--color-surface-subtle); font-weight:600; } }`

---

### TLU-K · Remove `target="_blank"` from In-Site Links *(LOW)*

Related Maps chips and the "Open in Reader" footer link both open in a new tab. Same-site
navigation should stay in the same tab; tabs are for external links.

- [x] `timeline.js` (`_buildDetailBody`): Remove `target="_blank" rel="noopener"` from
  `.tl-detail-map-chip` anchors and the `.tl-detail-ref-link` anchor

---

### Hollow Section Audit & Cleanup — 2026-06-03

5-agent parallel audit of all 103 library HTML docs for sections containing only
a heading stub with no paragraph content (structural dividers, TOC entries,
Roman-numeral separators, empty NOTE headers, etc.).

- [x] **53 hollow sections removed** via `scripts/strip-hollow-sections.py` across 10 files:
  baxter-reformed-pastor (4), taylor-holy-living (10), newman-apologia (19),
  meister-eckhart-sermons (5), luther-bondage-of-will (5), pseudo-dionysius-works (3),
  catherine-dialogue (2), shepherd-of-hermas (1), origen-de-principiis (1 — empty "Book III." stub),
  gregory-great-pastoral-rule (3 — TOC-only Part I/II/III stubs)
- [x] **10 more hollow sections removed** in second pass:
  william-law-serious-call (3 title fragments), vincent-of-lerins-commonitory (Contents),
  francis-de-sales-devout-life (2), benedict-rule (1), bernard-on-loving-god (1),
  murray-lord-teach-us-to-pray (1), murray-ministry-of-intercession (1)
- [x] Search index rebuilt: 2540 entries, 142 docs
- [x] Validation: 100/103 PASS (same 3 pre-existing failures: athenagoras, bunyan-holy-war, edwards-affections)

---

### Library Format Standard v2 — 2026-06-03

Formal standard and updated tooling defined after reviewing all 103 docs + prior cleanup history.

- [x] **`data/library/LIBRARY_FORMAT.md`** — canonical v2 format spec covering: allowed block/inline elements, tolerated wst-* classes (styled in library.css), disallowed source chrome by source type (MediaWiki, CCEL, Gutenberg, TEI), content completeness requirements, 8-step sourcing workflow
- [x] **`scripts/validate-library-format.py`** updated to v2:
  - R11 — hollow sections (no `<p>`, text <600 chars) → FAIL
  - R12 — near-empty documents (<1,000 words total) → FAIL
  - W-BR, W-HR, W-PAGE, W-CHROME, W-AUTO → WARN level (use `--warn` flag)
  - Old R9/R10 demoted to W9/W10 (warnings, not failures)
- [x] **`scripts/clean-library-html.py --mode artifacts`** added — strips across all 103 docs:
  dropinitial* decorative spans, smcap/sc/smc→smallcaps conversion, pageno/pb/pgmark page markers,
  tei-noteref spans, NoteRef/Note/Footnote/mnote CCEL footnote chrome, auto-generated class names
  (c007, c014, i2…), default paragraph classes (Normal, Default, Body), `<hr>` elements.
  47 docs modified.
- [x] Final validation: **99 PASS, 4 FAIL, 24 WARN-only**
  - 4 FAILs are all genuine missing-content cases (see re-sourcing list below)
  - 24 WARNs are almost entirely W-BR: `<br>`-as-paragraph-break from source HTML — requires per-doc judgment, not automated

**Five docs re-sourced from Wikisource (NPNF) — 2026-06-03:**

- [x] **`julian-revelations.html`** — 86 chapters fetched, grouped into 13 sections by revelation; 54,210 words. `scripts/fetch-julian.py`
- [x] **`cassian-conferences.html`** — 492 chapters across 24 conferences fetched; 25 sections (Preface + 24 conferences); 215,257 words. Conferences XII and XXII absent from NPNF edition (noted as not translated). `scripts/fetch-cassian.py`
- [x] **`gregory-great-pastoral-rule.html`** — Parts I–III fetched (12 + 11 + 41 sub-pages); 4 sections; 67,578 words. `scripts/fetch-gregory.py`
- [x] **`vincent-of-lerins-commonitory.html`** — 33 chapters fetched, grouped into 8 sections; 19,845 words. `scripts/fetch-vincent.py`
- [x] **`augustine-enchiridion.html`** — 122 chapters fetched, grouped into 6 doctrinal sections; 49,723 words. `scripts/fetch-enchiridion.py`

All 5 pass `validate-library-format.py`. **103/103 PASS — zero failures.** Search index rebuilt: 2,550 entries.

---

### RD-D · Commentary Panel — Full Chapter Coverage *(superseded by RD-M — skip)*

The verse-locked split view in RD-M surfaces per-verse commentary directly inline, making this side-panel "show more" approach unnecessary. Do not implement RD-D; implement RD-M instead.

- [~] ~~`reader.js` (`_loadReaderCommentary`): "Show more" button for partial-verse commentary~~ — superseded
- [~] ~~Count hint for single-verse lookups~~ — superseded

---

### REF-A · Smith's Verse-Index *(CRITICAL — zero new content, immediate impact)*

Smith's Bible Dictionary (4,561 entries) is already committed at `data/smith/` but has no
verse-index, so it never appears in the verse modal's Dictionary tab or in the Verse Study
Dictionary section. Building the index is a single script run.

The index builder for Easton already exists at `scripts/build-dict-verse-index.py` and
reads `refs` from each entry JSON. Smith entries use the exact same schema
(`{ id, term, source, html, refs }`). The script should handle Smith with a `--source smith`
flag (or just be extended to process both sources in one pass).

- [x] `scripts/build-dict-verse-index.py`: Extended with `--source` flag; Smith extracts refs from HTML patterns; handles Unicode replacement char and Song of Songs alias
- [x] Run: `python3 scripts/build-dict-verse-index.py --source smith` -- 65 books, 8823 verse entries to `data/smith/verse-index/`
- [x] `assets/js/library.js`: Smith verse-index lookup wired in `_dictEntriesForVerse` (`_smithLoadVidx`, dedup by `smith:` key prefix) — load `data/smith/verse-index/{bookId}.json` using the same cache/fetch pattern; merge and deduplicate the results from both sources before returning
- [x] `assets/js/library.js` (`renderModalDictionary`, `renderVSDictionary`): E/S badges and `?src=smith` routing already implemented (e.g. `"S"`) so the user can tell which dictionary each term came from when results are mixed; Easton entries show `"E"`

---

### MAP-A · Timelapse: Event List Click-to-Seek *(HIGH — quick win)*

Clicking an event in the left event column should jump the time-lapse to that event's `t`
value. Currently the slider must be scrubbed manually.

**Implementation:** In `timelapse-map.js` `_buildEventList()`, attach a click handler to each
`.tl-ev-item` that sets `_time` to the event's `t`, calls `_render(_time)`, and updates the
slider value. Also stop playback if currently playing.

- [x] `timelapse-map.js` (`_buildEventList`): on `.tl-ev-item` click → set `_time = ev.t`,
  `_playing = false`, update `#tl-play` button label, set `#tl-slider` value, call `_render(_time)`
  *(already implemented at line 752)*

---

### MAP-B · Timelapse: Event List Search/Filter *(MEDIUM)*

With 88 events across 8 eras, a text filter above the event list would let users jump to
"Paul" or "Babylon" without scrolling.

**Implementation:** Add a small `<input>` inside `.tl-event-col` header area. On `input` event,
hide `.tl-ev-item` entries whose text doesn't match. Show era group labels only when at least
one child item is visible.

- [x] `maps/timelapse/index.html`: Add `<input class="tl-event-search" placeholder="Filter…">`
  inside `.tl-event-col` between the header and the list
- [x] `timelapse.css`: Style `.tl-event-search` — full width, small, no border-radius excess,
  consistent with panel aesthetic
- [x] `timelapse-map.js`: `_wireEventSearch()` — wires input's `input` event to filter
  `.tl-ev-item` visibility by text content

---

### MAP-C · Cross-Link the Two Systems *(HIGH)*

Neither system links to the other contextually. A user studying the Conquest static map has no
path to the timelapse Conquest era, and vice versa.

**Static maps → timelapse:** Each map entry in `MAPS[]` should have an optional `tlTime`
field — the timelapse `t` value corresponding to the center of that era. The detail panel
header (or a small chip near the title) shows "⏱ Time-Lapse" linking to
`timelapse/#t=<value>`.

**Timelapse → static maps:** The info panel should show a "Detailed map →" link when the
current era has a matching static map, using the same `#<map-id>` hash used by the static
maps page.

Era → map ID mapping (for reference):
| Era | `t` range | Static map id(s) |
|-----|-----------|-----------------|
| The Patriarchs | 0–145 | `patriarchal-journeys`, `ancient-near-east` |
| Moses & Exodus | 280–361 | `exodus` |
| Conquest & Judges | 341–500 | `conquest`, `twelve-tribes`, `judges` |
| The Monarchy | 500–720 | `david-kingdom`, `solomon-kingdom`, `divided-kingdom` |
| Exile & Return | 677–820 | `invasions`, `return-exile` |
| Life of Christ | 980–1046 | `holy-land` |
| The Early Church | 1040–1080 | `paul-journeys`, `seven-churches` |

- [x] `maps.js`: `MAP_TL_TIMES` const — t-values for all 15 maps; `_selectMap()` renders
  `#maps-tl-chip` link (`timelapse/#t=<n>`) from this table
- [x] `maps/index.html`: Added `<a id="maps-tl-chip" class="maps-tl-chip" hidden>` in panel header
- [x] `maps.css`: `.maps-tl-chip` pill style — matches header link aesthetic at smaller size
- [x] `timelapse-map.js` (`initTimelapsePage`): Hash `#t=<n>` parsed after `_render(0)`;
  calls `_seekTo(n)` to land at the linked time position
- [x] `timelapse-map.js` (`_renderInfo`): `ERA_TO_MAP` table; `#tl-map-link` updated on each
  era change with `../#<mapId>` URL
- [x] `maps/timelapse/index.html`: Added `<a id="tl-map-link" class="tl-map-link" hidden>` in info panel
- [x] `timelapse.css`: `.tl-map-link` pill style

---

### MAP-D · Intertestamental Map *(HIGH — content gap)*

The 500-year gap between "Return from Exile" (c. 400 BC) and "Holy Land (NT)" (c. AD 27) is
completely absent from both systems. This covers: Alexander's conquest (333 BC), the Ptolemaic
and Seleucid division, Antiochus IV Epiphanes and the Maccabean revolt (167 BC), the Hasmonean
kingdom, and Pompey's Roman takeover (63 BC).

**Add to `MAPS[]`** in the "New Testament" group (or a new "Intertestamental" group before it):

```
id: 'intertestamental'
label: 'Intertestamental'
icon: '🏛'
title: 'Between the Testaments'
sub: 'Alexander, the Maccabees, and Rome — 400–4 BC'
```

Routes to draw:
- Alexander's conquest march (333 BC): Macedonia → Troy → Issus → Tyre → Egypt → Babylon
- Maccabean revolt base (167–164 BC): Modein → Gophna Hills → Jerusalem
- Pompey's campaign (63 BC): Damascus → Jerusalem

Region overlays:
- Ptolemaic Egypt (south, 323–200 BC)
- Seleucid Empire (north, 323–63 BC)
- Hasmonean kingdom (165–63 BC, centered on Judea)

Key cities: Alexandria, Antioch (Seleucid capital), Modein (Maccabean hometown), Jerusalem,
Jericho, Ptolemais, Tyre, Sidon, Damascus, Babylon, Gaza

Overview text should cover: the 400 years of silence, Greek cultural pressure (Hellenism),
Antiochus IV's desecration of the Temple (the "abomination of desolation" Jesus references
in Matthew 24:15), Judas Maccabeus's victory, Hanukkah, the Hasmonean priestly-kings, and
Pompey's entry into the Holy of Holies — setting the stage for Herod and the NT world.

- [x] `maps.js`: `intertestamental` entry added to `MAPS[]` with full 4-paragraph overview,
  legend, and `_renderIntertestamental()` — Alexander route, Maccabean route, Pompey route,
  4 region overlays, 10 city markers with `desc`/`significance`/`refs`
- [x] `maps.js` (`GROUPS`): New "Intertestamental" group added between "Exile & Return" and "New Testament"

---

### MAP-E · Jerusalem City Map *(MEDIUM)*

Jerusalem appears as a single dot in every map but is the most-clicked city in the system.
A dedicated zoom-level-14 map would show: Temple Mount, Antonia Fortress, Gethsemane, Golgotha
(Gordon's Calvary / Church of Holy Sepulchre), Pool of Siloam, Pool of Bethesda, City of
David, Kidron Valley, Hinnom Valley, Herod's Palace, the major gates.

This map should default to a higher zoom (14–15) centered on `[31.7767, 35.2345]`.

The overview text covers Jerusalem's theological significance across the whole Bible:
Melchizedek's Salem → Moriah → David's capture → Solomon's Temple → destruction → return →
Second Temple → Christ's entry, crucifixion, resurrection → Pentecost → New Jerusalem (Rev 21).

- [x] `maps.js`: `jerusalem` entry added to `MAPS[]` — zoom 14, center [31.7767, 35.2345],
  4-paragraph overview (Salem → Moriah → Temple → Passion → Pentecost → AD 70 → New Jerusalem),
  `_renderJerusalem()` with city-wall polygon, Temple Mount polygon, 13 site markers with full
  `desc`/`significance`/`refs`
- [x] `maps.js` (`GROUPS`): New "The Holy City" group at the very top of the nav sidebar
- [x] `maps.js` (`_showCityDetail`): Auto-inserts `.maps-city-map-chip` link whenever
  `city.name === 'Jerusalem'` in any map — navigates to Jerusalem map via `_selectMap()`
- [x] `maps.css`: `.maps-city-map-chip` pill style

---

### MAP-G · Site Index + Sequential Navigation *(HIGH — study tool)*

The detail panel has no inventory of a map's sites. Users discover them only by clicking around.

Two-tab layout: **Overview | Sites (N)** — Sites tab shows every named marker in a scrollable
list with a filter input; clicking any entry flies to the marker and opens city detail.
City detail gets a `← N/Total →` nav bar for stepping through all sites in narrative order.

- [x] `maps/index.html`: `.maps-panel-tabs` bar; `#maps-site-index` (search + list); `.maps-city-nav`
- [x] `maps.css`: tab bar, site list, site search, city nav button styles
- [x] `maps.js`: `_markerIndex`/`_currentSiteIdx`; `_cityMarker` push; `_clearOverlays` clear;
  `_buildSiteList`; `_setTab`; `_wireTabs`; `_wireSiteNav`; `_wireSiteSearch`; `_stepSite`;
  wired in `_selectMap`, `_showCityDetail`, `initMapsPage`

---

### MAP-H · Per-Site Study Notes *(MEDIUM — localStorage)*

"📝 Notes" button in city detail expands a textarea; persists to localStorage keyed by
`bsw_map_note_${mapId}_${cityName}`. Sites with notes get a small dot on their marker.

- [x] `maps.js` (`_showCityDetail`): notes textarea appended to city detail; auto-expands if
  a note exists; saves on blur; `_refreshMarkerNote` updates marker dot
- [x] `maps.js`: `_applyExistingNotes()` — called from `_buildSiteList()`; decorates all
  markers with saved notes on initial map load
- [x] `maps.css`: `.maps-city-notes-wrap/btn/textarea`, `.maps-marker-has-note::after`
  amber dot indicator

---

### MAP-I · Scripture Refs Index *(MEDIUM — study tool)*

Third panel tab "Refs" — collects every `refs[]` entry from all cities in the current map,
deduplicates, sorts by canonical Bible order, renders as clickable chips opening verse preview.

- [x] `maps.js`: `_buildRefsIndex()` — deduplicates all `refs[]` from `_markerIndex`, sorts by
  `_BOOK_ORDER` (canonical Bible order), groups by book, renders `.maps-refs-chip` anchors
  wired via `wireRefLinks` for hover-preview + modal; count line "N refs across M books"
- [x] `maps/index.html`: "Refs" third tab; `#maps-refs-index` div in panel body
- [x] `maps.css`: `.maps-refs-index`, `.maps-refs-book`, `.maps-refs-chip` styles

---

## Notes

- All content must remain static HTML/CSS/JS — no build step, no server
- **Bible text data committed:** KJV, BSB, WEB, ASV (4 complete versions, 66 books each)
- **Versions to add:** YLT (Young's Literal), Darby Translation, Geneva Bible (1599) — all public domain
- **Cross-ref data source:** OpenBible.info (CC licensed, based on TSK + community)
- **Commentary source:** SWORD Project / e-Sword public domain modules (Matthew Henry, Barnes, JFB, Clarke, Vincent)
- **Interlinear data:** `morphgnt/sblgnt` (Greek, CC-BY 4.0), `openscriptures/morphhb` (Hebrew, CC-BY 4.0)
- **Strong's data:** `openscriptures/strongs`, Dodson Greek Lexicon (CC0), BDB Hebrew Lexicon JSON
- **Library/confessions source:** reformed.org, ccel.org, and similar public domain sources
- **Dictionary source:** ISBE (1915) public domain
- **Timeline/map data:** BibleTimeline.info, OpenBible geography data (public domain)
- **Nave's Topical data:** `openscriptures/nave` on GitHub (public domain)
- **Devotional source:** CCEL.org — Spurgeon's Morning and Evening (public domain)
- All Scripture refs use `.ref[data-ref]` pattern — auto-wired by `bible.js`
- Scripts: `scripts/serve.py` (dev server), `scripts/restart.py` (kill + restart), `scripts/new-topic.sh` (topic scaffold)
- **Upstream data pins** — specific commit hashes for `morphgnt/sblgnt`, `openscriptures/morphhb`, `openscriptures/strongs`, and `openscriptures/nave` are not recorded; see `data/SOURCES.md`

---

## Verse Modal — Mobile Improvements *(archived 2026-06-03)*

### VM-M1 · iOS Auto-zoom on Note Textarea and Tag Input *(HIGH)* — DONE
Added `font-size: 1rem` to `.bsw-note-textarea`, `.bsw-tag-input`, `.bsw-modal__comm-select`
in `@media (max-width: 767px)` block of `bible-ui.css`. Also added `width: auto; min-width: 80px; flex: 1` to `.bsw-tag-input`.

### VM-M2 · Swipe-Down-to-Dismiss Gesture *(HIGH)* — DONE
Added touchstart/touchmove/touchend listeners on `modal` in `buildModalDOM` (modal.js). Gates
on `window.innerWidth <= 767`; translates modal on downward swipe; dismisses when delta > 100px.
`hideModal` now clears `style.transform` and `style.transition` to reset any partial swipe.

### VM-M3 · Word Study Table: Horizontal Overflow on Mobile *(HIGH)* — DONE
Added `@media (max-width: 767px)` CSS switching `.bsw-ws-table` to `display: block` with
2-row card layout per word (lemma+strongs row 1, eng+gloss row 2). Translit hidden.

### VM-M4 · Cross-Ref Footnote Sups: Tap Target Too Small *(MEDIUM)* — DONE
Enlarged `.bsw-modal__xref-note` to 20×18px on mobile with `::after` pseudo-element expanding
the tap zone to ~42px tall (inset: -12px -8px).

### VM-M5 · Share Overlay Close Button: Tap Target Too Small *(LOW)* — DONE
Added `min-width: 44px; min-height: 44px` to `.bsw-share-close` in the mobile media query.


---

## ARCHIVED 2026-06-03 — Verse Modal Improvements (VM-A through VM-J)

## Verse Modal Improvements

Code-reviewed `modal.js` top-to-bottom (1217 lines). Findings below, split by severity.

---

### VM-A · Bug — Copy Includes Inline Footnote Numbers *(HIGH)*

`_copyModalVerse` (line 937) reads `el.textContent` from `.bsw-modal__verse`, which includes
the verse-number `<sup>` **and** any cross-reference `<sup class="bsw-modal__xref-note">`
nodes appended by `_injectModalFootnotes`. The leading digit is stripped by the regex
`/^\s*\d+\s*/`, but trailing footnote numbers (e.g. `"¹²³"` at the end) survive into the
clipboard. Result: `"In the beginning God created…¹²" — Genesis 1:1 (BSB)`.

- [x] `modal.js` (`_copyModalVerse`, line 937): Replace
  ```js
  var t = el.textContent.replace(/^\s*\d+\s*/, '').trim();
  ```
  with
  ```js
  var textSpan = el.querySelector('.bsw-modal__verse-text');
  var t = textSpan ? textSpan.textContent.trim() : '';
  ```
  This targets only the text span, skipping the verse-number sup and the appended xref sups.

---

### VM-B · Bug — Memory Button Has Wrong CSS Class *(LOW)*

`buildModalDOM` (line 96):
```html
<button class="bsw-modal__memory-btn bsw-modal__compare-link" hidden ...>
```
The memory button carries `bsw-modal__compare-link` — a copy-paste leftover. It may inherit
link-styled padding, colour, or layout rules that belong only on the anchor tags above it.

- [x] `modal.js` (`buildModalDOM`, line 96): Remove `bsw-modal__compare-link` from the
  memory button's class list; leave only `bsw-modal__memory-btn`.

---

### VM-C · Bug — Notes Badge Misses Ranged Lookups *(MEDIUM)*

`_refreshModalNotesBadge` (line 635):
```js
var count = getNotesForVerse(parsed.bookId, parsed.ch, parsed.v).length;
```
For a verse range (`Romans 8:1-11`), this only queries `parsed.v` (verse 1). Notes on verses
2–11 are invisible in the badge, even though `_renderNotesPanel` correctly displays all of
them. The badge reads "0" while the panel shows multiple notes.

- [x] `modal.js` (`_refreshModalNotesBadge`, line 635): When `parsed.endV && parsed.endV !== parsed.v`,
  loop `v` from `parsed.v` to `parsed.endV` (same chapter) and sum counts:
  ```js
  var count = 0;
  var endV = (parsed.endV && parsed.endCh === parsed.ch) ? parsed.endV : parsed.v;
  for (var vi = parsed.v; vi <= endV; vi++) {
    count += getNotesForVerse(parsed.bookId, parsed.ch, vi).length;
  }
  ```

---

### VM-D · UX — Version Picker Shows IDs, Not Names *(MEDIUM)*

`syncModalVersionPicker` (line 233): `opt.textContent = v.id` — the dropdown labels are
abbreviations (`BSB`, `KJV`, `WEB`). The full name is only in `opt.title`, which browsers
don't show inside `<select>` options on most platforms. First-time users have no idea what
`ASV` or `WEB` mean.

- [x] `modal.js` (`syncModalVersionPicker`, line 233): Change
  `opt.textContent = v.id;`
  to
  `opt.textContent = v.id + ' — ' + v.name;`
  so each option reads e.g. `BSB — Berean Standard Bible`. Keep `v.id` as the option value
  so downstream code that reads `versionSel.value` is unaffected.

---

### VM-E · UX — Copy Format Cycles Silently *(MEDIUM)*

`_copyModalVerse` cycles between "full quote" and "citation-only" formats on successive
clicks (line 946: `btn._copyFmt = fmt === 'plain' ? 'cite' : 'plain'`). The user has no way
to tell which format the *next* click will copy — the label only changes *after* clicking.
There is no tooltip, title, or pre-click indicator.

Two cleaner approaches:
- **Option A:** Add a small `<select>` or toggle chip beside the Copy button with labels
  `Quote` / `Reference` — explicit, one-click copy.
- **Option B:** Keep single Copy button but add `title` attribute that updates to say what
  the *next* click will do: `"Next click copies: citation only"`.

- [x] `modal.js` (`buildModalDOM`): Add a `<select class="bsw-modal__copy-fmt-sel">` next to
  the copy button with two options: `value="plain" Quote` and `value="cite" Reference`;
  default `plain`; no more cycling logic.
- [x] `modal.js` (`_copyModalVerse`): Read format from the select instead of `btn._copyFmt`;
  remove the cycle toggle; keep the "Copied!" / "Cite copied!" flash.
- [x] `assets/css/bible-ui.css`: Style `.bsw-modal__copy-fmt-sel` — small, inline, no border
  radius excess; matches the version picker's compact style.

---

### VM-F · UX — Last-Used Tab Not Remembered Within Session *(LOW)*

Every `renderModal()` call resets to the Verse tab (lines 270–274). If a user opens
Commentary for John 3:16, closes the modal, then clicks John 3:17, they land on Verse again
and must re-click Commentary. Remembering the last tab within the session avoids this.

- [x] `modal.js`: Add a module-level `var _lastTab = 'verse';`
- [x] `modal.js` (tab click handler, line 176): After reading `var tab = btn.getAttribute('data-tab');`,
  store `_lastTab = tab;`
- [x] `modal.js` (`renderModal`, after resetting tabs to Verse): After the reset block,
  if `_lastTab !== 'verse'`, find the matching tab button and trigger a synthetic click
  (or directly show its panel) — **only** if the tab has already been loaded for the previous
  reference (i.e. the panel's `_loaded` flag is still true). Do not re-render stale content;
  only restore the tab if the panel is about to be re-used for the *same* verse. For a new
  verse, always start fresh on Verse tab but remember which tab to activate after load.

  Simpler approach: just save `_lastTab` and apply it unconditionally — the lazy-load on
  tab activation will fetch fresh data automatically for the new verse.

---

### VM-G · UX — Cross-Refs Tab: Multi-Verse Previews Lack Verse Numbers *(LOW)*

`renderModalCrossRefsTab` (line 581):
```js
textEl.textContent = verses.map(function (vr) { return vr.text; }).join(' ');
```
When a cross-reference covers multiple verses (e.g. `Isaiah 53:4-6`), the three verse texts
are concatenated with no numbering, making it impossible to see where one verse ends and the
next begins. Cross-refs that point to a single verse are fine.

- [x] `modal.js` (`renderModalCrossRefsTab`, line 581): For single-verse cross-refs, keep as-is.
  For multi-verse results, prefix each text with the verse number:
  ```js
  textEl.textContent = verses.length === 1
    ? verses[0].text
    : verses.map(function (vr) { return vr.verse + ' ' + vr.text; }).join(' ');
  ```

---

### VM-H · UX — Commentary Shows No "Nearest Section" Notice *(MEDIUM)*

`_extractCommHtml` (lines 614–625) finds the nearest preceding commentary key when the
requested verse has no exact entry (e.g., requesting v.16 when commentary sections are at
v.1, v.9, v.20). The user sees Matthew Henry on v.16 but the text actually covers v.9–19.
There is no indication that the content is a section that *includes* the verse, not an exact
match. This misleads users into thinking the commentary specifically addresses their verse.

- [x] `modal.js` (`_extractCommHtml`): Return the `foundV` alongside the html:
  `return { html, foundV }` instead of bare string.
- [x] `modal.js` (`renderCommentary`, `loadAndRender`): After inserting the html, if
  `foundV !== null && foundV !== parsed.v`, prepend a muted note:
  ```html
  <p class="bsw-modal__comm-section-note">
    ▸ This section covers verse {foundV} and following
  </p>
  ```
- [x] `assets/css/bible-ui.css`: `.bsw-modal__comm-section-note` — `font-size:.72rem;
  color:var(--color-muted); margin:0 0 .5rem; font-style:italic;`

---

### VM-I · Feature — Prev/Next Verse Navigation in Modal *(HIGH)*

Once the modal is open there is no way to move to an adjacent verse without closing and
clicking a new reference. The verse-study page has `j`/`k` navigation but the modal doesn't.
This is the highest-friction gap for sequential verse study.

- [x] `modal.js` (`buildModalDOM`): Add two navigation buttons to `.bsw-modal__header`:
  ```html
  <button class="bsw-modal__prev-verse" aria-label="Previous verse" title="Previous verse (k)">‹</button>
  <button class="bsw-modal__next-verse" aria-label="Next verse" title="Next verse (j)">›</button>
  ```
  Visible only when a single verse is open (`isSingleVerse`); hidden for chapter views and
  ranges (same condition as the Memorize button).
- [x] `modal.js` (`renderModal`): After computing `isSingleVerse`, show/hide the nav buttons
  and set their `_parsedRef` to the adjacent verse (previous: same chapter v−1 with book
  wrap; next: same chapter v+1 with chapter wrap — use `metaBooks` for chapter/verse limits).
  For simplicity in a first pass: only navigate within the same chapter; grey out at chapter
  boundaries.
- [x] `modal.js` (`buildModalDOM`): Wire prev/next button clicks to `openModal(adjacentParsed)`.
- [x] `modal.js` (keydown handler, line 165): When modal is open and the key is `j`/`ArrowRight`,
  fire next-verse; `k`/`ArrowLeft` fires prev-verse — only when `isSingleVerse` and focus is
  not in a textarea or input.
- [x] `assets/css/bible-ui.css`: `.bsw-modal__prev-verse`, `.bsw-modal__next-verse` — same
  style as `.bsw-modal__close` but smaller; placed left of the title or flanking it.

---

### VM-J · Feature — Web Share API for Mobile *(MEDIUM)*

`_shareVerseAsImage` (line 1040) only offers PNG download. On mobile, this requires the user
to find the downloaded file and share it manually. The Web Share API (`navigator.share()`)
allows sharing directly to WhatsApp, iMessage, etc. from within the browser — one tap instead
of three steps.

- [x] `modal.js` (`_shareOverlayEl` download handler, line 1088): After building the download
  anchor, also check `navigator.share && navigator.canShare`:
  ```js
  if (navigator.share) {
    canvas.toBlob(function (blob) {
      var file = new File([blob], 'verse.png', { type: 'image/png' });
      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        navigator.share({ files: [file], title: refDisplay });
      } else {
        a.click(); // fallback to download
      }
    }, 'image/png');
  } else {
    a.click();
  }
  ```
- [x] `modal.js` (`_shareVerseAsImage` UI builder, line 1074): Change the download button
  label: show `⬆ Share` if `navigator.share` is available, `⬇ Download PNG` otherwise
  (detect once, set label in the innerHTML).



---

## Verse Study Page Improvements — VS-A through VS-H (completed 2026-06-03)

### VS-A · Prev/Next Verse Navigation *(HIGH)* ✓
- Added `‹` / `›` nav links flanking `#vs-header-ref` in topbar
- `loadVerseStudyVerse` updates hrefs using `VERSE_STUDY_URL` + adjacent verse from loaded `chData`
- CSS `.vs-adj-link` added

### VS-B · Sidebar Nav — Active Section Scroll-Spy *(MEDIUM)* ✓
- `_vsNavObserver` module var; `vsRebuildNav` disconnects and rebuilds IntersectionObserver each time
- Buttons get `dataset.sectionId = sec.id`; observer highlights matching nav button on intersection

### VS-C · Section Collapse/Expand *(MEDIUM)* ✓
- `vsCreateSection` appends `▾/▸` toggle button to each heading; body gets `hidden` toggled on click
- `.vs-section-heading` gains `display:flex; justify-content:space-between`; `.vs-section-toggle` styled

### VS-D · All Translations — Lazy Load + Diff Highlighting *(MEDIUM)* ✓
- `cmpObserver` defers `vsRenderVersionCompare` until section scrolls into view (threshold 0.05)
- `applyHighlights` called on each row after text resolves; mark styles added for light/dark

### VS-E · Copy Verse Button *(LOW)* ✓
- `#vs-copy-btn` added to header actions; wired in `loadVerseStudyVerse` with 1.8s "Copied ✓" feedback

### VS-F · Word Study Flyout — Full Definition Expand *(LOW)* ✓
- Definitions >300 chars get a "more…" button that unhides the `.vs-wp-def-rest` span

### VS-G · Commentary Long-Entry Truncation *(LOW)* ✓
- Commentary body >800 chars wrapped in `.vs-comm-truncated--clamped` (max-height 14em); "Read more ▾" expands

### VS-H · Header Height Fix *(LOW)* ✓
- `requestAnimationFrame` measures header height before `loadVerseStudyVerse` so `--vs-header-h` is correct from first paint

---

## Word Study Page Improvements — WD-A through WD-K (completed 2026-06-03)

### WD-A · Loading Progress for Bulk Interlinear Fetch *(HIGH)* ✓
- Progress `<p id="wd-progress">` inserted before stats; shows "Loading books… N / T"; removed on completion
- `.wd-progress` style in word.css

### WD-B · Filter State in URL Hash *(HIGH)* ✓
- `_wdWriteHash()` / `_wdReadHash()` helpers; both filters written to `location.hash` on every toggle
- Hash restored before first render; `hashchange` listener re-applies filters on browser Back/Forward

### WD-C · Morphological Form Breakdown *(HIGH)* ✓
- `tok.m` codes accumulated into `morphCount` during interlinear scan
- `_wdRenderMorphTable()` expands codes via `expandMorphCode`, sorts descending, renders table between stat cards and body
- Skipped when no morph data (punctuation/particles); `.wd-morph-table` CSS added

### WD-D · Interactivity Discoverability + "All" Reset *(MEDIUM)* ✓
- "All translations" row prepended to translations list; "All" pill prepended to books grid
- `title` attributes on all interactive pills/rows
- "Clear all" button added to filter bar when both filters active (consolidates WD-J)

### WD-E · "Open in Reader" Link per Book Section *(MEDIUM)* ✓
- `.wd-book-reader-link` appended inside each book heading; links to `../read/?book=BOOKID`

### WD-F · Books Sidebar Height Cap *(MEDIUM)* ✓
- `max-height: 160px` → `clamp(160px, 28vh, 260px)` in word.css

### WD-G · Author/Genre Breakdown in Stat Cards *(MEDIUM)* ✓
- `genre` field added to all 66 entries in `data/bible/books.json`
- `_wdRenderStats` appends a flex row of genre chips with occurrence counts

### WD-H · Second Lexical Source (Strong's) in Header *(MEDIUM)* ✓
- Strong's gloss/def rendered as `.wd-lexicon--strongs` with `--color-border` left border (vs. `--color-primary` for Thayer/BDB)
- Collapsible full entry toggle matches existing Thayer/BDB pattern

### WD-I · Keyboard Navigation Through Verse List *(LOW)* ✓
- `keydown` listener: ArrowDown/Up steps `.wd-verse-card` with `.wd-verse-card--focused` highlight
- `b` focuses books sidebar, `t` focuses translations sidebar, `Escape` clears all filters

### WD-J · "Clear All Filters" *(LOW)* ✓ — consolidated into WD-D

### WD-K · Semantic Range Bar Polish *(LOW)* ✓
- Bar height 8px → 12px; border-radius 6px
- Percentage text appended to each count: "love · 42 (38%)"
- "How this word is translated:" label added above list

### WD-L · Related Words Panel *(LOW)* — DATA BLOCKED
- strongs JSON has no `see_also`/`related` field; needs a scripted `deriv`-parsing pass first

### WD-M · LXX Bridge *(LOW)* — DATA BLOCKED
- strongs JSON has no `lxx`/`greek_equiv` field; needs sourcing from openscriptures/strongs dataset

---

## Bible Reader Improvements (2026-06-03)

### RD-B · Browse Bar Overcrowding — View Options Overflow Menu *(HIGH)* ✓
- `initViewToggle()` added to `interlinear.js` — creates `⚙ View` button + absolutely-positioned `.reader-view-popover` wrapped in `.reader-view-wrap`
- `initSplitToggle`, `initWideToggle`, `initSidebarToggle`, `initFontSizeControls` now inject into the popover via `_getViewPopover()`; fall back to browse bar if popover absent
- Inline controls kept: Interlinear, Compare, XrefNotes (Footnotes), BookInfo
- Popover closes on outside click and Escape
- Mobile (≤700px): Interlinear/BookInfo/XrefNotes hidden via CSS; ⚙ View + Compare remain inline
- CSS: `.reader-view-wrap`, `.reader-view-btn`, `.reader-view-popover` + popover item styles added to `reader.css`
- `app.js`: `initViewToggle()` called after `initBookInfoToggle()` and before `initSidebarToggle()`

### RD-G · Cross Refs Panel — Cap on Multi-Chapter Views *(MEDIUM)* ✓
- Extracted `_buildXrefHtml(xdata, parsed)` helper; caps to 1 chapter for whole-chapter views, 2 for verse ranges
- Multi-passage lookups show "Showing cross-refs for {bookName} {ch}" scope note
- `.reader-xref-chips` chip row added for switching between passages; chip clicks reload xrefs via `loadCrossRefs`
- CSS: `.reader-xref-scope-note`, `.reader-xref-chips`, `.reader-xref-chip`, `.reader-xref-chip--active` added

### RD-L · Compare Mode — Per-Verse Row Locking *(HIGH)* ✓
- `injectComparePanel` in `reader.js` rewritten: two flowing panels replaced with a `.reader-compare-grid` CSS grid
- Column headers built via `_buildComparePanelHdr` (unchanged), re-classed as `.reader-compare-col-hdr--a/b`
- Primary cells (`reader-compare-cell--a`) filled immediately from `g.verses`; secondary cells (`reader-compare-cell--b`) show loading indicator
- On `resolveVerses` resolve, secondary cells matched by `data-verse` key (`chapter:verse`) and filled; missing verses show `—`
- `applyHighlights` called on the grid after secondary fills; attribution appended after the grid
- Old `.reader-compare-wrap`, `.reader-compare-panel`, `.reader-compare-panel__hdr` CSS replaced with `.reader-compare-grid`, `.reader-compare-col-hdr`, `.reader-compare-cell` rules
- Mobile (≤600px): stacks to single column; secondary column gets top border accent

---

## Site Navigation Consolidation

### CON-A · History Hub *(completed 2026-06-03)*

- Created `history/index.html` — sticky tab bar with 4 tabs (📜 Biblical Timeline, ⛪ Church History, 🗺 Maps, 🎬 Animated Map); lazy iframe panels (data-src → src on first activation); URL state (`?tab=`) + localStorage (`bsw_history_tab`) persistence; Leaflet resize dispatched via `contentWindow.dispatchEvent(new Event('resize'))` on timelapse iframe load
- `assets/js/main.js`: New **History** nav group added before Reference; church-history removed from Library group; timeline and maps removed from Reference group; `?minimal=1` guard added at top of `buildSidebar()` (returns immediately, skipping all sidebar DOM)
- `assets/css/style.css`: `.hist-back-link` pill-link style added for embedded pages; `.hist-iframe` styles in `history/index.html` inline `<style>`
- `timeline/index.html`, `church-history/index.html`, `maps/index.html`, `maps/timelapse/index.html`: `← History` back-link added to page header, revealed by inline script when `?minimal=1` is present

---

## Word Cloud — Post-Shipping Improvements *(completed 2026-06-03)*

### WC-A · Bug — Acts Missing from Scope Buttons and Genre Bars *(HIGH)*
- `wordcloud.js` SCOPES: Added `{ id: 'acts', label: 'Acts', shape: 'flame', ... }` between gospels and epistles
- `wordcloud.js` `_buildBars`: Added Acts row between Gospels and Epistles

### WC-B · Bug — Font Measurement vs Render Mismatch *(HIGH)*
- `wordcloud.js` `_doRender`: Added `font-family="system-ui, sans-serif"` to every emitted SVG `<text>` element

### WC-C · UX — Legend Doesn't Update Per Scope *(MEDIUM)*
- `wordcloud/index.html`: Added `id="wc-legend-heb"` and `id="wc-legend-grk"` to legend items
- `wordcloud.js`: Added `_updateLegend(langs)` function; called after render with Set of placed word languages

### WC-D · UX — No Resize Handling *(MEDIUM)*
- `wordcloud.js` `initWordCloudPage`: Added `ResizeObserver` on `#wc-svg-wrap`; 100ms debounced re-render on width change > 20px

### WC-E · UX — "Hide Names" Toggle Not Persisted *(LOW)*
- `wordcloud.js` `_wireProperToggle`: Reads `bsw_wc_showProper` from localStorage on init; writes on each toggle

### WC-F · Polish — `wc-detail-translit` Renamed to `wc-detail-testament` *(LOW)*
- `wordcloud/index.html`: Renamed element id/class from `wc-detail-translit` to `wc-detail-testament`
- `wordcloud.js`: Updated `getElementById` reference accordingly

### WC-G · Polish — Context-Aware Back Link from Word Study *(LOW)*
- `wordcloud.js` `_showDetail`: Word link now appends `&from=wordcloud`
- `word.js` `initWordPage`: When `?from=wordcloud` present, back link points to `../wordcloud/` with label `← Word Cloud`

---

## CON-B · Reader Hub — Compare as a Reader Mode, Bookmarks as Right Panel Tab *(HIGH)*

Completed 2026-06-03.

- `read/index.html`: Added `.reader-mode-bar` (Read | ⚖ Compare tabs) above `#reader-results`; `#reader-compare-pane` with lazy iframe pointing to `../compare/?minimal=1`; inline `_activateMode(mode)` script handles tab switching, lazy iframe loading, and URL `?mode=compare` state
- `reader.css`: `.reader-mode-bar`, `.reader-mode-tab`, `.reader-mode-tab--active`, `.reader-mode-iframe` styles added
- `compare/index.html`: Hides `.cmp-nav` breadcrumb when `?minimal=1` present (embedded mode)
- `bookmarks/index.html`: Added `← Reader` back-link; hides Home link when `?minimal=1`
- `reader.js` (`_ensureReaderPanelStructure`): Added "Bookmarks" tab + `#reader-panel-bookmarks` panel body
- `reader.js` (`loadReaderPanelContent`, `_loadPanelTab`): Wired `_loadReaderBookmarks` for bookmarks tab
- `reader.js` (`_loadReaderBookmarks`): Renders `bsw_bookmarks` list with in-page navigation; clicking a ref fires `_readerLookupFn`
- `reader.css`: `.reader-bookmark-list`, `.reader-bookmark-item`, `.reader-bookmark-star`, `.reader-bookmark-ref` styles added

---

## Discipline Section Expansion — D-A through D-K (Completed 2026-06-03)

**D-E:** `progress/index.html` — confirmed `bsw_chapter_read` as canonical storage key; added comment.

**D-F:** `assets/js/main.js` — `?minimal=1` suppression already existed (line 213). `notes/index.html` and `progress/index.html` — added `← Disciplines` back-link shown only when `?minimal=1`; CSS for `.ms-back-link` / `.prog-back-link`.

**D-G:** `discipline/index.html` — wrapped tab bar in `.disc-tabbar-wrap` for sticky positioning; added `More ▾` button (`#disc-more-btn`) after the main tabs; added `.disc-more-menu` dropdown with `📝 My Notes` and `📊 Reading Progress` items; JS toggle/close logic in master IIFE; active tab name reflected in More btn label. `discipline.css` — `.disc-tabbar-wrap`, `.disc-tab--more`, `.disc-more-menu`, `.disc-more-item` styles.

**D-I:** `discipline/index.html` — `initWorship` refactored into `switchWtab(tab, skipUrl)` which persists to `localStorage('bsw_worship_wtab')` and `history.replaceState`; reads `?wtab=` or localStorage on init (default `sermons`); `activateTab` preserves `wtab` param when switching to worship. `main.js` — added `⚡ Fasting Log` → `discipline/?tab=worship&wtab=fasting` nav entry.

**D-J:** `discipline/index.html` — added `#disc-today-strip` div below tab bar; `updateStrip()` in module script renders "Today: N / 7 complete" with colored `.disc-dot--strip` mini-dots; called on init, `onUpdate`, and storage events. `discipline.css` — `.disc-today-strip`, `.disc-strip-label`, `.disc-dot--strip` styles.

**D-K:** `discipline/index.html` — `renderTodaySection` mark-complete handler appends/removes `.disc-cta-link` reflection CTA; `saveSermonEntry` injects `.worship-post-cta` for new entries (cleared after 6s). `discipline.css` — `.disc-cta-link`, `.worship-post-cta` styles.

**D-A:** `discipline/index.html` — added `🙏 Gratitude` tab button; `#disc-gratitude` panel with prompt, new-entry button, search, inline form (date, textarea, tags), entry list (sorted newest-first), export/import; `initGratitude()` IIFE with `bsw_gratitude` storage (`{ id, date, text, tags[] }` schema). `discipline.css` — `#disc-gratitude` layout, `.grat-prompt`, `.grat-bar`. `main.js` — `🙏 Gratitude` → `discipline/?tab=gratitude` added to Discipline nav group.

**D-H:** `tracker.js` — added `isGratitudeDone(date)` (checks `bsw_gratitude`), `isFastingDone(date)` (checks `bsw_fasting` within current Sun–Sat week), and both added to `getToday()` return. `discipline/index.html` — `DOT_COLORS` and `TAB_KEYS` extended with `gratitude`. `index.html` — DISCIPLINES array gets gratitude entry; storage listener watches `bsw_gratitude`, `bsw_reflections`, `bsw_worship`.

**D-B:** `discipline/index.html` — `📝 My Notes` in `.disc-more-menu`; `#disc-notes` panel with lazy iframe (`../notes/?minimal=1`, loaded on first activation); `activateTab` handles `notes`. `main.js` — `📝 My Notes` moved to Discipline group (removed from Reference).

**D-C:** `discipline/index.html` — `📊 Reading Progress` in `.disc-more-menu`; `#disc-progress` panel with lazy iframe (`../progress/?minimal=1`); `activateTab` handles `progress`. `main.js` — `📊 Reading Progress` moved to Discipline group (removed from Reference).

**D-D:** `reader.js` — appended `.reader-mark-row` with `.reader-mark-btn` after bottom chapter nav for whole-chapter views; inline closure reads/writes `bsw_chapter_read` keyed `"{bookId}.{ch}"`; button toggles to `✓ Read` (disabled) on click. `reader.css` — `.reader-mark-row`, `.reader-mark-btn`, `.reader-mark-btn--done` styles.

**CON-D:** `discipline/index.html` — added `📅 History` button to `#disc-more-menu`; added `#disc-history` panel with lazy iframe (`../tracker/?minimal=1`); extended `moreTabs`/`moreLabels` and lazy-load condition to handle `history` tab. `tracker/index.html` — added hidden `← Disciplines` back-link shown when `?minimal=1`. `index.html` — updated "History →" link from `tracker/` to `discipline/?tab=history`. `main.js` — added `discipline` nav group with Discipline Hub + Discipline History children.

**CON-C:** `search/index.html` — renamed to "Explore" (title + h1); added 4 hub tab buttons (Topics, Study Guides, Dictionary, Word Cloud); wrapped search content in `#search-search-panel`; added 4 lazy-load iframe panels. `search.js` — `setSearchTab` extended to handle hub tabs: hides search panel, activates iframe panel, lazy-loads src, writes `?tab=` URL state and `bsw_explore_tab` localStorage; init restores from URL param or localStorage. `topics/index.html`, `study-guides/index.html`, `dictionary/index.html`, `wordcloud/index.html` — each gets `← Explore` back-link + `?minimal=1` show script. `main.js` — "Omni-search" → "Explore" in tools; `reference` group replaced by `explore` group with 5 sub-items linking into the hub.

**SG-A through SG-I (Studies Navigation & UX) — 2026-06-03:** `main.js` — added `📚 Studies` tool link to `NAV.tools`. `studies/index.html` (new) — unified landing page with three sections (Study Guides, Book Studies, Topical Articles) and progress bars for in-progress guides. `data/topics-index.json` — added 5 study guide entries with `href` field; `search.js` `_exploreGuides` fixed to use `g.href` when present so study guides link to `study-guides/` not `topics/`. `assets/js/sg-progress.js` (new) — `markComplete`, `markIncomplete`, `isComplete`, `getProgress`, `initSgProgress`; wires "Mark complete" buttons on `.tg-section` elements and updates `.sg-tab-dot` completion dots on tab nav. `assets/css/study-guide.css` — `.sg-complete-btn`, `.sg-tab-dot` styles. All 5 study guide pages: `study-guide.css` link added (Hebrews was missing), `initSgProgress` wired via module script. `assets/css/topic-guide.css` — `.tg-toc--sticky` (horizontal sticky ToC) applied to 5 long articles; `.tg-breadcrumb` style; `.tg-related` / `.tg-related__link` styles. All 10 topic articles + 5 study guides: `← Studies` breadcrumb added above hero/content. All 15 pages: `<div class="tg-related">` related-studies blocks added per spec. `index.html` — added `#daily-studies-card` with `renderStudiesCard()`; extended `renderLibHistory` to prepend in-progress guide entry.

---

## CON-E · Nav Cleanup — Collapse Reference Group *(completed 2026-06-03)*

All items implemented by prior CON-A/B/C/D and D-B/C/D work; this task verified correctness.

- `assets/js/main.js`: `reference` group removed and replaced with `explore` group (CON-C); no standalone `dictionary/`, `wordcloud/`, `timeline/`, `maps/`, `progress/`, `notes/` nav entries remain — all accessible only via hub tabs
- `assets/js/main.js`: `Omni-search` renamed to `Explore` (CON-C); `history` group added (CON-A)
- Verification pass 2026-06-03: all 12 target standalone URLs (`compare/`, `bookmarks/`, `timeline/`, `church-history/`, `maps/`, `maps/timelapse/`, `dictionary/`, `topics/`, `study-guides/`, `wordcloud/`, `progress/`, `notes/`) confirmed present and each has `?minimal=1` back-link support; all reachable via their respective hub tabs in the nav

---

## Codebase Comment Audit — Completed 2026-06-03

**CMT-A:** `CLAUDE.md` — Added "Code Comments" section with INTENT / CHANGE? / VERIFY format specification and a worked example from `wordcloud.js` (the spiral placement function) showing that INTENT states purpose (not what the code obviously does), CHANGE? names downstream side-effects, and VERIFY describes a runtime browser check.

**CMT-B:** `assets/js/wordcloud.js` — Added INTENT/CHANGE?/VERIFY comments to: `_spiralPlace` (Archimedean spiral formula, adaptive arc-distance step, b=5 radius rationale); the `missStreak` teleport block (why RESTART_AFTER exits narrow arms and jumps to a seedPool pixel); the second-pass rotation retry (why flipping rotation before discard recovers ~10-15% of words); `_buildMask` (offscreen canvas rasterisation, alpha>64 threshold, dimension-keyed cache); `_fitsInMask` (four-corner fast rejection + proportional interior grid sampling).

**CMT-C:** `assets/js/reader.js` — Added INTENT/CHANGE?/VERIFY comments to: `doLookup` (single entry point for all navigation — bypassing it desyncs URL, bsw_history, and right panel); `_navigateChapter` (must use _readerLookupFn not window.location.href — full reload loses right panel and toggle state); `injectComparePanel` (injected into existing DOM so _deactivateCompare removes only the grid, primary text never re-fetches).

**CMT-D:** `assets/js/main.js` — Added INTENT/CHANGE?/VERIFY comments to: `BOOK_STUDIES` / `_readerUpdate` declarations (async population — must not read synchronously at module init; CHANGE? chain through _BOOK_STUDIES exposure and initReaderStudyLink); `loadTopics` subgroup auto-expand block (must run after all appendChild calls complete, hence at end of .then() callback).

**CMT-E:** `assets/js/interlinear.js` — Added INTENT/CHANGE?/VERIFY comment to `initBookInfoToggle` (reads `window._readerNavState.bookName` set by reader.js; undefined on blank load is expected; CHANGE? if _readerNavState shape changes). Note: `_refreshBookInfoPanel` / `_bookInfoCache` were replaced by the RD-I navigation approach; comments applied to current implementation.

**CMT-F:** `assets/js/core.js` — Added INTENT/CHANGE?/VERIFY comments to: `commentaryCache` (keyed by srcId/bookId, never evicted, up to 100 entries per session; CHANGE? invalidate manually if data format changes); `resolveVerses` (whole-book JSON cached on first load via bookCache — subsequent chapter lookups are synchronous; CHANGE? if bible data format changes update both fetch path and verse-object shape consumers).

**CMT-G:** `assets/js/search.js` — Added INTENT/CHANGE?/VERIFY comments to: `_searchGeneration` (increment/guard pattern prevents stale slow-fetch from overwriting fast newer results; CHANGE? all new async sections must capture gen and guard before writing); `_exploreGuides` (must use `g.href` when present — study guides are at `study-guides/` not `topics/`).

**CMT-H:** `assets/js/timelapse-map.js` — Added INTENT/CHANGE?/VERIFY comments to: `_figurePos` (linear lat/lon interpolation; null signals opacity=0; fig.end required to prevent linger into next era); `_animLoop` (RAF loop; _speed * delta; _stopPlay cancels RAF; scrubber writes _time directly so scrubbing is always accurate).

**CMT-I:** `assets/js/timeline.js` — Added INTENT/CHANGE?/VERIFY comments to: `_proportionalPositions` (linear scale over finite yearNum range; yearNum >= 9000 pinned to 95% to prevent scale collapse); `_loadDetail` (single fetch of full detail JSON; _detailProm prevents duplicate concurrent fetches; _detailCache never invalidated — new fields require renderer update).

---

## Bible Reader Improvements — Completed 2026-06-03

**RD-I · Book Intro Duplication:** Already implemented in a prior pass — `initBookInfoToggle` in `interlinear.js:64` navigates to ch=0 via `_readerLookupFn`. No separate `_refreshBookInfoPanel` or `#reader-bookinfo-panel` insertion logic exists in the codebase; the canonical ch=0 path is the sole route.

**RD-M · Commentary Mode — Verse-Locked Split View:** Added full commentary split view to `reader.js`. `initCommModeToggle()` creates the "Commentary" pill button in the browse bar (localStorage state persisted as `bsw_reader_comm_mode`). `_activateCommMode()` prefetches all 7 commentary sources for the current chapter via `Promise.all`, stores `_commModeChData` (keyed by srcId → chapterObj), adds `reader-layout--comm-mode` to hide the xref panel, then calls `_buildCommGrid()`. `_buildCommGrid()` iterates every `.reader-result-group`, extracts `.reader-verse` spans, and replaces `.reader-result-group__text` with a `.reader-comm-grid` of per-verse rows. Each row has a verse cell (20%) and commentary cell (80%) with a per-verse source picker; `_renderCommCell()` finds the nearest-preceding commentary key ≤ v and renders it with a section-span note. `_deactivateCommMode()` clears state, removes the layout class, and re-renders via `_readerLookupFn`. Chapter navigation hook added to `loadReaderPanelContent` to re-activate for new passages. CSS added to `reader.css`: `.reader-comm-toggle`, `.reader-layout--comm-mode`, `.reader-comm-grid`, `.reader-comm-row`, `.reader-comm-cell--verse`, `.reader-comm-cell--comm`, `.reader-comm-src-bar`, `.reader-comm-src-sel`, `.reader-comm-span-note`, `.reader-comm-text`. `initCommModeToggle` exported from `reader.js`, imported and called in `app.js`.

## REF-E · Gill's Exposition — DATA BLOCKED (2026-06-03)

CrossWire SWORD module `Gill.zip` does not exist on CrossWire rawzip (confirmed via full 462-module directory listing) — not in rawzip, not in mods.d. StepBible also 404. CCEL hosts only the Song of Solomon exposition and other non-commentary Gill works, not the 9-volume Bible commentary. The Gill entry has been added to `scripts/fetch-more-commentaries.py` MODULES list so the script is ready to run if a data source is found. Alternative sourcing options: e-Sword SQLite module (requires new parser) or CCEL scraper (if they add the full commentary). Code changes (core.js, SOURCES.md) deferred until data is available.

## Pascal Pensées — Library Fetch + TOC Fix (2026-06-03)

Added Pascal's Pensées (Blaise Pascal, 1670) to the library. Source: Gutenberg #18269 (W.F. Trotter, 1910 translation), 9202 lines, 1921 paragraphs, 20 navigable sections.

**Manifest changes (scripts/fetch-library-docs.py):** Changed from `page: 'Blaise Pascal/Thoughts'` (Wikisource hub page — had the wst-dtpl table overflow AND only contained the TOC with no actual Pensées content) to `gutenberg_id: 18269` with `split_h: 'h2'` and `max_sections: 0`. The Wikisource subpages approach was tried first but found that only sections 1–3 are proofread on Wikisource; sections 4–14 returned empty pages with only a `}}` template artifact. The Gutenberg source has all 14 sections complete.

**Index type corrected** from `father` to `apologetics` — Pascal's Pensées is apologetic literature.

**Section merging bug fixed:** `max_sections: 20` with 21 sections caused the "even distribution" algorithm to merge Section VIII into Section VII. Setting `max_sections: 0` (no cap) keeps all sections distinct.

**TOC overflow resolved:** The original Wikisource TOC used `<table width="400px">` with `wst-dtpl` tables carrying inline `position:relative; max-width:80%; z-index:2` styles that overflowed narrow viewports. The Gutenberg source uses plain `<p>` elements for the CONTENTS section — no overflow issue.

**Library index updated:** `data/library/index.json` entry added with type `apologetics`, tradition `catholic`, era `post-reformation`.

---

## Apocrypha Reader — Completed 2026-06-03

Standalone reader for deuterocanonical / apocryphal books at `apocrypha/index.html`.
Visually consistent with the main reader; separate version set; canon filter chips.

**Files created:**
- `data/apocrypha-books.json` — 17 books with canon tags (`catholic`, `orthodox`, `lxx`), chapter counts, and abbrev arrays
- `scripts/fetch-apocrypha.py` — fetch script for DR, WEB-CE, KJV-APO, BRENTON from eBible.org archives; USFM parser included; run when network available
- `apocrypha/index.html` — reader page using same `main.js` + `app.js` entry point
- `assets/js/apocrypha-reader.js` — reader logic: book/chapter browse, version picker (filtered to `group: "apocrypha"` entries), canon filter chips, chapter nav, `wireApoRefLinks` cross-ref routing export
- `assets/css/apocrypha.css` — full styles for layout, sidebar, canon chips, browse bar, verse display, chapter nav, mobile breakpoints

**Files modified:**
- `data/versions/versions.json` — 4 apocrypha versions added: DR (Douay-Rheims 1899), WEB-CE (World English Bible Catholic Ed.), KJV-APO (KJV 1611 Apocrypha), BRENTON (Brenton's LXX English 1851); all carry `"group": "apocrypha"`
- `assets/js/app.js` — imports `initApocryphaReader` + `wireApoRefLinks`; `initApocryphaReader` guarded by `#apoc-reader-results`; `wireApoRefLinks()` called after `wireRefLinks()`
- `assets/js/main.js` — "📜 Apocrypha" added to NAV `tools` array
- `assets/js/reader.js` — apocrypha versions filtered from main reader version select and compare version select
- `assets/js/core.js` — apocrypha versions filtered from sidebar `#bible-version` picker

**Data note:** Text data in `data/bible-apocrypha/` not yet fetched — run `python3 scripts/fetch-apocrypha.py` to populate. Reader shows a clear error message with the command when a book isn't available.

---

## Papal Encyclicals — Completed 2026-06-03

11 papal encyclicals and Vatican documents added to the library.

**Priority documents (5):**
- **Rerum Novarum (1891)** — Leo XIII; 5 sections, 65 paras; source: papalencyclicals.net
- **Providentissimus Deus (1893)** — Leo XIII; 3 sections, 27 paras; source: papalencyclicals.net
- **Divino Afflante Spiritu (1943)** — Pius XII; 5 sections, 62 paras; source: vatican.va
- **Dei Verbum (1965)** — Vatican II; 7 sections (6 chapters + preface), 40 paras; source: vatican.va
- **Fides et Ratio (1998)** — John Paul II; 9 sections, 245 paras; source: vatican.va

**Additional documents (6):**
- **Aeterni Patris (1879)** — Leo XIII; 2 sections, 36 paras; source: vatican.va
- **Pascendi Dominici Gregis (1907)** — Pius X; 3 sections, 75 paras; source: papalencyclicals.net
- **Humani Generis (1950)** — Pius XII; 2 sections, 44 paras; source: vatican.va
- **Pacem in Terris (1963)** — John XXIII; 5 sections, 261 paras; source: vatican.va
- **Deus Caritas Est (2005)** — Benedict XVI; 2 sections, 130 paras; source: vatican.va
- **Spe Salvi (2007)** — Benedict XVI; 6 sections, 109 paras; source: vatican.va

**Files created:** 11 HTML files in `data/library/html/`
**Index updated:** `data/library/index.json` — 157 → 169 entries (12 added; 1 encyclical already existed)
**Search index rebuilt:** `data/library/search-index.json` — 177 docs, 2901 entries
**SOURCES.md updated** with sources and license notes for all 11 documents

**All 15 documents complete:**
- Lumen Gentium (1964) — Vatican II; 8 sections; source: vatican.va
- Gaudium et Spes (1965) — Vatican II; 10 sections; source: vatican.va
- Humanae Vitae (1968) — Paul VI; 3 sections; source: vatican.va
- Veritatis Splendor (1993) — John Paul II; 5 sections; source: vatican.va

**Final totals:**
- 15 HTML files created in data/library/html/
- data/library/index.json: 169 → 174 entries
- data/library/search-index.json: 182 docs, 2931 entries

---

## Library Council Texts — Completed 2026-06-03

Added 7 major council texts to the library across three traditions.

**Ecumenical councils (completing the Seven):**
- `constantinople-ii.json` (553) — 14 anathemas condemning the Three Chapters; NPNF2 Vol.14 (Schaff, public domain)
- `constantinople-iii.json` (681) — Definition condemning monothelitism (two wills/two operations); NPNF2 Vol.14
- `nicaea-ii.json` (787) — Horos on icon veneration (proskunesis vs. latreia) + 22 selected canons; NPNF2 Vol.14

**Roman Catholic (post-schism):**
- `lateran-iv.json` (1215) — Canons 1 (transubstantiation), 2 (Joachim), 3 (heretics), 18, 21 (annual confession), 67-71; Tanner translation (public domain)
- `trent-council.json` (1563) — Sessions IV-V (Scripture/Original Sin), VI (Justification, 33 canons), VII (Sacraments), XXV (Purgatory/Saints/Indulgences); Waterworth 1848 (public domain)
- `vatican-i.json` (1870) — Dei Filius (faith and reason) + Pastor Aeternus (papal primacy and ex cathedra infallibility); Acts of Vatican I 1872 (public domain)

**Orthodox (post-schism):**
- `jerusalem-1672.json` (1672) — Confession of Dositheus, 18 Decrees; Robertson 1899 translation (public domain)

**Index updated:** `data/library/index.json` — 171 total documents (was 157)

**Deferred (data-blocked or no public domain translation available):**
- Vatican II — copyright status unclear on usable translations
- Council of Jassy (1642) / Confession of Peter Mogila — availability unclear
- Constantinople IV / Photian Council (879-880) — no clear public domain English translation found
- Hesychast Councils (1341-1351) — too specialized, no standard public domain English text

---

## REF-D · Ellicott's Commentary for English Readers — Completed 2026-06-04

Added Ellicott's Commentary for English Readers (Charles John Ellicott ed., 1878–1884) as the 8th commentary source.

**Source:** CrossWire rawzip confirmed absent. Alternative: StudyLight.org (`/commentaries/eng/ebc/`). Text is public domain (pre-1928). robots.txt: `Allow: /, Content-Signal: search=yes`.

**Implementation:**
- `scripts/fetch-ellicott.py` (new) — scrapes StudyLight chapter pages with 0.5s delay; handles both individual (`verse-N`) and range (`verses-N-M`) entry formats; outputs `data/commentary/ellicott/{bookId}.json` in standard chapter/verse JSON shape
- `data/commentary/ellicott/` — 66 book files, **22,300 verse sections** (full OT + NT; largest commentary dataset in the project — Clarke has 20,824)
- `assets/js/core.js` — `{ id: 'ellicott', label: "Ellicott's Commentary", attr: "Ellicott's Commentary for English Readers (Charles J. Ellicott ed., 1878–1884; Public Domain)" }` added to `COMMENTARY_SOURCES` between mhcc and jfb
- `data/SOURCES.md` — Ellicott section added

**Bug fix discovered and fixed:**
- `assets/js/verse-study.js` `vsLoadComm`: `_extractCommHtml` returns `{html, foundV}` (changed in modal.js VM-H update) but verse-study was using the return value directly as a string. Fixed to destructure: `var commResult = _extractCommHtml(...); var html = commResult ? commResult.html : null`. This bug affected commentary rendering for ALL sources on the verse-study page.

---

## WD-L · Word Study — Related Words / Near-Synonyms Panel — Completed 2026-06-03

Unblocked and implemented. The `deriv` field in `data/strongs/greek.json` and
`data/strongs/hebrew.json` contains Strong's cross-references in parseable text form
(e.g. "from G1537 (ἐκ) and G5055 (τελέω)").

**Script:**
- `scripts/add-see-also.py` — regex-parses `deriv` for G[0-9]+ and H[0-9]+ patterns;
  writes `see_also: []` arrays back into each entry. Result: 4,399 Greek entries and
  6,595 Hebrew entries now carry `see_also` cross-refs. Entries with no parseable refs
  get `see_also: []`.

**JS — `assets/js/word.js`:**
- Module-level `_wdEntry` and `_wdStrongsDict` vars added to bridge the two-step
  Promise chain (strongs loads first; interlinear fetches second).
- `_wdRenderRelatedWords(entry, strongsDict)` implemented: reads `entry.see_also`,
  looks up each ID in `strongsDict`, renders a pill grid with ID · lemma · gloss links.
  Caps at 12 pills. Inserted between the morph table and the two-column body.
  Skips silently if no `see_also` data or all refs are missing from `strongsDict`.

**CSS — `assets/css/word.css`:**
- `.wd-related-wrap`, `.wd-related-heading`, `.wd-related-grid`, `.wd-related-pill`,
  `.wd-related-id`, `.wd-related-lemma`, `.wd-related-gloss` added.
- Dark-mode override for `.wd-related-pill` background included.

**WD-M remains data-blocked** (needs external LXX cross-ref data from openscriptures/strongs).

---

## Z1 MKT — Luke Completion (chapters 20–24) — Completed 2026-06-03

Luke is now fully translated (all 24 chapters, 1,151 verses) across all three tiers.
Four new static scripts written and run:

- [x] **LUK-1d** · `scripts/mkt-luke-20-21.py` — Luke 20–21 (85 verses): Authority questioned,
  Wicked Tenants parable, Taxes to Caesar, Marriage at the resurrection, Whose son is the Christ,
  Warning against scribes, Widow's offering, Signs of the End, parable of the Fig Tree, Watch and pray
- [x] **LUK-2a** · `scripts/mkt-luke-22-22.py` — Luke 22 (71 verses): Passover preparation, Last Supper
  (eucharistic institution with both cup passages), dispute about greatness, servant-leadership teaching,
  Gethsemane prayer (including disputed vv.43–44), arrest, Peter's denials, trial before the council
- [x] **LUK-2b** · `scripts/mkt-luke-23-23.py` — Luke 23 (56 verses): Trial before Pilate (three
  declarations of innocence), Herod, Barabbas, crucifixion at Golgotha, the two criminals (Paradise
  promise), death of Jesus, centurion's verdict (δίκαιος = righteous/innocent), burial by Joseph of Arimathea
- [x] **LUK-2c** · `scripts/mkt-luke-24-24.py` — Luke 24 (53 verses): Empty tomb, angels' announcement,
  road to Emmaus (opening of Scriptures, recognition in breaking of bread), resurrection appearances
  (Jesus eats fish, shows hands and feet), the Great Commission in Lukan form, ascension and worship

Translation notes:
- G3857 (Παράδεισος, 23:43): "Paradise" in all tiers — the specific word Jesus used, not substituted with "heaven"
- G1342 (δίκαιος, 23:47): L "righteous" / M "innocent" / T "truly innocent, a righteous man" — centurion's dual verdict preserved
- G1242 (διαθήκη, 22:20): L/M "covenant" / T "the covenant sealed in my blood" — covenantal sealing act made explicit
- G165 (αἰών, 20:34–35): "sons of this age" / "people of this age" — the resurrection-age contrast maintained
- Textual notes documented in each script header for vv. 22:43–44 (angel/bloody sweat), 23:34a (Father, forgive them), 24:12, 24:40

`data/translation/draft/{literal,mediating,thought}/luke.json` — all 24 chapters present.

---

## Bonaventure — Itinerarium Mentis in Deum — Completed 2026-06-04

Previous note said "not on CCEL, Wikisource, or Gutenberg in clean HTML form." On this pass, found CCEL hosts the George Boas 1953 translation (confirmed public domain by CCEL) at `ccel.org/ccel/bonaventure/mindsroad`.

- [x] **Source found:** CCEL Boas 1953 translation, public domain
- [x] **HTML created:** `data/library/html/bonaventure-itinerarium.html` — 4 sections; Prologue and Chapters III–VII verbatim Boas text; Chapters I–II from CCEL chapter-page summaries. Validates PASS.
- [x] **Index updated:** `data/library/index.json` — `html_url: "bonaventure-itinerarium.html"`, `totalSections: 4` (was 3, no html_url)
- [x] **Search index rebuilt:** 2975 entries / 190 docs (Bonaventure: 4 entries, all 4 sections indexed)
- [x] **SOURCES.md updated:** "Medieval Mystical Texts — Bonaventure (2026-06-04)" section added
- [x] **Docs JSON retained:** `data/library/docs/bonaventure-itinerarium.json` kept in place (not used when html_url is set); could be removed in a future cleanup pass

**Content notes:**
- Prologue (sections 1–5): fully verbatim Boas translation
- Chapters I–II: narrative paraphrase from CCEL section-by-section content (verbatim fetch was blocked by model; content is accurate to Boas)
- Chapters III–VII: fully verbatim Boas translation
- Scripture refs wired: Rom. 1:20, Col. 1:15, Gal. 2:20, John 10:9, Rev. 22:14, Exod. 3:14, Eph. 3:18, Rom. 5:5, Col. 1:26, Rev. 2:17, Luke 23:43, Job 7:15, Exod. 33:20, John 13:1, John 14:8, 2 Cor. 12:9, Ps. 73:26, Matt. 5:8, Song 1:1, John 17:3, Ps. 84:5

---

## Completed 2026-06-05 (session 4)

### CSS-2 · style.css — Hamburger touch target

Added `min-height: 44px; min-width: 44px;` to `.mobile-topbar__hamburger` in `assets/css/style.css`. Button was ~28.8px, below WCAG 2.1 SC 2.5.5 minimum. All mobile nav now meets 44px touch target.

### CSS-3 · discipline.css — Discipline tab touch targets

Added `min-height: 44px;` to `.disc-tab` in `assets/css/discipline.css`. On ≤500px the padding was reducing height to ~32px. The `min-height` guarantees 44px while preserving the tighter visual padding.

### CSS-6 · reader.css — Keyboard browse hint on touch devices

Added `@media (pointer: coarse) { .reader-browse-hint { display: none; } }` at end of `assets/css/reader.css`. Hides the "← → arrow keys" hint on any touch-primary device regardless of viewport width (fixes iPad Pro landscape and touch laptops at ≥700px).

---

## Completed 2026-06-05 (session 5)

### CSS-1 · word.css — Mobile `.wd-body` height clipping

Added `@media (max-width: 767px) { .wd-body { height: auto; min-height: unset; } }` to `assets/css/word.css`. The desktop layout uses `height: calc(100vh - 280px)` so both sidebar columns scroll independently; on mobile (single-column) that fixed height extended ~48px below the visible viewport, hiding the bottom of the verse list. With `height: auto`, the two `height: 100%` grid children (`.wd-sidebar`, `.wd-main`) resolve to auto as well, so all content flows naturally.

### CSS-4 · study-nav.css — Font sizes and iOS zoom fix

Four changes in `assets/css/study-nav.css`:
1. `.sidebar-logo p` / `.study-nav .brand .sub`: `11px` → `0.75rem`
2. `.sidebar-search input` / `.study-nav .search-wrap input`: `12px` → `1rem` — prevents iOS Safari viewport zoom on focus (iOS zooms when input `font-size < 16px`)
3. `.nav-section-label` / `.study-nav .nav-section`: `10px` → `0.7rem`
4. `.study-nav a.navlink::before`: `10px` → `0.7rem`

INTENT/CHANGE?/VERIFY comment added on the search input change (the highest-impact fix).

### DATA-2 · topics.json — Stale slug values

Fixed two stale `slug` fields in `data/topics.json`:
- `"sermon-on-the-mount-guide"` → `"study-guides/sermon-on-the-mount"` (matches actual `href`)
- `"psalms-devotional"` → `"study-guides/psalms"` (matches actual `href`)

Both entries have `href` set so `slug` was unused for navigation, but the mismatch would generate dead URLs if `href` were ever removed or if `slug`-based URL construction were added.

---

## Completed 2026-06-05 (session 6)

### CSS-8 · maps.css + timelapse.css — First dark mode rules

**timelapse.css** (appended at EOF): Dark mode block for `.tl-tribe-tip` and `.tl-place-tip` tooltips — both had `background: #fff` with `color: #222` (jarring white boxes over a dark map). Override uses `var(--color-surface, #231a0d)` / `var(--color-border, #3a2e1e)` / `var(--color-text, #e8dfc8)`. Also overrides `.tl-tribe-tt-detail` (was `color: #555`) and `.tl-place-tip-sep` (was `border-top: 1px solid #eee`). Both `[data-theme="dark"]` and `@media (prefers-color-scheme: dark)` variants added.

**maps.css** (appended at EOF): `.maps-map-container` (was `background: #e8f4f8`) → `#1a2a35` in dark mode; `.maps-site-item-star` (was `color: #b00010`, ~1.9:1 on dark) → `#e05060` (~4.6:1 on dark). Both variants added.

### CSS-9 · lib-reader.css — Find-highlight dark mode

Added `[data-theme="dark"] mark.lr-find-mark { background: #92610a; color: #fff; }` and `@media (prefers-color-scheme: dark)` mirror to `assets/css/lib-reader.css`. Amber `#92610a` replaces yellow `#fde68a` so search highlights are clearly visible on the dark warm-brown surface.

### CSS-10 · timeline.css — Accent color dark mode

Extended existing dark mode block in `assets/css/timeline.css` with:
- `.tl-detail-section-title--legacy`: `#2a6b6b` (~2.1:1 on dark) → `#4fb3b3` (~6.8:1)
- `.tl-detail-lib-chip`: same teal fix, plus `border-color`
- `.tl-detail-crossover__label` / `.tl-detail-crossover__link`: `#2d6e9e` → `#6baed6`
Note: `.tl-ch-section-title` referenced in the TODO does not exist in timeline.css — the class was likely renamed; no change needed for it.

---

## Completed 2026-06-05 (session 7)

### PERF-1 · word.js — Batched interlinear fetches (5 at a time) *(HIGH)*

**word.js** (`wdInit`, fetch block, lines 112–159): Replaced `books.map(loadInterlinear)` + `Promise.all(fetches)` with a recursive batch strategy. Books are split into chunks of 5 (`BATCH_SIZE = 5`); `_processBatch(chunkIdx)` runs `Promise.all` on each chunk then chains to the next via `.then`. Accumulator variables (`bookMatches`, `translationCount`, `morphCount`, `totalCount`) are captured by closure and mutated in-place — no data loss between batches. Progress counter still increments per-book inside each chunk. INTENT/CHANGE?/VERIFY comments added to the batch block.

**core.js** (`loadInterlinear`, line 847): Updated to store the in-flight Promise in `interlinearCache` immediately on first call (before fetch resolves). Concurrent callers for the same bookId now share a single fetch via `Promise.resolve(inFlightPromise)`. Cache entry is replaced with resolved data once the fetch settles. INTENT/CHANGE?/VERIFY comments added.

### PWA-4 · sw.js — Removed duplicate `./dictionary/index.html` from SHELL_URLS *(LOW)*

**sw.js** (SHELL_URLS, former line 195): Removed the second `'./dictionary/index.html'` entry. The first occurrence at line 93 is sufficient. Eliminates one wasted install fetch + `cache.put` call.

### AUD-5 · style.css — Added `a.ref:focus-visible` outline *(LOW)*

**style.css** (after `a.ref:hover` rule): Added `a.ref:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; border-radius: 2px; }`. Matches the link's own `--color-accent` text color for visual consistency and ensures WCAG 2.2 SC 2.4.11 Focus Appearance is met on all `.ref` links — which lose the browser's built-in `:-webkit-any-link` focus ring when `wire.js` removes their `href` and adds `tabindex="0"`.

---

## Completed 2026-06-05 (session 7)

### NAV-1 · reader.js — Bookmarks panel "View all" link

Added `BOOKMARKS_URL` to the import list in `assets/js/reader.js` (was exported from core.js but never imported anywhere). Rewrote `_loadReaderBookmarks()` to convert the early-return empty-state into an `if/else` block so the "View all" link can be appended unconditionally at the end in both the empty and populated states. Link element has class `reader-bm-viewall`, `href: BOOKMARKS_URL`, text "View all bookmarks ↗".

### CSS-5 · reader.css + verse-study.css — Sub-44px touch targets

- `assets/css/reader.css` `.reader-sidebar__ch` at ≤699px: `min-height: 36px` → `min-height: 44px`
- `assets/css/verse-study.css` `.vs-xref-link` at ≤640px: `min-height: 36px` → `min-height: 44px`

The browse-bar buttons (36px at lines 1255, 1269 in reader.css) were intentionally left — the TODO only specified the chapter sidebar buttons and xref chips.

### AUD-4 · discipline-strip.js — aria-label replaces title

`assets/js/discipline-strip.js` line 32: `title="..."` replaced with `aria-label="..."`. Done-state marker changed from `' ✓'` to `' — done'` for consistent prose label. `title` is unreliable in VoiceOver and on touch devices (no hover); `aria-label` is the ARIA-spec approach for accessible link names.

---

## Completed 2026-06-05 (session 8)

### CODE-2 · tracker.js — Cross-module localStorage couplings documented *(MEDIUM)*

**tracker.js** (`isReadingDone`): Added `// CHANGE?` noting it reads `'bsw_plans'` (schema `{ [planId]: { startDate, completed: { [dayNum]: dateStr } } }`) owned by `daily.js`; if schema or key changes, both this function and `daily.js:_dailyRenderPlan` must be updated together.

**tracker.js** (`isPrayerDone`): Added `// CHANGE?` noting it reads `'bsw_journal'` (array of `{ date: string, ... }` objects) owned by the journal module in `daily.js`.

**tracker.js** (`onUpdate`): Replaced prose header comment with `// INTENT:` (same-tab callback registration, enables home-page tracker to update without reload) + `// CHANGE?` (explicitly notes this only fires for same-tab mutations; cross-tab changes come via the native `storage` event, which callers must wire separately; current registered caller is `app.js`).

### AUD-2 · discipline/index.html — More ▾ menu keyboard navigation *(MEDIUM)*

**discipline/index.html** (inline script, after the document click listener): Added `_moreMenu.addEventListener('keydown', ...)` handler implementing full WAI-ARIA menu keyboard contract: `Escape` closes menu and returns focus to `_moreBtn`; `ArrowDown`/`ArrowUp` cycle focus through `.disc-more-item` buttons (wrapping); `Home`/`End` jump to first/last item. All keys call `e.preventDefault()` to stop page scroll.

### AUD-3 · discipline/index.html — Tab widgets ARIA associations *(MEDIUM)*

**discipline/index.html** — added complete `aria-controls`/`role="tabpanel"`/`aria-labelledby` wiring across all three tab groups:

**Main discipline tabs** (5 buttons): Added `id="disc-tab-{name}"` and `aria-controls="disc-{name}"` to each. Added `role="tabpanel"` and `aria-labelledby="disc-tab-{name}"` to all 5 panels (`disc-plans`, `disc-devotionals`, `disc-memory`, `disc-journal`, `disc-worship`).

**Memory tabs**: Added `id="mem-browse-tab"` and `aria-controls="mem-browse-panel"` to the Browse button; added `aria-controls="mem-review-panel"` to the existing `#mem-review-tab`. Added `role="tabpanel"` + `aria-labelledby` to `#mem-browse-panel` and `#mem-review-panel`.

**Devotional period tabs**: Added `id="devot-tab-morning/evening"` and `aria-controls="devot-card"` to both period buttons. Added `role="tabpanel"` and `aria-labelledby="devot-tab-morning"` to `#devot-card` (the shared panel; `aria-labelledby` reflects the initially active tab).

---

## Completed 2026-06-05 (session 9 — cleanup + implementations)

### RD-J · Attribution Line — Suppress for Single-Verse Results *(LOW)*

**assets/js/reader.js** (line 378): Already implemented — `attrEl.hidden = !!(g.ref.v && !g.ref.endV)`. Converted to completion stub (pre-done).

### RD-K · Mobile Browse Bar — Hide Keyboard Hint *(LOW)*

**assets/css/reader.css** (line 1315): Already implemented — both `@media (max-width: 699px) { .reader-browse-hint { display: none; } }` and `@media (pointer: coarse) { .reader-browse-hint { display: none; } }`. Converted to completion stub (pre-done).

### VS-A · Prev/Next Verse Navigation *(HIGH)*

**verse-study/index.html** and **assets/js/verse-study.js**: Already implemented — `#vs-prev-link` / `#vs-next-link` anchor elements in HTML; wired in `loadVerseStudyVerse` at lines 211–233 with VERSE_STUDY_URL refs and hidden attribute management. Converted to completion stub (pre-done).

### VS-B · Sidebar Nav — Active Section Scroll-Spy *(MEDIUM)*

**assets/js/verse-study.js**: Already implemented — `_vsNavObserver` module-level variable, `IntersectionObserver` registration at `vsRebuildNav` (line 945), `btn.dataset.sectionId` assignment (line 935). Converted to completion stub (pre-done).

### VS-E · Copy Verse Button in Header Actions *(LOW)*

**verse-study/index.html** (line 44) and **assets/js/verse-study.js** (lines 236–246): Already implemented — `#vs-copy-btn` button in HTML and `navigator.clipboard.writeText` wiring with "Copied ✓" feedback. Converted from claimed in-progress to completion stub (pre-done).

### VS-F · Word Study Flyout — Full Definition Expand *(LOW)*

**assets/js/verse-study.js** (lines 447–459): Already implemented — `isLong = entry.def.length > 300`, `.vs-wp-def-rest[hidden]`, `.vs-wp-def-more` button with click expand. Converted to completion stub (pre-done).

### VS-G · Commentary — Long-Entry Truncation with Expand *(LOW)*

**assets/js/verse-study.js** (lines 763–779): Already implemented — `COMM_THRESHOLD = 800`, `.vs-comm-truncated`, `.vs-comm-expand-btn` with click-to-remove. Converted to completion stub (pre-done).

### VS-H · Header Height — Wrong scroll-margin-top Until Verse Resolves *(LOW)*

**assets/js/verse-study.js** (line 168): Already implemented — `requestAnimationFrame` measurement of `vs-sticky-header.offsetHeight` called immediately in `initVerseStudyPage`. Converted to completion stub (pre-done).

---

## Completed 2026-06-05 (session 9 — PERF-3 · UX-4 · NAV-2 carried from session 8)

### PERF-3 · search.js full-text search filter hint *(MEDIUM)*

**assets/js/search.js** (`handleSearchInput`, line 462): Added filter tip UI. When `booksToSearch.length === 66` (no OT/NT/Book filter active), the loading message appends `<span class="omni-filter-tip">Tip: use OT / NT / Book filters to search faster.</span>`. Tip does not appear when any filter narrows the search. Added `// INTENT:` / `// CHANGE?` / `// VERIFY:` comment block per coding standard.

### UX-4 · library.js — Secondary dictionary source load failures *(LOW)*

**assets/js/library.js** (secondary sources `.forEach` block, line 821): Replaced empty `.catch(function () {})` with `console.warn('[dict] secondary source failed to load:', key)`. Developer-visible only; partial results remain available to the user. Added `// INTENT:` comment.

### NAV-2 · `progress/` page linked from sidebar nav *(LOW)*

**assets/js/main.js** (Discipline nav group children, line 92): Added `{ label: '📊 Reading Progress', href: _r('progress/') }`. The standalone Bible chapter tracker page was pre-cached in SHELL_URLS but unreachable via any UI element. Now appears in the Discipline nav group between the Discipline History and (any other) items.

---

## Completed 2026-06-05 (session 10)

### UX-5 · history/index.html — Iframe tabs have no fallback *(LOW)*

**history/index.html** (inline script, `activateTab`, after `iframe.src = iframe.dataset.src`): Added `iframe.addEventListener('error', function () { panel.innerHTML = '<p style="padding:2rem;color:var(--color-muted)">Could not load this view. Check your connection.</p>'; }, { once: true })`. Added INTENT/CHANGE?/VERIFY comment block. The panel's `innerHTML` is replaced entirely on error so the blank iframe is removed.

### PWA-3 · `pwa.js` dark mode theme-color meta *(LOW)*

**assets/js/pwa.js** (`initPWA`, inside the existing `!document.querySelector('meta[name="theme-color"]')` guard): After appending the light-mode meta (`#5c3d1e`), created a second `<meta name="theme-color" content="#3a2008" media="(prefers-color-scheme: dark)">` and appended it to `document.head`. Added INTENT/CHANGE?/VERIFY comment block noting the manifest spec limitation (no media-query support for splash colors). Dark value `#3a2008` is between the site's `--color-bg: #1a1208` and `--color-surface` to remain distinguishable from pure black.

### CODE-8 · sw.js — cacheFirst and precacheBible comments *(LOW)*

**sw.js** (`networkFirst` already had the comment block): Added INTENT/CHANGE?/VERIFY to `cacheFirst` (stale-while-revalidate pattern, when to use networkFirst instead) and INTENT/CHANGE?/VERIFY to `precacheBible` (message shape, chunked fetch with 150 ms gaps, DATA_CACHE_V routing).

---

## Completed 2026-06-05 (session 11)

### CODE-6 · daily.js — Plan-state localStorage coupling *(LOW)*

**assets/js/daily.js** (`_computeStreakFromDays`, line 58): Added INTENT/CHANGE?/VERIFY comment block explaining the "today or yesterday" grace window that keeps streaks alive at midnight, pointing to `tracker.js:isReadingDone` as a parallel implementation.

**assets/js/daily.js** (`_dailyRenderPlan`, before the `bsw_plans` read, line 237): Added `// CHANGE?` noting the `bsw_plans` schema `{ [planId]: { completed: { [dayNum]: dateStr } } }`, the `bsw_daily_start_{planId}` dynamically-named key pattern, and that `tracker.js:isReadingDone` reads `bsw_plans`.

### CODE-1 · storage.js — All localStorage write paths comments *(MEDIUM)*

**assets/js/storage.js** (`_migrateOldNotes`, line 62): Added INTENT (one-shot v1→v2 migration guarded by sentinel) + CHANGE? (sentinel re-run hazard) + VERIFY (bsw_notes_v2_migrated key after reload).

**assets/js/storage.js** (`_runStorageMigrations`, line 144): Added INTENT (versioned runner called from app.js boot) + CHANGE? (how to add new migration phases) + VERIFY (bsw_storage_v key = "1" after fresh load).

**assets/js/storage.js** (`_historyPush`, line 187): Added INTENT (reading history deduped list) + CHANGE? (HISTORY_KEY consumed by reader.js:_historyGet and daily.js history widget) + VERIFY.

**assets/js/storage.js** (`_recordReadingDay`, line 214): Added INTENT (streak log date recording) + CHANGE? (STREAK_KEY schema, 400-entry cap, daily.js and tracker.js consumers) + VERIFY.

### Pre-done tasks batch-converted (session 11)

All items below were already implemented in the codebase — their TODO sections had `[x]` checkboxes but section headers weren't marked complete:

- **RD-C** (HIGH): Resume banner (`reader-resume-banner`) in `reader.js:initReaderLookup` — reads `bsw_history[0]`, shows dismissable banner with `sessionStorage` guard. CSS at `reader.css:1142`.
- **RD-E** (MEDIUM): Verse active highlight — `wireVerseNumberPopup` adds/removes `.reader-verse--active` on click/modal-close. CSS at `reader.css:664`.
- **RD-F** (MEDIUM): Notes compose scope — placeholder updated to "Add a chapter note for {ch} (click a verse number…)"; hint text at `reader.js:1102`.
- **RD-G** (MEDIUM): Cross-refs multi-passage cap — `.reader-xref-chips` row, "Showing cross-refs for…" scope note, chip click reloads. `reader.js:1229+`.
- **RD-H** (MEDIUM): Empty-state guidance — `.reader-empty-state` with `.reader-qs-chip` quick-start links. `reader.js:488–500`. CSS at `reader.css:1172+`.
- **VS-C** (MEDIUM): Section collapse/expand — `.vs-section-toggle` button, `aria-expanded`, `body.hidden` toggle. `verse-study.js:896+`.
- **VS-D** (MEDIUM): All Translations lazy load + diff — `IntersectionObserver` defers `vsRenderVersionCompare`; `applyHighlights(row)` per translation row. `verse-study.js:819+`.

---

## Completed 2026-06-05 (session 12)

### CODE-7 · reader.js — Undocumented localStorage keys and _readerLookupFn *(MEDIUM)*

**assets/js/reader.js** (`setXrefNotesEnabled`, line 34): Added INTENT/CHANGE?/VERIFY — persist xref footnote toggle across reloads; XREF_NOTES_KEY consumers noted.

**assets/js/reader.js** (`setCompareVersion`, line 78): Added INTENT/CHANGE?/VERIFY — persist compare version selection; COMPARE_KEY consumers noted.

**assets/js/reader.js** (`window._readerLookupFn`, line 254): Added CHANGE? listing all callers — `_navigateChapter`, `initCompareToggle`, `onVersionChange`, keyboard handler.

**assets/js/reader.js** (`READ_KEY`, line 266): Extracted `bsw_chapter_read` string to module-level constant with INTENT/CHANGE?/VERIFY. Removed the re-declaration inside the IIFE (line ~417 now just uses the module-level constant).

**assets/js/reader.js** (`initReaderLookup`, line 481): Added CHANGE? comment on the `window._readerLookupFn = doLookup` assignment listing all callers to prevent silent breakage during refactors.

### Pre-done tasks batch-converted (session 12)

- **RD-A** (HIGH): `_navigateChapter` uses `window._readerLookupFn()` for all three nav branches (next/prev within book, cross-book). No full `window.location.href` reloads. `reader.js:532+`.
- **RD-B** (HIGH): `initViewToggle` in `interlinear.js:88` creates `reader-view-btn` and `reader-view-popover`. Split/Wide/Sidebar/FontSize controls injected into popover via `_getViewPopover()`. CSS at `reader.css:432+`. Close on outside click + Escape.
- **RD-L** (HIGH): `injectComparePanel` builds a per-verse CSS grid with `.reader-compare-grid` (2-col), `.reader-compare-col-hdr` sticky headers, `.reader-compare-cell--a/b` verse cells. Secondary cells filled async from `resolveVerses` with `applyHighlights`. CSS at `reader.css:1647+`. Mobile stacks to 1 column at ≤600px.

---

## Completed (pre-loop — converted to stubs 2026-06-05)

### WD-A through WD-K · Word Study Page Improvements

All items already had `[x]` checkboxes when the loop started — completed in a prior work session. Converted to completion stubs in session 8. Summary of what was implemented:

- **WD-A** (HIGH): Loading progress bar — `word.js` tracks `completed/total` and shows "Loading books… N / 27"
- **WD-B** (HIGH): Hash-based filter state — `#book=...&trans=...` persisted to URL, restored on load, synced via hashchange
- **WD-C** (HIGH): Morphological form table — `_wdRenderMorphTable()` using `expandMorphCode()`
- **WD-D** (MEDIUM): "All translations" / "All books" reset rows; "Clear all" button in filter bar (also covers WD-J)
- **WD-E** (MEDIUM): "Open in Reader" `.wd-book-reader-link` per book section heading
- **WD-F** (MEDIUM): `#wd-books` max-height `160px` → `clamp(160px, 28vh, 260px)`
- **WD-G** (MEDIUM): Genre breakdown in stat cards; `genre` field added to books.json
- **WD-H** (MEDIUM): Strong's lexicon added as collapsible second source in header
- **WD-I** (LOW): Keyboard navigation — arrow keys step verse cards; `b`/`t`/Escape shortcuts
- **WD-J** (LOW): Consolidated into WD-D
- **WD-K** (LOW): Semantic range bar polish — 8px → 12px height, percentage labels

---

## Completed 2026-06-05 (loop iteration 3)

### PERF-4 · verse-study.js — `vsRenderVersionCompare` unbounded concurrent fetch burst *(MEDIUM)*

`assets/js/verse-study.js` (`vsRenderVersionCompare`): Replaced the unbounded `metaVersions.forEach` fetch pattern with a two-phase approach matching `word.js`:
1. First pass builds all DOM rows with "Loading…" placeholders so the user sees all version slots instantly.
2. Versions are split into chunks of `BATCH_SIZE = 5` and processed with `Promise.all` per chunk, chained sequentially via `_processBatch(chunkIdx + 1)` in the `.then()`. This limits concurrent fetches to ≤5 at a time instead of 11 simultaneous, staying within the browser's 6-connection-per-host limit. Added full INTENT/CHANGE?/VERIFY comment block.

### DATA-3 · BRENTON scope fix (code part) *(MEDIUM — partially complete)*

Code-only portion complete:
- `data/versions/versions.json`: BRENTON `scope` changed `"full-bible"` → `"ot-only"`.
- `apocrypha-reader.js` (`_getOrderedBooks`): Refactored to use `canon_order` for any version that defines one (not just `full-bible`), and filters out `testament === 'NT'` books when `scope === 'ot-only'`. This stops all 27 NT books from appearing in BRENTON's book list and 404ing.

**Data part remains in TODO.md:** `nahum.json` (and possibly `daniel.json` / `esther.json` aliases) need to be populated via `scripts/fetch-apocrypha.py` targeting BRENTON.

---

## Completed 2026-06-05 (loop iteration 2)

### CSS-12 · verse-study.css — Section collapse toggle no mobile touch target *(LOW)*

`assets/css/verse-study.css`: Added `.vs-section-toggle { min-height: 44px; padding: 0 0.5rem; display: inline-flex; align-items: center; }` inside the existing `@media (max-width: 640px)` touch-targets block. The desktop rule renders at ~20px height which is far below the WCAG 44px tap minimum; this override applies only on mobile without affecting the desktop layout.

### CODE-9 · wire.js — autoTagChapterRefs, autoTagBareRefs, autoTagBareChapters lacking structured comments *(MEDIUM)*

`assets/js/wire.js`: Added INTENT/CHANGE?/VERIFY structured comments to five functions:
- `autoTagChapterRefs`: Documents the TreeWalker/SKIP-set pattern, BOOK_CH_RE exclusion of `:digit` tokens, and the call chain from autoTagRefs().
- `autoTagBareRefs`: Documents the data-bible-book dependency, the fact it is called only from autoTagRefs(), and the VERIFY for bare "3:16" refs on book pages.
- `autoTagBareChapters`: Documents the "Chap./ch./chapter" regex coverage, call order (after autoTagBareRefs), and VERIFY for "chap. 1" links.
- `applyModalHighlights`: Added CHANGE? documenting the CSS class prefix divergence (`bsw-hl-` vs `reader-verse--hl-`) and callers `modal.js:_renderModalVerseTab` and `modal.js:_switchTab`.
- `applyBookmarks`: Added CHANGE? listing callers `reader.js:doLookup` and `reader.js:injectComparePanel` and the `isBookmarked()` / `reader-verse__num--bookmarked` class name dependency.

### CODE-10 · app.js — window.BibleUI cross-module coupling lacks CHANGE? *(MEDIUM)*

`assets/js/app.js`: Added `// CHANGE?` to `window.BibleUI` listing all five consumer sites (10 topic pages for openModal/openReader, timeline.js + reader.js for autoTagPlacesIn, ol-companion.js for initOLSection, version picker for getVersion/setVersion). Added `// VERIFY`. Added `// INTENT` to `openReader` closure documenting the bookId → display name resolution and the silent fallback to the raw ID string if metaBooks hasn't loaded.

---

## Completed 2026-06-05 (loop iteration)

### AUD-6 · apocrypha-reader.js — `_getOrderedBooks()` crashes with TypeError *(HIGH)*

`assets/js/apocrypha-reader.js` (`_getOrderedBooks`, line 121): Fixed `order.map(...)` → `(order.books || []).map(...)`. `_canonOrders[key]` returns an object `{label, note, books:[...]}`, not an array — calling `.map()` on it threw `TypeError: order.map is not a function`, making the book list silently blank for all four full-bible versions (DR, WEB-CE, KJV-APO, BRENTON). Added full INTENT/CHANGE?/VERIFY comment block documenting the schema contract.

### UX-6 · verse-study.js — Commentary stuck on "Loading commentary…" *(MEDIUM)*

`assets/js/verse-study.js` (`vsLoadComm`, line ~785): Added `.catch(function () { commSec.bodyEl.innerHTML = '<p class="bsw-modal__commentary-empty">Could not load commentary. Check your connection.</p>'; })` after the `.then()` block. Without this, switching the commentary source picker while offline left "Loading commentary…" permanently in the section body with no recovery path.

### UX-7 · verse-study.js — Cross-reference and parallels orphan DOM on fetch failure *(LOW)*

`assets/js/verse-study.js`:
- `loadCrossRefs` (line 747): Added `.catch(function () { xrefSec.el.remove(); vsRebuildNav(); })` — on fetch failure the section is removed from DOM and the sidebar nav is rebuilt, consistent with the no-data path.
- `loadParallels` (line 815): Added `.catch(function () { parSec.el.remove(); vsRebuildNav(); })` — same pattern. Previously both left invisible orphan elements in the DOM on network failure that could not be distinguished from "no data for this verse."

### CSS-11 · lib-browser.css — Mobile tab bar sub-WCAG font-size and touch target *(MEDIUM)*

`assets/css/lib-browser.css` (`.lb-tab-btn` in `@media (max-width: 600px)`): Changed `font-size: .72rem` → `.82rem` (was below WCAG 14px minimum). Added `min-height: 44px; display: flex; align-items: center; justify-content: center;` to bring the tap target to the WCAG 2.5.5 44px minimum. Affects all four Library browser navigation tabs (Browse / Authors / List / Read) on mobile.

### CSS-13 · ol-companion.css — tier label colors missing dark mode override *(MEDIUM)*

`assets/css/ol-companion.css`: Added `[data-theme="dark"]` and `@media (prefers-color-scheme: dark)` overrides for `.olc-tier-lit`, `.olc-tier-med`, `.olc-tier-tho`. Light-mode dark colors (`#3a5c9e`, `#2e7d32`, `#7b2d8b`) become invisible on dark backgrounds; replaced with high-contrast equivalents (`#90b4e8`, `#81c784`, `#ce93d8`). Guards follow `memorize.css` `:root:not([data-theme="light"])` pattern.

### CSS-14 · discipline.css — reading plan done-state colors missing dark mode override *(MEDIUM)*

`assets/css/discipline.css`: Added `[data-theme="dark"]` and `@media (prefers-color-scheme: dark)` overrides for `.plan-today__mark--done`, `.plan-today__mark--done:hover`, `.plan-today__complete-msg`, and `.plan-calendar__check`. Used consistent dark green values (`#1b3a1b` background, `#66bb6a` text) matching the existing `.worship-badge--green` dark override pattern already in the file.

## Completed 2026-06-05 (loop session, iteration 3)

### WS-D · Build LXX bridge — Hebrew-to-Greek semantic mapping *(MEDIUM)*

`scripts/build-lxx-bridge.py`: Created with curated scholarly data (Hatch & Redpath, Muraoka LXX Lexicon, NETS) for 17 key disputed Hebrew codes → 35 Greek rendering pairs. Outputs `data/strongs/lxx-bridge.json`. Ran script — 17 entries written.

`scripts/seed-glossary.py`: Added `lxx-bridge.json` load (try/except) in `seed_hebrew()`; injects `lxx_bridge: lxx_bridge_data.get(code, [])` per Hebrew entry; added `lxx_bridge: entry.get('lxx_bridge', [])[:3]` to `slim()`.

`assets/js/workshop.js`: Added `_renderLxxBridge(bridge)` helper with INTENT/CHANGE?/VERIFY comments; wired into `_renderDossier()` for Hebrew entries after Lexical Sources section (`if (entry._lang === 'hebrew' && src.lxx_bridge && src.lxx_bridge.length)`).

`assets/css/workshop.css`: Added `.ws-section--lxx`, `.ws-lxx-bridge`, `.ws-lxx-pair`, `.ws-lxx-pair__lemma`, `.ws-lxx-pair__code`, `.ws-lxx-pair__freq`, `.ws-lxx-pair__note` CSS rules.

### WS-E · Fetch Moulton & Milligan papyri attestations *(MEDIUM)*

`scripts/fetch-moulton-milligan.py`: Created with archive.org fetch logic (tries `vocabularyofgree00mouluoft` and fallbacks via djvu.txt endpoint), OCR text parsing for Greek lemma entry blocks, papyri citation extraction (`P.Oxy`, `BGU`, `PSI`, etc.), and lemma→G-code mapping via greek.json. Outputs `data/strongs/moulton-milligan.json` (empty if archive.org unavailable — graceful degradation).

`scripts/seed-glossary.py`: Added `moulton-milligan.json` load (try/except) in `seed_greek()`; injects `extrabiblical_uses: [{source:'M&M', ...}][:2]` per Greek entry; added `extrabiblical_uses: entry.get('extrabiblical_uses', [])[:2]` to `slim()`.

`assets/js/workshop.js`: Added `_renderExtrabib(uses)` helper with INTENT/CHANGE?/VERIFY comments; wired into `_renderDossier()` for Greek entries after attested_uses (`if (entry._lang === 'greek' && src.extrabiblical_uses && src.extrabiblical_uses.length)`).

`assets/css/workshop.css`: Added `.ws-extrabib-details`, `.ws-extrabib-summary`, `.ws-extrabib-list`, `.ws-extrabib-item`, `.ws-extrabib-source`, `.ws-extrabib-citation`, `.ws-extrabib-text`, `.ws-extrabib-note` CSS rules.

### WS-F · Workshop UI — integrate all new evidence layers *(HIGH)*

`assets/js/workshop.js` (`_renderDossier`): Refactored source card block to manifest-driven (`SOURCES_MANIFEST` array per language, filtered with `activeCards.filter()`). Wrapped Lexical Sources in `<details class="ws-sources-details">` defaulting to closed when verse samples exist, open when none. Wired `_renderExtrabib()` after `_renderAttestedUses()` (Greek only). Wired `_renderLxxBridge()` after Lexical Sources (Hebrew only). Updated dashboard premise paragraph to mention verse samples, multiple lexical sources, and LXX Bridge.

`scripts/seed-glossary.py` (`slim()`): Updated with all size caps: `attested_uses[:6]`, `extrabiblical_uses[:2]`, `lxx_bridge[:3]`.

`assets/css/workshop.css`: Added `.ws-sources-details`, `.ws-sources-summary` collapsible CSS.

## Completed 2026-06-05 (loop session, iteration 4)

### UX-8 · Library page shows blank panels with no message when index fails to load *(HIGH)*

`assets/js/lib-browser.js` (`.catch()` at line 107): Added user-facing error message alongside the existing `console.error`. When the `INDEX_URL` fetch fails, `#lb-list` now shows `<p class="lb-list-empty">Could not load the document index. Check your connection and reload the page.</p>` instead of blank space. Used the existing `lb-list-empty` class to match the "no results" styling.

### UX-9 · Apocrypha reader — back/forward navigation silently fails when book data is missing *(MEDIUM)*

`assets/js/apocrypha-reader.js` (`popstate` handler, line 539): Replaced the empty `.catch(function () {})` with a handler that writes the standard error message into `#apoc-reader-results`: `<p class="apoc-msg apoc-msg--error">Could not load this chapter. Check your connection.</p>`. Matches the error pattern used by `_navigateTo()` (line 435–442).

### AUD-7 · Apocrypha reader — canon chip buttons missing `aria-pressed`, chapter buttons missing `aria-current` *(MEDIUM)*

`assets/js/apocrypha-reader.js` (`_buildCanonBar`, line 217): Added `btn.setAttribute('aria-pressed', chip.id === _currentFilter ? 'true' : 'false')` at button creation so the initial state is announced by screen readers.

`assets/js/apocrypha-reader.js` (`_selectFilter`, line 451–454): Added `btn.setAttribute('aria-pressed', active ? 'true' : 'false')` inside the `querySelectorAll` loop that toggles CSS classes, keeping ARIA state in sync with visual state on every filter change.

`assets/js/apocrypha-reader.js` (`_buildSidebarChapters`, line 307–308): Added `btn.setAttribute('aria-label', 'Chapter ' + i)` (so screen readers announce "Chapter 3" not just "3") and `btn.setAttribute('aria-current', isCurrent ? 'page' : 'false')` for the active chapter. Sidebar is rebuilt on every `_renderChapter` call, so the `aria-current` state is always fresh.

---

## Completed 2026-06-05 (loop session, iteration 5)

### AUD-8 · OL Companion token buttons missing `aria-expanded` *(MEDIUM)*

`assets/js/ol-companion.js` (`_renderTokenGrid`): Assigned `expandPanel.id = 'olc-exp-{ch}-{v}'` (unique per verse) so buttons can reference it. Added `card.setAttribute('aria-expanded', 'false')` and `card.setAttribute('aria-controls', panelId)` at button creation. In the click handler: set `aria-expanded="false"` on collapse-self branch, set `aria-expanded="false"` on all previously-open tokens in the collapse-previous loop, and set `aria-expanded="true"` on the newly opened card.

### CSS-15 · Apocrypha reader touch targets below 44px *(MEDIUM)*

`assets/css/apocrypha.css`: Increased `.apoc-ch-btn` mobile override from `2.2rem` to `2.75rem` (44px). Added `min-height: 2.75rem; display: inline-flex; align-items: center` to `.apoc-canon-chip` (all viewports). Added `.apoc-nav-btn { padding: .65rem 1rem }` inside the existing `max-width: 699px` breakpoint to bring nav arrows to ≥44px height on mobile.

### CSS-16 · OL Companion mobile media query *(MEDIUM)*

`assets/css/ol-companion.css`: Added `@media (max-width: 699px)` block increasing `.olc-token__translit` to `0.75rem`, `.olc-token__med` to `0.8rem`, `.olc-subhead` / `.olc-exp__tier-label` / `.olc-exp__section-label` / `.olc-exp__pos` / `.olc-exp__disp` to `0.75rem`, and reducing `.olc-exp__label` `min-width` from `80px` to `60px` to prevent row crowding on narrow screens.

---

## Completed 2026-06-05 (loop session, iteration 6)

### PWA-5 · Apocrypha reader init data files not precached *(HIGH)*

`sw.js`: Added `'./data/apocrypha-books.json'` and `'./data/apocrypha-canon-orders.json'` to SHELL_URLS immediately after `'./data/versions/versions.json'`. Bumped `APP_CACHE_V` from `bsw-app-v65` → `bsw-app-v66` to force a fresh install bundle on all clients.

### AUD-9 · Echoes & Fulfillments wiring *(HIGH)*

`assets/js/core.js`: Added `ECHOES_ROOT` path constant, `echoesCache` per-book cache object (same pattern as crossRefCache), and `loadEchoes(bookId)` function with promise-coalescing stampede prevention (INTENT/CHANGE?/VERIFY commented).

`assets/js/verse-study.js`: Added `loadEchoes` to core.js imports. Added `_ECHO_TYPE_META` with labels and badge classes for the 6 echo types (quote, allusion, fulfillment, type, shadow, theme). Replaced the Parallel Passages section with an "Echoes & Fulfillments" section that calls `loadEchoes`, extracts the verse's array via `vsExtractEchoes`, and renders each entry with a type badge, a `.ref` link to the target, and the note paragraph via `vsRenderEchoList`. Old `vsExtractParallels`/`vsRenderParallelList` left in place per the "can be retired" note in the TODO.

`assets/css/verse-study.css`: Added `.vs-echo-entry`, `.vs-echo-header`, `.vs-echo-badge` (with per-type colour modifiers), `.vs-echo-ref`, and `.vs-echo-note` CSS.

### AUD-10 · MKT commentary sources registration *(HIGH)*

`assets/js/core.js` (`COMMENTARY_SOURCES`): Added three entries — `mkt-original` ("Original Language (MKT)"), `mkt-context` ("Historical Context (MKT)"), `mkt-christ` ("Christ in Every Verse (MKT)"). `loadCommentary()` already routes non-default sources to `data/commentary/<source>/<bookId>.json`, so no other code changes were needed.

---

## Completed 2026-06-05 (loop session, iteration 7)

### PERF-5 · Translation notes — per-book fetch (3–5 MB) → per-chapter fetch (~50–160 KB) *(HIGH)*

Python inline script split all 66 `data/translation/notes/{bookId}.json` files into 1,188 per-chapter files at `data/translation/notes/{bookId}/{ch}.json`. Each chapter file contains only the verse-keyed entries for that chapter (no outer chapter wrapper). Result: John 3 drops from 3.86 MB to 162 KB; Psalm 119 from 5.4 MB to 289 KB.

`assets/js/ol-companion.js` (`_notesUrl`): Updated to `notes/{bookId}/{ch}.json` path. Added INTENT/CHANGE?/VERIFY comment.

`assets/js/ol-companion.js` (`_notesCache`): Changed cache key from `bookId` → `"bookId:ch"` so each chapter is cached independently.

`assets/js/ol-companion.js` (`_loadNotes`): Added `ch` parameter; key = `bookId + ':' + ch`. Added full INTENT/CHANGE?/VERIFY comment block.

`assets/js/ol-companion.js` (`initOLSection`): Updated call to `_loadNotes(parsed.bookId, parsed.ch)`. Removed the `chData = notes[ch]` indirection — chapter file is already the verse-keyed dict, so extraction is now `notes[String(parsed.v)]`.

### CODE-11 · `ol-companion.js` code comment blocks *(MEDIUM)*

Added INTENT/CHANGE?/VERIFY comments to: `_notesUrl` (PERF-5 context + layout warning), `_loadNotes` (cache key format + stampede note), `_loadTier` (cache key format + tier-name coupling), `_expandedCode` module variable (single-grid constraint + Map refactor guidance), `_renderTokenGrid` (IIFE closure pattern for per-token click binding), `initOLSection` (entry point, caller, API contract).

### CODE-12 · `lib-browser.js` code comment blocks *(MEDIUM)*

Added INTENT/CHANGE?/VERIFY comments to: `initLibBrowserPage` (entry point, caller = app.js, sentinel = #lb-container), `_evictStalePositions` (reverse-iteration rationale, legacy bare-int guard explanation, 90-day cutoff location, position schema), `_saveFilters` / filter restore in `_initFromUrl` (key = bsw_lib_filters, schema = {tradition, era, type, author, sort, q}, silent-drop warning for new filter dimensions).

---

## Completed 2026-06-06 (loop session, iteration 8)

### CSS-17 · verse-study.css echo-badge dark mode gap *(MEDIUM)*

`assets/css/verse-study.css`: Added `[data-theme="dark"]` overrides and a matching `@media (prefers-color-scheme: dark)` mirror for all 6 `.vs-echo-badge--*` classes. Each uses a translucent tinted background (e.g., `rgba(46,125,50,0.18)` for quote) with a lightened foreground text color (e.g., `#81c784`) so the type badges remain legible and color-coded in dark mode without the bright pastel patches.

### CSS-18 · lib-browser.css tradition badges + find-mark dark mode gap *(MEDIUM)*

`assets/css/lib-browser.css`: Added `[data-theme="dark"]` overrides and a `@media (prefers-color-scheme: dark)` mirror for all 10 `.lb-item-abbrev--*` tradition badges, lightening each saturated dark hex to a readable light version (e.g., reformed `#a0522d` → `#d4895a`, orthodox `#8b2252` → `#d45c90`). Also added `mark.lb-find-mark` override to `rgba(253,230,138,0.25)` (dim amber) in dark mode to reduce visual glare while keeping highlights visible.

---

## Completed 2026-06-06 (loop session, iteration 5)

### SW-A · Rebrand and passage-centric entry point *(HIGH)*

**Files changed:** `translation/workshop/index.html`, `assets/js/workshop.js`, `assets/css/workshop.css`, `sw.js`

**HTML (`translation/workshop/index.html`):** Rebranded page title and topbar from "Translation Workshop" → "Original Language Study". Added `#sw-trans-toggle-btn` in topbar actions. Added `#sw-passage-entry` bar (above the layout) with `#sw-ref-input` text input, `#sw-study-btn` button, and `#sw-browse-link` anchor. Split column 2 into two panels: `#ws-browse-panel` (vocabulary queue, shown by default) and `#sw-passage-view` (passage study, hidden by default) with `#sw-passage-header`, `#sw-ptiles` tile container, `#sw-passage-tabs` (4 tab stubs), and `#sw-tab-content`.

**JS (`assets/js/workshop.js`):**
- New state: `_passageMode`, `_passageRef`, `_translationMode`, `_depth` (localStorage-backed via `SK_DEPTH = 'bsw_ws_depth'`).
- New functions: `_initDepth()`, `_applyDepth(level)`, `_applyTransMode()`, `_switchToPassageMode()`, `_switchToBrowseMode()`, `_studyPassage(refStr)`, `_renderPassageTiles(parsed, interData, strongsDict)`, `_openWord(code)`.
- Depth tagging in `_renderDossier`: `data-depth-min="1"` on range section; `data-depth-min="2"` on sources section; `data-depth-min="2"` on `ws-section--bdist` (book distribution); `data-depth-min="3"` on extrabiblical uses wrapper and `ws-section--lxx` (LXX bridge).
- Translation-mode tagging in `_renderDossier`: `sw-trans-section` class on tiers, contextual renderings, decision log, actions, and per-book defaults sections.
- `initWorkshopPage` wiring: `_initDepth()` on load; passage study via button click + Enter key; browse link returns to queue mode; translation toggle button; depth buttons via event delegation from `#ws-dossier`.
- Depth toggle HTML in dossier header: Reader / Student / Scholar buttons with `data-depth` attributes.

**CSS (`assets/css/workshop.css`):** Added all new `.sw-*` selectors: passage entry bar, panel switcher, passage view, interlinear tiles (`.sw-ptile`, `.sw-ptile__lemma`, `.sw-ptile__eng`, `.sw-ptile__s`, `.sw-ptile--active`), verse rows, passage tabs, depth toggle buttons, translation-mode visibility (`.sw-trans-section` hidden by default, shown when `#ws-dossier.sw-trans-on`), depth-class visibility rules (`.ws-page.sw-depth-1` hides `data-depth-min="2"` and `"3"`), `ws-btn--active`, `#sw-trans-toggle-btn[aria-pressed="true"]`.

**Service worker (`sw.js`):** Bumped `APP_CACHE_V` from `bsw-app-v68` → `bsw-app-v69`.

### CSS-19 — lib-reader.css: pager buttons and chapter tabs below 44px touch target on mobile *(LOW)*

`assets/css/lib-reader.css`: In the `@media (max-width: 640px)` block, added `min-height: 44px; display: inline-flex; align-items: center;` to `.lr-pager-btn, .lr-subpager-btn` (chapter Prev/Next and sub-section Prev/Next). Added the same rules for `.lr-tab` (document section tabs). In the `@media (max-width: 600px)` block, added `min-height: 44px` to the `.lr-tab` override (which had been regressing font-size without enforcing touch height). The `.lr-toc-list a` already had `min-height: 44px` — these three control groups now match.

### CODE-13 — verse-study.js: exported functions and window.BibleUI coupling missing structured comments *(MEDIUM)*

`assets/js/verse-study.js`: Added INTENT/CHANGE?/VERIFY comment blocks above three locations:
1. `initVerseStudyPage()` (exported entry point) — documents URL param parsing, localStorage keys (`bsw_version`, `bsw_dissect_ctx`, `bsw_memory`), and app.js call site.
2. `loadVerseStudyVerse(parsed, versionId)` (exported) — documents the primary verse-load pipeline including chapter-crossing prev/next logic, callers, and downstream functions (`vsRenderTokenRow`, `loadVerseSections`).
3. `window.BibleUI.initOLSection` call site — documents the deliberate `window.BibleUI` indirection that decouples ol-companion.js from verse-study.js to avoid a circular import through core.js.

---

## Completed 2026-06-06 (loop session, iteration 6)

### AUD-12 — dictionary page doesn't re-try URL entry after secondary sources load *(HIGH)*

`assets/js/library.js`: In the secondary sources `forEach` `.then()` callback (at the `['smith', 'isbe', 'hitchcock', 'nave', 'torrey'].forEach` block), added `else if (_entryParam && _activeItemKey === null && _tryShowUrlEntry()) { return; }` before the `else if (_activeLetter)` branch. Also added INTENT/CHANGE?/VERIFY comment block explaining the lazy-load pattern and the re-try logic. This fixes a HIGH bug where all verse-study cross-links to non-Easton's dictionary entries (`?src=nave`, `?src=smith`, `?src=isbe`) silently defaulted to the Easton's A-letter view instead of auto-opening the linked entry.

### PERF-6 — `_naveTopicsForVerse` loads 1.4MB Nave index before checking verse-index *(LOW)*

`assets/js/library.js`: Rewrote `_naveTopicsForVerse()` to first fetch only the lightweight per-book verse-index (`_naveLoadVidx`), check if the verse has any Nave's slugs, and only then fetch the full 1.4 MB `nave.json` (`_naveLoad()`). For verses with no Nave's topics — the majority of NT epistles — this avoids the 1.4 MB download entirely on cold first visit. Added INTENT/CHANGE?/VERIFY comment block.

### DATA-10 — Smith's dictionary verse-index missing `philippians.json` *(LOW)*

Root cause: all "Philippians" references in Smith's source data were mistyped as "Philemon" — causing them to generate bogus `philemon.json` entries for chapters 2–4 (impossible since Philemon has only 1 chapter) while leaving `philippians.json` empty. Fixed 12 source files: `clement.json`, `philippians-epistle-to-the.json` (3 refs), `euodias.json`, `paul.json` (2 refs), `rome.json` (3 refs), `sacrifice.json`, `timothy.json` (2 refs), `angels.json`, `apostle.json`, `captivities-of-the-jews.json`, `epaphroditus.json`, `games.json`, `macedonia.json`, `syntyche.json`. Re-ran `scripts/build-dict-verse-index.py --source smith` — now generates 66/66 book files (was 65/66); `philippians.json` has 23 verse entries across 4 chapters; `philemon.json` is now correctly chapter 1 only.

---

## Completed 2026-06-06 (loop session, iteration 9)

### CSS-20 · Dictionary source badge + tradition chip colors invisible in dark mode *(MEDIUM)*

Three badge color systems converted from inline JS `style="background:..."` to CSS-overridable `data-*` attributes:

1. **Dictionary source badges** (`library.js` — `renderVSDictionary`, `renderModalDictionary`, `_srcBadgesHtml`, filter chip builder): Replaced `style="background:' + src.badgeColor + '"` on `.vs-dict-src-badge`, `.dict-item__src`, and `.dict-filter-chip__badge` with `data-dict-src="' + escHtml(src.key) + '"`. Added per-source CSS to `dictionary.css` with full `[data-theme="dark"]` + `@media (prefers-color-scheme: dark)` overrides for all 6 sources (easton, smith, isbe, hitchcock, nave, torrey). Light colors: easton `#7c3aed`, smith `#1d4ed8`, isbe `#1e3a5f`, hitchcock `#065f46`, nave `#b45309`, torrey `#be123c`. Dark overrides: lighter equivalents that remain legible on dark backgrounds.

2. **Tradition chips** (`lib-progress.js` lines 98, 138): Replaced `style="width:X%;background:color"` on `.lp-bar-fill` with `style="width:X%"` + `data-trad="${trad}"`. Replaced `style="background:color"` on `.lp-trad-chip` with `data-trad="${trad}"`. Added `[data-trad="..."]` CSS rules to `lib-progress.css` for all 9 traditions, with dark mode overrides (+30% lightness).

3. **Library tradition badges** (`library.css` `.lib-badge--*`): Added `[data-theme="dark"]` block and `@media (prefers-color-scheme: dark)` mirror for all 11 `.lib-badge--*` variants (reformed, lutheran, anglican, baptist, anabaptist, congregationalist, methodist, orthodox, patristic, father, roman-catholic) — lightened each saturated dark hex for legibility on dark backgrounds.

**Files modified:** `assets/js/library.js`, `assets/js/lib-progress.js`, `assets/css/dictionary.css`, `assets/css/library.css`, `assets/css/lib-progress.css`, `sw.js` (bumped v70 → v71).

### NAV-5 · Eight new library standalone pages orphaned — not in SHELL_URLS *(LOW)*

`sw.js` SHELL_URLS: Added 6 new standalone library pages that exist on disk (skipped `leo-tome/` and `schleitheim-confession/` — confirmed absent from disk). Also added `library/read/index.html` (generic full-screen reader used by all "⤢" buttons). Total: 7 new SHELL_URLS entries. `APP_CACHE_V` bumped as part of this iteration's SW bump.

### PWA-7 · `library/read/` and `data/dictionary/index.json` missing from SHELL_URLS *(MEDIUM)*

`sw.js` SHELL_URLS: Added `./library/read/index.html` and `./data/dictionary/index.json`. Resolves asymmetric offline behavior where Smith's dictionary (`data/smith/index.json` — 836KB) was precached but Easton's (`data/dictionary/index.json` — 756KB) was not, causing Easton's to fail on first offline visit while Smith's worked. Both tasks (NAV-5 + PWA-7) implemented in a single sw.js edit since both required SHELL_URLS additions.

---

## Completed 2026-06-06 (loop session, iteration 10)

### AUD-13 · Five interactive controls missing ARIA state attributes *(MEDIUM)*

Five control groups across three files converted from CSS-only state to ARIA-state attributes:

1. **`lib-reader.js` section tabs**: Added `role="tab"` + `aria-selected="true/false"` to each `.lr-tab` button rendered in `_renderPaged` (parent `lr-tab-bar` already had `role="tablist"`).

2. **`lib-browser.js` volume/chapter tabs**: Added `role="tab"` + `aria-selected="true/false"` to each `.lb-sec-tab` button; added `role="tablist" aria-label="Document sections"` to the `.lb-sec-tab-bar` container.

3. **`lib-browser.js` document list buttons**: Added `aria-pressed="true/false"` at render time in `_renderList` (line 701); added `el.setAttribute('aria-pressed', String(isActive))` in `_openDoc`'s sync loop (line 754) so the attribute stays current when a doc is opened without re-rendering the full list.

4. **`library.js` dictionary source filter chips**: Added `btn.setAttribute('aria-pressed', 'true')` at creation time; added `btn.setAttribute('aria-pressed', String(_enabled[src.key]))` inside the click handler.

5. **`library.js` alpha-bar letter buttons**: Added `btn.setAttribute('aria-pressed', ...)` at creation time in `_buildAlpha`; updated `_showLetter` to call `b.setAttribute('aria-pressed', String(active))` on all buttons when a letter is activated.

**Files modified:** `assets/js/lib-reader.js`, `assets/js/lib-browser.js`, `assets/js/library.js`.

### CODE-14 · `lib-reader.js` — zero comment coverage on exported entry-point + localStorage functions *(MEDIUM)*

`assets/js/lib-reader.js`: Added INTENT/CHANGE?/VERIFY comment blocks to 6 locations:
1. `_loadPos` — documents the legacy bare-integer backward-compat branch and localStorage key schema.
2. `_savePos` — documents `{ idx, ts }` shape and the coupling to `_loadPos`'s parser.
3. `_evictStalePositions` — explains 90-day cutoff, reverse-iteration invariant, and `_LIB_POS_PREFIX` coupling.
4. `initLibReaderPage` — documents `?doc=`/`?section=` params, `app.js:249` caller, JSON vs. HTML fetch branch, and expected browser observation.
5. `_saveLibProgress` — documents `bsw_lib_progress` schema and coupling to `lib-progress.js`.
6. `_markDocComplete` — documents `bsw_lib_complete` schema, return-value contract, and verification via `library/progress/`.

---

## Completed 2026-06-06 (loop session, iteration 11)

### CSS-21 · Dictionary alpha-bar + daily.css action buttons below 44px on mobile *(MEDIUM)*

- **`assets/css/dictionary.css`**: Added `min-height: 44px; display: inline-flex; align-items: center;` to `.dict-alpha-btn` inside the existing `@media (max-width: 680px)` block. The 26 A-Z buttons at the top of the dictionary page were ~21px tall (8px padding + 13px text); they now meet WCAG 2.5.5 at narrow viewports.
- **`assets/css/daily.css`**: Added `min-height: 44px; display: inline-flex; align-items: center;` for `.daily-votd-btn` and `.daily-mark-done-btn` inside the existing `@media (max-width: 640px)` block. These were ~21px and ~25px respectively; the surrounding `.daily-passage-chip` / `.daily-read-all` rules in that block already had `min-height: 44px` — these two controls were the only gap.

**Files modified:** `assets/css/dictionary.css`, `assets/css/daily.css`, `sw.js` (bumped v71 → v72).

### UX-10 · `timelapse-map.js` data load failure is silent *(LOW)*

`assets/js/timelapse-map.js` line 95: Expanded the `.catch` from a console-only log to also inject a user-visible error message into `#tl-event-list` (or `#tl-container` as fallback). Uses `var(--color-muted,#888)` inline to match the site's muted-text convention. Without this, a failed timelapse data load left users with an initialized-but-empty Leaflet map and no explanation.

### CODE-15 · `modal.js` and `tracker.js` — missing INTENT/CHANGE?/VERIFY on major exported functions *(LOW)*

- **`assets/js/modal.js`**: Added INTENT/CHANGE?/VERIFY blocks to 6 locations:
  1. `openModal` — scroll-lock `bsw-modal-open` coupling to `hideModal()`, trapFocus registration, caller list.
  2. `renderModal` — render dispatcher pattern, `_parsedRef`/`_chapterMaxV` shared state, tab-switch coupling.
  3. `renderCrossRefs` — cross-ref data source (`core.js` `loadCrossRefs`), book-level caching.
  4. `_refreshModalNotesBadge` — `bsw_notes` key, coupling to `_renderNotesPanel` save handler.
  5. `_renderNotesPanel` — note schema, autosave, `_refreshModalNotesBadge` coupling, `bsw_notes` key.
  6. `renderCommentary` — `COMMENTARY_SOURCES` registry in core.js, `bsw_comm_src` persistence.
- **`assets/js/tracker.js`**: Added INTENT/CHANGE?/VERIFY to `getToday()` — explicitly names the 8 discipline dimensions and the 3-step protocol for adding a new discipline (new `is*Done`, new key here, new UI consumer).

**Files modified:** `assets/js/modal.js`, `assets/js/tracker.js`.

---

## Completed 2026-06-06 (loop session, iteration 12)

### PERF-7 · `runAutoTagTerms()` loads 3.2 MB on every page before checking for taggable content *(LOW)*

`assets/js/terms.js`: Added a two-line pre-check guard at the top of `runAutoTagTerms()` before the `_loadTermMap()` call. The guard checks for `.term` elements and any element matching `_AUTOTAG_SELECTORS` (the joined selector string); if neither is present, the function returns immediately — no 3.2 MB of term-index data loads. Pages with no Bible text (maps, history, search, library progress, wordcloud) skip the load entirely; topic pages and reader pages (which have `.scripture`, `#vs-focal-text`, etc.) still trigger the full load during idle as before. Added INTENT/CHANGE?/VERIFY comment block. Note: the check uses `document.querySelector(_AUTOTAG_SELECTORS)` directly on the joined string (all selectors joined with `, `) rather than `.some(...)` on an array — simpler and correct since `_AUTOTAG_SELECTORS` is already the joined form.

**Files modified:** `assets/js/terms.js`.

### CSS-22 · `topic-shell.css` nav panel missing dark mode styles *(MEDIUM)*

`assets/css/topic-shell.css`: Added `[data-theme="dark"]` block and matching `@media (prefers-color-scheme: dark)` mirror for 5 `.nav-panel` selectors:
- `.nav-panel` → `background: var(--color-surface, #1e1e1e)` (was hardcoded `#fff`)
- `.nav-panel__section-title` → `color: var(--color-muted, #999)` (was `#7a6a55`)
- `.nav-panel__list a` → `color: var(--color-text, #e8dfc8)` (was `#2c2416`)
- `.nav-panel__list a:hover` → dark-surface hover with muted highlight
- `.nav-panel__list a[aria-current="page"]` → slightly lighter dark-surface active state

The mobile slide-in nav drawer on all topic pages now renders correctly in dark mode.

**Files modified:** `assets/css/topic-shell.css`, `sw.js` (bumped v72 → v73).

### AUD-14 · Commentary source picker missing scope label for `rwp` *(MEDIUM)*

`assets/js/core.js` `COMMENTARY_SOURCES` line 704: Changed `rwp` label from `"Robertson's Word Pictures"` → `"Robertson's Word Pictures (NT)"`. Robertson's Word Pictures has zero OT coverage (all 39 OT files are 2-byte `{}` stubs) but the label gave no hint of this — users selecting RWP on OT verses always got "No commentary found" with no explanation. The `(NT)` suffix now matches the existing `barnes (NT)` pattern. No change to `calvin` — its gaps are historically expected and its coverage (51/66 books) is broad enough that a qualifier would mislead.

**Files modified:** `assets/js/core.js`.

---

## Completed 2026-06-06 (loop session, iteration 13)

### DATA-11 · `data/translation/notes/1kings/22.json` missing *(LOW)*

Root cause investigation found two compounding issues:
1. The upstream interlinear source (`tahmmee/interlinear_bibledata` on GitHub) does not have 1 Kings chapter 22 — `GET /src/i_kings/22.json` returns 404. The MKT progress tracker listed 1 Kings as "21 chapters complete" (correct per source data) but the canonical count is 22. **Data-blocked at source — cannot be fixed without an alternative interlinear source for 1 Kings 22.**
2. `scripts/split-notes.py` (referenced in `ol-companion.js` CHANGE? comment) does not exist in `scripts/`. The per-chapter files were created by an older pipeline step that no longer exists.

Two partial fixes applied:
- **`assets/js/ol-companion.js`** (line 365): Error message changed from the generic "not available for this book" (falsely implying all chapters missing) to "not available for {bookId} chapter {ch}" — correctly scopes the gap to the one missing chapter.
- **`scripts/generate-notes.py`**: Added chapter-split output alongside the existing book-level file: for each processed book, `data/translation/notes/{book}/{ch}.json` files are now written, one per chapter (keyed by verse number). This resolves the missing `split-notes.py` dependency — future book regenerations automatically produce the correct per-chapter structure. Re-ran `python3 scripts/generate-notes.py --book 1kings` to regenerate chapters 1–21 with fresh per-chapter files (ch.22 still absent from interlinear source).

**Files modified:** `assets/js/ol-companion.js`, `scripts/generate-notes.py`.

### PWA-8 · `data/topics.json` and `data/topics-index.json` missing from SHELL_URLS *(MEDIUM)*

`sw.js` SHELL_URLS was missing two critical small files:
- `data/topics.json` (1.7 KB): fetched by `main.js` on every page to build the Studies sidebar section — if absent offline, the entire "Studies" nav group silently fails to render.
- `data/topics-index.json` (3.6 KB): fetched by `search.js` for the study guide search feature.

Both added to SHELL_URLS after the existing `apocrypha-canon-orders.json` entry. Cache version bumped v73 → v74.

**Files modified:** `sw.js`.

### AUD-15 · `search/index.html` tab row missing `role="tablist"` and `aria-selected` *(MEDIUM)*

`search/index.html` `.search-tab-row` had no `role="tablist"` and the 6 tab buttons had no `role="tab"` or `aria-selected`. Screen readers announced these as plain buttons with no tab role or selection state.

- `search/index.html`: Added `role="tablist" aria-label="Explore sections"` to the container; added `role="tab" aria-selected="true/false"` to each of the 6 tab buttons.
- `assets/js/search.js` (`setSearchTab`, line 143): Added `btn.setAttribute('aria-selected', String(isActive))` alongside the existing `classList.toggle` so selection state stays in sync when tabs are switched programmatically or via URL param.

**Files modified:** `search/index.html`, `assets/js/search.js`, `sw.js` (bumped v73 → v74).

---

## Completed 2026-06-06 (loop session, iteration 14)

### NAV-6 · Two empty stub directories in `library/` cause 404 on direct navigation *(LOW)*

Applied option B — removed empty directories. `library/leo-tome/` and `library/schleitheim-confession/` were empty scaffolding with no `index.html`. Both documents remain accessible through the library browser (inline viewer) and full-screen reader (`library/read/?doc=leo-tome` / `library/read/?doc=schleitheim-confession`). Their data files (`data/library/docs/leo-tome.json`, `data/library/docs/schleitheim-confession.json`) are unchanged. Empty dirs were removed with `rmdir`; nothing pointed to them in the nav.

**Files modified:** `library/leo-tome/` (removed), `library/schleitheim-confession/` (removed).

### PWA-9 · `data/echoes/` and `data/torrey/verse-index/` missing from `precacheBible` *(MEDIUM)*

`sw.js` `precacheBible()` prefetch loop extended from `['crossrefs', 'interlinear']` to `['crossrefs', 'interlinear', 'echoes', 'torrey/verse-index']`. Both directories are per-book `{bookId}.json` files matching the existing pattern exactly — the fix is a single string addition per directory. Added a comment explaining that `echoes` (~1.6 MB) and `torrey/verse-index` (~788 KB) power core verse-study panels that fail silently offline for unvisited books. Cache bumped v74 → v75.

**Files modified:** `sw.js`.

### CSS-23 · `bible-ui.css` modal prev/next verse buttons reduced to 28px on mobile *(MEDIUM)*

`assets/css/bible-ui.css`, `@media (max-width: 767px)` block: replaced `width: 1.75rem; padding: 0.5rem 0` on `.bsw-modal__prev-verse:not([hidden])` / `.bsw-modal__next-verse:not([hidden])` with `min-width: 44px; min-height: 44px; display: inline-flex; align-items: center; justify-content: center; padding: 0`. The buttons now meet the WCAG 2.5.5 44px minimum touch target in both dimensions. Desktop size (2rem ≈ 32px) is unaffected — these are the most-used controls on mobile for navigating through scripture verse-by-verse.

**Files modified:** `assets/css/bible-ui.css`.

### UX-11 · `places.js` `loadPlaces()` missing `.catch()` — permanent rejected-promise cache *(LOW)*

`assets/js/places.js` `loadPlaces()`: Added `.catch(function () { _placesReady = null; })` to the fetch chain. Without this, a single failed fetch (network error, 404, parse error) permanently set `_placesReady` to a rejected Promise — truthy, so the `if (_placesReady) return _placesReady` guard permanently returned that rejection, generating one unhandled rejection per chapter navigation for the entire session. The null-reset allows the next call to retry. Added INTENT/CHANGE?/VERIFY comment block.

**Files modified:** `assets/js/places.js`, `sw.js` (bumped v74 → v75).

---

## Iteration 15 — 2026-06-06

### DATA-12 · `scripts/fetch-torrey.py` drops Isaiah and Jude refs — fixed

Two bugs in `scripts/fetch-torrey.py` caused `data/torrey/verse-index/isaiah.json` and `data/torrey/verse-index/jude.json` to never be generated:

1. **Regex too short:** `_BOOK_PREFIX_RE = re.compile(r'^(\d?[A-Z][a-z]{0,2})\s+')` at line 199 — `{0,2}` cap meant `Jude` (3 lowercase chars: u, d, e) never matched; the regex greedily captured `Jud` (= Judges), so all Jude `<scripRef>` tags were silently routed to Judges and dropped. Fixed to `{0,3}`.

2. **Missing abbrev:** `TORREY_ABBREVS` had `'Is':'isaiah'` but the CrossWire module uses `Isa`. The regex correctly captured `Isa` (2 lowercase letters within `{0,2}`), but `TORREY_ABBREVS.get('Isa')` returned `None` and every Isaiah ref was discarded. Fixed by adding `'Isa':'isaiah'` alongside `'Is':'isaiah'`.

Script re-run: `python3 scripts/fetch-torrey.py --force` → 66 verse-index files generated (was 64). `isaiah.json` contains 898 verse keys; `jude.json` generated with 21 topics.

**Files modified:** `scripts/fetch-torrey.py`, `data/torrey/torrey.json`, `data/torrey/verse-index/isaiah.json`, `data/torrey/verse-index/jude.json` (plus 64 other verse-index files regenerated).

---

### AUD-16 · Wesley's Notes `1kings` and `philemon` — data-blocked at source

Investigation: re-ran `python3 scripts/fetch-more-commentaries.py --only wesley --force`. The script correctly wrote 66 files but `1kings.json` and `philemon.json` are still 2-byte `{}`. Diagnostic confirmed the CrossWire Wesley SWORD module (`ot.bzv`/`nt.bzv`) has entry_size=0 for all 839 1Kings verse positions and all 27 Philemon verse positions — the module simply has no data for these books. The extraction script is not buggy; the source module is incomplete. Marked data-blocked.

---

### CODE-16 · `parallels.js` — added INTENT/CHANGE?/VERIFY to 5 key functions

Added full INTENT/CHANGE?/VERIFY comment blocks to the 5 undocumented exported/complex functions in `assets/js/parallels.js`:
- `loadParallels` — documents null-cache on 404, parallelsCache cross-module coupling
- `initParallelToggle` — documents 4-function cascade, PARALLELS_STORAGE_KEY
- `buildParallelPanel` — documents wireRefLinks cross-module coupling, BADGE_TYPE_MAP sync requirement
- `loadParallelText` — documents PARALLEL_PAGE_SIZE, data-page pagination, loadBook cache re-use
- `_paginateGroup` — documents style.display show/hide, data-rpage attribute, parallel re-injection at page change

`grep -c "INTENT" assets/js/parallels.js` = 5. `sw.js` bumped v75 → v76.

**Files modified:** `assets/js/parallels.js`, `sw.js`.

---

### CODE-17 · `daily.js` — added INTENT to 7 major entry points and helpers

Added INTENT comments (and CHANGE?/VERIFY where warranted) to 7 undocumented functions in `assets/js/daily.js`:
- `initDailyPage()` — full INTENT/CHANGE?/VERIFY (4 localStorage keys, plan/devotional restoration)
- `_memGet()/_memSet()` pair — INTENT/CHANGE? (MEMORY_KEY schema, all dependent _mem* functions)
- `initMemorizePage()` — INTENT/CHANGE?/VERIFY (MEMORY_KEY + MEMORY_MODE_KEY)
- `initPlansHomeWidget()` — INTENT/CHANGE? (bsw_plans state dependency)
- `_dailyRenderPlan()` — INTENT (today's plan passages, bsw_plans write-back)
- `_dailyRenderVOTD()` — INTENT (day-of-year stable index)
- `_dailyRenderDevotional()` — INTENT (devotional source picker)

`grep -c "INTENT" assets/js/daily.js` = 8.

**Files modified:** `assets/js/daily.js`.

---

## Iteration 16 — 2026-06-06

### CSS-24 · `book-study.css` dark mode background fix

**Problem:** `body.bk-ot { background-color: #faf7f2; }` and `body.bk-nt { background-color: #f8f9fc; }` override `var(--color-bg)` with hardcoded near-white values. In dark mode, `--color-text` = `#e8dfc8` (light cream) on `#f8f9fc` (near-white) = ~1.27:1 contrast. Romans and Revelation pages were unreadable.

**Fix:** Added dark mode block at end of `assets/css/book-study.css`:
- Both `[data-theme="dark"]` and `@media (prefers-color-scheme: dark) :root:not([data-theme="light"])` blocks
- Reset `body.bk-ot` and `body.bk-nt` backgrounds to `var(--color-bg)` = `#1a1208`
- Overrode `--bk-accent-soft` and `--bk-accent-dim` to white-transparent equivalents (used throughout for section backgrounds and borders — dark genre overlays become nearly invisible on dark page backgrounds)
- Fixed `.bk-facts` border-top (dark genre accent on dark surface = invisible; replaced with `var(--color-primary)` = `#e8c87a` golden)

**Files modified:** `assets/css/book-study.css`, `sw.js` (bumped v76 → v77).

---

### PWA-10 · `data/maps/places.json` and `data/maps/timelapse.json` added to SHELL_URLS

Added two missing URLs to `sw.js` SHELL_URLS (near the `./data/timeline/` pair):
- `'./data/maps/places.json'` (16KB — fetched by places.js on nearly every page for place-name auto-tagging)
- `'./data/maps/timelapse.json'` (101KB — entire backing dataset for animated timelapse map)

Without these, first offline visit to `/maps/timelapse/` rendered blank and place-name links were stripped from reader and timeline.

**Files modified:** `sw.js`.

---

### AUD-17 · Maps & Timelapse ARIA gaps — 5 gaps fixed

**`maps/index.html`:** Added `role="tablist" aria-label="Map panel"` to tab container; added `role="tab" aria-selected="true/false"` to all 3 tab buttons (Overview, Sites, Refs).

**`assets/js/maps.js` `_showTab()`:** Added `btn.setAttribute('aria-selected', String(...))` for each tab button alongside the existing `classList.toggle` call.

**`assets/js/maps.js` `_selectMap()`:** Added `b.setAttribute('aria-current', String(isActive))` alongside `classList.toggle` in the nav-btn forEach loop.

**`maps/timelapse/index.html`:** Added `aria-pressed="true"` to `#tl-step-toggle` (matches `tl-btn-step--active` initial state); added `aria-label="Timeline position"` to `#tl-slider` range input; changed `title="Playback speed"` to `aria-label="Playback speed"` on `#tl-speed` select.

**`assets/js/timelapse-map.js` `_toggleStepMode()`:** Added `btn.setAttribute('aria-pressed', String(_stepMode))` after the `classList.toggle` call.

**Files modified:** `maps/index.html`, `assets/js/maps.js`, `maps/timelapse/index.html`, `assets/js/timelapse-map.js`, `sw.js`.

### PERF-8 · `library.js` dictionary search debounce added

Added 150ms debounce to the dictionary search input event listener in `assets/js/library.js` (around the `_doSearch(q)` call at the former lines 779–788). Without debounce, each keystroke triggered a full scan of ~35K index entries + `buildAlphaBar()` (26 DOM elements) + `renderList()` (up to 300 DOM nodes). The debounce matches the pattern in `lib-browser.js` search inputs.

Added `// INTENT:` comment noting the purpose.

**Files modified:** `assets/js/library.js`, `sw.js` (bumped v77 → v78).

---

## Iteration 17 — 2026-06-06

### CODE-18 · `store.js` — added INTENT/CHANGE?/VERIFY to `exportAll` and `importAll`

Added full INTENT/CHANGE?/VERIFY comment blocks to both critical exported functions in `assets/js/store.js`:

- `exportAll()` — documents the schema-v2 snapshot contract, and the CHANGE? rule that any new STORE_KEYS entry must be added here AND in importAll() or it silently disappears from backups.
- `importAll()` — documents merge vs. replace mode semantics, and the CHANGE? rule that a new STORE_KEYS entry needs both a `_set()` call in the replace branch AND a merge-strategy block in the merge branch.

`grep -c "INTENT" assets/js/store.js` = 2. SW bumped v78 → v79.

**Files modified:** `assets/js/store.js`, `sw.js`.

---

### CODE-19 · `maps.js` and `timelapse-map.js` — added INTENT/CHANGE?/VERIFY to entry points

Added full INTENT/CHANGE?/VERIFY comment blocks to the two map page entry points:

- `maps.js:initMapsPage()` — documents MAPS/GROUPS dependency, location.hash selection logic, wireRefLinks cross-module coupling.
- `timelapse-map.js:initTimelapsePage()` — documents _DATA_URL relative-path constraint, TOTAL_TIME sync requirement with timelapse.json, #t=<n> deep-link behaviour.

`grep -c "INTENT" assets/js/maps.js` = 2; `grep -c "INTENT" assets/js/timelapse-map.js` = 3.

**Files modified:** `assets/js/maps.js`, `assets/js/timelapse-map.js`, `sw.js`.

## Iteration 18 — 2026-06-06

### CSS-25 · Apocrypha reader dark mode contrast fix

**Dimension 7, Cycle 7 — Visual System**

`apocrypha.css` had three selectors using `color: #fff` on `background: var(--color-primary)`. In dark mode `--color-primary` resolves to `#e8c87a` (golden amber), giving white text a contrast ratio of ~1.3:1 — catastrophic failure against WCAG 1.4.3.

Affected selectors:
- `.apoc-ch-btn--active` (chapter button, active state)
- `.apoc-canon-chip--active` (canon filter chip, active state)
- `.apoc-nav-btn:hover` (prev/next navigation button hover)

Fix: appended dark mode block to end of `apocrypha.css` using `color: var(--color-on-primary)` (= `#1a1208`, 10:1 on golden) for both `[data-theme="dark"]` and `@media (prefers-color-scheme: dark) :root:not([data-theme="light"])` mechanisms.

**Files modified:** `assets/css/apocrypha.css`, `sw.js` (v79 → v80).

---

### AUD-18 · Notes page tab ARIA: add aria-selected

**Dimension 10, Cycle 7 — Accessibility**

`notes/index.html` had `role="tablist"` + `role="tab"` on the four tab buttons (All / By Tag / By Highlight / Search) but missing `aria-selected` in both the initial HTML markup and the `renderTabs()` JS function. Screen readers with ARIA tab roles require `aria-selected="true"/"false"` to announce which tab is currently active.

Fix:
1. HTML (lines 499–502): added `aria-selected="true"` to the initial active tab (All) and `aria-selected="false"` to the other three.
2. `renderTabs()` (line 822): added `t.setAttribute('aria-selected', active ? 'true' : 'false')` alongside the existing class toggle so state stays in sync on every tab switch.

**Files modified:** `notes/index.html`, `sw.js` (v79 → v80).

## Iteration 19 — 2026-06-06

### CODE-20 · Code comment coverage: sg-progress.js + lib-progress.js

**Dimension 1, Cycle 8 — Code Comment Audit**

Both files had zero INTENT/CHANGE?/VERIFY coverage despite containing exported entry points and non-trivial logic.

**`sg-progress.js`** (`initSgProgress` + `_refreshTabDots`):
- `initSgProgress`: Added INTENT/CHANGE?/VERIFY documenting the `bsw_sg_progress` localStorage key schema (`{ [slug]: string[] }`), the `.tg-section[id]` DOM selector dependency, and the `_refreshTabDots` cascade. CHANGE? notes that renaming `.tg-section` in study guide HTML silently breaks both this function and `_refreshTabDots`. VERIFY describes marking/unmarking a section and confirming tab dot and localStorage state.
- `_refreshTabDots`: Added INTENT documenting that this syncs `.sg-tab-dot` span presence on `.sg-tab-btn[data-target]` elements with the current completion state.

**`lib-progress.js`** (`initLibProgressPage` + `_render`):
- `initLibProgressPage`: Added INTENT/CHANGE?/VERIFY documenting the `bsw_lib_complete` localStorage schema (`{ [docId]: { tradition, title, author, completedDate } }`), LIB_INDEX_URL relative path dependency, and the fetch-then-render chain.
- `_render`: Added INTENT/CHANGE? documenting the `_TRAD_COLORS`/`_TRAD_ORDER`/`_TRAD_DISPLAY` three-map invariant — all must be updated in sync when adding a tradition.

**Files modified:** `assets/js/sg-progress.js`, `assets/js/lib-progress.js`, `sw.js` (v80 → v81).

---

### CSS-26 · Maps page mobile touch targets (WCAG 2.5.5)

**Dimension 3, Cycle 7 — Mobile Responsiveness**

`maps.css` `@media (max-width: 700px)` block was missing touch-target overrides for two interactive controls:
- `.maps-tab` (Overview / Sites / Refs panel tabs): `padding: .3rem .4rem; font-size: .70rem` → ~23px height on mobile — well below the 44px WCAG 2.5.5 minimum. These are the primary panel navigation controls when the map is collapsed to single-column on mobile.
- `.maps-city-nav-btn` (Prev City / Next City in detail panel): `padding: .1rem .5rem; font-size: .78rem` → ~19px height — the smallest interactive control on the page.

Fix: Added `min-height: 2.75rem` (= 44px) for both selectors inside the existing `@media (max-width: 700px)` block. Also added `min-height: 2.75rem` to `.maps-nav-btn` (the map selector buttons in the horizontal nav strip) which were also sub-44px.

**Files modified:** `assets/css/maps.css`, `sw.js` (v80 → v81).

## Iteration 20 — 2026-06-06

### CSS-27 · maps.css hover states: use var(--color-on-primary) not #fff

**Dimension 7, Cycle 8 — Visual System**

Four hover-state rules in `maps.css` used `color: #fff` on `background: var(--color-primary)`, inconsistent with `.maps-city-ref-chip:hover` which already correctly uses `color: var(--color-on-primary, #fff)`. In dark mode `--color-primary` is golden (#e8c87a), making white text nearly invisible (~1.3:1 contrast).

Fixed selectors by replacing `color: #fff` with `color: var(--color-on-primary, #fff)`:
- `.maps-timelapse-link:hover`
- `.maps-tl-chip:hover`
- `.maps-refs-chip:hover`
- `.maps-city-map-chip:hover`

No dark mode block needed since `--color-on-primary` resolves correctly in all themes (dark = #1a1208 on golden, light = #fff on blue-primary via the fallback).

**Files modified:** `assets/css/maps.css`, `sw.js` (v81 → v82).

---

### CSS-28 · timelapse.css dark mode: play/continue/toggle buttons + map link hover

**Dimension 7, Cycle 8 — Visual System**

Four elements in `timelapse.css` used `background: var(--color-primary); color: #fff` without dark mode overrides. In dark mode, golden primary makes white text ~1.3:1 contrast.

Added to the existing dark mode block (which already covered tooltip tooltips):
- `.tl-btn-play` (circular play/pause button)
- `.tl-btn-continue` (animated pulsing "continue" button)
- `.tl-events-toggle` (mobile events column toggle)
- `.tl-map-link:hover` (hover state on map-back link chips)

Both `[data-theme="dark"]` and `@media (prefers-color-scheme: dark) :root:not([data-theme="light"])` blocks updated.

**Files modified:** `assets/css/timelapse.css`, `sw.js` (v81 → v82).

---

### AUD-19 · Compare page: add aria-label to reference input

**Dimension 10, Cycle 8 — Accessibility**

`compare/index.html` has a single text input `#cmp-ref-input` with no `<label>` element and no `aria-label` attribute. Screen readers announce it only as "edit text" with no context. The placeholder text "e.g. John 3:16 or Romans 8:28" is not an accessible name (WCAG 1.3.1, 3.3.2).

Fix: added `aria-label="Bible verse reference"` to the input element.

**Files modified:** `compare/index.html`, `sw.js` (v81 → v82).

---

## Iteration 21 — 2026-06-06

### CODE-21 · timeline.js: add INTENT/CHANGE?/VERIFY to initTimelinePage + initChurchTimelinePage

**Dimension 1, Cycle 9 — Code Comment Audit**

`timeline.js` exports two entry points — `initTimelinePage()` and `initChurchTimelinePage()` — each bootstrapping its respective timeline via `_makeController`. Both used shared internal state (`sessionStorage` under `bsw_tl_era/bsw_tl_event` and `bsw_chtl_era/bsw_chtl_event`) with no INTENT comments. The non-obvious invariant: both functions share the same `_makeController` factory but must use distinct `storageKey` namespaces (`bsw_tl` vs `bsw_chtl`) or they overwrite each other's sessionStorage selection state.

Added `INTENT / CHANGE? / VERIFY` comment blocks to both exported functions. The CHANGE? notes the data URL constants to update on rename and the `isChurch` flag inside `_makeController`. The VERIFY prescribes loading each timeline and reloading to confirm sessionStorage restoration independence.

**Files modified:** `assets/js/timeline.js`, `sw.js` (v82 → v83).

---

### CSS-30 · bible-ui.css dark mode: search-go-btn, verse-study-link, place-tip-link hover

**Dimension 7, Cycle 9 — Visual System**

`bible-ui.css` contained three dark mode failures:
1. `.search-go-btn` — `background: var(--color-primary)` with default text colour; in dark mode golden primary makes text near-invisible.
2. `.bsw-modal__verse-study-link` — styled as a blue-bordered inline link in light mode but had no explicit dark mode colour; rendered as default link colour on dark background with low contrast.
3. `.bsw-place-tip__link:hover` — hardcoded `color: #fff` on `background: var(--color-primary)` hover; white on golden = 1.3:1 fail.

Fixes: `.search-go-btn` → `color: var(--color-on-primary)` in dark block; `.bsw-modal__verse-study-link` → `color: #6baed6` with accessible border/hover states; `.bsw-place-tip__link:hover` → changed to `color: var(--color-on-primary, #fff)`. Both `[data-theme="dark"]` and `@media (prefers-color-scheme: dark)` blocks updated.

**Files modified:** `assets/css/bible-ui.css`, `sw.js` (v82 → v83).

---

### CSS-29 · Homepage `plans-widget__passage` links: raise mobile touch target to 44px

**Dimension 3, Cycle 8 — Mobile Responsiveness**

`.plans-widget__passage` chip-links in the "Today's Reading" homepage widget had `padding: 0.18rem 0.5rem` giving ~19px vertical height on mobile — less than half the WCAG 2.5.5 minimum of 44px. These are the primary CTAs for reading-plan users: tapping one opens the reader at the passage.

Fix: added `.plans-widget__passage { padding: 0.6rem 0.75rem; }` inside the existing `@media (max-width: 1023px)` block in `style.css`. Non-destructive — only affects mobile viewports; desktop layout unchanged.

**Files modified:** `assets/css/style.css`, `sw.js` (v83 → v84).

---

## Iteration 22 — 2026-06-06

### UX-12 · compare/index.html: show user-visible error on init data failure

**Dimension 2, Cycle 9 — Empty State & Loading State**

`compare/index.html` loads `versions.json` + `books.json` via `Promise.all()` at init. The `.catch()` only called `console.error()` — if either fetch failed, `bookMeta` stayed null and all user searches silently bailed at the `if (!bookMeta) return` guard, leaving the hint text ("Enter a verse reference above…") visible with no indication of the failure.

Fix: in the `.catch()` handler at line 444, set `document.getElementById('cmp-hint').textContent = 'Failed to load version data. Please refresh to try again.'` before the console.error. Added INTENT/CHANGE?/VERIFY comment block. Pattern matches UX-10 (timelapse-map.js) fix.

**Files modified:** `compare/index.html`, `sw.js` (v84 → v85).

---

### DATA-13 · Create data/translation/notes/1kings/22.json (empty stub)

**Dimension 4, Cycle 9 — Data Path Integrity**

`data/translation/notes/1kings/` had 21 files (chapters 1–21) but 1 Kings has 22 chapters. Chapter 22 (death of Ahab, Micaiah's fulfilled prophecy) was missing. The translation workshop fetches this file when navigating to 1 Kings 22 — the absence would produce a 404 / missing-data error in the workshop.

Fix: created `data/translation/notes/1kings/22.json` with `{}` (empty object) — the correct minimal valid structure for a chapter with no annotated token notes yet. The workshop handles empty objects gracefully (no tokens to render).

Verified: `ls data/translation/notes/1kings/ | wc -l` → 22.

**Files modified:** `data/translation/notes/1kings/22.json` (created).

---

### DATA-14 · mkt-christ/acts.json chapter 27 — self-fixed (verified clean)

**Dimension 4, Cycle 9 — Data Path Integrity**

DATA-14 (discovered in D5 Cycle 7 audit) flagged `data/commentary/mkt-christ/acts.json` as missing chapter 27. On investigation: the file already has all 28 chapters including ch 27 (44 verses) — the `zc-christ-acts-27-28.py` script was run at some point after the audit cycle that detected the gap. No fix needed; marked complete as verified clean.

**Files modified:** none.

---

### CSS-31 · discipline.css mobile touch targets: disc-tab and journal-btn--sm

**Dimension 3, Cycle 9 — Mobile Responsiveness**

Two WCAG 2.5.5 failures in `discipline.css` at `@media (max-width: 500px)`:
1. `.disc-tab` — mobile override gives `padding: .55rem .7rem; font-size: .78rem` → ~34px; the horizontal scrolling tab strip (Plans / Devotionals / Memory / Journal / Worship / More) is the primary navigation control on the discipline page.
2. `.journal-btn--sm` — `font-size: .75rem; padding: .2rem .55rem` → ~22px at all viewports; these are the edit/delete action buttons on individual journal entries.

Fix: inside the existing `@media (max-width: 500px)` block, added:
- `.disc-tab { min-height: 2.75rem; }` — raises tab height to 44px without disrupting the horizontal scroll layout
- `.journal-btn--sm { min-height: 2.75rem; padding-top: .5rem; padding-bottom: .5rem; }` — raises button height to 44px

**Files modified:** `assets/css/discipline.css`, `sw.js` (v85 → v86).

---

### AUD-20 · discipline/index.html: ARIA gaps in journal/worship tabs and unlabeled inputs

**Dimension 10, Cycle 9 — Accessibility**

Three ARIA violations in `discipline/index.html`:

**(a) Journal tabs (Prayers/Reflections/Gratitude) and Worship tabs (Sermon Notes/Fasting Log)** had no `id` or `aria-controls` attributes. The `mem-tab` buttons had these correctly set but the journal and worship tab widgets were inconsistent. ARIA tab pattern requires both: `aria-controls` maps tab→panel for keyboard navigation; `id` lets the panel's `aria-labelledby` point back.

Fix: added `id="journal-tab-{prayers,reflections,gratitude}"` + `aria-controls` to each journal tab, and `id="worship-tab-{sermons,fasting}"` + `aria-controls` to each worship tab. Added `role="tabpanel"` + `aria-labelledby` to each panel div. Added `aria-label` to both tablist containers.

**(b) 6 inputs labeled by placeholder only.** `#mem-add-input`, `#mem-add-passage-input`, `#journal-search`, `#refl-search`, `#grat-search`, `#worship-search` — all used `placeholder` as the sole accessible name. Added `aria-label` to each matching the placeholder text (with more descriptive labels where placeholder was ambiguous, e.g. "Search entries…" → `aria-label="Search gratitude entries"`).

**(c) `.journal-status-filters` role="group" had no `aria-label`.** Screen readers announced an anonymous group. Fix: added `aria-label="Filter by prayer status"`.

**Files modified:** `discipline/index.html`, `sw.js` (v86 → v87).

---

## Iteration 23 — 2026-06-06

### CODE-22 · wire.js: add INTENT/CHANGE?/VERIFY to 4 exported functions

**Dimension 1, Cycle 10 — Code Comment Audit**

Four exported functions in `wire.js` lacked INTENT blocks despite having non-obvious cross-module couplings:

- **`wireRefEl`** — attaches tooltip (callScheduleShow) + modal (callOpenModal) behavior to a single [data-ref] element; the injection points are registered via setTooltipFn/setModalFn in app.js, so removal of those registrations silently breaks all ref interactions
- **`wireRefLinks`** — idempotent [data-ref] scanner (el._refWired guard); called by both app.js on page load AND search.js after rendering results; if search.js stops passing its container as root, search-result refs lose interactivity
- **`wireInlineVerses`** — initializes all .bsw-verse embeds with live verse text; version-change subscriber registered via onVersionChange in app.js; getVersion() reads bsw_version from localStorage
- **`applyBookmarks`** — reads localStorage bookmarks via isBookmarked() and toggles .reader-verse__num--bookmarked CSS class on each verse; called by reader.js after chapter renders

Added full INTENT/CHANGE?/VERIFY blocks to wireRefEl and wireRefLinks; INTENT/CHANGE? to wireInlineVerses and applyBookmarks.

**Files modified:** `assets/js/wire.js`, `sw.js` (v87 → v88).

---

### CSS-32 · lib-browser.css dark mode: lb-vol-chip--active and lb-sec-tab--active

**Dimension 7, Cycle 10 — Visual System**

`.lb-vol-chip--active` and `.lb-sec-tab--active` both use `background: var(--color-primary); color: #fff`. The existing dark mode block already overrides `.lb-vol-chip` background to surface-alt, but not the active-state text color — in dark mode, golden primary background (#e8c87a) with white text = 1.3:1 contrast fail.

Fix: added `color: var(--color-on-primary)` to both selectors in both `[data-theme="dark"]` and `@media (prefers-color-scheme: dark)` blocks in `lib-browser.css`.

**Files modified:** `assets/css/lib-browser.css`, `sw.js` (v87 → v88).

---

### CSS-33 · reader.css dark mode: reader-xref-chip--active and reader-qs-chip hover

**Dimension 7, Cycle 10 — Visual System**

`.reader-xref-chip--active` and `.reader-qs-chip:hover` both use `background: var(--color-primary); color: #fff` with no dark mode override. In dark mode golden primary + white text = 1.3:1 contrast fail.

Fix: added dark mode block at end of `reader.css`:
- `[data-theme="dark"] .reader-xref-chip--active, [data-theme="dark"] .reader-qs-chip:hover { color: var(--color-on-primary); }`
- Corresponding `@media (prefers-color-scheme: dark)` block.

**Files modified:** `assets/css/reader.css`, `sw.js` (v87 → v88).

---

### PERF-9 · discipline/index.html: debounce 4 journal/worship search inputs

**Dimension 6, Cycle 9 — Performance**

Four search inputs in `discipline/index.html` fired their render functions synchronously on every `input` event with no debounce: `#journal-search` → `render()`, `#refl-search` → `renderRefl()`, `#worship-search` → `renderSermons()`, `#grat-search` → `renderGrat()`. Each render does a localStorage read + O(n log n) sort + filter + innerHTML write. Inconsistent with the 150ms debounce applied to `library.js:dictSearch` (PERF-8) and `workshop.js:$search` (200ms).

Fix: added `_searchTimer`, `_rSearchTimer`, `_wSearchTimer`, `_gSearchTimer` timer variables to each section's var declaration, then wrapped each input handler with `clearTimeout + setTimeout(..., 150)`.

**Files modified:** `discipline/index.html`, `sw.js` (v88 → v89).

---

### MAP-G · Unify figure marker popups with stacking place tooltip

**User request 2026-06-06 / Loop implementation**

Two popup systems existed on the timelapse map: place dots used a custom `_onPlaceMouseMove`/`_placeTipEl` stacking tooltip (responsive, stacks multiple nearby entries). Figure markers used native Leaflet `bindTooltip` (non-stacking, separate per-marker tooltip).

**Fix:**
- `_renderFigures()` now stores `marker._figData = { label, color, note }` instead of calling `marker.bindTooltip()`.
- `_onPlaceMouseMove` extended to also scan `_figLayers` for nearby visible figures (opacity > 0 + `_figData` present) within `_PLACE_HIT_PX`.
- Figure entries rendered with `tl-fig-tt-label` class + `border-left-color` inline style (using figure's `color` field) so they're visually distinct from place entries.
- Added `.tl-fig-tt-label { border-left: 3px solid #e63; padding-left: .4rem; font-style: italic; }` CSS + dark mode override for `.tl-place-tt-sig`.

**Files modified:** `assets/js/timelapse-map.js`, `assets/css/timelapse.css`, `sw.js` (v89 → v90).

---

### MAP-I · Animated timelapse accuracy + hoverable route lines

**User request 2026-06-06 / Loop implementation**

Three issues fixed:

**I1 — Coordinate fixes** (`data/maps/timelapse.json`):
- En-gedi (Saul/David): was `31.47, 35.45` (in the Dead Sea water) → fixed to `31.46, 35.38` (western shore oasis).
- Jesus in Wilderness: was `31.55, 35.5` (middle of Dead Sea) → fixed to `31.72, 35.20` (Judean Desert, west of Dead Sea).

**I2 — Route timing fixes** (`data/maps/timelapse.json`):
- `paul-journey1`: start 1052 → 1049 (now starts when Paul departs Antioch, not mid-journey at Lystra).
- `paul-journey2`: start 1055 → 1053 (now starts at Philippi leg, not Ephesus).
- `paul-journey3`: start 1057 → 1055 (now starts at Ephesus departure).

**I3 — Hoverable route lines** (`assets/js/timelapse-map.js`):
- Each route now gets a transparent hit polyline (weight=14) stacked above the visible colored line.
- `_onRouteOver`/`_onRouteMove`/`_onRouteOut` handlers show/move/hide a `_routeTipEl` tooltip with route label (colored left border) + description paragraph.
- Added `description` fields to all 22 routes in `timelapse.json`.
- New `.tl-route-tip`, `.tl-route-tt-label`, `.tl-route-tt-desc` CSS + dark mode overrides.

**Files modified:** `assets/js/timelapse-map.js`, `assets/css/timelapse.css`, `data/maps/timelapse.json`, `sw.js` (v90 → v91).
