# BP Agent Guide — Biblepedia Article Synthesis

## What this loop does

Generates a synthesized article stub for every topic in Biblepedia's dictionary layer.
Each stub is a short, scholar-level wiki introduction (150–300 words) that unifies the
Easton's, Smith's, ISBE, and Hitchcock sources into a single coherent lede — before the
raw source expansions the user can open below.

The synthesis does NOT replace the raw source text. It is the **opening section** of the
Biblepedia article: the part a reader sees first. Raw source articles (Easton, Smith, ISBE)
remain as collapsible "Full entry →" expansions.

---

## Files to read in order before starting

1. `BP_SCRIPT_GUIDE.md` — exact script format, boilerplate, schema, quality rules
2. `BP_PROGRESS.md` — work queue; claim your unit before starting any work

---

## Prerequisites — gap analysis must be complete first

**Before doing any work**, open `BPG_PROGRESS.md` and check the Phase 3 row in the Summary table.

- If Phase 3 status is **not** `complete`, stop immediately. Do not claim a unit, do not write any script. Output this message and nothing else:

  > **BP loop blocked.** Gap analysis is not finished. All gaps must be curated and stub-needed items transferred to BP_PROGRESS.md (BPG Phase 3 complete) before article synthesis begins. Run the BPG loop first.

- If Phase 3 status is `complete`, proceed to the workflow below.

---

## Session workflow (every session, no exceptions)

### 1. Claim a unit

Open `BP_PROGRESS.md`. Find the **first row** with status `not started`. Set its status to:

```
in-progress @ <ISO-8601-UTC-timestamp>
```

Example: `in-progress @ 2026-06-10T14:30:00Z`

Save the file. Re-read it to confirm the save landed (race guard).

If all units are `complete` or `in-progress @ <recent-timestamp>` (< 40 minutes old), stop — no work to do.

A claim is stale if the timestamp is > 40 minutes old. You may reclaim a stale unit.

### 2. Load the source data for your unit

Your unit covers a letter+range (e.g., "A1: Aaron → Acre"). Load from these files:
- `../data/dictionary/index.json` — Easton index (id, term, brief)
- `../data/smith/index.json` — Smith index (id, term, brief)
- `../data/isbe/index.json` — ISBE index (id, term, brief)
- `../data/hitchcock/index.json` — Hitchcock names (id, term, meaning)

For each entry in your range, also load the full Easton entry if it exists:
- `../data/dictionary/{slug}.json` — full HTML + refs array

You do NOT need to load Smith or ISBE full entries for stubs — the index `brief` field is sufficient.

### 3. Check existing output

Check `../data/biblepedia/articles/` for any already-generated files in your range.
Do not regenerate existing articles (the merge function handles this, but verify first).

### 4. Write the synthesis script

Follow `BP_SCRIPT_GUIDE.md` exactly. Key rules:

- **One script per work unit** (named `bp-{unit-id}.py`, e.g., `bp-a1.py`)
- **Hardcode all content** — no runtime API calls, no file reading, pure dict
- **intro is HTML** — use `<p>`, `<em>`, `<strong>` only; no `<div>`, no headers
- **Two paragraphs max** for a stub (150–300 words total)
- **Category must be one of:** `people` · `places` · `concepts` · `names` · `events`
- **key_refs** — first 3–5 refs from the entry's `refs` array (Easton full entry)
- **Never invent information** — synthesis must be derivable from the source texts

### 5. Run the script

```bash
python3 ../scripts/bp-{unit-id}.py
```

Verify: the output directory gains the expected number of new `.json` files.
Spot-check 3 random entries: confirm `intro` is present, `category` is set, refs are real.

### 6. Update the tracker

In `BP_PROGRESS.md`:
- Set your unit row to `complete`
- Increment the "Complete" count in the Summary table
- Update "Last updated" line with today's date and unit ID

---

## Quality standards for synthesis

**People:**
> "Aaron, the eldest son of Amram and Jochebed and elder brother of Moses, was appointed the first High Priest of Israel. His name likely means <em>mountain of strength</em>..."

- Lead with who they are and their primary role in Scripture
- Name the key relationship (son of, brother of, king of...)
- Mention their most significant act or legacy
- End with their theological significance if notable

**Places:**
> "Bethlehem, a small town in the hill country of Judah approximately six miles south of Jerusalem, holds central importance in both Testaments..."

- Lead with location, region, and size (if known)
- Note both testaments if relevant
- Mention the key events that make it significant

**Concepts:**
> "Atonement, in biblical theology, refers to the removal of sin's guilt and the restoration of the relationship between God and humanity..."

- Lead with a clear definition
- Note both OT and NT dimensions if they differ
- Name the key mechanism (sacrifice, substitution, ransom, etc.)

**Names (Hitchcock-only, no article):**
> "Achan (meaning: <em>one who troubles</em>) appears in the account of Israel's defeat at Ai following the conquest of Jericho..."

- Lead with the name meaning if from Hitchcock
- Give the scriptural context in one sentence
- Note their significance (positive or cautionary)

---

## What NOT to do

- Do not copy-paste raw Easton/Smith HTML as the intro — write a true synthesis
- Do not exceed 300 words in the intro field
- Do not add sections to a stub (leave `sections: []`)
- Do not include commentary or theological application beyond what the sources state
- Do not use first person or devotional language
- Do not create articles for letter ranges not in your claimed unit
