#!/usr/bin/env python3
"""
scripts/translate-bible.py — Draft-translate the Bible from interlinear data.

Reads:
  data/translation/glossary-greek.json / glossary-hebrew.json
  data/interlinear/{book}.json

Writes:
  data/translation/draft/{tier}/{book}.json
  Shape: {"1": {"1": "In the beginning God created..."}}

Usage:
  python3 scripts/translate-bible.py                  # all tiers, all books, use-draft
  python3 scripts/translate-bible.py --tier mediating
  python3 scripts/translate-bible.py --testament nt
  python3 scripts/translate-bible.py --book john
  python3 scripts/translate-bible.py --confirmed-only  # only confirmed/override/locked
"""

import json
import os
import re
import argparse
from pathlib import Path

ROOT      = Path(__file__).parent.parent
INTER_DIR = ROOT / 'data' / 'interlinear'
GLOSS_DIR = ROOT / 'data' / 'translation'
OUT_DIR   = ROOT / 'data' / 'translation' / 'draft'

CONFIRMED_STATUSES = {'confirmed', 'override', 'locked'}
ALL_TIERS = ('literal', 'mediating', 'thought')

NT_BOOKS = [
    'matthew','mark','luke','john','acts',
    'romans','1corinthians','2corinthians','galatians','ephesians',
    'philippians','colossians','1thessalonians','2thessalonians',
    '1timothy','2timothy','titus','philemon','hebrews',
    'james','1peter','2peter','1john','2john','3john','jude','revelation',
]
OT_BOOKS = [
    'genesis','exodus','leviticus','numbers','deuteronomy',
    'joshua','judges','ruth','1samuel','2samuel',
    '1kings','2kings','1chronicles','2chronicles',
    'ezra','nehemiah','esther','job','psalms','proverbs',
    'ecclesiastes','songofsolomon','isaiah','jeremiah','lamentations',
    'ezekiel','daniel','hosea','joel','amos','obadiah',
    'jonah','micah','nahum','habakkuk','zephaniah','haggai',
    'zechariah','malachi',
]
ALL_BOOKS = NT_BOOKS + OT_BOOKS

# ── Glossary loading ──────────────────────────────────────────────────────────

def load_glossary(confirmed_only=False):
    """Return dict mapping Strong's code → entry."""
    out = {}
    for lang in ('greek', 'hebrew'):
        path = GLOSS_DIR / f'glossary-{lang}.json'
        if not path.exists():
            print(f'  Warning: {path} not found')
            continue
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        accepted = 0
        for code, entry in data.items():
            status = entry.get('status', 'draft')
            if confirmed_only and status not in CONFIRMED_STATUSES:
                continue
            out[code] = entry
            accepted += 1
        mode = 'confirmed' if confirmed_only else 'all'
        print(f'  {lang}: {accepted} entries loaded ({mode})')
    return out

# ── Context override matching ─────────────────────────────────────────────────

def apply_context_overrides(entry, surrounding_codes, tier):
    """Check context_overrides for a matching condition; return override rendering or None."""
    overrides = entry.get('context_overrides') or []
    for ov in overrides:
        condition = (ov.get('condition') or '').lower()
        # Simple keyword matching on surrounding Strong's codes and condition text
        for code in surrounding_codes:
            if code.lower() in condition:
                rendering = ov.get(tier) or ov.get('mediating') or ''
                if rendering:
                    return rendering
    return None

# ── Token rendering ───────────────────────────────────────────────────────────

def render_token(token, glossary, tier, surrounding_codes=None, use_interlinear_fallback=True, book=None):
    """Map one interlinear token to its tier rendering.

    Resolution order (4-level hierarchy):
      1. context_overrides — passage/construction-level (most specific)
      2. book_defaults[book] — per-book/author-level default
      3. tiers.{tier}.primary — global default rendering tendency
      4. interlinear source text — last-resort fallback
    """
    code     = token.get('s', '')
    src_text = token.get('text', '')   # interlinear's existing English

    if not code:
        return src_text

    entry = glossary.get(code)

    if entry is None:
        # No entry in loaded glossary at all
        return src_text if use_interlinear_fallback else f'[{code}?]'

    # 1. Context overrides (passage/construction-level)
    if surrounding_codes:
        override = apply_context_overrides(entry, surrounding_codes, tier)
        if override:
            return override

    # 2. Per-book default (author/genre-level)
    if book:
        book_defaults = entry.get('book_defaults') or {}
        bd = book_defaults.get(book) or {}
        bd_rendering = (bd.get(tier) or bd.get('mediating') or '').strip()
        if bd_rendering:
            return bd_rendering

    # 3. Global default rendering tendency
    tiers     = entry.get('tiers') or {}
    tier_data = tiers.get(tier) or tiers.get('mediating') or {}
    primary   = (tier_data.get('primary') or '').strip()

    if primary:
        return primary

    # 4. Fall back to interlinear text rather than a gap marker
    return src_text if use_interlinear_fallback else f'[{code}?]'

