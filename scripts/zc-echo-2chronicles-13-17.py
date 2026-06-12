"""
Echo Layer — 2 Chronicles chapters 13–17
Run: python3 scripts/zc-echo-2chronicles-13-17.py

Key echo connections in this range:
- 13:5: "salt covenant" → Lev 2:13; Num 18:19; Mark 9:49-50
- 13:12: "Do not fight against YHWH" → Acts 5:39
- 14:7: seek the LORD and have rest → Heb 4:9-10
- 14:11: Asa's prayer — the few against the many → 2 Cor 12:9
- 15:2: "Seek him and he will be found" → Matt 7:7-8; Jas 4:8
- 15:7: reward will not be taken away → Heb 10:35
- 16:9: eyes of the LORD run to and fro → Zech 4:10; Rev 5:6
- 17:9: teaching the law throughout Judah → Matt 28:20
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

CHRON2_ECHO_13_17 = {
  "13": {
    "5": [
      {"type": "allusion", "target": "Num 18:19", "note": "Abijah declares that YHWH gave the kingdom to David and his sons by a &#8220;salt covenant&#8221; (ḥuqqat melaḥ) — the permanent, incorruptible bond ratified by the priestly use of salt in all offerings (Lev 2:13; Num 18:19); the salt covenant is the Chronicler&#8217;s way of asserting the absolute irrevocability of the Davidic promise, anticipating Paul&#8217;s &#8220;the gifts and calling of God are irrevocable&#8221; (Rom 11:29) and the surety of the new covenant ratified in Christ&#8217;s own body"}
    ],
    "12": [
      {"type": "allusion", "target": "Acts 5:39", "note": "Abijah&#8217;s battle-speech ends: &#8220;Do not fight against the LORD, the God of your fathers, for you cannot succeed&#8221; — the warning that resistance to YHWH&#8217;s purposes is futile; Gamaliel echoes this logic before the Sanhedrin: &#8220;if it is of God, you will not be able to overthrow them — you might even be found opposing God!&#8221; (Acts 5:39); the Chronicler&#8217;s military-political principle becomes the NT&#8217;s apostolic-political principle"}
    ]
  },
  "14": {
    "7": [
      {"type": "allusion", "target": "Heb 4:9", "note": "Asa&#8217;s policy statement — &#8220;the land is still ours because we have sought (dāraš) the LORD our God&#8221; — links covenant faithfulness to the &#8220;rest&#8221; (mᵉnûḥāh) he gives the land; the author of Hebrews reads this rest-through-seeking pattern into the Sabbath rest that remains for the people of God (Heb 4:9-10): those who &#8220;strive to enter that rest&#8221; (Heb 4:11) by faith are doing what Asa did by dāraš; the Chronicler&#8217;s link between seeking YHWH and receiving rest is the OT grammar of Heb 4"}
    ],
    "11": [
      {"type": "allusion", "target": "2 Cor 12:9", "note": "Asa prays before the Cushite army of 300 chariots and 900,000 men: &#8220;There is no difference for you between helping the many or those who have no power. Help us, O LORD our God, for we rely on you, and in your name we have come against this multitude&#8221; — the theology of divine power perfected in human weakness (2 Cor 12:9); as the 300 at Gideon&#8217;s side (Judg 7) and Asa&#8217;s smaller force demonstrate, YHWH&#8217;s power is most visible when the odds are humanly impossible"},
      {"type": "allusion", "target": "Heb 11:34", "note": "Asa&#8217;s prayer &#8220;in your name we have come against this multitude&#8221; and subsequent victory over the Cushite army places him in the Hebrews 11 gallery of those who &#8220;became mighty in war, put foreign armies to flight&#8221; (Heb 11:34) through faith — not military superiority but trust in YHWH as the decisive factor; the name-of-YHWH theology of 2 Chr 14:11 is the OT basis of the NT&#8217;s &#8220;in the name of Jesus&#8221; formula"}
    ]
  },
  "15": {
    "2": [
      {"type": "allusion", "target": "Matt 7:7", "note": "Azariah&#8217;s oracle — &#8220;The LORD is with you while you are with him. If you seek him (dᵉrāšûhû), he will be found by you&#8221; — is the OT grammar that Jesus transmutes into &#8220;Seek and you will find&#8221; (Matt 7:7-8); the Chronicler&#8217;s theology of seekable divine presence becomes the Sermon on the Mount&#8217;s promise; James echoes both: &#8220;Draw near to God and he will draw near to you&#8221; (Jas 4:8); the mutuality of divine-human approach is the covenantal logic running from Azariah to Jesus to James"},
      {"type": "allusion", "target": "Jas 4:8", "note": "&#8220;If you seek him, he will be found by you, but if you forsake him, he will forsake you&#8221; (2 Chr 15:2) — the symmetry of divine-human relationship that James captures as &#8220;Draw near to God and he will draw near to you; cleanse your hands, you sinners, and purify your hearts, you double-minded&#8221; (Jas 4:8); both texts place covenantal responsiveness (divine seeking of seekers) alongside the corresponding covenantal warning against half-heartedness"}
    ],
    "7": [
      {"type": "allusion", "target": "Heb 10:35", "note": "Azariah&#8217;s charge: &#8220;But you, take courage! Do not let your hands be weak, for your work will be rewarded&#8221; (2 Chr 15:7) — the same exhortation the author of Hebrews gives the wavering community: &#8220;Therefore do not throw away your confidence, which has a great reward&#8221; (Heb 10:35); the OT precedent of courageous faithfulness yielding divine reward becomes the NT argument for perseverance; 1 Cor 15:58 is the Pauline form: &#8220;your labor in the Lord is not in vain&#8221;"}
    ],
    "12": [
      {"type": "allusion", "target": "Deut 29:1", "note": "The whole-assembly covenant renewal — &#8220;they entered into a covenant to seek the LORD, the God of their fathers, with all their heart and with all their soul&#8221; — reprises the Mosaic covenant-renewal structure of Deut 29; as Josiah later holds a covenant renewal (2 Chr 34:31-32), Asa&#8217;s assembly demonstrates the recurring pattern of covenant re-entrancein the old covenant: the people corporately commit to what was already asked of them; the new covenant promise (Jer 31:31-34) is that this re-entrancewill no longer be needed — the law written on the heart cannot be renewed because it is never fully absent"}
    ]
  },
  "16": {
    "9": [
      {"type": "allusion", "target": "Zech 4:10", "note": "Hanani&#8217;s oracle — &#8220;For the eyes of the LORD run to and fro throughout the whole earth, to give strong support to those whose heart is blameless (šālēm) toward him&#8221; — is echoed by the vision of the seven eyes on the plumb-line stone (Zech 4:10: &#8220;these seven rejoice to see the plumb line in the hand of Zerubbabel; they are the eyes of the LORD, which range through the whole earth&#8221;); both texts establish the same divine omniscience actively seeking whole-hearted devotion across the whole earth"},
      {"type": "type", "target": "Rev 5:6", "note": "The &#8220;eyes of the LORD running to and fro throughout the whole earth&#8221; (2 Chr 16:9; Zech 4:10) finds its NT antitype in the seven eyes of the Lamb in Rev 5:6: &#8220;the seven spirits of God sent out into all the earth&#8221; — the same divine omniscience that Hanani invokes as the ground of covenant faithfulness is now embodied in the crucified-and-risen Lamb; what was an abstract divine attribute in the OT becomes a concrete feature of the glorified Christ who sees and supports those whose heart is undivided toward him"}
    ]
  },
  "17": {
    "6": [
      {"type": "allusion", "target": "1 Cor 16:13", "note": "Jehoshaphat&#8217;s heart was &#8220;courageous in the ways of the LORD&#8221; (wayyigbah libbô bᵉdarḵê YHWH) — the same warrior-courage vocabulary that Paul adapts to the new covenant: &#8220;be watchful, stand firm in the faith, act like men, be strong&#8221; (1 Cor 16:13); the Chronicler&#8217;s ideal of the king whose heart is brave for YHWH&#8217;s ways becomes the apostle&#8217;s vision for the whole congregation; courage in the ways of God is not a royal but a communal virtue in the new covenant"}
    ],
    "9": [
      {"type": "shadow", "target": "Matt 28:20", "note": "Jehoshaphat sends officials, Levites, and priests throughout all the cities of Judah with the Book of the Law to teach — a national torah-teaching initiative reaching every city; this is the OT shadow of the Great Commission: &#8220;teaching them to observe all that I have commanded you&#8221; (Matt 28:20); as Jehoshaphat&#8217;s teachers went to every city of Judah, Christ&#8217;s disciples go to every nation; the torah being taught shifts from the Mosaic law to the law of Christ (Gal 6:2; 1 Cor 9:21), but the structure of commissioned teachers going to every place is preserved and universalized"}
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRON2_ECHO_13_17)
    save_echo('2chronicles', existing)
    print('2 Chronicles 13-17 echo layer written.')

if __name__ == '__main__':
    main()
