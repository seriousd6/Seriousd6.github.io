"""
MKT Echo Layer — 2 Chronicles chapters 25–28
Run: python3 scripts/zc-echo-2chronicles-25-28.py

Ch25: Individual moral accountability (25:4, citing Deut 24:16) — Rom 14:12; Ezek 18:4
Ch26: Seek God and prosper (26:5) — Matt 6:33
Ch28: Northern Israelites clothe and return Judahite captives (28:15) — proto-Good Samaritan; Luke 10:33
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

ECHOES = {
  "25": {
    "4": [
      {"type": "allusion", "target": "Rom 14:12", "note": "Amaziah did not execute the children of his father's killers, citing the law of Moses: 'the fathers shall not die for the children, neither shall the children die for the fathers, but every man shall die for his own sin' (citing Deut 24:16). This principle of individual moral accountability runs through Ezekiel 18:4 ('the soul who sins shall die') into Paul's climactic statement in Romans 14:12: 'each of us will give an account of himself to God.' Amaziah's merciful limitation of blood-vengeance to the actual killers is the OT application of the individual-accountability principle the NT universalizes."},
      {"type": "allusion", "target": "Ezek 18:4", "note": "The individual-accountability formula of 2 Chr 25:4 (citing Deut 24:16) is developed theologically in Ezekiel 18: the soul that sins shall die; a son does not bear the iniquity of his father; a father does not bear the iniquity of his son. Ezekiel 18 is the prophetic extension of Amaziah's legal reasoning into a full theology of individual moral responsibility."}
    ]
  },
  "26": {
    "5": [
      {"type": "allusion", "target": "Matt 6:33", "note": "As long as he sought the LORD, God made him prosper — the Chronicler's consistent prosperity-through-seeking principle finds its NT form in Matt 6:33: 'Seek first the kingdom of God and his righteousness, and all these things will be added to you.' The Chronicler presents Uzziah's prosperity as direct consequence of seeking God; Jesus's promise follows the same covenantal logic: seeking God reorients all other provisions."}
    ]
  },
  "28": {
    "15": [
      {"type": "allusion", "target": "Luke 10:33", "note": "The men named above took the captives and clothed those who were naked; they gave them sandals, provided them with food and drink, anointed them, carried on donkeys those who were faint, and brought them to Jericho — this act of the northern Israelites toward captured Judahites is the OT's closest narrative analogue to the Good Samaritan: an unexpected party (northerners, enemies of Judah) shows compassion to the wounded and helpless (captured Judahites), clothing them, feeding them, and transporting them to their destination (Jericho). The parallel is specific: both involve enemies acting as compassion-givers, and both end at Jericho. Luke's parable likely evokes this narrative memory."}
    ]
  }
}

def main():
    e = load_echo('2chronicles')
    merge_echo(e, ECHOES)
    save_echo('2chronicles', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'2chronicles echo: wrote entries for {count} verses across ch 25-28')

if __name__ == '__main__':
    main()
