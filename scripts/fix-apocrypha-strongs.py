#!/usr/bin/env python3
"""fix-apocrypha-strongs.py

Strips Strong's interlinear markup from canonical book files in the three
apocrypha version directories that were fetched with annotations embedded:
  data/bible-apocrypha/DR/
  data/bible-apocrypha/KJV-APO/
  data/bible-apocrypha/WEB-CE/

Contamination pattern: words joined with |strong="H0430" tokens, e.g.
  "In|strong="H0430"the|strong="H0853"beginning..."
Each token is replaced with a space, then multi-space runs are collapsed.

Safe to run multiple times — files with no contamination are left unchanged.
Spot-check after running:
  DR/genesis.json ch 1 v 1 → "In the beginning God created heaven, and earth."
  KJV-APO/genesis.json ch 1 v 1 → "In the beginning God created the heaven..."
  WEB-CE/genesis.json ch 1 v 1 → "In the beginning God created the heavens..."
"""

import json
import os
import re

APOCRYPHA_ROOT = os.path.join(
    os.path.dirname(__file__), '..', 'data', 'bible-apocrypha'
)
TARGET_DIRS = ['DR', 'KJV-APO', 'WEB-CE']

# Matches a Strong's annotation token: pipe + strong= attribute
STRONGS_RE = re.compile(r'\|strong="[HG]\d+"')


def strip_strongs(text):
    """Replace each |strong="..." token with a space, then collapse whitespace."""
    if not isinstance(text, str) or '|strong=' not in text:
        return text
    cleaned = STRONGS_RE.sub(' ', text)
    # Collapse multiple spaces, strip edges
    cleaned = re.sub(r'  +', ' ', cleaned).strip()
    # Remove space inserted before punctuation (e.g. "earth ." → "earth.")
    cleaned = re.sub(r' ([.,;:!?])', r'\1', cleaned)
    return cleaned


def fix_chapter_dict(chapters):
    """Walk {ch: {v: text}} and strip markup in-place. Returns (changed, total)."""
    changed = 0
    total = 0
    for ch_key, verses in chapters.items():
        if not isinstance(verses, dict):
            continue
        for v_key, text in verses.items():
            total += 1
            fixed = strip_strongs(text)
            if fixed != text:
                verses[v_key] = fixed
                changed += 1
    return changed, total


def fix_file(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    # All three target directories use {"chapters": {ch: {v: text}}} structure
    if 'chapters' in data and isinstance(data['chapters'], dict):
        chapters = data['chapters']
    elif isinstance(data, dict):
        # Flat fallback: {ch: {v: text}} directly at root
        chapters = data
    else:
        print(f'  SKIP (unexpected structure): {path}')
        return 0, 0

    changed, total = fix_chapter_dict(chapters)
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
    return changed, total


def main():
    grand_changed = 0
    grand_total = 0
    for dirname in TARGET_DIRS:
        dirpath = os.path.join(APOCRYPHA_ROOT, dirname)
        if not os.path.isdir(dirpath):
            print(f'Directory not found: {dirpath}')
            continue
        files = sorted(f for f in os.listdir(dirpath) if f.endswith('.json'))
        dir_changed = 0
        dir_total = 0
        for fname in files:
            fpath = os.path.join(dirpath, fname)
            changed, total = fix_file(fpath)
            dir_changed += changed
            dir_total += total
            if changed:
                print(f'  {dirname}/{fname}: {changed}/{total} verses fixed')
        print(f'{dirname}: {dir_changed} of {dir_total} verses cleaned')
        grand_changed += dir_changed
        grand_total += dir_total
    print(f'\nTotal: {grand_changed} of {grand_total} verses cleaned across all three versions.')
    if grand_changed == 0:
        print('No contamination found — files are already clean.')


if __name__ == '__main__':
    main()
