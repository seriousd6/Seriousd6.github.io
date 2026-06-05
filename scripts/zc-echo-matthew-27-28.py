"""
Echo layer — Matthew chapters 27–28 (Crucifixion + Resurrection)
Output: data/echoes/matthew.json (adds ch27-28)

Ch27: Trial before Pilate, crucifixion, death, burial.
Ch28: Resurrection, great commission.
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
  "27": {
    "9": [
      {"type": "fulfillment", "target": "Zech 11:12-13", "note": "They took the thirty pieces of silver and bought the potter's field — Matthew attributes to Jeremiah (combining Jer 32:6-9 + Zech 11:12-13); the silver thrown into the temple, used to buy the potter's field, fulfills the shepherd-wage-despised oracle"}
    ],
    "34": [
      {"type": "allusion", "target": "Ps 69:21", "note": "They offered him wine mixed with gall — they gave me poison for food, and for my thirst they gave me sour wine; the crucifixion details draw from the Psalms of the righteous sufferer"}
    ],
    "35": [
      {"type": "fulfillment", "target": "Ps 22:18", "note": "They divided his garments among them by casting lots — Ps 22:18 (they divided my garments among them, and for my clothing they cast lots); the crucifixion details are narrated as Psalm fulfillment"}
    ],
    "39": [
      {"type": "fulfillment", "target": "Ps 22:7", "note": "Those who passed by derided him, wagging their heads — all who see me mock me; they make mouths at me, they wag their heads (Ps 22:7); the crucifixion mockery as Psalm fulfillment"}
    ],
    "43": [
      {"type": "fulfillment", "target": "Ps 22:8", "note": "He trusts in God; let God deliver him — he trusts in the LORD; let him deliver him (Ps 22:8); the chief priests' taunt echoes the Psalmist's tormentors' taunt, fulfilling the Ps 22 passion narrative"}
    ],
    "46": [
      {"type": "fulfillment", "target": "Ps 22:1", "note": "My God, my God, why have you forsaken me — Jesus quotes Ps 22:1 from the cross; the cry of dereliction is the opening of the great Passion Psalm; the entire Psalm is being enacted and prayed"}
    ],
    "51": [
      {"type": "fulfillment", "target": "Exod 26:31-33", "note": "The curtain of the temple was torn in two from top to bottom — the veil separating the holy of holies is destroyed; the barrier between humanity and divine presence is removed by the death of Christ"},
      {"type": "allusion", "target": "Ezek 37:12-13", "note": "The tombs were opened and many bodies of the saints who had fallen asleep were raised — the valley of dry bones vision of resurrection; the opened graves in Jerusalem at the crucifixion are a foretaste of the general resurrection"}
    ],
    "57": [
      {"type": "allusion", "target": "Isa 53:9", "note": "A rich man from Arimathea named Joseph — they made his grave with the wicked and with a rich man in his death (Isa 53:9); the burial by a rich man fulfills the Servant Song detail"}
    ]
  },
  "28": {
    "6": [
      {"type": "fulfillment", "target": "Ps 16:10", "note": "He is not here, for he has risen — you will not abandon my soul to Sheol or let your holy one see corruption (Ps 16:10); the empty tomb is the fulfillment of the Davidic Psalm that Acts 2:27-31 identifies as resurrection prophecy"}
    ],
    "18": [
      {"type": "fulfillment", "target": "Dan 7:14", "note": "All authority in heaven and on earth has been given to me — the dominion and glory and kingdom given to the Son of Man; the Great Commission is grounded in the Danielic enthronement; Jesus claims the universal authority of the vindicated Son of Man"}
    ],
    "19": [
      {"type": "fulfillment", "target": "Gen 12:3", "note": "Make disciples of all nations — in you all the families of the earth shall be blessed; the Abrahamic promise of universal blessing reaches its fulfillment in the mission to all nations grounded in Christ's authority"}
    ],
    "20": [
      {"type": "fulfillment", "target": "Isa 7:14", "note": "I am with you always, to the end of the age — Immanuel (God with us, Isa 7:14); Matthew closes the Gospel where it opened: the presence of God-with-us is now the permanent promise of the risen Christ who sends his community to the nations"}
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
