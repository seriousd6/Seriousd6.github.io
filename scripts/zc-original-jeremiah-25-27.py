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
  "25": {
    "1": "<p>A precise date formula — the fourth year of Jehoiakim = 605 BCE, the year of the Battle of Carchemish, when Nebuchadnezzar decisively defeated Egypt and became the dominant power in the region. Jeremiah places his ministry in the sweep of international history.</p>",
    "2": "<p>Jeremiah speaks to all the people of Judah and all the inhabitants of Jerusalem — the universal audience mirrors the universal scope of the coming judgment; no one is exempt from hearing or from the covenant's consequences.</p>",
    "3": "<p><strong>מִשְּׁלֹשׁ עֶשְׂרֵה שָׁנָה</strong> (<em>mishlosh esreh shanah</em>, from the thirteenth year): Jeremiah's call was in the 13th year of Josiah (1:2) — making this 23 years of continuous prophesying. The length of service emphasizes the depth of Israel's stubborn refusal.</p>",
    "4": "<p><strong>הַשְׁכֵּם וְשָׁלֹחַ</strong> (<em>hashkem veshaloach</em>, rising early and sending): the infinitive absolute construction used repeatedly in Jeremiah for YHWH's persistent sending of his prophets — rising early connotes eager, urgent, repeated action. Despite this diligence, the people have not listened (<em>lo sham'u</em>) or inclined their ear (<em>lo hitu oznekhem</em>).</p>",
    "5": "<p>The core demand of the prophets: turn (<em>shuvu</em>) each from his evil way and evil deeds (<em>ma'alelav hara'im</em>), and dwell in the land that YHWH gave. The covenant offer was perpetually available — prophets were not bringing new information but calling back to what was already known.</p>",
    "6": "<p>Do not go after other gods to serve and bow down to them — the Shema's exclusive loyalty demand restated. Do not provoke YHWH with the work of your hands (<em>bema'aseh yedekhem</em>) — the idol-making described in ch 10 as provoking YHWH directly.</p>",
    "7": "<p>You have not listened to me — YHWH's verdict after 23 years. The idol-worship provokes YHWH (<em>le-ma'an hach'is oti</em>) to their own harm (<em>lera' lakhem</em>). The self-destructive nature of apostasy: it harms the people, not primarily YHWH.</p>",
    "8": "<p>Therefore — the covenant consequence clause (<em>laken</em>) follows the indictment. Because you have not heard my words, the judgment follows necessarily from the structure established in the covenant curses of Deuteronomy.</p>",
    "9": "<p><strong>עַבְדִּי</strong> (<em>avdi</em>, my servant): Nebuchadnezzar king of Babylon is called YHWH's servant — one of the most striking titles in Jeremiah. The same title is given to the prophets ('my servants the prophets', v4) and to David (Ps 89:3). YHWH claims sovereignty over the greatest earthly power by incorporating it into his covenantal purposes. <strong>חֶרֶב</strong> (<em>cherev</em>, sword), <strong>רָעָב</strong> (<em>ra'av</em>, famine), <strong>דֶּבֶר</strong> (<em>dever</em>, pestilence) — the classic covenant-curse triad of Lev 26:25-26 and Deut 28:21-22.</p>",
    "10": "<p>YHWH will banish the sound of joy (<em>qol sason</em>), gladness (<em>qol simcha</em>), the voice of the bride (<em>qol chatan vekol kallah</em>), and the sound of the millstone (<em>qol rechayim</em>) — the sounds of normal life. The absence of wedding sounds and grinding sounds signals complete social breakdown. Cf. Rev 18:22-23 where these same sounds mark the fall of Babylon.</p>",
    "11": "<p><strong>שִׁבְעִים שָׁנָה</strong> (<em>shivim shanah</em>, seventy years): the exile duration. The number may be symbolic (a human lifetime, a sabbath of decades) or roughly chronological (605-538 BCE = 67 years). Daniel 9:2 understood it literally and prayed toward its fulfillment. The point is the fixed, purposeful nature of the judgment — not open-ended but bounded by YHWH's plan.</p>",
    "12": "<p>After seventy years, YHWH will punish (<em>epoqod</em>, visit in judgment) the king of Babylon and that nation — making it an eternal wasteland (<em>shemamot olamim</em>). The same judgment standard applied to Judah is applied to Babylon: serving as YHWH's instrument does not exempt Babylon from accountability for its own cruelty.</p>",
    "13": "<p>YHWH will bring on that land everything written in this book — the self-referential note signals that the Book of Jeremiah is itself a covenantal document, its words carrying the weight of treaty stipulations that will be enforced.</p>",
    "14": "<p>Many nations and great kings will make servants of Babylon — YHWH will repay (<em>shillamti</em>) Babylon according to its deeds. The lex talionis principle: the enslaver will be enslaved; the nation that made others serve will itself serve. Cf. Jer 50:29 and Rev 18:6.</p>",
    "15": "<p><strong>כּוֹס הַיַּיִן הַחֵמָה</strong> (<em>kos hayyayin hachemmah</em>, the cup of the wine of wrath): <em>kos</em> (cup) is a powerful covenant metaphor — the cup can be a cup of salvation (Ps 116:13) or a cup of wrath. <em>Chemmah</em> (wrath/heat/poison) makes this the latter: YHWH's measured judgment poured out as a drink. The cup-of-wrath motif becomes central to NT Christology: Jesus drinks this cup at Gethsemane (Luke 22:42); Revelation 14:10 and 16:19 apply it to eschatological judgment.</p>",
    "16": "<p>The nations who drink the cup will stagger (<em>vega'ashu</em>) and be driven out of their minds (<em>vehit-holelu</em>) because of the sword YHWH sends among them. The drunkenness-of-judgment image links to the wineskin parable of ch 13 — the nations are filled with YHWH's wrath as wineskins filled with wine.</p>",
    "17": "<p>Jeremiah takes the cup from YHWH's hand and makes all the nations drink — the prophet's role as the divine instrument who delivers the cup of judgment. The listing of nations follows (vv18-26), culminating with Babylon itself (v26), showing that no empire is exempt from the cup.</p>",
    "18": "<p>Jerusalem and the cities of Judah are the first to drink — YHWH's judgment begins with his own household (cf. 1 Pet 4:17: 'judgment begins with the household of God'). This is not a contradiction of YHWH's love for Israel but a confirmation of covenant accountability — those who know the most bear the greatest responsibility.</p>",
    "19": "<p>Pharaoh king of Egypt and his servants — Egypt, the power from which Israel was delivered, is also subject to the cup. No previous relationship with YHWH exempts a nation from judgment; Egypt's past role as exodus-context does not shield it.</p>",
    "20": "<p>The land of Uz and the kings of Philistia — Uz is Job's homeland (Job 1:1), suggesting even that region of ancient wisdom falls under the cup. The Philistine cities (Ashkelon, Gaza, Ekron, Ashdod) are specific; this is the historical geography of Canaan's covenant territory.</p>",
    "21": "<p>Edom, Moab, Ammon — Israel's neighboring kinship nations (descendants of Esau and Lot) are included; kinship to Israel provides no exemption from the judgment. All the Transjordanian nations drink the cup.</p>",
    "22": "<p>The kings of Tyre, Sidon, and the coastland islands — the Phoenician maritime powers who controlled Mediterranean trade. Their wealth and seafaring power is no protection against the cup of YHWH's wrath.</p>",
    "23": "<p>Dedan, Tema, Buz, and all who cut the corners of their hair (<em>qotzei pe'ah</em>) — the Arab tribes who practiced this specific hair-cutting rite (also mentioned in 9:26 and 49:32); Jeremiah includes even the remote desert peoples in the universal scope of judgment.</p>",
    "24": "<p>All the kings of Arabia and the mixed peoples (<em>ha'erev</em>) who live in the desert — the totality of the Arabian Peninsula's populations. The list keeps extending to encompass all known peoples.</p>",
    "25": "<p>Zimri, Elam, and the Medes — eastern nations beyond Mesopotamia. Elam will receive its own oracle in ch 49; the Medes will be the instruments of Babylon's fall (50:41-43; Isa 13:17-19). Their current inclusion in the cup anticipates their later role.</p>",
    "26": "<p><strong>שֵׁשַׁךְ</strong> (<em>Sheshakh</em>) — a cryptogram (atbash: sh-sh-k = b-b-l in reversed Hebrew alphabet) for Babylon (<em>Bavel</em>). Babylon drinks the cup last — the nation that administers judgment is itself not exempt. The cup returns to its source. Cf. Rev 18:6.</p>",
    "27": "<p><strong>שְׁתוּ וְשִׁכְרוּ וְקִיאוּ</strong> (<em>shetu veshikru vekiy'u</em>, drink, get drunk, vomit): the physical degradation of the nations under divine judgment — not a dignified defeat but a shameful collapse. The sword (<em>cherev</em>) that YHWH is sending among them follows.</p>",
    "28": "<p>If they refuse to take the cup from your hand to drink — they will still drink: <strong>שָׁתֹה תִשְׁתּוּ</strong> (<em>shato tishthu</em>): the emphatic infinitive absolute — you will certainly drink. Refusal is not an option; the covenant judgment is not negotiable.</p>",
    "29": "<p><strong>הָעִיר אֲשֶׁר נִקְרָא שְׁמִי עָלֶיהָ</strong> (<em>ha'ir asher niqra shemi aleha</em>, the city that bears my name): Jerusalem — the city of YHWH's name. YHWH begins with his own name-city; if Jerusalem is not exempt, how can any other city expect exemption? The rhetorical force: the cup is universal because YHWH is the universal judge.</p>",
    "30": "<p><strong>יִשְׁאַג</strong> (<em>yish'ag</em>, he will roar): YHWH roaring from his holy dwelling (<em>me'on qodsho</em>) like a lion over his pasture — the lion is no longer the animal Israel feared from the Jordan thickets (12:8) but YHWH himself. <strong>הֵידָד כְּדֹרְכִים יַעֲנֶה</strong> (<em>heydad kedorkheim ya'aneh</em>, shouting like those who tread the grapes): YHWH's voice over the earth like the harvest shout — judgment is the harvest of what Israel and the nations have sown.</p>",
    "31": "<p><strong>בָּא שָׁאוֹן עַד-קְצֵה הָאָרֶץ</strong> (<em>ba sha'on ad-qetzeh ha'aretz</em>, a din reaches the ends of the earth): the cosmic scope of judgment — the whole earth is in the range of YHWH's court case (<em>riv</em>). YHWH has an indictment against all flesh; the wicked will be given to the sword.</p>",
    "32": "<p>Disaster is spreading from nation to nation — <strong>מִיַּרְכְּתֵי הָאָרֶץ</strong> (<em>miyarketey ha'aretz</em>, from the ends/farthest parts of the earth): the judgment is not localized but global in its sweep. The great storm (<em>sa'ar gadol</em>) is rising from the ends of the earth.</p>",
    "33": "<p>The slain of YHWH on that day will cover the face of the whole earth — <strong>מִקְצֵה הָאָרֶץ וְעַד-קְצֵהוּ</strong> (<em>miqtzeh ha'aretz ve'ad-qetzehu</em>, from one end of the earth to the other). They will not be mourned, gathered, or buried — dung (<em>domen</em>) on the face of the ground. The dishonor of unburied death is a covenant curse (Deut 28:26).</p>",
    "34": "<p><strong>הֵילִילוּ הָרֹעִים</strong> (<em>heililu haro'im</em>, wail, you shepherds): the <em>ro'im</em> (shepherds/rulers) are commanded to wail because their days of slaughter and scattering are coming. The leaders who failed their flocks will be first to mourn.</p>",
    "35": "<p><strong>וְאָבַד מָנוֹס מִן-הָרֹעִים</strong> (<em>ve'avad manos min-haro'im</em>, flight will perish from the shepherds): no escape for the leaders who scattered the flock. The usual options of flight and survival are cut off — covenant judgment is inescapable for those who bore the highest responsibility.</p>",
    "36": "<p><strong>קוֹל צַעֲקַת הָרֹעִים וִילְלַת אַדִּירֵי הַצֹּאן</strong> (<em>qol tza'aqat haro'im viylalat addire hatzzon</em>, sound of the cry of the shepherds and the wailing of the leaders of the flock): the lamentation of the ruling class. YHWH is ruining (<em>shochet</em>) their pasture because of the fierce anger of the oppressor.</p>",
    "37": "<p>The peaceful meadows (<em>nevot hashalom</em>) are devastated because of YHWH's fierce anger. The covenant blessing of peaceful pastures (Ps 23; Ezek 34:14-15) is reversed: the anger that should bring rain and abundance brings desolation.</p>",
    "38": "<p><strong>עָזַב כַּכְּפִיר סֻכֹּה</strong> (<em>azav kakfir sukkoh</em>, he has left his den like a young lion): YHWH has left his divine dwelling to come in judgment — a terrifying reversal. When YHWH dwells in Zion, his presence is protection; when he departs and comes against the nations, it is destruction. The land is made a desolation because of the oppressor's sword and YHWH's fierce anger (<em>charon apo</em>).</p>"
  },
  "26": {
    "1": "<p>Another precise date: the beginning of the reign (<em>bereshit mamlekhet</em>) of Jehoiakim — this places the temple sermon early in Jehoiakim's reign (608-607 BCE), providing the historical context that ch 7 (the sermon itself) lacks. The narrator preserves the context of what must have been a life-threatening crisis for Jeremiah.</p>",
    "2": "<p><strong>עֲמֹד בַּחֲצַר בֵּית-יְהוָה</strong> (<em>amod bachatzar beit-YHWH</em>, stand in the court of YHWH's house): Jeremiah is instructed to speak in the most public sacred space — the outer court where all who come to worship can hear. The message is not for a private audience but for maximum public impact. <strong>אַל-תִּגְרַע דָּבָר</strong> (<em>al-tigra' davar</em>, do not hold back a word): prophetic integrity requires complete disclosure, even when the message is dangerous.</p>",
    "3": "<p>Perhaps (<em>ulay</em>) they will listen and turn (<em>yashuvhu</em>) — the conditional clause preserves genuine human freedom while announcing inevitable judgment. YHWH does not pronounce the outcome as predetermined; the possibility of repentance is real. <strong>נִחַמְתִּי</strong> (<em>nichamti</em>, I will relent): YHWH's repentance/change of mind is real — cf. Jonah 3:9-10 (God relented from the disaster he had threatened Nineveh).</p>",
    "4": "<p>If you do not listen to walk in my law (<em>torati</em>) — the covenant condition restated with Deuteronomic vocabulary. The prophets are sent as the covenant's enforcement mechanism; ignoring them = ignoring the covenant terms.</p>",
    "5": "<p>My servants the prophets (<em>avadai haneviim</em>) — the prophets are again YHWH's servants, sent persistently and urgently (rising early, v4). But you have not listened — the same indictment as ch 25:4.</p>",
    "6": "<p><strong>שִׁלֹה</strong> (<em>Shiloh</em>) as the precedent: the first sanctuary where the ark was kept (Josh 18:1; 1 Sam 1-4) was destroyed. Shiloh's destruction (ca. 1050 BCE, though the timing is debated) is Jeremiah's proof that YHWH will destroy his own sanctuary if covenant-keeping fails. The threat is not empty rhetoric — there is historical precedent. Cf. Ps 78:60.</p>",
    "7": "<p>The priests, prophets, and all the people heard Jeremiah — the full spectrum of religious leadership. Their hearing sets up the trial: they are witnesses to what was said, and their subsequent judgment will reveal whether they comprehend YHWH's word or defend their own institutional interests.</p>",
    "8": "<p>As soon as Jeremiah finished speaking, the priests and prophets seized him (<em>yakhaziqu bo</em>) saying: 'You must die!' (<em>mot tamut</em>): the infinitive absolute of death — the same formula used in death-penalty declarations. The institutional religious leadership responds with violence when their security is threatened.</p>",
    "9": "<p>Why have you prophesied in YHWH's name saying this house will become like Shiloh? — the charge is not false prophecy (they don't address truth) but institutional blasphemy against the temple. The people massed against Jeremiah (<em>vayiqahel kol-ha'am</em>) — a crowd becomes a mob.</p>",
    "10": "<p>The officials of Judah come up from the king's house to the temple — the civil leadership enters as a higher court. The trial moves from religious to civil authority, reflecting the institutional complexity of the crisis.</p>",
    "11": "<p>The priests and prophets speak to the officials and all the people: 'This man deserves the death penalty' (<em>mishpat mavet la'ish hazeh</em>) — a formal legal verdict. The accusation: he has prophesied against this city as you have heard with your own ears. The charge conflates the prophet's message with an attack on the institution.</p>",
    "12": "<p>Jeremiah's defense: <strong>יְהוָה שְׁלָחַנִי</strong> (<em>YHWH shelachani</em>, YHWH sent me) — the authority claim. The divine commission is the basis of prophetic immunity; killing the prophet is killing YHWH's messenger. The defense is Christological in its structure: the sent one's authority derives entirely from the sender.</p>",
    "13": "<p>Now amend your ways (<em>hatzivu darkeykhem</em>) and deeds (<em>ma'alelekhem</em>) and obey the voice of YHWH your God — the prophetic appeal is still open even at the moment of threatened execution. Jeremiah preaches while on trial for his life; YHWH may relent.</p>",
    "14": "<p><strong>הִנְנִי בְיֶדְכֶם</strong> (<em>hineni beydekhem</em>, I am in your hands): Jeremiah submits to their jurisdiction — he does not claim prophetic immunity from civil process. Do to me what seems good and right to you. The passive acceptance of possible death mirrors a pattern: the servant who delivers YHWH's word trusts YHWH with the outcome.</p>",
    "15": "<p><strong>דַּם נָקִי</strong> (<em>dam naqi</em>, innocent blood): the legal category — executing Jeremiah would bring innocent blood on the city and its inhabitants, on YHWH himself (<em>al nafshoteykhem ve'al ha'ir hazot</em>). In covenant law, shedding innocent blood defiles the land (Num 35:33-34). The prophets who plotted against Jeremiah in Anathoth (ch 11) were seeking to shed innocent blood.</p>",
    "16": "<p>The officials and all the people to the priests and prophets: 'This man does not deserve the death penalty — he has spoken to us in the name of YHWH our God.' The civil officials recognize the distinction between institutional threat and genuine prophetic authority; they acquit.</p>",
    "17": "<p>Some of the elders of the land (<em>ziqnei ha'aretz</em>) rose to speak — the elders invoked as historical witnesses. They provide the precedent that Jeremiah's message is not unprecedented or deserving of death; it follows the pattern of true prophecy.</p>",
    "18": "<p><strong>מִיכָה הַמֹּרַשְׁתִּי</strong> (<em>Mikhah hamMorashthi</em>, Micah of Moresheth): Micah the prophet (Mic 3:12) is cited as a legal precedent — his contemporary was Hezekiah. <strong>צִיּוֹן שָׂדֶה תֵחָרֵשׁ</strong> (<em>Tzyon sadeh techaresh</em>, Zion will be plowed as a field): Micah's exact words (Mic 3:12) are quoted — the memory of prophetic words was preserved and invoked as legal precedent generations later.</p>",
    "19": "<p>Did Hezekiah put Micah to death? — the rhetorical historical question. Hezekiah feared YHWH (<em>yare' et-YHWH</em>) and sought (<em>vayechal</em>) his favor — the king's appropriate response to prophetic warning. And YHWH relented (<em>vayyinnachem</em>) of the disaster announced. The precedent proves: repentance is possible, killing prophets is wrong, and YHWH responds to genuine fear of him.</p>",
    "20": "<p>The case of Uriah son of Shemaiah — a contemporary prophet who also prophesied against Jerusalem and Judah. He fled to Egypt when Jehoiakim sought to kill him — the contrast with Jeremiah who stayed.</p>",
    "21": "<p>Jehoiakim sent men to Egypt — Elnathan son of Achbor and others — who brought Uriah back from Egypt. The international reach of royal power to silence prophets demonstrates the danger Jeremiah faced.</p>",
    "22": "<p>They brought Uriah from Egypt and presented him to King Jehoiakim, who killed him with the sword — the executive execution of a prophet. The contrast with Jeremiah is stark: same message, similar threat, different outcomes. Providence rather than merit determines survival.</p>",
    "23": "<p>His body was thrown into the burial place of the common people (<em>qivrei benei ha'am</em>) — a dishonorable burial that adds shame to death. The contrast: Jeremiah is preserved to fulfill his calling; Uriah's death is a warning of what prophets risked.</p>",
    "24": "<p><strong>אֲחִיקָם בֶּן-שָׁפָן</strong> (<em>Achiqam ben-Shaphan</em>, Ahikam son of Shaphan): the Shaphan family were consistent supporters of both Josiah's reform and Jeremiah. Ahikam's protection (<em>lo natan oto beyad ha'am lehammito</em>, he did not give him into the hand of the people to put him to death) was decisive. Providence working through covenant-faithful individuals preserves the prophet for his mission.</p>"
  },
  "27": {
    "1": "<p>The beginning of Zedekiah's reign — the textual note in brackets in many translations (the MT has 'Jehoiakim' but the chapter clearly concerns Zedekiah, a scribal error corrected in most manuscripts). The yoke sign-act is placed in a critical early moment of Zedekiah's reign.</p>",
    "2": "<p><strong>עֲשֵׂה לְךָ מֹוסֵרוֹת וּמֹטוֹת</strong> (<em>aseh lekha moserot umottot</em>, make for yourself bonds and yoke-bars): the yoke-components — <em>moserot</em> are the leather straps/thongs that secure the yoke to the animal's neck; <em>mottot</em> are the wooden crossbars of the yoke. The complete physical apparatus of agricultural servitude becomes a walking prophetic symbol.</p>",
    "3": "<p>Send the yoke to the ambassadors of Edom, Moab, Ammon, Tyre, and Sidon — the nations whose envoys were gathered in Jerusalem, presumably forming a coalition against Babylon. Jeremiah disrupts the diplomatic conference with YHWH's counterword: submit, do not resist.</p>",
    "4": "<p>The message to their masters: This is what YHWH of armies, the God of Israel, says to you — the universal divine title. The nations are addressed as subjects of YHWH's word even though they are not Israel's covenant partners; YHWH's sovereignty is total.</p>",
    "5": "<p><strong>אָנֹכִי עָשִׂיתִי אֶת-הָאָרֶץ</strong> (<em>anokhi asiti et-ha'aretz</em>, I made the earth): the creation sovereignty claim grounds the political claim. Because YHWH made the earth, the people, and the animals by his great power and outstretched arm (<em>zeroa netuyah</em>), he has the absolute right to assign ownership to whoever seems good to him (<em>lakol asher yashar be'einav</em>). The political theology of sovereignty: Creator = Owner = Sovereign over all political arrangements.</p>",
    "6": "<p><strong>עַבְדִּי</strong> (<em>avdi</em>, my servant): Nebuchadnezzar king of Babylon is again called YHWH's servant — the title appears twice (here and ch 25:9). Even the wild animals (<em>chayyot hassadeh</em>) are given to him to serve him. The cosmic servitude of nature to YHWH's appointed ruler is a creation-theology claim.</p>",
    "7": "<p>All nations (<em>kol-hagoyim</em>) will serve him — his son and his grandson — until the time (<em>ad bo et yomo</em>, until his time comes): a bounded sovereignty. The Babylonian empire is not permanent but has a YHWH-appointed duration. Then many nations and great kings will make him serve them — Babylon will be enslaved as it enslaved others.</p>",
    "8": "<p>The nation or kingdom that does not serve Nebuchadnezzar king of Babylon and does not put its neck under his yoke (<em>mottoh</em>) — I will punish with sword, famine, and pestilence (<em>cherev, ra'av, vaDever</em>). Resistance to YHWH's appointed instrument is resistance to YHWH himself; the covenant-curse triad returns.</p>",
    "9": "<p><strong>אַל-תִּשְׁמְעוּ אֶל-נְבִיאֵיכֶם</strong> (<em>al-tishme'u el-nevieyekhem</em>, do not listen to your prophets): followed by a list of false guidance-sources — <strong>קֹסְמֵיכֶם</strong> (<em>qosmeykhem</em>, your diviners), <strong>חֹלְמֵיכֶם</strong> (<em>cholmeykhem</em>, your dreamers), <strong>עֹנְנֵיכֶם</strong> (<em>onneykhem</em>, your soothsayers/cloud-readers), <strong>כַּשָּׁפֵיכֶם</strong> (<em>kashafeykhem</em>, your sorcerers). The full spectrum of divination practices condemned in Deut 18:10-12. These are the sources that say: 'You will not serve the king of Babylon' — but they lie.</p>",
    "10": "<p>They prophesy a lie (<em>sheqer</em>) to you — the false prophets promise what the people want to hear. The outcome of following false prophecy: removal (<em>harchiqenu</em>) from your land and expulsion in exile and perishing. Ironically, the prophecies meant to give security produce the catastrophe they promised to prevent.</p>",
    "11": "<p>But the nation that puts its neck under the yoke of the king of Babylon and serves him — I will leave it in its own land (<em>vehinachtihu al-admatoh</em>). The paradox of submission-as-survival: accepting the yoke is the path to staying in the land; resisting it leads to exile. This theological logic is exactly the kind of counter-intuitive message that got prophets killed.</p>",
    "12": "<p>Jeremiah speaks the same words to Zedekiah king of Judah: bring your necks under the yoke of the king of Babylon, serve him and his people, and you will live. The personal application of the prophetic word to the king — the message is not general but specific to the moment of decision Zedekiah faces.</p>",
    "13": "<p>Why should you and your people die by sword, famine, and pestilence (<em>cherev vera'av vedaver</em>) as YHWH has said about the nation that will not serve the king of Babylon? The rhetorical question exposes the self-destructiveness of the false-prophecy choice.</p>",
    "14": "<p><strong>אַל-תִּשְׁמְעוּ אֶל-דִּבְרֵי הַנְּבִיאִים</strong> (<em>al-tishme'u el-divrei haneviim</em>, do not listen to the words of the prophets): the false prophets tell you that you will not serve the king of Babylon — <strong>שֶׁקֶר הֵם נִבְּאִים לָכֶם</strong> (<em>sheqer hem nib'im lakhem</em>, they are prophesying falsehood to you).</p>",
    "15": "<p><strong>לֹא שְׁלַחְתִּים</strong> (<em>lo shelachtim</em>, I have not sent them): the diagnostic of false prophecy — the false prophet cannot demonstrate a divine commission. They prophesy in YHWH's name (<em>bishmi</em>) without YHWH's authorization. The result: I will drive you out and you will perish — both the prophets and those who believe them.</p>",
    "16": "<p>Jeremiah speaks to the priests and all the people: do not listen to the prophets who say the vessels of YHWH's house (<em>kelei beit-YHWH</em>) will soon be brought back from Babylon. <strong>שֶׁקֶר הֵם נִבְּאִים לָכֶם</strong> (<em>sheqer hem nib'im lakhem</em>, they are prophesying falsehood to you) — the repeated verdict.</p>",
    "17": "<p>Do not listen to them — serve the king of Babylon and live (<em>ichyu</em>). Why should this city become a desolation (<em>chorbah</em>)? The logic of prophetic pragmatism: not theological surrender but realistic assessment of what YHWH has determined.</p>",
    "18": "<p>But if they are prophets and if the word of YHWH is with them, let them intercede (<em>yifge'u na</em>) with YHWH of armies that the vessels remaining in the house of YHWH not go to Babylon — a challenge to the false prophets. If they have genuine prophetic access to YHWH, let them pray effectively. Their inability to prevent the remaining vessels from being taken proves their falsehood.</p>",
    "19": "<p>The specific vessels remaining — the bronze pillars (<em>ha'amudim</em>), the sea (<em>hayyam</em>), the stands (<em>hamkhaonot</em>), and the other vessels: the great ceremonial objects of the Solomonic temple. Their fate is being contested between true and false prophecy.</p>",
    "20": "<p>Nebuchadnezzar king of Babylon did not take them when he took Jeconiah son of Jehoiakim of Judah into exile from Jerusalem to Babylon — a historical note. The first deportation (597 BCE) included people but not all the temple vessels.</p>",
    "21": "<p>Thus says YHWH of armies, the God of Israel, concerning the vessels remaining in the house of YHWH, in the house of the king of Judah, and in Jerusalem — YHWH addresses specifically the objects of false prophecy's hopeful claims.</p>",
    "22": "<p><strong>בָּבֶלָה יוּבָאוּ וְשָׁמָּה יִהְיוּ</strong> (<em>Vavelah yuba'u veshammah yihyu</em>, they will be brought to Babylon and there they will remain): YHWH's counter-prophecy to the false prophets. The vessels will go to Babylon. But: <strong>עַד יוֹם פָּקְדִי אֹתָם</strong> (<em>ad yom poqdi otam</em>, until the day I attend to them) — a bounded removal, not permanent loss. YHWH will bring them back — the same pattern as the exile of people: bounded by YHWH's purposes, not open-ended. Cf. Ezra 1:7-11 (Cyrus restores the temple vessels).</p>"
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
