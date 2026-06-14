#!/usr/bin/env python3
"""
va_process.py — Verse Auditor processing script.

Wraps bare scripture references in HTML with <a class="ref" data-ref="Book Ch:V"> tags,
making them wire-ready for the site's wireRefLinks() system.

Usage:
    python3 scripts/va_process.py <filepath> [OPTIONS]

Options:
    --book BOOKNAME      Canonical book name for R5/R6/R7 (bare Ch:V, v. N, ch. N)
    --file-type TYPE     Override auto-detection (json_commentary | json_echoes |
                         json_book_study | json_library_doc | html)
    --dry-run            Print stats only; do not write file
    --show-sample N      Print N sample before/after pairs (implies --dry-run for display)

Run from repo root: python3 scripts/va_process.py <filepath> ...
"""

import re
import sys
import json
import hashlib
import pathlib
import argparse
from datetime import datetime, timezone

ROOT = pathlib.Path('.')

# ---------------------------------------------------------------------------
# Book name tables
# ---------------------------------------------------------------------------

CANONICAL_BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
    "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah",
    "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel",
    "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
    "Zephaniah", "Haggai", "Zechariah", "Malachi",
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans",
    "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews",
    "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John",
    "Jude", "Revelation",
]

# Maps abbreviated / alternate forms → canonical names.
# Keys are lowercase. Lookup is case-insensitive.
BOOK_ABBREVS = {
    # OT
    'gen': 'Genesis',
    'exod': 'Exodus', 'exo': 'Exodus',
    'lev': 'Leviticus',
    'num': 'Numbers',
    'deut': 'Deuteronomy', 'dt': 'Deuteronomy',
    'josh': 'Joshua', 'jos': 'Joshua',
    'judg': 'Judges', 'jdg': 'Judges',
    'ruth': 'Ruth',
    '1sam': '1 Samuel', '1sa': '1 Samuel', '1 sam': '1 Samuel', '1 sa': '1 Samuel',
    '2sam': '2 Samuel', '2sa': '2 Samuel', '2 sam': '2 Samuel', '2 sa': '2 Samuel',
    '1kgs': '1 Kings', '1ki': '1 Kings', '1king': '1 Kings', '1kings': '1 Kings',
    '1 kgs': '1 Kings', '1 ki': '1 Kings', '1 king': '1 Kings',
    '2kgs': '2 Kings', '2ki': '2 Kings', '2king': '2 Kings', '2kings': '2 Kings',
    '2 kgs': '2 Kings', '2 ki': '2 Kings', '2 king': '2 Kings',
    '1chr': '1 Chronicles', '1chron': '1 Chronicles', '1ch': '1 Chronicles',
    '1 chr': '1 Chronicles', '1 chron': '1 Chronicles',
    '2chr': '2 Chronicles', '2chron': '2 Chronicles', '2ch': '2 Chronicles',
    '2 chr': '2 Chronicles', '2 chron': '2 Chronicles',
    'ezra': 'Ezra',
    'neh': 'Nehemiah',
    'esth': 'Esther', 'est': 'Esther',
    'job': 'Job',
    'ps': 'Psalms', 'pss': 'Psalms', 'psa': 'Psalms', 'psalm': 'Psalms',
    'prov': 'Proverbs', 'pro': 'Proverbs', 'prv': 'Proverbs',
    'eccl': 'Ecclesiastes', 'eccles': 'Ecclesiastes', 'ecc': 'Ecclesiastes',
    'song': 'Song of Solomon', 'sos': 'Song of Solomon', 'cant': 'Song of Solomon',
    'isa': 'Isaiah',
    'jer': 'Jeremiah',
    'lam': 'Lamentations',
    'ezek': 'Ezekiel', 'eze': 'Ezekiel',
    'dan': 'Daniel',
    'hos': 'Hosea',
    'joel': 'Joel',
    'amos': 'Amos',
    'obad': 'Obadiah', 'ob': 'Obadiah',
    'jon': 'Jonah',
    'mic': 'Micah',
    'nah': 'Nahum',
    'hab': 'Habakkuk',
    'zeph': 'Zephaniah',
    'hag': 'Haggai',
    'zech': 'Zechariah', 'zec': 'Zechariah',
    'mal': 'Malachi',
    # NT
    'matt': 'Matthew', 'mt': 'Matthew',
    'mk': 'Mark', 'mar': 'Mark',
    'lk': 'Luke',
    'jn': 'John', 'jno': 'John',
    'acts': 'Acts',
    'rom': 'Romans',
    '1cor': '1 Corinthians', '1co': '1 Corinthians', '1 cor': '1 Corinthians', '1 co': '1 Corinthians',
    '2cor': '2 Corinthians', '2co': '2 Corinthians', '2 cor': '2 Corinthians', '2 co': '2 Corinthians',
    'gal': 'Galatians',
    'eph': 'Ephesians',
    'phil': 'Philippians', 'php': 'Philippians',
    'col': 'Colossians',
    '1thess': '1 Thessalonians', '1th': '1 Thessalonians', '1thes': '1 Thessalonians',
    '1 thess': '1 Thessalonians', '1 th': '1 Thessalonians', '1 thes': '1 Thessalonians',
    '2thess': '2 Thessalonians', '2th': '2 Thessalonians', '2thes': '2 Thessalonians',
    '2 thess': '2 Thessalonians', '2 th': '2 Thessalonians', '2 thes': '2 Thessalonians',
    '1tim': '1 Timothy', '1ti': '1 Timothy', '1 tim': '1 Timothy', '1 ti': '1 Timothy',
    '2tim': '2 Timothy', '2ti': '2 Timothy', '2 tim': '2 Timothy', '2 ti': '2 Timothy',
    'tit': 'Titus',
    'phlm': 'Philemon', 'phm': 'Philemon', 'philem': 'Philemon',
    'heb': 'Hebrews',
    'jas': 'James', 'jm': 'James',
    '1pet': '1 Peter', '1pe': '1 Peter', '1 pet': '1 Peter', '1 pe': '1 Peter',
    '2pet': '2 Peter', '2pe': '2 Peter', '2 pet': '2 Peter', '2 pe': '2 Peter',
    '1jn': '1 John', '1john': '1 John', '1 jn': '1 John', '1 john': '1 John',
    '2jn': '2 John', '2john': '2 John', '2 jn': '2 John', '2 john': '2 John',
    '3jn': '3 John', '3john': '3 John', '3 jn': '3 John', '3 john': '3 John',
    'jude': 'Jude',
    'rev': 'Revelation', 'apoc': 'Revelation',
}

