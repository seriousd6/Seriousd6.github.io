#!/usr/bin/env python3
"""
generate-reading-plans.py — Generate reading plan JSON files for data/plans/.

Plans:
  bible-in-a-year   365 days, sequential Gen→Rev
  mcheyne           365 days, 4 streams (M'Cheyne-style)
  nt-90-days        90  days, Matthew→Revelation
  psalms-proverbs   31  days, Psalms + Proverbs
  gospels-30-days   30  days, 4 Gospels

Usage:
  python3 scripts/generate-reading-plans.py
"""

import json, math
from pathlib import Path

ROOT = Path(__file__).parent.parent
BOOKS_JSON = ROOT / 'data' / 'bible' / 'books.json'
OUT_DIR    = ROOT / 'data' / 'plans'

# ── Load book metadata ─────────────────────────────────────────────────────
with open(BOOKS_JSON) as f:
    ALL_BOOKS = json.load(f)

BOOK_CHAPTERS = {b['name']: b['chapters'] for b in ALL_BOOKS}

# Helper: expand a book name into a list of "Book Ch" strings
def chapters_of(book):
    n = BOOK_CHAPTERS[book]
    return [f'{book} {ch}' for ch in range(1, n + 1)]

# Helper: distribute N items across D days (some days get ceil, some floor)
def distribute(items, days):
    n = len(items)
    result = []
    pos = 0
    for d in range(days):
        take = math.ceil((n - pos) / (days - d))
        result.append(items[pos: pos + take])
        pos += take
    return result

# ── Book name helpers ─────────────────────────────────────────────────────
OT_BOOKS = [b['name'] for b in ALL_BOOKS if b['testament'] == 'OT']
NT_BOOKS = [b['name'] for b in ALL_BOOKS if b['testament'] == 'NT']

def all_ch(books):
    """Flatten a list of book names into all their chapters."""
    out = []
    for b in books:
        out.extend(chapters_of(b))
    return out

def partial_ch(book, from_ch, to_ch):
    """Chapters from_ch..to_ch (inclusive, 1-based) of a book."""
    return [f'{book} {ch}' for ch in range(from_ch, to_ch + 1)]

# ── Plan 1: Bible in a Year ────────────────────────────────────────────────
def make_bible_in_a_year():
    all_chapters = all_ch(OT_BOOKS + NT_BOOKS)   # 1189 chapters
    days_list    = distribute(all_chapters, 365)

    plan = {
        'id':          'bible-in-a-year',
        'title':       'Bible in a Year',
        'description': 'Read the entire Bible sequentially — Genesis through Revelation — in 365 days.',
        'total_days':  365,
        'days': [
            {'day': i + 1, 'label': f'Day {i + 1}', 'passages': grp}
            for i, grp in enumerate(days_list)
        ]
    }
    return plan

