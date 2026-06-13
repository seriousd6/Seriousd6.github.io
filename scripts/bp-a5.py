"""
BP Article Synthesis — a5: Aretas → Azaziah
Covers Easton entries: Aretas through Azaziah (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Named biblical individuals and rulers
  - places:   Geographic locations (cities, rivers, regions, mountain slopes)
  - concepts: Theological terms, ritual practices, cultural/military terms, flora/fauna
  - events:   Specific biblical observances (Day of Atonement)

Script: scripts/bp-a5.py
Run: python3 scripts/bp-a5.py
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
    "aretas": {
        "id": "aretas",
        "term": "Aretas",
        "category": "people",
        "intro": "<p>Aretas (meaning <em>agreeable</em> or <em>virtuous</em>) was a dynastic name of the Nabataean kings of Arabia Petraea. The Aretas most significant to New Testament history is Aretas IV, the father-in-law of Herod Antipas. When Antipas divorced Aretas's daughter to enter an adulterous union with Herodias (Mark 6:17), Aretas launched a war against him and destroyed his army. He subsequently gained control of Damascus, and his governor there attempted to arrest Paul—a dramatic episode Paul himself recalls as an illustration of his sufferings (2 Corinthians 11:32).</p>",
        "hitchcock_meaning": "agreeable; virtuous",
        "source_ids": {"easton": "aretas", "isbe": "aretas"},
        "key_refs": ["2 Corinthians 11:32", "Mark 6:17", "Matthew 14:3"],
        "sections": []
    },
    "argob": {
        "id": "argob",
        "term": "Argob",
        "category": "places",
        "intro": "<p>Argob (meaning <em>a turf</em> or <em>fat land</em>) was a distinct region within the kingdom of Og in Bashan, located in the territory east of the Jordan. It is described as an island of rocky terrain rising twenty to thirty feet above the surrounding basalt tableland, roughly thirty miles by twenty miles in extent. Sixty fortified cities with walls, gates, and bars lay within it (Deuteronomy 3:4). After the conquest it was assigned to Jair the son of Manasseh, who renamed the area Havoth-jair. The name Argob also belongs to one of the palace guards slain with King Pekahiah (2 Kings 15:25).</p>",
        "hitchcock_meaning": "a turf; or fat land",
        "source_ids": {"easton": "argob", "smith": "argob"},
        "key_refs": ["Deuteronomy 3:4", "1 Kings 4:13", "2 Kings 15:25"],
        "sections": []
    },
    "arieh": {
        "id": "arieh",
        "term": "Arieh",
        "category": "people",
        "intro": "<p>Arieh (meaning <em>the lion</em>) was one of the bodyguards of King Pekahiah of Israel, slain alongside the king by the conspirator Pekah son of Remaliah at Samaria (2 Kings 15:25). He is mentioned only in this single verse and no further details about him are recorded.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arieh", "smith": "arieh", "isbe": "arieh"},
        "key_refs": ["2 Kings 15:25"],
        "sections": []
    },
    "ariel": {
        "id": "ariel",
        "term": "Ariel",
        "category": "people",
        "intro": "<p>Ariel (meaning <em>lion of God</em> or <em>altar hearth</em>) serves three distinct uses in the Old Testament. (1.) A person: one of the chief men Ezra dispatched to Casiphia to recruit Levites for the return from exile (Ezra 8:16). (2.) A poetic name for Jerusalem, used by Isaiah in chapters 29:1–7 to describe the city as a place both embattled and ultimately defended by God—<em>victorious under God</em>. (3.) The Hebrew term for the altar hearth of the temple (Ezekiel 43:15–16), understood as the source of Israel's lion-like spiritual strength.</p>",
        "hitchcock_meaning": "altar; light or lion of God",
        "source_ids": {"easton": "ariel", "smith": "ariel", "isbe": "ariel"},
        "key_refs": ["Ezra 8:16", "Isaiah 29:1", "Isaiah 29:2", "Ezekiel 43:15"],
        "sections": []
    },
    "arimathea": {
        "id": "arimathea",
        "term": "Arimathea",
        "category": "places",
        "intro": "<p>Arimathea was a <em>city of the Jews</em> and the hometown of Joseph, the wealthy member of the Sanhedrin in whose newly hewn tomb the body of Jesus was laid after the crucifixion. All four Gospels name it as Joseph's place of origin. It is most probably identified with Ramathaim-zophim in the hill country of Ephraim, the birthplace of Samuel (1 Samuel 1:1). Its New Testament significance rests entirely on Joseph's act of faith and courage in requesting the body of Jesus from Pilate and providing an honorable burial.</p>",
        "hitchcock_meaning": "a lion dead to the Lord",
        "source_ids": {"easton": "arimathea", "smith": "arimathea"},
        "key_refs": ["Matthew 27:57", "Matthew 27:60", "Luke 23:51", "John 19:38"],
        "sections": []
    },
    "arioch": {
        "id": "arioch",
        "term": "Arioch",
        "category": "people",
        "intro": "<p>Arioch (meaning <em>lion-like</em> or <em>venerable</em>) is the name of two biblical figures. (1.) The king of Ellasar, one of the four kings allied with Chedorlaomer who defeated the five kings of the Jordan valley in the campaign during which Lot was captured (Genesis 14:1, 9). Abraham pursued this coalition to rescue Lot. (2.) The captain of Nebuchadnezzar's guard, ordered to execute the Babylonian wise men when they failed to interpret the king's dream. Daniel secured an audience with the king through Arioch, allowing time for divine revelation (Daniel 2:14–25).</p>",
        "hitchcock_meaning": "long; great; tall",
        "source_ids": {"easton": "arioch", "smith": "arioch", "isbe": "arioch"},
        "key_refs": ["Genesis 14:1", "Genesis 14:9", "Daniel 2:14", "Daniel 2:25"],
        "sections": []
    },
    "aristarchus": {
        "id": "aristarchus",
        "term": "Aristarchus",
        "category": "people",
        "intro": "<p>Aristarchus (meaning <em>best ruler</em>) was a native of Thessalonica who became one of Paul's closest and most loyal companions. He was seized by the Ephesian mob during the riot of the silversmiths (Acts 19:29) and traveled with Paul on his final journey toward Jerusalem (Acts 20:4). He accompanied Paul on the sea voyage to Rome, sharing the shipwreck off Malta (Acts 27:2), and remained with him during his Roman imprisonment, described as a <em>fellow prisoner</em> and <em>fellow worker</em> in Colossians 4:10 and Philemon 24.</p>",
        "hitchcock_meaning": "the best prince",
        "source_ids": {"easton": "aristarchus", "smith": "aristarchus", "isbe": "aristarchus"},
        "key_refs": ["Acts 19:29", "Acts 20:4", "Acts 27:2", "Colossians 4:10"],
        "sections": []
    },
    "aristobulus": {
        "id": "aristobulus",
        "term": "Aristobulus",
        "category": "people",
        "intro": "<p>Aristobulus (meaning <em>a good counselor</em>) is a Roman Christian whose household Paul greets in Romans 16:10. Nothing is stated about Aristobulus himself—only his household members are addressed, suggesting he may have been dead or absent. Some have identified him with Aristobulus the grandson of Herod the Great, a private citizen in Rome, whose freed servants and slaves may have formed a recognizable household group within the Roman church.</p>",
        "hitchcock_meaning": "a good counselor",
        "source_ids": {"easton": "aristobulus", "smith": "aristobulus", "isbe": "aristobulus"},
        "key_refs": ["Romans 16:10"],
        "sections": []
    },
    "ark": {
        "id": "ark",
        "term": "Ark",
        "category": "concepts",
        "intro": "<p>The word <em>ark</em> in the Bible refers to two distinct objects. (1.) <strong>Noah's ark</strong>: a large vessel of gopher wood, sealed with pitch, measuring 300 cubits long, 50 cubits broad, and 30 cubits high—an oblong, three-storied floating structure built over 100 years to preserve Noah, his family, and representative animals through the universal flood (Genesis 6:14–7:16). The New Testament holds Noah's completion of the ark as an act of faith (Hebrews 11:7) and Peter uses it as a type of salvation through Christ's resurrection (1 Peter 3:20–21).</p><p>(2.) <strong>The ark of the covenant</strong>: a rectangular chest of acacia wood overlaid with gold, housing the two tablets of the law and surmounted by the mercy seat, where God met with Israel. It led Israel through the wilderness, was carried into battle, and finally housed in the Holy of Holies in Solomon's temple.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ark", "isbe": "ark"},
        "key_refs": ["Genesis 6:14", "Genesis 7:13", "Hebrews 11:7", "1 Peter 3:20", "Exodus 25:10"],
        "sections": []
    },
    "arkite": {
        "id": "arkite",
        "term": "Arkite",
        "category": "people",
        "intro": "<p>The Arkites were descendants of Canaan listed in the table of nations (Genesis 10:17; 1 Chronicles 1:15). They are associated with the ancient city of Arka (Irqata), a Phoenician settlement on the coast of Syria, north of Tripolis. They appear only in genealogical contexts and no narrative is associated with them.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arkite", "isbe": "arkite"},
        "key_refs": ["Genesis 10:17", "1 Chronicles 1:15"],
        "sections": []
    },
    "arm": {
        "id": "arm",
        "term": "Arm",
        "category": "concepts",
        "intro": "<p>The arm is used throughout Scripture as a figure for power, strength, and active agency, particularly as an attribute of God. The <em>arm of the LORD</em> is a prominent biblical metaphor for divine intervention: it was stretched out in the Exodus (Exodus 15:16; Deuteronomy 4:34), and Isaiah appeals to it in his Servant Songs as the instrument of eschatological salvation (Isaiah 51:9; 53:1). A broken arm signifies military defeat (Ezekiel 30:21; Jeremiah 48:25), while a strong arm denotes sovereign power (Psalm 89:13). The concept carries both physical and theological dimensions across both Testaments.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arm", "isbe": "arm"},
        "key_refs": ["Exodus 15:16", "Isaiah 51:9", "Isaiah 53:1", "Psalms 89:13"],
        "sections": []
    },
    "armageddon": {
        "id": "armageddon",
        "term": "Armageddon",
        "category": "places",
        "intro": "<p>Armageddon (from the Hebrew <em>Har-Magedon</em>, meaning <em>mount of Megiddo</em>) appears only once in Scripture, in Revelation 16:16, where it symbolically designates the gathering place for the final battle of the great day of God Almighty. The imagery draws on the historic Plain of Esdraelon (the Valley of Jezreel) beneath Megiddo, one of the ancient world's great battlefields where decisive engagements shaped Israel's history—including the death of King Josiah (2 Chronicles 35:22).</p><p>Interpreted variously as a literal location, a symbolic scene, or a spiritual conflict, Armageddon in Christian eschatology has come to represent the climactic confrontation between the forces of God and the powers of evil at the end of history.</p>",
        "hitchcock_meaning": "hill of fruits; mountain of Megiddo",
        "source_ids": {"easton": "armageddon", "smith": "armageddon", "isbe": "armageddon"},
        "key_refs": ["Revelation 16:16"],
        "sections": []
    },
    "armenia": {
        "id": "armenia",
        "term": "Armenia",
        "category": "places",
        "intro": "<p>Armenia (from the Hebrew <em>Ararat</em>) was the highland region north and northeast of Assyria corresponding to the modern Armenian plateau. The Authorized Version uses <em>Armenia</em> where the Revised Version reads <em>Ararat</em>—notably in 2 Kings 19:37 (= Isaiah 37:38), where the sons of Sennacherib fled there after murdering their father, and in Jeremiah 51:27, where it is called to arms against Babylon. Genesis 8:4 records that Noah's ark rested on the mountains of Ararat. The name of the ancient kingdom of Urartu, centered on Lake Van, underlies both terms.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "armenia", "smith": "armenia"},
        "key_refs": ["Genesis 8:4", "2 Kings 19:37", "Jeremiah 51:27"],
        "sections": []
    },
    "armoni": {
        "id": "armoni",
        "term": "Armoni",
        "category": "people",
        "intro": "<p>Armoni (meaning <em>inhabitant of a fortress</em>) was the first-named of the two sons of Saul by his concubine Rizpah daughter of Aiah. Together with his brother Mephibosheth and five grandsons of Saul, he was handed over by David to the Gibeonites to atone for Saul's violation of the covenant with them. All seven were killed, after which Rizpah's vigil over their exposed bodies moved David to give Saul's house an honorable burial (2 Samuel 21:8–14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "armoni", "smith": "armoni"},
        "key_refs": ["2 Samuel 21:8", "2 Samuel 21:9"],
        "sections": []
    },
    "armour": {
        "id": "armour",
        "term": "Armour",
        "category": "concepts",
        "intro": "<p>Armour in Scripture denotes both offensive and defensive military equipment used across the biblical periods. Offensive weapons included swords, spears, javelins, bows, arrows, slings, and battle-axes; defensive equipment comprised shields, helmets, coats of mail, and greaves. David famously refused Saul's armour before facing Goliath (1 Samuel 17:39). Paul transforms the imagery into a theological metaphor: the <em>whole armour of God</em> (Ephesians 6:13–17) equips believers for spiritual warfare, each piece—belt of truth, breastplate of righteousness, shield of faith, helmet of salvation, and sword of the Spirit—corresponding to a spiritual reality.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "armour"},
        "key_refs": ["1 Samuel 17:39", "Ephesians 6:13", "Ephesians 6:14", "Ephesians 6:17"],
        "sections": []
    },
    "armour-bearer": {
        "id": "armour-bearer",
        "term": "Armour-bearer",
        "category": "concepts",
        "intro": "<p>An armour-bearer was an officer selected by kings and commanders not only to carry weapons but also to stand beside his lord in combat and to dispatch enemies wounded by him. The role required exceptional bravery and absolute loyalty. Notable instances include Abimelech's armour-bearer (Judges 9:54), Jonathan's unnamed armour-bearer whose faith enabled the rout of a Philistine garrison (1 Samuel 14:7), and the young David who served Saul in this capacity (1 Samuel 16:21). Saul's own armour-bearer refused to kill the wounded king at Gilboa; Saul then fell on his own sword (1 Samuel 31:4–6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "armour-bearer"},
        "key_refs": ["1 Samuel 14:7", "1 Samuel 16:21", "1 Samuel 31:4", "Judges 9:54"],
        "sections": []
    },
    "armoury": {
        "id": "armoury",
        "term": "Armoury",
        "category": "concepts",
        "intro": "<p>An armoury was a storehouse for weapons and military equipment. In the Old Testament, the term is used of the treasury of the house of the forest of Lebanon, which housed Solomon's golden shields (1 Kings 10:17; 2 Samuel 8:7), and of Nehemiah's armoury adjacent to the Water Gate (Nehemiah 3:19). Jeremiah 50:25 speaks of the LORD opening his armoury to bring forth weapons of divine judgment against Babylon—a vivid metaphor of the LORD as a warrior deploying his arsenal.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "armoury"},
        "key_refs": ["Nehemiah 3:19", "Jeremiah 50:25", "2 Samuel 8:7"],
        "sections": []
    },
    "army": {
        "id": "army",
        "term": "Army",
        "category": "concepts",
        "intro": "<p>The Israelite army evolved from the tribal levy of the wilderness period—organized by tribe and family, marching in formation (Exodus 13:18)—into a professional standing force under David and Solomon, supplemented by foreign mercenaries (the Cherethites and Pelethites). The basic tactical unit was a division of a thousand men under a commander, with subdivisions of hundreds and fifties. During the monarchy, a royal bodyguard and a chariot force were added. The Mosaic law provided exemptions from service for the newly married, newly housed, newly planted, and the fearful (Deuteronomy 20:5–8). In prophetic and apocalyptic usage, the <em>host of heaven</em> and the <em>armies of the living God</em> designate angelic or divine forces.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "army", "smith": "army", "isbe": "army"},
        "key_refs": ["Exodus 13:18", "Numbers 2:2", "Deuteronomy 20:5", "1 Samuel 17:26"],
        "sections": []
    },
    "arnon": {
        "id": "arnon",
        "term": "Arnon",
        "category": "places",
        "intro": "<p>Arnon (meaning <em>swift</em> or <em>rejoicing</em>) was the southern boundary of Israelite territory east of the Jordan, separating Israel from Moab. The river rises in the mountains of Gilead and flows westward through a deep ravine for approximately eighty miles before emptying into the Dead Sea nearly opposite En-gedi. Its modern name is Wadi el-Mujeb. The Arnon was the northern boundary of Moab and the southern limit of Amorite territory before Israel's conquest; the towns on its banks were disputed in Israel's conflicts with Moab and Ammon throughout the period of the judges and monarchy.</p>",
        "hitchcock_meaning": "rejoicing; sunlight",
        "source_ids": {"easton": "arnon", "smith": "arnon"},
        "key_refs": ["Deuteronomy 3:8", "Deuteronomy 3:16", "Judges 11:26"],
        "sections": []
    },
    "aroer": {
        "id": "aroer",
        "term": "Aroer",
        "category": "places",
        "intro": "<p>Aroer (meaning <em>ruins</em> or <em>heath</em>) is the name of three locations in the Old Testament. (1.) The most prominent is a town on the north bank of the Arnon, on the border of Moab, assigned to Reuben (Deuteronomy 4:48; Joshua 12:2). (2.) A town in Gilead assigned to Gad (Joshua 13:25; 2 Samuel 24:5). (3.) A town in the Negev of Judah (1 Samuel 30:28), where David sent spoil after his victory over the Amalekites. The first is the most frequently mentioned in connection with territorial boundaries and military campaigns throughout the periods of conquest and monarchy.</p>",
        "hitchcock_meaning": "heath; tamarisk",
        "source_ids": {"easton": "aroer", "smith": "aroer"},
        "key_refs": ["Deuteronomy 4:48", "Joshua 12:2", "Judges 11:26", "2 Kings 10:33"],
        "sections": []
    },
    "arpad": {
        "id": "arpad",
        "term": "Arpad",
        "category": "places",
        "intro": "<p>Arpad (meaning <em>the light of redemption</em>) was an Aramean city-state north of Hamath in Syria, frequently paired with Hamath in the prophetic literature. Arpad was conquered by the Assyrians in the eighth century BC and its fate became a boast in Assyrian taunts against Jerusalem: the Rabshakeh invokes it as proof that no god had delivered any nation from Assyrian power (Isaiah 36:19; 37:13; 2 Kings 18:34; 19:13). Isaiah uses its fall as part of a lament over the march of Assyrian conquest (Isaiah 10:9).</p>",
        "hitchcock_meaning": "the light of redemption",
        "source_ids": {"easton": "arpad"},
        "key_refs": ["Isaiah 10:9", "Isaiah 36:19", "2 Kings 18:34"],
        "sections": []
    },
    "arphaxad": {
        "id": "arphaxad",
        "term": "Arphaxad",
        "category": "people",
        "intro": "<p>Arphaxad (meaning <em>a healer</em> or <em>a releaser</em>) was the third son of Shem, born two years after the Flood (Genesis 11:10). He lived 438 years and became an ancestor of Eber, from whom the Hebrews take their name. He dwelt in Mesopotamia and is regarded by Josephus as the progenitor of the Chaldeans. Luke's genealogy of Jesus traces the line through Arphaxad to Shem and Noah (Luke 3:36), making him a key link in the antediluvian and post-diluvian genealogies connecting Abraham to Noah.</p>",
        "hitchcock_meaning": "a healer; a releaser",
        "source_ids": {"easton": "arphaxad", "smith": "arphaxad", "isbe": "arphaxad"},
        "key_refs": ["Genesis 11:10", "1 Chronicles 1:17", "Luke 3:36"],
        "sections": []
    },
    "arrows": {
        "id": "arrows",
        "term": "Arrows",
        "category": "concepts",
        "intro": "<p>Arrows were among the most common offensive weapons of the ancient Near East, made initially of reeds and later of wood tipped with flint or iron. They are mentioned frequently in both literal and metaphorical senses in Scripture. Figuratively, arrows denote divine judgment—God's arrows of lightning, pestilence, and disaster (Deuteronomy 32:23, 42; Psalm 7:13; 18:14). Arrows are also used as a positive image of children (Psalm 127:4) and of the Lord's word directed against enemies (Zechariah 9:14). Jonathan's signal arrows to David (1 Samuel 20:20–22) is one of the most memorable narrative uses of the weapon.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arrows", "smith": "arrows"},
        "key_refs": ["Deuteronomy 32:23", "Psalms 127:4", "1 Samuel 20:20", "Ephesians 6:16"],
        "sections": []
    },
    "artaxerxes": {
        "id": "artaxerxes",
        "term": "Artaxerxes",
        "category": "people",
        "intro": "<p>Artaxerxes is the Greek form of a name borne by several Persian kings. Two are relevant to the biblical narrative. (1.) The king who halted the rebuilding of the temple at Jerusalem in response to a complaint from the inhabitants of Samaria (Ezra 4:7–23), probably identified with the Smerdis of classical sources. (2.) The long-reigning Artaxerxes I Longimanus (464–425 BC), in whose seventh year Ezra led a second return of exiles to Jerusalem (Ezra 7:1) and in whose twentieth year Nehemiah received permission to rebuild the city walls (Nehemiah 2:1–8). Both episodes make Artaxerxes I a pivotal figure in the restoration of the Jewish community after the Babylonian exile.</p>",
        "hitchcock_meaning": "the silence of light; fervent to spoil",
        "source_ids": {"easton": "artaxerxes", "smith": "artaxerxes", "isbe": "artaxerxes"},
        "key_refs": ["Ezra 4:7", "Ezra 7:1", "Nehemiah 2:1"],
        "sections": []
    },
    "artificer": {
        "id": "artificer",
        "term": "Artificer",
        "category": "concepts",
        "intro": "<p>An artificer was a craftsman skilled in working with any material—metal, wood, stone, or cloth. The term renders the Hebrew <em>ḥārāš</em>, encompassing smiths, carpenters, and engravers. Tubal-cain is identified as the first artificer in bronze and iron (Genesis 4:22), making him the ancestor of metalworking crafts. Isaiah includes the artificer among the skilled leaders of whom Jerusalem would be stripped as divine judgment (Isaiah 3:3). The construction of the tabernacle required artificers of exceptional skill, Bezalel being filled with God's Spirit specifically for this work (Exodus 31:3–5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "artificer", "isbe": "artificer"},
        "key_refs": ["Genesis 4:22", "Isaiah 3:3", "Exodus 31:3"],
        "sections": []
    },
    "artillery": {
        "id": "artillery",
        "term": "Artillery",
        "category": "concepts",
        "intro": "<p>Artillery appears in the King James Version of 1 Samuel 20:40 as a translation of the Hebrew <em>keli</em> (meaning <em>apparatus</em> or <em>equipment</em>), referring collectively to Jonathan's bow and arrows—the signal weapons he used to warn David to flee. The word carries no modern meaning of siege weaponry or cannon; it is simply an archaic English term for any missile weapons or equipment. Modern translations render the word as <em>weapons</em> or <em>bow and arrows</em>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "artillery", "isbe": "artillery"},
        "key_refs": ["1 Samuel 20:40"],
        "sections": []
    },
    "arvad": {
        "id": "arvad",
        "term": "Arvad",
        "category": "places",
        "intro": "<p>Arvad (meaning <em>wandering</em>) was a small island and city-state on the coast of Phoenicia (modern Ruad Island, off the coast of Syria), northernmost of the Phoenician cities. Its inhabitants, the Arvadites, are listed in the table of nations as descendants of Canaan (Genesis 10:18). Ezekiel mentions Arvad as furnishing skilled oarsmen and soldiers to Tyre (Ezekiel 27:8, 11), reflecting its importance as a maritime trading power in the ancient Mediterranean world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arvad", "smith": "arvad"},
        "key_refs": ["Genesis 10:18", "Ezekiel 27:8"],
        "sections": []
    },
    "asa": {
        "id": "asa",
        "term": "Asa",
        "category": "people",
        "intro": "<p>Asa (meaning <em>physician</em> or <em>cure</em>) was the third king of Judah, son of Abijah and great-grandson of Solomon, who reigned forty-one years (circa 910–869 BC). He is remembered as one of Judah's reforming kings: he removed the foreign altars and high places, broke down sacred pillars, cut down the Asherah poles, and even deposed his own grandmother Maachah from the queen-mother's position because of her Asherah idol. A decisive military victory over Zerah the Ethiopian, granted after prayer, marked the high point of his reign.</p><p>In his latter years Asa's faith weakened: he relied on Syria rather than God against Baasha of Israel, imprisoned the prophet Hanani, and in his final illness sought only physicians rather than the LORD—failures that cast a shadow over an otherwise exemplary reign.</p>",
        "hitchcock_meaning": "physician; cure",
        "source_ids": {"easton": "asa", "smith": "asa", "isbe": "asa"},
        "key_refs": ["1 Kings 15:8", "2 Chronicles 14:11", "2 Chronicles 15:16", "2 Chronicles 16:12"],
        "sections": []
    },
    "asahel": {
        "id": "asahel",
        "term": "Asahel",
        "category": "people",
        "intro": "<p>Asahel (meaning <em>creature of God</em> or <em>made by God</em>) was the youngest son of Zeruiah, David's sister, and the brother of Joab and Abishai. He was celebrated for his exceptional swiftness of foot. At the battle of Gibeon after Saul's death, Asahel pursued Abner, commander of Ish-bosheth's forces. Abner twice urged him to turn aside, but Asahel refused and was killed when Abner thrust the butt of his spear through him. His death at Abner's hand became the pretext Joab later used to murder Abner, claiming the right of a blood avenger. Asahel is listed among David's thirty mighty men (2 Samuel 23:24).</p>",
        "hitchcock_meaning": "creature of God",
        "source_ids": {"easton": "asahel", "smith": "asahel", "isbe": "asahel"},
        "key_refs": ["2 Samuel 2:18", "2 Samuel 2:23", "2 Samuel 23:24", "1 Chronicles 11:26"],
        "sections": []
    },
    "asaph": {
        "id": "asaph",
        "term": "Asaph",
        "category": "people",
        "intro": "<p>Asaph (meaning <em>convener</em> or <em>collector</em>) was a Levite of the clan of Gershom appointed by David as one of the three chief directors of temple music (1 Chronicles 6:39; 15:17). He stood at David's right hand in the procession that brought the ark to Jerusalem, playing cymbals. He is also identified as a <em>seer</em> (2 Chronicles 29:30), and twelve of the Psalms (50 and 73–83) are attributed to him or his school—psalms characterized by prophetic reflection on Israel's covenant history and divine judgment.</p><p>The <em>sons of Asaph</em>—his descendants or guild—continued as temple musicians through the monarchy and into the restoration after the exile (Ezra 2:41; Nehemiah 7:44), making Asaph's influence on Israelite worship remarkably durable.</p>",
        "hitchcock_meaning": "who gathers together",
        "source_ids": {"easton": "asaph", "smith": "asaph", "isbe": "asaph"},
        "key_refs": ["1 Chronicles 6:39", "1 Chronicles 25:1", "Psalms 50:1", "2 Chronicles 29:30"],
        "sections": []
    },
    "ascension": {
        "id": "ascension",
        "term": "Ascension",
        "category": "events",
        "intro": "<p>The Ascension of Christ refers to the bodily departure of the risen Jesus into heaven forty days after his resurrection (Acts 1:3, 9–11). Witnessed by his disciples on the Mount of Olives, the event is described in Luke 24:50–51 and Acts 1:9, where Jesus was lifted up and a cloud received him out of their sight. Two angels announced that he would return in the same manner. The Ascension marked the conclusion of Christ's post-resurrection appearances and the beginning of his session at the Father's right hand (Hebrews 1:3; Ephesians 1:20), from which he sent the Holy Spirit at Pentecost (John 16:7; Acts 2:33). It is affirmed in the Apostles' Creed and the Nicene Creed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ascension", "isbe": "ascension"},
        "key_refs": ["Acts 1:9", "Acts 1:11", "Luke 24:51", "Hebrews 1:3", "Ephesians 1:20"],
        "sections": []
    },
    "asenath": {
        "id": "asenath",
        "term": "Asenath",
        "category": "people",
        "intro": "<p>Asenath (an Egyptian name meaning <em>gift of the sun-god</em>, or <em>peril</em> in Hitchcock) was the daughter of Potiphera, priest of On (Heliopolis), and the wife given to Joseph by Pharaoh after his elevation to second-in-command of Egypt (Genesis 41:45). She bore Joseph two sons—Manasseh and Ephraim—both of whom Jacob blessed and adopted as his own, giving them a share in the inheritance of Israel (Genesis 48:5). Asenath represents the integration of Joseph into Egyptian court life and prefigures the mixed heritage of the tribe of Joseph.</p>",
        "hitchcock_meaning": "peril; misfortune",
        "source_ids": {"easton": "asenath", "smith": "asenath", "isbe": "asenath"},
        "key_refs": ["Genesis 41:45", "Genesis 41:50", "Genesis 46:20"],
        "sections": []
    },
    "ash": {
        "id": "ash",
        "term": "Ash",
        "category": "concepts",
        "intro": "<p>The ash tree in the Bible (Hebrew <em>oren</em>, meaning <em>tremulous</em>) is mentioned only in Isaiah 44:14, in the Authorized Version, as one of the trees a craftsman might use both to warm himself and to carve into an idol—an ironic passage highlighting the absurdity of idol worship. The Revised Version renders the word as <em>fir tree</em> or <em>pine tree</em>, and modern translations vary. The precise identification of the Hebrew species is uncertain, but the context emphasizes its use as a fuel and a material for woodworking.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ash", "smith": "ash"},
        "key_refs": ["Isaiah 44:14"],
        "sections": []
    },
    "ashdod": {
        "id": "ashdod",
        "term": "Ashdod",
        "category": "places",
        "intro": "<p>Ashdod (meaning <em>stronghold</em> or <em>effusion</em>) was one of the five major cities of the Philistine pentapolis, located about midway between Gaza and Joppa, three miles from the Mediterranean coast. It was a principal center of the worship of Dagon, whose temple there was disrupted when the ark of the covenant was placed before the idol and the statue fell and broke (1 Samuel 5:1–7). Though assigned to Judah, Ashdod was never incorporated into Israelite territory. King Uzziah breached its walls (2 Chronicles 26:6), and it appears in prophetic judgment oracles. In the New Testament, Philip the evangelist passed through Ashdod (called Azotus) after his encounter with the Ethiopian eunuch (Acts 8:40).</p>",
        "hitchcock_meaning": "effusion; inclination; theft",
        "source_ids": {"easton": "ashdod", "isbe": "ashdod"},
        "key_refs": ["Joshua 15:47", "1 Samuel 5:1", "1 Samuel 5:5", "Acts 8:40"],
        "sections": []
    },
    "ashdoth-pisgah": {
        "id": "ashdoth-pisgah",
        "term": "Ashdoth-pisgah",
        "category": "places",
        "intro": "<p>Ashdoth-pisgah (meaning <em>the slopes of Pisgah</em>) refers to the descending ravines and slopes on the western face of the Pisgah/Abarim mountain range, bordering the eastern shore of the Dead Sea and the Jordan valley. The name occurs in boundary and territorial descriptions for the eastern side of the Jordan (Deuteronomy 3:17; 4:49; Joshua 12:3; 13:20) rather than in any narrative event.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashdoth-pisgah", "isbe": "ashdoth-pisgah"},
        "key_refs": ["Deuteronomy 3:17", "Joshua 12:3", "Joshua 13:20"],
        "sections": []
    },
    "asher": {
        "id": "asher",
        "term": "Asher",
        "category": "people",
        "intro": "<p>Asher (meaning <em>happiness</em>) was the eighth son of Jacob, born to Zilpah, Leah's handmaid (Genesis 30:13). His mother named him Asher—<em>happy</em>—because she felt the women would pronounce her happy at his birth. The tribe founded by his four sons and one daughter received a coastal allotment in the northwest of Canaan, from the Carmel range to Sidon, including some of the richest agricultural land in Palestine. However, the tribe of Asher failed to drive out the Canaanite inhabitants of many of their cities and is notably absent from Deborah's battle against Sisera.</p><p>In the New Testament, the prophetess Anna was of the tribe of Asher (Luke 2:36), and Asher appears in the list of the twelve tribes sealed in Revelation 7:6.</p>",
        "hitchcock_meaning": "happiness",
        "source_ids": {"easton": "asher", "smith": "asher"},
        "key_refs": ["Genesis 30:13", "Numbers 2:27", "Joshua 19:24", "Luke 2:36"],
        "sections": []
    },
    "asherah": {
        "id": "asherah",
        "term": "Asherah",
        "category": "concepts",
        "intro": "<p>Asherah (plural <em>Asherim</em>) was a Canaanite goddess representing the passive, fertility principle in nature—the feminine counterpart to Baal, and related to the Assyrian goddess Ishtar. Her cult symbol was a wooden pole or shaped tree-trunk planted in the ground, often erected beside altars. The Authorized Version translates the word as <em>grove</em> or <em>groves</em>, but the Revised Version restores the proper name Asherah.</p><p>The Asherah poles appear frequently in Scripture as a characteristic form of Israelite apostasy: Gideon was commanded to cut down his father's (Judges 6:25–26), Manasseh installed one in the temple (2 Kings 21:7), and Josiah destroyed them in his reforms (2 Kings 23:6–7). The repeated association with Baal worship reflects the fertility cult's deep hold on Israelite popular religion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "asherah", "smith": "asherah", "isbe": "asherah"},
        "key_refs": ["Exodus 34:13", "Judges 6:25", "1 Kings 16:33", "2 Kings 23:6"],
        "sections": []
    },
    "ashes": {
        "id": "ashes",
        "term": "Ashes",
        "category": "concepts",
        "intro": "<p>Ashes in Scripture carry both ritual and symbolic significance. Ritually, the ashes of the red heifer mixed with water formed the purification solution for removing corpse-contamination (Numbers 19:5, 9), a practice the New Testament references as a type of the cleansing power of Christ's blood (Hebrews 9:13). Symbolically, sitting in ashes or wearing ashes on the head is one of the primary expressions of grief, mourning, and penitence in both Testaments (2 Samuel 13:19; Esther 4:3; Jeremiah 6:26; Matthew 11:21). The phrase <em>dust and ashes</em> (Genesis 18:27; Job 30:19) expresses human frailty before God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashes", "smith": "ashes"},
        "key_refs": ["Numbers 19:5", "Hebrews 9:13", "Esther 4:3", "Matthew 11:21"],
        "sections": []
    },
    "ashkelon": {
        "id": "ashkelon",
        "term": "Ashkelon",
        "category": "places",
        "intro": "<p>Ashkelon (also Askelon and Ascalon) was one of the five cities of the Philistine pentapolis, situated on the Mediterranean coast twelve miles north of Gaza. It was an important seaport and commercial hub. An Egyptian inscription at Karnak records its capture by Rameses II. In the period of the judges it was briefly taken by Judah (Judges 1:18) but quickly retaken by the Philistines. David's lament over Saul and Jonathan invokes Ashkelon in the famous phrase <em>tell it not in Gath, publish it not in the streets of Ashkelon</em> (2 Samuel 1:20). Prophets including Jeremiah, Zephaniah, Amos, and Zechariah pronounced judgment against it.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashkelon", "isbe": "ashkelon"},
        "key_refs": ["Joshua 13:3", "Judges 1:18", "2 Samuel 1:20", "Jeremiah 47:5"],
        "sections": []
    },
    "ashkenaz": {
        "id": "ashkenaz",
        "term": "Ashkenaz",
        "category": "people",
        "intro": "<p>Ashkenaz (meaning <em>a fire that spreads</em>) was the firstborn son of Gomer and grandson of Japheth in the table of nations (Genesis 10:3). He is regarded as the ancestor of a northern people, probably the Scythians or a related Indo-European group. In Jeremiah 51:27 Ashkenaz is called alongside Ararat and Minni to marshal forces against Babylon. In later Jewish usage the name came to designate the Germanic lands and their Jewish communities (Ashkenazim).</p>",
        "hitchcock_meaning": "a fire that spreads",
        "source_ids": {"easton": "ashkenaz", "smith": "ashkenaz", "isbe": "ashkenaz"},
        "key_refs": ["Genesis 10:3", "Jeremiah 51:27"],
        "sections": []
    },
    "ashpenaz": {
        "id": "ashpenaz",
        "term": "Ashpenaz",
        "category": "people",
        "intro": "<p>Ashpenaz was the chief of the eunuchs in Nebuchadnezzar's court, charged with selecting and training the young Judean captives for royal service in Babylon—among them Daniel, Hananiah, Mishael, and Azariah (Daniel 1:3). He was responsible for their education in Chaldean language and literature and for assigning them Babylonian names. When Daniel requested a diet of vegetables and water rather than the king's food, Ashpenaz was sympathetic but anxious about royal displeasure. He appears only in Daniel 1.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashpenaz", "smith": "ashpenaz", "isbe": "ashpenaz"},
        "key_refs": ["Daniel 1:3", "Daniel 1:7", "Daniel 1:10"],
        "sections": []
    },
    "ashtaroth": {
        "id": "ashtaroth",
        "term": "Ashtaroth",
        "category": "places",
        "intro": "<p>Ashtaroth was an ancient city in Bashan, in the territory of the Rephaim, named after the goddess Ashtoreth—a clue to its early cultic significance. It was the royal city of Og king of Bashan (Deuteronomy 1:4; Joshua 12:4) and was conquered by Israel in the Transjordanian campaign. The city was later assigned to the half-tribe of Manasseh and became a Levitical city (Joshua 21:27; 1 Chronicles 6:71). It is sometimes identified with the nearby site of Ashteroth-Karnaim.</p>",
        "hitchcock_meaning": "Ashtoreth, flocks; sheep; riches",
        "source_ids": {"easton": "ashtaroth", "smith": "ashtaroth", "isbe": "ashtaroth"},
        "key_refs": ["Deuteronomy 1:4", "Joshua 12:4", "Joshua 13:12"],
        "sections": []
    },
    "ashteroth-karnaim": {
        "id": "ashteroth-karnaim",
        "term": "Ashteroth Karnaim",
        "category": "places",
        "intro": "<p>Ashteroth Karnaim (meaning <em>Ashtoreth of the two horns</em>, possibly reflecting a double-horned goddess) was an ancient city of the Rephaim in Bashan, mentioned in Genesis 14:5 as one of the cities defeated by Chedorlaomer and his allies in their campaign against the eastern Jordan valley before the rescue of Lot by Abraham. It may be identified with or near the biblical Ashtaroth, and is tentatively located at the modern site of Sheikh Sa'ad in the Hauran.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashteroth-karnaim", "smith": "ashteroth-karnaim", "isbe": "ashteroth-karnaim"},
        "key_refs": ["Genesis 14:5"],
        "sections": []
    },
    "ashtoreth": {
        "id": "ashtoreth",
        "term": "Ashtoreth",
        "category": "concepts",
        "intro": "<p>Ashtoreth (plural <em>Ashtaroth</em>) was the principal female deity of the Phoenicians, corresponding to the Babylonian Ishtar and the Greek Aphrodite/Astarte. As the goddess of love, fertility, and war, she represented the passive principle of nature in contrast to the sun-god Baal. She was worshipped at high places with rituals associated with sexual immorality. Solomon, influenced by his foreign wives, built a high place for Ashtoreth of the Sidonians (1 Kings 11:5, 33), an apostasy that contributed to the division of the kingdom.</p><p>Israel's repeated turn to the Ashtaroth—always linked with Baal worship—is a recurring theme of the book of Judges, marking cycles of apostasy and divine discipline. The prophets condemned the cult as fundamental betrayal of covenant loyalty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashtoreth", "smith": "ashtoreth", "isbe": "ashtoreth"},
        "key_refs": ["Judges 10:6", "1 Samuel 7:4", "1 Kings 11:5", "1 Kings 11:33"],
        "sections": []
    },
    "ashurites": {
        "id": "ashurites",
        "term": "Ashurites",
        "category": "people",
        "intro": "<p>The Ashurites are mentioned in 2 Samuel 2:9 as one of the groups over whom Ish-bosheth, Saul's son, was made king by Abner after Saul's death. Their identity is uncertain—they may represent the tribe of Asher, or a group of Israelites in the Transjordanian region. The text is brief and the term appears only in this single reference.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ashurites", "isbe": "ashurites"},
        "key_refs": ["2 Samuel 2:9"],
        "sections": []
    },
    "asia": {
        "id": "asia",
        "term": "Asia",
        "category": "places",
        "intro": "<p>Asia in the New Testament refers to the Roman province of Proconsular Asia—not the continent, but the western portion of Asia Minor (modern western Turkey), administered from Ephesus. It encompassed the great cities of Ephesus, Smyrna, Pergamum, Thyatira, Sardis, Philadelphia, and Laodicea—the seven churches addressed in Revelation 1–3. Paul was twice prevented from entering Asia by the Spirit before his decisive mission to Ephesus, where he remained three years and from which <em>all who dwelt in Asia heard the word of the Lord</em> (Acts 19:10). Asia Minor was also the seedbed of the earliest Christian communities addressed by Peter (1 Peter 1:1).</p>",
        "hitchcock_meaning": "muddy; boggy",
        "source_ids": {"easton": "asia", "smith": "asia", "isbe": "asia"},
        "key_refs": ["Acts 16:6", "Acts 19:10", "Acts 19:22", "Revelation 1:4"],
        "sections": []
    },
    "asnapper": {
        "id": "asnapper",
        "term": "Asnapper",
        "category": "people",
        "intro": "<p>Asnapper is described in Ezra 4:10 as a <em>great and noble</em> Assyrian king who transported various peoples into the cities of Samaria, continuing the Assyrian resettlement policy that had been practiced since the fall of the northern kingdom. Most scholars identify him with Ashurbanipal (669–627 BC), known to classical sources as Sardanapalos, the last great Assyrian king, renowned for his library at Nineveh and his military campaigns. His settlers in Samaria later became the mixed population associated with the Samaritans.</p>",
        "hitchcock_meaning": "unhappiness; increase of danger",
        "source_ids": {"easton": "asnapper", "smith": "asnapper", "isbe": "asnapper"},
        "key_refs": ["Ezra 4:10"],
        "sections": []
    },
    "asp": {
        "id": "asp",
        "term": "Asp",
        "category": "concepts",
        "intro": "<p>Asp (Hebrew <em>pethen</em>) was a highly venomous snake, probably the Egyptian cobra (<em>Naja haje</em>) or the sand viper, known for the deadly potency of its poison. It appears in both literal and figurative uses in Scripture: Deuteronomy 32:33 compares the vine of Sodom to the poison of asps, and Job 20:14–16 uses it as an image of the ultimate self-destruction of the wicked. Isaiah's vision of the messianic age includes the nursing child playing safely over the asp's den (Isaiah 11:8). Paul, in Romans 3:13, cites Psalm 140:3—<em>the poison of asps is under their lips</em>—as part of his indictment of universal human sinfulness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "asp", "smith": "asp"},
        "key_refs": ["Deuteronomy 32:33", "Isaiah 11:8", "Romans 3:13"],
        "sections": []
    },
    "ass": {
        "id": "ass",
        "term": "Ass",
        "category": "concepts",
        "intro": "<p>The ass (donkey) was the most common beast of burden in biblical Palestine, appearing throughout both Testaments in mundane, symbolic, and prophetic roles. The domesticated species included the she-ass (<em>ʾāthôn</em>), the male working donkey (<em>ḥamôr</em>), and the swift riding ass (<em>ʿayir</em>). Patriarchs owned asses as livestock (Genesis 12:16; 45:23); Balaam's ass spoke by divine intervention (Numbers 22:23–30); and Samson slew Philistines with an ass's jawbone (Judges 15:15–16). Most significantly, Zechariah prophesied that Zion's king would come <em>humble, and riding on an ass</em> (Zechariah 9:9)—a prophecy fulfilled at Jesus's triumphal entry into Jerusalem (Matthew 21:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ass", "smith": "ass"},
        "key_refs": ["Numbers 22:23", "Zechariah 9:9", "Matthew 21:5", "Genesis 49:14"],
        "sections": []
    },
    "asshur": {
        "id": "asshur",
        "term": "Asshur",
        "category": "people",
        "intro": "<p>Asshur was the second son of Shem in the table of nations (Genesis 10:22; 1 Chronicles 1:17) and the eponymous ancestor of the Assyrians. He is credited with going out from the land of Shinar to found Nineveh and the other great cities of Assyria (Genesis 10:11–12). The name also occurs as a place name (the city of Asshur on the Tigris, ancient capital of Assyria) and as a collective designation for the Assyrian nation in prophetic texts (Numbers 24:22–24; Isaiah 19:23; Ezekiel 27:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "asshur", "smith": "asshur"},
        "key_refs": ["Genesis 10:11", "Genesis 10:22", "Numbers 24:22"],
        "sections": []
    },
    "assos": {
        "id": "assos",
        "term": "Assos",
        "category": "places",
        "intro": "<p>Assos (meaning <em>approaching</em> or <em>coming near</em>) was a seaport on the north shore of the Gulf of Adramyttium in the district of Mysia (Proconsular Asia), about twenty miles south of Alexandria Troas by road but a longer distance by sea around Cape Lectum. On his final journey to Jerusalem Paul walked the overland route from Troas to Assos while his companions sailed ahead; he boarded the ship at Assos (Acts 20:13–14). The city was known in antiquity for its philosophers and as the site where Aristotle spent time.</p>",
        "hitchcock_meaning": "approaching; coming near",
        "source_ids": {"easton": "assos", "isbe": "assos"},
        "key_refs": ["Acts 20:13", "Acts 20:14"],
        "sections": []
    },
    "assurance": {
        "id": "assurance",
        "term": "Assurance",
        "category": "concepts",
        "intro": "<p>Assurance in Scripture refers both to the certainty of divine facts and to the personal confidence of the believer's standing before God. Paul in Acts 17:31 declares that God has given <em>assurance</em> (Greek <em>pistis</em>) of the coming judgment by raising Christ from the dead. The Epistle to the Hebrews emphasizes the full assurance of faith in drawing near to God (10:22) and the full assurance of hope (6:11). Colossians 2:2 speaks of the riches of full assurance of understanding in knowing Christ. The Reformers and later Puritan theologians gave extensive attention to the <em>assurance of salvation</em> as a legitimate and important aspect of Christian experience.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "assurance", "isbe": "assurance"},
        "key_refs": ["Acts 17:31", "Hebrews 10:22", "Hebrews 6:11", "Colossians 2:2"],
        "sections": []
    },
    "assyria": {
        "id": "assyria",
        "term": "Assyria",
        "category": "places",
        "intro": "<p>Assyria was one of the great empires of the ancient Near East, centered on the upper Tigris valley in modern northern Iraq. Its name derived from the city of Asshur, its original capital, traditionally founded by Asshur son of Shem. Rising to dominance in the ninth century BC, Assyria became the dominant power of the Near East under kings such as Tiglath-pileser III, Shalmaneser V, Sargon II, and Sennacherib. Its policy of mass deportation reshaped the populations of conquered peoples: the northern kingdom of Israel was destroyed by Sargon II in 722 BC and its inhabitants deported—the event known as the exile of the ten tribes.</p><p>Sennacherib's campaign against Judah in 701 BC, including his siege of Lachish and taunting of Jerusalem, is recorded in both Kings and Isaiah. The prophets Nahum and Zephaniah announced Assyria's doom, which came with the fall of Nineveh in 612 BC.</p>",
        "hitchcock_meaning": "country of Assur or Ashur",
        "source_ids": {"easton": "assyria", "isbe": "assyria"},
        "key_refs": ["Genesis 10:22", "2 Kings 17:5", "2 Kings 17:6", "Isaiah 36:1"],
        "sections": []
    },
    "astrologer": {
        "id": "astrologer",
        "term": "Astrologer",
        "category": "concepts",
        "intro": "<p>Astrologers in the biblical world were court diviners who claimed to interpret celestial signs and predict events from the positions of stars and planets. In Daniel's account they are one of the professional classes summoned repeatedly by Nebuchadnezzar and Belshazzar—alongside magicians, enchanters, and Chaldeans—to interpret dreams and writing, and repeatedly they fail where Daniel succeeds through divine revelation (Daniel 1:20; 2:2, 10, 27). The law of Moses prohibited divination in all its forms (Deuteronomy 4:19; 18:10–12), and Isaiah mocks the astrologers of Babylon who cannot save the city from divine judgment (Isaiah 47:13–14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "astrologer"},
        "key_refs": ["Daniel 1:20", "Daniel 2:2", "Daniel 2:27", "Isaiah 47:13"],
        "sections": []
    },
    "astronomy": {
        "id": "astronomy",
        "term": "Astronomy",
        "category": "concepts",
        "intro": "<p>The Hebrews observed the heavens as the work of God and drew theological rather than astrological conclusions from what they saw. The Psalms and Job contain some of Scripture's most eloquent reflections on the stars as declarations of divine glory (Psalm 19:1; Job 9:9; 38:31–33). Named constellations include the Pleiades, Orion, and the Bear with her cubs. Israel's calendar was lunar-solar, dependent on observation of the new moon, but divination from celestial bodies was strictly forbidden (Deuteronomy 4:19). The star of Bethlehem (Matthew 2:2) and apocalyptic imagery of darkened sun, moon, and falling stars (Revelation 6:12–13) are the most theologically significant astronomical references in the New Testament.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "astronomy", "isbe": "astronomy"},
        "key_refs": ["Psalms 19:1", "Job 9:9", "Amos 5:8", "Matthew 2:2"],
        "sections": []
    },
    "asuppim": {
        "id": "asuppim",
        "term": "Asuppim",
        "category": "places",
        "intro": "<p>Asuppim (meaning <em>gatherings</em> or <em>storehouses</em>) was the name of the storage chambers or gatehouse at the southern entrance to the temple courts, used for housing materials and equipment related to temple worship (1 Chronicles 26:15, 17). The Revised Version renders it as <em>storehouse</em>. Nehemiah 12:25 mentions it in connection with the gatekeepers who guarded these storerooms after the return from exile.</p>",
        "hitchcock_meaning": "gatherings",
        "source_ids": {"easton": "asuppim"},
        "key_refs": ["1 Chronicles 26:15", "1 Chronicles 26:17", "Nehemiah 12:25"],
        "sections": []
    },
    "atad": {
        "id": "atad",
        "term": "Atad",
        "category": "places",
        "intro": "<p>Atad (meaning <em>buckthorn</em> or <em>a thorn</em>) is the name of the owner of a threshing floor east of the Jordan where the funeral cortege of Jacob paused for seven days of mourning before the final journey to Canaan (Genesis 50:10–11). The Canaanites, seeing the mourning, named the place Abel-mizraim (<em>mourning of Egypt</em>). The site is also mentioned in Judges 9:14–15 in Jotham's parable of the trees, where the bramble (thorn) is invited to be king.</p>",
        "hitchcock_meaning": "a thorn",
        "source_ids": {"easton": "atad", "smith": "atad", "isbe": "atad"},
        "key_refs": ["Genesis 50:10", "Genesis 50:11"],
        "sections": []
    },
    "ataroth": {
        "id": "ataroth",
        "term": "Ataroth",
        "category": "places",
        "intro": "<p>Ataroth (meaning <em>crowns</em>) is the name of several locations in the Old Testament. (1.) A city east of Jordan requested by and assigned to the tribe of Gad (Numbers 32:3, 34). (2.) A town on the border between Ephraim and Benjamin (Joshua 16:2, 7). (3.) Ataroth-adar, a border point of Ephraim (Joshua 16:5; 18:13). (4.) Ataroth-beth-Joab, a place in Judah (1 Chronicles 2:54). The most historically significant is the Gadite Ataroth, mentioned in the Mesha Stele (Moabite Stone) where King Mesha of Moab records recapturing the city from Israel.</p>",
        "hitchcock_meaning": "crowns",
        "source_ids": {"easton": "ataroth", "smith": "ataroth", "isbe": "ataroth"},
        "key_refs": ["Numbers 32:3", "Numbers 32:34", "Joshua 16:2"],
        "sections": []
    },
    "ater": {
        "id": "ater",
        "term": "Ater",
        "category": "people",
        "intro": "<p>Ater (meaning <em>left hand</em> or <em>shut</em>) is the name of three individuals in the post-exilic community. (1.) Ater of Hezekiah, head of a family of ninety-eight men who returned with Zerubbabel (Ezra 2:16; Nehemiah 7:21). (2.) A gatekeeping family of ninety-eight members who returned from Babylon (Ezra 2:42; Nehemiah 7:45). (3.) A leader who sealed the covenant with Nehemiah (Nehemiah 10:17). All three references are genealogical and post-exilic.</p>",
        "hitchcock_meaning": "left hand; shut",
        "source_ids": {"easton": "ater", "smith": "ater", "isbe": "ater"},
        "key_refs": ["Ezra 2:16", "Nehemiah 10:17"],
        "sections": []
    },
    "athaliah": {
        "id": "athaliah",
        "term": "Athaliah",
        "category": "people",
        "intro": "<p>Athaliah (meaning <em>whom God afflicts</em> or <em>the time of the LORD</em>) was the daughter of Ahab and Jezebel, who married Jehoram king of Judah, introducing Baal worship into the southern kingdom. After her son Ahaziah was killed by Jehu, she seized the throne of Judah—the only woman to reign over either kingdom—by massacring all the royal heirs. One infant, Joash (Jehoash), was hidden by the priest Jehoiada and his wife in the temple for six years.</p><p>In her seventh year, Jehoiada staged a coup: Joash was crowned, and Athaliah was led out of the temple and executed. Her six-year reign (circa 841–835 BC) represents the nadir of the Davidic dynasty's continuity and the deepest penetration of Omride influence into Judah.</p>",
        "hitchcock_meaning": "the time of the Lord",
        "source_ids": {"easton": "athaliah", "smith": "athaliah", "isbe": "athaliah"},
        "key_refs": ["2 Kings 11:1", "2 Kings 11:2", "2 Kings 11:16", "2 Kings 11:20"],
        "sections": []
    },
    "athens": {
        "id": "athens",
        "term": "Athens",
        "category": "places",
        "intro": "<p>Athens, capital of Attica and the most celebrated city of the ancient world, was the seat of Greek philosophy, literature, and art at the height of classical civilization. Paul visited it on his second missionary journey after being driven from Beroea (Acts 17:15). He debated in the synagogue and the Agora, and was brought before the Areopagus (Mars' Hill) to present his teaching. His sermon there—beginning with the observation of an altar to <em>an unknown God</em>—is one of the most remarkable examples of contextual apologetics in the New Testament (Acts 17:22–31).</p><p>Though the Athenian response was mixed—some mocked, some deferred, a few believed—the episode produced converts including Dionysius the Areopagite and a woman named Damaris. Paul left Corinth shortly after (1 Thessalonians 3:1).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "athens", "smith": "athens", "isbe": "athens"},
        "key_refs": ["Acts 17:15", "Acts 17:22", "Acts 17:31", "1 Thessalonians 3:1"],
        "sections": []
    },
    "atonement": {
        "id": "atonement",
        "term": "Atonement",
        "category": "concepts",
        "intro": "<p>Atonement (from the English compound <em>at-one-ment</em>) refers in biblical theology to the reconciliation of sinful humanity with God through the removal of guilt and the restoration of fellowship. In the Old Testament the concept is expressed primarily through the sacrificial system: the offerings of Leviticus (4–7), the annual Day of Atonement (Leviticus 16), and the principle that blood makes atonement because life is in the blood (Leviticus 17:11). The Hebrew <em>kipper</em> (to cover or ransom) underlies most OT atonement language.</p><p>In the New Testament, Christ's death is the definitive atoning sacrifice. Paul uses the cognate Greek terms for <em>propitiation</em> and <em>reconciliation</em> (Romans 3:25; 5:11; 2 Corinthians 5:18–21), while Hebrews develops the high-priestly typology: Christ as both the priest and the sacrifice who, entering the heavenly sanctuary once for all, accomplished what the Levitical system could only prefigure (Hebrews 9:11–14; 10:12–14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "atonement", "isbe": "atonement"},
        "key_refs": ["Leviticus 17:11", "Romans 3:25", "Romans 5:11", "Hebrews 9:12", "1 John 2:2"],
        "sections": []
    },
    "atonement-day-of": {
        "id": "atonement-day-of",
        "term": "Atonement, Day of",
        "category": "events",
        "intro": "<p>The Day of Atonement (Hebrew <em>Yom Kippur</em>), observed on the tenth day of Tishri, was the holiest day in the Hebrew calendar—the only fast commanded by the law of Moses. It was the one occasion in the year when the high priest entered the Holy of Holies, first to make atonement for himself and then for the entire nation (Leviticus 16:3–34). The ritual involved two goats: one was slaughtered as a sin offering and its blood sprinkled on the mercy seat; the other—the scapegoat (Azazel)—had the sins of Israel confessed over it and was then driven into the wilderness, symbolically removing iniquity from the camp.</p><p>The New Testament interprets these rites as types of Christ's once-for-all sacrifice: he is simultaneously the priest, the sin offering, and the one who bore away the sins of many (Hebrews 9:7–14; 10:1–4, 19–22).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "atonement-day-of", "isbe": "atonement-day-of"},
        "key_refs": ["Leviticus 16:3", "Leviticus 16:10", "Leviticus 23:27", "Hebrews 9:7"],
        "sections": []
    },
    "augustus": {
        "id": "augustus",
        "term": "Augustus",
        "category": "people",
        "intro": "<p>Augustus (meaning <em>increased</em> or <em>venerable</em>) was the cognomen of Gaius Julius Caesar Octavianus, the first Roman emperor (27 BC – AD 14). He appears in the New Testament as the emperor who issued the decree for a census of the entire Roman world, which brought Mary and Joseph to Bethlehem for the birth of Jesus (Luke 2:1). His long reign transformed the Roman Republic into an empire and established the <em>Pax Romana</em> under which much of early Christianity spread. He is also referenced indirectly through the Augustus band (Acts 27:1) and the coins bearing his image (Luke 20:24).</p>",
        "hitchcock_meaning": "increased; augmented",
        "source_ids": {"easton": "augustus", "smith": "augustus", "isbe": "augustus"},
        "key_refs": ["Luke 2:1", "Acts 27:1"],
        "sections": []
    },
    "augustus-band": {
        "id": "augustus-band",
        "term": "Augustus band",
        "category": "concepts",
        "intro": "<p>The Augustus band (also called the Augustan cohort or Sebaste cohort) was the Roman military unit to which the centurion Julius belonged—the officer in whose charge Paul was placed for the sea voyage to Rome (Acts 27:1). The Greek term <em>Sebastē</em> is the Greek equivalent of the Latin <em>Augusta</em>, the name given to Caesarea Maritima in honor of the emperor. The cohort was likely a detachment of auxiliary troops stationed in Caesarea, possibly serving as an imperial escort force.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "augustus-band", "smith": "augustus-band"},
        "key_refs": ["Acts 27:1"],
        "sections": []
    },
    "ava": {
        "id": "ava",
        "term": "Ava",
        "category": "places",
        "intro": "<p>Ava (also Ivah, meaning <em>iniquity</em>) was a city in Assyria from which colonists were brought by the Assyrians to repopulate Samaria after the deportation of the northern Israelites (2 Kings 17:24). Its inhabitants, the Avites, introduced the worship of their gods Nibhaz and Tartak into Samaria (2 Kings 17:31). The city is possibly identical with the Ava (Ivvah) mentioned alongside Hamath and Sepharvaim in the Assyrian boast to Hezekiah (2 Kings 18:34; Isaiah 37:13), though this identification is not certain.</p>",
        "hitchcock_meaning": "or Ivah, iniquity",
        "source_ids": {"easton": "ava", "smith": "ava", "isbe": "ava"},
        "key_refs": ["2 Kings 17:24", "2 Kings 17:31", "Isaiah 37:13"],
        "sections": []
    },
    "aven": {
        "id": "aven",
        "term": "Aven",
        "category": "places",
        "intro": "<p>Aven (meaning <em>nothingness</em> or <em>vanity</em>) is used by the Hebrew prophets as a polemical name for idolatrous sites. Hosea applies it to Bethel (Beth-aven, <em>house of vanity</em>), mocking Israel's northern sanctuary as a place of worthless idolatry (Hosea 10:8). Amos uses <em>the plain of Aven</em> (Amos 1:5) for the Aramean valley of Damascus. Ezekiel 30:17 applies the term to the Egyptian city of On (Heliopolis), city of the sun-god, as an oracle of judgment.</p>",
        "hitchcock_meaning": "iniquity; force; riches; sorrow",
        "source_ids": {"easton": "aven", "smith": "aven", "isbe": "aven"},
        "key_refs": ["Hosea 10:8", "Amos 1:5", "Ezekiel 30:17"],
        "sections": []
    },
    "avenger-of-blood": {
        "id": "avenger-of-blood",
        "term": "Avenger of blood",
        "category": "concepts",
        "intro": "<p>The avenger of blood (Hebrew <em>gōʾēl haddām</em>) was the nearest male relative of a murder victim, on whom fell the duty and right to execute the killer. The institution was rooted in the principle that innocent blood pollutes the land and demands justice. Moses regulated this practice by establishing six cities of refuge to which an accidental killer could flee; if the avenger caught the killer outside a city of refuge, the killing was lawful (Numbers 35:9–28; Deuteronomy 19:1–13). The accidental killer was required to remain in the city of refuge until the death of the high priest.</p><p>The broader term <em>gōʾēl</em> (kinsman-redeemer) also encompasses the duty to redeem enslaved relatives and to raise up offspring for a deceased brother—the same kinship-obligation in a different context.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "avenger-of-blood"},
        "key_refs": ["Numbers 35:12", "Numbers 35:19", "Deuteronomy 19:6", "Joshua 20:3"],
        "sections": []
    },
    "avim": {
        "id": "avim",
        "term": "Avim",
        "category": "people",
        "intro": "<p>The Avim (also Avites) were an ancient people who inhabited the villages of the southwestern coastal region before the Philistines (Deuteronomy 2:23). The Caphtorim who came from Caphtor destroyed them and settled in their territory. A remnant of the Avites, along with other peoples transplanted from Mesopotamia, was also settled in Samaria by the Assyrians after the fall of the northern kingdom (Joshua 13:3; 2 Kings 17:31).</p>",
        "hitchcock_meaning": "wicked or perverse men",
        "source_ids": {"easton": "avim", "smith": "avim", "isbe": "avim"},
        "key_refs": ["Deuteronomy 2:23", "Joshua 13:3"],
        "sections": []
    },
    "awl": {
        "id": "awl",
        "term": "Awl",
        "category": "concepts",
        "intro": "<p>An awl was a pointed metal or bone instrument used for boring holes, mentioned in Scripture primarily in connection with the law of voluntary permanent servitude. When a Hebrew slave, offered freedom in the seventh year, chose instead to remain permanently in his master's household, his master was to bring him to the door or doorpost and bore through his ear with an awl—a mark of willing, lifelong service (Exodus 21:6; Deuteronomy 15:17). Psalm 40:6 (cited in Hebrews 10:5 in its LXX form as <em>a body you have prepared for me</em>) may allude to the ear-boring rite in the context of willing obedience to God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "awl", "smith": "awl"},
        "key_refs": ["Exodus 21:6", "Deuteronomy 15:17", "Psalms 40:6"],
        "sections": []
    },
    "axe": {
        "id": "axe",
        "term": "Axe",
        "category": "concepts",
        "intro": "<p>Axes in the biblical world served both as woodcutting tools and as weapons of war, made first of stone and later of iron. Several Hebrew and Greek words are rendered <em>axe</em> in English translations. Notable references include: the law prohibiting its use in dressing stones for the altar (Deuteronomy 19:5; 1 Kings 6:7); Abimelech's men cutting branches with axes (Judges 9:48); Elisha's recovery of a borrowed iron axe-head that floated after prayer (2 Kings 6:5–7); and Isaiah's parable of the axe boasting over the one who wields it (Isaiah 10:15). John the Baptist famously uses the axe at the root of the tree as a metaphor for imminent divine judgment (Matthew 3:10; Luke 3:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "axe"},
        "key_refs": ["Deuteronomy 19:5", "Isaiah 10:15", "Matthew 3:10", "2 Kings 6:5"],
        "sections": []
    },
    "azal": {
        "id": "azal",
        "term": "Azal",
        "category": "places",
        "intro": "<p>Azal appears in Zechariah 14:5 in the eschatological vision of the day of the LORD, describing a cataclysmic splitting of the Mount of Olives that would create a great valley through which the survivors would flee—<em>as you fled from the earthquake in the days of Uzziah king of Judah</em>—with the valley extending to Azal. The location is uncertain; some suggest it was very near Jerusalem, others read the Hebrew as an adverb meaning <em>very near</em> rather than a proper name.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "azal", "smith": "azal"},
        "key_refs": ["Zechariah 14:5"],
        "sections": []
    },
    "azariah": {
        "id": "azariah",
        "term": "Azariah",
        "category": "people",
        "intro": "<p>Azariah (meaning <em>whom Jehovah helps</em> or <em>he that hears the Lord</em>) was one of the most common names in the Old Testament, borne by at least twenty-five individuals. The most prominent include: (1.) The high priest who officiated at the dedication of Solomon's temple (1 Kings 4:2; 1 Chronicles 6:9). (2.) The king of Judah also known as Uzziah, son of Amaziah, who reigned fifty-two years and was struck with leprosy for usurping priestly duties (2 Kings 15; 2 Chronicles 26). (3.) Azariah the prophet who encouraged King Asa's reform (2 Chronicles 15:1–8). (4.) One of Daniel's three companions given the Babylonian name Abednego (Daniel 1:6–7), who survived the fiery furnace.</p>",
        "hitchcock_meaning": "he that hears the Lord",
        "source_ids": {"easton": "azariah", "smith": "azariah", "isbe": "azariah"},
        "key_refs": ["1 Kings 4:2", "2 Chronicles 26:19", "Daniel 1:6", "2 Chronicles 15:1"],
        "sections": []
    },
    "azazel": {
        "id": "azazel",
        "term": "Azazel",
        "category": "concepts",
        "intro": "<p>Azazel is a Hebrew term appearing three times in Leviticus 16 (verses 8, 10, 26), where it designates the second of the two goats in the Day of Atonement ritual—the one over which the high priest confessed Israel's sins before it was driven into the wilderness. The Authorized Version renders it <em>scapegoat</em>; the Revised Version and most modern translations transliterate it as Azazel.</p><p>Its meaning is disputed: some interpreters understand it as a place (a remote wilderness area), others as a descriptor (<em>the goat that departs</em> or <em>entire removal</em>), and others as the name of a demonic figure inhabiting the desert. Theologically, the rite is understood as a dramatic enactment of the removal of sin from the community: the two goats together—one slaughtered, one sent away—symbolize both the atoning death and the complete bearing away of guilt that are united in Christ's work.</p>",
        "hitchcock_meaning": "the scape-goat",
        "source_ids": {"easton": "azazel", "isbe": "azazel"},
        "key_refs": ["Leviticus 16:8", "Leviticus 16:10", "Leviticus 16:26"],
        "sections": []
    },
    "azaziah": {
        "id": "azaziah",
        "term": "Azaziah",
        "category": "people",
        "intro": "<p>Azaziah (meaning <em>whom Jehovah strengthened</em> or <em>strength of the Lord</em>) is the name of three men in the Old Testament: (1.) A Levite musician who played the harp in the procession that brought the ark to Jerusalem under David (1 Chronicles 15:21). (2.) The father of Hoshea, who was the leader of Ephraim during David's reign (1 Chronicles 27:20). (3.) A Levite overseer of the temple offerings under Hezekiah's reformation (2 Chronicles 31:13).</p>",
        "hitchcock_meaning": "strength of the Lord",
        "source_ids": {"easton": "azaziah", "smith": "azaziah", "isbe": "azaziah"},
        "key_refs": ["1 Chronicles 15:21", "1 Chronicles 27:20", "2 Chronicles 31:13"],
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
    print(f'BP a5: Aretas → Azaziah: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
