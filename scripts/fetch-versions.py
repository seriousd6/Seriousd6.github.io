#!/usr/bin/env python3
"""
fetch-versions.py — Download public-domain Bible versions from wldeh/bible-api
and reformat them into data/bible/{VERSION}/{bookId}.json matching the existing
shape used by KJV, BSB, WEB, and ASV.

Usage:
    python3 scripts/fetch-versions.py [VERSION ...]

    # Fetch all new versions:
    python3 scripts/fetch-versions.py YLT DBY GNV AKJV WEBBE

    # Fetch a single version:
    python3 scripts/fetch-versions.py YLT

Output shape (same as existing versions):
    data/bible/YLT/genesis.json → { "1": { "1": "In the beginning…", "2": "…" }, "2": { … } }

Source: https://github.com/wldeh/bible-api
  Each book is fetched from:
    https://cdn.jsdelivr.net/gh/wldeh/bible-api@main/bibles/{version}/books/{bookId}/chapters/{ch}/verses.json
  or from the flat single-file endpoint if available.

Notes:
  - All versions listed are public domain with no redistribution restrictions.
  - Each version is ~10–12 MB total across 66 book files.
  - After running, add the new version IDs to sw.js SHELL_URLS if you want
    them in the install-time cache (not recommended — use PRECACHE_BIBLE instead,
    which already reads versions.json dynamically).
"""

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR  = REPO_ROOT / 'data' / 'bible'

# Map our version IDs to the wldeh/bible-api version slugs
VERSION_SLUGS = {
    'YLT':   'en_yl',
    'DBY':   'en_dby',
    'GNV':   'en_gnv',
    'AKJV':  'en_akjv',
    'WEBBE': 'en_webbe',
}

# Canonical book list — must match data/bible/books.json order and IDs
BOOKS = [
    'genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy',
    'joshua', 'judges', 'ruth', '1samuel', '2samuel',
    '1kings', '2kings', '1chronicles', '2chronicles', 'ezra',
    'nehemiah', 'esther', 'job', 'psalms', 'proverbs',
    'ecclesiastes', 'songofsolomon', 'isaiah', 'jeremiah', 'lamentations',
    'ezekiel', 'daniel', 'hosea', 'joel', 'amos',
    'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk',
    'zephaniah', 'haggai', 'zechariah', 'malachi',
    'matthew', 'mark', 'luke', 'john', 'acts',
    'romans', '1corinthians', '2corinthians', 'galatians', 'ephesians',
    'philippians', 'colossians', '1thessalonians', '2thessalonians',
    '1timothy', '2timothy', 'titus', 'philemon', 'hebrews',
    'james', '1peter', '2peter', '1john', '2john', '3john',
    'jude', 'revelation',
]

# wldeh/bible-api uses different slugs for some books — map overrides here
BOOK_SLUG_OVERRIDES = {
    '1samuel':      '1-samuel',
    '2samuel':      '2-samuel',
    '1kings':       '1-kings',
    '2kings':       '2-kings',
    '1chronicles':  '1-chronicles',
    '2chronicles':  '2-chronicles',
    'songofsolomon':'song-of-solomon',
    '1corinthians': '1-corinthians',
    '2corinthians': '2-corinthians',
    '1thessalonians':'1-thessalonians',
    '2thessalonians':'2-thessalonians',
    '1timothy':     '1-timothy',
    '2timothy':     '2-timothy',
    '1peter':       '1-peter',
    '2peter':       '2-peter',
    '1john':        '1-john',
    '2john':        '2-john',
    '3john':        '3-john',
}

BASE_URL = 'https://cdn.jsdelivr.net/gh/wldeh/bible-api@main/bibles'

# ── Helpers ────────────────────────────────────────────────────────────────────

def fetch_json(url, retries=3, delay=1.5):
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                raise RuntimeError(f'Failed to fetch {url}: {e}') from e

def book_slug(book_id):
    return BOOK_SLUG_OVERRIDES.get(book_id, book_id)

# ── Core fetch logic ───────────────────────────────────────────────────────────

def fetch_book(version_slug, book_id):
    """
    Fetch all chapters for a book and return a dict:
        { "1": { "1": "verse text", "2": "…" }, "2": { … } }
    """
    slug   = book_slug(book_id)
    url    = f'{BASE_URL}/{version_slug}/books/{slug}.json'
    try:
        raw = fetch_json(url)
    except RuntimeError:
        # Fallback: try chapter-by-chapter (some versions have split files)
        return fetch_book_by_chapters(version_slug, book_id)

    # wldeh shape: { "1": { "1": "text", … }, … }
    # or          { "chapters": { "1": { "verses": { "1": "text" } } } }
    if isinstance(raw, dict) and 'chapters' in raw:
        out = {}
        for ch, ch_data in raw['chapters'].items():
            verses = ch_data.get('verses', ch_data)
            out[str(ch)] = {str(v): str(text) for v, text in verses.items()}
        return out
    if isinstance(raw, dict) and all(isinstance(v, dict) for v in raw.values()):
        return {str(ch): {str(v): str(text) for v, text in vs.items()} for ch, vs in raw.items()}
    return {}

def fetch_book_by_chapters(version_slug, book_id, max_chapters=150):
    slug = book_slug(book_id)
    out  = {}
    for ch in range(1, max_chapters + 1):
        url = f'{BASE_URL}/{version_slug}/books/{slug}/chapters/{ch}/verses.json'
        try:
            raw = fetch_json(url)
        except RuntimeError:
            break  # no more chapters
        if not raw:
            break
        verses = raw if isinstance(raw, dict) else {}
        if isinstance(raw, dict) and 'verses' in raw:
            verses = raw['verses']
        out[str(ch)] = {str(v): str(text) for v, text in verses.items()}
    return out

# ── Main ───────────────────────────────────────────────────────────────────────

def fetch_version(version_id):
    if version_id not in VERSION_SLUGS:
        print(f'Unknown version: {version_id}. Available: {list(VERSION_SLUGS.keys())}')
        return False

    slug     = VERSION_SLUGS[version_id]
    out_dir  = DATA_DIR / version_id
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f'\nFetching {version_id} ({slug}) → {out_dir}')

    for i, book_id in enumerate(BOOKS, 1):
        out_path = out_dir / f'{book_id}.json'
        if out_path.exists():
            print(f'  [{i:02d}/66] {book_id} — already exists, skipping')
            continue
        print(f'  [{i:02d}/66] {book_id}…', end=' ', flush=True)
        try:
            data = fetch_book(slug, book_id)
            if data:
                with open(out_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
                ch_count = len(data)
                v_count  = sum(len(vs) for vs in data.values())
                print(f'{ch_count} chapters, {v_count} verses')
            else:
                print('WARNING: no data returned')
        except Exception as e:
            print(f'ERROR: {e}')
        time.sleep(0.25)  # polite rate limit

    print(f'{version_id} done.\n')
    return True

def main():
    targets = sys.argv[1:] or list(VERSION_SLUGS.keys())
    for v in targets:
        fetch_version(v.upper())
    print('All done. Run `python3 scripts/serve.py` to test locally.')

if __name__ == '__main__':
    main()
