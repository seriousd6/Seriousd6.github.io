"""
Lamentations + all 12 Minor Prophets — all four layers.
These complete the OT portion of the Z Commentary Suite.
Key NT: Hosea (son called out of Egypt; Lo-ammi/Ammi), Joel 2 (Pentecost),
        Amos (Day of the LORD, Amos 9:11 Davidic restoration),
        Jonah (sign of Jonah), Micah 5:2 (Bethlehem), Zech 9:9 (triumphal entry),
        Zech 12:10 (pierced one), Mal 3:1 (messenger), Mal 4:5 (Elijah).
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

# ============================
# LAMENTATIONS
# ============================

LAM_ECHO = {
  "3": {
    "22": [
      {"type": "allusion", "target": "Heb 13:8", "note": "The steadfast love of the LORD never ceases; his mercies never come to an end — the great confession of YHWH's faithfulness in the midst of Jerusalem's total destruction; Jesus Christ is the same yesterday and today and forever (Heb 13:8) is the new covenant form of the same confession: divine steadfast love, permanent and unending"},
      {"type": "allusion", "target": "Lam 3:26", "note": "It is good that one should wait quietly for the salvation of the LORD — the sufferer's renewed hope after total collapse; the salvation (yeshuah) that Lamentations awaits is the name of Jesus"}
    ]
  }
}

LAM_ORIGINAL = {
  "3": {
    "22": "<p><strong>chasde YHWH ki lo tamnu ki lo chalu rachamav</strong>: 'The steadfast love [<em>chesed</em>] of the LORD never ceases; his mercies [<em>rachamim</em>] never come to an end.' This confession (Lam 3:22-24) is the theological center of Lamentations — placed at the exact midpoint of the book (the acrostic structure of ch. 3 is 22×3 = 66 verses, and v. 22 is the centerpiece). Its context makes it remarkable: Lamentations is the most sustained expression of grief and lamentation in Scripture, written in the immediate aftermath of Jerusalem's destruction, yet its center is a confession of divine steadfast love. The structure embodies the theology: suffering and praise, grief and faith, can coexist — and at the center of the darkest book is the brightest confession.</p>"
  }
}

LAM_CONTEXT = {
  "1": {
    "1": "<p>Lamentations is a collection of five poems mourning the destruction of Jerusalem in 586 BCE. Four are acrostics (following the Hebrew alphabet), reflecting the artistic discipline of theological grief: the structure provides form for what might otherwise be formless pain. Traditionally attributed to Jeremiah (who is associated with Lamentations in 2 Chr 35:25 and the LXX introduction), the poems articulate Israel's grief, confession, and ongoing hope in YHWH's steadfast love. The book is read in Jewish tradition on Tisha B'Av, the fast commemorating the temple's destruction. Its influence on the NT's passion narrative is significant: the description of Jerusalem's suffering (1:12: 'Is it nothing to you, all you who pass by?') is echoed in the passion accounts; Christ's passion is interpreted through the Lamentations framework of righteous suffering.</p>"
  }
}

LAM_CHRIST = {
  "1": {
    "12": "<p>A type: 'Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow, which was brought upon me, which the LORD inflicted on the day of his fierce anger.' The suffering of Jerusalem — the Daughter of Zion who has suffered at YHWH's hand for her sins — is one of the OT's primary types of Christ's passion. The NT passion accounts use the Lamentations framework: the mockers who wag their heads at the crucified Jesus echo Lamentations (Lam 2:15: 'all who pass by clap their hands at you; they hiss and wag their heads at the daughter of Jerusalem'; Matt 27:39). But the typological inversion is crucial: Jerusalem suffers for her own sins; Christ suffers for ours. The language of innocent suffering that Lamentations applies to the city becomes, in the NT, applicable to the one who is truly innocent.</p>"
  },
  "3": {
    "22": "<p>A direct revelation: 'The steadfast love of the LORD never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness.' This confession — the OT's most concentrated statement of divine covenantal faithfulness — is the foundation of NT assurance. Paul says 'neither death nor life ... shall be able to separate us from the love of God in Christ Jesus our Lord' (Rom 8:38-39): the love the Preacher of Lamentations confessed in the ruins of Jerusalem is the love that cannot be severed by anything. Christ's resurrection is the supreme demonstration of the <em>chesed</em> that Lamentations confesses: even through the cross — the ultimate expression of divine wrath — the steadfast love did not fail.</p>"
  }
}

# ============================
# HOSEA
# ============================

HOSEA_ECHO = {
  "1": {
    "10": [
      {"type": "fulfillment", "target": "Rom 9:25-26", "note": "And in the place where it was said to them You are not my people it shall be said to them Children of the living God — Paul cites Hos 1:10 and 2:23 as OT support for Gentile inclusion: what YHWH said about restoring estranged Israel is applied to the calling of the Gentiles into the people of God; the not-my-people becoming my-people is the inclusive dynamic of the new covenant"}
    ]
  },
  "2": {
    "23": [
      {"type": "fulfillment", "target": "1 Pet 2:10", "note": "I will say to Lo-ammi You are my people; and he shall say You are my God — Peter applies Hosea's restoration promise to the church: once you were not a people, but now you are God's people; the covenant formula's restoration (you are my people/I am your God) is fulfilled in Christ's reconciling work"}
    ]
  },
  "6": {
    "6": [
      {"type": "fulfillment", "target": "Matt 9:13", "note": "For I desire steadfast love and not sacrifice, the knowledge of God rather than burnt offerings — Jesus quotes Hos 6:6 twice (Matt 9:13; 12:7) in defense of his association with sinners and his disciples' plucking grain on the Sabbath; the priority of covenant love over ritual is Jesus's critique of Pharisaic misapplication of the law"}
    ]
  },
  "11": {
    "1": [
      {"type": "fulfillment", "target": "Matt 2:15", "note": "Out of Egypt I called my son — Matthew cites Hos 11:1 as fulfilled in the flight to Egypt and the return: as YHWH called Israel (his son) out of Egypt in the Exodus, so Jesus (the true Son) recapitulates Israel's history; Jesus is the new Israel who succeeds where Israel failed"}
    ]
  }
}

HOSEA_ORIGINAL = {
  "11": {
    "1": "<p><strong>ki naar Yisrael vaehavuhu umimitzraim qarati livni</strong>: 'When Israel was a child, I loved him, and out of Egypt I called my son.' Matthew's citation of Hos 11:1 in Matt 2:15 is one of the NT's most discussed typological uses of the OT — because Hosea 11:1 in its original context is clearly not a predictive prophecy but a historical statement about the Exodus. Matthew's method is typological recapitulation: Jesus is the new Israel, the true Son of God who goes down to Egypt and is called out again; what happened to the nation in type is fulfilled in the person of the Messiah in antitype. This reading was not arbitrary: it was grounded in the OT's identification of Israel as YHWH's 'son' (Exod 4:22-23) and the expectation that the Messiah would recapitulate and fulfill Israel's story.</p>"
  }
}

HOSEA_CONTEXT = {
  "1": {
    "1": "<p>Hosea prophesied in the northern kingdom of Israel ca. 755-725 BCE, the final decades before Assyria destroyed Samaria (722 BCE). His marriage to Gomer — a woman who proved unfaithful — is the enacted metaphor of YHWH's relationship with Israel: YHWH's faithful covenant love (hesed) in the face of Israel's persistent idolatry (harlotry). The marriage metaphor for the YHWH-Israel covenant (developed also in Jeremiah 2-3, Ezekiel 16, and Isaiah 54) is Hosea's central theological contribution: covenant violation is not merely law-breaking but adultery, a betrayal of the intimate covenant-love relationship. The NT develops the bridegroom-bride metaphor for Christ-church (Eph 5:25-32; Rev 19:7-9) directly in line with Hosea's framework.</p>"
  }
}

HOSEA_CHRIST = {
  "11": {
    "1": "<p>A type: 'Out of Egypt I called my son.' The Hosea 11:1 citation in Matthew 2:15 reveals the NT's typological method: the Exodus — YHWH calling Israel his son out of Egypt — is recapitulated in miniature by the holy family's flight to Egypt and return. Jesus is the true Son of God where Israel was the representative son; Jesus is the true Israel who succeeds where Israel repeatedly failed. The NT development of this recapitulation: Israel spent 40 years in the wilderness and failed (Num 14); Jesus spent 40 days in the wilderness and prevailed (Matt 4). Israel crossed the Jordan under Joshua and conquered imperfectly; Jesus was baptized in the Jordan and accomplished the complete conquest of sin and death. The Exodus story is not just a historical event that Jesus parallels — it is the template YHWH designed to interpret what his Son would do.</p>"
  }
}

# ============================
# JOEL
# ============================

JOEL_ECHO = {
  "2": {
    "28": [
      {"type": "fulfillment", "target": "Acts 2:16-21", "note": "I will pour out my Spirit on all flesh — Peter on the Day of Pentecost cites Joel 2:28-32 as fulfilled in the Spirit's outpouring: this is what was uttered through the prophet Joel; the universal Spirit-gift (all flesh, sons and daughters, young and old, male and female, servant and free) is the new covenant's democratization of prophetic access to God"},
      {"type": "fulfillment", "target": "Acts 2:21", "note": "And it shall come to pass that everyone who calls on the name of the LORD shall be saved — Joel's salvation promise is cited by Peter (Acts 2:21) and Paul (Rom 10:13) as the OT basis for universal gospel accessibility: the LORD whose name saves is identified with Jesus, Lord and Christ (Acts 2:36)"}
    ]
  }
}

JOEL_ORIGINAL = {
  "2": {
    "28": "<p><strong>vehaya acharei chen eshpoch et ruchi al kol basar venivve'u bneichem uvnotechem ziknechem chalomot yachalomun bachureichem cheziyonot yiru</strong>: 'And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy, your old men shall dream dreams, and your young men shall see visions.' The universal Spirit-outpouring prophesied in Joel 2:28-32 is the most significant single prophecy cited in the NT's account of Pentecost. The key phrase is <em>kol basar</em> (all flesh): unlike the selective, temporary Spirit-anointing of specific judges, prophets, and kings in the OT, the new covenant Spirit will be given to all — removing the mediatorial hierarchy that required prophets and priests to relay YHWH's word to the people. This is Jeremiah 31:34 ('no longer will each person teach his neighbor, for they will all know me') from the pneumatological angle.</p>"
  }
}

JOEL_CONTEXT = {
  "1": {
    "1": "<p>Joel is undated — no contemporary king is mentioned — but it is typically placed in the post-exilic period (late 5th-early 4th century BCE) based on its references to the temple cult and its post-exilic vocabulary. The book's structure: a devastating locust plague (chs. 1-2:11) serves as the occasion for a call to repentance (2:12-17), followed by YHWH's promise of restoration (2:18-3:21). The locust plague is both a literal agricultural disaster and the harbinger of the Day of the LORD — the pattern of divine judgment working through historical events that will culminate in the final eschatological judgment. Joel is the OT prophet most cited in the NT on the Day of Pentecost, making his prophecy of the Spirit's universal outpouring the bridge between the Old and New covenant eras.</p>"
  }
}

JOEL_CHRIST = {
  "2": {
    "32": "<p>A fulfillment: 'And it shall come to pass that everyone who calls on the name of the LORD shall be saved.' Peter (Acts 2:21) and Paul (Rom 10:13) both cite Joel 2:32 as fulfilled in the gospel proclamation: the 'name of the LORD' whose invocation brings salvation is now identified as Jesus, whom God has made both Lord and Christ (Acts 2:36). The typological identification is clear: YHWH's name in the OT = Jesus's name in the NT. This is not a revision of the OT but the NT's claim that YHWH's name and Jesus's name are the same divine identity now disclosed fully in the incarnation. The universal accessibility of salvation ('everyone who calls') removes the national and ethnic boundaries that had characterized the OT covenant community.</p>"
  }
}

# ============================
# AMOS
# ============================

AMOS_ECHO = {
  "5": {
    "18": [
      {"type": "allusion", "target": "1 Thess 5:2", "note": "Woe to you who desire the day of the LORD — Amos warns that the Day of the LORD will be darkness not light for the presumptuous; Paul says the day of the Lord comes like a thief in the night; both challenge the assumption that the Day of the LORD is automatically good news for those who consider themselves God's people"}
    ]
  },
  "9": {
    "11": [
      {"type": "fulfillment", "target": "Acts 15:16-17", "note": "I will raise up the booth of David that is fallen — James cites Amos 9:11-12 at the Jerusalem Council as the OT justification for Gentile inclusion without circumcision; the restoration of the Davidic dynasty (the fallen booth) is being fulfilled in the Messiah Jesus, and the nations seeking the LORD follows from this restoration"}
    ]
  }
}

AMOS_ORIGINAL = {
  "9": {
    "11": "<p><strong>bayom hahu aqim et sukat David hanofelet vegadarta et pirzeihen vaharisotyav aqim uvenituha keyeme olam</strong>: 'In that day I will raise up the booth of David that is fallen and repair its breaches, and raise up its ruins and rebuild it as in the days of old.' The 'fallen booth of David' is an image of the Davidic dynasty in ruins — either the northern kingdom's secession (931 BCE) or the Babylonian destruction of the Davidic throne (586 BCE). James's citation at the Jerusalem Council (Acts 15:16-17) reads the restoration as the messianic reign of Jesus: the booth is raised; now the Gentiles ('all the nations who are called by my name', v. 12 in the LXX, which differs from the MT) stream in. The LXX variant makes the Gentile-inclusion application cleaner; James uses the LXX version. This is not a mistaken quotation but a deliberate use of the LXX rendering that the Spirit has superintended to carry the intended typological meaning.</p>"
  }
}

AMOS_CONTEXT = {
  "1": {
    "1": "<p>Amos prophesied ca. 760-750 BCE in the northern kingdom under Jeroboam II, a period of remarkable prosperity and military success — and of corresponding social injustice and covenant neglect. Amos is the first of the classical writing prophets and the OT's most sustained advocate for social justice: the Day of the LORD will expose the oppression of the poor (5:11-12), the corruption of the courts (5:12), the religious hypocrisy of the sanctuaries (5:21-24: I hate, I despise your feasts ... let justice roll down like waters). His social critique is grounded in covenant theology: YHWH's covenant with Israel demands covenant justice in the community; religious observance without ethical faithfulness is an abomination.</p>"
  }
}

AMOS_CHRIST = {
  "9": {
    "11": "<p>A fulfillment: 'In that day I will raise up the booth of David that is fallen.' James's application of Amos 9:11-12 at the Jerusalem Council (Acts 15:16-17) identifies the fulfillment: the resurrection of Christ is the raising of the fallen Davidic dynasty in its ultimate form. The 'booth of David' — the Davidic covenant and its dynastic promise — lay in ruins from 586 BCE onward; no Davidic king sat on an independent throne. The risen Jesus, enthroned at the Father's right hand (Acts 2:34-36), is the restored Davidic ruler whose reign brings in the nations. The Gentile mission is therefore not a deviation from the OT prophetic program but its very fulfillment: 'the remnant of mankind and all the nations who are called by my name' (Acts 15:17, citing Amos 9:12 LXX) stream into the reestablished Davidic kingdom.</p>"
  }
}

# ============================
# OBADIAH
# ============================

OBAD_ECHO = {
  "1": {
    "4": [
      {"type": "allusion", "target": "Luke 1:52", "note": "Though you soar aloft like the eagle, though your nest is set among the stars, from there I will bring you down — YHWH's judgment of Edom's pride; Mary's Magnificat: he has brought down the mighty from their thrones; the pride-and-fall pattern of Obadiah is the structure of divine reversal that the Magnificat celebrates"}
    ],
    "15": [
      {"type": "allusion", "target": "Rev 16:19", "note": "The day of the LORD is near upon all the nations. As you have done it shall be done to you — the lex talionis principle applied to the Day of the LORD; the great city was split and the nations drank from the cup of YHWH's wrath; Obadiah's principle of nations receiving what they did to Israel reaches its ultimate form in Revelation's final judgment"}
    ]
  }
}

OBAD_ORIGINAL = {
  "1": {
    "21": "<p><strong>vealu moshim behar tziyon lishpot et har Esav vehaitah lADONAI hamelukah</strong>: 'Saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's.' Obadiah's final verse is the OT's shortest prophetic book's most expansive declaration: the kingdom belongs to YHWH. Edom (the persistent enemy of Israel, descended from Esau) will be judged; the deliverers (<em>moshim</em>, saviors/deliverers) will ascend Zion; the kingdom is YHWH's alone. The NT takes the <em>moshim</em> (saviors/deliverers) as the saints who reign with Christ (Rev 20:4-6) and the kingdom as Christ's eternal reign (Rev 11:15).</p>"
  }
}

OBAD_CONTEXT = {
  "1": {
    "1": "<p>Obadiah is the shortest book in the OT (21 verses) and is addressed entirely to Edom — the nation descended from Esau, the brother of Jacob/Israel. The oracle condemns Edom for standing aloof (v. 11) or actively participating in Jerusalem's destruction (the context is almost certainly the Babylonian destruction of 586 BCE, when Edomites reportedly aided the attackers and blocked Jewish refugees, Obad 12-14). The Edom-Israel enmity runs throughout the OT from Genesis (Esau-Jacob) through Numbers (Edom refuses passage to Moses), 1 Samuel (David's wars), and the post-exilic period. Edom becomes in the Prophets a symbol for the hostile nations in general (Isa 34; Ezek 35; Mal 1:2-5), and its final judgment is the type of all anti-God hostility that will be judged on the eschatological Day of the LORD.</p>"
  }
}

OBAD_CHRIST = {
  "1": {
    "21": "<p>A shadow: 'Saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's.' Obadiah's closing declaration — the kingdom belongs to YHWH — is the OT's most compact eschatological statement. The NT's fulfillment: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever' (Rev 11:15). The deliverers who ascend Zion are the saints who reign with Christ in the new creation (Rev 20:6: they will be priests of God and of Christ and will reign with him). Edom — the hostile brother, the nation of Esau who despised his birthright — represents all who reject the covenant birthright; their ultimate defeat is not a tribal victory for Israel but the vindication of YHWH's justice over all who oppose his reign.</p>"
  }
}

# ============================
# JONAH
# ============================

JONAH_ECHO = {
  "1": {
    "17": [
      {"type": "fulfillment", "target": "Matt 12:40", "note": "And Jonah was in the belly of the fish three days and three nights — Jesus cites this as the sign of Jonah: the Son of Man will be three days and three nights in the heart of the earth; Jonah's entombment in the fish and his emergence is the type of Jesus's death and resurrection"}
    ]
  },
  "3": {
    "5": [
      {"type": "fulfillment", "target": "Matt 12:41", "note": "The men of Nineveh repented at the preaching of Jonah, and behold something greater than Jonah is here — Jesus contrasts Nineveh's repentance at Jonah's preaching with the Jewish generation's refusal to repent at Jesus's preaching; Nineveh is a Gentile city that responded; this generation has responded to a greater preacher with less"}
    ]
  }
}

JONAH_ORIGINAL = {
  "1": {
    "17": "<p><strong>vayeman YHWH dag gadol livlo et Yonah vayehi Yonah bime'ei haddag shlosha yamim ushlosha leilot</strong>: 'And the LORD appointed a great fish to swallow up Jonah. And Jonah was in the belly of the fish three days and three nights.' The historicity of Jonah has been debated throughout church history — a man surviving inside a large sea creature is extraordinary. Jesus's citation of Jonah in Matt 12:40 takes the narrative as historical: 'just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth.' If Jonah is a parable, Jesus is drawing a parable-to-reality comparison, which is unusual. The orthodox reading: both Jonah's experience and Jesus's resurrection are historical events in which the later was the greater antitype of the earlier.</p>"
  }
}

JONAH_CONTEXT = {
  "1": {
    "1": "<p>Jonah is unique among the writing prophets: instead of a prophetic oracle, it is a narrative about a prophet. Jonah ben Amittai is mentioned in 2 Kings 14:25 as a historical figure who prophesied during the reign of Jeroboam II (ca. 793-753 BCE). The book narrates his mission to Nineveh, the capital of the Assyrian Empire — Israel's most formidable enemy. His initial flight from the mission (not from fear but, the book reveals in ch. 4, from a reluctance to see Gentile enemies repent and be spared) is the book's theological problem: the prophet opposes the very grace that characterizes YHWH. The book's final question (4:11: should I not be concerned about Nineveh?) is deliberately unanswered — forcing the reader to answer it. Jesus's use of the 'sign of Jonah' (Matt 12:39-41) makes Jonah's historical experience the type of his own death and resurrection.</p>"
  }
}

JONAH_CHRIST = {
  "1": {
    "17": "<p>A type: 'Jonah was in the belly of the fish three days and three nights.' Jesus himself identifies this as the OT's appointed sign for his resurrection: 'For just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth' (Matt 12:40). The typological elements: Jonah goes into the deep as a substitute (the sailors are saved from the storm by throwing Jonah overboard; 1:12-15) → Jonah is entombed in the fish → Jonah emerges to complete his mission to the Gentiles. The antitype: Christ goes to the cross as the world's substitute → Christ is entombed → Christ rises and commissions the mission to all Gentiles (Matt 28:19). Jonah's Gentile mission to Nineveh is the shadow; the apostolic mission to all nations is the substance.</p>"
  }
}

# ============================
# MICAH
# ============================

MICAH_ECHO = {
  "5": {
    "2": [
      {"type": "fulfillment", "target": "Matt 2:6", "note": "But you O Bethlehem Ephrathah who are too little to be among the clans of Judah from you shall come forth for me one who is to be ruler in Israel — the Magi and Herod's scribes cite Micah 5:2 as the birthplace of the Messiah; Matthew cites it as fulfilled in Jesus's birth at Bethlehem; the ruler whose origin is from of old, from ancient days, is the pre-existent Christ born in the city of David"}
    ]
  },
  "6": {
    "8": [
      {"type": "allusion", "target": "Matt 23:23", "note": "He has told you, O man, what is good; and what does the LORD require of you but to do justice and to love kindness and to walk humbly with your God — the ethical summary of Micah; Jesus's woe against the Pharisees who tithe mint but neglect the weightier matters of the law: justice and mercy and faithfulness (Matt 23:23); Micah 6:8 is Jesus's standard for what constitutes the law's weightier matters"}
    ]
  }
}

MICAH_ORIGINAL = {
  "5": {
    "2": "<p><strong>veatta Beit-Lechem Efrata tzair lihyot be'alfei Yehudah mimcha li yetze lihyot moshel beYisrael umotza'otav mikedem miyemei olam</strong>: 'But you, O Bethlehem Ephrathah, who are too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.' <em>Motza'otav mikedem miyemei olam</em> (whose coming forth is from of old, from ancient days/from ancient times/from everlasting): the preposition and nouns can point to either the antiquity of the Davidic dynasty (David's line goes back to ancient Bethlehem) or to the eternal pre-existence of the coming ruler. The NT reading (John 8:58; John 1:1) takes it in the latter, stronger sense: the one born in Bethlehem has his 'goings forth' from eternity.</p>"
  }
}

MICAH_CONTEXT = {
  "1": {
    "1": "<p>Micah prophesied ca. 735-700 BCE, contemporary with Isaiah in the southern kingdom, during the Assyrian crisis that destroyed Samaria (722 BCE) and threatened Jerusalem (701 BCE). He was a rural prophet from Moresheth-Gath (a village in the Judean foothills), which gives his oracles a social-justice perspective: he speaks for the peasant farmers whose land is being seized by the powerful (2:1-2; 3:1-3). His prophecy of Jerusalem's destruction (3:12: Zion shall be plowed as a field; Jerusalem shall become a heap of ruins) was so striking that it was cited a century later as a precedent for not killing Jeremiah when he prophesied similarly (Jer 26:18-19). Micah 6:8 is the OT's most compact ethical summary and one of the most frequently cited prophetic verses.</p>"
  }
}

MICAH_CHRIST = {
  "5": {
    "2": "<p>A direct revelation: 'But you, O Bethlehem Ephrathah, who are too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.' The theological precision of this prophecy is remarkable: (1) the specific town — Bethlehem, not Jerusalem; (2) the paradox — too small to be a clan-city, yet the birthplace of the supreme ruler; (3) the pre-existence — his 'coming forth' predates his birth in Bethlehem, reaching back to 'ancient days' (or in the stronger reading, eternity). Matthew 2:6 cites it as fulfilled with a slight adaptation that applies Micah's 'ruler' language to the one who will 'shepherd my people Israel' — combining Micah's political and pastoral imagery into the Christ who is both king and shepherd (John 10:11; Rev 7:17).</p>"
  }
}

# ============================
# NAHUM
# ============================

NAHUM_ECHO = {
  "1": {
    "15": [
      {"type": "allusion", "target": "Rom 10:15", "note": "Behold upon the mountains the feet of him who brings good news, who publishes peace — Nahum announces the fall of Nineveh as good news (the oppressor is destroyed); Isaiah 52:7 uses the same image (how beautiful upon the mountains are the feet of him who brings good news); Paul cites Isaiah in Romans 10:15 for the gospel proclamation: the good news of peace is the gospel of Christ, and the messenger's feet are the apostles'"}
    ]
  }
}

NAHUM_ORIGINAL = {
  "1": {
    "3": "<p><strong>YHWH erech apayim ugedol koach venakeh lo yenakeh YHWH besufa uvishara darko veanan afar raglav</strong>: 'The LORD is slow to anger and great in power, and the LORD will by no means clear the guilty. His way is in whirlwind and storm, and the clouds are the dust of his feet.' Nahum opens with an acrostic poem (1:2-8, partial alphabet) on the character of YHWH — combining the divine attributes of mercy and judgment that Exod 34:6-7 announced: merciful and slow to anger (Exod 34:6; Nahum 1:3a) but will not leave the guilty unpunished (Exod 34:7b; Nahum 1:3a). Jonah announced repentance and YHWH relented; Nahum announces the final judgment because Nineveh did not permanently repent. The same divine character — patient mercy but ultimate justice — is the framework for the NT: God overlooked past sins (Acts 17:30; Rom 3:25) but now commands repentance in light of the coming judgment.</p>"
  }
}

NAHUM_CONTEXT = {
  "1": {
    "1": "<p>Nahum prophesied ca. 663-612 BCE — after the fall of Thebes (663 BCE, mentioned in 3:8) and before the fall of Nineveh (612 BCE, which Nahum predicts). He is the companion prophecy to Jonah: Jonah brought Nineveh to repentance (ca. 760 BCE) and YHWH relented; Nahum announces that Nineveh's subsequent return to violence and oppression means its final destruction is now inevitable. The contrast is instructive: divine patience has a limit; the same attributes of mercy and justice that led YHWH to spare Nineveh in Jonah's day lead him to destroy it in Nahum's day. Nineveh was destroyed in 612 BCE by a coalition of Babylonians and Medes, exactly as Nahum predicted.</p>"
  }
}

NAHUM_CHRIST = {
  "1": {
    "7": "<p>A revelation of God: 'The LORD is good, a stronghold in the day of trouble; he knows those who take refuge in him.' Set in the context of Nineveh's coming destruction, this verse identifies the flip-side of divine wrath: the same YHWH who destroys his enemies is the stronghold for those who trust him. The NT's form of this double-truth: 'It is a fearful thing to fall into the hands of the living God' (Heb 10:31) for those who reject Christ; but 'There is therefore now no condemnation for those who are in Christ Jesus' (Rom 8:1) for those who are in him. The refuge (<em>maoz</em>, stronghold/fortress) that Nahum declares is the God who is also Christ: 'the name of the LORD is a strong tower; the righteous man runs into it and is safe' (Prov 18:10).</p>"
  }
}

# ============================
# HABAKKUK
# ============================

HAB_ECHO = {
  "2": {
    "4": [
      {"type": "fulfillment", "target": "Rom 1:17", "note": "The righteous shall live by his faith — Paul quotes Hab 2:4 in Romans 1:17, Galatians 3:11, and Hebrews 10:38 as the OT summary of justification by faith: the just/righteous person lives by faithfulness/faith; Paul applies it to the righteousness of God revealed in the gospel"},
      {"type": "fulfillment", "target": "Gal 3:11", "note": "It is evident that no one is justified before God by the law, for the righteous shall live by faith — Paul cites Hab 2:4 as proof that the OT already knew that justification was by faith, not law-keeping; the law (Lev 18:5: he who does them shall live by them) and the prophet (Hab 2:4: the righteous shall live by faith) are placed in contrast"}
    ]
  }
}

HAB_ORIGINAL = {
  "2": {
    "4": "<p><strong>hineh afela lo yoshra nafsho bo vetzaddik beemunato yichyeh</strong>: 'Behold, his soul is puffed up; it is not upright within him, but the righteous shall live by his faith [or faithfulness, <em>emunah</em>].' This verse is the most quoted OT text in the NT letters. The Hebrew <em>emunah</em> covers a semantic range from 'faithfulness' (reliability, steadfastness) to 'faith' (trust, belief). Paul's use in Romans and Galatians emphasizes the trust/belief aspect; the Habakkuk context emphasizes endurance and faithfulness during the Babylonian crisis. Both senses are present: the righteous person is characterized by trust in YHWH's promise that sustains them through the crisis (both the original Babylonian threat and the ongoing existential challenge of life under divine wrath deferred). The Reformers' rediscovery of this verse (Luther: the just shall live by faith, not by works of the law) was the theological engine of the Protestant Reformation.</p>"
  }
}

HAB_CONTEXT = {
  "1": {
    "1": "<p>Habakkuk's dialogue with YHWH (ca. 605-598 BCE) is the OT's most direct expression of prophetic complaint about divine justice: Why do you tolerate wrong? (1:3); Why are you silent while the wicked swallow up the more righteous? (1:13). YHWH's answer — he is raising up the Babylonians as the instrument of judgment — only deepens the question: how can a holy God use a more wicked nation to judge a less wicked one? The book's resolution is the three-chapter arc of complaint → divine response → prophetic praise (ch. 3): the righteous will live by faith in YHWH's promises even when the present situation appears to contradict those promises. The book models the theodicy of faith: not a logical resolution of the problem of evil, but a trust in the character of YHWH that sustains through crisis.</p>"
  }
}

HAB_CHRIST = {
  "2": {
    "4": "<p>A direct revelation: 'The righteous shall live by his faithfulness/faith.' This verse, quoted three times in the NT, is the OT's most concentrated statement of the principle of justification by faith. Paul reads it as the OT's own principle against works-righteousness: 'it is evident that no one is justified before God by the law, for the righteous shall live by faith' (Gal 3:11). The christological dimension: the 'righteous one' who lives by faith in its ultimate form is Jesus himself, who trusted the Father through the cross and was vindicated in the resurrection (Heb 10:38-39 applies the verse to perseverance under persecution, contextualizing it with the author's own reflection on Christ's faithfulness). The Reformation's recovery of this verse as the summary of the gospel ('the just shall live by faith') was the recovery of the Christological center of the OT's own prophetic witness.</p>"
  }
}

# ============================
# ZEPHANIAH
# ============================

ZEPH_ECHO = {
  "3": {
    "14": [
      {"type": "allusion", "target": "Luke 1:28", "note": "Sing aloud O daughter of Zion; shout O Israel! Rejoice and exult with all your heart O daughter of Jerusalem — the call to rejoice because YHWH is among you (3:17); the angel's greeting to Mary (Rejoice, highly favored one, the Lord is with you) echoes the Zephaniah joy-announcement: the presence of YHWH is the reason for rejoicing, and in the incarnation, YHWH is present in the most intimate way imaginable"},
      {"type": "allusion", "target": "John 1:14", "note": "The LORD your God is in your midst — Zeph 3:17 (the LORD is in your midst) is the OT's joyful proclamation of divine presence; John 1:14 (the Word became flesh and dwelt in our midst) is the ultimate fulfillment: YHWH's presence in the tabernacle-tent and in the midst of his people now means the incarnate Son tabernacling among humanity"}
    ]
  }
}

ZEPH_ORIGINAL = {
  "3": {
    "17": "<p><strong>YHWH eloheicha bekirbecha gibbor yoshi'a yasis alayich besimcha yacharish be'ahavato yagel alayich berinah</strong>: 'The LORD your God is in your midst, a mighty one who will save; he will rejoice over you with gladness; he will quiet you by his love; he will exult over you with loud singing.' This verse is the OT's most intimate statement of divine delight in his people: YHWH not merely tolerating but actively rejoicing over Israel, singing over her. The father-over-child image (quieting, singing) is the most tender description of YHWH's covenant love. The NT fulfillment: 'The Father himself loves you' (John 16:27); 'God is love' (1 John 4:8); 'rejoice in the Lord always' (Phil 4:4) — the joy is mutual, as Zephaniah's vision shows: YHWH singing over his people is the grounding for the people's own joy.</p>"
  }
}

ZEPH_CONTEXT = {
  "1": {
    "1": "<p>Zephaniah prophesied ca. 640-609 BCE during the reign of Josiah (640-609 BCE), before or during Josiah's reform (621 BCE). He was a member of the royal family (his genealogy goes back four generations to Hezekiah, 1:1) — one of the few prophets with clear royal connections. His primary theme is the Day of the LORD (using the phrase more than any other prophet): a comprehensive divine judgment on Judah (ch. 1), the nations (2), and Jerusalem (3:1-8), followed by the promise of a purified remnant and YHWH's presence among them (3:9-20). Zephaniah 3:14-20's closing vision of joy and restoration is one of the OT's most beautiful eschatological passages and the probable background for the angel's greeting to Mary at the Annunciation.</p>"
  }
}

ZEPH_CHRIST = {
  "3": {
    "14": "<p>A fulfillment: 'Sing aloud, O daughter of Zion; shout, O Israel! Rejoice and exult with all your heart, O daughter of Jerusalem! The LORD has taken away the judgments against you ... The King of Israel, the LORD, is in your midst; you shall never again fear evil.' This call to rejoice because YHWH is in the midst of his people reaches its fulfillment in the incarnation. Luke's Annunciation (1:28-33) and the angels' song at the Nativity (2:10-14: I bring you good news of great joy) are the NT's recasting of Zephaniah's joy-cry: rejoice, for the Lord is with you. The movement from Zephaniah to Luke is the movement from prophetic announcement to historical fulfillment: the divine King who was to come 'in your midst' comes as the infant in Bethlehem, and then the risen Lord who sends the Spirit so that YHWH is 'in the midst' of the church (Matt 18:20; John 14:23).</p>"
  }
}

# ============================
# HAGGAI
# ============================

HAG_ECHO = {
  "2": {
    "6": [
      {"type": "fulfillment", "target": "Heb 12:26-27", "note": "Yet once more, in a little while, I will shake the heavens and the earth and the sea and the dry land — Hebrews cites Haggai 2:6 as pointing to the definitive eschatological shaking: the removal of created things that are shakeable, so that only the unshakeable kingdom remains; the new creation will be established through a shaking that removes the old"}
    ],
    "9": [
      {"type": "allusion", "target": "John 2:21", "note": "The latter glory of this house shall be greater than the former — Haggai promises that the second temple will surpass Solomon's in glory; this is fulfilled not in the physical Herodian temple but in Jesus entering the temple (John 2:19-21: destroy this temple, and in three days I will raise it up; the temple was his body); the presence of Christ in the second temple makes its latter glory exceed its former"}
    ]
  }
}

HAG_ORIGINAL = {
  "2": {
    "9": "<p><strong>gadol yihyeh kevod habayit haze ha-acharon min harishon amar YHWH tzvaot uvamaqom haze etten shalom neum YHWH tzvaot</strong>: 'The latter glory of this house shall be greater than the former, says the LORD of hosts. And in this place I will give peace, declares the LORD of hosts.' Haggai's promise was puzzling to the post-exilic community: the second temple was visibly inferior to Solomon's (Ezra 3:12: the elders who had seen the first temple wept when the second was founded). The fulfillment required an unexpected reading: the greater glory came not through architectural improvement (Herod's renovation made it physically grander) but through the presence of the messianic King who entered it (Matt 21:12-17; John 2:13-22). Jesus is the glory that made the second temple greater — the Shekinah presence in person, which the first temple never contained.</p>"
  }
}

HAG_CONTEXT = {
  "1": {
    "1": "<p>Haggai prophesied in 520 BCE, the second year of Darius I of Persia — 16 years after the first returnees arrived in Jerusalem. The temple reconstruction had stalled: the returning exiles had built their own houses while the temple remained unfinished (1:4). Haggai's four oracles (1:1-11; 2:1-9; 2:10-19; 2:20-23) call the community to prioritize the temple and promise divine blessing as a result. His contemporary was Zechariah, whose visions (chs. 1-8) addressed the same restoration community. Together they provide the theological framework for the post-exilic community's task: rebuilding the worship center through which YHWH's presence among his people would be maintained until the coming of the one greater than the temple.</p>"
  }
}

HAG_CHRIST = {
  "1": {
    "1": "<p>A theme: the prophetic word arrives in a precise historical moment — 'the second year of King Darius, the first day of the sixth month.' The NT's pattern of incarnational timing ('when the fullness of time had come, God sent forth his Son,' Gal 4:4) repeats Haggai's structure: YHWH speaks at the appointed moment in redemptive history, not before and not after. The post-exilic prophets Haggai and Zechariah operate in the period that the NT writers understand as the final chapter before the Messiah — the rebuilt temple being the house where the Lord would suddenly come (Mal 3:1).</p>",
    "2": "<p>A shadow: 'These people are saying, The time has not yet come to rebuild the LORD's house.' The deferred building is the spiritual failure Haggai diagnoses: prioritizing personal comfort over YHWH's house. The NT parallel is the parable of the excused guests (Luke 14:18-20) where each makes the same deferral — the messianic banquet is ready but the invited decline to come. The post-exilic 'time has not come' for the temple becomes the NT generation's 'we have no leisure' for the kingdom. Christ's coming does not wait for the moment when all competing priorities are resolved; he comes to the unready.</p>",
    "3": "<p>A theme: the word of the LORD comes again through the prophet — divine persistence in addressing deferred obedience. The repetition of the messenger formula ('the word of the LORD came through the prophet Haggai') seven times in the book models the NT's pattern of the Spirit's repeated prompting before judgment or fulfillment arrives. Christ is the final and complete Word that comes to his own house (John 1:11), replacing repeated prophetic messengers with the Son himself (Heb 1:1-2: 'in these last days he has spoken to us by his Son').</p>",
    "4": "<p>A shadow: 'Is this really the time for you to be living in your paneled houses while this house lies in ruins?' The contrast between personal prosperity and the desolate worship-center is the book's central accusation. In the NT, Jesus's cleansing of the temple (Matt 21:12-13; John 2:13-17) enacts exactly Haggai's concern: the house of YHWH has been turned from its purpose. John records Jesus's declaration that the temple is his Father's house (John 2:16) — echoing Haggai's priority that the house of YHWH must be built and maintained above personal interest.</p>",
    "5": "<p>A theme: 'Think carefully about the path you are on' (<em>simu levavkhem al darcheikhem</em>) — the reflexive examination that the covenant calls its people to practice. The NT uses the same diagnostic structure: Paul's examination-before-communion call (1 Cor 11:28: 'Let a person examine himself'), the letters to the seven churches (Rev 2-3: 'I know your works'), and Jesus's Sermon on the Mount (Matt 5:21-48: 'you have heard... but I say') all deploy the same principle: the covenant person must account for the gap between their way and the covenant standard.</p>",
    "6": "<p>A shadow: 'You have planted much but harvested little... you earn wages, but put them into a bag with holes.' The agricultural curse-structure (Deut 28:38-44: 'you will plant but not harvest') has taken hold; the covenant's warning against misplaced priorities is bearing fruit in economic futility. Christ addresses the same dynamic in the Sermon on the Mount: 'do not lay up treasures on earth... where thieves break in and steal' (Matt 6:19-21). The covenant-curse of futile labor is reversed in Christ's promise of the kingdom that moth and rust cannot corrupt — the truly abundant life that Haggai's deprived community anticipates.</p>",
    "7": "<p>A theme: the repeated call to 'think carefully about the path you are on' frames the diagnosis as the necessary prerequisite for the solution (v8). The doubled call to self-examination (vv5 and 7 are identical) reflects the Hebrew rhetorical pattern of double-invitation to underscore urgency. In the NT, repentance similarly precedes restoration: John the Baptist's 'Repent, for the kingdom of heaven is at hand' (Matt 3:2) functions as Haggai's summons — clear diagnosis of misdirection before the announcement of what YHWH will now do.</p>",
    "8": "<p>A type: 'Go up to the mountains, bring down wood, and build the house — so that I may take pleasure in it and be glorified.' The temple-building commission is the covenantal task of the post-exilic community. In the NT, the commission shifts from stone to living stones: 'you yourselves like living stones are being built up as a spiritual house' (1 Pet 2:5). Paul describes the church as 'God's building' where each person builds with gold, silver, or wood (1 Cor 3:9-15). The divine 'I will take pleasure in it' finds its ultimate fulfillment in the church as the dwelling of the Spirit (Eph 2:21-22).</p>",
    "9": "<p>A shadow: 'You expected much, but it came to little. And what you brought home, I blew away.' The divine withholding of increase is the covenant curse actively at work. In the NT, Jesus applies the same structure in the parable of the talents (Matt 25:29: 'to everyone who has, more will be given; from the one who has not, even what he has will be taken away') and in the vine teaching (John 15:2: 'every branch in me that does not bear fruit he takes away'). The blow-away of what should have accumulated is the active sign that covenant priorities have been inverted.</p>",
    "10": "<p>A shadow: 'On your account, the sky has withheld its dew and the earth has withheld its produce.' The covenant-curse structure (Deut 28:23-24: 'the heavens over you shall be bronze, and the earth under you shall be iron') is in operation. The NT reversal: Paul promises that 'my God will supply every need of yours according to his riches in glory in Christ Jesus' (Phil 4:19) — the supply comes through covenant faithfulness to the new temple-community; the withholding and the providing are both covenant instruments pointing toward Christ's mediation of all blessing.</p>",
    "11": "<p>A shadow: the comprehensive drought decree — grain, wine, oil, ground, people, livestock, all labor. The Deuteronomic curse-list (Deut 28:18, 23-24, 38-44) is activated in its fullness. The NT application: when the community's priorities are wrong, the blessing withheld is not merely material but spiritual. Jesus warns that hearing without doing produces the house built on sand (Matt 7:26-27) — the drought that comes is the coming judgment that exposes what was never truly built. But in Christ, the curse of Deut 28 is fully absorbed (Gal 3:13: 'Christ redeemed us from the curse of the law by becoming a curse for us').</p>",
    "12": "<p>A theme: Zerubbabel, Joshua, and the remnant obeyed the voice of the LORD — the covenant response of faithful obedience. The remnant-community that returns and obeys is the OT's type of the NT church: a small, apparently defeated community faithful to the covenant while the majority cultures pursue their own interests. Zerubbabel (civil leader, Davidic lineage) and Joshua (priestly leader) together model the kingly-priestly duality that Zechariah 4 and 6 develop as the 'two anointed ones' — both pointing toward Christ who holds both offices as the one great King-Priest (Heb 7:1-28; Rev 1:6).</p>",
    "13": "<p>A revelation of God: 'I am with you,' declares the LORD. The <em>Immanuel</em> promise — God's personal presence with his people — is the spine of the entire OT covenant and the explicit name of Jesus (Matt 1:23: 'Behold, the virgin shall conceive and bear a son, and they shall call his name Immanuel, which means God with us'). Haggai's two-word divine reassurance ('I am with you') is the covenant foundation; the incarnation is its irreversible, embodied fulfillment. The NT's 'I am with you always, to the end of the age' (Matt 28:20) closes the frame that Haggai's oracle opens.</p>",
    "14": "<p>A type: 'The LORD stirred up the spirit of Zerubbabel... the spirit of Joshua... and the spirit of all the remnant of the people.' The divine stirring of the human spirit for a sacred construction project echoes the Spirit's preparation of craftsmen for the tabernacle (Exod 36:2-3: 'every man whose heart stirred him up') and anticipates the Spirit's empowerment of the NT community for the living-temple building project (Acts 2:4; Eph 3:16-17). Christ is the one in whom 'the whole fullness of deity dwells bodily' (Col 2:9) — not a stirred-up spirit for temporary work but the permanent embodiment of YHWH's presence.</p>",
    "15": "<p>A theme: the date formula ('the twenty-fourth day of the sixth month, the second year of Darius') anchors the work of God in historical specificity. The NT's greatest events similarly carry specific dates and names: Pontius Pilate, Tiberius Caesar, 'the fifteenth year of the reign of Tiberius' for John the Baptist's commissioning (Luke 3:1-2). The particularity of redemption-in-history is fundamental to biblical theology: salvation is not a timeless myth but a dated act in a named world — culminating in 'crucified under Pontius Pilate' in the Apostles' Creed.</p>"
  },
  "2": {
    "1": "<p>A theme: a new divine word arrives on the twenty-first day of the seventh month — the final day of the Feast of Tabernacles (Sukkot; Lev 23:34-36). This liturgical timing is theologically loaded: Tabernacles celebrated Israel's wilderness dwelling in tents and the harvest ingathering; it was also the feast most associated with eschatological hopes (Zech 14:16-19: all nations will celebrate Tabernacles in the messianic age). John 7:37-38 records Jesus's great cry on 'the last day of the feast' (Tabernacles): 'If anyone thirsts, let him come to me and drink' — the eschatological fulfillment of what Haggai announces on this same feast day.</p>",
    "2": "<p>A type: Zerubbabel (governor, Davidic heir) and Joshua (high priest) together receive the divine address — the civil-priestly dual leadership of the restoration community. Zechariah 6:13 will explicitly predict a figure who 'will be a priest on his throne' — a single person combining both offices. This is fulfilled in Christ: Heb 7:1-3 establishes Christ as the Melchizedek-order priest-king; Rev 1:6 describes him making his people 'a kingdom and priests.' The Zerubbabel-Joshua partnership is the type whose antitype is one person who holds both crowns permanently.</p>",
    "3": "<p>A shadow: 'Who is left among you who saw this house in its former splendor? How does it appear to you now? Does it not seem like nothing to you?' The diminished second temple is the occasion for the promise of greater glory to come. In the NT, Jesus's disciples admire the Herodian temple stones (Mark 13:1) — the beauty of the second temple, enhanced by Herod — and Jesus predicts its destruction (Mark 13:2). The glory of the second temple, for all its enhancement, was still less than the first in the eyes of those who remembered; but Christ in the temple surpasses both (Mal 3:1).</p>",
    "4": "<p>A revelation of God: 'Be strong, Zerubbabel... be strong, Joshua... be strong, all you people of the land — and work! For I am with you, declares the LORD of Hosts.' The tripled 'be strong' (<em>chazaq chazaq</em>) formula echoes the commissioning of Joshua at the Jordan (Josh 1:6-9: 'be strong and courageous') and anticipates Paul's final exhortation: 'be strong in the Lord and in the strength of his might' (Eph 6:10). The divine presence as the ground of human strength — 'I am with you' — is the pattern Christ fulfills in promising the Spirit as the permanent paraclete (John 14:16-17).</p>",
    "5": "<p>A revelation of God: 'My Spirit remains in your midst; do not be afraid.' The divine Spirit's presence is the continuity between the wilderness covenant ('I made with you when you came out of Egypt') and the post-exilic restoration. The NT's Pentecost is the ultimate fulfillment: the Spirit who was 'in your midst' (external, dwelling among the community) becomes 'in you' (internal, indwelling each believer; John 14:17: 'he dwells with you and will be in you'). The incremental intensification — Spirit among them → Spirit within them → Christ in you the hope of glory (Col 1:27) — is the arc of redemptive history.</p>",
    "6": "<p>A shadow/allusion: 'Once more, in just a little while, I will shake the heavens, the earth, the sea, and the dry land.' The eschatological cosmic shaking that destabilizes every structure except the unshakeable kingdom. Heb 12:26-28 cites this verse as pointing to the definitive eschatological shaking at Christ's final return: 'Yet once more indicates the removal of things that are shaken... so that what cannot be shaken may remain.' The 'once more' is the hinge: after Christ's first coming has already shaken the existing order (Matt 27:51: the earth shook at the crucifixion), the final shaking will remove everything provisional. What remains is the kingdom that cannot be shaken.</p>",
    "7": "<p>A type: 'And I will shake all nations, so that the treasures of all nations shall come in, and I will fill this house with glory, says the LORD of Hosts.' The 'treasures/desired things' (<em>chemdah</em>) of the nations streaming to YHWH's house has been read messianically by the Vulgate ('the Desired of all nations will come'). The pattern is clear regardless: the nations streaming to YHWH's dwelling is the eschatological gathering of all peoples. The Magi (Gentile wise men) bringing treasure to the Christ-child (Matt 2:11) is the first fulfillment; the nations bringing their glory into the new Jerusalem (Rev 21:24-26) is the final one. The house is filled with glory because the incarnate Son is in it.</p>",
    "8": "<p>A revelation of God: 'The silver is mine and the gold is mine, declares the LORD of Hosts.' The divine ownership of all wealth is the foundation for the confidence that the temple will be filled with glory despite the community's poverty. In the NT, Paul grounds the collection for Jerusalem's poor in the same principle: 'you will be enriched in every way... for God is able to make all grace abound to you' (2 Cor 9:8-11). All resources ultimately belong to YHWH; the post-exilic community's poverty is not an obstacle to the divine building project. Christ 'though he was rich, yet for your sake he became poor, so that you by his poverty might become rich' (2 Cor 8:9).</p>",
    "9": "<p>A direct revelation: 'The future splendor of this house will surpass its former glory, says the LORD of Hosts. And in this place I will give peace.' This is one of the OT's most precise messianic predictions: the second temple's latter glory will exceed Solomon's, and <em>shalom</em> will be given in this place. The fulfillment: Jesus enters the second temple (Mal 3:1: 'the Lord whom you seek will suddenly come to his temple'), and the presence of the incarnate Son in the second temple is the greater glory. 'He himself is our peace' (Eph 2:14). The physical temple was still standing when the Prince of Peace walked its courts, making v9's promise literally true.</p>",
    "10": "<p>A theme: a second divine oracle arrives on the twenty-fourth day of the ninth month — two months after the foundation was laid (v18). The doubling of the date formula emphasizes that YHWH is tracking the community's progress with precision. The NT parallel: Christ's 'I am with you always, to the end of the age' (Matt 28:20) encompasses all the dated moments of the church's obedience — no step of faithful work is unobserved by the one who came to his temple and now inhabits his people as his living temple.</p>",
    "11": "<p>A shadow: 'Ask the priests for a ruling on the law' — the priestly teaching role (<em>horah</em>) is the official interpretive authority in the Mosaic system. The priests' answer in v12 reveals their understanding of holiness's non-transferability. Christ is the one in whom the Torah's teaching office is fulfilled (Matt 5:17-18: 'I have not come to abolish the Law or the Prophets but to fulfill them') and who becomes the final Teacher whose interpretation is authoritative in the new covenant era (John 14:26).</p>",
    "12": "<p>A shadow: the holiness-ruling on holy meat — sanctification does not transmit through indirect contact (the garment touching the food does not sanctify the food). The priests correctly identify that holiness does not work by proximity-contamination. In the NT, this principle is superseded: the Spirit who indwells the believer sanctifies from within, not merely by external contact. The question of what makes holy and what defiles is addressed by Jesus in Mark 7:14-23 ('nothing outside a person can defile him; things that come out of a person are what defile') — the new covenant internalizes holiness through the Spirit rather than through external contact-rules.</p>",
    "13": "<p>A shadow: defilement by contact with a corpse (<em>tum'at met</em>) does transmit — the priestly rule is the inverse of v12. Corpse-uncleanness was the strongest form of ritual impurity (Num 19). The NT development: Christ touches lepers (Matt 8:3) and dead bodies (Luke 7:14-15; Mark 5:41) without becoming defiled — instead, his touch transmits life and cleanness in the reverse direction. The one who is Life itself (John 14:6) cannot be contaminated by death; death is contaminated by his presence and undone. The holiness-question of Haggai is resolved by the greater purity of the incarnate Son.</p>",
    "14": "<p>A shadow: 'That is exactly how it is with this people and this nation before me... and with every work of their hands; and what they offer there is defiled.' The principle from vv12-13 is applied to the restored community: defilement extends from person to work to offering. Their uncleanness has infected everything they do. The NT equivalent: 'to the defiled and unbelieving, nothing is pure; both their minds and their consciences are defiled' (Titus 1:15). The solution is not ritual purity but new creation in Christ: 'if anyone is in Christ, he is a new creation' (2 Cor 5:17) — the source of defilement is removed, not merely managed.</p>",
    "15": "<p>A theme: 'Now consider carefully from this day forward. Before one stone was set upon another in the LORD's temple...' — the covenant turning point. The phrase 'from this day' (<em>min-ha-yom hazzeh</em>) marks the eschatological boundary between the former state and the new condition. The NT's great 'from this day forward' is the cross and resurrection: 'the old has passed away; behold, the new has come' (2 Cor 5:17). The laying of the temple's foundation is the OT's hinge-point analogous to the cross; after it, the conditions of blessing change.</p>",
    "16": "<p>A shadow: 'When someone came to a grain pile expecting twenty measures, there were only ten' — the systematic underperformance of the covenant-curse economy. The gap between expectation and reality is the covenant's diagnostic of misplaced priority. Jesus addresses the same gap in the parable of the prodigal son (Luke 15:14-17): the covenant-breaking son finds that 'he began to be in need... no one gave him anything.' The return to the father is the return to the source of all fruitfulness — what the returning exiles' temple-prioritization was meant to model.</p>",
    "17": "<p>A shadow: 'I struck you with blight, mildew, and hail — yet you did not return to me.' The withholding of harvest despite the covenant-curse prompts was designed to drive the community back to YHWH; it failed to produce repentance. The same pattern in the NT: the seals and trumpets of Revelation (8:7-11; 9:20-21) produce covenant-curse conditions specifically to drive the nations to repentance — and the same failure is recorded: 'they did not repent... they did not repent.' The purpose of covenant-curse is repentance and return; Christ's cross is the ultimate covenant-curse (Gal 3:13) that finally does produce the return it was designed to achieve.</p>",
    "18": "<p>A theme: 'Consider carefully from this day on — the twenty-fourth day of the ninth month — from the day the LORD's temple foundation was laid.' The foundation-day is the new beginning. Paul calls Christ 'the foundation' that has been laid (1 Cor 3:11: 'For no one can lay a foundation other than that which is laid, which is Jesus Christ'). The dating of new possibilities from the temple's foundation is the OT type of the new creation possibilities that open from the cross — Christ laid as the cornerstone (Matt 21:42; 1 Pet 2:6-7; Eph 2:20) that determines the character of everything built upon it.</p>",
    "19": "<p>A revelation of God: 'Is the seed still in the granary? The vine, the fig tree, the pomegranate, and the olive tree have not yet produced. But from this day on I will bless you.' The divine 'from this day' reversal initiates a new era of blessing from the moment of covenant re-prioritization. The NT's form: 'Blessed be the God and Father of our Lord Jesus Christ, who has blessed us in Christ with every spiritual blessing in the heavenly places' (Eph 1:3) — the blessing comes not from a future moment but from the one who has already come. Haggai's agricultural 'I will bless you' is the OT type of the comprehensive, already-accomplished blessing in Christ.</p>",
    "20": "<p>A theme: a second oracle comes on the same day — divine words multiply at the turning point of covenant history. The doubled oracle on the twenty-fourth day (the same day as vv15-19) models the surplus of divine speech at the hinge-moments of redemption. In the NT, the prologue of Hebrews captures the same intensification: 'Long ago, at many times and in many ways, God spoke to our fathers by the prophets, but in these last days he has spoken to us by his Son' (Heb 1:1-2). The multiplication of prophetic words at Haggai's level is overwhelmed by the single, final, fully adequate Word made flesh.</p>",
    "21": "<p>A shadow: 'I am about to shake the heavens and the earth' — the eschatological shaking of vv6-7 is now focused specifically on the political order: 'I will overturn royal thrones' (v22). The divine shaking that destabilizes empires is the OT's persistent witness that no political order is the final one. Christ's birth destabilized Herod's throne (Matt 2:3: 'Herod the king was troubled'); his resurrection declared that the kingdoms of the world have become the kingdom of our Lord (Rev 11:15); his return will finally shake everything that can be shaken.</p>",
    "22": "<p>A shadow: 'I will overturn royal thrones and shatter the power of the kingdoms of the nations. I will overturn chariots and their riders; horses and their riders will fall, each by the sword of his brother.' The overthrow of military-political empire by internecine conflict is the covenant-curse pattern for pagan powers. The NT application: the empires that opposed Christ's people fell by their own internal conflicts (Rome's civil wars; Babylon's fall to Persia). The final overthrow is the defeat of the beast at the parousia (Rev 19:11-21: 'the rest were slain by the sword that came from the mouth of him who was sitting on the horse'). The pattern Haggai announces is fulfilled climactically at Christ's return.</p>",
    "23": "<p>A direct revelation: 'On that day, declares the LORD of Hosts, I will take you, Zerubbabel my servant son of Shealtiel, and make you like a signet ring, for I have chosen you.' The signet ring (<em>chotem</em>) reversal is the book's climactic Christological verse. Jer 22:24 had pronounced Jeconiah (Coniah, Zerubbabel's grandfather in the Davidic line) cursed: 'as I live, declares the LORD, even if Coniah were the signet ring on my right hand, I would tear you off.' Zerubbabel's restoration as YHWH's signet ring reverses the Jeconiah curse — the Davidic dynasty is rehabilitated, the seal of kingship restored. Matthew's genealogy (Matt 1:12-16) runs through Zerubbabel to Jesus: the signet ring returned to the line reaches its ultimate form in the one who is 'the Son of David, the Son of Abraham' (Matt 1:1) and who bears the divine seal permanently (John 6:27: 'on him God the Father has set his seal').</p>"
  }
}

# ============================
# ZECHARIAH
# ============================

ZECH_ECHO = {
  "9": {
    "9": [
      {"type": "fulfillment", "target": "Matt 21:5", "note": "Rejoice greatly O daughter of Zion! Shout O daughter of Jerusalem! Behold your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey on a colt the foal of a donkey — Matthew and John both cite Zechariah 9:9 as fulfilled in the triumphal entry; the King of peace entering on a donkey (not a war horse) is the messianic sign"}
    ]
  },
  "11": {
    "12": [
      {"type": "fulfillment", "target": "Matt 26:15", "note": "And they weighed out as my wages thirty pieces of silver — the shepherd's wages in Zechariah 11:12 are applied to Judas's price for betraying Jesus; Matthew explicitly cites this as fulfillment (using Jeremiah's name by prophetic attribution of the scripture) in Matt 27:9-10"}
    ]
  },
  "12": {
    "10": [
      {"type": "fulfillment", "target": "John 19:37", "note": "They shall look on me whom they have pierced — Zechariah's oracle about the pierced one whom Jerusalem will mourn; John cites it at the crucifixion (they will look on the one they have pierced, John 19:37); Revelation applies it to the parousia (Rev 1:7: every eye will see him, even those who pierced him)"}
    ]
  },
  "13": {
    "7": [
      {"type": "fulfillment", "target": "Matt 26:31", "note": "Strike the shepherd, and the sheep will be scattered — Jesus quotes Zechariah 13:7 in Gethsemane as what will be fulfilled when he is arrested: strike the shepherd and the sheep of the flock will be scattered; the disciples' abandonment is the fulfillment of the Zechariah oracle about the smitten shepherd"}
    ]
  }
}

ZECH_ORIGINAL = {
  "12": {
    "10": "<p><strong>veshafachti al beit David veal yoshev Yerushalayim ruach chen vetachanunin vehibitu elai et asher daqaru vesafdu alav kemisped al hayachid vehamer alav kemispod al habechor</strong>: 'And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy, so that, when they look on me, on him whom they have pierced, they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.' The grammatical anomaly is striking: 'they shall look on me [YHWH speaking] whom they have pierced' — the divine speaker identifies himself as the one pierced. The transition from 'me' to 'him' within the verse is unexplained in the OT but is resolved in the NT: YHWH and the one who was pierced are identified — the one pierced at the crucifixion is YHWH in the person of the Son.</p>"
  }
}

ZECH_CONTEXT = {
  "1": {
    "1": "<p>Zechariah prophesied ca. 520-518 BCE (chs. 1-8, with the dated oracles) and possibly into the 5th or 4th century BCE (chs. 9-14, the 'Second Zechariah', are undated and stylistically different — many scholars treat them as later additions). His eight night visions (chs. 1-6) address the post-exilic restoration community with complex symbolic imagery; his oracle-collections (chs. 7-8, 9-11, 12-14) look further into the eschatological future. Zechariah is the most extensively quoted OT book in the Gospel passion narratives — his oracles about the triumphal entry (9:9), the thirty pieces of silver (11:12-13), the smitten shepherd (13:7), the pierced one (12:10), and the cosmic mourning (12:10-14) all find explicit NT citations in the passion story. The passion narrative is Zechariah 9-14 in fulfillment.</p>"
  }
}

ZECH_CHRIST = {
  "9": {
    "9": "<p>A direct revelation: 'Rejoice greatly, O daughter of Zion! Shout aloud, O daughter of Jerusalem! Behold, your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey, on a colt, the foal of a donkey.' The triumphal entry is one of the most deliberately staged Christological events in the Gospels: Jesus specifically arranges for the donkey (Luke 19:30-34), enters Jerusalem in a way that fulfills Zechariah's vision exactly, and Matthew and John both cite the fulfillment (Matt 21:5; John 12:15). The theological content of the sign: a king on a war horse signals military conquest; a king on a donkey signals peace and humility. The Messiah comes not to destroy enemies with military power but to bring salvation through the humble, peaceable means of his own sacrifice. The crowds' hosannas (Ps 118:26, 'Blessed is he who comes in the name of the LORD') are their recognition of the sign, even if they misread its implications.</p>"
  },
  "12": {
    "10": "<p>A direct revelation: 'They shall look on me, on him whom they have pierced, and they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.' The shift from 'me' (YHWH speaking) to 'him' (the one pierced) within the verse is the OT's most striking grammatical prolepsis of the incarnation: the one pierced is YHWH, yet YHWH speaks of him in the third person. John cites it at the crucifixion (19:37: these things took place that the Scripture might be fulfilled: they will look on him whom they have pierced), and Revelation applies it to the parousia (1:7: every eye will see him, even those who pierced him, and all tribes of the earth will wail on account of him). The mourning is both repentance (Acts 2:37: they were cut to the heart and said, Brothers, what shall we do?) and eschatological recognition (Rev 1:7: all tribes will wail).</p>"
  }
}

# ============================
# MALACHI
# ============================

MAL_ECHO = {
  "3": {
    "1": [
      {"type": "fulfillment", "target": "Matt 11:10", "note": "Behold I send my messenger and he will prepare the way before me — the messenger of the covenant is announced; Jesus quotes Malachi 3:1 (in combination with Exod 23:20) as fulfilled in John the Baptist: this is the one about whom it is written, Behold I send my messenger before your face who will prepare your way before you"},
      {"type": "fulfillment", "target": "Mark 1:2", "note": "Behold I send my messenger before your face — Mark opens his Gospel by combining Malachi 3:1 and Isaiah 40:3 as fulfilled in John the Baptist's ministry in the wilderness"}
    ]
  },
  "4": {
    "5": [
      {"type": "fulfillment", "target": "Matt 11:14", "note": "Behold I will send you Elijah the prophet before the great and awesome day of the LORD comes — Jesus identifies John the Baptist as the Elijah who was to come (Matt 11:14; 17:12): if you are willing to accept it, he is Elijah who is to come; the angel's announcement (Luke 1:17: he will go before him in the spirit and power of Elijah) grounds John's identity in Malachi's prophecy"}
    ],
    "6": [
      {"type": "allusion", "target": "Luke 1:17", "note": "He will turn the hearts of fathers to their children and the hearts of children to their fathers — the Elijah-prophecy of Malachi 4:6 is applied to John the Baptist's ministry; Luke 1:17 applies it directly: he will turn the hearts of the fathers to the children, and the disobedient to the wisdom of the just"}
    ]
  }
}

MAL_ORIGINAL = {
  "3": {
    "1": "<p><strong>hineni sholech malachi ufinah derekh lefanai ufitom yavo el heikhalov haAdon asher atem mevaksim umalach haberit asher atem chafetzim hineh ba amar YHWH tzvaot</strong>: 'Behold, I send my messenger [<em>malachi</em>], and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple; and the messenger of the covenant in whom you delight, behold, he is coming, says the LORD of hosts.' The word <em>malachi</em> means 'my messenger' — the book's title is this very word. YHWH promises two figures: the forerunner messenger (= John the Baptist) and the Lord who suddenly comes to his temple (= Jesus). The Lord's coming to his temple is the incarnation and the temple-cleansings (John 2:13-22; Mark 11:15-17). The 'messenger of the covenant' combines the forerunner and the Lord in a way that the NT separates: John is the messenger of Mal 3:1a; Jesus is the Lord of Mal 3:1b.</p>"
  },
  "4": {
    "5": "<p>The closing oracle of Malachi (4:5-6) is also the closing oracle of the OT: 'Behold, I will send you Elijah the prophet before the great and awesome day of the LORD comes. And he will turn the hearts of fathers to their children and hearts of children to their fathers, lest I come and strike the land with a decree of utter destruction.' The Hebrew canon ends here — with a promise of Elijah's return and a warning of cursing if he is rejected. The NT opens with John the Baptist filling this role (Luke 1:17; Matt 11:14; 17:10-13). The OT ends in expectation; the NT opens in fulfillment. The 400-year inter-testamental silence is the space between Malachi's promise and Matthew's fulfillment — the waiting for the forerunner who will announce the Lord's coming.</p>"
  }
}

MAL_CONTEXT = {
  "1": {
    "1": "<p>Malachi is the last book of the OT in both the Hebrew canon's traditional order and the Christian canon. It was written ca. 450-430 BCE, after the return from exile, during a period of post-exilic religious laxness. The prophet addresses: priests who offer defiled offerings (1:6-2:9), men who divorce their wives (2:14-16), the community's failure to tithe (3:10), and the skepticism of those who question YHWH's justice (3:13-15). Its six disputation speeches (each opening with a divine claim, then an objection, then YHWH's response) address the demoralization of the restored community. Malachi is the bridge between the OT and the NT: its final oracles (3:1; 4:5-6) are the OT's last prophetic words, pointing directly to John the Baptist and Jesus, so that the NT's opening (Matt 1-3; Mark 1; Luke 1-3) is the direct fulfillment of Malachi's closing.</p>"
  }
}

MAL_CHRIST = {
  "3": {
    "1": "<p>A direct revelation: 'Behold, I send my messenger, and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple.' This oracle ends the OT's prophetic program: the next thing to happen is the forerunner's preparation and the Lord's arrival. Four hundred years of prophetic silence follow — and then John the Baptist appears in the wilderness (Matt 3:1-3; Mark 1:2-4), fulfilling Malachi 3:1 (combined with Isaiah 40:3). Jesus's entry into the temple (John 2:13-22; Mark 11:15-17) is the Lord's sudden coming to his temple. The NT's opening chapters are Malachi's oracle in motion. The closing words of the OT (Mal 4:5-6) and the opening words of the NT (Matt 1:1) are not separated by 400 years of divine absence but by the divine patience that was preparing the fullness of time (Gal 4:4: when the fullness of time had come, God sent forth his Son).</p>"
  },
  "4": {
    "5": "<p>A fulfillment: 'Behold, I will send you Elijah the prophet before the great and awesome day of the LORD comes.' The OT ends with a promise; the NT opens with its fulfillment. John the Baptist comes 'in the spirit and power of Elijah' (Luke 1:17) — not literally Elijah reincarnated (John explicitly denies being Elijah, John 1:21) but fulfilling Elijah's eschatological role as the forerunner who prepares the way. Jesus confirms: 'if you are willing to accept it, he is Elijah who is to come' (Matt 11:14). The Transfiguration scene (Matt 17:3) brings the literal Elijah alongside the literal Moses alongside the literal Christ — the forerunner and the law flanking the fulfillment. Malachi's final word (the turning of fathers' and children's hearts, lest the land be struck with a curse) is the new covenant's mission: the gospel brings family reconciliation within the covenant community and protects from the ultimate curse, which Christ has absorbed (Gal 3:13).</p>"
  }
}

def main():
    books_data = [
        ('lamentations', LAM_ECHO, LAM_ORIGINAL, LAM_CONTEXT, LAM_CHRIST),
        ('hosea', HOSEA_ECHO, HOSEA_ORIGINAL, HOSEA_CONTEXT, HOSEA_CHRIST),
        ('joel', JOEL_ECHO, JOEL_ORIGINAL, JOEL_CONTEXT, JOEL_CHRIST),
        ('amos', AMOS_ECHO, AMOS_ORIGINAL, AMOS_CONTEXT, AMOS_CHRIST),
        ('obadiah', OBAD_ECHO, OBAD_ORIGINAL, OBAD_CONTEXT, OBAD_CHRIST),
        ('jonah', JONAH_ECHO, JONAH_ORIGINAL, JONAH_CONTEXT, JONAH_CHRIST),
        ('micah', MICAH_ECHO, MICAH_ORIGINAL, MICAH_CONTEXT, MICAH_CHRIST),
        ('nahum', NAHUM_ECHO, NAHUM_ORIGINAL, NAHUM_CONTEXT, NAHUM_CHRIST),
        ('habakkuk', HAB_ECHO, HAB_ORIGINAL, HAB_CONTEXT, HAB_CHRIST),
        ('zephaniah', ZEPH_ECHO, ZEPH_ORIGINAL, ZEPH_CONTEXT, ZEPH_CHRIST),
        ('haggai', HAG_ECHO, HAG_ORIGINAL, HAG_CONTEXT, HAG_CHRIST),
        ('zechariah', ZECH_ECHO, ZECH_ORIGINAL, ZECH_CONTEXT, ZECH_CHRIST),
        ('malachi', MAL_ECHO, MAL_ORIGINAL, MAL_CONTEXT, MAL_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
