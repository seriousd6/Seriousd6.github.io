"""
Echo Layer — Daniel chapters 3–5
Run: python3 scripts/zc-echo-daniel-3-5-fill.py

Key decisions:
- Dan 3:25 "son of the gods": classified as allusion (Christophany tradition) not type,
  since the Aramaic bar-elahin is pagan speech and NT never cites this verse directly.
- Dan 4:3/34: "eternal kingdom" → Rev 11:15 connection is genuine verbal echo.
- Dan 5:27 "Tekel": allusion to eschatological judgment (Rev 20:12; 2 Cor 5:10).
- Dan 5:30-31: Babylon's overnight fall → Rev 18:10 (shadow-level connection).
- ch4 and ch5 use kingdom and judgment themes that NT authors clearly draw on.
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
  "3": {
    "16": [
      {"type": "allusion", "target": "Heb 11:33-34", "note": "Shadrach, Meshach, and Abednego shutting the mouths of lions and quenching the power of fire are named in the faith hall of fame (Heb 11:33-34) as paradigm instances of faith that overcomes the impossible — their refusal to recant under capital threat models the witness-unto-death faith the NT commends."}
    ],
    "25": [
      {"type": "allusion", "target": "John 8:58", "note": "The fourth figure 'like a son of the gods' (Aram. bar-elahin), appearing to deliver the faithful from the furnace, resonates with early Christian readings of a pre-incarnate divine presence — Christ as the one who accompanies his people through fire before the incarnation, consistent with his claim of existence before Abraham (John 8:58) and the typology of the angel of YHWH throughout the OT."}
    ],
    "28": [
      {"type": "theme", "target": "Acts 4:19-20", "note": "Nebuchadnezzar's acknowledgment that no god can rescue like this (v.28-29) inverts to its positive form in the apostolic declaration that they must obey God rather than men — both scenes dramatize the collision between pagan state power and exclusive allegiance to the one God, with miraculous vindication establishing the claim."}
    ]
  },
  "4": {
    "3": [
      {"type": "allusion", "target": "Rev 11:15", "note": "Nebuchadnezzar's doxology 'his kingdom is an eternal kingdom and his dominion is from generation to generation' (v.3, echoed in v.34) is one of the OT formulations underlying Rev 11:15, where the heavenly voices declare that the kingdom of the world has become the kingdom of our Lord and of his Christ, who shall reign for ever and ever — the eternal kingdom language migrates from the Babylonian king's forced confession to the consummation declaration."}
    ],
    "17": [
      {"type": "theme", "target": "Luke 1:32-33", "note": "The repeated 'decree of the Most High' (vv.17, 24, 25, 32) asserting that the Most High rules the kingdom of men and gives it to whom he will underlies the angelic announcement to Mary that her son will be given 'the throne of his father David' and will reign over the house of Jacob forever — the universal sovereignty of the Most High passes to the Son of the Most High."}
    ],
    "34": [
      {"type": "allusion", "target": "1 Pet 5:5-6", "note": "Nebuchadnezzar is stripped of reason, driven out to live like an animal, and then restored when he lifts his eyes to heaven and blesses the Most High — the pattern of divine humiliation leading to restoration and exaltation is the same logic 1 Pet 5:5-6 draws on: 'God opposes the proud but gives grace to the humble; humble yourselves therefore under the mighty hand of God, that he may exalt you in due time.'"}
    ]
  },
  "5": {
    "5": [
      {"type": "shadow", "target": "Rev 20:11-15", "note": "The writing hand appearing at Belshazzar's feast — invisible, unpreventable, inscribing a verdict he cannot escape — is a shadow of the eschatological judgment scene in Rev 20, where books are opened and the dead are judged by what is written according to what they had done; both scenes enact the moment divine accounting breaks into human celebration."}
    ],
    "27": [
      {"type": "allusion", "target": "2 Cor 5:10", "note": "'Tekel — you have been weighed in the balances and found wanting' anticipates the NT theme of eschatological weighing: Paul's declaration that all must appear before the judgment seat of Christ draws on the same moral-accounting metaphor, but with Christ as the standard rather than the Mosaic law; the Daniel verdict shows what happens when the measure is YHWH's righteousness and the king comes up short."},
      {"type": "allusion", "target": "Rev 20:12", "note": "The inscription of verdict against Belshazzar anticipates the opening of books at the great white throne judgment (Rev 20:12), where the dead are judged according to what was written — in Daniel the verdict is immediate and personal; in Revelation it is cosmic and final, but the logic of written divine accounting is the same."}
    ],
    "30": [
      {"type": "shadow", "target": "Rev 18:10", "note": "Belshazzar's death and the fall of Babylon in a single night (v.30) is one of the historical templates behind Revelation's Babylon oracles: Rev 18:10 cries 'Alas, alas, for the great city Babylon! For in a single hour your judgment has come' — the overnight collapse of the historical Babylon imprints the grammar of sudden divine judgment on the Revelation vision of every empire that exalts itself against God."}
    ]
  }
}

def main():
    existing = load_echo('daniel')
    merge_echo(existing, DANIEL_ECHOES)
    save_echo('daniel', existing)
    print('Daniel 3-5 echoes written.')

if __name__ == '__main__':
    main()
