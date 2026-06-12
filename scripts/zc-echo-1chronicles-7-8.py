"""
Echo layer — 1 Chronicles chapters 7–8
Run: python3 scripts/zc-echo-1chronicles-7-8.py

Ch7: Ephraimite genealogy leads to Joshua (7:27) — the Joshua-Jesus typological name / Heb 4:8
Ch8: Benjaminite genealogy includes Saul's lineage (8:33) — Paul's tribal identity / Phil 3:5; Acts 13:21
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

ECHO = {
  "7": {
    "27": [
      {"type": "typology", "target": "Heb 4:8", "note": "Nun his son, Joshua his son — the Ephraimite genealogy of 1 Chronicles 7 ends with Joshua (Hoshea → Nun → Joshua), the same Joshua who led Israel into Canaan. Hebrews 4:8 makes the Joshua-Jesus typological connection explicit: if Joshua had given them rest, God would not have spoken of another day — the 'rest' Joshua provided was real but partial, pointing forward to the rest that Jesus secures. The shared name (Hebrew Yehoshua / Yeshua → Greek Iesous) is theologically loaded in Matt 1:21: you shall call his name Jesus, for he will save his people from their sins. The Chronicler's genealogy grounds this name in the Ephraimite lineage from which the first bearer came."},
      {"type": "allusion", "target": "Matt 1:21", "note": "The name Joshua/Jesus (Yehoshua → Yeshua → Iesous) appears in the Ephraimite lineage; Matt 1:21 gives the name its definitive interpretation — he will save his people from their sins — connecting the saving-leader name to its ultimate referent"}
    ]
  },
  "8": {
    "33": [
      {"type": "allusion", "target": "Phil 3:5", "note": "Ner fathered Kish, Kish fathered Saul — the Benjaminite genealogy of Saul runs through 1 Chronicles 8. Paul identifies himself as of the tribe of Benjamin (Phil 3:5: circumcised on the eighth day, of the people of Israel, of the tribe of Benjamin, a Hebrew of Hebrews), claiming descent from this same Benjaminite line. The genealogical precision mattered for Paul's identity claim: he was not a Hellenistic Jew of dubious ancestry but a Hebrew lineage Israelite traceable to Benjamin."},
      {"type": "allusion", "target": "Acts 13:21", "note": "Kish fathered Saul — Paul's synagogue sermon in Pisidian Antioch names Saul the son of Kish, a man of the tribe of Benjamin as the king God gave Israel, connecting the Saul of 1 Chronicles 8:33 to the sermon's OT historical review. The irony that Saul of Tarsus (Paul) — also a Benjaminite — persecuted the followers of Jesus before his conversion parallels the pattern of the first Saul: the Benjaminite who opposed YHWH's purposes and was replaced."}
    ]
  }
}

def main():
    e = load_echo('1chronicles')
    merge_echo(e, ECHO)
    save_echo('1chronicles', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'1chronicles echo: wrote {count} verses across ch 7-8')

if __name__ == '__main__':
    main()
