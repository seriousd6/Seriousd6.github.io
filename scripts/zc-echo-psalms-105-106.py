"""
Echo data — Psalms chapters 105–106 (both missing)
Run: python3 scripts/zc-echo-psalms-105-106.py

Key connections across the great historical Psalms:
- Ps 105:8: "He remembers his covenant forever, the promise he made for a thousand
  generations" → Luke 1:72-73 (Zechariah's benedictus: God remembered his covenant
  with Abraham, fulfilled in Christ's coming) / Gal 3:16 (the promises spoken to
  Abraham and to his seed = Christ).
- Ps 105:26: "He sent Moses his servant, and Aaron whom he had chosen" →
  Heb 3:3 — Moses the sent-servant type is surpassed by Christ the Son.
- Ps 105:39: "He spread a cloud as a covering; fire to give light at night" →
  John 8:12 — Christ is the light of the world; the pillar of fire was the type.
- Ps 105:40: "He gave them bread from heaven in abundance" → John 6:32 (not Moses
  but my Father gives the true bread — and I am that bread).
- Ps 105:41: "He opened the rock and water gushed out" → 1 Cor 10:4 (the rock
  was Christ).
- Ps 106:10: "He saved them from the hand of the foe" → Luke 1:74 (Zechariah's
  Benedictus applies this directly to the Christ-event).
- Ps 106:23: "Had not Moses stood in the breach" → Heb 7:25 / 1 Tim 2:5 —
  Christ the greater intercessor who always lives to intercede.
- Ps 106:37: "They sacrificed their sons and daughters to demons" → 1 Cor 10:20
  (Paul cites this OT theology of idolatry as operative in NT).
- Ps 106:48: "Praise be to the LORD from everlasting to everlasting; Amen!" →
  Rev 5:13-14 (heavenly 'Amen' directed to the Lamb who shares the throne).
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

# INTENT: Echo data for Psalms 105–106 — the two great historical Psalms rehearsing
#   the patriarchal promise and Exodus (Ps 105) and Israel's wilderness failures (Ps 106),
#   with NT fulfillments in the Benedictus (Luke 1:72-74 applies both psalms to Christ),
#   the true bread from heaven (John 6:32), the rock as Christ (1 Cor 10:4), and Christ
#   as the greater Moses who stands in the breach permanently (Heb 7:25).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in [105,106]])" should show non-zero for both.

PSALMS_ECHOES = {
  "105": {
    "8": [
      {
        "type": "fulfillment",
        "target": "Luke 1:72",
        "note": "He remembers his covenant forever, the word he commanded for a thousand generations — 'to show mercy to our ancestors and to remember his holy covenant, the oath he swore to our father Abraham' (Luke 1:72-73). Zechariah's Benedictus opens by citing the exact claim of Psalm 105:8: God has remembered his covenant forever — and declares that this remembering is fulfilled in the birth of Christ. The covenant kept 'for a thousand generations' is the covenant ratified at the cross and inaugurated in the manger."
      },
      {
        "type": "fulfillment",
        "target": "Gal 3:16",
        "note": "The promise he made for a thousand generations — the covenant he confirmed with Abraham — 'the promises were spoken to Abraham and to his seed. Scripture does not say \"and to seeds,\" meaning many people, but \"and to your seed,\" meaning one person, who is Christ' (Gal 3:16). The everlasting covenant promise remembered in Psalm 105:8 is the covenant whose singular beneficiary Paul identifies as Christ. The 'thousand generations' for whom the covenant was secured are those who are in Christ, Abraham's singular seed."
      }
    ],
    "26": [
      {
        "type": "type",
        "target": "Heb 3:3",
        "note": "He sent Moses his servant, Aaron whom he had chosen — 'Jesus has been found worthy of greater honor than Moses, just as the builder of a house has greater honor than the house itself' (Heb 3:3). The sending of Moses as servant (Ps 105:26) is the OT type that Hebrews uses to define Christ's surpassing greatness. Moses was a faithful servant in God's house; Christ is faithful as a Son over God's house (Heb 3:5-6). The sent-servant Moses anticipated the sent-Son Jesus — greater in the same ratio as the builder exceeds the house."
      }
    ],
    "39": [
      {
        "type": "type",
        "target": "John 8:12",
        "note": "He spread a cloud as a covering, and fire to give light at night — 'I am the light of the world. Whoever follows me will never walk in darkness, but will have the light of life' (John 8:12). The pillar of cloud and fire guiding Israel through the wilderness (Ps 105:39) is the type of Christ as the light of the world. Israel followed a visible fire through physical darkness; those who follow Christ receive the light of life through spiritual darkness. Acts 1:9: a cloud received him at the ascension — the glory-cloud of the wilderness returns at the end of his earthly ministry."
      }
    ],
    "40": [
      {
        "type": "fulfillment",
        "target": "John 6:32",
        "note": "They asked and he brought them quail; he gave them bread from heaven in abundance — 'It is not Moses who has given you the bread from heaven, but it is my Father who gives you the true bread from heaven. For the bread of God is the bread that comes down from heaven and gives life to the world' (John 6:32-33). Jesus corrects the attribution: the bread in Psalm 105:40 was not Moses's gift but the Father's. And the true bread from heaven is not manna that perishes but Christ himself — the one who gives life to the world, whom the manna typified."
      }
    ],
    "41": [
      {
        "type": "type",
        "target": "1 Cor 10:4",
        "note": "He opened the rock and water gushed out; it flowed like a river in the desert — 'they drank from the spiritual rock that accompanied them, and that rock was Christ' (1 Cor 10:4). Paul identifies the water-giving rock of Psalm 105:41 as Christ. The physical rock that produced water in the desert was a type of the spiritual rock who is the source of living water for his people. John 4:14: 'the water I give them will become in them a spring of water welling up to eternal life' — Christ is the opened rock from whom living water flows permanently."
      }
    ]
  },
  "106": {
    "10": [
      {
        "type": "fulfillment",
        "target": "Luke 1:74",
        "note": "He saved them from the hand of the foe; he redeemed them from the hand of the enemy — 'to rescue us from the hand of our enemies, and to enable us to serve him without fear' (Luke 1:74). Zechariah's Benedictus directly applies Psalm 106:10's exodus-redemption language to Christ's coming. The saving from the enemy's hand that Psalm 106 celebrates as the pattern of God's faithfulness becomes, in the Benedictus, the announcement that this ultimate rescue has arrived in the Messiah — liberation from spiritual enemies (sin, death, the devil) enabling fearless service."
      }
    ],
    "23": [
      {
        "type": "type",
        "target": "Heb 7:25",
        "note": "He would have destroyed them — had not Moses, his chosen one, stood in the breach before him to keep his wrath from destroying them — 'therefore he is able to save completely those who come to God through him, because he always lives to intercede for them' (Heb 7:25). Moses standing in the breach (Ps 106:23) is the supreme OT type of intercession: one man's prayer holding back divine wrath from the entire nation. Christ is the greater Moses who permanently stands in the breach — not for a single crisis but always, his life perpetually interceding for those who come to God through him."
      },
      {
        "type": "type",
        "target": "1 Tim 2:5",
        "note": "Had not Moses, his chosen one, stood in the breach before him — 'for there is one God and one mediator between God and mankind, the man Christ Jesus, who gave himself as a ransom for all people' (1 Tim 2:5). Moses the intercessor standing between God's wrath and Israel (Ps 106:23) is fulfilled in Christ the one mediator who stands between God and all humanity. The breach Moses filled temporarily with prayer, Christ fills permanently with his own sacrifice — the ransom that settles the wrath Moses could only delay."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "1 Cor 10:20",
        "note": "They sacrificed their sons and daughters to demons — 'the sacrifices of pagans are offered to demons, not to God, and I do not want you to be participants with demons' (1 Cor 10:20). Paul's warning against idol-feast participation draws on Psalm 106:37's theological interpretation of Canaanite child sacrifice: the real recipients of sacrifices offered to idols are demons. The Psalm's identification of idolatry as demonic worship is the foundation of Paul's NT argument about idol-meat — the same spiritual reality is operative in every era."
      }
    ],
    "48": [
      {
        "type": "allusion",
        "target": "Rev 5:13",
        "note": "Praise be to the LORD, the God of Israel, from everlasting to everlasting; let all the people say, 'Amen!' Praise the LORD — 'then I heard every creature in heaven and on earth and under the earth and on the sea, and all that is in them, saying: \"To him who sits on the throne and to the Lamb be praise and honor and glory and power, for ever and ever!\" The four living creatures said, \"Amen\"' (Rev 5:13-14). The everlasting doxology that closes Book IV of the Psalter (Ps 106:48) is the form that Revelation's universal worship takes. The 'Amen' that all the people say echoes through the four living creatures — the same 'Amen' now directed to the Lamb who shares the throne."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['105', '106']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 105-106 echoes complete.")

if __name__ == '__main__':
    main()
