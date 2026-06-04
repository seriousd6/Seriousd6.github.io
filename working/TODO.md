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

- [ ] `Z_COMMENTARY_SCRIPT_GUIDE.md` — static script boilerplate (load/save/merge helpers), HTML conventions, source data checklist
- [ ] `Z_COMMENTARY_AGENT_GUIDE.md` — content principles and length targets for all three commentary types
- [ ] `Z_PROGRESS.md` — full work queue (66 books × 3 commentaries + echo layer, ≤6ch units, same claim protocol as MKT_PROGRESS.md)
- [ ] `Z_AGENT_PROMPT.md` — paste prompt for agent sessions (mirrors MKT_AGENT_PROMPT.md)

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

### WD-A · Performance — Loading Progress for Bulk Interlinear Fetch *(HIGH)*

`initWordPage` fires one `loadInterlinear()` call per book in the relevant testament — up to 27
(NT) or ~39 (OT) concurrent fetches. There is no progress feedback; the user sees only the
static "Loading…" header text until every book resolves. For a common word (e.g. G2316 θεός,
1300+ occurrences) this can take 5–15 MB of network and several seconds on a slow connection.

- [x] `word.js` (`initWordPage`, books fetch block): Track `completed` and `total` counters.
  After each `loadInterlinear` promise settles, update a progress element:
  `"Loading books… 12 / 27"`. Insert a `<p id="wd-progress" class="wd-loading"></p>` below
  the header before the fetch starts; remove it (or replace with stat cards) once all books
  are done.
- [x] `word.css`: Add `.wd-progress { font-size:.82rem; color:var(--color-muted); margin-bottom:.5rem; }`

---

### WD-B · UX — Filter State Lost on Reload / Not Shareable *(HIGH)*

Book (`_wdCurrentBook`) and translation (`_wdCurrentFilter`) filters live only in JS module
state. Refreshing or sharing the URL loses both. A hash-based approach is cheap and makes
filtered views linkable.

- [x] `word.js` (`_wdToggleFilter`, `_wdToggleBook`): After updating module state, write to
  `location.hash` — e.g. `#book=john&trans=love`. Use `encodeURIComponent` on each value.
  Empty / null values should remove the key from the hash.
- [x] `word.js` (`initWordPage`, after data loads): Read `location.hash` and restore
  `_wdCurrentBook` and `_wdCurrentFilter` before calling `_wdRenderTranslations`,
  `_wdRenderBooks`, and `_wdRenderVerses`.
- [x] `word.js`: Listen to `window.addEventListener('hashchange', ...)` and re-apply filters
  so browser Back/Forward navigation works.

---

### WD-C · Feature — Morphological Form Breakdown *(HIGH)*

The interlinear token data includes a `.m` (morph code) field that `word.js` never reads.
For a Greek verb like G3004 (λέγω) the distribution of tenses, voices, and moods across all
occurrences is the most directly useful data for translation work. For nouns, case distribution
matters. This data is already loaded; it just isn't surfaced.

- [x] `word.js` (`initWordPage`, accumulation loop): While scanning tokens for matching
  Strong's IDs, also collect `tok.m` values into a `morphCount` object:
  `morphCount[tok.m] = (morphCount[tok.m] || 0) + 1`.
- [x] `word.js`: Add `_wdRenderMorphTable(morphCount)` — expands each code via
  `expandMorphCode` (already imported from `interlinear.js`) and renders a compact table of
  form → count, sorted descending. Insert it between the stat cards and the two-column body.
- [x] `word.css`: `.wd-morph-table` styles added.
  Omit this section entirely for words with no morph codes (punctuation / particles).

---

### WD-D · UX — Interactivity Not Discoverable; No "All" Reset *(MEDIUM)*

Translation rows and book pills are the only interactive elements in the sidebar, but they
look like plain data — no tooltip, no affordance copy. Clearing a filter requires finding and
clicking a chip in a different zone of the page; there is no "All / reset" button in the
sidebar itself.

- [x] `word.css`: `cursor:pointer` confirmed on `.wd-book-pill`; `title` attributes added via JS.
- [x] `word.js` (`_wdRenderTranslations`): "All translations" row prepended; active when no filter set.
  "All books" pill prepended in `_wdRenderBooks`.
- [x] `word.js` (`_wdRenderVerses`, render function): "Clear all" button added at right end of `.wd-filter-bar`; visible when both filters active (consolidated with WD-J).

---

### WD-E · Feature — "Open in Reader" Link per Book Section *(MEDIUM)*

Each `.wd-verse-ref-link` triggers the tooltip/modal but provides no path to the full passage
context in the Reader. A small link per book-section heading (not per verse card — too noisy)
closes the loop without cluttering the list.

