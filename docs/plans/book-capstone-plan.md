# Book Capstone Plan — the one Full Treatment per book

> Authored 2026-07-19; **reshaped 2026-07-20** to a single per-book treatment.
> The design spine for the **Studies tool** (`/studies/`): one autonomous loop that
> builds, for every book, **one "Full Treatment" page** — the fullest book-level
> study on the site. Keep this current if the contract changes.
>
> ## 2026-07-20 reshape — three tiers collapsed into one
>
> The earlier three-tier model (Guide + Bible Study Guide + Commentary) was
> **collapsed to remove repetition**. There is now **one page per book**: a rich
> **Intro** (consolidating everything already on the site per book — overview,
> author/date/setting/purpose, themes, outline, **timeline**, key people, key
> vocabulary + language notes, reception, and literary/cultural context) followed
> by the **fully synthesized commentary** in **per-chapter divisions** (each with
> original-language / historical-context / Christ lenses, verse-by-verse notes, the
> Cloud of Witnesses + external scholarship, and an optional "For reflection" set).
> Many-chapter books (Psalms, Isaiah) use a **chapter picker + lazy-load**. The
> separate Guide and Bible-Study-Guide tiers/pages are **retired** (their best
> content folds into the Intro and the per-chapter reflection). Sections below that
> still describe three tiers are historical — the single-treatment model governs.

## The target: the Studies tool

`/studies/` (`src/pages/studies/index.astro`) is a client-rendered grid. It
fetches `data/bible/books.json` + `data/books-content.json` and draws one card
per book with three **tier badges**. A badge is lit when its tier's
`exists` flag is `true`; unbuilt tiers are dashed/dim; a book with no tier at
all is greyed out. `bestUrl()` links each card to the first existing tier in
the order **deep_dive → guide → commentary**.

Today only ~6 books have any tier. **These three loops light up all 66.**

### The three tiers (per book)

| Tier | Display name | What it is | Loop | Output data |
|---|---|---|---|---|
| 1 | **Book Guide** | A general overview — orientation to the whole book | `book-guide-loop.md` | `data/books/guide/<book>.json` |
| 2 | **Bible Study Guide** *(was "Deep Dive")* | Chapter-by-chapter **group session guides** for small groups | `book-study-guide-loop.md` | `data/books/study-guide/<book>.json` |
| 3 | **Commentary** *(capstone)* | The full treatment: various voices, **section by section, then verse by verse within each section** | `book-commentary-loop.md` | `data/commentary/exposition/<book>/` |

Each book is treated on its own logic: sections follow the book's natural
logical structure (pericopes), and within a section the commentary proceeds
verse by verse.

## The "Deep Dive" → "Bible Study Guide" rename

The middle tier is **renamed** everywhere it is user-visible: the `/studies/`
hub copy + badge label, the per-book `bk-tier-nav` label/sub-label on the five
hand-authored books, and the `books-content.json` display context. Its purpose
also shifts — from "scholarly analysis" to **chapter-by-chapter group session
guides**.

**Internal identifiers are retained for URL/data stability** and are *not*
renamed: the `deep_dive` JSON key in `books-content.json`, the `deep-dive`
route slug (`topics/<book>/deep-dive.html`), the `data-tier-item="deep-dive"`
attribute, and the `.studies-tier-badge--deep-dive` CSS class. Only the strings
a reader sees change to "Bible Study Guide". (A later pass may migrate the slug
with redirect stubs; not now.)

The five hand-authored "Deep Dive" pages keep their scholarly content for the
moment; the Bible Study Guide loop supersedes that content with true session
guides as it reaches each book. Tracked in `docs/TODO.md`.

## books-content.json — the contract every loop writes

Per book (66 present, keyed by `books.json` `id`):

```json
"philemon": {
  "guide":      { "exists": false, "url": "topics/philemon/" },
  "deep_dive":  { "exists": false, "url": "topics/philemon/deep-dive.html" },
  "commentary": { "exists": false, "url": "topics/philemon/commentary.html",
                  "coverage": "none", "chapters_done": [], "chapters_total": 1 }
}
```

A loop's final step for a book is to flip its tier's `exists` to `true` (and,
for commentary, update `coverage` / `chapters_done`). This is the single switch
that lights the badge and the card link in the Studies tool. `books-content.json`
is hand-maintained — only `studies/index.astro` reads it; there is no generator.

## Pages: the render layer

All three tiers render as **build-time generated pages** under `src/pages/`,
following the site's `getStaticPaths()` content-page pattern (as biblepedia,
answers, library do). The route contracts already reserved in
`books-content.json`:

