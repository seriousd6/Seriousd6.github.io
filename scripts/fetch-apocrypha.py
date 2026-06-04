#!/usr/bin/env python3
"""
fetch-apocrypha.py — Download full apocryphal Bible versions from public-domain
sources and write them to data/bible-apocrypha/{VERSION}/{bookId}.json.

Each version stores ALL books (canonical 66 + deuterocanonical) in one directory
so the apocrypha reader can serve the complete Catholic / Orthodox / LXX Bible.

Output schema (identical to canonical Bible files):
    { "chapters": { "1": { "1": "verse text…", "2": "…" }, … } }

Supported versions:
    DR      — Douay-Rheims 1899 American edition (wldeh/bible-api; eBible.org fallback)
    WEB-CE  — World English Bible Catholic Edition (eBible.org)
    KJV-APO — KJV with Apocrypha 1611 (eBible.org)
    BRENTON — Brenton's LXX English 1851 (eBible.org)

Usage:
    python3 scripts/fetch-apocrypha.py [VERSION ...]   # specific versions
    python3 scripts/fetch-apocrypha.py                 # all versions
    python3 scripts/fetch-apocrypha.py WEB-CE --force  # re-fetch even if files exist
    python3 scripts/fetch-apocrypha.py WEB-CE --apo-only  # only deuterocanonical books
"""

import json
import os
import re
import sys
import time
import io
import zipfile
import urllib.request
from pathlib import Path

REPO_ROOT   = Path(__file__).resolve().parent.parent
OUT_DIR     = REPO_ROOT / 'data' / 'bible-apocrypha'
APO_BOOKS_JSON  = REPO_ROOT / 'data' / 'apocrypha-books.json'
CANON_BOOKS_JSON = REPO_ROOT / 'data' / 'bible' / 'books.json'

# ── Book lists ────────────────────────────────────────────────────────────────

# Deuterocanonical / apocryphal books only
APO_BOOKS = [
    'tobit', 'judith', '1maccabees', '2maccabees', 'wisdom', 'sirach', 'baruch',
    'additions-esther', 'prayer-of-azariah', 'susanna', 'bel-and-dragon',
    '1esdras', '2esdras', '3maccabees', '4maccabees', 'prayer-of-manasseh', 'psalm151',
]

