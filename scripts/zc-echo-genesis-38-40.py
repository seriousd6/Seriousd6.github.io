"""
MKT Echo — Genesis chapters 38–40
Run: python3 scripts/zc-echo-genesis-38-40.py

Source data used:
- data/interlinear/genesis.json
- data/parallels/genesis.json (no entries for chs 38-40)
- data/echoes/genesis.json (ch 41 has 1 entry pre-existing; chs 38-40 fully missing)

Key decisions:
- Ch 38 (Judah and Tamar): The primary NT echo is Matt 1:3 — Tamar appears in
  Jesus's genealogy as one of four irregular women, each representing a surprising
  inclusion in the Messianic line; Judah's declaration 'she is more righteous than I'
  (v26) anticipates the pattern of the outcast vindicated
- Ch 39 (Joseph and Potiphar's wife): The fourfold 'YHWH was with Joseph' refrain
  (vv. 2, 3, 21, 23) is the primary echo — it continues the covenant-presence formula
  running from Isaac (26:24) through Christ's commission (Matt 28:20); Acts 7:9-10
  cites this explicitly
- Ch 40 (Dream interpretations): v8 ('Do not interpretations belong to God?') is
  Joseph's theological humility before God-given revelation — anticipates Daniel's
  same claim (Dan 2:27-28) and Paul's on the Spirit revealing God's depths (1 Cor 2);
  v14 (Joseph's 'remember me') is a shadow of Luke 23:42
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
  "38": {
    "1": [
      {"type": "fulfillment", "target": "Matt 1:3",
       "note": "The Judah-Tamar episode (Gen 38) produces Perez, through whom the Messianic line runs (Ruth 4:18-22; 1 Chr 2:4-15). Matthew includes Tamar explicitly in Jesus's genealogy (Matt 1:3) — one of four women in the genealogy, each associated with scandal or irregularity (Tamar, Rahab, Ruth, Bathsheba). Matthew's inclusion of Tamar announces that the Messiah's line runs not through the conventionally righteous but through those who obtained righteousness by unexpected means."}
    ],
    "26": [
      {"type": "shadow", "target": "Luke 7:47",
       "note": "Judah's verdict — 'She is more righteous than I' (Gen 38:26) — reverses every expectation: the patriarch shamed, the woman vindicated. This pattern of the outcast declared righteous and the self-righteous exposed runs through Jesus's ministry: 'I tell you, her sins, which are many, are forgiven — for she loved much' (Luke 7:47). The sinful woman at Simon's table receives the same reversal Tamar received; in both cases, the unexpected party is declared righteous."},
      {"type": "allusion", "target": "Matt 1:3",
       "note": "Tamar's vindication ('more righteous than I') is the theological ground for her inclusion in the Messianic genealogy (Matt 1:3). She is not listed despite her irregular story but because of what it reveals: the Messiah's line includes the righteous-by-unexpected-means, not only the conventionally honorable."}
    ]
  },
  "39": {
    "2": [
      {"type": "fulfillment", "target": "Acts 7:9",
       "note": "'YHWH was with Joseph' (Gen 39:2-3, 21, 23) — the fourfold refrain of divine presence in Egypt is Stephen's text in Acts 7:9-10: 'God was with him and rescued him out of all his afflictions and gave him favor and wisdom before Pharaoh.' Stephen reads Joseph as the type of the one sent by God, rejected by his brothers, who yet was exalted to save them — the pattern of Christ's rejection and exaltation."},
      {"type": "shadow", "target": "Matt 28:20",
       "note": "The 'YHWH was with Joseph' refrain (Gen 39:2, 3, 21, 23) is the OT covenant-presence formula at its most insistent — even in slavery and false imprisonment, the divine presence does not depart. This formula runs from Isaac (26:24) through Joseph to Jesus's promise: 'I am with you always, to the end of the age' (Matt 28:20). Where earlier instances were conditional blessings, Christ's version is permanent and unconditional."}
    ],
    "9": [
      {"type": "theme", "target": "1 Cor 6:18",
       "note": "Joseph refuses Potiphar's wife: 'How then can I do this great wickedness and sin against God?' (Gen 39:9) — his refusal names sexual immorality first as sin against God, then as wickedness. Paul's instruction 'Flee from sexual immorality... the sexually immoral person sins against his own body' (1 Cor 6:18) echoes Joseph's moral logic: the offense is vertical (against God) before it is horizontal (against Potiphar). Joseph's flight (v. 12) is the OT embodiment of Paul's command."}
    ],
    "20": [
      {"type": "shadow", "target": "Phil 4:11",
       "note": "Joseph imprisoned despite his innocence, yet with YHWH present in the prison (Gen 39:20-23) — the contentment of the righteous sufferer. Paul's 'I have learned, in whatever situation I am, to be content' (Phil 4:11) names what Joseph embodies: flourishing under unjust affliction because the covenant God is present. The prison becomes a place of advancement (the keeper trusts him with everything, v. 22) rather than mere punishment."}
    ]
  },
  "40": {
    "8": [
      {"type": "allusion", "target": "Dan 2:28",
       "note": "Joseph tells the cupbearer and baker: 'Do not interpretations belong to God? Please tell them to me' (Gen 40:8) — the theological claim that dream-interpretation is a divine gift, not a human technique. Daniel repeats the identical claim before Nebuchadnezzar: 'There is a God in heaven who reveals mysteries' (Dan 2:28). Both stand in a foreign court, offering God-given revelation to a king and refusing to take credit for what comes from heaven."},
      {"type": "theme", "target": "1 Cor 2:10",
       "note": "Joseph's refusal to claim the ability to interpret as his own — 'interpretations belong to God' (Gen 40:8) — establishes the principle Paul elaborates in 1 Cor 2:10: 'These things God has revealed to us through the Spirit. For the Spirit searches everything, even the depths of God.' The interpretive authority Joseph claims for God is the same authority Paul claims for the Spirit — revelation comes down, not up."}
    ],
    "14": [
      {"type": "shadow", "target": "Luke 23:42",
       "note": "Joseph pleads with the cupbearer: 'Remember me when it is well with you, and please do me the kindness to mention me to Pharaoh, and so get me out of this house' (Gen 40:14) — the innocent sufferer's cry for remembrance from one who will be exalted. The criminal on the cross echoes this plea exactly: 'Remember me when you come into your kingdom' (Luke 23:42). Joseph's forgotten plea (the cupbearer did not remember him, 40:23) anticipates the answerable prayer: Jesus does not forget, does not delay, answers immediately."}
    ],
    "23": [
      {"type": "shadow", "target": "Ps 22:1",
       "note": "The cupbearer forgot Joseph (Gen 40:23) — the innocent sufferer abandoned by the one who should have interceded. The pattern of righteous abandonment in the Joseph narrative (sold by brothers, forgotten by the cupbearer) feeds into the Psalmic cry of forsakenness (Ps 22:1) that Christ adopts from the cross. Joseph's two years of additional imprisonment after being forgotten (41:1) is the OT shadow of the silence before vindication."}
    ]
  }
}


def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)
    print('Genesis 38-40 echoes written.')

if __name__ == '__main__':
    main()
