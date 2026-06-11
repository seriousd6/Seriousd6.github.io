"""
Echo Layer — Joshua chapter 24
Run: python3 scripts/zc-echo-joshua-24-24.py

Joshua 24: the covenant renewal at Shechem. Joshua rehearses the Heilsgeschichte (vv. 2-13),
issues the ultimatum (vv. 14-15), receives the people's oath (vv. 16-24), formalises the
covenant in writing and with a stone witness (vv. 25-27), and the chapter closes with
the deaths of Joshua and Eleazar and the burial of Joseph's bones (vv. 28-33).

Key echo targets:
- v2: ancestors beyond the Euphrates → Acts 7:2-4 (Stephen's Heilsgeschichte)
- v14-15: "choose whom you will serve" → Matt 4:10 (Jesus cites Deut 6:13)
- v19: "you cannot serve the LORD" → Rom 8:7
- v25-26: covenant written in the Book → Heb 8:10 (new covenant on hearts)
- v27: stone witness → Luke 19:40
- v29-31: Joshua dies, rest incomplete → Heb 4:8
- v32: Joseph's bones → Heb 11:22
- v33: Eleazar dies → Heb 7:23-24
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
    # INTENT: Add echo entries for chapters/verses not yet present; deduplicate by (type, target).
    # CHANGE? If echo schema changes, update all zc-echo-*.py scripts and Z_COMMENTARY_SCRIPT_GUIDE.md.
    # VERIFY: data/echoes/joshua.json should have ch24 keys after run.
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

# Joshua 24 — covenant renewal at Shechem.
# Echo entries are selective: verses with strong NT connections.
JOSHUA_ECHOES = {
    "24": {
        # Joshua gathers all Israel at Shechem — the same sacred assembly location as Gen 12:6,
        # linking back to Abraham's first altar in Canaan and forward to the covenant now being sealed.
        "1": [
            {
                "type": "theme",
                "target": "Gen 12:6",
                "note": "Shechem was where Abraham first entered Canaan and built an altar (Gen 12:6). Joshua's covenant assembly at the same location frames the inheritance as the fulfilment of the Abrahamic promise."
            }
        ],
        # Joshua's historical recital begins with the ancestors 'beyond the River' (Euphrates),
        # serving other gods. Stephen's speech in Acts 7:2-4 retells this same Heilsgeschichte
        # — the God who calls Abraham out of Mesopotamian idolatry.
        "2": [
            {
                "type": "allusion",
                "target": "Acts 7:2",
                "note": "Stephen's covenant speech in Acts 7:2-4 retells this same Heilsgeschichte: God appeared to Abraham 'when he was in Mesopotamia, before he lived in Haran.' Joshua's recital of salvation history is the OT model for the NT pattern of rehearsing God's acts as the basis for covenant loyalty."
            }
        ],
        # v3: God took Abraham from beyond the Euphrates and led him through Canaan
        # — Paul cites the Abrahamic covenant as the foundation of justification by faith.
        "3": [
            {
                "type": "theme",
                "target": "Gal 3:8",
                "note": "The rehearsal of God's initiative in calling Abraham ('I took your father Abraham') grounds covenant loyalty in divine grace — the same structure Paul uses in Gal 3:8 where the gospel was announced beforehand to Abraham."
            }
        ],
        # v5: 'I sent Moses and Aaron, and I plagued Egypt' — the exodus narrated as God's act.
        # 1 Cor 10:1-5 reads the exodus events as types written for the church's instruction.
        "5": [
            {
                "type": "type",
                "target": "1 Cor 10:1",
                "note": "Joshua's recital of the exodus plagues and wilderness events aligns with 1 Cor 10:1-5, where Paul reads those same events as 'types for us' — the pattern of divine rescue that is fulfilled in Christ's greater exodus."
            }
        ],
        # v14: 'Fear the LORD and serve him in sincerity and faithfulness' — the covenant call.
        # When tempted, Jesus cites Deut 6:13 ('Fear the LORD your God and serve him only') —
        # the same covenantal principle Joshua is now applying.
        "14": [
            {
                "type": "allusion",
                "target": "Matt 4:10",
                "note": "Jesus's reply to Satan's final temptation — 'You shall worship the Lord your God and serve him only' (Deut 6:13) — echoes the covenant call here: exclusive service to Yahweh, rejecting other gods. Joshua's 'put away the gods your ancestors served' parallels the same demand."
            }
        ],
        # v15: 'Choose today whom you will serve' — the decisive covenant ultimatum.
        # Elijah poses the same binary at Carmel (1 Kgs 18:21); Jesus poses it in Matt 6:24.
        "15": [
            {
                "type": "theme",
                "target": "Matt 6:24",
                "note": "The binary of 'choose whom you will serve' reappears in Jesus's teaching: 'No one can serve two masters' (Matt 6:24). The covenantal exclusive-loyalty demand Joshua frames here becomes a permanent NT principle."
            },
            {
                "type": "allusion",
                "target": "1 Kgs 18:21",
                "note": "Elijah's Carmel challenge — 'How long will you waver between two opinions?' — reprises Joshua's ultimatum here; both call Israel to stop straddling Yahweh and Baal and commit to one lord."
            }
        ],
        # v19: 'You are not able to serve the LORD; he is a holy God; he is a jealous God.'
        # Joshua's warning about Israel's inability echoes Paul's diagnosis in Romans 8:7-8.
        "19": [
            {
                "type": "theme",
                "target": "Rom 8:7",
                "note": "Joshua's warning that the people 'cannot serve the LORD' because of his holiness anticipates Paul's diagnosis: 'the mind governed by the flesh cannot submit to God's law' (Rom 8:7) — the same structural incapacity that only Christ's Spirit overcomes."
            }
        ],
        # v22: 'You are witnesses against yourselves that you have chosen the LORD.'
        # The people's self-incriminating oath echoes covenant-witness language in Malachi and Romans.
        "22": [
            {
                "type": "theme",
                "target": "Mal 3:5",
                "note": "The self-incriminating witness formula ('you are witnesses against yourselves') anticipates Malachi's covenant lawsuit where God himself is 'a swift witness against' the covenant-breakers (Mal 3:5) — covenant witness can cut both ways."
            }
        ],
        # v25-26: Covenant formalised in writing in the Book of the Law; a stone set up as witness.
        # Heb 8:10 contrasts the externally-written Mosaic covenant with the new covenant written
        # on hearts — both contexts hinge on the medium of covenant inscription.
        "25": [
            {
                "type": "shadow",
                "target": "Heb 8:10",
                "note": "Joshua's covenant written 'in the Book of the Law' (external stone and scroll) is the old-covenant mode that Hebrews 8:10 contrasts with the new: 'I will put my laws into their minds and write them on their hearts.' The Shechem covenant formalises the pattern that the new covenant transforms."
            }
        ],
        # v26: The large stone set up under the oak — a silent witness.
        # Jesus tells the Pharisees 'even the stones would cry out' (Luke 19:40) — picking up the
        # same tradition of stones as witnesses to divine acts and covenant claims.
        "26": [
            {
                "type": "allusion",
                "target": "Luke 19:40",
                "note": "The stone set up as witness 'has heard all the words the LORD spoke to us' (v27) — inanimate matter bearing testimony to covenant events. Jesus exploits the same tradition in Luke 19:40: if his disciples fall silent, 'the stones will cry out.'"
            }
        ],
        # v27: 'This stone shall be a witness against us' — stone hears God's words and testifies.
        "27": [
            {
                "type": "theme",
                "target": "Rev 2:17",
                "note": "The covenant stone that bears witness 'against us' if Israel fails resonates with the white stone of Rev 2:17 given to the overcomer — the new-covenant counterpart where the stone's testimony is gracious rather than accusatory."
            }
        ],
        # v29-31: Joshua dies at 110, buried at Timnath-serah; Israel served the LORD all his days.
        # Hebrews 4:8 names Joshua explicitly: his conquest did not bring the promised rest.
        "29": [
            {
                "type": "shadow",
                "target": "Heb 4:8",
                "note": "Joshua's death marks the end of his generation; the rest he won was territorial and temporary. Hebrews 4:8 states directly: 'If Joshua had given them rest, God would not have spoken of another day later on' — pointing to the greater Joshua (Jesus) who gives the Sabbath-rest that remains."
            }
        ],
        # v32: Joseph's bones buried at Shechem — completing the promise of Gen 50:25 ('carry my bones').
        # Heb 11:22 cites Joseph's faith in giving these burial instructions as an act of forward hope.
        "32": [
            {
                "type": "fulfillment",
                "target": "Heb 11:22",
                "note": "Hebrews 11:22 names this moment: Joseph 'mentioned the exodus of the Israelites and gave directions concerning his bones' as an act of faith — believing the promise of Canaan. The burial at Shechem is the literal fulfilment of that faith, completing a trajectory that spans Genesis to Joshua."
            },
            {
                "type": "allusion",
                "target": "Gen 50:25",
                "note": "Genesis 50:25 records Joseph's dying oath: 'God will surely come to your aid, and then you must carry my bones up from here.' Joshua 24:32 is the completion of that oath — the interlude between promise and fulfilment spans the entire exodus narrative."
            }
        ],
        # v33: Eleazar son of Aaron dies and is buried — the priestly line continues but mortal priests die.
        # Hebrews 7:23-24 contrasts the many mortal priests (each replaced by death) with Christ the
        # permanent priest who holds his priesthood permanently because he lives forever.
        "33": [
            {
                "type": "shadow",
                "target": "Heb 7:23",
                "note": "The deaths of Joshua (v29) and Eleazar (v33) together close the generation — leadership and priesthood both pass by death, requiring successors. Hebrews 7:23-24 makes this the decisive contrast with Christ: 'the former priests were many in number because they were prevented by death from continuing in office, but he holds his priesthood permanently.'"
            }
        ]
    }
}


def main():
    existing = load_echo('joshua')
    merge_echo(existing, JOSHUA_ECHOES)
    save_echo('joshua', existing)
    # Report coverage
    il = json.loads((ROOT / 'data/interlinear/joshua.json').read_text())
    ch = '24'
    il_count = len(il.get(ch, {}))
    echo_count = len(existing.get(ch, {}))
    print(f'  ch24: {echo_count} echo entries / {il_count} IL verses')
    all_chs = sorted(existing.keys(), key=int)
    print(f'  Joshua echo chapters now: {all_chs}')


if __name__ == '__main__':
    main()
