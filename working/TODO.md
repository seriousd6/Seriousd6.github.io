# Bible Study Website — Working TODO

Track progress here. Mark items `[x]` when complete.
Completed items are archived in `working/todo-archive.md`.

---

## Z4–Z8 MKT Commentary Suite

**Goal:** Three original verse-by-verse commentaries for all 66 books, an echo/fulfillment data layer, and a key-term concordance. Uses the same static script + guide + work queue pattern as the MKT translation.

**Commentaries:**
- **Z6 `mkt-original`** — Original Language: why each translation choice, what English misses (aspect, idiom, wordplay, semantic range, honor-shame, tense)
- **Z7 `mkt-context`** — Historical Context: what the original audience understood, ANE/Second Temple background, intertextual echoes
- **Z8 `mkt-christ`** — "Christ in Every Verse": types, shadows, fulfillments, prophecy — honest about directness (direct/type/shadow/theme/revelation of God)

### Infrastructure (build first — prerequisites for everything below)

- [x] `Z_COMMENTARY_SCRIPT_GUIDE.md` — static script boilerplate (load/save/merge helpers), HTML conventions, source data checklist
- [x] `Z_COMMENTARY_AGENT_GUIDE.md` — content principles and length targets for all three commentary types
- [x] `Z_PROGRESS.md` — full work queue (66 books × 3 commentaries + echo layer, ≤6ch units, same claim protocol as MKT_PROGRESS.md)
- [x] `Z_AGENT_PROMPT.md` — paste prompt for agent sessions (mirrors MKT_AGENT_PROMPT.md)

### Z4 — Echo & Fulfillment Data Layer

**Note: Echoes replace Parallels.** The existing parallels feature (`data/parallels/`, `loadParallels()`, the parallels panel) was the prototype of what echoes are designed to be. Once Z4 data is generated, the parallels panel is replaced by the Echoes & Fulfillments panel and `loadParallels()` is retired.

**Parallels absorption (do before writing any echo scripts):**
- [ ] Audit `data/parallels/` — review all entries for the books being processed
- [ ] Absorb `prophecy-source` entries → echo type `fulfillment`; `quotation` → `quote`; `parallel` → `theme` or `allusion` where substantive
- [ ] Add the `note` field that parallels entries lack (a brief argument for the connection)
- [ ] Document the absorption step in `Z_COMMENTARY_SCRIPT_GUIDE.md`

**Build:**
- [ ] Echo script units added to `Z_PROGRESS.md` work queue
- [ ] `assets/js/core.js` — add `ECHOES_ROOT`, `loadEchoes()`, `echoesCache`; retire `loadParallels()` once echoes covers same books
- [ ] `assets/js/verse-study.js` — replace parallels panel with "Echoes & Fulfillments" panel; type badge + `.ref` link + note per echo
- [ ] `assets/js/reader.js` — replace parallels panel reference with echoes
- [ ] Agents generate `data/echoes/{book}.json` via `zc-echo-{book}-{start}-{end}.py` (NT first)

Echo types: `quote` | `allusion` | `type` | `shadow` | `theme` | `fulfillment`

### Z5 — Key Term Decision Commentary

- [ ] `scripts/z5-terms-greek.py` — hardcoded decision notes for all Greek dispute_level≥2 terms (~60 entries)
- [ ] `scripts/z5-terms-hebrew.py` — Hebrew dispute_level≥2 terms (~40 entries)
- [ ] `data/translation/term-commentary.json` — output with lemma, decision_note HTML, key_verses, tradition_map
- [ ] `tools/terms/index.html` — searchable concordance page (tg-* CSS layout; left list, right panel)

### Z6–Z8 — Commentary UI Registration

- [ ] `assets/js/core.js:635` — add 3 entries to `COMMENTARY_SOURCES`:
  - `{ id: 'mkt-original', label: 'Original Language (MKT)', attr: '...' }`
  - `{ id: 'mkt-context',  label: 'Historical Context (MKT)', attr: '...' }`
  - `{ id: 'mkt-christ',   label: 'Christ in Every Verse (MKT)', attr: '...' }`
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

*(Completed 2026-06-03 — see todo-archive.md. WD-L complete 2026-06-03. WD-M data-blocked.)*

---

*(WD-A complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-B complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-C complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-D complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-E complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-F complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-G complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-H complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-I complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-J complete — consolidated into WD-D — see working/todo-archive.md 2026-06-05)*

---

*(WD-K complete — see working/todo-archive.md 2026-06-05)*

---

*(WD-L and WD-M claimed — see working/inprogress-wd-lm-todo.md)*

---

## Library Content Cleanup — LOW items remaining

Completed sections archived. Two optional polish items remain open.

*(Pascal Pensées claimed — see working/inprogress-pascal-pensees-todo.md)*

---

### LOW — Remaining polish

- [x] **Newman Apologia `[Pg N]` spans** — stripped 418 `.pagenum` spans from `newman-apologia.html` via BeautifulSoup.

- [x] **Smalcald Articles Part III sub-article `lib-article` nesting** — added `lib-article__num` (Roman numeral) and `lib-article__text` wrapper to all 13 articles; h3 updated to show title only.

---

## Bible Reader Improvements

**Evaluation (2026-06-03):**

The reader is feature-rich — multi-ref lookup, book introductions, compare mode, interlinear,
parallels, three right-panel tabs, six layout modes — but several implementation problems
undercut the experience. The most serious is a split navigation model: sidebar chapter buttons
use in-page rendering while prev/next chapter buttons do a full `window.location.href` page
reload. The toolbar is also severely overcrowded. Below items are roughly priority-ordered.

---

*(RD-A complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-B complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-C complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-E complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-F complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-G complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-H complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-I claimed — see working/inprogress-rdm-todo.md)*

---

*(RD-J complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-K complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-L complete — see working/todo-archive.md 2026-06-05)*

---

*(RD-M claimed — see working/inprogress-rdm-todo.md)*

---

## Verse Study Page Improvements

*(Claimed — see working/inprogress-vs-todo.md)*

*(VS-A complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-B complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-C complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-D complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-E complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-F complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-G complete — see working/todo-archive.md 2026-06-05)*

---

*(VS-H complete — see working/todo-archive.md 2026-06-05)*

---

## Reference Data Expansion

New commentary sources, dictionary upgrades, and one index that can be built from data
already on the site.

