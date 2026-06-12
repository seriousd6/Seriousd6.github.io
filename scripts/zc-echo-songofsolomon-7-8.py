#!/usr/bin/env python3
"""
MKT Echo Layer — Song of Solomon chapters 7–8
Run: python3 scripts/zc-echo-songofsolomon-7-8.py

Echo type: OT → NT direction (where this OT text is taken up in the NT).
No parallels file exists for Song of Solomon; echoes written from scratch.

Key connections for chs 7–8:
- 7:10 teshuqah (desire) reverses the curse of Gen 3:16 → fulfilled in Christ's
  desire for his bride (Eph 5:25; John 17:24)
- 7:12 "I will give you my love" in the vineyard → John 15:1-5 (vine and branches)
- 8:1-2 longing for the beloved as brother → Heb 2:11 (Christ not ashamed to call
  them brothers); the incarnation as the answer to the concealed intimacy
- 8:5 "coming up from the wilderness" → Hos 2:14-15 and Rev 12:6
- 8:7 many waters cannot quench love → Rom 8:38-39
- 8:14 "Make haste, my beloved" → Rev 22:20 (Maranatha / Come, Lord Jesus)
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

SONGOFSOLOMON_ECHOES = {
    "7": {
        "10": [
            {
                "type": "allusion",
                "target": "Eph 5:25-27",
                "note": "The beloved's declaration — 'I am my beloved's, and his desire is for me' — uses the rare word teshuqah (desire), the same word in Gen 3:16 where desire becomes distortion under the curse. Song 7:10 reverses this: the beloved's desire is now received as gift, not distortion. Paul's vision of Christ's love for the church (Eph 5:25-27: 'as Christ loved the church and gave himself up for her') is the new covenant fulfillment of this restored desire — the bridegroom's self-giving as the ultimate expression of the desire the Song describes."
            },
            {
                "type": "allusion",
                "target": "John 17:24",
                "note": "The mutual possession formula culminates in the beloved's desire being for her — a desire that mirrors Jesus's prayer in John 17:24: 'Father, I want those also whom you have given me to be with me where I am, to see my glory.' Christ's desire for his people is the ground of the eschatological consummation the Song anticipates."
            }
        ],
        "12": [
            {
                "type": "allusion",
                "target": "John 15:1-5",
                "note": "The beloved's invitation — to go to the vineyards and see whether the vine has budded, and 'there I will give you my love' — situates love's giving within the vineyard-fruitfulness setting. Jesus's vine discourse (John 15:1-5) uses this same setting: the vine and branches, the abiding, the fruit-bearing. The giving of love in the vineyard anticipates Christ's self-giving that makes fruitfulness possible: 'apart from me you can do nothing.'"
            }
        ],
        "13": [
            {
                "type": "allusion",
                "target": "Matt 13:52",
                "note": "The bride has kept 'all choice fruits, both new and old' in store for the beloved — a treasury of both recent and long-stored gifts. The image echoes Jesus's parable of the householder who 'brings out of his treasure what is new and what is old' (Matt 13:52) — the scribe trained for the kingdom draws on both the old covenant treasury and the new covenant's revelation, as the bride draws on both the new season's fruit and what was long preserved."
            }
        ]
    },
    "8": {
        "1": [
            {
                "type": "allusion",
                "target": "Heb 2:11",
                "note": "The beloved's longing — 'If only you were like a brother to me' so their intimacy could be displayed publicly without shame — is fulfilled in the incarnation. Hebrews 2:11 states that Christ 'is not ashamed to call them brothers,' the very shame-concern the beloved raises being precisely what the Son's identification with humanity resolves. The longing for unveiled, unashamed intimacy between bride and beloved is answered when the Word became flesh and dwelt among us."
            }
        ],
        "5": [
            {
                "type": "allusion",
                "target": "Hos 2:14-15",
                "note": "The beloved 'coming up from the wilderness, leaning on her beloved' echoes Israel's wilderness journey as the paradigm of covenant intimacy: Hosea 2:14-15 promises YHWH will again bring Israel into the wilderness and speak tenderly to her, turning the Valley of Trouble into a door of hope. The Song's image of the bride leaning on her beloved in the wilderness is the fulfilled picture of that covenant renewal — dependence on the beloved in the wilderness is the posture of covenant love."
            },
            {
                "type": "allusion",
                "target": "Rev 12:6",
                "note": "The woman 'coming up from the wilderness' anticipates Revelation's vision of the woman who flees into the wilderness where she is nourished (Rev 12:6, 14) — the church sustained through the wilderness of persecution, leaning on Christ as the bride leans on her beloved. The wilderness journey becomes the context for divine provision and protection, not abandonment."
            }
        ],
        "7": [
            {
                "type": "allusion",
                "target": "Rom 8:38-39",
                "note": "The declaration that 'many waters cannot quench love, and rivers cannot drown it' is fulfilled in Paul's Christological claim that nothing in all creation 'shall be able to separate us from the love of God in Christ Jesus our Lord' (Rom 8:38-39). The Song's hyperbole — not even floods can extinguish this love — becomes literally true in Christ's resurrection: the waters of death itself could not drown the love that is God's own nature."
            }
        ],
        "14": [
            {
                "type": "allusion",
                "target": "Rev 22:20",
                "note": "The Song's final word — 'Make haste, my beloved, and be like a gazelle or a young stag upon the mountains of spices' — is the bride's urgent cry for the bridegroom's return. Revelation's final word is the same eschatological longing: 'Come, Lord Jesus' (Rev 22:20, Maranatha). The Song of Songs ends where the entire biblical canon ends — with the bride calling for the bridegroom to hasten his return. What the Song expresses as intimate longing, the NT expresses as eschatological expectation."
            }
        ]
    }
}

def main():
    existing = load_echo('songofsolomon')
    merge_echo(existing, SONGOFSOLOMON_ECHOES)
    save_echo('songofsolomon', existing)
    print('Song of Solomon 7-8 echoes written.')

if __name__ == '__main__':
    main()
