"""
Echo layer — 1 Chronicles chapters 23–25
Run: python3 scripts/zc-echo-1chronicles-23-25.py

Ch23: Levites' portage work ended when tabernacle replaced / Heb 9:11; Heb 8:5
Ch24: 24 priestly courses — 8th is Abijah / Luke 1:5 (Zechariah's division)
Ch25: Temple musicians who prophesied with harps and lyres / Rev 5:8-9; Rev 14:2-3
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
  "23": {
    "26": [
      {"type": "typology", "target": "Heb 9:11", "note": "David declares that the Levites no longer need to carry the tabernacle (mishkan) or its vessels, for YHWH has given rest to Israel — the portable wilderness sanctuary is superseded by the permanent temple. Hebrews 9:11 applies the same logic of supersession to Christ: he came as high priest of the good things that have come, through the greater and more perfect tent, not made with hands, not of this creation. The Chronicler's transition from tent-bearing to temple-service is the OT's own typological staging: each stage superseded by a more permanent dwelling, pointing toward the eternal sanctuary that is Christ himself."},
      {"type": "allusion", "target": "Heb 8:5", "note": "The Levites' portage of the tabernacle ending with David's rest — the earthly sanctuary passing from portable to fixed — reflects Heb 8:5's structure: the earthly priests serve a copy and shadow of the heavenly things. Just as Chronicles records the transition from tabernacle to temple as a progressive coming-to-rest, Hebrews presents both as shadows of the heavenly sanctuary that is the true and final form."}
    ]
  },
  "24": {
    "10": [
      {"type": "fulfillment", "target": "Luke 1:5", "note": "The 8th lot fell to Abijah — of the 24 priestly divisions established by David and Zadok in 1 Chronicles 24, the 8th is Abijah. Luke 1:5 names Zechariah, father of John the Baptist, as a priest of the division of Abijah — precisely this 8th course. Luke's specification of the priestly division grounds the Annunciation narrative in the temple-rotation system of 1 Chronicles 24; the angel's appearance to Zechariah while he burned incense is anchored in the Chronicler's organized priestly schedule. The birth of the forerunner is dated by the very calendar David established."},
      {"type": "allusion", "target": "Rev 8:3-4", "note": "The priestly courses organized by David (including Abijah, 8th course) administered the incense offering in the temple — Zechariah was burning incense when the angel appeared (Luke 1:9-11). Revelation 8:3-4 places incense and prayer at the heavenly altar: another angel came and stood at the altar with a golden censer, and he was given much incense to offer with the prayers of all the saints on the golden altar. The incense ministry of the 24 priestly courses finds its heavenly counterpart in the angelic incense-ministry before God's throne."}
    ]
  },
  "25": {
    "1": [
      {"type": "typology", "target": "Rev 5:8-9", "note": "David set apart for the service the sons of Asaph, Heman, and Jeduthun, who prophesied with lyres, with harps, and with cymbals — the 288 temple musicians (24 divisions of 12, v7) who sing and play as a form of prophecy in the sanctuary. Revelation 5:8-9 places 24 elders before the Lamb, each holding a harp and golden bowls of incense, and they sing a new song. The structural parallel is precise: 24 orders, harps, singing in God's presence. The Chronicler's prophetic musicians who worship before the Ark are the OT type of the heavenly worshipers who surround the Lamb."},
      {"type": "allusion", "target": "Rev 14:2-3", "note": "The sons of Asaph, Heman, and Jeduthun who prophesied with lyres and harps in the Chronicler's temple music — designated as prophecy, not mere performance — anticipate Rev 14:2-3: a sound like harpists playing on their harps, and they were singing a new song before the throne. The Chronicler's insistence that music is prophecy (25:1, 3: who prophesied) is the OT warrant for the heavenly singing that Revelation depicts as the ultimate consummation of temple worship."}
    ]
  }
}

def main():
    e = load_echo('1chronicles')
    merge_echo(e, ECHO)
    save_echo('1chronicles', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'1chronicles echo: wrote {count} verses across ch 23-25')

if __name__ == '__main__':
    main()
