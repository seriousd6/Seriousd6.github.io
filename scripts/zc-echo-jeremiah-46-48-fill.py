"""
Echo — Jeremiah chapters 46–48 (Oracles Against the Nations)
Run: python3 scripts/zc-echo-jeremiah-46-48-fill.py

Oracles Against the Nations: Egypt (46), Philistia (47), Moab (48).
NT connections are more thematic than direct-citation here; the main patterns
are: the day-of-YHWH motif, divine vengeance on pride, indestructible word,
and the unexpected restoration promises for enemy nations.

Key echo decisions:
- 46:10 (day of the Lord, vengeance) = Rev 6:17; 2 Thess 1:8
- 46:27-28 (fear not, I am with you) = Matt 28:20; Rom 8:31
- 47:6-7 (sword of the LORD) = Rev 19:15
- 48:7 (trust in wealth) = Luke 12:19-20; 1 Tim 6:17
- 48:10 (cursed who does LORD's work negligently) = 1 Cor 15:58
- 48:29-30 (Moab's pride) = 1 Pet 5:5; Jas 4:6
- 48:47 (latter-days restoration of Moab) = Rev 21:24-26 (nations bring glory)
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

JER_ECHO_46_48 = {
  "46": {
    "10": [
      {"type": "allusion", "target": "Rev 6:17", "note": "That day belongs to the Lord GOD of hosts — a day of vengeance on his foes — the day belongs to YHWH Sabaoth as the divine warrior exacting judgment; Revelation&apos;s sixth seal announces the same reality: the great day of their wrath has come, and who can stand? (Rev 6:17); the OAN&apos;s day-of-YHWH against the nations becomes the eschatological day of wrath in Revelation"},
      {"type": "allusion", "target": "2 Thess 1:8", "note": "A day of vengeance, by which he avenges himself on his foes — YHWH&apos;s self-vindicating judgment against the armies of Egypt; Paul anticipates the same divine self-vindication at Christ&apos;s return: in flaming fire, inflicting vengeance on those who do not know God and those who do not obey the gospel of our Lord Jesus (2 Thess 1:8); the vengeance-of-YHWH motif of the OAN runs into the NT&apos;s eschatology of judgment"}
    ],
    "27": [
      {"type": "allusion", "target": "Matt 28:20", "note": "Fear not, O Jacob my servant, do not be dismayed, O Israel; for I am going to save you from far away — the divine-warrior oracle against Egypt concludes with an assurance of divine presence for YHWH&apos;s servant; Jesus&apos;s commission concludes with the same assurance: behold, I am with you always, to the end of the age (Matt 28:20); the OAN pattern — judgment on the nations, rescue for the servant — is the structure of the Great Commission&apos;s closing promise"},
      {"type": "allusion", "target": "Rom 8:31", "note": "I will make a complete end of all the nations to which I have scattered you, but of you I will not make a complete end — the contrast between Israel&apos;s salvation and the nations&apos; judgment; Paul&apos;s rhetorical question (if God is for us who can be against us?) presupposes this same covenantal asymmetry: those whom YHWH preserves through the exile cannot be ultimately destroyed"}
    ],
    "28": [
      {"type": "allusion", "target": "Heb 12:5-6", "note": "I will discipline you in just measure, and I will by no means leave you unpunished — YHWH&apos;s corrective judgment on his people distinguished from the total destruction of the nations; Hebrews applies this pattern to the church: the Lord disciplines the one he loves, and chastises every son whom he receives (Heb 12:6, quoting Prov 3:12); judgment as discipline (not destruction) is the covenantal form of love"}
    ]
  },
  "47": {
    "6": [
      {"type": "allusion", "target": "Rev 19:15", "note": "O sword of the LORD, how long before you rest? — the lament that the divine sword of judgment seems without end; Revelation&apos;s eschatological vision resolves it: from the returning Christ&apos;s mouth comes a sharp sword with which to strike down the nations (Rev 19:15); the sword that wreaked havoc on Philistia is the same word-sword that the Rider on the white horse wields at the final judgment"}
    ]
  },
  "48": {
    "7": [
      {"type": "allusion", "target": "Luke 12:19-20", "note": "Because you trusted in your own accomplishments and your stored wealth, you too will be captured — Moab&apos;s self-reliance and stored wealth become the ground of judgment; Jesus&apos;s parable of the rich fool (Luke 12:19-20: Soul, take your ease... you fool, this night your soul is required of you) applies the same pattern: trust in accumulated wealth is the posture that judgment exposes"},
      {"type": "allusion", "target": "1 Tim 6:17", "note": "You trusted in your stored wealth — Paul warns the rich not to set their hopes on the uncertainty of riches but on God who richly provides everything to enjoy (1 Tim 6:17); Moab&apos;s trust in stored wealth is the OT example of the misplaced confidence that Paul warns against; wealth becomes a rival to YHWH"}
    ],
    "10": [
      {"type": "allusion", "target": "1 Cor 15:58", "note": "Cursed is the one who carries out the LORD&apos;s work negligently — the Moab oracle&apos;s unexpected criterion: even YHWH&apos;s instruments of judgment must execute the commission faithfully; Paul applies the faithfulness-principle to the resurrection hope: be steadfast, immovable, always abounding in the work of the Lord, knowing that in the Lord your labor is not in vain (1 Cor 15:58); careless execution of divine commission is the OT analog to apostolic negligence"}
    ],
    "11": [
      {"type": "allusion", "target": "2 Cor 3:18", "note": "Moab has been undisturbed from his youth, settled quietly on his dregs — never poured from vessel to vessel, his taste has not changed; the wine-on-its-dregs image depicts spiritual stagnation: unchanged by trial or testing; Paul&apos;s contrast is the Spirit&apos;s transformative work: we are being transformed from one degree of glory to another (2 Cor 3:18); the vessel-to-vessel pouring that Moab never underwent is the pattern of spiritual formation through which believers are shaped"}
    ],
    "29": [
      {"type": "allusion", "target": "1 Pet 5:5", "note": "We have heard of Moab&apos;s pride — he is exceedingly arrogant, his insolence, his self-exaltation, his haughtiness, and the towering conceit of his heart — the multi-layered vocabulary of Moabite arrogance; Peter cites Prov 3:34 against this posture: God opposes the proud but gives grace to the humble (1 Pet 5:5); the specific sin for which Moab is destroyed (v.42: lifted himself up against the LORD) is the sin that Peter identifies as God&apos;s primary target"}
    ],
    "42": [
      {"type": "allusion", "target": "Rev 18:7-8", "note": "Moab will be destroyed as a nation because he lifted himself up against the LORD — pride-against-YHWH as the ground of national judgment; Revelation applies the same structure to Babylon: as she glorified herself and lived in luxury, so give her a like measure of torment and mourning (Rev 18:7-8); the Moab-OAN pattern of self-exaltation leading to destruction is the template for Babylon&apos;s fall in Revelation"}
    ],
    "47": [
      {"type": "allusion", "target": "Rev 21:24-26", "note": "Yet in the latter days I will restore the fortunes of Moab, declares the LORD — the unexpected restoration promise for a pagan enemy nation at the end of a long oracle of destruction; Revelation&apos;s new Jerusalem vision includes the nations bringing their glory and honor into the city (Rev 21:24-26); the latter-days restoration of Moab foreshadows the eschatological inclusion of nations in the new creation — even traditional enemies of Israel find a place in YHWH&apos;s final restoration"}
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHO_46_48)
    save_echo('jeremiah', existing)
    print('Jeremiah 46-48 echoes written.')

if __name__ == '__main__':
    main()