*(REF-B complete — Robertson's Word Pictures fetched; see archive)*
*(REF-C complete — Wesley's Notes fetched; see archive)*

*(REF-D complete — Ellicott's Commentary added; 22,300 sections; see working/todo-archive.md)*

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

*(Reformation-era works — 4 of 5 complete; see working/todo-archive.md. 1 DATA BLOCKED below.)*

- [x] **Zwingli, On the True and False Religion (1525)** — Completed via 1929 Preble translation (public domain 2025); 9 sections. See archive.org `latinworkscorres03zwin`.

- [ ] **Melanchthon, Loci Communes (1521)** — **DATA BLOCKED**: All English translations (Hill 1944, Manschreck 1965) are under copyright. No public domain English translation exists.

*(Missions & biography works claimed — see working/inprogress-missions-bio-todo.md)*

*(Apologetics texts claimed — see working/inprogress-lib-apologetics-todo.md)*

*(Council texts complete — see todo-archive.md. 7 docs added: CP2, CP3, Nic2, Lat4, Trent, VatI, Jer1672.)*

- [x] **Audit and add missing council texts** — completed 2026-06-03. Seven councils added across ecumenical, RC, and Orthodox traditions. Deferred: Vatican II (copyright unclear), Jassy 1642, CP4/Photian (no PD English translation), Hesychast (too specialized).

  **Still needed (deferred):**
  - Vatican II — *Lumen Gentium*, *Dei Verbum*, *Sacrosanctum Concilium*; copyright status unclear on usable English translations
  - Constantinople IV / Photian Council (879–880) — no clear public domain English translation available
  - Hesychast Councils (1341, 1347, 1351) — no standard public domain English text
  - Council of Jassy (1642) — *Confession of Peter Mogila*; availability unclear


*(Creeds & Confessions expansion claimed — see working/inprogress-lib-creeds-todo.md)*

*(Liturgical & church-order documents claimed — see working/inprogress-liturgical-docs-todo.md)*

*(Papal encyclicals claimed — see working/inprogress-papal-encyclicals-todo.md)*

---

## Maps Page Improvements

### Phase 1 — UX & Structure *(complete)*
All Phase 1 items are implemented: `ERA_GROUPS` drives nav section headers; `_buildNav()` renders group labels; `_selectMap()` has URL hash deep-linking; `_overviewHtml()` renders the overview panel; `_showCityDetail()` handles the `significance` field; city-detail panel is an `position:absolute` overlay; reset button is wired via `_wireResetButton()`. All CSS present.

*(Maps Phase 2/3 complete — see working/inprogress-maps-phase23-cona-archive.md for archive pass)*

---

## Home Page Improvements

*(Completed 2026-06-03 — see todo-archive.md. HP-A through HP-I all done.)*

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

*(CON-A complete — see working/inprogress-maps-phase23-cona-archive.md for archive pass)*

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

*(Apocryphal Reader — complete; data fetched 2026-06-03 — see working/todo-archive.md)*

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

## Word Cloud — Post-Shipping Improvements

*(Completed 2026-06-03 — see todo-archive.md. All WC-A through WC-G items done.)*

---

*(Studies SG-A through SG-I claimed — see working/inprogress-studies-sg-todo.md)*

---

*(CMT-A through CMT-I claimed — see working/inprogress-cmt-todo.md)*

---

## Code Comment Audit — Dimension 1

*Audit pass 2026-06-05. Files missing required INTENT/CHANGE?/VERIFY comments on exported functions,
localStorage write paths, algorithms, and cross-module couplings.*

---

*(CODE-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-3 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-4 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-5 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-6 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-7 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-8 complete — see working/todo-archive.md 2026-06-05)*

---

## Empty State & Loading State Audit — Dimension 2

*Audit pass 2026-06-05. Pages and panels with missing error feedback on fetch failure or empty data.*

---

*(UX-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(UX-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(UX-3 complete — see working/todo-archive.md 2026-06-05)*

---

*(UX-4 complete — see working/todo-archive.md 2026-06-05)*

---

*(UX-5 complete — see working/todo-archive.md 2026-06-05)*

---

## Mobile Responsiveness Audit — Dimension 3

*Audit pass 2026-06-05. CSS code-reading audit — no browser DevTools available; findings based on media-query analysis and layout calculations.*

---

*(CSS-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-3 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-4 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-5 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-6 complete — see working/todo-archive.md 2026-06-05)*

---

## Data Path Integrity Audit — Dimension 4

*Audit pass 2026-06-05. Verified fetch paths against actual files in `data/`. All commentary sources (mhcc, ellicott, jfb, clarke, calvin, barnes, rwp, wesley) have all 66 books. Crossrefs, echoes, interlinear all have full 66-book coverage. Plans, library docs, manifest shortcuts, SHELL_URLS in sw.js, and all main nav hrefs verified present.*

---

*(DATA-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(DATA-2 complete — see working/todo-archive.md 2026-06-05)*

---

## Feature Completeness Audit — Dimension 5

*Audit pass 2026-06-05. Checked: word cloud scope data (all 11 scopes have non-zero ot/nt/genre counts), study guide session tabs (5 guides, all tabs have real content), all 10 topic pages (no stubs — 285–2538 lines of real content), manifest shortcuts (3/3 resolve), sidebar nav links (all resolve), NT Daily devotional rotation logic. Reading plans, library docs, and commentary sources already verified in Dimension 4.*

---

*(AUD-1 complete — see working/todo-archive.md 2026-06-05)*

---

## Performance Audit — Dimension 6

*Audit pass 2026-06-05. Read: `assets/js/word.js`, `assets/js/search.js`, `assets/js/reader.js`, `assets/js/verse-study.js`, `assets/js/daily.js`, `assets/js/core.js`. Verified: search is 250ms-debounced; daily.js fetches one devotional on load (not all 5); vsRenderVersionCompare is lazy-loaded via IntersectionObserver; VOTD file is 2.7KB (not a concern). Measured: OT interlinear = 39 files × avg 205KB = 8MB total; NT interlinear = 27 files = 3.5MB; all 66 KJV books = 4.4MB.*

---

*(PERF-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(PERF-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(PERF-3 complete — see working/todo-archive.md 2026-06-05)*

---

*(PERF-4 complete — see working/todo-archive.md 2026-06-05)*

---

*Audit pass 2026-06-05 (Cycle 2). Read: `assets/js/verse-study.js`, `assets/js/daily.js`, `assets/js/ol-companion.js`, `assets/js/apocrypha-reader.js`, `assets/js/word.js`, `assets/js/reader.js`, `assets/js/core.js`. Verified: daily.js fetches only selected devotional (confirmed); `loadLibVerseIndex` is properly cached (confirmed double-call is a no-op at network level); IntersectionObserver deferral confirmed (line 819); word.js BATCH_SIZE=5 confirmed implemented. New finding: vsRenderVersionCompare fires 11 uncapped concurrent fetches — PERF-4.*

---

*Audit pass 2026-06-05 (Cycle 3). Read: `assets/js/lib-browser.js`, `assets/js/ol-companion.js`, `assets/js/reader.js`, `data/library/index.json` (92 KB, 182 docs). Verified: lib-browser.js search debounced 200ms/150ms ✓; `_saveSectionIdx` only fires on pagination not scroll ✓; scroll spy uses `{ passive: true }` ✓; `loadCrossRefs` in core.js caches by bookId with promise-store (concurrent verse renders share pending fetch) ✓; ol-companion.js fetches cached after first book load ✓; library index 92KB is reasonable ✓. New finding: `data/translation/notes/` book files are 3.8–5.4 MB; ol-companion.js fetches the entire book file to render any single verse — PERF-5.*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

## Performance Audit — Dimension 6, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Checked: verse-study new section fetch cascade (new sections trigger: `_naveLoad()` 1.4MB, `_naveLoadVidx` small, 3× dict verse-indexes small, `loadLibVerseIndex` small). Full indexes (Easton 753KB, Smith 833KB, ISBE 1.9MB) are NOT loaded by verse-study — `renderVSDictionary` only fetches the per-book verse-index files and renders link chips; full entry content loads only when user navigates to the dictionary page. Single shared promise `_naveLoading` prevents redundant fetches within a session. Finding: `_naveTopicsForVerse` loads the full 1.4MB Nave's index before checking if the verse has any topics.*

---

*(PERF-6 complete — see working/todo-archive.md 2026-06-06)*

---

## Performance Audit — Dimension 6, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: `app.js` init sequence (all page-specific inits guarded by landmark element checks ✓); `wordcloud.js` `frequencies.json` fetch is gated on `wc-container` element ✓; `places.js` 16KB places.json — trivially small, no issue; `search.js` debounced 250ms ✓. Focus: `terms.js` `runAutoTagTerms()` and `runAutoTagPlaces()` idle callback behavior on pages with no taggable content. One issue found.*

---

*(PERF-7 complete — see working/todo-archive.md 2026-06-06)*

---

## Performance Audit — Dimension 6, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: `library.js` OMNI_SOURCES load sequencing — all 5 secondary dict sources (Smith 852KB, ISBE 1.9MB, Hitchcock 180KB, Nave 1.4MB, Torrey 546KB) fire in parallel after Easton resolves, incremental `_buildOmniIndex()` rebuilds are intentional progressive enhancement ✓; `lib-reader.js` sequential index + doc fetch chain ✓; `lib-browser.js` search debounced 150ms/200ms ✓; `verse-study.js` loadVerseSections fires loadInterlinear + loadStrongs eagerly for interlinear table render (needed, by design) ✓; `vsRenderVersionCompare` now uses BATCH_SIZE=5 (PERF-4 fixed) ✓; `apocrypha-reader.js` metadata files <4KB ✓; `ol-companion.js` now fetches per-chapter 20–50KB (PERF-5 fixed) ✓. One issue found: dictionary search input lacks debounce.*

---

*(PERF-8 complete — see working/todo-archive.md 2026-06-06)*

---

## Visual System Audit — Dimension 7

*Audit pass 2026-06-05. Checked: hardcoded hex colors across all `assets/css/*.css`; dark mode blocks in style.css, topic-shell.css, topic-guide.css, timeline.css, timelapse.css, maps.css, lib-reader.css, word.css; `--tg-accent` usage consistency; `--color-heading` variable definition; template placeholder text (none found). Dark mode variables defined: `--color-bg`, `--color-surface`, `--color-primary`, `--color-text`, `--color-muted`, `--color-border`. Notably absent: `--color-heading` — never defined in style.css, only used via fallback.*

---

*(CSS-7 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-8 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-9 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-10 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-13 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-14 complete — see working/todo-archive.md 2026-06-05)*

---

*Audit pass 2026-06-05 (Cycle 2). Read: `assets/css/ol-companion.css`, `assets/css/apocrypha.css`, `assets/css/workshop.css`, `assets/css/discipline.css`, `assets/css/memorize.css`, `assets/css/devotionals.css`. Verified: apocrypha.css `#fff` uses are on primary-colored backgrounds (acceptable). workshop.css status badges have dark mode; dispute/action-button pastels do not (workshop is dev-tool, lower priority). memorize.css rate button colors (again/hard/good/easy) have no dark mode but remain legible since they are bright saturated on dark. discipline.css plan-done and calendar-check missing (tracked CSS-14). ol-companion.css tier labels missing (tracked CSS-13).*

---

*Audit pass 2026-06-05 (Cycle 3). Read: `assets/css/verse-study.css`, `assets/css/lib-browser.css`. Verified: no px font sizes in either file ✓; `#fff` in `lib-browser.css` lines 576/693 is white text on primary-colored active chips (acceptable pattern) ✓; `lb-author-dot--*` mid-range colors remain visible in dark mode ✓. New findings: verse-study.css echo-badge light pastels have no dark mode — CSS-17. lib-browser.css tradition abbrev badges use dark hex colors invisible in dark mode + `mark.lb-find-mark` bright yellow — CSS-18.*

---

*(item complete — see working/todo-archive.md 2026-06-06)*

---

*(item complete — see working/todo-archive.md 2026-06-06)*

---

*Audit pass 2026-06-06 (Cycle 4). Read: `assets/css/dictionary.css`, `assets/css/library.css`, `assets/css/lib-reader.css`, `assets/css/lib-progress.css`. Verified dark mode coverage: lib-reader.css covers `.lr-sidebar-inner`, `.lr-pager-num`, `.lr-vol-chip`, `.lr-find-bar`, `.lr-find-input`, `mark.lr-find-mark` (amber `#92610a`) — clean ✓. lib-progress.css covers `.lp-stat` and `.lp-bar-track` — clean ✓. Finding: dictionary badge colors (`#1e3a5f` ISBE navy, `#065f46` Hitchcock green, `#1d4ed8` Smith blue) are set as inline JS styles — cannot be overridden by CSS dark mode rules; `library.css` `.lib-badge--*` tradition classes use hardcoded hex with no dark mode block; `lib-progress.js` `.lp-trad-chip` also uses inline style colors.*

---

*(CSS-20 complete — see working/todo-archive.md 2026-06-06)*

---

## Visual System Audit — Dimension 7, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked CSS files not deeply audited for dark mode in prior cycles: `timeline.css` (dark mode covers spine-wrap, node-dot, tl-detail, legacy teal/blue colors ✓), `timelapse.css` (map stays intentionally light in both modes; dark mode covers tooltips ✓), `maps.css` (dark mode covers map-container bg and site-item-star ✓), `study-guide.css` (no hardcoded hex ✓), `wordcloud.css` (only `background: none` ✓), `topical.css` (no hardcoded hex outside dark mode ✓), `topic-guide.css` (only `#fff` on accent backgrounds ✓). One gap found: `topic-shell.css` `.nav-panel` (mobile slide-in nav drawer) has `background: #fff` with no dark mode override.*

---

*(CSS-22 complete — see working/todo-archive.md 2026-06-06)*

---

## Visual System Audit — Dimension 7, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked CSS files not yet audited for dark mode: `study-nav.css` (parchment vars, no dark mode block — intentional fixed-theme aesthetic for prayer/revelation study pages ✓), `daily.css` (checker/badge colors #4caf50/#b71c1c stay saturated in dark mode, remain legible ✓), `reader.css` (highlight verse number overrides covered by both [data-theme="dark"] and @media dark blocks ✓; `.reader-xref-note:hover { color: #2d6080; }` hover state ~2.9:1 contrast on dark bg — borderline but only on hover of hidden-by-default footnote markers, LOW priority), `bible-ui.css` (search-chip + modal verse highlight colors all have dark overrides ✓). Critical finding: `book-study.css` (987 lines, zero dark mode blocks) hardcodes `body.bk-ot/bk-nt` background-color as light values, overriding `var(--color-bg)` from style.css in dark mode, causing `--color-text: #e8dfc8` to render on `#f8f9fc` background — 1.27:1 contrast, near-invisible text on Romans and Revelation pages in dark mode.*

---

*(CSS-24 complete — see working/todo-archive.md 2026-06-06)*

---

## Visual System Audit — Dimension 7, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked remaining CSS files: `wordcloud.css` (0 dark mode blocks, 0 hardcoded hex colors — all `var()` — clean ✓); `dictionary.css` badge elements (`vs-dict-src-badge`, `dict-filter-chip__badge`, `dict-item__src`) use `color: #fff` on dark-colored backgrounds (deep blues/purples/reds); both `[data-theme="dark"]` and `@media` dark blocks exist for these — clean ✓; `ol-companion.css` `.olc-disp-*/olc-tier-*` have both dark override mechanisms ✓; `timeline.css` `.tl-detail-crossover__label` covered at lines 533–534 ✓; `topic-shell.css` cream (#e8d9bb) on dark topic header — intentional fixed contrast ✓. Critical finding: `apocrypha.css` has 3 selectors with `color: #fff` on `background: var(--color-primary)` (active chapter btn, active canon chip, nav btn hover) — in dark mode primary = #e8c87a golden, so white fails ~1.3:1 — CSS-25.*

---

*(CSS-25 complete — see working/todo-archive.md 2026-06-06)*

---

## Visual System Audit — Dimension 7, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked `maps.css` and `timelapse.css` for dark mode gaps. `maps.css`: `.maps-site-item-star #b00010` and `.maps-map-container #e8f4f8` already have dark overrides (lines 826–831) ✓. Found 4 hover-state rules using `color: #fff` on `background: var(--color-primary)`: `.maps-timelapse-link:hover`, `.maps-tl-chip:hover`, `.maps-refs-chip:hover`, `.maps-city-map-chip:hover` — all inconsistent with `.maps-city-ref-chip:hover` which correctly uses `var(--color-on-primary, #fff)` — CSS-27. `timelapse.css`: tooltip dark overrides present (Cycle 6) ✓. Found 4 elements with `background: var(--color-primary); color: #fff` lacking dark mode overrides: `.tl-btn-play`, `.tl-btn-continue`, `.tl-events-toggle`, `.tl-map-link:hover` — CSS-28.*

---

*(CSS-27 complete — see working/todo-archive.md 2026-06-06)*

---

*(CSS-28 complete — see working/todo-archive.md 2026-06-06)*

---

## Visual System Audit — Dimension 7, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Checked `bible-ui.css` (remaining after Cycle 8 covered maps/timelapse/apocrypha/book-study). Found 3 elements with colour failures in dark mode: `.search-go-btn` uses `background:var(--color-primary); color:var(--color-text)` — dark text on golden fails; `.bsw-modal__verse-study-link` is styled blue-on-light but the dark block only sets the border without resetting link colour to accessible blue; `.bsw-place-tip__link:hover` hardcodes `color:#fff` on `background:var(--color-primary)` hover — golden/white 1.3:1 fail. See CSS-30.*

---

*(CSS-30 complete — see working/todo-archive.md 2026-06-06)*

---

## Navigation & Discoverability Audit — Dimension 8

*Audit pass 2026-06-05. Checked: all main sidebar nav links (all resolve — `read/`, `apocrypha/`, `search/`, `studies/`, `discipline/`, `history/`, `library/`, `library/progress/`, `translation/workshop/`); all 10 topic cards → real pages; all 5 study guide cards → real pages; history hub 4 iframe tabs (all 4 `data-src` targets exist: `timeline/`, `church-history/`, `maps/`, `maps/timelapse/`); `?minimal=1` mode (correctly early-returns from `buildSidebar()` before both sidebar and mobile topbar are built); `tracker/` (embedded as iframe in `discipline/?tab=history`); `compare/` (linked via `COMPARE_URL` in `modal.js` line 411); `wordcloud/` (embedded as iframe in `search/?tab=wordcloud`). Redirect stubs (`plans/`, `journal/`, `memorize/`, `devotionals/`, `reflections/`) all redirect correctly to discipline tabs.*

---

*(NAV-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(NAV-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(NAV-3 complete — see working/todo-archive.md 2026-06-05)*

---

*Audit pass 2026-06-05 (Cycle 2). Checked: all pages on disk vs. nav entries; data/topics.json vs. topics/ dirs (all resolve); study-guides hrefs in topics.json (all 5 resolve); `worship/` redirect stub (correctly points to discipline/?tab=worship); NOTES_URL vs. BOOKMARKS_URL consumption (BOOKMARKS_URL used in reader.js:1101; NOTES_URL never imported — see NAV-3); `tools/terms/` (not yet created — Z5 planned work). No broken nav links, no orphaned topics, no missing study guides.*

---

*Audit pass 2026-06-06 (Cycle 3). Read: `assets/js/main.js` NAV array, `assets/js/verse-study.js` prev/next logic (lines 222–243), `verse-study/index.html`, `assets/css/style.css` sidebar layout. Verified: `apocrypha/` ✓ in NAV (line 56); `word/` ✓ linked via WORD_URL from search + verse-study tokens; `bookmarks/` ✓ linked via BOOKMARKS_URL (reader.js:1101); `notes/` ✓ linked via NOTES_URL (reader.js:1164 + modal.js:992); `verse-study/` ✓ linked from reader modal (modal.js:426); `study-guides/` ✓ linked from topics.json; `church-history/` ✓ linked from history hub iframe; all four pages have index.html ✓; verse-study page correctly loads main site sidebar (body.padding-left via style.css:72) ✓. New finding: verse-study prev/next hides at chapter boundaries with no cross-chapter fallback — NAV-4.*

---

*(NAV-4 complete — see working/todo-archive.md 2026-06-06)*

---

*Audit pass 2026-06-06 (Cycle 4). Checked all `*/index.html` files on disk against nav reachability. All top-level pages accounted for ✓ (redirect stubs, iframe-embedded pages, JS-linked pages all verified in prior cycles). Library sub-pages: old church father profile pages and major confessions are in SHELL_URLS ✓. New finding: 8 new library standalone pages exist on disk but have no navigation links pointing to them and are not in SHELL_URLS. Library browser opens all docs inline (not by navigating to `library/{id}/`); full-screen reader uses `library/read/?doc={id}`. These 8 standalone pages are orphaned — accessible only by direct URL.*

---

*(NAV-5 complete — see working/todo-archive.md 2026-06-06)*

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: `data/topics.json` vs `topics/` directories (all 10 slugs match on-disk dirs ✓); study-guide hrefs in topics.json vs `study-guides/` (all 5 match ✓); `studies/index.html` card hrefs (all 15 card links resolve ✓); `search.js` `_hubTabs` vs HTML iframe `data-src` attributes (topics → `../topics/?minimal=1` ✓, guides → `../study-guides/?minimal=1` ✓, dictionary ✓, wordcloud ✓); `history/index.html` iframe data-src values (all 4 tabs ✓); `discipline/index.html` `?tab=` parameter handling (moreTabs `notes/progress/history` correctly handled; `?tab=history` → `disc-history` panel with tracker iframe ✓); `translation/workshop/` in sidebar footer (`wsLink` at main.js:356 ✓); all library standalone pages vs `sw.js` SHELL_URLS (29 entries, all match real index.html files ✓); `library/read/` and `library/progress/` both in SHELL_URLS ✓; `LIB_READER_URL` at `core.js:42` exported but never imported (inline `_resolve()` used in lib-browser.js:857 and lib-progress.js:130 instead — cosmetic dead export, LOW). One gap found: 2 empty stub dirs in `library/`.*

---

*(NAV-6 complete — see working/todo-archive.md 2026-06-06)*

---

## PWA & Offline Audit — Dimension 9

*Audit pass 2026-06-05. Checked: `sw.js` cache strategy (`networkFirst` for navigation, `cacheFirst` for data/assets), install SHELL_URLS completeness, activate cleanup logic (correct — deletes non-current caches), `manifest.json` (shortcuts, icons, colors), `offline.html` (real content with working links, loads `main.js` correctly as non-module), `pwa.js` (`initPWA`, `triggerPrecache`, `_showSWUpdateToast`), `precacheBible` chunked fetching. All 200+ SHELL_URLS resolve to real files on disk — no broken precache paths. `workshop.js`/`workshop.css` intentionally absent (dev tool). `data/votd/verses.json` is a single pre-fetched file (no per-day files). 4 issues found.*

---

*(PWA-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(PWA-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(PWA-3 complete — see working/todo-archive.md 2026-06-05)*

---

*(PWA-4 complete — see working/todo-archive.md 2026-06-05)*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

*Audit pass 2026-06-05 (Cycle 2). Checked all SHELL_URLS against disk. New assets correctly included: `apocrypha.css/js`, `ol-companion.css/js`, `discipline.css/js`, `memorize.css/js`, `lib-browser/progress/reader.css/js`, `timelapse-map.js`, `places.js`, `worship/index.html`, `study-guides/*.html`. Intentionally absent (dev tool): `workshop.js`, `workshop.css`. Missing: `data/apocrypha-books.json` + `data/apocrypha-canon-orders.json` (tracked PWA-5); `topics/holy-catholic-church/index.html` (LOW — not all topics are precached, just the most popular); `translation/workshop/index.html` (intentional — dev tool, not for offline use).*

---

*Audit pass 2026-06-06 (Cycle 3). Read: `sw.js` SHELL_URLS (lines 29–203), `manifest.json`. Verified: `bsw-app-v66` current; PWA-5 resolved in archive ✓; all 26 non-workshop CSS files in SHELL_URLS ✓; all JS files in SHELL_URLS ✓; manifest.json shortcuts (read/, verse-study/, notes/) all resolve ✓; `translation/workshop/index.html` intentionally absent ✓. New finding: `library/progress/index.html` exists on disk and is in the sidebar nav but missing from SHELL_URLS — PWA-6.*

---

*(PWA-6 complete — see working/todo-archive.md 2026-06-06)*

---

*Audit pass 2026-06-06 (Cycle 4). Read: `sw.js` SHELL_URLS (lines 29–204), all `assets/css/*.css` and `assets/js/*.js` on disk, all `data/` top-level JSON files >200KB. Verified: `bsw-app-v69` current; all 26 CSS files ✓; all 32 JS files (workshop.js intentionally absent) ✓. Cross-referenced large data files vs SHELL_URLS — found two gaps: (1) `library/read/index.html` not in SHELL_URLS despite being the target of every "Open in full-screen reader" link in the library; (2) `data/dictionary/index.json` (756KB) not in SHELL_URLS while the conceptually equivalent `data/smith/index.json` (836KB) IS — Easton's dictionary page fails offline on first visit while Smith's works. Large files intentionally lazy-cached: `data/isbe/index.json` (1.9MB), `data/topical/nave.json` (1.4MB), `data/library/search-index.json` (920KB), all interlinear/crossref/commentary files — all correct per cacheFirst strategy.*

---

*(PWA-7 complete — see working/todo-archive.md 2026-06-06)*

---

*(PWA-9 complete — see working/todo-archive.md 2026-06-06)*

---

## Accessibility Audit — Dimension 10

*Audit pass 2026-06-05. Checked: focus styles (sidebar, modal, reader, `.ref` links), ARIA roles and labels (sidebar collapse button, hamburger, nav, modal dialog, reader controls, discipline tabs), modal keyboard trap (`trapFocus` in `modal.js` — complete: Escape closes, Tab cycles, `_lastFocused.focus()` restores on close), color contrast (all primary color pairs pass WCAG AA), `alt` attributes (no `<img>` elements in main pages — site uses CSS/SVG/emoji icons), theme toggle button accessible name (visible text content serves as label), `discipline-strip.js` mobile label handling. Modal, reader, and search ARIA patterns are solid. 4 issues found.*

---

*(AUD-2 complete — see working/todo-archive.md 2026-06-05)*

---

*(AUD-3 complete — see working/todo-archive.md 2026-06-05)*

---

*(AUD-4 complete — see working/todo-archive.md 2026-06-05)*

---

*(AUD-5 complete — see working/todo-archive.md 2026-06-05)*

---


*(item complete — see working/todo-archive.md 2026-06-05)*

*(item complete — see working/todo-archive.md 2026-06-05)*

---

*Audit pass 2026-06-05 (Cycle 2). Checked: `apocrypha-reader.js` (canon chips, chapter buttons — ARIA gaps found), `ol-companion.js` (token buttons — ARIA gap found), `lib-browser.js` (solid ARIA throughout — aria-label on all controls, aria-current on active doc link), `verse-study.js` section toggles (correct — aria-expanded + aria-controls). No new focus-order or contrast issues found beyond those tracked in cycles 1 & 2.*

---

*Audit pass 2026-06-06 (Cycle 3). Read: `verse-study/index.html`, `assets/js/verse-study.js`, `assets/js/wire.js`, `assets/js/ol-companion.js`, `assets/js/apocrypha-reader.js`, `assets/js/lib-browser.js`. Verified: lib-browser.js controls all labeled ✓; wire.js handles Enter + Space on `.ref` links ✓; verse-study token buttons have aria-label ✓; section headings use h2 ✓; context toggle has aria-pressed ✓; apocrypha-reader chapter buttons have aria-label + aria-current ✓ (AUD-7 resolved); ol-companion token buttons have aria-expanded ✓ (AUD-8 resolved). New finding: verse-study.js never updates document.title or marks #vs-header-ref as a heading — screen readers see a static "Verse Study" tab and no h1 — AUD-11.*

---

*(AUD-11 complete — see working/todo-archive.md 2026-06-06)*

---

*Audit pass 2026-06-06 (Cycle 4). Read: `assets/js/lib-reader.js`, `assets/js/lib-browser.js`, `assets/js/library.js` (dictionary page), `assets/js/lib-progress.js`. lib-progress.js is read-only (just links) — clean ✓. lib-reader find bar, pager prev/next, section select all have `aria-label` ✓. lib-browser toggle buttons update `aria-label` on state change ✓. Finding: five interactive control groups across three files use visual-only state (CSS classes) with no matching ARIA state attributes — screen readers cannot announce selected/active/on state.*

---

*(AUD-13 complete — see working/todo-archive.md 2026-06-06)*

---

## Feature Completeness Audit — Dimension 5, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (AUD-1) found the NT Daily Matthew chapter-count bug. This pass checked: ISBE data (9,380 entries + 66-book verse-index — complete), OL Companion wiring (`window.BibleUI.initOLSection` → verse-study.js — correct), book introductions (66/66), Nave's topical verse-index (66/66), topics-index.json (15 entries — all pages resolve), word cloud scopes (unchanged), translation workshop (page exists), apocrypha reader. Found one HIGH bug in apocrypha-reader.js `_getOrderedBooks()`.*

---

*(AUD-6 complete — see working/todo-archive.md 2026-06-05)*

---

## Feature Completeness Audit — Dimension 5, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Confirmed: reading plans (8/8 IDs → files), MKT commentary data (fully generated), echoes data (fully generated), apocrypha reader nav wiring, OL Companion wiring. Found two data-ready features with no UI access path.*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

## Feature Completeness Audit — Dimension 5, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Checked: dictionary page OMNI_SOURCES registration (Easton's, Smith's, ISBE, Hitchcock, Nave's, Torrey's — all 6 registered in OMNI_SOURCES ✓); `?src=...&entry=...` URL routing (`_tryShowUrlEntry` at line 782 — Easton's works because it loads first; secondary sources load async in a separate forEach at line 812 with no re-try of `_tryShowUrlEntry` after they resolve). Found one HIGH bug affecting all verse-study cross-links to non-Easton's sources.*

---

*(AUD-12 complete — see working/todo-archive.md 2026-06-06)*

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

*(DATA-4 complete — see working/todo-archive.md 2026-06-06)*

---

## Data Path Integrity Audit — Dimension 4, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Cross-checked all translation data paths (notes + 3 MKT draft tiers × 66 books = 264 files — all present). All 8 registered commentary sources have complete 66-book coverage. Topics.json href links all resolve. Found one new gap: WEB-CE has the same Daniel-additions data gap as DR (DATA-4) but with a slightly different set of missing books.*

---

*(DATA-5 complete — see working/todo-archive.md 2026-06-06)*

---

*(DATA-6 complete — script written; see working/todo-archive.md 2026-06-06. Run `python3 scripts/fix-apocrypha-strongs.py` to apply the data fix.)*

---

*(DATA-7 complete — script written; see working/todo-archive.md 2026-06-06. Run `python3 scripts/fix-brenton-spaces.py` to apply the data fix.)*

---

*(DATA-8 complete — see working/todo-archive.md 2026-06-06)*

---

*(DATA-9 complete — see working/todo-archive.md 2026-06-06)*

---

## Data Path Integrity Audit — Dimension 4, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Checked all verse-index paths used by the dictionary/topical panel: Easton's (`data/dictionary/verse-index/`) 66/66 ✓; Nave's (`data/topical/verse-index/`) 66/66 ✓; ISBE (`data/isbe/verse-index/`) 66/66 ✓; Torrey (`data/torrey/verse-index/`) 64/66 — missing Isaiah + Jude (correct: `torrey.json` has zero citations for those books); library (`data/library/verse-index/`) 47/66 (correct: only books with library citations have index files). AUD-9 (echoes) and AUD-10 (MKT commentary) are both resolved in code. One gap found: Smith's dictionary verse-index missing `philippians.json`.*

---

*(DATA-10 complete — see working/todo-archive.md 2026-06-06)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (CSS-1–6) addressed word.css height clipping, hamburger/discipline/reader touch targets, study-nav font-size, and reader keyboard hint visibility. This pass examined lib-browser.css, verse-study.css, memorize.css, maps.css, and timelapse.css. Two new issues found.*

---

*(CSS-11 complete — see working/todo-archive.md 2026-06-05)*

---

*(CSS-12 complete — see working/todo-archive.md 2026-06-05)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Prior cycles addressed the core reader, discipline, lib-browser, verse-study, maps, and timelapse pages. This pass audited `apocrypha.css` and `ol-companion.css` — both added after the previous mobile passes.*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Prior cycles covered word.css, core reader/discipline controls, lib-browser.css, verse-study.css, maps/timelapse/memorize, apocrypha.css, ol-companion.css. This pass audited `lib-reader.css` and `lib-progress.css` — the two remaining CSS files not covered in prior passes. lib-progress.css is clean (no interactive controls, mobile query at line 162). lib-reader.css has a touch-target gap: `.lr-toc-list a` was correctly fixed to 44px at 640px (lines 201–203), but three other interactive control groups were not. Finding below.*

---

*(CSS-19 complete — see working/todo-archive.md 2026-06-06)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Prior cycles covered word.css, reader/discipline/study-nav controls, lib-browser.css, verse-study.css, maps/timelapse/memorize, apocrypha.css, ol-companion.css, lib-reader.css, lib-progress.css. This pass checked: `dictionary.css` (634 lines, 11 media queries), `daily.css` (716 lines, 6 media queries), `book-study.css` (987 lines — read-only layout/display file, one 640px responsive breakpoint, no interactive controls), `topic-guide.css`, `topic-shell.css`, `study-guide.css`, `topical.css`, `timeline.css`, `wordcloud.css`, `devotionals.css`. book-study.css/topic-guide.css/study-guide.css/topical.css/timeline.css/wordcloud.css/devotionals.css: no interactive button/control groups; mobile breakpoints handle layout reflows — clean ✓. dictionary.css and daily.css: both have interactive control groups with sub-22px touch targets that lack corrective mobile breakpoints.*

---

*(CSS-21 complete — see working/todo-archive.md 2026-06-06)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Prior cycles covered word.css, reader/discipline/study-nav, lib-browser.css, verse-study.css, maps/timelapse/memorize, apocrypha.css, ol-companion.css, lib-reader.css, lib-progress.css, dictionary.css, daily.css, book-study.css, topic-guide.css, topic-shell.css, study-guide.css, topical.css, timeline.css, wordcloud.css, devotionals.css. This pass checked the four remaining CSS files: `bible-ui.css` (3840 lines, two mobile breakpoints at 480px and 767px), `discipline.css` (590 lines, one breakpoint at 500px), `library.css` (one breakpoint at 480px for Q&A grid), `workshop.css` (one breakpoint at 900px for source grid). library.css is mostly typographic display with no button controls — clean ✓. workshop.css is a dev-tool page only accessed from desktop — single grid layout query, no touch-target requirement ✓. discipline.css mobile breakpoint only adjusts .disc-tab padding and .plan-card__top flex direction; journal and worship entry edit/delete buttons remain sub-20px. bible-ui.css has a thorough 767px block covering modal close, action buttons, tabs, and xref chips — but the prev/next verse navigation buttons are explicitly made narrower on mobile than desktop.*

---

*(CSS-23 complete — see working/todo-archive.md 2026-06-06)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked `maps.css` (mobile breakpoint `@media (max-width: 700px)`): `.maps-nav-btn` (map selector, main nav) — `padding: .2rem .5rem; font-size: .74rem` → ~21px tall on mobile, too small but used in a horizontally-scrollable strip with `flex-shrink: 0` so fixing to 44px could cause layout overflow; LOW priority. `.maps-tab` (Overview/Sites/Refs panel tabs) — `padding: .3rem .4rem; font-size: .70rem` → ~23px tall on mobile; these are the primary panel navigation controls on mobile and need 44px. `.maps-city-nav-btn` (Prev/Next City in detail panel) — `padding: .1rem .5rem; font-size: .78rem` → ~19px tall on mobile; smallest interactive control, used when exploring city detail. Both `.maps-tab` and `.maps-city-nav-btn` are sub-44px with no existing mobile override — CSS-26.*

---

*(CSS-26 complete — see working/todo-archive.md 2026-06-06)*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (UX-1–5) addressed search.js, verse-study.js interlinear, discipline plans, library secondary sources, and history iframe tabs. This pass found two remaining missing `.catch()` patterns in verse-study.js.*

---

*(UX-6 complete — see working/todo-archive.md 2026-06-05)*

---

*(UX-7 complete — see working/todo-archive.md 2026-06-05)*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Previous cycles covered the core reader, search, verse-study, and discipline pages. This pass targeted two newer modules — lib-browser.js and apocrypha-reader.js — that were added after the prior audits.*

---


*(item complete — see working/todo-archive.md 2026-06-05)*


*(item complete — see working/todo-archive.md 2026-06-05)*

## Code Comment Audit — Dimension 1, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (CODE-1–8) addressed the most obvious gaps. This pass found two areas still missing required structured comments: three complex algorithms in wire.js added after the first-pass fixes, and the window.BibleUI cross-module coupling in app.js.*

---

*(CODE-9 complete — see working/todo-archive.md 2026-06-05)*

---

*(CODE-10 complete — see working/todo-archive.md 2026-06-05)*

---

## Code Comment Audit — Dimension 1, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Prior cycles (CODE-1–10) addressed the original JS files and wire.js/app.js additions. This pass found two files added since those fixes — ol-companion.js and lib-browser.js — that have zero INTENT/CHANGE?/VERIFY coverage despite containing complex state logic.*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

*(item complete — see working/todo-archive.md 2026-06-05)*

---

## Code Comment Audit — Dimension 1, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Prior cycles covered core.js, storage.js, reader.js, wire.js, app.js, ol-companion.js, lib-browser.js plus fixes CODE-1–12. This pass checked `verse-study.js` (1,238 lines, 11 INTENT/CHANGE?/VERIFY occurrences) and `interlinear.js` (472 lines, 6 occurrences). interlinear.js gaps are minor (private-state short setters). verse-study.js has two exported functions and one window.BibleUI coupling without required comments.*

---

*(CODE-13 complete — see working/todo-archive.md 2026-06-06)*

---

## Code Comment Audit — Dimension 1, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Prior cycles covered core.js, storage.js, reader.js, wire.js, app.js, ol-companion.js, lib-browser.js, verse-study.js, interlinear.js (CODE-1–13). This pass checked `lib-reader.js` (740 lines, 0 INTENT/CHANGE?/VERIFY), `tracker.js` (173 lines, 4 comments), and `modal.js` (1,496 lines, 7 comments). lib-reader.js has zero coverage despite an exported entry-point and four localStorage functions. modal.js has solid coverage on register* functions and buildModalDOM but is missing INTENT/CHANGE?/VERIFY on its 5 major render/open exported functions.*

---

*(CODE-14 complete — see working/todo-archive.md 2026-06-06)*

---

*(CODE-15 complete — see working/todo-archive.md 2026-06-06)*

---

## Code Comment Audit — Dimension 1, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Prior cycles covered core.js, storage.js, reader.js, wire.js, app.js, ol-companion.js, lib-browser.js, verse-study.js, interlinear.js, lib-reader.js, tracker.js, modal.js (CODE-1–15). This pass checked `parallels.js` (346 lines, 0 INTENT/CHANGE?/VERIFY), `daily.js` (1,323 lines, 4 comments), and `terms.js` (393 lines, 3 comments — existing coverage on `runAutoTagTerms` only). Two significant gaps found.*

---

*(CODE-16 complete — see working/todo-archive.md 2026-06-06)*

---

*(CODE-17 complete — see working/todo-archive.md 2026-06-06)*

---

## Code Comment Audit — Dimension 1, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Prior cycles covered core.js, storage.js, reader.js, main.js, word.js, search.js, wordcloud.js, wire.js, app.js, ol-companion.js, lib-browser.js, verse-study.js, interlinear.js, lib-reader.js, tracker.js, modal.js, parallels.js, daily.js, terms.js (CODE-1–17). Remaining unchecked files by INTENT count: maps.js (2448 lines, 1), timelapse-map.js (836 lines, 2 on _animLoop/_figurePos only), timeline.js (707 lines, 2 on internal helpers), pwa.js (155 lines, 3 — adequate), store.js (281 lines, 0), sg-progress.js (99 lines, 0), lib-progress.js (147 lines, 0), apocrypha-reader.js (613 lines, 10 — adequate). Two significant gaps found.*

---

*(CODE-18 complete — see working/todo-archive.md 2026-06-06)*

---

*(CODE-19 complete — see working/todo-archive.md 2026-06-06)*

---

## Code Comment Audit — Dimension 1, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Prior cycles covered all major JS modules (CODE-1–19). Remaining unchecked: `sg-progress.js` (99 lines, 0 INTENT — 2 exported entry points + 1 non-obvious internal), `lib-progress.js` (147 lines, 0 INTENT — 1 exported entry + 1 complex renderer), `timeline.js` (707 lines, 2 on internal helpers — needs entry-point coverage). Two files with zero coverage found: sg-progress.js + lib-progress.js — CODE-20.*

---

*(CODE-20 complete — see working/todo-archive.md 2026-06-06)*

---

## Code Comment Audit — Dimension 1, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Prior cycles covered all JS modules (CODE-1–20). Final unchecked file with exported entry points: `timeline.js` — `initTimelinePage()` and `initChurchTimelinePage()` both exported from line 691/700 with zero INTENT; they use `storageKey: 'bsw_tl'/'bsw_chtl'` that map to `sessionStorage` keys (bsw_tl_era, bsw_tl_event, etc.) with TLU-B URL-param fallback logic. Non-obvious: two separate timelines share the same _makeController factory but must use distinct storageKey namespaces or they'll overwrite each other's sessionStorage — CODE-21.*

---

*(CODE-21 complete — see working/todo-archive.md 2026-06-06)*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 4

*Audit pass 2026-06-06 (Cycle 4). Prior cycles covered reader, search, verse-study, discipline, lib-browser, apocrypha-reader. This pass targeted modules not yet covered: `ol-companion.js`, `word.js`, `lib-reader.js`, `lib-progress.js`, and the verse-study section loaders (confessions, church fathers, dictionary, OL companion). All modules have solid error handling: `_loadNotes`/`_loadTier` both have try/catch with null-cache on failure (ol-companion.js lines 38–44, 58–63); missing `?s=` shows user-visible error at line 47 and `.catch` at lines 192–195 (word.js); error messages at lines 59/63/97–99 with "Return to Library" link (lib-reader.js); `.catch` renders empty log at line 48 and "No completed works yet" state at line 120 (lib-progress.js); all four new verse-study sections (confessions/church-fathers/dictionary/OL companion) have `.catch` that removes the section and calls `vsRebuildNav` (verse-study.js lines 887/900/911/917). No new items this cycle.*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked remaining uncovered modules: `daily.js` (1,323 lines), `modal.js` (1,496 lines), `library.js` (dictionary page), `timeline.js`, `wordcloud.js`, `maps.js`, `timelapse-map.js`, `sg-progress.js`, `store.js`, `terms.js`. daily.js: every fetch has `.catch()` with user-visible message ✓. modal.js: cross-refs and commentary both show user messages on failure ✓; empty catches are for clipboard API and optional verse-text enrichment (silent is correct) ✓. library.js: Easton's main load failure → "Failed to load dictionary" ✓; entry fetch → "Could not load entry." ✓. timeline.js: "Unable to load timeline data." ✓. wordcloud.js: "Unable to load word frequency data." ✓. maps.js: all data inline — no fetch ✓. One finding: timelapse-map.js catch is console.error only, no user-visible error.*

---

*(UX-10 complete — see working/todo-archive.md 2026-06-06)*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Prior cycles covered reader.js, search.js, word.js, verse-study.js, library.js, lib-browser.js, apocrypha-reader.js, ol-companion.js, lib-reader.js, lib-progress.js, daily.js, modal.js, timeline.js, wordcloud.js, maps.js, timelapse-map.js, terms.js. This pass checked `parallels.js` (good: "Could not load." + "Not available." messages, silent empty `.catch()` on optional panels ✓), `discipline-strip.js` (no fetches — reads synchronously from tracker.js, renders gray dots as empty state ✓), `tracker.js` (pure localStorage module, no fetches ✓). One gap: `places.js` `loadPlaces()` has no `.catch()` — permanent rejected-promise cache causes repeated unhandled rejections on every reader page turn.*

---

*(UX-11 complete — see working/todo-archive.md 2026-06-06)*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). All JS files confirmed: pwa.js (no fetches ✓), tooltip.js (no fetches ✓), wire.js (no fetches ✓), interlinear.js (all 3 .catch() handled ✓), app.js (no fetches ✓), sg-progress.js (pure localStorage ✓). Redirect stubs: plans/, devotionals/, reflections/, worship/ all redirect to discipline/ — no own content. church-history/index.html and apocrypha/index.html — no page-level fetch logic. notes/index.html: three contextual empty states (no annotations, search empty, filtered empty) ✓. bookmarks/index.html: bsw-empty-state div with CTA to Reader ✓. One gap found: compare/index.html init .catch() is console.error-only.*

---

*(UX-12 complete — see working/todo-archive.md 2026-06-06)*

---

## Reader Interlinear — Popover Bugs

Four bugs in the interlinear tile popover (`assets/js/interlinear.js` — `_riShowPopover`, `renderReaderInterlinearRow`).

---

*(RI-A complete — see working/todo-archive.md 2026-06-06)*

---

*(RI-B complete — see working/todo-archive.md 2026-06-06)*

---

*(RI-C complete — see working/todo-archive.md 2026-06-06)*

---

*(RI-D complete — see working/todo-archive.md 2026-06-06)*

---

## Translation Workshop — Lexical Evidence Expansion

**Goal:** Transform the Workshop's "Attested Range" from an asserted definition into a demonstrated one. Right now `semantic_range` is a copy of the Strong's `def` field — the same single-source claim dressed up differently. The expansion adds three layers of evidence: more lexical sources (independent scholarly witnesses to the range), biblical attestation (the word in its actual textual contexts across the corpus), and extrabiblical attestation (papyri, Josephus, Philo, classical Greek — showing the word in the wild outside the Bible).

**Current sources:**
- Greek: Dodson (CC0 gloss/def) + Thayer 1889 (short/long def) — both are Strong's-adjacent derivatives
- Hebrew: Strong's Hebrew (gloss/def) + BDB 1906 (short/long def)
- `expansion` field: in schema, empty in every entry

**Evaluation:** The two-source display looks great visually. The semantic range framing is correct in theory. What's missing is *evidence* — the dossier tells you what scholars think the range is, but doesn't show you the word earning that range through actual use. A translator needs to see the word behaving differently in John vs. Paul, in the papyri vs. the LXX, in an oath vs. a prayer.

---

*(WS-A complete — see working/todo-archive.md 2026-06-05)*

---

*(WS-B complete — see working/todo-archive.md 2026-06-05)*

---

*(WS-C complete — see working/todo-archive.md 2026-06-05)*

---

*(WS-D complete — see working/todo-archive.md 2026-06-05)*

---

*(WS-E complete — see working/todo-archive.md 2026-06-05)*

---

*(WS-F complete — see working/todo-archive.md 2026-06-05)*


### WS-G · Curated semantic-range descriptions for top-100 disputed/high-use terms *(LOW — agent task)*

**Why:** The current `semantic_range` field is generated from the Strong's `def` field — it's the same text from the same source, just relabeled. For the 100 most significant terms (the Phase 1 + Phase 5 sets), the range description should be a curated synthesis: what do all the sources agree on, where do they diverge, and what does the corpus evidence show? This is an agent-writable task — one entry at a time, the agent reads all source cards + attested uses and writes a 2-3 sentence curated range description.

**Tasks:**
- [ ] Design the agent prompt for curated range writing (reads: dodson + thayer + abbott-smith + attested uses → writes: `semantic_range` as 2-3 sentence synthesis)
- [ ] Agent pass: curate `semantic_range` for all Phase 1 Greek entries (200 entries)
- [ ] Agent pass: curate `semantic_range` for all Phase 2 Hebrew entries (200 entries)
- [ ] Agent pass: curate `semantic_range` for Phase 5 contested terms (17 entries — highest priority)
- [ ] `apply-decisions.py` — extend to support `semantic_range` field updates (currently only handles status/tiers/log)

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

### ~~SW-A · Rebrand and passage-centric entry point~~ *(done 2026-06-06)*

*(archived — see working/todo-archive.md)*

---

### SW-B · Grammar significance system *(HIGH — highest scholarly value, most unique)*

**Why this matters most:** Every interlinear shows "VERB aorist active indicative 3rd singular" — but almost none explain what that means for interpretation. The Greek perfect tense signals completed-action-with-ongoing-results (γέγραπται = "it stands written," still authoritative). The Hebrew Piel intensifies the Qal action. The genitive case has twelve semantic functions that completely change meaning. Lay readers see the label and have no path forward.

**New data files to generate (agent task):**

- `data/grammar/greek-morphology-significance.json` — ~60 entries, keyed by morphological category:
  - All 7 tenses with significance + plain_english + interpretive_examples + common_misreading
  - 3 voices; 5 moods (imperative/subjunctive/optative/infinitive/participle) with force
  - 5 cases with their semantic functions (especially genitive's 12 uses: possessive, subjective, objective, partitive, appositive, genitive absolute, etc.)
- `data/grammar/hebrew-morphology-significance.json` — ~40 entries:
  - 7 binyanim (Qal/Niphal/Piel/Pual/Hiphil/Hophal/Hithpael) with semantic force
  - Perfect/imperfect aspect distinction (not tense — action-type); prophetic perfect explanation
  - Waw-consecutive significance; participle as verbal adjective; infinitive construct vs. absolute
- `data/grammar/greek-particles.json` — ~45 discourse particles with Strong's codes, discourse function, plain-English explanation, color class, and illustrative example:
  - G1063 γάρ (ground/reason — orange), G3767 οὖν (inference — green), G0235 ἀλλά (strong contrast — red), G1161 δέ (continuation — blue), G5620 ὥστε (result), G2443 ἵνα (purpose), G3754 ὅτι (content/reason), G1487 εἰ (conditional), G3361 μή vs. G3756 οὐ (prohibition types)
- `data/grammar/hebrew-particles.json` — ~30 entries: כִּי (causal/concessive/object marker), לָכֵן (therefore), הִנֵּה (immediacy marker), אַל vs. לֹא (prohibitions), waw-consecutive function

**UI tasks:**
- [ ] Grammar Significance section in dossier: parsed form in plain English + significance card + plain_english callout box; ⓘ next to every grammar term label opens the full card inline
- [ ] Discourse Markers toggle above interlinear tiles: when ON, particles detected by Strong's code get a colored border/badge on their tile; hover shows the particle's plain explanation
- [ ] Add `data/grammar/` paths to sw.js SHELL_URLS

**Verify:** Study Romans 8:1 in passage view — οὖν tile gets an orange/green "inference" badge. Hover → "Therefore — draws a logical conclusion from what came before. Romans 8:1 is the conclusion of a 7-chapter argument." Click tile → dossier Grammar section shows the ⓘ inference explanation card.

---

### SW-C · Grammar debates panel *(HIGH — unique to this tool)*

**Why:** Some of the most significant theological questions in the NT hinge entirely on Greek grammatical constructions — and a lay reader has no way to know the debate exists. πίστις Χριστοῦ has occupied NT scholars for 40 years and changes whether justification is primarily about our faith-act or Christ's covenant obedience. This panel surfaces ~40 such cases.

**New data file:** `data/grammar/grammar-debates.json` — ~40 entries:
```
Schema per entry: { id, label, strongs_keys, trigger_passages, construction,
  position_a: { label, rendering, argument, proponents },
  position_b: { label, rendering, argument, proponents },
  why_it_matters, scholarly_status }
```

Initial 40 entries to generate (agent task):
- πίστις Χριστοῦ: objective vs. subjective genitive (Rom 3:22, Gal 2:16, Phil 3:9)
- μονογενής: only-begotten vs. unique/one-of-a-kind (etymology debate)
- ἐν ἀρχῇ John 1:1: articular vs. anarticular
- ὁ νόμος in Paul: Mosaic Torah vs. any law principle
- αἰώνιος: belonging-to-the-age vs. everlasting duration
- ἱλαστήριον Rom 3:25: propitiation vs. expiation vs. mercy seat
- Granville Sharp Rule: Titus 2:13 ("our great God and Savior Jesus Christ")
- עַלְמָה Isa 7:14: virgin vs. young woman of marriageable age
- בְּרֵאשִׁית Gen 1:1: absolute vs. construct state
- רוּחַ אֱלֹהִים Gen 1:2: Spirit of God vs. mighty wind

**Tasks:**
- [ ] Agent task: generate `data/grammar/grammar-debates.json` (40 entries)
- [ ] In dossier: when clicked word's Strong's code + current passage matches a `trigger_passages` entry, add **Contested Interpretation** card: construction label, two positions with named proponents, why-it-matters section, scholarly-status badge
- [ ] CSS: `.sw-debate-card` (two-column positions, proponent chips, why-it-matters callout)

**Verify:** Study Gal 2:16 → click πίστεως → Contested Interpretation card shows both positions (faith IN Christ / faithfulness OF Christ) with named proponents and the theological consequence of each reading.

---

### SW-D · Literary analysis panel *(HIGH — the layer most tools miss entirely)*

**Why:** The Bible is literature, and its literary structure is part of its meaning. Psalm parallelism is not decorative — the second line always interprets the first. Paul's logical argument (thesis → ground → inference → application) is visible in the Greek particles and invisible in English. A narrative chiasm puts its center as the theological climax. Without literary awareness, readers flatten the text.

**New data files (all agent tasks):**

- `data/literary/genre.json` — 66 books: primary genre, sub-genres, literary note, structure note
- `data/literary/structures.json` — ~80 key pericopes with chiasm/structure data and center notes (John 1 prologue, Phil 2 hymn, 1 Cor 13, Sermon on the Mount, Philemon chiasm, Amos 5 chiasm, Ruth structure, etc.)
- `data/literary/devices-glossary.json` — 30 literary devices with plain-English definitions and biblical examples (chiasm, inclusio, synonymous/antithetical/synthetic/climactic parallelism, merism, hendiadys, litotes, hyperbole, irony, paronomasia, acrostic, anaphora, refrain)
- `data/literary/parallelism.json` — Psalms + Proverbs verse-by-verse parallelism type annotations

**Tasks:**
- [ ] `scripts/detect-parallelism.py` — heuristic: flag adjacent Psalms/Proverbs verses sharing 3+ content lemmas as potential synonymous parallelism; output `data/literary/parallelism.json`
- [ ] Literary Structure tab in passage view: genre badge + one-line note; if structural data exists for the pericope, render the chiasm/outline as a CSS-indented diagram (A B C → C' B' A' with matching colors per pair); literary device badges (clickable → device glossary explanation)
- [ ] Literary Context section in dossier (Student+ depth): genre of current book + literary structure annotation if present

**Verify:** Study John 1:1–18 → Literary Structure tab shows the chiasm with matching colors on paired elements, center highlighted, note about the center's theological significance. Psalm 23 → parallelism badges on verse pairs; clicking badge → plain-English explanation of synonymous parallelism.

---

### SW-E · Idiom database *(HIGH — most transformative for lay readers)*

**Why:** Biblical idioms are pervasive and almost never flagged. "Son of X" means "characterized by X." "Heart" in Hebrew means intellect and will, not emotions. "Bowels of mercy" means deep compassion (Paul means intestines). "Gird your loins" means prepare for action. "To know" a person means intimate relationship. "Hard-necked" means stubborn. Without this layer, lay readers either miss the idiom or misread it literally.

**New data files:**
- `data/idioms.json` — ~500 entries:
  ```
  Schema: { id, phrase, original_he, original_gr, strongs_trigger_he[], strongs_trigger_gr[],
    literal, cultural_meaning, significance, key_passages[], category, plain_english }
  ```
- `data/idioms-index.json` — inverted index: Strong's code → array of idiom IDs

**Categories across ~500 entries (agent task — draws from Clarke/Barnes/ISBE already on site):**
- Kinship metaphors: son/daughter of X, firstborn, only-begotten, father of X
- Body/anatomy: heart (= intellect+will), bowels/kidneys (= deep emotions), face (= honor), hand (= power), arm (= strength), neck (= submission vs. stubbornness), bosom (= intimate fellowship)
- Knowledge/perception: know (= intimate relationship), see (= understand), hear (= obey), remember (= act covenantally)
- Spatial metaphors: right hand (= highest honor), under the feet (= subjugated), in the bosom (= closest fellowship)
- Honor/shame: face/countenance, shame, nakedness, lift up the face, hide the face
- Agricultural: threshing floor (= judgment), gleaning, vine/vineyard (= Israel), harvest, winnowing
- Clothing: gird (= take on a role), naked (= vulnerable), garment of praise/righteousness
- Death/burial: sleep (= death), gathered to his people, Sheol/Hades
- Warfare: draw the sword, deliver into the hand of
- Numerics as idioms: 40 (testing), 7 (completeness), 70 (fullness), 12 (covenant completeness)
- Commonly misread terms: peace (= shalom = wholeness), salvation (= rescue/wholeness), glory (= kabod = weight), grace (= gift with relational obligation in honor culture), righteousness (= covenant faithfulness)

**Tasks:**
- [ ] Agent task: generate `data/idioms.json` (~500 entries)
- [ ] `scripts/seed-idioms.py` — writes JSON and builds `data/idioms-index.json`
- [ ] Passage view: detect idioms by matching tile Strong's codes against idioms-index.json; show collapsible **Idioms in This Passage** panel (plain_english + cultural_meaning + key_passages per idiom)
- [ ] Dossier: **Idiom Alert** section if the clicked word has an idiom trigger
- [ ] CSS: `.sw-idiom-badge` on triggering tiles, `.sw-idiom-panel`, `.sw-idiom-alert`

**Verify:** Study John 17:12 → G5207 (υἱός) tile gets an idiom badge. Idioms panel shows "son of X" entry: "When υἱός appears with a genitive noun, it usually means 'characterized by X' — 'son of destruction' = one destined for/characterized by destruction."

---

### SW-F · Cultural background system *(HIGH)*

**Why:** The Bible assumes a cultural world the reader no longer inhabits. Honor-shame dynamics drive more narrative tension than Western readers notice. Patron-client relationships explain why "giving thanks publicly" was a social obligation. Jewish purity categories make healing narratives legible as community restoration. ANE treaty structure is the template for the covenant system. Without this layer the text is opaque in ways the reader doesn't know to ask about.

**New data files (all agent tasks):**

- `data/cultural/frameworks.json` — 12 cultural framework primers (5 key concepts + key passages + reading tip each):
  1. Honor and Shame — challenge-riposte, face as honor, sitting and standing, shame as social loss
  2. Patron-Client Relationships — reciprocal obligation, public thanks as social duty, benefaction logic
  3. Jewish Purity and Holiness System — clean/unclean categories, healing = community restoration
  4. Mosaic Covenant Structure — ANE suzerainty-vassal treaty form → Deuteronomy's architecture
  5. Second Temple Judaism — Pharisees/Sadducees/Essenes/Zealots, messianic expectations, Torah debates
  6. Roman Imperial Context — "Son of God" / "Lord" / "gospel" as imperial titles; cross as political counter-claim
  7. Household Codes and Structure — oikos as economic unit, paterfamilias, house church context
  8. Ancient Near East Cosmology — divine council, cosmic geography, what biblical authors assumed about the cosmos
  9. Prophetic Speech Forms — oracle of doom, woe oracle, covenant lawsuit (rib), comfort oracle
  10. Wisdom Tradition — retribution principle and its limits (Job, Ecclesiastes), personified Wisdom (Prov 8)
  11. Apocalyptic Literature Conventions — why Revelation uses symbols, throne-room scenes, numeric symbolism
  12. Kinship and Tribal Social Structure — clan identity, levirate marriage, kinsman-redeemer, the goel

- `data/cultural/book-context.json` — 66 entries: setting, audience, date range, primary_frameworks[], key_background (what first readers knew that modern readers don't)
- `data/cultural/symbols.json` — number symbolism (3/4/7/10/12/40/70/666/1000), color symbolism (white/red/blue/purple/black), directional symbolism (east/west/north, Jerusalem as "up"), cosmological symbols (sea = chaos/nations, mountain = divine meeting place, garden = sacred space)

**Tasks:**
- [ ] Agent task: generate all three cultural data files
- [ ] Cultural Context tab in passage view: auto-surface book-context card for current book; surface relevant framework primers as collapsible banners; symbols panel if any tile matches symbols.json
- [ ] CSS: `.sw-cultural-panel`, `.sw-framework-primer`, `.sw-symbol-card`

**Verify:** Study Mark 5:1–20 → Cultural Context tab surfaces: honor-shame + jewish-purity frameworks. Expanding jewish-purity → "The man living among tombs is ritually impure (corpse contamination, Num 19) — excluded from community worship. Jesus' healing is simultaneously physical restoration, ritual cleansing, and social reintegration."

---

### SW-G · Proficiency / depth model *(MEDIUM — wires scaffold from SW-A)*

**Three levels — same data, different amounts visible:**

| Level | Visible sections | Target user |
|-------|-----------------|-------------|
| **Reader** | Semantic range summary (2 sentences), 3 verse samples, idiom alert, simple translation note, book-context card | New to Bible study |
| **Student** | All lexical sources, full verse samples, grammar significance, literary structure tab, all cultural frameworks, LXX bridge, book distribution heat map | Regular Bible student |
| **Scholar** | All of the above + grammar debates, cognate family, semantic field, author frequency, M&M papyri, OT-in-NT panel, Second Temple context | Sermon prep, seminary, deep exegesis |

**Tasks:**
- [ ] Tag every dossier section with `data-depth-min="1|2|3"` (1=Reader, 2=Student, 3=Scholar)
- [ ] `_wsApplyDepth(level)`: toggles `sw-depth-hidden` class on all `[data-depth-min]` elements where min > level; saves to `localStorage['bsw_ws_depth']`
- [ ] First-load one-time prompt: "Choose your study depth" with one-sentence description of each level
- [ ] At depth boundaries: "Unlock Student / Scholar level →" prompt that bumps depth on click

**Verify:** Reader depth → only semantic range, 3 samples, idiom alert visible. Scholar → all sections. Reload → depth preference restored.

---

### SW-H · Cognate word family display *(MEDIUM)*

**Why:** Seeing a Hebrew word's cognate family transforms interpretation. כָּבוֹד (glory/honor), כָּבֵד (heavy/the liver), כָּבַד (to honor/be heavy) all share כ-ב-ד. "The glory of the LORD" is not merely metaphorical — the root means *weight.* Greek: ἀγάπη / ἀγαπάω / ἀγαπητός — the family shows that "beloved" is literally "one who has been agapaoed."

**Tasks:**
- [ ] `scripts/build-cognate-families.py`:
  - Hebrew: group glossary entries by 3-consonant root; output `data/grammar/cognate-families-hebrew.json`
  - Greek: parse Abbott-Smith/Thayer derivation notes for parent-child relationships; output `data/grammar/cognate-families-greek.json`
  - Schema: `{ root_he, root_meaning, members: [{ code, lemma, gloss }] }`
- [ ] Word Family section in dossier (Student+ depth): root with core meaning callout + all family members as clickable chips (click → navigate to that entry's dossier)

**Verify:** Open H3519 (כָּבוֹד) → Word Family shows root כ-ב-ד "weight/heaviness" + chips for כָּבֵד ("heavy"), כָּבַד ("to honor/be heavy"). Click a chip → dossier navigates to that entry.

---

### SW-I · Semantic field clustering *(MEDIUM — computational)*

**Why:** Words do not travel alone. λόγος clusters with λαλέω, ἀκούω, γράφω in the corpus — revealing it functions primarily as a speech-act concept, not an abstract philosophical one. Seeing the semantic neighborhood shows how the word functioned conceptually, not just definitionally.

**Tasks:**
- [ ] `scripts/build-semantic-fields.py`:
  - For each Strong's code, collect all verses where it appears; for each verse, collect all other codes present
  - Compute PMI (pointwise mutual information) scores to find over-representation vs. chance
  - Output top 10 per entry: `data/grammar/semantic-fields-greek.json` + `data/grammar/semantic-fields-hebrew.json`
- [ ] Semantic Neighborhood section in dossier (Scholar depth): top 8 co-occurring words as clickable chips with gloss; tooltip explaining what co-occurrence means

**Verify:** Study G3056 (λόγος) → neighborhood shows λέγω, λαλέω, ἀκούω prominently. Study H2617 (חֶסֶד hesed) → neighborhood shows אֱמֶת (faithfulness), טוֹב (good), covenant-related terms.

---

### SW-J · Author / corpus frequency comparison *(MEDIUM)*

**Why:** Paul and John use the same word differently. ἀγάπη appears at ~60% higher rate in John's corpus than Paul's — revealing it is more theologically central to John's idiom. Noticing authorial characteristic vocabulary (John's κόσμος, Paul's δικαιοσύνη, Luke's σωτήρ) reveals theological emphasis and authorial voice.

**Tasks:**
- [ ] `scripts/build-author-frequencies.py`: define author groups (Paul: Rom–Philemon; John: Jn+1-3Jn+Rev; Luke: Lk+Acts; etc.); compute per-author normalized rates (occurrences per 1,000 words); add `author_freq` field to each glossary entry
- [ ] In dossier: author-grouped heat map view (author initials as row headers; intensity by normalized rate not raw count; highest-rate author gets a badge); toggle "By Author" / "By Book"

**Verify:** Open G0026 (ἀγάπη) → John has highest-rate badge. Open a word characteristic of Paul → Paul gets the badge.

---

### SW-K · OT-in-NT comparison panel *(MEDIUM)*

**Why:** Every NT quotation of the OT carries three text traditions: Masoretic Text (Hebrew), Septuagint (what NT authors usually quoted), and the NT author's form. Differences are often theologically significant and completely invisible to English readers. Matthew's παρθένος for עַלְמָה, Paul's use of Habakkuk 2:4 — these are hermeneutical decisions embedded in the text.

**New data file:** `data/ot-in-nt/quotations.json` — ~300 explicit quotations:
```
Schema: { id, nt_ref, ot_ref, quotation_marker, nt_greek, lxx_greek, mt_hebrew,
  key_differences: [{ word, note }], fulfillment_type, interpretation_note }
```

**Tasks:**
- [ ] Agent task: generate `data/ot-in-nt/quotations.json` (~300 entries using UBS apparatus, NET Bible notes, existing echoes data)
- [ ] In dossier for any NT word in a quoted passage: **OT Source** panel showing MT | LXX | NT in three columns, differences highlighted gold, interpretation note
- [ ] Also from OT side: "Quoted in the NT as..." link with comparison data
- [ ] CSS: `.sw-ot-in-nt`, `.sw-triple-compare`, `.sw-diff-highlight`

**Verify:** Study Matt 1:23 → click παρθένος → OT Source panel shows Isa 7:14 in three columns, עַלְמָה/παρθένος difference highlighted, interpretive note explaining LXX translation choice and Matthew's use of it.

---

### SW-L · Second Temple context snippets *(MEDIUM — targeted agent curation)*

**Why:** The NT authors lived inside a rich tradition of Jewish interpretation. John's λόγος theology is incomprehensible without Philo. The "Son of Man" cannot be fully understood without 1 Enoch's development of that figure. The Sabbath controversy narratives require knowing the Mishnah's 39 prohibited labor categories. The Dead Sea Scrolls use many of the same terms as the NT with similar sectarian intensity.

**New data file:** `data/second-temple/context.json` — ~80 curated entries:
```
Schema: { id, strongs_keys[], trigger_passages[], source, source_work,
  source_date, context, significance, representative_quote }
```

**~80 entries to generate (agent task):**
- Philo: Logos / Wisdom (for John 1); allegorical interpretation method
- Josephus: Pharisees, Sadducees, Essenes, Zealots (for Gospel controversies)
- Dead Sea Scrolls: light/darkness dualism (1QS — for John's idiom), messianic expectations, community boundary markers
- 1 Enoch: Son of Man as heavenly pre-existent judge (for Dan 7 + Gospels)
- Psalms of Solomon: Davidic messianism (for Palm Sunday + messianic expectation)
- Mishnah Shabbat 7:2: 39 prohibited Sabbath labor categories (for healing controversies)
- 4 Ezra / 2 Baruch: post-70 AD Jewish grief and hope (for Matthew 24 + Revelation context)
- Targum renderings of key OT texts (Isa 53, Ps 22, Ps 110)

**Tasks:**
- [ ] Agent task: generate `data/second-temple/context.json`
- [ ] In passage view: Second Temple Context collapsible panel when entries match current passage's Strong's codes or references
- [ ] CSS: `.sw-second-temple`, `.sw-st-source-chip`, `.sw-st-quote`

**Verify:** Study John 1:1 → Second Temple Context panel surfaces Philo Logos entry with source, date, context summary, significance (John establishes the frame, then explodes it with the Incarnation), representative quote.

---

### SW-M · Passage synthesis panel *(MEDIUM — integrates all layers)*

**Why:** Individual layers are valuable, but the interpretive payoff is synthesis. A scholar's commentary is not a list of word studies — it is an argument integrating grammar, lexical range, literary structure, cultural background, and intertextual context into a coherent reading of authorial intent. This panel provides that synthesis, initially agent-generated for key passages, always user-editable.

**New data:** `data/synthesis/{book}.json` — per-book, keyed by pericope reference:
```
Schema per pericope: { pericope_label, literary_note,
  key_terms: [{ code, note }],
  cultural_notes: [],
  intertextual_connections: [],
  synthesis: "one coherent paragraph",
  tradition_map: { patristic, reformation, modern_debates: [] } }
```

**Tasks:**
- [ ] Agent task: generate `data/synthesis/` for the 60 most-studied pericopes (NT: Gospel major discourses, Paul's thesis paragraphs, epistolary argument units; OT: Gen 1, Exod 3, Isa 53, Ps 22, Ps 110, Ruth 1, etc.)
- [ ] Synthesis tab in passage view: pericope label + literary note; key terms as clickable chips (click → open dossier) with interpretation note; cultural notes callout; intertextual connection links; synthesis paragraph in a prominent block; tradition map accordion
- [ ] User synthesis section: editable textarea per passage, localStorage-persisted at `bsw_ws_synthesis_${ref}`; auto-saves on blur
- [ ] "Export Study Sheet" button: renders passage + dossier summaries + synthesis + user notes as printable HTML

**Verify:** Study Rom 3:21–26 → Synthesis tab shows: pericope label ("The Thesis of Romans"), literary note (this is the hinge of the letter), key term notes for δικαιοσύνη and ἱλαστήριον, tradition map showing propitiation/expiation debate and New Perspective.

---

### SW-N · Study notes and vocabulary learning mode *(LOWER priority)*

**Study notes:**
- [ ] Personal passage notes: `localStorage['bsw_ws_passage_notes'][ref]` — textarea per reference; auto-saves on blur
- [ ] "Link to this word" — generates `translation/workshop/?s=G3056` URL
- [ ] Export Study Sheet (also wired in SW-M): `window.print()` with print-specific stylesheet hiding nav/sidebars

**Vocabulary flashcard mode:**
- [ ] "Learn Vocabulary" nav toggle → flashcard view: word large center; tap reveals transliteration, POS, gloss, frequency, 3 verse samples
- [ ] Default decks: Phase 1 (top 200 NT Greek — ~80% of NT occurrences) + Phase 2 (top 200 OT Hebrew)
- [ ] Custom deck: "Add to deck" button in dossier → `localStorage['bsw_ws_flashcards']`
- [ ] Spaced repetition: 4-button rating (Again 1d / Hard 3d / Good 7d / Easy 21d); next-review timestamps in localStorage
- [ ] Progress: % of deck reviewed today + streak counter

**Verify:** Export Study Sheet after studying John 1:1 → printable page renders with interlinear, λόγος dossier summary, synthesis note, user notes. Vocabulary mode: λόγος on front; tap → gloss + frequency + 3 samples; "Good" → marked for 7-day review.

---

## Data Path Integrity Audit — Dimension 4, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked echoes (66/66 ✓), all 11 commentary sources (66/66 ✓ — `barnes`/`rwp` OT files are intentional 2-byte `{}` stubs matching their NT-only scope), all 3 MKT tier draft paths (`data/translation/draft/literal|mediating|thought/` — 66/66 ✓), all 8 plans (✓), `data/library/index.json` (182 docs — 138 HTML + 44 JSON, 0 missing ✓), `manifest.json` shortcuts (3/3 ✓), `data/topics.json` (15/15 ✓), `data/votd/verses.json` (366 entries ✓), `data/devotionals/spurgeon-{morning,evening}.json` (366 entries ✓). One gap found: `data/translation/notes/1kings/22.json` missing.*

---

*(DATA-11 complete — see working/todo-archive.md 2026-06-06)*

---

## Data Path Integrity Audit — Dimension 4, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Cycle 5 checked echoes, commentary, MKT drafts, plans, library index, manifest, topics.json, votd, devotionals. This pass checked `data/torrey/verse-index/` completeness against the canonical 66 books. 64/66 present: `isaiah.json` and `jude.json` both absent. Traced root cause to two bugs in `scripts/fetch-torrey.py`: (1) `_BOOK_PREFIX_RE` regex `[a-z]{0,2}` caps lowercase at 2, so `Jude` (3 lowercase) never matches; (2) `TORREY_ABBREVS` maps `'Is':'isaiah'` but the CrossWire Torrey SWORD module likely uses `Isa`, causing 0 Isaiah entries in `torrey.json`. Confirmed: `python3 -c "import json; d=json.load(open('data/torrey/torrey.json')); print(sum(1 for t in d for v in t.get('verses',[]) if v.startswith('isaiah:')))"`  → 0.*

---

*(DATA-12 complete — see working/todo-archive.md 2026-06-06)*

---

## Data Path Integrity Audit — Dimension 4, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked: all 66 `data/books/introductions/` files (min size 6.5KB, 0 hollow stubs ✓); Strongs files (`greek.json` 5523 entries, `hebrew.json` 8674 entries, `bdb.json`/`thayer.json` 1.4–1.9MB each, `lxx-bridge.json` 17 curated entries ✓); library: 0 missing source files across 182 docs ✓; Smith verse-index: 66/66 ✓ (DATA-10 confirmed fixed); parallels: 54/66 — 12 books intentionally absent (2 John, 3 John, Ecclesiastes, Esther, Lamentations, Nahum, Nehemiah, Obadiah, Philemon, Ruth, Song of Solomon, Zephaniah — all handled with "Not available." fallback ✓); `votd/verses.json` 175 entries — uses `(doy - 1) % verses.length` modulo cycling, correct behaviour ✓; commentary sources (11): mhcc/ellicott/jfb/clarke/calvin/barnes/rwp/mkt stubs all as documented in prior cycles ✓; workshop phase files: phase1/phase2/phase5 only (intentional — workshop.js lines 60–62 define exactly these 3 phases) ✓. One regression found: DATA-11 was marked complete but `data/translation/notes/1kings/22.json` is still absent — see DATA-13.*

---

*(DATA-13 complete — see working/todo-archive.md 2026-06-06)*

---

## Feature Completeness Audit — Dimension 5, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: all 6 reading plans (total_days matches data array ✓); word cloud scopes (11 scopes, all fields present in `frequencies.json` ✓); study guide pages (Hebrews 14 sections, Ephesians 27, Romans 1–8 36, Sermon on the Mount 23, Psalms 20 — all static HTML with real content ✓); nav links including `studies/`, `apocrypha/`, `progress/`, `library/progress/` (all resolve ✓); `plans/` redirect stub correctly forwards to `discipline/?tab=plans` ✓; MKT commentary (mkt-original/context/christ) for John 1:1 confirmed populated ✓. Commentary source picker gap found: `rwp` label missing "(NT)" scope indicator; Calvin has 18 books silently empty.*

---

*(AUD-14 complete — see working/todo-archive.md 2026-06-06)*

---

## Feature Completeness Audit — Dimension 5, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked all 11 commentary sources for coverage gaps. Ellicott, JFB, Clarke: 0 empty books ✓. Barnes (NT) and rwp (NT): 39 empty OT books each — expected by scope label ✓. MKT-original/context/christ: 0 empty books ✓. Calvin: 18 empty books — aligns with Calvin's actual corpus (he did not write on Samuel, Kings, Chronicles, Ezra, Nehemiah, Esther, Job, Proverbs, Ecclesiastes, Song of Solomon, Judges, Ruth, 2 John, 3 John, Revelation) — expected, though no label scope indicator. Wesley: 2 books empty — `1kings.json` and `philemon.json` are 2-byte `{}` stubs despite Wesley's Notes covering all 66 canonical books — data pipeline error.*

---

*(AUD-16 data-blocked — CrossWire Wesley SWORD module has entry_size=0 for all 1Kings and Philemon positions; no data exists in the upstream source to regenerate. Investigated 2026-06-06.)*

---

### SW-O · Integration and wire-up pass *(final pass — after SW-A through SW-N)*

**After all data layers and components exist, wire them into a coherent experience:**

- [ ] **Auto-surface "What to notice here" banner** on passage load: detects discourse markers present, grammar debates triggered, idioms found, OT quotations (from echoes data), relevant cultural frameworks — summarizes in a small collapsible banner above the interlinear tiles
- [ ] **Cross-navigation everywhere:** verse sample → study that passage; cognate chip → open that word; echo reference → open target passage; OT-in-NT → open both references side-by-side
- [ ] **Mobile layout:** passage view full-width; tile tap → dossier as bottom sheet (slides up, swipe-down dismisses); tabs as horizontal scroll strip; discourse marker badges as single-letter chips
- [ ] **PWA shell:** Add all new data paths to sw.js SHELL_URLS or lazy-cache via `cacheFirst` on first access: `data/grammar/` (4 files), `data/cultural/` (3 files), `data/idioms.json`, `data/idioms-index.json`, `data/literary/` (4 files), `data/second-temple/context.json`, `data/ot-in-nt/quotations.json`, `data/synthesis/` (per-book, lazy)
- [ ] **Performance:** all new data lazy-loaded (fetch on first passage study, cached in memory + service worker); none blocking initial page load; large files split per-book

**Verify (golden path):** Enter "Romans 8:1" →
- Interlinear renders with οὖν highlighted (inference badge)
- Literary tab: genre card (epistle/diatribe) + argument structure showing 8:1 as conclusion of chs.1–7
- Cultural tab: honor-shame + patron-client frameworks; Romans book-context card
- Intertextual tab: relevant echoes listed
- Synthesis tab: thesis-sentence synthesis, tradition map
- Click οὖν → dossier slides in: particle significance card ("Therefore — conclusion of a 7-chapter argument"), Grammar section
- Works on mobile as bottom sheet; works offline (all data cached)

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked all SHELL_URLS CSS (26/26 ✓), SHELL_URLS JS (31/31 ✓ — workshop.js intentionally absent), history hub iframes (4/4 targets resolve ✓), discipline hub iframes (3/3 resolve ✓), search/?tab=dictionary → dictionary/index.html ✓, search/?tab=wordcloud → wordcloud/index.html ✓, studies/index.html in SHELL_URLS ✓, tooltip.js registered in app.js ✓. No new navigation or discoverability gaps found this cycle.*

---

## PWA & Offline Audit — Dimension 9, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: manifest.json shortcuts (read/, verse-study/, notes/ — all 3 resolve ✓); top-level data JSON files on disk (topics.json 1.7KB, topics-index.json 3.6KB, apocrypha-books.json ✓, apocrypha-canon-orders.json ✓); SHELL_URLS cross-reference of all CSS/JS (verified above in Dim 8). One gap found: data/topics.json and data/topics-index.json both absent from SHELL_URLS despite being critical for offline use — topics.json drives the Studies sidebar section on every page.*

---

*(PWA-8 complete — see working/todo-archive.md 2026-06-06)*

---

## Accessibility Audit — Dimension 10, Cycle 5

*Audit pass 2026-06-06 (Cycle 5). Checked: daily.js tab ARIA (tab buttons update aria-selected on click at lines 756, 836, 1097 ✓); word.js (no tablist UI — clean ✓); search.js + search/index.html — ARIA gap found (see AUD-15). apocrypha/index.html (no tab group in HTML — clean ✓). Other JS files (lib-browser, lib-reader, lib-progress, ol-companion) all verified in prior cycles.*

---

*(AUD-15 complete — see working/todo-archive.md 2026-06-06)*

---

## Accessibility Audit — Dimension 10, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: `maps.js` map-selector nav and panel tab buttons, `timelapse-map.js` play/step/slider/speed controls, `maps/index.html` and `maps/timelapse/index.html`. Prior cycles: reader/modal/sidebar/search/daily/apocrypha/ol-companion/lib-reader/lib-browser/verse-study all covered. Maps and timelapse were the last unchecked interactive feature areas. Gap found: AUD-17.*

---

*(AUD-17 complete — see working/todo-archive.md 2026-06-06)*

---

## Accessibility Audit — Dimension 10, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked: `word/index.html` — `<select id="bible-version">` has explicit `<label for="bible-version">` ✓; `dictionary/index.html` — `role="group"` + `aria-label` on filter group, `role="tablist"` + `aria-label` on alpha nav ✓; `timeline/index.html` — search input has `aria-label` ✓; `notes/index.html` — `role="tablist"` + `role="tab"` present but buttons missing `aria-selected` in HTML and `renderTabs()` never sets it — screen readers can't determine active tab — AUD-18.*

---

*(AUD-18 complete — see working/todo-archive.md 2026-06-06)*

---

## Accessibility Audit — Dimension 10, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: `timeline/index.html` — only interactive element is search input with `aria-label="Search events"` ✓; `compare/index.html` — `#cmp-ref-input` text input has no `<label>` and no `aria-label`; placeholder is not an accessible name — screen readers announce as "edit text" — AUD-19. `progress/index.html` — only chapter link grid, no interactive controls needing ARIA ✓. Dims 2, 4, 5, 6, 8 Cycle 7 all clean passes — worship/reflections/prayer empty states handled, data paths intact, feature implementations complete, no debounce gaps, all nav links resolve.*

---

*(AUD-19 complete — see working/todo-archive.md 2026-06-06)*

---

## Navigation & Discoverability Audit — Dimension 8, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: all 73 `index.html` files on disk cross-referenced against `sw.js` SHELL_URLS (lines 29–212) — all accounted for; 2 known intentional gaps remain: `topics/holy-catholic-church/index.html` (LOW, not all topics precached — documented Cycle 2) and `translation/workshop/index.html` (intentional dev tool, not for offline use — documented Cycle 2). `main.js` NAV array (lines 53–109) — all 15+ nav targets resolve ✓. `data/topics.json` — all 15 entries (10 topical + 5 study-guide slugs) match on-disk directories ✓. `data/library/index.json` — 182/182 documents have corresponding data files ✓. Topic page internal cross-links (30+ hrefs across 10 pages) — all resolve ✓. Study-guide internal links — all resolve ✓. `compare/index.html` ✓ (sw.js line 37), `progress/index.html` ✓ (line 100), `library/read/index.html` ✓ (line 202). No new findings this cycle.*

---

## PWA & Offline Audit — Dimension 9, Cycle 6

*Audit pass 2026-06-06 (Cycle 6). Checked: CSS on disk (27 files) vs SHELL_URLS — 26/26 ✓ (workshop.css intentionally absent); JS on disk (32 files) vs SHELL_URLS — 31/31 ✓ (workshop.js intentionally absent); manifest.json shortcuts (read/, verse-study/, notes/ — all 3 resolve ✓); `data/books/introductions/` (66 per-book JSONs) — correctly lazy-fetched by reader.js on demand, no precache needed ✓; `data/translation/` — dev-tool workshop data, intentionally absent ✓. Gap found: `data/maps/places.json` and `data/maps/timelapse.json` both missing from SHELL_URLS — see PWA-10.*

---

*(PWA-10 complete — see working/todo-archive.md 2026-06-06)*

---

## Feature Completeness Audit — Dimension 5, Cycle 7

*Audit pass 2026-06-06 (Cycle 7). Checked: MKT commentary chapter-level coverage for books marked complete in MKT progress tracking. mkt-original/acts: 28/28 ✓. mkt-context/acts: 28/28 ✓. mkt-christ/acts: 27/28 — chapter 27 absent despite Acts being flagged complete 2026-06-03; other 27 chapters (1–26 and 28) all populated with real content. mkt-original/luke: 24/24 ✓. mkt-context/luke: 24/24 ✓. mkt-christ/luke: 24/24 ✓. Gap found: DATA-14.*

---

*(DATA-14 complete — see working/todo-archive.md 2026-06-06)*

---

## Empty State & Loading State Audit — Dimension 2, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Verified remaining unchecked areas: `core.js` — `loadBooks()` `.catch()` degrades to `metaBooks=[]` silently; would leave reader book-dropdown empty and notes page without book metadata, but `books.json` is precached in SW making this scenario theoretically impossible under normal conditions ✓ (acceptable degradation). `notes/index.html` inline fetch — partial mitigation via toast on verse-picker ✓ (consistent with precaching argument above). `discipline/index.html` plan fetch `.catch()` → `devotRender(null)` shows `devot-empty` element correctly ✓; all plan JSONs are precached ✓. No new actionable items this cycle — all gaps are gated on simultaneous SW-cache and network failure for precached assets.*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked `style.css` — the one CSS file not explicitly covered in prior D3 cycles. Hamburger button correctly sized (`min-height: 44px; min-width: 44px` at lines 402–403) ✓. `.sb-link` mobile override (`padding: 0.75rem 1rem`) gives ~44px ✓. Gap found: `.plans-widget__passage` (home-page "Today's Reading" passage chip-links) — `padding: 0.18rem 0.5rem; font-size: 0.82rem` gives ~19px height; no `@media (max-width: 1023px)` override exists for these. See CSS-29.*

---

*(CSS-29 complete — see working/todo-archive.md 2026-06-06)*

---

## Mobile Responsiveness Audit — Dimension 3, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Checked `discipline.css` (not covered in D3 Cycle 8). `.disc-tab` desktop (`padding: .65rem 1.05rem; font-size: .85rem`) → ~39px — borderline but acceptable on desktop ✓. Mobile override (`@media (max-width: 500px)`): `.disc-tab { padding: .55rem .7rem; font-size: .78rem }` → ~34px, under 44px — CSS-31. `.journal-btn--sm { font-size: .75rem; padding: .2rem .55rem }` → ~22px at all viewports — CSS-31. No override exists in the mobile block for either. Also checked: `word.css` (no interactive controls at <500px ✓), `notes/index.html` inline styles (none ✓). Gap: CSS-31.*

---

*(CSS-31 complete — see working/todo-archive.md 2026-06-06)*

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

## Navigation & Discoverability Audit — Dimension 8, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: all 76 `index.html` files on disk cross-referenced against `sw.js` SHELL_URLS — 71/71 page URLs present ✓; 5 intentional omissions: `study-guides/_template/` (template, not a page), `topics/_template/` (template), `topics/_template-book/` (template), `topics/holy-catholic-church/` (known gap from Cycle 2 — one topic intentionally unprecached), `translation/workshop/` (dev tool, documented Cycle 2). No new pages added since last cycle. No new navigation issues.*

---

## PWA & Offline Audit — Dimension 9, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Verified PWA-10 fix in place: `./data/maps/places.json` (line 215) and `./data/maps/timelapse.json` (line 216) both present in SHELL_URLS ✓. Spot-checked all root-level data JSON files: `topics.json`, `apocrypha-books.json`, `apocrypha-canon-orders.json`, `topics-index.json` — all 4 on disk and in SHELL_URLS ✓. Key eager-fetch files confirmed: `books.json`, `versions.json`, `frequencies.json`, `verses.json` — all precached ✓. No new PWA issues found this cycle.*

---

## Accessibility Audit — Dimension 10, Cycle 9

*Audit pass 2026-06-06 (Cycle 9). Found 3 ARIA gaps in `discipline/index.html` — see AUD-20.*

---

*(AUD-20 complete — see working/todo-archive.md 2026-06-06)*

---

## Feature Completeness Audit — Dimension 5, Cycle 8

*Audit pass 2026-06-06 (Cycle 8). Checked: (1) `data/topics-index.json` — all 10 topic entries without explicit `href` resolve to real `topics/{slug}/index.html` pages (christology, covenants, holy-catholic-church, holy-spirit, justification, prayer, psalms, revelation, romans, sermon-on-the-mount all ✓); all 5 study-guide entries with explicit `href` also verified on disk ✓. (2) Library — all 182 docs in `data/library/index.json` are present on disk (html or json format), none are stubs under 100 bytes ✓. (3) Reading plans — all 8 plan files in `data/plans/` have correct day counts matching `total_days` field (365, 365, 365, 90, 31, 30, 52, 13 — all ✓); all 8 cached in `sw.js` SHELL_URLS ✓. (4) Catechism plans (heidelberg-weekly, wsc-quarterly) removed from `daily.js` home selector but remain accessible via `discipline/?tab=plans` which uses a separate `PLAN_IDS` array covering all 8 ✓. (5) All 5 study guide directories exist (`study-guides/hebrews/`, `romans-1-8/`, `ephesians/`, `sermon-on-the-mount/`, `psalms/`) ✓. (6) All discipline page tabs (plans, devotionals, memory, journal, worship, notes, progress, history) have corresponding `disc-panel` sections; `progress/index.html` and `tracker/index.html` both exist ✓. (7) `plans/index.html` is a redirect to `discipline/?tab=plans` ✓. No new feature completeness gaps found this cycle.*
