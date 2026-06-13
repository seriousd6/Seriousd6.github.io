#!/usr/bin/env python3
"""Build data/strongs/refs/{code}.json — verse reference lists per Strong's code.

For each Strong's code found in the interlinear data, writes a JSON file
listing all verse references where that code appears, in canonical order.
Used by the Bible reader (?strongs=H7676) to display all occurrences.

Each file:
  code, lemma, translit, gloss, count, refs (capped at MAX_REFS)
"""
import json, os, sys, time
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(path):
    with open(os.path.join(BASE, path)) as f:
        return json.load(f)

print('Loading dictionaries…')
greek_dict  = load('data/strongs/greek.json')
hebrew_dict = load('data/strongs/hebrew.json')
bdb_dict    = load('data/strongs/bdb.json')
thayer_dict = load('data/strongs/thayer.json')

print('Loading book order…')
books_meta = load('data/bible/books.json')
BOOK_ORDER = [b['id'] for b in books_meta]
BOOK_NAMES = {b['id']: b['name'] for b in books_meta}
BOOK_IDX   = {b['id']: i for i, b in enumerate(books_meta)}

interlinear_dir = os.path.join(BASE, 'data/interlinear')
out_dir         = os.path.join(BASE, 'data/strongs/refs')
os.makedirs(out_dir, exist_ok=True)

MAX_REFS = 9999  # effectively uncapped — client-side pagination handles display

# ── Scan all interlinear → collect refs per code ──────────────────────────────

print('Scanning interlinear data…')
t0 = time.time()

# code → list of (book_idx, ch, verse) tuples
code_locs = defaultdict(list)

for fname in sorted(os.listdir(interlinear_dir)):
    if not fname.endswith('.json'):
        continue
    book = fname[:-5]
    if book not in BOOK_IDX:
        continue
    bidx = BOOK_IDX[book]
    bname = BOOK_NAMES[book]

    with open(os.path.join(interlinear_dir, fname)) as f:
        data = json.load(f)

    for ch_str, verses in data.items():
        ch = int(ch_str)
        for v_str, tokens in verses.items():
            v = int(v_str)
            seen = set()
            for tok in tokens:
                code = tok.get('s', '').strip()
                if not code or code in seen:
                    continue
                seen.add(code)
                code_locs[code].append((bidx, ch, v, bname))

print(f'  {len(code_locs)} unique codes ({time.time()-t0:.1f}s)')

# ── Write one file per code ───────────────────────────────────────────────────

def get_meta(code):
    if code.startswith('H'):
        base = hebrew_dict.get(code, {})
        lex  = bdb_dict.get(code, {})
    else:
        base = greek_dict.get(code, {})
        lex  = thayer_dict.get(code, {})
    return {
        'lemma':   lex.get('lemma') or base.get('lemma', ''),
        'translit': lex.get('translit') or base.get('translit', ''),
        'gloss':   base.get('gloss', ''),
    }

def collapse_to_ranges(locs):
    """Collapse consecutive verses within the same chapter into range refs.
    e.g. [(Gen,1,1),(Gen,1,2),(Gen,1,3),(Gen,1,5)] → ['Genesis 1:1-3','Genesis 1:5']
    Adjacent chapters are kept separate so each group renders as its own block.
    """
    if not locs:
        return []
    refs = []
    # Group by (bidx, ch)
    from itertools import groupby
    for (bidx, ch), group in groupby(locs, key=lambda x: (x[0], x[1])):
        bname = None
        verses = []
        for bidx2, ch2, v, bn in group:
            bname = bn
            if v not in verses:
                verses.append(v)
        verses.sort()
        # Find consecutive runs
        run_start = verses[0]
        run_end   = verses[0]
        for v in verses[1:]:
            if v == run_end + 1:
                run_end = v
            else:
                refs.append(bname + ' ' + str(ch) + ':' + str(run_start) +
                            ('' if run_start == run_end else '-' + str(run_end)))
                run_start = run_end = v
        refs.append(bname + ' ' + str(ch) + ':' + str(run_start) +
                    ('' if run_start == run_end else '-' + str(run_end)))
    return refs

print('Writing refs files…')
t1 = time.time()
written = 0

for code, locs in code_locs.items():
    # Sort canonically: book order, then ch, then verse
    locs.sort(key=lambda x: (x[0], x[1], x[2]))

    total = len(locs)
    refs = collapse_to_ranges(locs)
    # Cap at MAX_REFS range-entries (each may cover multiple verses)
    refs = refs[:MAX_REFS]

    meta = get_meta(code)
    out  = {
        'code':    code,
        'lemma':   meta['lemma'],
        'translit': meta['translit'],
        'gloss':   meta['gloss'],
        'count':   total,
        'refs':    refs,
    }

    out_path = os.path.join(out_dir, code.lower() + '.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, separators=(',', ':'), ensure_ascii=False)
    written += 1

print(f'  {written} files written ({time.time()-t1:.1f}s)')
print(f'\nDone → data/strongs/refs/ ({written} codes)')
