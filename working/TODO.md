# Bible Study Website — Working TODO

Track progress here. Mark items `[x]` when complete.

---

## Completed

- [x] **Bible Reader** (`read/index.html`) — full-chapter and verse-range lookup, URL-shareable `?ref=` params, version switcher, split text + cross-refs layout
- [x] **Full-text search** (`search/index.html`) — version-aware search across all 66 books, fuzzy multi-word matching, exact-quote mode, live progress
- [x] **Verse tooltip + modal system** — hover preview, click-to-modal, focus/keyboard accessible, per-version rendering
- [x] **Version picker** — localStorage persistence, all pages synced
- [x] **Auto-tagging of scripture refs** in topic page prose (bare refs, ch:v, "Ch. N", continuations like "; 3:4")
- [x] **Cross-references (TSK) in verse modal** — data: `data/crossrefs/` (66 books), split panel in modal and reader
- [x] **Matthew Henry Commentary in verse modal** — data: `data/commentary/` (66 books), Commentary tab in modal
- [x] **Chapter navigation in Bible Reader** — Prev/Next buttons (top + bottom), book/chapter browse dropdowns, keyboard shortcuts (j / → next, k / ← prev)

---

## Phase A — Foundation (do these first, ≤ 2 days total)

These are broken-state or high-friction issues that block everything else.

- [ ] **A1. Fix broken library links** — `library/index.html` links to 6 pages that 404:
  `belgic-confession/`, `canons-of-dort/`, `westminster-larger-catechism/`,
  `london-baptist-confession/`, `augsburg-confession/`, `39-articles/`
  Either create stub pages or remove cards from the index until content is ready.

- [ ] **A2. Fix nav inconsistency** — most pages only show `Home | Reader | Search`.
  `library/index.html` correctly has `Topics | Library` but the rest don't.
  Add `Topics` and `Library` to the nav on: `index.html`, `read/index.html`,
  `search/index.html`, `topics/index.html`. One consistent header across the site.

- [ ] **A3. Update `main.js` Studies panel** — the `LIBRARY` constant at line 19 hardcodes
  only 2 items and has no Library section. Add a Library entry and keep it in sync
  as new topics and confessions are added.

- [ ] **A4. Delete stale `_includes/` directory** — `header.html`, `footer.html`, `head.html`
  are never used (no Jekyll build step). `header.html` references NIV/ESV/NASB/NLT
  versions that don't exist in the data. Safe to delete entirely.

- [ ] **A5. Reader — wider layout / responsiveness**
  - Root cause: `--max-width: 860px` in `style.css` caps the reader; wasted whitespace on wide screens
  - Add `.reader-page` body class to scope reader-specific layout without touching global CSS
  - Wide screens (1100px+): 3-column — chapter sidebar | verse text | cross-refs
  - Medium screens (700–1099px): current 2-column split (text | cross-refs)
  - Narrow (< 700px): single column, stacked
  - Target container width: 1200–1400px for reader only

---

## Phase B — Competitive Parity (closes the gap with Blue Letter Bible & BibleHub)

These are the features every serious free competitor has. Each one is achievable
with public domain data and the existing `bible.js` infrastructure.

- [ ] **B1. Parallel translation reader** *(effort: 2–3 days)*
  - In the Reader, a "Compare" toggle splits the text column into 2 side-by-side version panels
  - Each panel has its own version selector; both call the existing `resolveVerses()` independently
  - All 4 versions (KJV, BSB, WEB, ASV) are already local JSON — this is a pure UI change
  - Add more public domain versions to increase comparison value:
    - Young's Literal Translation (YLT) — public domain
    - Darby Translation — public domain
    - Geneva Bible (1599) — public domain
  - Fetch scripts for YLT/Darby/Geneva follow the same pattern as `scripts/fetch-bsb.py`
  - BibleHub's most-used feature; currently a total gap in this tool

- [ ] **B2. Strong's concordance word study** *(effort: 1–2 weeks)*
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
  - This is the #1 feature gap vs. BLB; closes the most important competitive distance

