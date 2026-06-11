"""
echo | leviticus | ch 13
Focused echo layer for the tzara'at (skin disease) diagnosis laws.
Key connections: priestly "unclean" pronouncement reversed by Jesus (Matt 8:3);
leper's exclusion posture (v.45-46) → Heb 13:12 (outside the camp); Isa 53:3
(suffering servant as social outcast); clean garment → Rev 7:14.
Run: python3 scripts/zc-echo-leviticus-13-13.py
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

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

LEVITICUS_ECHOES = {
  "13": {
    "3": [
      {"type": "typology", "target": "Matt 8:3",
       "note": "The priest examines the afflicted person and pronounces him unclean — the Levitical diagnosis system gave priests authority to declare the state of a person before God and community; Jesus reverses this protocol entirely: he touches the leper (making himself ritually exposed) and pronounces him clean, inverting the priestly role from diagnostician of uncleanness to restorer of cleanness"}
    ],
    "45": [
      {"type": "fulfillment", "target": "Luke 5:12",
       "note": "Torn clothes, loose hair, covered upper lip, and the cry 'Unclean! Unclean!' — this is the exact posture and cry of the leper in Luke 5:12 (full of leprosy, he fell on his face before Jesus); the gospel leper embodies Leviticus 13:45 precisely; Luke's detail 'full of leprosy' reflects the chronic/total case of vv. 12-13; Jesus's 'Be clean' is the judicial reversal of the priestly declaration this chapter prescribes"},
      {"type": "typology", "target": "Isa 53:3",
       "note": "The leper's marks — social exclusion, rejection, people hiding their faces — are the social reality of the suffering servant: he was despised and rejected, a man of sorrows, as one from whom men hide their faces; Isaiah pictures the servant as taking on the condition of the ritually impure outcast; Christ bears the status Leviticus 13 assigns to the unclean"}
    ],
    "46": [
      {"type": "allusion", "target": "Heb 13:12",
       "note": "He must live apart — his dwelling place shall be outside the camp: Hebrews 13:11-12 makes the outside-the-camp location of Leviticus 13 a type of the crucifixion: the bodies of animals whose blood was brought into the holy place were burned outside the camp; Jesus also suffered outside the gate to sanctify the people through his own blood; the leper's forced exile is the type of Christ's voluntary exile into shame and exclusion"}
    ],
    "58": [
      {"type": "allusion", "target": "Rev 7:14",
       "note": "The garment washed and from which the mark departs is clean again — the garment-cleansing protocol (vv. 47-59) is a type of the eschatological purification of the saints: those who have washed their robes and made them white in the blood of the Lamb (Rev 7:14); the repeated washing and re-examination in Leviticus 13 points toward the final cleansing that only the Lamb's blood accomplishes permanently"}
    ]
  }
}

def main():
    e = load_echo('leviticus')
    merge_echo(e, LEVITICUS_ECHOES)
    save_echo('leviticus', e)

if __name__ == '__main__':
    main()
