"""
Echo layer — Isaiah chapters 48–52
Run: python3 scripts/zc-echo-isaiah-48-52.py

Chapters 49 and 52 already have entries; this script adds missing chapters 48, 50, 51.

Key echo decisions:
- Isa 48:12 "I am the first and I am the last" → Rev 1:17; Rev 22:13 (fulfillment —
  Jesus claims this divine title verbatim).
- Isa 50:6 (Third Servant Song) → Matt 26:67; John 19:1 (fulfillment — striking,
  spitting at the passion directly match the Servant's self-description).
- Isa 50:8 "He who vindicates me is near" → Rom 8:33-34 (Paul quotes the logic of
  this challenge verbatim as the basis for no-condemnation in Christ).
- Isa 51:6 "my salvation will be forever" → Heb 1:11-12 (heavens wearing out
  contrasted with the eternal Christ; cf. Ps 102:26 which Hebrews also quotes).
- Isa 51:17/22 cup of wrath / cup removed → Matt 26:39; 2 Cor 5:21 (Christ drinks
  the cup of judgment so it is taken from his people).
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

ISAIAH_ECHOES = {
  "48": {
    "12": [
      {
        "type": "fulfillment",
        "target": "Rev 1:17",
        "note": "Jesus says 'I am the first and the last' to John on Patmos, directly claiming YHWH's self-identification from Isa 48:12; the same formula recurs in Rev 2:8 and Rev 22:13 ('the first and the last, the beginning and the end'), anchoring Christ's eternal divine identity in Isaiah's monotheistic claim."
      },
      {
        "type": "fulfillment",
        "target": "Rev 22:13",
        "note": "The risen Christ's final self-description — 'I am the Alpha and the Omega, the first and the last, the beginning and the end' — is the fullest NT expansion of Isa 48:12's formula, identifying the returning Lord as the eternal God who called Israel from the beginning."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Luke 4:18",
        "note": "Isa 48:16b 'the Lord GOD has sent me, and his Spirit' is the Servant's claim to be Spirit-sent by the Father — the same Trinitarian structure Christ enacts when he reads from Isa 61:1-2 in the Nazareth synagogue ('The Spirit of the Lord is upon me, because he has anointed me... he has sent me')."
      }
    ]
  },
  "50": {
    "6": [
      {
        "type": "fulfillment",
        "target": "Matt 26:67",
        "note": "The Servant's 'I gave my back to those who strike, and my cheeks to those who pull out the beard; I hid not my face from disgrace and spitting' is fulfilled at Jesus's trial and passion — Matt 26:67 (spit on and struck) and John 19:1 (flogged) enact this self-offering verse by verse."
      },
      {
        "type": "fulfillment",
        "target": "John 19:1",
        "note": "The flogging of Jesus by Pilate's soldiers directly fulfills 'I gave my back to those who strike' (Isa 50:6); Peter cites the Servant Songs as a unified passion narrative in 1 Pet 2:22-25, confirming that the early church read Isa 50 as messianic prophecy."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Rom 8:33",
        "note": "Paul's 'Who shall bring any charge against God's elect? It is God who justifies' echoes the Servant's courtroom challenge in Isa 50:8 ('He who vindicates me is near. Who will contend with me?'); the forensic logic — vindication by God making every accusation unanswerable — is carried directly into Paul's no-condemnation declaration for those in Christ."
      }
    ]
  },
  "51": {
    "6": [
      {
        "type": "shadow",
        "target": "Heb 1:11",
        "note": "Isa 51:6 'the heavens will vanish like smoke, the earth will wear out like a garment' is part of the same tradition that Hebrews quotes from Ps 102:26 when proving Christ's eternal immutability — the perishing creation is contrasted with the eternal Son who 'remains' and whose 'years will have no end' (Heb 1:11-12)."
      },
      {
        "type": "shadow",
        "target": "2 Pet 3:10",
        "note": "Peter's description of the day of the Lord — 'the heavens will pass away with a roar and the heavenly bodies will be burned up and dissolved' — draws on the same cosmic dissolution imagery as Isa 51:6, both contrasting the passing creation with the eternal salvation that Christ secures."
      }
    ],
    "12": [
      {
        "type": "shadow",
        "target": "John 14:16",
        "note": "YHWH's 'I, I am he who comforts you' (Isa 51:12) prefigures Christ's promise of 'another Helper' (Parakletos) — the Spirit of comfort sent in Christ's name (John 14:16-17,26). The personal divine comfort that Isaiah declares becomes the Trinitarian comfort of the new covenant, mediated through Christ and actualized by the Spirit."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Matt 26:39",
        "note": "Isa 51:17 'You who have drunk from the hand of the LORD the cup of his wrath' and v.22 'I have taken from your hand the cup of staggering' together form the OT template for Christ's Gethsemane prayer ('let this cup pass from me') and his voluntary drinking of it — Christ drained the cup of divine judgment so that it could be removed from his people (Isa 51:22-23)."
      }
    ]
  }
}

def main():
    existing = load_echo('isaiah')
    merge_echo(existing, ISAIAH_ECHOES)
    save_echo('isaiah', existing)
    # INTENT: Verify that previously missing chapters 48, 50, 51 now have echo entries
    # CHANGE? If isaiah.json echoes structure changes, update merge_echo dedup logic
    # VERIFY: ch 48 v12, ch 50 v6, ch 51 v6 all present in data/echoes/isaiah.json
    out = json.loads((ROOT / 'data' / 'echoes' / 'isaiah.json').read_text())
    for ch, vv in [('48', ['12', '16']), ('50', ['6', '8']), ('51', ['6', '12', '17'])]:
        for v in vv:
            count = len(out.get(ch, {}).get(v, []))
            print(f'  ch {ch} v{v}: {count} entries')

if __name__ == '__main__':
    main()
