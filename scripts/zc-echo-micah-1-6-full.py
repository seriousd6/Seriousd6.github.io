#!/usr/bin/env python3
"""
MKT Echo Layer — Micah chapters 1–6 (chs 1–4 missing; 5 and 6 partial)
Run: python3 scripts/zc-echo-micah-1-6-full.py

Echo type: OT → NT direction.
Ch 5:2 (Bethlehem → Matt 2:6) and 6:8 (justice/mercy → Matt 23:23) already present.

Key connections for chs 1–4:
- 1:4 mountains melt like wax → 2 Pet 3:10; Rev 20:11 (cosmic dissolution at judgment)
- 1:16 mourning for children → Matt 2:17-18 (Herod's massacre / Rachel weeping)
- 2:12-13 the Breaker goes before them → John 10:3-4 (shepherd leads out)
- 3:5 prophets cry peace for money → Matt 7:15 (wolves in sheep's clothing)
- 3:12 Zion plowed as a field → Matt 24:2; Luke 19:44 (temple destruction)
- 4:1-2 mountain of YHWH in latter days → Heb 12:22; Rev 21:10 (heavenly Zion)
- 4:3 swords into plowshares → Rev 21:4 (no more war/pain in new creation)
- 4:4 each under his vine and fig tree → John 1:48 (Nathanael under the fig tree)
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

MICAH_ECHOES = {
    "1": {
        "4": [
            {
                "type": "allusion",
                "target": "2 Pet 3:10-12",
                "note": "Micah's theophany vision — mountains melting under YHWH like wax before fire, valleys splitting apart — is the OT prototype for the NT's descriptions of cosmic dissolution at the Day of the Lord. 2 Peter 3:10-12 describes the elements dissolving with fire and the earth being exposed for judgment. Revelation 20:11 depicts the great white throne before which earth and sky fled and no place was found for them. What Micah renders as the local expression of YHWH descending in judgment, Peter and John universalize into the final cosmic reckoning when all creation is exposed before its Creator."
            }
        ],
        "16": [
            {
                "type": "allusion",
                "target": "Matt 2:17-18",
                "note": "Micah's lament for the Shephelah towns ends with a call to mourning for 'your cherished children' — the language of Rachel's grief for her lost children. Matthew 2:17-18 cites Jeremiah 31:15 (which draws on Rachel's weeping) when Herod massacres the infants of Bethlehem, in the wake of the Magi's visit. The mourning Micah calls for — parents bereaved of children by the advancing enemy — finds its NT fulfillment in the grief that attends the birth of the one born in Bethlehem (Mic 5:2). The child who is born and the grief over children who die are bound together in both texts."
            }
        ]
    },
    "2": {
        "12": [
            {
                "type": "allusion",
                "target": "John 10:3-4",
                "note": "Micah 2:12-13 promises a Breaker (<em>poreitz</em>) who will go up before the sheep, breaking open the way, YHWH at their head. The image is of a shepherd-leader who breaks through the gate of confinement and leads the flock out and forward. Jesus's Good Shepherd discourse in John 10:3-4 uses the identical structure: 'he calls his own sheep by name and leads them out... he goes before them, and the sheep follow him.' The Breaker of Micah who shatters the enclosure and leads the remnant out is the pattern the incarnate Shepherd fulfills — breaking the enclosure of sin and death and leading the flock through."
            }
        ]
    },
    "3": {
        "5": [
            {
                "type": "allusion",
                "target": "Matt 7:15",
                "note": "Micah's indictment of prophets who cry 'Peace' when given food but declare war against those who give nothing is the OT definition of the false prophet — one who calibrates the message to the audience's economic generosity. Jesus's warning in the Sermon on the Mount — 'Beware of false prophets, who come to you in sheep's clothing but inwardly are ravenous wolves' (Matt 7:15) — targets the same phenomenon. Luke 6:26 adds the economic dimension: 'Woe to you, when all people speak well of you' — the popularity that Micah's paid prophets cultivate is precisely the sign of their falseness."
            }
        ],
        "12": [
            {
                "type": "allusion",
                "target": "Matt 24:2",
                "note": "Micah 3:12 is one of the most audacious prophetic declarations in the OT — Zion plowed as a field, Jerusalem a heap of ruins, the temple mount overgrown. Jeremiah 26:18 records that Micah's oracle was remembered in Hezekiah's day as the precedent for prophetic temple-critique. Jesus's own temple prediction — 'there will not be left here one stone upon another that will not be thrown down' (Matt 24:2) — stands in direct succession to Micah 3:12. Micah's oracle is fulfilled in 586 BCE; Jesus's oracle is fulfilled in 70 CE. The pattern of temple-destruction as covenant judgment runs continuously."
            }
        ]
    },
    "4": {
        "1": [
            {
                "type": "allusion",
                "target": "Heb 12:22",
                "note": "Micah 4:1-2 (= Isa 2:2-3) envisions the mountain of YHWH's house established as the highest of mountains in the latter days, with all nations streaming to it to receive instruction. Hebrews 12:22 announces the fulfillment: 'you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem.' What Micah envisions as the eschatological destination of the nations, Hebrews declares is the present reality for those who have come to Jesus, the mediator of the new covenant. The pilgrimage to the mountain has already begun — not geographically but by faith in Christ."
            },
            {
                "type": "allusion",
                "target": "Rev 21:10",
                "note": "The vision of Micah 4:1-2 — the highest mountain from which YHWH's word goes forth — reaches its final form in Revelation 21:10: John is taken to 'a great, high mountain, and showed the holy city Jerusalem coming down out of heaven from God.' The mountain from which instruction goes out is now the mountain from which the new Jerusalem descends. The direction is reversed: instead of nations going up to the mountain, the city from the mountain comes down to the nations. Both visions describe the same eschatological reality — the meeting of heaven and earth — from different vantage points."
            }
        ],
        "3": [
            {
                "type": "allusion",
                "target": "Rev 21:4",
                "note": "The great vision of disarmament — 'they shall beat their swords into plowshares and their spears into pruning hooks; nation shall not lift up sword against nation, neither shall they learn war anymore' (Mic 4:3 = Isa 2:4) — is the OT's most concentrated expression of the peace the messianic age will bring. Revelation 21:4 declares the eschatological fulfillment: 'death shall be no more, neither shall there be mourning, nor crying, nor pain anymore.' War is the instrument of death; its abolition is the condition for the world without pain that Revelation describes. The swords-to-plowshares vision is realized when death itself is cast into the lake of fire (Rev 20:14)."
            }
        ],
        "4": [
            {
                "type": "allusion",
                "target": "John 1:48",
                "note": "The eschatological peace-symbol — 'they shall sit every man under his vine and under his fig tree, and no one shall make them afraid' (Mic 4:4) — appears in Zechariah 3:10 and 1 Kings 4:25 as the emblem of secure, Solomonic abundance. When Jesus sees Nathanael approaching and says 'before Philip called you, when you were under the fig tree, I saw you' (John 1:48), the resting-under-the-fig-tree image evokes this messianic peace. Nathanael's being-seen under the fig tree — and his immediate confession of Jesus as Son of God and King of Israel (John 1:49) — is a compressed sign of the messianic peace Micah describes arriving in the person of the one Nathanael has just recognized."
            }
        ]
    }
}

def main():
    existing = load_echo('micah')
    merge_echo(existing, MICAH_ECHOES)
    save_echo('micah', existing)
    print('Micah 1-6 echoes written.')

if __name__ == '__main__':
    main()
