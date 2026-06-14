# Bible Study Website — Looping Projects

Long-term agent loop tasks. Each entry tracks a multi-session agent corpus job.
Mark `[x]` only when the **entire** loop is complete.

To add a new looping project, see `working/todo-workflow.md` → "How to Add a Looping Project".

---

### Paragraph Annotation Upgrade (PARA2 loop)

*Upgrades existing `data/paragraphs/{bookId}.json` (already complete for 66 books) with per-break speaker attribution, compound type flags, and thought breaks. Rendering engine (JS + CSS) is already built. Loop agents work book by book on the data annotation pass.*

| File | Purpose |
|---|---|
| `PARA2_AGENT_PROMPT.md` | Paste prompt for each agent session |
| `PARA2_AGENT_GUIDE.md` | Schema reference, speaker vocabulary, annotation rules |
| `PARA2_PROGRESS.md` | Work queue — 38 books with dialogue breaks; phased by priority |

- [ ] **PARA2-Phase1** — Gospels + Acts (John, Matthew, Mark, Luke, Acts — 5 books, ~149 dialogue breaks)
- [ ] **PARA2-Phase2** — OT Narrative Dialogues (Job, Daniel, Chronicles, Samuel, etc.)
- [ ] **PARA2-Phase3** — OT Prophets (oracle type upgrades, Ezekiel, Jeremiah, Amos, etc.)
- [ ] **PARA2-Phase4** — NT Epistles, Wisdom, Revelation

---

### Paragraph Structure Data (PARA loop)

*Agent generates `data/paragraphs/{bookId}.json` for all 66 books — paragraph breaks, section types (narrative/poetry/dialogue/list/doxology), and section headings per chapter. Used by the reader's Print Mode to reformat verses into proper literary structure.*

| File | Purpose |
|---|---|
| `PARA_AGENT_PROMPT.md` | Paste prompt for each agent session |
| `PARA_QUEUE.md` | Work queue — 66 books (long books split into ~25-ch rows); claim → complete |

- [ ] **PARA-NT** — Complete all 27 NT books (~27 work units)
- [ ] **PARA-OT** — Complete all 39 OT books (~57 work units after long-book splits)

---

### Wide Source Commentary (WS loop)

*Agent writes per-verse synthesis from Calvin, Matthew Henry, Ellicott, JFB, Clarke, Wesley, Barnes for every verse of every book. Priority order: Hebrews → Romans → Galatians → Ephesians → 1 John → NT → OT.*

| File | Purpose |
|---|---|
| `WS_AGENT_PROMPT.md` | Paste prompt for each agent session |
| `WS_AGENT_GUIDE.md` | Content rules, synthesis principles, source weighting |
| `WS_SCRIPT_GUIDE.md` | Script boilerplate, JSON output format, merge safety |
| `WS_PROGRESS.md` | Work queue — one row per book/chapter unit; claim → complete |

- [ ] **WS-NT Phase 1** — Complete Hebrews, Romans, Galatians, Ephesians, 1 John (~40 script units)
- [ ] **WS-NT Phase 2** — Complete John, Luke, Acts, remaining NT epistles (~120 script units)
- [ ] **WS-OT Phase 1** — Complete Genesis, Psalms, Isaiah (~90 script units)
- [ ] **WS-OT Phase 2** — Remaining OT books (~350 script units)

---

### MKT Commentary Suite (Z6–Z8 loop)

*Agent generates three verse-by-verse original commentaries per book: Original Language, Historical Context, and Christ in Every Verse. Script pattern: `zc-{type}-{book}-{start}-{end}.py`. NT first.*

| File | Purpose |
|---|---|
| `Z_AGENT_PROMPT.md` | Paste prompt for each agent session |
| `Z_COMMENTARY_AGENT_GUIDE.md` | Content principles and length targets for all three commentary types |
| `Z_COMMENTARY_SCRIPT_GUIDE.md` | Script boilerplate, HTML conventions, source data checklist |
| `Z_PROGRESS.md` | Work queue — 66 books × 3 commentary types + echo layer; claim → complete |

