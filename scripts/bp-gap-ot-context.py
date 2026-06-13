"""
BP Article Synthesis — gap-ot-context: OT practices, law, places, and prophetic books
Covers 54 gap entries (score-10, OT-focused)
Sources consulted: data/smith/index.json, data/nave (nave-only items)
Script: scripts/bp-gap-ot-context.py
Run: python3 scripts/bp-gap-ot-context.py
"""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    path = os.path.join(OUT_DIR, slug + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None

def save_article(slug, data):
    path = os.path.join(OUT_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "angel-of-the-lord": {
        "term": "Angel of the Lord",
        "category": "concepts",
        "source_ids": {"smith": "angel-of-the-lord"},
        "key_refs": ["Genesis 16:7", "Exodus 3:2", "Judges 6:11", "Judges 13:22", "Zechariah 1:12"],
        "hitchcock_meaning": None,
        "intro": "<p>The Angel of the Lord (Hebrew <em>mal'ak YHWH</em>) appears in numerous Old Testament theophanies as a divine messenger who speaks and acts as God himself, receiving worship appropriate to God alone (Gen. 16:7-13; Ex. 3:2-6; Judg. 6:11-24). The figure is simultaneously identified with and distinguished from God: the Angel says 'I am the God of Bethel' (Gen. 31:13) and those who encounter him fear they have seen God face to face (Judg. 13:22). Many theologians identify the Angel of the Lord as a pre-incarnate Christophany — a visible appearance of the Son of God before the incarnation.</p><p>Smith's Dictionary notes that the formula 'the Angel of God' appears interchangeably with 'the Angel of the Lord' and that both designations apply to a being who is manifestly divine yet distinguishable from the Father. After the incarnation, 'angel of the Lord' in the NT refers to a created angelic being rather than this distinctive OT figure. The Angel of the Lord comforts Hagar (Gen. 16), calls to Abraham on Moriah (Gen. 22:11), guards Israel in the wilderness (Ex. 14:19), and commissions Gideon (Judg. 6:12) — making him the primary visible vehicle of God's direct presence with his people throughout the OT narrative.</p>"
    },
    "ass-donkey": {
        "term": "Ass (Donkey)",
        "category": "concepts",
        "source_ids": {"nave": "ass-donkey"},
        "key_refs": ["Genesis 22:3", "Numbers 22:28", "Zechariah 9:9", "Matthew 21:5", "Judges 5:10"],
        "hitchcock_meaning": None,
        "intro": "<p>The donkey (Hebrew <em>chamor</em>) was the principal beast of burden and riding animal in ancient Palestine, used for travel, agriculture, carrying loads, and grinding grain. Abraham saddled his donkey for the journey to Moriah (Gen. 22:3); Balaam rode his donkey until it was stopped by the Angel of the Lord (Num. 22:21-33), and the donkey was then given speech to rebuke its master — one of Scripture's most memorable episodes. The law protected working animals, prohibiting yoking an ox and donkey together (Deut. 22:10) and requiring rest on the Sabbath (Ex. 23:12).</p><p>Donkeys appear throughout OT history as the standard mount for persons of rank in times of peace — judges and elders rode white donkeys (Judg. 5:10; 10:4). The triumphal entry of Jesus into Jerusalem on a donkey's colt (Matt. 21:5-7; John 12:14-15) deliberately fulfilled Zechariah 9:9 — 'your king comes to you, righteous and having salvation, lowly and riding on a donkey' — contrasting the humble messianic king with the war-horse of conquering emperors. The donkey's associations with peace, humility, and common life make this fulfillment theologically precise.</p>"
    },
    "assyria-asshur": {
        "term": "Assyria (Asshur)",
        "category": "places",
        "source_ids": {"smith": "assyria-asshur"},
        "key_refs": ["Genesis 10:11", "2 Kings 15:29", "2 Kings 17:6", "Isaiah 10:5", "Nahum 1:1"],
        "hitchcock_meaning": None,
        "intro": "<p>Assyria was the great empire centered on the upper Tigris River (modern northern Iraq), founded by Asshur son of Shem (Gen. 10:11) and rising to dominate the ancient Near East from the ninth to seventh centuries BC. Its major cities — Nineveh, Calah (Nimrud), and Asshur — are among antiquity's most formidable urban centers, whose excavation has confirmed numerous biblical accounts. The Assyrian army was the most feared military force of the biblical world, deploying systematic siege warfare, mass deportation, and psychological terror.</p><p>Assyria is central to Hebrew prophecy: Jonah was sent to warn Nineveh of judgment; Isaiah called Assyria 'the rod of my anger' — God's instrument of discipline against Israel (Isa. 10:5); Nahum prophesied Nineveh's violent destruction; and Micah addressed the Assyrian invasion. Tiglath-pileser III (Pul) devastated the northern kingdom beginning in 734 BC (2 Kings 15:29; 1 Chr. 5:26); Sargon II completed the fall of Samaria in 722 BC, deporting approximately 27,000 Israelites (2 Kings 17:6). Sennacherib's siege of Jerusalem under Hezekiah ended in miraculous deliverance when 185,000 Assyrian troops were struck dead (2 Kings 19:35). Nineveh fell to the Babylonian-Median coalition in 612 BC.</p>"
    },
    "astarte": {
        "term": "Astarte",
        "category": "concepts",
        "source_ids": {"smith": "astarte"},
        "key_refs": ["Judges 2:13", "1 Samuel 7:3", "1 Kings 11:5", "2 Kings 23:13", "Jeremiah 44:17"],
        "hitchcock_meaning": None,
        "intro": "<p>Astarte (Hebrew <em>Ashtoreth</em>, plural <em>Ashtaroth</em>) was the principal female deity of the Phoenician and Canaanite pantheon — a goddess of fertility, love, sexuality, and war, identified with the planet Venus and cognate with the Babylonian Ishtar and the Egyptian Isis. She was the consort of Baal and was venerated across the ancient Near East under varying names and forms. Her cult involved ritual prostitution, fertility rites, and worship at shrines and high places with wooden cult objects (<em>Asherah</em> poles).</p><p>Israelites periodically abandoned YHWH to serve Baal and Ashtaroth, particularly during the period of the judges (Judg. 2:13; 10:6; 1 Sam. 7:3-4). Samuel called Israel to put away the Ashtaroth as a condition of covenant renewal (1 Sam. 7:3). Solomon built a high place for 'Ashtoreth the goddess of the Sidonians' under the influence of his foreign wives (1 Kings 11:5, 33), a syncretism that persisted until Josiah destroyed the high place during his reform (2 Kings 23:13). The Elijah narrative's confrontation at Mount Carmel implicitly targeted the Baal-Asherah cult that Jezebel had institutionalized in the northern kingdom.</p>"
    },
    "atonement-the-day-of": {
        "term": "Atonement, the Day of",
        "category": "concepts",
        "source_ids": {"smith": "atonement-the-day-of"},
        "key_refs": ["Leviticus 16:2", "Leviticus 23:27", "Hebrews 9:7", "Hebrews 9:12", "Hebrews 10:1"],
        "hitchcock_meaning": None,
        "intro": "<p>The Day of Atonement (Hebrew <em>Yom Kippur</em>) was the most solemn observance in the Hebrew calendar, observed on the tenth of Tishri (Lev. 16; 23:26-32). On this day alone the high priest entered the Most Holy Place, offering sacrifice first for his own sins, then for the nation's. He sprinkled blood from a sacrificed bull and goat seven times on the mercy seat of the ark, the throne of God's earthly presence. The day was observed as a complete fast — the only one commanded in the Mosaic law — with all work forbidden.</p><p>The scapegoat ritual gave the day its most vivid imagery: two goats were selected by lot; one was sacrificed and its blood used for atonement within the sanctuary; the other had the confessed sins of Israel symbolically laid upon it by the high priest and was then sent into the wilderness to 'Azazel,' representing the complete removal and banishment of the nation's sin. The Epistle to the Hebrews (chs. 9-10) develops the most sustained NT treatment of the Day of Atonement, presenting Christ's death as its definitive fulfillment: he entered not an earthly sanctuary made with hands but heaven itself, offering his own blood once for all rather than the yearly sacrifices that could never permanently remove sin (Heb. 9:12, 26; 10:1-14).</p>"
    },
    "balances": {
        "term": "Balances",
        "category": "concepts",
        "source_ids": {"smith": "balances"},
        "key_refs": ["Leviticus 19:36", "Deuteronomy 25:13", "Proverbs 11:1", "Amos 8:5", "Daniel 5:27"],
        "hitchcock_meaning": None,
        "intro": "<p>Balances (scales) were the standard instrument for commercial transactions throughout the ancient world, since standardized coinage was not introduced until the Persian period and even afterward metals were often weighed by weight. A typical balance consisted of a horizontal beam suspended from its center with pans on each end; stone or bronze weights on one side balanced the goods or metals on the other. The Mosaic law required honest weights and measures as an expression of covenant integrity: 'You shall have just balances, just weights, a just ephah, and a just hin' (Lev. 19:36; Deut. 25:13-16).</p><p>False balances — short-weighting buyers or manipulating weights to defraud — were condemned as abomination throughout Israel's moral literature: 'A false balance is an abomination to the LORD, but a just weight is his delight' (Prov. 11:1; Amos 8:5; Mic. 6:11). Archaeological finds have confirmed both the variety of ancient Near Eastern weights and evidence of deceptive practices. The phrase 'weighed in the balances and found wanting' in the handwriting at Belshazzar's feast (Dan. 5:27) transferred the commercial image into a metaphor for divine evaluation of moral and royal worth. The balance thus functioned as both a commercial tool and a moral symbol of divine justice.</p>"
    },
    "banquets": {
        "term": "Banquets",
        "category": "concepts",
        "source_ids": {"smith": "banquets"},
        "key_refs": ["Genesis 21:8", "1 Samuel 25:36", "Esther 1:3", "Isaiah 25:6", "Luke 14:16"],
        "hitchcock_meaning": None,
        "intro": "<p>Banquets and feasting occupied a central role in both the social and religious life of ancient Israel. Private banquets marked births and weanings (Gen. 21:8), betrothals and weddings (Gen. 29:22; John 2:1-11), sheep-shearing (1 Sam. 25:36), and royal occasions (1 Kings 3:15). The three great annual pilgrimage festivals — Passover, Weeks, and Tabernacles — required eating before God in a spirit of rejoicing, and the peace offering was consumed communally as a festive meal. In social terms, hosting a banquet expressed status, generosity, and covenant relationship.</p><p>The prophets employed banquet imagery in both critiques and promises. Amos condemned Israel's luxurious feasting accompanied by music as evidence of complacency toward injustice (Amos 6:4-7). Isaiah's vision of the eschatological banquet — 'a feast of rich food for all peoples, a banquet of aged wine' (Isa. 25:6-8) — became the foundational image of messianic blessing. Jesus used banquet parables extensively to describe the kingdom of heaven (Matt. 22:1-14; Luke 14:15-24), and his practice of table fellowship with sinners was a defining and controversial feature of his ministry. The Last Supper institutionalized a covenant meal — the Lord's Supper — as the central Christian act of communal worship.</p>"
    },
    "bathsheba-or-bathsheba": {
        "term": "Bathsheba",
        "category": "people",
        "source_ids": {"smith": "bathsheba-or-bathsheba"},
        "key_refs": ["2 Samuel 11:3", "2 Samuel 12:9", "1 Kings 1:28", "Matthew 1:6"],
        "hitchcock_meaning": None,
        "intro": "<p>Bathsheba, daughter of Eliam and wife of Uriah the Hittite, became the central figure in David's most serious moral failure. Her beauty, observed from the palace roof, led David to commit adultery with her while Uriah was on military campaign (2 Sam. 11:2-4). When she became pregnant, David arranged Uriah's death in battle to conceal the sin — a sequence of adultery and murder that the prophet Nathan confronted with the parable of a rich man who stole a poor man's single ewe lamb (2 Sam. 12:1-12). God's judgment through Nathan was direct: the sword would not depart from David's house, and the child of the adulterous union would die.</p><p>After the child's death, David married Bathsheba; their son Solomon was the one whom God declared he would love and establish (2 Sam. 12:24-25). Bathsheba exercised decisive political agency in David's final days, working with Nathan to secure Solomon's succession over Adonijah (1 Kings 1:11-31). As queen mother under Solomon, she continued to function as an intercessor and political figure (1 Kings 2:13-21). She is included by Matthew in the genealogy of Jesus as 'the wife of Uriah' (Matt. 1:6) — one of four women in the genealogy, each marking a place where God's grace overrode scandal to advance his purposes.</p>"
    },
    "beggar-begging": {
        "term": "Beggar; Begging",
        "category": "concepts",
        "source_ids": {"smith": "beggar-begging"},
        "key_refs": ["Deuteronomy 15:7", "Leviticus 19:9", "Acts 3:2", "Matthew 6:2", "Psalm 109:10"],
        "hitchcock_meaning": None,
        "intro": "<p>The Mosaic law addressed poverty through structural provisions rather than a formalized system of alms. The poor had the right to glean in fields, vineyards, and olive groves after the main harvest (Lev. 19:9-10; Deut. 24:19-21); to receive the third-year tithe (Deut. 14:28-29); and to borrow without interest from fellow Israelites (Ex. 22:25; Lev. 25:35-37). The Deuteronomic ideal was that 'there need be no poor among you' (Deut. 15:4) if the community practiced covenant generosity, though the realism of verse 11 — 'there will always be poor in the land' — acknowledges ongoing need.</p><p>Street begging as a visible practice became more prominent in the Second Temple period, when the blind, lame, and destitute positioned themselves at temple gates and city entrances to appeal for alms (Acts 3:2-3; John 9:8; Mark 10:46). Almsgiving was a recognized pillar of Jewish piety alongside prayer and fasting (Tob. 12:8). Jesus's teaching emphasized quiet generosity without public display (Matt. 6:2-4), and his healings of beggars were understood as fulfillments of Isaiah's messianic signs (Matt. 11:5). The apostolic community's care for the poor became a defining mark of early Christian communal life (Acts 2:44-45; Gal. 2:10).</p>"
    },
    "benjamin-the-tribe-of": {
        "term": "Benjamin, the Tribe of",
        "category": "people",
        "source_ids": {"smith": "benjamin-the-tribe-of"},
        "key_refs": ["Genesis 49:27", "Joshua 18:11", "Judges 20:46", "1 Samuel 9:21", "Philippians 3:5"],
        "hitchcock_meaning": None,
        "intro": "<p>The tribe of Benjamin, descended from Jacob's youngest son, occupied a small but strategically crucial territory in Canaan — bounded by Judah to the south, Ephraim to the north, and the Jordan to the east. Its allotment included the site of Jerusalem's immediate environs and cities of great military and religious significance including Gibeah, Mizpah, and Bethel (Josh. 18:11-28). Despite its small size, Jacob's blessing described Benjamin as 'a ravenous wolf' (Gen. 49:27), and the tribe was celebrated for warlike ferocity, particularly its ambidextrous slingers and archers (Judg. 20:16; 1 Chr. 12:2).</p><p>Benjamin produced Israel's first king, Saul son of Kish (1 Sam. 9:21), whose father's tribe acknowledged the unlikelihood: 'the smallest of all the tribes of Israel.' The civil war following the Gibeah atrocity (Judg. 19-21) nearly extinguished the tribe — only 600 men survived — requiring emergency intermarriage provision. After the division of the kingdom, Benjamin remained loyal to the Davidic dynasty and joined Judah in forming the southern kingdom (1 Kings 12:21; 2 Chr. 11:12). The apostle Paul identified himself as 'of the tribe of Benjamin, a Hebrew of Hebrews' (Phil. 3:5; Rom. 11:1), citing his tribal lineage as evidence of his unimpeachable Israelite credentials.</p>"
    },
    "bereavement": {
        "term": "Bereavement",
        "category": "concepts",
        "source_ids": {"nave": "bereavement"},
        "key_refs": ["2 Samuel 1:12", "Job 1:20", "John 11:35", "1 Thessalonians 4:13", "Romans 12:15"],
        "hitchcock_meaning": None,
        "intro": "<p>Biblical responses to bereavement — the loss of loved ones through death — encompassed formal mourning customs, communal solidarity, and profound theological reflection. Hebrew mourning rites included tearing garments (Gen. 37:34; 2 Sam. 1:11-12), wearing sackcloth, placing dust or ashes on the head, fasting, weeping loudly, and going barefoot. The community was expected to gather around the bereaved and provide comfort through presence and food (2 Sam. 3:35; Jer. 16:7). Professional mourning women were sometimes hired to lead the community's lamentation (Jer. 9:17-18; Amos 5:16).</p><p>The Psalms of lament provided a liturgical resource for processing grief before God with honest expression of pain, loss, and complaint alongside petition and trust (Ps. 22; 88). Job's response to the loss of his children — 'The LORD gave, and the LORD has taken away; blessed be the name of the LORD' (Job 1:21) — while exemplary in its theological orientation, does not suppress grief. Jesus's weeping at the tomb of Lazarus (John 11:35) legitimizes grief as a fully human response consistent with faith, even when resurrection is anticipated. Paul instructs believers not to grieve 'as others do who have no hope' (1 Thess. 4:13) — not prohibiting grief but grounding it in the resurrection hope — and calls the community to 'weep with those who weep' (Rom. 12:15) as an expression of genuine solidarity.</p>"
    },
    "betrothing": {
        "term": "Betrothing",
        "category": "concepts",
        "source_ids": {"smith": "betrothing"},
        "key_refs": ["Deuteronomy 22:23", "Matthew 1:18", "Matthew 1:20", "Hosea 2:19", "2 Corinthians 11:2"],
        "hitchcock_meaning": None,
        "intro": "<p>Biblical betrothal functioned as a binding legal contract between families that conferred the full legal status of marriage even before cohabitation began. A betrothed woman was legally called a 'wife,' and unfaithfulness during betrothal was treated as adultery with its corresponding penalties (Deut. 22:23-24). The betrothal agreement was typically made by the fathers of the couple and involved payment of a bride-price (<em>mohar</em>) to the bride's family as formal ratification. In later Second Temple practice a formal declaration before witnesses could also serve.</p><p>The betrothal period — customarily about a year — served to allow preparation of the couple's dwelling while the bride remained in her father's house. Joseph's discovery of Mary's pregnancy during their betrothal (Matt. 1:18-19) placed him in a legally precise dilemma: she had technically violated what was legally equivalent to marriage, making him entitled to a formal divorce proceeding. Joseph's decision to 'put her away quietly' (Matt. 1:19) rather than pursue public legal process reflects his righteousness and mercy before the angelic revelation clarified the situation. The NT also uses betrothal as a metaphor for the church's relationship to Christ, presenting Paul as a matchmaker who presented the Corinthian church 'as a pure virgin to her one husband' (2 Cor. 11:2).</p>"
    },
    "blood-revenger-of": {
        "term": "Blood, Revenger of",
        "category": "concepts",
        "source_ids": {"smith": "blood-revenger-of"},
        "key_refs": ["Numbers 35:19", "Numbers 35:24", "Deuteronomy 19:6", "Joshua 20:3", "Hebrews 6:18"],
        "hitchcock_meaning": None,
        "intro": "<p>The blood avenger (Hebrew <em>go'el haddam</em>, 'redeemer of blood') was the nearest male kinsman authorized and obligated under ancient Semitic customary law to kill the person responsible for a relative's death. The institution of blood vengeance expressed the deep conviction that a murdered person's blood 'cried out' from the ground for justice (Gen. 4:10) and that the obligation to answer that cry fell upon the family. Mosaic law acknowledged this institution while significantly modifying it to prevent unlimited cycles of revenge.</p><p>Numbers 35:9-28 and Deuteronomy 19:1-13 established six cities of refuge to which a person who had killed accidentally could flee before the blood avenger overtook them. A congregation would adjudicate: if the death was ruled premeditated murder, the slayer received no protection; if accidental manslaughter, the slayer could remain in the city of refuge until the death of the reigning high priest, after which he could return home free from the avenger's claim. Leaving the city of refuge before the high priest's death removed all protection. This system institutionalized due process, protecting the innocent from vendetta while maintaining the moral weight of human life. The writer of Hebrews uses the imagery of the city of refuge to describe the certainty available to Christians who 'flee for refuge' to the hope set before them in Christ (Heb. 6:18).</p>"
    },
    "booths": {
        "term": "Booths",
        "category": "concepts",
        "source_ids": {"smith": "booths"},
        "key_refs": ["Leviticus 23:40", "Leviticus 23:43", "Nehemiah 8:17", "Zechariah 14:16", "John 7:2"],
        "hitchcock_meaning": None,
        "intro": "<p>Booths (<em>sukkot</em>) were the temporary shelters of leafy branches — constructed from palm fronds, willow, myrtle, and other foliage — in which Israelites were commanded to dwell for seven days during the Feast of Tabernacles (Lev. 23:39-44). All native Israelites were to leave their permanent houses and live in these booths, commemorating the forty years their ancestors dwelt in temporary shelters in the wilderness following the Exodus from Egypt (Lev. 23:43). Nehemiah's restoration of the feast after the exile — for the first time since Joshua's day — involved the people constructing booths on rooftops, in courtyards, and in the temple precincts (Neh. 8:14-17).</p><p>The feast began on the fifteenth of Tishri, immediately following the Day of Atonement, and was accompanied by water-libation ceremonies and great illumination of the temple courts in Second Temple practice. Jesus's attendance at the feast (John 7:2, 14, 37) provided the occasion for his declaration on the great day of the feast that rivers of living water would flow from those who believed in him (John 7:37-39). Zechariah's eschatological vision requires all nations to come to Jerusalem annually to celebrate the Feast of Booths, and any nation that refuses will receive no rain (Zech. 14:16-19) — anchoring the feast in the final restoration of creation.</p>"
    },
    "burial-sepulchres": {
        "term": "Burial; Sepulchres",
        "category": "concepts",
        "source_ids": {"smith": "burial-sepulchres"},
        "key_refs": ["Genesis 23:19", "2 Samuel 2:32", "Isaiah 53:9", "Matthew 27:60", "Acts 2:29"],
        "hitchcock_meaning": None,
        "intro": "<p>Hebrew burial customs were shaped by respect for the body, the importance of family solidarity, and the significance of the ancestral burial plot as a permanent family possession. The preferred burial form was a rock-cut tomb or natural cave sealed with a large stone; prompt burial — ideally on the day of death — was important (Deut. 21:23; Acts 5:6-10). Exposure of a corpse was the gravest indignity, and to die without proper burial was a mark of divine judgment (Jer. 22:18-19; Isa. 14:19-20).</p><p>Abraham's purchase of the Cave of Machpelah as a permanent family burial place (Gen. 23) established the paradigm: the patriarchs treated burial rights as a matter of covenant importance. Royal burial in the 'tombs of the kings' in the City of David was an honor, and denial of royal burial was a sign of rejection (1 Kings 2:10; 2 Kings 9:28). Tombs were whitewashed annually before Passover to warn travelers of potential ritual defilement from contact with bones — a practice Jesus used as a metaphor for the Pharisees' outward righteousness concealing inner corruption (Matt. 23:27). Jesus's burial in a new, rock-cut tomb owned by Joseph of Arimathea fulfilled Isaiah's prophecy that he would be 'with the rich in his death' (Isa. 53:9) and established the empty tomb as the site of resurrection proclamation.</p>"
    },
    "canaan-the-land-of": {
        "term": "Canaan, the Land of",
        "category": "places",
        "source_ids": {"smith": "canaan-the-land-of"},
        "key_refs": ["Genesis 15:18", "Genesis 17:8", "Leviticus 18:24", "Joshua 1:4", "Acts 13:19"],
        "hitchcock_meaning": None,
        "intro": "<p>Canaan was the ancient name for the land west of the Jordan River and Dead Sea, stretching from the Euphrates in the north to the Sinai desert in the south — the territory promised by God to Abraham and his descendants as an everlasting possession (Gen. 15:18-21; 17:8). The name appears in Egyptian sources (the Amarna letters) and cuneiform tablets before the Israelite conquest, denoting both the land and its inhabitants. Its etymology may relate to the Semitic root for 'lowland' or to the purple-dye trade (<em>kinahhu</em> in Akkadian).</p><p>The Canaanite city-state culture encountered by Joshua was a polytheistic Bronze Age civilization. Mosaic law presents the conquest as delayed divine judgment on a society whose wickedness had 'filled up' over four generations (Gen. 15:16; Lev. 18:24-28): child sacrifice to Moloch, cult prostitution, divination, and sorcery are cited as the Canaanites' practices that the land itself 'vomited out.' The theological tension between the promised gift of the land and the command to displace its inhabitants runs throughout Joshua-Judges, and the gradual absorption rather than expulsion of remaining Canaanites becomes a persistent source of religious syncretism. Paul summarizes the entire process concisely in Acts 13:19.</p>"
    },
    "canaanites-the": {
        "term": "Canaanites, the",
        "category": "people",
        "source_ids": {"smith": "canaanites-the"},
        "key_refs": ["Genesis 10:15", "Genesis 15:16", "Deuteronomy 7:1", "Joshua 3:10", "Judges 1:27"],
        "hitchcock_meaning": None,
        "intro": "<p>The Canaanites were the pre-Israelite inhabitants of the land west of the Jordan, descended in the biblical genealogy from Canaan son of Ham (Gen. 10:15-19). The term functions both narrowly (one of the seven peoples of Canaan: Hittites, Girgashites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites — Deut. 7:1) and broadly (all inhabitants of the land). Their religion centered on Baal the storm god, Asherah the fertility goddess, and Astarte, with worship practices including child sacrifice, sacred prostitution, and divination.</p><p>The Mosaic command to utterly destroy the Canaanites (Deut. 7:1-5; 20:16-18) is grounded explicitly in two concerns: the danger of Israelite religious contamination through intermarriage ('they will turn your sons away from following me to serve other gods' — Deut. 7:4) and the execution of divine judgment on a society whose sin had reached full measure after centuries of warning (Gen. 15:16). The command's moral dimensions have generated sustained theological discussion from ancient times. Its practical outworking in Judges 1-2 shows incomplete fulfillment, and the remaining Canaanites became exactly the religious snare the law predicted (Judg. 2:11-13). Rahab and the Gibeonites represent individual Canaanites who sought covenant inclusion and received it.</p>"
    },
    "captivities-of-the-jews": {
        "term": "Captivities of the Jews",
        "category": "events",
        "source_ids": {"smith": "captivities-of-the-jews"},
        "key_refs": ["2 Kings 17:6", "2 Kings 24:14", "2 Kings 25:11", "Ezra 1:1", "Jeremiah 29:1"],
        "hitchcock_meaning": None,
        "intro": "<p>The captivities of the Jewish people unfolded across two centuries of Assyrian and Babylonian imperial expansion. The Assyrian phase began with Tiglath-pileser III's deportations from the northern kingdom's northern and eastern territories in 734-732 BC (2 Kings 15:29; 1 Chr. 5:26), continued with Shalmaneser V's siege of Samaria, and culminated in Sargon II's fall of Samaria in 722 BC and the deportation of approximately 27,000 Israelites, replaced by peoples from Babylon, Cuthah, Avva, Hamath, and Sepharvaim (2 Kings 17:3-6, 24). This effectively ended the northern kingdom.</p><p>The Babylonian captivity of Judah occurred in three deportations under Nebuchadnezzar: 605 BC (including Daniel and companions — Dan. 1:1-3), 597 BC (including King Jehoiachin, Ezekiel, and approximately 10,000 leading citizens — 2 Kings 24:10-16), and 586 BC (the destruction of Jerusalem and the temple, and deportation of the remainder — 2 Kings 25:8-12). The exile ended with Cyrus the Great's decree in 538 BC permitting return (Ezra 1:1-4; Isa. 44:28), fulfilled in the stages of return led by Zerubbabel, Ezra, and Nehemiah. The exile profoundly reshaped Jewish theology, produced major prophetic and wisdom literature, and established the synagogue as an institution for worship without a temple.</p>"
    },
    "care": {
        "term": "Care",
        "category": "concepts",
        "source_ids": {"nave": "care"},
        "key_refs": ["Matthew 6:25", "Philippians 4:6", "1 Peter 5:7", "Psalm 55:22", "Luke 12:22"],
        "hitchcock_meaning": None,
        "intro": "<p>Care and anxiety in Scripture are addressed both as natural human experiences and as invitations to deeper trust in God. The psalmists regularly bring their burdens and cares to God in frank prayer (Ps. 55:22; 62:8; 142:2), modeling the candid deposit of anxiety before God as an act of faith rather than stoic suppression. The wisdom literature acknowledges anxiety as part of the human condition: 'Anxiety in a man's heart weighs him down, but a good word makes him glad' (Prov. 12:25).</p><p>Jesus's extended teaching on anxiety in the Sermon on the Mount (Matt. 6:25-34) and its parallel in Luke 12:22-31 address material anxiety about food, drink, and clothing, grounding freedom from worry in the reality of God as Father who knows his children's needs and provides for his creatures. The argument moves from creation (birds, flowers) to covenant: if God clothes the grass, how much more will he clothe those made in his image? Peter's direct imperative — 'cast all your anxieties on him, because he cares for you' (1 Pet. 5:7) — personalizes this teaching. Paul's promise that divine peace 'which surpasses all understanding' will guard the heart and mind comes in the context of prayer as the channel through which cares become peace (Phil. 4:6-7). The NT consistently treats anxiety not as sin to suppress but as the occasion for prayer, trust, and communion with God.</p>"
    },
    "chaldeans-or-chaldees": {
        "term": "Chaldeans (Chaldees)",
        "category": "people",
        "source_ids": {"smith": "chaldeans-or-chaldees"},
        "key_refs": ["Genesis 11:28", "Job 1:17", "Isaiah 47:1", "Jeremiah 25:12", "Daniel 2:2"],
        "hitchcock_meaning": None,
        "intro": "<p>The Chaldeans (Hebrew <em>Kasdim</em>) were a Semitic people who settled in the marshy lowlands of southern Mesopotamia (ancient Chaldea) and eventually seized control of Babylon, establishing the Neo-Babylonian Empire under Nabopolassar (626-605 BC) and his son Nebuchadnezzar II (605-562 BC). Under Nebuchadnezzar, the Chaldean empire reached its greatest extent, conquering Jerusalem, destroying the temple, and carrying Judah into exile — events that define a major portion of the OT prophetic corpus.</p><p>The term 'Chaldean' appears in Daniel as a designation for an elite scholarly and priestly caste skilled in astrology, divination, and sacred learning (Dan. 2:2; 4:7; 5:7), reflecting the specialization of Babylonian intellectual life. The biblical references to 'Ur of the Chaldees' as Abraham's hometown (Gen. 11:28, 31; 15:7; Acts 7:4) use a term that is technically anachronistic for the early second millennium BC, either reflecting later scribal updating or an earlier presence of Chaldean groups in southern Mesopotamia than the historical record currently documents. Jeremiah prophesied the Chaldean empire's judgment and fall (Jer. 25:12; 50-51), fulfilled when Cyrus of Persia conquered Babylon in 539 BC.</p>"
    },
    "charitableness": {
        "term": "Charitableness",
        "category": "concepts",
        "source_ids": {"nave": "charitableness"},
        "key_refs": ["Leviticus 19:9", "Deuteronomy 15:10", "Luke 10:33", "2 Corinthians 9:7", "1 John 3:17"],
        "hitchcock_meaning": None,
        "intro": "<p>Charitableness — generous and kind concern for the vulnerable and the poor — is a consistent ethical demand embedded in both the structure of Mosaic law and the explicit commands of the prophets and apostles. The law wove provision for the poor into the agricultural economy through gleaning rights (Lev. 19:9-10; Deut. 24:19-21), the third-year tithe for the poor and alien (Deut. 14:28-29), interest-free loans to impoverished Israelites (Ex. 22:25; Lev. 25:35-37), and the Sabbatical debt release (Deut. 15:1-11). The Deuteronomic command is explicit: 'You shall open wide your hand to your brother, to the needy and to the poor' (Deut. 15:11).</p><p>The prophets made care for the poor a defining test of authentic covenant faithfulness: true fasting is to 'share your bread with the hungry and bring the homeless poor into your house' (Isa. 58:6-7), and Micah summarizes the whole law as 'to do justice, to love kindness (<em>hesed</em>), and to walk humbly with your God' (Mic. 6:8). Jesus extended neighborliness to include enemies through the parable of the Good Samaritan (Luke 10:25-37). The NT epistles make love of the poor a test of genuine faith: 'If anyone has the world's goods and sees his brother in need, yet closes his heart against him, how does God's love abide in him?' (1 John 3:17). Paul calls for cheerful, generous giving as a participation in God's own grace (2 Cor. 9:7-8).</p>"
    },
    "chastisement": {
        "term": "Chastisement",
        "category": "concepts",
        "source_ids": {"nave": "chastisement"},
        "key_refs": ["Proverbs 3:11", "Hebrews 12:6", "Deuteronomy 8:5", "Revelation 3:19", "2 Corinthians 12:7"],
        "hitchcock_meaning": None,
        "intro": "<p>Chastisement (divine discipline) is a consistent biblical theme expressing God's fatherly correction of his people through adversity, suffering, and consequence. Proverbs establishes the principle at the level of human parenting: 'My son, do not despise the LORD's discipline or be weary of his reproof, for the LORD reproves him whom he loves, as a father the son in whom he delights' (Prov. 3:11-12). Deuteronomy applies the same pattern to Israel's wilderness testing: 'Know then in your heart that, as a man disciplines his son, the LORD your God disciplines you' (Deut. 8:5).</p><p>The Epistle to the Hebrews develops the most sustained NT theology of divine discipline, quoting Proverbs 3:11-12 and arguing that the Christian's experience of hardship is evidence of sonship rather than divine abandonment: 'For the Lord disciplines the one he loves, and chastises every son whom he receives... God is treating you as sons' (Heb. 12:6-7). Discipline is presented as purposeful rather than arbitrary — producing 'the peaceful fruit of righteousness to those who have been trained by it' (Heb. 12:11). Christ's word to the Laodicean church — 'Those whom I love, I reprove and discipline' (Rev. 3:19) — applies the same principle to congregational rebuke. Paul's thorn in the flesh (2 Cor. 12:7) illustrates how divine discipline and gift can be paradoxically intertwined.</p>"
    },
    "chedorlaomer-or-chedorlaomer": {
        "term": "Chedorlaomer",
        "category": "people",
        "source_ids": {"smith": "chedorlaomer-or-chedorlaomer"},
        "key_refs": ["Genesis 14:1", "Genesis 14:9", "Genesis 14:17"],
        "hitchcock_meaning": None,
        "intro": "<p>Chedorlaomer, king of Elam, was the dominant member of the coalition of four kings who subjugated the five kings of the Sodom plain for twelve years before their rebellion in the thirteenth year (Gen. 14:1-9). His name appears to derive from Elamite elements, and the coalition's composition — Elam, Shinar, Ellassar, and Goiim — reflects political geography consistent with the early second millennium BC, when Elamite power over Mesopotamia is historically attested. No certain cuneiform identification has been established, though scholars have proposed various correspondences.</p><p>When the five Canaanite kings rebelled in the fourteenth year, Chedorlaomer's coalition defeated them in the Valley of Siddim and took plunder and captives including Lot, Abraham's nephew. Abraham's response was decisive: pursuing the coalition northward with 318 trained men, he routed them near Dan and recovered Lot, the captives, and the goods (Gen. 14:14-16). The episode established Abraham's military capacity and prestige among the kings of Canaan. The subsequent encounter with Melchizedek king of Salem, who blessed Abraham and received a tithe (Gen. 14:18-20), became theologically foundational for the Epistle to the Hebrews' treatment of Christ's priesthood after the order of Melchizedek (Ps. 110:4; Heb. 7).</p>"
    },
    "cherubim": {
        "term": "Cherubim",
        "category": "concepts",
        "source_ids": {"nave": "cherubim"},
        "key_refs": ["Genesis 3:24", "Exodus 25:18", "Ezekiel 10:15", "Revelation 4:6", "Psalms 80:1"],
        "hitchcock_meaning": None,
        "intro": "<p>Cherubim were angelic beings of the highest rank associated with the immediate presence and glory of God, depicted throughout Scripture as guardians of sacred thresholds and bearers of the divine throne-chariot. After the expulsion from Eden, God stationed cherubim with a flaming, turning sword at the entrance to the garden to guard the way to the tree of life (Gen. 3:24). Two golden cherubim overshadowed the ark of the covenant in the Most Holy Place (Ex. 25:18-22), their wings spread above the mercy seat — the earthly throne between which God was said to dwell and be enthroned (1 Sam. 4:4; 2 Sam. 6:2; Ps. 80:1).</p><p>Ezekiel's inaugural vision (ch. 1) and later temple vision (ch. 10) describe four living creatures with four faces (human, lion, ox, eagle) who bear God's chariot-throne; these are explicitly identified as cherubim in Ezekiel 10:15-20. The tabernacle veil and the temple walls and doors were decorated with images of cherubim (Ex. 26:31; 1 Kings 6:29-35), making their presence a defining feature of sacred space. In Revelation, the four living creatures surrounding the divine throne (Rev. 4:6-8), crying 'Holy, holy, holy' in perpetual worship, echo and fulfill the Ezekielian cherubic imagery. Cherubim thus frame the entire biblical narrative — from the gate of Eden to the throne of the Lamb.</p>"
    },
    "children": {
        "term": "Children",
        "category": "concepts",
        "source_ids": {"smith": "children"},
        "key_refs": ["Psalms 127:3", "Deuteronomy 6:7", "Proverbs 22:6", "Matthew 18:3", "Ephesians 6:1"],
        "hitchcock_meaning": None,
        "intro": "<p>Children were highly valued in biblical society as evidence of God's blessing; the birth of sons especially was celebrated (Gen. 33:5; Ps. 127:3-5; 128:3-4). Barrenness was a source of deep anguish and social stigma in a culture where family continuity and God's blessing were expressed through offspring — the stories of Sarah, Rachel, Hannah, and Elizabeth each feature divine intervention ending barrenness as a demonstration of God's power over natural limitation. Male children were circumcised on the eighth day as the sign of covenant membership (Gen. 17:12). The firstborn son held the birthright of double inheritance and special consecration to God (Ex. 13:2).</p><p>Parents bore primary responsibility for religious formation: 'You shall teach them diligently to your children, and shall talk of them when you sit in your house, and when you walk by the way, and when you lie down, and when you rise' (Deut. 6:7). Proverbs addresses parental discipline as an expression of love (Prov. 13:24; 22:6; 29:15). Jesus gave children remarkable theological prominence — presenting childlike trust and dependence as the paradigm of kingdom entry (Matt. 18:3; 19:14) and rebuking disciples who tried to prevent children's access to him. Paul's household codes address children directly as moral agents with obligations before the Lord (Eph. 6:1-3; Col. 3:20).</p>"
    },
    "chronicles-first-and-second-books-of": {
        "term": "Chronicles, First and Second Books of",
        "category": "concepts",
        "source_ids": {"smith": "chronicles-first-and-second-books-of"},
        "key_refs": ["1 Chronicles 17:14", "1 Chronicles 22:5", "2 Chronicles 7:14", "2 Chronicles 36:22", "Ezra 1:1"],
        "hitchcock_meaning": None,
        "intro": "<p>The Books of Chronicles, originally one composition in the Hebrew canon (divided in the LXX), retell Israel's history from Adam (via genealogies — 1 Chr. 1-9) through the edict of Cyrus permitting the return from exile (2 Chr. 36:22-23). The Chronicler focuses almost exclusively on the Davidic dynasty and the Jerusalem temple, largely omitting the northern kingdom's independent history. Written for the post-exilic community returning from Babylon, the work emphasizes the centrality of temple worship, the Levitical personnel and their duties, and the conditional nature of the covenant: 'If my people who are called by my name humble themselves and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land' (2 Chr. 7:14).</p><p>The Chronicler supplements Samuel-Kings with material found nowhere else: David's extensive preparations for the temple (1 Chr. 22-29), detailed Levitical organization, and accounts of religious revivals under Jehoshaphat, Hezekiah, and Josiah. Where Samuel-Kings evaluates kings politically and militarily, Chronicles evaluates them primarily by their fidelity to temple worship and Levitical order. The repetition of God's covenant promise to David (1 Chr. 17) and the elaborate worship preparations express the Chronicler's conviction that the restored community stands in unbroken continuity with the Davidic covenant and that right worship is the foundation of national renewal.</p>"
    },
    "civil-service": {
        "term": "Civil Service",
        "category": "concepts",
        "source_ids": {"nave": "civil-service"},
        "key_refs": ["Romans 13:1", "1 Peter 2:13", "Daniel 6:4", "Nehemiah 5:14", "Titus 3:1"],
        "hitchcock_meaning": None,
        "intro": "<p>The biblical material on civil service addresses both the obligations of those in governmental authority and the duties of subjects toward governing institutions. The Mosaic law provided comprehensive regulations for civil governance: kings were forbidden to multiply horses, wives, or gold (Deut. 17:16-17), were required to write a personal copy of the law and read it daily (Deut. 17:18-20), and were to administer justice without favoritism (Deut. 16:18-20). Judges and officials were to be appointed in every town and to pursue justice with complete impartiality (Deut. 16:18-19).</p><p>Daniel, Joseph, and Nehemiah provide models of faithful service within pagan or post-exilic governmental structures without compromising covenant loyalty. Daniel's administrators could find no corruption or negligence in him (Dan. 6:4). Nehemiah refused the governor's food allowance as an economic burden on the people (Neh. 5:14-18). The NT epistles teach submission to governing authorities as divinely ordered for the restraint of evil and the maintenance of order (Rom. 13:1-7; 1 Pet. 2:13-17; Titus 3:1), while Acts demonstrates that obedience to God supersedes human authority when the two conflict: 'We must obey God rather than men' (Acts 4:19; 5:29). Believers are called to pray for rulers (1 Tim. 2:1-2) and to be exemplary citizens where possible (1 Pet. 2:15).</p>"
    },
    "high-places": {
        "term": "High Places",
        "category": "concepts",
        "source_ids": {"nave": "high-places"},
        "key_refs": ["1 Samuel 9:12", "1 Kings 3:4", "2 Kings 18:4", "2 Kings 23:8", "Ezekiel 20:29"],
        "hitchcock_meaning": None,
        "intro": "<p>High places (Hebrew <em>bamot</em>) were elevated cult sites — natural hilltops, rocky outcrops, or artificially raised platforms — at which sacrifices, incense, and acts of worship were offered throughout the ancient Near East. Before the construction of the Jerusalem temple and the Deuteronomic principle of centralized worship, high places served as legitimate sites of Yahweh worship: Samuel sacrificed and ate with Saul at a high place (1 Sam. 9:12-14), and Solomon offered a thousand burnt offerings at the great high place at Gibeon (1 Kings 3:4). The tension between this older tradition and the Deuteronomic ideal of exclusive worship at the chosen place (Deut. 12:5-14) shapes the evaluations of Israelite kings across Samuel-Kings.</p><p>The standard formula for partial approval of Judean kings is that 'the high places were not removed' even when the king otherwise did what was right (1 Kings 15:14; 22:43; 2 Kings 12:3). High places dedicated to foreign deities were entirely condemned: Solomon built high places for Chemosh, Moloch, and Ashtoreth (1 Kings 11:7-8), and Ahab erected a Baal altar. Hezekiah's removal of the high places was a distinctive mark of his reform (2 Kings 18:4), but his successors restored them. Josiah's reform was the most thoroughgoing, destroying high places throughout both Judah and the former northern kingdom (2 Kings 23:8-20). After the exile, the high place system was not restored, and synagogue worship in local communities replaced the decentralized cult.</p>"
    },
    "isaiah-book-of": {
        "term": "Isaiah, Book of",
        "category": "concepts",
        "source_ids": {"smith": "isaiah-book-of"},
        "key_refs": ["Isaiah 1:1", "Isaiah 6:1", "Isaiah 53:4", "Isaiah 61:1", "Luke 4:18"],
        "hitchcock_meaning": None,
        "intro": "<p>The Book of Isaiah is the longest and most frequently cited of the Hebrew prophets, spanning sixty-six chapters. Chapters 1-39 address Judah's sin, the Assyrian crisis of the eighth century BC, and oracles concerning the surrounding nations, including the Immanuel prophecies (7:14; 9:6-7) and the vision of the divine throne (ch. 6). Chapters 40-55 ('Deutero-Isaiah' for many scholars) provide consolation for exiles in Babylon, announcing Cyrus as God's instrument (44:28; 45:1) and containing four Servant Songs of profound influence on NT Christology (42:1-4; 49:1-6; 50:4-9; 52:13-53:12). Chapters 56-66 address the restored community and envision the new creation.</p><p>The question of the book's compositional unity has divided scholars since the eighteenth century. Conservative interpreters cite the NT's uniform attribution of all sixty-six chapters to Isaiah son of Amoz (cf. John 12:38-41, quoting both halves), the continuity of themes and vocabulary, and the complete Isaiah Scroll from Qumran — which shows no break between chapters 39 and 40 — as evidence for single authorship. No OT book is quoted in the NT more frequently than Isaiah. Its portraits of the Suffering Servant (ch. 53), quoted in Acts 8:32-35 and applied extensively to the passion, and its vision of universal salvation and new creation, have made it the 'Fifth Gospel' in Christian theological tradition.</p>"
    },
    "jubilee-the-year-of": {
        "term": "Jubilee, the Year of",
        "category": "concepts",
        "source_ids": {"smith": "jubilee-the-year-of"},
        "key_refs": ["Leviticus 25:10", "Leviticus 25:23", "Isaiah 61:1", "Luke 4:18", "Leviticus 25:13"],
        "hitchcock_meaning": None,
        "intro": "<p>The Year of Jubilee was proclaimed by the blast of a ram's horn (<em>jobel</em>, from which 'jubilee' derives) on the Day of Atonement of the forty-ninth year, initiating the fiftieth year as the great year of release (Lev. 25:8-55). Three concurrent reversals characterized the Jubilee: all ancestral land reverted to its original tribal owner regardless of how it had been sold or transferred; all Israelite slaves were freed regardless of how long remained in their term of service; and the land rested from agricultural labor. The theological foundation was radical: 'The land shall not be sold in perpetuity, for the land is mine. For you are strangers and sojourners with me' (Lev. 25:23).</p><p>Whether the Jubilee was systematically practiced in Israel's history remains uncertain; no clear historical instance appears in the narrative books. Its provisions represent a comprehensive structural counter to the permanent accumulation of land and wealth by a few families at the expense of the many — preserving the integrity of the tribal allotment. Jesus's inaugural reading in the Nazareth synagogue from Isaiah 61 — 'to proclaim the year of the Lord's favor' (Luke 4:18-19) — drew on the Jubilee's language of release and restoration to define his ministry as the inauguration of the ultimate divine Jubilee: liberation not from economic bondage alone but from sin, sickness, and death.</p>"
    },
    "judges": {
        "term": "Judges",
        "category": "concepts",
        "source_ids": {"smith": "judges"},
        "key_refs": ["Judges 2:16", "Judges 2:18", "Hebrews 11:32", "Acts 13:20", "1 Samuel 7:15"],
        "hitchcock_meaning": None,
        "intro": "<p>The judges of Israel were charismatic military deliverers raised by God during the period between Joshua's death and Saul's coronation (c. 1200-1050 BC). They were empowered by the Spirit of God to rescue Israel from oppressors (Judg. 2:16-18) and were neither hereditary rulers nor permanent governors — their authority was locally recognized and functionally limited to the crisis at hand. The Hebrew <em>shofet</em> encompasses both military leadership and judicial adjudication of disputes (as illustrated by Deborah, who held court under her palm tree — Judg. 4:4-5).</p><p>The Book of Judges is organized around a repeating theological cycle: Israel's apostasy to Canaanite deities → divine punishment through oppression → Israel's cry for help → God's raising of a deliverer → rest → relapse into apostasy and repetition of the cycle. The major judges receive extended narratives: Othniel, Ehud, Deborah and Barak, Gideon, Jephthah, and Samson. Twelve minor judges are listed with brief notices only. The book's trajectory is one of progressive moral and spiritual deterioration, culminating in the civil war of chapters 19-21 and the refrain 'everyone did what was right in his own eyes' (Judg. 17:6; 21:25). Hebrews 11:32-34 names Gideon, Barak, Samson, and Jephthah among the heroes of faith.</p>"
    },
    "judith-the-book-of": {
        "term": "Judith, the Book of",
        "category": "concepts",
        "source_ids": {"smith": "judith-the-book-of"},
        "key_refs": ["Judith 4:1", "Judith 8:1", "Judith 13:8"],
        "hitchcock_meaning": None,
        "intro": "<p>The Book of Judith is a work of the Apocrypha (Deuterocanon for Roman Catholics and Eastern Orthodox Christians), preserved in Greek though almost certainly composed in Hebrew or Aramaic, narrating the deliverance of the Jewish city of Bethulia from the Assyrian general Holofernes through the courageous action of the devout widow Judith. Her name, meaning 'Jewess,' marks her as a symbolic embodiment of faithful Israel under threat. After Holofernes besieged her city, Judith entered the enemy camp under the pretext of offering intelligence, gained Holofernes's trust, waited until he was drunk, and decapitated him with his own sword — causing the Assyrian army to panic and flee.</p><p>The book's historical framework contains deliberate anachronisms (Nebuchadnezzar called 'king of the Assyrians,' post-exilic realities described as if pre-exilic) that signal historical fiction rather than chronicle. Modern scholars generally date its composition to the Maccabean period (c. 150-100 BC), reading it as encouragement for Jewish resistance against Seleucid oppression. Its themes — trust in God's deliverance of the weak over the powerful, the courage of women, the futility of pride, and reversal of expectations — place it in the tradition of Esther and the Exodus narrative. The book is not included in the Hebrew Bible or Protestant canon but is regarded as Scripture in Catholic and Eastern Orthodox traditions.</p>"
    },
    "kenite-the": {
        "term": "Kenite, the",
        "category": "people",
        "source_ids": {"smith": "kenite-the"},
        "key_refs": ["Judges 1:16", "Judges 4:17", "Judges 4:21", "1 Samuel 15:6", "Jeremiah 35:2"],
        "hitchcock_meaning": None,
        "intro": "<p>The Kenites (Hebrew <em>Qeni</em>, possibly 'smith' or 'metalworker') were a seminomadic people who inhabited the rocky desert between southern Canaan and the Sinai Peninsula. Their earliest connection to Israel came through Moses, whose father-in-law Jethro (also called Reuel and Hobab) was a Midianite priest with apparent Kenite affiliations (Judg. 1:16; 4:11). Jethro's counsel on judicial organization (Ex. 18) and his blessing of God's work in the Exodus suggest a relationship of recognized kinship between Kenite and Israelite religion.</p><p>A Kenite family's role in the Deborah-Barak narrative is decisive: Heber the Kenite had separated from the main Kenite group and settled near Kedesh; when the Canaanite commander Sisera fled the battlefield and sought refuge in Heber's tent, Heber's wife Jael killed him with a tent peg (Judg. 4:17-22). The Song of Deborah celebrates Jael as 'most blessed of women' (Judg. 5:24). Saul warned the Kenites to separate themselves from the Amalekites before his attack, honoring their historical kindness to Israel during the wilderness period (1 Sam. 15:6). The Rechabites of Jeremiah 35, who maintained strict abstinence from wine and a nomadic lifestyle in obedience to their ancestor Jonadab, were of Kenite descent (1 Chr. 2:55).</p>"
    },
    "kings-first-and-second-books-of": {
        "term": "Kings, First and Second Books of",
        "category": "concepts",
        "source_ids": {"smith": "kings-first-and-second-books-of"},
        "key_refs": ["1 Kings 2:1", "1 Kings 11:1", "2 Kings 17:7", "2 Kings 23:25", "2 Kings 25:27"],
        "hitchcock_meaning": None,
        "intro": "<p>The Books of Kings, originally a single composition in the Hebrew canon (divided in the LXX), continue the Deuteronomistic History from Solomon's accession (1 Kings 1) through the fall of Jerusalem, the destruction of the temple, and the exile to Babylon (2 Kings 25:1-21), ending with a note on Jehoiachin's release from Babylonian prison (2 Kings 25:27-30). Every king of Israel and Judah is evaluated by a consistent standard derived from Deuteronomy: faithfulness to exclusive covenant worship at the Jerusalem temple, rejection of idolatry, and obedience to the Mosaic law.</p><p>The northern kingdom's kings are uniformly condemned for perpetuating Jeroboam's golden calves (1 Kings 12:28-33). Southern kings receive mixed evaluations; Hezekiah and Josiah are most highly commended for their reforms (2 Kings 18:5; 23:25). The narratives of Elijah and Elisha (1 Kings 17 – 2 Kings 13) provide the theological and narrative centerpiece of the work, illustrating prophetic confrontation with royal apostasy. The fall of Samaria (722 BC) is explained theologically as the result of covenant breach (2 Kings 17:7-23). The fall of Jerusalem (586 BC) confirms that the Deuteronomic covenant curses have taken full effect — yet Jehoiachin's liberation hints at God's continued faithfulness to the Davidic promise, the basis for post-exilic hope.</p>"
    },
    "knowledge": {
        "term": "Knowledge",
        "category": "concepts",
        "source_ids": {"nave": "knowledge"},
        "key_refs": ["Proverbs 1:7", "Hosea 4:6", "John 17:3", "Philippians 3:8", "Colossians 1:9"],
        "hitchcock_meaning": None,
        "intro": "<p>Knowledge in biblical usage encompasses both intellectual understanding and relational intimacy, reflecting the Hebrew <em>yadah</em> (to know), which is used for both cognitive apprehension and the deepest human relationship. 'The fear of the LORD is the beginning of knowledge' (Prov. 1:7) establishes reverence for God as the foundation of all genuine understanding, contrasting the biblical perspective with any claim to autonomous human reason as the arbiter of truth. Hosea indicts Israel for a lack of knowledge of God (Hos. 4:1, 6), treating it as covenant betrayal rather than intellectual deficiency.</p><p>The NT develops the theme further: eternal life is defined as knowing God and Jesus Christ (John 17:3), and Paul regards the surpassing worth of knowing Christ Jesus his Lord as the measure against which all other achievement is counted as loss (Phil. 3:8). The 'knowledge of God' (<em>epignosis</em>) is the goal toward which Paul prays his churches will grow (Col. 1:9-10; Eph. 1:17). The Gnostic overvaluation of esoteric spiritual knowledge as the key to salvation is addressed and countered in Colossians, the Pastoral Epistles, and the Johannine letters: John emphasizes that the test of knowing God is not esoteric wisdom but keeping his commandments and loving the brothers (1 John 2:3-4; 4:7-8).</p>"
    },
    "lamentations-of-jeremiah": {
        "term": "Lamentations of Jeremiah",
        "category": "concepts",
        "source_ids": {"smith": "lamentations-of-jeremiah"},
        "key_refs": ["Lamentations 1:12", "Lamentations 3:22", "Lamentations 3:23", "Lamentations 5:21", "2 Chronicles 35:25"],
        "hitchcock_meaning": None,
        "intro": "<p>The Book of Lamentations consists of five poems written in response to the destruction of Jerusalem and the temple by Babylon in 586 BC. The first four are acrostic poems following the twenty-two letters of the Hebrew alphabet — a literary form that imposes ordered structure on grief, suggesting that even catastrophic loss can be articulated within the boundaries of language. The fifth poem is a non-acrostic community prayer. Jewish tradition attributes the book to Jeremiah, the weeping prophet who predicted Jerusalem's destruction and mourned it (Jer. 9:1; 2 Chr. 35:25).</p><p>The laments describe the siege's horrors with unflinching realism — famine so severe that mothers cooked their children (Lam. 4:10), the desecration of the sanctuary, the humiliation of priests and elders. The book wrestles honestly with the question of how God could permit the destruction of his chosen city and dwelling place: 'Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow' (Lam. 1:12). The pivotal third chapter provides a turn toward hope within desolation: 'The steadfast love of the LORD never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness' (Lam. 3:22-23). Jewish communities recite Lamentations on Tisha B'Av, the fast commemorating the temple's destruction. Paul's language of consolation in 2 Corinthians echoes Lamentations' movement from grief to hope.</p>"
    },
    "leaven-yeast": {
        "term": "Leaven (Yeast)",
        "category": "concepts",
        "source_ids": {"nave": "leaven-yeast"},
        "key_refs": ["Exodus 12:15", "Leviticus 2:11", "Matthew 16:6", "1 Corinthians 5:7", "Matthew 13:33"],
        "hitchcock_meaning": None,
        "intro": "<p>Leaven (fermented dough or its culture, producing carbon dioxide that makes bread rise) carried complex and deliberately contrasting symbolic meanings across Scripture. The Passover observance required the complete removal of all leaven from Israelite homes for seven days (Ex. 12:15; 13:7), commemorating the haste of the Exodus when there was no time for bread to rise. No grain offering made by fire was to include leaven (Lev. 2:11), though leavened bread appeared in the peace offering wave-loaves (Lev. 7:13) and the Pentecost firstfruits offering (Lev. 23:17).</p><p>The NT deploys leaven in both negative and positive registers. Jesus warned against 'the leaven of the Pharisees and Sadducees' (Matt. 16:6-12; Luke 12:1) and 'the leaven of Herod' (Mark 8:15), metaphors for corrupting teaching and influence that permeates a community. Paul draws directly on Passover imagery: 'Purge out the old leaven that you may be a new lump, as you are unleavened. For Christ, our Passover lamb, has been sacrificed' (1 Cor. 5:7-8). Yet Jesus also used leaven as a positive image — the kingdom of heaven is like leaven hidden in three measures of flour, quietly leavening the whole (Matt. 13:33) — expressing the gospel's quiet, pervasive, transformative power throughout the world.</p>"
    },
    "lending": {
        "term": "Lending",
        "category": "concepts",
        "source_ids": {"nave": "lending"},
        "key_refs": ["Exodus 22:25", "Leviticus 25:36", "Deuteronomy 15:8", "Psalm 37:26", "Luke 6:35"],
        "hitchcock_meaning": None,
        "intro": "<p>Biblical teaching on lending was shaped by the tension between commercial reality and the covenant community's obligation to care for the poor. Mosaic law prohibited charging interest (<em>neshek</em>, 'bite') to a fellow Israelite who had fallen into poverty (Ex. 22:25; Lev. 25:35-37; Deut. 23:19), while permitting interest from foreigners in commercial transactions (Deut. 23:20). The prohibition reflected the conviction that lending to a poor covenant-brother should be an act of solidarity and mercy rather than profit-seeking.</p><p>Collateral regulations protected borrowers' dignity: a millstone could not be taken as a pledge since it was the family's means of food preparation (Deut. 24:6); a widow's garment was protected (Deut. 24:17); a poor man's cloak taken as security had to be returned by nightfall since it served as his only covering (Ex. 22:26-27; Deut. 24:12-13). The Sabbatical Year included release of debts owed by Israelites (Deut. 15:1-11), with the command that imminent Sabbatical release should not discourage lending: 'You shall give to him freely, and your heart shall not be grudging' (Deut. 15:10). The prophets condemned lending at usury to the poor as exploitation (Ezek. 18:8; Neh. 5:1-13). Jesus's teaching — 'lend, expecting nothing in return' (Luke 6:35) — radicalizes the Mosaic principle into unconditional generosity modeled on God's own giving.</p>"
    },
    "lot-the": {
        "term": "Lot, the",
        "category": "concepts",
        "source_ids": {"nave": "lot-the"},
        "key_refs": ["Proverbs 16:33", "Numbers 26:55", "Joshua 7:14", "Acts 1:26", "Leviticus 16:8"],
        "hitchcock_meaning": None,
        "intro": "<p>The casting of lots was the standard method for seeking divine decision on important matters in ancient Israel, understood as placing the outcome entirely under God's direct control: 'The lot is cast into the lap, but its every decision is from the LORD' (Prov. 16:33). The physical nature of the lots — whether stones, marked sticks, pottery fragments, or the Urim and Thummim — is not specified in most passages. Their use presupposed that God would direct the outcome to reveal his will rather than leaving the matter to random chance.</p><p>Lots were cast to distribute the land of Canaan among the tribes (Num. 26:55; Josh. 18:10), to identify Achan's guilt (Josh. 7:14-18), to select Saul as king (1 Sam. 10:20-21), to assign Levitical duties and divisions in the temple (1 Chr. 24:5; Luke 1:9), and to identify Jonah as the source of the storm (Jon. 1:7). The Day of Atonement scapegoat ceremony used lots to determine which goat would be sacrificed and which sent to Azazel (Lev. 16:8). Roman soldiers cast lots for Jesus's garments at the crucifixion (Matt. 27:35), fulfilling Psalm 22:18 within the providential pattern of Scripture. The disciples' casting of lots to replace Judas (Acts 1:26) is the NT's final use of this method; the gift of the Spirit at Pentecost apparently rendered external lots unnecessary for discerning God's will.</p>"
    },
    "plagues-the-ten": {
        "term": "Plagues, the Ten",
        "category": "concepts",
        "source_ids": {"smith": "plagues-the-ten"},
        "key_refs": ["Exodus 7:14", "Exodus 9:14", "Exodus 12:12", "Psalms 78:43", "Revelation 16:1"],
        "hitchcock_meaning": None,
        "intro": "<p>The ten plagues of Egypt were successive divine judgments against Pharaoh and Egypt that culminated in the Exodus of Israel (Ex. 7-12). They escalated in severity: (1) water turned to blood; (2) frogs; (3) gnats/lice; (4) flies; (5) livestock disease; (6) boils; (7) hail; (8) locusts; (9) three days of darkness; (10) death of all Egyptian firstborns. The narrative presents them as a systematic confrontation with the gods of Egypt, with God explicitly declaring that through the plagues he will 'execute judgments against all the gods of Egypt' (Ex. 12:12) — each plague targeting an area under a specific deity's domain.</p><p>A series of notices about Pharaoh's hardening of heart — sometimes Pharaoh hardening his own heart (Ex. 8:15, 32) and sometimes God hardening it (Ex. 9:12; 10:1) — raises profound questions about divine sovereignty and human responsibility that Paul addresses directly in Romans 9:17-18. From the fourth plague onward, Israelites in Goshen were exempted, distinguishing God's people from Egypt. The tenth plague prompted the institution of the Passover sacrifice (Ex. 12:1-28) to protect Israelite firstborns and became the foundational annual memorial. Psalm 78 and 105 retell the plagues within the covenant history; Revelation's bowl judgments (Rev. 16) deliberately echo the plague sequence as the eschatological culmination of divine judgment on the enemies of God's people.</p>"
    },
    "proverbs": {
        "term": "Proverbs",
        "category": "concepts",
        "source_ids": {"nave": "proverbs"},
        "key_refs": ["Proverbs 1:7", "Proverbs 8:22", "Proverbs 9:10", "Proverbs 31:10", "Colossians 1:15"],
        "hitchcock_meaning": None,
        "intro": "<p>The Book of Proverbs is a collection of Hebrew wisdom literature drawn from multiple identified sources: the proverbs of Solomon (chs. 10-22; 25-29), 'the words of the wise' (22:17-24:34), the sayings of Agur son of Jakeh (ch. 30), and the words of King Lemuel taught him by his mother (ch. 31). The prologue (chs. 1-9) consists of extended wisdom speeches and the personification of Wisdom as a woman who calls in the streets, the markets, and the city gates. The book's foundational thesis is stated at both beginning and end: 'The fear of the LORD is the beginning of wisdom' (1:7; 9:10).</p><p>Proverbs represents practical wisdom for living in alignment with God's created moral order — observations about cause and effect in human relationships, economics, speech, family life, and governance. Its literary forms range from compact two-line proverbs to extended poems and the Proverbs 31 portrait of a capable woman. The personified Wisdom of chapter 8, who was 'beside him, like a master workman' at creation and in whom God delighted (8:30), became the primary OT resource for NT Christological reflection on Christ's pre-existence and role in creation: Colossians 1:15-17, John 1:1-3, and Hebrews 1:1-3 all draw on wisdom categories to articulate who Jesus is in relation to God and creation.</p>"
    },
    "purim": {
        "term": "Purim",
        "category": "concepts",
        "source_ids": {"smith": "purim"},
        "key_refs": ["Esther 3:7", "Esther 9:24", "Esther 9:26", "Esther 9:28", "Esther 9:32"],
        "hitchcock_meaning": None,
        "intro": "<p>Purim is the annual Jewish festival commemorating the deliverance of Persian Jewry from the genocidal plot of Haman the Agagite, as narrated in the Book of Esther. Haman cast <em>pur</em> (an Akkadian loan word for 'lot') to determine an auspicious date for exterminating all Jews in the Persian empire (Esth. 3:7), giving the feast its name. When the plot was reversed through the advocacy of Mordecai and Esther, they instituted a permanent two-day celebration on the fourteenth and fifteenth of Adar (February-March) through written decrees sent to all Jewish communities (Esth. 9:20-28).</p><p>The Purim observance centers on the public reading of the entire Book of Esther (the Megillah) with noisemakers (groggers) used to drown out Haman's name at each occurrence, feasting and gladness, exchange of gifts of food between neighbors, and giving of gifts to the poor (Esth. 9:22). Purim is not commanded in the Mosaic law but was established through communal authority in response to a historical deliverance. The Book of Esther is unique among the canonical books of the Hebrew Bible in making no explicit reference to God, yet the narrative presents an unmistakable theology of hidden divine providence working through human agency, coincidence, and courage. Purim is among the most festive and carnivalesque celebrations in the Jewish calendar.</p>"
    },
    "refuges-cities-of": {
        "term": "Refuges, Cities of",
        "category": "concepts",
        "source_ids": {"smith": "refuges-cities-of"},
        "key_refs": ["Numbers 35:11", "Joshua 20:2", "Deuteronomy 19:3", "Hebrews 6:18", "Numbers 35:28"],
        "hitchcock_meaning": None,
        "intro": "<p>The cities of refuge were six Levitical cities designated in the Mosaic law to provide asylum for persons who had killed someone accidentally (manslaughter) from the blood avenger (Num. 35:9-34; Deut. 19:1-13; Josh. 20). Three were appointed west of the Jordan — Kedesh in Galilee, Shechem in Ephraim, and Hebron in Judah — and three east of the Jordan — Bezer in Reuben, Ramoth-Gilead in Gad, and Golan in Manasseh (Josh. 20:7-8). Roads to these cities were to be maintained for ease of access; the cities were well publicized throughout the land.</p><p>A person who had accidentally killed someone could flee to the nearest city of refuge before the blood avenger overtook them. The congregation would adjudicate the case: if the death was ruled premeditated murder, the slayer was handed over for execution; if ruled accidental, the slayer remained safely in the city of refuge until the death of the high priest in office, after which they were free to return home without being subject to blood vengeance. Leaving the city before the high priest's death removed this protection. The institution established an early form of due process and fair adjudication before the community, preventing unlimited blood vengeance. The Epistle to the Hebrews uses the imagery of the city of refuge for the certainty of Christian hope: believers 'who have fled for refuge might have strong encouragement to hold fast to the hope set before us' in Christ (Heb. 6:18).</p>"
    },
    "ruth-book-of": {
        "term": "Ruth, Book of",
        "category": "concepts",
        "source_ids": {"smith": "ruth-book-of"},
        "key_refs": ["Ruth 1:16", "Ruth 2:12", "Ruth 4:10", "Ruth 4:17", "Matthew 1:5"],
        "hitchcock_meaning": None,
        "intro": "<p>The Book of Ruth, set 'in the days when the judges ruled' (Ruth 1:1), narrates the story of Ruth, a Moabite widow who follows her Jewish mother-in-law Naomi from Moab to Bethlehem after the deaths of both their husbands. Ruth's declaration of loyalty — 'Where you go I will go, and where you stay I will stay. Your people shall be my people, and your God my God' (1:16) — is among the most celebrated expressions of covenant faithfulness (<em>hesed</em>) in Scripture, spoken by a Gentile woman who embraced Israel's God of her own choosing.</p><p>The book's plot turns on the institution of the <em>go'el</em> (kinsman-redeemer), as the wealthy Boaz exercises his right and obligation to redeem Naomi's ancestral land and marry Ruth under the levirate custom, after a closer kinsman declines (Ruth 4:1-10). Ruth's faithfulness to Naomi and Boaz's <em>hesed</em> toward both women become models of covenant loyalty that mirrors God's own faithfulness to Israel. The book concludes with the birth of Obed, grandfather of David (4:17-22), placing this Gentile woman within the royal Davidic lineage. Matthew's genealogy of Jesus includes Ruth among four women cited (Matt. 1:5), each representing God's grace working through unexpected and non-Israelite channels. The book is read at Pentecost in Jewish liturgical practice.</p>"
    },
    "sabaoth-the-lord-of": {
        "term": "Sabaoth, the Lord of",
        "category": "concepts",
        "source_ids": {"smith": "sabaoth-the-lord-of"},
        "key_refs": ["Isaiah 6:3", "Romans 9:29", "James 5:4", "Psalms 46:7", "1 Samuel 4:4"],
        "hitchcock_meaning": None,
        "intro": "<p>The Lord of Sabaoth — transliterated from Hebrew <em>YHWH Tseva'ot</em> (LORD of hosts) — is a divine title appearing over 260 times in the Hebrew Bible, concentrated especially in Isaiah, Jeremiah, Haggai, Zechariah, and Malachi, and twice in the NT (Rom. 9:29; James 5:4). The term <em>tseva'ot</em> (hosts/armies) encompasses the heavenly armies of angels, the celestial bodies, and all earthly forces under divine command, expressing God's absolute sovereignty over every created power — angelic, cosmic, and military.</p><p>The title is closely associated with the ark of the covenant, beside which God was enthroned 'between the cherubim' and called 'the LORD of hosts' (1 Sam. 4:4; 2 Sam. 6:2), and with the Jerusalem temple. Isaiah's throne-room vision — in which the seraphim cry 'Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory' (Isa. 6:3) — anchored this title in Christian liturgy through the Trisagion and the Sanctus. The title asserts God's absolute sovereignty over history's military and cosmic forces, a claim of critical theological importance during the centuries of Assyrian and Babylonian imperial dominance. Paul's citation in Romans 9:29 (quoting Isa. 1:9) affirms God's continued faithfulness despite Israel's judgment; James 5:4 invokes the LORD of hosts as the righteous judge who hears the cries of oppressed workers.</p>"
    },
    "tabernacles-the-feast-of": {
        "term": "Tabernacles, the Feast of",
        "category": "concepts",
        "source_ids": {"smith": "tabernacles-the-feast-of"},
        "key_refs": ["Leviticus 23:34", "Deuteronomy 16:13", "John 7:37", "Zechariah 14:16", "Nehemiah 8:17"],
        "hitchcock_meaning": None,
        "intro": "<p>The Feast of Tabernacles (Hebrew <em>Sukkot</em>, also called the Feast of Ingathering — Ex. 23:16) was the third of the three annual pilgrimage festivals, lasting seven days beginning the fifteenth of Tishri, followed by an eighth-day assembly (Shemini Atzeret). The feast celebrated the completed agricultural year — all grain, wine, and oil safely gathered — making it the great thanksgiving of the harvest. It also commemorated Israel's forty years of dwelling in temporary shelters in the wilderness after the Exodus (Lev. 23:43).</p><p>All male Israelites were required to appear at the central sanctuary for the feast (Deut. 16:16), and worshippers constructed and lived in booths of leafy branches throughout the seven days. Second Temple practice added elaborate water-libation ceremonies on each day and the illumination of four great menorot in the Court of Women — the context for Jesus's declarations on the great day of the feast that rivers of living water would flow from those who believed in him (John 7:37-39) and that he is the light of the world (John 8:12). Zechariah's eschatological vision requires all nations to come to Jerusalem annually to celebrate Tabernacles in the new age (Zech. 14:16-19). Nehemiah's restoration of the feast was described as unprecedented since Joshua's day (Neh. 8:17).</p>"
    },
    "ten-commandments": {
        "term": "Ten Commandments",
        "category": "concepts",
        "source_ids": {"smith": "ten-commandments"},
        "key_refs": ["Exodus 20:1", "Deuteronomy 5:6", "Exodus 31:18", "Matthew 22:37", "Romans 7:7"],
        "hitchcock_meaning": None,
        "intro": "<p>The Ten Commandments (Hebrew <em>Aseret ha-Dibrot</em>, 'ten words') are the foundational covenant stipulations given by God to Israel at Sinai, inscribed by God himself on two stone tablets (Ex. 31:18; 32:15-16) and housed in the ark of the covenant. They were first spoken publicly in the hearing of the assembled congregation amid thunder, lightning, fire, and trumpet sound — the most direct divine speech to a corporate body in Scripture. Two accounts appear (Ex. 20:1-17; Deut. 5:6-21) with slight variations, particularly in the Sabbath commandment's grounding (creation in Exodus, redemption in Deuteronomy).</p><p>The commandments are traditionally divided into two tables: duties toward God (prohibitions of other gods, of idols, of misuse of the divine Name, and the Sabbath command, plus honor of parents) and duties toward humans (prohibitions of murder, adultery, theft, false witness, and coveting). Jesus summarized both tables in the two great commandments (Matt. 22:37-40), and Paul cited the Decalogue to illustrate what love of neighbor means concretely (Rom. 13:9). Paul also used the commandment against coveting to demonstrate how the law reveals sin rather than producing righteousness (Rom. 7:7-11). The Decalogue remains foundational to Christian ethics across all traditions, functioning as both the revelation of God's moral character and the standard against which human sinfulness is measured.</p>"
    },
    "trumpet": {
        "term": "Trumpet",
        "category": "concepts",
        "source_ids": {"smith": "trumpet"},
        "key_refs": ["Numbers 10:2", "Joshua 6:4", "Joel 2:1", "1 Corinthians 15:52", "Revelation 8:6"],
        "hitchcock_meaning": None,
        "intro": "<p>Scripture references two distinct trumpet instruments: the <em>shofar</em> (curved animal horn, typically a ram's) and the <em>chatsotsrah</em> (straight silver or bronze trumpet). God commanded Moses to make two silver trumpets for signaling the congregation, directing the movement of camp, summoning leaders, going to war, and marking the sacred calendar of feasts and new moons (Num. 10:1-10). Silver trumpets were blown by priests in the temple service. The shofar served different functions: the Sinai theophany (Ex. 19:16), the siege of Jericho (Josh. 6:4), Gideon's night attack (Judg. 7:8), and the anointing of kings (1 Kings 1:34).</p><p>The trumpet's primary eschatological associations pervade both Testaments. Joel called for a shofar blast to announce the Day of the LORD and summon a solemn assembly (Joel 2:1, 15). Isaiah and Zechariah envision a great trumpet heralding Israel's final ingathering (Isa. 27:13; Zech. 9:14). Paul's 'last trumpet' at which the dead are raised incorruptible and the living transformed (1 Cor. 15:52) and the trumpet at Christ's return (1 Thess. 4:16) draw directly on this prophetic tradition. The seven angelic trumpets of Revelation (Rev. 8-11), whose sounding unleashes successive judgments, represent the eschatological climax of the trumpet's role as herald of divine action in history.</p>"
    },
    "unclean-meats": {
        "term": "Unclean Meats",
        "category": "concepts",
        "source_ids": {"smith": "unclean-meats"},
        "key_refs": ["Leviticus 11:3", "Deuteronomy 14:3", "Acts 10:14", "Mark 7:19", "Romans 14:14"],
        "hitchcock_meaning": None,
        "intro": "<p>The Mosaic law distinguished between clean and unclean foods, specifying which animals could and could not be consumed by Israelites (Lev. 11; Deut. 14:3-21). For land animals, the criteria were dual: chewing the cud and having a completely split hoof. Animals meeting both criteria (cattle, sheep, goats, deer) were clean; those meeting only one were unclean — most notably the pig (split hoof but no cud-chewing) and the camel (cud-chewing but no split hoof). For water creatures, fins and scales were both required, excluding all shellfish and most seafood. Birds of prey, carrion-eaters, and most insects were unclean, with exceptions for certain locusts (Lev. 11:22).</p><p>The dietary distinctions served multiple purposes: marking Israel as a distinct covenant people set apart from the nations (Lev. 20:25-26), cultivating habits of discernment and self-discipline, and possibly encoding practical wisdom. Peter's vision of the great sheet containing all kinds of animals with the command 'kill and eat' (Acts 10:10-16) and the divine declaration 'What God has made clean, do not call common' was interpreted as signaling that Gentiles were no longer unclean and was confirmed by the Spirit's falling on Cornelius's household. Jesus's teaching that 'there is nothing outside a person that by going into him can defile him' (Mark 7:15) is interpreted by Mark as declaring all foods clean (Mark 7:19). Paul addresses residual concerns about food in Romans 14 and 1 Corinthians 8-10.</p>"
    },
    "wandering-in-the-wilderness": {
        "term": "Wandering in the Wilderness",
        "category": "concepts",
        "source_ids": {"smith": "wandering-in-the-wilderness"},
        "key_refs": ["Numbers 14:33", "Deuteronomy 8:2", "Psalm 95:10", "1 Corinthians 10:5", "Hebrews 3:17"],
        "hitchcock_meaning": None,
        "intro": "<p>Israel's forty years of wilderness wandering between the Exodus from Egypt and the conquest of Canaan resulted from the people's catastrophic failure of faith at Kadesh-barnea. When the twelve spies returned from Canaan, ten gave a discouraging report, and the people refused to trust God's promise and advance. God's judgment was proportionate: one year for each of the forty days of the spy mission; the entire generation of those who left Egypt (except Caleb and Joshua) was condemned to die in the wilderness without entering the Promised Land (Num. 13-14; 32:11-13; Deut. 2:14).</p><p>The wilderness years were simultaneously a time of remarkable divine provision — manna (Ex. 16), water from the rock (Ex. 17; Num. 20), the pillar of cloud and fire (Ex. 13:21-22) — and of persistent rebellion: the golden calf (Ex. 32), complaining about food (Num. 11), Miriam and Aaron's challenge (Num. 12), Korah's revolt (Num. 16), the bronze serpent episode (Num. 21), and Baal-Peor (Num. 25). Deuteronomy reflects on the wilderness as God's school for Israel: 'he humbled you and let you hunger... that he might make you know that man does not live by bread alone' (Deut. 8:3). Paul interprets the wilderness events as typological warnings for Christians (1 Cor. 10:1-13); Hebrews 3-4 applies Psalm 95's warning against hardening in the wilderness to the danger of Christian apostasy.</p>"
    },
    "witch-witchcrafts": {
        "term": "Witch; Witchcrafts",
        "category": "concepts",
        "source_ids": {"smith": "witch-witchcrafts"},
        "key_refs": ["Exodus 22:18", "Deuteronomy 18:10", "1 Samuel 28:7", "Isaiah 8:19", "Galatians 5:20"],
        "hitchcock_meaning": None,
        "intro": "<p>Witchcraft, divination, and sorcery were strictly prohibited in Mosaic law as fundamentally incompatible with exclusive covenant loyalty to YHWH. Deuteronomy 18:10-12 lists the forbidden practices comprehensively: child sacrifice, divination, omens, sorcery, casting spells, consulting mediums or spiritists, and necromancy — declaring all these 'an abomination to the LORD.' The death penalty was prescribed specifically for the medium or spiritist (Lev. 20:6, 27) and for the sorceress (Ex. 22:18). This prohibition reflects the conviction that seeking hidden knowledge or supernatural power through any channel other than God represents a fundamental rejection of the covenant relationship.</p><p>The most dramatic scriptural illustration is Saul's consultation of the medium at Endor on the eve of his final battle (1 Sam. 28:7-25). In desperate fear and having received no answer from God through dreams, Urim, or prophets, the king who had himself expelled mediums from the land secretly sought one out — a transgression cited as a cause of his death (1 Chr. 10:13-14). The prophets condemned Israel's attraction to occult practices as covenant betrayal (Isa. 8:19-20; Mic. 5:12; Nah. 3:4). In the NT, sorcery (<em>pharmakeia</em>) appears in the vice list as a work of the flesh (Gal. 5:20) and among the sins of those excluded from the new Jerusalem (Rev. 21:8; 22:15). The burning of magic books worth fifty thousand pieces of silver at Ephesus (Acts 19:19) represents the gospel's displacement of occult practice.</p>"
    },
    "women": {
        "term": "Women",
        "category": "concepts",
        "source_ids": {"smith": "women"},
        "key_refs": ["Judges 4:4", "2 Kings 22:14", "Proverbs 31:10", "Luke 8:2", "Galatians 3:28"],
        "hitchcock_meaning": None,
        "intro": "<p>The position of women in ancient Israel was defined primarily within the family structure — as daughters, wives, and mothers — yet significant female figures throughout Scripture exercised prophetic, judicial, and political authority that resists a reductively domestic characterization. Miriam was a prophetess and co-leader of the Exodus community alongside Moses and Aaron (Ex. 15:20-21; Mic. 6:4). Deborah functioned as both prophetess and judge over all Israel, holding court and summoning the military commander Barak (Judg. 4:4-9). Huldah the prophetess authenticated the Book of the Law for King Josiah's reform at a moment when the male prophets Jeremiah and Zephaniah were also active (2 Kings 22:14-20).</p><p>The Proverbs 31 capable woman represents industrious, commercially active, and publicly honored womanhood 'praised in the gates' — the civic arena of honor. Esther exercised decisive political agency to save the Jewish people from genocide. The NT records women as first witnesses of the empty tomb (Matt. 28:1-10; John 20:11-18) — a detail unlikely to have been invented given the low legal status of female testimony in antiquity, suggesting its historicity. Women supported Jesus's ministry financially and accompanied him to the cross when the male disciples fled (Luke 8:2-3; Mark 15:40-41). Paul's declaration that in Christ 'there is neither male nor female' (Gal. 3:28) established a theological principle with ongoing social implications; the NT depicts women as prophesying (1 Cor. 11:5), hosting churches (Acts 12:12; Col. 4:15), and co-laboring in the gospel (Phil. 4:3).</p>"
    },
    "year-sabbatical": {
        "term": "Year, Sabbatical",
        "category": "concepts",
        "source_ids": {"smith": "year-sabbatical"},
        "key_refs": ["Exodus 23:10", "Leviticus 25:4", "Deuteronomy 15:1", "2 Chronicles 36:21", "Nehemiah 10:31"],
        "hitchcock_meaning": None,
        "intro": "<p>The Sabbatical Year (<em>shemitah</em>, 'release') was the seventh year in the agricultural cycle prescribed by the Mosaic law, during which the land was to lie completely fallow: no sowing, pruning, or formal harvesting was permitted (Ex. 23:10-11; Lev. 25:1-7). Whatever grew of itself in the fallow year was available to the poor, the alien, and animals — illustrating the provision of rest and abundance beyond human effort. The theological grounding was explicit: the land belonged to God, not to its human occupants (Lev. 25:23), and the seven-year cycle mirrored the seven-day Sabbath in the weekly calendar.</p><p>The Sabbatical Year also required the release of all debts owed by fellow Israelites (Deut. 15:1-11), the public reading of the law at the Feast of Tabernacles (Deut. 31:10-13), and the freeing of Israelite slaves who had served six years (Deut. 15:12-18). The Chronicler specifically attributed the seventy years of Babylonian exile to accumulated unpaid sabbatical years: 'until the land had enjoyed its Sabbaths... to fulfill seventy years' (2 Chr. 36:21; Jer. 25:11). Post-exilic covenant renewal included a commitment to observe the sabbatical year and debt release (Neh. 10:31). Josephus and Maccabean-era sources confirm sabbatical year observance in Second Temple Judaism.</p>"
    },
    "zechariah-the-book-of": {
        "term": "Zechariah, the Book of",
        "category": "concepts",
        "source_ids": {"smith": "zechariah-the-book-of"},
        "key_refs": ["Zechariah 1:1", "Zechariah 9:9", "Zechariah 12:10", "Zechariah 13:7", "Matthew 21:5"],
        "hitchcock_meaning": None,
        "intro": "<p>The Book of Zechariah divides into three main sections of distinct character. Chapters 1-8 contain eight night visions received in 520-518 BC, during the early restoration period under Darius I when the second temple was being rebuilt under Zerubbabel and Joshua the high priest. The visions — the four horsemen, the horns and craftsmen, the measuring line, the cleansed high priest, the golden lampstand, the flying scroll, the woman in a basket, and the four chariots — use dense apocalyptic imagery to assure the struggling community of God's sovereign control over history and his commitment to Jerusalem's restoration.</p><p>Chapters 9-14 divide into two oracles (<em>massot</em>) of uncertain date that develop eschatological themes: the messianic king coming humble on a donkey (9:9, quoted in Matt. 21:5), the thirty pieces of silver (11:12-13, quoted in Matt. 27:9-10), mourning for the one 'whom they have pierced' (12:10, cited in John 19:37 and Rev. 1:7), and the striking of the shepherd and scattering of the sheep (13:7, cited by Jesus in Matt. 26:31). No OT book provides more material directly quoted in NT accounts of the passion than Zechariah. The book closes with a vision of all nations streaming to Jerusalem for the Feast of Tabernacles in the age of ultimate restoration (14:16-21).</p>"
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        article = {
            "id": slug,
            "term": data["term"],
            "category": data["category"],
            "intro": data["intro"],
            "hitchcock_meaning": data.get("hitchcock_meaning"),
            "source_ids": data["source_ids"],
            "key_refs": data["key_refs"],
            "sections": []
        }
        if merge_article(slug, article):
            written += 1
        else:
            skipped += 1
    print(f'BP gap-ot-context: OT practices/law/places/prophetic: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
