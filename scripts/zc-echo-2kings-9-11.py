"""
MKT Echo Data — 2 Kings chapters 9–11
Run: python3 scripts/zc-echo-2kings-9-11.py

Ch9: Jehu's anointing as the scourge of Ahab — prophetic anointing under cover;
     Jezebel's death in Naboth's plot — blood-for-blood fulfillment;
     Jehu as the anti-Ahab, the zeal-for-YHWH king (cf. 10:16)
Ch10: Jehu's purge — Ahab's dynasty ends; zeal that exceeds its mandate
Ch11: Joash hidden in the temple — the preserved royal heir / Rev 12 (hidden child)
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
    "6": [
      {"type": "allusion", "target": "John 18:36", "note": "Elisha sends a young prophet to anoint Jehu king in secret, in a private chamber, apart from the generals — a covert royal anointing that must be hidden until the moment of action; Jesus before Pilate: 'My kingdom is not of this world. If my kingdom were of this world, my servants would have been fighting.' The messianic king's identity is announced in hiddenness and only revealed at the appointed moment of confrontation."},
      {"type": "allusion", "target": "Acts 10:38", "note": "The anointing of Jehu (the scourge of Baal's dynasty) with the horn of oil — commissioned by a word from Elisha, carried out by a young prophet — is one of the OT's prophetic anointings that shapes the messianic anointing pattern; Acts 10:38 names the fulfillment: 'God anointed Jesus of Nazareth with the Holy Spirit and with power.'"}
    ],
    "26": [
      {"type": "allusion", "target": "Heb 12:24", "note": "Jehu fulfills Elijah's blood-oracle over Naboth's vineyard: the blood of Naboth and his sons (shed in the very plot now claimed by Joram) is avenged in the plot itself — blood answers blood in the place of blood. Heb 12:24 names the final resolution: Jesus's blood 'speaks a better word than the blood of Abel.' The blood-for-blood pattern that drives OT judgment (Naboth → Joram; Abel → Cain) is resolved in the one whose shed blood speaks mercy rather than vengeance."}
    ]
  },
  "11": {
    "3": [
      {"type": "allusion", "target": "Rev 12:5-6", "note": "Joash is hidden in the temple for six years while Athaliah rules — the legitimate Davidic heir concealed in YHWH's house while a usurper occupies the throne — an OT type of the hidden king awaiting the appointed moment of revelation; Rev 12:5-6 depicts the woman's child caught up to God while the dragon pursues her and she flees into the wilderness for 1,260 days. The pattern: the true heir hidden, the usurping power regnant, the moment of revelation coming at divine appointment."},
      {"type": "allusion", "target": "Matt 2:13-14", "note": "Joash the infant king hidden from Athaliah's massacre in the temple typologically parallels the infant Jesus hidden in Egypt from Herod's massacre (Matt 2:13-14); in both cases the legitimate royal heir survives a murderous usurper's attempt to eliminate the Davidic line, is protected in a place of divine provision, and emerges at the appointed time to claim the throne."}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, ECHO)
    save_echo('2kings', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2kings echo: wrote {count} verses across ch 9-11')

if __name__ == '__main__':
    main()
