"""
Echo Layer — Nehemiah chapter 13
Run: python3 scripts/zc-echo-nehemiah-13-13.py

Key echo connections in this range:
- 13:1-3: Ammonite/Moabite exclusion from the assembly → Deut 23:3-5 (cited); Eph 2:12-13 (those far off brought near)
- 13:4-9: Temple storeroom given to Tobiah → John 2:13-17 (Jesus cleanses the temple)
- 13:10-12: Levites return to their fields / tithes unpaid → Mal 3:10 (bring tithes into storehouse)
- 13:14: "Do not blot out my good deeds" → Heb 6:10 (God will not forget faithful work)
- 13:17-18: Sabbath profanation warning — ancestors did this and judgment followed → Isa 58:13; Heb 4:9-11
- 13:22: "Spare me according to the greatness of your steadfast love (ḥesed)" → Lam 3:22; Heb 4:16
- 13:26: Solomon led astray by foreign wives — the covenant-breaking king → 1 Kgs 11:4; 2 Cor 6:14
- 13:31: Final "Remember me for good" closes the memoir → Heb 7:25 (Christ's perpetual intercession)
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

NEH_ECHO_13 = {
  "13": {
    "1": [
      {"type": "quote", "target": "Deut 23:3", "note": "&#8220;On that day they read from the Book of Moses... that no Ammonite or Moabite should ever enter the assembly of God&#8221; — Nehemiah 13:1-2 is a direct citation of Deuteronomy 23:3-5, itself the basis for the exclusion policy; the reading of the Torah triggers immediate covenant enforcement — the word read creates the community it describes; this is the OT pattern for the public reading of Scripture as constitutive of community identity that Nehemiah 8&#8217;s great assembly established"},
      {"type": "allusion", "target": "Eph 2:12", "note": "The Ammonite and Moabite exclusion from the assembly (<em>qāhāl</em>) is precisely the &#8220;excluded from the commonwealth of Israel&#8221; status that Paul describes in Ephesians 2:12 — and which Christ abolishes: &#8220;but now in Christ Jesus you who once were far off have been brought near by the blood of Christ&#8221; (Eph 2:13); the boundary that Nehemiah enforces is provisional, not final — the wall Christ breaks down (Eph 2:14) is the same wall that Nehemiah&#8217;s assembly is drawing tight"}
    ],
    "2": [
      {"type": "allusion", "target": "Num 22:5", "note": "&#8220;They had not welcomed Israel with food and water, but had hired Balaam to curse them — yet our God turned the curse into a blessing&#8221; — Nehemiah 13:2 rehearses Numbers 22-24: the Moabite king Balak hired Balaam to curse Israel, but YHWH turned the oracle into blessing; the subversion of hired opposition by divine sovereignty is the same pattern that runs through Nehemiah&#8217;s own memoir (hired false prophets, hired counselors) — every attempt to use money to defeat God&#8217;s purposes is reversed"}
    ],
    "4": [
      {"type": "allusion", "target": "John 2:14", "note": "Eliashib the priest had prepared a large room for Tobiah — a political ally and covenant enemy — in the storerooms of the temple, displacing the grain offerings, incense, and Levitical tithes; this is the OT type of the temple desecration that Jesus confronts: &#8220;In the temple he found those who were selling oxen and sheep and pigeons, and the money-changers sitting there&#8221; (John 2:14); both Nehemiah and Jesus respond to the conversion of sacred space to commercial-political use with forcible expulsion; the pattern — the house of God corrupted by human convenience and politics, then cleansed — runs from Nehemiah to the Second Temple"}
    ],
    "8": [
      {"type": "allusion", "target": "John 2:17", "note": "&#8220;I was deeply displeased and threw all of Tobiah&#8217;s household belongings out of the room&#8221; — Nehemiah&#8217;s physical expulsion of Tobiah&#8217;s furnishings is the OT counterpart to Jesus&#8217; cleansing of the temple: &#8220;he drove them all out of the temple... and he poured out the coins of the money-changers and overturned their tables&#8221; (John 2:15); the disciples interpret Jesus&#8217; action through Ps 69:9: &#8220;zeal for your house will consume me&#8221; (John 2:17); Nehemiah&#8217;s zeal for the house of God is the OT form of the same passion for the sanctity of YHWH&#8217;s dwelling"}
    ],
    "10": [
      {"type": "allusion", "target": "Mal 3:10", "note": "&#8220;The portions due the Levites had not been given to them, and the Levites and singers who served had each fled back to their own fields&#8221; — Nehemiah 13:10 is the historical situation that Malachi 3:10 responds to: &#8220;Bring the full tithe into the storehouse, that there may be food in my house&#8221; — Malachi&#8217;s prophecy is addressed to a community doing exactly what Nehemiah here confronts: withholding the tithes that fund the temple ministry, causing the Levites to abandon their posts and return to subsistence agriculture; Nehemiah and Malachi are contemporaries addressing the same crisis"}
    ],
    "14": [
      {"type": "allusion", "target": "Heb 6:10", "note": "&#8220;Remember me, O my God, for this, and do not blot out (<em>ʾal-timḥeh</em>) the good deeds I have done for the house of my God&#8221; — Nehemiah&#8217;s appeal against erasure is the OT form of the assurance Hebrews gives: &#8220;God is not unjust so as to overlook your work and the love that you have shown for his name in serving the saints&#8221; (Heb 6:10); both texts address the anxiety that faithful labor for God&#8217;s house might go unnoticed and unrewarded; the NT grounds what Nehemiah prays for in the character of God rather than in his own record"}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 58:13", "note": "Nehemiah confronts the Sabbath merchants: &#8220;What is this evil thing you are doing — profaning the Sabbath day?&#8221; — Isaiah 58:13 is the prophetic basis for Nehemiah&#8217;s concern: &#8220;If you turn back your foot from the Sabbath, from doing your pleasure on my holy day... then you shall take delight in the LORD&#8221;; both Isaiah and Nehemiah understand Sabbath observance not as arbitrary rule-keeping but as the act of covenant loyalty that embodies trust in God&#8217;s provision rather than commercial anxiety"},
      {"type": "allusion", "target": "Heb 4:9", "note": "Nehemiah&#8217;s Sabbath enforcement — shutting the gates at dusk before the Sabbath, stationing guards to prevent trade — is the OT form of the Sabbath-rest that Hebrews 4 theologizes: &#8220;there remains a Sabbath rest for the people of God&#8221; (Heb 4:9); the physical Sabbath that Nehemiah enforces is the shadow of the eschatological rest that Christ makes available; Hebrews 4:10-11 applies the same warning as Nehemiah 13:18: those who violated the Sabbath in the wilderness fell, so &#8220;let us strive to enter that rest, so that no one may fall&#8221;"}
    ],
    "18": [
      {"type": "allusion", "target": "Ezek 20:13", "note": "&#8220;Did your ancestors not do the same, and did our God not bring all this disaster on us and on this city?&#8221; — Nehemiah&#8217;s appeal to the historical pattern: Sabbath violation → exile; Ezekiel 20:13 makes the same argument: &#8220;the house of Israel rebelled against me in the wilderness... they did not walk in my statutes, and they rejected my rules... and they greatly profaned my Sabbaths&#8221;; Ezekiel identifies Sabbath-breaking as the symbolic act of covenant rejection that made exile inevitable; Nehemiah&#8217;s warning applies this pattern to the second-generation returnees"}
    ],
    "22": [
      {"type": "allusion", "target": "Lam 3:22", "note": "&#8220;Remember me, O my God, for this as well, and spare me according to the greatness of your steadfast love (<em>ḥasḏᵉḵā</em>)&#8221; — Nehemiah&#8217;s closing petition invokes <em>ḥesed</em> — covenant loyalty/steadfast love — as the ground of appeal; Lamentations 3:22 is the theological articulation of the same ground: &#8220;The steadfast love (<em>ḥᵃsāḏê</em>) of the LORD never ceases; his mercies never come to an end&#8221;; both texts show the post-exilic community reaching beyond its own merit to YHWH&#8217;s character as the basis of hope"},
      {"type": "allusion", "target": "Heb 4:16", "note": "&#8220;Spare me according to the greatness of your steadfast love&#8221; — the appeal to divine mercy as the ground for approaching God in need; Hebrews 4:16 grounds the NT parallel in the high priesthood of Christ: &#8220;let us then with confidence draw near to the throne of grace, that we may receive mercy and find grace to help in time of need&#8221;; what Nehemiah appeals to through his &#8220;Remember me&#8221; prayers, the NT community approaches through the living mediator who is himself the expression of YHWH&#8217;s <em>ḥesed</em>"}
    ],
    "26": [
      {"type": "allusion", "target": "1 Kgs 11:4", "note": "&#8220;Was it not because of women like these that Solomon king of Israel sinned?... yet even he was led into sin by foreign women&#8221; — Nehemiah explicitly cites Solomon as the warning archetype for the covenant-breaking power of marriage outside the faith community; 1 Kings 11:4: &#8220;when Solomon was old his wives turned away his heart after other gods, and his heart was not wholly true to the LORD his God&#8221; — the very language of the lēḇāḇ šālēm (undivided heart) that Solomon himself lacked; the king who built the temple became the paradigm case of theological compromise through relational entanglement"},
      {"type": "allusion", "target": "2 Cor 6:14", "note": "Nehemiah&#8217;s prohibition on intermarriage with Ammonite, Moabite, and Ashdodite women — grounded in Solomon&#8217;s failure — is the OT precedent for Paul&#8217;s instruction: &#8220;do not be unequally yoked with unbelievers&#8221; (2 Cor 6:14); the Pauline prohibition is broader (any unbeliever, not specific ethnic groups) and grounded in the NT doctrine of the body as the temple of the Holy Spirit, but the underlying logic is identical: the primary loyalty to YHWH/Christ cannot coexist with primary relational allegiance to those whose identity is formed by different ultimate commitments"}
    ],
    "29": [
      {"type": "allusion", "target": "Mal 2:4", "note": "&#8220;Remember them, O my God, for they have defiled the priesthood and the covenant of the priests and Levites&#8221; — Nehemiah&#8217;s prayer against the grandson of the high priest who married Sanballat&#8217;s daughter; Malachi 2:4-8 is the prophetic parallel: &#8220;my covenant with him was one of life and peace... but you have turned aside from the way. You have caused many to stumble by your instruction; you have corrupted the covenant of Levi, says the LORD of hosts&#8221;; both texts identify the priestly class&#8217;s covenant betrayal as the most dangerous form of infidelity — the shepherds corrupting rather than protecting the flock"}
    ],
    "31": [
      {"type": "allusion", "target": "Heb 7:25", "note": "&#8220;Remember me, O my God, for good&#8221; — the memoir&#8217;s final word, and the final of Nehemiah&#8217;s five &#8220;Remember me&#8221; appeals (5:19; 13:14, 22, 29, 31); the entire memoir is bracketed by appeals to divine memory as the only ultimate record that matters; Hebrews 7:25 presents what these appeals were pointing toward: &#8220;he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them&#8221;; Nehemiah&#8217;s &#8220;remember me&#8221; is the OT form of the intercession that Christ makes permanently and effectively, not through accumulating a record of deeds but through his eternal priestly presence before the Father"}
    ]
  }
}

def main():
    existing = load_echo('nehemiah')
    merge_echo(existing, NEH_ECHO_13)
    save_echo('nehemiah', existing)
    print('Nehemiah 13 echo layer written.')

if __name__ == '__main__':
    main()
