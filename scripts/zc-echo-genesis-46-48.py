"""
Echo Layer — Genesis chapters 46–48
Run: python3 scripts/zc-echo-genesis-46-48.py

Key echo trajectories:
- Gen 46:3-4: 'Do not be afraid to go down to Egypt; I will bring you up again'
  → Exod 3:8 (descent-then-ascent pattern); Eph 4:8-9 (Christ descended then ascended);
  the Exodus as redemption archetype
- Gen 46:27: 70 souls go down to Egypt → Deut 10:22; Acts 7:14 (covenant remnant
  preserved through exile)
- Gen 47:7-9: Jacob blesses Pharaoh; sojourner speech → Heb 7:7; Heb 11:13-16;
  1 Pet 2:11 (strangers and pilgrims)
- Gen 48:5: adoption of Joseph's sons → Eph 1:5 (adoption as sons through Christ)
- Gen 48:15-16: 'the God who has been my shepherd... the angel who redeemed me'
  → Ps 23; John 10:11 (shepherd); the Angel-Redeemer → christophany; Isa 63:9
- Gen 48:17-20: crossed hands (Ephraim over Manasseh) → the younger-over-elder
  reversal pattern (Rom 9:10-13; 1 Cor 1:27-28; Matt 23:12)
- Existing ch 47 echo v31 [allusion] Heb 11:21 preserved by merge_echo.
- No parallels data to absorb for chs 46-48.
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
  "46": {
    "3": [
      {"type": "shadow", "target": "Isa 43:2", "note": "'I am God, the God of your father. Do not be afraid to go down to Egypt' (46:3) — the divine 'Fear not' formula accompanies every major covenant-transition in the OT (Gen 15:1; 21:17; 26:24; 28:13; Josh 1:9; Isa 41:10; 43:1-3). Isa 43:2 ('when you pass through the waters, I will be with you') is the prophetic crystallization of this pattern: the covenant God accompanies his people into the very worst of circumstances, not merely consoling from a distance but going down with them."}
    ],
    "4": [
      {"type": "shadow", "target": "Exod 3:8", "note": "'I myself will go down with you to Egypt, and I will also bring you up again' (46:4) — the descent-then-ascent covenant promise is the seed of the Exodus narrative. Exod 3:8 fulfills the 'bring up' promise explicitly: 'I have come down to deliver them out of the hand of the Egyptians and to bring them up out of that land.' Paul applies the descent-ascent pattern to Christ in Eph 4:8-10: 'when he ascended on high... in saying he ascended, what does it mean but that he had also descended?'"},
      {"type": "shadow", "target": "Eph 4:9", "note": "'I myself will go down with you to Egypt, and I will also bring you up again' (46:4) — the divine pattern of voluntary descent to rescue and subsequent ascent with the rescued. Eph 4:8-9 applies this to Christ's incarnation and ascension, citing Ps 68:18: he descended into the lower regions of the earth and then ascended far above all the heavens, that he might fill all things. Jacob's descent to Egypt and promised ascent is the patriarchal type of the cosmic descent and ascent of the Son."}
    ],
    "27": [
      {"type": "shadow", "target": "Deut 10:22", "note": "Seventy persons from Jacob's family went down to Egypt (46:27) — the founding number of the covenant community in exile. Deut 10:22 recalls this explicitly: 'Your fathers went down to Egypt seventy persons, and now the LORD your God has made you as numerous as the stars of heaven.' The seventy become the nation; the nation becomes the church of many nations. Acts 7:14 gives the LXX count of seventy-five, showing that the number itself became a theological marker of the preserved remnant."}
    ]
  },
  "47": {
    "7": [
      {"type": "shadow", "target": "Heb 7:7", "note": "Jacob blessed Pharaoh (47:7) — the covenant-bearer (the weaker and older shepherd) blesses the world's most powerful ruler. Heb 7:7 states the principle: 'it is beyond dispute that the inferior is blessed by the superior.' The paradox is that Jacob, a nomadic alien with nothing in worldly terms, carries the superior covenant blessing that Pharaoh cannot confer on himself. The same paradox governs Christian mission: those who carry the gospel carry a blessing the world's powerful cannot provide for themselves (1 Cor 1:27-28)."}
    ],
    "9": [
      {"type": "shadow", "target": "Heb 11:13", "note": "'The days of the years of my sojourning are 130 years. Few and evil have been the days of the years of my life' (47:9) — Jacob's self-description as a sojourner (<em>māgôr</em>) at death's approach echoes the confession of all the patriarchs. Heb 11:13-16: 'These all died in faith, not having received the things promised, but having seen them and greeted them from afar, and having acknowledged that they were strangers and exiles on the earth... they desire a better country, that is, a heavenly one.' Peter applies the same identity to the church: 'sojourners and exiles' (1 Pet 2:11)."}
    ]
  },
  "48": {
    "5": [
      {"type": "shadow", "target": "Eph 1:5", "note": "'Your two sons, who were born to you in the land of Egypt before I came to you in Egypt, are mine; Ephraim and Manasseh shall be mine, as Reuben and Simeon are' (48:5) — Jacob adopts Joseph's Gentile-born sons as his own, granting them full inheritance rights as firstborn. Eph 1:5 applies the adoption pattern to the church: 'he predestined us for adoption to himself as sons through Jesus Christ.' The legal inclusion of the otherwise-excluded into full covenant inheritance is the Joseph-narrative type of what God does in Christ."}
    ],
    "15": [
      {"type": "shadow", "target": "John 10:11", "note": "Jacob blesses Joseph with the formula: 'the God before whom my fathers Abraham and Isaac walked, the God who has been my shepherd all my life long to this day' (48:15) — the accumulated covenant history distilled into the shepherd metaphor. Ps 23 develops this metaphor; John 10:11 fulfills it: 'I am the good shepherd. The good shepherd lays down his life for the sheep.' The God who shepherded Jacob through Haran, Egypt, and wrestling at Peniel is the God who becomes the shepherd incarnate."},
      {"type": "shadow", "target": "Isa 63:9", "note": "'The angel who has redeemed me from all evil' (<em>hammalʾāk haggōʾēl ʾōtî</em>, 48:16) — Jacob invokes the Angel-Redeemer alongside God the Father (48:15-16), treating them as co-agents of his blessing. Isa 63:9 ('the angel of his presence saved them; in his love and in his pity he redeemed them') applies the same Angel-Redeemer to the Exodus. The triad in 48:15-16 — God before whom the fathers walked, God who shepherded, the angel who redeemed — maps onto John 1:1-18's language for the Word who was with God, was God, and became flesh."}
    ],
    "17": [
      {"type": "shadow", "target": "Rom 9:11", "note": "Jacob deliberately crosses his hands to lay his right hand on Ephraim the younger, giving the greater blessing to the second-born over the firstborn Manasseh (48:17-19). The younger-over-elder reversal is the repeated OT pattern that Paul cites in Rom 9:11-13 to illustrate divine elective purpose: 'though they were not yet born and had done nothing either good or bad — in order that God's purpose of election might continue, not because of works but because of him who calls — she was told, the older will serve the younger.' Abel, Isaac, Jacob, Joseph, Judah, Ephraim — the pattern is structural, not incidental."},
      {"type": "shadow", "target": "Matt 23:12", "note": "Jacob's crossing of his hands to prefer the younger (48:17-20) enacts the reversal principle Jesus articulates: 'whoever exalts himself will be humbled, and whoever humbles himself will be exalted' (Matt 23:12). The persistent OT pattern — the younger, the weaker, the less-expected inherits the covenant blessing — is the structural foundation for the Beatitudes (Matt 5:3-12) and the consistent NT claim that God's power is displayed in weakness (1 Cor 1:27-29; 2 Cor 12:9)."}
    ],
    "19": [
      {"type": "shadow", "target": "1 Cor 1:27", "note": "Manasseh the firstborn is set aside for Ephraim the younger, who will be 'greater' (48:19) and whose name becomes the blessing-formula for all Israel. This completes the OT series of unexpected elections: Abel over Cain, Isaac over Ishmael, Jacob over Esau, Judah over Reuben, Ephraim over Manasseh. Paul identifies the theological principle in 1 Cor 1:27-28: 'God chose what is weak in the world to shame the strong; God chose what is low and despised in the world, even things that are not, to bring to nothing things that are.'"}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    for ch in [46, 47, 48]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    total = len(result)
    print(f'  Genesis total: {total} chapters with echo data')
    print('Genesis 46-48 echoes written.')

if __name__ == '__main__':
    main()
