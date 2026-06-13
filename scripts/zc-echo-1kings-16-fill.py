"""
echo | 1kings | ch 16 gap-fill
Adds echo entry for ch16 (only missing echo chapter in 1 Kings).
Run: python3 scripts/zc-echo-1kings-16-fill.py
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

KINGS1_ECHOES = {
  "16": {
    "31": [
      {
        "type": "allusion",
        "target": "Rev 2:20",
        "note": "Ahab's marriage to Jezebel daughter of Ethbaal (v31) introduces the quintessential OT figure of a false prophetess who leads Israel into Baal worship and sexual immorality. Revelation 2:20 directly invokes the name: 'You tolerate that woman Jezebel, who calls herself a prophet and is teaching and seducing my servants to practice sexual immorality and to eat food sacrificed to idols.' The Thyatira letter uses 'Jezebel' as a type for syncretistic false prophecy in the church."
      }
    ],
    "34": [
      {
        "type": "fulfillment",
        "target": "Josh 6:26",
        "note": "Hiel the Bethelite rebuilds Jericho 'at the cost of Abiram his firstborn he laid its foundation, and at the cost of his youngest son Segub he set up its gates' — the precise fulfillment of Joshua's curse (Josh 6:26: 'Cursed before the LORD be the man who rises up and rebuilds this city Jericho; at the cost of his firstborn shall he lay its foundation, and at the cost of his youngest son shall he set up its gates'). The 500-year gap between pronouncement and fulfillment demonstrates the unbreakable reliability of prophetic word."
      }
    ]
  }
}

def main():
    existing = load_echo('1kings')
    merge_echo(existing, KINGS1_ECHOES)
    save_echo('1kings', existing)
    print(f'  1kings echo: ch16 = {len(existing.get("16", {}))} verse(s) with echo entries')

if __name__ == '__main__':
    main()
