"""
echo: Habakkuk ch3 — adds echo entries for the theophanic prayer (ch1 and ch2 already done).
merge_echo never overwrites existing entries.
Run: python3 scripts/zc-echo-habakkuk-1-3.py
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
    "3": {
        "13": [
            {
                "type": "allusion",
                "target": "Gen 3:15",
                "note": "You went out for the salvation of your people, with your anointed (meshiach) you crushed the head of the wicked — Habakkuk's theophanic vision pictures YHWH going out with his anointed to crush the enemy; the head-crushing echoes the protoevangelium of Gen 3:15 (he will bruise your head); the anointed who fights in YHWH's salvation is the messianic figure whose ultimate act is the crushing of the serpent's head at the cross"
            },
            {
                "type": "allusion",
                "target": "Heb 1:3",
                "note": "You crushed the head of the house of the wicked — the theophanic warrior YHWH going out with his anointed one; Hebrews 1:3 presents Christ as the one who after making purification for sins sat down at the right hand of the Majesty on high; Habakkuk's vision of the divine warrior going out for salvation is the OT template for what Hebrews describes as accomplished"
            }
        ],
        "17": [
            {
                "type": "allusion",
                "target": "Phil 4:11-13",
                "note": "Though the fig tree does not blossom, nor fruit be on the vines... yet I will rejoice in the LORD — Habakkuk's resolve to rejoice despite total agricultural collapse is the OT anticipation of Paul's contentment theology: I have learned in whatever state I am to be content (Phil 4:11); I can do all things through him who strengthens me (4:13); the joy that transcends circumstances is rooted in the same conviction Habakkuk expresses — salvation belongs to YHWH regardless of visible circumstances"
            }
        ],
        "18": [
            {
                "type": "allusion",
                "target": "Phil 4:4",
                "note": "Yet I will rejoice in the LORD; I will take joy in the God of my salvation — the resolve to rejoice in God despite external ruin is the OT ground of Paul's rejoice always (Phil 4:4); the God of my salvation (elohei yishi) is the same divine-salvation ground as the NT's joy in Christ; Habakkuk 3:17-18 is the OT's most concentrated statement of faith-despite-circumstances"
            }
        ],
        "19": [
            {
                "type": "allusion",
                "target": "2 Cor 12:9-10",
                "note": "God, the LORD, is my strength; he makes my feet like deer's feet — Habakkuk's closing confession that divine strength enables him to walk on high places despite crisis; Paul's my grace is sufficient for you, for my power is made perfect in weakness (2 Cor 12:9) is the NT form of the same conviction: divine strength given to the weak precisely in weakness; the deer's feet enabling sure-footed movement on dangerous heights is the image of grace-enabled perseverance"
            },
            {
                "type": "allusion",
                "target": "Ps 18:33",
                "note": "He makes my feet like the feet of deer and makes me tread on my high places — Habakkuk 3:19 is nearly identical to Ps 18:33 (He made my feet like the feet of a deer and set me secure on the heights); both texts use the deer-footed-on-heights image for divine empowerment; Psalm 18 is David's song after YHWH delivered him from all his enemies — the shared vocabulary links Habakkuk's prophetic confidence to the Davidic covenant of divine protection"
            }
        ]
    }
}


def main():
    e = load_echo('habakkuk')
    merge_echo(e, DATA)
    save_echo('habakkuk', e)
    total = sum(len(vv) for vv in DATA.values())
    print(f'habakkuk echo: added ch3 entries ({total} verses with echoes)')


if __name__ == '__main__':
    main()
