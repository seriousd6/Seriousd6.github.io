# Bible Study Website — Site Overview

*Generated 2026-06-06. Update this file whenever major new features land or the architecture shifts.*

---

## What It Is

A personal Bible study reference site hosted on GitHub Pages. Single-owner, static-file application —
no server, no framework, no build step — that has grown into a full-featured study environment covering
the entire canon (including Apocrypha) with 16 core translations + 3 MKT variants + 4 apocrypha versions,
11 commentary sources, 4 Bible dictionaries, rich topical and reference resources, commentary, word study,
topical articles, study guides, daily discipline tracking, and a library of historical Christian documents.

**Live URL:** https://seriousd6.github.io  
**Repo root:** `c:\Users\Administrator\Documents\GitHub\Seriousd6.github.io`  
**Hosting:** GitHub Pages (static, serves from repo root)

---

## Technical Architecture

| Layer | Choice | Notes |
|---|---|---|
| Language | HTML + CSS + vanilla JS (ES Modules) | No framework, no transpiler |
| Data | ~20,000+ static JSON files | Fetched on demand, cache-first via SW |
| State | `localStorage` exclusively | ~50 named `bsw_*` keys |
| Tooling | ~1,952 Python scripts | Offline data generation only, never run on-site |
| Hosting | GitHub Pages | Static files from repo root |
| PWA | Service Worker (`sw.js`) | Network-first HTML, cache-first data/assets |
| Dark mode | CSS custom properties + `[data-theme="dark"]` | System preference respected |

### Module System

- **`main.js`** (non-module, loads sync): Builds the entire sidebar DOM from a static nav tree and a runtime
  fetch of `data/topics.json`. Manages sidebar collapse state. Must load before `app.js` so the
  `#bible-version` element exists for `populateVersionPicker()`.
- **`app.js`** (ES module entry): Imports 32 feature modules, wires cross-module callbacks,
  exposes `window.BibleUI`.
- **`core.js`**: Shared URL constants (`DATA_ROOT`, `COMMENTARY_ROOT`, etc.), book maps,
  `parseRef()`, `escHtml()`, `resolveVerses()`, version-change event system.

**All 32 JS modules in `assets/js/`:**
`apocrypha-reader`, `app`, `core`, `daily`, `discipline-strip`, `interlinear`, `lib-browser`,
`lib-progress`, `lib-reader`, `library`, `main`, `maps`, `modal`, `ol-companion`, `parallels`,
`places`, `pwa`, `reader`, `search`, `sg-progress`, `storage`, `store`, `terms`, `timelapse-map`,
`timeline`, `tooltip`, `tracker`, `verse-study`, `wire`, `word`, `wordcloud`, `workshop`

### Data Architecture

All Bible text, commentary, cross-refs, parallels, interlinear, Strong's, dictionary, topical index,
library documents, devotionals, timeline, and map data are flat JSON files fetched on demand.
No database, no API server.

```
data/bible/{VERSION}/{book}.json           ← 9 committed versions (KJV/BSB/WEB/ASV + 5 stub + MKT×3)
data/bible-apocrypha/{VERSION}/{book}.json ← 4 apocrypha versions (DR, WEB-CE, KJV-APO, BRENTON)
data/commentary/{book}.json               ← MHCC (root-level, Matthew Henry Complete Commentary)
data/commentary/{source}/{book}.json      ← 10 named sources (see Commentary Sources below)
data/crossrefs/{book}.json
data/interlinear/greek/{book}.json        ← NT Greek (SBLGNT)
data/interlinear/hebrew/{book}.json       ← OT Hebrew (OpenScriptures MHB)
data/strongs/greek.json + hebrew.json     ← Strong's concordance + Dodson/BDB lexicons
data/strongs/gesenius.json                ← (planned) Gesenius' Hebrew-Chaldee Lexicon
data/strongs/abbott-smith.json            ← (planned) Abbott-Smith NT Greek Lexicon
data/topical/{topic}.json                 ← Nave's Topical Bible
data/torrey/torrey.json + verse-index/    ← Torrey's New Topical Textbook
data/dictionary/{term-slug}.json          ← Easton's Bible Dictionary (1897)
data/isbe/{slug}.json + verse-index/      ← ISBE (9,380 articles; 24,736 verse refs)
data/smith/{slug}.json                    ← Smith's Bible Dictionary (1884)
data/hitchcock/index.json                 ← Hitchcock's Bible Names
data/echoes/{book}.json                   ← OT–NT allusion data (type, target, note)
data/library/docs/{doc-id}.json           ← library document JSON exports
data/library/html/{doc-id}.html           ← library document raw HTML
data/library/index.json                   ← library document manifest
data/devotionals/spurgeon-morning.json    ← 365 entries
data/devotionals/spurgeon-evening.json    ← 365 entries
data/votd/{year}/{month}/{day}.json
data/timeline/events.json                 ← biblical timeline events
data/wordcloud/frequencies.json           ← word frequency data (generated from interlinear)
data/versions/versions.json              ← canonical version list
data/bible/books.json                    ← 66-book metadata
data/topics.json                         ← flat array of topic/study/book entries for nav
```

