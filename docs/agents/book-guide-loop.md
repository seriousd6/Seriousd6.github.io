# Book Guide Loop — procedure

> Authored 2026-07-19. Fills **Tier 1 (Book Guide)** of the Studies tool for
> every book of the Bible. See [../plans/book-capstone-plan.md](../plans/book-capstone-plan.md)
> for how the three tiers fit together. Keep this current if the contract changes.

## What it is

The **Book Guide** is a general, reader-facing overview of a whole book — the
orientation someone reads *before* studying it: what the book is, why it is in
the canon, how to read it, its shape, its themes, where Christ is in it, and the
handful of passages to know. One book per iteration by an autonomous loop.

It is **not** the chapter-by-chapter [Bible Study Guide](book-study-guide-loop.md)
(Tier 2) and not the [Commentary](book-commentary-loop.md) (Tier 3). Keep it
short and orienting — depth belongs to the other two tiers.

## Data layout

| Tree | Role |
|---|---|
| `data/books/introductions/<book>.json` | INPUT — existing book intro (author/date/setting/purpose/themes/outline) |
| `data/workshop/book-study/<book>.json` | INPUT — existing per-book study data (vocab, language, reception, reading guide) |
| `data/literary/genre.json`, `data/cultural/book-context.json` | INPUT — shared genre + context data (book-keyed inside) |
| `data/books/guide/<book>.json` | OUTPUT — the Book Guide (schema below) |

The loop **composes** the existing input data; it does not re-derive it. Its job
is the orienting overview those files lack.

## Frontier rule (how the loop knows what's next)

Progress is derived from the data tree — no tracker file is authoritative. Walk
`data/bible/books.json` in canonical order; the next work unit is the **first
book whose `data/books/guide/<book>.json` is missing.**

## Output schema — `data/books/guide/<book>.json`

```json
{
  "id": "<book id from books.json>",
  "one_line": "One sentence naming the book's burden.",
  "orientation": "<html>",        // 2–4 short paragraphs: what this book is, its occasion, why it matters
  "how_to_read": "<html>",        // 1–2 paragraphs: posture, pace, what to watch for, common misreadings
  "structure": [                  // the big-picture shape (4–8 movements)
    { "label": "…", "range": "1-7", "gist": "one line" }
  ],
  "christ_in_book": "<html>",     // 1–2 paragraphs: how the book points to / reveals Christ
  "key_passages": [ { "ref": "Philemon 1:6", "why": "one line" } ],
  "themes": ["short strings"],
  "_source": {
    "kind": "book-guide", "method": "ai-assisted", "generated": "YYYY-MM-DD",
    "inputs": ["data/books/introductions/<book>.json", "data/workshop/book-study/<book>.json"]
  }
}
```

- HTML in prose fields: `<p>`, `<strong>`, `<em>`, and `<a class="ref" data-ref="…">`
  only — no headings or lists inside a field.
- Scripture references are **always** anchored: `<a class="ref" data-ref="Book Ch:V">v.6</a>`
  (chapter-only citations point at verse 1). Never a bare "Book Ch:V".

## Per-book procedure

1. **Study one finished guide first** (once any exist) and skim the input files
   for your claimed book. Match the established voice.
2. Read `introductions/<book>.json`, `workshop/book-study/<book>.json`, the
   book's `genre.json` and `book-context.json` entries. **Do not reproduce** their
   content — distil and orient.
3. Write `data/books/guide/<book>.json` per the schema. Keep it tight: the whole
   guide should read in a few minutes. `orientation` ≈ 150–300 words;
   `how_to_read` ≈ 80–160; `christ_in_book` ≈ 80–160.
4. **Validate**: `python scripts/validate-commentary.py --guide <book>` must pass
   (shape, non-empty fields, every ref linked, `_source` present).
5. Commit exactly: `Book guide: <book>`. When the generated Guide page route is
   live, also flip `books-content.json` → `books.<book>.guide.exists = true` in
   the same commit. Scratch work in `scratchpad/` (gitignored). Do not push.

## Quality bar

- Orienting, not exhaustive. If a sentence belongs in the study guide or the
  commentary, it does not belong here.
- Grounded in the book and the input data; never invent history or authorship
  claims the sources don't support.
- Vary structure book to book; let each book's own shape lead.

## Tracker (dashboard — data tree is the source of truth)

| Metric | Value |
|---|---|
| Books with a guide | derive: count `data/books/guide/*.json` |
| Total books | 66 |
| Frontier | first book (canonical order) missing `guide/<book>.json` |

Hand-authored Guide pages already exist for: `romans`, `psalms`, `revelation`,
`hebrews`, `sermon-on-the-mount` (topic pages). The loop may still generate their
`guide/<book>.json` data for the generated-page path, but their `guide.exists`
is already `true` in `books-content.json`.
