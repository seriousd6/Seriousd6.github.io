"""
BP Article Synthesis — c2: Centurion → Chub
Covers Easton entries: Centurion through Chub (75 entries)

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

Script: scripts/bp-c2.py
Run: python3 scripts/bp-c2.py
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
    "centurion": {
        "id": "centurion",
        "term": "Centurion",
        "category": "concepts",
        "intro": "<p>A centurion was a Roman military officer commanding a unit of approximately one hundred soldiers — a basic tactical subdivision of a Roman legion. Centurions appear with notable frequency in the New Testament, and consistently in a favorable light: the centurion at Capernaum whose faith in Christ's authoritative word astonished Jesus (Matt. 8:5–13); the centurion at the cross who confessed <em>Truly this was the Son of God</em> upon witnessing the manner of Jesus's death (Mark 15:39); and Cornelius of the Italian cohort at Caesarea, described as a devout, God-fearing man whose prayers and alms were heard by God, and who became the first named Gentile to receive the Holy Spirit and Christian baptism (Acts 10:1–48).</p><p>Julius, a centurion of the Augustan cohort, treated Paul with courtesy during the voyage to Rome, saving his life at the shipwreck (Acts 27:1–3, 43). The centurion charged with Paul's custody allowed him to visit friends at Sidon. The consistent dignity with which centurions are portrayed in the Gospels and Acts reflects their role as the backbone of Roman military order, and the early church's openness to Gentile soldiers of good character.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "centurion", "smith": "centurion", "isbe": "centurion"},
        "key_refs": ["Mark 15:39", "Mark 15:44", "Mark 15:45", "Acts 10:1", "Acts 10:22"],
        "sections": []
    },
    "cephas": {
        "id": "cephas",
        "term": "Cephas",
        "category": "people",
        "intro": "<p>Cephas is the Aramaic name meaning <em>a rock or stone</em>, given by Jesus to Simon the son of Jonas at the time of their first meeting (John 1:42). Its Greek equivalent is Petros (Peter), the name by which Simon is almost universally known in the Gospels. Paul employs the Aramaic form Cephas consistently in his letters (Gal. 1:18; 2:9, 11, 14; 1 Cor. 1:12; 3:22; 9:5; 15:5), possibly reflecting the name by which Peter was known in Palestinian Jewish Christian circles. The name's conferral by Jesus at the outset of his ministry is understood as prophetic, anticipating the foundational role Simon would occupy in the early church.</p>",
        "hitchcock_meaning": "a rock or stone",
        "source_ids": {"easton": "cephas", "smith": "cephas", "isbe": "cephas"},
        "key_refs": ["John 1:42"],
        "sections": []
    },
    "cesarea": {
        "id": "cesarea",
        "term": "Cesarea",
        "category": "places",
        "intro": "<p>Cesarea is an alternate spelling of Caesarea, which in the New Testament refers primarily to Caesarea Maritima — the great port city on the Mediterranean coast of Palestine built by Herod the Great and named in honor of Caesar Augustus. It served as the administrative capital of the Roman province of Judaea and appears frequently in Acts: as the home of Cornelius the centurion (Acts 10), the base of Philip the evangelist (Acts 8:40; 21:8), and the site of Paul's imprisonments and trials before Felix, Festus, and Agrippa (Acts 23–26) before his voyage to Rome. A second city, Caesarea Philippi, lay at the headwaters of the Jordan and is the site where Peter's great confession was made (Matt. 16:13–16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cesarea"},
        "key_refs": [],
        "sections": []
    },
    "chaff": {
        "id": "chaff",
        "term": "Chaff",
        "category": "concepts",
        "intro": "<p>Chaff is the light husk separated from grain during the process of winnowing, when threshed grain is tossed into the air and the wind carries away the worthless material while the heavier kernels fall to the threshing floor. In biblical imagery, chaff became a pervasive symbol of what is worthless, ephemeral, and subject to divine judgment. The Psalms contrast the wicked — who are <em>like chaff that the wind drives away</em> (Ps. 1:4) — with the righteous, who are like firmly rooted trees. Isaiah employs the image for enemies consumed by divine fire (Isa. 5:24; 33:11), as does Hosea and Zephaniah for Israel's apostasy.</p><p>In the New Testament, John the Baptist's description of the coming one's ministry culminates in the image of the winnowing fork: <em>His winnowing fork is in his hand, and he will clear his threshing floor and gather his wheat into the barn, but the chaff he will burn with unquenchable fire</em> (Matt. 3:12). The metaphor frames the final judgment as a separation already inherent in the harvest process.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chaff", "smith": "chaff", "isbe": "chaff"},
        "key_refs": ["Exodus 15:7", "Isaiah 5:24", "Matthew 3:12", "Isaiah 33:11", "Psalms 1:4"],
        "sections": []
    },
    "chain": {
        "id": "chain",
        "term": "Chain",
        "category": "concepts",
        "intro": "<p>Chains in the Old Testament served both ornamental and punitive purposes. As insignia of honor, a gold chain placed around the neck signified high office: Pharaoh invested Joseph with such a chain as a mark of authority (Gen. 41:42), and Daniel received one from Belshazzar (Dan. 5:29). Decorative chains of gold adorned the temple pillars and the priestly breastplate (Exod. 39:17–21). Proverbs uses the image of a chain for the parental instruction and wisdom that adorn the recipient like a garland (Prov. 1:9).</p><p>In prophetic and apocalyptic literature, chains represent captivity and divine judgment (Ezek. 16:11; Lam. 3:7). In the New Testament, literal chains bind Paul in his Roman imprisonments (Acts 28:20; Eph. 6:20), while Jude and 2 Peter describe demonic beings held in chains of darkness awaiting judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chain", "smith": "chain"},
        "key_refs": ["Genesis 41:42", "Ezekiel 16:11", "Exodus 39:17", "Exodus 39:21", "Proverbs 1:9"],
        "sections": []
    },
    "chalcedony": {
        "id": "chalcedony",
        "term": "Chalcedony",
        "category": "concepts",
        "intro": "<p>Chalcedony (Greek <em>chalkêdôn</em>) appears in Scripture only in Revelation 21:19 as the third stone in the twelve foundations of the wall of the New Jerusalem. The name derives from the ancient city of Chalcedon on the Bosphorus. In modern mineralogy chalcedony refers to a microcrystalline form of quartz that comes in many varieties — including agate, carnelian, and jasper — but the ancient term is of uncertain application; John's intended stone may have been a blue or sky-blue variety, an emerald-green stone, or copper ore. Some identify it with the modern turquoise. The stone appears among those associated with the breastplate of the high priest in Ezekiel 28:13 (in forms rendered differently in ancient versions).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chalcedony", "smith": "chalcedony", "isbe": "chalcedony"},
        "key_refs": ["Revelation 21:19"],
        "sections": []
    },
    "chaldea": {
        "id": "chaldea",
        "term": "Chaldea",
        "category": "places",
        "intro": "<p>Chaldea (or Chaldaea) was the southern portion of Babylonia, comprising the alluvial plain of Lower Mesopotamia lying chiefly between the Euphrates and Tigris rivers as they approached the Persian Gulf. In the Old Testament it is sometimes used synonymously with Babylonia as a whole, particularly by the prophets, though strictly it designated the homeland of the Chaldean people who eventually rose to dominate the entire Babylonian empire under the Neo-Babylonian dynasty of Nabopolassar and Nebuchadnezzar (626–539 BC).</p><p>Ur of the Chaldees, the birthplace of Abraham (Gen. 11:28, 31; 15:7; Neh. 9:7), lay in this southern region, making Chaldea the geographic origin of Israel's covenant ancestor. The prophets Jeremiah and Ezekiel extensively describe Chaldea in their oracles against Babylon (Jer. 50–51; Ezek. 23), and Isaiah's oracles against Babylon (Isa. 13–14; 47) use Chaldea as virtually synonymous with the ruling world empire. Daniel ministered in the Chaldean royal court throughout the Babylonian period.</p>",
        "hitchcock_meaning": "as demons, or as robbers",
        "source_ids": {"easton": "chaldea", "smith": "chaldea"},
        "key_refs": ["Jeremiah 50:10", "Jeremiah 51:24", "Jeremiah 51:35", "Genesis 14:1"],
        "sections": []
    },
    "chaldee-language": {
        "id": "chaldee-language",
        "term": "Chaldee Language",
        "category": "concepts",
        "intro": "<p>The Chaldee (or Aramaic) language is the term historically applied to the biblical portions written in Aramaic rather than Hebrew. These include Daniel 2:4b–7:28 and Ezra 4:8–6:18 and 7:12–26, along with a single verse in Jeremiah (10:11) and two words in Genesis 31:47. The designation <em>Chaldee</em> reflects the historical association of Aramaic with the Babylonian court, where it functioned as the diplomatic and administrative lingua franca of the ancient Near East from the seventh century BC onward. Modern scholarship prefers the term <em>Biblical Aramaic</em>. Its presence in the Hebrew Bible documents Israel's contact with the dominant international language of the exile period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chaldee-language"},
        "key_refs": ["Daniel 2:4", "Daniel 2:28", "Ezra 4:8", "Genesis 31:46", "Jeremiah 10:11"],
        "sections": []
    },
    "chaldees": {
        "id": "chaldees",
        "term": "Chaldees",
        "category": "concepts",
        "intro": "<p>The Chaldees (or Chaldeans) were the inhabitants of Chaldea, the southern region of Babylonia. They rose from tribal origins in lower Mesopotamia to dominate the entire Babylonian empire under Nabopolassar and Nebuchadnezzar II, establishing the Neo-Babylonian empire (626–539 BC) that destroyed Jerusalem and carried Judah into exile. In the Old Testament they serve as the primary agent of God's judgment on apostate Judah (2 Kgs. 25; Jer. 39; Ezek. 23). In the book of Daniel, <em>Chaldeans</em> is also used as a professional title for the class of astrologers, magicians, and diviners in the royal court (Dan. 2:2, 4, 5, 10), who may have been a guild descended from or associated with Chaldean priestly tradition.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chaldees"},
        "key_refs": ["2 Kings 25", "Isaiah 13:19", "Isaiah 23:13"],
        "sections": []
    },
    "chamber": {
        "id": "chamber",
        "term": "Chamber",
        "category": "concepts",
        "intro": "<p>Chamber in biblical usage refers to any enclosed room within a house, palace, or temple complex. The Shunammite woman's preparation of a small chamber on the wall of her house for Elisha — furnished with a bed, table, chair, and lamp — illustrates the private guest accommodation of the period (2 Kgs. 4:10). The <em>upper chamber</em> or <em>upper room</em> (Greek <em>anagaion</em>) is the setting for the Last Supper (Mark 14:14–15; Luke 22:11–12) and for the assembly of disciples at Pentecost (Acts 1:13; 2:1). Royal palaces contained numerous specialized chambers for private audiences, guard duty, and storage (1 Kgs. 22:25; 2 Kgs. 9:2). The temple included side chambers (1 Kgs. 6:5–10) and treasury rooms, as well as the inner chambers associated with the priests' service (Ezek. 40–42).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chamber", "smith": "chamber", "isbe": "chamber"},
        "key_refs": ["2 Kings 4:10", "Mark 14:14", "1 Kings 22:25", "2 Kings 9:2", "Isaiah 26:20"],
        "sections": []
    },
    "chambering": {
        "id": "chambering",
        "term": "Chambering",
        "category": "concepts",
        "intro": "<p>Chambering appears in the Authorized Version of Romans 13:13 as the rendering of the Greek <em>koitais</em> (literally <em>beds</em>), referring to sexual immorality and illicit behavior. Paul urges believers to conduct themselves as in the daytime — <em>not in carousing and drunkenness, not in sexual immorality and sensuality, not in quarreling and jealousy</em>. The term denotes the licentiousness associated with the banquet and bedroom culture of Hellenistic Rome, against which early Christian ethical teaching consistently stood.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chambering", "isbe": "chambering"},
        "key_refs": ["Romans 13:13"],
        "sections": []
    },
    "chamberlain": {
        "id": "chamberlain",
        "term": "Chamberlain",
        "category": "concepts",
        "intro": "<p>The chamberlain was a high-ranking confidential servant or officer of a royal court, typically responsible for managing access to the monarch's private apartments and handling the royal treasury or household. In the Old Testament, the Hebrew equivalent is often rendered <em>eunuch</em> or <em>officer</em>; Potiphar, the Egyptian to whom Joseph was sold, held such a position (Gen. 37:36; 39:1). The Authorized Version's use of <em>chamberlain</em> in the New Testament reflects the Greek <em>oikonomos</em> (city treasurer): Erastus is identified as <em>chamberlain of the city</em> of Corinth (Rom. 16:23), indicating a position of civic financial administration. Blastus, Herod's chamberlain (Acts 12:20), served as the intermediary through whom Tyre and Sidon sought peace with the king.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chamberlain", "smith": "chamberlain", "isbe": "chamberlain"},
        "key_refs": ["Genesis 37:36", "Genesis 39:1", "Romans 16:23", "Acts 12:20"],
        "sections": []
    },
    "chameleon": {
        "id": "chameleon",
        "term": "Chameleon",
        "category": "concepts",
        "intro": "<p>The chameleon (Hebrew <em>koah</em> or <em>tinshemeth</em>, depending on the verse) is mentioned in Leviticus 11:30 among the unclean creeping things that Israel was forbidden to eat. It is a species of lizard known for its remarkable ability to change color to match its surroundings. Palestine hosts several species of chameleon, making its presence in the Mosaic food regulations fitting. The precise identification of which Hebrew word corresponds to the chameleon remains debated, as ancient versions render the terms differently. Its listing in the Mosaic code reflects the comprehensive character of the dietary laws governing all land creatures that move along the ground.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chameleon", "smith": "chameleon", "isbe": "chameleon"},
        "key_refs": ["Leviticus 11:30"],
        "sections": []
    },
    "chamois": {
        "id": "chamois",
        "term": "Chamois",
        "category": "concepts",
        "intro": "<p>The chamois (Hebrew <em>zemer</em>) appears in Deuteronomy 14:5 among the clean animals that Israel was permitted to eat. It is listed alongside the deer, gazelle, roebuck, and ibex in the group of hoofed wild animals. The precise identification is uncertain: the chamois as known in Europe does not inhabit Palestine, and the Hebrew term may refer to a mountain sheep, ibex, or wild goat native to the rocky highlands of the region. The Septuagint rendered it as <em>camelopardalis</em> (giraffe), which is also problematic geographically, and most modern translations prefer <em>mountain sheep</em> or simply transliterate the term.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chamois", "smith": "chamois", "isbe": "chamois"},
        "key_refs": ["Deuteronomy 14:5"],
        "sections": []
    },
    "champion": {
        "id": "champion",
        "term": "Champion",
        "category": "concepts",
        "intro": "<p>Champion in the Old Testament translates the Hebrew phrase <em>ish ha-benaim</em>, literally <em>the man between the two</em> — referring to the ancient practice of representative or single combat between chosen warriors from opposing armies (1 Sam. 17:4, 23). Goliath's challenge to Israel to send out a champion against whom he would fight was a standard formula of ancient Near Eastern warfare, in which the outcome of single combat was understood to decide the fate of the armies. The theological point of the narrative is that David, an untrained youth with no conventional armor, was God's chosen representative, and that the victory over Goliath was therefore a divine victory rather than a military one.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "champion", "isbe": "champion"},
        "key_refs": ["1 Samuel 17:4", "1 Samuel 17:23"],
        "sections": []
    },
    "chance": {
        "id": "chance",
        "term": "Chance",
        "category": "concepts",
        "intro": "<p>The concept of chance in Scripture is consistently subordinated to divine providence. In Luke 10:31, the Good Samaritan parable begins with the statement that <em>by chance a certain priest came down that road</em> — but the context implies that nothing in the story operates outside God's purposes. The apparent randomness of the Ark of the Covenant returning to Israelite territory (1 Sam. 6:9) is similarly interpreted as a test of whether it was truly God who struck Israel, and Ecclesiastes 9:11 acknowledges that <em>time and chance happen to them all</em> without endorsing a deistic view of random events. Biblical theology consistently holds that what appears as chance from a human perspective operates within the framework of divine sovereignty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chance", "isbe": "chance"},
        "key_refs": ["Luke 10:31", "1 Samuel 6:9", "Ecclesiastes 9:11"],
        "sections": []
    },
    "chancellor": {
        "id": "chancellor",
        "term": "Chancellor",
        "category": "concepts",
        "intro": "<p>Chancellor translates a Persian administrative title (Aramaic <em>ba'al te'em</em>, literally <em>lord of judgment</em> or <em>master of the decree</em>) used in the book of Ezra for Rehum the chancellor, who wrote a letter to King Artaxerxes opposing the rebuilding of Jerusalem's walls (Ezra 4:8–9, 17). The letter was successful in halting the work until the reign of Darius. The title represents a high Persian provincial official with judicial and administrative authority — essentially a royal commissioner overseeing the affairs of the Trans-Euphrates satrapy. The incident illustrates the administrative mechanisms through which the returning exiles' work faced opposition from neighboring peoples.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chancellor", "isbe": "chancellor"},
        "key_refs": ["Ezra 4:8", "Ezra 4:9", "Ezra 4:17"],
        "sections": []
    },
    "changes-of-raiment": {
        "id": "changes-of-raiment",
        "term": "Changes of Raiment",
        "category": "concepts",
        "intro": "<p>Changes of raiment — festive or fine garments kept in reserve — were reckoned among the treasures of wealthy households in the ancient Near East and were given as gifts or prizes on occasions of celebration or contract. Samson offered thirty changes of raiment as prizes in his riddle contest at his wedding (Judg. 14:12–13). Joseph sent his brothers back to Canaan with changes of garments, giving Benjamin five times as many (Gen. 45:22). Naaman brought ten changes of raiment among his gifts to the prophet Elisha, and Gehazi secretly received two of them through his deception (2 Kgs. 5:22–23). The practice reflects the high value placed on fine clothing in a world where fabric was costly and time-consuming to produce.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "changes-of-raiment"},
        "key_refs": ["Genesis 45:22", "Judges 14:12", "Judges 14:13", "2 Kings 5:22", "2 Kings 5:23"],
        "sections": []
    },
    "channel": {
        "id": "channel",
        "term": "Channel",
        "category": "concepts",
        "intro": "<p>Channel in Scripture refers to the bed or course of a river or the sea, used both literally and in poetic imagery. In Psalm 18:15 (= 2 Sam. 22:16), the <em>channels of the sea were seen</em> at the divine rebuke — a poetic description of God's intervention drying up the waters. Isaiah 8:7 employs the metaphor of the Assyrian army as a river overflowing its channels and flooding the land of Judah. Job 31:22 uses the shoulder-socket as an anatomical channel. The term thus covers both natural watercourses and the literary imagery of overwhelming power, divine or military, described through the movement of water.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "channel", "isbe": "channel"},
        "key_refs": ["Psalms 18:15", "Isaiah 8:7"],
        "sections": []
    },
    "chapel": {
        "id": "chapel",
        "term": "Chapel",
        "category": "concepts",
        "intro": "<p>Chapel translates the Hebrew <em>miqdash</em> (sanctuary) in its only New Testament occurrence at Amos 7:13, where the priest Amaziah of Bethel warns Amos: <em>do not prophesy again at Bethel, for it is the king's sanctuary (chapel) and it is a royal house</em>. The term underscores the political dimension of the Bethel shrine — it was not merely a place of worship but an instrument of royal ideology under Jeroboam II, which explains Amaziah's hostility to Amos's prophetic challenge. The irony of calling an idolatrous northern shrine a <em>sanctuary</em> would not have been lost on Amos's audience.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chapel", "isbe": "chapel"},
        "key_refs": ["Amos 7:13"],
        "sections": []
    },
    "chapiter": {
        "id": "chapiter",
        "term": "Chapiter",
        "category": "concepts",
        "intro": "<p>Chapiter is the archaic English term for the ornamental capital — the decorated head — of a pillar. Three distinct Hebrew words are translated this way in the Old Testament, referring to different architectural features. The chapiters of the two great bronze pillars Jachin and Boaz at the entrance of Solomon's temple were five cubits high and elaborately adorned with lily-work, network, and pomegranates (1 Kgs. 7:16–22; 2 Chr. 4:12–13). Their splendor made them among the most notable features of the temple façade. When Nebuchadnezzar destroyed the temple, these chapiters were among the items specifically catalogued as taken to Babylon (2 Kgs. 25:17; Jer. 52:22).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chapiter", "smith": "chapiter", "isbe": "chapiter"},
        "key_refs": ["1 Kings 7:16", "2 Kings 25:17", "2 Chronicles 4:12", "Exodus 36:38"],
        "sections": []
    },
    "chapter": {
        "id": "chapter",
        "term": "Chapter",
        "category": "concepts",
        "intro": "<p>The division of the biblical books into chapters is a relatively modern convention with no basis in the original manuscripts. The Old Testament books were divided into sections (Hebrew <em>parashiyyot</em> and <em>sedarim</em>) for synagogue reading, but the familiar chapter numbers were introduced to the whole Bible by Stephen Langton, Archbishop of Canterbury, around AD 1227, working with the Latin Vulgate. These were then applied to Hebrew and Greek texts. Verse numbers were added to the New Testament by Robert Estienne (Stephanus) in 1551 and to the Old Testament by Rabbi Nathan in the fifteenth century. The chapter and verse system, while convenient for reference (Acts 13:15), was not part of the original structure of any biblical book.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chapter"},
        "key_refs": ["Acts 13:15"],
        "sections": []
    },
    "charashim": {
        "id": "charashim",
        "term": "Charashim",
        "category": "places",
        "intro": "<p>Charashim (meaning <em>craftsmen</em>) was a valley mentioned in 1 Chronicles 4:14 as a place settled by the descendants of Joab son of Seraiah, a skilled craftsman of Judah. The same name appears in Nehemiah 11:35 as one of the towns settled by Benjaminites after the exile from Babylon. The designation <em>valley of craftsmen</em> suggests an industrial settlement known for its artisans — likely woodworkers, metalworkers, or stonecutters — whose guild identity became identified with the geographic location. The site is tentatively identified with Wadi el-Qelt east of Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "charashim", "isbe": "charashim"},
        "key_refs": ["1 Chronicles 4:14", "Nehemiah 11:35"],
        "sections": []
    },
    "charger": {
        "id": "charger",
        "term": "Charger",
        "category": "concepts",
        "intro": "<p>A charger in the Old Testament is a large, wide bowl or deep dish used for offerings or feasting. The silver chargers (basins) given by the heads of the twelve tribes at the dedication of the tabernacle were each weighing a hundred and thirty shekels of silver (Num. 7:13–85). In the New Testament, the charger appears in the account of Salome's request for the head of John the Baptist to be presented to her on a charger (platter), a detail that both Matthew (14:8, 11) and Mark (6:25, 28) record. This New Testament usage reflects a dining vessel — a large serving plate — rather than the ceremonial dish of the Old Testament.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "charger", "smith": "charger", "isbe": "charger"},
        "key_refs": ["Numbers 7:13", "Matthew 14:8", "Matthew 14:11", "Mark 6:25", "Mark 6:28"],
        "sections": []
    },
    "chariot": {
        "id": "chariot",
        "term": "Chariot",
        "category": "concepts",
        "intro": "<p>The chariot was the dominant war machine of the ancient Near East from approximately 1700 BC through the Persian period, used primarily for speed and shock in open-field battle rather than siege warfare. Egypt deployed six hundred elite chariot units against Israel at the Red Sea (Exod. 14:7), a demonstration of military superiority that made the subsequent divine deliverance all the more striking. The Canaanites' iron chariots were cited as the reason why Judah and Joseph's tribes could not initially expel certain peoples from the valleys (Josh. 17:18; Judg. 1:19). Solomon acquired fourteen hundred chariots for his standing army (1 Kgs. 10:26), and chariots appear throughout the accounts of Israelite and Judean warfare with the neighboring kingdoms.</p><p>Beyond military use, chariots carried theological significance: Elijah ascended to heaven in a chariot of fire (2 Kgs. 2:11), and Elisha's prayer opened his servant's eyes to see the fiery horses and chariots of God surrounding them (2 Kgs. 6:17). The chariot of Pharaoh's chief captain, in whose house Joseph served, introduced the motif (Gen. 41:43). Ezekiel's vision of the <em>chariot</em> (merkabah) of God became the basis of a whole tradition of Jewish mystical interpretation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chariot", "smith": "chariot", "isbe": "chariot"},
        "key_refs": ["Genesis 41:43", "Exodus 14:7", "Joshua 17:18", "Judges 1:19", "Judges 4:3"],
        "sections": []
    },
    "charity": {
        "id": "charity",
        "term": "Charity",
        "category": "concepts",
        "intro": "<p>Charity is the rendering in the Authorized Version of the Greek word <em>agapē</em>, which most modern versions translate as <em>love</em>. The word appears most prominently in 1 Corinthians 13, the great apostolic treatise on love, where Paul describes it as the supreme gift that surpasses tongues, prophecy, knowledge, faith, and even martyrdom: <em>If I have not charity, I am nothing</em>. The passage enumerates love's qualities — patience, kindness, absence of envy or pride, endurance of all things — before concluding that <em>charity never faileth</em> while prophecy and tongues will cease.</p><p>The Authorized Version's choice of <em>charity</em> preserved the Latin <em>caritas</em> of the Vulgate, which had connotations of Christian generosity and benevolence toward the poor. While <em>love</em> more accurately captures the Greek term's range, the older rendering shaped centuries of Christian devotion and continues in liturgical and rhetorical tradition. The word <em>agapē</em> appears with similar prominence in the Johannine literature, most famously in the declaration <em>God is love</em> (1 John 4:8, 16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "charity", "isbe": "charity"},
        "key_refs": ["1 Corinthians 13", "1 Corinthians 12:31"],
        "sections": []
    },
    "charmer": {
        "id": "charmer",
        "term": "Charmer",
        "category": "concepts",
        "intro": "<p>A charmer in the Old Testament is one who practices the art of serpent-charming or the recitation of incantations for magical purposes. The Mosaic law explicitly prohibited consulting charmers as part of the forbidden occult practices of Canaan (Deut. 18:11). The image of the deaf adder that stops its ear and <em>will not hearken to the voice of charmers</em> appears in Psalm 58:5 as a description of the irreformably wicked, and Jeremiah uses the same image for an enemy that cannot be propitiated (Jer. 8:17). Ecclesiastes 10:11 observes with practical wisdom that <em>a serpent may bite before it is charmed</em>, while Isaiah 19:3 includes charmer-consulting among the doomed stratagems of Egypt.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "charmer"},
        "key_refs": ["Psalms 58:5", "Jeremiah 8:17", "Ecclesiastes 10:11", "Isaiah 19:3", "Deuteronomy 18:11"],
        "sections": []
    },
    "charran": {
        "id": "charran",
        "term": "Charran",
        "category": "places",
        "intro": "<p>Charran is the New Testament Greek form (Acts 7:2, 4) of Haran, the city in northwestern Mesopotamia (modern southeastern Turkey) where Terah halted with Abraham, Lot, and Sarai on their journey from Ur of the Chaldees toward Canaan, and where Terah died at the age of two hundred and five (Gen. 11:31–32). Stephen's speech to the Sanhedrin (Acts 7) references Charran as the intermediate stopping point of Abraham's call before his entry into Canaan. The city lay on major trade routes and had a significant Mesopotamian moon-cult presence. Abraham later sent his servant back to the region of Charran to find a wife for Isaac (Gen. 24:4, 10).</p>",
        "hitchcock_meaning": "a singing or calling out",
        "source_ids": {"easton": "charran", "smith": "charran", "isbe": "charran"},
        "key_refs": ["Acts 7:2", "Acts 7:4"],
        "sections": []
    },
    "chebar": {
        "id": "chebar",
        "term": "Chebar",
        "category": "places",
        "intro": "<p>The Chebar (meaning <em>force</em> or <em>strength</em>) was a river or canal in the <em>land of the Chaldeans</em> along whose banks the prophet Ezekiel received his inaugural vision of the divine chariot-throne (Ezek. 1:1–3) and several subsequent visions (Ezek. 3:15, 23; 10:15, 20; 43:3). The community of Jewish exiles from whom Ezekiel came lived beside this waterway. Assyriological research has identified the Chebar with the <em>naru kabari</em> (the great canal) mentioned in Babylonian texts — a major irrigation channel running from the Euphrates near Nippur. The river thus anchors Ezekiel's visions in a specific geographic and historical setting: the Babylonian exile of the early sixth century BC.</p>",
        "hitchcock_meaning": "force or strength",
        "source_ids": {"easton": "chebar", "smith": "chebar", "isbe": "chebar"},
        "key_refs": ["Ezekiel 1:3", "Ezekiel 1:1", "Ezekiel 3:15", "Ezekiel 3:23", "Ezekiel 10:15"],
        "sections": []
    },
    "chedorlaomer": {
        "id": "chedorlaomer",
        "term": "Chedorlaomer",
        "category": "people",
        "intro": "<p>Chedorlaomer (corresponding to the Elamite name Kudur-Lagamar) was the king of Elam who led a coalition of four kings in the military campaign described in Genesis 14. He had held Mesopotamian supremacy over the five kings of the Canaanite Jordan plain for twelve years before those kings rebelled in the thirteenth year. In the fourteenth year, Chedorlaomer and his allies swept through Transjordan and the Negev, defeating the five kings at the Valley of Siddim and capturing Lot. This prompted Abraham's daring pursuit with three hundred and eighteen trained servants, resulting in Lot's rescue and the recovery of the plunder (Gen. 14:1–17). The identification of Chedorlaomer with specific Elamite kings in the cuneiform record has been proposed but not definitively established.</p>",
        "hitchcock_meaning": "roundness of a sheaf",
        "source_ids": {"easton": "chedorlaomer", "isbe": "chedorlaomer"},
        "key_refs": [],
        "sections": []
    },
    "cheek": {
        "id": "cheek",
        "term": "Cheek",
        "category": "concepts",
        "intro": "<p>Smiting a person on the cheek was regarded in the ancient Near East as a deliberate act of humiliation and grievous insult, beyond ordinary assault. Job describes his enemies striking his cheek in contempt (Job 16:10), and Lamentations 3:30 portrays the suffering servant giving his cheek to those who strike him. Micah prophesied that a ruler of Israel would be struck on the cheek (Mic. 5:1). These passages form the background for Jesus's teaching in the Sermon on the Mount: <em>if anyone slaps you on the right cheek, turn to him the other also</em> (Matt. 5:39; Luke 6:29) — a command understood not as passive acceptance of injustice but as a refusal to answer insult with retaliation, reflecting the spirit of Isaiah's Suffering Servant who <em>gave his back to those who strike</em> (Isa. 50:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cheek"},
        "key_refs": ["Job 16:10", "Lamentations 3:30", "Micah 5:1", "Luke 6:29", "Matthew 5:39"],
        "sections": []
    },
    "cheese": {
        "id": "cheese",
        "term": "Cheese",
        "category": "concepts",
        "intro": "<p>Cheese is mentioned three times in the Old Testament, reflecting its place in the pastoral economy of ancient Israel. Jesse sent David to take <em>ten cheeses</em> to the commander of his brothers' regiment at the front lines facing Goliath (1 Sam. 17:18). When David fled from Absalom, his supporters brought him honey, butter, sheep, cheese, and other provisions to Mahanaim (2 Sam. 17:29). Job employs the image of cheese to describe God's fashioning of the embryo in the womb: <em>Did you not pour me out like milk and curdle me like cheese?</em> (Job 10:10). The Hebrew terms used suggest curdled milk or a form of soft cheese rather than aged hard cheese.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cheese", "smith": "cheese", "isbe": "cheese"},
        "key_refs": ["1 Samuel 17:18", "2 Samuel 17:29", "Job 10:10"],
        "sections": []
    },
    "chemarim": {
        "id": "chemarim",
        "term": "Chemarim",
        "category": "concepts",
        "intro": "<p>Chemarim (Hebrew <em>kemarim</em>, meaning <em>black ones</em> — possibly for their black garments) is the term used in Zephaniah 1:4 for the idolatrous priests whom the Lord declared he would cut off from Jerusalem alongside the priests of Baal. The same Hebrew word is rendered <em>idolatrous priests</em> in 2 Kings 23:5, where Josiah's reform eliminated those whom previous kings of Judah had appointed to burn incense at the high places in the cities of Judah and around Jerusalem, as well as those who burned incense to Baal, the sun, the moon, the constellations, and all the host of heaven. Hosea 10:5 uses the word for the priests who mourned the exile of the calf idol from Bethel. The term thus designates non-Levitical priests of false worship throughout the monarchy period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chemarim", "isbe": "chemarim"},
        "key_refs": ["Zephaniah 1:4", "2 Kings 23:5", "Hosea 10:5"],
        "sections": []
    },
    "chemosh": {
        "id": "chemosh",
        "term": "Chemosh",
        "category": "concepts",
        "intro": "<p>Chemosh (meaning <em>the destroyer</em>, <em>subduer</em>, or possibly <em>fish-god</em>) was the national deity of Moab, whose devotees are called <em>the people of Chemosh</em> in Numbers 21:29 and Jeremiah 48:46. The god demanded sacrifices including human offering: the Moabite king Mesha, in a moment of military crisis, offered his firstborn son as a burnt offering on the city wall, a deed that the biblical narrator says caused <em>great wrath to come upon Israel</em> (2 Kgs. 3:27). Solomon, in his late apostasy, built a high place for Chemosh on the Mount of Olives east of Jerusalem — the Hill of Corruption — to please his Moabite wives (1 Kgs. 11:7, 33).</p><p>Jeremiah's oracle against Moab repeatedly invokes Chemosh's coming shame and exile alongside his people (Jer. 48:7, 13, 46). The Moabite Stone (c. 840 BC), discovered in 1868, contains an inscription by King Mesha attributing his military successes to Chemosh and mentioning Israel — the most detailed extra-biblical inscription bearing on Old Testament history. Chemosh appears to have been also worshipped by the Ammonites in some periods.</p>",
        "hitchcock_meaning": "handling; stroking; taking away",
        "source_ids": {"easton": "chemosh", "smith": "chemosh", "isbe": "chemosh"},
        "key_refs": ["Numbers 21:29", "Jeremiah 48:7", "Jeremiah 48:13", "Jeremiah 48:46", "1 Kings 11:7"],
        "sections": []
    },
    "chenaanah": {
        "id": "chenaanah",
        "term": "Chenaanah",
        "category": "people",
        "intro": "<p>Chenaanah (meaning <em>merchant</em> or <em>broken in pieces</em>) is the name of two individuals in the Old Testament. (1) A Benjamite, son of Bilhan, listed in 1 Chronicles 7:10 among the descendants of Benjamin. (2) The father of Zedekiah the prophet, who made iron horns and falsely prophesied that Ahab and Jehoshaphat would gore the Syrians to victory at Ramoth-gilead (1 Kgs. 22:11, 24; 2 Chr. 18:10, 23). This Zedekiah struck the true prophet Micaiah on the cheek for his contradicting report, and his father Chenaanah is remembered only through his son's false prophecy and its disastrous fulfillment when Ahab was killed at Ramoth-gilead.</p>",
        "hitchcock_meaning": "broken in pieces",
        "source_ids": {"easton": "chenaanah", "smith": "chenaanah", "isbe": "chenaanah"},
        "key_refs": ["1 Chronicles 7:10", "1 Kings 22:11", "1 Kings 22:24"],
        "sections": []
    },
    "chenaiah": {
        "id": "chenaiah",
        "term": "Chenaiah",
        "category": "people",
        "intro": "<p>Chenaiah (meaning <em>whom Jehovah hath made</em>) was a Levite described as the <em>chief of the Levites</em> responsible for the musical service when David organized the transport of the ark of the covenant to Jerusalem (1 Chr. 15:22). He was appointed to instruct the singers in song because he <em>was skillful</em>, indicating an expert musicianship recognized among his contemporaries. He may have been a Kohathite Levite of the house of Izhar or Hebron. Chenaiah's appointment reflects David's careful organization of Levitical ministry in preparation for the permanent establishment of worship in Jerusalem before the temple was built.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chenaiah"},
        "key_refs": ["1 Chronicles 15:22"],
        "sections": []
    },
    "chephirah": {
        "id": "chephirah",
        "term": "Chephirah",
        "category": "places",
        "intro": "<p>Chephirah (meaning <em>a little lioness</em> or <em>village</em>) was one of the four cities of the Gibeonite Hivites who deceived Joshua into making a peace treaty with them by presenting themselves as distant travelers (Josh. 9). The other three cities were Gibeon, Beeroth, and Kirjath-jearim. The treaty bound Israel to protect them, which Saul later violated. Chephirah was assigned to the tribe of Benjamin (Josh. 18:26) and was reoccupied after the Babylonian exile by returned exiles (Ezra 2:25; Neh. 7:29). It has been identified with Khirbet Kefireh, west of Jerusalem.</p>",
        "hitchcock_meaning": "a little lioness",
        "source_ids": {"easton": "chephirah", "smith": "chephirah", "isbe": "chephirah"},
        "key_refs": [],
        "sections": []
    },
    "cherethim": {
        "id": "cherethim",
        "term": "Cherethim",
        "category": "concepts",
        "intro": "<p>The Cherethim (or Cherethites) were a people closely associated with the Philistines, inhabiting the southern coastal region of Canaan (1 Sam. 30:14; Ezek. 25:16; Zeph. 2:5). Ezekiel's oracle against the Philistines includes the Cherethites as part of the coastal people under divine judgment. In the service of David, the Cherethites and Pelethites served as a royal bodyguard — elite foreign mercenaries personally loyal to the king — commanded by Benaiah son of Jehoiada (2 Sam. 8:18; 20:7, 23; 1 Kgs. 1:38, 44). They remained loyal to David during Absalom's revolt and to Solomon at his coronation. Their origin is variously linked to Crete (the Caphtorim) or to a southern Philistine clan, though no definitive identification has been established.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cherethim", "smith": "cherethim"},
        "key_refs": ["Ezekiel 25:16", "Zephaniah 2:5", "1 Samuel 30:14", "2 Samuel 8:18", "2 Samuel 20:7"],
        "sections": []
    },
    "cherith": {
        "id": "cherith",
        "term": "Cherith",
        "category": "places",
        "intro": "<p>Cherith (meaning <em>a cutting</em> or <em>gorge</em>) was a wadi or seasonal stream-bed east of the Jordan at which Elijah hid and was miraculously sustained during the drought he had announced to King Ahab (1 Kgs. 17:3–7). By divine command, ravens brought Elijah bread and meat morning and evening, and he drank from the brook until it dried up because of the drought. The Cherith episode is the first in a sequence of miracles that sustained Elijah through the three-and-a-half-year famine, continuing with the widow of Zarephath's inexhaustible flour and oil. Its location east of the Jordan has been debated; several wadis in the Transjordanian highlands have been proposed.</p>",
        "hitchcock_meaning": "cutting; piercing; slaying",
        "source_ids": {"easton": "cherith"},
        "key_refs": ["1 Kings 17:3", "1 Kings 17:5"],
        "sections": []
    },
    "cherub": {
        "id": "cherub",
        "term": "Cherub",
        "category": "concepts",
        "intro": "<p>The cherubim (plural of cherub) are a class of supernatural beings who appear in Scripture as guardians of the divine presence and throne. Their first appearance is at the east of the Garden of Eden, where God stationed them with a flaming, revolving sword to guard the way to the tree of life after the expulsion of Adam and Eve (Gen. 3:24). In the tabernacle and temple, golden cherubim were fashioned on the mercy seat of the ark of the covenant, their wings outstretched over the cover between which God declared he would meet with Moses (Exod. 25:17–22). Solomon's temple contained two great olive-wood cherubim, each ten cubits high with a wingspan of ten cubits, whose wings together spanned the entire breadth of the inner sanctuary (1 Kgs. 6:23–28).</p><p>Ezekiel's inaugural vision by the Chebar canal describes four living creatures with human, lion, ox, and eagle faces — identified in Ezekiel 10 as the cherubim — who support the divine chariot-throne. Their appearance there is terrifying and complex, combining features of multiple creatures with wheels full of eyes. Isaiah's seraphim (Isa. 6:2–3) are related beings who attend the divine throne and declare the holiness of God. In Revelation, four living creatures continue this tradition around the heavenly throne (Rev. 4:6–8). Cherubim are not the gentle winged infants of Renaissance art but powerful, multi-formed guardians of divine holiness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "cherub", "smith": "cherub", "isbe": "cherub"},
        "key_refs": ["Genesis 3:24", "Exodus 25:17", "Exodus 26:1", "Exodus 26:31", "Numbers 7:89"],
        "sections": []
    },
    "chesalon": {
        "id": "chesalon",
        "term": "Chesalon",
        "category": "places",
        "intro": "<p>Chesalon (meaning <em>strength</em> or <em>confidence</em>) was a town on the northern border of Judah, identified as a point on the shoulder of Mount Jearim (also called Chesalon) in the boundary description of Joshua 15:10. The site is identified with modern Kesla, a village about twelve miles west of Jerusalem in the Judean foothills. It served as a boundary marker between the tribal allotments of Judah and Dan.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chesalon", "smith": "chesalon", "isbe": "chesalon"},
        "key_refs": ["Joshua 15:10"],
        "sections": []
    },
    "chesed": {
        "id": "chesed",
        "term": "Chesed",
        "category": "people",
        "intro": "<p>Chesed (meaning <em>gain</em> or, in Hitchcock, <em>as a devil or destroyer</em>) was the fourth son of Nahor, Abraham's brother, by his wife Milcah (Gen. 22:22). The names of Nahor's sons in Genesis 22:20–24 appear to correspond to tribal or geographic names in the region of Aram (Syria), and Chesed may be the eponymous ancestor of the Chaldeans (Hebrew <em>Kasdim</em>), linking the Chaldean people to Abraham's extended family through the line of Nahor. He is not mentioned elsewhere in Scripture.</p>",
        "hitchcock_meaning": "as a devil, or a destroyer",
        "source_ids": {"easton": "chesed", "smith": "chesed", "isbe": "chesed"},
        "key_refs": ["Genesis 22:22"],
        "sections": []
    },
    "chesil": {
        "id": "chesil",
        "term": "Chesil",
        "category": "places",
        "intro": "<p>Chesil (meaning <em>ungodly</em> or <em>foolishness</em>) was a town in the extreme south of Judah, mentioned in Joshua 15:30 in the list of Judah's southern boundary cities. It is very probably the same place as Bethul (Josh. 19:4) and Bethuel (1 Chr. 4:30) assigned to Simeon, as those tribes' territories overlapped in the south. Some scholars also identify it with Bethlehem (of the south), distinguished from Bethlehem of Judah. The town's location in the Negev placed it on the southern frontier of Israelite settlement.</p>",
        "hitchcock_meaning": "foolishness",
        "source_ids": {"easton": "chesil", "smith": "chesil", "isbe": "chesil"},
        "key_refs": ["Joshua 15:30", "1 Chronicles 4:30"],
        "sections": []
    },
    "chest": {
        "id": "chest",
        "term": "Chest",
        "category": "concepts",
        "intro": "<p>The chest (Hebrew <em>'aron</em>, commonly rendered <em>ark</em>) in its non-ark usage refers to the offering box or coffer set up at the temple entrance to collect money for its repair. King Joash and the priest Jehoiada instituted this chest, boring a hole in its lid, and set it beside the altar at the right side of the entrance to the house of the Lord (2 Kgs. 12:9–10; 2 Chr. 24:8–11). The people's willingness to fill the chest with offerings reflected their response to Joash's initiative for temple restoration. The same word covers the boxes of treasure used to transport temple funds, illustrating that in biblical usage <em>chest</em> and <em>ark</em> are the same Hebrew concept applied to different containers.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chest", "smith": "chest", "isbe": "chest"},
        "key_refs": ["2 Kings 12:9", "2 Kings 12:10", "2 Chronicles 24:8", "2 Chronicles 24:10", "2 Chronicles 24:11"],
        "sections": []
    },
    "chestnut-tree": {
        "id": "chestnut-tree",
        "term": "Chestnut Tree",
        "category": "concepts",
        "intro": "<p>The chestnut tree (Hebrew <em>'armon</em>, meaning <em>naked</em> or <em>stripped</em> — referring to the tree's smooth, peeling bark) is mentioned in two Old Testament passages. In Genesis 30:37, Jacob peeled rods of chestnut (and other trees) to place before the flocks at their watering troughs in a folk-breeding practice aimed at influencing the coloring of the offspring. Ezekiel 31:8 includes the chestnut tree among the great trees of the forest of Lebanon as a measure of comparison for Assyria's greatness. The identification with the European chestnut is uncertain; many scholars now prefer the <em>plane tree</em> (Platanus orientalis), which grows along streambeds in the Levant and has conspicuously peeling bark.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chestnut-tree", "smith": "chestnut-tree", "isbe": "chestnut-tree"},
        "key_refs": ["Genesis 30:37", "Ezekiel 31:8"],
        "sections": []
    },
    "chesulloth": {
        "id": "chesulloth",
        "term": "Chesulloth",
        "category": "places",
        "intro": "<p>Chesulloth (meaning <em>fertile places</em> or <em>the loins</em>) was a town of the tribe of Issachar on the slopes overlooking the valley of Jezreel (Josh. 19:18). It is likely identical with Chisloth-tabor (Josh. 19:12), a place on the border of Zebulun near Mount Tabor. The site is tentatively identified with modern Iksal, a village on the hills southeast of Nazareth commanding the Jezreel Valley. As a border town of Issachar, it lay in the fertile agricultural heartland of northern Israel.</p>",
        "hitchcock_meaning": "fearfulness",
        "source_ids": {"easton": "chesulloth", "smith": "chesulloth", "isbe": "chesulloth"},
        "key_refs": ["Joshua 19:18"],
        "sections": []
    },
    "chezib": {
        "id": "chezib",
        "term": "Chezib",
        "category": "places",
        "intro": "<p>Chezib (meaning <em>deceitful</em>) was the town where Shelah, the third son of Judah by his Canaanite wife the daughter of Shua, was born (Gen. 38:5). The name is likely the same place as Achzib (Josh. 15:44; Mic. 1:14) and Chozeba (1 Chr. 4:22), all located in the Shephelah of Judah. The irony of the name <em>deceitful</em> at the birth of Shelah, in the context of Judah's relationship with Tamar involving multiple acts of deception, may be a deliberate narrative touch by the author of Genesis 38.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chezib", "smith": "chezib", "isbe": "chezib"},
        "key_refs": ["Genesis 38:5"],
        "sections": []
    },
    "chidon": {
        "id": "chidon",
        "term": "Chidon",
        "category": "places",
        "intro": "<p>Chidon (meaning <em>a dart</em>) was the name of the threshing-floor at which Uzzah was struck dead when he reached out to steady the ark of the covenant as the oxen pulling the cart stumbled (1 Chr. 13:9). The parallel account in 2 Samuel 6:6 names the same location Nachon or Nacon. David called the place Perez-uzza (<em>the breaking out against Uzzah</em>) in memory of the event, which halted the ark's procession to Jerusalem. The incident led to the ark being placed for three months in the house of Obed-edom the Gittite before its eventual successful transport to the city of David.</p>",
        "hitchcock_meaning": "a dart",
        "source_ids": {"easton": "chidon", "smith": "chidon"},
        "key_refs": ["1 Chronicles 13:9", "2 Samuel 6:6"],
        "sections": []
    },
    "chief-of-the-three": {
        "id": "chief-of-the-three",
        "term": "Chief of the Three",
        "category": "concepts",
        "intro": "<p>Chief of the Three was a title given to the foremost of David's three most distinguished mighty men. In 2 Samuel 23:8, the title is applied to Josheb-basshebeth the Tahchemonite (also called Adino the Eznite), who killed eight hundred men at one time. The corresponding list in 1 Chronicles 11:11 names Jashobeam the Hachmonite who killed three hundred in a single encounter. These three — Josheb-basshebeth, Eleazar son of Dodo the Ahohite, and Shammah the Hararite — formed the inner circle of David's military elite, distinguished from the wider group of thirty mighty men. Their exploits, including fetching water for David from the well at Bethlehem through Philistine lines, are recorded as acts of devotion beyond the requirements of duty (2 Sam. 23:13–17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chief-of-the-three"},
        "key_refs": ["2 Samuel 23:8", "1 Chronicles 11:11"],
        "sections": []
    },
    "chief-priest": {
        "id": "chief-priest",
        "term": "Chief Priest",
        "category": "concepts",
        "intro": "<p>The chief priest (also translated <em>high priest</em>) was the supreme head of the Israelite priesthood, distinguished from ordinary priests by unique vestments including the ephod, breastplate, and turban with the golden plate bearing <em>Holy to the Lord</em>. Established in the person of Aaron and transmitted through his descendants, the office carried responsibility for the annual Day of Atonement ritual — the only occasion when the high priest entered the innermost sanctuary to make atonement for Israel's sins. The chief priests in the New Testament formed a ruling aristocracy at Jerusalem closely associated with the Sadducean party, wielding both religious and political authority under Roman oversight. The Epistle to the Hebrews develops an extended theological argument that Jesus is the ultimate high priest, superior to the Aaronic order, whose self-offering surpasses and fulfills all that the Levitical sacrificial system foreshadowed (Heb. 4–10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chief-priest"},
        "key_refs": [],
        "sections": []
    },
    "chiefs-of-asia": {
        "id": "chiefs-of-asia",
        "term": "Chiefs of Asia",
        "category": "concepts",
        "intro": "<p>The Chiefs of Asia (Greek <em>Asiarchoi</em>) were prominent civic officials of the Roman province of Asia who appear in Acts 19:31 as personal friends of Paul, who warned him not to enter the theater during the Ephesian riot. Asiarchs were wealthy, high-status individuals elected by their cities to preside over public festivals and games in honor of the Roman imperial cult, and to manage the religious and social events of the koinon (the provincial assembly) of Asia. The fact that Paul had personal friends among this aristocratic pagan class illustrates the diverse social reach of his Ephesian ministry, during which all the residents of Asia heard the word of the Lord (Acts 19:10).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chiefs-of-asia"},
        "key_refs": ["Acts 19:31"],
        "sections": []
    },
    "child": {
        "id": "child",
        "term": "Child",
        "category": "concepts",
        "intro": "<p>Child in Scripture covers a wide range of Hebrew and Greek terms designating offspring at various stages of development — from infancy through early adulthood. The term carries considerable theological weight: children are described as a heritage from the Lord (Ps. 127:3), and the failure to produce heirs was a source of grief deeply felt by figures like Sarah, Hannah, and Elizabeth. The Mosaic law gave particular protections to children and imposed obligations of parental instruction (Deut. 6:7). Prophetic imagery often uses the vulnerability of childhood to describe Israel's dependence on God (Hos. 11:1; Isa. 49:15).</p><p>In the New Testament, Jesus's welcome of children in the face of his disciples' rebuke (<em>of such is the kingdom of God</em>, Mark 10:14) and his call to become like a child (Matt. 18:3) gave childhood a positive theological valuation as a model of receptivity and dependence. Paul and John both use <em>children of God</em> (Greek <em>tekna theou</em>) to describe the status of believers as those born of God through faith (John 1:12; Rom. 8:16; 1 John 3:1–2).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "child"},
        "key_refs": ["Genesis 37:3", "1 Kings 3:7", "Genesis 21:8", "Exodus 2:7", "Exodus 2:9"],
        "sections": []
    },
    "chileab": {
        "id": "chileab",
        "term": "Chileab",
        "category": "people",
        "intro": "<p>Chileab (meaning <em>protected by the father</em> or <em>like the father</em>) was the second son of David, born to him by Abigail the Carmelitess, former wife of Nabal, after David became king in Hebron (2 Sam. 3:3). In 1 Chronicles 3:1, the same son is called Daniel. Chileab is not mentioned again in the historical narrative, which suggests he died young or played no role in the succession struggles that occupied so much of David's reign. His birth to Abigail — whom David married after Nabal's death and whose wisdom had saved David from bloodguilt — gave him a notable heritage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chileab", "smith": "chileab", "isbe": "chileab"},
        "key_refs": ["2 Samuel 3:3", "1 Chronicles 3:1"],
        "sections": []
    },
    "chilion": {
        "id": "chilion",
        "term": "Chilion",
        "category": "people",
        "intro": "<p>Chilion (meaning <em>the pining one</em> or <em>finished; complete</em>) was the younger son of Elimelech and Naomi who accompanied his parents from Bethlehem to Moab during a famine (Ruth 1:2). In Moab, Chilion married a Moabite woman named Orpah. Both Chilion and his brother Mahlon died in Moab, leaving their mother Naomi a widow with two Moabite daughters-in-law and no male heirs. His death precipitated the central crisis of the book of Ruth: Naomi's decision to return to Bethlehem, Orpah's departure, and Ruth's famous declaration of loyalty — which led ultimately to Ruth's marriage to Boaz and the continuation of the family line (Ruth 4:9–10).</p>",
        "hitchcock_meaning": "finished; complete; perfect",
        "source_ids": {"easton": "chilion", "isbe": "chilion"},
        "key_refs": ["Ruth 1:2", "Ruth 4:9"],
        "sections": []
    },
    "chilmad": {
        "id": "chilmad",
        "term": "Chilmad",
        "category": "places",
        "intro": "<p>Chilmad (meaning <em>teaching or learning</em>) appears in Ezekiel 27:23 as one of the trading partners of the city of Tyre, listed alongside Sheba and Asshur. It is described as trading in choice garments, embroidered work, and chests of rich apparel. The exact location of Chilmad is unknown; suggestions have included Kalwadha (near Baghdad) and a site in the Tigris-Euphrates region, but no identification has been confirmed. The passage as a whole catalogues Tyre's far-flung commercial network in the ancient Near East before its prophesied destruction.</p>",
        "hitchcock_meaning": "teaching or learning",
        "source_ids": {"easton": "chilmad", "smith": "chilmad", "isbe": "chilmad"},
        "key_refs": ["Ezekiel 27:23"],
        "sections": []
    },
    "chimham": {
        "id": "chimham",
        "term": "Chimham",
        "category": "people",
        "intro": "<p>Chimham (meaning <em>pining</em> or <em>as they; like to them</em>) was probably the youngest son of Barzillai the Gileadite, the wealthy supporter who supplied David with provisions during his flight from Absalom and afterward came to escort the king back across the Jordan. When David offered to repay Barzillai with a place at the royal court in Jerusalem, the aged Barzillai declined on account of his age and sent Chimham in his place (2 Sam. 19:37–40). David promised to do for Chimham whatever he wished (2 Sam. 19:38; 1 Kgs. 2:7). The <em>inn of Chimham</em> near Bethlehem (Jer. 41:17) probably commemorates land David gave to this family, preserving his name in the landscape for generations.</p>",
        "hitchcock_meaning": "as they; like to them",
        "source_ids": {"easton": "chimham", "smith": "chimham", "isbe": "chimham"},
        "key_refs": ["2 Samuel 19:37", "Jeremiah 41:17", "1 Kings 2:7"],
        "sections": []
    },
    "chinnereth": {
        "id": "chinnereth",
        "term": "Chinnereth",
        "category": "places",
        "intro": "<p>Chinnereth (meaning <em>lyre</em>, from the harp-like shape of the lake) is the Old Testament name for what the New Testament calls the Sea of Galilee. It appears as a geographical designation for the lake itself (Deut. 3:17; Josh. 13:27; Num. 34:11) and also as the name of a fortified city on the northwestern shore of the lake (Josh. 19:35; 1 Kgs. 15:20). The lake was also called the Sea of Chinneroth (Josh. 12:3) and in later periods the Sea of Gennesaret (Luke 5:1) and the Sea of Tiberias (John 6:1; 21:1). Its shores became the primary setting of Jesus's ministry in Galilee, where he called his first disciples, calmed storms, and multiplied bread and fish for the multitudes.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chinnereth", "smith": "chinnereth"},
        "key_refs": ["Deuteronomy 3:17", "Joshua 19:35", "1 Kings 15:20", "Numbers 34:11", "Joshua 13:27"],
        "sections": []
    },
    "chios": {
        "id": "chios",
        "term": "Chios",
        "category": "places",
        "intro": "<p>Chios (meaning <em>open</em> or <em>mastic</em>) was a mountainous island in the Aegean Sea, situated about five miles off the western coast of Asia Minor (modern Turkey), approximately halfway between Smyrna and Lesbos. In Acts 20:15, Paul's ship on his final journey to Jerusalem anchored opposite Chios, passing between the island and the mainland on the way from Mitylene to Samos. The island was famous in antiquity for its wine and for the production of mastic resin. It belonged to the Roman province of Asia.</p>",
        "hitchcock_meaning": "open; opening",
        "source_ids": {"easton": "chios", "smith": "chios", "isbe": "chios"},
        "key_refs": ["Acts 20:15"],
        "sections": []
    },
    "chisleu": {
        "id": "chisleu",
        "term": "Chisleu",
        "category": "concepts",
        "intro": "<p>Chisleu (also spelled Kislev) is the ninth month of the Hebrew religious calendar, corresponding approximately to November–December in the Gregorian calendar. The name was adopted from the Babylonian month Kislimu during or after the exile and appears twice in the Old Testament: in Nehemiah 1:1, where it records the month in which Nehemiah received the distressing news about Jerusalem's broken walls, and in Zechariah 7:1, where a delegation came to seek a prophetic word from the Lord in the fourth year of Darius. The Feast of Hanukkah (not in the Old Testament canon) is celebrated on the 25th of Chisleu, commemorating the rededication of the temple after the Maccabean revolt.</p>",
        "hitchcock_meaning": "Cisleu, Casleu, rashness; confidence",
        "source_ids": {"easton": "chisleu", "smith": "chisleu"},
        "key_refs": ["Nehemiah 1:1", "Zechariah 7:1"],
        "sections": []
    },
    "chittim": {
        "id": "chittim",
        "term": "Chittim",
        "category": "concepts",
        "intro": "<p>Chittim (or Kittim) is a plural form in Genesis 10:4 designating the descendants of Kittim son of Javan (Greece), associated in the Table of Nations with the Mediterranean islands, particularly Cyprus — whose ancient capital Kition (Citium) is thought to preserve the name. In prophetic usage the term expands to cover the maritime powers of the western Mediterranean. Balaam's oracle speaks of ships from Chittim afflicting Assyria and Eber (Num. 24:24), and Isaiah refers to <em>the isle of Chittim</em> in his oracle against Tyre (Isa. 23:1, 12). Jeremiah uses Chittim as an example of western peoples more faithful to their gods than Israel is to the Lord (Jer. 2:10). In Daniel 11:30, ships of Chittim are understood as the Romans whose fleet turned back Antiochus IV Epiphanes from Egypt.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chittim", "isbe": "chittim"},
        "key_refs": ["Genesis 10:4", "Numbers 24:24", "Isaiah 23:1", "Isaiah 23:12", "Jeremiah 2:10"],
        "sections": []
    },
    "chiun": {
        "id": "chiun",
        "term": "Chiun",
        "category": "concepts",
        "intro": "<p>Chiun (or Kiyyun) appears in Amos 5:26 in the prophet's condemnation of Israel's wilderness idolatry: <em>You shall take up Sikkuth your king, and Chiun your idol, your star-god</em>. The term is generally identified with the Assyrian-Babylonian deity Kaiwanu, associated with the planet Saturn and its cult. The Septuagint rendered Chiun as Raiphan, which Stephen's speech in Acts 7:43 follows (quoting Amos 5:26 as <em>Rephan</em>). The passage indicates that even during the wilderness period Israel was worshipping astral deities alongside or instead of the God of the covenant — a charge consistent with the prophetic indictment of Israel's persistent idolatry rooted in the exodus generation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chiun", "smith": "chiun"},
        "key_refs": ["Amos 5:26", "Acts 7:43"],
        "sections": []
    },
    "chloe": {
        "id": "chloe",
        "term": "Chloe",
        "category": "people",
        "intro": "<p>Chloe (meaning <em>green herb</em> or <em>verdant</em>) was a female Christian mentioned in 1 Corinthians 1:11, where Paul writes that members of her household had informed him of the contentious factions dividing the Corinthian church. Paul names her without apology, indicating she was a person of recognized standing whose household could credibly report on the church's condition. Whether she herself was a believer, a patron of the Corinthian church, or a resident of Ephesus whose household members had recently been in Corinth is not stated. She is among the few women identified by name in Paul's letters in connection with the life of a specific congregation.</p>",
        "hitchcock_meaning": "green herb",
        "source_ids": {"easton": "chloe", "smith": "chloe", "isbe": "chloe"},
        "key_refs": ["1 Corinthians 1:11"],
        "sections": []
    },
    "chor-ashan": {
        "id": "chor-ashan",
        "term": "Chor-ashan",
        "category": "places",
        "intro": "<p>Chor-ashan (meaning <em>smoking furnace</em>) was one of the towns to which David sent gifts of spoil after his defeat of the Amalekites who had raided and burned Ziklag (1 Sam. 30:30). The same location may appear as Ashan in Joshua 15:42 and 19:7 in the tribal allotments of Judah and Simeon. The town lay in the Negev region of southern Judah and Simeon, among the communities that had supported David during his period of refuge and guerrilla activity before he became king.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chor-ashan"},
        "key_refs": ["1 Samuel 30:30", "Joshua 15:42", "Joshua 19:7"],
        "sections": []
    },
    "chorazin": {
        "id": "chorazin",
        "term": "Chorazin",
        "category": "places",
        "intro": "<p>Chorazin (meaning <em>the secret</em> or <em>here is a mystery</em>) was a city in Galilee named alongside Bethsaida and Capernaum in Jesus's pronouncement of woe against towns that had witnessed mighty works but had not repented (Matt. 11:21; Luke 10:13). Jesus's declaration that it would be more tolerable for Tyre and Sidon in the day of judgment than for Chorazin marks it as a site of significant miraculous ministry not otherwise recorded in the Gospels — a reminder that the canonical accounts are selective (cf. John 21:25). The site has been identified with Khirbet Kerazeh, about two miles north of Capernaum, where ruins of a second-century synagogue have been excavated.</p>",
        "hitchcock_meaning": "the secret; here is a mystery",
        "source_ids": {"easton": "chorazin", "smith": "chorazin", "isbe": "chorazin"},
        "key_refs": ["Matthew 11:21", "Luke 10:13"],
        "sections": []
    },
    "chosen": {
        "id": "chosen",
        "term": "Chosen",
        "category": "concepts",
        "intro": "<p>The concept of being chosen (Hebrew <em>bahar</em>; Greek <em>eklektos</em>) runs throughout Scripture as a description of God's sovereign selection of persons or peoples for a particular purpose. In the Old Testament, the term is applied to warriors selected for their skill (Exod. 15:4; Judg. 20:16), to Israel as God's chosen nation (Deut. 7:7; Ps. 105:43; Isa. 45:4), and to Jerusalem and the temple as the place God chose for his name to dwell (1 Kgs. 11:13). The choosing of Israel is explicitly not based on their size or merit but on God's love and covenant faithfulness (Deut. 7:7–8).</p><p>In the New Testament, <em>chosen</em> or <em>elect</em> describes those whom God calls in Christ (Matt. 22:14; Rom. 8:33; Eph. 1:4; 1 Pet. 2:9). The doctrine of divine election has been a central and contested subject in Christian theology, with different traditions emphasizing God's sovereign initiative and human responsibility in different ways. Jesus himself is called the <em>Chosen One</em> of God (Luke 23:35).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chosen", "isbe": "chosen"},
        "key_refs": ["Exodus 15:4", "Judges 20:16", "Psalms 105:43", "Deuteronomy 7:7", "1 Kings 11:13"],
        "sections": []
    },
    "chozeba": {
        "id": "chozeba",
        "term": "Chozeba",
        "category": "places",
        "intro": "<p>Chozeba (meaning <em>liars in wait</em> or <em>the place of ambush</em>) appears in 1 Chronicles 4:22 as the home of certain men of Judah described as <em>the men of Chozeba, and Joash and Saraph, who had dominion in Moab</em>. It is the same place as Chezib (Gen. 38:5) and Achzib (Josh. 15:44; Mic. 1:14), a town in the Shephelah of Judah. The triple identification under different names illustrates how a single ancient site could be known by multiple designations across different periods and literary contexts in the Old Testament.</p>",
        "hitchcock_meaning": "men liers in wait",
        "source_ids": {"easton": "chozeba", "smith": "chozeba", "isbe": "chozeba"},
        "key_refs": ["1 Chronicles 4:22", "Genesis 38:5", "Joshua 15:44"],
        "sections": []
    },
    "christ": {
        "id": "christ",
        "term": "Christ",
        "category": "concepts",
        "intro": "<p>Christ is the Greek translation (Christos, <em>anointed</em>) of the Hebrew title <em>Messiah</em> (<em>Mashiach</em>), meaning <em>anointed one</em>. In the Old Testament, anointing with oil consecrated prophets, priests, and kings to their offices, and the expectation of a supreme anointed figure who would fulfill all three roles developed progressively through the prophetic tradition. The title crystallized in passages like Psalm 2, Daniel 9:25–26, and Isaiah 61:1, which Jesus himself applied to his ministry (Luke 4:18–21). In the New Testament, Jesus of Nazareth is identified as this Christ from the opening verse of Mark (<em>the beginning of the gospel of Jesus Christ</em>) through the testimony of Peter's great confession (<em>You are the Christ</em>, Matt. 16:16) and the post-resurrection proclamation of Acts (Acts 17:3; 18:5).</p><p>The title is so closely linked to Jesus in the New Testament that it functions almost as a second personal name (Jesus Christ / Christ Jesus), though the earliest Christian preaching preserved its titular force: <em>God has made him both Lord and Christ</em> (Acts 2:36). Paul's letters consistently use Christ in the titular sense while also employing the compound name, and his theology of union <em>in Christ</em> made the title central to his entire account of salvation. The risen Jesus as Christ is understood to be the fulfillment of all Old Testament covenant expectation.</p>",
        "hitchcock_meaning": "anointed",
        "source_ids": {"easton": "christ", "smith": "christ"},
        "key_refs": ["Acts 17:3", "Acts 18:5", "Matthew 22:42", "Genesis 3:15", "Genesis 22:18"],
        "sections": []
    },
    "christian": {
        "id": "christian",
        "term": "Christian",
        "category": "concepts",
        "intro": "<p>Christian is the name given to the followers of Jesus Christ, first at Antioch in Syria (Acts 11:26), where the disciples were called Christians apparently by the Gentile population — a name that may have begun as a designation or even a term of mockery but was rapidly adopted by believers themselves. The word occurs only three times in the New Testament: in Acts 11:26 (origin at Antioch), Acts 26:28 (Agrippa's ironic response to Paul: <em>Almost you persuade me to become a Christian</em>), and 1 Peter 4:16 (<em>if anyone suffers as a Christian, let him not be ashamed</em>). The formation of the name — Christ followed by the Latin suffix <em>-ianus</em> — follows the pattern of other party names in the Greco-Roman world (Herodians, Caesareans), suggesting it was coined in a context familiar with Roman naming conventions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "christian", "smith": "christian", "isbe": "christian"},
        "key_refs": ["Acts 11:26", "Acts 26:28", "1 Peter 4:16"],
        "sections": []
    },
    "christs-false": {
        "id": "christs-false",
        "term": "Christs, False",
        "category": "concepts",
        "intro": "<p>False Christs (Greek <em>pseudochristoi</em>) are individuals who would present themselves as the Messiah, whose appearance Jesus warned would accompany and precede the end of the age. In the Olivet Discourse, Jesus cautioned his disciples: <em>Many will come in my name, saying, I am the Christ, and they will lead many astray</em> (Matt. 24:5, 24; Mark 13:6, 21–22). He warned that the signs and wonders performed by false Christs and false prophets would be so convincing as to <em>deceive, if possible, even the elect</em>, and he instructed his followers not to believe claims of a secret location for the returning Christ (Matt. 24:23–26). The warning reflects the heightened messianic expectation of first-century Judaism and the genuine danger of prophetic imposture in a climate of apocalyptic ferment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "christs-false", "isbe": "christs-false"},
        "key_refs": ["Matthew 24:24"],
        "sections": []
    },
    "chronicles": {
        "id": "chronicles",
        "term": "Chronicles",
        "category": "concepts",
        "intro": "<p>Chronicles in the general Old Testament sense refers to the <em>words of the days</em> (Hebrew <em>dibre hayyamim</em>) — annalistic records of events maintained in the courts of Israel and Judah. References to the <em>book of the chronicles of the kings of Israel</em> and <em>of Judah</em> appear throughout Kings as sources for further reading (e.g., 1 Kgs. 14:19; 15:7). These were official state records, distinct from the canonical books of Chronicles but related to them as source material. The <em>book of the chronicles of king David</em> (1 Chr. 27:24) was a particular register of census and administrative data. The canonical books of 1 and 2 Chronicles draw on these and other sources to provide a theological retelling of Israel's history from Adam to the edict of Cyrus.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chronicles"},
        "key_refs": ["1 Kings 14:19", "1 Chronicles 27:24"],
        "sections": []
    },
    "chronicles-of-king-david": {
        "id": "chronicles-of-king-david",
        "term": "Chronicles of King David",
        "category": "concepts",
        "intro": "<p>The Chronicles of King David (1 Chr. 27:24) refers to a specific official register or record book associated with David's census and military organization — the statistical state records maintained by Joab the commander but never completed because the census provoked divine anger before it was finished. This document is distinct from the canonical books of Chronicles but represents one of the court archives that formed the historical source material used by later compilers of Israel's history, including the Chronicler himself. The reference illustrates the existence of a rich archival tradition in ancient Israel alongside the canonical historical books.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chronicles-of-king-david"},
        "key_refs": ["1 Chronicles 27:24"],
        "sections": []
    },
    "chronicles-books-of": {
        "id": "chronicles-books-of",
        "term": "Chronicles, Books of",
        "category": "concepts",
        "intro": "<p>The Books of Chronicles (originally one book in the Hebrew canon, where they were titled <em>dibre hayyamim</em> — <em>words of the days</em>) provide a retelling of Israel's history from Adam's genealogy to the edict of Cyrus permitting the return from Babylon (538 BC). The Septuagint's title <em>Paraleipomena</em> (<em>things omitted</em>) reflected the view that Chronicles supplemented Kings, but modern scholarship recognizes it as a distinct theological work with its own emphases rather than merely a supplement.</p><p>The Chronicler's focus falls almost entirely on Judah and the Davidic dynasty, with the northern kingdom of Israel receiving minimal treatment. The books give substantial attention to the organization of Levitical worship, the temple, and the roles of priests and musicians — suggesting a post-exilic community concerned with restoring proper worship. David's preparations for the temple occupy as much space as his political and military achievements. The books conclude with Cyrus's proclamation, linking the history of Israel's covenant God to the movement of world empires and setting the stage for Ezra and Nehemiah.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chronicles-books-of", "isbe": "chronicles-books-of"},
        "key_refs": ["1 Chronicles 3:19", "1 Chronicles 27:24", "1 Chronicles 29:29", "2 Chronicles 9:29", "2 Chronicles 12:15"],
        "sections": []
    },
    "chronology": {
        "id": "chronology",
        "term": "Chronology",
        "category": "concepts",
        "intro": "<p>Biblical chronology is the arrangement of the events and persons of Scripture in their temporal sequence. The task is complicated by the variety of dating systems used in the ancient Near East, the use of both lunar and solar calendars, co-regencies between kings (where a son ruled alongside his father before the father's death), and apparent discrepancies between the numbers given in Kings and Chronicles. Key chronological anchors include the fixed dates of Assyrian and Babylonian records (particularly the Assyrian eponym lists and the Chronicle of Nabonassar) that can be correlated with biblical events such as the fall of Samaria (722 BC) and the destruction of Jerusalem (586 BC).</p><p>The date of the exodus from Egypt has been debated extensively, with proposals ranging from the fifteenth to the thirteenth century BC, dependent on the interpretation of the <em>four hundred and eighty years</em> of 1 Kings 6:1 and on archaeological evidence from Canaan. New Testament chronology similarly involves debate over the precise year of Jesus's birth, the length of his ministry, and the dates of Paul's missionary journeys — all set within the framework of datable Roman and Herodian history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chronology", "smith": "chronology"},
        "key_refs": ["Numbers 1:1", "Numbers 33:38", "1 Kings 6:1", "1 Kings 15:1", "1 Kings 15:9"],
        "sections": []
    },
    "chrysoprasus": {
        "id": "chrysoprasus",
        "term": "Chrysoprasus",
        "category": "concepts",
        "intro": "<p>Chrysoprasus (Greek <em>chrysoprasos</em>, meaning <em>golden leek</em>) is mentioned once in Scripture as the tenth of the twelve stones in the foundations of the New Jerusalem's walls (Rev. 21:20). In antiquity the term referred to a golden-green variety of stone, possibly a green nickel-bearing chalcedony or an apple-green variety of quartz. The color of leek's juice — a fresh yellow-green — gives the stone its Greek name. Like the other foundation stones of Revelation 21, it echoes the gemstones of the high priest's breastplate and the jewels of Eden's garden described in Ezekiel 28:13, pointing to continuity between the tabernacle symbolism and the heavenly city.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chrysoprasus"},
        "key_refs": ["Revelation 21:20"],
        "sections": []
    },
    "chub": {
        "id": "chub",
        "term": "Chub",
        "category": "concepts",
        "intro": "<p>Chub appears in Ezekiel 30:5 in a prophetic oracle against Egypt, listed among Egypt's allies who would fall together under the coming judgment of Nebuchadnezzar: <em>Cush, and Put, and Lud, and all Arabia, and Libya, and the people of the land that is in league, shall fall with them by the sword</em>. Some Hebrew manuscripts and translations read <em>Chub</em> as a variant of <em>Libya</em> (Lub) or as an otherwise unknown North African or Near Eastern people. The Septuagint omits the name or reads it differently. Its precise identification remains uncertain, but it belongs to the catalog of African and Near Eastern nations whose fortunes were bound up with Egypt's in the prophetic vision of Babylonian conquest.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "chub", "smith": "chub", "isbe": "chub"},
        "key_refs": ["Ezekiel 30:5"],
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
    print(f'BP Article Synthesis — c2: Centurion → Chub: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
