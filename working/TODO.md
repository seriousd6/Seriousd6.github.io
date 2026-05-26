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
- [x] **Parallel Passage Reader** — toggle in reader toolbar; stacked panels with fulfillment/prophecy/parallel type badges; lazy fetch with `bookCache` reuse; localStorage persistence (`bsw_parallels`); CSS in `reader.css`; data in `data/parallels/`

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

## Phase VS — Verse Study (Deep Dive) *(priority: high — build after Phase A)*

A full-page verse study experience that aggregates every available reference for a single verse. The "go deep" destination — richer than the quick modal, purpose-built for single-verse study.

- [ ] **VS1. Verse Study page** (`verse-study/index.html?ref=John+3:16&v=BSB`) *(effort: 3–5 days for core; sections grow incrementally as data is added)*

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
     - *(future: Add Note — B3; Highlight — B3; Bookmark — B6; Add to Memory — C4; wired into this menu when built)*
  3. **Direct URL** — fully shareable; works as a search-engine landing page

  ### Page structure

  ```
  [← John 3 in Reader]                              [Version ▾]

  ┌──────────────────────────────────────────────────────────┐
  │ John 3:16  [Context ▾]                                   │  ← sticky header
  │                                                          │
  │ ¹⁵ …that whoever believes may have eternal life.         │  ← prev verse, dimmed
  │                                                          │
  │ ¹⁶ For God so loved the world, that he gave his          │
  │    only Son, that whoever believes in him should         │
  │    not perish but have eternal life.                     │  ← focal verse, full-size
  │                                                          │
  │ ¹⁷ For God did not send his Son to condemn…              │  ← next verse, dimmed
  ├──────────────────────────────────────────────────────────┤
  │ Word Study                                               │
  │ [For] [God] [so] [loved] [the] [world] [that]…          │  ← clickable tokens
  │  ▼ G25 · ἀγαπάω · agapaō (Aorist Active Indicative 3S)  │  ← expands on click
  │    "to love, to regard with favor" · 143× in NT · all → │
  └──────────────────────────────────────────────────────────┘

  Desktop sidebar nav:  Cross-References | Commentary | Parallels | Confessions | Fathers | Dictionary
  Mobile: [Section: Cross-References ▾] dropdown at top of content area

  ## Cross-References
  ## Commentary  [Matthew Henry ▾]
  ## Parallel Passages
  ## Confessional Citations      ← appears when D1 verse-index is built
  ## Church Fathers              ← appears when D3 is built
  ## Dictionary Terms            ← appears when D4 is built
  ```

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

  ### JS additions (`bible.js` or new `verse-study.js`)

  - `tokenizeVerse(text)` — split verse text into word tokens, preserving punctuation as non-clickable spans
  - `renderTokenRow(tokens, container)` — build `<button class="vs-token">` elements; attach click handler
  - `openWordStudy(tokenEl, strongsId)` — expand inline word study panel below token row; collapse previous if different word clicked
  - `loadVerseSections(parsed)` — orchestrate parallel fetches for all data sections; each section renders independently as data arrives
  - Verse-number click handler in `bible.js` reader — build popup menu; wire "Verse Study" link and future note/highlight/bookmark/memory actions

  ### CSS: new `assets/css/verse-study.css`

  - `.vs-header` — sticky verse display block with context strip
  - `.vs-context-verse` — dimmed prev/next verse; hidden when context is toggled off
  - `.vs-focal-verse` — focal verse, full-weight typography
  - `.vs-token-row` — word token button row beneath the verse block
  - `.vs-token` — individual word button; highlights on hover and when its word study panel is open
  - `.vs-word-panel` — inline Strong's flyout below the token row
  - `.vs-sidebar` — sticky left section nav (desktop ≥ 768px)
  - `.vs-mobile-nav` — top-of-content `<select>` dropdown (mobile < 768px)
  - `.vs-section` — each reference section container (cross-refs, commentary, etc.)
  - `.vs-section-heading` — consistent section headings with `scroll-margin-top` for anchor accuracy

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
  - **VS1 integration:** B2 data directly powers the Verse Study word token panel

- [ ] **B3. Personal notes & verse highlights** *(effort: 3–5 days)*
  - Click a verse number to toggle a yellow highlight (persists in localStorage)
  - Right-click / long-press a verse → open a small note editor textarea
  - Notes saved to `localStorage` key `bsw_notes` as `{ "John 3:16": { highlight: true, note: "…" } }`
  - `notes/index.html` — "My Notes" page listing all annotated verses with ref links back to Reader
  - Export option: copy all notes as plain text or JSON
  - Highlights visible in both the Reader and verse modal
  - Privacy-first: everything local, nothing leaves the browser
  - **VS1 integration:** Note and Highlight actions wired into the Reader verse-number popup menu (alongside "Verse Study")

