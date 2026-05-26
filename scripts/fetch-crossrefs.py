#!/usr/bin/env python3
"""
fetch-crossrefs.py — Download and install cross-reference data (TSK-based).

Primary source: OpenBible.info cross-reference dataset (CC BY 4.0)
  ~500,000 verse-to-verse cross-references with community vote counts,
  derived from the Treasury of Scripture Knowledge plus community additions.

Run from repo root:
  python3 scripts/fetch-crossrefs.py [--force]

Output: data/crossrefs/{bookId}.json
Format: { "chapter": { "verse": [["Book Ch:V", votes], ...] } }
  Each entry is a 2-element array: [display_ref_string, vote_count].
  Refs are sorted by vote count descending (most relevant first).

  Backward compat: old files with plain string arrays still work in bible.js.

Supplementary sources:
  If you have additional cross-reference data in the same TSV format as
  OpenBible (From<TAB>To<TAB>Votes), pass it via --supplement PATH.
  Entries from the supplement are merged and deduplicated.

  Additional public-domain cross-reference data is available at:
    https://github.com/scrollmapper/bible_databases (TSK format)
    https://openbible.info/labs/cross-references/ (same primary source)

Options:
  --min-votes N      Minimum community votes to include a ref (default: 1)
  --force            Re-generate files even if they already exist
  --supplement PATH  Path to a supplementary TSV file to merge
"""

import json
import os
import sys
import io
import urllib.request
import zipfile
import argparse

REPO_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON  = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')
OUT_DIR     = os.path.join(REPO_ROOT, 'data', 'crossrefs')
SOURCE_URL  = 'https://a.openbible.info/data/cross-references.zip'
TSV_NAME    = 'cross_references.txt'

# OpenBible book-code → project bookId  (verified against actual TSV)
BOOK_MAP = {
    'Gen':   'genesis',        'Exod':  'exodus',         'Lev':   'leviticus',
    'Num':   'numbers',        'Deut':  'deuteronomy',    'Josh':  'joshua',
    'Judg':  'judges',         'Ruth':  'ruth',           '1Sam':  '1samuel',
    '2Sam':  '2samuel',        '1Kgs':  '1kings',         '2Kgs':  '2kings',
    '1Chr':  '1chronicles',    '2Chr':  '2chronicles',    'Ezra':  'ezra',
    'Neh':   'nehemiah',       'Esth':  'esther',         'Job':   'job',
    'Ps':    'psalms',         'Prov':  'proverbs',       'Eccl':  'ecclesiastes',
    'Song':  'songofsolomon',  'Isa':   'isaiah',         'Jer':   'jeremiah',
    'Lam':   'lamentations',   'Ezek':  'ezekiel',        'Dan':   'daniel',
    'Hos':   'hosea',          'Joel':  'joel',            'Amos':  'amos',
    'Obad':  'obadiah',        'Jonah': 'jonah',           'Mic':   'micah',
    'Nah':   'nahum',          'Hab':   'habakkuk',        'Zeph':  'zephaniah',
    'Hag':   'haggai',         'Zech':  'zechariah',       'Mal':   'malachi',
    'Matt':  'matthew',        'Mark':  'mark',            'Luke':  'luke',
    'John':  'john',           'Acts':  'acts',            'Rom':   'romans',
    '1Cor':  '1corinthians',   '2Cor':  '2corinthians',   'Gal':   'galatians',
    'Eph':   'ephesians',      'Phil':  'philippians',    'Col':   'colossians',
    '1Thess':'1thessalonians', '2Thess':'2thessalonians', '1Tim':  '1timothy',
    '2Tim':  '2timothy',       'Titus': 'titus',           'Phlm':  'philemon',
    'Heb':   'hebrews',        'Jas':   'james',           '1Pet':  '1peter',
    '2Pet':  '2peter',         '1John': '1john',           '2John': '2john',
    '3John': '3john',          'Jude':  'jude',            'Rev':   'revelation',
}


def parse_ref_str(ref_code, book_names):
    """Convert 'Gen.1.1' or 'John.1.1-John.1.3' → 'Genesis 1:1' / 'John 1:1-3'."""
    # Handle ranges: 'John.1.1-John.1.3'
    end_v = None
    if '-' in ref_code:
        start, end = ref_code.split('-', 1)
        end_parts = end.split('.')
        # Only use end verse if same book+chapter
        if len(end_parts) >= 3:
            end_v = end_parts[2]
        ref_code = start

    parts = ref_code.split('.')
    if len(parts) < 3:
        return None
    book_code, ch, v = parts[0], parts[1], parts[2]
    book_id = BOOK_MAP.get(book_code)
    if not book_id or book_id not in book_names:
        return None
    book_name = book_names[book_id]
    ref = f'{book_name} {ch}:{v}'
    if end_v and end_v != v:
        ref += f'-{end_v}'
    return ref


