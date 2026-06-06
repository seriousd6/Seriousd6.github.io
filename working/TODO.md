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

### PERF-4 · `vsRenderVersionCompare` unbounded concurrent fetch burst *(MEDIUM)*

**Problem:** `vsRenderVersionCompare` in `assets/js/verse-study.js` (line 981) calls `metaVersions.forEach` and fires one `resolveVerses()` → `loadBook()` call per non-stub version, all simultaneously with no queue or batch size cap. With 11 non-stub versions currently defined in `data/versions/versions.json`, opening the "All Translations" section for the first time triggers 11 concurrent book-JSON fetches at once. Although the section is correctly deferred via `IntersectionObserver` (VS-D), the fetch pattern once visible has no rate limit. This is inconsistent with `word.js`, which adopted a `BATCH_SIZE = 5` sequential-batch pattern (lines 120–128 in `word.js`) specifically to stay within the browser's 6-connection-per-host limit and surface partial results sooner. On a slow connection, all 11 "Loading…" placeholders remain blank until the slowest fetch resolves.

**Fix:**
- `assets/js/verse-study.js` (`vsRenderVersionCompare`): Replace the `metaVersions.forEach` with the same batch-queue pattern from `word.js`: split `filteredVersions` into chunks of 4–5, process chunks sequentially with `Promise.all` per chunk. Each chunk renders as it resolves so early results appear before the last chunk finishes.

**Verify:** In DevTools → Network, filter requests by the current book id (e.g. `john`). Open the verse study page for John 3:16 and scroll to "All Translations" — should see at most 4–5 simultaneous fetch requests at once, followed by a second batch, rather than 11 all at once.

---

*Audit pass 2026-06-05 (Cycle 2). Read: `assets/js/verse-study.js`, `assets/js/daily.js`, `assets/js/ol-companion.js`, `assets/js/apocrypha-reader.js`, `assets/js/word.js`, `assets/js/reader.js`, `assets/js/core.js`. Verified: daily.js fetches only selected devotional (confirmed); `loadLibVerseIndex` is properly cached (confirmed double-call is a no-op at network level); IntersectionObserver deferral confirmed (line 819); word.js BATCH_SIZE=5 confirmed implemented. New finding: vsRenderVersionCompare fires 11 uncapped concurrent fetches — PERF-4.*

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

## Navigation & Discoverability Audit — Dimension 8

*Audit pass 2026-06-05. Checked: all main sidebar nav links (all resolve — `read/`, `apocrypha/`, `search/`, `studies/`, `discipline/`, `history/`, `library/`, `library/progress/`, `translation/workshop/`); all 10 topic cards → real pages; all 5 study guide cards → real pages; history hub 4 iframe tabs (all 4 `data-src` targets exist: `timeline/`, `church-history/`, `maps/`, `maps/timelapse/`); `?minimal=1` mode (correctly early-returns from `buildSidebar()` before both sidebar and mobile topbar are built); `tracker/` (embedded as iframe in `discipline/?tab=history`); `compare/` (linked via `COMPARE_URL` in `modal.js` line 411); `wordcloud/` (embedded as iframe in `search/?tab=wordcloud`). Redirect stubs (`plans/`, `journal/`, `memorize/`, `devotionals/`, `reflections/`) all redirect correctly to discipline tabs.*

---

*(NAV-1 complete — see working/todo-archive.md 2026-06-05)*

---

*(NAV-2 complete — see working/todo-archive.md 2026-06-05)*

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

## Feature Completeness Audit — Dimension 5, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (AUD-1) found the NT Daily Matthew chapter-count bug. This pass checked: ISBE data (9,380 entries + 66-book verse-index — complete), OL Companion wiring (`window.BibleUI.initOLSection` → verse-study.js — correct), book introductions (66/66), Nave's topical verse-index (66/66), topics-index.json (15 entries — all pages resolve), word cloud scopes (unchanged), translation workshop (page exists), apocrypha reader. Found one HIGH bug in apocrypha-reader.js `_getOrderedBooks()`.*

---

*(AUD-6 complete — see working/todo-archive.md 2026-06-05)*

---