- [ ] **B3. Personal notes & verse highlights** *(effort: 3–5 days)*
  - Click a verse number to toggle a yellow highlight (persists in localStorage)
  - Right-click / long-press a verse → open a small note editor textarea
  - Notes saved to `localStorage` key `bsw_notes` as `{ "John 3:16": { highlight: true, note: "…" } }`
  - `notes/index.html` — "My Notes" page listing all annotated verses with ref links back to Reader
  - Export option: copy all notes as plain text or JSON
  - Highlights visible in both the Reader and verse modal
  - Privacy-first: everything local, nothing leaves the browser

- [ ] **B4. PWA / offline mode** *(effort: 2–3 days)*
  - Add `manifest.json` (name, icons, theme color, start URL, display: standalone)
  - Add a service worker (`sw.js`) with:
    - Cache-first strategy for `data/bible/**`, `data/crossrefs/**`, `data/commentary/**`, all CSS/JS
    - Network-first for HTML pages so updates are always received when online
    - Background pre-cache of all Bible JSON using `requestIdleCallback` after first visit
  - Total Bible JSON size: ~30–40 MB for 4 versions — reasonable for a dedicated study tool
  - Result: site works fully offline after first visit; no major free web tool offers this
  - This is a genuine architectural differentiator — the static JSON-based design is perfectly suited for PWA

