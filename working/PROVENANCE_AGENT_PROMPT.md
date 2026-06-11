/clear
# Provenance Annotation Agent Prompt

This prompt runs in a loop — each session claims one directory, writes and runs the
annotation script, and updates the tracker. Each run is fully self-contained.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `PROVENANCE_AGENT_GUIDE.md`
2. `PROVENANCE_PROGRESS.md`

---

## Step 1 — Claim a work unit

Scan the Work Queue table in `PROVENANCE_PROGRESS.md`. Find the first row whose **Status**
is `not started`. Immediately change its Status to `in-progress @ <timestamp>` and save
the file — this is your lock. Do this **before** any other work.

Get the timestamp:
```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
```

Re-read `PROVENANCE_PROGRESS.md` after saving to confirm your claim is still there.
If every row is `in-progress` or `complete`, stop and report:
**"No available work units — all queue entries are claimed or complete."**

Your claimed row gives you: the directory/file path, data type, approach (per-file or
index-only), and script filename.

---

## Step 2 — Study the target

Before writing the script, confirm:

1. The directory/file exists: `ls data/<your-claimed-path>/` (or `ls data/<path>`)
2. A few sample files to confirm JSON structure:
   ```python
   import json, pathlib, random
   files = list(pathlib.Path('data/<your-path>').glob('*.json'))
   sample = random.choice(files)
   data = json.loads(sample.read_text())
   print(list(data.keys())[:10])
   print('"_source" already present:', '_source' in data)
   ```
3. Check `PROVENANCE_PROGRESS.md` for the exact `_source` value to use for this directory
   (all values are pre-populated in the `_source values by directory` section).

If `_source` is already present in all sample files, mark the row `complete` in the
tracker and stop — the work was already done.

---

## Step 3 — Write the annotation script

Use the script pattern from `PROVENANCE_AGENT_GUIDE.md` Section 4 verbatim.
The script filename is given in your claimed row.

Required structure:
1. **Header docstring** — directory being annotated, run command, `_source` value used
2. **SOURCE dict** — exact value from the `_source values by directory` section of
   `PROVENANCE_PROGRESS.md` for your claimed directory
3. **Main loop** — glob the target files, skip if `"_source"` already present, add it, save
4. Print each processed filename; print "done." at the end

**Special rules:**
- For `index-only` rows: open the single index.json file, add `_source` at top level, save.
  If the index doesn't exist, note this and mark the row `skipped — no index found`.
- For `mhc` (the flat `data/commentary/*.json` files): glob `data/commentary/*.json` but
  **exclude** subdirectory files. Use `pathlib.Path('data/commentary').glob('*.json')`.
- For `data/interlinear/`: if no index.json exists, annotate a new file
  `data/interlinear/_provenance.json` with the `_source` value only.
- Never modify files in subdirectories when the target is the flat parent directory.

---

## Step 4 — Run the script

```bash
python3 scripts/<script-name>.py
```

Verify it exits cleanly and prints filenames + "done."

---

## Step 5 — Spot-check

```python
import json, pathlib

# Check 3 files from the annotated directory
files = sorted(pathlib.Path('data/<your-path>').glob('*.json'))[:3]
for p in files:
    data = json.loads(p.read_text())
    src = data.get('_source')
    print(p.name, '→', src.get('type') if src else 'MISSING')
```

All three must show the correct `type` value (`ai_assisted`, `external`, `derived`, or
`project_curated`). If any show `MISSING`, the script failed — debug and re-run.

---

## Step 6 — Update the tracker

Edit `PROVENANCE_PROGRESS.md` in a **single save**:

1. Set your row's Status to `complete`
2. Update the Summary table: increment Complete count, decrement Not Started
3. Update `**Last updated:**` to today's date

Re-read the file after saving to confirm the `in-progress` text is gone.

---

## Key facts

- Run all scripts from the **repo root** (not from `scripts/` or `working/`)
- `_source` keys in JSON files are **strings**, not integers — no special treatment needed
- Never overwrite an existing `_source` field — always check `if "_source" in data` first
- For files that are arrays rather than objects (e.g. `[{...}, {...}]`): wrap in an object
  `{"_source": ..., "data": [...]}` only if the downstream JS already handles that shape.
  If unsure, check how the file is loaded in `assets/js/`. If the JS expects a bare array,
  skip that file and note it in the tracker.
- The `data/commentary/*.json` flat files are Matthew Henry Concise (mhcc) — not Barnes,
  not JFB. Use the `mhc` source value.
- Small epistles (Philemon, 2–3 John, etc.) appear in some commentary subdirectories with
  very small files — annotate them the same way as any other book file.