### Commentary Sources (11 total)

| Key | Name | Coverage |
|---|---|---|
| *(root-level)* | Matthew Henry Complete Commentary (MHCC) | Full Bible |
| `barnes` | Barnes' Notes | Full Bible |
| `calvin` | Calvin's Commentaries | Full Bible |
| `clarke` | Adam Clarke's Commentary | Full Bible |
| `ellicott` | Ellicott's Commentary for English Readers | Full Bible |
| `jfb` | Jamieson, Fausset & Brown | Full Bible |
| `mkt-christ` | MKT — Christ-focused | Full Bible |
| `mkt-context` | MKT — Historical Context | Full Bible |
| `mkt-original` | MKT — Original Language | Full Bible |
| `rwp` | Robertson's Word Pictures | NT only |
| `wesley` | Wesley's Explanatory Notes | Full Bible (64 books) |

### localStorage Keys (~50 keys)

| Key | Purpose |
|---|---|
| `bsw_version` | Selected Bible translation (default: BSB) |
| `bsw_apoc_version` | Selected Apocrypha translation |
| `bsw_theme` | light / dark |
| `bsw_sidebar` | collapsed / open |
| `bsw_sidebar_chapters` | Chapter list visibility in sidebar |
| `bsw_fontsize` | Reader font size preference |
| `bsw_wide_reader` | Wide reader mode toggle |
| `bsw_split_panel` | Split panel state in reader |
| `bsw_compare` | Compare panel version preference |
| `bsw_interlinear` | Interlinear toggle state |
| `bsw_parallels` | Parallel passages toggle state |
| `bsw_xref_notes` | Cross-reference / notes panel state in reader |
| `bsw_reader_comm_mode` | Reader commentary mode (inline/panel) |
| `bsw_comm_src` | Commentary source preference |
| `bsw_reader_resume_dismissed` | Resume reading prompt dismissed flag |
| `bsw_notes_v2` | Timestamped verse notes (current format) |
| `bsw_notes` | Verse notes v1 (migrated to v2) |
| `bsw_notes_v2_migrated` | Migration flag |
| `bsw_bookmarks` | Bookmarked verses |
| `bsw_chapter_read` | Reading history (chapter → date) |
| `bsw_history` | Reader navigation history (recent refs) |
| `bsw_streak` | Reading streak data (ISO date array) |
| `bsw_plans` | Reading plan state |
| `bsw_daily_plan` | Active daily plan ID |
| `bsw_daily_start_` | Plan start date (prefix + plan ID) |
| `bsw_daily_devot` | Daily devotional completion state |
| `bsw_daily_notif` | Daily notification preference |
| `bsw_daily_notif_dismissed` | Notification prompt dismissed |
| `bsw_devot_period` | Morning / evening devotional period |
| `bsw_lib_progress` | Library reading history (doc → section) |
| `bsw_lib_complete` | Completed library documents |
| `bsw_lib_filters` | Library browser filter state |
| `bsw_lbpos_` | Library browser scroll position (prefix + doc ID) |
| `bsw_sg_progress` | Study guide session completion |
| `bsw_tracker` | Daily discipline checklist state |
| `bsw_fasting` | Fasting tracker |
| `bsw_memory` | Spaced repetition verse data |
| `bsw_memory_mode` | SRS mode (cards/list) |
| `bsw_journal` | Prayer journal entries |
| `bsw_gratitude` | Gratitude journal entries |
| `bsw_reflections` | Reflection journal entries |
| `bsw_worship` | Worship notes entries |
| `bsw_search_history` | Recent searches |
| `bsw_search_sort` | Search sort preference |
| `bsw_explore_tab` | Active tab in Explore hub |
| `bsw_wc_show` | Word cloud display setting |
| `bsw_tl` | Timeline position / filter state |
| `bsw_chtl` | Church history timeline state |
| `bsw_map_note_` | Map annotation notes (prefix + map ID) |
| `bsw_dissect_ctx` | Verse Study context/dissect state |
| `bsw_ws_decisions` | Translation Workshop decisions |
| `bsw_ws_ui` | Translation Workshop UI state |
| `bsw_storage_v` | Storage schema version (migration tracking) |
| `bsw_onboarded` | PWA onboarding completed flag |