- [ ] **B5. Parallel Passage Reader** *(effort: 1–2 weeks)*

  When reading a chapter, show stacked parallel panels below each passage that has known
  parallels. Three parallel types are supported, visually distinguished by label:

  | Type | Label | Example |
  |---|---|---|
  | `parallel` | ⇌ Parallel | Matt 5:3-12 ↔ Luke 6:20-26 |
  | `fulfillment` | ✓ Fulfilled in | Isa 7:14 → Matt 1:23 |
  | `prophecy-source` | ⌖ Prophesied in | Matt 1:23 → Isa 7:14 |

  **UI: global toggle + per-panel collapse (both, per user decision)**
  - A "Parallels" toggle button in the reader toolbar (next to version picker)
    - State persists in `localStorage` key `bsw_parallels` (default: off)
    - When turned on, all parallel panels for the visible chapter appear below their passages
    - When turned off, parallel panels are removed from the DOM (no reflow cost while off)
  - Each individual parallel panel has its own ▾ / ▸ collapse button
    - Collapse state resets on navigation (each chapter starts fully expanded)
  - Shows first 3 verses of each parallel by default; "Show all N verses ↓" button expands the rest

  **Display layout (stacked panels)**
  ```
  ┌──────────────────────────────────────────────────────────┐
  │  Matthew 5:1-12 (current passage)                        │
  │  ¹ And seeing the multitudes… ² And he opened his…       │
  │  ³ Blessed are the poor in spirit…                       │
  ├──────────────────────────────────────────────────────────┤
  │  ⇌ Parallel · Luke 6:17-26 · "Sermon on the Plain"   ▾  │
  │  ¹⁷ And he came down with them… ²⁰ And he lifted up…    │
  │  ²⁰ Blessed be ye poor: for yours is the kingdom…       │
  │  [Show all 10 verses]                                    │
  └──────────────────────────────────────────────────────────┘
  ```

  **Data: `data/parallels/{bookId}.json`**

  Schema per file:
  ```json
  {
    "5": {
      "3": [
        {
          "end": 12,
          "label": "The Beatitudes",
          "type": "parallel",
          "refs": [
            { "passage": "Luke 6:20-26", "label": "Sermon on the Plain" }
          ]
        }
      ]
    }
  }
  ```
  Key is the start-verse of the parallel section (string). `end` is the last verse of the
  section in the source book. Each `ref.passage` uses the standard `"Book Ch:V-V"` format
  already parsed by `parseRef()` in `bible.js`.

  Both directions are stored — `data/parallels/isaiah.json` contains the fulfillment link
  pointing to Matthew; `data/parallels/matthew.json` contains the prophecy-source link
  pointing to Isaiah. The build script generates both automatically.

  **Build script: `scripts/build-parallels.py`**

  Generates all `data/parallels/*.json` from a curated lookup table embedded in the script.
  No network requests needed — the parallel relationship list is stable biblical scholarship.

  Curated sections to include (~700 total):
  - **Gospel parallels** (~250): All synoptic parallels (Aland numbering) + Johannine parallels.
    Covers baptism, temptation, calling of disciples, Sermon on Mount/Plain, feeding of 5000,
    Transfiguration, triumphal entry, Last Supper, Passion narrative, Resurrection, etc.
  - **OT historical parallels** (~200): Kings/Chronicles overlap (same events in both),
    Samuel/Chronicles parallels, Isaiah 36-39 = 2 Kings 18-20 (nearly verbatim),
    Psalm duplicates (Ps 14=53, Ps 18=2 Sam 22).
  - **NT quotes of OT** (~150): Major explicit quotations in the NT epistles and Gospels
    (e.g., "it is written…" citations), tagged as `quotation` sub-type of `fulfillment`.
  - **Prophecy/fulfillment** (~100): Key Messianic prophecy chains (Isa 7:14, 53:1-12,
    Ps 22, Mic 5:2, Zech 9:9, etc.) linked bidirectionally with NT fulfillments.

  Script CLI:
  ```
  python3 scripts/build-parallels.py          # generate all files
  python3 scripts/build-parallels.py --force  # overwrite existing
  python3 scripts/build-parallels.py genesis matthew  # specific books only
  ```

  **`bible.js` additions**

  ```
  var parallelsCache = {}  // bookId → data or null (same pattern as crossRefCache)

  loadParallels(bookId)              — fetch + cache data/parallels/{bookId}.json
  renderParallelPanels(parsed, groupEl) — inject panels below a reader passage group
  renderOneParallel(refStr, type, label, container) — render a single stacked panel
  toggleParallels(on)               — show/hide all panels, persist preference
  initParallelToggle()              — build toggle button, wire to toolbar
  ```

  **Optimization approach (handles the many-parallels case)**

  1. **Lazy fetch**: `loadParallels()` is called only when the toggle is ON. If the user
     never enables parallels, zero parallel fetches occur.
  2. **Background pre-fetch of parallel books**: When the toggle turns on, scan the current
     chapter's parallel data and fire `Promise.all` for all parallel book JSONs in parallel.
     These write into the existing `bookCache`, so once loaded they never re-fetch. For the
     Olivet Discourse (Matt 24 + Mark 13 + Luke 21), this is 3 fetches that run concurrently.
  3. **Partial display by default**: Each panel shows the first 3 verses; the rest are rendered
     but hidden with `display:none` behind a "Show N more" toggle. This keeps DOM weight low
     on first render — the full text is in the DOM but not painted.
  4. **No virtual scrolling needed**: Stacked verse panels are semantically small DOM trees.
     Even a 4-way Gospel parallel (4 × 35 verses = 140 verse spans) is trivially fast to
     render. Virtualization adds complexity without meaningful gain here.
  5. **bookCache re-use**: Parallels share the same version-aware `bookCache` used by the
     reader. If the user has already read Mark that session, Mark's parallel text is free.
  6. **Toggle-off cleanup**: When parallels are toggled off, remove all `.reader-parallel-section`
     elements from the DOM so there is zero layout cost while the feature is inactive.

  **CSS: `assets/css/reader.css` additions**
  - `.reader-parallel-section` — panel container with left border accent colored by type
  - `.reader-parallel-header` — header row with type badge, passage ref, collapse chevron
  - `.reader-parallel-type-badge` — small tag: "Parallel" (blue) / "Fulfillment" (green) / "Prophecy" (gold)
  - `.reader-parallel-body` — verse text, same typography as main reader
  - `.reader-parallel-body--collapsed` — hides overflow verses (first 3 visible, rest hidden)
  - `.reader-parallel-more-btn` — "Show N more verses" expander

---

## Phase C — Scholarly Depth (makes this better than BLB for serious lay study)

