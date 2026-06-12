"""
MKT Echo — 1 Samuel chapters 25–27
Run: python3 scripts/zc-echo-1samuel-25-27.py

Ch 25: Samuel dies; Nabal the fool; Abigail the intercessor; David spared from blood-guilt.
Ch 26: David spares Saul a second time; the divine sleep; the inviolable anointed.
Ch 27: David's exile in Philistia; Ziklag; sojourner theology.

Echo anchors:
- Ch25: Samuel's death → Matt 11:11; Nabal = fool → Luke 12:20; Abigail mediates → Heb 7:25;
        bundle of the living → John 10:28; Abigail's "remember me" → Luke 23:42; YHWH strikes → Heb 10:31
- Ch26: Abishai's sword restrained → John 18:10; divine sleep → Matt 28:4; repayment → Matt 16:27
- Ch27: exile among enemies → Heb 11:13; Ziklag sojourn → 1 Pet 1:1
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

ECHOES = {
  "25": {
    "1": [
      {"type": "allusion", "target": "Matt 11:11", "note": "Samuel dies and all Israel assembles to mourn him — the prophet who anointed two kings, interceded at Mizpah, and served as YHWH's voice throughout the transition to monarchy is given a national funeral at Ramah. The mourning of all Israel for Samuel echoes Jesus's own eulogy of John the Baptist, the last prophet: 'Among those born of women there has arisen no one greater than John the Baptist' (Matt 11:11). Both Samuel and John are the prophetic figures whose work culminates in pointing to the anointed king; both die before that king's full vindication arrives."}
    ],
    "25": [
      {"type": "allusion", "target": "Luke 12:20", "note": "Nabal's very name means 'fool' (<em>nāḇāl</em>), and Abigail acknowledges it: 'Let not my lord regard this worthless fellow Nabal, for as his name is, so is he. Nabal is his name and folly is with him.' The man who withholds generosity from the anointed king, feasts lavishly while dismissing the claims of YHWH's appointed, and trusts his accumulated wealth is the OT type of Jesus's parable: 'Fool! This night your soul is required of you, and the things you have prepared, whose will they be?' (Luke 12:20). Nabal's name is the indictment the parable pronounces."}
    ],
    "29": [
      {"type": "allusion", "target": "John 10:28", "note": "Abigail intercedes for David and delivers a theological oracle: 'The life (<em>nepeš</em>) of my lord shall be bound in the bundle of the living (<em>ṣərôr haḥayyîm</em>) in the care of YHWH your God, and the lives of your enemies he shall sling out as from the hollow of a sling.' The image of YHWH binding and keeping the lives of his anointed in a protective bundle is the OT idiom behind Jesus's promise: 'I give them eternal life, and they will never perish, and no one will snatch them out of my hand' (John 10:28). The 'bundle of the living' is the prototype of the Father's hand from which no one can snatch the elect."}
    ],
    "31": [
      {"type": "theme", "target": "Luke 23:42", "note": "Abigail's final petition to David: 'And when YHWH has dealt well with my lord, then remember your servant (<em>zəḵartāh ʾeṯ-ʾămaṯeḵā</em>).' The request to be remembered when the king comes into his kingdom is the same structure as the dying thief's petition: 'Jesus, remember me when you come into your kingdom' (Luke 23:42). In both cases a suppliant at the edge of judgment, having acknowledged the king's authority and righteousness, asks only to be remembered. The king's favorable response — David immediately receives Abigail into his protection; Jesus grants the thief paradise — is the same pattern of sovereign grace responding to humble petition."}
    ],
    "38": [
      {"type": "theme", "target": "Heb 10:31", "note": "YHWH struck Nabal and he died — divine judgment vindicated David without his own hand being stained with blood. The story's structural point is that YHWH is the avenger of the anointed king: Abigail had kept David from taking vengeance, and YHWH executed it instead. This is the OT ground of Paul's 'Vengeance is mine, I will repay, says the Lord' (Rom 12:19) and Hebrews' 'It is a fearful thing to fall into the hands of the living God' (Heb 10:31). YHWH's direct judgment of Nabal demonstrates that relinquishing vengeance to YHWH is not weakness but eschatological faith."}
    ]
  },
  "26": {
    "8": [
      {"type": "theme", "target": "John 18:10", "note": "Abishai urges David to let him strike Saul with the spear — 'I will not strike him twice' — and David restrains him: 'Do not destroy him, for who can put out his hand against YHWH's anointed and be guiltless?' The restraint of the sword by the anointed one whose life is also under threat mirrors the Gethsemane scene: Peter draws his sword to defend Jesus, and Jesus says 'Put your sword back into its sheath' (John 18:10-11). In both scenes the true king declines the violence his defender offers, choosing divine vindication over human force as the path of the anointed."}
    ],
    "12": [
      {"type": "allusion", "target": "Matt 28:4", "note": "A deep sleep from YHWH (<em>tarḏēmāh YHWH</em>) fell upon Saul and his camp — the divine stupor that protected David and enabled him to take the spear and water jug without any man seeing, knowing, or waking. The theophanic sleep that falls on those around YHWH's anointed when he passes through in safety echoes the guards at the tomb who 'trembled and became like dead men' (Matt 28:4) at the resurrection. In both scenes, divine agency overrides human watchfulness to protect or vindicate the anointed one — the enemies cannot prevent what YHWH purposes."}
    ],
    "23": [
      {"type": "allusion", "target": "Matt 16:27", "note": "David declares: 'YHWH repays every man according to his righteousness and his faithfulness (<em>ṣidqātô weʾĕmunātô</em>), for YHWH gave you into my hand today, and I would not put out my hand against YHWH's anointed.' The principle of divine repayment according to covenant faithfulness is the OT form of Jesus's eschatological promise: 'The Son of Man is going to come with his angels in the glory of his Father, and then he will repay each person according to what he has done' (Matt 16:27). David's restraint is grounded in eschatological conviction: YHWH sees, YHWH will repay, human usurpation of divine judgment is faithlessness."}
    ]
  },
  "27": {
    "1": [
      {"type": "theme", "target": "Heb 11:13", "note": "David's monologue of faith-crisis: 'Now I shall perish one day by the hand of Saul. There is nothing better for me than that I should escape to the land of the Philistines.' The anointed king of Israel becomes a voluntary exile among his people's enemies — living as a sojourner (<em>gēr</em>) in Philistine territory. The pattern of the anointed forced into exile when rejected by his own (Joseph to Egypt, Moses to Midian, David to Philistia, Jesus to Egypt) is the OT theology of sojourning that Hebrews articulates: the patriarchs 'acknowledged that they were strangers and exiles on the earth' (Heb 11:13). David's Philistine exile is the anointed king's wilderness passage before his throne."}
    ],
    "5": [
      {"type": "allusion", "target": "1 Pet 1:1", "note": "David asks Achish for Ziklag — a border town on the margins — so he will not have to live in the Philistine royal city; he chooses the periphery, maintaining his distinct identity while resident in enemy territory. David's voluntary descent to the margins in a hostile kingdom, keeping his covenant identity alive while navigating a pagan court, is the structural pattern Peter applies to the church: 'the elect exiles of the Dispersion' (1 Pet 1:1). Both communities hold their true identity in tension with their resident alien status, living faithfully at the margins of an empire that does not recognize their true king."}
    ]
  }
}

def main():
    existing = load_echo('1samuel')
    merge_echo(existing, ECHOES)
    save_echo('1samuel', existing)
    print('1samuel ch 25-27: echoes written')

if __name__ == '__main__':
    main()
