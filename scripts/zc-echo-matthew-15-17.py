"""
Echo layer — Matthew chapters 15–17 (Traditions, feeding 4000, Transfiguration)
Output: data/echoes/matthew.json (adds ch15-17)

Ch15: Clean/unclean controversy; Canaanite woman; feeding 4000.
Ch16: Yeast of Pharisees; Peter's confession; first passion prediction.
Ch17: Transfiguration; elijah; temple tax.
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
  "15": {
    "4": [
      {"type": "quote", "target": "Exod 20:12", "note": "Honor your father and mother — Jesus cites the fifth commandment as the standard the Pharisees' corban tradition violates; the Decalogue as the standard by which human tradition is judged"},
      {"type": "quote", "target": "Exod 21:17", "note": "Whoever reviles father or mother must surely die — the Mosaic law intensifies the commandment; tradition that nullifies this is declared void by Jesus"}
    ],
    "8": [
      {"type": "fulfillment", "target": "Isa 29:13", "note": "This people honors me with their lips but their heart is far from me — Isaiah's indictment of empty cultic worship is cited by Jesus as fulfilled in the Pharisees' tradition-over-Torah practice"}
    ],
    "24": [
      {"type": "allusion", "target": "Ezek 34:16", "note": "I was sent only to the lost sheep of the house of Israel — the Ezekielian mission to seek the scattered lost flock of Israel; Jesus specifies his primary mission scope before extending grace to the Canaanite woman"}
    ],
    "27": [
      {"type": "allusion", "target": "Prov 9:1-5", "note": "Even the dogs eat the crumbs from the table of their masters — wisdom's table (she has set her table, 9:2) from which others benefit; the Canaanite woman's argument: even the crumbs from the masters table are enough"}
    ]
  },
  "16": {
    "14": [
      {"type": "allusion", "target": "Deut 18:15-18", "note": "Some say John the Baptist, others Elijah, others Jeremiah or one of the prophets — the popular identification of Jesus with the eschatological prophet like Moses (Deut 18:15); the crowd correctly senses prophetic fulfillment but misidentifies who"}
    ],
    "16": [
      {"type": "allusion", "target": "Ps 2:7", "note": "You are the Christ, the Son of the living God — Peter's confession of Messianic sonship; the royal Ps 2 Son, now identified in flesh by divine revelation rather than Davidic expectation"}
    ],
    "18": [
      {"type": "allusion", "target": "Isa 22:22", "note": "I will give you the keys of the kingdom of heaven — the key of the house of David placed on Eliakim's shoulder; the authority to open and shut given by divine appointment to the steward-figure"}
    ],
    "27": [
      {"type": "fulfillment", "target": "Dan 7:13-14", "note": "The Son of Man is going to come with his angels in the glory of his Father — the Danielic coming of the Son of Man in clouds with glory and universal judgment; Jesus identifies himself with this eschatological figure"}
    ]
  },
  "17": {
    "2": [
      {"type": "allusion", "target": "Exod 34:29-35", "note": "His face shone like the sun — Moses's face shone after descending from Sinai; the Transfiguration is the Mount Sinai pattern replicated with Jesus as the one whose glory shines, surpassing Moses who reflected the divine glory"},
      {"type": "allusion", "target": "Dan 12:3", "note": "His garments became white as light — those who are wise will shine like the brightness of the sky; the eschatological radiance now revealed in anticipation on the mountain"}
    ],
    "3": [
      {"type": "type", "target": "Deut 34:5-6", "note": "Moses and Elijah appeared, talking with him — Law (Moses) and Prophets (Elijah) attend Christ as witness-figures; Matthew presents the entire OT canon as pointing to and consulting with the one it foreshadowed"}
    ],
    "5": [
      {"type": "fulfillment", "target": "Ps 2:7", "note": "This is my beloved Son with whom I am well pleased; listen to him — the Ps 2 royal sonship declaration repeated from baptism (3:17); the addition listen to him echoes Deut 18:15 (the prophet like Moses whom you shall hear)"}
    ],
    "10": [
      {"type": "fulfillment", "target": "Mal 4:5-6", "note": "Elijah must come first — the disciples ask about the scribal tradition based on Mal 4:5; Jesus confirms Elijah has already come (in John the Baptist), connecting the mission-of-Elijah to restoration before the day of the LORD"}
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