- [ ] **C1. Additional public domain commentaries** *(effort: 1 week)*
  - Currently only Matthew Henry's Concise Commentary is bundled
  - Add to the Commentary tab (selectable source dropdown):
    - **Barnes' Notes on the Bible** (Albert Barnes, 1832–1885) — OT + NT, verse-by-verse, public domain
    - **Jamieson-Fausset-Brown Commentary** (1871) — single-volume, scholarly, public domain
    - **Adam Clarke's Commentary** (1810–1826) — strong on original languages, public domain
    - **Vincent's Word Studies** (NT only, Marvin Vincent, 1886) — excellent Greek word-level commentary
  - Data source: SWORD Project public domain modules; same processing pipeline as Matthew Henry
  - Storage: `data/commentary/{source}/{bookId}.json` — same shape as existing commentary JSON
  - e-Sword built its 25M-download reputation on bundling exactly these four; matching them is achievable

- [ ] **C2. Interlinear reader — Greek NT + Hebrew OT** *(effort: 2–4 weeks)*
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
    - These are the same datasets used by BLB and BibleHub
  - **Token JSON shape:**
    ```json
    { "eng": "In", "orig": "בְּרֵאשִׁ֖ית", "translit": "bə·rê·šîṯ",
      "strongs": "H7225", "parse": "N-FS", "lemma": "רֵאשִׁית" }
    ```
  - Render as a word-grid below the verse text when interlinear mode is active
  - This is the feature that makes this tool better than BLB for lay students who want
    original-language access without Logos pricing

- [ ] **C3. Reading plans** *(effort: 3–5 days)*
  - `plans/index.html` — browse and enroll in classic reading plans:
    - M'Cheyne's Calendar (OT + NT daily, 1 year) — public domain
    - Through the Bible in a Year (chronological) — public domain
    - New Testament in 90 Days
    - Psalms & Proverbs in a Month
    - Gospels in 30 Days
  - Plans stored as `data/plans/{id}.json` — arrays of daily reading lists
  - Enrollment + daily completion tracked in `localStorage` key `bsw_plans`
  - Home page widget: "Today's Reading" showing the day's passages for enrolled plans,
    each reference linking directly to the Reader
  - YouVersion's dominant engagement feature; even 3–5 plans add meaningful daily-return habit

---

## Phase D — Content & Reference

