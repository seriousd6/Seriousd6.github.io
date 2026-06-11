"""
Echo layer — Joshua 15–17
Run: python3 scripts/zc-echo-joshua-15-17.py

OT→NT direction: target = NT verse that takes up the OT passage.

Key decisions:
- Ch 15: boundary/town list chapters; selected verses with genuine NT uptake.
  v8 Valley of Hinnom → Gehenna (Matt 5:22): the specific toponym Jesus
  repurposes as his primary image of final judgment.
  v13-14 Caleb's faith → Heb 11 pattern: active conquest of giants at old age.
  v18-19 Achsah's springs request → John 16:24 ask-and-receive pattern.
  v63 Jebusites undriven → Heb 4:8 argument; David's later conquest (2 Sam 5:7)
  and the eschatological city (Rev 21:2) complete what Joshua left incomplete.
- Ch 16: Ephraim boundaries; v10 forced-labor compromise → partial obedience
  theme underlying Heb 3:7-11 'harden not your hearts' warning.
- Ch 17: Zelophehad's daughters reappear (vv.3-6) → Gal 3:28-29 inheritance
  without gender distinction. Joseph tribes' complaint (vv.14-18) → Heb 4:11
  striving to enter rest; faith over fear of iron chariots.
- No parallels file entries for chs 15–17.
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

JOSHUA_ECHOES_15_17 = {
    "15": {
        "8": [
            {"type": "allusion", "target": "Matt 5:22",
             "note": "The 'valley of the son of Hinnom' (<em>gê ben-Hinnom</em>) appears here as a boundary marker south of Jerusalem. By the Second Temple period it had become a burning refuse site, and Jesus' term <em>Gehenna</em> (Matt 5:22, 29-30; Mark 9:43) derives directly from this valley name — transforming a geographical landmark of Joshua's land survey into the NT's primary image of final judgment. The toponym carries the weight of defilement: Ahaz and Manasseh later sacrificed children there (2 Chr 28:3; 33:6), making it a site associated with the most extreme covenant violation."}
        ],
        "13": [
            {"type": "allusion", "target": "Heb 11:6",
             "note": "Caleb, now 85 years old (Josh 14:10), actively drives out the three Anakim clans — Sheshai, Ahiman, and Talmai — from Hebron. The same faith that sustained his minority report in Num 13:30 ('we are well able to overcome it') is still operative decades later in active conquest. This is the faith-as-endurance that Heb 11 catalogs: not a static trust but one that holds across the wilderness years and still moves toward the promise at the end. The Anakite giants are the very obstacle that caused the whole generation to fall in the wilderness (Num 14:1-4)."}
        ],
        "18": [
            {"type": "allusion", "target": "John 16:24",
             "note": "Achsah urges Othniel to ask her father Caleb for a field, and then herself dismounts and asks Caleb for the upper and lower springs to supplement the dry Negeb land she has received. Her request is granted without dispute. The narrative pattern — a daughter approaching her father to ask, receiving what she asks because she is already an heir — is the relational structure Jesus describes: 'Until now you have asked nothing in my name. Ask, and you will receive, that your joy may be full' (John 16:24). The daughter's boldness in petition, grounded in established inheritance, anticipates the believer's access to the Father through the Son."}
        ],
        "63": [
            {"type": "allusion", "target": "Heb 4:8",
             "note": "The Jebusites in Jerusalem are not driven out and remain 'to this day' — the conquest is explicitly incomplete at Jerusalem, the city that will become David's capital and the seat of the temple. The author of Hebrews argues that Joshua's inability to give complete rest (Heb 4:8, citing the Psalm 95 warning given generations after Joshua) proves that a greater rest remains. The undriven Jebusites are a specific instance of the broader pattern: Joshua's conquest established a real but provisional rest, which David's capture of Jebus (2 Sam 5:6-9) and ultimately the eschatological Jerusalem (Rev 21:2) will complete."},
            {"type": "shadow", "target": "Rev 21:2",
             "note": "Jerusalem — the city Judah could not fully take from the Jebusites (v63) — stands as an unfinished inheritance throughout the OT period. The arc runs from the failed Judahite conquest here to David's capture of Jebus (2 Sam 5:7), to Solomon's temple, to the fall and exile, and finally to John's vision of the holy city 'coming down out of heaven from God, prepared as a bride adorned for her husband' (Rev 21:2). The earthly city that could never be fully secured points to the heavenly one that needs no human military effort."}
        ]
    },
    "16": {
        "10": [
            {"type": "allusion", "target": "Heb 3:11",
             "note": "Ephraim does not drive out the Canaanites from Gezer but instead reduces them to forced labor — partial compliance where the command required complete separation. This becomes a recurring pattern in the land-taking (cf. Judg 1:28-33) that eventually leads to the syncretism and apostasy the prophets warn against. The wilderness generation's failure (Heb 3:11 cites Ps 95:11: 'they shall not enter my rest') stemmed from the same root: willingness to coexist with what God declared incompatible with covenant life. The forced-labor compromise is the land-conquest analogue of a hardened heart."}
        ]
    },
    "17": {
        "3": [
            {"type": "allusion", "target": "Gal 3:29",
             "note": "Zelophehad's five daughters — Mahlah, Noah, Hoglah, Milcah, and Tirzah — present their case again before Eleazar, Joshua, and the leaders (first established in Num 27:1-11; confirmed by Moses). They receive their inheritance among their father's brothers. Paul's declaration that 'if you are Christ's, then you are Abraham's offspring, heirs according to promise' (Gal 3:29), immediately preceded by 'there is neither male nor female' (Gal 3:28), takes up the pattern these daughters embody: gender is not a barrier to covenant inheritance. Their claim is not a special exception but a ruling that establishes the principle — a principle the NT sees completed in Christ."}
        ],
        "6": [
            {"type": "allusion", "target": "Gal 3:28",
             "note": "The ruling that Zelophehad's daughters receive an inheritance alongside their father's brothers (v6) is a juridical decision with theological weight: female descendants hold equal standing in the distribution of the land that represents covenant participation. Paul's 'neither male nor female, for you are all one in Christ Jesus' (Gal 3:28) is not importing a foreign concept but drawing out what the Mosaic covenant itself established through this precedent — that covenant membership and its inheritance are not conditioned on gender."}
        ],
        "14": [
            {"type": "allusion", "target": "Heb 4:11",
             "note": "The Joseph tribes complain that one allotment is insufficient for their large numbers, despite already possessing the hill country. Joshua's reply is pointed: 'If you are a numerous people, go up by yourselves to the forest, and there clear ground for yourselves' (v15). The inheritance is real but requires active engagement to realize — the forest must be felled, the Perizzites and Rephaim must be driven out. The author of Hebrews urges 'let us strive to enter that rest, so that no one may fall by the same sort of disobedience' (Heb 4:11): covenant rest is promised and real, but it is entered through active faith, not passive waiting. The tribes' complaint — we want more but we have not yet cleared what we already hold — names the failure mode exactly."},
            {"type": "allusion", "target": "Matt 17:20",
             "note": "The Joseph tribes fear the Canaanites 'who have iron chariots' (v16, 18), the superior military technology of the plains. Joshua's response does not remove the obstacle but commands faith: 'you shall drive out the Canaanites, though they have iron chariots and though they are strong' (v18), because the LORD is with them. The iron chariot is the OT analogue of the immovable mountain Jesus addresses in Matt 17:20: 'if you have faith like a grain of mustard seed, you will say to this mountain, &#8220;Move from here to there,&#8221; and it will move.' Superior opposing force does not determine outcomes when the LORD has spoken the grant."}
        ],
        "18": [
            {"type": "theme", "target": "Rom 8:37",
             "note": "Joshua's declaration to the house of Joseph — 'you shall drive out the Canaanites, though they have iron chariots and though they are strong' (v18) — grounds confidence not in Israel's military capability but in the LORD's prior grant of the land. The theme of victory through the power of the One who promises, not through human capacity, runs from this command through Paul's 'we are more than conquerors through him who loved us' (Rom 8:37). The Joseph tribes' fear is understandable; the command stands because the victor is not them."}
        ]
    }
}

def main():
    existing = load_echo('joshua')
    merge_echo(existing, JOSHUA_ECHOES_15_17)
    save_echo('joshua', existing)
    print('Joshua 15–17 echoes written.')

if __name__ == '__main__':
    main()
