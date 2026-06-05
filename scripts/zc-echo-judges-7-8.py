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

ECHO_7_8 = {
    "7": {
        "2": [
            {"type": "type", "target": "1 Cor 1:27",
             "note": "God reduces Gideon's army from 32,000 to 300 'lest Israel boast over me, saying, My own hand has saved me.' Paul draws on this exact logic: 'God chose what is weak in the world to shame the strong...so that no human being might boast in the presence of God' (1 Cor 1:27-29). The Gideon reduction is the paradigm of divine victory through insufficient means."},
            {"type": "allusion", "target": "2 Cor 12:9",
             "note": "'My power is made perfect in weakness' — the Lord's word to Paul inverts military common sense in the same way the Gideon reduction did. The smaller the army, the more visible the divine power; when God uses the 300 who remain, the outcome is not in question."}
        ],
        "20": [
            {"type": "type", "target": "2 Cor 4:7",
             "note": "The 300 hold torches hidden inside clay jars — at the signal they break the jars so the light blazes out. Paul uses the identical image for the gospel in the apostle's mortal body: 'we have this treasure in jars of clay, to show that the surpassing power belongs to God and not to us' (2 Cor 4:7). The Gideon image is the OT precedent: divine victory-light hidden in brittle, breakable containers."}
        ],
        "21": [
            {"type": "allusion", "target": "Heb 11:32",
             "note": "Gideon's name appears in the Hebrews 11 Hall of Faith (11:32-33). The Midian defeat stands as his faith-act — his obedience to an implausible strategy (torches in clay jars, 300 men) demonstrates 'the assurance of things hoped for, the conviction of things not seen' (11:1)."}
        ]
    },
    "8": {
        "22": [
            {"type": "allusion", "target": "John 6:15",
             "note": "The people ask Gideon to be their king: 'Rule over us, you and your son.' Gideon refuses: 'The LORD will rule over you.' The pattern inverts in the NT: when the crowd wants to make Jesus king by force after the feeding of the 5,000, he withdraws (John 6:15) — not because kingship is wrong but because the terms and timing are wrong. Gideon correctly refuses; Jesus awaits the cross as the path to his proper crown."}
        ]
    }
}

def main():
    e = load_echo('judges')
    merge_echo(e, ECHO)
    merge_echo(e, ECHO_7_8)
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
