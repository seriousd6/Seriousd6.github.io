"""
BP Article Synthesis — c1: Cab → Census
Covers Easton entries: Cab through Census (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-c1.py
Run: python3 scripts/bp-c1.py
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
    "cab": {
        "id": "cab",
        "term": "Cab",
        "category": "concepts",
        "intro": "<p>Cab (also spelled <em>kab</em>) was a Hebrew unit of dry measure equal to one-sixth of a seah, or approximately two quarts. It appears only once in Scripture, in the account of the siege of Samaria by Ben-hadad of Syria, when famine conditions were so severe that a cab of dove's dung sold for five pieces of silver (2 Kings 6:25). The extreme price illustrated the desperation of the besieged population. The cab was among the smaller measures of the Hebrew system, which also included the omer, seah, ephah, and homer.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cab", "smith": "cab", "isbe": "cab"},
        "key_refs": ["2 Kings 6:25"],
        "sections": []
    },
    "cabins": {
        "id": "cabins",
        "term": "Cabins",
        "category": "concepts",
        "intro": "<p>The word <em>cabins</em> occurs once in the King James Version (Jeremiah 37:16), referring to the cells or vaulted chambers of the dungeon in which the prophet Jeremiah was imprisoned. The Hebrew term suggests a pit-dungeon subdivided into small enclosures. Jeremiah had been cast into this prison by those who accused him of deserting to the Babylonians during the siege of Jerusalem. He remained in these close quarters until Ebed-melech secured his transfer to the court of the prison at the king's command.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cabins"},
        "key_refs": ["Jeremiah 37:16"],
        "sections": []
    },
    "cabul": {
        "id": "cabul",
        "term": "Cabul",
        "category": "places",
        "intro": "<p>Cabul (meaning <em>displeasing</em> or <em>dirty</em>) is the name of two locations in the Old Testament. (1.) A town on the eastern border of the tribe of Asher (Joshua 19:27), identified with the modern village of Kabul in Galilee, about nine miles southeast of Acre. (2.) The name given by Hiram, king of Tyre, to the twenty cities of Galilee that Solomon ceded to him in partial payment for the cedar and cypress timber and gold used in constructing the temple and palace in Jerusalem (1 Kings 9:13; 2 Chronicles 8:2). Hiram found the cities displeasing and called the district Cabul, a name expressing his dissatisfaction with the gift.</p>",
        "hitchcock_meaning": "displeasing; dirty",
        "source_ids": {"easton": "cabul", "smith": "cabul", "isbe": "cabul"},
        "key_refs": ["Joshua 19:27", "1 Kings 9:13", "2 Chronicles 8:2"],
        "sections": []
    },
    "caesar": {
        "id": "caesar",
        "term": "Caesar",
        "category": "people",
        "intro": "<p>Caesar was a title assumed by the Roman emperors after Julius Caesar, used throughout the New Testament to designate the reigning emperor as the sovereign authority over Judaea without specifying individual proper names (John 19:15; Acts 17:7). The Jews were required to pay tribute to Caesar (Matthew 22:17), and Roman citizens held the right of appeal directly to his authority (Acts 25:11). The Caesars referenced in the New Testament include Augustus, under whom Jesus was born and who ordered the census bringing Joseph and Mary to Bethlehem (Luke 2:1); Tiberius, during whose reign John the Baptist and Jesus carried out their ministries (Luke 3:1); and Claudius and Nero, during whose reigns the apostolic church expanded across the empire. The famous pronouncement of Jesus, \"Render to Caesar the things that are Caesar's, and to God the things that are God's\" (Matthew 22:21), established the foundational Christian teaching on the relationship between civic and divine obligation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "caesar", "smith": "caesar", "isbe": "caesar"},
        "key_refs": ["John 19:15", "Acts 17:7", "Matthew 22:17", "Acts 25:11", "Luke 2:1"],
        "sections": []
    },
    "caesara-philippi": {
        "id": "caesara-philippi",
        "term": "Caesarea Philippi",
        "category": "places",
        "intro": "<p>Caesarea Philippi was a city in the extreme north of ancient Palestine, situated at the base of Mount Hermon near the principal source of the Jordan River. It was rebuilt and enlarged by Philip the tetrarch, son of Herod the Great, who renamed it Caesarea in honor of the Roman emperor and added <em>Philippi</em> (\"of Philip\") to distinguish it from Caesarea on the coast. It corresponds to the earlier site of Panias (Banias), a center of worship for the god Pan. The city is significant in the Gospels as the setting for Peter's great confession — \"You are the Christ, the Son of the living God\" — in response to which Jesus declared that on this rock he would build his church (Matthew 16:13–19; Mark 8:27–30).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "caesara-philippi"},
        "key_refs": ["Matthew 16:13", "Mark 8:27"],
        "sections": []
    },
    "caesarea": {
        "id": "caesarea",
        "term": "Caesarea",
        "category": "places",
        "intro": "<p>Caesarea (Maritima) was a major port city on the Mediterranean coast of Palestine, approximately seventy miles northwest of Jerusalem at the northern end of the plain of Sharon. Built by Herod the Great (c. 10 B.C.) on the site of the earlier Strato's Tower, it was named in honor of Caesar Augustus and served as the administrative capital of the Roman province of Judaea. Its deep-water harbor, called Sebastos, was among the largest artificial harbors in the ancient world. Caesarea figures prominently in the New Testament as the home of Cornelius, where Peter first preached the gospel to the Gentiles and the Holy Spirit fell upon them (Acts 10); as the base of Philip the evangelist (Acts 21:8); as the place of Paul's imprisonments before his appeal to Caesar (Acts 23:33; 24–26); and as the site where Herod Agrippa I was struck dead for accepting divine honors (Acts 12:19–23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "caesarea", "smith": "caesarea", "isbe": "caesarea"},
        "key_refs": ["Acts 10:1", "Acts 10:24", "Acts 24:27", "Acts 25:1"],
        "sections": []
    },
    "cage": {
        "id": "cage",
        "term": "Cage",
        "category": "concepts",
        "intro": "<p>A cage in Scripture refers to an enclosure for confining birds or, figuratively, a place of captivity and corruption. Jeremiah uses the image of a cage full of birds to describe the abundance of deceit among those who grow rich through treachery (Jeremiah 5:27). Amos uses a similar figure in describing a basket of summer fruit as a sign of Israel's ripeness for judgment (Amos 8:1–2). In Revelation 18:2, fallen Babylon is called \"a cage of every unclean and hateful bird,\" depicting the city as a gathering place of evil. The cage thus functions consistently in Scripture as a symbol of spiritual corruption, false prosperity, and divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cage", "smith": "cage", "isbe": "cage"},
        "key_refs": ["Jeremiah 5:27", "Amos 8:1", "Revelation 18:2"],
        "sections": []
    },
    "caiaphas": {
        "id": "caiaphas",
        "term": "Caiaphas",
        "category": "people",
        "intro": "<p>Caiaphas was the Jewish high priest from approximately A.D. 18 to 36, serving during the entire administration of the Roman prefect Pontius Pilate. He was the son-in-law of Annas, who had previously held the high priesthood and continued to exercise great influence (John 18:13). Caiaphas presided over the Sanhedrin's conspiracy to arrest Jesus and arranged for his trial and condemnation. His cynical counsel — \"it is expedient for us that one man should die for the people, and that the whole nation should not perish\" (John 11:49–50) — was interpreted by the evangelist as an unwitting prophecy of Christ's atoning death. He also appears in the early chapters of Acts, when he presided over proceedings against Peter and John (Acts 4:6). His tenure ended when he was deposed by the proconsul Vitellius around A.D. 36.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "caiaphas", "isbe": "caiaphas"},
        "key_refs": ["Luke 3:2", "Matthew 26:3", "Matthew 26:57", "John 11:49", "John 18:13"],
        "sections": []
    },
    "cain": {
        "id": "cain",
        "term": "Cain",
        "category": "people",
        "intro": "<p>Cain (meaning <em>possession</em> or <em>a spear</em>) was the first-born son of Adam and Eve (Genesis 4:1) and the first murderer in Scripture. A tiller of the ground, Cain brought an offering of the fruit of the soil to the Lord, which was rejected in contrast to the accepted offering of his brother Abel, a shepherd. In anger and jealousy, Cain slew Abel in the field — the first recorded act of fratricide (Genesis 4:8). God cursed Cain to be a fugitive and wanderer on the earth, though he placed a mark on Cain to prevent his own killing. Cain settled in the land of Nod, east of Eden, and founded a city. He is cited in the New Testament as a warning example: his deeds were evil while his brother's were righteous (1 John 3:12), and he is called \"of the evil one\" (Hebrews 11:4; Jude 11). The \"way of Cain\" became a proverbial phrase for willful disobedience and envy of the godly.</p>",
        "hitchcock_meaning": "possession, or possessed",
        "source_ids": {"easton": "cain", "smith": "cain", "isbe": "cain"},
        "key_refs": ["Genesis 4:1", "Genesis 4:8", "Hebrews 11:4", "1 John 3:12"],
        "sections": []
    },
    "cainan": {
        "id": "cainan",
        "term": "Cainan",
        "category": "people",
        "intro": "<p>Cainan (meaning <em>possessor</em> or <em>purchaser</em>) is the name of two men in Scripture. (1.) A son of Enosh and grandson of Seth, listed in the antediluvian genealogy of Genesis 5:9–14. He lived 910 years and was the father of Mahalaleel. He appears in Luke's genealogy of Jesus (Luke 3:37). (2.) A son of Arphaxad and grandson of Shem, listed in the Septuagint version of Genesis 10:24 and 11:12–13 and in Luke 3:36, though he is absent from the standard Hebrew (Masoretic) text of the genealogy. The inclusion of this second Cainan in Luke has generated significant discussion among textual scholars regarding the Septuagint tradition underlying Luke's genealogy.</p>",
        "hitchcock_meaning": "possessor; purchaser",
        "source_ids": {"easton": "cainan", "smith": "cainan", "isbe": "cainan"},
        "key_refs": ["Genesis 5:9", "1 Chronicles 1:2", "Luke 3:36"],
        "sections": []
    },
    "cake": {
        "id": "cake",
        "term": "Cake",
        "category": "concepts",
        "intro": "<p>Cake in the Old Testament refers to various forms of flatbread used both in everyday meals and in religious offerings. Unleavened cakes were a required component of the meal offering (Leviticus 2:4; Exodus 29:2), typically baked on a griddle or in a pan with oil, and accompanied sacrifices and cereal offerings in temple worship. Women baked cakes as offerings to the queen of heaven, a practice condemned by Jeremiah as idolatrous (Jeremiah 7:18; 44:19). Amnon pretended illness to have his half-sister Tamar prepare cakes for him (2 Samuel 13:8). The prophet Hosea compared Ephraim to \"a cake not turned\" (Hosea 7:8) — scorched on one side and raw on the other — as a vivid image of half-hearted spiritual commitment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cake", "isbe": "cake"},
        "key_refs": ["Exodus 29:2", "Leviticus 2:4", "Jeremiah 7:18"],
        "sections": []
    },
    "calah": {
        "id": "calah",
        "term": "Calah",
        "category": "places",
        "intro": "<p>Calah (meaning <em>favorable</em> or <em>opportunity</em>) was one of the great ancient cities of Assyria, founded or rebuilt by Nimrod according to Genesis 10:11–12, along with Nineveh, Rehoboth-Ir, and Resen. Calah was situated at the confluence of the Upper Zab and Tigris rivers, approximately twenty miles south of Nineveh. It served as the Assyrian capital during the ninth and eighth centuries B.C. under kings Ashurnasirpal II and Shalmaneser III, who built elaborate palaces there. Excavations at the site (modern Nimrud) have uncovered ivories, monuments, and an obelisk recording Jehu's tribute to Shalmaneser. It was eventually supplanted by Nineveh as the empire's capital.</p>",
        "hitchcock_meaning": "favorable; opportunity",
        "source_ids": {"easton": "calah", "smith": "calah", "isbe": "calah"},
        "key_refs": ["Genesis 10:11"],
        "sections": []
    },
    "calamus": {
        "id": "calamus",
        "term": "Calamus",
        "category": "concepts",
        "intro": "<p>Calamus (from the Greek <em>kalamos</em>, a reed) was an aromatic plant used in ancient Israel as one of the chief spices in the holy anointing oil prescribed by God to Moses (Exodus 30:23). It was also traded through the port of Tyre alongside cassia and cinnamon (Ezekiel 27:19) and is mentioned in the Song of Solomon (4:14) among the choicest fragrant plants of the garden. The prophet Isaiah refers to it as a costly import that Israel failed to bring as an offering to God (Isaiah 43:24). Calamus is generally identified with sweet cane or sweet flag (<em>Acorus calamus</em>), a marsh plant with a sweet-scented rhizome native to India and widely traded throughout the ancient Near East.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "calamus", "smith": "calamus", "isbe": "calamus"},
        "key_refs": ["Exodus 30:23", "Song of Solomon 4:14", "Ezekiel 27:19", "Isaiah 43:24"],
        "sections": []
    },
    "calcol": {
        "id": "calcol",
        "term": "Calcol",
        "category": "people",
        "intro": "<p>Calcol (meaning <em>nourishing</em> or <em>sustaining</em>) was a son of Zerah of the tribe of Judah and one of the four men of renowned wisdom against whom Solomon's superior wisdom was measured (1 Kings 4:31). He is listed as a son of Mahol in that passage, and identified with Chalcol in the genealogy of 1 Chronicles 2:6, where he appears among the five sons of Zerah. No narrative details are given about Calcol; his significance in Scripture is solely as a proverbial standard of wisdom surpassed by Solomon.</p>",
        "hitchcock_meaning": "nourishing",
        "source_ids": {"easton": "calcol", "smith": "calcol"},
        "key_refs": ["1 Chronicles 2:6", "1 Kings 4:31"],
        "sections": []
    },
    "caleb": {
        "id": "caleb",
        "term": "Caleb",
        "category": "people",
        "intro": "<p>Caleb (meaning <em>dog</em> or possibly <em>bold</em>) is the name of several men in the Old Testament, the most prominent being Caleb son of Jephunneh of the tribe of Judah. He was one of the twelve spies sent by Moses to scout the land of Canaan (Numbers 13:6), and together with Joshua he brought back a faithful report, urging the people to trust God and enter the land. Because of this wholehearted fidelity, Caleb was promised that he and Joshua alone of their generation would enter Canaan (Numbers 14:30). At the age of eighty-five, after the conquest, Caleb boldly requested and received Hebron as his inheritance, driving out the Anakim (Joshua 14:6–15; 15:13–14). His daughter Achsah, given in marriage to Othniel, also appears in the narrative. Caleb became a symbol of steadfast faith and courage in old age.</p>",
        "hitchcock_meaning": "a dog; a crow; a basket",
        "source_ids": {"easton": "caleb", "smith": "caleb", "isbe": "caleb"},
        "key_refs": ["Numbers 13:6", "Numbers 32:12", "Joshua 14:6", "Joshua 15:13"],
        "sections": []
    },
    "calf": {
        "id": "calf",
        "term": "Calf",
        "category": "concepts",
        "intro": "<p>Calves appear in Scripture in two distinct contexts: as sacrificial animals and as objects of idolatrous worship. As a sacrifice, the fatted calf represented festive abundance and honor — most memorably in the parable of the prodigal son, where the father orders the fatted calf slaughtered to celebrate his son's return (Luke 15:23). The calf also appears in the ratification of covenants, where Jeremiah condemns those who violated the covenant by passing between the parts of a calf (Jeremiah 34:18–19). The golden calf stands as the most notorious example of Israelite apostasy: Aaron fashioned one for the people while Moses was on Sinai receiving the law (Exodus 32), and Jeroboam I set up golden calves at Bethel and Dan as alternative worship sites after the division of the kingdom (1 Kings 12:28–29), a sin commemorated throughout the books of Kings as the foundational transgression of the northern kingdom.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "calf", "smith": "calf", "isbe": "calf"},
        "key_refs": ["1 Samuel 28:24", "Luke 15:23", "Jeremiah 34:18", "1 Kings 12:28"],
        "sections": []
    },
    "calkers": {
        "id": "calkers",
        "term": "Calkers",
        "category": "concepts",
        "intro": "<p>Calkers were craftsmen who filled and sealed the seams of ships to make them watertight. The word appears twice in Ezekiel's lament over Tyre (Ezekiel 27:9, 27), where the city's maritime greatness is described in elaborate detail. The calkers of Tyre were men of Gebal (Byblos), a Phoenician city renowned for its shipbuilding expertise. The image of calkers abandoning their posts is part of Ezekiel's portrait of Tyre's total commercial and maritime collapse at divine judgment. The term underscores the highly specialized and organized nature of ancient Phoenician shipbuilding.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "calkers"},
        "key_refs": ["Ezekiel 27:9", "Ezekiel 27:27"],
        "sections": []
    },
    "call": {
        "id": "call",
        "term": "Call",
        "category": "concepts",
        "intro": "<p>The act of calling upon the name of the Lord is presented in Scripture as the foundational expression of true religion and relationship with God. The practice of calling upon God's name began in the generation of Enosh (Genesis 4:26) and continues as a defining mark of the covenant people throughout both Testaments. Paul quotes Joel's promise — \"everyone who calls on the name of the Lord will be saved\" (Romans 10:13) — as the ground of universal gospel proclamation. The term also encompasses God's call to individuals for salvation, service, or prophetic mission, a sovereign initiative running through the narratives of Abraham, Moses, Samuel, Isaiah, and the apostles. The New Testament epistles frequently describe believers as those who are \"called\" (klētos), marking divine election and vocation as the bedrock of Christian identity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "call"},
        "key_refs": ["Genesis 4:26", "Acts 2:21", "Romans 10:12"],
        "sections": []
    },
    "calling": {
        "id": "calling",
        "term": "Calling",
        "category": "concepts",
        "intro": "<p>Calling in the New Testament refers both to God's sovereign summons to salvation and to the social station or vocation in which a believer is found when converted. Paul instructs each person to remain in the calling in which they were called (1 Corinthians 7:20), cautioning against the assumption that conversion requires a change of social position. The fuller sense of calling — the \"high calling of God in Christ Jesus\" (Philippians 3:14) — encompasses the entire life of discipleship and ultimate glorification. There is \"one hope of your calling\" binding all believers together (Ephesians 4:4), and Paul repeatedly urges believers to walk worthy of it (Colossians 1:10; 1 Thessalonians 2:12). The concept thus integrates divine initiative, present vocation, and eschatological destiny.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "calling", "isbe": "calling"},
        "key_refs": ["1 Corinthians 7:20", "Ephesians 4:4"],
        "sections": []
    },
    "calneh": {
        "id": "calneh",
        "term": "Calneh",
        "category": "places",
        "intro": "<p>Calneh (meaning <em>our consummation</em>) was one of the four cities in the land of Shinar founded by Nimrod, along with Babel, Erech, and Accad (Genesis 10:10). Its precise location is debated; some scholars identify it with the Babylonian city of Nippur, while others have proposed Kullani in northern Syria. The prophets Amos (6:2) and Isaiah (10:9) refer to Calneh (or Calno) as a notable city that fell to Assyrian power, used as a warning to the complacent in Zion. In Ezekiel 27:23 it appears among the trading partners of Tyre. The city's early mention in Genesis as part of the original Mesopotamian city-state complex places it among the oldest named urban centers in the biblical record.</p>",
        "hitchcock_meaning": "our consummation",
        "source_ids": {"easton": "calneh", "isbe": "calneh"},
        "key_refs": ["Genesis 10:10", "Amos 6:2", "Isaiah 10:9"],
        "sections": []
    },
    "calvary": {
        "id": "calvary",
        "term": "Calvary",
        "category": "places",
        "intro": "<p>Calvary is the Latin form (Calvaria) of the Greek Kranion, itself translating the Hebrew Gulgoleth, all meaning <em>skull</em>. The name occurs explicitly only in Luke 23:33 (KJV), while the other Gospels use the equivalent phrase \"the place of a skull\" (Matthew 27:33; Mark 15:22; John 19:17). It designates the site of the crucifixion of Jesus, located outside the walls of Jerusalem. The name likely derived from the skull-like appearance of the rocky elevation rather than from any association with burials. Two principal locations have been proposed: the Church of the Holy Sepulchre, identified as the site by Helena, mother of Constantine, in the fourth century, and Gordon's Calvary (Skull Hill), a rocky escarpment north of the Damascus Gate identified in the nineteenth century. The theological significance of the location as the place of Christ's atoning death transcends the geographical debate.</p>",
        "hitchcock_meaning": "the place of a skull",
        "source_ids": {"easton": "calvary", "smith": "calvary", "isbe": "calvary"},
        "key_refs": ["Luke 23:33", "Matthew 27:33", "Mark 15:22", "John 19:17"],
        "sections": []
    },
    "camel": {
        "id": "camel",
        "term": "Camel",
        "category": "concepts",
        "intro": "<p>The camel was the essential beast of burden and long-distance transport throughout the ancient Near East and figures prominently throughout Scripture from Genesis to Revelation. There are two domesticated species — the one-humped dromedary (<em>Camelus dromedarius</em>), native to Arabia and the most common in biblical narratives, and the two-humped Bactrian camel. Abraham possessed camels as part of his considerable wealth (Genesis 12:16; 24:10), and the camel caravan of Ishmaelites that carried Joseph to Egypt is among the earliest commercial references (Genesis 37:25). Camel caravans transported the Queen of Sheba's gifts and spices (1 Kings 10:2). Under Mosaic law camels were classified as unclean animals because they chew the cud but do not have split hooves (Leviticus 11:4). In the New Testament, John the Baptist wore a garment of camel's hair (Matthew 3:4), and Jesus used the proverbial image of a camel passing through the eye of a needle to illustrate the near-impossibility of the rich entering God's kingdom (Matthew 19:24).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "camel", "smith": "camel", "isbe": "camel"},
        "key_refs": ["Genesis 24:64", "Genesis 37:25", "Leviticus 11:4", "Matthew 19:24"],
        "sections": []
    },
    "camon": {
        "id": "camon",
        "term": "Camon",
        "category": "places",
        "intro": "<p>Camon (meaning <em>his resurrection</em>) was the burial place of Jair, the Gileadite judge who ruled Israel for twenty-two years and had thirty sons who rode on thirty donkeys (Judges 10:3–5). The location of Camon is uncertain; ancient tradition placed it in Gilead east of the Jordan, while some manuscripts and commentators identify it with Kammon in the region of Galilee or with Qamm near Irbid in modern Jordan. Beyond its mention as Jair's burial site, nothing further is recorded of the town.</p>",
        "hitchcock_meaning": "his resurrection",
        "source_ids": {"easton": "camon", "smith": "camon", "isbe": "camon"},
        "key_refs": ["Judges 10:5"],
        "sections": []
    },
    "camp": {
        "id": "camp",
        "term": "Camp",
        "category": "concepts",
        "intro": "<p>The camp of Israel in the wilderness was organized according to detailed divine instructions, reflecting both military order and theological significance. The tabernacle occupied the center, surrounded by the Levites who served as an encircling guard; beyond them the twelve tribes were arranged in four groups of three on the four compass points, each under its own standard (Numbers 1–2). The arrangement expressed the principle that Israel's life radiated outward from the dwelling place of God. Ritually unclean persons were required to remain outside the camp (Numbers 5:2–3; Deuteronomy 23:10), a regulation that made the camp itself a zone of holiness. The Epistle to the Hebrews exploits this imagery in calling believers to go \"outside the camp\" bearing Christ's reproach, since Jesus suffered outside the city gate (Hebrews 13:12–13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "camp", "smith": "camp", "isbe": "camp"},
        "key_refs": ["Numbers 2:3", "Numbers 1:53", "Deuteronomy 23:10", "Hebrews 13:12"],
        "sections": []
    },
    "camphire": {
        "id": "camphire",
        "term": "Camphire",
        "category": "concepts",
        "intro": "<p>Camphire (KJV rendering) refers to the henna plant (<em>Lawsonia inermis</em>), a shrub cultivated throughout Palestine, Egypt, and Syria bearing small, intensely fragrant white or yellowish flowers. The Hebrew word <em>kopher</em> is translated as \"henna blossoms\" in modern versions. The beloved in the Song of Solomon is compared to a cluster of camphire blossoms from the vineyards of En-gedi (Song of Solomon 1:14; 4:13), and henna is listed among the choicest plants of the garden. The dye derived from henna leaves was widely used in the ancient world for ornamentation, and the flowers were worn or kept for their rich fragrance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "camphire", "smith": "camphire", "isbe": "camphire"},
        "key_refs": ["Song of Solomon 1:14"],
        "sections": []
    },
    "cana": {
        "id": "cana",
        "term": "Cana",
        "category": "places",
        "intro": "<p>Cana (meaning <em>reedy</em> or <em>of the reeds</em>, from Hebrew <em>qaneh</em>) was a town of Galilee where Jesus performed his first recorded miracle, turning water into wine at a wedding feast (John 2:1–11). It is also mentioned as the place where Jesus healed the son of a royal official from a distance while at Cana, the boy being in Capernaum (John 4:46–54). Cana was the hometown of Nathanael (John 21:2). The precise location remains debated between Kefr Kenna (about four miles northeast of Nazareth) and Khirbet Qana (about nine miles north of Nazareth), with the latter having stronger archaeological support. Cana of Galilee is not mentioned in the Old Testament.</p>",
        "hitchcock_meaning": "zeal; jealousy; possession",
        "source_ids": {"easton": "cana", "smith": "cana"},
        "key_refs": ["John 2:1", "John 4:46", "John 21:2"],
        "sections": []
    },
    "canaan": {
        "id": "canaan",
        "term": "Canaan",
        "category": "places",
        "intro": "<p>Canaan designates both a grandson of Noah and the land that bore his name. As a person, Canaan was the fourth son of Ham and the object of Noah's curse following Ham's improper conduct toward his father (Genesis 9:20–27). His descendants — Sidon, Heth, the Jebusites, Amorites, Girgashites, Hivites, Arkites, Sinites, Arvadites, Zemarites, and Hamathites (Genesis 10:15–18) — occupied the land of Canaan before the Israelite conquest. As a land, Canaan originally referred to the Phoenician coastal plain and gradually expanded to designate the entire territory between the Jordan and the Mediterranean, bounded roughly from Dan in the north to Beersheba in the south. God promised this land to Abraham and his descendants (Genesis 17:8), and the entire Pentateuchal narrative of exodus and wilderness journey is oriented toward its possession as the fulfillment of that covenant promise.</p>",
        "hitchcock_meaning": "merchant; trader; or that humbles and subdues",
        "source_ids": {"easton": "canaan", "smith": "canaan"},
        "key_refs": ["Genesis 10:6", "Genesis 17:8", "Joshua 5:12"],
        "sections": []
    },
    "canaan-the-language-of": {
        "id": "canaan-the-language-of",
        "term": "Canaan, the Language of",
        "category": "concepts",
        "intro": "<p>The phrase \"language of Canaan\" occurs once in Scripture, in Isaiah 19:18, in the context of a prophecy that five cities in Egypt will speak the language of Canaan and swear allegiance to the Lord of Hosts. The language of Canaan refers to Hebrew — the Semitic language shared by the Israelites and the original Canaanite inhabitants of the land — which was the language of the divine covenant and worship. The prophecy envisions a future in which Egypt, Israel's ancient oppressor, will be drawn into the worship of Israel's God and speak his people's sacred tongue. This is among the most remarkable universalistic prophecies in the Old Testament, anticipating the spiritual transformation of a pagan nation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "canaan-the-language-of"},
        "key_refs": ["Isaiah 19:18"],
        "sections": []
    },
    "canaanite": {
        "id": "canaanite",
        "term": "Canaanite",
        "category": "people",
        "intro": "<p>Canaanite in the Gospels designates Simon, one of the twelve apostles, called Simon the Canaanite (Matthew 10:4; Mark 3:18) to distinguish him from Simon Peter. The term does not indicate Canaanite ethnic origin but is a transliteration of the Aramaic <em>qan'ana</em>, meaning <em>zealot</em> — the same epithet rendered as \"the Zealot\" in Luke 6:15 and Acts 1:13. Simon may have been a member of the Zealot movement, a Jewish faction committed to armed resistance against Roman occupation, or the title may simply reflect personal zeal. Beyond his listing in the apostolic roll calls, no further narrative about him survives in the New Testament.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "canaanite"},
        "key_refs": ["Matthew 10:4", "Mark 3:18", "Luke 6:15"],
        "sections": []
    },
    "canaanites": {
        "id": "canaanites",
        "term": "Canaanites",
        "category": "people",
        "intro": "<p>The Canaanites were the pre-Israelite inhabitants of the land of Canaan, descended from Canaan son of Ham (Genesis 10:6–20). The term encompasses numerous distinct peoples including the Hittites, Amorites, Perizzites, Hivites, and Jebusites, who together occupied the territory between the Jordan River and the Mediterranean Sea. God commanded the Israelites to dispossess and destroy these nations because of their moral and religious corruption, particularly their practice of child sacrifice and ritual prostitution in the worship of Baal and Asherah (Deuteronomy 7:1–5; Exodus 3:8). Israel's repeated failure to fully drive out the Canaanites, and their subsequent adoption of Canaanite religion, became the central explanation offered by the historical books for Israel's downfall and exile.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "canaanites"},
        "key_refs": ["Genesis 10:6", "Exodus 3:8", "Deuteronomy 7:1"],
        "sections": []
    },
    "candace": {
        "id": "candace",
        "term": "Candace",
        "category": "people",
        "intro": "<p>Candace was a dynastic title, not a personal name, borne by the queens of the ancient Nubian kingdom of Meroe (Kush), situated south of Egypt along the Nile. The sole biblical reference occurs in Acts 8:27, where a high-ranking court official — the treasurer — of \"Candace, queen of the Ethiopians\" is encountered by Philip the evangelist on the road from Jerusalem to Gaza. This eunuch had been to Jerusalem to worship and was reading Isaiah 53 in his chariot when Philip came alongside him, explained the passage as fulfilled in Jesus, and baptized him. The narrative is among the first explicit accounts of the gospel reaching sub-Saharan Africa and an important moment in the spread of Christianity to Gentiles.</p>",
        "hitchcock_meaning": "who possesses contrition",
        "source_ids": {"easton": "candace", "isbe": "candace"},
        "key_refs": ["Acts 8:27"],
        "sections": []
    },
    "candle": {
        "id": "candle",
        "term": "Candle",
        "category": "concepts",
        "intro": "<p>The word rendered <em>candle</em> in the King James Version consistently refers to an oil lamp rather than a wax candle, as candles were not used in ancient Israel. The Hebrew <em>ner</em> and Greek <em>lychnos</em> both denote a clay or metal lamp burning olive oil. Scripture uses the lamp as a rich symbol: God's word is a lamp to one's feet and a light to one's path (Psalm 119:105); the lamp of the wicked is said to be put out in judgment (Job 18:6; Proverbs 24:20); and a virtuous woman's lamp does not go out at night (Proverbs 31:18). Jesus used the lamp as an image of witness and judgment — a city on a hill cannot be hidden, nor is a lamp put under a basket (Matthew 5:14–15) — and of readiness, as in the parable of the ten virgins (Matthew 25:1–13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "candle"},
        "key_refs": ["Job 18:6", "Psalms 18:28", "Proverbs 20:27"],
        "sections": []
    },
    "candlestick": {
        "id": "candlestick",
        "term": "Candlestick",
        "category": "concepts",
        "intro": "<p>The candlestick (more accurately, the lamp-stand or <em>menorah</em>) was one of the most sacred furnishings of the Mosaic tabernacle and later the temple. God commanded Moses to make it of pure beaten gold: a central shaft from which six branches extended, three on each side, each branch terminating in an almond-blossom-shaped lamp cup (Exodus 25:31–40). Its seven lamps were kept burning continually by the priests, giving light in the Holy Place before the veil. The completed lamp-stand is depicted on the Arch of Titus in Rome, among the spoils removed from the Jerusalem temple by Roman forces in A.D. 70. In the prophetic vision of Zechariah a golden lamp-stand flanked by two olive trees represents the Spirit's supply of light to the covenant community (Zechariah 4:2–6). In the book of Revelation the seven golden lamp-stands symbolize the seven churches of Asia (Revelation 1:12, 20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "candlestick", "smith": "candlestick"},
        "key_refs": ["Exodus 25:31", "Exodus 37:17", "Zechariah 4:2", "Revelation 1:12"],
        "sections": []
    },
    "cane": {
        "id": "cane",
        "term": "Cane",
        "category": "concepts",
        "intro": "<p>Cane in Scripture refers to an aromatic reed (<em>qaneh</em> in Hebrew), likely a species of fragrant grass or reed imported from distant lands and used in the preparation of the sacred anointing oil and incense. Isaiah rebukes Israel for failing to bring sweet cane as an offering to God (Isaiah 43:24), and Jeremiah associates it with costly imports (Jeremiah 6:20). The same Hebrew word is used for the measuring rod or reed and for reeds along riverbeds (Job 40:21; Isaiah 19:6), but in the spice context it denotes the aromatic plant <em>Calamus aromaticus</em> or a related species. It was among the luxury imports that flowed through Tyre and the ancient Near Eastern trade networks.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cane", "smith": "cane", "isbe": "cane"},
        "key_refs": ["Isaiah 43:24", "Jeremiah 6:20"],
        "sections": []
    },
    "canker": {
        "id": "canker",
        "term": "Canker",
        "category": "concepts",
        "intro": "<p>The word <em>canker</em> in the KJV translates two different Greek terms. In 2 Timothy 2:17, Paul compares the spread of false teaching to gangrene (<em>gangraina</em>), warning that the heresy of Hymenaeus and Philetus — their claim that the resurrection had already occurred — would eat through the body of faith like spreading necrosis. In James 5:3, the word describes the rust or corrosion (<em>ios</em>) that will eat the flesh of the wealthy who have hoarded riches while defrauding workers, serving as a witness against them on the day of judgment. Both uses employ vivid physical imagery to describe the spiritually destructive effects of false doctrine and covetousness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "canker", "isbe": "canker"},
        "key_refs": ["2 Timothy 2:17", "James 5:3"],
        "sections": []
    },
    "cankerworm": {
        "id": "cankerworm",
        "term": "Cankerworm",
        "category": "concepts",
        "intro": "<p>The cankerworm (Hebrew <em>yeleq</em>) was one of several insects used in Scripture to describe devastating locust-like plagues. It appears alongside the locust, palmerworm, and caterpillar as agents of divine judgment upon crops and vegetation. Joel invokes the image of cankerworms and locusts stripping the land bare as a metaphor for the army of divine judgment (Joel 1:4; 2:25), while Nahum uses the cankerworm as a picture of the swarming, all-consuming Assyrian armies (Nahum 3:15–16). The precise identification of the insect species named in these passages remains debated by entomologists and biblical scholars, with some suggesting the cankerworm represents a particular stage in the locust's life cycle.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cankerworm", "smith": "cankerworm"},
        "key_refs": ["Joel 1:4", "Joel 2:25", "Nahum 3:15"],
        "sections": []
    },
    "canneh": {
        "id": "canneh",
        "term": "Canneh",
        "category": "places",
        "intro": "<p>Canneh was an ancient trading city mentioned in Ezekiel's lament over Tyre (Ezekiel 27:23) as one of several Mesopotamian or Arabian trading partners that supplied goods to the Phoenician port. It is listed alongside Haran, Eden, Asshur, and Chilmad as a source of merchandise. The precise identification of Canneh is uncertain; some scholars equate it with Calneh of Genesis 10:10, while others suggest it was a distinct city in the northern Euphrates region or in Arabia. Its mention in the context of Tyre's extensive trade network attests to the wide commercial reach of the ancient Phoenician economy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "canneh", "smith": "canneh", "isbe": "canneh"},
        "key_refs": ["Ezekiel 27:23"],
        "sections": []
    },
    "canon": {
        "id": "canon",
        "term": "Canon",
        "category": "concepts",
        "intro": "<p>Canon (from Hebrew and Greek <em>kanon</em>, a rod or reed used as a measuring rule) refers to the authoritative collection of writings recognized as Scripture — the standard of faith and practice for the people of God. Applied to the Bible, a book is canonical when the church has recognized it as bearing divine authority, distinguishing it from other religious literature. The Hebrew canon (the Old Testament, arranged in the tripartite division of Torah, Prophets, and Writings) was settled in its essentials by the first century A.D., though debate over certain books (Esther, Ecclesiastes, Song of Solomon) continued among Jewish scholars. The New Testament canon reached its present form through gradual consensus in the early church, with the letters of Athanasius in A.D. 367 providing the earliest complete list matching the current twenty-seven books. The primary criterion for canonicity was apostolic origin or connection, consistent with the regula fidei (rule of faith), and universal reception in the churches.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "canon"},
        "key_refs": [],
        "sections": []
    },
    "capernaum": {
        "id": "capernaum",
        "term": "Capernaum",
        "category": "places",
        "intro": "<p>Capernaum (meaning <em>village of Nahum</em> or <em>city of comfort</em>) was a fishing town on the northwest shore of the Sea of Galilee that became the center of Jesus's Galilean ministry. Not mentioned in the Old Testament, it first appears in the Gospels, where it is called Jesus's \"own city\" (Matthew 9:1) after his rejection at Nazareth. Many of Jesus's most significant miracles occurred there: the healing of the centurion's servant (Matthew 8:5–13), the healing of Peter's mother-in-law (Matthew 8:14–15), the healing of a paralytic lowered through the roof (Mark 2:1–12), and the exorcism in the synagogue (Mark 1:21–28). The town was also home to Matthew (Levi) the tax collector (Matthew 9:9). Despite these mighty works, its inhabitants remained impenitent, drawing from Jesus a severe condemnation — it would be brought down to Hades (Matthew 11:23). The probable site is Tell Hum on the northern shore of the lake, where excavations have revealed a synagogue and an octagonal church.</p>",
        "hitchcock_meaning": "the field of repentance; city of comfort",
        "source_ids": {"easton": "capernaum", "smith": "capernaum", "isbe": "capernaum"},
        "key_refs": ["Matthew 4:13", "Matthew 8:5", "Mark 1:21", "Matthew 11:23"],
        "sections": []
    },
    "caphtor": {
        "id": "caphtor",
        "term": "Caphtor",
        "category": "places",
        "intro": "<p>Caphtor was the original homeland of the Philistines, according to both Deuteronomy 2:23 and Amos 9:7, where God reminds Israel that he brought the Philistines from Caphtor just as he brought Israel from Egypt. Jeremiah 47:4 likewise refers to the Philistines as \"the remnant of the coastland of Caphtor.\" The identification of Caphtor is debated but most commonly understood as Crete or the Aegean island world, consistent with the archaeological evidence linking the Philistines (the \"Sea Peoples\") to an Aegean migration in the twelfth century B.C. Some scholars identify Caphtor with the Egyptian toponym <em>Keftiu</em>, which denoted the Aegean region. The Cherethites, associated with the Philistines, are also connected to Crete.</p>",
        "hitchcock_meaning": "a sphere, buckle, or hand",
        "source_ids": {"easton": "caphtor"},
        "key_refs": ["Deuteronomy 2:23", "Jeremiah 47:4", "Amos 9:7"],
        "sections": []
    },
    "cappadocia": {
        "id": "cappadocia",
        "term": "Cappadocia",
        "category": "places",
        "intro": "<p>Cappadocia was a large region of central Asia Minor (modern Turkey), characterized by its high plateau and volcanic landscape. It is mentioned twice in the New Testament: in Acts 2:9, Cappadocians are among the Jewish diaspora pilgrims present at Pentecost who heard the apostles speak in their own languages; and in 1 Peter 1:1, Peter addresses his first epistle to the \"elect exiles of the Dispersion\" scattered throughout Cappadocia and neighboring regions. The province came under Roman control in A.D. 17 when Tiberius made it a province after the death of its last king. Cappadocia later became a significant center of early Christian monasticism and produced influential church fathers including Basil the Great and Gregory of Nyssa.</p>",
        "hitchcock_meaning": "the same as Caphtor",
        "source_ids": {"easton": "cappadocia", "isbe": "cappadocia"},
        "key_refs": ["Acts 2:9", "1 Peter 1:1"],
        "sections": []
    },
    "captain": {
        "id": "captain",
        "term": "Captain",
        "category": "concepts",
        "intro": "<p>Captain in the Old Testament renders several Hebrew terms designating military or civic leaders of varying rank and responsibility. The <em>sar</em> (prince or commander) was a senior military officer commanding hundreds or thousands of troops (1 Samuel 22:2; 2 Samuel 23:19). Special note attaches to the \"captain of the host,\" the supreme military commander. In the New Testament the chief captain (<em>chiliarchos</em>, commander of a thousand) was the Roman military tribune; it was such an officer, Lysias, who rescued Paul from the Jerusalem mob (Acts 21:31–40) and later sent him to Caesarea. In Joshua 5:14–15, the mysterious \"commander of the army of the Lord\" encountered by Joshua near Jericho is generally interpreted as a Christophany or angelic warrior of divine rank.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "captain", "smith": "captain", "isbe": "captain"},
        "key_refs": ["1 Samuel 22:2", "2 Samuel 23:19", "Joshua 5:14"],
        "sections": []
    },
    "captive": {
        "id": "captive",
        "term": "Captive",
        "category": "concepts",
        "intro": "<p>Captives in the ancient Near East were the primary human spoil of warfare — defeated enemies who might be killed, enslaved, ransomed, or deported depending on the conqueror's policy. The practice of marching defeated peoples into exile was systematically employed by the Assyrians and Babylonians as a means of breaking national identity and preventing revolt (2 Kings 15:29; 24:14). In the law of Moses, Israelites were permitted to take female captives in war under specified conditions that protected their dignity (Deuteronomy 21:10–14). The New Testament transforms the imagery: Paul describes Christ as having \"led captivity captive\" at his ascension (Ephesians 4:8, citing Psalm 68:18), triumphantly leading the defeated powers as his own captives in a heavenly procession.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "captive", "smith": "captive", "isbe": "captive"},
        "key_refs": ["1 Kings 20:32", "Joshua 10:24", "Deuteronomy 21:10", "Ephesians 4:8"],
        "sections": []
    },
    "captivity": {
        "id": "captivity",
        "term": "Captivity",
        "category": "events",
        "intro": "<p>The captivity of Israel refers to two major deportations that ended the independent existence of the two Israelite kingdoms. The Assyrian captivity of the northern kingdom (Israel) occurred in stages: Tiglath-pileser III deported the Transjordanian tribes and Galilean population in 732 B.C. (2 Kings 15:29), and Shalmaneser V and Sargon II completed the deportation of Samaria's population in 722/721 B.C. (2 Kings 17:6), resettling the land with peoples from Babylon and other Assyrian territories. The Babylonian captivity of the southern kingdom (Judah) was carried out by Nebuchadnezzar in three phases: 605 B.C. (including Daniel), 597 B.C. (including Ezekiel and the young king Jehoiachin), and 586 B.C., when Jerusalem and the temple were destroyed and the bulk of the remaining population deported (2 Kings 25). The return from Babylonian exile, authorized by Cyrus of Persia in 538 B.C. (Ezra 1), fulfilled Jeremiah's prophecy of a seventy-year exile (Jeremiah 25:11) and is theologically interpreted as a second exodus.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "captivity", "isbe": "captivity"},
        "key_refs": ["2 Kings 15:29", "2 Kings 17:6", "2 Kings 25:11", "Ezra 1:1"],
        "sections": []
    },
    "carbuncle": {
        "id": "carbuncle",
        "term": "Carbuncle",
        "category": "concepts",
        "intro": "<p>Carbuncle in the King James Version renders Hebrew words (<em>bareqet</em> and <em>ekdach</em>) denoting brilliant, fiery-red gemstones. The carbuncle (<em>bareqet</em>, probably an emerald or green stone) was the third stone in the first row of the high priest's breastplate (Exodus 28:17; 39:10), inscribed with the name of one of the tribes of Israel. Ezekiel lists it among the precious stones adorning the king of Tyre in his primordial glory (Ezekiel 28:13). Isaiah uses the second term (<em>ekdach</em>) in his vision of the restored Jerusalem, whose gates would be made of sparkling jewels (Isaiah 54:12). The precise identification of these gemstones with modern mineral classifications remains uncertain due to inconsistencies in ancient and medieval translation traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carbuncle", "smith": "carbuncle", "isbe": "carbuncle"},
        "key_refs": ["Exodus 28:17", "Ezekiel 28:13", "Isaiah 54:12"],
        "sections": []
    },
    "carcase": {
        "id": "carcase",
        "term": "Carcase",
        "category": "concepts",
        "intro": "<p>A carcase (or carcass) in the Mosaic law designated the body of a dead animal and was a primary source of ritual impurity. Contact with the carcase of any unclean animal, or with the dead body of a clean animal that had not been properly slaughtered, rendered a person unclean until evening and required washing of clothes (Leviticus 11:39–40; Numbers 19:16). The strict regulations surrounding carcases served both hygienic and theological purposes, reinforcing the separation of the holy from the impure. The word is also used figuratively in Scripture to describe the slain bodies of the enemies of God's people (Isaiah 66:24) and as a sign of divine curse on those who violated the covenant (Haggai 2:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carcase"},
        "key_refs": ["Leviticus 11:39", "Numbers 19:16"],
        "sections": []
    },
    "carchemish": {
        "id": "carchemish",
        "term": "Carchemish",
        "category": "places",
        "intro": "<p>Carchemish (meaning <em>fortress of Chemosh</em>) was a strategically vital city on the west bank of the Euphrates River that commanded the most important crossing point of the river on the main route between Mesopotamia and the Mediterranean world. Identified with modern Jerablus (Jarabulus) on the Turkish-Syrian border, it served as the capital of a Neo-Hittite kingdom in the Iron Age. The city is mentioned in 2 Chronicles 35:20 as the destination of the Egyptian pharaoh Necho's northward campaign during which Josiah was killed at Megiddo. The Battle of Carchemish in 605 B.C. (Jeremiah 46:2) was a decisive engagement in which Nebuchadnezzar of Babylon shattered the Egyptian army and effectively ended Egyptian power in the Levant, establishing Babylonian supremacy over the ancient Near East and directly precipitating the events leading to the fall of Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carchemish", "smith": "carchemish", "isbe": "carchemish"},
        "key_refs": ["Jeremiah 46:2", "2 Chronicles 35:20"],
        "sections": []
    },
    "carmel": {
        "id": "carmel",
        "term": "Carmel",
        "category": "places",
        "intro": "<p>Carmel (meaning <em>garden</em>, <em>park</em>, or <em>fruitful field</em>) is most prominently a mountain range in northern Israel extending approximately twelve miles from the Jezreel Valley to the Mediterranean coast, reaching 1,728 feet at its highest eastern point. It formed the boundary between the tribal territories of Asher and Manasseh. The headland of Carmel jutting into the bay of Acre was renowned in antiquity as a sacred site. It is most famous as the scene of Elijah's great contest with the 450 prophets of Baal, when fire fell from heaven to consume the waterlogged altar of the Lord and the drought was broken (1 Kings 18). Elisha maintained a residence there (2 Kings 4:25; 2:25). The mountain's lush vegetation made it a symbol of fertility and beauty in Hebrew poetry (Song of Solomon 7:5; Isaiah 35:2). A separate Carmel was also a town in the southern hill country of Judah where Nabal lived and where Saul erected a monument after defeating the Amalekites (1 Samuel 15:12; 25:2).</p>",
        "hitchcock_meaning": "circumcised lamb; harvest; full of ears of corn",
        "source_ids": {"easton": "carmel", "smith": "carmel", "isbe": "carmel"},
        "key_refs": ["1 Kings 18:19", "2 Kings 4:25", "Song of Solomon 7:5"],
        "sections": []
    },
    "carmi": {
        "id": "carmi",
        "term": "Carmi",
        "category": "people",
        "intro": "<p>Carmi (meaning <em>my vineyard</em> or <em>lamb of the waters</em>) is the name of two men in the Old Testament. (1.) A son of Reuben and grandson of Jacob who came to Egypt with the family (Genesis 46:9; Exodus 6:14), and founder of the Carmite clan (Numbers 26:6). (2.) A descendant of Judah listed in the genealogy of 1 Chronicles 4:1, sometimes identified as a son of Zimri. Most significantly in terms of narrative, Carmi was the father of Achan, the man of the tribe of Judah who violated the ban on the spoils of Jericho by secretly taking a Babylonian garment, silver, and gold — an act that brought defeat at Ai and resulted in Achan's execution by stoning (Joshua 7:1–26).</p>",
        "hitchcock_meaning": "my vineyard; lamb of the waters",
        "source_ids": {"easton": "carmi", "smith": "carmi", "isbe": "carmi"},
        "key_refs": ["Genesis 46:9", "Joshua 7:1", "1 Chronicles 4:1"],
        "sections": []
    },
    "carnal": {
        "id": "carnal",
        "term": "Carnal",
        "category": "concepts",
        "intro": "<p>Carnal (from Latin <em>caro</em>, flesh) is the theological term used in the King James Version to translate the Greek <em>sarkikos</em> and <em>sarkinos</em>, both derived from <em>sarx</em> (flesh). In Paul's letters, the carnal mind or fleshly orientation is set in direct opposition to the spiritual: \"the carnal mind is enmity against God\" (Romans 8:7), incapable of submitting to God's law and producing death (Romans 8:6). Paul rebukes the Corinthians for carnal behavior manifested in their party divisions and jealousy (1 Corinthians 3:3–4). The distinction between carnal and spiritual is not simply physical versus immaterial, but rather an orientation toward self and sin as opposed to God and righteousness. Carnal things (<em>sarkika</em>) include earthly material provisions given in exchange for spiritual ministry (Romans 15:27; 1 Corinthians 9:11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carnal", "isbe": "carnal"},
        "key_refs": ["Romans 8:6", "Romans 8:7", "1 Corinthians 3:3"],
        "sections": []
    },
    "carpenter": {
        "id": "carpenter",
        "term": "Carpenter",
        "category": "concepts",
        "intro": "<p>Carpenter in the Old Testament (Hebrew <em>charash</em>) denotes a craftsman who worked not only in wood but also in stone, iron, and copper — the term broadly covering all who worked with tools to shape hard materials. David employed Phoenician carpenters, brought from Tyre, in building his palace (2 Samuel 5:11; 1 Chronicles 14:1). The tools of the carpenter included the hammer, chisel, saw, and line (Isaiah 44:13; 1 Samuel 13:19–20; Isaiah 10:15). Scripture's most significant carpenter reference concerns Jesus of Nazareth: the people of his hometown asked, \"Is not this the carpenter?\" (Mark 6:3), and elsewhere, \"Is not this the carpenter's son?\" (Matthew 13:55), connecting Jesus to the trade of Joseph. The New Testament identification of Jesus as a carpenter has been a subject of theological reflection on the incarnation and the dignity of manual labor.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carpenter", "smith": "carpenter", "isbe": "carpenter"},
        "key_refs": ["2 Samuel 5:11", "Mark 6:3", "Matthew 13:55"],
        "sections": []
    },
    "carriage": {
        "id": "carriage",
        "term": "Carriage",
        "category": "concepts",
        "intro": "<p>Carriage in the King James Version consistently refers to luggage, baggage, or equipment carried by travelers and soldiers, not to a wheeled vehicle. The Hebrew and Greek terms denote burdens or packed belongings: the Danites' cattle and goods (Judges 18:21), the heavy idols borne by weary animals in Isaiah's lament (Isaiah 46:1), David's provisions left with a keeper when he went to the battlefront (1 Samuel 17:22), and the military baggage train of an army (Isaiah 10:28; 1 Samuel 10:22). In Acts 21:15, Paul and his companions \"took up their carriages\" — meaning they packed their baggage — and went up to Jerusalem. The modern English meaning of a wheeled conveyance had not yet developed when the KJV was translated in 1611.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carriage", "smith": "carriage", "isbe": "carriage"},
        "key_refs": ["Judges 18:21", "Isaiah 46:1", "1 Samuel 17:22"],
        "sections": []
    },
    "cart": {
        "id": "cart",
        "term": "Cart",
        "category": "concepts",
        "intro": "<p>Carts in the ancient Near East were simple two-wheeled ox-drawn vehicles used for transporting heavy loads. The Hebrew <em>agalah</em> denotes this basic farm and transport cart. Jacob's sons received carts from Pharaoh to bring their father and families to Egypt (Genesis 45:19, 27). The Philistines placed the ark of the covenant on a new cart when returning it to Israel after the plague upon them (1 Samuel 6:7–14), a practice repeated when David's first attempt to bring the ark to Jerusalem ended in the death of Uzzah (2 Samuel 6:3–8). God's displeasure at this second instance arose because the law required the ark to be carried on the shoulders of the Levites (Numbers 7:9), not on a cart — a lesson in the importance of approaching God according to his prescribed manner.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cart", "smith": "cart", "isbe": "cart"},
        "key_refs": ["2 Samuel 6:3", "1 Samuel 6:7", "Genesis 45:19"],
        "sections": []
    },
    "carve": {
        "id": "carve",
        "term": "Carve",
        "category": "concepts",
        "intro": "<p>Carving in Scripture refers primarily to the skilled work of engraving and cutting wood, stone, or ivory for decorative or religious purposes. Bezalel and Oholiab were divinely equipped craftsmen called to carve wood and engrave stone and metal for the tabernacle furnishings (Exodus 31:5; 35:33). Solomon's temple featured extensive carved cedar panels, palm trees, cherubim, and open flowers overlaid with gold (1 Kings 6:18, 29, 35). The prophets consistently condemn the carving of idols as an absurd and spiritually ruinous practice — Isaiah in particular develops an extended satirical description of a craftsman cutting down a tree, using half for firewood and half to carve a god that he then worships (Isaiah 44:13–17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "carve"},
        "key_refs": ["Exodus 31:5", "1 Kings 6:18", "Isaiah 44:13"],
        "sections": []
    },
    "casement": {
        "id": "casement",
        "term": "Casement",
        "category": "concepts",
        "intro": "<p>A casement in Scripture refers to a latticed window or window-screen of interwoven woodwork, used in ancient Near Eastern architecture to provide light and ventilation while screening the interior from view. The word appears twice in the KJV. In Proverbs 7:6, the wise man's mother \"looked through the casement\" (or lattice) and observed the foolish young man being seduced by the adulteress — a narrative frame that gives the subsequent warning its dramatic vividness. In Judges 5:28, Sisera's mother \"looked out at a window\" (casement) watching and waiting for her son's return from battle, a scene of tragic dramatic irony given that Sisera had already been killed by Jael.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "casement", "isbe": "casement"},
        "key_refs": ["Proverbs 7:6", "Judges 5:28"],
        "sections": []
    },
    "casiphia": {
        "id": "casiphia",
        "term": "Casiphia",
        "category": "places",
        "intro": "<p>Casiphia (meaning <em>money</em> or <em>covetousness</em>, possibly related to silver) was a place in Babylonia to which Ezra sent messengers to recruit Levites and temple servants for the return to Jerusalem (Ezra 8:17). The site was home to a community of Levitical ministers under a leader named Iddo. The messengers succeeded in bringing to Ezra thirty-eight Levites and 220 Nethinim (temple servants) to assist with the worship at the restored temple. The precise location of Casiphia is unknown, but it was evidently an established Jewish settlement in the Babylonian exile community where Levitical traditions were maintained.</p>",
        "hitchcock_meaning": "money; covetousness",
        "source_ids": {"easton": "casiphia", "smith": "casiphia", "isbe": "casiphia"},
        "key_refs": ["Ezra 8:17"],
        "sections": []
    },
    "casluhim": {
        "id": "casluhim",
        "term": "Casluhim",
        "category": "people",
        "intro": "<p>Casluhim (meaning <em>hopes of life</em>) were a people descended from Mizraim (Egypt), son of Ham, listed among the nations of Genesis 10:13–14 and 1 Chronicles 1:12. The text notes that the Philistines came from the Casluhim, a statement that has generated considerable discussion since Deuteronomy 2:23 and Amos 9:7 identify Caphtor (likely Crete or the Aegean) as the Philistine homeland. The most common scholarly resolution is that the Casluhim and Caphtorim may have been related peoples among the Sea Peoples who migrated into Canaan, or that there was an editorial dislocation in the Genesis text. The Casluhim otherwise play no further role in biblical narrative.</p>",
        "hitchcock_meaning": "hopes of life",
        "source_ids": {"easton": "casluhim", "smith": "casluhim", "isbe": "casluhim"},
        "key_refs": ["Genesis 10:14", "1 Chronicles 1:12"],
        "sections": []
    },
    "cassia": {
        "id": "cassia",
        "term": "Cassia",
        "category": "concepts",
        "intro": "<p>Cassia was an aromatic spice derived from the bark of a tree related to cinnamon (<em>Cinnamomum cassia</em>), imported in antiquity from India and southeastern Asia via Arabian trade routes. In the Mosaic law it was one of the four chief ingredients of the sacred anointing oil (Exodus 30:24), along with myrrh, cinnamon, and calamus. Ezekiel mentions it as a trade commodity of Tyre, supplied from Uzal (Ezekiel 27:19). The Psalmist names it among the fragrant garments of the messianic king (Psalm 45:8). Cassia (Hebrew <em>qiddah</em>) was a costly luxury import throughout the ancient world, its aromatic properties making it valuable both for religious ritual and for personal use.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cassia", "smith": "cassia", "isbe": "cassia"},
        "key_refs": ["Exodus 30:24", "Ezekiel 27:19", "Psalms 45:8"],
        "sections": []
    },
    "castaway": {
        "id": "castaway",
        "term": "Castaway",
        "category": "concepts",
        "intro": "<p>Castaway translates the Greek <em>adokimos</em> (rejected, disqualified, or failing the test) in 1 Corinthians 9:27, where Paul employs the metaphor of an athletic contest to describe his rigorous self-discipline: \"I discipline my body and keep it under control, lest after preaching to others I myself should be disqualified.\" The term denotes one who fails to meet the required standard and is excluded from the prize — not necessarily implying final damnation, but the possibility of ministerial failure and loss of reward through moral self-indulgence. The same word is used in 2 Timothy 3:8 of those who are \"reprobate concerning the faith\" and in Hebrews 6:8 of land bearing thorns that is \"rejected\" and near to a curse. Paul's self-application of the term reflects his earnest concern for personal integrity matching his public proclamation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "castaway", "isbe": "castaway"},
        "key_refs": ["1 Corinthians 9:27"],
        "sections": []
    },
    "castle": {
        "id": "castle",
        "term": "Castle",
        "category": "concepts",
        "intro": "<p>Castle in Scripture translates several Hebrew and Greek terms referring to fortified towers, citadels, or enclosures. The fortress on the hill of Zion captured from the Jebusites by David became his stronghold and the foundation of his royal city (1 Chronicles 11:7). Levitical cities had designated towers or strongholds (<em>tirah</em>) as secure residences (1 Chronicles 6:54). Genesis 25:16 uses the same word for the camps or settlements of Ishmael's sons. In the New Testament, the most significant \"castle\" is the Antonia Fortress, the Roman garrison adjacent to the temple mount in Jerusalem, into which Paul was carried by soldiers rescuing him from the Jewish mob (Acts 21:34–37). It was from the stairs of this fortress that Paul addressed the crowd in Hebrew.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "castle", "smith": "castle", "isbe": "castle"},
        "key_refs": ["1 Chronicles 11:7", "Genesis 25:16", "Acts 21:34"],
        "sections": []
    },
    "castor-and-pollux": {
        "id": "castor-and-pollux",
        "term": "Castor and Pollux",
        "category": "concepts",
        "intro": "<p>Castor and Pollux (Greek <em>Dioskouroi</em>, sons of Zeus) were the divine twin brothers of Greek and Roman mythology, worshipped as patrons and protectors of sailors. Their image as a ship's figurehead appears in Acts 28:11, where Paul and his companions sailed from Malta to Rome aboard an Alexandrian grain ship called the Twin Brothers. The mention of their patron deities as the ship's badge reflects common Hellenistic maritime religious practice. The twins were also associated with the constellation Gemini and with the phenomenon of St. Elmo's fire (the electrical discharge seen on ships' masts during storms), which ancient sailors took as a favorable sign of their divine presence. The passage provides an incidental detail of authentic first-century seamanship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "castor-and-pollux", "smith": "castor-and-pollux", "isbe": "castor-and-pollux"},
        "key_refs": ["Acts 28:11"],
        "sections": []
    },
    "caterpillar": {
        "id": "caterpillar",
        "term": "Caterpillar",
        "category": "concepts",
        "intro": "<p>Caterpillar in the King James Version renders Hebrew words (<em>chasil</em> and <em>gazam</em>) denoting insects used as instruments of divine judgment on crops and agriculture. The caterpillar appears alongside the locust and palmerworm in lists of devastating plagues upon vegetation (1 Kings 8:37; 2 Chronicles 6:28; Psalm 78:46; Deuteronomy 28:38). Joel's description of a fourfold plague — locusts, cankerworms, caterpillars, and palmerworms — consuming Israel's crops (Joel 1:4; 2:25) is likely a poetic multiplication of locust imagery representing total agricultural devastation. Isaiah uses the caterpillar as a symbol of God's power to strip the earth as judgment (Isaiah 33:4). The precise species distinctions in these Hebrew terms remain uncertain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "caterpillar", "smith": "caterpillar", "isbe": "caterpillar"},
        "key_refs": ["1 Kings 8:37", "Psalms 78:46", "Joel 1:4"],
        "sections": []
    },
    "catholic-epistles": {
        "id": "catholic-epistles",
        "term": "Catholic Epistles",
        "category": "concepts",
        "intro": "<p>The Catholic (or General) Epistles are a group of seven New Testament letters — James, 1 and 2 Peter, 1, 2, and 3 John, and Jude — named <em>catholic</em> (universal) because they are addressed to the church at large rather than to specific congregations or individuals, as Paul's letters typically are. The designation appears in Eusebius and other early church writers. These letters cover a broad range of concerns: practical ethics and the relationship between faith and works (James); Christian conduct under persecution and Peter's apostolic testimony (1 Peter); warnings against false teaching (2 Peter; Jude); love, fellowship, and the incarnation (1–3 John). Their canonical acceptance varied in the early church — some were disputed before eventual universal recognition — and they continue to hold a significant place in both Eastern and Western Christian traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "catholic-epistles", "isbe": "catholic-epistles"},
        "key_refs": [],
        "sections": []
    },
    "cattle": {
        "id": "cattle",
        "term": "Cattle",
        "category": "concepts",
        "intro": "<p>Cattle in Scripture encompass the domesticated bovine animals (oxen, cows, and calves) that formed the backbone of ancient Israelite agricultural and sacrificial life. They were used for plowing, threshing, and transportation, and their ownership was a primary index of wealth (Job 1:3; Psalm 144:14). Under Mosaic law, oxen and other cattle were central to the sacrificial system: the burnt offering, sin offering, and peace offering all permitted or required cattle (Leviticus 1:2–5; Numbers 7). The commandment forbidding muzzling an ox while it treads out grain (Deuteronomy 25:4) was later applied by Paul to the right of ministers to receive material support (1 Corinthians 9:9; 1 Timothy 5:18). The Psalmist's declaration that the cattle on a thousand hills belong to God (Psalm 50:10) asserts divine ownership of all creation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cattle", "smith": "cattle", "isbe": "cattle"},
        "key_refs": ["Deuteronomy 8:13", "1 Samuel 11:5", "Psalms 50:10"],
        "sections": []
    },
    "caul": {
        "id": "caul",
        "term": "Caul",
        "category": "concepts",
        "intro": "<p>The caul in the Mosaic sacrificial system referred to the fatty membrane encasing the liver — specifically the lobe or appendage above the liver — which was required to be burned on the altar as part of various animal offerings, including the peace offering, burnt offering, and sin offering (Exodus 29:13, 22; Leviticus 3:4, 10, 15; 4:9; 7:4). The burning of fat portions was considered especially pleasing to God and was reserved exclusively for him; the Israelites were forbidden to eat the fat of sacrificial animals (Leviticus 3:17). The caul thus represented the consecrated portions of the sacrifice returned entirely to God, signifying complete devotion in worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "caul", "smith": "caul", "isbe": "caul"},
        "key_refs": ["Exodus 29:13", "Leviticus 3:4", "Leviticus 3:10"],
        "sections": []
    },
    "cauls": {
        "id": "cauls",
        "term": "Cauls",
        "category": "concepts",
        "intro": "<p>Cauls in Isaiah 3:18 (KJV) refers to a women's head ornament or hairnet, listed among the elaborate feminine accessories condemned by the prophet Isaiah as symbols of the pride and luxury of the women of Jerusalem. The Hebrew word (<em>shabisim</em>) denotes a kind of ornamental headband, possibly a net or lattice of gold or precious material worn around the head. Isaiah's extended catalog of feminine luxury items (Isaiah 3:18–24) sets up the contrast with the desolation that divine judgment will bring — fine ornaments replaced by baldness, rich garments by sackcloth, and beauty by branding.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cauls"},
        "key_refs": ["Isaiah 3:18"],
        "sections": []
    },
    "causeway": {
        "id": "causeway",
        "term": "Causeway",
        "category": "concepts",
        "intro": "<p>Causeway in Scripture (Hebrew <em>mesillah</em>, a raised way or highway) refers to a paved or elevated road built for processional or military purposes. The two references in 1 Chronicles 26:16, 18 describe the divisions of the temple gatekeepers stationed at the causeway of the ascent, a raised approach road to the temple on the south side. In 2 Chronicles 9:11, King Solomon used the algum timber from Lebanon to construct stairways (causeways) for the temple and palace and to make harps and lyres. The concept of the prepared highway or causeway is also used figuratively in Isaiah, where the return from exile is described as a \"way\" or highway prepared through the wilderness (Isaiah 40:3; 62:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "causeway"},
        "key_refs": ["1 Chronicles 26:16", "1 Chronicles 26:18", "2 Chronicles 9:11"],
        "sections": []
    },
    "cave": {
        "id": "cave",
        "term": "Cave",
        "category": "places",
        "intro": "<p>Caves are a prominent feature of the limestone geology of Palestine and figure significantly throughout biblical history as places of refuge, burial, and habitation. The first cave mentioned in Scripture shelters Lot and his daughters after the destruction of Sodom (Genesis 19:30). The cave of Machpelah, purchased by Abraham from Ephron the Hittite, became the patriarchal burial ground for Abraham, Sarah, Isaac, Rebekah, Leah, and Jacob (Genesis 23; 25:9; 49:31; 50:13). During Elijah's flight from Jezebel, he took refuge in a cave at Horeb where God met him with the still small voice (1 Kings 19:9). David used caves as hiding places from Saul — most notably the cave of Adullam (1 Samuel 22:1) and the cave at En-gedi where he spared Saul's life (1 Samuel 24:3). Jesus was buried in a hewn rock tomb, functionally a cave, from which he rose on the third day.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cave", "smith": "cave", "isbe": "cave"},
        "key_refs": ["Genesis 19:30", "Genesis 25:9", "1 Samuel 22:1", "1 Kings 19:9"],
        "sections": []
    },
    "cedar": {
        "id": "cedar",
        "term": "Cedar",
        "category": "concepts",
        "intro": "<p>The cedar of Lebanon (<em>Cedrus libani</em>) was the most prized timber of the ancient Near East — celebrated for its height, fragrance, durability, and beauty. It grew abundantly on the slopes of Mount Lebanon and was harvested primarily by Phoenician craftsmen. David received cedar logs from Hiram of Tyre for building his palace (2 Samuel 5:11; 1 Chronicles 14:1), and Solomon used enormous quantities of cedar in constructing the temple (1 Kings 5:6–10; 6:9–10, 15–20) — cedar paneling covered the interior stone walls, giving the temple its fragrant, richly textured sanctuary. In Psalm 92:12, the righteous are compared to the towering cedar; Ezekiel uses the great cedar as a figure for the Assyrian empire (Ezekiel 31:3–9) and as a symbol of restored Davidic kingship (Ezekiel 17:22–24). The cutting down of the cedars of Lebanon by Assyria and Babylon became a stock image of divine judgment on great empires (Isaiah 14:8; 2 Kings 19:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cedar", "smith": "cedar", "isbe": "cedar"},
        "key_refs": ["1 Kings 5:6", "Psalms 92:12", "Ezekiel 31:3"],
        "sections": []
    },
    "cedron": {
        "id": "cedron",
        "term": "Cedron",
        "category": "places",
        "intro": "<p>Cedron (also spelled Kidron) is the Greek form of the Hebrew Kidron, the name of the valley and brook running between Jerusalem and the Mount of Olives. The sole New Testament reference using this spelling is John 18:1, which notes that Jesus and his disciples crossed the brook Cedron on the night of his arrest in Gethsemane. The Kidron Valley was significant throughout Israel's history as the boundary of the holy city, a burial ground, and the channel of ritual purification. Solomon warned Shimei not to cross the brook Kidron on pain of death (1 Kings 2:37). Asa, Josiah, and Hezekiah burned idols and Asherah poles in the Kidron as part of their religious reforms (1 Kings 15:13; 2 Kings 23:4–12). Jesus's crossing of the Cedron the night of his betrayal subtly echoes David's flight from Absalom across the same valley (2 Samuel 15:23).</p>",
        "hitchcock_meaning": "black; sad",
        "source_ids": {"easton": "cedron", "smith": "cedron", "isbe": "cedron"},
        "key_refs": ["John 18:1"],
        "sections": []
    },
    "ceiling": {
        "id": "ceiling",
        "term": "Ceiling",
        "category": "concepts",
        "intro": "<p>Ceilings in ancient Israelite architecture were typically of cedar beams or planks, and their quality was a mark of wealth and royal ambition. Solomon's temple featured a cedar ceiling covering the interior (1 Kings 6:9, 15; 7:3), and the house of the forest of Lebanon had a ceiling of cedar laid on forty-five pillars (1 Kings 7:2–3). The interior of the temple's cedar ceiling was carved with gourds and flowers (1 Kings 6:18). Jeremiah condemned the king Jehoiakim for building himself a lavish house with a paneled cedar ceiling at a time of national crisis, contrasting his father Josiah's justice with his own pursuit of luxury (Jeremiah 22:14). The use of expensive cedar ceilings became a symbol of royal extravagance in the prophetic critique of unjust rulers.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ceiling", "smith": "ceiling"},
        "key_refs": ["1 Kings 6:9", "1 Kings 7:3", "Jeremiah 22:14"],
        "sections": []
    },
    "cellar": {
        "id": "cellar",
        "term": "Cellar",
        "category": "concepts",
        "intro": "<p>Cellars in the Old Testament referred to underground storage chambers for wine, oil, and provisions. David's administrative organization included officers over the cellars (storehouses) of wine and oil (1 Chronicles 27:27–28), reflecting a sophisticated system of royal supply management. The word in Joel 1:17 describes granary storage pits that lie empty and in ruin as a result of the locust plague — a vivid image of agricultural catastrophe. In 1 Kings 7:51, the treasuries of the temple (often translated as storerooms or cellars) held the dedicated silver and gold of David awaiting the temple's completion. These storage facilities were essential to the economic administration of both palace and temple.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cellar", "isbe": "cellar"},
        "key_refs": ["1 Chronicles 27:28"],
        "sections": []
    },
    "cenchrea": {
        "id": "cenchrea",
        "term": "Cenchrea",
        "category": "places",
        "intro": "<p>Cenchrea (meaning <em>millet</em> or <em>small pulse</em>) was the eastern port of Corinth, situated on the Saronic Gulf approximately seven miles southeast of the city. As one of Corinth's two harbors — the other being Lechaion on the Corinthian Gulf to the west — Cenchrea handled the eastern Mediterranean trade. It is mentioned twice in the New Testament: Paul had his head shaved at Cenchrea in fulfillment of a vow (Acts 18:18) before sailing to Syria at the end of his second missionary journey; and in Romans 16:1, Paul commends Phoebe, \"a servant of the church at Cenchrea,\" to the Roman congregation — an important reference for the history of women's ministry and the diaconate in the early church.</p>",
        "hitchcock_meaning": "millet; small pulse",
        "source_ids": {"easton": "cenchrea"},
        "key_refs": ["Acts 18:18", "Romans 16:1"],
        "sections": []
    },
    "censer": {
        "id": "censer",
        "term": "Censer",
        "category": "concepts",
        "intro": "<p>The censer was a vessel, typically of gold or bronze, used to carry burning coals on which incense was placed, producing the fragrant smoke that ascended before the Lord in tabernacle and temple worship. In the tabernacle ritual, the high priest filled the censer with coals from the bronze altar of burnt offering and carried it into the Holy of Holies on the Day of Atonement, placing incense upon the coals so that the cloud of smoke covered the mercy seat (Leviticus 16:12–13). Golden censers were among the temple furnishings described in 1 Kings 7:50. The episode of Korah, Dathan, and Abiram includes the dramatic test of two hundred fifty men each bringing a censer before the Lord, followed by divine fire consuming them when they presumed to offer unauthorized incense (Numbers 16:17–35). King Uzziah was struck with leprosy when he presumed to burn incense in the temple (2 Chronicles 26:19). In Revelation, golden censers full of incense represent the prayers of the saints before the throne of God (Revelation 5:8; 8:3–5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "censer", "smith": "censer", "isbe": "censer"},
        "key_refs": ["Leviticus 16:12", "Numbers 16:39", "2 Chronicles 26:19", "Revelation 8:3"],
        "sections": []
    },
    "census": {
        "id": "census",
        "term": "Census",
        "category": "events",
        "intro": "<p>A census in the Old Testament was a count of the male population, primarily for military assessment and taxation, and carried significant theological implications when undertaken without divine sanction. Scripture records five principal census events among the Israelites. (1.) The Sinai census at the beginning of the wilderness wanderings numbered 603,550 men of fighting age (Exodus 38:26; Numbers 1:46). (2.) A second census at the close of the wilderness period counted 601,730 (Numbers 26:51), showing a slight decrease. (3.) David's census near the end of his reign, which he ordered against Joab's counsel, provoked divine wrath because it reflected proud self-reliance rather than trust in God's protection; a plague killed seventy thousand men before God relented (2 Samuel 24; 1 Chronicles 21). (4.) Solomon enrolled the alien residents in Israel, numbering 153,600 (2 Chronicles 2:17). (5.) In the New Testament, the census of Augustus Caesar that brought Joseph and Mary to Bethlehem for the birth of Jesus (Luke 2:1–7) is a pivotal event connecting Roman imperial administration to the fulfillment of Micah's prophecy (Micah 5:2).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "census", "smith": "census", "isbe": "census"},
        "key_refs": ["Exodus 38:26", "Numbers 26:51", "2 Samuel 24:9", "Luke 2:1"],
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
    print(f'BP c1: Cab → Census: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
