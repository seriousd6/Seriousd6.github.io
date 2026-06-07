# Wide Source Commentary — Script Guide

This document defines the Python script structure every agent must follow when generating Wide Source synthesis data. Read it before writing any `ws-synthesis-*` script.

---

## 1. Directory Map

```
data/
  commentary/
    synthesis/                   ← WRITE TARGET — {book}.json per book
    mhcc/{book}.json             ← READ — Matthew Henry Concise
    calvin/{book}.json           ← READ — Calvin's Commentaries
    ellicott/{book}.json         ← READ — Ellicott's Commentary
    jfb/{book}.json              ← READ — Jamieson-Fausset-Brown
    clarke/{book}.json           ← READ — Adam Clarke
    wesley/{book}.json           ← READ — John Wesley
    barnes/{book}.json           ← READ — Albert Barnes (NT only)
    rwp/{book}.json              ← READ — Robertson's Word Pictures (NT only)
  interlinear/{book}.json        ← READ — authoritative verse inventory (chapter/verse keys)
scripts/
  ws-synthesis-{book}-{start}-{end}.py   ← WRITE — one script per chapter range
WS_PROGRESS.md                  ← UPDATE — tracker after each script runs
```

---

## 2. Script Naming Convention

`scripts/ws-synthesis-{bookId}-{startCh}-{endCh}.py`

Examples:
```
scripts/ws-synthesis-hebrews-1-4.py
scripts/ws-synthesis-romans-5-8.py
scripts/ws-synthesis-john-1-4.py
scripts/ws-synthesis-genesis-1-5.py
```

---

## 3. Boilerplate — copy verbatim into every script

```python
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_synthesis(book):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_synthesis(book, data):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_synthesis(existing, new_data):
    """Merge new chapter/verse entries without overwriting existing ones."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entry in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entry
```

---

## 4. Full Script Structure

```python
"""
Wide Source Synthesis — {BookName} chapters {start}–{end}
bookId: {bookId}
Run: python3 scripts/ws-synthesis-{bookId}-{start}-{end}.py

Sources used: mhcc, calvin, ellicott, jfb, clarke, wesley[, barnes, rwp]
Chapter range: {start}–{end}  ({N} verses approx.)

Key synthesis decisions:
- <any verse where voices genuinely divide and how you resolved the key_tension>
- <any source whose section entry covered multiple verses — note which key you used>
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_synthesis(book):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_synthesis(book, data):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_synthesis(existing, new_data):
    """Merge new chapter/verse entries without overwriting existing ones."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entry in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entry

HEBREWS = {
    "1": {
        "1": {
            "synthesis": "<p>...</p>",
            "voices": [
                { "src": "calvin",   "attr": "Calvin's Commentaries",    "html": "<p>...</p>" },
                { "src": "mhcc",     "attr": "Matthew Henry Concise",    "html": "<p>...</p>" },
                { "src": "ellicott", "attr": "Ellicott's Commentary",    "html": "<p>...</p>" }
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('hebrews')
    merge_synthesis(existing, HEBREWS)
    save_synthesis('hebrews', existing)
    print('Hebrews 1–4 synthesis complete.')

if __name__ == '__main__':
    main()
```

**Rules:**
1. The data dictionary variable name is the book name in ALL CAPS (`HEBREWS`, `ROMANS`, `JOHN`, `GENESIS`)
2. Chapter and verse keys are **strings**: `"1"` not `1`
3. `synthesis` and `voices[].html` values are HTML strings using `<p>`, `<strong>`, `<em>` only
4. `consensus` is one of: `"affirm"`, `"mixed"`, `"divided"`
5. `key_tension` is `None` (Python) / `null` (JSON) when `consensus = "affirm"`

---

## 5. Reading Source Files

Before writing a single entry, load and inspect the source files for your chapter range:

```python
import json, pathlib

ROOT = pathlib.Path('.')
book = 'hebrews'
ch = '1'

sources = ['mhcc', 'calvin', 'ellicott', 'jfb', 'clarke', 'wesley', 'barnes']
for src in sources:
    p = ROOT / 'data' / 'commentary' / src / f'{book}.json'
    if not p.exists():
        print(f'{src}: not found')
        continue
    data = json.loads(p.read_text())
    ch_data = data.get(ch, {})
    print(f'\n=== {src} chapter {ch} keys: {sorted(ch_data.keys(), key=int)} ===')
    # Print first 200 chars of key "1" if present
    v1 = ch_data.get('1', '')
    print(v1[:200] if v1 else '(no verse 1 entry)')
```

**Section-entry pattern:** Some sources (especially mhcc, jfb) have one entry covering several verses. If `data[ch]` has key `"1"` with content that spans verses 1–4, use that entry for all four verses — but in the `voices` excerpt, note the range ("Henry on vv. 1–4:…").

---

## 6. Verification Check

Run after executing each script:

```python
import json, pathlib

ROOT = pathlib.Path('.')
book = 'hebrews'
start, end = 1, 4

# Load interlinear for authoritative verse inventory
il = json.loads((ROOT / 'data' / 'interlinear' / f'{book}.json').read_text())

# Load synthesis output
syn_path = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
syn = json.loads(syn_path.read_text()) if syn_path.exists() else {}

all_ok = True
for ch in range(start, end + 1):
    ck = str(ch)
    il_vv  = set(il.get(ck, {}).keys())
    syn_vv = set(syn.get(ck, {}).keys())
    missing = il_vv - syn_vv
    if missing:
        print(f'ch {ch} MISSING: {sorted(missing, key=int)}')
        all_ok = False
    else:
        print(f'ch {ch}: {len(syn_vv)} verses ✓')

if all_ok:
    print('All verses present ✓')

# Spot-check: verify synthesis field is non-empty on one verse
v = syn.get('1', {}).get('1', {})
print('\nSample verse 1:1 synthesis length:', len(v.get('synthesis', '')))
print('Voices count:', len(v.get('voices', [])))
print('Consensus:', v.get('consensus'))
```

All chapters must be fully covered before marking the work queue row `complete`.

---

## 7. Output JSON Shape (machine-readable reference)

```
data/commentary/synthesis/{book}.json
{
  "{ch}": {
    "{v}": {
      "synthesis":   "<p>…</p>",                          // required, HTML string
      "voices": [                                          // required, 2–6 items
        {
          "src":  "calvin",                               // source id
          "attr": "Calvin's Commentaries",               // display attribution
          "html": "<p>…</p>"                             // 40–80 word excerpt, HTML
        }
      ],
      "consensus":   "affirm" | "mixed" | "divided",     // required
      "key_tension": null | "…one sentence…"             // required (null if affirm)
    }
  }
}
```
