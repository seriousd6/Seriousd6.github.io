"""
BP Article Synthesis — n2: Net → Nymphas
Covers Easton entries: Net through Nymphas (47 entries)

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

Script: scripts/bp-n2.py
Run: python3 scripts/bp-n2.py
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
    "net": {
        "id": "net",
        "term": "Net",
        "category": "concepts",
        "intro": "<p>Nets were among the primary tools of fishing in the ancient biblical world, and the Gospels make them a prominent image both practically and theologically. Several types were used: the <em>sagene</em> (drag-net or seine), which was drawn through the water by a boat or between two boats and gathered everything in its path; the casting-net (<em>amphiblestron</em>), which a fisherman threw from shore or from the shallows; and various forms of nets strung between stakes in rivers. The Mediterranean and the Sea of Galilee were primary fishing grounds, and Isaiah 19:8 mentions Egyptian fishers casting nets in the Nile.</p><p>In the New Testament, the net carries significant metaphorical weight. Jesus called Simon Peter and Andrew while they were casting their nets and summoned them to become fishers of men (Matthew 4:18–19). The parable of the dragnet (Matthew 13:47–50) likens the kingdom of heaven to a net drawn in from the sea that gathers every kind, with the separation of good and bad fish at the shore representing the final judgment. John 21 records the miraculous catch of 153 fish, a post-resurrection appearance that echoes the earlier miraculous catch in Luke 5 and becomes a commissioning scene for Peter's apostolic mission.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "net", "smith": "net", "isbe": "net"},
        "key_refs": ["Isaiah 19:8", "Matthew 4:18", "Matthew 13:47", "John 21:11"]
    },
    "nethaneel": {
        "id": "nethaneel",
        "term": "Nethaneel",
        "category": "people",
        "intro": "<p>Nethaneel (meaning <em>same as Nathanael</em>, i.e., <em>God has given</em>) is the name of several individuals in the Old Testament. The most prominent was the son of Zuar, appointed as the leader of the tribe of Issachar in Moses's census and in the order of march through the wilderness (Numbers 1:8; 2:5). He offered the second tribal sacrifice at the dedication of the altar (Numbers 7:18–23). Other bearers of the name include a son of Jesse (David's brother, 1 Chronicles 2:14), a Levitical priest who blew a trumpet before the ark (1 Chronicles 15:24), and a post-exilic priest who had married a foreign wife (Ezra 10:22).</p>",
        "hitchcock_meaning": "same as Nathanael",
        "source_ids": {"easton": "nethaneel", "smith": "nethaneel"},
        "key_refs": ["Numbers 1:8", "Numbers 2:5", "1 Chronicles 2:14", "1 Chronicles 15:24"]
    },
    "nethaniah": {
        "id": "nethaniah",
        "term": "Nethaniah",
        "category": "people",
        "intro": "<p>Nethaniah (meaning <em>the gift of the LORD</em>) is the name of several individuals in the Old Testament. The most historically significant was the father of Ishmael, the Judahite captain who assassinated Gedaliah, the governor appointed over Judah by Nebuchadnezzar after the fall of Jerusalem (Jeremiah 40:14–41:10). This act of violence destroyed the fragile Judean community that had remained in the land. Another Nethaniah was a son of Asaph, one of the Levitical musicians appointed by David for the temple worship service (1 Chronicles 25:2, 12). A third was a Levite sent by Jehoshaphat to teach the law throughout Judah's cities (2 Chronicles 17:8).</p>",
        "hitchcock_meaning": "the gift of the Lord",
        "source_ids": {"easton": "nethaniah", "smith": "nethaniah"},
        "key_refs": ["1 Chronicles 25:2", "2 Chronicles 17:8", "Jeremiah 40:14"]
    },
    "nethinim": {
        "id": "nethinim",
        "term": "Nethinim",
        "category": "people",
        "intro": "<p>The Nethinim (Hebrew <em>nethinim</em>, meaning <em>those given</em> or <em>dedicated ones</em>) were a class of temple servants in Israel, assigned to assist the Levites in the lower and more menial work of the sanctuary. Their origin is traced to the Gibeonites, whom Joshua made hewers of wood and drawers of water for the congregation and for the altar (Joshua 9:27), and to a group of 320 servants that David and the princes appointed to assist the Levites (Ezra 8:20). By the time of the return from Babylon, the Nethinim were a recognized and hereditary class of temple workers.</p><p>Ezra lists 392 Nethinim who returned from Babylon with Zerubbabel (Ezra 2:58; Nehemiah 7:60), and 220 more came with Ezra himself (Ezra 7:7; 8:17–20). They lived in a dedicated quarter of Jerusalem called Ophel, adjacent to the temple mount (Nehemiah 3:26), and Ezra 7:24 records that Artaxerxes exempted them from taxation. Their role illustrates how non-Israelite peoples could be incorporated into Israel's worship system in subordinate but recognized capacities.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nethinim", "smith": "nethinim", "isbe": "nethinim"},
        "key_refs": ["Ezra 2:70", "Ezra 7:7", "Ezra 8:20", "Joshua 9:27"]
    },
    "netophah": {
        "id": "netophah",
        "term": "Netophah",
        "category": "places",
        "intro": "<p>Netophah was a town in Judah, in the hill country near Bethlehem, from which a number of David's mighty warriors came — including Maharai and Heleb the Netophathites (2 Samuel 23:28–29; 1 Chronicles 27:13, 15). Fifty-six men of Netophah returned from the Babylonian exile with Zerubbabel (Ezra 2:22; Nehemiah 7:26). After the exile, Netophathite Levites settled there, maintaining the tradition of musical worship established by David (Nehemiah 12:28). The site is identified with Khirbet Beit Faluh, approximately three miles southeast of Bethlehem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "netophah", "smith": "netophah"},
        "key_refs": ["Nehemiah 7:26", "1 Chronicles 2:54", "1 Chronicles 27:13"]
    },
    "nettle": {
        "id": "nettle",
        "term": "Nettle",
        "category": "concepts",
        "intro": "<p>Nettle (Hebrew <em>charul</em>, possibly also <em>qimmosh</em>) appears in Scripture as a symbol of desolation and neglect. Proverbs 24:30–31 describes the field and vineyard of the sluggard overrun with nettles and thorns — a picture of the consequences of laziness. Job 30:7 refers to desperate outcasts who sought shelter among the bushes and gathered under the nettles. Zephaniah 2:9 pronounces judgment on Moab and Ammon, declaring their lands shall be \"a possession of nettles, and saltpits, and a perpetual desolation\" — a reversal of the fertile land into barren waste. The nettle thus functions as a recurring image of curse, abandonment, and the fruits of neglected responsibility.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nettle", "smith": "nettle"},
        "key_refs": ["Proverbs 24:30", "Job 30:7", "Zephaniah 2:9"]
    },
    "new-moon-feast-of": {
        "id": "new-moon-feast-of",
        "term": "New Moon, Feast of",
        "category": "concepts",
        "intro": "<p>The Feast of the New Moon was a monthly observance in Israel, celebrated at the beginning of each lunar month when the new crescent appeared. The Law required special sacrifices on these days: burnt offerings, sin offerings, and peace offerings beyond the regular daily sacrifice (Numbers 28:11–15), accompanied by trumpet blasts (Numbers 10:10; Psalm 81:3). The new moon day was a time of rest from ordinary commerce (Amos 8:5) and religious assembly, and families and communities gathered to celebrate and offer sacrifice (1 Samuel 20:5–6).</p><p>The New Moon held special prominence in Israel's liturgical calendar, marking the orderly rhythm of God's created time. The seventh month's new moon (later known as Rosh Hashanah) was a particularly solemn assembly (Leviticus 23:23–25). The prophets criticized the formalism with which the people observed these festivals without corresponding justice and obedience (Isaiah 1:13–14; Amos 8:5). Colossians 2:16 groups new moon observances with Sabbaths and festivals as shadows pointing to Christ, the substance to whom all these ceremonies pointed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "new-moon-feast-of", "smith": "new-moon-feast-of", "isbe": "new-moon-feast-of"},
        "key_refs": ["Numbers 28:11", "Numbers 10:10", "Amos 8:5", "Colossians 2:16"]
    },
    "new-testament": {
        "id": "new-testament",
        "term": "New Testament",
        "category": "concepts",
        "intro": "<p>The New Testament (Greek <em>kaine diatheke</em>, meaning <em>new covenant</em> or <em>new testament</em>) is the collection of twenty-seven books that together constitute the second portion of the Christian Bible, all composed in Greek in the first century A.D. The term derives from Jesus's words at the Last Supper — \"This cup is the new covenant in my blood\" (Luke 22:20; 1 Corinthians 11:25) — which deliberately echoes Jeremiah 31:31's prophecy of a new covenant that would supersede the Mosaic. The New Testament documents are organized into Gospels (Matthew, Mark, Luke, John), Acts, Epistles (Pauline and General), and Revelation.</p><p>The New Testament's central subject is Jesus Christ — his life, death, resurrection, and exaltation — and the community that gathered around his name. The Gospels narrate his ministry; Acts records the Spirit-empowered expansion of his church; the Epistles address specific communities and theological questions arising from his work; and Revelation unveils the consummation of his kingdom. The New Testament authors read the Hebrew Scriptures through the lens of Christ's fulfillment: what the Law and Prophets anticipated, the New Testament proclaims as accomplished and being realized.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "new-testament", "isbe": "new-testament"},
        "key_refs": ["Luke 22:20", "Hebrews 8:8", "Jeremiah 31:31"]
    },
    "neziah": {
        "id": "neziah",
        "term": "Neziah",
        "category": "people",
        "intro": "<p>Neziah (meaning <em>conqueror</em> or <em>strong</em>) was the ancestor of a family of Nethinim — temple servants — who returned from the Babylonian exile with Zerubbabel (Ezra 2:54; Nehemiah 7:56). The name appears only in these two parallel lists of returning exiles. As a Nethinim family head, Neziah's descendants would have served in the menial but essential tasks of the restored temple in Jerusalem.</p>",
        "hitchcock_meaning": "conqueror; strong",
        "source_ids": {"easton": "neziah", "smith": "neziah"},
        "key_refs": ["Ezra 2:54"]
    },
    "nezib": {
        "id": "nezib",
        "term": "Nezib",
        "category": "places",
        "intro": "<p>Nezib (meaning <em>a standing-place</em> or <em>garrison</em>) was a town in the Shephelah of Judah, listed among the cities of the lowland assigned to Judah (Joshua 15:43). It is identified with Khirbet Beit Nisib, approximately ten miles northwest of Hebron. Beyond its listing in Joshua, no narrative events are connected with it in Scripture.</p>",
        "hitchcock_meaning": "standing-place",
        "source_ids": {"easton": "nezib", "smith": "nezib"},
        "key_refs": ["Joshua 15:43"]
    },
    "nibhaz": {
        "id": "nibhaz",
        "term": "Nibhaz",
        "category": "concepts",
        "intro": "<p>Nibhaz (meaning <em>budding</em> or <em>prophesying</em>) was an idol worshipped by the Avites, one of the peoples transplanted by the Assyrians into Samaria after the deportation of the northern tribes of Israel (2 Kings 17:31). The settlers brought their own gods with them and worshipped them in their new land alongside some fear of the God of Israel, creating the syncretistic religion that characterized the Samaritans. The exact nature of Nibhaz and its cult is unknown; the name may be a Hebrew distortion of a foreign deity's name.</p>",
        "hitchcock_meaning": "budding; prophesying",
        "source_ids": {"easton": "nibhaz", "smith": "nibhaz"},
        "key_refs": ["2 Kings 17:31"]
    },
    "nibshan": {
        "id": "nibshan",
        "term": "Nibshan",
        "category": "places",
        "intro": "<p>Nibshan (meaning <em>prophecy</em> or <em>growing of a tooth</em>) was a town in the wilderness of Judah, listed in Joshua 15:62 among the cities in the desert district near the Dead Sea. It lay in the desolate region between the hill country of Judah and the western shore of the Dead Sea. Its precise identification is uncertain, though it may be in the area of Khirbet el-Maqari. No narrative events are associated with it in Scripture.</p>",
        "hitchcock_meaning": "prophecy; growing of a tooth",
        "source_ids": {"easton": "nibshan", "smith": "nibshan"},
        "key_refs": ["Joshua 15:62"]
    },
    "nicanor": {
        "id": "nicanor",
        "term": "Nicanor",
        "category": "people",
        "intro": "<p>Nicanor (meaning <em>a conqueror</em> or <em>victorious</em>) was one of the seven men chosen by the Jerusalem church to oversee the fair distribution of food to Hellenistic Jewish widows who had been neglected in the daily ministration (Acts 6:1–5). He was among those described as men of honest report, full of the Holy Spirit and wisdom. Nicanor is otherwise unknown in the New Testament; tradition has sometimes connected him with later martyrdom, though this is not confirmed in Scripture.</p>",
        "hitchcock_meaning": "a conqueror; victorious",
        "source_ids": {"easton": "nicanor", "smith": "nicanor"},
        "key_refs": ["Acts 6:5"]
    },
    "nicodemus": {
        "id": "nicodemus",
        "term": "Nicodemus",
        "category": "people",
        "intro": "<p>Nicodemus (meaning <em>victory of the people</em>) was a Pharisee and ruler of the Jews — a member of the Sanhedrin — who came to Jesus by night, apparently seeking to avoid being seen (John 3:1–2). Jesus's conversation with him produced some of Scripture's most profound teaching on the new birth: \"Except a man be born again, he cannot see the kingdom of God\" (John 3:3), and the declaration of John 3:16 — \"For God so loved the world, that he gave his only begotten Son.\" Nicodemus's nighttime visit suggests fear of his colleagues, but his subsequent appearances suggest growing courage.</p><p>He defended Jesus before the Sanhedrin when they sought to condemn him without due process (John 7:50–52), and after the crucifixion he joined Joseph of Arimathea in providing a costly burial — bringing a hundred pounds of myrrh and aloes for the body of Jesus (John 19:39–40). This final act in the open, at personal and financial risk, suggests that the man who came by night had moved toward a more public faith.</p>",
        "hitchcock_meaning": "victory of the people",
        "source_ids": {"easton": "nicodemus", "smith": "nicodemus", "isbe": "nicodemus"},
        "key_refs": ["John 3:1", "John 7:50", "John 19:39"]
    },
    "nicolaitanes": {
        "id": "nicolaitanes",
        "term": "Nicolaitanes",
        "category": "concepts",
        "intro": "<p>The Nicolaitanes (or Nicolaitans) were a sect condemned twice in the letters to the seven churches in Revelation: Jesus declares that the church at Ephesus hates their deeds as he also hates them (Revelation 2:6), and the church at Pergamos is rebuked for having some who hold their doctrine (Revelation 2:15). Their teaching is associated with the doctrine of Balaam — eating food sacrificed to idols and committing sexual immorality — suggesting an antinomian movement that used Christian liberty as license for participation in pagan religious and social practices.</p><p>Ancient sources (Irenaeus, Clement of Alexandria) trace the Nicolaitans to Nicolas of Antioch, one of the seven deacons of Acts 6:5, though this identification is contested by other early writers. Whether or not the connection to Nicolas is historical, the Nicolaitan pattern — compromising with the surrounding culture's religious and sexual norms under theological cover — is presented in Revelation as a serious threat to the integrity of the churches that must not be tolerated.</p>",
        "hitchcock_meaning": "followers of Nicolas",
        "source_ids": {"easton": "nicolaitanes", "smith": "nicolaitanes", "isbe": "nicolaitanes"},
        "key_refs": ["Revelation 2:6", "Revelation 2:15"]
    },
    "nicolas": {
        "id": "nicolas",
        "term": "Nicolas",
        "category": "people",
        "intro": "<p>Nicolas (meaning <em>same as Nicodemus</em>, i.e., <em>victory of the people</em>) was a proselyte from Antioch — a Gentile who had converted to Judaism before becoming a Christian — and one of the seven men chosen by the Jerusalem church to assist the apostles in the fair distribution of food to widows (Acts 6:5). As a proselyte of Antioch, he was among the most diaspora-connected of the seven. Ancient tradition (Irenaeus, Epiphanius) later associated him with the founding of the Nicolaitan sect condemned in Revelation 2, though Clement of Alexandria disputed this, arguing that Nicolas himself was orthodox and that followers misused his teaching.</p>",
        "hitchcock_meaning": "same as Nicodemus",
        "source_ids": {"easton": "nicolas", "smith": "nicolas"},
        "key_refs": ["Acts 6:5"]
    },
    "nicopolis": {
        "id": "nicopolis",
        "term": "Nicopolis",
        "category": "places",
        "intro": "<p>Nicopolis (meaning <em>the city of victory</em>) was a city where Paul planned to spend the winter and to which he asked Titus to come (Titus 3:12). Several cities bore this name in the ancient world; the most likely candidate is Nicopolis in Epirus, on the western coast of Greece (modern Albania), founded by Augustus to commemorate his victory at the Battle of Actium in 31 B.C. It was a prominent city and a natural wintering location on the route between Rome and the eastern provinces. Paul's plan to winter there suggests an active western mission strategy in the period of the Pastoral Epistles.</p>",
        "hitchcock_meaning": "the city of victory",
        "source_ids": {"easton": "nicopolis", "smith": "nicopolis"},
        "key_refs": ["Titus 3:12"]
    },
    "niger": {
        "id": "niger",
        "term": "Niger",
        "category": "people",
        "intro": "<p>Niger (Latin meaning <em>black</em>) was the surname of Simeon, one of the prophets and teachers at the church in Antioch of Syria (Acts 13:1). The Latin name Niger suggests he may have been of African origin or dark complexion, possibly connecting him with the North African church. He was among the church leaders who were praying and fasting when the Holy Spirit called Barnabas and Saul (Paul) to their first missionary journey (Acts 13:2–3). Beyond this single reference, nothing else is known of Simeon Niger.</p>",
        "hitchcock_meaning": "black",
        "source_ids": {"easton": "niger", "smith": "niger"},
        "key_refs": ["Acts 13:1"]
    },
    "night-hawk": {
        "id": "night-hawk",
        "term": "Night-hawk",
        "category": "concepts",
        "intro": "<p>The night-hawk (Hebrew <em>tachmac</em>) appears in the lists of unclean birds in Leviticus 11:16 and Deuteronomy 14:15 — birds forbidden as food to Israelites. The precise identification of the Hebrew term is uncertain and has been rendered variously as night-hawk, owl, or short-eared owl by different translators. Whatever the exact species, the bird belongs to the category of nocturnal raptors or insect-hunters whose habits and diet made them ritually unclean according to the Mosaic Law. The clean/unclean animal distinction in Leviticus served both to set Israel apart from surrounding peoples and to instill habits of discrimination and holiness in everyday life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "night-hawk", "smith": "night-hawk"},
        "key_refs": ["Leviticus 11:16", "Deuteronomy 14:15"]
    },
    "nile": {
        "id": "nile",
        "term": "Nile",
        "category": "places",
        "intro": "<p>The Nile (Hebrew <em>Ye'or</em>, meaning <em>the river</em>, or <em>Shihor</em>, meaning <em>the dark</em>) was the lifeblood of Egypt and the central feature of its geography, religion, and economy. Though not called \"Nile\" in most English Old Testament translations, it is consistently referred to as \"the river\" or \"the river of Egypt.\" The annual flooding of the Nile deposited rich silt along its banks, making the Nile valley extraordinarily fertile in contrast to the surrounding desert — the foundation of Egypt's agricultural abundance. Pharaoh's dream of seven fat and seven lean cattle coming out of the Nile (Genesis 41:1–4) reflects this agricultural dependence.</p><p>The Nile is the setting of the first three plagues of the Exodus: its water was turned to blood, its frogs overran the land, and its lice afflicted man and beast (Exodus 7–8). Moses was hidden in the Nile's reeds as an infant and drawn out by Pharaoh's daughter (Exodus 2:3). The prophets use Nile imagery for Egypt's pride and power: Isaiah 23:3 calls Egypt's harvest \"the seed of Sihor\" and Jeremiah 2:18 rebukes Israel for seeking the waters of the Nile. Amos 8:8 uses the Nile's flooding as a metaphor for coming judgment on Israel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nile", "smith": "nile", "isbe": "nile"},
        "key_refs": ["Genesis 41:1", "Exodus 1:22", "Amos 8:8", "Isaiah 23:3"]
    },
    "nimrah": {
        "id": "nimrah",
        "term": "Nimrah",
        "category": "places",
        "intro": "<p>Nimrah (meaning <em>leopard</em> or <em>limpid water</em>) was a town east of the Jordan in the territory of Gad, also called Beth-nimrah (Numbers 32:36; Joshua 13:27). It was originally requested by the Gadites from Moses as part of their inheritance in Transjordan when they saw the land was suitable for their cattle (Numbers 32:3). The town lay in the Jordan valley north of the Dead Sea, in the fertile lowlands watered by streams descending from the mountains of Moab. Its full form, Beth-nimrah (\"house of the leopard\" or \"clear water\"), suggests either wildlife in the area or a spring of clear water.</p>",
        "hitchcock_meaning": "leopard; bitterness; rebellion",
        "source_ids": {"easton": "nimrah", "smith": "nimrah"},
        "key_refs": ["Numbers 32:3", "Joshua 13:27"]
    },
    "nimrim-waters-of": {
        "id": "nimrim-waters-of",
        "term": "Nimrim, Waters of",
        "category": "places",
        "intro": "<p>The Waters of Nimrim appear in prophetic oracles of judgment against Moab in Isaiah 15:6 and Jeremiah 48:34, where they are described as desolate — \"the waters of Nimrim shall be desolate\" — as part of the devastation coming upon the Moabite land. The location is likely in southern Moab, possibly identified with Wadi en-Numeirah, a seasonal stream flowing into the southeastern end of the Dead Sea. The drying up of these waters represents the comprehensive destruction of Moab's agricultural resources and the reversal of its fertile watered lands.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nimrim-waters-of", "smith": "nimrim-waters-of"},
        "key_refs": ["Isaiah 15:6", "Jeremiah 48:34"]
    },
    "nimrod": {
        "id": "nimrod",
        "term": "Nimrod",
        "category": "people",
        "intro": "<p>Nimrod (meaning <em>rebellion</em>, though possibly from an unknown Assyrian or Akkadian root) was the son of Cush and great-grandson of Noah through the Hamitic line, described as \"a mighty one in the earth\" and \"a mighty hunter before the LORD\" — a proverbial expression of great prowess (Genesis 10:8–9). He was the founder of the first great empire after the Flood: his kingdom began at Babel (Babylon), Erech (Uruk), Accad, and Calneh in the land of Shinar, and extended northward to Assyria, where he built Nineveh, Rehoboth-Ir, Calah, and Resen (Genesis 10:10–12).</p><p>Nimrod's connection to both Babylon and Assyria — the two great world empires that oppressed Israel — made his name a symbol of imperial power opposed to God. Micah 5:6 calls Assyria \"the land of Nimrod,\" using him as the archetype of Assyrian dominance. Jewish tradition often interpreted Nimrod as the architect of the Tower of Babel and as a tyrant who defied God, though Genesis itself does not explicitly make this connection.</p>",
        "hitchcock_meaning": "rebellion",
        "source_ids": {"easton": "nimrod", "smith": "nimrod", "isbe": "nimrod"},
        "key_refs": ["Genesis 10:8", "Genesis 10:10", "Micah 5:6"]
    },
    "nimshi": {
        "id": "nimshi",
        "term": "Nimshi",
        "category": "people",
        "intro": "<p>Nimshi (meaning <em>rescued from danger</em>) was the grandfather (or possibly father) of Jehu, the commander who became king of Israel after being anointed by Elisha's messenger (2 Kings 9:2; 1 Kings 19:16). Jehu is consistently called \"the son of Nimshi\" in the biblical text, though 2 Kings 9:2 identifies his father as Jehoshaphat the son of Nimshi, making Nimshi the grandfather. The phrase \"son of Nimshi\" became proverbial for Jehu's notoriously reckless and furious driving (2 Kings 9:20): \"the driving is like the driving of Jehu the son of Nimshi; for he driveth furiously.\"</p>",
        "hitchcock_meaning": "rescued from danger",
        "source_ids": {"easton": "nimshi", "smith": "nimshi"},
        "key_refs": ["2 Kings 9:2", "1 Kings 19:16"]
    },
    "nineveh": {
        "id": "nineveh",
        "term": "Nineveh",
        "category": "places",
        "intro": "<p>Nineveh was the great capital of the Assyrian Empire, situated on the eastern bank of the Tigris River opposite modern Mosul in northern Iraq. Founded by Nimrod (Genesis 10:11), it became one of the largest and most formidable cities of the ancient world. At its height under Sennacherib (705–681 B.C.), the city was enclosed by massive walls and contained great palaces and temples. The biblical description of Nineveh as \"an exceeding great city of three days' journey\" (Jonah 3:3) reflects either its immense size, its administrative district, or its reputation.</p><p>Nineveh appears most prominently in the Book of Jonah, where God sent the reluctant prophet to preach repentance to it. The city's unexpected repentance — from its king to its cattle — stands as a remarkable instance of Gentile response to the word of God and Jesus cited it as a warning to his own unrepentant generation (Matthew 12:41; Luke 11:32). Nahum's entire prophecy is an oracle against Nineveh, announcing its destruction; the city fell to the Babylonian-Median coalition in 612 B.C., fulfilling the prophet's word. Archaeology has confirmed the site at Kuyunjik and Nebi Yunus, where extensive Assyrian palace remains have been excavated.</p>",
        "hitchcock_meaning": "handsome; agreeable",
        "source_ids": {"easton": "nineveh", "smith": "nineveh", "isbe": "nineveh"},
        "key_refs": ["Genesis 10:11", "Jonah 3:3", "Matthew 12:41", "Nahum 1:1"]
    },
    "nisan": {
        "id": "nisan",
        "term": "Nisan",
        "category": "concepts",
        "intro": "<p>Nisan (meaning <em>standard</em> or <em>miracle</em>) is the first month of the Hebrew sacred calendar, corresponding to March–April, adopted from the Babylonian month name Nisanu during or after the exile. Before the exile it was known as Abib (<em>green ears</em>). The Passover was celebrated on the fourteenth of Nisan (Exodus 12:2–6), and the Feast of Unleavened Bread began on the fifteenth, making it the most liturgically significant month in Israel's year. Nehemiah 2:1 places Nehemiah's conversation with Artaxerxes in the month Nisan, and Esther 3:7 records Haman casting lots in Nisan to determine the date for the destruction of the Jews.</p>",
        "hitchcock_meaning": "standard; miracle",
        "source_ids": {"easton": "nisan", "smith": "nisan"},
        "key_refs": ["Nehemiah 2:1", "Esther 3:7"]
    },
    "nisroch": {
        "id": "nisroch",
        "term": "Nisroch",
        "category": "concepts",
        "intro": "<p>Nisroch (meaning <em>flight</em>, <em>proof</em>, or <em>temptation</em>) was an Assyrian deity in whose temple Sennacherib was worshipping when his sons Adrammelech and Sharezer murdered him (2 Kings 19:37; Isaiah 37:38). This ironic scene — the Assyrian king who had blasphemed the God of Israel being slain in the house of his own god — is presented as a vindication of Hezekiah's prayer and a demonstration of the LORD's sovereignty over the gods of the nations. Nisroch's identity is uncertain; he does not correspond clearly to any known major Assyrian deity, and the name may be a Hebrew distortion or a minor divine name.</p>",
        "hitchcock_meaning": "flight; proof; temptation; delicate",
        "source_ids": {"easton": "nisroch", "smith": "nisroch"},
        "key_refs": ["2 Kings 19:37", "Isaiah 37:38"]
    },
    "nitre": {
        "id": "nitre",
        "term": "Nitre",
        "category": "concepts",
        "intro": "<p>Nitre (Hebrew <em>nether</em>) in the biblical context refers not to saltpeter (potassium nitrate) but to natron — sodium carbonate — a naturally occurring alkali salt mined from dried lake beds in Egypt and used in ancient times for washing, cleaning, and embalming. Proverbs 25:20 compares one who sings songs to a heavy heart to vinegar poured on nitre, where the fizzing and dissolution of the natron illustrates how cheer poured on sorrow produces the opposite of comfort. Jeremiah 2:22 uses nitre along with soap (<em>borith</em>) to declare that even the strongest cleansing agents cannot remove Israel's stain of iniquity before God — only genuine repentance and divine forgiveness can accomplish that.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nitre", "smith": "nitre"},
        "key_refs": ["Proverbs 25:20", "Jeremiah 2:22"]
    },
    "no": {
        "id": "no",
        "term": "No",
        "category": "places",
        "intro": "<p>No (also called No-Amon or No-Ammon, meaning <em>the city of Amon</em>) was the great Egyptian city of Thebes, located about 400 miles south of Cairo on both banks of the Nile in Upper Egypt. It was one of Egypt's most magnificent capitals and the center of the worship of Amon-Ra, the supreme god of the Egyptian pantheon. Nahum 3:8 invokes the fall of No-Amon as a historical warning to Nineveh: \"Art thou better than populous No?\" — pointing to the Assyrian conquest of Thebes in 663 B.C. by Ashurbanipal as a precedent for Nineveh's own impending doom. Jeremiah and Ezekiel both include No among the Egyptian cities that will face God's judgment (Jeremiah 46:25; Ezekiel 30:14–16).</p>",
        "hitchcock_meaning": "stirring up; forbidding",
        "source_ids": {"easton": "no", "smith": "no", "isbe": "no"},
        "key_refs": ["Jeremiah 46:25", "Ezekiel 30:14", "Nahum 3:8"]
    },
    "noadiah": {
        "id": "noadiah",
        "term": "Noadiah",
        "category": "people",
        "intro": "<p>Noadiah (meaning <em>witness of the LORD</em> or <em>ornament of the LORD</em>) is the name of two individuals in Ezra and Nehemiah. The first was a Levite, son of Binnui, who assisted in the weighing of the temple silver and gold brought back by Ezra from Babylon (Ezra 8:33). The second — and more significant — was a prophetess who joined Sanballat, Tobiah, and Geshem in opposing Nehemiah's reconstruction of Jerusalem's walls. Nehemiah's prayer names her specifically: \"My God, think thou upon Tobiah and Sanballat... and on the prophetess Noadiah, and the rest of the prophets, that would have put me in fear\" (Nehemiah 6:14). She is one of only a few women explicitly identified as prophets in the Old Testament.</p>",
        "hitchcock_meaning": "witness, or ornament, of the Lord",
        "source_ids": {"easton": "noadiah", "smith": "noadiah"},
        "key_refs": ["Ezra 8:33", "Nehemiah 6:14"]
    },
    "noah": {
        "id": "noah",
        "term": "Noah",
        "category": "people",
        "intro": "<p>Noah (meaning <em>repose</em> or <em>consolation</em>) was the son of Lamech and tenth patriarch from Adam, born 1,056 years after creation according to the biblical chronology (Genesis 5:29). In an era of universal human corruption and violence, Noah \"found grace in the eyes of the LORD\" (Genesis 6:8) — the first occurrence of grace language in the Bible. God commissioned him to build the ark, through which he preserved his family and representatives of every animal kind through the Flood that destroyed the corrupt world. After the waters receded, God established his covenant with Noah and all living creatures, with the rainbow as its sign (Genesis 9:8–17).</p><p>Noah's theological significance extends through both Testaments. Ezekiel 14:14, 20 names him alongside Daniel and Job as exemplary righteous men. Hebrews 11:7 credits his faith: \"By faith Noah, being warned of God of things not seen as yet, moved with fear, prepared an ark to the saving of his house; by the which he condemned the world, and became heir of the righteousness which is by faith.\" Jesus uses Noah's generation as a type of the conditions preceding the Son of Man's coming (Matthew 24:37–39; Luke 17:26–27), and Peter twice uses the Flood as a type of baptism and divine judgment (1 Peter 3:20–21; 2 Peter 2:5).</p>",
        "hitchcock_meaning": "repose; consolation",
        "source_ids": {"easton": "noah", "smith": "noah", "isbe": "noah"},
        "key_refs": ["Genesis 6:8", "Genesis 9:13", "Hebrews 11:7", "Matthew 24:37"]
    },
    "nob": {
        "id": "nob",
        "term": "Nob",
        "category": "places",
        "intro": "<p>Nob was a priestly city in the territory of Benjamin, located near Jerusalem and visible from the northern approach to the city (Isaiah 10:28–32, where it figures in Sennacherib's march). It served as the location of the tabernacle and its sacred bread after the destruction of Shiloh, and the priests of Nob ministered there. David came to Nob when fleeing Saul, deceived Ahimelech the high priest into giving him the showbread and Goliath's sword (1 Samuel 21:1–9). Doeg the Edomite witnessed this encounter and reported it to Saul, who commanded Doeg to execute the priests of Nob — resulting in the massacre of eighty-five priests and the entire city's population, with only Abiathar escaping to join David (1 Samuel 22:9–23).</p>",
        "hitchcock_meaning": "discourse; prophecy",
        "source_ids": {"easton": "nob", "smith": "nob", "isbe": "nob"},
        "key_refs": ["1 Samuel 21:1", "1 Samuel 22:18", "Isaiah 10:32"]
    },
    "nobah": {
        "id": "nobah",
        "term": "Nobah",
        "category": "people",
        "intro": "<p>Nobah (meaning <em>that barks or yelps</em>) was a Manassite warrior who captured the city of Kenath in Bashan and its surrounding villages, renaming it Nobah after himself (Numbers 32:42) — one of the few instances in the Old Testament of a place being renamed after a living person. The town reverted to the name Kenath in later usage. A place called Nobah near Jogbehah east of the Jordan is also mentioned in Gideon's pursuit of the Midianite kings (Judges 8:11), which may refer to this same renamed city.</p>",
        "hitchcock_meaning": "that barks or yelps",
        "source_ids": {"easton": "nobah", "smith": "nobah"},
        "key_refs": ["Numbers 32:42", "Judges 8:11"]
    },
    "nobleman": {
        "id": "nobleman",
        "term": "Nobleman",
        "category": "concepts",
        "intro": "<p>The term nobleman (Greek <em>basilikos</em>, meaning <em>royal</em> or <em>belonging to the king</em>) appears in the Gospel of John's account of a royal official whose son lay dying at Capernaum. He traveled to Cana where Jesus was and implored him to heal his son. Jesus challenged his demand for signs, then declared \"Go thy way; thy son liveth.\" The man believed the word of Jesus and departed; on his way home his servants met him with news of his son's recovery, which confirmed it happened at the exact moment Jesus had spoken (John 4:46–54). This healing — the second sign Jesus performed in Galilee — demonstrates that Christ's authority operates across distance and that faith grounded in his word, rather than in visible miracles, is the pathway to salvation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nobleman", "smith": "nobleman"},
        "key_refs": ["John 4:46", "John 4:50"]
    },
    "nod": {
        "id": "nod",
        "term": "Nod",
        "category": "places",
        "intro": "<p>Nod (meaning <em>vagabond</em> or <em>fugitive</em>) was the land to which Cain went after God pronounced his judgment — \"a fugitive and a vagabond shalt thou be in the earth\" (Genesis 4:12). The text says Cain \"dwelt in the land of Nod, on the east of Eden\" (Genesis 4:16) and there built a city. The name Nod appears to be derived from the root of the curse itself, embedding the judgment into the geography: the land of wandering. Its precise location is unknown and likely symbolic — the land of Nod is the place defined by exile and restlessness, the existence of one cut off from the presence of God.</p>",
        "hitchcock_meaning": "vagabond; fugitive",
        "source_ids": {"easton": "nod", "smith": "nod"},
        "key_refs": ["Genesis 4:16"]
    },
    "nodab": {
        "id": "nodab",
        "term": "Nodab",
        "category": "people",
        "intro": "<p>Nodab (meaning <em>vowing of his own accord</em> or <em>noble</em>) was an Arab tribe that together with the Hagarites, Jetur, Nephish, and other eastern peoples was defeated by the Transjordanian tribes of Reuben, Gad, and the half-tribe of Manasseh in a battle enabled by their trust in God (1 Chronicles 5:19). The Nodabites may be connected with the Nubians or an Arabian group in the region east of Gilead. No further details of this tribe are recorded in Scripture.</p>",
        "hitchcock_meaning": "vowing of his own accord",
        "source_ids": {"easton": "nodab", "smith": "nodab"},
        "key_refs": ["1 Chronicles 5:19"]
    },
    "nogah": {
        "id": "nogah",
        "term": "Nogah",
        "category": "people",
        "intro": "<p>Nogah (meaning <em>brightness</em> or <em>clearness</em>) was one of the sons born to David in Jerusalem, listed among his children by his wives and concubines (1 Chronicles 3:7; 14:6). He is named between Nepheg and Japhia. Nogah does not appear elsewhere in the biblical narrative, and nothing further is known of him beyond the genealogical references. His name was part of the growing royal household David established at Jerusalem after he became king over all Israel.</p>",
        "hitchcock_meaning": "brightness; clearness",
        "source_ids": {"easton": "nogah", "smith": "nogah"},
        "key_refs": ["1 Chronicles 3:7"]
    },
    "noph": {
        "id": "noph",
        "term": "Noph",
        "category": "places",
        "intro": "<p>Noph (also Moph; identified with Memphis) was the Hebrew name for the ancient Egyptian capital of Memphis, located on the western bank of the Nile near the apex of the Delta. It appears in several prophetic oracles: Isaiah 19:13 mentions the princes of Noph among those who led Egypt astray; Jeremiah 2:16 rebukes Israel for seeking alliance with Egypt, connecting Noph and Tahapanes; and Ezekiel 30:13, 16 pronounces judgment on Noph and its idols. Hosea 9:6 predicts that Noph shall bury those who flee Assyrian judgment. The consistent appearance of Noph in prophecies against Egypt reflects its status as a major center of Egyptian power and paganism. See also <strong>Memphis</strong>.</p>",
        "hitchcock_meaning": "honeycomb; anything that distills or drops",
        "source_ids": {"easton": "noph", "smith": "noph"},
        "key_refs": ["Isaiah 19:13", "Ezekiel 30:13", "Hosea 9:6"]
    },
    "nophah": {
        "id": "nophah",
        "term": "Nophah",
        "category": "places",
        "intro": "<p>Nophah (meaning <em>fearful</em> or <em>binding</em>) appears in a fragment of an ancient victory poem cited in Numbers 21:30 among the Moabite cities devastated by Sihon the Amorite: \"We have shot at them; Heshbon is perished even unto Dibon, and we have laid them waste even unto Nophah, which reacheth unto Medeba.\" The poem is quoted to establish that Israel's capture of this territory from Sihon was legitimate — they were not taking Moabite land but land that Sihon himself had taken from Moab. Nophah's precise location is unknown.</p>",
        "hitchcock_meaning": "fearful; binding",
        "source_ids": {"easton": "nophah", "smith": "nophah"},
        "key_refs": ["Numbers 21:30"]
    },
    "north-country": {
        "id": "north-country",
        "term": "North country",
        "category": "places",
        "intro": "<p>The \"North country\" in prophetic literature primarily refers to Babylon and the region of Mesopotamia, approached from Israel's perspective by the northern land route rather than across the Arabian desert to the east. Jeremiah repeatedly uses the phrase to refer to Babylonia as the direction from which judgment would come (Jeremiah 1:14–15; 6:22; 10:22), and he announces that the exiles would return from the north country (Jeremiah 3:18; 16:15; 23:8). Zechariah's visions use north country to refer to the Babylonian diaspora that God would summon home (Zechariah 6:6–8). The phrase also appears in Isaiah 41:25, where God calls a conqueror (Cyrus) from the north as his instrument of deliverance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "north-country"},
        "key_refs": ["Jeremiah 1:14", "Jeremiah 3:18", "Isaiah 41:25"]
    },
    "northward": {
        "id": "northward",
        "term": "Northward",
        "category": "concepts",
        "intro": "<p>Northward as a directional designation appears frequently in the geographical descriptions of the land and tabernacle in the Old Testament. Moses viewed the Promised Land from four directions — northward, southward, eastward, and westward — from Mount Pisgah (Deuteronomy 3:27). The tabernacle was oriented so that the altar of burnt offering and various furnishings had specific northward arrangements (Leviticus 1:11), as animals for burnt offerings were to be slain on the north side of the altar before the LORD. In prophetic literature, north carries consistent associations with the direction of threat and divine judgment descending upon Israel — Ezekiel's vision of the divine chariot came from the north (Ezekiel 1:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "northward"},
        "key_refs": ["Deuteronomy 3:27", "Leviticus 1:11"]
    },
    "nose-jewels": {
        "id": "nose-jewels",
        "term": "Nose-jewels",
        "category": "concepts",
        "intro": "<p>Nose-jewels (Hebrew <em>nezem</em>) were ornamental rings worn in the nose or as pendants, a common form of personal adornment for women in the ancient Near East from earliest times. Abraham's servant gave Rebekah a nose-ring of gold as a bridal gift (Genesis 24:47). Proverbs 11:22 uses a gold ring in a pig's snout as a vivid image of beauty without discretion. Isaiah 3:21 lists nose-rings among the many adornments of Jerusalem's daughters that God would take away as judgment. Hosea 2:13 depicts Israel adorning herself with nose-jewels and earrings to pursue her lovers (the Baals) rather than remembering the LORD. The nose-ring thus appears both as a legitimate cultural ornament and as a symbol of misplaced devotion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nose-jewels", "smith": "nose-jewels"},
        "key_refs": ["Genesis 24:47", "Proverbs 11:22", "Isaiah 3:21", "Hosea 2:13"]
    },
    "numbering-of-the-people": {
        "id": "numbering-of-the-people",
        "term": "Numbering of the people",
        "category": "events",
        "intro": "<p>The Numbering of the People (also known as David's census) was the military census that King David commanded Joab to carry out throughout Israel and Judah, against Joab's protests (2 Samuel 24; 1 Chronicles 21). The account attributes the instigation either to the LORD's anger against Israel (2 Samuel 24:1) or to Satan (1 Chronicles 21:1) — reflecting the biblical understanding that God can use even human sin and spiritual opposition to accomplish his purposes of discipline. David himself later recognized the act as sinful, saying \"I have sinned greatly in that I have done\" (2 Samuel 24:10; 1 Chronicles 21:8).</p><p>The census yielded figures of 800,000 (or 1,100,000 in Chronicles) warriors in Israel and 500,000 in Judah. As punishment, God offered David three choices: seven years of famine, three months of military defeat, or three days of pestilence. David chose to fall into the hand of God rather than men, and the pestilence killed 70,000 in Israel. It ended at the threshing floor of Araunah the Jebusite in Jerusalem, which David purchased and on which Solomon later built the temple (2 Samuel 24:18–25; 1 Chronicles 21:22–30).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "numbering-of-the-people", "smith": "numbering-of-the-people"},
        "key_refs": ["2 Samuel 24:1", "1 Chronicles 21:1", "2 Samuel 24:13", "1 Chronicles 21:22"]
    },
    "numbers-book-of": {
        "id": "numbers-book-of",
        "term": "Numbers, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Numbers (Hebrew <em>Bemidbar</em>, <em>in the wilderness</em>; called Numbers in Greek and English translations for the two census lists it contains) is the fourth book of the Pentateuch, covering the thirty-eight years of Israel's wilderness wandering between Sinai and the plains of Moab. The book alternates between legislative material inherited from Sinai and narrative accounts of Israel's journey and failures. Its major episodes include the twelve spies and the resulting judgment of forty years in the wilderness (Numbers 13–14), Korah's rebellion (16), the bronze serpent (21), the oracles of Balaam (22–24), and the Phinehas incident (25).</p><p>Numbers is deeply concerned with the tension between God's faithfulness and Israel's repeated unbelief. The two censuses (chapters 1 and 26) bracket the wilderness generation: the first counts those who came out of Egypt, the second counts their children who will enter the land. Paul cites Numbers as a warning to the church: the failures of the wilderness generation — idolatry, sexual immorality, testing Christ, grumbling — are written for our instruction (1 Corinthians 10:6–11). Hebrews 3:7–4:11 uses the wilderness generation's unbelief as a sustained warning against apostasy, and John 3:14 connects the bronze serpent typologically to the lifting up of the Son of Man.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "numbers-book-of", "smith": "numbers-book-of", "isbe": "numbers-book-of"},
        "key_refs": ["Numbers 14:22", "Numbers 21:9", "1 Corinthians 10:11", "John 3:14"]
    },
    "nun": {
        "id": "nun",
        "term": "Nun",
        "category": "people",
        "intro": "<p>Nun (meaning <em>continuance</em> or <em>propagation</em>; also rendered Non in 1 Chronicles 7:27) was an Ephraimite and the father of Joshua, Moses's successor. He appears in Scripture only in his paternal role: Joshua is consistently identified as \"Joshua the son of Nun\" throughout the Pentateuch and the historical books, distinguishing him from other individuals named Joshua. Nun himself has no recorded deeds; his significance lies entirely in his son. He was of the tribe of Ephraim, and 1 Chronicles 7:27 places him in the lineage from Ephraim through the descendants who eventually gave rise to Joshua's family.</p>",
        "hitchcock_meaning": "same as Non",
        "source_ids": {"easton": "nun", "smith": "nun"},
        "key_refs": ["Exodus 33:11", "Numbers 11:28", "Joshua 1:1"]
    },
    "nuts": {
        "id": "nuts",
        "term": "Nuts",
        "category": "concepts",
        "intro": "<p>Nuts appear in two distinct contexts in the Old Testament. In Genesis 43:11, Jacob instructed his sons to take gifts to the ruler of Egypt (Joseph, whom they did not yet recognize), including \"nuts\" (Hebrew <em>botnim</em>), identified as pistachios — prized as a luxury item and delicacy in the ancient Near East. This was among the \"best fruits in the land\" of Canaan that Jacob sent as a conciliatory gift. In Song of Solomon 6:11, the beloved descends to \"the garden of nuts\" (Hebrew <em>egoz</em>, walnuts) to see the blossoms of the valley — a scene of springtime beauty and budding life. Walnut trees were common in the region of Lebanon and the Jordan valley.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "nuts", "smith": "nuts"},
        "key_refs": ["Genesis 43:11", "Song of Solomon 6:11"]
    },
    "nymphas": {
        "id": "nymphas",
        "term": "Nymphas",
        "category": "people",
        "intro": "<p>Nymphas (meaning <em>spouse</em> or <em>bridegroom</em>) was a Christian at Laodicea (or possibly Hierapolis or Colossae) in whose house a church met. Paul sends greetings to him and the church in his house in Colossians 4:15: \"Salute the brethren which are in Laodicea, and Nymphas, and the church which is in his house.\" The gender of the name is debated in manuscript tradition — some manuscripts read Nymphas (masculine), others Nympha (feminine) — with a corresponding variation in the pronoun used. As a house-church host, Nymphas was evidently a person of some means and standing who provided space for Christian assembly in the absence of dedicated church buildings in the first century.</p>",
        "hitchcock_meaning": "spouse; bridegroom",
        "source_ids": {"easton": "nymphas", "smith": "nymphas"},
        "key_refs": ["Colossians 4:15"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP n2: Net → Nymphas: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