- [x] `word.js` (`_wdRenderVerses`, book section heading): `.wd-book-reader-link` appended inside heading.
- [x] `word.css`: `.wd-book-reader-link` styles added.

---

### WD-F · UX — Books Sidebar Height Cap Too Tight *(MEDIUM)*

`#wd-books` is capped at `max-height: 160px`. An OT word spanning 30+ books makes the pill
grid nearly unreadable — three rows visible with heavy internal scrolling.

- [x] `word.css` (`#wd-books`): Replaced `max-height: 160px` with `clamp(160px, 28vh, 260px)`.

---

### WD-G · UX — Author / Genre Breakdown in Stat Cards *(MEDIUM)*

Stat cards show total occurrences, books, and unique translations — raw counts with no
interpretive context. A Pauline word vs. a Johannine word vs. a Synoptic word tells a very
different story; the book metadata almost certainly carries enough to compute a genre or
author label per book.

- [x] `data/bible/books.json`: `genre` field added to all 66 books.
- [x] `word.js` (`_wdRenderStats`): "By genre" chip row appended to stat cards.

---

### WD-H · Feature — Second Lexical Source in Header *(MEDIUM)*

The header shows Thayer (Greek) or BDB (Hebrew) as the sole lexical source. The Strong's
dictionary data (`entry.gloss`, `entry.def`) is already in memory (loaded by `loadStrongs`)
and could appear as a second source without any additional network fetch.

- [x] `word.js` (`_wdRenderHeader`): Strong's (1890) added as `.wd-lexicon--strongs` collapsible card.
- [x] `word.css`: `.wd-lexicon--strongs` with `--color-border` left-border added.

---

### WD-I · UX — Keyboard Navigation Through Verse List *(LOW)*

The verse list can run to hundreds of entries with no keyboard shortcut to step through
occurrences, jump to a book section, or toggle the active filter.

- [x] `word.js`: `keydown` listener added — arrows step cards, `b`/`t`/`Escape` shortcuts.
- [x] `word.css`: `.wd-verse-card--focused` style added.

---

### WD-J · UX — "Clear All Filters" When Both Filters Active *(LOW)*

When both a book and a translation filter are active the user must dismiss two chips
separately. A single button saves a click.

- [x] Consolidated into WD-D — single "Clear all" button in filter bar handles both cases.

---

### WD-K · Visual — Semantic Range Bar Polish *(LOW)*

The translation frequency bars in `.wd-translation-bar` already encode percentages but are
only 8px tall and carry no percentage label. A minor visual polish pass would make the
semantic range story clearer.

- [x] `word.css`: Bar height 8px → 12px; `border-radius:6px`.
- [x] `word.js`: Percentage text `(38%)` appended; "How this word is translated:" label added.
- [x] `word.css`: `.wd-trans-label`, `.wd-trans-pct` styles added.

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

### RD-A · Chapter Navigation — Eliminate Full Page Reloads *(HIGH)*

**Bug:** `_navigateChapter()` in `reader.js` uses `window.location.href = READER_URL + '?ref=...'`
for all prev/next chapter navigation. This causes a full page reload, losing scroll position,
clearing the right panel, resetting all toggles' visual state, and adding ~500ms latency for
every chapter flip. By contrast, the chapter sidebar already uses `window._readerLookupFn` for
in-page navigation — so the two nav paths are inconsistent.

- [x] `reader.js` (`_navigateChapter`): Replace all `window.location.href = ...` assignments
  with the in-page pattern already used by the sidebar:
  ```js
  var newRef = /* computed new ref string */;
  var input  = document.getElementById('reader-lookup-input');
  if (input) input.value = newRef;
  if (window._readerLookupFn) window._readerLookupFn();
  ```
  Apply to all three branches: next chapter within book, prev chapter crossing into previous
  book, next chapter crossing into next book. The `?ref=` URL is already updated by
  `history.replaceState` inside `doLookup`, so deep-linking still works.
- [x] `reader.js`: The ch=0 (intro page) branch of `_navigateChapter` already uses this pattern
  correctly — verify it stays unchanged and serves as the model.

---

### RD-B · Browse Bar Overcrowding — View Options Overflow Menu *(HIGH)*

**Problem:** All toggles are injected directly into the browse bar row:
Interlinear · Book Info · ⇅ Compare · † Footnotes · ⇔ Split · ⇿ Wide · A− · A · A+ · A++ ·
☰ Chapters · ? keyboard shortcuts · keyboard hint span = **13+ elements in one bar row**.
On a 1280px screen with the site sidebar open, the reading area is ~700px wide — this row
wraps or overflows, pushing content down.

**Fix:** Keep 3–4 most-used controls inline; move the rest into a ⚙ "View" overflow popover.