# Stem (filename without extension, lowercase, no spaces/hyphens) → canonical name.
# Used by process_json_commentary and process_json_echoes to infer book from filename.
STEM_TO_CANONICAL = {
    'genesis': 'Genesis', 'exodus': 'Exodus', 'leviticus': 'Leviticus',
    'numbers': 'Numbers', 'deuteronomy': 'Deuteronomy', 'joshua': 'Joshua',
    'judges': 'Judges', 'ruth': 'Ruth', '1samuel': '1 Samuel', '2samuel': '2 Samuel',
    '1kings': '1 Kings', '2kings': '2 Kings', '1chronicles': '1 Chronicles',
    '2chronicles': '2 Chronicles', 'ezra': 'Ezra', 'nehemiah': 'Nehemiah',
    'esther': 'Esther', 'job': 'Job', 'psalms': 'Psalms', 'proverbs': 'Proverbs',
    'ecclesiastes': 'Ecclesiastes', 'songofsolomon': 'Song of Solomon',
    'isaiah': 'Isaiah', 'jeremiah': 'Jeremiah', 'lamentations': 'Lamentations',
    'ezekiel': 'Ezekiel', 'daniel': 'Daniel', 'hosea': 'Hosea', 'joel': 'Joel',
    'amos': 'Amos', 'obadiah': 'Obadiah', 'jonah': 'Jonah', 'micah': 'Micah',
    'nahum': 'Nahum', 'habakkuk': 'Habakkuk', 'zephaniah': 'Zephaniah',
    'haggai': 'Haggai', 'zechariah': 'Zechariah', 'malachi': 'Malachi',
    'matthew': 'Matthew', 'mark': 'Mark', 'luke': 'Luke', 'john': 'John',
    'acts': 'Acts', 'romans': 'Romans', '1corinthians': '1 Corinthians',
    '2corinthians': '2 Corinthians', 'galatians': 'Galatians', 'ephesians': 'Ephesians',
    'philippians': 'Philippians', 'colossians': 'Colossians',
    '1thessalonians': '1 Thessalonians', '2thessalonians': '2 Thessalonians',
    '1timothy': '1 Timothy', '2timothy': '2 Timothy', 'titus': 'Titus',
    'philemon': 'Philemon', 'hebrews': 'Hebrews', 'james': 'James',
    '1peter': '1 Peter', '2peter': '2 Peter', '1john': '1 John',
    '2john': '2 John', '3john': '3 John', 'jude': 'Jude', 'revelation': 'Revelation',
}