# All 66 canonical books in order (IDs match data/bible/books.json)
CANON_BOOKS = [
    'genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy',
    'joshua', 'judges', 'ruth', '1samuel', '2samuel',
    '1kings', '2kings', '1chronicles', '2chronicles',
    'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs',
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

ALL_BOOKS = CANON_BOOKS + APO_BOOKS

# ── USFM / OSIS book codes ────────────────────────────────────────────────────

# Maps our book IDs to standard USFM 3-letter codes used in eBible.org filenames
USFM_CODES = {
    # Canonical OT
    'genesis': 'GEN', 'exodus': 'EXO', 'leviticus': 'LEV', 'numbers': 'NUM',
    'deuteronomy': 'DEU', 'joshua': 'JOS', 'judges': 'JDG', 'ruth': 'RUT',
    '1samuel': '1SA', '2samuel': '2SA', '1kings': '1KI', '2kings': '2KI',
    '1chronicles': '1CH', '2chronicles': '2CH', 'ezra': 'EZR', 'nehemiah': 'NEH',
    'esther': 'EST', 'job': 'JOB', 'psalms': 'PSA', 'proverbs': 'PRO',
    'ecclesiastes': 'ECC', 'songofsolomon': 'SNG', 'isaiah': 'ISA',
    'jeremiah': 'JER', 'lamentations': 'LAM', 'ezekiel': 'EZK', 'daniel': 'DAN',
    'hosea': 'HOS', 'joel': 'JOL', 'amos': 'AMO', 'obadiah': 'OBA', 'jonah': 'JON',
    'micah': 'MIC', 'nahum': 'NAM', 'habakkuk': 'HAB', 'zephaniah': 'ZEP',
    'haggai': 'HAG', 'zechariah': 'ZEC', 'malachi': 'MAL',
    # Canonical NT
    'matthew': 'MAT', 'mark': 'MRK', 'luke': 'LUK', 'john': 'JHN', 'acts': 'ACT',
    'romans': 'ROM', '1corinthians': '1CO', '2corinthians': '2CO', 'galatians': 'GAL',
    'ephesians': 'EPH', 'philippians': 'PHP', 'colossians': 'COL',
    '1thessalonians': '1TH', '2thessalonians': '2TH', '1timothy': '1TI',
    '2timothy': '2TI', 'titus': 'TIT', 'philemon': 'PHM', 'hebrews': 'HEB',
    'james': 'JAS', '1peter': '1PE', '2peter': '2PE', '1john': '1JN',
    '2john': '2JN', '3john': '3JN', 'jude': 'JUD', 'revelation': 'REV',
    # Deuterocanonical / apocryphal
    'tobit':              'TOB',
    'judith':             'JDT',
    '1maccabees':         '1MA',
    '2maccabees':         '2MA',
    'wisdom':             'WIS',
    'sirach':             'SIR',
    'baruch':             'BAR',
    'additions-esther':   'ESG',   # Greek Esther additions
    'prayer-of-azariah':  'S3Y',   # Song of the Three Young Men
    'susanna':            'SUS',
    'bel-and-dragon':     'BEL',
    '1esdras':            '1ES',
    '2esdras':            '2ES',
    '3maccabees':         '3MA',
    '4maccabees':         '4MA',
    'prayer-of-manasseh': 'MAN',
    'psalm151':           'PS2',   # Psalm 151
}

# eBible.org USFM zip download URLs (updated 2026-06-03; old _readaloud IDs were renamed)
EBIBLE_URLS = {
    'WEB-CE':  'https://ebible.org/Scriptures/eng-web-c_usfm.zip',
    'KJV-APO': 'https://ebible.org/Scriptures/eng-kjv_usfm.zip',
    'BRENTON': 'https://ebible.org/Scriptures/eng-Brenton_usfm.zip',
    'DR':      'https://ebible.org/Scriptures/engDRA_usfm.zip',
}

# wldeh/bible-api slug for DR (covers canonical books; apocrypha availability varies)
DR_API_BASE = 'https://cdn.jsdelivr.net/gh/wldeh/bible-api@main/bibles/en_drc'

# DR slug overrides for wldeh/bible-api (canonical books that differ from bookId)
DR_SLUG_OVERRIDES = {
    '1samuel': '1-samuel', '2samuel': '2-samuel',
    '1kings': '1-kings', '2kings': '2-kings',
    '1chronicles': '1-chronicles', '2chronicles': '2-chronicles',
    'songofsolomon': 'song-of-solomon',
    '1corinthians': '1-corinthians', '2corinthians': '2-corinthians',
    '1thessalonians': '1-thessalonians', '2thessalonians': '2-thessalonians',
    '1timothy': '1-timothy', '2timothy': '2-timothy',
    '1peter': '1-peter', '2peter': '2-peter',
    '1john': '1-john', '2john': '2-john', '3john': '3-john',
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def fetch_bytes(url, retries=3, delay=2.0):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'bible-study-fetch/1.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except Exception as e:
            if attempt < retries - 1:
                print(f'  Retry {attempt+1}/{retries} for {url}: {e}')
                time.sleep(delay * (attempt + 1))
            else:
                raise RuntimeError(f'Failed to fetch {url}: {e}') from e

def fetch_json(url, retries=3, delay=1.5):
    return json.loads(fetch_bytes(url, retries, delay).decode('utf-8'))

def save_book(version, book_id, chapters):
    out_path = OUT_DIR / version / f'{book_id}.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump({'chapters': chapters}, f, ensure_ascii=False, indent=2)
    total = sum(len(vs) for vs in chapters.values())
    print(f'  ✓ {book_id} ({len(chapters)} ch, {total} v)')

# ── USFM parser ───────────────────────────────────────────────────────────────

_VERSE_RE = re.compile(r'\\v\s+(\d+)\s+(.*?)(?=\\v\s+\d+|\\c\s+\d+|$)', re.DOTALL)
_TAG_RE   = re.compile(r'\\[a-z]+\d*\*?\s*')
_NOTE_RE  = re.compile(r'\\[fx][\s\S]*?\\[fx]\*', re.DOTALL)

def _clean(raw):
    text = _NOTE_RE.sub('', raw)
    text = _TAG_RE.sub('', text)
    return re.sub(r'\s+', ' ', text).strip()

def parse_usfm(content):
    """Parse USFM bytes/str into {ch_str: {v_str: text}} dict."""
    text = content if isinstance(content, str) else content.decode('utf-8', errors='replace')
    chapters = {}
    for m in re.finditer(r'\\c\s+(\d+)(.*?)(?=\\c\s+\d+|$)', text, re.DOTALL):
        ch, body = m.group(1), m.group(2)
        verses = {vm.group(1): _clean(vm.group(2)) for vm in _VERSE_RE.finditer(body)
                  if _clean(vm.group(2))}
        if verses:
            chapters[ch] = verses
    return chapters

# ── eBible zip fetcher ────────────────────────────────────────────────────────

_EBIBLE_CACHE = {}   # version → ZipFile object

def _get_zip(version):
    if version not in _EBIBLE_CACHE:
        url = EBIBLE_URLS[version]
        print(f'  Downloading {version} archive from eBible.org …')
        _EBIBLE_CACHE[version] = zipfile.ZipFile(io.BytesIO(fetch_bytes(url)))
    return _EBIBLE_CACHE[version]

def fetch_ebible_book(version, book_id):
    """Locate and parse one book from an eBible.org USFM zip."""
    zf   = _get_zip(version)
    code = USFM_CODES.get(book_id, '').upper()
    names = zf.namelist()

    # Strategy 1: match by USFM code anywhere in filename
    hits = [n for n in names if code and code in n.upper() and n.endswith(('.usfm', '.txt', '.SFM', '.sfm'))]
    # Strategy 2: match by book-id substring (lowercased)
    if not hits:
        hits = [n for n in names if book_id.replace('-', '').lower() in n.lower()
                and n.endswith(('.usfm', '.txt', '.SFM', '.sfm'))]

    # Strategy 3: psalm151 is embedded in the Psalms file as chapter 151 in LXX-based versions
    if not hits and book_id == 'psalm151':
        psa_hits = [n for n in names if 'PSA' in n.upper() and n.endswith(('.usfm', '.txt', '.SFM', '.sfm'))]
        if psa_hits:
            psa_hits.sort(key=len)
            all_chs = parse_usfm(zf.read(psa_hits[0]))
            if '151' in all_chs:
                return {'1': all_chs['151']}
        return None

    # Strategy 4: Catholic/LXX Bibles use ESG (Greek Esther) and DAG (Greek Daniel)
    #   instead of EST/DAN. Fall back to these extended codes for Catholic editions.
    FALLBACK_CODES = {'esther': 'ESG', 'daniel': 'DAG'}
    if not hits and book_id in FALLBACK_CODES:
        alt_code = FALLBACK_CODES[book_id]
        hits = [n for n in names if alt_code in n.upper() and n.endswith(('.usfm', '.txt', '.SFM', '.sfm'))]

    if not hits:
        return None

    # Prefer the shortest name (avoids appendix/intro files)
    hits.sort(key=len)
    chapters = parse_usfm(zf.read(hits[0]))
    return chapters if chapters else None

# ── DR fetcher (wldeh/bible-api CDN) ─────────────────────────────────────────

def _dr_slug(book_id):
    return DR_SLUG_OVERRIDES.get(book_id, book_id)

def fetch_dr_book(book_id):
    """Fetch one book from the wldeh/bible-api DR endpoint."""
    slug = _dr_slug(book_id)
    url  = f'{DR_API_BASE}/books/{slug}.json'
    try:
        raw = fetch_json(url)
    except RuntimeError:
        # Apocryphal books may not be in this CDN — try eBible fallback
        return None

    if isinstance(raw, dict) and 'chapters' in raw:
        out = {}
        for ch, ch_data in raw['chapters'].items():
            verses = ch_data.get('verses', ch_data)
            if isinstance(verses, dict):
                out[str(ch)] = {str(v): str(t) for v, t in verses.items()}
        return out or None

    if isinstance(raw, dict) and all(isinstance(v, dict) for v in raw.values()):
        return {str(ch): {str(v): str(t) for v, t in vs.items()} for ch, vs in raw.items()} or None

    return None

# ── Main ──────────────────────────────────────────────────────────────────────

SUPPORTED = {'DR', 'WEB-CE', 'KJV-APO', 'BRENTON'}

def run(versions, force=False, apo_only=False):
    book_list = APO_BOOKS if apo_only else ALL_BOOKS
    kind = 'deuterocanonical only' if apo_only else f'full Bible ({len(book_list)} books)'

    for version in versions:
        if version not in SUPPORTED:
            print(f'Unknown version: {version}. Supported: {sorted(SUPPORTED)}')
            continue

        print(f'\n=== {version} — {kind} ===')
        fetched = skipped = failed = 0

        for book_id in book_list:
            out_path = OUT_DIR / version / f'{book_id}.json'
            if out_path.exists() and not force:
                skipped += 1
                continue

            print(f'  {book_id}…', end=' ', flush=True)
            try:
                # All versions now use eBible.org USFM zips (DR CDN deprecated 2026-06-03)
                chapters = fetch_ebible_book(version, book_id)

                if chapters:
                    save_book(version, book_id, chapters)
                    fetched += 1
                else:
                    print('  (not in this version — skipped)')
                    failed += 1
            except Exception as e:
                print(f'  ERROR: {e}')
                failed += 1

        print(f'\n  {version}: {fetched} fetched, {skipped} already present, {failed} unavailable')

if __name__ == '__main__':
    args     = [a for a in sys.argv[1:] if not a.startswith('-')]
    force    = '--force'    in sys.argv
    apo_only = '--apo-only' in sys.argv
    versions = [a.upper() for a in args if a.upper() in SUPPORTED] or sorted(SUPPORTED)
    run(versions, force=force, apo_only=apo_only)
