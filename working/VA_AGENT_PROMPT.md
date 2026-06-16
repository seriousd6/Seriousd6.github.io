/clear
# Verse Auditor Agent Prompt

This prompt runs in a loop — each session claims **three files** from VA_PROGRESS.md, wraps bare
scripture references with `<a class="ref" data-ref="...">` tags, and updates the tracker.
Each iteration is fully self-contained. Working directory: repo root.

---

Read these files **in full** before doing anything else, in this order:

1. `VA_GUIDE.md`
2. `VA_PROGRESS.md`

---

## Step 0 — Discovery gate

Read the `Next discovery due:` line in `VA_PROGRESS.md`.

```python
from datetime import datetime, timezone

line = 'Next discovery due: 2026-06-08T12:00:00Z'   # ← paste the actual line
ts_str = line.split(':', 1)[1].strip()

if '(not yet run)' in ts_str:
    overdue = True
else:
    ts = datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
    overdue = datetime.now(timezone.utc) >= ts

print('Discovery overdue:', overdue)
```

If overdue (or line says `(not yet run)`):
  Run: `python3 scripts/va_discover.py`
  Re-read `VA_PROGRESS.md` in full before continuing.

If not overdue: skip to Step 1.

---

## Step 1 — Claim and process 3 work units

Repeat Steps 1–5 **three times** before moving to Step 6. Each repetition claims one row,
processes it, and marks it complete (or skipped) before claiming the next.

Scan `VA_PROGRESS.md` section tables in priority order: **T → M → E → L → D → K → P → O**.

| Row status | Action |
|---|---|
| `not_started` | Candidate — proceed to 1b |
| `in-progress @ TIMESTAMP` where age < 1h | Skip (another session is active) |
| `in-progress @ TIMESTAMP` where age ≥ 1h | Candidate — treat as abandoned |
| `complete` or `skipped` or `removed` | Skip |

### 1a. Check timestamp age for in-progress rows

```python
from datetime import datetime, timezone, timedelta

raw = 'in-progress @ 2026-06-07T14:30:00Z'   # ← paste the cell value
ts = datetime.fromisoformat(raw.split('@ ')[1].strip().replace('Z', '+00:00'))
age = datetime.now(timezone.utc) - ts
print('age:', age, '— stale' if age > timedelta(hours=1) else '— active, SKIP')
```

### 1b. mtime check (skip if file unchanged since last run)

Read the `Last Run` cell from the row. If it is `—`, skip this check and go to 1c.

Otherwise, check the file's modification time against `Last Run`:

```python
import os
from datetime import datetime, timezone

file_path = 'data/commentary/mkt-context/1chronicles'  # ← from row
last_run  = '2026-06-15T01:59:52Z'                     # ← from row's Last Run cell

if os.path.isdir(file_path):
    mtimes = [os.path.getmtime(os.path.join(file_path, f))
              for f in os.listdir(file_path)
              if os.path.isfile(os.path.join(file_path, f))]
    mtime = max(mtimes) if mtimes else 0
else:
    mtime = os.path.getmtime(file_path)

file_modified = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

if last_run >= file_modified:
    print(f'SKIP: unchanged (file_modified={file_modified}, last_run={last_run})')
else:
    print(f'PROCESS: changed (file_modified={file_modified}, last_run={last_run})')
```

**If SKIP:** Write to the row in one save: `Status → skipped`, `File Modified → file_modified`, `Notes → unchanged since {last_run}`. Do **not** claim as `in-progress`. Count as one work unit and move to the next candidate.

**If PROCESS (or Last Run was `—`):** Continue to 1c.

### 1c. Claim it

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
```

Write `in-progress @ <TIMESTAMP>` to the row's Status cell and save `VA_PROGRESS.md`.
Re-read the file to confirm the claim saved correctly.

---

## Step 2 — Identify context

Parse the file path from the row you claimed. Determine:

- **Section code** (T/M/E/L/D/K/P/O) from the `## Section X —` heading above the row
- **file_type** — from the section definition in `VA_GUIDE.md` Context Resolution table
- **book_ctx** — see table below

| Section | Book context | How to get it |
|---|---|---|
| T, M | Canonical book name | Filename stem, normalized: `romans` → `Romans`, `1corinthians` → `1 Corinthians` (see STEM_TO_CANONICAL in `va_process.py`) |
| E | Canonical book name | Filename stem |
| L, D, K, O | None | Do not pass `--book` |
| P | From file or None | Read `<body data-bible-book="...">` attribute in the HTML file; if absent, do not pass `--book` |

---

## Step 3 — Dry run

Run `va_process.py` with `--dry-run --show-sample 5` to preview changes:

