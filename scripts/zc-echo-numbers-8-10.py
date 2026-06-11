"""
Echo — Numbers chapters 8–10
Run: python3 scripts/zc-echo-numbers-8-10.py

Key echoes in this range:
- Num 8:1-4  → Rev 1:12-13,20; John 8:12 (menorah / Christ as light)
- Num 8:7    → Ezek 36:25; Heb 10:22 (purification sprinkling)
- Num 8:10   → Heb 7:26-27 (hand-laying / priestly substitution)
- Num 8:11   → Rom 12:1 (Levites wave-offered / living sacrifice)
- Num 8:19   → Heb 9:22-26 (Levitical atonement / Christ's once-for-all)
- Num 9:7    → Heb 9:14 (corpse-impurity / dead works)
- Num 9:11   → 2 Pet 3:9 (second Passover / divine patience)
- Num 9:12   → John 19:36 (no bone broken)
- Num 9:14   → Gal 3:28; Eph 2:13-18 (one law for all)
- Num 9:15-16 → 1 Cor 10:1-2 (cloud / Spirit at baptism)
- Num 9:17   → John 16:13; Acts 16:6-10 (cloud guidance / Spirit's leading)
- Num 9:23   → Heb 3:7-8 (hear his voice / obedience)
- Num 10:2   → Zech 9:14; Rev 8:2; 1 Thess 4:16 (trumpets)
- Num 10:9   → Rev 8:1-5 (remembered before YHWH / prayers before altar)
- Num 10:10  → Matt 24:31; 1 Cor 15:52 (trumpet call / resurrection)
- Num 10:11  → Heb 11:8-10 (departure by faith toward promised inheritance)
- Num 10:29  → Luke 14:23; Matt 11:28 (invitation to join YHWH's people)
- Num 10:35  → Ps 68:1; Rev 19:11-16 (arise O YHWH / Christ the warrior-king)
- Num 10:36  → Rev 5:11-12 (ten thousand thousands)
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
  "8": {
    "1": [
      {"type": "allusion", "target": "John 8:12", "note": "Aaron is commanded to set up the menorah so its seven lamps illuminate the space before it; Jesus declares 'I am the light of the world' — claiming the function that the menorah represented in the sanctuary."},
      {"type": "shadow",   "target": "Rev 1:12",  "note": "John sees seven golden lampstands with the risen Christ walking among them (Rev 1:12-13, 20); the churches are the menorah-community gathered around the one true light, continuing the tabernacle imagery."}
    ],
    "2": [
      {"type": "allusion", "target": "John 1:9",  "note": "The seven lamps shine toward the front of the lampstand — their light is directed outward, for the benefit of the space. John 1:9 describes the true light 'coming into the world' — light that does not keep its illumination to itself."}
    ],
    "4": [
      {"type": "allusion", "target": "Exod 25:31", "note": "The menorah was made exactly as YHWH showed Moses (Num 8:4 = Exod 25:31-40 enacted) — a rare compliance-confirmation note signaling the menorah's importance as a covenant sign."},
      {"type": "shadow",   "target": "Rev 21:23",  "note": "The perpetual lamp of the sanctuary points toward Rev 21:23 — the New Jerusalem has no need of sun or moon 'for the glory of God gives it light, and its lamp is the Lamb.'"}
    ],
    "7": [
      {"type": "allusion", "target": "Ezek 36:25", "note": "The purification sprinkling (water of purification, Num 8:7) prefigures Ezekiel's new-covenant promise: 'I will sprinkle clean water on you, and you shall be clean from all your uncleannesses.'"},
      {"type": "type",     "target": "Heb 10:22",  "note": "Hearts 'sprinkled clean from an evil conscience' (Heb 10:22) applies the Levitical sprinkling-for-consecration to the new covenant believer's access to God through Christ's blood."}
    ],
    "10": [
      {"type": "shadow",   "target": "Heb 7:26",   "note": "The Israelites lay hands on the Levites (Num 8:10), designating them as the community's priestly representatives. This anticipates the great high priest who is 'holy, innocent, unstained, separated from sinners' (Heb 7:26) and who represents all people before God."},
      {"type": "allusion", "target": "Lev 1:4",    "note": "The same hand-laying gesture used at animal sacrifice (Lev 1:4) is used here for the Levites — the tribe consecrated as a human wave-offering, standing in the structural position of the sacrifice they serve."}
    ],
    "11": [
      {"type": "type",     "target": "Rom 12:1",   "note": "Aaron presents the Levites as a 'wave offering' before YHWH (Num 8:11) — the entire tribe offered to God as a corporate living sacrifice. Paul's 'present your bodies as a living sacrifice, holy and acceptable to God' (Rom 12:1) applies this Levitical logic to all believers as the new priestly community."}
    ],
    "14": [
      {"type": "allusion", "target": "1 Pet 2:9",  "note": "The Levites are 'wholly given' to YHWH from among the Israelites (Num 8:14-16) — set apart from the community to represent it. 1 Peter 2:9 extends this priestly separation to all believers: 'a royal priesthood, a holy nation, a people for his own possession.'"}
    ],
    "16": [
      {"type": "type",     "target": "Exod 13:2",  "note": "The Levites are given to YHWH in place of every firstborn of Israel (Num 8:16-18), substituting for the firstborn claim established at the Exodus (Exod 13:2). The Levitical substitution-principle is a shadow of Christ's substitutionary atonement — one stands in for many."}
    ],
    "19": [
      {"type": "type",     "target": "Heb 9:22",   "note": "The Levites perform atonement for Israel 'that there may be no plague among the people when they come near the sanctuary' (Num 8:19). Hebrews 9:22-26 presents Christ's once-for-all offering as the fulfillment that Levitical atonement-mediation anticipated."},
      {"type": "allusion", "target": "Heb 7:27",   "note": "The Levites' ongoing atonement-function required constant repetition; Heb 7:27 contrasts this with Christ: 'he has no need, like those high priests, to offer sacrifices daily... he did this once for all when he offered up himself.'"}
    ],
    "25": [
      {"type": "theme",    "target": "1 Cor 12:4",  "note": "Levites serve from age 25-50, then assist but do not bear the heavy work (Num 8:25-26). The seasonal, graduated nature of service reflects the Pauline principle that different roles and capacities serve the body across different seasons (1 Cor 12:4-7)."}
    ]
  },
  "9": {
    "2": [
      {"type": "type",     "target": "1 Cor 5:7",  "note": "YHWH commands the second-year Passover (Num 9:2-3) — re-enacting the foundational deliverance event. Paul identifies Christ as 'our Passover lamb' who has been sacrificed (1 Cor 5:7), making every Lord's Supper a Passover-echo."}
    ],
    "7": [
      {"type": "shadow",   "target": "Heb 9:14",   "note": "Those impure from contact with a corpse cannot observe the Passover (Num 9:6-7); corpse-impurity disqualifies from the covenant meal. Heb 9:14 applies this logic to the new covenant: Christ's blood 'purifies our conscience from dead works to serve the living God.'"}
    ],
    "11": [
      {"type": "allusion", "target": "2 Pet 3:9",  "note": "The second Passover provision (Num 9:11) — a gracious second opportunity for those who could not observe on the appointed day — reflects divine patience that the NT develops in 2 Pet 3:9: 'The Lord is not slow to fulfill his promise... not wishing that any should perish, but that all should reach repentance.'"}
    ],
    "12": [
      {"type": "fulfillment", "target": "John 19:36", "note": "The Passover lamb's bones shall not be broken (Num 9:12; cf. Exod 12:46). John 19:36 applies this explicitly to Jesus: 'these things took place that the Scripture might be fulfilled: Not one of his bones will be broken.'"}
    ],
    "14": [
      {"type": "allusion", "target": "Gal 3:28",   "note": "One law for both the sojourner and the native-born who wishes to keep the Passover (Num 9:14). Galatians 3:28 extends the same principle to the new covenant community: 'There is neither Jew nor Greek... for you are all one in Christ Jesus.'"},
      {"type": "allusion", "target": "Eph 2:13",   "note": "The sojourner who wishes to join Israel in the Passover is welcomed under the same law as the native (Num 9:14). Eph 2:13 describes Gentiles 'who once were far off' now 'brought near by the blood of Christ' — the Passover's inclusive welcome extended to all nations."}
    ],
    "15": [
      {"type": "type",     "target": "1 Cor 10:1", "note": "The cloud covers the tabernacle the day it is erected (Num 9:15) — YHWH's presence accompanying the covenant community from the start. Paul identifies the cloud at the Exodus as a type of baptism: 'all were baptized into Moses in the cloud' (1 Cor 10:1-2), pointing to Christ."}
    ],
    "16": [
      {"type": "allusion", "target": "Exod 13:21", "note": "Cloud by day and fire by night (Num 9:16) echoes the original Exodus guidance (Exod 13:21-22). Numbers establishes the cloud-fire as a permanent feature of YHWH's guidance, not a one-time miracle at the Exodus."},
      {"type": "shadow",   "target": "Rev 21:23",  "note": "The fire-cloud that never departs from the tabernacle points toward the eschatological presence where YHWH's glory is the permanent light of the New Jerusalem — no more alternating cloud-by-day/fire-by-night, but continuous divine radiance."}
    ],
    "17": [
      {"type": "type",     "target": "John 16:13", "note": "Whenever the cloud lifted, Israel moved; whenever it settled, Israel camped (Num 9:17-23). The cloud directed Israel's movement through the wilderness. Jesus promises the Spirit of truth will 'guide you into all truth' (John 16:13) — the Spirit is the new-covenant cloud-guide."},
      {"type": "allusion", "target": "Acts 16:6",  "note": "Paul and Silas are 'forbidden by the Holy Spirit' to speak in Asia, and the 'Spirit of Jesus' does not allow them into Bithynia (Acts 16:6-7) — the pattern of Spirit-directed movement, halting or proceeding, directly mirrors Israel's cloud-directed wilderness travel."}
    ],
    "20": [
      {"type": "theme",    "target": "Heb 3:7",    "note": "Whether two days or a month or longer, Israel stayed as YHWH commanded (Num 9:20-22) — obedient movement and rest according to divine timing, not personal preference. Heb 3:7-8 applies this wilderness-obedience model: 'Today, if you hear his voice, do not harden your hearts.'"}
    ],
    "23": [
      {"type": "allusion", "target": "Heb 3:7",    "note": "Israel kept YHWH's charge 'at the command of YHWH through Moses' (Num 9:23). The Hebrews warning (3:7-11) holds up the wilderness generation as the counter-example of those who heard God's voice through Moses but hardened their hearts — the obedience of Num 9:23 is precisely what Hebrews calls the church to maintain."}
    ]
  },
  "10": {
    "2": [
      {"type": "shadow",   "target": "Zech 9:14",  "note": "Two silver trumpets are made to summon the assembly and signal departure (Num 10:2). Zechariah 9:14 picks up this imagery: 'YHWH God will blow the trumpet and will march forth in the whirlwinds of the south' — the trumpet as the sound of divine gathering and advance."},
      {"type": "shadow",   "target": "Rev 8:2",    "note": "The seven trumpets of Revelation 8-11 draw on the trumpet-series of Numbers 10 — signals of divine action, calling to assembly, marking transitions in YHWH's sovereign purposes. The tabernacle trumpets are the liturgical seedbed for the eschatological trumpet series."}
    ],
    "9": [
      {"type": "allusion", "target": "Rev 8:4",    "note": "When Israel sounds the alarm at war 'that you may be remembered before YHWH your God' (Num 10:9), the trumpets bring the people into YHWH's presence for aid. Rev 8:4 shows the incense of the saints' prayers ascending before God — the same logic of being 'brought to remembrance' before the divine throne."}
    ],
    "10": [
      {"type": "type",     "target": "1 Thess 4:16", "note": "Trumpets blown at feasts and new moons serve as 'a memorial before your God' and call the community to assemble (Num 10:10). 1 Thess 4:16 describes Christ's return announced by 'the trumpet of God' — the eschatological assembly-call that summons the dead and living before God."},
      {"type": "type",     "target": "Matt 24:31", "note": "Num 10:10 establishes the trumpet as the signal for the sacred gathering of YHWH's people. Matt 24:31: 'He will send out his angels with a loud trumpet call, and they will gather his elect from the four winds' — the final gathering-trumpet."},
      {"type": "shadow",   "target": "1 Cor 15:52", "note": "The Num 10:10 trumpet signals feast-day and new-moon transitions — YHWH's calendar-markers. 1 Cor 15:52: 'the trumpet will sound, and the dead will be raised imperishable' — the ultimate calendar-marker, the trumpet announcing the transition from mortal to immortal."}
    ],
    "11": [
      {"type": "allusion", "target": "Heb 11:8",   "note": "Israel departs from Sinai by faith, following the cloud into unknown territory, trusting the divine promise (Num 10:11-13). Heb 11:8 presents Abraham as the archetype: 'he went out, not knowing where he was going' — and the wilderness departure shares this pattern of faith-in-motion toward an unseen inheritance."}
    ],
    "17": [
      {"type": "allusion", "target": "Rev 7:4",    "note": "The ordered tribal march in Num 10:11-28 assigns each tribe its position in the procession. Rev 7:4-8 returns to the twelve-tribe enumeration in the eschatological sealing — the ordered people of God marching toward the promised end."}
    ],
    "29": [
      {"type": "allusion", "target": "Luke 14:23", "note": "Moses invites Hobab to join Israel: 'Come with us, and we will do you good, for YHWH has promised good to Israel' (Num 10:29). Luke 14:23: 'compel people to come in, that my house may be filled' — the gospel invitation echoes the structure of Moses's personal summons to join YHWH's people on the march."}
    ],
    "33": [
      {"type": "type",     "target": "Heb 4:8",    "note": "The ark goes three days' journey before Israel to seek out a resting place (Num 10:33) — the ark leading toward rest. Heb 4:8-9: 'if Joshua had given them rest, God would not have spoken of another day later on. So then, there remains a Sabbath rest for the people of God' — the ark-led march toward Canaan rest points to the greater rest Christ provides."}
    ],
    "35": [
      {"type": "allusion", "target": "Ps 68:1",    "note": "Moses's prayer 'Arise, O YHWH, and let your enemies be scattered; let those who hate you flee before you' (Num 10:35) is quoted verbatim in Ps 68:1, which then develops this victory march into a full liturgical procession ascending to YHWH's throne."},
      {"type": "shadow",   "target": "Rev 19:11",  "note": "The divine warrior who rises to scatter enemies (Num 10:35) is fulfilled in Rev 19:11-16: 'I saw heaven opened, and behold, a white horse! The one sitting on it is called Faithful and True, and in righteousness he judges and makes war' — Christ as the YHWH who rises to scatter all his enemies."}
    ],
    "36": [
      {"type": "allusion", "target": "Rev 5:11",   "note": "Moses's return prayer 'Return, O YHWH, to the ten thousand thousands of Israel' (Num 10:36) anticipates Rev 5:11: 'the number of them was myriads of myriads and thousands of thousands' around the throne of the Lamb — the innumerable host gathered around the one who has returned to his people."}
    ]
  }
}

def main():
    existing = load_echo('numbers')
    merge_echo(existing, NUMBERS_ECHOES)
    save_echo('numbers', existing)
    for ch in ['8', '9', '10']:
        count = len(existing.get(ch, {}))
        print(f'ch {ch}: {count} verses with echo entries')
    print('Numbers 8-10 echoes written.')

if __name__ == '__main__':
    main()