---

## Page Map

### Primary Navigation (sidebar top links)
| Route | Title | Purpose |
|---|---|---|
| `/read/` | The Holy Bible | Multi-version reader, interlinear, compare, commentary |
| `/apocrypha/` | Apocrypha Reader | Deuterocanonical books reader |
| `/search/` | Explore Hub | Verse search, omni-search, topic browser, word cloud, dictionary |
| `/studies/` | Studies Hub | Topics, book studies, and study guides index |
| `/discipline/` | Discipline Hub | Reading plans, devotionals, memory, tracker, journals |

### Reader Sub-Pages
| Route | Title | Purpose |
|---|---|---|
| `/compare/` | All Translations | Multi-version comparison view for a passage |

### Studies & Content
| Route | Title | Purpose |
|---|---|---|
| `/verse-study/` | Verse Study | Single-verse deep research |
| `/word/` | Word Study | Greek/Hebrew word lookup, morphology, all occurrences |
| `/topics/` | Topics Index | Entry point to topical articles and book studies |
| `/topics/{slug}/` | Topic Page | Individual topical article or book study |
| `/study-guides/` | Study Guides Index | Multi-session study guide listing |
| `/study-guides/{slug}/` | Study Guide | Multi-session tabbed study guide |

### Library & History
| Route | Title | Purpose |
|---|---|---|
| `/library/` | Library Browser | Historical documents browser |
| `/library/read/` | Library Reader | Document reading view |
| `/library/progress/` | Library Progress | Reading history and completion tracking |
| `/history/` | History Hub | Entry hub for timeline, church history, maps |
| `/timeline/` | Biblical Timeline | Biblical events timeline |
| `/church-history/` | Church History Timeline | Post-canon church history timeline |
| `/maps/` | Maps | Static biblical geography maps |
| `/maps/timelapse/` | Animated History Map | Animated territorial / empire timelapse |

### Discipline Sub-Pages (some are redirect aliases)
| Route | Title | Purpose |
|---|---|---|
| `/memorize/` | *(redirect → discipline)* | Scripture memory via spaced repetition |
| `/plans/` | *(redirect → discipline)* | Reading plan management |
| `/devotionals/` | *(redirect → discipline)* | Daily devotionals |
| `/reflections/` | *(redirect → discipline)* | Reflection journal |
| `/worship/` | *(redirect → discipline)* | Worship notes |
| `/tracker/` | Discipline History | Streak and checklist history |

### Personal Notes & Progress
| Route | Title | Purpose |
|---|---|---|
| `/notes/` | My Study | Verse notes and annotations viewer |
| `/bookmarks/` | Bookmarks | Saved verse bookmarks |
| `/progress/` | Reading Progress | Chapter reading history and statistics |
| `/journal/` | Prayer Journal | Prayer and free-form journal writing |

