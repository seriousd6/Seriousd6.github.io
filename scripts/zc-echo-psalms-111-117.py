"""
Echo data — Psalms chapters 111–117 (gap-fill: chs 111, 113, 114, 115 missing; 112, 116, 117 already present)
Run: python3 scripts/zc-echo-psalms-111-117.py

Key connections across the Egyptian Hallel (Ps 113–118) and surrounding psalms:
- Ps 111–118 are the Egyptian Hallel, sung at Passover. Matt 26:30 / Mark 14:26:
  "when they had sung a hymn" — Jesus and the disciples sang Psalms 113–118 at the
  Last Supper. Every verse of these Psalms was in the room at that meal.
- Ps 111:9: "He sent redemption to his people; he ordained his covenant forever.
  Holy and awesome is his name" → Rev 15:4 (who will not fear you, Lord, and glorify
  your name? for you alone are holy) / Phil 2:9-11 (name above every name).
- Ps 111:10: "The fear of the LORD is the beginning of wisdom" → Col 2:3 (in Christ
  are hidden all the treasures of wisdom and knowledge).
- Ps 113:7-8: "He raises the poor from the dust and lifts the needy from the ash heap"
  → Luke 1:52-53 (Magnificat: he has lifted up the humble and filled the hungry).
- Ps 113:9: "He settles the childless woman in her home as a happy mother" →
  Luke 1:36 (Elizabeth, barren, now six months pregnant — pattern of divine reversal).
- Ps 114:1-2: "When Israel came out of Egypt... Judah became God's sanctuary" →
  1 Pet 2:9 (you are a holy nation, God's special possession) / Heb 3:6.
- Ps 114:8: "Who turned the rock into a pool, the hard rock into springs of water" →
  1 Cor 10:4 (the rock was Christ).
- Ps 115:4-7: Idols of silver and gold — "those who make them will be like them" →
  Acts 17:29 (we should not think the divine being is like gold, silver, stone).
- Ps 115:17: "It is not the dead who praise the LORD" → 1 Cor 15:20 (Christ the
  firstfruits of those who have fallen asleep — the resurrection answers what the
  Psalm cannot yet see).
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

# INTENT: Echo data for Psalms 111, 113, 114, 115 — the Egyptian Hallel cluster
#   (Ps 113–118) sung at Passover and at the Last Supper (Matt 26:30); NT connections
#   include the Magnificat citing Ps 113:7-9 (Luke 1:52-53), the rock-as-Christ
#   (Ps 114:8 → 1 Cor 10:4), idol polemic (Ps 115 → Acts 17:29), and the wisdom
#   of God hidden in Christ (Ps 111:10 → Col 2:3).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in [111,113,114,115]])" should show non-zero for all four.

PSALMS_ECHOES = {
  "111": {
    "9": [
      {
        "type": "fulfillment",
        "target": "Phil 2:9",
        "note": "He sent redemption to his people; he ordained his covenant forever. Holy and awesome is his name — 'therefore God exalted him to the highest place and gave him the name that is above every name, that at the name of Jesus every knee should bow' (Phil 2:9-11). The covenant sent as redemption and the holy name that Psalm 111:9 celebrates find their NT disclosure in Christ: the redemption is his atoning death, the covenant is the new covenant in his blood (Luke 22:20), and the awesome name is the name of Jesus before which every knee bows. Rev 15:4: 'who will not fear you, Lord, and glorify your name? For you alone are holy.'"
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Col 2:3",
        "note": "The fear of the LORD is the beginning of wisdom — 'in whom are hidden all the treasures of wisdom and knowledge' (Col 2:3). The wisdom that begins with fearing the LORD (Ps 111:10) is, in the NT, a person: Christ himself is the wisdom of God (1 Cor 1:24), and all the treasures of wisdom are hidden in him. The Psalm's wisdom-ethic (fear → wise living → praise) is the pattern that Col 2 applies to Christ: knowing him is the beginning and fullness of wisdom."
      }
    ]
  },
  "113": {
    "7": [
      {
        "type": "allusion",
        "target": "Luke 1:52",
        "note": "He raises the poor from the dust and lifts the needy from the ash heap, to seat them with princes, with the princes of his people — 'he has brought down rulers from their thrones but has lifted up the humble. He has filled the hungry with good things but has sent the rich away empty' (Luke 1:52-53). The Magnificat's structure mirrors Psalm 113:7-8 precisely: divine reversal of social position. Psalm 113 was sung at Passover — it was almost certainly in Mary's mind as she composed her song. The pattern of God lifting the lowly reaches its supreme enactment in the incarnation, where the Most High takes human flesh in lowliness."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Luke 1:36",
        "note": "He settles the childless woman in her home as a happy mother of children — 'even Elizabeth your relative is going to have a child in her old age, and she who was said to be unable to conceive is in her sixth month' (Luke 1:36). The divine reversal of barrenness celebrated in Psalm 113:9 (recalling Hannah, Sarah, Rachel) is enacted in Elizabeth: the barren woman settled as a happy mother. The pattern the Psalm celebrates as characteristic of God reaches its penultimate OT-style fulfillment in John the Baptist's conception, and its final form in Mary's virginal conception — where God gives life where no life was humanly possible."
      }
    ]
  },
  "114": {
    "1": [
      {
        "type": "allusion",
        "target": "1 Pet 2:9",
        "note": "When Israel came out of Egypt, Jacob from a people of foreign tongue, Judah became God's sanctuary, Israel his dominion — 'but you are a chosen people, a royal priesthood, a holy nation, God's special possession, that you may declare the praises of him who called you out of darkness into his wonderful light' (1 Pet 2:9). The language Peter applies to the church — holy nation, God's sanctuary-people — is drawn from the Exodus identity Psalm 114 celebrates. The church is the new Exodus community: called out of spiritual Egypt (sin and bondage), constituted as God's dwelling-place and kingdom."
      }
    ],
    "8": [
      {
        "type": "type",
        "target": "1 Cor 10:4",
        "note": "Who turned the rock into a pool, the hard rock into springs of water — 'they drank from the spiritual rock that accompanied them, and that rock was Christ' (1 Cor 10:4). Psalm 114:8 celebrates the Exodus miracle of water from the rock; Paul identifies that rock as Christ. The physical transformation — hard rock into life-giving water — is the type of Christ who is the source of living water (John 4:14: 'a spring of water welling up to eternal life'). Psalm 114 was sung at Passover, the same setting where Jesus instituted the Lord's Supper; its rock-and-water imagery belongs to the Last Supper's liturgical context."
      }
    ]
  },
  "115": {
    "4": [
      {
        "type": "allusion",
        "target": "Acts 17:29",
        "note": "Their idols are silver and gold, made by human hands. They have mouths, but cannot speak, eyes, but cannot see — 'therefore since we are God's offspring, we should not think that the divine being is like gold or silver or stone — an image made by human skill and imagination' (Acts 17:29). Paul's Areopagus sermon applies the logic of Psalm 115's idol polemic — the living God cannot be contained in human-crafted images — as the theological argument against Athenian idolatry. The Psalm's reductio (idols are made by hands, therefore inert and absurd) is the argument Paul makes in Athens for turning to the God who made human hands."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Heb 13:6",
        "note": "Trust in the LORD — he is their help and shield — 'so we say with confidence: \"The Lord is my helper; I will not be afraid. What can mere mortals do to me?\"' (Heb 13:6). The trust in the LORD as help and shield (Ps 115:9, cited from Ps 118:6) is the confidence Hebrews draws on for its final exhortations: contentment, because the Lord is helper; boldness, because the Lord is shield. The Psalm's call to trust is the ground of the NT community's fearlessness in the face of persecution."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "1 Cor 15:20",
        "note": "It is not the dead who praise the LORD, those who go down to the place of silence — 'but Christ has indeed been raised from the dead, the firstfruits of those who have fallen asleep' (1 Cor 15:20). Psalm 115:17 states the pre-resurrection limit: the dead cannot praise. This is the horizon the Psalm cannot see past — the silence of the grave ends praise. The resurrection of Christ is the answer: the firstfruits of the dead have already begun to praise (Heb 2:12: 'I will declare your name to my brothers and sisters; in the assembly I will sing your praises'). Christ's resurrection opens the silence of Psalm 115:17."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['111', '112', '113', '114', '115', '116', '117']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 111-117 echoes complete.")

if __name__ == '__main__':
    main()
