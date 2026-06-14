# Bible Study Website — Working TODO

Track progress here. Mark items `[x]` when complete.
Completed items are archived in `working/todo-archive.md`.

---

*Long-running agent loop tasks tracked separately — see `working/TODO-Loops.md`.*

---

## Three-Tier Study Content System (TRB)

*Planned 2026-06-07. Three tiers per book: Book Guide (orientation + study questions), Deep Dive (scholarly analysis), Wide Source Commentary (per-verse synthesis from classic commentators). Replaces the unsustainable flat nav approach with a Studies hub page. Phases A, B, D, and C1 complete — see working/todo-archive.md (2026-06-10 cleanup pass).*

### Phase C — First Synthesis Commentary (WS loop)

- [ ] **TRB-C2 Proof-of-concept: Hebrews 1–4** — Run `WS_AGENT_PROMPT.md` loop for first unit (`ws-synthesis-hebrews-1-4.py`). Verify `data/commentary/synthesis/hebrews.json` chapters 1–4 fully covered.

- [ ] **TRB-C3 `topics/hebrews/commentary.html`** — Create Tier 3 display page for Hebrews. Loads `data/commentary/synthesis/hebrews.json` lazily by chapter. Each verse entry renders `synthesis` paragraph above a `<details>` element for the `voices` array. Add tier nav strip (Commentary active, Guide → `study-guides/hebrews/`, Deep Dive greyed until TRB-D1).

- [ ] **TRB-C4 Register `synthesis` in `core.js`** — Add `{ id: 'synthesis', label: 'Classic Voices (Synthesis)', attr: 'Synthesis of Calvin, Matthew Henry, Ellicott, JFB, Clarke, and Wesley' }` to `COMMENTARY_SOURCES`. Add branch in reader's commentary render: when `source === 'synthesis'`, render `entry.synthesis` as displayed HTML and append `<details>` for `entry.voices`.

- [ ] **TRB-C5 Update `books-content.json` for Hebrews commentary** — Set `hebrews.commentary.exists=true`, `coverage="partial"`, `chapters_done=[1,2,3,4]`. Verify reader banner shows commentary link when navigating Hebrews chapters 1–4.

---

## Workshop UX & Source Data — Bug Fixes (SW-Q)

*Identified 2026-06-07 via full workshop audit. Three hard bugs, four medium UX issues, three source-data pipeline gaps. Hard bugs (Q1–Q3) and medium UX issues (Q4–Q7) complete — see working/todo-archive.md (2026-06-10 cleanup pass).*

### Source Data Pipelines (scripts exist, need running or building)

- [ ] **SW-Q8 `attested_uses` pipeline** — 0/400 entries across phase1+phase2 have verse samples. This is the "evidence-first" foundation of the dossier design. Build or run a script that populates 3–5 verse samples per word from the interlinear data. Output: `{ ref, text, context, note }` array on each glossary entry.

- [ ] **SW-Q9 `lxx_bridge` expansion** — Only 13/200 Hebrew phase2 entries have LXX bridge data. The `_renderLxxBridge()` function is complete. Build a script that reads the LXX interlinear (or a mapping file) to find which Greek Strong's codes render each Hebrew code, and populate `lxx_bridge: [{ greek_code, greek_lemma, frequency, note }]` on the remaining 187 entries.

- [ ] **SW-Q10 `extrabiblical_uses` pipeline** — 0/400 entries have papyri/secular-Koine attestations. The `_renderExtrabib()` function is complete. Populate from a Moulton–Milligan source or curated dataset for at least the top-50 Greek words by NT frequency.

---

## Workshop — File Structure & Modularity (SW-S)

*workshop.js is 5,177 lines. As new features are added it must be split to stay maintainable. Split along mode boundaries so each file is independently readable. CSS follows the same split.*

- [ ] **SW-S1 Split workshop.js into modules** — Extract into:
  - `assets/js/workshop-core.js` — state variables, localStorage helpers, `_getEntry()`, `_openWord()`, `initWorkshopPage()`, mode-switching, flashcard system, URL param handling
  - `assets/js/workshop-verse.js` — `_studyPassage()`, `_renderPassageTiles()`, `_renderPassageNoticeBanner()`, `_renderPassageIdioms()`, all passage tab renderers (`_renderLiteraryTab`, `_renderCulturalTab`, `_renderOTinNTPanel`, `_renderSynthesisTab`, `_renderCrossRefsTab`, `_renderCommentaryTab`, `_renderGrammarRulesTab`)
  - `assets/js/workshop-word.js` — `_renderWordStudyPanel()`, `_renderLexicalSourcesSection()`, `_renderDictResults()`, `_initDictPanel()`, `_runDictSearch()`, all dossier section renderers (`_renderGrammarSection`, `_renderDebateSection`, `_renderIdiomAlertSection`, `_renderCognateSection`, `_renderSemanticSection`, `_renderAuthorFreqSection`, `_renderSTContext`, `_renderAttestedUses`, `_renderExtrabib`, `_renderLxxBridge`)
  - `assets/js/workshop-book.js` — `_renderBookStudy()`, `_renderBookTab()`, `_initBookStudyPanel()`, `_bookLang()`
  - `assets/js/workshop-dossier.js` — `_renderDossier()`, `_renderBookDistribution()`, `_renderBookDefaults()`, `_renderTiersView()`, action handlers (`_handleAction`, `_showOverrideForm`, etc.)
  - Each module imports from `workshop-core.js` and `./core.js`; `workshop-core.js` dynamically imports the others on demand
- [ ] **SW-S2 Split workshop.css** — Extract into:
  - `workshop-base.css` — page shell, topbar, loading, mode bar, layout grid
  - `workshop-verse.css` — tiles, passage entry, tabs, notice banner, idiom panel, particle colors
  - `workshop-word.css` — word study panel, dictionary panel, lexical source cards, dossier sections
  - `workshop-book.css` — book study panel, book tabs, term rows, idiom rows
  - `workshop-flashcard.css` — flashcard view, SRS rating buttons
  - `workshop.css` becomes a single-file `@import` aggregator (or load all from index.html)
- [ ] **SW-S3 Data file convention** — All new workshop data goes in dedicated subdirectories: `data/workshop/grammar-notes/`, `data/workshop/book-study/`. Nothing appended to existing phase1/phase2 JSON without a migration plan.

---

## Workshop — Word Study Redesign (SW-U)

*Word Study is currently a simplified dossier + book-limited concordance. Needs to be the deepest single-word resource on the site. SW-U1, U2, U5 complete — see working/todo-archive.md (2026-06-10 cleanup pass).*

- [ ] **SW-U3 Translation variation counts** — New section "Translation Renderings" in word detail. For each word, compute (or store) how many times each English gloss variant appears across the interlinear data. Format: `love (92×) · charity (KJV, 26×) · beloved (3×)`. Source: scan `data/interlinear/` for all tokens matching this Strong's code and tally the `text` field. This should be pre-computed by a build script (`scripts/build-translation-variants.py`) outputting `data/grammar/translation-variants-greek.json` and `translation-variants-hebrew.json` keyed by Strong's code. Render in word detail as a compact chip row.

