"""
MKT Echo Layer -- Psalms chapters 147-150
Run: python3 scripts/zc-echo-psalms-147-150.py

Psalm 147: Praise for God's rebuilding + his word going forth. v3->Luke 4:18 (bind
  brokenhearted); v4->Matt 10:30 (stars numbered); v15->Heb 4:12 (word runs swiftly).
Psalm 148: Universal cosmic praise. v5->John 1:3 (all things created by his command);
  v14 horn-raised->Luke 1:69 (Benedictus direct quote: horn of salvation).
Psalm 149: New song for the King. v1->Rev 5:9 (new song); v6 two-edged-sword->Heb 4:12.
Psalm 150: Grand doxological finale. v2->Rev 15:3 (great deeds); v6 everything-that-
  breathes->Phil 2:10-11/Rev 5:13.
This completes Psalms echo (150/150 chapters).
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
    "147": {
        "3": [
            {
                "type": "allusion",
                "target": "Luke 4:18",
                "note": (
                    "Verse 3 -- 'He heals the brokenhearted and binds up their wounds' -- is the "
                    "divine care that Jesus announces as his own agenda at the Nazareth synagogue "
                    "(Luke 4:18, quoting Isa 61:1: 'he has sent me to bind up the brokenhearted'). "
                    "The Psalmist's praise of God's therapeutic compassion is the OT register "
                    "Christ claims for himself at the opening of his public ministry. Rev 21:4 is "
                    "the eschatological completion: God 'will wipe every tear from their eyes.'"
                )
            }
        ],
        "4": [
            {
                "type": "theme",
                "target": "Matt 10:30",
                "note": (
                    "Verse 4 -- 'He determines the number of the stars; he gives to all of them "
                    "their names' -- celebrates the God who numbers and names an uncountable "
                    "multitude. Matt 10:30 applies this same precise divine knowledge to each "
                    "person: 'even the hairs of your head are all numbered.' The God who knows "
                    "every star by name knows every disciple with even greater intimacy -- "
                    "the psalmist's cosmic doxology becomes Jesus' ground for individual confidence."
                )
            }
        ],
        "15": [
            {
                "type": "theme",
                "target": "Heb 4:12",
                "note": (
                    "Verse 15 -- 'He sends out his command to the earth; his word runs swiftly' -- "
                    "describes God's word as swift, active, and effective in the world. Heb 4:12 "
                    "develops this: 'the word of God is living and active, sharper than any "
                    "two-edged sword.' 2 Thess 3:1 picks up the same speed-imagery: 'pray that "
                    "the word of the Lord may speed ahead and be honored.' The swift running word "
                    "of Ps 147 is identified in the NT as Jesus himself (John 1:1) and the Gospel "
                    "proclamation that spreads rapidly through the world."
                )
            }
        ]
    },
    "148": {
        "5": [
            {
                "type": "allusion",
                "target": "John 1:3",
                "note": (
                    "Verse 5 -- 'Let them praise the name of the LORD! For he commanded and they "
                    "were created' -- grounds universal praise in creation by divine fiat. John 1:3 "
                    "identifies the agent of that commanding word as the pre-incarnate Christ: "
                    "'All things were made through him, and without him was not any thing made "
                    "that was made.' Col 1:16 confirms: 'all things were created through him and "
                    "for him.' Ps 148's praise to the Creator is praise to the one who became "
                    "incarnate."
                )
            }
        ],
        "14": [
            {
                "type": "fulfillment",
                "target": "Luke 1:69",
                "note": (
                    "Verse 14 -- 'He has raised up a horn for his people, praise for all his "
                    "saints, for the people of Israel who are near to him' -- uses the horn "
                    "as a symbol of restored strength. Luke 1:69 directly fulfills this when "
                    "Zechariah sings: 'he has raised up a horn of salvation for us in the house "
                    "of his servant David.' The Benedictus explicitly echoes Ps 148:14 to "
                    "interpret the birth of the Messiah as God's long-awaited act of raising "
                    "the horn of his people."
                )
            }
        ]
    },
    "149": {
        "1": [
            {
                "type": "allusion",
                "target": "Rev 5:9",
                "note": (
                    "Verse 1 -- 'Sing to the LORD a new song, his praise in the assembly of the "
                    "godly!' -- calls for the new song that anticipates something new God has done. "
                    "Rev 5:9 presents its fulfillment: the four living creatures and elders 'sang "
                    "a new song, saying, Worthy are you to take the scroll and to open its seals, "
                    "for you were slain.' The new song Ps 149 anticipates is the song of the "
                    "redeemed before the Lamb -- creation's response to the new exodus "
                    "accomplished by Christ's death and resurrection."
                )
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Heb 4:12",
                "note": (
                    "Verse 6 -- 'Let the high praises of God be in their throats and two-edged "
                    "swords in their hands' -- pairs worship with the sword as the equipment of "
                    "God's people. Heb 4:12 identifies the word of God as 'sharper than any "
                    "two-edged sword.' Rev 19:15 presents Christ himself as the warrior whose "
                    "weapon is the word from his mouth. The saints' two-edged sword becomes "
                    "in the NT the word proclaimed and the word wielded by Christ -- the "
                    "battle is fought with truth, not with steel."
                )
            }
        ]
    },
    "150": {
        "2": [
            {
                "type": "theme",
                "target": "Rev 15:3",
                "note": (
                    "Verse 2 -- 'Praise him for his mighty acts; praise him according to his "
                    "excellent greatness' -- is the ground of all doxology: God's deeds and "
                    "character. Rev 15:3 is the heavenly fulfillment: 'Great and amazing are "
                    "your deeds, O Lord God the Almighty! Just and true are your ways, O King "
                    "of the nations!' The praise Ps 150 calls for is the praise the redeemed "
                    "and victorious sing before the throne -- the Psalter's final call answered "
                    "in the ultimate congregation."
                )
            }
        ],
        "6": [
            {
                "type": "fulfillment",
                "target": "Rev 5:13",
                "note": (
                    "Verse 6 -- 'Let everything that has breath praise the LORD! Praise the "
                    "LORD!' -- is the Psalter's ultimate doxological word: every breathing "
                    "creature enlisted in praise. Rev 5:13 presents the eschatological "
                    "fulfillment: 'And I heard every creature in heaven and on earth and under "
                    "the earth and in the sea, and all that is in them, saying, To him who sits "
                    "on the throne and to the Lamb be blessing and honor and glory and might "
                    "forever and ever!' Phil 2:10-11 arrives at the same universal scope "
                    "through Christ's exaltation. The Psalter's final word -- everything that "
                    "breathes, praise! -- is the exact scope of Christ's cosmic lordship."
                )
            }
        ]
    }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 147-150 echoes written -- Psalms echo layer complete!')

if __name__ == '__main__':
    main()
