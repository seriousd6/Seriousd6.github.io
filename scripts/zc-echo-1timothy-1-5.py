"""
MKT Echo Layer — 1 Timothy chapters 1–5 (completing ch1, ch4, ch5; ch2-3 already done)
Run: python3 scripts/zc-echo-1timothy-1-5.py

Echo entries cover OT citations, allusions, types, and prophecy-fulfillments.
Key OT connections:
- ch1: Decalogue (vice list mirrors second table); doxology connects to OT
  Kingship psalms and monotheism (Shema); "handed over to Satan" echoes Job 1-2
- ch4: "everything God created is good" = Gen 1:31 allusion; Neh 8 public
  Scripture reading; Num 27 hand-laying ordination
- ch5: Deut 25:4 explicit quotation (muzzled ox); Deut 17:6/19:15 two-witness
  rule; Dan 7 heavenly court imagery
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

ECHOES_1TIM = {
  "1": {
    "1": [
      {"type": "allusion", "target": "Ps 106:21", "note": "God our Savior — the OT title 'God their Savior' (Ps 106:21; Ps 25:5; Isa 43:3) is regularly applied to YHWH in the Psalms and Isaiah; Paul applies it to 'God our Savior' and to 'Christ Jesus our hope,' distributing the divine-Savior title between Father and Son in a proto-Trinitarian pairing"},
      {"type": "allusion", "target": "Jer 17:7", "note": "Christ Jesus our hope — the prophet's beatitude 'blessed is the one who trusts in YHWH, whose hope is YHWH' (Jer 17:7); the OT ground of hope in YHWH is now located specifically in Christ Jesus, making Christ the object of the trust and hope that Jeremiah locates in YHWH"}
    ],
    "9": [
      {"type": "allusion", "target": "Exod 20:1-17", "note": "The vice list of 1 Tim 1:9-10 maps to violations of the Decalogue's second table — lawbreakers/rebels (5th: honor parents); murderers (6th: do not murder); sexually immoral (7th: do not commit adultery); slave traders/kidnappers (8th: do not steal = in ancient application, stealing persons); liars/perjurers (9th: do not bear false witness). The law functions as a diagnostic of sin, not a means of righteousness."}
    ],
    "15": [
      {"type": "allusion", "target": "Ps 51:3-4", "note": "Christ Jesus came into the world to save sinners, of whom I am the foremost — Paul's self-identification as the 'foremost sinner' echoes David's confession in Ps 51 as the paradigmatic sinner pleading for mercy; the chief-sinner claim is a rhetorical intensification of the Davidic penitential tradition applied to the apostle's pre-conversion persecution"},
      {"type": "allusion", "target": "Ezek 34:16", "note": "Christ Jesus came into the world to save sinners — YHWH's promise to seek the lost, strengthen the weak, and heal the sick (Ezek 34:16) is concentrated in the one Shepherd who comes to save those who are lost (cf. Luke 19:10)"}
    ],
    "17": [
      {"type": "allusion", "target": "Ps 10:16", "note": "To the King eternal — YHWH as the eternal/everlasting King (Ps 10:16; Ps 29:10; Ps 145:13; Dan 4:34); the doxology's 'King of the ages' (basilei tōn aiōnōn) applies the OT eternal-kingship title to the one God"},
      {"type": "allusion", "target": "Exod 33:20", "note": "The only God, immortal, invisible — the invisibility of God (Exod 33:20: no one can see my face and live; John 1:18: no one has seen God at any time) grounds the doxology; the God who is invisible to direct perception has made himself known through Christ"},
      {"type": "allusion", "target": "Deut 6:4", "note": "The only God — the Shema's assertion of YHWH's uniqueness (Deut 6:4: YHWH is one) is the OT ground for the doxology's 'only God' (monō theō); Pauline monotheism is always Shema-shaped"}
    ],
    "20": [
      {"type": "allusion", "target": "Job 1:12", "note": "Whom I have handed over to Satan — the disciplinary handing over to Satan echoes the divine permission granted to Satan over Job (Job 1:12: 'everything he has is in your hand'); the Satan-handing-over in 1 Tim 1:20 is a disciplinary ecclesial act, not mere punishment — the goal is that they 'be taught not to blaspheme,' just as Job's suffering led to deeper understanding"}
    ]
  },
  "4": {
    "1": [
      {"type": "allusion", "target": "Dan 11:32", "note": "In later times some will abandon the faith and follow deceiving spirits — Daniel's end-time apostasy (Dan 11:32: those who act wickedly against the covenant he will corrupt with flattery) provides the OT frame for the Spirit's warning about future defection; the 'deceiving spirits' parallel the spiritual deception in Daniel's vision of end-time turbulence"}
    ],
    "3": [
      {"type": "allusion", "target": "Gen 9:3", "note": "Foods, which God created to be received with thanksgiving — God's authorization of all food after the flood (Gen 9:3: every moving thing that lives shall be food for you) is the theological ground for rejecting the false teachers' food prohibitions; the creational permission extends to all food without restriction"}
    ],
    "4": [
      {"type": "allusion", "target": "Gen 1:31", "note": "Everything God created is good — a near-direct allusion to Gen 1:31 (God saw everything that he had made, and behold, it was very good); the creational goodness of all things is the theological basis for the rejection of the ascetic food prohibitions the false teachers impose"}
    ],
    "8": [
      {"type": "allusion", "target": "Prov 3:1-2", "note": "Godliness has value for both the present life and the life to come — Prov 3:1-2 promises that keeping the commandments brings length of days and years of life; Paul's claim extends the promise eschatologically: godliness profits not only for temporal life but for the age to come, a fulfillment and expansion of the wisdom tradition's this-worldly promises"}
    ],
    "10": [
      {"type": "allusion", "target": "Josh 3:10", "note": "The living God, who is the Savior of all people — 'living God' (theos zōn) is an OT divine title distinguishing YHWH from dead idols (Josh 3:10; Ps 42:2; Jer 10:10; Dan 6:26); Paul's application of the living-God title to the one who saves all people (universally, not just Israel) extends the OT contrast between YHWH-the-living and idols to the broadest possible scope"}
    ],
    "13": [
      {"type": "allusion", "target": "Neh 8:1-8", "note": "Devote yourself to the public reading of Scripture — Ezra's public reading of the Law before all Israel (Neh 8:1-8) is the OT paradigm for the liturgical reading of Scripture as a communal formation practice; Timothy's devotion to public reading continues the synagogue and Ezra tradition of Scripture as the community's living constitution"}
    ],
    "14": [
      {"type": "allusion", "target": "Num 27:18-23", "note": "The gift given through prophecy when the body of elders laid their hands on you — the ordination of Joshua by Moses through the laying on of hands (Num 27:18-23: Take Joshua...and lay your hand on him, and invest him with some of your authority) is the OT type for the elder-laying-on-of-hands ordination practice; Timothy's commissioning follows the Mosaic pattern of authorized succession"}
    ]
  },
  "5": {
    "5": [
      {"type": "allusion", "target": "Ps 146:9", "note": "The widow who is really in need puts her hope in God and continues night and day to pray — YHWH's care for widows (Ps 146:9: YHWH watches over the sojourner; he upholds the widow and the fatherless) is the OT ground for the community's obligation to true widows; the widow who prays day and night enacts the trust in YHWH that the Psalms commend"}
    ],
    "10": [
      {"type": "allusion", "target": "Gen 18:1-8", "note": "Showing hospitality, washing the feet of the Lord's people — Abraham's foot-washing of the three visitors (Gen 18:4) and the Psalms' commendation of hospitality stand behind the widow-qualification list; foot-washing is the specific sign of hospitality (cf. Gen 18; Luke 7:44; John 13:14) that marks a genuinely hospitable community member"}
    ],
    "17": [
      {"type": "allusion", "target": "Num 18:21", "note": "Elders who direct the affairs of the church well are worthy of double honor, especially those whose work is preaching and teaching — the Levitical principle of material support for those who serve at the altar (Num 18:21: I give to the Levites all the tithes in Israel as their inheritance in return for their service at the tent of meeting) grounds the principle of paid ministry; the elder-support obligation is the new-covenant extension of the Levitical maintenance principle"}
    ],
    "18": [
      {"type": "fulfillment", "target": "Deut 25:4", "note": "Do not muzzle an ox while it is treading out the grain — the explicit Scripture quotation (cited in 1 Cor 9:9 with the same application); Deut 25:4's command to allow the ox to eat while threshing is read as a divine statement about the right of those who labor in God's service to receive material support; Paul reads the agricultural law as establishing a spiritual-economic principle"}
    ],
    "19": [
      {"type": "fulfillment", "target": "Deut 19:15", "note": "Do not entertain an accusation against an elder unless it is brought by two or three witnesses — the explicit application of Deut 17:6 and 19:15's two-witness judicial requirement to church discipline; the Mosaic law's procedural protection against false accusation (one witness is not enough) is applied directly to the protection of elders from baseless charges"}
    ],
    "21": [
      {"type": "allusion", "target": "Dan 7:10", "note": "In the sight of God and Christ Jesus and the elect angels — the heavenly court imagery draws on Dan 7:10 (thousands upon thousands attended him; ten thousand times ten thousand stood before him; the court sat in judgment) and the broader OT tradition of the divine council; the charge is made before the assembled heavenly witnesses as an oath-formula of maximum solemnity"}
    ]
  }
}

def main():
    existing = load_echo('1timothy')
    merge_echo(existing, ECHOES_1TIM)
    save_echo('1timothy', existing)

    il = json.loads((ROOT / 'data' / 'interlinear' / '1timothy.json').read_text())
    present_chs = sorted(existing.keys(), key=int)
    print(f'  Chapters with echo entries: {present_chs}')
    for ch in ['1', '2', '3', '4', '5']:
        count = len(existing.get(ch, {}))
        print(f'  ch{ch}: {count} verses with entries')

if __name__ == '__main__':
    main()