- [ ] **Z6 mkt-original** — All 66 books via `zc-original-*.py` (NT first: John + Romans)
- [ ] **Z7 mkt-context** — All 66 books via `zc-context-*.py` (NT first)
- [ ] **Z8 mkt-christ** — All 66 books via `zc-christ-*.py` (NT first)

---

### MKT Translation (Phase Z loop)

*Ongoing modern-language Bible translation loop. Produces three translation tiers (literal, mediating, thought-for-thought) plus translator notes per verse. NT continuation in progress.*

| File | Purpose |
|---|---|
| `MKT_AGENT_PROMPT.md` | Paste prompt for each translation session |
| `TRANSLATION_AGENT_GUIDE.md` | Translation philosophy, tier definitions, disputed-term handling |
| `MKT_STATIC_SCRIPT_GUIDE.md` | Script boilerplate, output schema, safety notes |
| `MKT_PROGRESS.md` | Work queue — tracks each book/chapter unit across all three tiers |

- [ ] **MKT NT continuation** — Remaining NT books (see `MKT_PROGRESS.md` for current position)
- [ ] **MKT OT** — Full OT translation (deferred until NT complete)

---

### Book Study Data (BS loop)

*Agent generates `data/workshop/book-study/{bookId}.json` for all 66 books — authorship, outline, themes, key passages, key vocabulary, christological reading, reception. Infrastructure items SW-V1–V4 must be built first.*

| File | Purpose |
|---|---|
| `BS_AGENT_PROMPT.md` | Paste prompt for each agent session |
| `BS_AGENT_GUIDE.md` | Content rules, depth targets, schema field guidance |
| `BS_SCRIPT_GUIDE.md` | Script boilerplate, JSON output schema, idempotency rules |
| `BS_PROGRESS.md` | Work queue — 66-row table, one row per book, 8 schema columns |

- [ ] **BS infrastructure** — Complete SW-V1–V4 first (schema, script template, agent prompt, progress tracker)
- [ ] **BS loop** — Generate book-study JSON for all 66 books (~66 script units)

---

### Verse Auditor (VA loop)

*Agent wraps plain-text scripture references in `<a class="ref" data-ref="...">` tags across all library HTML files and study pages. Idempotent — safe to re-run on already-tagged files.*

| File | Purpose |
|---|---|
| `VA_AGENT_PROMPT.md` | Paste prompt for each agent session |
| `VA_GUIDE.md` | Rule catalogue (R1–R7), context resolution, edge cases, double-wrap guard |
| `VA_PROGRESS.md` | Work queue — one row per HTML file; claim → complete |

- [ ] **VA loop** — Tag all remaining unprocessed library and study HTML files (see `VA_PROGRESS.md`)

---

### WS-G Semantic Range Curation (agent pass)

*Agent reads all lexical sources + attested uses and writes a curated 2–3 sentence `semantic_range` synthesis for top-100 disputed/high-use terms. Prerequisite: WS-A–F complete (done). Uses existing WS infrastructure.*

| File | Purpose |
|---|---|
| `WS_AGENT_PROMPT.md` | Base prompt — extend with WS-G semantic-range curation instructions |
| `WS_AGENT_GUIDE.md` | Source weighting rules applicable to range curation |

- [ ] **WS-G Greek** — Curate `semantic_range` for all Phase 1 Greek entries (200 entries)
- [ ] **WS-G Hebrew** — Curate `semantic_range` for all Phase 2 Hebrew entries (200 entries)
- [ ] **WS-G Phase 5** — Curate `semantic_range` for Phase 5 contested terms (17 entries — highest priority)

---

### Source Data Pipelines (SW-Q8–Q10)

*Build scripts that populate `attested_uses`, `lxx_bridge`, and `extrabiblical_uses` across the full workshop glossary. Each is a long-running data-generation pass over ~200–400 entries. No dedicated agent prompt files yet — scripts drive these.*