- [ ] **D1. Library section — complete the confessions data** *(effort: ongoing)*

  ### Data structure (`data/library/`)
  ```
  data/library/{id}.json              — the document itself
  data/library/index.json             — metadata list (id, title, abbrev, year, type)
  data/library/verse-index/{bookId}.json  — reverse lookup: verse → confessional citations
  ```

  Document types:
  - `"type": "creed"` — short articles, no proof texts (Apostles', Nicene, Athanasian)
  - `"type": "confession"` — chapters → numbered sections with proof text refs
  - `"type": "catechism"` — numbered Q&A with proof text refs
  - `"type": "canons"` — heads of doctrine → articles (+ rejections)

  Confession JSON shape:
  ```json
  {
    "id": "wcf", "title": "Westminster Confession of Faith",
    "abbrev": "WCF", "year": 1646, "type": "confession",
    "content": {
      "1": {
        "heading": "Of the Holy Scripture",
        "sections": { "1": { "text": "…", "proofs": ["2Pet 1:19-21", "2Tim 3:16"] } }
      }
    }
  }
  ```

  Catechism JSON shape (Q&A):
  ```json
  {
    "id": "wsc", "title": "Westminster Shorter Catechism",
    "abbrev": "WSC", "year": 1647, "type": "catechism",
    "content": {
      "1": {
        "q": "What is the chief end of man?",
        "a": "Man's chief end is to glorify God, and to enjoy him forever.",
        "proofs": ["1Cor 10:31", "Ps 73:25-28"]
      }
    }
  }
  ```

  Verse index shape:
  ```json
  // data/library/verse-index/john.json
  { "3": { "16": [{ "doc": "WCF", "ref": "WCF 7.3", "text": "…" }] } }
  ```

  ### Documents to build (priority order)
  - [x] Apostles' Creed (page exists)
  - [x] Nicene Creed (page exists)
  - [x] Athanasian Creed (page exists)
  - [x] Heidelberg Catechism (page exists)
  - [x] Westminster Confession of Faith (page exists)
  - [x] Westminster Shorter Catechism (page exists)
  - [ ] Belgic Confession (1561) — page missing, 404
  - [ ] Canons of Dort (1618–1619) — page missing, 404
  - [ ] Westminster Larger Catechism — page missing, 404
  - [ ] London Baptist Confession (1689) — page missing, 404
  - [ ] Augsburg Confession (1530) — page missing, 404
  - [ ] 39 Articles of Religion — page missing, 404

  ### Reader integration
  - Extend input parser to recognize library refs: "WCF 4", "WSC 1", "HC 26", "Belgic 1"
  - Reader renders library content with same Prev/Next nav and browse dropdown
  - Browse dropdown gets a "Library" group alongside the 66 Bible books
  - Scripture proof texts auto-linked via `.ref` system

  ### Verse modal integration
  - Add a **"Confessions"** tab (alongside Verse / Commentary / Word Study)
  - Loads `data/library/verse-index/{bookId}.json` on demand
  - Shows all confessional sections citing the selected verse, grouped by document
  - Each entry links to the full section in the Reader

- [ ] **D2. New topic studies** *(ongoing — target: 5+ more)*
  - Currently: Prayer, Book of Revelation (2 exist)
  - Priority additions:
    - Justification by Faith
    - The Holy Spirit
    - The Sermon on the Mount (Matthew 5–7)
    - Romans (book study)
    - The Psalms (overview + devotional categories)
    - The Covenants (Biblical Theology)
    - Christology (Person & Work of Christ)
  - Use `scripts/new-topic.sh` for scaffolding; follow `topics/_template/index.html`

- [ ] **D3. Church Fathers library**
  - Per-Father pages (Ignatius, Justin Martyr, Irenaeus, Tertullian, Origen, Chrysostom, Augustine, etc.)
  - Key writings and quotes organized by theological topic
  - All Scripture refs linked via `.ref` system
  - Could reuse the Library JSON structure from D1

- [ ] **D4. Bible dictionary / glossary**
  - Theological term definitions (propitiation, sanctification, covenant, imputation, etc.)
  - Biblical character profiles
  - Place name guide
  - Data source: ISBE (International Standard Bible Encyclopaedia, 1915) — public domain
  - Storage: `data/dictionary/{term-slug}.json`
  - Integration: hover over a `<span class="term">` → definition tooltip; standalone `dictionary/index.html`

---

## Phase E — Visual & Historical Tools

- [ ] **E1. Bible timeline** *(effort: 2–4 weeks)*
  - Interactive SVG timeline of biblical history:
    Creation → Patriarchs → Exodus → Judges → Monarchy → Divided Kingdom →
    Exile → Return → Intertestamental → Gospels → Acts → Epistles → Revelation
  - Clickable events link to relevant Reader passages
  - Data sources: public domain biblical chronology (BibleTimeline.info, OpenBible geography data)
  - Renders as a horizontal scrollable SVG on wide screens, vertical on mobile
  - No major free web tool has this done well — genuine differentiator for visual learners

- [ ] **E2. Biblical geography maps** *(effort: 2–3 weeks)*
  - SVG-based maps with clickable place names:
    - Ancient Near East (Patriarchal era)
    - The Exodus route
    - Canaan / Tribal allotments
    - Israel & Judah (Monarchy period)
    - Palestine in the time of Jesus
    - Paul's Missionary Journeys (3 separate maps)
  - Each place name linked to relevant passages via the `.ref` system
  - Hosted at `maps/index.html`

---

## Phase F — Polish

- [ ] **F1. Dark mode toggle**
  - CSS custom properties are already structured for it (all colors via `--color-*` variables)
  - Toggle button in header, preference saved to `localStorage` key `bsw_theme`
  - `prefers-color-scheme` media query as the default, manual toggle overrides it

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
- All Scripture refs use `.ref[data-ref]` pattern — auto-wired by `bible.js`
- Scripts: `scripts/serve.py` (dev server), `scripts/restart.py` (kill + restart), `scripts/new-topic.sh` (topic scaffold)
