# Bible Study Guide Loop — procedure

> Authored 2026-07-19. Fills **Tier 2 (Bible Study Guide)** of the Studies tool
> for every book of the Bible. This tier was formerly called "Deep Dive"; see the
> rename note in [../plans/book-capstone-plan.md](../plans/book-capstone-plan.md).
> Keep this current if the contract changes.

## What it is

The **Bible Study Guide** is a set of **chapter-by-chapter group session guides**
— what a small group works through together, session by session. Each session
covers a chapter (or a logical block of chapters for short/narrative books) and
runs the group from opening question through observation → interpretation →
application → prayer, with facilitator notes. One book per iteration.

It is **not** the orienting [Book Guide](book-guide-loop.md) (Tier 1) and not the
[Commentary](book-commentary-loop.md) (Tier 3). This tier is practical and
group-facing; keep questions open, discussable, and grounded in the text.

## Data layout

| Tree | Role |
|---|---|
| `data/books/introductions/<book>.json` | INPUT — book intro / outline |
| `data/workshop/book-study/<book>.json` | INPUT — vocab, language notes, reception, reading guide |
| `data/synthesis/<book>/<ch>.json` | INPUT — per-pericope five-domain synthesis (where present) |
| `data/bible/BSB/<book>.json` | INPUT — the text itself (for observation questions grounded in the words) |
| `data/books/study-guide/<book>.json` | OUTPUT — the session guides (schema below) |

## Frontier rule

Walk `data/bible/books.json` in canonical order; next unit = **first book whose
`data/books/study-guide/<book>.json` is missing.**

## Output schema — `data/books/study-guide/<book>.json`

```json
{
  "id": "<book id>",
  "intro": "<html>",              // 1 short paragraph: how to use these sessions
  "sessions": [
    {
      "session": 1,
      "title": "…",
      "range": "1-7",             // chapter(s) / logical block this session covers
      "big_idea": "<html>",       // 1–2 sentences naming the session's central point
      "open": "…",                // one warm opening / ice-breaker question
      "observe":  ["…", "…"],     // 2–4 "what does the text say?" questions (grounded in specific verses)
      "interpret":["…", "…"],     // 2–4 "what does it mean?" questions
      "apply":    ["…", "…"],     // 2–3 "so what?" application questions
      "pray": "…",                // one closing prayer prompt
      "leader_notes": "<html>"    // facilitator answers, watch-outs, key cross-refs
    }
  ],
  "_source": {
    "kind": "study-guide", "method": "ai-assisted", "generated": "YYYY-MM-DD",
    "inputs": ["data/books/introductions/<book>.json", "data/synthesis/<book>/…"]
  }
}
```

- Session count is per book. Default: **one session per chapter.** Short books
  group logically (Philemon's 1 chapter → 2–3 sessions by movement); long
  narrative arcs may span chapters. Never split a pericope across two sessions.
- Questions carry embedded refs where they point at a verse:
  `<a class="ref" data-ref="Philemon 1:6">v.6</a>`. Questions in the arrays are
  plain strings that MAY contain that anchor HTML.
- `leader_notes` HTML: `<p>`, `<strong>`, `<em>`, `<a class="ref">` only.

## Per-book procedure

1. **Study one finished study-guide first** (once any exist); match the voice
   and question style. Skim the five hand-authored `/study-guides/` pages
   (ephesians, hebrews, psalms, romans-1-8, sermon-on-the-mount) as the quality
   reference for tone.
2. Read the input files; skim the actual BSB text of each chapter so observation
   questions cite real wording, not generic prompts.
3. Decide the session breakdown from the book's structure (use the intro outline
   / synthesis pericopes). Write `data/books/study-guide/<book>.json`.
4. **Validate**: `python scripts/validate-commentary.py --study-guide <book>`.
5. Commit exactly: `Bible study guide: <book> (<N> sessions)`. When the generated
   page route is live, flip `books-content.json` →
   `books.<book>.deep_dive.exists = true` in the same commit (the internal key
   stays `deep_dive`; only the display name is "Bible Study Guide"). Do not push.

## Quality bar

- Questions must be **answerable from the text** and genuinely open — no yes/no
  filler, no questions that presuppose their answer.
- Observation before interpretation before application, every session.
- `leader_notes` give a real facilitator something to say — the likely answers,
  the common wrong turn, the cross-reference that unlocks it.
- Group-usable: a leader with this guide and a Bible can run the session.

## Tracker (dashboard — data tree is the source of truth)

| Metric | Value |
|---|---|
| Books with a study guide | derive: count `data/books/study-guide/*.json` |
| Total books | 66 |
| Frontier | first book (canonical order) missing `study-guide/<book>.json` |

Hand-authored middle-tier ("Deep Dive") pages exist for `romans`, `psalms`,
`revelation`, `hebrews`, `sermon-on-the-mount`; their content is scholarly
analysis and is **superseded** by this loop's session guides as it reaches them.
