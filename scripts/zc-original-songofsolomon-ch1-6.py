#!/usr/bin/env python3
"""Merge mkt-original commentary for Song of Solomon ch1-6 from data file."""
import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(SCRIPT_DIR, "zc-original-songofsolomon-ch1-6-data.json")
OUT_FILE = os.path.join(REPO_ROOT, "data/commentary/mkt-original/songofsolomon.json")
IL_FILE = os.path.join(REPO_ROOT, "data/interlinear/songofsolomon.json")


def merge_comm(path, new_data):
    try:
        existing = json.load(open(path, encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        existing = {}
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, content in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = content
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    return existing


# Load data
new_data = json.load(open(DATA_FILE, encoding="utf-8"))
out = merge_comm(OUT_FILE, new_data)

# Verify coverage
il = json.load(open(IL_FILE, encoding="utf-8"))
print("=== mkt-original Song of Solomon ch1-6 coverage ===")
total_il = total_out = 0
for ch in range(1, 7):
    il_count = len(il.get(str(ch), {}))
    out_count = len(out.get(str(ch), {}))
    total_il += il_count
    total_out += out_count
    status = "OK" if out_count >= il_count else f"MISSING {il_count - out_count}"
    print(f"  ch{ch}: {out_count}/{il_count} {status}")
print(f"  TOTAL: {total_out}/{total_il}")
