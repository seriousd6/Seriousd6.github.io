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
  "39": {
    "1": "<p>The resumption formula <em>ve'atah ben-adam hinabu al-Gog</em> (and you, son of man, prophesy against Gog) reopens the oracle of ch. 38. The two-chapter unit (38-39) forms the great Gog oracle — Ezekiel's eschatological battle text. Chapter 38 announced the invasion; chapter 39 describes YHWH's destruction of Gog and its theological aftermath. <em>Rosh nasi Meshech veTuval</em> (chief prince of Meshech and Tubal) — <em>rosh</em> here is a title (chief/head), not the country Russia (a common anachronistic misreading; the connection to Russia comes from 19th-century exegetes reading <em>Rosh</em> as a proper name).</p>",
    "2": "<p><strong>veshivvathicha veshishethicha</strong>: 'I will turn you back and lead you on.' The Hebrew roots here are debated: <em>shavah</em> can mean 'to turn back' or 'to lead,' and <em>shashah</em> can mean 'to lead' or 'to pull along by a hook' (cf. 38:4 where YHWH puts hooks in Gog's jaws). The MKT renders both verbs actively — YHWH is the agent who drives Gog forward to Israel's mountains. The crucial theological point is that Gog's invasion is not successful enemy initiative but YHWH's own deployment of an enemy instrument, as with Assyria in Isa 10:5-6.</p>",
    "3": "<p><strong>vehikeithi qashtech miyad semolecha</strong>: 'I will strike your bow from your left hand.' Military disarmament by divine action — the bow (<em>qashet</em>) from the left hand and arrows (<em>chitzim</em>) from the right hand. Archery was the dominant long-range weapon of ancient Near Eastern warfare. YHWH's direct action against Gog's weapons mirrors the exodus tradition: he fights for Israel, not Israel fighting for itself. The stripping of weapons prefigures the subsequent burning of those weapons by Israel over seven years (v. 9-10).</p>",
    "4": "<p><strong>al-harei Yisrael tipol atah vechal-agapeicha</strong>: 'On the mountains of Israel you will fall, you and all your troops.' The mountains of Israel (<em>harei Yisrael</em>) is a recurring Ezekielian location that appears in both judgment oracles against Israel (ch. 6) and salvation oracles for Israel (ch. 36). Gog falls in Israel's own land — judgment executed where the enemy had anticipated victory. <em>Lefzit qin'ah</em> (to the birds of prey of every kind) — the feeding of enemies to birds and beasts is the reversal of proper burial, a form of judgment that denies the defeated the dignity of covenant burial (cf. Deut 28:26).</p>",
    "5": "<p><strong>al-penei hasadeh tipol</strong>: 'You will fall in the open field.' The <em>sadeh</em> (open field, countryside) burial-denial formula is sealed with <em>ki ani dibarti ne'um adonai YHWH</em> (for I have spoken, declares the Lord YHWH). Ezekiel's characteristic concluding formula makes the divine speech itself the guarantee of the outcome — not military analysis or political prediction but the performative word of YHWH that accomplishes what it announces.</p>",
    "6": "<p><strong>veshilachti esh beMagog</strong>: 'I will send fire on Magog.' The judgment extends beyond Gog's army to Magog (the homeland) and the coastlands (<em>iyyim</em>) that &ldquo;dwell in security.&rdquo; <em>Esh</em> (fire) as the instrument of judgment is YHWH's characteristic weapon (Isa 30:30; Amos 1-2; Rev 20:9). The recognition formula <em>veyad'u ki ani YHWH</em> (they will know that I am YHWH) extends to the nations: the Gog defeat is not just Israel's salvation but a universal theophany that makes YHWH known among all peoples.</p>",
    "7": "<p><strong>ve'et-shem qodshi odiya bekerev ami Yisrael</strong>: 'I will make my holy name known in the midst of my people Israel.' <em>Shem qodshi</em> (my holy name) is the theological center of the Gog oracle and of Ezekiel's entire theology: YHWH's purpose is the vindication of his name among nations (cf. 36:20-23, where Israel's exile had profaned YHWH's name among the nations). The Gog defeat is the eschatological event that restores YHWH's reputation — the nations will know that Israel's exile was not YHWH's defeat but his judgment, and Israel's restoration is his power. <em>Lo akhallel et-shem qodshi od</em> (I will not let my holy name be profaned anymore) — the permanent securing of the divine honor.</p>",
    "8": "<p><strong>hineh baat umayom asher dibarti</strong>: 'Behold it is coming and it will happen, declares the Lord YHWH. This is the day of which I have spoken.' <em>Ba'ah</em> (it is coming) as perfect tense — prophetic certainty. The phrase <em>zeh hayom asher dibarti</em> (this is the day of which I have spoken) connects the Gog oracle to YHWH's prior speech — possibly to the restoration oracles of chs. 34-37 or to the foundational threat oracles of chs. 4-24. The day is singular — <em>hayom</em> — but it encompasses the eschatological event Ezekiel has been building toward.</p>",
    "9": "<p><strong>veyatze'u yoshevei arei Yisrael uviy'aru vehissiqu bensheq</strong>: 'Those who dwell in the cities of Israel will go out and make fires of the weapons.' The burning of weapons for seven years (<em>sheva shanim</em>) is the practical consequence of total military victory. <em>Magen vetzinnah qeshet vachitzim umes madanot varomach</em> — the weapon list (shields, bucklers, bow, arrows, war clubs, spears) represents the complete arsenal of ancient Near Eastern warfare. Using enemy weapons as fuel rather than importing wood from the forest is a sign of the complete sufficiency of the victory — the defeated enemy's equipment meets all of Israel's energy needs.</p>",
    "10": "<p><strong>lo yis'u etzim min-hasadeh</strong>: 'They shall not carry wood from the field.' The fuel self-sufficiency of vv. 9-10 has a symbolic dimension beyond practicality: Israel does not need to go out to the territory (<em>sadeh</em>) where enemies dwell to gather their sustenance. The plundering of those who plundered them and the spoiling of those who spoiled them (<em>veshaleloo et-sholeheihem ve'vezzoo et-bozezehem</em>) is the classic prophetic reversal — exact recompense through divine governance of history.</p>",
    "11": "<p><strong>venathati leGog makom sham qever beYisrael</strong>: 'I will give Gog a burial place there in Israel.' <em>Gei ha-avarim</em> (Valley of the Travelers/Passers-by) — the name is debated: <em>avarim</em> can mean &ldquo;those who pass through&rdquo; (common travelers) or is related to the Abarim mountains in Transjordan (Num 27:12; Deut 32:49). The MKT renders it 'travelers' following the contextual use. The renamed valley <em>Gei Hamon-Gog</em> (Valley of the Multitude of Gog) commemorates permanently the scale of YHWH's victory. The nose-blocking of the passers-by (<em>ve'gosemeth et-avar ha-avarim</em>) indicates an enormous stench from the mass of corpses.</p>",
    "12": "<p><strong>uvekabram otam beit Yisrael</strong>: 'The house of Israel will be burying them.' Seven months (<em>shiva chodeshim</em>) of burial is the temporal counterpart to the seven years of weapon-burning (v. 9) — the number seven in both cases signals completeness. The extended burial process communicates the scale of Gog's defeat but also the thoroughness of the land's cleansing: Israel must actively participate in removing all traces of the hostile army from the land of covenant blessing.</p>",
    "13": "<p><strong>vekabru kol-am haarets</strong>: 'All the people of the land will bury them.' The communal burial is characterized as a source of honor (<em>ve'hayah lahem leshem</em> = it will be to them a name/renown) in the day YHWH glorifies himself (<em>beyom hikavedi</em>). The burying of the enemy is not merely hygienic but theological — it is participation in YHWH's great act of vindication. The phrase <em>beyom hikavedi</em> (on the day I am glorified/honored) connects the burial directly to the <em>kavod</em> (glory) theme that runs through Ezekiel's theology.</p>",
    "14": "<p><strong>va'anshei tamid yavdilu oveerei baaretz</strong>: 'Men shall be set apart, regularly employed to pass through the land.' <em>Anshei tamid</em> (men of continualness/regularity) — a specialized burial detail (<em>mekabrim</em>) whose continual task is to search the land for remaining bones. The thoroughness of the land-cleansing operation emphasizes that even scattered and forgotten bones must be located. The passage of seven months was not sufficient — a dedicated professional corps is needed for the final purification.</p>",
    "15": "<p><strong>verau etzem adam</strong>: 'And when any one sees a human bone.' The wayfarer who sees a bone sets up a marker (<em>tziyyun</em> = a road marker, sign) beside it so that the burial detail can find it. This is the ancient equivalent of a danger marker and collection protocol. The systematic nature of the cleanup — specialized workers, markers, final collection — communicates that land defilement by unburied corpses (cf. Num 19:16) has cosmic importance: the land must be ritually pure for the divine presence to return (chs. 40-48).</p>",
    "16": "<p><strong>vegam shem-ir Hamonah</strong>: 'And the name of the city will also be Hamonah.' <em>Hamonah</em> (multitude, horde) is the city near the burial valley that will bear the name as a permanent memorial of YHWH's victory. The naming of both the valley (Hamon-gog, v. 11) and the city (Hamonah) permanently commemorates the defeat — the landscape itself becomes memorial testimony. This anticipates the eschatological transformation of place-names in Ezekiel's vision (44:35: Jerusalem named &ldquo;YHWH is There&rdquo;).</p>",
    "17": "<p><strong>ve'atah ben-adam koh amar adonai YHWH emor letzipor kol-kanaf</strong>: 'And you, son of man, thus says the Lord YHWH: Speak to every winged bird.' The summoning of birds and beasts to the sacrificial feast on Gog's corpses is deliberately described as a <em>zevach</em> (sacrifice) and a <em>mishteh</em> (feast/drinking party). The feast on the mighty and their horses (v. 18-20) is the inverse of the covenant sacrificial feast — instead of Israel feasting on covenant blessing, the creation feasts on covenant-enemy. Revelation 19:17-18 quotes this passage for the eschatological battle's aftermath.</p>",
    "18": "<p><strong>bashar gibborim tochelu vedam nesiayei haaretz tishteh</strong>: 'You will eat the flesh of mighty men and drink the blood of princes.' The specifics — <em>alim</em> (rams), <em>karim</em> (lambs), <em>attudim</em> (he-goats), <em>parim</em> (bulls) — use sacrificial animal terminology metaphorically for human rulers and warriors. The princes (<em>nesiyim</em>), mighty men (<em>gibborim</em>), and their forces are the &ldquo;animals&rdquo; at this inverted feast. The drinking of blood — normally the ultimate dietary prohibition in Israel (Lev 17:14) — here applied to birds and beasts signals that this feast is outside all normal categories: it is YHWH's own slaughter-feast.</p>",
    "19": "<p><strong>va'akaltem chelev lesova</strong>: 'You will eat fat until you are satisfied.' The three words — <em>chelev</em> (fat, the richest portions), <em>lesova</em> (to satiety/fullness), <em>ve'shatem dam lishkarah</em> (and drink blood to drunkenness) — are the language of excessive feasting. The irony is that the fat and blood — both reserved for YHWH in the sacrificial system (Lev 3:16-17) — are here given to creation's scavengers, because this feast is YHWH's own judgment-sacrifice in which the enemy army is the animal offering.</p>",
    "20": "<p><strong>usevitem al-shulchani</strong>: 'You will be filled at my table.' YHWH's table (<em>shulchani</em>) at which birds and beasts feast is the judgment-altar's counterpart to the sanctuary table (the table of the Presence). The complete military taxonomy — horses, riders, mighty men, warriors — confirms the universality of the judgment: no component of Gog's force escapes. The recognition formula follows: <em>venathati et-kevodi bagoyim</em> (I will set my glory among the nations).</p>",
    "21": "<p><strong>venathati et-kevodi bagoyim</strong>: 'I will set my glory among the nations.' The <em>kavod</em> (glory) statement is the theological climax of the Gog narrative. YHWH's purpose throughout the oracle has been the universal recognition of his sovereign power — not merely Israelite vindication but cosmic theophany. <em>Vereyu kol-hagoyim et-mishpati</em> (all the nations will see my judgment) — the Gog battle is a public event visible to all peoples, establishing beyond doubt that YHWH governs history and judges those who challenge his covenant purposes.</p>",
    "22": "<p><strong>veyad'u beit Yisrael ki ani YHWH elohehem</strong>: 'And the house of Israel will know that I am YHWH their God.' The recognition formula is applied to Israel specifically here: <em>elohehem</em> (their God) adds the covenant dimension — not merely that YHWH exists or is powerful but that he is Israel's own covenant God who has acted on their behalf. The phrase <em>min-hayom hahu vema'alah</em> (from that day onward) signals that the Gog defeat produces a permanent change in Israel's covenant knowledge — no more forgetting, no more idol substitution.</p>",
    "23": "<p><strong>veyad'u hagoyim ki ba'avonam galu beit Yisrael</strong>: 'The nations will know that the house of Israel went into exile for their iniquity.' The theological explanation of the exile for the benefit of the nations: YHWH hid his face (<em>hisstarti panai</em>) not because he was weak but because Israel sinned (<em>be'avonam</em>). YHWH's hiding of his face was a judicial act, not a defeat. The nations' misunderstanding of the exile (assuming YHWH was powerless to prevent it) is now corrected by the restoration — they learn both why Israel was exiled and why YHWH is now acting for her.</p>",
    "24": "<p><strong>ketumatam uchefishehem asiti otam</strong>: 'According to their impurity and according to their transgressions I acted against them.' The theological vindication is precise: YHWH's action in exile was perfectly calibrated to Israel's sin. <em>Tuma</em> (impurity, ritual/ethical defilement) and <em>pasha</em> (transgression, covenant violation) are the two categories of Israel's failure. YHWH's judicial response was measured, not arbitrary or excessive. The nations can now see that the exile was proportionate divine justice, not random military misfortune.</p>",
    "25": "<p><strong>lachan koh amar adonai YHWH atah ashiv et-shevut Yaakov</strong>: 'Therefore thus says the Lord YHWH: Now I will restore the fortunes of Jacob.' The <em>lachan</em> (therefore) of restoration is the climactic reversal. <em>Shevut Yaakov</em> (the fortunes of Jacob) — the formula <em>shav shevut</em> signals the turning of captivity/fortune (it can mean both restoring from exile and reversing misfortune). The jealousy for YHWH's holy name (<em>qinati leshemi qodshi</em>) is the motivation — the same jealousy that motivated judgment (36:5-6) now motivates restoration. Divine jealousy is not petty but the covenant passion that drives both justice and redemption.</p>",
    "26": "<p><strong>venessu et-kelimmatam vekhol-ma'alam asher ma'alu vi</strong>: 'They will bear their shame and all their treachery with which they have been unfaithful to me.' The restored Israel will not be returned to complacency — they will bear (<em>nasa</em> = to carry, to forgive, to bear responsibility for) the memory of their shame. This is neither condemnation nor forgotten grace: the shame is borne in the context of security (<em>beshivtam al-admatam labetach</em> = dwelling securely on their land). Held shame in the context of security is the formative posture of those who have experienced grace they did not deserve.</p>",
    "27": "<p><strong>beshofeti otam beshivti et-shevutam</strong>: 'When I have gathered them from the peoples and gathered them from their enemies' lands.' The public <em>kiddush hashem</em> (sanctification of the divine name) executed before many nations — <em>venikdashti bam le'einei goyim rabbim</em> (I will manifest my holiness through them before many nations). The return of the exiles is itself a theophanic event: it declares to watching nations that YHWH is who he claimed to be. The restoration is not merely humanitarian but doxological — its purpose is the universal proclamation of YHWH's holiness.</p>",
    "28": "<p><strong>veyad'u ki ani YHWH elohehem begaloti otam el-hagoyim</strong>: 'They will know that I am YHWH their God — I who exiled them among the nations.' The theological conclusion states explicitly what the narrative has implied throughout: YHWH was the agent of both exile and restoration. The same God who exiled (<em>galoti otam</em> = I exiled them) now gathers (<em>vikibatzti otam al-admatam</em> = I gathered them to their land). Divine sovereignty governs both movements — the scattering and the ingathering are both YHWH's actions, which is the basis of hope. <em>Velo-otir od mehם</em> (and I left none of them behind) — complete restoration, not a remnant of a remnant.</p>",
    "29": "<p><strong>velo-astir od panai mehem</strong>: 'I will no longer hide my face from them.' The reversal of the judicial face-hiding (<em>hisstarti panai</em> of v. 23-24) is the ultimate restoration promise. <em>Asher shafachti et-ruachi al-beit Yisrael</em> (when I have poured out my Spirit on the house of Israel) — the Spirit-pouring is both the means and the sign of the restoration. The poured-out Spirit is the eschatological fulfillment that Joel 2:28-32 develops and Acts 2:17-21 applies to Pentecost. The final seal: <em>ne'um adonai YHWH</em> — the divine declaration that closes the great Gog oracle.</p>"
  },
  "40": {
    "1": "<p><strong>bechameish ve'esrim shanah legalutenu berosh hashanah be'asor lachodesh</strong>: 'In the twenty-fifth year of our exile, at the beginning of the year, on the tenth of the month.' The precise date anchors the vision in history: 25th year of exile = approximately 573 BCE, 14 years after Jerusalem's fall in 587 BCE. The tenth of the first month (Nisan/Abib) is Yom Kippur's preparation date — the same date on which the Passover lamb was selected (Exod 12:3). The coincidence is theologically weighted: a vision of the restored sanctuary comes on the day of paschal selection. <em>Yad YHWH hayah alai</em> (the hand of YHWH was upon me) — the prophetic inspiration formula indicating Ezekiel's transport into the vision.</p>",
    "2": "<p><strong>bemareh Elohim heviani el-eretz Yisrael</strong>: 'In divine visions he brought me to the land of Israel.' <em>Mareh Elohim</em> (divine visions, visions of God) — the phrase used for the inaugural vision in 1:1. Ezekiel is brought to <em>har gavoah meod</em> (a very high mountain) on whose south side (<em>negbah</em>) was something like a city structure (<em>kimivneh ir</em>). The high mountain of divine dwelling is the universal religious imagination realized in Israelite form: Sinai (Exod 19), Zion (Ps 48; Isa 2:2), Eden-mountain (Ezek 28:14). The approach from the south/negev is distinctive and may indicate the eschatological rebuilding of Jerusalem proper.</p>",
    "3": "<p><strong>vayavi otam shamah vehineh ish</strong>: 'He brought me there, and behold a man.' The guide-figure — whose appearance is <em>kemar'eh nehoshet</em> (like the appearance of bronze) — holds a <em>pethil pishta</em> (linen measuring cord) and a <em>qane hammidah</em> (measuring reed). The bronze appearance links this figure to the cherubim and the divine throne-chariot vision (1:7). The measuring instruments establish the vision's architecture as precise and divinely-specified — not symbolic approximation but exact divine plans for the restored sanctuary. John borrows this measuring-angel figure for Rev 21:15.</p>",
    "4": "<p><strong>ben-adam ree be'einekha ushema be'oznekha</strong>: 'Son of man, see with your eyes and hear with your ears.' The instruction to observe carefully (<em>sim libecha</em> = set your heart/attention to everything being shown) establishes the visionary program: Ezekiel is not merely a passive recipient but an active documenting witness. <em>Lema'an areh otcha hovaati henna</em> (for the purpose of showing you, I brought you here) — the vision has a communicative purpose. What Ezekiel sees and records becomes the specification for the future sanctuary — the architectural equivalent of Moses being shown the pattern on the mountain (Exod 25:9, 40).</p>",
    "5": "<p><strong>vehineh choma michutz labayit saviv saviv</strong>: 'And there was a wall all around on the outside of the temple complex.' The outer wall (<em>choma</em>) establishing the sacred precinct is measured at six cubits both in height and width — and crucially, the cubit used is <em>amah ve'topach</em> (a standard cubit plus a handbreadth), making it approximately 21 inches rather than the standard 18-inch cubit. The measurement standard is divinely specified, not inherited from prior human architectural practice. This establishes from the start that the sanctuary's dimensions are revelatory rather than conventional.</p>",
    "6": "<p><strong>vayavo el-sha'ar asher panav derech haqadim</strong>: 'He came to the gate that faces east.' The east-facing outer gate is the first structure measured. The east gate has particular significance: the glory of YHWH will re-enter through the east gate (43:1-4), and the gate will be shut after the glory enters (44:1-2) because YHWH has entered by it. The gate complex is measured systematically: the steps, the threshold, the guardrooms (<em>taha</em>), the gate posts, and the vestibule.</p>",
    "7": "<p><strong>vetaha echad amah achat aroch ve'amah achat rochav</strong>: 'Each guardroom was one cubit long and one cubit wide.' The <em>tahot</em> (guardrooms, niches, side chambers in the gatehouse) are each measured individually. The number three on each side (v. 10) creates a total of six guardrooms per gate — symmetrical design. The standardization of measurements throughout (each guardroom identical, each threshold the same) communicates divine order and perfection in the architectural plan: this is not a human builder's practical compromise but YHWH's ideal specification.</p>",
    "8": "<p><strong>vayamad et-ulam hasha'ar mibayit</strong>: 'He measured the vestibule of the gate from inside.' The inner vestibule (<em>ulam</em>) completes the gate complex measurement. The precision of the measurement vocabulary — threshold, jamb, vestibule, guardroom — reflects Ezekiel's priestly background: he knows temple architecture as a specialist and records the visionary temple in the technical language of his professional formation.</p>",
    "9": "<p><strong>vayamad et-ulam hasha'ar shmonah amot</strong>: 'He measured the vestibule of the gate: eight cubits.' The vestibule is eight cubits with pillars (<em>ayil</em>) of two cubits — the pillars flanking the vestibule entrance. The eight-cubit vestibule width versus the six-cubit guardrooms creates a progression: the entrance chambers become progressively larger as one moves deeper into the gate complex, corresponding to the increasing holiness of the inner zones. The architectural progression from common to holy is built into the spatial design.</p>",
    "10": "<p><strong>vetahot hasha'ar derech haqadim</strong>: 'The guardrooms of the east gate were three on each side.' The symmetric three-plus-three arrangement (six guardrooms total) with identical dimensions establishes the symmetrical perfection of the divine design. The uniformity of the guardrooms — <em>mida achat leshloshtam</em> (the same measure for all three) — communicates that the sanctuary is not the product of human aesthetic variation but the exact replication of a heavenly template (cf. the tabernacle pattern, Exod 25:40).</p>",
    "11": "<p><strong>vayamad et-rochav pethach hasha'ar</strong>: 'He measured the width of the gate passage.' The gate passage (<em>pethach hasha'ar</em>) is ten cubits wide; the total gate length is thirteen cubits. These proportions determine what kind of traffic (processions, individual worshipers) can pass through and the spatial experience of those entering. The precision of the measurement commentary — width, length, and specific elements — reflects the architectural vision's character: it is detailed enough to function as a building specification.</p>",
    "12": "<p><strong>vigvul lifnei hatahot amah achat</strong>: 'There was a barrier before the guardrooms, one cubit on each side.' The barriers (<em>gevul</em>) in front of the guardrooms are half-walls that define the niches. Each guardroom is six cubits square. This architectural vocabulary — guardroom, barrier, vestibule, threshold — represents the standard technical terminology for ancient Near Eastern gate complexes, and Ezekiel's use of it grounds the visionary temple in recognizable architectural categories while specifying dimensions that exceed historical temples.</p>",
    "13": "<p><strong>vayamad et-hasha'ar migag hataha el-gag tahav</strong>: 'He measured the gate from roof of guardroom to roof of guardroom.' The measurement from roof to roof (twenty-five cubits wide) establishes the total span of the gate complex. The gate houses (<em>tahot</em>) face each other across this span. The architectural precision communicates the vision's genre: this is not impressionistic symbolism but a scaled architectural plan, recorded with the specificity of a royal building specification.</p>",
    "14": "<p><strong>vaya'as el-ayilim shishim amah</strong>: 'He measured the pilasters at sixty cubits.' The <em>ayilim</em> (pilasters, projecting jambs) at sixty cubits represent the outer framework of the gate complex. The count given in the MT is disputed (LXX differs significantly in several measurements of ch. 40), suggesting either textual transmission difficulty or that both LXX and MT preserve different but authentic measurement traditions. The MKT follows the MT throughout.</p>",
    "15": "<p><strong>umipnei hasha'ar hamavo ad-lifnei ulam hasha'ar hapenimi</strong>: 'From the front of the entrance gate to the front of the vestibule of the inner gate was fifty cubits.' The distance of fifty cubits from exterior to interior vestibule establishes the depth of the gate complex. The number fifty resonates with Jubilee and covenant rest symbolism, though the architectural context likely makes this functional rather than deliberate numerical theology.</p>",
    "16": "<p><strong>vechaloni shutumim la-tahot ve'el-aylihem mitayit la-sha'ar saviv</strong>: 'And there were narrow windows in the guardrooms and in their pilasters all around on the inside of the gate.' <em>Chaloni shutumim</em> (narrow/shuttered windows) — windows designed to admit light while restricting external view, associated with sacred spaces (cf. 1 Kgs 6:4 for Solomon's temple). The palm trees (<em>timorot</em>) carved on the pilasters appear throughout the temple vision (chs. 40-41) and connect the sanctuary to Eden-imagery: palm trees as the lush vegetation of the divine garden (cf. 41:18-20).</p>",
    "17": "<p><strong>vayevi'eni el-hachazarah hachutzah</strong>: 'He brought me to the outer court.' The <em>chatzar hachitzonah</em> (outer court) has pavement (<em>ritzmah</em>) and thirty chambers (<em>lishkot</em>) arranged around the court. The pavement (<em>ritzmah</em>) is laid beside the gates on the lower level. The thirty chambers represent administrative and support functions — storage, priestly preparation, and perhaps areas for worshipers' use. The number thirty may echo the thirty shekels of priestly assessment (Num 18:16) or be purely architectural.</p>",
    "18": "<p><strong>vehartizmah el-tzad hasha'arim leumat orech hasha'arim</strong>: 'The pavement was beside the gates, corresponding to the length of the gates.' The outer court pavement flanks the gate complexes on their inner sides. The architectural relationship between gates and pavement — the pavement being the lower-pavement (<em>haritzpa hatachtona</em>) — establishes a visual and spatial hierarchy between the levels of the court, with the gate complexes rising above the surrounding paved areas.</p>",
    "19": "<p><strong>vayamad rochav milifnei hasha'ar hatachton lifnei hachatzar haifnimit lachutz</strong>: 'He measured the width from the front of the lower gate to the outer edge of the inner court.' The distance from outer gate to inner court is one hundred cubits. The measurement east and north establishes the overall proportions of the outer court. The hundred-cubit measurement creates a large transitional space between the outer and inner zones — movement through this space would itself be a kind of ritual preparation as one progressed from less holy to more holy territory.</p>",
    "20": "<p><strong>vehasha'ar asher panav derech hatzafonah</strong>: 'And the gate facing north.' The north gate and south gate (v. 24) are described in parallel to the east gate, with the same measurements confirmed. The three gates on each face of the outer enclosure (north, east, south mentioned; no west gate for the outer court) reflect a standard ancient Near Eastern temple court arrangement. The identical dimensions of all gates (<em>kimidoteihem kamidot hasha'ar asher panav derech haqadim</em> = the same measurements as the east gate) establish the perfect symmetry of the visionary temple.</p>",
    "21": "<p><strong>vetahav shlosha mipo ushlosha mipo</strong>: 'Its guardrooms, three on this side and three on that side.' The north gate's guardrooms, pilasters, and vestibule are described with the same specification as the east gate. The repetition of measurements establishes the rigorous symmetry: every gate element is identical to its counterpart. This architectural uniformity is a spatial expression of divine consistency — the same God is approached from every direction with the same holiness requirements.</p>",
    "22": "<p><strong>vechalunav ve'etamav vetimorotav kemidot hasha'ar</strong>: 'Its windows and its vestibule and its palm trees had the same measurements as the east gate.' The palm trees (<em>timorot</em>) on the north gate match those on the east gate — the sacred vegetation motif is present at every entrance. The fifty cubits long and twenty-five cubits wide measurement is confirmed for all gates. The measurement standardization is not literary economy but architectural theology: the temple is perfectly proportioned, with no gate superior to another.</p>",
    "23": "<p><strong>vesha'ar lechatzar haifnimit nokhach hasha'ar latzafon velaqadim</strong>: 'There was a gate to the inner court opposite the north gate and opposite the east gate.' The alignment of outer and inner gates creates axial processional paths through the courts — a worshiper entering through the outer north gate and proceeding directly ahead would reach the inner north gate. This axis between outer and inner gates creates a structured approach to the inner court, each gate passage a stage in the movement toward the divine presence.</p>",
    "24": "<p><strong>vayolikheni derech darom</strong>: 'He led me toward the south.' The south gate is measured with identical specifications. The comprehensive enumeration of all three accessible gates (north, east, south) with their identical measurements establishes the outer court's complete enclosure. The triple confirmation of identical dimensions across all gates is Ezekiel's architectural way of saying that there is no preferred entrance, no superior gate — all approaches to YHWH's sanctuary are equally holy.</p>",
    "25": "<p><strong>vechalunav ve'etamav saviv kimidot hechalunot hahem</strong>: 'And windows and a vestibule all around corresponding to those other windows.' The windows (<em>chalunot</em>) in the south gate match the east gate's windows. The details are formulaic but not gratuitous: each repetition of &ldquo;the same measurements&rdquo; builds a cumulative picture of perfection — no element varies, no dimension is approximate. This is the architectural expression of YHWH's holiness: exact, complete, without deviation.</p>",
    "26": "<p><strong>vetimorah achat mipo vetimorah achat mipo el-aylov</strong>: 'And palm trees, one on each side, on its pilasters.' Palm trees flanking each gate pilaster — the Eden motif woven throughout the gate complex. The palm tree (<em>tamar</em>), associated with beauty, victory, and divine blessing (cf. Ps 92:12: &ldquo;the righteous will flourish like a palm tree&rdquo;), marks every entrance to the holy complex as simultaneously a place of covenant encounter and a gateway into the restored divine garden-sanctuary.</p>",
    "27": "<p><strong>vesha'ar lechatzar haifnimit derech negev</strong>: 'And there was a gate to the inner court on the south side.' The inner south gate, like the outer south gate, is fifty cubits from outer gate to inner gate. The consistent hundred-cubit depth between outer and inner courts — confirmed by the measurement from gate to gate — establishes the outer court as a precisely defined ceremonial space of exactly proportioned dimensions.</p>",
    "28": "<p><strong>vayevi'eni el-hachatzar haifnimit bisha'ar hadarom</strong>: 'He brought me to the inner court through the south gate.' The transition from outer to inner court marks a significant move inward toward the divine presence. The inner gates are described in the same detail as the outer gates, confirming their identical construction — five verses of measurement confirm that inner and outer gates are architecturally equivalent. The equality of construction between outer and inner gates suggests equal holiness requirements at each boundary.</p>",
    "29": "<p><strong>vetahav ue'eylav ue'etamav kemidot haeileh</strong>: 'Its guardrooms, pilasters, and vestibule were measured and were the same as those.' The inner south gate's dimensions are confirmed as identical to the outer gates (<em>kemidot haeileh</em> = the same as these). The inner court (<em>hachatzar haifnimit</em>) is entered through the same size gate complex as the outer court, creating a structural equality between the transitional spaces while the progression from outer to inner court itself marks increased holiness.</p>",
    "30": "<p><strong>ve'etamot saviv saviv orech chamesh ve'esrim amah veorech chamesh amot</strong>: 'And vestibules all around: twenty-five cubits long and five cubits wide.' The vestibules of the inner court are of identical dimensions to those of the outer court. The outer dimensions of the complex are thus consistent throughout. The five-cubit width of the vestibule creates a transitional space — not quite inside the gate chamber, not yet in the court — where the transition between holy spaces is marked architecturally.</p>",
    "31": "<p><strong>ve'etamav el-hechatzar hachutzah vetimorot el-aylov</strong>: 'And its vestibule faced the outer court, with palm trees on its pilasters.' The inner east gate's vestibule faces outward toward the outer court — the entry vestibule faces the worshiper approaching from outside. The eight steps (<em>u'shmoneh madregot ma'alohu</em>) leading up to the inner gates (versus the six steps of the outer gates) mark the increased elevation and therefore increased holiness of the inner court. Each step upward is a step deeper into the divine presence.</p>",
    "32": "<p><strong>vayevi'eni el-hachatzar haifnimit derech haqadim</strong>: 'He brought me to the inner court on the east side.' The inner east gate is measured and found identical to all the other gates. The complete survey of inner gates (south, east, north) mirrors the survey of outer gates, establishing perfect correspondence between the two enclosures. Each inner gate is reached by eight steps versus the outer gates' six steps, the gradual elevation physically enacting the ascent toward the divine presence.</p>",
    "33": "<p><strong>vetahav ve'etamav ve'etamav kemidot haeileh</strong>: 'Its guardrooms, pilasters, and vestibule were the same as those.' Each iteration of <em>kemidot haeileh</em> (the same as those) builds a cumulative confirmation of perfect architectural consistency. The repetition in chs. 40-48 can seem tedious but serves the theological function of communicating that the eschatological sanctuary is perfectly proportioned — nothing is approximate, nothing is left to human variation.</p>",
    "34": "<p><strong>ve'etamav el-hachatzar hachutzah vetimorot el-aylov mizzo umizo</strong>: 'And its vestibule faced the outer court, with palm trees on both sides.' The inner east gate's vestibule orientation mirrors the south gate. The eight steps (confirmed again for the east gate) establish the consistent elevation pattern. The measurement confirms that what was true of the south inner gate is equally true of the east inner gate — the architectural symmetry is rigorous.</p>",
    "35": "<p><strong>vayevi'eni el-sha'ar hatzafon vayamad kemidot haeileh</strong>: 'He brought me to the north gate and measured it — the same measurements as these.' The north inner gate completes the systematic measurement of all three inner gates. The survey is comprehensive: each gate measured in full detail, each found identical to the others. The effect is that by the time the survey is complete, the reader/listener has a vivid spatial impression of the entire temple complex — its symmetry, its proportions, its multiple layers of access.</p>",
    "36": "<p><strong>tahav etamav ufetachuv</strong>: 'Its guardrooms, its vestibule, and its openings.' The inner north gate's guardrooms and vestibule are the final elements in the gate-survey, completing the systematic outer and inner gate measurements. The total survey covers six gates (outer: north, east, south; inner: south, east, north) — a comprehensive mapping of all access points to the sacred precinct.</p>",
    "37": "<p><strong>ve'etamav el-hachatzar hachutzah vetimorot el-aylov mizzo umizo</strong>: 'And its vestibule faced the outer court, with palm trees on its pilasters, on both sides.' The final confirming formula for the inner north gate. The palm trees (<em>timorot</em>) are present at every gate, outer and inner, on every side. The consistent presence of the Eden-motif at every entry point suggests that the entire sanctuary complex is conceived as a restored Eden — the garden of divine presence accessible from every direction.</p>",
    "38": "<p><strong>velishkah upetachah el-ayilim hasha'arim</strong>: 'There was a chamber with its entrance by the gate pilasters.' Adjacent to the inner gates were chambers (<em>lishkot</em>) used for washing the burnt offerings (<em>sham yad'ichu et-haolah</em>). The functional chambers at the gates represent the practical infrastructure of priestly service — before sacrifice can be offered, the animals must be slaughtered and washed nearby. The integration of functional space with the sacred architecture reflects the priestly vision of the entire temple as a space organized around the mechanics of covenant worship.</p>",
    "39": "<p><strong>uve'ulam hasha'ar shulchanot shnaim mipo ushnaim mipo</strong>: 'And in the vestibule of the gate were two tables on each side.' Eight tables total (four described here and four more in v. 41) — tables on both sides of the gate vestibule where the sacrificial animals would be slaughtered. <em>Lishchoat aleihem et-haolah vehet-chattat veet-hasham</em> (to slaughter on them the burnt offering, sin offering, and guilt offering) — the three primary sacrificial categories requiring dedicated slaughter spaces. The precision of the cultic infrastructure communicates the seriousness and order of the divine worship.</p>",
    "40": "<p><strong>ulemitzan michutz la'ola lepetach sha'ar hatzafon</strong>: 'On the outside toward the north as one goes up to the entrance of the north gate.' Additional tables flanking the north gate's north side and south side. The spatial arrangement of slaughter tables on both sides of the gate creates a workflow: animals could be processed simultaneously on both sides, maximizing throughput for festival occasions when large numbers of sacrifices would be offered.</p>",
    "41": "<p><strong>shulchanot arba mipo veshulchanot arba mipo</strong>: 'Four tables on this side and four tables on that side.' Eight tables total beside the gate — four on each side — provides abundant preparation space. The table count (eight) matches the eight steps of the inner gates, though whether this is deliberate numerical theology or practical arithmetic is uncertain. Each table is <em>amah achat vahetzi orech ve'amah achat vahetzi rochav</em> (1.5 cubits long by 1.5 cubits wide by 1 cubit high) — a standard altar-table proportion.</p>",
    "42": "<p><strong>ve'arbaah shulchanot la'olah even gazit</strong>: 'The four tables for the burnt offering were of hewn stone.' The slaughter tables for the burnt offering are of hewn stone (<em>even gazit</em>) — the same material used for Solomon's temple (1 Kgs 5:17) and specified for Ezra's rebuilt altar. Stone tables are practical for slaughter (easy to wash, durable) and theologically appropriate (permanence, purity). The dimensions (1.5 x 1.5 x 1 cubit) are the same as the bronze laver bases in Solomon's temple, creating continuity with prior sacred architecture.</p>",
    "43": "<p><strong>vehashephataim topach echad</strong>: 'The hooks, a handbreadth long.' The iron hooks (<em>shephataim</em>) mounted in the gate vestibule — for hanging the slaughtered animals during preparation. The handbreadth measurement for the hooks contrasts with the cubit-scale measurements elsewhere, showing that even the smallest hardware elements of the temple are specified. <em>Ve'al hashulchanot yanichu et-habasar hakorban</em> (on the tables they shall lay the flesh of the offering) — the tables' function is confirmed: both slaughter and preparation of sacrificial meat.</p>",
    "44": "<p><strong>umichutz lasha'ar haifnimi</strong>: 'And outside the inner gate.' The priestly chambers (<em>lishkot meshorerim</em> = chambers of the singers/ministers) are located in the inner court beside the north and south inner gates. These chambers are for the priests who oversee the temple service — the singers (associated with Levitical ministry, cf. 1 Chr 25) would use the south-facing chamber; the priests who keep the altar charge use the north-facing chamber (v. 46).</p>",
    "45": "<p><strong>vayomer elai halishkah hazot asher paneh derech darom lakohanim shomrei mishmeret habayit</strong>: 'He said to me: This chamber that faces south is for the priests who keep charge of the house.' The functional designation of the chambers makes explicit that these are administrative spaces for the priestly divisions. <em>Shomrei mishmeret habayit</em> (keepers of the charge/watch of the house) is the standard designation for the priests who maintain the sanctuary's operational integrity — ensuring the sacrificial calendar, the ritual purity standards, and the physical maintenance of the sacred space.</p>",
    "46": "<p><strong>vehalishkah asher paneh derech tzafon lakohanim shomerei mishmeret hamizbeiach</strong>: 'And the chamber that faces north is for the priests who keep charge of the altar.' The altar-priests versus the house-priests distinction anticipates the detailed priestly regulations of ch. 44, where Ezekiel distinguishes between the Levites (who lost altar privileges because of their apostasy) and the Zadokite priests (who &ldquo;kept the charge of my sanctuary&rdquo; when Israel went astray). <em>Hem benei Tzadoq haqqerevim min-beni Levi el-YHWH</em> (these are the sons of Zadok, from the Levites, who approach YHWH to serve him) — the Zadokite priestly dynasty is formally installed in the eschatological temple.</p>",
    "47": "<p><strong>vayamad et-hechatzar orech meah amah verachav meah amah</strong>: 'He measured the inner court: one hundred cubits long and one hundred cubits wide.' The inner court is a perfect square — <em>rabhua</em> (four-square, perfectly squared). The perfect square is the geometry of divine perfection: the New Jerusalem in Rev 21:16 is also four-square (<em>tetragōnos</em>). The altar (<em>hamizbeiach</em>) stands in front of the temple (<em>lifnei habayit</em>) — centered in this perfect-square court, the focal point of the entire architectural complex and the point of covenant mediation.</p>",
    "48": "<p><strong>vayevi'eni el-ulam habayit vayamad ayil ha'ulam</strong>: 'He brought me to the vestibule of the temple and measured the pilasters of the vestibule.' The approach to the temple building itself (<em>habayit</em>) — the final stage of the architectural survey before the temple interior. The vestibule (<em>ulam</em>) is the entry porch of the main building. Its pilasters (<em>ayil</em>) are five cubits on each side. The gate passage width of three cubits on each side establishes the entry opening — narrower than the court gates, creating a sense of intensified holiness at the building threshold.</p>",
    "49": "<p><strong>orech ha'ulam esrim amah verachav achat esreh amah</strong>: 'The vestibule was twenty cubits long and eleven cubits wide.' The vestibule's dimensions (20 x 11 cubits) are close but not identical to Solomon's vestibule (1 Kgs 6:3: 20 x 10 cubits) — the extra cubit in width may be deliberate eschatological expansion. <em>Ubemad'regot a'lav</em> (there were steps that led up to it) — the vestibule is reached by steps, maintaining the pattern of ascending elevation as one approaches the divine presence. The columns (<em>amudim</em>) flanking the doorposts echo Jachin and Boaz of Solomon's temple (1 Kgs 7:15-22), connecting the visionary temple to the historical one while transcending it.</p>"
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
