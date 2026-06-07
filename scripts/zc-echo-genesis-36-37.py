"""
Echo Layer — Genesis chapters 36–37
Run: python3 scripts/zc-echo-genesis-36-37.py

Key echo trajectories:
- Gen 36 (Edomite genealogy): sparse but real — the Esau/Edom line points to the Jacob/Israel
  election (Rom 9:13; Mal 1:2-3); the Edomite kings (36:31) anticipate Israel's kingship and
  the coming David (Num 24:17-19); Obadiah and the prophets develop the Edom theme eschatologically
- Gen 37 (Joseph betrayed):
  - v4-5: brothers' hatred without cause → John 15:18-19 (world hates Christ, then disciples)
  - v18: conspiracy to kill → John 11:53; Ps 2:2
  - v24: thrown into the pit → Ps 40:2; Jonah 2:6 (pit/death/resurrection pattern)
  - v26-27: Judah's role in the betrayal → anticipates Judas (Matt 26:15)
  - v28: sold for 20 shekels → Matt 26:15 (30 pieces of silver; price of a slave in both cases)
  - v36: descent into Egypt/prison → Phil 2:8-9 (humiliation before exaltation)
  - Existing echoes: v3 [fulfillment] John 3:35; v28 [type] Acts 7:9 — not duplicated here
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
  "36": {
    "1": [
      {"type": "shadow", "target": "Rom 9:13", "note": "The toledot of Esau (that is, Edom) opens with the covenant line explicitly passing to Jacob, not Esau — a choice Paul addresses directly in Rom 9:13 (citing Mal 1:2-3): 'Jacob I loved, but Esau I hated.' The Edomite genealogy in ch 36 documents the flourishing of the non-elect line — Esau has chiefs, kings, and prosperity — making it plain that divine election is not about earthly advantage but about the covenant purpose through which blessing ultimately reaches all nations."}
    ],
    "31": [
      {"type": "shadow", "target": "Num 24:17", "note": "'These are the kings who reigned in the land of Edom, before any king reigned over the Israelites' (36:31) — the editorial note anticipates Israel's eventual kingship and places the Edomite kings as precedents. Balaam's oracle (Num 24:17-19) predicts a star from Jacob who will 'crush the forehead of Moab' and 'destroy all the sons of Sheth' — Edom will 'be dispossessed' (Num 24:18). The Edomite king-list frames the story that will culminate in David conquering Edom (2 Sam 8:14) and ultimately in the King of kings from Judah (Rev 19:16)."},
      {"type": "shadow", "target": "Obad 1:1", "note": "The Edomite genealogy and king-list (36:1-43) establishes Esau's descendants as a nation in their own right. The book of Obadiah is entirely devoted to the judgment of Edom for its pride and its role in Israel's suffering. Eschatologically (Obad 1:21: 'saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's'), Edom becomes the cipher for all that opposes God's kingdom — as Babylon does in Revelation — pointing toward the universal reign of the Lamb."}
    ]
  },
  "37": {
    "4": [
      {"type": "shadow", "target": "John 15:18", "note": "Joseph's brothers 'hated him and could not speak peaceably to him' (37:4) — hatred without a rational cause, driven purely by envy of the father's favor. Jesus applies this pattern to himself and his disciples: 'if the world hates you, know that it has hated me before it hated you... they hated me without a cause' (John 15:18, 25, citing Ps 35:19). The Joseph narrative structures the dynamic: divine favor provoking hatred from one's own family/people, leading to rejection and suffering that becomes the mechanism of salvation."}
    ],
    "5": [
      {"type": "shadow", "target": "Rev 12:1", "note": "Joseph's first dream — sheaves bowing to his sheaf — and his second — the sun, moon, and eleven stars bowing to him (37:9) — establish the prophetic pattern of cosmic imagery (sun, moon, stars) representing the covenant family. Rev 12:1 ('a woman clothed with the sun, with the moon under her feet, and on her head a crown of twelve stars') directly absorbs this imagery: the twelve stars = the twelve tribes = the twelve apostles, making the connection between Joseph's prophetic dream and the church's cosmic identity explicit."}
    ],
    "18": [
      {"type": "shadow", "target": "John 11:53", "note": "'They conspired against him to kill him' (37:18) — the brothers' murder-plot against Joseph uses the same conspiratorial pattern as the Sanhedrin's resolution against Jesus: 'they made plans to put him to death' (John 11:53). Ps 2:2 ('the kings of the earth set themselves, and the rulers take counsel together, against the LORD and against his Anointed') gives the theological grammar: opposition to the chosen one arises from those who should recognize him, driven by the same fear-of-displacement that drove Joseph's brothers."}
    ],
    "24": [
      {"type": "shadow", "target": "Ps 40:2", "note": "Joseph thrown into the pit — 'the pit was empty; there was no water in it' (37:24) — the pit (<em>bôr</em>) is the Hebrew term for both cistern and the underworld/death (Ps 28:1; 30:3; 88:4-6). Ps 40:2 ('he drew me up from the pit of destruction, out of the miry bog') is David's language for deliverance from near-death, which the NT applies to Christ's resurrection (Heb 10:5-7 quotes Ps 40 of Christ). The empty waterless pit where Joseph is left to die is the type of the tomb from which the true Joseph is drawn up on the third day."},
      {"type": "shadow", "target": "Jonah 2:6", "note": "Joseph in the waterless pit (37:24) is the structural forerunner of Jonah in the belly of the fish, who cries: 'you brought up my life from the pit (<em>bôr</em>)' (Jonah 2:6). Jesus explicitly identifies himself with Jonah: 'as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth' (Matt 12:40). The pit-to-pit-to-tomb chain of types converges on the resurrection."}
    ],
    "26": [
      {"type": "shadow", "target": "Matt 26:14", "note": "Judah (Hebrew form of the name Judas) proposes selling Joseph rather than killing him (37:26-27) — 'let not our hand be upon him, for he is our brother, our own flesh.' Judas of Iscariot (from the tribe of Judah) proposes selling Jesus for thirty pieces of silver (Matt 26:14-15). The verbal parallel — a 'Judah' figure brokering the sale of the beloved son — is structural: in both cases, the sale that seems to remove the threatened one becomes the mechanism of salvation for the very ones who arranged the sale (Acts 2:23: 'according to the definite plan and foreknowledge of God')."}
    ],
    "28": [
      {"type": "shadow", "target": "Matt 26:15", "note": "Joseph sold for twenty pieces of silver (37:28) — the price of a slave in the Mosaic law (Lev 27:5: the valuation of a male 5-20 years old). Jesus is betrayed for thirty pieces of silver (Matt 26:15; Zech 11:12-13) — the price of a slave gored by an ox (Exod 21:32). Both are 'slave-prices' — the contemptible valuation placed on the beloved son by those who sold him. The escalation from 20 to 30 and the Zechariah-Judas connection (Matt 27:9-10) deepens the typological identification."}
    ],
    "36": [
      {"type": "type", "target": "Phil 2:8", "note": "Joseph sold to Potiphar in Egypt (37:36) — the descent of the beloved, favored son into slavery in a foreign land begins the humiliation-exaltation arc that is the structural heart of the Joseph narrative. Paul's Christ-hymn follows the same arc: 'he humbled himself by becoming obedient to the point of death... therefore God has highly exalted him' (Phil 2:8-9). The Joseph type makes clear that the humiliation is not an accident but a necessary passage through which the exaltation comes — the pit precedes the throne."}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    for ch in [36, 37]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    total = len(result)
    print(f'  Genesis total: {total} chapters with echo data')
    print('Genesis 36-37 echoes written.')

if __name__ == '__main__':
    main()
