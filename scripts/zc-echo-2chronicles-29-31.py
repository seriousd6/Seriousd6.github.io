"""
MKT Echo Layer — 2 Chronicles chapters 29–31
Run: python3 scripts/zc-echo-2chronicles-29-31.py

Source data used:
- data/interlinear/2chronicles.json
- data/translation/draft/mediating/2chronicles.json

Key decisions:
- Ch29: Hezekiah's temple purification and rededication; v3 opens temple doors →
  Rev 3:7 (key of David); v24 sin offering for all Israel → Heb 9:26; v31 consecrate
  then draw near → Heb 10:22
- Ch30: Hezekiah's Passover; v5 the lapsed Passover → 1 Cor 5:7-8 (Christ our Passover);
  v9 YHWH will not turn face from returning people → Luke 15:20 (prodigal); v18-20
  Hezekiah's intercessory prayer for the ritually impure → Heb 4:14-16; v27 prayers
  reach heaven → Rev 8:3-4
- Ch31: Restoration of tithes; v4-5 supporting ministers for dedicated service →
  1 Cor 9:13-14; v10 surplus from faithful giving → 2 Cor 9:8; v20-21 wholehearted
  faithfulness in worship → John 4:23
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

CHRON2_ECHOES = {
  "29": {
    "3": [
      {
        "type": "allusion",
        "target": "Rev 3:7",
        "note": "Hezekiah's first act as king is to open the doors of the temple his father Ahaz had shut — in the first month of his reign, in the first year. In Rev 3:7 the risen Christ is described as 'the one who has the key of David, who opens and no one will shut, who shuts and no one opens.' Hezekiah's reopening of the closed sanctuary is a royal type of the risen Christ who has authority over access to the Father — the closed door of the temple is what Christ's death and resurrection definitively and permanently opens."
      }
    ],
    "11": [
      {
        "type": "theme",
        "target": "Rev 5:10",
        "note": "YHWH's direct address to the Levites through Hezekiah: 'Do not be negligent now, for the LORD has chosen you to stand before him, to serve him, to minister to him and burn incense.' The language of being chosen to stand before YHWH and serve is the priestly identity language that Rev 5:10 extends to all the redeemed: 'you have made them a kingdom and priests to our God, and they shall reign on the earth.' The Levitical calling to stand before God and serve in the sanctuary is the OT form of the universal royal priesthood Christ's blood purchases."
      }
    ],
    "24": [
      {
        "type": "type",
        "target": "Heb 9:26",
        "note": "The priests make a sin offering for all Israel — the king commanded that the burnt offering and sin offering be made 'for all Israel.' This comprehensive sin offering on behalf of the entire nation is the OT type of the eschatological sin offering Hebrews describes: 'he has appeared once for all at the end of the ages to put away sin by the sacrifice of himself' (Heb 9:26). Hezekiah's single purification offering to cover all Israel from Beersheba to Dan prefigures Christ's single sacrifice that definitively and exhaustively deals with the sin of God's people."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Heb 10:22",
        "note": "Hezekiah's invitation after the consecration rites: 'Now you have consecrated yourselves to the LORD; come near and bring sacrifices and thank offerings to the house of the LORD.' The pattern is consecration followed by the call to draw near. Heb 10:22 follows the same logic: 'let us draw near with a true heart in full assurance of faith, with our hearts sprinkled clean from an evil conscience.' The consecration-then-draw-near sequence Hezekiah enacts in the temple is precisely the argument of Hebrews about access to God through Christ's sacrifice — purification makes nearness possible."
      }
    ]
  },
  "30": {
    "5": [
      {
        "type": "allusion",
        "target": "1 Cor 5:7-8",
        "note": "The Chronicler notes that the Passover had not been kept as prescribed since the days of Solomon — a lapse of generations. Hezekiah's restoration of the Passover gives the narrative its urgency. Paul's declaration in 1 Cor 5:7-8 — 'Christ, our Passover lamb, has been sacrificed; let us therefore celebrate the festival' — is the NT fulfillment of Hezekiah's restoration. The national Passover that Hezekiah urgently convenes because it had been neglected finds its permanent, eschatological form in the Eucharistic celebration Paul describes, which is itself the once-for-all fulfillment of what Hezekiah restores."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Luke 15:20",
        "note": "The letter Hezekiah sends throughout all Israel includes the promise: 'For the LORD your God is gracious and merciful and will not turn his face from you, if you return to him.' The unconditional promise attached to the call to return — that YHWH will not refuse the one who turns back — is the OT warrant for Christ's parable of the returning son in Luke 15:20: 'while he was still a long way off, his father saw him and felt compassion, and ran and embraced him.' The father's unreserved welcome in the parable is the personal enactment of the covenant promise Hezekiah cites."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Heb 4:15-16",
        "note": "Hezekiah prays for the many people from Ephraim and Manasseh who ate the Passover without purifying themselves: 'May the good LORD pardon everyone who sets his heart to seek God, the LORD... even though not according to the sanctuary's rules of cleanness.' Hezekiah acts as intercessor for worshipers who came with sincere hearts but ritual impurity. This mediatorial intercession that bridges the gap between sincere seeking and cultic irregularity anticipates the NT high priest of Heb 4:15-16: 'one who in every respect has been tempted as we are, yet without sin... let us draw near to the throne of grace.'"
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Rev 8:3-4",
        "note": "The priests and Levites rise and bless the people at the Passover's conclusion, and the narrator reports: 'their prayer came to his holy habitation in heaven.' The priestly blessing ascending to the heavenly sanctuary is the earthly liturgy's climactic moment. Rev 8:3-4 shows the heavenly reality corresponding to this earthly pattern: 'the smoke of the incense, with the prayers of the saints, rose before God from the hand of the angel.' The prayer that ascended from Hezekiah's Passover liturgy is the type of the incense-prayer imagery Revelation uses for the eschatological intercession before the heavenly throne."
      }
    ]
  },
  "31": {
    "2": [
      {
        "type": "theme",
        "target": "1 Cor 12:28",
        "note": "Hezekiah re-established the divisions of the priests and Levites by their courses, assigning each to their designated function in the Lord's service. The organized, differentiated order of worship that Hezekiah restores is the OT form of the principle Paul articulates in 1 Cor 12:28: 'God has appointed in the church first apostles, second prophets, third teachers...' The Chronicler's emphasis on YHWH-ordered priestly structure corresponds to Paul's insistence that the church's differentiated ministry is divine appointment, not human invention."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "1 Cor 9:13-14",
        "note": "Hezekiah commanded the people of Jerusalem to give the portion due the priests and Levites, 'that they might give themselves to the Law of the LORD.' The logic is explicit: material support frees ministers for dedicated service to the word. Paul cites the same principle in 1 Cor 9:13-14: 'those who serve at the altar share in the sacrificial offerings; in the same way, the Lord commanded that those who proclaim the gospel should get their living by the gospel.' Paul's argument for ministerial support draws directly on the Levitical precedent Hezekiah enacts here."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "2 Cor 9:8",
        "note": "When Azariah the chief priest reports on the tithes brought to the storehouses he says: 'Since they began to bring the contributions into the house of the LORD, we have eaten and had enough and have plenty left, for the LORD has blessed his people.' The abundant surplus from faithful giving — eating to satisfaction with plenty remaining — is the pattern 2 Cor 9:8 universalizes: 'God is able to make all grace abound to you, so that having all sufficiency in all things at all times, you may abound in every good work.' The priestly surplus of Hezekiah's reform is the OT instance of the spiritual economics Paul describes."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "John 4:23",
        "note": "The Chronicler's summary of Hezekiah's reform: 'Thus Hezekiah did throughout all Judah, and he did what was good and right and faithful before the LORD his God... and he did it with all his heart, and prospered.' The completeness of Hezekiah's devotion — doing what is good, right, and faithful, with all his heart — anticipates Jesus' description of the worship the Father seeks: 'the true worshipers will worship the Father in spirit and truth, for the Father is seeking such people to worship him' (John 4:23). Hezekiah's whole-hearted, truth-ordered worship is the OT approximation of the spirit-and-truth worship the new covenant makes fully possible."
      }
    ]
  }
}

def main():
    existing = load_echo('2chronicles')
    merge_echo(existing, CHRON2_ECHOES)
    save_echo('2chronicles', existing)
    print('2 Chronicles 29–31 echoes written.')

if __name__ == '__main__':
    main()
