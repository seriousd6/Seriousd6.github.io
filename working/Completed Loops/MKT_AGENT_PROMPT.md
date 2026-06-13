# MKT Translation Agent Prompt

Copy and paste this entire prompt to a new agent session to claim and complete one work unit.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `TRANSLATION_AGENT_GUIDE.md`
2. `MKT_STATIC_SCRIPT_GUIDE.md`
3. `MKT_PROGRESS.md`

You are working on the Modern Kingdom Translation (MKT) project — a three-tier English Bible translation (Literal / Mediating / Thought) produced directly from Hebrew and Greek source texts. All work is written as static Python scripts containing hardcoded translation dictionaries; no API calls are made during the translation step.

---

## Step 1 — Claim a work unit

Open `MKT_PROGRESS.md` and read the **Work Queue** table at the bottom.

Find the first row whose Status is `not started`. Immediately edit that row's Status to `in-progress` and save the file — this is your lock. Do this **before** any other work.

After saving, re-read the file to confirm your claim is still there. If another agent overwrote your claim (the row now shows a different status you didn't write), move on to the next `not started` row and repeat.

If every row is `in-progress` or `complete`, stop and report: **"No available work units — all queue entries are claimed or complete."**

Your claimed row gives you: the book, chapter range, script filename, and verse count.

---

## Step 2 — Study the source material

Before writing a single verse, read:

- `data/interlinear/{book}.json` — source tokens for your claimed chapters
- The most recently completed script(s) for the same book (check `MKT_PROGRESS.md` Script reference table) — carries forward tone, contested-term decisions, and capitalisation conventions
- `data/translation/draft/literal/{book}.json` — confirm which chapters already have content so you do not overwrite them

---

## Step 3 — Word count constraint

Your script covers **only the chapter range in your claimed work queue row**. Do not expand beyond it. Units are pre-sized to ≤ 6 chapters / ≤ 250 verses.

If you run long mid-book, finish the current chapter cleanly and stop. Update the work queue row to show the chapters actually completed before marking it `complete`.

---

## Step 4 — Write the script

Follow `MKT_STATIC_SCRIPT_GUIDE.md` exactly. The required structure is:

1. **Header docstring** — book name, chapter range, run command, every contested-term decision documented
2. **Boilerplate** — `load` / `save` / `merge_tier` helpers (copy verbatim from the guide)
3. **Translation dictionary** — `BOOKNAME = { "ch": { "v": { "L": "...", "M": "...", "T": "..." } } }`
4. **`main()`** — iterates the three tiers, calls `merge_tier`, then `save`

Translation principles from `TRANSLATION_AGENT_GUIDE.md` Section 5 are non-negotiable. For every term in Section 6 (contested terms), make an explicit rendering choice in all three tiers and document it in the header.

---

## Step 5 — Run the script

```bash
python3 scripts/{script_name}.py
```

Verify it exits cleanly and prints the expected `wrote ...` lines. Spot-check three verses spread across the range by reading `data/translation/draft/literal/{book}.json` directly. Confirm real translation prose, not word salad.

---

## Step 6 — Update the tracker

Edit `MKT_PROGRESS.md`:

1. **Work Queue table** — update your row's Status to `complete`
2. **Book row** in the OT/NT table — update Chs Done, Verses Done, and Status string (e.g. `Partial — chs 1–21`)
3. **Summary table** — recalculate Partial (or Complete) chapters and verses
4. **`**Last updated:**`** — set to today's date
5. **Script reference table** — add your script name and chapter coverage

---

## Key facts

- Chapter and verse keys in all JSON files are **strings** (`"1"`, not `1`)
- All glossary entries are still `draft` — the primary gloss is a proposal, not a confirmed decision; you may deviate when context requires, but document it
- The three tiers are distinct: L = source syntax preserved, M = natural English with accurate glosses, T = meaning-driven with interpretive surface
- T should add genuine value over M — if they read the same, rewrite T
- `merge_tier` never overwrites existing content — safe to run against a partially-complete file
