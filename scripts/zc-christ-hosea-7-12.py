"""
mkt-christ | hosea | ch7–12 | 87 verses
run: python3 scripts/zc-christ-hosea-7-12.py

Key directness assignments:
- 8:7 (sow wind/whirlwind → Gal 6:7-8), 8:12 (law foreign → Heb 8:10 new covenant),
  8:13 (no pleasure in sacrifice → Heb 10:6), 10:8 (mountains cover us → Luke 23:30/Rev 6:16),
  10:12 (seek LORD until he comes → Matt 6:33/1 Cor 1:30), 12:9 (tents → John 1:14 tabernacle),
  12:10 (prophets → Heb 1:1-2), 12:13 (prophet from Egypt → Acts 3:22) = direct
- 11:8 (How can I give you up → Matt 23:37), 11:9 (God-not-human → Phil 2:6-8 Incarnation),
  11:10 (lion roar → Rev 5:5 Lion of Judah), 12:8 (I am rich → Rev 3:17 Laodicea) = direct
- Loads data from zc-christ-hosea-7-12-data.json (same directory)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_FILE = pathlib.Path(__file__).parent / 'zc-christ-hosea-7-12-data.json'

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
    existing = load_comm('mkt-christ', 'hosea')
    merge_comm(existing, new_data)
    save_comm('mkt-christ', 'hosea', existing)

if __name__ == '__main__':
    main()
