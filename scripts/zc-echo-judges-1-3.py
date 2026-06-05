"""
Judges — all four layers.
Key NT: Gideon/300 (Heb 11:32), Samson (Heb 11:32), Deborah (prophet-judge),
        Barak (Heb 11:32), Jephthah (Heb 11:32), the cycle of apostasy/deliverance.
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

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ECHO = {
  "4": {
    "4": [
      {"type": "allusion", "target": "Luke 2:36", "note": "Deborah a prophetess was judging Israel — Deborah is one of the Bible's few female prophets and judges; Anna the prophetess (Luke 2:36) and Philip's four prophesying daughters (Acts 21:9) stand in the same tradition of women through whom YHWH speaks; the Spirit's gifts are not restricted by gender"}
    ]
  },
  "6": {
    "14": [
      {"type": "allusion", "target": "Heb 11:32", "note": "The LORD turned to Gideon and said: Go in this might of yours and save Israel — Gideon is named in the Hall of Faith; his victory over Midian with 300 men demonstrates that divine deliverance is not by human strength or numbers but by YHWH's power, a principle Paul applies (1 Cor 1:27-29: God chose the weak things of the world to shame the strong)"}
    ]
  },
  "13": {
    "5": [
      {"type": "allusion", "target": "Heb 11:32", "note": "The boy shall be a Nazirite to God from the womb, and he shall begin to save Israel from the hand of the Philistines — Samson is named in the Hall of Faith; his life as a Nazirite deliverer who defeats enemies through weakness (captured, blind) parallels aspects of Christ's humiliated victory; his death bringing down more enemies than his life (16:30) has been read as a type of the cross"}
    ]
  },
  "21": {
    "25": [
      {"type": "allusion", "target": "John 1:11", "note": "In those days there was no king in Israel. Everyone did what was right in his own eyes — Judges' refrain of moral anarchy without a king is the context for understanding the messianic hope: Israel needed a king after God's own heart; he came to his own and his own people did not receive him"}
    ]
  }
}

ORIGINAL = {
  "2": {
    "16": "<p><strong>vayyaqem YHWH shoftim vayoshium miyad shoseihem</strong>: 'Then YHWH raised up judges, who saved them out of the hand of those who plundered them.' The <em>shofet</em> (judge) in Judges is not primarily a legal arbiter but a military deliverer who rescues Israel in crisis — the role combines elements of prophet (receives the divine call), priest (mediates between YHWH and Israel), and king (leads the people militarily). The Spirit of YHWH coming upon the judges (Othniel, Gideon, Jephthah, Samson) is the OT's primary example of Spirit-empowered charismatic leadership, pointing forward to the permanent anointing of the Spirit on the Davidic king (1 Sam 16:13) and ultimately on Christ at his baptism (Matt 3:16).</p>"
  }
}

CONTEXT = {
  "1": {
    "1": "<p>Judges narrates the period between Joshua's death (ca. 1380 BCE) and the monarchy (ca. 1050 BCE) — about three centuries of cyclical apostasy, judgment, repentance, and deliverance. The theological pattern ('the Deuteronomic cycle') repeats throughout: Israel abandons YHWH → YHWH sends a foreign oppressor → Israel cries out → YHWH raises a judge-deliverer → the land rests during the judge's lifetime → the cycle repeats after his death. The cycle gets progressively worse: Gideon's story (chs. 6-8) ends with his son Abimelech setting himself up as a king through fratricide; the book ends with two terrible episodes (Micah's idolatry, the Levite's concubine) that illustrate the full collapse of the covenant order. The refrain 'In those days there was no king in Israel; everyone did what was right in his own eyes' (17:6; 18:1; 19:1; 21:25) is the book's theological verdict and its forward-pointing arrow toward the monarchy.</p>"
  }
}

CHRIST = {
  "2": {
    "16": "<p>A type: 'Then the LORD raised up judges, who saved them out of the hand of those who plundered them.' Each judge is a partial, flawed type of the divine deliverer: they are raised up by YHWH, empowered by his Spirit, deliver Israel from oppression, provide rest during their tenure, and then die — leaving Israel without a permanent deliverer. The entire judge-cycle is the OT's lived demonstration that the people need a permanent deliverer, a judge who will not die, a king who will reign forever. Christ fulfills all three mediatorial roles of the judges (prophet, priest, king) permanently and perfectly: he is raised up by the Father, anointed without measure by the Spirit, delivers his people from the oppressor (sin and death), and reigns forever — so that the Deuteronomic cycle is permanently broken in him.</p>"
  }
}

ECHO_1_3 = {
  "1": {
    "1": [
      {"type": "allusion", "target": "Heb 4:8", "note": "After the death of Joshua — Hebrews 4:8 pivots on the name Joshua: 'if Joshua had given them rest, God would not have spoken of another day still to come.' The Greek <em>Iēsous</em> translates both Joshua (Hebrew <em>Yehoshua</em>) and Jesus; they share the same name. Hebrews uses this identity to argue that the rest Joshua brought into Canaan was provisional and pointed to the true rest Jesus provides; the unfinished conquest of Judges 1 (the Canaanites not fully driven out) is evidence that Joshua's rest was incomplete."}
    ],
    "19": [
      {"type": "allusion", "target": "Heb 11:32-34", "note": "The LORD was with Judah, and he took possession of the hill country — the partial successes and partial failures of the conquest form the backdrop for Hebrews 11's note that the faithful 'won strength out of weakness' and 'became mighty in war, put foreign armies to flight.' The Judges narrative is the historical substance behind the Hebrews catalog of faith — these are people who accomplished extraordinary things through faith, not superior technology or numbers."}
    ]
  },
  "2": {
    "2": [
      {"type": "allusion", "target": "2 Cor 6:14-16", "note": "You shall make no covenant with the inhabitants of this land — the prohibition on covenant-making with Canaanites, whose gods would become a snare (v.3), is the OT basis for Paul's warning against being yoked with unbelievers (2 Cor 6:14-16): 'What fellowship can light have with darkness? What agreement is there between the temple of God and idols?' Paul's covenant-exclusivity language echoes the Judges 2 prohibition."}
    ],
    "10": [
      {"type": "allusion", "target": "Heb 3:12-13", "note": "There arose another generation who did not know the LORD — the pattern of generational apostasy is precisely the danger Hebrews warns against: 'See to it that none of you has a sinful, unbelieving heart that turns away from the living God; encourage one another daily, as long as it is called today, so that none of you may be hardened by sin's deceitfulness.' The Judges cycle of forgetting God between generations is the OT precedent Hebrews addresses."}
    ],
    "11": [
      {"type": "allusion", "target": "Rom 1:21-23", "note": "They served the Baals... they went after other gods from among the gods of the peoples around them — the Baalism of the Judges period is the covenant-community instance of the universal pattern Paul describes in Romans 1: 'although they knew God, they neither glorified him as God... they exchanged the glory of the immortal God for images.' Israel's abandonment of YHWH for Baal is the specific historical case of the distortion Paul generalizes for all humanity."}
    ],
    "14": [
      {"type": "allusion", "target": "Acts 7:42", "note": "He gave them over to plunderers who plundered them — God's 'giving over' (<em>nathan beyad</em>) of the apostate community to their enemies anticipates Paul's <em>paredōken</em> (gave them over) in Romans 1:24,26,28 and Stephen's quotation in Acts 7:42 ('God turned away and gave them over'). The divine handing-over pattern of covenant-discipline in Judges is the OT root of the Romans 1 sequence."}
    ],
    "16": [
      {"type": "allusion", "target": "Acts 13:20", "note": "Then the LORD raised up judges who saved them — Paul's synagogue sermon at Pisidian Antioch places the judges in the salvation-history timeline: 'after that, he gave them judges for about 450 years until Samuel the prophet.' The judges are the penultimate chapter in the sequence from the exodus through David to Jesus, establishing them as the period whose providential function was to lead toward the messianic King."}
    ],
    "18": [
      {"type": "allusion", "target": "Heb 2:17-18", "note": "The LORD was moved to compassion by their groaning because of those who afflicted them — the divine compassion that drove the raising of judges in response to Israel's suffering under oppression is the OT pattern for Hebrews' claim that Christ 'had to be made like his brothers and sisters in every way, in order that he might become a merciful and faithful high priest' (Heb 2:17). The judge moved to act by the groaning of the oppressed people anticipates the high priest who sympathizes with human weakness."}
    ]
  },
  "3": {
    "9": [
      {"type": "type", "target": "Acts 13:23", "note": "The LORD raised up a deliverer for Israel, Othniel — the pattern of God raising up deliverers (<em>mōshia'</em>) in response to Israel's cry is the OT structural template for Acts 13:23: 'from David's descendants, God has brought to Israel the Savior Jesus, as he promised.' Each Judges deliverer is an instance of the pattern that culminates in Jesus; Othniel is the first and most complete judge (no recorded failure), making him the clearest type of the perfect Deliverer."}
    ],
    "10": [
      {"type": "type", "target": "Luke 4:18", "note": "The Spirit of the LORD was upon him, and he judged Israel — the Spirit-equipping of Othniel for judicial and military leadership is the OT structural pattern for the Spirit-anointing that qualifies Jesus for his messianic mission. Luke 4:18 (Jesus reads Isa 61:1: 'the Spirit of the Lord is upon me') activates the same formula. Each judge on whom the Spirit came was an anticipation of the one upon whom the Spirit would rest permanently (Isa 11:2; John 1:32-33)."},
      {"type": "allusion", "target": "Acts 10:38", "note": "The Spirit of the LORD was upon him, and he judged Israel — Peter's summary of Jesus's ministry deploys the same formula: 'God anointed Jesus of Nazareth with the Holy Spirit and power, and he went about doing good... because God was with him.' The Spirit-plus-divine-presence combination qualifies Othniel; the same combination, permanently and perfectly realized, characterizes Jesus's ministry."}
    ],
    "15": [
      {"type": "type", "target": "Heb 11:32", "note": "The LORD raised up for them a deliverer, Ehud the son of Gera — Hebrews 11:32 names Gideon, Barak, Samson, and Jephthah explicitly, then adds 'and what more shall I say? For time would fail me to tell of...' all the others. Ehud, the second judge, belongs to the same paradigm of faith-enabled deliverance that Hebrews celebrates: ordinary people through whom God accomplished extraordinary rescue."}
    ],
    "28": [
      {"type": "allusion", "target": "Rom 8:37", "note": "The LORD has given your enemies the Moabites into your hand — the formula of divine empowerment recurrent through Judges ('the LORD has given into your hand') is the OT vocabulary of victory that Paul distills in Romans 8:37: 'we are more than conquerors through him who loved us.' The judges' victories are won not by superior military force but by divine gift; the NT's confidence of spiritual victory derives from the same source."}
    ]
  }
}

def main():
    e = load_echo('judges')
    merge_echo(e, ECHO)
    merge_echo(e, ECHO_1_3)
    save_echo('judges', e)

    c = load_comm('mkt-original', 'judges')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', 'judges', c)

    c = load_comm('mkt-context', 'judges')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'judges', c)

    c = load_comm('mkt-christ', 'judges')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'judges', c)

    print('judges: all 4 layers written')

if __name__ == '__main__':
    main()
