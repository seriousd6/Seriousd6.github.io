"""
MKT Echo Layer — John chapter 7
Run: python3 scripts/zc-echo-john-7-7.py

Source data used:
- data/interlinear/john.json (Strongs tokens, ch 7)
- data/translation/draft/mediating/john.json (MKT text)
- data/translation/glossary-greek.json (G4151 πνεῦμα dispute_level 3; G2222 ζωή dispute_level 2)
- data/parallels/john.json (empty for ch 7 — nothing to absorb)
- data/echoes/john.json (chs 1–6 present; ch 7 not yet written)
- data/commentary/ellicott/john.json (vv 2, 14, 15, 37–42, 52)

Key decisions:
- v2: The Feast of Tabernacles (Sukkot) is the dominant frame for the chapter; Zech 14:16–19
  is classified 'shadow' rather than 'fulfillment' because John does not cite Zech 14 explicitly,
  though the eschatological resonance is likely deliberate.
- v5: Ps 69:8 ('stranger to my brothers') is classified 'allusion' — the verbal overlap is
  precise and John's use of Ps 69 elsewhere (2:17; 15:25; 19:28) makes intentionality probable.
- v14: Mal 3:1 ('suddenly come to his temple') is classified 'allusion' not 'fulfillment' —
  John does not cite Mal 3:1 directly, but the pattern is structurally precise.
- v16: Deut 18:18 (God puts words in the prophet's mouth) is 'type' — Jesus answers the Mosaic
  prophet expectation but transcends it: the words are not put in his mouth from outside but come
  from the unity of his divine commission.
- v37–38: The water-pouring ceremony at Tabernacles (Simchat Bet HaSho'evah) is the immediate
  liturgical backdrop; Isa 55:1 (allusion) and Zech 14:8 (shadow) are the OT antecedents.
  The 'rivers of living water' citation in v38 does not match any single OT text verbatim;
  it is best read as a composite of Isa 44:3, Ezek 47:1–9, and Zech 14:8.
- v39: Joel 2:28–29 is classified 'fulfillment' because Acts 2:16–21 explicitly identifies
  the Pentecost outpouring as fulfillment of Joel; John 7:39 establishes the precondition
  (glorification) for that fulfillment.
- v40: Deut 18:15 is classified 'type' — Jesus is the Prophet like Moses, though he surpasses
  Moses in authority (v16: his teaching is from God himself, not merely conveyed from God).
- v42: Mic 5:2 is classified 'fulfillment' — NT citations in Matt 2:6 explicitly apply it
  to Jesus; the crowd's question is ironic: they cite the very prophecy Jesus fulfills without
  knowing his Bethlehem birth.
- v52: 2 Kgs 14:25 (Jonah from Gath-hepher in Galilee) is 'allusion' — the Pharisees' claim
  that no prophet arises from Galilee is factually wrong; the echo is implicit irony,
  not a text John cites.
- v53: Classified under textual-tradition theme; the pericope adulterae (7:53–8:11) is absent
  in P66, P75, ‭א, B, and other early witnesses. v53 as transition verse gets a brief theme entry.
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


JOHN_ECHOES = {
  "7": {
    "1": [
      {
        "type": "allusion",
        "target": "Ps 69:4",
        "note": "Those who hate the psalmist without cause and seek to destroy him — a pattern John applies to Jesus across the passion narrative (15:25). The leaders' murderous intent without lawful charge situates Jesus within the persecuted righteous servant tradition."
      },
      {
        "type": "allusion",
        "target": "Jer 26:10-11",
        "note": "Jeremiah's temple speech prompted the priests and prophets to demand his death: 'This man deserves to die.' The pattern of religious authorities seeking a prophet's death for his public teaching is the direct antecedent for John 7's conflict."
      }
    ],
    "2": [
      {
        "type": "shadow",
        "target": "Lev 23:34-36",
        "note": "The Feast of Tabernacles (Sukkot) — commanded in Leviticus as a seven-day feast at harvest commemorating Israel's wilderness dwelling in booths — is the liturgical frame for the entire chapter. Jesus acts and speaks within and against this festival's symbolism."
      },
      {
        "type": "shadow",
        "target": "Zech 14:16-19",
        "note": "Zechariah's eschatological vision culminates in all nations going up to Jerusalem to worship at the Feast of Tabernacles — the feast becomes the site of universal covenant renewal. John's setting of Jesus's decisive water-cry at this feast places him at the center of that eschatological expectation."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Ps 69:8",
        "note": "The psalmist laments: 'I am a stranger to my own brothers, an alien to my own mother's sons.' Jesus's brothers urging him toward a public demonstration — without believing in him — fits this pattern of family estrangement that John has drawn on throughout (Ps 69 is quoted at 2:17 and 15:25)."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Isa 52:10",
        "note": "The brothers' demand that Jesus 'show himself to the world' ironically echoes the eschatological disclosure: 'The LORD will lay bare his holy arm in the sight of all the nations.' The brothers want a political unveiling; the Isaianic disclosure will come through crucifixion and resurrection, not a festival performance."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Ps 69:8",
        "note": "John's editorial comment that even Jesus's brothers did not believe in him precisely matches the psalmist's lament ('I am a stranger to my own brothers'). John's multiple uses of Ps 69 suggest a deliberate pattern — the righteous sufferer whose own household rejects him anticipates the Servant's rejection."
      }
    ],
    "6": [
      {
        "type": "theme",
        "target": "Hab 2:3",
        "note": "Habakkuk's oracle about the appointed time: 'the revelation awaits an appointed time; it speaks of the end and will not prove false. Though it linger, wait for it; it will certainly come.' Jesus's 'my time (kairos) is not yet here' reflects this OT conviction that divine action moves according to a fixed schedule, not human pressure."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Amos 5:10",
        "note": "Amos condemns those who 'hate the one who upholds justice in the court and detest the one who tells the truth.' The world's hatred of Jesus is specifically because he testifies against its evil works — the same truth-speaking that provoked hatred of the prophets."
      },
      {
        "type": "allusion",
        "target": "Ps 69:4",
        "note": "The psalmist is hated 'without reason' by more enemies than hairs on his head. Jesus identifies the world's hatred as directed specifically at him, not at the brothers — the pattern of unjust hostility toward the servant continues."
      }
    ],
    "8": [
      {
        "type": "theme",
        "target": "Deut 16:16",
        "note": "Moses commanded all Israelite males to appear before the LORD three times a year, including at Tabernacles. Jesus declines to go up on the brothers' timetable — his eventual going will be governed by divine appointment rather than covenant obligation, relocating the authority behind the pilgrimage."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "1 Kgs 19:3",
        "note": "Elijah's strategic withdrawal to Horeb when under threat is the OT paradigm for the prophet who does not move before the appointed time. Jesus's remaining in Galilee follows this pattern of withdrawal followed by decisive action — though unlike Elijah, Jesus's timing is governed entirely by the Father's schedule, not self-preservation."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Isa 49:2",
        "note": "The Servant describes himself: 'He made me into a polished arrow and concealed me in his quiver.' Jesus's secret ascent to the feast enacts this hiddenness of the Servant — present but not yet disclosed, waiting for the moment of unveiling."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Ps 63:1",
        "note": "The psalmist 'seeks' God earnestly. The leaders' seeking of Jesus at the feast is an ironic inversion — they seek him not to receive but to destroy. The verb (G2212 ζητέω) carries both senses; the one who should be sought as the LORD is being hunted by the guardians of the sanctuary."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Isa 53:3",
        "note": "The divided crowd response — 'a good man' vs. 'he deceives the people' — enacts the reception of the Servant, who is 'despised and rejected by mankind.' The charge of deception echoes Deut 13:5's warning against the false prophet who leads Israel astray; the irony is that the true prophet is charged with the false prophet's crime."
      },
      {
        "type": "allusion",
        "target": "Deut 13:5",
        "note": "The Mosaic law prescribed death for a prophet who 'entices you to rebel against the LORD your God' and 'led you astray.' The charge that Jesus 'deceives the people' deploys this legal category — the leaders are processing his ministry through the false-prophet statute, which shapes the escalating hostility through chapter 7."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Isa 59:14-15",
        "note": "Isaiah describes a state where 'truth has stumbled in the public square... whoever shuns evil becomes a prey.' The crowd's silencing out of fear for the leaders reflects this prophesied condition where public speech about the righteous is suppressed by those who abuse their authority."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Mal 3:1",
        "note": "Malachi promises: 'Then suddenly the Lord you are seeking will come to his temple; the messenger of the covenant, whom you desire, will come.' Jesus's unannounced mid-feast appearance in the temple courts to teach fulfills this structural pattern — sudden, unexpected, authoritative arrival in the sanctuary."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Isa 50:4-5",
        "note": "The Servant's speech: 'The Sovereign LORD has given me a well-instructed tongue, to know the word that sustains the weary. He wakens me morning by morning, wakens my ear to listen like one being instructed.' The leaders marvel at Jesus's literacy without rabbinic formation; the Servant's answer is that his teaching comes from divine instruction, not human schooling."
      }
    ],
    "16": [
      {
        "type": "type",
        "target": "Deut 18:18",
        "note": "God's promise: 'I will raise up for them a prophet like you from among their fellow Israelites, and I will put my words in his mouth.' Jesus directly answers the type: his teaching is not his own but from the one who sent him. Yet he transcends the Mosaic prophet pattern — the words are not placed in his mouth from outside but arise from his unity with the Father."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Ps 25:14",
        "note": "'The LORD confides in those who fear him; he makes his covenant known to them.' Jesus's epistemological principle — do God's will and you will recognize God's teaching — echoes this covenantal dynamic: knowledge of God follows commitment to God, not intellectual investigation from outside."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Num 16:28",
        "note": "Moses vindicates his divine commission by appealing to his selflessness: 'This is how you will know that the LORD has sent me to do all these things and that it was not my idea.' Jesus uses the same criterion — one who seeks the glory of the sender rather than his own glory is trustworthy. The parallel vindicates Jesus's commission by the standard Moses himself established."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Deut 31:29",
        "note": "Moses's final warning: 'For I know that after my death you are sure to become utterly corrupt and to turn from the way I have commanded you.' Jesus's accusation that none of them keeps the law fulfills Moses's own prediction — the law-givers who claim Moses have followed precisely the path Moses warned against."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "1 Kgs 18:17",
        "note": "Ahab's charge against Elijah — 'Is that you, you troubler of Israel?' — is the paradigm for the crowd's accusation that Jesus is demon-possessed and making false charges. The crowd's denial that anyone seeks his life echoes the broader pattern: those complicit in persecution deny the threat to the prophet."
      }
    ],
    "21": [
      {
        "type": "theme",
        "target": "Exod 34:10",
        "note": "God's covenant pledge: 'I will do wonders never before done in any nation in all the world.' Jesus appeals to his one work at Bethesda (ch 5) as a deed that should produce discernment rather than amazement that leads to no commitment — the pattern of signs-without-understanding that runs from Sinai onward."
      }
    ],
    "22": [
      {
        "type": "quote",
        "target": "Gen 17:12",
        "note": "God's command to Abraham: 'every male among you who is eight days old must be circumcised.' Jesus cites this against the Sabbath charge — circumcision was practiced on the Sabbath when the eighth day fell there, by rabbinical consensus. The patriarchal precedent predates and overrides Sabbath restriction by the leaders' own logic."
      },
      {
        "type": "quote",
        "target": "Lev 12:3",
        "note": "'On the eighth day the boy is to be circumcised.' The Levitical codification of Abraham's command is the specific text Jesus invokes: circumcision affecting a single member of the body overrides Sabbath prohibition; healing a whole body should do so with greater force."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Lev 12:3",
        "note": "The qal wahomer (lighter-to-heavier) argument: if circumcision — affecting one part of the body — overrides Sabbath, then healing a man's whole body must a fortiori override it. Jesus argues from within the Torah's own logic; those who accept Lev 12:3 as ground for Sabbath exception cannot consistently condemn the Bethesda healing."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Lev 19:15",
        "note": "'Do not pervert justice; do not show partiality to the poor or favoritism to the great, but judge your neighbor fairly.' Jesus's command to 'judge righteous judgment' quotes the Levitical standard directly. The leaders' judgment by appearance — condemning the Sabbath healing on surface legalism while allowing Sabbath circumcision — is precisely the partiality Lev 19:15 prohibits."
      },
      {
        "type": "allusion",
        "target": "Isa 11:3-4",
        "note": "The messianic king 'will not judge by what he sees with his eyes, or decide by what he hears with his ears; but with righteousness he will judge.' Jesus's call to righteous judgment implicitly identifies who alone can fulfill it — the one who embodies the Isaianic standard, not those who judge by appearance."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Jer 26:8-11",
        "note": "Jeremiah's temple speech prompted priests and false prophets to seize him: 'This man should be sentenced to death because he has prophesied against this city.' The Jerusalem crowd's observation — 'isn't this the man they are trying to kill?' — situates Jesus in the exact pattern of prophets threatened with death for their temple testimony."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Gen 49:10",
        "note": "Jacob's blessing of Judah: 'The scepter will not depart from Judah... until he to whom it belongs shall come and the obedience of the nations shall be his.' The crowd asks whether the rulers have concluded Jesus is the Messiah — they invoke the messianic category without grasping that the criteria for messianic recognition are being met before them."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Mal 3:1",
        "note": "The crowd's expectation that the Messiah's origin will be unknown reflects a tradition developed from Mal 3:1 ('suddenly come to his temple') — his arrival will be dramatic and unexpected, his provenance mysterious. The crowd uses this expectation to disqualify Jesus; the irony is that his true origin (from the Father, v29) is exactly the divine mystery Malachi gestures toward."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Isa 48:16",
        "note": "Isaiah's Servant: 'From the first announcement I have not spoken in secret; at the time it happens, I am there. And now the Sovereign LORD has sent me, endowed with his Spirit.' Jesus's cry in the temple — 'I am not here on my own authority; he who sent me is true' — follows the same pattern of divine commissioning that Isa 48:16 articulates."
      },
      {
        "type": "allusion",
        "target": "Exod 3:14",
        "note": "Jesus's 'I am (ἐγώ εἰμι) not here on my own authority' — while not the bare divine Name — draws on the Exodus self-disclosure tradition. The contested claim 'you know me and know where I am from' asserts a knowledge that transcends biographical fact: his true origin is the Father who sent him."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Isa 49:1",
        "note": "'The LORD called me from the womb; from my mother's body he has mentioned my name.' The prophetic pattern of being known by God from before birth is the OT register for Jesus's claim to know the Father because he is from him. Yet Jesus's relationship exceeds prophetic commission: prophets are known by God; Jesus knows God from within a prior unity with him."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Ps 31:15",
        "note": "'My times are in your hands; deliver me from the hands of my enemies.' The repeated Johannine refrain that 'his hour had not yet come' (3:6; 7:8; 8:20; 12:23) enacts this psalmist's trust — divine sovereignty over timing overrides every human attempt to seize or harm before the appointed moment."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Isa 35:5-6",
        "note": "Isaiah's vision of the messianic age: 'Then will the eyes of the blind be opened and the ears of the deaf unstopped. Then will the lame leap like a deer.' The crowd's question — 'when the Messiah comes, will he perform more signs than this man?' — draws on exactly this expectation. Jesus's healings are already the Isaianic index of messianic arrival."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "Jer 20:1-2",
        "note": "Pashur the priest had Jeremiah beaten and put in stocks for his temple prophecy. The chief priests and Pharisees' dispatch of guards to arrest Jesus repeats this pattern: religious authorities mobilizing force against the prophet whose temple speech destabilizes their authority."
      }
    ],
    "33": [
      {
        "type": "allusion",
        "target": "Isa 55:6",
        "note": "'Seek the LORD while he may be found; call on him while he is near.' Jesus's announcement of his departure sets a time limit: 'I am with you for only a short time.' The logic of Isa 55:6 — presence is temporary and the window for seeking will close — is what Jesus applies to his own ministry."
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "Prov 1:28",
        "note": "Wisdom's warning: 'Then they will call to me but I will not answer; they will look for me but will not find me.' Jesus's announcement — 'you will seek me but will not find me' — directly activates this Wisdom tradition. Those who dismiss the present call of Wisdom face the condition where seeking becomes futile because the moment has passed."
      },
      {
        "type": "allusion",
        "target": "Hos 5:15",
        "note": "'Then I will return to my lair until they have borne their guilt and seek my face — in their misery they will earnestly seek me.' The LORD's withdrawal in Hosea until repentance shapes the theological grammar of Jesus's announcement: the going away is not abandonment but a withdrawal that leaves seeking without resolution for those who refused to receive."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Isa 11:10-12",
        "note": "Isaiah's vision: 'In that day the Root of Jesse will stand as a banner for the peoples; the nations will rally to him.' The leaders' mocking question about Jesus going to 'teach the Greeks' is ironic prophecy — the Gentile mission they cannot imagine is precisely what the Isaianic trajectory requires. Their jest anticipates the actuality."
      },
      {
        "type": "allusion",
        "target": "Isa 49:6",
        "note": "'I will also make you a light for the Gentiles, that my salvation may reach to the ends of the earth.' The Servant's commission to the Gentiles is what the leaders unwittingly describe. The Diaspora mission they frame as absurd is the Servant's mandate the text has already announced."
      }
    ],
    "36": [
      {
        "type": "theme",
        "target": "Deut 4:29",
        "note": "'But if from there you seek the LORD your God, you will find him if you seek him with all your heart and with all your soul.' The leaders puzzle over 'where I am you cannot come,' which echoes the Deuteronomic condition for finding God: seeking with the whole heart. The condition they refuse is the very one that would resolve their confusion."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Isa 55:1",
        "note": "'Come, all you who are thirsty, come to the waters.' Jesus's cry on the last day of Tabernacles directly echoes this Isaianic invitation — the open public call to the thirsty to come. The Feast of Tabernacles had a daily water-drawing ceremony (Simchat Bet HaSho'evah) where a priest drew water from the Pool of Siloam and poured it on the altar; Jesus positions himself as the source the ceremony anticipated."
      },
      {
        "type": "shadow",
        "target": "Zech 14:8",
        "note": "Zechariah's eschatological vision: 'On that day living water will flow out from Jerusalem, half of it east to the Dead Sea and half of it west to the Mediterranean Sea.' The 'last day' of Tabernacles, the eschatological feast of Zech 14:16, is the precise moment Jesus invites the thirsty — standing himself as the source of Zechariah's living water."
      }
    ],
    "38": [
      {
        "type": "allusion",
        "target": "Ezek 47:1-9",
        "note": "Ezekiel's vision of water flowing from under the temple threshold, deepening as it flows, until 'wherever the river flows everything will live.' The 'rivers of living water' flowing from the believer who comes to Christ draws on this temple-river imagery — the source is now not the literal temple but the person of Jesus, in whom the new temple has arrived."
      },
      {
        "type": "allusion",
        "target": "Isa 44:3",
        "note": "'For I will pour water on the thirsty land, and streams on the dry ground; I will pour out my Spirit on your offspring.' This verse links the water and the Spirit, the same connection John makes in v39. The 'rivers of living water' citation in v38 is likely a composite of several texts, of which Isa 44:3 is one of the most direct antecedents."
      }
    ],
    "39": [
      {
        "type": "fulfillment",
        "target": "Joel 2:28-29",
        "note": "'And afterward, I will pour out my Spirit on all people.' Peter identifies Pentecost as the fulfillment of this promise (Acts 2:16–21). John 7:39 establishes the precondition: the Spirit could not be given until Jesus was glorified. The Johannine 'glorification' (lifting up on the cross, resurrection, ascension) is the event that releases the Joel promise."
      },
      {
        "type": "allusion",
        "target": "Ezek 36:26-27",
        "note": "'I will give you a new heart and put a new spirit in you... I will put my Spirit in you and move you to follow my decrees.' Ezekiel's new-covenant promise of the indwelling Spirit is what John 7:39 anticipates — the glorification of Jesus is the moment the Ezekielian promise of Spirit-given obedience becomes available."
      }
    ],
    "40": [
      {
        "type": "type",
        "target": "Deut 18:15",
        "note": "'The LORD your God will raise up for you a prophet like me from among your fellow Israelites; you must listen to him.' The crowd's identification of Jesus as 'the Prophet' deploys this Mosaic category. Jesus is the Prophet like Moses — teaching with divine authority, speaking only what the Father commands — but his relationship to the law he teaches is not that of a successor to Moses but of the one to whom Moses pointed."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "Mic 5:2",
        "note": "The Messiah's expected Bethlehem origin derives from Mic 5:2. The crowd's objection — 'How can the Messiah come from Galilee?' — cites this expectation as grounds for disqualification. The irony John builds here is that Jesus was born in Bethlehem (as Matthew and Luke record), making the crowd's objection the very evidence John expects the reader to supply."
      }
    ],
    "42": [
      {
        "type": "fulfillment",
        "target": "Mic 5:2",
        "note": "'But you, Bethlehem Ephrathah, though you are small among the clans of Judah, out of you will come for me one who will be ruler over Israel, whose origins are from of old, from ancient times.' Matt 2:6 explicitly applies this to Jesus. The crowd cites the prophecy thinking it disqualifies him; the reader of the Gospel knows it confirms him."
      },
      {
        "type": "allusion",
        "target": "2 Sam 7:12-13",
        "note": "God's promise to David: 'I will raise up your offspring to succeed you... I will establish the throne of his kingdom forever.' The crowd's requirement that the Messiah come from David's line and from Bethlehem correctly reflects the 2 Samuel promise. Jesus fulfills both — his Davidic descent is the genealogical basis the prophecy requires."
      }
    ],
    "43": [
      {
        "type": "allusion",
        "target": "Isa 8:14-15",
        "note": "Isaiah describes the LORD himself as a 'stone that causes people to stumble and a rock that makes them fall.' The division (σχίσμα, schism) among the people because of Jesus enacts the Isaianic pattern: the presence of God does not produce uniform reception but forced differentiation between those who stumble and those who shelter."
      }
    ],
    "44": [
      {
        "type": "allusion",
        "target": "Ps 124:7",
        "note": "'We have escaped like a bird from the fowler's snare; the snare has been broken, and we have escaped.' The divine protection that prevents anyone from seizing Jesus reflects this psalmist's confidence in God's deliverance from those who seek to ensnare the righteous — the hour not yet come is the broken snare."
      }
    ],
    "45": [
      {
        "type": "theme",
        "target": "Deut 18:18-19",
        "note": "God's warning: 'I will put my words in his mouth... If anyone does not listen to my words that the prophet speaks in my name, I myself will call them to account.' The guards' inability to arrest Jesus is matched by their admission that 'no one ever spoke the way this man does' — they are experiencing the authority of the Mosaic Prophet's speech that God himself guaranteed would be unignorable."
      }
    ],
    "46": [
      {
        "type": "allusion",
        "target": "Isa 50:4",
        "note": "'The Sovereign LORD has given me a well-instructed tongue, to know the word that sustains the weary.' The guards' verdict — 'no one ever spoke the way this man does' — is the reaction the Servant's divinely-given speech was designed to produce. The authority they cannot resist is the authority the Servant received from the LORD each morning."
      }
    ],
    "47": [
      {
        "type": "allusion",
        "target": "Jer 5:31",
        "note": "'The prophets prophesy lies, the priests rule by their own authority, and my people love it this way.' The Pharisees' assumption that the guards have been 'deceived' reflects the self-sustaining logic Jeremiah describes: leadership that is itself self-serving can only interpret the guards' honesty as corruption by the crowd's error."
      }
    ],
    "48": [
      {
        "type": "allusion",
        "target": "Isa 53:3",
        "note": "The Servant was 'despised and rejected by mankind — a man of suffering.' The Pharisees' rhetorical appeal — 'Have any of the rulers or Pharisees believed in him?' — makes elite rejection the criterion of theological truth. This is precisely the social logic that produces the Servant's rejection: status and authority become the measure of legitimacy."
      }
    ],
    "49": [
      {
        "type": "allusion",
        "target": "Deut 28:15-20",
        "note": "Moses warned: 'If you do not obey the LORD your God... all these curses will come on you and overtake you.' The Pharisees pronounce the crowd 'cursed' for not knowing the law — deploying the Deuteronomic curse. The irony is layered: Jesus has argued (v19) that the leaders themselves do not keep the law, placing them under the very curse they project onto others."
      }
    ],
    "50": [
      {
        "type": "theme",
        "target": "Exod 23:1-3",
        "note": "'Do not spread false reports. Do not help a guilty person by being a malicious witness... do not follow the crowd in doing wrong.' Nicodemus invokes Mosaic due process — hear the man first — which the Torah itself commands. His appeal is not legal technicality but faithfulness to the same law the leaders claim to uphold."
      }
    ],
    "51": [
      {
        "type": "allusion",
        "target": "Deut 19:15-17",
        "note": "'One witness is not enough to convict anyone accused of any crime or offense... A matter must be established by the testimony of two or three witnesses.' Nicodemus's question — 'Does our law condemn a man without first hearing him?' — invokes this Deuteronomic requirement. The leaders are trying to condemn Jesus without the process the Torah mandates."
      }
    ],
    "52": [
      {
        "type": "allusion",
        "target": "2 Kgs 14:25",
        "note": "Jonah son of Amittai was 'from Gath-hepher' — a town in Galilee (in the tribal territory of Zebulun). The Pharisees' claim that 'a prophet does not come out of Galilee' is historically false by their own scriptures. John may intend this as irony: the council dismisses Jesus's Galilean origin while Galilee had already produced at least one canonical prophet."
      }
    ],
    "53": [
      {
        "type": "theme",
        "target": "1 Kgs 22:17",
        "note": "Micaiah's vision of Israel 'scattered on the hills like sheep without a shepherd' pictures a people whose leadership has failed them. The crowd dispersing to their homes after the divided verdict of chapter 7 — with no resolution, no shepherd, and no authoritative word accepted — enacts this prophetic image of Israel without true guidance."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 7 echoes written.')

if __name__ == '__main__':
    main()
