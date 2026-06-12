"""
Echo Commentary — 1 Samuel chapters 19–21
Run: python3 scripts/zc-echo-1samuel-19-21.py

Ch19: Saul's escalating attempts to kill David; Jonathan protects David; David flees
Ch20: Jonathan and David's covenant; Jonathan's self-emptying loyalty to David
Ch21: David at Nob — the showbread (Jesus cites directly: Matt 12:3-4); David at Gath

Key OT↔NT connections:
- 20:14-15: Jonathan's covenant of hesed to David's descendants → Mephibosheth / Christ
- 21:6: The bread of the Presence given to David → Matt 12:3-4 (direct citation by Jesus)
- 20:31: Saul's hostility to David — "as long as Jesse's son lives, you have no kingdom"
  → echoes the rulers' hostility to Christ (John 11:48)
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
  "19": {
    "11": [
      {"type": "allusion", "target": "Matt 2:13", "note": "Michal warns David: 'If you do not escape with your life tonight, tomorrow you will be killed' — the pattern of the king's servants protecting him by night from a king who seeks his life echoes the Flight to Egypt: Joseph warned by the angel to flee with the child from Herod's murderous decree; in both cases the true king is hunted by the established power who fears displacement"},
      {"type": "allusion", "target": "John 7:1", "note": "Saul seeking to kill David while David moves through Israel in concealment is the pattern Jesus lives out in the Fourth Gospel: 'After this Jesus went about in Galilee. He would not go about in Judea, because the Jews were seeking to kill him' (John 7:1); the anointed king who is hunted by the established authorities before his hour comes is a recurring type, with Saul/David as its paradigmatic OT form"}
    ],
    "23": [
      {"type": "allusion", "target": "John 18:6", "note": "Saul strips off his clothes and prophesies before Samuel all day and all night — even the one pursuing David is involuntarily subdued by the Spirit's power. When the soldiers come to arrest Jesus, 'they drew back and fell to the ground' (John 18:6) at his self-identification; those who come to destroy the anointed are repeatedly overcome by a power they cannot control. The theme: the Spirit's presence around the anointed creates a zone of involuntary reverence that the adversary cannot simply override."}
    ]
  },
  "20": {
    "14": [
      {"type": "allusion", "target": "2 Sam 9:1", "note": "Jonathan's request — 'Show me the steadfast love (hesed) of YHWH, that I may not die... do not cut off your steadfast love from my house forever' — is fulfilled in 2 Sam 9:1 when David seeks out Jonathan's surviving son Mephibosheth and restores all of Saul's land to him. The covenant hesed that Jonathan requested becomes a type of Christ's covenant commitment to his people: the love that seeks out the crippled, the displaced, the one who expects only judgment, and restores them to the king's table (2 Sam 9:13)."},
      {"type": "allusion", "target": "Eph 2:12-13", "note": "Jonathan's covenant request — that David show hesed to his descendants even after Jonathan's death — is the OT form of the Gentiles being brought near by Christ's blood (Eph 2:12-13: 'you who were once far off have been brought near by the blood of Christ'); Mephibosheth was 'crippled in both feet,' dwelling in Lo-debar ('no pasture'), outside the city and outside the covenant — until David's covenant hesed sought him out"}
    ],
    "31": [
      {"type": "allusion", "target": "John 11:48", "note": "Saul's logic to Jonathan: 'As long as the son of Jesse lives on the earth, neither you nor your kingdom shall be established' — the calculus of those in power who see the anointed one as an existential threat to their position echoes the Sanhedrin's reasoning in John 11:48: 'If we let him go on like this, everyone will believe in him, and the Romans will come and take away both our place and our nation'; in both cases, the authorities' hostility to the anointed is motivated by self-preservation masked as concern for order"}
    ]
  },
  "21": {
    "3": [
      {"type": "allusion", "target": "Matt 12:3-4", "note": "David taking the bread of the Presence (lehem happanim) from Ahimelech — the consecrated bread reserved for priests — is directly cited by Jesus as precedent for the disciples picking grain on the Sabbath: 'Have you not read what David did when he was hungry... how he entered the house of God and ate the bread of the Presence, which it was not lawful for him to eat nor for those who were with him, but only for the priests?' (Matt 12:3-4). The citation is Christological: as David (the anointed king fleeing his enemies) superseded the ritual law by his authority and need, so Christ (the greater anointed king) supersedes Sabbath regulations by his authority — 'Something greater than the temple is here' (Matt 12:6)"},
      {"type": "allusion", "target": "Mark 2:25-26", "note": "Mark's version of Jesus's showbread argument (Mark 2:25-26) includes 'when Abiathar was high priest' — a historical note that has generated textual discussion (Ahimelech is the priest named in 1 Sam 21, Abiathar his son). The citation pattern in Mark shows Jesus treating the David narrative as living Scripture that illuminates his own situation: David as the rejected anointed king who receives covenant provision while fleeing Saul is the type Jesus applies to himself and his disciples as they move through Israel ahead of the authorities who will kill him"}
    ],
    "10": [
      {"type": "allusion", "target": "Phil 2:7", "note": "David at Gath conceals his identity and feigns madness — 'he changed his behavior before them and pretended to be insane' — to escape Achish king of Gath. The theme of the anointed king concealing his true identity and dignity in order to survive among enemies connects to Paul's kenosis language: Christ 'emptied himself, taking the form of a servant' (Phil 2:7) — not by pretense but by genuine incarnation. David's concealment is the type; Christ's self-humbling is the reality that the type shadows."}
    ]
  }
}

def main():
    e = load_echo('1samuel')
    merge_echo(e, ECHO)
    save_echo('1samuel', e)
    count = sum(len(v) for v in ECHO.values())
    print(f'1samuel echo: wrote {count} verses across ch 19-21')

if __name__ == '__main__':
    main()