## Data Path Integrity Audit — Dimension 4, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle verified all 18 canonical Bible versions, 8 commentary sources, crossrefs, interlinear, plans, library docs, manifest shortcuts, and nav hrefs. This pass checked the new apocrypha data layer (`data/bible-apocrypha/`, `apocrypha-books.json`, `apocrypha-canon-orders.json`) and JS fetch paths in `apocrypha-reader.js`, `terms.js`, `places.js`.*

---

### DATA-3 · BRENTON version missing scope correction and 3 canonical OT books *(MEDIUM)*

**Problem:** `data/versions/versions.json` declares `BRENTON` with `"scope": "full-bible"` and `"canon_order": "lxx"`. The `lxx` canon order in `apocrypha-canon-orders.json` lists 83 books (66 canonical + 17 deuterocanonical). However, `data/bible-apocrypha/BRENTON/` only has 51 files — the Brenton LXX is an Old Testament translation only with no NT content. The apocrypha reader uses `_isFullBible()` (`scope === 'full-bible'`) to decide whether to show NT navigation, so on BRENTON all 27 NT books appear in the book list but every one 404s when clicked. Additionally, 3 canonical OT books are missing from the BRENTON directory: `esther` (only `additions-esther.json` present — the Greek Esther with additions is there, but `esther.json` for the base canonical MT-mapped form is absent), `daniel` (LXX Daniel includes additions but no `daniel.json` base file), and `nahum` (no equivalent in the BRENTON directory — genuinely missing).

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

## Mobile Responsiveness Audit — Dimension 3, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (CSS-1–6) addressed word.css height clipping, hamburger/discipline/reader touch targets, study-nav font-size, and reader keyboard hint visibility. This pass examined lib-browser.css, verse-study.css, memorize.css, maps.css, and timelapse.css. Two new issues found.*

---

### CSS-11 · lib-browser.css — Mobile tab bar sub-WCAG font-size and touch target *(MEDIUM)* *(agent: in-progress)*

**Problem:** In `lib-browser.css` `@media (max-width: 600px)` (line 859), `.lb-tab-btn` has `font-size: .72rem` (11.52px at 16px base — WCAG AA body minimum is 14px) and `padding: .55rem .25rem` with no `min-height`. Computed button height is approximately 30–32px — below the WCAG 2.5.5 minimum of 44px. These tab buttons are the primary navigation for the entire Library browser on mobile: Browse / Authors / List / Read. A user on a 375px screen cannot reliably tap the correct tab or read the labels without zooming. This also affects the `lb-tab-btn--active` state which inherits the same dimensions.

**Fix:**
- `assets/css/lib-browser.css` (`.lb-tab-btn` in `@media (max-width: 600px)`, line 860): Change `font-size: .72rem` → `font-size: .82rem`. Add `min-height: 44px; display: flex; align-items: center; justify-content: center;` to guarantee a 44px tap height.

**Verify:** At 375px viewport width, all four Library browser tab buttons (Browse / Authors / List / Read) should be visually ≥44px tall and the label text readable without pinch-zoom.

---

### CSS-12 · verse-study.css — Section collapse toggle button has no mobile touch target *(LOW)*

**Problem:** In `verse-study.css` (line 869), `.vs-section-toggle` (the ▾/▴ button that collapses/expands each verse study section, added in VS-C) has `font-size: 0.72rem`, `padding: 0 0.2rem`, and no `min-height`. On mobile the button renders at roughly 14–16px × 20px — well below the 44px WCAG tap target. It sits adjacent to the section heading, so mis-taps scroll the page or activate the wrong element. No `@media (max-width: ...)` override exists for this element in the existing mobile touch-targets block (line 926).

**Fix:**
- `assets/css/verse-study.css` (`.vs-section-toggle` mobile rule, add inside existing `@media (max-width: 640px)` block at line 926): Add `.vs-section-toggle { min-height: 44px; padding: 0 0.5rem; display: inline-flex; align-items: center; }` to bring it to the WCAG tap minimum without affecting its desktop appearance.

**Verify:** On a 375px viewport in the verse study page, tap the ▾ button on any section heading — it should be easy to tap without hitting adjacent text. Section collapses correctly.

