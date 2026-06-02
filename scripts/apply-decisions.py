#!/usr/bin/env python3
"""
scripts/apply-decisions.py — merge workshop decisions into the glossary JSON files.

The Translation Workshop stores decisions in browser localStorage. This script
applies those decisions to the on-disk glossary files so that translate-bible.py
can see confirmed entries.

Workflow:
  1. In the workshop: click "Export JSON" → saves mkt-decisions-YYYY-MM-DD.json
  2. Run this script:
       python3 scripts/apply-decisions.py mkt-decisions-YYYY-MM-DD.json
  3. Committed glossary files now reflect your decisions.
  4. Run translate-bible.py to generate draft verse output.
  5. Run seed-glossary.py again to regenerate phase bundles (so the workshop
     queue shows the updated statuses on next load).

Usage:
  python3 scripts/apply-decisions.py <decisions-file.json>
  python3 scripts/apply-decisions.py <decisions-file.json> --dry-run
"""

import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

ROOT      = Path(__file__).parent.parent
GLOSS_DIR = ROOT / 'data' / 'translation'

GREEK_PATH  = GLOSS_DIR / 'glossary-greek.json'
HEBREW_PATH = GLOSS_DIR / 'glossary-hebrew.json'

VALID_STATUSES = {'confirmed', 'override', 'locked', 'disputed', 'deferred', 'draft'}

def load_glossary(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def save_glossary(path, data, dry_run):
    if dry_run:
        print(f'  [dry-run] would write {path}')
        return
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

def apply(decisions_path, dry_run=False):
    with open(decisions_path, encoding='utf-8') as f:
        raw = json.load(f)

    # Handle both wrapped {decisions: {...}} and bare {G26: {...}} formats
    decisions = raw.get('decisions', raw)
    exported  = raw.get('exported', 'unknown')

    print(f'Decisions file: {decisions_path}')
    print(f'  Exported:   {exported}')
    print(f'  Entries:    {len(decisions)}')
    print()

    greek  = load_glossary(GREEK_PATH)
    hebrew = load_glossary(HEBREW_PATH)

    stats = {'greek': {}, 'hebrew': {}}
    skipped = 0

    for code, dec in decisions.items():
        lang = 'greek' if code.startswith('G') else 'hebrew'
        gloss = greek if lang == 'greek' else hebrew

        if code not in gloss:
            print(f'  Warning: {code} not found in {lang} glossary — skipped')
            skipped += 1
            continue

        status = dec.get('status', '')
        if status and status not in VALID_STATUSES:
            print(f'  Warning: {code} has invalid status {status!r} — skipped')
            skipped += 1
            continue

        entry = gloss[code]
        old_status = entry.get('status', 'draft')

        # Apply all decision fields
        if status:
            entry['status'] = status

        # Tier overrides
        if dec.get('tiers'):
            entry['tiers'] = dec['tiers']

        # Decision log
        if dec.get('log'):
            existing_log = entry.get('decision_log', [])
            # Merge: add log entries not already present (dedupe by date+action)
            existing_keys = {(e.get('date',''), e.get('action',''), e.get('note','')) for e in existing_log}
            for item in dec['log']:
                key = (item.get('date',''), item.get('action',''), item.get('note',''))
                if key not in existing_keys:
                    existing_log.append(item)
                    existing_keys.add(key)
            entry['decision_log'] = existing_log

        # User notes
        if dec.get('notes'):
            entry['user_notes'] = dec['notes']

        # Track changes
        change = f'{old_status} → {status}' if status and status != old_status else 'log/tiers updated'
        stats[lang][code] = change

    # Print summary
    confirmed_g = sum(1 for c in stats['greek']   if 'confirmed' in stats['greek'][c]   or 'override' in stats['greek'][c]   or 'locked' in stats['greek'][c])
    confirmed_h = sum(1 for c in stats['hebrew']  if 'confirmed' in stats['hebrew'][c]  or 'override' in stats['hebrew'][c]  or 'locked' in stats['hebrew'][c])

    print(f'Greek:  {len(stats["greek"])} entries updated  ({confirmed_g} now confirmed/override/locked)')
    print(f'Hebrew: {len(stats["hebrew"])} entries updated  ({confirmed_h} now confirmed/override/locked)')
    if skipped:
        print(f'Skipped: {skipped}')
    print()

    # Show first 15 changes
    all_changes = [(f'[G] {c}', v) for c, v in stats['greek'].items()] + \
                  [(f'[H] {c}', v) for c, v in stats['hebrew'].items()]
    for label, change in sorted(all_changes)[:15]:
        print(f'  {label:12}  {change}')
    if len(all_changes) > 15:
        print(f'  … and {len(all_changes) - 15} more')
    print()

    save_glossary(GREEK_PATH,  greek,  dry_run)
    save_glossary(HEBREW_PATH, hebrew, dry_run)

    if not dry_run:
        print('Glossary files updated.')
        print()
        print('Next steps:')
        print('  1. Regenerate phase bundles so the workshop reflects new statuses:')
        print('       python3 scripts/seed-glossary.py')
        print('  2. Run the translation draft (once enough entries are confirmed):')
        print('       python3 scripts/translate-bible.py --tier all --testament nt')
        print('  3. Commit the updated glossary files:')
        print('       git add data/translation/glossary-*.json data/translation/phase*.json')
        print('       git commit -m "chore: apply workshop decisions"')
    else:
        print('[dry-run complete — no files written]')

def main():
    parser = argparse.ArgumentParser(description='Apply workshop decisions to glossary files')
    parser.add_argument('decisions_file', help='Path to the exported mkt-decisions-*.json file')
    parser.add_argument('--dry-run', action='store_true', help='Show what would change without writing')
    args = parser.parse_args()

    path = Path(args.decisions_file)
    if not path.exists():
        print(f'Error: {path} not found', file=sys.stderr)
        sys.exit(1)

    apply(path, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
