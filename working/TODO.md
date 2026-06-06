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

### NAV-4 — verse-study chapter-boundary navigation dead-end

**Priority:** MEDIUM  
**File:** `assets/js/verse-study.js` lines 222–243

The prev/next verse navigation in `verse-study/` silently hides when it reaches a chapter boundary:
- **At verse 1** (`pv = 0`): `pv >= 1` is false → `prevNavLink` gets `hidden` attribute. No link to the previous chapter's last verse.
- **At the last verse** (e.g., John 3:36): `chData[String(37)]` is undefined → `nextNavLink` gets `hidden` attribute. No link to John 4:1.

A user studying verse-by-verse reaches the end of a chapter and the navigation arrow simply vanishes. To continue to the next chapter, they must use "← Reader" (back to the reader), then re-navigate to the next chapter — three extra steps.

**Fix:** When the end-of-chapter check fails, instead of hiding the link, show a chapter-jump: `nextNavLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(bookName + ' ' + (ch+1) + ':1')` with label `›› Ch {ch+1}`. For prev: link to the reader at the previous chapter with a note (`← Ch {ch-1}`), or pre-load the previous chapter's data to determine its last verse number. The simplest option is a chapter-level jump (Ch N+1 : 1 / Ch N-1 : last) using `metaBooks[book].chapters` to guard against wrapping past the last chapter.

**Verify:** Navigate to verse-study for John 1:1 → prev link shows `← Ch reader` or is absent for chapter 1, verse 1 of the book. Navigate to last verse of John 3 → next link shows `›› Ch 4` linking to John 4:1.

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

## Data Path Integrity Audit — Dimension 4, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle verified all 18 canonical Bible versions, 8 commentary sources, crossrefs, interlinear, plans, library docs, manifest shortcuts, and nav hrefs. This pass checked the new apocrypha data layer (`data/bible-apocrypha/`, `apocrypha-books.json`, `apocrypha-canon-orders.json`) and JS fetch paths in `apocrypha-reader.js`, `terms.js`, `places.js`.*

---

### DATA-3 · BRENTON version missing scope correction and 3 canonical OT books *(MEDIUM)* *(partially done: code complete, data pending)*

**Problem:** `data/versions/versions.json` declares `BRENTON` with `"scope": "full-bible"` and `"canon_order": "lxx"`. The `lxx` canon order in `apocrypha-canon-orders.json` lists 83 books (66 canonical + 17 deuterocanonical). However, `data/bible-apocrypha/BRENTON/` only has 51 files — the Brenton LXX is an Old Testament translation only with no NT content. The apocrypha reader uses `_isFullBible()` (`scope === 'full-bible'`) to decide whether to show NT navigation, so on BRENTON all 27 NT books appear in the book list but every one 404s when clicked. Additionally, 3 canonical OT books are missing from the BRENTON directory: `esther` (only `additions-esther.json` present — the Greek Esther with additions is there, but `esther.json` for the base canonical MT-mapped form is absent), `daniel` (LXX Daniel includes additions but no `daniel.json` base file), and `nahum` (no equivalent in the BRENTON directory — genuinely missing).

**Code fix applied (2026-06-05):** Changed BRENTON `scope` in `data/versions/versions.json` from `"full-bible"` → `"ot-only"`. Updated `_getOrderedBooks()` in `apocrypha-reader.js` to: (1) use the canon order for any version that has one (not just full-bible), and (2) filter out NT canonical books for `ot-only` scope. This stops the 27 NT 404s. The 3 missing OT data files remain blocked.

**Fix:**
- `data/versions/versions.json` (`BRENTON` entry): Change `"scope": "full-bible"` → `"scope": "ot-only"` (or add a new `"scope": "lxx-ot"` value). Update `_isFullBible()` in `apocrypha-reader.js` to return false for OT-only scopes.
- `data/bible-apocrypha/BRENTON/`: Re-run the fetch script to populate `nahum.json`. Verify whether `daniel.json` and `esther.json` are needed as canon-mapped aliases (vs. the LXX-specific `additions-*` variants already present).

**Verify:** Open the apocrypha reader, select BRENTON, confirm the book list shows only OT books. Navigate to Nahum — it should load without a 404.

---

### DATA-4 · DR apocrypha version missing 4 Daniel/Esther additions *(LOW)*

**Problem:** `data/bible-apocrypha/DR/` has 73 files but the `dr` canon order in `apocrypha-canon-orders.json` lists 77 books. Four books in the DR canon are missing from the directory: `additions-esther`, `prayer-of-azariah`, `susanna`, and `bel-and-dragon`. All four are Daniel/Esther additions that the Douay-Rheims includes (as chapters of Daniel and Esther). When a user selects the DR version and navigates to any of these four books, the apocrypha reader shows a fetch error.

