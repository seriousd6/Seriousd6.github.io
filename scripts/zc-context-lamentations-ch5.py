"""
MKT Context Commentary — Lamentations chapter 5
Run: python3 scripts/zc-context-lamentations-ch5.py

Key decisions:
- Ch5 is non-acrostic (22 verses matching alphabet count but no alphabetical structure)
- Deuteronomy 28 covenant-curse framework applied throughout
- v7 engages the generational sin tension with Jer 31:29-30 and Ezek 18
- v21 uses shuv (return) to connect with Jer 31:18 and new covenant petition
- v22 ending: unanswered question treated as deliberate theological move
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

DATA_FILE = pathlib.Path(__file__).parent / 'zc-context-lamentations-ch5-data.json'

def main():
    new_data = json.loads(DATA_FILE.read_text())
    existing = load_comm('mkt-context', 'lamentations')
    merge_comm(existing, new_data)
    save_comm('mkt-context', 'lamentations', existing)

    il = json.loads((ROOT / 'data/interlinear/lamentations.json').read_text())
    print('=== mkt-context Lamentations ch5 coverage ===')
    for ch in range(5, 6):
        ck = str(ch)
        il_c = len(il.get(ck, {}))
        out_c = len(existing.get(ck, {}))
        status = 'OK' if out_c >= il_c else f'MISSING {il_c - out_c}'
        print(f'  ch{ch}: {out_c}/{il_c} {status}')

if __name__ == '__main__':
    main()
