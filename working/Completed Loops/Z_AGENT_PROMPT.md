/clear
# Z Commentary Agent Prompt

This prompt is designed to run in a loop — each session claims one work unit, completes it, updates the tracker, and exits. Each run is self-contained; no state is passed between sessions.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `Z_COMMENTARY_AGENT_GUIDE.md`
2. `Z_COMMENTARY_SCRIPT_GUIDE.md`
3. `Z_PROGRESS.md`

You are working on the Z Commentary Suite — three original verse-by-verse commentary layers (`mkt-original`, `mkt-context`, `mkt-christ`) plus an echo/fulfillment data layer (`echo`), covering all 66 books. All work is written as static Python scripts containing hardcoded HTML commentary dictionaries and echo entry dictionaries; no API calls are made during the writing step.

---

## Step 1 — Find and claim a real work unit

The tracker in `Z_PROGRESS.md` may be stale. **Always verify actual file state before claiming any row.**

### 1a. Find the first candidate

Scan the **NT Work Queue** table first, then the **OT Work Queue** if NT is exhausted. For each row, evaluate its Status field using the rules below:

| Status value | Action |
|---|---|
| `not started` or `partial` | Candidate — proceed to 1b |
| `in-progress @ <timestamp>` where timestamp is **< 20 minutes** old | **Skip** — another agent is actively working this unit; move to the next row |
| `in-progress @ <timestamp>` where timestamp is **≥ 20 minutes** old | Candidate — treat as abandoned; claim it as your own in Step 1c |
| `in-progress` (no timestamp) | Candidate — legacy format; treat as abandoned and claim it |
| `complete` | Skip |

Use this Python snippet to evaluate an `in-progress @ …` timestamp:

```python
from datetime import datetime, timezone, timedelta

raw = 'in-progress @ 2026-06-05T14:30:00Z'   # ← paste the cell value
ts_str = raw.split('@ ')[1].strip()
ts = datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
age = datetime.now(timezone.utc) - ts
print('age:', age, '— stale' if age > timedelta(minutes=20) else '— active, SKIP')
```

### 1b. Verify actual completeness with Python

For the candidate row, determine the output file from its type:

| Type | Output path |
|------|-------------|
| `echo` | `data/echoes/{book}.json` |
| `original` | `data/commentary/mkt-original/{book}.json` |
| `context` | `data/commentary/mkt-context/{book}.json` |
| `christ` | `data/commentary/mkt-christ/{book}.json` |

Run this Python check (adjust book, start, end, and path to match your candidate):

```python
import json

book = 'matthew'   # ← your book
start, end = 5, 6  # ← your chapter range
type_ = 'context'  # ← echo / original / context / christ

# Load output file
path = f'data/commentary/mkt-{type_}/{book}.json'  # adjust for echo
out = json.load(open(path)) if __import__('pathlib').Path(path).exists() else {}

# Load interlinear for authoritative verse inventory
il = json.load(open(f'data/interlinear/{book}.json'))

for ch in range(start, end + 1):
    ck = str(ch)
    il_vv  = set(il.get(ck, {}).keys())
    out_vv = set(out.get(ck, {}).keys())

    if type_ == 'echo':
        # Echo is selective — chapter presence with any entries = done
        status = 'done' if out_vv else 'missing'
    else:
        missing = il_vv - out_vv
        status = f'MISSING {sorted(missing, key=int)}' if missing else f'OK ({len(out_vv)} verses)'
    print(f'ch {ch}: {status}')
```

**Decision rules:**

- **All chapters fully covered** (no missing verses for commentary; chapter present for echo) → this row is actually complete. Update its Status to `complete` in `Z_PROGRESS.md` and move to the **next** candidate.
- **Any chapter missing or has gaps** → this is your real work unit. Proceed to Step 1c.
- **All rows in both queues are complete** → stop and report: *"All work queue entries are complete."*

### 1c. Claim it

