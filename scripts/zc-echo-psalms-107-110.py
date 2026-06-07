"""
MKT Echo Layer -- Psalms chapters 107-110
Run: python3 scripts/zc-echo-psalms-107-110.py

Psalm 107: Great psalm of rescue. v9->Luke 1:53 (Magnificat); v10/14->Luke 1:79;
  v16->Rev 1:18 (keys of Death/Hades); v20->John 1:14 (Word sent + healed).
Psalm 108: v3->Rom 15:9 (Paul quotes for Gentile mission); v5->Phil 2:9.
Psalm 109: v8->Acts 1:20 (Peter quotes re Judas); v25->Matt 27:39 (head-wagging).
Psalm 110: Already has 10 entries -- skip.
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

ps107_v9_note = (
    "Verse 9 -- 'he satisfies the longing soul, and the hungry soul he fills with good things' -- "
    "is quoted almost verbatim in Mary's Magnificat: 'he has filled the hungry with good things, "
    "and the rich he has sent away empty' (Luke 1:53). Mary recognizes the Incarnation as the "
    "fulfillment of this psalm's promise: God's characteristic act of filling the empty-handed "
    "is enacted in the coming of Christ."
)

ps107_v10_note = (
    "Verse 10 -- 'Some sat in darkness and in the shadow of death, prisoners in affliction and in irons' -- "
    "is the condition Zechariah's Benedictus announces as ended by the coming Messiah: "
    "'to give light to those who sit in darkness and in the shadow of death' (Luke 1:79). "
    "Zechariah borrows Ps 107's language of captives-in-darkness to describe what Christ's birth "
    "inaugurates -- the divine rescue the psalm celebrates."
)

ps107_v16_note = (
    "Verse 16 -- 'he shatters the doors of bronze and cuts in two the bars of iron' -- "
    "describes God breaking the barriers that imprison his people. Rev 1:18 applies this to the "
    "risen Christ: 'I have the keys of Death and Hades.' The shattering of prison-doors Ps 107 "
    "celebrates becomes in Revelation the authority over death itself -- Christ holds what God "
    "in the psalm wields."
)

ps107_v20_note = (
    "Verse 20 -- 'He sent out his word and healed them, and delivered them from their destruction' -- "
    "describes God's healing word as the agent of rescue. John 1:14 identifies that Word as a person: "
    "'the Word became flesh and dwelt among us.' The word God sent to heal in Ps 107 is the same "
    "Word that the Incarnation sends in person; Jesus' healings ('say the word, and my servant will "
    "be healed,' Luke 7:7) are the embodied form of what the psalm describes."
)

ps108_v3_note = (
    "Verse 3 -- 'I will give thanks to you, O LORD, among the peoples; I will sing praises to you "
    "among the nations' -- is part of the catena of OT texts Paul assembles in Rom 15:9-12 to prove "
    "that Christ's mission always included the Gentiles. Paul introduces the quote with 'as it is "
    "written,' making this verse one of his explicit proof-texts that the inclusion of the nations "
    "in God's praise was planned, not an afterthought."
)

ps108_v5_note = (
    "Verse 5 -- 'Be exalted, O God, above the heavens! Let your glory be over all the earth' -- "
    "is a doxological prayer for universal divine exaltation. Phil 2:9 reports its fulfillment "
    "christologically: 'God has highly exalted him and bestowed on him the name that is above every "
    "name.' The prayer for God's exaltation above the heavens is answered in the resurrection "
    "and ascension of the Son."
)

ps109_v8_note = (
    "Verse 8 -- 'May his days be few; may another take his office' -- is directly quoted by Peter "
    "in Acts 1:20 to justify replacing Judas: 'Let another take his office.' Peter reads the "
    "imprecatory language as prophetically applicable to Judas, whose betrayal of Jesus fulfills "
    "the role of the treacherous enemy the psalm curses -- and whose vacancy in the Twelve "
    "must be filled before Pentecost."
)

ps109_v25_note = (
    "Verse 25 -- 'I am an object of scorn to my accusers; when they see me, they wag their heads' -- "
    "is the gesture of contempt at the sufferer. Matt 27:39 records it at the crucifixion: "
    "'those who passed by derided him, wagging their heads.' The same physical gesture of "
    "contemptuous head-shaking that the psalmist endures is inflicted on Christ at Golgotha, "
    "placing Ps 109's righteous sufferer within the passion narrative."
)

PSALMS_ECHOES = {
    "107": {
        "9":  [{"type": "quote",    "target": "Luke 1:53",  "note": ps107_v9_note}],
        "10": [{"type": "allusion", "target": "Luke 1:79",  "note": ps107_v10_note}],
        "16": [{"type": "allusion", "target": "Rev 1:18",   "note": ps107_v16_note}],
        "20": [{"type": "allusion", "target": "John 1:14",  "note": ps107_v20_note}],
    },
    "108": {
        "3": [{"type": "quote",  "target": "Rom 15:9", "note": ps108_v3_note}],
        "5": [{"type": "theme",  "target": "Phil 2:9", "note": ps108_v5_note}],
    },
    "109": {
        "8":  [{"type": "quote",    "target": "Acts 1:20",  "note": ps109_v8_note}],
        "25": [{"type": "allusion", "target": "Matt 27:39", "note": ps109_v25_note}],
    },
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 107-110 echoes written.')

if __name__ == '__main__':
    main()
