#!/usr/bin/env python3
"""BP S4: Ships → Soap (75 Easton entries)"""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(fp):
        with open(fp) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    with open(fp, 'w') as f:
        json.dump(data, f, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "ships": {
        "id": "ships",
        "term": "Ships",
        "category": "concepts",
        "intro": "<p>Ships appear throughout Scripture as instruments of commerce, war, and providential rescue. The Phoenicians were the great maritime traders of the ancient Near East, and Jacob's prophecy that Zebulun would dwell at the seashore and become a haven for ships (Genesis 49:13) anticipates Israel's later coastal connections. Moses warned that Egypt would drive Israel back in ships as a sign of covenant curse (Deuteronomy 28:68), while Job compared the swift passing of time to ships of reed rushing down a river (Job 9:26).</p><p>The most detailed New Testament maritime account is Paul's voyage to Rome, recounted in Acts 27, where a severe storm nearly destroyed the grain ship carrying him — an account notable for its precise nautical vocabulary and realistic detail. Revelation 18:17–19 mourns the fall of Babylon through the lament of shipmasters and sailors who watched her wealth destroyed in a single hour. Isaiah 2:16 includes <em>ships of Tarshish</em> among the proud things that will be humbled on the day of the LORD — Tarshish ships being large ocean-going vessels, possibly trading as far as Spain.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ships"},
        "key_refs": ["Acts 27:41", "Revelation 18:17", "Isaiah 2:16", "Genesis 49:13"]
    },
    "shishak-i": {
        "id": "shishak-i",
        "term": "Shishak I",
        "category": "people",
        "intro": "<p>Shishak I (Egyptian <em>Sheshonk I</em>, c. 945–924 BC) was the founder of Egypt's Twenty-Second Dynasty and the pharaoh who invaded Judah in the fifth year of Rehoboam's reign. Having sheltered Jeroboam during the latter's flight from Solomon (1 Kings 11:40), Shishak moved against Judah shortly after the kingdom divided. His campaign swept through the fortified cities of Judah and reached Jerusalem, where he plundered the temple treasury and the palace — taking the golden shields Solomon had made (1 Kings 14:25–26; 2 Chronicles 12:2–9).</p><p>Shishak's own record of this campaign is preserved on the south wall of the temple at Karnak, where he lists the Palestinian towns he captured — a list that includes hundreds of place names and constitutes important extra-biblical confirmation of the biblical account. The prophet Shemaiah told Rehoboam that the invasion was a judgment for forsaking the LORD, but when the king and princes humbled themselves, God promised partial deliverance: they would be servants to Shishak rather than destroyed (2 Chronicles 12:7).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shishak-i"},
        "key_refs": ["1 Kings 14:25", "2 Chronicles 12:2", "1 Kings 11:40"]
    },
    "shittah-tree": {
        "id": "shittah-tree",
        "term": "Shittah-tree",
        "category": "concepts",
        "intro": "<p>The shittah-tree (Hebrew <em>shittah</em>, plural <em>shittim</em>) is the acacia — almost certainly <em>Acacia tortilis</em> or related species common to the Sinai peninsula and arid regions of Palestine. It is a thorny, drought-resistant tree yielding a hard, fine-grained, reddish-brown timber highly resistant to decay. Isaiah 41:19 lists the shittah tree among the trees God promises to plant in the wilderness as a sign of restoration.</p><p>Its primary biblical importance lies in its use in the construction of the Mosaic Tabernacle. The ark of the covenant, the table of showbread, the altar of burnt offering, the altar of incense, and the boards and pillars of the Tabernacle structure were all made of shittim wood overlaid with gold or bronze (Exodus 25–27; 37–38). The selection of this particular wood — durable, abundant in the Sinai desert, and light enough for a portable sanctuary — suited Israel's wilderness situation. The shittim stands at Shittim (Abel-shittim) in Moab likely derive their name from groves of this tree in the valley.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shittah-tree"},
        "key_refs": ["Exodus 25:10", "Exodus 25:23", "Isaiah 41:19"]
    },
    "shittim": {
        "id": "shittim",
        "term": "Shittim",
        "category": "places",
        "intro": "<p>Shittim (meaning <em>acacias</em>), also called Abel-shittim (Numbers 33:49), was the final encampment of Israel in the plains of Moab before crossing the Jordan into Canaan. Situated east of the Jordan, likely in the valley of the Wadi el-Kefrein, it was from here that Joshua sent two spies to Jericho (Joshua 2:1) and from here that Israel crossed over (Joshua 3:1). The site thus marks the transition from the wilderness wandering to the conquest.</p><p>Shittim was also the scene of Israel's catastrophic sin with the Moabite and Midianite women, who enticed the Israelites to worship Baal of Peor (Numbers 25:1–9). This episode resulted in a plague that killed 24,000 people, arrested only when Phinehas son of Eleazar executed a brazen Israelite and the Midianite woman he had brought into the camp. The prophet Micah later contrasted Balak's plot at Shittim with what the LORD did from Shittim to Gilgal as an invitation to remember God's saving acts (Micah 6:5).</p>",
        "sections": [],
        "hitchcock_meaning": "thorns",
        "source_ids": {"easton": "shittim", "smith": "shittim", "isbe": "shittim"},
        "key_refs": ["Numbers 25:1", "Numbers 33:49", "Joshua 2:1", "Micah 6:5"]
    },
    "shoa": {
        "id": "shoa",
        "term": "Shoa",
        "category": "places",
        "intro": "<p>Shoa appears in Ezekiel 23:23 as one of the nations summoned by God to execute judgment on Jerusalem, personified as the unfaithful woman Oholibah: <em>the Babylonians and all the Chaldeans, Pekod and Shoa and Koa, and all the Assyrians with them.</em> The identification of Shoa has been debated, but most scholars associate it with the Suti or Sutu — a semi-nomadic people attested in Assyrian records as inhabiting the mountain districts to the northeast of Babylonia. Some equate the name with the <em>Quti</em> or <em>Guti</em> of ancient Mesopotamian sources. Whatever its precise identification, Shoa appears as part of a coalition of Babylonian-aligned peoples representing the overwhelming military force arrayed against Judah in Ezekiel's prophetic vision of coming judgment.</p>",
        "sections": [],
        "hitchcock_meaning": "kings; tyrants",
        "source_ids": {"easton": "shoa", "smith": "shoa", "isbe": "shoa"},
        "key_refs": ["Ezekiel 23:23"]
    },
    "shobab": {
        "id": "shobab",
        "term": "Shobab",
        "category": "people",
        "intro": "<p>Shobab is a biblical name borne by two persons. (1.) A son of David born to him in Jerusalem by Bathsheba (2 Samuel 5:14; 1 Chronicles 3:5; 14:4). He is listed among the sons born to David after he became king in Jerusalem, but nothing further is recorded about him. (2.) A son of Caleb son of Hezron by his wife Azubah (1 Chronicles 2:18). He belonged to the tribe of Judah and is listed in the genealogical records of that tribe, though again without narrative detail. The name may mean <em>returned</em> or <em>rebellious</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "returned; turned back; a spark",
        "source_ids": {"easton": "shobab", "smith": "shobab", "isbe": "shobab"},
        "key_refs": ["2 Samuel 5:14", "1 Chronicles 3:5"]
    },
    "shobach": {
        "id": "shobach",
        "term": "Shobach",
        "category": "people",
        "intro": "<p>Shobach was the commander of the Syrian (Aramean) army under Hadadezer king of Zobah when Joab defeated the Syrians during David's wars with the Ammonites (2 Samuel 10:16–18). After the initial defeat at Rabbah, Hadadezer gathered additional Syrian forces from beyond the Euphrates at Helam. David himself led the Israelite army against them, routed the Syrians, and Shobach was mortally wounded and died on the battlefield. He is called Shophach in the parallel account in 1 Chronicles 19:16–18. His death marked the end of effective Syrian resistance during this phase of David's campaigns, causing the Syrian vassal states to make peace with Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "your bonds; your chains",
        "source_ids": {"easton": "shobach", "smith": "shobach", "isbe": "shobach"},
        "key_refs": ["2 Samuel 10:16", "1 Chronicles 19:16"]
    },
    "shobai": {
        "id": "shobai",
        "term": "Shobai",
        "category": "people",
        "intro": "<p>Shobai was the head of a family of gatekeepers whose descendants returned to Jerusalem from the Babylonian exile with Zerubbabel (Ezra 2:42; Nehemiah 7:45). His family is listed among the temple servants who came back to resume their duties in the restored community. The gatekeepers were responsible for the security and oversight of the temple precincts, and the restoration of their office was an important part of reconstituting proper worship in Jerusalem after the exile. Shobai himself presumably lived before the exile, and this post-exilic list preserves his name as the founding figure of this particular gatekeeper family.</p>",
        "sections": [],
        "hitchcock_meaning": "turning captivity",
        "source_ids": {"easton": "shobai", "smith": "shobai", "isbe": "shobai"},
        "key_refs": ["Ezra 2:42", "Nehemiah 7:45"]
    },
    "shobal": {
        "id": "shobal",
        "term": "Shobal",
        "category": "people",
        "intro": "<p>Shobal is a name borne by three biblical figures. (1.) A son of Seir the Horite and chief of one of the Horite clans of Edom (Genesis 36:20, 23; 1 Chronicles 1:38, 40). He was ancestor of several sub-clans of the Edomites. (2.) A son of Caleb son of Hur, the founder or chief of Kiriath-jearim (1 Chronicles 2:50, 52), one of the towns assigned to the tribe of Judah. His descendants included various sub-clans who settled in the region. (3.) A son of Judah by an unnamed mother (1 Chronicles 4:1–2), listed in the expanded genealogy of Judah. The repetition of this name across different genealogical threads may reflect the blending of Hurrite and Judahite tribal memories in the Chronicler's record.</p>",
        "sections": [],
        "hitchcock_meaning": "path; ear of corn",
        "source_ids": {"easton": "shobal", "smith": "shobal", "isbe": "shobal"},
        "key_refs": ["Genesis 36:20", "1 Chronicles 2:50"]
    },
    "shobi": {
        "id": "shobi",
        "term": "Shobi",
        "category": "people",
        "intro": "<p>Shobi son of Nahash from Rabbah of the Ammonites was one of three men who showed unexpected kindness to David during his flight from Absalom. Together with Machir son of Ammiel from Lo-debar and Barzillai the Gileadite, Shobi met the weary king at Mahanaim and supplied him with beds, basins, earthen vessels, wheat, barley, flour, parched grain, beans, lentils, honey, curds, sheep, and cheese (2 Samuel 17:27–29). His father Nahash had previously shown kindness to David — Nahash king of Ammon whose son Hanun later humiliated David's envoys, precipitating war. Shobi may have been a brother of Hanun who remained loyal to David and was rewarded with authority over Rabbah after its capture.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shobi", "smith": "shobi", "isbe": "shobi"},
        "key_refs": ["2 Samuel 17:27"]
    },
    "shocho": {
        "id": "shocho",
        "term": "Shocho",
        "category": "places",
        "intro": "<p>Shocho (also spelled Shochoh, Sochoh, Socoh, or Shoco) was a town in the lowland territory of Judah (the Shephelah). It appears in Joshua 15:35 in the list of cities of Judah in the valley, and is important as the site near which the Philistines encamped before the battle of Elah, when David killed Goliath: <em>the Philistines gathered their armies at Socoh, which belongs to Judah</em> (1 Samuel 17:1). The valley of Elah lay between Socoh and Azekah, and the two armies faced each other across it for forty days before the decisive confrontation. Later, Rehoboam fortified the city as part of his chain of defenses for Judah (2 Chronicles 11:7).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shocho", "smith": "shocho"},
        "key_refs": ["1 Samuel 17:1", "Joshua 15:35", "2 Chronicles 11:7"]
    },
    "shoe": {
        "id": "shoe",
        "term": "Shoe",
        "category": "concepts",
        "intro": "<p>Shoes (sandals) in biblical culture carried significant social and legal symbolism beyond their practical function as foot protection. Removing the sandal was a sign of humility and reverence — God commanded Moses to remove his sandals at the burning bush because he stood on holy ground (Exodus 3:5), and Joshua received the same command at Jericho (Joshua 5:15). The act of loosening or carrying another's sandals was a task too menial for a disciple — John the Baptist's declaration that he was not worthy to untie the sandal of the Coming One expressed extreme deference (John 1:27; Mark 1:7).</p><p>In the Mosaic law, the ceremony of <em>halitzah</em> (literally <em>taking off the sandal</em>) released a surviving brother from levirate marriage obligation; the widow drew off his sandal and spat in his face as a public mark of dishonor (Deuteronomy 25:9). Ruth 4:7–8 records the related custom of removing the sandal to ratify a property transaction. Ephesians 6:15 uses the image of sandal-wearing as a metaphor for the readiness that comes from the gospel of peace.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shoe", "smith": "shoe"},
        "key_refs": ["Exodus 3:5", "John 1:27", "Deuteronomy 25:9", "Ephesians 6:15"]
    },
    "shomer": {
        "id": "shomer",
        "term": "Shomer",
        "category": "people",
        "intro": "<p>Shomer is the name of two biblical individuals. (1.) The mother of Jehozabad, one of the conspirators who assassinated King Joash of Judah (2 Kings 12:21). She is called Shimrith the Moabitess in 2 Chronicles 24:26, suggesting a Moabite origin. (2.) A son of Heber of the tribe of Asher (1 Chronicles 7:32), also called Shemer in verse 34, listed in the Asherite genealogy. The name means <em>keeper</em> or <em>guardian</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "keeper; dregs",
        "source_ids": {"easton": "shomer", "smith": "shomer", "isbe": "shomer"},
        "key_refs": ["2 Kings 12:21", "1 Chronicles 7:32"]
    },
    "shophan": {
        "id": "shophan",
        "term": "Shophan",
        "category": "places",
        "intro": "<p>Shophan was a fortified city in Transjordan, mentioned in Numbers 32:35 as one of the cities built or fortified by the tribe of Gad after they requested and received their allotment on the east side of the Jordan. The full designation in the Masoretic text is <em>Atroth-shophan</em>, suggesting it may be a compound place name linked with the nearby site of Atroth. The Gadites undertook to build these cities as safe enclosures for their livestock and defensible towns for their families before crossing with the Israelite army to assist in the conquest of Canaan. The exact site of Shophan remains unidentified.</p>",
        "sections": [],
        "hitchcock_meaning": "rabbit; hid",
        "source_ids": {"easton": "shophan", "smith": "shophan", "isbe": "shophan"},
        "key_refs": ["Numbers 32:35"]
    },
    "shoshannim": {
        "id": "shoshannim",
        "term": "Shoshannim",
        "category": "concepts",
        "intro": "<p>Shoshannim (Hebrew <em>lilies</em>) is a musical or liturgical direction found in the superscriptions of Psalms 45, 69, and 80 (where it appears as <em>Shoshannim-Eduth</em> and <em>Shoshan Eduth</em>). Its precise meaning as a performance instruction is uncertain. The most common interpretation is that it designates either a musical instrument shaped like a lily, a melody or tune known by this title, or a specific musical mode. The Septuagint translates the word as <em>concerning the things that will be changed</em>, reflecting an alternative reading of the Hebrew root. Psalm 45 is a royal wedding song; Psalm 69 is a lament; Psalm 80 is a communal prayer for restoration — the common liturgical designation suggests these diverse psalms were performed using a shared musical tradition.</p>",
        "sections": [],
        "hitchcock_meaning": "those that shall be changed",
        "source_ids": {"easton": "shoshannim", "smith": "shoshannim"},
        "key_refs": ["Psalm 45:1", "Psalm 69:1", "Psalm 80:1"]
    },
    "shoshannim-eduth": {
        "id": "shoshannim-eduth",
        "term": "Shoshannim-Eduth",
        "category": "concepts",
        "intro": "<p>Shoshannim-Eduth appears in the superscription of Psalm 80 as a musical or liturgical designation. The compound combines <em>shoshannim</em> (lilies) with <em>eduth</em> (testimony or witness). It is closely related to <em>Shushan Eduth</em> in Psalm 60. The exact meaning of the compound remains uncertain to scholars: it may indicate a tune named <em>Lily of the Testimony</em>, a type of instrument associated with covenant testimony, or a specific performance mode for psalms connected with Israel's covenant relationship with God. Psalm 80 itself is a communal lament calling on God the Shepherd of Israel to restore the nation, making the testimony dimension of the title thematically appropriate.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shoshannim-eduth", "isbe": "shoshannim-eduth"},
        "key_refs": ["Psalm 80:1", "Psalm 60:1"]
    },
    "shrines-silver": {
        "id": "shrines-silver",
        "term": "Shrines, Silver",
        "category": "concepts",
        "intro": "<p>Silver shrines of Artemis (Diana) were miniature reproductions of the great temple of Artemis at Ephesus, sold to pilgrims and worshippers as votive objects and souvenirs. Acts 19:23–27 records that a silversmith named Demetrius, who made these silver shrines, stirred up a riot in Ephesus when Paul's preaching of the gospel began to threaten the trade. Demetrius warned his fellow craftsmen that not only their business was in danger but also the reputation of the great goddess Artemis herself. The ensuing uproar — the crowd chanting <em>Great is Artemis of the Ephesians!</em> for two hours in the theater — illustrates both the economic entanglement of idol-worship and the social disruption that the gospel caused in cities where it took hold.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shrines-silver"},
        "key_refs": ["Acts 19:24", "Acts 19:27"]
    },
    "shua": {
        "id": "shua",
        "term": "Shua",
        "category": "people",
        "intro": "<p>Shua is the name of two biblical individuals. (1.) A Canaanite of Adullam whose daughter Judah married, making her the mother of Er, Onan, and Shelah (Genesis 38:2, 12). She is not named individually; Judah married <em>the daughter of a certain Canaanite whose name was Shua</em>. (2.) A daughter of Heber of the tribe of Asher (1 Chronicles 7:32), one of the few women listed in the Asherite genealogy. The name means <em>prosperity</em> or <em>a cry for help</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "crying; saving",
        "source_ids": {"easton": "shua"},
        "key_refs": ["Genesis 38:2", "1 Chronicles 7:32"]
    },
    "shuah": {
        "id": "shuah",
        "term": "Shuah",
        "category": "people",
        "intro": "<p>Shuah was a son of Abraham by Keturah, the wife Abraham took after Sarah's death (Genesis 25:2; 1 Chronicles 1:32). His descendants, the Shuhites, settled in northern Arabia. The most notable connection is to Bildad the Shuhite, one of Job's three friends (Job 2:11), whose tribal identification suggests descent from Shuah's line. Abraham gave gifts to the sons of his concubines and sent them eastward while Isaac remained as heir, situating the Shuhite territory in the Arabian desert regions northeast of Canaan. The Shuhites appear in inscriptions as a people of the middle Euphrates region.</p>",
        "sections": [],
        "hitchcock_meaning": "ditch; swimming; humiliation",
        "source_ids": {"easton": "shuah", "smith": "shuah"},
        "key_refs": ["Genesis 25:2", "Job 2:11"]
    },
    "shual-the-land-of": {
        "id": "shual-the-land-of",
        "term": "Shual, The land of",
        "category": "places",
        "intro": "<p>The land of Shual was the direction toward which one of the three raiding companies of Philistines turned during their occupation of the central hill country in the days of Saul (1 Samuel 13:17). When the Philistines garrisoned at Michmash sent out plundering raids, one party went toward the land of Shual, which lay to the north. The territory is likely in the vicinity of Ophrah in Benjamin, though the exact location is uncertain. The name <em>shual</em> means <em>fox</em> or <em>jackal</em>. Some scholars connect this region with Hazar-shual (fox village), a settlement on the southern edge of Judah, but the context suggests a northern Benjamin location.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shual-the-land-of", "smith": "shual-the-land-of"},
        "key_refs": ["1 Samuel 13:17"]
    },
    "shuhite": {
        "id": "shuhite",
        "term": "Shuhite",
        "category": "names",
        "intro": "<p>Shuhite is the gentile designation applied to Bildad, one of Job's three friends (Job 2:11; 8:1; 18:1; 25:1; 42:9). The term identifies him as a descendant of Shuah, son of Abraham by Keturah (Genesis 25:2), whose tribal territory lay in the region of northern Arabia. The Shuhites are attested in Assyrian and Babylonian sources as a people of the middle Euphrates, and their association with the wisdom tradition represented by Job's friends is consistent with the ancient Near Eastern setting of the book of Job. Bildad's speeches are marked by appeal to received tradition and the wisdom of former generations (Job 8:8–10), suggesting a culture that valued accumulated ancestral knowledge.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shuhite", "smith": "shuhite", "isbe": "shuhite"},
        "key_refs": ["Job 2:11", "Job 8:1", "Genesis 25:2"]
    },
    "shulamite": {
        "id": "shulamite",
        "term": "Shulamite",
        "category": "names",
        "intro": "<p>The Shulamite is the designation given to the beloved woman in the Song of Solomon 6:13, where the friends call to her: <em>Return, return, O Shulamite; return, return, that we may gaze at you.</em> The word is the feminine form of Sholomo (Solomon), leading some interpreters to understand it simply as <em>Solomon's girl</em> or the feminine counterpart to the king. Others connect it with the town of Shunem in Issachar, giving it the meaning <em>Shunammite</em> — and thus identifying the Shulamite with Abishag the Shunammite of 1 Kings 1–2. A third interpretation reads the term as meaning <em>the peaceful one</em> or <em>the perfect one</em>, derived from the root <em>shalam</em>. The Shulamite's voice dominates the Song as the female beloved who describes her dark complexion (Song 1:5), her vineyard (1:6), and her passionate longing for her lover.</p>",
        "sections": [],
        "hitchcock_meaning": "peaceable; perfect; that recompenses",
        "source_ids": {"easton": "shulamite"},
        "key_refs": ["Song of Solomon 6:13", "Song of Solomon 1:5"]
    },
    "shunammite": {
        "id": "shunammite",
        "term": "Shunammite",
        "category": "names",
        "intro": "<p>Shunammite designates a person from Shunem, a town in the tribe of Issachar. Two Shunammite women are prominent in Scripture. (1.) Abishag the Shunammite was brought to care for the aged David in his last days (1 Kings 1:3, 15); after David's death, Adonijah's request to marry her was treated by Solomon as a bid for the throne and led to Adonijah's execution (1 Kings 2:17–25). (2.) The unnamed great woman of Shunem (2 Kings 4:8–37) who provided lodging and a room for Elisha, whose son Elisha raised from the dead. This same woman later fled to Philistia during a seven-year famine and returned to find her property taken; Elisha's servant Gehazi was telling the king of her son's resurrection when she arrived, and the king restored everything to her (2 Kings 8:1–6).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shunammite", "isbe": "shunammite"},
        "key_refs": ["1 Kings 1:3", "2 Kings 4:8", "2 Kings 4:35"]
    },
    "shunem": {
        "id": "shunem",
        "term": "Shunem",
        "category": "places",
        "intro": "<p>Shunem (meaning <em>their rest</em> or <em>two resting-places</em>) was a town in the tribe of Issachar, situated on the southwestern slope of the hill of Moreh in the Jezreel Valley, north of Jezreel and south of Mount Gilboa. It appears in Joshua 19:18 in the list of Issachar's towns. The Philistines encamped at Shunem before the battle of Jezreel in which Saul was defeated and killed at Mount Gilboa (1 Samuel 28:4).</p><p>Shunem is better known as the home of the <em>great woman</em> who showed hospitality to the prophet Elisha by building him a room on her roof, and whose son Elisha raised from the dead (2 Kings 4:8–37). It was also the hometown of Abishag, the young woman brought to comfort the dying David (1 Kings 1:3). The site is identified with modern Solem at the foot of Mount Moreh.</p>",
        "sections": [],
        "hitchcock_meaning": "their change; their sleep",
        "source_ids": {"easton": "shunem", "smith": "shunem", "isbe": "shunem"},
        "key_refs": ["Joshua 19:18", "1 Samuel 28:4", "2 Kings 4:8", "1 Kings 1:3"]
    },
    "shur": {
        "id": "shur",
        "term": "Shur",
        "category": "places",
        "intro": "<p>Shur (meaning <em>wall</em> or <em>enclosure</em>) was a region of desert and semi-desert on the northeastern border of Egypt, where the wilderness of Sinai meets the approaches to Canaan. It gave its name to the Wilderness of Shur, which the Israelites entered immediately after crossing the Red Sea (Exodus 15:22), traveling three days without water before reaching Marah. Hagar fled toward Shur when she ran from Sarah, and the angel of the LORD found her by a spring on the road to Shur (Genesis 16:7).</p><p>Abraham sojourned between Kadesh and Shur (Genesis 20:1). The Ishmaelites dwelt from Havilah to Shur, east of Egypt (Genesis 25:18). Saul smote the Amalekites from Havilah to Shur (1 Samuel 15:7), and David raided the same region (1 Samuel 27:8). The term likely refers to the Egyptian frontier fortification system (Egyptian <em>tjaru</em>) running along the eastern edge of the Nile Delta — a line of walls and watchtowers meant to control access into Egypt from Sinai.</p>",
        "sections": [],
        "hitchcock_meaning": "wall; ox; that beholds",
        "source_ids": {"easton": "shur", "smith": "shur", "isbe": "shur"},
        "key_refs": ["Genesis 16:7", "Exodus 15:22", "1 Samuel 15:7"]
    },
    "shushan": {
        "id": "shushan",
        "term": "Shushan",
        "category": "places",
        "intro": "<p>Shushan (Greek <em>Susa</em>, Hebrew <em>Shushan</em>, meaning <em>lily</em>) was the ancient capital of Elam and one of the principal royal residences of the Persian Empire. Located in the uplands of Susiana on the Shaur River, about 150 miles north of the head of the Persian Gulf, it served as the winter capital of the Persian kings while Persepolis served the summer. The city is identified with modern Shush in southwestern Iran.</p><p>Shushan is central to three biblical books. The book of Esther is set entirely at the palace of Shushan, where Xerxes (Ahasuerus) held his great feast and later elevated Esther to queenship. Daniel received his vision of the ram and the goat while standing by the Ulai Canal at Shushan (Daniel 8:2). Nehemiah served as cupbearer to the Persian king in the palace at Shushan when he received the news of Jerusalem's ruined walls that moved him to prayer and action (Nehemiah 1:1; 2:1). Archaeological excavations have confirmed the city's extensive palace complex.</p>",
        "sections": [],
        "hitchcock_meaning": "lily; rose; joy",
        "source_ids": {"easton": "shushan", "isbe": "shushan"},
        "key_refs": ["Esther 1:2", "Daniel 8:2", "Nehemiah 1:1"]
    },
    "shushan-eduth": {
        "id": "shushan-eduth",
        "term": "Shushan-Eduth",
        "category": "concepts",
        "intro": "<p>Shushan-Eduth appears in the superscription of Psalm 60 as a musical designation, literally meaning <em>lily of the testimony</em> or <em>lily of the witness</em>. It is closely related to Shoshannim-Eduth in Psalm 80. The term likely indicates either a specific melody or tune associated with covenant testimony (<em>eduth</em>), or a type of instrument used in liturgical performance. Psalm 60 is a national lament following military reverses under David, calling on God to restore Israel and give victory over Edom and the surrounding nations. The designation suggests the psalm was performed with a particular musical tradition connected to Israel's covenant witness before God.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shushan-eduth", "isbe": "shushan-eduth"},
        "key_refs": ["Psalm 60:1"]
    },
    "sibbecai": {
        "id": "sibbecai",
        "term": "Sibbecai",
        "category": "people",
        "intro": "<p>Sibbecai the Hushathite was one of David's thirty mighty warriors (2 Samuel 23:27; 1 Chronicles 11:29) and one of the twelve monthly commanders who oversaw the military rotation of Israel's army (1 Chronicles 27:11). He is particularly remembered for slaying Saph (also called Sippai), one of the descendants of the Rapha — the Philistine giant-warriors — at the battle of Gezer (2 Samuel 21:18; 1 Chronicles 20:4). This battle was one of several in which David's heroes dealt with the remnant of the Philistine giant clans. As a Hushathite, Sibbecai was from Hushah in Judah (1 Chronicles 4:4).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sibbecai", "smith": "sibbecai"},
        "key_refs": ["2 Samuel 21:18", "2 Samuel 23:27", "1 Chronicles 27:11"]
    },
    "sibmah": {
        "id": "sibmah",
        "term": "Sibmah",
        "category": "places",
        "intro": "<p>Sibmah (also spelled Shibmah or Sebam) was a town on the Moabite plateau east of the Jordan, in the territory originally taken from Sihon king of the Amorites. It was allotted to the tribe of Reuben (Numbers 32:38; Joshua 13:19), who rebuilt it. In the prophetic laments over Moab in Isaiah 16:8–9 and Jeremiah 48:32, Sibmah is mourned for its celebrated vineyards: <em>the vine of Sibmah</em> was proverbially renowned, and its tendrils were said to reach to Jazer and trail down to the sea. The wine culture of the Moabite plateau made this region of the Transjordan prosperous, and its destruction by invading armies is lamented with genuine grief in both prophets. The site is possibly Qurn el-Kibsh near Heshbon.</p>",
        "sections": [],
        "hitchcock_meaning": "conversion; captivity",
        "source_ids": {"easton": "sibmah", "smith": "sibmah", "isbe": "sibmah"},
        "key_refs": ["Numbers 32:38", "Isaiah 16:8", "Jeremiah 48:32"]
    },
    "sichem": {
        "id": "sichem",
        "term": "Sichem",
        "category": "places",
        "intro": "<p>Sichem is a variant form of Shechem, the important city in the central highlands of Canaan between Mount Ebal and Mount Gerizim. The name Sichem occurs in Genesis 12:6 in the account of Abram's first arrival in Canaan: <em>Abram passed through the land to the place of Sichem, as far as the terebinth of Moreh.</em> It is also used in Genesis 33:18 and Acts 7:16. Shechem was the site of the covenant renewal ceremony under Joshua (Joshua 24), the short-lived kingship of Abimelech (Judges 9), and later the capital of the northern kingdom under Jeroboam I (1 Kings 12:25). See also the main article on Shechem.</p>",
        "sections": [],
        "hitchcock_meaning": "portion; shoulder",
        "source_ids": {"easton": "sichem", "smith": "sichem", "isbe": "sichem"},
        "key_refs": ["Genesis 12:6", "Acts 7:16", "Joshua 24:1"]
    },
    "sickle": {
        "id": "sickle",
        "term": "Sickle",
        "category": "concepts",
        "intro": "<p>The sickle was the primary harvesting tool of the ancient Near East, used to cut grain stalks at the base. Early sickles were made of flint blades set in a wooden or bone handle; by the Iron Age they were made of iron. Deuteronomy 16:9 stipulates: <em>You shall begin to count the seven weeks from the time you first put the sickle to the standing grain</em> — linking the harvest tool directly to the liturgical calendar. Deuteronomy 23:25 permitted gleaning grain by hand from a neighbor's field but forbade using a sickle.</p><p>The sickle became a powerful apocalyptic image. Joel 3:13 calls for the sickle to be put in, for the harvest is ripe, as a summons to divine judgment on the nations. Revelation 14:14–19 elaborates this into a vision of the Son of Man and angels wielding sharp sickles to harvest the earth at the final judgment — both a grain harvest and a vintage of the vine depicting the gathering of souls and the wrath of God.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sickle", "isbe": "sickle"},
        "key_refs": ["Deuteronomy 16:9", "Joel 3:13", "Revelation 14:14"]
    },
    "siddim-vale-of": {
        "id": "siddim-vale-of",
        "term": "Siddim, Vale of",
        "category": "places",
        "intro": "<p>The Vale of Siddim was the battlefield where the four kings led by Chedorlaomer of Elam defeated the five Canaanite kings of the cities of the plain — including the kings of Sodom and Gomorrah (Genesis 14:3, 8–10). The valley is said to be <em>the Salt Sea</em> in the text's own explanatory gloss (<em>that is, the Salt Sea</em>), suggesting that by the time of writing the valley had been submerged under the waters of the Dead Sea. The valley contained bitumen pits into which the fleeing kings of Sodom and Gomorrah fell. Most scholars place it at the southern end of the Dead Sea, where the shallow waters cover what was once habitable lowland terrain. The catastrophe of Sodom and Gomorrah, which followed shortly after, fits with the tradition of a once-fertile region destroyed and submerged.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "siddim-vale-of", "isbe": "siddim-vale-of"},
        "key_refs": ["Genesis 14:3", "Genesis 14:8", "Genesis 14:10"]
    },
    "sidon": {
        "id": "sidon",
        "term": "Sidon",
        "category": "places",
        "intro": "<p>Sidon (also spelled Zidon; Hebrew meaning <em>fishing</em> or <em>fishery</em>) was the oldest and originally the most important of the Phoenician city-states, situated on the Mediterranean coast north of Tyre in modern Lebanon. Genesis 10:15 lists Sidon as the firstborn son of Canaan, reflecting the city's primacy among Canaanite coastal settlements. The territory of Sidon defined the northern boundary of Canaan (Genesis 10:19). Though allotted to the tribe of Asher (Joshua 19:28), Sidon was never conquered by Israel.</p><p>Sidon was renowned for its craftsmen, sailors, and merchants. Jezebel, whose marriage to Ahab brought Baal worship into Israel, was the daughter of Ethbaal king of the Sidonians (1 Kings 16:31). Jesus visited the region of Tyre and Sidon and healed the Syrophoenician woman's daughter there (Matthew 15:21; Mark 7:24). Paul stopped at Sidon on his voyage to Rome, where Julius the centurion allowed him to visit friends (Acts 27:3). Isaiah, Jeremiah, Ezekiel, and Joel all include Sidon in their oracles against the nations.</p>",
        "sections": [],
        "hitchcock_meaning": "hunting; fishing; venison",
        "source_ids": {"easton": "sidon", "smith": "sidon"},
        "key_refs": ["Genesis 10:15", "1 Kings 16:31", "Matthew 15:21", "Acts 27:3"]
    },
    "signet": {
        "id": "signet",
        "term": "Signet",
        "category": "concepts",
        "intro": "<p>A signet (Hebrew <em>hotam</em>, Greek <em>sphragis</em>) was a seal — typically a ring or cylinder — used to authenticate documents and attest authority by pressing it into clay or wax. Daniel 6:17 records that the king sealed the lion's den with his signet ring and with the signets of his lords so that nothing might be changed concerning Daniel. Esther 3:10 and 8:8–10 describe Ahasuerus giving his signet ring to Haman for the decree against the Jews, and later to Mordecai and Esther to write the counter-decree.</p><p>In prophetic imagery the signet carried the highest value. God said to Zerubbabel: <em>I will make you like a signet ring, for I have chosen you</em> (Haggai 2:23) — reversing the curse on Coniah/Jehoiachin who was told that even if he were God's signet ring, he would be pulled off and given to Nebuchadnezzar (Jeremiah 22:24). The signet was an image of intimacy, authorization, and the mark of ownership.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "signet", "isbe": "signet"},
        "key_refs": ["Daniel 6:17", "Haggai 2:23", "Jeremiah 22:24", "Esther 8:8"]
    },
    "sihon": {
        "id": "sihon",
        "term": "Sihon",
        "category": "people",
        "intro": "<p>Sihon was the Amorite king who ruled the Transjordanian territory from the Arnon River in the south to the Jabbok in the north, with his capital at Heshbon. When Israel, approaching Canaan from the east, requested peaceful passage through his territory, Sihon refused and went out to battle against them at Jahaz. Israel defeated him decisively, took possession of his entire territory, and settled in his cities — including Heshbon (Numbers 21:21–31; Deuteronomy 2:24–37).</p><p>This victory over Sihon (paired always with the defeat of Og of Bashan) became one of the paradigmatic acts of divine deliverance in Israel's memory. It is recited as a sign of God's power in Psalms 135:11 and 136:19–20, in Nehemiah's prayer (Nehemiah 9:22), and in Jephthah's argument with the Ammonites (Judges 11:19–22). The song of Numbers 21:27–30 (<em>Come to Heshbon!</em>) is quoted as an ancient victory taunt over Sihon's former city. His territory became the allotment of Reuben and Gad.</p>",
        "sections": [],
        "hitchcock_meaning": "rooting out; conclusion",
        "source_ids": {"easton": "sihon", "smith": "sihon", "isbe": "sihon"},
        "key_refs": ["Numbers 21:23", "Deuteronomy 2:30", "Psalm 135:11", "Nehemiah 9:22"]
    },
    "sihor": {
        "id": "sihor",
        "term": "Sihor",
        "category": "places",
        "intro": "<p>Sihor (also spelled Shihor) was a waterway on the border of Egypt, used to designate the southwestern extent of Canaan or the Nile itself. In Joshua 13:3 it defines the southern limit of unconquered Canaanite territory: <em>from Sihor, which is east of Egypt, as far as the border of Ekron in the north.</em> Isaiah 23:3 describes Sihor's harvest as Tyre's revenue, linking it to the Egyptian grain trade. Jeremiah 2:18 asks Israel why they go to Egypt to drink from the waters of Sihor. The name is generally understood as a variant of <em>Shichor</em> meaning <em>black</em> or <em>turbid</em>, often identified with the easternmost branch of the Nile or with the Wadi el-Arish, the traditional boundary between Egypt and Canaan.</p>",
        "sections": [],
        "hitchcock_meaning": "black; trouble (the river Nile)",
        "source_ids": {"easton": "sihor", "smith": "sihor", "isbe": "sihor"},
        "key_refs": ["Joshua 13:3", "Isaiah 23:3", "Jeremiah 2:18"]
    },
    "silas": {
        "id": "silas",
        "term": "Silas",
        "category": "people",
        "intro": "<p>Silas (also called Silvanus in the epistles — likely the more formal Latin name for the same person) was a prominent leader in the Jerusalem church who became Paul's companion on his second missionary journey. He and Judas Barsabas were chosen by the Jerusalem council to carry the letter resolving the Gentile circumcision controversy to Antioch (Acts 15:22–33). When Paul and Barnabas separated over John Mark, Paul chose Silas to accompany him through Syria, Cilicia, and into Macedonia (Acts 15:40–41).</p><p>Silas was with Paul at Philippi, where both were beaten and imprisoned after Paul cast out a spirit from a slave girl; their midnight singing of hymns and the subsequent earthquake that freed them is one of the memorable episodes of Acts 16. He continued with Paul in Thessalonica and Berea. As a Roman citizen (Acts 16:37), Silas shared Paul's legal standing. He is named as co-author of both Thessalonian letters (1 Thessalonians 1:1; 2 Thessalonians 1:1) and appears to have served as Peter's secretary for 1 Peter (1 Peter 5:12).</p>",
        "sections": [],
        "hitchcock_meaning": "three, or the third",
        "source_ids": {"easton": "silas", "smith": "silas", "isbe": "silas"},
        "key_refs": ["Acts 15:22", "Acts 16:25", "1 Thessalonians 1:1", "1 Peter 5:12"]
    },
    "silk": {
        "id": "silk",
        "term": "Silk",
        "category": "concepts",
        "intro": "<p>Silk appears twice in the English Bible, and both occurrences are textually debated. Proverbs 31:22 says the virtuous woman makes herself coverings of <em>silk and purple</em> (Hebrew <em>shesh</em>), though many modern translations render <em>shesh</em> as <em>fine linen</em> or <em>byssus</em> rather than silk, since true silk from China was rare and expensive in the ancient Near East and its availability in Solomonic Israel is uncertain. Ezekiel 16:10, 13 uses <em>meshi</em>, which is more commonly taken to mean silk or fine cloth; God dresses Jerusalem in fine linen, silk, and embroidered cloth as a metaphor for covenantal blessing. Revelation 18:12 lists silk (<em>sirikos</em>) among the luxury goods of fallen Babylon, confirming that silk was known in the Greco-Roman world as a prized eastern import.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "silk", "smith": "silk"},
        "key_refs": ["Proverbs 31:22", "Ezekiel 16:10", "Revelation 18:12"]
    },
    "silla": {
        "id": "silla",
        "term": "Silla",
        "category": "places",
        "intro": "<p>Silla is mentioned only once in Scripture, in the account of the assassination of King Joash of Judah: <em>his servants arose and made a conspiracy and struck down Joash at the house of Millo, on the way that goes down to Silla</em> (2 Kings 12:20). The location of Silla is unknown, and no other biblical or extra-biblical text illuminates it. It appears to be a site or descent near the Millo in Jerusalem, possibly a slope or road leading south from the city. The obscurity of the reference suggests it was a specific local landmark recognizable to the original audience but not otherwise significant in the biblical narrative.</p>",
        "sections": [],
        "hitchcock_meaning": "exalting",
        "source_ids": {"easton": "silla", "smith": "silla", "isbe": "silla"},
        "key_refs": ["2 Kings 12:20"]
    },
    "siloah-the-pool-of": {
        "id": "siloah-the-pool-of",
        "term": "Siloah, The pool of",
        "category": "places",
        "intro": "<p>The pool of Siloah (Siloam) is mentioned in Nehemiah 3:15 as a landmark near the king's garden beside the Fountain Gate, which Shallun son of Col-hozeh repaired during the restoration of Jerusalem's walls. The name is a variant of Siloam (Hebrew <em>Shiloah</em>, meaning <em>sent</em>), the pool fed by the waters channeled through Hezekiah's tunnel from the Gihon Spring. Isaiah 8:6 refers to the <em>waters of Shiloah that flow gently</em> as a figure for the quiet provision of God which Israel despised. See also the related article on Siloam, Pool of, which is the New Testament identification of this same water source.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "siloah-the-pool-of", "smith": "siloah-the-pool-of"},
        "key_refs": ["Nehemiah 3:15", "Isaiah 8:6"]
    },
    "siloam-pool-of": {
        "id": "siloam-pool-of",
        "term": "Siloam, Pool of",
        "category": "places",
        "intro": "<p>The Pool of Siloam (Hebrew <em>Shiloah</em>, Greek <em>Siloam</em>, meaning <em>sent</em>) was the reservoir at the southern end of Hezekiah's tunnel in Jerusalem, fed by the Gihon Spring through the 533-meter rock-cut conduit that Hezekiah constructed to secure Jerusalem's water supply before the Assyrian siege (2 Kings 20:20; 2 Chronicles 32:30; Isaiah 22:9). The Siloam Inscription discovered in 1880 commemorates the completion of this tunnel by workmen cutting from both ends.</p><p>The pool's greatest New Testament significance is as the site of the healing of the man born blind (John 9:1–11). Jesus mixed mud with saliva, applied it to the man's eyes, and commanded him: <em>Go, wash in the pool of Siloam.</em> He went, washed, and received his sight — prompting an extended controversy with the Pharisees over whether the healing was lawful on the Sabbath. Archaeological excavations since 2004 have uncovered a large first-century stepped pool at the southern end of the City of David, widely identified as the Pool of Siloam.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "siloam-pool-of"},
        "key_refs": ["John 9:7", "2 Kings 20:20", "Isaiah 8:6"]
    },
    "siloam-tower-of": {
        "id": "siloam-tower-of",
        "term": "Siloam, Tower of",
        "category": "places",
        "intro": "<p>The Tower of Siloam is mentioned only in Luke 13:4, where Jesus refers to <em>those eighteen on whom the tower in Siloam fell and killed them</em> as an example that fatal accidents are not evidence of exceptional guilt in the victims. The collapse was apparently a well-known recent event at the time Jesus spoke, though it is not mentioned elsewhere in ancient sources. The tower stood in the neighborhood of the Pool of Siloam in the lower city of Jerusalem, likely part of the wall or fortification system in that area. Jesus used both the Galilean victims of Pilate's violence (Luke 13:1–2) and the tower's collapse as illustrations that all people face mortality and need repentance, warning his audience not to interpret disasters as divine judgment on specific individuals.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "siloam-tower-of"},
        "key_refs": ["Luke 13:4"]
    },
    "silver": {
        "id": "silver",
        "term": "Silver",
        "category": "concepts",
        "intro": "<p>Silver was the primary medium of exchange in the ancient Near East before coinage, measured by weight rather than denomination. It first appears as a commodity in Genesis 13:2 (Abraham was rich in silver), and the purchase of Machpelah for 400 shekels of silver (Genesis 23:15–16) illustrates the weighed-silver transaction standard. Joseph's brothers received 20 pieces of silver when they sold him to the Ishmaelites (Genesis 37:28), and Judas betrayed Jesus for 30 pieces — the Mosaic price of a slave (Exodus 21:32; Zechariah 11:12–13; Matthew 26:15).</p><p>Silver was used extensively in the Tabernacle: the 100 sockets for the framework were each cast from a talent of silver contributed by the census ransom (Exodus 38:25–27). The refining of silver by fire — removing dross to purify the metal — became a standard metaphor for divine discipline: <em>I have refined you, but not as silver</em> (Isaiah 48:10); Malachi 3:3 pictures the Messiah as a refiner of silver purifying the sons of Levi. Zechariah 13:9 uses the same image for the remnant refined through tribulation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "silver", "smith": "silver", "isbe": "silver"},
        "key_refs": ["Genesis 23:16", "Matthew 26:15", "Malachi 3:3", "Zechariah 13:9"]
    },
    "silverling": {
        "id": "silverling",
        "term": "Silverling",
        "category": "concepts",
        "intro": "<p>Silverling is an archaic English term appearing in the KJV of Isaiah 7:23 to translate the Hebrew <em>keseph</em> (silver, money): <em>every place where there were a thousand vines worth a thousand silverlings</em>. The word is simply a diminutive or informal designation for a silver coin or piece of silver — it does not correspond to a specific denomination but captures the sense of individual silver pieces used as units of value. Modern translations render the same verse as <em>a thousand silver coins</em> or <em>a thousand pieces of silver</em>. The context describes the desolation coming upon the prosperous vineyards of Judah when the land is overrun and the carefully cultivated terraces revert to briers and thorns.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "silverling", "isbe": "silverling"},
        "key_refs": ["Isaiah 7:23"]
    },
    "simeon": {
        "id": "simeon",
        "term": "Simeon",
        "category": "people",
        "intro": "<p>Simeon (meaning <em>hearing</em> or <em>one who hears</em>) was the second son of Jacob and Leah (Genesis 29:33). Leah named him Simeon saying, <em>Because the LORD has heard that I am hated, he has given me this son also.</em> Simeon and his brother Levi avenged the rape of their sister Dinah by massacring the men of Shechem after the Shechemites agreed to circumcision (Genesis 34:25–29) — an act Jacob condemned as bringing trouble on his house. Jacob's deathbed blessing forecasted that both Simeon and Levi would be scattered in Israel (Genesis 49:5–7), a prophecy fulfilled differently for each: Levi received priestly duties spread across all Israel, while Simeon's territory was absorbed within Judah's allotment (Joshua 19:1–9).</p><p>Simeon was held hostage in Egypt by Joseph until the brothers returned with Benjamin (Genesis 42:24, 36). In the New Testament the name is borne by Simeon in the temple who recognized the infant Jesus as the Lord's Christ and spoke the Nunc Dimittis (Luke 2:25–35), and by Simeon called Niger, a leader in the Antioch church (Acts 13:1).</p>",
        "sections": [],
        "hitchcock_meaning": "that hears or obeys; that is heard",
        "source_ids": {"easton": "simeon", "smith": "simeon"},
        "key_refs": ["Genesis 29:33", "Genesis 34:25", "Genesis 49:5", "Luke 2:25"]
    },
    "simeon-the-tribe-of": {
        "id": "simeon-the-tribe-of",
        "term": "Simeon, The tribe of",
        "category": "people",
        "intro": "<p>The tribe of Simeon descended from Simeon the second son of Jacob and Leah. In the wilderness census of Numbers 1 it numbered 59,300 men of military age (Numbers 1:23), but by the second census in Numbers 26 this had fallen to 22,200 (Numbers 26:14) — a dramatic decline possibly connected with the plague following Baal Peor (Numbers 25), since the executed Zimri was a Simeonite prince (Numbers 25:14).</p><p>Jacob's prophecy that Simeon would be scattered in Israel (Genesis 49:7) was fulfilled through the tribe's territorial allotment: Simeon received cities within the inheritance of Judah, since Judah's portion was too large (Joshua 19:1, 9). This arrangement gradually resulted in Simeon being absorbed into Judah; by the time of the exile, the tribe of Simeon had largely disappeared as a distinct entity. Chronicles records a late Simeonite expansion in the days of Hezekiah, when Simeonites conquered Gedor and the territory of the Amalekites (1 Chronicles 4:24–43).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "simeon-the-tribe-of"},
        "key_refs": ["Genesis 49:5", "Numbers 1:23", "Joshua 19:1"]
    },
    "simon": {
        "id": "simon",
        "term": "Simon",
        "category": "people",
        "intro": "<p>Simon (abbreviated form of Simeon) is one of the most common names in the New Testament, borne by at least nine individuals. (1.) Simon Peter, the fisherman from Bethsaida who became the leading apostle; Jesus gave him the Aramaic name Cephas (Peter, <em>rock</em>) — Matthew 16:17–18. (2.) Simon the Canaanite (Matthew 10:4; Mark 3:18), also called Simon the Zealot (Luke 6:15; Acts 1:13), one of the twelve. The term <em>Canaanite</em> here is not ethnic but derives from the Aramaic <em>qanean</em>, equivalent to the Greek <em>zelotes</em>.</p><p>(3.) Simon the brother of Jesus (Matthew 13:55; Mark 6:3). (4.) Simon of Cyrene, compelled to carry Jesus's cross (Matthew 27:32). (5.) Simon the leper, in whose house at Bethany the woman anointed Jesus (Matthew 26:6; Mark 14:3). (6.) Simon the Pharisee, in whose house a sinful woman anointed Jesus's feet (Luke 7:40). (7.) Simon Iscariot, father of Judas (John 6:71). (8.) Simon the tanner at Joppa, in whose house Peter received his vision about clean and unclean things (Acts 10:6). (9.) Simon Magus, the sorcerer of Samaria (Acts 8:9–24).</p>",
        "sections": [],
        "hitchcock_meaning": "that hears; that obeys",
        "source_ids": {"easton": "simon", "smith": "simon"},
        "key_refs": ["Matthew 16:18", "Acts 8:9", "Matthew 27:32", "Luke 7:40"]
    },
    "simri": {
        "id": "simri",
        "term": "Simri",
        "category": "people",
        "intro": "<p>Simri (also spelled Shimri) is the name of several biblical individuals. (1.) A son of Hosah of the Merarite Levites, appointed as a gatekeeper in David's organization of the temple personnel; though not the firstborn, his father made him chief of his family (1 Chronicles 26:10). (2.) The father of Jediael, one of David's mighty warriors (1 Chronicles 11:45). (3.) A Simeonite ancestor of Ziza who joined in the expansion of Simeon's territory in Hezekiah's time (1 Chronicles 4:37). (4.) A Levite of the sons of Elizaphan who helped in Hezekiah's purification of the temple (2 Chronicles 29:13). The name means <em>watchful</em>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "simri", "smith": "simri", "isbe": "simri"},
        "key_refs": ["1 Chronicles 26:10", "2 Chronicles 29:13"]
    },
    "sin": {
        "id": "sin",
        "term": "Sin",
        "category": "concepts",
        "intro": "<p>Sin is defined in Scripture as <em>any want of conformity unto or transgression of the law of God</em> (Westminster Shorter Catechism, drawing on 1 John 3:4 and Romans 4:15). The concept encompasses both the inward state — the disposition of the heart against God — and outward conduct, whether by active transgression or by failure to do what is required. The Hebrew vocabulary of sin is rich: <em>hata</em> (to miss the mark), <em>pesha</em> (rebellion, trespass), <em>awon</em> (iniquity, perversity), and <em>resha</em> (wickedness) each capture different aspects of the same reality.</p><p>Biblical theology traces the origin of human sin to the fall of Adam (Genesis 3; Romans 5:12–21), through which sin entered the world and death through sin, spreading to all humanity. The Law revealed sin's full extent (Romans 3:20; 7:7–13) while the sacrificial system provided atonement within the covenant. Paul's analysis in Romans 1–3 establishes universal human guilt before the righteousness of God, setting the stage for the gospel of justification by faith. Christ bore sin in his body on the cross (1 Peter 2:24; 2 Corinthians 5:21; Isaiah 53:6) — the sinless one made sin so that sinners might be made the righteousness of God.</p>",
        "sections": [],
        "hitchcock_meaning": "bush",
        "source_ids": {"easton": "sin", "smith": "sin"},
        "key_refs": ["1 John 3:4", "Romans 5:12", "Romans 3:23", "1 Peter 2:24"]
    },
    "sin-wilderness-of": {
        "id": "sin-wilderness-of",
        "term": "Sin, Wilderness of",
        "category": "places",
        "intro": "<p>The Wilderness of Sin was a region in the Sinai peninsula through which the Israelites passed after leaving the Red Sea shore and before reaching Rephidim and Mount Sinai (Exodus 16:1; 17:1; Numbers 33:11–12). The name has no connection to moral sin but is a place name, possibly derived from <em>Siyn</em>, an ancient name for the Sinai peninsula itself or from the moon-god Sin. The arrival in this wilderness — <em>in the fifteenth day of the second month after their departure from Egypt</em> — triggered the first complaint about food and the provision of quail and manna (Exodus 16). The manna continued every day except the Sabbath for the entire forty years in the wilderness (Exodus 16:35). The Wilderness of Sin is generally located on the west coast of the Sinai peninsula, in the vicinity of the plain of El-Markha.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sin-wilderness-of", "smith": "sin-wilderness-of", "isbe": "sin-wilderness-of"},
        "key_refs": ["Exodus 16:1", "Exodus 16:14", "Numbers 33:11"]
    },
    "sin-offering": {
        "id": "sin-offering",
        "term": "Sin-offering",
        "category": "concepts",
        "intro": "<p>The sin-offering (<em>hatta't</em>) was one of the five major sacrificial types of the Mosaic system, prescribed in Leviticus 4–6:13 and 9. It was offered specifically for unintentional sins — acts of omission or commission done in ignorance or weakness, as opposed to the willful high-handed sins for which the Law prescribed death rather than sacrifice. The animal required varied by the offerer's status: a young bull for the high priest or congregation, a male goat for a ruler, a female goat or lamb for a common person, and for the very poor, two turtledoves or pigeons, or even fine flour (Leviticus 5:7, 11).</p><p>The distinctive ritual was the application of blood to specific places: on the horns of the altar of incense and before the veil for the priest and congregation; on the horns of the altar of burnt offering for individuals. The fat was burned on the altar; the flesh was eaten by the priests in most cases, or burned outside the camp if blood was brought into the tent. Hebrews 13:11–12 draws the parallel explicitly: just as the bodies of the sin-offering animals were burned outside the camp, so Jesus suffered outside the gate to sanctify his people through his own blood.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sin-offering", "smith": "sin-offering", "isbe": "sin-offering"},
        "key_refs": ["Leviticus 4:3", "Leviticus 4:28", "Hebrews 13:11", "Leviticus 5:7"]
    },
    "sinai": {
        "id": "sinai",
        "term": "Sinai",
        "category": "places",
        "intro": "<p>Sinai (also called Horeb) is the mountain in the Sinai peninsula where the LORD appeared to Moses in the burning bush (Exodus 3), gave Israel the Ten Commandments and the Mosaic Law (Exodus 19–20; Deuteronomy 4–5), and made covenant with Israel as a nation. The Israelites arrived at Sinai three months after the Exodus (Exodus 19:1) and remained there approximately a year, during which the Tabernacle was constructed and the entire Levitical system established. The mountain was surrounded by phenomena of divine presence: thunderings, lightning, thick cloud, and the sound of a very loud trumpet (Exodus 19:16–19).</p><p>The precise identification of biblical Sinai among the mountains of the Sinai peninsula remains debated, with traditional location at Jebel Musa in the southern Sinai being the most commonly accepted, though some scholars have proposed sites in northwest Arabia. Elijah fled to Horeb after his confrontation with Jezebel (1 Kings 19:8). Paul interprets Sinai allegorically in Galatians 4:24–25 as the covenant of slavery contrasted with the Jerusalem above. Hebrews 12:18–24 contrasts the terrifying mountain that could not be touched with the heavenly Mount Zion to which believers have come in Christ.</p>",
        "sections": [],
        "hitchcock_meaning": "a bush; enmity",
        "source_ids": {"easton": "sinai", "isbe": "sinai"},
        "key_refs": ["Exodus 19:1", "Exodus 19:18", "Galatians 4:24", "Hebrews 12:18"]
    },
    "sinaiticus-codex": {
        "id": "sinaiticus-codex",
        "term": "Sinaiticus codex",
        "category": "concepts",
        "intro": "<p>Codex Sinaiticus (designated by the Hebrew letter Aleph or א) is one of the oldest and most complete manuscripts of the Christian Bible, dating to the fourth century AD. Written on vellum in Greek, it originally contained the entire Old Testament (Septuagint) and New Testament, along with the Epistle of Barnabas and the Shepherd of Hermas. It was discovered by the scholar Constantin von Tischendorf at Saint Catherine's Monastery on the Sinai peninsula in 1844–1859, a find of immense importance for New Testament textual criticism. Portions of the manuscript are now held at the British Library, the National Library of Russia, Leipzig University, and Saint Catherine's Monastery. Together with Codex Vaticanus (B), Sinaiticus is the primary witness to the Alexandrian text type and serves as a critical anchor for modern critical editions of the Greek New Testament.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sinaiticus-codex"},
        "key_refs": []
    },
    "sinim-the-land-of": {
        "id": "sinim-the-land-of",
        "term": "Sinim, The land of",
        "category": "places",
        "intro": "<p>The land of Sinim appears in Isaiah 49:12 in a prophecy of the worldwide regathering of scattered Israel: <em>these shall come from far away, and these from the north and from the west, and these from the land of Sinim.</em> The identification has been debated throughout history. The Dead Sea Scrolls (1QIsa-a) read <em>Syene</em> (modern Aswan in southern Egypt) rather than Sinim, and most modern translations follow this reading as <em>the land of Aswan</em> or <em>the region of Aswan.</em> Older commentators often identified Sinim with China, pointing to the ancient name <em>Qin</em>. The Syene reading makes better geographical sense as a designation for the remote south (complementing north and west), referring to the Egyptian Jewish community at Elephantine near Aswan.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sinim-the-land-of"},
        "key_refs": ["Isaiah 49:12"]
    },
    "sinite": {
        "id": "sinite",
        "term": "Sinite",
        "category": "names",
        "intro": "<p>The Sinites were one of the Canaanite peoples descended from Canaan son of Ham (Genesis 10:17; 1 Chronicles 1:15), listed among the eleven peoples of Canaan in the Table of Nations. Their precise territory is uncertain. Some scholars have proposed identification with the region around Sin (Pelusium) on the northeastern border of Egypt, with the northern coast of Lebanon near Sinn en-Nabra, or with a place in northern Phoenicia mentioned in Assyrian inscriptions. The Sinites appear only in the genealogical lists and play no named role in biblical narrative beyond representing one of the nations that would be displaced before Israel's conquest of Canaan.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sinite", "smith": "sinite"},
        "key_refs": ["Genesis 10:17", "1 Chronicles 1:15"]
    },
    "sion": {
        "id": "sion",
        "term": "Sion",
        "category": "places",
        "intro": "<p>Sion appears in the Old Testament as a name for Mount Hermon in Deuteronomy 4:48: <em>Mount Siyon (that is, Hermon)</em> — an alternate name for the great peak on the northern border of Israel, not to be confused with Zion (Jerusalem). The same form Sion appears in the Septuagint for both Hermon and Zion. In the New Testament (KJV and some versions), Sion transliterates the Greek <em>Sion</em> which renders the Hebrew <em>Zion</em> — thus Hebrews 12:22 (<em>you have come to Mount Sion</em>), Romans 9:33, 11:26, and Revelation 14:1 all refer to Zion as the heavenly or eschatological mountain of God. The spelling Sion in the KJV is simply a transliteration variant for Zion throughout the New Testament.</p>",
        "sections": [],
        "hitchcock_meaning": "noise; tumult",
        "source_ids": {"easton": "sion", "smith": "sion", "isbe": "sion"},
        "key_refs": ["Deuteronomy 4:48", "Hebrews 12:22", "Revelation 14:1"]
    },
    "siphmoth": {
        "id": "siphmoth",
        "term": "Siphmoth",
        "category": "places",
        "intro": "<p>Siphmoth was one of the towns in southern Judah (the Negeb) to which David sent portions of the spoil from his raid on the Amalekites who had plundered Ziklag (1 Samuel 30:28). David sent gifts to Siphmoth and to numerous other towns in the area where he and his men had roamed — towns whose elders were his friends and who had supported him during his time as a fugitive from Saul. This distribution of spoil was both a practical gesture of alliance maintenance and a demonstration of David's fidelity to his covenant network. The site of Siphmoth is unidentified.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "siphmoth", "smith": "siphmoth", "isbe": "siphmoth"},
        "key_refs": ["1 Samuel 30:28"]
    },
    "sirah": {
        "id": "sirah",
        "term": "Sirah",
        "category": "places",
        "intro": "<p>Sirah is the name of a well or cistern mentioned in 2 Samuel 3:26 in connection with the treacherous killing of Abner. After Abner had made peace with David and departed in safety, Joab (who bore a blood feud against Abner for killing his brother Asahel) secretly sent messengers after Abner and brought him back from the well of Sirah without David's knowledge. When Abner returned to Hebron, Joab took him aside at the gate and killed him — an act David publicly disavowed with lamentation and a formal mourning ceremony. The well of Sirah is usually identified with the modern spring Ain Sarah, about a mile north of Hebron.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sirah", "smith": "sirah"},
        "key_refs": ["2 Samuel 3:26"]
    },
    "sirion": {
        "id": "sirion",
        "term": "Sirion",
        "category": "places",
        "intro": "<p>Sirion was the Sidonian name for Mount Hermon (Deuteronomy 3:9), the great snow-capped peak at the northern edge of the promised land (approximately 9,230 feet / 2,814 meters). The Amorites called the same mountain Shenir (Deuteronomy 3:9; 1 Chronicles 5:23). Psalm 29:6 uses Sirion as a poetic name in a theophanic psalm: <em>He makes Lebanon skip like a calf, and Sirion like a young wild ox</em> — picturing the response of creation to the voice of the LORD in the thunderstorm. The variation in names (Hermon, Sion, Sirion, Shenir) reflects the different peoples who inhabited the region around this towering landmark visible across much of ancient Syria-Palestine.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sirion", "smith": "sirion", "isbe": "sirion"},
        "key_refs": ["Deuteronomy 3:9", "Psalm 29:6"]
    },
    "sisera": {
        "id": "sisera",
        "term": "Sisera",
        "category": "people",
        "intro": "<p>Sisera was the military commander of Jabin king of Canaan, who oppressed Israel for twenty years (Judges 4:1–3). His army of nine hundred iron chariots gave Hazor formidable military superiority over the Israelite hill-country tribes. When Deborah the prophetess directed Barak to lead ten thousand men against Sisera from Mount Tabor, the LORD threw the Canaanite army into panic at the Kishon River — probably through a sudden storm that flooded the plain and rendered the chariots useless (Judges 4:15; 5:20–21). Sisera abandoned his chariot and fled on foot.</p><p>He sought refuge in the tent of Jael wife of Heber the Kenite, whose clan was at peace with Hazor. Jael welcomed him, gave him milk, covered him, and when he had fallen asleep drove a tent peg through his temple — fulfilling Deborah's prophecy that the glory of the victory would go to a woman (Judges 4:9, 21). The Song of Deborah (Judges 5) commemorates the victory and ends with a poignant ironic portrait of Sisera's mother waiting in vain for her son to return with plunder.</p>",
        "sections": [],
        "hitchcock_meaning": "that sees a horse or a swallow",
        "source_ids": {"easton": "sisera", "smith": "sisera", "isbe": "sisera"},
        "key_refs": ["Judges 4:2", "Judges 4:21", "Judges 5:26", "Psalm 83:9"]
    },
    "sitnah": {
        "id": "sitnah",
        "term": "Sitnah",
        "category": "places",
        "intro": "<p>Sitnah (meaning <em>hatred</em> or <em>opposition</em>) was the second well dug by Isaac's servants after their expulsion from Gerar by the Philistines of that region. The herdsmen of Gerar quarreled over the first well (called Esek, meaning <em>dispute</em>) and also over Sitnah — so Isaac moved on and dug a third well, Rehoboth, over which there was no quarrel (Genesis 26:21). The sequence of the three wells — Dispute, Hatred, Wide Places — illustrates the narrative pattern of conflict and resolution characteristic of Isaac's sojourn. The wells of Isaac were important landmarks in the Negeb, and the tradition of their naming preserved early memories of territorial disputes between the patriarchs and the Philistines.</p>",
        "sections": [],
        "hitchcock_meaning": "hatred",
        "source_ids": {"easton": "sitnah", "smith": "sitnah", "isbe": "sitnah"},
        "key_refs": ["Genesis 26:21"]
    },
    "sitting": {
        "id": "sitting",
        "term": "Sitting",
        "category": "concepts",
        "intro": "<p>In biblical culture the posture of sitting carried specific social and symbolic meaning distinct from modern usage. Sitting was the posture of judges, kings, and teachers exercising authority: <em>you shall sit on twelve thrones judging the twelve tribes of Israel</em> (Matthew 19:28); Jesus sat down to teach in the synagogue (Luke 4:20) and on the mountain (Matthew 5:1). The sitting of God or of Christ at the right hand is the supreme image of royal authority: <em>The LORD says to my Lord: Sit at my right hand</em> (Psalm 110:1), quoted more often in the New Testament than any other Old Testament passage.</p><p>Sitting in sackcloth and ashes was a posture of mourning (Jonah 3:6). Eating at table involved reclining rather than sitting upright on chairs. The ISBE article on sitting notes the range of cross-legged, kneeling, and reclining postures encompassed by biblical sitting vocabulary, and the social significance of where one sat — proximity to the host indicated honor (Luke 14:7–11).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sitting", "isbe": "sitting"},
        "key_refs": ["Psalm 110:1", "Matthew 19:28", "Luke 4:20"]
    },
    "sivan": {
        "id": "sivan",
        "term": "Sivan",
        "category": "concepts",
        "intro": "<p>Sivan is the third month of the Hebrew sacred calendar (corresponding to the post-exilic Babylonian month names adopted in the Ezra-Nehemiah period), falling approximately in May–June. It is mentioned once in the Hebrew Bible, in Esther 8:9: Mordecai's counter-decree permitting the Jews to defend themselves was written on the twenty-third day of the third month, which is Sivan, in the twelfth year of Ahasuerus. Sivan corresponds broadly to the agricultural season of the wheat harvest in Palestine (following the barley harvest of Nisan–Iyar), and the feast of Weeks (Pentecost/Shavuot) falls in this month — the feast celebrated on the fiftieth day after the first grain offering of Passover (Leviticus 23:15–16), historically associated with the giving of the Torah at Sinai.</p>",
        "sections": [],
        "hitchcock_meaning": "a bush or thorn",
        "source_ids": {"easton": "sivan", "smith": "sivan", "isbe": "sivan"},
        "key_refs": ["Esther 8:9", "Leviticus 23:15"]
    },
    "skin-coats-made-of": {
        "id": "skin-coats-made-of",
        "term": "Skin, Coats made of",
        "category": "concepts",
        "intro": "<p>Coats of skin were the garments God made for Adam and Eve after the Fall to clothe their nakedness: <em>the LORD God made for Adam and for his wife garments of skins and clothed them</em> (Genesis 3:21). This act of divine provision stands in contrast to their own inadequate covering of fig leaves (Genesis 3:7), and has been read by theologians as the first act of atoning sacrifice — the death of animals to cover human shame — foreshadowing the redemptive covering that would come through Christ. The specific animals used are not identified. The garments of skin were practical for nomadic life in contrast to woven cloth, and archaeological evidence confirms that skin garments were among the earliest human clothing.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "skin-coats-made-of"},
        "key_refs": ["Genesis 3:21", "Genesis 3:7"]
    },
    "skull-the-place-of-a": {
        "id": "skull-the-place-of-a",
        "term": "Skull, The place of a",
        "category": "places",
        "intro": "<p>The place of a skull is the translation of both the Hebrew <em>Golgotha</em> (an Aramaic form) and the Latin <em>Calvaria</em> (from which <em>Calvary</em> is derived), referring to the site of Jesus's crucifixion outside Jerusalem. All four Gospels identify the location by this name (Matthew 27:33; Mark 15:22; Luke 23:33; John 19:17). The Gospel of John adds that it was <em>near the city</em> and a garden was there.</p><p>The reason for the name is not given in Scripture. Common explanations include: the site was shaped like a skull, it was a place of execution where skulls were left, or it was named from a topographic feature. The traditional location, identified since at least the fourth century, is within the Church of the Holy Sepulchre in Jerusalem. A second proposal, Gordon's Calvary north of Damascus Gate, gained popularity in the nineteenth century. Archaeological and historical evidence supports the area around the Church of the Holy Sepulchre as outside the first-century city walls and thus a plausible crucifixion site.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "skull-the-place-of-a"},
        "key_refs": ["Matthew 27:33", "John 19:17", "Mark 15:22"]
    },
    "slave": {
        "id": "slave",
        "term": "Slave",
        "category": "concepts",
        "intro": "<p>Slavery as an institution pervaded the ancient Near East, and the biblical text both regulates and ultimately subverts it. The Hebrew and Greek words typically translated <em>servant</em> in English Bibles (<em>eved</em>, <em>doulos</em>) more accurately mean <em>slave</em> — bound service with no legal autonomy. The Mosaic Law established important limitations: Hebrew slaves were released in the seventh year (Exodus 21:2; Deuteronomy 15:12–18), brutal treatment could result in the slave's freedom (Exodus 21:26–27), and the law forbade returning a runaway slave to his master (Deuteronomy 23:15–16).</p><p>The book of Philemon addresses slavery directly: Paul sends back the runaway slave Onesimus with a letter asking his master Philemon to receive him <em>no longer as a slave but better than a slave, as a dear brother</em> (Philemon 16) — a request widely read as an implicit appeal for manumission. Paul's theological reframing is decisive: in Christ <em>there is neither slave nor free</em> (Galatians 3:28), and both master and slave have the same Master in heaven (Ephesians 6:9). The trajectory of biblical ethics, embodied in the Jubilee legislation and the gospel, is toward freedom (Isaiah 58:6; Luke 4:18).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "slave", "smith": "slave"},
        "key_refs": ["Exodus 21:2", "Philemon 16", "Galatians 3:28", "Deuteronomy 15:12"]
    },
    "slime": {
        "id": "slime",
        "term": "Slime",
        "category": "concepts",
        "intro": "<p>Slime in the KJV Bible refers to natural bitumen or asphalt — <em>hemar</em> in Hebrew — a petroleum product that seeped naturally to the surface in the Dead Sea region and was used as a waterproof mortar and caulking agent. The builders of Babel used slime (bitumen) for mortar in their brick construction: <em>they had brick for stone and slime for mortar</em> (Genesis 11:3). The Vale of Siddim (southern Dead Sea) was full of slime pits into which the kings of Sodom and Gomorrah fell in their rout (Genesis 14:10). Moses's mother used slime (<em>hemar</em>) along with pitch to waterproof the basket in which she hid the infant Moses among the reeds of the Nile (Exodus 2:3). The bitumen of the Dead Sea region was known in antiquity and exported as a commercial commodity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "slime", "smith": "slime"},
        "key_refs": ["Genesis 11:3", "Genesis 14:10", "Exodus 2:3"]
    },
    "sling": {
        "id": "sling",
        "term": "Sling",
        "category": "concepts",
        "intro": "<p>The sling was a simple but devastatingly effective weapon of the ancient world, consisting of a leather or woven pouch with two cords attached. The slinger placed a smooth stone in the pouch, whirled it overhead or at the side, and released one cord to hurl the projectile with great force and accuracy. Judges 20:16 mentions seven hundred Benjamite left-handed slingers so accurate they could hit a hair's breadth without missing. The sling was standard equipment in ancient Near Eastern armies alongside bows and spears.</p><p>David's defeat of Goliath with a sling and a single stone from the brook (1 Samuel 17:40–50) is the most famous biblical use of the weapon — David reached into his bag, took a stone, slung it, and struck the Philistine in the forehead. This victory became symbolic of divine deliverance through unexpected instruments: God's power made effective through the weakness of a shepherd boy against a heavily armed giant. The same image recurs in Zechariah 9:15, which prophesies that the sons of Zion will be like a warrior's stones in a sling.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sling", "smith": "sling", "isbe": "sling"},
        "key_refs": ["1 Samuel 17:40", "Judges 20:16", "Zechariah 9:15"]
    },
    "smith": {
        "id": "smith",
        "term": "Smith",
        "category": "concepts",
        "intro": "<p>Smiths — craftsmen who worked metal — are mentioned throughout Scripture in connection with both warfare and worship. The craft of metalworking is attributed to Tubal-cain, <em>forger of all cutting instruments of bronze and iron</em> (Genesis 4:22), in the genealogy of Cain. By the time of the Exodus, skilled artisans like Bezalel were filled with the Spirit of God with ability in crafting bronze, silver, and gold for the Tabernacle (Exodus 31:2–5).</p><p>The Philistines maintained a monopoly on iron smithing to prevent Israel from making swords and spears (1 Samuel 13:19–22) — a detail that explains Israelite military disadvantage in the early monarchy. Nebuchadnezzar deported the smiths and craftsmen from Jerusalem (2 Kings 24:14) as a strategic measure to prevent the rebuilding of weapons and fortifications. Isaiah used the smith as a metaphor: the smith who heats iron and works it with strong arms is like any craftsman making an idol — both are making something finite and lifeless from the same material that warms and cooks their food (Isaiah 44:12–17).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "smith", "smith": "smith", "isbe": "smith"},
        "key_refs": ["Genesis 4:22", "1 Samuel 13:19", "2 Kings 24:14", "Isaiah 44:12"]
    },
    "smyrna": {
        "id": "smyrna",
        "term": "Smyrna",
        "category": "places",
        "intro": "<p>Smyrna (modern İzmir, Turkey) was an ancient city of Ionia on the western coast of Asia Minor, about 40 miles north of Ephesus. It was one of the great cities of the Roman province of Asia, renowned for its beauty, its loyalty to Rome, and its thriving commercial harbor. The city had a large Jewish community and a strong imperial cult. <em>Smyrna</em> is the Greek word for myrrh, the fragrant resin used in embalming — a name some commentators have found symbolically resonant with the church's suffering.</p><p>Smyrna is one of the seven churches addressed in Revelation 2–3. The letter to Smyrna (Revelation 2:8–11) is notably one of only two letters (with Philadelphia) containing no rebuke. Jesus identifies himself as <em>the First and the Last, who died and came to life</em> — an encouragement for a church facing tribulation, poverty, and slander from those who call themselves Jews. He promises: <em>Be faithful unto death, and I will give you the crown of life.</em> The early bishop Polycarp, martyred at Smyrna around 155 AD, is the most famous of the church's historical figures.</p>",
        "sections": [],
        "hitchcock_meaning": "myrrh",
        "source_ids": {"easton": "smyrna", "smith": "smyrna", "isbe": "smyrna"},
        "key_refs": ["Revelation 2:8", "Revelation 2:10", "Revelation 2:11"]
    },
    "snail": {
        "id": "snail",
        "term": "Snail",
        "category": "concepts",
        "intro": "<p>The snail is mentioned twice in the KJV Bible. Leviticus 11:30 lists the snail (<em>chomet</em>) among unclean creeping things, in a group with the chameleon, lizard, sand reptile, and mole — though the identification of some of these terms remains uncertain and some modern translations render <em>chomet</em> as <em>skink</em> or a type of lizard rather than a snail. Psalm 58:8 uses the image of a snail that melts as it moves — a simile for the wicked: <em>Let them be like the snail that dissolves into slime.</em> The reference likely alludes to the glistening wet track that a snail leaves behind, which ancient people apparently thought meant the creature was melting or wasting away as it moved. The image captures the psalmist's wish that the wicked would waste away and perish.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "snail", "smith": "snail", "isbe": "snail"},
        "key_refs": ["Psalm 58:8", "Leviticus 11:30"]
    },
    "snare": {
        "id": "snare",
        "term": "Snare",
        "category": "concepts",
        "intro": "<p>The snare (Hebrew <em>pah</em> or <em>moqesh</em>, Greek <em>pagis</em>) was a trap used to catch birds or animals, consisting of a noose or spring mechanism concealed to catch unsuspecting prey. The image pervades biblical wisdom, prophecy, and psalm literature as a metaphor for sudden, unexpected spiritual or moral danger. Proverbs repeatedly warns that the lips of an adulteress are a snare (Proverbs 7:23), that flattery is a snare (Proverbs 29:5), and that the fear of man brings a snare (Proverbs 29:25). Psalm 91:3 promises that God will deliver his servant from the snare of the fowler.</p><p>The Mosaic law warned that the idols of the Canaanites would be a snare to Israel (Exodus 23:33; Deuteronomy 7:16), a warning repeatedly fulfilled in the narratives of Judges. Paul warns Timothy of the snares of the devil who takes people captive to do his will (2 Timothy 2:26; 1 Timothy 3:7). Ecclesiastes 9:12 uses the snare as an image of death catching people suddenly, like fish in a net or birds in a trap.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "snare", "isbe": "snare"},
        "key_refs": ["Proverbs 29:25", "Psalm 91:3", "Exodus 23:33", "2 Timothy 2:26"]
    },
    "snow": {
        "id": "snow",
        "term": "Snow",
        "category": "concepts",
        "intro": "<p>Snow falls periodically in the higher elevations of Palestine and regularly on the peaks of Lebanon and Hermon, which retain their snowcaps well into summer. Job 38:22 pictures divine storehouses of snow and hail reserved for times of trouble and battle. The whiteness of snow serves as Scripture's most common image of absolute purity or complete cleansing: Isaiah 1:18 — <em>though your sins are like scarlet, they shall be white as snow</em>; Psalm 51:7 — <em>wash me and I shall be whiter than snow.</em> The transfigured appearance of Jesus on the mountain was described as white as light (Matthew 17:2), and the appearance of the angel at the resurrection was <em>like snow</em> (Matthew 28:3).</p><p>Psalm 148:8 lists snow among the elements that praise God by fulfilling his command. Proverbs 31:21 commends the virtuous woman who is not afraid of snow for her household, since they are all clothed in scarlet. Proverbs 25:13 compares a faithful messenger to the coolness of snow in the heat of harvest — refreshing and reliable.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "snow", "smith": "snow", "isbe": "snow"},
        "key_refs": ["Isaiah 1:18", "Psalm 51:7", "Job 38:22", "Proverbs 25:13"]
    },
    "so": {
        "id": "so",
        "term": "So",
        "category": "people",
        "intro": "<p>So was the king of Egypt to whom Hoshea the last king of Israel sent envoys as part of an attempt to break free from Assyrian vassalage (2 Kings 17:4). Shalmaneser king of Assyria discovered the conspiracy, imprisoned Hoshea, and besieged Samaria — leading to the fall of the northern kingdom in 722 BC and the deportation of its population. The identity of <em>So king of Egypt</em> has been much debated. Proposals include Osorkon IV, a pharaoh of the Twenty-Second Dynasty who ruled in the Nile Delta; Tefnakht of Sais; or a reading of the text as a place name (Sais) rather than a personal name. Egyptian records offer no certain confirmation, and the brief mention in 2 Kings does not clarify the pharaoh's identity further.</p>",
        "sections": [],
        "hitchcock_meaning": "a measure for grain; vail",
        "source_ids": {"easton": "so", "smith": "so", "isbe": "so"},
        "key_refs": ["2 Kings 17:4"]
    },
    "soap": {
        "id": "soap",
        "term": "Soap",
        "category": "concepts",
        "intro": "<p>Soap in the ancient biblical world was not the fatty-acid soap of modern chemistry but a vegetable alkali — a cleaning agent made from the ashes of certain plants rich in potash or sodium carbonate. The Hebrew <em>borith</em> (from a root meaning <em>to be clean</em>) is the term used in Jeremiah 2:22 and Malachi 3:2. Jeremiah 2:22 uses it in a devastating metaphor: <em>Though you wash yourself with lye and use much soap, the stain of your guilt is still before me.</em> No amount of ritual or moral cleansing can remove the corruption of Israel's idolatry. Malachi 3:2 asks who can endure the day of the coming messenger: <em>he is like a refiner's fire and like fullers' soap</em> — the soap used by those who cleaned and whitened cloth. The image is of purifying divine judgment that will both cleanse the Levites and expose the guilt of the wicked.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "soap", "smith": "soap", "isbe": "soap"},
        "key_refs": ["Jeremiah 2:22", "Malachi 3:2"]
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
    print(f'BP S4: Ships → Soap: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__':
    main()
