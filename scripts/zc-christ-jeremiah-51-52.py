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
  "51": {
    "1": "<p>YHWH raises a <em>ruach</em> (wind/spirit) as a destroyer against Babylon — the same word used for the Spirit hovering over creation (Gen 1:2) and YHWH's breath that dries the Red Sea (Exod 14:21). The sovereign God who governs creation's winds governs the winds of judgment. Christ is the one through whom the Spirit is poured out (Acts 2:33) and who commands the wind (Mark 4:39) — the same divine breath that destroys Babylon will renew creation (Rev 21:5).</p>",
    "2": "<p>Strangers (<em>zarim</em>) are sent against Babylon to winnow it and empty the land. The winnowing imagery — separating grain from chaff — is John the Baptist's description of Christ's work: 'He will baptize you with the Holy Spirit and fire. His winnowing fork is in his hand to clear his threshing floor' (Matt 3:11-12; Luke 3:17). The divine judgment that falls on Babylon is the same principle that operates in the last judgment.</p>",
    "3": "<p>The archer who strings his bow and the soldier who arms himself — YHWH commands: 'Spare not her young men; devote to destruction all her army.' The holy war (<em>cherem</em>) language applied to Babylon. Christ's conquest at the end is described in the same military terms (Rev 19:11-21), but the conquest is through his word, not military force: 'from his mouth comes a sharp sword with which to strike down the nations.'</p>",
    "4": "<p>The slain fall in Babylon, the wounded in her streets. The image of a city filled with casualties — the language of total military defeat. John of Patmos draws directly on Jeremiah's Babylon oracles for Revelation's 'Babylon the Great': 'In her was found the blood of prophets and of saints, and of all who have been slain on earth' (Rev 18:24). The blood cried from the streets of ancient Babylon echoes in the eschatological Babylon.</p>",
    "5": "<p>For Israel and Judah are not widowed by their God, though their land is full of guilt against the Holy One of Israel. The covenant loyalty of YHWH persists through the exile — YHWH does not abandon the people even when they sin. This is the NT's foundation: 'If we are faithless, he remains faithful — for he cannot deny himself' (2 Tim 2:13). Christ's covenant commitment is permanent even when his people fail.</p>",
    "6": "<p>'Flee from the midst of Babylon; let every one save his life! Be not cut off in her punishment.' The urgency of departure from the doomed city is echoed directly in Revelation: 'Come out of her, my people, lest you take part in her sins, lest you share in her plagues' (Rev 18:4; cf. 2 Cor 6:17). The call to come out of Babylon is the call to leave the world's idolatrous system, answered fully in Christ who calls his own out of the world (John 17:15-16).</p>",
    "7": "<p>'Babylon was a golden cup in YHWH's hand, making all the earth drunken.' The golden cup of Babylon — the instrument of YHWH's judgment on the nations — is taken up in Revelation 17:4 where the whore of Babylon holds a golden cup 'full of abominations and the impurities of her sexual immorality.' The cup of judgment that nations were forced to drink (ch25:15) is the shadow of the cup Christ drinks at Calvary, emptying it so his people need not (Mark 14:36).</p>",
    "8": "<p>'Suddenly Babylon has fallen and been broken.' The suddenness of Babylon's fall — the great empire collapses without warning. Rev 18:8,10,17 echoes this: 'in a single hour your judgment has come.' Christ's parables of the sudden coming judgment (Matt 24:43-44; Luke 12:39-40) use the same suddenness motif. Every sudden historical fall of empire is a preview of the final, sudden reckoning.</p>",
    "9": "<p>'We would have healed Babylon, but she was not healed. Forsake her and let us go, each to his own country.' The impossibility of Babylon's healing — the incurable wound applied here to the world empire. The same diagnosis as Judah's incurable wound (Jer 30:12) extended to the world system. Christ heals what human effort cannot; but those who refuse healing are left to the incurable condition they have chosen (John 5:40).</p>",
    "10": "<p>'YHWH has brought about our vindication; come, let us declare in Zion the work of YHWH our God.' The declaration of divine vindication in Zion — the proclamation of YHWH's righteous acts. Rev 19:1-3 echoes this with the heavenly host crying 'Hallelujah!' at Babylon's fall. The vindication of YHWH's purposes is the content of the church's proclamation: 'we preach Christ crucified... the power of God and the wisdom of God' (1 Cor 1:23-24).</p>",
    "11": "<p>'Sharpen the arrows! Take up the shields! YHWH has stirred up the spirit of the kings of the Medes.' YHWH stirs the spirit of the Medes as his instrument of judgment — divine sovereignty working through pagan political powers. The same principle operates in the NT: Pilate has authority 'only because it has been given from above' (John 19:11). Every human political power operates within the scope of divine purpose.</p>",
    "12": "<p>Set up the standard against Babylon — post watchmen, prepare ambushes. YHWH has both planned and accomplished what he spoke against Babylon. The divine speech-act that creates and destroys is the pattern of the Logos: 'In the beginning was the Word... all things were made through him' (John 1:1-3). What YHWH speaks, he performs; what he performs, he spoke.</p>",
    "13": "<p>'You who dwell by many waters, rich in treasures, your end has come.' Babylon built beside the Euphrates — the city of waters and wealth. Revelation's Babylon sits 'on many waters' (Rev 17:1,15) where the waters are 'peoples and multitudes and nations and languages.' The world system's affluence and international reach does not insulate it from judgment; abundance can become the very ground of pride that invites destruction.</p>",
    "14": "<p>'YHWH of Hosts has sworn by himself: Surely I will fill you with men, as many as locusts, and they shall raise the shout of victory over you.' The divine self-oath guarantees Babylon's destruction — the same formula used in the Abraham promises (Heb 6:13-14). YHWH swears by himself because there is no greater authority to swear by. The double certainty of God's oath and God's promise provides the unshakeable anchor for hope (Heb 6:19).</p>",
    "15": "<p>'It is he who made the earth by his power, who established the world by his wisdom.' The creation hymn (identical to 10:12-16) interrupts the Babylon oracle to ground the judgment in YHWH's identity as Creator. Christ is identified as this Creator: 'all things were made through him, and without him was not any thing made that was made' (John 1:3; Col 1:16). The one who judges Babylon is the one who made everything Babylon claims to own.</p>",
    "16": "<p>The thunder, rain, lightning, and wind commanded by YHWH — the Creator's authority over nature is the basis for his authority over history. Jesus's nature miracles (calming the storm, walking on water) are epiphanies of this same creative authority. The disciples' question — 'Who then is this, that even wind and sea obey him?' (Mark 4:41) — is answered by Jeremiah: the one who established the world by wisdom.</p>",
    "17": "<p>'Every man is stupid and without knowledge; every goldsmith is put to shame by his idols, for his images are false.' The comprehensive failure of human wisdom without God — the same diagnosis as 10:14. The idol-maker's shame is the NT's starting point: 'the world did not know God through wisdom' (1 Cor 1:21). The wisdom of the world cannot produce the knowledge of YHWH; only the foolishness of the cross can (1 Cor 1:25).</p>",
    "18": "<p>'They are worthless, a work of delusion; at the time of their punishment they shall perish.' The idols that promised power and security perish when judgment comes — they cannot protect their makers. Christ is the one who cannot perish and who keeps those in him from ultimate perishing: 'whoever believes in him should not perish but have eternal life' (John 3:16). The contrast between the idol that perishes and the living God who protects is the Christological contrast of the whole Bible.</p>",
    "19": "<p>'Not like these is he who is the portion of Jacob.' The incomparability formula — the Creator-God as personal <em>chelek</em> (portion/inheritance) of his people. In the NT, Christ becomes the personal inheritance of believers: 'the riches of his glorious inheritance in the saints' (Eph 1:18). YHWH Tzvaot is his name — the God behind the name of Jesus (Phil 2:9-11).</p>",
    "20": "<p>'You are my war club and weapon of war: with you I break nations in pieces.' YHWH addresses Babylon as his instrument of judgment. The weapon in YHWH's hand — the agent of divine purposes who does not know he is being used. Cyrus is named as YHWH's anointed without knowing YHWH (Isa 45:4). Christ, by contrast, is the willing instrument — 'not my will, but yours be done' (Luke 22:42) — who carries the divine purpose knowingly and obediently.</p>",
    "21": "<p>'With you I break in pieces the horse and his rider; with you I break in pieces the chariot and the charioteer.' The comprehensive dismantling of military power through YHWH's chosen instrument. The horse and rider imagery echoes Exod 15:1 (the Song of the Sea) — the same pattern of divine victory over military force. Christ's final victory (Rev 19:11-21) is described as the rider on the white horse who defeats the armies of the earth.</p>",
    "22": "<p>Man and woman, old and young, young man and young woman — comprehensive human society broken by judgment. The universality of judgment when YHWH acts. The same universality is the scope of grace: 'there is neither Jew nor Greek, slave nor free, male and female, for you are all one in Christ Jesus' (Gal 3:28). The boundaries that judgment crosses are the same boundaries grace ignores.</p>",
    "23": "<p>Shepherds and flocks, farmers and plowing teams broken by YHWH through Babylon. The agricultural society, the pastoral economy — all within the scope of judgment. The shepherd imagery in the nations oracles resonates with Christ as the Good Shepherd (John 10:11): every shepherd in the OT is a foil that either anticipates or contrasts with the one true Shepherd who will not be broken.</p>",
    "24": "<p>'I will repay Babylon and all the inhabitants of Chaldea before your very eyes for all the evil that they have done in Zion.' The repayment principle — evil done against Zion is repaid to the perpetrator. The lex talionis at the national level: Rev 18:6 quotes this principle directly for eschatological Babylon. Christ is both the one who absorbs the repayment for his people (2 Cor 5:21) and the one through whom the final repayment comes (2 Thess 1:7-8).</p>",
    "25": "<p>'Behold, I am against you, O destroying mountain, declares YHWH, who destroys the whole earth.' Babylon as the destroying mountain. Daniel 2:35 describes a stone cut without hands that strikes the statue and becomes a great mountain filling the earth — the stone is Christ, the kingdom of God that destroys the world empires and fills the whole earth. The destroying mountain of Babylon is replaced by the life-giving mountain of YHWH's kingdom.</p>",
    "26": "<p>'No stone shall be taken from you for a corner and no stone for a foundation, for you shall be desolate forever.' Babylon will yield no building material — no cornerstone or foundation. The contrast with Christ: 'the stone the builders rejected has become the cornerstone' (Ps 118:22/Matt 21:42). Christ is the foundation that is laid (1 Cor 3:11) and the cornerstone of the new temple (Eph 2:20). What Babylon could never provide, Christ is.</p>",
    "27": "<p>Set up the battle standard; blow the trumpet among the nations; prepare the nations against Babylon. The universal mobilization against Babylon — a coalition of nations. The eschatological gathering of the nations in Revelation echoes this: the nations assembled to attack 'the beloved city' (Rev 20:9), but YHWH defends it. The same Lord who mobilized nations against Babylon mobilizes them against the final enemy.</p>",
    "28": "<p>Consecrate the nations against Babylon — the Medes with their kings and governors. The Medes as the instrument of judgment — historically Cyrus the Mede/Persian fulfilled this. Isaiah names Cyrus as YHWH's anointed (Isa 45:1). Every human <em>mashiach</em> (anointed) in the OT is a type that points to the true Anointed One — the Messiah whose victory is complete what Cyrus's victory only foreshadowed.</p>",
    "29": "<p>The land trembles and writhes — YHWH's purpose against Babylon stands: to make Babylon a desolation without inhabitant. The divine purpose (<em>makhshavot</em>, plans/purposes) is immovable. Against the purposes of YHWH no human plan prevails (Isa 46:10: 'my counsel shall stand and I will accomplish all my purpose'). Christ is the embodiment of the divine <em>logos</em> that does not return empty (Isa 55:11).</p>",
    "30": "<p>Babylon's warriors cease fighting, they sit in their strongholds, their strength fails, they become women. The reversal of martial valor — the same covenant-curse as Deut 28:25. The great empire's army rendered helpless before YHWH's purposes. 'Not by might, nor by power, but by my Spirit, says YHWH' (Zech 4:6) is the principle operating here — and in the cross: God's weakness is stronger than human strength (1 Cor 1:25).</p>",
    "31": "<p>Runner upon runner announces to the king of Babylon that his city is taken. The cascade of bad news reaching the king — the empire's information network becomes the bearer of its own doom. The good news (gospel) likewise travels through human messengers: 'How beautiful are the feet of those who preach the good news!' (Rom 10:15 quoting Isa 52:7). Both doom and salvation travel through human proclamation.</p>",
    "32": "<p>The crossing places are seized, the marshes set on fire, the warriors are dismayed. The systematic dismantling of Babylon's defensive infrastructure. Christ's defeat of the powers is similarly systematic: 'he disarmed the rulers and authorities and put them to open shame' (Col 2:15). Every defensive mechanism of sin and death is dismantled by the cross and resurrection.</p>",
    "33": "<p>'The daughter of Babylon is like a threshing floor at the time when it is trodden; yet a little while and the time of her harvest will come.' The harvest metaphor for judgment — the threshing floor where grain and chaff are finally separated. Jesus uses the same imagery for judgment (Matt 3:12; Rev 14:14-20). The moment of harvest comes for every age and civilization: 'let both grow together until the harvest' (Matt 13:30).</p>",
    "34": "<p>'Nebuchadnezzar the king of Babylon has devoured me; he has crushed me; he has made me an empty vessel; he has swallowed me like a monster.' The serpent/dragon (<em>tannin</em>) who swallows Jerusalem. In the NT cosmology, the dragon who swallows is the ancient serpent — Satan (Rev 12:9,15-16; 20:2). Christ comes to destroy the works of the devil (1 John 3:8) and to swallow up death in victory (1 Cor 15:54 quoting Isa 25:8). What the serpent swallows, Christ reclaims.</p>",
    "35": "<p>'The violence done to me and to my kinsmen be upon Babylon, shall the inhabitant of Zion say.' Zion's cry for covenant justice — the blood of the innocent crying out against Babylon. The blood of Abel cried from the ground (Gen 4:10); the blood of the martyrs cries under the altar (Rev 6:9-10): 'O Sovereign Lord, how long before you will judge and avenge our blood?' The answer in Revelation: 'a little longer.'</p>",
    "36": "<p>'Behold, I will plead your cause and take vengeance for you.' YHWH as advocate pleading Israel's legal case against Babylon. Christ is the advocate (<em>parakletos</em>) who pleads the cause of believers (1 John 2:1). The divine advocate who takes vengeance for Zion is the same one who intercedes before the Father. Justice and advocacy are held together in the same person — the righteous one who is both intercessor and judge.</p>",
    "37": "<p>Babylon becomes a heap of ruins, a haunt of jackals — the desolation formula. The wild animals taking over human ruins is the prophetic marker of complete divine judgment (Isa 13:21-22 for Babylon; 34:11-15 for Edom). Revelation's Babylon becomes 'a haunt of every foul bird, a haunt of every foul and hateful beast' (Rev 18:2). The eschatological desolation that the prophets anticipated, Revelation presents as happening to the final world empire.</p>",
    "38": "<p>They roar together like lions; they growl like lion cubs. The people of Babylon in their pride are like lions — until YHWH prepares the feast that becomes their trap. The lion and the lamb imagery of eschatological peace (Isa 11:6) reverses the predator-prey order. Christ as both Lion and Lamb (Rev 5:5-6) is the one who has conquered precisely as the Lamb who was slain — power through sacrifice.</p>",
    "39": "<p>'While they are inflamed I will prepare them a feast and make them drunk, that they may become merry, then sleep a perpetual sleep and not wake, declares YHWH.' The feast that becomes judgment. Belshazzar's feast (Dan 5) is the historical fulfillment — the writing on the wall while the army advances. Christ warns: 'be on guard against eating and drinking... lest that day come upon you suddenly like a trap' (Luke 21:34). Merriment is not immunity.</p>",
    "40": "<p>'I will bring them down like lambs to the slaughter, like rams and male goats.' The proud warriors of Babylon brought down as sacrificial animals. The reversal: those who devoured others become the devoured. The final judgment reverses all predator-prey relationships definitively. Christ, the Lamb who was slain, is also the one who opens the scroll of judgment (Rev 6:1) — slaughter and justice both belong to the Lamb.</p>",
    "41": "<p>'How Sheshach (Babylon) is taken, the praise of the whole earth seized! How Babylon has become a horror among the nations!' The elegiac <em>eikh</em> (how!) over the fall of the world city — the same word that opens Lamentations over Jerusalem. Revelation 18 echoes this lament: 'What city was like the great city?' (Rev 18:18). The fall of every great human civilization is a preview of the final judgment on the world system.</p>",
    "42": "<p>The sea rises over Babylon and covers it with roaring waves. The sea — the symbol of chaos and the nations (Rev 17:15) — overwhelms Babylon. The final destruction of the sea in Rev 21:1 ('and the sea was no more') marks the end of all chaos: the new creation is the world without the primordial threat, because Christ has made all things new.</p>",
    "43": "<p>Her cities become a horror, a dry and desert land — no one dwells there. The desolation-without-inhabitant formula applied to all of Babylon's urban network. Christ's promise of the new Jerusalem (Rev 21:2-4) reverses this: the holy city comes down from heaven, filled with the glory of God and the dwelling place of his people. Every desolated city in prophecy is answered by the city that cannot be desolated.</p>",
    "44": "<p>'I will punish Bel in Babylon and take out of his mouth what he has swallowed.' The god Bel/Marduk forced to disgorge what he consumed — the nations' tribute and Israel's dignity. The serpent/dragon forced to release what it swallowed is the Christological pattern of the harrowing of hell in patristic theology (though not NT explicit): Christ descends and liberates the captives. The God who takes from the mouth of Bel is the God who reclaims from the mouth of death.</p>",
    "45": "<p>'Come out from her, my people! Let every one save his life from the fierce anger of YHWH!' The direct divine address to YHWH's people inside Babylon: come out. This verse is quoted in 2 Cor 6:17 ('Come out from them and be separate') and echoed in Rev 18:4 as a call to the church in the world: do not participate in the world system's sins or share its plagues. The separation of the people of God from the doomed world system is an ongoing calling, not a one-time historical event.</p>",
    "46": "<p>'Let not your heart faint and you be not afraid.' The <em>al-tira</em> oracle — do not fear — addressed to those who hear the confusing reports of war. The command not to fear appears more often in the OT and NT combined than almost any other command. Christ's most repeated command is 'do not be afraid' (Matt 14:27; John 14:1,27). The ground: YHWH controls the reports of war that terrify the nations.</p>",
    "47": "<p>'Therefore, behold, the days are coming when I will punish the images of Babylon.' The <em>yemim baim</em> formula introducing the day of judgment on Babylon's idols. Every idol Babylon worshiped — Marduk, Nebo, Ishtar — will be shamed. The eschatological destruction of all false worship is the obverse of universal true worship: 'every knee will bow... and every tongue confess that Jesus Christ is Lord' (Phil 2:10-11).</p>",
    "48": "<p>'Then the heavens and the earth, and all that is in them, shall sing for joy over Babylon, for the destroyers shall come against her from the north.' The cosmic rejoicing at the fall of the world empire — creation itself celebrates. Rev 19:1-7 presents the same heavenly celebration at Babylon's fall: 'Hallelujah! Salvation and glory and power belong to our God, for his judgments are true and just.' The joy of heaven and earth at justice done is the vindication of creation's longing (Rom 8:19-22).</p>",
    "49": "<p>'Babylon must fall for the slain of Israel, just as for Babylon have fallen the slain of all the earth.' The covenant principle of corresponding judgment: the blood of Israel demands Babylon's blood. 'It is mine to avenge; I will repay' (Rom 12:19; Deut 32:35). The cross is where YHWH repays sin's debt most fully: Christ bears the punishment that sin deserves, and through him the blood-price is paid for his people.</p>",
    "50": "<p>'You who have escaped the sword, go, do not stand still! Remember YHWH from afar, and let Jerusalem come into your mind.' The call to the survivors: remember Jerusalem even in the far country. The remembrance of the holy city sustains exile community. The NT equivalent is the Lord's Supper: 'do this in remembrance of me' (1 Cor 11:24-25) — the exilic community in the world sustains its identity through the remembrance meal until the Lord comes.</p>",
    "51": "<p>'We are put to shame, for we have heard reproach; dishonor has covered our face, for foreigners have come into the holy places of YHWH's house.' The shame of violated sanctuary — foreigners defiling what was holy. The NT sees this violation of holiness as the problem Christ solves: his body is the true sanctuary (John 2:21), and those who come to him are built into a holy temple (Eph 2:21-22; 1 Pet 2:5). The shame of violated holiness is replaced by the glory of inhabited holiness.</p>",
    "52": "<p>'Therefore, behold, the days are coming, declares YHWH, when I will execute judgment upon her idols.' The days of reckoning for every idol system — Babylon's religious complex will be utterly dismantled. The exclusive lordship of Christ is the NT's answer to every idol: 'we know that an idol has no real existence' (1 Cor 8:4) and 'you cannot drink the cup of the Lord and the cup of demons' (1 Cor 10:21). The elimination of false worship is both historical and eschatological.</p>",
    "53": "<p>'Though Babylon should mount up to heaven, and though she should fortify her strong height, yet destroyers would come from me against her, declares YHWH.' The Babel tower motif (Gen 11:4: 'let us build a tower with its top in the heavens') repeated — the empire that reaches for heaven will be brought down. The principle is fixed: 'God opposes the proud but gives grace to the humble' (Jas 4:6; 1 Pet 5:5). The humility of the incarnation — 'he emptied himself' (Phil 2:7) — is the obverse of Babylon's proud ascent.</p>",
    "54": "<p>'A voice! A cry from Babylon!' The sound of the city breaking. The voice of lamentation from the place of former triumph. Rev 18:22-23 echoes this: 'and the sound of harpists and musicians... will be heard in you no more.' The silencing of Babylon's voice is the preparation for the heavenly voice that says 'Behold, I am making all things new' (Rev 21:5).</p>",
    "55": "<p>YHWH is laying waste to Babylon and silencing her great voice — the noisy waters of the nations hush. The silencing of the multitudinous noise of the world system makes space for the still small voice (1 Kgs 19:12) and the clear voice of YHWH. In the new creation, 'death shall be no more, neither shall there be mourning, nor crying, nor pain anymore' (Rev 21:4).</p>",
    "56": "<p>'For a destroyer has come against her, against Babylon; her warriors are taken; their bows are broken in pieces, for YHWH is a God of retribution (<em>El gemulot</em>); he will surely repay.' <em>El gemulot</em> — the God of retributions/repayments — is the foundation of the NT's theology of judgment and grace. Paul quotes Deut 32:35 ('Vengeance is mine') in Rom 12:19 and 2 Thess 1:8 promises that the Lord Jesus will come 'inflicting vengeance on those who do not know God.' The God of retribution is the God and Father of our Lord Jesus Christ.</p>",
    "57": "<p>'I will make drunk her officials and her wise men, her governors, her commanders, and her warriors; they shall sleep a perpetual sleep and not wake, declares the King, whose name is YHWH of Hosts.' The intoxication of judgment — the cup the nations could not hold upright. The cup of YHWH's wrath is what Christ himself drank at Gethsemane-to-Calvary (Mark 14:36; 10:38), so that his people drink the cup of blessing at the Supper (1 Cor 10:16) rather than the cup of judgment.</p>",
    "58": "<p>The broad walls of Babylon will be utterly broken, her high gates set on fire — people toil in vain. The massive defensive architecture of the ancient world's greatest city reduced to rubble. 'Unless YHWH builds the house, those who build it labor in vain' (Ps 127:1). The city built without YHWH cannot stand; Christ builds a city that cannot be shaken (Heb 12:28; Rev 21:10-21).</p>",
    "59": "<p>The oracle given to Seraiah the staff officer when he went to Babylon with Zedekiah. The written prophecy entrusted to a royal official who will carry it to the place where it is to be proclaimed. The word of judgment travels with the faithful servant. The apostolic commission similarly entrusts the word to servants who carry it to the ends of the earth (Matt 28:19-20; 2 Tim 2:2).</p>",
    "60": "<p>Jeremiah writes in a book all the disaster that would come upon Babylon — a written oracle of judgment committed to text. The written word outlasts the prophet — the scripture that endures after the messenger has died. 'Heaven and earth will pass away, but my words will not pass away' (Matt 24:35). The reliability of the written prophetic word is the ground of faith that extends across centuries.</p>",
    "61": "<p>Seraiah is to go to Babylon and read the words aloud — public proclamation of YHWH's word in the very city it concerns. The prophetic word proclaimed inside Babylon is the seed of its judgment. Christ's proclamation of the kingdom in the very domain of the enemy — 'the prince of this world is cast out' (John 12:31) — follows the same pattern: announcing the defeat of the power that seems dominant.</p>",
    "62": "<p>'Then you shall say, &ldquo;O YHWH, you have said concerning this place that you will cut it off, so that nothing shall dwell in it, neither man nor beast.&rdquo;' The prophet's prayer that names the specific word of YHWH and asks for its fulfillment. This is model prayer: grounded in the specific promises of scripture ('you have said'), claiming what YHWH has committed to do. The NT's boldness in prayer is grounded the same way: 'if we ask anything according to his will... he hears us' (1 John 5:14-15).</p>",
    "63": "<p>'When you finish reading this book, tie a stone to it and cast it into the midst of the Euphrates.' The dramatic sign-act: the book sinks into the river that sustained Babylon's civilization. The sinking stone as the sign of permanent, irrevocable judgment. Rev 18:21 echoes this exactly: 'a mighty angel took up a stone like a great millstone and threw it into the sea, saying, &ldquo;So will Babylon the great city be thrown down with violence.&rdquo;'</p>",
    "64": "<p>'Thus shall Babylon sink, to rise no more, because of the disaster that I am bringing upon her.' The final word of the Babylon oracles: irreversible sinking, permanent disappearance. Rev 18:21-24 concludes its Babylon oracle the same way — 'will be found no more.' The oracle of Jeremiah 50-51 closes with this declaration, and the Book of Revelation closes its Babylon oracle with the same finality. The two ends of the prophetic canon form an inclusio around the doom of the world system that opposes YHWH's kingdom."
  },
  "52": {
    "1": "<p>Zedekiah was twenty-one years old when he became king and reigned eleven years. The opening of the historical appendix with the regnal formula — the standard marker of a king's accountability period. Every king's reign is bookended by YHWH's judgment. The NT applies this accountability to all human authority: 'each of us will give an account of himself to God' (Rom 14:12). The historical appendix places the narrative of Jeremiah inside the framework of covenant judgment on kings.</p>",
    "2": "<p>Zedekiah did evil in the sight of YHWH — the evaluative formula that determines the shape of the reign. The Deuteronomistic judgment applies the covenant standard to every king. Christ is the king who does what is right in the eyes of YHWH perfectly — 'which of you convicts me of sin?' (John 8:46). Every failed king in Israel's history is a negative foil for the perfectly righteous King.</p>",
    "3": "<p>'For because of the anger of YHWH things came to the point in Jerusalem and Judah that he cast them out from his presence.' The covenant expulsion — being cast from YHWH's presence is the ultimate punishment. This is the deepest meaning of the cross: 'My God, my God, why have you forsaken me?' (Matt 27:46) — Christ experiences the casting-out from YHWH's presence that Judah deserved, so that those in Christ will never be cast out (John 6:37).</p>",
    "4": "<p>Nebuchadnezzar comes against Jerusalem in Zedekiah's ninth year, fourth month — the siege begins. The specific date marks the historical precision of prophetic fulfillment. Jesus's prophecy of the temple's destruction (Matt 24:1-2) was fulfilled with the same historical precision in 70 AD. The God who predicted and brought the Babylonian siege also predicted and brought the Roman siege through the same pattern of covenant judgment.</p>",
    "5": "<p>The city is besieged until the eleventh year of Zedekiah — eighteen months of siege. The prolonged siege before the city falls anticipates the 'great tribulation' language of Matt 24:21. The endurance of the remnant through extended siege is the NT pattern of perseverance: 'the one who endures to the end will be saved' (Matt 24:13). The siege of the city of God's people is not the end but the passage to judgment and then restoration.</p>",
    "6": "<p>By the fourth month, the ninth day, famine prevails and there is no food. The famine inside the besieged city — the covenant curse realized (Deut 28:52-57). Christ feeds the hungry multitudes (Mark 6:30-44; 8:1-10) as signs that the covenant curses are being reversed. The one who said 'I am the bread of life' (John 6:35) reverses the famine of the besieged city with the abundance of the messianic feast.</p>",
    "7": "<p>The city wall is breached — the defensive boundary violated. The breach of the walls of Zion is the covenant catastrophe — the holy city exposed to the nations. The NT temple: 'not one stone will be left on another' (Matt 24:2). Christ predicts this with grief (Luke 19:41-44). The breach of every human fortification points to the need for the city whose builder and maker is God (Heb 11:10).</p>",
    "8": "<p>The king and his soldiers flee at night, but the Chaldeans pursue and overtake Zedekiah. The king who abandons his people to save himself — the hired hand who flees when the wolf comes (John 10:12-13). Christ is the Good Shepherd who does not flee: 'I am the good shepherd. The good shepherd lays down his life for the sheep' (John 10:11). Zedekiah's flight is the anti-pattern of the Shepherd's self-sacrifice.</p>",
    "9": "<p>Zedekiah is captured and brought to Nebuchadnezzar at Riblah, where judgment is pronounced against him. The king brought before the foreign judge for sentencing. The pattern of Christ before Pilate — the true King of Israel brought before the foreign judge. But the outcome is reversed: Pilate pronounces death over the innocent King, whose 'sentencing' leads to resurrection and vindication.</p>",
    "10": "<p>The king of Babylon slaughters Zedekiah's sons before his eyes and also slaughters the officials. The murder of the king's sons before his eyes — the horror of watching the dynasty's end before personal punishment. The death of the Davidic line's physical heirs seems to end the covenant promise of 2 Sam 7. But YHWH raises up the heir of David from outside the biological line threatened by Zedekiah's catastrophe: 'he who is descended from David according to the flesh' (Rom 1:3).</p>",
    "11": "<p>Zedekiah's eyes are put out, he is bound in bronze chains and taken to Babylon where he is imprisoned until his death. The blinding of the king — the leader who would not see YHWH's word now literally cannot see. Christ gives sight to the blind (John 9:1-7; Luke 4:18) as the reversal of every blinding judgment. The one who came to make the blind see is the Messianic answer to a tradition of blind kings who refused to see.</p>",
    "12": "<p>Nebuzaradan, the captain of the guard, comes to Jerusalem in the nineteenth year of Nebuchadnezzar. The Babylonian official enters the holy city as an instrument of divine judgment. The temple that was meant to embody YHWH's presence will now be stripped and burned. Every destruction of the earthly temple points to Christ as the permanent sanctuary: 'Destroy this temple and in three days I will raise it up' (John 2:19-21).</p>",
    "13": "<p>He burns the house of YHWH, the king's house, and all the houses of Jerusalem. The burning of YHWH's house — the most shocking act of the entire narrative. The destruction that seemed impossible (who would let YHWH's house burn?) becomes reality under covenant judgment. The NT equivalent: 'Your house is left to you desolate' (Matt 23:38). Every earthly sanctuary is provisional; the permanent sanctuary is Christ himself (Rev 21:22: 'the Lord God Almighty and the Lamb are its temple').</p>",
    "14": "<p>All the walls of Jerusalem are broken down by the Babylonian army. The walls of the holy city — Zion's defense and the physical marker of YHWH's chosen place — demolished. The New Jerusalem has no need of defensive walls in the same sense: 'its gates will never be shut by day' (Rev 21:25) because the enemies have been finally defeated. But it has walls of precious stone whose foundation is the apostles (Rev 21:14).</p>",
    "15": "<p>The poorest of the people and the rest of the population are carried into exile. The comprehensive deportation — no segment of society is exempt. The only ones left are the poorest of the poor to tend the land. The NT reversal: it is the poor in spirit who inherit the kingdom (Matt 5:3), and the powerless who are lifted up (Luke 1:52). The exodus of the wealthy and powerful creates space for what YHWH builds through the weak.</p>",
    "16": "<p>Nebuzaradan leaves some of the poorest as vinedressers and farmers. The small remnant tending the promised land while the main body is in exile — the theme of the faithful few maintaining the covenant presence while the majority are absent. The remnant theology that runs through the prophets reaches its NT apex: 'so too at the present time there is a remnant chosen by grace' (Rom 11:5).</p>",
    "17": "<p>The bronze pillars, stands, and sea in the temple are broken up and carried to Babylon. The great temple furniture that took Hiram's craftsmen years to create (1 Kgs 7:13-47) — destroyed in an afternoon. The bronze sea (the laver of purification), the pillars Jachin and Boaz — all stripped. Christ fulfills every function of the temple's purification apparatus: 'the blood of Jesus his Son cleanses us from all sin' (1 John 1:7) without bronze vessel or priest.</p>",
    "18": "<p>The pots, shovels, snuffers, bowls, dishes, and all the bronze vessels used in the temple service are taken. The complete inventory of liturgical equipment — the instruments of Israel's worship — catalogued as plunder. The NT equivalent: the elaborate temple apparatus is replaced by Christ himself, who is both priest and sacrifice, both altar and offering (Heb 9:11-14). What the bronze vessels pointed toward, Christ is.</p>",
    "19": "<p>The fire pans, basins, pots, lampstands, dishes, and bowls — silver and gold items — taken. The gold and silver of the temple stripped. The lampstands — whose fire symbolized the presence of YHWH — extinguished and carried away. In Revelation, the seven golden lampstands are the churches (Rev 1:20), and Christ walks among them (Rev 2:1). The light of YHWH's presence, once extinguished from the temple, is now distributed among the people of God.</p>",
    "20": "<p>The bronze of the two pillars, one sea, and twelve bronze bulls under the sea — too great to weigh. The massive scale of the temple's bronze metalwork. The sheer material weight of what Israel devoted to YHWH's worship was enormous. The NT asks for a living sacrifice: 'present your bodies as a living sacrifice, holy and acceptable to God, which is your spiritual worship' (Rom 12:1). The materiality of worship shifts from bronze and gold to the bodies and lives of believers.</p>",
    "21": "<p>Each pillar was eighteen cubits high with a capital of five cubits — the description of the bronze columns. The architectural precision of the temple construction described here in its dismantling. The temple that was built with such care (1 Kgs 7:15-22) is stripped with such thoroughness. What took generations to build was destroyed in a day — illustrating that no human construction lasts apart from YHWH's blessing.</p>",
    "22": "<p>The capital was of bronze, five cubits high, with a network and pomegranates all round — the decorative detail of the destroyed temple. The precision of the record of destruction mirrors the precision of the original construction record. YHWH accounts for what was given to him in worship and what was taken away in judgment. The detail of what is lost increases the pathos — and intensifies the promise of the indestructible temple to come.</p>",
    "23": "<p>There were ninety-six pomegranates on the sides; all the pomegranates were a hundred upon the surrounding network. The pomegranate — symbol of fertility, of the promised land, of covenantal abundance (Num 13:23) — torn down and carried to Babylon. The symbols of covenant blessing stripped away. Christ restores fruitfulness: 'I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit' (John 15:5).</p>",
    "24": "<p>Seraiah the chief priest, Zephaniah the second priest, and three keepers of the threshold are taken. The priestly leadership of Israel — those responsible for the worship of YHWH — captured and led away. The Levitical priesthood ends in exile. Christ becomes the permanent high priest 'after the order of Melchizedek' (Heb 7:11-17) — not the Levitical order whose representatives were taken to Babylon but a permanent priesthood that requires no succession.</p>",
    "25": "<p>The commander of Babylon takes the official who was over the soldiers, seven royal advisors, the secretary in charge of military conscription, and sixty men of the people. The complete administrative apparatus of Judah decapitated — the entire governing class removed. The kingdom stripped of its human infrastructure. Christ rebuilds from the ground up: 'God chose what is low and despised in the world... to bring to nothing things that are' (1 Cor 1:28).</p>",
    "26": "<p>Nebuzaradan takes them to the king of Babylon at Riblah for judgment. The leadership of Judah brought before the foreign king for sentencing — the covenant community's human authority structures submit to foreign power as the consequence of covenant failure. The NT's counter-claim: 'the Father judges no one, but has given all judgment to the Son' (John 5:22). The judgment seat is ultimately Christ's, not any earthly king's.</p>",
    "27": "<p>The king of Babylon strikes them down and puts them to death at Riblah. The execution of Judah's leadership — the human structures of the covenant people eliminated. The destruction of every human institutional structure that the community depended on forces the question: what remains? The answer the Psalms give is: YHWH himself. 'God is our refuge and strength, a very present help in trouble' (Ps 46:1) — the answer to the destruction of every human institution.</p>",
    "28": "<p>In the seventh year of Nebuchadnezzar: three thousand twenty-three persons of Judah carried into exile. The first deportation census — a specific, recorded number. YHWH keeps the census even of exiles: not one is forgotten. 'Even the hairs of your head are all numbered' (Luke 12:7). The God who counts the hairs counts the exiles; the God who counts the exiles counts his people in every generation.</p>",
    "29": "<p>In Nebuchadnezzar's eighteenth year: eight hundred thirty-two persons from Jerusalem. The second deportation — the wave following the destruction of the city. The specific numbers serve as testimony: these were real people, individuals with names and families, not abstractions. The incarnation affirms the same particularity: 'the Word became flesh and dwelt among us' (John 1:14) — God enters specific, numbered, mortal particularity.</p>",
    "30": "<p>In the twenty-third year of Nebuchadnezzar: seven hundred forty-five persons carried away by Nebuzaradan — four thousand six hundred in all. The total census of the exile: 4,600 individuals. A remnant — small against the total population. The remnant through judgment becomes the seed of the new community. The NT church is planted in the same way: a small community chosen from the larger, entrusted with the word and the promise of universal expansion (Acts 1:15: 120 people; Matt 13:31-32: the mustard seed).</p>",
    "31": "<p>In Jehoiachin's thirty-seventh year of exile, Evil-merodach the king of Babylon lifts up Jehoiachin's head — graciously releases him in the year he became king. The elevation of the imprisoned Davidic king — lifted from prison to a place of honor at the foreign king's table. This is one of the most striking types of resurrection and exaltation in the OT: the captive king lifted up echoes Christ lifted from the tomb. The verbal pattern — <em>nasa rosh</em> (lift up the head) — is used for the chief butler's restoration in Gen 40:13.</p>",
    "32": "<p>Evil-merodach speaks kindly to Jehoiachin and gives him a throne above the thrones of the other kings in Babylon. Elevated above all the other captive kings — a position of honor above his peers in exile. This anticipates the resurrection exaltation of Christ: 'God has highly exalted him and bestowed on him the name that is above every name' (Phil 2:9). The imprisoned Davidic heir lifted to the highest seat is a type of the risen King of David's line.</p>",
    "33": "<p>Jehoiachin's prison garments are changed — he dines regularly at the king's table all the days of his life. The change of garments is a sign of status reversal: from prisoner's clothes to royal-court attire. The NT uses garment-change as a resurrection symbol: 'putting on Christ' (Gal 3:27; Col 3:9-10), the white robes of the saints (Rev 6:11; 7:13-14). The change from prison garments to court clothing is the shadow of the change from mortality to immortality (1 Cor 15:53-54).</p>",
    "34": "<p>'And every day of his life he was given a regular allowance by the king of Babylon, up to the day of his death.' The daily provision guaranteed — sustained for the rest of his earthly life by the king's gift. The type of eschatological sustenance: the heavenly provision that never fails. 'Your Father knows what you need before you ask him' (Matt 6:8); 'Give us this day our daily bread' (Matt 6:11). The daily allowance from the king in exile points to the daily provision of the Father for his exiled people — until the day of death gives way to resurrection.</p>"
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
