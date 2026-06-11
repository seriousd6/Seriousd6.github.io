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
  "10": {
    "1": "<p>The opening command to 'hear what YHWH speaks to you, O house of Israel' prefigures the Christological claim that YHWH's ultimate speech has come in his Son: 'In many and various ways God spoke of old to our fathers by the prophets, but in these last days he has spoken to us by his Son' (Heb 1:1-2). The word to Israel in Jeremiah's time is preliminary; the full Word is the incarnate Logos (John 1:1,14).</p>",
    "2": "<p>'Do not learn the way of the nations, and do not be dismayed at the signs of the heavens.' The contrast between Israel's calling and the nations' astrology anticipates Paul's contrast between the wisdom of the world and the wisdom of God revealed in Christ crucified (1 Cor 1:20-25). The 'signs of the heavens' that terrify pagans are subject to the Creator whom Christ embodies (Col 1:16-17).</p>",
    "3": "<p>The idol-making process described here — cutting a tree, shaping it, adorning it with silver and gold — is the polemic background for Paul's indictment in Rom 1:21-23: 'They exchanged the glory of the immortal God for images resembling mortal man and birds and animals.' The creation-to-idol trajectory that Jeremiah mocks is the spiritual condition from which Christ comes to rescue humanity.</p>",
    "5": "<p>'They cannot speak... they cannot walk... do not be afraid of them, for they cannot do evil, neither is it in them to do good.' The absolute impotence of idols establishes by contrast the power of Christ — who speaks with authority (Matt 7:29), heals, casts out evil, and does good everywhere he went (Acts 10:38). The idol is nothing; Christ is the power of God and the wisdom of God (1 Cor 1:24).</p>",
    "6": "<p>'There is none like you, O YHWH; you are great, and your name is great in might.' The incomparability of YHWH confessed here is re-centered in Christ in the NT — 'in him the whole fullness of deity dwells bodily' (Col 2:9). The divine name's greatness is revealed in the name of Jesus, at which every knee bows (Phil 2:9-11).</p>",
    "7": "<p>'Who would not fear you, O King of the nations? For this is your due.' The kingship of YHWH over all nations is the premise for the Great Commission: Christ as risen Lord sends his disciples to all nations precisely because 'all authority in heaven and on earth has been given to me' (Matt 28:18-20) — the universally-due fear of the divine King is now channeled through the Son's reign.</p>",
    "10": "<p><strong>The living God</strong> (<em>Elohim chayyim</em>) who makes the earth quake at his wrath — this title is specifically applied to Jesus in his encounter with Peter: 'You are the Christ, the Son of the living God' (Matt 16:16). The confession identifies Jesus as the incarnate presence of the very God whom the nations have no right to worship but must. 'The true God and eternal life' of 1 John 5:20 identifies the Son with this title.</p>",
    "11": "<p>This verse, uniquely in Aramaic within Jeremiah's Hebrew text, declares the end of gods who did not make heaven and earth. The NT judgment on 'so-called gods' (1 Cor 8:5-6) reaches its definitive expression in Christ: 'yet for us there is one God, the Father... and one Lord, Jesus Christ, through whom are all things and through whom we exist.' What Jeremiah announced in Aramaic to the nations, Christ's lordship enacts eschatologically.</p>",
    "12": "<p>'It is he who made the earth by his power, who established the world by his wisdom, and by his understanding stretched out the heavens.' The Creator-God of Jeremiah's doxology is identified in the NT as the one through whom the Father created — 'through him all things were made' (John 1:3); 'in him all things were created, in heaven and on earth' (Col 1:16). The Logos who was with God in creation became flesh in Jesus.</p>",
    "13": "<p>The thunder, rain, lightning, and wind deployed by YHWH the creator prefigure Christ's authority over weather — stilling the storm (Mark 4:39-41), prompting the disciples' question: 'Who then is this, that even wind and sea obey him?' The answer Jeremiah already knows: this is the incomparable God, maker of all (v6-7). Jesus's nature miracles are epiphanies of his creative identity.</p>",
    "14": "<p>'Every man is stupid and without knowledge; every goldsmith is put to shame by his idols.' The comprehensive stupidity of human wisdom without God is the condition Christ addresses in the incarnation. 'The world did not know God through wisdom' (1 Cor 1:21) — the failure of human knowledge (<em>da'at</em>) calls for the Teacher who is himself the truth (John 14:6).</p>",
    "16": "<p>'Not like these is he who is the portion of Jacob, for he is the one who formed all things, and Israel is the tribe of his inheritance; YHWH of Hosts is his name.' The God who is both creator of all and personal <em>chelek</em> (portion/inheritance) of his people is the pattern for Christ who is 'all, and in all' (Col 3:11) and the inheritance of the saints (Eph 1:11). The name <em>YHWH Tzvaot</em> is the name behind the name of Jesus.</p>",
    "21": "<p>'The shepherds are stupid and do not inquire of YHWH; therefore they have not prospered, and all their flock is scattered.' The failure of Israel's shepherds sets up the promised contrast: YHWH himself will shepherd (Ezek 34:11-16), fulfilled in Christ who declares 'I am the good shepherd' (John 10:11). Every scattered flock in the OT is a preparation for Christ's commission to gather 'the lost sheep of the house of Israel' (Matt 15:24) and then 'other sheep' beyond the fold (John 10:16).</p>",
    "23": "<p>'I know, O YHWH, that the way of man is not in himself, that it is not in man who walks to direct his steps.' This confession of human incapacity to self-direct anticipates Christ's claim 'I am the way' (John 14:6). The person who cannot find their own way needs the Way himself — not a teaching about direction but the personal guide who leads to the Father. Jeremiah's prayer for YHWH to correct (<em>yasser</em>) him gently becomes the ministry of the Spirit who leads into all truth (John 16:13).</p>",
    "24": "<p>'Correct me, O YHWH, but in justice; not in your anger, lest you bring me to nothing.' The prayer for correction in <em>mishpat</em> (justice) rather than <em>af</em> (wrath) anticipates the NT distinction: 'There is no condemnation for those in Christ Jesus' (Rom 8:1). Christ absorbs the wrath so that the correction remaining for believers is the loving discipline of the Father, not forensic punishment (Heb 12:5-11).</p>",
    "25": "<p>'Pour out your wrath on the nations that know you not... for they have devoured Jacob.' The prayer for divine wrath on the nations reaches its eschatological fulfillment through Christ — not the wrath of military judgment (the Babylonian pattern) but the wrath of the final day. Simultaneously, Christ's mission is that those 'nations that do not call on your name' should come to know YHWH (Matt 28:19), transforming Jeremiah's enemies-of-Jacob into worshipers of God.</p>"
  },
  "11": {
    "1": "<p>The word 'that came to Jeremiah from YHWH' frames the chapter as legal covenant-prosecution. The Christological fulfillment runs through Heb 8-10: Christ is the mediator of the new covenant that supersedes the broken Sinai covenant. The repeated accusation 'they did not listen' (vv4,7,8) that triggers covenant judgment is the same hardness Jesus laments: 'O Jerusalem, Jerusalem... how often would I have gathered your children... but you were not willing' (Matt 23:37).</p>",
    "4": "<p>'Obey my voice, and do all that I command you. So shall you be my people, and I will be your God.' The covenant formula (<em>I will be your God; you shall be my people</em>) that the Sinai covenant could not permanently secure is the content Christ comes to establish permanently. Rev 21:3: 'Behold, the dwelling of God is with man... he will be their God and they will be his people.' The formula Jeremiah quotes from Sinai is fulfilled in the new creation.</p>",
    "5": "<p>'That I may confirm the oath that I swore to your fathers, to give them a land flowing with milk and honey.' The land promise swore to Abraham finds its NT reinterpretation in Heb 11:16 and Rev 21: the patriarchs were looking for 'a better country, that is, a heavenly one.' Christ fulfills the land promise by giving not Canaan but the new creation — the 'heavenly homeland' that the material land always symbolized.</p>",
    "8": "<p>'They did not obey or incline their ear, but every one walked in the stubbornness of his evil heart.' The anthropological diagnosis — the stubborn, autonomous heart — is precisely what the new covenant addresses (31:33: 'I will put my law within them and write it on their hearts'). Christ came not just to announce but to enact the heart-transformation that Sinai could not produce, through the Spirit he pours out (Titus 3:5-6).</p>",
    "11": "<p>'I will bring disaster upon them that they cannot escape. Though they cry to me, I will not listen to them.' This divine refusal to hear echoes in Jesus's warning about the prayer of the unrepentant (Matt 7:21-23: 'I never knew you') and the closed door after the wedding (Matt 25:10-12). Covenant abandonment has a real telos — the moment when mercy's time has run out — which Christ announced was coming on that generation (Matt 23:38).</p>",
    "14": "<p>'Therefore do not pray for this people, or lift up a cry or prayer for them, for I will not listen when they call to me in their trouble.' The prohibition of intercession marks the depth of the breach — but Christ's intercession transcends this. Where Jeremiah was forbidden to intercede for stubborn Israel, Christ 'always lives to make intercession' for those who come to God through him (Heb 7:25). The new covenant opens an intercession that the old covenant's failure could not sustain.</p>",
    "15": "<p>'What right has my beloved in my house?' The beloved (<em>yedidati</em>) — Israel — has become unfaithful in YHWH's house (temple). Christ comes as the Son who has every right in the Father's house (John 2:16: 'Do not make my Father's house a house of trade'); he is the true <em>yedid</em> (beloved) who cleanses the temple and his own body becomes the true temple (John 2:19-21).</p>",
    "19": "<p><strong>'I was like a docile lamb led to the slaughter'</strong> (<em>keves aluf yuval litvoach</em>): one of the most direct proto-passion statements in the OT. Isaiah 53:7 uses the same lamb-to-slaughter image for the Suffering Servant, and John 1:29 identifies Jesus explicitly as 'the Lamb of God who takes away the sin of the world.' Jeremiah's experience of innocent suffering at the hands of his own people — from Anathoth, his hometown — prefigures Christ's rejection in Nazareth and Jerusalem. 'I did not know it was against me they devised schemes': the ignorance of the plot parallels the innocence of the Lamb.</p>",
    "20": "<p>'O YHWH of Hosts, who judges righteously, who tests the heart and the mind, let me see your vengeance upon them, for to you have I committed my cause.' Jeremiah entrusts his cause to YHWH the just judge — as Peter describes Christ's passion: 'He committed no sin... but continued entrusting himself to him who judges justly' (1 Pet 2:22-23). Christ fulfills the pattern not just by suffering innocently but by entrusting himself to the Father through the passion (Luke 23:46: 'Father, into your hands I commit my spirit').</p>",
    "21": "<p>'Do not prophesy in the name of YHWH, or you will die by our hand.' The threat of death for speaking YHWH's word — from Jeremiah's own hometown Anathoth — is a narrative rehearsal of the Nazareth rejection (Luke 4:24-29: 'No prophet is acceptable in his hometown') and ultimately of the Sanhedrin's determination to kill Jesus for his prophetic-messianic claims. The prophet's life is at stake for naming YHWH in the world.</p>",
    "23": "<p>The destruction of the men of Anathoth in the year of their punishment (<em>shnat pequddatam</em>) — the appointed accountability day — anticipates the theme of the 'day of visitation' that Jesus places in Jerusalem's future (Luke 19:44: 'because you did not know the time of your visitation'). The <em>paquddah</em> that Anathoth missed is the same visitation-logic applied to the generation that rejected its Messiah.</p>"
  },
  "12": {
    "1": "<p>'Righteous are you, O YHWH, when I complain to you; yet I would plead my case before you.' Jeremiah's bold theodicy prayer — 'Why does the way of the wicked prosper?' — is the prayer of the righteous sufferer that reaches its ultimate expression in Gethsemane (Matt 26:39-44) and on the cross (Psalm 22:1/Matt 27:46). Christ did not suppress the genuine anguish of innocent suffering but brought it fully before the Father, as Jeremiah models.</p>",
    "3": "<p>'But you, O YHWH, know me; you see me, and test my heart toward you.' The claim to be known by YHWH in the midst of suffering anticipates Christ's certainty of the Father's knowledge even in abandonment. The Father knows the Son completely (John 10:15); the resurrection is the Father's public vindication of this mutual knowledge, confirming that the righteous sufferer's trust was not misplaced.</p>",
    "5": "<p>'If you have raced with men on foot, and they have wearied you, how will you compete with horses?' YHWH's counter-challenge to Jeremiah — you have not yet seen real suffering — has a Christological echo in Heb 12:3-4: 'Consider him who endured such hostility from sinners against himself, so that you may not grow weary or fainthearted. In your struggle against sin you have not yet resisted to the point of shedding your blood.' The Christ-model of endurance surpasses all prophetic suffering.</p>",
    "7": "<p>'I have forsaken my house; I have abandoned my heritage.' The divine abandonment of the temple and land — the most agonizing theological claim in Jeremiah (cf. Ezek 10-11) — finds its personal NT concentration in Christ's cry: 'My God, my God, why have you forsaken me?' (Matt 27:46). The <em>azav</em> (abandon/forsake) of the sanctuary in Jeremiah 12 is the same root as in Psalm 22:1 that Christ utters on the cross. The macroscopic abandonment of the land is concentrated and borne personally by Christ.</p>",
    "10": "<p>'Many shepherds have destroyed my vineyard; they have trampled down my portion.' The destroyed vineyard is the direct background for Christ's parable of the wicked tenants (Matt 21:33-46) — YHWH's vineyard was entrusted to tenant-shepherds who destroyed it. Christ's parable updates the Isaianic and Jeremianic vineyard metaphor (Isa 5; Jer 12): the son is sent last, and they kill him too. The vineyard will be given to others (Matt 21:43).</p>",
    "11": "<p>'They have made it a desolation; desolate, it mourns to me. The whole land is made desolate, but no man lays it to heart.' The mourning land (<em>avlah alehu ha'aretz</em>) parallels the cosmic lamentation at Christ's death: 'The sun's light failed, and the curtain of the temple was torn in two' (Luke 23:44-45). Creation's mourning at sin's devastation reaches its apex at the cross, where the fullness of human covenant-breaking is concentrated.</p>",
    "14": "<p>'I will pluck up the house of Judah from among them, and after I have plucked them up I will return and have compassion on each of them, and I will bring them again, each to his heritage and each to his land.' The restoration promise — uprooting leading to replanting — operates on the pattern Christ enacts: through death (uprooting) comes resurrection life (replanting). Paul uses the olive-tree metaphor for the same logic: broken off to be grafted in (Rom 11:17-24).</p>",
    "15": "<p>'And it shall come to pass after I have plucked them up, I will again have compassion on them, and I will bring them again, each to his heritage.' The extension of restoration to the nations — if they learn the ways of YHWH — anticipates the eschatological mission: Christ's commission is that all nations be discipled (Matt 28:19), bringing them from false gods to the true God, and thus into the inheritance.</p>",
    "17": "<p>'But if any nation will not listen, then I will utterly pluck up and destroy that nation, declares YHWH.' The conditional judgment on non-listening nations is the same covenantal logic Jesus applies in Matthew 10:14-15: shaking the dust, declaring that Sodom and Gomorrah will fare better than cities that do not receive the word. The <em>nata'</em> (uproot/pluck) of the non-listening nation is the outcome Christ warns against.</p>"
  },
  "13": {
    "1": "<p>The linen waistband (<em>ezor pishta</em>) pressed against YHWH's loins — the most intimate garment — is the sign-act of Israel's covenantal purpose: to cling to YHWH as a waistband clings to the body (v11). In the NT, the covenant-garment metaphor is transformed: believers 'put on Christ' (Gal 3:27; Rom 13:14), Christ becomes the garment of righteousness. The sign-act of the ruined waistband is reversed by the new-covenant garment that cannot be corrupted.</p>",
    "9": "<p>'Thus will I ruin the pride of Judah and the great pride of Jerusalem.' The destruction of national pride is the condition for receiving grace. The Beatitudes begin 'Blessed are the poor in spirit' (Matt 5:3) — the bankruptcy of self-reliance that the ruined waistband enacts is the prerequisite for the kingdom. Christ brings not the reinforcement of human pride but its deconstruction as the path to covenant restoration.</p>",
    "11": "<p>'For as the waistband clings to the loins of a man, so I made the whole house of Israel and all of Judah cling to me, declares YHWH, that they might be for me a people, a name, a praise, and a glory.' The original covenant purpose — intimate adhesion to YHWH, being his glory and praise — is what sin has destroyed and Christ comes to restore. The church as 'a chosen race, a royal priesthood, a holy nation' (1 Pet 2:9) is the restored covenant people whose clinging to Christ fulfills what the linen waistband could not.</p>",
    "13": "<p>'I will fill with drunkenness all the inhabitants of this land.' The divine wine of judgment — here judgment on covenant-breakers — becomes in the NT the Supper's wine that is the blood of the new covenant (Matt 26:27-28). The cup that the wicked receive as wrath (Rev 14:10) is the same cup Christ drains for his people (Mark 10:38; 14:36), converting the judgment-cup into the covenant-cup.</p>",
    "14": "<p>'I will not pity or spare or have compassion, that I should not destroy them.' The suspended compassion that Jeremiah announces as judgment on the unrepentant is the necessary backdrop for Paul's declaration: 'While we were yet sinners, Christ died for us' (Rom 5:8). Compassion is not merely withheld — it is channeled through the cross, where the wrath that would destroy the unrepentant falls on the Son, allowing compassion to flow to the repentant.</p>",
    "15": "<p>'Hear and give ear; be not proud, for YHWH has spoken.' The repeated call to humble hearing throughout Jeremiah finds its NT fulfillment in Christ as the One to whom all must listen: 'This is my beloved Son; listen to him' (Mark 9:7; cf. Deut 18:15 — the prophet like Moses). The pride that refuses to listen is the same pride that puts the Son to death; the humility that hears becomes salvation.</p>",
    "16": "<p>'Give glory to YHWH your God before he brings darkness, before your feet stumble on the twilight mountains.' The call to give glory before judgment — before the darkness closes in — is the missionary urgency of the NT. In Rev 14:7, the angel flying in midheaven calls: 'Fear God and give him glory, for the hour of his judgment has come.' Christ opens the window of grace; the call to glorify YHWH before darkness is the shape of every evangelistic appeal.</p>",
    "17": "<p>'But if you will not listen, my soul will weep in secret for your pride.' Jeremiah's secret weeping over the pride that will bring destruction is an unmistakable type of Christ's weeping over Jerusalem (Luke 19:41-44): 'When he drew near and saw the city, he wept over it, saying, &ldquo;Would that you, even you, had known on this day the things that make for peace!&rdquo;' Both Jeremiah and Jesus weep over the same stubborn city for the same fatal pride.</p>",
    "23": "<p>'Can the Ethiopian change his skin or the leopard his spots? Then also you can do good who are accustomed to do evil.' The impossibility of self-reformation — the entrenched habit of sin that cannot be self-corrected — is the problem Christ addresses not by human self-improvement but by new creation: 'If anyone is in Christ, he is a new creation; the old has passed away; behold, the new has come' (2 Cor 5:17). What the leopard cannot do, the Spirit effects.</p>",
    "25": "<p>'This is your lot, the portion I have measured out to you, declares YHWH, because you have forgotten me and trusted in lies.' Forgetting YHWH — the covenant amnesia that produces idolatrous trust in lies — is addressed by Christ who calls himself 'the truth' (John 14:6). The Spirit he sends is the Spirit of truth who will 'bring to your remembrance all that I have said to you' (John 14:26) — the covenantal remembering that reverses Jeremiah's covenantal forgetting.</p>",
    "27": "<p>'Woe to you, O Jerusalem! How long will it be before you are made clean?' The closing lament — the city that cannot cleanse itself — anticipates both John the Baptist's baptism of repentance and Christ's declaration 'I will; be clean' to the leper (Mark 1:41). The impossibility of self-cleansing that Jeremiah laments is resolved by the one who washes his disciples' feet (John 13:8-10) and whose blood cleanses from all sin (1 John 1:7).</p>"
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
