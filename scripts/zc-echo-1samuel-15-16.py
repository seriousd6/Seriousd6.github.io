"""
Echo Commentary — 1 Samuel chapters 15–16
Run: python3 scripts/zc-echo-1samuel-15-16.py

Ch15: Saul's disobedience with Amalek — "to obey is better than sacrifice" (v22);
      rejection of Saul as king (vv23,28); divine immutability (v29)
Ch16: David's anointing — YHWH looks on the heart (v7); Spirit rushing on David (v13,
      already in JSON); David playing harp before tormented Saul (v23)

Key OT↔NT connections:
- 15:22 → Hos 6:6 / Matt 9:13 / Heb 10:5-7: obedience over sacrifice
- 15:28 → Acts 13:22: kingdom transferred to better king (David/Messiah)
- 16:7 → John 7:24 / 2 Cor 5:16: YHWH's seeing vs human seeing
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

ECHO = {
  "15": {
    "22": [
      {"type": "allusion", "target": "Hos 6:6", "note": "Samuel: 'to obey is better than sacrifice, and to heed than the fat of rams' — Hosea 6:6 ('I desire steadfast love, not sacrifice') is the prophetic development of Samuel's verdict; Jesus cites Hos 6:6 twice (Matt 9:13; 12:7) against those who prioritize ritual over mercy, making Samuel's rebuke to Saul the precursor to Jesus's critique of Pharisaic religion"},
      {"type": "allusion", "target": "Heb 10:5-7", "note": "Samuel's 'obedience rather than sacrifice' principle reaches its fullest expression in Psalm 40:6-8 (cited in Heb 10:5-7): 'Sacrifices and offerings you have not desired... then I said, Behold, I have come to do your will, O God' — applied to Christ's incarnation as the ultimate act of obedience that supersedes the entire sacrificial system; what Saul failed to embody, Christ perfectly enacted"},
      {"type": "allusion", "target": "Phil 2:8", "note": "Saul's failure is disobedience in the moment of apparent victory; Christ's obedience is the opposite pattern — 'he humbled himself by becoming obedient to the point of death, even death on a cross' (Phil 2:8); the contrast between Saul who preserved what God said to destroy and Christ who gave what was most precious defines the two contrasting models of covenant relationship"}
    ],
    "23": [
      {"type": "allusion", "target": "1 Sam 15:23", "note": "Samuel's equation of rebellion with divination and arrogance with idolatry is the OT grounding for Paul's argument that the unregenerate heart is in a state of fundamental hostility to God (Rom 8:7: 'the mind set on the flesh is hostile to God, for it does not submit to God's law') — Saul's partial obedience is the paradigm of the heart that acknowledges God in public while pursuing its own agenda in private"},
      {"type": "allusion", "target": "Rom 8:7", "note": "For rebellion is like the sin of divination, and insubordination like the iniquity of teraphim — Samuel identifies Saul's outward disobedience as spiritual idolatry; Paul's 'the mind set on the flesh is hostile to God' (Rom 8:7) is the NT extension: at root, all disobedience is self-worship, the substitution of one's own judgment for God's command"}
    ],
    "28": [
      {"type": "allusion", "target": "Acts 13:22", "note": "Samuel declares 'YHWH has torn the kingdom of Israel from you today and has given it to a neighbor of yours, who is better than you' — Paul in the Pisidian Antioch synagogue (Acts 13:22) names this transition: 'I have found in David the son of Jesse a man after my heart, who will do all my will'; the transfer from Saul (outward compliance, inward self-will) to David (inward alignment with YHWH's purposes) anticipates the transfer from the Mosaic administration to Christ who does 'all my will'"},
      {"type": "allusion", "target": "Heb 7:22", "note": "The kingdom torn from Saul and given to one 'better' points typologically to the superiority argument of Hebrews: Christ is 'better' than angels (Heb 1:4), better than Moses (Heb 3:3), better than Aaron (Heb 7:11), the guarantor of a 'better covenant' (Heb 7:22) — the OT pattern of replacement by the 'better' reaches its terminus in Christ who supersedes all that preceded him"}
    ],
    "29": [
      {"type": "allusion", "target": "Num 23:19", "note": "Samuel: 'The Glory of Israel will not lie or have regret, for he is not a man, that he should have regret' — this divine immutability saying echoes Num 23:19 ('God is not man, that he should lie, or a son of man, that he should change his mind'); the theological point is that YHWH's rejection of Saul is irrevocable, and his covenant promises are equally irrevocable — both rest on the same immutable divine character"},
      {"type": "allusion", "target": "Heb 6:17-18", "note": "YHWH's immutability (he does not 'relent' or 'lie') is the theological foundation of covenant confidence: Heb 6:17-18 ('So when God desired to show more convincingly to the heirs of the promise the unchangeable character of his purpose, he guaranteed it with an oath, so that by two unchangeable things... we who have fled for refuge might have strong encouragement') — the God who does not relent on Saul's rejection does not relent on his redemptive promises"}
    ]
  },
  "16": {
    "7": [
      {"type": "allusion", "target": "John 7:24", "note": "YHWH to Samuel: 'Do not look on his appearance or on the height of his stature... For YHWH sees not as man sees: man looks on the outward appearance, but YHWH looks on the heart' — Jesus applies this exact principle in John 7:24 ('Do not judge by appearances, but judge with right judgment') and it underlies his entire critique of Pharisaic religion: they optimize for appearances before men while YHWH sees the heart"},
      {"type": "allusion", "target": "2 Cor 5:16", "note": "YHWH's seeing the heart rather than the outward appearance (1 Sam 16:7) is the divine epistemology that Paul applies to the new covenant: 'from now on, therefore, we regard no one according to the flesh' (2 Cor 5:16) — the Spirit-enabled sight that sees past external qualifications to what God sees is the fulfillment of the divine perspective announced when David was anointed"},
      {"type": "allusion", "target": "Luke 16:15", "note": "The contrast between human and divine sight — man sees the outward, YHWH sees the heart — recurs in Jesus's statement to the Pharisees: 'You are those who justify yourselves before men, but God knows your hearts. For what is exalted among men is an abomination in the sight of God' (Luke 16:15); the YHWH-looking-on-the-heart principle of the anointing scene becomes a recurring motif of Jesus's critique of religious hypocrisy"}
    ]
  }
}

def main():
    e = load_echo('1samuel')
    merge_echo(e, ECHO)
    save_echo('1samuel', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'1samuel echo: wrote {count} verses across ch 15-16')

if __name__ == '__main__':
    main()
