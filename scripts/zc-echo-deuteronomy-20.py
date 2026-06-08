"""
Echo fix — Deuteronomy chapter 20 (missing from zc-echo-deuteronomy-18-21.py)
Run: python3 scripts/zc-echo-deuteronomy-20.py

Deuteronomy 20 is the laws of warfare. Key NT echoes:
- vv.5-7: The three war exemptions (house, vineyard, betrothed woman) are
  deliberately echoed by Luke 14:18-20's Great Banquet excuses
- v.10: "offer terms of peace first" → Luke 14:32; Luke 19:42
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
    # INTENT: Non-destructive merge — only add entries not already present
    # CHANGE? If echo schema gains new required fields, update here and all echo scripts
    # VERIFY: After run, data/echoes/deuteronomy.json ch 20 should have entries
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

DEUT_ECHO = {
  "20": {
    "5": [
      {"type": "allusion", "target": "Luke 14:18", "note": "I have bought a field, and I must go out and see it — Luke 14:18-20's three excuses in the Great Banquet parable (field, oxen, wife) deliberately echo Deut 20:5-7's three war exemptions (built a house, planted a vineyard, betrothed a woman); Jesus reframes the banquet-refusers as those who invoke the very excuses Torah authorized for battle, suggesting they treat the kingdom invitation as less urgent than a property transaction"},
    ],
    "10": [
      {"type": "allusion", "target": "Luke 14:32", "note": "When you draw near to a city to fight against it, first offer it terms of peace — the king who sends a delegation to ask for terms of peace in Luke 14:32 echoes the Deuteronomic war-law; Jesus transposes the military logic into the logic of discipleship: count the cost before you begin, and know whether you can complete the campaign"},
      {"type": "allusion", "target": "Luke 19:42", "note": "Would that you, even you, had known on this day the things that make for peace — Jesus weeping over Jerusalem echoes the Deuteronomic offer of peace before siege; Jerusalem's rejection of Christ is the rejection of the peace-terms YHWH's envoy came to offer before the judgment fell in 70 CE"},
    ],
  },
}

def main():
    existing = load_echo('deuteronomy')
    merge_echo(existing, DEUT_ECHO)
    save_echo('deuteronomy', existing)
    out = json.loads((ROOT / 'data' / 'echoes' / 'deuteronomy.json').read_text())
    ch20 = out.get('20', {})
    if ch20:
        print(f'  OK: ch 20 now has {len(ch20)} verse(s) with entries')
    else:
        print('  MISSING: ch 20 still empty')

if __name__ == '__main__':
    main()
