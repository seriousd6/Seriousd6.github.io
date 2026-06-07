"""
Combined script: Revelation — all four layers (echo + original + context + christ)
Output: data/echoes/revelation.json + mkt-original + mkt-context + mkt-christ

Revelation is the most OT-saturated NT book (approximately 404 verses
contain echoes from 278 OT passages without ever giving a direct citation).
Key zones: the throne-room vision (chs 4-5, Ezekiel + Isaiah + Daniel),
the seals/trumpets/bowls (Exodus plagues + prophetic judgment oracles),
the Lamb who was slain (Isa 53 + Passover), and the new creation (Isa 65-66 + Ezek 40-48).
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

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

REV_ECHO = {
  "1": {
    "7": [
      {"type": "fulfillment", "target": "Dan 7:13", "note": "Behold he is coming with the clouds — the Danielic Son of Man coming with the clouds of heaven; Revelation's opening vision applies Dan 7:13 directly to the parousia of Jesus"},
      {"type": "fulfillment", "target": "Zech 12:10", "note": "Every eye will see him, even those who pierced him, and all tribes of the earth will wail — the mourning of Zech 12:10 (they will look on him whom they have pierced, and mourn for him) is applied to the universal vision of the returning Christ; the piercing of Christ on the cross is the historical fulfillment of the Zecharian piercing"}
    ],
    "12": [
      {"type": "allusion", "target": "Dan 10:5-6", "note": "Among the lampstands one like a son of man, clothed with a long robe and with a golden sash — Daniel's vision of the heavenly man clothed in linen, girded with gold, with face like lightning; John's vision of the glorified Christ reuses Daniel's heavenly-figure imagery"},
      {"type": "allusion", "target": "Exod 25:37", "note": "The seven golden lampstands — the seven-branched menorah of the tabernacle; the seven churches are the new menorah, the light-bearing presence of God in the world as the tabernacle was in Israel"}
    ]
  },
  "2": {
    "7": [
      {"type": "fulfillment", "target": "Gen 2:9; 3:22-24", "note": "To the one who conquers I will grant to eat of the tree of life, which is in the paradise of God — the tree of life in the garden of Eden from which Adam and Eve were excluded after the Fall (Gen 3:22-24: lest he reach out his hand and take also of the tree of life); the promise to Ephesus reverses the expulsion-sentence, restoring access to what sin forfeited."},
      {"type": "allusion", "target": "Ezek 28:13", "note": "Paradise of God — the Edenic imagery of Ezek 28:13 (you were in Eden, the garden of God) where the garden is described as the dwelling of divine glory; the Revelation promise recasts Eden as the eschatological dwelling of the victorious community."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 49:2", "note": "The one who has the sharp two-edged sword — the Servant of the LORD whose mouth was made like a sharp sword (Isa 49:2: he made my mouth like a sharp sword, in the shadow of his hand he hid me); the sword-mouth of Christ as judge echoes the Servant whose word is the instrument of divine justice."}
    ],
    "14": [
      {"type": "allusion", "target": "Num 25:1-2; 31:16", "note": "The teaching of Balaam, who taught Balak to put a stumbling block before Israel, so that they might eat food sacrificed to idols and practice sexual immorality — Num 31:16 identifies Balaam's counsel to Balak: through him Israel committed unfaithfulness against the LORD at Peor (Num 25:1-3) by eating sacrifices to Moabite gods and committing sexual immorality; the Pergamum letter identifies the same syncretistic pattern in the church."}
    ],
    "17": [
      {"type": "allusion", "target": "Isa 62:2", "note": "I will give him a white stone with a new name written on it — Isa 62:2 promises a new name given by the LORD's own mouth to redeemed Jerusalem; the new name on the stone parallels the Isaianic promise of a renewed identity that replaces the old shame-name with a name reflecting covenant restoration."}
    ],
    "20": [
      {"type": "allusion", "target": "1 Kgs 16:31; 21:25; 2 Kgs 9:22", "note": "That woman Jezebel, who calls herself a prophetess and is teaching and seducing my servants to practice sexual immorality and to eat food sacrificed to idols — 1 Kgs 16:31 identifies Jezebel as the Phoenician queen who led Ahab into Baal worship; 2 Kgs 9:22 summarizes her influence as 'whoredoms and sorceries'; the Thyatira letter uses 'Jezebel' as the type-name for any figure who draws God's people into syncretistic sexual immorality."}
    ],
    "23": [
      {"type": "allusion", "target": "Jer 17:10", "note": "I am he who searches mind and heart, and I will give to each of you according to your works — Jer 17:10 (I the LORD search the heart and test the mind, to give every man according to his ways, according to the fruit of his deeds); the divine claim to search minds-and-hearts (Jer 11:20; Ps 7:9) is now made by the glorified Christ as judge of the churches."}
    ],
    "27": [
      {"type": "fulfillment", "target": "Ps 2:8-9", "note": "He will rule the nations with a rod of iron, as when earthen pots are broken in pieces, even as I myself have received authority from my Father — Ps 2:8-9 is the messianic oracle (ask of me, and I will make the nations your heritage; you shall break them with a rod of iron); the Thyatira promise shares the Davidic ruler's authority with the conqueror, extending the Ps 2 inheritance to the faithful community."}
    ]
  },
  "3": {
    "4": [
      {"type": "allusion", "target": "Zech 3:4-5", "note": "They will walk with me in white, for they are worthy — Zechariah's vision of Joshua the high priest being reclothed: 'Take off the filthy garments' and 'I will clothe you with pure vestments' (Zech 3:4); the worthy remnant in Sardis receive the clean garments that Zechariah's vision promised to the restored priesthood."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Exod 32:32-33; Dan 12:1", "note": "I will never blot his name out of the book of life — Moses's intercession in Exod 32:32 ('blot me out of your book') reveals that the heavenly record could erase names; Dan 12:1 promises that 'everyone found written in the book shall be delivered'; Revelation's promise to the conqueror in Sardis secures the Danielic deliverance as the permanent non-erasure of the faithful from God's book."}
    ],
    "7": [
      {"type": "fulfillment", "target": "Isa 22:22", "note": "Who has the key of David, who opens and no one will shut, who shuts and no one opens — Isa 22:22 is the investiture of Eliakim as royal steward ('I will place on his shoulder the key of the house of David; he shall open, and none shall shut; he shall shut, and none shall open'); the Philadelphia letter applies the steward's key-authority directly to Christ as the true and final steward of God's household."}
    ],
    "9": [
      {"type": "fulfillment", "target": "Isa 49:23; 60:14", "note": "I will make them come and bow down before your feet, and they will learn that I have loved you — Isa 49:23 (kings shall bow down to you with their faces to the ground) and Isa 60:14 (those who afflicted you shall come bowing low) describe the nations and enemies prostrating before restored Israel; the Philadelphia promise transfers this Isaianic vindication to the Gentile church community that will see its opponents humbled."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 56:5", "note": "I will make him a pillar in the temple of my God — Isa 56:5 promises to eunuchs and foreigners within the covenant 'a monument and a name better than sons and daughters; I will give them an everlasting name that shall not be cut off'; the pillar is the permanent, immovable place within God's house that matches Isaiah's promise of an indelible name for the marginalized faithful."},
      {"type": "fulfillment", "target": "Isa 62:2; Ezek 48:35", "note": "I will write on him the name of my God, and the name of the city of my God, the new Jerusalem — Isa 62:2 (you shall be called by a new name that the mouth of the LORD will give) and Ezek 48:35 (the name of the city from that time on shall be: The LORD Is There) converge: the victorious community is inscribed with the divine name and the city-name, realizing both Isaianic and Ezekielian promises of renewed identity."}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 65:16", "note": "The Amen, the faithful and true witness, the beginning of God's creation — Isa 65:16 (the God of the Amen; the former troubles are forgotten) uses the Hebrew Amen as a divine title for the faithful God; Revelation applies this Isaianic 'God of the Amen' title to Christ as the faithful witness whose testimony is the ground of the new creation."}
    ],
    "19": [
      {"type": "allusion", "target": "Prov 3:11-12", "note": "Those whom I love, I reprove and discipline — Prov 3:11-12 (do not despise the LORD's discipline or be weary of his reproof, for the LORD reproves him whom he loves, as a father the son in whom he delights); the Laodicea rebuke applies Wisdom's father-discipline maxim to the risen Christ's corrective relationship with his lukewarm church."}
    ],
    "20": [
      {"type": "allusion", "target": "Song 5:2", "note": "Behold, I stand at the door and knock. If anyone hears my voice and opens the door, I will come in to him and eat with him — Song 5:2's beloved stands outside knocking ('I hear my beloved knocking: Open to me, my sister, my love, my dove, my perfect one'); the Laodicea invitation recasts the Song's lover-at-the-door as Christ seeking entry into the church that has excluded him through its self-sufficiency."}
    ]
  },
  "4": {
    "2": [
      {"type": "allusion", "target": "Ezek 1:26-28", "note": "A throne stood in heaven with one seated on it, with the appearance of jasper and carnelian, and around the throne a rainbow — Ezekiel's throne-chariot vision (merkabah): the one on the throne with the appearance of gleaming amber, the rainbow surrounding; John's throne-room draws directly from Ezekiel's initial vision"},
      {"type": "allusion", "target": "Isa 6:1-3", "note": "The four living creatures crying Holy, holy, holy — the seraphim of Isaiah's throne vision crying the Trisagion; the four living creatures of Revelation 4 combine Ezekiel's four living creatures (Ezek 1:5-14) with Isaiah's seraphim (Isa 6:2-3)"}
    ]
  },
  "5": {
    "5": [
      {"type": "fulfillment", "target": "Gen 49:9-10", "note": "Behold, the Lion of the tribe of Judah, the Root of David — the Judah-lion prophecy of Gen 49:9-10 (the scepter shall not depart from Judah) identifies the Lion as the coming ruler from Judah's line; Revelation applies this to the resurrected Christ who has conquered"},
      {"type": "fulfillment", "target": "Isa 11:1", "note": "The Root of David has conquered — the shoot from the stump of Jesse (Isa 11:1) who will rule with justice; the Davidic root-branch motif of Isaiah fulfilled in Christ's resurrection-conquest"}
    ],
    "6": [
      {"type": "fulfillment", "target": "Isa 53:7", "note": "A Lamb standing, as though it had been slain — the lamb led to slaughter of Isa 53:7 (he was led like a lamb to the slaughter and like a sheep before its shearers is silent); the slain-but-standing Lamb is the risen Christ as the Servant who was killed and lives"},
      {"type": "allusion", "target": "Zech 3:9", "note": "A Lamb with seven horns and seven eyes, the seven spirits of God — the stone with seven eyes before Joshua the high priest (Zech 3:9: I will engrave its inscription; seven are the eyes of the LORD which range through the whole earth); the seven eyes as divine omniscience applied to the Lamb"}
    ]
  },
  "6": {
    "12": [
      {"type": "allusion", "target": "Joel 2:10", "note": "The sun became black as sackcloth, the full moon became like blood, the stars fell to earth — the Day-of-the-LORD cosmic signs of Joel 2:10 and 2:31 (the sun will be turned to darkness and the moon to blood before the great and awesome day of the LORD); the sixth seal's cosmic disruption uses Joel's Day-of-LORD imagery"}
    ]
  },
  "7": {
    "17": [
      {"type": "fulfillment", "target": "Isa 25:8", "note": "God will wipe away every tear from their eyes — Isa 25:8 (YHWH will swallow up death forever and wipe away tears from all faces); the eschatological comfort of the feast-after-death promise now applied to the great multitude before the Lamb"}
    ]
  },
  "11": {
    "15": [
      {"type": "fulfillment", "target": "Dan 2:44", "note": "The kingdom of the world has become the kingdom of our Lord and of his Christ — Daniel's vision of the stone that becomes a great mountain filling the whole earth (Dan 2:35, 44: 'the God of heaven will set up a kingdom that shall never be destroyed'); the seventh trumpet announces this as completed"}
    ]
  },
  "12": {
    "5": [
      {"type": "fulfillment", "target": "Ps 2:9", "note": "She gave birth to a male child, one who is to rule all the nations with a rod of iron — Ps 2:9 (you shall break them with a rod of iron); the messianic ruler of Ps 2 is identified as the male child born of the woman; the rod-of-iron rule is the eschatological conquest of Christ"}
    ]
  },
  "19": {
    "11": [
      {"type": "allusion", "target": "Isa 11:4", "note": "The rider on the white horse is called Faithful and True, and in righteousness he judges and makes war — the messianic judge who strikes the earth with the rod of his mouth and slays the wicked with the breath of his lips (Isa 11:4); the rider's warfare is by the word of his mouth (v. 15)"}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 63:1-3", "note": "He is clothed in a robe dipped in blood — the warrior-in-crimson of Isa 63:1-6 whose garments are stained red from treading the winepress of nations' judgment; the Revelation rider's blood-stained robe echoes the Isaianic divine warrior"}
    ]
  },
  "21": {
    "1": [
      {"type": "fulfillment", "target": "Isa 65:17", "note": "I saw a new heaven and a new earth, for the first heaven and first earth had passed away — Isa 65:17's promise (I create new heavens and a new earth; the former shall not be remembered) is the explicit basis for Revelation's new creation; the eschatological promise receives its fullest apocalyptic depiction here"}
    ],
    "3": [
      {"type": "fulfillment", "target": "Lev 26:11-12", "note": "Behold the dwelling place of God is with man — the Sinai covenant promise 'I will set my dwelling among you ... I will walk among you and will be your God and you shall be my people' (Lev 26:11-12) reaches its consummation in the New Jerusalem; what the tabernacle mediated, the new creation embodies directly"},
      {"type": "fulfillment", "target": "Ezek 37:27", "note": "My dwelling place shall be with them and I will be their God and they shall be my people — Ezekiel's new covenant promise of YHWH dwelling with his people in the restored Israel reaches its cosmic fullness in the new creation"}
    ]
  },
  "22": {
    "1": [
      {"type": "fulfillment", "target": "Ezek 47:1-12", "note": "The river of the water of life flowing from the throne — Ezekiel's vision of the temple-river that flows deeper and deeper toward the sea, bringing life wherever it goes (Ezek 47:9: everything will live where the river goes); the New Jerusalem's river fulfills Ezekiel's temple-river"}
    ],
    "2": [
      {"type": "fulfillment", "target": "Gen 2:9", "note": "The tree of life with its twelve kinds of fruit, one for each month — the tree of life in the middle of the garden (Gen 2:9) that Adam and Eve were excluded from after the Fall; the new creation restores unrestricted access to the tree of life for those who wash their robes (v. 14), reversing the consequence of Gen 3:24"}
    ]
  }
}

REV_ORIGINAL = {
  "1": {
    "8": "<p><strong>ego eimi to Alpha kai to Omega legei Kyrios ho Theos ho on kai ho en kai ho erchomenos ho Pantokrator</strong>: 'I am the Alpha and the Omega, says the Lord God, who is and who was and who is to come, the Almighty.' <em>Alpha kai Omega</em>: the first and last letters of the Greek alphabet — a comprehensive inclusio encompassing all of reality. The phrase is applied both to God the Father (1:8; 21:6) and to Jesus (22:13: 'I am the Alpha and the Omega, the first and the last, the beginning and the end') — the shared title making the Christological identification with YHWH explicit. <em>Pantokrator</em> (Almighty): the LXX translation of Hebrew <em>El Shaddai</em> and <em>YHWH Tsvaot</em> (LORD of hosts) — here applied to both Father and Son as the supreme governing power over all creation.</p>",

    "17": "<p><strong>ego eimi ho protos kai ho eschatos kai ho zon kai egenomen nekros kai idou zon eimi eis tous aionas ton aionon</strong>: 'I am the first and the last, and the living one. I died, and behold I am alive forevermore.' The phrase <em>ho protos kai ho eschatos</em> (first and last) is YHWH's self-identification in Isa 41:4; 44:6; 48:12 — the exclusive divine claim to be both origin and terminus of all history. Jesus applies this YHWH-title to himself in combination with the resurrection claim: 'I died and behold I am alive.' The resurrection is the proof that the crucified one is the living YHWH — the divine identity claim vindicated by rising from death.</p>"
  },
  "4": {
    "8": "<p><strong>hagios hagios hagios Kyrios ho Theos ho Pantokrator ho en kai ho on kai ho erchomenos</strong>: 'Holy, holy, holy, is the Lord God Almighty, who was and is and is to come.' The Trisagion (Isa 6:3) is adapted with the temporal formula that characterizes Revelation's divine self-identification. The fourfold repetition of praise from the four living creatures links Revelation's throne-room to Isaiah's call-vision: the same divine holiness that destroyed Isaiah's self-confidence before the vision of YHWH is now the content of ceaseless heavenly worship. John hears the cosmic liturgy that underlies all earthly worship.</p>"
  },
  "5": {
    "5": "<p><strong>enikesen ho leon ho ek tes phyles Iouda e riza David anoixai to biblion</strong>: 'The Lion of the tribe of Judah, the Root of David, has conquered, so that he can open the scroll.' The title-cluster is Christological recapitulation: <em>Leon ek phyles Iouda</em> (Lion-of-Judah: Gen 49:9-10), <em>Riza David</em> (Root of David: Isa 11:1, 10; Rev 22:16), <em>enikesen</em> (has conquered). Then the stunning inversion: the 'Lion' who conquers is revealed as a 'Lamb standing as if slain' (v. 6). John hears Lion, then sees Lamb — the conquering is through the cross, not through military force. This Lion-Lamb inversion is Revelation's central hermeneutic: power is redefined by the slain Lamb who stands.</p>"
  },
  "13": {
    "18": "<p><strong>de estin sophia ho echon noun psephisato ton arithmon tou theriou arithmos gar anthropou estin kai ho arithmos autou hexakosioi hexekonta hex</strong>: '666' — the number of the beast. <em>Arithmos anthropou</em> (number of a human/humanity) — the beast's number is not cosmic but human, not transcendent but sub-divine. <em>Gematria</em> (assigning numerical values to letters) was a common Greco-Roman literary technique. The best-attested solution: NERON KAISER in Hebrew letters (nun=50 + resh=200 + vav=6 + nun=50 + qoph=100 + samek=60 + resh=200 = 666). Nero Caesar as the prototype of the beast — the first Roman persecutor of Christians — makes the political-historical reference legible to John's seven churches (ca. 90-95 CE, under Domitian, the 'second Nero').</p>"
  },
  "21": {
    "3": "<p><strong>idou he skene tou theou meta ton anthropon kai skemnosei met auton</strong>: 'Behold the dwelling place (<em>skene</em>) of God is with people, and he will dwell (<em>skenosei</em>) with them.' The <em>skene</em>-language deliberately echoes the wilderness tabernacle (<em>Mishkan</em>) and anticipates John 1:14 where the Word <em>eskenosen</em> (tabernacled) among us. The eschatological new creation is the realization of what the tabernacle mediated: direct divine presence without the veil, without the intermediary system, without separation — YHWH's face-to-face dwelling with his people. The Sinai covenant promise reaches its telos in the new Jerusalem.</p>"
  },
  "22": {
    "20": "<p><strong>nai erchomai tachy</strong> (<em>nai erchomai tachy</em>): 'Surely I am coming soon.' The final direct speech of Christ in the canon is a promise of return. <em>Tachy</em> (soon/quickly): the eschatological urgency that has characterized the entire Revelation. The community's response — <em>Amen, erchou Kyrie Iesou</em> (Come, Lord Jesus) — is the Greek form of the Aramaic <em>Maranatha</em> (1 Cor 16:22; Didache 10:6). The canon ends with a promise and a prayer: Christ's 'I am coming' and the community's 'Come.' The entire Christian life is lived in this tension of promise-and-prayer, the <em>already</em> of Christ's victory and the <em>not yet</em> of his return.</p>"
  }
}

REV_CONTEXT = {
  "1": {
    "9": "<p>The island of Patmos is a small volcanic island in the Aegean Sea, part of the Dodecanese chain, about 37 miles southwest of Ephesus. The Roman practice of <em>relegatio in insulam</em> (banishment to an island) was used for political offenders of some status — those meriting death were executed, those of social standing were exiled. John's Patmos exile 'on account of the word of God and the testimony of Jesus' (v. 9) places the Revelation within the Roman persecution of Christians, most plausibly under Domitian (81-96 CE, who demanded to be addressed as <em>Dominus et Deus</em>, Lord and God — a title the Revelation's 'Lord God Almighty' directly counters). The imperial cult was particularly strong in the seven cities of Revelation (Smyrna, Pergamum, Thyatira, Sardis, Philadelphia, Laodicea, and Ephesus all had imperial temples and cult practices).</p>"
  },
  "4": {
    "1": "<p>John's heavenly ascent follows the well-established pattern of Jewish apocalyptic merkabah mysticism (throne-chariot speculation based on Ezek 1 and Isa 6). The rabbinic tradition (b. Hagigah 11b-16a) treated merkabah speculation as dangerous esoterica — only the wisest scholars should study it. John's vision democratizes the throne-room: every Christian is shown what the mystical traditions reserved for elite initiates. The four living creatures (combining Ezek 1:5-14's four creatures with Isa 6:2-3's seraphim) and the twenty-four elders (representing either the twelve patriarchs + twelve apostles, or the twenty-four priestly courses of 1 Chr 24) frame the throne in the same pattern as the OT heavenly-temple tradition.</p>"
  },
  "12": {
    "1": "<p>The woman clothed with the sun (ch. 12) has generated three major interpretive traditions: (1) the church giving birth to Christ and then fleeing persecution (corporate-ecclesial reading); (2) Mary (Roman Catholic tradition, citing Gen 3:15 and the Immaculate Conception typology); (3) Israel/the covenant community through whom the Messiah came (salvation-historical reading). The best reading combines 2 and 3: the woman is the covenant community (OT Israel → NT church) through whom the Messiah came; Mary is the proximate historical instantiation. The cosmic imagery (sun, moon, twelve stars = Gen 37:9's dream of Joseph) links the woman to the patriarchal promise-community.</p>"
  },
  "17": {
    "9": "<p>The seven hills on which the woman sits (v. 9: <em>hepta ore</em>) is the most explicit historical identification in Revelation — Rome was universally known as the 'city of seven hills' (Septemontium). The woman 'Babylon the great' (vv. 5, 18: 'the great city that has dominion over the kings of the earth') is Rome — coded in the 'Babylon' cipher that 1 Peter also uses (1 Pet 5:13). Jewish and Christian apocalyptic literature routinely used 'Babylon' for Rome as the current oppressive empire (4 Ezra 3:1-2, 28-31; 2 Baruch 10-11). The coding protected the text from Roman censorship while being transparent to readers in the seven churches who knew the 'mystery' (v. 7).</p>"
  }
}

REV_CHRIST = {
  "1": {
    "17": "<p>A direct revelation: 'I am the first and the last, and the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades.' Three layered claims: (1) divine identity — the first-and-last YHWH-title; (2) resurrection reality — I died and I live; (3) eschatological authority — I hold the keys to death and Hades. These three together constitute the Christological thesis of Revelation: the crucified and risen Lord is the sovereign YHWH who controls death itself. The entire apocalyptic vision — judgments, seals, trumpets, bowls, the final victory — flows from this threefold claim made by Christ to John on Patmos.</p>"
  },
  "5": {
    "6": "<p>A direct revelation: 'A Lamb standing, as though it had been slain, with seven horns and seven eyes, which are the seven spirits of God sent out into all the earth.' The Lamb-vision is Revelation's Christological center. The Lamb is: (1) slain — bearing the marks of the cross permanently in his resurrection body; (2) standing — the resurrection state; (3) with seven horns — omnipotent (seven = completeness; horns = power); (4) with seven eyes — omniscient. This is the highest Christological symbol in the canon: the crucified-and-risen Jesus is simultaneously the sacrificial victim and the omnipotent, omniscient Lord of all history. The entire drama of Revelation unfolds as this Lamb opens the seals of history.</p>",

    "12": "<p>A direct revelation: 'Worthy is the Lamb who was slain, to receive power and wealth and wisdom and might and honor and glory and blessing!' The sevenfold doxology directed to the Lamb matches the sevenfold doxology directed to God in v. 13 — the deliberate parallelism attributes to Christ the same divine worthiness that belongs to YHWH alone. The ground of worthiness is the slaying (<em>ho esphagmenos</em>) — the cross is the qualification for cosmic lordship. The order in the throne-room is anti-imperial: not the emperor who receives tribute but the crucified-and-exalted Lamb who receives worship from every creature.</p>"
  },
  "19": {
    "16": "<p>A direct revelation: 'On his robe and on his thigh he has a name written: King of kings and Lord of lords.' The rider on the white horse — identified in vv. 11-16 with 'Faithful and True,' with eyes like flame, with many diadems, clothed in blood-stained robe, wielding a sharp sword from his mouth — bears the supreme title that Deut 10:17 gives to YHWH (God of gods and Lord of lords). Jesus as King-of-kings and Lord-of-lords is the final Christological counter-claim to every imperial title: Caesar's claim to divine lordship is answered by the appearance of the one whose sovereignty is not shared and whose kingdom will not be destroyed.</p>"
  },
  "21": {
    "5": "<p>A direct revelation: 'And he who was seated on the throne said: Behold, I am making all things new.' In the new creation vision, the one seated on the throne (identified with the Lamb in 22:1, 3 where both are said to be the throne of the new Jerusalem) speaks the new creation into being. The <em>kaina</em> (new, qualitatively new) of v. 5 echoes 2 Cor 5:17 (new creation) and Isa 65:17 — the eschatological renewal is not the old patched up but the new inaugurated by divine decree. The Christological new creation: as Christ's word created the old order (John 1:3; Col 1:16), so his word re-creates the new.</p>"
  },
  "22": {
    "13": "<p>A direct revelation: 'I am the Alpha and the Omega, the first and the last, the beginning and the end.' Revelation's closing divine address: Jesus claims for himself the three divine-identity formulae that the book opened with in relation to the Father (1:8: Alpha-Omega + Almighty). The three phrases together (Alpha/Omega, first/last, beginning/end) constitute the most comprehensive divine self-identification in the canon — and the book assigns them to Jesus. The Christological conclusion of Revelation: the Jesus who was crucified under Pontius Pilate, who was raised and ascended, who will return, is the one to whom all time and all reality belong. He is the beginning and the end of all creation.</p>"
  }
}

def main():
    e = load_echo('revelation')
    merge_echo(e, REV_ECHO)
    save_echo('revelation', e)
    print(f'Rev echo: {len(e)} chapters, {sum(len(v) for v in e.values())} verses')

    c = load_comm('mkt-original', 'revelation')
    merge_comm(c, REV_ORIGINAL)
    save_comm('mkt-original', 'revelation', c)
    print(f'Rev original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', 'revelation')
    merge_comm(c, REV_CONTEXT)
    save_comm('mkt-context', 'revelation', c)
    print(f'Rev context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', 'revelation')
    merge_comm(c, REV_CHRIST)
    save_comm('mkt-christ', 'revelation', c)
    print(f'Rev christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
