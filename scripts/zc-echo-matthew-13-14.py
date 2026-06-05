"""
Echo layer — Matthew chapters 13–14 (Parables discourse + miracle section)
Output: data/echoes/matthew.json (adds ch13-14)

Ch13: Kingdom parables (sower, weeds, mustard, leaven, treasure, pearl, net).
Ch14: John the Baptist's death, feeding the 5000, water-walking.
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
  "13": {
    "14": [
      {"type": "fulfillment", "target": "Isa 6:9-10", "note": "You will indeed hear but never understand, see but never perceive — Isaiah's hardening commission is cited by Jesus as fulfilled in the parable-audience; the mystery of divine judgment through non-understanding"}
    ],
    "24": [
      {"type": "allusion", "target": "Gen 1:11-12", "note": "The parable of the weeds: a man sowed good seed in his field — the creation-language (seed producing according to its kind) grounds the parable; the kingdom-field is God's good creation into which an enemy introduced corruption"}
    ],
    "31": [
      {"type": "allusion", "target": "Ezek 17:22-24", "note": "The mustard seed that grows into a tree where birds nest — Ezekiel's cedar planted by YHWH that becomes the great tree where birds dwell; the kingdom's hidden beginning and universal scope"},
      {"type": "allusion", "target": "Dan 4:12", "note": "The great tree where birds of heaven nest in its branches — Nebuchadnezzar's tree-dream; the universal empire as a sheltering tree; the kingdom of heaven supersedes all earthly empires with a greater shelter"}
    ],
    "33": [
      {"type": "allusion", "target": "Exod 12:15", "note": "The leaven hidden in three measures of flour — the Passover instruction to remove leaven from the house; Jesus uses leaven positively (kingdom permeation), inverting the negative use, to show the kingdom's penetrating hidden growth"}
    ],
    "35": [
      {"type": "fulfillment", "target": "Ps 78:2", "note": "I will open my mouth in parables, I will utter what has been hidden since the foundation of the world — Matthew cites Ps 78:2 as fulfilled in Jesus's parable-teaching; the Asaph psalm of hidden-and-revealed salvation history"}
    ],
    "43": [
      {"type": "allusion", "target": "Dan 12:3", "note": "Then the righteous will shine like the sun in the kingdom of their Father — the wise who shine like the brightness of the sky; the eschatological glorification of the righteous at the harvest"}
    ],
    "47": [
      {"type": "allusion", "target": "Ezek 47:10", "note": "The parable of the net cast into the sea gathering fish of every kind — Ezekiel's vision of fishermen at the Dead Sea after the river of life; the eschatological gathering and sorting of all peoples"}
    ]
  },
  "14": {
    "3": [
      {"type": "type", "target": "1 Kgs 19:1-3", "note": "Herod arrested John because of Herodias — Herod Antipas / Herodias echoes Ahab / Jezebel; the righteous prophet arrested and threatened by the wicked king and his wife; the prophetic-persecution pattern recurring"}
    ],
    "19": [
      {"type": "type", "target": "Exod 16:14-15", "note": "He took the five loaves and two fish, looked up to heaven, blessed and broke and gave — the manna provision in the wilderness; Jesus feeds the crowd in the wilderness with miraculous bread, as YHWH fed Israel with manna"},
      {"type": "allusion", "target": "2 Kgs 4:42-44", "note": "Elisha fed 100 men with 20 loaves and there was some left over — the Elisha-feeding miracle as a type; Jesus feeds 5000 from 5 loaves with 12 basketfuls remaining, vastly exceeding the type"}
    ],
    "25": [
      {"type": "allusion", "target": "Job 9:8", "note": "He came to them walking on the sea — who tramples the waves of the sea (Job 9:8, YHWH); the divine prerogative of walking on water; Matthew's account presents Jesus doing what only YHWH can do"},
      {"type": "allusion", "target": "Ps 77:19", "note": "Your way was through the sea, your path through the great waters — YHWH's Exodus path through the sea; Jesus walking on the sea performs the Exodus-path as the divine act"}
    ],
    "33": [
      {"type": "allusion", "target": "Ps 2:12", "note": "Truly you are the Son of God — the disciples worship Jesus; the royal sonship of Ps 2 is recognized by the boat-community; the Gentile-inclusive tone of Matthew's Christology emerges at each divine revelation"}
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
