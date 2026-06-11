/clear
# Book Study Agent Prompt

This prompt runs in a loop — each session claims one book, generates its supplemental data, runs the script, and updates the tracker. Each run is fully self-contained.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `BS_AGENT_GUIDE.md`
2. `BS_SCRIPT_GUIDE.md`
3. `BS_PROGRESS.md`

---

## Step 1 — Find and claim a work unit

### 1a. Find the first unclaimed book

Scan the `BS_PROGRESS.md` table. Find the first row where **Status** is `not started`. Evaluate stale in-progress claims using the same 2-hour rule as the Z commentary agent:

| Status | Action |
|--------|--------|
| `not started` | Candidate — proceed to 1b |
| `in-progress @ <timestamp>` where timestamp **< 2 hours** old | Skip — another agent is working this book |
| `in-progress @ <timestamp>` where timestamp **≥ 2 hours** old | Candidate — treat as abandoned |
| `complete` | Skip |

Check the timestamp age with Python:
```python
from datetime import datetime, timezone, timedelta
raw = 'in-progress @ 2026-06-07T14:30:00Z'  # ← paste the cell value
ts = datetime.fromisoformat(raw.split('@ ')[1].strip().replace('Z', '+00:00'))
age = datetime.now(timezone.utc) - ts
print('age:', age, '— stale' if age > timedelta(hours=2) else '— active, SKIP')
```

### 1b. Verify the output file does not already exist

```python
import os
book_id = 'romans'  # ← your candidate
path = f'data/workshop/book-study/{book_id}.json'
print('exists:', os.path.exists(path))
```

If the file exists and has all four required fields (`key_vocabulary`, `language_notes`, `reception`, `reading_guide`), the book is already complete. Update its Status to `complete` in the tracker and move to the next candidate.

### 1c. Claim it

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
```

Set the row's Status to `in-progress @ <timestamp>` and save `BS_PROGRESS.md`. Re-read the file to confirm the save took effect.

---

## Step 2 — Study the source material

Read these files for your claimed book:

1. `data/books/introductions/{bookId}.json` — **read this carefully**. It already has author, date, outline, themes_detail, christ_connection, etc. Do not reproduce any of this in your script output. Your job is to add what this file lacks.

2. `data/literary/genre.json` — find the entry for your book. Read `literary_note` and `structure_note`. Use this to inform `language_notes`.

3. `data/cultural/book-context.json` — find the entry for your book. Read `historical_context` and `key_cultural_notes`. Use this to inform `reception` and `reading_guide`.

4. Run the vocabulary finder from `BS_AGENT_GUIDE.md` Section 5 to identify characteristic vocabulary candidates. Print the top 25 and decide which 12–18 to include based on theological weight in this specific book.

```python
import json

# Change these two values for your book
book_id      = 'romans'
author_group = 'Paul'      # see BS_AGENT_GUIDE.md Section 4 for the mapping
lang         = 'greek'     # 'greek' for NT, 'hebrew' for OT

freq     = json.load(open(f'data/grammar/author-freq-{lang}.json'))
glossary = json.load(open(f'data/translation/glossary-{lang}.json'))

candidates = [
    (code, data)
    for code, data in freq.items()
    if data.get('peak') == author_group
]
candidates.sort(key=lambda x: x[1]['rates'].get(author_group, 0), reverse=True)

print(f'Top 25 characteristic {lang} words for {author_group}:\n')
for code, data in candidates[:25]:
    g = glossary.get(code, {})
    rate  = data['rates'].get(author_group, 0)
    gloss = g.get('tiers', {}).get('literal', {}).get('primary', g.get('gloss', ''))
    srange = (g.get('semantic_range') or '')[:70]
    print(f"  {code:8} {(g.get('lemma') or ''):22} '{gloss:22}' rate={rate:.2f}  {srange}")
```

Also look up the specific glossary entry for any word you plan to include, to get the full `semantic_range` text you can reference in your `significance` note:

```python
code = 'G1343'
entry = json.load(open(f'data/translation/glossary-{lang}.json')).get(code, {})
print('lemma:', entry.get('lemma'))
print('translit:', entry.get('translit'))
print('gloss:', entry.get('tiers', {}).get('literal', {}).get('primary'))
print('semantic_range:', entry.get('semantic_range'))
```

---

## Step 3 — Write the script

Follow `BS_SCRIPT_GUIDE.md` exactly. Required structure:

1. **Header docstring** — book name, book_id, lang, run command, author group used, any non-obvious decisions
2. **Boilerplate** — copy `load_book_study`, `save_book_study`, `merge_book_study` verbatim from the guide
3. **Content dictionary** — `BOOK_STUDY = { "bookId": ..., "key_vocabulary": [...], "language_notes": "...", "reception": "...", "reading_guide": "..." }`
4. **`main()`** — loads existing, calls `merge_book_study`, saves

Content principles from `BS_AGENT_GUIDE.md` Section 3 are non-negotiable.

---

## Step 4 — Run and verify

```bash
python3 scripts/build-book-study-{bookId}.py
```

Then run the verification script from `BS_SCRIPT_GUIDE.md` Section 6, changing `book_id` to your book. All assertions must pass before you mark the row complete.

Spot-check the output manually:
- Open `data/workshop/book-study/{bookId}.json`
- Read two or three `significance` notes — do they add real interpretive value beyond a dictionary gloss?
- Read the first paragraph of `language_notes` — is it specific to this book, or generic?

If anything falls short of the quality bar in `BS_AGENT_GUIDE.md`, edit the script content dictionary in place, re-run, and re-verify.

---

## Step 5 — Update the tracker

Edit `BS_PROGRESS.md` in a **single save**:

1. Set your book's Status to `complete`
2. Mark the four field columns (`key_vocab`, `language_notes`, `reception`, `reading_guide`) with `✓`
3. Update the `Last updated:` line at the top to today's date
4. Increment the relevant counter in the Summary section

Re-read `BS_PROGRESS.md` after saving to confirm the `in-progress` text is gone.

---

## Key facts

- **Do not reproduce** content from `data/books/introductions/{bookId}.json` — the UI reads that file directly and merges it at render time
- **`merge_book_study()` never overwrites** existing non-empty fields — safe to re-run at any time
- Script output path: `data/workshop/book-study/{bookId}.json`
- Run all scripts from the **repo root** (`python3 scripts/build-book-study-{bookId}.py`)
- `bookId` is lowercase with no spaces: `1corinthians`, `songofsolomon`, `1peter`, etc.
- HTML in `language_notes`, `reception`, `reading_guide` uses `<p>`, `<strong>`, `<em>` only — no headings or lists
- Small epistles (Philemon, 2–3 John, Jude, Obadiah) may have 8–10 vocab entries; all others 12–18
- If context runs short mid-book, save what you have (partial is better than nothing) and note in the tracker which fields are complete

After completing this iteration, run /compact before calling ScheduleWakeup.