- [x] `interlinear.js` / `reader.js`: Add a single `<button id="reader-view-btn" class="reader-view-btn">⚙ View</button>` injected first into the browse bar. Below it, a `.reader-view-popover` (absolutely positioned, `hidden` by default).
- [x] Move these into the popover (shown as a vertical list of toggle rows inside the popover):
  - Split / Wide / Sidebar (layout toggles — rarely changed mid-session)
  - Font size group (A− A A+ A++) — keep as a 4-button row inside the popover
  - Parallels toggle (if present)
  - Keyboard shortcuts `?` link
- [x] Keep inline (always visible in browse bar):
  - Interlinear toggle (frequently used during study)
  - Compare toggle (frequently toggled)
  - † Footnotes toggle (frequently toggled)
  - Book Info toggle
- [x] `reader.css`: `.reader-view-popover` — `position:absolute; top:100%; right:0; z-index:200; background:var(--color-surface); border:1px solid var(--color-border); border-radius:8px; padding:.6rem .75rem; min-width:200px; box-shadow:0 4px 16px rgba(0,0,0,.15)`; close on outside click and Escape
- [x] Mobile (≤700px): Keep browse bar to book/chapter selects + Compare only; everything else in the ⚙ popover

---

### RD-C · Restore Last Position on Blank Load *(HIGH)*

When navigating to `read/` with no `?ref=` parameter, the reader shows a blank `#reader-results`
with no prompt. `bsw_history` already stores up to 100 recent references but is never used
to restore state.

- [x] `reader.js` (`initReaderLookup`): After the URL param check, if `refStr` is empty, read
  `bsw_history[0]` from localStorage; if present, inject a dismissable banner into
  `#reader-results`:
  ```html
  <div class="reader-resume-banner">
    Continue where you left off:
    <a class="reader-resume-link" href="?ref={lastRef}">{lastRef}</a>
    <button class="reader-resume-dismiss" aria-label="Dismiss">✕</button>
  </div>
  ```
  Do NOT auto-navigate — let the user click. Dismissing sets `bsw_reader_resume_dismissed`
  so the banner doesn't reappear in the same session (use `sessionStorage`, not localStorage).
- [x] `reader.css`: `.reader-resume-banner` — muted surface background, subtle left border in
  `--color-primary`, `padding:.75rem 1rem`, `border-radius:6px`, `margin-bottom:1rem`,
  flex row with the link and dismiss button

---

### RD-E · Verse Hover — Highlight Active Verse *(MEDIUM)*

Clicking a verse number opens the modal, but the verse itself is not visually highlighted in
the text — it looks identical to surrounding verses while the modal is open. A reading context
highlight would help the eye return to position after dismissing the modal.

- [x] `reader.js` (`wireVerseNumberPopup`): When a verse number is clicked, add class
  `.reader-verse--active` to the parent `.reader-verse` element; remove it when the modal
  closes (`modal.js` should fire a `bsw:modal:close` CustomEvent, or add a callback)
- [x] `reader.css`: `.reader-verse--active` — subtle highlight: `background:var(--color-primary-faint, rgba(92,61,30,.07)); border-radius:3px; outline:1px solid var(--color-primary-faint)`

---

### RD-F · Right Panel — Notes Compose Scope *(MEDIUM)*

The notes compose textarea in the right panel prompts `"Add a note for John 3…"` (whole
chapter). Notes added here are stored at chapter scope. But the notes display shows
verse-specific notes with their verse label — creating confusion about what the textarea
actually targets. The verse-modal path is the only way to add a verse-specific note.

- [x] `reader.js` (`_loadReaderNotes`): Change the compose textarea placeholder to explicitly
  say `"Add a chapter note for {chLabel} (click a verse number to note a specific verse)…"`
- [x] `reader.js`: Add a small hint beneath the textarea: `"Verse-specific notes: click the
  verse number ↑"` in `.reader-hint` muted style — links the two note-entry paths explicitly

---

### RD-G · Cross Refs Panel — Cap on Multi-Chapter Views *(MEDIUM)*

`_loadReaderXrefs` iterates `c <= Math.min(parsed.endCh, parsed.ch + 4)` — for a whole-chapter
view this is one chapter, but for a multi-passage lookup (`Genesis 1; Romans 8`) it could
produce cross-refs from all chapters simultaneously, making the panel unwieldy.

- [x] `reader.js` (`_loadReaderXrefs`): Cap to the first chapter only for whole-chapter views;
  for multi-passage lookups, show cross refs for the first group's chapter only and add a
  note `"Showing cross-refs for {bookName} {ch}"` at the top of the panel
- [x] Add a chip row `.reader-xref-chips` to let the user pick which loaded passage's cross-refs to show when there are multiple groups; clicking a chip reloads xrefs for that passage

