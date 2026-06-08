"""
echo | Isaiah | 19-23 | python3 scripts/zc-echo-isaiah-19-23.py

Key echo decisions:
- Isa 19:1 (LORD on swift cloud) -> Rev 1:7; Dan 7:13: theophanic cloud-coming
- Isa 19:23-25 (Egypt/Assyria in covenant) -> Eph 2:14-19; Gal 3:28: Gentile inclusion
- Isa 21:9 ("Fallen, fallen is Babylon") -> Rev 14:8; 18:2: direct verbal citation
- Isa 22:13 ("eat, drink, for tomorrow we die") -> 1 Cor 15:32: direct citation
- Isa 22:22 (key of David on Eliakim) -> Rev 3:7: direct citation applied to Christ
- Isa 23:17-18 (Tyre prostitution/commerce) -> Rev 17:2; 18:3; 21:24-26: Babylon-Tyre merge
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

ISAIAH_ECHOES = {
    "19": {
        "1": [
            {"type": "allusion", "target": "Rev 1:7", "note": "LORD coming on a swift cloud echoes the theophanic cloud-coming applied to Christ in Rev 1:7 (citing Dan 7:13); the same divine chariot imagery underlies both."},
            {"type": "allusion", "target": "Dan 7:13", "note": "The swift cloud as the divine vehicle recalls the Son of Man coming with clouds of heaven (Dan 7:13), the text NT writers consistently apply to Christ's coming in glory."}
        ],
        "16": [
            {"type": "allusion", "target": "Matt 24:6-8", "note": "Egypt trembling before the hand of the LORD anticipates the birth-pangs language of eschatological shaking (Matt 24:6-8); the nations in terror before divine judgment is a recurrent apocalyptic pattern."}
        ],
        "18": [
            {"type": "allusion", "target": "Zeph 3:9", "note": "Five Egyptian cities swearing loyalty to the LORD and speaking the language of Canaan anticipates Zeph 3:9 (a pure language given to the nations to call on the LORD) and the Pentecost reversal of Babel (Acts 2:4-11)."}
        ],
        "19": [
            {"type": "type", "target": "John 4:21-23", "note": "An altar to the LORD in the heart of Egypt anticipates the new-covenant worship Jesus announces to the Samaritan woman: worship in spirit and truth, not limited to one geographic location (John 4:21-23); fulfilled in the global church."}
        ],
        "20": [
            {"type": "fulfillment", "target": "Rom 15:9", "note": "The sign/witness to the LORD in Egypt foreshadows the Gentile mission; Paul's catena in Rom 15:9-12 builds on Isaiah's vision of nations calling on the LORD's name, of which this passage is an early anticipation."}
        ],
        "21": [
            {"type": "allusion", "target": "Rev 11:13", "note": "Egypt giving glory to God (the sign/witness in the land) anticipates the nations giving glory to God in Rev 11:13, the post-judgment response that signals eschatological conversion."}
        ],
        "22": [
            {"type": "allusion", "target": "Jas 5:15", "note": "The LORD striking Egypt and then healing — turning punishment into restoration — parallels the NT pattern of discipline leading to healing (Jas 5:15; Heb 12:10-11); judgment is not the final word."}
        ],
        "23": [
            {"type": "type", "target": "Eph 2:14-19", "note": "A highway uniting Egypt, Assyria, and Israel — three formerly hostile nations — as co-worshippers of the LORD prefigures the breaking down of the dividing wall in Christ (Eph 2:14); the triple blessing anticipates the one new humanity."}
        ],
        "24": [
            {"type": "fulfillment", "target": "Gal 3:28", "note": "Israel as the third alongside Egypt and Assyria, all three equally a blessing in the earth, is a striking OT anticipation of Gal 3:28 (neither Jew nor Greek) and the Gentile mission of Acts; geography dissolves into covenant family."}
        ],
        "25": [
            {"type": "fulfillment", "target": "Rom 9:25-26", "note": "Blessed be Egypt my people, and Assyria the work of my hands — extending covenant language (my people, the work of my hands) to Israel's ancient enemies anticipates the Gentile adoption Paul describes using Hosea in Rom 9:25-26 and the nations becoming heirs of Abraham (Gal 3:14; Eph 2:12-13)."}
        ]
    },
    "20": {
        "2": [
            {"type": "type", "target": "Heb 11:37", "note": "Isaiah's commanded nakedness as a three-year prophetic sign-act is one of the most radical embodied prophecies in the OT; the shame-bearing prophet anticipates the shame endured by the servants listed in Heb 11:37 and ultimately by Christ (Heb 12:2)."}
        ],
        "3": [
            {"type": "allusion", "target": "Heb 12:2", "note": "Isaiah's three-year barefoot, naked witness as a sign of coming Assyrian humiliation of Egypt typifies the pattern of the servant who bears shame for a redemptive purpose — the pattern completed in Christ despising the shame of the cross (Heb 12:2)."}
        ]
    },
    "21": {
        "6": [
            {"type": "allusion", "target": "Rev 3:2-3", "note": "The LORD stationing a watchman to report what he sees anticipates the watching motif of Rev 3:2-3 (be watchful) and Rev 16:15 (blessed is the one who stays awake); the watchman's posture is the eschatological stance of the church awaiting Christ's return."}
        ],
        "9": [
            {"type": "citation", "target": "Rev 14:8", "note": "Fallen, fallen is Babylon — directly cited as a refrain in Rev 14:8 and Rev 18:2 (the angel announcing Babylon's fall); Isaiah's oracle against historical Babylon becomes the script for the final judgment of spiritual Babylon in Revelation."},
            {"type": "citation", "target": "Rev 18:2", "note": "Fallen, fallen is Babylon — verbatim in Rev 18:2, the great city announcement. John's angel re-utters Isaiah's prophetic pronouncement, identifying Rome (spiritual Babylon) as the latter-day fulfillment of what Babylon the empire typified."}
        ],
        "10": [
            {"type": "allusion", "target": "1 Cor 15:58", "note": "What the LORD of hosts has declared — the trustworthy word handed to the people crushed and winnowed — parallels Paul's appeal to the certain resurrection word as the basis for steadfastness in labor (1 Cor 15:58); divine announcement grounds human endurance."}
        ],
        "11": [
            {"type": "allusion", "target": "John 9:4", "note": "The watchman's reply — morning is coming, but so is the night — anticipates the night/day dualism of John 9:4 (work while it is day; night is coming) and the eschatological tension between the already of resurrection dawn and the still-coming darkness before the final day."}
        ]
    },
    "22": {
        "13": [
            {"type": "citation", "target": "1 Cor 15:32", "note": "Let us eat and drink, for tomorrow we die — directly quoted by Paul in 1 Cor 15:32 as the logical conclusion of a life without resurrection hope; if there is no resurrection, carpe diem nihilism is the only rational response. Paul cites Isaiah to show what is at stake in the resurrection."}
        ],
        "20": [
            {"type": "type", "target": "Luke 16:10", "note": "Eliakim is called my servant — a Servant of the LORD title also given to the Davidic king; his appointment over the household foreshadows the faithful servant of the parables (Matt 24:45; Luke 16:10) and ultimately Christ as the one appointed over the Father's house (Heb 3:6)."}
        ],
        "22": [
            {"type": "citation", "target": "Rev 3:7", "note": "I will lay on his shoulder the key of the house of David; what he opens no one can shut, and what he shuts no one can open — directly applied to Christ in Rev 3:7 (the Philadelphian letter). Jesus holds the key of David: the authority over the messianic kingdom, access to God's house, and resurrection power over death (Rev 1:18)."},
            {"type": "allusion", "target": "Matt 16:19", "note": "The key of the house of David given to Eliakim anticipates the keys of the kingdom given to Peter (Matt 16:19); the binding and loosing authority derives from the royal-servant key-bearer motif here in Isaiah."}
        ],
        "23": [
            {"type": "allusion", "target": "Heb 6:19", "note": "Eliakim driven like a peg into a solid place, becoming a throne of glory — the firm peg as anchor of trust anticipates Heb 6:19 (hope as an anchor, firm and secure, entering the inner sanctuary); the image of something firmly placed inside the holy place of God's presence."}
        ]
    },
    "23": {
        "1": [
            {"type": "allusion", "target": "Rev 18:17", "note": "The lament over Tyre — no harbor, ships of Tarshish wailing — is absorbed into Rev 18:17-19's lament over fallen Babylon; every merchant ship captain who trades on the sea mourns the great city, echoing Isaiah's lamentation over the merchant city of Tyre."}
        ],
        "8": [
            {"type": "allusion", "target": "Rev 18:23", "note": "Tyre the crown-bestowing city whose traders were princes — the pride of merchant commerce — anticipates Rev 18:23 where Babylon's merchants were the great ones of the earth; the critique of commercial empire as idolatry runs from Isaiah through Revelation."}
        ],
        "15": [
            {"type": "allusion", "target": "Jer 25:11-12", "note": "Seventy years of Tyre's forgetting echoes the seventy-year exile of Jer 25:11-12 and Daniel's seventy weeks (Dan 9:2,24-27); the number seventy as a bounded period of judgment followed by restoration is a structuring motif across the prophets."}
        ],
        "17": [
            {"type": "allusion", "target": "Rev 17:2", "note": "Tyre returning to her earnings and playing the prostitute with all the kingdoms of the world — this language of harlotry and commercial empire is directly absorbed into Rev 17:2 (the great prostitute, with whom the kings of the earth committed sexual immorality) and Rev 18:3 (nations drunk on the wine of her adulteries)."},
            {"type": "allusion", "target": "Rev 18:3", "note": "Tyre as the trading harlot of the nations feeds directly into Rev 18:3's description of Babylon as the harlot whose merchants made the nations drunk; Isaiah's oracle against Tyre provides the prophetic template for the Babylon vision."}
        ],
        "18": [
            {"type": "allusion", "target": "Rev 21:24-26", "note": "Tyre's merchandise and earnings set apart as holy to the LORD — not stored or hoarded but given for abundant provision — anticipates Rev 21:24-26 where the nations bring their glory and honor into the new Jerusalem; the wealth of the Gentiles consecrated to God's service."}
        ]
    }
}

def main():
    data = load_echo('isaiah')
    merge_echo(data, ISAIAH_ECHOES)
    total = sum(len(v) for ch in data.values() for v in ch.values())
    chs = sorted(data.keys(), key=int)
    print(f'Isaiah echoes: {len(chs)} chapters, {total} entries total')
    save_echo('isaiah', data)

if __name__ == '__main__':
    main()
