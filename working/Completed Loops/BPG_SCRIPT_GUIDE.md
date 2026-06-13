# BPG Script Guide — Biblepedia Gap Analysis

## Phase 1 script: bpg-compute-gaps.py

This script is **ready to run** — it requires no content authoring.
It loads all existing source indexes and computes coverage gaps algorithmically.

```bash
python3 scripts/bpg-compute-gaps.py
```

Output: `data/biblepedia/gaps.json` — an array of gap objects, sorted by priority_score desc.

---

## Gap JSON schema

```json
[
  {
    "id": "jesus-the-christ",
    "term": "Jesus, the Christ",
    "original_title": "JESUS, THE CHRIST",
    "gap_type": "doctrine-no-article",
    "sources_present": ["nave"],
    "sources_absent": ["easton", "smith", "isbe"],
    "nave_verse_count": 2471,
    "nave_slug": "jesus-the-christ",
    "isbe_id": null,
    "smith_id": null,
    "hitchcock_meaning": null,
    "priority_score": 98,
    "status": "not-reviewed"
  }
]
```

**`status` values (set during Phase 2 curation):**
- `not-reviewed` — initial state
- `stub-needed` — add to BP Phase 2 work queue
- `redirect-only` — variant/alias; set `redirect_to` field
- `names-only` — minor name, low priority
- `already-covered` — article exists in data/biblepedia/articles/
- `skip` — too obscure or data artifact

---

## Phase 2 curation script: bpg-curate.py

Agents running Phase 2 write a small curation script for each batch of gaps they review.
This preserves the claim/work/verify pattern and keeps curation decisions in source control.

```python
"""
BPG Curation — Batch {N}: {FirstTerm} → {LastTerm}
Gaps reviewed: {count}

Decisions documented below. Status values:
  stub-needed   — add to BP Phase 2 queue
  redirect-only — alias; redirect_to field set
  names-only    — minor name, low priority  
  skip          — too obscure or data artifact
  already-covered — article exists

Script: scripts/bpg-curate-{N}.py
Run: python3 scripts/bpg-curate-{N}.py
"""

import json, os

GAPS_FILE = 'data/biblepedia/gaps.json'


def load_gaps():
    with open(GAPS_FILE, encoding='utf-8') as f:
        return json.load(f)


def save_gaps(gaps):
    with open(GAPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(gaps, f, ensure_ascii=False, indent=2)


# Curation decisions: { id: { status, redirect_to? } }
DECISIONS = {
    "jesus-the-christ":          { "status": "stub-needed" },
    "afflictions-and-adversities": { "status": "stub-needed" },
    "works":                     { "status": "skip" },
    "character":                 { "status": "skip" },
    "elias":                     { "status": "redirect-only", "redirect_to": "elijah" },
}


def main():
    gaps = load_gaps()
    idx  = { g['id']: g for g in gaps }
    updated = 0
    for gid, decision in DECISIONS.items():
        if gid in idx:
            idx[gid].update(decision)
            updated += 1
        else:
            print(f'WARNING: gap id {gid!r} not found in gaps.json')
    save_gaps(list(idx.values()))
    print(f'BPG Curation batch: updated {updated} gaps.')


if __name__ == '__main__':
    main()
```

---

## Output directory convention

| File | Created by | Purpose |
|---|---|---|
| `data/biblepedia/gaps.json` | `bpg-compute-gaps.py` | Master gap list (Phase 1 output) |
| `data/biblepedia/redirects.json` | Populated from `redirect-only` decisions | Term → target slug mapping for Biblepedia JS |
| `data/biblepedia/articles/{slug}.json` | BP loop scripts | Synthesized article stubs |
| `data/biblepedia/index.json` | `bpg-build-index.py` (future) | Aggregate index of all synthesized articles |