**Fix:**
- `data/bible-apocrypha/DR/`: Re-run `scripts/fetch-apocrypha.py` (or equivalent) targeting the DR version for `additions-esther`, `prayer-of-azariah`, `susanna`, `bel-and-dragon`. If the DR source treats these as chapters of Daniel/Esther rather than standalone books, update the `dr` canon order in `apocrypha-canon-orders.json` to remove the standalone entries.

**Verify:** Open the apocrypha reader with DR selected, navigate to Susanna — it should load content, not a fetch error.

---

## Data Path Integrity Audit — Dimension 4, Cycle 3

*Audit pass 2026-06-05 (cycle 3). Cross-checked all translation data paths (notes + 3 MKT draft tiers × 66 books = 264 files — all present). All 8 registered commentary sources have complete 66-book coverage. Topics.json href links all resolve. Found one new gap: WEB-CE has the same Daniel-additions data gap as DR (DATA-4) but with a slightly different set of missing books.*

---

### DATA-5 · WEB-CE full-bible version missing 3 Daniel-addition books *(MEDIUM)*

**Problem:** `data/bible-apocrypha/WEB-CE/` has 74 files but the `dr` canon order it shares with DR lists 77 books. Three books present in the canon order are missing from the WEB-CE directory: `bel-and-dragon`, `prayer-of-azariah`, and `susanna`. (DR has an additional gap — `additions-esther` — that WEB-CE does not.) All three are Daniel additions in the Catholic/deuterocanonical tradition. WEB-CE is the World English Bible with Deuterocanonicals, marketed as a full-Bible version. When a user selects WEB-CE and navigates to Bel and the Dragon, Prayer of Azariah, or Susanna, the apocrypha reader shows: `"[Book] is not yet available in World English Bible: Catholic Edition."` — a confusing error for a version that claims full coverage.

**Fix:**
- `data/bible-apocrypha/WEB-CE/`: Run `scripts/fetch-apocrypha.py` (or equivalent) targeting WEB-CE for `bel-and-dragon`, `prayer-of-azariah`, `susanna`. These three books ARE available in the WEB-CE source — they are the same Daniel additions that appear in Catholic editions.

**Verify:** Open apocrypha reader with WEB-CE selected, navigate to Susanna — it should display verses, not a fetch error.

---

### DATA-6 · DR / KJV-APO / WEB-CE canonical books contaminated with Strong's markup *(HIGH)*

**Problem:** The 66 canonical book files in `data/bible-apocrypha/DR/`, `KJV-APO/`, and `WEB-CE/` were fetched with Strong's interlinear annotations left in the verse text — e.g. `In|strong="H0430"the|strong="H0853"beginning…`. Contamination rates: DR 87%, KJV-APO 100%, WEB-CE 99.8%. The apocrypha-specific books (tobit, sirach, etc.) in the same directories are clean — only the canonical copies are affected. This makes every canonical chapter unreadable in these three versions.

**Fix:**
- Write `scripts/fix-apocrypha-strongs.py` that walks all three version directories, strips the pattern `\|strong="[HG]\d+"` (and surrounding whitespace artifacts such as `\s*\|strong="[HG]\d+"\s*`) from every verse string, and writes the files back in-place.
- Run it and spot-check: `DR/genesis 1:1` should read `"In the beginning God created the heaven and the earth."` with no pipe characters.

**Verify:** Open apocrypha reader, select DR, navigate to Genesis 1 — verses should be plain readable English with no `|strong=` artifacts.

---

### DATA-7 · BRENTON missing spaces in verse text (~1% of verses) *(MEDIUM)*

**Problem:** `data/bible-apocrypha/BRENTON/` has ~399 verses (~1%) where words are concatenated without spaces — e.g. `"Thebook"`, `"sonof"`, `"Inthe"`, `"Loverighteousness"`, `"Whereasmany"`. Affects both canonical and apocrypha-specific books. Root cause: the eBible.org USFM source has inline markers that the fetch script failed to tokenise correctly, causing adjacent words to merge.

**Fix (preferred):** Re-run `scripts/fetch-apocrypha.py BRENTON --force` to re-fetch from eBible.org with corrected USFM tokenisation.

**Fix (fallback):** Post-processing pass — `re.sub(r'([a-z])([A-Z])', r'\1 \2', text)` on all verse strings in `data/bible-apocrypha/BRENTON/`. Low false-positive risk in Biblical text (no camelCase proper nouns). After running, recheck count: should drop from 399 to 0.

