# Z Commentary Script Guide

This document describes how to write a `scripts/zc-{type}-{book}-{start}-{end}.py` commentary or echo script. Read it before writing any Z-series script.

---

## What a static commentary script does

A commentary script contains per-verse HTML commentary for one type and one book range, **hardcoded as a Python dictionary**. Running it merges those verses into the existing JSON files without touching anything already written. No API calls; no external lookups at runtime.

---

## Four script types

| Type | Output | Script name pattern |
|------|--------|---------------------|
| `echo`     | `data/echoes/{book}.json`                   | `zc-echo-{book}-{start}-{end}.py`     |
| `original` | `data/commentary/mkt-original/{book}.json`  | `zc-original-{book}-{start}-{end}.py` |
| `context`  | `data/commentary/mkt-context/{book}.json`   | `zc-context-{book}-{start}-{end}.py`  |
| `christ`   | `data/commentary/mkt-christ/{book}.json`    | `zc-christ-{book}-{start}-{end}.py`   |

---

## Commentary script structure (`original` / `context` / `christ`)

### 1. Header docstring

```python
"""
MKT {Type} Commentary — {Book} chapters {start}–{end}
Run: python3 scripts/zc-{type}-{book}-{start}-{end}.py

Source data used:
- data/interlinear/{book}.json
- data/translation/glossary-{greek|hebrew}.json (contested terms)
- data/translation/notes/{book}.json (translation reasoning if present)
- data/translation/draft/mediating/{book}.json (MKT text for quoting)

Key decisions in this range:
- <any non-obvious interpretive choices>
- <sources cited for historical/cultural claims>
- <Christological classification choices used>
"""
```

### 2. Boilerplate

Copy this block verbatim — do not rename helpers:

```python
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html
```

### 3. Commentary dictionary

```python
BOOKNAME = {
  "3": {
    "16": '<p><strong>ἠγάπησεν</strong> (aorist) — a single, completed act, not ongoing sentiment. God gave; this is a historical event, not a disposition.</p><p>μονογενῆ — <em>only-begotten</em>, carrying both uniqueness and the relational weight of the father–son bond that makes the gift costly.</p>',
    "17": '<p>The double negative (<em>οὐ … ἵνα κρίνῃ</em>) is emphatic: the mission is rescue, not condemnation. Condemnation is the pre-existing default state — not an additional sentence the Son brings.</p>'
  }
}
```

All chapter and verse keys are **strings** (`"3"`, `"16"`) — not integers.

### 4. `main()`

```python
def main():
    existing = load_comm('mkt-original', 'john')   # ← adjust source and book
    merge_comm(existing, BOOKNAME)
    save_comm('mkt-original', 'john', existing)
    print('John 3–5 mkt-original written.')

if __name__ == '__main__':
    main()
```

Replace `'mkt-original'` with `'mkt-context'` or `'mkt-christ'` as appropriate. Replace `'john'` with the lowercase filename stem (`'1corinthians'`, `'songofsolomon'`, etc.).

---

## HTML conventions

Each verse value is a **single HTML string** injected into the commentary panel.

- `<p>` is the primary block element; consecutive `<p>` tags are fine
- `<strong>` for key terms, lemma headings, or phrases being discussed
- `<em>` for inline Greek/Hebrew words or transliterations
- No `<h1>`–`<h6>` — the verse-study page provides the section heading
- No inline `style="..."` attributes — page CSS handles sizing and colour
- No `<div>` wrappers — the single string is injected directly
- Keep HTML well-formed: no unclosed tags; use `&amp;` for bare ampersands
- For Greek/Hebrew inline: prefer `<em>agápē</em> (love)` pattern — transliteration first, gloss in parentheses

**Examples from existing commentaries (match this register):**

Ellicott-style (verse-level, philological):
```html
<p>(16) <strong>For God so loved the world.</strong>—The aorist ἠγάπησεν marks the gift as a single historical act...</p>
```

MKT-original style (no verse number prefix needed — verse-study already shows it):
```html
<p><strong>ἠγάπησεν</strong> (aorist) — the giving of the Son is a completed event, not a disposition...</p>
```

---

## Echo script structure

### Echo schema

```json
{
  "1": {
    "29": [
      { "type": "type",     "target": "Exod 12:3",  "note": "The Passover lamb — slain for the protection of God's people, blood applied to avert judgment — structurally anticipates Christ's atoning death." },
      { "type": "allusion", "target": "Isa 53:7",   "note": "The Servant led as a lamb to slaughter; John the Baptist's naming activates the Isaiah 53 register without explicit citation." }
    ]
  }
}
```

**Echo types:**

