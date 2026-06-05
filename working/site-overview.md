# Bible Study Website — Site Overview

*Generated 2026-06-05. Update this file whenever major new features land or the architecture shifts.*

---

## What It Is

A personal Bible study reference site hosted on GitHub Pages. Single-owner, static-file application —
no server, no framework, no build step — that has grown into a full-featured study environment covering
the entire canon (including Apocrypha) with 18 translations, commentary, word study, topical articles,
study guides, daily discipline tracking, and a library of historical Christian documents.

**Live URL:** https://seriousd6.github.io  
**Repo root:** `c:\Users\Administrator\Documents\GitHub\Seriousd6.github.io`  
**Hosting:** GitHub Pages (static, serves from repo root)

---

## Technical Architecture

| Layer | Choice | Notes |
|---|---|---|
| Language | HTML + CSS + vanilla JS (ES Modules) | No framework, no transpiler |
| Data | ~20,000 static JSON files | Fetched on demand, cache-first via SW |
| State | `localStorage` exclusively | ~15 named `bsw_*` keys |
| Tooling | 477 Python scripts | Offline data generation only, never run on-site |
| Hosting | GitHub Pages | Static files from repo root |
| PWA | Service Worker (`sw.js`) | Network-first HTML, cache-first data/assets |
| Dark mode | CSS custom properties + `[data-theme="dark"]` | System preference respected |

### Module System

- **`main.js`** (non-module, loads sync): Builds the entire sidebar DOM from a nav tree and a runtime
  fetch of `data/topics.json`. Manages sidebar collapse state. Must load before `app.js` so the
  `#bible-version` element exists for `populateVersionPicker()`.
- **`app.js`** (ES module entry): Imports ~25 feature modules, wires cross-module callbacks,
  exposes `window.BibleUI`.
- **`core.js`**: Shared URL constants (`DATA_ROOT`, `COMMENTARY_ROOT`, etc.), book maps,
  `parseRef()`, `escHtml()`, `resolveVerses()`, version-change event system.

### Data Architecture

All Bible text, commentary, cross-refs, parallels, interlinear, Strong's, dictionary, topical index,
library documents, devotionals, timeline, and map data are flat JSON files fetched on demand.
No database, no API server.

```
data/bible/{VERSION}/{book}.json          ← one file per book per version (18 versions)
data/commentary/{SOURCE}/{book}.json      ← 8+ sources × 66 books
data/crossrefs/{book}.json
data/interlinear/{book}.json
data/strongs/{number}.json
data/topical/{topic}.json
data/library/docs/{doc-id}.json
data/devotionals/spurgeon-morning.json    ← 365 entries
data/votd/{year}/{month}/{day}.json
data/versions/versions.json              ← canonical version list
data/bible/books.json                    ← 66-book metadata
data/topics.json                         ← sidebar nav manifest
```

### localStorage Keys

| Key | Purpose |
|---|---|
| `bsw_version` | Selected Bible translation (default: BSB) |
| `bsw_theme` | light / dark |
| `bsw_sidebar` | collapsed / open |
| `bsw_notes_v2` | Timestamped verse notes |
| `bsw_chapter_read` | Reading history (chapter → date) |
| `bsw_plans` | Reading plan state |
| `bsw_lib_progress` | Library reading history |
| `bsw_sg_progress` | Study guide session completion |
| `bsw_tracker` | Daily discipline checklist |
| `bsw_memory` | Spaced repetition verse data |
| `bsw_journal` | Prayer journal entries |
| `bsw_gratitude` / `bsw_reflections` / `bsw_worship` | Journal sub-sections |

---

## Page Map

| Route | Page | Purpose |
|---|---|---|
| `/` | index.html | Daily dashboard (homepage) |
| `/read/` | Bible Reader | Multi-version reader, interlinear, compare |
| `/search/` | Explore Hub | Search, topics, study guides, dictionary, word cloud |
| `/discipline/` | Discipline Hub | Plans, devotionals, memory, journal, worship |
| `/verse-study/` | Verse Study | Single-verse deep research |
| `/word/` | Word Study | Greek/Hebrew word lookup, all occurrences |
| `/topics/` | Topics Index | Topical articles + book studies |
| `/topics/{slug}/` | Topic Page | Individual topical article |
| `/study-guides/{slug}/` | Study Guide | Multi-session tabbed study guide |
| `/library/` | Library | Historical documents browser |
| `/history/` | History Hub | Timeline, church history, maps, animated map |
| `/apocrypha/` | Apocrypha Reader | Deuterocanonical books |
| `/translation/workshop/` | Translation Workshop | MKT translation comparison |
| `/memorize/` | Memory Manager | Spaced repetition interface |
| `/journal/` | Journal | Prayer/reflection writing |

---

## Feature Inventory

### Core Loop (daily use)