def normalize_book(raw):
    """Return canonical book name for raw text (full name or abbreviation), or None."""
    if not raw:
        return None
    cleaned = raw.strip().rstrip('.')
    # Try exact match first (case-insensitive canonical names)
    for canon in CANONICAL_BOOKS:
        if canon.lower() == cleaned.lower():
            return canon
    # Try abbreviation lookup (lowercase key)
    return BOOK_ABBREVS.get(cleaned.lower())


def stem_to_canonical(stem):
    """Convert a filename stem (e.g. '1corinthians') to canonical book name."""
    return STEM_TO_CANONICAL.get(stem.lower())


# ---------------------------------------------------------------------------
# Regex construction
# ---------------------------------------------------------------------------

def _build_book_re():
    # Build alternation from all canonical names + abbreviations, longest first.
    # Numbered books like "1 Corinthians" must appear before their suffix "Corinthians".
    # The alternation sorts by length descending, so longer patterns win.
    all_strs = (
        sorted(CANONICAL_BOOKS, key=len, reverse=True) +
        sorted(BOOK_ABBREVS.keys(), key=len, reverse=True)
    )
    # De-duplicate while preserving order
    seen = set()
    unique = []
    for s in all_strs:
        key = s.lower()
        if key not in seen:
            seen.add(key)
            unique.append(s)
    alt = '|'.join(re.escape(b) for b in unique)
    return re.compile(
        r'\b(' + alt + r')\.?\s+(\d+):(\d+)(?:-(\d+))?',
        re.IGNORECASE
    )


_FULL_REF_RE = _build_book_re()

# Guard: match already-tagged refs so we never double-wrap them.
_EXISTING_REF_RE = re.compile(r'<a\b[^>]*\bdata-ref\b[^>]*>.*?</a>', re.IGNORECASE | re.DOTALL)

# HTML tag splitter — used to avoid touching tag attribute text.
_TAG_SPLIT_RE = re.compile(r'(<[^>]+>)')

# R5: bare Ch:V — only applied when book_ctx is supplied.
_BARE_REF_RE = re.compile(r'\b(\d+):(\d+)(?:-(\d+))?(?!\s*\w)')  # avoid matching times like "10:30am"

# R6: v. N / vv. N-M — only applied with book_ctx + chapter_ctx.
_VERSE_MENTION_RE = re.compile(r'\bvv?\.\s*(\d+)(?:-(\d+))?')

# R7: chap. N / ch. N — only applied with book_ctx.
_CHAP_MENTION_RE = re.compile(r'\bch(?:ap)?s?\.?\s*(\d+)')


# ---------------------------------------------------------------------------
# Core tagging logic
# ---------------------------------------------------------------------------

def _make_link(book, ch, start_v, end_v=None):
    ref = f'{book} {ch}:{start_v}'
    if end_v:
        ref += f'-{end_v}'
    return f'<a class="ref" data-ref="{ref}">{ref}</a>'


def _tag_text_node(text, book_ctx, chapter_ctx):
    """Apply R1/R2 (and optionally R5/R6/R7) to a plain-text segment (no HTML tags).
    Returns (new_text, count_fixed)."""
    count = 0
    result = text

    # R1/R2: full or abbreviated book name refs
    def replace_full(m):
        nonlocal count
        raw_book = m.group(1)
        ch = m.group(2)
        sv = m.group(3)
        ev = m.group(4)
        canon = normalize_book(raw_book)
        if canon:
            count += 1
            return _make_link(canon, ch, sv, ev)
        return m.group(0)

    result = _FULL_REF_RE.sub(replace_full, result)

    # R5: bare Ch:V (requires book_ctx)
    if book_ctx:
        def replace_bare(m):
            nonlocal count
            ch = m.group(1)
            sv = m.group(2)
            ev = m.group(3)
            # Only match if the preceding char is not a book-name-like word
            # (already handled by _FULL_REF_RE above; this catches genuine bare refs)
            count += 1
            return _make_link(book_ctx, ch, sv, ev)
        # Only apply R5 if there are no full-ref patterns nearby (heuristic: skip if text
        # was already modified by R1/R2 in the same node, to reduce false positives)
        if not _FULL_REF_RE.search(text):
            result = _BARE_REF_RE.sub(replace_bare, result)

    # R6: v. N / vv. N-M (requires book_ctx + chapter_ctx)
    if book_ctx and chapter_ctx:
        def replace_verse(m):
            nonlocal count
            sv = m.group(1)
            ev = m.group(2)
            count += 1
            return _make_link(book_ctx, chapter_ctx, sv, ev)
        result = _VERSE_MENTION_RE.sub(replace_verse, result)

    # R7: chap. N (requires book_ctx)
    if book_ctx:
        def replace_chap(m):
            nonlocal count
            ch = m.group(1)
            count += 1
            return f'<a class="ref" data-ref="{book_ctx} {ch}:1">{book_ctx} {ch}</a>'
        result = _CHAP_MENTION_RE.sub(replace_chap, result)

    return result, count


