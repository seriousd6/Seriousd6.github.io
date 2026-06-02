#!/usr/bin/env python3
"""
scripts/extract-phrases.py — identify recurring multi-token Strong's sequences
as phrase glossary candidates for MKT Phase 4.

Scans all interlinear book files for 2–4 token sequences that:
  - appear at least MIN_FREQ times across the corpus
  - contain at least one content word (non-article, non-conjunction)

Writes candidates to data/translation/phrase-candidates.json for review
in the Translation Workshop (Phase 4 queue).

Usage:
  python3 scripts/extract-phrases.py
  python3 scripts/extract-phrases.py --min-freq 8 --max-len 3
"""

import json
import os
import argparse
from collections import Counter
from pathlib import Path

ROOT      = Path(__file__).parent.parent
INTER_DIR = ROOT / 'data' / 'interlinear'
OUT_DIR   = ROOT / 'data' / 'translation'
STRONGS_G = ROOT / 'data' / 'strongs' / 'greek.json'
STRONGS_H = ROOT / 'data' / 'strongs' / 'hebrew.json'

# Strong's codes that are purely grammatical — phrases consisting only of these
# are not interesting idioms.
FUNCTION_CODES_G = {
    'G3588',  # ὁ — definite article
    'G2532',  # καί — and
    'G1161',  # δέ — but/and
    'G3739',  # ὅς — who/which (relative)
    'G846',   # αὐτός — him/her/it
    'G3756',  # οὐ — not
    'G3361',  # μή — not
    'G1722',  # ἐν — in
    'G1519',  # εἰς — into
    'G1537',  # ἐκ — from/out of
    'G575',   # ἀπό — from
    'G4314',  # πρός — to/toward
    'G1223',  # διά — through/because of
    'G2596',  # κατά — according to
    'G3326',  # μετά — with/after
    'G1909',  # ἐπί — on/upon
    'G5228',  # ὑπέρ — above/for
    'G3754',  # ὅτι — that/because
    'G2443',  # ἵνα — in order that
    'G1487',  # εἰ — if
    'G3767',  # οὖν — therefore
}

FUNCTION_CODES_H = {
    'H853',   # אֵת — direct object marker
    'H3588',  # כִּי — for/because/that
    'H834',   # אֲשֶׁר — who/which/that
    'H430',   # אֱלֹהִים — listed here only to avoid stripping God from phrases
}

ALL_BOOKS = [
    'genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy',
    'joshua', 'judges', 'ruth', '1samuel', '2samuel',
    '1kings', '2kings', '1chronicles', '2chronicles',
    'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs',
    'ecclesiastes', 'songofsolomon', 'isaiah', 'jeremiah', 'lamentations',
    'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah',
    'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai',
    'zechariah', 'malachi',
    'matthew', 'mark', 'luke', 'john', 'acts',
    'romans', '1corinthians', '2corinthians', 'galatians', 'ephesians',
    'philippians', 'colossians', '1thessalonians', '2thessalonians',
    '1timothy', '2timothy', 'titus', 'philemon', 'hebrews',
    'james', '1peter', '2peter', '1john', '2john', '3john', 'jude', 'revelation',
]

def load_glosses():
    """Map code → gloss for display in candidate output."""
    glosses = {}
    for path in (STRONGS_G, STRONGS_H):
        if path.exists():
            with open(path, encoding='utf-8') as f:
                d = json.load(f)
            for code, entry in d.items():
                glosses[code] = entry.get('gloss', '')
    return glosses

def has_content_word(seq, lang):
    """True if the sequence contains at least one non-function-word token."""
    func = FUNCTION_CODES_G if lang == 'greek' else FUNCTION_CODES_H
    return any(c not in func for c in seq)

def scan_corpus(min_len, max_len):
    """Return Counter of (lang, (code, ...)) n-gram tuples."""
    ngrams = Counter()

    for book in ALL_BOOKS:
        path = INTER_DIR / f'{book}.json'
        if not path.exists():
            continue
        with open(path, encoding='utf-8') as f:
            data = json.load(f)

        # Determine language from the first token code prefix
        first_code = ''
        for ch_data in data.values():
            for v_data in ch_data.values():
                if v_data:
                    first_code = v_data[0].get('s', '')
                    break
            if first_code:
                break
        lang = 'greek' if first_code.startswith('G') else 'hebrew'

        for ch_data in data.values():
            for tokens in ch_data.values():
                codes = [t.get('s', '') for t in tokens if t.get('s', '')]
                for n in range(min_len, min(max_len, len(codes)) + 1):
                    for i in range(len(codes) - n + 1):
                        seq = tuple(codes[i:i + n])
                        if has_content_word(seq, lang):
                            ngrams[(lang, seq)] += 1

    return ngrams

def main():
    parser = argparse.ArgumentParser(description='Extract phrase glossary candidates')
    parser.add_argument('--min-freq', type=int, default=5,
                        help='Minimum occurrences to include (default: 5)')
    parser.add_argument('--min-len',  type=int, default=2,
                        help='Minimum tokens in phrase (default: 2)')
    parser.add_argument('--max-len',  type=int, default=4,
                        help='Maximum tokens in phrase (default: 4)')
    args = parser.parse_args()

    print(f'Scanning interlinear corpus for {args.min_len}–{args.max_len}-token phrases '
          f'(min {args.min_freq} occurrences)…')

    glosses = load_glosses()
    ngrams  = scan_corpus(args.min_len, args.max_len)

    candidates = []
    for (lang, seq), freq in ngrams.items():
        if freq < args.min_freq:
            continue
        # Skip sequences that are subsets of longer frequent sequences (basic filter)
        gloss_parts = [glosses.get(c, c) for c in seq]
        candidates.append({
            'language': lang,
            'tokens':   list(seq),
            'freq':     freq,
            'surface_glosses': gloss_parts,
            'literal_form':    ' + '.join(gloss_parts),
            'mediating':       '',   # to be filled in workshop
            'thought':         '',
            'expansion':       '',
            'refs':            [],
            'status':          'candidate',
        })

    # Sort by frequency desc
    candidates.sort(key=lambda x: -x['freq'])

    out_path = OUT_DIR / 'phrase-candidates.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)

    print(f'\nFound {len(candidates)} candidate phrases → {out_path}')
    print('\nTop 20 by frequency:')
    for c in candidates[:20]:
        tokens_str = ' · '.join(c['tokens'])
        print(f"  {c['freq']:4}×  [{c['language'][:2]}]  {tokens_str}  →  {c['literal_form'][:60]}")

    print('\nReview candidates in the Translation Workshop → Phase 4 queue.')
    print('Promote entries to glossary-phrases-{lang}.json after review.')

if __name__ == '__main__':
    main()
