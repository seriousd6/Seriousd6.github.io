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
  "10": {
    "1": "<p>The opening summons — <strong>שִׁמְעוּ</strong> (<em>shim'u</em>, hear!) — calls Israel to covenant attention, the same imperative as the Shema (Deut 6:4). This anti-idol polemic (vv1-16) is one of the most sustained in the OT, parallel in many ways to Isa 40-48.</p>",
    "2": "<p><strong>חֻקּוֹת</strong> (<em>chuqqot</em>, customs/practices) of the nations: the same root used for YHWH's covenant statutes, here applied to pagan religious practice. <strong>אוֹתוֹת</strong> (<em>otot</em>, signs) of the heavens — astral divination was central to Babylonian religion; Jeremiah directly targets what would be the dominant religious culture of exile.</p>",
    "3": "<p><strong>הֶבֶל</strong> (<em>hevel</em>, breath/vapor/worthlessness) is the key verdict on idolatry throughout this polemic. The word is Qohelet's signature term (Ecclesiastes); here it renders idol-worship as existentially empty, not merely prohibited. The craftsman (<em>charash</em>) cuts a tree from the forest with an axe (<em>garzen</em>) — material and finite origins exposed from the start.</p>",
    "4": "<p>The idol is adorned with silver and gold, fastened with hammer and nails — a human artifact that cannot stand upright without being nailed down. The polemic anticipates Paul's diagnosis in Rom 1:23 (exchanging the glory of the immortal God for images made to look like mortal creatures).</p>",
    "5": "<p>Like a scarecrow (<em>tomer</em>, literally 'palm-trunk post') in a cucumber field — the idol cannot speak, cannot walk, must be carried. The comparison stresses functional uselessness: it occupies the field but produces nothing and controls nothing. 'Do not fear them' — the nations Israel might envy are worshiping what cannot act.</p>",
    "6": "<p>The contrast opens: <strong>מֵאֵין כָּמוֹךָ</strong> (<em>me'eyn kamokha</em>, there is none like you) — the incomparability formula. <strong>גָּדוֹל שִׁמְךָ בִּגְבוּרָה</strong> — YHWH's name (his character, his reputation) is great in power (<em>gevurah</em>).</p>",
    "7": "<p><strong>מִי לֹא יִירָאֲךָ</strong> (<em>mi lo yira'akha</em>, who would not fear you?) — rhetorical question implying universal warrant for YHWH-reverence. Among all the wise of nations and all their kingdoms, none compares. <strong>כִּי לְךָ יָאָה</strong> (<em>ki lekha ya'eh</em>, for it is fitting for you) — the fear is appropriate, not merely coerced.</p>",
    "8": "<p><strong>בָּעַר</strong> (<em>ba'ar</em>, brutish/stupid): a term for the irrationality of idol-worship, used three times in this chapter (vv8, 14, 21). Unlike <em>hevel</em> which stresses emptiness, <em>ba'ar</em> stresses acting below human rational capacity. The wooden idol-system is a teaching of <em>hevel</em> — a pedagogy of vapor.</p>",
    "9": "<p>Silver from <strong>תַּרְשִׁישׁ</strong> (<em>Tarshish</em>, the far west) and gold from <strong>אוּפָז</strong> (<em>Uphaz</em>, an unidentified gold source) — the idol is cosmopolitan in sourcing, international in pretension, and yet still a fabrication of human craftsmen (<em>charash</em>) and goldsmiths (<em>tzoreph</em>). Blue and purple cloth complete the royal appearance — but it is an appearance only.</p>",
    "10": "<p><strong>וַיהוָה אֱלֹהִים אֱמֶת</strong> (<em>veYHWH Elohim emet</em>, but YHWH is the true/real God): <em>emet</em> is not merely factual correctness but covenantal reliability and deep ontological reality — the opposite of <em>hevel</em>. <strong>אֱלֹהִים חַיִּים</strong> (<em>Elohim chayyim</em>, living God): the idols are dead artifacts; YHWH is alive and self-existent. <strong>מֶלֶךְ עוֹלָם</strong> (<em>melekh olam</em>, eternal king): belonging to the age/eternity — the same phrase Jesus applies to the Father in John 17:3 ('the only true God').</p>",
    "11": "<p>This verse is unique in the Hebrew Bible: written entirely in <strong>Aramaic</strong>, not Hebrew — the only Aramaic verse in Jeremiah. The Aramaic is likely intentional, addressed to nations who would understand it: in their own language, their gods are condemned. <em>Elahayya di shemayya ve-ar'a la avadu</em> — the gods who did not make heaven and earth will perish (<em>ye'avadu</em>) from the earth and from under the heavens.</p>",
    "12": "<p><strong>עֹשֵׂה אֶרֶץ בְּכֹחוֹ</strong> (<em>oseh eretz bekocho</em>): YHWH made the earth by his power (<em>koach</em>). Three parallel cola: power (<em>koach</em>), wisdom (<em>chokhmah</em>), understanding (<em>tevunah</em>). These are the same divine attributes Prov 3:19-20 names as instruments of creation — the wisdom-creation tradition that becomes Christological in 1 Cor 1:30 and Col 1:16.</p>",
    "13": "<p>YHWH's voice over the waters produces roaring heavens; clouds rise from the ends of the earth (<em>aqtzei-aretz</em>). Lightning (<em>baraqim</em>) for rain; wind (<em>ruach</em>) from his storehouses — YHWH is not a national deity but the lord of cosmic weather, precisely what the Baal cult claimed for its storm-god.</p>",
    "14": "<p><strong>נִבְעַר כָּל-אָדָם מִדַּעַת</strong> (<em>niv'ar kol-adam mida'at</em>, every person is brutish without knowledge): the idol-maker's problem is epistemic, not technical. The goldsmith is shamed by his idol because it is a <strong>פֶּסֶל שֶׁקֶר</strong> (<em>pesel sheqer</em>, image of falsehood/deception): <em>sheqer</em> (falsehood) is the moral opposite of <em>emet</em>. No breath (<em>ruach</em>) is in them.</p>",
    "15": "<p><strong>הֶבֶל הֵמָּה</strong> (<em>hevel hemmah</em>, they are vapor/vanity) — the final verdict. <strong>מַעֲשֵׂה תַּעְתֻּעִים</strong> (<em>ma'aseh ta'tu'im</em>, a work of mockery/delusion): will be destroyed in the time of their punishment (<em>pekudatam</em>).</p>",
    "16": "<p><strong>לֹא כְאֵלֶּה חֵלֶק יַעֲקֹב</strong> (<em>lo ke'elleh chelek Ya'akov</em>): <em>chelek</em> (portion/lot/share) — YHWH is what Jacob possesses, not what Jacob makes. <strong>כִּי יוֹצֵר הַכֹּל הוּא</strong> (<em>ki yotzer hakol hu</em>, for he is the Maker of everything): the one who makes all things cannot be one of the things made. Israel is his <strong>נַחֲלָתוֹ</strong> (<em>nachalato</em>, his inheritance) — YHWH Tzeva'ot is his name.</p>",
    "17": "<p>The scene shifts to impending exile. <strong>כַּנְסִי</strong> (<em>kansi</em>, gather up): addressed to Jerusalem personified (feminine). Gather your bundle (<em>keli</em>) from the ground — the besieged city is told to prepare for deportation.</p>",
    "18": "<p><strong>קֹלֵעַ</strong> (<em>qola'</em>, a slinger): YHWH will fling (<em>qela'</em>) the inhabitants as a slinger flings a stone. The violence of the image captures the force of exile — not a gradual departure but an expulsion. <strong>הַפַּעַם</strong> (<em>hapa'am</em>, at this time) — this time is definitive.</p>",
    "19": "<p><strong>אוֹי לִי</strong> (<em>oy li</em>, woe to me): Jeremiah's lament breaks into the oracle. <strong>שִׁבְרִי</strong> (<em>shivri</em>) and <strong>מַכָּתִי</strong> (<em>makati</em>) — my fracture, my wound: Jeremiah identifies with Judah's coming trauma. <strong>נְחֵלִי</strong> (<em>nechelil</em>): 'This is truly my burden' — I will carry it (<em>essa</em>).</p>",
    "20": "<p>The lament continues with tent imagery (<em>oholi</em>, my tent; <em>yeriyo'tai</em>, my tent-cords): the covenant community as a tent whose cords are broken. <strong>בָּנַי יְצָאֻנִי</strong> (<em>banai yetza'uni</em>, my children have gone from me) — exile as family dissolution. There is no one to pitch the tent again.</p>",
    "21": "<p><strong>הָרֹעִים בָּעֲרוּ</strong> (<em>haro'im ba'aru</em>, the shepherds acted brutishly): <em>ba'ar</em> again — the leaders who should guide the flock have become as irrational as idol-worshipers. They have not sought (<em>darash</em>) YHWH — the prophetic demand that leaders consult YHWH (Deut 12:5 uses the same root for seeking YHWH at the appointed place).</p>",
    "22": "<p><strong>קוֹל שְׁמוּעָה</strong> (<em>qol shemu'ah</em>, sound of a report!) — the watchword of judgment from the north. The cities of Judah will become a lair of jackals (<em>tannim</em>) — the standard desolation image in Jeremiah (cf. 51:37).</p>",
    "23": "<p><strong>יָדַעְתִּי יְהוָה כִּי לֹא לָאָדָם דַּרְכּוֹ</strong> (<em>yada'ti YHWH ki lo la'adam darko</em>, I know, O YHWH, that man's way is not his own): one of the most theologically freighted statements in the book. The prophet confesses that human beings cannot direct their own steps — a basis for the new covenant hope of ch 31 (inner transformation by YHWH). Cf. Prov 20:24; Phil 2:13 (God who works in you both to will and to act).</p>",
    "24": "<p><strong>יַסְּרֵנִי יְהוָה אַךְ בְּמִשְׁפָּט</strong> (<em>yassareni YHWH akh bemishpat</em>, correct me, O YHWH, but in justice): Jeremiah asks not to escape chastisement but for it to be measured (<em>bemishpat</em>), not in anger (<em>be'appekha</em>). The fear: being reduced to nothing (<em>lema'at</em>).</p>",
    "25": "<p>The prayer turns outward: pour out your wrath on the nations who do not know you and on the families who do not call on your name — cf. Ps 79:6. Israel's judgment is not YHWH's final word; the nations who consumed Jacob will face reckoning.</p>"
  },
  "11": {
    "1": "<p>A new oracle section opens. <strong>הַדְּבָרִים הָאֵלֶּה</strong> (<em>hadevarim ha'elleh</em>, these words) refers to the covenant terms — the covenant is accessible as a text, a set of specific terms that can be announced.</p>",
    "2": "<p><strong>שִׁמְעוּ אֶת-דִּבְרֵי הַבְּרִית</strong> (<em>shim'u et-divrei haberit</em>, hear the words of the covenant): the covenant (<em>berit</em>) has specific terms (<em>devarim</em>) that must be heard and proclaimed. This chapter likely connects to Josiah's covenant renewal (2 Kings 23:1-3), though Jeremiah's emphasis falls on covenant failure.</p>",
    "3": "<p><strong>אָרוּר הָאִישׁ</strong> (<em>arur ha'ish</em>, cursed is the man): the covenant curse formula (cf. Deut 27-28). Not hearing the covenant = falling under the curse structure that was always embedded in the covenant. Covenant is not merely a relationship but a legal structure with enforceable consequences.</p>",
    "4": "<p><strong>כּוּר הַבַּרְזֶל</strong> (<em>kur habarzel</em>, furnace of iron): Egypt as crucible — both suffering and refinement. <strong>הֱיוּ לִי לְעָם</strong> (<em>heyu li le'am</em>, be my people) / <strong>אֱלֹהֵיכֶם</strong> (<em>Eloheikhem</em>, your God): the mutual covenant formula that runs from Exodus through Jeremiah to Rev 21:3.</p>",
    "5": "<p><strong>אֶרֶץ זָבַת חָלָב וּדְבָשׁ</strong> (<em>eretz zavat chalav udevash</em>, land flowing with milk and honey): the promise linked to Sinai-covenant obedience. Its loss (exile) signifies its removal. <strong>אָמֵן יְהוָה</strong> (<em>Amen YHWH</em>) — Jeremiah's covenant affirmation.</p>",
    "6": "<p>YHWH commands Jeremiah to proclaim (<em>qara</em>) these words in the cities of Judah and streets of Jerusalem — the covenant is public proclamation, not private instruction. The nationwide command anticipates the nationwide covenant-breaking that follows.</p>",
    "7": "<p><strong>הָעֵד הַעִדֹתִי</strong> (<em>ha'ed ha'idoti</em>): infinitive absolute construction for emphatic repeated action — I earnestly, repeatedly warned your ancestors. The frequency of YHWH's warning heightens the culpability of Israel's refusal.</p>",
    "8": "<p><strong>לֹא שָׁמְעוּ</strong> (<em>lo sham'u</em>, they did not listen): the covenant's perpetual problem. <strong>שְׁרִירוּת לִבָּם</strong> (<em>sherirul libam</em>, stubbornness of their heart): a key Jeremianic phrase for the structural resistance that makes the old covenant insufficient and the new covenant (ch 31) necessary.</p>",
    "9": "<p><strong>קֶשֶׁר</strong> (<em>qesher</em>, conspiracy/treason): not merely individual disobedience but organized collective rejection — a political-rebellion term. The men of Judah and inhabitants of Jerusalem have returned to the sins of their first ancestors.</p>",
    "10": "<p><strong>שָׁבוּ עַל עֲוֺנוֹת אֲבוֹתָם</strong> (<em>shavu al avonot avotam</em>, returned to the iniquities of their ancestors): covenant-breaking is generational and repetitive — confirming the diagnosis of 10:23 that humans cannot direct their own way. They went after other gods; they broke the covenant.</p>",
    "11": "<p><strong>הִנְנִי מֵבִיא אֲלֵיהֶם רָעָה</strong> (<em>hineni mevi alehem ra'ah</em>): the <em>hinneh</em> particle marks the immediacy of divine action. <strong>לֹא יוּכְלוּ לָצֵאת מִמֶּנָּה</strong> — from which they cannot escape. The irrevocability is underscored.</p>",
    "12": "<p>The cities will cry to their gods, but the gods cannot save. The tragic irony: Israel chose gods who cannot answer in the time of need, while abandoning the God who could. <strong>כְּמִסְפַּר עָרֶיךָ</strong> (<em>kemispar areycha</em>) — as many as your cities are your gods.</p>",
    "13": "<p>As many altars (<em>mizbechot</em>) as streets in Jerusalem, set for Baal — directly violating the Deuteronomic principle of one worship-place. The proliferation of worship sites signals the complete breakdown of covenant exclusivity.</p>",
    "14": "<p><strong>אַל-תִּתְפַּלֵּל</strong> (<em>al-titpallel</em>, do not pray/intercede): a striking prohibition on prophetic intercession — the covenant-breaking is so complete that even Moses-style intercession is forbidden. This is repeated in 7:16 and 15:1 (not even Moses and Samuel could intercede). The prohibition signals a covenant boundary has been crossed.</p>",
    "15": "<p><strong>יְדִידִי</strong> (<em>yedidi</em>, my beloved): a term of deep covenant affection — cf. Deut 33:12; Song of Songs. YHWH calls Israel 'my beloved' even while announcing judgment. <strong>מַה-לִּידִידִי בְּבֵיתִי</strong> (<em>mah-liyedidi beveyti</em>): what claim does my beloved have in my house when she acts wickedly? Sacrifice cannot override unfaithfulness.</p>",
    "16": "<p><strong>זַיִת רַעֲנָן יְפֵה-פְרִי תֹאַר</strong> (<em>zayit ra'anan yefeh-peri to'ar</em>, a thriving olive tree, beautiful in fruit and appearance): Israel as YHWH's intended planting — productive and beautiful. The olive tree metaphor recurs in Ps 52:8 and Rom 11:17-24 (Paul's wild-olive grafting). The contrast: with fire and noise, its branches will burn.</p>",
    "17": "<p>YHWH himself planted (<em>neta'</em>) Israel and now pronounces judgment because of the evil done, burning incense to Baal. The planting-pruning imagery anticipates John 15 (the vine; the Father who removes fruitless branches).</p>",
    "18": "<p>YHWH revealed to Jeremiah the plot of the Anathoth men against him. <strong>אָז רָאִיתִי מַעֲלְלֵיהֶם</strong> (<em>az ra'iti ma'alelehem</em>): YHWH's revelation is the source of Jeremiah's knowledge — the prophet could not have known by ordinary means.</p>",
    "19": "<p><strong>כְּכֶבֶשׂ אַלּוּף</strong> (<em>kekeves alluf</em>, like a gentle/tame lamb) led to slaughter (<em>tivach</em>) without knowing it. This image is taken up in NT for Christ: Isa 53:7 ('led like a lamb to slaughter'), John 1:29 ('the Lamb of God'), Acts 8:32. <strong>נַכְרִיתֶנּוּ מֵאֶרֶץ חַיִּים</strong> (<em>nakritenu me'eretz chayyim</em>, let us cut him off from the land of the living): the exact phrase used in Isa 53:8 of the Servant.</p>",
    "20": "<p><strong>יְהוָה צְבָאוֹת שֹׁפֵט צֶדֶק</strong> (<em>YHWH Tzeva'ot shofet tzedek</em>, YHWH of armies, righteous judge): Jeremiah commits his case to the divine judge. <strong>בֹּחֵן כְּלָיוֹת וָלֵב</strong> (<em>bocheyn kelayot va-lev</em>, tester of kidneys and heart): in Hebrew physiology, kidneys = deep emotion/conscience; heart = thought/will — testing both means examining the complete inner person. Cf. Rev 2:23 (Jesus: 'I search hearts and minds').</p>",
    "21": "<p>The specific threat: men of Anathoth threaten Jeremiah not to prophesy in YHWH's name. The hometown opposition to the prophet is a type of the broader rejection pattern — anticipating Jesus's rejection at Nazareth (Luke 4:24: 'no prophet is accepted in his hometown').</p>",
    "22": "<p>YHWH's response: the young men of Anathoth will die by sword; their sons and daughters by famine. The principle that violence plotted against the prophet returns on the plotters — a microcosm of the larger oracle-fulfillment dynamic throughout Jeremiah.</p>",
    "23": "<p><strong>שְׁאֵרִית לֹא תִהְיֶה לָהֶם</strong> (<em>she'erit lo tihyeh lahem</em>, there will be no remnant for them): the reversal of remnant hope applied to Jeremiah's persecutors. The year of their punishment (<em>pekudatam</em>) is coming.</p>"
  },
  "12": {
    "1": "<p><strong>צַדִּיק אַתָּה יְהוָה</strong> (<em>tzaddiq attah YHWH</em>): Jeremiah opens his theodicy complaint by formally acknowledging YHWH's righteousness — the legal premise of the lawsuit (<em>rib</em>). <strong>אַךְ מִשְׁפָּטִים אֲדַבֵּר אוֹתָךְ</strong> (<em>akh mishpatim adabber otakha</em>, yet I will argue my case with you): <em>mishpatim</em> are legal judgments; the prophetic complaint is a formal legal proceeding. The complaint: why does the wicked prosper (<em>shalehu</em>, be undisturbed)?</p>",
    "2": "<p><strong>נְטַעְתָּם גַּם-שֹׁרָשׁוּ</strong> (<em>neta'tam gam-shorrashu</em>, you planted them and they have taken root): YHWH's own planting is acknowledged. The devastating diagnosis: <strong>קָרוֹב בְּפִיהֶם וְרָחוֹק מִכִּלְיוֹתֵיהֶם</strong> (<em>qarov befiyhem verachok mikillyotehem</em>, near in their mouths but far from their inner being) — verbal religion without inner reality. Cf. Isa 29:13; Matt 15:8.</p>",
    "3": "<p>YHWH knows (<em>yada'ta</em>) Jeremiah intimately — the covenantal knowledge that distinguishes genuine relationship from verbal profession. <strong>בָּחַנְתָּ לִבִּי</strong> (<em>vachanta libbi</em>, you have tested my heart): YHWH's scrutiny confirms genuine covenant loyalty. <strong>הַשְׁלִיכֵם כְּצֹאן לְטִבְחָה</strong> (<em>hashlikhem ketzon letivchah</em>): the lamb-imagery of ch 11 reversed — the persecutors become the ones marked for slaughter.</p>",
    "4": "<p><strong>עַד-מָתַי תֶּאֱבַל הָאָרֶץ</strong> (<em>ad-matai te'eval ha'aretz</em>, how long will the land mourn): the land participates in covenant consequences — drought and famine as manifestations of broken covenant (Deut 28:23-24). The wicked claim: 'He will not see our latter end' — denying divine judgment.</p>",
    "5": "<p>YHWH's unexpected response: <strong>כִּי אֶת-רַגְלִים רַצְתָּ</strong> (<em>ki et-raglim ratztah</em>, if you have raced against foot-soldiers): a challenge-question that escalates stakes. If this level of difficulty wears Jeremiah out, how will he survive the thicket of the Jordan? The point: what is coming will be harder, not easier; the prophet must deepen rather than seek relief.</p>",
    "6": "<p>Even Jeremiah's own brothers (<em>acheycha</em>) have dealt treacherously (<em>bagadu</em>) with him. <strong>אַל-תַּאֲמֵן בָּהֶם</strong> (<em>al-ta'amen bahem</em>, do not trust them): the root <em>aman</em> — do not place <em>emunah</em> in them. Micah 7:5-6 captures the same family-betrayal dynamic; Jesus invokes it in Matt 10:35-36.</p>",
    "7": "<p><strong>עָזַבְתִּי אֶת-בֵּיתִי</strong> (<em>azavti et-beiti</em>, I have forsaken my house): YHWH speaks as one who has abandoned his own household — temple and covenantal family. <strong>נָתַתִּי אֶת-יְדִידוּת נַפְשִׁי</strong> (<em>natati et-yedidut nafshi</em>, I have given the beloved of my soul): <em>yedidut</em> is passionate covenant-love. Giving her over to enemies is an act of grief-driven self-sacrifice.</p>",
    "8": "<p>My inheritance (<em>nachalati</em>) has become like a lion roaring against me — the covenant relationship that should be the greatest good has become the source of the greatest grief. The lion that should be a lamb has turned predatory.</p>",
    "9": "<p>Is my inheritance like a speckled bird of prey surrounded by other birds of prey? The image suggests Israel's exposed, vulnerable position — made a target by the surrounding nations because of her unfaithfulness.</p>",
    "10": "<p><strong>רֹעִים רַבִּים שִׁחֲתוּ כַרְמִי</strong> (<em>ro'im rabbim shichatu karmi</em>, many shepherds have ruined my vineyard): <em>kerem</em> (vineyard) is the covenant metaphor for Israel (cf. Isa 5:1-7). The shepherd-rulers who trample the vineyard stand condemned — the sequence continues through Ezek 34 and John 10.</p>",
    "11": "<p><strong>שְׁמָמָה</strong> (<em>shemamah</em>, desolation): the land mourning (<em>avelah</em>) before YHWH. Because no one lays it to heart (<em>sheym al lev</em>, takes it seriously), the desolation persists.</p>",
    "12": "<p>Destroyers have come upon all the bare heights in the wilderness — YHWH's sword devours from one end to the other. No peace (<em>shalom</em>) for any flesh — the sword is a covenant curse for treaty-breaking (Lev 26:25).</p>",
    "13": "<p><strong>זָרְעוּ חִטִּים וְקֹצִים קָצָרוּ</strong> (<em>zar'u chittim veqotzim qatzaru</em>, they sowed wheat but reap thorns): the agricultural reversal of covenant blessing (Deut 28:18-24) — futile labor as covenant curse. Ashamed (<em>hivoshu</em>) of their produce because of YHWH's fierce anger.</p>",
    "14": "<p>The nations: evil neighbors who touch Israel's inheritance will be uprooted (<em>attesh</em>) from their land. But after uprooting, YHWH will have compassion — the first hint that judgment on nations serves a larger restorative purpose.</p>",
    "15": "<p><strong>וְשַׁבְתִּי וְרִחַמְתִּים</strong> (<em>veshavti verichhamtim</em>, I will return and have compassion on them): the compassion-after-judgment pattern that drives the new covenant promise. Each person will be brought back to their heritage (<em>nachlatohu</em>) and land.</p>",
    "16": "<p>Nations who learn Israel's ways — who learn to swear by YHWH's name rather than Baal — will be built up (<em>yibbaneh</em>) among YHWH's people. Covenant membership is extendable to nations who adopt the covenant pattern — anticipating the Gentile inclusion of the NT.</p>",
    "17": "<p>The nation that does not listen (<em>lo yishma'</em>) will be utterly uprooted and destroyed — the same covenant-obedience standard applies to all nations. Covenant relationship brings both the promise of inclusion and the threat of consequence.</p>"
  },
  "13": {
    "1": "<p><strong>אֵזוֹר פִּשְׁתִּים</strong> (<em>ezor pishtim</em>, linen belt/waistcloth): the sign-act (<em>mashal</em>) begins with an intimate garment — worn next to the skin, signifying the closeness of the YHWH-Israel bond. Linen (<em>pishtim</em>) was the material of priestly garments (Ex 28:39), adding priestly overtones to the sign. <strong>אַל-תְּבִיאֵהוּ בַמָּיִם</strong> (<em>al-tevi'ehu vamayim</em>, do not put it in water): kept unwashed, representing the uncleansed intimacy of the relationship as it was meant to be.</p>",
    "2": "<p>Jeremiah buys the sash and wears it according to YHWH's word — sign-acts require faithful literal enactment; the prophet's body becomes the medium of the prophetic message.</p>",
    "3": "<p>YHWH's second word: go to the Euphrates (<em>Perat</em>) and hide it there in a crevice of rock. The Euphrates is Babylon — the hiding place is the location of exile.</p>",
    "4": "<p>The command is enacted — whether by literal travel or visionary enactment (the distance makes literal two-way travel possible but logistically demanding). The sign-act is narrated to be read, not audited for logistics.</p>",
    "5": "<p>Jeremiah went and hid the sash at the Euphrates as commanded — the prophet's obedience in sign-acts is as constitutive of the message as the spoken word. The enacted word is YHWH's word.</p>",
    "6": "<p>Many days later YHWH says: arise, retrieve the sash — the time gap represents the exile period. What was hidden is now to be recovered and examined as evidence.</p>",
    "7": "<p><strong>וְהִנֵּה נִשְׁחַת הָאֵזוֹר</strong> (<em>vehinneh nishchat ha'ezor</em>, and behold the sash was ruined): <em>shachat</em> (ruin/corruption) — the same root used for the moral corruption of the people. <strong>לֹא יִצְלָח לַכֹּל</strong> (<em>lo yitzlach lakol</em>, good for nothing at all): completely useless. The ruined garment is the sermon before the sermon.</p>",
    "8": "<p>The word of YHWH came again to interpret the sign — the sign-act requires prophetic interpretation. Ezekiel's sign-acts follow the same pattern; Jesus's parables function similarly.</p>",
    "9": "<p><strong>כָּכָה אַשְׁחִית</strong> (<em>kakha ashchit</em>, in this way I will ruin): the sign is the sermon. <strong>גְּאוֹן יְהוּדָה</strong> (<em>ge'on Yehudah</em>) and <strong>גְּאוֹן יְרוּשָׁלַם</strong> (<em>ge'on Yerushalayim</em>, the great pride of Judah and Jerusalem): their pride will be ruined precisely as the sash was — the pride-judgment link runs throughout the prophets.</p>",
    "10": "<p><strong>הָעָם הָרַע הַזֶּה</strong> (<em>ha'am hara' hazeh</em>, this evil people): moral diagnosis. <strong>שְׁרִירוּת לִבָּם</strong> (<em>sherirul libam</em>, stubbornness of their heart): this phrase recurs throughout Jeremiah (3:17; 7:24; 9:13; 11:8; 23:17) — the structural intractability that makes the new covenant (ch 31) necessary rather than optional. They cling (<em>halakh achar</em>) to other gods.</p>",
    "11": "<p><strong>כַּאֲשֶׁר יִדְבַּק הָאֵזוֹר אֶל-מָתְנֵי-אִישׁ</strong> (<em>ka'asher yiddaq ha'ezor el-motnei-ish</em>): <em>davaq</em> (cling/cleave) — the same word for the marriage bond (Gen 2:24), for Israel's commanded devotion to YHWH (Deut 10:20: <em>uvdo uvo tidbaq</em>, serve him and cling to him), and for Ruth clinging to Naomi (Ruth 1:14). YHWH bound Israel to himself as intimate garment for renown (<em>tiferet</em>), praise (<em>tehillah</em>), and glory (<em>tif'eret</em>) — but they would not listen.</p>",
    "12": "<p>Every wineskin (<em>nevel</em>) is filled with wine — a proverb the people use dismissively ('yes, of course!'). But YHWH redirects: I will fill every inhabitant with drunkenness (<em>shikkaron</em>). The wine/judgment equation runs through the prophets (Jer 25:15-17 — the cup of wrath).</p>",
    "13": "<p>The drunkenness will cause them to dash (<em>nifatzti</em>) against one another — father against son. YHWH will not spare (<em>lo achmel</em>), pity (<em>lo arachem</em>), or have mercy (<em>lo achus</em>) — triple negation for the completeness of judgment.</p>",
    "14": "<p><strong>וְנִפַּצְתִּים אִישׁ אֶל-אָחִיו</strong> (<em>venifatztim ish el-achiv</em>, I will dash them man against his brother): the internal violence following covenant-breaking. No pity, no compassion, no mercy — three ways of saying the protective covenant relationship is suspended.</p>",
    "15": "<p><strong>שִׁמְעוּ וְהַאֲזִינוּ</strong> (<em>shim'u veha'azinu</em>): hear and give ear — synonymous verbs for emphatic summons. <strong>אַל-תִּגְבְּהוּ</strong> (<em>al-tigbehu</em>, do not be arrogant): the pride-warning before the deportation. <strong>כִּי יְהוָה דִּבֵּר</strong> (<em>ki YHWH dibber</em>) — the prophetic authority-claim.</p>",
    "16": "<p><strong>תְּנוּ לַיהוָה אֱלֹהֵיכֶם כָּבוֹד</strong> (<em>tenu laYHWH Eloheykhem kavod</em>, give glory/honor to YHWH your God): <em>kavod</em> (glory/weight) — the call to acknowledge YHWH's weightiness before the darkness of exile falls. Before the feet stumble on the mountains of twilight, before the hoped-for light becomes deep darkness.</p>",
    "17": "<p><strong>תִּבְכֶּה נַפְשִׁי בְמִסְתָּרִים</strong> (<em>tivkeh nafshi bemistarim</em>, my soul will weep in secret): one of the most intimate prophetic self-revelations — Jeremiah's hidden tears for the flock's captivity. The prophet's inner grief mirrors YHWH's own grief over the covenant people. <strong>מִפְּנֵי גַאֲוָה</strong> (<em>mipney ga'avah</em>) — because of pride: pride is the reason for exile.</p>",
    "18": "<p>The command to king (<em>melekh</em>) and queen mother (<em>gevira</em>): sit low (<em>shiflu</em>), for your crown (<em>ateret tif'artechem</em>, crown of your glory) has fallen. This likely addresses Jehoiachin and Nehushta (2 Kings 24:8) — the royal house goes into exile and its dignity is stripped.</p>",
    "19": "<p>The cities of the Negev are shut up (<em>sug</em>), with no one to open them. All Judah is carried into exile — the geography of deportation expanding from south to north. The totality fulfills the covenant curse of Lev 26:33.</p>",
    "20": "<p>Jerusalem is addressed directly: <strong>שְׂאִי עֵינַיִךְ</strong> (<em>se'i einayikh</em>, lift up your eyes): see those coming from the north. Where is your beautiful flock that was given to you? The shepherd-imagery turned accusatory — Jerusalem is responsible for the flock she received and failed to protect.</p>",
    "21": "<p>What will you say when they appoint your trained allies as head over you? A rhetorical question exposing the bitter irony: the alliances cultivated for security will become Judah's captors. The pain (<em>chavalim</em>) of a woman in childbirth — sudden, unavoidable, consuming.</p>",
    "22": "<p><strong>לָמָּה קָרָאנִי זֹאת</strong> (<em>lamah qara'ani zo't</em>, why has this happened to me?): Jerusalem's anticipated question. The answer: <strong>בְּרֹב עֲוֺנֵךְ</strong> (<em>berov avonekh</em>, because of the multitude of your iniquities). The skirt-lifting metaphor: the shame of exposed unfaithfulness as both military defeat and judicial consequence.</p>",
    "23": "<p><strong>הֲיַהֲפֹךְ כּוּשִׁי עוֹרוֹ</strong> (<em>hayahafokh Kushi oro</em>, can a Cushite change his skin): the Cushite (<em>Kushi</em>) is used for a visually unmistakable difference. <strong>וְנָמֵר חֲבַרְבֻּרֹתָיו</strong> (<em>venamed chavarburotav</em>, or a leopard its spots): the leopard's pattern is as fixed as the Cushite's skin. Theological point: Judah has become so habituated to evil (<em>hiskhilu laro'a</em>, accustomed to doing evil) that self-generated moral change is as impossible as changing these natural characteristics. One of the OT's most direct statements of the bondage of the will — grounding the need for the new covenant's heart-replacement in ch 31.</p>",
    "24": "<p><strong>כְּקַשׁ עֹבֵר</strong> (<em>kekash over</em>, like passing chaff): scattered by the desert wind (<em>ruach midbar</em>). The wind-chaff image for judgment appears in Ps 1:4 and continues into NT judgment imagery (Matt 3:12 — chaff burned with unquenchable fire).</p>",
    "25": "<p><strong>זֶה גוֹרָלֵךְ מְנָת-מִדַּיִךְ</strong> (<em>zeh goralekh menat-midayikh</em>): <em>goral</em> (lot/fate) and <em>menah</em> (measured portion) frame exile as YHWH's judicial apportionment. <strong>שָׁכַחְתְּ אוֹתִי</strong> (<em>shakacht oti</em>, you have forgotten me): the sin is ultimately relational — forgetting YHWH is the root of all the rest.</p>",
    "26": "<p>YHWH himself will lift her skirts over her face — shame of exposed nakedness as both military metaphor for defeat and legal metaphor for the consequences of unfaithfulness. Cf. Ezek 16:37; Hos 2:3.</p>",
    "27": "<p>The closing indictment: <strong>נִאֻפַיִךְ</strong> (<em>ni'ufayikh</em>, your adulteries) — covenant infidelity as sexual unfaithfulness, the Hosea-Jeremiah metaphorical frame; <strong>מִצְהֲלוֹתַיִךְ</strong> (<em>mitzhalotayikh</em>, your lustful cries/neighings); <strong>זִמַּת זְנוּתֵךְ</strong> (<em>zimmah znutekh</em>, the obscene acts of your prostitution). The verdict: <strong>אוֹי לָךְ יְרוּשָׁלַם</strong> (<em>oy lakh Yerushalayim</em>, woe to you, Jerusalem) — covenant lament. Will you not be made clean? How long yet?</p>"
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
