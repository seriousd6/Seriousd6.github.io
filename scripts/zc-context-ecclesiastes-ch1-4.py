"""
MKT Context Commentary — Ecclesiastes chapters 1–4 (fill pass)
Run: python3 scripts/zc-context-ecclesiastes-ch1-4.py

Fills missing verses in ch1-4 context; ch1:v1 already present from prior script.
Key decisions:
- Solomonic persona = literary/rhetorical device (not a literal authorship claim)
- ANE parallels: Gilgamesh (Siduri carpe diem), Egyptian Harper's Song, Mesopotamian Pessimistic Dialogue
- 'Under the sun' (29x) = mortal existence frame without resurrection horizon
- 'Hevel' = vapor/breath (impermanence), not nihilism
- 3:11 'eternity in the heart' = anthropological center; human transcendence-intuition
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


import json as _json

ECCLESIASTES = _json.loads(pathlib.Path(ROOT / 'scripts' / 'zc-context-ecclesiastes-ch1-4-data.json').read_text())

def main():
    existing = load_comm('mkt-context', 'ecclesiastes')
    merge_comm(existing, ECCLESIASTES)
    save_comm('mkt-context', 'ecclesiastes', existing)

    il = _json.loads((ROOT / 'data' / 'interlinear' / 'ecclesiastes.json').read_text())
    for ch in [1, 2, 3, 4]:
        ck = str(ch)
        missing = set(il.get(ck, {}).keys()) - set(existing.get(ck, {}).keys())
        print(f'  ch{ch}: {"complete" if not missing else "MISSING " + str(sorted(missing, key=int))}')

if __name__ == '__main__':
    main()
