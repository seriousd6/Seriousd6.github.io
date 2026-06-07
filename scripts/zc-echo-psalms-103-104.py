"""
MKT Echo Layer — Psalms chapters 103–104
Run: python3 scripts/zc-echo-psalms-103-104.py

Psalm 103 (David): The great psalm of forgiveness and divine compassion.
  v3 forgives+heals→Luke 5:24/Acts 10:38; v8 Exod 34:6 formula→Jas 5:11/2 Pet 3:9;
  v12 east-from-west→Heb 10:17; v13 father-pities→Luke 15:20; v15→1 Pet 1:24 (quote);
  v17 steadfast-love→John 3:16; v19 throne-rules-all→Rev 11:15.
Psalm 104: Already has Heb 1:7 entry (v4); chapter is done by echo standards.
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

PSALMS_ECHOES = {
  "103": {
    "3": [
      {
        "type": "allusion",
        "target": "Luke 5:24",
        "note": "Verse 3 — 'who forgives all your iniquity, who heals all your diseases' — pairs forgiveness and healing as twin acts of divine mercy. When Jesus heals the paralytic and declares his sins forgiven (Luke 5:24), his opponents object; Jesus appeals to visible healing as evidence of invisible forgiveness — the same pairing Ps 103 presents as God's dual gift. Christ does in his body what the psalm attributes to God alone."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Jas 5:11",
        "note": "Verse 8 — 'The LORD is merciful and gracious, slow to anger and abounding in steadfast love' — is the canonical restatement of Exod 34:6, the divine name proclamation. James 5:11 draws on this same formula ('the Lord is compassionate and merciful') to encourage endurance. The NT consistently appeals to this character-declaration of God — merciful, patient, loyal — as the ground of confidence in suffering, now known to be definitively expressed in Christ (2 Cor 1:3)."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Rom 5:8",
        "note": "Verse 10 — 'He does not deal with us according to our sins, nor repay us according to our iniquities' — declares the mercy-gap between what God could give and what he actually gives. Rom 5:8 identifies the basis of this gap: 'God shows his love for us in that while we were still sinners, Christ died for us.' The psalm announces the gap; Paul explains it — the reason God does not repay as deserved is the substitution accomplished at the cross."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Heb 10:17",
        "note": "Verse 12 — 'as far as the east is from the west, so far does he remove our transgressions from us' — is the OT's strongest statement of complete forgiveness. Heb 10:17 quotes the new covenant promise of Jer 31:34 to the same effect: 'I will remember their sins and their lawless deeds no more.' East-from-west is infinite distance; Christ's blood achieves what the psalm promises — not just covered but removed, not just pardoned but forgotten by God."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Luke 15:20",
        "note": "Verse 13 — 'As a father shows compassion to his children, so the LORD shows compassion to those who fear him' — is the image Jesus presses to its limit in the parable of the prodigal son. Luke 15:20 depicts the father who 'saw him while he was still a long way off, and felt compassion, and ran and embraced him and kissed him.' Jesus does not invent this image of God as compassionate father; he takes the picture Ps 103 sketches and draws it to the most extravagant possible conclusion."
      }
    ],
    "15": [
      {
        "type": "quote",
        "target": "1 Pet 1:24",
        "note": "Verses 15-16 — 'As for man, his days are like grass; he flourishes like a flower of the field; for the wind passes over it, and it is gone' — are directly quoted in 1 Pet 1:24 to contrast the perishable with the imperishable: 'All flesh is like grass and all its glory like the flower of grass. The grass withers, and the flower falls, but the word of the Lord remains forever.' Peter cites Ps 103 to ground the permanence of the Gospel message against the fragility of human life."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "John 3:16",
        "note": "Verse 17 — 'But the steadfast love of the LORD is from everlasting to everlasting on those who fear him' — declares that God's <em>hesed</em> has no beginning and no end. John 3:16 names the event in which this eternal love erupted into time: 'God so loved the world that he gave his only Son.' The everlasting love Ps 103 celebrates is the same love whose historical expression was the Incarnation and the cross."
      }
    ],
    "19": [
      {
        "type": "theme",
        "target": "Rev 11:15",
        "note": "Verse 19 — 'The LORD has established his throne in the heavens, and his kingdom rules over all' — is the Psalter's declaration of divine sovereignty over all creation. Rev 11:15 announces its eschatological consummation: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever.' The reign Ps 103 declares in heaven becomes, through Christ's resurrection and exaltation, the reign that fills earth."
      }
    ]
  }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 103-104 echoes written.')

if __name__ == '__main__':
    main()
