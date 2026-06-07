#!/usr/bin/env python3
"""
SW-J: Build per-author normalized frequency rates for each Strong's code.

Author groups (by bookId as used in data/interlinear/):
  Paul:   romans, 1corinthians, 2corinthians, galatians, ephesians, philippians,
          colossians, 1thessalonians, 2thessalonians, 1timothy, 2timothy, titus, philemon
  John:   john, 1john, 2john, 3john, revelation
  Luke:   luke, acts
  Matthew: matthew
  Mark:   mark
  Peter:  1peter, 2peter
  Hebrews: hebrews
  James:  james
  Jude:   jude
  OT-Moses: genesis, exodus, leviticus, numbers, deuteronomy
  OT-Historical: joshua, judges, ruth, 1samuel, 2samuel, 1kings, 2kings,
                 1chronicles, 2chronicles, ezra, nehemiah, esther
  OT-Wisdom: job, psalms, proverbs, ecclesiastes, songofsolomon
  OT-Major: isaiah, jeremiah, lamentations, ezekiel, daniel
  OT-Minor: hosea, joel, amos, obadiah, jonah, micah, nahum, habakkuk,
            zephaniah, haggai, zechariah, malachi

Output:
  data/grammar/author-freq-greek.json  — { code: { paul: N, john: N, ... } } where N = per-1000-tokens
  data/grammar/author-freq-hebrew.json — same for OT authors
"""

import json, os, math

BOOK_GROUPS_NT = {
    'Paul':    ['romans','1corinthians','2corinthians','galatians','ephesians','philippians',
                'colossians','1thessalonians','2thessalonians','1timothy','2timothy','titus','philemon'],
    'John':    ['john','1john','2john','3john','revelation'],
    'Luke':    ['luke','acts'],
    'Matthew': ['matthew'],
    'Mark':    ['mark'],
    'Peter':   ['1peter','2peter'],
    'Hebrews': ['hebrews'],
    'James':   ['james'],
    'Jude':    ['jude'],
}

BOOK_GROUPS_OT = {
    'Moses':       ['genesis','exodus','leviticus','numbers','deuteronomy'],
    'Historical':  ['joshua','judges','ruth','1samuel','2samuel','1kings','2kings',
                    '1chronicles','2chronicles','ezra','nehemiah','esther'],
    'Wisdom':      ['job','psalms','proverbs','ecclesiastes','songofsolomon'],
    'Major':       ['isaiah','jeremiah','lamentations','ezekiel','daniel'],
    'Minor':       ['hosea','joel','amos','obadiah','jonah','micah','nahum','habakkuk',
                    'zephaniah','haggai','zechariah','malachi'],
}

def load_interlinear(bookId, base):
    path = os.path.join(base, 'data', 'interlinear', bookId + '.json')
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def is_greek_code(code):
    return code.startswith('G')

def is_hebrew_code(code):
    return code.startswith('H')

def process_groups(groups, base, lang_filter):
    """Returns: (author_totals, author_code_counts)
       author_totals: { author: total_token_count }
       author_code_counts: { code: { author: count } }
    """
    author_totals = { a: 0 for a in groups }
    code_author_counts = {}

    for author, books in groups.items():
        for bookId in books:
            inter = load_interlinear(bookId, base)
            for ch, verses in inter.items():
                for v, tokens in verses.items():
                    for tok in tokens:
                        code = tok.get('s', '')
                        if not code:
                            continue
                        if lang_filter == 'greek' and not is_greek_code(code):
                            continue
                        if lang_filter == 'hebrew' and not is_hebrew_code(code):
                            continue
                        author_totals[author] += 1
                        if code not in code_author_counts:
                            code_author_counts[code] = {}
                        code_author_counts[code][author] = code_author_counts[code].get(author, 0) + 1

    return author_totals, code_author_counts

def build_freq_output(author_totals, code_author_counts, groups):
    """For each code, compute per-1000-token rate per author. Return only codes
    where at least 2 authors have non-zero rates (otherwise not useful for comparison).
    Also mark the peak_author (highest rate).
    """
    result = {}
    for code, counts in code_author_counts.items():
        rates = {}
        for author in groups:
            total = author_totals[author]
            if total == 0:
                continue
            cnt = counts.get(author, 0)
            rate = round((cnt / total) * 1000, 4)
            if rate > 0:
                rates[author] = rate

        if len(rates) < 2:
            continue

        # Peak author (highest rate)
        peak = max(rates, key=lambda a: rates[a])
        result[code] = { 'rates': rates, 'peak': peak }

    return result

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(base, 'data', 'grammar')

    for label, groups, lang in [
        ('greek',  BOOK_GROUPS_NT, 'greek'),
        ('hebrew', BOOK_GROUPS_OT, 'hebrew'),
    ]:
        print(f'Processing {label}…')
        author_totals, code_counts = process_groups(groups, base, lang)
        print(f'  Author totals: { {a: t for a, t in author_totals.items() if t > 0} }')
        print(f'  Unique codes tracked: {len(code_counts)}')

        freq_data = build_freq_output(author_totals, code_counts, groups)
        print(f'  Codes with 2+ authors: {len(freq_data)}')

        out_path = os.path.join(out_dir, f'author-freq-{label}.json')
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(freq_data, f, ensure_ascii=False)
        print(f'  → {out_path}')

if __name__ == '__main__':
    main()
