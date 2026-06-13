"""
BP Article Synthesis — e1: Eagle → Eliphelet
Covers Easton entries: Eagle through Eliphelet (75 entries)

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

Script: scripts/bp-e1.py
Run: python3 scripts/bp-e1.py
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
    "eagle": {
        "id": "eagle",
        "term": "Eagle",
        "category": "concepts",
        "intro": "<p>The eagle of Scripture (Hebrew <em>nesher</em>) most likely refers to the griffon vulture or great vulture rather than the true eagle, as the term was applied broadly to the largest soaring birds of Palestine. Several species are identified across the biblical text: the golden eagle, imperial eagle, osprey, and the griffon vulture, which nests in cliffs and circles at enormous heights. The bird's power and swiftness made it a standard metaphor in biblical poetry — military invasions strike like eagles (Deuteronomy 28:49; Jeremiah 49:22), and the LORD renews strength like the eagle's (Psalms 103:5; Isaiah 40:31).</p><p>Eagles were ceremonially unclean under Mosaic law (Leviticus 11:13) and are frequently used in prophetic imagery. Ezekiel employs the eagle twice in allegories for the Babylonian and Egyptian empires (Ezekiel 17). In the New Testament, the eagle appears in the apocalyptic imagery of Revelation 4:7 as one of the four living creatures, and Revelation 12:14 pictures the woman given eagle's wings in flight. The care of an eagle for its young — hovering, bearing them on its wings — is used to describe God's provision for Israel in the wilderness (Deuteronomy 32:11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eagle", "smith": "eagle", "isbe": "eagle"},
        "key_refs": ["Deuteronomy 28:49", "2 Samuel 1:23", "Job 39:27", "Psalms 103:5", "Isaiah 40:31"]
    },
    "ear": {
        "id": "ear",
        "term": "Ear",
        "category": "concepts",
        "intro": "<p>The ear is used extensively in Scripture in both literal and figurative senses. Literally, it refers to the organ of hearing, but its primary biblical importance lies in its symbolic use for attention, obedience, and spiritual receptivity. To \"uncover the ear\" (1 Samuel 9:15; 2 Samuel 7:27) is to make a secret communication; to \"incline the ear\" is to give attentive heed (Psalms 45:10; Proverbs 4:20). God's ear is spoken of anthropomorphically: \"The ear of the LORD is toward the righteous\" (1 Peter 3:12; Psalms 34:15).</p><p>The piercing of a servant's ear against the doorpost (Exodus 21:6) symbolized voluntary, permanent servitude — the servant chose to remain rather than go free in the sabbatical year. In the New Testament, Christ repeatedly calls for hearing beyond mere physical sound: \"He who has ears, let him hear\" (Matthew 11:15; 13:9) is a formula pointing to spiritual comprehension. The ear of the wicked is said to be dull (Isaiah 6:10; Matthew 13:15), and James calls for believers to be \"swift to hear, slow to speak\" (James 1:19).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ear"},
        "key_refs": ["Psalms 34:15", "Exodus 21:6", "Isaiah 6:10", "Matthew 13:9"]
    },
    "earing": {
        "id": "earing",
        "term": "Earing",
        "category": "concepts",
        "intro": "<p>Earing is an archaic English word derived from the Latin <em>aro</em> (to plow), meaning ploughing or tillage. It appears in the King James Version at Genesis 45:6 and Exodus 34:21: \"in earing time and in harvest thou shalt rest.\" The term captures the agricultural rhythm of ancient Israelite life, in which both the plowing season (autumn–winter) and the harvest season (spring–summer) were punctuated by Sabbath rest regardless of the urgency of the agricultural calendar.</p><p>Modern translations typically render the word as \"plowing\" or \"plowing season,\" as the archaic English sense has been entirely lost. The law that Sabbath rest applied even during the busiest farming periods underscored that covenant obedience was not suspended for economic necessity — an emphatic statement in an agrarian society where missed planting or harvest windows could mean famine.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "earing", "smith": "earing"},
        "key_refs": ["Genesis 45:6", "Exodus 34:21"]
    },
    "earnest": {
        "id": "earnest",
        "term": "Earnest",
        "category": "concepts",
        "intro": "<p>In biblical usage, earnest (Greek <em>arrabon</em>) refers to a pledge or down payment that guarantees the full payment to follow — a legal and commercial term adopted by Paul to describe the Holy Spirit's role in the believer's life. The Spirit is called the \"earnest of our inheritance\" (2 Corinthians 1:22; 5:5; Ephesians 1:14), meaning that the present experience of the Spirit in regeneration, gifting, and sanctification is not the fullness of what God has promised but a real foretaste of the glory that will be revealed. The word was used in Greek commercial contracts for a deposit that both initiated a transaction and legally obligated completion.</p><p>The theological weight of the term is significant: the Spirit as earnest means that salvation is not merely a future promise but has already begun in the believer's present experience. The same Spirit who now intercedes, seals, and transforms the believer is the pledge of the bodily resurrection and the new creation. Paul uses this commercial metaphor to anchor eschatological hope in present spiritual reality rather than abstract expectation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "earnest"},
        "key_refs": ["2 Corinthians 1:22", "2 Corinthians 5:5", "Ephesians 1:14"]
    },
    "earrings": {
        "id": "earrings",
        "term": "Earrings",
        "category": "concepts",
        "intro": "<p>Earrings appear throughout the Old Testament as common personal ornaments worn by both men and women in Israel and throughout the ancient Near East. The Hebrew term <em>nezem</em> refers to a ring worn in the ear or nose; context often determines which is meant. Jacob gathered the earrings of his household at Shechem and buried them beneath the oak at Bethel as part of a religious purification, suggesting that some earrings had idolatrous associations (Genesis 35:4). The golden earrings contributed by the Israelites in the wilderness became the material for the golden calf — a cautionary instance of ornamentation misused for idolatry (Exodus 32:2–3).</p><p>In Numbers 31:50, the Israelite soldiers offered captured earrings as a gift to the LORD. Ezekiel's allegory of Jerusalem as a bride describes earrings among God's gifts to her (Ezekiel 16:12), reflecting the cultural normalcy of the adornment. Isaiah 3:20 lists earrings among the ornaments of proud Jerusalem that will be stripped away in judgment. The New Testament cautions against elaborate jewelry as a primary basis of personal appearance (1 Timothy 2:9; 1 Peter 3:3), though without prohibiting it outright.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "earrings", "smith": "earrings"},
        "key_refs": ["Genesis 35:4", "Exodus 32:2", "Numbers 31:50", "Ezekiel 16:12"]
    },
    "earth": {
        "id": "earth",
        "term": "Earth",
        "category": "concepts",
        "intro": "<p>The word <em>earth</em> in Scripture carries two primary meanings that must be distinguished by context. In the sense of soil or ground, it translates the Hebrew <em>adamah</em> — the material from which Adam (<em>adam</em>) was formed (Genesis 2:7). In the sense of the whole terrestrial world or inhabited land, it translates <em>erets</em>, the same word used for a specific country or region. This ambiguity runs through the creation narrative: \"In the beginning God created the heavens and the earth (<em>erets</em>)\" (Genesis 1:1).</p><p>Theologically, the earth belongs to the LORD (Psalms 24:1), was created good (Genesis 1:31), was cursed at the fall (Genesis 3:17), and will be renewed at the consummation (Revelation 21:1; Isaiah 65:17). The \"new earth\" is a central hope of biblical eschatology, in which the created order is not abandoned but redeemed. The concept of <em>adamah</em> as soil also grounds the covenant of stewardship: humanity was placed in the garden \"to work it and keep it\" (Genesis 2:15), establishing a relationship of care with the physical creation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "earth", "smith": "earth", "isbe": "earth"},
        "key_refs": ["Genesis 1:1", "Genesis 9:20", "Psalms 24:1", "Revelation 21:1"]
    },
    "earthquake": {
        "id": "earthquake",
        "term": "Earthquake",
        "category": "concepts",
        "intro": "<p>Earthquakes are mentioned throughout Scripture both as natural phenomena and as signs of divine presence or judgment. Palestine lies along active seismic zones, and the biblical text reflects the reality of significant quakes: the earthquake in the days of Uzziah king of Judah (Amos 1:1; Zechariah 14:5) was so memorable that it served as a dating marker two centuries later. The Psalms describe the earth trembling at God's approach (Psalms 18:7; 68:8), and Sinai's quaking accompanied the theophany of the law-giving (Exodus 19:18).</p><p>In the prophetic and apocalyptic literature, earthquakes signal eschatological upheaval: Isaiah (13:13; 24:19), Joel (2:10), Nahum (1:5), and the book of Revelation (6:12; 8:5; 11:13) all use seismic imagery for the shaking of the present order before the new age. In the New Testament, an earthquake accompanies the crucifixion (Matthew 27:51) and the resurrection (Matthew 28:2), theologically marking those events as cosmic in significance. The earthquake that freed Paul and Silas in Philippi (Acts 16:26) is presented as divine intervention.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "earthquake", "smith": "earthquake", "isbe": "earthquake"},
        "key_refs": ["Psalms 18:7", "Amos 1:1", "Matthew 27:51", "Revelation 6:12"]
    },
    "east": {
        "id": "east",
        "term": "East",
        "category": "concepts",
        "intro": "<p>East (<em>mizrah</em> in Hebrew, meaning \"the rising\") was the primary orientation point in the ancient Near Eastern world. Biblical geography and temple design were oriented eastward: the entrance of the tabernacle and Temple faced east, the rising sun marking the direction of God's approach (Ezekiel 43:2; 44:1). The \"east country\" or \"land of the east\" (Genesis 25:6; Numbers 23:7) denoted broadly the territories beyond the Jordan and Euphrates — Mesopotamia, Arabia, and the regions of Aram.</p><p>Theologically, east carries both positive and negative connotations in Scripture. The garden of Eden was \"eastward\" (Genesis 2:8), and after the fall, humanity was driven east of Eden (Genesis 3:24; 4:16). The nations assembled from the east to build Babel (Genesis 11:2). Conversely, the glory of the LORD was seen coming from the east in Ezekiel's vision of restoration (Ezekiel 43:2), and the star of the Magi came from the east (Matthew 2:1–2). In Jewish liturgical practice, prayer facing east anticipated the direction of divine return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "east", "smith": "east"},
        "key_refs": ["Genesis 2:8", "Genesis 25:6", "Ezekiel 43:2", "Matthew 2:1"]
    },
    "east-gate": {
        "id": "east-gate",
        "term": "East Gate",
        "category": "places",
        "intro": "<p>The East Gate of Jerusalem appears in Jeremiah 19:2 where it is identified with, or near, the Potter's Gate — the gate that led out to the Valley of Hinnom (Gehenna) on the southeastern side of the city. The site was associated with the practice of child sacrifice at Topheth and became a scene of Jeremiah's enacted prophecy, in which he smashed a potter's vessel to symbolize God's judgment on Judah's idolatry.</p><p>A second notable \"East Gate\" in Scripture is the outer east gate of the restored temple complex in Ezekiel's vision (Ezekiel 44:1–3). In that vision, the gate was to remain permanently shut after the glory of the LORD entered through it, reserved only for the prince on appointed days. This \"Golden Gate\" in Ezekiel's ideal temple has generated significant eschatological interpretation in both Jewish and Christian tradition regarding the manner of the Messiah's entry into Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "east-gate"},
        "key_refs": ["Jeremiah 19:2", "Ezekiel 44:1", "Nehemiah 3:29"]
    },
    "east-sea": {
        "id": "east-sea",
        "term": "East Sea",
        "category": "places",
        "intro": "<p>The East Sea, also called the Eastern Sea, refers in the Old Testament to the Dead Sea, which lies on the eastern border of Canaan. It is called the East Sea in distinction from the Mediterranean (the \"Western Sea\" or \"Great Sea\") to the west. Joel 2:20 uses it in the context of the northern army being driven into the eastern and western seas. Ezekiel 47:18 employs it as a geographic boundary in the description of the restored land.</p><p>The Dead Sea — also called the Salt Sea (Genesis 14:3), the Sea of Arabah (Deuteronomy 3:17), and the Sea of the Plain — lies approximately 1,400 feet below sea level, making it the lowest body of water on earth. Its extreme salinity supports no fish life, giving it the character of a natural symbol of desolation in prophetic literature. Ezekiel's vision of healing waters flowing eastward from the restored temple and sweetening the Dead Sea (Ezekiel 47:8–9) therefore carries dramatic restorative imagery.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "east-sea"},
        "key_refs": ["Joel 2:20", "Ezekiel 47:18", "Deuteronomy 3:17"]
    },
    "east-wind": {
        "id": "east-wind",
        "term": "East Wind",
        "category": "concepts",
        "intro": "<p>The east wind in Scripture is consistently associated with drought, scorching heat, and God's judgment. In Palestine, the east wind (Arabic <em>sirocco</em>) blows off the Arabian desert and Mesopotamian plains, bringing hot, dry, dust-laden air that withers vegetation and makes outdoor life oppressive. Ezekiel repeatedly uses the east wind as a symbol of divine judgment: Tyre's wealth was scattered by it (Ezekiel 27:26), and Pharaoh's Egypt fell before it (Ezekiel 17:10; 19:12).</p><p>In the Exodus narrative, the LORD drove back the Red Sea with a strong east wind all night (Exodus 14:21), and an east wind brought the plague of locusts upon Egypt (Exodus 10:13). Job laments that God tosses him about in a storm and dissolves him in the east wind (Job 27:21). Hosea uses the east wind as a figure for the coming Assyrian destruction of Ephraim (Hosea 13:15). In contrast to this destructive force, Isaiah 27:8 speaks of God restraining the east wind as a picture of measured rather than total judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "east-wind"},
        "key_refs": ["Exodus 14:21", "Job 27:21", "Ezekiel 27:26", "Hosea 13:15"]
    },
    "east-children-of-the": {
        "id": "east-children-of-the",
        "term": "East, Children of the",
        "category": "concepts",
        "intro": "<p>\"Children of the East\" (<em>bene qedem</em>) is a collective designation in the Old Testament for the nomadic and semi-nomadic peoples who inhabited the deserts and steppes east of Canaan, broadly corresponding to Arabia and the Syrian desert. They are identified in Judges 6:3 and 7:12 as the Midianites, Amalekites, and associated eastern raiders who periodically invaded Israelite territory during the period of the judges. Their camels and livestock are described as innumerable, covering the land like locusts.</p><p>In Job 1:3, Job himself is called \"the greatest of all the people of the East,\" indicating a region of wealth and wisdom — consistent with the Old Testament association of eastern peoples with proverbial wisdom (1 Kings 4:30). Balaam comes from Pethor \"in the land of the children of the east\" (Numbers 23:7). Ezekiel 25:4 foretells that the children of the east will possess Ammon as part of the judgment on that nation. The Nabateans of later history are considered by many scholars to be the same group's successors.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "east-children-of-the"},
        "key_refs": ["Judges 6:3", "Job 1:3", "Numbers 23:7", "1 Kings 4:30"]
    },
    "easter": {
        "id": "easter",
        "term": "Easter",
        "category": "concepts",
        "intro": "<p>Easter is the English rendering used in the King James Version at Acts 12:4, where the Greek text has <em>pascha</em> — the standard New Testament word for Passover. The KJV translators retained \"Easter\" here based on the English ecclesiastical calendar (and possibly an awareness of the pagan festival of <em>Eostre</em>, a Saxon spring goddess), but modern translations uniformly render it \"Passover,\" which is the correct meaning in context: Herod Agrippa was waiting until after the Passover festival to bring Peter out for trial.</p><p>As a Christian celebration, Easter commemorates the resurrection of Jesus Christ on the first day of the week following Passover. The New Testament does not use the term \"Easter\" for the resurrection celebration, but the apostolic church met on the first day of the week (Acts 20:7; 1 Corinthians 16:2) and broke bread in remembrance of the risen Lord. The dating of Easter in relation to Passover became a major controversy in early church history (the Quartodeciman controversy), eventually resolved by the Council of Nicaea in 325.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "easter", "smith": "easter", "isbe": "easter"},
        "key_refs": ["Acts 12:4", "1 Corinthians 5:7", "Acts 20:7"]
    },
    "eating": {
        "id": "eating",
        "term": "Eating",
        "category": "concepts",
        "intro": "<p>Eating customs in biblical times reflected both social boundaries and covenantal relationships. The ancient Hebrews would not eat with Egyptians (Genesis 43:32), as such table fellowship was considered a form of religious and social integration that their culture prohibited. Meals were eaten reclining rather than sitting in later periods (John 13:23; Luke 7:36), a Hellenistic custom adopted in the intertestamental era. Before eating, hands were washed as a religious ritual, though the Pharisees extended this requirement to elaborate ceremonial washings (Mark 7:3).</p><p>In the Mosaic law, extensive dietary regulations (Leviticus 11; Deuteronomy 14) divided foods into clean and unclean categories, shaping Israel's diet as a mark of covenant distinctiveness. The New Testament records the abolition of these food laws for Gentile believers through Peter's vision (Acts 10:9–16) and Paul's teaching (Romans 14; 1 Corinthians 8), though Paul nuances the principle by emphasizing the primacy of love over knowledge in matters of food sacrificed to idols. The Lord's Supper (1 Corinthians 11:23–26) transforms the act of eating into a proclamation of Christ's death until his return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eating"},
        "key_refs": ["Genesis 43:32", "Mark 7:3", "Acts 10:13", "1 Corinthians 11:23"]
    },
    "ebal": {
        "id": "ebal",
        "term": "Ebal",
        "category": "places",
        "intro": "<p>Ebal (meaning <em>ancient heaps</em>) is a mountain in central Canaan, rising 3,076 feet above sea level and approximately 1,200 feet above the adjacent valley of Shechem. It stands directly across the valley from Mount Gerizim, together forming the natural amphitheater that was the site of Israel's covenant renewal ceremony upon entering Canaan. Moses commanded that after crossing the Jordan, the tribes of Reuben, Gad, Asher, Zebulun, Dan, and Naphtali should stand on Mount Ebal to pronounce the curses of the covenant (Deuteronomy 27:13), while the remaining tribes stood on Gerizim for the blessings.</p><p>Joshua faithfully executed this ceremony after the conquest of Ai: he built an altar of unhewn stones on Mount Ebal (Joshua 8:30–35), offered burnt offerings and peace offerings, and read all the words of the law before the assembled congregation of Israel. The site's significance lies in its function as the focal point for Israel's formal acceptance of covenant obligations. Ebal also appears in the genealogies as a son of Shobal (1 Chronicles 1:22) and as a son of Joktan in some manuscript traditions.</p>",
        "hitchcock_meaning": "ancient heaps",
        "source_ids": {"easton": "ebal", "smith": "ebal"},
        "key_refs": ["Deuteronomy 27:13", "Joshua 8:30", "Joshua 8:33", "1 Chronicles 1:22"]
    },
    "ebed": {
        "id": "ebed",
        "term": "Ebed",
        "category": "people",
        "intro": "<p>Ebed (meaning <em>a servant</em> or <em>laborer</em>) is the name of two individuals in the Old Testament. The more notable is the father of Gaal, in whom the men of Shechem placed their confidence during the rebellion against Abimelech (Judges 9:26–41). Gaal son of Ebed stirred up the citizens of Shechem against Abimelech's rule, boasting that he would overthrow him — only to be driven from the city when Zebul, Abimelech's officer, warned his master and Abimelech returned to crush the rebellion. The second Ebed is mentioned in Ezra 8:6 as the father of Jotham, one of the heads of the returning exiles who accompanied Ezra from Babylon.</p>",
        "hitchcock_meaning": "a servant; laborer",
        "source_ids": {"easton": "ebed", "smith": "ebed"},
        "key_refs": ["Judges 9:26", "Judges 9:28", "Ezra 8:6"]
    },
    "ebed-melech": {
        "id": "ebed-melech",
        "term": "Ebed-melech",
        "category": "people",
        "intro": "<p>Ebed-melech (meaning <em>the king's servant</em>, likely an official title) was an Ethiopian eunuch in the service of King Zedekiah of Judah. He appears in a pivotal episode in Jeremiah 38: when the princes of Judah had cast Jeremiah into a muddy cistern to die, Ebed-melech interceded directly with the king and received permission to rescue the prophet, lowering ropes and worn rags to him so he could be drawn out safely. His intervention likely saved Jeremiah's life.</p><p>The account is notable for several reasons: it presents a foreigner and a court servant as a faithful defender of God's prophet while the princes of Judah sought Jeremiah's death. Because of this act of courage, Ebed-melech received a personal oracle of promise from Jeremiah (Jeremiah 39:15–18): in the fall of Jerusalem, his life would be preserved and he would not be given into the hands of those whom he feared, \"because thou hast put thy trust in me, saith the LORD.\"</p>",
        "hitchcock_meaning": "the king's servant",
        "source_ids": {"easton": "ebed-melech"},
        "key_refs": ["Jeremiah 38:7", "Jeremiah 38:11", "Jeremiah 39:16"]
    },
    "eben-ezer": {
        "id": "eben-ezer",
        "term": "Eben-ezer",
        "category": "places",
        "intro": "<p>Eben-ezer (meaning <em>the stone of help</em>) is the name of a memorial stone set up by the prophet Samuel after Israel's victory over the Philistines near Mizpah. Following a period of spiritual renewal — in which the Israelites put away their foreign gods, gathered at Mizpah under Samuel's leadership, and cried out to God — the LORD thundered against the Philistine army with a great noise and threw them into confusion, allowing Israel to defeat them (1 Samuel 7:7–12). Samuel then erected a stone between Mizpah and Jeshanah, naming it Eben-ezer: \"Hitherto hath the LORD helped us.\"</p><p>The location is significant because an earlier battle near the same site had ended in catastrophe for Israel — the ark had been captured and 30,000 Israelites had fallen (1 Samuel 4:1–11). The stone of help thus marked a reversal of fortunes and a renewed covenant experience. The name \"Ebenezer\" became a common name in Christian tradition (particularly in English Puritan and Nonconformist culture) as a testimony to God's past faithfulness, expressing the same sentiment as Samuel's declaration.</p>",
        "hitchcock_meaning": "the stone of help",
        "source_ids": {"easton": "eben-ezer", "smith": "eben-ezer"},
        "key_refs": ["1 Samuel 7:7", "1 Samuel 7:12", "1 Samuel 4:1"]
    },
    "eber": {
        "id": "eber",
        "term": "Eber",
        "category": "people",
        "intro": "<p>Eber (meaning <em>one that passes</em> or <em>the region beyond</em>) was the third post-diluvian patriarch after Shem in the Shemite genealogy (Genesis 10:24; 11:14–17). He was the great-grandson of Shem and the ancestor of the Hebrews, from whose name (<em>ibri</em>) the designation \"Hebrew\" is traditionally derived. Eber's son Peleg was born \"in his days the earth was divided\" (Genesis 10:25), a phrase interpreted variously as referring to the division of the nations at Babel or to a geographical division of lands.</p><p>Eber lived 464 years according to the Masoretic text — longer than his ancestors after the flood — and is mentioned in Luke 3:35 in the genealogy of Jesus. The term \"Hebrews\" as the ethnic name for Abraham's descendants is likely connected to Eber as the ancestral eponym, though some scholars also connect it to the Habiru/Apiru peoples attested in ancient Near Eastern texts. Numbers 24:24 contains Balaam's oracle that ships from Kittim would afflict Asshur and Eber.</p>",
        "hitchcock_meaning": "one that passes; anger",
        "source_ids": {"easton": "eber", "smith": "eber", "isbe": "eber"},
        "key_refs": ["Genesis 10:24", "Genesis 11:14", "Numbers 24:24", "Luke 3:35"]
    },
    "ebony": {
        "id": "ebony",
        "term": "Ebony",
        "category": "concepts",
        "intro": "<p>Ebony appears once in Scripture, in Ezekiel 27:15, as one of the luxury goods brought by merchants from Dedan to the great trading port of Tyre: \"They brought thee for a present horns of ivory and ebony.\" Ebony is a dense, black hardwood derived from trees of the genus <em>Diospyros</em>, prized throughout the ancient world for carving, inlay work, and luxury furnishings. It was not native to Canaan or Mesopotamia and was imported from sub-Saharan Africa and southern India via Arabia, making it a marker of long-distance trade and aristocratic wealth in the ancient Near East.</p><p>Archaeological finds from Egyptian royal tombs and Mesopotamian palace sites confirm ebony's high value in antiquity — it appeared alongside ivory, gold, and lapis lazuli as emblematic of luxury trade goods. In the context of Ezekiel's lament over Tyre, the mention of ebony underscores the city's position at the center of international commerce, making the prophecy of its destruction (Ezekiel 26–27) all the more dramatic.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ebony", "smith": "ebony"},
        "key_refs": ["Ezekiel 27:15"]
    },
    "ebronah": {
        "id": "ebronah",
        "term": "Ebronah",
        "category": "places",
        "intro": "<p>Ebronah (meaning <em>passage over</em>) is listed in Numbers 33:34–35 as one of the wilderness stations of the Israelites between Jotbathah and Ezion-gaber during their forty years of wandering. Its precise location has not been identified with certainty by modern archaeology, but the sequence places it in the Arabah region approaching the northeastern arm of the Red Sea (the Gulf of Aqaba). Ezion-gaber, the next station and a known location, helps narrow the probable area to the eastern Sinai peninsula or the Wadi Arabah.</p><p>Like many of the wilderness station names in Numbers 33, Ebronah is known only from this itinerary list and appears nowhere else in Scripture. The name's meaning (<em>passage</em>) may reflect a geographical feature — a ford, crossing point, or narrow passage through the terrain.</p>",
        "hitchcock_meaning": "passage over; being angry",
        "source_ids": {"easton": "ebronah", "smith": "ebronah"},
        "key_refs": ["Numbers 33:34"]
    },
    "ecbatana": {
        "id": "ecbatana",
        "term": "Ecbatana",
        "category": "places",
        "intro": "<p>Ecbatana (also Achmetha) was the ancient capital of the Median empire and one of the great cities of the ancient Near East, situated on the slopes of Mount Alvand in modern northwestern Iran (the site of present-day Hamadan). It appears in Scripture in Ezra 6:2, where the decree of Cyrus authorizing the rebuilding of the Jerusalem temple was found stored in \"the palace that is in Achmetha, in the province of the Medes.\" The record had been deposited there rather than in Babylon, explaining why initial searches at Babylon found nothing (Ezra 5:17).</p><p>Ecbatana served as the summer capital of the Persian kings, who moved their court there during the hot season. Ancient sources describe it as a city of concentric walls of different colors, with a great palace complex. The city plays a larger role in the deuterocanonical books: Tobit is set largely in Ecbatana, and it appears in Judith 1 as the great city Nebuchadnezzar sent his general against. For the canonical narrative, its primary significance is as the archive location that confirmed the legal basis for the temple's reconstruction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ecbatana", "smith": "ecbatana"},
        "key_refs": ["Ezra 6:2"]
    },
    "ecclesiastes": {
        "id": "ecclesiastes",
        "term": "Ecclesiastes",
        "category": "concepts",
        "intro": "<p>Ecclesiastes is the Greek rendering of the Hebrew <em>Koheleth</em>, meaning \"Preacher\" or \"Assembler\" — the title and pen name of the book's author, who speaks as a king and wisdom teacher reflecting on the meaning of human existence. The book belongs to the Wisdom literature of the Old Testament and is distinctive for its frank wrestling with the apparent futility of life \"under the sun\" — the cyclical nature of human experience, the inevitability of death, and the limitations of wisdom, wealth, and pleasure as ultimate goods. The recurring phrase \"vanity of vanities, all is vanity\" (<em>hebel habalim</em>, literally \"vapor of vapors\") encapsulates its central thesis.</p><p>The book is traditionally attributed to Solomon, who uniquely possessed both the wisdom and the wealth to conduct the experiment the text describes. However, the author's persona may function literarily as a representative sage rather than as a strict claim of Solomonic authorship. Despite its unflinching acknowledgment of life's absurdities, the book does not end in nihilism: the conclusion (Ecclesiastes 12:13–14) calls the reader to fear God and keep his commandments as the whole duty of humanity, grounding life's meaning in covenant relationship rather than human achievement.</p>",
        "hitchcock_meaning": "a preacher",
        "source_ids": {"easton": "ecclesiastes", "smith": "ecbatana"},
        "key_refs": ["Ecclesiastes 1:2", "Ecclesiastes 2:11", "Ecclesiastes 12:13"]
    },
    "eclipse": {
        "id": "eclipse",
        "term": "Eclipse",
        "category": "concepts",
        "intro": "<p>Solar eclipses are alluded to in several prophetic passages of the Old Testament, though the word \"eclipse\" itself does not appear in Scripture. Amos 8:9 records the divine warning: \"I will cause the sun to go down at noon, and I will darken the earth in the clear day\" — an image of sudden judgment using the natural phenomenon of eclipse or darkness as a sign. Similar imagery appears in Micah 3:6, Zechariah 14:6, and Joel 2:10, where the darkening of sun and moon accompanies eschatological judgment or the Day of the LORD.</p><p>The darkening of the sun during the crucifixion of Jesus (Matthew 27:45; Luke 23:44–45), traditionally described as \"darkness over all the land\" from noon until 3 p.m., has been interpreted both as miraculous and as a solar eclipse, though the Passover timing (a full moon) makes an ordinary lunar eclipse impossible and a solar eclipse equally improbable astronomically. Most scholars treat the darkness as a supernatural sign accompanying the death of Christ, consistent with the OT prophetic pattern in which cosmic darkness signals divine action in history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eclipse"},
        "key_refs": ["Amos 8:9", "Matthew 27:45", "Joel 2:10"]
    },
    "ed": {
        "id": "ed",
        "term": "Ed",
        "category": "concepts",
        "intro": "<p>Ed (meaning <em>witness</em>) is the name given to the altar built by the eastern tribes of Israel — Reuben, Gad, and the half-tribe of Manasseh — after they crossed the Jordan to return to their inheritance. The name does not appear in the Hebrew text of Joshua 22:34 as a proper noun but is supplied in many translations from context; the verse states that \"the children of Reuben and the children of Gad called the altar Ed, meaning: it is a witness between us that the LORD is God.\"</p><p>The altar caused a crisis in Israel: the western tribes assembled for war against the eastern tribes, fearing that the altar represented a schismatic rival sanctuary in violation of the centralized worship law. The eastern tribes clarified that the altar was not for burnt offering or sacrifice but solely as a memorial witness (<em>ed</em>) between the two groups of tribes — that the eastern tribes retained their portion in the LORD even though separated by the Jordan. The crisis resolved peacefully when the intent was understood. The episode illustrates the high value Israel placed on unity of worship and the potential for symbols to be misread without explanation.</p>",
        "hitchcock_meaning": "witness",
        "source_ids": {"easton": "ed", "smith": "ed"},
        "key_refs": ["Joshua 22:10", "Joshua 22:26", "Joshua 22:34"]
    },
    "edar": {
        "id": "edar",
        "term": "Edar",
        "category": "places",
        "intro": "<p>Edar (meaning <em>tower of the flock</em>) was a tower or landmark between Bethlehem and Hebron in the hill country of Judah, near which Jacob pitched his tent after the death and burial of Rachel at Bethlehem (Genesis 35:21). The name suggests a watchtower used by shepherds to guard their flocks — a common feature of the pastoral landscape of Judah. Beyond Jacob's encampment here, the place receives no further narrative development in the Old Testament canonical text.</p><p>Micah 4:8 contains the phrase \"O tower of the flock (<em>migdal-eder</em>), the stronghold of the daughter of Zion,\" which is sometimes identified with Edar and taken as a messianic reference to Bethlehem's vicinity as the origin point of the coming king. Jewish tradition locates the tower near the fields where the shepherds received the angelic announcement of Christ's birth (Luke 2:8–15), though this connection is traditional rather than explicit in the text.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "edar"},
        "key_refs": ["Genesis 35:21", "Micah 4:8"]
    },
    "eden": {
        "id": "eden",
        "term": "Eden",
        "category": "places",
        "intro": "<p>Eden (meaning <em>delight</em> or <em>pleasure</em>) is the garden in which God placed the first human beings, Adam and Eve, described in Genesis 2–3. The garden was located in the east and was watered by a river that divided into four streams: Pishon, Gihon, Hiddekel (Tigris), and Euphrates. The mention of the Tigris and Euphrates suggests a location in the broader Mesopotamian region, though the exact site cannot be determined. Eden contained every tree pleasant to the sight and good for food, including the tree of life and the tree of the knowledge of good and evil.</p><p>After the fall, God drove Adam and Eve from Eden and placed cherubim with a flaming sword to guard the way to the tree of life (Genesis 3:24). In prophetic literature, Eden becomes a symbol of primordial abundance: Ezekiel uses it as a standard of comparison for the glory of Tyre (Ezekiel 28:13; 31:9) and of restored Israel (Ezekiel 36:35). Isaiah 51:3 promises that the LORD will make Zion's wilderness like Eden. Revelation's vision of the new creation (Revelation 22:1–2) alludes to Eden's restoration in the river of life and the tree of life, bringing the biblical narrative to its eschatological resolution.</p>",
        "hitchcock_meaning": "pleasure; delight",
        "source_ids": {"easton": "eden", "isbe": "eden"},
        "key_refs": ["Genesis 2:8", "Genesis 3:24", "Ezekiel 28:13", "Revelation 22:2"]
    },
    "eder": {
        "id": "eder",
        "term": "Eder",
        "category": "places",
        "intro": "<p>Eder (meaning <em>flock</em>) is the name of a city in the south of Judah near the border of Idumea (Edom), listed in Joshua 15:21 among the southernmost towns of the tribe of Judah. It is also the name of a descendant of Beriah in the genealogies of Benjamin (1 Chronicles 8:15) and a Levite in the time of Hezekiah (1 Chronicles 23:23; 24:30). The city of Eder lay in the Negev region — the semi-arid southern zone of Judah that bordered Edom — and would have been a modest settlement in a sparsely populated frontier area.</p>",
        "hitchcock_meaning": "a flock",
        "source_ids": {"easton": "eder", "smith": "eder"},
        "key_refs": ["Joshua 15:21", "1 Chronicles 23:23"]
    },
    "edom": {
        "id": "edom",
        "term": "Edom",
        "category": "places",
        "intro": "<p>Edom (meaning <em>red</em> or <em>earthy</em>) is both the personal name given to Esau at the time of his selling his birthright — \"Feed me with that same red (<em>edom</em>) pottage\" (Genesis 25:30) — and the name of the nation descended from him, inhabiting the rugged terrain south and southeast of the Dead Sea. The Edomites controlled the mountainous region of Seir (also called Mount Seir), with their capital at Sela (later Petra), and occupied key trade routes between the Red Sea and Canaan. They were thus a significant regional power throughout the Old Testament period.</p><p>Israel and Edom maintained a relationship of perpetual tension rooted in the rivalry of Jacob and Esau: Edom refused Israel passage through their territory during the Exodus (Numbers 20:14–21), and later Edomite hostility culminated in their role during the Babylonian sack of Jerusalem, when they encouraged its destruction and seized refugees (Obadiah 10–14). The prophets pronounce judgment against Edom with particular severity (Isaiah 34; Jeremiah 49:7–22; Ezekiel 35; Obadiah). Theologically, Edom functions in the prophetic texts as a type of the nations opposed to God's purposes, whose ultimate fate is judgment.</p>",
        "hitchcock_meaning": "red, earthy; of blood",
        "source_ids": {"easton": "edom"},
        "key_refs": ["Genesis 25:30", "Numbers 20:18", "Isaiah 34:5", "Obadiah 10"]
    },
    "edrei": {
        "id": "edrei",
        "term": "Edrei",
        "category": "places",
        "intro": "<p>Edrei (meaning <em>mighty</em> or <em>strength</em>) is the name of two places in the Old Testament. The more significant is one of the chief cities of the kingdom of Bashan, east of the Jordan in the territory of Og, where Moses and the Israelites defeated Og in battle (Numbers 21:33; Deuteronomy 3:1). This was a pivotal victory that opened the Transjordan region to Israel and demonstrated that even the giant Rephaim kings were no match for the LORD's power. Edrei has been identified with the modern site of Der'a in southern Syria.</p><p>A second Edrei appears as a city in the territory allotted to Naphtali (Joshua 19:37). The Bashan Edrei is the more historically significant, as the defeat of Og at Edrei became a standard reference point in Israel's recollection of the conquest (Deuteronomy 3:10; Joshua 12:4; 13:12), affirming God's faithfulness to give Israel the land he had promised.</p>",
        "hitchcock_meaning": "a very great mass, or cloud",
        "source_ids": {"easton": "edrei", "smith": "edrei"},
        "key_refs": ["Numbers 21:33", "Deuteronomy 3:1", "Joshua 13:12"]
    },
    "effectual-call": {
        "id": "effectual-call",
        "term": "Effectual Call",
        "category": "concepts",
        "intro": "<p>Effectual call is a Reformed theological term for the inward work of the Holy Spirit by which God brings the elect to saving faith. It is distinguished from the general or outward call — the gospel invitation extended to all who hear the preached word — in that the effectual call invariably accomplishes its purpose: those effectively called are regenerated, illumined to understand the gospel, and moved to respond with faith and repentance. The concept draws primarily from Romans 8:30 (\"those he called, he also justified\"), 1 Corinthians 1:23–24 (\"to those who are called, both Jews and Greeks, Christ the power of God and the wisdom of God\"), and Ephesians 1:4–5.</p><p>The Easton's entry notes that Scripture distinguishes (1) the election of individuals to privilege — as in the calling of Abraham, Isaac, and Jacob — and (2) election to eternal life. The effectual call is the means by which the eternal decree of election is applied in time. Arminian theology disputes the irresistibility of the call, holding that God's grace can be finally resisted, while Reformed theology maintains that the call produces what it announces because it is God's own power at work rather than merely an invitation awaiting human response.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "effectual-call"},
        "key_refs": ["Romans 8:30", "1 Corinthians 1:24", "Ephesians 1:4", "2 Thessalonians 2:13"]
    },
    "effectual-prayer": {
        "id": "effectual-prayer",
        "term": "Effectual Prayer",
        "category": "concepts",
        "intro": "<p>Effectual prayer is the phrase used in the KJV rendering of James 5:16: \"The effectual fervent prayer of a righteous man availeth much.\" The Revised Version renders the same phrase as \"the supplication of a righteous man availeth much in its working,\" reflecting the Greek <em>deēsis energoumenē</em> — literally \"a prayer being energized\" or \"prayer that works.\" The text points to prayer that is active and earnest rather than mechanical or rote, connected to the righteousness and faith of the one who prays.</p><p>James grounds the statement in the example of Elijah, who prayed that it would not rain and it did not rain for three and a half years, then prayed again and rain came (James 5:17–18; 1 Kings 17–18). The passage locates prayer's power not in the technique or eloquence of the pray-er but in the character (righteous) and earnestness (fervent) of the prayer and ultimately in the God who answers. The verse has been foundational for Protestant teaching on intercessory prayer and for pneumatic traditions that emphasize prayer as an active, Spirit-empowered exercise.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "effectual-prayer"},
        "key_refs": ["James 5:16", "James 5:17", "1 Kings 18:42"]
    },
    "egg": {
        "id": "egg",
        "term": "Egg",
        "category": "concepts",
        "intro": "<p>Eggs appear in Scripture primarily as symbols of fragility, abandonment, and common provision. The Hebrew <em>beytsah</em> (meaning \"whiteness\") refers to eggs in general; the text most commonly mentions bird eggs in metaphorical contexts. Isaiah 10:14 uses deserted eggs as a figure for how effortlessly the Assyrian king plundered the nations: \"as one gathereth eggs that are left, have I gathered all the earth.\" Deuteronomy 22:6–7 legislates that if a bird's nest with eggs is found, the mother bird must be let go even while the eggs are taken — a law that combines practical conservation with ethical concern for animal life.</p><p>Job 6:6 asks whether the tasteless egg can be eaten without salt, using the image to describe the flatness of his friends' counsel. Luke 11:12 places the egg in a series of contrasts: no loving father gives his child a scorpion when asked for an egg, illustrating the trustworthy goodness of God in answering prayer. The egg's simplicity and universality made it a ready image for ordinary provision and basic sustenance in the agrarian world of the Bible.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "egg"},
        "key_refs": ["Deuteronomy 22:6", "Isaiah 10:14", "Job 6:6", "Luke 11:12"]
    },
    "eglah": {
        "id": "eglah",
        "term": "Eglah",
        "category": "people",
        "intro": "<p>Eglah (meaning <em>heifer</em> or <em>chariot</em>) is listed as one of David's wives at Hebron, and the mother of his sixth son Ithream (2 Samuel 3:5; 1 Chronicles 3:3). Beyond this brief genealogical mention, nothing further is recorded about her in the Old Testament. Jewish tradition in the Talmud controversially identified Eglah with Michal, David's first wife, but this identification has no support in the biblical text itself, which treats them as distinct individuals in the list of David's wives and sons born at Hebron.</p>",
        "hitchcock_meaning": "heifer; chariot; round",
        "source_ids": {"easton": "eglah", "smith": "eglah"},
        "key_refs": ["2 Samuel 3:5", "1 Chronicles 3:3"]
    },
    "eglaim": {
        "id": "eglaim",
        "term": "Eglaim",
        "category": "places",
        "intro": "<p>Eglaim (meaning <em>drops of the sea</em> or <em>two ponds</em>) is a place name that appears in Isaiah 15:8 in the oracle against Moab: \"The cry is gone round about the borders of Moab; the howling thereof unto Eglaim, and the howling thereof unto Beer-elim.\" The site marked one of the boundary points for the spreading of Moab's lament in Isaiah's prophecy. It is sometimes identified with En-eglaim mentioned in Ezekiel 47:10, a location on the shore of the Dead Sea where fishermen would stand in the eschatological vision of the healing waters.</p><p>The exact location of Eglaim has not been definitively identified by modern archaeology, but both the Isaiah and Ezekiel contexts place it in the Moabite region east or southeast of the Dead Sea. Its significance in Scripture is solely as a geographic reference point within prophetic laments against Moab.</p>",
        "hitchcock_meaning": "drops of the sea",
        "source_ids": {"easton": "eglaim", "smith": "eglaim"},
        "key_refs": ["Isaiah 15:8", "Ezekiel 47:10"]
    },
    "eglon": {
        "id": "eglon",
        "term": "Eglon",
        "category": "people",
        "intro": "<p>Eglon (meaning related to <em>heifer</em> or <em>round</em>) is the name of the Moabite king who oppressed Israel for eighteen years during the period of the judges, and also the name of a Canaanite royal city in the lowlands of Judah. As a king, Eglon allied with the Ammonites and Amalekites to capture Jericho (the City of Palms) and exact tribute from Israel (Judges 3:12–14). His domination ended when Ehud the Benjaminite, a left-handed judge, gained a private audience with Eglon, drew a concealed double-edged sword with his left hand, and killed him. The text notes that Eglon was \"a very fat man\" — a detail central to the narrative mechanics and possibly a satirical touch.</p><p>The city of Eglon (Joshua 10; 15:39) was one of the five Amorite cities whose kings allied against Gibeon and were defeated by Joshua. Its king Debir was among those killed and hanged by Joshua (Joshua 10:26). The city was later allotted to Judah.</p>",
        "hitchcock_meaning": "same as Eglah",
        "source_ids": {"easton": "eglon", "smith": "eglon"},
        "key_refs": ["Judges 3:12", "Judges 3:15", "Judges 3:21", "Joshua 10:3"]
    },
    "egypt": {
        "id": "egypt",
        "term": "Egypt",
        "category": "places",
        "intro": "<p>Egypt (Hebrew <em>Mitzraim</em>, meaning <em>the two Egypts</em> — Upper and Lower Egypt) is the ancient civilization centered on the Nile valley, one of the oldest and most powerful kingdoms of the ancient world and one of the most significant settings in biblical history. The patriarchs descended to Egypt during famines (Genesis 12:10; 42), and the entire covenant nation was born during the period of Egyptian bondage — 430 years of sojourn culminating in the exodus under Moses (Exodus 12:40–41). Egypt is thus the primary backdrop for the formative event of Old Testament theology: the deliverance of Israel from slavery.</p><p>Throughout the prophetic literature, Egypt represents the temptation of political alliance and worldly security in place of trust in the LORD (Isaiah 30:1–5; 31:1–3; Hosea 7:11). At the same time, prophets also foresee Egypt's ultimate redemption: Isaiah 19:18–25 envisions Egypt worshipping the LORD alongside Israel and Assyria, called \"my people\" and \"the work of my hands.\" In the New Testament, the flight to Egypt (Matthew 2:13–15) echoes the exodus typology, and Revelation 11:8 uses \"Egypt\" figuratively for the great city where the Lord was crucified, denoting the place of bondage and opposition to God's people.</p>",
        "hitchcock_meaning": "that troubles or oppresses; anguish",
        "source_ids": {"easton": "egypt", "isbe": "egypt"},
        "key_refs": ["Exodus 12:40", "Isaiah 30:1", "Isaiah 19:25", "Matthew 2:13"]
    },
    "ehud": {
        "id": "ehud",
        "term": "Ehud",
        "category": "people",
        "intro": "<p>Ehud (meaning <em>he that praises</em>) was the second major judge of Israel, raised up by God to deliver Israel from eighteen years of oppression under Eglon king of Moab (Judges 3:15–30). He was the son of Gera, a Benjaminite, and notably left-handed — an unusual characteristic that became central to the deliverance narrative. Sent to bring tribute to Eglon, Ehud concealed a cubit-long double-edged dagger on his right thigh (where a left-handed man would not normally be expected to carry a weapon), gained a private audience with the king on the pretext of a secret message from God, and killed him.</p><p>After the assassination, Ehud escaped before the body was discovered, summoned the Israelites, seized the Jordan fords, and led a victory against Moab in which ten thousand men were killed. Following Ehud's judgeship, the land had peace for eighty years (Judges 3:30). A second Ehud appears in 1 Chronicles 7:10 as a great-grandson of Benjamin. Ehud is listed in Judges among the judges who were raised up as deliverers, demonstrating that God works through morally complex means and unlikely instruments to preserve his covenant people.</p>",
        "hitchcock_meaning": "he that praises",
        "source_ids": {"easton": "ehud", "smith": "ehud", "isbe": "ehud"},
        "key_refs": ["Judges 3:15", "Judges 3:20", "Judges 3:28", "Judges 3:30"]
    },
    "ekron": {
        "id": "ekron",
        "term": "Ekron",
        "category": "places",
        "intro": "<p>Ekron (meaning <em>barrenness</em> or <em>torn away</em>) was the most northerly of the five major Philistine cities (the Pentapolis), the others being Gaza, Ashdod, Ashkelon, and Gath. It lay in the Shephelah (the lowland foothills between the coastal plain and the hill country of Judah) and controlled an important route between the coast and the interior. Ekron is first mentioned in Joshua 13:3 as part of the coastal territory not fully subdued, and it remained a bone of contention between Israel and the Philistines throughout the era of the judges and the early monarchy.</p><p>The Philistines brought the captured ark of God to Ekron (1 Samuel 5:10), where it caused a plague that prompted its return to Israel. The god Baal-zebub (\"lord of the flies\") was worshipped at Ekron, and Ahaziah king of Israel sent to consult him — earning prophetic rebuke from Elijah (2 Kings 1:2–16). Ekron was allotted to Judah (Joshua 15:11) and later to Dan (Joshua 19:43), though Philistine control made these allotments largely theoretical. Prophets including Zephaniah (2:4) and Zechariah (9:5–7) pronounced judgment against the city.</p>",
        "hitchcock_meaning": "barrenness; torn away",
        "source_ids": {"easton": "ekron"},
        "key_refs": ["Joshua 13:3", "1 Samuel 5:10", "2 Kings 1:2", "Zephaniah 2:4"]
    },
    "el-bethel": {
        "id": "el-bethel",
        "term": "El-Bethel",
        "category": "places",
        "intro": "<p>El-Bethel (meaning <em>God of Bethel</em>) is the name Jacob gave to the place where he built an altar upon his return from Paddan-aram, in obedience to God's command to return to Bethel and dwell there (Genesis 35:6–7). At this site, Jacob gathered his household, put away their foreign gods and earrings, purified themselves, and went up to Bethel — the same place where God had appeared to him in his flight from Esau decades before. Jacob named the altar \"El-Bethel\" in commemoration of the God who had revealed himself there.</p><p>The site thus marks the culmination of Jacob's covenant journey: from the initial theophany at Bethel when he fled (Genesis 28:19), through his years with Laban, back to a renewed encounter with God at the same sacred location. The naming acknowledges that the significance of Bethel lay not in the place itself but in the God who met Jacob there. God subsequently appeared to Jacob again at this site and confirmed the name Israel and the Abrahamic promises (Genesis 35:9–13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "el-bethel"},
        "key_refs": ["Genesis 35:6", "Genesis 35:7", "Genesis 28:19"]
    },
    "el-elohe-isreal": {
        "id": "el-elohe-isreal",
        "term": "El-elohe-Israel",
        "category": "concepts",
        "intro": "<p>El-elohe-Israel (meaning <em>Mighty One, God of Israel</em>, or <em>God, the God of Israel</em>) is the name Jacob gave to the altar he erected at Shechem after his peaceful return from Paddan-aram and his tense meeting with Esau (Genesis 33:18–20). Having purchased a parcel of ground from the sons of Hamor, Jacob set up the altar there as an act of worship acknowledging the God who had protected him through all his years away from Canaan and had brought him back safely.</p><p>The name is theologically significant: Jacob identifies the deity he worships specifically as \"the God of Israel\" — using his covenant name Israel rather than his birth name Jacob. This represents Jacob's full embrace of his God-given identity after the wrestling at Peniel (Genesis 32:28). The altar at Shechem positioned God's claim in the heart of Canaan, at the location where Abram had first built an altar upon entering the promised land (Genesis 12:6–7), connecting Jacob's worship to the covenant inheritance of the patriarchs.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "el-elohe-isreal"},
        "key_refs": ["Genesis 33:18", "Genesis 33:20", "Genesis 32:28"]
    },
    "elah": {
        "id": "elah",
        "term": "Elah",
        "category": "places",
        "intro": "<p>Elah (meaning <em>terebinth</em> or <em>oak</em>) is the name of a valley and several individuals in the Old Testament. The Valley of Elah, named for the terebinth trees that lined it, is the site of the famous confrontation between David and Goliath (1 Samuel 17:2, 19) — one of the most celebrated narratives in Scripture. The valley lies southwest of Jerusalem in the Shephelah, at the foot of the Judean hills, and marked a strategic boundary between Israelite and Philistine territory. David selected five smooth stones from a brook in the valley for his sling.</p><p>Among the individuals named Elah: (1) a chief of Edom descended from Esau (Genesis 36:41); (2) Elah son of Baasha, king of Israel for two years before being assassinated by Zimri in a conspiracy (1 Kings 16:8–10), fulfilling Jehu's prophecy against Baasha's house; (3) the father of Hoshea, the last king of Israel (2 Kings 15:30); and (4) a son of Caleb (1 Chronicles 4:15). The valley retains a variation of its ancient name today as Wadi es-Sant.</p>",
        "hitchcock_meaning": "an oak; a curse; perjury",
        "source_ids": {"easton": "elah", "smith": "elah"},
        "key_refs": ["1 Samuel 17:2", "1 Samuel 17:19", "1 Kings 16:8", "Genesis 36:41"]
    },
    "elam": {
        "id": "elam",
        "term": "Elam",
        "category": "places",
        "intro": "<p>Elam was both a personal name — Elam son of Shem in the table of nations (Genesis 10:22) — and the ancient kingdom that bore his name, located in the mountainous region east and northeast of Babylon, corresponding roughly to the modern Iranian province of Khuzestan and parts of the Zagros mountains. One of the oldest civilizations of the ancient Near East, Elam was at various periods a rival to Babylon and Assyria. The Elamite king Chedorlaomer appears in Genesis 14 as the leader of the eastern coalition that Genesis 14 describes Abraham's forces defeating.</p><p>The prophets address Elam in oracles of both judgment and restoration: Jeremiah 49:34–39 delivers a divine word against Elam at the beginning of Zedekiah's reign; Isaiah 11:11 includes Elam among the scattered nations from which the LORD will gather the remnant of Israel; and in a remarkable passage, Isaiah 21:2 calls Elam to attack Babylon. By the New Testament period, Elamites were present in Jerusalem at Pentecost and heard the apostles speaking in their language (Acts 2:9), fulfilling the breadth of the Spirit's outpouring among all nations.</p>",
        "hitchcock_meaning": "a young man; a virgin; a secret",
        "source_ids": {"easton": "elam", "smith": "elam", "isbe": "elam"},
        "key_refs": ["Genesis 10:22", "Genesis 14:1", "Isaiah 11:11", "Acts 2:9"]
    },
    "elasah": {
        "id": "elasah",
        "term": "Elasah",
        "category": "people",
        "intro": "<p>Elasah (meaning <em>the doings of God</em> or <em>God has made</em>) is the name of two individuals in the Old Testament. The first is a son of Helez, descendant of Judah from the family of Hezron (1 Chronicles 2:39–40). The second, and more historically notable, is Elasah son of Shaphan, who was one of the two envoys sent by King Zedekiah to King Nebuchadnezzar in Babylon — and who carried the famous letter of Jeremiah to the Jewish exiles in Babylon instructing them to settle in the land, seek its welfare, and not believe the false prophets who promised quick return (Jeremiah 29:3). This Elasah came from the family of Shaphan, which was generally sympathetic to Jeremiah's ministry. Ezra 10:22 also lists an Elasah among those who had married foreign wives and agreed to put them away.</p>",
        "hitchcock_meaning": "the doings of God",
        "source_ids": {"easton": "elasah", "smith": "elasah"},
        "key_refs": ["Jeremiah 29:3", "1 Chronicles 2:39", "Ezra 10:22"]
    },
    "elath": {
        "id": "elath",
        "term": "Elath",
        "category": "places",
        "intro": "<p>Elath (also Eloth; meaning <em>grove</em>, <em>hind</em>, or <em>trees</em>) was an ancient seaport at the northeastern tip of the Red Sea's Gulf of Aqaba, strategically positioned at the crossroads of trade routes connecting Egypt, Arabia, Africa, and the eastern Mediterranean. The site is mentioned in Deuteronomy 2:8 as Israel passed through it during the wilderness journey, and it became significant as a harbor in the days of Solomon, who built a fleet at the nearby Ezion-gaber (1 Kings 9:26) to trade with Ophir for gold.</p><p>Control of Elath fluctuated between Israel and Edom: Azariah (Uzziah) king of Judah recovered and rebuilt Elath (2 Kings 14:22; 2 Chronicles 26:2), but Edom subsequently regained it during the reign of Ahaz (2 Kings 16:6), after which it remained in Edomite (later Nabatean and Roman) hands. The site is now Aqaba, Jordan, and Eilat, Israel — modern cities that preserve the ancient strategic importance of the location as a gateway between the Red Sea and the land routes of the Levant.</p>",
        "hitchcock_meaning": "a hind; strength; an oak",
        "source_ids": {"easton": "elath"},
        "key_refs": ["Deuteronomy 2:8", "1 Kings 9:26", "2 Kings 14:22", "2 Kings 16:6"]
    },
    "eldad": {
        "id": "eldad",
        "term": "Eldad",
        "category": "people",
        "intro": "<p>Eldad (meaning <em>favored of God</em> or <em>God has loved</em>) was one of the seventy elders chosen by Moses at God's command to share the burden of leadership over Israel in the wilderness (Numbers 11:16–30). For reasons not explained in the text, Eldad and his companion Medad did not go out to the tabernacle when the Spirit came upon the seventy elders; instead, they remained in the camp — yet the Spirit rested upon them there and they prophesied among the people.</p><p>When Joshua son of Nun reported this to Moses and urged him to forbid them, Moses gave a remarkable response: \"Enviest thou for my sake? would God that all the LORD's people were prophets, and that the LORD would put his spirit upon them!\" (Numbers 11:29). The episode is frequently cited in discussions of the Spirit's freedom and the democratization of prophecy, and it anticipates Joel's promise that God would pour out his Spirit on all flesh (Joel 2:28–29), fulfilled at Pentecost (Acts 2:16–18).</p>",
        "hitchcock_meaning": "favored of God; love of God",
        "source_ids": {"easton": "eldad", "smith": "eldad"},
        "key_refs": ["Numbers 11:26", "Numbers 11:28", "Numbers 11:29", "Joel 2:28"]
    },
    "elder": {
        "id": "elder",
        "term": "Elder",
        "category": "concepts",
        "intro": "<p>Elder (Hebrew <em>zaqen</em>; Greek <em>presbyteros</em>) is one of the oldest and most persistent institutional offices in biblical society, functioning in Israel as both a social and religious leadership role throughout all periods of the Old Testament and continuing in a transformed form in the New Testament church. In the patriarchal period, elders governed tribal clans by seniority and wisdom. Moses appointed seventy elders to assist in governing Israel (Numbers 11:16–17), and the system of elders as a governing body appears throughout the historical books as the representative leadership of the community (Deuteronomy 27:1; Joshua 7:6; 1 Samuel 4:3).</p><p>In the New Testament, elders (<em>presbyteroi</em>) are among the primary officers of the local church, alongside deacons and overseers (<em>episkopoi</em>). Paul's letters to Timothy and Titus specify qualifications for elders (1 Timothy 3:1–7; Titus 1:5–9), and James 5:14 instructs the sick to call for the elders of the church to pray. The terms <em>elder</em> and <em>overseer/bishop</em> appear to be used interchangeably in some passages (Acts 20:17, 28; Titus 1:5, 7), leading to significant debate about church governance in church history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "elder", "smith": "elder", "isbe": "elder"},
        "key_refs": ["Numbers 11:16", "Deuteronomy 27:1", "1 Timothy 3:1", "Titus 1:5"]
    },
    "elealeh": {
        "id": "elealeh",
        "term": "Elealeh",
        "category": "places",
        "intro": "<p>Elealeh (meaning <em>God has ascended</em> or <em>burnt-offering of God</em>) was a town in the pastoral territory east of the Jordan, originally belonging to the kingdom of Sihon king of the Amorites and captured by Israel (Numbers 32:3). It was assigned to the tribe of Reuben, which rebuilt it (Numbers 32:37). Elealeh lay in close proximity to Heshbon, the chief city of the region, and appears alongside Heshbon in the prophetic oracles against Moab in Isaiah 15:4 and 16:9, where the prophet grieves over the devastation of the lush agricultural region.</p><p>The site has been identified with the modern ruin of el-Al, a short distance northeast of Heshbon (modern Hesban) in the highlands of Transjordan. Jeremiah 48:34 also includes Elealeh in the lament over Moab, indicating that by Jeremiah's time the town had come under Moabite control again — consistent with the area's frequent change of hands between Israel, Moab, and later Ammon.</p>",
        "hitchcock_meaning": "burnt-offering of God",
        "source_ids": {"easton": "elealeh", "smith": "elealeh"},
        "key_refs": ["Numbers 32:3", "Numbers 32:37", "Isaiah 15:4", "Jeremiah 48:34"]
    },
    "eleazar": {
        "id": "eleazar",
        "term": "Eleazar",
        "category": "people",
        "intro": "<p>Eleazar (meaning <em>God has helped</em>) was the third son of Aaron and Elisheba, and the successor to his father as High Priest of Israel (Numbers 20:28). After the deaths of his two elder brothers Nadab and Abihu, who were struck down for offering unauthorized fire before the LORD (Leviticus 10:1–2), Eleazar became Aaron's heir apparent. He was appointed to supervise the Levites (Numbers 3:32) and was given charge of the sanctuary furnishings during the wilderness journey. When Aaron died on Mount Hor, Moses transferred the priestly vestments to Eleazar in the sight of the congregation, formally installing him as High Priest (Numbers 20:25–28).</p><p>Eleazar partnered with Joshua in the distribution of Canaan by lot among the twelve tribes (Joshua 14:1; 19:51), playing the priestly role in the formal allotment process. He is listed in 1 Chronicles 6 in the priestly genealogy, and his son Phinehas — who showed zealous action at Baal-peor (Numbers 25:7–13) — continued the high-priestly line. Eleazar died and was buried at Gibeah in the hill country of Ephraim, in a field belonging to his son Phinehas (Joshua 24:33).</p>",
        "hitchcock_meaning": "help of God, court of God",
        "source_ids": {"easton": "eleazar", "smith": "eleazar", "isbe": "eleazar"},
        "key_refs": ["Exodus 6:23", "Numbers 20:28", "Joshua 14:1", "Joshua 24:33"]
    },
    "elect-lady": {
        "id": "elect-lady",
        "term": "Elect Lady",
        "category": "concepts",
        "intro": "<p>The \"elect lady\" is the addressee of the Second Epistle of John (2 John 1:1): \"The elder unto the elect lady and her children, whom I love in the truth.\" The identity has been debated since the early church. Some interpreters take \"elect lady\" as referring to a specific named woman — possibly Kyria (a proper name corresponding to the Greek word for \"lady\") — along with her literal children. Others hold that the phrase is a collective metaphor for a local church personified as a woman (consistent with the feminine personification of communities in the Old Testament), with \"her children\" as the church members.</p><p>The closing verse (2 John 1:13) — \"the children of thy elect sister greet thee\" — supports the metaphorical interpretation: a sister church sends greetings. The letter's content, which warns against receiving teachers who deny that Christ came in the flesh, addresses the community's need to exercise discernment about itinerant teachers. The title \"elect lady\" in either reading emphasizes the dignity and God's choosing of the community or individual addressed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "elect-lady"},
        "key_refs": ["2 John 1:1", "2 John 1:13"]
    },
    "election-of-grace": {
        "id": "election-of-grace",
        "term": "Election of Grace",
        "category": "concepts",
        "intro": "<p>Election of grace is the biblical doctrine that God sovereignly chooses — from before the foundation of the world and apart from foreseen human merit — those who will be saved through Jesus Christ. The phrase comes from Romans 11:5: \"Even so then at this present time also there is a remnant according to the election of grace.\" Paul contrasts election of grace with election \"of works\" to establish that if God's choosing were based on anything in the creature, grace would no longer be grace.</p><p>The Scripture speaks of election at multiple levels: the election of the nation of Israel as God's covenant people (Deuteronomy 7:6; Romans 9:4–5), the election of individuals within the nation to specific offices or roles (Saul, David), and the election of individuals to eternal life (Ephesians 1:4–5; 2 Thessalonians 2:13; 1 Peter 1:2). Debates between Reformed (Calvinist) and Arminian theology center on whether election is unconditional (based solely on God's sovereign will) or conditional (based on God's foreknowledge of human faith). The pastoral weight of the doctrine, as Paul presents it in Romans 8:29–30, is assurance: those God foreknew, predestined, called, justified, and glorified form an unbreakable chain that no created power can interrupt.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "election-of-grace"},
        "key_refs": ["Romans 11:5", "Ephesians 1:4", "2 Thessalonians 2:13", "1 Peter 1:2"]
    },
    "elements": {
        "id": "elements",
        "term": "Elements",
        "category": "concepts",
        "intro": "<p>The Greek word <em>stoicheia</em>, translated \"elements\" in the New Testament, carries a range of meanings that have generated significant interpretive debate. In its primary sense it denotes the basic constituents or rudimentary principles of any system. Peter uses it for the physical elements of the cosmos that will be dissolved at the last day (2 Peter 3:10, 12). Paul's usage is more controversial: in Galatians 4:3, 9 and Colossians 2:8, 20, <em>stoicheia</em> appears in the context of the Mosaic law and Gentile religious observance — \"weak and beggarly elements\" or \"elements of the world\" to which Paul says believers were formerly enslaved.</p><p>Interpreters debate whether Paul means (a) the basic spiritual forces or powers behind pagan religion and the law as externally imposed systems, (b) the elementary teachings or \"ABCs\" of pre-Christian religion, or (c) angelic intermediaries associated with the cosmos. In any reading, Paul's point is that faith in Christ has freed believers from bondage to these elementary principles, and returning to them — whether through Jewish calendar observances or Colossian asceticism — represents a regression rather than spiritual advance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "elements"},
        "key_refs": ["Galatians 4:3", "Galatians 4:9", "Colossians 2:8", "2 Peter 3:10"]
    },
    "elephant": {
        "id": "elephant",
        "term": "Elephant",
        "category": "concepts",
        "intro": "<p>The elephant is not named directly in the canonical Hebrew or Greek text of Scripture, but it is present indirectly: the word translated \"ivory\" in the Old Testament (Hebrew <em>shen-habbim</em>, literally \"tooth of the elephant\" or \"tooth of ivory\") indicates the animal's product was well-known in Israel, even if the animal itself was not native to Canaan. Solomon's great ivory throne (1 Kings 10:18) and the ivory palaces and beds of wealthy Israelites condemned by Amos (Amos 3:15; 6:4) all presuppose extensive trade in elephant ivory from Africa and India.</p><p>The Greek word <em>elephantinos</em> (ivory) in Revelation 18:12 appears in the list of luxury goods that the merchants of the great city traded. War elephants appear prominently in the deuterocanonical books of 1 and 2 Maccabees, where the Seleucid armies deployed them against the Jewish forces of Judas Maccabaeus — and Eleazar Maccabaeus died in a famous incident by driving a spear beneath an elephant he believed to carry the king (1 Maccabees 6:43–46). The elephant thus appears in biblical tradition primarily as a symbol of luxury trade and military power.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "elephant"},
        "key_refs": ["1 Kings 10:18", "Amos 3:15", "Revelation 18:12"]
    },
    "elhanan": {
        "id": "elhanan",
        "term": "Elhanan",
        "category": "people",
        "intro": "<p>Elhanan (meaning <em>grace of God</em>, <em>gift of God</em>, or <em>mercy of God</em>) is the name of two warriors in the service of David. The first is mentioned in 2 Samuel 21:19 as slaying Goliath the Gittite — a statement that appears to contradict the account of David slaying Goliath in 1 Samuel 17. The parallel passage in 1 Chronicles 20:5 resolves this by specifying that Elhanan son of Jair killed Lahmi the brother of Goliath, suggesting a scribal error or textual corruption in the Samuel text where \"Goliath\" was substituted for \"Lahmi the brother of Goliath.\"</p><p>The second Elhanan, son of Dodo of Bethlehem, is listed among David's thirty mighty men — an elite warrior corps whose exploits are recounted in 2 Samuel 23:24 and 1 Chronicles 11:26. The name's meaning and the warrior context in which both men appear suggest a tradition of valiant service in David's campaigns against the Philistines.</p>",
        "hitchcock_meaning": "grace, or gift, or mercy of God",
        "source_ids": {"easton": "elhanan", "smith": "elhanan"},
        "key_refs": ["2 Samuel 21:19", "1 Chronicles 20:5", "2 Samuel 23:24"]
    },
    "eli": {
        "id": "eli",
        "term": "Eli",
        "category": "people",
        "intro": "<p>Eli (meaning <em>the offering</em> or <em>the lifting up</em>) was the high priest of Israel at Shiloh during the formative period when Samuel was called to prophetic ministry. A descendant of Ithamar, the younger son of Aaron, Eli judged Israel for forty years (1 Samuel 4:18). His tenure was marked by failure of parental discipline: his sons Hophni and Phinehas were corrupt priests who treated the offerings of the LORD with contempt and committed sexual immorality at the tabernacle entrance, and Eli rebuked them only mildly (1 Samuel 2:22–25).</p><p>God pronounced judgment on Eli's house through a man of God (1 Samuel 2:27–36) and confirmed it to the child Samuel (1 Samuel 3:11–14): the two sons would die on the same day, and Eli's priestly line would be cut off. The fulfillment came swiftly — the Philistines defeated Israel at Aphek, captured the ark, and killed Hophni and Phinehas in battle. When a messenger brought the news to Eli, he fell backward from his seat at the city gate, broke his neck, and died at age ninety-eight. The ark's capture prompted his daughter-in-law's dying cry: \"The glory has departed from Israel\" (<em>Ichabod</em>, 1 Samuel 4:21–22).</p>",
        "hitchcock_meaning": "the offering or lifting up",
        "source_ids": {"easton": "eli", "smith": "eli", "isbe": "eli"},
        "key_refs": ["1 Samuel 1:3", "1 Samuel 2:22", "1 Samuel 3:11", "1 Samuel 4:18"]
    },
    "eliab": {
        "id": "eliab",
        "term": "Eliab",
        "category": "people",
        "intro": "<p>Eliab (meaning <em>God is my father</em> or <em>God is the father</em>) is the name of several men in the Old Testament, the most prominent being David's eldest brother. When Samuel came to Jesse's house to anoint the next king, Eliab — tall and handsome — was the first candidate presented, and Samuel initially assumed he must be God's choice. But the LORD told Samuel: \"Look not on his countenance, or on the height of his stature... for the LORD seeth not as man seeth; for man looketh on the outward appearance, but the LORD looketh on the heart\" (1 Samuel 16:6–7). Eliab was passed over, and the youngest son David was anointed instead. Eliab later rebuked David at the battle against Goliath for leaving the sheep to watch the battle (1 Samuel 17:28).</p><p>Other men named Eliab include: a chief of the tribe of Zebulun in the wilderness census (Numbers 1:9); a Reubenite son of Pallu and father of Dathan and Abiram, who joined Korah's rebellion (Numbers 16:1); and a Levite musician appointed by David (1 Chronicles 15:18, 20; 16:5).</p>",
        "hitchcock_meaning": "God is my father; God is the father",
        "source_ids": {"easton": "eliab", "smith": "eliab"},
        "key_refs": ["1 Samuel 16:6", "1 Samuel 17:28", "Numbers 1:9", "Numbers 16:1"]
    },
    "eliada": {
        "id": "eliada",
        "term": "Eliada",
        "category": "people",
        "intro": "<p>Eliada (meaning <em>whom God cares for</em> or <em>knowledge of God</em>) is the name of two individuals in the Old Testament. The first is one of David's sons born after his establishment in Jerusalem, listed in 2 Samuel 5:16 and 1 Chronicles 3:8 among the children born to him there. This Eliada is also called Beeliada in 1 Chronicles 14:7, a variant that substitutes \"Baal\" for \"El\" in the name — likely reflecting a period when the title Baal (\"lord\") was used for the LORD without idolatrous connotation, and later revised due to Baal-worship associations.</p><p>The second Eliada was the father of Rezon, the leader of a band of Syrian raiders who became an adversary of Solomon throughout his reign (1 Kings 11:23). Rezon had fled from his master Hadadezer king of Zobah and became king of Damascus, harassing Israel as an instrument of divine discipline for Solomon's idolatry.</p>",
        "hitchcock_meaning": "knowledge of God",
        "source_ids": {"easton": "eliada", "smith": "eliada"},
        "key_refs": ["2 Samuel 5:16", "1 Chronicles 14:7", "1 Kings 11:23"]
    },
    "eliakim": {
        "id": "eliakim",
        "term": "Eliakim",
        "category": "people",
        "intro": "<p>Eliakim (meaning <em>whom God will raise up</em>) is the name of several men in the Old Testament, the most significant being the son of Hilkiah who served as palace administrator (<em>asher al-habayit</em>) under King Hezekiah of Judah. When Sennacherib's Assyrian forces besieged Jerusalem, Eliakim led the delegation that met the Rabshakeh at the conduit of the upper pool, where the Assyrian commander delivered his psychological warfare speech (2 Kings 18:18–27; Isaiah 36:3). Isaiah 22:20–25 contains a divine oracle appointing Eliakim to replace the corrupt steward Shebna: \"I will clothe him with thy robe and strengthen him with thy girdle... and I will fasten him as a nail in a sure place; and he shall be for a glorious throne to his father's house.\"</p><p>Isaiah's oracle about Eliakim is notably messianic in its language — particularly the imagery of the key of the house of David laid on his shoulder (Isaiah 22:22), which Revelation 3:7 applies to Christ. A second Eliakim was the son of Abiud in Matthew's genealogy of Jesus (Matthew 1:13), and a third appears in Luke 3:30 in a different section of the Lucan genealogy.</p>",
        "hitchcock_meaning": "resurrection of God",
        "source_ids": {"easton": "eliakim", "smith": "eliakim", "isbe": "eliakim"},
        "key_refs": ["2 Kings 18:18", "Isaiah 22:20", "Isaiah 22:22", "Revelation 3:7"]
    },
    "eliam": {
        "id": "eliam",
        "term": "Eliam",
        "category": "people",
        "intro": "<p>Eliam (meaning <em>God's people</em> or <em>the people of God</em>) is the name of two individuals in the Old Testament. The first is the father of Bathsheba, the wife of Uriah the Hittite and later of David (2 Samuel 11:3). The second, and possibly the same person, is listed among David's thirty mighty men as Eliam son of Ahithophel the Gilonite (2 Samuel 23:34). If these two are identical, it would make Bathsheba the granddaughter of Ahithophel, David's wise counselor who later betrayed him by advising Absalom — a detail that would add personal grievance to Ahithophel's political betrayal, since David had wronged Bathsheba's family.</p><p>The identification of the two Eliams remains uncertain, but the textual proximity in 2 Samuel makes the connection plausible and has been noted by commentators since antiquity as adding depth to the Ahithophel-David conflict narrative.</p>",
        "hitchcock_meaning": "the people of God",
        "source_ids": {"easton": "eliam", "smith": "eliam"},
        "key_refs": ["2 Samuel 11:3", "2 Samuel 23:34"]
    },
    "elias": {
        "id": "elias",
        "term": "Elias",
        "category": "people",
        "intro": "<p>Elias is the Greek form of the Hebrew name Elijah (meaning <em>God the Lord</em>, or <em>my God is Jehovah</em>), used throughout the New Testament and in the King James Version for all references to the great prophet. Matthew 11:14 records Jesus's declaration that John the Baptist, if the people would receive it, was the Elias (Elijah) who was to come — fulfilling Malachi 4:5's promise of the return of Elijah before the great and terrible day of the LORD. The disciples asked Jesus directly about this expectation (Matthew 17:10–13; Mark 9:11–13), and Jesus confirmed that John had come \"in the spirit and power of Elijah\" (Luke 1:17).</p><p>Elijah appeared in person at the Transfiguration alongside Moses, speaking with Jesus about his departure (Matthew 17:3; Luke 9:30–31). Bystanders at the cross misheard Jesus's cry \"Eli, Eli\" as a call to Elias/Elijah (Matthew 27:47). James 5:17 cites \"Elias\" as an example of effective prayer — a man of like passions who prayed and was answered dramatically. The New Testament's use of the Greek \"Elias\" for the Hebrew \"Elijah\" preserved a hope that was central to Jewish messianic expectation.</p>",
        "hitchcock_meaning": "same as Elijah",
        "source_ids": {"easton": "elias", "smith": "elias"},
        "key_refs": ["Matthew 11:14", "Matthew 17:3", "James 5:17", "Malachi 4:5"]
    },
    "eliashib": {
        "id": "eliashib",
        "term": "Eliashib",
        "category": "people",
        "intro": "<p>Eliashib (meaning <em>whom God will restore</em> or <em>the God of conversion</em>) is the name of several individuals in the Old Testament. The most prominent is the high priest during the time of Nehemiah, a grandson of the high priest Joshua who returned with Zerubbabel from Babylon. Eliashib supervised the rebuilding of the Sheep Gate during the wall-repair project under Nehemiah's leadership (Nehemiah 3:1), but he later compromised the community's covenant integrity by allowing Tobiah the Ammonite — a persistent opponent of the restoration — to use a large chamber in the temple courts as living quarters, which Nehemiah expelled on his return to Jerusalem (Nehemiah 13:4–9).</p><p>Other men named Eliashib include: a priest appointed over the eleventh course of priests under David (1 Chronicles 24:12); a Levite singer who had married a foreign woman and agreed to put her away under Ezra's reform (Ezra 10:24); and several laymen who had also married foreign women (Ezra 10:27, 36). The name thus appears across priestly, Levitical, and lay contexts in the restoration period.</p>",
        "hitchcock_meaning": "the God of conversion",
        "source_ids": {"easton": "eliashib", "smith": "eliashib"},
        "key_refs": ["Nehemiah 3:1", "Nehemiah 13:4", "Nehemiah 13:7", "1 Chronicles 24:12"]
    },
    "eliathah": {
        "id": "eliathah",
        "term": "Eliathah",
        "category": "people",
        "intro": "<p>Eliathah (meaning <em>to whom God will come</em> or <em>thou art my God</em>) was one of the fourteen sons of Heman the Levite musician — the king's seer in the service of the sanctuary appointed by David (1 Chronicles 25:4). Eliathah was assigned by lot to lead the twentieth course of Levitical musicians in the regular rotation of temple worship (1 Chronicles 25:27). His brothers were similarly assigned to serve in the elaborate musical program David organized for the tabernacle and later the temple, with all twenty-four courses of singers and instrumentalists serving under royal and divine direction.</p>",
        "hitchcock_meaning": "thou art my God",
        "source_ids": {"easton": "eliathah", "smith": "eliathah"},
        "key_refs": ["1 Chronicles 25:4", "1 Chronicles 25:27"]
    },
    "elidad": {
        "id": "elidad",
        "term": "Elidad",
        "category": "people",
        "intro": "<p>Elidad (meaning <em>whom God has loved</em> or <em>beloved of God</em>) was a leader of the tribe of Benjamin appointed by God to assist in the division of Canaan among the tribes (Numbers 34:21). He was the son of Chislon and served as one of the tribal representatives who, along with Joshua and Eleazar the high priest, oversaw the formal allotment of the land to the nine and a half tribes west of the Jordan following the completion of the military conquest. Beyond this single reference, Elidad receives no further mention in the biblical text.</p>",
        "hitchcock_meaning": "beloved of God",
        "source_ids": {"easton": "elidad", "smith": "elidad"},
        "key_refs": ["Numbers 34:21"]
    },
    "eliel": {
        "id": "eliel",
        "term": "Eliel",
        "category": "people",
        "intro": "<p>Eliel (meaning <em>to whom God is might</em> or <em>God, my God</em>) is the name of several men in the Old Testament, primarily in the genealogies and military lists of Chronicles. Among them: (1) a chief of the half-tribe of Manasseh east of the Jordan (1 Chronicles 5:24), listed among the heads of the tribe; (2) an ancestor of Elkanah and Samuel in the line of Kohath (1 Chronicles 6:34); (3) two heads of families in Benjamin (1 Chronicles 8:20, 22); (4) a Mahavite warrior among David's mighty men (1 Chronicles 11:46–47); (5) a Gadite who joined David at Ziklag (1 Chronicles 12:11); (6) a Levite porter (1 Chronicles 15:9, 11); and (7) an overseer of temple offerings under Hezekiah (2 Chronicles 31:13). The frequency of the name reflects its meaning's appeal as an expression of faith in God's power.</p>",
        "hitchcock_meaning": "God, my God",
        "source_ids": {"easton": "eliel", "smith": "eliel"},
        "key_refs": ["1 Chronicles 5:24", "1 Chronicles 11:46", "1 Chronicles 15:9"]
    },
    "eliezer": {
        "id": "eliezer",
        "term": "Eliezer",
        "category": "people",
        "intro": "<p>Eliezer (meaning <em>God his help</em> or <em>help of my God</em>) is most famous as the chief servant of Abraham, sent on the critical mission of finding a bride for Isaac from among Abraham's kindred in Mesopotamia (Genesis 24). Though his name is not given in Genesis 24 itself, the servant is almost universally identified with Eliezer of Damascus, described in Genesis 15:2 as the heir Abraham feared would inherit in the absence of a son: \"he that shall be heir of my house is this Eliezer of Damascus.\" His long journey to Paddan-aram and his prayer-guided discovery of Rebekah at the well constitute one of the most detailed and theologically rich narratives of divine guidance in Genesis.</p><p>Other notable men named Eliezer include: (1) the second son of Moses and Zipporah, whose name commemorated God's deliverance from Pharaoh (Exodus 18:4; 1 Chronicles 23:15); (2) a priest who blew the trumpet at the bringing of the ark to Jerusalem (1 Chronicles 15:24); (3) a son of Dodavahu who prophesied against Jehoshaphat's maritime venture (2 Chronicles 20:37); and (4) several men listed in Ezra who had married foreign wives (Ezra 10:18, 23, 31).</p>",
        "hitchcock_meaning": "help, or court, of my God",
        "source_ids": {"easton": "eliezer", "smith": "eliezer", "isbe": "eliezer"},
        "key_refs": ["Genesis 15:2", "Genesis 24:2", "Exodus 18:4", "1 Chronicles 23:15"]
    },
    "elihu": {
        "id": "elihu",
        "term": "Elihu",
        "category": "people",
        "intro": "<p>Elihu (meaning <em>whose God is he</em> or <em>he is my God himself</em>) appears most prominently in the book of Job as the son of Barachel the Buzite, of the family of Ram — a young man who had listened in growing frustration as Job and his three friends argued (Job 32:1–6). Unlike the three friends (Eliphaz, Bildad, and Zophar), Elihu waited to speak because of his youth, but he eventually offered four speeches (Job 32–37) in which he rebuked both Job (for self-righteousness) and the three friends (for failing to answer Job adequately while condemning him).</p><p>Elihu's speeches are structurally distinct from those of the three friends and from God's answer in the whirlwind; God's rebuke at the end of Job specifically names the three friends but not Elihu, leading to debate about whether his contribution is positively or negatively evaluated. Many commentators see Elihu as a transitional voice who moves the dialogue toward the divine speeches of chapters 38–41. Other men named Elihu include ancestors of Samuel (1 Samuel 1:1; 1 Chronicles 6:34), a Manassite warrior (1 Chronicles 12:20), a temple doorkeeper (1 Chronicles 26:7), and a brother of David (1 Chronicles 27:18).</p>",
        "hitchcock_meaning": "he is my God himself",
        "source_ids": {"easton": "elihu", "smith": "elihu"},
        "key_refs": ["Job 32:2", "Job 32:6", "Job 33:1", "Job 37:24"]
    },
    "elijah": {
        "id": "elijah",
        "term": "Elijah",
        "category": "people",
        "intro": "<p>Elijah (meaning <em>whose God is Jehovah</em>, or <em>God the LORD</em>) was among the most dramatic of Israel's prophets, active in the northern kingdom during the reigns of Ahab and Ahaziah in the ninth century BC. His ministry was characterized by supernatural acts and fierce confrontation with Baal worship under the influence of Queen Jezebel. His sudden appearance before Ahab to announce a three-and-a-half-year drought (1 Kings 17:1), his miraculous provision through the widow of Zarephath, the contest with 450 prophets of Baal at Mount Carmel (1 Kings 18), his flight and renewal at Horeb after Jezebel's threat, and his translation to heaven in a whirlwind without tasting death (2 Kings 2:11) make him one of the most vivid figures in the Old Testament.</p><p>Elijah's eschatological significance is profound: Malachi 4:5–6 promises that God will send Elijah before the great Day of the LORD to turn hearts. Jesus identified John the Baptist as the fulfillment of this promise \"in the spirit and power of Elijah\" (Luke 1:17; Matthew 11:14; 17:12). Elijah appeared alongside Moses at the Transfiguration (Matthew 17:3). James cites him as a model of effective intercessory prayer (James 5:17). In the New Testament, \"Elias\" is the Greek form used throughout.</p>",
        "hitchcock_meaning": "God the Lord, the strong Lord",
        "source_ids": {"easton": "elijah", "smith": "elijah", "isbe": "elijah"},
        "key_refs": ["1 Kings 17:1", "1 Kings 18:36", "2 Kings 2:11", "Malachi 4:5"]
    },
    "elika": {
        "id": "elika",
        "term": "Elika",
        "category": "people",
        "intro": "<p>Elika (meaning <em>pelican of God</em> or <em>God is his rejector</em>) was a Harodite warrior listed among David's thirty — the elite corps of mighty men whose individual exploits are commemorated in 2 Samuel 23:25 and 1 Chronicles 11:27. He was from Harod, a location in Issachar (Judges 7:1), and his inclusion in the list of thirty places him among the most distinguished warriors of David's kingdom. Beyond this military reference, nothing else is recorded about him in the biblical text.</p>",
        "hitchcock_meaning": "pelican of God",
        "source_ids": {"easton": "elika", "smith": "elika"},
        "key_refs": ["2 Samuel 23:25"]
    },
    "elim": {
        "id": "elim",
        "term": "Elim",
        "category": "places",
        "intro": "<p>Elim (meaning <em>trees</em>, <em>the rams</em>, or <em>the strong</em>) was the second named camp of the Israelites after their passage through the Red Sea, reached after the bitter waters of Marah had been sweetened (Exodus 15:27). The text describes it as a paradisiacal oasis in contrast to the surrounding desert: \"And they came to Elim, where were twelve wells of water, and threescore and ten palm trees: and they encamped there by the waters.\" The twelve wells and seventy palms have been symbolically interpreted — the twelve tribes and the seventy elders — but the text presents them straightforwardly as a place of rest and refreshment.</p><p>The location of Elim has been identified by many scholars with the Wadi Gharandel in the western Sinai peninsula, which still contains significant vegetation and water sources by desert standards. After Elim, the Israelites moved on to the Wilderness of Sin (Exodus 16:1; Numbers 33:9–11), where they complained about food and received the first gift of manna and quail. Elim's twelve springs mark it as one of the rare moments of ease and provision in the otherwise arduous wilderness journey.</p>",
        "hitchcock_meaning": "the rams; the strong; stags",
        "source_ids": {"easton": "elim", "smith": "elim", "isbe": "elim"},
        "key_refs": ["Exodus 15:27", "Numbers 33:9"]
    },
    "elimelech": {
        "id": "elimelech",
        "term": "Elimelech",
        "category": "people",
        "intro": "<p>Elimelech (meaning <em>God his king</em> or <em>my God is king</em>) was a man of the tribe of Judah from Bethlehem-judah, the husband of Naomi and father of Mahlon and Chilion (Ruth 1:2–3). During a famine in Canaan, Elimelech led his family to sojourn in Moab — a decision whose consequences form the opening tragedy of the book of Ruth. Shortly after arriving in Moab, Elimelech died, leaving Naomi a widow in a foreign land. His two sons then married Moabite women, Orpah and Ruth, and both sons also died within ten years, leaving the three women widowed and childless.</p><p>Elimelech's death sets in motion the chain of events through which Ruth, following Naomi back to Bethlehem, met Boaz — a wealthy kinsman of Elimelech. Boaz acted as kinsman-redeemer (<em>goel</em>), purchasing Elimelech's land and marrying Ruth to preserve the family name and inheritance, producing a son through whom the line continued to David and ultimately to Jesus Christ (Ruth 4:17–22; Matthew 1:5). Elimelech's brief appearance in the narrative thus stands at the origin of the providential chain that runs from Bethlehem to the Davidic covenant.</p>",
        "hitchcock_meaning": "my God is king",
        "source_ids": {"easton": "elimelech", "smith": "elimelech", "isbe": "elimelech"},
        "key_refs": ["Ruth 1:2", "Ruth 1:3", "Ruth 4:3", "Ruth 4:9"]
    },
    "elioenai": {
        "id": "elioenai",
        "term": "Elioenai",
        "category": "people",
        "intro": "<p>Elioenai (meaning <em>toward Jehovah are my eyes</em> or <em>to him are my fountains</em>) is the name of several individuals in the Old Testament, primarily in post-exilic genealogies and records. Among them: (1) a son of Neariah in the Davidic genealogy of the post-exilic period (1 Chronicles 3:23–24), representing a continuation of the royal line after the exile; (2) a head of a Simeonite family (1 Chronicles 4:36); (3) a son of Becher of Benjamin (1 Chronicles 7:8); (4) a Levite gatekeeper, son of Meshelemiah (1 Chronicles 26:3); (5) a priest who had married a foreign woman in the time of Ezra (Ezra 10:22); (6) a Levite who had done the same (Ezra 10:27); and (7) a priest at the dedication of Jerusalem's wall under Nehemiah (Nehemiah 12:41). The name's expression of dependence and longing toward God made it a favored name in the post-exilic community.</p>",
        "hitchcock_meaning": "toward him are mine eyes; or to him are my fountains",
        "source_ids": {"easton": "elioenai", "smith": "elioenai"},
        "key_refs": ["1 Chronicles 3:23", "Ezra 10:22", "Nehemiah 12:41"]
    },
    "eliphalet": {
        "id": "eliphalet",
        "term": "Eliphalet",
        "category": "people",
        "intro": "<p>Eliphalet (meaning <em>God his deliverance</em>) is the name of two of David's sons born in Jerusalem (2 Samuel 5:16; 1 Chronicles 14:7). The first, also called Elpelet (1 Chronicles 14:5), is numbered among the children born to David after he established his capital in Jerusalem. A second son also named Eliphalet appears in the same list — a situation some scholars attribute to the death of the first son and David naming a subsequent son the same name. An Eliphalet also appears in Ezra 8:13 as a son of Adonikam who returned with Ezra to Jerusalem from Babylon, and another in Ezra 10:33 among those who had married foreign wives.</p>",
        "hitchcock_meaning": "God of deliverance",
        "source_ids": {"easton": "eliphalet", "smith": "eliphalet"},
        "key_refs": ["2 Samuel 5:16", "1 Chronicles 14:5", "Ezra 8:13"]
    },
    "eliphaz": {
        "id": "eliphaz",
        "term": "Eliphaz",
        "category": "people",
        "intro": "<p>Eliphaz (meaning <em>God his strength</em> or <em>the endeavor of God</em>) is the name of two distinct individuals in the Old Testament. The first and more historically significant is Eliphaz the Temanite, the eldest and most eloquent of Job's three friends who came to comfort him in his suffering (Job 2:11). In three rounds of speeches (Job 4–5; 15; 22), Eliphaz argued from personal visionary experience and from the principle of divine retributive justice that Job's suffering must be the result of hidden sin. His theology, while not entirely wrong, failed to account for the particular situation of Job and was ultimately rebuked by God at the close of the book: \"My wrath is kindled against thee, and against thy two friends: for ye have not spoken of me the thing that is right, as my servant Job hath\" (Job 42:7–9).</p><p>The second Eliphaz was the eldest son of Esau by his wife Adah the daughter of Elon the Hittite (Genesis 36:4, 10–12), and the father of Teman — the ancestor of the Temanites, from whom Job's friend came. This genealogical connection may explain Eliphaz the Temanite's involvement as a wise man from Edom, a region noted in the Old Testament for its wisdom tradition (Obadiah 8; Jeremiah 49:7).</p>",
        "hitchcock_meaning": "the endeavor of God",
        "source_ids": {"easton": "eliphaz", "smith": "eliphaz"},
        "key_refs": ["Job 2:11", "Job 4:1", "Job 42:7", "Genesis 36:4"]
    },
    "elipheleh": {
        "id": "elipheleh",
        "term": "Elipheleh",
        "category": "people",
        "intro": "<p>Elipheleh was a Levite musician appointed by David to play \"on the Alamoth\" (soprano strings or flutes — an instrument of higher pitch) in the procession that brought the ark of the covenant to Jerusalem (1 Chronicles 15:18, 21). He is listed among the gatekeepers and second-tier musicians in David's elaborate musical organization for the worship of the tabernacle. The term <em>Alamoth</em> appears in the subscription of Psalm 46 and indicates a particular mode or instrument type, though its precise meaning remains debated by scholars.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "elipheleh", "smith": "elipheleh"},
        "key_refs": ["1 Chronicles 15:18", "1 Chronicles 15:21"]
    },
    "eliphelet": {
        "id": "eliphelet",
        "term": "Eliphelet",
        "category": "people",
        "intro": "<p>Eliphelet (meaning <em>God his deliverance</em>) is the name of several individuals in the Old Testament. The most notable is Eliphelet son of Ahasbai the Maachathite, one of David's thirty distinguished warriors, whose military exploits are listed in 2 Samuel 23:34. A second Eliphelet is listed in 1 Chronicles 11:35 (as Eliphal in some manuscripts). David also had a son named Eliphelet born to him in Jerusalem (2 Samuel 5:16; 1 Chronicles 3:6, 8). Ezra 8:13 mentions an Eliphelet among those who returned from Babylon with Ezra, and Ezra 10:33 lists another among those who had married foreign wives and agreed to put them away.</p><p>The name's meaning — emphasizing God as the source of deliverance — made it a recurring choice in Israelite families across different periods of biblical history. Its appearance in both Davidic genealogies and post-exilic records reflects the name's lasting appeal as a confession of trust in divine rescue.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eliphelet", "smith": "eliphelet"},
        "key_refs": ["2 Samuel 23:34", "1 Chronicles 11:35", "Ezra 8:13"]
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
    print(f'BP {__doc__.split(chr(10))[1].strip()}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