# ── Plan 2: M'Cheyne 4-stream ─────────────────────────────────────────────
# Stream 1 (365 ch): Gen – 2Kgs + 1Chr 1-27
# Stream 2 (365 ch): 1Chr 28-29 + 2Chr – Isa 51
# Stream 3 (365 ch): Matt – Rev + Psa 1-105
# Stream 4 (365 ch): Isa 52-66 + Jer – Mal + Acts – Jude + Rev 1-17
def make_mcheyne():
    s1 = (all_ch(['Genesis','Exodus','Leviticus','Numbers','Deuteronomy',
                  'Joshua','Judges','Ruth','1 Samuel','2 Samuel',
                  '1 Kings','2 Kings'])              # 338 ch
          + partial_ch('1 Chronicles', 1, 27))        # +27 = 365

    s2 = (partial_ch('1 Chronicles', 28, 29)          # 2
          + all_ch(['2 Chronicles','Ezra','Nehemiah','Esther',
                    'Job','Psalms','Proverbs','Ecclesiastes','Song of Solomon'])  # 36+10+13+10+42+150+31+12+8 = 312
          + partial_ch('Isaiah', 1, 51))               # +51 = 365

    s3 = (all_ch(NT_BOOKS)                             # 260
          + partial_ch('Psalms', 1, 105))               # +105 = 365

    s4 = (partial_ch('Isaiah', 52, 66)                 # 15
          + all_ch(['Jeremiah','Lamentations','Ezekiel','Daniel',
                    'Hosea','Joel','Amos','Obadiah','Jonah',
                    'Micah','Nahum','Habakkuk','Zephaniah',
                    'Haggai','Zechariah','Malachi'])    # 52+5+48+12+67 = 184 → cumsum 199
          + all_ch(['Acts','Romans','1 Corinthians','2 Corinthians',
                    'Galatians','Ephesians','Philippians','Colossians',
                    '1 Thessalonians','2 Thessalonians','1 Timothy',
                    '2 Timothy','Titus','Philemon','Hebrews','James',
                    '1 Peter','2 Peter','1 John','2 John','3 John','Jude'])  # 149 → cumsum 348
          + partial_ch('Revelation', 1, 17))             # +17 = 365

    # Verify
    for idx, s in enumerate([s1, s2, s3, s4], 1):
        assert len(s) == 365, f'Stream {idx} has {len(s)} chapters (expected 365)'

    plan = {
        'id':          'mcheyne',
        'title':       "M'Cheyne One Year Reading Plan",
        'description': ("Read the Old Testament once and the New Testament + Psalms twice in a year. "
                        "Four readings per day drawn from different parts of Scripture."),
        'total_days':  365,
        'days': [
            {'day': i + 1, 'label': f'Day {i + 1}',
             'passages': [s1[i], s2[i], s3[i], s4[i]]}
            for i in range(365)
        ]
    }
    return plan

# ── Plan 3: NT in 90 Days ─────────────────────────────────────────────────
def make_nt_90():
    nt_chapters = all_ch(NT_BOOKS)   # 260 ch
    days_list   = distribute(nt_chapters, 90)

    plan = {
        'id':          'nt-90-days',
        'title':       'New Testament in 90 Days',
        'description': 'Read the entire New Testament — Matthew through Revelation — in 90 days.',
        'total_days':  90,
        'days': [
            {'day': i + 1, 'label': f'Day {i + 1}', 'passages': grp}
            for i, grp in enumerate(days_list)
        ]
    }
    return plan

# ── Plan 4: Psalms & Proverbs in a Month ─────────────────────────────────
def make_psalms_proverbs():
    psa = chapters_of('Psalms')        # 150 ch
    pro = chapters_of('Proverbs')      # 31 ch

    # Spread psalms across 31 days, one proverb per day
    psa_days = distribute(psa, 31)
    days_list = [psa_days[d] + [pro[d]] for d in range(31)]

    plan = {
        'id':          'psalms-proverbs',
        'title':       'Psalms & Proverbs in a Month',
        'description': 'Read all 150 Psalms and all 31 Proverbs in 31 days.',
        'total_days':  31,
        'days': [
            {'day': i + 1, 'label': f'Day {i + 1}', 'passages': days_list[i]}
            for i in range(31)
        ]
    }
    return plan

# ── Plan 5: Gospels in 30 Days ────────────────────────────────────────────
def make_gospels_30():
    gospel_chs = all_ch(['Matthew','Mark','Luke','John'])  # 89 ch
    days_list  = distribute(gospel_chs, 30)

    plan = {
        'id':          'gospels-30-days',
        'title':       'Gospels in 30 Days',
        'description': 'Read all four Gospels — Matthew, Mark, Luke, and John — in 30 days.',
        'total_days':  30,
        'days': [
            {'day': i + 1, 'label': f'Day {i + 1}', 'passages': grp}
            for i, grp in enumerate(days_list)
        ]
    }
    return plan

# ── Write files ────────────────────────────────────────────────────────────
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    plans = [
        make_bible_in_a_year(),
        make_mcheyne(),
        make_nt_90(),
        make_psalms_proverbs(),
        make_gospels_30(),
    ]

    for plan in plans:
        out_path = OUT_DIR / f'{plan["id"]}.json'
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(plan, f, ensure_ascii=False, separators=(',', ':'))
        total_readings = sum(len(d['passages']) for d in plan['days'])
        print(f'  ✓ {plan["id"]}.json — {plan["total_days"]} days, {total_readings} total readings')

if __name__ == '__main__':
    main()
