/clear
# Wide Source Commentary Agent Prompt

This prompt runs in a loop — each session claims one work unit, synthesizes one chapter range from the public-domain commentators, runs the script, and updates the tracker. Each run is fully self-contained.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `WS_AGENT_GUIDE.md`
2. `WS_SCRIPT_GUIDE.md`
3. `WS_PROGRESS.md`

---

## Step 1 — Find and claim a work unit

### 1a. Find the first unclaimed row

Scan the **NT Work Queue** table in `WS_PROGRESS.md` first, then the OT Work Queue if NT is exhausted. Follow the priority order at the top of that file (Hebrews → Romans → Galatians → Ephesians → 1 John first).

| Status | Action |
|--------|--------|
| `not started` | Candidate — proceed to 1b |
| `in-progress @ <timestamp>` where timestamp **< 2 hours** old | Skip — another agent is working this unit |
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

### 1b. Verify the output file does not already cover this range

```python
import json, pathlib
ROOT = pathlib.Path('.')
book = 'hebrews'   # ← your candidate
start, end = 1, 4  # ← your chapter range

il  = json.loads((ROOT / 'data' / 'interlinear' / f'{book}.json').read_text())
syn_path = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
syn = json.loads(syn_path.read_text()) if syn_path.exists() else {}

for ch in range(start, end + 1):
    ck = str(ch)
    il_vv  = set(il.get(ck, {}).keys())
    syn_vv = set(syn.get(ck, {}).keys())
    missing = il_vv - syn_vv
    status = f'MISSING {sorted(missing, key=int)}' if missing else f'complete ({len(syn_vv)} verses)'
    print(f'ch {ch}: {status}')
```

If all chapters are fully covered, update the row to `complete` in the tracker and move to the next candidate.

### 1c. Claim it

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
```

Set the row's Status to `in-progress @ <timestamp>` and save `WS_PROGRESS.md`. Re-read the file to confirm the save took effect.

---

## Step 2 — Read the source material for your chapter range

Read the commentaries for your claimed book and chapters. Use this script to see what each source has for each chapter:

```python
import json, pathlib
ROOT = pathlib.Path('.')
book = 'hebrews'      # ← your book
chapters = [1, 2]     # ← your range

sources = ['mhcc', 'calvin', 'ellicott', 'jfb', 'clarke', 'wesley', 'barnes']
for src in sources:
    p = ROOT / 'data' / 'commentary' / src / f'{book}.json'
    if not p.exists():
        print(f'{src}: not found'); continue
    data = json.loads(p.read_text())
    for ch in chapters:
        ck = str(ch)
        ch_data = data.get(ck, {})
        if not ch_data:
            print(f'{src} ch {ch}: (no data)'); continue
        keys = sorted(ch_data.keys(), key=int)
        print(f'\n=== {src} ch {ch} keys: {keys} ===')
        # Show first entry for context
        first_v = keys[0] if keys else None
        if first_v:
            print(ch_data[first_v][:300])
```

Note which sources use **section entries** (one key covering multiple verses) vs. per-verse entries. This matters for how you select excerpts for the `voices` array.

Also consult:
- `data/interlinear/{book}.json` — authoritative verse inventory; every verse key present here must appear in your output
- Any previously written synthesis in `data/commentary/synthesis/{book}.json` — check existing chapter/verse keys so `merge_synthesis` can skip them

---

## Step 3 — Write the script

Follow `WS_SCRIPT_GUIDE.md` exactly. Required structure:

1. **Header docstring** — book, chapter range, sources used, any key_tension decisions (where voices divide)
2. **Boilerplate** — `load_synthesis`, `save_synthesis`, `merge_synthesis` copied verbatim from the guide
3. **Data dictionary** — `BOOKNAME = { "ch": { "v": { synthesis, voices, consensus, key_tension } } }` — **every verse from the interlinear must have an entry**
4. **`main()`** — loads existing synthesis, calls `merge_synthesis`, saves

Apply the content principles from `WS_AGENT_GUIDE.md` to every entry:
- Synthesis is your prose, integrating the voices — not a list of what each commentator said
- Use commentator names inline ("Calvin stresses…", "Henry notes…")
- voices excerpts are 40–80 words, directly from the source HTML
- Be honest: use `consensus: "divided"` when voices genuinely disagree; set `key_tension`

Work units are already sized at ≤45 verses (typically 1–2 chapters). If context runs short mid-chapter, finish that chapter cleanly, stop, and update the work queue row to show the chapter actually completed; leave the remainder as a new `not started` row.

---

## Step 4 — Run and verify

```bash
python3 scripts/ws-synthesis-{bookId}-{start}-{end}.py
```

Confirm it exits cleanly and prints the expected `wrote …` line. Then run the verification check from `WS_SCRIPT_GUIDE.md` Section 6 (adjust `book`, `start`, `end`).

**If any verses are missing:** add the missing entries to the script, re-run, and re-verify before continuing. Do not mark the row complete with gaps.

Spot-check three entries spread across the range:
- Is the `synthesis` paragraph 100–250 words of actual prose (not a list or a paraphrase chain)?
- Does it name commentators inline, not just quote them?
- Does the `voices` array have 2–5 entries, each 40–80 words?
- Is `consensus` set correctly — not reflexively `"affirm"` when the sources actually differ?

---

## Step 5 — Update the tracker

Edit `WS_PROGRESS.md` in a **single save** (do not write twice):

1. **Work Queue table** — set your row's Status to `complete`
2. **NT/OT book table** — update the Synthesis column for your book:
   - `complete X/N` where X = chapters done, N = total (e.g., `complete 4/13` for Hebrews after first unit)
   - `complete` when all chapters for that book are done
3. **Summary table** — increment the relevant complete count if the book is now fully done
4. **`Last updated:`** line — set to today's date

Re-read `WS_PROGRESS.md` after saving to confirm the `in-progress` text is gone.

---

## Key facts

- Chapter and verse keys are **strings** — `"1"` not `1`
- Output path: `data/commentary/synthesis/{book}.json`
- `merge_synthesis` **never overwrites** existing entries — safe to re-run at any time
- The interlinear is the **authoritative verse inventory** — if a verse key exists in the interlinear, it must exist in the synthesis output
- `key_tension` must be `None` in Python (serializes to `null` in JSON) when `consensus = "affirm"`
- `barnes` and `rwp` are NT only — do not reference them for OT books
- Run all scripts from the **repo root**: `python3 scripts/ws-synthesis-{bookId}-{start}-{end}.py`
- For small epistles (Philemon, 2–3 John, Jude, Obadiah), the whole book fits in one script

After completing this iteration, run /compact before calling ScheduleWakeup.
