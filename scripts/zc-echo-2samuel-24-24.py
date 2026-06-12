"""
echo | 2 Samuel 24
Run: python3 scripts/zc-echo-2samuel-24-24.py

Key echoes:
- v1: divine/satanic incitement — 1 Chr 21:1 ascribes it to Satan; NT theology of sovereignty/testing
- v10: David's immediate confession — pattern for 1 John 1:9
- v13: three-option judgment triad — sword/famine/plague echoes Jer 14:12; Rev 6:8
- v14: "fall into the hand of the LORD, for his mercy is great" — choosing mercy over human judgment
- v16: angel's hand stayed at Araunah's threshing floor — site identified as Moriah/Temple Mount (2 Chr 3:1)
- v17: David intercedes, "let your hand be against me" — substitutionary logic, type of Christ
- v24: "I will not offer what costs me nothing" — costly sacrifice principle
- v25: prayer for the land answered, plague stopped at the place of future Temple atonement
"""

import json
import pathlib

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


SAMUEL2_CH24_ECHOES = {
    "24": {
        "1": [
            {
                "type": "parallel",
                "target": "1 Chr 21:1",
                "note": "Chronicles attributes the incitement to 'Satan' (haśśāṭān) rather than YHWH, reflecting later Second Temple theology's sharpened distinction between divine and adversarial agency — the same theological move visible in Job 1-2 and Luke 22:31 ('Satan demanded to sift you')."
            }
        ],
        "10": [
            {
                "type": "echo",
                "target": "1 John 1:9",
                "note": "David's immediate confession after the census — 'I have sinned greatly in what I have done' — establishes the pattern: conviction leading directly to confession. 1 John 1:9 'if we confess our sins, he is faithful and just to forgive' is the covenant principle David relies on here."
            }
        ],
        "13": [
            {
                "type": "echo",
                "target": "Rev 6:8",
                "note": "The three-option judgment — famine, military rout, plague — is the classic covenant-curse triad (sword, famine, pestilence: Jer 14:12; Ezek 14:21). Revelation's four horsemen (death, war, famine, plague) are the eschatological form of the same triadic judgment structure."
            }
        ],
        "14": [
            {
                "type": "echo",
                "target": "Lam 3:22",
                "note": "David chooses to 'fall into the hand of the LORD, for his mercy (raḥamîm) is great' — the same theological confidence Jeremiah voices in Lamentations 3:22-23: YHWH's mercies are not exhausted even in judgment. Divine discipline is safer than human enmity because it operates within covenant love."
            }
        ],
        "16": [
            {
                "type": "foreshadow",
                "target": "2 Chr 3:1",
                "note": "The threshing floor of Araunah the Jebusite — where the destroying angel's hand is halted — is identified in 2 Chr 3:1 as Mount Moriah, the site where Solomon builds the Temple. The place where plague-judgment is arrested becomes the perpetual location of Israel's atonement system."
            },
            {
                "type": "echo",
                "target": "Gen 22:14",
                "note": "YHWH's relenting (wayyinnāḥem) at Araunah's threshing floor re-enacts the Moriah pattern of Gen 22: divine judgment arrested at the last moment, a substitute provided, the site named for divine provision. Both Mount Moriah scenes foreshadow the definitive arrested-judgment at Calvary."
            }
        ],
        "17": [
            {
                "type": "foreshadow",
                "target": "Isa 53:6",
                "note": "David's intercession — 'I am the one who sinned … let your hand be against me and my father's house' — is the Davidic king offering himself as substitute for the flock. Isaiah 53:6 fulfills this logic eschatologically: 'the LORD has laid on him the iniquity of us all.' The shepherd-king absorbs the punishment the sheep deserve."
            },
            {
                "type": "echo",
                "target": "Rom 5:8",
                "note": "David's unanswered plea to bear the punishment himself points forward to the one king whose substitutionary offer was accepted: 'while we were still sinners, Christ died for us.' What David requested but could not accomplish, Christ enacted."
            }
        ],
        "24": [
            {
                "type": "echo",
                "target": "Luke 21:3-4",
                "note": "David's refusal of Araunah's free offer — 'I will not sacrifice to the LORD my God burnt offerings that cost me nothing' — is the OT articulation of the widow's costly offering Jesus commends: true worship costs the worshiper something, not token generosity from surplus."
            }
        ],
        "25": [
            {
                "type": "foreshadow",
                "target": "Heb 9:12",
                "note": "The altar where David's burnt and peace offerings stay the plague foreshadows the Temple's sacrificial system centered on this same site. Hebrews 9:12 points to Christ's once-for-all offering as the fulfillment: the location where plague was halted by sacrifice becomes, ultimately, the place from which the eternal high priest enters the heavenly sanctuary."
            },
            {
                "type": "echo",
                "target": "2 Chr 7:14",
                "note": "YHWH responding to David's prayer 'for the land' (wayyēʿāṯēr YHWH lā-ʾāreṣ) and withdrawing the plague anticipates Solomon's dedicatory prayer for the same site: 2 Chr 7:14 'if my people … pray and seek my face … I will hear from heaven and forgive their sin and heal their land.'"
            }
        ]
    }
}


def main():
    existing = load_echo('2samuel')
    merge_echo(existing, SAMUEL2_CH24_ECHOES)
    save_echo('2samuel', existing)

    ch24 = existing.get('24', {})
    print(f'ch 24: {len(ch24)} verse entries')
    total = sum(len(v) for v in ch24.values())
    print(f'Total echo entries in ch 24: {total}')
    all_chs = sorted(existing.keys(), key=int)
    print(f'Chapters with echo data: {all_chs}')


if __name__ == '__main__':
    main()