### Specialized Tools
| Route | Title | Purpose |
|---|---|---|
| `/word/` | Word Study | Lemma lookup, morphological distribution |
| `/wordcloud/` | Word Cloud | Frequency visualization by book/scope |
| `/dictionary/` | Bible Reference | ISBE + Easton + Smith + Hitchcock dictionary browser |
| `/translation/workshop/` | Translation Workshop | MKT literal/mediating/thought comparison |

---

## Feature Inventory

### Core Loop (daily use)

1. **Bible Reader** (`/read/`)
   - 16 core translations (KJV, BSB, WEB, ASV + 5 stub versions + MKT×3) + 4 apocrypha versions
   - Flexible ref lookup: `John 3:16`, `Romans 8`, `Gen 1; John 1:1–14`
   - Keyboard navigation (j/k for next/prev chapter)
   - Cross-reference panel, compare mode, interlinear Hebrew/Greek toggle, parallel passages
   - Inline commentary panel (11 sources, switchable)
   - Highlight & notes (local), bookmarks, reading history, streak tracking
   - Wide/split reader modes, font size control

2. **Verse Modal** (triggered by any `.ref` click)
   - Tabs: Verse text, Cross-refs, Commentary (11 sources), Word Study, Topics, Confessions, Echoes
   - Actions: highlight, note, bookmark, memorize, copy, share as image, print
   - Auto-tagged theological terms (links to Dictionary)
   - Auto-tagged place names (links to Maps)

3. **Daily Discipline Hub** (`/discipline/`)
   - Reading plans (configurable start date)
   - Morning/Evening Spurgeon + Psalms + Proverbs + NT Daily devotionals
   - Spaced-repetition Scripture memory (SRS, card and list modes)
   - Prayer journal, reflections, gratitude, worship notes
   - Discipline streak tracking (daily checklist)
   - Fasting tracker

4. **Homepage** (`/`)
   - Time-based greeting, today's date
   - Quick verse lookup (jumps to `/read/`)
   - Verse of the Day
   - Reading plan for today
   - Devotional carousel
   - Disciplines tracker (checklist with links to hub)
   - In-progress study guides card
   - Continue Reading card (library history + book suggestions)

### Study Depth Features

5. **Verse Study** (`/verse-study/`) — Single-verse research: text, cross-refs, commentary (11 sources),
   parallels, echoes, word study in one page

6. **Word Study** (`/word/`) — Lemma lookup, morphological distribution, all occurrences across Bible

7. **Topics** (`/topics/`) — 7 topical articles + 3 book studies + 1 sermon series:
   - Topical: Prayer, Justification, Holy Spirit, Covenants, Christology, Holy Catholic Church, The Psalms
   - Book studies: Revelation, Romans, Sermon on the Mount

8. **Study Guides** (`/study-guides/`) — 5 multi-session guides:
   Hebrews (14 sessions), Romans 1–8 (9 sessions), Ephesians (7 sessions), Psalms (4-week devotional),
   Sermon on the Mount (6 sessions). Tabbed sessions with discussion questions.

9. **Search & Explore** (`/search/`) — Verse search with filters, omni-search, topic browser,
   dictionary, word cloud entry point

10. **Studies Hub** (`/studies/`) — Single index page combining all topics, book studies, and study guides

### Reference Resources

11. **Library** (`/library/`) — Historical documents: creeds, confessions, church fathers,
    Reformation works, papal encyclicals, liturgical texts, medieval mystical texts; reading progress tracked

12. **History Hub** (`/history/`) — Entry hub for biblical timeline, church history, maps

13. **Biblical Timeline** (`/timeline/`) — Interactive biblical events timeline

14. **Church History Timeline** (`/church-history/`) — Post-canon church history events

15. **Maps** (`/maps/`) — 15+ static biblical geography maps

16. **Timelapse Map** (`/maps/timelapse/`) — Animated territorial / empire history

17. **Translation Workshop** (`/translation/workshop/`) — Side-by-side MKT literal/mediating/thought comparison

18. **Apocrypha** (`/apocrypha/`) — Full reader for deuterocanonical books (4 versions)

19. **Bible Reference / Dictionary** (`/dictionary/`) — Integrated ISBE (9,380 entries) +
    Easton's (1897) + Smith's (1884) + Hitchcock's Bible Names

