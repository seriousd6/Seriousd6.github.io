"""
Echo layer — Matthew chapters 11–12 (John's question, Sabbath controversies, Beelzebul)
Output: data/echoes/matthew.json (adds ch11-12)

Ch11: John's question, Jesus's testimony to John, condemnation of unrepentant cities, rest.
Ch12: Sabbath controversies (grain + withered hand), Beelzebul, sign of Jonah, true family.
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
  "11": {
    "5": [
      {"type": "fulfillment", "target": "Isa 35:5-6", "note": "The blind receive their sight and the lame walk, lepers are cleansed and the deaf hear, the dead are raised — Jesus lists the exact Isaianic signs of divine salvation; the list is his answer to whether he is the Coming One"},
      {"type": "fulfillment", "target": "Isa 61:1", "note": "The poor have good news preached to them — the anointed servant's mission listed by Jesus as the evidence of his identity; the Spirit-anointed mission of Isa 61 is underway"}
    ],
    "10": [
      {"type": "fulfillment", "target": "Mal 3:1", "note": "Behold I send my messenger before your face who will prepare your way — Malachi's herald of the LORD's coming; Jesus applies this to John the Baptist as the forerunner-prophet who prepares his own coming"}
    ],
    "14": [
      {"type": "fulfillment", "target": "Mal 4:5", "note": "He is Elijah who is to come — Malachi's promise of Elijah returning before the great day of the LORD; Jesus identifies John as the fulfillment of this promise (if you are willing to accept it)"}
    ],
    "21": [
      {"type": "allusion", "target": "Jonah 3:5-6", "note": "Tyre and Sidon would have repented in sackcloth and ashes — Nineveh's repentance at Jonah's preaching is the standard; the Gentile cities shame the unresponsive Galilean towns"}
    ],
    "23": [
      {"type": "allusion", "target": "Isa 14:13-15", "note": "Will you be exalted to heaven? You will be brought down to Hades — the taunt against Babylon's pride (I will ascend to heaven / you will be brought down to Sheol); Jesus applies the Babylon-fall oracle to Capernaum"}
    ],
    "25": [
      {"type": "allusion", "target": "Ps 8:2", "note": "Hidden from the wise and revealed to little children — from the mouths of infants and nursing babies you have established strength; the divine reversal that bypasses the wise to reveal to the small"}
    ],
    "27": [
      {"type": "allusion", "target": "Dan 7:14", "note": "All things have been handed over to me by my Father — the authority given to the Son of Man; Jesus claims the Danielic universal sovereignty as the ground of his unique knowledge of and access to the Father"}
    ],
    "28": [
      {"type": "allusion", "target": "Sir 24:19-20", "note": "Come to me all who labor and are heavy laden and I will give you rest — Wisdom's invitation (Come to me, you who desire me; eat your fill of my fruits); Jesus speaks as personified Wisdom giving rest"},
      {"type": "allusion", "target": "Jer 6:16", "note": "Find rest for your souls — stand at the crossroads and ask for the ancient paths, where the good way is, and you will find rest for your souls; Jeremiah's rest-promise for those who walk the good way"}
    ],
    "29": [
      {"type": "allusion", "target": "Sir 51:23-27", "note": "Take my yoke upon you and learn from me — Sirach's call to put your neck under the yoke of wisdom; Jesus presents himself as the true Wisdom whose yoke is easy"}
    ]
  },
  "12": {
    "3": [
      {"type": "allusion", "target": "1 Sam 21:1-6", "note": "David and his companions ate the bread of the Presence — the precedent for necessity overriding Sabbath-precision; David's violation of the showbread law was justified by urgent need; Jesus appeals to the same precedent"}
    ],
    "5": [
      {"type": "allusion", "target": "Num 28:9-10", "note": "The priests in the temple profane the Sabbath and are guiltless — the Levitical law required Sabbath offerings that constituted work; cultic necessity created Sabbath exceptions; the temple itself breaks the Sabbath"},
      {"type": "allusion", "target": "Hos 6:6", "note": "I desire mercy and not sacrifice — Jesus quotes Hosea a second time (9:13 and here) as the hermeneutical key for reading the Sabbath controversy; mercy-toward-suffering trumps cultic precision"}
    ],
    "18": [
      {"type": "fulfillment", "target": "Isa 42:1-4", "note": "Behold my servant whom I have chosen, my beloved in whom my soul is well pleased — Matthew cites Isa 42:1-4 in full as the explanation for Jesus's quiet, non-public healing ministry; the servant who does not cry aloud or bruise the reed is the pattern"}
    ],
    "40": [
      {"type": "fulfillment", "target": "Jonah 1:17", "note": "As Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth — the Jonah-sign is the death-and-resurrection of Jesus; Jonah's sea-entombment as the type"}
    ],
    "41": [
      {"type": "allusion", "target": "Jonah 3:5", "note": "The men of Nineveh repented at the preaching of Jonah — the Nineveh repentance as the witness against this generation; something greater than Jonah is here, yet this generation does not repent"}
    ],
    "42": [
      {"type": "allusion", "target": "1 Kgs 10:1-10", "note": "The queen of the South came from the ends of the earth to hear the wisdom of Solomon — the Sheba queen's diligence contrasts with this generation's refusal; something greater than Solomon is here"}
    ],
    "43": [
      {"type": "allusion", "target": "Lev 16:8-10", "note": "When the unclean spirit goes out of a person through waterless places — the scapegoat driven to the wilderness (the azazel in Lev 16); the demon's waterless wandering echoes the wilderness exile of the unclean spirit-goat"}
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
