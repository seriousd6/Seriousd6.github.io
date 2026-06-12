"""
Echo Layer — 1 Chronicles chapters 19–22
Run: python3 scripts/zc-echo-1chronicles-19-22.py

Key echo connections in this range:
- 19:13: Joab's warrior call → 1 Cor 16:13
- 20:8: defeat of giant enemies → Col 2:15
- 21:1: Satan incites census (cf. 2 Sam 24 says LORD) → 1 Pet 5:8; Job 1:6
- 21:15-16: angel stayed at threshing floor → Heb 9:26
- 21:26: fire from heaven on altar → Heb 9:11-12
- 22:1: threshing floor declared as temple site → John 2:19-21; 1 Cor 3:16
- 22:8-10: warrior-king cannot build; man of peace (Solomon) will → Eph 2:14-17
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

CHRON1_ECHO_19_22 = {
  "19": {
    "2": [
      {"type": "allusion", "target": "2 Cor 5:20", "note": "David sends emissaries to Hanun with an offer of covenant kindness, but they are suspected of espionage and humiliated; Paul describes believers as ambassadors of reconciliation (2 Cor 5:20) whose message is similarly rejected — the pattern of rejected covenant overtures runs from David's envoys through the rejected prophets to the rejected Christ (Matt 23:37)"}
    ],
    "13": [
      {"type": "allusion", "target": "1 Cor 16:13", "note": "Joab's battle-speech — 'Be strong and let us show ourselves courageous for our people and for the cities of our God, and may the LORD do what is good in his sight' — is the OT warrior exhortation that Paul transmutes into spiritual warfare: 'Be watchful, stand firm in the faith, act like men, be strong' (1 Cor 16:13); the same call to courage for the sake of God's people appears in the new covenant context of spiritual rather than military battle"}
    ]
  },
  "20": {
    "4": [
      {"type": "shadow", "target": "Col 2:15", "note": "The chronicle of victories over the giants of Gath (vv. 4–8) — each named enemy felled by a Davidite warrior — is a shadow of Christ's definitive victory over the spiritual powers: 'He disarmed the rulers and authorities and put them to open shame, triumphing over them in him' (Col 2:15); as the Davidic son conquered every giant the Philistines could field, so David's greater Son defeats every spiritual adversary"}
    ]
  },
  "21": {
    "1": [
      {"type": "allusion", "target": "Job 1:6", "note": "1 Chr 21:1 deliberately replaces 2 Sam 24:1 ('the LORD incited David') with 'Satan stood against Israel and incited David' — an editorial decision that exposes the behind-the-scenes adversary theology: as in Job 1:6, Satan operates within God's sovereign permission but is the proximate instigator of the human pride that becomes sin; this same theology culminates in Zech 3:1 and in Jesus' warning to Peter (Luke 22:31: Satan demanded to sift you like wheat)"},
      {"type": "allusion", "target": "1 Pet 5:8", "note": "Chronicles' naming of Satan as the one who incited the census-pride contributes to the biblical trajectory that ends in Peter's warning: 'Your adversary the devil prowls around like a roaring lion, seeking someone to devour' (1 Pet 5:8); the census is a military-strength audit — a counting of swords rather than a trust in YHWH — exactly the kind of proud self-reliance Satan exploits"}
    ],
    "15": [
      {"type": "type", "target": "Heb 9:26", "note": "The angel of the LORD stops the plague at the threshing floor of Ornan the Jebusite — staying divine judgment at a specific site that becomes the permanent place of atonement (22:1 declares it the future temple site); the spatial logic runs forward to Christ, who 'appeared once for all at the end of the ages to put away sin by the sacrifice of himself' (Heb 9:26): as the plague was arrested at the place of sacrifice, so the judgment against humanity is arrested at the cross"}
    ],
    "26": [
      {"type": "allusion", "target": "Heb 9:11-12", "note": "YHWH answers David's altar on Araunah's threshing floor with fire from heaven — divine acceptance of the sacrifice that stayed the plague; the author of Hebrews sees Christ's self-offering as the antitype of every such divine-fire acceptance: 'he entered once for all into the holy places, not by means of the blood of goats and calves but by means of his own blood, thus securing an eternal redemption' (Heb 9:11-12); the fire that fell on David's altar is replaced by the Spirit (Acts 2:3) and the Father's acceptance of the Son's sacrifice"}
    ]
  },
  "22": {
    "1": [
      {"type": "allusion", "target": "John 2:19", "note": "David's declaration — 'This is the house of the LORD God, and this is the altar of burnt offering for Israel' — consecrates the threshing floor as the temple site; Jesus applies the same logic to his own body ('Destroy this temple, and in three days I will raise it up', John 2:19), and the NT extends it to the church as the living temple (1 Cor 3:16-17; Eph 2:21-22): the place where sacrifice is made and accepted is the place where God dwells among his people"}
    ],
    "8": [
      {"type": "shadow", "target": "Eph 2:14", "note": "YHWH tells David he cannot build the temple because he has shed much blood; the temple will be built by Solomon — whose name means peace (shalom) — a man of rest and quiet given by YHWH (v. 9); the shadow points to Christ who 'is our peace' (Eph 2:14) and whose blood-shedding paradoxically enables the peace that the warrior-king's blood-shedding prevented: the cross is simultaneously the ultimate blood-shedding and the act that establishes the permanent dwelling of God among his people (Rev 21:3)"}
    ]
  }
}

def main():
    existing = load_echo('1chronicles')
    merge_echo(existing, CHRON1_ECHO_19_22)
    save_echo('1chronicles', existing)
    print('1 Chronicles 19-22 echo layer written.')

if __name__ == '__main__':
    main()
