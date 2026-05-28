#!/usr/bin/env python3
"""
Builds data/library/verse-index/{bookId}.json reverse-lookup files.

For each library document, extracts every proof-text .ref[data-ref]
element inside .lib-refs spans and maps the cited verse back to the
section that cites it.

Output citation shape:
  { "doc": "WCF", "slug": "westminster-confession",
    "section": "1", "heading": "Chapter I — Of the Holy Scripture" }

Run from repo root:  python3 scripts/build-verse-index.py
"""

import json
import re
from pathlib import Path
from collections import defaultdict

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit('pip install beautifulsoup4')

REPO      = Path(__file__).resolve().parent.parent
DOCS_DIR  = REPO / 'data' / 'library' / 'docs'
OUT_DIR   = REPO / 'data' / 'library' / 'verse-index'
BOOKS_JSON = REPO / 'data' / 'bible' / 'books.json'


def build_book_map(books):
    m = {}
    for b in books:
        bid = b['id']
        m[b['name'].lower()] = bid
        for a in b['abbrevs']:
            m[a.lower()] = bid
    # Common variants not always in abbrevs
    extras = {
        'psalm':            'psalms',
        'ps':               'psalms',
        'song of songs':    'song-of-solomon',
        'song of sol':      'song-of-solomon',
        'sos':              'song-of-solomon',
        '1 cor':            '1-corinthians',
        '2 cor':            '2-corinthians',
        '1 tim':            '1-timothy',
        '2 tim':            '2-timothy',
        '1 thess':          '1-thessalonians',
        '2 thess':          '2-thessalonians',
        'gal':              'galatians',
        'eph':              'ephesians',
        'phil':             'philippians',
        'col':              'colossians',
        'heb':              'hebrews',
        'jas':              'james',
        'rev':              'revelation',
        'matt':             'matthew',
        'mat':              'matthew',
        'mk':               'mark',
        'lk':               'luke',
        'jn':               'john',
        'acts':             'acts',
        'rom':              'romans',
        'prov':             'proverbs',
        'eccl':             'ecclesiastes',
        'isa':              'isaiah',
        'jer':              'jeremiah',
        'ezek':             'ezekiel',
        'dan':              'daniel',
        'hos':              'hosea',
        'zech':             'zechariah',
        'mal':              'malachi',
        'deut':             'deuteronomy',
        'num':              'numbers',
        'lev':              'leviticus',
        'exod':             'exodus',
        'gen':              'genesis',
    }
    for k, v in extras.items():
        m.setdefault(k, v)
    return m


def parse_ref(ref_str, book_map):
    """
    Parse 'Romans 3:23' or 'Romans 3:23-25' → (bookId, chapter, verse).
    Returns None for chapter-only refs or unrecognised books.
    Only indexes the *start* verse of a range.
    """
    ref_str = ref_str.strip()
    m = re.match(
        r'^((?:\d\s+)?[A-Za-z][A-Za-z\s\.]*?)\s+(\d+):(\d+)(?:-\d+)?$',
        ref_str
    )
    if not m:
        return None
    book_raw = m.group(1).strip().rstrip('.')
    ch       = m.group(2)
    v        = m.group(3)
    bid      = book_map.get(book_raw.lower())
    if not bid:
        return None
    return (bid, ch, v)


def main():
    books    = json.loads(BOOKS_JSON.read_text('utf-8'))
    book_map = build_book_map(books)

    # verse_index[bookId][ch][v] = list of citation dicts
    verse_index = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    skipped = []

    for doc_path in sorted(DOCS_DIR.glob('*.json')):
        doc    = json.loads(doc_path.read_text('utf-8'))
        abbrev = doc['abbrev']
        slug   = doc['id']

        for section in doc['sections']:
            sec_ref = section['ref']
            heading = section['heading']

            soup = BeautifulSoup(section['html'], 'html.parser')
            for refs_span in soup.find_all(class_='lib-refs'):
                for link in refs_span.find_all('a', attrs={'data-ref': True}):
                    data_ref = link.get('data-ref', '').strip()
                    parsed = parse_ref(data_ref, book_map)
                    if not parsed:
                        if ':' in data_ref:
                            skipped.append(data_ref)
                        continue
                    bid, ch, v = parsed
                    citation = {
                        'doc':     abbrev,
                        'slug':    slug,
                        'section': sec_ref,
                        'heading': heading,
                    }
                    existing = verse_index[bid][ch][v]
                    is_dup = any(
                        e['doc'] == abbrev and e['section'] == sec_ref
                        for e in existing
                    )
                    if not is_dup:
                        existing.append(citation)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    total_cits = 0
    for bid in sorted(verse_index):
        ch_data = verse_index[bid]
        out = {ch: dict(vs) for ch, vs in ch_data.items()}
        path = OUT_DIR / f'{bid}.json'
        path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n', 'utf-8')
        count = sum(len(vs) for vs in ch_data.values())
        total_cits += count
        print(f'  {bid}: {count} verse entries')

    print(f'\nTotal: {len(verse_index)} books, {total_cits} verse entries')

    if skipped:
        unique_skipped = sorted(set(skipped))[:20]
        print(f'\nSkipped refs (unrecognised book, sample):')
        for r in unique_skipped:
            print(f'  {r}')


if __name__ == '__main__':
    main()
