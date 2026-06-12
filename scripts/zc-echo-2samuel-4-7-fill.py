"""
Echo Layer — 2 Samuel chapters 4–7
Run: python3 scripts/zc-echo-2samuel-4-7-fill.py

Ch7 already has v12 and v14 entries (Nathan's oracle → Luke 1:32-33, Heb 1:5).
This script adds ch4, ch5, ch6 entries only; ch7 entries preserved by merge_echo.

Key echo connections:
- 5:2  — shepherd-king vocabulary → Ezek 34; John 10:11
- 5:3  — David's third anointing → NT's triple witness to Christ's identity
- 5:4  — David 30 years old at accession → Luke 3:23 (Jesus ~30 at ministry start)
- 5:7  — Zion captured → Heb 12:22; Rev 14:1; 1 Pet 2:6
- 5:20 — Baal-perazim ("Lord who bursts through") → Isa 28:21
- 5:24 — divine advance-guard sound in trees → holy-war divine-presence motif
- 6:2  — ark / name of LORD of hosts enthroned above cherubim → John 1:14; Heb 9:5
- 6:14 — David dancing in linen ephod → priestly-royal fusion → Ps 110; Heb 7:1-3
- 6:21 — king humbling before YHWH → Phil 2:7-8 kenosis pattern
- 6:23 — Michal's barrenness → covenant consequence for despising the anointed
- 4:9  — "LORD who has redeemed my life from all distress" → Ps 34:19; 1 Pet 1:18-19
- 4:11 — innocent blood on the king's watch → Matt 27:24-25 Pilate pattern
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

SAMUEL_ECHOES = {
  "4": {
    "4": [
      {
        "type": "theme",
        "target": "2 Sam 9:1-13",
        "note": "The parenthetical about Mephibosheth — Jonathan's crippled son dropped by his nurse in the flight from Jezreel — appears in a chapter about the deaths of Saul's line. It places the last vulnerable member of the Saulide house in the shadow of the political violence, preparing for ch9 where David will seek him out and show covenant loyalty (ḥesed) to him for Jonathan's sake. The aside is a narrative crumb dropped into the assassination story: amid death, one of the house of Saul lives. The ḥesed David will show Mephibosheth — seating him at his table despite his disability — is the grace-structure that the NT applies to sinners brought to the King's table (Luke 14:21)."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Ps 34:19",
        "note": "David's oath formula — 'the LORD lives, who has redeemed my life from every distress' (<em>pādāh</em> = ransom/redeem) — is the same redemption vocabulary that Ps 34:19 uses: 'the LORD redeems the soul of his servants; none who take refuge in him will be condemned.' The <em>pādāh</em> root (ransom/price-paid redemption) is the foundation on which 1 Pet 1:18-19 builds: 'redeemed... not with perishable things such as silver or gold, but with the precious blood of Christ.' David's personal testimony of redemption from distress is the earthly version of the cosmic redemption Christ accomplishes."
      }
    ],
    "11": [
      {
        "type": "theme",
        "target": "Matt 27:24",
        "note": "David's demand for justice when wicked men murder a righteous man on his bed — 'should I not require his blood from your hands?' — inverts the Barabbas scene: here the king refuses to benefit from the murder of an innocent and punishes those who thought they were doing him a favor. Pilate's handwashing (Matt 27:24) is the opposite: the judge who washes his hands of innocent blood rather than requiring account. David&rsquo;s insistence on accountability for innocent blood is the standard of justice that makes Pilate's abnegation all the more striking."
      }
    ]
  },
  "5": {
    "2": [
      {
        "type": "type",
        "target": "Ezek 34:23",
        "note": "YHWH's word to David — 'you shall shepherd my people Israel' (<em>tirʿeh</em> from the root <em>rāʿāh</em>) — establishes the shepherd as the defining metaphor of the Davidic king. Ezekiel 34 pronounces judgment on Israel's failed human shepherds and promises: 'I will place over them one shepherd, my servant David' (v23). Jesus fulfills this directly: 'I am the good shepherd' (John 10:11), explicitly applying the Ezekiel 34 language. The shepherd-king that David typifies finds its perfect expression in the one who lays down his life for the sheep."
      },
      {
        "type": "fulfillment",
        "target": "John 10:11",
        "note": "'I am the good shepherd; the good shepherd lays down his life for the sheep' — Jesus applies to himself the shepherd-king vocabulary that YHWH used in appointing David. Where David shepherded Israel through conquest and administration, Christ shepherds through self-sacrifice. The Davidic commission ('shepherd my people Israel') is fulfilled in the one whose shepherding consists in dying for the flock."
      }
    ],
    "3": [
      {
        "type": "type",
        "target": "Acts 2:36",
        "note": "David's third anointing — over all Israel at Hebron, after earlier anointings at Bethlehem (1 Sam 16) and over Judah (2 Sam 2:4) — completes his installation as king. The progressive public disclosure of the elect king parallels Christ's progressive revelation: anointed at baptism (Matt 3:16-17), declared Son of God by the resurrection (Rom 1:4), and installed as Lord and Christ at the Ascension (Acts 2:36: 'God has made this Jesus, whom you crucified, both Lord and Messiah'). The Hebron covenant between David and the elders ('the elders of Israel came to the king, and David made a covenant with them') prefigures the new covenant sealed at the Last Supper between Christ and his disciples."
      }
    ],
    "4": [
      {
        "type": "theme",
        "target": "Luke 3:23",
        "note": "David was thirty years old when he began to reign — the same age the Lukan narrative specifies for Jesus at the start of his public ministry: 'Now Jesus himself was about thirty years old when he began his ministry' (Luke 3:23). Thirty was also the age of Levitical service-entry (Num 4:3, 23) and Joseph's appointment to govern Egypt (Gen 41:46). The age-30 marker at the beginning of David's full kingship and Jesus's ministry is not incidental; Luke's specification matches the royal/priestly service-commencement age that the Torah establishes. The one who is both king and priest (Ps 110) begins his work at the age the law assigns to each office."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Heb 12:22",
        "note": "David captures the stronghold of Zion and calls it 'the city of David' — the theological center of Israel's worship and the seat of the Davidic dynasty. Zion becomes the location from which YHWH rules (Ps 2:6: 'I have installed my king on Zion, my holy mountain') and the destination toward which the nations come (Isa 2:2-3). Hebrews 12:22 identifies the eschatological destination of believers as 'Mount Zion... the heavenly Jerusalem.' Revelation 14:1 places the Lamb on Mount Zion with the 144,000. The physical Zion David captures is the earthly type of the heavenly Zion that Christ establishes as his permanent throne."
      },
      {
        "type": "theme",
        "target": "1 Pet 2:6",
        "note": "1 Pet 2:6 cites Isa 28:16 ('I lay in Zion a chosen and precious cornerstone') — Isaiah's Zion theology is directly built on the Davidic founding of Zion here. Peter applies the Zion-foundation image to Christ: 'the one who trusts in him will never be put to shame.' The stone laid in Zion is Christ; the Zion that David captures becomes the location of the greatest of divine covenants, fulfilled when God himself lays a cornerstone in Zion."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Matt 1:23",
        "note": "'David grew steadily greater, for the LORD God of hosts was with him' — the divine-presence formula (<em>YHWH ʾelōhê ṣěḇāʾôt ʿimmô</em>) is the Immanuel formula in its Davidic register. Isaiah 7:14's promise — 'they will call him Immanuel' (God with us) — is the eschatological fulfillment of what the divine presence with David prefigures. Matthew 1:23 cites the Immanuel prophecy for Jesus's birth, completing the trajectory from 'the LORD was with David' through to 'God with us' in person."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Isa 28:21",
        "note": "'The LORD has burst through my enemies before me like a flood of waters' — the place is named Baal-perazim ('Lord of bursting-through'). Isaiah 28:21 cites this battle as a type of YHWH's future eschatological action: 'the LORD will rise up as he did at Mount Perazim, as he did in the Valley of Gibeon — to do his work, his strange work, and perform his task, his strange task.' The Baal-perazim victory becomes Isaiah's shorthand for overwhelming divine intervention. The 'bursting through' of all that opposes YHWH's purposes is the pattern that culminates in the resurrection — the ultimate divine 'breaking through' death."
      }
    ],
    "24": [
      {
        "type": "theme",
        "target": "Josh 10:14",
        "note": "The sound of marching in the tops of the balsam trees as the signal that YHWH has gone out before the army — the invisible divine advance-guard that leads Israel's attack — is the holy-war motif of divine participation in the battle (cf. Josh 10:14: 'There has been no day like it before or since, a day when the LORD listened to a human being'). The divine army that goes before the earthly army is developed in 2 Kgs 6:17 (the horses and chariots of fire surrounding Elisha) and Rev 19:11-16 (Christ leading the heavenly armies at the eschaton). YHWH's going out before his people to defeat their enemies is the pattern that Christ fulfills as the captain of salvation (Heb 2:10)."
      }
    ]
  },
  "6": {
    "2": [
      {
        "type": "theme",
        "target": "John 1:14",
        "note": "The ark of God 'bears the name of the LORD of hosts who is enthroned above the cherubim' (<em>niqqrāʾ šēm šēm YHWH ṣəḇāʾôt yōšēḇ hakərûḇîm</em>) — the ark as the earthly locus of the divine name and presence. The divine name enthroned above the cherubim is the OT's closest approach to the concept of personal divine presence. John 1:14 — 'the Word became flesh and made his dwelling (<em>eskēnōsen</em>, tabernacled) among us' — describes the Incarnation as the fulfillment of the divine-presence dwelling: where the ark carried the Name, Christ is the Name in person (Phil 2:9-11; Rev 19:13)."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Matt 21:8-9",
        "note": "David and all Israel celebrating before the LORD with lyres, harps, tambourines, castanets, and cymbals as the ark is brought up — the jubilant procession of the divine presence into Jerusalem. The Triumphal Entry (Matt 21:8-9) is the deliberate re-enactment of this procession: palm branches, shouting, &lsquo;Hosanna to the Son of David!&rsquo; — the people celebrating the presence of the Davidic king entering the holy city. Jesus approaches Jerusalem as David approached it with the ark: the King is coming, and his people celebrate with all their strength."
      }
    ],
    "11": [
      {
        "type": "theme",
        "target": "Luke 1:56",
        "note": "The ark staying in Obed-edom's house for three months while it blessed his household recalls the structure of Mary's visit to Elizabeth: Mary stays with Elizabeth about three months (Luke 1:56), and Elizabeth is blessed by the presence of the child she carries — 'why am I so favored, that the mother of my Lord should come to me?' (Luke 1:43). The blessed household that receives the divine presence for three months is a structural anticipation of the Incarnation's blessing coming through the presence of Christ in the womb."
      }
    ],
    "14": [
      {
        "type": "type",
        "target": "Ps 110:4",
        "note": "David dancing before the LORD wearing a linen ephod — the garment of the priest — enacts the fusion of priestly and royal roles that Psalm 110:4 declares: 'You are a priest forever, in the order of Melchizedek.' David is king, but in his Zion worship he functions in a priestly capacity: offering sacrifices (v13, 17), blessing the people in YHWH's name (v18), and distributing the fellowship meal (v19). Hebrews 7 develops the Melchizedek king-priest pattern and applies it to Christ, the ultimate priest-king who makes the final atonement and intercedes forever."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "John 1:11",
        "note": "Michal's contempt for David as he danced before the LORD — 'she despised him in her heart' — is the type of the reception of the humiliated king that recurs throughout the messianic narrative. David humbles himself in worship; Michal sees only undignified exposure. John 1:11 — 'he came to that which was his own, but his own did not receive him' — captures the same dynamic: the king who worships and serves is despised by those who expected royal dignity on different terms. The daughter of the former king who despises the present anointed one is the archetype of covenant community members who reject the new dispensation."
      }
    ],
    "21": [
      {
        "type": "shadow",
        "target": "Phil 2:7-8",
        "note": "David's response to Michal — 'I will make myself even more contemptible than this, and I will be humble in my own sight' — is the kenotic structure: the king who deliberately descends below his station for YHWH's honor. Philippians 2:7-8 describes Christ's kenosis: 'he made himself nothing, taking the very nature of a servant... he humbled himself by becoming obedient to death.' The pattern of the anointed king who chooses contemptibility before the LORD rather than dignity before the crowd is the structure that the Incarnation and the cross embody absolutely. David's willing abasement before YHWH's presence is the earthly shadow of Christ's willing descent for the redemption of the world."
      }
    ],
    "23": [
      {
        "type": "theme",
        "target": "Luke 1:28",
        "note": "Michal's barrenness — the covenant consequence for despising YHWH's anointed — contrasts with the blessing of those who receive and honor the anointed one. Obed-edom's household was blessed for receiving the ark (v11); Michal's line is cut off for despising the king who carried YHWH's presence. Luke 1:28 — 'Greetings, you who are highly favored! The Lord is with you' — describes the blessing of Mary who receives the ultimate anointed one with humility ('I am the Lord's servant', v38), the antitype of Michal who despised the humiliated king."
      }
    ]
  }
}

def main():
    existing = load_echo('2samuel')
    merge_echo(existing, SAMUEL_ECHOES)
    save_echo('2samuel', existing)
    print('2 Samuel 4-7 echoes written.')

if __name__ == '__main__':
    main()
