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
  "47": {
    "1": "<p><strong>vayeshiveni el-petach habayit vehineh mayim yotzeim mitachat miftan habayit qadimah</strong>: 'He brought me back to the entrance of the house, and behold, water was flowing out from below the threshold of the house toward the east.' The temple river (<em>nahal</em>) originates beneath the temple threshold — specifically the south side of the threshold at the south side of the altar. The source is the sanctuary itself, not a natural spring. This is the theological crucial point: the life-giving water does not arise from the land or any natural source but from YHWH's own dwelling place. The direction — east (<em>qadimah</em>) — is eschatologically significant: it flows toward the Dead Sea (the Arabah), the most desolate region of the land, and toward the sunrise, the direction from which the divine glory returned (43:1-4).</p>",
    "2": "<p><strong>vayotzieni derech sha'ar tzafon</strong>: 'He brought me out by way of the north gate.' The guide leads Ezekiel out through the north gate and around the outside to the outer east gate, where he sees the water trickling (<em>mephakkim</em>) from the south side. The detail that Ezekiel must exit through the north gate and go around — rather than passing through the closed east gate — is consistent with 44:1-2 (the east gate is shut because YHWH has entered by it). The river flows past the east gate and away.</p>",
    "3": "<p><strong>beyetzet ha'ish qadim uqav biyado vayamad elef amot</strong>: 'As the man went out eastward with a measuring line in his hand, he measured a thousand cubits.' The four measurements of 1,000 cubits each (vv. 3-5) create a fourfold progressive deepening: <em>echel-hamaim</em> (ankle-water), <em>maim birkayim</em> (knee-water), <em>maim motnayim</em> (hip/waist-water), then impassable swimming depth. The 1,000-cubit intervals — approximately 500 meters — mark a journey of 4 kilometers from the temple, with each stage representing an exponential increase in the river's volume with no upstream tributaries visible. The quantitative impossibility signals the river's supernatural, divine character.</p>",
    "4": "<p><strong>vayamad elef vaya'avereni bamayim maim birkayim</strong>: 'He measured another thousand, and led me through the water — it was knee-deep.' The progression from ankle (<em>echel</em>) to knee (<em>birkayim</em>) continues. The personal nature of the journey — being led (<em>va'avereni</em> = he brought me through) — means Ezekiel experiences each stage physically, wading deeper. The incremental wading enacts the reader's increasing immersion in the vision's blessing: each step deeper is a step into greater divine abundance.</p>",
    "5": "<p><strong>vayamad elef nahal lo-uchal la'avor</strong>: 'He measured another thousand, and it was a river I could not cross.' The climax: what began as a trickle is now an impassable river (<em>nahal lo-uchal la'avor</em> = a river that cannot be crossed/forded). <em>Gavehu hamayim maie schia</em> (the waters had risen to swimming level) — the water that was trickling under the south threshold is now a great river requiring swimming. The quantitative impossibility is the point: no natural spring multiplies 1000-fold every 500 meters. This is creation-power applied to land renewal — YHWH's own life flowing out through his temple to heal the most cursed landscape on earth.</p>",
    "6": "<p><strong>vayomer elai hen-raita ben-adam</strong>: 'He said to me: Son of man, have you seen?' The rhetorical question invites Ezekiel — and through him the exilic audience — to register the wonder. The guide's question is not information-seeking but attention-directing: <em>have you seen this?</em> The pause at the riverbank before the explanation forces a moment of pure wonder before the theological articulation of what has been seen.</p>",
    "7": "<p><strong>beshuveni vehineh el-sefat hanachal etzim rabbim me'od</strong>: 'When I returned, I saw on the banks of the river very many trees on both sides.' The trees on both banks of the river are identified in v. 12 as fruit trees whose leaves do not wither and that bear fruit every month. Before the explanation comes the visual impression — an abundance of lush trees lining both banks of the river flowing through the Arabah's barren landscape. The <em>me'od</em> (very much/exceedingly) emphasizes the profusion: not a few trees but a forest of them.</p>",
    "8": "<p><strong>vayomer elai hamayim haeleh yotzeim el-gelilah haqadmonit veyardu el-haAravah</strong>: 'He said to me: These waters flow toward the eastern region and go down into the Arabah and enter the sea.' The destination is precise: the <em>Aravah</em> (the Jordan Valley rift below sea level, site of the Dead Sea) and <em>hayyam hammutzaim</em> (the sea that is brought out = the Dead Sea, so called because it is the stagnant terminal basin). <em>Umayim yeraphe'u</em> (and the waters will be healed/made fresh) — <em>raphe</em> (to heal) is the medical term for restoration to health. The healing of the Dead Sea is the ultimate geographical reversal: the most salt-saturated, lifeless water body on earth made fresh and teeming with life by the temple river.</p>",
    "9": "<p><strong>vehaya kol-nefesh chaya asher yishrots el kol asher yavo sham hanachalaim yichyeh</strong>: 'Every living creature that swarms, wherever the river goes, will live.' <em>Nefesh chaya</em> (living creature) is the same phrase used in Gen 1:20-21 and 2:7 for the living creatures of creation. The river creates new <em>bara</em>-level life wherever it flows — it is a creation event, not merely irrigation. <em>Vehayah ha-dagah rabbah meod</em> (the fish will be very many) — the Dead Sea, currently devoid of fish due to extreme salinity, will teem with fish in every variety (<em>ke-dagat hayam hagadol harbeh meod</em> = like the fish of the Great [Mediterranean] Sea, very many).</p>",
    "10": "<p><strong>ve'amdu alav daugim me-En-Gedi ve'ad En-Eglaim mishtoach lachemotayim</strong>: 'Fishermen will stand beside it from En-gedi to En-eglaim; it will be a place for spreading nets.' En-gedi (a spring-oasis on the western Dead Sea shore) and En-eglaim (probably at the northern end) mark the entire length of the Dead Sea's western shore. The Dead Sea — currently having no fishermen because it has no fish — will support commercial fishing operations along its entire length. <em>Leminehah tiheye</em> (each kind in its kind) — the taxonomic completeness of the fish population emphasizes the total renewal: every category of fish, not merely a few hardy species.</p>",
    "11": "<p><strong>biztzetav uvge'avav lo' yeraphe'u lamelach nittanu</strong>: 'But its swamps and marshes will not become fresh; they will be given over to salt.' This exception is theologically interesting: not everything is healed. The swamps and marshes at the Dead Sea's margins remain salty and will be used for salt production. Salt has covenant significance (Num 18:19; Lev 2:13: &ldquo;covenant of salt&rdquo;) and practical necessity. The exception preserves salt resources while still transforming the main sea body. It also introduces an element of eschatological realism: the new creation preserves functional continuity with present creation rather than annihilating it.</p>",
    "12": "<p><strong>ve'al hanachal ya'aleh el-sifato mizeh umizeh kol-etz-mazon</strong>: 'On the banks of the river, on both sides, will grow all kinds of food trees.' <em>Etz-mazon</em> (food/nourishment trees) — not ornamental but edible trees, trees that feed. The three characteristics (<em>lo yinbol alehav velo yitom piryov</em> = leaves will not wither, fruit will not fail) reverse the curse on creation (Gen 3:17-19: thorns, thistles, painful toil). <em>Lechadashehem yivkeh ki meimaiv min-hamiqdash hemah yotz'im</em> (they will bear fresh fruit each month, because their water flows from the sanctuary) — monthly fruit (not seasonal) and evergreen leaves are the marks of the eschatological Eden-restoration. Revelation 22:2 quotes this verse directly for the new creation.</p>",
    "13": "<p><strong>koh amar adonai YHWH ze gevul asher titnahaluh et-haarets</strong>: 'Thus says the Lord YHWH: This is the boundary by which you shall apportion the land as inheritance.' The transition from the visionary river to the land-allotment legislation (<em>nachalah</em> = inheritance, ancestral possession) is abrupt but theologically coherent: the river vision establishes the life-giving character of the land to which the tribes will return. <em>Yosef chavalim</em> (Joseph shall have two portions/lots) — this gives Ephraim and Manasseh each their own portion in the land, fulfilling Jacob's adoption of Joseph's sons in Gen 48:5.</p>",
    "14": "<p><strong>unechaltem oto ish kechiv</strong>: 'You shall divide it equally, each the same as his brother.' The equal distribution (<em>ish kechiv</em> = one like his neighbor, equally) removes the tribal inequalities of the historical settlement (where Judah received disproportionately large territory and some tribes received inadequate portions). <em>Nasati et-yadi latheta otah laavoteichem</em> (I raised my hand to give it to your ancestors) — the divine oath formula authenticates the allotment: this land distribution is the fulfillment of the Abrahamic covenant promise, not a new political arrangement.</p>",
    "15": "<p><strong>vezeh gevul haaretz ligvul tzafon</strong>: 'This shall be the northern boundary of the land.' The northern boundary runs from the Mediterranean Sea (<em>hayam hagadol</em>) by the road of Hethlon toward Lebo-hamath and Zedad. This boundary is similar to but not identical with the historical land boundaries — it is a divinely specified ideal land, not a historical reconstruction. <em>Lebo-Hamath</em> (the entrance of Hamath) is the traditional northern marker of the Promised Land (Num 34:8; 1 Kgs 8:65).</p>",
    "16": "<p><strong>Chamat Berota Sivrayim</strong>: 'Hamath, Berothah, Sibraim.' The precise place names — Berothah, Sibraim, Hazer-hatticon, Hauran — trace the northern boundary through the Damascus-Hamath region. The precision of the geographic specification (even if some locations are uncertain to modern scholars) communicates that the eschatological land is a real geographic space, not a purely spiritual abstraction. The vision's realism — actual place names, measurable dimensions, fishermen and farmers — is Ezekiel's insistence that YHWH's promises are materially concrete.</p>",
    "17": "<p><strong>vehayah gevul min-hayam Chatzar-Einan</strong>: 'The boundary shall run from the sea to Hazar-enan.' The northern boundary terminates at Hazar-enan, on the northern edge of Damascus's border territory. <em>Gevul Chamat tzafonah</em> (with Hamath's border to the north) — the boundary is carefully calibrated to the east-west extent of the northern region. The land described is larger than any historically realized Israelite territory, corresponding to the <em>ideal</em> land promised to Abraham (Gen 15:18: from the Nile to the Euphrates) without being identical to it.</p>",
    "18": "<p><strong>vepeat qadim mibeyn Hauran umibeyn Dammesheq</strong>: 'The east side: between Hauran and Damascus.' The Jordan River (<em>hayarden</em>) forms the eastern boundary from the north (Hauran/Damascus region) down to the eastern sea (the Dead Sea or Gulf of Aqaba). The use of the Jordan as eastern boundary reflects the historical land's eastern limit, though Transjordan is now included in the tribal allotments (in contrast to the historical settlement where the eastern tribes held Transjordanian territory as a secondary arrangement).</p>",
    "19": "<p><strong>vepeat negev teiman mitamar ad-mei Merivat-Qadesh</strong>: 'The south side: from Tamar to the waters of Meribah-kadesh.' The southern boundary runs from Tamar (near En-gedi) through Meribah-kadesh (near Kadesh-barnea, the wilderness staging ground) to the Brook of Egypt (<em>nachal Mitzraim</em> = the Wadi el-Arish). This follows the traditional southern boundary of the Promised Land (Num 34:3-5). The inclusion of Meribah-kadesh (the place of Israel's rebellion: Num 20:13; Ps 95:8) in the restored land's boundary marks the redemption of a place associated with faithlessness.</p>",
    "20": "<p><strong>vepeat yam hayam hagadol miggevul ad-nokhach levo-Chamat</strong>: 'The west side: the Great Sea [Mediterranean] from the southern boundary to the entrance of Hamath.' The western boundary is the simplest: the Mediterranean coastline from south to north. The land's four boundaries — north (Hamath region), east (Jordan), south (Negev/Sinai), west (Mediterranean) — form a comprehensive and generous land grant that exceeds historical Israel's settled territory and fulfills the Abrahamic promise of a great land from the river to the sea.</p>",
    "21": "<p><strong>uchalqetem et-haarets hazot lachem leshivtei Yisrael</strong>: 'You shall divide this land among yourselves according to the tribes of Israel.' The distribution is tribal — the twelve-tribe structure of Israel is preserved in the eschatological land allotment, connecting the restoration to the foundational covenant structure (the twelve sons of Jacob, cf. Gen 49). The land is for the tribes of Israel, but vv. 22-23 immediately extend this.</p>",
    "22": "<p><strong>vehaya tachelqu otah benahalah lachem ulgerim hagarim betochechem</strong>: 'You shall apportion it as an inheritance for yourselves and for the resident aliens who live among you.' The inclusion of the <em>ger</em> (resident alien, sojourner) in the tribal inheritance is a significant extension of the historical Torah's treatment of aliens. While the Torah protected aliens and required equal justice for them, it did not give them tribal land inheritance. Here, aliens who have had children in Israel (<em>asher holedu vanim betochechem</em>) receive land <em>like native Israelites</em> (<em>vegeru batochem yihyu lachem ke'ezrach</em>). This is the eschatological fulfillment of the universal reach of covenant blessing.</p>",
    "23": "<p><strong>vehaya bashevet asher gar hasham haager titenu nachalato</strong>: 'In whatever tribe the sojourner resides, there you shall give him his inheritance.' The alien's inheritance is located with the specific tribe where he lives — not a separate zone but integrated into tribal territory. <em>Ne'um adonai YHWH</em> — the divine declaration seals the unprecedented provision. This prophetic extension of covenant inheritance to resident aliens anticipates Paul's argument in Galatians and Ephesians that Gentiles in Christ are fellow-heirs and members of the covenant household.</p>"
  },
  "48": {
    "1": "<p><strong>ve'eleh shemot hashvatim miqtzei tzafon</strong>: 'These are the names of the tribes: beginning from the north.' The tribal allotments are described from north to south in strips running the full width of the land from the eastern to the western border (<em>mipeat qadimah el-yam</em> = from the east side to the sea). The northernmost tribes (Dan, Asher, Naphtali, Manasseh, Ephraim, Reuben, Judah) are placed north of the sacred central zone; the southern tribes (Benjamin, Simeon, Issachar, Zebulun, Gad) are placed south of it. The arrangement differs significantly from the historical tribal territory allocation in Joshua.</p>",
    "2": "<p><strong>ve'al gevul Dan mipeat qadimah ad-peat yamah Asher echad</strong>: 'Adjoining Dan's territory, from east to west: Asher, one portion.' The formula <em>mipeat qadimah ad-peat yamah</em> (from the east side to the sea side) applies to every tribal allotment — each tribe receives a horizontal strip spanning the full width of the land. This equal-width distribution replaces the historical irregular allotments with geometrically equal portions, expressing the divine equity that characterizes the eschatological order.</p>",
    "3": "<p><strong>ve'al gevul Asher Naphtali echad</strong>: 'Adjoining Asher: Naphtali, one portion.' The formulaic repetition of the allotment descriptions — each tribe receiving one portion, each described in the same brief formula — emphasizes the equality of the distribution. The tribal order (Dan, Asher, Naphtali, Manasseh, Ephraim, Reuben, Judah from north to south) is not the birth order of the sons of Jacob but a divinely specified arrangement that places Judah immediately adjacent to the sacred central zone.</p>",
    "4": "<p><strong>ve'al gevul Naphtali Menasheh echad</strong>: 'Adjoining Naphtali: Manasseh, one portion.' Manasseh is placed above Ephraim, reversing the birth-order blessing of Gen 48:14-19 where Jacob crossed his hands to give Ephraim (the younger) the greater blessing. In Ezekiel's eschatological arrangement, the historical reversals are resolved: Manasseh occupies a portion slightly north of Ephraim (his younger brother), and both receive equal single portions rather than the double portion implied by Joseph's double-inheritance.</p>",
    "5": "<p><strong>ve'al gevul Menasheh Ephraim echad</strong>: 'Adjoining Manasseh: Ephraim, one portion.' Ephraim — the northern kingdom's leading tribe after the split, associated with the Israelite apostasy Ezekiel had condemned — receives a portion in the restored land alongside Judah. The inclusion of the northern tribes in the eschatological allotment is the fulfillment of the reunification promise of 37:15-22 (the two sticks joined into one in Ezekiel's hand).</p>",
    "6": "<p><strong>ve'al gevul Ephraim Reuven echad</strong>: 'Adjoining Ephraim: Reuben, one portion.' Reuben, the firstborn who lost his preeminence (Gen 49:3-4; Deut 33:6), receives a full portion equal to all other tribes. The historical diminishment of Reuben's significance (the tribe became numerically small and historically marginal) is reversed in the eschatological allotment — primogeniture curses are dissolved in the new order.</p>",
    "7": "<p><strong>ve'al gevul Reuven Yehudah echad</strong>: 'Adjoining Reuben: Judah, one portion.' Judah is placed immediately north of the sacred central zone (the terumah). This is the most theologically significant placement: Judah as the royal-messianic tribe (Gen 49:10) flanks the sacred precinct on its north side, as Benjamin (the tribe of the Jerusalem temple's historical location) flanks it on the south. The arrangement places the two most significant covenant tribes on either side of YHWH's dwelling place.</p>",
    "8": "<p><strong>ve'al gevul Yehudah mipeat qadimah ad-peat yamah tihyeh haterumah</strong>: 'Adjoining Judah, from east to west, shall be the contribution [sacred portion].' <em>Terumah</em> (contribution, elevated/lifted offering) is the term for the sacred central strip. The same width as the tribal allotments (east to west) but of specified length (25,000 cubits wide). The sanctuary (<em>hamiqdash</em>) is at the center of this sacred zone. The word <em>terumah</em> for land — normally used for grain offerings lifted to YHWH — applies the concept of the elevated gift to sacred territory: this central strip is Israel's land-offering to YHWH.</p>",
    "9": "<p><strong>haterumah asher tarimun laYHWH orech esrim ve'chamesh elef</strong>: 'The offering you shall set apart for YHWH shall be twenty-five thousand cubits in length.' The sacred portion measures 25,000 × 20,000 cubits (approximately 12.5 × 10 km). Within this zone the priests' territory (25,000 × 10,000), the Levites' territory (25,000 × 10,000), and the city territory (25,000 × 5,000) are arranged in horizontal strips. The sacred central zone is the architectural heart of the entire land distribution — everything else is organized around it.</p>",
    "10": "<p><strong>uleileh tihyeh terumah haqodesh lakohanim</strong>: 'For the priests shall be the holy contribution.' The priestly allocation — 25,000 × 10,000 cubits — has YHWH's sanctuary (<em>miqdash YHWH</em>) at its center (<em>betoch</em>). The Zadokite priests receive the central strip closest to the sanctuary. The physical geography of the sacred zone mirrors the holiness hierarchy: the sanctuary at the center, surrounded by the priests' territory, surrounded by the Levites' territory, with the city on the south perimeter.</p>",
    "11": "<p><strong>lakohanim hamequdash mibeni Tzadoq</strong>: 'For the consecrated priests, the sons of Zadok.' The explicit designation of the Zadokite priests (<em>beni Tzadoq</em>) as the holders of the central priestly territory is the eschatological vindication of their covenant faithfulness. <em>Asher shamru et-mishmarti</em> (who kept my charge) — the historical Zadokites remained loyal during Israel's apostasy when &ldquo;the Levites went astray&rdquo; (44:10-15). The land allotment permanently memorializes the principle: faithfulness in the historical order carries forward into the eschatological order.</p>",
    "12": "<p><strong>vehayeta lahem terumiyah min-terumiat haaretz</strong>: 'It shall be theirs as a special portion within the land's contribution.' The priestly portion is a <em>terumiyah</em> (a lifted portion within the larger terumah) — the most holy section (<em>qodesh qodashim</em>) of the entire land. The spatial language of elevation (<em>terum-</em>) applied to the priestly land mirrors the sacrificial language of elevated offerings: just as the choicest parts of the sacrifice are lifted to YHWH, the choicest portion of the land is reserved for his sanctuary servants.</p>",
    "13": "<p><strong>velaleviim kemodat hakohanim</strong>: 'And the Levites shall have a portion alongside the priests.' The Levites receive an equivalent strip (25,000 × 10,000 cubits), equal in size to the priestly portion but immediately adjacent to it rather than centering the sanctuary. The total sacred zone width is thus 20,000 cubits (priests 10,000 + Levites 10,000), with the city's 5,000-cubit strip making the complete 25,000-cubit terumah.</p>",
    "14": "<p><strong>velo yimkeru mimenu velo yamiru velo ya'avir reshit haaretz</strong>: 'They shall not sell or exchange any of it; they shall not transfer the prime portion of the land.' The prohibition against selling the sacred land (<em>lo yimkeru, lo yamiru, lo ya'avir reshit haaretz ki qodesh laYHWH</em>) is an eschatological version of the Jubilee land laws (Lev 25:23: &ldquo;the land shall not be sold in perpetuity, for the land is mine&rdquo;). The sacred central zone is permanently inalienable — it belongs to YHWH, and the use of it by priests and Levites is stewardship, not ownership.</p>",
    "15": "<p><strong>vachamesh alafim hanot'rim barochav</strong>: 'The remaining five thousand cubits in width.' The city strip (25,000 × 5,000 cubits) is for <em>chol</em> (common/profane use) — housing, open pasture, and the city itself. The distinction <em>chol</em> (common) versus <em>qodesh</em> (holy) is not a spiritual demotion but a functional category: the city zone serves the practical needs of Israel's population rather than the specifically cultic functions of the priestly and Levitical zones.</p>",
    "16": "<p><strong>ve'eleh midoteiha peat tzafon chamesh meot ve'arba elafim</strong>: 'These shall be the city's measurements: on the north, 4,500 [cubits].' The eschatological city is a perfect square — 4,500 × 4,500 cubits on all four sides. The perfect-square geometry (<em>arbaat tefachim</em>) matches the inner court's perfect square (47:47) and anticipates the New Jerusalem's four-square description in Rev 21:16. The mathematical precision of the city's dimensions communicates divine perfection — this is not a human city laid out by planners but YHWH's ideal city.</p>",
    "17": "<p><strong>vehayah migrash ha'ir tzafon me'atayim vachamishim</strong>: 'The city shall have open land: 250 cubits on each side.' The <em>migrash</em> (open land, pastureland) around the city is 250 cubits on all four sides — a buffer zone between the city proper and the agricultural land. This open land provision is consistent with Levitical city regulations (Num 35:4-5) where a 2,000-cubit open area surrounded Levitical towns. The city is not crowded to its boundaries but has breathing space — a mark of abundance and order in the divine plan.</p>",
    "18": "<p><strong>vehaNot'ar beorekh leumat terumah haqodesh</strong>: 'What remains in length alongside the holy portion.' The agricultural land flanking the city — 10,000 cubits east and 10,000 cubits west — will produce food for the city's workers (<em>avodat ha'ir</em>). The integration of agricultural productivity with the sacred zone and city ensures that the eschatological community is self-sustaining: the land itself supports the city that serves the sanctuary. There is no tension between sacred and agricultural space — they are architecturally integrated.</p>",
    "19": "<p><strong>ve'ovdei ha'ir min-kol-shivtei Yisrael ya'avduha</strong>: 'The workers of the city shall cultivate it — workers from all the tribes of Israel.' The city's agricultural land is worked by representatives from all twelve tribes, not by a single tribe. This inter-tribal character of the city workforce mirrors the twelve gates named after all twelve tribes (vv. 31-34) — the eschatological city belongs equally to all Israel, transcending the historical tribal divisions that had fragmented the covenant community.</p>",
    "20": "<p><strong>kol-haterumah esrim vachamesh elef besrim vachamesh elef ravia'it taqrivu</strong>: 'The entire offering is 25,000 by 25,000 cubits — a square.' The complete terumah zone is a perfect square: 25,000 × 25,000 cubits. This perfect square encompasses the priestly territory, Levitical territory, and city territory together. The geometric perfection of the sacred zone — a square within the land's horizontal strips — creates a visually centered structure: the perfect square of YHWH's dwelling in the middle of the horizontal tribal strips stretching from sea to Jordan.</p>",
    "21": "<p><strong>vehanot'ar lanasi</strong>: 'What remains shall be for the prince.' The <em>nasi</em> (prince, leader — the royal figure who is not called <em>melech</em>/king in the eschatological vision, cf. 34:24; 37:25) receives the territory on both sides of the sacred zone — east of it to the eastern border and west of it to the Mediterranean. The prince's territory flanks the entire sacred zone on both sides. This arrangement ensures that the prince's land is defined relative to YHWH's sanctuary, not the reverse — YHWH's dwelling is primary, the prince's territory secondary.</p>",
    "22": "<p><strong>umitoch achuzat halevi'im umitoch achuzat ha'ir betoch asher lanasi</strong>: 'From between the Levites' possession and the city's possession — in the middle of the prince's territory.' The Judah-Benjamin boundary section that contains the sacred zone and city falls within the prince's territory, but the sacred portions are excluded from his ownership. This architectural arrangement prevents the king from appropriating the sacred zone — a structural safeguard against the kind of royal abuse of sacred space that characterized the historical monarchy (cf. the complaint of 43:7-9 against the kings' proximity to YHWH's threshold).</p>",
    "23": "<p><strong>veha'shet hashvatim hanot'rim</strong>: 'As for the remaining tribes.' The southern tribes (Benjamin through Gad, vv. 23-27) occupy the strips south of the sacred central zone. Benjamin is placed immediately south of the sacred zone — the historical location of Jerusalem's earliest territory — giving Benjamin the honor of flanking the divine dwelling place from the south as Judah does from the north.</p>",
    "24": "<p><strong>ve'al gevul Binyamin mipeat qadimah ad-peat yamah Shim'on echad</strong>: 'Adjoining Benjamin, from east to west: Simeon, one portion.' Simeon — historically the tribe that dispersed within Judah's territory (Josh 19:1; Gen 49:7: &ldquo;I will divide them in Jacob&rdquo;) — receives its own defined territory in the eschatological order. The reversal of Jacob's curse on Simeon (Gen 49:5-7) in the restored order is one of the subtle signals that the eschatological allotment is not merely political reorganization but covenant renewal that undoes historical judgments.</p>",
    "25": "<p><strong>ve'al gevul Shim'on Yissachar echad</strong>: 'Adjoining Simeon: Issachar, one portion.' Issachar and Zebulun (v. 26) — the two tribes of Leah's sons who are historically associated with the northern region — are placed in the south in Ezekiel's eschatological arrangement. The tribal placement throughout (north and south of the sacred zone) does not simply replicate historical geography but creates a new order centered entirely on the sanctuary, with tribes repositioned according to the logic of the new spatial center.</p>",
    "26": "<p><strong>ve'al gevul Yissachar Zevulun echad</strong>: 'Adjoining Issachar: Zebulun, one portion.' Zebulun completes the series of Leah-tribe allotments. The placement of Issachar and Zebulun in the south is notable because Isa 9:1 specifically prophecies honor for &ldquo;the land of Zebulun and the land of Naphtali&rdquo; (the first territories darkened by Assyrian invasion) — a prophecy Matthew applies to Jesus's Galilean ministry (Matt 4:15-16). The Ezekielian placement of Zebulun and Naphtali on opposite ends of the tribal arrangement (Naphtali in the north, Zebulun in the south) reflects a different geographical logic.</p>",
    "27": "<p><strong>ve'al gevul Zevulun Gad echad</strong>: 'Adjoining Zebulun: Gad, one portion.' Gad — historically a Transjordanian tribe (Josh 13:24-28) — receives the southernmost strip of the eschatological land. This placement replaces the Transjordanian wilderness territory of the historical Gadites with fertile Cisjordanian land within the sacred borders, completing the reversal of Transjordanian marginality. All twelve tribes are within the ideal land's borders, equally endowed with east-to-sea strips.</p>",
    "28": "<p><strong>ve'al gevul Gad el-peat negev teimah vehayah gevul mitamar mei Merivat-Qadesh nachlah hayam hagadol</strong>: 'On the south side of Gad, the boundary runs from Tamar to the waters of Meribah-kadesh, then along the Brook of Egypt to the Great Sea.' The southern boundary of the entire land is confirmed through the description of Gad's southern border: from Tamar through Meribah-kadesh to the Wadi el-Arish and the Mediterranean. This matches the southern boundary of 47:19, closing the land description symmetrically.</p>",
    "29": "<p><strong>zot haaretz asher tapilu benahalah leshivtei Yisrael</strong>: 'This is the land you shall distribute by lot as an inheritance among the tribes of Israel.' The summary formula closes the land allotment. <em>Ve'eleh machlekotam ne'um adonai YHWH</em> (these are their portions, declares the Lord YHWH) — the divine declaration authenticates the entire allotment as divinely specified. The present tense (<em>tapilu</em> = you shall allot) frames the allotment as a future act to be performed, not merely a vision of the past.</p>",
    "30": "<p><strong>ve'eleh totzaot ha'ir mipeat tzafon</strong>: 'These shall be the exits/gates of the city on the north side.' <em>Totzaot</em> (exits, outlets) refers to the city gates, each named after a tribe. The northern wall has three gates (Reuben, Judah, Levi), the eastern wall three (Joseph, Benjamin, Dan), the southern wall three (Simeon, Issachar, Zebulun), and the western wall three (Gad, Asher, Naphtali) — twelve gates for twelve tribes. The naming of the city gates after all twelve tribes, including Levi (who had no land allotment in the historical settlement) and using Joseph (single name) rather than Ephraim/Manasseh to preserve the twelve, is the eschatological restoration of Israel's complete tribal identity.</p>",
    "31": "<p><strong>vesha'arei ha'ir al-shemot shivtei Yisrael</strong>: 'The city's gates shall be named after the tribes of Israel.' The three northern gates are: gate of Reuben, gate of Judah, gate of Levi. Levi's inclusion in the city gates (rather than a territorial allotment) is consistent with the Levites' sacral role — they receive the sacred zone territory but also have a named gate of access to the city. Revelation 21:12 derives its twelve named gates from this passage, applying the Ezekielian vision to the New Jerusalem.</p>",
    "32": "<p><strong>vepeat qadimah chamesh meot ve'arba alafim ushlosha sha'arim</strong>: 'On the east side: 4,500 cubits, three gates.' The eastern gates: Joseph, Benjamin, Dan. Joseph as a single name (not Ephraim and Manasseh separately) preserves the twelve-gate count while honoring Joseph's covenant significance. The arrangement of tribes around the four walls has no clear pattern derived from the Pentateuchal tribal groupings — it is a new arrangement for a new city.</p>",
    "33": "<p><strong>vepeat negev chamesh meot ve'arba alafim midah ushlosha sha'arim</strong>: 'On the south side: 4,500 cubits in measurement, three gates.' The southern gates: Simeon, Issachar, Zebulun — three of the Leah-tribe sons. The distribution of Leah's sons across all four walls (Reuben and Judah on the north, Simeon/Issachar/Zebulun on the south) balances the matriarchal tribes around the city's perimeter.</p>",
    "34": "<p><strong>peat yamah chamesh meot ve'arba alafim ushlosha sha'arim</strong>: 'The west side: 4,500 cubits, three gates.' The western gates: Gad, Asher, Naphtali — the sons of the handmaidens Zilpah and Bilhah. The placement of the handmaid-tribe sons on the western wall is the final element in the complete perimeter. Every tribe has a named gate; no tribe is excluded from access to the eschatological city. The walls' total perimeter (4 × 4,500 = 18,000 cubits) matches the explicit statement of v. 35.</p>",
    "35": "<p><strong>saviv shmoneh asar elef vesheme ha'ir miyom YHWH shammah</strong>: 'The circumference shall be eighteen thousand cubits. And the name of the city from that day shall be: YHWH-Shammah.' <em>YHWH shammah</em> (YHWH Is There) is the climactic final verse of Ezekiel and the resolution of the book's central crisis. The book opened with the divine glory departing the defiled temple (chs. 8-11) — its entire theological energy has been directed toward the question of whether YHWH would return to dwell among his people. The answer is given in two words: YHWH Is There. The city name is not a human honorific but a divine state of affairs — YHWH's presence is the defining characteristic of the eschatological city. The NT's echo: Revelation 21:3 (&ldquo;the dwelling place of God is with man&rdquo;) and 22:3-4 (&ldquo;the throne of God and of the Lamb will be in it, and his servants will worship him; they will see his face&rdquo;) are both direct fulfillments of YHWH-Shammah.</p>"
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