---

## Empty State & Loading State Audit — Dimension 2, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (UX-1–5) addressed search.js, verse-study.js interlinear, discipline plans, library secondary sources, and history iframe tabs. This pass found two remaining missing `.catch()` patterns in verse-study.js.*

---

### UX-6 · verse-study.js — Commentary stuck on "Loading commentary…" after source-switch network failure *(MEDIUM)* *(agent: in-progress)*

**Problem:** In `verse-study.js`, the inner `vsLoadComm` function (line 752) sets `commSec.bodyEl.innerHTML` to `'<p class="bsw-modal__loading">Loading commentary…</p>'` before the fetch, but has no `.catch()` handler. On initial page load this is harmless — the commentary section stays hidden if the fetch fails. However, once the section has been successfully shown and the user switches the commentary source picker, the section is already visible. If the new fetch fails (offline, source unavailable), `commSec.bodyEl.innerHTML` is left permanently showing "Loading commentary…" with no way to dismiss or retry. This is the same pattern that UX-2 fixed for the interlinear section.

**Fix:**
- `verse-study.js` (`vsLoadComm`, line ~785): Add `.catch(function () { commSec.bodyEl.innerHTML = '<p class="bsw-modal__commentary-empty">Could not load commentary. Check your connection.</p>'; })` after the `.then()` block.

**Verify:** In the verse study page with a commentary source loaded, disable the network (DevTools → Network → Offline), then switch to a different commentary source — the "Loading commentary…" message should be replaced with a "Could not load" error, not stay stuck.

---

### UX-7 · verse-study.js — Cross-reference and parallels sections leave hidden orphan DOM nodes on fetch failure *(LOW)* *(agent: in-progress)*

**Problem:** In `verse-study.js`, both `xrefSec` (line 741, `loadCrossRefs`) and `parSec` (line 807, `loadParallels`) have no `.catch()` handler. On network failure both sections remain as invisible orphan DOM elements (created but never made visible and never removed). `vsRebuildNav()` correctly excludes hidden sections from the sidebar, so the user sees nothing wrong. However, the orphan nodes are a resource/memory inconsistency and mask the real cause of absent sections — a user on a slow connection cannot distinguish "no data for this verse" from "fetch failed." The same fix pattern was applied to `interlinearSec` in UX-2.

**Fix:**
- `verse-study.js` (xref section, line ~747): Add `.catch(function () { xrefSec.el.remove(); vsRebuildNav(); })` after the loadCrossRefs `.then()`.
- `verse-study.js` (parallels section, line ~813): Add `.catch(function () { parSec.el.remove(); vsRebuildNav(); })` after the loadParallels `.then()`.

**Verify:** In the verse study page with DevTools → Network → Offline, load a verse — the cross-references and parallels sections should be absent (removed), not silently orphaned in the DOM (confirm via DevTools Elements that no hidden `.vs-xrefs` or `.vs-parallels` elements remain).

---

## Code Comment Audit — Dimension 1, Cycle 2

*Audit pass 2026-06-05 (cycle 2). First cycle (CODE-1–8) addressed the most obvious gaps. This pass found two areas still missing required structured comments: three complex algorithms in wire.js added after the first-pass fixes, and the window.BibleUI cross-module coupling in app.js.*

---

### CODE-9 · wire.js — autoTagChapterRefs, autoTagBareRefs, autoTagBareChapters lacking INTENT/CHANGE?/VERIFY *(MEDIUM)*

**Problem:** Five exported functions in `wire.js` are still missing required structured comments after the first-pass fix (which addressed `autoTagRefs`, `updateInlineVerses`, and `applyHighlights`). `autoTagChapterRefs` (line 203), `autoTagBareRefs` (line 285), and `autoTagBareChapters` (line 360) are complex TreeWalker algorithms with no `INTENT`, `CHANGE?`, or `VERIFY` at all. `applyModalHighlights` (line 480) uses a different CSS class prefix (`bsw-hl-`) than `applyHighlights` (`reader-verse--hl-`), but has no `CHANGE?` documenting that divergence or listing its callers. `applyBookmarks` (line 497) writes DOM state from localStorage bookmarks but has no `CHANGE?` noting which callers in `reader.js` must stay in sync.