- [ ] **SW-U4 Full cross-book concordance** — Replace the "occurrences in current book" right column with a full scripture concordance. On word open, load all interlinear books for that language lazily (or use a pre-built verse-index keyed by Strong's code). Show results as a searchable list: ref · verse gloss with the target word highlighted in `<em>`. Filter bar: by Testament (OT/NT), by book group (Pauline, Wisdom, Prophets…), by author. Clicking a verse opens it in verse study mode. Cap initial render at 50 results with "load more." Pre-build script: `scripts/build-strongs-concordance.py` → `data/grammar/concordance-greek.json` + `concordance-hebrew.json` keyed by Strong's code → `[{ ref, bookId, ch, v, gloss }]`. These files will be large (~15MB each) so stream/paginate on load.

---

### Z6–Z8 — Commentary Agent Generation

- [ ] Agents generate `data/commentary/mkt-original/{book}.json` via `zc-original-{book}-*.py` (NT first, start John + Romans)
- [ ] Agents generate `data/commentary/mkt-context/{book}.json` via `zc-context-{book}-*.py` (NT first)
- [ ] Agents generate `data/commentary/mkt-christ/{book}.json` via `zc-christ-{book}-*.py` (NT first)

### Script naming convention
`scripts/zc-{type}-{book}-{start}-{end}.py`
Examples: `zc-original-john-1-5.py`, `zc-context-romans-1-8.py`, `zc-christ-genesis-1-10.py`, `zc-echo-john-1-5.py`

### Data outputs
- `data/echoes/` — typed echo layer per book
- `data/commentary/mkt-original/` — Original Language commentary per book
- `data/commentary/mkt-context/` — Context commentary per book
- `data/commentary/mkt-christ/` — Christological commentary per book
- `data/translation/term-commentary.json` — ~100 high-dispute term decision notes

### Verification
- verse-study John 3:16 → all 3 new MKT sources in commentary picker
- verse-study John 1:29 → Echoes panel shows Exod 12 type + Isa 53:7 allusion
- `tools/terms/index.html` → G4102 πίστις decision note with tradition map
- No regressions: existing commentaries (mhcc, jfb, etc.) still load

---

## Word Study Page Improvements

*(WD-L and WD-M claimed — see working/inprogress-wd-lm-todo.md)*

---

## Library Content Cleanup — LOW items remaining

Completed sections archived. Newman Apologia and Smalcald Articles polish items also complete — see working/todo-archive.md (2026-06-10 cleanup pass).

*(Pascal Pensées claimed — see working/inprogress-pascal-pensees-todo.md)*

---

## Bible Reader Improvements

**Evaluation (2026-06-03):**

The reader is feature-rich — multi-ref lookup, book introductions, compare mode, interlinear,
parallels, three right-panel tabs, six layout modes — but several implementation problems
undercut the experience. The most serious is a split navigation model: sidebar chapter buttons
use in-page rendering while prev/next chapter buttons do a full `window.location.href` page
reload. The toolbar is also severely overcrowded. Below items are roughly priority-ordered.

---

*(RD-I claimed — see working/inprogress-rdm-todo.md)*

---

*(RD-M claimed — see working/inprogress-rdm-todo.md)*

---

## Verse Study Page Improvements

*(Claimed — see working/inprogress-vs-todo.md)*

---

## Reference Data Expansion

New commentary sources, dictionary upgrades, and one index that can be built from data
already on the site.

---

*(REF-E · DATA BLOCKED — Gill.zip not in CrossWire rawzip or mods.d; see working/inprogress-ref-e-gill-todo.md for details)*

---

*(REF-F claimed — see working/inprogress-ref-f-isbe-todo.md)*

---

## Phase B — Competitive Parity

*(B4a claimed — see working/inprogress-b4a-pwa-todo.md)*

---

## Library Expansion — Pending

*(Bonaventure Itinerarium claimed — see working/inprogress-bonaventure-todo.md)*

- [ ] **Melanchthon, Loci Communes (1521)** — **DATA BLOCKED**: All English translations (Hill 1944, Manschreck 1965) are under copyright. No public domain English translation exists.

*(Missions & biography works claimed — see working/inprogress-missions-bio-todo.md)*

*(Apologetics texts claimed — see working/inprogress-lib-apologetics-todo.md)*

*(Creeds & Confessions expansion claimed — see working/inprogress-lib-creeds-todo.md)*

*(Liturgical & church-order documents claimed — see working/inprogress-liturgical-docs-todo.md)*

*(Papal encyclicals claimed — see working/inprogress-papal-encyclicals-todo.md)*

---

## Maps Page Improvements

### Phase 1 — UX & Structure *(complete)*
All Phase 1 items are implemented: `ERA_GROUPS` drives nav section headers; `_buildNav()` renders group labels; `_selectMap()` has URL hash deep-linking; `_overviewHtml()` renders the overview panel; `_showCityDetail()` handles the `significance` field; city-detail panel is an `position:absolute` overlay; reset button is wired via `_wireResetButton()`. All CSS present.

---

## Home Page Improvements

---

## Site Navigation Consolidation

The site has grown to ~20 top-level routes. Most are small single-purpose pages that end up
buried in the sidebar and forgotten. The pattern already proven by the discipline hub — a sticky
tab bar, lazy iframe loading with `?minimal=1`, and each sub-page still working standalone — can
be applied across the rest of the site to collapse those 20 routes into ~6 hub destinations.

**Target nav structure after all CON work:**

| Hub | Tabs |
|-----|------|
| **Holy Bible** (`read/`) | Read · Compare · Bookmarks |
| **Explore** (`search/`) | Search · Topics · Study Guides · Dictionary |
| **History** (`history/`) | Biblical Timeline · Church History · Maps · Animated Map |
| **Library** (`library/`) | unchanged (Browse + Reading History + subgroups) |
| **Discipline** (`discipline/`) | Plans · Devotionals · Memory · Journal · Worship · Gratitude · History · (Notes · Progress in More ▾) |
| **Home** (`/`) | unchanged — daily dashboard |

The Reference nav group dissolves entirely: Timeline and Maps move to History, Dictionary moves
to Explore, Notes and Progress move to Discipline (D-B/D-C). Word Cloud moves under Explore.
Church History moves from Library → History.

**Shared implementation pattern for all CON hubs:**

All inter-page embedding uses the `?minimal=1` mechanism from D-F: each embedded page suppresses
its sidebar and shows a back-link. Iframe `src` is set to `""` initially and only assigned when the
tab is first activated (lazy load). Each embedded page continues to work standalone at its original URL.

---

*(CON-B claimed — see working/inprogress-con-b-reader-hub-todo.md)*

---

*(CON-C claimed — see working/inprogress-con-c-todo.md)*

---

*(CON-D claimed — see working/inprogress-con-d-todo.md)*

---

*(CON-E claimed — see working/inprogress-con-e-todo.md)*

---

*(PB-A, PB-B, PB-C claimed — see working/inprogress-pb-todo.md)*

---

## Discipline Section Expansion

*(Claimed — see working/inprogress-discipline-d-todo.md)*

---

## Phase O — Long-term / Deferred *(stub phase — intentionally deprioritised)*

These items have been identified but are intentionally deferred. They require significant
research, have unclear scope, or are likely out of scope for a personal static-site project.
Recorded here so they are not forgotten, but none should be started without deliberate
re-evaluation.

- [ ] **O1. Audio support for memory verses** *(stub — deferred)*
  - TTS integration or royalty-free audio recordings for Scripture memory (C4) so verses can
    be heard while commuting; no clear path on a static site without a TTS API dependency

- [ ] **O2. Apocrypha / deuterocanonical books** *(promoted — see dedicated section below)*

- [ ] **O3. MKT print / ePub edition** *(stub — deferred)*
  - Generating a full three-tier MKT as a downloadable PDF or ePub; significant formatting
    work with unclear demand for a personal study tool

- [ ] **O4. Social sharing beyond verse image cards** *(stub — deferred)*
  - Shareable verse links, QR codes, and embed codes; may belong here if the site remains
    personal, or in Phase N if broader readership becomes a goal

- [ ] **O5. `bible.js` unit test suite** *(stub — deferred)*
  - A Jest or Vitest test suite for core functions (ref parsing, search, modal logic,
    localStorage handling); low urgency while the site has one author who can manually verify;
    revisit if the codebase grows or contributors are added

- [ ] **O6. Internationalisation of UI chrome** *(stub — deferred, see L3)*
  - All button labels, headings, and status messages are hardcoded English; i18n would require
    a locale file system and ongoing translation maintenance

---

## Phase Z — Modern Kingdom Translation (MKT) *(long-term / exploratory)*

*(MKT NT continuation claimed — see working/inprogress-mkt-todo.md)*

---

## Maps System Improvements

Two-part system: **static thematic maps** (`maps/index.html` + `assets/js/maps.js`) and the
**animated time-lapse** (`maps/timelapse/` + `assets/js/timelapse-map.js`). The systems are
complementary — spatial reference vs. temporal narrative — but currently disconnected and each
has gaps.

**Key files:**
- `assets/js/maps.js` — 14 static maps, all data inline (144KB, 1,894 lines)
- `assets/js/timelapse-map.js` — animation engine, reads `data/maps/timelapse.json`
- `data/maps/timelapse.json` — empire, route, figure, event, tribe, place data
- `assets/css/maps.css` / `assets/css/timelapse.css`
- `maps/index.html` / `maps/timelapse/index.html`

---

*(MAP-F claimed — see working/inprogress-map-f-todo.md)*

---

### MAP-H — Popup dot color scheme: visually identify entry type at a glance

**Context:** The user asked for subtle colors to identify popup entry types. Currently place
entries and figure entries share the same plain text style (place dots are all blue; figure
entries now have a colored border from MAP-G, but the dot colors on the map itself are
inconsistent).

**Tasks:**
- [ ] **H1 — Map dot accent colors:** Review current dot colors and add a consistent
  scheme: place dots (blue `#4a90d9`), figure markers (amber/warm color from figure's
  `color` field), tribe dots (existing translucent fill).
- [ ] **H2 — Tooltip type badge:** Add a tiny `PLACE` / `PERSON` chip to each entry in
  the stacking tooltip. Style: small, uppercase, muted. Blue tone for place, amber for person.
- [ ] **H3 — Dark mode** for the new type-badge chips.

---

### MAP-I — Animated timelapse accuracy pass

**Context:** The user reported (2026-06-06) that several coordinates are wrong (Jesus in
the Wilderness looks like he's in the Dead Sea), route lines appear at the wrong time,
and figure/journey lines are not hoverable to show what they represent.

- [ ] **I4 — Empire/route coords deeper audit**: Beyond En-gedi/Wilderness, verify
  Exodus route waypoints through Sinai Peninsula, Abraham Ur→Haran→Canaan arc, and
  Assyrian/Babylonian campaign paths against biblical atlas references.

**Files:** `data/maps/timelapse.json`, `assets/js/timelapse-map.js`, `assets/css/timelapse.css`

---

## Word Cloud — Post-Shipping Improvements

---

*(Studies SG-A through SG-I claimed — see working/inprogress-studies-sg-todo.md)*

---

*(CMT-A through CMT-I claimed — see working/inprogress-cmt-todo.md)*

---

## Code Comment Audit — Dimension 1

*Audit pass 2026-06-05. Files missing required INTENT/CHANGE?/VERIFY comments on exported functions,
localStorage write paths, algorithms, and cross-module couplings.*

---

## Empty State & Loading State Audit — Dimension 2

*Audit pass 2026-06-05. Pages and panels with missing error feedback on fetch failure or empty data.*

---

## Mobile Responsiveness Audit — Dimension 3

*Audit pass 2026-06-05. CSS code-reading audit — no browser DevTools available; findings based on media-query analysis and layout calculations.*

---

## Data Path Integrity Audit — Dimension 4

*Audit pass 2026-06-05. Verified fetch paths against actual files in `data/`. All commentary sources (mhcc, ellicott, jfb, clarke, calvin, barnes, rwp, wesley) have all 66 books. Crossrefs, echoes, interlinear all have full 66-book coverage. Plans, library docs, manifest shortcuts, SHELL_URLS in sw.js, and all main nav hrefs verified present.*

---

## Feature Completeness Audit — Dimension 5

*Audit pass 2026-06-05. Checked: word cloud scope data (all 11 scopes have non-zero ot/nt/genre counts), study guide session tabs (5 guides, all tabs have real content), all 10 topic pages (no stubs — 285–2538 lines of real content), manifest shortcuts (3/3 resolve), sidebar nav links (all resolve), NT Daily devotional rotation logic. Reading plans, library docs, and commentary sources already verified in Dimension 4.*

---

## Performance Audit — Dimension 6

*Audit pass 2026-06-05. Read: `assets/js/word.js`, `assets/js/search.js`, `assets/js/reader.js`, `assets/js/verse-study.js`, `assets/js/daily.js`, `assets/js/core.js`. Verified: search is 250ms-debounced; daily.js fetches one devotional on load (not all 5); vsRenderVersionCompare is lazy-loaded via IntersectionObserver; VOTD file is 2.7KB (not a concern). Measured: OT interlinear = 39 files × avg 205KB = 8MB total; NT interlinear = 27 files = 3.5MB; all 66 KJV books = 4.4MB.*

---

*Audit pass 2026-06-05 (Cycle 2). Read: `assets/js/verse-study.js`, `assets/js/daily.js`, `assets/js/ol-companion.js`, `assets/js/apocrypha-reader.js`, `assets/js/word.js`, `assets/js/reader.js`, `assets/js/core.js`. Verified: daily.js fetches only selected devotional (confirmed); `loadLibVerseIndex` is properly cached (confirmed double-call is a no-op at network level); IntersectionObserver deferral confirmed (line 819); word.js BATCH_SIZE=5 confirmed implemented. New finding: vsRenderVersionCompare fires 11 uncapped concurrent fetches — PERF-4.*

---

*Audit pass 2026-06-05 (Cycle 3). Read: `assets/js/lib-browser.js`, `assets/js/ol-companion.js`, `assets/js/reader.js`, `data/library/index.json` (92 KB, 182 docs). Verified: lib-browser.js search debounced 200ms/150ms ✓; `_saveSectionIdx` only fires on pagination not scroll ✓; scroll spy uses `{ passive: true }` ✓; `loadCrossRefs` in core.js caches by bookId with promise-store (concurrent verse renders share pending fetch) ✓; ol-companion.js fetches cached after first book load ✓; library index 92KB is reasonable ✓. New finding: `data/translation/notes/` book files are 3.8–5.4 MB; ol-companion.js fetches the entire book file to render any single verse — PERF-5.*

---

## Performance Audit — Dimension 6, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Checked: verse-study new section fetch cascade (new sections trigger: `_naveLoad()` 1.4MB, `_naveLoadVidx` small, 3× dict verse-indexes small, `loadLibVerseIndex` small). Full indexes (Easton 753KB, Smith 833KB, ISBE 1.9MB) are NOT loaded by verse-study — `renderVSDictionary` only fetches the per-book verse-index files and renders link chips; full entry content loads only when user navigates to the dictionary page. Single shared promise `_naveLoading` prevents redundant fetches within a session. Finding: `_naveTopicsForVerse` loads the full 1.4MB Nave's index before checking if the verse has any topics.*

---

## Performance Audit — Dimension 6, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: `app.js` init sequence (all page-specific inits guarded by landmark element checks ✓); `wordcloud.js` `frequencies.json` fetch is gated on `wc-container` element ✓; `places.js` 16KB places.json — trivially small, no issue; `search.js` debounced 250ms ✓. Focus: `terms.js` `runAutoTagTerms()` and `runAutoTagPlaces()` idle callback behavior on pages with no taggable content. One issue found.*

---

## Performance Audit — Dimension 6, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: `library.js` OMNI_SOURCES load sequencing — all 5 secondary dict sources (Smith 852KB, ISBE 1.9MB, Hitchcock 180KB, Nave 1.4MB, Torrey 546KB) fire in parallel after Easton resolves, incremental `_buildOmniIndex()` rebuilds are intentional progressive enhancement ✓; `lib-reader.js` sequential index + doc fetch chain ✓; `lib-browser.js` search debounced 150ms/200ms ✓; `verse-study.js` loadVerseSections fires loadInterlinear + loadStrongs eagerly for interlinear table render (needed, by design) ✓; `vsRenderVersionCompare` now uses BATCH_SIZE=5 (PERF-4 fixed) ✓; `apocrypha-reader.js` metadata files <4KB ✓; `ol-companion.js` now fetches per-chapter 20–50KB (PERF-5 fixed) ✓. One issue found: dictionary search input lacks debounce.*

---

## Visual System Audit — Dimension 7

*Audit pass 2026-06-05. Checked: hardcoded hex colors across all `assets/css/*.css`; dark mode blocks in style.css, topic-shell.css, topic-guide.css, timeline.css, timelapse.css, maps.css, lib-reader.css, word.css; `--tg-accent` usage consistency; `--color-heading` variable definition; template placeholder text (none found). Dark mode variables defined: `--color-bg`, `--color-surface`, `--color-primary`, `--color-text`, `--color-muted`, `--color-border`. Notably absent: `--color-heading` — never defined in style.css, only used via fallback.*

---

*Audit pass 2026-06-05 (Cycle 2). Read: `assets/css/ol-companion.css`, `assets/css/apocrypha.css`, `assets/css/workshop.css`, `assets/css/discipline.css`, `assets/css/memorize.css`, `assets/css/devotionals.css`. Verified: apocrypha.css `#fff` uses are on primary-colored backgrounds (acceptable). workshop.css status badges have dark mode; dispute/action-button pastels do not (workshop is dev-tool, lower priority). memorize.css rate button colors (again/hard/good/easy) have no dark mode but remain legible since they are bright saturated on dark. discipline.css plan-done and calendar-check missing (tracked CSS-14). ol-companion.css tier labels missing (tracked CSS-13).*

---

*Audit pass 2026-06-05 (Cycle 3). Read: `assets/css/verse-study.css`, `assets/css/lib-browser.css`. Verified: no px font sizes in either file ✓; `#fff` in `lib-browser.css` lines 576/693 is white text on primary-colored active chips (acceptable pattern) ✓; `lb-author-dot--*` mid-range colors remain visible in dark mode ✓. New findings: verse-study.css echo-badge light pastels have no dark mode — CSS-17. lib-browser.css tradition abbrev badges use dark hex colors invisible in dark mode + `mark.lb-find-mark` bright yellow — CSS-18.*

---

*Audit pass 2026-06-06 (Cycle 4). Read: `assets/css/dictionary.css`, `assets/css/library.css`, `assets/css/lib-reader.css`, `assets/css/lib-progress.css`. Verified dark mode coverage: lib-reader.css covers `.lr-sidebar-inner`, `.lr-pager-num`, `.lr-vol-chip`, `.lr-find-bar`, `.lr-find-input`, `mark.lr-find-mark` (amber `#92610a`) — clean ✓. lib-progress.css covers `.lp-stat` and `.lp-bar-track` — clean ✓. Finding: dictionary badge colors (`#1e3a5f` ISBE navy, `#065f46` Hitchcock green, `#1d4ed8` Smith blue) are set as inline JS styles — cannot be overridden by CSS dark mode rules; `library.css` `.lib-badge--*` tradition classes use hardcoded hex with no dark mode block; `lib-progress.js` `.lp-trad-chip` also uses inline style colors.*

---

## Visual System Audit — Dimension 7, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked CSS files not deeply audited for dark mode in prior cycles: `timeline.css` (dark mode covers spine-wrap, node-dot, tl-detail, legacy teal/blue colors ✓), `timelapse.css` (map stays intentionally light in both modes; dark mode covers tooltips ✓), `maps.css` (dark mode covers map-container bg and site-item-star ✓), `study-guide.css` (no hardcoded hex ✓), `wordcloud.css` (only `background: none` ✓), `topical.css` (no hardcoded hex outside dark mode ✓), `topic-guide.css` (only `#fff` on accent backgrounds ✓). One gap found: `topic-shell.css` `.nav-panel` (mobile slide-in nav drawer) has `background: #fff` with no dark mode override.*

---

## Visual System Audit — Dimension 7, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked CSS files not yet audited for dark mode: `study-nav.css` (parchment vars, no dark mode block — intentional fixed-theme aesthetic for prayer/revelation study pages ✓), `daily.css` (checker/badge colors #4caf50/#b71c1c stay saturated in dark mode, remain legible ✓), `reader.css` (highlight verse number overrides covered by both [data-theme="dark"] and @media dark blocks ✓; `.reader-xref-note:hover { color: #2d6080; }` hover state ~2.9:1 contrast on dark bg — borderline but only on hover of hidden-by-default footnote markers, LOW priority), `bible-ui.css` (search-chip + modal verse highlight colors all have dark overrides ✓). Critical finding: `book-study.css` (987 lines, zero dark mode blocks) hardcodes `body.bk-ot/bk-nt` background-color as light values, overriding `var(--color-bg)` from style.css in dark mode, causing `--color-text: #e8dfc8` to render on `#f8f9fc` background — 1.27:1 contrast, near-invisible text on Romans and Revelation pages in dark mode.*

---

## Visual System Audit — Dimension 7, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked remaining CSS files: `wordcloud.css` (0 dark mode blocks, 0 hardcoded hex colors — all `var()` — clean ✓); `dictionary.css` badge elements (`vs-dict-src-badge`, `dict-filter-chip__badge`, `dict-item__src`) use `color: #fff` on dark-colored backgrounds (deep blues/purples/reds); both `[data-theme="dark"]` and `@media` dark blocks exist for these — clean ✓; `ol-companion.css` `.olc-disp-*/olc-tier-*` have both dark override mechanisms ✓; `timeline.css` `.tl-detail-crossover__label` covered at lines 533–534 ✓; `topic-shell.css` cream (#e8d9bb) on dark topic header — intentional fixed contrast ✓. Critical finding: `apocrypha.css` has 3 selectors with `color: #fff` on `background: var(--color-primary)` (active chapter btn, active canon chip, nav btn hover) — in dark mode primary = #e8c87a golden, so white fails ~1.3:1 — CSS-25.*

---

## Visual System Audit — Dimension 7, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked `maps.css` and `timelapse.css` for dark mode gaps. `maps.css`: `.maps-site-item-star #b00010` and `.maps-map-container #e8f4f8` already have dark overrides (lines 826–831) ✓. Found 4 hover-state rules using `color: #fff` on `background: var(--color-primary)`: `.maps-timelapse-link:hover`, `.maps-tl-chip:hover`, `.maps-refs-chip:hover`, `.maps-city-map-chip:hover` — all inconsistent with `.maps-city-ref-chip:hover` which correctly uses `var(--color-on-primary, #fff)` — CSS-27. `timelapse.css`: tooltip dark overrides present (Cycle 6) ✓. Found 4 elements with `background: var(--color-primary); color: #fff` lacking dark mode overrides: `.tl-btn-play`, `.tl-btn-continue`, `.tl-events-toggle`, `.tl-map-link:hover` — CSS-28.*

---

## Visual System Audit — Dimension 7, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Checked `bible-ui.css` (remaining after Cycle 8 covered maps/timelapse/apocrypha/book-study). Found 3 elements with colour failures in dark mode: `.search-go-btn` uses `background:var(--color-primary); color:var(--color-text)` — dark text on golden fails; `.bsw-modal__verse-study-link` is styled blue-on-light but the dark block only sets the border without resetting link colour to accessible blue; `.bsw-place-tip__link:hover` hardcodes `color:#fff` on `background:var(--color-primary)` hover — golden/white 1.3:1 fail. See CSS-30.*

---

## Visual System Audit — Dimension 7, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Checked `lib-browser.css` and `reader.css` for remaining dark mode text-color gaps. `lib-browser.css`: existing dark block fixes `.lb-vol-chip` background but not `.lb-vol-chip--active` or `.lb-sec-tab--active` text — both use `background:var(--color-primary); color:#fff`; in dark mode golden primary → white fails ~1.3:1 — CSS-32. `reader.css`: `.reader-xref-chip--active` (background:var(--color-primary); color:#fff) and `.reader-qs-chip:hover` (same) both lack dark overrides — CSS-33. Also spot-checked `word.css`, `study-guide.css`, `library.css` — no `color:#fff` on primary-bg patterns found ✓.*

---

## Navigation & Discoverability Audit — Dimension 8

*Audit pass 2026-06-05. Checked: all main sidebar nav links (all resolve — `read/`, `apocrypha/`, `search/`, `studies/`, `discipline/`, `history/`, `library/`, `library/progress/`, `translation/workshop/`); all 10 topic cards → real pages; all 5 study guide cards → real pages; history hub 4 iframe tabs (all 4 `data-src` targets exist: `timeline/`, `church-history/`, `maps/`, `maps/timelapse/`); `?minimal=1` mode (correctly early-returns from `buildSidebar()` before both sidebar and mobile topbar are built); `tracker/` (embedded as iframe in `discipline/?tab=history`); `compare/` (linked via `COMPARE_URL` in `modal.js` line 411); `wordcloud/` (embedded as iframe in `search/?tab=wordcloud`). Redirect stubs (`plans/`, `journal/`, `memorize/`, `devotionals/`, `reflections/`) all redirect correctly to discipline tabs.*

---

*Audit pass 2026-06-05 (Cycle 2). Checked: all pages on disk vs. nav entries; data/topics.json vs. topics/ dirs (all resolve); study-guides hrefs in topics.json (all 5 resolve); `worship/` redirect stub (correctly points to discipline/?tab=worship); NOTES_URL vs. BOOKMARKS_URL consumption (BOOKMARKS_URL used in reader.js:1101; NOTES_URL never imported — see NAV-3); `tools/terms/` (not yet created — Z5 planned work). No broken nav links, no orphaned topics, no missing study guides.*

---

*Audit pass 2026-06-06 (Cycle 3). Read: `assets/js/main.js` NAV array, `assets/js/verse-study.js` prev/next logic (lines 222–243), `verse-study/index.html`, `assets/css/style.css` sidebar layout. Verified: `apocrypha/` ✓ in NAV (line 56); `word/` ✓ linked via WORD_URL from search + verse-study tokens; `bookmarks/` ✓ linked via BOOKMARKS_URL (reader.js:1101); `notes/` ✓ linked via NOTES_URL (reader.js:1164 + modal.js:992); `verse-study/` ✓ linked from reader modal (modal.js:426); `study-guides/` ✓ linked from topics.json; `church-history/` ✓ linked from history hub iframe; all four pages have index.html ✓; verse-study page correctly loads main site sidebar (body.padding-left via style.css:72) ✓. New finding: verse-study prev/next hides at chapter boundaries with no cross-chapter fallback — NAV-4.*

---

*Audit pass 2026-06-06 (Cycle 4). Checked all `*/index.html` files on disk against nav reachability. All top-level pages accounted for ✓ (redirect stubs, iframe-embedded pages, JS-linked pages all verified in prior cycles). Library sub-pages: old church father profile pages and major confessions are in SHELL_URLS ✓. New finding: 8 new library standalone pages exist on disk but have no navigation links pointing to them and are not in SHELL_URLS. Library browser opens all docs inline (not by navigating to `library/{id}/`); full-screen reader uses `library/read/?doc={id}`. These 8 standalone pages are orphaned — accessible only by direct URL.*

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: `data/topics.json` vs `topics/` directories (all 10 slugs match on-disk dirs ✓); study-guide hrefs in topics.json vs `study-guides/` (all 5 match ✓); `studies/index.html` card hrefs (all 15 card links resolve ✓); `search.js` `_hubTabs` vs HTML iframe `data-src` attributes (topics → `../topics/?minimal=1` ✓, guides → `../study-guides/?minimal=1` ✓, dictionary ✓, wordcloud ✓); `history/index.html` iframe data-src values (all 4 tabs ✓); `discipline/index.html` `?tab=` parameter handling (moreTabs `notes/progress/history` correctly handled; `?tab=history` → `disc-history` panel with tracker iframe ✓); `translation/workshop/` in sidebar footer (`wsLink` at main.js:356 ✓); all library standalone pages vs `sw.js` SHELL_URLS (29 entries, all match real index.html files ✓); `library/read/` and `library/progress/` both in SHELL_URLS ✓; `LIB_READER_URL` at `core.js:42` exported but never imported (inline `_resolve()` used in lib-browser.js:857 and lib-progress.js:130 instead — cosmetic dead export, LOW). One gap found: 2 empty stub dirs in `library/`.*

---

## PWA & Offline Audit — Dimension 9

*Audit pass 2026-06-05. Checked: `sw.js` cache strategy (`networkFirst` for navigation, `cacheFirst` for data/assets), install SHELL_URLS completeness, activate cleanup logic (correct — deletes non-current caches), `manifest.json` (shortcuts, icons, colors), `offline.html` (real content with working links, loads `main.js` correctly as non-module), `pwa.js` (`initPWA`, `triggerPrecache`, `_showSWUpdateToast`), `precacheBible` chunked fetching. All 200+ SHELL_URLS resolve to real files on disk — no broken precache paths. `workshop.js`/`workshop.css` intentionally absent (dev tool). `data/votd/verses.json` is a single pre-fetched file (no per-day files). 4 issues found.*

---

*Audit pass 2026-06-05 (Cycle 2). Checked all SHELL_URLS against disk. New assets correctly included: `apocrypha.css/js`, `ol-companion.css/js`, `discipline.css/js`, `memorize.css/js`, `lib-browser/progress/reader.css/js`, `timelapse-map.js`, `places.js`, `worship/index.html`, `study-guides/*.html`. Intentionally absent (dev tool): `workshop.js`, `workshop.css`. Missing: `data/apocrypha-books.json` + `data/apocrypha-canon-orders.json` (tracked PWA-5); `topics/holy-catholic-church/index.html` (LOW — not all topics are precached, just the most popular); `translation/workshop/index.html` (intentional — dev tool, not for offline use).*

---

*Audit pass 2026-06-06 (Cycle 3). Read: `sw.js` SHELL_URLS (lines 29–203), `manifest.json`. Verified: `bsw-app-v66` current; PWA-5 resolved in archive ✓; all 26 non-workshop CSS files in SHELL_URLS ✓; all JS files in SHELL_URLS ✓; manifest.json shortcuts (read/, verse-study/, notes/) all resolve ✓; `translation/workshop/index.html` intentionally absent ✓. New finding: `library/progress/index.html` exists on disk and is in the sidebar nav but missing from SHELL_URLS — PWA-6.*

---

*Audit pass 2026-06-06 (Cycle 4). Read: `sw.js` SHELL_URLS (lines 29–204), all `assets/css/*.css` and `assets/js/*.js` on disk, all `data/` top-level JSON files >200KB. Verified: `bsw-app-v69` current; all 26 CSS files ✓; all 32 JS files (workshop.js intentionally absent) ✓. Cross-referenced large data files vs SHELL_URLS — found two gaps: (1) `library/read/index.html` not in SHELL_URLS despite being the target of every "Open in full-screen reader" link in the library; (2) `data/dictionary/index.json` (756KB) not in SHELL_URLS while the conceptually equivalent `data/smith/index.json` (836KB) IS — Easton's dictionary page fails offline on first visit while Smith's works. Large files intentionally lazy-cached: `data/isbe/index.json` (1.9MB), `data/topical/nave.json` (1.4MB), `data/library/search-index.json` (920KB), all interlinear/crossref/commentary files — all correct per cacheFirst strategy.*

---

## Accessibility Audit — Dimension 10

*Audit pass 2026-06-05. Checked: focus styles (sidebar, modal, reader, `.ref` links), ARIA roles and labels (sidebar collapse button, hamburger, nav, modal dialog, reader controls, discipline tabs), modal keyboard trap (`trapFocus` in `modal.js` — complete: Escape closes, Tab cycles, `_lastFocused.focus()` restores on close), color contrast (all primary color pairs pass WCAG AA), `alt` attributes (no `<img>` elements in main pages — site uses CSS/SVG/emoji icons), theme toggle button accessible name (visible text content serves as label), `discipline-strip.js` mobile label handling. Modal, reader, and search ARIA patterns are solid. 4 issues found.*

---

*Audit pass 2026-06-05 (Cycle 2). Checked: `apocrypha-reader.js` (canon chips, chapter buttons — ARIA gaps found), `ol-companion.js` (token buttons — ARIA gap found), `lib-browser.js` (solid ARIA throughout — aria-label on all controls, aria-current on active doc link), `verse-study.js` section toggles (correct — aria-expanded + aria-controls). No new focus-order or contrast issues found beyond those tracked in cycles 1 & 2.*

---

*Audit pass 2026-06-06 (Cycle 3). Read: `verse-study/index.html`, `assets/js/verse-study.js`, `assets/js/wire.js`, `assets/js/ol-companion.js`, `assets/js/apocrypha-reader.js`, `assets/js/lib-browser.js`. Verified: lib-browser.js controls all labeled ✓; wire.js handles Enter + Space on `.ref` links ✓; verse-study token buttons have aria-label ✓; section headings use h2 ✓; context toggle has aria-pressed ✓; apocrypha-reader chapter buttons have aria-label + aria-current ✓ (AUD-7 resolved); ol-companion token buttons have aria-expanded ✓ (AUD-8 resolved). New finding: verse-study.js never updates document.title or marks #vs-header-ref as a heading — screen readers see a static "Verse Study" tab and no h1 — AUD-11.*

---

*Audit pass 2026-06-06 (Cycle 4). Read: `assets/js/lib-reader.js`, `assets/js/lib-browser.js`, `assets/js/library.js` (dictionary page), `assets/js/lib-progress.js`. lib-progress.js is read-only (just links) — clean ✓. lib-reader find bar, pager prev/next, section select all have `aria-label` ✓. lib-browser toggle buttons update `aria-label` on state change ✓. Finding: five interactive control groups across three files use visual-only state (CSS classes) with no matching ARIA state attributes — screen readers cannot announce selected/active/on state.*

---

## Feature Completeness Audit — Dimension 5, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (AUD-1) found the NT Daily Matthew chapter-count bug. This pass checked: ISBE data (9,380 entries + 66-book verse-index — complete), OL Companion wiring (`window.BibleUI.initOLSection` → verse-study.js — correct), book introductions (66/66), Nave's topical verse-index (66/66), topics-index.json (15 entries — all pages resolve), word cloud scopes (unchanged), translation workshop (page exists), apocrypha reader. Found one HIGH bug in apocrypha-reader.js `_getOrderedBooks()`.*

---

## Feature Completeness Audit — Dimension 5, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Confirmed: reading plans (8/8 IDs → files), MKT commentary data (fully generated), echoes data (fully generated), apocrypha reader nav wiring, OL Companion wiring. Found two data-ready features with no UI access path.*

---

## Feature Completeness Audit — Dimension 5, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Checked: dictionary page OMNI_SOURCES registration (Easton's, Smith's, ISBE, Hitchcock, Nave's, Torrey's — all 6 registered in OMNI_SOURCES ✓); `?src=...&entry=...` URL routing (`_tryShowUrlEntry` at line 782 — Easton's works because it loads first; secondary sources load async in a separate forEach at line 812 with no re-try of `_tryShowUrlEntry` after they resolve). Found one HIGH bug affecting all verse-study cross-links to non-Easton's sources.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle verified all 18 canonical Bible versions, 8 commentary sources, crossrefs, interlinear, plans, library docs, manifest shortcuts, and nav hrefs. This pass checked the new apocrypha data layer (`data/bible-apocrypha/`, `apocrypha-books.json`, `apocrypha-canon-orders.json`) and JS fetch paths in `apocrypha-reader.js`, `terms.js`, `places.js`.*

---

### DATA-3 · BRENTON version missing scope correction and 1 canonical OT book *(MEDIUM)* *(partially done: code + 2 of 3 data files complete, nahum still missing)*

**Problem:** `data/versions/versions.json` declares `BRENTON` with `"scope": "full-bible"` and `"canon_order": "lxx"`. The `lxx` canon order in `apocrypha-canon-orders.json` lists 83 books (66 canonical + 17 deuterocanonical). However, the Brenton LXX is an Old Testament translation only with no NT content. The apocrypha reader uses `_isFullBible()` to decide whether to show NT navigation, so on BRENTON all 27 NT books appeared in the book list but every one 404d when clicked. Additionally, 3 canonical OT books were missing from the BRENTON directory.

**Code fix applied (2026-06-05):** Changed BRENTON `scope` to `"ot-only"`. Updated `_getOrderedBooks()` to filter NT books for OT-only scope. This stops the 27 NT 404s.

**Data fix applied (2026-06-06, iteration 4):** Re-running `fetch-apocrypha.py BRENTON --force` recovered `daniel.json` (12 ch, 420 v) and `esther.json` (10 ch, 164 v). `nahum.json` is genuinely absent from the eBible.org BRENTON source and remains missing.

**Remaining:** `nahum.json` — source data not available from eBible.org for BRENTON; requires manual sourcing or alternative BRENTON source.

**Verify:** Open the apocrypha reader, select BRENTON, confirm the book list shows only OT books. Navigate to Daniel — it should load (now resolved). Navigate to Nahum — still a 404 until data is sourced.

---

## Data Path Integrity Audit — Dimension 4, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Cross-checked all translation data paths (notes + 3 MKT draft tiers × 66 books = 264 files — all present). All 8 registered commentary sources have complete 66-book coverage. Topics.json href links all resolve. Found one new gap: WEB-CE has the same Daniel-additions data gap as DR (DATA-4) but with a slightly different set of missing books.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Checked all verse-index paths used by the dictionary/topical panel: Easton's (`data/dictionary/verse-index/`) 66/66 ✓; Nave's (`data/topical/verse-index/`) 66/66 ✓; ISBE (`data/isbe/verse-index/`) 66/66 ✓; Torrey (`data/torrey/verse-index/`) 64/66 — missing Isaiah + Jude (correct: `torrey.json` has zero citations for those books); library (`data/library/verse-index/`) 47/66 (correct: only books with library citations have index files). AUD-9 (echoes) and AUD-10 (MKT commentary) are both resolved in code. One gap found: Smith's dictionary verse-index missing `philippians.json`.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (CSS-1–6) addressed word.css height clipping, hamburger/discipline/reader touch targets, study-nav font-size, and reader keyboard hint visibility. This pass examined lib-browser.css, verse-study.css, memorize.css, maps.css, and timelapse.css. Two new issues found.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Prior cycles addressed the core reader, discipline, lib-browser, verse-study, maps, and timelapse pages. This pass audited `apocrypha.css` and `ol-companion.css` — both added after the previous mobile passes.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Prior cycles covered word.css, core reader/discipline controls, lib-browser.css, verse-study.css, maps/timelapse/memorize, apocrypha.css, ol-companion.css. This pass audited `lib-reader.css` and `lib-progress.css` — the two remaining CSS files not covered in prior passes. lib-progress.css is clean (no interactive controls, mobile query at line 162). lib-reader.css has a touch-target gap: `.lr-toc-list a` was correctly fixed to 44px at 640px (lines 201–203), but three other interactive control groups were not. Finding below.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Prior cycles covered word.css, reader/discipline/study-nav controls, lib-browser.css, verse-study.css, maps/timelapse/memorize, apocrypha.css, ol-companion.css, lib-reader.css, lib-progress.css. This pass checked: `dictionary.css` (634 lines, 11 media queries), `daily.css` (716 lines, 6 media queries), `book-study.css` (987 lines — read-only layout/display file, one 640px responsive breakpoint, no interactive controls), `topic-guide.css`, `topic-shell.css`, `study-guide.css`, `topical.css`, `timeline.css`, `wordcloud.css`, `devotionals.css`. book-study.css/topic-guide.css/study-guide.css/topical.css/timeline.css/wordcloud.css/devotionals.css: no interactive button/control groups; mobile breakpoints handle layout reflows — clean ✓. dictionary.css and daily.css: both have interactive control groups with sub-22px touch targets that lack corrective mobile breakpoints.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Prior cycles covered word.css, reader/discipline/study-nav, lib-browser.css, verse-study.css, maps/timelapse/memorize, apocrypha.css, ol-companion.css, lib-reader.css, lib-progress.css, dictionary.css, daily.css, book-study.css, topic-guide.css, topic-shell.css, study-guide.css, topical.css, timeline.css, wordcloud.css, devotionals.css. This pass checked the four remaining CSS files: `bible-ui.css` (3840 lines, two mobile breakpoints at 480px and 767px), `discipline.css` (590 lines, one breakpoint at 500px), `library.css` (one breakpoint at 480px for Q&A grid), `workshop.css` (one breakpoint at 900px for source grid). library.css is mostly typographic display with no button controls — clean ✓. workshop.css is a dev-tool page only accessed from desktop — single grid layout query, no touch-target requirement ✓. discipline.css mobile breakpoint only adjusts .disc-tab padding and .plan-card__top flex direction; journal and worship entry edit/delete buttons remain sub-20px. bible-ui.css has a thorough 767px block covering modal close, action buttons, tabs, and xref chips — but the prev/next verse navigation buttons are explicitly made narrower on mobile than desktop.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked `maps.css` (mobile breakpoint `@media (max-width: 700px)`): `.maps-nav-btn` (map selector, main nav) — `padding: .2rem .5rem; font-size: .74rem` → ~21px tall on mobile, too small but used in a horizontally-scrollable strip with `flex-shrink: 0` so fixing to 44px could cause layout overflow; LOW priority. `.maps-tab` (Overview/Sites/Refs panel tabs) — `padding: .3rem .4rem; font-size: .70rem` → ~23px tall on mobile; these are the primary panel navigation controls on mobile and need 44px. `.maps-city-nav-btn` (Prev/Next City in detail panel) — `padding: .1rem .5rem; font-size: .78rem` → ~19px tall on mobile; smallest interactive control, used when exploring city detail. Both `.maps-tab` and `.maps-city-nav-btn` are sub-44px with no existing mobile override — CSS-26.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (UX-1–5) addressed search.js, verse-study.js interlinear, discipline plans, library secondary sources, and history iframe tabs. This pass found two remaining missing `.catch()` patterns in verse-study.js.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Previous cycles covered the core reader, search, verse-study, and discipline pages. This pass targeted two newer modules — lib-browser.js and apocrypha-reader.js — that were added after the prior audits.*

---

## Code Comment Audit — Dimension 1, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (CODE-1–8) addressed the most obvious gaps. This pass found two areas still missing required structured comments: three complex algorithms in wire.js added after the first-pass fixes, and the window.BibleUI cross-module coupling in app.js.*

---

## Code Comment Audit — Dimension 1, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Prior cycles (CODE-1–10) addressed the original JS files and wire.js/app.js additions. This pass found two files added since those fixes — ol-companion.js and lib-browser.js — that have zero INTENT/CHANGE?/VERIFY coverage despite containing complex state logic.*

---

## Code Comment Audit — Dimension 1, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Prior cycles covered core.js, storage.js, reader.js, wire.js, app.js, ol-companion.js, lib-browser.js plus fixes CODE-1–12. This pass checked `verse-study.js` (1,238 lines, 11 INTENT/CHANGE?/VERIFY occurrences) and `interlinear.js` (472 lines, 6 occurrences). interlinear.js gaps are minor (private-state short setters). verse-study.js has two exported functions and one window.BibleUI coupling without required comments.*

---

## Code Comment Audit — Dimension 1, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Prior cycles covered core.js, storage.js, reader.js, wire.js, app.js, ol-companion.js, lib-browser.js, verse-study.js, interlinear.js (CODE-1–13). This pass checked `lib-reader.js` (740 lines, 0 INTENT/CHANGE?/VERIFY), `tracker.js` (173 lines, 4 comments), and `modal.js` (1,496 lines, 7 comments). lib-reader.js has zero coverage despite an exported entry-point and four localStorage functions. modal.js has solid coverage on register* functions and buildModalDOM but is missing INTENT/CHANGE?/VERIFY on its 5 major render/open exported functions.*

---

## Code Comment Audit — Dimension 1, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Prior cycles covered core.js, storage.js, reader.js, wire.js, app.js, ol-companion.js, lib-browser.js, verse-study.js, interlinear.js, lib-reader.js, tracker.js, modal.js (CODE-1–15). This pass checked `parallels.js` (346 lines, 0 INTENT/CHANGE?/VERIFY), `daily.js` (1,323 lines, 4 comments), and `terms.js` (393 lines, 3 comments — existing coverage on `runAutoTagTerms` only). Two significant gaps found.*

---

## Code Comment Audit — Dimension 1, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Prior cycles covered core.js, storage.js, reader.js, main.js, word.js, search.js, wordcloud.js, wire.js, app.js, ol-companion.js, lib-browser.js, verse-study.js, interlinear.js, lib-reader.js, tracker.js, modal.js, parallels.js, daily.js, terms.js (CODE-1–17). Remaining unchecked files by INTENT count: maps.js (2448 lines, 1), timelapse-map.js (836 lines, 2 on _animLoop/_figurePos only), timeline.js (707 lines, 2 on internal helpers), pwa.js (155 lines, 3 — adequate), store.js (281 lines, 0), sg-progress.js (99 lines, 0), lib-progress.js (147 lines, 0), apocrypha-reader.js (613 lines, 10 — adequate). Two significant gaps found.*

---

## Code Comment Audit — Dimension 1, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Prior cycles covered all major JS modules (CODE-1–19). Remaining unchecked: `sg-progress.js` (99 lines, 0 INTENT — 2 exported entry points + 1 non-obvious internal), `lib-progress.js` (147 lines, 0 INTENT — 1 exported entry + 1 complex renderer), `timeline.js` (707 lines, 2 on internal helpers — needs entry-point coverage). Two files with zero coverage found: sg-progress.js + lib-progress.js — CODE-20.*

---

## Code Comment Audit — Dimension 1, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Prior cycles covered all JS modules (CODE-1–20). Final unchecked file with exported entry points: `timeline.js` — `initTimelinePage()` and `initChurchTimelinePage()` both exported from line 691/700 with zero INTENT; they use `storageKey: 'bsw_tl'/'bsw_chtl'` that map to `sessionStorage` keys (bsw_tl_era, bsw_tl_event, etc.) with TLU-B URL-param fallback logic. Non-obvious: two separate timelines share the same _makeController factory but must use distinct storageKey namespaces or they'll overwrite each other's sessionStorage — CODE-21.*

---

## Code Comment Audit — Dimension 1, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Checked `wire.js` — 4 exported functions with no INTENT block: `wireRefEl` (core tooltip/modal event wiring, cross-module via callScheduleShow/callOpenModal), `wireRefLinks` (idempotent [data-ref] scanner, called from app.js and search.js), `wireInlineVerses` (populates .bsw-verse elements on init, version-change wired via app.js), `applyBookmarks` (reads localStorage bookmarks, toggles CSS class on verse numbers). All 4 are non-obvious in their cross-module couplings — CODE-22.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Prior cycles covered reader, search, verse-study, discipline, lib-browser, apocrypha-reader. This pass targeted modules not yet covered: `ol-companion.js`, `word.js`, `lib-reader.js`, `lib-progress.js`, and the verse-study section loaders (confessions, church fathers, dictionary, OL companion). All modules have solid error handling: `_loadNotes`/`_loadTier` both have try/catch with null-cache on failure (ol-companion.js lines 38–44, 58–63); missing `?s=` shows user-visible error at line 47 and `.catch` at lines 192–195 (word.js); error messages at lines 59/63/97–99 with "Return to Library" link (lib-reader.js); `.catch` renders empty log at line 48 and "No completed works yet" state at line 120 (lib-progress.js); all four new verse-study sections (confessions/church-fathers/dictionary/OL companion) have `.catch` that removes the section and calls `vsRebuildNav` (verse-study.js lines 887/900/911/917). No new items this cycle.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked remaining uncovered modules: `daily.js` (1,323 lines), `modal.js` (1,496 lines), `library.js` (dictionary page), `timeline.js`, `wordcloud.js`, `maps.js`, `timelapse-map.js`, `sg-progress.js`, `store.js`, `terms.js`. daily.js: every fetch has `.catch()` with user-visible message ✓. modal.js: cross-refs and commentary both show user messages on failure ✓; empty catches are for clipboard API and optional verse-text enrichment (silent is correct) ✓. library.js: Easton's main load failure → "Failed to load dictionary" ✓; entry fetch → "Could not load entry." ✓. timeline.js: "Unable to load timeline data." ✓. wordcloud.js: "Unable to load word frequency data." ✓. maps.js: all data inline — no fetch ✓. One finding: timelapse-map.js catch is console.error only, no user-visible error.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Prior cycles covered reader.js, search.js, word.js, verse-study.js, library.js, lib-browser.js, apocrypha-reader.js, ol-companion.js, lib-reader.js, lib-progress.js, daily.js, modal.js, timeline.js, wordcloud.js, maps.js, timelapse-map.js, terms.js. This pass checked `parallels.js` (good: "Could not load." + "Not available." messages, silent empty `.catch()` on optional panels ✓), `discipline-strip.js` (no fetches — reads synchronously from tracker.js, renders gray dots as empty state ✓), `tracker.js` (pure localStorage module, no fetches ✓). One gap: `places.js` `loadPlaces()` has no `.catch()` — permanent rejected-promise cache causes repeated unhandled rejections on every reader page turn.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). All JS files confirmed: pwa.js (no fetches ✓), tooltip.js (no fetches ✓), wire.js (no fetches ✓), interlinear.js (all 3 .catch() handled ✓), app.js (no fetches ✓), sg-progress.js (pure localStorage ✓). Redirect stubs: plans/, devotionals/, reflections/, worship/ all redirect to discipline/ — no own content. church-history/index.html and apocrypha/index.html — no page-level fetch logic. notes/index.html: three contextual empty states (no annotations, search empty, filtered empty) ✓. bookmarks/index.html: bsw-empty-state div with CTA to Reader ✓. One gap found: compare/index.html init .catch() is console.error-only.*

---

## Reader Interlinear — Popover Bugs

Four bugs in the interlinear tile popover (`assets/js/interlinear.js` — `_riShowPopover`, `renderReaderInterlinearRow`).

---

## Translation Workshop — Lexical Evidence Expansion

**Goal:** Transform the Workshop's "Attested Range" from an asserted definition into a demonstrated one. Right now `semantic_range` is a copy of the Strong's `def` field — the same single-source claim dressed up differently. The expansion adds three layers of evidence: more lexical sources (independent scholarly witnesses to the range), biblical attestation (the word in its actual textual contexts across the corpus), and extrabiblical attestation (papyri, Josephus, Philo, classical Greek — showing the word in the wild outside the Bible).

**Current sources:**
- Greek: Dodson (CC0 gloss/def) + Thayer 1889 (short/long def) — both are Strong's-adjacent derivatives
- Hebrew: Strong's Hebrew (gloss/def) + BDB 1906 (short/long def)
- `expansion` field: in schema, empty in every entry

**Evaluation:** The two-source display looks great visually. The semantic range framing is correct in theory. What's missing is *evidence* — the dossier tells you what scholars think the range is, but doesn't show you the word earning that range through actual use. A translator needs to see the word behaving differently in John vs. Paul, in the papyri vs. the LXX, in an oath vs. a prayer.

---

### WS-G · Curated semantic-range descriptions for top-100 disputed/high-use terms *(LOW — agent task)*

**Why:** The current `semantic_range` field is generated from the Strong's `def` field — it's the same text from the same source, just relabeled. For the 100 most significant terms (the Phase 1 + Phase 5 sets), the range description should be a curated synthesis: what do all the sources agree on, where do they diverge, and what does the corpus evidence show? This is an agent-writable task — one entry at a time, the agent reads all source cards + attested uses and writes a 2-3 sentence curated range description.

**Tasks:**
- [ ] Design the agent prompt for curated range writing (reads: dodson + thayer + abbott-smith + attested uses → writes: `semantic_range` as 2-3 sentence synthesis)
- [ ] Agent pass: curate `semantic_range` for all Phase 1 Greek entries (200 entries)
- [ ] Agent pass: curate `semantic_range` for all Phase 2 Hebrew entries (200 entries)
- [ ] Agent pass: curate `semantic_range` for Phase 5 contested terms (17 entries — highest priority)

**Note:** Do WS-A–E first. The curated range descriptions should synthesise all the evidence, not just paraphrase Strong's.

---

## Study Workshop Overhaul — Original Language Bible Study Tool

**Goal:** Transform the Translation Workshop from a translation production tool into the best free original language Bible study tool in the world — one that takes a lay reader with no Greek or Hebrew and walks them into the depth a scholar would see, layer by layer. Every interpretive dimension that affects meaning should be at their fingertips: grammar significance, idiom, cultural practice, literary structure, intertextual echoes, contested interpretations, the full attested range of every word.

**Survey of the landscape:**

| Tool | Strength | Key gap for lay readers |
|------|----------|------------------------|
| **Logos Bible Software** | Most comprehensive (Passage Guide, Cultural Backgrounds Commentary, syntax DBs, Factbook, Word Study Guide) | $500–$2,000+; overwhelming UI; desktop-first; complexity barrier hides the scholarship |
| **Accordance** | Fast, clean, scholar-grade morphology/syntax trees | Mac-only; paid; same complexity wall |
| **STEP Bible (Tyndale, free)** | Best free web tool: color-coded morphology, multiple interlinears, grammar search | No cultural background; no literary analysis; no idiom layer; no proficiency model |
| **Blue Letter Bible (free)** | Popular with lay readers; Strong's + Thayer/BDB/Gesenius per word; verse-level commentary | Cluttered UI; shows parsing without saying why it matters; no literary structure |
| **Bible Hub (free)** | Everything aggregated | So dense it is paralyzing; no editorial curation; no proficiency model |
| **The Bible Project** | Best at literary structure, narrative arc, theme tracking, genre | No word-level study; no original language access |
| **NET Bible (free)** | ~60,000 translator notes — most transparent about why translations differ | Notes are scholarly, not lay-accessible; hard to navigate |
| **Sefaria** | Excellent for Rabbinic/Second Temple Jewish context | Judaism-focused; NT absent; interface unfamiliar to most Christians |

**What none of them do well for lay readers:**
1. Show grammar features AND explain in plain English why that feature matters for interpretation
2. Identify idioms inline and explain the cultural meaning of the phrase in its original setting
3. Make the logical argument structure visible (Greek particles γάρ/οὖν/ἀλλά are the author's connectors — invisible in English)
4. Present contested scholarly interpretations without requiring seminary training to evaluate
5. Progressive proficiency model — the same tool serves a new reader AND a seminary student

**What this site already has that most tools lack:**
- Complete morphological interlinear for all 66 books (SBLGNT NT + OpenScriptures OT)
- 5,523 Greek + 8,674 Hebrew glossary entries with Abbott-Smith, Thayer, Gesenius, BDB, M&M papyri, LXX bridge, book-frequency heat maps
- 11 commentary sources × 66 books (including three MKT original-language commentaries)
- Echoes/intertextual layer (54/66 books), 1,254 chapter files of translation notes, timeline, maps, ISBE dictionary

---

## Data Path Integrity Audit — Dimension 4, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked echoes (66/66 ✓), all 11 commentary sources (66/66 ✓ — `barnes`/`rwp` OT files are intentional 2-byte `{}` stubs matching their NT-only scope), all 3 MKT tier draft paths (`data/translation/draft/literal|mediating|thought/` — 66/66 ✓), all 8 plans (✓), `data/library/index.json` (182 docs — 138 HTML + 44 JSON, 0 missing ✓), `manifest.json` shortcuts (3/3 ✓), `data/topics.json` (15/15 ✓), `data/votd/verses.json` (366 entries ✓), `data/devotionals/spurgeon-{morning,evening}.json` (366 entries ✓). One gap found: `data/translation/notes/1kings/22.json` missing.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Cycle 5 checked echoes, commentary, MKT drafts, plans, library index, manifest, topics.json, votd, devotionals. This pass checked `data/torrey/verse-index/` completeness against the canonical 66 books. 64/66 present: `isaiah.json` and `jude.json` both absent. Traced root cause to two bugs in `scripts/fetch-torrey.py`: (1) `_BOOK_PREFIX_RE` regex `[a-z]{0,2}` caps lowercase at 2, so `Jude` (3 lowercase) never matches; (2) `TORREY_ABBREVS` maps `'Is':'isaiah'` but the CrossWire Torrey SWORD module likely uses `Isa`, causing 0 Isaiah entries in `torrey.json`. Confirmed: `python3 -c "import json; d=json.load(open('data/torrey/torrey.json')); print(sum(1 for t in d for v in t.get('verses',[]) if v.startswith('isaiah:')))"`  → 0.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked: all 66 `data/books/introductions/` files (min size 6.5KB, 0 hollow stubs ✓); Strongs files (`greek.json` 5523 entries, `hebrew.json` 8674 entries, `bdb.json`/`thayer.json` 1.4–1.9MB each, `lxx-bridge.json` 17 curated entries ✓); library: 0 missing source files across 182 docs ✓; Smith verse-index: 66/66 ✓ (DATA-10 confirmed fixed); parallels: 54/66 — 12 books intentionally absent (2 John, 3 John, Ecclesiastes, Esther, Lamentations, Nahum, Nehemiah, Obadiah, Philemon, Ruth, Song of Solomon, Zephaniah — all handled with "Not available." fallback ✓); `votd/verses.json` 175 entries — uses `(doy - 1) % verses.length` modulo cycling, correct behaviour ✓; commentary sources (11): mhcc/ellicott/jfb/clarke/calvin/barnes/rwp/mkt stubs all as documented in prior cycles ✓; workshop phase files: phase1/phase2/phase5 only (intentional — workshop.js lines 60–62 define exactly these 3 phases) ✓. One regression found: DATA-11 was marked complete but `data/translation/notes/1kings/22.json` is still absent — see DATA-13.*

---

## Feature Completeness Audit — Dimension 5, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: all 6 reading plans (total_days matches data array ✓); word cloud scopes (11 scopes, all fields present in `frequencies.json` ✓); study guide pages (Hebrews 14 sections, Ephesians 27, Romans 1–8 36, Sermon on the Mount 23, Psalms 20 — all static HTML with real content ✓); nav links including `studies/`, `apocrypha/`, `progress/`, `library/progress/` (all resolve ✓); `plans/` redirect stub correctly forwards to `discipline/?tab=plans` ✓; MKT commentary (mkt-original/context/christ) for John 1:1 confirmed populated ✓. Commentary source picker gap found: `rwp` label missing "(NT)" scope indicator; Calvin has 18 books silently empty.*

---

## Feature Completeness Audit — Dimension 5, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked all 11 commentary sources for coverage gaps. Ellicott, JFB, Clarke: 0 empty books ✓. Barnes (NT) and rwp (NT): 39 empty OT books each — expected by scope label ✓. MKT-original/context/christ: 0 empty books ✓. Calvin: 18 empty books — aligns with Calvin's actual corpus (he did not write on Samuel, Kings, Chronicles, Ezra, Nehemiah, Esther, Job, Proverbs, Ecclesiastes, Song of Solomon, Judges, Ruth, 2 John, 3 John, Revelation) — expected, though no label scope indicator. Wesley: 2 books empty — `1kings.json` and `philemon.json` are 2-byte `{}` stubs despite Wesley's Notes covering all 66 canonical books — data pipeline error.*

---

*(AUD-16 data-blocked — CrossWire Wesley SWORD module has entry_size=0 for all 1Kings and Philemon positions; no data exists in the upstream source to regenerate. Investigated 2026-06-06.)*

---

### WS-R · SRS ease factor for flashcard deck *(MEDIUM)*

The flashcard SRS uses fixed intervals (`FC_INTERVALS = { again:1, hard:3, good:7, easy:21 }`) with no adaptive multiplier. A word consistently rated "Easy" is scheduled at 21 days indefinitely and never graduates to a longer interval.

Fix: Add an `ease` field (default 2.5) to each entry in `bsw_ws_fc_progress`. On each rating:
- **Again**: next_date = today + 1d; ease = max(1.3, ease − 0.20)
- **Hard**: next_date = today + round(interval × 1.2); ease = max(1.3, ease − 0.15)
- **Good**: next_date = today + round(interval × ease)
- **Easy**: next_date = today + round(interval × ease × 1.3); ease = min(3.0, ease + 0.15)

`FC_INTERVALS` become seeds for the *first* review only; thereafter intervals compound. Store last interval in progress entry alongside ease and due_date.

Verify: Rate G3056 "Easy" three times → intervals should grow (e.g., 21 → 54 → 140 days) rather than capping at 21 days every time.

---

### WS-S · Grammar morph hint — per-POS vs. per-token limitation *(LOW — document only)*

The Grammar Significance section in the dossier shows all morphology hints for a word's part of speech (e.g., all seven Greek tense categories for any verb). It cannot show the *specific* morphological form of the clicked token (e.g., "this particular verb is aorist passive indicative") because the glossary entries don't carry per-token morphology tags.

Fix path (not planned): integrate SBLGNT morphological data into the interlinear JSON during the data pipeline (currently interlinear tokens carry `strongs` and `text` but not `morph` tags). This would allow the dossier to highlight only the relevant hint row. Estimated data pipeline change: 3–4MB additional per-book JSON, rewrite of `scripts/fetch-interlinear.py`.

Document as known architectural limitation. No actionable code change until interlinear data upgraded.

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked all SHELL_URLS CSS (26/26 ✓), SHELL_URLS JS (31/31 ✓ — workshop.js intentionally absent), history hub iframes (4/4 targets resolve ✓), discipline hub iframes (3/3 resolve ✓), search/?tab=dictionary → dictionary/index.html ✓, search/?tab=wordcloud → wordcloud/index.html ✓, studies/index.html in SHELL_URLS ✓, tooltip.js registered in app.js ✓. No new navigation or discoverability gaps found this cycle.*

---

## PWA & Offline Audit — Dimension 9, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: manifest.json shortcuts (read/, verse-study/, notes/ — all 3 resolve ✓); top-level data JSON files on disk (topics.json 1.7KB, topics-index.json 3.6KB, apocrypha-books.json ✓, apocrypha-canon-orders.json ✓); SHELL_URLS cross-reference of all CSS/JS (verified above in Dim 8). One gap found: data/topics.json and data/topics-index.json both absent from SHELL_URLS despite being critical for offline use — topics.json drives the Studies sidebar section on every page.*

---

## Accessibility Audit — Dimension 10, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: daily.js tab ARIA (tab buttons update aria-selected on click at lines 756, 836, 1097 ✓); word.js (no tablist UI — clean ✓); search.js + search/index.html — ARIA gap found (see AUD-15). apocrypha/index.html (no tab group in HTML — clean ✓). Other JS files (lib-browser, lib-reader, lib-progress, ol-companion) all verified in prior cycles.*

---

## Accessibility Audit — Dimension 10, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: `maps.js` map-selector nav and panel tab buttons, `timelapse-map.js` play/step/slider/speed controls, `maps/index.html` and `maps/timelapse/index.html`. Prior cycles: reader/modal/sidebar/search/daily/apocrypha/ol-companion/lib-reader/lib-browser/verse-study all covered. Maps and timelapse were the last unchecked interactive feature areas. Gap found: AUD-17.*

---

## Accessibility Audit — Dimension 10, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked: `word/index.html` — `<select id="bible-version">` has explicit `<label for="bible-version">` ✓; `dictionary/index.html` — `role="group"` + `aria-label` on filter group, `role="tablist"` + `aria-label` on alpha nav ✓; `timeline/index.html` — search input has `aria-label` ✓; `notes/index.html` — `role="tablist"` + `role="tab"` present but buttons missing `aria-selected` in HTML and `renderTabs()` never sets it — screen readers can't determine active tab — AUD-18.*

---

## Accessibility Audit — Dimension 10, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: `timeline/index.html` — only interactive element is search input with `aria-label="Search events"` ✓; `compare/index.html` — `#cmp-ref-input` text input has no `<label>` and no `aria-label`; placeholder is not an accessible name — screen readers announce as "edit text" — AUD-19. `progress/index.html` — only chapter link grid, no interactive controls needing ARIA ✓. Dims 2, 4, 5, 6, 8 Cycle 7 all clean passes — worship/reflections/prayer empty states handled, data paths intact, feature implementations complete, no debounce gaps, all nav links resolve.*

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: all 73 `index.html` files on disk cross-referenced against `sw.js` SHELL_URLS (lines 29–212) — all accounted for; 2 known intentional gaps remain: `topics/holy-catholic-church/index.html` (LOW, not all topics precached — documented Cycle 2) and `translation/workshop/index.html` (intentional dev tool, not for offline use — documented Cycle 2). `main.js` NAV array (lines 53–109) — all 15+ nav targets resolve ✓. `data/topics.json` — all 15 entries (10 topical + 5 study-guide slugs) match on-disk directories ✓. `data/library/index.json` — 182/182 documents have corresponding data files ✓. Topic page internal cross-links (30+ hrefs across 10 pages) — all resolve ✓. Study-guide internal links — all resolve ✓. `compare/index.html` ✓ (sw.js line 37), `progress/index.html` ✓ (line 100), `library/read/index.html` ✓ (line 202). No new findings this cycle.*

---

## PWA & Offline Audit — Dimension 9, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: CSS on disk (27 files) vs SHELL_URLS — 26/26 ✓ (workshop.css intentionally absent); JS on disk (32 files) vs SHELL_URLS — 31/31 ✓ (workshop.js intentionally absent); manifest.json shortcuts (read/, verse-study/, notes/ — all 3 resolve ✓); `data/books/introductions/` (66 per-book JSONs) — correctly lazy-fetched by reader.js on demand, no precache needed ✓; `data/translation/` — dev-tool workshop data, intentionally absent ✓. Gap found: `data/maps/places.json` and `data/maps/timelapse.json` both missing from SHELL_URLS — see PWA-10.*

---

## Feature Completeness Audit — Dimension 5, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked: MKT commentary chapter-level coverage for books marked complete in MKT progress tracking. mkt-original/acts: 28/28 ✓. mkt-context/acts: 28/28 ✓. mkt-christ/acts: 27/28 — chapter 27 absent despite Acts being flagged complete 2026-06-03; other 27 chapters (1–26 and 28) all populated with real content. mkt-original/luke: 24/24 ✓. mkt-context/luke: 24/24 ✓. mkt-christ/luke: 24/24 ✓. Gap found: DATA-14.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Verified remaining unchecked areas: `core.js` — `loadBooks()` `.catch()` degrades to `metaBooks=[]` silently; would leave reader book-dropdown empty and notes page without book metadata, but `books.json` is precached in SW making this scenario theoretically impossible under normal conditions ✓ (acceptable degradation). `notes/index.html` inline fetch — partial mitigation via toast on verse-picker ✓ (consistent with precaching argument above). `discipline/index.html` plan fetch `.catch()` → `devotRender(null)` shows `devot-empty` element correctly ✓; all plan JSONs are precached ✓. No new actionable items this cycle — all gaps are gated on simultaneous SW-cache and network failure for precached assets.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked `style.css` — the one CSS file not explicitly covered in prior D3 cycles. Hamburger button correctly sized (`min-height: 44px; min-width: 44px` at lines 402–403) ✓. `.sb-link` mobile override (`padding: 0.75rem 1rem`) gives ~44px ✓. Gap found: `.plans-widget__passage` (home-page "Today's Reading" passage chip-links) — `padding: 0.18rem 0.5rem; font-size: 0.82rem` gives ~19px height; no `@media (max-width: 1023px)` override exists for these. See CSS-29.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Focused on `timelapse.css` — substantially revised since Cycle 2 by timelapse phase-2 work (event column, search, step/continue buttons, events-toggle). Single mobile breakpoint at `@media (max-width: 700px)` handles layout reflow (column direction, event column 160px height) but does not fix touch targets. Interactive controls below 44px on mobile: `.tl-btn-play` (`width: 2.2rem; height: 2.2rem` → ~35px), `.tl-btn-step` (`height: 2.2rem` → ~35px), `.tl-btn-continue` (`height: 2.2rem` → ~35px), `.tl-events-toggle` (`height: 2rem` → ~32px — mobile-only button, worst offender), `.tl-event-search` (`padding: .3rem .55rem; font-size: .73rem` → ~24px). Workshop.css checked — dev-tool only, no mobile requirement ✓. See CSS-34.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Checked `discipline.css` (not covered in D3 Cycle 8). `.disc-tab` desktop (`padding: .65rem 1.05rem; font-size: .85rem`) → ~39px — borderline but acceptable on desktop ✓. Mobile override (`@media (max-width: 500px)`): `.disc-tab { padding: .55rem .7rem; font-size: .78rem }` → ~34px, under 44px — CSS-31. `.journal-btn--sm { font-size: .75rem; padding: .2rem .55rem }` → ~22px at all viewports — CSS-31. No override exists in the mobile block for either. Also checked: `word.css` (no interactive controls at <500px ✓), `notes/index.html` inline styles (none ✓). Gap: CSS-31.*

## Empty State & Loading State Audit — Dimension 2, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Checked new/recently-modified modules since Cycle 9: `workshop.js` — queue no-results state present at line 407 ✓, dossier "not found" / "outside vocabulary" states present ✓, log "no decisions" state present ✓. `timelapse-map.js` — data load failure shows inline message (UX-10 ✓), but `_wireEventSearch()` (lines 900–905) hides all items via `display:'none'` when search matches nothing, with no feedback message — user sees a blank list. See UX-13. `wire.js` — empty verses guard at line 469 ✓. `places.js` — UX-11 fix in place ✓.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). UX-12 fix in place: compare/index.html `.catch()` now shows "Failed to load version data. Please refresh to try again." in `#cmp-hint` ✓. All other modules confirmed clean from prior cycles. No new items found.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). DATA-13 fix in place: `data/translation/notes/1kings/22.json` now exists (22 files in 1kings/ directory ✓). DATA-14 verified clean: `data/commentary/mkt-christ/acts.json` has all 28 chapters including ch 27 (44 verses) ✓ — script `zc-christ-acts-27-28.py` was already run. All other data paths confirmed from Cycle 8 audit ✓. No new data path issues found.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: timelapse.json internal cross-references — all 88 event figure/place refs resolve (0 orphans ✓); wordcloud frequencies.json — 330 words, all 8 genre fields present across all words ✓; Torrey verse-index — 66/66 books (DATA-12 confirmed fixed: isaiah.json has 898 verse entries, jude.json has 72 entries ✓); places.json — 75 entries, 0 missing names/coordinates, all 75 mapId references match valid map IDs in maps.js ✓; MHCC commentary — 66/66 canonical book JSONs present ✓; Ellicott — 66/66 present ✓. No new data path issues found this cycle.*

---

## Performance Audit — Dimension 6, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: `daily.js` devotional fetch — confirmed on-demand only (single selected source fetched on init, not all 5 in parallel ✓); `modal.js` commentary — `loadAndRender(src)` fires a single `loadCommentary()` per source selection, no preloading ✓; `word.js` interlinear — BATCH_SIZE=5 chunks confirmed in place at lines 112–128 ✓; `interlinear.js` reader integration — `loadInterlinear(bk.id)` called once per chapter (single book) ✓; `notes/index.html` search — no-debounce `input` handler fires pure DOM re-render only (localStorage-backed, no fetch) — acceptable ✓. No new performance issues found this cycle.*

---

## Data Path Integrity Audit — Dimension 4, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Checked all new data directories added for Study Workshop (SW-D through SW-M): `data/literary/` (genre.json 33KB, structures.json 24KB ✓ — fetched by `_loadLiterary()`; `devices-glossary.json` 32KB present, precached, and fetched ✓). `data/cultural/` (book-context.json 63KB, frameworks.json 26KB, symbols.json 9KB — all fetched by `_loadCultural()` ✓). `data/ot-in-nt/quotations.json` (65KB — fetched by `_renderOTinNTSection()` ✓). `data/second-temple/context.json` (38KB — fetched by `_renderSecondTempleSection()` ✓). `data/synthesis/` (8 books: galatians, genesis, hebrews, isaiah, john, matthew, psalms, romans — all 5–13KB; missing books handled gracefully by `_loadSynthesis()` returning `[]` on 404 ✓). `data/idioms.json` (77KB) and `data/idioms-index.json` (3.9KB) — both fetched by `_loadIdioms()` ✓. All referenced grammar files present (author-freq, cognate-families, cognate-index, semantic-fields for greek/hebrew — all 66KB–1.4MB ✓). No open items.*

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: all 76 `index.html` files on disk cross-referenced against `sw.js` SHELL_URLS — 71/71 page URLs present ✓; 5 intentional omissions: `study-guides/_template/` (template, not a page), `topics/_template/` (template), `topics/_template-book/` (template), `topics/holy-catholic-church/` (known gap from Cycle 2 — one topic intentionally unprecached), `translation/workshop/` (dev tool, documented Cycle 2). No new pages added since last cycle. No new navigation issues.*

---

## PWA & Offline Audit — Dimension 9, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Verified PWA-10 fix in place: `./data/maps/places.json` (line 215) and `./data/maps/timelapse.json` (line 216) both present in SHELL_URLS ✓. Spot-checked all root-level data JSON files: `topics.json`, `apocrypha-books.json`, `apocrypha-canon-orders.json`, `topics-index.json` — all 4 on disk and in SHELL_URLS ✓. Key eager-fetch files confirmed: `books.json`, `versions.json`, `frequencies.json`, `verses.json` — all precached ✓. No new PWA issues found this cycle.*

---

## Accessibility Audit — Dimension 10, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Found 3 ARIA gaps in `discipline/index.html` — see AUD-20.*

---

## Performance Audit — Dimension 6, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Checked recently modified files: `workshop.js` — all 3 input handlers properly debounced (queue search 200ms, dictionary search 250ms, word-study input 300ms ✓); lazy loading caches in place for all large data files (cognate families 850KB–1.4MB, semantic fields 553KB–998KB — pre-warmed on page load via `_preWarmGrammar()`, single-load thereafter ✓); `_renderDossier()` is synchronous HTML string build — acceptable for one-per-click frequency ✓. `timelapse-map.js` — RAF loop uses `requestAnimationFrame` correctly, cancelled on pause via `cancelAnimationFrame` ✓; `_renderEmpires`/`_renderFigures` both use dirty-check key comparison to skip DOM updates when visible set unchanged ✓; `_animLoop` has 2 live `getElementById('tl-slider')` calls per frame (lines 415, 426) — O(1) hash lookups, no measurable impact at 60fps. No new performance issues found this cycle.*

---

## Performance Audit — Dimension 6, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Found debounce gap: see PERF-9.*

---

## Feature Completeness Audit — Dimension 5, Cycle 10

*Audit pass 2026-06-06 (Cycle 10). Focused on Study Workshop new panels (SW-D through SW-M). (1) Workshop tabs — all 6 passage-level tabs present in HTML (literary, cultural, intertextual, synthesis, cross-refs, commentary) with corresponding `_render*Tab` functions in workshop.js ✓. (2) Literary data — `genre.json` 66/66 books ✓; `structures.json` 20 entries for 16 books (partial, curated — graceful "no data" fallback at line 3142 ✓). (3) Cultural data — `book-context.json` 66/66 books ✓; `frameworks.json` 12 entries; `symbols.json` 4 symbol categories — both partial but graceful ✓. (4) Intertextual — `ot-in-nt/quotations.json` 61 quotations across 11 NT books; missing-passage case shows "no formal quotations" stub ✓. (5) Second Temple — `second-temple/context.json` 30 entries, 60 unique Strong's codes — partial, graceful ✓. (6) Synthesis — 8 books (galatians/genesis/hebrews/isaiah/john/matthew/psalms/romans), 1-3 pericopes each; `_loadSynthesis()` returns `[]` on 404 gracefully ✓. (7) Idioms — 49 idioms, 116 indexed Strong's codes ✓. (8) Topics — still 10 (no new ones added) ✓. (9) Study guide section counts reconfirmed: hebrews=14, romans-1-8=9, ephesians=7, sermon-on-the-mount=6, psalms=5 — NAV-7 still open. No new feature completeness gaps found this cycle.*

---

## Feature Completeness Audit — Dimension 5, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Checked: (1) Echo data — 66/66 files, 5 sparse books (2chronicles, 2john, 3john, esther, nehemiah each 1 entry) are historically reasonable, not stubs ✓. (2) Grammar/workshop data — all 5 files in `data/grammar/` present (greek/hebrew particles, morphology-significance, grammar-debates with 31 items, 23 greek + 15 hebrew particles) ✓; workshop.js phase1/phase2/phase5 all confirmed populated (200/200/17 entries all non-pending) ✓. (3) MKT commentary — all 3 tiers (mkt-original, mkt-context, mkt-christ) have 66/66 books with content ✓. (4) Calvin commentary — 18 empty books are historically expected (no Calvin commentary on history/wisdom books, 2 John, 3 John, Revelation); handled with "No commentary found" message; prior audit decision not to add scope qualifier ✓. (5) Translation workshop — phase1/phase2/phase5.json, index-greek/hebrew.json, glossary-greek/hebrew.json all present; glossary-phrases-greek/hebrew.json are `{}` but not referenced by workshop.js ✓. (6) Parallel reader data — 54 files in `data/parallels/`, 0 stubs ✓. (7) VOTD — 175-entry verses.json with modulo cycling ✓. (8) Book introductions — 66/66 in `data/books/introductions/` ✓. (9) Timelapse — 32 figures / 88 events / 35 places at expected counts ✓. No new feature completeness gaps found this cycle.*

---

## PWA & Offline Audit — Dimension 9, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Verified: (1) APP_CACHE_V `bsw-app-v93` / DATA_CACHE_V `bsw-data-v3` — both preserved in activate handler's `currentCaches` array ✓. (2) Install handler opens APP_CACHE_V with `cache:'reload'` for all 186 SHELL_URLS ✓; offline.html and all its dependencies (style.css, main.js, favicon.svg) present in SHELL_URLS ✓. (3) manifest.json, icon-192.png, icon-512.png, favicon.svg, favicon.ico all in SHELL_URLS ✓. (4) manifest.json shortcuts (read/, verse-study/, notes/) all resolve to real pages ✓. (5) precacheBible (triggered by PRECACHE_BIBLE message from pwa.js): filters stub/group/tier≥3 versions correctly — no 404 storms; caches bible book JSON, crossrefs, interlinear, echoes, torrey/verse-index, Strongs, parallels into DATA_CACHE_V progressively in chunks of 6 with 150ms gaps ✓. (6) Commentary files (74MB, 330 files) correctly excluded from eager precache — cached lazily on first access via DATA_CACHE_V cacheFirst ✓. (7) Grammar/workshop data (`data/grammar/`) not precached — served lazily by DATA_CACHE_V cacheFirst on any `/data/` path; intentional (large, infrequent) ✓. (8) workshop.js and workshop.css explicitly omitted from SHELL_URLS (dev tool exclusion) ✓. No new PWA issues found this cycle.*

---

## Feature Completeness Audit — Dimension 5, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: (1) `data/topics-index.json` — all 10 topic entries without explicit `href` resolve to real `topics/{slug}/index.html` pages (christology, covenants, holy-catholic-church, holy-spirit, justification, prayer, psalms, revelation, romans, sermon-on-the-mount all ✓); all 5 study-guide entries with explicit `href` also verified on disk ✓. (2) Library — all 182 docs in `data/library/index.json` are present on disk (html or json format), none are stubs under 100 bytes ✓. (3) Reading plans — all 8 plan files in `data/plans/` have correct day counts matching `total_days` field (365, 365, 365, 90, 31, 30, 52, 13 — all ✓); all 8 cached in `sw.js` SHELL_URLS ✓. (4) Catechism plans (heidelberg-weekly, wsc-quarterly) removed from `daily.js` home selector but remain accessible via `discipline/?tab=plans` which uses a separate `PLAN_IDS` array covering all 8 ✓. (5) All 5 study guide directories exist (`study-guides/hebrews/`, `romans-1-8/`, `ephesians/`, `sermon-on-the-mount/`, `psalms/`) ✓. (6) All discipline page tabs (plans, devotionals, memory, journal, worship, notes, progress, history) have corresponding `disc-panel` sections; `progress/index.html` and `tracker/index.html` both exist ✓. (7) `plans/index.html` is a redirect to `discipline/?tab=plans` ✓. No new feature completeness gaps found this cycle.*

---

## Resolved — pending archive

### CSS-35 · Synoptic parallel labels showed `&#39;` mojibake *(RESOLVED 2026-06-13)*

**Problem:** `assets/js/synoptic.js` `_buildPanel()` (line 116) set the pericope label via
`labelRow.textContent = escHtml(pericope.label)`. `escHtml` encodes `'` → `&#39;` and
`textContent` does not decode entities, so labels like "John's proclamation" rendered as
"John&#39;s proclamation". The parallels data itself is clean (raw apostrophes).
**Fix:** Removed the `escHtml` wrapper — `textContent` escapes safely on its own (escHtml is
for `innerHTML` only). Bumped `APP_CACHE_V`.
**Verify:** Open a Gospel chapter with a synoptic parallel (e.g. Mark 1), toggle the synoptic
panel — pericope headers show a normal apostrophe. Antipattern documented in
`AUDIT_AGENT_GUIDE.md` dimension D; codebase grep confirms no other `textContent = escHtml`
or `.title/.ariaLabel = escHtml` instances.

---

## Audit — reader-core (Cycle 1, 2026-06-14)

### CSS-36 · Cross-ref note marker color is hardcoded, no dark-mode override *(MEDIUM)* — ✅ RESOLVED 2026-06-14
**Problem:** `assets/css/reader.css` `.reader-xref-note` (lines 1064, 1071) and its
`:hover/:focus-visible` (line 1078) hardcode `color: #4a85a3` / `border-bottom: ... #4a85a3`
and hover `#2d6080`. A grep of `reader.css` finds no `[data-theme="dark"] .reader-xref-note`
override. The inline cross-reference superscript markers next to verses therefore render in
a fixed light-mode mid-blue in dark mode, clashing with the dark surface and reducing contrast.
**Fix:** Replace the hardcoded hexes with a theme variable (e.g. `var(--color-accent)` for
text/border and a darker/lighter shade for hover via `color-mix` or a `[data-theme="dark"]`
override block alongside the other dark overrides in `reader.css`).
**Verify:** Open `/read/` in dark mode on a chapter with cross-refs (e.g. John 3); the xref
note markers should sit in the accent/gold family, not light-mode blue.

### CSS-37 · Reader toolbar touch targets below 44px on mobile *(MEDIUM)* — ✅ RESOLVED 2026-06-14
**Problem:** In `assets/css/reader.css` `@media (max-width: 640px)`, `.reader-browse-bar > button`
(line ~1323) and `.reader-font-size-btn` (lines ~1337–1338) set `min-height: 36px` /
`min-width: 34px`, below the 44px touch-target minimum the rest of the same block uses for the
lookup/browse controls (lines 1281/1285/1307). The font-size +/- buttons and injected toolbar
buttons are harder to tap on phones.
**Fix:** Raise `min-height` to 44px (and `min-width` to 44px for the square font-size buttons)
in that media block, matching the lookup/browse controls.
**Verify:** DevTools at 375px on `/read/`; the font-size and toolbar buttons measure ≥44px.

### CODE-23 · Inline chapter-tracker script lacks required INTENT/CHANGE?/VERIFY *(LOW)* — ✅ RESOLVED 2026-06-14
**Problem:** `read/index.html` lines 68–101 contain an inline IIFE that writes the
`bsw_chapter_read` localStorage key (`recordChapter`) and depends on a `MutationObserver`
reading `window._readerNavState` (set by `reader.js`). Per `working/CLAUDE.md`, code that
writes localStorage and couples to cross-module global state requires `INTENT/CHANGE?/VERIFY`
comments; only a one-line comment is present. If `reader.js` renames or stops setting
`window._readerNavState`, chapter tracking silently breaks with no pointer to the coupling.
**Fix:** Add the three-line comment block; `CHANGE?` must name `window._readerNavState`
(reader.js) and the `bsw_chapter_read` key (read by `discipline`/`progress`).
**Verify:** Comment present; reading a chapter still records it (DevTools → Application →
localStorage `bsw_chapter_read`).

### UX-14 · Library optgroup in the book picker: silent-fail + unbounded growth *(LOW)* — ✅ RESOLVED 2026-06-14 (dead code removed: the Library optgroup no longer appears in the Scripture book picker; library docs are browsed at /library/ and read at /library/read/)
**Problem:** `assets/js/reader.js` `initReaderBrowse` (line 817) appends a "Library" optgroup
to `#reader-book-select` by iterating *every* doc in `LIB_INDEX_URL` (line 823) — now 165 docs,
so the book dropdown carries a 165-item Library group (awkward on mobile). The fetch's
`.catch(function(){})` (line 831) is silent: if the index fails, the Library group simply never
appears with no log or fallback.
**Fix:** Consider capping/grouping the Library optgroup (or moving library navigation out of the
book `<select>` to the dedicated `/library/` browser), and at minimum log/console-warn on the
catch so a failed index load is diagnosable.
**Verify:** `/read/` book dropdown is navigable on a 375px screen; with `LIB_INDEX_URL` blocked
(DevTools offline), the failure is observable in console rather than silent.

---

## Audit — reader-panels (Cycle 1, 2026-06-14)

### CSS-38 · Synoptic panel collapse toggle has no visible focus style *(MEDIUM)* — ✅ RESOLVED 2026-06-14
**Problem:** The synoptic parallel panel label is now a `<button class="reader-synoptic-label">`
toggle (`assets/js/synoptic.js` `_buildPanel`), but `assets/css/reader.css` defines no
`:focus-visible` rule for it (unlike the other reader buttons at lines 501, 698, 1077, 1434).
With `border: none` and custom styling, a keyboard user tabbing onto the collapse toggle gets
no consistent focus ring, so it's hard to tell it's focused.
**Fix:** Add `.reader-synoptic-label:focus-visible { outline: 2px solid var(--color-accent);
outline-offset: -2px; }` to `reader.css` near the other synoptic rules.
**Verify:** On `/read/` (e.g. Mark 1) Tab to a synoptic panel label — a visible focus ring
appears; Enter/Space toggles collapse.

### UX-15 · Interlinear rows for verses with no data are left empty in the DOM *(LOW)* — ✅ RESOLVED 2026-06-14
**Problem:** `assets/js/interlinear.js` `_injectInterlinearForVerse` inserts a
`<div class="reader-interlinear-row">` (line 320) *before* loading data, then on no
book/verse data or error sets `row.innerHTML = ''` (lines 325, 327, 329) instead of removing
it. The empty row stays in the DOM (adding any row margin/padding as blank space under such
verses), and the early-return guard at line 310 (`nextElementSibling … contains
'reader-interlinear-row'`) then treats the empty row as "already injected", so toggling
interlinear off/on won't retry or clean it up.
**Fix:** Replace the three `row.innerHTML = ''` cases with `row.remove();` so verses without
interlinear data leave no residual element and remain re-injectable.
**Verify:** Enable interlinear on a chapter that mixes verses with and without alignment data;
verses without data show no empty gap, and the injected rows count matches verses with data
(DevTools → count `.reader-interlinear-row`).

---

## Audit — cloud-of-witnesses (Cycle 1, 2026-06-14)

*Validator clean: `validate-data.py` passes — 44 fathers all have Biblepedia articles, catena served shape valid. No mojibake antipattern. `decorateCatena` wired at all render sites (modal, reader panel, reader grid, verse-study).*

### UX-16 · Clicking a Cloud-of-Witnesses father name both opens Biblepedia and toggles the voice *(MEDIUM)* — ✅ RESOLVED 2026-06-14
**Problem:** In `assets/js/core.js` `decorateCatena()`, each father name is an
`<a class="cv-name" target="_blank" …>` placed *inside* `<summary class="cv-head">` of the
voice's `<details class="catena-voice">`. There is no `stopPropagation`/`preventDefault`, so
clicking the name to open the father's Biblepedia article (new tab) *also* fires the native
`<summary>` toggle — the voice collapses/expands underneath the user every time they follow
the link. Affects the verse modal, reader commentary panel, reader inline grid, and verse-study.
**Fix:** Stop the link click from toggling the details — e.g. add a delegated listener at the
render sites (or in a small post-decorate wiring step) that calls `e.stopPropagation()` on
clicks of `a.cv-name`; alternatively move the link out of `<summary>` into a non-summary head row.
**Verify:** Open a Gospel verse → Cloud of Witnesses; click a father name — the Biblepedia
article opens in a new tab and the voice's expanded/collapsed state does **not** change.

### CSS-39 · Father-name Biblepedia link has no link affordance *(LOW)* — ✅ RESOLVED 2026-06-14
**Problem:** `.cv-name` (assets/css/style.css:808) styles the father name as
`font-weight:600; color:var(--color-heading)` with no link styling, but in `decorateCatena`
it is rendered as an `<a>` to the father's Biblepedia article. There is no hover, underline,
cursor, or color cue distinguishing it from the non-clickable badges/text, so users cannot tell
the name is a link — the Biblepedia cross-link is effectively undiscoverable.
**Fix:** Add `a.cv-name` affordance in `style.css` — e.g. `a.cv-name { text-decoration: none; }`
`a.cv-name:hover, a.cv-name:focus-visible { text-decoration: underline; }` and a focus-visible
outline; consider a subtle color/dotted-underline cue so it reads as a link at rest.
**Verify:** Hover a father name in a Cloud-of-Witnesses voice — it shows a link affordance
(underline/pointer); keyboard focus shows a visible ring.

---

## Audit — red-letter (Cycle 1, 2026-06-14)

*Validator clean: `validate-data.py` [3] passes — 234 red-letter ranges all valid and in-range (the RL loop is filling OT data; missing OT books are expected, not findings). Speaker chips use `textContent` safely (no mojibake). `.reader-verse--god/--jesus` have light + dark colour overrides.*

### CSS-40 · Red-letter text clashes with same-hue highlight backgrounds *(MEDIUM)* — ✅ RESOLVED 2026-06-14
**Problem:** `applyRedLetter` and `applyHighlights` (assets/js/reader.js) both add classes to the
same `.reader-verse`, so a verse can be **both** red-letter and highlighted. `.reader-verse--jesus`
sets red text `#b03a2e` and `.reader-verse--hl-red` sets a red background `rgba(220,80,80,0.36)`
(assets/css/reader.css ~3694 / ~hl-red); likewise `.reader-verse--god` purple text `#6b2fa0` over
`.reader-verse--hl-purple` purple background. Highlighting a verse of Jesus'/God's words in the
matching colour renders red-on-red / purple-on-purple — very low contrast and hard to read.
**Fix:** Make the two systems coexist — e.g. when a verse is highlighted, let the highlight set
the text colour back to `var(--color-text)` (an `.reader-verse--hl-red.reader-verse--jesus`
override), or give red-letter text a subtle outline/`text-shadow` so it stays legible on any
highlight, or shift the hl-red/hl-purple tints so they don't collide with the speaker hues.
**Verify:** Highlight a red-lettered verse (e.g. a saying of Jesus in Matthew 5) with the red
highlight — the words remain clearly readable in both light and dark mode.

### AUD-21 · Red-letter speaker is conveyed by colour alone (WCAG 1.4.1) *(LOW)* — ✅ RESOLVED 2026-06-14
**Problem:** In the default reader view, the only indication that a verse contains Jesus' words
(red) or God's words (purple) is the text colour (`.reader-verse--jesus/--god` in reader.css).
There is no non-colour cue, so colour-blind users (and anyone who can't distinguish the hue from
body text) get no signal — a WCAG 2.1 SC 1.4.1 (Use of Color) gap. The paragraph view's labelled
speaker chips help, but the inline verse colouring does not.
**Fix:** Add an optional non-colour affordance for red-letter verses — e.g. a small speaker glyph
or left edge-marker on `.reader-verse--jesus/--god`, or a verse-number badge, surfaced at least
when a "distinguish speakers without colour" preference is set. Keep it subtle to preserve the
red-letter reading experience.
**Verify:** With a greyscale/colour-blind simulation, red-letter verses are still distinguishable
from surrounding narrative text.

---

## Audit — modal-verse-study (Cycle 1, 2026-06-14)

*Mostly clean: modal has role="dialog" + aria-modal + aria-labelledby, Escape/backdrop close, focus trap & restore, swipe-dismiss; error/empty states are thorough and specific; no mojibake antipattern; verse-study.css has dark-mode overrides and no stray hardcoded colors. One issue:*

### UX-17 · Cloud-of-Witnesses commentary in verse-study is clamped, undercutting its collapsible voices *(MEDIUM)* — ✅ RESOLVED 2026-06-14
**Problem:** In `assets/js/verse-study.js` (VS-G, lines 819–836), commentary whose
`textContent.length > 800` is wrapped in `.vs-comm-truncated--clamped` (a max-height clamp with a
"Read more ▾" button). When the source is **catena** (Cloud of Witnesses), the body was just
decorated into many `<details open>` voice cards (line 812), whose combined text is almost always
> 800 chars — so it is *always* clamped. The clamp cuts off voices below the fold, and because the
per-voice `<details>` collapse is the intended way to manage that length, the two mechanisms fight:
the reader can't collapse individual voices to navigate (they're hidden by the clamp), and "Read
more" just dumps all of them. Net: the new collapsible-voices UX is defeated in verse-study.
**Fix:** Skip the char-clamp when `src === 'catena'` (the per-voice collapse already handles
length) — e.g. guard the `if (textContent.length > COMM_THRESHOLD)` block with `&& src !== 'catena'`;
or, if a cap is still wanted, collapse all but the first N voices instead of a max-height clamp.
**Verify:** Open verse-study on a verse with many Cloud-of-Witnesses voices (e.g. Matthew 5:3) →
the voices show as individually collapsible cards with no "Read more" max-height clamp over them.


---

# Reader → Great + Synthesis roadmap (merged from working/todo.md, 2026-06-14)

> Consolidated here from the former lowercase `todo.md` (which collided by case with this
> file). This is now the single canonical task list.

## High priority — after Red-Letter & Cloud of Witnesses loops finish

> Gated: start only when **every** Work-Queue row in both `RL_PROGRESS.md` and
> `COW_PROGRESS.md` is `complete`. These rewrite the files those loops are writing, so
> they cannot run concurrently. Full execution plan in `working/POST_LOOP_TASKS.md`.

- [x] **Split commentary into per-chapter files** — DONE 2026-06-14. `split-commentary.py`
      (round-trip verified) → `data/commentary/{src}/{book}/{ch}.json`; `loadCommentary(book,
      src, ch)` per-chapter; `cow-merge.py` emits per-chapter; manifest rebuilt. Psalms+CoW
      verse tap 14 MB → ~112 KB. *(POST_LOOP_TASKS.md Task 1.)*
- [x] **Per-dataset cache versioning** — DONE 2026-06-14. `sw.js` `DATA_VERSIONS` map +
      `_dataSeg`/`_dataCacheForPath`; bumping one dataset no longer evicts the others.
      *(POST_LOOP_TASKS.md Task 2.)*

## Lower priority (non-blocking, can run alongside the loops)

- [ ] Trim SW precache to app-shell only (currently 218 URLs incl. the 1.7 MB Biblepedia index on install).
- [ ] Cloud of Witnesses UX: collapse-all + filter-by-tradition controls (badge metadata already in `_CATENA_ROWS`).
- [ ] Command-palette / launcher for discoverability across the many surfaces.
- [ ] Biblepedia father article → link to their Library works + "verses they comment on".
- [ ] Minify JS in CI (1.45 MB raw across 35 modules).

## Synthesis commentaries — small follow-ups (after the loops produce data)

> Loops + pilot (John 1) built 2026-06-14. See `working/SYNTHESIS_PLAN.md` and the
> `SYNTH_VERSE_*` / `SYNTH_SECTION_*` docs. These are the small UI/cleanup tasks around them.

- [ ] **Voice badges in the commentary block** — render the per-verse `voices` list from
      `data/commentary/cow-synthesis-tags/{book}/{ch}.json` as badges on the commentary panel
      (the Cloud-of-Witnesses / Synthesis sources), so a reader sees at a glance which voices a
      verse was synthesised from. (Owner's idea; the tag data already carries `voices`.)
- [ ] **/about methods note** for the two AI synthesis commentaries (grounding, schools taxonomy,
      tagging, isAI) — parity with the existing MKT methods disclosure.
- [ ] **Flesh out the section-synthesis blade references** — beyond the current voice-name list,
      pull live key-terms (OL/interlinear) and connections (echoes/crossrefs) for the section range.
- [ ] **Cleanup:** remove the empty `data/commentary/synthesis/` dir (leftover; real data lives at
      `data/synthesis/`), and migrate the old per-book `data/synthesis/{book}.json` prototype (8
      books, ref-keyed) into the new per-chapter `data/synthesis/{book}/{ch}.json` schema.
- [ ] **Hide the ✦ synthesis button** on Outline rows that have no section data yet (currently it
      opens a blade that says "not yet"), once coverage is partial — needs a per-chapter synthesis
      index check.

---

# Reader → Great (roadmap, 2026-06-14)

Goal: take the reader from a great *reference aggregator* to an *active study tool*.
Theme: **composition** (bring resources together around a passage) + **output** (let the
user produce and keep something). Working top-down; each item shipped + cache-bumped.

## Passage Study Desk (reader-anchored ~50% right panel — supersedes verse-study)

Decision (2026-06-14): make the reader the primary study desk. A passage-scoped right
panel composes existing data (paragraphs, speakers, original language, places/maps,
echoes, commentary). Absorb the standalone verse-study/word pages later. Phasing:

- [x] **SD-P1 · Shell + Outline + Speakers.** `assets/js/study-desk.js` — "📖 Study"
      toggle in the browse bar opens a right desk (50% desktop / drawer mobile) that reads
      `data/paragraphs/{book}.json` for the current chapter: an **Outline** of pericope
      headings (click → scroll the reader to it, with a flash) and a **Speakers** section
      (who speaks, with verse ranges, colour-coded). Refreshes on chapter change. *(Done 2026-06-14.)*
- [x] **SD-P2 · Key-word usage.** Aggregate interlinear/Strong's across the selection →
      the passage's repeated original-language terms (frequency + gloss). Brings OL into the
      reader. *(Done 2026-06-14: `_fillKeywords` in study-desk.js — counts Strong's codes in
      the in-scope verses, language auto-detected from the G…/H… prefix, repeated terms (≥2)
      shown lemma/translit/gloss + count, each linking to the workshop word study.)*
- [x] **SD-P3 · "Where & when" map (places + period + regional powers, per book/passage).**
      Lazy-load Leaflet (unpkg; `_ensureLeaflet` now waits for the stylesheet too — that was
      the "map not rendering at all" bug). The "Where & when" section is **always available,
      even when a passage names no place**, driven by three generated study files:
        • `data/study/book-context.json` (scripts/generate-book-context.py) — per-book author /
          when+where written / setting era / representative timeline `t`.
        • `data/study/book-places.json` (scripts/generate-book-places.py) — landmark places the
          book discusses (scanned from the text).
        • `data/study/era-powers.json` (scripts/generate-era-powers.py) — slim eras + empire
          polygons/opacity-stages + event→ref index (extracted from maps/timelapse.json).
      It renders a composition header (author/when/where) + a Leaflet map showing the **regional
      powers** of the period as shaded empire polygons (opacity interpolated at the era's `t`),
      the book's **landmark** dots, the **passage's own** places (gold, range-scoped), and a
      ✍ place-of-writing marker. Each place tooltip names the power that **controlled** it
      (point-in-polygon). If a passage's events span multiple eras, it renders **one annotated
      map per period**; otherwise the book's setting era. *(Done 2026-06-14: `_fillMaps`,
      `_buildPeriodMap`, `_passagePeriods`, `_powersAt`, `_controllerOf`, `_detectPlaces`.)*
- [x] **SD-P4 · Connections + notes/export.** `_fillConnections` aggregates cross-refs
      (weight-ranked, deduped, top 12) as `.ref` links; **echoes now reuse the reader's exact
      collapsible card UI** via `renderEchoCardsGrouped` (exported from parallels.js), grouped
      + annotated per verse ("Connections for {book ch:v}"). `_fillNotes` adds a passage-scoped
      notes box (localStorage `bsw_study_notes_{book}_{ch}`) and an **Export study sheet** button
      that assembles context/powers/outline/speakers/keywords/places/connections/notes into a
      downloadable Markdown file. **All sections are collapsible** (`study-sec-toggle`; collapsed
      state persisted in `bsw_study_collapsed`, survives navigation). *(Done 2026-06-14.)*
- [x] **SD-P5 · Range scope.** A from/to verse selector (`_buildRangeControl`/`_wireRange`)
      restricts key words, places and connections to a verse sub-range without leaving the
      chapter; "Whole ch." resets. *(Done 2026-06-14. Used selects rather than click-start/
      shift-click-end to avoid colliding with the reader-audio verse-click handler. Absorbing &
      retiring the standalone verse-study/word pages remains deferred per the earlier
      "redirect later" decision.)*

## Blade stack (drill-down panes — Azure-style) — STARTED 2026-06-14

Decision: scale the desk to deeper tools via a blade stack overlaid on the desk, rather than
more inline sections. Overlay-stack + breadcrumb model (reader keeps its width; mobile = full
screen). `openBlade(type, params, title)` pushes; top renders into `#sd-blade-body`; breadcrumb
walks back; `_BLADES` registry = one render fn per tool.

- [x] **Blade framework** — stack, breadcrumb, back/close, slide-in overlay, scroll-lock, closes
      on chapter change / desk close. *(Done 2026-06-14, study-desk.js.)*
- [x] **Word-study blade** — click a key word → lemma/translit/pronounce + lexicon definition
      (Thayer/BDB via `loadLexicon`) + derivation + occurrences in this passage + all occurrences
      (`data/strongs/refs/{code}.json`, paginated) as `.ref` links + workshop link. *(Done.)*
- [x] **Book-details blade** — "📖 About {book}" button → composes `data/books/introductions/
      {book}.json` (author/date/setting/purpose/themes/outline/key-verses/key-people/context/
      christ-connection/themes-detail) + our `book-context` (written-where+confidence, recipients,
      setting era). *(Done.)*
- [ ] **Next blades** (register a render fn each): commentary (Barnes/Ellicott/catena) · Cloud-of-
      Witnesses father · Biblepedia article · cross-version word ("rendered in KJV/ASV/WEB/BSB") ·
      timeline/event · place detail. Also: absorb/retire standalone word & verse-study pages now
      that the word-study blade exists (the deferred SD-P5 retirement).

## Fix first

- [x] **UX-17 — verse-study clamp defeats Cloud-of-Witnesses voices.** Skip the
      "Read more" char-clamp when `src === 'catena'` (per-voice collapse handles length).
      *(Done 2026-06-14.)*

## Foundational (good → great)

- [ ] **G1 · Performance — per-chapter commentary split + per-dataset cache.** Prereq for
      everything feeling instant. *Gated on the COW/RL loops (see top of this file +
      POST_LOOP_TASKS.md).* Do not start until those loops finish.
- [x] **G2 · Audio read-aloud.** `assets/js/reader-audio.js` — `speechSynthesis` TTS of
      the open passage; verse-by-verse highlight + auto-scroll, "🔊 Listen" toggle in the
      view popover, floating bar (play/pause/stop + speed select, persisted), stops on
      re-render. Graceful no-op where unsupported. *(Done 2026-06-14.)*
- [x] **G3 · Unified "Study this passage" workspace.** The composed layout already exists
      (the verse modal's Commentary / Cross-refs / Word-study / Notes tabs = quick hub;
      the `verse-study` page = deep workspace). Tightened the handoff: the modal's
      verse-study link is now a prominent primary **"📖 Study this verse"** button (was a
      faint link; also fixed its hardcoded blue → theme vars). *(Done 2026-06-14. Possible
      follow-up: an in-reader composite side-panel that shows all layers for the focal
      verse without leaving the reader.)*
- [ ] **G4 · Deeper original-language word study from the reader.** Click a word → full
      lexicon entry + parsing/morphology + gloss + **every occurrence** with filter
      (surface the workshop data inline), not just the interlinear row.
- [ ] **G5 · Contextual where/when.** For narrative passages, a small affordance linking
      the place (maps) and event (timeline/timelapse) — data already exists.

## Differentiators (great → excellent)

- [ ] **E1 · First-class study output.** Assemble highlights + notes + cross-refs into a
      passage study-sheet / outline / verse-map, **exportable** to Markdown/PDF.
- [ ] **E2 · Study-aware search.** Search *within* commentary & the fathers; "find every
      cross-reference into this verse"; phrase/word search across versions.
- [ ] **E3 · Cross-version word study.** "How is this Hebrew/Greek word rendered across
      KJV/ASV/WEB/BSB" — uses the versions + alignment data already present.
- [ ] **E4 · Guided study in the reader.** Surface "today's reading" (plans) and study-
      guide questions inline, so the reader is where the plan happens.
- [ ] **E5 · Grounded passage assistant.** "Ask about this passage", grounded in the
      loaded resources (commentary, fathers, cross-refs) with sources cited. Needs care
      given the no-backend constraint — scope later.
