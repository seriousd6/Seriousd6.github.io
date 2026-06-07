"""
echo layer — Colossians chapter 4 (fills missing ch4)
Output: data/echoes/colossians.json
Run: python3 scripts/zc-echo-colossians-4-full.py
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
    # INTENT: Merge echo entries without overwriting existing verse keys — safe to re-run.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update traversal.
    # VERIFY: Re-running produces identical output; existing entries preserved.
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

NEW_ECHOES = {
  "4": {
    "2": [
      {"type": "allusion", "target": "Dan 6:10", "note": "Devote yourselves to prayer, being watchful in it with thanksgiving — Daniel prayed three times daily even under threat of death; the pattern of disciplined, steadfast prayer that Colossians calls for echoes Daniel's unwavering prayer practice as the mark of covenant faithfulness in a pagan environment"},
      {"type": "allusion", "target": "Ps 55:17", "note": "Evening and morning and at noon I utter my complaint and moan, and he hears my voice — the psalmist's three-times-daily prayer discipline is the OT ground for Paul's call to devote to prayer; thanksgiving added by Paul marks the new-covenant development of the practice"}
    ],
    "6": [
      {"type": "allusion", "target": "Prov 16:24", "note": "Let your speech always be gracious, seasoned with salt — Proverbs' gracious words are like a honeycomb, sweet to the soul and healing to the body; the seasoned-with-salt image adds the covenantal dimension: salt was required in all Mosaic grain offerings (Lev 2:13: you shall season all your grain offerings with salt) and signified covenant permanence"},
      {"type": "allusion", "target": "Lev 2:13", "note": "Salt as the sign of the covenant of your God — every offering was to be seasoned with the salt of the covenant; Paul's call for speech seasoned with salt draws on the sacrificial-covenantal resonance: Christian speech is a kind of offering"}
    ],
    "10": [
      {"type": "allusion", "target": "Acts 15:37-39", "note": "Mark the cousin of Barnabas — the Barnabas/Mark conflict that split the first missionary team (Acts 15:37-39: Barnabas took Mark, Paul took Silas) is now resolved: Paul commends Mark to the Colossians, showing the restoration of the broken relationship"},
      {"type": "allusion", "target": "Acts 12:12", "note": "John whose other name is Mark (Acts 12:12: the house of Mary, mother of John whose other name was Mark) — the Jerusalem house-church connection; Mark is a figure who bridges the Jerusalem origin and the Gentile mission, restored to Paul's circle by the time of Colossians"}
    ],
    "16": [
      {"type": "allusion", "target": "Rev 3:14-22", "note": "Have it also read in the church of the Laodiceans — Revelation's letter to Laodicea (Rev 3:14: to the angel of the church in Laodicea write) addresses the same congregation Paul directs to receive this letter; the Laodicean church appears in both Paul's circle and John's seven churches, suggesting a continuous community history across the NT documents"}
    ],
    "17": [
      {"type": "allusion", "target": "Phlm 2", "note": "Say to Archippus, see that you fulfill the ministry that you have received in the Lord — Archippus is addressed as Paul's fellow soldier in Philemon 2; the parallel instruction suggests a pattern of accountability across the Pauline letter network, where individual leaders are publicly charged before their congregations"}
    ],
    "18": [
      {"type": "allusion", "target": "Gal 6:11", "note": "I, Paul, write this greeting with my own hand — Galatians 6:11 (see with what large letters I am writing to you with my own hand) and 2 Thess 3:17 (this is the sign of genuineness in every letter of mine) establish the autograph as Paul's authentication marker against forgery; the Colossian autograph similarly asserts authenticity"},
      {"type": "allusion", "target": "2 Thess 3:17", "note": "Remember my chains — the imprisoned apostle's autograph connects to the chain-reference in Eph 6:20 (ambassador in chains) and Phil 1:13-14; the physical reality of Paul's imprisonment authenticates both the letter and the apostolic suffering-pattern it embodies"}
    ]
  }
}

if __name__ == '__main__':
    existing = load_echo('colossians')
    merge_echo(existing, NEW_ECHOES)
    save_echo('colossians', existing)
    for ch in ['1', '2', '3', '4']:
        print(f'  ch {ch}: {len(existing.get(ch, {}))} verses with echoes')
