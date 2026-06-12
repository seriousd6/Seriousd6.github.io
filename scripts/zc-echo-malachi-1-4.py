"""Malachi echo layer — NT allusions/fulfillments for chs 1–4.
Existing echo already has ch3:1 (Matt 11:10/Mark 1:2) and ch4:5-6 (Matt 11:14/Luke 1:17).
This script adds ch1 and ch2 entries to complete all-chapter coverage.
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

MAL_ECHO = {
  "1": {
    "11": [
      {"type": "allusion", "target": "Rev 5:9", "note": "From the rising of the sun to its setting my name will be great among the nations, and in every place incense will be offered to my name, and a pure offering — Malachi's oracle that YHWH's name will be universally worshiped is the OT's most explicit prediction of global worship; Revelation fulfills it: worthy is the Lamb, sang the four living creatures and the elders representing every tribe, language, people, and nation (Rev 5:9); the incense in Revelation is the prayers of the saints (Rev 8:3-4) — the universal pure offering Malachi foresaw"},
      {"type": "allusion", "target": "John 4:21", "note": "In every place incense will be offered to my name, and a pure offering — Jesus's dialogue with the Samaritan woman reaches the same conclusion from the opposite direction: neither on this mountain nor in Jerusalem will you worship the Father... true worshipers will worship the Father in spirit and truth (John 4:21-23); Malachi says every place; Jesus says spirit and truth transcends every specific place; the universal worship Malachi foresaw is the Spirit-directed worship Jesus inaugurates"}
    ]
  },
  "2": {
    "10": [
      {"type": "allusion", "target": "Eph 4:6", "note": "Have we not all one Father? Has not one God created us? Why then are we faithless to one another, profaning the covenant of our fathers? — Malachi's rhetorical grounding of ethical faithfulness in monotheistic creation-faith; Paul gives the NT's equivalent: one God and Father of all, who is over all and through all and in all (Eph 4:6); shared paternity under one Creator grounds the unity and mutual faithfulness that the body of Christ is called to express, just as it grounded Israel's covenant community"}
    ],
    "15": [
      {"type": "allusion", "target": "Matt 19:6", "note": "Did he not make them one, with a portion of the Spirit in their union? And what was the one God seeking? Godly offspring. So guard yourselves in your spirit, and let none of you be faithless to the wife of your youth — Malachi's argument against divorce: God made the marriage partners one; Jesus uses the same creation-oneness argument: what God has joined together, let not man separate (Matt 19:6); both ground marriage faithfulness in the divine act of making two into one, and both locate the breach in human hardness of heart (Matt 19:8)"}
    ]
  }
}

def main():
    existing = load_echo('malachi')
    merge_echo(existing, MAL_ECHO)
    save_echo('malachi', existing)
    covered = sorted(existing.keys(), key=int)
    print(f'  malachi echo: chapters with data = {covered}')
    for ch in covered:
        vcount = sum(len(v) for v in existing[ch].values())
        print(f'    ch{ch}: {vcount} total entries')

if __name__ == '__main__':
    main()
