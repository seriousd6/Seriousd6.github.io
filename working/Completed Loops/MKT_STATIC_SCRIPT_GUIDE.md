# MKT Static Script Guide

This document describes how to write a `scripts/mkt-{book}-{start}-{end}.py` translation script. Read it before writing any new script.

---

## What a static script does

A static script contains the three-tier translation for a range of chapters **hardcoded as a Python dictionary**. Running it merges those chapters into the existing draft JSON files without touching anything already translated. There are no API calls, no glossary lookups at runtime — the agent writes the translation prose directly.

---

## File structure

### 1. Header docstring

```python
"""
MKT {Book} chapters {start}–{end} — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-{book}-{start}-{end}.py

Translation decisions:
- {STRONG_CODE} ({lemma}): "{L rendering}" (L) / "{M rendering}" (M) / "{T rendering}" (T) — reason
- {STRONG_CODE} ({lemma}): ...
- Any textual-critical notes (disputed verses, manuscript variants)
- Aspect and tense notes specific to this passage
- OT echo notes if relevant
"""
```

The header must document every contested-term decision made (Section 6 of `TRANSLATION_AGENT_GUIDE.md`) and any non-obvious choices. This is the only place for prose explanation — do not scatter comments through the data.

### 2. Boilerplate imports and helpers

Copy this block verbatim — do not vary the helper names or signatures:

```python
import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]
```

`merge_tier` only writes chapter/verse keys that are absent in the existing file. It never overwrites content that is already there.

### 3. Translation dictionary

```python
BOOKNAME = {
  "16": {
    "1": {
      "L": "Literal rendering — word-for-word, source syntax preserved.",
      "M": "Mediating rendering — natural English, accurate primary glosses.",
      "T": "Thought rendering — meaning-driven; idioms as meaning, poetry with cadence."
    },
    "2": {
      "L": "...",
      "M": "...",
      "T": "..."
    }
  },
  "17": { ... }
}
```

**Key rules:**
- All chapter and verse keys are **strings** (`"16"`, not `16`)
- Every verse must have all three keys: `"L"`, `"M"`, `"T"`
- Do not skip verses — translate every verse in the range, including doxologies, genealogy entries, and repeated formulas
- Do not use `None` or empty strings for any tier

### 4. main() function

```python
def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'bookname')
        merge_tier(existing, BOOKNAME, tier_key)
        save(tier_dir, 'bookname', existing)
    print('{Book} {start}–{end} written.')

if __name__ == '__main__':
    main()
```

Replace `'bookname'` with the lowercase filename stem (e.g. `'acts'`, `'1corinthians'`, `'songofsolomon'`). This must match the filename in `data/translation/draft/literal/`.

---

## Reading the interlinear source

Before translating a chapter, read its token data:

```
data/interlinear/{book}.json
```

Format: `{ "ch": { "v": [ { "s": "G1234", "text": "english gloss" }, ... ] } }`

- `s` — Strong's code (`G####` = Greek, `H####` = Hebrew)
- `text` — the English surface gloss from the base interlinear

The token order is often scrambled (interlinear word order, not English). Use it to identify which Greek/Hebrew words are present, look up disputed codes in the glossary, and determine aspect/tense for verbs. Do not simply concatenate the token `text` fields — that produces word salad, not translation.

---

## Looking up a Strong's code

If you need the full lexical entry for a code:

```python
import json
g = json.load(open('data/translation/glossary-greek.json'))
print(g.get('G3056'))   # λόγος
```

Fields of interest: `lemma`, `pos`, `dispute_level`, `tiers.literal.primary`, `semantic_range`, `source_data.dodson.def`.

All entries are still status `draft` — the primary gloss is a proposed rendering, not a confirmed decision. You may deviate from it when context requires; document the deviation in the script header.

---

## Continuity with adjacent scripts

**Always read the most recently completed script for the same book** before writing. Key things to carry forward:

- How contested terms were rendered in prior chapters (especially `πνεῦμα`, `σάρξ`, `κύριος`, `יהוה`, `חֶסֶד`)
- Whether `ἐκκλησία` is rendered "assembly / church / community" or a different choice
- The capitalisation convention for Spirit/spirit
- Any OT quotation rendering style locked in for this book
- Poetic structure decisions (e.g. whether Psalms use line breaks in T tier)

Inconsistency across scripts for the same book is a defect. If a prior script made a choice you disagree with, note it in the header but maintain consistency — change it only if you plan to also fix prior chapters.

---

## Three-tier mandates

| Tier | Key | Rule |
|------|-----|------|
| Literal | `L` | Word-for-word. Preserve source word order where English tolerates it. Keep grammatical awkwardness. Use Strong's-accurate words even if stiff. |
| Mediating | `M` | Natural English sentences. Accurate primary glossary renderings. No paraphrase, no added explanation. |
| Thought | `T` | Meaning-driven. Idioms rendered as their meaning. Hebrew poetry gets cadence and line breaks. Honour-shame dynamics, OT echoes, and Greek aspect nuances are surfaced explicitly. |

L should read like a trot. M should read like a careful modern translation. T should read like a scholar who also writes well.

---

## Verse-level quality checklist

Before finalising each verse, confirm:

- [ ] L preserves the source's word count approximately — not padded with explanation
- [ ] M reads as a complete, natural English sentence
- [ ] T adds genuine interpretive value over M — if T ≈ M, rewrite T
- [ ] Contested terms (Section 6 of the guide) have explicit, consistent renderings
- [ ] Aspect is honoured: aorist = completed act, present = ongoing, perfect = past act with lasting result
- [ ] Divine name H3068 (יהוה): use `LORD` (small caps convention) in L/M; `the LORD` or `Yahweh` in T depending on context — document your choice in the header
- [ ] No verse has an empty string or placeholder text in any tier

---

## After running

1. Verify the script prints the expected `wrote ...` lines with no errors
2. Spot-check 3 verses spread across the range:
   ```python
   import json
   d = json.load(open('data/translation/draft/literal/{book}.json'))
   print(d['16']['1'])   # first verse of claimed range
   print(d['18']['20'])  # mid-range
   print(d['21']['38'])  # last verse of claimed range
   ```
3. Confirm those verses are real prose, not word salad
4. Then update `MKT_PROGRESS.md` per the tracker update instructions in `MKT_AGENT_PROMPT.md`