1. **Bible Reader** (`/read/`)
   - 18 translations (KJV, BSB, WEB, ASV, YLT, DBY, GNV, AKJV, WEBBE + 3 MKT tiers + Apocrypha versions)
   - Flexible ref lookup: `John 3:16`, `Romans 8`, `Gen 1; John 1:1–14`
   - Keyboard navigation (j/k for next/prev chapter)
   - Cross-reference panel, compare mode, interlinear Hebrew/Greek toggle, parallel passages
   - Highlight & notes (local), bookmarks, reading history

2. **Verse Modal** (triggered by any `.ref` click)
   - Tabs: Verse text, Cross-refs, Commentary, Word Study, Topics, Confessions
   - Actions: highlight, note, bookmark, memorize, copy, share as image, print

3. **Daily Discipline Hub** (`/discipline/`)
   - Reading plans (configurable start date)
   - Morning/Evening Spurgeon + Psalms + Proverbs + NT Daily devotionals
   - Spaced-repetition Scripture memory (SRS)
   - Prayer journal, reflections, gratitude, worship notes
   - Discipline streak tracking (7-item daily checklist)

4. **Homepage** (`/`)
   - Time-based greeting, today's date
   - Quick verse lookup (jumps to `/read/`)
   - Verse of the Day
   - Reading plan for today
   - Devotional carousel
   - Disciplines tracker (7-item checklist with links to hub)
   - In-progress study guides card
   - Continue Reading card (library history + book suggestions)

### Study Depth Features

5. **Verse Study** (`/verse-study/`) — Single-verse research: text, cross-refs, commentary, parallels, word study in one page

6. **Word Study** (`/word/`) — Lemma lookup, morphological distribution, all occurrences across Bible

7. **Topics** (`/topics/`) — 6 topical articles (Prayer, Justification, Holy Spirit, Covenants, Christology, Holy Catholic Church) + 4 book studies

8. **Study Guides** (`/study-guides/`) — 5 multi-session guides (Hebrews 14, Romans 1–8 9, Ephesians 7, Psalms 5, Sermon on Mount 6), tabbed sessions with discussion questions

9. **Search & Explore** (`/search/`) — Verse search with filters, omni-search, topic browser, dictionary, word cloud

### Reference Resources

10. **Library** (`/library/`) — 28+ historical documents: creeds, confessions, church fathers; reading history

11. **History Hub** (`/history/`) — Biblical timeline, church history, 15+ static maps, animated history map

12. **Translation Workshop** (`/translation/workshop/`) — Side-by-side MKT literal/mediating/thought comparison

13. **Apocrypha** (`/apocrypha/`) — Full reader for deuterocanonical books

### System Features

14. **PWA** — Offline capable (cache-first data), installable, app shortcuts, dark mode
15. **Dark Mode** — CSS custom properties + system preference
16. **Bible Version Switcher** — 18 translations, persisted to localStorage
17. **Local Highlights & Notes** — Color palette (10 colors), v2 timestamped notes, storage migration

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

**CSS file organization:**
- `style.css` — global design system (properties, layout, sidebar, typography, dark mode)
- `*.css` per feature — 26 additional feature-specific stylesheets

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
Add a card entry in `topics/index.html` and an entry in `data/topics.json`.

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

3. **Incremental extensibility** — Templates for topics and study guides make adding
   new content a copy-and-edit operation.

4. **All data local / all state local** — No accounts, no analytics, no external login.
   Highlights, notes, and progress are in `localStorage`. A privacy principle and a
   simplicity principle simultaneously.

5. **Progressive enhancement** — Sidebar, modal, and version picker layer on top of
   static HTML that already has meaningful content.

6. **Modular, decoupled JS** — Each feature module owns one domain. Cross-module
   communication goes through registered callbacks in `app.js`, not direct imports.

### Aspirational (worth enforcing going forward)

7. **Daily study environment, not just a reference lookup** — The homepage and nav
   should make the core loop explicit: discipline hub + reader are primary; library and
   timeline are depth resources. This hierarchy is not yet surfaced in the UI.

8. **Owner-specific features stay non-prominent** — MKT workshop, echoes, Apocrypha
   reader are personal tools. They don't need to be first in navigation.

9. **Offline experience is first-class** — With ~20,000 JSON files cached, the site is
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

477 scripts in `scripts/` — never run on the site, only offline to regenerate JSON data.

| Category | Examples |
|---|---|
| Data builders | `build-library-data.py`, `build-parallels.py`, `build-verse-index.py` |
| Commentary generation | `zc-context-{book}-{ch}.py`, `zc-christ-{book}-{ch}.py` |
| Translation (MKT) | `mkt-{book}-{ch}.py` — literal/mediating/thought variants |
| Enrichment | `enrich-batch-1.py` … `enrich-batch-7.py` |
| Validation | `apply-decisions.py`, `check-contrast.py` |
| Dev server | `serve.py` |
