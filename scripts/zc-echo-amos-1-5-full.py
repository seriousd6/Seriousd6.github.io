#!/usr/bin/env python3
"""
MKT Echo Layer — Amos chapters 1–5 (chs 1–4 missing; ch 5 partial)
Run: python3 scripts/zc-echo-amos-1-5-full.py

Echo type: OT → NT direction.

Key connections:
- 1:2 YHWH roars from Zion → Rev 5:5 (Lion of Judah); Heb 12:26
- 2:6 sold the righteous for silver → Matt 26:14-15 (Judas)
- 2:11 raised up prophets but you made them not prophesy → Matt 23:34-37
- 3:7 YHWH reveals secret (sod) to prophets → Rev 10:7; 1 Cor 2:10
- 3:8 lion has roared, who can but prophesy? → 1 Cor 9:16
- 4:11 like Sodom and Gomorrah → 2 Pet 2:6; Jude 7
- 4:12 prepare to meet your God → Heb 9:27; Rev 20:12
- 5:14-15 hate evil, love good → Rom 12:9 (near-verbatim echo)
- 5:21-24 I hate your feasts; let justice roll → Matt 23:23; Luke 11:42
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

AMOS_ECHOES = {
    "1": {
        "2": [
            {
                "type": "allusion",
                "target": "Rev 5:5",
                "note": "Amos opens with YHWH roaring from Zion like a lion: 'The LORD roars from Zion and utters his voice from Jerusalem.' Revelation 5:5 identifies the exalted Christ as 'the Lion of the tribe of Judah, the Root of David,' who has conquered. The lion-roar from Zion that opens Amos's prophecy of judgment is the same royal voice that in Revelation vindicates the cosmos. What Amos hears as terrifying judgment-announcement, Revelation hears as the victorious proclamation of the enthroned Lamb-Lion."
            },
            {
                "type": "allusion",
                "target": "Heb 12:26",
                "note": "The voice from Zion that causes Carmel to wither (1:2) anticipates Hebrews 12:26's citation of Haggai about the voice that shakes heaven and earth. Both texts draw on the same tradition of the divine voice that exercises cosmos-level power from the sanctuary. Hebrews contrasts the terrifying voice at Sinai with the voice of the heavenly Zion — which is the same lion-roar now mediated through the blood of Jesus, making judgment and grace simultaneous."
            }
        ]
    },
    "2": {
        "6": [
            {
                "type": "allusion",
                "target": "Matt 26:14-15",
                "note": "Amos's indictment of Israel includes the charge that 'they sell the righteous for silver, and the needy for a pair of sandals' (2:6) — the one who should be vindicated in court is instead traded as a commodity for gain. Matthew 26:14-15 presents the ultimate irony of this pattern: Judas negotiates with the chief priests to betray Jesus for thirty pieces of silver. The righteous one, the just one, is sold for money — exactly the covenant violation Amos names as Israel's definitive transgression."
            }
        ],
        "11": [
            {
                "type": "allusion",
                "target": "Matt 23:34-37",
                "note": "YHWH's complaint in Amos 2:11-12 is that he raised up prophets and Nazirites from Israel's own sons, yet Israel commanded the prophets not to prophesy. Jesus echoes this pattern in Matthew 23:34-37: 'I am sending you prophets and wise men and scribes, some of whom you will kill and crucify... Jerusalem, Jerusalem, the city that kills the prophets.' The rejection of divinely-sent messengers is the sustained pattern Amos identifies and Jesus stands at the end of."
            }
        ]
    },
    "3": {
        "7": [
            {
                "type": "allusion",
                "target": "Rev 10:7",
                "note": "Amos 3:7 states the governing principle of biblical prophecy: 'Surely the Lord YHWH does nothing without revealing his secret (sod) to his servants the prophets.' Revelation 10:7 announces the completion of this revelatory economy: 'in the days of the trumpet call to be sounded by the seventh angel, the mystery (mysterion) of God would be fulfilled, just as he announced to his servants the prophets.' The Greek mysterion translates the Hebrew sod — what Amos claims as a structural axiom of God's dealings, Revelation declares is about to be completed in Christ."
            },
            {
                "type": "allusion",
                "target": "1 Cor 2:10",
                "note": "The divine sod (council-secret) that YHWH reveals to his prophets (Amos 3:7) is the OT background for Paul's claim in 1 Corinthians 2:10 that 'God has revealed these things to us through the Spirit.' The Spirit searches even the depths of God and communicates them to those he indwells — the prophetic principle of Amos (revelation as a structural feature of God's relationship with his people) is now democratized through the Spirit's universal indwelling of the church."
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "1 Cor 9:16",
                "note": "Amos 3:8 offers a compulsion-argument for prophecy: 'The lion has roared; who will not fear? The Lord YHWH has spoken; who can but prophesy?' The divine speech creates an irresistible prophetic necessity. Paul gives the same argument in 1 Corinthians 9:16: 'Woe to me if I do not preach the gospel! For necessity is laid upon me.' The prophetic compulsion Amos names as the response to the lion's roar is the same necessity Paul names as the ground of his apostolic commission — to hear God's word and not speak it is impossible."
            }
        ]
    },
    "4": {
        "11": [
            {
                "type": "allusion",
                "target": "Jude 7",
                "note": "YHWH's description of Israel's judgment — 'I overthrew some of you, as when God overthrew Sodom and Gomorrah, and you were like a brand plucked out of the fire' (4:11) — deploys Sodom and Gomorrah as the paradigmatic case of covenant judgment. Jude 7 uses the same reference eschatologically: Sodom and Gomorrah 'serve as an example by undergoing a punishment of eternal fire.' What YHWH did to Israel's cities is a foretaste of the final judgment Sodom prefigured — Amos's warning is Jude's exhibit A."
            }
        ],
        "12": [
            {
                "type": "allusion",
                "target": "Heb 9:27",
                "note": "The climax of Amos 4's covenant lawsuit is the stark summons: 'Prepare to meet your God, O Israel.' Having enumerated the plagues that did not produce repentance, YHWH declares the encounter unavoidable. Hebrews 9:27 restates this as the universal human condition: 'It is appointed for man to die once, and after that comes judgment.' The summons to meet God that Amos delivers as prophetic shock to a covenant people becomes in Hebrews the inescapable appointment every human being keeps. Christ's once-for-all sacrifice is the only preparation that suffices."
            },
            {
                "type": "allusion",
                "target": "Rev 20:12",
                "note": "The command to 'prepare to meet your God' (4:12) anticipates Revelation 20:12's vision of the great white throne judgment: 'I saw the dead, great and small, standing before the throne, and books were opened.' What Amos announces as the imminent encounter between YHWH and a covenant-breaking nation, Revelation universalizes as the final meeting between every human being and their Creator. Amos's covenant lawsuit becomes John's vision of universal accountability."
            }
        ]
    },
    "5": {
        "14": [
            {
                "type": "allusion",
                "target": "Rom 12:9",
                "note": "Amos 5:14-15 — 'Seek good, not evil, that you may live... Hate evil, love good, and establish justice in the gate' — is the ethical positive of the book's indictments. Paul's ethical summation in Romans 12:9 echoes the same language: 'Let love be genuine. Abhor what is evil; hold fast to what is good.' The near-verbal parallel is striking: shiknu ra, ahavu tov (hate evil, love good) in Amos maps directly onto Paul's apostolic paraenesis. The same moral logic runs from the covenant community of Israel to the community of Christ."
            }
        ],
        "21": [
            {
                "type": "allusion",
                "target": "Matt 23:23",
                "note": "Amos 5:21-24 is the most concentrated OT critique of worship divorced from justice: 'I hate, I reject your festivals... but let justice roll down like waters, and righteousness like an ever-flowing stream.' Jesus's rebuke of the scribes and Pharisees in Matthew 23:23 makes the same move: 'You tithe mint and dill and cumin, and have neglected the weightier matters of the law: justice and mercy and faithfulness.' Both texts are not anti-worship but pro-integration — ritual without justice is the form of religion that both prophets condemn."
            }
        ]
    }
}

def main():
    existing = load_echo('amos')
    merge_echo(existing, AMOS_ECHOES)
    save_echo('amos', existing)
    print('Amos 1-5 echoes written.')

if __name__ == '__main__':
    main()
