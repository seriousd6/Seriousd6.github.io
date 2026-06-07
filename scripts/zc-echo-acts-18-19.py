"""
MKT Echo Layer — Acts chapters 18–19
Run: python3 scripts/zc-echo-acts-18-19.py

Source data used:
- data/interlinear/acts.json
- data/parallels/acts.json (no parallels for ch18 or ch19)
- data/echoes/acts.json (no existing entries for ch18 or ch19)

Key decisions:
- Acts 18 "Do not be afraid; I am with you" (v9): typed against Isa 41:10 / Jer 1:8 / Josh 1:9
  — the commissioning formula pattern through the OT applied to the apostolic mission
- Acts 18 "Your blood be on your own heads" (v6): allusion to Ezek 33:4 watchman oracle
- Acts 18 "I have many people in this city" (v10): Isa 65:1-2 (found by those who did not
  seek — applied to Corinthian Gentile mission)
- Acts 19 Spirit given at handlaying (vv.2-6): Joel 2:28-29 / Ezek 36:27 echo
- Acts 19 burning of magic books (vv.18-19): Deut 18:10-12 / Isa 8:19-20 framework
- Acts 19 "word of the Lord spread widely" (v20): Isa 55:11 refrain (same as Acts 12:24 pattern)
- Acts 19 Artemis riot (vv.27-34): Ps 115:4-8 / Isa 44:9-20 idol-polemic background
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
    # INTENT: merge echo entries; deduplicate by (type, target) within each verse
    # CHANGE? If echo schema changes, update dedup key here
    # VERIFY: spot-check acts.json ch18 v9 and ch19 v20 in browser echoes panel
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

ACTS_ECHOES = {
  "18": {
    "6": [
      {"type": "allusion", "target": "Ezek 33:4", "note": "Paul's declaration — 'Your blood be on your own heads! I am innocent' — echoes the Ezekiel watchman oracle: if the watchman warns and the people do not listen, 'his blood shall be upon his own head' (Ezek 33:4). Paul frames the turning to Gentiles not as abandonment of Israel but as the completion of the prophetic watchman's obligation: he has warned; the responsibility now rests with those who refuse."}
    ],
    "9": [
      {"type": "allusion", "target": "Isa 41:10", "note": "The Lord's night-vision commission — 'Do not be afraid; keep on speaking, do not be silent. For I am with you' — echoes the divine 'fear not' commissioning formula of Isaiah 41:10 ('Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you'). The same formula runs through the commissioning of patriarchs (Gen 26:24) and prophets (Jer 1:8), marking Paul's Corinthian mission as the continuation of the OT prophetic-servant pattern."},
      {"type": "allusion", "target": "Jer 1:8", "note": "The 'I am with you' promise and command not to be afraid echoes Jeremiah's commissioning: 'Do not be afraid of them, for I am with you to deliver you' (Jer 1:8). Like Jeremiah sent to a resistant people, Paul is sent to Corinth for an extended ministry despite opposition; the divine promise of presence is the same word that sustained the weeping prophet, now sustaining the apostle to the Gentiles."}
    ],
    "10": [
      {"type": "allusion", "target": "Isa 65:1", "note": "'I have many people in this city' — God's assurance that the Corinthian mission will succeed echoes Isaiah 65:1: 'I was ready to be sought by those who did not ask for me; I was ready to be found by those who did not seek me.' Paul cites this verse in Romans 10:20 as fulfilled in the Gentile mission; here Acts narrates its ongoing outworking as God assures Paul of a harvest already determined in election."}
    ],
    "18": [
      {"type": "allusion", "target": "Num 6:18", "note": "Paul's vow at Cenchreae — cutting his hair because of a vow — reflects the Nazirite vow-conclusion practice of Numbers 6 (the Nazirite shaved his head at the completion of the vow). Luke records this detail to show Paul remaining observant of Jewish practice; it also ties the mission to the OT consecration-vow tradition in which a servant set apart to God marks the completion of a divine service."}
    ],
    "28": [
      {"type": "allusion", "target": "Ps 2:7", "note": "Apollos 'vigorously refuted his Jewish opponents in public debate, proving from the Scriptures that Jesus was the Messiah' — the scriptural proof was built primarily on texts like Ps 2:7 (the decree of adoption: 'You are my Son; today I have become your Father'), Ps 16:10 (not abandoned to Sheol), and Isa 53 (the suffering servant). Luke presents Apollos as doing what Paul did in Thessalonica (17:2-3): demonstrating from the OT that the Christ had to suffer and rise."}
    ]
  },
  "19": {
    "2": [
      {"type": "allusion", "target": "Joel 2:28", "note": "The twelve Ephesian disciples who had received only John's baptism and 'had not heard that there is a Holy Spirit' receive the Spirit when Paul lays hands on them, echoing Joel 2:28-29 ('I will pour out my Spirit on all flesh; your sons and daughters will prophesy'). The Pentecostal Spirit-outpouring is extending outward: from Jerusalem (Acts 2) to Samaria (8:17) to Gentiles (10:44) and now to disciples at the edge of the known mission field."}
    ],
    "6": [
      {"type": "fulfillment", "target": "Joel 2:28", "note": "The twelve disciples speaking in tongues and prophesying after Paul's handlaying is Luke's explicit fulfillment of Joel 2:28 ('your sons and daughters shall prophesy'). Peter had proclaimed this fulfillment at Pentecost (Acts 2:17); Acts narrates its continued outpouring as the Spirit advances the mission geographically. Each new instance of Spirit-reception with tongues and prophecy is the ongoing fulfillment of Joel's 'all flesh' universality."}
    ],
    "12": [
      {"type": "allusion", "target": "2 Kgs 13:21", "note": "Handkerchiefs and aprons that had touched Paul healing the sick echoes the Elisha tradition in which physical contact with the prophet mediated divine power — 2 Kings 13:21 describes a dead man reviving when he touched Elisha's bones. Luke presents the apostolic healings as operating within the same prophetic-servant tradition: God works through physical means associated with his commissioned servants (cf. 2 Kgs 5:14, Naaman healed in the Jordan as Elisha instructed)."}
    ],
    "17": [
      {"type": "theme", "target": "Ps 99:3", "note": "The result of the failed exorcism and the Spirit's power — 'the name of the Lord Jesus was held in high honor' — echoes the Psalm theology of the divine name: 'Let them praise your great and awesome name — it is holy' (Ps 99:3). The name of Jesus, demonstrated as uniquely authoritative against the would-be competitors, establishes the same holy name-reverence that the Psalter attributed to YHWH's name alone."}
    ],
    "19": [
      {"type": "allusion", "target": "Deut 18:10", "note": "The public burning of magic books worth fifty thousand drachmas echoes the Deuteronomic prohibition on divination and sorcery (Deut 18:10-12: 'there shall not be found among you... anyone who practices divination, a soothsayer, an augur, a sorcerer'). The Ephesian converts' voluntary destruction of their sorcery texts is the practical enactment of Deuteronomic covenant allegiance: the things that belong to the old lord are burned in the presence of the new one."},
      {"type": "allusion", "target": "Isa 8:19", "note": "The burning of magic books also echoes Isaiah's polemic against consulting mediums and spiritists: 'should not a people inquire of their God? Why consult the dead on behalf of the living?' (Isa 8:19). The Ephesian converts have made the Isaianic choice: the living word of the Lord Jesus displaces the dead words of the magic practitioners."}
    ],
    "20": [
      {"type": "theme", "target": "Isa 55:11", "note": "'The word of the Lord spread widely and grew in power' — the fifth occurrence of Luke's Acts-refrain (6:7; 12:24; 13:49; 19:20; 28:30-31) enacts Isaiah 55:11: 'my word shall not return to me empty, but it shall accomplish that which I purpose, and shall succeed in the thing for which I sent it.' Each refrain marks a stage of the word's advance; Ephesus (the major city of Asia Minor) is now added to the spreading geography of the kingdom."}
    ],
    "27": [
      {"type": "allusion", "target": "Ps 115:4", "note": "Demetrius's complaint that Artemis's 'magnificent goddess' status is threatened by Paul's preaching echoes the Psalm polemic against idols: 'Their idols are silver and gold, the work of human hands' (Ps 115:4). Paul's proclamation that 'gods made by human hands are no gods at all' (v.26) is precisely the Psalm's argument — the idol is human-made and therefore cannot be divine. Acts 19 dramatizes the collision between the Psalm's idol-polemic and the flourishing idolatry industry of Ephesian Artemis."}
    ],
    "34": [
      {"type": "allusion", "target": "Isa 46:1", "note": "The crowd's chant — 'Great is Artemis of the Ephesians!' for two hours — ironically echoes the impotent repetition that Isaiah mocks in idol-worship: 'Bel bows down, Nebo stoops; their idols are on beasts and livestock' (Isa 46:1). Where YHWH carries his people (Isa 46:3-4), the idol must be carried and its worshippers cry its name to sustain its reputation. The two hours of Ephesian chanting is the dramatic embodiment of what Isaiah described: noise and repetition substituting for the genuine power that the name of Jesus just demonstrated."}
    ]
  }
}

def main():
    existing = load_echo('acts')
    merge_echo(existing, ACTS_ECHOES)
    save_echo('acts', existing)
    ch18_count = len(existing.get('18', {}))
    ch19_count = len(existing.get('19', {}))
    print(f'Acts 18-19 echoes: ch18={ch18_count} verses, ch19={ch19_count} verses.')

if __name__ == '__main__':
    main()
