# Site Audit Agent Guide

*This document is the standing brief for an AI agent running a recurring site audit.
Run it via `/loop` in Claude Code, or use it as the prompt for a one-off audit session.
Findings go to `working/TODO.md` using the format specified below.*

---

## Agent Mission

You are auditing the Bible study site at `c:\Users\Administrator\Documents\GitHub\Seriousd6.github.io`.

Each audit pass should:
1. Pick **one area** from the audit dimensions below (rotate through them across sessions)
2. Read the relevant files thoroughly
3. Find real issues — bugs, gaps, inconsistencies, missing states, usability problems
4. Write up any findings in `working/TODO.md` using the exact format below
5. Skip items already tracked (search TODO.md before writing)

Do **not** fix anything during an audit pass. The audit produces suggestions; a separate work
session implements them. Do **not** add vague items like "improve performance" — every item must
name specific files, functions, and observable symptoms.

---

## How to Write a TODO Entry

All new TODO entries go at the bottom of the appropriate existing section in `working/TODO.md`,
or in a new section at the bottom if no section fits. Use this exact format:

```markdown
### AREA-X · Short descriptive title *(HIGH / MEDIUM / LOW)*

**Problem:** One paragraph. What is broken, missing, or inconsistent?
Name the file(s) and function(s) where the issue lives. Describe the observable symptom
a user would see. If it is a gap rather than a bug, describe what the user cannot do.

**Fix:**
- `filename.js` (`functionName`): Specific change described in one line.
- `filename.css`: Specific CSS rule to add or change.
- Any other files affected.

**Verify:** What to observe in the browser or console to confirm the fix is correct.
```

Use priority labels:
- **HIGH** — broken behavior, data loss risk, confusing UX on the main path
- **MEDIUM** — missing feature, degraded experience, inconsistency
- **LOW** — polish, edge case, minor visual issue

Prefix codes to use (pick the right one for the area being audited):
- `AUD-` for audit-discovered items with no other natural prefix
- `NAV-` for navigation and routing
- `UX-` for user experience flows
- `CSS-` for visual and style system
- `CODE-` for code quality, comment discipline, architecture
- `PWA-` for offline, service worker, install flow
- `DATA-` for data files, missing JSON, broken paths
- `PERF-` for performance, unnecessary fetches, load time

---

## Audit Dimensions

Work through these in order across audit sessions. After completing the full cycle, start again.

---

### Dimension 1 — Code Comment Audit

**Goal:** Find JS functions and state interactions missing required `INTENT/CHANGE?/VERIFY` comments.

**What to check:**
- `assets/js/storage.js` — storage migration logic, v1→v2 upgrade, all write paths
- `assets/js/tracker.js` — `getToday()`, `onUpdate()`, localStorage coupling
- `assets/js/app.js` — version-change callback chain, cross-module registration
- `assets/js/core.js` — `parseRef()`, `resolveVerses()`, Bible-ready event system
- `assets/js/wire.js` — `wireRefLinks()`, `autoTagRefs()`, `applyHighlights()`
- `assets/js/modal.js` — shared modal state, tab switching, note editing
- `assets/js/daily.js` — plan state management, devotional loading
- `assets/js/reader.js` — cross-ref panel loading, compare mode, history writing
- `sw.js` — cache strategy, activation cleanup, network-first vs. cache-first branches

**What to look for:**
- Any exported function or function that writes `localStorage` without a `// INTENT:` comment
- Any algorithm (loop, sort, complex conditional) without `// INTENT:`
- Any cross-module coupling (e.g., `window.BibleUI.*`, `window._readerLookupFn`) without
  `// CHANGE?` noting the downstream callers
- Any `localStorage.setItem` / `localStorage.getItem` call without `// VERIFY:` nearby
- Cache key strings (e.g., `bsw-app-v64`) without a comment explaining when to bump them

**How to report:**
Write one `CODE-X` TODO entry per file (not per function) that summarizes what's missing.
Include 2–3 specific function names as examples in the Problem description.

---

### Dimension 2 — Empty State & Loading State Audit

**Goal:** Find pages and panels that have no feedback when loading or when data is absent.

