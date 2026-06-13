"""
BP Article Synthesis — b2: Bartholomew → Berechiah
Covers Easton entries: Bartholomew through Berechiah (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-b2.py
Run: python3 scripts/bp-b2.py
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
    "bartholomew": {
        "id": "bartholomew",
        "term": "Bartholomew",
        "category": "people",
        "intro": "<p>Bartholomew (meaning <em>son of Tolmai</em>) was one of the twelve apostles of Jesus, listed in all three Synoptic Gospels and in Acts (Matthew 10:3; Mark 3:18; Luke 6:14; Acts 1:13). He is consistently paired with Philip in the apostolic lists. Many scholars identify him with Nathanael of Cana, the disciple Philip brought to Jesus in John 1:45–51, since Nathanael appears where Bartholomew would be expected in John's Gospel. Tradition holds that he carried the gospel to Armenia and India; he is venerated as a martyr.</p>",
        "hitchcock_meaning": "a son that suspends the waters",
        "source_ids": {"easton": "bartholomew", "smith": "bartholomew", "isbe": "bartholomew"},
        "key_refs": ["Matthew 10:3", "John 1:45", "John 1:46", "Acts 1:13"],
        "sections": []
    },
    "bartimaeus": {
        "id": "bartimaeus",
        "term": "Bartimaeus",
        "category": "people",
        "intro": "<p>Bartimaeus (meaning <em>son of Timaeus</em>) was a blind beggar sitting by the roadside near Jericho who cried out to Jesus as <em>Son of David</em> as he passed. Despite being rebuked by the crowd, his persistent appeals moved Jesus to call him, ask what he wanted, and restore his sight in response to his faith (Mark 10:46–52; cf. Matthew 20:30). Mark alone names him and his father, suggesting he was known to the early Christian community. His healing is the last miracle Jesus performed before his entry into Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bartimaeus", "smith": "bartimaeus", "isbe": "bartimaeus"},
        "key_refs": ["Mark 10:46", "Mark 10:52", "Matthew 20:30"],
        "sections": []
    },
    "baruch": {
        "id": "baruch",
        "term": "Baruch",
        "category": "people",
        "intro": "<p>Baruch (meaning <em>blessed</em>) was the devoted secretary and companion of the prophet Jeremiah, of the tribe of Judah. He transcribed Jeremiah's dictated oracles onto a scroll (Jeremiah 36:4), read them publicly in the temple, and preserved and transmitted them when Jehoiakim burned the original scroll. He witnessed the purchase of Jeremiah's field at Anathoth as a sign of future restoration (Jeremiah 32:12). God granted him a personal oracle of comfort amid the catastrophe of Jerusalem's fall (Jeremiah 45).</p><p>Baruch appears in the post-exilic period as a signatory of the covenant renewal under Nehemiah (Nehemiah 10:6). The deuterocanonical Book of Baruch, attributed to him, is regarded as scriptural by Roman Catholic and Eastern Orthodox Christians but not by Protestants.</p>",
        "hitchcock_meaning": "who is blessed",
        "source_ids": {"easton": "baruch", "smith": "baruch", "isbe": "baruch"},
        "key_refs": ["Jeremiah 36:4", "Jeremiah 32:12", "Jeremiah 45:5", "Nehemiah 10:6"],
        "sections": []
    },
    "barzillai": {
        "id": "barzillai",
        "term": "Barzillai",
        "category": "people",
        "intro": "<p>Barzillai (meaning <em>of iron</em> or <em>son of contempt</em>) is the name of three men in the Old Testament. (1.) Barzillai the Meholathite, whose son Adriel married Merab, Saul's daughter (2 Samuel 21:8). (2.) Barzillai the Gileadite of Rogelim, a wealthy man of eighty who provided food and supplies for David when he fled Absalom's rebellion; David invited him to Jerusalem but he declined on account of his age, sending his son Chimham instead. On his deathbed David charged Solomon to show kindness to Barzillai's sons (1 Kings 2:7). (3.) A priest whose genealogy was lost because he had taken his wife's name from the priestly family of Barzillai (Ezra 2:61).</p>",
        "hitchcock_meaning": "son of contempt; made of iron",
        "source_ids": {"easton": "barzillai", "smith": "barzillai", "isbe": "barzillai"},
        "key_refs": ["2 Samuel 17:27", "2 Samuel 19:31", "1 Kings 2:7", "Ezra 2:61"],
        "sections": []
    },
    "bashan": {
        "id": "bashan",
        "term": "Bashan",
        "category": "places",
        "intro": "<p>Bashan (meaning <em>light soil</em> or <em>smooth, fertile plain</em>) was the broad, fertile territory east of the Jordan and northeast of Gilead, corresponding roughly to the modern Hauran plateau and Golan Heights. It was renowned in antiquity for its oak forests, its fat cattle, and its grain—a proverbial image of lush abundance (Deuteronomy 32:14; Amos 4:1; Ezekiel 39:18). Before the Israelite conquest it was the kingdom of Og, whose defeat by Moses is recorded in Numbers 21:33 and Deuteronomy 3. After the conquest, Bashan was divided between the half-tribe of Manasseh, Reuben, and Gad. Its bulls and rams appear as metaphors for powerful enemies in the Psalms (Psalm 22:12; 68:15).</p>",
        "hitchcock_meaning": "in the tooth; in ivory",
        "source_ids": {"easton": "bashan", "smith": "bashan", "isbe": "bashan"},
        "key_refs": ["Numbers 21:33", "Deuteronomy 3:1", "Psalms 22:12", "Amos 4:1"],
        "sections": []
    },
    "bashan-hill-of": {
        "id": "bashan-hill-of",
        "term": "Bashan, Hill of",
        "category": "places",
        "intro": "<p>The hill of Bashan is mentioned in Psalm 68:15 alongside the phrase <em>many-peaked mountain</em> and is generally understood to refer to Mount Hermon, the great snow-capped peak north of Bashan that dominates the horizon of the region. The psalm contrasts this impressive mountain with Zion, the hill God has chosen as his dwelling—a theological statement about divine election over natural grandeur.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bashan-hill-of"},
        "key_refs": ["Psalms 68:15"],
        "sections": []
    },
    "bashan-havoth-jair": {
        "id": "bashan-havoth-jair",
        "term": "Bashan-havoth-jair",
        "category": "places",
        "intro": "<p>Bashan-havoth-jair (meaning <em>the Bashan of the tent-villages of Jair</em>) was the name given to the region of Argob in northern Bashan by Jair son of Manasseh, who captured sixty cities there after the conquest (Deuteronomy 3:14). The name refers to the sixty unwalled towns or tent-villages—<em>havoth</em>—he settled. The same territory later formed part of the administrative district of Ben-geber under Solomon (1 Kings 4:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bashan-havoth-jair"},
        "key_refs": ["Deuteronomy 3:14", "Joshua 13:30", "1 Kings 4:13"],
        "sections": []
    },
    "bashemath": {
        "id": "bashemath",
        "term": "Bashemath",
        "category": "people",
        "intro": "<p>Bashemath (meaning <em>sweet-smelling</em> or <em>perfumed</em>) is the name of two or three women in the Esau narratives. (1.) A daughter of Ishmael and the last wife of Esau, also called Mahalath (Genesis 36:3; cf. 28:9), who became the mother of Reuel. (2.) A daughter of Elon the Hittite, also named among Esau's wives (Genesis 26:34). The apparent discrepancies in naming Esau's wives reflect the complexity of the Genesis sources. Bashemath is also mentioned as the name of a daughter of Solomon who married Ahimaaz (1 Kings 4:15).</p>",
        "hitchcock_meaning": "perfumed; confusion of death; in desolation",
        "source_ids": {"easton": "bashemath", "smith": "bashemath"},
        "key_refs": ["Genesis 36:3", "Genesis 36:4", "Genesis 26:34"],
        "sections": []
    },
    "basilisk": {
        "id": "basilisk",
        "term": "Basilisk",
        "category": "concepts",
        "intro": "<p>The basilisk is the Revised Version's rendering of the Hebrew <em>tsepha</em> or <em>tsiphoni</em> in Isaiah 11:8; 14:29; 59:5; and Jeremiah 8:17, where the Authorized Version uses <em>cockatrice</em>. It denotes a highly venomous snake, probably a specific species of viper. In Isaiah's vision of the messianic age, the nursing child will play safely over the basilisk's den (Isaiah 11:8)—a vivid image of restored harmony. Isaiah 14:29 and 59:5 use the creature as a metaphor for deadly danger, and Jeremiah 8:17 employs it as an image of inescapable divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "basilisk", "isbe": "basilisk"},
        "key_refs": ["Isaiah 11:8", "Isaiah 14:29", "Isaiah 59:5", "Jeremiah 8:17"],
        "sections": []
    },
    "basin": {
        "id": "basin",
        "term": "Basin",
        "category": "concepts",
        "intro": "<p>Several Hebrew words are rendered <em>basin</em> (or <em>bason</em>) in the English Bible, covering a range of vessels used for washing, for catching blood in sacrifice, and for temple service. The large bronze <em>lavers</em> in the tabernacle and temple were used for priestly washing (Exodus 30:18; 1 Kings 7:38). David prepared gold and silver basins for the temple treasury (1 Chronicles 28:17). At the Last Supper Jesus used a basin (<em>niptēr</em>) to wash the disciples' feet (John 13:5)—an act of servant leadership that reinterpreted the washbasin's ritual associations.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "basin", "smith": "basin"},
        "key_refs": ["Exodus 24:6", "John 13:5", "1 Chronicles 28:17"],
        "sections": []
    },
    "basket": {
        "id": "basket",
        "term": "Basket",
        "category": "concepts",
        "intro": "<p>Baskets in Scripture represent a variety of woven containers used for carrying food, offerings, and goods. Five distinct Hebrew words are translated <em>basket</em>, differing in size and material. In Joseph's narrative, the chief baker's dream featured three baskets of bread (Genesis 40:16–18). The offering of firstfruits was presented in a basket before the LORD (Deuteronomy 26:2–4). Moses was placed in a basket of bulrushes (Exodus 2:3). In the New Testament, the disciples gathered twelve basketfuls of fragments after the feeding of the five thousand (Matthew 14:20), and Paul escaped Damascus in a basket lowered over the city wall (Acts 9:25; 2 Corinthians 11:33).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "basket", "smith": "basket", "isbe": "basket"},
        "key_refs": ["Genesis 40:16", "Deuteronomy 26:2", "Matthew 14:20", "Acts 9:25"],
        "sections": []
    },
    "bastard": {
        "id": "bastard",
        "term": "Bastard",
        "category": "concepts",
        "intro": "<p>The word <em>bastard</em> in the Authorized Version translates the Hebrew <em>mamzer</em>, meaning <em>polluted</em>, in Deuteronomy 23:2, where it denotes one of illegitimate or mixed birth excluded from the assembly of the LORD to the tenth generation. In Zechariah 9:6 it is used of the mixed population that would inhabit Ashdod. The New Testament's sole use (Hebrews 12:8) applies the Greek <em>nothos</em> metaphorically: those who are not disciplined by God are illegitimate children rather than true sons—a reversal of the stigma, making discipline a mark of authentic sonship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bastard", "smith": "bastard"},
        "key_refs": ["Deuteronomy 23:2", "Zechariah 9:6", "Hebrews 12:8"],
        "sections": []
    },
    "bastinado": {
        "id": "bastinado",
        "term": "Bastinado",
        "category": "concepts",
        "intro": "<p>Bastinado—beating with a rod or stick—was a common form of corporal punishment in the ancient Near East and the Greco-Roman world. Mosaic law permitted flogging as a judicial penalty, limiting it to forty stripes (Deuteronomy 25:2–3). Proverbs frequently commends the rod for correcting the foolish (Proverbs 22:15; 26:3). The New Testament records Paul's three beatings with rods by Roman lictors (2 Corinthians 11:25; Acts 16:22–23), a punishment that was technically illegal to inflict on a Roman citizen.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bastinado"},
        "key_refs": ["Deuteronomy 25:2", "Proverbs 22:15", "Acts 16:22", "2 Corinthians 11:25"],
        "sections": []
    },
    "bat": {
        "id": "bat",
        "term": "Bat",
        "category": "concepts",
        "intro": "<p>The bat (Hebrew <em>ataleph</em>) is listed among the unclean birds in the Mosaic food laws (Leviticus 11:19; Deuteronomy 14:18)—its classification with birds reflecting ancient taxonomy based on flight rather than modern zoology. Isaiah 2:20 uses the bat evocatively in the eschatological vision of the day of the LORD: idolaters will throw their silver and gold idols to the moles and bats when they flee in terror into caves and rocky crags before the divine majesty. The bat thus becomes an image of darkness, worthlessness, and the reversal of false worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bat", "smith": "bat"},
        "key_refs": ["Leviticus 11:19", "Deuteronomy 14:18", "Isaiah 2:20"],
        "sections": []
    },
    "bath": {
        "id": "bath",
        "term": "Bath",
        "category": "concepts",
        "intro": "<p>The bath was the standard Hebrew liquid measure, equal to one-tenth of a homer (Ezekiel 45:11, 14). Estimates of its capacity range from approximately five to nine modern gallons (roughly 20–40 liters). Solomon's bronze sea in the temple held two thousand baths (1 Kings 7:26), and each of the ten moveable lavers held forty baths (1 Kings 7:38). The bath's equivalent for dry measure was the ephah. The term is also used figuratively in Ezekiel 45:10–14 in the context of just commercial weights and measures, as part of a vision of restored equity in the ideal commonwealth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bath", "smith": "bath"},
        "key_refs": ["1 Kings 7:26", "1 Kings 7:38", "Ezekiel 45:10", "Ezekiel 45:14"],
        "sections": []
    },
    "bath-rabbim": {
        "id": "bath-rabbim",
        "term": "Bath-rabbim",
        "category": "places",
        "intro": "<p>Bath-rabbim (meaning <em>daughter of many</em>) was a gate of the ancient Ammonite city of Heshbon, east of the Jordan, near which were pools. It is mentioned only in the Song of Solomon 7:4, where the beloved's eyes are compared to the pools by the gate of Bath-rabbim—an image of depth, clarity, and beauty. The pools at Heshbon may have been the city's reservoirs. No historical event is associated with the name.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bath-rabbim"},
        "key_refs": ["Song of Solomon 7:4"],
        "sections": []
    },
    "bath-sheba": {
        "id": "bath-sheba",
        "term": "Bath-sheba",
        "category": "people",
        "intro": "<p>Bath-sheba (meaning <em>daughter of the oath</em> or <em>daughter of seven</em>, also called Bath-shua in 1 Chronicles 3:5) was the daughter of Eliam and wife of Uriah the Hittite, whom David saw bathing and took into his household in an act of adultery, subsequently arranging Uriah's death in battle. The prophet Nathan confronted David with a parable that led to his repentance (Psalm 51). Their first child died, but their second son was Solomon.</p><p>After David's death, Bath-sheba played a decisive role in securing Solomon's succession over Adonijah, acting as the queen mother whose intercession had direct access to the throne. She is listed in Jesus's genealogy in Matthew 1:6 as <em>the wife of Uriah</em>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bath-sheba", "isbe": "bath-sheba"},
        "key_refs": ["2 Samuel 11:3", "2 Samuel 12:24", "1 Kings 1:11", "Matthew 1:6"],
        "sections": []
    },
    "baths": {
        "id": "baths",
        "term": "Baths",
        "category": "concepts",
        "intro": "<p>Bathing was frequent among the Hebrews for both hygienic and ritual purposes. Ritual bathing was required for purification from various forms of uncleanness—after contact with a corpse, after childbirth, after discharge, and for priests before service (Leviticus 14:8; Numbers 19:19; Exodus 30:20). The pools and baths used for ritual purification (<em>mikveh</em>) had specific requirements for water source. In Egypt, where the Hebrews lived, regular bathing was also customary (Exodus 2:5). Jesus's washing of the disciples' feet at the Last Supper drew on the imagery of bathing as a sign of cleansing and prepared them for the greater cleansing of forgiveness (John 13:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baths"},
        "key_refs": ["Leviticus 14:8", "Numbers 19:19", "John 13:10"],
        "sections": []
    },
    "battering-ram": {
        "id": "battering-ram",
        "term": "Battering-ram",
        "category": "concepts",
        "intro": "<p>The battering-ram was the principal siege weapon of the ancient Near East, used to break through city gates and walls. Ezekiel 4:2 and 21:22 describe its use in the context of the Babylonian siege of Jerusalem—Nebuchadnezzar is depicted consulting omens at the crossroads to decide whether to attack Jerusalem or Rabbath-ammon, ultimately directing his battering-rams against Jerusalem's gates. The ram typically consisted of a heavy beam of wood with a metal head, suspended in a wheeled frame and swung by ropes against the fortification. Reliefs from Assyrian palaces depict their use in detail.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "battering-ram", "isbe": "battering-ram"},
        "key_refs": ["Ezekiel 4:2", "Ezekiel 21:22"],
        "sections": []
    },
    "battle-axe": {
        "id": "battle-axe",
        "term": "Battle-axe",
        "category": "concepts",
        "intro": "<p>The battle-axe (or war-club, Hebrew <em>mappets</em>) is mentioned in Jeremiah 51:20 in a metaphorical address to Cyrus (or Babylon) as God's <em>war club and weapon of battle</em>—the instrument by which the LORD smashes nations and kingdoms. The weapon in its literal form was a heavy mallet or bronze-headed club used in close combat. In the figurative sense of Jeremiah, divine judgment is the ultimate battle-axe that breaks the pride of empire.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "battle-axe", "isbe": "battle-axe"},
        "key_refs": ["Jeremiah 51:20"],
        "sections": []
    },
    "battle-bow": {
        "id": "battle-bow",
        "term": "Battle-bow",
        "category": "concepts",
        "intro": "<p>The battle-bow was the war-bow used in combat, distinguished from the hunting bow. Zechariah 9:10 announces the messianic king's abolition of the battle-bow, chariot, and war-horse as part of his proclamation of peace to the nations. Zechariah 10:4 uses the battle-bow as a metaphor for the rulers and warriors who will come from Judah in the day of restoration. The breaking of the battle-bow appears repeatedly in prophetic literature as a sign of disarmament under divine sovereignty (Hosea 1:5; Psalm 46:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "battle-bow", "isbe": "battle-bow"},
        "key_refs": ["Zechariah 9:10", "Zechariah 10:4", "Hosea 1:5"],
        "sections": []
    },
    "battlement": {
        "id": "battlement",
        "term": "Battlement",
        "category": "concepts",
        "intro": "<p>A battlement was a low parapet wall or balustrade enclosing the flat roof of an Israelite house, required by Mosaic law to be built to prevent accidental deaths (Deuteronomy 22:8)—an early building safety regulation. City walls were also topped with battlements for defensive purposes. Jeremiah 5:10 uses the image metaphorically when he commands the invaders to break down Jerusalem's battlements, for they do not belong to the LORD.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "battlement", "smith": "battlement", "isbe": "battlement"},
        "key_refs": ["Deuteronomy 22:8", "Jeremiah 5:10"],
        "sections": []
    },
    "bay": {
        "id": "bay",
        "term": "Bay",
        "category": "places",
        "intro": "<p>Bay in the Authorized Version denotes the northern estuary of the Dead Sea at the mouth of the Jordan River (Joshua 15:5; 18:19), used as a boundary marker for the tribes of Judah and Benjamin. The same Hebrew word (<em>lashon</em>, <em>tongue</em>) is used in Isaiah 11:15 for the tongue-shaped gulf of the Red Sea (the Gulf of Suez), which God promises to dry up in the eschatological return of the exiles. Zechariah 6:3, 7 uses the word differently, describing the dappled (or bay-coloured) horses of the prophetic visions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bay"},
        "key_refs": ["Joshua 15:5", "Joshua 18:19", "Isaiah 11:15"],
        "sections": []
    },
    "bay-tree": {
        "id": "bay-tree",
        "term": "Bay-tree",
        "category": "concepts",
        "intro": "<p>The bay-tree appears only in Psalm 37:35 in the Authorized Version, where the wicked are compared to a <em>green bay-tree</em> spreading in its native soil—an image of vigorous, well-rooted prosperity. The Hebrew word (<em>ezrach</em>) more literally means <em>a native tree</em> or <em>a tree grown in its own soil</em>, and the Revised Version renders it accordingly. The precise species is uncertain; the image emphasizes the temporary and self-satisfied flourishing of the ungodly before divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bay-tree", "smith": "bay-tree"},
        "key_refs": ["Psalms 37:35"],
        "sections": []
    },
    "bdellium": {
        "id": "bdellium",
        "term": "Bdellium",
        "category": "concepts",
        "intro": "<p>Bdellium (Hebrew <em>bedolah</em>) is mentioned in Genesis 2:12 as one of the products of the land of Havilah, alongside gold and onyx stone. In Numbers 11:7 the appearance of manna is compared to it. The word may refer to a fragrant resin (bdellium gum, from an Arabian shrub), a pearl, or possibly a crystal or other translucent substance; ancient translators and modern scholars differ. Its association with gold and precious stone in Genesis suggests something of value, while its comparison to manna in Numbers points to a pale, whitish appearance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bdellium", "smith": "bdellium"},
        "key_refs": ["Genesis 2:12", "Numbers 11:7"],
        "sections": []
    },
    "beacon": {
        "id": "beacon",
        "term": "Beacon",
        "category": "concepts",
        "intro": "<p>A beacon in the biblical sense was a pole or mast (<em>to'ren</em>) erected on a mountaintop or prominent point as a signal, rallying standard, or warning (Isaiah 30:17; 33:23; Ezekiel 27:5). The term is related to the word for a ship's mast. Isaiah 30:17 uses it in a warning that Judah's army will be reduced to so few that the survivors will be as conspicuous and isolated as a solitary beacon on a hilltop—a stark image of defeat and desolation. Beacons of fire were also used across the ancient Near East to send rapid military communications.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beacon", "smith": "beacon"},
        "key_refs": ["Isaiah 30:17", "Isaiah 33:23"],
        "sections": []
    },
    "bealiah": {
        "id": "bealiah",
        "term": "Bealiah",
        "category": "people",
        "intro": "<p>Bealiah (meaning <em>whose Lord is Jehovah</em>) was a Benjamite, one of the thirty mighty men who came to David at Ziklag while he was still under Philistine pressure from Saul. He is described as skilled with both right and left hand in slinging stones and shooting arrows (1 Chronicles 12:5). His name, unusual for its theophoric form, is the only information Scripture records about him.</p>",
        "hitchcock_meaning": "the god of an idol; in an assembly",
        "source_ids": {"easton": "bealiah", "smith": "bealiah"},
        "key_refs": ["1 Chronicles 12:5"],
        "sections": []
    },
    "bealoth": {
        "id": "bealoth",
        "term": "Bealoth",
        "category": "places",
        "intro": "<p>Bealoth (meaning <em>citizens</em> or <em>mistresses</em>) was a town in the extreme south of Judah (Joshua 15:24), in the Negev district. It is also mentioned in 1 Kings 4:16 in connection with one of Solomon's administrative districts, possibly as a different location in the north of Israel (Aloth). The Judean Bealoth may be identified with the village of Khirbet Ghazzeh in the Negev.</p>",
        "hitchcock_meaning": "cast under",
        "source_ids": {"easton": "bealoth", "smith": "bealoth"},
        "key_refs": ["Joshua 15:24", "1 Kings 4:16"],
        "sections": []
    },
    "beam": {
        "id": "beam",
        "term": "Beam",
        "category": "concepts",
        "intro": "<p>Beam renders several Hebrew and Greek words in Scripture, covering structural timbers in buildings, the bar of a loom, and the shaft of a spear. Goliath's spear shaft is compared to a weaver's beam in 1 Samuel 17:7—a vivid indication of its massive size. The floating iron axe-head recovered from the Jordan River (2 Kings 6:5–7) came from beams being cut for the sons of the prophets' building project. Jesus's use of the beam (<em>dokos</em>) and speck (<em>karphos</em>) in Matthew 7:3–5 is one of his most memorable images of self-deception, warning against condemning others' minor faults while blind to one's own major failures.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beam", "isbe": "beam"},
        "key_refs": ["1 Samuel 17:7", "2 Kings 6:2", "Matthew 7:3", "Matthew 7:5"],
        "sections": []
    },
    "beans": {
        "id": "beans",
        "term": "Beans",
        "category": "concepts",
        "intro": "<p>Beans (Hebrew <em>pol</em>) are mentioned twice in the Old Testament. In 2 Samuel 17:28 they are among the provisions—with wheat, barley, flour, parched grain, honey, curds, sheep, and cheese—that Barzillai and others brought to David and his men in the wilderness during Absalom's rebellion. Ezekiel 4:9 includes beans among the mixed grains used to make bread in the prophet's enacted siege-ration symbolism. Beans were a staple food for common people throughout the ancient Near East, providing protein particularly in lean times.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beans", "smith": "beans"},
        "key_refs": ["2 Samuel 17:28", "Ezekiel 4:9"],
        "sections": []
    },
    "bear": {
        "id": "bear",
        "term": "Bear",
        "category": "concepts",
        "intro": "<p>The bear (Hebrew <em>dob</em>) was native to the mountain regions of ancient Palestine and the broader Near East. It is mentioned frequently in both literal and figurative contexts. David killed a bear that attacked his flock, demonstrating the courage that led him to face Goliath (1 Samuel 17:34–37). Two bears mauled the youths who mocked Elisha at Bethel (2 Kings 2:24). In prophetic imagery, the bear represents ferocity and unpredictability: a bereaved she-bear is the most dangerous animal known (Proverbs 17:12; 2 Samuel 17:8; Hosea 13:8). Daniel's vision depicts Persia as a bear (Daniel 7:5), and Revelation 13:2 applies the same image to the beast from the sea.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bear", "smith": "bear"},
        "key_refs": ["1 Samuel 17:34", "2 Kings 2:24", "Proverbs 17:12", "Daniel 7:5"],
        "sections": []
    },
    "beard": {
        "id": "beard",
        "term": "Beard",
        "category": "concepts",
        "intro": "<p>The beard held great social and religious significance in biblical culture. Israelite law prohibited trimming the edges of the beard (Leviticus 19:27; 21:5), a prohibition likely directed against mourning rites or pagan practices. Shaving or plucking the beard was a sign of deep mourning and humiliation (Isaiah 15:2; Jeremiah 41:5; 48:37; Ezra 9:3). The anointing oil flowing down Aaron's beard at his consecration is a poetic image of divine blessing and priestly unity in Psalm 133:2. When Hanun humiliated David's ambassadors by shaving half their beards (2 Samuel 10:4), it was an act of deliberate cultural provocation that precipitated war.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beard", "smith": "beard"},
        "key_refs": ["Leviticus 19:27", "Psalms 133:2", "2 Samuel 10:4", "Isaiah 15:2"],
        "sections": []
    },
    "beast": {
        "id": "beast",
        "term": "Beast",
        "category": "concepts",
        "intro": "<p>Beast in the Bible covers multiple categories of animal. As a broad term it includes domestic cattle and herds (Exodus 22:5; Numbers 20:4), wild animals (Leviticus 26:22; Daniel 4:12), and the full range of living creatures. In apocalyptic literature the term takes on symbolic weight: Daniel's four beasts from the sea represent successive world empires (Daniel 7); Revelation's beast from the sea (chapter 13) and beast from the earth (the false prophet) are agents of anti-Christian power in the end times. The number of the beast (666; Revelation 13:18) has generated extensive interpretive discussion across church history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beast", "isbe": "beast"},
        "key_refs": ["Daniel 7:3", "Revelation 13:1", "Revelation 13:18", "Revelation 19:20"],
        "sections": []
    },
    "beaten-gold": {
        "id": "beaten-gold",
        "term": "Beaten Gold",
        "category": "concepts",
        "intro": "<p>Beaten gold refers to gold worked by hammering rather than casting—a technique producing both decorative sheet metal and rounded or embossed forms. The golden lampstand (menorah) in the tabernacle was made of <em>beaten work</em> (Numbers 8:4), meaning its branches and cups were hammered out from a single piece of pure gold rather than assembled from cast components. Solomon's two hundred large and three hundred small shields of beaten gold were displayed in the House of the Forest of Lebanon (1 Kings 10:16–17), representing both artisanal skill and royal wealth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beaten-gold", "isbe": "beaten-gold"},
        "key_refs": ["Numbers 8:4", "1 Kings 10:16", "1 Kings 10:17"],
        "sections": []
    },
    "beaten-oil": {
        "id": "beaten-oil",
        "term": "Beaten Oil",
        "category": "concepts",
        "intro": "<p>Beaten oil (Hebrew <em>shemen kathith</em>) was the finest grade of olive oil, obtained by beating or crushing ripe olives in a mortar rather than pressing them in an olive press. This process yielded a pure, clear oil free of sediment. It was required for the perpetual lamp in the tabernacle (Exodus 27:20; Leviticus 24:2) and for the daily grain offering (Exodus 29:40; Numbers 28:5). Its superior purity made it the prescribed oil for the sanctuary's holiest uses.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beaten-oil", "isbe": "beaten-oil"},
        "key_refs": ["Exodus 27:20", "Exodus 29:40", "Leviticus 24:2"],
        "sections": []
    },
    "beautiful-gate": {
        "id": "beautiful-gate",
        "term": "Beautiful Gate",
        "category": "places",
        "intro": "<p>The Beautiful Gate was one of the entrances to the Jerusalem temple complex, mentioned in Acts 3:2 as the place where Peter and John encountered the man lame from birth who begged for alms. Most scholars identify it with the Nicanor Gate, a magnificent bronze gate on the eastern side of the Court of Women—an identification supported by Josephus, who describes it as far surpassing the silver and gold doors of the temple. It was here that Peter declared, <em>Silver and gold have I none, but what I have I give you: in the name of Jesus Christ of Nazareth, rise up and walk</em> (Acts 3:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beautiful-gate", "isbe": "beautiful-gate"},
        "key_refs": ["Acts 3:2", "Acts 3:6", "Acts 3:10"],
        "sections": []
    },
    "becher": {
        "id": "becher",
        "term": "Becher",
        "category": "people",
        "intro": "<p>Becher (meaning <em>first-born</em> or <em>young camel</em>) is the name of two men in the Old Testament. (1.) The second son of Benjamin (Genesis 46:21), also called Bered in 1 Chronicles 7:20, whose descendants are listed as the Bachrites (Numbers 26:35). (2.) A son of Ephraim (1 Chronicles 7:20), from whose lineage the Ephraimite line descended. The dual occurrence of the name reflects its use across different tribal genealogies.</p>",
        "hitchcock_meaning": "first begotten; first fruits",
        "source_ids": {"easton": "becher", "smith": "becher", "isbe": "becher"},
        "key_refs": ["Genesis 46:21", "Numbers 26:35", "1 Chronicles 7:20"],
        "sections": []
    },
    "bed": {
        "id": "bed",
        "term": "Bed",
        "category": "concepts",
        "intro": "<p>Beds in ancient Israel ranged from simple reed mats on the floor to elevated couches with carved frames, depending on social status. The Hebrew <em>mittah</em> denotes the sleeping couch (Exodus 8:3), while the rich used beds of ivory inlaid with gold (Amos 6:4), condemned by Amos as a sign of decadent luxury. Saul's bed in 1 Samuel 19:13 was used by Michal to deceive his messengers with a household idol. Jesus's healings frequently involved commanding the healed person to take up their mat and walk (John 5:8; Mark 2:11), reversing the disability that had confined them to bed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bed", "smith": "bed"},
        "key_refs": ["Exodus 8:3", "Amos 6:4", "Mark 2:11", "John 5:8"],
        "sections": []
    },
    "bed-chamber": {
        "id": "bed-chamber",
        "term": "Bed-chamber",
        "category": "concepts",
        "intro": "<p>The bed-chamber in Eastern houses was typically a slightly elevated platform at the upper end of the main room, or a separate inner room. References include: Elisha's provision of a small upper chamber as a guest room in Shunem (2 Kings 4:10); the bed-chamber as a place of private conspiracy in 2 Kings 6:12, where the Syrian king suspected a spy revealing his plans; and the hiding of the infant Joash from Athaliah in a bed-chamber of the temple (2 Kings 11:2). Ecclesiastes 10:20 warns against cursing the king even in your bedroom—an expression of the reach of royal surveillance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bed-chamber"},
        "key_refs": ["2 Kings 4:10", "2 Kings 6:12", "2 Kings 11:2"],
        "sections": []
    },
    "bedan": {
        "id": "bedan",
        "term": "Bedan",
        "category": "people",
        "intro": "<p>Bedan is mentioned in 1 Samuel 12:11 as one of the judges God sent to deliver Israel—alongside Jerubbaal (Gideon), Jephthah, and Samuel—in Samuel's farewell address. His identity is uncertain: some identify him with Abdon (Judges 12:13), the judge from Pirathon; others with Barak. He is also the name of a son of Ulam of the tribe of Manasseh (1 Chronicles 7:17). The reference in Samuel is significant as an example of divine deliverance through judges in response to Israel's repentance.</p>",
        "hitchcock_meaning": "according to judgment",
        "source_ids": {"easton": "bedan", "smith": "bedan", "isbe": "bedan"},
        "key_refs": ["1 Samuel 12:11"],
        "sections": []
    },
    "bedstead": {
        "id": "bedstead",
        "term": "Bedstead",
        "category": "concepts",
        "intro": "<p>The most notable bedstead in Scripture is the iron bedstead of Og king of Bashan, preserved at Rabbath-ammon and measuring nine cubits long by four cubits wide (approximately 13–14 feet by 6 feet), cited as proof of Og's gigantic stature (Deuteronomy 3:11). This detail was long preserved as a monument to Israel's great conquest east of the Jordan. The word translated <em>bedstead</em> may also refer to a sarcophagus or funerary couch in Og's case. Elsewhere the same Hebrew word is rendered <em>couch</em> or <em>bed</em>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bedstead", "isbe": "bedstead"},
        "key_refs": ["Deuteronomy 3:11"],
        "sections": []
    },
    "bee": {
        "id": "bee",
        "term": "Bee",
        "category": "concepts",
        "intro": "<p>Bees are mentioned several times in Scripture, reflecting their abundance in ancient Palestine. The danger of wild bee swarms is evoked in Deuteronomy 1:44 and Psalm 118:12, where enemies surround the speaker like bees. Samson found a swarm of bees and honey in the carcass of the lion he had slain—the basis of his famous riddle (Judges 14:8–18). Isaiah 7:18 uses the bee as a figure for the Assyrian army summoned by God's whistle: armies from Assyria will swarm over the land like bees. The promised land described as flowing with milk and <em>honey</em> (Exodus 3:8) implies the abundant presence of bees throughout Canaan.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bee", "smith": "bee"},
        "key_refs": ["Deuteronomy 1:44", "Judges 14:8", "Psalms 118:12", "Isaiah 7:18"],
        "sections": []
    },
    "beelzebub": {
        "id": "beelzebub",
        "term": "Beelzebub",
        "category": "concepts",
        "intro": "<p>Beelzebub (Greek <em>Beelzeboul</em>, from the Philistine god Baal-zebub of Ekron—<em>lord of the flies</em>) is the name given to Satan as <em>the prince of demons</em> in the New Testament. The Pharisees accused Jesus of casting out demons by the power of Beelzebub (Matthew 10:25; 12:24–27; Mark 3:22; Luke 11:15–19). Jesus's response—that a kingdom divided against itself cannot stand—constitutes one of his clearest assertions that his exorcisms demonstrate the arrival of God's kingdom (Matthew 12:28). The name is not found in any Hebrew text; it appears exclusively in the New Testament as a Synoptic designation for the ruler of demons.</p>",
        "hitchcock_meaning": "same as Baalzebub",
        "source_ids": {"easton": "beelzebub", "smith": "beelzebub", "isbe": "beelzebub"},
        "key_refs": ["Matthew 12:24", "Matthew 12:27", "Matthew 12:28", "Mark 3:22"],
        "sections": []
    },
    "beer": {
        "id": "beer",
        "term": "Beer",
        "category": "places",
        "intro": "<p>Beer (meaning <em>well</em>) is the name of two places in the Old Testament. (1.) A location in the wilderness where God commanded Moses to gather the people and water sprang up; the people sang the well-song recorded in Numbers 21:16–18. (2.) A place in Gilead to which Jotham fled after delivering his fable of the trees, when his half-brother Abimelech threatened him following the massacre at Shechem (Judges 9:21). Both sites are otherwise unidentified.</p>",
        "hitchcock_meaning": "a well",
        "source_ids": {"easton": "beer", "smith": "beer"},
        "key_refs": ["Numbers 21:16", "Judges 9:21"],
        "sections": []
    },
    "beer-elim": {
        "id": "beer-elim",
        "term": "Beer-elim",
        "category": "places",
        "intro": "<p>Beer-elim (meaning <em>well of heroes</em> or <em>well of the mighty ones</em>) was probably the same site as Beer in Numbers 21:16, where Israel's chiefs dug a well in the wilderness. The name appears in Isaiah 15:8 in the oracle against Moab, describing the cry of distress that will reach even to Beer-elim—suggesting it was a place on the southern boundary of Moab or in the broader region. The association with heroes or princes reflects the memorable occasion when the leaders of Israel dug the well with their own staffs.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beer-elim", "isbe": "beer-elim"},
        "key_refs": ["Numbers 21:16", "Isaiah 15:8"],
        "sections": []
    },
    "beer-lahai-roi": {
        "id": "beer-lahai-roi",
        "term": "Beer-lahai-roi",
        "category": "places",
        "intro": "<p>Beer-lahai-roi (meaning <em>the well of him that liveth and seeth me</em> or <em>well of the living one who sees me</em>) was the well in the Negev wilderness, between Kadesh and Bered, where the angel of the LORD appeared to Hagar when she fled from Sarai's harsh treatment. There she received the promise of Ishmael's birth and God's provision (Genesis 16:7–14). Isaac later lived near this well and went out to meditate in the field when Rebekah arrived (Genesis 24:62; 25:11). The name commemorates Hagar's remarkable acknowledgment: <em>You are a God of seeing</em>.</p>",
        "hitchcock_meaning": "the well of him that liveth and seeth me",
        "source_ids": {"easton": "beer-lahai-roi", "isbe": "beer-lahai-roi"},
        "key_refs": ["Genesis 16:7", "Genesis 16:14", "Genesis 24:62", "Genesis 25:11"],
        "sections": []
    },
    "beeri": {
        "id": "beeri",
        "term": "Beeri",
        "category": "people",
        "intro": "<p>Beeri (meaning <em>my well</em> or <em>man of the well</em>) is the name of two men in the Old Testament. (1.) A Hittite, the father of Judith, one of the wives Esau took at the age of forty—marriages that brought grief to his parents Isaac and Rebekah (Genesis 26:34; 36:2). (2.) The father of the prophet Hosea (Hosea 1:1), about whom nothing else is recorded.</p>",
        "hitchcock_meaning": "my well",
        "source_ids": {"easton": "beeri", "smith": "beeri"},
        "key_refs": ["Genesis 26:34", "Hosea 1:1"],
        "sections": []
    },
    "beeroth": {
        "id": "beeroth",
        "term": "Beeroth",
        "category": "places",
        "intro": "<p>Beeroth (meaning <em>wells</em>) was one of the four Hivite cities—along with Gibeon, Chephirah, and Kirjath-jearim—that entered by deception into a covenant of peace with Joshua (Joshua 9:17; 18:25). Located in the territory of Benjamin, it was notable as the hometown of Baanah and Rechab, who murdered Ish-bosheth (2 Samuel 4:2), and of David's mighty warrior Naharai (2 Samuel 23:37). Exiles from Beeroth returned with Zerubbabel after the Babylonian captivity (Ezra 2:25).</p>",
        "hitchcock_meaning": "wells; explaining",
        "source_ids": {"easton": "beeroth", "smith": "beeroth"},
        "key_refs": ["Joshua 9:17", "Joshua 18:25", "2 Samuel 4:2"],
        "sections": []
    },
    "beeroth-of-the-children-of-jaakan": {
        "id": "beeroth-of-the-children-of-jaakan",
        "term": "Beeroth of the children of Jaakan",
        "category": "places",
        "intro": "<p>Beeroth of the children of Jaakan (also Bene-jaakan) was a wilderness encampment of Israel listed in the itinerary of Numbers 33:31–32 and Deuteronomy 10:6, associated with the death and burial of Aaron's father Eleazar. Its location east of Canaan is uncertain. The name means <em>wells of the sons of Jaakan</em>, Jaakan being a Horite clan in the region of Edom (1 Chronicles 1:42).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beeroth-of-the-children-of-jaakan"},
        "key_refs": ["Deuteronomy 10:6", "Numbers 33:31"],
        "sections": []
    },
    "beersheba": {
        "id": "beersheba",
        "term": "Beersheba",
        "category": "places",
        "intro": "<p>Beersheba (meaning <em>well of the oath</em> or <em>well of seven</em>) was the southernmost significant city of ancient Israel, marking the boundary of the settled land in the proverbial phrase <em>from Dan to Beersheba</em>. Abraham dug a well there and made a covenant with Abimelech (Genesis 21:31); Isaac re-dug the same well and received a divine covenant-renewal there (Genesis 26:23–25); and Jacob received God's assurance there on his way to Egypt (Genesis 46:1–4). Elijah fled to Beersheba and rested under a broom tree before his journey to Horeb (1 Kings 19:3–4). The city lay in the northern Negev, in the territory of Simeon within Judah's borders.</p>",
        "hitchcock_meaning": "the well of an oath; the seventh well",
        "source_ids": {"easton": "beersheba", "isbe": "beersheba"},
        "key_refs": ["Genesis 21:31", "Genesis 26:23", "Genesis 46:1", "1 Kings 19:3"],
        "sections": []
    },
    "beetle": {
        "id": "beetle",
        "term": "Beetle",
        "category": "concepts",
        "intro": "<p>The beetle (Hebrew <em>hargol</em>, meaning <em>leaper</em>) appears only in Leviticus 11:22, where it is listed among the four species of hopping insects permitted for food under the Mosaic food laws, alongside the locust, bald locust, and grasshopper. The precise identification of <em>hargol</em> is uncertain; modern translations often render it as <em>cricket</em> or <em>katydid</em> rather than beetle, since true beetles do not hop. Whatever the specific species, it belonged to the class of winged insects with jointed legs for leaping, and was considered clean for consumption.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beetle", "smith": "beetle"},
        "key_refs": ["Leviticus 11:22"],
        "sections": []
    },
    "beeves": {
        "id": "beeves",
        "term": "Beeves",
        "category": "concepts",
        "intro": "<p>Beeves is an archaic English plural of <em>beef</em>, used in the Authorized Version to denote bovine cattle—oxen, bulls, and cows. It appears in Leviticus 22:19, 21 for animals offered as sacrifices, and in Numbers 31:28, 30, 33, 38, 44 in the distribution of plunder taken from Midian. The word is not found in modern translations, which use <em>cattle</em> or <em>oxen</em>. In Old Testament law, cattle were among the most prized animals for both agricultural work and sacrificial offering.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beeves", "smith": "beeves"},
        "key_refs": ["Leviticus 22:19", "Numbers 31:28"],
        "sections": []
    },
    "beg": {
        "id": "beg",
        "term": "Beg",
        "category": "concepts",
        "intro": "<p>Begging and poverty are treated seriously in biblical law and wisdom literature. Mosaic law commanded regular provision for the poor through gleaning rights, sabbatical year debt release, and tithes (Exodus 23:11; Deuteronomy 15:11; Leviticus 19:10). Psalm 37:25 famously claims the psalmist has never seen the righteous forsaken or their children begging bread—an expression of trust in divine provision, not a denial of poverty's existence. The New Testament shows beggars at the temple gate (Acts 3:2) and Bartimaeus crying by the roadside (Mark 10:46). Jesus's beatitude on the poor in spirit (Matthew 5:3) and Luke's version on the poor (Luke 6:20) reflect deep engagement with the theology of dependence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "beg"},
        "key_refs": ["Deuteronomy 15:11", "Psalms 37:25", "Acts 3:2", "Luke 6:20"],
        "sections": []
    },
    "behead": {
        "id": "behead",
        "term": "Behead",
        "category": "concepts",
        "intro": "<p>Beheading as a form of capital punishment is attested in both Testaments. In the Old Testament, the heads of enemies were sometimes taken after battle (1 Samuel 17:51; 2 Samuel 4:8; 20:21–22). Execution by beheading is implied in several narratives. In the New Testament, John the Baptist was beheaded at the order of Herod Antipas, at the request of Herodias's daughter (Matthew 14:10; Mark 6:27). Revelation 20:4 describes martyrs who were beheaded for their testimony and their refusal to worship the beast. Roman law used decapitation (<em>gladio</em>) as a more honorable execution method than crucifixion, extended to Roman citizens.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "behead"},
        "key_refs": ["Matthew 14:10", "Mark 6:27", "Revelation 20:4"],
        "sections": []
    },
    "behemoth": {
        "id": "behemoth",
        "term": "Behemoth",
        "category": "concepts",
        "intro": "<p>Behemoth (a Hebrew plural of majesty for <em>great beast</em>) appears in Job 40:15–24, where God describes it to Job as the supreme example of powerful creatures that exist beyond human mastery—<em>the first of the works of God</em>, eating grass like an ox, with bones like bronze bars and limbs like iron rods, lying in the reeds and lotus plants of the Jordan. Its identity is disputed: most modern commentators identify it with the hippopotamus, whose massive body and aquatic habits match the description; others have suggested the elephant, the water buffalo, or (in a minority view) a mythological creature. Like Leviathan, Behemoth serves theologically to humble Job before the Creator's sovereign power over all his works.</p>",
        "hitchcock_meaning": "beasts",
        "source_ids": {"easton": "behemoth", "smith": "behemoth", "isbe": "behemoth"},
        "key_refs": ["Job 40:15", "Job 40:19", "Job 40:23"],
        "sections": []
    },
    "bekah": {
        "id": "bekah",
        "term": "Bekah",
        "category": "concepts",
        "intro": "<p>The bekah (meaning <em>half</em>) was a Hebrew unit of weight equal to half a shekel, roughly five to six grams of silver. It is explicitly defined in Exodus 38:26 as <em>a bekah a head, that is, half a shekel, according to the shekel of the sanctuary</em>—the payment required of each man in the census of the wilderness. The bekah also features in Genesis 24:22 as the weight of the golden ring Eliezer gave Rebekah. As a standard weight, the bekah was used in commercial transactions and is attested by archaeological examples of inscribed stone weights.</p>",
        "hitchcock_meaning": "half a shekel",
        "source_ids": {"easton": "bekah", "smith": "bekah"},
        "key_refs": ["Exodus 38:26", "Genesis 24:22"],
        "sections": []
    },
    "bel": {
        "id": "bel",
        "term": "Bel",
        "category": "concepts",
        "intro": "<p>Bel is the Aramaic form of Baal, the chief national deity of Babylon, identified with the god Marduk. As the patron god of Babylon's imperial power, Bel represents the ultimate idolatrous challenge to Israel's LORD. Isaiah 46:1 describes Bel bowing down and Nebo stooping as they are loaded onto exhausted beasts—a mocking reversal in which idols that should carry their worshippers must themselves be carried. Jeremiah 50:2 and 51:44 announce that Bel will be put to shame and disgorge what he has swallowed—a reference to nations conquered and absorbed into Babylonian power. The deuterocanonical book of Bel and the Dragon dramatizes Daniel's exposure of the Bel cult as fraud.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bel", "smith": "bel", "isbe": "bel"},
        "key_refs": ["Isaiah 46:1", "Jeremiah 50:2", "Jeremiah 51:44"],
        "sections": []
    },
    "bela": {
        "id": "bela",
        "term": "Bela",
        "category": "places",
        "intro": "<p>Bela (meaning <em>a thing swallowed</em> or <em>destruction</em>) is primarily the name of the city also called Zoar, the small city near Sodom to which Lot fled during the divine judgment that destroyed the cities of the plain (Genesis 14:2, 8; 19:20–23). The name Bela also belongs to several persons: (1.) The firstborn son of Benjamin (Genesis 46:21), whose descendants were the Belaites (Numbers 26:38). (2.) The son of Beor and first king of Edom (Genesis 36:32–33; 1 Chronicles 1:43–44). (3.) A son of Azaz, a Reubenite (1 Chronicles 5:8).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bela", "smith": "bela"},
        "key_refs": ["Genesis 14:2", "Genesis 19:20", "Genesis 36:32", "Genesis 46:21"],
        "sections": []
    },
    "belial": {
        "id": "belial",
        "term": "Belial",
        "category": "concepts",
        "intro": "<p>Belial (Hebrew <em>beliyya'al</em>, meaning <em>worthlessness</em> or <em>without profit</em>) is used throughout the Old Testament as a term for wickedness or wickedness personified, often translated <em>worthless men</em> or <em>sons of Belial</em> in the Authorized Version. It denotes moral depravity and rebellion against God: the men who demanded the gang-rape at Gibeah (Judges 19:22), the wicked sons of Eli (1 Samuel 2:12), and Nabal (1 Samuel 25:17) are all called sons of Belial. In the New Testament (2 Corinthians 6:15) Paul uses Belial as a proper name for Satan, asking what harmony Christ can have with Belial—making the term fully personalized as the embodiment of evil in contrast to Christ.</p>",
        "hitchcock_meaning": "wicked; worthless",
        "source_ids": {"easton": "belial", "smith": "belial", "isbe": "belial"},
        "key_refs": ["Deuteronomy 13:13", "1 Samuel 2:12", "2 Corinthians 6:15"],
        "sections": []
    },
    "bell": {
        "id": "bell",
        "term": "Bell",
        "category": "concepts",
        "intro": "<p>The bells first mentioned in Scripture are the small golden bells sewn alternately with pomegranates on the hem of the high priest's ephod (Exodus 28:33–35). Their sound served a specific purpose: when the high priest entered the Holy of Holies on the Day of Atonement, the bells signaled his presence and movement within the sanctuary, so that he would not die. This auditory signal connected the silent holy space with the waiting congregation outside. Zechariah 14:20 envisions the messianic age when even the bells of the horses will bear the inscription <em>Holy to the LORD</em>—the sacred inscription of the high priest's headplate applied to the most ordinary implements.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bell", "isbe": "bell"},
        "key_refs": ["Exodus 28:33", "Exodus 28:34", "Exodus 28:35", "Zechariah 14:20"],
        "sections": []
    },
    "bellows": {
        "id": "bellows",
        "term": "Bellows",
        "category": "concepts",
        "intro": "<p>Bellows appear in Jeremiah 6:29 in the context of metallurgical refining: <em>The bellows blow fiercely; the lead is consumed by the fire</em>—the refiner's bellows are inadequate to purify the ore, just as the wickedness of Jerusalem cannot be removed by prophetic warning. The bellows used in ancient Near Eastern smelting were typically leather bags that forced air through a clay nozzle into the furnace, creating the high temperatures needed to work copper, bronze, and iron. They represent the human effort that drives the refining process, whether literal or figurative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bellows", "smith": "bellows"},
        "key_refs": ["Jeremiah 6:29"],
        "sections": []
    },
    "belly": {
        "id": "belly",
        "term": "Belly",
        "category": "concepts",
        "intro": "<p>The belly in Scripture serves both literal and figurative purposes. In Hebrew thought the belly (<em>beten</em>) could denote the womb, the inner being, or the seat of carnal desires. Paul uses it metaphorically in Philippians 3:19, describing those <em>whose god is their belly</em>—people who serve sensual appetite as an idol. Romans 16:18 applies the same image to false teachers who serve <em>their own belly</em>. Titus 1:12 quotes the Cretan poet Epimenides on <em>lazy gluttons</em>. Jonah's three days in the belly of the fish (Jonah 1:17; Matthew 12:40) became a type of Christ's death and resurrection.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "belly", "isbe": "belly"},
        "key_refs": ["Jonah 1:17", "Matthew 12:40", "Philippians 3:19", "Romans 16:18"],
        "sections": []
    },
    "belshazzar": {
        "id": "belshazzar",
        "term": "Belshazzar",
        "category": "people",
        "intro": "<p>Belshazzar (meaning <em>Bel protect the king</em>) was the last king of Babylon, described in Daniel 5 as the son of Nebuchadnezzar (in the sense of royal successor or descendant). Historical records identify him as the son of Nabonidus, the last Neo-Babylonian king, serving as co-regent while his father campaigned. On the night of a great feast at which Belshazzar used the sacred vessels looted from the Jerusalem temple, a hand appeared and wrote on the wall: <em>Mene, Mene, Tekel, Parsin</em>. Daniel interpreted the words as a divine verdict of judgment—numbered, weighed, and divided—fulfilled that very night when Belshazzar was killed and Darius the Mede received his kingdom (Daniel 5:30–31).</p>",
        "hitchcock_meaning": "master of the treasure",
        "source_ids": {"easton": "belshazzar", "smith": "belshazzar", "isbe": "belshazzar"},
        "key_refs": ["Daniel 5:1", "Daniel 5:25", "Daniel 5:30", "Daniel 5:31"],
        "sections": []
    },
    "belteshazzar": {
        "id": "belteshazzar",
        "term": "Belteshazzar",
        "category": "people",
        "intro": "<p>Belteshazzar (meaning <em>Beltis protect the king</em> or <em>who lays up treasures in secret</em>) was the Chaldean name given to Daniel by Ashpenaz, chief of Nebuchadnezzar's eunuchs, when the young Judean captives were assimilated into Babylonian court culture (Daniel 1:7). The renaming was part of an attempt to reshape their identity—giving them Babylonian names, language, and diet. Despite this, Daniel maintained his Jewish identity and faith. The name Belteshazzar is distinguished from Belshazzar by one letter in Hebrew and should not be confused with the Babylonian king.</p>",
        "hitchcock_meaning": "who lays up treasures in secret",
        "source_ids": {"easton": "belteshazzar", "smith": "belteshazzar", "isbe": "belteshazzar"},
        "key_refs": ["Daniel 1:7", "Daniel 2:26", "Daniel 4:8"],
        "sections": []
    },
    "ben-ammi": {
        "id": "ben-ammi",
        "term": "Ben-ammi",
        "category": "people",
        "intro": "<p>Ben-ammi (meaning <em>son of my people</em> or <em>born of incest</em>) was the son of Lot by his younger daughter, born after the destruction of Sodom in the cave where the daughters had gotten their father drunk (Genesis 19:38). He became the ancestor of the Ammonites (<em>Bene-ammon</em>), the people of Ammon, whose territory lay east of the Jordan. Like Moab (the son of the elder daughter), Ben-ammi's origin story contextualizes Israel's often-hostile relationship with the Ammonites throughout the Old Testament narrative.</p>",
        "hitchcock_meaning": "son of my people",
        "source_ids": {"easton": "ben-ammi", "isbe": "ben-ammi"},
        "key_refs": ["Genesis 19:38"],
        "sections": []
    },
    "ben-hadad": {
        "id": "ben-hadad",
        "term": "Ben-hadad",
        "category": "people",
        "intro": "<p>Ben-hadad (meaning <em>son of Hadad</em>, the Syrian storm-god) was the standing dynastic title of the kings of Damascus/Aram-Syria, analogous to <em>Pharaoh</em> in Egypt. Three kings are distinguished: (1.) Ben-hadad I, who made a league with Asa of Judah against Baasha of Israel (1 Kings 15:18). (2.) Ben-hadad II, the most prominent, who besieged Samaria twice, was miraculously defeated by Ahab, was later healed by Elisha, and was finally assassinated by Hazael (1 Kings 20; 2 Kings 6:24; 8:7–15). (3.) Ben-hadad III, son of Hazael, under whom Syria declined and Israel recovered territory under Jehoash (2 Kings 13:3, 24–25).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ben-hadad"},
        "key_refs": ["1 Kings 15:18", "1 Kings 20:1", "2 Kings 8:9", "2 Kings 13:3"],
        "sections": []
    },
    "benaiah": {
        "id": "benaiah",
        "term": "Benaiah",
        "category": "people",
        "intro": "<p>Benaiah (meaning <em>built up by Jehovah</em> or <em>son of the Lord</em>) was the son of Jehoiada, the chief priest, and one of David's mightiest warriors. He commanded David's personal bodyguard—the Cherethites and Pelethites—and is renowned for three feats of exceptional valor: killing two lion-like warriors of Moab, killing a lion in a pit on a snowy day, and slaying a formidable Egyptian warrior with his own spear (2 Samuel 23:20–23; 1 Chronicles 11:22–25). He remained loyal to David during Absalom's rebellion and supported Solomon's succession against Adonijah. Solomon appointed him commander-in-chief of the army in place of Joab (1 Kings 2:35).</p>",
        "hitchcock_meaning": "son of the Lord",
        "source_ids": {"easton": "benaiah", "smith": "benaiah", "isbe": "benaiah"},
        "key_refs": ["2 Samuel 23:20", "2 Samuel 23:22", "1 Kings 1:32", "1 Kings 2:35"],
        "sections": []
    },
    "bench": {
        "id": "bench",
        "term": "Bench",
        "category": "concepts",
        "intro": "<p>The bench mentioned in Ezekiel 27:6 refers to the deck or thwarts of Tyrian ships—described as made of cypress (<em>ashurim</em>) from the islands of Kittim, inlaid with ivory. The image occurs in Ezekiel's elaborate lament over Tyre, which he portrays as a great merchant ship perfectly built from the finest materials of every nation. The bench or deck is one detail in this extended metaphor of maritime commerce and coming destruction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bench", "isbe": "bench"},
        "key_refs": ["Ezekiel 27:6"],
        "sections": []
    },
    "bene-jaakan": {
        "id": "bene-jaakan",
        "term": "Bene-jaakan",
        "category": "places",
        "intro": "<p>Bene-jaakan (meaning <em>children of Jaakan</em> or <em>sons of sorrow</em>) was a wilderness encampment of Israel listed in Numbers 33:31–32 between Moseroth and Hor-haggidgad. It is the same site as Beeroth of the children of Jaakan (Deuteronomy 10:6), associated with the burial of Aaron's death and the appointment of the Levites. The Jaakan were a Horite clan in the Edomite region (1 Chronicles 1:42). The site is otherwise unidentified geographically.</p>",
        "hitchcock_meaning": "sons of sorrow",
        "source_ids": {"easton": "bene-jaakan", "isbe": "bene-jaakan"},
        "key_refs": ["Numbers 33:31", "Numbers 33:32", "Deuteronomy 10:6"],
        "sections": []
    },
    "benjamin": {
        "id": "benjamin",
        "term": "Benjamin",
        "category": "people",
        "intro": "<p>Benjamin (meaning <em>son of my right hand</em>; his dying mother Rachel called him Ben-oni, <em>son of my sorrow</em>) was the youngest son of Jacob, the only one born in Canaan, and the full brother of Joseph. His birth cost Rachel her life (Genesis 35:18). Jacob clung to Benjamin after Joseph's disappearance, and the story of Joseph's test of his brothers revolves around Benjamin's detention in Egypt. Jacob's dying blessing describes Benjamin as a <em>ravenous wolf</em> (Genesis 49:27), a prophecy reflected in the tribe's fierce warriors, including Ehud, Saul, and Jonathan.</p><p>The tribe of Benjamin occupied a small but strategically vital territory between Judah and Ephraim, including Jerusalem's suburbs, Jericho, Bethel, and Gibeah. After the kingdom's division, Benjamin aligned with Judah. Paul identifies himself as <em>of the tribe of Benjamin</em> (Philippians 3:5; Romans 11:1).</p>",
        "hitchcock_meaning": "son of the right hand",
        "source_ids": {"easton": "benjamin", "smith": "benjamin", "isbe": "benjamin"},
        "key_refs": ["Genesis 35:18", "Genesis 49:27", "Joshua 18:21", "Philippians 3:5"],
        "sections": []
    },
    "beor": {
        "id": "beor",
        "term": "Beor",
        "category": "people",
        "intro": "<p>Beor (meaning <em>a torch</em> or <em>burning</em>) is the name of two men in the Old Testament. (1.) The father of Bela, the first king of Edom named in the table of Edomite kings (Genesis 36:32; 1 Chronicles 1:43). (2.) The father of Balaam the prophet of Pethor (Numbers 22:5; 24:3, 15; 31:8; Deuteronomy 23:4; Micah 6:5; 2 Peter 2:15). The New Testament's single reference to Beor's son identifies Balaam as an example of a false prophet who loved the wages of unrighteousness.</p>",
        "hitchcock_meaning": "burning; foolish; mad",
        "source_ids": {"easton": "beor", "smith": "beor", "isbe": "beor"},
        "key_refs": ["Genesis 36:32", "Numbers 22:5", "2 Peter 2:15"],
        "sections": []
    },
    "bera": {
        "id": "bera",
        "term": "Bera",
        "category": "people",
        "intro": "<p>Bera (meaning <em>gift</em> or <em>son of evil</em>) was the king of Sodom at the time of the invasion of the four Mesopotamian kings under Chedorlaomer (Genesis 14:2, 8, 17, 21). He was defeated at the battle of the Valley of Siddim, which was full of bitumen pits; he and his allies fled and some fell into the pits. After Abraham's victory over the invaders and the rescue of Lot, Bera met Abraham in the Valley of Shaveh, where the king of Sodom offered Abraham the recovered goods—an offer Abraham declined to avoid the impression that Sodom had made him rich.</p>",
        "hitchcock_meaning": "a well; declaring",
        "source_ids": {"easton": "bera", "smith": "bera", "isbe": "bera"},
        "key_refs": ["Genesis 14:2", "Genesis 14:17", "Genesis 14:21"],
        "sections": []
    },
    "berachah": {
        "id": "berachah",
        "term": "Berachah",
        "category": "places",
        "intro": "<p>Berachah (meaning <em>blessing</em>) is the name of a valley not far from En-gedi, on the edge of the Judean wilderness, where King Jehoshaphat and his people assembled to bless the LORD after a miraculous victory over the combined forces of Moab, Ammon, and Edom—whose armies had destroyed each other without a battle being fought (2 Chronicles 20:26). The name commemorates the act of corporate thanksgiving on that day. Berachah is also the name of a Benjamite warrior who joined David at Ziklag (1 Chronicles 12:3).</p>",
        "hitchcock_meaning": "blessing; bending the knee",
        "source_ids": {"easton": "berachah", "smith": "berachah"},
        "key_refs": ["2 Chronicles 20:26", "1 Chronicles 12:3"],
        "sections": []
    },
    "berea": {
        "id": "berea",
        "term": "Berea",
        "category": "places",
        "intro": "<p>Berea (meaning <em>heavy</em> or <em>well-watered</em>) was a city of Macedonia, modern Veria, located about forty miles southwest of Thessalonica. Paul and Silas fled there after being driven from Thessalonica (Acts 17:10). The Bereans received the gospel with exceptional eagerness, searching the Scriptures daily to verify what Paul taught—earning them the reputation as <em>more noble</em> than the Thessalonians (Acts 17:11). When Jews from Thessalonica stirred up trouble there as well, Paul departed by sea while Silas and Timothy remained. Sopater of Berea was among those who accompanied Paul on his final journey to Jerusalem (Acts 20:4).</p>",
        "hitchcock_meaning": "heavy; weighty",
        "source_ids": {"easton": "berea", "isbe": "berea"},
        "key_refs": ["Acts 17:10", "Acts 17:11", "Acts 17:13", "Acts 20:4"],
        "sections": []
    },
    "berechiah": {
        "id": "berechiah",
        "term": "Berechiah",
        "category": "people",
        "intro": "<p>Berechiah (meaning <em>blessed by Jehovah</em>) is the name of six men in the Old Testament. (1.) The son of Shimea and father of Asaph the musician (1 Chronicles 6:39). (2.) A Levite musician who assisted in bringing the ark to Jerusalem (1 Chronicles 15:17, 23). (3.) An Ephraimite leader who insisted on releasing Judean prisoners taken by Pekah king of Israel (2 Chronicles 28:12). (4.) A son of Zerubbabel (1 Chronicles 3:20). (5.) A Levite who settled in Jerusalem after the exile (1 Chronicles 9:16). (6.) The father of Zechariah the prophet (Zechariah 1:1, 7; Matthew 23:35), making Berechiah the grandfather of Zechariah the son of Jehoiada—though some textual questions exist in Matthew's attribution.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "berechiah", "smith": "berechiah", "isbe": "berechiah"},
        "key_refs": ["1 Chronicles 6:39", "1 Chronicles 15:17", "2 Chronicles 28:12", "Zechariah 1:1"],
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
    print(f'BP b2: Bartholomew → Berechiah: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
