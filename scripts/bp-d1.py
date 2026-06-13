"""
BP Article Synthesis — d1: Daberath → Diamond
Covers Easton entries: Daberath through Diamond (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-d1.py
Run: python3 scripts/bp-d1.py
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
    # Never overwrite an existing synthesis — idempotent safety
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


# ── Article data ──────────────────────────────────────────────────────────────
ARTICLES = {
    "daberath": {
        "id": "daberath",
        "term": "Daberath",
        "category": "places",
        "intro": "<p>Daberath (also spelled Dabareh, meaning <em>same as Dabareh</em>) was a Levitical town on the border of Zebulun and Issachar, located at the foot of Mount Tabor (Joshua 19:12). It was assigned to the Levites of the Gershonite family as one of their forty-eight cities (Joshua 21:28; 1 Chronicles 6:72). Modern scholars generally identify it with the village of Deburiyeh on the northwestern slope of Mount Tabor, still bearing a cognate name. The site is possibly connected to the incident in Matthew 17:14 (and parallels) where Jesus descended from the mountain of transfiguration into a crowd below.</p>",
        "hitchcock_meaning": "same as Dabareh",
        "source_ids": {"easton": "daberath", "smith": "daberath", "isbe": "daberath"},
        "key_refs": ["Joshua 19:12", "Joshua 21:28"],
        "sections": []
    },
    "daemon": {
        "id": "daemon",
        "term": "Daemon",
        "category": "concepts",
        "intro": "<p>Daemon (from Greek <em>daimōn</em>) is an alternative transliteration of the word rendered <em>demon</em> in most English versions. In classical Greek the term denoted a spirit of intermediate rank between gods and mortals, sometimes benevolent in Greek thought, but in the New Testament exclusively applied to malevolent spiritual beings subject to Satan. They are portrayed as being cast out by Jesus's authority (Matthew 8:16; 12:43) and by his disciples (Matthew 10:1), and they acknowledge Jesus's divine identity while trembling (James 2:19). The New Testament consistently distinguishes daemons as personal, intelligent, evil spirits distinct from Satan himself, who exercise influence over individuals and in some instances over geographic territories.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daemon"},
        "key_refs": ["Matthew 8:16", "Matthew 10:1", "Matthew 12:43", "James 2:19"],
        "sections": []
    },
    "daemoniac": {
        "id": "daemoniac",
        "term": "Daemoniac",
        "category": "concepts",
        "intro": "<p>A daemoniac (demoniac) was a person under the direct control or indwelling of one or more evil spirits. The Gospels record numerous accounts of Jesus confronting and expelling demoniacs, including a mute man whose speech was restored (Matthew 9:32–33), the Gadarene demoniacs — one or two men possessed by a legion of demons who drove them to self-destructive behavior among the tombs (Matthew 8:28; Mark 5:1–20) — and a boy whose seizure-like symptoms were instantly healed (Mark 9:17–27). The New Testament presents demonic possession as a real and distinct condition, separable from (though sometimes accompanied by) physical illness. Jesus's power over demoniacs was cited as evidence of the arrival of the kingdom of God (Matthew 12:28).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daemoniac"},
        "key_refs": ["Matthew 9:32", "Mark 9:17", "Matthew 8:28"],
        "sections": []
    },
    "dagon": {
        "id": "dagon",
        "term": "Dagon",
        "category": "concepts",
        "intro": "<p>Dagon (from Hebrew <em>dag</em>, fish, or possibly <em>dagan</em>, grain) was the chief national deity of the Philistines. Ancient sources and the idol's name suggest he was depicted with a human head and hands but the body of a fish, combining Mesopotamian and Semitic fish-deity traditions. His worship was widespread across the ancient Levant — temples to Dagon existed at Gaza, Ashdod, and Beth-shan. In Scripture he appears at three decisive moments: Samson's destruction of the temple at Gaza, killing thousands of Philistines (Judges 16:23–30); the capture of the ark of the covenant by the Philistines, when Dagon's idol fell prostrate before the ark and was broken (1 Samuel 5:2–7); and the deposit of Saul's armor in the temple of Dagon at Beth-shan after his death (1 Chronicles 10:10). Each episode serves in the biblical narrative to demonstrate the LORD's supremacy over pagan deities.</p>",
        "hitchcock_meaning": "corn; a fish",
        "source_ids": {"easton": "dagon", "smith": "dagon", "isbe": "dagon"},
        "key_refs": ["Judges 16:23", "1 Samuel 5:2", "1 Chronicles 10:10"],
        "sections": []
    },
    "dagons-house": {
        "id": "dagons-house",
        "term": "Dagon's House",
        "category": "places",
        "intro": "<p>The house (temple) of Dagon refers to temples dedicated to the Philistine god Dagon. The most narratively significant is the temple at Ashdod, where the Philistines placed the captured ark of the covenant (1 Samuel 5:2), only to find the idol of Dagon toppled before the ark repeatedly until the statue was broken. A separate temple of Dagon at Beth-shan (1 Chronicles 10:10) is where the Philistines fastened Saul's head after his defeat at Gilboa. A town called Beth-dagon — \"house of Dagon\" — is mentioned in Joshua 15:41 (in Judah) and Joshua 19:27 (in Asher), indicating the widespread distribution of Dagon worship across Canaan before and during the period of Israel's settlement.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dagons-house"},
        "key_refs": ["1 Samuel 5:2", "1 Chronicles 10:10", "Joshua 15:41"],
        "sections": []
    },
    "daily-sacrifice": {
        "id": "daily-sacrifice",
        "term": "Daily Sacrifice",
        "category": "concepts",
        "intro": "<p>The daily sacrifice (Hebrew <em>tamid</em>, meaning <em>continual</em>) consisted of two male lambs offered each day on the altar of burnt offering in the tabernacle and later the temple — one at dawn and one at twilight — accompanied by a grain offering and a drink offering (Exodus 29:38–42; Numbers 28:3–8). This perpetual sacrifice was the heartbeat of Israelite worship, symbolizing the nation's continual consecration to God. Its interruption was therefore a sign of severe divine judgment or foreign oppression. Daniel's prophetic visions refer to the cessation of the daily sacrifice as a marker of the great tribulation under Antiochus Epiphanes (Daniel 8:11–13; 11:31; 12:11) and its eschatological counterpart, fulfillments that Jesus cited in the Olivet Discourse (Matthew 24:15).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daily-sacrifice"},
        "key_refs": ["Daniel 8:12", "Daniel 11:31", "Daniel 12:11"],
        "sections": []
    },
    "dale-the-kings": {
        "id": "dale-the-kings",
        "term": "Dale, the King's",
        "category": "places",
        "intro": "<p>The King's Dale (Hebrew <em>emeq ha-melek</em>) was a valley near Jerusalem, mentioned twice in Scripture. In Genesis 14:17, it is identified as the Valley of Shaveh, the site where the king of Sodom met Abraham after his defeat of the confederate kings and where Melchizedek also appeared to bless him. In 2 Samuel 18:18, it is the place where Absalom had erected a monument to himself during his lifetime, since he had no son to perpetuate his name — a pillar known in the writer's day as \"Absalom's monument.\" The valley's exact location near Jerusalem has not been conclusively identified, but ancient tradition placed it in the Kidron Valley.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dale-the-kings"},
        "key_refs": ["Genesis 14:17", "2 Samuel 18:18"],
        "sections": []
    },
    "dalmanutha": {
        "id": "dalmanutha",
        "term": "Dalmanutha",
        "category": "places",
        "intro": "<p>Dalmanutha (meaning <em>a bucket</em> or <em>a branch</em>) was a place on the western shore of the Sea of Galilee where Jesus withdrew with his disciples after the feeding of the four thousand (Mark 8:10). Matthew's parallel account calls the same location Magadan (Matthew 15:39), which is likely identified with ancient Magdala (modern Migdal). The exact site of Dalmanutha remains uncertain; it may have been a district name or a smaller locality near Magdala. Jesus was immediately confronted there by Pharisees and Sadducees seeking a sign from heaven, which he refused to give, instead departing by boat.</p>",
        "hitchcock_meaning": "a bucket; a branch",
        "source_ids": {"easton": "dalmanutha", "smith": "dalmanutha", "isbe": "dalmanutha"},
        "key_refs": ["Mark 8:10"],
        "sections": []
    },
    "dalmatia": {
        "id": "dalmatia",
        "term": "Dalmatia",
        "category": "places",
        "intro": "<p>Dalmatia (meaning <em>deceitful lamps</em> or <em>vain brightness</em>, though the etymology is uncertain) was a Roman province on the eastern coast of the Adriatic Sea, corresponding roughly to modern Croatia and Bosnia. It is mentioned once in the New Testament, in 2 Timothy 4:10, where Paul reports that Titus has gone to Dalmatia — presumably for missionary work. Romans 15:19 may imply Paul himself had evangelized \"as far as Illyricum,\" the broader region of which Dalmatia was a part, suggesting that the Christian faith reached this area during Paul's third missionary journey or through subsequent workers.</p>",
        "hitchcock_meaning": "deceitful lamps; vain brightness",
        "source_ids": {"easton": "dalmatia", "smith": "dalmatia", "isbe": "dalmatia"},
        "key_refs": ["2 Timothy 4:10", "Romans 15:19"],
        "sections": []
    },
    "damaris": {
        "id": "damaris",
        "term": "Damaris",
        "category": "people",
        "intro": "<p>Damaris (meaning <em>a little woman</em>) was a woman of Athens who believed in response to Paul's sermon on the Areopagus (Acts 17:34). She is mentioned alongside Dionysius the Areopagite as one of the few named converts from that occasion. Nothing further is recorded about her in Scripture. Her specific mention by name alongside a member of the Areopagus court suggests she may have been a woman of some social standing or prominence. The sermon at the Areopagus, addressing Athenian philosophy and the unknown god, was among Paul's most intellectually engaging encounters and produced few converts compared with his synagogue preaching.</p>",
        "hitchcock_meaning": "a little woman",
        "source_ids": {"easton": "damaris", "smith": "damaris", "isbe": "damaris"},
        "key_refs": ["Acts 17:34"],
        "sections": []
    },
    "damascus": {
        "id": "damascus",
        "term": "Damascus",
        "category": "places",
        "intro": "<p>Damascus (meaning <em>activity</em> or <em>a sack full of blood</em>) is one of the oldest continuously inhabited cities in the world and the capital of ancient Syria (Aram), situated approximately 133 miles north of Jerusalem in a fertile plain east of the Anti-Lebanon mountains. Abraham pursued the four kings who had taken Lot as far as Hobah, north of Damascus (Genesis 14:15), and his servant Eliezer was from Damascus (Genesis 15:2). David conquered it and installed garrisons after defeating the Syrians who came to aid Hadadezer (2 Samuel 8:5–6). Throughout the period of the divided monarchy, Damascus and Israel alternated between alliance and enmity. Isaiah prophesied its desolation (Isaiah 17:1–3), fulfilled by Tiglath-pileser III in 732 B.C. The city assumes major New Testament significance as the destination of Saul of Tarsus when the risen Christ appeared to him and transformed him into the apostle Paul (Acts 9:1–22). Paul later escaped the city hidden in a basket lowered over the wall (2 Corinthians 11:32–33).</p>",
        "hitchcock_meaning": "a sack full of blood; the similitude of burning",
        "source_ids": {"easton": "damascus", "smith": "damascus", "isbe": "damascus"},
        "key_refs": ["Genesis 14:15", "2 Samuel 8:5", "Isaiah 7:8", "Acts 9:2"],
        "sections": []
    },
    "damnation": {
        "id": "damnation",
        "term": "Damnation",
        "category": "concepts",
        "intro": "<p>Damnation in the KJV translates several Greek words — most commonly <em>krima</em> (judgment) and <em>krisis</em> (condemnation) — referring to divine judgment and its consequences. In Romans 13:2, those who resist governing authorities \"receive to themselves damnation\" (judgment). In 1 Corinthians 11:29, partaking of the Lord's Supper unworthily brings damnation (judgment) upon oneself. Romans 14:23 speaks of eating with a doubtful conscience as damnation. Modern translations tend to use \"condemnation\" or \"judgment\" for these passages, reserving \"damnation\" for its contemporary sense of eternal punishment, which is the meaning in stronger passages such as Matthew 23:33 (\"the damnation of hell\"). The biblical concept encompasses both present divine judgment on sin and the final, eschatological condemnation of the unrepentant.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "damnation"},
        "key_refs": ["Romans 13:2", "1 Corinthians 11:29", "Romans 14:23"],
        "sections": []
    },
    "dan": {
        "id": "dan",
        "term": "Dan",
        "category": "people",
        "intro": "<p>Dan (meaning <em>judgment</em> or <em>he that judges</em>) was the fifth son of Jacob, born to Bilhah, Rachel's handmaid (Genesis 30:6). Rachel named him Dan, saying, \"God has judged me.\" He was the progenitor of the tribe of Dan, which in the wilderness encampment led the north section of Israel's formation (Numbers 2:25). The tribe received a coastal allotment west of Benjamin but was unable to hold it against the Philistines (Judges 1:34–35), leading to a migration northward where they conquered Laish and renamed it Dan (Judges 18). The city of Dan at the far northern frontier gave rise to the proverbial phrase <em>from Dan to Beersheba</em> denoting the full extent of the land of Israel. Jeroboam I erected one of his golden calves at Dan (1 Kings 12:29), making it a center of the northern kingdom's rival worship.</p>",
        "hitchcock_meaning": "judgment; he that judges",
        "source_ids": {"easton": "dan", "smith": "dan"},
        "key_refs": ["Genesis 30:6", "Numbers 2:25", "Judges 18:29", "1 Kings 12:29"],
        "sections": []
    },
    "dan-jaan": {
        "id": "dan-jaan",
        "term": "Dan-jaan",
        "category": "places",
        "intro": "<p>Dan-jaan was a site on the northern boundary of Israel visited by Joab and the commanders of the army during David's census of the population (2 Samuel 24:6). The name and location are uncertain; some manuscripts and ancient versions read \"Dan and Ijon\" (separate towns), while others treat it as a single place-name. It was evidently located in the far north of the land, near the region of Gilead and the Sidonians. The census route traveled from Aroer in the south through Transjordan, then northward to Dan-jaan and Sidon, then southwest back to Beersheba — a circuit of the entire territory of Israel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dan-jaan", "isbe": "dan-jaan"},
        "key_refs": ["2 Samuel 24:6"],
        "sections": []
    },
    "dance": {
        "id": "dance",
        "term": "Dance",
        "category": "concepts",
        "intro": "<p>Dancing in Scripture was a customary expression of religious joy, military celebration, and festivity. Women danced with timbrels to celebrate victories — Miriam led the women of Israel after the crossing of the Red Sea (Exodus 15:20) and Jephthah's daughter came out dancing to meet her father (Judges 11:34). David danced before the ark of the LORD with great enthusiasm as it entered Jerusalem (2 Samuel 6:14–16), an act that provoked Michal's contempt. The Psalms call Israel to praise God with dancing (Psalms 149:3; 150:4). In the New Testament, dancing appears in the parable of the prodigal son's celebration (Luke 15:25) and as the occasion for Herod's rash promise to Salome (Matthew 14:6). The rhythmic, communal nature of Hebrew dance was primarily an expression of communal worship and celebration rather than entertainment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dance", "smith": "dance"},
        "key_refs": ["Judges 21:21", "Psalms 30:11", "2 Samuel 6:14"],
        "sections": []
    },
    "daniel": {
        "id": "daniel",
        "term": "Daniel",
        "category": "people",
        "intro": "<p>Daniel (meaning <em>God is my judge</em>) is the name of several men in Scripture, most prominently the fourth-century prophet whose life and visions are recorded in the book bearing his name. Born of noble or royal Judean lineage, he was among the young men taken to Babylon by Nebuchadnezzar after the first deportation in 605 B.C. (Daniel 1:1–4). He distinguished himself in the Babylonian court by refusing to defile himself with the king's food, and through divine gift he interpreted dreams and visions that confounded the Chaldean sages (Daniel 2; 4). Under Belshazzar he interpreted the writing on the wall (Daniel 5), and under Darius the Mede he was cast into the lions' den for praying to God against the king's decree, emerging unharmed (Daniel 6). His four apocalyptic visions (Daniel 7–12) contain prophecies cited in the New Testament by Jesus, Paul, and John. Jesus refers to Daniel's \"abomination of desolation\" in the Olivet Discourse (Matthew 24:15).</p>",
        "hitchcock_meaning": "judgment of God; God my judge",
        "source_ids": {"easton": "daniel", "smith": "daniel", "isbe": "daniel"},
        "key_refs": ["Daniel 1:3", "Daniel 6:1", "Daniel 9:2", "Matthew 24:15"],
        "sections": []
    },
    "daniel-book-of": {
        "id": "daniel-book-of",
        "term": "Daniel, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Daniel is a prophetic and apocalyptic work in two distinct parts: a narrative section (chapters 1–6) recounting Daniel's life and the miraculous interventions of God in the Babylonian and Medo-Persian courts, and a visionary section (chapters 7–12) containing four great apocalyptic visions of world empires and the end of days. In the Hebrew Bible it is placed among the Writings (<em>Ketuvim</em>) rather than the Prophets, though the New Testament quotes and alludes to it as authoritative prophecy. The book was written partly in Aramaic (2:4b–7:28) and partly in Hebrew. Critical debate has long focused on the date of composition — sixth-century authorship by Daniel himself versus a second-century date during the Maccabean crisis — with evangelical scholars defending the earlier date based on fulfilled predictive prophecy, linguistic evidence, and Jesus's own citation of Daniel as a genuine prophet (Matthew 24:15). The book's visions of four world empires, the Ancient of Days, the Son of Man, and the seventy weeks are foundational for New Testament eschatology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daniel-book-of", "isbe": "daniel-book-of"},
        "key_refs": ["Daniel 7:13", "Daniel 9:27", "Matthew 24:15"],
        "sections": []
    },
    "dannah": {
        "id": "dannah",
        "term": "Dannah",
        "category": "places",
        "intro": "<p>Dannah (meaning <em>judging</em>) was a town in the hill country of Judah, listed in Joshua 15:49 among the cities of the tribe of Judah in the highlands near Hebron. It appears in the same cluster as Debir (Kirjath-sannah) and Socoh, placing it in the southern hill country. The site has not been definitively identified with a modern location, though some scholars have proposed Khirbet Samia or a neighboring ruin in the Hebron region. It is mentioned only once in Scripture and plays no further role in the biblical narrative.</p>",
        "hitchcock_meaning": "judging",
        "source_ids": {"easton": "dannah", "smith": "dannah", "isbe": "dannah"},
        "key_refs": ["Joshua 15:49"],
        "sections": []
    },
    "darda": {
        "id": "darda",
        "term": "Darda",
        "category": "people",
        "intro": "<p>Darda (meaning <em>home of knowledge</em>) was one of four men of renowned wisdom against whom Solomon's incomparable wisdom was measured (1 Kings 4:31). He is listed alongside Ethan the Ezrahite, Heman, and Calcol as sons of Mahol. In 1 Chronicles 2:6, Dara (a variant spelling) appears among the five sons of Zerah of the tribe of Judah. Whether these are the same individual or distinct persons is debated. Darda is otherwise unknown to Scripture; his fame was evidently proverbial in the ancient Near Eastern wisdom tradition, used to set a standard that Solomon surpassed.</p>",
        "hitchcock_meaning": "home of knowledge",
        "source_ids": {"easton": "darda", "isbe": "darda"},
        "key_refs": ["1 Kings 4:31"],
        "sections": []
    },
    "daric": {
        "id": "daric",
        "term": "Daric",
        "category": "concepts",
        "intro": "<p>The daric (Hebrew <em>darkemon</em>) was a Persian gold coin weighing approximately 8.4 grams, named after Darius I of Persia. It bore the image of the Persian king as a running archer and was the standard gold coin of the Persian empire. In Scripture it appears in the context of contributions for the rebuilding of the temple: David's offering for the first temple (1 Chronicles 29:7) uses the term anachronistically in the sense of a gold coin of known weight, while Ezra 2:69 and 8:27 and Nehemiah 7:70–72 record post-exilic contributions in darics for the second temple's construction. The daric is thus a marker of the Persian period documents and confirms the historical authenticity of the Ezra-Nehemiah records.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daric", "smith": "daric", "isbe": "daric"},
        "key_refs": ["1 Chronicles 29:7", "Ezra 2:69", "Nehemiah 7:70"],
        "sections": []
    },
    "darius": {
        "id": "darius",
        "term": "Darius",
        "category": "people",
        "intro": "<p>Darius is the name of three rulers in Scripture. (1.) Darius the Mede (Daniel 5:31; 6:1), son of Ahasuerus, who received the kingdom of Babylon after the fall of Belshazzar and under whose reign Daniel was cast into the lions' den. His identification with known historical figures — whether Cyaxares II, Ugbaru/Gubaru, or Cyrus himself — remains debated. (2.) Darius I of Persia (Hystaspes), who reigned 522–486 B.C. and confirmed the decree of Cyrus permitting the rebuilding of the Jerusalem temple (Ezra 4:24; 6:1–12), the work resuming in his second year through the prophets Haggai and Zechariah (Ezra 5:1–2; Haggai 1:1). The temple was completed in his sixth year (Ezra 6:15). (3.) Darius the Persian mentioned in Nehemiah 12:22, likely Darius II (423–404 B.C.) or Darius III (336–330 B.C.), during whose reign certain Levitical records were kept.</p>",
        "hitchcock_meaning": "he that informs himself",
        "source_ids": {"easton": "darius", "smith": "darius", "isbe": "darius"},
        "key_refs": ["Daniel 6:1", "Ezra 4:24", "Ezra 6:1", "Haggai 1:1"],
        "sections": []
    },
    "darkness": {
        "id": "darkness",
        "term": "Darkness",
        "category": "concepts",
        "intro": "<p>Darkness in Scripture functions both as a physical phenomenon and as a rich theological symbol of evil, divine judgment, and the absence of God. As a plague, the three days of darkness over Egypt (Exodus 10:21–23) — described as darkness that could be felt — foreshadowed the eschatological darkness of judgment. God's presence was sometimes veiled in thick darkness (Exodus 20:21; 1 Kings 8:12), expressing divine transcendence and mystery. The three hours of darkness at the crucifixion (Matthew 27:45; Luke 23:44) recalled the Exodus plague and signaled that the ultimate judgment was falling upon the Son of God. In Johannine theology, darkness is the realm of sin and unbelief in opposition to Christ who is the light of the world (John 1:5; 3:19). Paul calls believers to walk as children of light, having no fellowship with the unfruitful works of darkness (Ephesians 5:8–11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "darkness", "smith": "darkness"},
        "key_refs": ["Exodus 10:21", "Matthew 27:45", "Luke 23:44", "John 1:5"],
        "sections": []
    },
    "darling": {
        "id": "darling",
        "term": "Darling",
        "category": "concepts",
        "intro": "<p>Darling in the KJV (Psalms 22:20; 35:17) translates the Hebrew word <em>yechidah</em>, meaning <em>only one</em> or <em>sole</em>, referring to the soul as one's unique and irreplaceable life. In Psalm 22:20, the psalmist cries: \"Deliver my soul from the sword, my darling from the power of the dog\" — the parallelism making clear that <em>darling</em> is the poet's life itself, the single precious possession he implores God to rescue. In Psalm 35:17, the same term appears in a petition for rescue from attacking enemies described as lions. Christian interpreters reading Psalm 22 messianically understand these verses as expressing Christ's prayer from the cross for deliverance from death, fulfilled in the resurrection.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "darling", "isbe": "darling"},
        "key_refs": ["Psalms 22:20", "Psalms 35:17"],
        "sections": []
    },
    "dart": {
        "id": "dart",
        "term": "Dart",
        "category": "concepts",
        "intro": "<p>Darts in Scripture denote light thrown projectiles — javelins, arrows, or short spears used in ancient warfare. The term appears in several notable contexts. The \"fiery darts\" of the evil one described in Ephesians 6:16 are burning arrows — possibly fire-tipped projectiles — which faith is said to quench as a shield. This metaphor describes spiritual attacks of doubt, temptation, and accusation launched against the believer. In Deuteronomy 32:23–42, God's arrows and darts represent divine judgment on Israel's enemies. The physical dart also appears in the account of Absalom's death when Joab drove three darts (javelins) into his heart as he hung in the oak tree (2 Samuel 18:14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dart", "isbe": "dart"},
        "key_refs": ["Ephesians 6:16", "2 Samuel 18:14"],
        "sections": []
    },
    "date": {
        "id": "date",
        "term": "Date",
        "category": "concepts",
        "intro": "<p>The date palm (<em>Phoenix dactylifera</em>) was one of the most valuable trees of ancient Palestine and the Near East, providing fruit, sap, leaves for thatching, and timber. The Hebrew word <em>tamar</em> means both the date palm tree and its fruit, and was also used as a personal name (Tamar, Genesis 38:6; 2 Samuel 13:1). Date palms are mentioned among the trees of the booths in the Feast of Tabernacles (Nehemiah 8:15; Leviticus 23:40) and are implied in Joel 1:12 among the trees afflicted by the locust plague. Jericho was proverbially known as the \"city of palm trees\" (Deuteronomy 34:3; 2 Chronicles 28:15). In the New Testament, the crowds spread palm branches before Jesus at his triumphal entry into Jerusalem (John 12:13), and the redeemed in Revelation 7:9 stand with palm branches as a symbol of victory.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "date"},
        "key_refs": ["Joel 1:12", "Nehemiah 8:15", "Leviticus 23:40"],
        "sections": []
    },
    "dathan": {
        "id": "dathan",
        "term": "Dathan",
        "category": "people",
        "intro": "<p>Dathan (meaning <em>laws</em> or <em>rites</em>) was a Reubenite, son of Eliab, who joined the rebellion of Korah the Levite against the authority of Moses and Aaron in the wilderness (Numbers 16:1–35). Together with his brother Abiram, On son of Peleth, and the Levite Korah, he challenged Moses's exclusive leadership, claiming that all the congregation was holy and that Moses had exalted himself above the assembly. God's judgment was swift: the earth opened and swallowed Dathan, Abiram, and their households, and fire consumed the 250 men who had offered incense. The event is invoked as a warning against rebellion in Deuteronomy 11:6, Psalm 106:17, and as a type of destruction for the ungodly in later tradition.</p>",
        "hitchcock_meaning": "laws or rites",
        "source_ids": {"easton": "dathan", "smith": "dathan", "isbe": "dathan"},
        "key_refs": ["Numbers 16:1", "Deuteronomy 11:6", "Psalms 106:17"],
        "sections": []
    },
    "daughter": {
        "id": "daughter",
        "term": "Daughter",
        "category": "concepts",
        "intro": "<p>Daughter in Scripture carries both its literal meaning of a female offspring and several extended uses. \"Daughter of Zion\" and \"daughter of Jerusalem\" are poetic personifications of the city and its people (Isaiah 3:16; 10:32; Micah 4:8), expressing tender relationship and sometimes reproach. \"Daughters of men\" in Genesis 6:2 designates a group whose identity has been debated throughout church history. The phrase \"daughter of Abraham\" (Luke 13:16) affirms a woman's full covenant membership. In wisdom literature, a daughter's character reflects on the household (Sirach 42:9–11). The legal status of daughters in Israelite law included rights of inheritance when no sons survived (Numbers 27:1–11; 36:1–12), a provision that Zelophehad's daughters successfully petitioned Moses to establish.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daughter", "smith": "daughter", "isbe": "daughter"},
        "key_refs": ["Genesis 20:12", "Isaiah 3:16", "Numbers 27:1"],
        "sections": []
    },
    "david": {
        "id": "david",
        "term": "David",
        "category": "people",
        "intro": "<p>David (meaning <em>well-beloved</em> or <em>dear</em>) was the eighth and youngest son of Jesse of Bethlehem and the greatest king of Israel, whose reign (approximately 1010–970 B.C.) established the theological template of covenant kingship for all subsequent messianic expectation. Anointed secretly by Samuel while still a shepherd boy (1 Samuel 16:12–13), he came to prominence by slaying Goliath the Philistine (1 Samuel 17) and served in Saul's court before years of flight from the jealous king. After Saul's death, David was first made king of Judah at Hebron, then of all Israel. He captured Jerusalem and made it his capital, sought to build the temple (2 Samuel 7), and expanded Israel's borders to their greatest extent. His sin with Bathsheba and the murder of Uriah (2 Samuel 11) brought lasting consequences through Nathan's prophecy, including the rebellion of his son Absalom. Nevertheless David remained the paradigmatic king — \"a man after God's own heart\" (1 Samuel 13:14; Acts 13:22). The New Testament opens by tracing Jesus's lineage to David (Matthew 1:1), fulfilling the Davidic covenant (2 Samuel 7:12–16) that his throne would endure forever.</p>",
        "hitchcock_meaning": "well-beloved, dear",
        "source_ids": {"easton": "david", "smith": "david", "isbe": "david"},
        "key_refs": ["1 Samuel 16:12", "2 Samuel 7:12", "Acts 13:22", "Matthew 1:1"],
        "sections": []
    },
    "david-city-of": {
        "id": "david-city-of",
        "term": "David, City of",
        "category": "places",
        "intro": "<p>The City of David referred specifically to the ancient Jebusite fortress of Zion on the southeastern ridge of Jerusalem, which David captured from the Jebusites and made his royal seat (2 Samuel 5:7; 1 Chronicles 11:7). He built up the city around it and brought the ark of the covenant there (2 Samuel 6:12). The name is distinct from Jerusalem as a whole, designating the original Davidic stronghold on the southern hill, southwest of the later temple mount. It served as the royal burial ground for most of Judah's kings (1 Kings 2:10; 11:43). In the New Testament, Bethlehem is called the City of David (Luke 2:4, 11), linking the site of Jesus's birth to the Davidic covenant and Micah's prophecy (Micah 5:2).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "david-city-of", "smith": "david-city-of", "isbe": "david-city-of"},
        "key_refs": ["1 Chronicles 11:7", "1 Kings 3:1", "Luke 2:4", "Luke 2:11"],
        "sections": []
    },
    "day": {
        "id": "day",
        "term": "Day",
        "category": "concepts",
        "intro": "<p>Day in Scripture has several meanings. The ordinary civil day ran from sunset to sunset following the Genesis pattern (\"evening and morning,\" Genesis 1:5), a reckoning confirmed in Leviticus 23:32 where the Day of Atonement runs from one evening to the next. The daylight hours were divided into the first, third, sixth, and ninth hours, and the night into four watches. In prophetic literature, \"the day of the LORD\" (<em>yom YHWH</em>) refers to a decisive moment of divine intervention — initially conceived as a day of national triumph and later recast by the prophets as a day of judgment on Israel and the nations alike (Amos 5:18–20; Isaiah 2:12; Joel 2:1–11; Zephaniah 1:14–18). The New Testament frames Christ's return as \"the day of the Lord\" (1 Thessalonians 5:2; 2 Peter 3:10), giving the prophetic theme its ultimate fulfillment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "day", "smith": "day", "isbe": "day"},
        "key_refs": ["Leviticus 23:32", "Amos 5:18", "1 Thessalonians 5:2"],
        "sections": []
    },
    "daysman": {
        "id": "daysman",
        "term": "Daysman",
        "category": "concepts",
        "intro": "<p>Daysman (from the archaic English <em>umpire</em> or <em>arbitrator</em>) translates the Hebrew <em>mokiach</em> in Job 9:33 — one who argues between parties or lays his hand on both, acting as a mediating judge. Job despairs that there is no such arbiter between himself and God who could lay a hand on both parties, negotiate their dispute, and bring resolution. The concept anticipates the New Testament understanding of Christ as the one mediator between God and man (1 Timothy 2:5) who fulfills the role Job lacked — capable of touching both the divine and human sides of humanity's broken relationship with God because of his unique person as the God-man.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daysman", "smith": "daysman", "isbe": "daysman"},
        "key_refs": ["Job 9:33"],
        "sections": []
    },
    "dayspring": {
        "id": "dayspring",
        "term": "Dayspring",
        "category": "concepts",
        "intro": "<p>Dayspring (the dawn, the rising of the sun) is used in Job 38:12, where God challenges Job with the question of whether he has commanded the morning or appointed the dayspring its place. The image is of the dawn taking hold of the edges of the earth and shaking the wicked out of it like dust from a garment. More theologically significant is its use in Luke 1:78, where Zechariah's prophecy (the Benedictus) describes the coming Messiah as \"the dayspring from on high\" who will visit his people to give light to those who sit in darkness and the shadow of death — a direct allusion to Isaiah 9:2 and 60:1–2. The metaphor frames Christ as the dawn breaking over the long darkness of human sin and death.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dayspring", "isbe": "dayspring"},
        "key_refs": ["Job 38:12", "Luke 1:78"],
        "sections": []
    },
    "daystar": {
        "id": "daystar",
        "term": "Daystar",
        "category": "concepts",
        "intro": "<p>Daystar (the morning star) appears twice in the New Testament with distinct applications. In 2 Peter 1:19, the daystar (<em>phosphoros</em>, light-bearer) is promised to rise in the hearts of believers as the fulfillment of prophetic Scripture when the day dawns — pointing to the inner illumination of Christ's truth confirmed by personal experience. In Revelation 2:28 and 22:16, Jesus identifies himself as the \"bright and morning star\" (<em>ho astēr ho lampros ho prōinos</em>), the supreme celestial marker of a new era's dawn. The image echoes Balaam's prophecy of \"a star out of Jacob\" (Numbers 24:17) and affirms Christ as the fulfillment of all Israel's messianic hope.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "daystar"},
        "key_refs": ["2 Peter 1:19", "Revelation 22:16", "Numbers 24:17"],
        "sections": []
    },
    "days-journey": {
        "id": "days-journey",
        "term": "Day's Journey",
        "category": "concepts",
        "intro": "<p>A day's journey was an imprecise unit of distance in the ancient world, generally understood to represent the distance an ordinary traveler could cover in a day — roughly twenty to thirty miles depending on terrain, method of travel, and era. The phrase is used in Scripture to describe moderate distances: Elijah's wilderness journey (1 Kings 19:4), the three-day journey into the wilderness requested of Pharaoh (Exodus 3:18), and the spacing of the manna camp from Mount Sinai (Numbers 11:31). In the New Testament, Mary and Joseph traveled a day's journey before discovering Jesus was missing after the Passover visit to Jerusalem (Luke 2:44). The related term <em>Sabbath day's journey</em> (Acts 1:12) referred to the rabbinic limitation of about 2,000 cubits (approximately 3/4 mile) that was permitted for travel on the Sabbath.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "days-journey", "isbe": "days-journey"},
        "key_refs": ["Exodus 3:18", "Luke 2:44"],
        "sections": []
    },
    "deacon": {
        "id": "deacon",
        "term": "Deacon",
        "category": "concepts",
        "intro": "<p>Deacon (from Greek <em>diakonos</em>, servant or minister) designates a recognized office of the early Christian church, first implied in the appointment of the seven men in Acts 6:1–6 to oversee the distribution of food to Greek-speaking widows, freeing the apostles for prayer and the ministry of the word. The qualifications for deacons are formally stated in 1 Timothy 3:8–13: blameless character, not double-tongued, not given to wine, not greedy, holding the faith with a clear conscience, and tested before appointment. Deacons and overseers (bishops/elders) are addressed together in Paul's greeting to the Philippians (Philippians 1:1), indicating a two-fold office structure in the earliest churches. The diaconal office became foundational in subsequent church governance across all Christian traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "deacon", "smith": "deacon"},
        "key_refs": ["Acts 6:1", "1 Timothy 3:8", "Philippians 1:1"],
        "sections": []
    },
    "deaconess": {
        "id": "deaconess",
        "term": "Deaconess",
        "category": "concepts",
        "intro": "<p>Deaconess refers to women who served in an official or semi-official ministerial capacity in the early church. Phoebe is described as a <em>diakonos</em> (deacon/servant) of the church at Cenchrea and commended by Paul to the Roman congregation with language suggesting recognized status (Romans 16:1–2). Other women mentioned in leadership and ministry contexts include Priscilla (Romans 16:3), Euodia and Syntyche who \"labored side by side\" with Paul in the gospel (Philippians 4:2–3), and the women mentioned in Romans 16:12. The instruction in 1 Timothy 3:11 about \"women\" (or possibly \"wives of deacons\") has been interpreted as referring to female deacons. Historical evidence from the second century confirms a recognized order of deaconesses who assisted with the baptism of women and ministered to sick and poor women in the congregation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "deaconess", "smith": "deaconess"},
        "key_refs": ["Romans 16:1", "1 Timothy 3:11", "Philippians 4:2"],
        "sections": []
    },
    "dead-sea": {
        "id": "dead-sea",
        "term": "Dead Sea",
        "category": "places",
        "intro": "<p>The Dead Sea (called in Scripture the <em>Salt Sea</em>, <em>Sea of the Plain</em>, or <em>East Sea</em>) is the terminal lake of the Jordan River, situated approximately 1,400 feet below sea level — the lowest point on Earth's surface. It lies about sixteen miles east of Jerusalem. Its extraordinary salinity (approximately 34%) prevents all aquatic life, giving rise to its modern name. Scripture's earliest reference is Genesis 14:3, where it is the site of the battle of the five kings against the four. The cities of Sodom and Gomorrah are traditionally located on the plain at its southern end. Ezekiel's vision of the eschatological temple envisions fresh water flowing eastward from Jerusalem to heal the Dead Sea, teeming thereafter with fish (Ezekiel 47:8–10) — a powerful image of cosmic renewal. The Dead Sea Scrolls, discovered in caves at Qumran on its northwestern shore beginning in 1947, have revolutionized the study of the Old Testament text and Second Temple Judaism.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dead-sea", "smith": "dead-sea"},
        "key_refs": ["Genesis 14:3", "Numbers 34:12", "Deuteronomy 3:17", "Ezekiel 47:8"],
        "sections": []
    },
    "deal-tenth": {
        "id": "deal-tenth",
        "term": "Deal, Tenth",
        "category": "concepts",
        "intro": "<p>A tenth deal (Hebrew <em>assaron</em>) was a unit of dry measure equal to one-tenth of an ephah, approximately two quarts, used in specifying the grain portions of the Mosaic sacrificial offerings. It appears frequently in the priestly legislation of Leviticus and Numbers as the standard measure for the fine flour in the grain offering accompanying animal sacrifices (Exodus 29:40; Leviticus 14:10, 21; Numbers 15:4). The precision of the measurement underscores the careful regulation of worship in the Mosaic law, where even the smallest element of the offering was divinely specified to prevent unauthorized variation in approach to God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "deal-tenth"},
        "key_refs": ["Exodus 29:40", "Leviticus 14:10"],
        "sections": []
    },
    "dearth": {
        "id": "dearth",
        "term": "Dearth",
        "category": "concepts",
        "intro": "<p>Dearth (famine or scarcity of food) was in Scripture a recognized instrument of divine discipline and judgment. Among the notable famines recorded are: the famine in Canaan that drove Abram to Egypt (Genesis 12:10) and later sent Jacob's sons to Egypt for grain, initiating the Joseph narrative (Genesis 42); the seven-year famine predicted by Joseph and stored against (Genesis 41); the famine in the time of the judges that sent Naomi to Moab (Ruth 1:1); and the three-year famine in David's reign for Saul's bloodguilt against the Gibeonites (2 Samuel 21:1). The famine of Elijah's day — three and a half years of drought in Israel — was both judgment on Ahab and Jezebel and a platform for God's vindication on Carmel (1 Kings 17; Luke 4:25–26). Amos lists famine alongside drought and plague as divine covenant curses sent to call Israel back to God (Amos 4:6–8).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dearth", "smith": "dearth", "isbe": "dearth"},
        "key_refs": ["Genesis 12:10", "Ruth 1:1", "2 Samuel 21:1", "1 Kings 17:1"],
        "sections": []
    },
    "death": {
        "id": "death",
        "term": "Death",
        "category": "concepts",
        "intro": "<p>Death in Scripture is portrayed as the separation of body and spirit resulting from the entrance of sin into the world (Genesis 2:17; Romans 5:12), not as a natural element of creation but as its enemy. Physical death — the return of dust to the earth and the spirit to God (Ecclesiastes 12:7; Psalm 104:29) — is distinguished from spiritual death, the alienation of the soul from God through sin (Ephesians 2:1), and from the \"second death,\" the lake of fire representing final separation from God (Revelation 20:14; 21:8). Scripture presents death as the last enemy (1 Corinthians 15:26), overcome by Christ's resurrection. The sting of death is sin and the strength of sin is the law (1 Corinthians 15:55–56), but through the resurrection of Christ, death is swallowed up in victory. Hebrews presents Christ as sharing in flesh and blood precisely to destroy the one who holds the power of death (Hebrews 2:14–15).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "death", "isbe": "death"},
        "key_refs": ["Genesis 2:17", "Romans 5:12", "1 Corinthians 15:26", "Revelation 20:14"],
        "sections": []
    },
    "debir": {
        "id": "debir",
        "term": "Debir",
        "category": "places",
        "intro": "<p>Debir (meaning <em>an orator</em> or <em>a word</em>) was an important Canaanite city in the hill country of Judah, also called Kirjath-sannah and Kirjath-sepher (\"city of the book,\" suggesting it may have been a scribal center). It was captured first by Joshua (Joshua 10:38–39) and later by Caleb's nephew Othniel, who received Caleb's daughter Achsah in marriage as a reward (Joshua 15:15–17; Judges 1:11–15). The city was assigned to the tribe of Judah and made a Levitical city (Joshua 21:15). Its probable identification is with Tell Beit Mirsim, excavated by W.F. Albright, though Khirbet Rabud has also been proposed. The narrative of Othniel's conquest of Debir is particularly noteworthy as it introduces the first judge of Israel.</p>",
        "hitchcock_meaning": "an orator; a word",
        "source_ids": {"easton": "debir", "smith": "debir"},
        "key_refs": ["Joshua 15:15", "Joshua 15:49", "Judges 1:11"],
        "sections": []
    },
    "deborah": {
        "id": "deborah",
        "term": "Deborah",
        "category": "people",
        "intro": "<p>Deborah (meaning <em>a bee</em>) is the name of two women in the Old Testament. (1.) Rebekah's nurse, who accompanied her mistress from Paddan-aram to Canaan and died at Bethel, where she was buried under the oak of weeping, Allon-bachuth (Genesis 24:59; 35:8). (2.) A prophetess and the fourth judge of Israel, the only woman to hold that office, who \"held court\" under the Palm of Deborah between Ramah and Bethel (Judges 4:4–5). She summoned Barak son of Abinoam to lead Israel's army against Sisera, the commander of Jabin's Canaanite forces, with ten thousand men from Naphtali and Zebulun. When Barak refused to go without her, she accompanied him but prophesied that the honor of killing Sisera would go to a woman (Judges 4:9). Israel's victory, accomplished when Sisera was killed by Jael, is celebrated in the Song of Deborah (Judges 5), one of the oldest and most elaborate poems in the Old Testament.</p>",
        "hitchcock_meaning": "word; thing; a bee",
        "source_ids": {"easton": "deborah", "smith": "deborah", "isbe": "deborah"},
        "key_refs": ["Genesis 35:8", "Judges 4:4", "Judges 5:1"],
        "sections": []
    },
    "debt": {
        "id": "debt",
        "term": "Debt",
        "category": "concepts",
        "intro": "<p>Debt in the Mosaic law was handled with humanitarian concern to prevent the permanent impoverishment of fellow Israelites. Loans to the poor were to be made without interest (Deuteronomy 23:19–20; Leviticus 25:36–37), and all debts among Israelites were to be released in the seventh year (Deuteronomy 15:1–3). If a debtor could not repay, he might sell himself into indentured service, but was to be released in the year of jubilee (Leviticus 25:39–41). The New Testament extends the concept of debt into the spiritual realm: sin is described as a debt owed to God in the Lord's Prayer (Matthew 6:12, \"forgive us our debts\"), and Paul warns against the ongoing debt of love owed to one another (Romans 13:8). The parable of the unforgiving servant (Matthew 18:23–35) uses the imagery of an enormous financial debt forgiven by a king to illustrate the nature of God's forgiveness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "debt"},
        "key_refs": ["Deuteronomy 15:1", "Matthew 6:12", "Romans 13:8"],
        "sections": []
    },
    "debtor": {
        "id": "debtor",
        "term": "Debtor",
        "category": "concepts",
        "intro": "<p>Debtor in the Old Testament referred to a person who owed money and whose rights were protected by Mosaic law against harsh treatment: a creditor was forbidden to enter the debtor's house to take his pledge (Deuteronomy 24:10–11) and could not take essential items like millstones or a widow's garment (Deuteronomy 24:6, 17). A cloak taken as security had to be returned before nightfall (Exodus 22:26–27). In the New Testament, Paul describes all Gentiles as debtors to receive the gospel (Romans 1:14–15), and uses the analogy of slavery to debt to describe life under sin contrasted with life in the Spirit (Romans 8:12). The spiritual dimension of indebtedness — to God, to neighbor, and to the gospel call — runs throughout Pauline theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "debtor", "smith": "debtor"},
        "key_refs": ["Deuteronomy 24:10", "Romans 1:14", "Romans 8:12"],
        "sections": []
    },
    "decalogue": {
        "id": "decalogue",
        "term": "Decalogue",
        "category": "concepts",
        "intro": "<p>The Decalogue (from Greek <em>deka</em>, ten, and <em>logos</em>, word) is the name given by the Greek fathers to the Ten Commandments, called in the Hebrew text the \"ten words\" (<em>aseret ha-devarim</em>, Exodus 34:28; Deuteronomy 4:13; 10:4). They were inscribed by God on two tablets of stone and given to Moses at Sinai (Exodus 31:18), first broken when Moses saw the golden calf (Exodus 32:19) and rewritten on a second pair of tablets (Exodus 34:1). The commandments are recorded in Exodus 20:3–17 and repeated in Deuteronomy 5:6–21. They govern Israel's relationship with God (commandments 1–4) and with fellow human beings (commandments 5–10). Jesus affirmed their continuing authority and deepened their ethical demands in the Sermon on the Mount (Matthew 5:17–48). The traditional division of the commandments into two tablets differs between Jewish, Catholic, and Protestant traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "decalogue", "isbe": "decalogue"},
        "key_refs": ["Exodus 20:3", "Deuteronomy 5:6", "Matthew 5:17"],
        "sections": []
    },
    "decapolis": {
        "id": "decapolis",
        "term": "Decapolis",
        "category": "places",
        "intro": "<p>Decapolis (Greek, <em>deka</em> ten + <em>polis</em> city) was a league or district of ten predominantly Greek-speaking cities east and southeast of the Sea of Galilee, in the region of Bashan and Gilead and extending to Damascus. The cities — most commonly listed as Scythopolis (the only one west of the Jordan), Pella, Gerasa, Philadelphia, Gadara, Hippos, Dion, Raphana, Canatha, and Damascus — had been Hellenized under Seleucid and Roman rule. The Decapolis is mentioned three times in the New Testament: crowds from this region followed Jesus (Matthew 4:25); the Gadarene demoniac after his healing proclaimed what Jesus had done \"throughout the Decapolis\" (Mark 5:20); and Jesus traveled through the region healing a deaf man (Mark 7:31). The area represented the frontier between Jewish and Gentile populations.</p>",
        "hitchcock_meaning": "containing ten cities",
        "source_ids": {"easton": "decapolis", "isbe": "decapolis"},
        "key_refs": ["Matthew 4:25", "Mark 5:20", "Mark 7:31"],
        "sections": []
    },
    "decision-valley-of": {
        "id": "decision-valley-of",
        "term": "Decision, Valley of",
        "category": "places",
        "intro": "<p>The Valley of Decision appears in Joel 3:14 in the prophet's vision of the day of the LORD: \"Multitudes, multitudes in the valley of decision! For the day of the LORD is near in the valley of decision.\" Joel identifies this valley with the Valley of Jehoshaphat (Joel 3:2, 12), where God will gather all nations to judge them for their treatment of Israel. The Hebrew word <em>charuts</em> means <em>decision</em> or <em>determination</em> and describes the irreversible nature of the divine verdict about to fall. The Valley of Jehoshaphat has been traditionally identified with the Kidron Valley east of Jerusalem, though the name is symbolic of divine judgment rather than necessarily indicating a specific geographic location.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "decision-valley-of", "isbe": "decision-valley-of"},
        "key_refs": ["Joel 3:14"],
        "sections": []
    },
    "decrees-of-god": {
        "id": "decrees-of-god",
        "term": "Decrees of God",
        "category": "concepts",
        "intro": "<p>The decrees of God are his eternal, sovereign purposes by which he foreordains all things that come to pass, including the salvation of his people. The concept appears throughout Scripture in various formulations: God's counsel stands forever and his plans from generation to generation (Psalm 33:11); his works were planned before the foundation of the world (Ephesians 1:4; 2 Thessalonians 2:13); and all things are known to him from eternity (Acts 15:18). Systematic theology distinguishes between God's decretive will (what he has determined will certainly occur) and his preceptive will (what he commands human beings to do), as well as his decrees of election, reprobation, creation, providence, and redemption. The doctrine of divine decrees has been a central and contested topic in Reformed and Arminian theology, with debates focusing on the relationship between divine sovereignty and human free will.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "decrees-of-god"},
        "key_refs": ["Psalms 33:11", "Ephesians 1:4", "Acts 15:18"],
        "sections": []
    },
    "dedan": {
        "id": "dedan",
        "term": "Dedan",
        "category": "people",
        "intro": "<p>Dedan (meaning <em>their breasts</em>, <em>friendship</em>, or <em>a judge</em>) is the name of two persons and the people descended from them. (1.) A son of Raamah and grandson of Cush (son of Ham), whose descendants became a north Arabian tribe (Genesis 10:7; 1 Chronicles 1:9). (2.) A son of Jokshan and grandson of Abraham by Keturah (Genesis 25:3; 1 Chronicles 1:32). The Dedanites appear in the prophetic writings as traders operating in the northwest Arabian Peninsula, trading with Tyre in saddlecloths for riding (Ezekiel 27:15, 20) and in Isaiah 21:13 as a caravan encamping in the Arabian desert. Jeremiah and Ezekiel include them in oracles against Arabia and Edom (Jeremiah 25:23; 49:8; Ezekiel 25:13).</p>",
        "hitchcock_meaning": "their breasts; friendship; a judge",
        "source_ids": {"easton": "dedan", "smith": "dedan"},
        "key_refs": ["Genesis 10:7", "Isaiah 21:13", "Ezekiel 27:15"],
        "sections": []
    },
    "dedanim": {
        "id": "dedanim",
        "term": "Dedanim",
        "category": "people",
        "intro": "<p>Dedanim (meaning <em>the descendants of Dedan</em>) were the inhabitants or descendants of the Arabian tribe of Dedan (see <strong>Dedan</strong>). The name appears in Isaiah 21:13 in an oracle concerning Arabia, where the Dedanim caravans are depicted as encamped in the forest of Arabia, urged to bring water and bread to the weary fugitives of Tema. The passage envisions a military disaster overtaking these Arabian trading peoples, described as carrying drawn swords. The Dedanim are thus portrayed as a people of commercial importance along the ancient Arabian trade routes who will be disrupted by coming political upheaval.</p>",
        "hitchcock_meaning": "the descendants of Dedan",
        "source_ids": {"easton": "dedanim", "smith": "dedanim"},
        "key_refs": ["Isaiah 21:13"],
        "sections": []
    },
    "dedication-feast-of-the": {
        "id": "dedication-feast-of-the",
        "term": "Dedication, Feast of the",
        "category": "events",
        "intro": "<p>The Feast of Dedication (Hebrew <em>Hanukkah</em>, meaning <em>dedication</em>; John 10:22) was a Jewish festival instituted in 164 B.C. to commemorate the purification and rededication of the Jerusalem temple by Judas Maccabaeus after its desecration by Antiochus IV Epiphanes, who had erected an altar to Zeus and sacrificed swine on it in 167 B.C. The feast lasted eight days beginning on the twenty-fifth of the month Kislev (November/December), celebrated with the lighting of lamps — hence the alternate designation Feast of Lights. It is the only Jewish feast mentioned in the New Testament solely in John's Gospel, where Jesus is found teaching in the temple porticos during the feast when the Jewish leaders press him to declare plainly whether he is the Messiah. The feast's commemoration of Israel's deliverance from foreign oppression provides a fitting context for his discourse on himself as the Good Shepherd who lays down his life for the sheep (John 10:1–30).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dedication-feast-of-the", "smith": "dedication-feast-of-the"},
        "key_refs": ["John 10:22"],
        "sections": []
    },
    "deep": {
        "id": "deep",
        "term": "Deep",
        "category": "concepts",
        "intro": "<p>The deep (<em>tehom</em> in Hebrew, <em>abyssos</em> in Greek) in Scripture denotes both the primordial watery abyss and the realm of the dead or demonic powers. In Genesis 1:2, the Spirit of God hovered over the face of the deep before creation began. The same term describes the flood waters (Genesis 7:11, \"the fountains of the great deep\"). In the New Testament, <em>abyssos</em> (the abyss) refers to the domain of demons (Luke 8:31; Romans 10:7) — the vast depth from which there is no return, and the place to which the dragon will be confined during the millennium (Revelation 20:3). The Psalms use the deep as an image of extreme distress and divine rescue (Psalm 69:15; 88:6). The biblical deep thus combines cosmological, hydrological, and theological meanings under a single potent image of unfathomable depth beyond human reach.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "deep", "isbe": "deep"},
        "key_refs": ["Genesis 1:2", "Luke 8:31", "Romans 10:7", "Revelation 20:3"],
        "sections": []
    },
    "degrees-song-of": {
        "id": "degrees-song-of",
        "term": "Degrees, Song of",
        "category": "concepts",
        "intro": "<p>The Songs of Degrees (also called Songs of Ascents) are a collection of fifteen Psalms (Psalms 120–134) each bearing the superscription <em>shir ha-ma'alot</em>, rendered variously as \"song of degrees,\" \"song of ascents,\" or \"song of steps.\" The most widely accepted interpretation is that these were pilgrimage songs sung by Jewish worshippers as they <em>went up</em> (ascended) to Jerusalem for the three great annual festivals — Passover, Pentecost, and Tabernacles (Deuteronomy 16:16). An alternative view holds that the \"degrees\" refer to the fifteen steps ascending from the Court of Women to the Court of Israel in the temple, on which Levites stood to sing. The collection includes both national prayers (Psalms 120, 126, 132) and intimate hymns of trust and household blessing (Psalms 127, 128, 131, 133).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "degrees-song-of"},
        "key_refs": ["Deuteronomy 16:16"],
        "sections": []
    },
    "dehavites": {
        "id": "dehavites",
        "term": "Dehavites",
        "category": "people",
        "intro": "<p>The Dehavites were one of several peoples listed in Ezra 4:9 as signatories of a letter to Artaxerxes opposing the rebuilding of Jerusalem, described as peoples settled in Samaria by Asnappar (Ashurbanipal) of Assyria. The identification of the Dehavites is uncertain; many scholars read the Aramaic text as simply a form of the Aramaic word for <em>that is</em>, making it a connective particle rather than a proper ethnic name. If genuine, the Dehavites may have been a Mesopotamian or Iranian people. They appear only in this single verse and play no further role in biblical narrative beyond their opposition to the restoration of Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dehavites", "smith": "dehavites"},
        "key_refs": ["Ezra 4:9"],
        "sections": []
    },
    "delaiah": {
        "id": "delaiah",
        "term": "Delaiah",
        "category": "people",
        "intro": "<p>Delaiah (meaning <em>the poor of the Lord</em> or <em>freed by the Lord</em>) is the name of several men in the Old Testament. (1.) A priest to whom the twenty-third division of temple service was assigned in the time of David (1 Chronicles 24:18). (2.) A prince who interceded unsuccessfully with Jehoiakim not to burn Jeremiah's scroll (Jeremiah 36:12, 25). (3.) One whose descendants returned from Babylonian exile with Zerubbabel but could not prove their Israelite ancestry (Ezra 2:60; Nehemiah 7:62). (4.) The father of Shemaiah, a false prophet who tried to intimidate Nehemiah (Nehemiah 6:10). The name was common enough that at least four distinct individuals bore it in the Old Testament period.</p>",
        "hitchcock_meaning": "the poor of the Lord",
        "source_ids": {"easton": "delaiah", "smith": "delaiah", "isbe": "delaiah"},
        "key_refs": ["1 Chronicles 24:18", "Jeremiah 36:12", "Ezra 2:60"],
        "sections": []
    },
    "delilah": {
        "id": "delilah",
        "term": "Delilah",
        "category": "people",
        "intro": "<p>Delilah (meaning <em>languishing</em>, <em>poor</em>, or <em>head of hair</em>) was a Philistine woman living in the Valley of Sorek who was bribed by the five Philistine lords — each offering 1,100 pieces of silver — to discover the source of Samson's supernatural strength and the means of overcoming it (Judges 16:4–20). After three failed attempts using false answers from Samson, Delilah wore him down through persistent pleading until he disclosed that his strength lay in his uncut hair, the sign of his Nazirite vow. She then had his head shaved while he slept on her knees, and the Philistines captured and blinded him. Her name has become proverbial in Western culture for a treacherous woman who betrays a powerful man through intimacy. Samson's final act of strength, bringing down the pillars of the temple of Dagon (Judges 16:28–30), more than compensated for all his captured years.</p>",
        "hitchcock_meaning": "poor; small; head of hair",
        "source_ids": {"easton": "delilah", "isbe": "delilah"},
        "key_refs": ["Judges 16:4", "Judges 16:17"],
        "sections": []
    },
    "deluge": {
        "id": "deluge",
        "term": "Deluge",
        "category": "events",
        "intro": "<p>The Deluge (Latin <em>diluvium</em>) is the name given to the great flood of Noah's day recorded in Genesis 6–9 — the most catastrophic judgment in human history before the final judgment. Its cause was the universal corruption and violence of antediluvian humanity (Genesis 6:5–12). God commanded Noah to build the ark and bring aboard his family and representatives of all animal kinds. The flood began when the fountains of the great deep burst open and the windows of heaven were opened (Genesis 7:11), inundating the earth for 150 days before the waters receded. Noah, his wife, his three sons and their wives — eight persons in total — survived aboard the ark. God's covenant with Noah after the flood, marked by the rainbow, guaranteed that the earth would never again be destroyed by water (Genesis 9:11–17). The New Testament cites the flood as a historical event typologically connected to baptism (1 Peter 3:20–21) and as a model of judgment preceding Christ's return (Matthew 24:37–39; 2 Peter 3:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "deluge", "smith": "deluge"},
        "key_refs": ["Genesis 7:11", "Genesis 9:11", "Matthew 24:37", "1 Peter 3:20"],
        "sections": []
    },
    "demas": {
        "id": "demas",
        "term": "Demas",
        "category": "people",
        "intro": "<p>Demas (meaning <em>popular</em>) was a co-worker of Paul who is mentioned three times in the New Testament, and his trajectory traces a sobering arc of apostasy. He is first mentioned as a fellow laborer alongside Luke in Paul's greeting from Rome (Philemon 1:24) and is named again in Colossians 4:14. However, in Paul's final letter, written from his second Roman imprisonment, he reports with evident grief: \"Demas, in love with this present world, has deserted me and gone to Thessalonica\" (2 Timothy 4:10). The contrast with Luke, who remained faithful, and with Crescens and Titus, who departed on missions, underscores that Demas's departure was motivated not by gospel work but by worldly attraction. He became a cautionary figure for the love of the world over faithfulness to Christ.</p>",
        "hitchcock_meaning": "popular",
        "source_ids": {"easton": "demas", "smith": "demas", "isbe": "demas"},
        "key_refs": ["Philemon 1:24", "Colossians 4:14", "2 Timothy 4:10"],
        "sections": []
    },
    "demetrius": {
        "id": "demetrius",
        "term": "Demetrius",
        "category": "people",
        "intro": "<p>Demetrius (meaning <em>belonging to Ceres</em>, the goddess of grain) is the name of two men in the New Testament. (1.) A silversmith at Ephesus who made silver shrines of the goddess Artemis and led the riot against Paul, fearing that Paul's preaching about idols made with hands would destroy his profitable trade and dishonor the great goddess (Acts 19:24–40). The riot filled the theater with thousands crying out for Artemis until the city clerk quieted them. (2.) A believer commended by the apostle John as having a good testimony from everyone, from the truth itself, and from John and his companions (3 John 1:12). Whether he was the bearer of John's third epistle is uncertain but plausible.</p>",
        "hitchcock_meaning": "belonging to corn, or to Ceres",
        "source_ids": {"easton": "demetrius", "smith": "demetrius"},
        "key_refs": ["Acts 19:24", "3 John 1:12"],
        "sections": []
    },
    "demon": {
        "id": "demon",
        "term": "Demon",
        "category": "concepts",
        "intro": "<p>Demons in Scripture are personal, malevolent spiritual beings — fallen angels aligned with Satan — who oppose God and human flourishing. The Old Testament rarely uses the term directly but refers to evil spirits (Judges 9:23; 1 Samuel 16:14) and to the idols of the nations as demons to whom sacrifices were offered (Deuteronomy 32:17; Psalm 106:37). In the New Testament, demons (Greek <em>daimonia</em>) are portrayed as intelligent beings who recognized Jesus's divine identity and authority (Mark 1:24; 5:7), capable of possessing and tormenting human beings (Matthew 8:28–34), and subject to exorcism by Jesus's word and, through his name, by his disciples (Matthew 10:1). Paul warns that behind pagan idol worship stand demons rather than true deities (1 Corinthians 10:20–21). Their final destiny is the lake of fire (Matthew 25:41; Revelation 20:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "demon", "smith": "demon"},
        "key_refs": ["Deuteronomy 32:17", "Mark 1:24", "1 Corinthians 10:20"],
        "sections": []
    },
    "den": {
        "id": "den",
        "term": "Den",
        "category": "concepts",
        "intro": "<p>A den in Scripture typically refers to a cave or hollow in the earth used as a hiding place or dwelling — for animals, for people in distress, or metaphorically for criminals. Lions retire to their dens at dawn (Job 37:8; 38:40; Psalm 104:22), making the den a symbol of wild, dangerous territory. The den of lions into which Daniel was cast (Daniel 6:16–23) is the most famous biblical den, and his miraculous deliverance from it became a paradigmatic example of God's protection of the faithful (Hebrews 11:33). Jesus condemned the money-changers in the temple by citing Jeremiah 7:11 — they had made the house of prayer into a den of robbers (Matthew 21:13). In the Revelation, the hiding of the great and the small in dens and rocks of the mountains (Revelation 6:15) images the terror of the day of wrath.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "den", "isbe": "den"},
        "key_refs": ["Psalms 104:22", "Daniel 6:16", "Matthew 21:13"],
        "sections": []
    },
    "deputy": {
        "id": "deputy",
        "term": "Deputy",
        "category": "concepts",
        "intro": "<p>Deputy in the Old Testament translates Hebrew terms for viceroy, governor, or regional administrator acting on behalf of a higher authority. The \"deputy\" who governed Edom during a period of Judah's dominance (1 Kings 22:47) was a vassal regent. Solomon's twelve deputies administered the regions of Israel, each responsible for provisioning the royal household for one month of the year (1 Kings 4:5, 7–19). In the New Testament, the Greek <em>anthypatos</em> (proconsul) is rendered \"deputy\" in the KJV (Acts 13:7–8, 12; 18:12; 19:38), designating the Roman senatorial governor of a province. The proconsul Sergius Paulus of Cyprus became a believer after witnessing Paul's confrontation with Bar-Jesus the sorcerer (Acts 13:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "deputy", "smith": "deputy", "isbe": "deputy"},
        "key_refs": ["1 Kings 22:47", "Acts 13:7"],
        "sections": []
    },
    "derbe": {
        "id": "derbe",
        "term": "Derbe",
        "category": "places",
        "intro": "<p>Derbe (meaning <em>a sting</em>) was a city in the southeastern region of Lycaonia in Asia Minor (modern Turkey), part of the Roman province of Galatia. Paul and Barnabas visited it on the first missionary journey after being driven from Lystra by Jews from Antioch and Iconium (Acts 14:20–21), and Paul passed through it again on his second journey (Acts 16:1). The city was the home of Gaius, one of Paul's traveling companions (Acts 20:4). An inscription discovered in the mid-twentieth century at Kerti Hüyük near Karaman has helped confirm the probable location of Derbe. Unlike at Lystra, where Paul was stoned, his time at Derbe appears to have been productive and peaceful, resulting in the discipling of \"many.\"</p>",
        "hitchcock_meaning": "a sting",
        "source_ids": {"easton": "derbe", "smith": "derbe", "isbe": "derbe"},
        "key_refs": ["Acts 14:20", "Acts 16:1", "2 Timothy 3:11"],
        "sections": []
    },
    "desert": {
        "id": "desert",
        "term": "Desert",
        "category": "places",
        "intro": "<p>Desert in Scripture encompasses both literally arid, uninhabited wilderness regions and a theologically charged space of encounter with God. The Hebrew terms include <em>midbar</em> (uninhabited land, often pastured), <em>arabah</em> (the Jordan-Rift Valley desert plain), and <em>yeshimon</em> (desolation). Israel's forty years of wilderness wandering in the <em>midbar</em> were a formative period of both divine provision and testing: manna, water from rock, and the pillar of cloud and fire all accompanied the nation through the desert. The prophets anticipated a new exodus through a desert highway (Isaiah 40:3; 43:19–20), a vision fulfilled in John the Baptist's ministry \"in the wilderness\" (Matthew 3:1–3; Mark 1:3–4). Jesus himself was led by the Spirit into the desert to be tempted (Matthew 4:1), and Paul spent time in Arabia after his conversion (Galatians 1:17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "desert", "smith": "desert", "isbe": "desert"},
        "key_refs": ["Exodus 3:1", "Isaiah 40:3", "Matthew 4:1"],
        "sections": []
    },
    "desire-of-all-nations": {
        "id": "desire-of-all-nations",
        "term": "Desire of All Nations",
        "category": "concepts",
        "intro": "<p>\"The desire of all nations\" is a messianic phrase from Haggai 2:7, where the prophet promises that God will shake the nations and the desire (or treasures) of all nations will come to fill the second temple with glory surpassing the first. The Hebrew <em>chemdah</em> (desire, treasure, delight) has been interpreted in two ways: (1.) as the precious things or tribute of the nations flowing into Jerusalem (as in Isaiah 60:5–7), giving the verse an economic and political sense; or (2.) messianically, as the one yearned for by all peoples — identifying the promised one with Christ, whose coming to the second temple in his incarnation fulfilled the prophecy's deeper intent. The Vulgate's rendering <em>desideratus cunctis gentibus</em> (the Desired of All Nations) gave rise to the messianic interpretation prominent in Christian hymnody and devotion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "desire-of-all-nations", "isbe": "desire-of-all-nations"},
        "key_refs": ["Haggai 2:7"],
        "sections": []
    },
    "desolation-abomination-of": {
        "id": "desolation-abomination-of",
        "term": "Desolation, Abomination of",
        "category": "concepts",
        "intro": "<p>The Abomination of Desolation (Hebrew <em>shiqqutz shomem</em>) is a phrase from Daniel 9:27; 11:31; and 12:11 referring to a desecrating sacrilege that causes the temple to become desolate, deprived of its legitimate worship. The immediate historical fulfillment occurred in 167 B.C. when Antiochus IV Epiphanes erected an altar to Zeus in the Jerusalem temple and sacrificed swine on it (1 Maccabees 1:54). Jesus applied the same prophecy to a future desolation connected with the destruction of the temple (Matthew 24:15; Mark 13:14), warning his disciples in Judea to flee when they see it standing in the holy place. Luke's parallel (Luke 21:20) interprets it as the surrounding of Jerusalem by armies, which occurred in A.D. 70 under Titus. Many interpreters see a dual fulfillment — both in A.D. 70 and in a yet-future eschatological event — consistent with Daniel's typological pattern.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "desolation-abomination-of", "isbe": "desolation-abomination-of"},
        "key_refs": ["Daniel 9:27", "Matthew 24:15", "Mark 13:14", "Luke 21:20"],
        "sections": []
    },
    "destroyer": {
        "id": "destroyer",
        "term": "Destroyer",
        "category": "concepts",
        "intro": "<p>The destroyer in Scripture refers to angelic or divine agents of judgment bringing death. In the Exodus narrative, the destroyer (<em>ha-mashchit</em>) struck down the firstborn of Egypt on the night of Passover, passing over the Israelite houses marked with blood (Exodus 12:23). In the wilderness, the destroying angel (<em>malach ha-mashchit</em>) was the agent of the plague that killed 70,000 Israelites as a result of David's census (2 Samuel 24:15–16; 1 Chronicles 21:15). Paul references the destroyer from the Exodus account when warning the Corinthians against testing God as Israel did (1 Corinthians 10:10). In Hebrews 11:28, keeping the Passover and sprinkling blood is cited as the act by which Moses preserved Israel from the destroyer — and the typological connection to Christ's blood as the ultimate protection from divine judgment is explicit in the broader context.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "destroyer", "isbe": "destroyer"},
        "key_refs": ["Exodus 12:23", "2 Samuel 24:16", "1 Corinthians 10:10"],
        "sections": []
    },
    "destruction": {
        "id": "destruction",
        "term": "Destruction",
        "category": "concepts",
        "intro": "<p>Destruction in the Old Testament (Hebrew <em>Abaddon</em> and <em>sheol</em>) refers to the underworld realm of the dead, often used as a synonym or parallel for Sheol. Job speaks of \"Destruction\" (<em>Abaddon</em>) as having no covering before God (Job 26:6; 28:22), and it is personified alongside Death as a witness to human folly. Abaddon appears in Revelation 9:11 as the name of the angel of the bottomless pit — in Hebrew Abaddon, in Greek Apollyon (Destroyer) — designating a demonic ruler over the realm of destruction. In the New Testament, destruction (<em>apoleia</em>) also designates eternal perdition, the final state of the lost (Matthew 7:13; Philippians 3:19; 2 Peter 3:7), as opposed to life and salvation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "destruction", "isbe": "destruction"},
        "key_refs": ["Job 26:6", "Revelation 9:11", "Matthew 7:13"],
        "sections": []
    },
    "destruction-city-of": {
        "id": "destruction-city-of",
        "term": "Destruction, City of",
        "category": "places",
        "intro": "<p>The City of Destruction appears in Isaiah 19:18 in a remarkable prophecy of Egypt's future conversion: \"In that day five cities in the land of Egypt will speak the language of Canaan and swear allegiance to the LORD of hosts. One of these will be called the City of Destruction.\" Some Hebrew manuscripts read <em>ir ha-heres</em> (City of the Sun, i.e., Heliopolis/On), which the Septuagint preserves as the City of the Sun. The reading \"City of Destruction\" (<em>ir ha-heres</em> with different pointing) has been interpreted as either a deliberate wordplay on the pagan city's name or as a reference to a city that once worshipped the sun-god being turned to the worship of the LORD. The entire oracle (Isaiah 19:18–25) envisions Egypt, Assyria, and Israel worshipping together — one of the most universalistic passages in the prophets.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "destruction-city-of"},
        "key_refs": ["Isaiah 19:18"],
        "sections": []
    },
    "deuteronomy": {
        "id": "deuteronomy",
        "term": "Deuteronomy",
        "category": "concepts",
        "intro": "<p>Deuteronomy (from Greek <em>deuteronomion</em>, meaning <em>second law</em> or <em>repetition of the law</em>, translating the LXX's rendering of Deuteronomy 17:18) is the fifth book of the Pentateuch and Moses's final address to Israel on the plains of Moab before the entry into Canaan. Composed primarily as three extended sermons by Moses, it recapitulates and expands the law given at Sinai, emphasizing covenant loyalty, the central sanctuary, love for God with all one's heart, and the consequences of obedience and disobedience (the blessings and curses of chapters 27–28). The Shema (Deuteronomy 6:4–9) — \"Hear, O Israel: the LORD our God, the LORD is one\" — is the foundational confession of Jewish faith. Jesus cited Deuteronomy in each of his three responses to the devil's temptations (Matthew 4:4, 7, 10) and called the command to love God with all one's heart (Deuteronomy 6:5) the greatest commandment. The book concludes with Moses's death and the appointment of Joshua as his successor.</p>",
        "hitchcock_meaning": "repetition of the law",
        "source_ids": {"easton": "deuteronomy", "smith": "deuteronomy", "isbe": "deuteronomy"},
        "key_refs": ["Deuteronomy 6:4", "Matthew 4:4", "Matthew 22:37"],
        "sections": []
    },
    "devil": {
        "id": "devil",
        "term": "Devil",
        "category": "concepts",
        "intro": "<p>Devil (Greek <em>diabolos</em>, slanderer or accuser) is the name given in the New Testament to the supreme adversary of God and humanity, identified with Satan (<em>adversary</em> in Hebrew). He is portrayed as a personal being of great power and intelligence who fell through pride (1 Timothy 3:6; Isaiah 14:12–15), who tempted Adam and Eve in Eden (Genesis 3; Revelation 12:9), who appears as an accuser of the brethren before God (Job 1:6–12; Zechariah 3:1–2; Revelation 12:10), and who tempted Jesus directly in the wilderness (Matthew 4:1–11). He is called the ruler of this world (John 12:31; 14:30), the god of this age (2 Corinthians 4:4), the prince of the power of the air (Ephesians 2:2), and a murderer and liar from the beginning (John 8:44). Christ's mission was to destroy the works of the devil (1 John 3:8; Hebrews 2:14), accomplished definitively in the cross and resurrection, with his final defeat at the last judgment (Revelation 20:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "devil", "smith": "devil", "isbe": "devil"},
        "key_refs": ["Job 1:6", "Matthew 4:1", "John 8:44", "Revelation 20:10"],
        "sections": []
    },
    "dew": {
        "id": "dew",
        "term": "Dew",
        "category": "concepts",
        "intro": "<p>Dew was of vital agricultural importance in Palestine, where the long dry summer (May–October) brought no rain and crops depended on the heavy night dews drawn from Mediterranean moisture. Its presence or absence was accordingly treated as a sign of divine blessing or curse. Isaac's blessing to Jacob included \"the dew of heaven\" (Genesis 27:28), and the absence of dew was part of Elijah's curse on Israel during the drought (1 Kings 17:1). God's provision of manna came with the morning dew (Exodus 16:13–14). In prophetic imagery, dew symbolizes gentle, life-giving divine blessing: the LORD's teaching falls like dew (Deuteronomy 32:2); the remnant of Jacob will be like dew among the nations (Micah 5:7); and the Messiah's coming will be like dew on the mown grass (Psalm 72:6). Gideon's fleece test involving dew remains one of Scripture's most memorable signs of divine confirmation (Judges 6:36–40).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dew", "smith": "dew", "isbe": "dew"},
        "key_refs": ["Genesis 27:28", "Deuteronomy 32:2", "Psalms 72:6", "Judges 6:37"],
        "sections": []
    },
    "diadem": {
        "id": "diadem",
        "term": "Diadem",
        "category": "concepts",
        "intro": "<p>Diadem in Scripture refers to a royal headdress or turban signifying authority and dignity, distinct from the crown (<em>kether</em>) in Hebrew thought. The high priest's turban included a diadem-like ornament (Ezekiel 21:26; Isaiah 28:5). Job used the imagery of wearing justice as a robe and his turban (<em>tsanif</em>) as a diadem to describe his former role as an advocate for the poor and needy (Job 29:14). In prophetic literature, God himself is described as a diadem of beauty to his people (Isaiah 28:5), and the restored Zion will hold a royal diadem in the LORD's hand (Isaiah 62:3). In the New Testament, the Greek <em>diadema</em> (as opposed to <em>stephanos</em>, the victor's wreath) designates the royal crown worn by the dragon (Revelation 12:3), the beast (Revelation 13:1), and the conquering Christ (Revelation 19:12), marking sovereign dominion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "diadem", "smith": "diadem", "isbe": "diadem"},
        "key_refs": ["Ezekiel 21:26", "Isaiah 28:5", "Job 29:14", "Revelation 19:12"],
        "sections": []
    },
    "dial": {
        "id": "dial",
        "term": "Dial",
        "category": "concepts",
        "intro": "<p>The dial (Hebrew <em>ma'aloth</em>, steps or degrees) of Ahaz is one of Scripture's most remarkable accounts of divine miracle-working to confirm a prophetic sign. When King Hezekiah was mortally ill and prayed for healing, the prophet Isaiah promised recovery and as a sign caused the shadow on the stairway (sundial) of Ahaz to go backward ten steps — either a reversal of the sun's apparent movement or a phenomenon of refraction causing the shadow to retreat (2 Kings 20:9–11; Isaiah 38:7–8). The term likely refers to a series of graduated steps on which the sun cast a measurable shadow, functioning as a time-keeping device. It represents both the reality of the miracle and the physical sign confirming God's word to Hezekiah that he would live an additional fifteen years.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dial", "smith": "dial"},
        "key_refs": ["2 Kings 20:11", "Isaiah 38:8"],
        "sections": []
    },
    "diamond": {
        "id": "diamond",
        "term": "Diamond",
        "category": "concepts",
        "intro": "<p>Diamond in the KJV translates two distinct Hebrew terms. (1.) <em>Yahalom</em> (Exodus 28:18; 39:11; Ezekiel 28:13), the third stone in the second row of the high priest's breastplate, is now generally rendered as <em>moonstone</em>, <em>jasper</em>, or <em>emerald</em> by modern translators, since the hardness of true diamond was not exploited in ancient lapidary work and the exact mineral is uncertain. (2.) <em>Shamir</em> (Jeremiah 17:1; Ezekiel 3:9) is an extremely hard material used as a cutting or engraving tool — rendered as diamond, emery, or flint in various translations. Jeremiah uses it metaphorically: \"The sin of Judah is written with an iron pen; with a point of diamond it is engraved on the tablet of their heart\" (Jeremiah 17:1), conveying the indelible, deeply etched nature of Israel's spiritual corruption.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "diamond", "smith": "diamond", "isbe": "diamond"},
        "key_refs": ["Exodus 28:18", "Jeremiah 17:1", "Ezekiel 28:13"],
        "sections": []
    },
}


def main():
    written = 0
    skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP d1: Daberath → Diamond: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
