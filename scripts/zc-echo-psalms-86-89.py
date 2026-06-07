"""
Echo data — Psalms chapters 86–89 (gap-fill: chs 86, 87, 88 missing; 89 already present)
Run: python3 scripts/zc-echo-psalms-86-89.py

Key connections:
- Ps 86:5: "abounding in steadfast love for all who call on you" → Rom 10:12-13
  (no distinction between Jew and Gentile; "everyone who calls on the name of the Lord
  will be saved") — the universal scope of divine steadfast love becomes the basis for
  the universal gospel offer.
- Ps 86:9: "All the nations you have made will come and bow before you" → Phil 2:10-11
  (every knee bows, every tongue confesses Jesus as Lord) / Rev 15:4.
- Ps 86:13: "Rescued my soul from the lowest depths of Sheol" → Acts 2:24 / Acts 2:31
  (resurrection as divine rescue from Sheol).
- Ps 86:15: "Compassionate, gracious, slow to anger, abounding in steadfast love and
  faithfulness" (= Exod 34:6 formula) → John 1:14 (grace and truth = hesed + emet
  embodied in the incarnate Word).
- Ps 87:4-6: Nations registered as "born in Zion" → Heb 12:23 (church of the firstborn
  whose names are written in heaven) / Phil 3:20 (citizenship in heaven) / Gal 4:26.
- Ps 87:7: "All my springs of life are in you" → John 4:14 (living water welling up
  to eternal life) / Rev 22:1.
- Ps 88:5: "Like the slain who lie in the grave — cut off from your hand" → Matt 27:46
  / 2 Cor 5:21 — Christ enters the darkest Psalm as the one truly cut off from the
  Father's hand at the cross.
- Ps 88:8: "My companions pushed far away; sealed in, cannot get out" → Mark 14:50
  (all deserted him) / Matt 27:66 (tomb sealed).
- Ps 88:18: "Darkness" — the Psalm ends with darkness and no answer; the resurrection
  is the answer Psalm 88 doesn't yet see (John 20:1 — darkness turning to dawn).
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

# INTENT: Echo data for Psalms 86, 87, 88 — universal call to all nations (Ps 86 →
#   Rom 10:13/Phil 2:10), the Exodus 34:6 character formula embodied in Christ (Ps 86:15
#   → John 1:14), nations enrolled as Zion-born citizens (Ps 87 → Heb 12:23), and
#   Psalm 88 as the darkest OT psalm whose darkness Christ fully enters (Matt 27:46 /
#   Mark 14:50) and whose answer is only given in the resurrection (John 20:1).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(86,90)])" should show non-zero for all four.

PSALMS_ECHOES = {
  "86": {
    "5": [
      {
        "type": "allusion",
        "target": "Rom 10:13",
        "note": "You, O Lord, are good and forgiving, abounding in steadfast love for all who call on you — 'for there is no difference between Jew and Gentile — the same Lord is Lord of all and richly blesses all who call on him, for, \"Everyone who calls on the name of the Lord will be saved\"' (Rom 10:12-13). The universal scope of divine steadfast love for 'all who call' (Ps 86:5) is the OT ground of Paul's universal gospel offer. The same God whose hesed is boundless for all who call on him is the God who richly blesses all who call on Christ's name."
      }
    ],
    "9": [
      {
        "type": "fulfillment",
        "target": "Phil 2:10",
        "note": "All the nations you have made will come and bow before you, O Lord, and they will glorify your name — 'that at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue acknowledge that Jesus Christ is Lord, to the glory of God the Father' (Phil 2:10-11). The universal bowing of all nations before the Lord (Ps 86:9) is fulfilled through the exaltation of Christ — the name before which every knee bows is the name of Jesus. Rev 15:4: 'All nations will come and worship before you, for your righteous acts have been revealed.'"
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Acts 2:31",
        "note": "Your steadfast love toward me is great; you have rescued my soul from the lowest depths of Sheol — 'seeing what was to come, he spoke of the resurrection of the Messiah, that he was not abandoned to the realm of the dead, nor did his body see decay' (Acts 2:31). Peter's Pentecost sermon presents the resurrection as God's rescue of the Messiah from Sheol — the same rescue Psalm 86:13 celebrates. David's prayer of rescue from Sheol's lowest depths is the type of the resurrection by which God drew Christ up from death's deepest pit."
      }
    ],
    "15": [
      {
        "type": "fulfillment",
        "target": "John 1:14",
        "note": "You, O Lord, are a compassionate and gracious God, slow to anger, abounding in steadfast love and faithfulness — 'the Word became flesh and dwelt among us, and we have seen his glory... full of grace and truth' (John 1:14). Psalm 86:15 quotes the Exodus 34:6 divine self-declaration (the LORD's name: compassionate, gracious, slow to anger, abounding in hesed and emet). John 1:14 applies the same two key terms — hesed ('grace') and emet ('truth') — to the incarnate Word. Christ is the embodiment of the character Psalm 86:15 describes; the Exodus formula finds its fullest expression in the face of Jesus."
      }
    ]
  },
  "87": {
    "4": [
      {
        "type": "allusion",
        "target": "Phil 3:20",
        "note": "Among those who acknowledge me I will name Rahab and Babylon — 'This one was born there' — 'But our citizenship is in heaven. And we eagerly await a Savior from there, the Lord Jesus Christ' (Phil 3:20). Psalm 87:4-6 presents the nations enrolled by God as though born in Zion — a heavenly citizenship that transcends earthly origin. Paul's declaration that believers' citizenship is in heaven is the NT realization of the Psalm's vision: through Christ, those born in every nation are registered as citizens of the heavenly city (Heb 12:22-23: 'the church of the firstborn, whose names are written in heaven')."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "John 4:14",
        "note": "Singers and dancers alike say, 'All my springs of life are in you' — 'whoever drinks the water I give them will never thirst. Indeed, the water I give them will become in them a spring of water welling up to eternal life' (John 4:14). The springs of life found in Zion (Ps 87:7) are the living water Christ gives — he is the one in whom all springs are found. Rev 22:1: the river of the water of life flowing from the throne of God and the Lamb. The singers of Psalm 87 who declare Zion their source of all life are the type of those who find in Christ the inexhaustible spring."
      }
    ]
  },
  "88": {
    "5": [
      {
        "type": "allusion",
        "target": "2 Cor 5:21",
        "note": "Like one cast loose among the dead — like the slain who lie in the grave — those you no longer remember, cut off from your hand — 'God made him who had no sin to be sin for us, so that in him we might become the righteousness of God' (2 Cor 5:21). Psalm 88:5 describes the condition of being 'cut off from God's hand' — the most radical form of divine abandonment. Christ enters this condition on behalf of sinners: the sinless one becomes the one whom God 'no longer remembers' in the sense of Psalm 88:5, so that sinners might be remembered and counted righteous. The cross is the fulfillment of this psalm's darkest moment."
      },
      {
        "type": "allusion",
        "target": "Matt 27:46",
        "note": "Cut off from your hand — 'About three in the afternoon Jesus cried out in a loud voice: \"Eli, Eli, lema sabachthani?\" (which means \"My God, my God, why have you forsaken me?\")' (Matt 27:46). The state of being cut off from God's hand (Ps 88:5) is what Christ vocalizes in the cry of dereliction. He does not merely recite the Psalm — he lives it in its most acute form, as the truly innocent one bearing the full weight of the condition the Psalm laments."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Mark 14:50",
        "note": "You have pushed my companions far away from me; you have made me repulsive to them. I am sealed in and cannot get out — 'then everyone deserted him and fled' (Mark 14:50). The abandonment by companions that Psalm 88:8 describes is enacted at the arrest in Gethsemane: every disciple flees. The sealing-in with no way out anticipates the sealed tomb (Matt 27:66: 'making the tomb secure by putting a seal on the stone and posting the guard') — the one who could not get out is the one who walks out on the third day."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "John 20:1",
        "note": "My companions are in darkness — Psalm 88 is the only Psalm with no resolution; it ends in darkness without a turn to praise. This structural absence is significant: the darkness at the end of Psalm 88 is the condition of the disciples after the crucifixion — 'Early on the first day of the week, while it was still dark, Mary Magdalene went to the tomb' (John 20:1). The resurrection is the answer Psalm 88 does not yet see. The darkness that ends the Psalm is pierced by the dawn of Easter morning — the one who was 'in darkness' (v.6, v.18) is raised, and the darkness-ending Psalm finds its answer outside its own frame."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['86', '87', '88', '89']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 86–89 echoes complete.")

if __name__ == '__main__':
    main()