- [ ] **SW-Q8** — `attested_uses` pipeline: 3–5 verse samples per word from interlinear data (~400 entries)
- [ ] **SW-Q9** — `lxx_bridge` expansion: populate 187 remaining Hebrew entries from LXX mapping
- [ ] **SW-Q10** — `extrabiblical_uses` pipeline: top-50 Greek NT words from Moulton–Milligan or equivalent

---

### Pre-build Scripts (SW-U3/U4)

*One-time large data-generation scripts. Listed here because they block word-study features and each needs a dedicated run session. Output files are ~15MB each.*

- [ ] **SW-U3** — `scripts/build-translation-variants.py` → `data/grammar/translation-variants-greek/hebrew.json`
- [ ] **SW-U4** — `scripts/build-strongs-concordance.py` → `data/grammar/concordance-greek/hebrew.json` (~15MB each)

*Planned 2026-06-07. Three tiers per book: Book Guide (orientation + study questions), Deep Dive (scholarly analysis), Wide Source Commentary (per-verse synthesis from classic commentators). Replaces the unsustainable flat nav approach with a Studies hub page. See plan at `.claude/plans/i-want-you-to-mellow-ritchie.md` for full architecture.*

### Phase A — Foundation (no visible user changes)

- [x] **TRB-A1 `data/books-content.json`** — Create master content manifest for all 66 books. Each entry has `guide`, `deep_dive`, `commentary` with `exists` flag, `url`, and for commentary: `coverage`, `chapters_done`, `chapters_total`. Seed current state: revelation/romans/sermon-on-the-mount/psalms `deep_dive.exists=true`; study-guides/hebrews, ephesians, etc. `guide.exists=true`; all commentary `exists=false`. Also include `topical` array for non-book topic pages (prayer, justification, etc.).

- [x] **TRB-A2 `studies/index.html`** — New Studies hub page. JS-rendered from `data/books-content.json`. Organized by testament (OT/NT) → book. Each book row/card shows which tiers exist as pill badges (Guide / Deep Dive / Commentary — greyed if not built). Filter bar: Testament, Genre, "Has content" toggle. Topical articles get a separate section below. This replaces `topics/index.html` as the content discovery surface.

- [x] **TRB-A3 Update `main.js` sidebar** — Remove Library subgroup items (Bible Book Overviews, Study Guides, Topical Articles) and their individual entries. Replace with single `📚 Studies` → `/studies/` link. Add `_bookContent` fetch from `data/books-content.json` alongside `topics.json`. Rebuild `BOOK_STUDIES` map from `_bookContent` instead of `topics.json`. Add `getBannerItems(bookId, ch, v, bookContent)` function for tier-aware reader banner logic.

- [x] **TRB-A4 `.bk-tier-nav` CSS** — Add tier navigation strip component to `assets/css/book-study.css`. Sticky top bar, uses `--bk-accent` for active tab indicator. Active state driven by `[data-tier=X] [data-tier-item=X]` CSS selector (no JS needed). `[hidden]` on `<li>` suppresses missing tiers.

### Phase B — Retrofit Existing Pages

- [x] **TRB-B1 Migrate `topics/revelation/index.html`** — Copy current page to `topics/revelation/deep-dive.html`. Replace `index.html` with a new slim Book Guide (using `_template-book`). Add tier nav strip to both pages. Update `data/books-content.json` entry.

- [x] **TRB-B2 Migrate `topics/romans/index.html`** — Same pattern. New `index.html` Book Guide. Current page → `deep-dive.html`. Tier nav strip on both. Guide link in strip → `study-guides/romans-1-8/` (partial, note chs 1–8).

- [x] **TRB-B3 Migrate `topics/sermon-on-the-mount/index.html` and `topics/psalms/index.html`** — Same pattern as B1/B2.

