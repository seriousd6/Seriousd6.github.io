"""
MKT Echo — Genesis chapters 25–26
Run: python3 scripts/zc-echo-genesis-25-26.py

Source data used:
- data/interlinear/genesis.json
- data/parallels/genesis.json (no parallels entries for chs 25-26)
- data/echoes/genesis.json (ch 25 v23 pre-existing [Rom 9:12]; script adds 25:29-34 and all of ch 26)

Key decisions:
- Ch 25: only v29-34 (Esau's birthright sale) adds to pre-existing v23; the Ishmael
  genealogy (vv. 12-18) has no strong direct NT echo beyond the nations-framework already
  covered in ch 10-11 entries; Jacob's birth-name meaning (ya'aqov = heel-grasper)
  is noted but the key NT echo is Heb 12:16-17 on Esau's despising of the birthright
- Ch 26: Isaac's covenant renewal (vv. 1-5, 23-25) carries the Abrahamic blessing
  formula taken up by Paul (Gal 3:16 — 'offspring' singular = Christ); the third
  wife-sister narrative (vv. 6-11) does not have a strong direct NT echo but is
  noted thematically; the Abimelech covenant (vv. 26-31) shows a Gentile king
  recognizing YHWH's blessing — foreshadows the Gentile mission
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

GENESIS_ECHOES = {
  "25": {
    "23": [
      {"type": "fulfillment", "target": "Rom 9:12",
       "note": "Pre-existing entry — 'the older will serve the younger' (Gen 25:23) is Paul's proof text in Rom 9:10-12 for unconditional divine election: the oracle was given before the twins were born, before either had done good or evil, so that God's purpose of election would stand — not because of works but because of him who calls."}
    ],
    "29": [
      {"type": "allusion", "target": "Heb 12:16",
       "note": "'See to it that no one... is unholy like Esau, who sold his own birthright for a single meal' (Heb 12:16) — the birthright sale of Gen 25:29-34 becomes in Hebrews the canonical image for trading ultimate inheritance for immediate gratification. The 'birthright' (<em>bĕkōrāh</em>) carried the double portion and patriarchal blessing; Esau's contempt for it ('What use is the birthright to me?' v. 32) is the OT type of those who profane holy things for temporal comfort."}
    ],
    "34": [
      {"type": "allusion", "target": "Heb 12:17",
       "note": "'Esau despised his birthright' (Gen 25:34b) — Hebrews 12:17 completes the typological use: 'For you know that afterward, when he desired to inherit the blessing, he was rejected, for he found no chance to repent, though he sought it with tears.' The irreversibility of Esau's loss (confirmed in Gen 27:38-40) makes him the canonical figure for the point of no return — the squandering of covenant privilege that cannot be undone by later regret."}
    ]
  },
  "26": {
    "4": [
      {"type": "fulfillment", "target": "Gal 3:16",
       "note": "'In your offspring all the nations of the earth shall be blessed' (Gen 26:4) — the Abrahamic blessing formula is re-granted to Isaac verbatim. Paul's argument in Gal 3:16 turns on the singular 'offspring' (<em>zera</em> / <em>sperma</em>): it does not say 'offsprings' (plural) but 'your offspring' (singular), which is Christ. The re-iteration to Isaac is another link in the singular-seed chain running from Abraham through Isaac and Jacob to Christ."},
      {"type": "allusion", "target": "Acts 3:25",
       "note": "'In your offspring all the families of the earth shall be blessed' — repeated to Isaac in Gen 26:4, it is the same formula Peter quotes in Acts 3:25 at Pentecost: 'In your offspring shall all the families of the earth be blessed.' Peter applies the promise to the Gentile mission inaugurated by Christ's resurrection; Isaac's re-receiving of the promise is another step in the canonical chain from the Abrahamic covenant to the universal gospel."}
    ],
    "24": [
      {"type": "shadow", "target": "Matt 28:20",
       "note": "YHWH appears to Isaac at Beersheba: 'I am the God of Abraham your father; fear not, for I am with you and will bless you and multiply your offspring for my servant Abraham's sake' (Gen 26:24). The divine 'I am with you' (<em>ʾānōkî ʿimmāk</em>) formula — given here to Isaac, to Jacob (28:15), to Joseph (39:2-3), to Moses (Exod 3:12), to Joshua (Josh 1:5) — reaches its definitive fulfillment in Jesus's commission: 'I am with you always, to the end of the age' (Matt 28:20). The incarnate Christ does not merely promise his presence but himself embodies it."}
    ],
    "28": [
      {"type": "shadow", "target": "Luke 2:32",
       "note": "Abimelech of Gerar comes to Isaac and says: 'We see plainly that the LORD has been with you' (Gen 26:28) — a Philistine king recognizes and testifies to YHWH's blessing on the covenant bearer. This pattern of Gentile recognition of divine favor on the covenant people foreshadows the universal reach of that favor in Christ: Simeon prophesies that Christ will be 'a light for revelation to the Gentiles' (Luke 2:32); the Magi and the centurion at the cross are NT expressions of the same pattern Abimelech embodies."}
    ],
    "33": [
      {"type": "theme", "target": "John 4:12",
       "note": "The re-digging of Abraham's wells (Gen 26:18-22) culminates in naming Shibah ('oath'), giving Beersheba its second etymology (the first in Gen 21:31 — both = well of the oath). Jesus's conversation at a well in Samaria (John 4) invokes the patriarchal well-tradition: 'Are you greater than our father Jacob, who gave us the well?' (John 4:12). The living water Jesus offers (John 4:10-14) is the fulfillment of what the patriarchal wells pointed to — access to the covenant God who sustains life."}
    ]
  }
}


def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)
    print('Genesis 25-26 echoes written.')

if __name__ == '__main__':
    main()
