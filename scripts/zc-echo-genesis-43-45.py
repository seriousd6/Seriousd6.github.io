"""
MKT Echo — Genesis chapters 43–45
Run: python3 scripts/zc-echo-genesis-43-45.py

Source data used:
- data/interlinear/genesis.json
- data/parallels/genesis.json (no entries for chs 43-45)
- data/echoes/genesis.json (chs 43, 44, 45 all missing; 41-42 pre-existing)

Key decisions:
- Ch 43 (return to Egypt with Benjamin): Judah's surety pledge (v9) is the
  primary theological echo — Heb 7:22 uses the same vocabulary (guarantor)
  for Christ as guarantor of the new covenant; Joseph's emotional reunion with
  Benjamin foreshadows reconciliation themes (Luke 15)
- Ch 44 (silver cup; Judah's intercession): v32-33 is the most theologically dense
  echo in Genesis 43-45 — Judah's offer to substitute himself for Benjamin is the
  most explicit OT model of voluntary substitution; from Judah's tribe comes the
  ultimate substitute (Christ); 1 Pet 3:18 and Isa 53:6 are the direct NT counterparts
- Ch 45 (Joseph reveals himself): v5,7 ('God sent me before you to preserve life')
  is the definitive OT statement of divine providence through human evil; Acts 2:23
  and Rom 8:28 are its NT counterparts; the reconciliation scene echoes Luke 15:20
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
  "43": {
    "9": [
      {"type": "type", "target": "Heb 7:22",
       "note": "Judah pledges himself as surety for Benjamin: 'I will be a pledge of his safety. From my hand you shall require him. If I do not bring him back and set him before you, then let me bear the blame forever' (Gen 43:9). Hebrews uses the identical concept for Christ: Jesus is the 'guarantor' (egguos, Heb 7:22) of a better covenant. Judah, from the tribe from which Christ came, stands surety for his brother; Christ the Son of Judah stands surety for his people before the Father."}
    ],
    "29": [
      {"type": "shadow", "target": "Luke 15:20",
       "note": "Joseph saw his brother Benjamin and said: 'God be gracious to you, my son!' (Gen 43:29) — Joseph, barely containing his emotion (v. 30), blesses the long-separated full brother. The pattern of the exalted figure overwhelmed with compassion at the sight of the estranged runs through Joseph and forward to the father who ran and embraced the returning prodigal (Luke 15:20). The Joseph narrative is the primary OT subtext for the parable."}
    ]
  },
  "44": {
    "16": [
      {"type": "shadow", "target": "Rom 3:19",
       "note": "Judah responds when the cup is found: 'What shall we say to my lord? What shall we speak? Or how can we clear ourselves? God has found out the guilt of your servants' (Gen 44:16). The brothers stand in guilty silence before the viceroy — the OT image of universal guilty silence before God. Paul cites this universal silence in Rom 3:19: 'so that every mouth may be stopped, and the whole world may be held accountable to God.' Judah's speechless guilt is the raw experience Paul universalizes."}
    ],
    "32": [
      {"type": "type", "target": "1 Pet 3:18",
       "note": "Judah's intercession climaxes in voluntary substitution: 'Please let your servant remain instead of the boy as a servant to my lord, and let the boy go back with his brothers' (Gen 44:33). This is the most explicit substitution offer in the OT. Christ's substitution fulfills what Judah enacted: 'Christ also suffered once for sins, the righteous for the unrighteous, that he might bring us to God' (1 Pet 3:18). Judah, from whose tribe Christ came, enacts the substitutionary pattern that Christ fulfills absolutely."},
      {"type": "shadow", "target": "Isa 53:6",
       "note": "Judah's 'let me bear the blame forever' and 'let your servant remain instead of the boy' (Gen 44:32-33) establishes the substitution structure that Isaiah 53 elaborates: 'the LORD has laid on him the iniquity of us all' (Isa 53:6). The logic is identical — one bears what belongs to another, so the other may go free. Judah's offer is only partially enacted (Joseph relents without requiring it); Christ's is fully enacted."}
    ]
  },
  "45": {
    "5": [
      {"type": "shadow", "target": "Acts 2:23",
       "note": "Joseph's theological interpretation of his suffering: 'Do not be distressed or angry with yourselves because you sold me here, for God sent me before you to preserve life' (Gen 45:5) — human evil and divine purpose both affirmed without collapsing into each other. Acts 2:23 states the identical dual causation for Christ's death: 'delivered up according to the definite plan and foreknowledge of God — you crucified and killed by the hands of lawless men.' Both Joseph and Jesus identify divine purpose running through human wickedness without excusing the wickedness."}
    ],
    "7": [
      {"type": "shadow", "target": "Rom 8:28",
       "note": "'God sent me before you to preserve for you a remnant on earth, and to keep alive for you many survivors' (Gen 45:7) — Joseph's formula for divine providential purpose through suffering is the OT precursor to 'all things work together for good, for those who are called according to his purpose' (Rom 8:28). Joseph's life is the canonical worked example: betrayal, slavery, false accusation, imprisonment — all overruled and redirected by God toward the preservation of the covenant family."}
    ],
    "14": [
      {"type": "allusion", "target": "Luke 15:20",
       "note": "Joseph fell upon his brother Benjamin's neck and wept; then he kissed all his brothers and wept upon them (Gen 45:14-15). The parable of the prodigal son draws on this reconciliation scene: the father runs, embraces, and kisses (Luke 15:20-21), echoing the emotionally charged reunion of the exalted Joseph with his estranged brothers. In both scenes the one wronged initiates the embrace; in both the estranged are welcomed without conditions."}
    ]
  }
}


def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)
    print('Genesis 43-45 echoes written.')

if __name__ == '__main__':
    main()