| Type | Use when |
|------|----------|
| `quote`       | NT text directly quotes OT (verbatim or LXX) |
| `allusion`    | Deliberate verbal or thematic echo — not a direct quote |
| `type`        | OT person, institution, or event structurally anticipating Christ or NT fulfillment |
| `shadow`      | Broader OT pattern pointing forward — less structurally direct than a type |
| `theme`       | Shared theological theme across OT–NT without a specific verbal connection |
| `fulfillment` | NT text explicitly presents itself as fulfilling OT prediction |

**Classify honestly.** Prefer `allusion` over `fulfillment` unless the NT text explicitly claims fulfillment. The `note` field must contain the **argument** — one or two sentences explaining *why* the connection holds and what it contributes to interpretation.

### Echo boilerplate

```python
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))
```

### Echo dictionary

```python
BOOKNAME_ECHOES = {
  "1": {
    "29": [
      { "type": "type",     "target": "Exod 12:3",  "note": "Passover lamb → ..." },
      { "type": "allusion", "target": "Isa 53:7",   "note": "Servant lamb → ..." }
    ]
  }
}
```

### Echo `main()`

```python
def main():
    existing = load_echo('john')
    merge_echo(existing, BOOKNAME_ECHOES)
    save_echo('john', existing)
    print('John 1–6 echoes written.')

if __name__ == '__main__':
    main()
```

---

## Parallels absorption (do before writing echo scripts for any book)

The existing `data/parallels/{book}.json` files are the prototype that echoes replace. Check for a parallels file before writing a new echo script:

```python
import json
p = json.load(open('data/parallels/{book}.json'))
# Format: { "ch": { "v": [ { "type": "prophecy-source"|"quotation"|"parallel",
#                              "refs": [{ "passage": "Genesis 1:1", "label": "..." }] } ] } }
```

**Absorption map:**

| Parallels `type` | → Echo `type` |
|-----------------|---------------|
| `prophecy-source` | `fulfillment` if NT explicitly claims it; else `type` or `allusion` |
| `quotation`       | `quote` |
| `parallel`        | `theme` or `allusion` — evaluate each case |

Every absorbed entry **must gain a `note` field**. Parallels only have a `label` (e.g. `"Voice crying in the wilderness"`); the echo `note` must be a sentence explaining why the connection holds and what it reveals. Do not carry the `label` forward verbatim as the `note`.

---

## Source data available

| Data | File | Notes |
|------|------|-------|
| Original language tokens | `data/interlinear/{book}.json` | `s` = Strongs code, `text` = surface gloss |
| Glossary / semantic range | `data/translation/glossary-{greek\|hebrew}.json` | `semantic_range`, `dispute_level`, `source_data.thayer` / `.bdb` |
| MKT mediating text | `data/translation/draft/mediating/{book}.json` | Quote the MKT text when illustrating translation choices |
| Translation notes | `data/translation/notes/{book}.json` | `reasoning.decisions`, `reasoning.key_terms` (present only where `translate-with-claude.py` has run) |
| Existing parallels | `data/parallels/{book}.json` | Absorb before writing echo scripts |
| Ellicott's Commentary | `data/commentary/ellicott/{book}.json` | Best verse-level philological source; cite content, not Ellicott by name |
| JFB | `data/commentary/jfb/{book}.json` | Useful for historical background and cultural context |

---

## Quality checklist

- [ ] Every verse in the claimed range has a non-empty entry (no gaps — genealogy verses and formulaic lines need brief entries)
- [ ] HTML is well-formed — no unclosed tags, no bare `&`
- [ ] Commentary adds information — no verse entry merely paraphrases the MKT text
- [ ] Echo notes contain an argument, not just a label
- [ ] Echo types are classified conservatively — prefer `allusion` over `fulfillment` when uncertain
- [ ] Script exits cleanly, prints expected `wrote …` lines
- [ ] Spot-check 3 verses:
  ```bash
  python3 -c "import json; d=json.load(open('data/commentary/mkt-original/john.json')); print(d['3']['16'])"
  ```

---

## Continuity

**Always read any previously completed scripts for the same book and type** before starting. Carry forward:

- Terminology (e.g. "the Evangelist" vs. "John"; "Paul" vs. "the Apostle")
- Cultural framework language (patron-client, honor-shame, covenant-loyalty)
- How specific contested terms (σάρξ, πνεῦμα, δικαιοσύνη, יהוה, חֶסֶד) are discussed
- Whether a Christological classification (type vs. shadow) was fixed for an OT motif
- Consistent citation form for OT echoes (`Isa 53:7`, not `Isaiah 53:7` — abbreviate)

Inconsistency within a book across scripts is a defect.
