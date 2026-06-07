"""
MKT Echo — Genesis chapters 10–12
Run: python3 scripts/zc-echo-genesis-10-12.py

Source data used:
- data/interlinear/genesis.json
- data/parallels/genesis.json (absorbed: ch 12 v1 already in echoes; ch 12 v3 already in echoes)
- data/echoes/genesis.json (merge_echo is non-destructive; ch 12 entries pre-existing)

Key decisions:
- Ch 10 (Table of Nations): focus on Nimrod/Babel seed (forward to Rev 17–18) and the
  "all nations" framework taken up in Acts 17:26 and Rev 7:9; most genealogical entries
  carry the theme of covenant-fulfillment (all nations structured before Abram's call)
- Ch 11 (Babel + Shem genealogy): Pentecost reversal (Acts 2) is the primary echo for
  the language-confusion passage; Babel's tower project points forward to Rev 17–18
  Babylon typology; the Shem-to-Terah genealogy (vv. 10–26) is in Jesus's Lucan line
- Ch 12: pre-existing entries from earlier script run (Heb 11:8, Acts 7:2-4, Gal 3:8);
  script adds nothing to ch 12 — merge_echo will skip pre-existing keys
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

GENESIS_ECHOES = {
  "10": {
    "1": [
      {"type": "theme", "target": "Acts 17:26",
       "note": "The Table of Nations (Gen 10) is the canonical background to Paul's Areopagus declaration: 'From one man he made all the nations (panta ta ethnē) to live on all the face of the earth, having determined allotted periods and the boundaries of their dwelling place.' Paul draws directly on the Noahic-nations framework to establish that all ethnic diversity descends from a single humanity made for God."},
      {"type": "shadow", "target": "Rev 7:9",
       "note": "The 70 nations of the Table of Nations (counted in Hebrew tradition as 70 from Shem, Ham, and Japheth) are the world that every-nation-tribe-people-language of Rev 7:9 reverses: where Genesis 10 describes the scattering into peoples, Revelation's great multitude is the eschatological gathering of every scattered people before the Lamb."}
    ],
    "5": [
      {"type": "shadow", "target": "Acts 2:8",
       "note": "The coastland peoples spread 'each with his own language, by their clans, in their nations' (Gen 10:5) — an anticipation of the Babel fragmentation (ch. 11) and its eschatological reversal at Pentecost, where each person heard the apostles speaking 'in his own language' (glōssē); the Spirit at Pentecost undoes what the nations' scattering established."}
    ],
    "8": [
      {"type": "shadow", "target": "Rev 17:5",
       "note": "Nimrod, 'a mighty hunter before the LORD' and the first kingdom-builder of Babel (Gen 10:8-10), is the OT seed of the Babylon-the-Great typology. His founding of Babel (the city of confusion, ch. 11) becomes the enduring symbol of human empire against God — Revelation's Babylon is Nimrod's project at its eschatological extreme."}
    ],
    "10": [
      {"type": "allusion", "target": "Rev 17:5",
       "note": "Nimrod's first kingdom was 'Babel, Erech, Akkad, and Calneh, in the land of Shinar' (Gen 10:10). The name Babel (Babylon in Greek) becomes the NT's code for the final human empire opposed to God: Rev 17:5 labels 'Babylon the Great' as the mother of harlots. The river begins here in Gen 10 — Nimrod's Shinar, the Tower of Babel (ch. 11), Israel's captivity, and Rev 18's lament are all within the same Babylon typology."}
    ],
    "25": [
      {"type": "theme", "target": "Luke 3:35",
       "note": "Eber's son Peleg ('for in his days the earth was divided,' Gen 10:25) is the pivot point of the Table of Nations — the division of peoples happens in Peleg's era (corresponding to Babel, Gen 11). Peleg appears in Luke's genealogy of Jesus (Luke 3:35), tracing the Savior's lineage through this very point of division, as if to mark him as the one who will gather what Peleg's era scattered."}
    ],
    "32": [
      {"type": "theme", "target": "Gal 3:8",
       "note": "The Table of Nations concludes: 'From these the nations spread abroad on the earth after the flood' (Gen 10:32). This founding dispersal of the nations is the backdrop against which God calls Abram (Gen 12:1-3) to be the channel through whom all these nations will be blessed. Paul's citation of Gen 12:3 in Gal 3:8 ('the Scripture foresaw that God would justify the Gentiles by faith') makes sense only against the Table of Nations — God was always working toward all these nations."}
    ]
  },
  "11": {
    "1": [
      {"type": "shadow", "target": "Acts 2:6",
       "note": "The pre-Babel world had 'one language and the same words' (Gen 11:1) — linguistic unity marking undivided humanity. Pentecost partially reverses this: where Babel shattered the one language into many (Gen 11:7), the Spirit at Pentecost did not restore a single language but enabled each to hear in their own language (Acts 2:6-8), a deeper unity-in-diversity that prefigures Rev 7:9's eschatological gathering."}
    ],
    "4": [
      {"type": "shadow", "target": "Rev 18:10",
       "note": "'Let us build ourselves a city and a tower with its top in the heavens, and let us make a name for ourselves, lest we be dispersed over the face of the whole earth' (Gen 11:4) — the Babel project is the archetype of every human city that exalts itself against God. Revelation's lament over Babylon ('Alas, alas, O great city Babylon, you mighty city!' Rev 18:10) is the final reckoning with what Babel began: the city built to make a name, brought down in an hour."}
    ],
    "7": [
      {"type": "shadow", "target": "Acts 2:4",
       "note": "YHWH's verdict at Babel — 'Come, let us go down and there confuse their language, so that they may not understand one another's speech' (Gen 11:7) — is the founding act of human ethnic and linguistic division. The Pentecost reversal is exact: where YHWH 'confused' (bālal) Babel, the Spirit at Pentecost gave speech that each person understood; what was scattered is being regathered through the gospel (Acts 2:4-8)."}
    ],
    "9": [
      {"type": "allusion", "target": "Rev 14:8",
       "note": "Babel — 'because there YHWH confused (bālal) the language of all the earth, and from there YHWH dispersed them over the face of all the earth' — gives its name to Babylon, which the prophets (Isa 13; Jer 50-51) and Revelation use as the symbol of human empire's end. Revelation's 'Fallen, fallen is Babylon the great' (Rev 14:8; 18:2) is the final judgment on what the builders of Babel set in motion."},
      {"type": "allusion", "target": "1 Pet 5:13",
       "note": "Peter's closing greeting 'She who is at Babylon, who is likewise chosen, sends you greetings' (1 Pet 5:13) uses Babel/Babylon as a code name for Rome — showing that Babel became a canonical type for every empire that sets itself against the people of God. The typology began in Gen 11:9 and was still alive in Peter's use of it decades after Christ's ascension."}
    ],
    "10": [
      {"type": "theme", "target": "Luke 3:36",
       "note": "The Shem-to-Terah genealogy (Gen 11:10-26) — Shem, Arpachshad, Shelah, Eber, Peleg, Reu, Serug, Nahor, Terah — is reproduced in Luke's genealogy of Jesus (Luke 3:35-36), demonstrating that the Lucan Christ comes through the Shemite covenant line that runs from Noah's son Shem through to Abraham. The genealogy is not merely biographical; it traces the covenant line forward toward the seed of Abraham."}
    ],
    "26": [
      {"type": "fulfillment", "target": "Acts 7:2",
       "note": "Terah fathered Abram, Nahor, and Haran (Gen 11:26-27), setting up the Abrahamic call of ch. 12. Stephen's speech (Acts 7:2) dates the divine appearance to Abraham to his time in Mesopotamia before he settled in Haran — identifying the God who called Abraham as the God of glory, the covenant-keeping God who works outside the land, as he will work among the Gentile nations."}
    ],
    "31": [
      {"type": "allusion", "target": "Heb 11:8",
       "note": "Terah took Abram, Lot, and Sarai from Ur of the Chaldeans to go to Canaan but settled in Haran (Gen 11:31). The journey begun by Terah that he did not complete becomes the journey Abraham completes by faith (Heb 11:8: 'he went out, not knowing where he was going'). The staging of the call at Haran (after the aborted journey from Ur) underscores the point that Abraham is not acting on his own initiative but responding to divine command."}
    ]
  }
}


def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)
    print('Genesis 10-12 echoes written.')

if __name__ == '__main__':
    main()
