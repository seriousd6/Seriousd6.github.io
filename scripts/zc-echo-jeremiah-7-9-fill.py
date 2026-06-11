"""
MKT Echo Layer — Jeremiah chapters 7–9
Run: python3 scripts/zc-echo-jeremiah-7-9-fill.py

Chapters 7 and 9 already have entries (7:11 = Matt 21:13 den of robbers;
9:24 = 1 Cor 1:31 / 2 Cor 10:17 boasting). Only chapter 8 needs entries.

Key echo decisions:
- 8:11 'peace, peace when there is no peace' → 1 Thess 5:3 is the clearest NT
  allusion: Paul's 'peace and safety' false-security formula is drawn from Jeremiah's
  false-prophet vocabulary
- 8:13 barren fig tree (no figs) → Matt 21:19 / Luke 13:6-9 fig tree cursing and
  parable; contextually linked to the temple cleansing which itself quotes Jer 7:11
- 8:22 balm in Gilead / no physician → Luke 5:31 / Matt 9:12 Jesus as physician;
  answered prophetically in Christ
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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

JER_ECHOES = {
  "8": {
    "7": [
      {
        "type": "allusion",
        "target": "Luke 12:56",
        "note": "The birds know their appointed seasons instinctively; Jesus rebukes his contemporaries for reading weather signs but failing to discern the covenant moment — the same contrast between natural attentiveness and spiritual blindness that Jeremiah draws with the migratory stork."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "1 Thess 5:3",
        "note": "Paul's 'while people are saying Peace and safety, destruction will come on them suddenly' (1 Thess 5:3) draws on the Jeremianic false-prophet formula: 'peace, peace, when there is no peace' (6:14; 8:11). The vocabulary of false security followed by sudden judgment is the same covenantal pattern."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Mark 11:13",
        "note": "Jesus's cursing of the fig tree that has leaves but no fruit (Mark 11:13-14, 20-21) enacts the Jeremiah 8:13 image — no figs on the fig tree, no grapes on the vine — as an acted parable of covenant Israel's barrenness. The temple cleansing that frames the fig tree incident itself quotes Jer 7:11, tightening the Jeremian context."
      },
      {
        "type": "allusion",
        "target": "Luke 13:7",
        "note": "The parable of the barren fig tree (Luke 13:6-9) uses the same 'no fruit for three years' structure as the Jeremiah harvest-failure image: the vineyard owner instructs the worker to cut it down since it bears no fruit and wastes the soil."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Matt 9:12",
        "note": "Jeremiah's rhetorical question 'Is there no physician there?' is answered in Christ: Jesus identifies himself as the physician who has come for the sick, not the healthy (Matt 9:12; Luke 5:31). The balm that cannot heal Israel's covenant-wound finds its answer in the one who heals what no earthly medicine could cure."
      }
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHOES)
    save_echo('jeremiah', existing)

    # Verify chapter 8 now has entries
    out = json.loads((ROOT / 'data/echoes/jeremiah.json').read_text())
    for ch in ['7', '8', '9']:
        entries = out.get(ch, {})
        status = 'done' if entries else 'MISSING'
        print(f'  ch {ch}: {status} ({sum(len(v) for v in entries.values())} echo entries)')

if __name__ == '__main__':
    main()