- [x] **TRB-B4 Add tier strips to existing study guides** — Add the `bk-tier-nav` HTML (lighter variant: Guide active, Deep Dive link if exists, ← All Studies) to `study-guides/hebrews/`, `study-guides/ephesians/`, `study-guides/romans-1-8/`, `study-guides/sermon-on-the-mount/`, `study-guides/psalms/`.

- [x] **TRB-B5 Deprecate `topics/index.html`** — Add `<meta http-equiv="refresh" content="0;url=/studies/">` redirect. Update any hardcoded links to `topics/index.html` that exist in the codebase.

### Phase C — First Synthesis Commentary (WS loop)

- [x] **TRB-C1 WS infrastructure** — *(Done)* `WS_PROGRESS.md`, `WS_AGENT_GUIDE.md`, `WS_SCRIPT_GUIDE.md`, `WS_AGENT_PROMPT.md` created 2026-06-07.

- [ ] **TRB-C2 Proof-of-concept: Hebrews 1–4** — Run `WS_AGENT_PROMPT.md` loop for first unit (`ws-synthesis-hebrews-1-4.py`). Verify `data/commentary/synthesis/hebrews.json` chapters 1–4 fully covered.

- [ ] **TRB-C3 `topics/hebrews/commentary.html`** — Create Tier 3 display page for Hebrews. Loads `data/commentary/synthesis/hebrews.json` lazily by chapter. Each verse entry renders `synthesis` paragraph above a `<details>` element for the `voices` array. Add tier nav strip (Commentary active, Guide → `study-guides/hebrews/`, Deep Dive greyed until TRB-D1).

- [ ] **TRB-C4 Register `synthesis` in `core.js`** — Add `{ id: 'synthesis', label: 'Classic Voices (Synthesis)', attr: 'Synthesis of Calvin, Matthew Henry, Ellicott, JFB, Clarke, and Wesley' }` to `COMMENTARY_SOURCES`. Add branch in reader's commentary render: when `source === 'synthesis'`, render `entry.synthesis` as displayed HTML and append `<details>` for `entry.voices`.

- [ ] **TRB-C5 Update `books-content.json` for Hebrews commentary** — Set `hebrews.commentary.exists=true`, `coverage="partial"`, `chapters_done=[1,2,3,4]`. Verify reader banner shows commentary link when navigating Hebrews chapters 1–4.

### Phase D — First New Deep Dive (Hebrews)

- [x] **TRB-D1 `topics/_template-book/deep-dive.html`** — Create Deep Dive template. Structure: sticky sidebar nav with section links, chapter accordions (`<details>`), tabs for interpretive schools (if applicable), key term tables, canonical connections section. Based on current `topics/revelation/index.html` design language.

- [x] **TRB-D2 `topics/hebrews/deep-dive.html`** — Create Deep Dive for Hebrews using the new template. Content: authorship/date/audience, the argument of Hebrews (Christological superiority), key OT typological connections (Melchizedek, tabernacle, Day of Atonement), chapter-by-chapter breakdown, five warning passages, key terms (κρείττων, ἀρχιερεύς, τελειόω, etc.). Update `books-content.json`.

---

## Wide Source Commentary — Agent Loop (WS)

*Infrastructure created 2026-06-07. Loop agent writes per-verse synthesis from Calvin, Matthew Henry, Ellicott, JFB, Clarke, Wesley, Barnes. See `WS_AGENT_PROMPT.md` to start.*

**Priority order:** Hebrews → Romans → Galatians → Ephesians → 1 John → John → Luke → Acts → remaining NT → OT (Genesis, Psalms, Isaiah first)

**Tracker:** `WS_PROGRESS.md`

- [ ] **WS-NT Phase 1** — Complete Hebrews, Romans, Galatians, Ephesians, 1 John (5 books, ~40 script units)
- [ ] **WS-NT Phase 2** — Complete John, Luke, Acts, remaining NT epistles (22 books, ~120 script units)
- [ ] **WS-OT Phase 1** — Complete Genesis, Psalms, Isaiah (3 books, ~90 script units)
- [ ] **WS-OT Phase 2** — Remaining OT books (36 books, ~350 script units)

