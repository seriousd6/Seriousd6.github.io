> Reconstructed 2026-07-19 from the public About page (src/pages/about/index.astro), the only surviving copy after the original gitignored working/ files were lost from this clone. Companion guides referenced below (e.g. TRANSLATION_AGENT_GUIDE.md, BS_AGENT_GUIDE.md, MKT_PROGRESS.md, site-overview.md) are still pending recovery from the owner's other machine — treat missing references accordingly.

# Book Study Agent Prompt

This prompt runs in a loop — each session claims one book, generates its supplemental data,
runs the script, and updates the tracker. Each run is fully self-contained.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `BS_AGENT_GUIDE.md`
2. `BS_SCRIPT_GUIDE.md`
3. `BS_PROGRESS.md`

---

## Step 1 — Find and claim a work unit

### 1a. Find the first unclaimed book

Scan the `BS_PROGRESS.md` table. Find the first row where **Status** is `not started`.
Evaluate stale in-progress claims using a 2-hour staleness rule:

| Status | Action |
|--------|--------|
| `not started` | Candidate — proceed to 1b |
| `in-progress @ <timestamp>` where timestamp < 2 hours old | Skip — another agent is working this book |
| `in-progress @ <timestamp>` where timestamp ≥ 2 hours old | Candidate — treat as abandoned |
| `complete` | Skip |

### 1b. Verify the output file does not already exist

  import os
  book_id = 'romans'
  path = f'data/workshop/book-study/{book_id}.json'
  print('exists:', os.path.exists(path))

If the file exists and has all four required fields, the book is already complete.
Update its Status to `complete` in the tracker and move to the next candidate.

### 1c. Claim it

Set the row's Status to `in-progress @ <timestamp>` and save `BS_PROGRESS.md`.
Re-read the file to confirm the save took effect.

---

## Step 2 — Study the source material

Read these files for your claimed book:

1. `data/books/introductions/{bookId}.json` — **read this carefully**. Do not reproduce
   any of this in your script output. Your job is to add what this file lacks.
2. `data/literary/genre.json` — find the entry for your book. Read `literary_note`
   and `structure_note`. Use this to inform `language_notes`.
3. `data/cultural/book-context.json` — find the entry for your book. Use this to
   inform `reception` and `reading_guide`.
4. Run the vocabulary finder from `BS_AGENT_GUIDE.md` Section 5 to identify
   characteristic vocabulary candidates. Print the top 25 and decide which 12–18 to
   include based on theological weight in this specific book.

---

## Step 3 — Write the script

Follow `BS_SCRIPT_GUIDE.md` exactly. Required structure:

1. **Header docstring** — book name, book_id, lang, run command, author group used,
   any non-obvious decisions
2. **Boilerplate** — copy `load_book_study`, `save_book_study`, `merge_book_study`
   verbatim from the guide
3. **Content dictionary** — `BOOK_STUDY = { "bookId": ..., "key_vocabulary": [...],
   "language_notes": "...", "reception": "...", "reading_guide": "..." }`
4. **`main()`** — loads existing, calls `merge_book_study`, saves

Content principles from `BS_AGENT_GUIDE.md` Section 3 are non-negotiable.

---

## Step 4 — Run and verify

  python3 scripts/build-book-study-{bookId}.py

All assertions must pass. Spot-check:
- Read two or three `significance` notes — do they add real interpretive value?
- Read the first paragraph of `language_notes` — is it specific to this book?

If anything falls short, edit the script content dictionary in place, re-run, re-verify.

---

## Step 5 — Update the tracker

Edit `BS_PROGRESS.md` in a **single save**:
1. Set your book's Status to `complete`
2. Mark the four field columns with ✓
3. Update the `Last updated:` line to today's date
4. Increment the relevant counter in the Summary section

---

## Key facts

- **Do not reproduce** content from `data/books/introductions/{bookId}.json`
- `merge_book_study()` never overwrites existing non-empty fields — safe to re-run
- HTML in text fields uses `<p>`, `<strong>`, `<em>` only — no headings or lists
- Small epistles (Philemon, 2–3 John, Jude, Obadiah) may have 8–10 vocab entries
- If context runs short mid-book, save what you have (partial is better than nothing)

---

# BS Agent Guide (excerpt)

> Second section: the only surviving excerpt of the full BS Agent Guide (originally `working/BS_AGENT_GUIDE.md`, to be restored as `docs/bs_agent_guide.md` — pending recovery), as published on the About page. It defines the quality standards for key vocabulary, language notes, reception, and reading guide.

## What the Book Study adds (summary of BS_AGENT_GUIDE.md)

### key_vocabulary (12–18 entries per book)
The most characteristic vocabulary of the book, selected by two criteria:
1. Author-distinctive words — Strong's codes where the `peak` author matches this book's
   author group in author-frequency data
2. Theologically significant within this book — words that carry interpretive weight here
   specifically

Each entry includes a `significance` note: "2–3 sentences. WHY this word matters in this
specific book — not a generic definition. The theological/literary/rhetorical load it
carries here, what its semantic range implies that English loses, and how understanding
the original changes interpretation."

Quality bar: "Paul uses this 33× in Romans (his highest density anywhere) always in the
forensic register — God's declarative act, not a moral quality the believer develops" is
the target. "This word means X" is not enough.

### language_notes (400–700 words, HTML)
3–5 paragraphs on what the original language specifically reveals in this book.
Not generic grammar — observations about THIS book.

For NT Greek books:
- Characteristic aspect choices (e.g., John's use of perfect tense for abiding states)
- Particle patterns and what they reveal about argument structure
- Key Greek idioms or constructions opaque in English
- Genre-specific language features

For OT Hebrew books:
- Root-play and wordplay that disappears in English
- Binyan choices that signal theological meaning
- Poetic structure if applicable
- Narrative grammar — waw-consecutive chains, fronting for emphasis

### reception (300–400 words, HTML)
A concise survey of how this book has been read through church history.
One paragraph per major tradition:
- Patristic — which fathers engaged it most and their signature interpretive moves
- Medieval — notable allegorical or scholastic readings if relevant
- Reformation — Luther, Calvin, or Zwingli if they wrote on it; the interpretive shift
- Modern — the one or two critical debates that define contemporary scholarship

A short paragraph that illuminates is better than a list of names.

### reading_guide (200–300 words, HTML)
- What to watch for as you read verse by verse
- The single most important thing to understand before starting
- Common misreadings to avoid (with a sentence on why they happen)
- Where to start if dipping in rather than reading sequentially

### What NOT to do
- Do not reproduce content from data/books/introductions/{bookId}.json
- Do not write significance notes that just restate the dictionary gloss
- Do not add language_notes that are generic ("Greek has cases")
- Do not write reception that is just a list of names without interpretive content
