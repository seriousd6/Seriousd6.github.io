"""
Echo Commentary — Hebrews chapters 1–5
Run: python3 scripts/zc-echo-hebrews-1-5.py

Key decisions:
- Hebrews' dense OT citation structure requires careful type/fulfillment distinction:
  explicit "it is written" or "he says" citations = quote; verbal/thematic parallels = allusion
- 1:5 Ps 2:7 and 2 Sam 7:14 = fulfillment (author explicitly applies to the Son's exaltation)
- 2:6-8 Ps 8 = fulfillment (author cites and applies to Jesus's humiliation-exaltation)
- 3:7-11 Ps 95 = quote + typological: Israel's wilderness rebellion = shadow for the community's warning
- 4:3-5 Gen 2:2 + Ps 95 combined = type (God's rest pattern from creation + wilderness failure)
- Melchizedek (ch5): Gen 14 shadow; Ps 110:4 quote/fulfillment
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

HEBREWS = {
  "1": {
    "1": [
      {"type": "theme", "target": "Amos 3:7", "note": "God has spoken through the prophets — the prophetic tradition of divine address through human instruments is the OT pattern that Hebrews' opening celebrates and then contrasts with the final speaking in the Son. The prologue honors the prophetic tradition (God did speak) while insisting on the qualitative difference of the Son's speech."},
      {"type": "theme", "target": "Jer 31:31–34", "note": "The new covenant oracle promises a fuller divine communication beyond the Mosaic: 'I will put my law within them... they shall all know me.' Hebrews opens in the key of this Jeremianic new-covenant promise: the Son's final speaking is the fulfillment of the word God promised to deliver in the new covenant."}
    ],
    "2": [
      {"type": "allusion", "target": "Gen 1:1–3", "note": "Creation through the divine word/agent — the same logic as 'through whom he also created the worlds' picks up the wisdom and logos traditions (Prov 8:22-31; Ps 33:6) that identify the divine agent of creation. The Son as creator establishes his superiority to angels, who were themselves created."},
      {"type": "allusion", "target": "Ps 2:8", "note": "\"Ask of me, and I will make the nations your heritage, and the ends of the earth your possession\" — the Son appointed heir of all things participates in the Davidic king's inheritance of the nations. Hebrews 1:2 applies this universal inheritance to the Son's eschatological appointment."}
    ],
    "3": [
      {"type": "allusion", "target": "Wis 7:26", "note": "\"She is a reflection of eternal light, a spotless mirror of the working of God, and an image of his goodness\" — the Wisdom of Solomon's portrait of Wisdom as the radiance and image of God is the conceptual background to the Son as 'the radiance of the glory of God and the exact imprint of his nature.' Hebrews adopts and applies to the Son what earlier Jewish wisdom tradition said about personified Wisdom."},
      {"type": "allusion", "target": "Ps 110:1", "note": "\"Sit at my right hand\" — the exaltation to God's right hand after making purification for sins is the fulfillment of the Davidic lord's enthronement. Verse 3's right-hand session introduces the psalm that will be the letter's most-used text (1:13; 8:1; 10:12; 12:2)."}
    ],
    "4": [
      {"type": "allusion", "target": "Phil 2:9–11", "note": "The exaltation logic is the same: the one who humbled himself has been given the name above every name. Hebrews' 'having become as much superior to angels as the name he has inherited is more excellent than theirs' parallels the Philippians hymn's exaltation-to-the-name-of-Lord."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Ps 2:7", "note": "\"You are my Son; today I have begotten you\" — Hebrews 1:5 cites Psalm 2:7 as the scriptural ground of the Son's superior name. In context, 'today' refers to the eschatological enthronement/resurrection-exaltation (cf. Acts 13:33 where Luke applies Ps 2:7 to the resurrection). The Son's divine sonship revealed in exaltation fulfills the royal-sonship promise of the coronation psalm."},
      {"type": "fulfillment", "target": "2 Sam 7:14", "note": "\"I will be his father, and he shall be my son\" — the Davidic covenant promise to Solomon (and to the Davidic line) is applied in Hebrews 1:5 to the Son as its ultimate fulfillment. The divine-sonship relationship promised to David's descendants finds its definitive instantiation in the Son who is superior to angels."}
    ],
    "6": [
      {"type": "fulfillment", "target": "Deut 32:43", "note": "\"Rejoice with him, O heavens; bow down to him, all gods, for he avenges the blood of his children\" — the LXX of Deut 32:43 (Ode 2) includes the command for heavenly beings to worship God; Hebrews applies this to the Son's entry into the world: 'Let all God's angels worship him.' The command for angelic worship of the Son grounds his supremacy over the angel-host."},
      {"type": "allusion", "target": "Ps 97:7", "note": "\"All who serve carved idols are put to shame... worship him, all you gods\" — the LXX reads <em>proskyneō</em> (worship) and <em>angeloi</em> (angels) in this verse; Hebrews draws on this tradition to establish that angelic worship of the Son is scripturally commanded."}
    ],
    "7": [
      {"type": "quote", "target": "Ps 104:4", "note": "\"He makes his messengers winds, his ministers a flame of fire\" — Hebrews cites Ps 104:4 LXX to characterize angels as changeable, functional servants (winds, fire) in contrast to the Son's eternal, unchanging nature. The angels are instruments; the Son is the craftsman."}
    ],
    "8": [
      {"type": "fulfillment", "target": "Ps 45:6–7", "note": "\"Your throne, O God, is forever and ever... therefore God, your God, has anointed you\" — Hebrews 1:8-9 addresses the Son directly with the language of Psalm 45 (originally a royal wedding psalm), applying the divine throne and anointing of the Davidic king to the Son. The psalm's address 'Your throne, O God' is taken as God's address to the Son — a high Christological move."}
    ],
    "10": [
      {"type": "fulfillment", "target": "Ps 102:25–27", "note": "\"Of old you laid the foundation of the earth... they will perish, but you will remain... you are the same, and your years have no end\" — Hebrews 1:10-12 cites Ps 102:25-27, originally addressed to Yahweh, as God's address to the Son. The eternal stability of the creator contrasted with the perishability of creation establishes the Son's divine permanence over against the angels who are transient ministers."}
    ],
    "13": [
      {"type": "fulfillment", "target": "Ps 110:1", "note": "\"Sit at my right hand until I make your enemies a footstool for your feet\" — the climactic citation of 1:13 returns to the Ps 110:1 motif introduced in 1:3. God says this to the Son but has never said it to any angel — the right-hand session is the exclusive prerogative of the Son. Hebrews uses Ps 110:1 more than any other OT text (1:3, 13; 8:1; 10:12; 12:2)."}
    ]
  },
  "2": {
    "6": [
      {"type": "fulfillment", "target": "Ps 8:4–6", "note": "\"What is man that you are mindful of him... you have crowned him with glory and honor... you have put all things under his feet\" — Hebrews 2:6-8 cites Psalm 8 as the scriptural account of humanity's intended dominion and of Jesus's actual fulfillment of that destiny through humiliation and exaltation. The author's interpretive move: Ps 8 describes what is 'not yet' for humanity in general but what has already been accomplished in Jesus specifically — he was humiliated (crowned with thorns) and then crowned with glory through death and resurrection."}
    ],
    "7": [
      {"type": "type", "target": "Gen 1:26–28", "note": "The creation mandate — dominion over all things — is the Adamic calling that Psalm 8 describes and that Jesus fulfills. The second-Adam typology implicit in Hebrews 2:5-9 is the background: the Son of Man who fulfills the dominion mandate achieves what Adam failed to secure."}
    ],
    "12": [
      {"type": "fulfillment", "target": "Ps 22:22", "note": "\"I will tell of your name to my brothers; in the midst of the congregation I will praise you\" — Hebrews 2:12 presents the risen Christ speaking Ps 22:22, announcing to his brothers (the new human family) the name of God. The psalm that began with 'My God, my God, why have you forsaken me' ends in communal praise — Hebrews applies the latter part to the exalted Christ's proclamation in the church assembly."}
    ],
    "13": [
      {"type": "fulfillment", "target": "Isa 8:17–18", "note": "\"I will put my trust in him... here am I, and the children God has given me\" — Hebrews 2:13 applies Isaiah 8:17-18 (the prophet's own words of trust and his identification of his disciples as 'children') to the Son: the one who trusts in God and identifies the covenant people as his children. The Son adopts the prophet's stance of faith-trust and the community of disciples as his family."},
      {"type": "allusion", "target": "Isa 8:14", "note": "The stone of stumbling and rock of offense context (Isa 8:14) surrounds the Hebrews 2:13 citation; the broader Isaianic section (8:12-18) is about the remnant community who fear God and trust in him despite the national crisis — a community pattern that Hebrews applies to the Son and his followers."}
    ],
    "14": [
      {"type": "fulfillment", "target": "Gen 3:15", "note": "\"He shall bruise your head, and you shall bruise his heel\" — the protoevangelium's promise that the seed of the woman will destroy the serpent is the deepest background to Hebrews 2:14: 'so that through death he might destroy the one who has the power of death, that is, the devil.' The incarnate Son destroys the devil precisely through what appears to be his defeat (death)."},
      {"type": "shadow", "target": "Hos 13:14", "note": "\"Shall I ransom them from the power of Sheol? Shall I redeem them from Death? O Death, where are your plagues? O Sheol, where is your sting?\" — the divine challenge to death that Hosea voices is the OT pattern for the Son's destruction of death's power through his own death and resurrection."}
    ],
    "17": [
      {"type": "type", "target": "Lev 16:1–22", "note": "The Aaronic high priest's annual atonement ritual — entering the Most Holy Place with blood for the sins of the people — is the OT type that establishes the category of high priesthood that Hebrews develops. The Day of Atonement ritual structure (priest, blood, entry into God's presence, intercession) provides the interpretive framework for understanding Christ's death as high-priestly atonement."}
    ]
  },
  "3": {
    "1": [
      {"type": "type", "target": "Num 12:7", "note": "\"Not so with my servant Moses. He is faithful in all my house\" — the divine commendation of Moses as faithful steward in God's house is the OT type that Hebrews uses to establish the comparison: Jesus is faithful as Moses was faithful, but as a Son rather than a servant, and over the house rather than within it."}
    ],
    "2": [
      {"type": "allusion", "target": "1 Sam 2:35", "note": "\"I will raise up for myself a faithful priest, who shall do according to what is in my heart and in my mind\" — the promise of a faithful priest that God himself will raise up is the OT background to Jesus as the faithful high priest appointed by God. The servant-of-God faithfulness theme in Numbers 12 and 1 Samuel 2 converge in Hebrews' portrait of the faithful apostle and high priest."}
    ],
    "5": [
      {"type": "type", "target": "Num 12:7–8", "note": "Moses as faithful servant-in-the-house is the explicit OT type for Hebrews 3:5. The Mosaic faithfulness is real and honored ('Moses was faithful in all God's house') but structurally inferior: a servant testifying to future things rather than the Son who builds and is over the house."}
    ],
    "7": [
      {"type": "quote", "target": "Ps 95:7–11", "note": "\"Today, if you hear his voice, do not harden your hearts as at Meribah... they shall not enter my rest\" — Hebrews 3:7-11 cites Psalm 95:7-11 as the Holy Spirit's contemporary address ('today') to the community. The extended citation is framed as Scripture speaking directly into the present moment — the wilderness generation's failure to enter God's rest is the scriptural warning that the community must not repeat."}
    ],
    "11": [
      {"type": "allusion", "target": "Num 14:20–23", "note": "God's oath that the unbelieving wilderness generation 'shall not enter the land' is the historical event behind the Ps 95 citation and Hebrews 3:11. The oath-formula 'As I swore in my wrath, They shall not enter my rest' grounds the warning in the specific Numbers 14 episode of the spies' report and Israel's refusal to enter Canaan."}
    ],
    "15": [
      {"type": "shadow", "target": "Exod 17:1–7", "note": "The Meribah water-from-the-rock episode — Israel's testing of God and hardening against his provision — is the specific historical background to the Ps 95 'hardening' warning. The community that complains against God's sufficiency enacts the Meribah pattern."},
      {"type": "shadow", "target": "Num 20:2–13", "note": "The second Meribah episode (Moses striking the rock) shows the persistent pattern of Israel's hardening — and of Moses's own failure at Meribah which disqualified him from entering the Promised Land, reinforcing the sermon's theme that even the most faithful leaders could fail if they hardened."}
    ]
  },
  "4": {
    "1": [
      {"type": "theme", "target": "Deut 12:9", "note": "\"You have not yet come to the rest and to the inheritance that the LORD your God is giving you\" — Moses acknowledges that the wilderness generation has not yet arrived at the rest that God is giving, setting up the expectation that 'rest' is the goal of the covenant journey. Hebrews 4 develops the multi-layered concept of divine rest using this trajectory."}
    ],
    "3": [
      {"type": "type", "target": "Gen 2:2", "note": "\"On the seventh day God finished his work... and he rested on the seventh day\" — the creation Sabbath rest is the primordial type of the divine rest that Hebrews 4:3-5 combines with the Ps 95 warning. God's rest exists from the foundation of the world (Gen 2:2 LXX: <em>katepausen... apo pantōn tōn ergōn autou</em>); entry into that rest is the eschatological possibility that the wilderness generation forfeited and that remains available."}
    ],
    "4": [
      {"type": "quote", "target": "Gen 2:2", "note": "\"And God rested on the seventh day from all his works\" — the Hebrews author explicitly cites Gen 2:2 as the scriptural grounding for the concept of God's rest, combining it with the Ps 95 citation to argue that the divine rest has been available since creation and that its availability extends to the present community."}
    ],
    "7": [
      {"type": "quote", "target": "Ps 95:7–8", "note": "\"Today, if you hear his voice, do not harden your hearts\" — the Ps 95 text is re-cited in 4:7 with the interpretive argument: David (the speaker of Ps 95, later than Joshua) says 'today,' which proves that Joshua's conquest did not exhaust the meaning of 'rest' — a further rest remains. The citation supports the hermeneutical move that Ps 95\'s rest refers beyond geographical Canaan."}
    ],
    "8": [
      {"type": "type", "target": "Josh 21:44", "note": "\"The LORD gave them rest on every side just as he had sworn to their fathers\" — Joshua's giving of the land-rest is acknowledged but treated by Hebrews as a type that did not exhaust the category of divine rest (since Ps 95's 'today' comes later). Joshua's territorial rest is real but provisional — a type of the eschatological sabbath-rest that remains."}
    ],
    "9": [
      {"type": "fulfillment", "target": "Gen 2:2", "note": "\"There remains a Sabbath rest for the people of God\" — Hebrews 4:9 coins the term <em>sabbatismos</em> (Sabbath-rest) to describe the eschatological rest that remains. The creation Sabbath of Gen 2:2 is the original type; the conquest rest of Joshua is an intermediate type; the remaining Sabbath-rest is the eschatological goal that the community is urged to strive to enter."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 49:2", "note": "\"He made my mouth like a sharp sword\" — the Servant's sharp-sword mouth (the divine word as weapon) is the background to Hebrews 4:12's 'word of God is living and active, sharper than any two-edged sword.' The word that discerns hearts and judges is the same word that God used through the Servant's mouth."},
      {"type": "allusion", "target": "Isa 55:10–11", "note": "\"My word shall not return to me empty... it shall accomplish that which I purpose\" — the divine word that achieves its effect is the OT background for the living and active word of God in Hebrews 4:12. The word's power to penetrate and discern is grounded in its divine origin and effectiveness."}
    ],
    "13": [
      {"type": "theme", "target": "Ps 139:1–12", "note": "\"O LORD, you have searched me and known me... you discern my thoughts from afar... where shall I flee from your presence?\" — the Psalmist's meditation on divine omniscience and inescapability is the OT background for Hebrews' 'all are naked and exposed to the eyes of him to whom we must give account.' The word of God that pierces also exposes to the divine gaze."}
    ]
  },
  "5": {
    "1": [
      {"type": "type", "target": "Lev 9:7", "note": "\"Moses said to Aaron, 'Draw near to the altar and offer your sin offering and your burnt offering and make atonement for yourself and for the people'\" — the Aaronic high priest's role of offering for himself first and then for the people is the OT structure that Hebrews 5:1-3 describes. The high priest's solidarity-in-weakness with the people (needing atonement himself) is the structural element that the Levitical system embodies and that Jesus surpasses by being without sin."}
    ],
    "4": [
      {"type": "type", "target": "Exod 28:1", "note": "\"Bring near to you Aaron your brother, and his sons with him, from among the people of Israel, to serve me as priests\" — the divine appointment of Aaron, not self-appointment, is the OT pattern for the proper basis of high priestly office. Hebrews 5:4 requires that the high priest be called by God; Jesus' calling by God (not self-appointment) fulfills this requirement."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Ps 2:7", "note": "\"You are my Son; today I have begotten you\" — Hebrews 5:5 returns to Ps 2:7 (cited in 1:5) as the scriptural word by which God appointed the Son to the high priestly office. The divine appointment-through-address is the scriptural basis for the Son's non-self-appointed priesthood."}
    ],
    "6": [
      {"type": "fulfillment", "target": "Ps 110:4", "note": "\"You are a priest forever, after the order of Melchizedek\" — the first explicit citation of Ps 110:4 in Hebrews (already introduced in 4:14 by the name Melchizedek's first appearance in 5:6). This single verse from Ps 110 will generate the extended Melchizedek discussion of chs. 5-7. The oath-backed, eternal, non-Levitical priesthood that Ps 110:4 promises is the scriptural foundation for Hebrews' entire high-priestly Christology."}
    ],
    "7": [
      {"type": "allusion", "target": "Ps 22:24", "note": "\"He has not despised or scorned the suffering of the afflicted one; he has not hidden his face from him but has listened to his cry for help\" — the Gethsemane-type prayer offered with loud cries and tears (Heb 5:7) participates in the Ps 22 pattern of the suffering righteous one whose anguished prayer is heard by God."},
      {"type": "allusion", "target": "Ps 116:1–2", "note": "\"I love the LORD, for he heard my voice and my pleas for mercy... therefore I will call on him as long as I live\" — the answered-prayer pattern of Psalm 116 is the background for 'he was heard because of his godly fear.' The Son's prayer was not unheard but answered — through resurrection rather than removal of the cup."}
    ],
    "8": [
      {"type": "theme", "target": "Ps 2:7", "note": "\"Today I have begotten you\" — the Son's learning obedience through suffering (Heb 5:8) is paradoxical alongside divine sonship. The divine sonship of Ps 2 is not mere metaphor but the reality through which the Son undergoes genuine human learning. Son-though-he-was is the Hebrews formulation of the incarnation's kenotic paradox."}
    ],
    "10": [
      {"type": "shadow", "target": "Gen 14:17–20", "note": "Melchizedek, king of Salem and priest of God Most High, blessed Abraham and received tithes from him — the Genesis narrative provides the sparse historical material from which Hebrews builds the extended typology. The priest-king who appears without genealogy, blesses the patriarch, and receives tithes from him is the historical shadow of the Son's eternal, genealogy-free priesthood."}
    ]
  }
}

def main():
    existing = load_echo('hebrews')
    merge_echo(existing, HEBREWS)
    save_echo('hebrews', existing)
    total = sum(len(vlist) for ch in existing.values() for vlist in ch.values())
    print(f'Hebrews echoes ch1–5: {len(existing)} chapters, {total} total connections.')

if __name__ == '__main__':
    main()
