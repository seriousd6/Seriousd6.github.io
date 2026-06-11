#!/usr/bin/env python3
"""
build-dict-verse-index.py — Build per-book verse-index for Easton's and/or Smith's dictionary.

For Easton: reads refs from the 'refs' field of each data/dictionary/{slug}.json
For Smith:  extracts refs from parenthesized patterns in HTML text (e.g. "(Numbers 26:59; 33:39)")

Writes: data/{source}/verse-index/{bookId}.json
  { "ch": { "v": [{id, term}, ...] } }

Run from repo root:
  python3 scripts/build-dict-verse-index.py              # both sources
  python3 scripts/build-dict-verse-index.py --source easton
  python3 scripts/build-dict-verse-index.py --source smith
"""

import json, re, argparse
from pathlib import Path
from collections import defaultdict
from bs4 import BeautifulSoup

REPO       = Path(__file__).resolve().parent.parent
BOOKS_JSON = REPO / 'data' / 'bible' / 'books.json'

def build_name_map(books_json):
    """Build {normalized_name: book_id} covering full names and abbreviations."""
    books = json.loads(books_json.read_text())
    m = {}
    for b in books:
        bid = b['id']
        m[b['name'].lower()] = bid
        for abbr in b.get('abbrevs', []):
            m[abbr.lower()] = bid
    # Extra aliases used by Smith's dictionary but absent from books.json
    _EXTRA = {
        'song of songs': 'songofsolomon',
        'canticles': 'songofsolomon',
        'canticle of canticles': 'songofsolomon',
        'solomon': 'songofsolomon',   # Smith uses "Solomon 4:8" for Song of Solomon
    }
    m.update(_EXTRA)
    return m

# Regex for parenthesized content that looks like scripture refs
_PAREN_RE = re.compile(r'\(([^)]{3,300})\)')
# A segment starts a new book if it begins with a book-name-like token
_BOOK_START_RE = re.compile(
    r'^([123]?\s*[A-Z][a-zA-Z]+(?:\s+of\s+[A-Z][a-zA-Z]+)?(?:\s+[A-Z][a-zA-Z]+)?)\s+(\d+):(\d+)',
)
# Bare chapter:verse continuation (no book prefix)
_BARE_REF_RE = re.compile(r'^(\d+):(\d+)')


def _normalize(text):
    """Replace non-breaking spaces and normalize whitespace."""
    return text.replace('\xa0', ' ').replace('\ufffd', ' ').strip()


def _parse_segment(segment, current_book, name_map):
    """Parse one semicolon-separated ref segment; returns list of (bookId, ch, v) or []."""
    segment = _normalize(segment)
    results = []

    # Try book-prefixed ref first
    m = _BOOK_START_RE.match(segment)
    if m:
        book_token = _normalize(m.group(1))
        ch = m.group(2)
        v  = m.group(3)
        bid = name_map.get(book_token.lower())
        if bid:
            current_book = bid
            results.append((bid, ch, v))
            # Handle comma-separated extra verses for same ch: e.g. "9:35,36"
            rest = segment[m.end():]
            for extra in re.findall(r',\s*(\d+)', rest):
                results.append((bid, ch, extra))
            return current_book, results

    # Try bare ch:v continuation
    m = _BARE_REF_RE.match(segment)
    if m and current_book:
        ch = m.group(1)
        v  = m.group(2)
        results.append((current_book, ch, v))
        rest = segment[m.end():]
        for extra in re.findall(r',\s*(\d+)', rest):
            results.append((current_book, ch, extra))
        return current_book, results

    return current_book, results


def extract_refs_from_html(html_text, name_map):
    """Extract (bookId, ch, v) tuples from Smith-style HTML with parenthesized refs."""
    plain = BeautifulSoup(html_text, 'html.parser').get_text()
    results = []
    for paren_m in _PAREN_RE.finditer(plain):
        content = _normalize(paren_m.group(1))
        # Skip if no digit:digit pattern (e.g. "B.C. 1573")
        if not re.search(r'\d+:\d+', content):
            continue
        segments = content.split(';')
        current_book = None
        for seg in segments:
            current_book, found = _parse_segment(seg.strip(), current_book, name_map)
            results.extend(found)
    return results


def _add_entry(idx, bid, ch, v, slug, term):
    existing = idx[bid][ch][v]
    if not any(e['id'] == slug for e in existing):
        existing.append({'id': slug, 'term': term})


def build_index(source_dir, out_dir, name_map, source_label):
    """Build verse-index from a dictionary source directory."""
    out_dir.mkdir(parents=True, exist_ok=True)
    idx = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    entries = sorted(source_dir.glob('*.json'))
    processed = 0
    for p in entries:
        if p.name == 'index.json':
            continue
        data = json.loads(p.read_text())
        slug = data.get('id', p.stem)
        term = data.get('term', slug)

        # Try refs field first (Easton has it; Smith does not)
        refs_list = data.get('refs') or []
        if refs_list:
            for ref in refs_list:
                m = re.match(r'^(.+?)\s+(\d+):(\d+)$', ref.strip())
                if not m:
                    continue
                bid = name_map.get(m.group(1).lower())
                if not bid:
                    continue
                _add_entry(idx, bid, m.group(2), m.group(3), slug, term)
        else:
            # Extract from HTML (Smith path)
            html = data.get('html', '')
            if html:
                for bid, ch, v in extract_refs_from_html(html, name_map):
                    _add_entry(idx, bid, ch, v, slug, term)
        processed += 1

    written = 0
    for bid, ch_map in idx.items():
        out = {ch: dict(v_map) for ch, v_map in ch_map.items()}
        out_path = out_dir / f'{bid}.json'
        out_path.write_text(json.dumps(out, ensure_ascii=False, separators=(',', ':')), 'utf-8')
        written += 1

    total_verses = sum(
        sum(len(vs) for vs in ch_map.values())
        for ch_map in idx.values()
    )
    print(f'[{source_label}] {processed} entries → {written} book files, {total_verses} verse entries → {out_dir}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', choices=['easton', 'smith', 'isbe', 'both', 'all'], default='both',
                        help='"both"=easton+smith, "all"=easton+smith+isbe')
    args = parser.parse_args()

    name_map = build_name_map(BOOKS_JSON)

    if args.source in ('easton', 'both', 'all'):
        build_index(
            source_dir=REPO / 'data' / 'dictionary',
            out_dir=REPO / 'data' / 'dictionary' / 'verse-index',
            name_map=name_map,
            source_label='easton',
        )

    if args.source in ('smith', 'both', 'all'):
        build_index(
            source_dir=REPO / 'data' / 'smith',
            out_dir=REPO / 'data' / 'smith' / 'verse-index',
            name_map=name_map,
            source_label='smith',
        )

    if args.source in ('isbe', 'all'):
        build_index(
            source_dir=REPO / 'data' / 'isbe',
            out_dir=REPO / 'data' / 'isbe' / 'verse-index',
            name_map=name_map,
            source_label='isbe',
        )


if __name__ == '__main__':
    main()