def main():
    parser = argparse.ArgumentParser(description='Fetch cross-reference data.')
    parser.add_argument('--min-votes', type=int, default=1,
                        help='Minimum community votes to include a ref (default: 1)')
    parser.add_argument('--force', action='store_true',
                        help='Re-generate all files even if they exist')
    parser.add_argument('--supplement', metavar='PATH',
                        help='Path to a supplementary TSV file (same format as OpenBible) to merge')
    args = parser.parse_args()

    with open(BOOKS_JSON) as f:
        books_meta = json.load(f)

    # bookId → canonical name
    book_names = {b['id']: b['name'] for b in books_meta}

    print(f'Fetching cross-reference data from OpenBible.info …')
    try:
        with urllib.request.urlopen(SOURCE_URL, timeout=60) as r:
            zip_bytes = r.read()
    except Exception as e:
        print(f'ERROR: Could not download cross-reference data: {e}')
        sys.exit(1)

    print(f'  Downloaded {len(zip_bytes):,} bytes — parsing …')

    # Parse the TSV from inside the zip
    # Accumulate refs per book: bookId → ch → v → {to_display → best_votes}
    # Keyed by display string so we can merge and deduplicate later.
    xrefs = {}  # bookId → {ch_str → {v_str → {display_str → votes}}}
    total_kept = 0
    total_skipped = 0

    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        with zf.open(TSV_NAME) as tsv_file:
            text = tsv_file.read().decode('utf-8')

    def parse_tsv_lines(lines, source_label=''):
        nonlocal total_kept, total_skipped
        for line in lines:
            line = line.strip()
            if not line or line.startswith('From') or line.startswith('#'):
                continue

            parts = line.split('\t')
            if len(parts) < 3:
                continue

            from_ref_code = parts[0].strip()
            to_ref_code   = parts[1].strip()
            try:
                votes = int(parts[2].strip())
            except ValueError:
                votes = 0

            # Negative votes = community-flagged non-cross-ref; skip those too
            if votes < args.min_votes:
                total_skipped += 1
                continue

            from_parts = from_ref_code.split('.')
            if len(from_parts) < 3:
                total_skipped += 1
                continue
            from_book_code = from_parts[0]
            from_ch        = from_parts[1]
            from_v         = from_parts[2]

            from_book_id = BOOK_MAP.get(from_book_code)
            if not from_book_id:
                total_skipped += 1
                continue

            to_display = parse_ref_str(to_ref_code, book_names)
            if not to_display:
                total_skipped += 1
                continue

            # Merge: keep the highest vote count for each unique (from, to) pair
            book_xrefs = xrefs.setdefault(from_book_id, {})
            ch_xrefs   = book_xrefs.setdefault(from_ch, {})
            v_dict     = ch_xrefs.setdefault(from_v, {})
            if to_display not in v_dict or votes > v_dict[to_display]:
                if to_display not in v_dict:
                    total_kept += 1
                v_dict[to_display] = votes

    parse_tsv_lines(text.splitlines(), source_label='OpenBible')

    # Optional supplementary source (same TSV format)
    if args.supplement:
        try:
            with open(args.supplement, encoding='utf-8') as sf:
                supp_lines = sf.readlines()
            before = total_kept
            parse_tsv_lines(supp_lines, source_label='supplement')
            print(f'  Merged supplement: +{total_kept - before:,} new refs from {args.supplement}')
        except Exception as e:
            print(f'  WARNING: Could not read supplement file: {e}')

    print(f'  Kept {total_kept:,} cross-references (skipped {total_skipped:,} below threshold)')

    # Write one JSON file per book
    os.makedirs(OUT_DIR, exist_ok=True)
    written = skipped = 0

    for book_id, ch_data in sorted(xrefs.items()):
        out_file = os.path.join(OUT_DIR, book_id + '.json')

        if os.path.exists(out_file) and not args.force:
            skipped += 1
            continue

        # Sort chapters and verses numerically; sort each verse's refs by votes desc
        sorted_data = {}
        for ch in sorted(ch_data.keys(), key=lambda x: int(x)):
            sorted_data[ch] = {}
            for v in sorted(ch_data[ch].keys(), key=lambda x: int(x)):
                # ch_data[ch][v] is a dict: display_str → votes
                # Output: [[display_str, votes], ...] sorted by votes descending
                sorted_data[ch][v] = sorted(
                    [[ref_str, votes] for ref_str, votes in ch_data[ch][v].items()],
                    key=lambda x: -x[1]
                )

        with open(out_file, 'w') as f:
            json.dump(sorted_data, f, ensure_ascii=False, separators=(',', ':'))

        total_refs = sum(len(vs) for ch in sorted_data.values() for vs in ch.values())
        print(f'  {book_names.get(book_id, book_id)}: {total_refs} refs')
        written += 1

    # Books in our list that had zero cross-refs (rare) — write empty file
    for meta in books_meta:
        bid = meta['id']
        if bid not in xrefs:
            out_file = os.path.join(OUT_DIR, bid + '.json')
            if not os.path.exists(out_file) or args.force:
                with open(out_file, 'w') as f:
                    json.dump({}, f)
                print(f'  {meta["name"]}: 0 refs (empty file written)')
                written += 1

    print(f'\nDone. Written: {written}  Skipped (exists): {skipped}')
    print(f'Output dir: {OUT_DIR}')


if __name__ == '__main__':
    main()
