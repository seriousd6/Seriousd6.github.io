"""
mkt-original | micah | ch1–6 | 84 verses
run: python3 scripts/zc-original-micah-1-6.py

Key interpretation decisions:
- 1:1: Micah ben Moresheth — rural Judean village; class-conscious shepherd-prophet vs urban elite
- 1:8-16: paronomasia city-lament chain — each town name puns on its fate (Gath/tell, Aphrah/dust, etc.)
- 2:2: nachala (inalienable tribal inheritance) — Naboth-syndrome latifundialization condemned
- 2:12-13: poretz (breakthrough one) — shepherd-king who breaks open the pen; messianic overtone
- 3:12: Zion-plowed-as-field — verbatim citation in Jer 26:18 (rare OT intra-citation)
- 4:1-4: eschatological mountain vision — parallel to Isa 2:2-4 (shared oracle tradition)
- 4:8: Migdal Eder (Tower of the Flock) — near Bethlehem; shepherd-messianic geography
- 4:10: Babylon prophecy — remarkable specificity from 8th-c. prophet (Babylonian exile still 120 yrs off)
- 5:1: cheek-struck judge — siege context before 5:2 Bethlehem oracle
- 5:5: ve-hayah zeh shalom — 'this one shall be their peace' = personal, not treaty peace
- 6:1-2: mountains-as-witnesses — cosmic courthouse using creation as jury
- 6:8: mishpat/chesed/tsena'at lekhet — three-clause climax resolving the sacrificial ladder
- Loads data from zc-original-micah-1-6-data.json (same directory)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_FILE = pathlib.Path(__file__).parent / 'zc-original-micah-1-6-data.json'

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
    existing = load_comm('mkt-original', 'micah')
    merge_comm(existing, new_data)
    save_comm('mkt-original', 'micah', existing)

if __name__ == '__main__':
    main()
