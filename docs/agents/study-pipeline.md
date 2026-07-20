# Book Treatment loop — the single per-book study

> Reshaped 2026-07-20. There is now **one "Full Treatment" page per book** — the
> three tiers (Guide / Bible Study Guide / Commentary) were collapsed to remove
> repetition. This loop fills the Studies tool (`/studies/`) with that treatment
> for all 66 books. Architecture: [../plans/book-capstone-plan.md](../plans/book-capstone-plan.md).
> Per-unit schema + quality bar: [book-commentary-loop.md](book-commentary-loop.md).

## What a "Full Treatment" is

One page per book (`/topics/<book>/commentary.html`):

1. A rich **Intro** that consolidates everything the site already holds per book —
   overview, author/date/setting/purpose, themes, outline, **timeline**, key
   people, key vocabulary + language notes, reception, and literary/cultural
   context. **The page assembles these automatically** from the existing data
   trees (`introductions`, `workshop/book-study`, `literary`, `cultural`).
2. The fully synthesized **Commentary** in per-chapter divisions — original-language
   / historical-context / Christ lenses, verse-by-verse notes, the Cloud of
   Witnesses + attributed external scholarship, and a per-chapter "For reflection"
   set. Many-chapter books get a chapter picker + lazy-load.

## What the loop actually writes

The intro's source data already exists for all 66 books — the page renders it. The
loop's job is the **commentary**:

- `data/commentary/exposition/<book>/_book.json` — overview (argument, occasion,
  theology, Christ, structure) + witnesses/external + `_source` provenance.
- `data/commentary/exposition/<book>/<ch>.json` — per chapter: an optional `_meta`
  (`title` + `reflection` questions) plus section-keyed entries (section →
  verse-by-verse, with the `original_language` / `historical_context` / `christ`
  lenses, `witnesses`, `external`, `application`).

Full schema + quality bar (the multi-perspective synthesis): [book-commentary-loop.md](book-commentary-loop.md).

## The tracker

[study-pipeline-tracker.md](study-pipeline-tracker.md) — one row per book, one
**Treatment** column. Statuses: `⬜` todo · `🔄 @<ISO-time> <agent> (n/N ch)` in
progress · `✅` done (overview + all chapters exist and validate) · `♻️` reframe.
Claim a cell, do the work, validate, flip `books-content.json`, mark `✅` — one
commit. A `🔄` older than 3h is stale and may be reclaimed.

## Frontier

Walk `data/bible/books.json` in canonical order; the next book is the first `⬜`/`♻️`
Treatment cell (or resume a `🔄` you own). There is **no gating between stages** —
it is one stage now. Reference exemplar: **Philemon** (overview + ch 1, all 25
verses, multi-perspective + reflection). Reframe exemplar: **Hebrews**.

## Reframe — hand-authored books (`romans`, `psalms`, `revelation`, `hebrews`)

These already have hand-authored overview + chapter-study pages. Their content
**feeds the treatment**: the book overview → the Intro; the chapter-by-chapter
study (e.g. Hebrews' *The Argument* + OT-background boxes) → the per-chapter
commentary + reflection. Once a book's treatment exists, retire/redirect its old
literal pages (`topics/<book>/index.astro`, `deep-dive.astro`,
`study-guides/<book>/`) — tracked in `docs/TODO.md`. (`sermon-on-the-mount` is a
topic, not a `books.json` id, and is not a tracked book.)

## Per iteration

1. Claim the book's Treatment cell in the tracker (`🔄`).
2. Write `_book.json` (if missing), then chapters `1..N` — the source
   `cow/<book>/<ch>.json` always exists.
3. Validate: `python scripts/validate-commentary.py --overview <book>` /
   `--chapter <book> <ch>` — must pass clean.
4. Commit: `Commentary: <book> overview` and `Commentary: <book> <ch> (<N> verses)`.
   In the same commit, flip `data/books-content.json` →
   `books.<book>.commentary.exists = true` (+ `coverage` / `chapters_done`) and
   update the tracker. **Do not push** — deploys need owner approval.
5. Mark `✅` only when `_book.json` and every chapter exist.
