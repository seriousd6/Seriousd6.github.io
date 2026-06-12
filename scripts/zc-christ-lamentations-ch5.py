"""
MKT Christ Commentary — Lamentations chapter 5
Run: python3 scripts/zc-christ-lamentations-ch5.py

Key classification decisions:
- v12 princes hanged: type — Gal 3:13 makes the tree-curse typology explicit
- v20 why forgotten: direct connection — Matt 27:46 is Christ's citation of Ps 22:1
  entering the abandonment experience Israel voices here
- v22 closing question: revelation of God — unanswered by Lamentations; answered
  definitively by the resurrection (Rom 8:31-39)
- Most verses: revelation of God or shadow — the chapter's reversals are the template
  for Christ's reversals (rest/yoke, bread of life, crown of life, new creation)
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

DATA_FILE = pathlib.Path(__file__).parent / 'zc-christ-lamentations-ch5-data.json'

def main():
    new_data = json.loads(DATA_FILE.read_text())
    existing = load_comm('mkt-christ', 'lamentations')
    merge_comm(existing, new_data)
    save_comm('mkt-christ', 'lamentations', existing)

    il = json.loads((ROOT / 'data/interlinear/lamentations.json').read_text())
    print('=== mkt-christ Lamentations ch5 coverage ===')
    for ch in range(5, 6):
        ck = str(ch)
        il_c = len(il.get(ck, {}))
        out_c = len(existing.get(ck, {}))
        status = 'OK' if out_c >= il_c else f'MISSING {il_c - out_c}'
        print(f'  ch{ch}: {out_c}/{il_c} {status}')

if __name__ == '__main__':
    main()