- [ ] **B4. PWA / offline mode** *(effort: 2–3 days)*
  - Add `manifest.json` (name, icons, theme color, start URL, display: standalone)
  - Add a service worker (`sw.js`) with:
    - Cache-first strategy for `data/bible/**`, `data/crossrefs/**`, `data/commentary/**`, all CSS/JS
    - Network-first for HTML pages so updates are always received when online
    - Background pre-cache of all Bible JSON using `requestIdleCallback` after first visit
  - Total Bible JSON size: ~30–40 MB for 4 versions — reasonable for a dedicated study tool
  - Result: site works fully offline after first visit; no major free web tool offers this
  - This is a genuine architectural differentiator — the static JSON-based design is perfectly suited for PWA

- [x] **B5. Parallel Passage Reader** *(complete)*
  - Toggle in reader toolbar (next to version picker); state in `localStorage` key `bsw_parallels` (default: off)
  - Three parallel types with visual badges: ⇌ Parallel (blue) / ✓ Fulfilled in (green) / ⌖ Prophesied in (gold)
  - Stacked panels below each passage; first 3 verses visible, "Show N more" expander for remainder
  - Per-panel ▾/▸ collapse button; collapse state resets on chapter navigation
  - Lazy fetch — `loadParallels()` only fires when toggle is ON; zero fetches while feature is inactive
  - `bookCache` reuse — parallel book text is free if the user has already read it that session
  - Toggle-off removes all `.reader-parallel-section` elements from DOM (zero layout cost while inactive)
  - CSS in `reader.css`; data in `data/parallels/{bookId}.json`

- [ ] **B6. Bookmarks** *(effort: half day)*
  - One-click star/bookmark on any verse — no text entry required (distinct from B3 notes, which require writing)
  - Stored in `localStorage` key `bsw_bookmarks` as an array of ref strings (`["John 3:16", "Ps 23:1"]`)
  - `bookmarks/index.html` — list all bookmarked verses with jump links to Reader and Verse Study
  - Bookmarked verse numbers get a small ★ indicator in the Reader
  - Wired into the Reader verse-number popup menu (VS1) alongside Note, Highlight, Verse Study

- [ ] **B7. Single-verse all-translations comparison** *(effort: 1–2 days)*
  - Dedicated view showing one verse across all available versions stacked vertically
  - URL: `compare/index.html?ref=John+3:16` — shareable; works as a search-engine landing page
  - Accessible from: Reader toolbar, Verse Study page header, verse modal
  - Distinct from B1 (B1 is side-by-side chapters; this is one verse × all versions)
  - BibleHub's most-visited page format; drives significant search traffic for "[verse] all translations"
  - Add YLT, Darby, Geneva (from B1) first to make the comparison compelling — 7 versions stacked is genuinely useful

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
  - **VS1 integration:** commentary source dropdown in Verse Study powered by the same data

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
  - **VS1 integration:** interlinear row slots directly beneath the VS1 token row — same token shape, same click handler
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

- [ ] **C4. Scripture memory / flashcard tool** *(effort: 3–5 days)*
  - `memorize/index.html` — browse verses in the memory list; enter flashcard mode
  - Flashcard modes: show reference → recall text; or show text → recall reference
  - Spaced repetition via simple interval scoring in `localStorage` key `bsw_memory`:
    `{ "John 3:16": { interval: 3, nextReview: "2026-06-01", score: 2 } }`
  - "Add to Memory" action available from: verse modal, Verse Study page, Reader verse-number popup menu
  - No backend required; highest-engagement feature not yet on this list

- [ ] **C5. Nave's Topical Bible** *(effort: 1–2 weeks)*
  - 20,000+ topic index (Orville Nave, 1896 — public domain) — the backbone of BLB and e-Sword topical tools
  - `topical/index.html` — alphabetical browse + search across all topics
  - Data source: `openscriptures/nave` on GitHub
  - Storage: `data/topical/{topic-slug}.json` (topic heading + verse list)
  - **Verse modal integration:** new "Topics" tab listing all Nave's topics that cite the current verse
  - **VS1 integration:** same Topics data surfaces in the Verse Study sidebar
  - Distinct from manual `topics/` pages — those are curated studies; Nave's is an exhaustive concordance-style topical index

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
  - **VS1 integration:** same data powers the Confessional Citations section in Verse Study

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
  - **VS1 integration:** Father quotes for a verse surface in the Church Fathers section of Verse Study

- [ ] **D4. Bible dictionary / glossary**
  - Theological term definitions (propitiation, sanctification, covenant, imputation, etc.)
  - Biblical character profiles
  - Place name guide
  - Data source: ISBE (International Standard Bible Encyclopaedia, 1915) — public domain
  - Storage: `data/dictionary/{term-slug}.json`
  - Integration: hover over a `<span class="term">` → definition tooltip; standalone `dictionary/index.html`
  - **VS1 integration:** Dictionary Terms section highlights theological terms in the focal verse text

