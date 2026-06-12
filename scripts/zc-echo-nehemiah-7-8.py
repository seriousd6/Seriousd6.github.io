"""
Echo Layer — Nehemiah chapters 7–8 (gap-fill: ch 7 missing)
Run: python3 scripts/zc-echo-nehemiah-7-8.py

Ch 8 already has 1 entry (Neh 8:8 → Luke 24:45 from zc-echo-ezra-1-4.py).
This script adds ch 7 echo entries:
- 7:2: Hanani and Hananiah appointed as faithful gatekeepers → 2 Tim 2:2
- 7:5: God puts it in Nehemiah's heart to examine who belongs → Heb 4:12-13
- 7:64-65: Priestly genealogy crisis — excluded until priest with Urim and Thummim →
  Heb 7:11-17 (Christ as the priest who renders the Aaronic order obsolete)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

NEH_ECHO = {
  "7": {
    "2": [
      {"type": "allusion", "target": "2 Tim 2:2", "note": "Nehemiah appoints his brother Hanani and Hananiah the governor of the castle over Jerusalem because 'he was a more faithful and God-fearing man than many' — the criterion for appointment is faithfulness and fear of God, not status or lineage; Paul's instruction to Timothy follows the same criterion: 'entrust to faithful men who will be able to teach others also' (2 Tim 2:2); the pattern of selecting leaders on the basis of character rather than birth or social position is the governing principle of both Nehemiah's administration and the church's leadership"}
    ],
    "5": [
      {"type": "allusion", "target": "Heb 4:12-13", "note": "God put it into Nehemiah's heart to examine the genealogy — the divine prompting to investigate who genuinely belongs to the covenant community; this points to the NT's understanding of divine scrutiny: 'the word of God is living and active, sharper than any two-edged sword, piercing to the division of soul and spirit... discerning the thoughts and intentions of the heart. And no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account' (Heb 4:12-13); YHWH's impulse to Nehemiah to examine who belongs shadows the divine omniscience that sees every heart"},
      {"type": "allusion", "target": "Rev 20:12", "note": "Nehemiah discovers the book of genealogy of those who returned first and has it read — the covenant community's identity established by being found in the written record; Rev 20:12 describes the final judgment: 'books were opened... and the dead were judged by what was written in the books, according to what they had done. And another book was opened, which is the book of life'; the genealogical registry of Nehemiah 7 is the earthly type of the eschatological book of life — belonging is determined by being found written in the record"}
    ],
    "65": [
      {"type": "fulfillment", "target": "Heb 7:11-17", "note": "The governor tells the priests whose genealogy could not be verified that they cannot eat the most holy food 'until a priest should arise with Urim and Thummim' — the suspension of their priestly rights awaiting a future definitive priestly oracle; the writer of Hebrews announces exactly this fulfillment: Christ 'has become a priest not on the basis of a legal requirement concerning bodily descent but by the power of an indestructible life' (Heb 7:16); he is the priest who renders the Aaronic order superseded, and his high-priestly authority resolves every question the Urim and Thummim could only signal"}
    ]
  }
}

def main():
    e = load_echo('nehemiah')
    before_chs = set(e.keys())
    merge_echo(e, NEH_ECHO)
    after_chs = set(e.keys())
    new_chs = sorted(after_chs - before_chs, key=int)
    save_echo('nehemiah', e)
    total_added = sum(len(v) for v in NEH_ECHO.values())
    print(f'nehemiah echo ch 7-8: added {total_added} verse-entries for ch7; ch7 now complete')
    if new_chs:
        print(f'  new chapters: {new_chs}')

if __name__ == '__main__':
    main()
