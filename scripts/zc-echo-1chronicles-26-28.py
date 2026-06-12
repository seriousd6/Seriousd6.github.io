"""
MKT Echo — 1 Chronicles chapters 26–28
Run: python3 scripts/zc-echo-1chronicles-26-28.py

Ch 26: Gatekeeper assignments by lot; Levitical treasury oversight
Ch 27: Monthly military divisions; tribal administrators; David's counselors
Ch 28: David's charge to Solomon; the divine tabnit (pattern) for the temple;
       the Deut 31 charge echoed in Heb 13:5

Key decisions:
- 26:12 (lots for gatekeepers): connects to priestly-lot tradition and Acts 1:26 pattern
- 26:20 (treasuries of the LORD's house): connected to Rev 21:26 nations-bring-glory motif
- 27:23 (uncounted, because YHWH promised stars): Abrahamic promise of innumerable seed → Rom 4:18
- 28:9 (YHWH searches all hearts): Heb 4:13 / Rev 2:23 — omniscient scrutiny of the heart
- 28:11-12 (tabnit given by the Spirit): Heb 8:5 — the earthly sanctuary as shadow of the
  heavenly pattern; strongest echo in these chapters
- 28:20 (be strong, he will not leave you): verbatim quotation of Deut 31:6 cited in Heb 13:5
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

ECHOES = {
  "26": {
    "12": [
      {"type": "shadow", "target": "Acts 1:26", "note": "The gatekeeper assignments were determined by lot — small and great alike, family by family (26:13) — as the divinely sanctioned method for assigning priestly and Levitical roles at the threshold of God's house; Acts 1:26 uses the same mechanism (the lot fell on Matthias) to fill the twelfth apostolic office, applying to the NT threshold-guardians of the church the same principle the Chronicler records: where human preference is absent, divine choice is made visible through the lot."},
      {"type": "shadow", "target": "Heb 8:5", "note": "The Levitical gatekeepers were assigned stations at the four compass points of the temple precinct according to divinely ordered duty-rosters — the precise, architecturally structured assignment of priestly personnel to God's house reflects the same logic Hebrews identifies in Mosaic worship: the earthly sanctuary with its gatekeepers and precincts is a copy and shadow of the heavenly (Heb 8:5); the elaborate human gatekeeping arrangement points to the one through whom alone access to the true heavenly sanctuary now comes."}
    ],
    "20": [
      {"type": "allusion", "target": "Rev 21:26", "note": "The Levitical treasuries of the house of God held dedicated things from Israel's wars, spoils set apart by David and the commanders — the wealth of conquest consecrated to YHWH's service; Revelation 21:26 pictures the final fulfillment: the kings of the earth bring their glory and honor into the new Jerusalem, the ultimate treasury of God's house, where the consecration of all human achievement into divine worship reaches its eschatological completion."}
    ]
  },
  "27": {
    "23": [
      {"type": "allusion", "target": "Rom 4:18", "note": "David did not count those under twenty years of age, because YHWH had promised to multiply Israel as the stars of heaven (27:23) — the census deliberately stops at the boundary of the Abrahamic promise, refusing to number what God said would be innumerable; Paul's description of Abraham's faith in Rom 4:18 cites the same star-promise ('who against hope believed in hope, that he might become the father of many nations, as it was said, So shall your seed be') — the uncountable multitude that began as a promise to Abraham runs through David's deliberate restraint and into the NT's vision of the redeemed from every nation."}
    ]
  },
  "28": {
    "9": [
      {"type": "shadow", "target": "Heb 4:13", "note": "David charges Solomon: 'Know the God of your father and serve him with a whole heart and a willing mind, for the LORD searches all hearts and understands every plan and thought' (28:9) — the Davidic charge grounds faithful service in divine omniscience; Hebrews 4:13 states the same principle as the foundation of the call to perseverance: no creature is hidden before him, but all are naked and exposed to the eyes of him to whom we must give account; the all-searching God before whom Solomon is charged to serve without dissimulation is the God before whom the church is called to hold fast."},
      {"type": "allusion", "target": "Rev 2:23", "note": "YHWH searches all hearts and understands every plan and thought (28:9); Revelation 2:23 places the same claim on the lips of the risen Christ: 'I am he who searches mind and heart' — transferring to Christ the divine prerogative that the OT exclusively attributes to YHWH, and establishing that the exalted Lord exercises the same sovereign scrutiny of the interior life that the OT God demanded of Solomon."}
    ],
    "11": [
      {"type": "shadow", "target": "Heb 8:5", "note": "David gave Solomon the plan (<em>tabnît</em>) of the temple — the vestibule, the buildings, the treasuries, the upper rooms, the inner chambers, the place of the mercy seat — and explained: all this he made me understand in writing from the hand of the LORD, all the work of the plan (28:11-19); the word <em>tabnît</em> (pattern, blueprint) is the exact Hebrew word used in Exodus 25:9,40, where YHWH showed Moses the heavenly pattern (<em>tabnît</em>) after which the tabernacle was to be built; Hebrews 8:5 cites the Exodus pattern-command and calls the entire Levitical service a copy and shadow of the heavenly sanctuary — the tabnît David received for Solomon's temple stands in the same chain: earthly sanctuary built after heavenly pattern, pointing to the true heavenly sanctuary into which Christ has entered as our high priest."}
    ],
    "12": [
      {"type": "shadow", "target": "1 Cor 3:16", "note": "David said the temple plan came to him by the Spirit — 'all this, in writing from the hand of the LORD, he made me understand, all the work of the plan' (28:19), implicitly through prophetic inspiration; the Spirit-given blueprint for God's earthly dwelling-place is the OT precedent for Paul's announcement in 1 Cor 3:16 that believers are God's temple and the Spirit of God dwells in them — the architect of the Solomonic temple in David's vision and the divine presence that inhabits the new covenant community are the same Spirit, now indwelling human beings rather than a stone building."}
    ],
    "20": [
      {"type": "fulfillment", "target": "Heb 13:5", "note": "David's charge to Solomon — 'Be strong and courageous and do it. Do not be afraid and do not be dismayed, for the LORD God, even my God, is with you. He will not leave you or forsake you' (28:20) — quotes verbatim from Moses' charge to Joshua at the Jordan (Deut 31:6,8) and applies it to the temple-building successor; Hebrews 13:5 quotes the same Deuteronomy promise as the ground of contentment and fearlessness for the new covenant community: 'He has said, I will never leave you nor forsake you'; David's transmission of Moses' promise to Solomon becomes the NT's promise to all who approach God through Christ, the true temple-builder."}
    ]
  }
}

def main():
    existing = load_echo('1chronicles')
    merge_echo(existing, ECHOES)
    save_echo('1chronicles', existing)
    ch_count = len(ECHOES)
    v_count = sum(len(vv) for vv in ECHOES.values())
    entry_count = sum(len(ee) for vv in ECHOES.values() for ee in vv.values())
    print(f'1 Chronicles 26-28 echoes written ({ch_count} chapters, {v_count} verses, {entry_count} entries).')

if __name__ == '__main__':
    main()
