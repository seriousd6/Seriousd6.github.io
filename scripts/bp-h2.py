"""
BP Article Synthesis — h2: Hare → Hebrews, Epistle to
Covers Easton entries: Hare through Hebrews, Epistle to (75 entries)

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

Script: scripts/bp-h2.py
Run: python3 scripts/bp-h2.py
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
    "hare": {
        "id": "hare",
        "term": "Hare",
        "category": "concepts",
        "intro": "<p>The hare (Hebrew <em>'arnebeth</em>) is listed among the animals prohibited as food under the Mosaic dietary law (Leviticus 11:6; Deuteronomy 14:7). It is classified as \"unclean\" on the grounds that it \"cheweth the cud\" but does not part the hoof — making it unclean under the dual criteria of the Mosaic food code. Zoologically, the hare does not technically ruminate; it practices <em>caecotrophy</em> — the re-ingestion of soft cecal pellets — which the biblical text may have observed as an apparent chewing motion, sufficient for the practical categorization of ancient law without requiring modern biological precision. Two species of hare were common in Palestine: the Syrian hare (<em>Lepus syriacus</em>) and the Egyptian hare (<em>Lepus aegypticus</em>), both still found in the region.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hare", "smith": "hare"},
        "key_refs": ["Leviticus 11:6", "Deuteronomy 14:7"]
    },
    "hareth": {
        "id": "hareth",
        "term": "Hareth",
        "category": "places",
        "intro": "<p>Hareth (meaning <em>thicket</em>) was a wood or forest in the mountains of Judah where David took refuge with his men during the period of his flight from King Saul. The prophet Gad instructed David to leave the cave of Adullam and go into the land of Judah, and David went to the forest of Hareth (1 Samuel 22:5). Its exact location has not been identified with certainty, though it lay in the hill country of Judah. The adjacent verse (2 Samuel 23:14; 1 Chronicles 11:16) mentions a Philistine garrison at Bethlehem and David holding the stronghold, suggesting Hareth was somewhere in the general area between Adullam and Bethlehem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hareth", "smith": "hareth"},
        "key_refs": ["1 Samuel 22:5"]
    },
    "harhaiah": {
        "id": "harhaiah",
        "term": "Harhaiah",
        "category": "people",
        "intro": "<p>Harhaiah (meaning <em>heat</em> or <em>anger of the LORD</em>) was the father of Uzziel, a goldsmith who worked on the repair of the Jerusalem wall under Nehemiah's direction (Nehemiah 3:8). Uzziel son of Harhaiah is listed among the guild craftsmen who repaired a section of the wall near the city center during the great restoration project of approximately 445 BC. The family's trade as goldsmiths and perfumers represented the skilled artisan class of post-exilic Jerusalem.</p>",
        "hitchcock_meaning": "heat, or anger, of the Lord",
        "source_ids": {"easton": "harhaiah", "smith": "harhaiah"},
        "key_refs": ["Nehemiah 3:8"]
    },
    "harhur": {
        "id": "harhur",
        "term": "Harhur",
        "category": "people",
        "intro": "<p>Harhur (meaning <em>fever</em> or <em>made warm</em>) was one of the Nethinim — the temple servants of non-Israelite origin who assisted the Levites in menial temple duties. His descendants are listed among the Nethinim who returned from Babylonian exile with Zerubbabel (Ezra 2:51; Nehemiah 7:53). The Nethinim were likely descendants of the Gibeonites (Joshua 9:27) or other captive peoples assigned to temple service, and their faithful return to Jerusalem to resume their duties reflects the restoration of the full temple administration under Zerubbabel and later Ezra.</p>",
        "hitchcock_meaning": "made warm",
        "source_ids": {"easton": "harhur", "smith": "harhur"},
        "key_refs": ["Ezra 2:51", "Nehemiah 7:53"]
    },
    "harim": {
        "id": "harim",
        "term": "Harim",
        "category": "people",
        "intro": "<p>Harim (meaning <em>flat-nosed</em>, <em>destroyed</em>, or <em>dedicated to God</em>) is the name of several individuals in the Old Testament. The most prominent is the head of the third division of priests appointed by David for temple service (1 Chronicles 24:8). His descendants were among those who returned from the Babylonian exile: Ezra 2:32 and Nehemiah 7:35 list 320 members of the family of Harim among the lay returnees, and Ezra 2:39 lists 1,017 descendants of Harim among the priests who returned. Multiple Harims appear in the post-exilic records: a priest who signed the covenant renewal under Nehemiah (Nehemiah 10:5) and a lay leader who also signed (Nehemiah 10:27), as well as several individuals who had married foreign women and agreed to put them away under Ezra's reform (Ezra 10:21, 31).</p>",
        "hitchcock_meaning": "destroyed; dedicated to God",
        "source_ids": {"easton": "harim", "smith": "harim"},
        "key_refs": ["1 Chronicles 24:8", "Ezra 2:32", "Ezra 2:39", "Nehemiah 10:5"]
    },
    "hariph": {
        "id": "hariph",
        "term": "Hariph",
        "category": "people",
        "intro": "<p>Hariph (meaning <em>autumnal rain</em>) is the name of a family head in post-exilic Judah. Nehemiah 7:24 lists 112 men of the children of Hariph among those who returned from Babylon. A leader named Hariph also appears among the signatories of the covenant renewal under Nehemiah (Nehemiah 10:19), pledging to walk in God's law and separate from the surrounding peoples. The name may be the same as Jorah in Ezra 2:18, which lists a family group of 112 as well, suggesting a textual variant between the two lists.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hariph", "smith": "hariph"},
        "key_refs": ["Nehemiah 7:24", "Nehemiah 10:19"]
    },
    "harlot": {
        "id": "harlot",
        "term": "Harlot",
        "category": "concepts",
        "intro": "<p>Harlot translates two Hebrew terms in the Old Testament that must be distinguished. <em>Zonah</em> (Genesis 34:31; 38:15) is the common word for a prostitute — a woman who exchanges sexual access for payment. <em>Qedeshah</em> (Genesis 38:21–22; Deuteronomy 23:17), rendered \"harlot\" in the KJV, more precisely denotes a cult prostitute associated with the fertility shrines of Canaan — a role explicitly prohibited in Mosaic law. The Mosaic code condemned all prostitution, forbade the bringing of a harlot's wages into the temple (Deuteronomy 23:18), and required that priests not marry a harlot (Leviticus 21:14).</p><p>Despite this moral condemnation, harlots appear in several pivotal narratives: Rahab the harlot of Jericho protected the Israelite spies and is listed in the faith roll of Hebrews 11:31 and in the genealogy of Jesus (Matthew 1:5; James 2:25). Jephthah's mother was a harlot (Judges 11:1). Samson visited a harlot at Gaza (Judges 16:1). Solomon adjudicated between two harlots (1 Kings 3:16). The prophets, especially Hosea (chapters 1–3), Jeremiah (3:1–3), and Ezekiel (chapters 16; 23), used the harlot metaphor extensively for Israel's unfaithfulness to God through idolatry. In the New Testament, Jesus declared that \"harlots\" were entering the kingdom before the self-righteous (Matthew 21:31–32), and Revelation's great harlot Babylon (Revelation 17–18) symbolizes the empire of spiritual unfaithfulness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harlot", "smith": "harlot"},
        "key_refs": ["Genesis 38:15", "Deuteronomy 23:17", "Hebrews 11:31", "Revelation 17:1"]
    },
    "harnepher": {
        "id": "harnepher",
        "term": "Harnepher",
        "category": "people",
        "intro": "<p>Harnepher (meaning <em>the anger of a bull</em> or <em>increasing heat</em>) was a chief of the tribe of Asher listed in the genealogy of 1 Chronicles 7:36 as a son of Zophah. He appears in the tribal genealogies as one of the heads of Asher's clans — a man of valor and chief among the princes (1 Chronicles 7:40). Beyond this genealogical mention, nothing further is recorded about him in the biblical text.</p>",
        "hitchcock_meaning": "the anger of a bull; increasing heat",
        "source_ids": {"easton": "harnepher", "smith": "harnepher"},
        "key_refs": ["1 Chronicles 7:36"]
    },
    "harness": {
        "id": "harness",
        "term": "Harness",
        "category": "concepts",
        "intro": "<p>Harness in the Old Testament refers both to the yoke and tackle used to fasten animals to a cart or plough, and to military armor. The Hebrew <em>'asar</em> (\"to bind\") describes the fastening of animals: 1 Samuel 6:7 records the Philistines yoking two milk cows (<em>'asar</em>) to the cart carrying the ark of God. In a military sense, harness refers to the coat of armor or battle equipment worn by soldiers: 1 Kings 22:34 describes the random arrow that struck Ahab \"between the joints of the harness\" — i.e., between the plates of his armor — mortally wounding him despite his disguise.</p><p>Jeremiah 46:4 calls Egypt's warriors to \"harness the horses\" — meaning to yoke or equip them for battle. 2 Chronicles 9:24 mentions that Solomon received tribute including \"harness\" (translated \"armor\" in modern versions) and spices. The concept of putting on armor as preparation for battle became a rich metaphor in Paul's writing: the full armor of God in Ephesians 6:11–17 translates military harness imagery into spiritual disciplines and resources for the believer's struggle against evil.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harness"},
        "key_refs": ["1 Samuel 6:7", "1 Kings 22:34", "Jeremiah 46:4", "Ephesians 6:11"]
    },
    "harod": {
        "id": "harod",
        "term": "Harod",
        "category": "places",
        "intro": "<p>Harod (meaning <em>palpitation</em> or <em>trembling</em>, related to astonishment and fear) was a fountain in the Valley of Jezreel where Gideon assembled his army before the battle against the Midianites (Judges 7:1). The spring of Harod is the site where God reduced Gideon's force from 32,000 to 300 men — first by releasing those who were afraid (22,000 left), then by testing the manner of drinking at the water (only 300 lapped water with their hands to their mouths rather than kneeling to drink). The dramatic reduction of the army was designed to ensure that Israel could not claim the victory as their own achievement but would recognize it as the LORD's deliverance.</p><p>The spring of Harod has been identified with 'Ain Jalud at the foot of Mount Gilboa, a powerful spring that still flows today in the Jezreel Valley. The Philistine forces encamped at the same spring in a later period (1 Samuel 29:1), and two of David's mighty men, Shammah and Elika, were described as \"Harodites\" (2 Samuel 23:25), suggesting they came from a village near this spring.</p>",
        "hitchcock_meaning": "astonishment; fear",
        "source_ids": {"easton": "harod", "smith": "harod"},
        "key_refs": ["Judges 7:1", "Judges 7:4", "Judges 7:7", "1 Samuel 29:1"]
    },
    "harodite": {
        "id": "harodite",
        "term": "Harodite",
        "category": "concepts",
        "intro": "<p>Harodite is a geographical designation applied to two of David's elite warriors in 2 Samuel 23:25: Shammah the Harodite and Elika the Harodite. The epithet indicates they were from the area of Harod, the spring in the Valley of Jezreel near Mount Gilboa where Gideon had encamped before his victory over Midian (Judges 7:1). In the parallel passage of 1 Chronicles 11:27, Shammah is called \"the Harorite\" — a variant spelling that may reflect a copying error or a slightly different village name. Both warriors were among the thirty mighty men whose deeds of valor on behalf of David are commemorated in the military rosters of the Davidic kingdom.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harodite"},
        "key_refs": ["2 Samuel 23:25", "1 Chronicles 11:27"]
    },
    "harosheth-of-the-gentiles": {
        "id": "harosheth-of-the-gentiles",
        "term": "Harosheth of the Gentiles",
        "category": "places",
        "intro": "<p>Harosheth of the Gentiles (literally <em>the woodlands of the nations</em>) was the home city and military base of Sisera, the captain of the army of Jabin king of Canaan (Judges 4:2), and was located near Hazor in the northern Jezreel Valley region. Sisera garrisoned at Harosheth his 900 iron chariots — the military superiority that made Jabin's oppression of Israel so daunting for twenty years. After the victory of Deborah and Barak on Mount Tabor, the fleeing Canaanite army was pursued to Harosheth: \"All the host of Sisera fell upon the edge of the sword; and there was not a man left\" (Judges 4:16).</p><p>The city's name includes a reference to \"Gentiles\" or \"nations\" (<em>hagoyim</em>), suggesting it was a mixed or predominantly non-Israelite population center. It has been tentatively identified with Tell Amr near modern Haifa at the northern entrance to the Jezreel Valley, where the Kishon River exits into the coastal plain — a strategic location that controlled the route between the valley and the coast.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harosheth-of-the-gentiles"},
        "key_refs": ["Judges 4:2", "Judges 4:13", "Judges 4:16"]
    },
    "harp": {
        "id": "harp",
        "term": "Harp",
        "category": "concepts",
        "intro": "<p>The harp (Hebrew <em>kinnor</em>) was the national musical instrument of Israel and one of the oldest stringed instruments known to antiquity. Jubal is credited with its invention (Genesis 4:21), and it appears in the earliest patriarchal narratives: Laban rebuked Jacob for leaving without giving him a chance to send him away \"with mirth, and with songs, with tabret, and with harp\" (Genesis 31:27). The <em>kinnor</em> was played by David to soothe Saul's troubled spirit (1 Samuel 16:23) and was among the instruments played by the prophetic bands (1 Samuel 10:5). David organized large choirs and orchestras using harps for the worship at Jerusalem (1 Chronicles 15:16; 25:1–6).</p><p>The precise form of the Israelite <em>kinnor</em> is debated — it may have resembled a lyre more than a true harp, with strings stretched across a frame and plucked rather than a vertical column. It was used in both joyful celebration (Isaiah 24:8; Revelation 5:8; 14:2) and in lament: the exiles in Babylon hung their harps on the willow trees by the rivers, unable to sing the LORD's song in a foreign land (Psalm 137:2). In Revelation, harps accompany the song of the redeemed in the heavenly worship (Revelation 5:8; 14:2; 15:2).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harp", "smith": "harp"},
        "key_refs": ["Genesis 4:21", "1 Samuel 16:23", "Psalms 137:2", "Revelation 5:8"]
    },
    "harrow": {
        "id": "harrow",
        "term": "Harrow",
        "category": "concepts",
        "intro": "<p>Harrow in the Old Testament translates the Hebrew <em>harits</em>, which describes a sharp threshing sledge — a heavy wooden frame fitted with sharp stones or iron teeth on its underside, dragged over harvested grain to thresh it and cut the stalks. The implement is mentioned in 2 Samuel 12:31 and 1 Chronicles 20:3 in the description of David's treatment of the Ammonites after the siege of Rabbah, where the text states he put the population under or over saws, harrows of iron, and axes. This passage is debated: some translations and commentators read it as forced labor rather than execution.</p><p>Job 39:10 uses the term in questioning whether a human being can bind or harrow the valley with a wild ox, illustrating the animal's uncontrollable strength. Isaiah 28:24 refers to the farmer who \"harreth\" (breaks up) the ground for sowing. The implement's function of breaking and cutting made it a natural figure for destructive judgment, while its agricultural use in preparing the soil for seed was also available as a metaphor for redemptive preparation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harrow", "smith": "harrow"},
        "key_refs": ["2 Samuel 12:31", "Job 39:10", "Isaiah 28:24"]
    },
    "harsha": {
        "id": "harsha",
        "term": "Harsha",
        "category": "people",
        "intro": "<p>Harsha (meaning <em>worker</em> or <em>enchanter</em>) was a temple servant (Nethinim) whose descendants returned from the Babylonian exile with Zerubbabel (Ezra 2:52; Nehemiah 7:54). The Nethinim were a class of temple workers, probably descendants of non-Israelite peoples assigned to menial service in the sanctuary. Their return to Jerusalem after the exile demonstrates the continuity of the temple service community and their attachment to the worship of the God of Israel despite their mixed ethnic origins.</p>",
        "hitchcock_meaning": "workmanship; a wood",
        "source_ids": {"easton": "harsha", "smith": "harsha"},
        "key_refs": ["Ezra 2:52", "Nehemiah 7:54"]
    },
    "hart": {
        "id": "hart",
        "term": "Hart",
        "category": "concepts",
        "intro": "<p>Hart (Hebrew <em>'ayal</em>) is the male deer or stag, one of the clean animals permitted as food under the Mosaic law (Deuteronomy 12:15; 14:5). It was a prized game animal in Israel, listed among the provisions brought daily for Solomon's table (1 Kings 4:23). The hart's swiftness, grace, and intense thirst made it a natural source of imagery in Hebrew poetry: Psalm 42:1 opens with the famous simile \"As the hart panteth after the water brooks, so panteth my soul after thee, O God\" — an image of intense spiritual longing that became one of the most beloved expressions of devotion in the Psalter.</p><p>Song of Solomon 2:9 and 8:14 compare the beloved to a roe or young hart leaping on the mountains — an image of eagerness and graceful approach. Isaiah 35:6 prophesies that in the day of restoration \"the lame man shall leap as an hart\" — one of several images in that chapter depicting the reversal of all debility and limitation. The hart thus serves in Scripture as a figure for longing, swiftness, and the joy of full restoration.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hart", "smith": "hart"},
        "key_refs": ["Deuteronomy 14:5", "Psalms 42:1", "Isaiah 35:6", "Song of Solomon 2:9"]
    },
    "harum": {
        "id": "harum",
        "term": "Harum",
        "category": "people",
        "intro": "<p>Harum (meaning <em>elevated</em> or <em>high</em>) was a descendant of Judah listed in the tribal genealogy of 1 Chronicles 4:8 as a member of the family of Koz. The genealogy connects him to the line of Judah through Haahashtari and Naarah, within the extended genealogical register that Chronicles provides for the leading families of Judah. Beyond this genealogical reference, nothing further is recorded about him in the biblical text.</p>",
        "hitchcock_meaning": "high; throwing down",
        "source_ids": {"easton": "harum", "smith": "harum"},
        "key_refs": ["1 Chronicles 4:8"]
    },
    "haruphite": {
        "id": "haruphite",
        "term": "Haruphite",
        "category": "concepts",
        "intro": "<p>Haruphite is a geographical or clan designation applied to Shephatiah, one of the Benjaminite warriors who came to David at Ziklag during his time of refuge from Saul (1 Chronicles 12:5). The epithet indicates that Shephatiah was from the village of Hariph — possibly the same location as \"Hariph\" in the post-exilic census lists (Nehemiah 7:24), or from a village in Benjamin whose name is not otherwise recorded. These Benjaminite warriors who joined David despite belonging to Saul's own tribe represent a significant transfer of loyalty, recognized by the chronicler as evidence of God's support for David's kingship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "haruphite"},
        "key_refs": ["1 Chronicles 12:5"]
    },
    "haruz": {
        "id": "haruz",
        "term": "Haruz",
        "category": "people",
        "intro": "<p>Haruz (meaning <em>eager</em> or <em>careful</em>) was the father of Meshullemeth, the wife of Manasseh king of Judah and mother of Amon (2 Kings 21:19). He was from Jotbah, a location in Galilee, making Meshullemeth one of the northern women who married into the Judahite royal family. Amon succeeded his father Manasseh and reigned for two years before being assassinated by his servants. The mention of Haruz's hometown and patronymic in the royal succession formula is consistent with the Deuteronomistic History's standard notation of each king's mother's name and origin — a practice that recognized the queen mother's significance in ancient Israelite court life.</p>",
        "hitchcock_meaning": "careful",
        "source_ids": {"easton": "haruz", "smith": "haruz"},
        "key_refs": ["2 Kings 21:19"]
    },
    "harvest": {
        "id": "harvest",
        "term": "Harvest",
        "category": "concepts",
        "intro": "<p>Harvest in Israel followed an agricultural calendar determined by the seasons of the land. The barley harvest came first, beginning around the sixteenth of Abib (March–April) — the day of the wave-offering of firstfruits that opened the harvest season (Leviticus 23:9–14). The wheat harvest followed several weeks later, concluding at Pentecost (the Feast of Weeks, fifty days after Passover). The grape and olive harvest completed the annual agricultural cycle in the autumn (August–October). Ruth's gleaning in the barley and wheat harvests (Ruth 2:23) and the period of the early rains that preceded sowing (1 Samuel 12:17) placed harvest in its precise seasonal slot in the ancient Israelite year.</p><p>Theologically, harvest functions as both celebration and judgment in Scripture. The feast calendar organized around harvest commemorated God's provision and the covenant's fruitfulness. The prophets and Jesus used harvest as a figure for judgment: Isaiah 17:5–6 pictures the eschatological gleaning of Israel; Jeremiah 8:20 mourns \"harvest is past, the summer is ended, and we are not saved.\" Jesus taught that the harvest is the end of the age when the righteous and wicked will be separated (Matthew 13:39), and the fields already white for harvest are the nations ready to receive the gospel (John 4:35). Revelation 14:14–16 presents the final harvest of the earth as an act of divine sovereignty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harvest", "smith": "harvest"},
        "key_refs": ["Leviticus 23:9", "Ruth 2:23", "John 4:35", "Revelation 14:15"]
    },
    "hasadiah": {
        "id": "hasadiah",
        "term": "Hasadiah",
        "category": "people",
        "intro": "<p>Hasadiah (meaning <em>favored by Jehovah</em> or <em>the mercy of the LORD</em>) was one of the sons of Pedaiah, listed in the post-exilic royal genealogy of 1 Chronicles 3:20 as a descendant of Zerubbabel and of the line of David. He represents the continuation of the Davidic line in the Persian period, several generations after the return from Babylon. The careful recording of these post-exilic Davidic descendants in Chronicles reflects the ongoing messianic hope that a son of David would eventually reign over a restored Israel.</p>",
        "hitchcock_meaning": "the mercy of the Lord",
        "source_ids": {"easton": "hasadiah", "smith": "hasadiah"},
        "key_refs": ["1 Chronicles 3:20"]
    },
    "hasenuah": {
        "id": "hasenuah",
        "term": "Hasenuah",
        "category": "people",
        "intro": "<p>Hasenuah (meaning <em>bristling</em> or <em>hated</em>) was a Benjaminite whose son Hodaviah is listed among those who settled in Jerusalem after the return from exile (1 Chronicles 9:7). The name appears in the genealogical records of Benjamin as part of the restoration community's effort to repopulate Jerusalem. Nehemiah 11:9 mentions a Judah son of Hasenuah as the second in charge of the city of Jerusalem, suggesting the family held a position of local administrative authority in the restored community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hasenuah", "smith": "hasenuah"},
        "key_refs": ["1 Chronicles 9:7", "Nehemiah 11:9"]
    },
    "hashabiah": {
        "id": "hashabiah",
        "term": "Hashabiah",
        "category": "people",
        "intro": "<p>Hashabiah (meaning <em>regarded by Jehovah</em> or <em>the estimation of the LORD</em>) is one of the more frequently recurring names in the post-exilic period, borne by at least a dozen individuals in Chronicles, Ezra, and Nehemiah. Among the most notable: (1) a Merarite Levite in the Davidic genealogy of the temple singers (1 Chronicles 6:45; 9:14); (2) a son of Jeduthun, appointed to lead the twelfth course of Levitical musicians (1 Chronicles 25:3, 19); (3) a chief of the Hebronites whom David set over the tribes west of the Jordan for all affairs of God and the king (1 Chronicles 26:30); (4) a chief Levite under Josiah who contributed to the Passover celebration (2 Chronicles 35:9); and (5) a leader who traveled with Ezra from Babylon and was entrusted with the temple treasures for the journey (Ezra 8:19, 24). Several Hashabiahites signed the covenant renewal under Nehemiah (Nehemiah 10:11; 11:15, 22; 12:21, 24).</p>",
        "hitchcock_meaning": "the estimation of the Lord",
        "source_ids": {"easton": "hashabiah", "smith": "hashabiah"},
        "key_refs": ["1 Chronicles 6:45", "1 Chronicles 26:30", "Ezra 8:19", "Nehemiah 10:11"]
    },
    "hashabniah": {
        "id": "hashabniah",
        "term": "Hashabniah",
        "category": "people",
        "intro": "<p>Hashabniah is the name of two individuals in the post-exilic period. The first is the father of Hattush, who repaired a section of the Jerusalem wall under Nehemiah's direction (Nehemiah 3:10). The second is one of the Levites whom Ezra appointed to lead the congregation in a liturgical prayer of confession and covenant renewal — a long prayer recounting Israel's history from the creation through the exile (Nehemiah 9:5). This Levitical role in the public reading of history and covenant renewal reflects the central function of the Levites in the restoration community's spiritual life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hashabniah", "smith": "hashabniah"},
        "key_refs": ["Nehemiah 3:10", "Nehemiah 9:5"]
    },
    "hashbadana": {
        "id": "hashbadana",
        "term": "Hashbadana",
        "category": "people",
        "intro": "<p>Hashbadana (meaning <em>consideration in judging</em>) was one of the men who stood at Ezra's left hand when Ezra read the book of the law to the assembled congregation of Israel at the Water Gate in Jerusalem (Nehemiah 8:4). The public reading of the Torah to the whole assembly — men, women, and children old enough to understand — was a landmark moment in the spiritual restoration of post-exilic Judah, and those who stood beside Ezra on the wooden platform served as ceremonial witnesses and assistants to the event. Six men stood on Ezra's right and seven on his left, representing the community's leadership gathered for this covenant renewal occasion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hashbadana", "smith": "hashbadana"},
        "key_refs": ["Nehemiah 8:4"]
    },
    "hashmonah": {
        "id": "hashmonah",
        "term": "Hashmonah",
        "category": "places",
        "intro": "<p>Hashmonah (meaning <em>fatness</em>) was the thirtieth stopping place of the Israelites during their forty years of wilderness wandering, situated between Mithkah and Moseroth (Numbers 33:29–30). Its precise location in the Sinai or Negev region has not been definitively identified. Like many of the wilderness station names in Numbers 33, it appears only in the itinerary list and carries no narrative detail. The progression of stations through Numbers 33 traces Israel's route from Egypt to the plains of Moab before the crossing of the Jordan, and Hashmonah represents one waypoint in that long journey through the wilderness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hashmonah", "smith": "hashmonah"},
        "key_refs": ["Numbers 33:29", "Numbers 33:30"]
    },
    "hashub": {
        "id": "hashub",
        "term": "Hashub",
        "category": "people",
        "intro": "<p>Hashub (meaning <em>intelligent</em> or <em>esteemed</em>) is the name of several individuals in the post-exilic period. Among them: (1) a Levite of the family of Merari, listed among those who settled in Jerusalem after the exile (Nehemiah 11:15; 1 Chronicles 9:14); (2) a son of Pahath-moab who repaired a section of the Jerusalem wall and the Tower of the Furnaces under Nehemiah (Nehemiah 3:11); (3) another wall builder who repaired the section opposite his own house (Nehemiah 3:23); and (4) a signatory of the covenant renewal under Nehemiah (Nehemiah 10:23). The name's recurrence in the wall-building project and covenant renewal reflects a community of Levitical and lay leaders actively rebuilding both the physical and spiritual infrastructure of post-exilic Jerusalem.</p>",
        "hitchcock_meaning": "esteemed; numbered",
        "source_ids": {"easton": "hashub", "smith": "hashub"},
        "key_refs": ["Nehemiah 3:11", "Nehemiah 3:23", "Nehemiah 10:23"]
    },
    "hashubah": {
        "id": "hashubah",
        "term": "Hashubah",
        "category": "people",
        "intro": "<p>Hashubah (meaning <em>estimation</em> or <em>thought</em>) was a son of Zerubbabel listed in the post-exilic Davidic genealogy of 1 Chronicles 3:20. He is one of seven children of Zerubbabel named in this passage, representing the continuation of the royal Davidic line into the Persian period after the return from Babylon. The preservation of these names in the Chronicler's genealogy reflects the ongoing theological importance of the Davidic lineage for the post-exilic community's messianic hope.</p>",
        "hitchcock_meaning": "estimation; thought",
        "source_ids": {"easton": "hashubah", "smith": "hashubah"},
        "key_refs": ["1 Chronicles 3:20"]
    },
    "hashum": {
        "id": "hashum",
        "term": "Hashum",
        "category": "people",
        "intro": "<p>Hashum (meaning <em>opulent</em> or <em>their silence</em>) is the name of two individuals in the post-exilic records. The first is the head of a family of returnees from Babylon: 228 men of the children of Hashum are listed in Ezra 2:19 (Nehemiah 7:22 gives 328) among those who returned with Zerubbabel. Seven members of this family had married foreign women and were included in Ezra's reform (Ezra 10:33). The second Hashum stood at Ezra's left hand during the public reading of the law at the Water Gate (Nehemiah 8:4) and also signed the covenant renewal document (Nehemiah 10:18), suggesting a prominent lay leader in the Jerusalem community.</p>",
        "hitchcock_meaning": "silence; their hasting",
        "source_ids": {"easton": "hashum", "smith": "hashum"},
        "key_refs": ["Ezra 2:19", "Nehemiah 8:4", "Nehemiah 10:18"]
    },
    "hasrah": {
        "id": "hasrah",
        "term": "Hasrah",
        "category": "people",
        "intro": "<p>Hasrah (meaning <em>poverty</em> or <em>wanting</em>) was the grandfather of Shallum, the husband of Huldah the prophetess (2 Chronicles 34:22). In the parallel passage of 2 Kings 22:14, Hasrah is given as Harhas — a variant spelling. Shallum held the position of keeper of the wardrobe (possibly the priestly vestments or royal wardrobe), and his wife Huldah was the prophetess whom King Josiah's delegation consulted after the discovery of the book of the law in the temple. Huldah's response confirmed the authenticity of the book and prophesied both judgment on Judah and Josiah's peaceful death before the coming disaster.</p>",
        "hitchcock_meaning": "wanting",
        "source_ids": {"easton": "hasrah", "smith": "hasrah"},
        "key_refs": ["2 Chronicles 34:22", "2 Kings 22:14"]
    },
    "hasupha": {
        "id": "hasupha",
        "term": "Hasupha",
        "category": "people",
        "intro": "<p>Hasupha (meaning <em>uncovered</em> or <em>made bare</em>) was a temple servant (Nethinim) whose descendants returned from Babylonian exile with Zerubbabel and were listed in the census of returnees (Ezra 2:43; Nehemiah 7:46). The Nethinim were a hereditary class of temple workers, and their return to Jerusalem to resume their duties in the temple service represents an important continuity between the pre-exilic and post-exilic temple communities. The inclusion of Hasupha's family in both the Ezra and Nehemiah lists confirms their place in the official record of the restoration community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hasupha", "smith": "hasupha"},
        "key_refs": ["Ezra 2:43", "Nehemiah 7:46"]
    },
    "hat": {
        "id": "hat",
        "term": "Hat",
        "category": "concepts",
        "intro": "<p>Hat appears in the King James Version at Daniel 3:21 (Chaldean <em>karb'ela</em>), where it describes one of the garments worn by Shadrach, Meshach, and Abednego when they were thrown into the fiery furnace: \"their coats, their hosen, and their hats, and their other garments.\" The Aramaic term is of uncertain meaning — it may refer to a mantle, a cloak (<em>pallium</em>), or a head covering. The Revised Version renders it as \"mantles,\" and modern translations vary between \"cloaks,\" \"robes,\" \"turbans,\" or \"other clothing.\" The point of the verse is that the men were bound and thrown in still wearing all their clothing, making the subsequent report that not even the smell of fire was on them (Daniel 3:27) all the more remarkable.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hat"},
        "key_refs": ["Daniel 3:21"]
    },
    "hatach": {
        "id": "hatach",
        "term": "Hatach",
        "category": "people",
        "intro": "<p>Hatach (meaning <em>verity</em> or <em>he that strikes</em>) was a eunuch or chamberlain in the palace of Ahasuerus (Xerxes) of Persia, appointed by the king to attend Queen Esther (Esther 4:5–10). He served as the crucial intermediary between Esther in the palace and Mordecai at the king's gate during the crisis of Haman's decree against the Jews. Hatach carried Esther's questions to Mordecai, brought back Mordecai's urgent message about the decree and his appeal to Esther to intercede with the king, and returned to tell Esther Mordecai's response — including the famous statement that Esther had come to the kingdom \"for such a time as this\" (Esther 4:14).</p>",
        "hitchcock_meaning": "he that strikes",
        "source_ids": {"easton": "hatach", "smith": "hatach"},
        "key_refs": ["Esther 4:5", "Esther 4:9", "Esther 4:10"]
    },
    "hathath": {
        "id": "hathath",
        "term": "Hathath",
        "category": "people",
        "intro": "<p>Hathath (meaning <em>terror</em> or <em>fear</em>) was a son of Othniel, the first judge of Israel, listed in the Judahite genealogy of 1 Chronicles 4:13. Othniel son of Kenaz — who had also distinguished himself by capturing Kirjath-sepher (Judges 1:12–13; 3:9–11) — founded a lineage in Judah that included Hathath and Meonothai. Beyond this genealogical reference, nothing further is recorded about Hathath himself in the biblical text. His father Othniel remains the more significant figure, known as the judge who delivered Israel from Cushan-rishathaim king of Mesopotamia.</p>",
        "hitchcock_meaning": "fear",
        "source_ids": {"easton": "hathath", "smith": "hathath"},
        "key_refs": ["1 Chronicles 4:13"]
    },
    "hatipha": {
        "id": "hatipha",
        "term": "Hatipha",
        "category": "people",
        "intro": "<p>Hatipha (meaning <em>captured</em>) was a temple servant (Nethinim) whose descendants returned from the Babylonian exile and are listed in the census of returnees (Ezra 2:54; Nehemiah 7:56). Like the other Nethinim families, Hatipha's descendants resumed their temple service duties in Jerusalem after the return under Zerubbabel. The meaning of the name — \"captured\" — may reflect the origin of this family as war captives or enslaved persons incorporated into the temple service in an earlier period of Israel's history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hatipha", "smith": "hatipha"},
        "key_refs": ["Ezra 2:54", "Nehemiah 7:56"]
    },
    "hatita": {
        "id": "hatita",
        "term": "Hatita",
        "category": "people",
        "intro": "<p>Hatita (meaning <em>exploration</em> or <em>a bending of sin</em>) was a temple porter or gatekeeper whose descendants returned from the Babylonian exile with Zerubbabel (Ezra 2:42; Nehemiah 7:45). The temple porters (<em>sha'arim</em>) were the gatekeepers who controlled access to the temple courts, a role that carried significant responsibility for maintaining the holiness of the sanctuary. Their return to Jerusalem and resumption of gatekeeper duties formed part of the broader restoration of the Levitical service infrastructure under Zerubbabel and Jeshua.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hatita", "smith": "hatita"},
        "key_refs": ["Ezra 2:42", "Nehemiah 7:45"]
    },
    "hatred": {
        "id": "hatred",
        "term": "Hatred",
        "category": "concepts",
        "intro": "<p>Hatred in Scripture is categorized among the works of the flesh (Galatians 5:20 lists <em>echthrai</em>, enmities or hatreds, as a characteristic of the sinful nature) and is treated as a serious moral failing throughout both Testaments. The Mosaic law prohibited hatred of a kinsman in the heart: \"Thou shalt not hate thy brother in thine heart\" (Leviticus 19:17), placing inner attitude on par with outward action. Proverbs makes a sharp distinction between hatred that stirs up strife and love that covers sins (Proverbs 10:12; 1 Peter 4:8).</p><p>Jesus extended the standard: not only murder but anger toward a brother is subject to judgment (Matthew 5:21–22), and his summary of the law was love of God and neighbor — the antithesis of hatred. John declares that anyone who hates his brother is a murderer (1 John 3:15) and cannot claim to love God (1 John 4:20). The exception in Scripture to the prohibition on hatred is the hatred of evil itself: \"Ye that love the LORD, hate evil\" (Psalm 97:10), and the psalmist declares he hates those who hate God (Psalm 139:21–22) — an expression of covenant loyalty that is carefully distinguished from personal animosity. Luke 14:26's requirement to \"hate\" father and mother for Christ's sake uses the term comparatively (as demonstrated by the parallel in Matthew 10:37) to express supreme love for Christ above all other relationships.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hatred"},
        "key_refs": ["Galatians 5:20", "Leviticus 19:17", "1 John 3:15", "Psalms 97:10"]
    },
    "hattush": {
        "id": "hattush",
        "term": "Hattush",
        "category": "people",
        "intro": "<p>Hattush (meaning <em>assembled</em> or <em>forsaking sin</em>) is the name of four individuals in the post-exilic period. (1) A priest who returned to Jerusalem with Zerubbabel (Nehemiah 12:2). (2) A descendant of David and Shecaniah who returned with Ezra (Ezra 8:2; 1 Chronicles 3:22), significant as a member of the royal Davidic line returning to the land. (3) A son of Hashabniah who repaired part of the Jerusalem wall (Nehemiah 3:10). (4) A priest who signed the covenant renewal (Nehemiah 10:4). The name appears across both priestly and royal genealogies in the restoration period, suggesting multiple unrelated families bore it.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hattush"},
        "key_refs": ["Ezra 8:2", "Nehemiah 3:10", "Nehemiah 10:4", "Nehemiah 12:2"]
    },
    "hauran": {
        "id": "hauran",
        "term": "Hauran",
        "category": "places",
        "intro": "<p>Hauran (meaning <em>cave-land</em> or <em>hollow land</em>) is a region mentioned in Ezekiel's vision of the restored boundaries of Israel (Ezekiel 47:16, 18). It lay to the northeast of Canaan, encompassing the broad volcanic plateau east of the Sea of Galilee and south of Damascus, corresponding roughly to the region known in New Testament times as Gaulanitis and Trachonitis. The Hauran is characterized by its black basalt soil — extraordinarily fertile for grain farming and still one of the breadbaskets of the modern Middle East.</p><p>In Ezekiel's eschatological land division (Ezekiel 47–48), Hauran forms part of the northeastern boundary marker for the restored tribal territories. The region appears in ancient Assyrian records as \"Haurina\" and was contested between Israel, Damascus, and Assyria during the ninth and eighth centuries BC. In the Hellenistic and Roman periods it was known as Auranitis, and the broader region formed part of Philip's tetrarchy (Luke 3:1).</p>",
        "hitchcock_meaning": "a hole; liberty; whiteness",
        "source_ids": {"easton": "hauran", "smith": "hauran"},
        "key_refs": ["Ezekiel 47:16", "Ezekiel 47:18"]
    },
    "haven": {
        "id": "haven",
        "term": "Haven",
        "category": "places",
        "intro": "<p>A haven is a harbor or sheltered anchorage for ships, mentioned in both the Psalms and the New Testament. Psalm 107:30 uses the image of God bringing sailors \"unto their desired haven\" after a storm as a picture of divine deliverance, and the whole Psalm celebrates God's rescue of various travelers from danger — the desert wanderer, the prisoner, the sick, and the sailor — all brought to their destination by God's mercy. The haven is thus a figure for God's saving purpose reaching its completion.</p><p>In the New Testament, the account of Paul's voyage to Rome includes specific harbor references: the harbor of Fair Havens (Acts 27:8) on the south coast of Crete, where the ship Paul sailed on paused before the disastrous attempt to reach Phoenix for the winter. Paul warned against continuing the voyage (Acts 27:10), but the centurion followed the pilot's advice and they sailed into the storm that ultimately wrecked the ship on Malta. Ezekiel 27:3 describes Tyre as situated \"at the entry of the sea, a merchant of the people for many isles\" — a key haven in ancient Mediterranean trade.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "haven"},
        "key_refs": ["Psalms 107:30", "Acts 27:8", "Ezekiel 27:3"]
    },
    "havilah": {
        "id": "havilah",
        "term": "Havilah",
        "category": "places",
        "intro": "<p>Havilah (meaning <em>the sand region</em> or <em>that suffers pain</em>) is both a personal name and a geographical designation in the Old Testament. As a place, Havilah appears most notably in the Eden narrative: the Pishon river encircled the land of Havilah, where gold, bdellium, and the onyx stone were found (Genesis 2:11–12). The location is debated — some identify it with a region of Arabia or the Indian subcontinent based on the resources described; others place it in the upper Mesopotamian region. A second Havilah appears in the table of nations as the extent of the Ishmaelite territory: they \"dwelt from Havilah unto Shur, that is before Egypt\" (Genesis 25:18; 1 Samuel 15:7), placing this Havilah in the Arabian peninsula or Sinai region.</p><p>As a personal name, Havilah appears twice in the table of nations: as a son of Cush (Genesis 10:7) and as a son of Joktan (Genesis 10:29), representing two distinct peoples who perhaps settled in regions both bearing the name Havilah.</p>",
        "hitchcock_meaning": "that suffers pain; that brings forth",
        "source_ids": {"easton": "havilah", "smith": "havilah"},
        "key_refs": ["Genesis 2:11", "Genesis 10:7", "Genesis 25:18", "1 Samuel 15:7"]
    },
    "havoth-jair": {
        "id": "havoth-jair",
        "term": "Havoth-jair",
        "category": "places",
        "intro": "<p>Havoth-jair (meaning <em>the hamlets of the enlightener</em> or <em>villages of Jair</em>) was a district of villages in the Bashan region east of the Jordan, in the territory of Gilead and northern Transjordan. The name derives from Jair son of Manasseh, who captured the district during the conquest period and named the villages after himself (Numbers 32:41; Deuteronomy 3:14). The number of villages is given variously in different passages — 23 (Judges 10:4) or 30 (1 Kings 4:13) or 60 (1 Chronicles 2:22) — reflecting different extents of territory at different periods or textual variants.</p><p>The judge Jair (Judges 10:3–5), a Gileadite who judged Israel for twenty-two years, had thirty sons who rode on thirty ass colts and had thirty cities in Gilead, also called Havoth-jair — connecting the judge to the same territory as the earlier Jair son of Manasseh, perhaps as a descendant. Solomon's administrative district (1 Kings 4:13) included the \"towns of Jair\" in Gilead, showing the region's continued significance as an organized administrative unit in the monarchy period.</p>",
        "hitchcock_meaning": "the villages that enlighten",
        "source_ids": {"easton": "havoth-jair"},
        "key_refs": ["Numbers 32:41", "Deuteronomy 3:14", "Judges 10:4", "1 Kings 4:13"]
    },
    "hawk": {
        "id": "hawk",
        "term": "Hawk",
        "category": "concepts",
        "intro": "<p>The hawk (Hebrew <em>netz</em>, expressive of strong and rapid flight) designates a family of raptors including various species of falcon and hawk native to Palestine — the sparrowhawk, kestrel, and hobby among them. Several species of hawk were migratory visitors to Canaan, making \"the hawk flying toward the south\" (Job 39:26) a natural observation about the seasonal movements of birds of prey. Leviticus 11:16 and Deuteronomy 14:15 list the hawk among the unclean birds not to be eaten, along with the eagle, vulture, osprey, kite, and raven.</p><p>In Job 39:26, God questions Job: \"Doth the hawk fly by thy wisdom and stretch her wings toward the south?\" — one of a series of rhetorical questions about the mysteries of the created order that demonstrate the Creator's incomparable wisdom and Job's finitude. The hawk's migratory patterns, known and governed by God though beyond human control or planning, serve as one example among many of the vast domain of divine knowledge that undergirds the natural world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hawk", "smith": "hawk"},
        "key_refs": ["Leviticus 11:16", "Deuteronomy 14:15", "Job 39:26"]
    },
    "hay": {
        "id": "hay",
        "term": "Hay",
        "category": "concepts",
        "intro": "<p>Hay as a preserved fodder crop was not in common use among the ancient Hebrews; fresh grass and straw (<em>teben</em>) were the typical feeds for livestock. The Hebrew terms translated \"hay\" in the KJV refer primarily to fresh grass (<em>hasir</em>) or the aftermath of mowing. Proverbs 27:25 describes the agricultural cycle: \"The hay appeareth, and the tender grass sheweth itself, and herbs of the mountains are gathered\" — a picture of the spring flush of vegetation followed by harvest. Isaiah 15:6 uses withered grass as an image of desolation: \"The hay is withered away, the grass faileth, there is no green thing.\"</p><p>In the New Testament, Paul uses hay alongside wood, gold, and silver as building materials that represent different qualities of spiritual work built on the foundation of Jesus Christ (1 Corinthians 3:12). Hay and stubble are combustible materials that will be consumed by the fire of divine testing at the day of judgment, representing superficial or temporally motivated ministry in contrast to the durable work of gold, silver, and precious stones.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hay", "smith": "hay"},
        "key_refs": ["Proverbs 27:25", "Isaiah 15:6", "1 Corinthians 3:12"]
    },
    "hazael": {
        "id": "hazael",
        "term": "Hazael",
        "category": "people",
        "intro": "<p>Hazael (meaning <em>whom God beholds</em> or <em>that sees God</em>) was an officer of Ben-hadad II of Syria who became king of Damascus through assassination and subsequently became one of Israel's most formidable enemies. Elijah was commissioned by God at Horeb to anoint Hazael as king over Syria (1 Kings 19:15), and the prophet Elisha fulfilled this commission: when Hazael came to inquire of the prophet about Ben-hadad's illness, Elisha told him that Ben-hadad would recover but wept because he foresaw the devastation Hazael would inflict on Israel — burning their cities, killing their young men, dashing their infants, and ripping open their pregnant women (2 Kings 8:12). The next day Hazael smothered the bedridden king with a wet cloth and assumed the throne.</p><p>Hazael's long reign (approximately 842–796 BC) was indeed catastrophic for Israel: he defeated Jehu's forces and seized all Israelite territory east of the Jordan (2 Kings 10:32–33), reduced Israel to a remnant under Jehoahaz (2 Kings 13:3–7), threatened Jerusalem until Joash paid him tribute from the temple treasury (2 Kings 12:17–18), and reached as far as Gath. His oppression fulfilled the prophetic words of Elisha and the Deuteronomistic warnings about the consequences of covenant unfaithfulness. Amos 1:4 pronounces judgment on the house of Hazael for his atrocities.</p>",
        "hitchcock_meaning": "that sees God",
        "source_ids": {"easton": "hazael", "smith": "hazael"},
        "key_refs": ["1 Kings 19:15", "2 Kings 8:12", "2 Kings 10:32", "Amos 1:4"]
    },
    "hazar-addar": {
        "id": "hazar-addar",
        "term": "Hazar-addar",
        "category": "places",
        "intro": "<p>Hazar-addar (meaning <em>village of Addar</em>) was a place on the southern boundary of Canaan as defined in the Mosaic land grant (Numbers 34:4; Joshua 15:3). It lay in the Negev, between Kadesh-barnea and Azmon on the prescribed boundary line. The parallel passage in Joshua 15:3 divides the name into \"Hezron\" and \"Addar\" — possibly two separate waypoints that were combined into a single compound name in Numbers. The precise location has not been definitively identified, but it lay in the desert region southeast of Beersheba.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazar-addar"},
        "key_refs": ["Numbers 34:4", "Joshua 15:3"]
    },
    "hazar-enan": {
        "id": "hazar-enan",
        "term": "Hazar-enan",
        "category": "places",
        "intro": "<p>Hazar-enan (meaning <em>village of fountains</em>) was a place on the northeastern frontier of Canaan, marking the northeastern corner of the ideal land boundary described in Numbers 34:9–10. It appears again in Ezekiel's vision of restored Israel (Ezekiel 47:17; 48:1) as the northern boundary point of the land. The site has been tentatively identified with Qaryatein in the Syrian desert northeast of Damascus, or with another watered location at the edge of the settled land that would explain the name \"village of fountains.\" The exact location remains uncertain, but it consistently marks the extreme northeastern corner of the ideal Israelite territory in the biblical text.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazar-enan"},
        "key_refs": ["Numbers 34:9", "Ezekiel 47:17", "Ezekiel 48:1"]
    },
    "hazar-gaddah": {
        "id": "hazar-gaddah",
        "term": "Hazar-gaddah",
        "category": "places",
        "intro": "<p>Hazar-gaddah (meaning <em>village of fortune</em>) was a city on the southern border of Judah, listed in Joshua 15:27 among the towns of Judah in the southernmost district (the Negev). It lay in the area between Beersheba and the Edomite border — the sparse but inhabited zone of wells and seasonal pasture that marked the edge of the cultivable land. Like many of the place names in this catalogue, its precise location has not been confirmed by modern archaeology, though it likely lay in the broad Negev region south of Beersheba.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazar-gaddah"},
        "key_refs": ["Joshua 15:27"]
    },
    "hazar-hatticon": {
        "id": "hazar-hatticon",
        "term": "Hazar-hatticon",
        "category": "places",
        "intro": "<p>Hazar-hatticon (meaning <em>the village of the midway</em> or <em>middle village</em>) appears in Ezekiel 47:16 as a waypoint on the ideal northern boundary of the restored land in the prophet's eschatological vision. It is placed near Hamath in the northeastern border region, alongside Damascus and Hauran. The site has not been identified with certainty, and like several boundary markers in Ezekiel's visionary geography, it may refer to a location known to the prophet's contemporaries but now lost to history or known only by a different name.</p>",
        "hitchcock_meaning": "middle village; preparation",
        "source_ids": {"easton": "hazar-hatticon"},
        "key_refs": ["Ezekiel 47:16"]
    },
    "hazar-maveth": {
        "id": "hazar-maveth",
        "term": "Hazar-maveth",
        "category": "places",
        "intro": "<p>Hazar-maveth (meaning <em>court of death</em>) was the third son of Joktan in the table of nations (Genesis 10:26; 1 Chronicles 1:20), and the name was also applied to the region in southern Arabia that his descendants inhabited. The land of Hazar-maveth is identified with the ancient region of Hadramaut in modern Yemen — a term that preserves the biblical name in its Arabic form. The Hadramaut was one of the prosperous incense-producing regions of southern Arabia, important in the ancient spice trade that connected the Arabian peninsula with the Mediterranean world. The name's meaning — \"court of death\" — may reflect the arid and harsh nature of the desert terrain surrounding the fertile incense valleys.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazar-maveth"},
        "key_refs": ["Genesis 10:26", "1 Chronicles 1:20"]
    },
    "hazar-shual": {
        "id": "hazar-shual",
        "term": "Hazar-shual",
        "category": "places",
        "intro": "<p>Hazar-shual (meaning <em>village of the jackal</em> or <em>enclosure of the jackal</em>) was a city on the southern border of Judah (Joshua 15:28) and was also assigned to the tribe of Simeon (Joshua 19:3; 1 Chronicles 4:28), as Simeon's territory was an enclave within Judah. After the exile, it was among the places resettled by the returning Jews from Judah (Nehemiah 11:27). Jackals (<em>shu'alim</em>) were common in the semi-arid Negev and their presence around an ancient settlement would naturally give it a name. The site has been tentatively identified with Tell es-Saba near Beersheba.</p>",
        "hitchcock_meaning": "a wolf's house",
        "source_ids": {"easton": "hazar-shual"},
        "key_refs": ["Joshua 15:28", "Joshua 19:3", "Nehemiah 11:27"]
    },
    "hazar-susah": {
        "id": "hazar-susah",
        "term": "Hazar-susah",
        "category": "places",
        "intro": "<p>Hazar-susah (meaning <em>village of the horse</em> or <em>horse yard</em>) was a city in the territory of Simeon (Joshua 19:5), likely the same as Sansannah in Judah's southern territory (Joshua 15:31). It is also identified with Hazar-susim (1 Chronicles 4:31). The horse connection in the name may indicate that the site served as a stable or breeding station in the ancient period — possibly connected to Solomon's horse-trading activities in the region (2 Chronicles 1:14; 9:28). The city lay in the Negev south of Beersheba.</p>",
        "hitchcock_meaning": "or susim, the hay-paunch of a horse",
        "source_ids": {"easton": "hazar-susah"},
        "key_refs": ["Joshua 15:31", "Joshua 19:5", "1 Chronicles 4:31"]
    },
    "hazel": {
        "id": "hazel",
        "term": "Hazel",
        "category": "concepts",
        "intro": "<p>Hazel translates the Hebrew <em>luz</em> in Genesis 30:37, where Jacob peeled white stripes in rods of hazel (and poplar and almond) and placed them in the watering troughs before the flocks during their breeding season — part of his selective breeding strategy to increase his own portion of the flocks. The Hebrew <em>luz</em> refers to a nut-bearing tree; the true hazel (<em>Corylus avellana</em>) is found in Palestine, though some scholars identify <em>luz</em> with the storax tree. The name <em>luz</em> is also a placename for the ancient name of Bethel (Genesis 28:19; Judges 1:23), though the connection between the placename and the tree is uncertain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazel", "smith": "hazel"},
        "key_refs": ["Genesis 30:37"]
    },
    "hazerim": {
        "id": "hazerim",
        "term": "Hazerim",
        "category": "places",
        "intro": "<p>Hazerim (meaning <em>villages</em> or <em>enclosures</em>) appears in Deuteronomy 2:23 as the name of the temporary, unfortified settlements in which the Avvim lived in the region of southern Canaan before being displaced by the Caphtorim (Philistines) who came from Caphtor (Crete). The word <em>hazerim</em> refers to the kind of unwalled open villages — essentially semicircular encampments of tents or huts — common to the semi-nomadic peoples of the Negev and coastal plain. The passage illustrates that the Canaanite and coastal populations also underwent significant displacement before Israel's arrival, not by Israel's hand but by other migrations, situating Israel's conquest within a broader pattern of population movement in the ancient Levant.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazerim", "smith": "hazerim"},
        "key_refs": ["Deuteronomy 2:23"]
    },
    "hazeroth": {
        "id": "hazeroth",
        "term": "Hazeroth",
        "category": "places",
        "intro": "<p>Hazeroth (meaning <em>fenced enclosures</em> or <em>villages</em>) was a wilderness station of the Israelites, reached after leaving Kibroth-hattaavah, and the location where Miriam and Aaron criticized Moses for marrying a Cushite woman — and where Miriam was struck with leprosy and subsequently healed after Moses interceded for her (Numbers 11:35; 12:1–16). The site lay along the route from Sinai toward Kadesh-barnea in the Sinai peninsula. After the healing of Miriam, the congregation departed from Hazeroth and camped in the wilderness of Paran. Hazeroth has been tentatively identified with 'Ain Khadra in the northeastern Sinai.</p>",
        "hitchcock_meaning": "villages; palaces",
        "source_ids": {"easton": "hazeroth", "smith": "hazeroth"},
        "key_refs": ["Numbers 11:35", "Numbers 12:1", "Numbers 33:17", "Numbers 33:18"]
    },
    "hazezon-tamar": {
        "id": "hazezon-tamar",
        "term": "Hazezon-tamar",
        "category": "places",
        "intro": "<p>Hazezon-tamar (meaning <em>pruning of the palm</em> or <em>drawing near to bitterness</em>) was the original name of the city later called En-gedi, located on the western shore of the Dead Sea in the wilderness of Judah. It appears in Genesis 14:7 as the place where the eastern coalition kings (led by Chedorlaomer) defeated the Amorites, and in 2 Chronicles 20:2 Jehoshaphat is warned that a vast army has come from beyond the Dead Sea \"even from Hazazon-tamar, which is En-gedi.\" En-gedi, famous for its oasis spring and as David's refuge from Saul (1 Samuel 23:29; 24:1), was one of the most important locations in the Judean wilderness.</p>",
        "hitchcock_meaning": "drawing near to bitterness",
        "source_ids": {"easton": "hazezon-tamar"},
        "key_refs": ["Genesis 14:7", "2 Chronicles 20:2"]
    },
    "hazo": {
        "id": "hazo",
        "term": "Hazo",
        "category": "people",
        "intro": "<p>Hazo (meaning <em>vision</em> or <em>seeing</em>) was one of the twelve sons of Nahor, Abraham's brother, born to him by his concubine Reumah (Genesis 22:22). The twelve sons of Nahor listed in Genesis 22:20–24 are presented as the ancestors of the Aramean peoples who inhabited the region of Paddan-aram and northern Mesopotamia. Hazo represents one of these Aramean tribal groups, though the specific territory or tribe his name designated has not been positively identified. The genealogy's purpose is to trace the kinship between Abraham's family and the broader Semitic population of the Fertile Crescent.</p>",
        "hitchcock_meaning": "seeing; prophesying",
        "source_ids": {"easton": "hazo", "smith": "hazo"},
        "key_refs": ["Genesis 22:22"]
    },
    "hazor": {
        "id": "hazor",
        "term": "Hazor",
        "category": "places",
        "intro": "<p>Hazor (meaning <em>enclosed</em> or <em>fortified</em>) was the greatest Canaanite city in northern Palestine during the Late Bronze Age and the dominant power in the Galilee region. Joshua 11:1 records that Jabin king of Hazor rallied the northern coalition of Canaanite kings against Israel, assembling a force \"with horses and chariots very many\" at the waters of Merom. Joshua defeated them, pursued them, and burned Hazor — described as \"the head of all those kingdoms\" (Joshua 11:10). Archaeological excavations at Tell el-Qedah (Tell Hazor) in upper Galilee have confirmed a massive Bronze Age city of some 200 acres (one of the largest in Canaan) that shows evidence of violent destruction in the Late Bronze Age.</p><p>A second king Jabin of Hazor appears in the era of the judges (Judges 4:2), whose commander Sisera was defeated by Deborah and Barak and killed by Jael. Solomon rebuilt Hazor as one of his chariot cities along with Megiddo and Gezer (1 Kings 9:15). The Assyrian king Tiglath-pileser III captured Hazor during the campaign against Pekah king of Israel (2 Kings 15:29). Several other places named Hazor appear in the south of Judah (Joshua 15:23–25; Nehemiah 11:33), and Jeremiah 49:28–33 contains an oracle against the semi-nomadic peoples of Hazor in Arabia.</p>",
        "hitchcock_meaning": "court; hay",
        "source_ids": {"easton": "hazor", "smith": "hazor"},
        "key_refs": ["Joshua 11:1", "Joshua 11:10", "Judges 4:2", "1 Kings 9:15"]
    },
    "hazor-hadattah": {
        "id": "hazor-hadattah",
        "term": "Hazor-hadattah",
        "category": "places",
        "intro": "<p>Hazor-hadattah (meaning <em>new Hazor</em>, from the Aramaic <em>hadattah</em> meaning \"new\") was a city in the southernmost district of Judah listed in Joshua 15:25 among the towns near Kedesh in the Negev. The designation \"new\" distinguishes it from other Hazors, suggesting it was a more recently established settlement or refounded city in the series of desert towns that marked the southern border of Judah's tribal territory. Its precise location has not been identified by modern archaeology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hazor-hadattah"},
        "key_refs": ["Joshua 15:25"]
    },
    "he-ass": {
        "id": "he-ass",
        "term": "He-ass",
        "category": "concepts",
        "intro": "<p>The he-ass or male donkey (Hebrew <em>hamor</em>) was one of the most commonly domesticated animals of the ancient Near East and appears frequently throughout the Old Testament as a beast of burden, a marker of wealth, and an animal of both agricultural and ceremonial significance. Abraham, Jacob, and Job all counted asses among their substantial livestock holdings (Genesis 12:16; 32:5; Job 1:3). The Mosaic law regulated the treatment of the ass with notable care: the ox and ass were not to be yoked together (Deuteronomy 22:10), the lost ass of an enemy was to be returned (Exodus 23:4–5), and the ass that had fallen under its burden was to be helped up (Deuteronomy 22:4).</p><p>Theologically, the ass appears in two pivotal passages: Balaam's donkey that saw the angel of the LORD and spoke (Numbers 22:22–35), and the triumphant entry of Jesus into Jerusalem riding on a donkey's colt (Matthew 21:1–7; Zechariah 9:9) — an act of deliberate messianic symbolism presenting the king who comes humbly, not on a war horse but on a beast of peace. The ass thus spans the biblical narrative from the patriarchs to the Messiah's entry into his capital.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "he-ass"},
        "key_refs": ["Genesis 12:16", "Numbers 22:28", "Zechariah 9:9", "Matthew 21:5"]
    },
    "head-bands": {
        "id": "head-bands",
        "term": "Head-bands",
        "category": "concepts",
        "intro": "<p>Head-bands (Hebrew <em>kishshurim</em>) are mentioned in Isaiah 3:20 and Jeremiah 2:32 as feminine ornaments. Despite the English translation, the Hebrew term appears to refer more accurately to girdles or belts for the waist rather than bands for the head — the KJV translation of \"head-bands\" may reflect an incorrect derivation. Isaiah 3:18–23 catalogs an extensive list of feminine adornments that God will strip from the proud daughters of Zion in judgment, including anklets, headbands, crescents, pendants, armlets, sashes, perfume boxes, amulets, signet rings, nose rings, festal robes, mantles, cloaks, and handbags. The catalog's purpose is not to condemn feminine adornment per se but to show how deeply the women of Jerusalem had invested their identity and hope in material luxury rather than covenant faithfulness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "head-bands"},
        "key_refs": ["Isaiah 3:20", "Jeremiah 2:32"]
    },
    "head-dress": {
        "id": "head-dress",
        "term": "Head-dress",
        "category": "concepts",
        "intro": "<p>Head coverings and ornamental headdresses appear in Scripture from priestly vestments to royal turbans to the everyday coverings of Israelite men and women. The priests were commanded to wear linen <em>migba'oth</em> (caps or turbans, Exodus 28:40) as part of their sacred vestments for ministering at the tabernacle. The high priest wore a linen turban (<em>mitznefet</em>) with the golden plate bearing the inscription \"Holy to the LORD\" (Exodus 28:36–38). Job 29:14 describes the turban of justice as part of his righteousness metaphor, and Isaiah 3:23 includes festive turbans among the ornaments of Jerusalem's women.</p><p>The head-dress could also be a sign of mourning when removed or disheveled: Ezekiel 24:17 forbids the prophet from putting on his head-dress or removing his shoes as part of the sign-act marking the death of his wife and the coming fall of Jerusalem. Isaiah 61:3 promises \"a beautiful headdress instead of ashes\" as part of the eschatological restoration — the turban replacing the ash-covered head of mourning. In the New Testament, Paul's instruction about head coverings in 1 Corinthians 11:2–16 addresses the proper head covering in worship, with the symbolic logic drawn from the creation order.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "head-dress"},
        "key_refs": ["Exodus 28:40", "Job 29:14", "Isaiah 61:3", "1 Corinthians 11:4"]
    },
    "heap": {
        "id": "heap",
        "term": "Heap",
        "category": "concepts",
        "intro": "<p>Heap (<em>tel</em> in Hebrew) referred to a mound of ruins — a destroyed city reduced to rubble and left as a permanent monument to judgment. When Joshua burned Ai, he reduced it to a heap of ruins forever (Joshua 8:28), and Jeremiah later used the same term (<em>tel</em>) as a figure for irreversible judgment: \"And I will make Jerusalem heaps\" (Jeremiah 9:11; 26:18; Micah 3:12). The Palestinian landscape was dotted with such <em>tells</em> — mounds formed by successive layers of occupation and destruction — and the biblical writers were well aware of their meaning as testament to the fate of cities that fell before conquering armies or divine judgment.</p><p>Heaps of stones also marked covenants and boundaries: the heap of witness between Jacob and Laban (Genesis 31:46–52, called Galeed in Hebrew and Jegar-sahadutha in Aramaic) was a memorial cairn. Stones heaped over the bodies of Achan (Joshua 7:26) and Absalom (2 Samuel 18:17) marked sites of judgment. Proverbs 25:22 and Romans 12:20 use the image of heaping coals of fire on an enemy's head as a picture of overcoming evil with good.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "heap"},
        "key_refs": ["Joshua 8:28", "Jeremiah 9:11", "Genesis 31:46", "Romans 12:20"]
    },
    "heart": {
        "id": "heart",
        "term": "Heart",
        "category": "concepts",
        "intro": "<p>In biblical anthropology, the heart (<em>lev</em> or <em>levav</em> in Hebrew; <em>kardia</em> in Greek) is the central organ of the inner life — encompassing not merely emotion (as in modern usage) but the totality of a person's intellect, will, conscience, and moral character. The heart is the seat of understanding (1 Kings 3:9; Proverbs 14:33), of plans and intentions (Proverbs 16:9; Matthew 9:4), of faith (Romans 10:10), of worship (Deuteronomy 6:5), and of moral character (Matthew 5:8; 15:19). The great commandment calls for love of God with the whole heart (Deuteronomy 6:5; Matthew 22:37), establishing the heart as the organ of covenant relationship.</p><p>Scripture consistently presents the unregenerate heart as corrupt and self-deceived: \"The heart is deceitful above all things, and desperately wicked; who can know it?\" (Jeremiah 17:9). The prophets announced that the new covenant would involve a transformation of the heart itself — the law written on the heart rather than on stone tablets (Jeremiah 31:33; Ezekiel 36:26–27), replacing the \"heart of stone\" with a \"heart of flesh\" by the Spirit of God. The New Testament presents this as accomplished in regeneration: believers are sealed by the Spirit in their hearts (2 Corinthians 1:22; Ephesians 1:13–14), and the peace of God guards the heart (Philippians 4:7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "heart"},
        "key_refs": ["Deuteronomy 6:5", "Jeremiah 17:9", "Jeremiah 31:33", "Ezekiel 36:26"]
    },
    "hearth": {
        "id": "hearth",
        "term": "Hearth",
        "category": "concepts",
        "intro": "<p>Hearth in the Old Testament translates several Hebrew terms for cooking and heating fires in household and palace settings. In Jeremiah 36:22–23, the Hebrew <em>ah</em> describes the large brazier or fire pot burning in the king's winter house — into which Jehoiakim cut and burned the scroll of Jeremiah's prophecies column by column as it was read to him, a gesture of defiant rejection of God's word. Zechariah 12:6 uses the hearth as a figure for Jerusalem's military power in the last days: \"In that day will I make the governors of Judah like an hearth of fire among the wood.\" Psalm 102:3 uses \"hearth\" (burning brand) for the consuming nature of divine affliction: \"My bones are burned as an hearth.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hearth", "smith": "hearth"},
        "key_refs": ["Jeremiah 36:22", "Zechariah 12:6", "Psalms 102:3"]
    },
    "heath": {
        "id": "heath",
        "term": "Heath",
        "category": "concepts",
        "intro": "<p>Heath translates the Hebrew <em>'arar</em> in Jeremiah 17:6 and 48:6, where it denotes a stunted, desolate desert shrub — likely the juniper known in Arabic as <em>'arâr</em> (<em>Juniperus phoenicea</em>) or possibly the tamarisk or another low desert plant. Jeremiah 17:6 uses it as an image of spiritual desolation: \"He shall be like the heath in the desert, and shall not see when good cometh.\" The heath growing in parched desert conditions — unable to benefit from rain when it falls because it is planted in salt land — pictures the person who trusts in man rather than God, whose inner spiritual life remains barren even when providential circumstances improve. The parallel verse (Jeremiah 17:8) contrasts this with the person who trusts in the LORD, described as a tree planted by the water.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "heath", "smith": "heath"},
        "key_refs": ["Jeremiah 17:6", "Jeremiah 48:6"]
    },
    "heathen": {
        "id": "heathen",
        "term": "Heathen",
        "category": "concepts",
        "intro": "<p>Heathen (Hebrew plural <em>goyim</em>) originally designated \"nations\" or \"peoples\" in a general sense — all the peoples of the earth, including Israel (Genesis 12:2; 18:18). Over the course of Israel's history, the term became more specifically applied to the non-Israelite nations who did not worship the LORD, and carried connotations of idolatry, moral impurity, and separation from the covenant. The Mosaic law repeatedly warns Israel not to walk in the statutes of the heathen (Leviticus 20:23; 26:14), and the prophets condemned Israel when they adopted heathen practices.</p><p>The Old Testament's ultimate vision, however, was not the permanent exclusion of the heathen but their inclusion in God's covenant purposes: Abraham was to be a father of many nations, and \"in thee shall all nations (<em>goyim</em>) be blessed\" (Genesis 12:3; 18:18; Galatians 3:8). The prophets looked forward to a day when the heathen nations would stream to Zion (Isaiah 2:2–4; Micah 4:1–3) and worship the God of Israel. Paul quotes these passages extensively in Romans 15 to ground his mission to the Gentiles in the purposes of God declared in the Old Testament, and Peter's vision in Acts 10 dramatically demonstrated that the heathen were not to be called \"unclean\" any longer (Acts 10:28).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "heathen", "smith": "heathen"},
        "key_refs": ["Genesis 18:18", "Leviticus 20:23", "Isaiah 2:2", "Acts 10:28"]
    },
    "heave-offering": {
        "id": "heave-offering",
        "term": "Heave Offering",
        "category": "concepts",
        "intro": "<p>The heave offering (Hebrew <em>terumah</em>, from a root meaning \"to lift up\") was a sacrificial category in the Mosaic system designating an offering lifted or raised before the LORD as a formal act of presentation. Exodus 29:27 applies the term to portions of the ordination offerings of Aaron's installation. Leviticus 7:34 assigns the breast of the wave offering and the thigh of the heave offering to the priests as their perpetual portion. Numbers 6:20 includes a heave offering in the Nazirite's concluding ceremony, and Numbers 15:20 commands a heave offering of the first dough of each batch of bread baked at home — bringing the everyday domestic act of bread-making into the orbit of sacred offering.</p><p>Modern translations typically render <em>terumah</em> as \"contribution,\" \"gift,\" or \"offering\" rather than \"heave offering,\" since the older understanding of a vertical lifting gesture may be less accurate than a general sense of a portion \"set apart\" or \"lifted off\" for God. The principle behind the terumah was the recognition that all produce belonged first to God, and the offering of a portion consecrated the whole — a theology Paul echoes in Romans 11:16: \"If the firstfruit is holy, so is the lump.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "heave-offering"},
        "key_refs": ["Exodus 29:27", "Leviticus 7:34", "Numbers 15:20", "Romans 11:16"]
    },
    "heaven": {
        "id": "heaven",
        "term": "Heaven",
        "category": "concepts",
        "intro": "<p>Heaven in Scripture encompasses a cluster of related but distinct concepts that must be distinguished by context. In its primary cosmological sense, \"heaven and earth\" (Genesis 1:1) denotes the totality of creation — the visible universe and everything in it. The \"heaven\" of the sky and weather (Genesis 1:8; Matthew 16:2–3) is the atmosphere and starry expanse. The \"heaven of heavens\" (Deuteronomy 10:14; 1 Kings 8:27; Nehemiah 9:6) is the highest realm of God's throne — transcending even the created cosmos, so that even the heaven of heavens cannot contain God. Paul's reference to a man \"caught up to the third heaven\" (2 Corinthians 12:2) likely reflects a Jewish cosmological scheme of layered heavens.</p><p>Theologically, heaven is the dwelling place of God (Isaiah 66:1; Matthew 6:9), the realm of the angelic hosts (Matthew 22:30; Hebrews 12:22), and the destination of the redeemed (John 14:2–3; 2 Corinthians 5:1; Revelation 21:1–4). The New Testament presents the kingdom of heaven as both present reality (Matthew 12:28; Luke 17:21) and future consummation (Matthew 25:34; Revelation 11:15). The new creation of Revelation 21 is described as a \"new heaven and a new earth\" — not the abolition of the material creation but its transformation and renewal under the complete and unmediated presence of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "heaven", "smith": "heaven"},
        "key_refs": ["Genesis 1:1", "Deuteronomy 10:14", "2 Corinthians 12:2", "Revelation 21:1"]
    },
    "heber": {
        "id": "heber",
        "term": "Heber",
        "category": "people",
        "intro": "<p>Heber (meaning <em>passing over</em> or <em>a companion</em>) is the name of several individuals in the Old Testament. The most narratively significant is Heber the Kenite, the husband of Jael (Judges 4:11, 17–22). Heber had separated himself from the main body of the Kenites and pitched his tent near Kedesh in Naphtali, in a position of apparent neutrality or alliance with the Canaanites — his tent was near the oak of Zaanannim, and there was peace between King Jabin of Hazor and the house of Heber. When Sisera, the defeated Canaanite commander, fled to Heber's tent seeking refuge, his wife Jael killed him by driving a tent peg through his temple while he slept, fulfilling Deborah's prophecy that Sisera would be delivered into the hand of a woman (Judges 4:9; 5:24–27).</p><p>Other men named Heber include: (1) the son of Beriah and grandson of Asher, from whom the Heberites descended (Genesis 46:17; Numbers 26:45); (2) a son of Ezrah in the Judahite genealogy (1 Chronicles 4:18); (3) a Benjaminite (1 Chronicles 8:17); and (4) a chief of the Gadites (1 Chronicles 5:13).</p>",
        "hitchcock_meaning": "one that passes; anger",
        "source_ids": {"easton": "heber", "smith": "heber"},
        "key_refs": ["Judges 4:11", "Judges 4:17", "Judges 5:24", "Genesis 46:17"]
    },
    "hebrew": {
        "id": "hebrew",
        "term": "Hebrew",
        "category": "concepts",
        "intro": "<p>Hebrew as an ethnic and linguistic designation applies to the Israelites, though its origins and usage are more complex than a simple synonym for \"Israelite.\" In the Old Testament, \"Hebrew\" (<em>ibri</em>) is typically used when an Israelite speaks to or is described by a non-Israelite (Genesis 39:14; 41:12; Exodus 1:19), or when an Israelite identifies himself to a foreigner (Genesis 40:15; Jonah 1:9), suggesting it was the outsider's term for the people — or a term of self-identification in cross-cultural contexts. The derivation is traditionally traced to Eber (Genesis 10:24; 11:14–17), the ancestor through whom the line of Abraham descended, making \"Hebrew\" an ethnic designation for the children of Eber.</p><p>In the New Testament, Paul identifies himself as \"a Hebrew of the Hebrews\" (Philippians 3:5; 2 Corinthians 11:22) — a pure-blooded member of the Hebrew-speaking Jewish community, not a diaspora Jew who had adopted Greek as his primary language. Acts 6:1 distinguishes \"Hellenists\" (Greek-speaking Jewish Christians) from \"Hebrews\" (Aramaic-speaking Jewish Christians) in the early Jerusalem church. The \"Hebrew tongue\" mentioned in Acts 21:40, 22:2 and Revelation 9:11; 16:16 refers to the Aramaic spoken by Palestinian Jews in the first century, though Hebrew proper remained the language of synagogue reading and religious scholarship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hebrew", "smith": "hebrew"},
        "key_refs": ["Genesis 39:14", "Philippians 3:5", "Acts 6:1"]
    },
    "hebrew-language": {
        "id": "hebrew-language",
        "term": "Hebrew Language",
        "category": "concepts",
        "intro": "<p>Hebrew is a Semitic language belonging to the Canaanite branch of the Northwest Semitic family, closely related to Phoenician and ancient Ugaritic. It was the primary language in which the Old Testament was written (with portions of Daniel and Ezra in Aramaic) and the native tongue of the Israelite nation from the patriarchal period through the exile. The language is sometimes called \"the language of Canaan\" (Isaiah 19:18) or \"the Jews' language\" (2 Kings 18:26, 28; Isaiah 36:11), and in later Jewish tradition simply \"the holy tongue\" (<em>leshon ha-qodesh</em>).</p><p>The Assyrian Rabshakeh's demand to speak to Jerusalem's leaders \"in the Syrian language\" rather than Hebrew (2 Kings 18:26; Isaiah 36:11) was a deliberate attempt to undermine morale by letting the common people hear the terms of surrender — the very threat the officials sought to prevent by requesting the diplomatic Aramaic. After the exile, Aramaic became the vernacular of Palestinian Jews, and Nehemiah 13:24 records that children of mixed marriages could not speak \"in the Jews' language\" — a sign of cultural assimilation that Nehemiah vigorously resisted. In the New Testament period, Hebrew proper coexisted with vernacular Aramaic and Greek in a complex linguistic environment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hebrew-language", "smith": "hebrew-language"},
        "key_refs": ["2 Kings 18:26", "Isaiah 36:11", "Nehemiah 13:24"]
    },
    "hebrew-of-the-hebrews": {
        "id": "hebrew-of-the-hebrews",
        "term": "Hebrew of the Hebrews",
        "category": "concepts",
        "intro": "<p>\"Hebrew of the Hebrews\" is Paul's self-designation in Philippians 3:5 as part of his catalog of Jewish credentials — everything he once counted as gain before counting it loss for Christ. The phrase denotes that Paul was not merely an Israelite by religion but a pure-blooded, Aramaic-speaking Jew from a family that had maintained Hebrew identity without assimilation into Greek culture. Both his parents were Hebrews, making him a \"Hebrew of the Hebrews\" — a superlative form emphasizing racial and cultural purity as distinct from a diaspora Jew who might speak Greek as a first language and have adopted Hellenistic customs.</p><p>The parallel phrase in 2 Corinthians 11:22 — \"Are they Hebrews? So am I. Are they Israelites? So am I. Are they the seed of Abraham? So am I\" — shows Paul defending his Jewish credentials against \"super-apostles\" who questioned his apostolic standing. The triple assertion covers ethnic lineage (Hebrews), national covenant identity (Israelites), and physical descent (Abraham's seed). Paul's willingness to count all of this as \"dung\" for the surpassing worth of knowing Christ (Philippians 3:8) makes the catalog a measure of what he surrendered, not a claim to superiority.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hebrew-of-the-hebrews"},
        "key_refs": ["Philippians 3:5", "2 Corinthians 11:22"]
    },
    "hebrews": {
        "id": "hebrews",
        "term": "Hebrews",
        "category": "concepts",
        "intro": "<p>In the New Testament, \"Hebrews\" (Acts 6:1; 2 Corinthians 11:22; Philippians 3:5) refers specifically to the Aramaic-speaking Jewish Christians or Jews of Palestine, as distinguished from the \"Hellenists\" — Greek-speaking Jews of the diaspora. The first major internal tension in the Jerusalem church arose between these two groups: the Hellenists complained that their widows were being neglected in the daily distribution of food compared with the widows of the Hebrews (Acts 6:1). The apostles resolved this by appointing seven deacons — all of whom have Greek names, suggesting they were drawn from the Hellenist community to address the Hellenist complaint.</p><p>\"Hebrews\" as a broader designation for the Israelite people appears throughout the Old Testament and is used by Paul to describe his own identity (Philippians 3:5; 2 Corinthians 11:22). The Epistle to the Hebrews takes its name from its primary audience — Jewish Christians who were in danger of apostasy back to Judaism — and engages extensively with the Levitical priesthood, sacrificial system, and Mosaic covenant to demonstrate the superiority and finality of Christ's high priesthood and atoning work.</p>",
        "hitchcock_meaning": "descendants of Heber",
        "source_ids": {"easton": "hebrews"},
        "key_refs": ["Acts 6:1", "Philippians 3:5", "2 Corinthians 11:22"]
    },
    "hebrews-epistle-to": {
        "id": "hebrews-epistle-to",
        "term": "Hebrews, Epistle to",
        "category": "concepts",
        "intro": "<p>The Epistle to the Hebrews is a sustained theological argument addressed to Jewish Christians — likely in Rome or possibly Jerusalem — who were in danger of abandoning their faith and returning to the Judaism from which they had come, possibly under the pressure of persecution. The letter argues comprehensively for the supremacy and finality of Christ: he is greater than the angels (chapters 1–2), greater than Moses (3–4), greater than the Levitical priesthood of Aaron (5–10), presenting himself as the eternal High Priest after the order of Melchizedek who has offered the once-for-all sacrifice that the entire Levitical system had only anticipated in shadow and type. The argument is punctuated by five solemn warnings against apostasy (2:1–4; 3:7–4:13; 5:11–6:12; 10:26–39; 12:14–29).</p><p>The question of authorship has been debated since antiquity: Paul, Barnabas, Apollos, Priscilla, and Luke have all been proposed. Origen's famous dictum stands: \"Who wrote the epistle, only God truly knows.\" The letter lacks a standard Pauline opening but shares Pauline theological vocabulary. Hebrews 13:19, 24 suggests the author planned to visit the recipients and had associates in common with them — possibly placing the author in Paul's circle. Its canonical status was disputed in the Western church for centuries but was ultimately accepted as authoritative. Its rich Christology and its theology of the new covenant fulfill the old (chapters 8–10) have made it a foundational text in Christian understanding of how the two Testaments relate.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hebrews-epistle-to"},
        "key_refs": ["Hebrews 1:1", "Hebrews 4:14", "Hebrews 10:12", "Hebrews 13:19"]
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
