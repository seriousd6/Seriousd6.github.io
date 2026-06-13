import json, os, pathlib

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    return json.loads(p.read_text()) if p.exists() else None

def save_article(slug, data):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "misheal": {
        "id": "misheal", "term": "Misheal", "category": "places",
        "hitchcock_meaning": "requiring; lent; pit",
        "source_ids": {"easton": "misheal", "isbe": "misheal"},
        "key_refs": ["Joshua 19:26"],
        "intro": "<p>Misheal (also spelled Mishal or Mashal) was a town assigned to the tribe of Asher in the division of Canaan under Joshua (Josh. 19:26). It lay in the coastal lowland region of Asher and was later designated as one of the Levitical cities given to the Gershonite clan (Josh. 21:30; 1 Chr. 6:74, where it appears as Mashal). Its precise location in the modern landscape has not been definitively established, though it is generally sought in the area south of Acre (Acco) near the Carmel range. The town illustrates the systematic distribution of territory among the tribes and the provision made for the Levites who received no tribal inheritance of their own but were settled in cities distributed throughout Israel's holdings.</p>"
    },
    "mishma": {
        "id": "mishma", "term": "Mishma", "category": "people",
        "hitchcock_meaning": "hearing; obeying",
        "source_ids": {"easton": "mishma", "smith": "mishma", "isbe": "mishma"},
        "key_refs": ["Genesis 25:14", "1 Chronicles 4:25", "1 Chronicles 4:26"],
        "intro": "<p>Mishma (meaning <em>hearing</em>) is the name of two men in the Old Testament. The first was one of the twelve sons of Ishmael, the son of Abraham and Hagar (Gen. 25:14; 1 Chr. 1:30), and thus the founder of an Arab tribe bearing his name. The second Mishma was a Simeonite, the son of Mibsam and the father of Hammuel (1 Chr. 4:25–26). The Simeonite line of Mishma may represent a tribal family that had absorbed the earlier Ishmaelite clan name, reflecting the intermingling of Semitic peoples in the Negev region. The name itself recalls the importance of hearing and obedience as virtues in Hebrew culture, though neither biblical figure is remembered for any specific deed beyond the genealogical record.</p>"
    },
    "mishmannah": {
        "id": "mishmannah", "term": "Mishmannah", "category": "people",
        "hitchcock_meaning": "fatness; taking away provision",
        "source_ids": {"easton": "mishmannah", "smith": "mishmannah", "isbe": "mishmannah"},
        "key_refs": ["1 Chronicles 12:10"],
        "intro": "<p>Mishmannah (meaning <em>fatness</em> or <em>strength</em>) was one of the Gadite warriors who crossed the Jordan to join David at Ziklag during the period when Saul was still king (1 Chr. 12:10). These Gadites are described in striking terms: their faces were like lions' faces, and they were as swift as gazelles on the mountains (1 Chr. 12:8). Mishmannah is listed fourth in the roll of honor, ranked among the chiefs or commanders of his band. His joining David at a time of political danger illustrates the gathering of military support that eventually led to David's unchallenged kingship over all Israel. Beyond this genealogical and military notice, nothing further is recorded of him in Scripture.</p>"
    },
    "misrephoth-maim": {
        "id": "misrephoth-maim", "term": "Misrephoth-maim", "category": "places",
        "hitchcock_meaning": "hot waters",
        "source_ids": {"easton": "misrephoth-maim", "isbe": "misrephoth-maim"},
        "key_refs": ["Joshua 11:8", "Joshua 13:6"],
        "intro": "<p>Misrephoth-maim (meaning <em>burning of waters</em> or <em>hot waters</em>) was a site on the northern coastal plain of Canaan to which Joshua pursued the forces of the Canaanite coalition under King Jabin of Hazor after the decisive battle near the waters of Merom (Josh. 11:8). The exact nature of the place is debated: the name may refer to salt-pans, lime-kilns, or glass-works where water was heated, all of which were attested industries on the Lebanese coast in antiquity. It is also mentioned in Josh. 13:6 as lying within the territory that remained to be subdued in the north. The site is tentatively identified with Khirbet el-Musheirifeh, a ruin near the promontory of en-Nakhurah, approximately eleven miles north of Acre on the Phoenician coast.</p>"
    },
    "mite": {
        "id": "mite", "term": "Mite", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mite", "smith": "mite", "isbe": "mite"},
        "key_refs": ["Luke 21:2", "Luke 12:59", "Mark 12:42"],
        "intro": "<p>The mite (Greek <em>lepton</em>, meaning <em>thin</em> or <em>small</em>) was the smallest coin in circulation in first-century Judea, equivalent to one-eighth of a Roman as or approximately one sixty-fourth of a denarius. Two mites made one quadrans (the Latin farthing), the smallest Roman copper coin. The mite's primary significance in Scripture comes from Jesus' commendation of the poor widow who cast two mites — her entire livelihood — into the temple treasury (Mark 12:41–44; Luke 21:1–4). Jesus held her offering as exceeding all others, since the wealthy gave out of abundance while she gave out of poverty. The passage has made the \"widow's mite\" a proverbial expression for sacrificial giving. The coin also appears in Luke 12:59, where it marks the extreme end of a debt that must be paid in full.</p>"
    },
    "mithcah": {
        "id": "mithcah", "term": "Mithcah", "category": "places",
        "hitchcock_meaning": "sweetness; pleasantness",
        "source_ids": {"easton": "mithcah", "smith": "mithcah"},
        "key_refs": ["Numbers 33:28", "Numbers 33:29"],
        "intro": "<p>Mithcah (meaning <em>sweetness</em> or <em>pleasantness</em>) was one of the wilderness stations where the Israelites camped during their forty-year journey from Egypt to Canaan (Num. 33:28–29). It appears in the itinerary between Terah and Hashmonah in the lists recorded in Numbers 33, which catalogs the successive stopping points of the Exodus generation. The site cannot be identified with certainty in the modern landscape, as many of the wilderness stations remain archaeologically unlocated. The name's pleasant connotation may reflect a natural feature — perhaps a spring or oasis — that made it a welcome respite in the desert wilderness. As with most wilderness stations, Mithcah is significant primarily as a marker of Israel's providential journey under divine guidance toward the Promised Land.</p>"
    },
    "mithredath": {
        "id": "mithredath", "term": "Mithredath", "category": "people",
        "hitchcock_meaning": "breaking the law",
        "source_ids": {"easton": "mithredath", "smith": "mithredath", "isbe": "mithredath"},
        "key_refs": ["Ezra 1:8", "Ezra 4:7"],
        "intro": "<p>Mithredath (a Persian name meaning <em>given by Mithra</em>, the sun deity, equivalent to the Greek Mithridates) is the name of two Persian officials mentioned in the book of Ezra. The first was the treasurer of King Cyrus who, by royal command, counted out and delivered to Sheshbazzar the prince of Judah the gold and silver vessels that Nebuchadnezzar had taken from the Jerusalem temple (Ezra 1:8). The second Mithredath was a Persian officer stationed in Samaria who, together with Bishlam and Tabeel, wrote a letter of complaint to King Artaxerxes opposing the rebuilding of Jerusalem (Ezra 4:7). The two men represent contrasting postures toward the Jewish restoration: the first a servant of Cyrus's benevolent decree, the second an active opponent of the returned exiles' building program.</p>"
    },
    "mitre": {
        "id": "mitre", "term": "Mitre", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mitre", "smith": "mitre", "isbe": "mitre"},
        "key_refs": ["Exodus 28:4", "Exodus 28:37", "Exodus 29:6", "Leviticus 8:9"],
        "intro": "<p>The mitre (Hebrew <em>mitsnepheth</em>, meaning something <em>wound round</em>) was the distinctive turban or head-dress of the Israelite high priest, prescribed as part of the sacred vestments in Exodus 28:4. It consisted of a band of fine white linen approximately eight yards in length, wound into the form of a cap and fitted upon the head. Attached to the front of the mitre by a blue cord was a golden plate engraved with the words <em>HOLINESS TO THE LORD</em> (Ex. 28:36–38; 39:30), which Aaron was to wear on his forehead whenever he entered the sanctuary, bearing the iniquity of the holy offerings that Israel presented to God. The mitre was conferred on Aaron at his consecration by Moses (Lev. 8:9) and distinguished the high priest from ordinary priests, who wore simpler caps (<em>migbaoth</em>). In Ezekiel 21:26 the same Hebrew word is translated \"diadem,\" indicating its royal as well as priestly connotations.</p>"
    },
    "mitylene": {
        "id": "mitylene", "term": "Mitylene", "category": "places",
        "hitchcock_meaning": "purity; cleansing; press",
        "source_ids": {"easton": "mitylene", "smith": "mitylene", "isbe": "mitylene"},
        "key_refs": ["Acts 20:14"],
        "intro": "<p>Mitylene (modern Mytilene) was the chief city of the island of Lesbos, located on the island's eastern coast in the northern Aegean Sea. The city was renowned in antiquity as a center of culture and learning; the poets Sappho and Alcaeus were among its most famous natives. Paul touched at Mitylene during his third missionary journey while sailing from Corinth to Judea (Acts 20:14), having sailed past Ephesus to avoid losing time there. He arrived at Mitylene after crossing from Assos, and spent a night there before continuing southward to Chios and Samos. The city is today still known as Mytilene and remains the capital of the island of Lesbos. Its mention in Acts reflects the well-traveled Aegean sea route that Paul regularly used in his missionary travels between Macedonia and Syria.</p>"
    },
    "mixed-multitude": {
        "id": "mixed-multitude", "term": "Mixed multitude", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mixed-multitude", "smith": "mixed-multitude", "isbe": "mixed-multitude"},
        "key_refs": ["Exodus 12:38", "Nehemiah 13:3", "Numbers 11:4"],
        "intro": "<p>The mixed multitude (Hebrew <em>erev rav</em>, literally <em>a great mixture</em>) refers to the non-Israelite population that left Egypt alongside the Israelites at the Exodus (Ex. 12:38). These were likely Egyptians of lower social standing, descendants of the Hyksos, enslaved peoples of other nationalities, or others who attached themselves to the departing Hebrews out of fear or opportunity. Their presence became a source of spiritual danger in the wilderness: Numbers 11:4 attributes the craving for meat that sparked the Israelites' murmuring partly to the \"rabble\" or mixed multitude. Their appetite for Egyptian food undermined confidence in God's provision. In the post-exilic period, Nehemiah separated the mixed multitude from the assembly of Israel as part of the covenant renewal (Neh. 13:3), reflecting the ongoing concern to maintain the distinctiveness of the covenant community from surrounding peoples.</p>"
    },
    "mizar": {
        "id": "mizar", "term": "Mizar", "category": "places",
        "hitchcock_meaning": "little",
        "source_ids": {"easton": "mizar", "smith": "mizar"},
        "key_refs": ["Psalms 42:6"],
        "intro": "<p>Mizar (meaning <em>little</em>) is a hill or summit mentioned once in Scripture, in the lament of Psalm 42:6, where the psalmist writes: <em>My soul is cast down within me; therefore I remember you from the land of Jordan and of Hermon, from Mount Mizar.</em> The precise location of Mizar is uncertain, but the context suggests a lesser elevation in the vicinity of the Jordan River headwaters and the Anti-Lebanon range, possibly one of the lower spurs of Hermon. The name's meaning — \"little\" — contrasts it with the towering heights of Lebanon and Hermon nearby. Some scholars identify it with Jebel Ajlun east of the Jordan. The reference appears to be autobiographical: the psalmist, exiled and cut off from the sanctuary in Jerusalem, recalls the landscape of the north as he pours out his soul in longing for God's presence.</p>"
    },
    "mizpah": {
        "id": "mizpah", "term": "Mizpah", "category": "places",
        "hitchcock_meaning": "a watch-tower; speculation",
        "source_ids": {"easton": "mizpah", "smith": "mizpah"},
        "key_refs": ["Genesis 31:49", "Judges 11:11", "1 Samuel 7:5", "1 Kings 15:22"],
        "intro": "<p>Mizpah (also Mizpeh, meaning <em>watch-tower</em> or <em>look-out</em>) was the name given to several distinct locations in biblical Israel. The most famous was Mizpah of Gilead, east of the Jordan, where Laban and Jacob set up a cairn of stones as a covenant memorial (Gen. 31:49), giving the site its name with the blessing \"the LORD watch between me and thee.\" This same Gilead Mizpah became associated with Jephthah, who made his ill-fated vow there and from it led Israel against the Ammonites (Judg. 11:11, 34). A second Mizpah in Benjamin served as a major national assembly point: Samuel gathered Israel there for prayer and renewal (1 Sam. 7:5–12), and later it was the scene of Saul's election as king (1 Sam. 10:17). After the fall of Jerusalem it became the seat of Gedaliah's governorship (2 Kings 25:23). This Benjaminite Mizpah is generally identified with Tell en-Nasbeh, eight miles north of Jerusalem.</p>"
    },
    "mizpar": {
        "id": "mizpar", "term": "Mizpar", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mizpar", "smith": "mizpar", "isbe": "mizpar"},
        "key_refs": ["Ezra 2:2", "Nehemiah 7:7"],
        "intro": "<p>Mizpar (also spelled Mispereth in Nehemiah 7:7) was one of the leading men who returned with Zerubbabel and Jeshua from the Babylonian exile in the first wave of restoration under Cyrus's decree (Ezra 2:2). He is listed among the eleven principal leaders of the return, a company that also included Nehemiah and Mordecai, who are named before and after him in the parallel lists. The name Mizpar means <em>number</em> or <em>writing</em>, though nothing beyond the genealogical register connects him to any specific action in the restoration narrative. His presence in both the Ezra and Nehemiah lists confirms the historical reliability of the roster of returnees and situates him among the founding generation of the Second Temple community.</p>"
    },
    "mizraim": {
        "id": "mizraim", "term": "Mizraim", "category": "places",
        "hitchcock_meaning": "tribulations",
        "source_ids": {"easton": "mizraim", "isbe": "mizraim"},
        "key_refs": ["Genesis 10:6", "Genesis 10:13", "1 Chronicles 1:8", "1 Chronicles 1:11"],
        "intro": "<p>Mizraim is the standard Hebrew name for Egypt, derived from a dual form of the root <em>matzor</em> meaning <em>fortress</em> or <em>enclosure</em>, possibly reflecting the two great divisions of Upper and Lower Egypt. In the Table of Nations, Mizraim is listed as a son of Ham and grandson of Noah (Gen. 10:6), representing Egypt as a people descended from the Hamitic line. His sons — Ludim, Anamim, Lehabim, Naphtuhim, Pathrusim, Casluhim, and Caphtorim — are understood as the ancestor-eponyms of various peoples connected with Egypt and the eastern Mediterranean (Gen. 10:13–14; 1 Chr. 1:11–12). The dual form of the name (<em>Mizrayim</em> in Hebrew) may preserve a memory of Egypt's ancient division into two kingdoms unified under Menes around 3100 BC. The modern Arabic name for Egypt, <em>Misr</em>, preserves a close phonetic echo of the ancient Hebrew designation.</p>"
    },
    "mizzah": {
        "id": "mizzah", "term": "Mizzah", "category": "people",
        "hitchcock_meaning": "defluxion from the head",
        "source_ids": {"easton": "mizzah", "smith": "mizzah", "isbe": "mizzah"},
        "key_refs": ["Genesis 36:13", "Genesis 36:17"],
        "intro": "<p>Mizzah was one of the four sons of Reuel, who was himself the son of Esau and his wife Basemath (Gen. 36:13). Mizzah thus belonged to the third generation of Esau's Edomite descendants, and along with his brothers Nahath, Zerah, and Shammah he is counted among the chiefs or clan-leaders of Edom (Gen. 36:17; 1 Chr. 1:37). The name Mizzah appears to mean <em>despair</em> or a form of bodily ailment in Hitchcock's interpretation, though the etymology is uncertain. Like most of the Edomite chiefs in Genesis 36, Mizzah is recorded without narrative detail; his significance lies in his position within the genealogical framework that traces the fulfillment of God's promise that Esau too would become a great nation (Gen. 25:23; 36:31–39).</p>"
    },
    "mnason": {
        "id": "mnason", "term": "Mnason", "category": "people",
        "hitchcock_meaning": "a diligent seeker; an exhorter",
        "source_ids": {"easton": "mnason", "smith": "mnason", "isbe": "mnason"},
        "key_refs": ["Acts 21:16"],
        "intro": "<p>Mnason was a Christian of Cyprus and an \"old\" (or early) disciple — that is, one who had been a follower of Jesus since the earliest days of the Church — with whom Paul lodged when he arrived in Jerusalem at the close of his third missionary journey (Acts 21:16). The Caesarean disciples accompanied Paul and brought him to Mnason's house, indicating that Mnason was a known and trusted member of the Jerusalem Christian community. His Cypriot origin links him to the same island that produced Barnabas (Acts 4:36), and the early wave of Cypriot believers who had played an important role in spreading the gospel to Antioch (Acts 11:19–20). The description of him as an \"early disciple\" (R.V.) may indicate that he had been a follower of Jesus during his earthly ministry or had been converted at Pentecost. He provided Paul hospitality at a moment of considerable tension (Acts 21:17–22).</p>"
    },
    "moab": {
        "id": "moab", "term": "Moab", "category": "places",
        "hitchcock_meaning": "of his father",
        "source_ids": {"easton": "moab", "smith": "moab"},
        "key_refs": ["Genesis 19:37", "Numbers 22:3", "Ruth 1:4", "Jeremiah 48:11"],
        "intro": "<p>Moab refers to both the eponymous ancestor of the Moabite people and the territory they inhabited east of the Dead Sea. Moab was the son born to Lot by his elder daughter after the destruction of Sodom (Gen. 19:37), and the nation traced its descent from this morally compromised origin. The land of Moab lay east of the Jordan and the Dead Sea, south of the Arnon River, bounded by Edom to the south and the Ammonites to the northeast. It was a high tableland of fertile pasture, famous for its sheep and wool (2 Kings 3:4). Israel's relationship with Moab was complex: though forbidden to attack Moab in the wilderness (Deut. 2:9) because of the Lot connection, Israel was later oppressed by Moab under Eglon (Judg. 3:12–30), and the Moabites were excluded from the congregation to the tenth generation (Deut. 23:3). Yet Ruth, the Moabite ancestress of David and ultimately of Jesus, is the most celebrated individual from that nation.</p>"
    },
    "moabite": {
        "id": "moabite", "term": "Moabite", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moabite"},
        "key_refs": ["Genesis 19:37", "Deuteronomy 23:3", "Ruth 1:4", "Nehemiah 13:1"],
        "intro": "<p>The Moabites were the people descended from Moab, the son of Lot (Gen. 19:37), who inhabited the plateau east of the Dead Sea between the Arnon and Zered rivers. From their original territory they expanded northward over land formerly held by the Amorites. Moabite religion centered on the national deity Chemosh, to whom human sacrifices were made (2 Kings 3:27). The Mosaic law excluded Moabites from the assembly of Israel to the tenth generation because of their hostility during the Exodus and their hiring of Balaam to curse Israel (Deut. 23:3–4; Neh. 13:1). Despite this exclusion, Ruth the Moabitess became the great-grandmother of David through her loyalty to Naomi and her confession of Israel's God (Ruth 1:16), and is listed in the genealogy of Jesus (Matt. 1:5). The prophets frequently addressed oracles against Moab (Isa. 15–16; Jer. 48; Amos 2:1–3), yet also held out the prospect of Moab's ultimate humbling and partial restoration.</p>"
    },
    "moabite-stone": {
        "id": "moabite-stone", "term": "Moabite Stone", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moabite-stone", "isbe": "moabite-stone"},
        "key_refs": ["2 Kings 3:4", "2 Kings 3:5"],
        "intro": "<p>The Moabite Stone (also known as the Mesha Stele) is a basalt inscription erected by Mesha, king of Moab, discovered at Dibon (biblical Dibon-Gad) by the German missionary F.A. Klein in 1868. The stone stands approximately 3½ feet high and 2 feet wide, rounded at the top, and bears thirty-four lines of text written in a script closely related to archaic Hebrew (Phoenician-Hebrew alphabet). It is one of the most significant extra-biblical archaeological discoveries relating to Old Testament history. The inscription records Mesha's victories over Israel, his public building projects, and his wars on other frontiers — all undertaken, he declares, at the command of Chemosh, the Moabite national god. The stone directly corroborates and supplements the account of 2 Kings 3:4–5, where Mesha the sheep-master is described as rebelling against Israel after Ahab's death. The stele is now housed in the Louvre in Paris.</p>"
    },
    "moladah": {
        "id": "moladah", "term": "Moladah", "category": "places",
        "hitchcock_meaning": "birth; generation",
        "source_ids": {"easton": "moladah", "smith": "moladah", "isbe": "moladah"},
        "key_refs": ["Joshua 15:26", "Joshua 19:2", "Nehemiah 11:26"],
        "intro": "<p>Moladah (meaning <em>birth</em> or <em>generation</em>) was a town in the southern district of Judah that was subsequently allocated to the tribe of Simeon within Judah's territory (Josh. 15:26; 19:2). It is listed among the southernmost cities near Beersheba in the Negev region. After the Babylonian exile, Moladah was resettled by returning Jews from the tribe of Judah (Neh. 11:26), confirming its continued importance as a settled community in the post-exilic south. The site is tentatively identified with the modern village of Khirbet el-Waten (or el-Milh), situated approximately ten miles east of Beersheba. As a Simeonite city within Judah's allotment, Moladah illustrates the pattern by which the small tribe of Simeon received scattered towns within the already-settled inheritance of Judah (Josh. 19:1).</p>"
    },
    "mole": {
        "id": "mole", "term": "Mole", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mole", "smith": "mole", "isbe": "mole"},
        "key_refs": ["Leviticus 11:30", "Isaiah 2:20"],
        "intro": "<p>Several Hebrew words are rendered \"mole\" or related burrowing creatures in English translations of the Old Testament, reflecting the difficulty of precisely identifying ancient fauna. The Hebrew <em>tinshameth</em> in Leviticus 11:30, listed among unclean animals, is rendered \"mole\" in the Authorized Version but \"chameleon\" in the Revised Version — likely denoting some species of lizard. The Hebrew <em>holed</em> in Leviticus 11:29, rendered \"weasel\" in most translations, may refer to the mole-rat (<em>Spalax typhlus</em>), a burrowing rodent common in Palestine. The true European mole (<em>Talpa europaea</em>) does not range into the Holy Land. Isaiah 2:20 provides the most vivid biblical image: in the day of the LORD's judgment, people will cast their silver and gold idols \"to the moles and to the bats\" — creatures inhabiting dark, hidden places, a fitting image for the worthlessness of idolatry before God's presence.</p>"
    },
    "moloch": {
        "id": "moloch", "term": "Moloch", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moloch", "smith": "moloch", "isbe": "moloch"},
        "key_refs": ["1 Kings 11:7", "2 Kings 23:10", "Amos 5:26", "Acts 7:43"],
        "intro": "<p>Moloch (also Molech; from Hebrew <em>melek</em>, <em>king</em>) was the chief national deity of the Ammonites, worshipped through the sacrifice of children burned in fire. The name combines the consonants of <em>melek</em> (king) with the vowels of <em>bosheth</em> (shame), a deliberate scribal stigma applied by Hebrew writers. Moloch worship was one of the most condemned practices in the Old Testament: the law explicitly forbade Israelites from offering their children to Moloch (Lev. 18:21; 20:2–5), on pain of death. Despite this prohibition, Solomon erected a high place for Moloch on the Mount of Olives as part of his accommodation to his foreign wives (1 Kings 11:7), and the cult persisted through the monarchy, with children burned at Topheth in the Valley of Hinnom (2 Kings 23:10). King Josiah defiled Topheth to end the practice (2 Kings 23:13). The prophets Stephen quotes Amos 5:26 in Acts 7:43 to indict Israel's wilderness-era idolatry, applying a tradition that Moloch worship had deeper roots than the monarchy period.</p>"
    },
    "money": {
        "id": "money", "term": "Money", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "money", "smith": "money", "isbe": "money"},
        "key_refs": ["Genesis 23:16", "Genesis 33:19", "Matthew 22:19", "1 Timothy 6:10"],
        "intro": "<p>In the Old Testament, money primarily took the form of uncoined precious metals — silver and gold — weighed out in transactions rather than counted as stamped coinage. The earliest biblical references mention Abraham's wealth in silver (Gen. 13:2) and the purchase of the cave of Machpelah for four hundred shekels of silver weighed according to the merchant's standard (Gen. 23:16). The shekel was the principal unit of weight, with sixty gerahs to the shekel. Coined money was introduced into the Near East in the seventh century BC by the Lydians; Persian coins (<em>darics</em> and <em>drachmas</em>) appear in post-exilic texts (Ezra 2:69; Neh. 7:70). In the New Testament period, the monetary system was mixed: Roman denarii, Greek drachmas, and Jewish shekels and temple currency all circulated, requiring the services of money-changers. The love of money, rather than money itself, is identified by Paul as a root of all kinds of evil (1 Tim. 6:10).</p>"
    },
    "money-changer": {
        "id": "money-changer", "term": "Money-changer", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "money-changer"},
        "key_refs": ["Matthew 21:12", "Mark 11:15", "John 2:15", "Exodus 30:13"],
        "intro": "<p>Money-changers were traders who set up tables in the outer courts of the Jerusalem temple to exchange foreign currency for the Jewish or Tyrian shekel required for payment of the annual half-shekel temple tax (Ex. 30:13–15; Matt. 17:24). Since the Mosaic law stipulated this offering in a specific coinage, pilgrims arriving from throughout the diaspora needed to convert their Roman, Greek, Egyptian, or other currencies, and the money-changers charged a premium for the exchange. Jesus twice drove out the money-changers from the temple courts (at the beginning of his ministry in John 2:13–17, and at the end in Matt. 21:12–13 and parallels), overturning their tables and accusing them of making the house of prayer into \"a den of thieves\" — citing Jeremiah 7:11 and Isaiah 56:7. The episode reflects both Jesus' zeal for the sanctity of temple worship and his prophetic indictment of commercial exploitation of pilgrims in the sacred precinct.</p>"
    },
    "month": {
        "id": "month", "term": "Month", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "month", "smith": "month", "isbe": "month"},
        "key_refs": ["Genesis 7:11", "1 Kings 4:7", "Colossians 2:16"],
        "intro": "<p>The Hebrew calendar was lunar, with each month beginning at the appearance of the new moon. A lunar month of approximately 29½ days was the basic unit, resulting in years of 354 days that required periodic intercalation of an additional month to keep the calendar aligned with the agricultural seasons. The Mosaic law tied the religious calendar closely to the monthly cycle: the new moon itself was marked by special offerings (Num. 28:11–15) and the blowing of trumpets (Num. 10:10; Ps. 81:3), and major festivals fell on the tenth (Day of Atonement), fourteenth (Passover), or fifteenth (Firstfruits, Tabernacles) of specific months. The first month (<em>Abib</em> or <em>Nisan</em>) was established at the Exodus as the beginning of the sacred year (Ex. 12:2). Later, Babylonian month-names were adopted in the post-exilic period. Paul warns against making observance of months a matter of religious obligation (Gal. 4:10; Col. 2:16), since Christ has fulfilled the shadow of the ceremonial calendar.</p>"
    },
    "moon": {
        "id": "moon", "term": "Moon", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moon", "smith": "moon", "isbe": "moon"},
        "key_refs": ["Genesis 1:16", "Psalms 104:19", "Isaiah 60:20", "Revelation 21:23"],
        "intro": "<p>The moon (Hebrew <em>yareah</em> from its paleness, and <em>lebana</em>, <em>the white one</em>) was appointed by God at creation to govern the night and to serve as a sign for seasons, days, and years alongside the sun (Gen. 1:14–16; Ps. 104:19). In the Israelite calendar the lunar cycle determined the months and religious feasts, and the new moon was marked with special offerings and rest (Num. 28:11–15; Amos 8:5). The Psalms celebrate the moon's enduring constancy as a witness to God's covenant with David (Ps. 89:37). Prophetic literature frequently pairs the dimming of the moon with cosmic judgment preceding the Day of the LORD (Isa. 24:23; Joel 2:31; Matt. 24:29), while eschatological passages envision a time when the moon's light will be superseded by the direct glory of God (Isa. 60:19–20; Rev. 21:23). Worship of the moon was strictly forbidden in Israel (Deut. 4:19; 2 Kings 23:5), though such veneration was common among surrounding nations.</p>"
    },
    "mordecai": {
        "id": "mordecai", "term": "Mordecai", "category": "people",
        "hitchcock_meaning": "contrition; bitter; bruising",
        "source_ids": {"easton": "mordecai", "smith": "mordecai", "isbe": "mordecai"},
        "key_refs": ["Esther 2:5", "Esther 3:2", "Esther 8:1", "Esther 10:3"],
        "intro": "<p>Mordecai, son of Jair of the tribe of Benjamin and a descendant of the exiles carried to Babylon under Nebuchadnezzar, was the Jewish guardian and cousin of Esther who became the deliverer of the Jewish people in Persia. Residing in Susa, the Persian capital, he had adopted his orphaned cousin Hadassah (Esther) as his own daughter. When Esther was chosen queen by Ahasuerus (Xerxes), Mordecai maintained a daily watch at the palace gate (Esther 2:11). His discovery and reporting of a plot against the king's life (Esther 2:21–23) went unrewarded at the time but proved decisive later. His refusal to bow to Haman the Agagite — motivated by loyalty to his Jewish identity — provoked Haman's genocidal decree against all the Jews in the empire (Esther 3:2–6). Mordecai's urgent appeal to Esther produced her courageous intercession, which reversed Haman's edict. Haman was hanged on the gallows he had prepared for Mordecai, who was elevated to prime minister and became great among the Jews and an advocate of his people's welfare (Esther 10:3).</p>"
    },
    "moreh": {
        "id": "moreh", "term": "Moreh", "category": "places",
        "hitchcock_meaning": "stretching",
        "source_ids": {"easton": "moreh", "smith": "moreh"},
        "key_refs": ["Genesis 12:6", "Genesis 12:7", "Deuteronomy 11:30"],
        "intro": "<p>Moreh (meaning <em>teacher</em> or <em>archer</em>, possibly <em>early rain</em>) designates two distinct locations in the Old Testament. The first and better-known is the oak (or terebinth) of Moreh near Shechem, situated in the valley between Mounts Ebal and Gerizim. Here Abraham built his first altar in Canaan after God appeared to him with the promise, \"To your offspring I will give this land\" (Gen. 12:6–7). The site was later referenced in the law as a landmark for Israel's entry into the land (Deut. 11:30). The oak of Moreh at Shechem had sacred associations throughout Israel's history: it was there that Jacob buried foreign idols beneath it (Gen. 35:4) and Joshua erected his memorial stone (Josh. 24:26). The second location, the Hill of Moreh, lay near Jezreel and was the site where the Midianite army camped before Gideon's famous night attack (Judg. 7:1). These two sites share a name but belong to different regions and historical contexts.</p>"
    },
    "moreh-the-hill-of": {
        "id": "moreh-the-hill-of", "term": "Moreh, the Hill of", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moreh-the-hill-of"},
        "key_refs": ["Judges 7:1"],
        "intro": "<p>The Hill of Moreh was a ridge in the Jezreel valley where the Midianite and Amalekite coalition camped before Gideon's famous night attack with his band of three hundred men (Judg. 7:1). It lay to the north of the spring of Harod, where Gideon's forces encamped, so that the Israelite army looked down across the valley toward the vast enemy encampment below. The hill is generally identified with the long ridge known today as Jebel ed-Duhy (Nebi Dahi), also called Little Hermon, which runs parallel to Mount Gilboa on the south, with the plain of Jezreel stretching between them. Gideon's victory there — won by divine strategy rather than military strength, and with his drastically reduced force of three hundred — became a paradigmatic example of God's deliverance against overwhelming odds (Judg. 7:2–22; Heb. 11:32).</p>"
    },
    "moresheth-gath": {
        "id": "moresheth-gath", "term": "Moresheth-gath", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moresheth-gath", "isbe": "moresheth-gath"},
        "key_refs": ["Micah 1:14", "Jeremiah 26:18"],
        "intro": "<p>Moresheth-gath (meaning <em>possession of the wine-press</em>) was a town in the Shephelah (lowland) of Judah, probably situated near or as a suburb of the Philistine city of Gath. It is notable as the birthplace and home of the prophet Micah (Mic. 1:1, 14), who is therefore called the Morasthite (Jer. 26:18). Micah's oracle in 1:14 uses the name of the town in a wordplay lamenting the impending Assyrian invasion. Jeremiah's contemporaries cited Micah of Moresheth's prophecy against Jerusalem (Jer. 26:18–19) as a precedent for prophesying judgment without suffering death, which helped spare Jeremiah when he delivered a similar oracle. The site is commonly identified with Tell el-Judeideh, approximately twenty miles southwest of Jerusalem in the foothills between the coastal plain and the Judean highlands.</p>"
    },
    "moriah": {
        "id": "moriah", "term": "Moriah", "category": "places",
        "hitchcock_meaning": "bitterness of the Lord",
        "source_ids": {"easton": "moriah", "smith": "moriah"},
        "key_refs": ["Genesis 22:2", "2 Chronicles 3:1", "2 Samuel 24:24"],
        "intro": "<p>Moriah (meaning <em>chosen of Jehovah</em> or <em>seen of the LORD</em>) refers to two related but possibly identical locations of supreme sacred significance. The \"land of Moriah\" was the destination God commanded Abraham to travel to in order to offer Isaac as a burnt offering (Gen. 22:2), a three-day journey from Beersheba. The angel of the LORD intervened at the last moment and provided a ram in Isaac's place, and Abraham named the site <em>Jehovah-jireh</em> — \"the LORD will provide\" (Gen. 22:14). The second reference to Moriah identifies it as the site in Jerusalem where Solomon built the temple, on the threshing floor of Ornan (Araunah) the Jebusite that David had purchased after the divine judgment of the census (2 Sam. 24:24–25; 2 Chr. 3:1). The identification of both sites as Moriah suggests a deliberately theological connection: the hill of Abraham's sacrifice became the hill of Israel's sacrifice, and ultimately the hill nearest to Golgotha where the ultimate sacrifice of the Son of God took place.</p>"
    },
    "mortar": {
        "id": "mortar", "term": "Mortar", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mortar", "smith": "mortar", "isbe": "mortar"},
        "key_refs": ["Genesis 11:3", "Exodus 1:14", "Numbers 11:8", "Nahum 3:14"],
        "intro": "<p>The word mortar in the English Bible translates two distinct Hebrew concepts. The first (<em>homer</em> or <em>chomer</em>) refers to cement made of lime and sand or clay used in building construction: the builders of Babel used bitumen as mortar (Gen. 11:3), and the enslaved Israelites in Egypt made mortar as part of their brick-making labor (Ex. 1:14). Nahum's taunt against Nineveh includes the command to \"tread the mortar\" in a last-ditch effort to repair the city's defenses (Nah. 3:14). The second sense of mortar refers to a grinding vessel: a deep bowl in which grain, spices, or other substances are pounded with a pestle. The Israelites in the wilderness ground manna in mortars (Num. 11:8), and Proverbs 27:22 observes that a fool's folly will not depart even if he is ground in a mortar. Both uses reflect essential technologies of ancient Near Eastern daily life.</p>"
    },
    "mosera": {
        "id": "mosera", "term": "Mosera", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mosera"},
        "key_refs": ["Deuteronomy 10:6", "Numbers 33:37", "Numbers 33:38"],
        "intro": "<p>Mosera (meaning <em>a bond</em> or <em>chastisement</em>) was a wilderness station of the Israelites, described in Deuteronomy 10:6 as the location where Aaron died and where he was buried. The reference in Numbers 33:37–38 places Aaron's death at Mount Hor on the border of Edom, which appears to be a complementary rather than contradictory account: Mosera may have been the name of the broader district or encampment at the foot of Mount Hor where the Israelites were stationed when Aaron ascended the mountain to die. The site is tentatively identified with el-Tayibeh, a spring at the base of the pass leading up to Mount Hor. Aaron's death at this location marked a transition for Israel: his priestly garments were transferred to his son Eleazar, who succeeded him as high priest (Num. 20:26–28).</p>"
    },
    "moseroth": {
        "id": "moseroth", "term": "Moseroth", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moseroth", "isbe": "moseroth"},
        "key_refs": ["Numbers 33:30", "Numbers 33:31"],
        "intro": "<p>Moseroth (the plural form of Mosera, meaning <em>bonds</em> or <em>chastisements</em>) was a wilderness station in the Israelites' itinerary during the Exodus, appearing between Hashmonah and Bene-jaakan in the list of Numbers 33 (vv. 30–31). It is generally understood to be the same location as Mosera mentioned in Deuteronomy 10:6, where Aaron's death is recorded. The plural form may indicate a cluster of encampments rather than a single site, or it may simply reflect a variant orthographic tradition. Like most of the forty-two wilderness stations in Numbers 33, the precise location of Moseroth cannot be determined with certainty from archaeological or geographical evidence, and it remains unidentified on modern maps of the Sinai and Negev regions.</p>"
    },
    "moses": {
        "id": "moses", "term": "Moses", "category": "people",
        "hitchcock_meaning": "taken out; drawn forth",
        "source_ids": {"easton": "moses", "smith": "moses", "isbe": "moses"},
        "key_refs": ["Exodus 3:4", "Exodus 20:1", "Deuteronomy 34:10", "Hebrews 11:24"],
        "intro": "<p>Moses, son of Amram and Jochebed of the tribe of Levi, was the deliverer, lawgiver, and prophet of Israel whose life and ministry shaped the entire Old Testament. Born during Pharaoh's edict ordering the death of Hebrew male infants, he was hidden for three months, then placed in a basket on the Nile where he was found and adopted by Pharaoh's daughter (Ex. 2:1–10). Raised in the Egyptian court, he fled to Midian after killing an Egyptian taskmaster. At the burning bush on Mount Horeb, God called him to lead Israel out of Egypt (Ex. 3), commissioning him despite his reluctance. Through the ten plagues and the Passover, Moses led the Exodus of the Israelites and their crossing of the Red Sea. At Sinai he received the law — the Ten Commandments and the full covenant code — and mediated the covenant between God and Israel. He led the nation through forty years of wilderness wandering, interceding repeatedly for a rebellious people. Forbidden to enter the land because of his striking the rock at Meribah (Num. 20:12), he died on Mount Nebo within sight of Canaan. Scripture's epitaph is unequaled: <em>there has not arisen a prophet since in Israel like Moses, whom the LORD knew face to face</em> (Deut. 34:10).</p>"
    },
    "mote": {
        "id": "mote", "term": "Mote", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mote", "isbe": "mote"},
        "key_refs": ["Matthew 7:3", "Luke 6:41", "Luke 6:42"],
        "intro": "<p>The mote (Greek <em>karphos</em>, meaning a dry piece of straw, chaff, or splinter) appears in Jesus' teaching on judgmentalism in the Sermon on the Mount and its parallel in Luke 6 (Matt. 7:3–5; Luke 6:41–42). Jesus uses the contrast between a mote (a tiny particle of dust or wood) lodged in another person's eye and a beam or plank (<em>dokos</em>) lodged in one's own eye to expose the hypocrisy of harsh critics who are blind to far greater faults in themselves. The vivid absurdity of the image — someone with a log in their eye trying to remove a speck from their neighbor's — makes it one of the most memorable of Jesus' rhetorical illustrations. The teaching does not forbid all moral discernment but insists on self-examination before correcting others. The word \"mote\" has become an English idiom for any trivially small fault or flaw.</p>"
    },
    "moth": {
        "id": "moth", "term": "Moth", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moth", "smith": "moth", "isbe": "moth"},
        "key_refs": ["Job 4:19", "Isaiah 51:8", "Matthew 6:19", "Hosea 5:12"],
        "intro": "<p>The moth (Hebrew <em>'ash</em>; Greek <em>ses</em>) is the only lepidopterous (butterfly/moth) insect mentioned in Scripture, where it appears consistently as a symbol of decay, impermanence, and the fragility of earthly wealth. The larvae of the clothes-moth (<em>Tinea pellionella</em>) feed on wool, linen, and stored garments, making moth damage a familiar household loss in the ancient world. Job uses the moth to illustrate the frailty of human life before God: those who dwell in houses of clay have foundations in the dust and are crushed like the moth (Job 4:19). Isaiah applies the same metaphor to God's judgment on enemies (Isa. 50:9; 51:8). Jesus uses the moth's destruction of stored clothing as an argument against earthly treasure: \"Do not lay up for yourselves treasures on earth, where moth and rust destroy\" — contrasting it with heavenly treasure that cannot be consumed (Matt. 6:19–20). Hosea employs the moth as an image of God's slow, consuming judgment on Ephraim (Hos. 5:12).</p>"
    },
    "mouldy": {
        "id": "mouldy", "term": "Mouldy", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mouldy"},
        "key_refs": ["Joshua 9:5", "Joshua 9:12"],
        "intro": "<p>The word mouldy occurs in the account of the Gibeonite deception in Joshua 9. The Gibeonites, fearing Israel's advance through Canaan, disguised themselves as a delegation from a distant country, presenting worn sandals, patched wineskins, and dry, mouldy bread as evidence of a long journey (Josh. 9:5, 12). The Hebrew word rendered \"mouldy\" (<em>nikuddim</em>) more precisely denotes bread that has hardened into crumbling, brittle pieces — dried to the consistency of cracknels — rather than bread visibly grown with mold. Their ruse succeeded: the Israelite leaders failed to inquire of the LORD and swore a covenant of peace with the Gibeonites (Josh. 9:14–15). When the deception was discovered, Israel honored its oath but made the Gibeonites perpetual servants — woodcutters and water-carriers for the sanctuary. The episode illustrates the danger of acting on appearances without seeking divine counsel.</p>"
    },
    "mount": {
        "id": "mount", "term": "Mount", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount", "smith": "mount"},
        "key_refs": ["Deuteronomy 11:11", "Psalms 48:2", "Isaiah 2:2"],
        "intro": "<p>Palestine is a distinctly mountainous country (Deut. 3:25; 11:11; Ezek. 34:13), and the mountains of the biblical world carry profound theological as well as geographical significance. The main ranges include the Lebanon and Anti-Lebanon in the far north, the hills of Galilee descending southward, the isolated peak of Tabor rising from the Jezreel plain, and the central highland ridge running through Samaria and Judea with peaks such as Ebal, Gerizim, and the hills of Jerusalem. East of the Jordan rise the highlands of Bashan and Gilead, while in the south the Negev gives way to the sandstone massif of Edom. Specific mountains hold central importance in salvation history: Sinai (the mount of the law), Zion (the mount of the temple and the Davidic covenant), Carmel (Elijah's contest), Hermon (possibly the Transfiguration), and Olivet (Jesus' ascension). The eschatological vision of Isaiah locates the LORD's house on \"the mountain of the LORD\" exalted above all hills, to which all nations will stream (Isa. 2:2–4).</p>"
    },
    "mount-of-beatitudes": {
        "id": "mount-of-beatitudes", "term": "Mount of Beatitudes", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount-of-beatitudes"},
        "key_refs": ["Matthew 5:1", "Matthew 5:2", "Luke 6:17"],
        "intro": "<p>The Mount of Beatitudes is the traditional name for the hillside where Jesus delivered the Sermon on the Mount (Matt. 5–7), which opens with the eight Beatitudes (Matt. 5:3–12). Matthew describes Jesus ascending a mountain and sitting to teach (Matt. 5:1), while Luke's parallel account places the teaching on a level place (Luke 6:17), which may indicate a plateau on the hillside. The precise location has not been identified with certainty. Christian tradition since at least the fourth century has associated it with the hill now known as Karn Hattin (the Horns of Hattin), southwest of the Sea of Galilee. A rival tradition places it on a gentle hill called the Mount of Beatitudes (Har Karkom) near Capernaum and Tabgha on the northwest shore of the lake, where a Franciscan church commemorates the site. The Sermon on the Mount delivered there — covering ethics, prayer, righteousness, and kingdom living — constitutes the fullest body of Jesus' ethical teaching in the Gospels.</p>"
    },
    "mount-of-corruption": {
        "id": "mount-of-corruption", "term": "Mount of Corruption", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount-of-corruption", "isbe": "mount-of-corruption"},
        "key_refs": ["2 Kings 23:13", "1 Kings 11:7"],
        "intro": "<p>The Mount of Corruption (also called the Mount of Offence, Latin <em>Mons Offensionis</em>) was the derogatory name given to the southern spur of the Mount of Olives where Solomon erected shrines to pagan deities for his foreign wives. He built high places there for Chemosh, the god of Moab, and for Molech, the god of Ammon, as well as for the Sidonian goddess Ashtoreth (1 Kings 11:7; 2 Kings 23:13). The name Mount of Corruption — substituting a word of shame for whatever the original name of the ridge may have been — expresses the Hebrew scribal practice of stigmatizing sites of idolatry. These shrines remained standing for approximately three centuries until King Josiah defiled and demolished them as part of his sweeping reformation (2 Kings 23:13). The site is traditionally located on the southern slope of Olivet, opposite Zion across the Kidron Valley.</p>"
    },
    "mount-of-the-amalekites": {
        "id": "mount-of-the-amalekites", "term": "Mount of the Amalekites", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount-of-the-amalekites", "isbe": "mount-of-the-amalekites"},
        "key_refs": ["Judges 12:15"],
        "intro": "<p>The Mount of the Amalekites was a hill or elevated district in the territory of Ephraim near the town of Pirathon, mentioned once in Scripture in connection with Abdon the judge, who was buried at Pirathon \"in the hill-country of the Amalekites\" (Judg. 12:15). The reference indicates that this region of Ephraim had at some earlier period been occupied or associated with Amalekite settlements, traces of which remained in the local place-name even after Israelite settlement. Pirathon itself is generally identified with Fer'ata, a village about seven miles west-southwest of Shechem. The single mention of the Mount of the Amalekites is notable primarily as evidence of the distribution of Amalekite presence across Canaan beyond their better-known strongholds in the Negev and Sinai regions.</p>"
    },
    "mount-of-the-amorites": {
        "id": "mount-of-the-amorites", "term": "Mount of the Amorites", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount-of-the-amorites", "isbe": "mount-of-the-amorites"},
        "key_refs": ["Deuteronomy 1:19", "Deuteronomy 1:20"],
        "intro": "<p>The Mount of the Amorites was the elevated rocky range that formed the southern edge of the Promised Land as approached from the Sinai wilderness, described in Moses' retrospective address as the highlands encountered after crossing \"that great and terrible wilderness\" (Deut. 1:19–20). Moses directed Israel to go up and take possession of the hill country, but the people refused after the discouraging report of the spies, precipitating forty years of wandering (Deut. 1:26–33). The region corresponds to the high limestone plateau of the Negev highlands, the southern Judean hills, and possibly the region later associated with the Amorite kingdoms. The Amorites were one of the pre-Israelite peoples of Canaan who inhabited both the hill country and the Transjordanian plateau, and their name was sometimes used broadly to denote all the inhabitants of Canaan (Gen. 15:16).</p>"
    },
    "mount-of-the-congregation": {
        "id": "mount-of-the-congregation", "term": "Mount of the Congregation", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount-of-the-congregation"},
        "key_refs": ["Isaiah 14:13"],
        "intro": "<p>The Mount of the Congregation (Hebrew <em>har mo'ed</em>) occurs once in Scripture, in Isaiah's taunt against the king of Babylon (Isa. 14:13). The boastful king declares his intention to ascend to heaven and set his throne above the stars of God: \"I will sit on the mount of assembly in the far reaches of the north.\" This language reflects Babylonian and Canaanite cosmology, in which the gods were believed to assemble on a cosmic mountain in the far north — corresponding to the Babylonian mountain <em>Im-Kharasak</em> (\"the mighty mountain of Bel\") or the Canaanite mount Zaphon. Isaiah's oracle uses this mythological imagery to expose the king's hubris: his aspiration to divine status will be cast down to Sheol (Isa. 14:15). The passage has been read by many interpreters as simultaneously addressing a cosmic fall — whether of a primordial figure or of Satan — behind the human king's arrogance.</p>"
    },
    "mount-of-the-valley": {
        "id": "mount-of-the-valley", "term": "Mount of the Valley", "category": "places",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mount-of-the-valley", "isbe": "mount-of-the-valley"},
        "key_refs": ["Joshua 13:19"],
        "intro": "<p>The Mount of the Valley is mentioned in the territorial description of Reuben's inheritance east of the Jordan (Josh. 13:19), appearing as one of the cities or districts in the plain. The phrase designates hilly terrain adjacent to the valley of the Jordan — most likely the elevated ground at the northern end of the Dead Sea where the Jordan plain rises into the tableland of Moab. The specific reference in Joshua 13:19 names it among cities including Kirjathaim and Sibmah. The region corresponds to the fertile Ghor, the Jordan valley depression, where the mount would refer to the escarpment or highland overlooking the valley floor. The passage is part of the systematic allotment of territory that Moses had distributed to the two and a half tribes east of the Jordan before his death (Josh. 13:8–12).</p>"
    },
    "mourn": {
        "id": "mourn", "term": "Mourn", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mourn"},
        "key_refs": ["Genesis 23:2", "Matthew 5:4", "James 4:9", "Revelation 21:4"],
        "intro": "<p>Mourning in the Bible encompasses both formal practices of grief and the spiritual disposition of contrition before God. The Old Testament records elaborate public mourning for the dead: tearing garments, wearing sackcloth and ashes, fasting, wailing, and hiring professional mourners (Gen. 23:2; 2 Sam. 3:31; Jer. 9:17–18). Set periods of mourning were observed for prominent figures — thirty days for Aaron and Moses (Num. 20:29; Deut. 34:8), seven days for Jacob (Gen. 50:10). Mourning was also practiced in response to national calamity, divine judgment, and personal sin, particularly in the prophetic and wisdom traditions (Joel 1:13–14; Ezra 9:3–5). Jesus' second Beatitude pronounces blessing on those who mourn — generally understood as those who grieve over sin — with the promise that they shall be comforted (Matt. 5:4). James calls believers to exchange worldly laughter for mourning and weeping as a disposition of repentance (Jas. 4:9). The eschatological hope is that God will wipe away every tear and mourning will cease entirely (Rev. 21:4; Isa. 61:3).</p>"
    },
    "mouse": {
        "id": "mouse", "term": "Mouse", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mouse", "smith": "mouse"},
        "key_refs": ["Leviticus 11:29", "1 Samuel 6:4", "Isaiah 66:17"],
        "intro": "<p>The mouse (Hebrew <em>'akhbar</em>, a swift digger) encompasses several rodent species in its biblical usage, including the field-mouse, dormouse, rat, hamster, and jerboa — all creatures common in the agricultural landscape of ancient Palestine. Mosaic law classified the mouse among unclean animals forbidden for food (Lev. 11:29). Despite this prohibition, mice or rats were apparently eaten by Bedouin peoples in the region, and Isaiah 66:17 condemns those who eat the mouse and other abominations as part of pagan rites. The plague of mice sent by God upon the Philistines when they captured the ark of the covenant (1 Sam. 5–6) prompted them to return the ark along with a guilt offering of five golden mice — one for each Philistine city affected (1 Sam. 6:4–5). This episode suggests the association of mice with destructive plague, and the golden images served as a ritual acknowledgment of divine power over both the pest and the pestilence it represented.</p>"
    },
    "mowing": {
        "id": "mowing", "term": "Mowing", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mowing", "smith": "mowing"},
        "key_refs": ["Psalms 72:6", "Amos 7:1"],
        "intro": "<p>Mowing (Hebrew <em>gez</em>) refers to the cutting of grass or grain, a fundamental activity of the agricultural year in ancient Israel. The \"king's mowings\" mentioned in Amos 7:1 refer to a royal prerogative by which the first cutting of the spring grass was reserved for the king's cavalry and stables before the rest could be harvested by the people (cf. 1 Kings 18:5). In Amos's vision, a locust plague devours the spring crop just as it was beginning to grow after the king's mowing — a devastating blow striking the most vulnerable point in the agricultural cycle. Psalm 72:6 uses the image of rain on mown grass to describe the king's refreshing and restoring rule: \"He shall come down like rain upon the mown grass, like showers that water the earth.\" The contrast between the vulnerability of cut grass and the life-giving power of rain makes mowing a fitting symbol of human need met by divine provision.</p>"
    },
    "moza": {
        "id": "moza", "term": "Moza", "category": "people",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "moza", "smith": "moza", "isbe": "moza"},
        "key_refs": ["1 Chronicles 2:46", "1 Chronicles 8:36", "1 Chronicles 9:42"],
        "intro": "<p>Moza (meaning <em>a going forth</em>) is the name of two individuals in the genealogical records of Chronicles. The first was a son of Caleb by his concubine Ephah (1 Chr. 2:46), listed among the descendants of Judah. The second, and more prominently situated, was a descendant of King Saul through Jonathan and Merib-baal (Mephibosheth), listed in the genealogy of Benjamin as the son of Zimri and the father of Binea (1 Chr. 8:36–37; 9:42–43). This second Moza's inclusion in the Saulide lineage through Jonathan is significant because it traces the surviving royal line of Saul's house for several generations after the dynasty's end, demonstrating that Jonathan's descendants continued despite the transfer of the kingdom to David. The two men named Moza are unrelated and belong to different tribes.</p>"
    },
    "mozah": {
        "id": "mozah", "term": "Mozah", "category": "places",
        "hitchcock_meaning": "unleavened",
        "source_ids": {"easton": "mozah", "smith": "mozah", "isbe": "mozah"},
        "key_refs": ["Joshua 18:26"],
        "intro": "<p>Mozah (meaning <em>unleavened</em> or <em>an issuing of water</em>) was a town in the territory of Benjamin, listed among the cities in Joshua 18:26. It appears in the second group of Benjamin's cities, alongside Mizpeh and Chephirah, suggesting it lay in the hill-country northwest of Jerusalem. The site is tentatively identified with Khirbet Beit Mizza or the nearby Colonia (Qaluniyeh), a village approximately four miles northwest of Jerusalem on the road to Emmaus. Josephus mentions a place called Emmaus (Motsa) in this vicinity. Beyond its inclusion in the territorial list of Benjamin, Mozah is not the scene of any recorded biblical event, and its significance lies primarily in the systematic geography of Israel's tribal distribution as recorded by Joshua.</p>"
    },
    "mufflers": {
        "id": "mufflers", "term": "Mufflers", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mufflers"},
        "key_refs": ["Isaiah 3:19"],
        "intro": "<p>Mufflers appear in Isaiah 3:19 as one of the twenty-one articles of feminine adornment that the LORD declares he will remove from the \"daughters of Zion\" as a judgment for their haughtiness and pride (Isa. 3:16–23). The Hebrew term (<em>nетifot</em>, often rendered \"pendants\" or \"eardrops\" in modern translations) refers to light, trembling ornamental veils or hanging decorations — possibly fine gauze veils or dangling jewelry worn about the face and ears. The Authorized Version's \"mufflers\" reflects the older English sense of a cloth wrapped about the face. The extended catalog of luxury items in Isaiah 3 — anklets, headbands, crescents, pendants, bracelets, sashes, perfume boxes, amulets, rings, and more — serves as an indictment of the wealthy women of Jerusalem whose conspicuous consumption was coupled with injustice and spiritual complacency.</p>"
    },
    "mulberry": {
        "id": "mulberry", "term": "Mulberry", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mulberry"},
        "key_refs": ["2 Samuel 5:23", "2 Samuel 5:24", "1 Chronicles 14:14", "Psalms 84:6"],
        "intro": "<p>The mulberry tree of the English Bible translates two Hebrew words that may not refer to the same species. In Psalm 84:6, the Hebrew <em>baka</em> (meaning <em>to weep</em>, from the resinous drops the tree exudes) gives its name to the \"Valley of Baca\" — a place of weeping transformed by the pilgrims into a place of springs, a common rendering of which is \"valley of tears.\" More significant historically are the <em>bekaim</em> trees of 2 Samuel 5:23–24 and 1 Chronicles 14:14–15, in whose tops the sound of marching was to serve as God's signal for David to attack the Philistines. Most scholars now identify these trees as aspen or trembling poplar (<em>Populus tremula</em>), whose leaves rustle conspicuously in even slight breezes, making the rustling sound an identifiable signal. The true mulberry (<em>Morus nigra</em>) was grown in Palestine but is likely not the species intended in these military contexts.</p>"
    },
    "mule": {
        "id": "mule", "term": "Mule", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mule", "smith": "mule", "isbe": "mule"},
        "key_refs": ["2 Samuel 18:9", "1 Kings 1:33", "Zechariah 14:15"],
        "intro": "<p>The mule (Hebrew <em>pered</em>), the sterile offspring of a horse and a donkey, was a prized beast of burden and riding animal in ancient Israel. Though the Mosaic law forbade the breeding of mules by prohibiting the mating of different species (Lev. 19:19), the use of mules was not prohibited, and they were imported from abroad. Mules were the riding animals of kings and nobles: David's sons rode mules (2 Sam. 13:29), and Absalom was riding his mule when his hair caught in the terebinth tree where Joab killed him (2 Sam. 18:9). Solomon rode David's mule to his anointing at Gihon (1 Kings 1:33–44), a deliberate act of royal succession. Mules carried heavy loads (2 Kings 5:17; 1 Chr. 12:40) and were used in trade (1 Kings 10:25; Ezra 2:66). By the time of the exile they were common enough to feature in lists of returned property and eschatological imagery (Zech. 14:15).</p>"
    },
    "murder": {
        "id": "murder", "term": "Murder", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "murder", "smith": "murder", "isbe": "murder"},
        "key_refs": ["Numbers 35:16", "Numbers 35:31", "Genesis 9:6", "Matthew 5:21"],
        "intro": "<p>Murder — the intentional unlawful killing of a human being — is among the most severely condemned acts in biblical law and ethics. The prohibition against murder is embedded in the Noahic covenant (Gen. 9:6: <em>Whoever sheds the blood of man, by man shall his blood be shed, for God made man in his own image</em>) and reiterated in the Sixth Commandment (Ex. 20:13; Deut. 5:17). The Mosaic law carefully distinguished murder from accidental homicide (manslaughter), prescribing cities of refuge where those guilty of unintentional killing could seek asylum from the avenger of blood (Num. 35:11–28). For deliberate murder, capital punishment was mandatory and no ransom was accepted (Num. 35:16–21, 31). Jesus radicalized the commandment by extending its scope to encompass hatred and contemptuous anger as murder of the heart (Matt. 5:21–22). The New Testament consistently lists murder among the gravest sins excluding from the kingdom of God (Rev. 21:8; 22:15) and associates it with the fallen nature of a world in rebellion against its Creator (Rom. 1:29; 1 John 3:15).</p>"
    },
    "murmuring": {
        "id": "murmuring", "term": "Murmuring", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "murmuring"},
        "key_refs": ["Numbers 14:27", "Psalms 106:25", "1 Corinthians 10:10", "Philippians 2:14"],
        "intro": "<p>Murmuring — the complaining, grumbling rebellion of Israel against God and his appointed leaders during the wilderness period — is one of the recurring themes of the Exodus narrative. The Israelites murmured against Moses and Aaron at the waters of Marah (Ex. 15:24), at Rephidim (Ex. 17:3), repeatedly over food (Num. 11:1–4), in response to the spies' report (Num. 14:2), during Korah's rebellion (Num. 16:41), and against the rigors of the journey (Num. 21:4–5). God consistently regarded this murmuring as directed against himself rather than merely against human leadership (Ex. 16:8; Num. 14:27). The consequences were severe: the generation that murmured at the spies' report was condemned to die in the wilderness (Num. 14:28–35). Psalm 106:25 identifies murmuring with unbelief. Paul cites the wilderness generation as a warning to the Corinthians (1 Cor. 10:10), and exhorts the Philippians to do all things without murmuring or disputing (Phil. 2:14), presenting contentment and gratitude as marks of the renewed life in Christ.</p>"
    },
    "murrain": {
        "id": "murrain", "term": "Murrain", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "murrain", "isbe": "murrain"},
        "key_refs": ["Exodus 9:3", "Exodus 9:6", "Psalms 78:50"],
        "intro": "<p>Murrain (from Old French <em>morine</em>, death or pestilence) designates the fifth of the ten plagues of Egypt, recorded in Exodus 9:1–7. The Hebrew <em>deber</em> (literally <em>destruction</em> or <em>pestilence</em>) describes a severe epidemic disease that struck the livestock of Egypt — horses, donkeys, camels, herds, and flocks — causing widespread sudden death among animals in the field (Ex. 9:3, 6). The plague was announced in advance by Moses and executed on the appointed day by the LORD. A divine distinction was preserved: none of Israel's livestock died (Ex. 9:4, 6–7), a fact that Pharaoh verified but that still failed to soften his heart. Psalm 78:50 reflects on the plague in the context of God's judgments in Egypt, and Psalm 105:29–36 reviews the plagues in sequence. The murrain was the first plague to strike living creatures directly rather than natural elements or human persons, escalating the pressure on Pharaoh to release Israel.</p>"
    },
    "mushi": {
        "id": "mushi", "term": "Mushi", "category": "people",
        "hitchcock_meaning": "he that touches, that withdraws or takes away",
        "source_ids": {"easton": "mushi", "smith": "mushi", "isbe": "mushi"},
        "key_refs": ["Exodus 6:19", "Numbers 3:20", "Numbers 3:33", "Numbers 26:58"],
        "intro": "<p>Mushi was the second of two sons of Merari, son of Levi (Ex. 6:19; Num. 3:20), making him a grandson of Levi and a great-grandson of Jacob. Together with his brother Mahli, he was the ancestor of the Mushite clan of Levites (Num. 3:33; 26:58). The Merarite division of the Levites, to which the Mushites belonged, was responsible in the wilderness for transporting the heavy structural components of the tabernacle — the frames, bars, pillars, and bases (Num. 4:29–33). Under the monarchic period, the descendants of Mushi continued in Levitical temple service. His name (<em>withdrawn</em> or <em>he who touches</em>) may relate to the Levites' role in handling sacred furniture. In Chronicles the Mushite genealogy is extended through several generations, confirming the clan's ongoing importance in the post-Davidic Levitical organization (1 Chr. 6:47; 23:23; 24:30).</p>"
    },
    "music": {
        "id": "music", "term": "Music", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "music", "smith": "music", "isbe": "music"},
        "key_refs": ["Genesis 4:21", "Exodus 15:20", "2 Samuel 6:5", "Colossians 3:16"],
        "intro": "<p>Music held a central place in Israelite worship, celebration, and cultural life throughout the biblical period. Jubal, a descendant of Cain, is identified as \"the father of all those who play the harp and flute\" (Gen. 4:21), placing music's origins in the earliest generations of humanity. The Exodus period produced some of the oldest surviving biblical poetry set to music: the Song of Moses after the Red Sea crossing (Ex. 15) and Miriam's victory song with timbrel and dancing (Ex. 15:20–21). The golden age of Hebrew music came under David and Solomon: David organized Levitical musicians in courses (1 Chr. 23–25), composed psalms, and introduced a wide range of instruments into temple worship. The Psalter itself is largely a hymnal, with many psalms bearing musical notations in their superscriptions. Music served three primary functions in Israel's life: praise of God in worship, celebration of victory and rejoicing, and lament in times of grief and penitence. The New Testament continues this tradition, calling believers to speak to one another in psalms, hymns, and spiritual songs (Eph. 5:19; Col. 3:16).</p>"
    },
    "music-instrumental": {
        "id": "music-instrumental", "term": "Music, Instrumental", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "music-instrumental"},
        "key_refs": ["Psalms 150:3", "Psalms 150:4", "Psalms 150:5", "1 Chronicles 15:16"],
        "intro": "<p>The instrumental music of ancient Israel employed three families of instruments. Stringed instruments included the <em>kinnor</em> (harp or lyre, David's instrument), the <em>nebel</em> (psaltery or harp, a larger stringed instrument), and the <em>sabbeka</em> (a lute or lyre). Wind instruments included the <em>halil</em> (a pipe or flute), the silver <em>hatsotserah</em> (a straight trumpet used for signaling), and the curved ram's-horn <em>shofar</em>, whose blast marked sacred assemblies, battles, and the jubilee year. Percussion instruments included the <em>toph</em> (timbrel or tambourine), <em>metsiltayim</em> (cymbals), and <em>menaanei'm</em> (sistrums). Psalm 150 offers the Bible's fullest catalog of these instruments, commanding praise with every category of sound. David organized the Levitical musicians into hereditary orders using these instruments for the temple service (1 Chr. 15:16–24; 25:1–31). The variety of instruments reflects the full-bodied, joyful character of Hebrew worship.</p>"
    },
    "musician-chief": {
        "id": "musician-chief", "term": "Musician, Chief", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "musician-chief", "isbe": "musician-chief"},
        "key_refs": ["Habakkuk 3:19", "1 Chronicles 16:41", "Psalms 4:1"],
        "intro": "<p>The Chief Musician (Hebrew <em>lamnatseah</em> or <em>menatstseah</em>, meaning <em>to the precentor</em> or <em>for the director</em>) appears in the superscriptions of fifty-five psalms and in the closing verse of Habakkuk's prayer (Hab. 3:19). The inscription indicates that these psalms were committed to the director of the Levitical choir or orchestra for performance in the temple liturgy. The office of chief musician was first held by Jeduthun (1 Chr. 16:41), with Heman and Asaph serving as his colleagues (2 Chr. 35:15). These three guilds — sons of Asaph, sons of Heman, and sons of Jeduthun — conducted the musical worship of the Jerusalem temple. The position was hereditary and prestigious, and the three families appear as the custodians of Israel's liturgical musical tradition. The inscription \"for the chief musician\" suggests an organized and professionally maintained collection of sacred songs intended for regular congregational use in worship.</p>"
    },
    "mustard": {
        "id": "mustard", "term": "Mustard", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mustard", "smith": "mustard", "isbe": "mustard"},
        "key_refs": ["Matthew 13:31", "Matthew 17:20", "Mark 4:31", "Luke 13:19"],
        "intro": "<p>The mustard plant of the New Testament parables is generally identified as <em>Sinapis nigra</em>, black mustard, a shrub-like annual herb that grows commonly in Galilee and throughout the Holy Land. Its seeds are among the smallest used in Palestinian agriculture, yet the plant can grow to a height of eight to ten feet in favorable conditions, large enough for birds to nest in its branches. Jesus used the mustard seed in two distinct but related parables. In the Parable of the Mustard Seed (Matt. 13:31–32; Mark 4:30–32; Luke 13:18–19), the kingdom of heaven is compared to a mustard seed that grows from the smallest of seeds into the greatest of garden plants, illustrating the vast and surprising growth of the kingdom from its humble beginnings. In the saying on faith (Matt. 17:20; Luke 17:6), Jesus tells his disciples that faith even as small as a mustard seed would be sufficient to move mountains — emphasizing quality of trust over quantity.</p>"
    },
    "muth-labben": {
        "id": "muth-labben", "term": "Muth-labben", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "muth-labben", "isbe": "muth-labben"},
        "key_refs": ["Psalms 9:1"],
        "intro": "<p>Muth-labben (Hebrew, literally <em>death of the son</em>) appears only in the superscription of Psalm 9, translated in older versions as \"upon Muth-labben\" or \"to the chief musician upon Muth-labben.\" The phrase is most likely a musical instruction indicating either the tune to which the psalm was to be sung, the instrument on which it was to be played, or an occasion for its performance. Three main interpretations have been proposed: (1) the phrase refers to the death of Labben, an otherwise unknown individual; (2) it means \"death of the son\" and may indicate a psalm composed in connection with the death of Absalom (2 Sam. 18:33), though this identification is uncertain; (3) it designates a specific musical mode or melody whose name incorporated these words. The phrase illustrates the challenge of interpreting the technical musical terminology in the psalm headings, much of which remains obscure to modern scholarship.</p>"
    },
    "muzzle": {
        "id": "muzzle", "term": "Muzzle", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "muzzle", "isbe": "muzzle"},
        "key_refs": ["Deuteronomy 25:4", "1 Corinthians 9:9", "1 Timothy 5:18"],
        "intro": "<p>The law of the muzzle is one of the most briefly stated yet theologically significant provisions of Mosaic legislation: \"You shall not muzzle an ox when it is treading out the grain\" (Deut. 25:4). In the agriculture of the ancient Near East, oxen were driven across spread-out sheaves to tread out the grain, and it would have been easy and economical to prevent them from eating the grain as they worked. The law prohibited this, requiring that working animals be allowed to eat from the harvest they were helping to produce. Paul cites this commandment twice as the scriptural basis for the principle that those who labor in ministry are entitled to material support from those they serve (1 Cor. 9:9–14; 1 Tim. 5:18). His exegetical comment — \"Is it for oxen that God is concerned? Does he not certainly speak for our sake?\" (1 Cor. 9:9–10) — applies the agricultural law by analogy to the rights of the gospel worker, establishing one of the New Testament's clearest statements on ministerial compensation.</p>"
    },
    "myra": {
        "id": "myra", "term": "Myra", "category": "places",
        "hitchcock_meaning": "I flow; pour out; weep",
        "source_ids": {"easton": "myra", "smith": "myra", "isbe": "myra"},
        "key_refs": ["Acts 27:5", "Acts 27:6"],
        "intro": "<p>Myra was one of the principal cities of Lycia, a province on the southwestern coast of Asia Minor (modern Turkey), situated approximately two and a half miles inland from the harbor town of Andriake. It played an important role in Paul's final journey to Rome as a prisoner: after sailing from Caesarea along the coast of Cilicia and Pamphylia, the centurion Julius found an Alexandrian grain ship at Myra bound for Italy and transferred Paul and the other prisoners to it (Acts 27:5–6). This Alexandrian grain ship, likely part of the imperial grain fleet that supplied Rome from Egypt, subsequently encountered the great storm that wrecked the vessel at Malta (Acts 27:14–44). Myra later became an important Christian center: Nicholas, the fourth-century bishop of Myra, is the historical figure behind the tradition of Saint Nicholas. The city's ruins, including an impressive Lycian rock-cut theater and necropolis, are visible near the modern Turkish town of Demre.</p>"
    },
    "myrrh": {
        "id": "myrrh", "term": "Myrrh", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "myrrh", "smith": "myrrh", "isbe": "myrrh"},
        "key_refs": ["Exodus 30:23", "Matthew 2:11", "Mark 15:23", "John 19:39"],
        "intro": "<p>Myrrh is a fragrant resinous gum obtained by making incisions in the bark of trees of the genus <em>Commiphora</em> (principally <em>C. myrrha</em>), native to Arabia and East Africa. It was among the most prized aromatic substances of the ancient world, used in perfumery, medicine, embalming, and religious ritual. In the Old Testament, myrrh was a principal ingredient in the holy anointing oil prepared for the tabernacle and its vessels (Ex. 30:23), and it appears frequently in the erotic poetry of the Song of Solomon as a symbol of love and intimacy (Song 1:13; 5:1). The wise men brought myrrh as one of their three gifts to the infant Jesus (Matt. 2:11), and its symbolism has been widely interpreted as pointing to his coming death and burial. At the crucifixion Jesus was offered wine mingled with myrrh as a mild analgesic, which he refused (Mark 15:23). After his death, Nicodemus brought a large quantity of myrrh and aloes to prepare his body for burial in the Jewish manner (John 19:39).</p>"
    },
    "myrtle": {
        "id": "myrtle", "term": "Myrtle", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "myrtle", "smith": "myrtle", "isbe": "myrtle"},
        "key_refs": ["Nehemiah 8:15", "Isaiah 55:13", "Zechariah 1:8"],
        "intro": "<p>The myrtle (Hebrew <em>hadas</em>) is <em>Myrtus communis</em>, a fragrant evergreen shrub with dark glossy leaves and white flowers, still common in the hill country and ravines of Palestine and Lebanon. It was one of the four plant species prescribed for the construction of the booths at the Feast of Tabernacles alongside palm branches, willows, and \"goodly trees\" (Lev. 23:40; Neh. 8:15). The personal name Hadassah — Esther's Hebrew name (Esther 2:7) — is derived from the same root, suggesting the myrtle was associated with beauty and pleasantness. Isaiah's great passage of restoration uses the myrtle as a symbol of divine transformation: \"Instead of the thorn shall come up the cypress; instead of the brier shall come up the myrtle\" (Isa. 55:13), picturing the messianic renewal of the natural and social order. In Zechariah's night visions, the angel of the LORD stands among myrtle trees in a ravine (Zech. 1:8, 10–11), a setting that has been interpreted as symbolizing the sheltered, quiet state of Israel during the period of the nations' domination.</p>"
    },
    "mysia": {
        "id": "mysia", "term": "Mysia", "category": "places",
        "hitchcock_meaning": "criminal; abominable",
        "source_ids": {"easton": "mysia", "smith": "mysia", "isbe": "mysia"},
        "key_refs": ["Acts 16:7", "Acts 16:8"],
        "intro": "<p>Mysia was a province in the northwest corner of Asia Minor (modern Turkey), bordered by the Propontis (Sea of Marmara) and Hellespont to the north, Bithynia to the northeast, Lydia to the south, and the Aegean Sea to the west. Its principal cities included Troas on the coast, Pergamum in the south, and Assos. Paul passed through Mysia on his second missionary journey, when the Spirit of Jesus forbade him to enter Bithynia to the northeast (Acts 16:7), effectively directing him westward toward the Aegean coast. He traveled through Mysia — apparently without preaching there — and came down to the port city of Troas (Acts 16:8), where he received the Macedonian vision calling him to cross into Europe (Acts 16:9–10). This pivotal redirection through Mysia marked the point at which the gospel first crossed from Asia into Europe, making Mysia a geographical transition point of enormous missionary significance even though it was not itself directly evangelized at this stage.</p>"
    },
    "mystery": {
        "id": "mystery", "term": "Mystery", "category": "concepts",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mystery", "isbe": "mystery"},
        "key_refs": ["Ephesians 3:3", "Colossians 1:27", "Romans 11:25", "1 Corinthians 15:51"],
        "intro": "<p>Mystery (Greek <em>mysterion</em>) in the New Testament does not denote something inherently unknowable or esoteric but rather a divine truth formerly hidden that has now been disclosed through revelation. The term appears to draw on Old Testament concepts of divine counsel and secret wisdom (cf. Dan. 2:18–19, 27–30; Amos 3:7) rather than on the Greek mystery cults, in which <em>mysteria</em> were secret rites disclosed only to initiates. Paul is the primary New Testament expositor of this concept: he describes the inclusion of the Gentiles as equal heirs of the promise in Christ as a mystery hidden for ages but now made manifest through the gospel (Eph. 3:3–11; Col. 1:26–27). The content of Christ in believers — \"Christ in you, the hope of glory\" (Col. 1:27) — is itself the central mystery. Other New Testament mysteries include the partial hardening of Israel (Rom. 11:25), the resurrection and transformation of the dead at Christ's coming (1 Cor. 15:51), the union of Christ and the church as a profound mystery analogous to marriage (Eph. 5:32), and the mystery of lawlessness already at work in the world (2 Thess. 2:7). The common thread is divine initiative: God reveals what was hidden, and this disclosure is the essence of the gospel.</p>"
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        article = {
            "id": slug,
            "term": data["term"],
            "category": data["category"],
            "intro": data["intro"],
            "hitchcock_meaning": data.get("hitchcock_meaning"),
            "source_ids": data.get("source_ids", {}),
            "key_refs": data.get("key_refs", []),
            "sections": []
        }
        if merge_article(slug, article):
            written += 1
        else:
            skipped += 1
    print(f"BP m4: Misheal → Mystery: wrote {written}, skipped {skipped} existing.")


if __name__ == "__main__":
    main()
