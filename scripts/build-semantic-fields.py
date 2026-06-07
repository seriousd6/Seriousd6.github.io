#!/usr/bin/env python3
"""
SW-I: Build semantic field clustering using PMI (pointwise mutual information).

For each Strong's code X:
  - Collect all (bookId, ch, v) verse locations where X appears
  - For each such verse, collect all other codes present (Y)
  - PMI(X, Y) = log2(P(X,Y) / (P(X) * P(Y)))
    where P(X,Y) = (verses_with_both_X_and_Y) / total_verses
          P(X)   = verses_with_X / total_verses
  - Output top 10 co-occurring codes by PMI for each X

Output:
  data/grammar/semantic-fields-greek.json
  data/grammar/semantic-fields-hebrew.json

Schema: { code: [{ code, pmi, co_count }, ...] }  (list of top neighbors, sorted by pmi desc)

Performance note: With 66 books × ~31k verses avg, the full pairwise matrix is large.
Strategy: accumulate verse-level code sets (frozenset), then build co-occurrence counts
in two passes. Only emit entries for codes appearing in at least 10 verses.
"""

import json, os, math
from collections import defaultdict

def load_interlinear(bookId, base):
    path = os.path.join(base, 'data', 'interlinear', bookId + '.json')
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def iter_verse_code_sets(interlinear):
    """Yield frozenset of Strong's codes for each verse in this book's interlinear data."""
    for ch, verses in interlinear.items():
        for v, tokens in verses.items():
            codes = frozenset(tok['s'] for tok in tokens if tok.get('s'))
            if codes:
                yield codes

def build_pmi(base, books, prefix_filter):
    """Returns { code: [{ code, pmi, co_count }, ...] } for all codes starting with prefix."""
    # Pass 1: collect verse-level code sets for all books
    print(f'  Pass 1: collecting verse code sets...')
    all_verse_sets = []
    for bookId in books:
        inter = load_interlinear(bookId, base)
        for cs in iter_verse_code_sets(inter):
            # Filter to only codes with the right prefix
            filtered = frozenset(c for c in cs if c.startswith(prefix_filter))
            if filtered:
                all_verse_sets.append(filtered)
    total_verses = len(all_verse_sets)
    print(f'  {total_verses} verses with {prefix_filter}* codes')

    # Pass 2: count individual code and pairwise occurrences
    print(f'  Pass 2: counting code frequencies and co-occurrences...')
    code_counts   = defaultdict(int)
    co_counts     = defaultdict(int)   # (codeA, codeB) → count, codeA < codeB always

    for vs in all_verse_sets:
        codes = sorted(vs)
        for c in codes:
            code_counts[c] += 1
        for i in range(len(codes)):
            for j in range(i + 1, len(codes)):
                co_counts[(codes[i], codes[j])] += 1

    # Pass 3: compute PMI for each code, keep top 10 by PMI
    print(f'  Pass 3: computing PMI...')
    MIN_VERSE_COUNT = 10  # ignore codes appearing in fewer than 10 verses
    MIN_CO_COUNT    = 3   # ignore pairs with fewer than 3 co-occurrences

    result = {}
    eligible = [c for c, n in code_counts.items() if n >= MIN_VERSE_COUNT]
    print(f'  {len(eligible)} codes with ≥{MIN_VERSE_COUNT} verse appearances')

    for code in eligible:
        neighbors = []
        px = code_counts[code] / total_verses

        # Collect all co-occurring codes
        for other in eligible:
            if other == code:
                continue
            pair = (min(code, other), max(code, other))
            co = co_counts.get(pair, 0)
            if co < MIN_CO_COUNT:
                continue
            py = code_counts[other] / total_verses
            pxy = co / total_verses
            pmi = math.log2(pxy / (px * py))
            neighbors.append({ 'code': other, 'pmi': round(pmi, 3), 'co_count': co })

        # Sort by PMI, take top 10
        neighbors.sort(key=lambda n: -n['pmi'])
        if neighbors:
            result[code] = neighbors[:10]

    return result

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Greek NT books
    nt_books = ['matthew','mark','luke','john','acts','romans','1corinthians','2corinthians',
                'galatians','ephesians','philippians','colossians','1thessalonians',
                '2thessalonians','1timothy','2timothy','titus','philemon','hebrews',
                'james','1peter','2peter','1john','2john','3john','jude','revelation']

    # Hebrew OT books
    ot_books = ['genesis','exodus','leviticus','numbers','deuteronomy','joshua','judges',
                'ruth','1samuel','2samuel','1kings','2kings','1chronicles','2chronicles',
                'ezra','nehemiah','esther','job','psalms','proverbs','ecclesiastes',
                'songofsolomon','isaiah','jeremiah','lamentations','ezekiel','daniel',
                'hosea','joel','amos','obadiah','jonah','micah','nahum','habakkuk',
                'zephaniah','haggai','zechariah','malachi']

    out_dir = os.path.join(base, 'data', 'grammar')

    for lang, books, prefix in [
        ('greek',  nt_books, 'G'),
        ('hebrew', ot_books, 'H'),
    ]:
        print(f'\nProcessing {lang}...')
        result = build_pmi(base, books, prefix)
        print(f'  {len(result)} codes with PMI neighborhood data')

        out_path = os.path.join(out_dir, f'semantic-fields-{lang}.json')
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False)
        print(f'  → {out_path}')

if __name__ == '__main__':
    main()