- Book Guide → `topics/<book>/` (index)
- Bible Study Guide → `topics/<book>/deep-dive.html`
- Commentary → `topics/<book>/commentary.html`

**This session builds the Commentary page** (the capstone the owner asked for),
as `src/pages/topics/[book]/commentary.astro` — a dynamic route whose
`getStaticPaths()` iterates `books.json` and emits a page for every book that
has `data/commentary/exposition/<book>/_book.json`. It coexists with the five
literal `topics/<book>/` dirs (which contain `index.astro`/`deep-dive.astro`
but no `commentary.astro`), so it may include those books too — no route
conflict. Guide + Bible-Study-Guide generated pages are a defined follow-on
(they reuse the finished `book-study.css` `bk-*` template; see TODO), so the
loops that feed them can run now and their pages light up next.

The five literal book dirs are exempt from the generated Guide/Study-Guide
routes via a slug-exclusion set in `getStaticPaths()` (documented in each page).

## Data schemas

### Tier 1 — `data/books/guide/<book>.json`
```json
{
  "id": "philemon",
  "one_line": "…",
  "orientation": "<html>",        // what this book is; why it's in the canon
  "how_to_read": "<html>",        // posture, pace, what to watch for
  "structure": [ { "label": "…", "range": "1-7", "gist": "…" } ],
  "christ_in_book": "<html>",
  "key_passages": [ { "ref": "Philemon 1:6", "why": "…" } ],
  "themes": ["reconciliation", "…"],
  "_source": { "kind": "book-guide", "method": "ai-assisted", "generated": "YYYY-MM-DD",
               "inputs": ["data/books/introductions/philemon.json", "…"] }
}
```

### Tier 2 — `data/books/study-guide/<book>.json`
Chapter-by-chapter group session guides.
```json
{
  "id": "philemon",
  "intro": "<html>",              // how to use these sessions
  "sessions": [
    {
      "session": 1,
      "title": "…",
      "range": "1-7",             // chapter(s) or logical block this session covers
      "big_idea": "<html>",
      "open": "…",                // ice-breaker / opening question
      "observe": ["…"],           // observation questions (what does it say?)
      "interpret": ["…"],         // interpretation questions (what does it mean?)
      "apply": ["…"],             // application questions (so what?)
      "pray": "…",                // a closing prayer prompt
      "leader_notes": "<html>"    // answers/watch-outs for the facilitator
    }
  ],
  "_source": { "kind": "study-guide", "method": "ai-assisted", "generated": "YYYY-MM-DD", "inputs": ["…"] }
}
```
Session granularity is per book: usually one session per chapter, but short
books group logically (e.g. Philemon = 1 chapter → 2–3 sessions) and long
narrative blocks may span chapters.

### Tier 3 — `data/commentary/exposition/<book>/` (the capstone)
Two file kinds per book, mirroring the site's existing book-level /
per-chapter split (cf. `data/synthesis/<book>.json` + `<book>/<ch>.json`). The
commentary is the **full synthesis** — for each section and verse, as many
perspectives as the text warrants: original language, historical context, Christ,
the Cloud of Witnesses, and attributed external scholarship (rendered as
per-section "lens" blocks on the page).

**`_book.json`** — book-level commentary overview:
```json
{
  "id": "philemon", "title": "Philemon", "testament": "NT", "genre": "epistle",
  "overview": {
    "argument": "<html>", "occasion": "<html>", "theology": "<html>", "christ": "<html>",
    "structure": [ { "label": "…", "range": "1-7", "gist": "…" } ]
  },
  "witnesses": ["John Chrysostom", "…"],     // internal COW voices drawn on across the book
  "external":  [ { "name": "…", "work": "…", "year": "…", "note": "…" } ],  // attributed, no verbatim copying
  "ai_assisted": true,
  "_source": { "kind": "commentary", "method": "ai-assisted", "generated": "YYYY-MM-DD",
               "inputs": ["data/commentary/cow/philemon/1.json",
                          "data/commentary/cow-synthesis/philemon/1.json",
                          "external scholarship (attributed)"] }
}
```

