#!/usr/bin/env python3
"""BP H3 — Hebron → Hill of Evil Counsel (75 articles)."""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    p = os.path.join(OUT_DIR, f'{slug}.json')
    with open(p, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
"hebron": {
    "term": "Hebron",
    "category": "places",
    "intro": "<p>Hebron (meaning <em>society; friendship</em>) is one of the most ancient cities in Canaan, located in the Judean hill country about 20 miles south of Jerusalem at an elevation of roughly 3,000 feet. It was \"built seven years before Zoan in Egypt\" (Num. 13:22), making it among the oldest continuously inhabited cities in the world. Abraham dwelt and built an altar at the oaks of Mamre near Hebron (Gen. 13:18), and Sarah died and was buried there in the cave of Machpelah, which Abraham purchased from Ephron the Hittite as the family burial ground (Gen. 23:2–20). Isaac and Rebekah, Jacob and Leah were also buried there. After the conquest, Caleb received Hebron as his inheritance because of his faithfulness as a spy (Josh. 14:13–14). David was anointed king at Hebron and reigned there seven and a half years over Judah before capturing Jerusalem (2 Sam. 2:1–4; 5:5). Hebron was also the city from which Absalom launched his rebellion (2 Sam. 15:10) and was designated one of the six cities of refuge (Josh. 20:7).</p>",
    "hitchcock_meaning": "society; friendship",
    "source_ids": {"easton": "hebron", "smith": "hebron", "isbe": "hebron"},
    "key_refs": ["Genesis 13:18", "Genesis 23:2", "Joshua 14:13", "2 Samuel 2:1"]
},
"hegai": {
    "term": "Hegai",
    "category": "people",
    "intro": "<p>Hegai (or Hege, possibly meaning <em>meditation; groaning</em>) was the eunuch in charge of the harem of King Ahasuerus (Xerxes I) of Persia. When the young women were gathered for the king's selection of a new queen after the deposition of Vashti, Esther was placed under Hegai's custody. The text notes that Esther \"obtained kindness of him,\" and Hegai quickly provided her with cosmetics, her appointed portions of food, seven chosen maidens, and the best place in the harem (Esth. 2:8–9). His favor toward Esther foreshadows her selection as queen. Hegai's advice guided Esther on what to take when she came before the king (Esth. 2:15), and the king chose her above all the other women.</p>",
    "hitchcock_meaning": "meditation; word; groaning; separation",
    "source_ids": {"easton": "hegai"},
    "key_refs": ["Esther 2:8", "Esther 2:15"]
},
"heifer": {
    "term": "Heifer",
    "category": "concepts",
    "intro": "<p>A heifer is a young cow that has not yet had a calf, and several distinct ritual uses of heifers appear in the Old Testament. The red heifer ceremony of Numbers 19 was among the most important purification rites: an unblemished red cow on which no yoke had been placed was slaughtered and burned outside the camp, and its ashes were mixed with water to produce \"water of purification\" for cleansing those who had become ceremonially unclean through contact with a corpse. The ritual was acknowledged as a <em>chukkat</em> — a divine ordinance without a fully explained rationale. A heifer's neck was broken in the valley to atone for an unsolved murder under the ordinance of Deuteronomy 21:1–9, removing bloodguilt from a community. Jeremiah compares Egypt to \"a very fair heifer\" soon to be stung into flight (Jer. 46:20). In the New Testament, Hebrews 9:13 contrasts the ashes of the heifer with the blood of Christ, whose sacrifice accomplishes what the ritual could only foreshadow.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "heifer"},
    "key_refs": ["Numbers 19:2", "Deuteronomy 21:4", "Hebrews 9:13"]
},
"heir": {
    "term": "Heir",
    "category": "concepts",
    "intro": "<p>Inheritance and heirship in ancient Israel followed patrilineal primogeniture — the firstborn son received a double portion of the father's estate (Deut. 21:17). If a man had no sons, daughters could inherit on condition they marry within their tribe (Num. 27:1–11; 36). The laws of inheritance in Numbers 27 and 36 were established through the case of Zelophehad's daughters. In the New Testament, \"heir\" becomes a central theological metaphor: believers are described as heirs of God and co-heirs with Christ (Rom. 8:17), heirs of the kingdom promised to those who love God (James 2:5), and heirs of salvation (Heb. 1:14). The parable of the wicked tenants uses the language of \"the heir\" for the Son who is rejected and killed (Matt. 21:38). Christ himself is declared heir of all things (Heb. 1:2).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "heir"},
    "key_refs": ["Deuteronomy 21:17", "Romans 8:17", "Hebrews 1:2", "Galatians 4:7"]
},
"helah": {
    "term": "Helah",
    "category": "names",
    "intro": "<p>Helah was one of the two wives of Ashhur, the father of Tekoa, mentioned in the genealogy of Judah (1 Chr. 4:5, 7). Her sons were Zereth, Izhar, and Ethnan. The name may relate to a root meaning <em>rust</em> or <em>sickness</em>. Helah is mentioned only in this genealogical context with no further narrative detail.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "helah"},
    "key_refs": ["1 Chronicles 4:5"]
},
"helam": {
    "term": "Helam",
    "category": "places",
    "intro": "<p>Helam (meaning <em>their army; their trouble</em>) was a place east of the Jordan where the Syrians (Arameans) gathered under Hadarezer of Zobah to make war against David, after their initial defeat by Joab. David crossed the Jordan, met them in battle at Helam, and inflicted a decisive defeat — killing 700 chariot fighters and 40,000 horsemen, along with Shobach the commander (2 Sam. 10:16–18). After this defeat the Aramean kings who had been vassals of Hadarezer made peace with Israel and submitted to David. The exact location of Helam is uncertain.</p>",
    "hitchcock_meaning": "their army; their trouble",
    "source_ids": {"easton": "helam"},
    "key_refs": ["2 Samuel 10:16", "2 Samuel 10:17"]
},
"helbah": {
    "term": "Helbah",
    "category": "places",
    "intro": "<p>Helbah (related in meaning to Helbon, meaning <em>milk; fatness</em>) was a town in the territory of Asher from which the tribe failed to expel the Canaanite inhabitants (Judg. 1:31). It appears in the list of unoccupied Canaanite towns alongside Achzib, Helbah, Aphik, and Rehob, reflecting the broader pattern of incomplete conquest in the coastal and northern regions. The site has not been positively identified.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "helbah"},
    "key_refs": ["Judges 1:31"]
},
"helbon": {
    "term": "Helbon",
    "category": "places",
    "intro": "<p>Helbon (meaning <em>milk; fatness</em>) was a place noted for the quality of its wine, mentioned in Ezekiel's lament over Tyre: \"Damascus was thy merchant in the multitude of the wares of thy making, for the multitude of all riches; in the wine of Helbon, and white wool\" (Ezek. 27:18). Helbon was evidently a wine-producing district that supplied the luxury markets of Tyre and Damascus. It has been identified with the modern village of Halbun, about 12 miles north of Damascus in a fertile valley still known for viticulture.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "helbon"},
    "key_refs": ["Ezekiel 27:18"]
},
"heldai": {
    "term": "Heldai",
    "category": "names",
    "intro": "<p>Heldai (meaning <em>the world; rustiness</em>) is the name of two men in the Old Testament. (1.) A commander of the twelfth monthly division of David's army (1 Chr. 27:15), also apparently called Heled and Heleb (2 Sam. 23:29; 1 Chr. 11:30), one of David's mighty men. (2.) One of the exiles who returned from Babylon bringing silver and gold, from whom Zechariah was commanded to make a crown for the high priest Joshua son of Jehozadak as a prophetic act pointing to the coming Branch (Zech. 6:10, 14, where he is also called Helem in verse 14).</p>",
    "hitchcock_meaning": "the world; rustiness",
    "source_ids": {"easton": "heldai"},
    "key_refs": ["1 Chronicles 27:15", "Zechariah 6:10"]
},
"heleb": {
    "term": "Heleb",
    "category": "names",
    "intro": "<p>Heleb (also Heled or Heldai) was a son of Baanah the Netophathite, one of David's thirty mighty men (2 Sam. 23:29; 1 Chr. 11:30). The variations in spelling across manuscripts reflect the transmission of proper names in ancient Hebrew texts. His hometown Netophah was a village near Bethlehem. Beyond his inclusion in the elite warrior list, no individual exploits of Heleb are recorded in the biblical text.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "heleb"},
    "key_refs": ["2 Samuel 23:29", "1 Chronicles 11:30"]
},
"heled": {
    "term": "Heled",
    "category": "names",
    "intro": "<p>Heled is a variant spelling of Heleb (see also Heldai), a son of Baanah the Netophathite and one of David's mighty men listed in 1 Chronicles 11:30. The name appears with slight orthographic variations across the parallel lists in Samuel and Chronicles, reflecting normal textual transmission differences for minor names. He was part of the elite corps of warriors known as the Thirty who served David with exceptional courage.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "heled"},
    "key_refs": ["1 Chronicles 11:30"]
},
"helek": {
    "term": "Helek",
    "category": "names",
    "intro": "<p>Helek (meaning <em>part; portion</em>) was the second son of Gilead and grandson of Manasseh (Num. 26:30; Josh. 17:2). He was the founder of the Helekite clan within the half-tribe of Manasseh that settled in Canaan. The name is preserved in the Samaria ostraca — ancient inscribed pottery from the 9th–8th centuries B.C. that mention estate names corresponding to Manassehite clans including Helek, confirming the biblical genealogical tradition.</p>",
    "hitchcock_meaning": "part; portion",
    "source_ids": {"easton": "helek"},
    "key_refs": ["Numbers 26:30", "Joshua 17:2"]
},
"helem": {
    "term": "Helem",
    "category": "names",
    "intro": "<p>Helem (meaning <em>dreaming; healing</em>) appears in two contexts. (1.) A man of the tribe of Asher, son of Heber (1 Chr. 7:35), also called Hotham. (2.) In Zechariah 6:14, Helem is named alongside Tobijah, Jedaiah, and Hen as recipients of the symbolic crown — likely an alternative form of the name Heldai (Zech. 6:10), one of the exiles who brought silver and gold from Babylon to the prophet Zechariah.</p>",
    "hitchcock_meaning": "dreaming; healing",
    "source_ids": {"easton": "helem"},
    "key_refs": ["1 Chronicles 7:35", "Zechariah 6:14"]
},
"heleph": {
    "term": "Heleph",
    "category": "places",
    "intro": "<p>Heleph (meaning <em>changing; passing over</em>) was a town marking the northern boundary of Naphtali's allotment in Canaan (Josh. 19:33). It is listed as a border point along with Allon-bezaanannim and other towns in Naphtali's northern territory. The site has not been positively identified, though it was somewhere in the lower Galilee region.</p>",
    "hitchcock_meaning": "changing; passing over",
    "source_ids": {"easton": "heleph"},
    "key_refs": ["Joshua 19:33"]
},
"helez": {
    "term": "Helez",
    "category": "names",
    "intro": "<p>Helez (meaning <em>armed; set free</em>) is the name of two men. (1.) Helez the Paltite (or Pelonite), one of David's thirty mighty men, also the commander of the seventh monthly division of the army (2 Sam. 23:26; 1 Chr. 11:27; 27:10). (2.) A man of Judah, son of Azariah, mentioned in the genealogy of 1 Chronicles 2:39.</p>",
    "hitchcock_meaning": "armed; set free",
    "source_ids": {"easton": "helez"},
    "key_refs": ["2 Samuel 23:26", "1 Chronicles 27:10"]
},
"heli": {
    "term": "Heli",
    "category": "names",
    "intro": "<p>Heli (meaning <em>ascending; climbing up</em>) is listed in Luke's genealogy of Jesus as the father of Joseph, the husband of Mary (Luke 3:23). This creates an apparent discrepancy with Matthew's genealogy (Matt. 1:16), which names Jacob as Joseph's father. Several solutions have been proposed: that Luke gives Mary's genealogy while Matthew gives Joseph's, making Heli Mary's father; that the levirate marriage custom accounts for the two lines; or that one is a legal and the other a biological descent. Heli is distinct from Eli the high priest of Shiloh whose name is similarly spelled in Greek.</p>",
    "hitchcock_meaning": "ascending; climbing up",
    "source_ids": {"easton": "heli"},
    "key_refs": ["Luke 3:23"]
},
"helkai": {
    "term": "Helkai",
    "category": "names",
    "intro": "<p>Helkai (meaning the same as Helek — <em>part; portion</em>) was a priest heading the family of Meraioth in the days of the high priest Joiakim, who served in Jerusalem after the return from Babylonian exile (Neh. 12:15). He appears in the list of priestly families and their heads during the period of Nehemiah's reforms, one of many names preserved in that community's careful record-keeping of the restored priesthood.</p>",
    "hitchcock_meaning": "same as Helek",
    "source_ids": {"easton": "helkai"},
    "key_refs": ["Nehemiah 12:15"]
},
"helkath": {
    "term": "Helkath",
    "category": "places",
    "intro": "<p>Helkath (meaning <em>part; portion of the field</em>) was a border town in the territory of Asher (Josh. 19:25), assigned as a Levitical city to the Gershonite Levites (Josh. 21:31). In 1 Chronicles 6:75 it is called Hukok. The site is generally identified with modern Tell el-Qasis in the Kishon Valley east of Haifa, though certainty is elusive. It served both as a boundary marker for Asher's allotment and as one of the cities where Levites were stationed among the tribes.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "helkath"},
    "key_refs": ["Joshua 19:25", "Joshua 21:31"]
},
"helkath-hazzurim": {
    "term": "Helkath-hazzurim",
    "category": "places",
    "intro": "<p>Helkath-hazzurim (meaning <em>the field of strong men</em> or <em>field of the rock-edges</em>) was a field near the pool of Gibeon where a fateful combat took place at the outset of the conflict between the house of Saul and the house of David. At Abner's suggestion, twelve men from Benjamin representing Saul's house and twelve from Judah representing David's fought each other simultaneously; each man seized his opponent's head and thrust his sword into his side, so that all twenty-four fell together (2 Sam. 2:12–16). This inconclusive \"tournament\" led immediately to a larger battle in which Asahel was slain by Abner, setting in motion the blood feud that would lead to Abner's eventual murder by Joab.</p>",
    "hitchcock_meaning": "the field of strong men, or of rocks",
    "source_ids": {"easton": "helkath-hazzurim"},
    "key_refs": ["2 Samuel 2:16"]
},
"hell": {
    "term": "Hell",
    "category": "concepts",
    "intro": "<p>\"Hell\" in English translations renders three distinct biblical terms. (1.) Hebrew <em>Sheol</em> (65 occurrences in the OT) denotes the realm of the dead — not a place of punishment per se but the unseen world where all the dead go. It is rendered \"grave,\" \"pit,\" and \"hell\" in the KJV. (2.) Greek <em>Hades</em> is the NT equivalent of Sheol, the place of the dead awaiting judgment (Luke 16:23; Rev. 20:13–14). In Jesus' parable of the rich man and Lazarus, Hades already contains torment for the wicked (Luke 16:23). (3.) Greek <em>Gehenna</em> (12 of 13 NT occurrences on the lips of Jesus) is the place of final punishment — derived from the Valley of Hinnom (Hebrew <em>gê-hinnōm</em>) south of Jerusalem, where child sacrifice had been practiced and which became a smouldering rubbish heap, a vivid symbol of destruction. Gehenna is described as a place of unquenchable fire (Mark 9:43–48; Matt. 5:22; 10:28). Revelation 20:14 describes the lake of fire as \"the second death.\" These terms must be distinguished to understand the Bible's developing eschatology of the afterlife.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hell", "smith": "hell", "isbe": "hell"},
    "key_refs": ["Luke 16:23", "Matthew 10:28", "Revelation 20:14", "Mark 9:43"]
},
"helmet": {
    "term": "Helmet",
    "category": "concepts",
    "intro": "<p>A helmet was a protective head covering worn in battle, made of bronze or iron for warriors and of leather for lighter infantry. In the OT, Goliath wore a bronze helmet (1 Sam. 17:5), and Saul fitted David with his own bronze helmet before the duel — which David removed (1 Sam. 17:38–39). Helmets are mentioned among the military equipment of various armies (2 Chr. 26:14; Ezek. 27:10). In the New Testament, Paul employs the helmet as a metaphor in his description of the spiritual armor: \"the helmet of salvation\" (Eph. 6:17), and in 1 Thessalonians 5:8 he speaks of the \"hope of salvation as a helmet,\" grounding the protective function in the confident hope of final deliverance in Christ.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "helmet"},
    "key_refs": ["1 Samuel 17:5", "Ephesians 6:17", "1 Thessalonians 5:8"]
},
"helon": {
    "term": "Helon",
    "category": "names",
    "intro": "<p>Helon (meaning <em>window; grief</em>) was the father of Eliab, who led the tribe of Zebulun during the wilderness period (Num. 1:9; 2:7; 7:24, 29; 10:16). Eliab son of Helon assisted Moses in the census of Israel and represented Zebulun in the tabernacle dedication offerings, presenting his tribe's gifts on the fifth day. Helon himself appears only as a patronymic and is not otherwise mentioned in the narrative.</p>",
    "hitchcock_meaning": "window; grief",
    "source_ids": {"easton": "helon"},
    "key_refs": ["Numbers 1:9", "Numbers 2:7"]
},
"help-meet": {
    "term": "Help-meet",
    "category": "concepts",
    "intro": "<p>\"Help-meet\" (sometimes rendered \"helpmeet\" as one word) translates the Hebrew phrase <em>'ēzer kenegdô</em> in Genesis 2:18: \"It is not good that man should be alone; I will make him a help meet for him\" — meaning a helper corresponding to him or suitable to him. The word <em>'ēzer</em> (helper, ally) is used elsewhere of God himself as Israel's help (Ps. 121:2; 124:8), carrying no connotation of inferiority. The phrase <em>kenegdô</em> means \"as his counterpart\" or \"equal and opposite\" — someone who corresponds to the man and complements him. The creation of woman from the man's rib (Gen. 2:21–23) and Adam's recognition of her as \"bone of my bone and flesh of my flesh\" grounds the institution of marriage as the divinely ordained partnership of man and woman. Paul's language of mutual submission (Eph. 5:21–33) and Peter's description of women as \"fellow heirs of the grace of life\" (1 Pet. 3:7) build on this foundational creation account.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "help-meet"},
    "key_refs": ["Genesis 2:18", "Psalms 121:2", "1 Peter 3:7"]
},
"helps": {
    "term": "Helps",
    "category": "concepts",
    "intro": "<p>\"Helps\" (Greek <em>antilēmpsis</em>, literally \"a laying hold of\" or \"supporting\") appears in Paul's list of spiritual gifts and ministries in 1 Corinthians 12:28: \"And God hath set some in the church, first apostles, secondarily prophets, thirdly teachers, after that miracles, then gifts of healings, helps, governments, diversities of tongues.\" The term likely refers to practical acts of assistance rendered to members of the community in need — charitable help, supportive care, or administrative service — rather than a specific miraculous endowment. The deacons' ministry described in Acts 6:1–6 may exemplify this kind of \"helps\" in its concrete form.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "helps"},
    "key_refs": ["1 Corinthians 12:28", "Acts 6:2"]
},
"hem": {
    "term": "Hem",
    "category": "concepts",
    "intro": "<p>The hem or border of a garment in ancient Israelite culture carried specific religious significance. Numbers 15:38–40 commanded Israelite men to wear tassels (Hebrew <em>tzitzit</em>) on the corners of their garments as a visual reminder to keep all the commandments of the LORD. The Hebrew word for corner (<em>kānāf</em>) also means wing or hem. The woman with the issue of blood touched \"the hem of his garment\" (Matt. 9:20; Luke 8:44), and crowds at Gennesaret sought to touch even the fringe of Jesus' robe (Matt. 14:36), reflecting the belief that divine healing power was present in this consecrated teacher. Jesus rebuked the Pharisees for enlarging their tassels to display their piety (Matt. 23:5).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hem"},
    "key_refs": ["Numbers 15:38", "Matthew 9:20", "Matthew 23:5"]
},
"heman": {
    "term": "Heman",
    "category": "people",
    "intro": "<p>Heman (meaning <em>faithful; their trouble; tumult</em>) is the name of two biblical figures. (1.) The son of Zerah of Judah, renowned for his wisdom — he is listed alongside Chalcol and Darda as men whose wisdom Solomon's surpassed (1 Kings 4:31; 1 Chr. 2:6). He may have authored Psalm 88, titled \"A Psalm of Heman the Ezrahite.\" (2.) The grandson of Samuel, son of Joel, a Levitical musician appointed by David as one of the chief singers and instrumentalists for the worship at the tabernacle (1 Chr. 6:33; 15:17; 25:1). This Heman led a choir of 14 sons and 3 daughters, representing the seventy \"horns\" by which God exalted him (1 Chr. 25:4–8). He was placed at the center of the three-man leadership of worship, flanked by Asaph on his right and Ethan (Jeduthun) on his left.</p>",
    "hitchcock_meaning": "their trouble; tumult; much; in great number",
    "source_ids": {"easton": "heman", "smith": "heman"},
    "key_refs": ["1 Kings 4:31", "1 Chronicles 6:33", "Psalms 88:1"]
},
"hemath": {
    "term": "Hemath",
    "category": "places",
    "intro": "<p>Hemath is an alternative spelling of Hamath, the major Aramean city on the Orontes River in central Syria. In 1 Chronicles 2:55 \"the house of Rechab\" is connected with Hemath, suggesting a settlement in or near the city. Amos 6:14 uses the phrase \"from the entering of Hamath\" to describe the full northern extent of Israel's territory. The \"entering in of Hamath\" (Num. 34:8; Josh. 13:5) designated the traditional northern boundary of the land promised to Israel. Hamath itself was a powerful Aramean kingdom whose king Tou sent congratulatory gifts to David after his defeat of Hadarezer (2 Sam. 8:9–10).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hemath"},
    "key_refs": ["Amos 6:14", "Numbers 34:8", "1 Chronicles 2:55"]
},
"hemlock": {
    "term": "Hemlock",
    "category": "concepts",
    "intro": "<p>The Hebrew word <em>rōsh</em>, rendered \"hemlock\" in Hosea 10:4 and Amos 6:12, is more commonly translated \"gall\" or \"poison.\" It refers to a bitter, poisonous plant — possibly the colocynth, henbane, or some other toxic herb — and is used metaphorically for bitter injustice. Amos asks, \"Shall horses run upon the rock? will one plow there with oxen? for ye have turned judgment into gall, and the fruit of righteousness into hemlock\" (Amos 6:12). Hosea similarly uses it for the poisonous growth of injustice in the courts (Hos. 10:4). The same word is rendered \"gall\" in Deuteronomy 29:18 and Lamentations 3:19, where it describes extreme bitterness. Whether the word refers specifically to hemlock (<em>Conium maculatum</em>) or another toxic plant is uncertain.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hemlock"},
    "key_refs": ["Hosea 10:4", "Amos 6:12", "Deuteronomy 29:18"]
},
"hen": {
    "term": "Hen",
    "category": "names",
    "intro": "<p>Hen (meaning <em>grace; quiet; rest</em>) was the son of Zephaniah, mentioned in Zechariah 6:14 as one of those in whose honor (or under whose name) the symbolic crown made from silver and gold was to be kept as a memorial in the temple. He may be the same as Josiah son of Zephaniah mentioned in Zechariah 6:10 — Hen being a kindly alternate name (meaning \"gracious one\"). Beyond this single mention, nothing else is known of him. The domestic bird (hen) is mentioned by Jesus in his lament over Jerusalem: \"How often would I have gathered thy children together, even as a hen gathereth her chickens under her wings\" (Matt. 23:37).</p>",
    "hitchcock_meaning": "grace; quiet; rest",
    "source_ids": {"easton": "hen"},
    "key_refs": ["Zechariah 6:14", "Matthew 23:37"]
},
"hena": {
    "term": "Hena",
    "category": "places",
    "intro": "<p>Hena was a city mentioned by the Assyrian Rabshakeh in his boast to Hezekiah: \"Where are the gods of Hamath and Arpad? where are the gods of Sepharvaim, Hena, and Ivah?\" (2 Kings 18:34; 19:13; Isa. 37:13). The rhetorical question listed cities the Assyrians had already conquered — implying that Jerusalem's God could not save the city any more than the gods of Hena had saved it. The location of Hena is uncertain; some identify it with Ana or Hit on the Euphrates. The passage emphasizes Sennacherib's contemptuous challenge to the LORD, which was answered by the angel's slaying of 185,000 Assyrian troops (2 Kings 19:35).</p>",
    "hitchcock_meaning": "troubling",
    "source_ids": {"easton": "hena"},
    "key_refs": ["2 Kings 18:34", "Isaiah 37:13"]
},
"henadad": {
    "term": "Henadad",
    "category": "names",
    "intro": "<p>Henadad (meaning <em>grace of the beloved</em> or <em>grace of Hadad</em>) was the head of a family of Levites whose descendants helped Zerubbabel with the rebuilding of the temple after the return from Babylon (Ezra 3:9) and later helped Nehemiah rebuild the wall of Jerusalem (Neh. 3:18, 24; 10:9). The name contains the theophoric element Hadad, the Aramean storm deity, reflecting the hybrid naming patterns common among Israelites with connections to the wider Semitic world. Members of this family held positions of responsibility in both the temple reconstruction and the covenant renewal under Nehemiah.</p>",
    "hitchcock_meaning": "grace of the beloved",
    "source_ids": {"easton": "henadad"},
    "key_refs": ["Ezra 3:9", "Nehemiah 3:18"]
},
"henoch": {
    "term": "Henoch",
    "category": "names",
    "intro": "<p>Henoch is a variant transliteration of the name Enoch, appearing in 1 Chronicles 1:3 in the genealogy from Adam through the pre-flood patriarchs. (Also appears as a son of Midian in Gen. 25:4 / 1 Chr. 1:33.) The primary Enoch (Gen. 5:18–24) was the seventh from Adam, father of Methuselah, who \"walked with God\" and was taken by God without dying — a unique testimony preserved as a model of faith in Hebrews 11:5. The name is rendered Henoch in some older English traditions following the Latin Vulgate.</p>",
    "hitchcock_meaning": "same as Enoch",
    "source_ids": {"easton": "henoch"},
    "key_refs": ["1 Chronicles 1:3", "Genesis 5:24", "Hebrews 11:5"]
},
"hepher": {
    "term": "Hepher",
    "category": "names",
    "intro": "<p>Hepher (meaning <em>a digger</em>) appears as both a personal name and a place name. (1.) The third son of Gilead and founder of the Hepherite clan within the half-tribe of Manasseh (Num. 26:32; 27:1; Josh. 17:2–3). His son Zelophehad had only daughters, whose case led to the legislation on female inheritance in Numbers 27. (2.) A town in the Shephelah of Canaan whose king Joshua defeated (Josh. 12:17), later in Solomon's twelfth administrative district (1 Kings 4:10). (3.) A son of Ashhur, father of Tekoa (1 Chr. 4:6). (4.) One of David's mighty men (1 Chr. 11:36).</p>",
    "hitchcock_meaning": "a digger",
    "source_ids": {"easton": "hepher"},
    "key_refs": ["Numbers 26:32", "Numbers 27:1", "Joshua 12:17"]
},
"hephzibah": {
    "term": "Hephzibah",
    "category": "names",
    "intro": "<p>Hephzibah (meaning <em>my delight is in her</em>) appears in two contexts. (1.) The wife of King Hezekiah of Judah and mother of his son Manasseh, who succeeded him on the throne (2 Kings 21:1). She is one of the few queens of Judah mentioned by name in the regnal records. (2.) A symbolic name given to Zion in Isaiah's prophecy of eschatological restoration: \"Thou shalt no more be termed Forsaken; neither shall thy land any more be termed Desolate: but thou shalt be called Hephzibah, and thy land Beulah: for the LORD delighteth in thee\" (Isa. 62:4). The name thus expresses God's delight in his renewed people and land, the reversal of the desolation of exile.</p>",
    "hitchcock_meaning": "my delight is in her",
    "source_ids": {"easton": "hephzibah"},
    "key_refs": ["2 Kings 21:1", "Isaiah 62:4"]
},
"herb": {
    "term": "Herb",
    "category": "concepts",
    "intro": "<p>Herbs in the Bible include both food plants and aromatic or medicinal plants. At creation, God gave \"every herb bearing seed\" as food for humans and animals (Gen. 1:29–30). Bitter herbs (<em>mĕrōrîm</em>) were prescribed as part of the Passover meal (Ex. 12:8; Num. 9:11), traditionally interpreted as representing the bitterness of Egyptian slavery; rabbinic tradition identified them as lettuce, chicory, or horseradish. Garden herbs — mint, anise (dill), and cumin — are mentioned by Jesus when he rebukes the Pharisees' meticulous tithing of kitchen herbs while neglecting justice and mercy (Matt. 23:23; Luke 11:42). The \"herb of the field\" broadly represents the ordinary produce on which human life depends (Gen. 3:18).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herb"},
    "key_refs": ["Genesis 1:29", "Exodus 12:8", "Matthew 23:23"]
},
"herd": {
    "term": "Herd",
    "category": "concepts",
    "intro": "<p>Herds of cattle (Hebrew <em>bāqār</em>) were a primary measure of wealth in ancient Israel, along with flocks of sheep and goats. Abraham, Isaac, Jacob, and Job are all described as wealthy in part by the size of their herds. Cattle herds provided meat, milk, hides, and labor (plowing, threshing). The law specified distinctions between sacrificial animals from the herd (bulls and cows) and from the flock (sheep and goats), with herd animals typically associated with more costly peace offerings and burnt offerings (Lev. 1:3; 3:1). The famous parable context in Luke 15:23 — the fatted calf killed to celebrate the prodigal son's return — assumes that cattle-keeping was part of a prosperous household's economy.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herd"},
    "key_refs": ["Genesis 12:16", "Leviticus 1:3", "Luke 15:23"]
},
"herdsman": {
    "term": "Herdsman",
    "category": "concepts",
    "intro": "<p>A herdsman was one who tended cattle or large livestock, distinguished from a shepherd who kept flocks of sheep and goats. The occupation is ancient and honored in the biblical world: the patriarchs and their sons were herdsmen (Gen. 13:7–8), and David was called from tending his father's flock to be king (1 Sam. 16:11). The prophet Amos identified himself as \"a herdsman and a gatherer of sycamore fruit\" (Amos 7:14) — a man of no prophetic lineage or school, called directly by God. The Egyptians famously viewed shepherds as an abomination (Gen. 46:34), yet the Israelites were settled in Goshen specifically because of their skill with livestock. Herdsmen often represented a simpler, rural way of life in contrast to city dwellers.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herdsman"},
    "key_refs": ["Genesis 13:7", "Amos 7:14", "1 Samuel 16:11"]
},
"heres": {
    "term": "Heres",
    "category": "places",
    "intro": "<p>Heres (meaning <em>the sun</em> or <em>an earthen pot</em>) appears in a few biblical contexts. (1.) Har-heres, the \"Mount of the Sun,\" was a site in the territory of Dan that the Danites failed to take from the Amorites (Judg. 1:35). It is perhaps the same as Beth-shemesh. (2.) Timnath-heres (Judg. 2:9) or Timnath-serah (Josh. 19:50; 24:30) was the city given to Joshua as his inheritance in the hill country of Ephraim, where he was buried. (3.) The \"ascent of Heres\" is mentioned in Judges 8:13 in the account of Gideon's pursuit of the Midianite kings.</p>",
    "hitchcock_meaning": "the son; an earthen pot",
    "source_ids": {"easton": "heres"},
    "key_refs": ["Judges 1:35", "Judges 2:9", "Judges 8:13"]
},
"heresy": {
    "term": "Heresy",
    "category": "concepts",
    "intro": "<p>Heresy (Greek <em>hairesis</em>, literally <em>a choice</em> or <em>a sect</em>) appears in the New Testament with a range of meaning. In Acts it refers neutrally to a sect or party — the Pharisees, Sadducees, and even the early Christians are called a <em>hairesis</em> (Acts 5:17; 15:5; 24:5, 14; 26:5; 28:22) without necessary pejorative connotation. In Paul and Peter it takes on its later negative sense: factions within the church that create divisions (1 Cor. 11:19; Gal. 5:20), and specifically destructive false teachings brought in by false teachers who deny the Master who bought them (2 Pet. 2:1). Titus 3:10 prescribes rejecting a \"heretic\" (factious person) after two warnings. The developed theological meaning — a teaching that contradicts essential Christian doctrine — grew from this NT usage into the patristic controversies over Christology and the Trinity.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "heresy"},
    "key_refs": ["Acts 24:14", "2 Peter 2:1", "Titus 3:10", "Galatians 5:20"]
},
"hermas": {
    "term": "Hermas",
    "category": "names",
    "intro": "<p>Hermas was a Christian at Rome to whom Paul sends greetings in Romans 16:14: \"Salute Asyncritus, Phlegon, Hermas, Patrobas, Hermes, and the brethren which are with them.\" The name is a shortened form of several Greek names compounded with Hermes (the Greek deity). Some ancient writers proposed that this Hermas was the author of the early Christian writing known as <em>The Shepherd of Hermas</em>, a popular 2nd-century apocalyptic text, but this identification is uncertain and most scholars consider the author of <em>The Shepherd</em> to be a later figure. Nothing else is known of this Hermas from Scripture.</p>",
    "hitchcock_meaning": "Mercury; gain; refuge",
    "source_ids": {"easton": "hermas"},
    "key_refs": ["Romans 16:14"]
},
"hermes": {
    "term": "Hermes",
    "category": "names",
    "intro": "<p>Hermes was a Roman Christian greeted by Paul in Romans 16:14, listed alongside Asyncritus, Phlegon, Hermas, and Patrobas. The name is that of the Greek messenger deity (Roman Mercury), commonly borne by slaves and freedmen in the Greco-Roman world, suggesting he may have been of that social background. He is distinct from the deity Hermes/Mercury, whom the Lystrans called Barnabas and Paul when they performed a miracle (Acts 14:12), calling Paul \"Hermes\" because he was the chief speaker. Nothing further about this Roman believer is recorded.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hermes"},
    "key_refs": ["Romans 16:14", "Acts 14:12"]
},
"hermogenes": {
    "term": "Hermogenes",
    "category": "names",
    "intro": "<p>Hermogenes (meaning <em>begotten of Mercury</em> or <em>born of Hermes</em>) was one of the Asian Christians who deserted Paul during his final imprisonment, mentioned alongside Phygelus: \"This thou knowest, that all they which are in Asia be turned away from me; of whom are Phygellus and Hermogenes\" (2 Tim. 1:15). The desertion was probably connected with the dangers of associating with Paul at his Roman trial, when many feared the consequences of standing with him. Paul contrasts their defection with the loyalty of Onesiphorus, who searched for Paul in Rome and was not ashamed of his chains (2 Tim. 1:16–18).</p>",
    "hitchcock_meaning": "begotten of Mercury",
    "source_ids": {"easton": "hermogenes"},
    "key_refs": ["2 Timothy 1:15"]
},
"hermon": {
    "term": "Hermon",
    "category": "places",
    "intro": "<p>Hermon (meaning <em>anathema; devoted to destruction</em>, or possibly from a root meaning <em>sacred</em>) is the majestic peak at the southwestern end of the Anti-Lebanon range, rising to approximately 9,200 feet above sea level — the highest point in the Levant. It marks the northern boundary of the territory taken from the Amorites and assigned to Israel (Deut. 3:8; Josh. 11:3, 17). The Sidonians called it Sirion, the Amorites called it Shenir (Deut. 3:9). Its snowfields feed the headwaters of the Jordan River, and the dew of Hermon is proverbial for refreshment (Ps. 133:3). The transfiguration of Jesus is traditionally placed on a high mountain that many identify with Hermon, though Tabor is the more ancient tradition (Matt. 17:1). Psalm 89:12 invokes Hermon alongside Tabor as landmarks of God's creative power.</p>",
    "hitchcock_meaning": "anathema; devoted to destruction",
    "source_ids": {"easton": "hermon", "smith": "hermon", "isbe": "hermon"},
    "key_refs": ["Deuteronomy 3:8", "Psalms 133:3", "Psalms 89:12"]
},
"hermonites-the": {
    "term": "Hermonites, the",
    "category": "names",
    "intro": "<p>The Hermonites is a poetic plural form referring to Mount Hermon's multiple peaks or aspects, used in Psalm 42:6 in the lament of a Levite in exile who remembers God \"from the land of Jordan, and of the Hermonites, from the hill Mizar.\" The plural suggests the writer looked upon Hermon's massif from the northeastern Jordan valley, perhaps from the territory of Dan or the Golan, and used the memory of this holy landscape as a touchstone for longing after God's presence at the Jerusalem sanctuary.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hermonites-the"},
    "key_refs": ["Psalms 42:6"]
},
"herod-agrippa-i": {
    "term": "Herod Agrippa I",
    "category": "people",
    "intro": "<p>Herod Agrippa I (born c. 10 B.C., died 44 A.D.) was the grandson of Herod the Great and the last king to rule over all of Judea as a united kingdom. Educated in Rome, he cultivated relationships with the imperial family and was eventually given the territories of his uncles Philip and Antipas, and finally Judea and Samaria as well, reigning from 41–44 A.D. To curry favor with Jewish religious leaders, he executed the apostle James the son of Zebedee and imprisoned Peter (Acts 12:1–3). His sudden and gruesome death — struck down by an angel of God and eaten by worms after accepting divine honors at Caesarea (Acts 12:20–23) — is recorded in both Acts and by Josephus (<em>Antiquities</em> 19.8.2). His death ended the brief restoration of the Herodian kingdom and Judea reverted to direct Roman provincial rule.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-agrippa-i", "smith": "herod-agrippa-i"},
    "key_refs": ["Acts 12:1", "Acts 12:21", "Acts 12:23"]
},
"herod-antipas": {
    "term": "Herod Antipas",
    "category": "people",
    "intro": "<p>Herod Antipas (died after 39 A.D.) was the son of Herod the Great by Malthace, who received the tetrarchy of Galilee and Perea after his father's death (Matt. 14:1; Luke 3:1). He is the Herod most prominent in the Gospels: he divorced his first wife to marry Herodias, his niece and sister-in-law (wife of his half-brother Philip), an action that John the Baptist condemned (Matt. 14:3–4; Mark 6:17–18; Luke 3:19). Herodias' daughter Salome danced at his birthday feast; Antipas' rash oath led to John's beheading (Matt. 14:6–11). Jesus called him \"that fox\" (Luke 13:32). Pilate sent Jesus to Antipas during the trial since Jesus was a Galilean; Antipas mocked him but found no fault (Luke 23:7–12). He was eventually banished to Gaul by the emperor Caligula.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-antipas", "smith": "herod-antipas"},
    "key_refs": ["Matthew 14:1", "Matthew 14:10", "Luke 13:32", "Luke 23:8"]
},
"herod-archelaus": {
    "term": "Herod Archelaus",
    "category": "people",
    "intro": "<p>Herod Archelaus was a son of Herod the Great by Malthace (brother of Antipas) who was appointed ethnarch of Judea, Samaria, and Idumea after his father's death in 4 B.C., though denied the title of king. His brutal and incompetent rule was so oppressive that both Jews and Samaritans petitioned Rome against him; Augustus banished him to Gaul in 6 A.D. He is mentioned only once in the Gospels: when Joseph, returning from Egypt with the child Jesus, heard that Archelaus was ruling Judea in his father Herod's place, he was afraid to go there and was divinely warned to settle in Galilee instead (Matt. 2:22).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-archelaus"},
    "key_refs": ["Matthew 2:22"]
},
"herod-arippa-ii": {
    "term": "Herod Agrippa II",
    "category": "people",
    "intro": "<p>Herod Agrippa II (born c. 27 A.D., died c. 100 A.D.) was the son of Herod Agrippa I and the last of the Herodian dynasty to hold a significant role in Jewish affairs. He ruled over the former tetrarchies of Philip and Lysanias in the north. He is known in the New Testament for the hearing he conducted with the Roman governor Festus regarding Paul's appeal to Caesar (Acts 25:13–26:32). Paul's eloquent defense before Agrippa culminated in Agrippa's famous remark: \"Almost thou persuadest me to be a Christian\" (Acts 26:28). Agrippa's judgment, shared with Festus, was that Paul had done nothing deserving death or imprisonment — had he not appealed to Caesar, he could have been set free (Acts 26:32).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-arippa-ii"},
    "key_refs": ["Acts 25:13", "Acts 26:28", "Acts 26:32"]
},
"herod-philip-i": {
    "term": "Herod Philip I",
    "category": "people",
    "intro": "<p>Herod Philip I was a son of Herod the Great and Mariamne II (daughter of the high priest Simon). He lived as a private citizen in Rome, having been disinherited by his father. His wife Herodias left him for his half-brother Antipas. Mark 6:17 identifies him as the husband from whom Herodias was taken. He is to be distinguished from Philip the Tetrarch (Philip II), a different half-brother who ruled the northeastern territories. Philip I appears in no other Gospel narrative and plays no political role in the history of the period.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-philip-i"},
    "key_refs": ["Mark 6:17"]
},
"herod-philip-ii": {
    "term": "Herod Philip II",
    "category": "people",
    "intro": "<p>Herod Philip II was a son of Herod the Great and Cleopatra of Jerusalem, appointed tetrarch of Batanea, Iturea, Trachonitis, and Auranitis — the northeastern territories (Luke 3:1). He rebuilt and enlarged the city at Caesarea Philippi (ancient Paneas), renaming it after himself and after Caesar (Matt. 16:13; Mark 8:27). He was regarded by Josephus as the most just of Herod's sons. He married Salome, the daughter of Herodias (the one who danced for Antipas). He died in 34 A.D. without an heir and his territories were absorbed into the province of Syria until Agrippa I received them.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-philip-ii"},
    "key_refs": ["Luke 3:1", "Matthew 16:13"]
},
"herod-the-great": {
    "term": "Herod the Great",
    "category": "people",
    "intro": "<p>Herod the Great (c. 73–4 B.C.) was the king of Judea at the time of Jesus' birth (Matt. 2:1; Luke 1:5), appointed by the Roman Senate as \"king of the Jews\" in 37 B.C. He was the son of Antipater the Idumaean and an Arab mother. Despite his non-Jewish origin, he was a remarkable builder: his projects included the massive expansion of the Jerusalem temple (begun c. 20 B.C., still under construction in John 2:20), the palace-fortress of Masada, the harbor city of Caesarea Maritima, and the Herodion. His reign was marked by political cunning, intense cruelty to rivals (he executed his wife Mariamne I and several sons), and the building projects for which he is remembered. He is infamous in Christian tradition for ordering the massacre of infant boys in Bethlehem in his attempt to eliminate the newborn \"king of the Jews\" (Matt. 2:16–18), fulfilling Jeremiah's prophecy of Rachel weeping for her children. He died shortly after this event, around 4 B.C.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herod-the-great", "smith": "herod-the-great", "isbe": "herod-the-great"},
    "key_refs": ["Matthew 2:1", "Matthew 2:16", "Luke 1:5", "John 2:20"]
},
"herodians": {
    "term": "Herodians",
    "category": "people",
    "intro": "<p>The Herodians were a Jewish political party who supported the Herodian dynasty's continued rule over Palestine and the accommodation to Roman imperial power that it represented. Though not a religious sect, they aligned with the Pharisees on at least one occasion in their shared opposition to Jesus: after Jesus healed the withered hand on the Sabbath, the Pharisees and Herodians conspired to destroy him (Mark 3:6). They were sent together to trap Jesus with the question about paying taxes to Caesar (Mark 12:13–17; Matt. 22:16), which Jesus famously deflected with \"Render to Caesar the things that are Caesar's.\" Jesus warned his disciples against \"the leaven of Herod\" (Mark 8:15) alongside the leaven of the Pharisees, suggesting a corrupting political influence.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herodians", "smith": "herodians"},
    "key_refs": ["Mark 3:6", "Mark 12:13", "Matthew 22:16"]
},
"herodias": {
    "term": "Herodias",
    "category": "people",
    "intro": "<p>Herodias was a granddaughter of Herod the Great and daughter of Aristobulus and Bernice. She married first her half-uncle Herod Philip I and had a daughter, Salome, by him. She then left Philip to marry his half-brother Herod Antipas, the tetrarch of Galilee and Perea. John the Baptist rebuked this marriage as unlawful (Lev. 18:16; 20:21; Matt. 14:3–4; Mark 6:17–18), and Herodias harbored a grudge against John and wanted to kill him, but Antipas feared the people and kept John in prison instead. When Antipas swore to give Salome whatever she asked after her dance at his birthday banquet, Herodias instructed her daughter to request the head of John the Baptist on a plate (Matt. 14:6–11; Mark 6:21–28), and Antipas complied. Herodias eventually went with Antipas into exile in Gaul.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "herodias", "smith": "herodias"},
    "key_refs": ["Matthew 14:3", "Mark 6:19", "Mark 6:24"]
},
"herodion": {
    "term": "Herodion",
    "category": "names",
    "intro": "<p>Herodion (meaning <em>the song of Juno</em>, or simply a name related to Herod) was a Roman Christian whom Paul greets in Romans 16:11 and identifies as \"my kinsman\" — likely a fellow Jew, as Paul uses <em>syngenēs</em> (kinsman) for Jewish believers. Whether \"kinsman\" means a blood relative or a fellow Israelite, the term expresses special closeness. Herodion's name suggests a connection to the Herodian household, and Paul mentions greetings to those \"of the household of Narcissus\" in the same passage — household names often indicate slaves or freedmen of prominent Roman families.</p>",
    "hitchcock_meaning": "the song of Juno",
    "source_ids": {"easton": "herodion"},
    "key_refs": ["Romans 16:11"]
},
"heron": {
    "term": "Heron",
    "category": "concepts",
    "intro": "<p>The heron is listed among the unclean birds in the Mosaic dietary law (Lev. 11:19; Deut. 14:18). The Hebrew name <em>'anāphāh</em> appears to indicate an irritable or angry bird — possibly connected to a root meaning \"to snort\" or \"be angry.\" The identification with the heron (<em>Ardea cinerea</em>) is traditional and plausible given the bird's prominence in the wetlands of Palestine. Several species of heron, stork, and egret are native to the Jordan Valley and the coastal marshes. All such large wading birds that feed on fish and frogs were classed as unclean.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "heron"},
    "key_refs": ["Leviticus 11:19", "Deuteronomy 14:18"]
},
"heshbon": {
    "term": "Heshbon",
    "category": "places",
    "intro": "<p>Heshbon (meaning <em>invention; industry</em>) was the royal city of Sihon, king of the Amorites, east of the Jordan River. When Israel requested passage through Sihon's territory and he refused, Moses led Israel against him and defeated the Amorites at Jahaz, capturing Heshbon and all its cities (Num. 21:21–26). The city was subsequently assigned to the tribe of Reuben (Num. 32:37) and later to Gad, and designated a Levitical city (Josh. 21:39). The Song of Solomon invokes the \"pools of Heshbon by the gate of Bath-rabbim\" (Song 7:4) as an image of beauty. By Jeremiah's time Heshbon had come under Moabite control and was an object of prophetic lament (Jer. 48:2, 34, 45; 49:3). The site is identified with modern Tell Hesbān, where excavations have revealed occupation from the Iron Age through the Islamic period.</p>",
    "hitchcock_meaning": "invention; industry",
    "source_ids": {"easton": "heshbon", "smith": "heshbon"},
    "key_refs": ["Numbers 21:26", "Numbers 32:37", "Song of Solomon 7:4"]
},
"heshmon": {
    "term": "Heshmon",
    "category": "places",
    "intro": "<p>Heshmon (meaning <em>a hasty messenger</em>) was a town in the southernmost part of Judah's allotment, near the Negev border, listed among the towns in Joshua 15:27. It appears alongside Hazargaddah and Moladah in the southern district of Judah. The site has not been positively identified among known archaeological locations, and the town plays no further role in biblical narrative beyond this allotment list.</p>",
    "hitchcock_meaning": "a hasty messenger",
    "source_ids": {"easton": "heshmon"},
    "key_refs": ["Joshua 15:27"]
},
"heth": {
    "term": "Heth",
    "category": "people",
    "intro": "<p>Heth (meaning <em>trembling; fear</em>) was the second son of Canaan and grandson of Noah (Gen. 10:15; 1 Chr. 1:13), ancestor of the Hittites. The \"sons of Heth\" (<em>bĕnê-ḥēt</em>) is used interchangeably with \"Hittites\" in the patriarchal narratives: Abraham purchased the cave of Machpelah from Ephron the Hittite, a son of Heth, to bury Sarah (Gen. 23:3–20). Esau's marriages to Hittite women grieved his parents Isaac and Rebekah (Gen. 26:34–35; 27:46). The biblical Hittites (sons of Heth) are not always identical to the great Hittite empire of Anatolia; some scholars distinguish the Syro-Palestinian Hittites as a separate entity, possibly descendants of Heth as a Canaanite tribal ancestor.</p>",
    "hitchcock_meaning": "trembling; fear",
    "source_ids": {"easton": "heth"},
    "key_refs": ["Genesis 10:15", "Genesis 23:3", "Genesis 23:20"]
},
"hethlon": {
    "term": "Hethlon",
    "category": "places",
    "intro": "<p>Hethlon (meaning <em>a fearful dwelling</em>) was a location on the ideal northern boundary of Israel described in Ezekiel's vision of the restored land: \"From the great sea, the way of Hethlon, as men go to Zedad; Hamath, Berothah, Sibraim...\" (Ezek. 47:15; 48:1). The same location appears in Numbers 34:8 as \"Hazar-enan\" in the boundary list. Hethlon has been tentatively identified with Heitela, a village north of Damascus on the road from the coast to Hamath, but certainty is elusive. It marks the northwestern approach to the traditional northern border of Canaan.</p>",
    "hitchcock_meaning": "a fearful dwelling",
    "source_ids": {"easton": "hethlon"},
    "key_refs": ["Ezekiel 47:15", "Ezekiel 48:1"]
},
"hezekiah": {
    "term": "Hezekiah",
    "category": "people",
    "intro": "<p>Hezekiah (meaning <em>strength of the LORD</em> or <em>whom Jehovah has strengthened</em>) was the son of Ahaz and one of the most celebrated kings of Judah, reigning approximately 715–686 B.C. (2 Kings 18–20; 2 Chr. 29–32; Isa. 36–39). The biblical account gives him one of the highest commendations among David's successors: \"He trusted in the LORD God of Israel; so that after him was none like him among all the kings of Judah, nor any that were before him\" (2 Kings 18:5). His major achievements included a thoroughgoing religious reformation — reopening and cleansing the temple, destroying the bronze serpent Nehushtan (which had become an idol), and abolishing the high places and Asherah poles. He successfully defended Jerusalem against Sennacherib's Assyrian siege in 701 B.C. through a combination of his engineering feat (the Siloam Tunnel), desperate prayer (Isa. 37:14–20), and divine intervention (the angel slaying 185,000 Assyrian troops, 2 Kings 19:35). His life was extended fifteen years after a terminal illness when he prayed and God answered through Isaiah (2 Kings 20:1–11; Isa. 38). He also entertained Babylonian envoys whose visit prompted Isaiah's prophecy of eventual Babylonian exile (Isa. 39).</p>",
    "hitchcock_meaning": "strength of the Lord",
    "source_ids": {"easton": "hezekiah", "smith": "hezekiah", "isbe": "hezekiah"},
    "key_refs": ["2 Kings 18:5", "2 Kings 19:35", "2 Kings 20:6", "Isaiah 37:14"]
},
"hezion": {
    "term": "Hezion",
    "category": "names",
    "intro": "<p>Hezion was the grandfather of Ben-hadad I, king of Damascus (Syria), mentioned in 1 Kings 15:18. He was the founder of the Ben-hadad dynasty of Aramean kings. When Asa king of Judah bribed Ben-hadad of Damascus with the temple treasury silver and gold to break his treaty with Baasha of Israel and attack the north, Ben-hadad is identified as \"the son of Tabrimmon, the son of Hezion, king of Syria, that dwelt at Damascus.\" Hezion appears only in this genealogical reference; nothing else is recorded of him in Scripture.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hezion"},
    "key_refs": ["1 Kings 15:18"]
},
"hezir": {
    "term": "Hezir",
    "category": "names",
    "intro": "<p>Hezir (meaning <em>swine</em> or <em>strong</em>) is the name of two men in the Old Testament. (1.) The head of the seventeenth priestly course in David's organization of temple worship (1 Chr. 24:15). (2.) One of the chiefs of the people who set his seal to the covenant of national renewal in Nehemiah's time (Neh. 10:20). Both names reflect the continuity of priestly and lay leadership across the pre-exilic and post-exilic periods of Israel's history.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hezir"},
    "key_refs": ["1 Chronicles 24:15", "Nehemiah 10:20"]
},
"hezro": {
    "term": "Hezro",
    "category": "names",
    "intro": "<p>Hezro (also spelled Hezrai) was a Carmelite — from Carmel in the Judean hill country — who was one of David's thirty mighty men (2 Sam. 23:35; 1 Chr. 11:37). He is listed in the elite corps of warriors who served David with extraordinary valor. Beyond this inclusion in the roster of the Thirty, no individual exploits are recorded for Hezro in the biblical text.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hezro"},
    "key_refs": ["2 Samuel 23:35", "1 Chronicles 11:37"]
},
"hezron": {
    "term": "Hezron",
    "category": "names",
    "intro": "<p>Hezron (meaning <em>the dart of joy; the division of the song</em>) is the name of two important figures in the genealogies. (1.) The third son of Reuben (Gen. 46:9; Ex. 6:14) and head of the Hezronite family in that tribe. (2.) The older son of Pharez (son of Judah and Tamar), and a critical link in the Messianic genealogy: Hezron of Judah is listed as an ancestor of David (Ruth 4:18–19; 1 Chr. 2:5, 9) and consequently of Jesus Christ (Matt. 1:3; Luke 3:33). His descendants through Ram/Aram included Amminadab, Nahshon, and ultimately David, making Hezron an important figure in the royal and messianic lineage. Also a place name: Hazor-Hezron (Josh. 15:25) is a town in southern Judah.</p>",
    "hitchcock_meaning": "the dart of joy; the division of the song",
    "source_ids": {"easton": "hezron"},
    "key_refs": ["Genesis 46:12", "Ruth 4:18", "Matthew 1:3"]
},
"hiddai": {
    "term": "Hiddai",
    "category": "names",
    "intro": "<p>Hiddai (meaning <em>a praise; a cry</em>) was a warrior from the brooks of Gaash in Ephraim, one of David's thirty mighty men (2 Sam. 23:30). In the parallel passage in 1 Chronicles 11:32 he is called Hurai. He belonged to the elite corps of warriors who distinguished themselves in David's service. The brooks of Gaash, near the hill of Gaash in the Ephraim highlands, is also associated with Joshua, who was buried \"in the border of his inheritance in Timnath-serah... on the north side of the hill of Gaash\" (Josh. 24:30).</p>",
    "hitchcock_meaning": "a praise; a cry",
    "source_ids": {"easton": "hiddai"},
    "key_refs": ["2 Samuel 23:30", "1 Chronicles 11:32"]
},
"hiddekel": {
    "term": "Hiddekel",
    "category": "places",
    "intro": "<p>Hiddekel is the Hebrew name for the Tigris River (Akkadian <em>Idiqlat</em>), the third of the four rivers said to flow from the Garden of Eden (Gen. 2:14). It is described as going \"toward the east of Assyria\" — an accurate geographic description since the Tigris defines the eastern boundary of the Assyrian heartland. The Tigris also appears in Daniel 10:4, where Daniel is standing on its bank when he receives his final vision. At 1,150 miles long, the Tigris is the second-largest river in southwestern Asia after the Euphrates; together they form the alluvial plain of Mesopotamia (modern Iraq) that was the cradle of ancient Babylonian and Assyrian civilization.</p>",
    "hitchcock_meaning": "sharp voice; sound",
    "source_ids": {"easton": "hiddekel"},
    "key_refs": ["Genesis 2:14", "Daniel 10:4"]
},
"hiel": {
    "term": "Hiel",
    "category": "names",
    "intro": "<p>Hiel (meaning <em>God lives; the life of God</em>) was a man of Bethel who rebuilt and refortified Jericho during the reign of Ahab king of Israel (1 Kings 16:34). Joshua had pronounced a curse on anyone who rebuilt Jericho (Josh. 6:26): \"Cursed be the man before the LORD that riseth up and buildeth this city Jericho: he shall lay the foundation thereof in his firstborn, and in his youngest son shall he set up the gates of it.\" This curse was fulfilled in Hiel: when he laid the foundation, his firstborn Abiram died; when he set up the gates, his youngest son Segub died. The incident is presented as a sobering confirmation that Joshua's word, inspired by God, remained in force across the centuries.</p>",
    "hitchcock_meaning": "God lives; the life of God",
    "source_ids": {"easton": "hiel"},
    "key_refs": ["1 Kings 16:34", "Joshua 6:26"]
},
"hierapolis": {
    "term": "Hierapolis",
    "category": "places",
    "intro": "<p>Hierapolis (meaning <em>holy city</em>) was a city in the Lycus River valley of Phrygia (modern western Turkey), located about six miles north of Laodicea and twelve miles from Colossae. It had a Christian congregation under the pastoral care of Epaphras, whom Paul commends as \"always labouring fervently for you in prayers\" (Col. 4:12–13). The three cities — Colossae, Laodicea, and Hierapolis — formed a cluster of churches in the Lycus valley. Hierapolis was famous for its hot springs whose mineral-rich waters cascaded over the cliff at Pamukkale, creating white terraces still visible today; Revelation's rebuke of Laodicea for being \"lukewarm\" (Rev. 3:16) may allude to this geothermal context. Church tradition says Philip the Apostle died and was buried at Hierapolis.</p>",
    "hitchcock_meaning": "holy city",
    "source_ids": {"easton": "hierapolis"},
    "key_refs": ["Colossians 4:13"]
},
"higgaion": {
    "term": "Higgaion",
    "category": "concepts",
    "intro": "<p>Higgaion is a musical or liturgical term appearing in the superscription or text of three psalms. In Psalm 92:3 it denotes the \"murmuring tone\" or meditative sound of the harp. In Psalm 9:16 it appears alongside <em>Selah</em> as a performance direction, possibly indicating a pause for meditation or a dramatic interlude in the instrumental music. In Psalm 19:14 it is used for \"meditation\" in the phrase \"let... the meditation of my heart be acceptable in thy sight.\" The exact nature of the musical instruction has been lost; interpretations range from a particular melody to a sign indicating contemplative playing. The root <em>hāgāh</em> means to murmur, muse, or meditate.</p>",
    "hitchcock_meaning": "meditation; consideration",
    "source_ids": {"easton": "higgaion"},
    "key_refs": ["Psalms 9:16", "Psalms 19:14", "Psalms 92:3"]
},
"high-place": {
    "term": "High Place",
    "category": "concepts",
    "intro": "<p>A high place (Hebrew <em>bāmāh</em>, plural <em>bāmôt</em>) was an elevated site — natural hilltop or artificial platform — used for religious sacrifice and worship. Before the Jerusalem temple, sacrifice at local high places was tolerated or even practiced by the patriarchs (Gen. 8:20) and Israel (1 Sam. 9:12–14), and Solomon himself sacrificed at Gibeon, \"the great high place\" (1 Kings 3:4). After the temple was built, the persistent use of high places by the people of both kingdoms became a primary source of prophetic condemnation. The reforming kings Hezekiah and Josiah are distinguished by their destruction of the high places (2 Kings 18:4; 23:5–20). The high places were associated with the Asherah poles, standing stones, and incense altars of Canaanite religion, and their use represented syncretism between Yahwism and the fertility cults of Canaan.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "high-place", "smith": "high-place", "isbe": "high-place"},
    "key_refs": ["1 Kings 3:4", "2 Kings 18:4", "2 Kings 23:8", "Ezekiel 20:29"]
},
"high-priest": {
    "term": "High Priest",
    "category": "concepts",
    "intro": "<p>The high priest (Hebrew <em>kōhēn haggādôl</em>, \"the great priest\") was the supreme religious official of Israel under the Mosaic covenant, holding a unique and irreplaceable role in the sacrificial system and in Israel's covenant relationship with God. Aaron was the first high priest, consecrated with an elaborate ceremony of anointing and investiture (Ex. 29; Lev. 8). The high priest wore distinctive garments including the breastplate of twelve gemstones, the ephod, the blue robe with bells, the mitre, and the golden plate inscribed \"Holy to the LORD.\" He alone entered the Holy of Holies on the annual Day of Atonement to make expiation for Israel's sins by sprinkling blood on the mercy seat (Lev. 16). The office was hereditary through Aaron's son Eleazar and his descendants. In the New Testament, the Epistle to the Hebrews presents Christ as the supreme and final High Priest — \"a priest for ever after the order of Melchizedek\" (Heb. 6:20) — whose one offering of himself has rendered the repeated animal sacrifices permanently obsolete (Heb. 9:11–14; 10:11–14). Caiaphas and Annas held the high-priestly office at the time of Jesus' trial.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "high-priest", "smith": "high-priest", "isbe": "high-priest"},
    "key_refs": ["Leviticus 16:32", "Hebrews 6:20", "Hebrews 9:11", "Matthew 26:57"]
},
"highway": {
    "term": "Highway",
    "category": "concepts",
    "intro": "<p>A highway in the ancient Near East was a raised or established road prepared for public travel — constructed paths elevated above surrounding terrain to allow passage in all seasons. The Hebrew <em>mesillāh</em> (raised road, causeway) appears primarily in poetry and prophecy. The prophetic image of the highway appears powerfully in Isaiah: the highway for the LORD (Isa. 40:3), the \"Way of Holiness\" for the redeemed to travel in the age of salvation (Isa. 35:8), and the highway from Assyria for the scattered to return (Isa. 11:16; 19:23). Isaiah 62:10 commands preparation of the highway for the returning exiles. John the Baptist's ministry fulfills the call to \"prepare ye the way of the LORD, make straight in the desert a highway for our God\" (Isa. 40:3; Matt. 3:3). Roman roads (viae) were among the great engineering achievements of the empire that facilitated the spread of the gospel.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "highway"},
    "key_refs": ["Isaiah 40:3", "Isaiah 35:8", "Matthew 3:3"]
},
"hilkiah": {
    "term": "Hilkiah",
    "category": "people",
    "intro": "<p>Hilkiah (meaning <em>God is my portion</em> or <em>my portion is Jehovah</em>) is most significantly the high priest in the reign of Josiah who discovered the Book of the Law (almost certainly Deuteronomy) while the temple was being repaired (2 Kings 22:8; 2 Chr. 34:14–15). When the book was read to Josiah he tore his clothes in grief, recognizing how far Judah had strayed from the covenant, and sent Hilkiah with others to consult the prophetess Huldah. This discovery triggered the great Josianic reformation — the centralization of worship, the destruction of idols, and the massive Passover observance described in 2 Kings 23. Hilkiah was also the father of Jeremiah the prophet (Jer. 1:1) and father of Eliakim the palace administrator (2 Kings 18:18). Several other men named Hilkiah appear in Chronicles, Nehemiah, and Ezra, reflecting the name's popularity in priestly circles.</p>",
    "hitchcock_meaning": "God is my portion",
    "source_ids": {"easton": "hilkiah", "smith": "hilkiah"},
    "key_refs": ["2 Kings 22:8", "2 Chronicles 34:14", "Jeremiah 1:1"]
},
"hill": {
    "term": "Hill",
    "category": "concepts",
    "intro": "<p>Hills (Hebrew <em>gibeāh</em>, <em>har</em>) are ubiquitous in Palestinian geography and carry rich theological resonances in Scripture. The \"hill of the LORD\" (Ps. 24:3; Isa. 2:2–3) is a title for Mount Zion and the Jerusalem temple, the place of divine encounter. The phrase \"every high hill\" or \"high hills\" often appears in condemnation of idolatrous worship (Jer. 2:20; Ezek. 6:13; Hos. 4:13), since Canaanite fertility religion favored hilltop shrines. The Sermon on the Mount (Matt. 5–7) and the Transfiguration took place on hills. \"A city set on a hill cannot be hid\" (Matt. 5:14) uses the visibility of hilltop settlements as a metaphor for the witnessing vocation of the church. \"The hills melt like wax\" (Ps. 97:5; Mic. 1:4) images divine theophany before which the natural world trembles.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hill"},
    "key_refs": ["Psalms 24:3", "Isaiah 2:2", "Matthew 5:14"]
},
"hill-of-evil-counsel": {
    "term": "Hill of Evil Counsel",
    "category": "places",
    "intro": "<p>The Hill of Evil Counsel is a site on the south side of the Valley of Hinnom, opposite Jerusalem, whose name derives from a tradition preserved in church history: that the house of the high priest Caiaphas stood there, and that it was here that the chief priests and rulers of the Jews resolved to put Jesus to death (Matt. 26:3–5; John 11:47–53). The name thus reflects Christian interpretation of the site rather than an ancient toponym. It commands a prominent view of Jerusalem across the Hinnom Valley. The tradition is preserved in Byzantine and medieval pilgrimage literature and has been associated with the area now known as Jebel Abu Tor, southwest of the Old City. Whether or not Caiaphas's house was actually located there, the name captures the theological significance of the council that condemned the Son of God.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "hill-of-evil-counsel"},
    "key_refs": ["Matthew 26:3", "John 11:47"]
},
}

wrote = 0
skipped = 0
for slug, data in ARTICLES.items():
    article = {
        "id": slug,
        "term": data["term"],
        "category": data["category"],
        "intro": data["intro"],
        "hitchcock_meaning": data.get("hitchcock_meaning"),
        "source_ids": data.get("source_ids", {}),
        "key_refs": data.get("key_refs", []),
        "sections": []
    }
    if merge_article(slug, article):
        wrote += 1
    else:
        skipped += 1

print(f"BP h3: Hebron → Hill of Evil Counsel: wrote {wrote}, skipped {skipped} existing.")
