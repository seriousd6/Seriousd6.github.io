"""
MKT Echo — Daniel chapters 6–8
Run: python3 scripts/zc-echo-daniel-6-8.py

Echo is selective: only verses with meaningful OT→NT connections are included.
Chapters 6–7 already have entries; this script adds chapter 8.

Key decisions:
- Dan 8:9-11 small horn (Antiochus IV) classified as shadow/type of the NT Antichrist
  figure; Matt 24:15 explicitly fulfills the "abomination of desolation" language of
  Dan 8:11,13 (and Dan 9:27/11:31).
- Dan 8:16 Gabriel's first naming: canon thread running to Luke 1:19,26.
- Dan 8:18 prostration-and-raising pattern: allusion to Rev 1:17 / Matt 17:6-7.
- Dan 8:25 "broken without human hand": allusion to Dan 2:34 and Rev 19:20.
- Dan 8:26 "seal up the vision": deliberate contrast with Rev 22:10 unsealing.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

DANIEL_ECHOES = {
  "8": {
    "11": [
      {
        "type": "fulfillment",
        "target": "Matt 24:15",
        "note": "The 'abomination of desolation' language Jesus cites in Matt 24:15 ('let the reader understand') draws on this verse (the regular offering taken away, the sanctuary overthrown) together with Dan 9:27 and 11:31. Jesus presents Antiochus IV's desecration as a type with a future antitype in the end times."
      },
      {
        "type": "shadow",
        "target": "2 Thess 2:4",
        "note": "The small horn magnifying itself against the Prince of the host and overturning his sanctuary is the OT shadow behind Paul's 'man of lawlessness' who exalts himself above every god and takes his seat in the temple — the same sacrilegious self-deification pattern at eschatological scale."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Rev 6:10",
        "note": "The holy one's question 'How long will the vision last — the regular offering taken away and the transgression that devastates?' (v.13) is structurally identical to the souls under the altar in Rev 6:10 crying 'How long, O Lord?' Both frame the suffering of God's people as a precisely measured interval that the sovereign God will end at the appointed time."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Luke 1:19",
        "note": "Gabriel is named for the first time in Scripture here, sent to interpret the vision. The same Gabriel reappears in Luke 1:19 (to Zechariah) and 1:26 (to Mary), creating a canonical thread: the angel who interpreted history's apocalyptic empires is the same messenger who announces the birth of the one whose kingdom will end them all."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Rev 1:17",
        "note": "Gabriel's address 'Understand, son of man, that the vision is for the time of the end' and Daniel's terror at an angelic presence anticipates the pattern at Rev 1:17 where John, in the presence of the risen Christ, falls as dead before being raised and commissioned to understand end-time revelation."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Matt 17:6-7",
        "note": "Daniel falls into a deep sleep face-down before the angel; Gabriel touches him and raises him to his feet. The identical pattern — prostration before heavenly glory, a touch, the command 'rise' — recurs at the Transfiguration (Matt 17:6-7), establishing a scriptural register of how humans respond to theophany and how God meets that collapse."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Rev 19:20",
        "note": "'He will be broken without human hand' (v.25) — the antitypical Antichrist figure is destroyed by divine agency alone, not human power. Dan 2:34 (the stone cut without hands that destroys the statue) uses the same motif; Rev 19:20 fulfills it when the beast is thrown directly into the lake of fire without a human battle."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Rev 22:10",
        "note": "Gabriel commands Daniel to 'seal up the vision, for it concerns the distant future.' Rev 22:10 deliberately inverts this: 'Do not seal up the words of the prophecy of this book, for the time is near.' The unsealing marks the transition from promise to fulfillment: what Daniel was told to close, John is told to open — the age of apocalyptic concealment has ended in Christ."
      }
    ]
  }
}

def main():
    existing = load_echo('daniel')
    merge_echo(existing, DANIEL_ECHOES)
    save_echo('daniel', existing)
    print('Daniel 6-8 echo written (ch 8 added).')

if __name__ == '__main__':
    main()