```bash
# json_commentary (Sections T, M):
python3 scripts/va_process.py data/commentary/ellicott/romans.json --dry-run --show-sample 5

# json_echoes (Section E):
python3 scripts/va_process.py data/echoes/mark.json --dry-run --show-sample 5

# html with book context (Section P, when data-bible-book present):
python3 scripts/va_process.py topics/john/index.html --book John --dry-run --show-sample 5

# html without book context (Sections L, O, or P without data-bible-book):
python3 scripts/va_process.py data/library/html/calvin-institutes-vol2.html --dry-run --show-sample 5
```

Capture: `Refs found`, `Refs fixed`, and the sample pairs.

---

## Step 4 — Verify

Inspect the `--show-sample` output. Confirm all of the following:

- [ ] `data-ref` values use **full canonical** book names (`1 Corinthians`, not `1Cor`)
- [ ] No double-wrapping: no `<a data-ref` inside another `<a data-ref`
- [ ] No Greek/Hebrew lemma text wrapped (e.g., `δοῦλος`, `H1697`)
- [ ] Parenthetical ref lists: each ref gets its own link, semicolons remain as text
- [ ] `Refs fixed` count is plausible

If sample looks wrong (false positives, malformed data-ref, double-wrapping):
  - Update the row: Status → `skipped`, Notes → brief description of the problem
  - Save `VA_PROGRESS.md` and skip to Step 6

---

## Step 5 — Write

If verification passes, run without `--dry-run` to write the file:

```bash
python3 scripts/va_process.py data/commentary/ellicott/romans.json
```

Confirm the script exits cleanly and prints `Refs fixed: N`.

Run idempotency check — `--dry-run` on the now-processed file should show `Refs fixed: 0`:

```bash
python3 scripts/va_process.py data/commentary/ellicott/romans.json --dry-run
```

Get the file's modification time to store in `File Modified`:

```python
import os
from datetime import datetime, timezone

file_path = 'data/commentary/ellicott/romans.json'  # ← from row

if os.path.isdir(file_path):
    mtimes = [os.path.getmtime(os.path.join(file_path, f))
              for f in os.listdir(file_path)
              if os.path.isfile(os.path.join(file_path, f))]
    mtime = max(mtimes) if mtimes else 0
else:
    mtime = os.path.getmtime(file_path)

file_modified = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
print(f'File Modified: {file_modified}')
```

Update the row in `VA_PROGRESS.md` in a **single save**:

```
Status        → complete
Refs Fixed    → N    (use the refs_fixed number from Step 3 output)
Last Run      → ISO timestamp (now)
File Modified → file_modified from above
Notes         → any edge case observations, or — if clean
```

Re-read `VA_PROGRESS.md` after saving to confirm `in-progress` is gone from the row.

---

## Step 6 — Loop completion check

Run after all 3 files are processed (or after any skips that reduce the batch).
Count active rows (status = `not_started` or `in-progress`):

```python
import re
text = open('VA_PROGRESS.md').read()

not_started = len(re.findall(r'\| not_started \|', text))
in_prog     = len(re.findall(r'\| in-progress @', text))
print(f'Remaining: {not_started} not_started, {in_prog} in-progress')
```

**If any `not_started` rows remain:** stop — this iteration is complete. Proceed to Step 7.

**If ALL rows are `complete`, `skipped`, or `removed`:**
  1. Print: `All files audited at <TIMESTAMP>. Loop complete — stopping.`
  2. Do NOT call ScheduleWakeup. The loop ends here.
  3. The user will restart the loop manually when they want another full pass.

**Manual restart command** (run in repo root to reset statuses while preserving Last Run / File Modified):

```python
with open('working/VA_PROGRESS.md') as f:
    lines = f.readlines()

out = []
for line in lines:
    if line.startswith('|') and ('| complete |' in line or '| skipped |' in line):
        parts = line.split('|')
        if len(parts) == 8 and parts[2].strip() in ('complete', 'skipped'):
            parts[2] = ' not_started '
        out.append('|'.join(parts))
    else:
        out.append(line)

with open('working/VA_PROGRESS.md', 'w') as f:
    f.writelines(out)
print('Reset complete.')
```

---

## Step 7 — Schedule next wake

Only reached if `not_started` rows remain (Step 6 first branch).

After completing this iteration (all 3 files), run `/compact` before calling ScheduleWakeup.

Call ScheduleWakeup with:
  - `delaySeconds`: 60
  - `reason`: `VA loop — processing next file in queue`
  - `prompt`: same /loop prompt used to start this session

---

## Key facts

- Run all commands from the **repo root** (where `VA_PROGRESS.md` lives)
- File type is auto-detected from path; `--file-type` overrides if needed
- `va_process.py` is idempotent — safe to re-run on any file
- `va_discover.py` only runs once per 24h; never removes row data, only adds/marks-removed
- Traditional commentaries (Section T) have the most bare refs — ~2,000–5,000 per source
- Library HTML and library docs (L, D) are largely pre-tagged; expect low `Refs fixed` counts
- Commentary filename stem `songofsolomon` → canonical `Song of Solomon`
