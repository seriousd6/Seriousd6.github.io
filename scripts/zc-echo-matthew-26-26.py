"""
Echo layer — Matthew chapter 26 (Passion begins: anointing, Passover, Gethsemane, arrest)
Output: data/echoes/matthew.json (adds ch26)
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
  "26": {
    "15": [
      {"type": "fulfillment", "target": "Zech 11:12", "note": "They paid him thirty pieces of silver — Zechariah weighs out thirty shekels, the price at which he was valued; Matthew presents the betrayal price as fulfillment of the shepherd-rejected oracle"}
    ],
    "24": [
      {"type": "fulfillment", "target": "Isa 53:3", "note": "The Son of Man goes as it is written of him — the Servant's path of rejection and suffering was written; the passion narrative is narrated as the fulfillment of the Servant Song"}
    ],
    "26": [
      {"type": "fulfillment", "target": "Exod 12:14-20", "note": "As they were eating, Jesus took bread — the Last Supper is explicitly a Passover meal; the bread and cup are reinterpreted from the Exodus Passover elements to the new Passover of Christ's body and blood"},
      {"type": "shadow", "target": "Jer 31:31-34", "note": "This is my blood of the covenant — the new covenant in my blood; the Jeremianic new covenant promise now enacted at the table with the body and blood of Jesus"}
    ],
    "28": [
      {"type": "fulfillment", "target": "Jer 31:31-34", "note": "My blood of the covenant which is poured out for many for the forgiveness of sins — the new covenant ratified by blood, and the forgiveness of sins promised in Jer 31:34 (I will forgive their iniquity) now enacted in the cup"}
    ],
    "31": [
      {"type": "fulfillment", "target": "Zech 13:7", "note": "Strike the shepherd and the sheep will be scattered — Jesus cites Zech 13:7 as predicting the disciples scattering at his arrest; the shepherd struck by YHWH and the flock scattered is the passion pattern"}
    ],
    "38": [
      {"type": "allusion", "target": "Ps 42:5-6", "note": "My soul is very sorrowful, even to death — the Psalmist whose soul is cast down (Ps 42:5); Jesus in Gethsemane experiencing the full weight of the impending cross in the language of the Psalms of descent"}
    ],
    "39": [
      {"type": "allusion", "target": "Ps 22:1", "note": "Let this cup pass from me, nevertheless not as I will but as you will — the cry of the one abandoned (Ps 22:1) already anticipated; the submission to the Father in Gethsemane is the voluntary embrace of the cup that Ps 22 will narrate"},
      {"type": "allusion", "target": "Isa 51:17-22", "note": "The cup of staggering — YHWH takes from Jerusalem the cup of his wrath and puts it in the hand of her tormentors; Jesus voluntarily takes the cup of divine wrath that Israel could not bear"}
    ],
    "64": [
      {"type": "fulfillment", "target": "Dan 7:13", "note": "You will see the Son of Man seated at the right hand of Power and coming on the clouds of heaven — Jesus combines Ps 110:1 (seated at the right hand) with Dan 7:13 (coming on clouds) in his response to the high priest; the answer that condemns him is the Christological claim"},
      {"type": "fulfillment", "target": "Ps 110:1", "note": "The Son of Man seated at the right hand of Power — Ps 110:1 (sit at my right hand) applied to the exalted Christ; the humiliation before Caiaphas will end in the heavenly enthronement"}
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