---

### RD-H · Empty-State Guidance for Blank Load *(MEDIUM)*

Separate from RD-C (which adds the resume banner for returning users). First-time visitors or
users who've cleared history see a completely blank `#reader-results` with no affordance.

- [x] `reader.js` (`initReaderLookup`): If no `?ref=` param AND no history entry, render a
  structured empty state in `#reader-results`:
  ```html
  <div class="reader-empty-state">
    <p class="reader-hint">Enter a reference above — <em>John 3:16</em>, <em>Romans 8</em>,
    <em>Gen 1; John 1:1–14</em></p>
    <div class="reader-quick-starts">
      <a class="reader-qs-chip" href="?ref=John+1">John 1</a>
      <a class="reader-qs-chip" href="?ref=Psalms+23">Psalm 23</a>
      <a class="reader-qs-chip" href="?ref=Romans+8">Romans 8</a>
      <a class="reader-qs-chip" href="?ref=Genesis+1">Genesis 1</a>
      <a class="reader-qs-chip" href="?ref=Isaiah+53">Isaiah 53</a>
    </div>
  </div>
  ```
- [x] `reader.css`: `.reader-empty-state` — centered, `padding:2rem 0`; `.reader-qs-chip` —
  same style as `.daily-passage-chip` (outlined pill links)

---

*(RD-I claimed — see working/inprogress-rdm-todo.md)*

---

### RD-J · Attribution Line — Suppress for Single-Verse Results *(LOW)*

The attribution line (`"Berean Standard Bible…"`) appears after every result group including
single-verse lookups like `John 3:16`. For a one-liner verse, the attribution takes up nearly
as much vertical space as the verse itself.

- [x] `reader.js` (`doLookup`): Set `attrEl.hidden = g.ref.v && !g.ref.endV` — hide
  attribution when the lookup is a single verse (verse specified, no range). Keep it visible
  for chapter views and ranges where attribution is appropriate context.

---

### RD-K · Mobile Browse Bar — Hide Keyboard Hint *(LOW)*

`.reader-browse-hint` (`"j / → next chapter · k / ← prev"`) is visible on mobile where
keyboard navigation is impossible.

- [x] `reader.css`: Add `@media (max-width: 700px) { .reader-browse-hint { display: none; } }`

---

### RD-L · Compare Mode — Per-Verse Row Locking *(HIGH)*

**Problem:** Both compare columns render as independent flowing text. Since verse lengths
vary between translations, the two columns fall out of vertical sync — if verse 3 in version A
takes two lines but version B's verse 3 takes four, every verse after that appears at a
different vertical position in each column. The comparison becomes unusable for detailed
textual study. The root cause is the current DOM structure: each column is a `<p>` with
consecutive `<span class="reader-verse">` children — two independent text flows with no shared
row relationship.

**Fix:** Replace the two flowing columns with a per-verse CSS grid where each verse number
occupies one explicit grid row, shared across both columns. Row height is set by whichever
cell is taller — both cells for verse N are always vertically aligned.

**Target DOM structure:**
```html
<div class="reader-compare-grid">
  <!-- sticky column headers -->
  <div class="reader-compare-col-hdr reader-compare-col-hdr--a">
    <span class="reader-compare-panel__label">A:</span>
    <select class="reader-compare-ver-sel">…</select>
  </div>
  <div class="reader-compare-col-hdr reader-compare-col-hdr--b">
    <span class="reader-compare-panel__label">B:</span>
    <select class="reader-compare-ver-sel">…</select>
  </div>
  <!-- verse rows — one pair per verse, automatically placed into the same CSS grid row -->
  <div class="reader-compare-cell reader-compare-cell--a" data-verse="1">
    <sup class="reader-verse__num">1</sup> In the beginning God created…
  </div>
  <div class="reader-compare-cell reader-compare-cell--b" data-verse="1">
    <sup class="reader-verse__num">1</sup> In the beginning God created…
  </div>
  <div class="reader-compare-cell reader-compare-cell--a" data-verse="2">…</div>
  <div class="reader-compare-cell reader-compare-cell--b" data-verse="2">…</div>
  …
</div>
```
In a `display: grid; grid-template-columns: 1fr 1fr` container, consecutive pairs of cells
are automatically placed into the same row, and the row height equals the taller of the two.
No explicit `grid-row` declarations needed.

**Implementation:**

