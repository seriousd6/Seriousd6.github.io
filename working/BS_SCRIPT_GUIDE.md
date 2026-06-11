# Book Study — Script Guide

This guide defines the Python script structure every agent must follow when generating book study data.

---

## 1. Directory structure

```
data/
  books/introductions/{bookId}.json   ← READ ONLY — primary intro source (author, date, outline, themes_detail, christ_connection, etc.)
  workshop/book-study/{bookId}.json   ← WRITE TARGET — supplemental data (key_vocab, language_notes, reception, reading_guide)
  grammar/
    author-freq-greek.json            ← READ — NT vocabulary frequency by author group
    author-freq-hebrew.json           ← READ — OT vocabulary frequency by author group
  translation/
    glossary-greek.json               ← READ — Greek lemma / translit / tiers / semantic_range
    glossary-hebrew.json              ← READ — Hebrew lemma / translit / tiers / semantic_range
  literary/genre.json                 ← READ — genre, sub[], literary_note, structure_note
  cultural/book-context.json          ← READ — historical_context, cultural_frameworks, key_cultural_notes
scripts/
  build-book-study-{bookId}.py        ← WRITE — one script per book
BS_PROGRESS.md                        ← UPDATE — tracker after each script runs successfully
```

---

## 2. Script naming convention

`scripts/build-book-study-{bookId}.py`

Examples:
```
scripts/build-book-study-romans.py
scripts/build-book-study-john.py
scripts/build-book-study-genesis.py
scripts/build-book-study-psalms.py
```

---

## 3. Boilerplate — copy verbatim into every script

```python
import json, os, sys

def load_book_study(book_id):
    path = f'data/workshop/book-study/{book_id}.json'
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_book_study(book_id, data):
    os.makedirs('data/workshop/book-study', exist_ok=True)
    path = f'data/workshop/book-study/{book_id}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'wrote {path} ({len(data.get("key_vocabulary", []))} vocab entries)')

def merge_book_study(existing, new_data):
    """Fill only fields not already present. Safe to re-run."""
    result = dict(existing)
    for key, val in new_data.items():
        if key not in result or not result[key]:
            result[key] = val
    return result
```

---

## 4. Full script structure

```python
"""
Book Study Data — {BookName}
book_id: {bookId}
lang: greek | hebrew

Run: python3 scripts/build-book-study-{bookId}.py

Notes:
- Key vocabulary selected from {author_group} author group peaks in author-freq-{lang}.json
- [any non-obvious interpretation decisions or notable language features]
"""

import json, os, sys

# ── boilerplate ──────────────────────────────────────────────────────────────

def load_book_study(book_id):
    path = f'data/workshop/book-study/{book_id}.json'
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_book_study(book_id, data):
    os.makedirs('data/workshop/book-study', exist_ok=True)
    path = f'data/workshop/book-study/{book_id}.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'wrote {path} ({len(data.get("key_vocabulary", []))} vocab entries)')

def merge_book_study(existing, new_data):
    result = dict(existing)
    for key, val in new_data.items():
        if key not in result or not result[key]:
            result[key] = val
    return result

# ── content ──────────────────────────────────────────────────────────────────

BOOK_STUDY = {
    "bookId": "{bookId}",

    "key_vocabulary": [
        {
            "code": "G####",
            "lemma": "...",
            "translit": "...",
            "gloss": "...",
            "significance": "2–3 sentences on WHY this word matters in THIS book specifically."
        },
        # 12–18 entries total
    ],

    "language_notes": (
        "<p>First paragraph — most important language feature of this book.</p>"
        "<p>Second paragraph — second feature.</p>"
        "<p>Third paragraph — third feature, or specific verse examples.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> ...</p>"
        "<p><strong>Reformation:</strong> ...</p>"
        "<p><strong>Modern debates:</strong> ...</p>"
    ),

    "reading_guide": (
        "<p>The single most important thing to understand before reading...</p>"
        "<p>What to watch for verse by verse...</p>"
        "<p>Common misreadings: ...</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('{bookId}')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('{bookId}', merged)

main()
```

---

## 5. Content dictionary rules

### `key_vocabulary` entries

Required fields on every entry: `code`, `lemma`, `translit`, `gloss`, `significance`.

- `code` — Strong's code exactly as it appears in glossary-{lang}.json (e.g., `"G1343"`, `"H2617"`)
- `lemma` — copy from glossary entry `lemma` field
- `translit` — copy from glossary entry `translit` field
- `gloss` — copy from `tiers.literal.primary` in the glossary entry (not the raw Strongs gloss)
- `significance` — your original content; do not copy from semantic_range or source_data

Aim for 12 minimum, 18 maximum entries per book. Small epistles (Philemon, 2–3 John, Jude) may have fewer — 8 is acceptable for books under 30 verses.

### HTML rules (language_notes, reception, reading_guide)

Use only: `<p>`, `<strong>`, `<em>`. No `<h3>`, `<h4>`, `<ul>`, `<li>`, `<table>`. The UI provides all section headings and layout.

**Correct:**
```python
"language_notes": (
    "<p>Paul's use of <strong>δικαιοσύνη</strong> (righteousness) in Romans is consistently forensic..."
    "</p>"
    "<p>The particle <em>γάρ</em> appears 65× in Romans...</p>"
),
```

**Incorrect:**
```python
"language_notes": "<h3>Key Greek Features</h3><ul><li>Aorist tense...</li></ul>",
```

Use Python string concatenation (not `+`) to keep lines short:
```python
"language_notes": (
    "<p>First paragraph.</p>"
    "<p>Second paragraph.</p>"
),
```

---

## 6. Verification checklist (run after `python3 scripts/build-book-study-{bookId}.py`)

```python
import json, os

book_id = '{bookId}'  # ← change this
path = f'data/workshop/book-study/{book_id}.json'

assert os.path.exists(path), f'File not found: {path}'
data = json.load(open(path))

# Required fields present
for field in ['bookId', 'key_vocabulary', 'language_notes', 'reception', 'reading_guide']:
    assert field in data and data[field], f'Missing or empty: {field}'

# Vocabulary quality checks
vocab = data['key_vocabulary']
assert 8 <= len(vocab) <= 18, f'Expected 8–18 vocab entries, got {len(vocab)}'
for i, entry in enumerate(vocab):
    for f in ['code', 'lemma', 'gloss', 'significance']:
        assert entry.get(f), f'Entry {i} missing field: {f}'
    assert len(entry['significance']) >= 80, f'Entry {i} significance too short (< 80 chars)'

# HTML fields are non-trivial
for field in ['language_notes', 'reception', 'reading_guide']:
    assert len(data[field]) >= 200, f'{field} too short (< 200 chars)'
    assert '<p>' in data[field], f'{field} missing <p> tags'

print(f'✓ {book_id}: {len(vocab)} vocab entries, all fields present and non-trivial')
```

Copy this into a shell cell and run it after the script to confirm output before marking the tracker row complete.

---

## 7. Re-run safety

`merge_book_study()` only fills fields not already present and non-empty. It is always safe to re-run a script. If you need to force-overwrite a specific field, delete it from the JSON file manually first, then re-run.

---

## 8. Run command

Always run scripts from the repo root:

```bash
python3 scripts/build-book-study-{bookId}.py
```

The script will print:
```
wrote data/workshop/book-study/{bookId}.json (15 vocab entries)
```

Any Python error means the script did not write. Fix before marking the tracker.
