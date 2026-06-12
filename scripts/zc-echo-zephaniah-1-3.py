"""
echo: Zephaniah ch1-2 — adds echo entries for the Day of Wrath (ch1) and nations
judgment / remnant (ch2). Ch3 already has echo data; merge_echo never overwrites.
Run: python3 scripts/zc-echo-zephaniah-1-3.py
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


DATA = {
    "1": {
        "14": [
            {
                "type": "allusion",
                "target": "Rev 6:17",
                "note": "The great day of the LORD is near, near and hastening fast — Zephaniah's Dies Irae portrait of the Day of the LORD (vv14-16: wrath, distress, anguish, ruin, devastation, darkness, gloom, clouds, trumpet blast, battle cry) is the OT template for Revelation's Great Day of Wrath; Rev 6:17 ('the great day of their wrath has come, and who can stand?') echoes Zephaniah's portrait directly; the eschatological day Zephaniah foresaw finds its ultimate fulfillment in the final judgment of Revelation"
            },
            {
                "type": "allusion",
                "target": "1 Thess 5:2",
                "note": "The great day of the LORD is near, near and hastening fast — Paul's day of the Lord comes like a thief in the night (1 Thess 5:2) draws on the OT Day of the LORD tradition that Zephaniah articulates most intensely; both texts stress the imminence and suddenness of the day; Paul applies the OT's Day of YHWH to the return of Christ"
            }
        ],
        "18": [
            {
                "type": "allusion",
                "target": "1 Pet 1:18-19",
                "note": "Neither their silver nor their gold shall be able to deliver them on the day of the LORD's wrath — Zephaniah declares that material wealth cannot buy escape from divine judgment; Peter echoes the same contrast: you were ransomed not with perishable things such as silver or gold but with the precious blood of Christ (1 Pet 1:18-19); what silver and gold cannot accomplish, the blood of Christ accomplishes — deliverance from the day of wrath"
            }
        ]
    },
    "2": {
        "3": [
            {
                "type": "allusion",
                "target": "Matt 5:3-5",
                "note": "Seek the LORD, all you humble of the land, who do his just commands; seek righteousness, seek humility — Zephaniah's call to seek YHWH through righteousness and humility (anavah) is the OT anticipation of the Beatitudes; blessed are the poor in spirit (Matt 5:3), blessed are the meek (5:5) — the meek (anavim/praeis) who seek humility in Zephaniah are the blessed of the Sermon on the Mount; both texts present the humble remnant as the recipients of divine favor in the coming day of judgment"
            }
        ],
        "11": [
            {
                "type": "allusion",
                "target": "Phil 2:10-11",
                "note": "To him shall bow down, each in its place, all the lands of the nations — Zephaniah's vision of the universal prostration of the nations before YHWH (after he makes all the gods of the earth shrivel up) is the OT template for Paul's universal-homage passage in Phil 2:10-11: at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue confess that Jesus Christ is Lord; Zephaniah's eschatological vision of the nations bowing before YHWH is fulfilled when they bow before the risen Christ"
            }
        ]
    }
}


def main():
    e = load_echo('zephaniah')
    merge_echo(e, DATA)
    save_echo('zephaniah', e)
    total = sum(len(vv) for vv in DATA.values())
    print(f'zephaniah echo: added ch1-2 entries ({total} chapters with echoes)')


if __name__ == '__main__':
    main()