- [x] `reader.js` (`injectComparePanel`): Replace the current two-panel approach with a
  per-verse grid builder. Extract primary verses from `g.verses` (already resolved). Build the
  grid DOM immediately with primary cells filled and secondary cells showing
  `<span class="reader-compare-loading">…</span>` as placeholders:
  ```js
  var grid = document.createElement('div');
  grid.className = 'reader-compare-grid';
  // — header row —
  grid.appendChild(_buildComparePanelHdr(primaryVer, 'primary'));
  grid.appendChild(_buildComparePanelHdr(cmpVer, 'secondary'));
  // — verse rows — primary cells filled immediately
  g.verses.forEach(function (vObj) {
    var cellA = document.createElement('div');
    cellA.className = 'reader-compare-cell reader-compare-cell--a';
    cellA.dataset.verse = String(vObj.chapter) + ':' + String(vObj.verse);
    cellA.innerHTML = '<sup class="reader-verse__num reader-compare-vnum">' +
      vObj.verse + '</sup>' + escHtml(vObj.text);
    var cellB = document.createElement('div');
    cellB.className = 'reader-compare-cell reader-compare-cell--b reader-compare-cell--loading';
    cellB.dataset.verse = String(vObj.chapter) + ':' + String(vObj.verse);
    cellB.innerHTML = '<span class="reader-compare-loading">…</span>';
    grid.appendChild(cellA);
    grid.appendChild(cellB);
  });
  // replace existing text content with the grid
  var bottomNav = groupEl.querySelector('.reader-chapter-nav--bottom');
  if (bottomNav) groupEl.insertBefore(grid, bottomNav);
  else groupEl.appendChild(grid);
  textEl.parentNode && textEl.parentNode.removeChild(textEl);
  attrEl && attrEl.parentNode && attrEl.parentNode.removeChild(attrEl);
  ```
- [x] `reader.js`: When secondary `resolveVerses` resolves, fill in each `--b` cell by
  matching on `data-verse`:
  ```js
  resolveVerses(g.ref, cmpVer).then(function (verses) {
    if (!verses || !verses.length) {
      grid.querySelectorAll('.reader-compare-cell--b').forEach(function (cell) {
        cell.innerHTML = '<span class="reader-compare-unavail">—</span>';
        cell.classList.remove('reader-compare-cell--loading');
      });
      return;
    }
    var byVerse = {};
    verses.forEach(function (v) { byVerse[v.chapter + ':' + v.verse] = v.text; });
    grid.querySelectorAll('.reader-compare-cell--b').forEach(function (cell) {
      var key  = cell.dataset.verse;
      var text = byVerse[key];
      var vNum = key.split(':')[1];
      cell.classList.remove('reader-compare-cell--loading');
      cell.innerHTML = text
        ? '<sup class="reader-verse__num reader-compare-vnum">' + vNum + '</sup>' + escHtml(text)
        : '<span class="reader-compare-unavail">—</span>';
    });
    applyHighlights(grid);
    // Add attribution below the grid
    var attr = ATTRIBUTION[cmpVer];
    if (attr) {
      var attrEl2 = document.createElement('p');
      attrEl2.className = 'reader-result-group__attr';
      attrEl2.textContent = attr;
      grid.after(attrEl2);
    }
  });
  ```
- [x] `reader.js` (`_buildComparePanelHdr`): No structural changes needed — the function
  still returns a `div` which now becomes a column header cell inside the grid rather than a
  panel header above a panel.

**CSS:**

- [x] `reader.css`: Replace `.reader-compare-wrap` / `.reader-compare-panel` rules with:
  ```css
  .reader-compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;                        /* no gap — borders handle separation */
    margin: 0.5rem 0 1rem;
  }
  .reader-compare-col-hdr {
    /* first two children of the grid = sticky column headers */
    position: sticky;
    top: 0;
    z-index: 10;
    background: var(--color-bg);
    border: 1px solid var(--color-border);
    border-bottom: 2px solid var(--color-primary);
    padding: 0.3rem 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-ui);
  }
  .reader-compare-col-hdr--a { border-right: none; border-radius: 6px 0 0 0; }
  .reader-compare-col-hdr--b { border-radius: 0 6px 0 0; }
  .reader-compare-cell {
    padding: 0.5rem 0.75rem;
    font-size: var(--reader-font-size, 1rem);
    line-height: 1.72;
    border-bottom: 1px solid var(--color-border);
    /* align-self: stretch is default — both cells in a row stretch to the same height */
  }
  .reader-compare-cell--a {
    border-right: 1px solid var(--color-border);
  }
  .reader-compare-cell--loading {
    color: var(--color-muted);
  }
  .reader-compare-unavail {
    color: var(--color-muted);
    font-style: italic;
    font-size: 0.85rem;
  }
  .reader-compare-vnum {
    color: var(--color-muted);
    font-size: 0.72em;
    margin-right: 0.2em;
    vertical-align: super;
    font-style: normal;
    user-select: none;
  }
  @media (max-width: 600px) {
    /* On narrow screens, stack versions — verse locking less important than readability */
    .reader-compare-grid { grid-template-columns: 1fr; }
    .reader-compare-col-hdr--a,
    .reader-compare-cell--a { border-right: none; }
    .reader-compare-col-hdr--b,
    .reader-compare-cell--b { border-top: 2px solid var(--color-primary); }
  }
  ```