- [ ] **D5. Book introductions & outlines** *(effort: 1–2 weeks)*
  - Per-book intro for all 66 books: author, date written, purpose, key themes, structural outline
  - Outline uses section-level labels with verse ranges (e.g., "Matthew 5–7: Sermon on the Mount") — each section links directly to the Reader at that chapter
  - **Historical timeline strip** — each book intro includes an estimated date range and a mini-timeline showing 1–2 significant biblical events immediately preceding and following the book, so the reader can place it in redemptive-historical context at a glance
    - Example for Ruth: `← Judges period (oppression & cycles) · Ruth (~1100 BC) · Early Monarchy (Samuel, Saul) →`
    - Example for Galatians: `← Paul's 1st Missionary Journey (Acts 13–14) · Galatians (~AD 48) · Jerusalem Council (Acts 15) →`
    - Events link to relevant Reader passages; dates sourced from standard evangelical chronology (public domain)
    - Data shape: `"timeline": { "date": "~1100 BC", "before": [{ "label": "Judges period", "ref": "Judges 2:16" }], "after": [{ "label": "Early Monarchy", "ref": "1 Samuel 1:1" }] }`
  - Data: static JSON `data/books/introductions/{bookId}.json`; text sourced from ISBE (1915) + Easton's (public domain)
  - Displayed in the Reader sidebar (collapsible) when viewing any chapter of that book
  - Also accessible at `books/{bookId}/index.html` as a standalone reference page
  - Missing from every major free web tool — genuine differentiator for book-study users

- [ ] **D6. Spurgeon's Morning and Evening devotionals** *(effort: 2–3 days)*
  - Public domain daily devotional (C.H. Spurgeon, 1865) — 365 morning + 365 evening entries
  - Each entry keyed to a Bible verse; surfaces in Verse Study for relevant verses
  - Data: `data/devotionals/spurgeon-morning.json` + `data/devotionals/spurgeon-evening.json` (keyed by `MM-DD`)
  - `devotionals/index.html` — browse today's entry or navigate by date
  - Source: CCEL.org plain text files; public domain
  - Complementary to D7 (VOTD) and C3 (reading plans)

- [ ] **D7. Verse of the Day** *(effort: 2–4 hours)*
  - Home page widget showing today's featured verse with full tooltip/modal on hover/click
  - Implementation: static `data/votd.json` — curated list of 365 verse refs; selected by `dayOfYear % 365`
  - No API dependency, no backend, no CORS — consistent with the static-first design; works offline after B4
  - Natural companion to D6 (Spurgeon) and C3 (reading plans); high daily-return engagement

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

- [ ] **F2. Copy / Share verse** *(effort: 1–2 hours)*
  - One-click copy button in the verse modal, Reader verse-number popup menu, and Verse Study page
  - Default format: `"For God so loved the world…" — John 3:16 (BSB)`
  - Optional formats selectable via a small dropdown: Plain text | Markdown blockquote | Academic citation (`John 3:16, Berean Standard Bible, 2022`)
  - Implementation: `navigator.clipboard.writeText()`; `execCommand('copy')` fallback for older browsers
  - Universal expectation; currently absent from the entire site

- [ ] **F3. Text accessibility controls** *(effort: 3–4 hours)*
  - Font size control in Reader and Verse Study: Small / Medium / Large / XL
  - Preference saved to `localStorage` key `bsw_fontsize`; applied via CSS custom property `--reader-font-size`
  - `reader.css` already uses `--reader-font-size`; needs a toggle UI and localStorage wiring
  - Optional: serif / sans-serif toggle (Georgia default vs. system-ui)
  - Critical for older users and mobile reading comfort

- [ ] **F4. Read history / recently viewed** *(effort: 2–3 hours)*
  - Last 10 passages viewed in the Reader saved to `localStorage` key `bsw_history`
  - Each entry: `{ ref: "John 3", version: "BSB", timestamp: … }`
  - Displayed in sidebar (collapsible "Recently viewed" group) or home page "Continue reading…" widget
  - Shown as "John 3 · BSB · 2 days ago" with a direct link back to the Reader

- [ ] **F5. Print-friendly chapter view** *(effort: 2–4 hours)*
  - "Print this chapter" button in Reader toolbar
  - Applies `@media print` styles: hide sidebar, nav, cross-ref panel; full-width verse text, clean margins, page break handling
  - Some print CSS already exists in stylesheets; needs a dedicated button and a layout audit pass
  - Important for physical Bible study groups and sermon prep

- [ ] **F6. Structured citation format** *(effort: 1–2 hours)*
  - "Cite" button in verse modal and Verse Study page
  - Copies the verse in a selectable academic format:
    - Short: `John 3:16 (BSB)`
    - Long: `John 3:16, Berean Standard Bible (2022)`
    - MLA-style: `"For God so loved…" Holy Bible, Berean Standard Bible, 2022, John 3:16.`
  - Distinct from F2 (which copies verse text + ref); this copies a citation string only
  - Useful for sermon notes, academic papers, Bible study handouts

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
