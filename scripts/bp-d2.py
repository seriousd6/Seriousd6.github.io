"""
BP Article Synthesis — d2: Diana → Dye
Covers Easton entries: Diana through Dye (71 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Named biblical individuals (Hitchcock match or clear person)
  - places:   Geographic locations (cities, plains, gates, rivers)
  - concepts: Theological terms, ritual objects, cultural practices, animals, materials
  - events:   Specific biblical occurrences (none in this range)
  - names:    Hitchcock-only (none in this range — all have Easton entries)

Script: scripts/bp-d2.py
Run: python3 scripts/bp-d2.py  (from project root)
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
    "diana": {
        "id": "diana",
        "term": "Diana",
        "category": "concepts",
        "intro": "<p>Diana, called Artemis in Greek, was the goddess of hunting, the moon, and chastity, worshipped as the great mother deity of Ephesus. Her magnificent temple there—one of the Seven Wonders of the ancient world—made her cult the defining feature of Ephesian civic and economic life. She appears in the New Testament in Acts 19, where Paul's preaching so diminished the market for silver shrines of the goddess that the silversmiths' guild, led by Demetrius, incited a riot in her honor; the crowd filled the theater for two hours chanting \"Great is Artemis of the Ephesians!\" (Acts 19:28, 34).</p><p>The Ephesian Artemis was distinct from the Greek Artemis of classical mythology: she was depicted as a multi-breasted fertility figure, reflecting an Eastern goddess tradition predating Greek influence. The episode in Acts illustrates both the economic power of ancient religion and the direct challenge the gospel of Christ posed to the pagan cult industry of Asia Minor.</p>",
        "hitchcock_meaning": "luminous, perfect",
        "source_ids": {"easton": "diana", "smith": "diana"},
        "key_refs": ["Acts 19:23", "Acts 19:28", "Acts 19:34"],
        "sections": []
    },
    "diblaim": {
        "id": "diblaim",
        "term": "Diblaim",
        "category": "people",
        "intro": "<p>Diblaim, whose name means <em>cluster of figs</em>, was the father of Gomer, the woman the prophet Hosea was commanded by God to take as his wife (Hos. 1:3). Beyond this single mention, no further information about Diblaim appears in Scripture. His daughter Gomer's marriage to Hosea—commanded as a living parable of Israel's faithlessness to the LORD—was one of the most theologically charged prophetic acts in the Old Testament, and Diblaim's only significance is this family connection: as the father of the woman whose marriage and repeated unfaithfulness served as the central prophetic symbol of the book of Hosea.</p>",
        "hitchcock_meaning": "cluster of figs",
        "source_ids": {"easton": "diblaim", "smith": "diblaim", "isbe": "diblaim"},
        "key_refs": ["Hosea 1:3"],
        "sections": []
    },
    "diblathaim": {
        "id": "diblathaim",
        "term": "Diblathaim",
        "category": "places",
        "intro": "<p>Diblathaim (meaning <em>two cakes</em> or <em>double fig-cake</em>) was a city of Moab east of the Dead Sea. It appears in the wilderness itinerary as Almon-diblathaim (Num. 33:46–47) and as Beth-diblathaim in the prophetic oracle against Moab (Jer. 48:22). The site lay on the Moabite plateau and is listed among the Moabite cities upon which Jeremiah pronounced divine judgment in connection with Babylon's destruction of the region.</p><p>Its precise location has not been confirmed archaeologically, though it may correspond to Khirbet Deleilat esh-Sherqiyeh in the eastern Moabite highlands northeast of the Dead Sea. The ISBE notes that the name's occurrence both in the wilderness itinerary and in Jeremiah's oracle links it to two distinct historical periods—the Exodus era and the late pre-exilic period—making it an identifiable landmark of Moabite geography.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "diblathaim", "isbe": "diblathaim"},
        "key_refs": ["Numbers 33:46", "Numbers 33:47", "Jeremiah 48:22"],
        "sections": []
    },
    "dibon": {
        "id": "dibon",
        "term": "Dibon",
        "category": "places",
        "intro": "<p>Dibon (meaning <em>pining</em> or <em>wasting</em>) was one of the most prominent cities of Moab, situated approximately four miles north of the Arnon Gorge on the Transjordanian plateau. It appears first as one of the cities taken from Sihon king of the Amorites during Israel's passage through Transjordan (Num. 21:30) and was subsequently assigned to the tribes of Reuben and Gad as a rebuilt settlement (Num. 32:3, 34; Josh. 13:9, 17). Also called Dibon-gad, it served as an important Moabite administrative center in later periods.</p><p>The Moabite Stone (Mesha Stele), discovered at modern Dhiban in 1868, was inscribed by the Moabite king Mesha and references Dibon as his capital city—providing extrabiblical confirmation of the city's prominence. Isaiah 15:2 and Jeremiah 48:18, 22 include Dibon in sweeping oracles of judgment against Moab. Archaeological excavations at Dhiban have confirmed continuous occupation from the Early Bronze Age onward.</p>",
        "hitchcock_meaning": "abundance of knowledge",
        "source_ids": {"easton": "dibon", "smith": "dibon"},
        "key_refs": ["Numbers 21:30", "Numbers 32:34", "Isaiah 15:2", "Jeremiah 48:18"],
        "sections": []
    },
    "didymus": {
        "id": "didymus",
        "term": "Didymus",
        "category": "people",
        "intro": "<p>Didymus is the Greek word for <em>twin</em>, used in the Gospel of John as an alternative name for the apostle Thomas (John 11:16; 20:24; 21:2). The designation indicates that Thomas's Aramaic name—<em>Tʾōmā</em>, meaning twin—was rendered into Greek for the benefit of wider readers, with both names presented as equivalents. Why Thomas bore this epithet is unexplained in the biblical text; whether he had an actual twin sibling or the name was applied for other reasons is unknown.</p><p>Thomas is best known for his absence when the risen Christ first appeared to the disciples, his subsequent profession of doubt, and his dramatic confession upon seeing Jesus eight days later: \"My Lord and my God!\" (John 20:28)—one of the most direct Christological declarations in the Gospels. Early Christian tradition, unverified in the New Testament, credits Thomas with bringing the gospel to India, where communities bearing his name persist.</p>",
        "hitchcock_meaning": "a twin; double",
        "source_ids": {"easton": "didymus", "smith": "didymus", "isbe": "didymus"},
        "key_refs": ["John 11:16", "John 20:24", "John 20:28"],
        "sections": []
    },
    "dimnah": {
        "id": "dimnah",
        "term": "Dimnah",
        "category": "places",
        "intro": "<p>Dimnah (meaning <em>dunghill</em>) was a city within the tribal territory of Zebulun, assigned to the Merarite branch of the Levites as part of the Levitical city allotments (Josh. 21:35). It is likely identical to Rimmon in the parallel Levitical city list in 1 Chronicles 6:77, where Dimnah does not appear—suggesting either a scribal variant between the two accounts or a dual name for the same location.</p><p>The site's exact location in the territory of Zebulun has not been identified archaeologically, and it plays no narrative role in the Old Testament beyond its mention in the Levitical city lists. The ISBE notes the textual difficulty between the Joshua and Chronicles lists as significant for assessing the reliability and transmission of these administrative records.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dimnah", "smith": "dimnah", "isbe": "dimnah"},
        "key_refs": ["Joshua 21:35", "1 Chronicles 6:77"],
        "sections": []
    },
    "dinah": {
        "id": "dinah",
        "term": "Dinah",
        "category": "people",
        "intro": "<p>Dinah (meaning <em>judged</em> or <em>vindicated</em>) was the daughter of Jacob by Leah, and the only daughter of Jacob mentioned by name in the genealogical records (Gen. 30:21; 46:15). Her narrative role centers on a deeply disruptive episode: Shechem son of Hamor saw her while she was visiting the women of the land, seized her, and lay with her—an act the text describes as defilement (Gen. 34:2). Her brothers, learning of it, responded in apparent agreement to the proposed marriage but extracted a condition that all Shechemite men be circumcised.</p><p>While the men were recovering, Simeon and Levi—Dinah's full brothers—entered the city and killed all the males, then plundered the town (Gen. 34:25–29). Jacob rebuked them for bringing trouble on his household; they replied that their sister should not be treated as a harlot. Jacob recalled this violence in his deathbed blessing, scattering Simeon and Levi in Israel as a consequence (Gen. 49:5–7). Dinah herself speaks no words in the narrative, and she is never mentioned after Genesis 46:15's genealogical notice.</p>",
        "hitchcock_meaning": "judgment; who judges",
        "source_ids": {"easton": "dinah", "smith": "dinah", "isbe": "dinah"},
        "key_refs": ["Genesis 30:21", "Genesis 34:2", "Genesis 34:25", "Genesis 49:5"],
        "sections": []
    },
    "dine": {
        "id": "dine",
        "term": "Dine",
        "category": "concepts",
        "intro": "<p>Dine appears in Genesis 43:16, where Joseph commands that his brothers be brought to his house at noon to dine with him in Egypt—a custom Easton identifies as the standard Egyptian mealtime. The noon meal was likely the main meal of the day in Egypt, and the context of Joseph dining with his brothers (though at separate tables due to Egyptian custom, Gen. 43:32) represents a significant moment of escalating tension in the Joseph narrative before his self-revelation.</p><p>In the New Testament, Luke 14:12 uses the word in Jesus's teaching on true hospitality: not inviting only friends and family to dinners and banquets but welcoming the poor and those unable to repay. The broader biblical practice of table fellowship carried significant social and theological weight—sharing a meal signified acceptance, trust, and in some contexts covenant relationship. Jesus's repeated practice of dining with tax collectors and sinners was itself a theological statement about the nature of the kingdom (Luke 15:1–2; 19:5–7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dine"},
        "key_refs": ["Genesis 43:16", "Luke 14:12"],
        "sections": []
    },
    "dinhabah": {
        "id": "dinhabah",
        "term": "Dinhabah",
        "category": "places",
        "intro": "<p>Dinhabah (meaning <em>robbers' den</em> or <em>he gives judgment</em>) was the capital city of Bela son of Beor, the first named king of Edom, whose reign predated the Israelite monarchy (Gen. 36:32; 1 Chr. 1:43). The city appears only in the genealogical and royal list of Edomite kings, which records eight successive rulers of Edom without dynastic succession—each from a different family or city—suggesting an elective or competitive kingship structure rather than hereditary rule.</p><p>The location of Dinhabah is entirely unknown; no extrabiblical source or archaeological identification has been proposed with confidence. The ISBE notes the difficulty of locating Edomite cities from this early period. Dinhabah's significance is solely that it represents the administrative center of the earliest documented Edomite royal government in the Genesis genealogy.</p>",
        "hitchcock_meaning": "he gives judgment",
        "source_ids": {"easton": "dinhabah", "smith": "dinhabah", "isbe": "dinhabah"},
        "key_refs": ["Genesis 36:32", "1 Chronicles 1:43"],
        "sections": []
    },
    "dionysius": {
        "id": "dionysius",
        "term": "Dionysius",
        "category": "people",
        "intro": "<p>Dionysius the Areopagite was one of the converts Paul made at Athens following his address at the Areopagus (Acts 17:34). As a member of the Areopagus—the ancient civic and judicial council of Athens that had authority over education, morals, and public religion—Dionysius was a man of considerable social standing and intellectual formation. His conversion alongside a woman named Damaris is noted as one of the few named fruits of Paul's Athenian mission, which otherwise produced fewer converts than Paul's work in other cities.</p><p>Early church tradition, going back to Dionysius of Corinth (c. AD 170), identifies him as the first bishop of Athens, though this cannot be confirmed from the New Testament. A body of mystical theological writings circulated under the name \"Pseudo-Dionysius the Areopagite\" (likely composed c. AD 500) profoundly influenced medieval Christian mysticism and theology, though they bear no connection to the biblical Dionysius.</p>",
        "hitchcock_meaning": "divinely touched",
        "source_ids": {"easton": "dionysius", "smith": "dionysius", "isbe": "dionysius"},
        "key_refs": ["Acts 17:34"],
        "sections": []
    },
    "diotrephes": {
        "id": "diotrephes",
        "term": "Diotrephes",
        "category": "people",
        "intro": "<p>Diotrephes, whose name means <em>nourished by Jupiter</em> (reflecting a Greek pagan background), was a leader in a Christian congregation addressed in 3 John. The apostle John rebukes him pointedly as one who \"loves to have the preeminence\" among the church—refusing to acknowledge John's apostolic authority, refusing to receive the traveling missionaries John commended, forbidding others from welcoming them, and threatening to expel from the congregation those who showed hospitality (3 John 9–10).</p><p>Whether Diotrephes was a formally appointed church officer who abused his position or an upstart lay leader who had seized authority is debated in the commentaries. In either case his conduct stands as an early documented example of ambition for power disrupting the fellowship of the early church. John promises to deal with him personally on his next visit. The ISBE notes he may have represented a resistance to itinerant apostolic oversight as local congregations consolidated their own structures in the late first century.</p>",
        "hitchcock_meaning": "nourished by Jupiter",
        "source_ids": {"easton": "diotrephes", "smith": "diotrephes", "isbe": "diotrephes"},
        "key_refs": ["3 John 1:9", "3 John 1:10"],
        "sections": []
    },
    "disciple": {
        "id": "disciple",
        "term": "Disciple",
        "category": "concepts",
        "intro": "<p>Disciple (Greek <em>mathētēs</em>, meaning <em>learner</em> or <em>pupil</em>) designates in the New Testament the followers of a teacher, applied most broadly to the followers of Jesus but also to disciples of John the Baptist (Matt. 9:14; Luke 11:1) and of Moses (John 9:28). Jesus's call to discipleship was distinguished from the rabbinic model by the initiative: where Jewish students sought out a rabbi to follow, Jesus chose his disciples and summoned them with the command \"Follow me.\" The conditions of discipleship as Jesus articulated them are demanding—self-denial, cross-bearing, and a loyalty to him that takes precedence over family ties (Luke 14:26–27, 33).</p><p>The term encompasses both the Twelve specifically and the larger circle of followers. The Seventy-Two (Luke 10:1–17) represent a wider commissioned group, and the 120 in Acts 1:15 show disciples extending well beyond the core apostles. In the book of Acts, \"the disciples\" effectively becomes a synonym for \"believers\" or members of the Way. The Great Commission charges the apostles to \"make disciples of all nations\" (Matt. 28:19), placing discipleship-making—not merely conversion—as the mission's goal.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "disciple", "smith": "disciple", "isbe": "disciple"},
        "key_refs": ["Matthew 9:14", "Luke 14:26", "Luke 14:33", "Matthew 28:19"],
        "sections": []
    },
    "dish": {
        "id": "dish",
        "term": "Dish",
        "category": "concepts",
        "intro": "<p>Dish designates various vessels used for serving food in both domestic and sacred contexts in Scripture. In the tabernacle, golden dishes (<em>qᵊśāwōt</em>) were placed on the table of showbread alongside plates, flagons, and bowls (Exod. 25:29; 37:16). In Judges 5:25, Jael brought curds to Sisera in a \"lordly dish\"—a magnificent bowl—as part of the account of his assassination. Gideon placed meat in a basket with broth poured into a dish for the angel at the oak of Ophrah (Judg. 6:38).</p><p>In the New Testament, Jesus's statement at the Last Supper—\"He who has dipped his hand in the dish with me will betray me\" (Matt. 26:23)—refers to the common bowl from which bread was dipped in sauce or olive oil at the communal meal. Second Kings 21:13 uses the image of Jerusalem being wiped as one wipes a dish—turning it upside down and wiping it clean—as a metaphor for the totality of divine judgment upon the city.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dish", "smith": "dish", "isbe": "dish"},
        "key_refs": ["Exodus 25:29", "Judges 5:25", "2 Kings 21:13", "Matthew 26:23"],
        "sections": []
    },
    "dishan": {
        "id": "dishan",
        "term": "Dishan",
        "category": "people",
        "intro": "<p>Dishan (meaning <em>antelope</em> or possibly <em>a threshing</em>) was the youngest of the seven sons of Seir the Horite, the heads of the Horite clans who inhabited the region of Seir before the Edomites (descendants of Esau) dispossessed and replaced them (Gen. 36:21, 28, 30; Deut. 2:12; 1 Chr. 1:38, 42). Dishan's two sons were Uz and Aran. The Horites—whose name may derive from a Semitic root meaning \"cave dwellers\"—occupied the territory that later became Edom in the Transjordanian highlands south of the Dead Sea.</p><p>Dishan appears only in the genealogical tables of the Horite clans in Genesis 36 and the parallel Chronicles list, with no narrative role. His inclusion in these records reflects the ancient Israelite recognition of the pre-Edomite inhabitants of the region and their ethnic connection to Abraham's family through his nephew Lot's descendants.</p>",
        "hitchcock_meaning": "a threshing",
        "source_ids": {"easton": "dishan", "smith": "dishan"},
        "key_refs": ["Genesis 36:21", "Genesis 36:28", "Genesis 36:30"],
        "sections": []
    },
    "dispensation": {
        "id": "dispensation",
        "term": "Dispensation",
        "category": "concepts",
        "intro": "<p>Dispensation (Greek <em>oikonomia</em>, literally <em>household management</em> or <em>stewardship</em>) denotes in the New Testament both a specific responsibility entrusted to an agent and the divine arrangement by which that responsibility is ordered. In 1 Corinthians 9:17, Paul speaks of a \"stewardship\" (dispensation) committed to him for preaching the gospel. Ephesians 1:10 describes God's purpose as a \"dispensation of the fullness of times\"—a divinely ordered plan to unite all things in Christ. Ephesians 3:2 speaks of the \"dispensation of the grace of God\" given to Paul in connection with the mystery of Gentile inclusion; Colossians 1:25 similarly describes his commission to make God's word fully known.</p><p>The term became foundational in later Reformed and evangelical theology, particularly in the \"dispensationalist\" framework that divides redemptive history into distinct administrative epochs or dispensations, each characterized by a particular form of God's covenant relationship with humanity. This theological use goes well beyond the specific New Testament occurrences, which focus on present stewardship rather than historical periodization.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dispensation", "isbe": "dispensation"},
        "key_refs": ["1 Corinthians 9:17", "Ephesians 1:10", "Ephesians 3:2", "Colossians 1:25"],
        "sections": []
    },
    "dispersion": {
        "id": "dispersion",
        "term": "Dispersion",
        "category": "concepts",
        "intro": "<p>The Dispersion (Greek <em>diaspora</em>, meaning <em>scattered abroad</em>) refers to the settlement of Jewish communities outside the land of Israel, originating in the Assyrian deportation of the northern tribes (722 BC) and accelerating through the Babylonian exile of Judah (586 BC). By the New Testament era, Jewish diaspora communities existed throughout the Mediterranean world, Mesopotamia, and Egypt—in many cities numerically exceeding the Jewish population of Palestine. Significant communities flourished at Alexandria, Antioch, Rome, and in Asia Minor.</p><p>James 1:1 addresses his epistle to \"the twelve tribes scattered abroad\"—using <em>diaspora</em> as a descriptor for Jewish Christians living outside Israel. First Peter 1:1 similarly addresses \"the elect exiles of the Dispersion.\" Both uses carry theological overtones of a people who are sojourners and strangers in the world, awaiting their true homeland. The Dispersion also played a critical role in early Christian mission: Paul consistently found synagogues in diaspora cities as his initial point of contact, and the presence of Greek-speaking Jewish converts (\"Hellenists,\" Acts 6:1) shaped the theological character of early Christianity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dispersion"},
        "key_refs": ["James 1:1", "1 Peter 1:1", "Deuteronomy 30:4"],
        "sections": []
    },
    "distaff": {
        "id": "distaff",
        "term": "Distaff",
        "category": "concepts",
        "intro": "<p>The distaff (Hebrew <em>peleḵ</em>, meaning <em>a circle</em> or <em>spindle-whorl</em>) was a key implement in the ancient process of hand-spinning, the instrument around which raw fiber (wool or flax) was wound for twisting into yarn or thread. In Proverbs 31:19, the portrait of the capable wife describes her as one who \"puts her hands to the distaff, and her hands hold the spindle\"—emphasizing that household textile production was a primary mark of the virtuous Israelite woman's industry and skill.</p><p>The ISBE notes that the Hebrew term may refer specifically to the circular whorl (the weighted disk that maintains spindle rotation and tension) rather than the full rod of a distaff. Hand-spinning of flax and wool was central to the domestic economy of ancient Israel; garments and textiles were produced entirely within the household. The same root word (<em>peleḵ</em>) appears in Nehemiah 3 as a unit of a district, suggesting the term had both a technical textile meaning and a broader administrative use.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "distaff", "isbe": "distaff"},
        "key_refs": ["Proverbs 31:19"],
        "sections": []
    },
    "divination": {
        "id": "divination",
        "term": "Divination",
        "category": "concepts",
        "intro": "<p>Divination, the practice of discerning hidden knowledge or future events through occult means, is consistently condemned in Scripture. The Mosaic law explicitly prohibits augury, soothsaying, necromancy, consulting mediums, and interpreting omens, designating these as abominations of the nations Israel was dispossessing (Deut. 18:10–14). Forms of divination attested in the Old Testament include hydromancy (divining by water; Gen. 44:5), hepatoscopy (examining animal livers; Ezek. 21:21), casting arrows (belomancy; Ezek. 21:21), and consulting the dead (1 Sam. 28:8–20). Micah condemns prophets who divine for pay (Mic. 3:6–7, 11).</p><p>The theological ground for the prohibition is stated in Deuteronomy 18:15: God provides his own authorized spokesman—the prophet—making occult inquiry unnecessary and a sign of distrust. In the New Testament, Paul cast a spirit of divination (<em>pneuma python</em>) out of a slave girl at Philippi whose fortune-telling had been a lucrative business for her owners (Acts 16:16–18). The contrast between genuine prophetic revelation by the Spirit of God and divinatory inquiry through demonic means is a persistent thread in both Testaments.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "divination", "smith": "divination", "isbe": "divination"},
        "key_refs": ["Deuteronomy 18:10", "1 Samuel 28:8", "Micah 3:11", "Acts 16:16"],
        "sections": []
    },
    "divorce": {
        "id": "divorce",
        "term": "Divorce",
        "category": "concepts",
        "intro": "<p>Divorce, the dissolution of the marriage bond, was regulated but not originated by the Mosaic law (Deut. 24:1–4). The provision required a written certificate of divorce and forbade the husband from taking back a wife he had divorced if she had been married to another man in the interim. The Hebrew phrase indicating grounds for divorce—\"some indecency\" (Deut. 24:1)—was interpreted variously by rabbinic schools: the school of Shammai restricted it to sexual immorality; the school of Hillel allowed divorce for virtually any displeasure. Malachi 2:16 contains the divine statement most often translated \"I hate divorce.\"</p><p>In the New Testament, Jesus addresses divorce in the Sermon on the Mount (Matt. 5:31–32) and in debate with the Pharisees (Matt. 19:3–9; Mark 10:2–12), affirming the creation ideal of permanent marriage and restricting Mosaic provision to a concession to human hardness of heart. Paul addresses the complex situations of believing spouses married to unbelievers in 1 Corinthians 7:10–16. Ezra's reform requiring dissolution of marriages to foreign women (Ezra 10:11) represents the most controversial application of divorce legislation in the Old Testament period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "divorce", "smith": "divorce", "isbe": "divorce"},
        "key_refs": ["Deuteronomy 24:1", "Malachi 2:16", "Matthew 5:31", "Matthew 19:3"],
        "sections": []
    },
    "dizahab": {
        "id": "dizahab",
        "term": "Dizahab",
        "category": "places",
        "intro": "<p>Dizahab (meaning <em>region of gold</em>) was a place mentioned in the opening verse of Deuteronomy (Deut. 1:1) as one of the landmarks near which Moses delivered his final address to Israel: \"in the Arabah, opposite Suph, between Paran and Tophel, Laban, Hazeroth, and Dizahab.\" The precise list appears to situate the speech in the wilderness east of the Jordan in the plains of Moab, though the individual locations are difficult to identify with certainty.</p><p>Dizahab's exact position has not been confirmed, with most proposals placing it either in the Sinai Peninsula or in the Arabah south of the Dead Sea. Smith suggests it may be on the western shore of the Gulf of Aqaba. It receives no other mention in the biblical narrative, and no archaeological identification has been proposed with confidence. Its name's association with gold may reflect the presence of mineral resources in the region or simply preserve an ancient local designation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dizahab", "smith": "dizahab"},
        "key_refs": ["Deuteronomy 1:1"],
        "sections": []
    },
    "doctor": {
        "id": "doctor",
        "term": "Doctor",
        "category": "concepts",
        "intro": "<p>Doctor in the King James Version translates Greek terms meaning <em>teacher</em> (Greek <em>didaskalos</em> or <em>nomodidaskalos</em>). In Luke 2:46, the twelve-year-old Jesus is found in the temple \"sitting among the teachers (doctors), listening to them and asking them questions\"—a scene that astonished the assembled scholars with his understanding and his answers. Luke 5:17 introduces \"Pharisees and teachers of the law\" who had gathered from every village of Galilee, Judea, and Jerusalem as Jesus healed and taught.</p><p>In Acts 5:34, Gamaliel is specifically identified as a <em>nomodidaskalos</em>—a teacher of the law—\"held in honor by all the people,\" who counseled the Sanhedrin to adopt a wait-and-see posture toward the apostles. The term is essentially equivalent to \"rabbi\" or \"scribe\" in its Jewish context and designates those professionally trained to interpret and transmit the Torah. Paul identifies himself as having been educated \"at the feet of Gamaliel\" (Acts 22:3), placing him in the mainstream of first-century Jewish legal scholarship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "doctor", "isbe": "doctor"},
        "key_refs": ["Luke 2:46", "Luke 5:17", "Acts 5:34"],
        "sections": []
    },
    "dodai": {
        "id": "dodai",
        "term": "Dodai",
        "category": "people",
        "intro": "<p>Dodai the Ahohite was a military officer during the reign of David, named as commander of the division of twenty-four thousand men assigned to service in the second month of David's rotating military organization (1 Chr. 27:4). He is most likely the same person as Dodo the Ahohite (1 Chr. 11:12; 2 Sam. 23:9), the father of Eleazar—one of David's three greatest warriors. The name variation (Dodai/Dodo) is a minor textual variant between the Chronicles military list and the narrative accounts.</p><p>Eleazar son of Dodo performed one of the most celebrated acts of valor among the Thirty, holding his ground alone against the Philistines at Pas-dammim after the other Israelites had retreated, fighting until his hand was too exhausted to release the sword (2 Sam. 23:9–10). David and the people attributed the victory to the LORD. Dodai's family thus contributed both administrative service and legendary military achievement to David's kingdom.</p>",
        "hitchcock_meaning": "beloved",
        "source_ids": {"easton": "dodai", "smith": "dodai", "isbe": "dodai"},
        "key_refs": ["1 Chronicles 27:4", "2 Samuel 23:9"],
        "sections": []
    },
    "dodanim": {
        "id": "dodanim",
        "term": "Dodanim",
        "category": "people",
        "intro": "<p>Dodanim (also spelled Rodanim in 1 Chr. 1:7, likely the original reading) were a people descended from Javan, the son of Japheth, listed in the Table of Nations (Gen. 10:4). The spelling difference between Dodanim and Rodanim—a single Hebrew letter—is attributed by most scholars to a scribal transposition, with Rodanim being supported by the Samaritan Pentateuch and the Septuagint. The Rodanim are widely identified with the inhabitants of the island of Rhodes (<em>Rhodos</em>) and related Aegean maritime peoples.</p><p>Their inclusion in the Table of Nations among the Japhethite peoples who spread through the coastlands and islands of the Mediterranean (Gen. 10:5) is consistent with the known role of Rhodian and Aegean traders and colonists in the ancient world. Smith identifies them with the Dardanians of Trojans in one tradition, while favoring the Rhodian identification. No narrative events in Scripture involve the Dodanim/Rodanim directly.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dodanim", "smith": "dodanim"},
        "key_refs": ["Genesis 10:4", "1 Chronicles 1:7"],
        "sections": []
    },
    "dodo": {
        "id": "dodo",
        "term": "Dodo",
        "category": "people",
        "intro": "<p>Dodo (meaning <em>his uncle</em> or <em>beloved</em>) is the name of three biblical figures: (1) a man of Issachar, grandfather of Tola who judged Israel twenty-three years after Abimelech (Judg. 10:1); (2) an Ahohite of the tribe of Benjamin, father of Eleazar—one of David's three greatest military heroes, who single-handedly held the field against the Philistines at Pas-dammim until his hand cleaved to his sword, with David and the people attributing the victory to the LORD (2 Sam. 23:9–10; 1 Chr. 11:12); and (3) a Bethlehemite, father of Elhanan, another of David's thirty mighty men (2 Sam. 23:24).</p><p>The same Ahohite figure appears in 1 Chronicles 27:4 as Dodai, commander of the second monthly division of David's army. The name's occurrence across Issacharian, Benjamite, and Judahite families within a relatively short span suggests it was a name in common use in Israel during the pre-monarchic and early monarchic periods.</p>",
        "hitchcock_meaning": "his uncle",
        "source_ids": {"easton": "dodo", "smith": "dodo"},
        "key_refs": ["Judges 10:1", "2 Samuel 23:9", "2 Samuel 23:24"],
        "sections": []
    },
    "doeg": {
        "id": "doeg",
        "term": "Doeg",
        "category": "people",
        "intro": "<p>Doeg (meaning <em>fearful</em> or <em>careful</em>) was an Edomite, the chief overseer of Saul's flocks, who was detained at the sanctuary at Nob when David arrived fleeing from Saul and received from the priest Ahimelech both the consecrated showbread and the sword of Goliath (1 Sam. 21:7). When Saul interrogated his servants about who had aided David, Doeg volunteered his eyewitness account, triggering a chain of events that ended in catastrophe.</p><p>Saul ordered the execution of the priests of Nob—a command the Israelite soldiers refused to carry out—but Doeg complied, slaughtering eighty-five priests and then destroying the entire city of Nob: men, women, children, infants, and animals (1 Sam. 22:18–19). Abiathar alone escaped to join David. Psalm 52's superscription connects the psalm to Doeg, addressing him as a \"mighty man\" who boasts in evil and loves destruction. He became in later Jewish tradition the archetype of the malicious informer and the brutal enforcer of tyrannical power.</p>",
        "hitchcock_meaning": "careful, who acts with uneasiness",
        "source_ids": {"easton": "doeg", "smith": "doeg", "isbe": "doeg"},
        "key_refs": ["1 Samuel 21:7", "1 Samuel 22:18", "Psalms 52:1"],
        "sections": []
    },
    "dog": {
        "id": "dog",
        "term": "Dog",
        "category": "concepts",
        "intro": "<p>Dogs in the ancient biblical world were predominantly semi-wild scavengers rather than household pets. They roamed in packs at city gates and rubbish heaps, fed on refuse and carrion, and were associated with uncleanness and social dishonor. To call oneself a \"dead dog\" was a common expression of self-abasement before a superior (1 Sam. 24:14; 2 Sam. 9:8). Dead bodies devoured by dogs represented the most ignominious fate, invoked as divine judgment against Ahab and Jezebel (1 Kgs. 21:19, 23–24) and fulfilled in the death of Jezebel (2 Kgs. 9:35–36). Psalm 22:16 uses attacking dogs as a metaphor for the enemies surrounding the suffering psalmist.</p><p>In the New Testament, Jesus's exchange with the Syrophoenician woman (Matt. 15:26–27) uses the diminutive <em>kynarion</em> (\"little dogs,\" household pets) and her quick-witted reply about crumbs became the turning point in the conversation. Philippians 3:2 uses \"dogs\" as Paul's derogatory label for those demanding circumcision of Gentile Christians. Revelation 22:15 places \"dogs\" outside the holy city among the impure and immoral.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dog", "smith": "dog", "isbe": "dog"},
        "key_refs": ["1 Kings 21:19", "Psalms 22:16", "Matthew 15:26", "Philippians 3:2"],
        "sections": []
    },
    "doleful-creatures": {
        "id": "doleful-creatures",
        "term": "Doleful creatures",
        "category": "concepts",
        "intro": "<p>Doleful creatures appears only in Isaiah 13:21 (KJV), in the oracle of judgment against Babylon: \"But wild beasts of the desert shall lie there; and their houses shall be full of doleful creatures.\" The underlying Hebrew word (<em>ʾōḥîm</em>, literally \"shrieks\" or \"howlers\") likely refers to owls, jackals, or other creatures whose calls were associated with desolation and the uninhabited wilderness. Modern translations render the phrase variously as \"howling creatures,\" \"owls,\" or \"hyenas.\"</p><p>This vocabulary of desolation—wild animals inhabiting the ruins of once-great cities—is a standard prophetic motif used across multiple oracles to describe divine judgment reduced to wilderness (Isa. 34:13–15; Jer. 50:39; Zeph. 2:14). The reversal of the inhabited city into a haunt of nocturnal animals and desert creatures signifies not merely political defeat but the thoroughgoing removal of human civilization as a consequence of divine displeasure.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "doleful-creatures"},
        "key_refs": ["Isaiah 13:21"],
        "sections": []
    },
    "door-keeper": {
        "id": "door-keeper",
        "term": "Door-keeper",
        "category": "concepts",
        "intro": "<p>Door-keeper (Hebrew <em>shōʿēr</em>, <em>gatekeeper</em>) designates those responsible for guarding and controlling access to city gates, royal palaces, and the temple sanctuary. In the Levitical organization of the temple service, gatekeepers formed a distinct order assigned to the various doors and thresholds of the LORD's house (1 Chr. 9:17–27; 26:1–19; Neh. 11:19). Four principal families—the sons of Shallum, Akkub, Talmon, and Ahiman—served as porters in the temple gates, with 212 individuals registered in their genealogical records.</p><p>Psalm 84:10 contains one of Scripture's most celebrated sentiments: \"I would rather be a doorkeeper in the house of my God than dwell in the tents of wickedness\"—contrasting the lowest position of temple service with any residence outside God's presence. In the New Testament, John 18:16–17 refers to the doorkeeper of the high priest's courtyard who admitted Peter on the night of Jesus's arrest, and Acts 12:13 mentions Rhoda as the girl who came to the door when Peter knocked after his miraculous release from prison.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "door-keeper"},
        "key_refs": ["Psalms 84:10", "1 Chronicles 9:17", "John 18:16"],
        "sections": []
    },
    "door-posts": {
        "id": "door-posts",
        "term": "Door-posts",
        "category": "concepts",
        "intro": "<p>Door-posts (Hebrew <em>mezuzôt</em>) are the vertical structural members flanking the entrance of a room or building and carry significant religious and covenantal meaning in the Old Testament. In Exodus 12:7, God commanded Israelite families to apply the blood of the Passover lamb to the two doorposts and the lintel of their houses, so that the destroyer would pass over them—the event commemorated annually in the Passover. This inaugural use established the doorpost as a threshold marker of covenant belonging.</p><p>Deuteronomy 6:9 (and 11:20) extends this symbolism by commanding Israel to write the words of the Shema on the doorposts of their houses and gates—the instruction that gave rise to the Jewish <em>mezuzah</em> practice of affixing a small scripture scroll to the right doorpost of every entrance. Additionally, Exodus 21:6 and Deuteronomy 15:17 prescribe the doorpost as the place where a voluntary slave was to have his ear pierced with an awl as a public sign of permanent bond to his master.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "door-posts"},
        "key_refs": ["Exodus 12:7", "Deuteronomy 6:9", "Exodus 21:6"],
        "sections": []
    },
    "doors": {
        "id": "doors",
        "term": "Doors",
        "category": "concepts",
        "intro": "<p>Doors in the ancient Near East were typically constructed of wood, stone, or bronze, moving on pivots set into sockets in the threshold and lintel stones. Proverbs 26:14 captures the mechanical principle: \"As a door turns on its hinges, so does a sluggard on his bed.\" City gates and palace doors could be massive affairs—Samson carrying the gates of Gaza (posts, bar, and all) on his shoulders to the top of the hill (Judg. 16:3) conveys their weight and the extraordinary strength it implied. Job 38:10 uses the \"bars and doors\" of the sea as a metaphor for divine restraint placed on creation's most powerful forces.</p><p>In the New Testament, Jesus describes himself as both the shepherd who enters by the door (John 10:1–2) and as \"the door of the sheep\" (John 10:7, 9)—the only legitimate means of access to salvation and the true community of God's people. Revelation 3:20 uses the image of Christ standing at the door and knocking, a call for the tepid Laodicean church to open and receive him in fellowship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "doors", "smith": "doors"},
        "key_refs": ["Proverbs 26:14", "Judges 16:3", "John 10:7", "Revelation 3:20"],
        "sections": []
    },
    "dophkah": {
        "id": "dophkah",
        "term": "Dophkah",
        "category": "places",
        "intro": "<p>Dophkah (meaning <em>a knocking</em> or <em>driver</em>) was an Israelite encampment in the Sinai wilderness, listed in the travel itinerary of Numbers 33:12–13 between the wilderness of Sin and Alush on the route toward Mount Sinai. No narrative events are associated with Dophkah in the biblical text beyond its position in the wilderness travel log.</p><p>Modern scholars have proposed its identification with Serabit el-Khadim in the southern Sinai Peninsula—an Egyptian turquoise and copper mining site at which inscriptions referencing Semitic workers (including the Proto-Sinaitic script) have been found. The ISBE and some archaeologists support this identification as consistent with the geographic route from the Red Sea crossing toward Sinai. If correct, it would link Israel's wilderness journey to one of the most significant ancient industrial sites in the Sinai, and the Proto-Sinaitic inscriptions found there are among the earliest alphabetic writing known.</p>",
        "hitchcock_meaning": "a knocking",
        "source_ids": {"easton": "dophkah", "smith": "dophkah", "isbe": "dophkah"},
        "key_refs": ["Numbers 33:12", "Numbers 33:13"],
        "sections": []
    },
    "dor": {
        "id": "dor",
        "term": "Dor",
        "category": "places",
        "intro": "<p>Dor (meaning <em>generation</em> or <em>habitation</em>) was an ancient Canaanite royal city on the Mediterranean coast of Palestine, on the southern slopes of Mount Carmel. Its king joined the northern coalition defeated by Joshua at the waters of Merom (Josh. 11:1–2; 12:23). Though Dor fell within the tribal allotment of Manasseh, the tribe failed to drive out the Canaanite inhabitants (Judg. 1:27). In Solomon's administrative reorganization, Dor was the center of a province governed by Ben-abinadab, his son-in-law (1 Kgs. 4:11).</p><p>The site, identified with Tel Dor (Khirbet el-Burj) on the Carmel coast south of modern Haifa, has been extensively excavated. Evidence reveals continuous occupation from the Middle Bronze Age through the Hellenistic period, with particularly rich remains from the Late Bronze and Iron Ages, including evidence of Phoenician presence and maritime trade. In the Hellenistic period it was known as Dora and served as a harbor city of some importance.</p>",
        "hitchcock_meaning": "generation, habitation",
        "source_ids": {"easton": "dor", "smith": "dor"},
        "key_refs": ["Joshua 11:1", "Judges 1:27", "1 Kings 4:11"],
        "sections": []
    },
    "dorcas": {
        "id": "dorcas",
        "term": "Dorcas",
        "category": "people",
        "intro": "<p>Dorcas (Greek <em>dorkas</em>, meaning <em>a female roe-deer</em> or <em>gazelle</em>—the Greek equivalent of the Aramaic name Tabitha) was a Christian disciple at Joppa (modern Jaffa) renowned for her charitable works, particularly making robes and garments for the poor widows of the community (Acts 9:36–42). When she died, the believers sent urgently for Peter in nearby Lydda. Peter came, dismissed the mourning widows, knelt in prayer beside her body, and commanded \"Tabitha, arise\"—whereupon she opened her eyes, sat up, and was presented alive to the saints and widows.</p><p>The miracle became widely known throughout Joppa and directly led many to believe in the Lord. Dorcas is notable as one of only two women in the New Testament explicitly called a <em>mathētria</em>—a female disciple (Acts 9:36). Her story illustrates the early church's practical ministry to widows and the poor and provides one of the clearest New Testament analogies to the resurrections performed by Elijah (1 Kgs. 17:17–23) and Elisha (2 Kgs. 4:32–37).</p>",
        "hitchcock_meaning": "a female roe-deer",
        "source_ids": {"easton": "dorcas", "smith": "dorcas", "isbe": "dorcas"},
        "key_refs": ["Acts 9:36", "Acts 9:40", "Acts 9:42"],
        "sections": []
    },
    "dothan": {
        "id": "dothan",
        "term": "Dothan",
        "category": "places",
        "intro": "<p>Dothan (meaning <em>two wells</em> or <em>the law; custom</em>) was a prosperous pastoreland and town in the hill country of Samaria, approximately thirteen miles north of Shechem. It appears in two pivotal narratives: first, as the place where Joseph found his brothers tending their flocks—it was at Dothan that they conspired to kill him, cast him into a waterless pit, and then sold him to the Ishmaelite caravan bound for Egypt (Gen. 37:17–28); and second, as the city where the prophet Elisha was residing when the king of Syria sent a large military force to capture him (2 Kgs. 6:13–17).</p><p>In the Elisha account, Dothan is surrounded by the Aramean army, but Elisha prays that his servant may see the greater army of the LORD—the horses and chariots of fire filling the hills around the city. The Syrian force is subsequently struck with blindness and led to Samaria. The site is identified with Tell Dothan in the Jezreel Valley approach, which has been extensively excavated, revealing continuous occupation from around 3100 BC through the Hellenistic period.</p>",
        "hitchcock_meaning": "the law; custom",
        "source_ids": {"easton": "dothan", "smith": "dothan", "isbe": "dothan"},
        "key_refs": ["Genesis 37:17", "2 Kings 6:13", "2 Kings 6:17"],
        "sections": []
    },
    "dough": {
        "id": "dough",
        "term": "Dough",
        "category": "concepts",
        "intro": "<p>Dough in the ancient world was typically made from wheat or barley flour mixed with water, then leavened with a piece of fermented dough retained from a previous batch. The unleavened dough (<em>maṣṣôt</em>) that the Israelites carried out of Egypt in kneading troughs on their shoulders—without time for leavening—became the basis for the annual Feast of Unleavened Bread and the instruction to eat no leavened bread during the seven days of Passover (Exod. 12:34, 39). The absence of leaven in the Passover dough thus memorialized the urgency of the Exodus.</p><p>Hosea 7:8 uses the image of Ephraim as \"a cake not turned\"—half-raw dough on one side—as a vivid metaphor for a nation only half-committed in its allegiances and compromised by mixing with the nations. Numbers 15:17–21 required that the first portion of kneaded dough be presented to the LORD as a contribution, a principle Paul applies theologically in Romans 11:16: \"If the dough offered as firstfruits is holy, so is the whole lump.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dough", "isbe": "dough"},
        "key_refs": ["Exodus 12:34", "Exodus 12:39", "Hosea 7:8"],
        "sections": []
    },
    "dove": {
        "id": "dove",
        "term": "Dove",
        "category": "concepts",
        "intro": "<p>The dove is one of the most richly symbolic birds in the biblical tradition, associated with gentleness, purity, mourning, and peace. In Genesis 8, Noah sent a dove from the ark; its return with a fresh olive branch announced that the floodwaters were receding and the judgment was lifting—establishing the olive-bearing dove as a lasting symbol of peace and restoration. Doves were the sacrificial bird of the poor: the law prescribed a pair of turtledoves or pigeons for those who could not afford a lamb (Lev. 12:8; 14:22), the offering brought by Mary at Jesus's purification (Luke 2:24). In the Song of Solomon, the dove is a recurring term of endearment and a figure of beauty and intimacy.</p><p>The Spirit descended \"like a dove\" at Jesus's baptism in all four Gospels (Matt. 3:16; Mark 1:10; Luke 3:22; John 1:32)—the most theologically significant dove imagery in the New Testament, connecting the Spirit's visible presence to the gentleness and peace the dove embodies. Jesus instructed his disciples to be \"wise as serpents and innocent as doves\" (Matt. 10:16). Dove merchants at the Jerusalem temple are among those Jesus drove out at the cleansing (John 2:16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dove", "smith": "dove", "isbe": "dove"},
        "key_refs": ["Genesis 8:11", "Leviticus 12:8", "Matthew 3:16", "John 2:16"],
        "sections": []
    },
    "doves-dung": {
        "id": "doves-dung",
        "term": "Dove's dung",
        "category": "concepts",
        "intro": "<p>Dove's dung appears in 2 Kings 6:25 in the account of the Aramean siege of Samaria, which produced a famine so severe that \"a donkey's head was sold for eighty shekels of silver, and the fourth part of a kab of dove's dung for five shekels.\" The phrase has generated scholarly debate over its interpretation: Easton presents two main views—(1) the phrase refers literally to dried bird excrement used as fuel for cooking, a practice attested in the ancient Near East and known from travelers' accounts; or (2) it designates a plant known as \"dove's dung,\" possibly a bulbous plant (<em>Ornithogalum umbellatum</em>, Star of Bethlehem) whose bulbs were eaten as food in times of scarcity.</p><p>Smith and the ISBE lean toward the literal interpretation, noting that under conditions of extreme siege-starvation, even excrement used as cooking fuel could command a price. Both interpretations agree on the underlying point: the siege had reduced Samaria to consuming substances utterly unsuited for human use, illustrating the completeness of the siege's desperation before God's miraculous intervention.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "doves-dung", "smith": "doves-dung"},
        "key_refs": ["2 Kings 6:25"],
        "sections": []
    },
    "dowry": {
        "id": "dowry",
        "term": "Dowry",
        "category": "concepts",
        "intro": "<p>The dowry (Hebrew <em>môhar</em>, more precisely the <em>bride-price</em>) in the biblical world was a payment made by the prospective groom or his family to the bride's father as part of the marriage transaction—distinct from the personal property a bride brought into the marriage and from gifts given to the family. It functioned as compensation for the loss of the daughter's labor and as an economic component of the covenant established between the two families. Exodus 22:17 prescribes the standard bride-price for a seduced virgin as the legal rate, even if the father refuses the marriage.</p><p>Jacob's fourteen years of labor for Laban constituted a bride-price paid in service rather than money (Gen. 29:18–20). Shechem offered any price as môhar and gift to secure Dinah (Gen. 34:12). The most unusual example is Saul's demand that David bring a hundred Philistine foreskins as his bride-price for Michal (1 Sam. 18:25)—a demand designed to result in David's death. The practice reflects the legal and economic framework within which marriage was arranged in ancient Israelite society.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dowry", "smith": "dowry", "isbe": "dowry"},
        "key_refs": ["Genesis 34:12", "Exodus 22:17", "1 Samuel 18:25"],
        "sections": []
    },
    "dragon": {
        "id": "dragon",
        "term": "Dragon",
        "category": "concepts",
        "intro": "<p>Dragon in the Old Testament translates two distinct Hebrew words: <em>tannîn</em> (a large serpent, sea creature, or chaos-monster) and <em>tan</em>/<em>tannîm</em> (a term often designating jackals or desert creatures, though the distinction is not always consistent). In poetic and prophetic usage, <em>tannîn</em> typically represents the primeval sea-monster of chaos that God conquered in creation (Ps. 74:13; 89:10; Isa. 51:9)—a mythological imagery adapted from ancient Near Eastern cosmogony. Egypt is symbolized as the great dragon lying in the Nile (Isa. 51:9; Ezek. 29:3), and Babylon similarly (Jer. 51:34).</p><p>In the New Testament, Revelation uses <em>drakōn</em> (dragon) exclusively as a designation for Satan in his cosmic opposition to God and the church (Rev. 12:3–4; 13:2, 4; 20:2). He is identified as \"that ancient serpent, who is called the devil and Satan\" (Rev. 12:9; 20:2)—explicitly connecting the apocalyptic dragon to the serpent of Genesis 3. This typological connection traces a unified biblical narrative of the evil power that opposes God's purposes, from the garden through the exile to the eschatological judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dragon", "isbe": "dragon"},
        "key_refs": ["Psalms 74:13", "Isaiah 51:9", "Revelation 12:9", "Revelation 20:2"],
        "sections": []
    },
    "dragon-well": {
        "id": "dragon-well",
        "term": "Dragon well",
        "category": "places",
        "intro": "<p>Dragon Well (also called the Jackal Well or Fountain of the Dragon) was a spring or pool in the vicinity of Jerusalem mentioned in Nehemiah 2:13 as a landmark along the route of Nehemiah's nocturnal inspection of Jerusalem's broken walls. The text records that he rode \"by night by the Valley Gate to the Dragon Well and to the Dung Gate, examining the walls of Jerusalem that were broken down and its gates that had been destroyed by fire.\"</p><p>The site's precise identification is uncertain. Some scholars propose En-rogel in the Kidron Valley near the junction with the Hinnom Valley; the ISBE suggests the possibility of its identification with the Pool of Gihon (though this is unlikely given Gihon's different position). The name may derive from a serpent or dragon motif associated with the water source, which is unrecorded in the text. Its function in the narrative is purely topographic, helping orient the reader to Nehemiah's route around the southern portion of the ancient city.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dragon-well", "isbe": "dragon-well"},
        "key_refs": ["Nehemiah 2:13"],
        "sections": []
    },
    "dram": {
        "id": "dram",
        "term": "Dram",
        "category": "concepts",
        "intro": "<p>Dram in the KJV translates the Hebrew <em>ʾadarkōn</em> or <em>darkᵉmôn</em>, both referring to the <em>daric</em>—the gold coin of the Persian Empire named after King Darius I. The daric was a high-quality gold coin weighing approximately 8.4 grams (about a third of a troy ounce), bearing the image of the Persian king in a running or kneeling position with a bow and spear. It was the standard gold coinage of the Achaemenid period and widely circulated throughout the Persian world.</p><p>The daric appears in the Old Testament in the context of offerings for temple construction: 1 Chronicles 29:7 records the leaders' contributions in gold darics; Ezra 2:69 and Nehemiah 7:70–72 document daric contributions to the post-exilic temple rebuilding fund; and Ezra 8:27 specifies gold bowls worth a thousand darics among the vessels returned to Jerusalem. Their appearance confirms the post-exilic dating of these texts and illustrates the integration of Persian-era monetary practices into the life of the restored Judean community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dram", "smith": "dram", "isbe": "dram"},
        "key_refs": ["1 Chronicles 29:7", "Ezra 2:69", "Ezra 8:27", "Nehemiah 7:70"],
        "sections": []
    },
    "draught-house": {
        "id": "draught-house",
        "term": "Draught-house",
        "category": "concepts",
        "intro": "<p>Draught-house (a privy or latrine) appears in 2 Kings 10:27, where Jehu ordered the temple of Baal at Samaria to be demolished after executing its worshippers, and the building converted into a draught-house—a public latrine. This act represented a supreme form of ritual desecration, permanently defiling the former sacred site and rendering it physically contemptible. Jehu's program of destroying Baal worship included both judicial execution of Baal's prophets and priests and this symbolic humiliation of the worship space itself.</p><p>In Matthew 15:17 and Mark 7:19, Jesus uses the same concept (translated \"draught\" or \"sewer\") in his teaching on defilement: whatever enters the mouth passes through the stomach and is expelled into the latrine, demonstrating that food cannot make a person spiritually unclean—and thus implicitly declaring all foods clean. The contrast between what passes through the body and what proceeds from the heart defines true defilement.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "draught-house"},
        "key_refs": ["2 Kings 10:27", "Matthew 15:17"],
        "sections": []
    },
    "drawer-of-water": {
        "id": "drawer-of-water",
        "term": "Drawer of water",
        "category": "concepts",
        "intro": "<p>Drawer of water was a menial occupation in ancient Israel, involving the daily labor of hauling water from wells, springs, or cisterns to supply households, animals, and building projects. In Deuteronomy 29:11, \"your woodcutters and your drawers of water\" are listed as the lowest social strata within the covenant community—those who performed the most servile physical labor yet were equally included in the covenant assembly and its obligations.</p><p>The most detailed biblical episode involving drawers of water concerns the Gibeonites (Josh. 9:21–27). Having deceived Joshua into a peace treaty, the Gibeonites were condemned to serve as woodcutters and drawers of water for the congregation and for the altar of the LORD in perpetuity—a status that paradoxically connected the deceiving outsiders permanently to the sanctuary service. Joshua's pronouncement established a hereditary role that some identify with the Nethinim, the temple servants mentioned in Ezra and Nehemiah as assigned to assist the Levites in temple work.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drawer-of-water", "isbe": "drawer-of-water"},
        "key_refs": ["Deuteronomy 29:11", "Joshua 9:21", "Joshua 9:27"],
        "sections": []
    },
    "dream": {
        "id": "dream",
        "term": "Dream",
        "category": "concepts",
        "intro": "<p>Dreams served throughout Scripture as a medium of divine revelation, though the prophetic tradition was careful to distinguish genuine God-given dreams from idle imagination and deceptive claims. In the patriarchal period, God communicated directly through dreams to Abimelech (Gen. 20:3), Laban (Gen. 31:24), Jacob (Gen. 28:12; 31:10), and Joseph (Gen. 37:5–9); Joseph also interpreted dreams for the cupbearer, the baker, and Pharaoh, whose dreams of seven cows and seven heads of grain revealed seven years of abundance followed by seven of famine (Gen. 41). Gideon was encouraged by a Midianite's dream of a barley loaf toppling a tent (Judg. 7:13–15). Solomon received his foundational commission in a dream at Gibeon (1 Kgs. 3:5).</p><p>The prophets drew a firm distinction between genuine revelation and the dreaming of false prophets (Jer. 23:25–28). In the New Testament, Joseph in Matthew's Gospel is guided repeatedly by angelic messages in dreams (Matt. 1:20; 2:12–13, 19, 22), and Pilate's wife urges clemency for Jesus based on her dream (Matt. 27:19). Joel 2:28, quoted by Peter at Pentecost (Acts 2:17), places dreams among the Spirit's gifts in the last days.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dream"},
        "key_refs": ["Genesis 28:12", "Genesis 41:1", "Judges 7:13", "Matthew 1:20"],
        "sections": []
    },
    "dredge": {
        "id": "dredge",
        "term": "Dredge",
        "category": "concepts",
        "intro": "<p>Dredge appears in the KJV of Job 24:6—\"They reap every one his corn in the field: and they gather the vintage of the wicked\"—where the Hebrew <em>bᵊlîlô</em> (literally \"mixed feed\" or \"fodder\") refers to the mixed grain or stubble gleaned from another's field. Modern translations render the term as \"fodder,\" \"mixed feed,\" or \"livestock grain.\" The verse describes the destitute poor forced to harvest leftover grain from the fields of the wicked—grain that is properly fodder for animals rather than food for people.</p><p>The ISBE cross-references this word under the entry for Corn. The context in Job 24 is a sustained lament over the social injustices that go unpunished: the poor are driven from their land, must glean fields that belong to others, and eat what animals eat, illustrating the depth of their oppression and the apparent indifference of divine justice—a tension at the heart of Job's dialogue with his friends.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dredge", "isbe": "dredge"},
        "key_refs": ["Job 24:6"],
        "sections": []
    },
    "dregs": {
        "id": "dregs",
        "term": "Dregs",
        "category": "concepts",
        "intro": "<p>Dregs (Hebrew <em>shᵊmārîm</em>, meaning <em>lees</em> or <em>sediment</em>) refers to the thick residue that settles at the bottom of wine vessels during fermentation and aging—the material strained off when wine is clarified. In biblical usage the dregs of a cup of wine became one of the most powerful and recurring images of divine judgment: Psalm 75:8 pictures the LORD holding a cup of foaming wine full of mixture, which all the wicked of the earth must drain to its dregs.</p><p>Isaiah 51:17 intensifies the image with Jerusalem as one who has drunk from the cup of God's wrath and drained \"the bowl of staggering, the dregs of the cup of staggering,\" staggering so that no one can help her up. Isaiah 51:22 then reverses the image as divine comfort: God will take the cup from her hand and pass it to her tormentors instead. This cup-of-wrath imagery—drained to the last drops of the dregs—recurs in the prophets and culminates in Revelation 14:10 and 16:19, where Babylon drinks the wine of God's wrath undiluted.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dregs", "isbe": "dregs"},
        "key_refs": ["Psalms 75:8", "Isaiah 51:17", "Isaiah 51:22"],
        "sections": []
    },
    "dress": {
        "id": "dress",
        "term": "Dress",
        "category": "concepts",
        "intro": "<p>Dress in ancient Israel encompassed garments that reflected social status, climate, religious law, and gender distinction. The earliest clothing in Scripture consists of fig-leaf coverings made by Adam and Eve (Gen. 3:7) and the animal-skin garments God provided them (Gen. 3:21). The primary fabrics were linen (from flax) and wool, with the Mosaic law explicitly prohibiting the weaving of the two together in a single garment (<em>shaʿatnez</em>, Deut. 22:11; Lev. 19:19). Basic dress for both sexes included an inner tunic (<em>kuttōnet</em>), an outer robe or mantle (<em>salmāh</em>), a girdle or belt, and sandals.</p><p>The high priest's vestments—described in detail in Exodus 28—were the most elaborate dress in Israel, including the ephod, breastplate, robe, tunic, turban, and sash, each with specific symbolic significance. In the New Testament, John the Baptist's garment of camel's hair and leather belt (Matt. 3:4) consciously echoed the dress of the prophet Elijah (2 Kgs. 1:8), marking him as a prophetic figure in that tradition. James 2:2–4 and Matthew 22:11–12 both show that dress communicated social status in ways the church had to navigate carefully.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dress", "smith": "dress", "isbe": "dress"},
        "key_refs": ["Genesis 3:21", "Deuteronomy 22:11", "Exodus 28:1", "Matthew 3:4"],
        "sections": []
    },
    "drink": {
        "id": "drink",
        "term": "Drink",
        "category": "concepts",
        "intro": "<p>The standard drinks of the ancient Hebrews included water, wine, grape juice, milk, and <em>shekar</em> (strong drink fermented from grain or fruit). Water was the basic necessity, drawn from wells, cisterns, and rivers. Wine (<em>yayin</em>) was the primary fermented beverage, produced from grapes and consumed at meals, religious feasts, and celebrations; it also served medicinal purposes (1 Tim. 5:23). Milk from cattle, sheep, and goats was a dietary staple, particularly in the patriarchal period. Beer or barley-based drinks may also have been consumed, though the specific term varies.</p><p>The theological dimensions of drink in Scripture extend from the water of the Exodus wilderness (Exod. 17:1–7) to Jesus's transformation of water into wine at Cana (John 2:1–11) and his declaration to the Samaritan woman of \"living water\" that springs up to eternal life (John 4:10–14). The cup of the Lord's Supper, using the fruit of the vine, became the primary drinking rite of the new covenant community (1 Cor. 11:25–26). The drink of judgment—the cup of God's wrath—runs alongside this as a sustained counterpoint throughout the prophets and Revelation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drink", "isbe": "drink"},
        "key_refs": ["Exodus 17:6", "John 4:10", "1 Corinthians 11:25"],
        "sections": []
    },
    "drink-strong": {
        "id": "drink-strong",
        "term": "Drink, strong",
        "category": "concepts",
        "intro": "<p>Strong drink (Hebrew <em>shēḵār</em>) was a fermented beverage distinct from wine (<em>yayin</em>), probably produced from barley, dates, pomegranates, or other fruits rather than grapes. The ISBE notes it was likely similar to beer in many contexts. Scripture consistently associates strong drink with the danger of intoxication and the loss of judgment. The Nazirite vow prohibited both wine and strong drink, and mothers of those vowed from birth were also to abstain (Judg. 13:4, 7, 14; Luke 1:15 for John the Baptist).</p><p>Isaiah condemns those who rise early in pursuit of strong drink (Isa. 5:11) and those who are \"heroes\" in drinking wine and valiant in mixing strong drink (Isa. 5:22). Proverbs 20:1 warns that \"strong drink is a brawler\" and that whoever is led astray by it is not wise. Yet Deuteronomy 14:26 permits the purchase of strong drink for consumption at the feast of tithes in Jerusalem—indicating that moderate use at appropriate occasions was not itself condemned. The distinction throughout Scripture is between moderate use and drunkenness, which is uniformly forbidden.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drink-strong", "smith": "drink-strong", "isbe": "drink-strong"},
        "key_refs": ["Judges 13:4", "Isaiah 5:11", "Proverbs 20:1", "Luke 1:15"],
        "sections": []
    },
    "drink-offering": {
        "id": "drink-offering",
        "term": "Drink-offering",
        "category": "concepts",
        "intro": "<p>The drink-offering (Hebrew <em>nesek</em>, <em>libation</em>) was a prescribed quantity of wine poured out at the altar in conjunction with animal sacrifices under the Mosaic system (Num. 15:5–10; Exod. 29:38–40). It accompanied the regular morning and evening burnt offerings, as well as additional offerings at the major festivals. The wine was poured as a liquid offering to the LORD—not consumed by the priests—making it one of the purest forms of offering in which the entire substance was given to God. The quantity varied by the animal offered: one-quarter hin for a lamb, one-third hin for a ram, and one-half hin for a bull.</p><p>Second Kings 16:13 records Ahaz offering a drink-offering on his new pagan altar, adapting the form of Israelite worship to syncretistic ends. Numbers 6:15–17 specifies drink-offerings as part of the Nazirite's completion offerings. Paul employs the drink-offering image metaphorically twice: in Philippians 2:17, he describes his potential martyrdom as being \"poured out as a drink-offering\" on the sacrifice of the Philippians' faith; in 2 Timothy 4:6, he says he is already \"being poured out as a drink-offering\" as his death approaches—self-offering completing a life of service.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drink-offering", "isbe": "drink-offering"},
        "key_refs": ["Numbers 15:5", "Exodus 29:40", "Philippians 2:17", "2 Timothy 4:6"],
        "sections": []
    },
    "dromedary": {
        "id": "dromedary",
        "term": "Dromedary",
        "category": "concepts",
        "intro": "<p>The dromedary (single-humped camel, <em>Camelus dromedarius</em>) was one of the most important animals in the ancient Near East, essential for long-distance caravan trade and transportation across desert routes connecting Arabia, Mesopotamia, and Egypt. Distinguished from the Bactrian (two-humped) camel by its single hump and superior adaptation to hot, arid climates, the dromedary could travel days without water and carry heavy loads across terrain impassable to wheeled vehicles.</p><p>Camels appear as a mark of patriarchal wealth from Abraham onward (Gen. 12:16; 24:10) and feature prominently in the account of Rebekah's journey to become Isaac's wife. Isaiah 60:6 envisions dromedaries from Midian and Ephah bringing gold and incense to the restored Zion. Jeremiah 2:23 compares faithless Israel to a swift young female camel—a <em>bikrāh</em>, a riding dromedary—darting restlessly across the landscape as a metaphor for Israel's frantic and erratic pursuit of foreign gods. The image captures the dromedary's speed and unpredictability in contrast to Israel's covenantal obligation of steadfast loyalty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dromedary", "smith": "dromedary", "isbe": "dromedary"},
        "key_refs": ["Isaiah 60:6", "Jeremiah 2:23", "Genesis 24:10"],
        "sections": []
    },
    "dropsy": {
        "id": "dropsy",
        "term": "Dropsy",
        "category": "concepts",
        "intro": "<p>Dropsy (Greek <em>hydrōpikos</em>, modern edema or hydrops) is an abnormal accumulation of fluid in the tissues or body cavities, causing swelling, and may be associated with liver disease, heart failure, or kidney disorders. It is mentioned only once in the New Testament, in Luke 14:2, where a man afflicted with it is present before Jesus at the home of a prominent Pharisee on the Sabbath.</p><p>Jesus healed the man before the assembled guests, then posed a counter-challenge to the lawyers and Pharisees: \"Which of you, having a son or an ox that has fallen into a well on a Sabbath day, will not immediately pull him out?\" Their silence in response to this comparison implicitly conceded the point. The healing and the subsequent teaching on humility and the proper guest list for banquets (Luke 14:7–14) form a unified Sabbath controversy narrative that characterizes Jesus's approach to the religious establishment throughout Luke's Gospel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dropsy", "isbe": "dropsy"},
        "key_refs": ["Luke 14:2"],
        "sections": []
    },
    "dross": {
        "id": "dross",
        "term": "Dross",
        "category": "concepts",
        "intro": "<p>Dross refers to the impurities and waste material separated from silver or other metals during the smelting and refining process—the slag and base elements that rise to the surface or are drawn off when heat is applied to ore. In Scripture, dross functions as a consistent metaphor for moral corruption and the worthless elements within a society or individual that divine judgment is designed to remove. Proverbs 25:4 states the principle: \"Take away the dross from the silver, and the smith has material for a vessel.\"</p><p>Isaiah 1:22 laments Jerusalem's condition: \"Your silver has become dross, your best wine mixed with water\"—describing a society corrupted at its core. Isaiah 1:25 then announces God's redemptive response: \"I will turn my hand against you and will smelt away your dross as with lye and remove all your alloy.\" Psalm 119:119 declares that God puts away \"all the wicked of the earth like dross.\" Ezekiel 22:18–22 develops the extended metaphor of Israel as dross in the furnace of Jerusalem, which God will heat to purify. Malachi 3:2–3 uses the refiner's fire and fuller's soap as images of the purifying work of the coming messenger.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dross", "isbe": "dross"},
        "key_refs": ["Proverbs 25:4", "Isaiah 1:22", "Isaiah 1:25", "Ezekiel 22:18"],
        "sections": []
    },
    "drought": {
        "id": "drought",
        "term": "Drought",
        "category": "concepts",
        "intro": "<p>Drought in Palestine was not merely a climatic event but was understood in the covenant framework as a consequence of faithlessness to the LORD. The Mosaic law explicitly listed the withholding of rain and the hardening of the skies \"like bronze\" among the covenant curses for disobedience (Deut. 28:23–24). The agricultural calendar depended on two rainy seasons: the early rain (<em>yôreh</em>, October–November) for plowing and planting, and the latter rain (<em>malqôsh</em>, March–April) for ripening the grain. Absence of either caused crop failure and famine.</p><p>Elijah's three-and-a-half-year drought under Ahab (1 Kgs. 17:1; James 5:17) was a direct challenge to Baal, the Canaanite storm-and-rain deity whose cult Ahab promoted—if Baal controlled the rain, the drought was a public demonstration of his impotence. Haggai 1:10–11 connects the post-exilic community's drought to their failure to rebuild the temple. Jeremiah 14 is a sustained lament over drought as divine judgment. Psalm 32:4 uses the image of a summer's drought to describe the spiritual desiccation of unconfessed sin.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drought", "isbe": "drought"},
        "key_refs": ["Deuteronomy 28:23", "1 Kings 17:1", "Haggai 1:11", "Psalms 32:4"],
        "sections": []
    },
    "drown": {
        "id": "drown",
        "term": "Drown",
        "category": "concepts",
        "intro": "<p>Drowning in Scripture appears both as an act of divine judgment celebrated in song and as a warning image in ethical teaching. Exodus 15:4–5 celebrates the drowning of Pharaoh's chariots and his army in the Red Sea—\"they sank into the depths like a stone\"—as the climax of Israel's deliverance, celebrated in the Song of Moses and Miriam. Amos 8:8 and 9:5 use the imagery of the land rising and sinking like the Nile to describe the judgment coming upon Israel. Hebrews 11:29 recalls that when Israel crossed the Red Sea on dry ground, the Egyptians who attempted the crossing \"were drowned.\"</p><p>In the New Testament, Jesus's warning in Matthew 18:6 about causing a child to stumble—\"it would be better for him to have a great millstone fastened around his neck and to be drowned in the depth of the sea\"—uses drowning as the image for a fate preferable to the judgment awaiting those who harm the innocent. The image also appears in 1 Timothy 6:9, where desire for wealth \"plunges people into ruin and destruction.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drown"},
        "key_refs": ["Exodus 15:4", "Hebrews 11:29", "Matthew 18:6"],
        "sections": []
    },
    "drunk": {
        "id": "drunk",
        "term": "Drunk",
        "category": "concepts",
        "intro": "<p>The first recorded instance of drunkenness in Scripture is Noah's intoxication after the flood (Gen. 9:21), an episode that led to the cursing of Canaan. The Old Testament consistently portrays drunkenness as a cause of shame, poor judgment, and moral failure: Lot's daughters made him drunk to commit incest (Gen. 19:32–35); Nabal's drunkenness on the night before his death preceded Abigail's intervention (1 Sam. 25:36–37); the prophets condemn the leaders of Israel and Judah as drunkards incapable of governing justly (Isa. 28:1–8). Proverbs 20:1 warns that strong drink is a brawler and that being led astray by it is folly.</p><p>The New Testament is equally clear: Romans 13:13 includes drunkenness in conduct incompatible with living in the light of the gospel; 1 Corinthians 6:10 places drunkards among those who will not inherit the kingdom of God; Galatians 5:21 lists drunkenness among the works of the flesh. Ephesians 5:18 draws the explicit contrast: \"Do not get drunk with wine, for that is debauchery, but be filled with the Spirit.\" Paul's rebuke of the Corinthians for drunkenness at the Lord's Supper (1 Cor. 11:21) shows how seriously the early church took this failure of conduct.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "drunk"},
        "key_refs": ["Genesis 9:21", "Ephesians 5:18", "1 Corinthians 6:10", "Proverbs 20:1"],
        "sections": []
    },
    "drusilla": {
        "id": "drusilla",
        "term": "Drusilla",
        "category": "people",
        "intro": "<p>Drusilla (meaning <em>watered by the dew</em>) was the youngest daughter of Herod Agrippa I and the Jewish wife of the Roman procurator Felix when Paul appeared before him at Caesarea (Acts 24:24). She was renowned in her time for her beauty. Felix, a freedman of low origin who had risen to the governorship of Judea through court connections, had persuaded her to leave her first husband, Aziz king of Emesa, to marry him—a union that Josephus notes as violating Jewish law and that would have been considered scandalous by observant Jews.</p><p>When Paul was brought before Felix and Drusilla and reasoned about righteousness, self-control, and the coming judgment, Felix was alarmed and dismissed him with the famous reply: \"Go away for now. When I get an opportunity I will summon you\" (Acts 24:25)—a postponement that Paul's subsequent detentions made permanent. The historian Josephus later records that Drusilla and her son by Felix perished in the eruption of Mount Vesuvius in AD 79.</p>",
        "hitchcock_meaning": "watered by the dew",
        "source_ids": {"easton": "drusilla", "smith": "drusilla", "isbe": "drusilla"},
        "key_refs": ["Acts 24:24", "Acts 24:25"],
        "sections": []
    },
    "duke": {
        "id": "duke",
        "term": "Duke",
        "category": "concepts",
        "intro": "<p>Duke in the KJV translates the Hebrew <em>ʾallûp</em> (literally <em>chief</em> or <em>clan-head</em>), used specifically of the chiefs or tribal leaders of Edom—the heads of the Edomite clans descended from Esau's sons (Gen. 36:15–43; Exod. 15:15; 1 Chr. 1:51–54). The term designates the heads of the constituent clans into which Edomite society was organized, each named after a territorial designation or ancestor. The word bears no connection to the English feudal title \"duke\" beyond the KJV's translation convention.</p><p>Modern translations consistently use \"chief,\" \"clan-chief,\" or \"chieftain\" to avoid the feudal English connotation. The ISBE notes that the Edomite social organization implied by these lists—with multiple simultaneous chiefs rather than a single king—represents either an earlier non-monarchic period of Edomite history or a parallel tribal organization existing alongside the royal line. Exodus 15:15's reference to the chiefs of Edom trembling at the news of Israel's Exodus confirms the political significance of these leaders in the ancient Near Eastern world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "duke", "isbe": "duke"},
        "key_refs": ["Genesis 36:15", "Exodus 15:15", "1 Chronicles 1:51"],
        "sections": []
    },
    "dulcimer": {
        "id": "dulcimer",
        "term": "Dulcimer",
        "category": "concepts",
        "intro": "<p>Dulcimer (Aramaic <em>sumpônyāh</em>, from Greek <em>symphōnia</em>, meaning <em>sounding together</em>) appears in Daniel 3:5, 10, 15 as one of the instruments in Nebuchadnezzar's royal orchestra, playing at the signal to bow before his golden image on the plain of Dura. The exact instrument is disputed: the ISBE and many modern commentators translate it as <em>bagpipe</em>—two pipes played simultaneously that produce a consonant sound—consistent with the Greek etymology of \"sounding together.\" Smith treats it as a stringed instrument, and older English translations adopted the dulcimer convention from Renaissance usage.</p><p>Whatever the specific instrument, the <em>sumpônyāh</em> formed part of a full royal ensemble that included horn, pipe, lyre, trigon, harp, and all kinds of music—the complete sensory apparatus of royal ceremony. The orchestra's sound was the signal for mass prostration before the image; Shadrach, Meshach, and Abednego's refusal to bow, even knowing the penalty of the furnace, made the moment of music a test of ultimate loyalty between the kingdom of Babylon and the kingdom of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dulcimer", "smith": "dulcimer", "isbe": "dulcimer"},
        "key_refs": ["Daniel 3:5", "Daniel 3:15"],
        "sections": []
    },
    "dumah": {
        "id": "dumah",
        "term": "Dumah",
        "category": "people",
        "intro": "<p>Dumah (meaning <em>silence</em> or <em>rest</em>) was the fourth son of Ishmael and a grandson of Abraham by Hagar (Gen. 25:14; 1 Chr. 1:30), giving his name to an Arab tribe and the region they inhabited. Dumah is associated with the oasis of Dumat al-Jandal (modern Al-Jawf) in northwestern Saudi Arabia—known in Assyrian records as Adumatu—an important caravan hub in the northwestern Arabian desert. A separate town named Dumah also appears in the hill country of Judah (Josh. 15:52), an unrelated Judean settlement.</p><p>Isaiah 21:11 contains a cryptic oracle titled \"the burden of Dumah,\" addressed to a voice calling from Seir: \"Watchman, what time of the night? Watchman, what time of the night?\" The oracle's address to Seir (Edom) while titled \"Dumah\" has led to various interpretations—some treating Dumah as a punning reference to Edom (through the letters <em>d-m</em>), others identifying it as the Arabian Dumah facing Edom. The oracle's mood of uncertain watchfulness suits the name's meaning of silence and expectancy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dumah", "smith": "dumah", "isbe": "dumah"},
        "key_refs": ["Genesis 25:14", "Joshua 15:52", "Isaiah 21:11"],
        "sections": []
    },
    "dumb": {
        "id": "dumb",
        "term": "Dumb",
        "category": "concepts",
        "intro": "<p>Dumbness (muteness) in Scripture occurs both as a natural condition from birth or illness and as a specific miraculous sign. Exodus 4:11 establishes God as the creator of the mute and the deaf alongside those who see—affirming divine sovereignty over human physical limitations. Proverbs 31:8 calls on those with voice to \"speak up for those who cannot speak for themselves.\" The servant of the LORD is portrayed in Isaiah 53:7 as like a sheep before its shearers—\"silent\" (dumb) under suffering.</p><p>In the New Testament, Jesus healed numerous people who were mute: a demon-possessed man unable to speak (Matt. 9:32–33), a blind and mute man (Matt. 12:22; Luke 11:14). Zechariah, father of John the Baptist, was struck dumb by the angel Gabriel as a sign of his unbelief and could not speak until the naming of John (Luke 1:20–22, 64)—a dumbness that broke into both speech and praise at the moment of obedient naming. Jesus's own silence before Herod (Luke 23:9) is presented as a fulfillment of Isaiah 53:7.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dumb", "isbe": "dumb"},
        "key_refs": ["Exodus 4:11", "Proverbs 31:8", "Matthew 9:32", "Luke 1:20"],
        "sections": []
    },
    "dung": {
        "id": "dung",
        "term": "Dung",
        "category": "concepts",
        "intro": "<p>Dung in Scripture appears in both practical and symbolic contexts. As agricultural material, it was used to fertilize fig trees and gardens (Luke 13:8) and was collected outside city walls (Neh. 2:13). Sacrificial offerings were only partially burned on the altar; the hide, flesh, and dung of certain offerings were carried outside the camp and burned there (Exod. 29:14; Lev. 4:11; 8:17; Num. 19:5). The Epistle to the Hebrews (13:11–13) uses this regulation typologically: as the sacrificial bodies were burned outside the camp, so Jesus suffered outside the gate of Jerusalem to sanctify the people through his own blood.</p><p>Second Kings 6:25 records dove's dung selling at high prices during the Aramean siege of Samaria, illustrating extreme famine conditions. Paul employs the Greek term <em>skybala</em>—refuse, rubbish, or dung—in Philippians 3:8 to characterize his former religious credentials (circumcision, Pharisaic standing, blamelessness under the law) compared to the surpassing worth of knowing Christ Jesus: \"I count them as rubbish, in order that I may gain Christ.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dung", "smith": "dung"},
        "key_refs": ["Leviticus 4:11", "2 Kings 6:25", "Hebrews 13:11", "Philippians 3:8"],
        "sections": []
    },
    "dung-gate": {
        "id": "dung-gate",
        "term": "Dung-gate",
        "category": "places",
        "intro": "<p>The Dung Gate (Hebrew <em>shaʿar hāʾashpōt</em>, literally <em>the gate of the refuse heap</em>) was one of the gates of ancient Jerusalem, situated on the south wall of the city near the Valley of Hinnom. It is mentioned in Nehemiah 2:13 as one of the landmarks in Nehemiah's nighttime inspection of the broken walls, and was assigned as a section of the wall to be rebuilt under the supervision of Malchijah son of Rechab, ruler of Beth-hakkerem (Neh. 3:14). Nehemiah 12:31 includes it in the procession route at the dedication of the rebuilt walls.</p><p>The gate served as the exit through which refuse and waste were carried out of the city into the Hinnom Valley, giving it both its name and its function as the city's sanitation outlet. The Hinnom Valley below it was the city's refuse dump and the location of the infamous Topheth, associated with child sacrifice under apostate Israelite kings. The modern Dung Gate on the south side of the Old City of Jerusalem, leading to the Western Wall plaza, is near the location of the ancient gate.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dung-gate"},
        "key_refs": ["Nehemiah 2:13", "Nehemiah 3:14", "Nehemiah 12:31"],
        "sections": []
    },
    "dung-hill": {
        "id": "dung-hill",
        "term": "Dung-hill",
        "category": "concepts",
        "intro": "<p>Dung-hill in Scripture functions as a symbol of the lowest conceivable social condition, with the image of being raised from the dung-hill to sit with princes representing one of the most vivid reversals of fortune in biblical literature. First Samuel 2:8 and Psalm 113:7 share identical language: \"He raises the poor from the dust; he lifts the needy from the ash heap [dung-hill], to make them sit with princes\"—a divine reversal celebrated by Hannah in her song and by the psalmist as characteristic of God's justice. Mary's Magnificat (Luke 1:52) echoes this tradition of divine reversal.</p><p>Lamentations 4:5 uses the same image in mourning the fall of Jerusalem: those who once ate delicate food \"are desolate in the streets; those who were brought up in purple embrace ash heaps [dung-hills]\"—inverting the image for judgment. In the Aramaic sections of Daniel, the destruction of a lawbreaker's house to become \"a dung-hill\" (Dan. 2:5; 3:29 KJV; modern translations: \"a heap of ruins\") represents the most severe social degradation as legal penalty in the royal court of Babylon.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dung-hill"},
        "key_refs": ["1 Samuel 2:8", "Psalms 113:7", "Lamentations 4:5"],
        "sections": []
    },
    "dungeon": {
        "id": "dungeon",
        "term": "Dungeon",
        "category": "concepts",
        "intro": "<p>Dungeon designates a place of confinement more severe than an ordinary prison, characterized by darkness, restricted space, and extreme hardship. In the patriarchal narratives, Joseph was cast into an empty cistern (literally \"the pit\") by his brothers and later confined in Pharaoh's prison (Gen. 39:20; 40:3; 41:10; 42:19). Jeremiah was lowered by ropes into a muddy cistern-dungeon where he sank in the mire, rescued only through the intercession of the Ethiopian court official Ebed-melech (Jer. 38:6–13)—one of Scripture's most vivid accounts of political imprisonment.</p><p>The \"inner prison\" of Acts 16:24, where Paul and Silas were placed with their feet in stocks after flogging at Philippi, corresponds to the most secure section of the Roman prison—reserved for the most dangerous or condemned prisoners. The Psalms use dungeon imagery to describe extreme spiritual distress (Ps. 88:8; 142:7), and Isaiah 42:7 and 61:1 include release of prisoners from dungeons among the promises of the coming servant and the Spirit-anointed herald. These texts shaped Jesus's own programmatic announcement in Luke 4:18.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dungeon", "smith": "dungeon", "isbe": "dungeon"},
        "key_refs": ["Genesis 39:20", "Jeremiah 38:6", "Acts 16:24", "Isaiah 42:7"],
        "sections": []
    },
    "dura": {
        "id": "dura",
        "term": "Dura",
        "category": "places",
        "intro": "<p>Dura (meaning <em>a circle</em>, <em>walled place</em>, or <em>enclosure</em>—from the Akkadian <em>dūru</em>) was the plain near Babylon in the province of Babylon where Nebuchadnezzar erected a golden image ninety cubits high and six cubits wide and summoned all his officials, satraps, governors, and regional administrators to bow before it at the sound of the royal orchestra (Dan. 3:1). The episode of the three men—Shadrach, Meshach, and Abednego—who refused to bow and were cast into the furnace heated to extraordinary intensity became one of the most celebrated narratives of faith under imperial coercion in the entire Old Testament.</p><p>The exact location of the plain of Dura has not been definitively established; excavations near Hillah in Iraq have uncovered a large square brick structure (approximately fourteen meters on each side) that some archaeologists identify with the pedestal for the golden image, though certainty remains elusive. Multiple sites in Babylonia bore the name Dura, as the term was common in Akkadian topography. The Dura of Daniel is now generally located south of Babylon on the Euphrates plain.</p>",
        "hitchcock_meaning": "same as Dor",
        "source_ids": {"easton": "dura", "smith": "dura", "isbe": "dura"},
        "key_refs": ["Daniel 3:1"],
        "sections": []
    },
    "dust": {
        "id": "dust",
        "term": "Dust",
        "category": "concepts",
        "intro": "<p>Dust in Scripture carries multiple layers of meaning rooted in its role in the creation narrative. God formed Adam from the dust of the ground (<em>ʿāphār</em>) and breathed life into him (Gen. 2:7), and the curse pronounced at the Fall reversed this: \"You are dust, and to dust you shall return\" (Gen. 3:19). This establishes dust as the fundamental symbol of human mortality and creatureliness throughout the biblical tradition. Job expresses penitence by saying \"I abhor myself, and repent in dust and ashes\" (Job 42:6), and casting dust on the head was a standard gesture of grief and mourning in the ancient Near East (Josh. 7:6; Lam. 2:10).</p><p>Shaking dust from one's feet (Matt. 10:14; Acts 13:51) was a symbolic gesture of judgment and repudiation used by Jesus and later the apostles toward places that rejected their message—a practice adapted from the Jewish custom of shaking off Gentile dust before entering Israel. Daniel 12:2's promise that \"those who sleep in the dust of the earth shall awake\"—some to everlasting life, some to shame—is one of the clearest Old Testament affirmations of bodily resurrection. Revelation 18:19 uses throwing dust on the head as a mourning gesture over fallen Babylon.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dust", "smith": "dust", "isbe": "dust"},
        "key_refs": ["Genesis 2:7", "Genesis 3:19", "Matthew 10:14", "Daniel 12:2"],
        "sections": []
    },
    "dwarf": {
        "id": "dwarf",
        "term": "Dwarf",
        "category": "concepts",
        "intro": "<p>Dwarf appears once in the Levitical legislation (Lev. 21:20), in the list of physical blemishes that disqualified a descendant of Aaron from serving at the altar as a priest—though the same person could still eat of the priestly food and the most holy things. The Hebrew term (<em>daq</em>, meaning <em>thin</em> or <em>emaciated</em>) is variously understood by translators and commentators: it may designate dwarfism specifically, or more broadly a person who is wasted, underdeveloped, or too thin. Modern translations differ: \"dwarf\" (KJV, NIV), \"hunchback\" (ESV), or \"emaciated\" (NASB).</p><p>The underlying principle of the legislation was that priests serving at the altar before the LORD were to be physically whole, reflecting the holiness and perfection required in approaching the divine presence—a requirement extending also to the sacrificial animals (Lev. 22:17–25). The ISBE notes that the physical disqualification affected only the priest's service at the altar and involved no moral failing; the person retained full priestly status and provision, just not the privilege of officiating at worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dwarf", "isbe": "dwarf"},
        "key_refs": ["Leviticus 21:20"],
        "sections": []
    },
    "dwell": {
        "id": "dwell",
        "term": "Dwell",
        "category": "concepts",
        "intro": "<p>Dwell and its cognates carry significant theological weight in the biblical narrative, particularly in relation to God's presence among his people. The tabernacle (Hebrew <em>mishkān</em>, from the root <em>shākan</em>, \"to dwell\") was designed as the dwelling place of the LORD in Israel's midst (Exod. 25:8; 29:45–46), and God's command to build it is framed as the desire to dwell among his people. The promise \"I will dwell among you and be your God\" recurs as a covenant formula throughout the prophets (Lev. 26:11–12; Ezek. 37:27; Zech. 2:10–11).</p><p>In the New Testament, John 1:14's statement that the Word \"dwelt among us\" uses the same root (<em>skēnoō</em>, \"to tabernacle\") to identify the Incarnation as the ultimate fulfillment of the dwelling-presence theology. The indwelling of the Spirit in the believer (John 14:17; 1 Cor. 3:16) and the mutual indwelling of believers in Christ and Christ in them (John 15:4–7; 1 John 4:13) represent the progressive realization of the covenant promise. Revelation 21:3 announces the eschatological completion: \"Behold, the dwelling place (<em>skēnē</em>) of God is with man. He will dwell with them.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dwell", "isbe": "dwell"},
        "key_refs": ["Exodus 25:8", "John 1:14", "1 Corinthians 3:16", "Revelation 21:3"],
        "sections": []
    },
    "dwellings": {
        "id": "dwellings",
        "term": "Dwellings",
        "category": "concepts",
        "intro": "<p>Dwellings in the ancient Near East ranged from the tents of nomadic and semi-nomadic peoples to the mudbrick and stone houses of settled agricultural communities. In Canaan and Israel, the standard domestic dwelling was constructed of sun-dried mudbrick on stone foundations, with a flat roof of timber beams covered with packed mud—a construction type attested archaeologically from the Early Bronze Age onward. Leviticus 14:40–45 prescribes detailed procedures for houses afflicted with spreading mildew or fungal growth, requiring removal of infected stones and replastering, or demolition in severe cases—evidence that stone-and-plaster construction was standard in Israelite settlements.</p><p>Ezekiel 13:10–12 uses the image of a wall poorly built and whitewashed—plastered over with untempered mortar to conceal its weakness—as a metaphor for false prophets who cover over the people's spiritual condition with superficial assurances of peace when there is no peace. The prophetic contrast between the sturdy house built on rock and the flimsy house built on sand (Matt. 7:24–27; Luke 6:47–49) uses domestic building as a metaphor for the foundation of one's life in relation to Jesus's teaching.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dwellings"},
        "key_refs": ["Leviticus 14:40", "Ezekiel 13:10", "Matthew 7:24"],
        "sections": []
    },
    "dye": {
        "id": "dye",
        "term": "Dye",
        "category": "concepts",
        "intro": "<p>Dye and dyeing, though not described in procedural detail in the Bible, are attested throughout the scriptural narrative through the colored fabrics that formed part of Israel's sacred and domestic life. The tabernacle curtains and priestly vestments required threads of blue (<em>tᵊḵēlet</em>), purple (<em>ʾargāmān</em>), and crimson/scarlet (<em>tôlāʿ shānî</em>)—all dyed materials produced by complex dyeing processes (Exod. 26:1; 28:5–6; 35:6). Blue was derived from the snail <em>Murex trunculus</em>; purple from the Murex shellfish (the celebrated Tyrian purple of antiquity); and crimson from the dried bodies of the coccus ilicis insect (kermes).</p><p>The association of purple with wealth and royalty appears throughout Scripture: Judges 8:26 notes the purple garments of Midianite kings; Proverbs 31:22 describes the capable wife's garments of purple; Luke 16:19 uses purple as the marker of the rich man's luxury. Acts 16:14 introduces Lydia of Thyatira as \"a seller of purple goods\"—a dealer in the luxury textile trade who was Paul's first convert in Europe and whose household became the nucleus of the Philippian church. Revelation 17:4 and 18:12–16 use purple as an emblem of Babylon's imperial wealth and excess.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "dye"},
        "key_refs": ["Exodus 26:1", "Acts 16:14", "Proverbs 31:22", "Revelation 17:4"],
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
    print(f'BP d2: Diana → Dye: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