- [x] `reader.css`: Remove old `.reader-compare-wrap`, `.reader-compare-panel`,
  `.reader-compare-panel__hdr` rules (now replaced by `.reader-compare-grid` and
  `.reader-compare-col-hdr`)

**Versification edge cases:**
- If a verse exists in version A but not in version B (e.g., Mark 16:9 in some critical texts):
  the secondary cell shows `—` (handled by `byVerse[key]` being undefined above)
- If version B has a verse that version A does not: that verse simply has no paired row and
  is silently omitted — acceptable for now; could be addressed in a future pass

---

*(RD-M claimed — see working/inprogress-rdm-todo.md)*

---

## Verse Study Page Improvements

*(Claimed — see working/inprogress-vs-todo.md)*

### VS-A · Prev/Next Verse Navigation *(HIGH)*

There is no way to move to the adjacent verse from the study page. To study John 3:15 after
John 3:16 the user must hit back, click a different verse number in the Reader, and re-enter the
verse study page — reloading all sections. The chapter data is already fully loaded as part of
`loadVerseStudyVerse`, so computing adjacent verse refs costs nothing extra.

- [x] `verse-study/index.html`: Add two nav links flanking `#vs-header-ref` in `.vs-header__topbar`:
  ```html
  <a id="vs-prev-link" class="vs-adj-link" href="#" hidden aria-label="Previous verse">‹</a>
  <!-- existing #vs-header-ref -->
  <a id="vs-next-link" class="vs-adj-link" href="#" hidden aria-label="Next verse">›</a>
  ```
- [x] `verse-study.js` (`loadVerseStudyVerse`): Inside the `.then(function (chapters) { … })` callback,
  after setting `focalTextEl.textContent`, update the nav links:
  ```js
  var prevLink = document.getElementById('vs-prev-link');
  var nextLink = document.getElementById('vs-next-link');
  if (prevLink) {
    var pv = parsed.v - 1;
    if (pv >= 1 && chData[String(pv)]) {
      prevLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + pv);
      prevLink.title = parsed.bookName + ' ' + parsed.ch + ':' + pv;
      prevLink.removeAttribute('hidden');
    } else { prevLink.setAttribute('hidden', ''); }
  }
  if (nextLink) {
    var nv = parsed.v + 1;
    if (chData[String(nv)]) {
      nextLink.href = VERSE_STUDY_URL + '?ref=' + encodeURIComponent(parsed.bookName + ' ' + parsed.ch + ':' + nv);
      nextLink.title = parsed.bookName + ' ' + parsed.ch + ':' + nv;
      nextLink.removeAttribute('hidden');
    } else { nextLink.setAttribute('hidden', ''); }
  }
  ```
- [x] `verse-study.css`: `.vs-adj-link { color: var(--color-accent); text-decoration: none; font-size: 1.1rem; padding: 0 0.2rem; flex-shrink: 0; line-height: 1; }` `.vs-adj-link[hidden] { display: none; }` `.vs-adj-link:hover { color: var(--color-primary); }`

---

### VS-B · Sidebar Nav — Active Section Scroll-Spy *(MEDIUM)*

`.vs-nav-btn--active` is defined in `verse-study.css` (lines 247–251) but is never applied by
JavaScript. `vsRebuildNav()` builds the button list on every section update but has no mechanism
to track which section is currently in view. The sidebar acts only as a jump list with no
orientation feedback — the user can't tell at a glance which section they're reading.

- [x] `verse-study.js` (`vsRebuildNav`): Declare a module-level variable `var _vsNavObserver = null`.
  At the top of `vsRebuildNav`, call `if (_vsNavObserver) { _vsNavObserver.disconnect(); _vsNavObserver = null; }`.
  After building sidebar buttons, wire each button with `btn.dataset.sectionId = id` in
  `vsCreateSection`, then register a fresh `IntersectionObserver`:
  ```js
  _vsNavObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var id = entry.target.id;
      document.querySelectorAll('#vs-sidebar .vs-nav-btn').forEach(function (btn) {
        btn.classList.toggle('vs-nav-btn--active', btn.dataset.sectionId === id);
      });
    });
  }, { rootMargin: '-8% 0px -75% 0px', threshold: 0 });
  visible.forEach(function (sec) { _vsNavObserver.observe(sec); });
  ```
