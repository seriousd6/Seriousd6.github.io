/clear
# Paragraph Structure Agent Prompt

This prompt runs in a loop — each session claims one work unit (one book or chapter range), generates `data/paragraphs/{bookId}.json`, and updates the tracker. Each run is fully self-contained.

---

Read the following files **in full** before doing anything else — in this order, no skipping:

1. `PARA_QUEUE.md`

---

## Step 1 — Find and claim a work unit

Scan `PARA_QUEUE.md` for the first row with Status `not started`. Large books (Psalms, Isaiah, Jeremiah, Ezekiel, Genesis) are split into chapter-range rows; shorter books are one row per book.

| Status | Action |
|--------|--------|
| `not started` | Candidate — proceed to step 1b |
| `in-progress @ <timestamp>` where timestamp **< 2 hours** old | Skip — another agent is working this unit |
| `in-progress @ <timestamp>` where timestamp **≥ 2 hours** old | Candidate — treat as abandoned |
| `complete` | Skip |

Check timestamp age:
```python
from datetime import datetime, timezone, timedelta
raw = 'in-progress @ 2026-06-11T14:30:00Z'  # ← paste cell value
ts = datetime.fromisoformat(raw.split('@ ')[1].strip().replace('Z', '+00:00'))
age = datetime.now(timezone.utc) - ts
print('age:', age, '— stale' if age > timedelta(hours=2) else '— active, SKIP')
```

### 1b. Verify output file does not already cover this range

```python
import json, pathlib
ROOT = pathlib.Path('.')
book = 'john'    # ← your candidate bookId
start, end = 1, 21  # ← chapter range from the queue row

para_path = ROOT / 'data' / 'paragraphs' / f'{book}.json'
existing = json.loads(para_path.read_text()) if para_path.exists() else {}

missing_chs = [ch for ch in range(start, end + 1) if str(ch) not in existing]
if missing_chs:
    print(f'Missing chapters: {missing_chs}')
else:
    print('Already complete — mark complete in queue and move to next row')
```

### 1c. Claim it

```python
from datetime import datetime, timezone
print(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
```

Set the row's Status to `in-progress @ <timestamp>` and save `PARA_QUEUE.md`. Re-read to confirm.

---

## Step 2 — Read the interlinear data for your chapter range

The interlinear data gives you the exact verses and their text — use it to verify your paragraph divisions against actual verse content.

```python
import json, pathlib
ROOT = pathlib.Path('.')
book = 'john'      # ← your book
chapters = [1, 2]  # ← first two chapters of your range (or all if short book)

il = json.loads((ROOT / 'data' / 'interlinear' / f'{book}.json').read_text())

for ch in chapters:
    ck = str(ch)
    vs = il.get(ck, {})
    print(f'\n=== Chapter {ch} ({len(vs)} verses) ===')
    for v, tokens in sorted(vs.items(), key=lambda x: int(x[0])):
        text = ' '.join(t.get('text', '') for t in tokens if t.get('text'))
        print(f'  v{v}: {text[:120]}')
```

Run this for each chapter in your range to see the verse flow. Use it to verify your paragraph break placements are at the right verse boundaries.

---

## Step 3 — Generate the paragraph structure JSON

### Schema

```json
{
  "1": {
    "breaks": [
      { "v": 1, "type": "narrative" },
      { "v": 14, "type": "narrative" },
      { "v": 19, "type": "narrative" }
    ],
    "headings": [
      { "before": 1, "text": "The Word Became Flesh" },
      { "before": 14, "text": "The Word Among Us" },
      { "before": 19, "text": "The Testimony of John" }
    ]
  },
  "2": {
    "breaks": [
      { "v": 1, "type": "narrative" },
      { "v": 13, "type": "narrative" }
    ],
    "headings": [
      { "before": 1, "text": "The Wedding at Cana" },
      { "before": 13, "text": "Clearing the Temple" }
    ]
  }
}
```

**Paragraph types:**

| Type | Use for |
|------|---------|
| `narrative` | Prose narrative, historical accounts, letters |
| `poetry` | Psalms, poetry sections in the prophets, Song of Solomon, laments |
| `dialogue` | Speeches, conversations, direct address sections |
| `list` | Genealogies, lists of names, numbered items, beatitudes |
| `doxology` | Doxologies, benedictions, praise refrains |

