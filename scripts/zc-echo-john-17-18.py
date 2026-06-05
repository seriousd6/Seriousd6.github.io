"""
MKT Echo — John chapters 17–18
Run: python3 scripts/zc-echo-john-17-18.py

Source data used:
- data/interlinear/john.json (Strongs tokens, chs 17–18)
- data/translation/draft/mediating/john.json (MKT text, 66 verses total)
- data/parallels/john.json (ch 17: no entries; ch 18: three entries absorbed below)
- data/echoes/john.json (chs 1–13 already written; 17–18 empty)

Key decisions in this range:
- John 17: This is the High Priestly Prayer — the chapter is saturated with
  priestly-intercessory and Servant-song registers. Every verse is traceable to
  OT patterns; the selection favors the most exegetically load-bearing connections.
- John 17:2 (Dan 7:13-14): classified `type` — the Son of Man receiving authority
  over all flesh is the structural background for the Father granting the Son
  dominion and the power to give life. The parallels are too precise to be merely
  thematic.
- John 17:8 (Deut 18:18): classified `type` — the prophet-like-Moses who speaks
  exactly the words God gave him is the OT template Jesus embodies.
- John 17:9 (Exod 28-30 high priestly intercession): classified `type` — the
  narrowing of intercession to the covenant community (not the whole world) mirrors
  the Yom Kippur structure.
- John 17:19 (Lev 16 / Exod 29): classified `type` — the high priest consecrating
  himself before entering to make atonement for the community is the structural
  precedent for Christ sanctifying himself for the disciples.
- John 18:5-6 (ἐγώ εἰμι / soldiers falling): two echoes retained — Exod 3:14/Isa
  43:10-13 for the divine name register, Ps 27:2 for the falling-enemies motif;
  both classified `allusion` since the Evangelist does not cite these texts.
- John 18:14 (Caiaphas' prophecy): classified `fulfillment` — John 11:51 frames
  it explicitly as divine prophecy; the echo of Isa 53:8 is the OT anchor.
- John 18:39-40 (Barabbas): classified `type` for Lev 16 scapegoat — the structural
  parallel (one innocent/one guilty; one dies/one goes free at the appointed feast)
  is a designed correspondence, not merely analogous.
- John 18 parallels file absorption: the three parallels entries all reference other
  NT gospels (Matt, Mark, Luke), not OT texts; synoptic parallels are not echo-layer
  material and were therefore not absorbed.
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
  "17": {
    "1": [
      {
        "type": "allusion",
        "target": "Isa 52:13",
        "note": "The Servant 'will be raised and lifted up and highly exalted' — glorification through the path of suffering. Jesus' prayer that the Son be glorified through the hour of his death activates the same Servant trajectory: exaltation is not despite the passion but through it."
      },
      {
        "type": "type",
        "target": "Lev 16:2-4",
        "note": "The high priest entered the Holy of Holies once a year to intercede for Israel; he 'lifted up' the atonement offering before YHWH. Jesus, the true High Priest, now enters the heavenly sanctuary through prayer on the eve of his sacrificial death — the chapter as a whole functions as the Yom Kippur prayer of the greater Aaron."
      }
    ],
    "2": [
      {
        "type": "type",
        "target": "Dan 7:13-14",
        "note": "In Daniel's vision the one like a son of man approaches the Ancient of Days and is given 'dominion and glory and a kingdom, that all peoples, nations, and languages should serve him.' The Father's grant of authority 'over all flesh' so that the Son may give eternal life is the realized form of this investiture — authority received from the Father in order to bless all nations."
      },
      {
        "type": "allusion",
        "target": "Ps 2:8",
        "note": "'Ask of me, and I will give you the nations as your inheritance, the uttermost parts of the earth as your possession.' The Messianic Son receiving all peoples as his domain from the Father — Jesus does not ask; the Father has already given."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Jer 31:34",
        "note": "The new-covenant promise that 'they shall all know me, from the least of them to the greatest' — Jesus defines eternal life as knowing the Father and the Son. The Jeremianic new covenant passes through the knowledge of God; Jesus declares that this knowing has arrived in himself."
      },
      {
        "type": "allusion",
        "target": "Deut 6:4",
        "note": "'Hear, O Israel: the LORD our God, the LORD is one.' Jesus' phrase 'the only true God' (μόνον ἀληθινὸν θεόν) is a Greek rendering of the Shema's exclusive monotheism. The definition of eternal life is framed within Israel's primary confession."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Isa 53:10-11",
        "note": "'When his soul makes an offering for guilt... he shall see the fruit of the travail of his soul and be satisfied.' The completion of 'the work you gave me to do' frames the passion in terms of the Servant's fulfilled commission — not failure but accomplishment of the divine purpose."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Prov 8:22-31",
        "note": "Lady Wisdom declares: 'The LORD brought me forth as the first of his works... I was constantly at his side.' The Johannine Logos/Son who was with the Father 'before the world began' draws on this Wisdom tradition — pre-existence with the Father, shared in the act of creation, now petitioned to be restored."
      },
      {
        "type": "allusion",
        "target": "Isa 48:11",
        "note": "'For my own sake, for my own sake I do it... my glory I will not give to another.' YHWH's glory is inviolable and inalienable; Jesus prays to receive back the glory that is properly and eternally his — an implicit claim to share the divine identity."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Exod 3:13-15",
        "note": "God revealed his name to Moses so that Israel might know who sent him. Now Christ has 'revealed the Father's name' to the disciples — the revelation of the divine name given to the covenant community is the pattern. Christ is the new Moses who discloses the name of the one who sent him."
      },
      {
        "type": "allusion",
        "target": "Ps 22:22",
        "note": "'I will declare your name to my brothers; in the congregation I will praise you.' Cited in Heb 2:12 as Christ's act of declaring the Father's name to the community of his brothers — what the Psalmist anticipates, Christ performs among those the Father gave him."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Isa 42:1",
        "note": "'Behold my servant, whom I uphold, my chosen, in whom my soul delights; I have put my Spirit upon him.' Everything the Servant has — his appointment, his Spirit, his mission — comes from the one who sent him. The disciples' recognition that 'everything you have given me comes from you' locates Jesus in the Servant's posture of total dependence on the Father's commission."
      }
    ],
    "8": [
      {
        "type": "type",
        "target": "Deut 18:18",
        "note": "'I will raise up for them a prophet like you from among their brothers. And I will put my words in his mouth, and he shall speak to them all that I command him.' Jesus gave the disciples exactly the words the Father gave him — this is the defining function of the prophet-like-Moses, now fulfilled: the transmitted word received with certainty."
      }
    ],
    "9": [
      {
        "type": "type",
        "target": "Exod 28:29-30",
        "note": "The high priest bore the names of the twelve tribes on his breastplate when he entered the Holy Place — his intercession was specific to the covenant people, not the nations at large in that moment. Jesus' explicit limitation of his prayer to 'those you have given me' mirrors the priestly intercession for the particular community rather than a general petition."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Deut 10:14",
        "note": "'To the LORD your God belong heaven and the highest heavens, the earth and all that is in it.' The absolute sovereignty of YHWH over all things provides the backdrop for Jesus' declaration that all he has is the Father's and all the Father has is his — the mutual possession of Son and Father is the relational intensification of the divine sovereignty confession."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Prov 18:10",
        "note": "'The name of the LORD is a strong tower; the righteous man runs into it and is safe.' Jesus prays that the disciples be kept 'by the power of your name' — the divine name as a place of active protection is the Proverbs 18 register, now explicitly invoked for the community."
      },
      {
        "type": "allusion",
        "target": "Ps 20:1",
        "note": "'May the LORD answer you in the day of trouble! May the name of the God of Jacob protect you!' The Psalm is itself a prayer for protection through the divine name — Jesus prays the same protection for his disciples as the Psalm prays for the king going into danger."
      }
    ],
    "12": [
      {
        "type": "fulfillment",
        "target": "Ps 41:9",
        "note": "'Even my close friend in whom I trusted, who ate my bread, has lifted his heel against me.' Jesus cited this verse at 13:18 to identify Judas as its fulfillment. The reference here to the one who 'perished' so that Scripture would be fulfilled loops back to the same fulfillment event — the betrayer's loss is not an oversight but a divinely anticipated exception."
      },
      {
        "type": "allusion",
        "target": "Ps 109:8",
        "note": "'May another take his office.' Cited in Acts 1:20 for Judas specifically; the phrase 'son of perdition' (υἱὸς τῆς ἀπωλείας) and the loss of the one who was expected to be kept belong to the Psalm 109 framework of the doomed adversary whose end was written."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Ps 16:11",
        "note": "'You make known to me the path of life; in your presence there is fullness of joy.' The 'full measure of my joy' that Jesus wills for the disciples is the same joy of God's presence that Psalm 16 locates at the Father's right hand — the Psalm in its fullness is a Christological text (Acts 2:25-28), and the joy it promises is now prayed for the community."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Ps 69:4",
        "note": "'More in number than the hairs of my head are those who hate me without cause; mighty are those who would destroy me.' The disciples inherit the Psalmist's situation: the world's hatred falling on the righteous without cause. Jesus interprets the disciples' expected experience through the template of the suffering righteous one."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Zech 3:1-2",
        "note": "Joshua the high priest stands before the angel of the LORD while Satan stands at his right hand to accuse him; the LORD rebukes the adversary and protects his servant. Jesus' prayer to keep the disciples 'from the evil one' follows this intercessory pattern: the heavenly advocate protecting the community from the accuser."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "Dan 7:17-18",
        "note": "The four beasts 'are four kings who shall arise out of the earth; but the saints of the Most High shall receive the kingdom.' The disciples' not belonging to the world has its OT precedent in Daniel's distinction between the earthly kingdoms that arise from below and the people of the Most High whose citizenship is from above."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Ps 119:142",
        "note": "'Your righteousness is everlasting and your law is truth.' The identification of the divine word with truth is the Psalm 119 axiom; Jesus applies it directly: 'your word is truth.' Sanctification through immersion in the truth of God's word is the pattern the Psalmist describes and Christ now authorizes for the disciples."
      },
      {
        "type": "allusion",
        "target": "Ps 119:160",
        "note": "'The sum of your word is truth, and every one of your righteous rules endures forever.' A second Psalm 119 pillar for the same equation: the divine word and truth are not merely correlated but identical in their source. Sanctification through such truth is permanent, not provisional."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Isa 6:8",
        "note": "'Whom shall I send, and who will go for us? Here am I! Send me.' The commissioning-sending structure of prophetic calling — the one sent by God sends others into the world on the same errand. The disciples' mission parallels both the prophet's sending and Christ's own."
      }
    ],
    "19": [
      {
        "type": "type",
        "target": "Lev 16:6",
        "note": "'Aaron shall offer the bull as a sin offering for himself, and shall make atonement for himself and for his house.' The high priest consecrated himself before making atonement for the people — self-consecration preceding communal atonement is the Yom Kippur structure. Jesus sanctifies himself (consecrates himself as the sacrifice) so that the disciples may be truly sanctified: the same movement from priest's self-offering to the community's benefit."
      },
      {
        "type": "allusion",
        "target": "Isa 53:10",
        "note": "'It was the will of the LORD to crush him; he has put him to grief; when his soul makes an offering for guilt, he shall see his offspring.' The Servant's self-offering — willingly made — produces the sanctification of those who follow. 'For them I sanctify myself' is the Servant's logic applied by Jesus to his own coming death."
      }
    ],
    "20": [
      {
        "type": "shadow",
        "target": "Isa 56:6-8",
        "note": "'And the foreigners who join themselves to the LORD... these I will bring to my holy mountain... for my house shall be called a house of prayer for all peoples. The Lord GOD, who gathers the outcasts of Israel, declares, I will gather yet others to him.' Jesus prays for those who will believe through the disciples' message — the gathering of distant peoples through the going-out of testimony is the Isaianic trajectory Jesus explicitly claims."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Ezek 37:17",
        "note": "'Join them one to another into one stick, that they may become one in your hand.' God's promise to reunite the divided people Israel (the two sticks of Judah and Ephraim becoming one) provides the typological frame for the disciples' unity: what YHWH promised for his divided covenant people, Christ prays for his community — and the basis is the Father-Son unity itself."
      },
      {
        "type": "allusion",
        "target": "Deut 6:4",
        "note": "'The LORD our God, the LORD is one.' The Shema's declaration of divine unity is the model for the disciples' unity: their oneness is to reflect and participate in the oneness of Father and Son. 'That they may be one even as we are one' presupposes the Shema as the pattern."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Ps 8:5",
        "note": "'You have crowned him with glory and honor.' The conferral of divine glory on the human being made in God's image — Jesus gives the disciples the very glory the Father gave him, extending the Psalm's vision: not merely humanity crowned, but redeemed humanity sharing in the glory of the Son."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Isa 43:10",
        "note": "'You are my witnesses, declares the LORD, and my servant whom I have chosen, that you may know and believe me and understand that I am he.' The community's unity-in-witness is the means by which the world comes to know; the Isaianic servant-witness pattern — a community bearing testimony so that the world may know YHWH — is the template Jesus applies to the disciples."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Exod 33:18",
        "note": "Moses said to God: 'Please show me your glory.' Moses' longing to see the divine glory was only partially granted (Exod 33:20-23: the back, not the face). Jesus prays that the disciples will see his glory where he is — the request Moses could not fully receive is now promised to the disciples as their eschatological inheritance."
      }
    ],
    "25": [
      {
        "type": "theme",
        "target": "Isa 45:5",
        "note": "'I am the LORD, and there is no other, besides me there is no God; I equip you, though you do not know me.' YHWH declares that the world does not know him even while he works in it; the 'Righteous Father' whom the world does not know is the same God whom Deutero-Isaiah describes as unrecognized by the nations. Jesus' intimate knowledge stands against the world's ignorance — the pattern Isa 45 establishes."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Exod 34:6-7",
        "note": "On Sinai, Moses heard God pass by declaring his name and character: 'The LORD, the LORD, a God merciful and gracious, slow to anger, and abounding in steadfast love and faithfulness.' Christ's ongoing declaration of the Father's name continues and surpasses the Sinai disclosure — what was heard by one man on a mountain is now made known to a community and will continue to be declared."
      }
    ]
  },
  "18": {
    "1": [
      {
        "type": "type",
        "target": "2 Sam 15:23",
        "note": "David, betrayed by Ahithophel and fleeing Absalom, crossed the Kidron Valley in grief and submission to God's will (2 Sam 15:23, 30-31). The rejected-but-righteous king crossing the Kidron is the OT type Jesus enacts: both cross in the context of imminent betrayal, and both submit to the Father's will rather than defending their throne by force."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Ps 41:9",
        "note": "'Even my close friend in whom I trusted, who ate my bread, has lifted his heel against me.' The betrayer exploiting intimate knowledge of the private meeting place is the precise Psalm 41 pattern — a close companion's access weaponized against the one he knew. Jesus cited this verse at 13:18; its enactment begins here."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Ps 2:1-2",
        "note": "'Why do the nations rage and the peoples plot in vain? The kings of the earth set themselves, and the rulers take counsel together, against the LORD and against his Anointed.' The military array — Roman soldiers, temple officials, torches and weapons — descending on Jesus is the Psalm's scene made concrete. Acts 4:25-28 explicitly applies Ps 2:1-2 to this arrest."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "'He poured out his soul to death and was numbered with the transgressors; yet he bore the sin of many.' Jesus steps forward voluntarily — knowing all that was going to happen — to meet those who have come to arrest him. The voluntary surrender is the Servant's posture: not seized passively but offering himself, fully aware, to the appointment."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Isa 43:10-13",
        "note": "'Before me no god was formed, nor shall there be any after me. I, I am he (ἐγώ εἰμι in the LXX)... there is none who can deliver from my hand.' The Deutero-Isaiah divine-name formula — ἐγώ εἰμι as the self-declaration of YHWH — is the background for Jesus' 'I am he.' When he speaks the name, the soldiers draw back and fall."
      },
      {
        "type": "allusion",
        "target": "Ps 27:2",
        "note": "'When evildoers assail me to eat up my flesh, my adversaries and foes, it is they who stumble and fall.' The Psalm describes precisely what the Evangelist narrates: attackers approach the righteous one and it is they, not he, who fall to the ground. The detail is not explained; the Psalm provides the theological frame."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Exod 3:14",
        "note": "God said to Moses: 'I AM WHO I AM' — the divine name as pure self-existence. Jesus' utterance of ἐγώ εἰμι ('I am he') in response to the soldiers carries the force of the divine name, and the soldiers' falling backward is the created world's involuntary response to the presence of the one who bears it."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Isa 43:10",
        "note": "'You are my witnesses... that you may know and believe me and understand that I am he.' The repeated question 'Who is it you want?' and the repeated 'I am he' functions as a double witness — the Evangelist's characteristic pattern of repeated disclosure so that readers (and characters) cannot claim they did not know who stood before them."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Ezek 34:11-12",
        "note": "'I myself will search for my sheep and look after them. As a shepherd looks after his scattered flock when he is with them, so I will look after my sheep.' Jesus insists on protecting his disciples ('let these men go') even at the moment of his arrest — the shepherd's self-exposure to danger in order to secure the flock is the Ezekiel 34 pattern, enacted."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Ezek 34:16",
        "note": "'I will seek the lost, and I will bring back the strayed, and I will bind up the injured, and I will strengthen the weak.' The Shepherd who loses none of those entrusted to him — Jesus fulfills his own word (6:39: 'I shall lose nothing of all that he has given me') and the OT shepherd-promise: the disciples are protected and not a single one delivered into the soldiers' hands."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Isa 51:17",
        "note": "'Awake, awake, stand up, O Jerusalem, you who have drunk from the hand of the LORD the cup of his wrath.' Peter's sword is a refusal of the cup; the next verse makes clear that the cup is from the Father. The same cup of divine wrath that Isaiah describes Israel drinking is now Christ's to receive — willingly, from his Father's hand."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Ps 75:8",
        "note": "'For in the hand of the LORD there is a cup with foaming wine, well mixed, and he pours out from it, and all the wicked of the earth shall drain it down to the dregs.' The cup in the Father's hand — the cup of divine judgment — is given to Christ not as punishment but as mission. 'Shall I not drink the cup the Father has given me?' accepts what the Psalm describes as the destiny of the wicked, borne by the innocent one on their behalf."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Isa 53:7-8",
        "note": "'He was oppressed, and he was afflicted, yet he opened not his mouth... By oppression and judgment he was taken away.' The binding and leading away of the Servant — who does not resist — is enacted here: Jesus is bound and led first to Annas. The Isaianic Servant pattern governs the shape of the passion narrative."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Ps 2:2",
        "note": "'The kings of the earth set themselves, and the rulers take counsel together, against the LORD and against his Anointed.' The sequence of appearances before official rulers — Annas, Caiaphas, then Pilate — is the unfolding of the Psalm's scenario: the ruling powers of both religious and civil authority arrayed against God's Anointed."
      }
    ],
    "14": [
      {
        "type": "fulfillment",
        "target": "Isa 53:8",
        "note": "'For the transgression of my people, a stroke was due to him.' Caiaphas had advised (John 11:49-51) that it was expedient for one man to die for the people — the Evangelist explicitly framed this as unwitting prophecy (11:51: 'he did not say this of his own accord, but being high priest that year he prophesied'). The Isaianic Servant who dies 'for the transgression of my people' is the text Caiaphas' political calculation unconsciously fulfills."
      }
    ],
    "15": [
      {
        "type": "theme",
        "target": "Ps 88:8",
        "note": "'You have caused my companions to shun me; you have made me a horror to them. I am shut in so that I cannot escape.' The pattern of abandonment by companions in the hour of extremity — Peter's following at a distance, the other disciple needing a special arrangement to get in — enacts the Psalm's portrait of the one deserted in his night of distress."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "Ps 38:11",
        "note": "'My friends and companions stand aloof from my plague, and my nearest kin stand far off.' Peter standing outside at the door and requiring admission is a spatial expression of the disciples' theological distance from Jesus' hour of trial — what the Psalmist laments as abandonment, the Evangelist narrates as the beginning of Peter's denial sequence."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Zech 13:7",
        "note": "'Strike the shepherd, and the sheep will be scattered.' Jesus cited this verse in the Synoptic Gethsemane scene (Matt 26:31; Mark 14:27) as the prophetic frame for the disciples' flight and failure. The first denial is the beginning of the scattering Zechariah predicted — a servant girl's question exposes what the soldiers' swords could not: the sheep are not remaining with the struck shepherd."
      }
    ],
    "18": [
      {
        "type": "theme",
        "target": "Ps 31:11",
        "note": "'I am the scorn of all my adversaries, a horror to my neighbors, an object of dread to my acquaintances; those who see me in the street flee from me.' Peter's warming himself by the officials' fire — standing with those who arrested Jesus rather than beside him — is the practical expression of what the Psalm describes: the companion who cannot afford to be seen as associated with the afflicted one."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Isa 50:4-5",
        "note": "'The Lord GOD has given me the tongue of those who are taught, that I may know how to sustain with a word him who is weary... The Lord GOD has opened my ear, and I was not rebellious.' The Servant speaks what he was taught, openly and without evasion, before those who judge him. Jesus answers the high priest's interrogation with the same posture: he has spoken what the Father gave him to speak, publicly, and he does not retreat."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Isa 45:19",
        "note": "'I did not speak in secret, in a land of darkness; I did not say to the offspring of Jacob, Seek me in vain. I the LORD speak the truth; I declare what is right.' YHWH's self-declaration that he speaks openly and truthfully, not in secret, is echoed in Jesus' defense: 'I have spoken openly to the world... I said nothing in secret.' Christ speaks with the same quality of open, public, non-evasive disclosure."
      }
    ],
    "21": [
      {
        "type": "theme",
        "target": "Deut 19:15",
        "note": "'A single witness shall not suffice against a person for any crime or for any wrong in connection with any offense that he has committed. Only on the evidence of two witnesses or of three witnesses shall a charge be established.' Jesus invokes the procedural principle of the Torah: 'Ask those who heard me.' The judicial process being used against him violates its own foundations — witnesses, not a closed interrogation, establish the truth."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Isa 50:6",
        "note": "'I gave my back to those who strike, and my cheeks to those who pull out the beard; I hid not my face from disgrace and spitting.' The official strikes Jesus on the face during the interrogation — the Servant's receiving of blows from those in authority is the Isaianic pattern precisely enacted. Jesus does not hide or recoil but challenges the injustice directly."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Mic 5:1",
        "note": "'They shall strike the judge of Israel with a rod on the cheek.' The one who is truly the ruler of Israel — Micah's passage speaks of the Bethlehem ruler whose 'coming forth is from of old' — receives a blow on the cheek from an official. The irony the Evangelist builds: the struck one is the judge, and his question ('if I spoke the truth, why did you strike me?') is the true judge's judicial inquiry."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Isa 53:8",
        "note": "'By oppression and judgment he was taken away.' The sequence of transfers — bound and sent from Annas to Caiaphas — continues the Servant's being 'taken away' through a series of judicial proceedings. Each handover is a step in the divine design that the Servant's song describes as proceeding 'for the transgression of my people.'"
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Zech 13:7",
        "note": "'Strike the shepherd, and the sheep will be scattered.' Peter's second denial — 'I am not one of his disciples' — deepens the scattering. The struck shepherd is inside being tried; the sheep are outside denying they ever belonged to the flock. The Zechariah prophecy is completing its fulfillment denial by denial."
      }
    ],
    "26": [
      {
        "type": "theme",
        "target": "Ps 31:11-12",
        "note": "'I am the scorn of all my adversaries, a horror to my neighbors, an object of dread to my acquaintances... I have been forgotten like one who is dead; I have become like a broken vessel.' Peter is challenged by a relative of the man whose ear he cut off — the net closes, memory specific and hostile. The Psalm's portrait of the one surrounded by those with evidence against him sets the frame."
      }
    ],
    "27": [
      {
        "type": "fulfillment",
        "target": "Zech 13:7",
        "note": "'Strike the shepherd, and the sheep will be scattered.' The rooster's crowing at Peter's third denial marks the completion of the scattering Zechariah predicted. Jesus cited this verse in the Synoptic accounts explicitly (Matt 26:31; Mark 14:27) as the night's prophetic script. The cock-crow is not mere narrative realism; it is the marker that the Zechariah fulfillment is now complete."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Isa 1:13-16",
        "note": "'Your new moons and your appointed feasts my soul hates... When you spread out your hands, I will hide my eyes from you; even though you make many prayers, I will not listen; your hands are full of blood.' The leaders will not enter the praetorium to avoid ritual defilement so they can eat the Passover — while delivering an innocent man to death. Isaiah's indictment of religious observance combined with injustice is the OT framework for this bitter irony."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Ps 2:1-2",
        "note": "'Why do the nations rage... the rulers take counsel together, against the LORD and against his Anointed.' Pilate comes out to receive their accusation: the Roman governor now joins the scene. The two powers — Jewish leadership and Roman state — are the 'kings of the earth' and 'rulers' of Psalm 2 converging; Acts 4:26-27 applies this psalm explicitly to the events of this night."
      }
    ],
    "30": [
      {
        "type": "theme",
        "target": "Isa 53:3",
        "note": "'Despised and rejected by men, a man of sorrows and acquainted with grief; and as one from whom men hide their faces he was despised, and we esteemed him not.' The leaders' refusal to name a specific charge ('if he were not a criminal') while insisting on his guilt is the social dynamic of rejection without justification — the Servant is condemned by those who will not look at him clearly."
      }
    ],
    "31": [
      {
        "type": "theme",
        "target": "Deut 17:6-7",
        "note": "'On the evidence of two witnesses or of three witnesses the one who is to die shall be put to death.' Pilate's 'judge him by your own law' exposes the situation: the leaders want Roman execution, not Mosaic judgment, because the charge that would condemn Jesus requires a form of death (crucifixion) the Torah does not prescribe. The legal machinery of two systems is being maneuvered against the innocent."
      }
    ],
    "32": [
      {
        "type": "fulfillment",
        "target": "Num 21:8-9",
        "note": "'Make a fiery serpent and set it on a pole, and everyone who is bitten, when he sees it, shall live.' Jesus had cited this passage at 3:14 ('as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up'). The manner of death — crucifixion, being 'lifted up' — fulfills what Jesus himself identified as the Mosaic type. The note here is the Evangelist's confirmation that the type is being enacted."
      }
    ],
    "33": [
      {
        "type": "allusion",
        "target": "Ps 2:6",
        "note": "'As for me, I have set my King on Zion, my holy hill.' Pilate's question 'Are you the king of the Jews?' is the dramatic irony of the trial: the Roman governor is asking whether Jesus is the Anointed King of Psalm 2, whom YHWH has installed and whom the rulers of the earth rage against. Pilate will write the answer on the cross."
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "Isa 53:3",
        "note": "'He was despised and we esteemed him not.' Jesus' counter-question to Pilate — 'Is that your own idea, or did others tell you about me?' — draws out whether the accusation has any independent footing. The pattern of the Servant judged by others' characterization rather than direct encounter is the Isaianic frame: the condemnation builds from hearsay, not genuine knowledge of who stands before them."
      }
    ],
    "35": [
      {
        "type": "theme",
        "target": "Ps 22:12",
        "note": "'Many bulls encompass me; strong bulls of Bashan surround me.' Pilate's 'your own people and chief priests have handed you over to me' names the social reality the Psalm describes: the righteous one surrounded by those who should have been his own. The isolation of Jesus — rejected by his own nation's leaders and handed to the Gentiles — is the Psalm's pattern."
      }
    ],
    "36": [
      {
        "type": "allusion",
        "target": "Dan 7:13-14",
        "note": "The Son of Man receives 'dominion and glory and a kingdom' from the Ancient of Days — a kingdom not won by earthly armies but given from above. Jesus' 'my kingdom is not of this world' directly contrasts his kingdom with the beast-kingdoms that arise from below by force (Dan 7:2-8). If his kingdom were of this world, his servants would fight — but the kingdom of Dan 7 is given, not seized."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Isa 55:3",
        "note": "'Incline your ear, and come to me; hear, that your soul may live.' The call to hear the word of truth, the response to which determines life — Jesus tells Pilate that everyone 'on the side of truth' hears his voice. The Isaianic invitation (hear and live) and Jesus' test of Pilate (will he listen to the one who is truth?) occupy the same theological space."
      }
    ],
    "38": [
      {
        "type": "allusion",
        "target": "Isa 53:9",
        "note": "'He had done no violence, and there was no deceit in his mouth.' Pilate's 'I find no basis for a charge against him' is the Roman official's unwitting confirmation of the Servant's innocence. Three times Pilate will declare Jesus innocent (18:38; 19:4, 6); each declaration echoes the Isaianic witness that the Servant condemned by others had done no wrong."
      }
    ],
    "39": [
      {
        "type": "type",
        "target": "Lev 16:15-22",
        "note": "On the Day of Atonement two goats were presented: one was slaughtered as a sin offering; the other — the scapegoat — was released into the wilderness, bearing the sins of the people. The Passover custom of releasing one prisoner enacts the same structural logic: one dies (the innocent Jesus), one goes free (the guilty Barabbas). The festival of release at Passover is the Atonement-day structure applied to the moment of the true Passover Lamb."
      }
    ],
    "40": [
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "'He was numbered with the transgressors.' Barabbas was a robber and insurrectionist (λῃστής); his release in exchange for the innocent Jesus places Jesus quite literally in the position the Isaiah 53 Servant occupies — the innocent one handed over while the guilty go free, the transgressor's sentence absorbed by the one who never transgressed."
      },
      {
        "type": "allusion",
        "target": "Isa 53:6",
        "note": "'All we like sheep have gone astray; we have turned—every one—to his own way; and the LORD has laid on him the iniquity of us all.' The crowd's choice of Barabbas — the guilty released, the innocent retained — enacts what Isaiah describes: the guilt of the people transferred to the Servant. The crowd chooses the wrong man to die; the divine logic ensures the right substitution takes effect."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 17–18 echoes written.')

if __name__ == '__main__':
    main()
