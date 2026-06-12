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
    "1": "<p>Habakkuk prophesied ca. 605-598 BCE — after Babylon's decisive defeat of Assyria and Egypt at Carchemish (605 BCE) and before or during Nebuchadnezzar's first Judahite campaign (598-597 BCE). He is the only writing prophet whose primary mode is direct dialogue with YHWH rather than oracles to Israel; the book is structured as a formal <em>rib</em> (covenant lawsuit/complaint) in which the prophet brings charges and YHWH responds. The book's three-chapter arc: complaint about Judean injustice (1:2-4) → YHWH's Babylonian answer (1:5-11) → second complaint about YHWH's method (1:12-2:1) → five woe oracles against Babylon (2:6-20) → theophany-psalm of faith (ch3). The NT cites Habakkuk 2:4 three times (Rom 1:17; Gal 3:11; Heb 10:38), making it the most-quoted Minor Prophet verse in the Pauline corpus.</p>",
    "2": "<p><span class='term'>How long, O LORD, must I call for help and you will not hear?</span> — <em>ad-anah YHWH shiwwati</em>: the <em>ad-anah</em> (how long?) formula opens the classical lament structure (Ps 13:1-2; 74:10; 89:46; 94:3). Habakkuk deploys the formal complaint (<em>rib</em>) genre: a covenant party accusing the covenant-keeper of failing to uphold treaty obligations. <em>Chamas</em> (violence) is the keyword of the book and the specific trigger-word for the Flood in Gen 6:11-13 ('the earth was filled with <em>chamas</em>'). The implicit argument: if <em>chamas</em> required divine intervention then (the Flood), why does YHWH tolerate it now?</p>",
    "3": "<p><span class='term'>Why do you make me see injustice and stare at wickedness?</span> — the visual compulsion (<em>tabbitu</em> = stare intently) portrays the prophet as forced witness to evil against his will. <em>Shod</em> (destruction) and <em>chamas</em> (violence) alliterate in Hebrew; the sound-reinforcement underscores the accusation. <em>Rib</em> (legal dispute) and <em>madon</em> (contention) frame the social disorder as a collapsed judicial system — not merely violence but the failure of covenant mechanisms designed to address violence. The prophet's suffering as witness is itself a form of injustice: YHWH makes him see what should not be tolerated.</p>",
    "4": "<p><span class='term'>The law is paralyzed and justice never prevails</span> — <em>watafug ha-Torah</em>: <em>pug</em> (become numb, paralyzed, grow cold/stiff) describes the Torah as covenant instrument rendered unresponsive. <em>Mishpat lo yetze la-netzach</em> (justice never prevails permanently) — <em>netzach</em> = 'forever' or 'to a decisive end.' <em>Mequqqal ha-mishpat</em> (justice comes out twisted/bent) — <em>qalal</em> = distortion, the opposite of the straight judicial measure. Judicial corruption is the covenant's internal failure: more corrosive than external enemies because it destroys the community's self-repair mechanisms.</p>",
    "5": "<p><span class='term'>Look out among the nations and pay attention; be utterly astonished</span> — YHWH's first answer shifts the prophetic gaze from Judean local injustice to the international stage. <em>Himmahu</em> (be utterly astonished) — the root <em>tamah</em> = astonishment at the incomprehensible. <em>Ki po'el po'al bimechem</em> (I am doing something in your own days) — the divine work is already in motion within the prophet's lifetime. Paul cites this verse in Acts 13:41 at Pisidian Antioch as a warning against rejecting the gospel: the same incomprehensibility-structure applies — the new covenant work is as unbelievable as the Babylonian judgment, and equally dangerous to dismiss.</p>",
    "6": "<p><span class='term'>I am raising up the Chaldeans</span> — <em>hineni meqim et-ha-Kasdim</em>: the Chaldeans = the neo-Babylonian empire under Nabopolassar and Nebuchadnezzar II, who defeated Assyria at Nineveh (612 BCE) and Egypt at Carchemish (605 BCE). The Chaldeans' military characteristics described in vv6b-11 are historically accurate: extreme speed of advance, comprehensive siege capability, cavalry superiority. YHWH's '<em>hineni</em> raising up' frames Babylon as an instrument, not an autonomous actor — the same framing as Isa 10:5 ('Woe to Assyria, the rod of my anger').</p>",
    "7": "<p><span class='term'>They answer to no authority but their own</span> — <em>mimmennu mishpato use'eto yetze</em>: their judicial norm (<em>mishpat</em>) and their elevation (<em>se'et</em>) proceed from themselves alone. This is the theological danger: YHWH deploys a power that acknowledges no authority above itself, not even YHWH's. The Babylonian empire operated with an absolute divine-mandate ideology — Nebuchadnezzar as earthly regent of Marduk, accountable to no external standard. The instrument that forgets it is an instrument is also what Isa 10:12-15 warns against in the Assyrian parallel.</p>",
    "8": "<p><span class='term'>Their horses are faster than leopards and fiercer than wolves at dusk</span> — <em>ze'evei erev</em> (wolves of evening) = wolves that have been hungry all day, hunting at their most intense. The animal metaphors (leopard, wolf, eagle) were standard ANE military comparisons; Babylonian cavalry was genuinely feared for speed and surprise. <em>Uts</em> (they swoop) = the eagle-attack image for sudden assault from distance. Babylonian annals and the books of Kings both describe the rapid advance of Nebuchadnezzar's forces across Judah — from the north, down through the hill country, to Jerusalem — in a matter of weeks.</p>",
    "9": "<p><span class='term'>Their faces press forward like the east wind</span> — <em>megammat penehem qadimah</em>: the <em>ruach qadim</em> (east wind, sirocco) was associated in the ANE with destruction and death — Gen 41:6 (scorching wind), Ezek 17:10 (the east wind that dries up the transplanted vine), Jon 4:8 (the scorching east wind). The Babylonians came geographically from the northeast but the directional force of their advance felt like the destroying desert wind. <em>Yeasef kakkhol shevi</em> (he scoops up captives like sand) — the mass-deportation policy confirmed by Babylonian administrative records of Judahite exiles.</p>",
    "10": "<p><span class='term'>They mock kings and scoff at rulers; they laugh at every fortress</span> — the Babylonian attitude to existing political structures was contemptuous; they absorbed kingdoms rapidly. <em>Yitsbor afar wayilkedeha</em> (they pile up earth/siege ramps and take it) — the systematic Babylonian siege methodology: earthworks, ramps, battering rams. Excavation at Lachish (destroyed ca. 701 BCE by Assyria, again ca. 597 BCE by Babylon) shows the characteristic ramp-and-assault technique. No fortress was genuinely impregnable against a determined Babylonian siege — as Jerusalem discovered in 586 BCE.</p>",
    "11": "<p><span class='term'>Then his spirit charges ahead; he sweeps through and transgresses, ascribing his might to his own god</span> — <em>az chalaf ruach wayya'avor</em>: the Babylonian momentum carries forward past any resistance. <em>Veashem zu kocho le'elohav</em> (ascribing his might to his own god) — Babylon attributes military success to Marduk, not to YHWH who is the actual agent deploying them. This is the same pattern as Isa 10:12-15: Assyria's arrogance in claiming 'by the strength of my hand I have done this.' The instrument forgets it is an instrument — a pattern that sets up Babylon's own eventual judgment (Rev 18).</p>",
    "12": "<p><span class='term'>Are you not from everlasting, O LORD my God, my Holy One?</span> — the prophet pivots from complaint to theological confession as the ground for his second complaint. <em>Miqqedem</em> (from everlasting) — YHWH's eternal nature is the framework within which the historical anomaly of Babylon must be interpreted. <em>Lo namut</em> (we will not die) — covenant confidence, not personal optimism; the people of the eternal God cannot be finally destroyed. <em>Shattam le-mishpat</em> (you have appointed them for judgment, for correction) — the prophet accepts YHWH's sovereignty even while questioning his method; this acceptance is itself a form of <em>emunah</em>.</p>",
    "13": "<p><span class='term'>Your eyes are too pure to approve of evil; you cannot look upon wickedness</span> — <em>tehorah einayim mire'ot ra'</em>: the divine holiness is not merely the absence of evil but an active intolerance of it. This is the sharpest formulation of the theodicy problem: YHWH's holiness means he cannot countenance evil (<em>lo tuchal habbit el-amal</em>) — yet he is apparently using a more wicked nation to punish a less wicked one. The ANE understanding of divine justice was retributive proportionality; Habakkuk applies that standard to YHWH's method and finds the apparent inconsistency. The book does not resolve this by argument but by the theophany of ch3.</p>",
    "14": "<p><span class='term'>Why have you made humanity like the fish of the sea</span> — the fishing metaphor dominating vv14-17 was a powerful ANE image for imperial conquest: the great empire as fisherman, the nations as helpless catch. Egyptian and Assyrian reliefs depict conquered peoples as fish drawn up in nets. <em>Lo moshel bo</em> (no one to rule over them) — fish and creeping things lack the hierarchical ordering that would give them defense; they are atomized, anarchic prey. The absence of governance is both a description of Judean social collapse (v4) and of the helplessness before Babylonian power.</p>",
    "15": "<p><span class='term'>He hauls all of them up with a fishhook; he drags them away in his net</span> — the sequence: individual fishhook → net → dragnet portrays systematic, comprehensive harvest of peoples. The escalation from individual to mass-catch mirrors Babylon's policy: first individual targets (kings, nobles), then groups (craftsmen, soldiers), then whole populations. The Babylonian chronicles and 2 Kings 24-25 document exactly this progression in the Judahite campaigns of 605, 598-597, and 586 BCE.</p>",
    "16": "<p><span class='term'>So he offers sacrifices to his net and burns incense to his dragnet</span> — the military instrument becomes the object of worship: the idolatry of power, in which military success validates itself as divine favor. <em>Ki vahem shamen chelqo</em> (for by them his portion is rich) — the economic theology of empire: prosperity = divine approval; the mechanism of domination is sacralized. The NT parallel is Paul's critique of those whose 'god is their belly' (Phil 3:19) — the proximate cause of success becomes the ultimate object of devotion.</p>",
    "17": "<p><span class='term'>Will he keep on emptying his net, slaying nations without pity, forever?</span> — the final complaint question stands without immediate answer; the reader enters ch2 still holding the tension. <em>Hahiqreq yariqqo</em> (will he keep emptying his net?) — the insatiable appetite of empire, the net perpetually refilled. <em>Velokhmal laharog goyim</em> (slaying nations without pity, without sparing) — the covenant accusation-formula for merciless genocide; the same phrase Obadiah uses against Edom (Obad 14: 'you should not have handed over the survivors'). The question stands as the book's central tension.</p>"
  },
  "2": {
    "1": "<p><span class='term'>I will take my post at the watchtower and station myself on the rampart</span> — <em>al mishmarti e'emad</em>: the <em>mishmar</em> (watch-post, guard station) was the elevated position from which the prophetic watchman received and proclaimed divine messages. Ezekiel 33:7 develops the watchman metaphor most fully: 'I have made you a watchman for the house of Israel.' The elevated position implies wider perspective: the prophet sees the divine movements hidden from ground-level. <em>Va'atsapeh lirot mah yadabber-bi</em> (I will watch to see what he will say to me) — divine communication as deliberate waiting posture; the prophet positions himself to receive.</p>",
    "2": "<p><span class='term'>Write down the vision; inscribe it plainly on tablets so that the one who reads it can carry the message</span> — <em>kotov chazon uvaar al-ha-lukhot</em>: tablet-inscription for public display; <em>baer</em> (make plain, explain) appears in Deut 1:5 where Moses 'explains' the Torah. Written prophecy preserves the oracle for the future generation that will see its fulfillment. The parallel with Moses writing on tablets connects Habakkuk's vision to the Sinai covenant documentation, suggesting the same level of divine authority and public accountability. <em>Lema'an yarutz qore vo</em> (so that a runner reading it can carry the message) — legible at speed; urgent, public proclamation.</p>",
    "3": "<p><span class='term'>For the vision awaits its appointed time; it speaks of the final outcome and will not prove false</span> — <em>ki od chazon lammo'ed</em>: <em>mo'ed</em> (appointed time, set season) is the eschatological vocabulary of the covenant calendar — the same word for the sacred assembly seasons (Lev 23). The vision of the <em>qetz</em> (final outcome/end) is temporally fixed in YHWH's sovereign schedule. <em>Im yahemeh chakeh lo</em> (though it lingers, wait for it) — the imperative of patient waiting (<em>chakeh</em>) is the practical application of the 'appointed time' theology; cf. 'when the fullness of time had come' (Gal 4:4).</p>",
    "4": "<p><span class='term'>The righteous shall live by his faithfulness</span> — <em>vetzaddiq beemunato yichyeh</em>: <em>emunah</em> (faithfulness, steadfastness, reliability) covers a semantic range from 'reliability/fidelity' to 'trust/belief.' The contrast with the <em>puffed-up</em> soul (whose way is not right) establishes <em>emunah</em> as the opposite of self-reliant arrogance: the righteous person is characterized by covenant-faithfulness that endures under pressure. The DSS commentary (1QpHab, 2nd-1st c. BCE) reads 'his faith' as faithfulness to the Teacher of Righteousness. Paul's three NT citations (Rom 1:17; Gal 3:11; Heb 10:38) drove the Reformation's doctrine of justification by faith and remain the most-cited Minor Prophet verse in Christian theology.</p>",
    "5": "<p><span class='term'>Wine is a deceiver; the proud man cannot stay put</span> — <em>vehakkayin boged</em>: wine as the metaphor for Babylon's hubris and insatiability; the intoxication of imperial power. <em>He'hir nefesh ketze'ol</em> (he opens his appetite as wide as Sheol) — the Babylonian appetite for conquest is insatiable as death itself. Isa 5:14 uses the same Sheol-image for Jerusalem's arrogance. The comparison with Sheol/Death places imperial power in the category of cosmic anti-creation forces — the forces that must ultimately yield to the Creator who defined death's boundaries.</p>",
    "6": "<p><span class='term'>Woe to the one who piles up wealth that is not his own</span> — the first of five woe oracles (vv6-20) structuring Babylon's judgment. The ANE lament-form (<em>hoy</em> woe-cry) was spoken over corpses; to address Babylon with <em>hoy</em> places it in the position of the dead, anticipating the verdict before its execution. <em>Hamakbir lo she'eino</em> (who piles up what is not his) — the debt-accumulation through imperial predation. <em>Avitot</em> (pledged goods) taken as security and never returned violates Torah debt-law (Exod 22:26: 'if you take your neighbor's cloak in pledge, return it by sunset'); the imperial scale of this violation is the Mosaic law written in blood.</p>",
    "7": "<p><span class='term'>Will not your debtors suddenly turn on you?</span> — the reversal of creditor-debtor relationships; those Babylon has victimized become the agents of its downfall. <em>Uvezu lekha</em> (and you will become their plunder) — the precise symmetry of the covenant curse: what Babylon took (<em>baz</em>, plunder) will be taken from Babylon. Historical fulfillment came rapidly: Persia conquered Babylon in 539 BCE; Cyrus reversed the deportation policies and issued the decree allowing Judahite return (Ezra 1). The empire built on unjust profit was itself plundered.</p>",
    "8": "<p><span class='term'>Because you have plundered many nations, all the surviving peoples will plunder you</span> — the <em>lex talionis</em> at imperial scale: the covenant's retributive-justice principle applied internationally. <em>Dam adam uchamas eretz</em> (for the blood shed against humanity and for the violence against the land) — the four-term indictment: blood of individuals, violence against the land-ecosystem, the city as communal structure, and inhabitants as persons. This comprehensive scope anticipates Revelation's indictment of Babylon: 'in you was found the blood of prophets and of saints, and of all who have been slain on earth' (Rev 18:24).</p>",
    "9": "<p><span class='term'>Woe to him who makes unjust profit for his household, to place his nest on high</span> — second woe: against the economics of security-through-exploitation. <em>Lebatzo batzah ra'</em> (to make unjust profit) — <em>betza</em> (gain by cutting off, unjust profit) is the term for profit extracted by force or fraud. <em>Sum bammaron qinno</em> (to place his nest on high) — the bird-nest-as-security metaphor; cf. Obad 4 (Edom's eagle-nest arrogance). The height built on exploitation of others is the inversion of the covenant principle: security comes from YHWH (<em>maoz</em> in Nah 1:7), not from the accumulated plunder of others.</p>",
    "10": "<p><span class='term'>You have plotted the disgrace of your own household</span> — <em>yatzta boshet leveitekha</em>: the ironic reversal; the strategy designed to secure the household has produced its shame. <em>Boshet</em> (public shame, disgrace) is the community-visible opposite of the <em>kavod</em> (honor/glory) that motivated the unjust accumulation. <em>Vechotet nafshekhah</em> (you have brought guilt/sin upon yourself) — the act of exploitation is simultaneously self-condemnation: the legal guilt adheres to the perpetrator. The self-defeating logic of covenant violation: the means of security become the means of destruction.</p>",
    "11": "<p><span class='term'>For the very stone in the wall will cry out against you, and the wooden beam will echo the charge</span> — <em>aven miqqir tizaq</em>: the building materials themselves become legal witnesses. Stones from plundered cities or buildings constructed with unjust materials carry the testimony of their origin. The entire built environment of the imperial house is a witness against it. Jesus draws on this Habakkuk image in Luke 19:40 ('if they keep silent, the stones will cry out') — the created order as witness to both injustice and the presence of the covenant King.</p>",
    "12": "<p><span class='term'>Woe to the one who builds a city on bloodshed and founds a town by injustice</span> — third woe: against imperial city-building. The ancient Near Eastern city was the symbol of civilization and divine blessing — founded by gods, protected by patron deities, the seat of justice. <em>Damim</em> (bloodshed) and <em>avlah</em> (injustice) as building materials invert the civic ideal. Nebuchadnezzar's building inscriptions boast his construction projects; Habakkuk indicts their foundations. Jer 51:58 applies nearly identical language to Babylon's walls and gates: 'the thick wall of Babylon shall be leveled to the ground.'</p>",
    "13": "<p><span class='term'>Is it not indeed from the LORD of hosts that peoples labor only to fuel the flames</span> — <em>halo hineh me'et YHWH tzvaot</em>: YHWH is the agent who ensures empire's labor ultimately comes to nothing. <em>Vile'umim beyede-aish yig'au</em> (nations exhaust themselves for nothing) — the <em>tohu</em> (vanity/futility) of Eccl 1 applied to imperial labor. The futility of empire-building apart from YHWH is covenant logic: systems built on exploitation are self-consuming. Jer 51:58 repeats this word-for-word about Babylon's actual walls, prophesying their collapse.</p>",
    "14": "<p><span class='term'>For the earth will be filled with the knowledge of the glory of the LORD, as the waters cover the sea</span> — the great eschatological counter-reality at the center of the five woe oracles. This verse is nearly verbatim with Isa 11:9 ('the earth will be full of the knowledge of the LORD as the waters cover the sea') — sharing a common eschatological tradition. <em>Yeda'at kevod-YHWH</em> (knowledge of YHWH's glory) is the full covenant-relationship knowledge of YHWH's <em>kabod</em>. The empire covers the earth with violence now; the <em>kavod</em> will cover it ultimately, completely, and permanently. This verse is the answer to the theodicy-question of 1:13: YHWH cannot countenance evil forever because the final state is his glory filling the earth.</p>",
    "15": "<p><span class='term'>Woe to the one who makes his neighbor drink</span> — fourth woe: against forcing the cup of violence on others. <em>Hamashqeh re'ehu chemato</em> (who gives his neighbor to drink from his cup of wrath) — the cup-of-wrath metaphor (Jer 25:15-29; Isa 51:17-23; Rev 14:10) represents forced experience of divine/imperial punishment. <em>Ushmach</em> (so that you may exult/gloat) — the sadism of power, not merely strategic domination but enjoyment of the victim's degradation. The ANE treaty-curse literature includes curses about forced humiliation; Habakkuk is applying this category to Babylon's conduct toward the nations.</p>",
    "16": "<p><span class='term'>You will be glutted with shame instead of glory</span> — <em>shaba'ta qalon mikavodʼ</em>: the exact inversion of desired outcome; the pursuit of imperial <em>kavod</em> produces its opposite. <em>Shovvah gam atta</em> (drink in turn) — the cup of wrath passes; Babylon which administered judgment-by-cup will drink from it. <em>Kos yamin YHWH</em> (the cup in YHWH's right hand) — the right hand = the hand of covenantal power and judicial authority; YHWH's cup overturns Babylon's pretended glory. Historical fulfillment: Persia's conquest, Babylon's dismantling, Cyrus's decree — the empire's glory became its shame.</p>",
    "17": "<p><span class='term'>For the violence you did to Lebanon will overwhelm you</span> — <em>ki chamas Levanon yekhasekha</em>: the Lebanon cedar forests were systematically stripped by successive empires (Assyria, Babylon) for timber. The ecological devastation is cognizable as a covenant crime alongside human atrocities. <em>Washod behemot yechittan</em> (the terror brought upon the wildlife will recoil on you) — the covenant's scope extends to the non-human world; compare Gen 9:5 where YHWH demands an accounting for animal blood. The land and its creatures are covenant parties, not merely objects; their destruction falls under the same retributive logic as human violence.</p>",
    "18": "<p><span class='term'>What use is a carved idol when its maker has shaped it?</span> — fifth woe: against idolatry, the theological root of all preceding covenant violations. <em>Mah hoil pesel ki fesalhu</em> — the idol is human handiwork; its uselessness is self-evident. The idol-polemic tradition (Isa 40:18-20; 44:9-20; Jer 10:1-16; Ps 115:4-8) exposes the absurdity of worshipping what you made. <em>Yoreih sheker</em> (a teacher of lies) — the idol actively deceives; it trains its worshipers in falsehood about reality. This is not merely irreligion but epistemological corruption: the idolater has no reliable account of the world.</p>",
    "19": "<p><span class='term'>Woe to the one who says to a wooden idol, 'Awake!'</span> — the fifth woe made explicit; addressing the idol in the 2nd person intensifies the absurdity. <em>Hu' yoreh</em> (can it really teach?) — the rhetorical question whose answer is obviously no. <em>Hineh hu' tafus zahav vakesef</em> (see — it is overlaid with gold and silver) — external appearance of wealth and beauty cannot supply what is absent internally: <em>vekhol-ruach ein beqirbo</em> (there is no breath at all within it). The contrast positions v20: the idol has no <em>ruach</em>; YHWH has his temple. The idolater has gold but not life; the covenant community has the living God in his dwelling.</p>",
    "20": "<p><span class='term'>But the LORD is in his holy temple; let all the earth be silent before him</span> — <em>vaADONAI behekhal qodsho has milfanav kol-ha-aretz</em>: the majestic conclusion to the five woe oracles. Against the silent idols (v19) stands YHWH who is present in his temple (whether the cosmic temple of creation or the Jerusalem sanctuary). <em>Has</em> (silence, hush!) — the exclamatory command for reverential silence before the divine sovereign; cf. Zeph 1:7; Amos 6:10; Zech 2:13. The earth's silence before YHWH is the counterpoint to the clamor of empire and the empty words of idols. This verse is the theological resolution of chs 1-2's crisis: YHWH has not vacated the field; he is enthroned, and the nations must be silent before him.</p>"
  },
  "3": {
    "1": "<p><span class='term'>A prayer of Habakkuk the prophet, set to Shigionoth</span> — <em>shigionoth</em> (plural) may indicate a dithyrambic, passionately irregular song form; the singular <em>shiggayon</em> appears in Ps 7's superscription. Ch3 is formally a psalm — with <em>Selah</em> pause markers at vv3, 9, 13 and a liturgical instruction at v19 ('for the choir director: on stringed instruments') — appended to the prophetic dialogue. The formal shift from dialogic oracle to liturgical hymn marks the book's resolution: the theodicy of faith culminates not in argument but in worship. Habakkuk enters the argument through the mouth of the complaint-prophet (chs 1-2) and exits through the mouth of the praise-psalmist (ch3).</p>",
    "2": "<p><span class='term'>O LORD, I have heard your report and stood in awe; in the midst of the years, revive your work</span> — <em>shim'akha</em> (your report, what I have heard of you) = the content of chs 1-2 now received; the hearing generates <em>yare'ti</em> (reverential awe). <em>Chayyeh po'alkha bekerev shanim</em> (revive your work in the midst of the years) — the Exodus-conquest theophany (described in vv3-15) is the template: the prophet prays for that divine pattern to recur in history. <em>Beshinah rachem</em> (in wrath remember mercy) — not a cancellation of wrath but its tempering by covenant <em>chesed</em>; the same dynamic as Exod 34:6-7 (YHWH merciful and slow to anger, yet not clearing the guilty). This phrase became the primary Habakkuk text in Jewish liturgy for the Days of Awe (Rosh Hashanah, Yom Kippur).</p>",
    "3": "<p><span class='term'>God came from Teman; the Holy One came from Mount Paran</span> — the theophany locates YHWH approaching from the south/southeast: Teman = Edomite territory; Paran = the Sinai wilderness. This is the traditional direction of the Exodus theophany: Deut 33:2 ('the LORD came from Sinai, rose from Seir, shone forth from Mount Paran'); Judg 5:4-5 (Deborah's Song: 'when you marched from the field of Edom, the earth trembled'). The cosmic Warrior-God tradition in which YHWH advances from his Sinai base is one of the oldest forms in Israelite poetry — pre-monarchic, deeply embedded in the wilderness period's memory. <em>Selah</em> invites pause on this primordial approach.</p>",
    "4": "<p><span class='term'>His radiance shone like light; rays of brightness came from his hand; and there was the hiding place of his power</span> — <em>qarnayim miyado lo</em>: the <em>qarnayim</em> (rays/horns of light) is the same root as Exod 34:29-30, where Moses's face 'sent out rays' (<em>qaran</em>) after encountering YHWH. The divine radiance that made Moses's face shine and terrified Israel at Sinai is here the universal light of the cosmic theophany. <em>Vesham chebyonezo</em> (and there was the hiding place of his power) — the paradox: the most visible aspect of YHWH (the light) conceals his deepest power; the brightness is veil as much as disclosure.</p>",
    "5": "<p><span class='term'>Pestilence marched before him, and burning plague went out at his feet</span> — <em>dever</em> (pestilence/plague) and <em>reshef</em> (burning plague, pestilence-fire) are the divine warrior's heralds. In Canaanite mythology Reshef was the god of plague and war; here demythologized into YHWH's attendants. The Exodus plagues (Exod 7-12) are the historical referent: pestilence was the covenant instrument against Egypt. YHWH's cosmic march in ch3 recapitulates the Exodus on a universal scale — the plagues that struck Egypt are now the standard advance of the divine army.</p>",
    "6": "<p><span class='term'>He stopped and shook the earth; with a look he scattered the nations; the ancient mountains crumbled</span> — <em>amad vayemoded eretz</em> (he stood and measured/shook the earth): <em>madad</em> can mean both 'to measure' (surveying) and 'to shake.' <em>Vayater goyim</em> (he scattered the nations) — cf. Ps 68:1 ('let God arise, let his enemies be scattered'). <em>Harerei ad</em> (ancient mountains) and <em>givot olam</em> (eternal hills) — the most stable features of the physical world become unstable at the divine approach. The geological permanence that ANE peoples associated with divine foundations (mountains were the seats of gods) yields before the Creator who established them.</p>",
    "7": "<p><span class='term'>I saw the tents of Cushan in distress; the tent-curtains of the land of Midian trembled</span> — Cushan (likely south Arabian or Nubian) and Midian (south of Judah, east of Sinai) represent the surrounding nations who witness and tremble at the theophany. Their trembling at a God who is not their own demonstrates YHWH's universal sovereignty — not merely a regional deity. Midian appears in the Exodus tradition as the region of Moses's calling (Exod 3) and the initial Sinai theophanies; their trembling confirms this ch3 theophany recapitulates the Exodus event.</p>",
    "8": "<p><span class='term'>Were you angry at the rivers, O LORD? Was your wrath against the rivers, or your fury against the sea?</span> — the rhetorical questions invoke the Exodus traditions: the Reed Sea crossing (Exod 14-15), the Jordan crossing (Josh 3-4). The waters/sea (<em>yam</em>) in the OT cosmic framework represent both literal waters and the primordial chaos (Gen 1:2; Ps 89:9-10). YHWH's action against the waters was not anger at the waters per se but defense of his people — the purpose clause follows immediately. <em>Tirkav al-susekha markevotekha yeshu'ah</em> (you mounted your horses, your chariots of salvation) — YHWH as divine charioteer, the ANE divine-warrior image at its most concentrated.</p>",
    "9": "<p><span class='term'>Your bow was unsheathed and made bare; your sworn oaths to the tribes stood firm</span> — <em>shevu'ot mattot omer selah</em>: 'your sworn oaths (<em>shevu'ot</em>) to the tribes (<em>mattot</em>)' — the covenant oaths to the patriarchal tribes (Gen 15; 22:16-18; 26:3; 28:13-15) are the theological ground for the Exodus-conquest. YHWH's military action on Israel's behalf is covenant-oath fulfillment, not arbitrary favor. <em>Tivqa aretz neharot</em> (you split the earth open with rivers) — the water-splitting power now turns from sea-parting (Exod 14) to river-opening; the same sovereign who controlled the Reed Sea controls all water systems.</p>",
    "10": "<p><span class='term'>The mountains saw you and convulsed; the floodwaters swept past; the deep roared out its voice</span> — <em>ra'ukha yachilu harim</em> (the mountains writhed in labor-pain/fear) — the birth-agony metaphor for mountains suggests cosmic upheaval reaching to creation's foundations. <em>Tehom natan qolo</em> (the deep [<em>tehom</em>] gave its voice) — the primordial deep of Gen 1:2 that YHWH subdued at creation speaks again in response to the theophany; the same force that threatened chaos acknowledges the Creator's passage. The cosmic acknowledgment confirms that the divine approach is not merely natural phenomena but the Creator exercising original creative authority.</p>",
    "11": "<p><span class='term'>The sun and moon stood still in their places at the gleam of your flying arrows</span> — <em>shemesh yareach amad zevulah</em>: the primary allusion is Josh 10:12-13 (Joshua's long day at Gibeon: 'Sun, stand still at Gibeon, and moon, in the Valley of Aijalon'). The astronomical bodies halted as light from YHWH's own weapons replaced solar illumination. The theophany in Habakkuk recapitulates the conquest battles where cosmic forces were enlisted in YHWH's war — confirming that the coming divine action against Babylon will be as interventionist as the original conquest of Canaan.</p>",
    "12": "<p><span class='term'>In your fury you strode through the earth; in your anger you trampled the nations</span> — <em>bezan titz'ad eretz bezaaf tashresh goyim</em>: the divine march through the earth is simultaneously a judgment-march. The nations underfoot in the theophany are the historical enemies of Israel (Egypt, Canaan) whose defeat the theophany recapitulates — and by implication Babylon, whose defeat the prophet anticipates. The scope (earth, nations) contrasts with the specific purpose in v13 (your people, your anointed one): cosmic action for covenant-particular salvation.</p>",
    "13": "<p><span class='term'>You went out to save your people, to save your anointed one</span> — <em>yatza'ta leshaya' ammekha leshaya' et-meshichekha</em>: the entire cosmic theophany of vv3-12 has one purpose: salvation of the covenant people and the anointed one. <em>Meshichekha</em> (your anointed one) may refer to Israel as the corporate anointed, to the Davidic king, or proleptically to the messianic figure. <em>Machatzta rosh mibbeit rasha'</em> (you struck the head from the wicked household) — decapitation imagery for the empire (Egypt, Canaan, Babylon) whose power is broken at the top. The 'wicked household' whose head is removed is the specific counterpart to 'your people' who are saved.</p>",
    "14": "<p><span class='term'>You pierced the head of his warlords with their own weapons</span> — <em>naqavta vematav rosh</em>: the ironic judgment pattern in which the enemy's own weapons become the instrument of destruction — the same irony as Haman executed on Mordecai's gallows (Esth 7:10), David beheading Goliath with the giant's own sword (1 Sam 17:51). <em>Yelaku liseroteri la'akol anavim bamister</em> (they charged to scatter us, exulting as if to devour the poor in secret) — the oppressor's confidence in secrecy and surprise is exposed; the cosmic warrior sees and acts against what the empire thought it could do unobserved.</p>",
    "15": "<p><span class='term'>You trod through the sea with your horses, churning through great mounds of water</span> — the final theophany image returns to the sea: <em>darekhta vayam susekha</em> (you trod with your horses through the sea). YHWH did not merely part the water at the Reed Sea but charged through it with his cavalry — the active-warrior image contrasting with the passive 'waters parted' narrative. <em>Chomer mayim rabbim</em> (great mounds/heap of water) — the walls of water at the Reed Sea parting (Exod 14:22: 'the waters were a wall to them on their right and left'). The Exodus event is the anchor for all the theophany imagery in ch3.</p>",
    "16": "<p><span class='term'>When I heard, my whole body trembled; at the sound my lips quivered; rottenness crept into my bones</span> — the prophet's somatic response to the theophany; the physical body registers what the intellect has received. <em>Veteqev yavi' batzamai</em> (rottenness entered my bones) — complete dissolution of bodily confidence; cf. Dan 10:8 (Daniel's strength left him at the vision), Ezek 3:14-15 (Ezekiel overwhelmed). <em>Asher anuach leyom tzarah</em> (that I must wait quietly for the day of trouble) — the resolution: waiting posture (<em>nuach</em>, rest/quiet) for the coming Babylonian invasion, now understood as within YHWH's sovereign plan. This is the <em>emunah</em> of 2:4 expressed as embodied waiting-posture under physical terror.</p>",
    "17": "<p><span class='term'>Though the fig tree does not blossom and there is no fruit on the vine; though the olive harvest fails and the fields produce no food</span> — the most comprehensive statement of covenantal faith in the OT. Habakkuk lists every element of the ANE subsistence economy: <em>te'enah</em> (fig tree), <em>gefen</em> (vine), <em>ma'aseh zayt</em> (olive yield), <em>sadot</em> (fields, grain), <em>miqneh</em> (livestock), <em>baqar</em> (cattle). The six-term list covers every agricultural and pastoral element of a pre-industrial economy. Total failure of all six simultaneously = worst imaginable catastrophe; the systematic 'though... though... though' accumulation escalates to the point of total deprivation. This is a description of what the Babylonian conquest and subsequent famine would produce — lived experience that threatened to make faith appear absurd.</p>",
    "18": "<p><span class='term'>Yet I will exult in the LORD; I will rejoice in the God of my salvation</span> — <em>va'ani baADONAI e'eloze agil be'elohei yish'i</em>: the pivot on <em>va'ani</em> (yet I/but I) is the great faith-declaration of the book. Two verbs of rejoicing: <em>e'eloze</em> (exult, rejoice with leaping) and <em>agil</em> (rejoice with circling/spinning) — active, embodied joy of covenant worship. <em>Elohei yish'i</em> (God of my salvation) — <em>yish'i</em> is the possessive of <em>yeshua'</em> (salvation); the personal appropriation of the salvific God under conditions of total material deprivation. Mary's Magnificat (Luke 1:47: 'my spirit rejoices in God my Savior') echoes Habakkuk's declaration, applying the same structure to the incarnation as the ultimate form of YHWH's saving presence.</p>",
    "19": "<p><span class='term'>The Lord GOD is my strength; he gives me feet like a deer and makes me walk on the heights</span> — <em>ADONAI Elohim cheli</em>: the covenant divine name with the additional <em>Elohim</em> (God-in-power) emphasizes both relational covenant (<em>ADONAI</em>) and sovereign might (<em>Elohim</em>) as the prophet's <em>chayil</em> (strength, army-force). <em>Kachalot raglai</em> (feet like hinds/deer) — the deer traverses mountain terrain inaccessible to human feet; 2 Sam 22:34 and Ps 18:33 use the same image for David's YHWH-empowered agility. <em>Al bamotai yadrekheni</em> (he makes me walk on my high places) — the mountain-heights are the covenant person's inheritance even when the valleys are stripped bare. The book ends with liturgical instruction ('for the choir director: on stringed instruments'), placing this theodicy-resolution within the community's ongoing worship.</p>"
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
  "2": {
    "7": "<p>A type: 'And I will shake all nations, so that the treasures of all nations shall come in, and I will fill this house with glory, says the LORD of hosts.' The 'treasures/desired things of all nations' (<em>chemdah</em>) coming to the temple has been read messianically (the Vulgate translates it 'veniet Desideratus cunctis gentibus', 'the one desired by all nations will come'). Whether or not this is the primary meaning, the pattern is clear: the nations streaming to the temple with their wealth is the OT vision of the eschatological gathering of all peoples to YHWH's dwelling. In the NT: the Magi (Gentile wise men) coming to the Christ-child with their treasures (Matt 2:11) is one fulfillment; the nations bringing their glory into the new Jerusalem (Rev 21:24-26) is the final fulfillment. The temple's latter glory exceeds the former because it is the glory of the incarnate Son and ultimately the new creation temple where God dwells with his people forever.</p>"
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
