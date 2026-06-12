"""
MKT Echo — 1 Samuel chapters 9–12
Run: python3 scripts/zc-echo-1samuel-9-12.py

Ch 9: Saul sought, found by YHWH's providence — Samuel anoints him privately.
Ch 10: Saul anointed, three signs, Spirit rushes on him, chosen by lot at Mizpah.
Ch 11: Saul delivers Jabesh-Gilead, kingdom renewed at Gilgal.
Ch 12: Samuel's farewell covenant speech — YHWH's saving acts, warning about kingship.

Echo anchors:
- Ch9: providence in apparent lostness; prophetic anointing
- Ch10: Spirit-coming as new creation; lot → YHWH's sovereign choice; anointing
- Ch11: Spirit-empowered deliverance; Gilgal renewal
- Ch12: YHWH's saving history; faithful remnant; 'do not fear but serve faithfully'
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
  "9": {
    "3": [
      {"type": "theme", "target": "Luke 15:4", "note": "Kish's donkeys are lost and Saul is sent to seek them — the narrative that will end with the anointing of Israel's first king begins with a mundane search for lost animals. YHWH's providential guidance of Saul through a failed search mirrors the parable of the lost sheep (Luke 15:4): what appears to be aimless wandering is YHWH's sovereign leading toward an encounter with the prophet. The seeking of the lost is YHWH's initiative, not merely the seeker's — the donkeys' lostness is what brings Saul to Samuel."}
    ],
    "16": [
      {"type": "allusion", "target": "Acts 13:21", "note": "YHWH tells Samuel: 'Tomorrow about this time I will send you a man from the land of Benjamin, and you shall anoint him to be prince over my people Israel.' The divine selection and prophetic anointing of the Benjaminite king is the pattern Paul summarizes in Acts 13:21: 'Then they asked for a king, and God gave them Saul the son of Kish, a man of the tribe of Benjamin.' The divine initiative in Israel's monarchy — YHWH choosing and directing the anointing — is the theological background for the NT's understanding that all authority is given from above (John 19:11)."}
    ]
  },
  "10": {
    "6": [
      {"type": "type", "target": "Acts 2:4", "note": "The Spirit of YHWH will rush upon you (<em>ṣālaḥ</em>) and you will be turned into another man — Samuel's promise of Spirit-transformation at Saul's anointing anticipates Pentecost: 'They were all filled with the Holy Spirit' (Acts 2:4). The pattern of an anointed one receiving the Spirit and being changed is the OT sequence that NT fulfillment expands: what happened to Saul individually at his anointing happens to the entire church at Pentecost. The 'other man' language anticipates Paul's 'new creation' (2 Cor 5:17)."}
    ],
    "1": [
      {"type": "allusion", "target": "1 John 2:20", "note": "Samuel takes a flask of oil and pours it on Saul's head and kisses him — the anointing with oil (<em>māšaḥ</em>) that gives Saul the title <em>māšîaḥ</em> (anointed one). The NT reinterprets anointing: 'you have been anointed by the Holy One' (1 John 2:20). Every Christian is an anointed one — <em>christos</em> in Greek, <em>māšîaḥ</em> in Hebrew — sharing in Christ's anointing. The oil on Saul's head is the provisional, revocable type; the Spirit on the believer is the permanent, irrevocable fulfillment."}
    ],
    "24": [
      {"type": "theme", "target": "John 15:16", "note": "At the lot-selection at Mizpah, YHWH causes the lot to fall on Saul — 'Is there anyone else here?' 'There is no one like him among all the people.' The divine selection through the lot is YHWH's sovereign choice: Samuel says 'Do you see him whom YHWH has chosen?' (v24). Jesus applies the same divine-election logic to his disciples: 'You did not choose me, but I chose you' (John 15:16). The chosen king foreshadows the chosen disciples; the choosing belongs to YHWH/Christ, not to popular selection."}
    ]
  },
  "11": {
    "6": [
      {"type": "allusion", "target": "Luke 4:18", "note": "The Spirit of God rushed upon Saul when he heard of the Ammonite threat and his anger was greatly kindled — <em>ṣālaḥ rûaḥ ʾĕlōhîm</em>. The Spirit's empowerment for delivering the oppressed is the OT pattern that Jesus claims at Nazareth: 'The Spirit of the Lord is upon me, because he has anointed me to proclaim good news to the poor' (Luke 4:18, citing Isa 61:1). Both Saul's Spirit-empowerment and Jesus's cite the same Spirit-anointing pattern — but Saul's empowerment is conditional and revocable (16:14), while Jesus's is permanent."}
    ],
    "13": [
      {"type": "theme", "target": "John 3:17", "note": "Saul says: 'Not a man shall be put to death today, for today YHWH has worked salvation in Israel' — the day of victory is a day of mercy, not retribution. The same principle governs the incarnation: 'For God did not send his Son into the world to condemn the world, but in order that the world might be saved through him' (John 3:17). The victory-day that Saul declares a day of mercy rather than vengeance anticipates the greater victory of Christ who absorbs the condemnation rather than distributing it."}
    ]
  },
  "12": {
    "22": [
      {"type": "allusion", "target": "Rom 11:1-2", "note": "Samuel declares: 'YHWH will not abandon his people, for his great name's sake, because it has pleased YHWH to make you a people for himself.' The divine commitment to Israel's covenant preservation — rooted not in their merit but in YHWH's own name and pleasure — is the exact ground Paul invokes in Romans 11:1-2: 'Has God rejected his people? By no means! For I am an Israelite... God has not rejected his people whom he foreknew.' YHWH's commitment to his own name's reputation is the permanent anchor of the covenant's permanence."}
    ],
    "24": [
      {"type": "theme", "target": "Heb 13:15", "note": "Samuel's closing covenant call: 'Only fear YHWH and serve him faithfully with all your heart, for consider what great things he has done for you.' The combination of reverent fear, covenant service, and memory of YHWH's saving acts is the OT form of Hebrews 13:15: 'Through him let us continually offer up a sacrifice of praise to God, that is, the fruit of lips that acknowledge his name.' Grateful remembrance of divine saving acts produces the faithful service that Samuel calls Israel to — the same dynamic as NT eucharistic worship."}
    ]
  }
}

def main():
    existing = load_echo('1samuel')
    merge_echo(existing, ECHOES)
    save_echo('1samuel', existing)
    print('1samuel ch 9-12: echoes written')

if __name__ == '__main__':
    main()
