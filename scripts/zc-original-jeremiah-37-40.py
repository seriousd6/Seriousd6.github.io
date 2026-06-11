"""
Combined OT Phase 2 script: Deuteronomy, Jeremiah, Ezekiel, Daniel — all four layers.
These four books have the highest NT echo density of all remaining OT books.
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

# ============================================================
# DEUTERONOMY
# ============================================================

DEUT_ECHO = {
  "6": {
    "4": [
      {"type": "allusion", "target": "Mark 12:29", "note": "Hear O Israel the LORD our God the LORD is one — Jesus cites the Shema (Deut 6:4-5) as the first and greatest commandment; the Shema frames the entire law in the context of YHWH's singular Lordship over Israel"},
      {"type": "allusion", "target": "1 Cor 8:6", "note": "One God the Father from whom are all things and one Lord Jesus Christ through whom are all things — Paul's expansion of the Shema incorporates Jesus into the divine identity: the 'one Lord' of the Shema is now differentiated into Father and Son"}
    ]
  },
  "18": {
    "15": [
      {"type": "fulfillment", "target": "Acts 3:22", "note": "A prophet like me will the LORD your God raise up for you — Peter cites Deut 18:15 as fulfilled in Jesus; the eschatological prophet-like-Moses was the figure Israel expected, and Peter declares Jesus to be that prophet"},
      {"type": "fulfillment", "target": "Acts 7:37", "note": "God will raise up for you a prophet like me from your brothers — Stephen's speech identifies the prophet-like-Moses promise as the Christological center of Moses's ministry; Israel's rejection of Moses typifies their rejection of Jesus"}
    ]
  },
  "21": {
    "23": [
      {"type": "fulfillment", "target": "Gal 3:13", "note": "Cursed is everyone who hangs on a tree — Paul cites Deut 21:23 as fulfilled in the crucifixion: Christ redeemed us from the curse of the law by becoming a curse for us, for cursed is everyone who hangs on a tree; the cross is the site of curse-absorption"}
    ]
  },
  "30": {
    "12": [
      {"type": "allusion", "target": "Rom 10:6-8", "note": "Do not say in your heart who will go up to heaven — Paul adapts Deut 30:12-14 Christologically: the word that is near you, in your heart and mouth, is the word of faith we proclaim; what Deuteronomy said of the Torah-command is now said of Christ and his gospel"}
    ]
  },
  "32": {
    "21": [
      {"type": "fulfillment", "target": "Rom 10:19", "note": "I will make you jealous of those who are not a nation — Paul cites the Song of Moses (Deut 32:21) as the OT basis for the Gentile mission provoking Israel to jealousy; the unexpected reversal of Gentile blessing is Moses's own warning"}
    ],
    "43": [
      {"type": "fulfillment", "target": "Rom 15:10", "note": "Rejoice O Gentiles with his people — Paul cites Deut 32:43 LXX as one of four OT texts (Rom 15:9-12) proving that Gentile inclusion in the worship of God was always the divine plan from Moses through the Psalms and Isaiah"}
    ]
  }
}

DEUT_ORIGINAL = {
  "6": {
    "4": "<p><strong>shema yisrael YHWH eloheinu YHWH echad</strong> (<em>šĕmaʿ yiśrāʾēl Yhwh ʾĕlōhênû Yhwh ʾeḥād</em>): 'Hear O Israel: YHWH our God, YHWH is one.' The Shema is the foundational confession of Jewish faith, recited morning and evening by observant Jews. <em>Echad</em> (one) is the standard Hebrew numeral one — it allows for internal distinction (as in <em>yom echad</em>, one day, composed of evening and morning; Gen 2:24, <em>basar echad</em>, one flesh, composed of two persons) but asserts the unity of the divine being against all polytheism. Paul's expansion in 1 Cor 8:6 ('one God the Father ... and one Lord Jesus Christ') is not an abandonment of monotheism but a Christological reconfiguration: the Shema's single divine identity now encompasses both Father and Son.</p>"
  },
  "18": {
    "15": "<p><strong>navi mikirbecha meacheicha kamoni yaqim lecha YHWH eloheicha elav tishmaun</strong> (<em>nābîʾ miqqirbĕkā mēʾahêkā kāmōnî yāqîm lĕkā Yhwh ʾĕlōhêkā ʾēlāw tišmāʿûn</em>): 'A prophet like me will YHWH your God raise up for you from among your brothers; to him you shall listen.' The singular prophet (<em>navi</em>) can be read as: (1) a category or series of prophets who will continue Moses's role; (2) an individual eschatological figure. The Qumran community awaited a specific prophetic figure alongside the Messiah and the Aaronic priest (1QS 9:11). Peter and Stephen in Acts 3 and 7 take reading (2): the specific individual is Jesus, whose coming makes the definitive Torah-interpretation that Moses could only anticipate.</p>"
  },
  "30": {
    "15": "<p><strong>reeh natati lefanecha hayom et-hahayyim veet-hatov veet-hamot veet-hara</strong> (<em>rĕʾēh nātattî lĕpānêkā hayyôm ʾet-hahayyîm wĕʾet-haṭṭôb wĕʾet-hammāwet wĕʾet-hārāʿ</em>): 'See I have set before you today life and good, and death and evil.' The covenant's binary choice — life or death, blessing or curse — is Israel's definitive moral situation. Paul's Christological reading of Deut 30 in Romans 10:6-8 is one of his most daring hermeneutical moves: the Torah's own accessibility-language ('not up in heaven, not across the sea, but very near you') is applied to the word of Christ — the gospel is the <em>Torah's own principle</em> of accessibility now embodied in the proclaimed word of faith.</p>"
  }
}

DEUT_CONTEXT = {
  "1": {
    "1": "<p>Deuteronomy is the fifth book of the Torah and claims to be Moses's farewell addresses on the plains of Moab before Israel enters Canaan (Deut 1:1-5). Its genre is that of a suzerainty treaty — a literary form well-attested in Hittite treaties of the second millennium BCE (Meredith Kline's groundbreaking work showed the structural parallels): preamble (1:1-5), historical prologue (1:6-4:49), stipulations (5-26), sanctions/blessings-curses (27-30), succession arrangements (31-34). The treaty-form supports an early date for Deuteronomy's core. The 'Deuteronomistic History' (Joshua through Kings) shares Deuteronomy's theological vocabulary and framework — its editors used Deuteronomy as the lens for evaluating Israel's kings.</p>"
  },
  "18": {
    "20": "<p>The test for a true prophet (18:21-22: if the word does not come to pass, it is not from YHWH) is applied in the NT to Jesus in a reversed form: his words came to pass, validating his prophetic authority. The false-prophet warning (18:20: the prophet who presumes to speak in YHWH's name a word I have not commanded him — that prophet shall die) is the background for Paul's 'if anyone preaches a gospel contrary to the one you received, let him be accursed' (Gal 1:8-9) — the apostolic test of false teaching applies Deuteronomic prophet-testing logic.</p>"
  },
  "34": {
    "10": "<p>'There has not arisen a prophet since in Israel like Moses, whom YHWH knew face to face' (34:10) is Deuteronomy's own closing judgment — the book ends by declaring Moses's prophetic incomparable greatness, which simultaneously points forward to the one greater prophet who is still awaited (18:15). The ending creates an anticipation: Moses is the greatest so far; the prophet-like-Moses is still coming. Hebrews 3:3 completes the comparison: Jesus has been counted worthy of more glory than Moses, as the builder of a house has more honor than the house.</p>"
  }
}

DEUT_CHRIST = {
  "18": {
    "15": "<p>A fulfillment: 'YHWH your God will raise up for you a prophet like me from among you, from your brothers — it is to him you shall listen.' Moses is the OT's supreme mediator — prophet (spoke YHWH's word), priest (offered sacrifice), and king (led the nation). The prophet-like-Moses is therefore the one who fulfills and exceeds all three mediatorial roles. Jesus is explicitly this prophet (Acts 3:22; 7:37), and exceeds him: as the Sermon on the Mount places Jesus's authority above Moses's ('you have heard it said ... but I say to you'), so Hebrews (3:3-6) places Christ's glory above Moses's as Son above servant. The Mosaic mediation was provisional; the Christological mediation is final and complete.</p>"
  },
  "21": {
    "23": "<p>A fulfillment: 'A hanged man is cursed by God.' Paul's citation of Deut 21:23 in Galatians 3:13 is one of his most audacious Christological moves: the cross is the cursed man's tree, and Christ became the curse for us by hanging on it. The law's curse-category — designed for criminals — is the very location where Christ absorbs all covenant-curses. The cross is not a circumvention of Torah-logic but its fulfillment: the law had always required a curse-bearer for the covenant community's sin, and Christ is that bearer. The Deuteronomic law that seemed to disqualify Jesus (a hanged criminal is cursed by God) becomes, in Paul's reading, the very mechanism of redemption.</p>"
  },
  "30": {
    "15": "<p>A direct revelation: 'See I have set before you today life and good, and death and evil.' Deuteronomy's covenant-choice reaches its eschatological fullness in Jesus: 'I am the way, and the truth, and the life' (John 14:6); 'I came that they may have life and have it abundantly' (John 10:10). The choice Moses set before Israel — life or death — is now embodied in a person. To choose Christ is to choose life in the covenant's deepest sense; to reject him is to choose the death that Moses warned of. The binary structure of Deut 30 (life vs. death, blessing vs. curse) is not dissolved in the NT but given its ultimate personal form in Christ.</p>"
  }
}

# ============================================================
# JEREMIAH
# ============================================================

JER_ECHO = {
  "1": {
    "5": [
      {"type": "allusion", "target": "Gal 1:15", "note": "Before I formed you in the womb I knew you, before you were born I consecrated you — Paul describes his own apostolic call with the same language: he was set apart before his birth; the prophetic-call pattern of Jeremiah's consecration becomes the pattern for Paul's apostolic election"}
    ]
  },
  "7": {
    "11": [
      {"type": "fulfillment", "target": "Matt 21:13", "note": "Has this house become a den of robbers in your eyes? — Jesus quotes Jer 7:11 in the temple-cleansing: my house shall be called a house of prayer, but you have made it a den of robbers; the Jeremianic temple-sermon's judgment of Israel's false security in the temple is Jesus's own indictment of the Herodian temple system"}
    ]
  },
  "31": {
    "15": [
      {"type": "fulfillment", "target": "Matt 2:18", "note": "A voice was heard in Ramah, weeping and loud lamentation, Rachel weeping for her children — Matthew cites Jer 31:15 as fulfilled in Herod's massacre of the infants of Bethlehem; Rachel weeping for her exiled children (the Babylonian deportation) is now Rachel weeping for the slaughtered children of Bethlehem"},
      {"type": "allusion", "target": "Luke 23:28", "note": "Jesus's warning to the daughters of Jerusalem to weep not for him but for themselves and their children echoes the Jeremianic pattern of future lamentation over Jerusalem (Jer 9:1; 14:17; 31:15); the weeping-for-Israel motif runs from Jeremiah through Luke's passion narrative"}
    ],
    "31": [
      {"type": "fulfillment", "target": "Heb 8:8-12", "note": "Behold the days are coming when I will make a new covenant with the house of Israel — Hebrews cites Jer 31:31-34 in full (the longest OT quotation in the NT) as the scriptural demonstration that the Mosaic covenant was designed to be superseded; the new covenant's promise (law on hearts, universal knowledge of YHWH, permanent forgiveness) is fulfilled in Christ"},
      {"type": "fulfillment", "target": "Luke 22:20", "note": "This cup is the new covenant in my blood — Jesus at the Last Supper identifies the cup with Jer 31:31-34's new covenant; the blood of Christ is the blood of the covenant Jeremiah announced, making the Lord's Supper the enacted new covenant seal"}
    ]
  }
}

JER_ORIGINAL = {
  "31": {
    "31": "<p><strong>hinei yamim baim neum YHWH vekharati et-beit Yisrael veet-beit Yehudah berit hadasha</strong> (<em>hinnēh yāmîm bāʾîm nĕʾum Yhwh wĕkārattî ʾet-bêt yiśrāʾēl wĕʾet-bêt yĕhûdāh bĕrît ḥădāšāh</em>): 'Behold the days are coming, declares YHWH, when I will make a new covenant with the house of Israel and the house of Judah.' <em>Berit hadasha</em> (new covenant): the only occurrence of this exact phrase in the OT. <em>Hadash</em> (new) can mean 'renewed' (as in the new moon, <em>hodesh</em>) or 'qualitatively different.' Jeremiah's contrast makes it the latter: 'not like the covenant I made with their fathers ... which they broke' (v. 32). The new covenant is distinguished by three characteristics: (1) internalized law (v. 33: on the heart, not stone); (2) universal direct knowledge of YHWH (v. 34: no longer 'know the LORD'); (3) permanent forgiveness (v. 34: I will remember their sin no more).</p>"
  },
  "37": {
    "1": "<p>A brief regnal formula for Zedekiah — <strong>מַלַּךְ</strong> (<em>mallakh</em>, was made king): the passive/causative points to Nebuchadnezzar as the appointing power (v. 1b makes this explicit). <strong>תַּחַת</strong> (<em>tachath</em>, in place of): Coniah/Jeconiah was deposed and exiled (597 BCE); Zedekiah rules as a vassal king, not a free monarch. The opening frames everything that follows: a king installed by Babylon is now secretly consulting the prophet to resist Babylon.</p>",
    "2": "<p><strong>לֹא שָׁמְעוּ</strong> (<em>lo shame'u</em>, they did not listen): the Jeremianic indictment verb — <em>shama'</em> (listen, obey) or its negation is the hinge between covenant obedience and covenant disaster throughout the book. All three parties are indicted: the king, his servants (<em>avadav</em>), and the people of the land (<em>am ha'aretz</em>) — no class is exempt. The words were spoken through (<em>beyad</em>, by the hand of) Jeremiah — the prophetic instrumentality formula.</p>",
    "3": "<p><strong>דְּרַשׁ</strong> (<em>drash</em>, inquire/seek): Zedekiah's sending of envoys to Jeremiah is an act of cultic consultation — <em>drash</em> is the technical verb for seeking a divine oracle. The irony is acute: the king who refuses to heed Jeremiah's sustained preaching still treats him as an oracular resource to be consulted in a crisis. <strong>הִתְפַּלֵּל</strong> (<em>hitpallel</em>, pray): the request is for intercessory prayer — YHWH is approached through the prophet's mediation.</p>",
    "4": "<p><strong>בָּא וְיֹצֵא</strong> (<em>ba veyotze'</em>, coming and going): Jeremiah's freedom of movement is noted because it is about to end. The circumstantial clause explains the state of affairs before the main action of the chapter. The author's literary technique: establish the prophet's relative freedom, then show how it is taken away by those he is trying to warn.</p>",
    "5": "<p>Pharaoh's army (<em>cheil Par'oh</em>) advances and the Chaldeans lift the siege temporarily. <strong>שָׁמְעוּ</strong> (<em>same'u</em>, they heard): the same root used in v2 for Israel's failure to hear — the Chaldeans hear military intelligence and respond; Israel hears the word of YHWH and does not respond. The contrast is built into the vocabulary.</p>",
    "6": "<p>The characteristic prophetic messenger formula: the word of YHWH came (<em>vayehi devar YHWH el</em>) — the initiative is entirely divine; the prophet is a receiver and transmitter, not an originator. The oracle in vv7-10 is YHWH's direct reply to Zedekiah's request for a word.</p>",
    "7": "<p><strong>שֹׁב יָשׁוּב</strong> (<em>shov yashuv</em>, he will return): the infinitive absolute for emphasis — Pharaoh's army will certainly return to Egypt; its departure is not permanent rescue. The same <em>shuv</em> root that means 'repent/return' throughout Jeremiah is used here in its literal sense, but the irony is present: what Israel fails to do (turn/repent to YHWH), Pharaoh's army does naturally (return to its own land).</p>",
    "8": "<p><strong>וְלָכְדוּהָ וּשְׂרָפוּהָ בָאֵשׁ</strong> (<em>velakheduha userafuha va'esh</em>, they will capture it and burn it with fire): the dual fate of the city is stated with unambiguous finality. The burning with fire (<em>esh</em>) is a recurring prophetic image for Jerusalem's destruction (cf. 21:10, 32:29, 38:18) and the fire of YHWH's covenant judgment (Deut 32:22).</p>",
    "9": "<p><strong>אַל-תַּשִּׁאוּ נַפְשֹׁתֵיכֶם</strong> (<em>al-tashi'u nafshoteykhem</em>, do not deceive yourselves): the reflexive idiom — literally 'do not lift up your own lives [in vain hope].' The warning against self-deception is psychologically precise: under siege pressure, people generate false hope from any temporary relief. <em>Halokh yelekhu</em> (they will certainly go away) uses emphatic infinitive absolute — the Chaldeans are definitely not leaving permanently.</p>",
    "10": "<p>The argument reaches extreme hypothetical: even if only wounded men (<em>anashim medukkaim</em>) were left from the Chaldean army, they would still rise and burn the city. The point is theological: the judgment is YHWH's own determination and cannot be deflected by military events. Human calculations are irrelevant when divine decree is operative.</p>",
    "11": "<p>A narrative transition verse — <strong>הֵעָלוֹת חֵיל הַכַּשְׂדִּים</strong> (<em>he'alot cheil hakhashdim</em>, when the Chaldean army had withdrawn/gone up): the siege is lifted. The vocabulary of military withdrawal sets the scene for Jeremiah's attempt to leave the city on private business.</p>",
    "12": "<p><strong>חָלַק מִשָּׁם</strong> (<em>chalaq misham</em>, to receive his portion there): the unusual phrase may mean receiving a hereditary property division or share. Anathoth was Jeremiah's hometown (1:1). The mundane detail — the prophet trying to conduct personal property business during a crisis — is characteristic of Jeremiah's narrative: his life and the city's fate are constantly intertwined. <strong>בְּנִיָמִן</strong> (<em>Binyamin</em>, Benjamin): Anathoth was in the tribal territory of Benjamin.</p>",
    "13": "<p><strong>נֹפֵל אַתָּה אֶל-הַכַּשְׂדִּים</strong> (<em>nofel attah el-hakhashdim</em>, you are defecting/falling to the Chaldeans): <em>nafal el</em> (fall/go over to) is the idiomatic expression for defection, used throughout chs 37-39. The arrest is based on political suspicion, not legal evidence — Irijah does not listen (<em>lo shama'</em>, again the indictment verb) to Jeremiah's denial.</p>",
    "14": "<p><strong>שֶׁקֶר</strong> (<em>sheqer</em>, lie/falsehood): Jeremiah's denial uses the same word that characterizes the false prophets throughout the book. The irony: the only true prophet accuses his accusers of falsehood, while the false prophets are never arrested. Irijah refuses to listen — the echo of v2 (the people refused to listen) is intentional.</p>",
    "15": "<p><strong>הִכּוּ</strong> (<em>hikku</em>, they beat him): the officials' violence against the prophet is unambiguous. <strong>בֵּית הָאֵסוּר</strong> (<em>beit ha'esur</em>, house of detention/imprisonment): literally 'house of the bond/chain.' The scribal house of Jonathan is converted into a prison — the institution of literacy (the scribe) becomes the instrument of prophetic suppression.</p>",
    "16": "<p><strong>חֲנֻיֹּות הַבּוֹר</strong> (<em>chanuyot habor</em>, the vaulted cells of the pit): <em>bor</em> (pit/cistern) is Jeremiah's prison vocabulary — the same word appears in ch38's cistern narrative. The pit (<em>bor</em>) is also the underworld, the place of the dead in Psalms and elsewhere. The prison conditions approximate death — a motif that will be made literal in ch38.</p>",
    "17": "<p><strong>הֲיֵשׁ דָּבָר מֵאֵת יְהוָה</strong> (<em>hayesh davar me'et YHWH</em>, is there a word from YHWH?): Zedekiah's private inquiry is urgent and genuine — he wants to know YHWH's word. Jeremiah's reply is direct: <strong>יֵשׁ</strong> (<em>yesh</em>, there is). The answer: 'You will be handed over to the king of Babylon.' The word from YHWH has not changed since ch21. No imprisonment changes the prophetic word.</p>",
    "18": "<p>Jeremiah's legal complaint (<em>ma chatatati lekha</em>, what have I sinned against you): the language is formal legal protestation of innocence. He inverts the question — if his prophecy was false, what specific wrong did he do? The implicit argument: prophecy that accurately describes what is happening cannot be criminalized.</p>",
    "19": "<p><strong>הַנֹּבְאִים לָכֶם</strong> (<em>hannov'im lakhem</em>, the prophets who prophesied to you): the false prophets who promised 'the king of Babylon will not come against you' are rhetorically invoked. Their non-appearance before the enemy is proof of their falsehood — <em>where are they now?</em> The prophetic vindication comes through historical fulfillment, not institutional endorsement.</p>",
    "20": "<p><strong>תִּפֹּל תַּחֲנוּנָתִי</strong> (<em>tipol tachanunatiy</em>, let my plea fall before you): <em>tachanunim</em> are earnest supplications/entreaties — the word used in prayers seeking mercy. The request not to be returned to Jonathan's prison is the only personal request Jeremiah makes in the entire chapter. The prophet who has given YHWH's word faithfully asks only for basic survival.</p>",
    "21": "<p><strong>חֲצַר הַמַּטָּרָה</strong> (<em>chatzer hamattarah</em>, court of the guard): the less severe confinement — an open courtyard detention rather than a dungeon cell. <strong>כִּכַּר לֶחֶם</strong> (<em>kikkar lechem</em>, loaf of bread): the daily provision from the bakers' street (<em>chutz ha'ofim</em>) until the bread ran out. The narrator preserves the physical detail — the prophet of divine judgment is kept alive by a daily bread allotment, a small mercy in the catastrophe.</p>"
  },
  "38": {
    "1": "<p>Four officials are named who heard Jeremiah's words: Shephatiah son of Mattan, Gedaliah son of Pashhur, Jucal (Jehucal) son of Shelemiah, and Pashhur son of Malchiah. Two of these (Jucal/Jehucal and Pashhur) were previously mentioned as envoys of Zedekiah (37:3; 21:1). They now turn from messengers to accusers — the officials who once sought Jeremiah's help are now seeking his death.</p>",
    "2": "<p><strong>הַיֹּשֵׁב בָּעִיר הַזֹּאת יָמוּת</strong> (<em>hayoshev ba'ir hazot yamut</em>, whoever stays in this city will die): Jeremiah's message is stark — the city is under covenant-curse. <strong>הַנֹּפֵל אֶל-הַכַּשְׂדִּים יִחְיֶה</strong> (<em>hannofeil el-hakhashdim yichyeh</em>, whoever goes over to the Chaldeans will live): the same <em>nafal el</em> (fall to/defect) vocabulary of ch37 — what got Jeremiah arrested is now presented as the survival strategy. The triple death-by-triad: sword, famine, pestilence (<em>cherev, ra'av, dever</em>) for those who stay; life for those who go over.</p>",
    "3": "<p><strong>הִנָּתֵן תִּנָּתֵן</strong> (<em>hinaten tinaten</em>, she will certainly be handed over): emphatic infinitive absolute construction expressing absolute certainty. The grammatical stress on inevitability is characteristic of Jeremiah's judgment speeches — the time for conditional clauses has passed; YHWH's word is now simply declarative.</p>",
    "4": "<p><strong>מְרַפֶּא הוּא אֶת-יְדֵי אַנְשֵׁי הַמִּלְחָמָה</strong> (<em>merappe hu et-yedei anshei hamilchama</em>, he is weakening the hands of the soldiers): the charge uses military/political language — Jeremiah's preaching is not heresy but sedition, undermining military morale (<em>yedei</em>, literally 'the hands' = military capacity). <strong>דֹּרֵשׁ לְשָׁלוֹם</strong> (<em>doresh leshalom</em>, seeking/desiring the welfare): the accusation implies Jeremiah is a collaborator; the officials have inverted the prophetic vocation — the prophet who seeks the true welfare of the people is accused of seeking their harm.</p>",
    "5": "<p><strong>הִנֵּה הוּא בְיֶדְכֶם</strong> (<em>hineh hu beyedkhem</em>, he is in your hands): Zedekiah's capitulation — the royal phrase of abdication. <strong>אֵין הַמֶּלֶךְ יוּכַל אֶתְכֶם דָּבָר</strong> (<em>ein hammelekh yukhal etkhem davar</em>, the king cannot do anything against you): a remarkable admission of the king's powerlessness against his officials. This is the theological problem of Zedekiah's reign: a man who secretly fears YHWH (vv16-17) but is politically paralyzed by his officials.</p>",
    "6": "<p><strong>בּוֹר</strong> (<em>bor</em>, cistern/pit): the same word as ch37's prison (<em>beit ha'asur = house of detention</em> → <em>bor</em> = actual pit). The cistern was used for water storage; when empty (<em>ein bo mayim</em>, no water in it) it became a prison. <strong>וַיִּשְׁקַע יִרְמְיָהוּ בַּטִּיט</strong> (<em>vayishqa Yirmeyahu batit</em>, Jeremiah sank into the mud): the imagery of Ps 40:2 — 'He drew me up from the pit of destruction, out of the miry bog' — is realized literally. The prophet of judgment experiences covenant-curse conditions first-hand.</p>",
    "7": "<p><strong>עֶבֶד-מֶלֶךְ הַכּוּשִׁי</strong> (<em>Eved-Melekh haKushi</em>, Ebed-melech the Ethiopian/Cushite): the name means literally 'servant of the king.' The irony is layered: a foreigner (Cushite, from sub-Saharan Africa), whose name means 'servant of the king,' serves the king of Judah while the Judean officials are murdering the king's — and ultimately YHWH's — prophet. <strong>סָרִיס</strong> (<em>saris</em>, court official/eunuch): the same term for Joseph's Egyptian master (Gen 39:1). A marginalized foreigner whose service to YHWH's prophet will be honored with a specific personal oracle (39:15-18).</p>",
    "8": "<p>Ebed-melech goes directly from the cistern to the king — the narrative pace accelerates. The bureaucratic geography (cistern → king's house) maps the power asymmetry: Ebed-melech, though low in status, has access to the king that he uses on behalf of the imprisoned prophet.</p>",
    "9": "<p><strong>הָרֵעוּ הָאֲנָשִׁים הָאֵלֶּה</strong> (<em>hare'u ha'anashim ha'elleh</em>, these men have done evil): Ebed-melech's accusation before the king uses the covenant-ethics vocabulary — <em>ra'</em> (evil). The practical argument: Jeremiah will die of hunger (<em>ra'av</em>, famine — the word from the covenant-curse triad) before any military action kills him. Even in prison, the covenant curses pursue.</p>",
    "10": "<p>Zedekiah's command: take thirty men (<em>shloshim anashim</em>). The number is strikingly large — it suggests either great concern for Jeremiah's safety against opposition, or the physical difficulty of the rescue from the deep cistern.</p>",
    "11": "<p><strong>סְחָבוֹת בָּלוֹת וּמְלָחִים</strong> (<em>sechabot balot umelachim</em>, worn-out rags and scraps): the mundane materials of Jeremiah's rescue — old rags and worn garments to cushion the rope. The physical detail is preserved because it humanizes the rescue: a powerful court official using worn cloth to save a prophet from a muddy pit. The covenantal imagination sees grace in small provisions.</p>",
    "12": "<p><strong>שִׂים נָא הַסְּחָבוֹת וְהַמְּלָחִים תַּחַת אַצִּלוֹת יָדֶיךָ</strong> (<em>sim na hassechabot vehammelachim tachat atzilot yadekha</em>, put the rags and cloths under your armpits beneath the ropes): physical tenderness in a life-or-death rescue. Ebed-melech's care for the prophet's physical comfort (preventing rope-burn) is noted — the detail reveals a character who does good thoroughly, not minimally.</p>",
    "13": "<p><strong>יַעֲלוּ אֶת-יִרְמְיָהוּ בַּחֲבָלִים</strong> (<em>ya'alu et-Yirmeyahu bachavalim</em>, they pulled Jeremiah up with ropes): the reversal of v6 — thrown in by officials who use their power for death; pulled out by a foreign servant who uses his access for life. Jeremiah returns to the court of the guard (<em>chatzer hamattarah</em>), the intermediate confinement.</p>",
    "14": "<p><strong>בַּמָּבוֹא הַשְּׁלִישִׁי</strong> (<em>bammavo hashlishi</em>, the third entrance): the private, oblique approach — Zedekiah summons Jeremiah to an out-of-the-way entrance for a secret conversation. The secrecy is itself significant: a king who cannot publicly acknowledge the prophet whose words he privately desires.</p>",
    "15": "<p><strong>הֲמוֹת תְּמִיתֵנִי</strong> (<em>hamot temiteni</em>, you will certainly put me to death): emphatic infinitive absolute. Jeremiah pre-empts the risk — his counsel cannot be honest unless he has immunity. The conditional structure (if I tell you ... if I counsel you ...) reveals the trap: the king needs the prophet's word but cannot protect the prophet from his own officials.</p>",
    "16": "<p><strong>חַי-יְהוָה אֲשֶׁר עָשָׂה-לָנוּ אֶת-הַנֶּפֶשׁ הַזֹּאת</strong> (<em>chai-YHWH asher asah-lanu et-hannefesh hazot</em>, as YHWH lives who made this life for us): an oath formula invoking YHWH as both witness and life-giver. <em>Nefesh</em> (life/breath/being) in YHWH's creative provision — the same root as <em>nishmat chayyim</em> (breath of life) in Gen 2:7. Zedekiah's oath is the most theologically weighted statement in the chapter: he knows YHWH, swears by him, but cannot serve him.</p>",
    "17": "<p><strong>יְהוָה אֱלֹהֵי צְבָאוֹת אֱלֹהֵי יִשְׂרָאֵל</strong> (<em>YHWH Elohei Tzvaot Elohei Yisrael</em>): the full throne-room title — YHWH of Hosts, God of Israel. The gravitas of the divine name proportionate to the gravity of the choice. <strong>יָצֹא תֵצֵא</strong> (<em>yatzo tetze</em>, if you go out): the choice Jeremiah presents is <em>shuv</em> (turn/surrender) and live, or refuse and be burned (vv8,18).</p>",
    "18": "<p>The covenant consequences of refusal: the city burned (<em>nitzteta ba'esh</em>), personal capture (<em>lo timalet miyad</em>). The warnings of ch21 and 34 are recapitulated here in direct address to the king. The personal dimension is sharpened — Zedekiah is not just warned about the city but told exactly what will happen to him personally.</p>",
    "19": "<p><strong>יָרֵאתִי</strong> (<em>yare'ti</em>, I am afraid): the royal confession of fear. The king who cannot submit to Babylon fears a third party — the Judean defectors (<em>hanefashim asher nafelu el-hakhashdim</em>). The same <em>nafal el</em> idiom. Political paralysis layered on fear: afraid of Nebuchadnezzar, afraid of the defectors, afraid of his own officials — and therefore unable to act on the word of YHWH.</p>",
    "20": "<p><strong>שְׁמַע בְּקוֹל יְהוָה</strong> (<em>shema beqol YHWH</em>, obey the voice of YHWH): the Deuteronomic obedience formula — <em>shama' beqol</em> is the covenantal call to hear-and-obey. Jeremiah's promise: <strong>וְיִיטַב לְךָ</strong> (<em>veyitav lekha</em>, and it will go well with you) — the blessing side of the covenant. The offer of life is still available, even at this late hour.</p>",
    "21": "<p>The adversative condition: <strong>וְאִם-מָאֵן אַתָּה</strong> (<em>ve'im-maen attah</em>, but if you refuse): the hinge between blessing and curse. YHWH has revealed (<em>hirani YHWH</em>) what will happen if Zedekiah refuses. Prophetic revelation gives exact knowledge of covenant consequences.</p>",
    "22": "<p><strong>הֻצְאוּ כָּל-הַנָּשִׁים</strong> (<em>hutzu kol-hannashim</em>, all the women will be led out): the women of the royal court, Zedekiah's dependents, will be taken to the Babylonian officials. <strong>הֶחֱלִיאֻךָ וְיָכְלוּ לְךָ אַנְשֵׁי שְׁלֹמֶךָ</strong> (<em>hecheli'ukha veyakhlu lekha anshei shlomekha</em>, your trusted men have prevailed against you and defeated you): the taunt-song the women will sing exposes the social reality — the king was destroyed by the very men who should have supported him.</p>",
    "23": "<p><strong>מַלֵּט לֹא תִמָּלֵט</strong> (<em>mallet lo timaleit</em>, you will not escape at all): emphatic double infinitive absolute — absolute certainty of capture. <strong>תִּתָּפֵשׂ</strong> (<em>titafes</em>, you will be seized): the fulfillment comes in 39:5 — word becomes event. The prophecy is not threat but description of inevitable consequence.</p>",
    "24": "<p>Zedekiah's response to prophetic counsel: not acceptance or rejection but a demand for secrecy. <strong>אַל-יֵדַע אִישׁ</strong> (<em>al-yeda ish</em>, let no man know): the king's primary concern is political exposure, not personal survival through obedience.</p>",
    "25": "<p>The scenario Zedekiah anticipates: officials questioning Jeremiah about the content of the private conversation. The king provides a cover story — a plausible official reason for the meeting (Jeremiah was petitioning about his imprisonment).</p>",
    "26": "<p>The cover story: <strong>אֲנִי מַפִּיל תְּחִנָּתִי לִפְנֵי הַמֶּלֶךְ</strong> (<em>ani mappil techinnati lifnei hammelekh</em>, I was laying my plea before the king): <em>techinnah</em> (entreaty/petition) is the word Jeremiah used in 37:20 for his actual request about imprisonment. The official story is a partial truth that conceals the whole truth. The episode raises the ethical complexity of prophetic survival in an authoritarian environment.</p>",
    "27": "<p><strong>וַיִּשְׁאֲלוּ אֹתוֹ</strong> (<em>vayyish'alu oto</em>, they questioned him): the officials do exactly what Zedekiah predicted. Jeremiah's answer follows the king's script. <strong>וַיֶּחֱשׁוּ מִמֶּנּוּ</strong> (<em>vayechashu mimmenu</em>, they were silent/stopped questioning him): the cover holds. The political survival of the prophet is secured — but the theological problem remains: the word that would have saved the city is suppressed.</p>",
    "28": "<p><strong>עַד-הַיּוֹם אֲשֶׁר-נִלְכְּדָה יְרוּשָׁלָ͏ִם</strong> (<em>ad-hayyom asher-nilkedeha Yerushalayim</em>, until the day Jerusalem was captured): the understated narrative close. Jeremiah's confinement continues until the city falls. The final clause of the verse in some manuscripts links directly to ch39 — the prophet in the court of the guard when Jerusalem is captured.</p>"
  },
  "39": {
    "1": "<p>Precise date: the ninth year of Zedekiah, tenth month (January 588 BCE). The Babylonian siege is documented in 2 Kings 25:1 and the Babylonian Chronicles. The specificity of the dating serves a theological function: YHWH's word spoken through Jeremiah is grounded in verifiable historical events, not general predictions. The beginning of the siege is the beginning of the end.</p>",
    "2": "<p><strong>בֻּקְעָה הָעִיר</strong> (<em>buq'ah ha'ir</em>, the city was breached): <em>baqa'</em> (breach/split/cleave) is a violent word — a wall is torn open as a body is torn. The date: eleventh year of Zedekiah, fourth month, ninth day (July 586 BCE). The 18-month siege is over. Tisha B'Av (the ninth of Av) commemorates this event; the later temple destructions are dated to the same annual date in Jewish tradition, making it the day of national catastrophe.</p>",
    "3": "<p>The Babylonian officials take up their positions at the Middle Gate (<em>sha'ar hatavekh</em>). Their names and titles are given: Nergal-sharezer, Samgar-nebo, Sarsekim the Rab-saris, Nergal-sharezer the Rab-mag. The Rab-mag (<em>rav mag</em>) and Rab-saris (<em>rav saris</em>) are Babylonian administrative titles. The presence of named officials in a Hebrew text from this period provides historical corroboration of Jeremiah's setting.</p>",
    "4": "<p><strong>וַיֵּצְאוּ לַיְלָה</strong> (<em>vayyetze'u layelah</em>, they went out by night): Zedekiah's midnight flight — the king who would not surrender by day flees by night. <strong>דֶּרֶךְ גַּן הַמֶּלֶךְ</strong> (<em>derekh gan hammelekh</em>, by way of the king's garden): the king who would not enter the way of covenant submission takes an escape route through his own garden. The irony of 'the king's garden' — all that worldly property he fled to preserve is left behind.</p>",
    "5": "<p><strong>עֲרָבוֹת יְרִיחוֹ</strong> (<em>aravot Yerikho</em>, the plains of Jericho): the geography of the flight and capture is precise. <strong>מִשְׁפָּטִים</strong> (<em>mishpatim</em>, judgments): at Riblah before Nebuchadnezzar, Zedekiah faces formal legal judgments (<em>mishpatim</em>) — the covenant vocabulary for the legal verdict. Riblah in Syria is the administrative center where Nebuchadnezzar conducted his court.</p>",
    "6": "<p><strong>אֶת-בְּנֵי צִדְקִיָּהוּ</strong> (<em>et-benei Tzidkiyahu</em>, the sons of Zedekiah): killed before their father's eyes. The fulfillment of 32:4 and 34:3 — Jeremiah had told Zedekiah he would see the king of Babylon face to face, and so he does, but as a prisoner watching his sons die. Also all the nobles of Judah (<em>kol-chorei Yehudah</em>) are executed — the leadership class that resisted YHWH's word is eliminated.</p>",
    "7": "<p><strong>אֶת-עֵינֵי צִדְקִיָּהוּ עִוֵּר</strong> (<em>et-einei Tzidkiyahu iver</em>, he blinded the eyes of Zedekiah): the last thing Zedekiah sees is his sons' deaths; then his eyes are put out. The fulfillment of Ezek 12:13: 'I will bring him to Babylon ... yet he shall not see it' — a prophecy that seemed contradictory until now: he would be brought to Babylon but not see it (blinded before arrival). <strong>נְחֻשְׁתַּיִם</strong> (<em>nechushtatayim</em>, bronze chains — dual): the dual form = two fetters.</p>",
    "8": "<p><strong>אֶת-בֵּית הַמֶּלֶךְ וְאֶת-בָּתֵּי הָעָם שָׂרַף</strong> (<em>et-beit hammelekh ve'et-battei ha'am saraf</em>, burned the king's palace and the people's houses): the covenant curse of Deut 28:52 realized — your cities will be besieged until your high and fortified walls come down. The burning of the physical city is the physical completion of the spiritual desolation that Jeremiah had been announcing for 40 years.</p>",
    "9": "<p><strong>אֵת יֶתֶר הָעָם</strong> (<em>et yeter ha'am</em>, the rest of the people): Nebuzaradan the captain of the guard (<em>rav tabachim</em>, chief of the butchers/executioners — military title) exiles the survivors. The word for exile, <em>golah</em>, is from <em>galah</em> (to uncover, to go into exile, to strip bare) — the deportation as exposure and vulnerability.</p>",
    "10": "<p><strong>דַּלַּת הָעָם</strong> (<em>dallat ha'am</em>, the poorest of the people — from <em>dal</em>, thin/weak/poor): the ironic remnant. Those who had nothing are given land and vineyards — the covenant promise of the land is partially fulfilled for the poor, the ones the ruling class always marginalized. The covenant's land-promise passes over the king and nobles to the <em>dallim</em>.</p>",
    "11": "<p><strong>בְּיַד נְבוּזַרְאֲדָן</strong> (<em>beyad Nevuzaradan</em>, through Nebuzaradan): the divine arrangement is mediated through the foreign commander. YHWH's protection of Jeremiah reaches through the Babylonian chain of command — Nebuchadnezzar himself gives the orders.</p>",
    "12": "<p><strong>קַח אֹתוֹ וְשִׂים עֵינֶיךָ עָלָיו</strong> (<em>qach oto vesim einekha alav</em>, take him and look after him): the 'set your eyes on him' idiom means attentive protection. <strong>כַּאֲשֶׁר יְדַבֵּר אֵלֶיךָ כֵּן עֲשֵׂה</strong> (<em>ka'asher yedabber elekha ken aseh</em>, do to him as he says to you): complete deference to the prophet's expressed wishes. The foreign king gives the prophet of YHWH more honor than the king of Judah did.</p>",
    "13": "<p>The named officials who carry out the orders — Nebuzaradan, Nebushazban the Rab-saris, Nergal-sharezer the Rab-mag — are the same officials from v3. The administrative machinery that conquered Jerusalem is now the instrument of Jeremiah's protection. Providence works through institutions, including hostile ones.</p>",
    "14": "<p><strong>אֶל-גְּדַלְיָהוּ בֶּן-אֲחִיקָם בֶּן-שָׁפָן</strong> (<em>el-Gedalyahu ben-Achiqam ben-Shaphan</em>): Gedaliah son of Ahikam, the Shaphan-family member who had protected Jeremiah earlier (26:24). The family of Shaphan appears at every critical juncture of Jeremiah's protected survival. Jeremiah is handed over to the one family who consistently honored the prophetic word. <strong>לְהֵשֶׁב בְּתוֹךְ הָעָם</strong> (<em>leheshev betokh ha'am</em>, to live among the people): Jeremiah's preferred place — among the remaining people in the land.</p>",
    "15": "<p>A temporal insertion: the oracle to Ebed-melech was delivered while Jeremiah was still in the court of the guard — before the city fell. The placement here, after the fall narrative, signals the author's thematic intention: the faithfulness of the foreign servant is rewarded with a personal salvation oracle, placed in contrast to Zedekiah's fate.</p>",
    "16": "<p><strong>מֵבִיא אֶת-דְּבָרַי אֶל-הָעִיר הַזֹּאת לְרָעָה וְלֹא לְטוֹבָה</strong> (<em>mevi et-devarai el-ha'ir hazot lera'ah velo letovah</em>, bringing my words against this city for harm and not for good): the words-coming-to-fulfillment formula. YHWH's words are the active agent — they 'come' (<em>bo</em>) to the city as he himself 'comes' in judgment. <strong>לְעֵינֶיךָ בַּיּוֹם הַהוּא</strong> (<em>le'einekha bayyom hahu</em>, before your eyes on that day): Ebed-melech will witness the fulfillment.</p>",
    "17": "<p><strong>אֲבָל אַמַּלְטְךָ בַּיּוֹם הַהוּא</strong> (<em>aval amaltetkha bayyom hahu</em>, but I will deliver you on that day): the adversative <em>aval</em> (but/however) is the pivot of grace within judgment. While the city falls, the foreign servant is exempted. <strong>לֹא תִנָּתֵן בְּיַד הָאֲנָשִׁים אֲשֶׁר-אַתָּה יָגוֹר מִפְּנֵיהֶם</strong> (<em>lo tinaten beyad ha'anashim asher-attah yagor mipneihem</em>, you will not be given into the hands of the men you fear): the covenant protection language.</p>",
    "18": "<p><strong>כִּי-בָטַחְתָּ בִּי</strong> (<em>ki-vatachta bi</em>, because you trusted in me): the theological ground of Ebed-melech's rescue — not his ethnicity, not his court status, but his <em>batach</em> (trust/reliance) in YHWH. The same verb (batach) used in the Psalms for confident trust in YHWH as refuge. A foreign servant who trusted YHWH receives the covenant promise of protection that Judah's own king refused through disobedience.</p>"
  },
  "40": {
    "1": "<p>Released at Ramah (<em>Ramah</em>): a holding area for deportees north of Jerusalem. The opening temporal clause situates this after the fall but before Jeremiah's definitive movement — a second calling/release narrative. <strong>בַּחֲנִקִּים אֲסֻר בְּתוֹךְ כָּל-גָּלוּת יְרוּשָׁלַ͏ִם</strong> (<em>bachanickim asur betokh kol-galut Yerushalayim</em>, bound with chains among all the exiles of Jerusalem): the prophet of exile is himself counted among the exiles, chained with them — he shares the suffering of the people whose judgment he announced.</p>",
    "2": "<p><strong>יְהוָה אֱלֹהֶיךָ דִּבֶּר אֶת-הָרָעָה הַזֹּאת</strong> (<em>YHWH Elohekha dibber et-hara'ah hazot</em>, YHWH your God spoke this disaster): a pagan commander confessing YHWH's prophetic sovereignty — 'YHWH your God pronounced this disaster.' The Babylonian acknowledges what Zedekiah's court refused to acknowledge: the disaster was YHWH's word made event. The irony is total: the foreign conqueror understands the theology; the covenant people did not.</p>",
    "3": "<p><strong>כַּאֲשֶׁר דִּבֶּר וַיַּעַשׂ יְהוָה</strong> (<em>ka'asher dibber vayyaas YHWH</em>, as he said, so YHWH has done): Nebuzaradan's creedal summary — YHWH spoke and acted exactly as he said. This is the core of prophetic theology: the word and its fulfillment are one movement. <strong>לֹא-שְׁמַעְתֶּם בְּקוֹל יְהוָה</strong> (<em>lo-shame'tem beqol YHWH</em>, you did not obey the voice of YHWH): the pagan officer uses the covenant-indictment formula — the <em>shama' beqol</em> that Deuteronomy required and Jeremiah demanded. The foreigner pronounces the verdict the people refused to hear from their own prophet.</p>",
    "4": "<p><strong>הַיּוֹם פָּטַחְתִּי אֶת-הָאַזִּקִּים</strong> (<em>hayyom patachti et-ha'aziqim</em>, today I have released your fetters): <em>aziqim</em> = shackles/chains. The day of Jeremiah's release from chains is a small personal exodus — physically freed from bondage in the moment of national exile. <strong>אֶל כָּל-הַטּוֹב בְּעֵינֶיךָ לָלֶכֶת שָׁם</strong> (<em>el kol-hattov be'einekha lalechet sham</em>, to wherever seems good in your eyes to go): genuine freedom of choice offered by the Babylonian commander — a freedom the king of Judah never gave the prophet.</p>",
    "5": "<p><strong>שׁוּב אֶל-גְּדַלְיָּהוּ</strong> (<em>shuv el-Gedalyahu</em>, return to Gedaliah): the use of <em>shuv</em> (return) here is ironic — the prophet who spent 40 years calling Israel to <em>shuv</em> to YHWH is now told by a Babylonian to <em>shuv</em> to the land. <strong>וּשְׁבֵה אִתּוֹ בְּתוֹךְ הָעָם</strong> (<em>ushvei itto betokh ha'am</em>, and live with him among the people): <em>yashav</em> (dwell/sit/remain) — Jeremiah's choice is to dwell with the remnant rather than receive Babylonian support. The prophet identifies with the people in their land even in their humiliation.</p>",
    "6": "<p><strong>מִצְפָּה</strong> (<em>Mitzpah</em>, Mizpah): literally 'watchtower/lookout point' — the administrative capital of the post-conquest remnant community. The covenant symbol: even after the destruction of Jerusalem and the temple, YHWH has a people in the land, and Jeremiah is among them. The land promised to Abraham, which the exile has not permanently revoked, still has a remnant.</p>",
    "7": "<p>The captains of the forces in the open country (<em>sarei hachayalot asher bassadeh</em>) and their men hear the news of Gedaliah's appointment. They had avoided capture by being outside the city. The post-conquest social geography: the poorest remained (v10), the military forces hiding in the countryside return.</p>",
    "8": "<p>Named captains come to Gedaliah at Mizpah: Ishmael son of Nethaniah (whose name and pedigree — son of Nethaniah, Elishama — will become significant in ch41), Johanan and Jonathan sons of Kareah, Seraiah, the sons of Ephai the Netophathite, and Jezaniah son of the Maacathite. The inventory of names preserves the historical reality of the remnant community's military leadership.</p>",
    "9": "<p><strong>אַל-תִּירְאוּ מֵעֲבוֹד אֶת-הַכַּשְׂדִּים</strong> (<em>al-tire'u me'avod et-hakhashdim</em>, do not be afraid to serve the Chaldeans): Gedaliah's foundational speech uses <em>yare'</em> (fear) and <em>aved</em> (serve) — the Deuteronomic vocabulary of covenantal service (serve YHWH; fear YHWH). He redirects this language to the political reality: the survival strategy is to serve Babylon, which is precisely what Jeremiah had been saying for decades. <strong>שְׁבוּ בָאָרֶץ</strong> (<em>shevu va'aretz</em>, settle/dwell in the land): the covenant promise — living in the land — is possible even under Babylonian governance if the community submits.</p>",
    "10": "<p><strong>לִפְנֵי הַכַּשְׂדִּים</strong> (<em>lifnei hakhashdim</em>, before the Chaldeans): Gedaliah will represent the community to the Babylonian administrators. <strong>אִסְפוּ יַיִן וְקַיִץ וְשֶׁמֶן</strong> (<em>isfu yayin veqayitz veshemen</em>, gather wine and summer fruit and oil): the covenant land's agricultural abundance is still available — the harvest is not canceled. The return to normal agricultural life is both practical instruction and a covenant sign: the land still produces for those who remain in it.</p>",
    "11": "<p>Jews in Moab, Ammon, Edom, and other nations — the diaspora before the formal exile — hear that the king of Babylon has left a remnant in the land. <strong>פְּלֵיטָה</strong> (<em>peleitah</em>, remnant/surviving fugitives): the remnant theology — YHWH always preserves a <em>peleitah</em>, a surviving band (cf. Isa 37:32; Joel 2:32). Even in judgment, the covenant promise of continuity is not extinguished.</p>",
    "12": "<p><strong>וַיָּשֻׁבוּ כָּל-הַיְּהוּדִים מִכָּל-הַמְּקֹמוֹת</strong> (<em>vayashuvu kol-haYehudim mikol-hamqomot</em>, all the Jews returned from all the places): the double <em>kol</em> (all) emphasizes the scope — a mini-return from exile. This small return is a foretaste of the larger return prophesied in chs 30-33. The gathering at Gedaliah's Mizpah is a type of the eschatological ingathering.</p>",
    "13": "<p>Johanan son of Kareah and the military captains come to Gedaliah — the scene transitions from hopeful gathering to ominous warning. The intelligence they bring (Ishmael is plotting assassination) will be refused by Gedaliah, with catastrophic consequences.</p>",
    "14": "<p><strong>הֲיָדֹעַ תֵּדַע</strong> (<em>hayado' teda'</em>, do you really know?): the interrogative with emphatic infinitive absolute — surely you know! Baalis king of Ammon (<em>merekh Bene-Ammon</em>) has sent Ishmael to assassinate Gedaliah. The Ammonite king's political interest: preventing a stable Judean remnant that might eventually resist Ammonite expansion into formerly Judean territory. Political instability in the region is geopolitically useful to Ammon.</p>",
    "15": "<p><strong>בַּסֵּתֶר</strong> (<em>basseter</em>, secretly): Johanan offers to kill Ishmael privately — assassination to prevent assassination. <strong>לָמָּה יַכֶּכָּה וְנָפֹצוּ כָּל-יְהוּדָה הַנִּקְבָּצִים אֵלֶיךָ</strong> (<em>lammah yakkekha venafotzou kol-Yehudah haniqbatzim elekha</em>, why should he strike you down and scatter all the Jews gathered around you?): the practical argument — the remnant community is fragile; killing Ishmael would preserve it.</p>",
    "16": "<p><strong>לֹא-תַעֲשֶׂה הַדָּבָר הַזֶּה</strong> (<em>lo-ta'aseh haddavar hazzeh</em>, you must not do this): Gedaliah's refusal is absolute. <strong>שֶׁקֶר אַתָּה דֹּבֵר אֶל-יִשְׁמָעֵאל</strong> (<em>sheqer attah dover el-Yishma'el</em>, you are speaking falsely about Ishmael): the tragic final word of ch40. Gedaliah's <em>sheqer</em> — calling Johanan's warning a lie — echoes the entire book's pattern: the truth-tellers are not believed; the covenant community repeatedly fails to hear the word that would save it. The chapter ends with Gedaliah's fatal error stated plainly, awaiting the catastrophe of ch41.</p>"
  }
}

JER_CONTEXT = {
  "1": {
    "1": "<p>Jeremiah prophesied ca. 627-586 BCE (from the 13th year of Josiah through the fall of Jerusalem and beyond), the most turbulent period in Judah's history. He witnessed Josiah's reform (621 BCE, 2 Kings 22-23) and its collapse, the defeats at Megiddo (609 BCE) and Carchemish (605 BCE), Nebuchadnezzar's three deportations (605, 597, 586 BCE), the destruction of Jerusalem and the temple (586 BCE), and the assassination of Gedaliah. His call at the outset of his ministry and his suffering throughout (the 'Confessions', Jer 11-20) make him the most personal of the prophets — his inner life is more visible in Scripture than any other OT figure. The 'new covenant' oracle (31:31-34) is addressed to a people in the ruins of the Babylonian exile.</p>"
  },
  "31": {
    "34": "<p>The three promises of Jer 31:33-34 in their historical context: (1) the Torah internalized on hearts rather than carved on tablets solves the problem that generated the exile — Israel kept the external law while their hearts were far from YHWH; (2) the universal knowledge of YHWH solves the class-stratification of covenantal knowledge (prophets, priests, sages knew; the people often did not); (3) the permanent forgiveness ('I will remember their sin no more') solves the accumulated sin-debt that the Mosaic sacrificial system could cover but not finally remove (Heb 10:1-4: the law has a shadow ... sacrifices cannot make perfect those who draw near). The new covenant addresses precisely the structural deficiencies of the Mosaic covenant.</p>"
  }
}

JER_CHRIST = {
  "31": {
    "31": "<p>A direct revelation: 'Behold the days are coming when I will make a new covenant with the house of Israel and the house of Judah.' The new covenant is the Christological center of the OT's prophetic program: Jesus at the Last Supper explicitly claims to enact this covenant (Luke 22:20: 'This cup that is poured out for you is the new covenant in my blood'), and Hebrews quotes all of Jer 31:31-34 (8:8-12) as the scriptural proof that the old covenant's priesthood and sacrificial system were provisional and superseded. The three elements of the new covenant are fulfilled in Christ: (1) law on hearts → the Spirit writes Christ's character in the believer; (2) universal knowledge of YHWH → all who come to Christ know the Father (John 17:3); (3) permanent forgiveness → the once-for-all sacrifice of Christ (Heb 9:26-28; 10:14).</p>"
  }
}

# ============================================================
# EZEKIEL
# ============================================================

EZEK_ECHO = {
  "11": {
    "19": [
      {"type": "fulfillment", "target": "2 Cor 3:3", "note": "I will remove the heart of stone and give them a heart of flesh — the new heart/new spirit promise of Ezek 11:19 and 36:26 is fulfilled in the Spirit's ministry that Paul describes: written not on stone tablets but on tablets of human hearts"}
    ]
  },
  "34": {
    "11": [
      {"type": "fulfillment", "target": "John 10:11", "note": "I myself will search for my sheep and seek them out — YHWH's own shepherding (Ezek 34:11-16) is enacted by Jesus as the Good Shepherd; what YHWH promised to do for his abandoned sheep (I myself will shepherd them) is what Jesus claims to be doing: I am the good shepherd"}
    ]
  },
  "36": {
    "25": [
      {"type": "fulfillment", "target": "John 3:5", "note": "I will sprinkle clean water on you and you shall be clean; I will give you a new spirit — the new birth of water and Spirit in John 3:5 is the fulfillment of Ezek 36:25-27; what Ezekiel prophesied as the new covenant's cleansing and Spirit-filling is what Jesus announces as the necessary birth for entering the kingdom"}
    ]
  },
  "37": {
    "1": [
      {"type": "allusion", "target": "John 11:43-44", "note": "The valley of dry bones that come to life at YHWH's breath-word — Jesus's command 'Lazarus, come out' is the personal enactment of the eschatological resurrection vision of Ezek 37; the Spirit's breath (John 20:22) that animates the church repeats the pattern of Ezek 37:9-10"}
    ]
  },
  "47": {
    "1": [
      {"type": "fulfillment", "target": "Rev 22:1", "note": "The river of water flowing from the temple — Ezekiel's visionary river (increasingly deep, bringing life to everything it touches) is fulfilled in Revelation's river of life flowing from the throne of God and the Lamb; Jesus is himself the source of living water (John 7:38-39)"}
    ]
  }
}

EZEK_ORIGINAL = {
  "1": {
    "28": "<p><strong>ke-mareh haqeshet asher yihyeh beanav beyom hagashem ken mareh hanog saviv hu mareh demut kevod YHWH</strong>: 'Like the appearance of the bow that is in the cloud on the day of rain, so was the appearance of the brightness all around. Such was the appearance of the likeness of the glory of YHWH.' Ezekiel's theophany of the divine chariot-throne (<em>merkabah</em>) is the foundation of Jewish mystical speculation. His careful qualification of language — 'likeness of the glory of YHWH' rather than 'glory of YHWH' — maintains divine transcendence even in the vision. John of Revelation reuses Ezekiel's visionary vocabulary (the four living creatures of Ezek 1 reappear in Rev 4:6-8; the rainbow around the throne in Rev 4:3 echoes Ezek 1:28), grounding the Christological throne-vision in the Ezekielian framework.</p>"
  },
  "36": {
    "26": "<p><strong>venathati lachem lev hadash veruach hadasha etten bekirbechem vahashirothi et-lev haeben mivsarchem venatati lachem lev basar</strong>: 'And I will give you a new heart and a new spirit I will put within you. And I will remove the heart of stone from your flesh and give you a heart of flesh.' The new heart-new spirit promise is the Ezekielian new covenant (parallel to Jer 31:31-34). <em>Lev hadash</em> (new heart): the decision-making center (<em>lev</em>) of human personhood is replaced — not repaired, not improved, but new. <em>Ruach hadasha</em> (new spirit): YHWH's own Spirit placed within (v. 27: 'I will put my Spirit within you and cause you to walk in my statutes'). This is Pentecost prophesied — the Spirit's indwelling that replaces external Torah-motivation with internal Spirit-empowered desire and ability to obey.</p>"
  }
}

EZEK_CONTEXT = {
  "1": {
    "1": "<p>Ezekiel was a priest who was deported to Babylon in the first deportation (597 BCE) and received his call-vision in 593 BCE by the Chebar canal in Babylonia ('the thirtieth year', 1:1 — possibly his own thirtieth year, the age for priestly service). He prophesied to the exilic community ca. 593-571 BCE. His priestly background shapes his theology: the book is preoccupied with divine glory (<em>kavod</em>), the departure of the Shekinah from the temple (chs. 8-11), and its eschatological return (chs. 40-48). The merkabah vision (ch. 1) was the most influential single vision in subsequent Jewish mysticism — the Hekhalot literature built an entire tradition of heavenly ascent around it. The four living creatures (lion, ox, eagle, human) reappear in Irenaeus's identification of the four Gospel symbols.</p>"
  },
  "37": {
    "1": "<p>The valley of dry bones vision (37:1-14) is addressed to the exilic community that had concluded 'our bones are dried up, our hope is lost, we are indeed cut off' (v. 11). The corporate resurrection metaphor — national restoration envisioned as bodily resurrection — uses the imagery of physical resurrection for Israel's return from exile. This is not a straightforward prophecy of individual eschatological resurrection (though the same imagery is applied there in Isa 26:19; Dan 12:2), but a bold use of resurrection as the metaphor for what only divine creative power could accomplish for the exiled nation. The NT develops the resurrection-from-exile typology: Christ's resurrection is both personal and the beginning of the great return-from-death that Ezekiel envisioned.</p>"
  }
}

EZEK_CHRIST = {
  "34": {
    "11": "<p>A direct revelation: 'For thus says the Lord GOD: Behold I, I myself will search for my sheep and seek them out ... I will rescue them from all places where they have been scattered ... I will seek the lost and I will bring back the strayed and I will bind up the injured and I will strengthen the weak.' Jesus's 'I am the good shepherd' (John 10:11) and the parable of the lost sheep (Luke 15:4-6) are the incarnational enactment of Ezek 34's promise. What YHWH said he himself would do (in contrast to the failed shepherds of Israel's leaders) is what Jesus does: the divine shepherd-promise is fulfilled by the Son who is YHWH present in person, doing what YHWH promised he personally would do for the scattered flock.</p>"
  },
  "36": {
    "27": "<p>A direct revelation: 'And I will put my Spirit within you and cause you to walk in my statutes and be careful to obey my rules.' Pentecost is Ezekiel 36:27 enacted. The Spirit's indwelling is not merely motivational but causally efficacious: 'I will cause you to walk' — the Hebrew Hiphil form makes YHWH the enabling cause of the obedience that follows. This is the new covenant's answer to the old covenant's demand without the enabling Spirit: the same Torah-standard now fulfilled because the Spirit from within enables what the law from without could only command. Paul's 'the righteous requirement of the law might be fulfilled in us who walk not according to the flesh but according to the Spirit' (Rom 8:4) is the Christological-pneumatological fulfillment of Ezek 36:27.</p>"
  },
  "47": {
    "9": "<p>A type: 'And wherever the river goes, every living creature that swarms will live, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes.' The eschatological temple-river of Ezekiel's vision (ch. 47), increasingly deep and life-giving, is the OT type for the water that flows from Christ. Jesus at Tabernacles (John 7:38-39) applies the Spirit-water promise to himself: 'rivers of living water will flow from within him' — and John explains this is the Spirit. Revelation's new creation river (22:1) flowing from the throne of God and the Lamb completes the Ezekiel type: the new temple's river is Christ himself, and all who drink from him live.</p>"
  }
}

# ============================================================
# DANIEL
# ============================================================

DAN_ECHO = {
  "2": {
    "44": [
      {"type": "fulfillment", "target": "Luke 1:33", "note": "The God of heaven will set up a kingdom that shall never be destroyed — the stone that becomes a great mountain filling the whole earth (Dan 2:35, 44) is fulfilled in the kingdom announced by the angel: his kingdom will have no end"},
      {"type": "fulfillment", "target": "Rev 11:15", "note": "The kingdom of the world has become the kingdom of our Lord and of his Christ — the seventh trumpet's announcement is the explicit fulfillment of Dan 2:44's never-to-be-destroyed kingdom of heaven"}
    ]
  },
  "7": {
    "13": [
      {"type": "fulfillment", "target": "Matt 26:64", "note": "You will see the Son of Man seated at the right hand of Power and coming on the clouds of heaven — Jesus applies Dan 7:13 to himself before the Sanhedrin; the coming on the clouds of heaven is the exaltation of the Son of Man to the divine throne, which the high priest recognizes as blasphemy"},
      {"type": "fulfillment", "target": "Acts 1:9", "note": "A cloud took him out of their sight — the ascension cloud echoes the Son of Man coming with the clouds of Dan 7:13; the ascension is the enthronement, not a departure to a distant location"},
      {"type": "fulfillment", "target": "Rev 1:7", "note": "Behold he is coming with the clouds — Revelation combines Dan 7:13 with Zech 12:10 to describe the parousia as the final manifestation of the Son of Man's cloud-coming that began at the ascension"}
    ]
  },
  "9": {
    "24": [
      {"type": "allusion", "target": "Luke 4:18", "note": "To anoint a most holy place — the seventy weeks leading to the anointing of the most holy one (or most holy place) has been interpreted as pointing to Christ's anointing at baptism; the messianic anointing is the fulfillment of Daniel's eschatological program"},
      {"type": "allusion", "target": "Heb 9:26", "note": "To finish transgression, put an end to sin, and atone for iniquity — the six goals of Daniel's seventy weeks (9:24) are summarized in Hebrews: he has appeared once for all at the end of the ages to put away sin by the sacrifice of himself"}
    ]
  },
  "12": {
    "2": [
      {"type": "fulfillment", "target": "John 5:28-29", "note": "Many who sleep in the dust of the earth shall awake, some to everlasting life and some to shame and everlasting contempt — Jesus's promise of a resurrection of all the dead, some to life and some to judgment, applies Dan 12:2's general resurrection language to himself as the one who gives life and judges"}
    ]
  }
}

DAN_ORIGINAL = {
  "7": {
    "13": "<p><strong>hazeh haveit bechezwe leylaya vaara im-anane shemayya kebar enash ateh vead attiq yomaya matah uqdamoy haytivuhi</strong> (Aramaic): 'I saw in the night visions, and behold, with the clouds of heaven there came one like a son of man, and he came to the Ancient of Days and was presented before him.' The 'one like a son of man' (<em>kebar enash</em>, Aramaic for 'like a human being') in Daniel 7 contrasts with the four beasts (lions, bears, leopards, a terrible beast) that rise from the sea — representing successive human empires. The human figure comes from heaven, not the sea, and receives the dominion the beasts claimed. The NT application (Jesus's self-designation as 'Son of Man' in all four Gospels) is the consistent claim that Jesus is this figure who receives eternal dominion from the Ancient of Days — a claim recognized as divine by the Sanhedrin (Mark 14:62-64).</p>"
  },
  "9": {
    "24": "<p><strong>shivim shavuim nechetach al-amecha vehal ir qadshecha lekale happesha ulehatem chataut velchapper avon ulehavi tsdeq olamim velachtom chazot venavia velimshoach qodesh qodashim</strong>: 'Seventy weeks are decreed about your people and your holy city, to finish the transgression, to put an end to sin, to atone for iniquity, to bring in everlasting righteousness, to seal both vision and prophet, and to anoint a most holy place.' The six infinitives of Dan 9:24 have generated centuries of calculation and debate. The <em>shavuim</em> (weeks/sevens) are most naturally weeks of years (seven-year units), giving 490 years from the decree to rebuild Jerusalem. The six goals — which are systematically soteriological and eschatological — align most naturally with Christ's work: atonement (to finish transgression, atone for iniquity), righteousness (bring in everlasting righteousness), and the end of the prophetic age (seal vision and prophet).</p>"
  }
}

DAN_CONTEXT = {
  "1": {
    "1": "<p>The book of Daniel is set in the Babylonian exile (605-538 BCE) and narrates the experiences of four young Jewish men under Nebuchadnezzar, Belshazzar, Darius the Mede, and Cyrus of Persia. The historical reliability of Daniel's court settings has been debated (Darius the Mede is unattested by name in Babylonian records; some details seemed anachronistic). The primary critical alternative: Daniel was composed ca. 167-164 BCE during the Maccabean revolt, as <em>vaticinium ex eventu</em> (prophecy after the fact) using the fictional setting of the sixth century. Conservative scholars argue for a sixth century date and understand the Darius question as a secondary title for Cyrus or an otherwise unrecorded official. The book's affinities with the Aramaic of the fifth-fourth centuries and the absence of Greek loanwords that would be expected in a second century BCE composition support an early composition.</p>"
  },
  "7": {
    "1": "<p>Daniel 7-12 contains four major apocalyptic visions. The genre of apocalypse (from Greek <em>apokalypsis</em>, unveiling) is characterized by: symbolic or heavenly visions mediated by an angel, disclosure of the heavenly perspective on historical events, periodization of history into fixed sequences, and imminent divine intervention. Daniel is the OT's primary apocalyptic text; its imagery (beasts from the sea, the Ancient of Days, the Son of Man, the four kingdoms) was enormously influential on Jewish and Christian apocalyptic (1 Enoch, 4 Ezra, 2 Baruch, and the NT's Revelation). Jesus's eschatological discourse (Mark 13 and parallels) draws extensively from Daniel, particularly the abomination of desolation (Dan 11:31; 12:11 → Mark 13:14) and the coming of the Son of Man (Dan 7:13 → Mark 13:26).</p>"
  }
}

DAN_CHRIST = {
  "7": {
    "13": "<p>A direct revelation: 'One like a son of man came with the clouds of heaven and came to the Ancient of Days and was presented before him. And to him was given dominion and glory and a kingdom, that all peoples, nations, and languages should serve him; his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed.' Jesus's consistent self-identification as 'the Son of Man' throughout the Gospels is a deliberate claim to be this figure — the one who receives from the Ancient of Days the universal, eternal dominion. The ascension is the receiving of this dominion; Pentecost is the beginning of its exercise; the parousia is its final manifestation. The 'Son of Man' claim is Jesus's most characteristic and most Christologically loaded self-designation.</p>"
  },
  "9": {
    "26": "<p>A fulfillment: 'After sixty-two weeks, an anointed one shall be cut off and shall have nothing.' The phrase 'cut off' (<em>yikaret</em>) is the judicial-death vocabulary of Torah (used for capital offenses). The anointed one is cut off not for his own sins (the grammar allows 'and there is nothing to him' or 'but not for himself') — the same pattern as Isa 53:8 ('cut off out of the land of the living ... for the transgression of my people'). Regardless of the precise calculation of the seventy weeks, the Christological core is the same: the anointed one (the Messiah) dies, is cut off, apparently without inheriting anything — and yet this death is the very mechanism by which the six goals of v. 24 are accomplished. The cross is Daniel's predicted event.</p>"
  },
  "12": {
    "2": "<p>A direct revelation: 'And many of those who sleep in the dust of the earth shall awake, some to everlasting life and some to shame and everlasting contempt.' Daniel 12:2 is the OT's clearest statement of a general resurrection with differentiated outcomes — resurrection to life and resurrection to judgment. Jesus applies this directly to himself: 'The hour is coming when all who are in the tombs will hear his voice and come out, those who have done good to the resurrection of life and those who have done evil to the resurrection of judgment' (John 5:28-29). Christ is the voice that summons from the tombs — the executor of Daniel's two-outcome resurrection — and his own resurrection is the first fruits of what Dan 12:2 prophesied for the final eschatological hour.</p>"
  }
}

def main():
    books_data = [
        ('deuteronomy', DEUT_ECHO, DEUT_ORIGINAL, DEUT_CONTEXT, DEUT_CHRIST),
        ('jeremiah', JER_ECHO, JER_ORIGINAL, JER_CONTEXT, JER_CHRIST),
        ('ezekiel', EZEK_ECHO, EZEK_ORIGINAL, EZEK_CONTEXT, EZEK_CHRIST),
        ('daniel', DAN_ECHO, DAN_ORIGINAL, DAN_CONTEXT, DAN_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book)
        merge_echo(e, echo_d)
        save_echo('', e) if False else save_echo(book, e)

        c = load_comm('mkt-original', book)
        merge_comm(c, orig_d)
        save_comm('mkt-original', book, c)

        c = load_comm('mkt-context', book)
        merge_comm(c, ctx_d)
        save_comm('mkt-context', book, c)

        c = load_comm('mkt-christ', book)
        merge_comm(c, chr_d)
        save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
