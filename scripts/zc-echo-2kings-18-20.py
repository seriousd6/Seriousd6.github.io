"""
MKT Echo Layer — 2 Kings chapters 18–20
Run: python3 scripts/zc-echo-2kings-18-20.py

Source data used:
- data/interlinear/2kings.json
- data/translation/draft/mediating/2kings.json (MKT text)
- data/parallels/2kings.json (absorbed: ch18:13→Isa 36/2Chr 32; ch19:1→Isa 37; ch20:1→Isa 38)
- data/echoes/2kings.json (existing entries)

Key decisions:
- Ch 18:4 Nehushtan: Jesus's explicit citation (John 3:14) = fulfillment
- Ch 18:13 Sennacherib parallel to Isa 36 / 2Chr 32: absorbed as theme
- Ch 19:14 Hezekiah's prayer: allusion to Phil 4:6 and prayer model in Heb 11
- Ch 19:30-31 remnant: direct OT-to-NT trajectory (Rom 9:27; 11:5) = allusion
- Ch 19:35 angel of the LORD striking the Assyrian camp: allusion to Matt 26:53
- Ch 20:5 "heard your prayer, seen your tears": allusion to Heb 5:7 / Ps 56:8
- Ch 20:6 "for the sake of my servant David": theme running to Rom 15:8
- Ch 20:17-18 exile prophecy: type/shadow → Dan 1:1-7 (Hezekiah's descendants)
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

KINGS2_ECHOES = {
  "18": {
    "4": [
      {"type": "fulfillment", "target": "John 3:14-15", "note": "Hezekiah destroys the Nehushtan — the bronze serpent Moses made (Num 21:8-9) — because Israel has been burning incense to it. Jesus explicitly cites the lifting up of the serpent as the OT type of his own crucifixion: 'As Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life' (John 3:14-15). The Hezekiah narrative shows the type becoming an idol, which is precisely why Jesus's citation is typological rather than allegorical: the serpent's healing power was real (Num 21:9) but pointed beyond itself to the greater lifting up that would actually save."},
      {"type": "allusion", "target": "Num 21:8-9", "note": "The Nehushtan was the bronze serpent Moses made at YHWH's command — a type of atoning substitution (the serpent of judgment lifted up, those who looked lived). Hezekiah's destruction of it after generations of idolatrous use illustrates how a genuine divine gift can become an idol when the instrument is worshipped rather than the God who gave it. The principle runs through the NT's warning against making means into ends (1 Cor 1:12-13; Gal 4:8-10)."}
    ],
    "13": [
      {"type": "theme", "target": "Isa 36:1", "note": "The Sennacherib invasion narrative (2 Kgs 18:13–19:37) is virtually identical to Isaiah 36–37, confirming the literary dependence of Kings and Isaiah on a common court record. The parallel accounts serve different theological purposes: Kings uses the narrative as the climax of Hezekiah's reign before his fatal dealings with Babylon; Isaiah uses it to frame the Servant Songs that follow (Isa 40–55), connecting YHWH's defeat of Assyria to the greater deliverance to come."}
    ],
    "19": [
      {"type": "theme", "target": "Ps 20:7", "note": "Rabshakeh's challenge — 'What is the basis of this trust?' — and his contempt for trust in YHWH versus military alliance frames the theological question that runs through Psalms (Ps 20:7: 'Some trust in chariots and some in horses, but we trust in the name of the LORD our God') and the NT: 'Do not be anxious about anything... present your requests to God' (Phil 4:6-7). The Hezekiah crisis is the OT's supreme test case for trust in YHWH against impossible odds."}
    ],
    "31": [
      {"type": "allusion", "target": "Mic 4:4", "note": "Rabshakeh parodies the covenant-peace image — 'eat from his own vine and fig tree' — to make Assyrian submission sound like shalom. The genuine vine-and-fig-tree image (Mic 4:4; Zech 3:10) signifies covenant peace under a faithful king. Jesus's recognition of Nathanael 'under the fig tree' (John 1:48) and his cursing of the fruitless fig tree (Matt 21:19) work within this symbolic field. Rabshakeh's mockery of the image reveals that the false peace of empire is a counterfeit of the genuine covenant peace."}
    ],
    "35": [
      {"type": "theme", "target": "Dan 3:15", "note": "Rabshakeh's boast — 'Which of all the gods of these lands has rescued his territory from me? How then will the LORD rescue Jerusalem?' — is the theological challenge that recurs in the exile literature. Nebuchadnezzar makes the same challenge in the fiery furnace narrative (Dan 3:15: 'What god will be able to rescue you from my hand?'). The answer in both cases is the same: YHWH rescues. The Sennacherib crisis establishes the pattern that Daniel's narratives repeat under Babylonian and Persian empires."}
    ]
  },
  "19": {
    "1": [
      {"type": "theme", "target": "Isa 37:1", "note": "The narrative of Hezekiah's prayer and YHWH's deliverance (2 Kgs 19:1-37) is virtually verbatim in Isaiah 37:1-38. Isaiah embeds this narrative in his book as the climax of the Assyrian section (Isa 36-39) and the transition to the Servant Songs (Isa 40-55), suggesting that YHWH's defeat of Sennacherib is a type of the greater deliverance to come through the Servant."}
    ],
    "4": [
      {"type": "theme", "target": "Rev 6:10", "note": "'The living God' — Hezekiah's plea that Isaiah pray to 'the living God' who has been mocked by Sennacherib echoes the martyrs' cry in Revelation 6:10 ('How long, Sovereign Lord, holy and true, until you judge?'). Both invoke the living God against powers that mock his sovereignty. The phrase distinguishes YHWH from the dead gods of the nations (Ps 115:4-7) — a distinction the NT extends to include all who trust in perishable things (1 Thess 1:9)."}
    ],
    "14": [
      {"type": "allusion", "target": "Phil 4:6", "note": "Hezekiah takes Sennacherib's threatening letter and 'spreads it out before the LORD' in the temple — a concrete physical act of bringing an enemy's specific threat directly to God in prayer. Paul's command to 'in everything by prayer and petition, with thanksgiving, present your requests to God' (Phil 4:6) has this Hezekiah pattern as its OT model: bring the actual threat, not an abstraction, before YHWH and let him handle it."}
    ],
    "15": [
      {"type": "allusion", "target": "Ps 99:1", "note": "'LORD, God of Israel, enthroned between the cherubim, you alone are God over all the kingdoms of the earth.' Hezekiah's prayer opens with the divine throne between the ark's cherubim (the OT's supreme image of YHWH's royal presence) and immediately asserts universal sovereignty against Sennacherib's polytheistic worldview. Ps 99:1 uses the same image; the NT extends it to the ascended Christ at the Father's right hand (Heb 1:3) — the greater cherubim-throne is occupied by the incarnate Son."},
      {"type": "theme", "target": "Acts 17:24-25", "note": "Hezekiah's assertion — 'you are God over all the kingdoms of the earth; you made heaven and earth' — is the OT's most direct declaration of YHWH's universal sovereignty in the face of imperial polytheism. Paul's Areopagus speech (Acts 17:24-25) repeats the same claim before a Greek audience: 'The God who made the world and everything in it is the Lord of heaven and earth and does not live in temples made by human hands.' Hezekiah's prayer in the temple against Sennacherib and Paul's speech on the Areopagus against Zeus are the same theological argument in different cultural contexts."}
    ],
    "19": [
      {"type": "theme", "target": "Rev 15:4", "note": "'That all the kingdoms of the earth may know that you, LORD, are God alone' — Hezekiah's prayer aims at universal divine recognition as its goal. This is the same goal that drives the entire biblical narrative: Revelation 15:4 pictures all nations coming to worship before YHWH ('All nations will come and worship before you, for your righteous acts have been revealed'). The deliverance of Jerusalem is not merely national rescue but a sign event for the nations."}
    ],
    "28": [
      {"type": "allusion", "target": "Ezek 38:4", "note": "YHWH's threat against Sennacherib — 'I will put my hook in your nose and my bridle in your mouth, and I will make you return by the way you came' — uses the language of controlling a powerful animal. Ezekiel applies the same image to Gog (Ezek 38:4), and Revelation draws on the Gog tradition for its final battle. The 'hook in the nose' figure establishes a pattern: YHWH controls the great empires that threaten his people, turning their aggression back on itself."}
    ],
    "30": [
      {"type": "allusion", "target": "Rom 9:27", "note": "YHWH's word through Isaiah — 'The surviving remnant of the house of Judah will again take root downward and bear fruit upward' — is classic OT remnant theology: the covenant people are reduced to a remnant that carries forward the line of promise. Paul cites Isaiah's remnant language (Rom 9:27: 'Isaiah cries out concerning Israel: though the number of the sons of Israel be as the sand of the sea, only a remnant of them will be saved') to explain that God's election has always worked through a remnant, not the entire ethnic nation. Hezekiah's Jerusalem is the remnant-in-crisis that demonstrates this principle."},
      {"type": "allusion", "target": "Rom 11:5", "note": "'For a remnant will go out from Jerusalem, and survivors from Mount Zion. The zeal of the LORD of hosts will accomplish this.' The remnant language here (Isa 37:32, embedded in the 2 Kings 19 narrative) is the OT text behind Paul's argument in Rom 11:5: 'So too at the present time there is a remnant, chosen by grace.' The zeal of YHWH preserving the remnant in the Assyrian crisis is the theological pattern for God's election of the faithful remnant from Israel in Paul's own time."}
    ],
    "35": [
      {"type": "allusion", "target": "Matt 26:53", "note": "The angel of the LORD strikes 185,000 Assyrian soldiers in a single night — the most dramatic military deliverance in Kings. Jesus alludes to this tradition when arrested: 'Do you think I cannot call on my Father, and he will at once put at my disposal more than twelve legions of angels?' (Matt 26:53). Jesus is referencing the power demonstrated at the Assyrian camp: YHWH can deploy angel armies that make the greatest human military irrelevant. Jesus chooses not to deploy them — that restraint is the mystery of the cross."},
      {"type": "theme", "target": "Heb 11:32-34", "note": "The deliverance at the Assyrian camp is among the acts of faith Hebrews 11 alludes to: those 'who through faith... escaped the edge of the sword, were made strong out of weakness' (Heb 11:34). Hezekiah's faith — spreading the letter before YHWH, believing Isaiah's word, holding the city without further military action — is the OT's supreme example of trust that produces deliverance without human military effort."}
    ]
  },
  "20": {
    "1": [
      {"type": "theme", "target": "Isa 38:1-8", "note": "Hezekiah's illness and healing (2 Kgs 20:1-11) is paralleled in Isa 38:1-8 with the addition of a psalm of thanksgiving (Isa 38:9-20) not found in Kings. The parallel accounts together provide the fullest picture of the Hezekiah narrative: Kings uses it to explain the transition from YHWH's protection to the coming Babylonian threat (20:12-19); Isaiah uses it as a type of death-and-resurrection that anticipates the Servant Songs."}
    ],
    "5": [
      {"type": "allusion", "target": "Heb 5:7", "note": "YHWH's word to Hezekiah — 'I have heard your prayer, I have seen your tears' — is the OT's clearest statement that God hears and is moved by the tears of prayer. Hebrews 5:7 applies the same divine responsiveness to Christ: 'In the days of his flesh, Jesus offered up prayers and supplications, with loud cries and tears, to him who was able to save him from death, and he was heard because of his reverence.' Both Hezekiah and Christ weep in the face of death; both are heard; but where Hezekiah's prayer reverses the sentence, Christ's submission to death fulfills a deeper purpose."},
      {"type": "allusion", "target": "Ps 56:8", "note": "YHWH's notice of Hezekiah's tears ('I have seen your tears') echoes the psalmist's confidence that God stores his tears (Ps 56:8: 'You have kept count of my tossings; put my tears in your bottle'). The divine attention to human weeping is a consistent OT theme that the NT presents as fulfilled in the incarnation: 'Jesus wept' (John 11:35), and the God who notices tears has himself taken on the form of a weeping man."}
    ],
    "6": [
      {"type": "theme", "target": "Rom 15:8", "note": "'I will defend this city for my own sake and for the sake of my servant David' — the double motivation (YHWH's own honor and the Davidic covenant) grounds the defense of Jerusalem. Paul's argument in Romans 15:8 ('Christ became a servant to the circumcised to show God's truthfulness, in order to confirm the promises given to the patriarchs') applies the same logic to the incarnation: God acts for his own sake (truthfulness to promises) and for the sake of the patriarchal covenant. The Davidic covenant that YHWH defends in Hezekiah's crisis is the covenant Christ comes to confirm."}
    ],
    "11": [
      {"type": "allusion", "target": "Josh 10:12-14", "note": "The sundial sign — the shadow retreating ten steps on the stairway of Ahaz — is the OT's second miracle involving the sun (after Joshua's long day, Josh 10:12-14). Both are signs in which YHWH demonstrates sovereignty over time and celestial bodies as confirmation of a decisive act: Joshua's conquest and Hezekiah's healing. The NT presents this sovereignty over time as fulfilled in Christ's resurrection — 'the first day of the week' becomes the new creation's beginning, the Lord of the Sabbath recalibrating sacred time."}
    ],
    "12": [
      {"type": "theme", "target": "Isa 39:1", "note": "Merodach-Baladan's embassy to Hezekiah parallels Isa 39:1-8 verbatim. The juxtaposition is deliberately ironic: immediately after YHWH's miraculous defense of Jerusalem from Assyria, Hezekiah proudly shows Babylon's envoys everything in his treasury. The narrative positions Babylon as the greater threat that Assyria failed to be — the threat that will come to completion in 2 Kgs 25. Isaiah 39 makes the same transition explicitly: after Hezekiah's failure, Isaiah announces the Servant who will accomplish the greater exodus from Babylon (Isa 40:1-5)."}
    ],
    "17": [
      {"type": "shadow", "target": "Dan 1:1-7", "note": "Isaiah's prophecy — 'everything in your palace... will be carried off to Babylon, nothing will be left' — is the first explicit announcement of the Babylonian exile in Kings. Daniel 1:1-7 records the first installment of its fulfillment: Nebuchadnezzar carries off temple vessels and takes 'some of the Israelites from the royal family and the nobility.' Hezekiah's descendants who will be 'eunuchs in the palace of the king of Babylon' (v18) almost certainly include Daniel and his companions (Dan 1:3-6). The prophecy and its fulfillment bracket the fall of Jerusalem."},
      {"type": "theme", "target": "Isa 40:1-2", "note": "The prophecy of Babylonian exile (2 Kgs 20:17 / Isa 39:6-7) is the literary trigger for Isaiah 40:1-2 ('Comfort, comfort my people... her warfare has ended'). The exile announced here in the narrative is the exile that the Servant Songs (Isa 40-55) promise to reverse through a new exodus. Thus 2 Kings 20:17 is the narrative seed of the greatest prophetic promise in the OT — the comfort of a people brought home from Babylon through YHWH's servant."}
    ],
    "19": [
      {"type": "theme", "target": "Phil 4:11", "note": "Hezekiah's response to Isaiah's prophecy of exile — 'The word of the LORD that you have spoken is good... Will there not be peace and security in my days?' — reveals a theologically troubling contentment: peace for himself regardless of what follows. This is not the same as Paul's contentment (Phil 4:11), which is contentment in all circumstances because of Christ. Hezekiah's contentment is a failure of solidarity with future generations — a warning that genuine contentment must encompass the welfare of those who come after."}
    ]
  }
}

def main():
    existing = load_echo('2kings')
    merge_echo(existing, KINGS2_ECHOES)
    save_echo('2kings', existing)
    print('2 Kings 18–20 echoes written.')

if __name__ == '__main__':
    main()
