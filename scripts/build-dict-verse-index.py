#!/usr/bin/env python3
"""
build-dict-verse-index.py — Build per-book verse-index for Easton's dictionary.

Reads all data/dictionary/{slug}.json, collects refs per verse, and writes
  data/dictionary/verse-index/{bookId}.json
  { "ch": { "v": [{id, term}, ...] } }

Run from repo root: python3 scripts/build-dict-verse-index.py
"""

import json, re
from pathlib import Path
from collections import defaultdict

REPO    = Path(__file__).resolve().parent.parent
DICT_DIR = REPO / 'data' / 'dictionary'
OUT_DIR  = REPO / 'data' / 'dictionary' / 'verse-index'
BOOKS_JSON = REPO / 'data' / 'bible' / 'books.json'

def build_name_to_id(books_json):
    books = json.loads(books_json.read_text())
    return {b['name'].lower(): b['id'] for b in books}

REF_RE = re.compile(r'^(.+?)\s+(\d+)(?::(\d+))?$')

def parse_ref(ref_str, name_map):
    """'Genesis 1:27' → (bookId, '1', '27') or None."""
    m = REF_RE.match(ref_str.strip())
    if not m:
        return None
    book_name = m.group(1).lower()
    ch = m.group(2)
    v  = m.group(3)
    if not v:
        return None  # chapter-level refs — skip for verse index
    book_id = name_map.get(book_name)
    if not book_id:
        return None
    return (book_id, ch, v)

def main():
    name_map = build_name_to_id(BOOKS_JSON)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # book_id → ch → v → [{id, term}]
    idx = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    entries = sorted(DICT_DIR.glob('*.json'))
    for p in entries:
        if p.name == 'index.json':
            continue
        data = json.loads(p.read_text())
        slug  = data.get('id', p.stem)
        term  = data.get('term', slug)
        for ref in data.get('refs', []):
            parsed = parse_ref(ref, name_map)
            if not parsed:
                continue
            bid, ch, v = parsed
            # Avoid duplicates per (book, ch, v, slug)
            existing = idx[bid][ch][v]
            if not any(e['id'] == slug for e in existing):
                existing.append({'id': slug, 'term': term})

    written = 0
    for bid, ch_map in idx.items():
        # Convert defaultdict to plain dict for serialization
        out = {ch: dict(v_map) for ch, v_map in ch_map.items()}
        out_path = OUT_DIR / f'{bid}.json'
        out_path.write_text(json.dumps(out, ensure_ascii=False, separators=(',', ':')), 'utf-8')
        written += 1

    total_verses = sum(
        sum(len(vs) for vs in ch_map.values())
        for ch_map in idx.values()
    )
    print(f'Written {written} book files, {total_verses} verse entries → data/dictionary/verse-index/')

if __name__ == '__main__':
    main()
