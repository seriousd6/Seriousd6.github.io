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
  "41": {
    "1": "<p>Ishmael, of royal blood, murders Gedaliah at the shared meal — a betrayal of table fellowship. The covenant meal violated by murder prefigures the Last Supper's shadow: 'one of you will betray me' (John 13:21). The one appointed to govern the remnant is cut down by an insider — the pattern of covenant treachery runs from Judas to the depths of human sin against those entrusted with the word.</p>",
    "2": "<p>Gedaliah and his men are struck down — the Babylonian-appointed governor of Judah killed. The end of the covenant community's reconstruction attempt through human political means. Christ establishes a kingdom 'not of this world' (John 18:36) precisely because every human political arrangement for the people of God is fragile and vulnerable to betrayal from within.</p>",
    "3": "<p>All the Chaldeans and the soldiers with Gedaliah are also killed. The collateral victims of covenant treachery — those associated with faithful governance suffer alongside the leader. In the NT, the suffering of the church follows the same pattern: those identified with Christ share his cross (2 Tim 3:12: 'all who desire to live a godly life in Christ Jesus will be persecuted').</p>",
    "4": "<p>The murder was done in secret — no one yet knew. The hidden crime before the community discovers it. The revelation of hidden things at judgment is a NT theme: 'There is nothing hidden that will not be disclosed' (Luke 12:2). Christ's resurrection exposed the hidden injustice of the cross as the world's verdict on the righteous one.</p>",
    "5": "<p>Eighty men come from the north with offerings of grain and incense for the ruined temple — still making pilgrimage to the destroyed sanctuary, mourning its loss. The instinct to worship even amid ruins points to the irreplaceable human need for the divine presence. Christ transforms the ruined temple into his own body (John 2:19-21) — the permanent sanctuary that cannot be destroyed by any enemy.</p>",
    "6": "<p>Ishmael goes out to meet the pilgrims weeping — false mourning as a manipulation tactic. The false face of grief used to lure the vulnerable is the pattern of false religion: appearing mournful, humble, devout, while concealing predatory intent. Jesus names this: 'they love to pray standing in the synagogues... to be seen by men' (Matt 6:5).</p>",
    "7": "<p>Ishmael slaughters the eighty pilgrims in the cistern. The cistern — a place meant to collect life-giving water — becomes a mass grave. The reversal of life-giving spaces into death mirrors the false prophet who brings death in the guise of life. Christ reverses this: the tomb becomes empty, the place of death becomes the sign of life (John 20:1-9).</p>",
    "8": "<p>Ten men of the eighty plead for their lives by offering hidden stores of wheat, barley, oil, and honey. They buy survival with what they have. The contrast with grace: in every human economy, survival requires resources. Christ's economy reverses this — 'Blessed are the poor in spirit' (Matt 5:3), and the poor in worldly resources receive the kingdom (Luke 6:20). Grace is given to those with nothing to offer.</p>",
    "9": "<p>The cistern where the bodies are thrown was made by King Asa for fear of Baasha — a military defense structure becomes a burial pit. Human defensive strategies become instruments of further tragedy. The fortifications we build for safety often become the places of our undoing. Christ is the only fortress that does not fail (Ps 46:1; Eph 6:11).</p>",
    "10": "<p>Ishmael carries away the king's daughters and all the people left at Mizpah as captives. The community taken captive by a treacherous insider — the deepest form of betrayal. Christ comes to proclaim liberty to captives (Luke 4:18; Isa 61:1) and to lead captivity captive (Eph 4:8 quoting Ps 68:18). The captivity caused by human treachery is reversed by divine redemption.</p>",
    "11": "<p>Johanan hears what Ishmael has done and takes his forces to pursue him. The intervention of a protector who rescues the captives — a pattern of deliverance. Every human deliverer in the OT (judges, kings, commanders) anticipates the ultimate Deliverer who pursues and rescues those taken captive by sin and death (Col 1:13: 'he has delivered us from the domain of darkness').</p>",
    "12": "<p>They catch up with Ishmael at the great pool of Gibeon — near where Joab and Abner's forces met (2 Sam 2:13). The historical weight of Gibeon as a site of contest between rival claimants. Christ's victory over death is the definitive resolution of all such contests — the final showdown after which there are no more rivals to the kingdom (1 Cor 15:25: 'he must reign until he has put all his enemies under his feet').</p>",
    "13": "<p>The people with Ishmael rejoice when they see Johanan's forces — they turn back to him. The people rescued from the false captor rush to the true deliverer. This is the pattern of conversion: recognizing in Christ the rescuer from the false lord who had them captive. 'Come to me, all who labor and are heavy laden, and I will give you rest' (Matt 11:28).</p>",
    "14": "<p>All the people Ishmael had taken captive turn and go over to Johanan. The complete transfer of loyalty from the false leader to the faithful one. Discipleship is this transfer: turning from whatever false allegiance had held captive — sin, self, the world — and returning to the one who will lead them home.</p>",
    "15": "<p>Ishmael escapes to the Ammonites with eight men. The treacherous one escapes with his faction intact, for now. The delay of justice for the wicked is a consistent OT experience that becomes a NT promise: 'It is mine to avenge; I will repay, says the Lord' (Rom 12:19). The escape of Ishmael is temporary; YHWH's judgment is patient but certain.</p>",
    "16": "<p>Johanan takes all the remnant — soldiers, women, children, eunuchs — from Gibeon. The comprehensive gathering of all who survived the catastrophe. The church is this kind of gathering: 'from every nation, tribe, people, and language' (Rev 7:9) — the comprehensive collection of those rescued from destruction under the leadership of the true deliverer.</p>",
    "17": "<p>They stay at Geruth Kimham near Bethlehem, intending to go to Egypt. The stopping place near Bethlehem — the city of David, the future birthplace of the Messiah. History's tragedies pass through the places that will later be filled with hope. Bethlehem, place of refuge for the fleeing remnant, will become the birthplace of the one who ends all fleeing (Matt 2:1).</p>",
    "18": "<p>They are afraid of the Babylonians because Ishmael killed Gedaliah. Fear drives them toward Egypt — the return to the place of bondage as a refuge from present threat. The human instinct to run back to familiar bondage rather than trust the uncertain future with YHWH is the root of spiritual regression. Christ calls his followers to trust rather than flee: 'Do not let your hearts be troubled; do not be afraid' (John 14:27).</p>"
  },
  "42": {
    "1": "<p>All the military commanders approach Jeremiah with the people — a unified community seeking divine guidance before a major decision. The instinct to seek prophetic counsel before acting is commendable. Jesus invites this same approach: 'Come to me... learn from me' (Matt 11:28-29). The problem in this chapter is not the asking but the predetermined answer they brought with them.</p>",
    "2": "<p>'Let our plea come before you, and pray to YHWH your God for all this remnant.' The appeal to Jeremiah as intercessor — a man who has access to YHWH. The NT fulfillment is Christ as the one mediator who intercedes for all (1 Tim 2:5; Heb 7:25). Every human intercessor in the OT is a shadow of the one Intercessor who stands between humanity and God permanently.</p>",
    "3": "<p>'That YHWH your God may tell us the way we should go and the thing we should do.' The prayer for divine direction of the path. This is precisely what Christ claims to provide in a definitive way: 'I am the way' (John 14:6). The remnant's prayer for guidance through Jeremiah becomes, in the NT, the direct access to the Way himself who is both guide and destination.</p>",
    "4": "<p>Jeremiah promises to pray and to tell them everything YHWH reveals — 'I will not keep back a word from you.' The faithful prophet who withholds nothing: Jesus makes the same claim to his disciples: 'I have made known to you everything that I have heard from my Father' (John 15:15). The prophetic transparency reaches its apex in the Son who reveals the Father completely (John 1:18).</p>",
    "5": "<p>The community swears: 'May YHWH be a true and faithful witness against us if we do not act according to all the word YHWH your God sends.' The solemn oath of obedience before hearing the word — promising compliance before knowing the content. This is exactly the spiritual posture that Christian discipleship requires: prior surrender to the will of YHWH before knowing every detail (Rom 12:1-2).</p>",
    "6": "<p>'Whether it is good or evil, we will obey the voice of YHWH our God.' The unconditional submission: good or evil (from our perspective), we will obey. This is the Gethsemane posture: 'Not my will, but yours, be done' (Luke 22:42). The remnant articulates the ideal that only Christ perfectly embodied — total submission to the Father's will regardless of personal cost.</p>",
    "7": "<p>After ten days the word of YHWH comes to Jeremiah. The divine delay — ten days of waiting for the word. Jesus often delays before responding (John 11:6: he stayed two days longer when Lazarus was sick). The wait is not indifference but timing: YHWH's word comes at the appointed moment, not on human demand.</p>",
    "8": "<p>Jeremiah summons all the commanders and the people — the full community hears the prophetic answer together. The word of YHWH is not a private oracle for leaders alone but a community-shaping proclamation. The church as the community that hears the word together (Col 3:16: 'let the word of Christ dwell in you richly... teaching and admonishing one another').</p>",
    "9": "<p>'Thus says YHWH, the God of Israel, to whom you sent me to present your plea before him.' The formal prophetic citation formula — YHWH speaks through Jeremiah in response to the community's petition. The answer to prayer comes through the word — the spoken and written divine address. In the NT, the Spirit guides the community through the word and prayer together (Acts 13:2-4).</p>",
    "10": "<p>'If you will remain in this land, then I will build you up and not pull you down; I will plant you and not pluck you up.' The conditional stay-and-flourish promise. The abiding-and-flourishing pattern is the vine-and-branches discourse in John 15:4-5: 'Whoever abides in me and I in him, he it is that bears much fruit, for apart from me you can do nothing.' The condition of remaining with YHWH/Christ is the precondition for all fruitfulness.</p>",
    "11": "<p>'Do not be afraid of the king of Babylon, of whom you are afraid. Do not be afraid of him, declares YHWH, for I am with you, to save you and to deliver you from his hand.' The <em>al-tira</em> oracle (do not fear) with its ground: 'I am with you.' Christ gives this same assurance at the commissioning: 'I am with you always, to the end of the age' (Matt 28:20). The basis for courage is not circumstances but divine presence.</p>",
    "12": "<p>'I will grant you mercy, that he may have mercy on you and let you remain in your own land.' YHWH will turn the hostile heart of Nebuchadnezzar toward mercy. The sovereign God who governs even enemy hearts (Prov 21:1: 'The king's heart is a stream of water in the hand of YHWH') grants mercy through unexpected channels. Joseph's brothers intended evil; YHWH intended good (Gen 50:20). Providence operates through hostile agents.</p>",
    "13": "<p>'But if you say, &ldquo;We will not remain in this land,&rdquo; disobeying the voice of YHWH your God.' The alternative path named explicitly: disobedience framed as not remaining. The structure of every temptation is to leave the place of obedience. The prodigal son leaves his father's house; Israel leaves the covenant land; Adam and Eve leave the garden as the consequence of disobedience. Departure from the word of God is the shape of sin.</p>",
    "14": "<p>'No, we will go to the land of Egypt, where we shall not see war... nor be hungry for bread, and there we will dwell.' The appeal of Egypt: no war, no hunger, security. The false refuge of the world promises exactly what only YHWH can provide — peace, provision, security. Jesus confronts the same temptation in the wilderness: bread, safety, kingdoms (Matt 4:1-11). The answer to every false promise is the word of God.</p>",
    "15": "<p>'Hear the word of YHWH, O remnant of Judah: Thus says YHWH of Hosts, the God of Israel, If you set your faces to enter Egypt and go to live there.' The repeated word of YHWH confronting the desire to flee. The persistence of the divine word against human preference is the shape of grace: YHWH does not simply grant what we want but speaks the truth we need. 'My grace is sufficient for you' is not the answer they wanted but the one that saves (2 Cor 12:9).</p>",
    "16": "<p>'The sword that you fear shall overtake you there in the land of Egypt, and the famine of which you are afraid shall follow close after you there into Egypt, and there you shall die.' The irony of flight from danger: the danger follows. There is no geographical solution to spiritual crisis. The prodigal's far country did not provide escape; Egypt will not provide escape. Christ alone is the hiding place that genuinely shelters: 'you are my hiding place; you will protect me from trouble' (Ps 32:7).</p>",
    "17": "<p>All who set their faces to go to Egypt shall die by sword, famine, and pestilence — none shall escape. The comprehensive judgment on flight from YHWH's word. The refusal to hear the prophetic word brings the disaster they feared. The NT parallel: 'How shall we escape if we neglect such a great salvation?' (Heb 2:3). Neglecting the word of God escalates the consequence, not reduces it.</p>",
    "18": "<p>'As my anger and wrath were poured out on the inhabitants of Jerusalem, so my wrath will be poured out on you when you go to Egypt.' The extension of covenant judgment to the diaspora who flee. YHWH's justice is not geographically limited — it follows covenant-breakers wherever they go. This is the dark side of 'where shall I flee from your presence?' (Ps 139:7-8) — the universal reach of YHWH extends to his covenant justice as much as to his covenant care.</p>",
    "19": "<p>'Do not go to Egypt. Know for a certainty that I have warned you today.' The stark, simple command. YHWH does not obscure the prophetic word in complexity — the command is plain. Jesus similarly gives clear commands: 'Follow me' (Mark 1:17), 'Repent and believe' (Mark 1:15). The clarity of the divine command strips away the pretense that the people did not know what was required.</p>",
    "20": "<p>'You have made a fatal mistake, for you sent me to YHWH your God, saying, &ldquo;Pray for us to YHWH our God, and whatever YHWH our God says, tell us and we will do it.&rdquo;' The fatal error named: consulting the word with prior intent to disobey it. This is the solemn warning of James 1:22: 'Be doers of the word, and not hearers only, deceiving yourselves.' Seeking God's guidance while planning to disobey is self-deception that escalates judgment.</p>",
    "21": "<p>'And I have told you today, but you have not obeyed the voice of YHWH your God in anything that he sent me to tell you.' The accountability statement: you have been told. The prophetic witness creates responsibility. 'If I had not come and spoken to them, they would not be guilty of sin, but now they have no excuse for their sin' (John 15:22). The word that saves also creates the accountability that judges.</p>",
    "22": "<p>'Know for a certainty that you shall die by the sword, by famine, and by pestilence in the place where you desire to go to live.' The prophetic word closes with certainty of consequence. The finality of YHWH's word against those who reject it anticipates the NT's urgency: 'now is the favorable time; behold, now is the day of salvation' (2 Cor 6:2). The window of grace is real, and its closing is as certain as YHWH's word.</p>"
  },
  "43": {
    "1": "<p>Azariah and Johanan declare that Jeremiah is lying and that Baruch has incited him against them. The accusation of deception against the faithful prophet is the signature response of those who reject the uncomfortable word. Jesus was accused of leading the people astray (Luke 23:2); his messengers faced the same charge (Acts 17:6-7). The true prophet is always vulnerable to the accusation of deception from those who prefer comfortable lies.</p>",
    "2": "<p>'For Baruch the son of Neriah has set you against us, to deliver us into the hand of the Chaldeans.' The scapegoating of the prophet's associate — blame the messenger's helper when you cannot directly accuse the messenger. The same pattern in the NT: when direct attacks on Jesus fail, opponents attack his disciples (John 9:34). Persecution disperses itself across the prophet and those around him.</p>",
    "3": "<p>The accusation is that the scribal assistant manipulated the prophet. The suspicion that truth-speakers are puppets of hidden agendas — conspiracy thinking as a defense against the word of God. Paul addresses this repeatedly: 'we have renounced disgraceful, underhanded ways... by the open statement of the truth we commend ourselves to everyone's conscience before God' (2 Cor 4:2).</p>",
    "4": "<p>Johanan and all the commanders and all the people disobey the voice of YHWH — going to Egypt. The communal act of disobedience: no one breaks rank to remain. The pressure of group disobedience is a perennial spiritual danger. Jesus names the corresponding call: 'Enter by the narrow gate. For the gate is wide and the way is easy that leads to destruction, and those who enter by it are many' (Matt 7:13).</p>",
    "5": "<p>They take the entire remnant, including those who returned from all the nations where they had been scattered, back to Egypt. The comprehensive gathering of the restored remnant — only to lead them back into bondage. The anti-Exodus completed. The NT reverses this: Christ gathers the scattered (John 11:52) not back to Egypt but to the true homeland, the new creation (Rev 21:1-4).</p>",
    "6": "<p>Men, women, children, the king's daughters, Jeremiah, and Baruch are all taken to Egypt. Jeremiah accompanies the disobedient community — the prophet goes with the people he cannot save from their choice. This is the pattern of Christ who goes with the sinful community to their death: 'He was numbered with the transgressors' (Isa 53:12; Mark 15:28). The servant of YHWH does not abandon the people even when they walk toward destruction.</p>",
    "7": "<p>They come to Tahpanhes — the royal city of Egypt. The entrance into Egypt's centers of power as the supposed place of safety. Every human fortress chosen instead of YHWH proves ultimately hollow. Heb 6:18-19 presents Christ as the one true place of refuge: 'we who have fled for refuge might have strong encouragement to hold fast to the hope set before us.' He is the anchor within the veil, not the shadow of Pharaoh's fortress.</p>",
    "8": "<p>The word of YHWH comes to Jeremiah even in Egypt — the divine word is not geographically limited. YHWH speaks to his prophet in Babylon (chs 25-26), in Jerusalem, and now in Egypt. The ubiquity of prophetic revelation anticipates the Spirit poured out in all places (Acts 2:17-18) and the risen Christ's promise to be with his disciples 'to the end of the age' wherever they go (Matt 28:20).</p>",
    "9": "<p>The sign-act: bury large stones in the pavement at Pharaoh's palace in Tahpanhes. Jeremiah's physical action speaks the divine word in the place of exile. The prophetic sign-act as embodied proclamation prefigures Christ who is himself the embodied word (John 1:14) — not merely announcing but enacting the divine message in his own person.</p>",
    "10": "<p>'I will send for Nebuchadnezzar... and he will set his throne above these stones that I have hidden, and he will spread his royal canopy over them.' Nebuchadnezzar is YHWH's servant even in Egypt — the instrument of divine judgment follows the fugitives to their chosen refuge. No human political alliance with Egypt can protect from YHWH's purposes. Only the kingdom that cannot be shaken remains (Heb 12:28).</p>",
    "11": "<p>'He shall come and strike the land of Egypt, giving to the pestilence those who are doomed to pestilence, to captivity those who are doomed to captivity, and to the sword those who are doomed to the sword.' The fates catalogued with precision — each person receives exactly what they fled from. The futility of flight from covenant consequences is complete. Christ's substitution at the cross is the only genuine transfer of this fate: 'he who knew no sin became sin for us, so that in him we might become the righteousness of God' (2 Cor 5:21).</p>",
    "12": "<p>'He shall clean the land of Egypt as a shepherd cleans his cloak of vermin.' The shepherd-cleaning imagery — YHWH as shepherd cleaning what is defiled. Jesus identifies as the Good Shepherd (John 10:11) whose cleaning reaches further: 'You are already clean because of the word I have spoken to you' (John 15:3). The divine cleansing accomplished through Christ is thorough and permanent.</p>",
    "13": "<p>The pillar of Beth-shemesh in Egypt will be broken down — the sacred columns of Egypt's solar religion demolished by YHWH's instrument. The gods of Egypt were powerless before YHWH at the Exodus (Exod 12:12) and remain so. Christ disarms the rulers and authorities, making a public spectacle of them (Col 2:15). Every false religious system ultimately yields before the one who is the light of the world (John 8:12).</p>"
  },
  "44": {
    "1": "<p>The word of YHWH to Jeremiah for the Jews in Egypt — at Migdol, Tahpanhes, Memphis, and Pathros. The comprehensive geographical address: the entire Jewish diaspora in Egypt receives the prophetic word. The word of God finds people wherever they have scattered. The NT commission reflects this same comprehensiveness: 'to the end of the earth' (Acts 1:8), and the Spirit falls on those assembled from 'every nation under heaven' (Acts 2:5).</p>",
    "2": "<p>'You have seen all the disaster I brought upon Jerusalem and all the cities of Judah.' The appeal to witnessed history as the ground for prophetic authority. YHWH's past acts authenticate the present word. The NT uses the same appeal: the resurrection is a historical fact witnessed by many (1 Cor 15:3-8) that authenticates everything Christ said and promised. Eyewitness testimony grounds faith.</p>",
    "3": "<p>'Because of the evil that they committed, provoking me to anger by going to burn offerings and serve other gods.' The idolatry that led to judgment catalogued once more. The repetition of the cause-consequence relationship is pedagogical: YHWH wants the survivors to understand why the catastrophe happened so they do not repeat it. Paul uses the same retrospective analysis of Israel's wilderness failures as instruction for the church (1 Cor 10:6-11).</p>",
    "4": "<p>'I sent to you all my servants the prophets, sending them persistently, saying, &ldquo;Do not do this abominable thing that I hate.&rdquo;' The long patience of YHWH — servant after servant, warning after warning. Jesus names this very pattern in the parable of the wicked tenants (Matt 21:34-36): servant after servant is sent, each rejected. The culminating sending is the Son himself (Matt 21:37).</p>",
    "5": "<p>'But they did not listen or incline their ear, to turn from their evil and make no offerings to other gods.' The persistent failure to hear — the hardened ear is the central diagnostic of covenant failure throughout Jeremiah. Christ's parable of the sower explains this hardness: the seed that falls on the path, on rocky ground, among thorns (Matt 13:3-7). The word is proclaimed; the receptivity of the heart determines the outcome.</p>",
    "6": "<p>'Therefore my wrath and my anger were poured out and kindled in the cities of Judah and in the streets of Jerusalem.' The wrath already executed as historical fact. The past tense (<em>poured out</em>) grounds the warning: this is what YHWH's anger looks like in history. Paul uses the same past tense for the wrath poured on the cross: 'God put forward [Christ] as a propitiation by his blood' (Rom 3:25) — the historical cross as the standard by which all wrath is measured.</p>",
    "7": "<p>'And now thus says YHWH... why do you commit great evil against yourselves?' The <em>lamah</em> (why?) question of YHWH — the divine inquiry into human self-destructive behavior. Sin is named as harm to oneself: 'you are cutting off from you man and woman, child and infant.' Jesus's language similarly frames sin as self-harm: 'The thief comes only to steal and kill and destroy' (John 10:10) — the one who practices sin is the slave of sin and the one who loses the abundant life.</p>",
    "8": "<p>'Provoking me to anger with the works of your hands, burning offerings to other gods in the land of Egypt.' The idolatry in Egypt continues the same pattern that destroyed Jerusalem. The same sin in a different geography produces the same result. This is the logic of the new covenant's universality: sin is not a local problem but a human problem, requiring a universal solution — Christ who 'takes away the sin of the world' (John 1:29).</p>",
    "9": "<p>'Have you forgotten the wickedness of your ancestors, the wickedness of the kings of Judah, the wickedness of their wives, your own wickedness, and the wickedness of your wives?' The comprehensive indictment across generations: ancestors, kings, wives, and the present generation all share the same sin. The generational transmission of sin is the diagnosis that the NT addresses: 'as in Adam all die, so also in Christ shall all be made alive' (1 Cor 15:22).</p>",
    "10": "<p>'They have not humbled themselves even to this day, nor have they feared, nor walked in my law and my statutes.' The triad of failure: no humility, no fear, no obedience. The Beatitudes address the first (Matt 5:3: 'blessed are the poor in spirit'), and the new covenant addresses the last (Jer 31:33: law written on hearts). Christ provides the grounds for all three: humility before a crucified Savior, reverence born of love, obedience from an indwelt heart.</p>",
    "11": "<p>'Behold, I will set my face against you for harm, to cut off all Judah.' The divine face turned against — the antithesis of the Aaronic blessing (Num 6:25: 'YHWH make his face shine on you'). This curse-side of the covenant faces toward Christ at the cross: 'My God, my God, why have you forsaken me?' (Matt 27:46) — the divine face turned away from the Son who bore the covenant curse, so that it might be turned toward those who believe.</p>",
    "12": "<p>They will consume all the remnant of Judah who set their faces to go to Egypt — sword and famine will destroy them all. The comprehensive judgment on the final remnant who chose Egypt. The NT counterpart is the solemn warning of Heb 10:26-27: 'if we go on sinning deliberately after receiving the knowledge of the truth, there no longer remains a sacrifice for sins.' Deliberate rejection of the known word escalates judgment.</p>",
    "13": "<p>'I will punish those who dwell in the land of Egypt, as I have punished Jerusalem.' The extension of covenant judgment to the diaspora: wherever they go, YHWH's covenant standards follow. The universality of the divine moral law reflects the character of the God who is present everywhere. Paul argues the same: 'when Gentiles... do by nature what the law requires... they are a law to themselves' (Rom 2:14-15). Covenant accountability is not geographically bounded.</p>",
    "14": "<p>None shall escape except a small remnant who return to the land of Judah. The survival of a small remnant out of the comprehensive judgment — the <em>she'erit</em> (remnant) theology that runs throughout the prophets. Paul uses this remnant theology in Rom 9:27 (citing Isa 10:22): 'Though the number of the sons of Israel be as the sand of the sea, only a remnant of them will be saved.' The remnant becomes the seed of the new people of God.</p>",
    "15": "<p>All the men who knew their wives were making offerings to the queen of heaven, and all the women standing by in a great assembly, answer Jeremiah. The organized religious resistance of the entire community — a group committed to their idolatry. The community bound together in false worship is the dark mirror of the church: a gathering that shares a common identity, but oriented toward the wrong object of devotion.</p>",
    "16": "<p>'As for the word that you have spoken to us in the name of YHWH, we will not listen to you.' The explicit, conscious refusal: we have heard and we reject. This is the gravest spiritual state — not ignorance but conscious rejection of the known word. Heb 6:4-6 describes those who have tasted the heavenly gift and fallen away — the impossibility of renewed repentance for those who crucify the Son of God afresh.</p>",
    "17": "<p>'But we will do everything that we have vowed — make offerings to the queen of heaven.' The vow to idolatry treated as binding — a covenant with the false god. Paul's warning about yokes of slavery (Gal 5:1) addresses this: being bound to what is not God is the deepest form of covenant unfaithfulness. Christ sets free those who are enslaved to vows made to false lords.</p>",
    "18": "<p>'But since we left off making offerings to the queen of heaven... we have lacked everything and have been consumed by sword and famine.' The inversion of the truth: they attribute their safety to the queen of heaven and their disaster to abandoning her. This is the consistent logic of idolatry — protecting the false god by reinterpreting the evidence. Jesus diagnoses this as the suppression of truth (cf. Rom 1:18).</p>",
    "19": "<p>'And as for us, did we make cakes for her and pour out drink offerings to her without our husbands?' The women's insistence on the communal nature of their worship — husbands knew and approved. The family-level complicity in idolatry shows how thoroughly the covenant community had been corrupted at every level. Reformation must go to the household level — why Joshua's declaration was 'as for me and my house, we will serve YHWH' (Josh 24:15).</p>",
    "20": "<p>Jeremiah speaks to all the people — men and women — who answered him. The inclusive prophetic address: both men and women, the whole community, receive the word. The NT fulfills this inclusivity: 'there is neither male nor female, for you are all one in Christ Jesus' (Gal 3:28), and the Spirit is poured out on both sons and daughters (Acts 2:17).</p>",
    "21": "<p>'Did not YHWH remember the offerings you made in the cities of Judah and in the streets of Jerusalem — you and your ancestors, your kings and your officials, and the people of the land?' The divine memory is complete and accurate — YHWH has not forgotten the history of their idolatry. The corollary: YHWH also remembers the faithful — 'Your name is written in the Lamb's book of life' (Rev 21:27). Divine memory is both the ground of judgment and the ground of salvation.</p>",
    "22": "<p>'YHWH could no longer bear your evil deeds and the abominations that you committed; therefore your land has become a desolation and a waste and a curse, without inhabitant, as it is to this day.' The divine patience exhausted — the limit of YHWH's forbearance reached in history. This is not divine abandonment but divine justice. Peter uses the same frame for the delay of the final judgment: 'The Lord is not slow to fulfill his promise... but is patient toward you, not wishing that any should perish' (2 Pet 3:9).</p>",
    "23": "<p>'It is because you burned offerings and because you sinned against YHWH and did not obey the voice of YHWH or walk in his law or in his statutes or in his testimonies that this disaster has happened to you.' The clear causal statement: covenant disobedience produces covenant curse. This is not mechanical karma but covenantal structure — the framework Christ fulfills by exhausting the curse himself (Gal 3:13: 'Christ redeemed us from the curse of the law by becoming a curse for us').</p>",
    "24": "<p>Jeremiah speaks to all the people, including all the women — the inclusive community receives the complete word. Every member of the community, including those least likely to be considered prophetic addressees in the ancient world, receives the full word of YHWH. The gospel's universality follows this pattern: the word reaches all without distinction.</p>",
    "25": "<p>YHWH confirms their oath to the queen of heaven — they will surely perform it. The solemn irony of confirmed covenant with a false god: they wanted to vow and YHWH holds them to it — not because YHWH approves but because the choice has consequences. The law of sowing and reaping (Gal 6:7-8) cannot be suspended: 'whatever one sows, that will he also reap.'</p>",
    "26": "<p>'Behold, I have sworn by my great name, says YHWH, that my name shall no more be invoked by the mouth of any man of Judah in all the land of Egypt.' The swearing by the divine name — the most solemn divine oath — against the idolatrous community. The covenant name of YHWH will not be associated with this community in Egypt. The NT counterpart: 'I never knew you; depart from me' (Matt 7:23). The name of YHWH/Christ will not be claimed by those who persist in covenant rebellion.</p>",
    "27": "<p>'I am watching over them for disaster and not for good, and all the men of Judah who are in the land of Egypt shall be consumed by the sword and by famine.' The divine watching for evil — the reversal of the promised watching for good (Jer 1:12: 'I am watching over my word to perform it'). The same divine attentiveness that brings blessing brings judgment when the covenant is broken. YHWH's sovereignty over human history does not change; only the direction of his purpose changes based on the covenant response.</p>",
    "28": "<p>A small number will escape the sword and return to Judah — they will know whose word stood. The remnant who return will have lived to see that Jeremiah's word was true. This is the purpose of fulfilled prophecy in the OT: to authenticate the prophetic word. The resurrection is the NT fulfillment of the same purpose — validating everything Jesus said and promised (Acts 2:32-36).</p>",
    "29": "<p>The sign: Pharaoh Hophra will be given into the hand of his enemies. The fall of the human fortress they chose instead of YHWH will itself be a sign confirming Jeremiah's word. Every historical confirmation of prophetic truth is a shadow of the final confirmation: 'every eye will see him, even those who pierced him' (Rev 1:7). The vindication of the true prophet is written into the structure of history.</p>",
    "30": "<p>Pharaoh Hophra is given into the hand of his enemies — as Zedekiah was given into the hand of Nebuchadnezzar. The parallel fates of Israel's king and Egypt's king before YHWH's judgment: no human throne is exempt from the divine reckoning. 'The kings of the earth set themselves... against YHWH and against his Anointed' (Ps 2:2), but Christ is the king before whom every king will bow (Phil 2:10-11).</p>"
  },
  "45": {
    "1": "<p>The word to Baruch is dated to the fourth year of Jehoiakim — when he wrote Jeremiah's dictated scroll (ch36). This brief oracle is placed here at the end of the 'Baruch narrative' section as a personal word to the prophet's companion. Its placement at the biographical section's conclusion frames the entire narrative of Jeremiah's ministry: the servant who carries the word needs a word for himself.</p>",
    "2": "<p>'Thus says YHWH, the God of Israel, to you, O Baruch.' The name-specific address from YHWH — the God of all Israel speaks personally to one man. The covenant God who addresses nations and history also addresses individuals by name. Jesus demonstrates this pattern: 'Zacchaeus' (Luke 19:5), 'Mary' (John 20:16), 'Simon son of Jonah' (Matt 16:17). The personal address of YHWH is the basis for Christian prayer as intimate encounter.</p>",
    "3": "<p>'You said, &ldquo;Woe is me! For YHWH has added sorrow to my pain. I am weary with my groaning, and I find no rest.&rdquo;' Baruch's lament — the exhaustion of carrying the prophetic burden in a generation that does not receive it. Paul's language matches: 'We are afflicted in every way, but not crushed; perplexed, but not driven to despair' (2 Cor 4:8). The servant of the word is permitted to name the weight of the calling without despair taking over.</p>",
    "4": "<p>'Behold, what I have built I am tearing down, and what I have planted I am plucking up — that is, the whole land.' YHWH himself is tearing down — the cosmic-scale deconstruction happening in history. In this context, personal ambitions and plans are shown to be part of a much larger divine project. Jesus places individual discipleship within the same cosmic frame: 'The Son of Man is going as it is written of him' (Matt 26:24). The individual's story is inside the larger story of divine purpose.</p>",
    "5": "<p>'And do you seek great things for yourself? Seek them not, for behold, I am bringing disaster upon all flesh, declares YHWH. But I will give you your life as a prize of war in all places where you go.' The minimalist covenant promise to Baruch: not greatness, not security, not success — just his life, preserved through the upheaval. This is the eschatological promise stripped to its essence: 'The one who endures to the end will be saved' (Matt 24:13). Christ's promise to his disciples in persecution is the same: not comfort but presence and ultimate life — 'I am the resurrection and the life' (John 11:25).</p>"
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