**What to check (read each page's JS init function):**
- `read/index.html` + `reader.js` — blank load, missing chapter data, failed version fetch
- `search/index.html` + `search.js` — zero results, failed fetch
- `word/index.html` + `word.js` — no Strong's number in URL, failed interlinear fetch
- `verse-study/index.html` + `verse-study.js` — invalid ref, missing commentary
- `library/index.html` + `library.js` — empty library index, missing document
- `discipline/index.html` — empty plan (no chapters today), empty journal, no memory cards due
- `history/index.html` — timeline with no data, map with missing GeoJSON
- `topics/{slug}/index.html` — ref links with no data (e.g., `data-ref` pointing to
  a verse that 404s)

**What to look for:**
- `fetch()` calls with no `.catch()` handler
- Elements that stay empty (no spinner, no "nothing here" message, no fallback text)
- Loading indicators that never get cleared (spinner shown but never removed on error)
- Cases where a missing `?ref=` URL param causes a blank page with no guidance

**How to report:**
One `UX-X` entry per page/module that lists which specific panels have no empty/error state.

---

### Dimension 3 — Mobile Responsiveness Audit

**Goal:** Find layout breaks, overflow, or hidden content on narrow screens.

**What to check:**
- Open browser DevTools, set viewport to 375px wide (iPhone SE)
- Then 768px (tablet)
- Check each of these pages: `/`, `/read/`, `/discipline/`, `/search/`, `/verse-study/`,
  `/word/`, `/library/`, `/history/`, `/topics/prayer/`, `/study-guides/hebrews/`

**What to look for:**
- Text or buttons cut off outside viewport (check for `overflow-x: scroll` on `body`)
- Modal or popover positioned off-screen
- Sidebar not closing properly after navigation on mobile
- Tables (`.reader-compare-grid`, topic tables) that overflow horizontally
- Font size below 14px on body text (WCAG minimum)
- Touch targets smaller than 44px (buttons, verse numbers, nav items)
- Sticky headers overlapping content at anchor targets
- `.reader-browse-hint` keyboard hint visible on touch devices

**How to report:**
One `CSS-X` entry per page with a list of specific CSS rules and media queries to add/fix.

---

### Dimension 4 — Data Path Integrity Audit

**Goal:** Find JS fetch calls that target data files that may not exist.

**What to check:**
- All `fetch()` calls in all `assets/js/*.js` that build a path from `DATA_ROOT`
- Cross-check the constructed paths against actual files in `data/`
- Check `data/topics.json` — every `href` and `slug` entry should resolve to a real page
- Check `data/versions/versions.json` — every `id` should have corresponding files in `data/bible/{id}/`
- Check sidebar nav links in `main.js` — every `href` should resolve to a real page
- Check `manifest.json` shortcuts — `url` values should resolve
- Check `sw.js` precache list (if any explicit file list exists)

**Specific paths to verify:**
```
data/bible/{VERSION}/{book}.json   ← do all 18 versions have all 66 books?
data/commentary/{SOURCE}/{book}.json  ← which sources have gaps?
data/echoes/{book}.json            ← which books are missing echo data?
data/devotionals/spurgeon-morning.json  ← does it cover all 365 days?
data/votd/{year}/{month}/{day}.json    ← is current year's data present?
data/plans/*.json                  ← are all plan IDs referenced from main.js real files?
```

**How to report:**
One `DATA-X` entry per category (missing version data, missing commentary, etc.) noting
which books/versions are absent.

---

### Dimension 5 — Feature Completeness Audit

**Goal:** Find features that are wired up in the UI but backed by missing or stub data.

**What to check:**
- Commentary sources listed in `core.js` COMMENTARY_SOURCES — test each in the verse modal
- Sidebar nav links — click every link and confirm the page loads with real content
- `data/topics.json` entries — every `slug` should have a corresponding `topics/{slug}/index.html`
  and that page should have actual content, not just template placeholder text
- Study guide session tabs — click every session in every guide; confirm content loads
- Reading plans — select each plan in the discipline hub; confirm today's chapters show
- Library documents — click a sampling of library entries; confirm HTML loads
- Word cloud scopes — try OT, NT, each book scope; confirm data loads
- Devotional sources — test each of the 5 buttons (Morning, Evening, Psalms, Proverbs, NT Daily)
  for today's date

**How to report:**
One `AUD-X` entry per category (missing topic page, stub study guide session, etc.).

---

### Dimension 6 — Performance Audit

**Goal:** Find unnecessary or redundant network fetches, oversized data loads.

**What to check:**
- Open Network tab in DevTools, load each major page, note total request count + KB transferred
- Look for fetch calls inside event handlers that fire on every keystroke (search input)
- Look for non-deferred fetches that load on page init but whose data isn't needed immediately
  (e.g., loading all devotionals when only one is shown)
- Check `word.js` — up to 39 concurrent interlinear fetches; is there a reasonable cap or queue?
- Check `verse-study.js` — `vsRenderVersionCompare` was supposed to be lazy-loaded (VS-D);
  confirm the IntersectionObserver deferral is actually working
- Check `daily.js` — does it fetch all 5 devotional sources on page load, or only the selected one?
- Check `reader.js` cross-ref loading — does it fetch cross-refs for every chapter in a multi-chapter
  view, or just the first?

**How to report:**
One `PERF-X` entry per fetch pattern problem, naming the function and the refactoring approach.

---

### Dimension 7 — Visual System Audit

**Goal:** Find pages that deviate from the design system (colors, typography, spacing, dark mode).

**What to check:**
- Open each topic page and study guide in dark mode — check for hardcoded colors that don't invert
- Check all hero headers — do they all use `--tg-accent` correctly?
- Check for hardcoded hex colors in `*.css` files that should be `var(--color-*)` references
- Check font-size usage — are there `font-size` values in px that should be `rem`?
- Check `topics/_template/index.html` and `study-guides/_template/index.html` for
  placeholder text (e.g., "YOUR TOPIC HERE", "[description]", lorem ipsum) that leaked
  into a real page
- Compare the sidebar on topic pages vs. non-topic pages — does overlay mode activate correctly?
- Check dark mode on the library reader, maps page, timeline, and animated map specifically —
  these are the most likely to have dark mode gaps

**How to report:**
One `CSS-X` entry per page or component type with specific property names to fix.

---

### Dimension 8 — Navigation & Discoverability Audit

**Goal:** Find orphaned pages, broken links, and nav hierarchy problems.

**What to check:**
- Every link in the sidebar nav (`main.js` NAV array) — does the target page exist?
- Every card in `topics/index.html` — does it link to a real page?
- Every study guide card in `search/index.html` — does it link to a real page?
- Check for pages that exist on disk but are not linked from anywhere in the nav or topic index
  (use `Glob` to find all `*/index.html` files, then check whether each is reachable from the sidebar)
- Check `?minimal=1` mode — pages that are embedded in iframes should suppress their sidebar;
  test `/discipline/?tab=plans` in an iframe; test `/topics/prayer/?minimal=1`
- The `history/` hub — confirm all 4 tabs (Biblical Timeline, Church History, Maps, Animated Map)
  load their content without errors
- Mobile: confirm the hamburger menu opens and the sidebar overlay closes on nav item click

**How to report:**
One `NAV-X` entry per broken link or orphaned page category.

---

### Dimension 9 — PWA & Offline Audit

**Goal:** Find gaps in the offline experience and service worker strategy.

**What to check:**
- Open Chrome DevTools → Application → Service Workers; confirm `bsw-app-v{N}` is registered
- Switch to offline mode; navigate to `/`, `/read/`, `/discipline/`; confirm they load from cache
- Navigate to `offline.html` directly; assess whether it provides real value or is just a placeholder
- Check whether all CSS and JS files are in the app cache (or fetched on first use and cached)
- Check whether `data/votd/` files for the current year are pre-fetched or cached on first use
- Check `manifest.json` — are all shortcut URLs pointing to real pages?
- Install the PWA on mobile; confirm app icons look correct and the standalone mode works
- Check dark mode in standalone (installed) mode

**How to report:**
One `PWA-X` entry per gap, describing what the user experiences when offline.

---

### Dimension 10 — Accessibility Audit

**Goal:** Find keyboard, screen reader, and contrast issues.

**What to check:**
- Tab through each page in order; check that focus order is logical
- Verify all interactive elements (buttons, links, selects) have visible focus styles
- Check the verse modal — can it be opened and closed with keyboard only?
- Check the sidebar collapse button — does it have `aria-label`?
- Check `.ref` links — do they have meaningful `title` or `aria-label` attributes?
- Run Chrome Accessibility DevTools on `/`, `/read/`, `/discipline/` — look for
  missing `alt` attributes, missing ARIA roles, contrast failures
- Check color contrast: `--color-muted` (#8a7a6a) on `--color-bg` (#faf8f4) — is it ≥ 4.5:1?
- Check the dark mode versions of the same contrast ratios
- Verify the theme toggle button has an accessible name

**How to report:**
One `AUD-X` entry per accessibility failure category (not per individual element).

---

## Running This Audit in a Loop

To run one audit pass per loop iteration via `/loop`:

```
/loop 1800 Check the Bible study site for issues using working/audit-agent-guide.md. 
Pick the next unfinished dimension from the guide, audit that area by reading the relevant 
source files, and append any findings to working/TODO.md using the format in the guide. 
Track which dimension you just completed so the next run picks the next one.
```

Or use it manually: read this file, pick a dimension, audit, write findings.

---

## What NOT to Do During an Audit

- Do not fix anything — audit only
- Do not add items already tracked in `working/TODO.md` (search before writing)
- Do not add vague items ("improve UX", "add better error handling") — every item needs a file and function name
- Do not create new files other than appending to `working/TODO.md`
- Do not run Python scripts or modify data files
- Do not open a browser — audit is code-reading only (unless explicitly doing a visual/DevTools audit)

---

## Suggested Audit Session Log

Track which dimension was last audited here so the next pass picks up where it left off.

| Session | Date | Dimension | Items Found |
|---|---|---|---|
| 1 | 2026-06-05 | (first run — guide created) | — |
