#!/usr/bin/env python3
"""
absorb-parallels.py — Migrate OT-NT parallels data into the echoes format.

Reads each data/parallels/<book>.json, converts OT-NT connection types to the
echoes schema ({ type, target, note }), and merges into data/echoes/<book>.json.
Synoptic 'parallel' entries are skipped (they belong to parallels.js, not echoes).

Type mapping:
  prophecy-source  → fulfillment  (OT verse pointing toward NT fulfillment)
  allusion-source  → allusion     (OT verse underlying a NT allusion)
  quotation-source → quote        (OT verse directly quoted in NT)
  fulfillment      → fulfillment  (NT verse realizing OT prophecy)
  quotation        → quote        (NT verse quoting OT)
  allusion         → allusion     (NT verse alluding to OT)
  parallel         → SKIP         (synoptic / Chronicles parallel, not OT→NT echo)
"""

import json, os, sys, re

PARALLELS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'parallels')
ECHOES_DIR    = os.path.join(os.path.dirname(__file__), '..', 'data', 'echoes')

TYPE_MAP = {
    'prophecy-source':  'fulfillment',
    'allusion-source':  'allusion',
    'quotation-source': 'quote',
    'fulfillment':      'fulfillment',
    'quotation':        'quote',
    'allusion':         'allusion',
}

def normalize_ref(passage):
    """Normalize 'Matthew 1:23' to the same string format used in echoes targets."""
    return passage.strip()

def make_note(entry, target_passage):
    """Build a one-sentence note from the parallels label field."""
    label = entry.get('label', '').strip()
    if not label:
        return target_passage
    return label

def absorb_file(book_id, dry_run=False):
    par_path  = os.path.join(PARALLELS_DIR, book_id + '.json')
    echo_path = os.path.join(ECHOES_DIR,    book_id + '.json')
    if not os.path.exists(par_path):
        return 0

    with open(par_path, encoding='utf-8') as f:
        par_data = json.load(f)

    # Load existing echoes (may be empty or non-existent)
    echo_data = {}
    if os.path.exists(echo_path):
        with open(echo_path, encoding='utf-8') as f:
            echo_data = json.load(f)

    added = 0
    for ch, verses in par_data.items():
        for v, entries in verses.items():
            for entry in entries:
                par_type = entry.get('type', '')
                echo_type = TYPE_MAP.get(par_type)
                if not echo_type:
                    continue  # skip 'parallel' and any unknown types

                refs = entry.get('refs', [])
                for ref in refs:
                    target = normalize_ref(ref.get('passage', ''))
                    if not target:
                        continue
                    note = make_note(entry, target)

                    # Build the echo entry
                    new_echo = {'type': echo_type, 'target': target, 'note': note}

                    # Check for duplicates: same type + target already in this verse
                    # Guard against malformed entries (string instead of dict)
                    existing = echo_data.get(ch, {}).get(v, [])
                    if isinstance(existing, str):
                        existing = []   # malformed — treat as empty
                    already_present = any(
                        isinstance(e, dict) and
                        e.get('type') == echo_type and e.get('target') == target
                        for e in existing
                    )
                    if already_present:
                        continue

                    # Merge in (guard against malformed string entries)
                    if ch not in echo_data:
                        echo_data[ch] = {}
                    if v not in echo_data[ch] or isinstance(echo_data[ch][v], str):
                        echo_data[ch][v] = []
                    echo_data[ch][v].append(new_echo)
                    added += 1

    if added and not dry_run:
        # Sort by chapter then verse numerically
        sorted_data = {}
        for ch in sorted(echo_data.keys(), key=lambda x: int(x)):
            sorted_data[ch] = {}
            for vv in sorted(echo_data[ch].keys(), key=lambda x: int(x)):
                sorted_data[ch][vv] = echo_data[ch][vv]
        with open(echo_path, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, ensure_ascii=False, indent=2)

    return added

def main():
    dry_run = '--dry-run' in sys.argv
    total_added = 0
    books_updated = []

    for fname in sorted(os.listdir(PARALLELS_DIR)):
        if not fname.endswith('.json'):
            continue
        book_id = fname[:-5]
        added = absorb_file(book_id, dry_run=dry_run)
        if added:
            books_updated.append((book_id, added))
            total_added += added

    print(f'{"DRY RUN — " if dry_run else ""}Absorbed {total_added} parallels entries into echoes across {len(books_updated)} books:')
    for book_id, count in books_updated:
        print(f'  {book_id}: +{count}')

if __name__ == '__main__':
    main()
