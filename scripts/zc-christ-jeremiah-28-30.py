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
  "28": {
    "1": "<p>Hananiah, a prophet from Gibeon, arises in the fourth year of Zedekiah to contradict Jeremiah's message of a 70-year exile. The collision of two prophets claiming YHWH's authority establishes the central NT question about true versus false proclamation. Jesus warns: 'Beware of false prophets who come to you in sheep's clothing' (Matt 7:15). The false prophet promises peace without repentance — the ancient version of the message that minimizes judgment.</p>",
    "2": "<p>Hananiah claims to speak in the name of YHWH: 'I have broken the yoke of the king of Babylon.' The invocation of the divine name without divine authority is the pattern Jesus condemns: 'Not everyone who says to me Lord, Lord will enter the kingdom' (Matt 7:21-22). The false prophet's message is about removal of burden without transformation — an external fix rather than heart-renewal.</p>",
    "3": "<p>Hananiah promises the return of the temple vessels within two years. The specific timeframe is designed to seem verifiable and credible. Jesus's own predictions include specific timeframes (Matt 24:34) but are grounded in his authority as the Son who knows the Father's will (Mark 13:32). The false prophet's specificity is a rhetorical tool, not divine knowledge.</p>",
    "4": "<p>The promise of Jeconiah's return and the breaking of Babylon's yoke is a message of false comfort — removing the covenant consequence of sin without dealing with the sin itself. Christ's ministry does the opposite: 'I have come not to bring peace but a sword' (Matt 10:34) — first dealing with the root (sin, death) so that true peace may follow. False religion promises the fruit without addressing the root.</p>",
    "5": "<p>Jeremiah responds before the priests and all the people in the temple — the public setting of the prophetic confrontation. Christ's public confrontations with the scribes and Pharisees follow this pattern: truth and error must be distinguished before the watching community. The temple is the place where prophetic authority is contested because it is the place where YHWH's presence is invoked.</p>",
    "6": "<p>'Amen! May YHWH do so; may YHWH fulfill your words.' Jeremiah's ironic amen — he agrees with the desired outcome (restoration, peace) while disagreeing with Hananiah's claim that it is imminent and without repentance. This models honest engagement with false hope: affirming the genuine desire while challenging the false timeline. Christ similarly affirms what is true in Jewish expectation while correcting the corruption (Matt 5:17-20).</p>",
    "7": "<p>The appeal to prior prophets establishes the rule of prophetic tradition: consistent witness over time validates a message. Jesus appeals to the same tradition — he stands in the line of the prophets whom Jerusalem killed (Matt 23:37). The authority of a prophet is demonstrated by continuity with the prophetic tradition, not by novelty.</p>",
    "8": "<p>The prophets before Jeremiah prophesied war and famine against many nations. The pattern of true prophecy is uncomfortable: it announces judgment before restoration. This is Christ's own pattern — the Sermon on the Mount begins with the poor in spirit, not the triumphant; the resurrection comes through the cross. True prophecy follows the death-to-life sequence.</p>",
    "9": "<p>'As for the prophet who prophesies peace, when the word of that prophet comes to pass, then it will be known that YHWH has truly sent him.' The fulfillment criterion for prophecy (Deut 18:22) is applied to Hananiah — and his failure is later confirmed (v17). Christ is the ultimate test case: his resurrection on the third day, his prediction of the temple's destruction (70 AD), and his promise of his return authenticate his prophetic authority beyond all others.</p>",
    "10": "<p>Hananiah removes the yoke from Jeremiah's neck and breaks it — a dramatic counter-sign-act. The breaking of the wooden yoke prefigures a heavier iron yoke (v13). This is the pattern of false gospel: remove the visible burden (accountability, cross-bearing) and substitute a heavier invisible one (self-deception, bondage to sin). Christ's yoke is easy precisely because it is real: 'Take my yoke upon you and learn from me' (Matt 11:29).</p>",
    "11": "<p>Hananiah proclaims the nations' yoke broken before Jeremiah simply walks away. Jeremiah's withdrawal is not defeat — it is waiting for YHWH's word. Jesus similarly withdrew from confrontation at strategic moments (Luke 4:30; John 8:59) — not from fear but from sovereign timing. The true prophet speaks when YHWH commands and waits when he does not.</p>",
    "12": "<p>The word of YHWH comes to Jeremiah after Hananiah has broken the wooden yoke. YHWH's response to Hananiah's sign-act is to escalate: wooden yoke broken → iron yoke. This is the pattern of rejecting the light burden of covenant obedience and receiving the heavy burden of judgment. The NT counterpart: rejecting the easy yoke of Christ leads to the bondage Christ came to break (Gal 5:1).</p>",
    "13": "<p>Iron yokes cannot be broken as wooden ones can. The escalation from wood to iron communicates that false prophecy does not remove judgment but intensifies it. The message of grace that omits repentance produces harder hearts and heavier consequences — the theological principle Paul articulates: 'You are storing up wrath for yourself on the day of wrath' (Rom 2:5). Only Christ removes the iron yoke completely through the cross.</p>",
    "14": "<p>'I have put a yoke of iron on the neck of all these nations to serve Nebuchadnezzar.' The nations' subjection to Babylon is YHWH's sovereign act — the world's empires are instruments in divine hands. This establishes the framework for understanding Rome in the NT period: human political authority is real but derivative (John 19:11). Christ's kingdom 'is not of this world' (John 18:36) but will ultimately outlast all iron yokes.</p>",
    "15": "<p>Jeremiah confronts Hananiah directly: 'YHWH has not sent you, and you have made this people trust in a lie.' The verdict against the false prophet is that he created false trust — faith in the wrong word. This is the precise danger Jesus warns against: building on sand instead of rock (Matt 7:26-27). The false prophet produces faith that does not hold when the storm comes.</p>",
    "16": "<p>Hananiah will die that very year because he spoke rebellion against YHWH. The swift judgment on the false prophet is sobering — false teaching is not a minor error but rebellion (<em>sarah</em>) against YHWH. James warns that teachers will be judged more strictly (Jas 3:1). The NT intensifies the stakes around prophetic authority, not relaxes them.</p>",
    "17": "<p>Hananiah died in the seventh month of that same year — the word of YHWH fulfilled against the word of Hananiah in real historical time. The swift vindication of Jeremiah points to the pattern of Christ's own vindication: prophecies made (Matt 26:64), the Passion, resurrection (Acts 2:23-24). YHWH vindicates his true prophet in history; the resurrection is the ultimate historical vindication.</p>"
  },
  "29": {
    "1": "<p>Jeremiah's letter to the exiles in Babylon from Jerusalem — a letter sent across political and geographical boundaries to sustain a community of faith. The pastoral letter format anticipates the NT epistolary tradition: Paul writes to communities in exile from their true homeland (Phil 3:20; 1 Pet 1:1). The letter bridges the gap between the sender's presence and the recipients' need.</p>",
    "2": "<p>The letter goes after Jeconiah, the queen mother, officials, craftsmen, and smiths — the elite of Judah — have already gone into exile. The community that receives Jeremiah's letter is the best and brightest of Judah, stripped of their homeland. Paul similarly addresses letters to communities that include social elite (Acts 17:12) but re-centers them on a different set of values.</p>",
    "3": "<p>Elasah and Gemariah carry the letter — named messengers who bear the word. The incarnational principle: the word is not disembodied but carried by human agents. Christ himself is the Word made flesh (John 1:14), the ultimate divine messenger who does not merely carry the message but is the message.</p>",
    "4": "<p>'Thus says YHWH of Hosts, the God of Israel, to all the exiles whom I have sent into exile from Jerusalem to Babylon.' YHWH acknowledges his own agency in the exile: 'whom I have sent.' The exiles were not accidents of history but YHWH's purposeful placement. Paul sees his imprisonment the same way: 'what has happened to me has really served to advance the gospel' (Phil 1:12). Providence shapes the mission field.</p>",
    "5": "<p>Build houses, plant gardens, eat their produce — the command to invest in exile rather than maintaining a posture of suspended animation. This is the NT pattern for the church as exile community: 'seek the good of the city where I have sent you into exile' (v7). The kingdom of God is not built by withdrawal but by engaged presence, bearing fruit in alien soil (John 15:8).</p>",
    "6": "<p>Take wives, have sons and daughters — establish family life in exile. The exiles are not to minimize their numbers but to multiply. The NT mission follows: 'Go and make disciples' (Matt 28:19). The people of God grow in every soil, including hostile environments. The church's demographic vitality in exile is itself a sign of YHWH's blessing.</p>",
    "7": "<p>'Seek the welfare (<em>shalom</em>) of the city where I have sent you into exile, and pray to YHWH on its behalf.' This is the foundational text for the church's civic vocation: loving enemies, praying for those who persecute (Matt 5:44), being salt and light in society (Matt 5:13-16). The command to seek the city's <em>shalom</em> anticipates the NT's theology of the church as a community for the world's benefit.</p>",
    "8": "<p>'Do not let your prophets and your diviners who are among you deceive you.' The warning against internal false prophecy mirrors Christ's warning: 'Many false prophets will arise and lead many astray' (Matt 24:11). The danger is not external but internal — voices within the covenant community that promise comfort without truth.</p>",
    "9": "<p>'They are prophesying falsely to you in my name; I did not send them.' The claim of YHWH's name without YHWH's commission — the counterfeit gospel that Paul warns against: 'If anyone is preaching to you a gospel contrary to the one you received, let him be accursed' (Gal 1:9). Authentication of the messenger by YHWH is non-negotiable.</p>",
    "10": "<p>'When seventy years are completed for Babylon, I will visit you and fulfill to you my good word.' The 70-year period is YHWH's appointed time — a specific, numbered divine plan. This temporal specificity about YHWH's plan is the foundation of the NT claim that Christ came 'when the time had fully come' (Gal 4:4). YHWH's plans have a kairos — an appointed time, not just chronos.</p>",
    "11": "<p><strong>'For I know the plans I have for you, declares YHWH, plans for welfare and not for evil, to give you a future and a hope.'</strong> This is one of the most-cited OT promises in the NT era: the certainty of YHWH's good intent toward his people. In Christ it finds its yes and amen (2 Cor 1:20) — every plan of welfare converges in the one who is himself the embodiment of shalom, and in whom 'all the promises of God find their Yes.' The future and hope is not vague optimism but has a personal name.</p>",
    "12": "<p>'Then you will call upon me and come and pray to me, and I will hear you.' Access to YHWH's hearing is promised to the exiles who seek him — anticipating the new covenant access Christ opens. 'Whatever you ask in my name, this I will do' (John 14:13). Prayer heard by God is the mark of covenant relationship, fully realized in Christ who intercedes (Heb 7:25).</p>",
    "13": "<p>'You will seek me and find me, when you seek me with all your heart.' The seeking-finding promise is quoted by Jesus directly (Matt 7:7: 'Seek and you will find'). Christ is not merely a route to finding YHWH — he is the one through whom YHWH is found: 'I am the way... no one comes to the Father except through me' (John 14:6). The wholehearted seeking of Jer 29:13 is directed to the person of Christ in the NT.</p>",
    "14": "<p>'I will be found by you... and I will restore your fortunes.' The restoration promise — <em>ashiv et-shevutchem</em> — is YHWH's sovereign act of reversal. The ultimate restoration is the new creation: Rev 21:5, 'Behold, I am making all things new.' Christ's resurrection is the firstfruits of that total restoration (1 Cor 15:20-23), the guarantee that YHWH's plan to restore is not a metaphor but a physical, historical reality.</p>",
    "15": "<p>The exiles appeal to their own prophets in Babylon. The availability of prophetic voices in exile reflects the expansion of prophetic ministry beyond the land — anticipating the NT where the Spirit is poured out on all flesh (Acts 2:17-18). YHWH is not confined to a geography; his word reaches the exiles.</p>",
    "16": "<p>Concerning the king sitting on David's throne and the people remaining in Jerusalem — YHWH addresses the whole covenant community, not just the exiles. The scope of YHWH's word encompasses both those in exile and those who remain. Christ's commission is similarly universal: 'all nations' (Matt 28:19), 'to the ends of the earth' (Acts 1:8).</p>",
    "17": "<p>The bad figs who were not deported — those left in Jerusalem who think they escaped — will face sword, famine, and plague. The irony: those who avoided the covenant discipline of exile (the first deportation) face worse judgment. This reverses the apparent advantage. Jesus makes the same point: the tax collectors and prostitutes enter the kingdom before the self-righteous (Matt 21:31).</p>",
    "18": "<p>They will become a horror to all the nations — <em>leharzinah</em>, object of shock. The covenant curse of Deut 28:25 applied: those who thought they were safe become the example of divine judgment. The NT equivalent is the parable of the older brother (Luke 15:28-30) who thinks his proximity guarantees favor.</p>",
    "19": "<p>'Because they did not pay attention to my words, declares YHWH, which I persistently sent to them by my servants the prophets.' The persistent sending of prophets is the pattern Jesus names in the parable of the wicked tenants (Matt 21:34-36) — servant after servant sent, each rejected. The long patience of YHWH before judgment is itself an act of grace.</p>",
    "20": "<p>'Hear the word of YHWH, all you exiles whom I sent away from Jerusalem to Babylon.' The repeated call to hear — YHWH's persistent address to the community that has been disciplined. This is the pattern of the father running to the returning son (Luke 15:20) — YHWH does not abandon the exiles to silence but pursues them with his word.</p>",
    "21": "<p>Ahab and Zedekiah, the false prophets in Babylon, spoke lies in YHWH's name and committed adultery. The moral failure of the false prophets is not incidental — Jesus connects false teaching with moral corruption: a tree is known by its fruit (Matt 7:17). The prophetic calling requires both verbal faithfulness and moral integrity.</p>",
    "22": "<p>They will become a byword: 'YHWH make you like Zedekiah and Ahab, whom the king of Babylon roasted in the fire.' The gruesome end of false prophets becomes a proverb. The severity of judgment on false prophets in the OT establishes the gravity with which the NT treats the same: 'their condemnation is just' (Rom 3:8).</p>",
    "23": "<p>'Because they have done an outrageous thing in Israel: they have committed adultery with their neighbors' wives and have spoken in my name lying words that I did not command them.' The double sin — sexual and prophetic unfaithfulness — is treated as a unit. Paul's list of qualifications for church leaders (1 Tim 3; Tit 1) reflects the same principle: public ministry demands integrity in every domain.</p>",
    "24": "<p>Shemaiah of Nehelam wrote letters opposing Jeremiah — a coordinated effort to undermine the true prophet from within the exile community. The opposition to Jeremiah from multiple fronts (priests, prophets, officials) typifies Christ's multi-front opposition: Pharisees, Herodians, Sadducees, and finally the Roman state (Mark 3:6; 15:1-15). Truth-tellers face institutional resistance.</p>",
    "25": "<p>Shemaiah sent letters in his own name to Jerusalem's priests and all the people, claiming authority he did not have. The self-appointed authority — speaking without divine commission — is the false apostle Paul warns about: those who 'commend themselves' (2 Cor 10:12). True authority is given, not assumed.</p>",
    "26": "<p>Shemaiah's letter commands the priest to put any prophet who acts crazily in the stocks. The attempt to silence the true prophet by institutional authority — 'put him in the stocks' — anticipates Jeremiah 20 and prefigures the institutional silencing of Christ (Matt 26:65-66: 'He is guilty of death') and the apostles (Acts 5:18). The establishment often resists the prophet.</p>",
    "27": "<p>Shemaiah accuses Jeremiah of prophesying falsely, calling him a madman. The accusation of madness against the true prophet — Jesus was also accused of being out of his mind (Mark 3:21: 'He is out of his mind') and of having a demon (John 8:48). The pattern: dismiss the prophet's authority by questioning his sanity.</p>",
    "28": "<p>Jeremiah had written to the exiles to settle in Babylon for a long time — the command to build and plant. This long-haul patience is the NT posture of those awaiting the parousia: 'Be patient, therefore, brothers, until the coming of the Lord' (Jas 5:7). Neither despairing nor falsely optimistic, but faithfully present in the world until YHWH's appointed time.</p>",
    "29": "<p>Zephaniah reads Shemaiah's letter to Jeremiah — the priest delivers the attack to the prophet himself. The transparency of opposition is notable: YHWH ensures Jeremiah knows who opposes him and why. Jesus similarly knows the intentions of his opponents (Mark 2:8: 'immediately perceiving in his spirit') and names the hypocrisy openly.</p>",
    "30": "<p>The word of YHWH comes to Jeremiah regarding Shemaiah's opposition. The divine response to false prophetic attack is more divine speech — YHWH does not leave his prophet without a counter-word. The NT equivalent: the Spirit gives speech in moments of persecution (Matt 10:19-20). The word is not silenced by opposition.</p>",
    "31": "<p>'Shemaiah the Nehelamite has prophesied to you, though I did not send him.' The divine verdict is unambiguous: not sent. The criterion of divine sending versus self-sending runs throughout the NT: 'How can they preach unless they are sent?' (Rom 10:15). The mission depends on authorization, and authorization comes from YHWH alone — given to the Son (John 20:21) and through the Son to his people.</p>",
    "32": "<p>Shemaiah will not see the good that YHWH will do for his people — he and his descendants cut off from the restoration. The exclusion from eschatological blessing is the NT pattern for those who oppose the gospel (Matt 8:12; Rev 22:15). The mercy offered in YHWH's plans (v11) is not coercive — it can be forfeited by persistent opposition to the divine word.</p>"
  },
  "30": {
    "1": "<p>The opening of the Book of Consolation (chs 30-33) — YHWH commands Jeremiah to write down these words. The writing command is significant: this is meant to be preserved for the coming generation who will witness the fulfillment. The preserved written word anticipates scripture's function in the NT: 'these things were written for our instruction' (1 Cor 10:11; Rom 15:4).</p>",
    "2": "<p>'Write in a book all the words I have spoken to you.' The codification of prophetic speech into a text that will outlast the moment — the principle behind all scripture. Jesus's words are preserved and fulfilled as scripture (John 19:24,36; 20:31). The word written for the future is the basis of faith grounded in testimony rather than direct experience.</p>",
    "3": "<p>'For behold, days are coming, declares YHWH, when I will restore the fortunes of my people Israel and Judah.' The <em>yemim baim</em> (days are coming) formula — the prophetic horizon of eschatological fulfillment. Jesus opens his ministry with 'the time is fulfilled' (Mark 1:15) — he announces that the days Jeremiah was waiting for have arrived. The restoration of Israel and Judah points ultimately to the new creation in which all things are made new (Rev 21:5).</p>",
    "4": "<p>These are the words YHWH spoke concerning Israel and Judah — both kingdoms addressed, which means the restoration is not merely the end of the Babylonian exile but the full gathering of the divided people. The NT presents Christ as the one who breaks down the wall between peoples (Eph 2:14) and gathers the scattered children of God into one (John 11:52).</p>",
    "5": "<p>'We have heard a cry of panic, of terror, and no peace.' The sound of terror preceding the deliverance. The tribulation pattern — anguish before rescue — is the structure of the gospel: 'the hour is coming, and is now here, when you will be scattered... and will leave me alone' (John 16:32), but also 'I have overcome the world' (John 16:33). Tribulation is the prelude to peace.</p>",
    "6": "<p>Men in labor-like anguish — the childbirth imagery for eschatological distress (cf. 4:31). Paul uses the same image for creation's travail awaiting the resurrection (Rom 8:22: 'the whole creation has been groaning in the pangs of childbirth until now'). The pain is not meaningless suffering but the labor of new creation.</p>",
    "7": "<p>'Alas! That day is great; there is none like it; it is a time of distress for Jacob.' The <em>yom gadol</em> (great day) that is also a time of Jacob's trouble — unprecedented tribulation. Jesus quotes this tradition in Matthew 24:21 ('there will be great tribulation, such as has not been from the beginning of the world until now'). But the verse continues: 'yet he shall be saved out of it' — the tribulation is not the end but the passage to salvation.</p>",
    "8": "<p>'I will break his yoke from off your neck.' The promise of freedom from the yoke of oppression — the reversal of the iron yoke threatened in ch28. Christ comes to proclaim liberty to captives (Luke 4:18; Isa 61:1), to free those enslaved under the law (Gal 4:3-5), to break every yoke (Isa 58:6). The broken yoke is the signature act of eschatological redemption.</p>",
    "9": "<p><strong>'They shall serve YHWH their God and David their king, whom I will raise up for them.'</strong> A direct Davidic prophecy: YHWH will <em>raise up</em> (<em>aqim</em>) David as king — the resurrection vocabulary used for the Davidic covenant fulfillment. In the NT this is explicitly applied to Jesus: 'God raised up Jesus... David, having died, was buried... but he whom God raised up did not see corruption' (Acts 13:34-37). The raised Davidic king is Christ.</p>",
    "10": "<p>'Fear not, O Jacob my servant... for I will save you from far away.' The oracle of salvation (<em>al-tira</em>) — the same formula spoken to Abraham (Gen 15:1) and repeated throughout Isaiah. Christ embodies this word — 'Do not be afraid' is his most common command (Matt 14:27; John 14:1). Salvation from a far country is the pattern of the incarnation: the Son comes from heaven to the far country where the lost sheep is.</p>",
    "11": "<p>'For I am with you to save you, declares YHWH.' The Emmanuel promise — YHWH-with-us — which Matthew explicitly identifies as fulfilled in Jesus (Matt 1:23: 'God with us'). The presence of God as the means of salvation is the Christological core: not a distant deity sending instructions but a God who enters the situation personally. 'I will be with you' culminates in 'the Word became flesh and dwelt among us' (John 1:14).</p>",
    "12": "<p>'Your hurt is incurable, your wound is grievous.' The honest diagnosis of the depth of sin's damage — not a minor adjustment needed but an incurable wound. This is the anthropological premise of the incarnation: only YHWH can heal what human remedies cannot. Jesus comes as the divine physician (Mark 2:17: 'Those who are well have no need of a physician') precisely for those whose condition is medically hopeless.</p>",
    "13": "<p>'There is none to uphold your cause, no medicine for your wound.' The forensic and medical metaphors converge: no advocate, no cure. Christ answers both: as advocate (1 John 2:1: 'we have an advocate with the Father, Jesus Christ the righteous') and as healer (Matt 8:17 quotes Isa 53:4 for Jesus's healing ministry). The double hopelessness of the incurable wound is met by Christ's double ministry.</p>",
    "14": "<p>'All your lovers have forgotten you; they do not care for you.' The lovers (political allies) who abandoned Israel — a recurrent OT metaphor for covenant unfaithfulness whose reversal is the central theme of redemption. Christ comes for those abandoned by every human help: 'I will never leave you nor forsake you' (Heb 13:5) stands against every human abandonment. The faithless lovers are replaced by the faithful Bridegroom (Rev 19:7).</p>",
    "15": "<p>'Why do you cry out over your wound? Your pain is incurable.' YHWH acknowledges the pain while also naming its cause: 'Because your guilt is great, your sins are flagrant.' The incurable wound is not arbitrary suffering but the consequence of sin. Christ does not minimize this: the cross is the place where the full weight of the wound is carried — not dismissed but borne (Isa 53:5: 'by his wounds we are healed').</p>",
    "16": "<p>'Therefore all who devour you shall be devoured, and all your foes shall go into captivity.' The reversal of Israel's fate is simultaneously a judgment on Israel's oppressors. This retributive logic runs through Revelation: Babylon that devoured will be devoured (Rev 18:6). Christ's victory is not merely positive restoration but the definitive defeat of the powers that oppressed.</p>",
    "17": "<p><strong>'For I will restore health to you, and your wounds I will heal, declares YHWH.'</strong> The healing of the incurable wound — the theme that runs through the entire Book of Consolation. Jesus's healing ministry throughout the Gospels is the embodied enactment of this promise: 'He took our illnesses and bore our diseases' (Matt 8:17 quoting Isa 53:4). Every physical healing is a sign of the deeper spiritual healing Christ brings to the incurable wound of sin.</p>",
    "18": "<p>'I will restore the fortunes of Jacob's tents and have compassion on his dwellings.' Restoration of the physical dwelling-place — the place of community, family life, and security. The New Jerusalem (Rev 21:3) is the ultimate fulfillment: 'Behold, the dwelling place of God is with man. He will dwell with them.' The tent/tabernacle/dwelling imagery runs from Eden to Sinai to the temple to Christ (John 1:14: <em>eskēnōsen</em>, tabernacled) to the New Jerusalem.</p>",
    "19": "<p>'Out of them shall come songs of thanksgiving, and the voices of those who celebrate.' The community of restored worship — voices of praise replacing voices of lament. The Psalter and the Revelation are the two great collections of this worship. Christ is the leader of the congregation's praise (Heb 2:12 quoting Ps 22:22: 'In the midst of the congregation I will sing your praise'). The multiplied, rejoicing community is the telos of restoration.</p>",
    "20": "<p>'Their children shall be as they were of old.' The generational continuity of the covenant community — the promise that the restoration is not just for this generation but for the children. The NT promises the same: 'the promise is for you and for your children' (Acts 2:39). The covenant community is not merely personal but familial and generational, passing the inheritance forward.</p>",
    "21": "<p><strong>'Their ruler shall be one of themselves, and their governor shall come from their midst; I will make him draw near, and he shall approach me.'</strong> The native ruler who approaches YHWH — the priestly-kingly figure who has access to the divine presence. Hebrews presents Christ precisely in these terms: the high priest who is one of us (Heb 2:17: 'he had to be made like his brothers in every respect'), who draws near to God on behalf of the people (Heb 10:19-22). The drawing-near of the ruler to God is fulfilled in Christ's priestly intercession.</p>",
    "22": "<p><strong>'And you shall be my people, and I will be your God.'</strong> The covenant formula — the most concise statement of the covenant relationship in the entire OT. It appears in Exodus, Leviticus, Ezekiel, Jeremiah repeatedly, and is fulfilled in the NT: 'I will make my dwelling among them and walk among them, and I will be their God, and they shall be my people' (2 Cor 6:16; Rev 21:3). Christ mediates this ultimate covenant relationship — he is the Immanuel, God-with-us, in whom the formula becomes personal presence.</p>",
    "23": "<p>The storm of YHWH's wrath — <em>sar'ah YHWH</em>, tempest of YHWH — will burst on the heads of the wicked. The divine judgment that precedes the restoration is YHWH's active wrath, not passive permission. In the NT, this wrath is poured out on Christ at Calvary for those who believe, and reserved for the final day for those who do not (Rom 5:9: 'saved by him from the wrath of God'; Rev 19:15: the winepress of the wrath of God).</p>",
    "24": "<p>'In the latter days you will understand this.' The eschatological horizon placed at the end of the storm-oracle: full understanding comes at the end of the process. Paul echoes this: 'Now I know in part; then I shall know fully' (1 Cor 13:12). Christ's coming initiates the 'latter days' (Heb 1:2: 'in these last days he has spoken to us by his Son'), and his return completes them. The clarity that comes at the end is the full revelation of what was always true.</p>"
  },
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