- [x] `verse-study.js` (`vsCreateSection`): When building the sidebar `btn`, add `btn.dataset.sectionId = id;`
  (one line, before `sidebar.appendChild(btn)`)

---

### VS-C · Section Collapse/Expand *(MEDIUM)*

All 12 sections are fixed-open. After reading cross-references or commentary, the user must scroll
past the entire section to reach the ones below. On mobile with long commentary (Clarke,
Jamieson-Fausset-Brown) or a verse with many cross-refs, this can require scrolling 30+ screenfuls.
Independent per-section collapse fits the long-form layout better than the reader's tab-panel model.

- [x] `verse-study.js` (`vsCreateSection`): Add a collapse toggle to each section heading:
  ```js
  var toggleBtn = document.createElement('button');
  toggleBtn.className = 'vs-section-toggle';
  toggleBtn.setAttribute('aria-expanded', 'true');
  toggleBtn.setAttribute('aria-controls', id + '-body');
  toggleBtn.textContent = '▾';
  heading.appendChild(toggleBtn);
  body.id = id + '-body';

  toggleBtn.addEventListener('click', function () {
    var expanded = toggleBtn.getAttribute('aria-expanded') === 'true';
    toggleBtn.setAttribute('aria-expanded', String(!expanded));
    body.hidden = expanded;
    toggleBtn.textContent = expanded ? '▸' : '▾';
  });
  ```
- [x] `verse-study.css`: Update `.vs-section-heading` to `display:flex; align-items:baseline; justify-content:space-between;`
  Add `.vs-section-toggle { background:none; border:none; cursor:pointer; font-size:.72rem; color:var(--color-muted); padding:0 .2rem; margin-left:.4rem; flex-shrink:0; }` `.vs-section-toggle:hover { color:var(--color-primary); }`

---

### VS-D · All Translations — Lazy Load + Diff Highlighting *(MEDIUM)*

`vsRenderVersionCompare` fires a `resolveVerses` call for every version in `metaVersions` the
instant the section is built — 8–12 parallel fetch requests on page load before the user has
scrolled to that section. Additionally, the section shows all translation texts verbatim with no
diff highlighting, making it harder to spot translation choices at a glance. The Reader already has
`applyHighlights` in `wire.js` that handles this.

- [x] `verse-study.js` (`loadVerseSections`): Replace the current eager call to `vsRenderVersionCompare`
  with an `IntersectionObserver` that defers the fetch until the section is near the viewport:
  ```js
  var cmpObserver = new IntersectionObserver(function (entries) {
    if (!entries[0].isIntersecting) return;
    cmpObserver.disconnect();
    vsRenderVersionCompare(parsed, cmpSec.bodyEl);
  }, { threshold: 0.05 });
  cmpSec.el.removeAttribute('hidden');
  vsRebuildNav();
  cmpObserver.observe(cmpSec.el);
  ```
  Remove the current `vsRenderVersionCompare(parsed, cmpSec.bodyEl)` call that precedes the show/rebuild.
- [x] `verse-study.js` (`vsRenderVersionCompare`): Import `applyHighlights` from `./wire.js`; after each
  `resolveVerses` resolve, call `applyHighlights(row)` on the `.vs-cmp-row` container, using the
  current version's text as the baseline — words that differ from the current version get `<mark>` tags
- [x] `verse-study.css`: `.vs-cmp-row mark { background: rgba(255, 200, 0, 0.35); border-radius: 2px; padding: 0 1px; }`
  `[data-theme="dark"] .vs-cmp-row mark { background: rgba(200, 160, 0, 0.3); }`

---

### VS-E · Copy Verse Button in Header Actions *(LOW)*

The header has Memorize and Share buttons but no plain copy-to-clipboard. Copying verse text + 
reference is the most common action for messages, notes apps, and documents — faster than the
image builder for text-only use. The verse text is already in `#vs-focal-text` and the ref in
`#vs-header-ref` when the verse loads.

- [x] `verse-study/index.html`: Add `<button id="vs-copy-btn" class="vs-context-btn" type="button" hidden>Copy</button>` to `.vs-header__actions` (after the Share button)
- [x] `verse-study.js` (`loadVerseStudyVerse`): After `focalTextEl.textContent = text`, wire the button:
  ```js
  var copyBtn = document.getElementById('vs-copy-btn');
  if (copyBtn && text) {
    copyBtn.removeAttribute('hidden');
    copyBtn.onclick = function () {
      var ref = (document.getElementById('vs-header-ref') || {}).textContent || '';
      navigator.clipboard.writeText(text + (ref ? ' — ' + ref : '')).then(function () {
        copyBtn.textContent = 'Copied ✓';
        setTimeout(function () { copyBtn.textContent = 'Copy'; }, 1800);
      });
    };
  }
  ```

