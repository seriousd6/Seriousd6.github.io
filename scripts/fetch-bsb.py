#!/usr/bin/env python3
"""
fetch-bsb.py — Download and install the Berean Standard Bible (CC0).

Source: scrollmapper/bible_databases on GitHub
License: CC0 — may be freely used, reproduced, and distributed.

Run from repo root:
  python3 scripts/fetch-bsb.py

Idempotent — skips books that already exist.
"""

import json
import os
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')
OUT_DIR    = os.path.join(REPO_ROOT, 'data', 'bible', 'BSB')
SOURCE_URL = ('https://raw.githubusercontent.com/scrollmapper/'
              'bible_databases/master/formats/json/BSB.json')

def main():
    with open(BOOKS_JSON) as f:
        books_meta = json.load(f)

    print(f'Fetching BSB from scrollmapper …')
    with urllib.request.urlopen(SOURCE_URL, timeout=30) as r:
        bsb = json.load(r)

    bsb_books = bsb['books']
    os.makedirs(OUT_DIR, exist_ok=True)

    ok = skip = 0
    for bsb_book, meta in zip(bsb_books, books_meta):
        out_file = os.path.join(OUT_DIR, meta['id'] + '.json')
        if os.path.exists(out_file):
            print(f'  {meta["name"]} — skipped (exists)')
            skip += 1
            continue

        chapters_out = {}
        for ch_obj in bsb_book['chapters']:
            ch_key    = str(ch_obj['chapter'])
            verses_out = {}
            for v_obj in ch_obj['verses']:
                text = v_obj.get('text', '').strip()
                if text:
                    verses_out[str(v_obj['verse'])] = text
            if verses_out:
                chapters_out[ch_key] = verses_out

        out = {
            'version': 'BSB',
            'book':    meta['name'],
            'bookId':  meta['id'],
            'chapters': chapters_out,
        }
        with open(out_file, 'w') as f:
            json.dump(out, f, ensure_ascii=False, separators=(',', ':'))

        total_v = sum(len(v) for v in chapters_out.values())
        print(f'  {meta["name"]} — {len(chapters_out)} chapters, {total_v} verses')
        ok += 1

    print(f'\nDone. Written: {ok}  Skipped: {skip}')

if __name__ == '__main__':
    main()
