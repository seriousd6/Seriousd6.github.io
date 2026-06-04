#!/usr/bin/env python3
"""
Parse the `deriv` field in data/strongs/greek.json and data/strongs/hebrew.json,
extract Strong's cross-references (G[0-9]+ and H[0-9]+), and write `see_also` arrays
back into each entry in-place.

Run once from repo root:
  python3 scripts/add-see-also.py

Output: overwrites greek.json and hebrew.json with `see_also` field added.
The field is a list of strings like ["G1537", "G5055"] (Greek-to-Greek or
Greek-to-Hebrew refs). Entries with no parseable refs get `see_also: []`.
"""

import json
import re
from pathlib import Path

GREEK_PATH = Path("data/strongs/greek.json")
HEBREW_PATH = Path("data/strongs/hebrew.json")

# Match G\d+ or H\d+ Strong's IDs — skip multi-digit sequences that are clearly
# not Strong's numbers (Strong's tops out at G5624 / H8674)
GREEK_PATTERN = re.compile(r'\bG(\d{1,4})\b')
HEBREW_PATTERN = re.compile(r'\bH(\d{1,4})\b')


def extract_refs(deriv_text, own_key):
    """Return list of Strong's IDs referenced in deriv_text, excluding own_key."""
    if not deriv_text:
        return []
    greek_ids = ['G' + m for m in GREEK_PATTERN.findall(deriv_text)]
    hebrew_ids = ['H' + m for m in HEBREW_PATTERN.findall(deriv_text)]
    all_refs = greek_ids + hebrew_ids
    # Deduplicate and remove self-references
    seen = set()
    result = []
    for ref in all_refs:
        if ref != own_key and ref not in seen:
            seen.add(ref)
            result.append(ref)
    return result


def process_file(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    changed = 0
    for key, entry in data.items():
        deriv = entry.get('deriv', '')
        refs = extract_refs(deriv, key)
        if entry.get('see_also') != refs:
            entry['see_also'] = refs
            changed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{path.name}: {len(data)} entries, {changed} updated")
    non_empty = sum(1 for e in data.values() if e.get('see_also'))
    print(f"  → {non_empty} entries now have see_also refs")


if __name__ == '__main__':
    for p in [GREEK_PATH, HEBREW_PATH]:
        if not p.exists():
            print(f"SKIP: {p} not found")
            continue
        process_file(p)