---

### VS-F · Word Study Flyout — Full Definition Expand *(LOW)*

`_vsRenderWordPanel` truncates `entry.def` at 300 characters and appends `…` with no way to see
the rest. For OT Hebrew entries the most specific lexical notes often appear past that threshold.
The expansion needs only a show/hide toggle on the already-rendered HTML — no re-fetch.

- [x] `verse-study.js` (`_vsRenderWordPanel`): Replace the hard slice with an inline expand:
  ```js
  if (entry.def && entry.def !== entry.gloss) {
    var isLong = entry.def.length > 300;
    html += '<div class="vs-word-panel__def">';
    html += '<span class="vs-wp-def-text">' + escHtml(isLong ? entry.def.slice(0, 300) : entry.def) + '</span>';
    if (isLong) {
      html += '<span class="vs-wp-def-rest" hidden>' + escHtml(entry.def.slice(300)) + '</span>';
      html += ' <button class="vs-wp-def-more" type="button">more…</button>';
    }
    html += '</div>';
  }
  ```
  After `_vsWordPanelEl.innerHTML = html;`, add the expand wire (after the existing `closeBtn` wire):
  ```js
  var moreBtn = _vsWordPanelEl.querySelector('.vs-wp-def-more');
  if (moreBtn) {
    moreBtn.addEventListener('click', function () {
      var rest = _vsWordPanelEl.querySelector('.vs-wp-def-rest');
      if (rest) rest.removeAttribute('hidden');
      moreBtn.remove();
    });
  }
  ```
- [x] `verse-study.css`: `.vs-wp-def-more { background:none; border:none; color:var(--color-accent); font-size:.8rem; cursor:pointer; padding:0; }` `.vs-wp-def-more:hover { text-decoration:underline; }`

---

### VS-G · Commentary — Long-Entry Truncation with Expand *(LOW)*

Commentary HTML is injected verbatim with no length cap. Clarke and JFB entries can run 1,000–2,000
words, forcing the user to scroll through the entire section to reach Parallel Passages and other
sections below. A soft word threshold with a "Read more" expand keeps the page navigable without
hiding content. This should apply after `wireRefLinks` to avoid wiring links that are hidden.

- [x] `verse-study.js` (`vsLoadComm`): After `wireRefLinks(commSec.bodyEl)`, apply a character-count collapse:
  ```js
  var COMM_THRESHOLD = 800;
  var commBody = commSec.bodyEl;
  if (commBody.textContent.length > COMM_THRESHOLD) {
    var wrapper = document.createElement('div');
    wrapper.className = 'vs-comm-truncated';
    while (commBody.firstChild) wrapper.appendChild(commBody.firstChild);
    commBody.appendChild(wrapper);
    var expandBtn = document.createElement('button');
    expandBtn.className = 'vs-comm-expand-btn';
    expandBtn.type = 'button';
    expandBtn.textContent = 'Read more ▾';
    commBody.appendChild(expandBtn);
    expandBtn.addEventListener('click', function () {
      wrapper.classList.remove('vs-comm-truncated--clamped');
      expandBtn.remove();
    });
    wrapper.classList.add('vs-comm-truncated--clamped');
  }
  ```
- [x] `verse-study.css`: `.vs-comm-truncated--clamped { max-height: 14em; overflow: hidden; }` `.vs-comm-expand-btn { display:block; margin-top:.5rem; background:none; border:none; color:var(--color-accent); font-family:var(--font-ui); font-size:.82rem; cursor:pointer; padding:0; }` `.vs-comm-expand-btn:hover { text-decoration:underline; }`

---

### VS-H · Header Height — Wrong scroll-margin-top Until Verse Resolves *(LOW)*

`--vs-header-h` is set inside the `.then()` callback of `loadVerseStudyVerse`, but `loadVerseSections`
is called immediately after (synchronously). The Notes section renders synchronously and is visible
in the nav before the verse text loads — if the user clicks Notes in the sidebar at that point,
`scroll-margin-top` uses the fallback value of `200px`, which may be wrong. Adding an initial
measurement on the first animation frame gives sections a correct offset immediately, without
waiting for the verse fetch to resolve.

- [x] `verse-study.js` (`initVerseStudyPage`): Immediately after wiring event listeners and before
  calling `loadVerseStudyVerse`, add:
  ```js
  requestAnimationFrame(function () {
    var header = document.getElementById('vs-sticky-header');
    if (header) {
      document.documentElement.style.setProperty('--vs-header-h', header.offsetHeight + 'px');
    }
  });
  ```
  The existing post-verse-load measurement in `loadVerseStudyVerse` still runs and corrects the
  value after the verse text (and any token row content) has been added to the header.

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

