"""
echo | Numbers | chapters 25–26
Run: python3 scripts/zc-echo-numbers-25-26-fill.py

Ch 25: Baal Peor apostasy (1 Cor 10:8 / Rev 2:14); Phinehas's covenant of perpetual
       priesthood types Heb 7:24; his zeal reckoned as righteousness (Ps 106:31).
Ch 26: Second census — sons of Korah survive (Korah-psalm tradition, Ps 84);
       land by lot (Acts 1:26); only Joshua/Caleb survive = faith-entry type (Heb 3:19).
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
  "25": {
    "1": [
      {"type": "allusion", "target": "1 Cor 10:8", "note": "While Israel lived in Shittim, the people began to whore with the daughters of Moab and eat at their sacrifices — the Baal Peor apostasy combines sexual immorality and pagan worship in a single act of covenant defection. Paul explicitly cites this event: &ldquo;We must not indulge in sexual immorality as some of them did, and twenty-three thousand fell in a single day&rdquo; (1 Cor 10:8). The Shittim incident is Paul's paradigmatic warning against presuming on covenant privilege; Israel's election did not protect them from the consequences of Peor-style apostasy, and neither does Christian initiation protect from analogous defection."},
      {"type": "allusion", "target": "Rev 2:14", "note": "Israel's sexual immorality with Moabite women and eating of pagan sacrificial meals at Baal Peor is the backdrop for the Pergamum letter's charge: &ldquo;you have some there who hold the teaching of Balaam, who taught Balak to put a stumbling block before the sons of Israel, so that they might eat food sacrificed to idols and practice sexual immorality&rdquo; (Rev 2:14). Numbers 31:16 identifies Balaam as the one who counseled this strategy; Revelation recasts Peor-style compromise as the &ldquo;teaching of Balaam&rdquo; — a doctrine of accommodation to pagan culture that recapitulates the wilderness apostasy within the churches."}
    ],
    "12": [
      {"type": "type", "target": "Heb 7:24", "note": "YHWH gives Phinehas &ldquo;my covenant of peace, and it shall be for him and for his descendants after him the covenant of a perpetual priesthood&rdquo; (vv.12-13) — this is the only place in the Torah where an individual Levite receives a covenant of perpetual priesthood. Hebrews 7:24 declares of Christ: &ldquo;he holds his priesthood permanently, because he continues forever.&rdquo; The Phinehas covenant establishes the type of a priesthood that does not pass from one generation to another but persists in a single person who intercedes and stops God's wrath; Christ fulfills this as the one whose once-for-all intercession (Heb 7:25) permanently ends the plague of sin and death."}
    ],
    "13": [
      {"type": "allusion", "target": "Ps 106:31", "note": "Phinehas's action — executing the Israelite man and Midianite woman in flagrante delicto — stops the plague and YHWH declares that Phinehas &ldquo;was zealous with my jealousy among them.&rdquo; Psalm 106:30-31 cites this as a reckoning event: &ldquo;Then Phinehas stood up and intervened, and the plague was stayed. And that was counted to him as righteousness from generation to generation forever.&rdquo; The vocabulary of &ldquo;reckoned/counted as righteousness&rdquo; (the same root as Gen 15:6 for Abraham) is applied to Phinehas's zealous intercessory act — establishing that righteousness-reckoning is not exclusive to faith but encompasses the priestly intervention that turns away wrath, the pattern Christ fulfills as the ultimate intercessor (Rom 8:34)."}
    ]
  },
  "26": {
    "11": [
      {"type": "allusion", "target": "Ps 84:1", "note": "The second census notes: &ldquo;But the sons of Korah did not die&rdquo; (v.11) — a parenthetical survival notice that is theologically charged. Korah's rebellion ended in divine judgment that swallowed Korah himself (Num 16:32-33), yet his sons survived and became the authors of Psalms 42-49, 84-85, 87-88. These Korah psalms express the deepest yearnings for the presence of God: &ldquo;How lovely is your dwelling place, O LORD of hosts!&rdquo; (Ps 84:1). The survival of Korah's sons despite their father's rebellion against Moses and Aaron is a type of grace that preserves a worshipping remnant through judgment — a remnant whose praise of the temple and longing for God's courts becomes canonical Scripture."}
    ],
    "55": [
      {"type": "allusion", "target": "Acts 1:26", "note": "The land of Canaan is to be apportioned by lot among the tribes according to their census numbers (vv.55-56): &ldquo;But the land shall be divided by lot.&rdquo; The use of lot-casting to determine YHWH's allocation — removing human preference and placing decision in divine hands — becomes the biblical procedure for discerning God's will in matters of distribution. Acts 1:26 follows this exact precedent when the apostles must replace Judas: &ldquo;And they cast lots for them, and the lot fell on Matthias, and he was numbered with the eleven apostles.&rdquo; The Canaan-distribution-by-lot in Numbers 26 establishes the theological warrant for the apostolic use of lots as a divine-selection mechanism."}
    ],
    "65": [
      {"type": "allusion", "target": "Heb 3:19", "note": "The second census concludes: &ldquo;not one of them was left except Caleb the son of Jephunneh and Joshua the son of Nun&rdquo; (v.65) — the entire generation that left Egypt has died in the wilderness in fulfillment of YHWH's judgment after the Kadesh rebellion (Num 14). The two exceptions are those who &ldquo;wholly followed YHWH&rdquo; (Num 14:24) — who trusted the divine promise when the rest did not. Hebrews 3:19 draws the theological conclusion: &ldquo;So we see that they were unable to enter because of unbelief.&rdquo; The census arithmetic of Num 26 — the absence of all except two faithful ones — is the numerical demonstration of the Hebrews thesis that the wilderness generation perished not because of ethnic or ritual deficiency but because of unbelief, and that the entry into rest is therefore available to any who do not harden their hearts (Heb 3:15)."}
    ]
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, ECHO)
    save_echo('numbers', e)
    print('Numbers 25-26 echo written.')

if __name__ == '__main__':
    main()