**Rules for `breaks`:**
- Every chapter must start with a break at `v: 1`
- Each `breaks` entry marks where a new paragraph begins at that verse
- Verse 1 of every chapter always gets a break (required)
- Aim for 3–8 paragraphs per chapter; very short chapters (< 8 verses) may have 1–3
- Poetry type: use for every stanza group in the Psalms, Proverbs, prophetic poetry — break at natural stanza boundaries
- Dialogue type: sustained speeches (e.g. Job's friends, Sermon on the Mount discourse sections)

**Rules for `headings`:**
- Headings are editorial titles placed before a paragraph — use standard section headings from modern Bible editions (ESV, NIV, NASB)
- Every `headings` entry has a matching break at the same verse number
- Not every paragraph needs a heading — only use headings at major section transitions
- Do not number headings in the text field
- Be concise: 3–6 words, title case

### Use your Bible knowledge

You know the literary structure of every book. For each chapter in your range:
- Where does a new scene or topic begin?
- Where does the author shift from narrative to dialogue? From poetry to prose?
- What are the traditional section headings (as used in ESV/NIV/NASB)?

You do not need to look anything up — generate from your knowledge of Bible text, then verify against the interlinear verse text you read in Step 2.

### Special genre rules

**Psalms:** Every Psalm is its own unit. Break by stanza. Mark all verse content as `poetry` type. Headings should describe the psalm's theme, not its superscription (e.g. "A Lament for Enemies" not "A Psalm of David").

**Proverbs:** Chapters 1–9 and 31 have discernible paragraph structure (parental address units). Chapters 10–29 are individual proverbs — group loosely by theme if a theme cluster is clear; otherwise 3–5 verse groupings are fine. Type: `list` for proverb clusters, `narrative` for the woman of virtue (31:10–31).

**Prophecy:** Alternate between `narrative` (historical prose sections), `poetry` (oracles), and `dialogue` (divine speech introductions like "Thus says the LORD"). Mark extended oracle blocks as `poetry`.

**Genealogies:** Type `list`.

**Letters (Pauline):** Most content is `narrative` (prose argument). Mark doxologies as `doxology`. Mark lists of greetings/instructions as `list`.

---

## Step 4 — Write the output file

Load any existing data for the book (other chapter ranges may already be complete), merge your new chapters in, and write the result:

```python
import json, pathlib
ROOT = pathlib.Path('.')
book = 'john'   # ← your book

para_path = ROOT / 'data' / 'paragraphs' / f'{book}.json'
para_path.parent.mkdir(exist_ok=True)

# Load existing data (may have chapters from other sessions)
existing = json.loads(para_path.read_text()) if para_path.exists() else {}

# Your generated data — fill in all chapters in your range
new_data = {
    "1": {
        "breaks": [
            {"v": 1, "type": "narrative"},
            {"v": 14, "type": "narrative"},
            {"v": 19, "type": "narrative"},
            {"v": 29, "type": "narrative"},
            {"v": 35, "type": "narrative"},
            {"v": 43, "type": "narrative"}
        ],
        "headings": [
            {"before": 1, "text": "The Word Became Flesh"},
            {"before": 14, "text": "The Word Among Us"},
            {"before": 19, "text": "John's Testimony"},
            {"before": 29, "text": "The Lamb of God"},
            {"before": 35, "text": "The First Disciples"},
            {"before": 43, "text": "Philip and Nathanael"}
        ]
    }
    # ... all chapters in your range
}

# Merge (do NOT overwrite chapters already in existing)
merged = {**existing}
for ch_key, ch_data in new_data.items():
    merged[ch_key] = ch_data  # overwrite with new data for this session's range

# Write merged result
para_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False))
print(f'Written {len(merged)} chapters to {para_path}')
```

---

## Step 5 — Verify the output

```python
import json, pathlib
ROOT = pathlib.Path('.')
book = 'john'
start, end = 1, 21

para_path = ROOT / 'data' / 'paragraphs' / f'{book}.json'
data = json.loads(para_path.read_text())

# Check all chapters in range are present
missing = [ch for ch in range(start, end + 1) if str(ch) not in data]
if missing:
    print(f'ERROR: missing chapters {missing}')
else:
    print(f'All {end - start + 1} chapters present')

# Check each chapter has a break at v:1 and at least one break
for ch in range(start, end + 1):
    breaks = data[str(ch)]['breaks']
    if not breaks or breaks[0]['v'] != 1:
        print(f'WARNING: ch {ch} does not start with v:1 break — has: {breaks[0] if breaks else "none"}')
    valid_types = {'narrative', 'poetry', 'dialogue', 'list', 'doxology'}
    bad = [b for b in breaks if b['type'] not in valid_types]
    if bad:
        print(f'WARNING: ch {ch} has invalid types: {bad}')
    headings = data[str(ch)].get('headings', [])
    break_vs = {b['v'] for b in breaks}
    for h in headings:
        if h['before'] not in break_vs:
            print(f'WARNING: ch {ch} heading at v{h["before"]} has no matching break')

print('Verification complete')
```

---

## Step 6 — Update the queue

Set the row's Status to `complete` in `PARA_QUEUE.md`. Re-read to confirm. Stop.
