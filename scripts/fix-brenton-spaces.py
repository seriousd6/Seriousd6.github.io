#!/usr/bin/env python3
"""fix-brenton-spaces.py

Fixes ~399 verse strings in data/bible-apocrypha/BRENTON/ where adjacent words
were concatenated without spaces — e.g. "thatI will return" should be "that I
will return". Root cause: the eBible.org USFM source has inline markers that
the fetch script failed to tokenise correctly, merging adjacent words.

Fix: insert a space between every lowercase→uppercase character boundary using
  re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
This is low false-positive risk in Biblical text (no camelCase proper nouns).

Known limitation: all-lowercase fusions (e.g. "menmay") are not caught by this
pattern and require a re-fetch of the BRENTON source (see DATA-7 preferred fix).

Safe to run multiple times — files with no fused words are left unchanged.
Spot-check after running:
  BRENTON/jeremiah.json ch 12 v 15 → "...that I will return..." (space before I)
  BRENTON/jeremiah.json ch 18 v 7  → "If I shall pronounce..." (space after If)
"""

import json
import os
import re

BRENTON_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'data', 'bible-apocrypha', 'BRENTON'
)

# Insert space between lowercase→uppercase letter boundary
FUSED_RE = re.compile(r'([a-z])([A-Z])')


def fix_spaces(text):
    """Insert spaces at lowercase→uppercase word boundaries."""
    if not isinstance(text, str) or not FUSED_RE.search(text):
        return text
    return FUSED_RE.sub(r'\1 \2', text)


def fix_chapter_dict(chapters):
    """Walk {ch: {v: text}} and fix fused words in-place. Returns (changed, total)."""
    changed = 0
    total = 0
    for ch_key, verses in chapters.items():
        if not isinstance(verses, dict):
            continue
        for v_key, text in verses.items():
            total += 1
            fixed = fix_spaces(text)
            if fixed != text:
                verses[v_key] = fixed
                changed += 1
    return changed, total


def fix_file(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    if 'chapters' in data and isinstance(data['chapters'], dict):
        chapters = data['chapters']
    elif isinstance(data, dict):
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
    if not os.path.isdir(BRENTON_DIR):
        print(f'Directory not found: {BRENTON_DIR}')
        return

    files = sorted(f for f in os.listdir(BRENTON_DIR) if f.endswith('.json'))
    total_changed = 0
    total_verses = 0

    for fname in files:
        fpath = os.path.join(BRENTON_DIR, fname)
        changed, total = fix_file(fpath)
        total_changed += changed
        total_verses += total
        if changed:
            print(f'  {fname}: {changed}/{total} verses fixed')

    print(f'\nTotal: {total_changed} of {total_verses} verses fixed in BRENTON.')
    if total_changed == 0:
        print('No fused words found — files are already clean.')
    else:
        # Recount remaining fused-word verses to confirm fix
        remaining = 0
        for fname in files:
            with open(os.path.join(BRENTON_DIR, fname), encoding='utf-8') as f:
                data = json.load(f)
            chs = data.get('chapters', data)
            for ch in chs.values():
                for txt in ch.values():
                    if FUSED_RE.search(str(txt)):
                        remaining += 1
        print(f'Fused-word verses remaining after fix: {remaining}')


if __name__ == '__main__':
    main()