def tag_refs_in_html(html_str, book_ctx=None, chapter_ctx=None):
    """Wrap bare scripture references in html_str with <a class="ref"> tags.
    Skips content already inside existing data-ref anchors and HTML tag attributes.
    Returns (new_html, count_fixed)."""
    # Split into already-tagged refs vs. everything else
    segments = []
    last_end = 0
    for m in _EXISTING_REF_RE.finditer(html_str):
        segments.append(('text', html_str[last_end:m.start()]))
        segments.append(('tagged', m.group(0)))
        last_end = m.end()
    segments.append(('text', html_str[last_end:]))

    total_fixed = 0
    result_parts = []
    for kind, chunk in segments:
        if kind == 'tagged':
            result_parts.append(chunk)
            continue
        # Split by HTML tags; only process text nodes (not tag attributes)
        tag_parts = _TAG_SPLIT_RE.split(chunk)
        for part in tag_parts:
            if part.startswith('<'):
                result_parts.append(part)
            else:
                fixed, n = _tag_text_node(part, book_ctx, chapter_ctx)
                result_parts.append(fixed)
                total_fixed += n

    return ''.join(result_parts), total_fixed


# ---------------------------------------------------------------------------
# File-type processors
# ---------------------------------------------------------------------------

def md5_of(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def process_json_commentary_chapter_dir(path, book_name, dry_run=False, show_sample=0):
    """Process a per-chapter commentary directory where each {ch}.json is {v: html_str}.
    INTENT: commentary was split from per-book {ch:{v:html}} into per-chapter {v:html} files;
    chapter number comes from the filename stem so R5/R6 bare-ref context stays accurate.
    Returns (refs_found, refs_fixed, samples)."""
    chapter_files = sorted(
        [f for f in path.iterdir() if f.suffix == '.json' and f.stem.isdigit()],
        key=lambda f: int(f.stem)
    )
    total_found = 0
    total_fixed = 0
    samples = []

    for chapter_file in chapter_files:
        chapter_num = chapter_file.stem
        data = json.loads(chapter_file.read_text(encoding='utf-8'))
        changed = False

        for v_key in list(data.keys()):
            original = data[v_key]
            if not isinstance(original, str):
                continue
            tagged, n = tag_refs_in_html(original, book_name, chapter_num)
            if n:
                total_fixed += n
                if len(samples) < show_sample:
                    samples.append((original[:200], tagged[:200]))
                changed = True
            total_found += n + len(_EXISTING_REF_RE.findall(original))
            if not dry_run:
                data[v_key] = tagged

        if not dry_run and changed:
            chapter_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    return total_found, total_fixed, samples


def process_json_commentary(path, book_name, dry_run=False, show_sample=0):
    """Process {ch: {v: html_str}} commentary JSON. Returns (refs_found, refs_fixed, samples)."""
    data = json.loads(path.read_text(encoding='utf-8'))
    total_found = 0
    total_fixed = 0
    samples = []

    for ch_key in data:
        for v_key in data[ch_key]:
            original = data[ch_key][v_key]
            if not isinstance(original, str):
                continue
            tagged, n = tag_refs_in_html(original, book_name, ch_key)
            if n:
                total_fixed += n
                if len(samples) < show_sample:
                    samples.append((original[:200], tagged[:200]))
            # Count all refs (already-tagged + newly-fixed)
            total_found += n + len(_EXISTING_REF_RE.findall(original))
            if not dry_run:
                data[ch_key][v_key] = tagged

    if not dry_run and total_fixed > 0:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    return total_found, total_fixed, samples


def process_json_echoes(path, book_name, dry_run=False, show_sample=0):
    """Process {ch: {v: [echo_objects]}} echoes JSON. Normalizes target + tags note."""
    data = json.loads(path.read_text(encoding='utf-8'))
    total_fixed = 0
    total_found = 0
    samples = []
    changed = False

    for ch_key in data:
        for v_key in data[ch_key]:
            for echo in data[ch_key][v_key]:
                # Normalize target field (abbreviated ref → canonical)
                target = echo.get('target', '')
                if target:
                    m = _FULL_REF_RE.match(target)
                    if m:
                        raw_book = m.group(1)
                        canon = normalize_book(raw_book)
                        if canon and canon != raw_book:
                            new_target = f'{canon} {m.group(2)}:{m.group(3)}'
                            if m.group(4):
                                new_target += f'-{m.group(4)}'
                            if not dry_run:
                                echo['target'] = new_target
                            changed = True
                            total_fixed += 1

                # Tag bare refs in note field
                note = echo.get('note', '')
                if note and isinstance(note, str):
                    tagged_note, n = tag_refs_in_html(note, book_name)
                    total_found += n + len(_EXISTING_REF_RE.findall(note))
                    if n:
                        total_fixed += n
                        if len(samples) < show_sample:
                            samples.append((note[:200], tagged_note[:200]))
                        if not dry_run:
                            echo['note'] = tagged_note
                        changed = True

    if not dry_run and changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    return total_found, total_fixed, samples


def process_json_book_study(path, dry_run=False, show_sample=0):
    """Process book study JSON. Tags bare refs in string fields."""
    data = json.loads(path.read_text(encoding='utf-8'))
    TEXT_FIELDS = ['significance', 'language_notes', 'reception', 'reading_guide',
                   'introduction', 'outline', 'themes', 'historical_context']
    total_fixed = 0
    total_found = 0
    samples = []
    changed = False

    def walk(obj):
        nonlocal total_fixed, total_found, changed
        if isinstance(obj, dict):
            for k in list(obj.keys()):
                v = obj[k]
                if isinstance(v, str) and k in TEXT_FIELDS:
                    tagged, n = tag_refs_in_html(v)
                    total_found += n + len(_EXISTING_REF_RE.findall(v))
                    if n:
                        total_fixed += n
                        if len(samples) < show_sample:
                            samples.append((v[:200], tagged[:200]))
                        if not dry_run:
                            obj[k] = tagged
                        changed = True
                else:
                    walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(data)

    if not dry_run and changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    return total_found, total_fixed, samples


def process_json_library_doc(path, dry_run=False, show_sample=0):
    """Process library doc JSON ({sections: [{html: ...}]}). Tags bare refs in html fields."""
    data = json.loads(path.read_text(encoding='utf-8'))
    total_fixed = 0
    total_found = 0
    samples = []
    changed = False
    HTML_FIELDS = ['html', 'body', 'content', 'text']

    def walk(obj):
        nonlocal total_fixed, total_found, changed
        if isinstance(obj, dict):
            for k in list(obj.keys()):
                v = obj[k]
                if isinstance(v, str) and k in HTML_FIELDS:
                    tagged, n = tag_refs_in_html(v)
                    total_found += n + len(_EXISTING_REF_RE.findall(v))
                    if n:
                        total_fixed += n
                        if len(samples) < show_sample:
                            samples.append((v[:200], tagged[:200]))
                        if not dry_run:
                            obj[k] = tagged
                        changed = True
                else:
                    walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(data)

    if not dry_run and changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    return total_found, total_fixed, samples


def process_html_file(path, book_ctx=None, dry_run=False, show_sample=0):
    """Process an HTML file. Tags bare refs in text nodes."""
    original = path.read_text(encoding='utf-8')
    tagged, n = tag_refs_in_html(original, book_ctx)
    total_found = n + len(_EXISTING_REF_RE.findall(original))
    samples = []
    if n and show_sample:
        # Find a context window around first change
        m = _FULL_REF_RE.search(original)
        if m:
            start = max(0, m.start() - 30)
            samples.append((original[start:start+200], tagged[start:start+200]))

    if not dry_run and n:
        path.write_text(tagged, encoding='utf-8')

    return total_found, n, samples


# ---------------------------------------------------------------------------
# Auto-detect file type
# ---------------------------------------------------------------------------

def detect_file_type(path):
    """Infer file type from path. Returns one of the TYPE constants."""
    p = pathlib.Path(path)
    # Per-chapter commentary directory: commentary/{source}/{book}/
    if p.is_dir():
        parts_str = str(p)
        if 'commentary' in parts_str and any(
            src in parts_str for src in ['mkt-original', 'mkt-context', 'mkt-christ',
                                          'ellicott', 'jfb', 'barnes', 'clarke',
                                          'wesley', 'rwp', 'calvin', 'synthesis']
        ):
            return 'json_commentary_chapter_dir'
        return 'html'
    if p.suffix == '.html':
        return 'html'
    if p.suffix == '.json':
        parts_str = str(p)
        if 'commentary' in parts_str and any(
            src in parts_str for src in ['ellicott', 'jfb', 'barnes', 'clarke',
                                          'wesley', 'rwp', 'calvin', 'synthesis',
                                          'mkt-original', 'mkt-context', 'mkt-christ']
        ):
            return 'json_commentary'
        if 'echoes' in parts_str:
            return 'json_echoes'
        if 'book-study' in parts_str:
            return 'json_book_study'
        if 'library' in parts_str and 'docs' in parts_str:
            return 'json_library_doc'
    return 'html'


def infer_book_from_path(path, file_type):
    """Derive canonical book name from filename stem (or directory name) if applicable."""
    p = pathlib.Path(path)
    if file_type == 'json_commentary_chapter_dir':
        # Book name is the directory itself (e.g., mkt-original/romans → Romans)
        return stem_to_canonical(p.name)
    if file_type in ('json_commentary', 'json_echoes'):
        return stem_to_canonical(p.stem)
    return None


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Tag bare scripture references in a file.')
    parser.add_argument('filepath', help='File to process (relative to repo root)')
    parser.add_argument('--book', help='Canonical book name (for R5/R6/R7 bare refs)')
    parser.add_argument('--file-type', dest='file_type',
                        choices=['json_commentary', 'json_echoes', 'json_book_study',
                                 'json_library_doc', 'html'],
                        help='Override auto-detected file type')
    parser.add_argument('--dry-run', action='store_true', help='Print stats; do not write')
    parser.add_argument('--show-sample', type=int, default=0, metavar='N',
                        help='Print N before/after sample pairs')
    args = parser.parse_args()

    path = pathlib.Path(args.filepath)
    if not path.exists():
        print(f'ERROR: File or directory not found: {path}', file=sys.stderr)
        sys.exit(1)

    file_type = args.file_type or detect_file_type(path)
    book_name = args.book or infer_book_from_path(path, file_type)
    dry_run = args.dry_run or (args.show_sample > 0)

    print(f'File:      {path}')
    print(f'Type:      {file_type}')
    print(f'Book ctx:  {book_name or "(none)"}')
    print(f'Dry run:   {dry_run}')
    print()

    if file_type == 'json_commentary_chapter_dir':
        refs_found, refs_fixed, samples = process_json_commentary_chapter_dir(
            path, book_name, dry_run=dry_run, show_sample=args.show_sample)
    elif file_type == 'json_commentary':
        refs_found, refs_fixed, samples = process_json_commentary(
            path, book_name, dry_run=dry_run, show_sample=args.show_sample)
    elif file_type == 'json_echoes':
        refs_found, refs_fixed, samples = process_json_echoes(
            path, book_name, dry_run=dry_run, show_sample=args.show_sample)
    elif file_type == 'json_book_study':
        refs_found, refs_fixed, samples = process_json_book_study(
            path, dry_run=dry_run, show_sample=args.show_sample)
    elif file_type == 'json_library_doc':
        refs_found, refs_fixed, samples = process_json_library_doc(
            path, dry_run=dry_run, show_sample=args.show_sample)
    else:
        refs_found, refs_fixed, samples = process_html_file(
            path, book_ctx=book_name, dry_run=dry_run, show_sample=args.show_sample)

    print(f'Refs found:  {refs_found}')
    print(f'Refs fixed:  {refs_fixed}')
    if not dry_run:
        print(f'Written:     yes' if refs_fixed > 0 else 'Written:     no (already clean)')

    for i, (before, after) in enumerate(samples, 1):
        print(f'\nSample [{i}/{len(samples)}]:')
        print(f'  BEFORE: {before!r}')
        print(f'  AFTER:  {after!r}')


if __name__ == '__main__':
    main()