**`<ch>.json`** — per chapter, keyed by pericope **start verse**, section →
verse-by-verse:
```json
{
  "1": {
    "pericope_label": "Greeting",
    "range": "1-3",
    "exposition": "<html>",           // flowing commentary on the section (gets the illuminated drop cap)
    "original_language": "<html>",    // optional — key Greek/Hebrew terms; what English loses
    "historical_context": "<html>",   // optional — setting / background behind the section
    "christ": "<html>",               // optional — Christ in this section
    "verses": [
      { "v": "1", "note": "<html>" }, // verse-by-verse, weaving witnesses + perspectives inline
      { "v": "2", "note": "<html>" }
    ],
    "witnesses": [ { "voice": "John Chrysostom", "tradition": "eastern", "point": "…" } ],
    "external":  [ { "name": "…", "point": "…" } ],
    "application": "<html>"           // optional
  }
}
```
Verse keys mirror the source `cow/<book>/<ch>.json` exactly — never renumber.
Scripture refs are always `<a class="ref" data-ref="Philemon 1:6">v.6</a>`.

## Provenance (works with the Provenance loop)

The Commentary and Guide/Study-Guide artifacts are **AI-assisted** and must say
so. Every generated file carries a top-level `_source` object (schema above);
the commentary `_book.json` also carries `"ai_assisted": true`. The commentary
page renders an "AI-assisted · attributed sources" badge (the site's existing
`src-badge--ai` treatment). External scholarship is **named and summarized,
never copied verbatim** — the same posture the COW synthesis uses for its
witnesses. This keeps the [provenance loop](../agents/provenance-loop.md) able
to validate `_source` presence across the new trees.

## The pipeline (combined, gated) — how ordering works

The three tiers run as **one gated pipeline per book**: Guide → Bible Study Guide
→ Commentary, each stage startable only after the previous is `✅` (Guide starts
from 0). Ordering, claims, and the reframe backlog are governed by a **single
tracker**, not per-loop frontiers:
[agents/study-pipeline.md](../agents/study-pipeline.md) +
[agents/study-pipeline-tracker.md](../agents/study-pipeline-tracker.md). Each
iteration: claim a tracker cell → do the stage → validate → flip
`books-content.json` → mark the tracker `✅`, all in one commit. The three stage
docs own each stage's schema and quality bar; the pipeline owns the order.

## Reframing the hand-authored books

Four books already have hand-authored pages whose content is **mis-tiered** under
the new definitions (`romans`, `psalms`, `revelation`, `hebrews`; the topical
`sermon-on-the-mount` is not a tracked book). Their Guide/Study-Guide stages
**re-sort existing content** into the correct tier rather than writing cold —
marked `♻️` in the tracker.

**Worked example — Hebrews** (its two pages are effectively swapped):
- `study-guides/hebrews/` ("Study Guide") is a 13-chapter chapter-by-chapter study
  (*The Argument* + OT-background boxes + discussion questions) → this is
  **Bible Study Guide** (Tier 2) content: one session per chapter.
- `topics/hebrews/deep-dive.astro` ("Bible Study Guide") is a book overview (hero,
  facts, outline, genre & rhetorical structure) → **morph into the Guide**
  (Tier 1): orientation, how-to-read, structure, Christ, key passages, themes.
Then Commentary (Tier 3) is generated fresh as the full synthesis. Full procedure:
[agents/study-pipeline.md](../agents/study-pipeline.md) ("Reframe rule").

## Validation

`python scripts/validate-commentary.py` guards the commentary tree (verse keys
mirror source; refs linked; `_source` present; `ai_assisted` true; sections
non-empty). The Guide/Study-Guide trees are guarded by lightweight shape checks
in the same script (`--guide` / `--study-guide` modes). Wired into
`validate.yml` alongside the existing data/library/synthesis validators. Loops
**must pass the validator before committing**, per repo policy.

## Illuminated styling (Commentary tier only)

The Commentary page — the capstone — gets an **illuminated-on-paper** treatment
(see `assets/css/commentary.css`): Daylight's paper-white ground kept, plus
drop caps (Literata 900), gilt/brass rule ornaments, ember rubric section
heads, and parchment-tinted witness panels, built on the existing
parchment/gold token set and the `color-mix(var(--color-accent) N%, transparent)`
tint idiom. **No new font** — the offline/no-external-fonts invariant holds.
Genre tint comes from the `bk-<genre>` `--bk-accent` already on `<body>`. A
specimen is added to `/design/`. Guide + Bible-Study-Guide pages keep the plain
`bk-*` book-study styling; only the capstone is illuminated.

## Commit conventions (per loop)

- Guide:        `Book guide: <book>`
- Study Guide:  `Bible study guide: <book> (<N> sessions)`
- Commentary:   `Commentary: <book> <ch> (<N> verses)` and
                `Commentary: <book> overview` for `_book.json`

Do not push — pushes deploy production and need owner approval. Update
`docs/TODO.md` + `docs/STATUS.md` in the same commit as substantive work.
