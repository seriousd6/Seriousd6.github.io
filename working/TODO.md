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

## Bugs

- [ ] **BUG-1. Memory — completing the last card does nothing**
  - After scoring the final card in a review session, the UI sits on a blank or stale state with no feedback
  - Add a "completion card" that appears after the last card is scored: brief encouragement text
    (e.g., "Session complete — well done! You reviewed N verses."), today's review count, and a
    button to return to the Browse panel
  - Check `_memNextCard()` in `bible.js` — the path where `pendingCards` empties after the last
    score needs to render the completion view rather than calling `_memShowCard()` again
  - Completion state should also update the summary stats visible in the Browse panel

- [ ] **BUG-2. Commentaries not visible in the Reader pane**
  - The Commentary tab in the verse modal works, but the Reader's right-hand pane does not show
    commentary content when selected
  - Trace `_refreshCommentaryPanel()` (or equivalent) in `bible.js` — check whether the call is
    wired to the reader's cross-ref panel tab switcher or whether the fetch/render path silently fails
  - Expected behavior: selecting "Commentary" in the reader right-pane tab loads the relevant
    commentary entry for the currently visible passage, identical to the modal's Commentary tab

- [ ] **BUG-3. Topics tab in verse modal needs more breathing room**
  - The Topics tab content (Nave's topic chips) is visually cramped — insufficient padding between
    the chip row, the count line, and the "Browse all" link (see screenshot: chips sit flush against
    the tab border)
  - Add `padding-top` / `gap` adjustments to the `.bsw-modal-topics` container in `bible-ui.css`;
    match the visual rhythm of the Verse and Commentary tabs

- [ ] **BUG-4. Search page label still reads "Omni-search" — should be "Search"**
  - The search page (`search/index.html`) heading or tab label was renamed to "Omni-search" during
    development but should simply read "Search" in all user-visible text
  - Update: page `<title>`, `<h1>` / heading element, sidebar nav entry in `main.js`, and any
    `aria-label` or placeholder text that still says "Omni-search"

- [ ] **BUG-5. Book-study banner doesn't clear when navigating to a book with no study**
  - When a book with an available study is selected in the Reader, the "Study available" banner appears
  - Navigating to a different book that has no study should clear the banner; navigating to a book
    that has a study should update it to that book's study
  - Locate the banner-render call in `bible.js` (triggered on book/chapter load); ensure it runs
    on every navigation event, not just on initial page load or when a study is found — an explicit
    "hide banner" path is needed for the no-study case

- [ ] **BUG-6. Notes in the Reader pane cannot be deleted**
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

## Phase VS — Verse Study (Deep Dive) *(priority: high — build after Phase A)*

A full-page verse study experience that aggregates every available reference for a single verse. The "go deep" destination — richer than the quick modal, purpose-built for single-verse study.

- [x] **VS1. Verse Study page** (`verse-study/index.html?ref=John+3:16&v=BSB`) — sticky header with focal verse + context strip, word token row, cross-references, Matthew Henry commentary, parallel passages; modal "Open in Verse Study" button; reader verse-number click popup

  ### Design decisions (locked)

  - **URL pattern:** `verse-study/index.html?ref=John+3:16` — same `?ref=` param convention as the Reader; version from `localStorage` or `&v=` override; fully shareable
  - **Layout:** Sticky verse header + sidebar section nav on desktop; top-of-page `<select>` dropdown on mobile (< 768px)
  - **Word study interaction:** Click any word token → expand inline panel below the token row showing Strong's number, Greek/Hebrew, morphology, gloss, occurrence count. Designed so the interlinear row (C2) slots in beneath each token later without restructuring the DOM.
  - **Context strip:** Previous and next verse shown dimmed above/below the focal verse; toggleable via a **Context** button in the header; state saved to `localStorage` key `bsw_dissect_ctx`
  - **Commentary:** One source shown at a time with a source selector dropdown (Matthew Henry first; Barnes, JFB, Clarke, Vincent added automatically as C1 data is built)
  - **Mobile section nav:** Top-of-page `<select>` dropdown; selecting a section smooth-scrolls to it
  - **Name:** "Verse Study" (user-facing label)
  - **Completion note (stub):** Several VS1 sections are currently hidden on the live page pending
    data from B2, C2, D1, D3, and D4; the exact set of sections that are live vs. hidden is not
    tracked; see M3 (data validation stub) — a validation pass should document which sections are
    active and which are waiting on specific data dependencies
  - **Sections with no data yet:** Hidden entirely — they appear automatically as their data dependencies are built; no "coming soon" placeholders

  ### Entry points

  1. **Verse modal** — "Open in Verse Study" button at the bottom of the modal (alongside existing "Read in Reader")
  2. **Reader verse-number click** — clicking a verse-number superscript in the reader opens a small popup menu:
     - **Verse Study** — navigate to `verse-study/index.html?ref=...`
     - *(future: Bookmark — B6; Add to Memory — C4)*
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
  - This is the #1 feature gap vs. BLB; closes the most important competitive distance
  - **VS1 integration:** B2 data directly powers the Verse Study word token panel

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
  - This is a genuine architectural differentiator — the static JSON-based design is perfectly suited for PWA

- [ ] **B4a. PWA / Lighthouse validation audit** *(stub — needs scoping before work begins)*
  - B4 is marked complete but has never been formally audited against PWA install criteria or
    Lighthouse performance targets; an audit could surface regressions or gaps not caught in development
  - Needs to determine: which Lighthouse categories matter (Performance, A11y, Best Practices, PWA),
    what target scores are acceptable, and what remediation steps are in scope
  - Also covers: whether the site is installable on Android and iOS, whether the app icon/manifest
    display correctly on home screens, and whether offline fallback pages exist for all routes

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

## Phase C — Scholarly Depth (makes this better than BLB for serious lay study)

- [x] **C1. Additional public domain commentaries** *(complete)*
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

- [ ] **C2a. RTL layout for Hebrew interlinear tokens** *(stub — needs scoping before work begins)*
  - Hebrew text in C2 is currently rendered left-to-right; Biblical Hebrew reads right-to-left and
    incorrect directionality makes the script visually wrong and harder to read
  - Needs to determine: whether `dir="rtl"` goes on individual tokens, the row container, or both;
    how RTL affects the alignment of transliteration + morphology labels beneath each token;
    whether Strong's numbers (which are LTR) need special handling; and how the interlinear grid
    lays out when Hebrew (RTL) and Greek (LTR) chapters are mixed (e.g., on the compare page)

- [x] **C3. Reading plans** *(complete)*
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

- [ ] **C3a. Reading plan progress tracking** *(stub — needs scoping before work begins)*
  - C3 tracks daily completion but has no visible % complete or projected finish date per plan;
    users have no sense of how far they've come or when they'll finish
  - Needs to determine: where this surface lives (plan detail page vs. home widget vs. both),
    how to handle plans that fall behind schedule (skip-day logic, catch-up mode), and whether
    a streak counter or visual calendar heatmap is in scope here or belongs in a later engagement phase

- [x] **C4. Scripture memory / flashcard tool** *(complete)*
  - `memorize/index.html` — browse verses in the memory list; enter flashcard mode
  - Flashcard modes: show reference → recall text; or show text → recall reference
  - Spaced repetition via simple interval scoring in `localStorage` key `bsw_memory`:
    `{ "John 3:16": { interval: 3, nextReview: "2026-06-01", score: 2 } }`
  - "Add to Memory" action available from: verse modal, Verse Study page, Reader verse-number popup menu
  - No backend required; highest-engagement feature not yet on this list

- [x] **C5. Nave's Topical Bible** *(effort: 1–2 weeks)*
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
  - [x] Belgic Confession (1561)
  - [x] Canons of Dort (1618–1619)
  - [x] Westminster Larger Catechism
  - [x] London Baptist Confession (1689)
  - [x] Augsburg Confession (1530)
  - [x] 39 Articles of Religion

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
  - **Dependency note:** F12 (Chapter 0 navigation) is the UI wire-up for this data; F12 can ship
    with placeholder intros before D5 data is complete, but D5 must finish for Chapter 0 to be useful

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

- [ ] **F0. Core accessibility audit** *(stub — needs scoping before work begins)*
  - No formal accessibility audit has been done; the site may have focus management, ARIA label,
    and screen reader gaps that make it unusable for visually impaired users
  - Needs to determine: which WCAG level to target (AA is the standard), which pages to audit
    first (Reader and Verse Study are the highest-traffic), what tooling to use (axe-core, NVDA,
    VoiceOver), and which gaps are quick wins vs. deep restructuring
  - Related stub: F1a (keyboard-only navigation audit); C2a (RTL Hebrew); L1 (high-contrast mode)

- [ ] **F1a. Keyboard-only navigation audit** *(stub — needs scoping before work begins)*
  - F8 adds keyboard shortcut discovery, but it is not known whether all interactive elements
    (verse popups, modals, collapsible panels, tool toggles) are reachable via Tab/Enter/Escape
    without a mouse
  - Needs to determine: which UI elements are missing tabindex or focus styles, whether focus
    trapping in modals is implemented correctly, and whether the skip-nav link exists

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

- [ ] **F7. Read history / "Continue Reading" home widget** *(effort: 2–3 hours)*
  - Record the last 20 passages viewed in the Reader to `localStorage` key `bsw_history` as
    `{ ref: "John 3", version: "BSB", ts: <timestamp> }` — push on each `initReader` call,
    deduplicate by `ref`, trim to 20 entries; logic in `bible.js` alongside existing localStorage helpers
  - Home page (`index.html`) gains a fourth `daily-card` section labelled "Continue Reading";
    rendered by a new `initHistoryWidget()`; shows last 3 entries with ref text, version badge,
    and relative time label produced by the existing `_noteRelTime()` utility already in `bible.js`
  - Each entry links directly to `read/index.html?ref=…` — no new URL format required
  - Widget hidden entirely if `bsw_history` is empty (first-visit) — no placeholder clutter
  - CSS: one `.daily-card--history` modifier in `daily.css`; reuses existing `.daily-card` shell
  - **F4 dependency:** F4 and F7 share the same storage write; implementing both together is efficient

- [ ] **F8. Keyboard shortcuts help overlay** *(effort: 2–4 hours)*
  - Several keyboard shortcuts exist (j / → next chapter, k / ← prev, Ctrl+K search jump) but
    are completely undiscoverable unless the user reads the source code
  - Press `?` anywhere outside an input field → open a modal overlay listing all active shortcuts
    grouped by context (Global / Reader / Verse Study); wire in existing `initReaderKeyboard()` and
    the VS init block using the same `keydown` pattern already throughout `bible.js`; skip if
    `document.activeElement` is `input`, `textarea`, or `select`
  - Dismiss with `Escape` or a close button; reuses existing `.bsw-modal-backdrop` and
    `trapFocus()` logic from `openModal()`
  - Add a small `?` icon button in the Reader browse bar (next to `.reader-browse-hint`) so
    mouse users can discover it too
  - No new CSS file needed; a `.bsw-shortcuts-overlay` block in `bible-ui.css` is sufficient

- [ ] **F9. Service worker update toast** *(effort: 2–3 hours)*
  - The SW currently calls `SKIP_WAITING` immediately on `updatefound` → `statechange`, silently
    activating a new cache version; the user's open tab serves stale JS/CSS until they manually reload
  - Change the handler so that instead of calling `SKIP_WAITING` immediately, it shows a
    non-blocking toast: "A new version is available — **Reload**"
  - Clicking "Reload" sends `SKIP_WAITING` to `reg.waiting`, then listens for
    `navigator.serviceWorker.controllerchange` and calls `location.reload()`; auto-dismiss after 30s
  - Toast: `<div id="bsw-sw-toast" class="bsw-sw-toast" hidden>` injected by `initPWA()` in
    `bible.js`; CSS in `bible-ui.css`; must not appear on first install (existing
    `if (navigator.serviceWorker.controller)` guard covers this)
  - The `sw.js` message handler that responds to `SKIP_WAITING` is already present — no SW changes needed

- [ ] **F10. Open Graph / Twitter Card meta tags** *(effort: 3–5 hours)*
  - All `?ref=` URLs in `read/`, `verse-study/`, and `compare/` produce blank link previews when
    shared to Slack, iMessage, or social media — no `<meta property="og:*">` tags exist anywhere
  - Add `_setOGMeta(title, description, url)` helper in `bible.js` that creates/updates OG + Twitter
    meta tags in `document.head`; call after verse/chapter renders in each affected page
    - Reader: title `"John 3 — Bible Reader"`, description = first verse of displayed passage
    - Verse Study: title `"John 3:16 — Verse Study"`, description = focal verse text
    - Compare: title `"John 3:16 — All Translations"`
  - Add static default OG tags to `<head>` of each of those three HTML files as a baseline for
    crawlers that do not execute JS; JS overrides them once content loads
  - No new data files; ~30 lines of JS + 4 `<meta>` tags per HTML page

- [ ] **F11. Reader opens to daily verse when no reference is given** *(effort: 1–2 hours)*
  - Currently navigating to `read/index.html` with no `?ref=` parameter shows a blank or default state
  - On load, if no `ref` query param is present, derive today's verse from the same logic that
    powers the Verse of the Day widget (D7): `data/votd.json` keyed by `dayOfYear % 365`
  - Navigate the Reader to that verse's chapter and highlight the verse, exactly as if the user
    had typed the ref manually — gives every session a natural starting point
  - **Dependency:** D7 (VOTD data) must be built first; until then, fall back to a hardcoded
    welcome verse (e.g., Psalm 119:105) as a placeholder

- [ ] **F12. End-of-book navigation: Chapter 0 introduction + in-reader book metadata button** *(effort: 1–2 days)*

  ### Chapter 0 — Book Introduction as a navigable chapter

  Each book has a "Chapter 0" that is its full introduction (the content produced by D5):
  author, date, purpose, key themes, structural outline with linked verse ranges, and the
  historical timeline strip. This makes the introduction a first-class stop in the reading flow,
  not a sidebar afterthought.

  **Navigation behavior:**
  - When on the last chapter of a book, pressing Next (or keyboard shortcut) loads **Chapter 0
    of the next book** — the full D5 introduction — before dropping the reader into Chapter 1
  - After reading Chapter 0, Next continues to Chapter 1 of that book
  - When on Chapter 1 of a book, pressing Prev navigates to Chapter 0 of the same book (the
    intro), then further Prev goes to the last chapter of the preceding book
  - Wrap-around: past Revelation Chapter 0 returns to Genesis Chapter 0; Prev from Genesis
    Chapter 0 wraps to Revelation's last chapter
  - URL: `read/index.html?ref=Genesis.0` — Chapter 0 is a real addressable route; the Reader
    already parameterizes by ref; `ch === 0` triggers intro rendering instead of verse fetch

  **Chapter 0 rendering:**
  - Full D5 content rendered in the main reading pane (not the sidebar): title, author block,
    date/occasion, key themes as a bulleted list, structural outline with verse-range links,
    historical timeline strip (inline horizontal on wide, vertical on mobile)
  - Styled consistently with the Reader's existing prose; scripture refs in the outline use the
    standard `.ref[data-ref]` pattern so they open tooltips on hover
  - A prominent "Begin Reading →" button at the bottom loads Chapter 1
  - No verse-level tools (no highlights, no notes per verse) on Chapter 0 — but a single
    "Bookmark this book" action is available

  **Data:** reads from `data/books/introductions/{bookId}.json` (defined by D5); F12 is the UI
  wire-up — D5 is the data creation task. F12 can ship with placeholder intros and be filled
  in as D5 progresses.

  ### In-reader book metadata button

  While reading any numbered chapter, a **"Book Info"** toggle button appears in the Reader
  browse bar alongside the existing Parallels and Interlinear buttons.

  - Clicking it expands a collapsible panel immediately above the verse list (same slide-down
    pattern as the existing commentary panel) showing a condensed summary of the D5 data:
    author, date, ~2-sentence purpose statement, and a mini timeline strip
  - A "Full Introduction →" link at the bottom of the panel navigates to Chapter 0
  - State is not persisted — panel collapses on chapter navigation (same behavior as Interlinear)
  - No new CSS file; `.reader-bookinfo-panel` block added to `bible-ui.css`; button uses the
    existing `.reader-tool-btn` class already applied to Parallels and Interlinear toggles

- [ ] **F13. Asset optimisation** *(stub — needs scoping before work begins)*
  - No image optimisation has been done; any PNG/JPG assets should be WebP; SVGs should be
    cleaned of editor metadata; total page weight impact is unknown
  - Needs to determine: which assets exist, their current sizes, and whether WebP conversion
    or SVG minification would produce meaningful savings on the target audience's devices

- [ ] **F14. Data compression and lazy-loading strategy** *(stub — needs scoping before work begins)*
  - Commentary JSON files are large and currently loaded eagerly; no gzip or lazy-load strategy
    is in place; the ~43 MB total cache could be reduced significantly with compression
  - Needs to determine: which data files are the best candidates for lazy loading (commentaries,
    topical data, interlinear), whether GitHub Pages serves pre-compressed `.gz` files or if
    compression must happen at build time, and what the actual impact on Time-to-Interactive is

- [ ] **F15. Empty state UX** *(stub — needs scoping before work begins)*
  - A first-time visitor with no notes, bookmarks, memory cards, or enrolled plans sees blank
    pages on Notes, Bookmarks, Memorize, and Plans — no guidance on what to do next
  - Needs to determine: which empty states are highest priority, what the copy and CTA should be,
    and whether a global first-visit onboarding flow (Phase U) should handle this instead

- [ ] **F16. LocalStorage migration and data versioning** *(stub — needs scoping before work begins)*
  - As features evolve, `localStorage` schemas (bsw_notes, bsw_plans, bsw_memory, etc.) will
    gain new fields; existing users' data needs forward-migration so it isn't silently corrupted
    or ignored after a schema change
  - Needs to determine: a versioning scheme for each storage key (e.g., `bsw_notes_v` field),
    a migration runner that fires on page load, and what the fallback is if migration fails
  - This is a data-safety risk that grows with every new feature that touches localStorage

- [ ] **F17. Service worker cache invalidation strategy** *(stub — needs scoping before work begins)*
  - B4 implements cache-first for data files but has no plan for breaking schema changes (e.g.,
    adding a new required field to every verse JSON) — old cached versions could break silently
    for users who haven't cleared their cache
  - Needs to determine: how cache versioning works (SW version bump clears old caches?),
    what the rollback plan is for a bad cache push, and how to handle users on very old SW versions
  - Related to F16 (localStorage migration) — both are data-safety risks that compound over time

---

## Phase G — Search Quality *(priority: medium — high daily-use impact)*

The search engine is accurate but presents results in canonical Bible order with no relevance
ranking, no scope filtering, and no session memory. These three items address that incrementally;
each is independently shippable.

- [ ] **G1. Relevance-ranked search results** *(effort: 4–6 hours)*
  - Results currently sort by canonical book/chapter/verse order regardless of match quality
  - A `computeTextSimilarity()` function already exists in `bible.js` (~lines 607–638) but is not
    called from `handleSearchInput()`
  - Add a `score` field to each result: exact phrase match → 100; all words present → Jaccard
    similarity via `computeTextSimilarity()`; partial match → 0
  - Sort `allResults` by `score DESC`, canonical order as tiebreaker
  - Add a "Sort: Relevance | Bible order" toggle next to the `.search-mode-btn` row;
    preference saved to `localStorage` key `bsw_search_sort`
  - No new data files; all logic changes are in `bible.js`

- [ ] **G2. Search scope filters (Testament / Book)** *(effort: 3–5 hours)*
  - Users studying a specific book or testament have no way to constrain results today
  - Add a collapsible "Filter ▾" row below search mode buttons (collapsed by default)
  - Controls: `All | Old Testament | New Testament` toggle buttons; a Book `<select>` populated
    from `metaBooks` (disabled when a Testament filter is active)
  - `booksToSearch` in `handleSearchInput()` gains a `.filter()` call gated on active filter state;
    the Strong's search `handleStrongsSearch()` respects the same Testament control
  - Filter state is session-only variables (not persisted to localStorage)
  - Status line update: "Searching Old Testament… (18 / 39 books)"

- [ ] **G3. Search history (recent queries)** *(effort: 2–3 hours)*
  - Save last 10 distinct non-empty queries to `localStorage` key `bsw_search_history` (push on
    submit, deduplicate, trim to 10)
  - On focus of `#bsw-search-input` when empty, show a small dropdown of recent queries below
    the input (`.search-history-dropdown`); dismiss on blur or when user types
  - Each history item is a clickable chip that sets the input value and triggers search
  - "Clear history" link at the bottom removes the key from localStorage
  - No dependencies on G1 or G2; ships independently
  - CSS: `.search-history-dropdown` + `.search-history-chip` in `bible-ui.css`

- [ ] **G4. Search results: book-grouped bubble/chip layout** *(effort: 6–10 hours)*
  - Current results render as a flat list of verse rows sorted by book order; this is functional
    but dense and hard to scan at a glance
  - Replace with a grouped-by-book layout, styled similarly to the interlinear word-token grid:
    each book is a section heading followed by a row of verse chips, where each chip shows the
    first 10–15 words of the verse in a rounded bubble
  - Page width: expand the search results container to use more horizontal space (currently narrow);
    chips can wrap naturally so each book's row fills the available width
  - **Chip interaction:**
    - Hovering a chip shows the standard verse tooltip (existing `openTooltip()` behavior)
    - Clicking a chip opens the verse modal (`openModal()`) — identical to hovering/clicking a
      `.ref` link anywhere else on the site
  - **Chip shape:**
    ```html
    <span class="search-chip" data-ref="Romans 3:23">
      <span class="search-chip__ref">Romans 3:23</span>
      <span class="search-chip__preview">for all have sinned and fall…</span>
    </span>
    ```
  - Results count and the "Sort: Relevance | Bible order" toggle (G1) remain above the grouped list
  - CSS: `.search-results-book-group`, `.search-chip`, `.search-chip__ref`, `.search-chip__preview`
    in `bible-ui.css`; chip width ~200–240px; truncate preview text with `text-overflow: ellipsis`

- [ ] **G5. Strong's: English keyword → code lookup** *(effort: 4–6 hours)*
  - Currently Strong's search requires knowing the code (G3056, H1697); most users start from
    an English word and want to discover the underlying Greek or Hebrew
  - Add an English-to-Strong's lookup mode in the Strong's search tab:
    - User types an English word (e.g., "love") → results show all Strong's entries whose
      gloss or definition contains that word, displayed as chips: `G25 ἀγαπάω · agapaō — to love`
    - User clicks a chip → the existing Strong's concordance view loads for that code, showing
      all verses containing that word — no new verse-fetch logic needed
  - Implementation: build a reverse index `data/strongs/english-index.json` mapping lowercase
    English gloss words to arrays of Strong's codes:
    `{ "love": ["G25", "G5368", "H157", "H160", …] }` (~500 KB estimated)
  - The index is built once from the existing `data/strongs/greek.json` + `data/strongs/hebrew.json`
    via a `scripts/build-strongs-index.py` script; committed and static thereafter
  - Also accept raw Strong's codes typed directly (existing behavior) — mode is detected by
    whether the input matches `/^[GH]\d+$/i`
  - UI: a single search input with a small "G/H code" / "English word" mode indicator; no
    extra tab needed since the disambiguation is automatic

- [ ] **G6. Topics search: include Nave's topics and library documents** *(effort: 4–6 hours)*
  - The "Topics" search mode in `search/index.html` currently searches only the curated `topics/`
    study pages and `topics/index.html`; it does not search Nave's 20,000+ topic index or the
    11 library/confession documents — significant blind spots
  - **Nave's topics:** when the query matches a Nave's topic name (exact or fuzzy), surface the
    matching topics as chips above the study-page results, each linking to
    `topical/index.html?topic={slug}`; load `data/topical/` index on demand (already fetched by
    the topical page — reuse the same fetch and cache pattern)
  - **Library documents:** integrate the `data/library/search-index.json` built in I2; when a
    text query matches content inside a confession or creed, show those results in a "Confessions
    & Creeds" group below the topic study results; each result links to the relevant section
  - Result groups in Topics mode (top to bottom):
    1. Nave's topic matches (chips, if any)
    2. Curated topic study pages (existing behavior)
    3. Confession/creed sections (from library search index, if I2 is built)
  - **Dependency:** I2 (library search index) must be built for group 3 to work; groups 1 and 2
    are independent of I2 and can ship first

---

## Phase H — Notes & Highlights UX *(priority: medium)*

The notes system has a solid data model but the `notes/index.html` page is minimal and
the highlight system is single-color. These three items improve daily usability.

- [ ] **H1. Multi-color highlights** *(effort: 3–5 hours)*
  - Currently `toggleHighlight()` stores `highlight: true/false` and only renders yellow
  - Replace with `highlight: "yellow" | "green" | "blue" | "pink" | false`; `bsw_notes_v2`
    gains an optional `"color"` field on each entry; backward compatible (`true` treated as yellow)
  - Verse-number popup "Highlight" action becomes a 4-swatch color palette (16×16px CSS squares);
    clicking a swatch calls `toggleHighlight(refStr, color)`; same color re-clicked toggles off
  - Reader renders highlighted rows with a left border matching the active color:
    `--highlight-yellow`, `--highlight-green`, `--highlight-blue`, `--highlight-pink` CSS custom
    properties added to `:root` in `style.css`
  - `notes/index.html` badge gains the color name; `.notes-item--highlighted` gains four modifier classes

- [ ] **H2. Notes search and filter** *(effort: 2–4 hours)*
  - `notes/index.html` currently renders `Object.keys(notes).sort()` with no search or filter
  - Add a search input above the export buttons; filters the rendered list in real-time using
    `element.textContent.toLowerCase().includes(q)` — no fetch needed (all notes in localStorage)
  - Filter chips: `All | Highlighted | Notes only`; uses CSS class toggling, not re-render
  - Sort control: `Ref order | Most recent | Oldest` — uses the `created` timestamp field already
    present in every `bsw_notes_v2` entry
  - Results count badge: "Showing 12 of 47 annotated verses"
  - All logic is inline `<script>` in `notes/index.html` following the existing render pattern

- [ ] **H3. Notes backup / restore (import JSON)** *(effort: 2–3 hours)*
  - The page has "Export JSON" but no import path; a user who clears storage or switches devices
    loses everything — the most serious data-loss risk in the current design
  - Add "Import from backup" button; clicking it opens a `<input type="file" accept=".json">`
    file picker (triggered via `.click()` — no visible input element)
  - Read via `FileReader.readAsText()`, parse JSON, validate shape, merge into `bsw_notes` without
    overwriting existing entries unless user checks a "Replace existing" checkbox
  - `bsw_notes_v2` import: validate required fields; assign new `id` values; deduplicate by
    `(bookId, ch, v, text)` fingerprint
  - Show a summary toast after import: "Imported 34 notes, 12 highlights. 3 duplicates skipped."
  - Entirely client-side `FileReader` API; no server communication

- [ ] **H4. Verse tagging for personal organisation** *(stub — needs scoping before work begins)*
  - Users have no way to organise their notes and highlights beyond the existing filter chips
    (All / Highlighted / Notes only); a tagging system would let them build a personal topical
    index (e.g., #prayer, #promise, #warning, #sermon-notes)
  - Needs to determine: how tags are stored (extend `bsw_notes_v2` schema with a `tags: []`
    field), where tags are added and edited (inline in the notes page vs. in the verse popup),
    whether tags are free-text or chosen from a managed list, and how tag filtering interacts
    with the existing search and filter UI in H2
  - Related to I5 (memory verse tags) — consider a unified tagging system across both features

---

## Phase I — Advanced Content *(builds on existing data and infrastructure)*

- [ ] **I1. Catechism reading plans** *(effort: 3–5 hours)*
  - Reading plans exist for Bible reading but not for the catechisms in `library/` — a gap given
    that the Heidelberg Catechism (52 Lord's Days) and Westminster Shorter Catechism (107 Q&As)
    are structured for systematic reading
  - Add two new plan files using the exact existing plan JSON shape:
    - `data/plans/heidelberg-weekly.json` — 52 entries, one per Lord's Day:
      `{ "day": 1, "label": "Lord's Day 1", "questions": [1, 2], "href": "../../library/heidelberg-catechism/#ld1" }`
    - `data/plans/wsc-quarterly.json` — 13 weeks × ~8 Q&As; same shape
  - Register both in the plan-selector dropdown in `plans/index.html` and home page `#daily-plan-select`
    using existing `_plansGetState()` / `_plansDayNum()` infrastructure in `bible.js`
  - "Read" links navigate to `library/` anchors rather than the Bible Reader
  - Progress tracked in `bsw_plans` localStorage key — same key, same shape, zero migration needed
  - Add both new JSON files to `SHELL_URLS` in `sw.js` for offline support

- [ ] **I2. Library cross-document search** *(effort: 4–6 hours)*
  - Eleven library documents exist but there is no way to search across them; a user wondering
    "where do the confessions address the Lord's Supper?" must open each document individually
  - Build a `scripts/build-library-index.py` script that scrapes the 11 library HTML pages and
    emits `data/library/search-index.json`:
    ```json
    [
      { "doc": "WCF", "docSlug": "westminster-confession",
        "section": "29.1", "heading": "Of the Lord's Supper",
        "text": "Our Lord Jesus, in the night wherein he was betrayed…" }
    ]
    ```
  - Add a search input to `library/index.html` above the document grid; on input, fetch
    `data/library/search-index.json` (cached after first load), filter client-side, render results
    as `doc · section — heading` cards with matched phrase highlighted via existing `highlightMatch()`
  - Each result links to `library/{docSlug}/index.html#{section-anchor}`
  - The index file is small (~200 KB total for all 11 documents); committed and updated manually
    when document content changes

- [ ] **I3. Morphology parse code decoder** *(effort: 3–5 hours)*
  - Interlinear display (C2) and word study panel (B2) show parse codes verbatim (`V-AOR-ACT-IND-3S`,
    `Piel-PERF-3MS`) — meaningful only to readers who already know Greek or Hebrew grammar,
    defeating the purpose of providing interlinear data to lay students
  - **Part 1 — data:** extend the interlinear build script to include a `"m"` (parse code) field in
    each token; update `data/interlinear/*.json` (66 files); target token shape:
    `{ "s": "G25", "text": "loved", "m": "V-AAI-3S" }`
  - **Part 2 — decoder:** add `expandMorphCode(code)` in `bible.js` with inline look-up tables
    (~60 entries each for Greek and Hebrew); maps abbreviated segments to plain English:
    `"V-AAI-3S"` → `"Verb — Aorist Active Indicative — 3rd Person Singular"`
  - Wire into `_vsRenderWordPanel()` (pass `match.m` as the `morph` arg instead of `null`) and
    into `_riShowPopover()` in the interlinear grid popover
  - Display as a two-line block: abbreviated code on top, plain-English expansion below in muted text
  - Look-up tables are small enough to inline in `bible.js` — no new data file needed for Part 2

- [ ] **I4. Verse sharing / image card generator** *(effort: 5–8 hours)*
  - F2 (planned) handles plain-text clipboard copy; a shareable image card — verse text + reference
    in a designed layout, downloadable as PNG — is a qualitatively different and high-engagement
    sharing vector; no backend required (HTML Canvas API)
  - Add a "Share as image" action to the verse modal action bar and to the Verse Study page header
  - On click, open a canvas-based preview overlay (`.bsw-share-overlay`):
    - 1200×630 px canvas (standard OG image size)
    - 2–3 design presets (Light parchment / Dark slate / Minimal white) selectable via radio buttons
    - Verse text drawn with `ctx.fillText()` using a serif font; reference + version badge smaller below
    - "Download PNG" button: `canvas.toDataURL('image/png')` → temp `<a download="verse.png">` → `.click()` → `.remove()`
  - Font: load a ~40 KB base64-encoded Latin subset of a free serif (e.g., Crimson Text) via
    `FontFace` API before drawing — needed for consistent rendering across devices
  - CSS: `.bsw-share-overlay`, `.bsw-share-canvas`, `.bsw-share-preset-row` in `bible-ui.css`
  - **Dependency:** F2 (copy verse) should ship first as it establishes the action bar UI pattern

- [ ] **I5. Memory verse tags and Anki export** *(effort: 3–5 hours)*
  - The memory system (`bsw_memory`) is a flat object with no organization; users memorizing verses
    across multiple sermon series, books, and themes have no way to filter or group them
  - Add optional `tags: ["string"]` array to each `bsw_memory` entry — backward compatible,
    no migration needed (entries without `tags` treated as `[]`)
  - Browse panel in `memorize/index.html`: tag filter chips showing all tags in use; a "+" button
    and inline text input to add tags to any verse; tags normalized to lowercase-kebab-case
  - Review session scoping: `"Review: All | [tag]"` selector limits `_memIsDue()` checks to entries
    matching the selected tag
  - **Anki export:** "Export for Anki" button produces a `.txt` file in tab-separated format
    (`Front\tBack\n`) where Front = reference, Back = verse text fetched from the active cached version
    via `loadBook()`; download via `<a download>` pattern; works fully offline with cached data

---

## Phase J — Word Cloud *(priority: low — exploratory / visual)*

- [ ] **J1. Most-common-words word cloud** *(effort: 1–2 weeks)*
  - A visual word cloud of the most theologically significant words in the Bible, sized by frequency —
    an engaging entry point that surfaces what the Bible most talks about
  - **Word selection strategy:** not raw word frequency (which surfaces "the", "and", "LORD") but
    *meaningful* word frequency: for each English word in the active version, map it to its
    underlying Strong's lemma (using the interlinear data), then count lemma occurrences; this
    groups translation variants ("love", "loved", "loving" → G25 ἀγαπάω) into a single count
  - Stop-list: exclude articles, conjunctions, prepositions, and the divine name (or offer a
    toggle to include/exclude proper nouns like "God", "Lord", "Jesus", "Israel")
  - **Rendering:** SVG-based word cloud using a layout algorithm (D3-cloud or a pure-JS spiral
    layout implemented from scratch to avoid a framework dependency); words sized by `log(count)`
    to prevent the top words from overwhelming smaller ones
  - Clicking a word opens a panel showing: the Strong's entry (lemma, gloss, count), a sample
    of 5–10 key verses containing that word, and a link to the full Strong's concordance view
  - **Scope controls:** filter the cloud by book, testament, or genre (Law / History / Poetry /
    Prophecy / Gospels / Epistles) — recompute counts client-side from cached interlinear data
  - **Data:** uses existing `data/interlinear/` (66 books) and `data/strongs/` — no new data
    files required; computation runs once on page load and is memoized in a module-level cache
  - Hosted at `wordcloud/index.html`; linked from the main nav Tools group in `main.js`
  - **Effort note:** the spiral layout algorithm is the highest-effort part; using a prebuilt
    pure-JS layout library (MIT-licensed, no build step needed) is acceptable here

---

## Phase K — Bible Version Expansion via API *(priority: medium)*

- [ ] **K1. Add public-domain versions from wldeh/bible-api** *(effort: 3–5 days)*

  The `wldeh/bible-api` (<https://github.com/wldeh/bible-api>) provides structured JSON for many
  translations. Public-domain versions can be downloaded, committed to `data/bible/`, and served
  offline like the existing four.

  **Versions to commit locally (public domain — no redistribution restriction):**
  | ID | Name | Year | Attribution required |
  |----|------|------|----------------------|
  | YLT | Young's Literal Translation | 1898 | None |
  | DBY | Darby Translation | 1890 | None |
  | GNV | Geneva Bible | 1599 | None |
  | AKJV | American King James Version | ~2000 | None |
  | WEBBE | World English Bible British Edition | 2000 | None |

  **Process:**
  1. Review `wldeh/bible-api` data schema; write `scripts/fetch-versions.py` to pull and reformat
     each version into `data/bible/{VERSION}/{bookId}.json` matching the existing shape
  2. Commit new version directories; add entries to `data/versions/versions.json`
  3. Add new paths to `SHELL_URLS` in `sw.js` (tier-2 cache — pre-fetch after first load, not
     during install, since each version adds ~10–12 MB)
  - **UI:** no version-picker code changes needed — it already reads `versions.json` dynamically

---

## Phase L — Accessibility & Internationalisation *(stub phase — all items need scoping)*

All items in this phase are stubs. They were identified as gaps during a gap analysis but have
not yet been researched or scoped. Do not begin work on any item until it has been expanded
from stub form with concrete implementation details.

- [ ] **L1. High-contrast mode** *(stub — needs scoping before work begins)*
  - No high-contrast mode exists; users with low vision who rely on high-contrast system themes
    may find the current colour scheme insufficient
  - Needs to determine: whether `@media (prefers-contrast: high)` is sufficient or if a manual
    toggle is needed, which colour-pair combinations need attention (text on scripture block
    backgrounds, link colours, secondary text), and whether this is part of F0 (accessibility
    audit) or a separate deliverable

- [ ] **L2. Full keyboard navigation parity** *(stub — see also F0, F1a)*
  - Umbrella item for ensuring every feature is reachable keyboard-only; specifically the
    verse popup menu, the interlinear word panel, and all modal dialogs
  - Needs to determine scope after F0 audit results are known; this item should not be started
    before F0 is complete

- [ ] **L3. Internationalisation (i18n) framework** *(stub — likely out of scope for now)*
  - All UI chrome is hardcoded English; no plan exists for Spanish, French, German, or other
    language UI translations
  - Needs to determine: whether i18n is in scope at all for this personal project, and if so,
    what framework approach works without a build step (a simple JSON locale file + a
    `t('key')` helper would be sufficient)
  - Note: Bible text is already multi-version (and MKT adds an original translation); i18n
    here refers only to UI labels, not Bible content

- [ ] **L4. Font size and display controls validation** *(stub — see F3)*
  - F3 adds a font size toggle for the Reader and Verse Study, but it has not been validated
    that the preference scales correctly through all affected elements: interlinear word grid,
    Strong's flyout, verse modal, commentary panel, and mobile layout
  - Needs to determine: which CSS custom property controls font size in each context, and
    whether a single `--reader-font-size` variable is sufficient or if multiple variables
    are needed

---

## Phase M — Infrastructure, DevOps & Performance *(stub phase — all items need scoping)*

These items address operational and technical health. None of them are user-visible features
but all of them reduce risk. All are stubs requiring further research before work begins.

- [ ] **M1. Data build and deployment pipeline documentation** *(stub — needs scoping before work begins)*
  - The Python scripts in `scripts/` fetch and transform upstream data (Bible text, interlinear,
    Strong's, commentaries) but there is no documented process for when to run them, in what
    order, how to validate output, or how changes are committed and deployed
  - Needs to determine: which scripts exist and what each does, what the expected run frequency
    is (one-time setup vs. periodic re-sync), and whether a simple README in `scripts/` is
    sufficient or if a Makefile / CI step is warranted

- [ ] **M2. Upstream data source version pinning and re-sync strategy** *(stub — needs scoping before work begins)*
  - `data/interlinear/`, `data/strongs/`, and `data/commentary/` are sourced from external
    GitHub repos (`morphgnt/sblgnt`, `openscriptures/morphhb`, etc.) but the specific commit
    hashes used are not recorded anywhere; if those repos update, re-sync is done blind
  - Needs to determine: how to pin each source to a specific commit or release tag, where to
    record those pins (a `data/SOURCES.md` file is a simple option), and what the re-sync
    process looks like when an upstream source publishes a correction

- [ ] **M3. Data file completeness validation** *(stub — needs scoping before work begins)*
  - Commentary data and interlinear data may have gaps (missing books, missing verses, missing
    tokens) that are not surfaced to the user in any meaningful way — they just see blank sections
  - Needs to determine: what a validation script should check (all 66 books present, all
    chapters, verse count vs. expected), what the output format should be, and whether this
    runs as a one-time check or a CI gate

- [ ] **M4. Search performance profiling** *(stub — needs scoping before work begins)*
  - Full-text search runs client-side against all cached Bible JSON; for large result sets or
    slow devices, this could be noticeably slow, but no profiling has been done
  - Needs to determine: what the worst-case query looks like (single-word common term across
    all versions), how to measure it, and what an acceptable response time threshold is

- [ ] **M5. `bible.js` modularisation plan** *(stub — likely long-term)*
  - `bible.js` is 2000+ lines and growing; it handles verse rendering, modal system, tooltips,
    version switching, commentary, Strong's, interlinear, notes, bookmarks, memory, and plans
  - This is real technical debt but low urgency on a no-build static site; splitting it requires
    either ES module imports (which need a server for local dev or a bundler) or a simple
    script-load sequence
  - Needs to determine: whether the no-build constraint can be relaxed (even a simple
    concatenation step via a shell script would suffice), and which logical boundaries are
    cleanest to split on first (verse-modal.js, reader-keyboard.js, etc.)

- [ ] **M6. `data/references/` directory clarification** *(stub — immediate low-effort clarification needed)*
  - A `data/references/` directory exists in the repo but is not mentioned anywhere in the TODO,
    CLAUDE.md, or any HTML or JS file found during the gap analysis; its purpose is unknown
  - Action needed: inspect its contents, determine if it is used, unused, or a placeholder;
    either document it in the Notes section or delete it if orphaned

---

## Phase N — Engagement & Content Depth *(stub phase — all items need scoping)*

These are features that drive regular use and deepen the study experience. All are stubs.

- [ ] **N1. Reading streaks and engagement tracking** *(stub — needs scoping before work begins)*
  - No streak or habit-tracking feature exists; YouVersion's dominant retention mechanic is a
    daily reading streak with a visible counter and a "don't break the chain" nudge
  - Needs to determine: what counts as a "reading day" (any Reader visit? a minimum verse count?
    a plan completion?), where the streak counter displays (home page widget, header badge),
    and whether achievements/badges are in scope or just the streak count
  - Related to C3a (reading plan progress) — streaks and plan progress are often shown together

- [ ] **N2. Prayer journal** *(stub — needs scoping before work begins)*
  - Users want to log prayers alongside Scripture, separate from verse-level notes; a day-keyed
    journal where each entry can link to one or more Bible references
  - Needs to determine: storage key and schema (separate from `bsw_notes`), UI location
    (`journal/index.html` vs. embedded in the home page), whether entries can be linked to
    verses (`.ref` pattern), and whether this is a standalone feature or part of a broader
    devotional flow with Spurgeon (D6) and VOTD (D7)

- [ ] **N3. Study guide / curriculum templates** *(stub — needs scoping before work begins)*
  - No structured multi-session study format exists; a study guide would be a series of
    guided questions tied to Bible passages — more structured than reading plans, less
    open-ended than the current topic pages
  - Needs to determine: data format (JSON or HTML), authoring workflow, how they differ
    from the existing `topics/` pages, and whether they are personal (like plans) or
    published as site content

- [ ] **N4. First-visit onboarding experience** *(stub — needs scoping before work begins)*
  - A brand new visitor sees no guidance on what the site offers or where to start; there is
    no welcome flow, no feature tour, and no help overlay beyond the keyboard shortcut modal (F8)
  - Needs to determine: what the onboarding goal is (get the user to read one verse? enroll
    in a plan? understand the tools?), whether this is a modal wizard, a guided tour overlay,
    or a dedicated landing page, and whether it fires once (first visit) or is accessible later

- [ ] **N5. Commentary citation and passage export** *(stub — needs scoping before work begins)*
  - No way exists to copy a passage plus its commentary as a formatted block for sermon prep,
    journaling, or sharing; the current Copy action (F2) only copies the verse text
  - Needs to determine: what formats are useful (plain text block, Markdown, RTF for Word),
    which commentary sources are included in an export, and how citation formatting works
    (which style: Chicago, Turabian, informal?)

---

## Phase O — Long-term / Deferred *(stub phase — intentionally deprioritised)*

These items have been identified but are intentionally deferred. They require significant
research, have unclear scope, or are likely out of scope for a personal static-site project.
Recorded here so they are not forgotten, but none should be started without deliberate
re-evaluation.

- [ ] **O1. Audio support for memory verses** *(stub — deferred)*
  - TTS integration or royalty-free audio recordings for Scripture memory (C4) so verses can
    be heard while commuting; no clear path on a static site without a TTS API dependency

- [ ] **O2. Apocrypha / deuterocanonical books** *(stub — deferred)*
  - The site targets the 66-book Protestant canon; adding Tobit, Maccabees, etc. would
    require interlinear data, Strong's coverage, and version picker changes; no current plan

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

- [ ] **Z0. MKT Translation Workshop — a personal Hebrew and Greek mastery tool** *(effort: 3–5 weeks for the tool; ongoing as you use it)*

  The Workshop is built before any verse is translated. It is the human-in-the-loop interface
  for everything in Z1: every glossary entry the AI proposes passes through it, you confirm or
  correct it, and the process of doing so is designed to make you progressively fluent in reading
  Biblical Hebrew and Greek — not just as an editor signing off on AI decisions, but as someone
  who understands *why* each decision was made.

  Hosted at `translation/workshop/index.html`. Not linked in the public nav — a private tool.
  All decisions written to `data/translation/glossary-*.json` and
  `data/translation/glossary-phrases-*.json` with a `status` field; the translation script
  (Z1 Step 2) only consumes entries with `status: "confirmed"` or `"locked"`.

  ---

  ### The Lexical Dossier — what you see for each word or phrase

  Every item in the review queue opens a full **Lexical Dossier** panel. For a single lemma
  (e.g. ἀγάπη / G26):

  **1. The word itself**
  - Lemma in original script with full Unicode rendering
  - Pronunciation guide (transliteration + IPA approximation)
  - Part of speech, gender/number pattern (for nouns), principal parts (for verbs)
  - Root etymology: what the word is built from, what cognates exist in Aramaic / Ugaritic /
    Arabic / LXX Greek; etymological chain rendered as a small visual tree
  - **Frequency panel:** how many times it appears in the OT/NT, breakdown by book, by author,
    by genre — rendered as a small bar chart so you can see at a glance whether this is a
    Pauline signature word, an OT poetic term, or a word Jesus uses rarely but significantly

  **2. Lexical source evidence — side by side**
  Each public-domain source gets its own collapsible column so you can read them in parallel:
  | Source | What it contributes |
  |--------|---------------------|
  | Dodson (CC0) | Concise NT gloss — the AI's starting point |
  | Thayer (1889) | Extended semantic range, NT usage patterns, LXX cross-refs |
  | Vine (1940) | Theological usage notes, near-synonym distinctions |
  | Moulton & Milligan (1930) | Papyri attestations — how the word was used by ordinary people in 1st-century letters, contracts, and receipts; often the most illuminating column |
  | Liddell-Scott (abridged) | Classical/secular Greek range; shows where NT usage departs or aligns |
  | Robertson's Word Pictures | Phrase and construction notes; syntactic edge cases |
  | BDB (Hebrew) | Contextual usage categories — BDB breaks each lemma into numbered senses with OT examples |
  | Gesenius (Hebrew) | Etymology, cognate-language attestations, semantic history |

  **3. Semantic range map**
  A simple visual — a horizontal bar divided into the word's attested English ranges with
  approximate proportional width based on LXX + NT usage frequency. Shows you the word's
  "center of gravity" and how far the tiers are pulling from it.

  Example for σάρξ (G4561):

  ```
  ←── body/flesh (physical) ──── human nature (general) ──── sinful nature (Pauline) ──→
       [████████████████]          [████████████]               [█████████████████████]
       Gospels / literal           General epistles              Romans / Galatians
  ```

  **4. The AI's proposed renderings**
  Three-tier proposal with explicit reasoning for each:
  ```
  Literal:    "flesh"
  Reasoning:  Source term is physical-body in all pre-Pauline uses; literal tier should
              preserve the shock of Paul repurposing it. Departing here would over-interpret.

  Mediating:  "flesh / sinful nature"  [context-split via context_override]
  Reasoning:  BDB/Thayer both note the Pauline ethical sense is distinct; mediating tier
              uses context_override: physical-body contexts → "flesh", soteriological
              contexts (Rom 6–8, Gal 5) → "sinful nature".

  Thought:    "our fallen human nature"
  Reasoning:  NLT-style; Moulton & Milligan shows σάρξ in papyri never has ethical freight —
              so MKT-T makes the Pauline extension explicit rather than leaving it to the reader.
  ```

  **5. Phrase context viewer**
  Every verse containing this lemma is listed with the surrounding 3–5 words highlighted.
  Click any verse to open it in the Reader alongside the interlinear. This is the fastest
  way to develop intuition — seeing the word in every context it appears, not just definitions.
  Filter by book, testament, author, or genre to compare usage patterns.

  **6. LXX bridge panel** *(Hebrew lemmas only, and Greek lemmas with LXX attestations)*
  - Which Hebrew word(s) does the LXX translate this Greek word with? (or vice versa)
  - What does that Hebrew/Greek cognate mean? (cross-links to its own dossier)
  - Why does this matter for the NT rendering? The AI explains the semantic inheritance chain.
  - Example shown visually: `חֶסֶד (H2617) → LXX: ἔλεος (G1656) → NT: mercy/lovingkindness gap`

  **7. Related lemmas**
  Near-synonyms and semantic-field neighbors, each with a one-line contrast note:
  - ἀγάπη vs. φιλία vs. ἔρως: "ἀγάπη: willed commitment · φιλία: warm affection · ἔρως: desire (absent from NT)"
  - Links to each related dossier; reviewing a semantic cluster together is faster and more
    effective than reviewing words in isolation

  ---

  ### Your actions on each entry

  Every dossier has an action bar at the bottom. You are not just approving — you are
  participating in the translation:

  **Confirm** — accept the AI's proposed renderings and reasoning as-is; entry moves to
  `status: "confirmed"`; the AI logs your confirmation as a signal that its reasoning was sound

  **Override** — change one or more tiers; a required free-text field asks for your reasoning
  (1–3 sentences minimum); your reasoning is stored in the glossary entry alongside the AI's
  and displayed to you again during Step 3 consistency review

  **Inform** — you have context the AI lacks; open a dialogue input:
  *"The Moulton & Milligan entry for [X] shows a papyrus from AD 50 where this word means…"*
  or *"In my reading of Romans 7, Paul seems to be doing something specific here that changes
  this rendering…"* — the AI responds with a revised proposal and its updated reasoning; you
  can go back and forth as many times as needed before confirming

  **Dispute** — flag the entry as genuinely contested; it joins the human-priority review queue
  and also appears in the contested-terms table (Z1) so it gets extra attention before Step 2

  **Defer** — skip for now; entry stays `status: "draft"`; deferred entries form a revisit queue
  shown on the dashboard

  **Lock** — after confirming, mark a rendering as final; locked entries are never touched by
  the consistency checker (Step 3) or by future AI re-draft passes; use for entries where you
  have high confidence

  ---

  ### The learning architecture

  The Workshop is sequenced to build your knowledge systematically, not dump everything at once:

  **Phase 1 — The 200 most frequent NT Greek lemmas** *(covers ~80% of all NT word occurrences)*
  Work through these first. After reviewing ~50 you will have internalized the basic vocabulary
  of the Pauline letters; after ~200 you can read slow NT Greek with a dictionary. The tool
  tracks your streak and estimates comprehension coverage as you go.

  **Phase 2 — The 200 most frequent OT Hebrew lemmas** *(covers ~75% of all OT word occurrences)*
  Same approach. Hebrew root patterns (binyanim) are explained as you encounter them — the tool
  recognizes when you've just seen the Qal stem of a root and flags the related Hiphil/Niphal
  forms you'll encounter soon, so you build paradigm intuition alongside vocabulary.

  **Phase 3 — Semantic clusters**
  After frequency coverage, work by semantic domain: all emotion words together, all
  covenantal terms together, all eschatological terms together. The cluster view shows the
  full semantic field at once so you can see the distinctions between near-synonyms in context.

  **Phase 4 — Phrase glossary**
  Hebrew idioms and Greek constructions reviewed after the underlying lemmas are familiar.
  The Inform action is especially valuable here — idioms often have a compelling story behind
  them (why does "lift up the face" mean favor? what does the Semitic background of "son of"
  constructions tell us?) and the AI is prepared to walk through it.

  **Phase 5 — Contested terms queue** *(dispute_level 3–4)*
  The 50–100 hardest decisions, reviewed last when you have the most context. The AI presents
  the full debate — every major translation's choice and the reasoning behind it — and you make
  a decision for MKT with your eyes open. These decisions are the most theologically
  significant choices in the entire translation.

  ---

  ### Progress dashboard

  The workshop home page shows:
  - Lemma coverage: `confirmed / total` per language, with a sparkline of daily pace
  - Domain coverage heatmap: which semantic domains are complete vs. outstanding
  - Disputed items: items flagged via Dispute action, sorted by dispute_level
  - Deferred queue: items you skipped, oldest first
  - Your decision log: a full journal of every Override and Inform exchange, searchable,
    becoming over time a personal commentary on your translation philosophy
  - Estimated "verse coverage" — what percentage of all Bible verses can now be translated
    using only confirmed glossary entries (starts at 0%; reaches ~90% after Phase 1+2)

  ---

  ### Data flow into Z1

  The Workshop is the gate:
  - `status: "draft"` — AI-proposed, not yet reviewed; translation script will not use these
  - `status: "confirmed"` — you accepted the AI's rendering; ready for Step 2
  - `status: "override"` — you changed the rendering; your version is used; AI reasoning
    replaced by your reasoning in the glossary file
  - `status: "locked"` — confirmed and frozen; consistency checker skips these
  - `status: "disputed"` — flagged for extra human review; Step 2 cannot proceed until all
    disputed entries in the contested-terms table are resolved

  The translation script (`scripts/translate-bible.py`) reads only `confirmed`, `override`,
  and `locked` entries. Running it before the glossary is complete produces a partial
  translation with clearly marked gaps — a useful intermediate state for testing the pipeline.

- [ ] **Z1. Generate the Modern Kingdom Translation (MKT) using the project's own source data** *(effort: 1–2 months)*

  The project already holds everything needed to produce a fully original, copyright-free English
  translation: the Westminster Leningrad Codex (Hebrew OT) and SBLGNT (Greek NT) with word-level
  morphological tagging and Strong's numbers are already committed in `data/interlinear/`. Both
  source datasets are CC-BY 4.0 — a translation produced from them is a new work owned outright
  by the author with no redistribution restriction.

  ### Translation philosophy — three tiers, one unified source

  Rather than committing to a single philosophy, MKT generates **three renderings per verse**
  from the same underlying glossary and interlinear source. The reader moves between them with
  a slider; the translation adapts rather than forcing the reader to switch versions.

  | Tier | ID | Philosophy | Comparable to |
  |------|----|------------|---------------|
  | 1 — Literal | `MKT-L` | Word-for-word; source syntax preserved as far as English allows; every lemma gets its primary glossary rendering; nothing added or softened | NASB95, YLT, Interlinear |
  | 2 — Mediating | `MKT-M` | Natural English sentence order; primary glossary renderings; idiomatic connectives; the default reading mode | BSB, ESV, NKJV |
  | 3 — Thought | `MKT-T` | Meaning-driven; glossary alternates used where they communicate more clearly; phrases rather than individual word mappings; poetic passages in contemporary cadence | NLT, The Message (register only) |

  All three tiers share:
  - The same glossary (same Strong's decisions for contested terms — the theology is identical)
  - The same expansion annotations (Z2 hover dots) — the semantic commentary does not change
    with the slider position
  - The same MKT commentary (Z3), written against MKT-M as the reference tier

  The slider is a **UI morphing mechanism**, not three separate Bibles — the reader experiences
  one coherent translation at a chosen level of interpretive distance from the source.

  ### Process

  **Step 1 — Build a shared translation glossary** *(~2–4 weeks — this is the foundation everything else rests on)*

  The glossary is the intellectual core of MKT. A naïve lemma-to-word mapping misses most of
  what makes Biblical language difficult: the same lemma means different things in different
  syntactic contexts; many key phrases are idiomatic (their meaning is not the sum of their
  parts); Greek and Hebrew each have semantic domains with no clean English equivalent; and some
  terms carry theological weight that a purely linguistic approach obscures. The glossary must
  handle all of this before a single verse is translated.

  #### Two glossary types

  **A. Lemma glossary** (`data/translation/glossary-greek.json`, `glossary-hebrew.json`)
  One entry per Strong's number. The full shape:
  ```json
  {
    "G26": {
      "lemma": "ἀγάπη",
      "pos": "noun",
      "domain": ["emotion", "relationship", "theology"],
      "dispute_level": 2,
      "tiers": {
        "literal":    { "primary": "love",             "notes": "retain when followed by genitive of object" },
        "mediating":  { "primary": "love",             "notes": null },
        "thought":    { "primary": "unconditional love","notes": "may expand to 'self-giving love' in narrative contexts" }
      },
      "context_overrides": [
        { "condition": "preceded by G2316 (θεός) as subject", "literal": "divine love", "thought": "God's self-giving love" },
        { "condition": "1 Cor 13 discourse", "thought": "love that never fails" }
      ],
      "related_lemmas": ["G5368", "G2309"],
      "semantic_range": "Self-giving, other-directed regard; encompasses both affection and commitment; broader than φιλία (warm friendship) and unrelated to ἔρως (desire). In LXX used to translate אַהֲבָה (H160).",
      "expansion": "ἀγάπη — self-giving, unconditional love; distinct from φιλία (affection) and ἔρως (desire)",
      "sources": ["dodson", "thayer", "vine", "lxx_link:H160"]
    }
  }
  ```

  Key fields:
  - `domain` — Louw-Nida-style semantic domain tags; used by the word cloud (J1) and search
    scope filters (G2) to group semantically related lemmas
  - `dispute_level` — 0 (uncontested) to 4 (major theological debate); drives the Z2 expansion
    dot rendering and the contested-terms review priority queue
  - `context_overrides` — explicit rendering decisions for specific syntactic environments;
    these take precedence over tier defaults during translation and are logged as intentional
    departures so the consistency checker (Step 3) does not flag them
  - `related_lemmas` — semantic field links; surfaces in the Strong's panel ("see also") and
    informs the word cloud lemma-grouping logic
  - `sources` — which lexical sources informed this entry; `lxx_link` connects Hebrew and Greek
    cognates across Testaments (e.g., the LXX bridge between ἀγάπη and אַהֲבָה)

  **B. Phrase glossary** (`data/translation/glossary-phrases-greek.json`, `glossary-phrases-hebrew.json`)
  One entry per idiomatic multi-word expression. These cannot be resolved by lemma lookup alone:
  ```json
  {
    "heb_lift_face": {
      "language": "hebrew",
      "tokens": ["H5375", "H6440"],
      "surface_example": "נָשָׂא פָנִים",
      "literal_form":    "lift up face",
      "mediating":       "show favor",
      "thought":         "accept with honor",
      "expansion":       "An idiom for granting favor or accepting someone; opposite of 'hiding the face' (divine rejection). Cf. Numbers 6:26.",
      "refs": ["Gen 4:7", "Num 6:26", "Job 22:26"],
      "sources": ["bdb", "gesenius"]
    },
    "grk_works_of_law": {
      "language": "greek",
      "tokens": ["G2041", "G3551"],
      "surface_example": "ἔργα νόμου",
      "literal_form":    "works of law",
      "mediating":       "works of the law",
      "thought":         "deeds done to earn standing before God",
      "expansion":       "Pauline phrase, central to Galatians and Romans. Debate: does it refer to (a) moral law generally, (b) Torah boundary markers (circumcision, food laws, calendar), or (c) any rule-keeping done for justification? MKT-T renders it as (c) in soteriological contexts; other contexts use mediating form.",
      "dispute_level": 4,
      "refs": ["Rom 3:20", "Gal 2:16", "Gal 3:2"],
      "sources": ["bdag_summary", "vine", "moulton_milligan"]
    }
  }
  ```

  Phrase entries are matched during translation before lemma lookup — a token sequence that
  matches a phrase entry uses the phrase rendering, not the individual lemma renderings. The
  translation script tracks which phrase entries fired per verse for the consistency log.

  #### Lexical sources to incorporate

  **Greek:**
  | Source | Status | What it adds |
  |--------|--------|--------------|
  | Dodson Greek Lexicon | CC0 — already in project (`data/strongs/greek.json`) | Baseline gloss per lemma |
  | Thayer's Greek-English Lexicon (1889) | Public domain | Extended semantic range notes, NT usage patterns, LXX cross-refs |
  | Vine's Expository Dictionary (1940) | Public domain | Theological usage notes, distinction between near-synonyms |
  | Moulton & Milligan — *Vocabulary of the Greek NT* (1930) | Public domain | Koine papyri attestations — shows how words were used in everyday 1st-century Greek, not just literary contexts |
  | Liddell-Scott-Jones abridged | Public domain (abridged ed.) | Classical/secular range to show where NT usage departs from or aligns with broader Greek |
  | Robertson's *Word Pictures in the NT* (1930) | Public domain | Phrase-level and syntactic commentary; excellent source for idiom and construction notes |
  | Vincent's *Word Studies in the NT* (1887) | Public domain | Already feeds commentary (D4); cross-mine for phrase glossary entries |

  **Hebrew:**
  | Source | Status | What it adds |
  |--------|--------|--------------|
  | Brown-Driver-Briggs (BDB, 1906) | Public domain — JSON via `openscriptures/strongs` | Gold-standard OT Hebrew lexicon; extensive contextual usage breakdowns per lemma |
  | Gesenius' Hebrew and Chaldee Lexicon (1857, Tregelles trans.) | Public domain | Etymology, cognate language attestations (Aramaic, Arabic, Ugaritic), semantic range evidence |
  | Jastrow *Dictionary of Talmud and Midrash* (1903) | Public domain | Post-biblical Hebrew/Aramaic usage; essential for late OT and intertestamental vocabulary drift |
  | TWOT entry summaries | Derivative fair-use summaries only | Theological significance of key terms; the primary data (BDB, Gesenius) is the source; TWOT is a cross-check |

  **Cross-Testament bridge:**
  - The Septuagint (LXX) is the key that connects Hebrew and Greek semantic ranges: when the
    LXX translates a Hebrew word with a specific Greek word, that Greek word inherits the Hebrew
    word's semantic freight in NT usage. Track these links in `lxx_link` fields of both glossaries.
  - Example: LXX translates חֶסֶד (H2617, *hesed*) with ἔλεος (G1656, *mercy*) ~170 times — so
    NT uses of ἔλεος carry the *hesed* overtones (covenantal loyalty, not just pity). The MKT-T
    tier should reflect this; MKT-L should not.

  #### Build process

  1. **Automated draft pass** — LLM processes every Strong's entry in both files plus the
     public-domain lexical sources (fed as context) and produces a draft glossary entry for each
     lemma; phrase candidates are flagged by the model where token sequences appear repeatedly
     with non-compositional meanings across the interlinear data
  2. **Phrase extraction script** — `scripts/extract-phrases.py` scans `data/interlinear/` for
     recurring multi-token sequences; cross-references against a seed list of known Hebrew and
     Greek idioms from Thayer, BDB, and Robertson to produce phrase glossary candidates
  3. **Human review** — glossary draft reviewed top-down by `dispute_level` (4 → 0); all
     `context_overrides` and phrase entries require explicit human sign-off before translation begins
  4. **Flag theologically contested terms** — ~50–100 lemmas at dispute_level 3–4 reviewed
     manually before the translation pass (see list below); their tier renderings locked before
     Step 2 starts so the model cannot drift on them

  **Step 2 — Translate verse-by-verse × 3 tiers** *(~$150–450 in API cost — 3× Z1 original)*
  - Three parallel LLM passes per verse, each with the same interlinear token array and the
    same glossary, but with a different rendering instruction:
    - `MKT-L`: *"Preserve source word order and morphology as closely as English syntax allows.
      Use only the `literal` glossary field. Do not add explanatory words."*
    - `MKT-M`: *"Natural English sentence flow. Use the `mediating` glossary field. Prefer
      accuracy over elegance; add connectives only where English requires them."*
    - `MKT-T`: *"Communicate the full meaning clearly to a modern reader. Use the `thought`
      glossary field. Rephrase idioms; render poetry with contemporary cadence. Do not
      change the theological content — only its expression."*
  - Script: `scripts/translate-bible.py` — extended to accept a `--tier` argument; three runs
    write to `data/translation/draft/literal/`, `mediating/`, `thought/`
  - Log every glossary departure for review (shared log across tiers)

  **Step 3 — Consistency pass** *(~1–2 days scripting)*
  - Run `scripts/check-consistency.py` against each tier independently; then a cross-tier diff
    that flags where MKT-T departs significantly from MKT-L on the same lemma (for human audit
    of whether the departure is intentional)

  **Step 4 — Human review** *(2–6 weeks depending on depth)*
  - Review all three tiers together for each contested passage — the three columns side by side
    reveal where the theology is being shaped by philosophy rather than source text
  - Prioritize: theologically contested terms, poetic books (Psalms, Job, Proverbs), the
    Prologue of John, the opening of Genesis
  - Spot-check at least one chapter per Bible book across all three tiers
  - Final sign-off before committing

  ### Theologically contested terms requiring manual decisions
  | Greek/Hebrew | Term | Key translation choices |
  |---|---|---|
  | G1342 δίκαιος | righteous / just | consistent rendering vs. context-split |
  | G1343 δικαιοσύνη | righteousness / justification | one word or two? |
  | G4561 σάρξ | flesh / sinful nature / body | literal vs. interpretive |
  | G166 αἰώνιος | eternal / everlasting / age-long | theological weight of "eternal" |
  | G3056 λόγος | Word / word / reason | John 1 capitalization |
  | G26 ἀγάπη | love / charity | KJV "charity" vs. modern "love" |
  | H430 אֱלֹהִים | God / gods / divine beings | context-sensitive? |
  | H7307 רוּחַ | spirit / Spirit / wind / breath | capitalization policy |
  | H2617 חֶסֶד | steadfast love / lovingkindness / mercy | no clean English equivalent |
  | H3068 יהוה | LORD / Yahweh / Jehovah | rendering of the divine name |

  ### Output

  **Data files:**
  - Three versioned directories: `data/bible/MKT-L/`, `data/bible/MKT-M/`, `data/bible/MKT-T/`
    each containing 66 book files in the standard shape
  - Shared glossary: `data/translation/glossary-greek.json` + `data/translation/glossary-hebrew.json`
    (all three tiers' renderings in each entry, as above)
  - All three committed; all three registered in `data/versions/versions.json`
  - License: CC0 — freely shareable, no attribution required

  **Version picker behavior:**
  - The three MKT tiers do not appear as three separate dropdown entries; selecting "MKT" in
    the version picker shows the Reader with the slider visible and defaults to MKT-M
  - The slider (`<input type="range" min="1" max="3">`) sits in the Reader header beneath the
    version label; dragging it swaps the displayed verse text client-side from the already-loaded
    tier data (no network request — all three tiers for the current chapter are loaded together)
  - Slider position saved to `localStorage` key `bsw_mkt_tier`; restored on next MKT session
  - Tier labels beneath the slider: **Literal · Mediating · Thought**

  **Integration points:**
  - Parallel reader and compare page: MKT appears once with a mini-slider per column, not as
    three separate version rows
  - Verse Study: all three tier texts shown stacked with tier labels, no slider (study context
    benefits from seeing all three at once)
  - Share / export: the active tier at time of share is what gets copied/exported; tier label
    included in the attribution line ("MKT · Mediating")
  - Translation notes page (`translation/index.html`): documents the three-tier philosophy, the
    glossary decisions for contested terms, and example verse comparisons across all three tiers

  ### Why this is worth doing
  - **No other translation tool does this** — a slider that morphs between literal, mediating,
    and thought-for-thought within one internally consistent translation is genuinely novel; it
    makes the exegetical decision visible rather than hiding it inside a publisher's philosophy
  - All three tiers share the same theological decisions for contested terms — the slider changes
    English expression, not doctrine; the reader can trust that MKT-L and MKT-T agree on the
    *meaning* of every verse, just not on how close to stay to the source syntax
  - Completely copyright-free; can be embedded, printed, or shared without legal friction
  - The Z2 expansion layer and Z3 commentary are always written against MKT-M, so switching
    tiers never orphans the reader from the study tools — everything stays aligned
  - The BSB was produced by a similar computer-assisted + human-review pipeline — this is not
    an unprecedented approach; the three-tier extension multiplies the API cost ~3× but the
    scripting and review infrastructure is otherwise identical
  - The infrastructure (source texts, Strong's data, scripting patterns) is already 80% present

- [ ] **Z2. Amplified-style semantic expansion layer for the MKT** *(effort: 2–4 weeks)*

  Alongside the primary MKT rendering, attach brief inline annotations to words and phrases where
  the Greek/Hebrew is semantically wider, theologically contested, or routinely obscured by single-
  word translation choices — giving the reader the exegetical conversation without leaving the verse.

  ### What "Amplified experience" means for MKT

  Unlike the AMP Bible's bracketed parentheticals embedded directly in verse text, MKT's approach
  is non-intrusive: the base translation reads clean; expansions appear on demand.

  - Each token flagged in the glossary as "contested" or "semantically rich" receives an
    `"expansion"` field alongside its primary rendering:
    ```json
    {
      "G26": {
        "primary": "love",
        "expansion": "ἀγάπη — self-giving, unconditional love; distinct from φιλία (affection) and ἔρως (desire)"
      }
    }
    ```
  - A `"notes"` array on the verse level (in `data/translation/draft/{bookId}.json`) captures
    phrase-level observations: ambiguities that span multiple tokens (e.g. "flesh" vs. "sinful nature"
    argument across a full sentence), textual variants, or translation philosophy departures

  ### Rendering in the UI

  - **Inline expansion dots**: contested words in the MKT display a subtle underline
    dot; hovering/tapping opens a small popover (reuses existing `.ref-tooltip` CSS class) showing
    the expansion text and alternate renderings
  - **"Study mode" toggle** in the Reader header: when on, all expansion annotations are shown
    inline beneath each verse in a muted smaller font — the closest equivalent to the printed
    Amplified Bible; when off, the verse reads as plain text
  - **Verse study page** (`verse-study/`): the expansion content surfaces automatically in the
    word panel alongside the existing Strong's / morphology data — no extra click needed
  - No new data files beyond what Z1 already produces; expansion data lives in the glossary and
    verse note arrays already planned

  ### Contested-phrase coverage priorities
  Seed the expansion layer starting with these high-yield passages before generalizing:
  - Romans 1–8 (δικαιοσύνη, σάρξ, πνεῦμα throughout)
  - John 1:1–18 (λόγος, θεός, μονογενής)
  - Genesis 1–3 (בָּרָא vs. יָצַר, רוּחַ, נֶפֶשׁ)
  - The Sermon on the Mount (μακάριος, πτωχοὶ τῷ πνεύματι)
  - Hebrews 1–4 (ὑπόστασις, χαρακτήρ, κατάπαυσις)

- [ ] **Z3. MKT Custom Commentary** *(effort: 2–6 months, ongoing)*

  A purpose-built verse-by-verse commentary written to accompany the Modern Kingdom Translation.
  Unlike the existing public-domain commentaries (Matthew Henry, Barnes, JFB) which were written
  against KJV and reflect 17th–19th century concerns, the MKT commentary is written:
  - Against the MKT text specifically (cross-references its glossary decisions)
  - In contemporary English, assuming a reader who wants to understand the text, not impress anyone
  - With explicit integration of the Strong's/morphological data already in the project
  - Reformed/evangelical in theological orientation, but noting where other traditions read differently

  ### Data shape

  Reuses the existing commentary data schema in `data/commentaries/` (verse-keyed JSON):
  ```json
  {
    "John.3.16": {
      "source": "MKT",
      "text": "...",
      "glossary_refs": ["G3779", "G26", "G3439"],
      "cross_refs": ["Rom 5:8", "1 John 4:9"]
    }
  }
  ```
  A new source key `"MKT"` added to the commentary selector dropdown; displays alongside or
  instead of the existing public-domain sources.

  ### Generation pipeline (LLM-assisted, human-edited)

  **Step 1 — Draft pass** *(~$100–300 API cost for full Bible)*
  - Per-verse prompt: feed the MKT text, the expansion layer annotations (Z2), relevant
    Strong's entries, cross-references, and the glossary decisions that shaped this verse
  - LLM produces a 2–5 sentence explanatory note: what the verse says, why the translation choices
    were made, what the reader should carry forward
  - Script: `scripts/generate-commentary.py` — writes `data/commentaries/bsw-draft/{bookId}.json`

  **Step 2 — Theological review pass** *(human)*
  - Flag any verse where the draft commentary takes a contested theological position without
    acknowledging it; revise to note the tension rather than resolve it silently
  - Prioritize: the contested-terms table from Z1, soteriological passages, eschatology, the
    Johannine "I AM" sayings, the Olivet Discourse

  **Step 3 — Cross-commentary diff** *(tooling)*
  - `scripts/compare-commentaries.py` — for each verse, print MKT commentary alongside MHC and
    Barnes side by side; flag substantive disagreements for human attention
  - Goal: not to harmonize, but to ensure the MKT commentary is aware of where it diverges

  **Step 4 — Commit and integrate**
  - Merge reviewed files into `data/commentaries/mkt.json` (one combined file, book-keyed)
  - Register in the commentary source list; the existing `_vsShowCommentary()` UI handles display
    with no changes required

  ### Long-term: community annotation layer
  If the project ever adds any server component (even a lightweight write-only endpoint), the MKT
  commentary could accept reader-submitted paragraph-level corrections or alternate readings — a
  lightweight crowd-annotation layer on top of the generated base. Out of scope for the static-only
  MVP but worth designing the data shape to accommodate (a `"contributions": []` array per verse).

- [ ] **Z4. MKT versioning and update strategy** *(stub — needs scoping before work begins)*
  - Z1 produces MKT v1.0; corrections discovered after release (better glossary choice,
    consistency error, exegetical improvement) need a versioning scheme that does not
    silently change what users have bookmarked, annotated, or memorised
  - Needs to determine: whether MKT uses semantic versioning (v1.0 / v1.1 / v2.0), whether
    the glossary versions independently from the translated text, how users are notified of
    updates, and whether old cached MKT data is replaced automatically or requires user action
  - Also covers: whether MKT-L / MKT-M / MKT-T each have independent version numbers or
    always update as a set

- [ ] **Z3a. MKT commentary tier behaviour** *(stub — needs scoping before work begins)*
  - Z3 generates commentary written against MKT-M (the mediating tier); the behaviour when
    the slider is at MKT-L or MKT-T is undefined — does the commentary stay anchored to
    MKT-M text regardless of slider position, or does it shift?
  - Needs to determine: whether the commentary panel shows a "Commentary written against
    MKT-M" disclaimer when another tier is active, whether any commentary notes are
    tier-specific, and whether the Verse Study page shows all three tier texts stacked even
    when commentary is open

- [ ] **Z1a. MKT public-facing landing page** *(stub — needs scoping before work begins)*
  - Z1 references `translation/index.html` as a translation notes page, but its content,
    audience, and depth have not been designed; it could be a brief philosophy statement or
    a full academic methodology page
  - Needs to determine: who the intended reader is (curious visitor vs. serious scholar),
    what sections to include (three-tier philosophy, contested-terms decisions, example verse
    comparisons, glossary methodology, licensing), and whether this page is linked from the
    main nav or only discoverable via search/direct link

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
- **`data/references/` directory** — purpose currently unknown; see M6 (stub) to clarify or remove
- **Upstream data pins** — specific commit hashes for `morphgnt/sblgnt`, `openscriptures/morphhb`, `openscriptures/strongs`, and `openscriptures/nave` are not recorded; see M2 (stub) to address this
