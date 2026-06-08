"""
Echo layer — Isaiah chapters 59–64
Run: python3 scripts/zc-echo-isaiah-59-64.py

Chapters 59-61, 63-64 already have entries; this script adds missing chapter 62.

Key echo decisions:
- Isa 62:4-5 bridegroom rejoicing over the bride → Rev 19:7; John 3:29 (fulfillment —
  the divine bridegroom is Christ; Rev 19 explicitly develops the image).
- Isa 62:11 "Behold, your salvation comes; his reward is with him" → Rev 22:12 (direct
  verbal parallel: Christ at his return brings "my recompense with me"); Matt 21:5
  (the triumphal entry quote "Say to the daughter of Zion" draws on this verse).
- Isa 62:12 "called The Holy People, The Redeemed of the LORD" → 1 Pet 2:9 (the NT
  church's new identity titles are drawn from this and related OT passages).
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

ISAIAH_ECHOES = {
  "62": {
    "5": [
      {
        "type": "fulfillment",
        "target": "Rev 19:7",
        "note": "Isa 62:5 'as the bridegroom rejoices over the bride, so shall your God rejoice over you' is the OT anticipation of Rev 19:7 ('the marriage of the Lamb has come, and his Bride has made herself ready') — Jesus is explicitly identified as the divine bridegroom who rejoices over his redeemed people, bringing the prophetic image to its consummation."
      },
      {
        "type": "allusion",
        "target": "John 3:29",
        "note": "John the Baptist applies the bridegroom figure to Jesus: 'The friend of the bridegroom, who stands and hears him, rejoices greatly at the bridegroom's voice' — the rejoicing bridegroom of Isa 62:5 is the same one whose voice John hears and over whom he rejoices."
      }
    ],
    "11": [
      {
        "type": "fulfillment",
        "target": "Rev 22:12",
        "note": "Christ's return announcement — 'Behold, I am coming soon, bringing my recompense with me, to repay each one for what he has done' — is the NT fulfillment of Isa 62:11's 'Behold, your salvation comes; behold, his reward is with him, and his recompense before him'; the verbal parallel is exact and intentional."
      },
      {
        "type": "fulfillment",
        "target": "Matt 21:5",
        "note": "The triumphal entry quotation 'Say to the daughter of Zion, Behold, your king is coming to you' (Matt 21:5) draws its opening formula from Isa 62:11 ('Say to the daughter of Zion, Behold, your salvation comes'), identifying the entering king as the salvation Isa 62 announces."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "1 Pet 2:9",
        "note": "Peter's description of the church — 'a chosen race, a royal priesthood, a holy nation, a people for his own possession' — draws on Isa 62:12's titles for redeemed Israel ('The Holy People, The Redeemed of the LORD, A City Not Forsaken'), applying the prophetic identity of restored Zion to the NT community gathered around Christ."
      }
    ]
  }
}

def main():
    existing = load_echo('isaiah')
    merge_echo(existing, ISAIAH_ECHOES)
    save_echo('isaiah', existing)
    # INTENT: Add echo entries for the single missing chapter (62) in the 59-64 range
    # CHANGE? If more chapters in 59-64 become empty, add them here
    # VERIFY: ch 62 now present in data/echoes/isaiah.json with 3 entries
    out = json.loads((ROOT / 'data' / 'echoes' / 'isaiah.json').read_text())
    for ch in range(59, 65):
        ck = str(ch)
        entries = out.get(ck, {})
        total = sum(len(v) for v in entries.values())
        status = f'done ({len(entries)} vv, {total} entries)' if entries else 'MISSING'
        print(f'  ch {ch}: {status}')

if __name__ == '__main__':
    main()
