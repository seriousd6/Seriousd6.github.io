#!/usr/bin/env python3
"""
MKT Echo Layer — Zechariah chapter 14 (entirely missing)
Run: python3 scripts/zc-echo-zechariah-14-14-full.py

Echo type: OT → NT direction.

Key connections:
- 14:4 feet on Mount of Olives, mountain splits → Acts 1:11-12 (return from/to Olives)
- 14:5 YHWH comes with all his holy ones → 1 Thess 3:13; 2 Thess 1:7 (parousia with saints)
- 14:7 unique day, no day/night → Rev 22:5 (no night in new Jerusalem)
- 14:8 living waters from Jerusalem → John 7:37-38; Rev 22:1-2 (rivers of living water)
- 14:9 YHWH king over all the earth, one name → Rev 11:15 (kingdom of world becomes Lord's)
- 14:16 surviving nations go up to worship → Rev 15:4; Rev 21:24 (nations walk in the light)
- 14:20-21 everything holy to YHWH → Rev 5:13; Heb 12:14 (universal holiness)
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

ZECHARIAH_ECHOES = {
    "14": {
        "4": [
            {
                "type": "allusion",
                "target": "Acts 1:11-12",
                "note": "Zechariah 14:4 declares that 'his feet will stand on the Mount of Olives' when YHWH comes to fight for Jerusalem. Acts 1:11-12 records the angelic announcement at the Ascension — 'This Jesus, who was taken up from you into heaven, will come in the same way as you saw him go into heaven' — immediately followed by the note that the disciples 'returned to Jerusalem from the mount called Olivet.' The Ascension leaves from the Mount of Olives; the angelic promise points to a return to the same place. Luke does not cite Zechariah explicitly, but the geography is exact: the mountain that Zechariah identifies as the location of YHWH's eschatological feet-standing is the mountain from which Jesus ascended and to which he will return."
            }
        ],
        "5": [
            {
                "type": "allusion",
                "target": "1 Thess 3:13",
                "note": "Zechariah 14:5 declares that 'YHWH my God will come, and all the holy ones with him' — the eschatological entourage of the divine warrior. Paul uses almost identical language in 1 Thessalonians 3:13: 'so that he may establish your hearts blameless in holiness before our God and Father, at the coming (parousia) of our Lord Jesus with all his holy ones.' The 'holy ones' (hagioi) who accompany Christ at the parousia are the same escort that Zechariah describes accompanying YHWH. The OT cosmic warfare scene — the divine warrior arriving with his heavenly army — is reframed in Paul as the parousia of Christ with his saints."
            },
            {
                "type": "allusion",
                "target": "2 Thess 1:7",
                "note": "2 Thessalonians 1:7 describes 'the revelation of the Lord Jesus from heaven with his mighty angels in flaming fire.' The structure is identical to Zechariah 14:5: the coming one arrives with a heavenly entourage, as a warrior bringing judgment against those who persecute God's people. Zechariah's 'all the holy ones with him' is the OT template for the NT's consistent picture of the parousia as a military arrival with an escorting host. Both texts serve the same rhetorical function: assuring persecuted communities that the divine warrior is coming with irresistible force."
            }
        ],
        "7": [
            {
                "type": "allusion",
                "target": "Rev 22:5",
                "note": "Zechariah 14:7 describes the eschatological day as 'a unique day, known only to YHWH — with no distinction between day and night, for at evening time there will be light.' Revelation 22:5 describes the new Jerusalem in precisely these terms: 'And night will be no more. They will need no light of lamp or sun, for the Lord God will be their light.' The paradoxical day that transcends the day/night cycle — light at evening — is the OT form of the eschatological reality Revelation describes: the divine presence itself as the source of perpetual light, rendering the day/night alternation obsolete. Both texts use the abolition of darkness to signal the completeness of YHWH's presence."
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "John 7:37-38",
                "note": "Zechariah 14:8 — 'living waters (mayim chayyim) shall flow out from Jerusalem, half of them to the eastern sea and half to the western sea' — is one of the primary OT backgrounds for Jesus's cry at the Feast of Tabernacles: 'If anyone thirsts, let him come to me and drink. Whoever believes in me, as the Scripture has said, &#x201C;Out of his heart will flow rivers of living water&#x201D;' (John 7:37-38). The Feast of Tabernacles was accompanied by water-pouring ceremonies that evoked Zechariah's vision of living waters from Jerusalem. Jesus positions himself as the source of what Zechariah promised — the living water flows from him as the new Jerusalem, the new temple."
            },
            {
                "type": "allusion",
                "target": "Rev 22:1-2",
                "note": "Revelation 22:1-2 describes 'the river of the water of life, bright as crystal, flowing from the throne of God and of the Lamb through the middle of the street of the city.' This is the direct fulfillment of Zechariah 14:8 — the living waters flowing from Jerusalem (now identified as the new Jerusalem, the city of God). The east/west direction of Zechariah's waters becomes the river through the middle of the new city in Revelation. Ezekiel 47 provides an intermediate form of the same vision. All three texts — Zechariah, Ezekiel, Revelation — describe the same eschatological reality: the life-giving water that flows from the presence of God restoring and sustaining the new creation."
            }
        ],
        "9": [
            {
                "type": "allusion",
                "target": "Rev 11:15",
                "note": "Zechariah 14:9 — 'YHWH will be king over all the earth. On that day YHWH will be one and his name one' — is the OT's compressed statement of eschatological monotheism: the universal, undivided sovereignty of YHWH. Revelation 11:15 enacts this in the seventh trumpet: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever.' Zechariah's 'YHWH will be king over all the earth' is what Revelation 11:15 declares accomplished — but now the king who reigns is identified as both the Lord and his Christ. The one name of Zechariah becomes the one name above every name (Phil 2:9-11)."
            }
        ],
        "16": [
            {
                "type": "allusion",
                "target": "Rev 15:4",
                "note": "Zechariah 14:16 — 'then everyone who survives of all the nations that have come against Jerusalem shall go up year after year to worship the King, YHWH of Hosts, and to keep the Feast of Tabernacles' — is the OT vision of Gentile nations streaming to worship in Jerusalem. Revelation 15:4 fulfills it in the song of Moses and the Lamb: 'Who will not fear, O Lord, and glorify your name? For you alone are holy. All nations will come and worship you, for your righteous acts have been revealed.' The annual pilgrimage of the nations to Jerusalem in Zechariah becomes the eternal worship of the nations before the throne in Revelation. The Feast of Tabernacles — the festival of ingathering — is fulfilled when the Gentile nations are gathered before the Lamb."
            },
            {
                "type": "allusion",
                "target": "Rev 21:24",
                "note": "Revelation 21:24 describes the new Jerusalem: 'By its light will the nations walk, and the kings of the earth will bring their glory into it.' This is the new covenant fulfillment of Zechariah 14:16's vision of the nations coming to worship in Jerusalem. In Zechariah, the nations must travel to Jerusalem each year for the feast; in Revelation, the nations walk permanently in the light of the city, bringing their glory in without seasonal constraint. The eschatological pilgrimage that Zechariah envisions as an annual obligation becomes in Revelation the eternal condition of the new creation."
            }
        ],
        "20": [
            {
                "type": "allusion",
                "target": "Heb 12:14",
                "note": "Zechariah 14:20-21 declares that 'on that day the inscription Holy to YHWH (Qodesh la-YHWH) shall be on the bells of the horses' — the phrase previously reserved for the high priest's golden plate (Exod 28:36) now inscribed on the most common military equipment. Every pot in Jerusalem will be holy like the temple bowls; the distinction between sacred and profane will be abolished. Hebrews 12:14 carries this into the NT exhortation: 'Strive for peace with everyone, and for the holiness without which no one will see the Lord.' The universal holiness Zechariah promises — everything Qodesh la-YHWH — is what Hebrews summons the community toward as the eschatological goal that shapes present ethics."
            }
        ]
    }
}

def main():
    existing = load_echo('zechariah')
    merge_echo(existing, ZECHARIAH_ECHOES)
    save_echo('zechariah', existing)
    print('Zechariah 14 echoes written.')

if __name__ == '__main__':
    main()
