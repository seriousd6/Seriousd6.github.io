#!/usr/bin/env python3
"""
generate-chronological-plan.py — Generate Bible-in-a-Year Chronological plan.

Reads the entire Bible in roughly historical sequence rather than canonical order.
Output: data/plans/bible-in-a-year-chronological.json

Usage:
  python3 scripts/generate-chronological-plan.py
"""

import json, math
from pathlib import Path

ROOT       = Path(__file__).parent.parent
BOOKS_JSON = ROOT / 'data' / 'bible' / 'books.json'
OUT_DIR    = ROOT / 'data' / 'plans'

with open(BOOKS_JSON) as f:
    ALL_BOOKS = json.load(f)

BOOK_CHAPTERS = {b['name']: b['chapters'] for b in ALL_BOOKS}
NAME_BY_ID    = {b['id']: b['name'] for b in ALL_BOOKS}

def chapters_of(name):
    n = BOOK_CHAPTERS[name]
    return [f'{name} {ch}' for ch in range(1, n + 1)]

def partial_ch(name, from_ch, to_ch):
    return [f'{name} {ch}' for ch in range(from_ch, to_ch + 1)]

def all_ch(*names):
    out = []
    for n in names:
        out.extend(chapters_of(n))
    return out

def distribute(items, days):
    n, result, pos = len(items), [], 0
    for d in range(days):
        take = math.ceil((n - pos) / (days - d))
        result.append(items[pos: pos + take])
        pos += take
    return result

# ── Chronological chapter sequence ────────────────────────────────────────────
CHRON = (
    # Primeval history
    partial_ch('Genesis', 1, 11) +

    # Patriarchal era — Job is set in this period
    chapters_of('Job') +
    partial_ch('Genesis', 12, 50) +

    # Exodus and the Law
    all_ch('Exodus', 'Leviticus', 'Numbers', 'Deuteronomy') +

    # Conquest and Settlement
    all_ch('Joshua', 'Judges', 'Ruth') +

    # United Kingdom
    all_ch('1 Samuel', '2 Samuel') +

    # Psalms (bulk composed during David/Solomon era)
    chapters_of('Psalms') +

    # Solomon's wisdom writings
    partial_ch('1 Kings', 1, 11) +
    all_ch('Proverbs', 'Ecclesiastes', 'Song of Solomon') +

    # Divided Kingdom
    partial_ch('1 Kings', 12, 22) +
    chapters_of('2 Kings') +

    # Chronicles (retrospective history)
    all_ch('1 Chronicles', '2 Chronicles') +

    # 8th-century prophets (Assyrian period)
    all_ch('Amos', 'Hosea', 'Jonah', 'Isaiah', 'Micah', 'Joel') +

    # 7th-century prophets (Babylonian threat / Judah's last days)
    all_ch('Nahum', 'Habakkuk', 'Zephaniah', 'Jeremiah', 'Lamentations') +
    chapters_of('Obadiah') +

    # Exile in Babylon
    all_ch('Ezekiel', 'Daniel') +

    # Return from exile
    all_ch('Ezra', 'Haggai', 'Zechariah', 'Nehemiah', 'Esther') +
    chapters_of('Malachi') +

    # NT — Gospels
    all_ch('Matthew', 'Mark', 'Luke', 'John') +

    # Acts and early church
    chapters_of('Acts') +

    # Epistles in rough chronological order
    chapters_of('James') +
    chapters_of('Galatians') +
    all_ch('1 Thessalonians', '2 Thessalonians') +
    all_ch('1 Corinthians', '2 Corinthians') +
    chapters_of('Romans') +
    all_ch('Philippians', 'Philemon', 'Colossians', 'Ephesians') +
    all_ch('1 Timothy', 'Titus', '2 Timothy') +
    chapters_of('Hebrews') +
    all_ch('1 Peter', '2 Peter') +
    all_ch('1 John', '2 John', '3 John', 'Jude') +
    chapters_of('Revelation')
)

assert len(CHRON) == 1189, f'Expected 1189 chapters, got {len(CHRON)}'

days_list = distribute(CHRON, 365)

plan = {
    'id':          'bible-in-a-year-chronological',
    'title':       'Bible in a Year — Chronological',
    'description': 'Read the entire Bible in roughly historical order — from Creation through Revelation — in 365 days.',
    'total_days':  365,
    'days': [
        {'day': i + 1, 'label': f'Day {i + 1}', 'passages': days_list[i]}
        for i in range(365)
    ]
}

OUT_DIR.mkdir(parents=True, exist_ok=True)
out_path = OUT_DIR / 'bible-in-a-year-chronological.json'
with open(out_path, 'w') as f:
    json.dump(plan, f, separators=(',', ':'))

print(f'Written {out_path}')
print(f'  Total chapters: {len(CHRON)}')
print(f'  Days: {len(plan["days"])}')
print(f'  Day 1 sample: {plan["days"][0]["passages"]}')
print(f'  Day 146 sample: {plan["days"][145]["passages"]}')
