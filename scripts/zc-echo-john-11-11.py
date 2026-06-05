"""
MKT Echo Layer — John chapter 11
Run: python3 scripts/zc-echo-john-11-11.py

Source data used:
- data/interlinear/john.json (Strongs tokens, ch 11)
- data/translation/draft/mediating/john.json (MKT text, all 57 verses)
- data/translation/glossary-greek.json (G1690 ἐμβριμάομαι, G2222 ζωή, G386 ἀνάστασις)
- data/parallels/john.json (v51: Dan 9:25-26 → absorbed as fulfillment)
- data/echoes/john.json (empty for ch 11)

Key decisions:
- v11: κεκοίμηται (perfect passive of κοιμάω) deliberately activates Dan 12:2 "sleep in dust"
  vocabulary; classified as fulfillment (NT explicitly frames it as resurrection sleep).
- v21/32: Martha and Mary's "if you had been here" echoed against 2 Kgs 4:27 (Shunammite);
  classified as allusion — the structural parallel is precise but John does not cite it.
- v25: Three echoes (Dan 12:2, Deut 32:39, Isa 26:19) each address a distinct aspect of the
  "I am the resurrection" claim; all three retained.
- v35 (Jesus wept): Isa 53:3 and Jer 9:1 chosen over more generic grief texts; the Servant
  passage is the stronger theological anchor.
- v41: 1 Kgs 18:36-37 (Elijah at Carmel) chosen as primary echo — the structural parallel
  (public prayer before resurrection-sign for a crowd's faith) is closer than Elisha parallels.
- v47: Ps 2:2 classified as fulfillment — the NT explicitly reads the Sanhedrin's gathering
  against Jesus through this psalm (Acts 4:25-28).
- v50-51: Isa 53:8 and Dan 9:26 both retained for v51; Isa 53:8 alone for v50 — Caiaphas'
  political statement is the unconscious echo; the narrator's divine intention in v51 warrants
  the Danielic fulfillment.
- v52: Three OT ingathering texts (Isa 56:8, Jer 31:10, Ezek 34:13) each add a distinct nuance;
  Isa 56:8 is primary (the explicit "others besides those already gathered").
- v53: Ps 2:1-2 as fulfillment (confirmed by Acts 4); Jer 11:19 as allusion (innocent lamb
  led to slaughter by a plot — structural type rather than prophetic citation).
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
  "11": {
    "1": [
      {
        "type": "theme",
        "target": "Ps 116:15",
        "note": "'Precious in the sight of the LORD is the death of his faithful servants.' The Hebrew name underlying Lazarus (Elʿazar, 'God has helped') signals the chapter's theological direction: the death of someone beloved by God is not the end but the occasion for divine action."
      }
    ],
    "2": [
      {
        "type": "theme",
        "target": "Ps 23:5",
        "note": "The anointing Mary performed on Jesus (narrated fully in ch 12 but cross-referenced here) echoes the anointing of Ps 23: 'you anoint my head with oil.' What was a gesture of costly hospitality becomes an anticipatory consecration of the one about to pass through the valley of death."
      }
    ],
    "3": [
      {
        "type": "theme",
        "target": "Ps 91:14-15",
        "note": "'Because he loves me, says the LORD, I will rescue him... He will call on me, and I will answer him; I will be with him in trouble.' The sisters' appeal — 'the one you love is sick' — follows the Psalm's pattern: the beloved calls from distress, counting on the bond of love to move God to act."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Ps 118:17-18",
        "note": "'I will not die but live, and will proclaim what the LORD has done. The LORD has chastened me severely, but he has not given me over to death.' Jesus' declaration that the sickness 'will not end in death' but will serve divine glory echoes the Psalm's pattern: apparent fatal crisis becomes the platform for declaring God's power."
      },
      {
        "type": "allusion",
        "target": "Isa 40:5",
        "note": "'The glory of the LORD will be revealed, and all people will see it together.' Jesus names the glory of God as the purpose of the crisis — framing the raising of Lazarus as a moment of divine self-disclosure of the kind Isaiah announced."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Deut 7:8",
        "note": "'It is because the LORD loved you...' The narrator's note that Jesus 'loved' (ἠγάπα, G25 — the covenantal love term) Martha, Mary, and Lazarus places this personal friendship within the register of the divine ἀγαπάω that drives God's election and rescue of his people."
      }
    ],
    "6": [
      {
        "type": "theme",
        "target": "Isa 55:8-9",
        "note": "'My thoughts are not your thoughts, neither are your ways my ways... as the heavens are higher than the earth, so are my ways higher than your ways.' Jesus' deliberate two-day delay, which from human perspective appears to abandon the one he loves, follows a divine logic that transcends the expectation of immediate rescue."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Isa 50:7",
        "note": "'Because the Sovereign LORD helps me, I will not be disgraced. Therefore have I set my face like flint.' The Servant's resolve to go toward Jerusalem despite mortal danger is the OT template for Jesus' decision to return to Judea where the authorities had sought to stone him."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Ps 31:13",
        "note": "'For I hear many whispering, terror on every side! They conspire against me and plot to take my life.' The disciples' reminder that the Jewish leaders were trying to stone Jesus echoes the Psalmist's situation of the righteous one surrounded by those who seek his death — a pattern that will intensify through the passion narrative."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Jer 13:16",
        "note": "'Give glory to the LORD your God before he brings the darkness, before your feet stumble on the darkening hills.' Jesus' saying about twelve daylight hours — walk by day and you will not stumble — directly inverts Jeremiah's warning: Jeremiah urges haste before light is gone; Jesus asserts that those who follow him walk in the light that makes stumbling impossible."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Isa 59:9-10",
        "note": "'We look for light, but all is darkness; for brightness, but we walk in deep shadows. Like the blind we grope along the wall, feeling our way like people without eyes; we stumble at midday as if it were twilight.' Isaiah's description of those who have no light is the condition Jesus identifies: walking in night because 'the light is not in them' — darkness is internal, not merely circumstantial."
      }
    ],
    "11": [
      {
        "type": "fulfillment",
        "target": "Dan 12:2",
        "note": "'Multitudes who sleep in the dust of the earth will awake, some to everlasting life, others to shame and everlasting contempt.' Jesus' use of κεκοίμηται (has fallen asleep) for Lazarus' death deliberately activates the Daniel 12 vocabulary for the dead awaiting resurrection — and his going to 'wake him up' reframes the raising as a foretaste of the last-day awakening Daniel foretold."
      },
      {
        "type": "allusion",
        "target": "1 Kgs 2:10",
        "note": "David 'rested with his ancestors and was buried in the City of David' — the OT idiom of death as rest/sleep that Jesus' language echoes. The disciples' confusion in v12 shows how naturalized this euphemism had become; Jesus uses it to reframe death as temporary rest before divine waking."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Isa 6:9-10",
        "note": "'Be ever hearing, but never understanding; be ever seeing, but never perceiving.' The disciples' misunderstanding of plain speech — taking death-as-sleep literally — instantiates the Isaianic pattern of those who hear but cannot grasp, though here the misunderstanding is correctable rather than the hardening of the Pharisees."
      }
    ],
    "13": [
      {
        "type": "theme",
        "target": "Prov 26:7",
        "note": "'Like a lame man's legs that hang limp is a proverb in the mouth of a fool.' The narrator's clarifying aside — Jesus spoke of death, they thought he meant sleep — illustrates the gap between the speaker's register and the hearers'. Wisdom's vocabulary requires spiritual ears to decode; without them, even direct speech about death reads as banality."
      }
    ],
    "14": [
      {
        "type": "theme",
        "target": "Amos 3:7",
        "note": "'Surely the Sovereign LORD does nothing without revealing his plan to his servants the prophets.' Jesus tells the disciples plainly ('Lazarus is dead') only after the two-day delay has served its purpose. The plain disclosure follows the divine pattern: God reveals his intentions to those who walk with him before he acts."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Isa 53:10",
        "note": "'Yet it was the LORD's will to crush him and cause him to suffer... the LORD makes his life an offering for sin.' Jesus is 'glad' he was not present to prevent the death — the apparent tragedy is the necessary condition for a greater act. The logic that apparent harm serves divine purpose echoes the Servant's suffering, which was also the Father's will for the sake of others' faith."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "Ruth 1:16-17",
        "note": "'Where you go I will go, and where you stay I will stay... where you die I will die.' Thomas' declaration — 'let us also go, that we may die with him' — echoes Ruth's covenant-loyalty that goes even unto death. Both express the deepest form of solidarity: following the beloved into mortal danger, not from certainty of survival but from the bond itself."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Ezek 37:11",
        "note": "'These bones are the whole house of Israel. They say, Our bones are dried up and our hope is gone; we are cut off.' Four days in the tomb was the ancient marker of irreversible death — beyond any natural hope of recovery. This is precisely the 'no hope' condition Ezekiel's valley of dry bones depicted, the condition into which Jesus now comes."
      }
    ],
    "18": [
      {
        "type": "theme",
        "target": "Mic 5:2",
        "note": "'But you, Bethlehem Ephrathah, though you are small among the clans of Judah, out of you will come for me one who will be ruler over Israel.' The narrator's geographical note — Bethany is less than two miles from Jerusalem — echoes the OT pattern where events in seemingly insignificant places near Jerusalem carry world-historical weight."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Job 2:11-13",
        "note": "Job's three friends came to comfort him, sitting with him in silence for seven days — the OT model of communal mourning solidarity. The many Jews who come to comfort Martha and Mary follow this ancient pattern of presence-in-grief. Their witness to the raising will turn mourners into divided testimony-bearers."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "Gen 18:2",
        "note": "Abraham 'ran from the entrance of his tent to meet them' when the three divine visitors appeared at Mamre. Martha's going out to meet Jesus as soon as she hears he is coming echoes the patriarch's eager movement toward the divine visitor — an instinct of welcome that the story will vindicate."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "2 Kgs 4:28",
        "note": "The Shunammite woman, whose son had just died, confronted Elisha: 'Did I ask you for a son, my lord? Didn't I tell you, Don't raise my hopes?' — an accusation wrapped in grief. Martha's words to Jesus, 'if you had been here, my brother would not have died,' follow the same structural pattern: the grieving person appeals to the prophet/man of God with implicit rebuke of delay."
      },
      {
        "type": "allusion",
        "target": "Ps 22:11",
        "note": "'Do not be far from me, for trouble is near and there is no one to help.' The lament to God about absence in crisis is the Psalmic template for Martha's words — the complaint that God was not present when most needed, which is itself a form of faith that expects his presence to matter."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "1 Kgs 17:20-21",
        "note": "Elijah stretched himself over the dead child three times and cried to the LORD — and the child was restored. Martha's statement 'I know that even now God will give you whatever you ask' follows the prophetic intercession pattern exactly: the prophet's petition to God on behalf of the dead, with the expectation of divine response."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Isa 26:19",
        "note": "'Your dead will live, LORD; their bodies will rise — let those who dwell in the dust wake up and shout for joy.' Jesus' statement 'your brother will rise again' invokes precisely this OT resurrection hope; Martha will demonstrate in v24 that she understands the reference, placing the exchange within Israel's eschatological expectation."
      }
    ],
    "24": [
      {
        "type": "fulfillment",
        "target": "Dan 12:2",
        "note": "Martha's articulation — 'he will rise again in the resurrection at the last day' — is the hope of Daniel 12:2 stated verbatim. She represents the best of Second Temple resurrection theology, correctly interpreting the OT data, while being about to discover that the one who will bring that resurrection stands before her."
      }
    ],
    "25": [
      {
        "type": "fulfillment",
        "target": "Dan 12:2",
        "note": "'Multitudes who sleep in the dust will awake, some to everlasting life.' The resurrection Daniel described as a future divine act Jesus personifies: 'I am the resurrection' — not merely the one who performs it but the person in whom the resurrection-power resides. The ἐγώ εἰμι claims divine life-authority."
      },
      {
        "type": "allusion",
        "target": "Deut 32:39",
        "note": "'I put to death and I bring to life; I have wounded and I will heal, and no one can deliver out of my hand.' This divine monopoly on resurrection power in Moses' song is what Jesus claims personally: the exclusive authority over death and life that the Song of Moses reserves for YHWH alone."
      },
      {
        "type": "allusion",
        "target": "Isa 26:19",
        "note": "'Your dead will live, LORD; their bodies will rise.' The resurrection Isaiah prophesied as God's act for his people is here declared by Jesus as fulfilled in his own person — he does not merely announce it but identifies himself as the resurrection's source and substance."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Isa 25:8",
        "note": "'He will swallow up death forever. The Sovereign LORD will wipe away the tears from all faces.' The eschatological end of death that Isaiah foretells is what Jesus offers as a present reality for the believer: 'whoever lives by believing in me will never die.' Isaiah's future-tense divine act becomes Jesus' present-tense gift."
      },
      {
        "type": "allusion",
        "target": "Ps 16:10-11",
        "note": "'You will not abandon me to the realm of the dead... you make known to me the path of life; you will fill me with joy in your presence.' The Davidic confidence that God will not leave him in death — which Peter applies to the resurrection in Acts 2:27 — Jesus extends to all believers: the life that cannot be abandoned to death is available to all who believe."
      }
    ],
    "27": [
      {
        "type": "fulfillment",
        "target": "Ps 2:7",
        "note": "'You are my Son; today I have begotten you' — the divine declaration to the anointed Davidic king. Martha's confession 'you are the Son of God' applies this messianic title to Jesus directly; her identification of him as 'the one who is to come into the world' echoes the enthronement psalm's proclamation of the king's divine sonship."
      },
      {
        "type": "fulfillment",
        "target": "Dan 9:25",
        "note": "'From the time the word goes out to restore and rebuild Jerusalem until the Anointed One, the ruler, comes...' Martha identifies Jesus as 'the Messiah' — the expected Anointed One of Daniel's reckoning. Her confession at the tomb is the climactic moment when the Danielic title is claimed in the context of death and resurrection."
      }
    ],
    "28": [
      {
        "type": "theme",
        "target": "Isa 30:20-21",
        "note": "'Your teachers will be hidden no more; with your own eyes you will see them. Whether you turn to the right or to the left, your ears will hear a voice behind you, saying, This is the way; walk in it.' Martha's announcement 'the Teacher is here and is asking for you' enacts this Isaianic promise: the hidden teacher becomes visible and present at the moment of grief."
      }
    ],
    "29": [
      {
        "type": "theme",
        "target": "Ps 119:60",
        "note": "'I will hasten and not delay to obey your commands.' Mary's quick response — 'she got up quickly and went to him' — embodies the Psalmist's posture toward divine summons. The readiness to move immediately at the Teacher's call is the mark of the one who has truly heard."
      }
    ],
    "30": [
      {
        "type": "theme",
        "target": "Exod 3:5",
        "note": "'Do not come any closer,' God said. 'Take off your sandals, for the place where you are standing is holy ground.' Jesus remaining at the liminal space outside the village, where Martha met him, marks the encounter site as threshold-ground — the ordinary boundary becomes the location of the extraordinary meeting."
      }
    ],
    "31": [
      {
        "type": "theme",
        "target": "Isa 61:2-3",
        "note": "'To comfort all who mourn... to bestow on them a crown of beauty instead of ashes, the oil of joy instead of mourning, and a garment of praise instead of a spirit of despair.' The Jews follow Mary toward the tomb to mourn; they will instead encounter the one who fulfills the Isaianic comfort — the mourning will be turned to joy in the same visit."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "2 Kgs 4:27",
        "note": "The Shunammite fell at Elisha's feet in bitter grief when her son died: 'She came to the man of God at the mountain and caught hold of his feet.' Mary falling at Jesus' feet and repeating Martha's words — 'Lord, if you had been here, my brother would not have died' — follows the same exact gesture and cry. Both women approach the prophet-figure in prostrate grief with the same implicit appeal."
      }
    ],
    "33": [
      {
        "type": "allusion",
        "target": "Isa 63:9",
        "note": "'In all their distress he too was distressed, and the angel of his presence saved them.' God's sharing in his people's suffering — entering into their grief rather than acting above it — is enacted in Jesus' ἐμβριμάομαι (deep agitation) and ταράσσω (being troubled). The God who was distressed in Israel's distress is now personally present in the grief of Bethany."
      }
    ],
    "34": [
      {
        "type": "theme",
        "target": "Ps 88:3-6",
        "note": "'I am counted among those who go down to the pit; I am like one without strength. I am set apart with the dead, like the slain who lie in the grave, whom you remember no more.' The tomb Jesus asks to be shown is the destination this Psalm describes from the inside — the place of abandonment and silence. Jesus' question locates him as the one moving toward exactly this place, not avoiding it."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Isa 53:3",
        "note": "'He was despised and rejected by mankind, a man of suffering, and familiar with pain.' The Servant's acquaintance with grief is here made visible: Jesus weeps at the tomb of his friend, entering human sorrow rather than standing above it. The brevity of the verse — 'Jesus wept' (ἐδάκρυσεν, the only time this word occurs in the NT) — carries the Servant's tears."
      },
      {
        "type": "allusion",
        "target": "Jer 9:1",
        "note": "'Oh, that my head were a spring of water and my eyes a fountain of tears! I would weep day and night for the slain of my people.' The weeping prophet wept over Israel's death and judgment; Jesus weeps at Lazarus' tomb as the one in whom God's grief over human mortality is fully present — the tears of the divine-human Mediator before the grave he is about to open."
      }
    ],
    "36": [
      {
        "type": "theme",
        "target": "Ps 109:4",
        "note": "'In return for my friendship they accuse me, but I am a man of prayer.' The Jews' observation 'see how he loved him' is genuine recognition of the love before them — but within John's irony it comes immediately before accusations and rejection. Love visible to onlookers is not yet faith that transforms them."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Ps 22:8",
        "note": "'He trusts in the LORD; let the LORD rescue him. Let him deliver him, since he delights in him.' The mockers at the cross will use almost these exact words (Matt 27:43). Here the same taunting logic appears at the tomb: 'Could not he who opened the eyes of the blind man have kept this man from dying?' The pattern of challenging the righteous sufferer's trust in God runs from Psalm 22 through both scenes."
      }
    ],
    "38": [
      {
        "type": "allusion",
        "target": "Lam 3:53-55",
        "note": "'They tried to end my life in a pit and threw stones at me; the waters closed over my head, and I thought I was about to perish. I called on your name, LORD, from the depths of the pit.' The sealed cave-tomb is the OT pit-imagery at its most literal — the place from which no human escape is possible. Jesus' coming to it is the divine answer to the lament that cries from the pit."
      }
    ],
    "39": [
      {
        "type": "allusion",
        "target": "Ezek 37:11",
        "note": "'Our bones are dried up and our hope is gone; we are cut off.' Martha's objection — four days, already an odor — names precisely the 'beyond all human hope' condition that Ezekiel's valley of dry bones symbolized for Israel. Jesus proceeds anyway, against the voice of physical impossibility."
      }
    ],
    "40": [
      {
        "type": "allusion",
        "target": "Isa 40:5",
        "note": "'The glory of the LORD will be revealed, and all people will see it together.' Jesus recalls his word to Martha — 'you will see the glory of God' — as the frame for what is about to happen. The Isaianic revelation-of-glory pattern is now enacted not as cosmic event but as the raising of one man from a specific tomb outside Jerusalem."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "1 Kgs 18:36-37",
        "note": "Elijah's prayer at Carmel: 'LORD, the God of Abraham, Isaac and Israel, let it be known today that you are God in Israel and that I am your servant... so these people will know that you, LORD, are God, and that you are turning their hearts back again.' Jesus' public prayer before the miracle — explicitly performed for the crowd's faith, not for his own need — is structurally identical to Elijah's public prayer before the fire fell."
      }
    ],
    "42": [
      {
        "type": "allusion",
        "target": "Exod 4:5",
        "note": "'This is so that they may believe that the LORD, the God of their fathers... has appeared to you.' Moses' signs were performed so that Israel would believe God had sent him; Jesus makes the same pedagogical purpose explicit: 'I said this for the benefit of the people standing here, that they may believe that you sent me.' The sign-for-faith structure is identical."
      }
    ],
    "43": [
      {
        "type": "fulfillment",
        "target": "Ezek 37:4",
        "note": "'Prophesy to these bones and say to them, Dry bones, hear the word of the LORD!' In Ezekiel's vision it was the prophetic word that summoned life back to the dead; here Jesus does not relay a word from God but speaks with his own authority: 'Lazarus, come out!' The Evangelist presents this as fulfillment not just parallel — the one who is the Word now calls the dead directly."
      },
      {
        "type": "allusion",
        "target": "Isa 26:19",
        "note": "'Let those who dwell in the dust wake up and shout for joy.' The voice that awakens the dead Isaiah anticipated is here enacted: Jesus' loud voice summons Lazarus from the dust. The resurrection Isaiah described as God's future act is performed in a single, specific command."
      }
    ],
    "44": [
      {
        "type": "allusion",
        "target": "Isa 61:1",
        "note": "'The Spirit of the Sovereign LORD is on me... to proclaim freedom for the captives and release from darkness for the prisoners.' Jesus' command 'take off the grave clothes and let him go' enacts the messianic Jubilee liberation: the one bound in the captivity of death is physically released — the grave-wrappings undone as a visible sign of the freedom the Anointed One came to bring."
      }
    ],
    "45": [
      {
        "type": "theme",
        "target": "Isa 52:10",
        "note": "'The LORD will lay bare his holy arm in the sight of all the nations, and all the ends of the earth will see the salvation of our God.' The sign witnessed by the Judean Jews — 'many... believed in him' — fulfills the pattern of faith produced by visible divine action. The salvation-act is performed publicly so that witness can become faith."
      }
    ],
    "46": [
      {
        "type": "allusion",
        "target": "Jer 26:10-11",
        "note": "After Jeremiah's temple sermon, religious officials brought him before the authorities: 'the priests and the prophets said, This man should be sentenced to death because he has prophesied against this city.' The pattern of reporting the prophet to the leadership as a prelude to judicial proceedings repeats exactly — a miraculous act in Jerusalem triggers a report to the authorities who will seek the performer's death."
      }
    ],
    "47": [
      {
        "type": "fulfillment",
        "target": "Ps 2:2",
        "note": "'The kings of the earth rise up and the rulers band together against the LORD and against his anointed.' The Sanhedrin convening to decide what to do about Jesus is the Psalm 2 conspiracy of rulers against God's Anointed — cited explicitly in Acts 4:25-28 as fulfillment of this psalm. The word 'plotted' in v53 confirms the register."
      }
    ],
    "48": [
      {
        "type": "allusion",
        "target": "Jer 7:4",
        "note": "'Do not trust in deceptive words and say, This is the temple of the LORD, the temple of the LORD, the temple of the LORD!' The leaders fear losing 'our temple and our nation' to Roman reprisal — their identity is bound to the building. Jeremiah warned against exactly this confusion of building with divine presence. They sacrifice the one who is the true Temple to protect the shadow."
      }
    ],
    "49": [
      {
        "type": "theme",
        "target": "Isa 56:10-11",
        "note": "'Israel's watchmen are blind, they all lack knowledge... they are shepherds who lack understanding.' Caiaphas' dismissal of his colleagues — 'you know nothing at all' — is ironic: he too knows nothing, speaking better than he knows. The blindness Isaiah named in Israel's watchmen is here distributed across the entire leadership."
      }
    ],
    "50": [
      {
        "type": "allusion",
        "target": "Isa 53:8",
        "note": "'By oppression and judgment he was taken away... for the transgression of my people he was punished.' Caiaphas' political calculation — 'it is better for you that one man die for the people than that the whole nation perish' — is an unconscious statement of the Isaianic substitution: one dying for the people's preservation. The narrator confirms in v51 that this is involuntary prophecy."
      }
    ],
    "51": [
      {
        "type": "fulfillment",
        "target": "Dan 9:26",
        "note": "'After the sixty-two sevens, the Anointed One will be put to death and will have nothing.' The cutting off of the Anointed One that Daniel's weeks-reckoning predicted is the event Caiaphas unknowingly prophesies. The narrator's explanation — 'as high priest that year he prophesied' — frames his statement as fulfillment of the Danielic schedule."
      },
      {
        "type": "fulfillment",
        "target": "Isa 53:8",
        "note": "'For the transgression of my people he was punished.' The Servant-death for the people that Isaiah described is the content of Caiaphas' prophecy — one dying for the nation — and the narrator confirms it is exactly this: Jesus 'would die for the Jewish nation' (v51b). The Sanhedrin's political calculus is God's redemptive purpose spoken from the mouth of the high priest."
      }
    ],
    "52": [
      {
        "type": "fulfillment",
        "target": "Isa 56:8",
        "note": "'The Sovereign LORD declares — he who gathers the exiles of Israel: I will gather still others to them besides those already gathered.' Jesus' death is not only for the nation but for 'the scattered children of God' — fulfilling Isaiah's explicit promise that the ingathering would extend beyond ethnic Israel to others not yet gathered."
      },
      {
        "type": "allusion",
        "target": "Jer 31:10",
        "note": "'He who scattered Israel will gather them and will watch over his flock like a shepherd.' The dispersed sheep gathered by the shepherd is the image Jeremiah pairs with the new covenant; the gathering of scattered children into one through Jesus' death is the new-covenant fulfillment of this shepherd-gathering promise."
      },
      {
        "type": "allusion",
        "target": "Ezek 34:13",
        "note": "'I will bring them out from the nations and gather them from the countries.' Ezekiel's promise of divine gathering from the nations — applied to the post-exilic restoration — is here given its ultimate referent: the death of Jesus that would bring the scattered children of God together from every nation."
      }
    ],
    "53": [
      {
        "type": "fulfillment",
        "target": "Ps 2:1-2",
        "note": "'Why do the nations conspire and the peoples plot in vain? The kings of the earth rise up and the rulers band together against the LORD and against his anointed.' The formal decision to put Jesus to death — 'from that day on they plotted to take his life' — is the Psalm 2 conspiracy actualized. Acts 4:25-28 explicitly applies Ps 2:1-2 to this gathering."
      },
      {
        "type": "allusion",
        "target": "Jer 11:19",
        "note": "'I had been like a gentle lamb led to the slaughter; I did not realize that they had plotted against me: Let us destroy the tree and its fruit; let us cut him off from the land of the living.' Jeremiah as innocent prophet facing a death-plot is a structural type of the pattern here: the one who has spoken and acted for God, condemned to death by the leadership. Jeremiah's lament anticipates the Servant's fate."
      }
    ],
    "54": [
      {
        "type": "allusion",
        "target": "1 Sam 23:14",
        "note": "David 'stayed in the wilderness strongholds and in the hills of the Desert of Ziph. Saul searched for him day after day, but God did not give David into his hands.' Jesus' withdrawal to Ephraim near the wilderness follows the Davidic pattern of the anointed one hiding from those who seek his life — protected until the appointed time, not by accident but by divine preservation."
      }
    ],
    "55": [
      {
        "type": "fulfillment",
        "target": "Exod 12:14-17",
        "note": "The Passover ordinance required all Israel to gather in Jerusalem for the feast — the very feast instituted by the slaying of the lamb whose blood averted judgment. The Passover drawing near while authorities plot Jesus' arrest is the fulfillment-engine: the festival that was always a type of the Lamb's death is about to become the event of which it was always a type."
      }
    ],
    "56": [
      {
        "type": "allusion",
        "target": "Ps 122:1-2",
        "note": "'I rejoiced with those who said to me, Let us go to the house of the LORD. Our feet are standing in your courts, Jerusalem.' The Passover pilgrims who have come to the temple courts and are asking 'Isn't he coming to the festival?' are seeking the divine presence in the building while the one who is the true Temple remains outside, sought by those with warrant for his arrest."
      }
    ],
    "57": [
      {
        "type": "allusion",
        "target": "Jer 38:4-6",
        "note": "Jerusalem's officials demanded that Jeremiah be silenced and arrested because his message undermined the city: 'This man should be handed over to us — he is discouraging the soldiers... He is not seeking the good of this people but their ruin.' The warrant the chief priests and Pharisees issue for Jesus' arrest follows the same structural pattern of the religious-political establishment moving against the prophet whose presence they cannot control."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 11 echoes written.')

if __name__ == '__main__':
    main()
