"""
Echo layer — Matthew chapters 7–8 (Sermon conclusion + miracles)
Output: data/echoes/matthew.json (adds ch7-8)

Ch7: Sermon on the Mount conclusion — golden rule, two ways, narrow gate, false prophets,
wise/foolish builders. All with extensive Torah/Wisdom echoes.
Ch8: Miracle cycle — healing, exorcism, stilling the storm. Moses/Elijah typology.
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

ECHOES = {
  "7": {
    "1": [
      {"type": "allusion", "target": "Lev 19:15", "note": "Do not judge — do not render unjust judgment; the Levitical prohibition on partiality and unjust verdict; Jesus universalizes the judicial warning to interpersonal relations"}
    ],
    "7": [
      {"type": "allusion", "target": "Prov 8:17", "note": "Ask and it will be given to you, seek and you will find, knock and it will be opened — wisdom invites those who seek her; the prayer-seek-knock triad echoes wisdom's invitation pattern"},
      {"type": "allusion", "target": "Jer 29:13", "note": "You will seek me and find me when you seek me with all your heart — the covenant promise of finding when seeking with the whole heart; Jesus applies it to prayer-access"}
    ],
    "12": [
      {"type": "fulfillment", "target": "Lev 19:18", "note": "The golden rule: whatever you wish that others would do to you, do also to them, for this is the Law and the Prophets — the love-neighbor command of Lev 19:18 as the summary of the entire Torah; Jesus names it as the fulcrum of the whole Sermon's ethical demand"}
    ],
    "13": [
      {"type": "allusion", "target": "Deut 30:15-19", "note": "Enter by the narrow gate — I set before you life and death, blessing and curse; the Deuteronomic two-ways covenant structure (life or death, choose life) is the template for the narrow/wide gate teaching"}
    ],
    "15": [
      {"type": "allusion", "target": "Ezek 22:27", "note": "Beware of false prophets who come in sheep's clothing but are ravenous wolves — Ezekiel's princes as wolves tearing the prey; the wolf-in-sheep's-clothing image in the prophetic tradition"}
    ],
    "23": [
      {"type": "allusion", "target": "Ps 6:8", "note": "Depart from me, you workers of lawlessness — the Psalmist's dismissal of evildoers; Jesus applies this Psalmic phrase to the final rejection of false miracle-workers who never knew him"}
    ],
    "24": [
      {"type": "allusion", "target": "Prov 10:25", "note": "The righteous is an everlasting foundation — the wise builder on rock echoes the Proverbs contrast between the righteous who endure (like bedrock) and the wicked who are swept away"},
      {"type": "type", "target": "Exod 19:5", "note": "The one who hears and does — the Sinai covenant demanded hearing-and-doing; the covenant-keeper who built on rock embodies the Deuteronomic shema (hear and do)"}
    ]
  },
  "8": {
    "4": [
      {"type": "allusion", "target": "Lev 14:1-32", "note": "Show yourself to the priest and offer the gift Moses commanded — the Levitical cleansing ritual for leprosy; Jesus sends the healed man back into the covenant system as its testimony; he fulfills, not bypasses, Mosaic law"}
    ],
    "11": [
      {"type": "fulfillment", "target": "Isa 49:12", "note": "Many will come from east and west and recline at table with Abraham, Isaac, and Jacob — the Isaianic gathering of scattered Israel from all directions; Matthew applies it to Gentile inclusion in the kingdom-banquet"}
    ],
    "12": [
      {"type": "allusion", "target": "Dan 12:2", "note": "Outer darkness, where there is weeping and gnashing of teeth — Daniel's everlasting contempt for those who do not awaken to life; the outer darkness of exclusion from the kingdom-feast"}
    ],
    "17": [
      {"type": "fulfillment", "target": "Isa 53:4", "note": "He took our infirmities and bore our diseases — Matthew cites Isa 53:4 (the Servant's vicarious bearing) as the theological explanation for Jesus's healing ministry; the healings are not merely humanitarian acts but Servant-mission fulfillments"}
    ],
    "20": [
      {"type": "allusion", "target": "Ps 63:10", "note": "Foxes have holes and birds have nests but the Son of Man has nowhere to lay his head — the homelessness of wandering in a hostile land; the one given universal dominion (Dan 7:14) lives as a refugee in his own world"}
    ],
    "23": [
      {"type": "type", "target": "Jonah 1:4-5", "note": "A great storm arose on the sea while Jesus slept — Jonah asleep during the storm that YHWH sent; both narratives feature a great storm, a sleeping leader, terrified sailors, a miraculous calming; Jesus is the true Jonah"},
      {"type": "allusion", "target": "Ps 107:29", "note": "He made the storm be still — YHWH stills the storm and the waves; the Psalmic divine sovereignty over the sea now exercised by Jesus; the disciples ask who this is (v.27) and the Psalm answers: YHWH"}
    ],
    "27": [
      {"type": "fulfillment", "target": "Ps 107:28-29", "note": "Even the winds and the sea obey him — the Psalm of YHWH stilling the sea (he made the storm be still) is realized; the disciples perceive what the Psalm declared about God"}
    ],
    "29": [
      {"type": "allusion", "target": "Dan 7:14", "note": "What have you to do with us, Son of God? Have you come here to torment us before the time? — the demons know the Danielic eschatological schedule; the Son of Man with universal dominion will judge; their question is a Danielic question"}
    ]
  }
}

def main():
    existing = load_echo('matthew')
    merge_echo(existing, ECHOES)
    save_echo('matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
