"""
mkt-original | amos | ch1–5 | 86 verses
run: python3 scripts/zc-original-amos-1-5.py

Key interpretation decisions:
- 1:3–2:16: oracle formula 'for three crimes… and for four' (x, x+1 idiom = maximal accumulation)
- 2:8: begadim chavolim (pledged garments) — collateral forbidden to be kept overnight (Exod 22:26)
- 3:2: yada'ti (I have known) — covenant-election sense; election intensifies accountability
- 3:7: sod (divine council/secret) — the prophet admitted to YHWH's inner deliberative council
- 4:1: parot ha-Bashan (cows of Bashan) — satirical address to wealthy women as fattened cattle
- 4:4-5: sarcastic liturgical parody — 'come and rebel' in worship-call form
- 5:1: qinah meter — 3+2 stress pattern of funeral lament; Israel addressed in its own dirge
- 5:18: yom YHWH — first extended treatment in writing prophets; popular expectation inverted
- 5:24: nachal eitan (ever-flowing stream) = perennial wadi, not seasonal; permanent justice demanded
- 5:26: Sikkuth/Kiyyun vocalized with sheqets vowels (contempt); Acts 7:42-43 cites LXX version
- Loads data from zc-original-amos-1-5-data.json (same directory)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_FILE = pathlib.Path(__file__).parent / 'zc-original-amos-1-5-data.json'

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

def main():
    new_data = json.loads(DATA_FILE.read_text())
    existing = load_comm('mkt-original', 'amos')
    merge_comm(existing, new_data)
    save_comm('mkt-original', 'amos', existing)

if __name__ == '__main__':
    main()