20. **Word Cloud** (`/wordcloud/`) — Word frequency visualization by book, testament, or full Bible

### Personal Records

21. **Bookmarks** (`/bookmarks/`) — Saved and organized verse bookmarks

22. **My Study** (`/notes/`) — Notes and highlights viewer

23. **Reading Progress** (`/progress/`) — Chapter-by-chapter reading history, statistics

24. **Tracker** (`/tracker/`) — Discipline streak history, daily checklist log

### System Features

25. **PWA** — Offline capable (cache-first data), installable, app shortcuts, dark mode
26. **Dark Mode** — CSS custom properties + system preference
27. **Bible Version Switcher** — 16 translations + MKT + Apocrypha versions, persisted to localStorage
28. **Local Highlights & Notes** — Color palette (10 colors), v2 timestamped notes, storage migration
29. **Auto-tag theological terms** — `terms.js` underlines key terms in verse text; click → Dictionary
30. **Auto-tag place names** — `places.js` underlines place names in verse text; click → Maps

---

## CSS Design System

All colors, spacing, and typography are CSS custom properties on `:root`. Every component
responds to dark mode automatically via `[data-theme="dark"]` attribute swap.

**Color palette (light mode):**
```css
--color-bg:       #faf8f4  /* warm off-white */
--color-surface:  #f3efe8  /* card backgrounds */
--color-primary:  #5c3d1e  /* warm brown — primary brand */
--color-accent:   #8c6a00  /* gold — links, highlights */
--color-text:     #1a1008
--color-muted:    #8a7a6a
--color-border:   #d6cfc4
```

**Informal genre color conventions** (in template comments, not yet CSS vars):
```
Pauline / theology:  #1e3a6e  (navy)
OT / Psalms:         #5c3d1e  (brown — site primary)
Gospels / Kingdom:   #3d5a2a  (forest green)
Eschatology:         #52278a  (violet)
```

**Typography:**
- Body: `Georgia` serif, 1.05rem, line-height 1.75
- UI: `system-ui` sans-serif
- Max content width: 860px

**Layout:**
- Desktop: 240px fixed sidebar pushes content right
- Mobile (<1024px): sidebar becomes drawer overlay, hamburger toggle
- Topic pages: sidebar in overlay mode (max reading width)

**CSS file organization (28 files total):**
- `style.css` — global design system (properties, layout, sidebar, typography, dark mode)
- Feature CSS (27 files): `apocrypha`, `bible-ui`, `book-study`, `daily`, `devotionals`,
  `dictionary`, `discipline`, `lib-browser`, `lib-progress`, `lib-reader`, `library`, `maps`,
  `memorize`, `ol-companion`, `reader`, `study-guide`, `study-nav`, `timelapse`, `timeline`,
  `topic-guide`, `topic-shell`, `topical`, `verse-study`, `word`, `wordcloud`, `workshop`

---

## Reference Linking Convention

Used universally across all pages:
```html
<a class="ref" data-ref="John 3:16">John 3:16</a>
```
`wire.js` picks these up at runtime and attaches modal + hover tooltip behavior.
No per-page wiring needed — the convention is self-registering.

---

## Extensibility — Adding New Content

**New topic page:** Copy `topics/_template/index.html`, edit title/description/content.
Add an entry in `data/topics.json` (type: `"topical"` or `"book"`).

**New book study:** Copy `topics/_template-book/index.html`, fill in chapter content.
Add entry in `data/topics.json` (type: `"book"`, include `"book"` key for study-link banner).

**New study guide:** Copy `study-guides/_template/index.html`, fill in sessions.
Add entry in `data/topics.json` under `type: "study"`.

**Hero accent colors by genre:**
- OT / Psalms: `--tg-accent: #5c3d1e`
- Gospels / Kingdom: `--tg-accent: #3d5a2a`
- Pauline / theology: `--tg-accent: #1e3a6e`
- Eschatology / Revelation: `--tg-accent: #52278a`

---

## Code Comment Convention (REQUIRED)

