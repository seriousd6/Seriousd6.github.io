"""
MKT Christ Commentary — Song of Solomon chapters 1-6
Run: python3 scripts/zc-christ-songofsolomon-ch1-6.py

Key classification decisions:
- Most verses: shadow or revelation of God — the Song's love imagery as shadow of Christ-church love
- ch3:4 finding/holding the beloved: type — NT parallel is Mary Magdalene at the empty tomb (John 20:16-17)
- ch4:7 "no defect": direct connection — Eph 5:27 is the explicit NT citation of this theme
- ch3:9-10 litter/Tabernacle materials: type — deliberate incense/temple vocabulary
- ch6:10 dawn/sun/moon: shadow — Rev 12:1 applies same imagery to the glorified church
- Mutual possession formula reversal (2:16 vs 6:3) treated as revelation of maturation in faith
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

DATA_FILE = pathlib.Path(__file__).parent / 'zc-christ-songofsolomon-ch1-6-data.json'

def main():
    new_data = json.loads(DATA_FILE.read_text())
    existing = load_comm('mkt-christ', 'songofsolomon')
    merge_comm(existing, new_data)
    save_comm('mkt-christ', 'songofsolomon', existing)

    # Verify coverage ch1-6
    il = json.loads((ROOT / 'data/interlinear/songofsolomon.json').read_text())
    print('=== mkt-christ Song of Solomon ch1-6 coverage ===')
    for ch in range(1, 7):
        ck = str(ch)
        il_c = len(il.get(ck, {}))
        out_c = len(existing.get(ck, {}))
        status = 'OK' if out_c >= il_c else f'MISSING {il_c - out_c}'
        print(f'  ch{ch}: {out_c}/{il_c} {status}')

if __name__ == '__main__':
    main()
