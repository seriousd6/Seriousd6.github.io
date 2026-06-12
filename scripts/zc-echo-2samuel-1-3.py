"""
Echo Commentary — 2 Samuel chapters 1–3
Run: python3 scripts/zc-echo-2samuel-1-3.py

Ch1: David's lament over Saul and Jonathan — the anointed's grief for the fallen;
     Jonathan's covenant love surpassing human bonds
Ch2: David anointed at Hebron — the partial-then-full anointing pattern;
     the long war between Saul's house and David's house begins
Ch3: David grows stronger while Saul's house weakens — kingdom growth pattern;
     Abner's oracle: 'by the hand of my servant David I will save my people'

Key OT↔NT echo connections:
- 1:19,25,27 → Luke 19:41-44: lament of the king-Messiah over the fallen/rejected
- 1:26 → John 15:13: covenant love surpassing human love
- 3:1 → 1 Cor 15:25: the growing-stronger messianic kingdom
- 3:18 → Acts 4:12 / Isa 42-53: servant David as type of the servant Messiah
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
  "1": {
    "19": [
      {"type": "allusion", "target": "Luke 19:41-44", "note": "David's lament over Saul and Jonathan — 'How the mighty have fallen!' (ʾêḵ nāpəlû gibbôrîm) — is the OT archetype of the anointed king grieving over his fallen people. Jesus weeps over Jerusalem (Luke 19:41: 'when he drew near and saw the city, he wept over it') in the same lament pattern: the Messiah-king mourning what his people's rejection of his anointing will bring upon them. Both laments arise from the same theological source — covenant love confronting covenant failure."},
      {"type": "allusion", "target": "Matt 23:37", "note": "David's lament 'How the mighty have fallen' — sung publicly, taught to Judah (v18) — establishes the pattern of the anointed who turns personal grief into corporate instruction. Jesus's lament over Jerusalem ('O Jerusalem, Jerusalem, the city that kills the prophets... How often would I have gathered your children together as a hen gathers her brood under her wings, and you were not willing!' Matt 23:37) is the Davidic lament pattern brought to its full Christological expression: the king-Messiah weeping over the city that will reject him."}
    ],
    "26": [
      {"type": "allusion", "target": "John 15:13", "note": "David's eulogy for Jonathan — 'your love to me was extraordinary, surpassing the love of women' — is the OT measure of covenant love at its highest. Jesus's statement 'greater love has no one than this, that someone lay down his life for his friends' (John 15:13) is the NT definition of the same quality: the love that exceeds all ordinary human bonds because it proceeds from covenant commitment rather than instinct. Jonathan's love for David was precisely this — a love expressed by giving up his throne-claim, his armor, his future — and David's lament recognizes it as the highest form of human love the OT narrative contains."},
      {"type": "allusion", "target": "Rom 5:7-8", "note": "Jonathan's love for David surpassed ordinary human love — he did not merely love David as a fellow warrior but as the anointed one whose kingdom was being established at the cost of Jonathan's own. Paul's contrast in Rom 5:7-8 ('scarcely for a righteous person will one die... but God shows his love for us in that while we were still sinners, Christ died for us') builds on this OT understanding of extraordinary love: the love that gives what it did not have to give, for one who had no claim on it."}
    ]
  },
  "2": {
    "4": [
      {"type": "allusion", "target": "Acts 2:36", "note": "David is anointed king over Judah at Hebron — but the full kingdom over all Israel comes only in 2 Sam 5. The two-stage anointing pattern (Judah first, then all Israel) mirrors the NT's 'already/not yet' structure of Christ's kingship: at the resurrection, God has 'made him both Lord and Christ' (Acts 2:36), but the full subjection of all things awaits the consummation (1 Cor 15:24-28). The Hebron anointing is the type of the resurrection-exaltation; the Jerusalem anointing over all Israel is the type of the parousia."},
      {"type": "allusion", "target": "1 Cor 15:24-28", "note": "David's partial reign at Hebron during the long war with the house of Saul anticipates the NT picture of Christ reigning now while enemies are being progressively subdued: 'For he must reign until he has put all his enemies under his feet' (1 Cor 15:25). The conflict between the house of Saul and the house of David (v1: 'there was a long war') is the narrative type of the ongoing conflict between the old order and the messianic kingdom."}
    ]
  },
  "3": {
    "1": [
      {"type": "allusion", "target": "1 Cor 15:25", "note": "The summary of 2 Sam 3:1 — 'the house of David grew stronger and stronger, while the house of Saul became weaker and weaker' — is the narrative expression of the kingdom-growth pattern. 1 Cor 15:25 ('he must reign until he has put all his enemies under his feet') describes the same dynamic: the messianic kingdom progressively overcoming all opposition until the final subjection. The 'long war' between the two houses is the type of the church age, in which the kingdom of Christ grows to ultimate triumph against a weakening opposition."},
      {"type": "allusion", "target": "Dan 2:34-35", "note": "The growing strength of David's house against the weakness of Saul's is also the type of the stone in Daniel 2:34-35: 'a stone was cut out by no human hand, and it struck the image... but the stone that struck the image became a great mountain and filled the whole earth.' The messianic kingdom that begins small and apparently weak becomes the dominant power — the same pattern as David's house growing stronger while the old regime weakens."}
    ],
    "18": [
      {"type": "allusion", "target": "Acts 4:12", "note": "Abner's acknowledgment to the elders of Israel — 'YHWH has spoken of David, saying, By the hand of my servant David I will save my people Israel from the hand of the Philistines and from the hand of all their enemies' — is the OT commission of the servant-king as savior of YHWH's people. Peter's proclamation in Acts 4:12 — 'there is salvation in no one else, for there is no other name under heaven given among men by which we must be saved' — is the NT fulfillment: the one through whose hand YHWH saves is Jesus, the ultimate servant-David."},
      {"type": "allusion", "target": "Isa 42:1", "note": "The title 'my servant David' (ʿabdî dāwiḏ) used by YHWH in Abner's oracle connects to the Isaianic Servant Songs (Isa 42:1: 'Behold my servant, whom I uphold'; 49:3: 'you are my servant, Israel, in whom I will be glorified'). The trajectory from the historical David to the eschatological Servant-Messiah is precisely this: the ʿebed YHWH who saves the people runs through David typologically and arrives in Jesus, who embodies both the Davidic kingship and the Isaianic servanthood that saves by suffering."}
    ]
  }
}

def main():
    e = load_echo('2samuel')
    merge_echo(e, ECHO)
    save_echo('2samuel', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'2samuel echo: wrote {count} verses across ch 1-3')

if __name__ == '__main__':
    main()
