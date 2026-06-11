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
    "1": "<p>A direct revelation: 'Then he brought me back to the door of the temple and behold water was issuing from below the threshold of the temple toward the east — for the temple faced east — and the water was flowing down from below the south end of the threshold of the temple, south of the altar.' The river of life flowing from the threshold of the temple — from the eastward-facing door, the direction of the divine glory's return (43:1-5). The source of life is the divine presence. In the NT, the source is identified personally: &ldquo;On the last day of the feast, the great day, Jesus stood up and cried out, &lsquo;If anyone thirsts, let him come to me and drink&rsquo;&rdquo; (John 7:37). Christ is the temple from whom the living water flows (John 2:19-21; 7:38-39; Rev 22:1).</p>",
    "2": "<p>A structural note: 'He brought me out by way of the north gate and led me around on the outside to the outer gate that faces toward the east; and behold the water was trickling out on the south side.' The measuring man leads Ezekiel out to observe the river from the outside. The vision of the temple-river requires both an interior source (the divine presence) and an exterior flow (the life-giving effect on the surrounding world). The pattern of interior-then-exterior corresponds to the Spirit's work: given within (Ezek 36:27; John 14:17) and then flowing out (Acts 2; John 7:38-39).</p>",
    "3": "<p>A pattern: 'Going on eastward with a measuring line in his hand the man measured a thousand cubits and then led me through the water and it was ankle-deep.' Ankle-deep: the first measure of the river. The graduated depth of Ezekiel's river — ankle, knee, waist, unswimmable — is the NT's pattern for the Spirit's expanding work. The initial measure is real but limited: a trickle from the threshold, a stream barely covering the feet. Every genuine work of the Spirit begins small. The mustard seed (Matt 13:31-32), the leaven in three measures of flour (Matt 13:33), the single grain of wheat (John 12:24) — all begin from imperceptible origins toward overwhelming fullness.</p>",
    "4": "<p>A pattern: 'Again he measured a thousand and led me through the water and it was knee-deep. Again he measured a thousand and led me through the water and it was waist-deep.' Knee-deep, then waist-deep: the river grows at each thousand-cubit measurement. The progression is not gradual but stepped — each interval produces a new depth, a qualitative advance. This pattern appears in the history of the gospel: Pentecost (trickle), the Gentile mission (knee-deep), the expansion through the Roman Empire (waist-deep). Each advance is YHWH's doing, not human strategy. &ldquo;The earth will be filled with the knowledge of the glory of YHWH as the waters cover the sea&rdquo; (Hab 2:14).</p>",
    "5": "<p>A direct revelation: 'Again he measured a thousand and it was a river that I could not pass through, for the water had risen. It was deep enough to swim in, a river that could not be passed through.' The unswimmable river — the fullness of the Spirit overflowing all human control. The river that began as a trickle is now a torrent. This progression is the eschatological fullness that the Spirit's work is moving toward: &ldquo;rivers of living water&rdquo; (John 7:38) beyond any individual's containment. The day is coming when the Spirit's power will be as universal and uncontrollable as a flooding river — the consummation of what Pentecost began.</p>",
    "6": "<p>A structural note: 'And he said to me, &ldquo;Son of man, have you seen this?&rdquo; Then he led me back to the bank of the river.' The measuring man pauses to ask whether Ezekiel has truly seen — the prophetic question that invites the prophet (and through him, the reader) to grasp the significance of the vision. The question &ldquo;have you seen this?&rdquo; is the call to sustained contemplation. Jesus's &ldquo;he who has ears to hear, let him hear&rdquo; (Matt 13:9) is the same invitation: the vision is given; the seeing must be active.</p>",
    "7": "<p>A structural note: 'As I went back I saw on the bank of the river very many trees on one side and on the other.' Trees on both banks — the first sign of the river's life-giving effect. The landscape is transforming as the water flows. The trees anticipate the detailed description of verse 12 (fruit trees, never withering, fresh leaves, medicinal) and reach their fullest expression in Rev 22:2: &ldquo;the tree of life with its twelve kinds of fruit, yielding its fruit each month. The leaves of the tree were for the healing of the nations.&rdquo;</p>",
    "8": "<p>A direct revelation: 'And he said to me, &ldquo;This water flows toward the eastern region and goes down into the Arabah and enters the sea; when the water flows into the sea, the water will become fresh.&rdquo;' The river flows into the Dead Sea — the most lifeless body of water in the known world, hyper-saline, devoid of fish — and makes it fresh. This is resurrection imagery: life entering the realm of death and transforming it. The Dead Sea becoming fresh is the OT type of what Christ's resurrection brings: the entry of the living God into the realm of death (1 Pet 3:18-20) transforming it from within. &ldquo;Death is swallowed up in victory&rdquo; (1 Cor 15:54).</p>",
    "9": "<p>A type: 'And wherever the river goes, every living creature that swarms will live, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes.' The eschatological temple-river of Ezekiel's vision, increasingly deep and life-giving, is the OT type for the water that flows from Christ. Jesus at Tabernacles (John 7:38-39) applies the Spirit-water promise to himself: &ldquo;rivers of living water will flow from within him&rdquo; — and John explains this is the Spirit. Revelation's new creation river (22:1) flowing from the throne of God and the Lamb completes the Ezekiel type: the new temple's river is Christ himself, and all who drink from him live.</p>",
    "10": "<p>A type: 'Fishermen will stand beside the sea. From En-gedi to En-eglaim it will be a place for spreading nets. Its fish will be of very many kinds, like the fish of the Great Sea.' Fishermen on the banks of the healed Dead Sea spreading their nets — the apostolic mission in type. Jesus calls his disciples at the Sea of Galilee: &ldquo;Follow me and I will make you fishers of men&rdquo; (Matt 4:19). The healed Dead Sea teeming with fish is the world transformed by the gospel, and the fishermen casting nets are those whom Christ calls to gather the harvest. The same river that makes the waters fresh also fills the nets.</p>",
    "11": "<p>A structural note: 'But its swamps and marshes will not become fresh; they are to be left for salt.' The swamps and marshes — the stagnant backwaters not connected to the river's flow — remain salt. Even in the eschatological restoration, divine sovereignty includes judgment: not everything is healed, not by failure of the river's power but by the deliberate reservation of certain places for salt. The mystery of divine election persists even in the new creation. The river of life is sufficient to heal everything; whether everything receives it is the question that the NT addresses in its teaching on hardness of heart (Mark 3:5; Rom 11:25).</p>",
    "12": "<p>A direct revelation: 'And on the banks on both sides of the river there will grow all kinds of trees for food. Their leaves will not wither nor their fruit fail, but they will bear fresh fruit every month because the water for them flows from the sanctuary. Their fruit will be for food and their leaves for healing.' The tree of life — here multiplied into all kinds of trees on both banks, bearing fruit every month, with leaves for healing. Revelation 22:2 quotes this almost verbatim: &ldquo;the tree of life with its twelve kinds of fruit, yielding its fruit each month. The leaves of the tree were for the healing of the nations.&rdquo; Ezekiel's temple-river vision is the direct source for the new creation's arboretum. Christ is the one from whom this life flows (John 15:5: &ldquo;I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit&rdquo;).</p>",
    "13": "<p>A structural note: 'Thus says the Lord GOD: These are the boundaries by which you shall divide the land for inheritance among the twelve tribes of Israel. Joseph shall have two portions.' The tribal allotment section (47:13-48:35) returns to the covenantal framework: the land is YHWH's gift, divided equitably among the tribes, with Joseph receiving a double portion (honoring the Manasseh/Ephraim split) and Levi receiving no land (they have YHWH as their portion, Num 18:20). The ordered distribution of the land points toward the ordered inheritance of the new creation: &ldquo;Blessed are the meek, for they shall inherit the earth&rdquo; (Matt 5:5).</p>",
    "14": "<p>A structural note: 'You shall divide it equally; I swore to give it to your fathers and this land shall fall to you as your inheritance.' The equal division — each tribe receiving an equitable allotment regardless of size — is the eschatological reversal of Canaan's historical allocation (which was by lot and varied by population). The oath to the fathers (Gen 12:7; 15:18-21) is honored. YHWH's promises to Abraham, Isaac, and Jacob reach their final form in this vision. The NT applies the Abrahamic inheritance to all who are in Christ: &ldquo;if you are Christ's, then you are Abraham's offspring, heirs according to promise&rdquo; (Gal 3:29).</p>",
    "15": "<p>A structural note: 'This shall be the boundary of the land: On the north side from the Great Sea by way of Hethlon to Lebo-hamath and on to Zedad.' The northern boundary of the ideal land extends beyond any historical Israelite territory — from the Mediterranean to Hamath in modern Syria. The eschatological boundaries exceed the historical. The pattern appears throughout the NT's vision of the new creation: what God promised exceeds what was historically achieved. The &ldquo;land&rdquo; that Hebrews 11 says the patriarchs were seeking was &ldquo;a better country, that is a heavenly one&rdquo; (Heb 11:16).</p>",
    "16": "<p>A structural note: 'Berothah, Sibraim which is on the border between Damascus and Hamath, as far as Hazer-hatticon which is on the border of Hauran.' The northern boundary in geographic detail — the kind of specificity that appears in the Numbers boundary descriptions (Num 34:7-9). The precision of the eschatological geography signals that Ezekiel's vision is not allegory but territorial promise: a real land, with real boundaries, for a real people. The NT's &ldquo;new earth&rdquo; (Rev 21:1) is the ultimate form of this territorial promise — specific, real, and enduring.</p>",
    "17": "<p>A structural note: 'So the boundary shall run from the sea to Hazar-enan, which is on the northern border of Damascus, with the border of Hamath to the north. This shall be the north side.' The triple repetition of boundaries (verse 15-17 for the north) reflects the careful legal precision of the covenant document. Boundaries that are unclear lead to conflict; YHWH's allotment is unambiguous. The precision points toward the clarity of the new creation's inheritance: &ldquo;this is what I have prepared for you&rdquo; — a specific, uncontested gift.</p>",
    "18": "<p>A structural note: 'On the east side between Hauran and Damascus; along the Jordan between Gilead and the land of Israel; to the eastern sea and as far as Tamar. This shall be the east side.' The eastern boundary along the Jordan — the traditional boundary between Israel and the surrounding nations. The Jordan is the liminal space in Israel's history: crossed at the conquest (Josh 3), the boundary of Elijah's ministry, the site of Jesus's baptism (Matt 3:13-17). The eastern boundary in the eschatological vision passes through the same terrain where the Spirit descended on Jesus and the Father's voice declared: &ldquo;This is my beloved Son, with whom I am well pleased.&rdquo;</p>",
    "19": "<p>A structural note: 'On the south side it shall run from Tamar as far as the waters of Meribah-kadesh from there along the Brook of Egypt to the Great Sea. This shall be the south side.' The southern boundary runs from Tamar to Kadesh-barnea to the Wadi of Egypt — the traditional southern border of Canaan. Kadesh-barnea is the site of Israel's greatest failure (Num 13-14: the spies' report, the refusal to enter, the forty-year wilderness sentence). That the eschatological boundary passes through Kadesh signals that the sites of Israel's failures are redeemed in the final restoration: no place of past disobedience is excluded from the new inheritance.</p>",
    "20": "<p>A structural note: 'On the west side the Great Sea shall be the boundary to a point opposite Lebo-hamath. This shall be the west side.' The Mediterranean as the western boundary — the sea that Israel never fully controlled but that marks the natural western limit of the promised land. The sea as boundary, not enemy: in Ezekiel's vision, Israel's territory is bounded and defined, secure within its borders. In Revelation's new creation, &ldquo;the sea was no more&rdquo; (Rev 21:1) — not because the sea is abolished but because the sea-as-boundary and sea-as-chaos is no longer needed when the new creation is fully realized.</p>",
    "21": "<p>A structural note: 'So you shall divide this land among you according to the tribes of Israel.' The command to divide sets the framework for chapter 48's detailed allotment. The divine command to divide the land is covenantal: the land is YHWH's to give, the tribes are YHWH's people, and the division is his act. The NT equivalent: &ldquo;In my Father's house are many rooms. If it were not so, would I have told you that I go to prepare a place for you?&rdquo; (John 14:2). The eschatological inheritance is specifically prepared and specifically distributed.</p>",
    "22": "<p>A pattern: 'You shall allot it as an inheritance for yourselves and for the sojourners who reside among you and have had children among you. They shall be to you as native-born children of Israel. With you they shall be allotted an inheritance among the tribes of Israel.' Foreigners who have lived among Israel and raised their children in the land receive a full inheritance alongside native Israelites — the most radical land-inclusion clause in the Torah-prophetic corpus. The Gentile inclusion in Israel's land-inheritance is the OT anticipation of Paul's &ldquo;there is neither Jew nor Greek ... you are all one in Christ Jesus ... heirs according to promise&rdquo; (Gal 3:28-29). The eschatological land includes those who came from outside.</p>",
    "23": "<p>A structural note: 'In whatever tribe the sojourner resides, there you shall assign him his inheritance, declares the Lord GOD.' The sojourner receives his inheritance in whatever tribe he has made his home — no central reservation, no segregation, but full integration. The principle is integration by adoption: the sojourner becomes a full member of the tribe in which he lives. The NT's &ldquo;household of God&rdquo; (Eph 2:19: &ldquo;you are no longer strangers and aliens, but you are fellow citizens with the saints and members of the household of God&rdquo;) is the fulfillment of this integrationist vision: in Christ, there is no sojourner-class.</p>"
  },
  "48": {
    "1": "<p>A structural note: 'These are the names of the tribes: Beginning at the northern extreme, beside the way of Hethlon to Lebo-hamath as far as Hazar-enan on the northern border of Damascus opposite Hamath, and extending from the east side to the west, Dan, one portion.' Chapter 48 distributes the land in horizontal strips running east to west — 7 tribes north of the sacred district, the sacred district itself (including the city), and 7 tribes south. The horizontal strips give each tribe equal access to both the Jordan and the sea. The radical equality of the distribution — every tribe the same width — is the eschatological overturning of the historical inequalities of the original tribal allotments.</p>",
    "2": "<p>A structural note: 'Adjoining the territory of Dan from the east side to the west, Asher, one portion.' Asher directly south of Dan in the northern block. The northern seven tribes (Dan, Asher, Naphtali, Manasseh, Ephraim, Reuben, Judah) include both the &ldquo;lost&rdquo; northern tribes and the southern tribes, all restored together. The unity of the twelve tribes in the allotment is the fulfillment of Ezekiel 37:15-23 (the two sticks joined — Judah and Joseph becoming one). Christ as the one who &ldquo;makes both one&rdquo; (Eph 2:14) fulfills the reunification that Ezekiel's allotment enacts.</p>",
    "3": "<p>A structural note: 'Adjoining the territory of Asher from the east side to the west, Naphtali, one portion.' Naphtali — the tribe of Galilee (Isa 9:1: &ldquo;in the former time he brought into contempt the land of Zebulun and the land of Naphtali&rdquo;). Naphtali was despised historically, the region that bore the Assyrian invasion first. Matthew 4:15-16 cites Isaiah 9:1-2 as fulfilled in Jesus's Galilean ministry: &ldquo;the people dwelling in darkness have seen a great light.&rdquo; In the eschatological allotment, Naphtali receives an equal strip of the promised land — the despised region fully restored.</p>",
    "4": "<p>A structural note: 'Adjoining the territory of Naphtali from the east side to the west, Manasseh, one portion.' Manasseh — one of the two Joseph tribes — receives a full allotment. In the original Canaan division, Manasseh received a trans-Jordan portion and a west-Jordan portion; in Ezekiel's vision, Joseph's tribes are unified west of the Jordan. The messy historical geography is simplified into the clean eschatological symmetry. The new creation's order exceeds the old creation's complexity.</p>",
    "5": "<p>A structural note: 'Adjoining the territory of Manasseh from the east side to the west, Ephraim, one portion.' Ephraim — the leading northern tribe, the dominant power in the divided kingdom, the tribe through which the northern exile came (Hos 4-14 is substantially addressed to Ephraim). Ephraim's restoration to a full inheritance is the eschatological reversal of the northern exile: &ldquo;YHWH has called you back like a wife deserted and grieved in spirit&rdquo; (Isa 54:6). The tribes most deeply lost are fully restored.</p>",
    "6": "<p>A structural note: 'Adjoining the territory of Ephraim from the east side to the west, Reuben, one portion.' Reuben — the firstborn of Jacob who lost his birthright through immorality (Gen 35:22; 49:3-4) and received only a trans-Jordan territory historically. In the eschatological allotment, Reuben is restored to the main land with an equal strip. The forfeited birthright is returned. The pattern: &ldquo;if we confess our sins he is faithful and just to forgive us our sins&rdquo; (1 John 1:9). No historical failure is permanent in the eschatological restoration.</p>",
    "7": "<p>A structural note: 'Adjoining the territory of Reuben from the east side to the west, Judah, one portion.' Judah — the royal tribe, the tribe of David, the tribe from which the Messiah comes (Gen 49:10; Mic 5:2) — is given the strip directly north of the sacred district. This positioning is significant: Judah is nearest to the holy portion, reflecting the tribe's covenantal preeminence. Christ as the Lion of the tribe of Judah (Rev 5:5) makes Judah's positioning in the eschatological map a Christological declaration: the Messiah's tribe holds the land adjacent to the divine presence.</p>",
    "8": "<p>A structural note: 'Adjoining the territory of Judah from the east side to the west shall be the portion that you shall set apart, twenty-five thousand cubits in breadth and in length equal to one of the tribal portions from the east side to the west, with the sanctuary in the middle of it.' The sacred district — equal in width to each tribal strip but designated for the sanctuary, the priests, the Levites, and the city — is the geographical center of the entire allotment. The sanctuary in the middle of the sacred district, in the middle of the land, surrounded by tribes on all sides: this is the eschatological enactment of YHWH dwelling in the midst of his people. Christ is the temple (John 2:21) who is himself the center of the new creation.</p>",
    "9": "<p>A structural note: 'The portion that you shall set apart for YHWH shall be twenty-five thousand cubits in length and twenty thousand in breadth.' The holy portion is large — 25,000 × 20,000 cubits (roughly 8 × 6.5 miles). Its generous scale reflects the principle that in the eschatological order, the sacred is not a small reservation within a secular land but a substantial center that anchors the entire distribution. The NT eschatology expands this: in the new creation, there is no temple — &ldquo;for its temple is the Lord God the Almighty and the Lamb&rdquo; (Rev 21:22) — because the sacred fills everything.</p>",
    "10": "<p>A structural note: 'These shall be the allotments of the holy portion: the priests shall have an allotment measuring twenty-five thousand cubits on the north side, ten thousand cubits in breadth on the west side, ten thousand in breadth on the east side, and twenty-five thousand in length on the south side, with the sanctuary of YHWH in the middle of it.' The priestly portion with the sanctuary at its center. The Zadokite priests who remained faithful (44:15-16) receive the portion immediately surrounding the sanctuary. In the NT, Christ is the ultimate high priest (Heb 4:14-16) who dwells at the center of the new creation, and all believers are &ldquo;a royal priesthood&rdquo; (1 Pet 2:9) surrounding him.</p>",
    "11": "<p>A structural note: 'This shall be for the consecrated priests, the sons of Zadok, who kept my charge and did not go astray when the people of Israel went astray, as the Levites did.' The faithfulness of the Zadokites in the period of Israel's apostasy is honored with the best land — the priestly portion nearest the sanctuary. Faithfulness under pressure receives its eschatological reward. The NT pattern: &ldquo;well done, good and faithful servant. You have been faithful over a little; I will set you over much. Enter into the joy of your master&rdquo; (Matt 25:21). Fidelity that appears unrewarded in history is rewarded in the age to come.</p>",
    "12": "<p>A structural note: 'It shall belong to them as a special portion from the holy portion of the land, a most holy place, adjoining the territory of the Levites.' The most holy section — the superlative holiness-designation. In the tabernacle and temple, the Most Holy Place was the inner chamber where YHWH's presence dwelt and only the high priest entered once a year. In Ezekiel's vision, the most holy place expands into an entire district. The trajectory moves from a small room to a large district to — in Revelation's new creation — the entire new Jerusalem as the Holy of Holies (Rev 21:16, a perfect cube, like the Holy of Holies of Solomon's temple at 1 Kings 6:20).</p>",
    "13": "<p>A structural note: 'And alongside the territory of the priests, the Levites shall have an allotment twenty-five thousand cubits in length and ten thousand in breadth. The whole length shall be twenty-five thousand cubits and the breadth twenty thousand.' The Levites receive a portion equal to the priests — a dramatic reversal of their historical position. In Numbers 35, the Levites received only forty-eight cities scattered through the tribes; in Ezekiel's vision, they receive a large contiguous district. The service-people are honored in the new order. Christ &ldquo;who came not to be served but to serve&rdquo; (Matt 20:28) makes service the highest status in the kingdom.</p>",
    "14": "<p>A structural note: 'They shall not sell or exchange any of it. They shall not alienate this choice portion of the land for it is holy to YHWH.' The holy portion cannot be sold or transferred — it is permanently holy, permanently belonging to YHWH. This inalienability is the eschatological fulfillment of the Jubilee principle (Lev 25:23: &ldquo;the land shall not be sold in perpetuity, for the land is mine&rdquo;). In the new creation, all things are permanently YHWH's and permanently given: &ldquo;an inheritance that is imperishable, undefiled, and unfading, kept in heaven for you&rdquo; (1 Pet 1:4).</p>",
    "15": "<p>A structural note: 'The remaining strip five thousand cubits wide and twenty-five thousand long, alongside the holy portion, shall be for common use for the city, for dwellings and for open country. The city shall be in the middle of it.' The city (48:15-20) is a separate zone within the overall sacred district — common use, not holy, but centrally located within the holy district. The distinction between the temple-precinct and the city remains, but both are within the larger sacred allocation. The city surrounded by the holy district surrounded by the tribal lands: concentric circles of holiness radiating from the sanctuary.</p>",
    "16": "<p>A structural note: 'These shall be its measurements: the north side four thousand five hundred cubits, the south side four thousand five hundred, the east side four thousand five hundred, and the west side four thousand five hundred.' The city is a perfect square — 4,500 × 4,500 cubits on each side. The perfect square form echoes the Holy of Holies (1 Kings 6:20) and anticipates the new Jerusalem (Rev 21:16: &ldquo;its length and width and height are equal&rdquo;). The perfect geometric form is the architectural expression of divine holiness: without corner-cutting, without irregularity, every side equal. Christ, the &ldquo;cornerstone&rdquo; (Eph 2:20), makes the entire city perfectly aligned.</p>",
    "17": "<p>A structural note: 'And the city shall have open land: on the north two hundred and fifty cubits, on the south two hundred and fifty, on the east two hundred and fifty, and on the west two hundred and fifty.' The city surrounded by open land on all sides — a buffer zone between the city and the agricultural land. The city breathes; it is not a cramped fortress but an open settlement with land around it. The new Jerusalem descends with a garden-city character (Rev 21-22: gates, streets, river, trees) — not a densely packed ruin but a spacious, living city.</p>",
    "18": "<p>A structural note: 'The remainder of the length alongside the holy portion shall be ten thousand cubits to the east and ten thousand to the west. It shall be alongside the holy portion. Its produce shall be food for the workers of the city.' The agricultural strips on either side of the city produce food for the city's workers. The workers who serve the city eat from its produce — a self-sustaining community. The principle: those who serve the sanctuary are fed by it. Jesus's &ldquo;the laborer deserves his wages&rdquo; (Luke 10:7) and Paul's principle that those who preach the gospel should live by the gospel (1 Cor 9:14) both rest on this foundation.</p>",
    "19": "<p>A structural note: 'And the workers of the city from all the tribes of Israel shall till it.' The city's agricultural land is worked by people from all the tribes — the city belongs to no single tribe but to all of Israel together. The city as pan-tribal common ground anticipates the new Jerusalem's twelve-gates structure (48:31-34), which assigns one gate to each tribe while the city itself is shared by all. In Christ, every tribe and nation shares the heavenly city: &ldquo;after this I looked and behold a great multitude that no one could number from every nation, from all tribes and peoples and languages&rdquo; (Rev 7:9).</p>",
    "20": "<p>A structural note: 'The whole portion that you shall set apart shall be twenty-five thousand cubits square that is the holy portion together with the property of the city.' The total sacred district stated as a perfect square: 25,000 × 25,000 cubits. The entire allocation is described geometrically, reinforcing the precision and completeness of YHWH's eschatological ordering. The perfect square of the sacred district corresponds to the perfect cube of the new Jerusalem (Rev 21:16) — both are expressions of the same theological principle: YHWH's new creation is perfectly ordered, perfectly holy, perfectly complete.</p>",
    "21": "<p>A direct revelation: 'What remains on both sides of the holy portion and the property of the city shall belong to the prince. Extending from the twenty-five thousand cubits of the holy portion to the east border and westward from the twenty-five thousand cubits to the west border, parallel to the tribal portions, it shall belong to the prince.' The prince's land flanking the holy district — the messianic figure of Ezekiel's vision (the <em>nasi</em> identified with the Davidic line in 34:23-24 and 37:25) receives land on both sides of the sacred district. The prince is near the sanctuary but not within it: close to YHWH's presence, with access and responsibility, but not himself the high priest. Christ as the one who is simultaneously the Davidic prince and the ultimate high priest (Heb 7:1-28) transcends this distinction.</p>",
    "22": "<p>A direct revelation: 'The property of the Levites and the property of the city shall be in the middle of what belongs to the prince. The portion of the prince shall lie between the territory of Judah and the territory of Benjamin.' The prince's land sandwiches the holy district and city, flanking them on both sides. Judah to the north of the sacred district, Benjamin to the south: the two royal tribes (Judah the tribe of the Davidic line, Benjamin the tribe of Saul but also of Paul) bracket the prince's land. The topography of kingship surrounds the presence of God. Christ the Davidic king holds the land adjacent to his own sanctuary — the shepherd-prince whose land is coextensive with the flock's territory.</p>",
    "23": "<p>A structural note: 'As for the rest of the tribes: from the east side to the west, Benjamin, one portion.' The southern block begins with Benjamin — the smallest tribe but historically significant: first king (Saul), Jerusalem's original border tribe, home of Paul (Rom 11:1; Phil 3:5). In the eschatological allotment, Benjamin is restored to the honored position south of the sacred district. The smallest tribe is not marginalized; it borders the holy portion. &ldquo;God chose what is low and despised in the world ... so that no human being might boast in the presence of God&rdquo; (1 Cor 1:28-29).</p>",
    "24": "<p>A structural note: 'Adjoining the territory of Benjamin from the east side to the west, Simeon, one portion.' Simeon — the tribe absorbed into Judah historically (Gen 49:7: &ldquo;I will divide them in Jacob and scatter them in Israel&rdquo;), with no independent territory after the conquest. In Ezekiel's vision, Simeon receives a full, separate allotment. Jacob's deathbed curse-as-prophecy (the scattering of Simeon) is reversed: even the tribe predicted to be scattered receives an inheritance. The gospel's reach extends to every cursed condition.</p>",
    "25": "<p>A structural note: 'Adjoining the territory of Simeon from the east side to the west, Issachar, one portion.' Issachar — in Jacob's blessing, &ldquo;a strong donkey, crouching between the sheepfolds, who saw that a resting place was good ... and became a servant at forced labor&rdquo; (Gen 49:14-15). Even the tribe whose historical characterization was servitude receives a full, equal inheritance. In the kingdom of Christ, &ldquo;the last will be first and the first last&rdquo; (Matt 20:16): every tribe that bore dishonor in the historical order is honored in the eschatological.</p>",
    "26": "<p>A structural note: 'Adjoining the territory of Issachar from the east side to the west, Zebulun, one portion.' Zebulun — Naphtali's companion tribe in the despised Galilee region (Isa 9:1; Matt 4:15). Matthew's fulfillment citation brings Zebulun and Naphtali together as the region where Jesus began his Galilean ministry: the despised north is the first to see the great light. In the eschatological allotment, Zebulun receives a full inheritance — the light that shone in Galilee prefigures the full restoration of the tribe in the new order.</p>",
    "27": "<p>A structural note: 'Adjoining the territory of Zebulun from the east side to the west, Gad, one portion.' Gad — the trans-Jordan tribe that chose its allotment east of the Jordan (Num 32), outside the main territory. In Ezekiel's vision, Gad is brought west of the Jordan with all the other tribes, given a full inheritance in the main land. The tribes that had settled for the periphery are drawn into the center. The principle: the eschatological inheritance is better than any provisional settlement that feels adequate in the meantime.</p>",
    "28": "<p>A structural note: 'On the south side it shall run from Tamar as far as the waters of Meribah-kadesh from there along the Brook of Egypt to the Great Sea. This shall be the south side.' The southern boundary of the eschatological land repeats (cf. 47:19). The repetition of boundaries in the legal allotment document confirms that Ezekiel's vision is a formal covenant-document: this is not poetry about a vague future but a specific legal promise about a specific territory. The precision of prophetic promises is not decorative but substantive: YHWH commits to particular places and particular peoples.</p>",
    "29": "<p>A structural note: 'This is the land that you shall allot as an inheritance among the tribes of Israel and these are their portions, declares the Lord GOD.' The summary statement closes the tribal allotment. &ldquo;This is the land&rdquo; — the demonstrative points back to everything Ezekiel has seen in chapters 40-48: the temple, the river, the sacred district, the city, the tribal strips. The full vision is covenant-promise, guaranteed by YHWH's declaration. The NT closes similarly: &ldquo;I am making all things new ... these words are trustworthy and true&rdquo; (Rev 21:5).</p>",
    "30": "<p>A direct revelation: 'These shall be the exits of the city: On the north side which is to be four thousand five hundred cubits by measure, three gates, the gate of Reuben, the gate of Judah, and the gate of Levi.' The gates of the new city are named for the twelve tribes — three on each of the four sides. Revelation 21:12-13 reproduces this structure exactly: &ldquo;It had a great high wall with twelve gates and at the gates twelve angels and on the gates the names of the twelve tribes of the sons of Israel were inscribed.&rdquo; John's vision of the new Jerusalem is the eschatological completion of Ezekiel's city-gate vision. The tribes that were scattered are gathered, and their names are permanently inscribed on the gates of the eternal city.</p>",
    "31": "<p>A direct revelation: 'The gates of the city shall be named after the tribes of Israel. The three gates on the north shall be the gate of Reuben, the gate of Judah, and the gate of Levi.' The north side gates: Reuben (firstborn restored), Judah (the royal tribe), and Levi (the priestly tribe receiving a gate of its own, though no tribal land). In Ezekiel's vision, Levi is included in the city-gates even without a land allotment — the priestly tribe has a different kind of inheritance (YHWH himself, Ezek 44:28) but is named among the city's gates. In Rev 21, the Levitical tribe is included in the twelve gates. All twelve have permanent access to the holy city.</p>",
    "32": "<p>A direct revelation: 'On the east side four thousand five hundred cubits, three gates: the gate of Joseph, the gate of Benjamin, and the gate of Dan.' The east side gates: Joseph (united — covering Manasseh and Ephraim), Benjamin, and Dan. Dan's inclusion is notable: Dan was the tribe most associated with idolatry in the OT (Judg 17-18; 1 Kings 12:29), and Dan is absent from the list of the 144,000 in Rev 7:5-8. Yet here Dan appears on the city's gates. The eschatological city includes a gate for the idolatry-tribe — YHWH's grace extends even to the most compromised. The gates are named not because the tribes earned them but because YHWH named them.</p>",
    "33": "<p>A direct revelation: 'On the south side four thousand five hundred cubits by measure, three gates: the gate of Simeon, the gate of Issachar, and the gate of Zebulun.' The south side gates: Simeon (the scattered, restored), Issachar (the servant, honored), Zebulun (the despised, received). The gates on the south side are three of the most historically marginalized tribes. The eschatological city's south entrance is named for those the historical order overlooked. The first shall be last and the last first (Matt 20:16): the gate-names of the eternal city declare this reversal.</p>",
    "34": "<p>A direct revelation: 'On the west side four thousand five hundred cubits, three gates: the gate of Gad, the gate of Asher, and the gate of Naphtali.' The west side gates: Gad (brought from the periphery), Asher (the northern tribe, restored), Naphtali (Galilee, the first to see the great light). The western face of the new city looks out toward the sea — and is named for three restored tribes. All four sides of the city are equally named, equally accessed, equally honored. The city has no back entrance: every side is a front entrance, named for restored Israel, open to all who come.</p>",
    "35": "<p>A direct revelation: 'The circumference of the city shall be eighteen thousand cubits. And the name of the city from that time on shall be, YHWH is There.' <em>YHWH Shammah</em> — &ldquo;YHWH is There&rdquo; — is Ezekiel's final word, the climax of the entire book and of the entire temple-vision (chs 40-48). The name reverses the book's opening crisis: the divine glory departing (10:18-19; 11:22-23) — YHWH is no longer there. Now: YHWH is There. Permanently. Irrevocably. The exile is over; the presence has returned and will never leave again. John's new Jerusalem vision is the NT's YHWH Shammah: &ldquo;Behold the dwelling place of God is with man. He will dwell with them and they will be his people and God himself will be with them as their God&rdquo; (Rev 21:3). Christ himself is YHWH Shammah: &ldquo;and the Word became flesh and dwelt among us&rdquo; (John 1:14) — the incarnation is the first coming of YHWH Shammah; the parousia and new creation are its eternal consummation.</p>"
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
