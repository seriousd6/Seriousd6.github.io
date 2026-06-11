"""
Echo layer — Numbers 27–29
Run: python3 scripts/zc-echo-numbers-27-29.py

Key echo threads:
  Ch 27: Daughters of Zelophehad (inheritance rights); Moses's death announced; Joshua commissioned
         — "sheep without a shepherd" (Num 27:17) echoed verbatim in Matt 9:36; Joshua as Jesus-type
  Ch 28: Daily, sabbath, new-moon, Passover, and Feast of Weeks offerings
         — tamid → Heb 10:11; new moon/sabbath → Col 2:16-17; Passover → 1 Cor 5:7
  Ch 29: 7th-month festivals: Trumpets, Yom Kippur, Sukkot (8 days, decreasing bulls)
         — Trumpets → 1 Thess 4:16; Yom Kippur → Heb 9:7; Tabernacles → John 7:37-38
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

NUMBERS_ECHOES = {
  "27": {
    "1": [
      {"type": "theme", "target": "Gal 3:28", "note": "The daughters of Zelophehad's inheritance appeal establishes the legal principle that women can inherit — an anomaly in ancient inheritance law. Paul's declaration that in Christ there is 'neither male nor female' for purposes of inheritance in the covenant family (Gal 3:28) reflects the trajectory begun at Num 27, where gender does not disqualify from the father's name and portion."}
    ],
    "4": [
      {"type": "theme", "target": "Isa 56:5", "note": "The daughters' concern — 'why should our father's name disappear from his clan?' — is the OT's deepest anxiety: being cut off from the covenant community without an heir. YHWH resolves this anxiety ultimately in Christ: 'I will give them an everlasting name that shall not be cut off' (Isa 56:5), and in Christ, adoption as children of God guarantees a share in the Father's inheritance regardless of natural descent (Rom 8:17)."}
    ],
    "12": [
      {"type": "type", "target": "Heb 11:13", "note": "Moses ascends the mountain to view the Promised Land before dying — seeing the promise from a distance but not entering it. Hebrews 11:13 presents this as the pattern of all OT faith: 'These all died in faith, not having received the things promised, but having seen them and greeted them from afar.' Moses on Nebo is the paradigmatic example of dying in hope without arrival — a hope that Christ ultimately fulfills for all such pilgrims."}
    ],
    "17": [
      {"type": "allusion", "target": "Matt 9:36", "note": "Moses prays for 'a man over the congregation, who shall go out before them and come in before them... that the congregation of the LORD may not be as sheep that have no shepherd' — the precise phrase Jesus uses in Matt 9:36: 'When he saw the crowds, he had compassion for them, because they were harassed and helpless, like sheep without a shepherd.' The Mosaic prayer for a shepherd-leader is answered in Jesus, who names himself 'the good shepherd' (John 10:11)."},
      {"type": "allusion", "target": "Ezek 34:23", "note": "The image of Israel as sheep needing a shepherd (Num 27:17) runs through the prophets to Ezekiel's promise: 'I will set up over them one shepherd, my servant David, and he shall feed them.' Christ as the Davidic shepherd-king is the ultimate answer to Moses's prayer for a leader who will shepherd YHWH's flock."}
    ],
    "18": [
      {"type": "type", "target": "Heb 4:8", "note": "Joshua (<em>Yehoshua</em>, 'YHWH saves') is chosen as Moses's successor, a man 'in whom is the Spirit.' The Greek equivalent of Joshua is Iēsous — Jesus. Heb 4:8 makes the typological link explicit: 'For if Joshua had given them rest, God would not have spoken of another day later on.' Joshua leads into the earthly Canaan; Jesus leads into the true rest. The Spirit-endowed Joshua is the named type of the Spirit-anointed Christ."}
    ],
    "20": [
      {"type": "allusion", "target": "Matt 28:18", "note": "Moses transfers some of his authority (<em>hod</em>, splendor/majesty) to Joshua so the congregation will obey. The transfer of leadership authority from Moses to Joshua prefigures the granting of all authority to Jesus: 'All authority in heaven and on earth has been given to me' (Matt 28:18). The Mosaic transfer was partial; Christ receives it in full."},
      {"type": "type", "target": "Heb 3:3", "note": "Moses commissions Joshua as his successor, but Hebrews argues that Jesus is not merely Moses's latest successor — he is of a different order entirely: 'Jesus has been counted worthy of more glory than Moses, as much more as the builder of a house has more honor than the house itself' (Heb 3:3). The Moses–Joshua succession is the type; the Moses–Christ contrast is the antitype."}
    ],
    "23": [
      {"type": "allusion", "target": "1 Tim 4:14", "note": "Moses lays his hands on Joshua before the congregation, transferring the commission and publicly acknowledging YHWH's designation. The laying-on-of-hands ceremony for ministry appointments continues in the NT: 'Do not neglect the gift you have, which was given you by prophecy when the council of elders laid their hands on you' (1 Tim 4:14). The Mosaic ordination gesture becomes the church's ongoing practice for setting apart ministers."}
    ]
  },
  "28": {
    "3": [
      {"type": "type", "target": "Heb 10:11", "note": "The <em>tamid</em> (daily burnt offering) — two lambs every day, morning and evening — is the perpetual sacrifice that defines the daily rhythm of Israel's worship. Heb 10:11 uses the daily offering as the foil for Christ's once-for-all sacrifice: 'Every priest stands daily at his service, offering repeatedly the same sacrifices, which can never take away sins.' The tamid's repetition is the built-in evidence of its inadequacy, pointing to the one sacrifice that does not need repeating."}
    ],
    "11": [
      {"type": "shadow", "target": "Col 2:16", "note": "The monthly new-moon offering is one of the three Levitical calendar-markers (sabbath, new moon, festivals) that Paul lists in Col 2:16-17: 'Let no one pass judgment on you in questions of food and drink, or with regard to a festival or a new moon or a Sabbath. These are a shadow of the things to come, but the substance belongs to Christ.' The new-moon sacrifice, along with the sabbath and the annual festivals, constitutes the Jewish sacred-time structure that Christ fulfills and thereby relativizes."}
    ],
    "16": [
      {"type": "fulfillment", "target": "1 Cor 5:7", "note": "The Passover sacrifice requirements of Num 28:16-25 (14th of Nisan, unleavened bread for seven days) form the festival backdrop for Christ's crucifixion. Paul quotes the Passover tradition directly: 'For Christ, our Passover lamb, has been sacrificed' (1 Cor 5:7). The timing was not accidental — Jesus died at Passover as the fulfillment of the Passover type established in Exod 12 and perpetuated in Num 28."}
    ],
    "26": [
      {"type": "fulfillment", "target": "Acts 2:1", "note": "The Feast of Weeks (Shavuot/Pentecost), the firstfruits offering fifty days after Passover, is the festival backdrop of Acts 2. The Spirit is poured out 'when the day of Pentecost arrived' (Acts 2:1) — on the very day of the Feast of Weeks. The firstfruits offering of Num 28:26 is fulfilled by the Spirit as the firstfruits of the new covenant age: 'we ourselves, who have the firstfruits of the Spirit, groan inwardly' (Rom 8:23)."},
      {"type": "type", "target": "1 Cor 15:20", "note": "The Feast of Weeks is the firstfruits harvest offering — the first portion of the grain harvest consecrated to YHWH. Paul applies the firstfruits typology to the resurrection: 'Christ has been raised from the dead, the firstfruits of those who have fallen asleep' (1 Cor 15:20). The Pentecost offering of firstfruits is the type of the risen Christ as the first of the resurrection harvest."}
    ]
  },
  "29": {
    "1": [
      {"type": "shadow", "target": "1 Thess 4:16", "note": "The Day of Trumpets (1st of Tishri) is a day of trumpet-blowing (<em>yom teruah</em>) and holy assembly — a festival announced by the ram's horn blast. The eschatological trumpet motif runs from the OT feast through the NT: 'For the Lord himself will descend from heaven with a cry of command, with the voice of an archangel, and with the sound of the trumpet of God' (1 Thess 4:16). The annual trumpet-blast of Num 29:1 is the type of the final trumpet that announces the resurrection and the return of Christ."},
      {"type": "shadow", "target": "1 Cor 15:52", "note": "The Day of Trumpets signals the opening of the seventh month — the month of YHWH's great festivals. Paul's 'last trumpet' at the resurrection (1 Cor 15:52) activates this festival-trumpet association: the sound that once announced the sacred month now announces the sacred age, the resurrection of the dead and the transformation of the living."}
    ],
    "7": [
      {"type": "type", "target": "Heb 9:7", "note": "The 10th of Tishri is Yom Kippur (Day of Atonement), when the high priest enters the holy of holies with the blood of the sin offerings (Lev 16). The Num 29 festival calendar assigns specific sin offerings for this day. Hebrews uses Yom Kippur as the primary OT type for Christ's high-priestly work: 'Into the second tent only the high priest goes, and only once a year, and not without blood... but when Christ appeared as a high priest... he entered once for all into the holy places, not by means of the blood of goats and calves but by means of his own blood, thus securing an eternal redemption' (Heb 9:7, 11-12)."}
    ],
    "12": [
      {"type": "type", "target": "John 7:2", "note": "The 15th of Tishri begins the Feast of Tabernacles (Sukkot), seven days of booths plus a closing assembly, the most joyful festival in the Jewish calendar. John's Gospel sets Jesus's climactic water-proclamation at this feast (John 7:2, 37-38): on the last day of the feast, the great day, Jesus stood up and cried out, &ldquo;If anyone thirsts, let him come to me and drink&rdquo; (John 7:37). The water-libation ceremony of Sukkot — daily pouring of water at the altar — is the ritual context Jesus interrupts with his claim to give living water."},
      {"type": "theme", "target": "Zech 14:16", "note": "The Feast of Tabernacles is the only festival Zechariah prophesies will be celebrated by all nations in the eschatological age: 'Then everyone who survives of all the nations that have come against Jerusalem shall go up year after year to worship the King, the LORD of hosts, and to keep the Feast of Booths' (Zech 14:16). The 8-day Sukkot of Num 29 points toward the universal eschatological celebration of YHWH's kingship through the nations gathered to Christ."}
    ],
    "35": [
      {"type": "shadow", "target": "Rev 21:3", "note": "The eighth day closing assembly (<em>Shemini Atzeret</em>) on the 22nd of Tishri concludes the festival calendar — the culminating holy assembly after the seven days of Tabernacles. The eighth day is the day beyond the sabbatical cycle, the day of new creation and eschatological rest. The Sukkot-tabernacles imagery finds its ultimate fulfillment in Revelation: 'Behold, the dwelling place of God is with man. He will dwell with them, and they will be his people' (Rev 21:3). The word <em>skēnōsei</em> (dwell/tabernacle) deliberately echoes Sukkot — God tabernacles permanently with his people in the new creation."}
    ],
    "39": [
      {"type": "theme", "target": "Heb 10:1", "note": "The totality of offerings in Num 28-29 — the 70 bulls of Sukkot alone, plus the rams, lambs, and sin offerings across all the festivals — constitutes an overwhelming quantity of sacrifice, yet Hebrews declares it was never sufficient: 'For since the law has but a shadow of the good things to come instead of the true form of these realities, it can never, by the same sacrifices that are continually offered every year, make perfect those who draw near' (Heb 10:1). The comprehensive festival-offering calendar of Num 28-29 is the quantitative shadow pointing to the one qualitatively sufficient sacrifice of Christ."}
    ],
    "40": [
      {"type": "allusion", "target": "Heb 3:5", "note": "Moses tells the Israelites everything YHWH commanded him — faithful transmission of all the ordinances. Heb 3:5 makes Moses's faithful service the foil for Christ's superior faithfulness: 'Moses was faithful in all God's house as a servant, to testify to the things that were to be spoken later, but Christ is faithful over God's house as a son.' Moses faithfully transmits the festival calendar; Christ is the one to whom the entire calendar testifies."}
    ]
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, NUMBERS_ECHOES)
    save_echo('numbers', e)
    print('numbers echo: ch 27-29 written')

if __name__ == '__main__':
    main()
