#!/usr/bin/env python3
"""extract-daniel-additions.py

DR and WEB-CE store the Daniel/Esther additions embedded in their canonical
daniel.json and esther.json files (Catholic tradition: ch 13 = Susanna,
ch 14 = Bel and the Dragon, ch 3 extended = Prayer of Azariah).

The apocrypha reader expects standalone files:
  {version}/susanna.json          — { "chapters": { "1": { v: text, … } } }
  {version}/bel-and-dragon.json   — { "chapters": { "1": { … } } }
  {version}/prayer-of-azariah.json — { "chapters": { "1": { … } } }
  DR/additions-esther.json        — extracted from DR esther ch 11-16 → ch 1-6

This script extracts those chapters and writes the standalone files.
"""

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
APO_DIR   = REPO_ROOT / 'data' / 'bible-apocrypha'

# INTENT: Standard Catholic Daniel ch 3 has 100 verses (DR) / 97 verses (WEB-CE).
# Verses 1-23 are the canonical MT text; verses 24 onward are the Prayer of Azariah
# and Song of the Three Young Men — i.e., the deuterocanonical addition.
# We extract v24+ as the standalone prayer-of-azariah.json.
PRAYER_OF_AZARIAH_START = 24  # first verse of the addition in Daniel 3


def save_book(path: Path, chapters: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'chapters': chapters}, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')


def load_book(path: Path) -> dict:
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    return d.get('chapters', d)


def extract_daniel_additions(version: str) -> int:
    daniel_path = APO_DIR / version / 'daniel.json'
    if not daniel_path.exists():
        print(f'  {version}/daniel.json not found — skipping')
        return 0

    chs = load_book(daniel_path)
    written = 0

    # Susanna = Daniel chapter 13 → standalone chapter 1
    if '13' in chs:
        out = APO_DIR / version / 'susanna.json'
        if not out.exists():
            save_book(out, {'1': chs['13']})
            print(f'  {version}/susanna.json — wrote chapter 1 ({len(chs["13"])} verses from Daniel 13)')
            written += 1
        else:
            print(f'  {version}/susanna.json already exists — skipped')
    else:
        print(f'  {version}: Daniel has no chapter 13 (Susanna) — skipped')

    # Bel and the Dragon = Daniel chapter 14 → standalone chapter 1
    if '14' in chs:
        out = APO_DIR / version / 'bel-and-dragon.json'
        if not out.exists():
            save_book(out, {'1': chs['14']})
            print(f'  {version}/bel-and-dragon.json — wrote chapter 1 ({len(chs["14"])} verses from Daniel 14)')
            written += 1
        else:
            print(f'  {version}/bel-and-dragon.json already exists — skipped')
    else:
        print(f'  {version}: Daniel has no chapter 14 (Bel) — skipped')

    # Prayer of Azariah = Daniel chapter 3, verses 24+ → standalone chapter 1
    if '3' in chs:
        ch3 = chs['3']
        extended = {str(i - PRAYER_OF_AZARIAH_START + 1): ch3[str(i)]
                    for i in range(PRAYER_OF_AZARIAH_START, max(int(v) for v in ch3.keys()) + 1)
                    if str(i) in ch3}
        if extended:
            out = APO_DIR / version / 'prayer-of-azariah.json'
            if not out.exists():
                save_book(out, {'1': extended})
                print(f'  {version}/prayer-of-azariah.json — wrote chapter 1 ({len(extended)} verses from Daniel 3 v{PRAYER_OF_AZARIAH_START}+)')
                written += 1
            else:
                print(f'  {version}/prayer-of-azariah.json already exists — skipped')
        else:
            print(f'  {version}: Daniel 3 has no extended verses at v{PRAYER_OF_AZARIAH_START}+ — skipped')
    else:
        print(f'  {version}: Daniel has no chapter 3 — skipped')

    return written


def extract_dr_esther_additions() -> int:
    """DR esther.json has 16 chapters; ch 11-16 are the Greek Esther additions.
    Map them to additions-esther.json chapters 1-6."""
    esther_path = APO_DIR / 'DR' / 'esther.json'
    out_path    = APO_DIR / 'DR' / 'additions-esther.json'
    if out_path.exists():
        print('  DR/additions-esther.json already exists — skipped')
        return 0
    if not esther_path.exists():
        print('  DR/esther.json not found — skipping')
        return 0

    chs = load_book(esther_path)
    addition_chapters = {}
    for i, src_ch in enumerate(range(11, 17), start=1):  # 11-16 → 1-6
        if str(src_ch) in chs:
            addition_chapters[str(i)] = chs[str(src_ch)]
        else:
            print(f'  DR esther: chapter {src_ch} not found')

    if addition_chapters:
        save_book(out_path, addition_chapters)
        total_v = sum(len(v) for v in addition_chapters.values())
        print(f'  DR/additions-esther.json — wrote {len(addition_chapters)} chapters, {total_v} verses (from DR esther ch 11-16)')
        return 1
    return 0


def main():
    total = 0

    print('=== DR ===')
    total += extract_daniel_additions('DR')
    total += extract_dr_esther_additions()

    print('\n=== WEB-CE ===')
    total += extract_daniel_additions('WEB-CE')
    # WEB-CE additions-esther is already a 10-chapter Greek Esther file (present)

    print(f'\nDone — {total} new files written.')


if __name__ == '__main__':
    main()
