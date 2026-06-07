"""
MKT Echo Layer -- Psalms chapters 134-139
Run: python3 scripts/zc-echo-psalms-134-139.py

Psalm 134 (3v): closing Song of Ascents; v2 lifted hands->1 Tim 2:8.
Psalm 135: v14->Heb 10:30 (DIRECT QUOTE: Lord will judge his people).
Psalm 136: 26x refrain 'steadfast love endures forever'; v26->Rev 11:13 (God of heaven).
Psalm 137: Babylon lament; v8 recompense->Rev 18:6 (Babylon judgment language).
Psalm 138: v8 Lord-fulfills-purpose->Phil 1:6 (he who began good work will complete it).
Psalm 139: Omnipresence psalm; v7-8->Rom 8:38-39; v13->Gal 1:15/Luke 1:41;
  v16->Rev 20:12/Phil 4:3; v23-24->Heb 4:12-13.
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

PSALMS_ECHOES = {
    "134": {
        "2": [
            {
                "type": "theme",
                "target": "1 Tim 2:8",
                "note": (
                    "Verse 2 -- 'Lift up your hands to the holy place and bless the LORD' -- "
                    "is the posture of temple worship carried into the NT in 1 Tim 2:8: 'I desire "
                    "that in every place the men should pray, lifting holy hands without anger or "
                    "quarreling.' The gesture that marks priestly worship before God in the Jerusalem "
                    "sanctuary is transferred to every place of Christian assembly, since through "
                    "Christ all believers have direct access to the holy place (Heb 10:19-22)."
                )
            }
        ]
    },
    "135": {
        "14": [
            {
                "type": "quote",
                "target": "Heb 10:30",
                "note": (
                    "Verse 14 -- 'the LORD will vindicate his people and have compassion on his "
                    "servants' -- is directly quoted in Heb 10:30: 'The Lord will judge his people.' "
                    "The author places it alongside Deut 32:35 ('Vengeance is mine, I will repay') "
                    "as a warning against apostasy: the God who vindicates his people also judges "
                    "those who treat his blood covenant with contempt. The psalm's comfort becomes "
                    "Hebrews' solemn warning within the same divine character."
                )
            }
        ]
    },
    "136": {
        "1": [
            {
                "type": "theme",
                "target": "Rev 7:12",
                "note": (
                    "Psalm 136 is built entirely around the antiphonal refrain 'for his steadfast "
                    "love endures forever' (repeated 26 times). Rev 7:12 takes up this Psalter "
                    "pattern in the heavenly worship: 'blessing and glory and wisdom and thanksgiving "
                    "and honor and power and might be to our God forever and ever.' The unending "
                    "quality the psalm asserts about God's love -- forever, forever, forever -- "
                    "becomes the quality of the worship Christ's redemption evokes in heaven."
                )
            }
        ],
        "26": [
            {
                "type": "allusion",
                "target": "Rev 11:13",
                "note": (
                    "Verse 26 -- 'Give thanks to the God of heaven, for his steadfast love endures "
                    "forever' -- concludes Ps 136 with a universal doxology to the heavenly sovereign. "
                    "Rev 11:13 echoes this title in the earthquake aftermath: 'the rest were terrified "
                    "and gave glory to the God of heaven.' The title God of heaven, used for the God "
                    "who rules all nations, is the name acknowledged even by those who feared, not "
                    "yet loved -- the psalm's praise becoming the world's forced recognition."
                )
            }
        ]
    },
    "137": {
        "1": [
            {
                "type": "allusion",
                "target": "Rev 18:2",
                "note": (
                    "Verse 1 -- 'By the rivers of Babylon -- there we sat down and wept, when we "
                    "remembered Zion' -- establishes Babylon as the anti-Zion, the place of exile "
                    "and lament. Rev 18:2 takes up the Babylon symbol for the world-system opposed "
                    "to God: 'Fallen, fallen is Babylon the great!' The grief of Ps 137 beside "
                    "the rivers of Babylon becomes in Revelation the announcement of Babylon's fall -- "
                    "the exile is over, the exiles vindicated."
                )
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "Rev 18:6",
                "note": (
                    "Verse 8 -- 'O daughter of Babylon, doomed to be destroyed, blessed shall he be "
                    "who repays you with what you have done to us' -- invokes the law of recompense "
                    "against Babylon. Rev 18:6 uses identical language for the eschatological "
                    "judgment: 'Pay her back as she herself has paid back others, and repay her "
                    "double for her deeds.' Revelation is consciously drawing on Ps 137's "
                    "vindication-language to frame the final judgment of the anti-God world-system."
                )
            }
        ]
    },
    "138": {
        "2": [
            {
                "type": "theme",
                "target": "John 1:14",
                "note": (
                    "Verse 2 -- 'you have exalted above all things your name and your word' -- "
                    "declares that God's word shares the honor of the divine name. John 1:14 "
                    "identifies that word as a person: 'the Word became flesh and dwelt among us.' "
                    "What the psalm celebrates as the supreme dignity of divine speech, the Prologue "
                    "presents as the act of Incarnation -- the Word exalted above all things "
                    "becomes the Word who stoops to dwell among us."
                )
            }
        ],
        "8": [
            {
                "type": "allusion",
                "target": "Phil 1:6",
                "note": (
                    "Verse 8 -- 'The LORD will fulfill his purpose for me; your steadfast love, "
                    "O LORD, endures forever. Do not forsake the works of your hands' -- is a prayer "
                    "that God will complete what he began. Phil 1:6 makes this an apostolic "
                    "confidence: 'he who began a good work in you will bring it to completion at "
                    "the day of Jesus Christ.' The psalmist's plea becomes Paul's certainty -- "
                    "grounded in Christ's resurrection, which is the pledge that God does not "
                    "abandon the works of his hands."
                )
            }
        ]
    },
    "139": {
        "7": [
            {
                "type": "theme",
                "target": "Rom 8:38",
                "note": (
                    "Verses 7-8 -- 'Where shall I go from your Spirit? Or where shall I flee from "
                    "your presence? If I ascend to heaven, you are there! If I make my bed in "
                    "Sheol, you are there!' -- map the complete impossibility of escaping God's "
                    "presence. Rom 8:38-39 applies this as Gospel confidence: neither death nor "
                    "life, neither heights nor depths, can separate us from the love of God in "
                    "Christ Jesus. The omnipresence that might terrify becomes, through Christ, "
                    "the guarantee that nothing can undo God's claim on his people."
                )
            }
        ],
        "13": [
            {
                "type": "allusion",
                "target": "Gal 1:15",
                "note": (
                    "Verse 13 -- 'you formed my inward parts; you knitted me together in my "
                    "mother's womb' -- grounds human identity in divine creative action before "
                    "birth. Gal 1:15 applies the same framework to Paul's calling: 'he who had "
                    "set me apart before I was born and who called me by his grace.' Luke 1:41 "
                    "shows John the Baptist, still in the womb, recognizing the presence of "
                    "Christ. Ps 139's prenatal theology of divine knowledge and formation "
                    "underlies the NT's account of vocation before birth."
                )
            }
        ],
        "16": [
            {
                "type": "allusion",
                "target": "Rev 20:12",
                "note": (
                    "Verse 16 -- 'in your book were written, every one of them, the days that "
                    "were formed for me, when as yet there was none of them' -- introduces the "
                    "image of God's book in which human lives are written before birth. Rev 20:12 "
                    "extends this: 'the books were opened... and the dead were judged by what "
                    "was written in the books.' Phil 4:3 speaks of names 'written in the book "
                    "of life.' The book of Ps 139 -- the record of a life known to God before "
                    "it began -- becomes the eschatological register of those who belong to God."
                )
            }
        ],
        "23": [
            {
                "type": "allusion",
                "target": "Heb 4:12",
                "note": (
                    "Verses 23-24 -- 'Search me, O God, and know my heart! Try me and know my "
                    "thoughts! And see if there be any grievous way in me, and lead me in the "
                    "way everlasting' -- invite exactly the divine penetration of the self that "
                    "Heb 4:12-13 attributes to God's word: 'the word of God is living and active, "
                    "sharper than any two-edged sword, piercing to the division of soul and of "
                    "spirit... discerning the thoughts and intentions of the heart... no creature "
                    "is hidden from his sight.' The psalmist prays for what the word of God "
                    "in Christ inevitably does -- searches and exposes the inner life."
                )
            }
        ]
    }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 134-139 echoes written.')

if __name__ == '__main__':
    main()