**Verify:** BRENTON/tobit 1:1 should read `"The book of the words of Tobit…"` not `"Thebook of the words of Tobit…"`.

---

### DATA-8 · additions-esther chapter count mismatch — WEB-CE and BRENTON have 10 chapters, expected 7 *(LOW)*

**Problem:** `apocrypha-books.json` declares `additions-esther` as 7 chapters, but both `data/bible-apocrypha/WEB-CE/additions-esther.json` and `data/bible-apocrypha/BRENTON/additions-esther.json` contain 10 chapters. The traditional "Additions to Esther" (Deuterocanonical) has 6 lettered sections (A–F) in NRSV convention, or 7 chapters in some enumerations. 10 chapters matches neither — the source likely used the Greek Esther continuous chapter numbering (chapters 11–16 of a combined Hebrew+Greek Esther).

**Fix:**
- Inspect both files: determine what chapter keys are used and what content is in them.
- Either: (a) update `apocrypha-books.json` to reflect the correct count for this numbering convention, or (b) restructure the files to the declared 7-chapter schema if the source supports it.
- Update `apocrypha-canon-orders.json` chapter count field if needed.

**Verify:** The apocrypha reader should navigate additions-esther chapter by chapter without a "chapter not found" error at any step.

---

### DATA-9 · BRENTON Baruch missing chapter 6 (Letter of Jeremiah) *(LOW)*

**Problem:** `data/bible-apocrypha/BRENTON/baruch.json` has 5 chapters; `apocrypha-books.json` declares 6. Chapter 6 of Baruch is the "Letter of Jeremiah" — a distinct text traditionally appended to Baruch in LXX manuscripts, included in Brenton's 1851 translation.

**Fix:**
- Re-run `scripts/fetch-apocrypha.py BRENTON --force` to re-fetch, or manually source Brenton's Baruch chapter 6 from Wikisource (public domain) and append to the file as chapter key `"6"` with verse keys `"1"` through `"73"`.
- Expected opening: `"The copy of an epistle, which Jeremy sent unto them which were to be led captives into Babylon…"`

**Verify:** BRENTON/baruch.json has chapters 1–6; navigating to chapter 6 in the apocrypha reader shows the Letter of Jeremiah text.

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

## Reader Interlinear — Popover Bugs

Four bugs in the interlinear tile popover (`assets/js/interlinear.js` — `_riShowPopover`, `renderReaderInterlinearRow`).

---

### RI-A · Popover spawns off-screen on right edge and bottom edge *(HIGH)*

**Root cause:** The popover is `position: fixed` in CSS (`reader.css:2020`), which means coordinates are viewport-relative. But `_riShowPopover` (interlinear.js:393–395) positions it with:
```js
pop.style.top  = (r.bottom + window.scrollY + 4) + 'px';
pop.style.left = Math.max(8, r.left + window.scrollX) + 'px';
```
Adding `window.scrollY` / `window.scrollX` to a `fixed` element's coordinates pushes it far below and to the right of the viewport whenever the user has scrolled. With `fixed` positioning, `getBoundingClientRect()` already returns viewport coordinates — scroll offsets must not be added.

Additionally there is no right-edge or bottom-edge clamping: a tile near the right side of the screen will cause the 280px popover to overflow the viewport, and a tile near the bottom will push the popover below the fold.

**Fix — interlinear.js `_riShowPopover`, lines 393–395:**
```js
var POP_W = 280;
var POP_MARGIN = 8;
var r = tile.getBoundingClientRect();

// Position below tile; flip above if it would overflow the bottom
var topBelow = r.bottom + 4;
var topAbove = r.top - 4;  // will subtract pop height after render
pop.style.left = Math.min(
  Math.max(POP_MARGIN, r.left),
  window.innerWidth - POP_W - POP_MARGIN
) + 'px';
pop.style.top = topBelow + 'px';  // initial placement; adjust after render

// After the element is in the DOM, flip above if it overflows the bottom
requestAnimationFrame(function () {
  var popH = pop.offsetHeight;
  if (topBelow + popH > window.innerHeight - POP_MARGIN) {
    pop.style.top = Math.max(POP_MARGIN, r.top - popH - 4) + 'px';
  }
});
```
Remove `window.scrollY` and `window.scrollX` from both lines.

**Verify:** Click a tile on a word near the right edge of the interlinear row — popover should stay fully within the viewport. Click a tile on the last verse in a chapter — popover should flip above the tile rather than disappearing below the fold.

---

### RI-B · Popover stays fixed on screen when user scrolls — loses connection to tile *(HIGH)*

