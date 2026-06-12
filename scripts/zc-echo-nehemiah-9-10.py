"""
MKT Echo Layer — Nehemiah chapters 9–10
Run: python3 scripts/zc-echo-nehemiah-9-10.py

Ch9: Levitical creation-confession — 'You alone are the LORD' (9:6) — Rev 4:11; Col 1:16
     God gracious/compassionate/slow-to-anger in the wilderness (9:17) — Luke 15:20; 2 Pet 3:9
     Good Spirit given to instruct them (9:20) — John 16:13; Eph 1:17
     Cry-and-deliver cycle repeated (9:27-28) — Rom 11:26; Heb 12:5-6
     God's great mercies — punishment less than deserved (9:31) — Rom 3:24-26
Ch10: Covenant commitment sealed — walk in God's law (10:29) — Heb 8:10; 2 Cor 3:3
      Sabbath commerce prohibition (10:31) — Col 2:17; Heb 4:9-10
      Firstfruits obligation (10:35-36) — Rom 8:23; 1 Cor 15:20
      House of God — we will not neglect it (10:39) — Heb 10:25; 1 Pet 2:5
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

ECHOES = {
  "9": {
    "6": [
      {"type": "allusion", "target": "Rev 4:11", "note": "The Levitical prayer begins with a creation-confession: 'You alone are the LORD. You made the heavens, even the highest heavens, and all their starry host, the earth and all that is on it, the seas and all that is in them.' This comprehensive monotheistic doxology — the solus Dominus formula — echoes forward to the four living creatures in Revelation 4:11: 'You are worthy, our Lord and God, to receive glory and honor and power, for you created all things, and by your will they were created and have their being.' Both passages ground worship in creation-sovereignty. The NT ascription of the same creative authority to Christ (Col 1:16: 'all things have been created through him and for him') makes the Nehemiah confession Christologically charged: the one praised for creating all things is the one through whom all things were made."},
      {"type": "allusion", "target": "Col 1:16", "note": "'You alone are the LORD. You made the heavens... the earth and all that is on it, the seas and all that is in them' — the comprehensive Creator praise of Neh 9:6. Colossians 1:16 attributes this same creative scope to Christ: 'by him all things were created: things in heaven and on earth, visible and invisible... all things have been created through him and for him.' The Levites' praise of YHWH as the one who made everything in Neh 9:6 is the OT ground-note that Paul transposes into Christological key. The NT revelation is not that a different Creator is now praised, but that the one the Levites praised as LORD is the one who became incarnate."}
    ],
    "17": [
      {"type": "allusion", "target": "Luke 15:20", "note": "In the wilderness-apostasy section, the prayer recalls: 'But you are a God ready to forgive, gracious and merciful, slow to anger and abounding in steadfast love' — the Exodus attribute-list (Exod 34:6-7) applied to YHWH's response to the golden-calf generation. Luke 15:20: 'while he was still a long way off, his father saw him and was filled with compassion for him; he ran to his son, threw his arms around him and kissed him.' Jesus's father in the parable embodies precisely this self-portrait of YHWH from Exod 34/Neh 9: the one who runs toward the returning prodigal rather than waiting with arm folded is the compassionate, patient, steadfast-love God the Levites confess. The parable is an enacted Neh 9:17."},
      {"type": "allusion", "target": "2 Pet 3:9", "note": "The confession that YHWH is 'slow to anger' in the face of Israel's repeated wilderness apostasy — the same generation that had seen the Exodus miracles — grounds the NT patience-theology. 2 Peter 3:9: 'The Lord is not slow in keeping his promise, as some understand slowness. Instead he is patient with you, not wanting anyone to perish, but everyone to come to repentance.' Peter's defense of divine delay grounds it in the same covenantal attribute the Levites confess: YHWH's patience is not failure to act but faithfulness to his own character — the character that refrained from destroying the wilderness generation and extended grace to the returnees in Nehemiah."}
    ],
    "20": [
      {"type": "allusion", "target": "John 16:13", "note": "The prayer recalls YHWH's provision in the wilderness: 'You gave your good Spirit to instruct them' — the Spirit as divine teacher accompanying Israel through the forty years. John 16:13: 'But when he, the Spirit of truth, comes, he will guide you into all the truth. He will not speak on his own; he will speak only what he hears, and he will tell you what is yet to come.' The Spirit's teaching function in the new covenant era (John 16) is the fulfillment of what the Levites recall as an OT provision: YHWH's good Spirit was teacher in the wilderness; the same Spirit — now poured out in fullness — teaches the whole church. Nehemiah 9:20 is the OT statement of the principle the upper-room discourse fulfills."},
      {"type": "allusion", "target": "Eph 1:17", "note": "The 'good Spirit' given to instruct Israel in the wilderness — YHWH's inner-transforming, directional provision alongside the external manna and water. Ephesians 1:17: 'I keep asking that the God of our Lord Jesus Christ, the glorious Father, may give you the Spirit of wisdom and revelation, so that you may know him better.' Paul's prayer for the Spirit as wisdom-giver is the NT form of the Levites' confession that YHWH gave his good Spirit to teach. The continuity of divine pedagogy — Spirit as teacher from wilderness to new covenant — runs through both texts."}
    ],
    "27": [
      {"type": "allusion", "target": "Rom 11:26", "note": "The cry-and-deliver cycle at the center of the prayer: 'And when they cried to you, you heard from heaven, and according to your great mercies you gave them saviors who saved them from the hand of their enemies' — the recurring pattern of apostasy, oppression, cry, and deliverance in the Judges period. Romans 11:26: 'And in this way all Israel will be saved.' Paul's eschatological vision of Israel's final deliverance follows the same structural logic as the Nehemiah prayer: a history of apostasy, discipline, and crying out — and YHWH's final saving response. The Judges cycle embedded in Neh 9:26-28 is the historical pattern the NT reads as prefiguring the ultimate deliverance through Christ."},
      {"type": "allusion", "target": "Heb 12:5", "note": "The prayer traces the repeated cycle of YHWH's discipline and rescue: 'Many times you delivered them, but they returned to do evil before you. Again you abandoned them to the hand of their enemies... But when they turned and cried to you, you heard from heaven.' Hebrews 12:5-6 cites Proverbs 3:11-12: 'My son, do not make light of the Lord's discipline, and do not lose heart when he rebukes you, because the Lord disciplines the one he loves.' The discipline-and-restoration cycle the Levites trace through Israel's history is the theological basis of Hebrews' argument: the God who disciplines is the God who loves — the pattern repeated across generations in Neh 9 is pedagogical, not punitive."}
    ],
    "31": [
      {"type": "allusion", "target": "Rom 3:24", "note": "'Nevertheless, in your great mercies you did not make an end of them or forsake them, for you are a gracious and merciful God.' The explicit acknowledgment that YHWH's actual response was mitigated relative to what the covenant violations deserved — the pattern of under-punishment that the OT recognizes but cannot fully account for without the cross. Romans 3:24-26: God 'passed over former sins in his divine forbearance' — a forbearance that looked forward to Christ's sacrifice. Nehemiah 9:31 is one of the OT's clearest recognitions of this pattern: the great mercies that preserved Israel through centuries of apostasy were advances on the cross, not suspensions of justice."}
    ]
  },
  "10": {
    "29": [
      {"type": "allusion", "target": "Heb 8:10", "note": "The covenant-signing assembly: 'all these join their brothers the nobles, and enter into a curse and an oath to walk in God's law that was given by Moses... and to observe and do all the commandments of the LORD our Lord.' The sealed covenant commitment to internal law-keeping echoes forward to the new covenant promise of Hebrews 8:10 (citing Jer 31:33): 'I will put my laws in their minds and write them on their hearts. I will be their God, and they will be my people.' The Nehemiah covenant is sealed externally — written on parchment, signed with names; the new covenant is written internally. The Nehemiah covenant is the OT's fullest post-exilic expression of covenant desire; its limitation (written on paper, requiring the people's own effort) points toward the new covenant's solution."},
      {"type": "allusion", "target": "2 Cor 3:3", "note": "The covenant document sealed by the community — 'the people entered into a curse and an oath to walk in God's law' — is the OT form of the commitment to divine instruction. 2 Corinthians 3:3: 'You show that you are a letter from Christ, the result of our ministry, written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts.' Paul's contrast between the old covenant inscription (stone tablets, scrolls) and the new (Spirit-written hearts) is directly relevant to Neh 10: the sealed scroll of Neh 10 is the external form; the Spirit's writing in 2 Cor 3 is its new covenant fulfillment."}
    ],
    "31": [
      {"type": "allusion", "target": "Col 2:17", "note": "The covenant pledge includes Sabbath-commerce abstention: 'if the peoples of the land bring in goods or any grain on the Sabbath day to sell, we will not buy from them on the Sabbath or on a holy day.' The Sabbath-boundary as covenant identity marker is what Paul addresses in Colossians 2:16-17: 'do not let anyone judge you by what you eat or drink, or with regard to a religious festival, a New Moon celebration or a Sabbath day. These are a shadow of the things that were to come; the reality, however, is found in Christ.' The Sabbath pledge of Neh 10:31 is the OT expression of the reality whose shadow it casts — the rest that Christ himself embodies (Matt 11:28) and that remains for the people of God (Heb 4:9)."},
      {"type": "allusion", "target": "Heb 4:9", "note": "The Sabbath-commerce pledge of Neh 10:31 — the community binding itself to honor the seventh-day boundary — points to the eschatological Sabbath of Hebrews 4:9: 'There remains, then, a Sabbath-rest for the people of God.' Nehemiah's community attempted to recover the Sabbath through covenant commitment and legal enforcement (Neh 13:15-22). The Hebrews author reveals that the true Sabbath is not secured by community pledge but entered by faith in Christ — 'anyone who enters God's rest also rests from their works, just as God did from his' (4:10). The Nehemiah Sabbath covenant is the earnest attempt to enter what only Christ fully opens."}
    ],
    "35": [
      {"type": "allusion", "target": "Rom 8:23", "note": "The covenant obligation to bring firstfruits of the ground and firstborn of sons and animals to the house of God (Neh 10:35-36) — the dedication of the beginning of every harvest and every family to YHWH as acknowledgment of his prior ownership. Romans 8:23: 'Not only so, but we ourselves, who have the firstfruits of the Spirit, groan inwardly as we wait eagerly for our adoption to sonship, the redemption of our bodies.' Paul's 'firstfruits of the Spirit' takes the firstfruits vocabulary of the covenant obligation and redefines it: believers already possess the Spirit as the firstfruits of the final harvest — the beginning installment of the new-creation abundance the whole creation awaits. The Nehemiah firstfruits pledge is the OT form; the Spirit-as-firstfruits is the NT reality it adumbrated."},
      {"type": "allusion", "target": "1 Cor 15:20", "note": "The firstborn-of-sons and firstfruits-of-ground dedication in Neh 10:35-36 — the covenant obligation to consecrate the first and best to YHWH — finds its ultimate NT fulfillment in 1 Corinthians 15:20: 'But Christ has indeed been raised from the dead, the firstfruits of those who have fallen asleep.' The OT firstfruits principle (the first portion consecrated to YHWH, guaranteeing and representing the whole harvest) is fulfilled in Christ: his resurrection is the firstfruits consecrated to the Father, guaranteeing the full harvest of resurrected believers. The Nehemiah firstfruits covenant is the liturgical practice whose ultimate referent is Christ's resurrection."}
    ],
    "39": [
      {"type": "allusion", "target": "Heb 10:25", "note": "The covenant pledge concludes: 'We will not neglect the house of our God' — the communal commitment to maintain the temple system, its Levites, its tithes, its sacrifices. Hebrews 10:25: 'not giving up meeting together, as some are in the habit of doing, but encouraging one another — and all the more as you see the Day approaching.' The Nehemiah pledge to not neglect the house of God is the OT form of the same covenant imperative the author of Hebrews presses on the new covenant community. Both texts address communities tempted to let the corporate worship commitment slip; both ground the imperative in the covenant bond. The temple they pledged not to neglect has been replaced by the gathered assembly in which Christ is present (Matt 18:20)."},
      {"type": "allusion", "target": "1 Pet 2:5", "note": "The community's pledge to sustain the house of God — its priests, its Levites, its sacrificial system — is the OT covenant obligation whose NT form is 1 Peter 2:5: 'you also, like living stones, are being built into a spiritual house to be a holy priesthood, offering spiritual sacrifices acceptable to God through Jesus Christ.' Nehemiah's community pledged to maintain a physical house with a Levitical priesthood; Peter declares that the new covenant community IS the house, and all members are the priesthood. The Nehemiah pledge of Neh 10:39 is the OT covenant that the new covenant restructures from the ground up — stone-and-wood temple replaced by living-stone community."}
    ]
  }
}

def main():
    e = load_echo('nehemiah')
    merge_echo(e, ECHOES)
    save_echo('nehemiah', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'nehemiah echo: wrote entries for {count} verses across ch 9-10')

if __name__ == '__main__':
    main()
