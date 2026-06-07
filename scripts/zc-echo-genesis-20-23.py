"""
MKT Echo — Genesis chapters 20–23
Run: python3 scripts/zc-echo-genesis-20-23.py

Source data used:
- data/interlinear/genesis.json
- data/parallels/genesis.json (no entries for chs 20-23 to absorb)
- data/echoes/genesis.json (ch 21 has 3 entries, ch 22 has 5 entries — pre-existing; script adds ch 20 and 23)

Key decisions:
- Ch 20 (Abimelech narrative #2): v7 is the first OT use of "prophet" (nabi) — primarily
  notable for how God sovereignly protects the promise-line (Sarah must bear Isaac);
  echoes center on the preserved Abrahamic seed running forward to Christ and on
  Abraham's intercessory role anticipating priestly/prophetic mediation
- Ch 21 (Isaac's birth + Hagar expelled): pre-existing entries cover Heb 11 and Gal 4:29;
  script adds nothing — merge_echo will skip existing keys
- Ch 22 (Aqedah): pre-existing 5 entries; script adds nothing
- Ch 23 (Machpelah purchase): the patriarchs own only a tomb in the promised land —
  Heb 11:13-16 and Acts 7:5 are the direct NT commentary; the Machpelah purchase is
  a canonical down-payment on the full land-inheritance that arrives in Christ
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
  "20": {
    "1": [
      {"type": "theme", "target": "Rom 9:7",
       "note": "The Abimelech episode endangers Sarah — and therefore the promised seed — for the second time (the first is Gen 12:10-20 in Egypt). God sovereignly intervenes before Sarah is taken, preserving the Abrahamic line through which Isaac must come. Paul's 'through Isaac shall your offspring be named' (Rom 9:7) presupposes that this line was protected despite Abraham's failures; the promise-seed is God's doing, not Abraham's."}
    ],
    "7": [
      {"type": "allusion", "target": "Num 12:6",
       "note": "God tells Abimelech: 'He is a prophet (<em>nāḇî</em>), and he will pray for you' — this is the first occurrence of the word <em>nāḇî</em> (prophet) in the OT. The prophet's role here is intercessory: God speaks through Abraham to Abimelech, and Abraham prays for healing. Numbers 12:6 defines the prophetic office ('If there is a prophet among you, I the LORD make myself known to him in a vision') — Abraham's nocturnal divine encounter and intercessory prayer establish the prototype."},
      {"type": "shadow", "target": "Heb 7:25",
       "note": "Abraham's prayer for Abimelech (v. 7, fulfilled in v. 17) foreshadows Christ's permanent intercessory ministry: 'he always lives to make intercession for them' (Heb 7:25). Abraham as prophet-intercessor is one of the OT shadows of the one Mediator who prays for those who come to God through him (1 Tim 2:5)."}
    ],
    "12": [
      {"type": "theme", "target": "Matt 1:1",
       "note": "Abraham's disclosure that Sarah is indeed his half-sister (Gen 20:12) — true, but misleading — is part of the narrative context that makes the divine protection of Sarah all the more striking. The Matthean genealogy traces Jesus's line through Abraham (Matt 1:1-2); the protection of Sarah in Gerar, like the protection in Egypt, is the protection of the Messianic line at its most vulnerable."}
    ],
    "17": [
      {"type": "allusion", "target": "Jas 5:16",
       "note": "Abraham prayed to God and God healed Abimelech — the fulfilled intercession of Gen 20:17 grounds the principle James articulates: 'the prayer of a righteous person has great power as it is working' (Jas 5:16). Abraham is the paradigmatic righteous man whose prayer effects healing for a Gentile king, across the ethnic boundary that will only be fully broken down in Christ (Gal 3:28)."}
    ]
  },
  "23": {
    "1": [
      {"type": "allusion", "target": "Heb 11:13",
       "note": "Sarah's death at Hebron (v. 1-2) opens the Machpelah purchase narrative, which is the canonical expression of the patriarchs' alien-and-stranger status: 'These all died in faith, not having received the things promised, but having seen them and greeted them from afar, and having acknowledged that they were strangers and exiles on the earth' (Heb 11:13). Sarah is buried in the promised land without possessing it; the faith of the patriarchs consists precisely in this — dying without the promise fulfilled, but trusting the God who promised."}
    ],
    "4": [
      {"type": "fulfillment", "target": "Acts 7:5",
       "note": "Abraham's request — 'I am a sojourner and foreigner (<em>gēr-wĕtôšāb</em>) among you; give me property among you for a burying place' (v. 4) — is the exact situation Stephen cites in Acts 7:5: 'He gave him no inheritance in it, not even a foot's length, but promised to give it to him as a possession and to his offspring after him, when as yet he had no child.' Stephen reads Machpelah as proof that the patriarchal promise was not yet fulfilled in Abraham's lifetime; the land awaits its full-inheritance recipient."}
    ],
    "9": [
      {"type": "shadow", "target": "Eph 1:14",
       "note": "The cave of Machpelah purchased for 400 shekels of silver (v. 9-16) is the patriarchs' only concrete possession in Canaan — a tomb, not a homestead. This 'down payment' on the land is theologically resonant with Paul's description of the Spirit as 'the guarantee (<em>arrabōn</em>) of our inheritance' (Eph 1:14): the Spirit in this age is what Machpelah was for Abraham — the purchased first installment of the full inheritance that awaits the resurrection and new creation."}
    ],
    "19": [
      {"type": "theme", "target": "Heb 11:16",
       "note": "Abraham buries Sarah in the cave of Machpelah, in Hebron, in the land of Canaan (v. 19-20) — the patriarchs' dead are in the ground of the land they were promised. Hebrews 11:16 draws the theological conclusion: 'They desire a better country, that is, a heavenly one. Therefore God is not ashamed to be called their God, for he has prepared for them a city.' Machpelah is not the goal — it is the evidence of hope fixed on a city and country beyond what Abraham could possess in his lifetime."}
    ]
  }
}


def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)
    print('Genesis 20-23 echoes written.')

if __name__ == '__main__':
    main()
