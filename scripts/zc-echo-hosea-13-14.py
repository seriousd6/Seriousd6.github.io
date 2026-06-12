"""
MKT Echo — Hosea chapters 13–14
Run: python3 scripts/zc-echo-hosea-13-14.py

Ch13 already has v14 (1 Cor 15:55). This script adds ch14 only.
Key NT connections:
  14:2 — "fruit of lips" → Heb 13:15 (sacrifice of praise = fruit of lips)
  14:4 — "I will love them freely" → 1 John 4:10 / Rom 5:8 (unconditional grace)
  14:9 — "who is wise / stumble" → 1 Pet 2:8 / Rom 9:33
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
    print(f'wrote {p.relative_to(ROOT)}')

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

HOSEA_ECHOES = {
  "14": {
    "2": [
      {"type": "fulfillment", "target": "Heb 13:15", "note": "Take words with you and return to the LORD; say to him, Forgive all our sins and receive us graciously, and we will offer the fruit of our lips — Hebrews 13:15 cites the exact phrase 'fruit of lips': through him then let us continually offer up a sacrifice of praise to God, that is, the fruit of lips that acknowledge his name; the prayer-of-return that Hosea prescribes — returning to YHWH with words and offering the fruit of lips — is fulfilled in Christ-mediated worship"},
      {"type": "allusion", "target": "Luke 15:18-19", "note": "Take words with you and return to the LORD — the prescribed words of return in Hosea 14:2 (Forgive all our sins and receive us graciously) are the vocabulary of the prodigal son's rehearsed speech: Father, I have sinned against heaven and before you; I am no longer worthy to be called your son; the repentance script that Hosea provides is enacted by the returning son, who is received with free grace rather than the wages of his sin"}
    ],
    "4": [
      {"type": "allusion", "target": "1 John 4:10", "note": "I will heal their waywardness; I will love them freely, for my anger has turned away from them — the free, unilateral love of YHWH extended to the wayward is the OT form of 1 John 4:10: not that we loved God but that he loved us and sent his Son as the propitiation for our sins; the love is initiated by God, not earned, directed at the wayward, and accompanied by the turning away of divine anger — precisely the atonement dynamic"},
      {"type": "allusion", "target": "Rom 5:8", "note": "I will love them freely — the freely-given love extended to the wayward is the OT form of Paul's while we were still sinners, Christ died for us; Hosea's free love (without precondition, before repentance is complete) anticipates the unconditional grace of the cross: God demonstrates his own love for us in this"}
    ],
    "9": [
      {"type": "allusion", "target": "1 Pet 2:8", "note": "The ways of the LORD are right, and the upright walk in them, but transgressors stumble in them — Peter applies the stumbling pattern to Christ: a stone of stumbling, and a rock of offense; they stumble because they disobey the word; Hosea's observation that the same divine ways that the righteous walk in are the ways that transgressors stumble over is the OT form of the stone-of-stumbling theology applied to Christ"},
      {"type": "allusion", "target": "Rom 9:33", "note": "Transgressors stumble in them — Paul's stone-of-stumbling citation (Isa 8:14; 28:16) shares the stumbling pattern Hosea uses: those who resist God's covenant way stumble; Israel stumbled over Christ as the stone because they pursued righteousness by works rather than by faith (Rom 9:32); Hosea's stumbling transgressors anticipate the tragic stumbling of Israel over its own Messiah"}
    ]
  }
}

def main():
    existing = load_echo('hosea')
    merge_echo(existing, HOSEA_ECHOES)
    save_echo('hosea', existing)
    print('Hosea 14 echo written.')

if __name__ == '__main__':
    main()
