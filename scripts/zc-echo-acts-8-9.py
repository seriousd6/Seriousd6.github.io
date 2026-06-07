"""
MKT Echo Layer — Acts chapters 8–9
Output: data/echoes/acts.json
Run: python3 scripts/zc-echo-acts-8-9.py

Key decisions:
- Acts 8:32-33 (Isa 53:7-8 quote) already present; merge_echo skips it.
- Acts 9 (Saul's conversion) is one of the NT's most OT-saturated pericopes:
  the Damascus Road theophany echoes Ezekiel/Daniel throne-room scenes;
  Saul's commission echoes the Servant of Isaiah 49 and Jeremiah's call;
  the blind-eyes-opened echoes Isaiah's new-exodus healing promises;
  Tabitha's raising echoes the Elijah/Elisha resurrections in Kings.
- Echo entries are placed on the verse where the echo is most audible;
  multi-verse pericopes anchor to their initial verse.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echoes(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echoes(existing, new_data):
    # INTENT: Add new chapter/verse echo entries without overwriting existing ones — safe to re-run.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update this traversal.
    # VERIFY: Re-running should print same verse counts (no duplicated or overwritten entries).
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries

ACTS_ECHOES = {
"8": {
    "26": [
        {
            "type": "typology",
            "target": "1 Kgs 18:12",
            "note": "Philip 'caught up' by the Spirit after the Ethiopian's baptism echoes Elijah's sudden spirit-transportation. Both prophets fulfill their word and are removed; the Spirit moves the servant from task to task."
        }
    ],
    "32": [
        {
            "type": "fulfillment",
            "target": "Isa 53:7-8",
            "note": "The Ethiopian reads the exact passage of the Suffering Servant led to slaughter without opening his mouth. Philip announces Jesus as the fulfillment of this servant-portrait — the explicit OT-to-Christ bridge of Isaiah's servant songs."
        }
    ]
},
"9": {
    "3": [
        {
            "type": "typology",
            "target": "Ezek 1:28",
            "note": "The sudden light 'flashing from heaven around him' echoes the appearance of the divine glory (kābôd) in Ezekiel's chariot-throne vision — 'the appearance of the likeness of the glory of the LORD.' Divine self-manifestation in overwhelming light is the characteristic form of Israel's theophany tradition."
        },
        {
            "type": "allusion",
            "target": "Dan 10:6",
            "note": "The blinding radiance that fells Saul recalls the appearance of the divine messenger to Daniel — 'his face like the appearance of lightning' — which also left Daniel falling face-down, drained of strength (Dan 10:9, 17)."
        }
    ],
    "4": [
        {
            "type": "typology",
            "target": "Dan 8:17",
            "note": "Saul falling to the ground before the heavenly voice mirrors Daniel 8:17 ('when he came, I was frightened and fell on my face') and 10:9, the posture of human creatureliness before divine appearance throughout the prophetic books."
        }
    ],
    "6": [
        {
            "type": "typology",
            "target": "Isa 6:8-9",
            "note": "The risen Christ's 'rise and go into the city, and you will be told what to do' is the commission-form of the prophetic call: rise (restoration from prostration) + go + receive further instructions. Isaiah's call uses the same sequence — divine appearance, commissioning, and mission assignment."
        },
        {
            "type": "typology",
            "target": "Ezek 2:1",
            "note": "'Son of man, stand on your feet, and I will speak with you' — the 'rise' command in prophetic commissions is YHWH's restoration of the prostrate prophet for active service. The pattern repeats here with Saul: the fallen persecutor is raised for mission."
        }
    ],
    "9": [
        {
            "type": "allusion",
            "target": "Dan 10:17",
            "note": "Saul's three-day blindness, eating nothing, and drinking nothing echoes Daniel's exhaustion-fast after the divine encounter (Dan 10:2-3, 17) — the bodily depletion that accompanies genuine theophanic experience in the biblical tradition."
        }
    ],
    "15": [
        {
            "type": "fulfillment",
            "target": "Isa 49:1-6",
            "note": "Christ's description of Saul as 'a chosen vessel to carry my name before the Gentiles and kings and the children of Israel' fulfills the Servant's calling in Isa 49:1-6 — 'formed from the womb to be his servant... I will make you a light for the nations, that my salvation may reach to the end of the earth.' Saul-become-Paul is the individual embodiment of the Servant's Gentile mission."
        },
        {
            "type": "typology",
            "target": "Jer 1:5",
            "note": "'Before I formed you in the womb I knew you, and before you were born I consecrated you; I appointed you a prophet to the nations' — the divine pre-appointment of Jeremiah as prophet to the nations is the template for Paul's pre-appointment. Both resist at first; both are sent to Gentiles; both suffer for the mission."
        }
    ],
    "16": [
        {
            "type": "fulfillment",
            "target": "Isa 53:3-5",
            "note": "'I will show him how much he must suffer for the sake of my name' — the appointed suffering of the missionary echoes and participates in the Servant's appointed suffering. Paul's sufferings are the extension of the Servant's: 'filling up what is lacking in Christ's afflictions' (Col 1:24). The suffering-for-the-name pattern is the Servant's legacy to every subsequent bearer of that name."
        }
    ],
    "17": [
        {
            "type": "typology",
            "target": "Num 27:18",
            "note": "Ananias laying hands on Saul for the reception of the Spirit echoes Moses laying hands on Joshua to commission him — 'Take Joshua the son of Nun, a man in whom is the Spirit, and lay your hand on him' (Num 27:18). Laying on of hands transfers anointing and commissions for mission throughout the OT."
        }
    ],
    "18": [
        {
            "type": "fulfillment",
            "target": "Isa 42:7",
            "note": "The scales falling from Saul's eyes and his sight being restored fulfills the Servant's mission: 'to open the eyes that are blind.' The persecutor who was spiritually blind receives physical-sight-restoration as the enacted sign of his spiritual new-birth — the Servant's ministry comes first to the one who will carry it to the Gentiles."
        },
        {
            "type": "allusion",
            "target": "Isa 29:18",
            "note": "'In that day the deaf shall hear the words of a book, and out of their gloom and darkness the eyes of the blind shall see' — Isaiah's new-exodus healing promises are enacted each time a blind person receives sight through the Servant and his messengers. Saul's healing is the personal inauguration of the Servant's blindness-healing mission."
        }
    ],
    "20": [
        {
            "type": "typology",
            "target": "Isa 52:7",
            "note": "Saul immediately proclaiming Jesus as Son of God in the synagogues echoes the herald of good news in Isa 52:7 — 'How beautiful are the feet of him who brings good news.' The herald announces what the servant has accomplished; Saul's proclamation is the herald's cry following the servant's resurrection."
        }
    ],
    "22": [
        {
            "type": "allusion",
            "target": "Prov 21:22",
            "note": "Saul 'confounding' (sugchunn— throwing into confusion) the Damascus Jews by proving Jesus is the Christ echoes the wisdom-tradition's image of the wise man who takes the city of the mighty — 'A wise man scales the city of the mighty and brings down the stronghold in which they trust.' Saul's arguments demolish the opponents' positions as wisdom demolishes fortified positions."
        }
    ],
    "31": [
        {
            "type": "allusion",
            "target": "1 Kgs 4:24-25",
            "note": "The summary of ecclesial peace ('the church throughout all Judea and Galilee and Samaria had peace and was being built up') echoes the Solomonic peace-description: 'he had peace on all sides around him, and Judah and Israel lived in safety... each man under his vine and under his fig tree.' The messianic peace of the new-Solomonic kingdom extends to the church's regional flourishing."
        }
    ],
    "34": [
        {
            "type": "typology",
            "target": "2 Kgs 5:10",
            "note": "Peter's command 'Jesus Christ heals you; rise and make your bed' echoes the prophetic-healing command pattern established in Elisha's ministry — most strikingly Elisha's instruction to Naaman ('Go and wash in the Jordan seven times, and your flesh shall be restored') and to the Shunammite's son through Gehazi. The prophet speaks; the healing follows; the pattern is the same because the same Spirit operates."
        },
        {
            "type": "typology",
            "target": "Isa 35:6",
            "note": "'Then shall the lame man leap like a deer' — the new-exodus healing promises of Isaiah 35 continue to be fulfilled in the apostolic healings. Aeneas's 'rise' (anastēthi) from his eight-year paralysis is another instance of the lame-leaping that marks the messianic age."
        }
    ],
    "36": [
        {
            "type": "typology",
            "target": "Prov 31:20",
            "note": "Tabitha is described as 'full of good works and acts of charity' — the portrait of the Proverbs 31 woman who 'opens her hand to the poor and reaches out her hands to the needy.' Her specific works (making tunics and garments, v.39) are the Proverbs 31 woman's textile works embodied in the early church."
        }
    ],
    "37": [
        {
            "type": "typology",
            "target": "1 Kgs 17:17",
            "note": "Tabitha's death and her placement in an upper room echoes the widow of Zarephath's son who died and was laid out — the situation that precedes the Elijah-resurrection miracle. The upper room, the death of someone beloved, the calling for the prophet: all three elements match."
        }
    ],
    "40": [
        {
            "type": "typology",
            "target": "1 Kgs 17:19-22",
            "note": "Peter putting everyone outside, kneeling to pray, then commanding 'Tabitha, rise' (Tabitha, anástēthi) follows the exact sequence of Elijah's resurrection of the widow's son: going to the upper room, lying on the child, calling to the LORD. Luke frames Peter's ministry on the Elijah-Elisha pattern established in chs 1-9 of his Gospel (Luke 7:11-17)."
        },
        {
            "type": "typology",
            "target": "2 Kgs 4:33-35",
            "note": "Elisha also went in alone, shut the door, prayed, and lay on the dead child until the child's body warmed and he sneezed seven times and opened his eyes. Peter's private prayer and command parallels Elisha's methodology — the prophet alone with the dead, prayer, and the spoken word of restoration."
        }
    ]
}
}

def main():
    existing = load_echoes('acts')
    merge_echoes(existing, ACTS_ECHOES)
    save_echoes('acts', existing)
    for ck in ['8', '9']:
        n = len(existing.get(ck, {}))
        print(f'Acts ch {ck}: {n} echo entries')

if __name__ == '__main__':
    main()
