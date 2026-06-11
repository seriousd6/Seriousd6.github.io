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
  "49": {
    "1": "<p><strong>מִלְכֹּם</strong> (<em>Milkom</em>): the national deity of Ammon (cf. 1 Kgs 11:5,7). The oracle's opening is a legal challenge: has Israel no heir to possess Gad's territory? The verb <em>yarash</em> (inherit, dispossess) is the covenant-land term used for Israel's original conquest. Milcom 'possessing' (<em>yarash</em>) Israelite territory is a theological affront — it is YHWH's land, and the Ammonite national god has no legitimate claim.</p>",
    "2": "<p><strong>תְּרוּעַת מִלְחָמָה</strong> (<em>teru'at milchama</em>, war cry): the same term as the sacred shout (<em>teru'ah</em>) at Sinai and the signal for holy war. YHWH announces that he will deploy the war-shout against Rabbah (<em>Rabbat Bene-Ammon</em>, modern Amman) — the Ammonite capital. <strong>תֵּהְיֶה לְתֵל שְׁמָמָה</strong> (<em>tehyeh letel shemamah</em>, will become a heap of ruin): <em>tel</em> (mound) is the archaeological designation for ancient ruin mounds, still used today.</p>",
    "3": "<p><strong>הֵילִילִי חֶשְׁבּוֹן</strong> (<em>heilili Cheshbon</em>, wail, O Heshbon): Heshbon was previously a Moabite/Reubenite city; the overlap of territories in these oracle poems reflects historical complexity. <strong>שַׂקִּים חִגְרוּ</strong> (<em>saqim chigru</em>, gird on sackcloth): the mourning garment. <strong>מַלְכָּם</strong> (<em>Malkam</em>): some manuscripts have <em>melek</em> (their king) and others <em>Milkom</em> (the god) — the ambiguity may be intentional: the god who was their 'king' goes into exile.</p>",
    "4": "<p><strong>הַבַּת הַשּׁוֹבֵבָה</strong> (<em>habbat hashsovevah</em>, the backsliding/faithless daughter): the feminine personification of Ammon as a daughter who has turned away — <em>shavav</em> is the apostasy root. <strong>בָּטְחָה בְּאֹוצְרֹתֶיהָ</strong> (<em>vatcha be'otzarotehah</em>, trusted in her treasures): trust-vocabulary (<em>batach</em>) applied to material security rather than YHWH — the Ammonite error that mirrors Israel's recurring failure.</p>",
    "5": "<p><strong>מְבִיא עָלַיִךְ פַּחַד</strong> (<em>mevi alayikh pachad</em>, bringing terror upon you): <em>pachad</em> is dread/terror — the covenant curse of Deut 28:66-67. The full title <em>Adonai YHWH Tzvaot</em> (Lord YHWH of Hosts) carries maximum divine-warrior weight — the armies of heaven mobilized against Ammon.</p>",
    "6": "<p><strong>וְאַחֲרֵי-כֵן אָשִׁיב אֶת-שְׁבוּת בְּנֵי עַמּוֹן</strong> (<em>ve'acharei-khen ashiv et-shevut benei Ammon</em>, but afterward I will restore the fortunes of the Ammonites): the same restoration formula used for Israel (29:14; 30:3). YHWH's restoration purpose extends even to Ammon — the cup of wrath is followed by the possibility of return, countering the idea that the nations oracles are simply doom.</p>",
    "7": "<p><strong>חָכְמָה בְּתֵימָן</strong> (<em>chokhmah beteman</em>, wisdom in Teman): Edom/Teman had an ancient reputation for wisdom in the ANE — Job's friend Eliphaz is from Teman (Job 2:11). The oracle's opening question — has Edomite wisdom perished? — is rhetorical: Edom's famous wisdom has failed to anticipate the judgment. Obadiah 8 uses the same motif.</p>",
    "8": "<p><strong>עַמְקוּ לָשֶׁבֶת</strong> (<em>amqu lashevet</em>, go deep to dwell): the imperative to Dedan (an Edomite/Arabian tribe) to flee into the deep wilderness. <strong>אֵיד עֵשָׂו</strong> (<em>eid Esav</em>, the disaster of Esau): Edom consistently identified as Esau's descendants — the fraternal enmity of Jacob and Esau projected onto national history. The <em>eid</em> (disaster) echoes the cup-of-wrath theme (v12).</p>",
    "9": "<p><strong>בֹּצְרִים</strong> (<em>botzrim</em>, grape-gatherers): the harvest analogy — even a grape-harvester leaves gleanings by covenant law (Lev 19:10). What will happen to Edom is worse: like nighttime thieves who take only what they want, but YHWH's stripping (<em>chashafti</em>, I have stripped bare) is total (v10). The legal harvest imagery contrasts the partial taking of human agents with YHWH's comprehensive judgment.</p>",
    "10": "<p><strong>אֲנִי חָשַׂפְתִּי אֶת-עֵשָׂו</strong> (<em>ani chasafti et-Esav</em>, but I myself have stripped Esau bare): emphatic personal pronoun — YHWH himself, not Nebuchadnezzar, is the agent. <em>Chashaf</em> (strip/uncover) is used of removing a garment: Edom's protective covering is removed. <strong>גֻּלּוּ זַרְעוֹ</strong> (<em>gullu zar'o</em>, his offspring are devastated): the exile vocabulary, <em>galah</em>, applied to Edom.</p>",
    "11": "<p><strong>עָזְבָה יְתֹמֶיךָ</strong> (<em>azvah yetomekha</em>, leave your orphans): YHWH will keep the orphans alive and the widows can trust him. The covenant care for the vulnerable (Deut 10:18; 27:19) extends even in the context of national destruction. YHWH's judgment on Edom does not revoke his care for the weak who survive it.</p>",
    "12": "<p><strong>כּוֹס</strong> (<em>kos</em>, cup): the cup-of-wrath motif from ch25. If those who did not deserve to drink (<em>asher lo mishpat lahem lishtos et-hakos</em>) were made to drink — i.e., Judah — then certainly Edom will not escape. Paul uses similar reasoning in Rom 11:21 (if God did not spare the natural branches, neither will he spare you).</p>",
    "13": "<p><strong>נִשְׁבַּעְתִּי בִי</strong> (<em>nishbati vi</em>, I have sworn by myself): the divine self-oath formula used for the most irrevocable commitments — used for Abraham's blessing (Gen 22:16) and the new covenant (Heb 6:13). Here it guarantees Bozrah's desolation. <strong>בָּצְרָה</strong> (<em>Botzrah</em>): the principal city of Edom, modern Buseirah in southern Jordan.</p>",
    "14": "<p><strong>שְׁמוּעָה שָׁמַעְתִּי מֵאֵת יְהוָה</strong> (<em>shmu'ah shamati me'et YHWH</em>, I have heard a message from YHWH): the prophetic reception formula — the prophet hears before he speaks. An envoy (<em>tzir</em>) is sent among the nations to form a coalition against Edom. Obadiah 1 parallels this verse almost exactly.</p>",
    "15": "<p><strong>קָטֹן נְתַתִּיךָ בַּגּוֹיִם</strong> (<em>qaton netattikha baggoyim</em>, I have made you small among the nations): the inversion of Edom's pride. <strong>בָּזוּי בָּאָדָם</strong> (<em>vazui ba'adam</em>, despised among human beings): the trajectory of pride → humiliation is the Proverbs principle of divine governance (Prov 16:18) operating at the national level.</p>",
    "16": "<p><strong>זְדוֹן לִבֶּךָ</strong> (<em>zedon libbkha</em>, the pride of your heart): <em>zadon</em> (pride/insolence) is from the root of Pharaoh's hardening and Babylon's arrogance. <strong>שֹׁכְנִי בְּחַגְוֵי הַסֶּלַע</strong> (<em>shokhni bechagvei hasela'</em>, you who dwell in the clefts of the rock): Petra/Sela, Edom's rock-carved mountain fortress. The security of the rock citadel is exposed as a delusion: YHWH's judgment is not blocked by topography.</p>",
    "17": "<p><strong>שַׁמָּה תִּהְיֶה אֱדוֹם</strong> (<em>shammah tihyeh Edom</em>, Edom will become a horror): the horror-and-hissing formula (<em>shammah</em> + <em>sherikah</em>) is the standard covenant-curse expression for complete desolation, used repeatedly for Jerusalem and now applied to Edom. The rhetorical transfer: what Jerusalem suffered for covenant-breaking, Edom suffers for pride and violence against her brother.</p>",
    "18": "<p><strong>כְּמַהְפֵּכַת סְדֹם וַעֲמֹרָה</strong> (<em>kemahpekat Sedom va'Amorah</em>, as in the overthrow of Sodom and Gomorrah): the Sodom/Gomorrah desolation as the paradigm case of total divine judgment. No one will dwell there: <em>lo yeshev sham ish velo yagur bah ben adam</em>. The same formula appears in 50:40 for Babylon — Edom and Babylon parallel recipients of Sodom-type judgment.</p>",
    "19": "<p><strong>כַּאֲרִי יַעֲלֶה מִגְּאוֹן הַיַּרְדֵּן</strong> (<em>ka'ari ya'aleh migge'on haYarden</em>, like a lion coming up from the thickets of the Jordan): the same lion simile used in 4:7 and 5:6 for the enemy as YHWH's agent. <strong>מִי כָּמֹנִי</strong> (<em>mi khamoni</em>, who is like me?): YHWH's rhetorical self-assertion — the incomparability formula from Isa 40:25 applied to his judicial authority over Edom.</p>",
    "20": "<p><strong>יַעֲצַת יְהוָה</strong> (<em>ya'atzat YHWH</em>, the counsel/plan of YHWH): Edom's fate is YHWH's deliberate plan, not accident. <em>Etza</em> (counsel/plan) is wisdom vocabulary — YHWH's sovereign governance operates through deliberate design. The sheep of Teman (<em>tzon teman</em>) will be dragged away — the shepherd-flock imagery of judgment.</p>",
    "21": "<p><strong>מִקּוֹל נִפְלָתָם רָעֲשָׁה הָאָרֶץ</strong> (<em>miqqol nifllatam ra'ashah ha'aretz</em>, at the noise of their fall the earth trembles): the cosmic-scale earthquake response to the fall of a nation — similar imagery to Isa 13:13 (Babylon) and Rev 18:19. The eschatological echo: cosmic disturbance marks the fall of the proud.</p>",
    "22": "<p><strong>כַּנֶּשֶׁר יִדְאֶה וְיִפְרֹשׂ כְּנָפָיו</strong> (<em>kannesher yid'eh veyifros kenafav</em>, like an eagle he will soar and spread his wings): the eagle attack imagery — used for Nebuchadnezzar in Ezek 17:3 as the great eagle. Over Bozrah (<em>al-Botzrah</em>) — the eagle spreads its wings over Edom's capital as a bird of prey over its quarry.</p>",
    "23": "<p><strong>חָמַת וְאַרְפָּד</strong> (<em>Chamat ve'Arfad</em>, Hamath and Arpad): Syrian cities — Hamath on the Orontes, Arpad in northwestern Syria. The <em>shemu'ah ra'ah</em> (bad news/evil report) causes dismay. <strong>הַיָּם</strong> (<em>hayyam</em>, the sea): their anxiety is like the troubled sea — uncontrollable agitation without resolution.</p>",
    "24": "<p><strong>הֵרְפְּתָה דַמֶּשֶׂק</strong> (<em>herpetah Dammesek</em>, Damascus has grown feeble): the great Aramean capital enfeebled — the city that once threatened Israel (Isa 7:1-9) now flees. <em>Chalchalah ve'chivlim</em> (anguish and pangs) — the childbirth imagery for national catastrophe (cf. 4:31; 6:24).</p>",
    "25": "<p><strong>אֵיךְ לֹא-עֻזְּבָה עִיר תְּהִלָּה</strong> (<em>eikh lo-uzzevah ir tehillah</em>, how is the renowned city not abandoned!): the elegiac <em>eikh</em> (how!) introduces a lament over Damascus's fall — the same opening word as Lamentations 1:1. <em>Ir tehillah</em> (city of praise/renown) — Damascus's reputation for civilization is used as a measure of the pathos of its destruction.</p>",
    "26": "<p><strong>יִשְׁכְּבוּ בַחוּצֹתֶיהָ בַּחוּרֶיהָ</strong> (<em>yishkevu bakhutzotyeha bachurehah</em>, her young men will lie in her streets): the inverse of the city's vitality — <em>bachurim</em> (choice young men in their prime) slain in public spaces. The oracle for Damascus echoes the lament over Jerusalem (Lam 2:21).</p>",
    "27": "<p><strong>וְהִצַּתִּי אֵשׁ בְּחוֹמַת דַּמָּשֶׂק</strong> (<em>vehitzatti esh bechomatDammesek</em>, I will set fire to the wall of Damascus): the fire-on-the-walls formula used throughout the nations oracles (Amos 1:4,7,10,12,14). <strong>בִּירֹנוֹת בֶּן-הֲדַד</strong> (<em>biranot Ben-Hadad</em>, the palaces of Ben-hadad): Ben-hadad was the dynastic name of Aramean kings (cf. 1 Kgs 20; 2 Kgs 6-8).</p>",
    "28": "<p>The oracle formula identifies the historical event: Nebuchadnezzar struck (<em>hikkah</em>) Kedar and the kingdoms of Hazor. Kedar = the Arab tribes of the northern Arabian Peninsula (Gen 25:13; Isa 21:16-17) — descended from Ishmael; pastoral/semi-nomadic people, famous for their black tents (Song 1:5) and archery (Isa 21:17).</p>",
    "29": "<p><strong>אָהֳלֵיהֶם וְצֹאנָם</strong> (<em>ohaleihem vetzonam</em>, their tents and flocks): the specific material culture of the tent-dwelling Arab tribes — tents, flocks, curtains (<em>yeriot</em>), vessels (<em>kelim</em>), camels. The list of plunder enumerates the pastoral economy's wealth. <strong>מָגוֹר מִסָּבִיב</strong> (<em>magor missaviv</em>, terror on every side): Jeremiah's own signature phrase (20:3-4,10) now applied to the nations.</p>",
    "30": "<p><strong>נוּסוּ נֻדוּ מְאֹד</strong> (<em>nusu nudu me'od</em>, flee! go far away!): urgent triple imperatives. <strong>עָמַק עָצָה</strong> (<em>amaq atzah</em>, he has made a deep plan): Nebuchadnezzar's strategic intelligence is noted, but behind it is YHWH's counsel — echoing Isa 29:15's warning against hiding plans from YHWH.</p>",
    "31": "<p><strong>גּוֹי שַׁלְאֲנָן</strong> (<em>goi shala'nan</em>, a nation at ease/living in security): the irony of security as vulnerability — a peaceful nation that has no defensive walls, gates, or bars (<em>lo-delatot velo-beriach</em>) is easy prey. Security built on prosperity rather than YHWH's protection is an illusion.</p>",
    "32": "<p><strong>גְּמַלֵּיהֶם לָבַז</strong> (<em>gemaleihem labaz</em>, their camels for plunder): the camel economy stripped. <strong>קֹצְצֵי פֵאָה</strong> (<em>qotztzei pe'ah</em>, those who clip the corners of their hair): a distinctive ethnic identifier for certain Arabian tribes (cf. 9:26; 25:23). They will be <em>zarah lekhol-ruach</em> (scattered to every wind) — the diaspora language.</p>",
    "33": "<p><strong>הָיְתָה חָצוֹר לִמְעוֹן תַּנִּים</strong> (<em>hayetah Chatsor lime'on tannim</em>, Hazor will become a haunt of jackals): when human habitation ends, wild animals take over. <em>Tannim</em> (jackals) are the emblematic inhabitants of ruins throughout the prophets (cf. 9:11; 10:22 for Jerusalem). <strong>שְׁמָמָה עוֹלָם</strong> (<em>shemamah olam</em>, desolation forever): not temporary exile but total abandonment.</p>",
    "34": "<p>The Elam oracle opens with a precise date: the beginning (<em>bereshit</em>) of the reign of Zedekiah. Elam was an ancient power east of Babylon (modern southwestern Iran). The oracle predicts Elam's defeat before the historical rise of Persian power (Elam was absorbed into the Persian Empire under Cyrus). The date formula grounds this among the earliest of Jeremiah's dated prophecies.</p>",
    "35": "<p><strong>שֹׁבֵר אֶת-קֶשֶׁת עֵילָם</strong> (<em>shover et-qeshet Elam</em>, I will break Elam's bow): Elam was famous for its archers — their bow was their primary military asset and national symbol (Isa 22:6). Breaking the bow = destroying the nation's military power at its source. <strong>רֵאשִׁית גְּבוּרָתָם</strong> (<em>reshit gevuratam</em>, the foremost of their strength): the bow was Elam's qualitative edge in battle.</p>",
    "36": "<p><strong>אַרְבַּע רוּחוֹת הַשָּׁמַיִם</strong> (<em>arba ruchot hashamayim</em>, the four winds of heaven): cosmic scope — YHWH will bring the four winds against Elam and scatter them in all directions. This imagery recurs in Ezekiel (37:9) and Daniel (7:2; 8:8) and Revelation's four winds (Rev 7:1).</p>",
    "37": "<p><strong>וְחַתֵּתִי אֶת-עֵילָם</strong> (<em>vachatteti et-Elam</em>, I will terrify Elam): <em>chatt</em> (terror/dismay) — the same root for the shattered self-confidence that judgment brings. The covenant curse of Deut 28:25 ('YHWH will cause you to be defeated before your enemies') applied to the nations: YHWH's moral governance is universal.</p>",
    "38": "<p><strong>וְשַׂמְתִּי כִסְאִי בְּעֵילָם</strong> (<em>vesamti kis'i be'Elam</em>, I will place my throne in Elam): YHWH's throne over Elam — the divine king's judicial seat established in judgment over foreign territory. The throne (<em>kisse'</em>) is the symbol of legal authority. YHWH as universal sovereign has a throne that moves with his judicial activity — cf. Isa 66:1 and Ezek 1 (the mobile chariot-throne).</p>",
    "39": "<p><strong>וְהָיָה בְּאַחֲרִית הַיָּמִים</strong> (<em>vehayah be'acharit hayyamim</em>, but in the latter days): the eschatological phrase. <strong>אָשִׁיב אֶת-שְׁבוּת עֵילָם</strong> (<em>ashiv et-shevut Elam</em>): the same restoration formula applied to Israel and Ammon (v6) is given to Elam. YHWH's purposes for the nations include their ultimate restoration — anticipating the eschatological vision of nations streaming to Zion (Isa 2:2-4; Rev 21:24-26).</p>"
  },
  "50": {
    "1": "<p><strong>הַדָּבָר אֲשֶׁר-דִּבֶּר יְהוָה אֶל-בָּבֶל</strong> (<em>haddavar asher-dibber YHWH el-Bavel</em>, the word that YHWH spoke concerning Babylon): the opening of the most extensive nations oracle in the OT — two full chapters (50-51). The title formula is emphatic: not through vision or symbolic act but <em>davar</em> (word) — direct divine speech. The word concerning the instrument of judgment is itself a judgment.</p>",
    "2": "<p><strong>בֵּל</strong> (<em>Bel</em>) and <strong>מְרֹדַךְ</strong> (<em>Merodakh/Marduk</em>): Bel (='lord') is the title of the chief Babylonian deity Marduk, the patron god of Babylon. <strong>הֹבִישׁוּ עֲצַבֶּיהָ</strong> (<em>hovish atzabbeha</em>, her idols are put to shame): when Babylon falls, its gods are exposed as powerless. Cf. Isa 46:1-2 (Bel bows; Nebo stoops). The fall of Babylon is simultaneously the defeat of Babylon's gods.</p>",
    "3": "<p><strong>מִצָּפוֹן עָלָה עָלֶיהָ גּוֹי</strong> (<em>mitzafon alah aleha goy</em>, from the north a nation has come up against her): the standard 'enemy from the north' oracle formula — used for Babylon's attack on Judah in chs 1-6, now applied against Babylon itself. The wheel of judgment turns: the instrument becomes the object.</p>",
    "4": "<p><strong>בָּכוֹ יֵלֵכוּ</strong> (<em>bakho yelekhu</em>, they will come weeping): Israel and Judah (<em>Israel uYehudah yachdav</em>) will come together — the reunification of the divided kingdom, a theme from chs 30-33. <strong>אֶת-יְהוָה אֱלֹהֵיהֶם יְבַקֵּשׁוּ</strong> (<em>et-YHWH Eloheihem yevaqqeshu</em>, they will seek YHWH their God): <em>baqesh</em> (seek earnestly) — the return involves not just physical migration but spiritual re-orientation toward YHWH.</p>",
    "5": "<p><strong>בְּרִית עוֹלָם</strong> (<em>berit olam</em>, everlasting covenant): the foundational covenant phrase — cf. Gen 9:16 (with Noah), 17:7 (with Abraham), Isa 55:3 (Davidic covenant). The covenant joined at Zion is eternal — not conditional like the Mosaic covenant that was broken (31:32) but permanent like the new covenant (31:33-34). The return from exile culminates in covenant-renewal, not merely political restoration.</p>",
    "6": "<p><strong>צֹאן אֹבְדוֹת</strong> (<em>tzon ovedot</em>, lost sheep): the lost-sheep metaphor for Israel — used by Jesus directly (Matt 10:6; 15:24; Luke 15:4-6). <strong>רֹעֵיהֶם הִתְעוּם</strong> (<em>ro'eihem hit'um</em>, their shepherds led them astray): the shepherds (kings and prophets) who led Israel into apostasy. The people have forgotten (<em>shakhechu</em>) their resting place (<em>rivtzam</em>) — the covenant land and its rest.</p>",
    "7": "<p><strong>כָּל-מְצָאֵיהֶם אֲכָלוּם</strong> (<em>kol-metzaehem akhalum</em>, all who found them devoured them): the nations that conquered Israel claim innocence — 'we are not guilty, for they sinned against YHWH the habitation of righteousness.' The enemies invoke Israel's own covenant guilt as moral justification for predation: the conquerors are YHWH's instruments even while acting from their own interests.</p>",
    "8": "<p><strong>נוּדוּ מִתּוֹךְ בָּבֶל</strong> (<em>nudu mitokh Bavel</em>, go out from the midst of Babylon): the call to flee Babylon — the foundational text for the eschatological 'come out of her' in Rev 18:4 and 2 Cor 6:17. <strong>כָּאֵילִים לִפְנֵי צֹאן</strong> (<em>ka'eilim lifnei tzon</em>, like he-goats leading the flock): the goat leads the flock — those who flee first enable others to follow.</p>",
    "9": "<p><strong>מֵעַרֵּר גּוֹיִם גְּדֹלִים</strong> (<em>me'arrer goyim gedolim</em>, an assembly of great nations from the north): the eschatological coalition against Babylon — historically the Medes (Isa 13:17) and Persians. <strong>חִצָּיו כְּגִבּוֹר מַשְׁכִּיל</strong> (<em>chitzav kegibor maskil</em>, his arrows like those of a skilled warrior): the arrows return not <em>riqam</em> (empty) — they all find their mark. Total military effectiveness.</p>",
    "10": "<p><strong>וְהָיְתָה כַשְׂדִּים לְשָׁלָל</strong> (<em>vehayetah Khashdim leshalal</em>, Chaldea will be for plunder): the reversal — Chaldea/Babylon, which plundered all the nations, becomes itself plunder. The retributive principle of 51:24 and Rev 18:6 (repay her double).</p>",
    "11": "<p><strong>שֹׁסֵי נַחֲלָתִי</strong> (<em>shosei nachalati</em>, plunderers of my inheritance): Israel as YHWH's <em>nachalah</em> (inheritance/portion) — the attack on Israel is an attack on YHWH's own property. <strong>כְּעֶגְלָה דָשָׁה</strong> (<em>ke'eglah dashah</em>, like a heifer on grass): the leaping/playful image of Babylon's joy over Israel's destruction — frivolous delight in conquest that YHWH will reverse.</p>",
    "12": "<p><strong>בֹּשָׁה אִמְּכֶם מְאֹד</strong> (<em>boshah imkhem me'od</em>, your mother will be utterly ashamed): Babylon as mother — the city personified as progenitor of its people. <strong>אַחֲרִית גּוֹיִם</strong> (<em>acharit goyim</em>, the least of nations): the inversion of imperial status — the empire that dominated all nations will be last among them.</p>",
    "13": "<p><strong>מֵחֲמַת יְהוָה</strong> (<em>mechamat YHWH</em>, because of YHWH's wrath): the explicit theological cause of Babylon's desolation — not geopolitical accident but YHWH's directed wrath. <strong>שַׁמָּה תִּהְיֶה לְכֹלָה</strong> (<em>shammah tihyeh lekhollah</em>, she will be completely desolate): the superlative desolation formula. Historically ironic: Babylon was indeed abandoned, a desolate mound for centuries.</p>",
    "14": "<p><strong>עִרְכוּ עַל-בָּבֶל מִסָּבִיב</strong> (<em>irkhu al-Bavel missaviv</em>, take your positions against Babylon from every side): the battle deployment command. <strong>כָּל-דֹּרְכֵי קֶשֶׁת</strong> (<em>kol-dorkhei qeshet</em>, all who draw the bow): archers surround the city. <strong>אַל-תַּחְמֹלוּ</strong> (<em>al-tachmolu</em>, do not spare your arrows): no quarter — the covenant standard of <em>cherem</em> applied to Babylon.</p>",
    "15": "<p><strong>נָתְנָה יָדָהּ</strong> (<em>natneah yadah</em>, she has surrendered): the surrender gesture — offering the hand. <strong>נִקְמַת יְהוָה</strong> (<em>niqmat YHWH</em>, the vengeance of YHWH): <em>naqam</em> (vengeance/retribution) — YHWH's retributive justice on behalf of his people. The vengeance is not personal spite but covenant-legal satisfaction.</p>",
    "16": "<p><strong>כִּרְתוּ זוֹרֵעַ מִבָּבֶל</strong> (<em>kirtu zore'a mibbavel</em>, cut off the sower from Babylon): the agricultural infrastructure destroyed. The sword drives everyone to their own people (<em>el-ammo yifanu</em>) — the dissolution of Babylon's polyglot population that sustained its imperial economy (cf. Rev 18:17-19 on the merchants fleeing).</p>",
    "17": "<p><strong>שֶׂה פְזוּרָה יִשְׂרָאֵל</strong> (<em>seh pezurah Yisrael</em>, Israel is a scattered sheep): <em>pazar</em> (scatter) is the diaspora verb. Two predators named: the king of Assyria first (<em>rishonah</em>) devoured, and last (<em>ve'acharonah</em>) Nebuchadnezzar of Babylon. The two-stage scattering maps onto Assyrian conquest of the north (722 BCE) and Babylonian conquest of the south (586 BCE).</p>",
    "18": "<p><strong>לָכֵן כֹּה-אָמַר יְהוָה צְבָאוֹת</strong> (<em>lakhen koh-amar YHWH Tzvaot</em>, therefore thus says YHWH of Hosts): the consequential conjunction. YHWH will punish (<em>paqad</em>) the king of Babylon as he punished the king of Assyria. The same judicial standard applies to each imperial power in sequence — precedent binds YHWH's judgment.</p>",
    "19": "<p><strong>וַהֲשִׁבֹתִי אֶת-יִשְׂרָאֵל אֶל-נָוֵהוּ</strong> (<em>vahashivoti et-Yisrael el-naveihu</em>, I will restore Israel to his pasture): <em>shuv</em> (return/restore) and <em>naveh</em> (pasture/home) — restoration to covenant land for grazing. <strong>כַּרְמֶל וְהַבָּשָׁן</strong> (<em>Karmel vehaBashan</em>): the most fertile grazing territories — Carmel and Bashan were proverbial for lush vegetation and well-fed livestock.</p>",
    "20": "<p><strong>יְבֻקַּשׁ אֶת-עֲוֹן יִשְׂרָאֵל וְאֵינֶנּוּ</strong> (<em>yevuqqash et-avon Yisrael ve'einennu</em>, Israel's iniquity will be searched for and not found): the forensic search — <em>baqash</em> (seek/search diligently) — finding nothing. The complete erasure of recorded iniquity: the covenant-accusation against Israel will have no evidence. This is the experiential content of the new covenant's 'I will remember their sin no more' (31:34).</p>",
    "21": "<p><strong>מְרָתַיִם</strong> (<em>Meratayim</em>): a cryptographic name for Babylon (from <em>marah</em> = bitter/rebel; <em>meratayim</em> = double rebellion). <strong>פְּקוֹד</strong> (<em>Pekod</em>): another Babylonian name with wordplay — <em>paqad</em> means 'visit in judgment.' Both names encode YHWH's accusation: Babylon is doubly rebellious and is being visited with judgment. The wordplay is both political geography and theological verdict.</p>",
    "22": "<p><strong>קוֹל מִלְחָמָה בָּאָרֶץ</strong> (<em>qol milchama ba'aretz</em>, the sound of battle in the land): a terse proclamation — two words frame the announcement. <strong>וְשֶׁבֶר גָּדוֹל</strong> (<em>veshever gadol</em>, and great destruction): <em>shever</em> (breaking/destruction) is the covenant word for catastrophic collapse (cf. Isa 30:14; Jer 6:14: 'they have healed the wound of my people lightly'). Now there is no light healing.</p>",
    "23": "<p><strong>פַּטִּישׁ כָּל-הָאָרֶץ</strong> (<em>pattish kol-ha'aretz</em>, the hammer of the whole earth): Babylon's imperial self-designation — the hammer that smashes other nations. <strong>אֵיךְ נִכְרַת</strong> (<em>eikh nikkrat</em>, how it is cut down!): the elegiac <em>eikh</em> as for Damascus (49:25). The great instrument of divine judgment has itself been broken: the hammer becomes the nail.</p>",
    "24": "<p><strong>יָקַשְׁתִּי לְךָ</strong> (<em>yaqashti lekha</em>, I laid a snare for you): YHWH as the hunter who set the trap. <strong>וְלֹא יָדָעַתְּ</strong> (<em>velo yada'at</em>, and you did not know it): the ignorance of the prey — Babylon did not know when the trap was set. <strong>כִּי בַיהוָה הִתְגָּרִית</strong> (<em>ki vaYHWH hitgarit</em>, for against YHWH you have contended): the root charge — Babylon's arrogance was ultimately a contest (<em>garah</em>) with YHWH himself.</p>",
    "25": "<p><strong>פָּתַח יְהוָה אֶת-אוֹצָרוֹ</strong> (<em>patach YHWH et-otzaro</em>, YHWH has opened his armory): YHWH's weapons-treasury — the storehouse of covenant judgment. <strong>מְלֶאכֶת אֲדֹנָי יְהוִה צְבָאוֹת</strong> (<em>melekhet Adonai YHWH Tzvaot</em>, the work of the Lord YHWH of Hosts): Babylon's destruction is described as YHWH's own 'work' — cf. Isa 28:21 where YHWH's 'strange work' of judgment is his own purposeful project.</p>",
    "26": "<p><strong>כִּי-עֵת הִיא</strong> (<em>ki-et hi'</em>, for it is the time): the appointed time (<em>et</em>) — the kairos moment of Babylon's judgment. <strong>כְּמוֹ עֲרֵמִים הַחֲרִימוּהָ</strong> (<em>kemo aremim hacheriumuha</em>, pile her up like heaps): the grain-heap imagery. <em>Hacharim</em> (completely destroy): the covenant <em>cherem</em> term — total dedication to destruction, the same language used for Canaanite cities in the conquest.</p>",
    "27": "<p><strong>טִבְחוּ כָל-פָּרֶיהָ</strong> (<em>tivkhu kol-pareha</em>, slaughter all her bulls): the temple sacrifice vocabulary — the Babylonian military/elite as bulls going to slaughter. <strong>כִּי-בָא יוֹמָם עֵת פְּקֻדָּתָם</strong> (<em>ki-va yomam et pequddatam</em>, for their day has come, the time of their judgment): the <em>yom paquddah</em> (day of visitation/judgment) — the appointed accountability day has arrived.</p>",
    "28": "<p><strong>קוֹל נָסִים וּפְלֵטִים</strong> (<em>qol nasim ufletim</em>, the voice of those who flee and escape): the news is carried out of Babylon by its survivors. <strong>לְהַגִּיד בְּצִיּוֹן אֶת-נִקְמַת יְהוָה</strong> (<em>lehagid beTziyyon et-niqmat YHWH</em>, to declare in Zion the vengeance of YHWH): the refugees become heralds in Zion — the crimes committed against YHWH's house are publicly avenged. The proclamation in Zion completes the legal circle.</p>",
    "29": "<p><strong>שַׁלְּמוּ-לָהּ כְּפָעֳלָהּ</strong> (<em>shalemu-lah kefo'alah</em>, repay her according to her work): the <em>shillem</em> (repay/requite) principle of covenant justice — what Babylon did, do to her. <strong>כְּכֹל אֲשֶׁר עָשְׂתָה עֲשׂוּ-לָהּ</strong> (<em>kekhol asher astha asuha</em>, according to all that she did, do to her): the lex talionis at the national level. Rev 18:6 quotes this principle directly for the eschatological Babylon.</p>",
    "30": "<p><strong>לָכֵן יִפְּלוּ בַחוּרֶיהָ בִּרְחֹבֹתֶיהָ</strong> (<em>lakhen yippelu vachehurehah birkhovoteiha</em>, therefore her young men will fall in her streets): the lament-pattern — the city's vitality dies in its own public spaces. The same formula applied to Damascus (49:26) and Jerusalem in Lamentations is now applied to Babylon — all proud cities receive the same covenant reckoning.</p>",
    "31": "<p><strong>הִנְנִי אֵלֶיךָ זָדוֹן</strong> (<em>hineni elekha zadon</em>, behold, I am against you, O arrogance!): the divine <em>hineni elekha</em> formula — used against Tyre, Egypt, and Gog in Ezekiel. Babylon is personified as <em>zadon</em> (pride/arrogance) itself. <strong>כִּי בָא יוֹמֶךָ</strong> (<em>ki va yomekha</em>, for your day has come): the day of YHWH vocabulary applied to Babylon — cf. Isa 13:6,9.</p>",
    "32": "<p><strong>וְכָשַׁל זָדוֹן וְנָפַל</strong> (<em>vekhushal zadon venafal</em>, arrogance will stumble and fall): the Proverbs principle at the national level (Prov 16:18: pride goes before a fall). <strong>וְהִצַּתִּי-אֵשׁ בְּעָרָיו</strong> (<em>vehitzatti-esh be'arav</em>, I will set fire to his cities): the fire-judgment formula visited on the hammer that wielded fire against others.</p>",
    "33": "<p><strong>עֲשׁוּקִים בְּנֵי-יִשְׂרָאֵל וּבְנֵי-יְהוּדָה יַחְדָּו</strong> (<em>ashuqim benei-Yisrael uvenei-Yehudah yachdav</em>, the people of Israel and the people of Judah are oppressed together): the reunification of north and south even in their oppression — <em>yachdav</em> (together) prepares for common restoration. <strong>מֵאֲנוּ לְשַׁלְּחָם</strong> (<em>me'anu leshallecham</em>, they refused to let them go): the Exodus vocabulary — Pharaoh refused (<em>maen</em>) to let Israel go; now Babylon repeats the pattern and faces the same pattern's judgment.</p>",
    "34": "<p><strong>גֹּאֲלָם חָזָק</strong> (<em>go'alam chazaq</em>, their Redeemer is strong/mighty): the <em>go'el</em> (kinsman-redeemer) theology — the legal-familial concept of the nearest relative with both the obligation and the right to redeem a family member from slavery. <em>YHWH Tzvaot shemo</em> (YHWH of Hosts is his name): the title emphasizes military power — the Redeemer is not only legally entitled but militarily capable. The <em>go'el</em> theme runs from Ruth through Isaiah 40-55 (where 'Redeemer' appears 13 times) to Christ who ransoms.</p>",
    "35": "<p><strong>חֶרֶב אֶל-כַּשְׂדִּים</strong> (<em>cherev el-Kashdim</em>, a sword against the Chaldeans): the extended sword-sequence poem — nine <em>cherev el</em> (sword against) stanzas using anaphoric accumulation. The sword Babylon wielded against others is now turned against every class of Babylonian society: officials, sages, warriors, horses, foreigners, treasures.</p>",
    "36": "<p><strong>חֶרֶב אֶל-הַבַּדִּים</strong> (<em>cherev el-habaddim</em>, a sword against her diviners/false prophets): <em>baddim</em> can mean liars/boasters or diviners who speak falsely — both meanings fit. <strong>וְנֹאָלוּ</strong> (<em>veno'alu</em>, they will become fools): the reversal of Babylon's claim to wisdom and divinatory expertise.</p>",
    "37": "<p><strong>חֶרֶב אֶל-הַסּוּסִים</strong> (<em>cherev el-hasusim</em>, a sword against her horses): the complete military-economic complex dismantled — horses, chariots (<em>rekev</em>), foreign troops (<em>erev</em>). <strong>וְהָיוּ לְנָשִׁים</strong> (<em>vehayou lenashim</em>, they will become as women): the covenant-curse reversal of martial valor (Deut 28:25). The treasury (<em>otzarotehah</em>) plundered: economic infrastructure follows the military.</p>",
    "38": "<p><strong>חֹרֶב אֶל-מֵימֶיהָ</strong> (<em>chorev el-meimehah</em>, a drought against her waters): the wordplay shifts from <em>cherev</em> (sword) to <em>chorev</em> (drought/dryness) — nearly identical sounds (ch-r-v). Babylon's hydraulic engineering (the Euphrates, Tigris, irrigation canals) targeted. <strong>אֶרֶץ פְּסִילִים הִיא</strong> (<em>eretz pesilim hi'</em>, for it is a land of idols): Babylon's water-wealth has become spiritually insane (<em>yiththolellu</em>) through idol-madness — cf. Isa 44:9-20 on the idolater's derangement.</p>",
    "39": "<p><strong>צִיִּים וְאִיִּים</strong> (<em>tziyyim ve'iyyim</em>, wild desert creatures and jackals): the desolation fauna who occupy ruin sites. This desolation formula applied to Edom (49:33) anticipates Revelation's 'Babylon ... a haunt of every foul bird and beast' (Rev 18:2). The sequence: Sodom → Edom → Babylon → eschatological Babylon, all described in the same vocabulary.</p>",
    "40": "<p><strong>כְּמַהְפֵּכַת אֱלֹהִים אֶת-סְדֹם וְאֶת-עֲמֹרָה</strong> (<em>kemahpekat Elohim et-Sedom ve'et-Amorah</em>, as when God overthrew Sodom and Gomorrah): the identical formula used for Edom (49:18). Edom and Babylon are parallel types of YHWH's total judgment. In the NT, both serve as figures for eschatological judgment (Rev 14:8; 18:2,21).</p>",
    "41": "<p><strong>הִנֵּה עַם בָּא מִצָּפוֹן</strong> (<em>hineh am ba mitzafon</em>, behold, a people is coming from the north): the enemy-from-the-north oracle pattern used against Judah (1:14; 4:6; 6:1,22) reversed and applied to Babylon. <strong>גּוֹי גָּדוֹל וּמְלָכִים רַבִּים</strong> (<em>goi gadol umelakhim rabbim</em>, a great nation and many kings): the Medo-Persian coalition under Cyrus.</p>",
    "42": "<p><strong>קֶשֶׁת וְכִידוֹן</strong> (<em>qeshet vekidon</em>, bow and spear): the full weapons complement. <strong>אַכְזָרִי הוּא וְלֹא יְרַחֵמוּ</strong> (<em>akhzari hu velo yerachemu</em>, they are cruel and show no mercy): the same characterization given to Babylon when it attacked Judah (6:23) — now applied to Babylon's attackers. The judgment is symmetrical.</p>",
    "43": "<p><strong>שָׁמַע מֶלֶךְ-בָּבֶל אֶת-שִׁמְעָם</strong> (<em>shama melekh-Bavel et-shim'am</em>, the king of Babylon heard the report of them): the same <em>shama'</em> (hear/listen) that marks Israel's failure throughout Jeremiah — now the king of Babylon hears and his hands go limp (<em>raffu yadav</em>). The word that Babylon refused to hear (YHWH's prophetic warnings through Jeremiah) now comes as military intelligence: the same paralysis that fell on Judah falls on Babylon.</p>",
    "44": "<p><strong>כַּאֲרִי יַעֲלֶה מִגְּאוֹן הַיַּרְדֵּן</strong> (<em>ka'ari ya'aleh migge'on haYarden</em>): the lion-from-Jordan simile applied verbatim to Babylon as Jeremiah applied it to Edom (49:19). The repetition is deliberate — Edom and Babylon are parallel targets, and YHWH's incomparability (<em>mi khamoni</em>) governs both judgments equally.</p>",
    "45": "<p><strong>שִׁמְעוּ עֲצַת יְהוָה</strong> (<em>shim'u atzat YHWH</em>, hear the plan of YHWH): the <em>etzah</em> (plan/counsel) of YHWH against Babylon — parallel to 49:20 for Edom. <strong>אֲשֶׁר יָעַץ אֶל-אֶרֶץ כַּשְׂדִּים</strong> (<em>asher ya'atz el-eretz Kashdim</em>, which he has devised against the land of the Chaldeans): <em>ya'atz</em> (devise/plan/purpose) — YHWH's purposes for the nations are not spontaneous but deliberately planned in his council.</p>",
    "46": "<p><strong>מִקּוֹל תִּפְלַשׂ בָּבֶל</strong> (<em>miqqol tiplas Bavel</em>, at the sound of Babylon's capture): the earth quakes (<em>ra'ashah ha'aretz</em>) — cosmic-scale seismic response to the fall of the world-empire. <strong>בַּגּוֹיִם יִשָּׁמַע זַעֲקָהּ</strong> (<em>baggoyim yishama za'aqah</em>, her cry will be heard among the nations): cf. Rev 18:9-10 where the kings of the earth weep at Babylon's destruction from afar. The chapter closes with the full extent of Babylon's significance: its fall reverberates through all the nations, as its rise did.</p>"
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