---

## Workshop — Book Study Data Process (SW-V)

*Book Study is data-light. Define a world-class schema and a repeatable agent script loop to fill all 66 books.*

### Schema

- [ ] **SW-V1 Define `data/workshop/book-study/{bookId}.json` schema** — Each file contains:
  ```json
  {
    "bookId": "romans",
    "author": "Paul (c. AD 57)",
    "date_written": "c. AD 57",
    "occasion": "...",
    "audience": "...",
    "provenance": "Corinth",
    "outline": [
      { "label": "Greeting & Theme", "ref": "Rom 1:1-17", "summary": "..." },
      ...
    ],
    "themes": [
      { "title": "Justification by Faith", "refs": ["Rom 1:17", "Rom 3:21-26"], "body": "2–3 paragraph treatment" },
      ...
    ],
    "key_passages": [
      { "ref": "Rom 3:21-26", "title": "The Heart of the Gospel", "why": "..." }
    ],
    "key_vocabulary": [
      { "code": "G1343", "lemma": "δικαιοσύνη", "gloss": "righteousness", "significance": "..." }
    ],
    "literary_structure": "...",
    "christological_reading": "...",
    "redemptive_historical_place": "...",
    "reception_highlights": "Brief — key interpreters (Augustine, Luther, Barth) and their distinctive reading"
  }
  ```
- [ ] **SW-V2 Build script template** — `scripts/build-book-study-{bookId}.py` pattern: reads existing `data/cultural/book-context.json` entry for the book, reads `data/literary/genre.json` entry, reads available synthesis data, and calls a structured prompt to generate the full schema above. Output written to `data/workshop/book-study/{bookId}.json`. Script is safe to re-run (won't overwrite fields already populated).
- [ ] **SW-V3 Agent prompt file** — `BS_AGENT_PROMPT.md` at repo root: 6-step paste prompt (claim book → read existing data → write → run script → verify JSON → update `BS_PROGRESS.md`). Mirrors Z_AGENT_PROMPT.md pattern.
- [ ] **SW-V4 Progress tracker** — `BS_PROGRESS.md` at repo root: 66-row table, one row per book, 8 columns (author · date · outline · themes · key_passages · key_vocab · christological · reception). Mark complete as each is generated.
- [x] **SW-V5 UI — Book Study renders new schema** — `_loadBookStudyData(bookId)` fetches `data/workshop/book-study/{bookId}.json`. `_renderBookStudy` shows Vocabulary/Language/Reception/Reading Guide tabs when data exists. `_renderBookVocabTab` renders key_vocabulary as expandable rows clicking through to Word Study.

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
- [x] Audited data/parallels/: 1037 entries across 54 books; types: parallel(243) quotation(135) fulfillment(183) allusion(79) prophecy-source(183) allusion-source(79) quotation-source(135)
- [x] scripts/absorb-parallels.py written and run: 746 OT-NT entries absorbed into 50 echo files; synoptic parallels skipped (COMPLETE)
- [x] note field generated from parallels label field in absorb-parallels.py (COMPLETE)
- [x] Absorption documented via script comments in scripts/absorb-parallels.py; Z_COMMENTARY_SCRIPT_GUIDE.md update deferred (COMPLETE)

**Build:**
- [x] Echo files complete for all 66 books; absorption complete; no new script units needed (COMPLETE)
- [x] core.js: ECHOES_ROOT + loadEchoes() + echoesCache already implemented; 66 echo files in data/echoes/ (COMPLETE)
- [x] verse-study.js: vsExtractEchoes + vsRenderEchoList + "Echoes & Fulfillments" section already implemented (COMPLETE)
- [x] reader.js: parallels panel is the B5 parallel-passage reader (different feature, not echoes); echoes are verse-study-only (COMPLETE)
- [x] data/echoes/: 66 book files already exist (COMPLETE)

Echo types: `quote` | `allusion` | `type` | `shadow` | `theme` | `fulfillment`