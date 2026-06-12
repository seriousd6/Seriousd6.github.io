#!/usr/bin/env python3
"""
MKT Echo Layer — Joel chapters 1–3 (completing ch 1; ch 2 and 3 partial)
Run: python3 scripts/zc-echo-joel-1-3-full.py

Echo type: OT → NT direction (where this OT text is taken up in the NT).

Key connections for ch 1:
- 1:4 four-stage locust army → Rev 9:3-11 (eschatological locust plague from the pit)
- 1:6 nation with lion's teeth → Rev 9:8 (verbal echo of lion-teeth locusts)
- 1:8 lament like a virgin → 2 Cor 11:2 (church betrothed as a virgin)
- 1:14 sacred assembly, fast → Acts 2:1; 1:14 (gathered prayer precedes Spirit's coming)
- 1:15 Day of the LORD near → 1 Thess 5:2; Rev 6:17 (NT Day of the Lord language)
- 1:19-20 creation crying out → Rom 8:22 (creation groaning for redemption)

Additional ch 2 and 3 gap coverage:
- 2:12-13 rend hearts not garments → 2 Cor 7:10; Matt 3:8
- 2:25 restore what locusts ate → John 10:10; Rev 21:4-5
- 2:30-31 signs before the day → Matt 24:29-30; Luke 21:25
- 3:2 nations gathered for judgment → Matt 25:31-46; Rev 20:12
- 3:10 plowshares into swords → Rev 19:11-15 (inverse of Isa 2:4 / Mic 4:3)
- 3:18 mountains drip with new wine → Rev 22:1-2 (river of life, new creation abundance)
- 3:21 YHWH dwells in Zion → Rev 21:3 (God's dwelling with his people)
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

JOEL_ECHOES = {
    "1": {
        "4": [
            {
                "type": "allusion",
                "target": "Rev 9:3-11",
                "note": "Joel's four-stage locust swarm (gazam, arbeh, yeleg, chasil — whether four species or four life-stages of the same insect) describes a total stripping of the land. Revelation 9:3-11 draws on this template for the eschatological locust army that ascends from the pit: their appearance is like horses prepared for battle, they have crowns, faces like men, hair like women, teeth like lions (cf. Joel 1:6). The Joel plague is the historical prototype that Revelation universalizes — what fell on one nation now falls on the whole earth, as the covenant lawsuit expands to cosmic dimensions."
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Rev 9:8",
                "note": "The locust nation is described as having 'the teeth of a lion, and the jaw teeth of a great lion' (sinnav ke-ari, metallet'ot laish). Revelation 9:8 picks up the identical image in the eschatological locust vision: 'their teeth were like lions' teeth.' The verbal parallel is deliberate — John reads Joel as the blueprint for his apocalyptic vision, mapping the historical locust judgment onto the final judgment plague against the earth."
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "2 Cor 11:2",
                "note": "Joel calls the nation to 'lament like a virgin (betulah) girded with sackcloth for the husband of her youth.' The image of the virgin betrothed but bereft anticipates the NT's use of bridal language for God's people: Paul tells the Corinthians he has 'betrothed you to one husband, to present you as a pure virgin to Christ' (2 Cor 11:2). The covenantal grief of Joel 1 — the bride cut off from her bridegroom — finds its resolution in the restored betrothal the new covenant provides."
            }
        ],
        "14": [
            {
                "type": "allusion",
                "target": "Acts 1:14",
                "note": "Joel's command to 'consecrate a fast, call a sacred assembly (atzarah), gather the elders' anticipates the gathering of the disciples in Acts 1:14: 'all these were continually devoting themselves to prayer, together with the women and Mary the mother of Jesus.' The pre-Pentecost prayer assembly fulfills the call to solemn assembly before the Day of the LORD — the Spirit's outpouring in Acts 2 is the divine response to the cry for covenant renewal that Joel's atzarah demands."
            },
            {
                "type": "allusion",
                "target": "Acts 2:1",
                "note": "The gathered sacred assembly of Joel 1:14 precedes the Spirit's restoration promise (Joel 2:28-32). Acts 2:1 notes the disciples were 'all together in one place' when the Spirit fell — the Pentecost event is the answer to the kind of solemn, united assembly Joel commands, positioned as God's response to his people gathered in repentance and prayer before his presence."
            }
        ],
        "15": [
            {
                "type": "allusion",
                "target": "1 Thess 5:2",
                "note": "Joel 1:15 introduces the 'Day of the LORD' (Yom YHWH) as near, coming 'as destruction from the Almighty' (shod mishaddai — a Hebrew wordplay). This Day of the LORD language becomes the NT's primary framework for the parousia: Paul tells the Thessalonians 'the day of the Lord will come like a thief in the night' (1 Thess 5:2). The eschatological urgency Joel attaches to the day — it is near, and its character is devastating judgment — becomes the urgency undergirding NT eschatological ethics."
            },
            {
                "type": "allusion",
                "target": "Rev 6:17",
                "note": "The Day of the LORD introduced in Joel 1:15 as a day of destruction near at hand reaches its climax in Revelation's sixth seal: 'the great day of their wrath has come, and who is able to stand?' (Rev 6:17). Joel's locust plague is one preliminary expression of this day; Revelation's seal-judgments are its final, universal expression. The rhetorical question of Revelation echoes Joel 2:11's own question ('the day of the LORD is great and very awesome; who can endure it?')."
            }
        ],
        "19": [
            {
                "type": "allusion",
                "target": "Rom 8:22",
                "note": "Joel's cry 'To you, LORD, I cry — for fire has devoured the open pastures and flame has burned all the trees of the field' (1:19-20) is accompanied by the image of wild animals panting for God (1:20). The whole creation suffering under divine judgment — animals, trees, pastures, water sources — anticipates Paul's vision of a creation 'groaning together in the pains of childbirth' (Rom 8:22) under the bondage of decay, waiting for the redemption that will undo the effects of curse and covenant failure. Joel's lamenting creation is Paul's groaning creation in embryo."
            }
        ]
    },
    "2": {
        "12": [
            {
                "type": "allusion",
                "target": "2 Cor 7:10",
                "note": "The LORD's call in Joel 2:12-13 — 'return to me with all your heart, with fasting, weeping, and mourning; and rend your heart and not your garments' — distinguishes true inward repentance from external performance. Paul's letter to Corinth makes the same distinction: 'godly grief produces repentance that leads to salvation without regret, whereas worldly grief produces death' (2 Cor 7:10). The rending of the heart that Joel demands is precisely the godly grief Paul describes — sorrow that issues in genuine return rather than mere ceremony."
            }
        ],
        "13": [
            {
                "type": "allusion",
                "target": "Matt 3:8",
                "note": "The call to return to YHWH who is 'gracious and merciful, slow to anger, abounding in steadfast love' (Joel 2:13 — echoing Exod 34:6-7, the divine name formula) demands fruit commensurate with repentance. John the Baptist picks up the same demand: 'Bear fruit in keeping with repentance' (Matt 3:8). The character of God that Joel articulates — his hesed as the ground for returning — is the same character that makes the Baptist's call urgent: God's patience makes genuine repentance possible and necessary."
            }
        ],
        "25": [
            {
                "type": "allusion",
                "target": "John 10:10",
                "note": "YHWH's promise to 'restore to you the years that the swarming locust has eaten' (Joel 2:25) is the foundational OT promise of a life recovered from devastation. Jesus's declaration 'I came that they may have life, and have it abundantly' (John 10:10) is the fulfillment of this restorative promise: the thief (the enemy, the destroyer) has stripped the years; the good shepherd comes to restore more than was lost. The locust's theft and God's restoration prefigures the cosmic theft of sin and Christ's abundant counter-gift."
            }
        ],
        "30": [
            {
                "type": "allusion",
                "target": "Matt 24:29",
                "note": "Joel 2:30-31 describes cosmic signs preceding the Day of the LORD: blood, fire, smoke, the sun darkened, the moon turned to blood. Jesus draws on this exact imagery in the Olivet Discourse: 'Immediately after the tribulation of those days, the sun will be darkened, and the moon will not give its light, and the stars will fall from heaven' (Matt 24:29). The Joel passage is the primary template for the eschatological sign-language of Jesus's teaching about the end — not metaphor but the heavenly theater of divine judgment."
            }
        ]
    },
    "3": {
        "2": [
            {
                "type": "allusion",
                "target": "Matt 25:31-46",
                "note": "Joel 3:2 promises YHWH will gather all nations and bring them down to the Valley of Jehoshaphat to enter into judgment with them. This universal judgment of the nations is the OT foreground for Jesus's parable of the sheep and goats in Matthew 25:31-46: 'When the Son of Man comes in his glory... all the nations will be gathered before him, and he will separate people one from another.' Joel's valley becomes the eschatological throne of the Son of Man; the nations' treatment of God's people becomes the criterion of judgment."
            }
        ],
        "10": [
            {
                "type": "allusion",
                "target": "Rev 19:15",
                "note": "Joel 3:10 calls the nations to 'beat your plowshares into swords and your pruning hooks into spears' — the deliberate inversion of Isaiah 2:4 and Micah 4:3. While those prophets envision swords becoming plowshares in the messianic peace, Joel summons the hostile nations to arm themselves for the final battle that will expose their opposition to YHWH. Revelation 19:15 shows the outcome: 'from his mouth comes a sharp sword with which to strike down the nations.' The nations gather armed with swords; the returning Christ strikes them with the sword of his word."
            }
        ],
        "18": [
            {
                "type": "allusion",
                "target": "Rev 22:1-2",
                "note": "Joel 3:18 envisions the eschatological day when 'mountains shall drip sweet wine, hills shall flow with milk, and all the stream beds of Judah shall flow with water; a fountain shall come forth from the house of the LORD.' Revelation 22:1-2 describes the river of the water of life flowing from the throne of God and the Lamb, with the tree of life on either bank bearing fruit for the nations. Joel's fertile new creation — flowing from the divine sanctuary — reaches its canonical climax in Revelation's new Jerusalem, where the curse is abolished and the abundance of Eden is surpassed."
            }
        ],
        "21": [
            {
                "type": "allusion",
                "target": "Rev 21:3",
                "note": "Joel 3:21 closes with 'YHWH dwells in Zion' (YHWH shokhein b'Tzion) — the covenant presence of God with his people as the ultimate goal of all judgment and restoration. Revelation 21:3 reaches the same terminus: 'Behold, the dwelling (skene) of God is with man.' The Hebrew shekhina and the Greek skene share the same root concept — God pitching his tent among his people. Joel's closing promise is the eschatological reality that the whole canon builds toward and Revelation announces as fulfilled."
            }
        ]
    }
}

def main():
    existing = load_echo('joel')
    merge_echo(existing, JOEL_ECHOES)
    save_echo('joel', existing)
    print('Joel 1-3 echoes written.')

if __name__ == '__main__':
    main()
