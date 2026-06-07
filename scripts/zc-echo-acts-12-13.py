"""
MKT Echo Layer — Acts chapters 12–13
Run: python3 scripts/zc-echo-acts-12-13.py

Source data used:
- data/interlinear/acts.json
- data/parallels/acts.json (parallels absorbed for ch13: v22, v33, v34, v35, v41, v47)
- data/echoes/acts.json (existing ch13 entries for v33, v34, v35, v47 preserved)

Key decisions:
- Ch12 angel-release of Peter (vv.7-11): typed against Exod 12 Passover-deliverance (Luke
  notes it was the Festival of Unleavened Bread, v3) + Ps 34:7 (angel of LORD delivers)
  + Dan 6:22 (God sends angel to shut lions' mouths / shut prison)
- Herod's death (vv.20-23): allusion network — Isa 14:13-15 (the divine-claimant king
  brought low), Ezek 28:2 (prince of Tyre: "I am a god"), Dan 4:30-33 (Nebuchadnezzar's
  pride and divine judgment); Ps 2:4 (the LORD holds such rulers in derision)
- v24 "the word of God continued to spread": theme from Isa 55:10-11
- ch13 v22: 1 Sam 13:14 absorbed from parallels (David "a man after my own heart")
- ch13 v41: Hab 1:5 absorbed from parallels (look you scoffers, wonder and perish)
- Already present in echoes: ch13 v33 (Ps 2:7/6), v34 (Isa 55:3), v35 (Ps 16:10),
  v47 (Isa 49:6) — merge_echo will skip these
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
    # INTENT: merge echo entries; deduplicate by (type, target) within each verse
    # CHANGE? If echo schema changes, update dedup key here
    # VERIFY: spot-check acts.json ch12 v7 and ch13 v22 in browser echoes panel
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

ACTS_ECHOES = {
  "12": {
    "3": [
      {"type": "allusion", "target": "Exod 12:1", "note": "Luke notes the arrest occurred 'during the Festival of Unleavened Bread' — the Passover-Exodus season. Peter's imprisonment and angelic release (vv.7-11) replays the Passover pattern: God delivers his servant from mortal captivity precisely at the feast that commemorates the first great deliverance, giving the Exodus typology fresh historical fulfillment in the apostolic age."}
    ],
    "5": [
      {"type": "theme", "target": "Ps 34:6", "note": "The church's earnest prayer for the imprisoned Peter echoes the Psalter's theology of communal intercession for the afflicted. The prayer-and-deliverance sequence in vv.5-11 follows the Psalm 34 pattern: the righteous cry, the angel delivers (v.7; Ps 34:7), and the deliverance is announced to the assembly."}
    ],
    "7": [
      {"type": "allusion", "target": "Ps 34:7", "note": "The angel of the Lord appearing and the light shining in the cell enacts Psalm 34:7 — 'the angel of the LORD encamps around those who fear him, and delivers them.' Peter's prison deliverance is the NT fulfillment of this Psalm promise: the same divine-messenger protection David invoked is now operative in the apostolic community."},
      {"type": "type", "target": "Dan 6:22", "note": "As God sent his angel to shut the mouths of the lions for Daniel, so he sends his angel to release Peter from Herod's chains. The structural parallel — righteous man imprisoned for faith, divine-messenger deliverance overnight, the ruler's power frustrated — establishes Acts 12 as an Acts-of-Daniel type narrative within the early church's mission."}
    ],
    "10": [
      {"type": "allusion", "target": "Exod 14:21", "note": "The iron gate opening 'by itself' (automatos) echoes the Exodus pattern of God making a way where there is none. Luke uses the vocabulary of miraculous divine opening to interpret the prison-release as a new-Exodus liberation event, reinforced by the Passover timing (v.3)."}
    ],
    "11": [
      {"type": "allusion", "target": "Dan 6:22", "note": "Peter's confession — 'Now I know without a doubt that the Lord sent his angel and rescued me from Herod' — echoes Daniel's deliverance-recognition. The pattern is identical: a faithful servant threatened by a hostile king, divine-messenger rescue, and the ruler's plan frustrated. Luke presents Peter as a new Daniel, and the apostolic mission as the continuation of the OT righteous-servant-and-deliverer pattern."}
    ],
    "15": [
      {"type": "allusion", "target": "Ps 91:11", "note": "The praying community's suggestion 'it must be his angel' echoes the OT tradition of divine messengers accompanying God's servants (Ps 91:11, 'he will command his angels concerning you to guard you in all your ways'; Dan 10:13). The first-century expectation of personal guardian angels was grounded in such texts, and Luke presents the community's intuition as theologically correct even before Peter's arrival confirms it."}
    ],
    "22": [
      {"type": "allusion", "target": "Ezek 28:2", "note": "The crowd's acclamation — 'This is the voice of a god, not of a mortal man!' — and Herod's acceptance parallels Ezekiel's oracle against the prince of Tyre: 'your heart is proud, and you have said, I am a god' (Ezek 28:2). In both cases the fatal error is accepting divine identity; in both cases divine judgment follows immediately. The echo is thematic but precise."}
    ],
    "23": [
      {"type": "allusion", "target": "Dan 4:30", "note": "The angel striking Herod down 'because he did not give God the glory' mirrors the Nebuchadnezzar judgment of Daniel 4: a king at the peak of power who accepts god-like acclamation is struck down. Luke's report uses the OT divine-judgment-on-proud-kings template; Herod worm-eaten is the inverse of the glorified Servant (Isa 52:13-53:12)."},
      {"type": "allusion", "target": "Ps 2:4", "note": "The Lord's overthrow of Herod echoes Psalm 2:4 — 'He who sits in the heavens laughs; the Lord holds them in derision.' The Psalm presents kings who conspire against the LORD's Anointed as objects of divine derision; Herod who persecuted the apostles and killed James (v.2) is struck down in his moment of greatest theatrical power."}
    ],
    "24": [
      {"type": "theme", "target": "Isa 55:11", "note": "Luke's summary refrain — 'the word of God continued to spread and flourish' — echoes Isaiah 55:10-11: the divine word does not return empty but accomplishes the purpose for which it was sent. This refrain appears five times in Acts (6:7; 12:24; 13:49; 19:20; 28:30-31), each marking a stage of the word's advance despite — and often because of — opposition."}
    ]
  },
  "13": {
    "22": [
      {"type": "quote", "target": "1 Sam 13:14", "note": "Paul's synagogue sermon cites God's testimony about David: 'I have found in David the son of Jesse a man after my heart, who will do all my will' (blending 1 Sam 13:14 with Ps 89:20). The citation grounds the Christological argument: if David was the man after God's own heart yet died and saw corruption, then the greater Son of David who did not see corruption (v.35) must be the one God's heart truly sought."},
      {"type": "allusion", "target": "Ps 89:20", "note": "Acts 13:22 blends 1 Sam 13:14 with Ps 89:20 ('I have found David, my servant; with my holy oil I have anointed him'). The combined citation establishes the Davidic typology: David's anointing and heart-alignment are the type; the resurrection of Jesus — the perfectly faithful Son of David whom death could not hold (v.35) — is the antitype."}
    ],
    "41": [
      {"type": "quote", "target": "Hab 1:5", "note": "Paul closes his Antioch sermon with Habakkuk 1:5 as a warning: 'Look, you scoffers, wonder and perish; for I am doing a work in your days, a work that you will not believe, even if one tells it to you.' The original Habakkuk context was God's warning about the Babylonian invasion; Paul applies it to the equally incredible work of the resurrection and the Gentile mission — a work so surprising that those who refuse it will face covenant consequences."}
    ]
  }
}

def main():
    existing = load_echo('acts')
    merge_echo(existing, ACTS_ECHOES)
    save_echo('acts', existing)
    ch12_count = len(existing.get('12', {}))
    ch13_count = len(existing.get('13', {}))
    print(f'Acts 12-13 echoes: ch12={ch12_count} verses with echoes, ch13={ch13_count} verses with echoes.')

if __name__ == '__main__':
    main()