Per `CLAUDE.md`, all non-trivial new code must include:
```js
// INTENT: [what this block does and WHY — not a restatement of the obvious]
// CHANGE? [specific variables, file paths, or downstream callers to update]
// VERIFY: [browser/console observation that confirms correctness]
```
Required on: exported functions, non-trivial algorithms, shared/global state,
caches, and cross-module couplings (`window.*`, `localStorage.*`).

Extended rationale in `CODING_PHILOSOPHY.md` and `CODING_RULES.md` (repo root).

---

## Service Worker Cache Strategy

```
APP_CACHE_V = 'bsw-app-v{N}'   ← HTML/CSS/JS/icons — bump on code deploy
DATA_CACHE_V = 'bsw-data-v{N}' ← JSON data — bump on schema change
```
- HTML: network-first (always fresh online)
- CSS/JS/icons: cache-first (cached after first load)
- JSON data: cache-first

**Rollback:** Revert commit + bump both cache version numbers.

---

## Design & Purpose Principles

### Established (the site already follows these)

1. **Scripture-first readability** — Georgia serif, 1.75 line-height, 860px max-width.
   The text itself is not competing with chrome.

2. **No build step, no dependencies** — Zero toolchain; the owner edits in Sublime Text
   and pushes. A `package.json` would break this contract.

3. **Incremental extensibility** — Templates for topics, book studies, and study guides make
   adding new content a copy-and-edit operation.

4. **All data local / all state local** — No accounts, no analytics, no external login.
   Highlights, notes, and progress are in `localStorage`. A privacy principle and a
   simplicity principle simultaneously.

5. **Progressive enhancement** — Sidebar, modal, and version picker layer on top of
   static HTML that already has meaningful content.

6. **Modular, decoupled JS** — Each feature module owns one domain. Cross-module
   communication goes through registered callbacks in `app.js`, not direct imports.

### Aspirational (worth enforcing going forward)

7. **Daily study environment, not just a reference lookup** — The sidebar top-nav and homepage
   should make the core loop explicit: Discipline Hub + Reader are primary; Library, Maps, and
   Timeline are depth resources. This hierarchy is surfaced in the sidebar tools order but
   not yet in the homepage layout priority.

8. **Owner-specific features stay non-prominent** — MKT workshop, echoes, Apocrypha reader
   are personal tools. They don't need to be first in navigation.

9. **Offline experience is first-class** — With ~20,000+ JSON files cached, the site is
   an offline Bible library. `offline.html` should reflect that, not be a bare fallback.

10. **Comment discipline enforced** — INTENT/CHANGE?/VERIFY is mandatory specifically
    because cross-module state (storage migrations, version callbacks, cache keys) is where
    subtle bugs live. `storage.js`, `tracker.js`, and the `app.js` callback chain are the
    highest-priority targets.

11. **Visual system stays formal** — Genre/theme color conventions and hero pattern options
    should be CSS custom properties, not just informal comments in templates. This prevents
    visual drift as new pages are added.

---

## Python Tooling (offline data generation)

~1,952 scripts in `scripts/` — never run on the site, only offline to regenerate JSON data.

| Category | Examples |
|---|---|
| Data builders | `build-library-data.py`, `build-parallels.py`, `build-verse-index.py` |
| Commentary generation | `zc-context-{book}-{ch}.py`, `zc-christ-{book}-{ch}.py` |
| Translation (MKT) | `mkt-{book}-{ch}.py` — literal/mediating/thought variants |
| Enrichment | `enrich-batch-1.py` … `enrich-batch-7.py` |
| Fetch scripts | `fetch-commentary.py`, `fetch-isbe.py`, `fetch-ellicott.py`, `fetch-strongs.py`, etc. |
| Validation | `apply-decisions.py`, `check-contrast.py` |
| Dev server | `serve.py` |

Agent prompt guides for offline generation tools:
- `LOOP_AGENT_PROMPT.md` — loop-based site audit agent
- `Z_AGENT_PROMPT.md` — Z commentary (Christ-focused / context / original language) agent
- `Z_COMMENTARY_AGENT_GUIDE.md` — commentary generation guide
- `MKT_AGENT_PROMPT.md` — MKT translation agent prompt
- `TRANSLATION_AGENT_GUIDE.md` — translation workflow guide
