"""
MKT Echo Layer -- Psalm 119
Run: python3 scripts/zc-echo-psalms-119-119.py

Psalm 119: The great Torah psalm (176 verses, 22 sections, one per Hebrew letter).
  All 8 synonyms for God's word (law, testimonies, ways, precepts, statutes,
  commandments, rules, word) run through every section. The NT identifies Christ
  himself as the Word (John 1:1) and treats Scripture as fulfilled in him.

Key connections:
  v9->Eph 5:26 (cleansing by word); v11->Col 3:16 (word dwelling richly);
  v18->Luke 24:45 (opened minds to understand Scripture);
  v89->Matt 24:35/1 Pet 1:25 (word endures forever);
  v105->John 8:12/2 Pet 1:19 (lamp and light); v160->John 17:17 (word is truth);
  v165->John 14:27 (peace of not stumbling); v176->1 Pet 2:25 (straying sheep returned).
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

ps119_v9_note = (
    "Verse 9 -- 'How can a young man keep his way pure? By guarding it according to your word' -- "
    "names the sanctifying power of God's word. Eph 5:26 applies this to Christ's work for the "
    "church: 'having cleansed her by the washing of water with the word.' The psalm's answer to "
    "the purity question is fulfilled when Christ himself, the living Word, accomplishes what the "
    "written word points to."
)

ps119_v11_note = (
    "Verse 11 -- 'I have stored up your word in my heart, that I might not sin against you' -- "
    "is the psalm's description of the internalized word as moral protection. Col 3:16 expands "
    "this into the community: 'Let the word of Christ dwell in you richly.' The singular 'I' "
    "of the psalm becomes the collective 'you' of the new covenant assembly; the word that guards "
    "the individual now indwells the body of Christ."
)

ps119_v18_note = (
    "Verse 18 -- 'Open my eyes, that I may behold wondrous things out of your law' -- prays for "
    "spiritual illumination to see what the text really means. Luke 24:45 records the fulfillment "
    "in the resurrection appearance: 'Then he opened their minds to understand the Scriptures.' "
    "The prayer for opened eyes is answered by the risen Christ himself -- the interpreter of his "
    "own word -- who enables the disciples to see what had always been there."
)

ps119_v89_note = (
    "Verse 89 -- 'Forever, O LORD, your word is firmly fixed in the heavens' -- declares the "
    "permanence of divine speech. Matt 24:35 (Jesus speaking) makes this absolute: 'Heaven and "
    "earth will pass away, but my words will not pass away.' And 1 Pet 1:25 quotes Isa 40:8 to "
    "the same effect: 'the word of the Lord remains forever.' The psalm's 'fixed in the heavens' "
    "and Jesus' 'my words will not pass away' are the same claim: divine word is more permanent "
    "than creation itself."
)

ps119_v105_note = (
    "Verse 105 -- 'Your word is a lamp to my feet and a light to my path' -- is the Psalter's "
    "most famous image for the guiding function of Scripture. John 8:12 applies this to Christ "
    "personally: 'I am the light of the world. Whoever follows me will not walk in darkness.' "
    "The word that functions as lamp and light in Ps 119 is embodied in the Word-become-flesh; "
    "2 Pet 1:19 extends the image to prophecy as 'a lamp shining in a dark place' until the day "
    "dawns and the morning star (Christ) rises in their hearts."
)

ps119_v160_note = (
    "Verse 160 -- 'The sum of your word is truth' -- is the OT's most direct equation of God's "
    "word with truth. John 17:17 makes the same claim in Jesus' high-priestly prayer: 'Sanctify "
    "them in the truth; your word is truth.' The psalm's axiom becomes Jesus' petition -- and "
    "the identification of word-with-truth leads to the identification of the Word with the "
    "Truth (John 14:6: 'I am the way, and the truth, and the life')."
)

ps119_v165_note = (
    "Verse 165 -- 'Great peace have those who love your law; nothing can make them stumble' -- "
    "promises a peace rooted in God's word that creates stability. John 14:27 attributes this "
    "peace directly to Christ: 'Peace I leave with you; my peace I give to you.' Phil 4:7 names "
    "it 'the peace of God, which surpasses all understanding.' The psalm's 'great peace' from "
    "loving God's word is the same peace Christ bestows through himself, the Word made flesh."
)

ps119_v176_note = (
    "Verse 176 -- 'I have gone astray like a lost sheep; seek your servant, for I do not forget "
    "your commandments' -- closes the longest psalm with an admission of lostness and a plea to "
    "be sought. Luke 15:4-6 presents Christ as the shepherd who 'leaves the ninety-nine... and "
    "goes after the one that is lost.' 1 Pet 2:25 applies this directly: 'For you were straying "
    "like sheep, but have now returned to the Shepherd and Overseer of your souls.' Ps 119's "
    "final word is not achievement but need -- the lost sheep crying to be found, which Christ "
    "makes his defining mission."
)

PSALMS_ECHOES = {
    "119": {
        "9":   [{"type": "allusion", "target": "Eph 5:26",    "note": ps119_v9_note}],
        "11":  [{"type": "theme",    "target": "Col 3:16",    "note": ps119_v11_note}],
        "18":  [{"type": "allusion", "target": "Luke 24:45",  "note": ps119_v18_note}],
        "89":  [{"type": "allusion", "target": "Matt 24:35",  "note": ps119_v89_note}],
        "105": [{"type": "allusion", "target": "John 8:12",   "note": ps119_v105_note}],
        "160": [{"type": "allusion", "target": "John 17:17",  "note": ps119_v160_note}],
        "165": [{"type": "theme",    "target": "John 14:27",  "note": ps119_v165_note}],
        "176": [{"type": "allusion", "target": "Luke 15:4",   "note": ps119_v176_note}],
    }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalm 119 echoes written.')

if __name__ == '__main__':
    main()
