"""
MKT Echo — Genesis chapters 33–35
Run: python3 scripts/zc-echo-genesis-33-35.py

Source data used:
- data/interlinear/genesis.json
- data/parallels/genesis.json (no entries for chs 33-35)
- data/echoes/genesis.json (all three chapters missing; ch 37 has 2 entries pre-existing)

Key decisions:
- Ch 33 (Jacob-Esau reconciliation): v4 (Esau runs to embrace Jacob) is the most
  significant echo target — Luke 15:20 deliberately echoes this scene in the
  parable of the prodigal son; the geographic purchase of Shechem (v19) points
  forward to John 4 (Jesus at Sychar/Shechem)
- Ch 34 (Dinah/Shechem): few direct NT quotes; strongest echoes are geographic
  (John 4 at Sychar = Shechem) and typological (Levi's violence → later redemption
  to priesthood); Jacob's rebukes of Simeon and Levi anticipate Gen 49:5-7
- Ch 35 (Bethel covenant + Benjamin's birth): v18 (Benjamin = 'son of the right
  hand') is the strongest Christological shadow; v10-12 covenant renewal grounds
  the Israel-genealogy of Christ; v4 (burying foreign gods) echoes NT repentance
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
  "33": {
    "4": [
      {"type": "allusion", "target": "Luke 15:20",
       "note": "Esau ran to meet Jacob, embraced him, fell on his neck, and kissed him (Gen 33:4) — this scene is the literary template for the father's reception of the prodigal son: 'While he was still a long way off, his father saw him and felt compassion, and ran and embraced him and kissed him' (Luke 15:20). The identical sequence (ran, embraced, kissed, wept/rejoiced) shows Jesus drawing on the Jacob-Esau reconciliation as the image of divine welcome after estrangement — the father in the parable acts as Esau did, not as an offended creditor."}
    ],
    "10": [
      {"type": "shadow", "target": "2 Cor 4:6",
       "note": "Jacob says to Esau: 'To see your face is like seeing the face of God, for you have received me with such favor' (Gen 33:10). The language of seeing the face of God in a human face foreshadows Paul's Christological statement: 'the light of the knowledge of the glory of God in the face of Jesus Christ' (2 Cor 4:6). Jacob glimpses something of the divine in Esau's gracious reception; the full revelation of God's face comes only in Christ."}
    ],
    "19": [
      {"type": "allusion", "target": "John 4:5",
       "note": "Jacob buys a plot of ground at Shechem from the sons of Hamor (Gen 33:19) — the same land that becomes the location of John 4: 'a city of Samaria called Sychar, near the field that Jacob had given to his son Joseph' (John 4:5). Jesus's conversation with the Samaritan woman at Jacob's well takes place on the ground purchased in this verse; the living water Jesus offers (John 4:10-14) is given in the place where Jacob had settled and where Shechem's violence against Dinah would occur (ch. 34)."}
    ]
  },
  "34": {
    "2": [
      {"type": "theme", "target": "John 4:9",
       "note": "The Shechem narrative (Gen 34) takes place in the territory that becomes Samaria. Jesus's conversation at Sychar (John 4:9) — 'How is it that you, a Jew, ask for a drink from me, a woman of Samaria?' — is set against the long history of hostility between Jews and Samaritans rooted in part in Simeon and Levi's massacre of the Shechemites (Gen 34:25-29). Jesus crosses the ethnic and moral fault-line at the very location of the original rupture, offering the Samaritan woman what Shechem took by force."}
    ],
    "25": [
      {"type": "allusion", "target": "Gen 49:5",
       "note": "Simeon and Levi massacre the Shechemites with swords (Gen 34:25-29), setting up Jacob's dying curse: 'Simeon and Levi are brothers; weapons of violence are their swords... I will divide them in Jacob and scatter them in Israel' (Gen 49:5-7). Levi's scattering becomes his priestly assignment — scattered through the cities of Israel as the covenant-keepers. The violent act that earns a curse is the raw material God reverses: Levi becomes the tribe of mediation rather than destruction (Num 25:13; Deut 33:8-11)."}
    ]
  },
  "35": {
    "4": [
      {"type": "allusion", "target": "Acts 19:19",
       "note": "Jacob commands his household to put away their foreign gods; they hand over all the foreign gods and the earrings, and Jacob buries them under the oak at Shechem (Gen 35:4) — a pre-Bethel purge before encountering God. The NT parallel is the Ephesian converts' mass burning of magic books at a cost of 50,000 silver pieces (Acts 19:19): in both cases, meeting the God of the covenant requires renouncing and destroying the objects of false worship. The deliberate disposal (burial / burning) marks a clean break."}
    ],
    "10": [
      {"type": "fulfillment", "target": "Rev 21:12",
       "note": "God confirms Jacob's name as Israel at Bethel (Gen 35:10), and immediately reissues the Abrahamic covenant: 'a nation and a company of nations shall come from you, and kings shall come from your own body' (v. 11). The twelve tribes flowing from Israel's twelve sons (vv. 23-26) become the twelve gates of the New Jerusalem, each gate named after one of the tribes (Rev 21:12) — the covenant people of Israel are built permanently into the eschatological city of God."}
    ],
    "18": [
      {"type": "shadow", "target": "Acts 2:33",
       "note": "Rachel names her dying-birth son Ben-Oni ('son of my sorrow'), but Jacob renames him Benjamin ('son of the right hand,' Gen 35:18). The naming captures the Christological pattern of humiliation followed by exaltation: Christ on the cross was the Son of Sorrow — forsaken, dying, bearing the grief of the world — but is now the Son of the Right Hand, 'exalted at the right hand of God' (Acts 2:33; Ps 110:1). Benjamin, the son born in his mother's death agony who received the name of honor, is a shadow of this double identity."},
      {"type": "allusion", "target": "Ps 110:1",
       "note": "Jacob's renaming of Ben-Oni to Benjamin ('son of my right hand') uses the same positional honor that Psalm 110:1 assigns to the Messiah: 'Sit at my right hand.' The tribe of Benjamin — the only tribe born in Canaan, the tribe of Saul and of Paul — carries this right-hand resonance through Israel's history until Christ fulfills the royal Messianic promise that Benjamin's name first embodied."}
    ]
  }
}


def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)
    print('Genesis 33-35 echoes written.')

if __name__ == '__main__':
    main()
