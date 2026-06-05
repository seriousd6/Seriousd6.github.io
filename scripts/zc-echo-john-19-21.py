"""
MKT Echo Layer — John chapters 19–21
Run: python3 scripts/zc-echo-john-19-21.py

Source data used:
- data/interlinear/john.json (Strongs tokens, chs 19–21)
- data/translation/draft/mediating/john.json (MKT text)
- data/translation/glossary-greek.json (G25 ἀγαπάω, G5368 φιλέω, G5055 τελέω, G1720 ἐμφυσάω, G4151 πνεῦμα)
- data/parallels/john.json (9 OT entries absorbed for ch 19, 1 for ch 20; synoptic parallels skipped)
- data/echoes/john.json (chs 1–13 present; chs 19–21 empty)

Key decisions:
- 19:9: Isa 53:7 classified as fulfillment (John's passion narrative is saturated with Servant
  parallels; the silent response before the governor matches Isa 53:7b precisely).
- 19:5 (Ecce Homo): Zech 6:12 LXX ("Behold the man, his name is the Branch") is the primary
  echo; the precise verbal overlap ἰδοὺ ὁ ἄνθρωπος across LXX and Pilate's cry is deliberate.
- 19:14: classified as fulfillment — John marks the sixth-hour Preparation Day explicitly because
  that was the hour the Passover lambs were being slaughtered at the temple (m. Pesaḥim 5:1).
- 19:29: Ps 69:21 on v28 (the explicit fulfillment claim); Exod 12:22 on v29 (the hyssop
  instrument of Passover applied to the final Passover victim — a distinct connection).
- 19:34 (blood and water): Zech 13:1 primary (cleansing fountain); Ezek 47 secondary.
- 20:12 (two angels at head and foot): Exod 25:18-20 primary — the geometry of the mercy seat
  (two cherubim, one at each end of the atonement cover) is reproduced too precisely to be
  accidental; the place of atonement is now empty and its guardians have become witnesses.
- 20:22 (he breathed): Gen 2:7 primary; Ezek 37:9 secondary — John signals both new creation
  and reconstituted-Israel simultaneously.
- 21:9 (fire of coals): 1 Kgs 19:5-7 primary — the only other charcoal fire (ἀνθρακιά) in the
  NT is John 18:18 where Peter denied Christ; the resurrection breakfast at a charcoal fire is a
  deliberate echo of the denial scene, staging Peter's restoration.
- 21:15-17 (ἀγαπάω / φιλέω): both verbs retained in echoes as meaningful — Ezek 34 is the
  controlling shepherd backdrop, not the more generalized Ps 23.
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
  "19": {
    "1": [
      {
        "type": "fulfillment",
        "target": "Isa 50:6",
        "note": "'I offered my back to those who beat me, my cheeks to those who pulled out my beard; I did not hide my face from mocking and spitting.' The Servant's submission to flogging — accepted rather than evaded — is what Pilate's scourging enacts; the passive posture of the Servant before his tormentors is precisely the posture the Evangelist presents."
      },
      {
        "type": "allusion",
        "target": "Isa 53:5",
        "note": "'He was pierced for our transgressions, he was crushed for our iniquities; the punishment that brought us peace was on him, and by his wounds we are healed.' The flogging is not incidental cruelty but the wound-bearing the Servant passage identifies as redemptive — John's narrative positions the scourging within this framework."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Gen 3:18",
        "note": "The curse on the ground included 'thorns and thistles' (Gen 3:18). The soldiers' crown of thorns places the curse of the Fall literally on the head of the one who came to bear it — the material of judgment becomes the ironic diadem of the one absorbing judgment on humanity's behalf."
      },
      {
        "type": "allusion",
        "target": "Ps 22:6-7",
        "note": "'I am a worm and not a man, scorned by everyone, despised by the people. All who see me mock me; they hurl insults.' The purple-robe mockery enacts the Psalmist's description of the righteous sufferer as an object of scorn — the contempt David described in the first person is now performed on the one who prays that psalm."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Lam 3:30",
        "note": "'Let him offer his cheek to one who would strike him, and let him be filled with disgrace.' The soldiers striking Jesus in the face follows the posture of the Suffering One in Lamentations — accepting the blow of contempt as part of enduring affliction without retaliation."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Isa 53:9",
        "note": "'He had done no violence, nor was any deceit in his mouth.' Pilate's threefold declaration of innocence — 'I find no fault in him' — echoes the Servant's moral profile; the governor's legal verdict becomes an unwitting testimony to the Servant's character."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Zech 6:12",
        "note": "Zechariah's oracle names a coming figure: 'Here is the man whose name is the Branch' (LXX: ἰδοὺ ἀνήρ, 'Behold the man'). Pilate's cry — 'Behold the man!' (ἰδοὺ ὁ ἄνθρωπος) — verbally echoes the LXX form of this messianic designation; the one Zechariah called 'the man, the Branch,' Pilate presents to the crowd."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Ps 69:4",
        "note": "'Those who hate me without reason outnumber the hairs of my head; many are my enemies without cause, those who seek to destroy me.' The chief priests shouting 'Crucify!' fulfills the Psalmist's portrait of groundless hatred — Pilate himself has just declared Jesus innocent, making the demand for crucifixion precisely the hatred-without-cause the psalm anticipates."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Lev 24:16",
        "note": "'Anyone who blasphemes the name of the LORD is to be put to death. The entire assembly must stone them.' The Jewish leaders invoke precisely this Torah provision — 'we have a law, and according to that law he must die, because he claimed to be the Son of God.' The irony is total: the blasphemy law is deployed against the one who is what he claims."
      }
    ],
    "8": [
      {
        "type": "theme",
        "target": "Ps 76:7",
        "note": "'It is you alone who are to be feared. Who can stand before you when you are angry?' Pilate's increasing fear upon hearing 'Son of God' echoes the Psalmic response to divine presence — the pagan governor experiences the numinous terror appropriate before the holy, without knowing what he fears."
      }
    ],
    "9": [
      {
        "type": "fulfillment",
        "target": "Isa 53:7",
        "note": "'He was oppressed and afflicted, yet he did not open his mouth; he was led like a lamb to the slaughter, and as a sheep before its shearers is silent, so he did not open his mouth.' Jesus' refusal to answer Pilate's question — giving him 'no answer' — is the Servant's silence enacted verbatim; John has already absorbed the parallels file's identification of this as prophecy-fulfillment."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Prov 21:1",
        "note": "'In the LORD's hand the king's heart is a stream of water that he channels toward all who please him.' Pilate's boast of authority to release or crucify is answered in v11 by Jesus' claim that the authority 'comes from above' — the proverb's theology of divine sovereignty over human power is the frame Jesus applies to his own situation."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Dan 4:17",
        "note": "'The Most High is sovereign over all kingdoms on earth and gives them to anyone he wishes.' Jesus' declaration that Pilate's power was 'given from above' is the Daniel 4 theology applied directly — earthly authority over life and death is derived, not ultimate, and the one who exercises it over Jesus does so within divine permission."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "1 Sam 8:7",
        "note": "When Israel demanded a king, God told Samuel: 'It is not you they have rejected, but they have rejected me as their king.' The leaders' threat — 'If you release this man, you are no friend of Caesar' — coerces Pilate by invoking Caesar's kingship against the one whose kingship they should have welcomed; Israel's ancient rejection of divine kingship reaches its final form."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Joel 3:12",
        "note": "'Let the nations be roused; let them advance into the Valley of Jehoshaphat, for there I will sit to judge all the nations on every side.' Pilate taking the judgment seat (βῆμα) to pronounce verdict on Jesus inverts the Joel image: it is God who sits to judge the nations, yet here the nations' representative judges God's anointed — the irony the Evangelist presses throughout the trial."
      }
    ],
    "14": [
      {
        "type": "fulfillment",
        "target": "Exod 12:6",
        "note": "The Passover instructions required slaughtering the lamb 'at twilight' on the fourteenth of Nisan — the Preparation Day (m. Pesaḥim 5:1 specifies the afternoon). John's precise notation — 'It was the day of Preparation of the Passover; it was about noon' — marks the moment when Pilate presents Jesus to the crowd as the hour when the Passover lambs were being prepared for slaughter at the temple."
      },
      {
        "type": "allusion",
        "target": "Zech 9:9",
        "note": "'See, your king comes to you, righteous and victorious, lowly.' Pilate's ironic 'Here is your king' echoes the Zechariah proclamation of the coming king — presented in humiliation, not triumph. The crowd will reject him; but the declaration stands."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "1 Sam 8:7",
        "note": "The chief priests' cry — 'We have no king but Caesar' — is the fullest expression of Israel's ancient rejection of divine kingship. When Israel first demanded a human king, God said they had rejected him as king; here the nation explicitly chooses a pagan emperor over the one the Father sent. The Samuel warning reaches its terminus."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Isa 53:6",
        "note": "'We all, like sheep, have gone astray, each of us has turned to our own way; and the LORD has laid on him the iniquity of us all.' The handing over of Jesus to be crucified is the act by which the Servant bearing is accomplished — 'laid on him' by the divine purpose is effected through Pilate's decision."
      }
    ],
    "17": [
      {
        "type": "type",
        "target": "Gen 22:6",
        "note": "Abraham placed the wood for the burnt offering on Isaac his son, who carried it to the place of sacrifice (Gen 22:6). Jesus bearing his own cross to Golgotha structurally recapitulates the Isaac scene: the beloved son carries the instrument of his own death to the appointed mountain, with no substitution provided this time."
      },
      {
        "type": "allusion",
        "target": "Lev 16:21-22",
        "note": "The Day of Atonement scapegoat bore Israel's sins and was 'sent away into the wilderness' — led outside the camp carrying the accumulated iniquity. Jesus going 'outside the city' to Golgotha bearing his cross echoes the scapegoat's removal from the community with its burden of sin."
      }
    ],
    "18": [
      {
        "type": "fulfillment",
        "target": "Isa 53:12",
        "note": "'He was numbered with the transgressors.' The crucifixion with two others — one on each side, Jesus in the middle — is the Isaianic detail fulfilled precisely: the Servant is not executed alone but placed among criminals, counted as one of them by the manner of his death."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Ps 2:6",
        "note": "'I have installed my king on Zion, my holy mountain.' The inscription Pilate places over the cross — 'JESUS OF NAZARETH, THE KING OF THE JEWS' — inadvertently fulfills the Psalm's declaration; the rulers of the earth gather against the LORD's anointed (vv1-3) while God's king is established, here in the most paradoxical form possible."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Isa 45:22-23",
        "note": "'Turn to me and be saved, all you ends of the earth... Before me every knee will bow; by me every tongue will swear.' The inscription written in Hebrew, Latin, and Greek — the three languages of religion, empire, and culture — makes the claim of kingship universal; all linguistic communities are addressed by the sign above the cross."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Ps 118:22-23",
        "note": "'The stone the builders rejected has become the cornerstone; the LORD has done this, and it is marvelous in our eyes.' The priests' objection to Pilate's inscription — protest against naming Jesus King — is the builder-rejection the psalm describes; Pilate's immovable 'What I have written, I have written' enacts the cornerstone's permanence."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Isa 46:10",
        "note": "'I make known the end from the beginning, from ancient times, what is still to come. I say: My purpose will stand, and I will do all that I please.' Pilate's 'What I have written, I have written' — his refusal to alter the inscription against all pressure — is deployed by John as an echo of divine irrevocability: the declaration that Jesus is King cannot be unmade."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Ps 22:17-18",
        "note": "'I can count all my bones; people stare and gloat over me. They divide my clothes among them and cast lots for my garment.' The soldiers dividing Jesus' outer garments into four shares sets up the exact scenario Ps 22:18 will fulfill in the next verse — John is careful to separate the dividing of garments from the lot-casting to preserve the psalm's own two-part structure."
      }
    ],
    "24": [
      {
        "type": "fulfillment",
        "target": "Ps 22:18",
        "note": "'They divide my clothes among them and cast lots for my garment.' John explicitly identifies this as fulfillment: 'This happened that the scripture might be fulfilled which said, They divided my clothes among them and cast lots for my garment.' The lot-cast for the seamless tunic fulfills the second clause of the psalm verse exactly."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Ps 38:11",
        "note": "'My friends and companions avoid me because of my wounds; my neighbors stay far away.' Against the pattern of abandonment the Psalm describes, the women near the cross represent its inversion: those who love him do not flee. The Evangelist notes their presence as a counter-testimony to the desertion the psalm anticipated."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Ps 22:9-10",
        "note": "'Yet you brought me out of the womb; you made me trust in you, even at my mother's breast. From birth I was cast on you; from my mother's womb you have been my God.' At the moment of death, Jesus commends his mother to new care — the Psalm that frames his passion (cited in v24) also places the mother's role at its opening; Jesus' provision for his mother echoes the psalm's opening lines about maternal bond."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Isa 54:1",
        "note": "'Sing, barren woman, you who never bore a child; burst into song, shout for joy, you who were never in labor; because more are the children of the desolate woman than of her who has a husband, says the LORD.' The Beloved Disciple taking Mary 'into his own home' transfers maternal care in the moment of greatest desolation — a small enactment of the Isaianic comfort that the bereaved woman gains new family."
      }
    ],
    "28": [
      {
        "type": "fulfillment",
        "target": "Ps 69:21",
        "note": "'They put gall in my food and gave me vinegar for my thirst.' John explicitly frames the cry 'I thirst' as fulfilling scripture — 'knowing that everything was now finished, so that scripture would be fulfilled, Jesus said, I am thirsty.' The Psalm verse is the text John signals; the act of v29 will complete it."
      },
      {
        "type": "allusion",
        "target": "Ps 22:15",
        "note": "'My mouth is dried up like a potsherd, and my tongue sticks to the roof of my mouth; you lay me in the dust of death.' The physical thirst of the dying man the Passion Psalm describes is voiced here verbatim — 'I thirst' is both a literal cry and the Psalm's bodily anguish spoken in the first person."
      }
    ],
    "29": [
      {
        "type": "fulfillment",
        "target": "Ps 69:21",
        "note": "The vinegar-soaked sponge lifted to Jesus' mouth completes the act that v28's 'I thirst' named as scripture-fulfillment. This verse is the mechanical completion of Ps 69:21 — 'they gave me vinegar for my thirst' — absorbed from the parallels file."
      },
      {
        "type": "allusion",
        "target": "Exod 12:22",
        "note": "'Take a bunch of hyssop, dip it into the blood in the basin and put some of the blood on the top and on both sides of the doorframe.' Hyssop was the instrument that applied the Passover blood. Here hyssop carries the sponge to the lips of the final Passover lamb — the same plant that mediated the original Passover protection now touches the one whose blood is the ultimate Passover."
      }
    ],
    "30": [
      {
        "type": "fulfillment",
        "target": "Ps 22:31",
        "note": "'They will proclaim his righteousness, declaring to a people yet unborn: He has done it!' The Hebrew of Psalm 22's final word — ʿāśāh, 'he has done it' — is the OT equivalent of John's τετέλεσται ('it is finished'). The Passion Psalm that opened with 'My God, my God, why have you forsaken me?' closes with a proclamation of completion; Jesus' last word is that psalm's last word spoken aloud."
      },
      {
        "type": "allusion",
        "target": "Isa 53:11",
        "note": "'After he has suffered, he will see the light of life and be satisfied; by his knowledge my righteous servant will justify many.' The Servant's suffering has a completion point — 'he will be satisfied' after the work is done. 'It is finished' (τετέλεσται) names the moment Isaiah described: the Servant's assignment has been discharged."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Deut 21:22-23",
        "note": "'You must not leave the body hanging on the pole overnight. Be sure to bury it that same day, because anyone who is hung on a pole is under God's curse.' The Jewish leaders' request to remove the bodies 'because it was Preparation Day' invokes this Deuteronomic law — and unwittingly invokes its curse clause over the one they condemned. Paul will cite exactly this text in Gal 3:13 to explain the cross's meaning."
      }
    ],
    "32": [
      {
        "type": "theme",
        "target": "Ps 34:20",
        "note": "'He protects all his bones, not one of them will be broken.' The breaking of the other two men's legs sets the contrast that v33 will make explicit — every other crucified person had their legs broken, but not Jesus. The protective word of Ps 34:20 is already operative, seen first from its negative side."
      }
    ],
    "33": [
      {
        "type": "fulfillment",
        "target": "Ps 34:20",
        "note": "'He protects all his bones, not one of them will be broken.' Jesus already dead means the soldiers do not break his legs — John identifies this in v36 as scripture-fulfillment. The event anticipated in v32 is sealed in v33; the Psalmist's protective word is enacted precisely."
      }
    ],
    "34": [
      {
        "type": "fulfillment",
        "target": "Zech 13:1",
        "note": "'On that day a fountain will be opened to the house of David and the inhabitants of Jerusalem, to cleanse them from sin and impurity.' The blood and water flowing from the pierced side is the opened fountain Zechariah described — not water alone, but blood and water together, the twin elements of atonement and purification."
      },
      {
        "type": "allusion",
        "target": "Ezek 47:1-5",
        "note": "Waters flowing from the side of the temple (Ezek 47:1) — ankle-deep, then knee-deep, then a river too deep to cross — symbolized the life-giving stream going out from God's dwelling. Jesus as the true Temple (John 2:21) releases this water from his side; the eschatological river begins at the cross."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Deut 19:15",
        "note": "'A matter must be established by the testimony of two or three witnesses.' The Evangelist's insistence — 'The man who saw it has given testimony, and his testimony is true. He knows that he tells the truth' — is structured as formal legal testimony in the Deuteronomic sense. The eyewitness account of blood and water is not embellishment but legally weighted attestation."
      }
    ],
    "36": [
      {
        "type": "fulfillment",
        "target": "Exod 12:46",
        "note": "'Do not break any of the bones.' The Passover lamb instruction — no bone to be broken — is explicitly cited by John as fulfilled in the unbroken bones of Jesus. The Passover ordinance that governed Israel's founding redemption now governs the death of the Lamb it always typified."
      },
      {
        "type": "fulfillment",
        "target": "Ps 34:20",
        "note": "'He protects all his bones, not one of them will be broken.' John cites this Psalm as a second scripture fulfilled in the unbroken bones — the Righteous Sufferer of Ps 34, preserved by divine protection even in death."
      }
    ],
    "37": [
      {
        "type": "fulfillment",
        "target": "Zech 12:10",
        "note": "'They will look on me, the one they have pierced, and they will mourn for him as one mourns for an only child.' John cites this as the second fulfillment in this verse: 'They will look on the one they have pierced.' Revelation 1:7 will extend this looking to every eye; John's Gospel notes the first fulfilment at the piercing itself."
      }
    ],
    "38": [
      {
        "type": "fulfillment",
        "target": "Isa 53:9",
        "note": "'He was assigned a grave with the wicked, and with the rich in his death, though he had done no violence, nor was any deceit in his mouth.' Joseph of Arimathea — a wealthy disciple — provides his own unused tomb for Jesus' burial. The Servant verse that predicted burial 'with the rich' is fulfilled precisely: the execution among criminals (v18) gives way to burial through the intervention of a rich man."
      }
    ],
    "39": [
      {
        "type": "allusion",
        "target": "2 Chr 16:14",
        "note": "King Asa was buried 'in the tomb that he had cut out for himself in the City of David. They laid him on a bier covered with spices and various blended perfumes.' Royal burial in Israel involved aromatic spices as a mark of honor; Nicodemus' bringing a hundred pounds of myrrh and aloes signals that Jesus receives a burial of royal dignity despite dying as a condemned criminal."
      }
    ],
    "40": [
      {
        "type": "allusion",
        "target": "Song 4:13-14",
        "note": "'Your plants are an orchard of pomegranates with choice fruits, with henna and nard, nard and saffron, calamus and cinnamon, with every kind of incense tree, myrrh and aloes.' The spices wound with Jesus' body are the garden-of-the-beloved's fragrant offerings — the burial garden of v41 will echo the enclosed garden of Song of Sol 4, where love and death meet."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "Gen 2:8-9",
        "note": "The first garden was the place God prepared for the man he had formed; the new tomb is in a garden, 'in which no one had ever been laid.' The Evangelist's garden setting for the burial deliberately evokes the first garden — the place of death is framed as a garden, pointing forward to the resurrection in the same garden (20:15) as the reversal of Eden's sentence."
      }
    ],
    "42": [
      {
        "type": "allusion",
        "target": "Isa 53:10",
        "note": "'Yet it was the LORD's will to crush him and cause him to suffer.' Even the burial logistics — hasty because of the Preparation Day — are encompassed by the divine will that appointed every detail of the Servant's death. The Evangelist has organized the passion to show that nothing happened outside the scripture-shaped plan."
      }
    ]
  },
  "20": {
    "1": [
      {
        "type": "allusion",
        "target": "Song 3:1-2",
        "note": "'All night long on my bed I looked for the one my heart loves; I looked for him but did not find him. I will get up now and go about the city, through its streets and squares; I will search for the one my heart loves.' Mary going to the tomb while it was still dark — seeking the beloved who is gone — follows this nocturnal-search pattern; the seeking that preceded finding the beloved is the Song's template for the resurrection-garden encounter."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Ps 142:4",
        "note": "'Look and see, there is no one at my right hand; no one is concerned for me. I have no refuge; no one cares for my life.' Mary's disorientation — 'They have taken the Lord out of the tomb, and we don't know where they have put him' — echoes the Psalmist's cry of abandonment; the body of her Lord is gone and she does not yet know where to look."
      }
    ],
    "3": [
      {
        "type": "theme",
        "target": "Ps 119:32",
        "note": "'I run in the path of your commands, for you have broadened my understanding.' Peter and the Beloved Disciple running to the tomb enacts the urgency of those who run toward divine disclosure — the movement toward the empty tomb is the disciples' first step toward understanding the scripture that Jesus had to rise."
      }
    ],
    "4": [
      {
        "type": "theme",
        "target": "Eccl 9:11",
        "note": "'The race is not to the swift or the battle to the strong.' The detail that the other disciple outran Peter is not incidental competition — the Evangelist records it because it is the Beloved Disciple (eyewitness, ultimately the author) who arrives first. The race of the witnesses is a race toward testimony."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Isa 53:12",
        "note": "The burial cloths lying undisturbed without the body recall the grave of the Servant who completed his assignment — the grave-wrappings remain, but the one they held is gone. The orderly linen signals departure, not robbery: a body taken in haste would not leave the cloths arranged."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "2 Kgs 2:13-14",
        "note": "When Elijah was taken into heaven, his cloak fell and Elisha picked it up — the garments left behind signaled the master's ascent to a higher realm. Peter entering the tomb and seeing the burial cloths lying there echoes this pattern: the wrappings of the body remain while the person has departed to a realm the grave cannot hold."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Ps 16:10",
        "note": "'You will not abandon me to the realm of the dead, nor will you let your faithful one see decay.' The cloth that had been around Jesus' head lay separately, folded — the careful arrangement speaks against decomposition and against robbery; the one God would not abandon to decay has departed from the tomb intact, the napkin witnessing to an unhurried exit."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Hab 2:4",
        "note": "'The righteous person will live by their faithfulness.' The Beloved Disciple 'saw and believed' — before any explanation, before the scripture was understood (v9), before the appearance to Mary. His is the faith that acts on sight of the empty space and the arranged cloths — the faithfulness that precedes full comprehension."
      }
    ],
    "9": [
      {
        "type": "fulfillment",
        "target": "Ps 16:10",
        "note": "'You will not abandon me to the realm of the dead, nor will you let your faithful one see decay.' John identifies this as the scripture they 'still did not understand' — the text that required the resurrection rather than merely anticipated it. Peter in Acts 2:27-31 will make explicit what John notes here: Ps 16 is the scripture the disciples had not yet read as resurrection-text."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Isa 55:8-9",
        "note": "'My thoughts are not your thoughts, neither are your ways my ways.' The disciples returning to 'where they were staying' — not yet understanding — follows the Isaianic pattern: divine action exceeds human comprehension; they have seen, and one has believed, but the full meaning will require the Spirit's teaching (14:26)."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Lam 1:16",
        "note": "'This is why I weep and my eyes overflow with tears. No one is near to comfort me, no one to restore my spirit.' Mary weeping outside the tomb — unable to leave, yet finding nothing inside but absence — enacts the posture of Lamentations: grief at desolation without yet seeing the comfort that is coming."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Exod 25:18-20",
        "note": "The mercy seat of the ark had two cherubim of gold, one at each end, facing each other with wings spread over the cover — the place of atonement bracketed by heavenly guardians. Two angels in white are seated where Jesus' body had been, 'one at the head and the other at the foot' — the geometry of the mercy seat is reproduced exactly at the empty tomb; the place of ultimate atonement is now empty, its guardians present as witnesses."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Ps 88:3-5",
        "note": "'I am overwhelmed with troubles and my life draws near to death. I am counted among those who go down to the pit; I am like one without strength. I am set apart with the dead, like the slain who lie in the grave, whom you remember no more.' Mary's 'they have taken away my Lord, and I don't know where they have put him' is the disorientation of the Psalmist who cannot locate God in the place of death — she is looking for him in the wrong category of existence."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Gen 3:8",
        "note": "In the first garden, the man and woman 'heard the sound of the LORD God as he was walking in the garden in the cool of the day.' Mary encounters the risen Jesus in a garden and does not recognize him — the new Adam is present in the garden, and the encounter is the inversion of Eden: instead of hiding from God, she seeks him; instead of hearing a verdict of death, she will hear her name called."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Gen 2:15",
        "note": "The LORD placed the man in the garden 'to work it and take care of it' — the first role in creation was gardener. Mary's mistake of Jesus for 'the gardener' is the Evangelist's irony: the risen one is precisely that — the last Adam who restores what the first Adam failed, caring now for the garden of creation as its true keeper."
      }
    ],
    "16": [
      {
        "type": "fulfillment",
        "target": "Isa 43:1",
        "note": "'Do not fear, for I have redeemed you; I have summoned you by name; you are mine.' Jesus speaks one word — 'Mary' — and she recognizes him. This is the Good Shepherd's voice calling his sheep by name (John 10:3), which is itself the enacted form of the Isaianic promise: redemption is personal, known by name, not by category."
      }
    ],
    "17": [
      {
        "type": "fulfillment",
        "target": "Ps 110:1",
        "note": "'The LORD says to my lord: Sit at my right hand until I make your enemies a footstool for your feet.' Jesus' instruction to tell the disciples 'I am ascending to my Father and your Father, to my God and your God' names the ascension that Ps 110:1 anticipates — the exaltation to the Father's right hand that the resurrection sets in motion."
      },
      {
        "type": "allusion",
        "target": "Ruth 1:16",
        "note": "'Your people will be my people and your God my God.' Jesus' formulation — 'my Father and your Father, my God and your God' — echoes the covenant-solidarity language of Ruth's pledge; the risen Christ binds the disciples into the same filial relationship he holds, making his Father theirs."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Isa 40:9",
        "note": "'You who bring good news to Zion, go up on a high mountain. You who bring good news to Jerusalem, lift up your voice with a shout, lift it up, do not be afraid; say to the towns of Judah, Here is your God!' Mary going to the disciples and announcing 'I have seen the Lord' is the first fulfillment of the Isaianic herald-figure — the good news of God's appearing proclaimed to waiting people."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Num 6:24-26",
        "note": "The Aaronic blessing — 'The LORD bless you and keep you; the LORD make his face shine on you and be gracious to you; the LORD turn his face toward you and give you peace' — closes with שָׁלוֹם (shalom). The risen Christ's greeting 'Peace be with you' is the priestly blessing given by the Great High Priest himself, standing now in the midst of his community."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Zech 13:6",
        "note": "'If someone asks, What are these wounds on your body? they will answer, The wounds I was given at the house of my friends.' Zechariah's question about the wounded one — whose wounds identify him as the pierced shepherd — is answered here: Jesus shows his hands and side as the marks that identify the risen Lord to his disciples."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Isa 61:1-2",
        "note": "'The Spirit of the Sovereign LORD is on me, because the LORD has anointed me to proclaim good news to the poor. He has sent me.' The commission Jesus now extends to the disciples — 'As the Father has sent me, I am sending you' — is the Isaianic mission handed on: the one anointed to proclaim good news, now sending others in the same pattern."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Gen 2:7",
        "note": "'Then the LORD God formed a man from the dust of the ground and breathed into his nostrils the breath of life, and the man became a living being.' Jesus breathing on the disciples and saying 'Receive the Holy Spirit' is a new-creation act that mirrors the first: the divine breath that animated Adam now constitutes the new community. John's ἐνεφύσησεν (he breathed) is the same verb the LXX uses in Gen 2:7."
      },
      {
        "type": "allusion",
        "target": "Ezek 37:9",
        "note": "'Come, breath, from the four winds and breathe into these slain, that they may live.' Ezekiel's vision of the Spirit-breath reconstituting the dry bones of Israel is enacted in compressed form: the risen Jesus breathes the Spirit into the discouraged disciples-as-dry-bones, reconstituting them as the living Israel of God."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Isa 22:22",
        "note": "'I will place on his shoulder the key to the house of David; what he opens no one can shut, and what he shuts no one can open.' The authority to forgive and retain sins given to the disciples here echoes the key-of-David binding-and-loosing authority — to which Jesus applies this same text in Matt 16:19 to Peter's representative function."
      }
    ],
    "24": [
      {
        "type": "theme",
        "target": "Ps 78:22",
        "note": "'For they did not believe in God or trust in his deliverance.' Thomas' absence from the appearance and his demand for physical proof recapitulate Israel's recurring pattern of requiring further evidence after signs already given — a pattern Psalm 78 traces through the wilderness generation. The pattern of unbelief after testimony will be addressed directly in Jesus' response in v29."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Zech 13:6",
        "note": "'What are these wounds on your body? The wounds I was given at the house of my friends.' Thomas' demand to see 'the nail marks in his hands' and 'put my hand into his side' before believing echoes the Zechariah question about the wounded shepherd — except here it is the disciple, not the questioner, who seeks the wounds as proof of identity."
      }
    ],
    "26": [
      {
        "type": "theme",
        "target": "Isa 7:14",
        "note": "'Therefore the Lord himself will give you a sign.' The second appearance — also through locked doors, again with the same greeting 'Peace be with you' — restates the pattern of divine sign given for belief. The sign for Thomas is not a diminished faith but the same physical evidence the other disciples had in v20."
      }
    ],
    "27": [
      {
        "type": "fulfillment",
        "target": "Zech 13:6",
        "note": "'What are these wounds on your body?' The answer to Zechariah's question is spoken here: the wounds are the marks of the stricken shepherd (Zech 13:7) who was pierced (Zech 12:10). Jesus presenting his hands and side to Thomas closes the question Zechariah posed — the wounded one is identified by the wounds that were given at the moment of judgment."
      }
    ],
    "28": [
      {
        "type": "fulfillment",
        "target": "Ps 35:23",
        "note": "'Awake, and rise to my defense! Contend for me, my God and my Lord.' The Psalm's address — 'my God and my Lord' (אֱלֹהַי וַאדֹנָי) — is the double title Thomas uses: κύριός μου καὶ ὁ θεός μου, 'My Lord and my God.' Thomas' confession applies to Jesus the exact address the Psalmist used for YHWH."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Ps 34:8",
        "note": "'Taste and see that the LORD is good; blessed is the one who takes refuge in him.' The beatitude Jesus pronounces — 'blessed are those who have not seen and yet have believed' — is the higher form of the Psalmist's 'taste and see': those who trust the testimony of the witnesses receive the same blessing as those who experienced directly, the blessing of the one who 'takes refuge in him' without demanding prior sensory confirmation."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Isa 8:16",
        "note": "'Bind up this testimony of warning and seal up God's instruction among my disciples.' The note that Jesus performed many other signs 'not written in this book' echoes Isaiah's act of sealing — the authorized witness is a selection from a larger body of available testimony, deliberately shaped for its purpose."
      }
    ],
    "31": [
      {
        "type": "fulfillment",
        "target": "Ps 2:7",
        "note": "'You are my Son; today I have begotten you' — the Davidic king's divine sonship. John's purpose statement — 'that you may believe that Jesus is the Messiah, the Son of God' — names the two titles the Psalm confers: Messiah (Anointed One, v2) and Son of God (v7). The Gospel is written to generate the faith these signs were designed to produce."
      }
    ]
  },
  "21": {
    "1": [
      {
        "type": "allusion",
        "target": "Isa 9:1-2",
        "note": "'Nevertheless, there will be no more gloom for those who were in distress. In the past he humbled the land of Zebulun and the land of Naphtali, but in the future he will honor Galilee of the nations, by the Way of the Sea, beyond the Jordan — The people walking in darkness have seen a great light.' The post-resurrection appearance in Galilee fulfills the Isaianic geography: the region Isaiah named as the site of great light is the location of the risen Lord's manifestation."
      }
    ],
    "2": [
      {
        "type": "theme",
        "target": "Num 1:2-3",
        "note": "The listing of those present — seven disciples named — echoes the OT pattern of named witnesses whose testimony carries legal weight. The number seven suggests completeness; the gathering is not a casual assembly but a constituted witness-community for what is about to occur."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Ezek 29:4-5",
        "note": "Ezekiel's judgment oracle against Pharaoh as a sea monster whose net-catch is empty inverts the flourishing abundance of ch 47; the fishermen catching nothing through the night echoes the fruitless labor of those who work apart from divine provision — a pattern John will shortly reverse."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Isa 25:9",
        "note": "'Surely this is our God; we trusted in him, and he saved us. This is the LORD, we trusted in him; let us rejoice and be glad in his salvation.' The pattern of the disciples not recognizing Jesus at first — and then recognizing him — follows the recognition-of-God pattern in Isaiah's eschatological salvation: the moment of recognition becomes the moment of rejoicing."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Judg 18:14",
        "note": "The question about fish — 'Friends, haven't you any fish?' (literally 'children, do you have any fish?') — is not a neutral inquiry; 'children' (παιδία) is a term of address that implies the questioner's authority over those addressed. The one addressing them as children and asking about the catch is establishing the authority that v6 will make explicit."
      }
    ],
    "6": [
      {
        "type": "fulfillment",
        "target": "Ezek 47:9-10",
        "note": "'Swarms of living creatures will live wherever the river flows... Fishermen will stand along the shore; from En Gedi to En Eglaim there will be places for spreading nets. The fish will be of many kinds — like the fish of the Great Sea.' Ezekiel's vision of the eschatological catch — immense abundance of fish wherever the life-giving river reaches — is enacted in the miraculous haul: the word of Jesus produces the eschatological abundance Ezekiel described."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "2 Sam 6:14-16",
        "note": "David 'danced before the LORD with all his might' when the ark was brought to Jerusalem — leaping into the procession without regard for decorum. Peter wrapping his outer garment around himself and jumping into the water to reach Jesus follows this pattern of urgent, undignified movement toward the divine presence — love that cannot wait for the boat."
      }
    ],
    "8": [
      {
        "type": "theme",
        "target": "Ps 107:23-30",
        "note": "'Some went out on the sea in ships, trading on the mighty waters... He stilled the storm to a whisper... They were glad when it grew calm, and he guided them to their desired haven.' The other disciples bringing the net-full of fish ashore in the boat follows the Psalmist's pattern of the sea-workers who encounter God's provision and are brought safely to harbor."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "1 Kgs 19:5-7",
        "note": "'All at once an angel touched him and said, Get up and eat. He looked around, and there by his head was some bread baked over hot coals, and a jar of water. Arise and eat, for the journey is too great for you.' The risen Jesus preparing a charcoal fire with fish and bread for his exhausted disciples echoes the angel's provision for the depleted Elijah. The only other ἀνθρακιά (charcoal fire) in the NT is John 18:18 — the fire of Peter's denial; the resurrection breakfast at a new charcoal fire stages his restoration."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Ps 23:5",
        "note": "'You prepare a table before me in the presence of my enemies.' The Lord who is the Good Shepherd prepares the meal — 'bring some of the fish you have just caught' — incorporating the disciples' catch into the provision he has already prepared. The shepherd's table is set, and the sheep are invited to contribute what they brought from their labors."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Ezek 47:10",
        "note": "'Fishermen will stand along the shore... The fish will be of many kinds — like the fish of the Great Sea, in large numbers.' The 153 large fish hauled ashore — with the net not breaking — is the Ezekiel eschatological catch made literal. Various patristic calculations identify 153 as the number of nations or species known to ancient naturalists, making the count a symbol of the universal scope of the mission Jesus is about to commission."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Ruth 2:14",
        "note": "Boaz called to Ruth: 'Come over here. Have some bread and dip it in the wine vinegar.' The invitation from a benefactor to a meal — especially one who holds authority over those invited — echoes the Ruth scene: a generous lord inviting a dependent to eat at his table. Jesus as the Lord of the harvest calls his laborers to breakfast."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "John 6:11",
        "note": "Jesus taking the bread and giving it to the disciples echoes the feeding of the five thousand (6:11), which itself echoed Exod 16 (the manna). The Evangelist's language is identical: 'Jesus took the bread and gave it to them, and did the same with the fish.' The resurrection breakfast recapitulates the wilderness-provision sign, identifying the risen Lord as the one who continues to give bread."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Hos 6:2",
        "note": "'After two days he will revive us; on the third day he will restore us, that we may live in his presence.' John notes this is the 'third time' Jesus appeared — the third-day / third-time pattern of restoration that Hosea frames as the eschatological structure of divine action: after apparent death comes divine restoration on the third occurrence."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Ezek 34:15-16",
        "note": "'I myself will tend my sheep and have them lie down, declares the Sovereign LORD. I will search for the lost and bring back the strays. I will bind up the injured and strengthen the weak.' The command 'Feed my lambs' (βόσκε τὰ ἀρνία μου) delegating the divine shepherd-work to Peter is the Ezekiel 34 commission handed to a human under-shepherd. The divine 'I myself' of Ezek 34 works through Peter."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Isa 40:11",
        "note": "'He tends his flock like a shepherd: He gathers the lambs in his arms and carries them close to his heart; he gently leads those that have young.' The second commission — 'Take care of my sheep' (ποίμαινε τὰ πρόβατά μου) — uses the word for pastoral tending (ποιμαίνω) that Isa 40:11 implies. The risen Lord who is the good shepherd (John 10) delegates the Isaianic shepherd-tenderness to Peter."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Jer 23:4",
        "note": "'I will place shepherds over them who will tend them, and they will no longer be afraid or terrified, nor will any be missing, declares the LORD.' The third commission restores Peter despite his threefold denial — three questions mirroring three denials. Jeremiah's promise of faithful shepherds appointed after the failure of faithless ones is enacted: the failed denier becomes the appointed shepherd."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Isa 65:2",
        "note": "'All day long I have held out my hands to an obstinate and rebellious people.' Peter once stretched out his hands in warmth beside the charcoal fire of denial; Jesus now prophesies that he will 'stretch out your hands' in death — a martyr's posture. The image of outstretched hands, which in Isaiah belongs to God's persistent appeal to the resistant, now becomes Peter's martyrdom posture, the final act of his restored fidelity."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Isa 50:4-5",
        "note": "'The Sovereign LORD has given me a well-instructed tongue, to know the word that sustains the weary. He wakens me morning by morning, wakens my ear to listen like one being instructed. The Sovereign LORD has opened my ears; I have not been rebellious; I have not turned away.' The Servant who follows without turning away is the model for the disciple Jesus calls: 'Follow me' — the second call to Peter is an echo of the first (1:43), and its content is Servant-discipleship."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "1 Kgs 19:19-20",
        "note": "When Elijah threw his cloak over Elisha, calling him as a successor, Elisha turned and saw Elijah. Peter 'turned and saw' the Beloved Disciple following — the arrangement of succession-disciple following prophet-disciple echoes the Elijah-Elisha commissioning. Peter is the newly commissioned disciple, and the Beloved Disciple is also in the train."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Job 1:9-10",
        "note": "'Does Job fear God for nothing? Have you not put a hedge around him and his household and everything he has?' Peter's question 'Lord, what about him?' echoes the human tendency to evaluate another's calling by comparison. The adversary asked about Job's circumstances relative to God's purpose; Peter asks about the Beloved Disciple's fate relative to his own calling. Jesus' response (v22) redirects attention from comparison to commission."
      }
    ],
    "22": [
      {
        "type": "allusion",
        "target": "Isa 46:10",
        "note": "'My purpose will stand, and I will do all that I please.' Jesus' 'If I want him to remain until I return, what is that to you?' asserts the divine prerogative over each disciple's calling — what God determines for one person is not normative for another. The divine will that governs history also governs individual apostolic destinies."
      }
    ],
    "23": [
      {
        "type": "theme",
        "target": "2 Kgs 2:3-5",
        "note": "The prophets at Bethel and Jericho told Elisha: 'Do you know that the LORD is going to take your master from you today?' The rumor about the Beloved Disciple not dying echoes the prophetic anticipation of Elijah's translation — both cases involve speculation about whether a specific figure will die in the normal way. John corrects the misunderstanding just as the text must correct misreadings of Elijah's translation."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Deut 19:15",
        "note": "'A matter must be established by the testimony of two or three witnesses.' The testimonial close — 'This is the disciple who testifies to these things and who wrote them down. We know that his testimony is true' — invokes the Deuteronomic standard for legally valid testimony. The Gospel closes by certifying its own witness according to the Torah's evidentiary requirement."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Amos 7:14-15",
        "note": "'I was neither a prophet nor the son of a prophet... the LORD took me from tending the flock and said, Go, prophesy to my people Israel.' The Gospel's closing reflection — 'I suppose that even the whole world would not have room for the books that would be written' — echoes the OT sense of the inexhaustible word: even the prophet who was 'merely a shepherd' was entrusted with more than could be contained. The Word made flesh (1:1) exceeds every book."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 19–21 echoes written.')

if __name__ == '__main__':
    main()