Get the current UTC timestamp in ISO 8601 format:

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
```

Set the row's Status to `in-progress @ <timestamp>` (e.g., `in-progress @ 2026-06-05T14:30:00Z`) and save `Z_PROGRESS.md`. Re-read the file to confirm the save.

---

## Step 2 — Study the source material

Before writing a single verse, read these files for your claimed book:

- `data/interlinear/{book}.json` — use this as your **definitive verse inventory**. Every verse key present in the interlinear must appear in your commentary output. Do not invent or skip verse numbers.
- `data/translation/glossary-{greek|hebrew}.json` — semantic ranges; `dispute_level >= 2` terms deserve explicit treatment
- `data/translation/draft/mediating/{book}.json` — the MKT text; quote it when illustrating translation choices
- Any previously completed scripts for the **same book and type** in `scripts/` — carry forward terminology, how key terms are rendered, and Christological classification decisions

For `echo` type only:
- `data/parallels/{book}.json` — absorb existing parallels before writing new entries (see `Z_COMMENTARY_SCRIPT_GUIDE.md` for the absorption map)

For `mkt-original` type only:
- `data/translation/notes/{book}.json` — contains per-verse `reasoning` where `translate-with-claude.py` has run; use it to understand why the MKT made specific choices

---

## Step 3 — Chapter range and gap targeting

Your script covers **only the chapter range in your claimed work unit**. Do not expand beyond it.

Before writing, note which verses already exist in the output file (from Step 1b). Your commentary dictionary only needs entries for **missing verses** — `merge_comm` / `merge_echo` will skip any verse keys that are already present. You may include already-present verses in your dictionary without harm, but targeting only gaps is efficient.

If you run into context pressure mid-range, finish the current chapter cleanly, stop, and update your work queue row to show the chapters actually completed.

---

## Step 4 — Write the script

Follow `Z_COMMENTARY_SCRIPT_GUIDE.md` exactly. Required structure:

1. **Header docstring** — type, book, chapter range, run command, any non-obvious interpretation decisions
2. **Boilerplate** — `load_comm` / `save_comm` / `merge_comm` (or echo equivalents) copied verbatim from the guide
3. **Data dictionary** — `BOOKNAME = { "ch": { "v": "<html>" } }` (commentary) or `BOOKNAME_ECHOES = { "ch": { "v": [{type, target, note}] } }` (echo). **Every verse key from the interlinear must have an entry.**
4. **`main()`** — loads existing file, calls `merge_comm` / `merge_echo`, saves

Content principles from `Z_COMMENTARY_AGENT_GUIDE.md` Section 4 are non-negotiable. Type-specific guidance in Section 5 governs what to cover.

---

## Step 5 — Run and verify completeness

```bash
python3 scripts/{script_name}.py
```

Verify it exits cleanly and prints the expected `wrote …` line. Then run a **verse-completeness check** against the interlinear:

```python
import json

book = 'matthew'; start, end = 5, 6; type_ = 'context'

path = f'data/commentary/mkt-{type_}/{book}.json'
out = json.load(open(path))
il  = json.load(open(f'data/interlinear/{book}.json'))

all_ok = True
for ch in range(start, end + 1):
    ck = str(ch)
    missing = set(il.get(ck, {}).keys()) - set(out.get(ck, {}).keys())
    if missing:
        print(f'ch {ch} STILL MISSING: {sorted(missing, key=int)}')
        all_ok = False
    else:
        print(f'ch {ch}: complete ({len(out.get(ck,{}))} verses)')

if all_ok:
    print('All verses present ✓')
```

**If any verses are still missing:** fix the script (add the missing entries), re-run it, and re-verify before continuing. Do not mark the row complete with gaps.

Spot-check three verses spread across the range for content quality — confirm output is substantive HTML that adds information beyond the MKT text, not paraphrase or padding.

---

## Step 6 — Update the tracker

Edit `Z_PROGRESS.md` in a **single save** (do not write twice):

1. **Work Queue table** — set your row's Status to `complete` (this simultaneously removes the `in-progress @ <timestamp>` lease — do not leave both)
2. **NT/OT book table** — update the type column for your book:
   - `complete` if all chapters for that type are now fully covered
   - `partial` if only some chapters are covered
3. **Summary table** — increment the relevant complete count if the book is now fully done for that type
4. **`Last updated:`** line — set to today's date

Re-read the file after saving to confirm the Status cell no longer contains any `in-progress` or timestamp text.

---

## Key facts

- Chapter and verse keys in all JSON files are **strings** — `"1"` not `1`
- Commentary output paths: `data/commentary/mkt-original/{book}.json`, `data/commentary/mkt-context/{book}.json`, `data/commentary/mkt-christ/{book}.json`
- Echo output path: `data/echoes/{book}.json`
- `merge_comm` and `merge_echo` **never overwrite** existing entries — safe to re-run against any partially complete file
- Echo `target` must be a short parseable ref: `"Isa 53:7"` not `"Isaiah 53:7"`
- Parallels files (`data/parallels/{book}.json`) are prototype data to absorb into echoes — do not add new entries to parallels
- `mkt-christ` requires an entry for **every verse** including genealogies, lists, and transitional verses; brief entries are preferable to gaps
- Content quality over speed: one substantive `<p>` is better than three padding blocks
- The interlinear is the authoritative verse inventory — if a verse key exists in the interlinear, it must exist in your commentary output


After completing this iteration, run /compact before calling ScheduleWakeup.