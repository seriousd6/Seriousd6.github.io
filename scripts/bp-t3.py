"""
BP Article Synthesis — t3: Topaz → Tyropoeon Valley
Covers Easton entries: Topaz through Tyropoeon Valley (38 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'sea of', 'river', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals
  - names:    Hitchcock-only (no Easton/Smith entry exists)
  - events:   title is clearly an event (battle, feast, exile, flood, etc.)

Script: scripts/bp-t3.py
Run: python3 scripts/bp-t3.py
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


ARTICLES = {
    "topaz": {
        "id": "topaz",
        "term": "Topaz",
        "category": "concepts",
        "intro": "<p>Topaz (Hebrew <em>pitdah</em>) was a precious stone prized in the ancient world for its golden-yellow or greenish translucence. It appears in three significant biblical settings: as the second stone of the first row in the high priest's breastplate (Exodus 28:17; 39:10), symbolizing one of the twelve tribes of Israel; in Ezekiel's lament over the king of Tyre, who is said to have been \"in Eden the garden of God\" adorned with every precious stone including topaz (Ezekiel 28:13); and as one of the twelve foundation stones of the New Jerusalem in Revelation 21:20. Job 28:19 refers to \"the topaz of Ethiopia\" as something that cannot compare with wisdom, indicating the gem was imported from Nubia. The precise identification of biblical <em>pitdah</em> with modern topaz is not certain; some scholars identify it with a yellow peridot or chrysolite.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "topaz", "smith": "topaz", "isbe": "topaz"},
        "key_refs": ["Exodus 28:17", "Ezekiel 28:13", "Job 28:19", "Revelation 21:20"]
    },
    "tophel": {
        "id": "tophel",
        "term": "Tophel",
        "category": "places",
        "intro": "<p>Tophel (meaning \"ruin\" or \"without understanding\" in Hebrew) was a place in the wilderness of Sinai referenced in the opening verse of Deuteronomy (1:1) as one of the locations near which Moses delivered his farewell speeches to Israel: \"These are the words which Moses spake unto all Israel on this side Jordan in the wilderness, in the plain over against the Suph, between Paran, and Tophel, and Laban, and Hazeroth, and Dizahab.\" The verse is essentially establishing the geographic setting for the entire book of Deuteronomy. The exact location of Tophel is uncertain, though some scholars have identified it with Tafileh, a site in modern Jordan east of the Arabah valley, southeast of the Dead Sea. It is mentioned only this once in the Bible.</p>",
        "hitchcock_meaning": "ruin; folly; without understanding",
        "source_ids": {"easton": "tophel", "smith": "tophel", "isbe": "tophel"},
        "key_refs": ["Deuteronomy 1:1"]
    },
    "tophet": {
        "id": "tophet",
        "term": "Tophet",
        "category": "places",
        "intro": "<p>Tophet (also spelled Topheth; possibly from Hebrew <em>toph</em>, \"drum,\" with reference to drums beaten to mask the cries of sacrificed children) was a site in the Valley of Hinnom (Gehenna) south of Jerusalem where Israelites, particularly during the apostate periods of the monarchy, sacrificed their children by fire to the god Molech. Jeremiah condemns the practice in the strongest terms (Jeremiah 7:31–32; 19:6, 11–14) and prophesies that God will make Tophet and the whole valley a place of burial so filled with corpses it will be called \"the valley of slaughter.\" King Josiah defiled Tophet during his reforms to prevent further use (2 Kings 23:10). Isaiah 30:33 uses Tophet as a typological image for the judgment prepared for the Assyrian king: \"For Tophet is ordained of old; yea, for the king it is prepared.\" The site's association with fire, death, and divine judgment contributed to the later Jewish use of Gehenna as a term for the place of punishment after death.</p>",
        "hitchcock_meaning": "a drum; betraying",
        "source_ids": {"easton": "tophet"},
        "key_refs": ["Jeremiah 7:31", "2 Kings 23:10", "Isaiah 30:33"]
    },
    "torches": {
        "id": "torches",
        "term": "Torches",
        "category": "concepts",
        "intro": "<p>Torches in Scripture appear both as practical implements of illumination and as vivid images of power, judgment, and divine glory. In the account of Jesus's arrest in Gethsemane, the cohort of soldiers and officers sent by the chief priests came equipped with \"lanterns and torches and weapons\" (John 18:3), lighting the dark garden for their search. Nahum 2:3–4 employs the image of torches to depict the terrifying advance of the Babylonian army against Nineveh: \"The chariots flash like torches in the day of his preparation.\" In the Old Testament, the torch (<em>lapid</em>) appears in Abram's covenant ceremony, where \"a smoking firepot and a flaming torch passed between the pieces\" (Genesis 15:17), representing God's self-binding oath. Samson used torches tied to foxes' tails to burn the Philistines' grain fields (Judges 15:4–5). Daniel 10:6 describes the angelic messenger with \"eyes like flaming torches,\" an image of searching, penetrating divine sight echoed in Revelation's portrait of Christ (Revelation 1:14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "torches"},
        "key_refs": ["John 18:3", "Nahum 2:3", "Genesis 15:17", "Judges 15:4"]
    },
    "torment": {
        "id": "torment",
        "term": "Torment",
        "category": "concepts",
        "intro": "<p>Torment in the New Testament most frequently translates the Greek <em>basanos</em>, a word originally denoting a touchstone used to test the purity of gold, then extended to mean the rack or instrument of judicial torture, and finally suffering itself. Matthew 4:24 records that those afflicted with \"divers diseases and torments\" (as well as those possessed by demons) were brought to Jesus and healed. The demonic spirits in the Gadarene account feared that Jesus had come to torment them before the appointed time (Matthew 8:29), acknowledging his authority to inflict eschatological punishment. Luke 16:23–28 uses the term in Jesus's parable of Lazarus and the rich man, describing the rich man's anguish in Hades as torment from which no relief was available. In Revelation, the torment of Babylon (18:7, 10, 15) and of the beast-worshippers (14:10–11) describes the irreversible consequences of divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "torment"},
        "key_refs": ["Matthew 4:24", "Matthew 8:29", "Luke 16:23", "Revelation 14:10"]
    },
    "tortoise": {
        "id": "tortoise",
        "term": "Tortoise",
        "category": "concepts",
        "intro": "<p>The tortoise appears once in the King James Bible in the list of unclean creatures in Leviticus 11:29, where the Hebrew <em>tsabh</em> is rendered \"tortoise\" among the swarming things that move on the ground. Modern translations and lexicographers generally identify <em>tsabh</em> more precisely as a large lizard — probably the monitor lizard (<em>Varanus niloticus</em> or a related species) common to the Near East, rather than a tortoise properly speaking. The KJV rendering reflects the understanding of seventeenth-century translators. The passage categorizes <em>tsabh</em> among the eight unclean swarming things whose carcasses conveyed ritual impurity to any vessel, food, or person that touched them (Leviticus 11:29–38). The careful distinction of clean and unclean animals in the Mosaic law served both hygienic and symbolic purposes in marking Israel's separateness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tortoise", "smith": "tortoise", "isbe": "tortoise"},
        "key_refs": ["Leviticus 11:29"]
    },
    "tow": {
        "id": "tow",
        "term": "Tow",
        "category": "concepts",
        "intro": "<p>Tow (Hebrew <em>neoret</em>) refers to the short, coarse fibers separated from flax during the process of hackling or combing, leaving behind the finer linen. In Judges 16:9, Delilah uses the image of tow to describe the ease with which Samson broke the seven fresh bowstrings she had bound him with: \"And he brake the withs, as a thread of tow is broken when it toucheth the fire.\" Tow ignites instantly when touched by flame, making it a proverbial image of frailty and instantaneous destruction. Isaiah 1:31 uses a related image — \"the strong shall be as tow\" — to depict the coming judgment on the wicked in Israel. The ease with which tow burns made it a natural figure for anything that would be rapidly consumed under divine wrath or proved to be far weaker than it appeared.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tow"},
        "key_refs": ["Judges 16:9", "Isaiah 1:31"]
    },
    "tower-of-the-furnaces": {
        "id": "tower-of-the-furnaces",
        "term": "Tower of the furnaces",
        "category": "places",
        "intro": "<p>The Tower of the Furnaces (Hebrew <em>migdal hattannirim</em>) was a fortification tower on the north-western angle of the walls of Jerusalem, mentioned twice in the book of Nehemiah in the account of the post-exilic rebuilding of the city walls: it appears in the list of construction assignments (Nehemiah 3:11) and again in the processional dedication of the completed wall (Nehemiah 12:38). The tower's name likely derives from its proximity to a quarter of the city where bakers or potters operated kilns and furnaces. Jeremiah 37:21 references the \"bakers' street\" in the vicinity, suggesting the area had a recognized commercial character. The tower was part of the defensive circuit of Jerusalem rebuilt under Nehemiah's leadership in the mid-fifth century BC after the Babylonian destruction of the city.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tower-of-the-furnaces", "isbe": "tower-of-the-furnaces"},
        "key_refs": ["Nehemiah 3:11", "Nehemiah 12:38"]
    },
    "towers": {
        "id": "towers",
        "term": "Towers",
        "category": "concepts",
        "intro": "<p>Towers in Scripture served military, agricultural, and symbolic purposes. Militarily, watchtowers provided vantage points for defenders and were built into city walls at intervals; the tower at Shechem fell when Abimelech burned it with its thousand refugees inside (Judges 9:46–49). Agricultural towers in vineyards were built for watchmen to guard the harvest (Isaiah 5:2; Matthew 21:33), a detail Jesus incorporated into his parable of the wicked tenants. The unfinished Tower of Babel (Genesis 11:4) represents humanity's rebellious attempt at self-exaltation, answered by God's dispersal of the builders. Tower imagery also appears in the Psalms as a metaphor for divine protection: \"The name of the LORD is a strong tower; the righteous runneth into it and is safe\" (Proverbs 18:10), and God himself is called a \"tower of salvation\" (2 Samuel 22:51). The tower of Penuel, torn down by Gideon as judgment on its inhabitants (Judges 8:9, 17), illustrates the political dimension of tower-destruction as punishment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "towers"},
        "key_refs": ["Genesis 11:4", "Judges 8:17", "Proverbs 18:10", "Matthew 21:33"]
    },
    "trachonitis": {
        "id": "trachonitis",
        "term": "Trachonitis",
        "category": "places",
        "intro": "<p>Trachonitis (Greek, meaning \"rugged\" or \"rocky country\") was a volcanic basalt plateau lying north-east of the Jordan, corresponding roughly to the Old Testament region of Argob. It appears in the New Testament only in Luke 3:1, which identifies Philip the tetrarch as ruler of \"Ituraea and the region of Trachonitis\" at the time John the Baptist began his ministry. The region is characterised by extensive lava fields riddled with caves and fissures, which historically made it a refuge for outlaws and robbers. The Romans, particularly Herod the Great and subsequently his son Philip, made sustained efforts to pacify and settle Trachonitis, bringing in colonists from Babylon. The area corresponds broadly to the modern Leja region of southern Syria. Its precise borders in the first century are uncertain, but it lay between Damascus to the north and Gaulanitis to the west.</p>",
        "hitchcock_meaning": "stony",
        "source_ids": {"easton": "trachonitis", "smith": "trachonitis", "isbe": "trachonitis"},
        "key_refs": ["Luke 3:1"]
    },
    "tradition": {
        "id": "tradition",
        "term": "Tradition",
        "category": "concepts",
        "intro": "<p>Tradition (Greek <em>paradosis</em>, \"that which is handed over\") refers in Scripture to teaching passed down from one generation to another, whether oral or written. The word is used neutrally in Paul's letters to describe apostolic teaching delivered to the churches (1 Corinthians 11:2; 2 Thessalonians 2:15; 3:6), where he commends believers for holding to the traditions he has transmitted. However, in the Gospels the term frequently carries a negative force: Jesus rebukes the Pharisees and scribes for setting aside the commandment of God to keep \"the tradition of the elders\" (Mark 7:3, 9, 13; Matthew 15:2–6), specifically citing the <em>corban</em> practice as an example of tradition nullifying divine law. Paul likewise warns against philosophy and \"vain deceit, after the tradition of men\" as opposed to Christ (Colossians 2:8). The tension between received tradition and living divine authority is a recurring theme in both Testaments, resolved in the New Testament by the priority of Christ and the apostolic witness over accumulated human custom.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tradition", "isbe": "tradition"},
        "key_refs": ["Mark 7:9", "Mark 7:13", "Colossians 2:8", "2 Thessalonians 2:15"]
    },
    "trance": {
        "id": "trance",
        "term": "Trance",
        "category": "concepts",
        "intro": "<p>Trance (Greek <em>ekstasis</em>, from which the English word \"ecstasy\" derives) describes a state in which a person is temporarily removed from normal sensory awareness and receives divine revelation. In the New Testament, Peter falls into a trance (<em>ekstasis</em>) while praying on a rooftop in Joppa and receives the vision of the sheet containing unclean animals, through which God prepares him for the conversion of Cornelius (Acts 10:10; 11:5). Paul describes a trance in the Jerusalem temple in which the Lord appeared to him and commanded him to leave the city and go to the Gentiles (Acts 22:17). His account in 2 Corinthians 12:1–4 of being \"caught up to the third heaven\" may also describe such an experience, though he uses different vocabulary there. The trance is thus associated in the New Testament specifically with moments of pivotal divine direction expanding the mission of the church beyond Jewish boundaries.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "trance", "smith": "trance", "isbe": "trance"},
        "key_refs": ["Acts 10:10", "Acts 11:5", "Acts 22:17"]
    },
    "transfiguration-the": {
        "id": "transfiguration-the",
        "term": "Transfiguration, the",
        "category": "events",
        "intro": "<p>The Transfiguration of Jesus occurred on a \"high mountain apart\" — traditionally identified as Mount Tabor or, by some scholars, Mount Hermon — approximately six days after Peter's confession at Caesarea Philippi. All three Synoptic Gospels record the event (Matthew 17:1–8; Mark 9:2–8; Luke 9:28–36): Jesus's face shone like the sun and his garments became dazzling white; Moses and Elijah appeared conversing with him; and a voice from a bright cloud declared, \"This is my beloved Son; hear him.\" Peter, James, and John, who had accompanied Jesus, fell on their faces in terror. The Transfiguration stands at the midpoint of Jesus's public ministry, looking back to the baptism (where the same divine voice spoke) and forward to the cross and resurrection. Smith identifies it as the culminating point of Christ's public ministry. Peter's eyewitness testimony of the event is explicitly invoked in 2 Peter 1:16–18 as confirmation of the apostolic proclamation of Christ's power and majesty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "transfiguration-the", "smith": "transfiguration-the"},
        "key_refs": ["Matthew 17:1", "Mark 9:2", "Luke 9:28", "2 Peter 1:16"]
    },
    "treasure-cities": {
        "id": "treasure-cities",
        "term": "Treasure cities",
        "category": "concepts",
        "intro": "<p>Treasure cities (also called store cities or supply cities) were fortified depots built to store food, weapons, and strategic materials for military campaigns or emergency use. In Exodus 1:11, the Israelites during their Egyptian bondage were compelled to build the treasure cities of Pithom and Rameses for Pharaoh — a detail that archaeological excavation at Tell el-Maskhuta (possibly Pithom) has confirmed through the discovery of large storage chambers. Solomon also built extensive treasure cities (1 Kings 9:19; 2 Chronicles 8:4–6), including Hazor, Megiddo, Gezer, and Beth-horon, creating a network of royal supply depots across his kingdom. 1 Chronicles 27:25 lists the officer Azmaveth as overseer of the king's treasuries in the field and in the cities, suggesting a developed royal logistics system. The construction of such cities required large forced-labor corvées, which contributed to the social tensions that led to the division of the kingdom after Solomon's death.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "treasure-cities"},
        "key_refs": ["Exodus 1:11", "1 Kings 9:19", "1 Chronicles 27:25"]
    },
    "treasure-houses": {
        "id": "treasure-houses",
        "term": "Treasure houses",
        "category": "concepts",
        "intro": "<p>Treasure houses were secure repositories for royal, temple, or state wealth in the ancient Near East. In the Old Testament, the Jerusalem temple had its own dedicated treasury, and both its sacred vessels and accumulated wealth were periodically raided by foreign kings — Shishak of Egypt (1 Kings 14:26), Jehoash of Israel (2 Kings 14:14), and eventually Nebuchadnezzar of Babylon (Daniel 1:2), who carried the vessels to the house of his god in Babylon. The books of Ezra and Nehemiah record the reverse movement: Cyrus's decree authorized the return of these vessels from the Persian royal treasure house (Ezra 5:17; 7:20), and Nehemiah established dedicated storerooms for the temple treasury (Nehemiah 10:38; 13:12–13). The care given to temple treasure houses reflects the ancient understanding that the wellbeing of the sanctuary's wealth corresponded to the health of the covenant relationship between God and his people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "treasure-houses"},
        "key_refs": ["Daniel 1:2", "Ezra 5:17", "Nehemiah 10:38"]
    },
    "treasury": {
        "id": "treasury",
        "term": "Treasury",
        "category": "concepts",
        "intro": "<p>The treasury of the Jerusalem temple consisted of thirteen trumpet-shaped bronze receptacles located in the Court of the Women, into which worshippers cast their offerings. The Gospels record two significant scenes set there. In Mark 12:41–44 (Luke 21:1–4), Jesus sat opposite the treasury and observed worshippers contributing gifts, singling out a poor widow who cast in two small copper coins (<em>lepta</em>) as having given more than all the wealthy donors — \"for she of her want did cast in all that she had.\" In John 8:20, the treasury area is where Jesus spoke the words recorded in John 8, a location the evangelist notes expressly. Matthew 27:6 records that the chief priests refused to put Judas's thirty pieces of silver back into the <em>korban</em> (treasury) because it was blood money, instead purchasing the Potter's Field — fulfilling Zechariah 11:12–13 as cited by Matthew.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "treasury", "smith": "treasury"},
        "key_refs": ["Mark 12:41", "John 8:20", "Matthew 27:6"]
    },
    "tree-of-life": {
        "id": "tree-of-life",
        "term": "Tree of life",
        "category": "concepts",
        "intro": "<p>The Tree of Life stood in the midst of the Garden of Eden alongside the Tree of the Knowledge of Good and Evil (Genesis 2:9). After the fall, God expelled Adam and Eve from the garden specifically to prevent them from eating of it and living forever (Genesis 3:22–24), placing cherubim and a flaming sword to guard the way. Its fruit is thus associated with immortality — a partaking not yet permitted to fallen humanity. The Tree of Life reappears as a wisdom motif in Proverbs (3:18; 11:30; 13:12; 15:4), where it becomes a metaphor for wisdom, righteousness, and fulfilled hope. The most theologically rich recurrence is in the book of Revelation (2:7; 22:2, 14), where the Tree of Life stands in the new Jerusalem \"on either side of the river\" bearing twelve fruits and whose leaves are \"for the healing of the nations\" — its access now restored to the redeemed, reversing the expulsion from Eden. The arc from Genesis to Revelation thus frames redemptive history between two appearances of the Tree of Life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tree-of-life", "isbe": "tree-of-life"},
        "key_refs": ["Genesis 2:9", "Genesis 3:22", "Proverbs 3:18", "Revelation 22:2"]
    },
    "tree-of-the-knowledge-of-good-and-evil": {
        "id": "tree-of-the-knowledge-of-good-and-evil",
        "term": "Tree of the knowledge of good and evil",
        "category": "concepts",
        "intro": "<p>The Tree of the Knowledge of Good and Evil stood in the midst of the Garden of Eden and was the one tree explicitly forbidden to Adam and Eve by God: \"of the tree of the knowledge of good and evil, thou shalt not eat of it: for in the day that thou eatest thereof thou shalt surely die\" (Genesis 2:17). Its name suggests that eating it would confer a moral and experiential knowledge that God had reserved for himself — an autonomous wisdom gained by transgression rather than by trusting obedience. The serpent's temptation exploited this by promising Eve that eating would make her \"as gods, knowing good and evil\" (Genesis 3:5). Eve saw the fruit as desirable for wisdom, and after both she and Adam ate, \"the eyes of them both were opened\" (Genesis 3:7) — but to their shame and alienation from God rather than to the divine dignity the serpent had promised. The episode is the paradigm of human rebellion and the entry point of sin, death, and curse into creation, setting the stage for the entire biblical narrative of redemption.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tree-of-the-knowledge-of-good-and-evil"},
        "key_refs": ["Genesis 2:17", "Genesis 3:5", "Genesis 3:6", "Genesis 3:22"]
    },
    "trespass-offering": {
        "id": "trespass-offering",
        "term": "Trespass offering",
        "category": "concepts",
        "intro": "<p>The trespass offering (Hebrew <em>'asham</em>, \"guilt\" or \"debt\") was one of the five main Levitical sacrifices, distinct from the sin offering (<em>chattat</em>) in that it addressed violations involving the misappropriation of something sacred or the infringement of another's rights. The law is given in Leviticus 5:14–6:7 and Numbers 5:5–8. It was required in cases of unwitting misuse of sacred objects (Leviticus 5:15), certain hidden sins (Leviticus 5:17–19), and deliberate wrongs against a neighbor combined with a false oath (Leviticus 6:2–5). In the last case restitution of the principal plus a fifth was required in addition to the sacrifice — emphasizing the restorative as well as expiatory function of the offering. The trespass offering appears in Isaiah 53:10, where the Servant of the LORD is said to make his soul an <em>'asham</em> — a guilt offering — for the sins of the people, providing the richest typological basis in the Old Testament for the substitutionary atonement accomplished by Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "trespass-offering", "smith": "trespass-offering", "isbe": "trespass-offering"},
        "key_refs": ["Leviticus 5:14", "Leviticus 6:2", "Numbers 5:5", "Isaiah 53:10"]
    },
    "tribe": {
        "id": "tribe",
        "term": "Tribe",
        "category": "concepts",
        "intro": "<p>A tribe in the biblical sense was a large kinship group descended from a single ancestor, organized as a social, political, and military unit. The twelve tribes of Israel descended from the twelve sons of Jacob (also named Israel), though the list varies slightly depending on context: Joseph's two sons Ephraim and Manasseh were each reckoned as a tribe in territorial allotments, while Levi was excluded from territorial inheritance as the priestly tribe dispersed throughout the land. The tribal structure was foundational to Israelite life from the Exodus and wilderness period through the period of the Judges, when tribal confederacy was the primary political form, to the monarchy, where tribal distinctions continued to shape power dynamics. The division of the kingdom after Solomon's death followed tribal lines — Judah and Benjamin in the south, ten tribes in the north. In the New Testament, Revelation 7 presents the sealing of 144,000 from the twelve tribes of Israel as a symbol of the complete people of God, and Revelation 21:12 names the twelve tribes on the gates of the new Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tribe", "isbe": "tribe"},
        "key_refs": ["Genesis 49:28", "Numbers 1:44", "Revelation 7:4", "Revelation 21:12"]
    },
    "tribulation": {
        "id": "tribulation",
        "term": "Tribulation",
        "category": "concepts",
        "intro": "<p>Tribulation (Hebrew <em>tsar</em>, \"narrow\" or \"pressed\"; Greek <em>thlipsis</em>, \"pressure\" or \"affliction\") denotes severe suffering, persecution, or distress in Scripture. In Deuteronomy 4:30, Moses foretells that in the last days tribulation will drive Israel to return to the LORD. In the New Testament, tribulation is presented as the normal condition of believers in this age: \"In the world ye shall have tribulation: but be of good cheer; I have overcome the world\" (John 16:33). Paul counts on tribulation to produce patience (Romans 5:3–4) and sees present suffering as incomparable to future glory (Romans 8:18). Jesus's discourse in Matthew 24 speaks of \"great tribulation, such as was not since the beginning of the world\" preceding the end, a passage much debated as to whether it refers to the siege of Jerusalem in AD 70, a future eschatological event, or both. In Romans 2:9, tribulation and anguish constitute the penal consequence awaiting those who do evil.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tribulation", "isbe": "tribulation"},
        "key_refs": ["Deuteronomy 4:30", "John 16:33", "Romans 5:3", "Matthew 24:21"]
    },
    "tribute": {
        "id": "tribute",
        "term": "Tribute",
        "category": "concepts",
        "intro": "<p>Tribute in Scripture refers both to taxes imposed by a king on his subjects or on conquered peoples, and to the temple tax required of every adult male Israelite. The forced-labor tribute (<em>mas</em>) was imposed by Solomon on the Canaanites remaining in the land (1 Kings 9:21), and the heavy burden he placed on Israel contributed to the division of the kingdom. In the New Testament, the question of tribute takes on theological sharpness: the Pharisees and Herodians attempt to trap Jesus with the question of whether it is lawful to pay tribute to Caesar (Matthew 22:17–21; Mark 12:14–17), and Jesus's response — \"render unto Caesar what is Caesar's, and unto God what is God's\" — became the foundational Christian statement on church and state. Matthew 17:24–27 records a separate episode concerning the temple tax (<em>didrachma</em>): Jesus, declaring that the sons of the king are free, nonetheless instructs Peter to pay it to avoid giving offense, with the money miraculously provided in a fish's mouth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tribute", "smith": "tribute", "isbe": "tribute"},
        "key_refs": ["Matthew 22:17", "Matthew 17:24", "Romans 13:6", "1 Kings 9:21"]
    },
    "trinity": {
        "id": "trinity",
        "term": "Trinity",
        "category": "concepts",
        "intro": "<p>Trinity is a theological term not found in Scripture but used to express the biblical teaching that the one God (Deuteronomy 6:4; Isaiah 44:6; Mark 12:29) eternally subsists as three distinct Persons — Father, Son, and Holy Spirit — who are co-equal and co-eternal in nature while remaining numerically one in being. The doctrine is not explicitly stated in a single biblical passage but is derived from the cumulative witness of both Testaments. The Old Testament contains plural forms of address to God, Trinitarian echoes in the repeated threefold blessing and vision passages, and the presence of the Spirit and the Word as divine agents. The New Testament is more explicit: the baptism of Jesus reveals all three Persons simultaneously (Matthew 3:16–17); the Great Commission commands baptism \"into the name\" (singular) \"of the Father and of the Son and of the Holy Spirit\" (Matthew 28:19); and Paul's Trinitarian benediction in 2 Corinthians 13:14 became the standard form of Christian blessing. The formal doctrine was defined at the Council of Nicaea (AD 325) and Councils of Constantinople (AD 381), ruling out subordinationism and modalism.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "trinity", "isbe": "trinity"},
        "key_refs": ["Deuteronomy 6:4", "Matthew 3:16", "Matthew 28:19", "2 Corinthians 13:14"]
    },
    "troas": {
        "id": "troas",
        "term": "Troas",
        "category": "places",
        "intro": "<p>Troas (named after the ancient city of Troy in its vicinity) was a port city on the north-western coast of Asia Minor (modern Turkey), located near the southern entrance to the Hellespont. It was a major transit point between Asia and Europe in the Roman period. Troas figures prominently in Paul's missionary journeys: in Acts 16:8–11, Paul receives his Macedonian vision there — the call to \"come over into Macedonia and help us\" — initiating the gospel's first advance into Europe. In 2 Corinthians 2:12, Paul mentions Troas as a place where an open door for preaching awaited him, though he could not rest there because he had not found Titus. Acts 20:6–12 records Paul's extended stay at Troas, where he preached until midnight and a young man named Eutychus fell from a window; Paul restored him to life. In 2 Timothy 4:13, Paul asks Timothy to bring his cloak and books left with Carpus at Troas.</p>",
        "hitchcock_meaning": "penetrated",
        "source_ids": {"easton": "troas", "smith": "troas", "isbe": "troas"},
        "key_refs": ["Acts 16:8", "Acts 20:6", "2 Corinthians 2:12", "2 Timothy 4:13"]
    },
    "trogyllium": {
        "id": "trogyllium",
        "term": "Trogyllium",
        "category": "places",
        "intro": "<p>Trogyllium was a small promontory and anchorage on the western coast of Asia Minor, opposite the island of Samos, near the city of Miletus. It appears in Acts 20:15 in the Western text tradition, which adds that Paul's ship \"tarried\" at Trogyllium — a brief overnight stop between Samos and Miletus during his third missionary journey as he made haste to reach Jerusalem before Pentecost. The location offered a sheltered anchorage for ancient ships navigating the notoriously difficult waters between the island of Samos and the mainland. Some manuscripts of Acts omit the reference, which accounts for its absence in certain modern translations. Trogyllium is mentioned by ancient geographers including Strabo and is identified with a promontory today called Cape Mykale or nearby Doğanbey in Turkey.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "trogyllium", "smith": "trogyllium", "isbe": "trogyllium"},
        "key_refs": ["Acts 20:15"]
    },
    "trophimus": {
        "id": "trophimus",
        "term": "Trophimus",
        "category": "people",
        "intro": "<p>Trophimus (Greek, meaning \"well-nourished\" or \"a foster-child\") was a Gentile Christian from Ephesus who accompanied Paul on his final journey to Jerusalem (Acts 20:4). His presence in Jerusalem at the end of Paul's third missionary journey became the occasion for the riot that led to Paul's arrest: certain Asian Jews, seeing Paul in the city with Trophimus, falsely assumed that Paul had brought the Gentile into the temple, crying out that he had defiled the holy place (Acts 21:28–29). This accusation, though untrue, triggered the mob violence that resulted in Paul's imprisonment under Roman custody. Paul's later letter to Timothy mentions that he had left Trophimus sick at Miletus (2 Timothy 4:20) — a detail that incidentally attests that the apostle did not invariably heal his companions, adding a realistic texture to the Pauline mission narrative.</p>",
        "hitchcock_meaning": "well educated; well brought up",
        "source_ids": {"easton": "trophimus", "smith": "trophimus", "isbe": "trophimus"},
        "key_refs": ["Acts 20:4", "Acts 21:29", "2 Timothy 4:20"]
    },
    "trumpets": {
        "id": "trumpets",
        "term": "Trumpets",
        "category": "concepts",
        "intro": "<p>Trumpets in the Bible appear in a wide variety of materials and forms, serving military, liturgical, and eschatological functions. The two main Hebrew terms are <em>shofar</em> (the curved horn of a ram or goat, used primarily for signaling) and <em>chatsotsrah</em> (the straight silver trumpet prescribed in Numbers 10:1–10, made in pairs for the priests). God commanded Moses to make two silver trumpets for the assembly, for journeying, and for war; the blowing of them over burnt offerings and peace offerings was to serve as a memorial before God. The shofar was blown at Sinai when God descended (Exodus 19:16, 19), at the fall of Jericho (Joshua 6:4–20), and at the coronation of kings. In eschatological passages, the trumpet announces the day of the LORD (Joel 2:1; Zephaniah 1:16) and in the New Testament heralds both the resurrection (1 Corinthians 15:52; 1 Thessalonians 4:16) and the angelic judgments of Revelation (Revelation 8–9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "trumpets"},
        "key_refs": ["Numbers 10:2", "Joshua 6:4", "1 Corinthians 15:52", "Revelation 8:6"]
    },
    "trumpets-feast-of": {
        "id": "trumpets-feast-of",
        "term": "Trumpets, Feast of",
        "category": "events",
        "intro": "<p>The Feast of Trumpets was celebrated on the first day of Tishri (the seventh month of the sacred year, first month of the civil year), distinguished from ordinary new-moon festivals by the especially prominent blowing of the shofar throughout the day. The law is given in Leviticus 23:23–25 and Numbers 29:1–6: it was a day of solemn rest, a holy convocation, with specific burnt offerings in addition to the regular new-moon sacrifices. The Mishnah tractate Rosh Hashanah (\"Head of the Year\") elaborates the rabbinic observance that developed from this day, which became the Jewish New Year. The repeated trumpet blasts served as a \"memorial\" before God — a summoning of divine attention on behalf of the people — and as a call to repentance in preparation for the Day of Atonement ten days later. Some Christian interpreters have seen the Feast of Trumpets as a type of the eschatological trumpet blast announcing the return of Christ and the gathering of his people (1 Thessalonians 4:16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "trumpets-feast-of", "smith": "trumpets-feast-of", "isbe": "trumpets-feast-of"},
        "key_refs": ["Leviticus 23:24", "Numbers 29:1", "1 Thessalonians 4:16"]
    },
    "truth": {
        "id": "truth",
        "term": "Truth",
        "category": "concepts",
        "intro": "<p>Truth in Scripture carries a range of meanings anchored in the Hebrew <em>'emeth</em> (faithfulness, reliability, stability) and the Greek <em>aletheia</em> (correspondence with reality, unconcealment). In Proverbs 12:17, 19, truth is contrasted with falsehood as what an honest witness speaks. In Isaiah 59:14–15, truth has \"fallen in the street\" as a social collapse alongside justice, describing the covenant breakdown of Israel. In the prophets, God's <em>'emeth</em> is his covenantal faithfulness — his reliability to keep his promises. The New Testament deepens the term: Jesus declares himself \"the way, the truth, and the life\" (John 14:6), identifying truth not merely as a quality but as a person. John's Gospel uses <em>aletheia</em> repeatedly: the Word \"full of grace and truth\" (John 1:14), \"the truth shall make you free\" (John 8:32), the Spirit as \"the Spirit of truth\" (John 16:13). Paul speaks of \"the truth of the gospel\" (Galatians 2:5, 14) as the content of apostolic proclamation. Pilate's question \"What is truth?\" (John 18:38) encapsulates the collision between Roman relativism and the embodied truth standing before him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "truth", "isbe": "truth"},
        "key_refs": ["Proverbs 12:19", "John 14:6", "John 8:32", "John 16:13"]
    },
    "tryphena-and-tryphosa": {
        "id": "tryphena-and-tryphosa",
        "term": "Tryphena and Tryphosa",
        "category": "people",
        "intro": "<p>Tryphena and Tryphosa were two female Christians in Rome whom Paul greets in the closing chapter of his letter to the Romans (Romans 16:12), commending them as women who \"labor in the Lord.\" Their names (Greek <em>Truphaina</em> and <em>Truphosa</em>, both from the root meaning \"delicate\" or \"luxurious\") are attested in Roman inscriptions, including several from the imperial household, raising the possibility that they were freedwomen or slaves of the imperial court. Paul's identical description of their work — \"laboring in the Lord\" — suggests they served in similar capacities, and they may have been sisters. Nothing further is known of them from Scripture or early tradition, but their inclusion in Paul's roster of personal greetings, alongside other women such as Priscilla, Mary, Junia, and Persis, reflects the active participation of women in the Roman church's ministry.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tryphena-and-tryphosa"},
        "key_refs": ["Romans 16:12"]
    },
    "tubal": {
        "id": "tubal",
        "term": "Tubal",
        "category": "people",
        "intro": "<p>Tubal was the fifth son of Japheth in the Table of Nations (Genesis 10:2), named alongside Meshech as an ancestor of northern peoples. The name is associated in biblical prophecy with a nation or tribal grouping in the far north or north-east. Isaiah 66:19 lists Tubal among the distant nations to whom God will send survivors to declare his glory. Ezekiel repeatedly pairs Tubal with Meshech as a trading partner of Tyre (Ezekiel 27:13) and as part of the coalition assembled under Gog for the great eschatological invasion of Israel (Ezekiel 38:2–3; 39:1). Ancient inscriptions identify Tubal (Assyrian <em>Tabal</em>) with a region in eastern Anatolia (modern Turkey), corresponding to the territory south of the Black Sea. The pairing of Meshech-Tubal in prophecy likely reflects their geographical proximity and military cooperation in the ancient world. In later prophetic interpretation they have sometimes been identified with more northern peoples, including Russia and Turkey.</p>",
        "hitchcock_meaning": "the earth; the world; confusion",
        "source_ids": {"easton": "tubal", "smith": "tubal", "isbe": "tubal"},
        "key_refs": ["Genesis 10:2", "Ezekiel 38:2", "Isaiah 66:19"]
    },
    "tubal-cain": {
        "id": "tubal-cain",
        "term": "Tubal-cain",
        "category": "people",
        "intro": "<p>Tubal-cain was the son of Lamech and Zillah in the antediluvian genealogy of Cain (Genesis 4:22), described as \"an instructor of every artificer in brass and iron\" — making him the biblical ancestor of metalworking, both in bronze and iron. His half-sister was Naamah. The name combines <em>Tubal</em> (possibly related to the Assyrian <em>Tabal</em>, a metalworking region) with <em>Cain</em>, suggesting a continuation of the Cainite line's cultural innovations: his forefather Jubal introduced music, and Jabal pioneered pastoral life. Tubal-cain's role as the father of metallurgy is significant because the working of metals — particularly iron — was closely connected to the development of weapons in the ancient world, and his invention is sometimes read as part of the escalating violence that characterized the pre-flood civilization, culminating in Lamech's boastful song of vengeance (Genesis 4:23–24).</p>",
        "hitchcock_meaning": "worldly possession; possessed of confusion",
        "source_ids": {"easton": "tubal-cain", "isbe": "tubal-cain"},
        "key_refs": ["Genesis 4:22"]
    },
    "turtle-turtle-dove": {
        "id": "turtle-turtle-dove",
        "term": "Turtle, Turtle-dove",
        "category": "concepts",
        "intro": "<p>The turtle-dove (Hebrew <em>tor</em>; Greek <em>trugon</em>) was a migratory bird whose seasonal return to Israel was celebrated as a sign of spring: \"The voice of the turtle is heard in our land\" (Song of Solomon 2:12). The turtle-dove was the bird of the poor in the Levitical sacrificial system: where the law permitted offering either a lamb or two doves or young pigeons, the dove option accommodated those unable to afford larger animals (Leviticus 1:14; 5:7; 12:8; 14:22). When Mary and Joseph brought the infant Jesus to the temple for purification and presentation, they offered \"a pair of turtledoves, or two young pigeons\" (Luke 2:24) — indicating they presented the offering of the poor, a detail consistent with their humble circumstances. The bird's gentle and mournful character made it a symbol of innocence and longing in ancient poetry, and its faithfulness to its mate was proverbial in antiquity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "turtle-turtle-dove"},
        "key_refs": ["Luke 2:24", "Leviticus 5:7", "Song of Solomon 2:12"]
    },
    "tychicus": {
        "id": "tychicus",
        "term": "Tychicus",
        "category": "people",
        "intro": "<p>Tychicus (Greek, meaning \"fortunate\" or \"by chance\") was an Asian Christian who served as one of Paul's most trusted personal messengers and emissaries. He accompanied Paul on the collection journey to Jerusalem (Acts 20:4) and was later the bearer of three of Paul's prison epistles: Ephesians (6:21–22), Colossians (4:7–8), and possibly Philemon, carrying the letters to their destinations and providing personal news of Paul's situation. Paul describes him in both Ephesians and Colossians as \"a beloved brother and faithful minister in the Lord\" — high praise for a man who served as Paul's link to churches he could not personally visit. Titus 3:12 and 2 Timothy 4:12 indicate that Paul also sent Tychicus on missions to Crete and Ephesus, making him one of the most extensively deployed of Paul's co-workers, trusted to represent the apostle's authority in sensitive ecclesiastical situations.</p>",
        "hitchcock_meaning": "casual; by chance",
        "source_ids": {"easton": "tychicus", "smith": "tychicus", "isbe": "tychicus"},
        "key_refs": ["Ephesians 6:21", "Colossians 4:7", "Acts 20:4", "2 Timothy 4:12"]
    },
    "type": {
        "id": "type",
        "term": "Type",
        "category": "concepts",
        "intro": "<p>A type (Greek <em>tupos</em>, \"stamp,\" \"impression,\" or \"pattern\") in biblical theology is an Old Testament person, event, institution, or object that God designed to prefigure a corresponding New Testament reality — its \"antitype\" (<em>antitupos</em>). The Greek word <em>tupos</em> appears in Scripture with meanings ranging from a physical mark (John 20:25, the print of the nails) to a moral pattern (Romans 6:17; Philippians 3:17) to an explicit typological designation (Romans 5:14; 1 Corinthians 10:6, 11). Paul calls Adam \"a type of the one who was to come\" (Romans 5:14), and in 1 Corinthians 10:6, 11 the wilderness experiences of Israel are said to have occurred \"as types for us\" and were written down as warnings for the end of the ages. Hebrews develops the typological method most extensively, presenting the Levitical priesthood, tabernacle, and sacrificial system as shadows (<em>skia</em>) of the heavenly realities fulfilled in Christ. Typology is distinct from allegory in that it treats the historical reality of both type and antitype seriously, finding divine intention in the patterns of history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "type", "isbe": "type"},
        "key_refs": ["Romans 5:14", "1 Corinthians 10:11", "Hebrews 9:24", "John 20:25"]
    },
    "tyrannus": {
        "id": "tyrannus",
        "term": "Tyrannus",
        "category": "people",
        "intro": "<p>Tyrannus (Greek, meaning \"tyrant\" or \"prince\") was a man at Ephesus in whose school or lecture hall Paul conducted his daily teaching ministry for approximately two years (Acts 19:9–10). When opposition in the synagogue became too severe, Paul withdrew with the disciples and began reasoning daily in \"the school of Tyrannus,\" a practice that continued long enough that, as Luke records, \"all who dwelt in Asia heard the word of the Lord Jesus, both Jews and Greeks.\" Whether Tyrannus was a philosopher, rhetor, or simply the owner of a hall available during midday hours (the Western text adds that Paul taught there from the fifth to the tenth hour, the customary siesta time when lecture halls were idle), his premises provided the base for one of the most extensive periods of settled ministry in Paul's career. The Ephesian mission, with its attendant miracles and the riot of the silversmiths (Acts 19:23–41), was built on this extended teaching period in the school of Tyrannus.</p>",
        "hitchcock_meaning": "a prince; one that reigns",
        "source_ids": {"easton": "tyrannus", "smith": "tyrannus", "isbe": "tyrannus"},
        "key_refs": ["Acts 19:9", "Acts 19:10"]
    },
    "tyre": {
        "id": "tyre",
        "term": "Tyre",
        "category": "places",
        "intro": "<p>Tyre (Hebrew <em>Tsor</em>, \"rock\"; Greek <em>Turos</em>) was the principal city of ancient Phoenicia, located on the eastern Mediterranean coast approximately 23 miles north of Acre and 20 miles south of Sidon. Originally built on the mainland and on a small rocky island offshore, it became one of the greatest commercial powers of the ancient world, establishing colonies throughout the Mediterranean including Carthage. In the Old Testament, Tyre was on friendly terms with Israel under Hiram I, who supplied cedar timber and craftsmen for Solomon's temple (1 Kings 5:1–12; 2 Chronicles 2:3–16) and later built a fleet of ships for Solomon at Ezion-geber (1 Kings 9:26–28). Its princess Jezebel, daughter of the Tyrian king Ethbaal, married Ahab of Israel and introduced Baal worship (1 Kings 16:31). The prophets pronounced severe judgment on Tyre — Isaiah (chapter 23), Ezekiel (chapters 26–28), Amos (1:9–10), and Joel (3:4–8) — which was partially fulfilled by Nebuchadnezzar's thirteen-year siege and completed by Alexander the Great, who in 332 BC built a causeway from the mainland to the island fortress and razed it. Jesus visited the region of Tyre and Sidon (Matthew 15:21; Mark 7:24) and cited it as a city that would have repented had it seen his miracles (Matthew 11:21–22).</p>",
        "hitchcock_meaning": "Tyrus, strength; rock; sharp",
        "source_ids": {"easton": "tyre", "smith": "tyre", "isbe": "tyre"},
        "key_refs": ["1 Kings 5:1", "Ezekiel 26:3", "Matthew 11:21", "Acts 12:20"]
    },
    "tyropoeon-valley": {
        "id": "tyropoeon-valley",
        "term": "Tyropoeon Valley",
        "category": "places",
        "intro": "<p>The Tyropoeon Valley (Greek, meaning \"Valley of the Cheesemongers\" or \"of the cheesemakers\") is the name given by the Jewish historian Josephus to the central valley that ran north-south through ancient Jerusalem, separating the western hill (the upper city) from the eastern hill containing the temple mount. The valley was much deeper in antiquity than it appears today; centuries of accumulated debris have largely filled it in, making its original topography difficult to appreciate without archaeological excavation. The Tyropoeon was traversed by a series of bridges connecting the western city to the temple precinct, the most impressive of which was supported by the large arch whose remains were identified by Edward Robinson in the nineteenth century (Robinson's Arch). The valley served as a commercial artery of the city and its name suggests the presence of a market district there. Josephus describes it in detail in his account of the topography of Jerusalem in <em>Jewish War</em> 5.4.1, making it one of the few Jerusalem geographical features known primarily from extra-biblical sources.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "tyropoeon-valley"},
        "key_refs": []
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP t3: Topaz → Tyropoeon Valley: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
