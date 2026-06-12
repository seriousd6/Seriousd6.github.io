"""
Echo layer — 1 Chronicles chapters 9–10
Run: python3 scripts/zc-echo-1chronicles-9-10.py

Ch9: Gatekeepers registered in faithfulness — controlled sanctuary access / Heb 10:19-22
Ch10: Saul's theological verdict — not seeking YHWH / Heb 11:6; Acts 13:22
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
  "9": {
    "22": [
      {"type": "typology", "target": "Heb 10:19-22", "note": "All these, who were chosen as gatekeepers at the thresholds, were 212. They were enrolled by genealogies in their villages. David and Samuel the seer established them in their office of trust — the 212 gatekeepers appointed in faithfulness (be-emunatam) to control access to the sanctuary embody the OT system of restricted entry to God's presence. Hebrews 10:19-22 announces the system's end: we have confidence to enter the holy places by the blood of Jesus, by the new and living way that he opened for us through the curtain. The gatekeepers' office (maintaining who may and may not enter) is superseded by the opened veil; what the gatekeepers enforced as restriction, Christ removes as barrier."},
      {"type": "allusion", "target": "John 10:9", "note": "The gatekeepers who control access to the sanctuary — appointed in faithfulness by David — anticipate Jesus's declaration: I am the gate; if anyone enters by me, he will be saved. The shift is from human gatekeepers restricting access to the divine gate who opens it; from an office that excludes the unqualified to the one who qualifies all who enter through him."}
    ]
  },
  "10": {
    "14": [
      {"type": "typology", "target": "Heb 11:6", "note": "He did not seek guidance from YHWH. Therefore YHWH put him to death — the Chronicler's theological verdict on Saul names his core failure as not seeking YHWH (lo darash be-YHWH). Hebrews 11:6 names the same principle positively: whoever would draw near to God must believe that he exists and that he rewards those who seek him. Saul is the OT's sharpest negative case: a man who ceased to seek YHWH (after 1 Sam 28's consultation of the medium) and whose kingdom-failure is presented as the direct result. The faith-hall of Hebrews 11 implicitly includes the contrast of those who, unlike Saul, sought God through death."},
      {"type": "allusion", "target": "Acts 13:22", "note": "He did not seek guidance from YHWH — Saul's failure to seek God leads the Chronicler immediately to David. Paul's synagogue sermon in Acts 13:22 makes the contrast explicit: after removing Saul he raised up David to be their king, of whom he testified: I have found in David the son of Jesse a man after my heart, who will do all my will. The not-seeking-Saul/heart-of-David contrast in Acts 13 is the NT's reading of exactly the Chronicler's theological move from 1 Chr 10 to 11."}
    ]
  }
}

def main():
    e = load_echo('1chronicles')
    merge_echo(e, ECHO)
    save_echo('1chronicles', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'1chronicles echo: wrote {count} verses across ch 9-10')

if __name__ == '__main__':
    main()
