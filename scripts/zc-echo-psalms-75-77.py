"""
Echo data — Psalms chapters 75–77
Run: python3 scripts/zc-echo-psalms-75-77.py

Key connections:
- Ps 75:2: "When I choose the appointed time, I will judge with perfect equity" →
  Acts 17:31 / John 5:22: God has fixed a day when he will judge through the man
  he appointed. The judge who sets the appointed time is the Father who has given all
  judgment to the Son.
- Ps 75:8: The cup of foaming wine the wicked must drain → Rev 14:10 (cup of God's
  wrath); and Christ's Gethsemane prayer (Matt 26:39) — he takes the cup so the
  redeemed need not drain it to the dregs.
- Ps 76:2: "His tabernacle in Salem / dwelling in Zion" → John 1:14 (Word tabernacled
  among us); Heb 12:22 (heavenly Zion).
- Ps 76:9: "God arose to judge, to save all the humble" → Matt 5:5 / Luke 1:52
  (God lifts the humble; Beatitudes pattern).
- Ps 77:7-9: "Will the Lord reject forever?... Has his steadfast love ceased?" →
  Matt 27:46 / Ps 22:1 — the questions of abandonment reach their sharpest point
  in the cry of dereliction.
- Ps 77:19: "Your path went through the sea; your footprints could not be found" →
  Rom 11:33 (paths of God beyond tracing out).
- Ps 77:20: "You guided your people like a flock through Moses and Aaron" →
  John 10:11 / Heb 13:20 — Christ the Good Shepherd fulfills the type of the
  shepherd-leader who brings the flock through the wilderness.
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

# INTENT: Echo data for Psalms 75–77 — the appointed-time judgment given to the Son
#   (Ps 75 → Acts 17:31/John 5:22), the cup of wrath that Christ drinks for the
#   redeemed (Ps 75:8 → Matt 26:39/Rev 14:10), the divine tabernacle in Salem
#   become the incarnation (Ps 76:2 → John 1:14), and the untraceable path through
#   the sea (Ps 77:19 → Rom 11:33) answered by the Good Shepherd (Ps 77:20 → John 10).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(75,78)])" should show non-zero for all three.

PSALMS_ECHOES = {
  "75": {
    "2": [
      {
        "type": "allusion",
        "target": "Acts 17:31",
        "note": "When I choose the appointed time, I will judge with perfect equity — 'For he has set a day when he will judge the world with justice by the man he has appointed. He has given proof of this to everyone by raising him from the dead' (Acts 17:31). The divine speaker of Psalm 75:2 who sets the appointed time of judgment is the Father; the one through whom he executes that judgment is 'the man he has appointed' — the risen Christ. The Psalm's assured timing ('when I choose') is the Father's sovereign scheduling of the judgment entrusted to the Son."
      },
      {
        "type": "allusion",
        "target": "John 5:22",
        "note": "I will judge with perfect equity — 'Moreover, the Father judges no one, but has entrusted all judgment to the Son' (John 5:22). The divine judge of Psalm 75:2 who promises perfect judgment at the appointed time has entrusted that function to the Son. The perfectly equitable judgment of the Psalm is the judgment Christ exercises — a delegation the Father makes to ensure that the judge himself has walked in human weakness and temptation (Heb 4:15)."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Phil 2:9",
        "note": "God is the judge; he brings one person down and raises another up — 'therefore God exalted him to the highest place and gave him the name that is above every name' (Phil 2:9). The divine pattern of Psalm 75:7 — bringing one down, raising another up — reaches its defining expression in the crucifixion and resurrection of Christ. The one who was brought to the lowest point (death on a cross, Phil 2:8) is raised to the highest place by the divine judge who governs all ascent and descent."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Rev 14:10",
        "note": "In the hand of the LORD there is a cup of foaming wine, well mixed; all the wicked of the earth shall drain it to the very dregs — 'they, too, will drink the wine of God's fury, which has been poured full strength into the cup of his wrath' (Rev 14:10). Psalm 75:8's cup of divine wrath that all the wicked must drink is the same cup that Revelation pours out in the bowl-judgment sequence. The image is continuous from Psalm to Revelation — the cup of divine wrath has been prepared and must be fully consumed."
      },
      {
        "type": "allusion",
        "target": "Matt 26:39",
        "note": "All the wicked of the earth shall drain it to the very dregs — 'My Father, if it is possible, may this cup be taken from me. Yet not as I will, but as you will' (Matt 26:39). Christ in Gethsemane does not avoid the cup but takes it — the cup the wicked must drain (Ps 75:8) is the cup Christ voluntarily drinks in their place. His drinking to the dregs at Calvary is the mechanism by which the redeemed are spared; the cross is the cup of wrath exhausted for them."
      }
    ]
  },
  "76": {
    "2": [
      {
        "type": "allusion",
        "target": "John 1:14",
        "note": "His tabernacle is in Salem; his dwelling place is in Zion — 'the Word became flesh and tabernacled among us; and we beheld his glory' (John 1:14). The divine tabernacle in Salem (Jerusalem) that Psalm 76:2 celebrates is the OT form of the divine dwelling that John announces as enacted in the incarnation. The same verb root (σκηνόω) connects both: God's tabernacling presence moves from a fixed location (Zion) to a mobile, personal presence in the flesh of the Son — Emmanuel, God dwelling among his people."
      },
      {
        "type": "allusion",
        "target": "Heb 12:22",
        "note": "His dwelling place is in Zion — 'you have come to Mount Zion, to the city of the living God, the heavenly Jerusalem... to Jesus the mediator of a new covenant' (Heb 12:22, 24). The earthly Zion where God dwells in Psalm 76:2 is the shadow of the heavenly Zion to which all believers now have access through Christ. The Jerusalem where God tabernacled becomes the heavenly Jerusalem that Christ opened — the dwelling of God permanently accessible through the one who is himself that dwelling."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Luke 1:52",
        "note": "When God arose to judge, to save all the humble of the earth — 'he has brought down rulers from their thrones but has lifted up the humble' (Luke 1:52, the Magnificat). Mary's song applies the divine pattern of Psalm 76:9 directly to the Christ-event: God arises to judge — bringing down the powerful and saving the humble — in the birth of the Messiah. The Psalm's promise of divine rescue for the humble is the pattern the Magnificat declares enacted in the incarnation."
      },
      {
        "type": "allusion",
        "target": "Matt 5:5",
        "note": "God arose to judge, to save all the humble of the earth — 'Blessed are the meek, for they will inherit the earth' (Matt 5:5). The divine saving of the humble/meek that Psalm 76:9 promises is the beatitude Jesus pronounces over the same group. The ones who appear to have nothing — the humble of the earth — are the ones whom God rises to vindicate; Jesus' Beatitude declares the eschatological inheritance already secured in himself."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Rev 17:14",
        "note": "He cuts off the spirit of princes; he is fearsome to the kings of the earth — 'They will wage war against the Lamb, but the Lamb will triumph over them because he is Lord of lords and King of kings' (Rev 17:14). The fearsome God who cuts off princes and terrifies kings (Ps 76:12) is the Lamb who conquers all earthly kings. The awe-inspiring warrior of Psalm 76 is the slain-and-risen Lamb of Revelation — the paradox of omnipotence clothed in apparent weakness conquering all competing powers."
      }
    ]
  },
  "77": {
    "7": [
      {
        "type": "allusion",
        "target": "Matt 27:46",
        "note": "Will the Lord reject us forever? Will he never again be pleased with us? Has his steadfast love ceased once and for all? — 'My God, my God, why have you forsaken me?' (Matt 27:46). The rhetorical crisis of Psalm 77:7-9 — the agonized questioning of whether God has permanently withdrawn — reaches its sharpest expression in Christ's cry of dereliction. He does not merely ask the Psalm's questions but lives them at their most acute. His resurrection on the third day is the definitive answer: no, God has not rejected forever; his steadfast love has not ceased."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "1 Tim 3:16",
        "note": "O God, your path runs through what is holy; what god anywhere is as great as our God? — 'Great is the mystery of godliness: God appeared in a body, was vindicated by the Spirit, was seen by angels, was preached among the nations, was believed on in the world, was taken up in glory' (1 Tim 3:16). The incomparability of God (Psalm 77:13: 'what god is as great?') is fully disclosed in the Christ-event. The mystery that no other god could match — God becoming flesh, dying, rising, ascending — is the NT answer to the Psalm's rhetorical question about divine incomparability."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "1 Pet 1:18",
        "note": "With your strong arm you redeemed your people, the descendants of Jacob and Joseph — 'For you know that it was not with perishable things such as silver or gold that you were redeemed... but with the precious blood of Christ, a lamb without blemish or defect' (1 Pet 1:18-19). The redemption by God's strong arm (Ps 77:15) is the exodus type that the NT declares fulfilled in the redemption by Christ's blood. The strong arm becomes the cross; the cost of liberation is no longer military conquest but the self-giving sacrifice of the Son."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Rom 11:33",
        "note": "Your path went through the sea, your way through the great deep; but your footprints could not be found — 'Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his paths beyond tracing out!' (Rom 11:33). The untraceable path of God through the sea (Psalm 77:19) becomes Paul's doxology about the unsearchable ways of God in the plan of salvation — particularly the mystery of Israel's hardening and ultimate redemption. The path through the deep that leaves no human-discernible footprint is the pattern of God's ways that Paul worships rather than analyzes."
      }
    ],
    "20": [
      {
        "type": "type",
        "target": "John 10:11",
        "note": "You guided your people like a flock, through the leadership of Moses and Aaron — 'I am the good shepherd. The good shepherd lays down his life for the sheep' (John 10:11). The shepherd-leadership of Moses and Aaron through the wilderness (Ps 77:20) is the type that Christ fulfills as the Good Shepherd. Moses and Aaron guided the flock through physical desert; Christ leads the flock through death itself — Heb 13:20: 'the great Shepherd of the sheep, who was brought back from the dead through the blood of the eternal covenant.' The shepherd-leader who parts the sea and brings the people through becomes the shepherd who passes through death and brings the sheep after him."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['75', '76', '77']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 75–77 echoes complete.")

if __name__ == '__main__':
    main()
