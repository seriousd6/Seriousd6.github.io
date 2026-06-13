#!/usr/bin/env python3
"""BP G2 — Gibeah → Grecians (75 articles)."""
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
"gibeah": {
    "term": "Gibeah",
    "category": "places",
    "intro": "<p>Gibeah (meaning <em>a hill</em>) was a town in the territory of Benjamin, best known as \"Gibeah of Saul\" — the hometown and base of Israel's first king (1 Sam. 10:26; 11:4; Isa. 10:29). The site is identified with modern Tell el-Ful, approximately three miles north of Jerusalem. Gibeah became infamous earlier in Israelite history for a horrific act of gang violence against a Levite's concubine, an outrage that triggered a civil war in which the tribe of Benjamin was nearly annihilated (Judg. 19–20). Despite this dark legacy, it was Saul's residence and the administrative center of his kingdom. The site has also been identified with \"Gibeah of Judah\" in some interpretations, though that is generally treated as a separate location.</p>",
    "hitchcock_meaning": "a hill",
    "source_ids": {"easton": "gibeah"},
    "key_refs": ["1 Samuel 13:15", "Isaiah 10:29", "Judges 19:12", "1 Samuel 10:26"]
},
"gibeah-of-judah": {
    "term": "Gibeah of Judah",
    "category": "places",
    "intro": "<p>Gibeah of Judah was a hill-town in the territory of Judah, mentioned in connection with the father-in-law of Michal and as an ancestral seat in the hill country. It is distinct from the more prominent Gibeah of Benjamin (Gibeah of Saul) and from Gibeah of Phinehas. The exact identification of the site remains uncertain, but it lay in the Judean highlands. Several passages use the simple designation \"Gibeah\" for towns in this region, requiring contextual reading to distinguish them.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gibeah-of-judah"},
    "key_refs": ["Joshua 15:57"]
},
"gibeah-of-phinehas": {
    "term": "Gibeah of Phinehas",
    "category": "places",
    "intro": "<p>Gibeah of Phinehas was a hill in the territory of Ephraim where Eleazar the son of Aaron was buried. The name derives from Phinehas the priest, son of Eleazar, to whom the hill had been given. After Phinehas died, he was also buried there. The site served as a family burial ground for the priestly line of Aaron in the period of the judges (Josh. 24:33).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gibeah-of-phinehas"},
    "key_refs": ["Joshua 24:33"]
},
"gibeah-haaraloth": {
    "term": "Gibeah-haaraloth",
    "category": "places",
    "intro": "<p>Gibeah-haaraloth (meaning <em>hill of the foreskins</em>) was the place near Gilgal where Joshua circumcised the Israelite males born during the forty years of wilderness wandering. The entire generation that had come out of Egypt had not been circumcised, and before Israel could celebrate the Passover and proceed to battle, the covenant sign had to be restored (Josh. 5:3). The name commemorates this mass circumcision carried out at Gilgal before the campaign in Canaan began.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gibeah-haaraloth"},
    "key_refs": ["Joshua 5:3"]
},
"gibeon": {
    "term": "Gibeon",
    "category": "places",
    "intro": "<p>Gibeon (meaning <em>hill-city</em>) was a major Hivite city northwest of Jerusalem within the territory of Benjamin, described as \"greater than Ai, and all the men thereof were mighty\" (Josh. 10:2). Its inhabitants famously deceived Joshua into making a covenant of peace by pretending to be travelers from a distant country (Josh. 9). The deception was discovered but the covenant was upheld, and the Gibeonites became servants — hewers of wood and drawers of water — for the Israelite community. Gibeon became the site of the tabernacle after the conquest and was important in David's and Solomon's reigns; it was at Gibeon that God appeared to Solomon in a dream and offered him the gift of wisdom (1 Kings 3:5). The miraculous battle at Gibeon, in which Joshua commanded the sun and moon to stand still, was the decisive engagement securing the southern Canaanite coalition's defeat (Josh. 10:12–14).</p>",
    "hitchcock_meaning": "hill; cup; thing lifted up",
    "source_ids": {"easton": "gibeon", "smith": "gibeon", "isbe": "gibeon"},
    "key_refs": ["Joshua 10:2", "Joshua 9:15", "1 Kings 3:5", "2 Samuel 21:1"]
},
"gideon": {
    "term": "Gideon",
    "category": "people",
    "intro": "<p>Gideon (meaning <em>he that bruises or breaks; a destroyer</em>), also called Jerubbaal (\"let Baal contend\"), was the fifth judge of Israel whose history is told in detail in Judges 6–8. Called by the angel of the LORD while threshing wheat in a winepress to hide it from Midianite raiders, Gideon initially protested his insignificance but was commissioned to deliver Israel from seven years of Midianite oppression. He destroyed his father's altar to Baal and the Asherah pole beside it — earning the name Jerubbaal — then assembled an army which God reduced from 32,000 to 300 men to ensure that Israel would not take credit for the victory (Judg. 7:2–8). Through a night attack with torches, trumpets, and clay jars, Gideon's 300 routed the Midianite host. He is commended in Hebrews 11:32 among the heroes of faith. His downfall came in later life when he made an ephod from battle spoils that became an object of idolatry, and his son Abimelech's violent seizure of power brought chaos to Israel after his death.</p>",
    "hitchcock_meaning": "he that bruises or breaks; a destroyer",
    "source_ids": {"easton": "gideon", "smith": "gideon", "isbe": "gideon"},
    "key_refs": ["Judges 6:12", "Judges 7:7", "Judges 8:27", "Hebrews 11:32"]
},
"gier-eagle": {
    "term": "Gier Eagle",
    "category": "concepts",
    "intro": "<p>The gier eagle is listed among the unclean birds in the Mosaic law (Lev. 11:18; Deut. 14:17). The Hebrew word rendered \"gier eagle\" is <em>racham</em>, derived from a root meaning tenderness, possibly because the bird was thought to show affection to its young. Modern scholars generally identify it as the Egyptian vulture (<em>Neophron percnopterus</em>), a scavenging bird common throughout the Near East. Like all birds of prey and scavengers, it was ceremonially unclean for Israel.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gier-eagle"},
    "key_refs": ["Leviticus 11:18", "Deuteronomy 14:17"]
},
"gift": {
    "term": "Gift",
    "category": "concepts",
    "intro": "<p>Gifts in the Bible serve a wide range of social and religious functions. They could be gratuities to secure favor (Prov. 19:6), thank-offerings for divine blessing (Num. 18:11), betrothal payments (Gen. 34:12), or tribute rendered to a superior power (2 Sam. 8:2). In the Mosaic law, the firstfruits and tithes were designated gifts to the LORD through the priesthood. The New Testament distinguishes natural gifts from the charismata — the spiritual gifts bestowed by the Holy Spirit for the edification of the church. The supreme gift of God is Jesus Christ himself: \"the unspeakable gift\" (2 Cor. 9:15), and salvation is described as \"the gift of God\" in contrast to earned wages (Rom. 6:23; Eph. 2:8).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gift"},
    "key_refs": ["Proverbs 19:6", "Numbers 18:11", "Romans 6:23", "2 Corinthians 9:15"]
},
"gifts-spiritual": {
    "term": "Gifts, Spiritual",
    "category": "concepts",
    "intro": "<p>Spiritual gifts (Greek <em>charismata</em>) are supernatural endowments bestowed by the Holy Spirit upon believers for the common good and the edification of the church. In the apostolic period these included gifts of prophecy, tongues, interpretation, healing, miracles, discernment, wisdom, and knowledge (1 Cor. 12; Rom. 12:6–8; Eph. 4:11). They were given sovereignly by the Spirit as he willed (1 Cor. 12:11), not as rewards for merit, and were to be exercised in love (1 Cor. 13). The laying on of apostles' hands was sometimes the occasion for their impartation (Acts 8:17; 19:6). Paul's extended treatment in 1 Corinthians 12–14 addresses both the diversity of gifts and the primacy of love over spectacular manifestations. The gifts are distinguished from the fruit of the Spirit (Gal. 5:22–23), which describes character formation rather than ministry endowments.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gifts-spiritual"},
    "key_refs": ["1 Corinthians 12:4", "Romans 12:6", "Ephesians 4:11", "Acts 8:17"]
},
"gihon": {
    "term": "Gihon",
    "category": "places",
    "intro": "<p>Gihon (meaning <em>valley of grace</em> or <em>bursting forth</em>) refers to two distinct locations in Scripture. (1.) One of the four rivers of Eden (Gen. 2:13), which encompassed the land of Cush. Its identification is disputed — proposed candidates include the Nile, the Araxes, and various other streams, with no scholarly consensus. (2.) A spring on the eastern slope of the hill of Ophel in Jerusalem, in the Kidron Valley. This was the principal water supply for ancient Jerusalem, and it was at this spring that Solomon was anointed king while Adonijah was attempting to seize the throne (1 Kings 1:33–34, 38–45). King Hezekiah later diverted Gihon's waters through the famous Siloam Tunnel (2 Chr. 32:30) to protect the city's water supply during the Assyrian siege — an engineering feat confirmed by the Siloam Inscription discovered in 1880.</p>",
    "hitchcock_meaning": "valley of grace",
    "source_ids": {"easton": "gihon", "smith": "gihon", "isbe": "gihon"},
    "key_refs": ["Genesis 2:13", "1 Kings 1:33", "2 Chronicles 32:30"]
},
"gilboa": {
    "term": "Gilboa",
    "category": "places",
    "intro": "<p>Gilboa (meaning <em>boiling spring</em> or <em>revolution of inquiry</em>) is a mountain range in northern Israel, now called Jebel Fukua', rising on the eastern side of the Jezreel Valley southeast of Jezreel. It is most memorable as the scene of Saul's disastrous defeat by the Philistines in which his three sons Jonathan, Abinadab, and Malchishua were slain, and Saul himself died by his own hand to avoid capture (1 Sam. 28:4; 31:1–6). David's lament over Saul and Jonathan includes the memorable curse: \"Ye mountains of Gilboa, let there be no dew, neither let there be rain upon you\" (2 Sam. 1:21), marking the site as one associated with mourning and shame.</p>",
    "hitchcock_meaning": "revolution of inquiry",
    "source_ids": {"easton": "gilboa", "smith": "gilboa"},
    "key_refs": ["1 Samuel 28:4", "1 Samuel 31:1", "2 Samuel 1:21"]
},
"gilead": {
    "term": "Gilead",
    "category": "places",
    "intro": "<p>Gilead (meaning <em>the heap or mass of testimony</em>) was the mountainous region east of the Jordan River, extending from the Yarmuk River in the north to the Arnon in the south, roughly corresponding to modern northern Jordan. It was a fertile land of forests, pasture, and spice-producing trees. The tribes of Reuben, Gad, and half of Manasseh settled there after the conquest (Num. 32:1–5). Gilead gave its name to the famous \"balm of Gilead,\" a healing resin widely traded in the ancient world (Gen. 37:25; Jer. 8:22). The region features prominently in the narratives of Jacob and Laban (Gen. 31), the judge Jephthah, the prophet Elijah, and later the Transjordanian campaigns of the divided monarchy. Gilead was among the first territories conquered by the Assyrians under Tiglath-pileser III (2 Kings 15:29).</p>",
    "hitchcock_meaning": "the heap or mass of testimony",
    "source_ids": {"easton": "gilead", "smith": "gilead", "isbe": "gilead"},
    "key_refs": ["Genesis 31:21", "Numbers 32:1", "Psalms 60:7", "Jeremiah 8:22"]
},
"gilead-balm-of": {
    "term": "Gilead, Balm of",
    "category": "concepts",
    "intro": "<p>The balm of Gilead was a precious aromatic resin or medicinal ointment produced in the Gilead region east of the Jordan, prized throughout the ancient Near East for its healing properties. It was one of the goods carried by Ishmaelite traders traveling from Gilead to Egypt when Joseph was sold (Gen. 37:25). The prophet Jeremiah laments the spiritual condition of Judah by asking rhetorically, \"Is there no balm in Gilead? Is there no physician there?\" (Jer. 8:22), using the balm as a symbol of healing now unavailable because of the people's apostasy. The exact botanical identity of the substance — whether a resin of the balsam tree (<em>Commiphora opobalsamum</em>), storax, or another gum — remains debated. In Christian tradition the phrase became a metaphor for the healing offered through Christ.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gilead-balm-of"},
    "key_refs": ["Genesis 37:25", "Jeremiah 8:22", "Jeremiah 46:11", "Ezekiel 27:17"]
},
"gilgal": {
    "term": "Gilgal",
    "category": "places",
    "intro": "<p>Gilgal (meaning <em>wheel; rolling; heap of stones</em>) is the name of several places in the Old Testament, the most important being the first Israelite camp west of the Jordan River after crossing on dry ground. At Gilgal, Joshua set up twelve stones taken from the riverbed as a memorial (Josh. 4:20), and all the males born in the wilderness were circumcised there (Josh. 5:2–9). Gilgal became Israel's base of operations for the Canaan campaign and the site of the first Passover celebration in the land. The tabernacle was stationed at Gilgal before moving to Shiloh. The prophet Samuel made circuit there (1 Sam. 7:16), and it was where Saul was confirmed as king (1 Sam. 11:14–15). A second Gilgal, near Bethel, was later associated with the schools of the prophets (2 Kings 2:1; 4:38) and condemned by Amos and Hosea as a center of corrupt worship (Amos 4:4; 5:5; Hos. 4:15).</p>",
    "hitchcock_meaning": "wheel; rolling; heap",
    "source_ids": {"easton": "gilgal", "smith": "gilgal", "isbe": "gilgal"},
    "key_refs": ["Joshua 4:20", "Joshua 5:9", "1 Samuel 11:15", "Amos 4:4"]
},
"giloh": {
    "term": "Giloh",
    "category": "places",
    "intro": "<p>Giloh (meaning <em>he that rejoices; he that overturns</em>) was a town in the hill country of Judah listed among the cities in Joshua's allotment (Josh. 15:51). It is best known as the hometown of Ahithophel, the brilliant counselor who served David but then defected to Absalom's rebellion (2 Sam. 15:12). When Absalom rejected his strategic counsel in favor of Hushai's advice, Ahithophel perceived that the rebellion would fail, returned home to Giloh, set his house in order, and hanged himself (2 Sam. 17:23). The site has not been positively identified.</p>",
    "hitchcock_meaning": "he that rejoices; he that overturns",
    "source_ids": {"easton": "giloh"},
    "key_refs": ["Joshua 15:51", "2 Samuel 15:12", "2 Samuel 17:23"]
},
"gimzo": {
    "term": "Gimzo",
    "category": "places",
    "intro": "<p>Gimzo (meaning <em>that bulrush</em>) was a town in the Shephelah, the lowland region of Judah between the central hill country and the coastal plain. It is mentioned only once in Scripture, as one of the towns seized by the Philistines during the reign of Ahaz when God used the Philistines to punish Israel's unfaithfulness (2 Chr. 28:18). It may correspond to modern Jimzu, a village near Lydda (Lod).</p>",
    "hitchcock_meaning": "that bulrush",
    "source_ids": {"easton": "gimzo"},
    "key_refs": ["2 Chronicles 28:18"]
},
"gin": {
    "term": "Gin",
    "category": "concepts",
    "intro": "<p>A gin in biblical usage is a trap or snare set to catch birds or animals, representing the Hebrew <em>pach</em>, a spring-trap or noose. The word appears in Isaiah 8:14 (\"a gin\" for the people) and Amos 3:5 (\"Can a bird fall in a snare upon the earth, where no gin is for him?\"), where it is used metaphorically for entrapments — whether divine judgment or the schemes of enemies. The image of the gin or snare is common in the wisdom literature and psalms to describe the dangers that beset the righteous (Ps. 141:9).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gin"},
    "key_refs": ["Amos 3:5", "Isaiah 8:14", "Psalms 141:9"]
},
"girdle": {
    "term": "Girdle",
    "category": "concepts",
    "intro": "<p>The girdle was a belt or sash worn around the waist or loins by both men and women in the ancient Near East, serving practical and symbolic functions. It could be made of leather (as Elijah's and John the Baptist's girdles were, 2 Kings 1:8; Matt. 3:4), fine linen, or embroidered cloth. Soldiers and warriors girded their loins for battle, which is the origin of the New Testament metaphor of putting on the \"girdle of truth\" as part of the spiritual armor (Eph. 6:14). To \"gird up the loins\" meant to prepare for strenuous activity by tucking one's robe into the belt. The high priest wore an elaborately worked girdle as part of his vestments (Ex. 28:4). Jeremiah's parable of the linen girdle hidden at the Euphrates illustrated Israel's ruin through Babylon (Jer. 13:1–11).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "girdle"},
    "key_refs": ["2 Kings 1:8", "Matthew 3:4", "Ephesians 6:14", "Jeremiah 13:1"]
},
"girgashite": {
    "term": "Girgashite",
    "category": "people",
    "intro": "<p>The Girgashites were one of the seven Canaanite nations inhabiting the land before the Israelite conquest, listed among the peoples God commanded Israel to dispossess (Deut. 7:1; Josh. 3:10). They appear in the Table of Nations as descendants of Canaan (Gen. 10:16). Their precise location in Canaan is unknown, as no Girgashite city has been positively identified. Ancient Ugaritic texts may contain a reference to a family or clan bearing a similar name. The Girgashites are included in covenantal and historical catalogs (Neh. 9:8) but play no further individual role in biblical narrative.</p>",
    "hitchcock_meaning": "who arrives from pilgrimage",
    "source_ids": {"easton": "girgashite"},
    "key_refs": ["Deuteronomy 7:1", "Joshua 3:10", "Genesis 10:16"]
},
"gittah-hepher": {
    "term": "Gittah-hepher",
    "category": "places",
    "intro": "<p>Gittah-hepher (meaning <em>digging; a wine-press</em>), also known simply as Gath-hepher, was a town on the border of Zebulun's territory in Galilee. It is significant primarily as the birthplace of the prophet Jonah son of Amittai (2 Kings 14:25; Josh. 19:13). The site is generally identified with modern Khirbet ez-Zurra', near Nazareth. Jonah's ministry predated his famous journey to Nineveh and included a prophecy during the reign of Jeroboam II that Israel's borders would be restored, which came to pass.</p>",
    "hitchcock_meaning": "digging; a wine-press",
    "source_ids": {"easton": "gittah-hepher"},
    "key_refs": ["2 Kings 14:25", "Joshua 19:13"]
},
"gittaim": {
    "term": "Gittaim",
    "category": "places",
    "intro": "<p>Gittaim (meaning <em>a double wine-press</em>) was a town to which the Beerothites fled (2 Sam. 4:3) and which was resettled after the return from the Babylonian exile (Neh. 11:33). The Beerothites were Hivites who had originally deceived Israel into a covenant in Joshua's day; they fled to Gittaim and remained there as sojourners. The site's exact location is uncertain but may have been in the Shephelah or Benjamin.</p>",
    "hitchcock_meaning": "a wine-press",
    "source_ids": {"easton": "gittaim"},
    "key_refs": ["2 Samuel 4:3", "Nehemiah 11:33"]
},
"gittite": {
    "term": "Gittite",
    "category": "people",
    "intro": "<p>A Gittite was an inhabitant of Gath, one of the five principal Philistine cities. The term appears most prominently in connection with David's loyal followers: Obed-edom the Gittite, in whose house the ark of the covenant rested for three months after Uzzah's death (2 Sam. 6:10–11), and Ittai the Gittite, a foreign commander who pledged absolute loyalty to David during Absalom's rebellion (2 Sam. 15:18–22). Goliath himself was also a Gittite. The loyalty of these foreign soldiers from Gath stands in notable contrast to those Israelites who abandoned David.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gittite"},
    "key_refs": ["2 Samuel 6:10", "2 Samuel 15:18", "1 Samuel 17:4"]
},
"gittith": {
    "term": "Gittith",
    "category": "concepts",
    "intro": "<p>Gittith appears in the superscription of three psalms (Pss. 8, 81, 84) as a musical term: \"To the chief musician upon Gittith.\" The exact meaning is uncertain. Some scholars derive it from Gath (the Philistine city) and understand it as a Gittite musical instrument or melody imported from there. Others connect it to the Hebrew word for wine-press (<em>gat</em>) and suggest it designated a vintage-harvest tune. The Septuagint renders it as \"for the wine-presses,\" supporting the harvest-song interpretation. The precise instrument or tune is no longer recoverable.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gittith"},
    "key_refs": ["Psalms 8:1", "Psalms 81:1", "Psalms 84:1"]
},
"gizonite": {
    "term": "Gizonite",
    "category": "names",
    "intro": "<p>Gizonite appears once in Scripture as a designation for Hashem the Gizonite, one of David's mighty men listed in 1 Chronicles 11:34. The term denotes his place of origin, though the location of Gizon is not known from any other source. The parallel list in 2 Samuel 23 may record a slightly different form of the name. Hashem the Gizonite belonged to the elite corps of warriors who served David with exceptional valor.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gizonite"},
    "key_refs": ["1 Chronicles 11:34"]
},
"glass": {
    "term": "Glass",
    "category": "concepts",
    "intro": "<p>Glass was known to the Egyptians from at least 1500 B.C. and to the Phoenicians, who are credited with developing the blowpipe technique. In ancient Israel, glass was a luxury item used for small vessels, ornaments, and inlay work. The Hebrew word <em>zekukith</em> (Job 28:17), comparing gold and glass as items of great worth, is one of the few direct OT references. In the New Testament, the sea of glass before the divine throne in Revelation (Rev. 4:6; 15:2) conveys transcendent purity and calm. The mirror metaphor — seeing \"through a glass, darkly\" (1 Cor. 13:12, KJV) — refers to ancient polished-metal mirrors, not transparent glass, but the image communicates the partial, indirect nature of present spiritual knowledge contrasted with the full clarity of the eschaton.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "glass"},
    "key_refs": ["Job 28:17", "Revelation 4:6", "1 Corinthians 13:12"]
},
"glean": {
    "term": "Glean",
    "category": "concepts",
    "intro": "<p>Gleaning was the practice of gathering grain or grapes left behind by harvesters, and the Mosaic law mandated that farmers leave a portion of their fields and vineyards unharvested for the poor, the widow, the orphan, and the foreigner (Lev. 19:9–10; 23:22; Deut. 24:19–21). This provision established a structural form of social welfare built into the agricultural calendar rather than depending on ad hoc charity. The book of Ruth provides the most detailed narrative illustration of gleaning: Ruth gleaned in Boaz's barley and wheat fields at harvest time, ultimately leading to her redemption and marriage to Boaz (Ruth 2). The practice shaped Israel's understanding of God's care for the vulnerable.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "glean"},
    "key_refs": ["Leviticus 19:9", "Deuteronomy 24:19", "Ruth 2:3"]
},
"glede": {
    "term": "Glede",
    "category": "concepts",
    "intro": "<p>The glede is listed among the unclean birds in the Mosaic dietary law (Deut. 14:13). The Hebrew term <em>ra'ah</em> denotes a bird of prey, most likely identified as the red kite (<em>Milvus milvus</em>), a falcon-family bird known for its keen eyesight — the root of the Hebrew word means \"to see.\" The kite is common throughout the Levant. Along with eagles, vultures, and other raptors, it was forbidden as food for Israel. The parallel list in Leviticus 11 uses a slightly different Hebrew term, making precise ornithological identification uncertain.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "glede"},
    "key_refs": ["Deuteronomy 14:13", "Leviticus 11:14"]
},
"glorify": {
    "term": "Glorify",
    "category": "concepts",
    "intro": "<p>To glorify means to honor, praise, or magnify — to cause another's excellence and worth to be recognized and celebrated. In Scripture, the primary object of glorification is God: human beings are created to glorify God, and all of creation declares his glory (Ps. 19:1). Jesus spoke of glorifying the Father through the completion of his redemptive mission (John 17:4), and the Father glorified the Son in the resurrection and ascension (John 13:31–32; Phil. 2:9–11). The New Testament also speaks of believers being glorified — transformed to share in the divine glory as the final stage of salvation (Rom. 8:30). The Westminster Shorter Catechism's famous answer, \"Man's chief end is to glorify God and enjoy him forever,\" crystallizes this biblical theme.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "glorify"},
    "key_refs": ["John 17:4", "John 13:31", "Romans 8:30", "Psalms 19:1"]
},
"glory": {
    "term": "Glory",
    "category": "concepts",
    "intro": "<p>Glory (Hebrew <em>kābôd</em>, Greek <em>doxa</em>) is one of the richest theological terms in Scripture, carrying several distinct but related meanings. In its basic sense it refers to weight, abundance, or wealth, and hence to the honor and reputation that accompanies them (Gen. 31:1; Ps. 49:12). Most significantly, the \"glory of God\" (<em>kābôd YHWH</em>) denotes the visible manifestation of the divine presence — the luminous cloud that filled the tabernacle and temple (Ex. 40:34–35; 1 Kings 8:11), appearing at Sinai, guiding Israel in the wilderness, and filling Ezekiel's vision of the divine chariot. In the New Testament the divine glory is revealed in Jesus Christ: John declares that \"the Word became flesh and dwelt among us, and we beheld his glory\" (John 1:14). The eschatological hope of believers is to be conformed to the glory of Christ (Rom. 8:18; Col. 3:4) and to dwell in the glory of the new Jerusalem where God himself is the light (Rev. 21:23).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "glory", "smith": "glory", "isbe": "glory"},
    "key_refs": ["Exodus 40:34", "John 1:14", "Romans 8:18", "Revelation 21:23"]
},
"glutton": {
    "term": "Glutton",
    "category": "concepts",
    "intro": "<p>A glutton in biblical usage is one who is addicted to excessive eating and drinking, often linked with a lazy, dissolute lifestyle. The Mosaic law prescribed that a persistently rebellious son who was \"a glutton and a drunkard\" could be brought before the elders and stoned (Deut. 21:20–21), reflecting how seriously the community took this breakdown of self-control and filial respect. Jesus was falsely accused by his critics of being \"a gluttonous man and a winebibber\" (Matt. 11:19; Luke 7:34) because he ate freely with sinners and tax collectors. Paul quotes a Cretan saying that Cretans are always \"gluttons\" (Titus 1:12) in warning against false teachers. The concept belongs to the broader biblical treatment of self-mastery and the ordering of bodily appetites.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "glutton"},
    "key_refs": ["Deuteronomy 21:20", "Matthew 11:19", "Proverbs 23:21"]
},
"gnash": {
    "term": "Gnash",
    "category": "concepts",
    "intro": "<p>To gnash the teeth is a gesture of rage, grief, or extreme anguish in biblical literature. In the Old Testament, enemies gnash their teeth at the righteous in hatred and contempt (Ps. 35:16; 37:12; Lam. 2:16). In the New Testament, \"weeping and gnashing of teeth\" becomes a repeated phrase of Jesus describing the torment of those excluded from the kingdom of God — the outer darkness, the furnace of fire (Matt. 8:12; 13:42, 50; 22:13; 24:51; 25:30; Luke 13:28). Stephen's accusers gnashed on him with their teeth in fury before stoning him (Acts 7:54). The image conveys extreme emotional and physical distress.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gnash"},
    "key_refs": ["Psalms 35:16", "Matthew 8:12", "Acts 7:54"]
},
"gnat": {
    "term": "Gnat",
    "category": "concepts",
    "intro": "<p>The gnat is mentioned in two significant biblical contexts. (1.) In the plagues of Egypt, the third plague was an infestation of gnats or lice (Hebrew <em>kinnim</em>), produced when Aaron struck the dust of the earth at God's command (Ex. 8:16–19). The Egyptian magicians could not replicate this plague and declared, \"This is the finger of God.\" (2.) Jesus uses the gnat as an image of meticulous fastidiousness in his rebuke of the Pharisees: \"Ye blind guides, which strain at a gnat, and swallow a camel\" (Matt. 23:24) — condemning their scrupulous tithing of kitchen herbs while neglecting the weightier matters of justice, mercy, and faithfulness. The gnat was among the smallest of creatures; the contrast with the camel (the largest land animal in Palestine) makes the hypocrisy vivid.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gnat"},
    "key_refs": ["Exodus 8:16", "Matthew 23:24"]
},
"goad": {
    "term": "Goad",
    "category": "concepts",
    "intro": "<p>A goad was a pointed stick, typically made of wood with a metal tip, used to drive oxen while plowing. It appears in two notable scriptural contexts. (1.) Shamgar the judge slew 600 Philistines with an oxgoad (Judg. 3:31), using a farm implement as a weapon. (2.) Paul's vision of the risen Christ on the Damascus road included the words, \"It is hard for thee to kick against the pricks\" (Acts 26:14) — the goads being a metaphor for divine prodding that a rebellious person injures himself by resisting. Ecclesiastes 12:11 compares the words of the wise to goads that prod the mind to productive thought.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goad"},
    "key_refs": ["Judges 3:31", "Acts 26:14", "Ecclesiastes 12:11"]
},
"goat": {
    "term": "Goat",
    "category": "concepts",
    "intro": "<p>The goat (<em>Capra hircus</em>) was among the most important domestic animals of ancient Israel, kept for milk, meat, leather, and hair. Goats feature prominently in Israel's sacrificial system: a male goat was among the acceptable burnt offerings (Lev. 1:10), and the Day of Atonement ritual involved two goats — one sacrificed as a sin offering and one, the scapegoat, over which the high priest confessed Israel's sins before releasing it into the wilderness bearing the people's iniquities (Lev. 16:7–10, 20–22). In prophecy and eschatology, goats represent the wicked: the parable of the sheep and goats separates the righteous from the unrighteous at the final judgment (Matt. 25:32–33). Daniel's prophetic vision of a goat from the west represented the Greek empire under Alexander the Great (Dan. 8:5–8).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goat", "smith": "goat"},
    "key_refs": ["Leviticus 16:8", "Matthew 25:32", "Daniel 8:5"]
},
"goath": {
    "term": "Goath",
    "category": "places",
    "intro": "<p>Goath (meaning <em>his touching; his roaring</em>) was a location near Jerusalem mentioned in Jeremiah's prophecy of the city's restoration after exile: \"And the measuring line shall yet go forth over against it upon the hill Gareb, and shall compass about to Goath\" (Jer. 31:39). The passage describes the future enlarged boundaries of Jerusalem encompassing areas previously outside the city walls. Goath has not been positively identified, and its exact location within the Jerusalem environs remains unknown.</p>",
    "hitchcock_meaning": "his touching; his roaring",
    "source_ids": {"easton": "goath"},
    "key_refs": ["Jeremiah 31:39"]
},
"gob": {
    "term": "Gob",
    "category": "places",
    "intro": "<p>Gob (meaning <em>cistern; grasshopper</em>) was a site at which two battles between David's warriors and the Philistine giants took place (2 Sam. 21:18–19). In the parallel account in 1 Chronicles 20:4 the location is called Gezer, suggesting that Gob and Gezer may be the same place or close neighbors. At Gob, Sibbechai the Hushathite slew Saph, a descendant of the giants, and Elhanan the son of Jaare-oregim slew the brother of Goliath. These battles completed the subjugation of the Philistine giant clan begun by David's defeat of Goliath.</p>",
    "hitchcock_meaning": "cistern; grasshopper",
    "source_ids": {"easton": "gob"},
    "key_refs": ["2 Samuel 21:18", "1 Chronicles 20:4"]
},
"goblet": {
    "term": "Goblet",
    "category": "concepts",
    "intro": "<p>A goblet was a rounded drinking vessel, often distinguished from an ordinary cup by its more ornate form. In the Song of Solomon 7:2, the beloved's navel is compared to \"a round goblet which wanteth not liquor\" — a poetic image of graceful form and abundance. In a more somber vein, the prophets employ the cup or goblet as a symbol of divine judgment: God compels the nations to drink from the cup of his wrath (Jer. 25:15; Rev. 14:10). Silver goblets were among the tableware in Egyptian royal households, as illustrated by the silver cup hidden in Benjamin's sack by Joseph's command (Gen. 44:2).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goblet"},
    "key_refs": ["Song of Solomon 7:2", "Genesis 44:2", "Jeremiah 25:15"]
},
"god": {
    "term": "God",
    "category": "concepts",
    "intro": "<p>\"God\" in English renders several Hebrew and Greek terms. The primary Hebrew designations are <em>'El</em> (from a root meaning \"to be strong\"), <em>'Elōah</em> (used chiefly in poetry, especially Job), and the plural <em>'Elōhîm</em> — the common OT name for the deity, used with singular verbs when referring to Israel's God and expressing his fullness of power and majesty. The covenant name of the God of Israel, <em>YHWH</em> (rendered LORD in most English translations), expresses self-existent being and faithful relationship. God's essential attributes in Scripture include eternity, omnipresence, omniscience, omnipotence, perfect holiness, justice, and love. The Shema — \"The LORD our God, the LORD is one\" (Deut. 6:4) — is the foundational monotheistic confession of Israel. The New Testament reveals the Trinity: Father, Son, and Holy Spirit as the one God (Matt. 28:19; 2 Cor. 13:14). Systematic theology employs the term <em>theology proper</em> for the disciplined study of God's nature and attributes.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "god", "smith": "god", "isbe": "god"},
    "key_refs": ["Deuteronomy 6:4", "Exodus 34:6", "Psalms 14:1", "John 4:24"]
},
"godhead": {
    "term": "Godhead",
    "category": "concepts",
    "intro": "<p>\"Godhead\" is an archaic English term denoting the divine nature or essence, occurring three times in the King James Bible to render distinct Greek words. In Acts 17:29 (<em>theion</em>) Paul declares that the divine nature is not like gold, silver, or stone; in Romans 1:20 (<em>theiotēs</em>) the eternal power and divine nature are visible in creation; in Colossians 2:9 (<em>theotēs</em>) Paul states that in Christ \"dwelleth all the fulness of the Godhead bodily.\" The Colossians passage is the most theologically significant: it asserts that the complete divine nature, not merely divine attributes, is permanently and bodily present in the incarnate Christ. This text became central in Trinitarian and Christological debates about the full deity of Jesus.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "godhead"},
    "key_refs": ["Acts 17:29", "Romans 1:20", "Colossians 2:9"]
},
"godliness": {
    "term": "Godliness",
    "category": "concepts",
    "intro": "<p>Godliness (<em>eusebeia</em> in Greek) refers to the whole of practical piety — reverence toward God expressed in faithful conduct and worship. Paul describes it as profitable both for this life and for eternity (1 Tim. 4:8) and lists it among the qualities Timothy is to pursue (1 Tim. 6:11; 2 Pet. 1:6–7). The \"mystery of godliness\" (1 Tim. 3:16) refers to the content of the Christian faith — the incarnation, resurrection, ascension, and proclamation of Christ — which is the foundation of true piety. Peter connects godliness to knowledge and self-control as a progression in Christian character (2 Pet. 1:3–7). The New Testament warns against a \"form of godliness\" that denies its power — external religious performance without inner transformation (2 Tim. 3:5).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "godliness"},
    "key_refs": ["1 Timothy 4:8", "2 Peter 1:6", "1 Timothy 3:16", "2 Timothy 3:5"]
},
"goel": {
    "term": "Goel",
    "category": "concepts",
    "intro": "<p>Goel (Hebrew <em>gō'ēl</em>, the participle of <em>gā'al</em>, \"to redeem\") is the kinsman-redeemer — the nearest male relative who bore both the right and the obligation to redeem a distressed family member or their property. Duties of the goel included purchasing a kinsman's land to keep it within the family (Lev. 25:25), redeeming a kinsman sold into slavery (Lev. 25:48–49), marrying a deceased kinsman's widow (levirate-like duty, illustrated in Ruth 4), and serving as the blood-avenger against a murderer (Num. 35:19). The institution of the goel is applied theologically to God himself, who acts as Israel's redeemer from Egyptian slavery (Ex. 6:6; 15:13) and from Babylonian exile (Isa. 41:14; 43:14). In the New Testament, Christ's redemptive work fulfills this typology as the divine kinsman-redeemer who pays the ransom price for humanity.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goel"},
    "key_refs": ["Ruth 3:12", "Ruth 4:4", "Leviticus 25:25", "Isaiah 41:14"]
},
"gog": {
    "term": "Gog",
    "category": "people",
    "intro": "<p>Gog appears in two distinct biblical contexts. (1.) A Reubenite, the son of Shemaiah and father of Shimei, mentioned in the genealogy of 1 Chronicles 5:4. (2.) The central figure of Ezekiel's eschatological prophecy (Ezek. 38–39): the prince of Meshech and Tubal, from the \"land of Magog,\" who leads a great multinational coalition against restored Israel in the latter days. God brings Gog against Israel to defeat him utterly and demonstrate his holiness before the nations, with the aftermath involving seven months of burying the dead (Ezek. 39:12). The name Gog and Magog reappear in Revelation 20:8 as symbolic names for the nations Satan gathers for the final rebellion at the end of the millennium. Attempts to identify the historical Gog with specific nations (Scythians, Russians, etc.) remain speculative.</p>",
    "hitchcock_meaning": "roof; covering",
    "source_ids": {"easton": "gog", "smith": "gog", "isbe": "gog"},
    "key_refs": ["Ezekiel 38:2", "Ezekiel 39:11", "Revelation 20:8"]
},
"golan": {
    "term": "Golan",
    "category": "places",
    "intro": "<p>Golan (meaning <em>passage; revolution</em>) was a city in the region of Bashan east of the Jordan, assigned to the half-tribe of Manasseh and designated as one of the six cities of refuge for the accidental manslayer (Deut. 4:43; Josh. 20:8). It was also set apart as a Levitical city given to the Gershonite Levites (Josh. 21:27). Golan gave its name to the surrounding district — the Golan Heights, still known by that name today — a strategically elevated plateau east of the Sea of Galilee.</p>",
    "hitchcock_meaning": "passage; revolution",
    "source_ids": {"easton": "golan"},
    "key_refs": ["Deuteronomy 4:43", "Joshua 20:8", "Joshua 21:27"]
},
"gold": {
    "term": "Gold",
    "category": "concepts",
    "intro": "<p>Gold was the most prized metal in the ancient world and features prominently throughout Scripture as a symbol of wealth, divine splendor, and purity. The Hebrew Bible uses multiple words for gold (<em>zāhāb</em>, <em>paz</em>, <em>kethem</em>, <em>hārûz</em>), reflecting different grades and forms. It was used extensively in the construction and furnishing of the tabernacle and temple: the ark of the covenant, the mercy seat, the lampstand, the altar of incense, and the overlaid walls and doors were all of gold (Ex. 25–26; 1 Kings 6–7). Solomon's reign represented the apex of Israelite gold use; 1 Kings 10 describes his immense wealth in gold. Gold figures in the New Testament as among the gifts brought by the Magi (Matt. 2:11) and in the imagery of the New Jerusalem, whose streets and walls are described as pure gold (Rev. 21:18–21). Theologically, gold is used as a metaphor for faith refined through trials (1 Pet. 1:7; Job 23:10).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gold", "smith": "gold"},
    "key_refs": ["Exodus 25:11", "1 Kings 10:14", "1 Peter 1:7", "Revelation 21:18"]
},
"golden-calf": {
    "term": "Golden Calf",
    "category": "events",
    "intro": "<p>The golden calf was an idolatrous image twice erected in Israel's history as a substitute focus for worship. (1.) At Sinai, while Moses received the law on the mountain, Aaron fashioned a golden calf from the people's earrings in response to their demand for visible gods (Ex. 32:1–6). The people declared, \"These be thy gods, O Israel, which brought thee up out of the land of Egypt,\" an apostasy that provoked Moses to smash the stone tablets. God threatened to destroy Israel; Moses interceded, and 3,000 were slain by the Levites as judgment. (2.) Jeroboam I set up two golden calves at Bethel and Dan to prevent his northern kingdom's subjects from making pilgrimages to Jerusalem, declaring the same words as Aaron had (1 Kings 12:28–30). This became \"the sin of Jeroboam\" that persisted throughout the northern kingdom and contributed to its eventual Assyrian exile (2 Kings 17:16–23). The calf may have been conceived as a pedestal for the invisible deity rather than the deity itself — a syncretistic compromise condemned throughout the prophets.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "golden-calf"},
    "key_refs": ["Exodus 32:4", "1 Kings 12:28", "Deuteronomy 9:16", "Nehemiah 9:18"]
},
"goldsmith": {
    "term": "Goldsmith",
    "category": "concepts",
    "intro": "<p>Goldsmiths in the ancient Near East were highly skilled artisans who worked gold into ornaments, vessels, cult objects, and inlaid decorations. In Israel, the craft is mentioned in connection with the refining of idols — Isaiah mocks the idol-maker who fashions a god from gold and then falls down before it (Isa. 40:19; 41:7). Nehemiah lists \"the goldsmiths' sons\" among those who helped repair the Jerusalem wall (Neh. 3:8, 31–32), suggesting a guild of craftsmen organized by family or trade in the post-exilic period. The imagery of refining gold as a metaphor for divine purification of God's people appears in Malachi 3:3, where God is like a refiner's fire purifying the sons of Levi as gold.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goldsmith"},
    "key_refs": ["Isaiah 40:19", "Nehemiah 3:8", "Malachi 3:3"]
},
"golgotha": {
    "term": "Golgotha",
    "category": "places",
    "intro": "<p>Golgotha (Aramaic, meaning <em>a heap of skulls</em> or <em>skull-shaped place</em>; Latin Calvaria, English Calvary) was the site of Jesus' crucifixion, just outside Jerusalem (Matt. 27:33; Mark 15:22; Luke 23:33; John 19:17). The name most likely derived from the hill's skull-like shape rather than from any use as a place of execution. Crucifixions typically occurred along public roads outside city gates to maximize the deterrent effect, consistent with Golgotha being near but outside Jerusalem's walls (Heb. 13:12; John 19:20). The exact location within the Jerusalem landscape remains debated: the traditional site inside the Church of the Holy Sepulchre has ancient support from the 4th century onwards, while Gordon's Calvary north of the Damascus Gate attracted attention in the 19th century. Golgotha stands at the center of Christian theology as the place where the redemptive death of Christ was accomplished.</p>",
    "hitchcock_meaning": "a heap of skulls; something skull-shaped",
    "source_ids": {"easton": "golgotha", "smith": "golgotha", "isbe": "golgotha"},
    "key_refs": ["Matthew 27:33", "Mark 15:22", "John 19:17", "Hebrews 13:12"]
},
"goliath": {
    "term": "Goliath",
    "category": "people",
    "intro": "<p>Goliath (meaning <em>passage; revolution; heap</em>) was a Philistine warrior from Gath, described as a giant of extraordinary stature — \"six cubits and a span\" in height (approximately nine feet, 1 Sam. 17:4). He was likely descended from the Rephaim, the giant peoples of Canaan who took refuge among the Philistines after being dispossessed by Israel (Deut. 2:20–21). For forty days Goliath issued a daily challenge to Israel's army to send a champion to settle the battle by single combat, a practice attested in ancient Near Eastern warfare. When the armies met in the Valley of Elah, David, a young shepherd and son of Jesse, accepted the challenge without armor, trusting in the LORD. He struck Goliath with a stone from his sling, felled him, and cut off his head with Goliath's own sword (1 Sam. 17:51). David's victory became one of the defining moments of his rise to prominence. A second warrior named Goliath, whose brother was slain in a later Philistine war, appears in 2 Samuel 21:19 / 1 Chronicles 20:5, creating a textual difficulty resolved by the Chronicles parallel as referring to Lahmi, Goliath's brother.</p>",
    "hitchcock_meaning": "passage; revolution; heap",
    "source_ids": {"easton": "goliath", "smith": "goliath", "isbe": "goliath"},
    "key_refs": ["1 Samuel 17:4", "1 Samuel 17:51", "2 Samuel 21:19"]
},
"gomer": {
    "term": "Gomer",
    "category": "people",
    "intro": "<p>Gomer is the name of two biblical figures. (1.) The daughter of Diblaim, who became the wife of the prophet Hosea at God's command, as a living parable of Israel's spiritual adultery — her unfaithfulness to Hosea mirrored Israel's idolatry and covenant-breaking (Hos. 1:3; 3:1–3). Whether the marriage was literal or visionary is debated, but the theological point is clear: God's relationship with Israel is like a faithful husband's love for an unfaithful wife. (2.) The eldest son of Japheth, grandson of Noah, and ancestor of the northern peoples known as the Cimmerians (Gen. 10:2–3; 1 Chr. 1:5–6). Gomer's descendants — Ashkenaz, Riphath, and Togarmah — are associated with peoples of Asia Minor and the Black Sea region. Ezekiel lists Gomer among the nations that join Gog's coalition (Ezek. 38:6).</p>",
    "hitchcock_meaning": "to finish; complete",
    "source_ids": {"easton": "gomer", "smith": "gomer"},
    "key_refs": ["Hosea 1:3", "Genesis 10:2", "Ezekiel 38:6"]
},
"gomorrah": {
    "term": "Gomorrah",
    "category": "places",
    "intro": "<p>Gomorrah (meaning <em>rebellious people</em> or <em>submersion</em>) was one of the five cities of the plain of Siddim near the southern end of the Dead Sea region, destroyed along with Sodom by fire and brimstone from heaven (Gen. 10:19; 13:10; 19:24–28). The wickedness of Sodom and Gomorrah was so notorious that Abraham interceded with God for any righteous people within them, but none beyond Lot's family were found (Gen. 18:20–33). The destruction of these cities became the paradigmatic example of divine judgment on extreme moral depravity throughout Scripture (Deut. 29:23; Isa. 1:9–10; Jer. 23:14; Amos 4:11; 2 Pet. 2:6; Jude 7). Jesus invoked Gomorrah's fate in warning that cities rejecting his disciples would face a worse judgment (Matt. 10:15). The precise geographic location of Gomorrah remains disputed, with various sites along the Dead Sea's southern shore proposed by archaeologists.</p>",
    "hitchcock_meaning": "rebellious people",
    "source_ids": {"easton": "gomorrah", "smith": "gomorrah", "isbe": "gomorrah"},
    "key_refs": ["Genesis 19:24", "Isaiah 1:9", "Matthew 10:15", "Jude 7"]
},
"goodly-trees": {
    "term": "Goodly Trees",
    "category": "concepts",
    "intro": "<p>\"Boughs of goodly trees\" (Lev. 23:40) were among the four plant species specified for the celebration of the Feast of Tabernacles (Sukkot), along with palm branches, thick boughs of trees, and willows of the brook. The Hebrew phrase <em>hadar</em> (splendid, beautiful) was interpreted by the rabbis as referring to the citron or etrog (<em>Citrus medica</em>), a fragrant fruit still used in the traditional Sukkot ceremony. The four species together — etrog, palm, myrtle, and willow — are waved before the LORD in celebration of the harvest, symbolizing the joy and completeness of God's provision. The identification with citron is ancient but not certain from the text itself.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goodly-trees"},
    "key_refs": ["Leviticus 23:40", "Nehemiah 8:15"]
},
"goodness": {
    "term": "Goodness",
    "category": "concepts",
    "intro": "<p>Goodness in biblical ethics is not a passive quality but the active, deliberate preference of right over wrong — a firm and persistent resistance to moral evil and a resolute pursuit of virtue. In man, goodness is the outworking of a character formed by right desires and disciplined habits. The Hebrew <em>tôb</em> and Greek <em>agathōsynē</em> encompass both moral excellence and beneficial effect: what is genuinely good is also genuinely beneficial. The New Testament lists goodness among the fruit of the Spirit (Gal. 5:22) and describes it as one of the qualities believers are to produce through faith (2 Pet. 1:5). Paul prays that the Thessalonians may be counted worthy of their calling, and that God would fulfill every desire for goodness (2 Thess. 1:11). Ultimately, only God is good in the absolute sense (Mark 10:18), and human goodness is derivative of and dependent upon divine grace.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goodness"},
    "key_refs": ["Galatians 5:22", "2 Peter 1:5", "Romans 15:14"]
},
"goodness-of-god": {
    "term": "Goodness of God",
    "category": "concepts",
    "intro": "<p>The goodness of God is the divine perfection by which he exercises his benevolence toward creatures according to their nature and circumstances. It includes his benevolence (the disposition to do good), his mercy (goodness toward the guilty), his grace (goodness toward the undeserving), and his longsuffering (goodness toward the persistently rebellious). The classic declaration of Exodus 33:19 — \"I will make all my goodness pass before thee\" — is the self-revelation God proclaimed to Moses after the golden calf incident. Psalm 145:8–9 declares: \"The LORD is gracious, and full of compassion; slow to anger, and of great mercy. The LORD is good to all: and his tender mercies are over all his works.\" The New Testament grounds God's goodness supremely in the gift of his Son (John 3:16; Rom. 8:32). Paul's warning that \"the goodness of God leadeth thee to repentance\" (Rom. 2:4) shows that divine benevolence is meant to evoke gratitude and transformation, not presumption.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "goodness-of-god"},
    "key_refs": ["Psalms 145:8", "Exodus 33:19", "Romans 2:4", "1 John 4:8"]
},
"gopher": {
    "term": "Gopher",
    "category": "concepts",
    "intro": "<p>Gopher wood is the material God specified for the construction of Noah's ark: \"Make thee an ark of gopher wood\" (Gen. 6:14). The Hebrew term <em>gofer</em> appears nowhere else in Scripture, making its identification uncertain. Proposed identifications include cypress (common in the ancient Near East, durable for shipbuilding), cedar, pine, or an obsolete Semitic term for a resinous wood. Some scholars note that the word <em>kopher</em> (pitch, used to seal the ark) is cognate, suggesting that gopher wood may refer to a resinous, pitch-producing tree. The Septuagint renders it as \"squared timber.\" No certain botanical identification has been established.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gopher"},
    "key_refs": ["Genesis 6:14"]
},
"goshen": {
    "term": "Goshen",
    "category": "places",
    "intro": "<p>Goshen was a fertile district in northeastern Egypt, in the Nile Delta region, where Jacob's family settled at Joseph's invitation (Gen. 45:10; 46:28–29). Joseph presented his family to Pharaoh as shepherds, and they were granted Goshen because Egyptians generally had an aversion to shepherds (Gen. 46:34), keeping Israel somewhat separate from the Egyptian population. The family of seventy souls multiplied greatly in Goshen during the 430 years of sojourn in Egypt (Ex. 12:40–41). During the plagues, Goshen was repeatedly distinguished from the rest of Egypt: the flies, the pestilence, the hail, and the darkness did not come upon Goshen where Israel dwelt (Ex. 8:22; 9:26; 10:23). The region is generally identified with the Wadi Tumilat in the eastern delta. The name Goshen is also applied to a district in southern Canaan (Josh. 10:41; 11:16) and to a town in the hill country of Judah (Josh. 15:51).</p>",
    "hitchcock_meaning": "approaching; drawing near",
    "source_ids": {"easton": "goshen", "smith": "goshen", "isbe": "goshen"},
    "key_refs": ["Genesis 45:10", "Genesis 46:28", "Exodus 8:22", "Exodus 12:37"]
},
"gospel": {
    "term": "Gospel",
    "category": "concepts",
    "intro": "<p>Gospel (Old English <em>godspel</em>, meaning \"good news\" or \"word of God\") translates the Greek <em>euangelion</em>, itself the background of the English word \"evangel.\" In the New Testament, \"the gospel\" is the announcement of the good news of salvation accomplished through the death, burial, and resurrection of Jesus Christ (1 Cor. 15:1–4). Paul defines it as the power of God for salvation to everyone who believes (Rom. 1:16). The term had secular Greek usage for the announcement of victory in battle or the birth of a royal heir, and the prophets of Isaiah anticipated a messenger announcing \"good tidings\" of God's reign (Isa. 52:7; 61:1). Jesus inaugurated his ministry proclaiming \"the gospel of the kingdom\" (Matt. 4:23). The apostles were commissioned to preach the gospel to every creature (Mark 16:15). Paul distinguished the true gospel from any counterfeit that added conditions to grace (Gal. 1:6–9). Theologically, the gospel encompasses both the facts of redemption and their personal appropriation through faith.</p>",
    "hitchcock_meaning": "going out, departure",
    "source_ids": {"easton": "gospel", "smith": "gospel", "isbe": "gospel"},
    "key_refs": ["Romans 1:16", "1 Corinthians 15:3", "Mark 16:15", "Isaiah 52:7"]
},
"gospels": {
    "term": "Gospels",
    "category": "concepts",
    "intro": "<p>The four Gospels — Matthew, Mark, Luke, and John — are the canonical accounts of the life, ministry, death, and resurrection of Jesus Christ. The designation \"Gospel according to\" is ancient, reflecting that each is an account of the one gospel message narrated from a particular perspective. Mark is generally considered the earliest (c. 50–65 A.D.), while Matthew and Luke likely drew on Mark and a shared sayings source (Q), and John represents an independent tradition (c. 85–95 A.D.). Matthew was written primarily for a Jewish-Christian audience, emphasizing Jesus as the fulfillment of OT messianic prophecy. Mark is the most direct and action-focused account. Luke, written for a Gentile audience, stresses universal salvation and the Holy Spirit. John is the most theological, opening with a prologue on the pre-existent Word and structuring Jesus' ministry around seven signs and seven \"I am\" discourses. Together the four Gospels present a stereoscopic portrait of the person of Christ while maintaining theological harmony on all essentials of the faith.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gospels", "smith": "gospels", "isbe": "gospels"},
    "key_refs": ["Matthew 4:23", "Mark 1:1", "Luke 1:1", "John 20:31"]
},
"gourd": {
    "term": "Gourd",
    "category": "concepts",
    "intro": "<p>Two different plants are called gourd in the English Bible. (1.) Jonah's gourd (Hebrew <em>qîqāyôn</em>, Jonah 4:6–10), identified by most modern scholars with the castor-oil plant (<em>Ricinus communis</em>), which grows rapidly to provide shade and then withers quickly. God used this plant to illustrate his compassion: when Jonah was angry over its withering, God pointed out that Jonah's concern for a temporary plant was nothing compared to God's compassion for the 120,000 souls of Nineveh. (2.) The \"wild gourds\" (Hebrew <em>paqquōt</em>), shredded into the pot at Gilgal causing poisoning, were likely colocynth (<em>Citrullus colocynthis</em>), a bitter and toxic wild plant (2 Kings 4:38–40). Elisha healed the stew by adding meal.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "gourd"},
    "key_refs": ["Jonah 4:6", "2 Kings 4:38"]
},
"government-of-god": {
    "term": "Government of God",
    "category": "concepts",
    "intro": "<p>The government of God refers to God's sovereign ordering and administration of all creation in accordance with his will and purposes — typically treated under the heading of providence. God's government encompasses both his upholding of the natural order (general providence) and his direction of human history toward redemptive ends (special providence). Scripture affirms that \"the LORD reigneth\" (Ps. 93:1; 97:1) and that \"he doeth according to his will in the army of heaven, and among the inhabitants of the earth\" (Dan. 4:35). The government of God is distinct from his decretive will (what he ordains) and his preceptive will (what he commands), though both are aspects of his sovereign rule. The Lord's Prayer petition, \"Thy kingdom come, thy will be done\" (Matt. 6:10), expresses the believer's alignment with God's governing purposes.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "government-of-god"},
    "key_refs": ["Psalms 93:1", "Daniel 4:35", "Matthew 6:10", "Romans 8:28"]
},
"governments": {
    "term": "Governments",
    "category": "concepts",
    "intro": "<p>\"Governments\" appears in 1 Corinthians 12:28 (Greek <em>kubernēseis</em>, literally \"steeringsmanship\" or \"administrations\") as one of the spiritual gifts listed among those God has appointed in the church: apostles, prophets, teachers, miracles, gifts of healing, helps, governments, and varieties of tongues. The word denotes the capacity for wise administration and guiding a community — the same Greek root gives the English word \"cybernetics.\" In political theology, Scripture affirms that civil governments are instituted by God for the restraint of evil and the promotion of justice (Rom. 13:1–7; 1 Pet. 2:13–14), though they remain accountable to the divine Governor they represent.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "governments"},
    "key_refs": ["1 Corinthians 12:28", "Romans 13:1", "1 Peter 2:13"]
},
"governor": {
    "term": "Governor",
    "category": "concepts",
    "intro": "<p>The English word \"governor\" translates several Hebrew and Greek terms in Scripture, covering a range of administrative roles. In the Old Testament, the Hebrew <em>nāgîd</em> (a prominent leader), <em>peḥāh</em> (a provincial governor under Persian or Assyrian authority), and <em>śar</em> (a prince or official) are all rendered \"governor\" at various points. In the New Testament, Roman governors held judicial and military authority over provinces: Pontius Pilate and Festus were governors (<em>hēgemōn</em>) of Judea. Joseph was appointed governor over Egypt (Gen. 42:6; Acts 7:10). The governor of Damascus sought to seize Paul (2 Cor. 11:32). The term thus encompasses everything from local clan leaders to imperial provincial administrators across the full sweep of biblical history.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "governor"},
    "key_refs": ["2 Chronicles 28:7", "Genesis 42:6", "Matthew 27:2", "Romans 13:3"]
},
"gozan": {
    "term": "Gozan",
    "category": "places",
    "intro": "<p>Gozan (meaning <em>fleece; pasture; who nourisheth the body</em>) was a region in northwestern Mesopotamia on the Habor River (a tributary of the Euphrates), to which the Assyrian kings deported the northern tribes of Israel following the fall of Samaria in 722 B.C. under Shalmaneser V and Sargon II (2 Kings 17:6; 18:11; 1 Chr. 5:26). The area corresponds to the modern Khabur River basin in northeastern Syria. Gozan is also mentioned in Sennacherib's taunt to Hezekiah, listing it among the nations the Assyrians had defeated, whose gods had not saved them (2 Kings 19:12; Isa. 37:12). Archaeological discoveries from Tell Halaf in the Gozan region have illuminated the culture of that area.</p>",
    "hitchcock_meaning": "fleece; pasture; who nourisheth the body",
    "source_ids": {"easton": "gozan"},
    "key_refs": ["2 Kings 17:6", "2 Kings 19:12", "1 Chronicles 5:26"]
},
"grace": {
    "term": "Grace",
    "category": "concepts",
    "intro": "<p>Grace (Hebrew <em>ḥēn</em>; Greek <em>charis</em>) is the unmerited favor and free, sovereign benevolence of God toward undeserving sinners, standing at the center of both Old and New Testament soteriology. In the OT, grace first appears with Noah, who \"found grace in the eyes of the LORD\" (Gen. 6:8), and is expressed in God's covenant faithfulness to an undeserving people. The classic proclamation of divine grace is God's self-revelation to Moses: \"The LORD, the LORD God, merciful and gracious, longsuffering, and abundant in goodness and truth\" (Ex. 34:6). In the New Testament, grace reaches its fullest expression in the incarnation: \"The Word became flesh and dwelt among us, full of grace and truth\" (John 1:14). Paul makes grace foundational to his gospel: salvation is \"by grace through faith, not of works\" (Eph. 2:8–9), ensuring that God alone receives glory. Grace is distinguished from law (John 1:17; Rom. 6:14–15), from works (Rom. 4:4; 11:6), and from merit. It is not merely God's attitude but his active power enabling repentance, faith, sanctification, and final perseverance.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grace", "smith": "grace", "isbe": "grace"},
    "key_refs": ["Genesis 6:8", "Exodus 34:6", "John 1:14", "Ephesians 2:8"]
},
"grace-means-of": {
    "term": "Grace, Means of",
    "category": "concepts",
    "intro": "<p>\"Means of grace\" is a theological expression — not found in Scripture itself — designating those institutions ordained by God as the ordinary channels through which he conveys saving and sanctifying grace to human souls. Reformed and Lutheran theology identifies three primary means: (1.) the Word of God, both read and preached, which is \"living and active\" (Heb. 4:12) and able to make one \"wise for salvation\" (2 Tim. 3:15); (2.) the sacraments — baptism and the Lord's Supper — which are visible words that seal and apply the promises of the gospel; and (3.) prayer, through which the believer receives grace and communion with God. The concept guards against both a mechanical sacramentalism (where the rite automatically conveys grace apart from faith) and a purely individualist spirituality that bypasses the appointed instruments God has provided for his church.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grace-means-of"},
    "key_refs": ["Hebrews 4:12", "2 Timothy 3:15", "Matthew 28:19", "1 Corinthians 11:26"]
},
"graft": {
    "term": "Graft",
    "category": "concepts",
    "intro": "<p>Grafting, the horticultural process of inserting a branch or bud of one plant into another so that they unite and grow, is used by Paul in Romans 11 as an extended metaphor for the relationship between Jews and Gentiles in God's redemptive purposes. Paul describes the Gentile Christians as wild olive branches grafted into the cultivated olive tree of Israel (Rom. 11:17–24), while natural branches (unbelieving Israel) have been broken off. The metaphor is deliberately \"contrary to nature\" — normally one grafts cultivated shoots onto wild stock, not the reverse — which Paul acknowledges (11:24), making the point that God's inclusion of the Gentiles is a supernatural act of grace, not a natural development. The metaphor warns Gentile believers against arrogance toward Israel and sustains hope for Jewish restoration.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "graft"},
    "key_refs": ["Romans 11:17", "Romans 11:23", "Romans 11:24"]
},
"grain": {
    "term": "Grain",
    "category": "concepts",
    "intro": "<p>Grain in the biblical world referred primarily to wheat and barley, the staple crops of Palestine and the ancient Near East. Grain is used theologically in two principal metaphors. (1.) In Amos 9:9, God promises to sift Israel as grain is sifted in a sieve, ensuring that no true kernel falls to the ground. (2.) In Jesus' teaching, a grain of wheat falling into the earth and dying to bear much fruit (John 12:24) becomes the paradigm for his own death and resurrection and for the self-denying life of discipleship. The grain of mustard seed (Matt. 13:31) illustrates the surprising growth of the kingdom from small beginnings. Grain offerings (<em>minḥāh</em>) were a key element of the Levitical sacrificial system (Lev. 2), presented to God as an expression of dedication.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grain"},
    "key_refs": ["John 12:24", "Matthew 13:31", "Amos 9:9", "Leviticus 2:1"]
},
"grape": {
    "term": "Grape",
    "category": "concepts",
    "intro": "<p>Grapes (Hebrew <em>'ēnāb</em>) were one of the principal fruits of Canaan and the source of wine, vinegar, raisins, and grape juice. Viticulture features extensively in Scripture as a mark of the land's fertility: the spies brought back a single cluster so large it required two men to carry it on a pole (Num. 13:23). The vine and its fruit become rich symbols throughout the Bible: the vine represents Israel herself (Ps. 80:8–16; Isa. 5:1–7; Hos. 10:1), and Jesus applies the image to himself — \"I am the true vine\" (John 15:1). The blood of the grape was used in Passover celebrations, and Jesus instituted the Lord's Supper with the cup of the vine as the symbol of his blood of the new covenant (Matt. 26:27–29). The eschatological judgment is portrayed as a vintage where the grapes of wrath are trodden (Rev. 14:18–20; Isa. 63:1–6).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grape"},
    "key_refs": ["Numbers 13:23", "John 15:1", "Matthew 26:27", "Revelation 14:18"]
},
"grass": {
    "term": "Grass",
    "category": "concepts",
    "intro": "<p>Grass (Hebrew <em>ḥāṣîr</em>, <em>deše'</em>; Greek <em>chortos</em>) is a recurring biblical metaphor for the brevity and fragility of human life. The classic expression is Isaiah 40:6–8: \"All flesh is grass, and all the goodliness thereof is as the flower of the field: the grass withereth, the flower fadeth... but the word of our God shall stand for ever.\" This image is taken up in 1 Peter 1:24 and James 1:10–11. In contrast, Jesus' reference to God clothing \"the grass of the field\" (Matt. 6:30) grounds the argument for divine provision: if God so adorns what is temporary and common, how much more will he provide for his children? The rapid growth and withering of grass in the Near Eastern dry season makes it an apt illustration of human transience.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grass"},
    "key_refs": ["Isaiah 40:6", "Matthew 6:30", "1 Peter 1:24", "Psalms 103:15"]
},
"grasshopper": {
    "term": "Grasshopper",
    "category": "concepts",
    "intro": "<p>Grasshoppers and locusts are rendered by several Hebrew words in the Old Testament. As an image of smallness and insignificance, the ten faithless spies reported that Israel seemed like grasshoppers in comparison to the giant Canaanites (Num. 13:33). Isaiah uses the same image: the nations are \"as grasshoppers\" before God (Isa. 40:22). Certain species of locust were permitted as food in the Levitical code (Lev. 11:22), and John the Baptist ate locusts in the wilderness (Matt. 3:4). The locust invasion of Joel 1–2 is a central image of devastation and divine judgment. Qoheleth's lament that \"the grasshopper shall be a burden\" (Eccl. 12:5) is a metaphor for the frailty of old age.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grasshopper"},
    "key_refs": ["Numbers 13:33", "Isaiah 40:22", "Leviticus 11:22", "Ecclesiastes 12:5"]
},
"grate": {
    "term": "Grate",
    "category": "concepts",
    "intro": "<p>The grate was a network of bronze grating set into the altar of burnt offering in the tabernacle, halfway down from the top, beneath the ledge that projected around the altar's middle. Rings at the four corners of the grating held the poles used to carry the altar (Ex. 27:4–5; 38:4–5). The grating served a practical function: it held the fire and coals while allowing ash and fat to fall through below the ledge. The entire altar and its bronze grating were constructed according to God's specification given to Moses on the mountain, ensuring that the central place of Israel's worship was built exactly as directed.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grate"},
    "key_refs": ["Exodus 27:4", "Exodus 38:4"]
},
"grave": {
    "term": "Grave",
    "category": "concepts",
    "intro": "<p>Among the ancient Hebrews, graves were located outside cities in the open field or in hewn rock tombs (Luke 7:12; John 11:30). Kings and prominent persons were sometimes buried in the city itself (1 Kings 2:10; 1 Sam. 25:1). Graves were marked with pillars or stones (Gen. 35:20; 2 Kings 23:17) and their contact rendered a person ceremonially unclean under the Mosaic law (Num. 19:16; Matt. 23:27). The Hebrew word <em>sheol</em> and Greek <em>hades</em>, often translated \"grave\" in older English versions, more broadly denote the realm of the dead. The resurrection of Lazarus from his tomb (John 11:43–44) and Christ's own resurrection from the grave are the pivotal NT events that transform the grave's meaning for believers: death is no longer final, but the gateway to resurrection life (1 Cor. 15:54–55; Rev. 20:13).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grave"},
    "key_refs": ["Luke 7:12", "John 11:43", "1 Corinthians 15:55", "Revelation 20:13"]
},
"graven-image": {
    "term": "Graven Image",
    "category": "concepts",
    "intro": "<p>A graven image (Hebrew <em>pesel</em>) is a carved or sculpted idol — a representation of a deity shaped from wood, stone, or metal. The making and worshiping of graven images is explicitly prohibited in the second commandment (Ex. 20:4–5; Deut. 5:8–9) and is condemned throughout the prophets as the fundamental form of idolatry. Isaiah's extended satirical description of idol-making (Isa. 44:9–20) — where a man fells a tree, burns half for fire, and fashions the other half into a god — reduces the practice to absurdity. Graven images were to be utterly destroyed when Israel entered Canaan (Ex. 34:13; Deut. 7:5). The prohibition covers not only the making of images of foreign gods but also any image made to represent the God of Israel (Deut. 4:15–19), since God has no visible form and transcends all human representation.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "graven-image"},
    "key_refs": ["Exodus 20:4", "Deuteronomy 5:8", "Isaiah 44:17", "Psalms 97:7"]
},
"graving": {
    "term": "Graving",
    "category": "concepts",
    "intro": "<p>Graving refers to the art of engraving or incising designs into metal, stone, or wood — one of the skilled crafts employed in the construction of the tabernacle and temple. Bezalel was specifically gifted by God's Spirit for \"all manner of workmanship\" including graving in stone and wood (Ex. 31:5; 35:33). The high priest's breastplate featured twelve engraved stones, one for each tribe of Israel (Ex. 28:9–21), and the phrase \"Holiness to the LORD\" was engraved on the golden plate of his turban (Ex. 39:30). Seals bearing engraved names or symbols were used throughout the ancient Near East for authenticating documents and ownership marks. Isaiah 49:16's promise — \"I have graven thee upon the palms of my hands\" — uses the image of permanent inscription to express God's unfailing remembrance of his people.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "graving"},
    "key_refs": ["Exodus 31:5", "Exodus 28:9", "Isaiah 49:16"]
},
"greaves": {
    "term": "Greaves",
    "category": "concepts",
    "intro": "<p>Greaves were leg armor, typically of bronze, covering the shins from knee to ankle. They protected soldiers in hand-to-hand combat from sword cuts and spear thrusts at the lower leg. In the Old Testament, Goliath the Philistine warrior is specifically noted as wearing greaves of bronze (1 Sam. 17:6), part of the description of his formidable full military equipment that makes David's victory all the more remarkable. Greaves were standard equipment for Greek and Roman heavy infantry (hoplites and legionaries), and the term appears in ancient Near Eastern military catalogs. Paul's description of the believer's spiritual armor in Ephesians 6:10–17 parallels Roman military equipment but does not specifically mention greaves.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "greaves"},
    "key_refs": ["1 Samuel 17:6"]
},
"grecians": {
    "term": "Grecians",
    "category": "people",
    "intro": "<p>\"Grecians\" in the New Testament (Greek <em>Hellēnistai</em>) refers to Greek-speaking Jews of the Diaspora, as distinguished from \"Hebrews\" — Aramaic-speaking Palestinian Jews (Acts 6:1; 9:29). This linguistic and cultural distinction created tension in the early Jerusalem church: the Grecian widows were being overlooked in the daily food distribution, prompting the apostles to appoint seven deacons, most of whom bore Greek names, to address the need (Acts 6:1–6). Stephen and Philip were among these Hellenistic Jewish Christians. Paul engaged the Grecians (Hellenistic Jews) in the Jerusalem synagogues after his conversion (Acts 9:29). The term is to be distinguished from \"Greeks\" (<em>Hellēnes</em>), which typically refers to Gentile Greeks. The growing influence of Greek culture on diaspora Judaism, and the church's successful Hellenistic mission, were both shaped by this community.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "grecians", "isbe": "grecians"},
    "key_refs": ["Acts 6:1", "Acts 9:29", "Acts 11:20"]
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

print(f"BP g2: Gibeah → Grecians: wrote {wrote}, skipped {skipped} existing.")