# ── Verse assembly ────────────────────────────────────────────────────────────

_WS_RE   = re.compile(r'  +')
_PUNC_RE = re.compile(r' ([.,;:!?\)])')
_OPEN_RE = re.compile(r'([\(]) ')
_GAP_RE  = re.compile(r'\[[GH]\d+\?\]')

def assemble_verse(tokens, glossary, tier, use_interlinear_fallback=True, book=None):
    """Assemble interlinear tokens into a draft verse string."""
    codes = [t.get('s', '') for t in tokens if t.get('s', '')]
    words = []

    for i, tok in enumerate(tokens):
        surrounding = codes[max(0, i-2):i] + codes[i+1:i+3]
        word = render_token(tok, glossary, tier, surrounding, use_interlinear_fallback, book=book)
        if word:
            words.append(word)

    text = ' '.join(words)
    text = _WS_RE.sub(' ', text)
    text = _PUNC_RE.sub(r'\1', text)
    text = _OPEN_RE.sub(r'\1', text)
    text = text.strip()

    if text and text[0].islower():
        text = text[0].upper() + text[1:]

    return text

# ── Book translation ──────────────────────────────────────────────────────────

def translate_book(book, glossary, tier, use_interlinear_fallback=True):
    inter_path = INTER_DIR / f'{book}.json'
    if not inter_path.exists():
        return None, 0, 0

    with open(inter_path, encoding='utf-8') as f:
        inter = json.load(f)

    result = {}
    gaps   = 0
    verses = 0

    for ch_str, ch_data in inter.items():
        result[ch_str] = {}
        for v_str, tokens in ch_data.items():
            text = assemble_verse(tokens, glossary, tier, use_interlinear_fallback, book=book)
            result[ch_str][v_str] = text
            if not use_interlinear_fallback:
                gaps += len(_GAP_RE.findall(text))
            verses += 1

    return result, verses, gaps

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tier',           default='all',
                        choices=['all','literal','mediating','thought'])
    parser.add_argument('--testament',      default='all',
                        choices=['all','nt','ot'])
    parser.add_argument('--book',           default=None)
    parser.add_argument('--confirmed-only', action='store_true',
                        help='Only use confirmed/override/locked entries (shows gaps for unreviewed)')
    args = parser.parse_args()

    tiers = ALL_TIERS if args.tier == 'all' else (args.tier,)
    use_interlinear_fallback = not args.confirmed_only

    if args.book:
        books = [args.book.lower()]
    elif args.testament == 'nt':
        books = NT_BOOKS
    elif args.testament == 'ot':
        books = OT_BOOKS
    else:
        books = ALL_BOOKS

    print('Loading glossary…')
    glossary = load_glossary(confirmed_only=args.confirmed_only)

    if not glossary:
        print('No glossary entries found. Run seed-glossary.py first.')
        return

    mode = 'confirmed-only' if args.confirmed_only else 'draft (all entries + interlinear fallback)'
    print(f'  Mode: {mode}')
    print(f'  {len(glossary)} entries available')
    print()

    for tier in tiers:
        tier_dir = OUT_DIR / tier
        tier_dir.mkdir(parents=True, exist_ok=True)

        total_v = 0
        print(f'Tier: {tier}')

        for book in books:
            book_data, verses, gaps = translate_book(
                book, glossary, tier, use_interlinear_fallback
            )
            if book_data is None:
                print(f'  {book:20} — no interlinear data')
                continue

            out_path = tier_dir / f'{book}.json'
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(book_data, f, ensure_ascii=False, separators=(',', ':'))

            total_v += verses
            if args.confirmed_only and gaps > 0:
                print(f'  {book:20} {verses:4}v  {gaps:4} gaps ({gaps/verses*100:.0f}%)')
            else:
                print(f'  {book:20} {verses:4}v')

        print(f'  ── {total_v} total verses\n')

    print(f'Output: data/translation/draft/')

if __name__ == '__main__':
    main()
