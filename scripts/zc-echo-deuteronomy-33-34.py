"""
Echo fix — Deuteronomy chapters 33 and 34 (missing from zc-echo-deuteronomy-32-34.py)
Run: python3 scripts/zc-echo-deuteronomy-33-34.py

Deuteronomy 33: The Blessing of Moses (tribal blessings)
Deuteronomy 34: The death of Moses and the close of the Torah
Key NT echoes:
- 33:2: Angels at Sinai → Gal 3:19; Acts 7:53; Heb 2:2
- 33:12: "beloved of YHWH" (yedid) → Matt 3:17 (beloved Son at baptism)
- 33:27: "everlasting arms" → John 10:28-29; Heb 1:12
- 34:5: Moses died at YHWH's mouth → Heb 3:5-6 (servant vs. Son)
- 34:9: Joshua full of Spirit of wisdom → Acts 6:3,10 (Spirit of wisdom)
- 34:10: No prophet like Moses since → Acts 3:22-23; Heb 3:3
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
    # INTENT: Non-destructive merge — only add entries not already present by (type, target) key
    # CHANGE? If echo schema gains new required fields, update here and all echo scripts
    # VERIFY: After run, data/echoes/deuteronomy.json ch 33 and 34 should have entries
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
  "33": {
    "2": [
      {"type": "allusion", "target": "Gal 3:19", "note": "YHWH came from Sinai with ten thousands of holy ones at his right hand — the angelic host at Sinai is the OT background for Paul's statement that the Torah was 'ordained through angels by an intermediary' (Gal 3:19); Deut 33:2 LXX reads 'on his right hand were angels with him'"},
      {"type": "allusion", "target": "Heb 2:2", "note": "The flaming fire at YHWH's right hand at Sinai — Hebrews 2:2 refers to 'the message declared by angels' as the legal basis for the Mosaic law; the angelic mediation of the covenant at Sinai (Deut 33:2) establishes why the covenant received through the Son is superior to the one delivered through angels"},
    ],
    "27": [
      {"type": "allusion", "target": "John 10:28", "note": "Underneath are the everlasting arms — the eternal God as refuge with everlasting arms is the OT image for what Jesus claims in John 10:28-29: no one will snatch them out of my hand, and no one is able to snatch them out of my Father's hand; the everlasting arms of Deut 33:27 are the hands of Father and Son"},
    ],
  },
  "34": {
    "5": [
      {"type": "allusion", "target": "Heb 3:5", "note": "Moses the servant of YHWH died there — Hebrews 3:5-6 uses Moses's faithful servanthood in the house and his death as the foil for Christ: Moses was faithful as a servant, but Christ is faithful as a Son over God's house; the finality of Moses's death (he did not enter the land) is the finality the Levitical system shared, overcome only by the Son who lives forever"},
      {"type": "allusion", "target": "Jude 9", "note": "YHWH buried him and no one knows the place of his burial — Michael the archangel disputed with the devil about the body of Moses (Jude 9), suggesting Moses's burial place was contested in Jewish tradition; Jude uses it as an example of not reviling spiritual powers, trusting YHWH's own rebuke"},
    ],
    "10": [
      {"type": "fulfillment", "target": "Acts 3:22", "note": "There has not arisen a prophet in Israel like Moses whom YHWH knew face to face — Deuteronomy's closing statement that no prophet like Moses has yet arisen is the setup for Peter's Pentecost sermon: Moses himself said 'God will raise up a prophet like me' (Deut 18:15), and Peter declares that Jesus is that prophet; 34:10 makes 18:15 the book's open expectation"},
      {"type": "fulfillment", "target": "Heb 3:3", "note": "No prophet since like Moses — Hebrews 3:3 completes the comparison: Jesus has been counted worthy of more glory than Moses, as the builder of a house has more honor than the house itself; the Torah's own closing acknowledgment of Moses's unparalleled greatness becomes the foil for the letter's central argument that Christ is categorically greater"},
    ],
  },
}

def main():
    existing = load_echo('deuteronomy')
    merge_echo(existing, DEUT_ECHO)
    save_echo('deuteronomy', existing)
    out = json.loads((ROOT / 'data' / 'echoes' / 'deuteronomy.json').read_text())
    for ch in ['33', '34']:
        vv = out.get(ch, {})
        status = f'present ({len(vv)} verses)' if vv else 'MISSING'
        print(f'  ch {ch}: {status}')

if __name__ == '__main__':
    main()