**Root cause:** The popover is `position: fixed` and is never repositioned or removed when the reader scroll container scrolls. After the user scrolls a few lines, the popover floats at its original screen position with no visible connection to any tile, covering unrelated text.

**Fix — interlinear.js `_riShowPopover`:**
Add a one-shot scroll listener on the reader's scroll container that closes the popover when the user scrolls:
```js
// Close on scroll — fixed popover can't track the tile
var _scrollClose = function () {
  if (_riPopoverEl) { _riPopoverEl.remove(); _riPopoverEl = null; }
  _scrollTarget.removeEventListener('scroll', _scrollClose);
};
var _scrollTarget = document.querySelector('.reader-content') ||
                    document.getElementById('reader-results') ||
                    window;
_scrollTarget.addEventListener('scroll', _scrollClose, { passive: true });
```
Store a reference to the scroll listener alongside `_riPopoverEl` so it can be removed when the popover is closed by other means (close button, outside click).

**Verify:** Open an interlinear popover, then scroll the reader. The popover should disappear immediately on scroll rather than floating adrift over the text.

---

### RI-C · No "Word Study" link in popover — was present before, now missing *(HIGH)*

**Root cause:** `_riShowPopover` (interlinear.js:377–388) builds the popover HTML with close button, header, orig, def, and deriv — but no links section. The CSS already has `.ri-popover__links` and `.ri-popover__links .vs-context-btn` (reader.css:2115–2125), confirming the section was planned and previously existed but was dropped from the JS render.

The word study URL pattern is `WORD_URL + '?s=' + strongs` (matches verse-study.js:508, 573, 707). `WORD_URL` is exported from `core.js` line 45 but is not currently imported in `interlinear.js`.

**Fix — interlinear.js:**
1. Add `WORD_URL` to the import from `./core.js` (line 6).
2. Append a links block to the popover HTML in `_riShowPopover`:
```js
'<div class="ri-popover__links">' +
  '<a class="vs-context-btn" href="' + escHtml(WORD_URL + '?s=' + encodeURIComponent(strongs)) + '" ' +
     'title="Open full word study">' +
    'Word Study →' +
  '</a>' +
'</div>'
```

**Verify:** Click any interlinear tile — the popover should show a "Word Study →" link at the bottom. Clicking it should navigate to the word study page for that Strong's code (e.g. `word/?s=G3056`).

---

### RI-D · Tile click feels unresponsive — no active state, outside-click timing bug *(MEDIUM)*

**Root causes:**
1. `.ri-tile--active` is defined in CSS (`reader.css:1966`) but the JS never applies it — there is no visual feedback between click and popover render, making repeated clicks feel ignored.
2. The outside-click listener is registered inside a `setTimeout(10ms)` (interlinear.js:398–402). On fast clicks this can race: the tile click event propagates, the 10ms fires, and the newly created outside-click listener immediately closes the popover it just opened. Using `e.stopPropagation()` on the tile click is cleaner and removes the race.
3. Touch targets: `.ri-tile` has no explicit minimum height/touch-area, making it hard to tap accurately on mobile.

**Fix — interlinear.js `renderReaderInterlinearRow` and `_riShowPopover`:**

In `renderReaderInterlinearRow`, change the tile click handler:
```js
tile.addEventListener('click', function (e) {
  e.stopPropagation();  // prevents immediate outside-click close
  // Remove active state from previously active tile
  if (_riActiveTile && _riActiveTile !== tile) {
    _riActiveTile.classList.remove('ri-tile--active');
  }
  tile.classList.add('ri-tile--active');
  _riShowPopover(tile, strongsDict);
});
```

In `_riShowPopover`, remove the `setTimeout` wrapper and use a direct `document.addEventListener` (safe because `e.stopPropagation()` on the tile prevents immediate close):
```js
// Replace the setTimeout block:
document.addEventListener('click', function _outside(e) {
  if (!pop.contains(e.target)) {
    pop.remove(); _riPopoverEl = null;
    if (_riActiveTile) { _riActiveTile.classList.remove('ri-tile--active'); _riActiveTile = null; }
    document.removeEventListener('click', _outside);
  }
});
```

Also update the close button handler to remove the active class.

**Fix — reader.css:**
Add a minimum touch target to `.ri-tile`:
```css
.ri-tile { min-height: 44px; }  /* WCAG 2.5.5 touch target */
```

**Verify:** Click a tile — it should immediately show an active/highlighted state, and the popover should appear without any flicker or immediate close. Click outside — the popover closes and the tile's active state is removed. On mobile, tapping small tiles should register reliably.

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
