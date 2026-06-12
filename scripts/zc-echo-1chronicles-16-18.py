"""
MKT Echo Layer — 1 Chronicles chapters 16–18
Run: python3 scripts/zc-echo-1chronicles-16-18.py

Ch 16: David's psalm before the ark — drawn from Ps 96, 105, 106; key NT echoes
        in universal praise (Rev 5, 19), idols vs. YHWH (1 Cor 8), judgment coming (Rev 11),
        hesed-endurance (1 Pet 1), and gathering from nations (Rom 11).
Ch 17: Davidic covenant (already has v13 → Heb 1:5); adding v11-12 (Acts 2:30) and v14 (Lk 1:32-33).
Ch 18: David's just reign as type of messianic justice (Isa 9:7 / Jer 23:5).

Absorption from parallels:
- ch17:1 (2 Sam 7:1-16) → already captured by v13/Heb 1:5 entry
- ch18:1 (2 Sam 8:1-18) → narrative parallel; echo layer focuses on messianic-type dimension
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

CHRON1_ECHOES = {
  "16": {
    "8": [
      {
        "type": "allusion",
        "target": "Ps 105:1",
        "note": "David's psalm (vv8-22) is drawn substantially from Ps 105:1-15 — the psalm of Israel's covenant history from Abraham through the Exodus; Chronicles places it at the ark's installation as the theological interpretive frame for the Davidic covenant"
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Luke 9:35",
        "note": "'Touch not my anointed ones; do my prophets no harm' — the Hebrew ‎meshiḥay (my anointed ones) refers to the patriarchs in context (Ps 105:15); the divine protection-of-the-anointed formula anticipates the Father's declaration over Jesus ('This is my Son, my Chosen') as YHWH's supreme anointed one whom no one may harm with impunity"
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "1 Cor 8:4-6",
        "note": "'All the gods of the peoples are idols (‎elilim), but the LORD made the heavens' — the contrast between the non-existence of pagan gods and YHWH as creator is the theological foundation Paul develops in 1 Cor 8:4-6: idols are nothing (oudeis theos ei mē heis) and there is one God the Father from whom all things come, one Lord Jesus Christ through whom all things exist"
      }
    ],
    "31": [
      {
        "type": "fulfillment",
        "target": "Rev 19:6",
        "note": "'The LORD reigns' (YHWH mālāk) — the enthronement cry of this psalm is taken up in Rev 19:6 as the heavenly multitude cries 'Hallelujah! For the Lord our God, the Almighty, reigns (ebasileúsen)' — the temporal declaration of David's psalm becomes the eschatological announcement of the final enthronement"
      }
    ],
    "33": [
      {
        "type": "fulfillment",
        "target": "Rev 11:18",
        "note": "'He comes to judge the earth' (bāʾ lišpōṭ hāʾāreṣ) — Ps 96:13, repeated here, provides the vocabulary for the eschatological judgment; Rev 11:18 announces 'the time has come for judging the dead' at the seventh trumpet, fulfilling this psalm's anticipation of YHWH's coming judgment of all the earth"
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "1 Pet 1:24-25",
        "note": "'For his steadfast love (ḥesed) endures forever' — the ḥesed-refrain becomes in the NT the ground of the imperishable word (1 Pet 1:23-25 citing Isa 40:6-8: the word of the Lord endures forever); the psalm's insistence on YHWH's never-ending covenant-love is the OT ground for the NT claim that the gospel stands permanently"
      }
    ],
    "35": [
      {
        "type": "fulfillment",
        "target": "Rom 11:26",
        "note": "'Gather us and deliver us from among the nations' — the psalm's prayer for regathering from exile (originally pointing toward the Babylonian return) anticipates the eschatological ingathering Paul describes in Rom 11:25-26: the fullness of the Gentiles coming in, then all Israel being saved — the final gathering that the psalm foreshadows"
      }
    ]
  },
  "17": {
    "11": [
      {
        "type": "fulfillment",
        "target": "Acts 2:30",
        "note": "'I will raise up one of your own sons after you, and I will establish his kingdom' — Acts 2:30 cites the Davidic covenant (2 Sam 7 / 1 Chr 17) to explain the resurrection: 'knowing that God had sworn with an oath to seat one of his descendants on his throne,' Peter declares that Jesus, raised from the dead, now occupies that throne; the 'raising up' of v11 finds its ultimate fulfillment in the resurrection-enthronement, not merely in Solomon"
      }
    ],
    "14": [
      {
        "type": "fulfillment",
        "target": "Luke 1:32-33",
        "note": "'I will establish him in my house and over my kingdom forever, and his throne will stand firm forever' — the angel Gabriel announces to Mary in near-verbatim terms: 'He will be great and will be called the Son of the Most High. The Lord God will give him the throne of his father David, and he will reign over Jacob's descendants forever; his kingdom will never end' (Luke 1:32-33) — a direct citation of the Davidic covenant's eternal-throne promise, declared fulfilled in Jesus"
      }
    ]
  },
  "18": {
    "14": [
      {
        "type": "type",
        "target": "Isa 9:7",
        "note": "'David reigned over all Israel and administered justice (mišpāṭ) and equity (ṣᵉdāqāh) to all his people' — David's just reign is the historical type that Isaiah's messianic prophecy elaborates: 'of the increase of his government and peace there will be no end; he will reign on David's throne... with justice (mišpāṭ) and righteousness (ṣᵉdāqāh) forever' (Isa 9:7); the Chronicler's summary of David's reign as characterized by justice and equity is precisely the language the prophets use for the coming Messiah's rule"
      },
      {
        "type": "allusion",
        "target": "Jer 23:5",
        "note": "The summary of David's just administration anticipates Jeremiah's 'righteous Branch' oracle: 'I will raise up for David a righteous Branch, a King who will reign wisely and do what is just (mišpāṭ) and right (ṣᵉdāqāh) in the land' (Jer 23:5) — the terms are identical; David's historical reign of justice is both the precedent and the shadow of the Branch's coming rule"
      }
    ]
  }
}

def main():
    e = load_echo('1chronicles')
    merge_echo(e, CHRON1_ECHOES)
    save_echo('1chronicles', e)
    count = sum(len(v) for v in CHRON1_ECHOES.values())
    print(f'1chronicles echoes: wrote {count} verse entries across ch 16-18')

if __name__ == '__main__':
    main()
