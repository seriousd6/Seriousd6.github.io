# BP Script Guide — Biblepedia Article Synthesis

## Script naming

```
scripts/bp-{unit-id}.py
```

Examples: `scripts/bp-a1.py`, `scripts/bp-h3.py`, `scripts/bp-gap-nav1.py`

---

## Exact boilerplate (copy verbatim, fill in header and ARTICLES dict)

```python
"""
BP Article Synthesis — {unit-id}: {FirstTerm} → {LastTerm}
Covers Easton entries: {FirstTerm} through {LastTerm} ({count} entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'sea of', 'river', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals
  - names:    Hitchcock-only (no Easton/Smith entry exists)
  - events:   title is clearly an event (battle, feast, exile, flood, etc.)

Script: scripts/bp-{unit-id}.py
Run: python3 scripts/bp-{unit-id}.py
"""

import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)


def load_article(slug):
    path = os.path.join(OUT_DIR, slug + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None


def save_article(slug, data):
    path = os.path.join(OUT_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def merge_article(slug, data):
    # Never overwrite an existing synthesis — idempotent safety
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


# ── Article data ──────────────────────────────────────────────────────────────
# Keys are Easton's `id` slugs (lowercase, hyphenated).
# For gap articles (Nave/Smith-only), use a normalized slug derived from term.
ARTICLES = {
    "aaron": {
        "id": "aaron",
        "term": "Aaron",
        "category": "people",
        "intro": "<p>Aaron, the eldest son of Amram and Jochebed and elder brother of Moses, was the first High Priest of Israel. His name is variously interpreted as <em>mountain of strength</em>, <em>mountaineer</em>, or <em>illuminator</em>. Born during Israel's bondage in Egypt, Aaron became Moses's spokesman before Pharaoh and later the mediator between God and the congregation at the tabernacle.</p><p>His appointment as High Priest established the Aaronic line that served at the sanctuary for generations. Though he shared responsibility for the golden calf incident—a serious failure of leadership—Aaron was restored to priestly service and died on Mount Hor, transferring the priestly vestments to his son Eleazar. The New Testament's Epistle to the Hebrews cites Aaron as a type of Christ, whose priesthood fulfills and surpasses the Levitical order.</p>",
        "hitchcock_meaning": "mountain of strength",
        "source_ids": {
            "easton": "aaron",
            "smith": "aaron",
            "isbe": "aaron"
        },
        "key_refs": ["Exodus 6:20", "Exodus 28:1", "Numbers 20:28", "Hebrews 5:4"]
    },
    # ... remaining entries in your range
}


def main():
    written = 0
    skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP {__doc__.split(chr(10))[1].strip()}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
```

---

## Article JSON schema

```json
{
  "id": "string — Easton's id slug (or normalized term for gap articles)",
  "term": "string — display name, title-cased",
  "category": "people | places | concepts | names | events",
  "intro": "string — HTML, <p> tags only, 150–300 words, two paragraphs max",
  "sections": [],
  "hitchcock_meaning": "string | null — from Hitchcock, if available",
  "source_ids": {
    "easton": "string | null",
    "smith": "string | null",
    "isbe": "string | null",
    "nave": "string | null"
  },
  "key_refs": ["array of verse reference strings from the entry's refs array"]
}
```

**Field notes:**
- `sections` — always `[]` for stubs; a future enrichment pass may add sections
- `source_ids` — set only the sources that actually have an entry for this term
- `key_refs` — take the first 4–6 refs from Easton's `refs` array; if Easton has none, use Smith or ISBE
- `intro` — valid HTML fragment; no `<div>`, `<h>`, `<ul>`, `<ol>`; only `<p>`, `<em>`, `<strong>`, `<a class="ref" data-ref="...">` for inline verse refs

---

## Gap article slugs (Phase 2 — Nave-only / Smith-only)

For topics that have no Easton entry, derive the slug as:
```python
slug = term.lower().replace(' ', '-').replace(',', '').replace("'", '').replace('.','')
```

Examples:
- `"JESUS, THE CHRIST"` → `"jesus-the-christ"`
- `"AFFLICTIONS AND ADVERSITIES"` → `"afflictions-and-adversities"`
- `"ZEAL, RELIGIOUS"` → `"zeal-religious"`

Use `nave` as the source in `source_ids` and omit `easton`/`smith`/`isbe` if they have no entry.
Set `key_refs` to the first 5 verses from Nave's `verses` array.

---

## Category detection rules

Apply in this order (first match wins):

1. **events** — if the term contains: `battle of`, `siege of`, `fall of`, `exodus`, `captivity`, `exile`, `flood`, `passover`, `pentecost`, `transfiguration`
2. **places** — if the term or Easton brief contains: `city of`, `town of`, `village of`, `sea of`, `river`, `mount `, `mountain`, `valley`, `land of`, `region of`, `wilderness of`, `plain of`
3. **people** — if Hitchcock has an entry for this term AND brief does NOT trigger places rule
4. **names** — if Hitchcock has an entry AND there is NO Easton/Smith article (Hitchcock-only)
5. **concepts** — everything else

---

## Intro quality checklist

Before finalizing each intro, verify:

- [ ] Opens with the subject (not "In biblical history…" or "The word…")
- [ ] Includes the key identity/role in the first sentence
- [ ] Does not exceed 300 words
- [ ] Does not contain unsourced claims (every fact derivable from source texts)
- [ ] Does not use first person or devotional language ("Let us…", "We see…")
- [ ] No broken HTML (all tags closed, no bare `&` without entity encoding)
- [ ] Hitchcock meaning cited as `<em>meaning</em>` inline, not as a separate sentence
- [ ] NT/OT balance where both testaments treat the topic
