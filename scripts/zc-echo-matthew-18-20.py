"""
Echo layer — Matthew chapters 18–20 (Community discourse, marriage, riches, servanthood)
Output: data/echoes/matthew.json (adds ch18-20)

Ch18: Community discourse — the little ones, the lost sheep, discipline, forgiveness.
Ch19: Divorce, the rich young ruler, the workers in the vineyard.
Ch20: Workers in the vineyard; third passion prediction; James/John's ambition; blind Bartimaeus.
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
  "18": {
    "12": [
      {"type": "fulfillment", "target": "Ezek 34:11-12", "note": "If a man has 100 sheep and one goes astray — YHWH himself will seek the lost and scattered sheep; Jesus acts as the divine shepherd, embodying the Ezekielian rescue-mission in parable form"}
    ],
    "15": [
      {"type": "allusion", "target": "Lev 19:17-18", "note": "If your brother sins go and tell him his fault between you and him alone — the Levitical command to rebuke your neighbor, not hate him in your heart; the community discipline procedure extends the Mosaic neighbor-love command"}
    ],
    "16": [
      {"type": "quote", "target": "Deut 19:15", "note": "At the mouth of two or three witnesses every word may be confirmed — the Deuteronomic witness requirement (two or three witnesses for any charge); Jesus applies the forensic standard to community discipline"}
    ],
    "20": [
      {"type": "allusion", "target": "Prov 8:34", "note": "Where two or three are gathered in my name, there am I among them — blessed is the one who listens to me, watching daily at my gates; Wisdom present with those who gather to hear; now Jesus as the present Wisdom in the community's midst"}
    ],
    "22": [
      {"type": "allusion", "target": "Gen 4:24", "note": "Seventy times seven — Lamech's boast of 77-fold vengeance; Jesus inverts the Lamech-escalation of vengeance into unlimited forgiveness; where sin escalated to 77x vengeance, grace escalates to 77x forgiveness"}
    ]
  },
  "19": {
    "4": [
      {"type": "quote", "target": "Gen 1:27", "note": "He who created them from the beginning made them male and female — Jesus grounds the marriage-permanence argument in the creation order; the creational given precedes the Mosaic concession"},
      {"type": "quote", "target": "Gen 2:24", "note": "Therefore a man shall leave his father and mother and hold fast to his wife and the two shall become one flesh — the creation ordinance of marital union cited as the theological foundation that precedes and outranks the divorce provision"}
    ],
    "7": [
      {"type": "allusion", "target": "Deut 24:1", "note": "Moses commanded one to give a certificate of divorce — the Deuteronomic divorce provision; Jesus reframes it as a concession to hardness of heart, not a divine ideal; the creational intention (Gen 2:24) stands over the Mosaic accommodation"}
    ],
    "18": [
      {"type": "quote", "target": "Exod 20:12-16", "note": "Do not murder, do not commit adultery, do not steal, do not bear false witness, honor your father and mother — Jesus cites the Decalogue commandments to the rich young ruler as the path to life, which the man claims to have kept"}
    ],
    "19": [
      {"type": "quote", "target": "Lev 19:18", "note": "You shall love your neighbor as yourself — the Levitical love-neighbor command as the summary of the social commandments; Jesus adds it to the Decalogue recitation"}
    ],
    "28": [
      {"type": "allusion", "target": "Dan 7:9", "note": "The Son of Man will sit on his glorious throne, and you will also sit on twelve thrones judging the twelve tribes of Israel — the Ancient of Days on the throne (Dan 7:9); Jesus promises the disciples thrones in the paliggenesia, the eschatological renewal"}
    ]
  },
  "20": {
    "18": [
      {"type": "allusion", "target": "Isa 53:3", "note": "The Son of Man will be delivered to the chief priests and scribes, condemned to death, and delivered to the Gentiles — the Servant who was despised and rejected, handed over to suffering; the passion prediction echoes the Servant Song progression"}
    ],
    "28": [
      {"type": "fulfillment", "target": "Isa 53:10-11", "note": "The Son of Man came not to be served but to serve and to give his life as a ransom for many — the Servant who makes his soul an offering for sin and justifies many (Isa 53:10-11); Jesus identifies himself as the Isaiah Servant and his death as the ransom-offering"}
    ],
    "30": [
      {"type": "allusion", "target": "Ps 146:8", "note": "Two blind men crying Lord have mercy on us, Son of David — YHWH opens the eyes of the blind (Ps 146:8); the Son of David performing the divine act of sight-restoration; Davidic title and divine healing action together"}
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