**Fix:**
- `wire.js` (`autoTagChapterRefs`, line 203): Add INTENT (same TreeWalker/SKIP-set pattern as autoTagRefs; tags "Book Ch" and "Book Ch–Ch" whole-chapter patterns, excluding tokens followed by `:digit`) + CHANGE? (if bookLookup/metaBooks structure changes or the SKIP set diverges from autoTagRefs, both functions break silently; autoTagRefs calls this at its end) + VERIFY (open a topic page with plain "Romans 5–8" text; after load it should become a clickable whole-chapter ref).
- `wire.js` (`autoTagBareRefs`, line 285): Add INTENT (bare "Ch:V" patterns on book-specific pages; only invoked when body has `data-bible-book`; bookId and bookName supplied by autoTagRefs) + CHANGE? (if data-bible-book handling in autoTagRefs changes, this function stops being called; also called nowhere else) + VERIFY.
- `wire.js` (`autoTagBareChapters`, line 360): Add INTENT ("Chap. 3" / "ch. 3" / "chapter 3" patterns on book-specific pages; called in sequence after autoTagBareRefs from autoTagRefs) + CHANGE? + VERIFY.
- `wire.js` (`applyModalHighlights`, line 480): Add CHANGE? noting the CSS class prefix split: this function applies `bsw-hl-{colour}` to `.bsw-modal__verse` elements; `applyHighlights` applies `reader-verse--hl-{colour}` to `.reader-verse` elements — they must not be swapped; callers are `modal.js:_renderModalVerseTab` and `modal.js:_switchTab`.
- `wire.js` (`applyBookmarks`, line 497): Add CHANGE? listing callers: `reader.js:doLookup` and `reader.js:injectComparePanel`; if `isBookmarked()` schema in `storage.js` changes or the `reader-verse__num--bookmarked` class name is renamed, both call sites silently show no bookmark state.

**Verify:** Open the reader at a chapter with a bookmarked verse; confirm the bookmark star renders. Open a book-specific topic page (e.g. `topics/gospel-of-john/`) and verify "3:16" and "Chap. 1" are auto-tagged as clickable ref links.

---

### CODE-10 · app.js — window.BibleUI cross-module coupling lacks CHANGE? *(MEDIUM)*

**Problem:** `app.js` line 102 declares `window.BibleUI` — the site's only intentional window-level global, depended on by non-module inline scripts on topic pages and by `ol-companion.js`. Per CLAUDE.md rules, any `window.*` cross-module coupling requires `// CHANGE?` noting downstream callers. Currently the object has a one-line prose comment ("the only intentional global") but no structured `CHANGE?` listing which pages use each key, and no `VERIFY`. The nested `openReader` closure (lines 110–115) also has no `INTENT`, despite a non-obvious `bookId → display name` resolution step that silently falls back to the raw ID string if `metaBooks` isn't loaded. Removing or renaming any `window.BibleUI` key without updating inline scripts fails completely silently.

**Fix:**
- `app.js` (`window.BibleUI`, line 102): Add `// CHANGE?` listing consumers: topic-page inline scripts call `BibleUI.openModal()` and `BibleUI.autoTagPlacesIn()`; `ol-companion.js` calls `BibleUI.initOLSection()`; `timeline.js` calls `BibleUI.autoTagPlacesIn()` after dynamic renders; removing any key with no replacement silently breaks the relevant pages. Also add `// VERIFY`: from a topic page DevTools console, confirm `window.BibleUI.openModal` is a function and calling it opens the verse modal.
- `app.js` (`openReader`, line 110): Add `// INTENT:` explaining the bookId → name resolution step (callers on topic pages pass an ID like `"genesis"` not the display name `"Genesis"`; falls back to bookId string if metaBooks isn't ready, which produces a broken reader URL).

**Verify:** From a topic page console, call `window.BibleUI.openReader('john', 3, 16)` — confirm the reader navigates to John 3:16. Confirm `window.BibleUI.openModal` is callable with a `{bookId, ch, v}` parsed object.
