"""
Echo Layer — Genesis chapters 13–16
Run: python3 scripts/zc-echo-genesis-13-16.py

Key echo trajectories:
- Gen 13:14-17 land promise: Gal 3:16-18 (promise to Abraham's Seed = Christ), Heb 11:8-10 (the city
  with foundations), Rom 4:13 (heir of the world through faith)
- Gen 14:18-20 Melchizedek: Heb 7:1-17; Ps 110:4 — already in echoes; script adds Ps 110:4 dimension
- Gen 15 covenant of pieces: Heb 9:15-22 (blood ratification of the new covenant); 15:6 already covered
- Gen 15:17 theophany (fire): Exod 13:21; Acts 2:3 (divine fire presence in new covenant)
- Gen 16 Hagar/Ishmael: Gal 4:22-31 (explicit allegory of the two covenants); 16:13 El Roi = Luke 1:48

Existing echoes for ch 14 (v18: Heb 7:1-10, Heb 7:15-17) and ch 15 (v5: Rom 4:18, v6: Rom 4:3 / Gal 3:6 /
James 2:23, v14: Acts 7:7) are preserved by merge_echo and not duplicated here.
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
  "13": {
    "10": [
      {"type": "shadow", "target": "Rev 22:1", "note": "Lot 'saw that the Jordan valley was well watered everywhere like the garden of the LORD' (13:10) — the Edenic lushness of the valley is the surface appeal that conceals its proximity to Sodom. The New Jerusalem's river of life and tree of life (Rev 22:1-2) restore the genuine garden of God that Lot's choice only approximated and perverted."}
    ],
    "14": [
      {"type": "shadow", "target": "Heb 11:8", "note": "'Lift up your eyes and look from the place where you are, northward and southward and eastward and westward, for all the land that you see I will give to you and to your offspring forever' (13:14-15) — the promise of visible land to unseen offspring is the structure of Abrahamic faith. Heb 11:8-10 reads this promise as looking beyond Canaan to 'the city that has foundations, whose designer and builder is God.'"}
    ],
    "15": [
      {"type": "shadow", "target": "Gal 3:16", "note": "'To your offspring I will give it' (13:15) — Paul's exegesis in Gal 3:16 turns on the singular 'offspring' (<em>sperma</em>): it does not say 'offsprings' (plural) but 'offspring' (singular), who is Christ. The land promise to Abraham's singular Seed is thus ultimately a promise fulfilled in and through Christ, not merely ethnic Israel."},
      {"type": "shadow", "target": "Rom 4:13", "note": "The comprehensive land promise — 'all the land that you see' — is interpreted by Paul in Rom 4:13 as a promise that Abraham would be 'heir of the world (<em>kosmos</em>),' not merely of Canaan. This universalization of the land promise occurs through faith, not law, and is inherited by those who share Abraham's faith in the God who gives life to the dead."}
    ],
    "16": [
      {"type": "shadow", "target": "Heb 11:12", "note": "'I will make your offspring as the dust of the earth, so that if one can count the dust of the earth, your offspring also can be counted' (13:16) — the hyperbolic promise to an childless man. Heb 11:12 holds this promise alongside the starlike-multitude promise (Gen 15:5): 'from one man, and him as good as dead, were born descendants as many as the stars of heaven and as many as the innumerable grains of sand by the seashore.'"}
    ],
    "18": [
      {"type": "shadow", "target": "Rom 15:7", "note": "Abram moved his tent to Hebron and 'built there an altar to the LORD' (13:18) — the pattern of faithful sojourn punctuated by altar-building (cf. 12:7, 8; 13:4, 18; 26:25; 35:1-7). The pilgrim-patriarch building altars to God in foreign land foreshadows the church's calling to offer 'sacrifices acceptable to God through Jesus Christ' (1 Pet 2:5) while sojourning in a world that is not yet the homeland (Heb 11:13-16)."}
    ]
  },
  "14": {
    "18": [
      {"type": "fulfillment", "target": "Ps 110:4", "note": "Melchizedek is 'priest of God Most High' (<em>kōhēn lĕ'ēl 'elyôn</em>, 14:18) — the one OT figure who combines royal and priestly office before the Levitical system exists. Ps 110:4 ('You are a priest forever after the order of Melchizedek') addresses the Davidic king in a way that Hebrews 7 applies solely to Christ: the Melchizedek-priesthood is the category that allows a king from Judah (not Levi) to exercise eternal priesthood."},
      {"type": "type", "target": "Heb 7:3", "note": "Melchizedek appears without genealogy, without recorded birth or death — 'without father or mother or genealogy, having neither beginning of days nor end of life' (Heb 7:3). This is not a claim that Melchizedek was supernatural, but that the silence of the text, read typologically, makes him 'resembling the Son of God' who holds 'a permanent priesthood' (Heb 7:17) by virtue of indestructible life, not lineal succession."}
    ],
    "19": [
      {"type": "shadow", "target": "Matt 26:26", "note": "Melchizedek brought out 'bread and wine' (<em>leḥem wĕyayin</em>) and blessed Abram (14:18-19). The eucharistic elements appear here in a priestly blessing before the Levitical system, associated with the priest-king 'of the order of Melchizedek.' The Last Supper, where Jesus ('a priest forever after the order of Melchizedek,' Heb 7:17) takes bread and wine and blesses his disciples, fulfills this priestly type."}
    ],
    "20": [
      {"type": "shadow", "target": "Heb 7:4", "note": "Abram gave Melchizedek 'a tenth of everything' (14:20) — tithe to a priest before the Levitical law existed. Heb 7:4-10 makes this the basis for asserting Melchizedek's greatness over Levi: Levi was, in effect, 'still in the loins of his ancestor' Abraham when Abraham paid the tithe, meaning the Levitical priesthood is itself subordinate to the Melchizedekian priesthood that Christ fulfills."}
    ]
  },
  "15": {
    "1": [
      {"type": "shadow", "target": "John 10:11", "note": "'Fear not, Abram, I am your shield (<em>māgēn</em>); your reward shall be very great' (15:1) — the divine self-disclosure as shield to the patriarch who has renounced worldly reward (14:22-23). The 'I am your shield' formula anticipates Christ's self-designation (John 10:11, 14: 'I am the good shepherd') as the one who absorbs the blow of judgment in the place of the flock."}
    ],
    "5": [
      {"type": "shadow", "target": "Gal 3:29", "note": "'Look toward heaven, and number the stars, if you are able to number them... So shall your offspring be' (15:5) — the promise is made to a man without heir. Gal 3:29 applies the stellar-offspring promise to all who are in Christ: 'if you are Christ's, then you are Abraham's offspring, heirs according to promise.' The countless stars represent the multinational community of faith gathered in Christ."}
    ],
    "6": [
      {"type": "shadow", "target": "Heb 11:1", "note": "Abraham 'believed the LORD, and he counted it to him as righteousness' (15:6) — this verse is the OT locus classicus for justification by faith, quoted in Rom 4:3, Gal 3:6, and James 2:23. Its structure — faith in a divine promise about something not yet visible — matches Heb 11:1's definition: 'faith is the assurance of things hoped for, the conviction of things not seen.'"}
    ],
    "17": [
      {"type": "type", "target": "Exod 13:21", "note": "The smoking fire pot and flaming torch that pass between the covenant pieces (15:17) — God alone passes through, binding himself unilaterally. The fire is the theophanic form of the divine presence: the pillar of fire that leads Israel (Exod 13:21-22), the burning bush (Exod 3:2), the fire on Sinai (Exod 19:18). The covenant ratified by fire anticipates the new covenant sealed by Christ's descent as the Spirit in tongues of fire (Acts 2:3)."},
      {"type": "shadow", "target": "Jer 34:18", "note": "The covenant of the pieces (15:17) — cutting animals in half and walking between them — was the ANE covenant-ratification rite: the parties invoke upon themselves the fate of the divided animal if they break the covenant (cf. Jer 34:18-19). Uniquely, only God passes through in Gen 15, making the covenant entirely unilateral: if it is broken, God himself bears the consequence. This is the typological background of the cross, where God in Christ bears the covenant curse (Gal 3:13)."}
    ],
    "18": [
      {"type": "shadow", "target": "Gal 3:17", "note": "The formal covenant ratification 'on that day' (15:18) — 'To your offspring I give this land' — is the covenant that Paul in Gal 3:17 identifies as 430 years before the Law and therefore not annulled by the Law. The Abrahamic covenant's land promise stands because it was sealed by God's unilateral oath-act in 15:17, making it, like the new covenant, entirely a matter of grace rather than human performance."}
    ]
  },
  "16": {
    "1": [
      {"type": "shadow", "target": "Gal 4:22", "note": "Sarai's barrenness and her Egyptian maidservant Hagar (16:1) are the two women of Paul's explicit allegory in Gal 4:22-31: 'Abraham had two sons, one by a slave woman and one by a free woman.' Paul identifies Hagar with the Sinai covenant (and the law), Sarai/Sarah with the Jerusalem above (and the new covenant of promise). The historical account thus carries a typological freight Paul describes as an allegory about two covenant orders."}
    ],
    "3": [
      {"type": "shadow", "target": "Gal 4:24", "note": "Sarai gives Hagar to Abram so that she 'may obtain children by her' (16:3) — the attempt to fulfill the divine promise by human arrangement rather than divine gift. This is the 'born after the flesh' pattern (Gal 4:23) that Paul contrasts with Isaac 'born through promise' (Gal 4:23). The attempt to secure the covenant blessing through human strategy is the fundamental error that the law-covenant repeats — seeking righteousness by works rather than receiving it by promise."}
    ],
    "7": [
      {"type": "shadow", "target": "Luke 1:30", "note": "The angel of the LORD finds Hagar 'by a spring of water in the wilderness, the spring on the way to Shur' (16:7) — the pattern of the divine messenger seeking out the outcast and marginalized in the wilderness recurs throughout Luke-Acts. Luke's Gospel emphasizes God's reach to those outside the covenant community (Samaritans, Gentiles, women) in language that echoes this foundational scene where God pursues the runaway slave girl."}
    ],
    "10": [
      {"type": "shadow", "target": "Rom 9:7", "note": "'I will surely multiply your offspring so that they cannot be numbered for multitude' (16:10) — the multiplication promise given to Hagar echoes the promise to Abraham (13:16; 15:5). Rom 9:7-9 distinguishes the two lineages: 'not all children of Abraham are his offspring' — the promise runs through Isaac (the child of the free woman), not Ishmael. The parallel promises reveal that God's purpose of election, not physical descent, governs who inherits the covenant."}
    ],
    "11": [
      {"type": "theme", "target": "Luke 1:31", "note": "The angel's naming oracle — 'You shall call his name Ishmael, because the LORD has listened (<em>šāmaʿ</em>) to your affliction' (16:11) — follows the pattern of angelic annunciation: angel appears → name given → etymology explained. Luke 1:31 ('you will conceive... and you shall call his name Jesus') and 1:13 (Zechariah: 'call his name John') repeat this naming-oracle structure, placing the incarnation within a long line of divine interventions announced by heavenly messengers."}
    ],
    "13": [
      {"type": "shadow", "target": "Luke 1:48", "note": "'You are a God of seeing' — <em>ʾattāh ʾēl roʾî</em>, the name Hagar gives God (16:13). The marginalized slave woman outside the covenant community is the one who receives divine vision and gives God a new name. Mary's Magnificat echoes this structure: 'he has looked on the humble estate of his servant' (Luke 1:48 — <em>epeblepsen</em>, he looked attentively) — the God who saw Hagar is the God who sees the lowly and reverses their condition."},
      {"type": "theme", "target": "Ps 34:15", "note": "'The LORD, the God who sees me' (<em>El Roi</em>, 16:13) — the divine attribute of seeing those whom humans overlook. Ps 34:15 ('The eyes of the LORD are toward the righteous and his ears toward their cry') develops this theme. Christ, who 'saw' the widow of Nain in her grief (Luke 7:13), the Zacchaeus hiding in the sycamore tree (Luke 19:5), and the bleeding woman in the crowd (Mark 5:32), embodies the El Roi character of God."}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    for ch in [13, 14, 15, 16]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    print('Genesis 13–16 echoes written.')

if __name__ == '__main__':
    main()
