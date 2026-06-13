"""
BP Article Synthesis — i: Ibhar → Izrahite
Covers Easton entries: Ibhar through Izrahite (65 entries)

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

Script: scripts/bp-i.py
Run: python3 scripts/bp-i.py
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
    "ibhar": {
        "id": "ibhar",
        "term": "Ibhar",
        "category": "people",
        "intro": "<p>Ibhar (meaning <em>election</em> or <em>he who is chosen</em>) was one of David's sons born to him during his reign in Jerusalem. He appears in the genealogical lists of 1 Chronicles 3:6 and 2 Samuel 5:15 among the children David fathered in Jerusalem after becoming king over all Israel. The name indicates divine favor or selection, consistent with the broader theological reflection on David's dynasty as chosen by God.</p><p>Beyond his inclusion in the royal genealogy, Ibhar receives no individual narrative in Scripture. He stands among a large group of David's sons in Jerusalem — a list that underscores the fulfillment of God's promises to establish David's house — but is otherwise unknown in biblical history.</p>",
        "hitchcock_meaning": "election; he that is chosen",
        "source_ids": {"easton": "ibhar", "smith": "ibhar", "isbe": "ibhar"},
        "key_refs": ["1 Chronicles 3:6", "2 Samuel 5:15"]
    },
    "ibleam": {
        "id": "ibleam",
        "term": "Ibleam",
        "category": "places",
        "intro": "<p>Ibleam was a Canaanite city in the territory assigned to Manasseh, located along the road leading from the Plain of Esdraelon up to the highland plateau — the same general corridor that passed near Megiddo. The city is listed in Joshua 17:11 among the places within Issachar and Asher that Manasseh was supposed to control, though Joshua 17:12 and Judges 1:27 record that Manasseh failed to drive out the Canaanites there, so the Canaanites continued to dwell in Ibleam.</p><p>Ibleam appears at a critical moment in the history of the northern monarchy: it was near Ibleam, at the ascent of Gur, that King Ahaziah of Judah was mortally wounded by Jehu's archers during Jehu's coup against the house of Ahab (2 Kings 9:27). The city is identified in 1 Chronicles 6:70 as assigned to the Kohathite Levites, under the variant name Bileam. Its general location is near modern Jenin in the Jezreel Valley region.</p>",
        "hitchcock_meaning": "ancient people; people decreasing",
        "source_ids": {"easton": "ibleam", "smith": "ibleam", "isbe": "ibleam"},
        "key_refs": ["Joshua 17:11", "Judges 1:27", "2 Kings 9:27", "1 Chronicles 6:70"]
    },
    "ibzan": {
        "id": "ibzan",
        "term": "Ibzan",
        "category": "people",
        "intro": "<p>Ibzan (meaning <em>illustrious</em> or <em>father of a target</em>) was the tenth judge of Israel, succeeding Jephthah. He was from Bethlehem — most likely Bethlehem in Zebulun rather than the more famous Bethlehem of Judah, though some traditions have identified him with both. According to Judges 12:8–10, Ibzan judged Israel for seven years and was noted for his large family: thirty sons and thirty daughters. He arranged marriages for all of them outside his own clan, a detail that suggests both his wealth and his diplomatic range.</p><p>Like the minor judges Tola, Jair, and Elon, Ibzan's tenure is described briefly, with no military exploits or specific theological crises recorded. His judgeship appears to have been a period of relative administrative stability. He died and was buried at Bethlehem. The stress on his many children reflects the ancient Near Eastern value of a large household as a mark of divine blessing and social influence.</p>",
        "hitchcock_meaning": "father of a target; father of coldness",
        "source_ids": {"easton": "ibzan", "smith": "ibzan", "isbe": "ibzan"},
        "key_refs": ["Judges 12:8"]
    },
    "ice": {
        "id": "ice",
        "term": "Ice",
        "category": "concepts",
        "intro": "<p>Ice in Scripture appears primarily in poetic and wisdom literature as a figure for the power and majesty of God over creation. Job 6:16 describes wadis dark with ice and into which snow vanishes — imagery of the desolate wilderness. Job 38:29 presents God's rhetorical question: \"Out of whose womb did the ice come?\" — placing frost and ice among the mysteries of creation that only God controls. Psalm 147:17 describes God casting forth ice like morsels, asking \"who can stand before his cold?\" and then melting them with his word.</p><p>Ice and frost are relatively rare in the lowland regions of ancient Israel but occur in higher elevations — the mountains of Lebanon and the hill country — particularly in winter months. The Old Testament uses ice as a symbol of divine sovereign power over nature and as a concrete image of the extremities of weather that distinguish God's creation from human control. No specific ritual or legal significance attaches to ice in biblical law; its appearances are consistently in the domain of poetry, doxology, and wisdom reflection on the natural order.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ice", "isbe": "ice"},
        "key_refs": ["Job 6:16", "Job 38:29", "Psalms 147:17"]
    },
    "ichabod": {
        "id": "ichabod",
        "term": "Ichabod",
        "category": "people",
        "intro": "<p>Ichabod (meaning <em>where is the glory?</em> or <em>no glory</em>) was the son of Phinehas and grandson of Eli the priest. He was born on the day that the ark of God was captured by the Philistines at the Battle of Aphek (1 Samuel 4:1–22). His mother, dying in childbirth upon hearing the catastrophic news — that her father-in-law Eli had fallen dead, that her husband Phinehas had been killed, and that the ark had been taken — named the child Ichabod as a theological statement of mourning: \"The glory has departed from Israel\" (1 Samuel 4:19–22).</p><p>The name encapsulates the crisis at the end of the Eli era. The loss of the ark represented not merely a military defeat but the apparent abandonment of Israel's sanctuary by the divine presence. Ichabod thus becomes a living emblem of national and spiritual collapse. He is mentioned again by name only once more, in 1 Samuel 14:3, where his brother Ahijah serves as priest — a brief genealogical note placing the dynasty of Eli in the background of Saul's kingship.</p>",
        "hitchcock_meaning": "where is the glory? or, no glory",
        "source_ids": {"easton": "ichabod", "smith": "ichabod", "isbe": "ichabod"},
        "key_refs": ["1 Samuel 4:19", "1 Samuel 4:21", "1 Samuel 14:3"]
    },
    "iconium": {
        "id": "iconium",
        "term": "Iconium",
        "category": "places",
        "intro": "<p>Iconium was the capital of the ancient region of Lycaonia in south-central Asia Minor (modern Konya in Turkey), situated on a fertile plain at the edge of the Anatolian plateau. By the New Testament period it was part of the Roman province of Galatia. Paul and Barnabas visited Iconium on the first missionary journey (Acts 13:51–14:5), preaching in the synagogue and winning a large number of both Jews and Gentiles, but eventually fleeing when a plot was laid against them to stone them — a division in the city between those who sided with the apostles and those with the Jewish opponents.</p><p>Paul returned to Iconium on the second missionary journey to strengthen the churches (Acts 16:2), and the city's congregation was clearly established. In 2 Timothy 3:11 Paul refers to his persecutions at Antioch, Iconium, and Lystra as examples of suffering he endured but from which the Lord delivered him. Iconium remained a significant city in the early church's eastern mission and is listed among Paul's key sites of ministry in Asia Minor. The Hitchcock meaning of <em>coming</em> reflects the Greek form of the name.</p>",
        "hitchcock_meaning": "coming",
        "source_ids": {"easton": "iconium", "smith": "iconium", "isbe": "iconium"},
        "key_refs": ["Acts 13:50", "Acts 13:51", "Acts 14:1", "2 Timothy 3:11"]
    },
    "idalah": {
        "id": "idalah",
        "term": "Idalah",
        "category": "places",
        "intro": "<p>Idalah was a town near the western border of the tribe of Zebulun in northern Canaan, listed in Joshua 19:15 among the cities that fell within Zebulun's inheritance when the land was divided among the tribes. The name has been interpreted as meaning <em>snares</em>, though the etymology is uncertain. Its exact site has not been definitively identified by modern archaeology, though some scholars have proposed locations in the lower Galilee region consistent with the tribal boundaries described in Joshua 19.</p><p>Beyond its single mention in the boundary list of Zebulun, Idalah receives no further narrative in Scripture. It represents one of many smaller Canaanite settlements that were absorbed into the Israelite tribal territories during the conquest and settlement period, their names preserved in the administrative records embedded in the book of Joshua.</p>",
        "hitchcock_meaning": "the hand of slander, or of cursing",
        "source_ids": {"easton": "idalah", "smith": "idalah", "isbe": "idalah"},
        "key_refs": ["Joshua 19:15"]
    },
    "iddo": {
        "id": "iddo",
        "term": "Iddo",
        "category": "people",
        "intro": "<p>Iddo is the name of several distinct biblical figures. (1.) A Gershonite Levite, son of Joah, ancestor of the musician Asaph (1 Chronicles 6:21). (2.) The son of Zechariah and officer over the half-tribe of Manasseh in Gilead under David (1 Chronicles 27:21). (3.) A prophet and seer during the reigns of Solomon, Rehoboam, and Abijah whose visions and chronicles are cited as source documents in 2 Chronicles 9:29; 12:15; and 13:22 — making him one of the prophetic historians whose works do not survive independently but were incorporated into the materials behind Chronicles. (4.) The grandfather of the prophet Zechariah (Zechariah 1:1; Ezra 5:1; 6:14; Nehemiah 12:4, 16), whose family returned from the Babylonian exile with Zerubbabel.</p><p>The prophetic Iddo of Solomon's era is particularly notable because his \"visions\" and \"commentary\" are named alongside those of Nathan and Ahijah as records of the events of Solomon's reign. The grandfather of Zechariah adds further significance to the name, as Zechariah's visionary prophecies became foundational texts for understanding the post-exilic restoration and, later, messianic expectation in the New Testament.</p>",
        "hitchcock_meaning": "his band; power; praise",
        "source_ids": {"easton": "iddo", "smith": "iddo", "isbe": "iddo"},
        "key_refs": ["1 Chronicles 6:21", "1 Chronicles 27:21", "2 Chronicles 12:15", "Zechariah 1:1"]
    },
    "idol": {
        "id": "idol",
        "term": "Idol",
        "category": "concepts",
        "intro": "<p>Idol translates several distinct Hebrew words in the Old Testament, each carrying a different nuance of contempt or description: <em>aven</em> (nothingness, vanity; Isaiah 41:29; 66:3), <em>elilim</em> (things of naught; Leviticus 19:4; 26:1), <em>gillulim</em> (logs, dung-pellets; a derogatory term used especially in Ezekiel), <em>atsabim</em> (things causing grief; 1 Samuel 31:9), and <em>matstsebah</em> (a standing pillar or image). The variety of terms reflects the breadth of Israelite opposition to all forms of image worship, expressed through vocabulary that deliberately diminishes the dignity of foreign gods.</p><p>The manufacture and veneration of idols was one of the primary covenantal prohibitions for Israel (Exodus 20:4–5; Deuteronomy 5:8–9), and the prophets returned repeatedly to the absurdity of idol-making — a craftsman cutting down a tree, using half for fuel and shaping the other half into a god (Isaiah 44:9–20). In the New Testament, Paul addresses idol meat in Corinth (1 Corinthians 8–10), affirming that an idol is nothing in the world — a restatement of the prophetic polemic — while warning against participation in pagan sacrificial meals as a form of spiritual communion with demons (1 Corinthians 10:19–21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "idol", "smith": "idol"},
        "key_refs": ["Isaiah 41:29", "Exodus 20:4", "Isaiah 44:17", "1 Corinthians 10:19"]
    },
    "idolatry": {
        "id": "idolatry",
        "term": "Idolatry",
        "category": "concepts",
        "intro": "<p>Idolatry — the worship of images or the rendering of divine honor to any created thing — is one of the central prohibitions of the biblical covenant. Its origins in human history are traced in Romans 1:21–23: knowing God, humanity exchanged the glory of the incorruptible God for the likeness of created things. The Old Testament shows idolatry already present among Abraham's ancestors in Mesopotamia (Joshua 24:2) and within Rachel's own household (Genesis 31:19), and it remained a persistent temptation throughout Israel's history despite the prophets' repeated condemnation.</p><p>The covenant at Sinai made the prohibition of idolatry the first and second of the Ten Commandments (Exodus 20:3–6). Israel's departure into idolatry — particularly the worship of Baal, Asherah, and the calf images set up at Bethel and Dan by Jeroboam — is treated in the historical books as the primary cause of the divine judgments that led to exile. The prophets used the metaphor of marital unfaithfulness to describe idolatry's covenantal character (Hosea; Ezekiel 16; 20). In the New Testament, covetousness is identified as a form of idolatry (Colossians 3:5; Ephesians 5:5), expanding the concept beyond physical images to any displacement of God from his proper place of ultimate allegiance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "idolatry", "smith": "idolatry", "isbe": "idolatry"},
        "key_refs": ["Romans 1:21", "Exodus 20:3", "1 Kings 12:28", "Colossians 3:5"]
    },
    "idumaea": {
        "id": "idumaea",
        "term": "Idumaea",
        "category": "places",
        "intro": "<p>Idumaea is the Greek and Latin form of Edom, the territory south and southeast of the Dead Sea traditionally associated with Esau's descendants. In the Old Testament the region is called Edom; the name Idumaea reflects the Greek rendering that became standard in the Hellenistic and Roman periods. The prophets pronounced judgment on Edom repeatedly for its hostility to Israel, most notably at the time of Jerusalem's fall to Babylon (Isaiah 34:5–6; Ezekiel 35:15; 36:5; Obadiah).</p><p>By the time of the Maccabees, Idumaea's population had been pushed northward and partially absorbed into Judaea. John Hyrcanus forcibly converted the Idumaeans to Judaism around 125 BC, and their absorption into the Jewish people produced the Herodian dynasty — the family of Herod the Great, an Idumaean by descent. Mark 3:8 mentions Idumaea as one of the regions from which crowds came to hear Jesus, reflecting its incorporation into the broader Judaean world by the first century. The Herodian connection makes Idumaea's history directly relevant to the political setting of the Gospels.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "idumaea"},
        "key_refs": ["Isaiah 34:5", "Ezekiel 35:15", "Mark 3:8"]
    },
    "igal": {
        "id": "igal",
        "term": "Igal",
        "category": "people",
        "intro": "<p>Igal (meaning <em>redeemed</em> or <em>avenger</em>) is the name of two biblical figures. (1.) The son of Joseph of the tribe of Issachar, sent as one of the twelve spies to survey the land of Canaan under Moses (Numbers 13:7). He was among the ten who brought back a discouraging report, arguing that Israel could not overcome the Canaanites. (2.) One of David's thirty mighty warriors, described as the son of Nathan of Zobah (2 Samuel 23:36), also listed as Joel the brother of Nathan in 1 Chronicles 11:38 — a textual discrepancy possibly due to scribal error in transmission.</p><p>A third person named Igal appears in 1 Chronicles 3:22 among the descendants of Zerubbabel in the post-exilic Davidic line. The name's meaning of redemption or vindication carries theological resonance in the context of Israel's covenant hope, though neither the spy nor the warrior receives extended narrative beyond his listing in these records.</p>",
        "hitchcock_meaning": "redeemed; defiled",
        "source_ids": {"easton": "igal", "smith": "igal", "isbe": "igal"},
        "key_refs": ["Numbers 13:7", "2 Samuel 23:36", "1 Chronicles 3:22"]
    },
    "iim": {
        "id": "iim",
        "term": "Iim",
        "category": "places",
        "intro": "<p>Iim (meaning <em>ruins</em>) refers to two distinct locations in the Old Testament. (1.) A city in the far south of Judah listed in Joshua 15:29 among the towns of the Negev tribal allotment. Its exact site is uncertain, though it lay in the arid southern borderlands of the tribe. (2.) A wilderness encampment of Israel during the Exodus journey, mentioned in Numbers 33:45 under the fuller name Ije-abarim (Ruins of Abarim) — the form used at that stage of the itinerary — though some manuscripts treat Iim and Ije-abarim as separate stations.</p><p>The name reflects the landscape of ruins or heaps that characterized certain sites in the Negev and the Trans-jordanian wilderness. Beyond the brief topographical mentions in these boundary and itinerary lists, neither location receives further narrative attention in the biblical text.</p>",
        "hitchcock_meaning": "heaps of Hebrews, or of angry men",
        "source_ids": {"easton": "iim", "smith": "iim", "isbe": "iim"},
        "key_refs": ["Joshua 15:29", "Numbers 33:45"]
    },
    "ije-abarim": {
        "id": "ije-abarim",
        "term": "Ije-abarim",
        "category": "places",
        "intro": "<p>Ije-abarim (meaning <em>ruins of Abarim</em> or <em>heaps of the passages</em>) was the forty-seventh encampment of Israel during the wilderness wanderings, listed in Numbers 33:44–45. It was situated on the eastern frontier of Moab, in the region east of the Dead Sea associated with the Abarim mountain range — the same highlands that include Mount Nebo, where Moses would later view the promised land before his death. The Israelites camped here after leaving Oboth and before moving to Dibon-gad.</p><p>The site marks Israel's approach to the borders of Moab and the final stages of the wilderness journey before entering the Transjordan. The Abarim range was the geographical boundary between the desert and the territories Israel would need to negotiate passage through — setting up the encounters with the kings of Sihon and Og described in Numbers 21. The name's emphasis on <em>ruins</em> or <em>heaps</em> may indicate the topographical character of the area rather than any previous settlement.</p>",
        "hitchcock_meaning": "heaps of Hebrews, or of passengers",
        "source_ids": {"easton": "ije-abarim", "isbe": "ije-abarim"},
        "key_refs": ["Numbers 33:44", "Numbers 33:45"]
    },
    "ijon": {
        "id": "ijon",
        "term": "Ijon",
        "category": "places",
        "intro": "<p>Ijon was a fortified city in the territory of Naphtali in northern Israel, situated near the headwaters of the Jordan River in the Huleh basin region. The name may mean <em>ruin</em> or <em>a fountain</em>. Ijon is mentioned in two military contexts: Ben-hadad of Syria captured it along with Dan and Abel-beth-maacah during his invasion of northern Israel at the instigation of King Asa of Judah (1 Kings 15:20; 2 Chronicles 16:4), and Tiglath-pileser III of Assyria captured it again as part of his campaign against the northern kingdom during the reign of Pekah (2 Kings 15:29), after which its population was deported to Assyria.</p><p>These two captures illustrate the vulnerability of Naphtali's northernmost cities to invasion along the natural corridor that ran through the Huleh valley from the north. The site is generally identified with Tell ed-Dibbin, north of Lake Huleh, and represents one of the first Israelite territories to fall to Assyrian expansion in the 730s BC.</p>",
        "hitchcock_meaning": "look; eye; fountain",
        "source_ids": {"easton": "ijon", "smith": "ijon", "isbe": "ijon"},
        "key_refs": ["1 Kings 15:20", "2 Kings 15:29"]
    },
    "ilai": {
        "id": "ilai",
        "term": "Ilai",
        "category": "people",
        "intro": "<p>Ilai the Ahohite was one of David's mighty warriors, listed among the thirty in 1 Chronicles 11:29. He is identified as an Ahohite — a member of the clan descended from Ahoah, a Benjaminite family that produced several of David's most distinguished soldiers, including Eleazar son of Dodo, one of the three chief heroes. In the parallel list of 2 Samuel 23:28 the name appears as Zalmon the Ahohite, a textual variation that may reflect scribal error or a dual name.</p><p>Beyond his inclusion in the roster of David's warriors, Ilai receives no individual narrative in Scripture. The list of the thirty in 1 Chronicles 11 and 2 Samuel 23 preserves the names of the elite fighting force that formed the nucleus of David's military establishment, many of whom joined him during his years as an outlaw in the wilderness before he became king.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ilai", "smith": "ilai", "isbe": "ilai"},
        "key_refs": ["1 Chronicles 11:29", "2 Samuel 23:28"]
    },
    "illyricum": {
        "id": "illyricum",
        "term": "Illyricum",
        "category": "places",
        "intro": "<p>Illyricum was the Roman province occupying the eastern Adriatic coast and its hinterland — roughly the territory of modern Croatia, Bosnia, and western Serbia. It lay northwest of Macedonia and formed the northwestern boundary of Paul's missionary activity in the eastern Mediterranean. In Romans 15:19 Paul states that he has fully preached the gospel of Christ \"from Jerusalem and round about unto Illyricum\" — indicating that by the time of writing he considered his work in the east complete and was ready to move westward to Spain via Rome.</p><p>The reference implies Paul had reached Illyricum, though Acts does not record a specific mission there. Most scholars understand the visit to have occurred during the period described in Acts 20:2, when Paul traveled through Macedonia before returning to Greece. Illyricum represents the westernmost point of Paul's confirmed missionary geography in the eastern empire, and the verse in Romans is one of the few explicit geographic claims Paul makes about the extent of his completed ministry. The province was later called Dalmatia; 2 Timothy 4:10 mentions Titus going to Dalmatia, which may overlap with this region.</p>",
        "hitchcock_meaning": "joy; rejoicing",
        "source_ids": {"easton": "illyricum", "smith": "illyricum", "isbe": "illyricum"},
        "key_refs": ["Romans 15:19", "Acts 20:2", "2 Timothy 4:10"]
    },
    "imagery": {
        "id": "imagery",
        "term": "Imagery",
        "category": "concepts",
        "intro": "<p>Imagery in the biblical context appears most significantly in the phrase \"chambers of his imagery\" in Ezekiel 8:12, where the prophet is shown in vision the secret idolatrous practices of the elders of Israel in Jerusalem. Seventy elders stand before images on the walls — carvings or paintings of animals and abominable creatures representing the gods of Egypt and other nations — burning incense in a hidden inner room of the temple precinct. They justify their actions by saying \"the LORD seeth us not; the LORD hath forsaken the earth.\"</p><p>The scene represents the depth of the syncretism and apostasy that Ezekiel's visions expose in Jerusalem prior to the Babylonian destruction. \"Chambers of imagery\" thus refers to private rooms or recesses where forbidden images were venerated away from public view — the hidden corruption that God sees even when worshippers believe themselves concealed. The passage is one of the most vivid in the prophetic literature for depicting the inner spiritual condition of Jerusalem before judgment fell in 586 BC.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "imagery", "isbe": "imagery"},
        "key_refs": ["Ezekiel 8:12"]
    },
    "imla": {
        "id": "imla",
        "term": "Imla",
        "category": "people",
        "intro": "<p>Imla (also spelled Imlah) was the father of Micaiah, the prophet who confronted Ahab and Jehoshaphat before the Battle of Ramoth-gilead. In 1 Kings 22:8–9 and 2 Chronicles 18:7–8, when Jehoshaphat requests a prophet of the LORD beyond Ahab's four hundred court prophets, Ahab responds: \"There is yet one man, Micaiah the son of Imla, by whom we may inquire of the LORD: but I hate him; for he doth not prophesy good concerning me.\" Imla's son then delivers the famous vision of the lying spirit among the heavenly court and the prophecy of Ahab's death.</p><p>Imla himself receives no narrative of his own; he is identified only as Micaiah's father. His name means <em>replenisher</em>, and he is remembered entirely through the courage of his son, who stood alone against the false optimism of Ahab's court prophets and paid for his faithfulness with imprisonment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "imla", "smith": "imla"},
        "key_refs": ["2 Chronicles 18:7", "1 Kings 22:8"]
    },
    "immanuel": {
        "id": "immanuel",
        "term": "Immanuel",
        "category": "concepts",
        "intro": "<p>Immanuel (Hebrew <em>Immanu El</em>, meaning <em>God with us</em>) is the name given in Isaiah 7:14 to a child whose birth is announced as a sign to King Ahaz of Judah: \"Behold, the virgin shall conceive and bear a son, and shall call his name Immanuel.\" In its immediate historical context the sign relates to the Syro-Ephraimite crisis of 734–733 BC, assuring Ahaz that the threat from the kingdoms of Syria and Israel would pass before the child reaches an age of moral discernment (Isaiah 7:15–16). The same name appears in Isaiah 8:8, where the land of Judah is called \"thy land, O Immanuel,\" presenting the name as a divine title associated with protection of the covenant land.</p><p>The New Testament's definitive interpretation of Isaiah 7:14 appears in Matthew 1:22–23, where the Gospel writer cites it as fulfilled in the birth of Jesus, born of a virgin and given the name that summarizes his identity: God present with his people in human form. The theological weight of \"Immanuel\" thus moves from a sign in the context of eighth-century Judah to the christological center of the incarnation — the claim that in Jesus of Nazareth, God himself took up dwelling among humanity.</p>",
        "hitchcock_meaning": "God with us",
        "source_ids": {"easton": "immanuel", "smith": "immanuel", "isbe": "immanuel"},
        "key_refs": ["Isaiah 7:14", "Isaiah 8:8", "Matthew 1:23"]
    },
    "immer": {
        "id": "immer",
        "term": "Immer",
        "category": "people",
        "intro": "<p>Immer was the head of the sixteenth of the twenty-four courses of priests established by David for service at the sanctuary (1 Chronicles 24:14). The priestly course of Immer became one of the more prominent divisions, as Jeremiah's antagonist Pashhur held the office of chief governor of the temple and was identified as \"son of Immer the priest\" (Jeremiah 20:1), suggesting continued leadership within that family. The name means <em>talkative</em> or <em>a lamb</em>.</p><p>After the Babylonian exile, members of the family of Immer were among those who returned to Judah: Ezra 2:37 and Nehemiah 7:40 record 1,052 members of the \"children of Immer\" among the returning exiles. Additionally, Ezra 2:59 lists a place called Immer in Babylonia from which some returned, though they could not prove their Israelite descent. The name thus represents both a priestly family line and possibly a place of Babylonian settlement associated with the exiled community.</p>",
        "hitchcock_meaning": "saying; speaking; a lamb",
        "source_ids": {"easton": "immer", "smith": "immer", "isbe": "immer"},
        "key_refs": ["1 Chronicles 24:14", "Jeremiah 20:1", "Ezra 2:37"]
    },
    "immortality": {
        "id": "immortality",
        "term": "Immortality",
        "category": "concepts",
        "intro": "<p>Immortality — the perpetuity of personal existence beyond death — is a doctrine developed progressively across both Testaments. The Old Testament does not systematically expound a doctrine of the afterlife, though it assumes the continuation of the person after death in Sheol, the realm of the departed. The patriarchs are \"gathered to their people\" at death (Genesis 25:8; 49:33), and Enoch's translation without dying (Genesis 5:24) and Elijah's ascent in a chariot of fire (2 Kings 2:11) are presented as exceptional divine acts that bear witness to a life beyond the grave. The Psalms occasionally express hope for divine presence beyond death (Psalms 16:10–11; 49:15; 73:24).</p><p>The clearest Old Testament statement of bodily resurrection and immortality is Daniel 12:2–3: \"many of them that sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt.\" In the New Testament, immortality is firmly grounded in the resurrection of Christ: \"our Savior Jesus Christ, who has abolished death and brought life and immortality to light through the gospel\" (2 Timothy 1:10). Paul distinguishes the mortal body that is sown in corruption from the immortal, incorruptible body that is raised (1 Corinthians 15:42–54), making the resurrection the basis for the believer's hope of immortality.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "immortality"},
        "key_refs": ["Daniel 12:2", "2 Timothy 1:10", "1 Corinthians 15:53", "Psalms 16:10"]
    },
    "imputation": {
        "id": "imputation",
        "term": "Imputation",
        "category": "concepts",
        "intro": "<p>Imputation in biblical theology refers to the legal act of reckoning or crediting something to a person's account — treating it as belonging to them, whether or not it originated with them. The concept operates in both directions in Scripture. On one side, Adam's sin is imputed to all humanity: \"by one man sin entered the world, and death through sin, so death spread to all men, because all sinned\" (Romans 5:12). On the other, the faith of Abraham was imputed to him as righteousness (Genesis 15:6; Romans 4:3, 22), establishing the pattern of justification by faith apart from works.</p><p>The doctrine of the imputation of Christ's righteousness to the believer is central to the Pauline understanding of justification. God reckons to the sinner the perfect obedience of Christ, just as Christ bore the sin of the many. The Philemon reference (Philemon 1:18) provides a concrete illustration: Paul offers to have Onesimus's debt imputed to his own account. Reformed theology has developed the doctrine of imputation into a three-part structure — Adam's sin imputed to all, the sin of the elect imputed to Christ, and Christ's righteousness imputed to the elect — though the precise formulation has been contested across traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "imputation", "isbe": "imputation"},
        "key_refs": ["Romans 5:12", "Romans 4:3", "Genesis 15:6", "Philemon 1:18"]
    },
    "incarnation": {
        "id": "incarnation",
        "term": "Incarnation",
        "category": "concepts",
        "intro": "<p>Incarnation (from the Latin <em>incarnatio</em>, <em>becoming flesh</em>) denotes the act by which the eternal Son of God took human nature into personal union with his divine nature, being born as the man Jesus of Nazareth. The doctrinal foundation is John 1:14: \"the Word became flesh and dwelt among us.\" The pre-existent Word — who was with God and was God (John 1:1–2) — entered into genuine human existence, not as an appearance or a temporary possession of a human body, but as a real human being with a human nature complete in body, soul, and experience.</p><p>The New Testament presents the incarnation as a voluntary act of self-humbling: \"though he was rich, yet for your sakes he became poor\" (2 Corinthians 8:9); he \"emptied himself, taking the form of a servant\" (Philippians 2:7). Hebrews 2:14–17 grounds the incarnation in the necessity of the atonement: the Son shared in flesh and blood precisely so that through death he could destroy the power of death and become a merciful high priest, able to sympathize with human weakness. The incarnation is thus not merely the means of revelation but the precondition of the redemptive work — only a genuinely human mediator could represent humanity before God and offer the sacrifice that atoned for human sin.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "incarnation", "isbe": "incarnation"},
        "key_refs": ["John 1:14", "Philippians 2:7", "Hebrews 2:14", "1 Timothy 3:16"]
    },
    "incense": {
        "id": "incense",
        "term": "Incense",
        "category": "concepts",
        "intro": "<p>Incense was a fragrant compound burned on the altar of incense in the Israelite tabernacle and temple as a regular offering to God. The composition prescribed in Exodus 30:34–38 combined stacte, onycha, galbanum, and pure frankincense in equal parts — a formula declared holy and reserved exclusively for divine worship; making it for personal use was a capital offence. Incense was burned twice daily by the priests on the golden altar before the veil (Exodus 30:7–8), and on the Day of Atonement the high priest carried burning incense into the Holy of Holies to create a cloud of smoke over the mercy seat (Leviticus 16:12–13).</p><p>Psalm 141:2 interprets incense theologically: \"Let my prayer be counted as incense before you.\" This identification of prayer with rising incense becomes programmatic in the New Testament's imagery: Revelation 5:8 and 8:3–4 depict golden bowls of incense as the prayers of the saints offered before God's throne. The angel's offering of much incense with the prayers of all the saints in Revelation 8:3 presents intercession in the language of the temple's incense liturgy, now fulfilled in the heavenly sanctuary. Zechariah was burning incense in the temple when Gabriel announced the birth of John the Baptist (Luke 1:9–11), placing the incarnation narrative in the context of Israel's ongoing temple worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "incense", "smith": "incense", "isbe": "incense"},
        "key_refs": ["Exodus 30:34", "Psalms 141:2", "Revelation 8:3", "Luke 1:9"]
    },
    "india": {
        "id": "india",
        "term": "India",
        "category": "places",
        "intro": "<p>India appears in the Old Testament only in Esther 1:1 and 8:9, where it marks the eastern boundary of the empire of Ahasuerus (Xerxes): the kingdom extended \"from India even unto Ethiopia\" — a phrase indicating the vast reach of Persian dominion from the Indus Valley in the east to the Nile watershed in the west. The Hebrew <em>Hoddu</em> corresponds to the Persian <em>Hindush</em>, which referred to the territory of the Indus River region, roughly equivalent to the Sindh province of modern Pakistan.</p><p>The mention of India in Esther is geographical rather than narrative — it frames the scope of the empire within which the events of the book unfold, establishing that Jews of the diaspora were dispersed across the full extent of the known world of that era. Some ancient traditions connect the Ophir of Solomon's trading voyages with the Indian subcontinent (1 Kings 10:22; Ezekiel 27:15, 24), associating the trade in gold, ivory, and peacocks with Indian commerce, though Ophir's precise location remains debated.</p>",
        "hitchcock_meaning": "praise; law",
        "source_ids": {"easton": "india", "smith": "india", "isbe": "india"},
        "key_refs": ["Esther 1:1", "Esther 8:9"]
    },
    "inkhorn": {
        "id": "inkhorn",
        "term": "Inkhorn",
        "category": "concepts",
        "intro": "<p>Inkhorn in the King James Version translates the Hebrew <em>qeset</em>, which refers to a writing case or scribal palette — a container for ink used by scribes in the ancient Near East. In the vision of Ezekiel 9, God summons six men bearing slaughter weapons and one man clothed in linen with a writing case at his side (Ezekiel 9:2–3). This linen-clad figure is commanded to go through Jerusalem and mark the foreheads of those who sigh and cry over the abominations committed in the city — a mark that would protect them from the coming judgment carried out by the other six.</p><p>The inkhorn-bearer functions as a divine agent of distinction and protection within the judgment scene, foreshadowing the angelic sealing of the 144,000 in Revelation 7:3–4. The writing case itself was a characteristic implement of the professional scribe in Egyptian and Mesopotamian contexts, often consisting of a palette with wells for ink and a pen case, worn at the belt. In Ezekiel's vision its presence on the celestial figure marks him as an agent of record and preservation rather than destruction — the one who writes names for life rather than death.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "inkhorn"},
        "key_refs": ["Ezekiel 9:2", "Ezekiel 9:3", "Ezekiel 9:11"]
    },
    "inn": {
        "id": "inn",
        "term": "Inn",
        "category": "concepts",
        "intro": "<p>Inn in the modern sense — a commercial establishment offering paid lodging to travelers — was largely unknown in the ancient Near East. The Hebrew <em>malon</em> (a place of lodging for the night) and Greek <em>kataluma</em> (a guest room, lodging place) cover a range from private hospitality to public resting places along roads. The caravanserai or khan (<em>khan</em> in Arabic) was the typical waystop on major routes: an open courtyard enclosed by walls where travelers could shelter with their animals, with basic amenities but not typically private rooms or meals. The earliest mention of a lodging place in the Bible is in Genesis 42:27 and Exodus 4:24, where the word denotes a night encampment.</p><p>The most theologically significant New Testament uses cluster around the birth of Jesus: Luke 2:7 states that Mary laid the infant in a manger because \"there was no room in the inn\" (<em>kataluma</em>). The same word appears in Mark 14:14 and Luke 22:11 for the guest room where Jesus celebrated the Last Supper. Luke 10:34 uses the distinct word <em>pandocheion</em> (a public inn that accepts all comers) for the inn in the parable of the Good Samaritan — a more commercial establishment that received payment. The inn thus appears at both the beginning and the center of Jesus's ministry in Luke's narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "inn", "smith": "inn", "isbe": "inn"},
        "key_refs": ["Luke 2:7", "Luke 10:34", "Mark 14:14", "Exodus 4:24"]
    },
    "inspiration": {
        "id": "inspiration",
        "term": "Inspiration",
        "category": "concepts",
        "intro": "<p>Inspiration in biblical theology refers to the supernatural divine influence by which the human authors of Scripture wrote under God's guidance so that their writings carry the authority of God himself. The foundational text is 2 Timothy 3:16: \"All Scripture is God-breathed (<em>theopneustos</em>) and profitable for doctrine, for reproof, for correction, for instruction in righteousness.\" The Greek <em>theopneustos</em> — \"breathed out by God\" — indicates that Scripture is the product of divine breath or speech, analogous to God's creative word that brought the world into existence.</p><p>Peter's description of the prophetic process in 2 Peter 1:21 — \"holy men of God spoke as they were moved (<em>pheromenoi</em>, carried along) by the Holy Spirit\" — presents inspiration as the Spirit's sovereign oversight of human writers while preserving their individual personalities, vocabularies, and literary styles. The doctrine does not flatten Scripture into mechanical dictation but claims divine superintendence over the whole. Jesus's own treatment of Old Testament texts affirms their binding authority down to the letter (Matthew 5:18; John 10:35: \"Scripture cannot be broken\"), grounding the New Testament's use of the Old in a high view of the inspiration of the Hebrew canon.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "inspiration", "smith": "inspiration", "isbe": "inspiration"},
        "key_refs": ["2 Timothy 3:16", "2 Peter 1:21", "Matthew 5:18", "John 10:35"]
    },
    "intercession-of-christ": {
        "id": "intercession-of-christ",
        "term": "Intercession of Christ",
        "category": "concepts",
        "intro": "<p>The intercession of Christ is one dimension of his ongoing high priestly work: having completed his atoning sacrifice on earth, the ascended Christ lives to intercede for his people before the Father in heaven. Hebrews 7:25 states that \"he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them.\" This perpetual intercession is grounded in his finished sacrifice (Hebrews 9:12, 24) — he entered the heavenly sanctuary \"by his own blood\" and appears in the presence of God on behalf of his people.</p><p>Romans 8:34 places Christ's intercession alongside his death, resurrection, and exaltation at God's right hand as grounds for the believer's assurance: \"who is to condemn? Christ Jesus is the one who died — more than that, who was raised — who is at the right hand of God, who indeed is interceding for us.\" John 17 records the high priestly prayer in which Jesus intercedes for his disciples and for all who will believe through their word. The First Epistle of John identifies Christ as the believer's advocate (<em>parakletos</em>) with the Father (1 John 2:1), using legal language that overlaps with the intercessory role described in Hebrews.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "intercession-of-christ", "isbe": "intercession-of-christ"},
        "key_refs": ["Hebrews 7:25", "Romans 8:34", "John 17:20", "1 John 2:1"]
    },
    "intercession-of-the-spirit": {
        "id": "intercession-of-the-spirit",
        "term": "Intercession of the Spirit",
        "category": "concepts",
        "intro": "<p>The intercession of the Spirit refers to the Holy Spirit's work of praying on behalf of believers in a manner that transcends human speech and comprehension. Romans 8:26–27 is the primary text: \"the Spirit himself intercedes for us with groanings too deep for words. And he who searches hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to the will of God.\" This intercession supplements the believer's weakness in prayer — the Spirit takes up what the believer cannot articulate and presents it to God in complete alignment with the divine will.</p><p>The Spirit's intercession is distinguished from Christ's in its location and mode: Christ intercedes as the ascended high priest in the heavenly sanctuary before the Father (Hebrews 7:25; Romans 8:34), while the Spirit intercedes within the believer on earth. Together they constitute a double intercession that grounds the confidence of Romans 8:28: \"And we know that for those who love God all things work together for good.\" Jesus's promise in John 14:26 that the Father would send the Spirit as another <em>parakletos</em> (helper, advocate) connects the Spirit's intercessory role to the same legal-mediatorial category that describes Christ's advocacy in 1 John 2:1.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "intercession-of-the-spirit"},
        "key_refs": ["Romans 8:26", "Romans 8:27", "John 14:26"]
    },
    "iphedeiah": {
        "id": "iphedeiah",
        "term": "Iphedeiah",
        "category": "people",
        "intro": "<p>Iphedeiah (meaning <em>set free by Jehovah</em> or <em>redemption of the Lord</em>) was a chief of the tribe of Benjamin listed in the genealogy of 1 Chronicles 8:25. He appears among the heads of fathers' houses in the Benjaminite genealogy compiled in that chapter, placed in the line of Shashak. Beyond this single genealogical mention, Iphedeiah receives no individual narrative or further identification in Scripture.</p><p>The name carries the characteristic Yahwistic element <em>-iah</em>, indicating personal identification with Israel's covenantal God and reflecting the naming conventions common among the tribe of Benjamin. He represents one of many named Benjaminite leaders in the post-settlement period whose family records were preserved in the genealogical archives that the Chronicler drew upon.</p>",
        "hitchcock_meaning": "redemption of the Lord",
        "source_ids": {"easton": "iphedeiah", "smith": "iphedeiah"},
        "key_refs": ["1 Chronicles 8:25"]
    },
    "ira": {
        "id": "ira",
        "term": "Ira",
        "category": "people",
        "intro": "<p>Ira is the name of three men associated with David's reign, all bearing a name meaning <em>citizen</em> or <em>watchman</em>. (1.) Ira the Ithrite, one of David's thirty mighty warriors (2 Samuel 23:38; 1 Chronicles 11:40). (2.) Ira son of Ikkesh the Tekoite, another of the thirty, who also commanded the sixth division of David's monthly rotation of military officers (2 Samuel 23:26; 1 Chronicles 11:28; 27:9). (3.) Ira the Jairite, identified in 2 Samuel 20:26 as a priest (<em>kohen</em>) to David — a puzzling title since he was not from a Levitical family, suggesting perhaps the term is used loosely here for a chief minister or adviser.</p><p>The three Iras illustrate the diversity of backgrounds among David's close associates: warriors from Tekoa and the Ithrite clan, and an administrative official. The designation of a non-Levite as \"priest\" in 2 Samuel 20:26 has generated scholarly discussion about the flexibility of priestly terminology in early monarchic Israel before the later institutionalization of the Levitical system.</p>",
        "hitchcock_meaning": "watchman; making bare; pouring out",
        "source_ids": {"easton": "ira", "smith": "ira", "isbe": "ira"},
        "key_refs": ["2 Samuel 23:26", "2 Samuel 23:38", "2 Samuel 20:26"]
    },
    "irad": {
        "id": "irad",
        "term": "Irad",
        "category": "people",
        "intro": "<p>Irad (meaning <em>runner</em>, <em>wild ass</em>, or <em>fugitive</em>) was an antediluvian patriarch in the line of Cain, son of Enoch and father of Mehujael (Genesis 4:18). He belongs to the Cainite genealogy that parallels the Sethite line in Genesis 5 — a literary contrast between two branches of humanity, one marked by the culture of the city-builder Cain and the other by those who \"began to call on the name of the LORD\" (Genesis 4:26). The Cainite list ends with Lamech's boast of sevenfold vengeance, setting up the contrast with the covenant line through Seth.</p><p>Irad's name may be related to the ancient city of Eridu in Mesopotamia, one of the oldest cities in the Sumerian tradition, suggesting a possible etymological connection between the Cainite genealogy and ancient Mesopotamian traditions of primordial civilization. Beyond his position in the genealogy, Irad receives no narrative in Scripture.</p>",
        "hitchcock_meaning": "wild ass; heap of empire; fugitive",
        "source_ids": {"easton": "irad", "smith": "irad", "isbe": "irad"},
        "key_refs": ["Genesis 4:18"]
    },
    "iram": {
        "id": "iram",
        "term": "Iram",
        "category": "people",
        "intro": "<p>Iram (meaning <em>citizen</em> or <em>city-dweller</em>) was a chief (<em>alluf</em>) of Edom in the territory of Mount Seir, listed in the catalog of Edomite chiefs at the end of Genesis 36 (verse 43) and in the parallel list in 1 Chronicles 1:54. The Edomite chiefs listed in Genesis 36:40–43 are distinct from the earlier list of kings (36:31–39) and appear to represent a later system of tribal leadership — clan chiefs named after their districts or regions rather than a royal succession.</p><p>Iram is the last name in the Edomite chief list, closing the genealogical records of Esau's descendants. Beyond this closing position in the table, nothing further is recorded about Iram in Scripture. The Edomite genealogies in Genesis 36 serve as a closing bracket on the Esau narrative before Genesis 37 turns entirely to Joseph and the line of Jacob.</p>",
        "hitchcock_meaning": "the effusion of them; a high heap",
        "source_ids": {"easton": "iram", "smith": "iram", "isbe": "iram"},
        "key_refs": ["Genesis 36:43", "1 Chronicles 1:54"]
    },
    "irha-heres": {
        "id": "irha-heres",
        "term": "Irha-heres",
        "category": "places",
        "intro": "<p>Irha-heres appears in Isaiah 19:18 in a prophecy about Egypt's future conversion: \"In that day shall five cities in the land of Egypt speak the language of Canaan, and swear to the LORD of hosts; one shall be called, The city of destruction (<em>Ir ha-heres</em>).\" The phrase is textually uncertain — some Hebrew manuscripts read <em>Ir ha-heres</em> (city of destruction) while others read <em>Ir ha-heres</em> (city of the sun, i.e., Heliopolis). The Septuagint reads \"city of righteousness\" (<em>polis asedek</em>), and the Dead Sea Scrolls support the \"city of the sun\" reading.</p><p>The most probable original reading is \"City of the Sun\" (<em>Ir ha-Shemesh</em>), referring to Heliopolis (On), the great center of Egyptian sun-worship, which Isaiah prophesies will be converted to worship of the LORD. The alternative reading \"city of destruction\" may have been introduced by later scribes as a polemic against the Jewish temple at Leontopolis near Heliopolis, founded in the second century BC. The passage as a whole (Isaiah 19:16–25) presents one of the most striking universalist prophecies in the Old Testament, envisioning Egypt and Assyria worshipping alongside Israel as \"my people\" and \"the work of my hands.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "irha-heres"},
        "key_refs": ["Isaiah 19:18"]
    },
    "iron": {
        "id": "iron",
        "term": "Iron",
        "category": "concepts",
        "intro": "<p>Iron was the most technologically significant metal of the late biblical period, progressively replacing bronze in tools, weapons, and construction from around 1200 BC onward. Tubal-cain is identified in Genesis 4:22 as \"an instructor of every cutting instrument in bronze and iron,\" placing iron-working in the primeval history alongside the origins of music and city-building. The Israelites' lack of iron-working capability during the early settlement period is explicitly noted in 1 Samuel 13:19–22: the Philistines controlled the technology and prevented Israel from smithing, forcing them to depend on Philistine smiths even to sharpen agricultural tools. This monopoly gave the Philistines a significant military advantage.</p><p>Iron appears in legal and narrative contexts throughout the Old Testament: the altar was not to be built with iron tools (Deuteronomy 27:5), since iron's association with warfare made it unsuitable for the peace of the altar; iron chariots gave Canaanite enemies military superiority that Israel feared (Joshua 17:16; Judges 4:3); and Solomon's temple preparations included vast amounts of iron for nails, hinges, and structural work (1 Chronicles 22:3). Prophetically, iron symbolizes hardness and oppression (Deuteronomy 28:23; Isaiah 48:4), and the iron and clay feet of Nebuchadnezzar's statue in Daniel 2 represent the divided final kingdom before God establishes his own.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "iron", "smith": "iron"},
        "key_refs": ["Genesis 4:22", "1 Samuel 13:19", "Deuteronomy 27:5", "Daniel 2:33"]
    },
    "irrigation": {
        "id": "irrigation",
        "term": "Irrigation",
        "category": "concepts",
        "intro": "<p>Irrigation — the artificial watering of land — was a fundamental technology of ancient agriculture in the Near East, particularly in Egypt and Mesopotamia where it was essential to cultivation. The contrast between Egypt's irrigation-dependent agriculture and Canaan's rain-dependent farming is explicit in Deuteronomy 11:10–12: \"the land where you are entering to possess it is not like the land of Egypt, from which you have come, where you used to sow your seed and water it with your foot like a vegetable garden. But the land into which you are about to cross to possess it... drinks water from the rain of heaven.\" Watering \"with your foot\" likely refers to directing water channels with the foot, operating sluice gates, or working treadle-operated irrigation devices.</p><p>In Canaan, water was obtained primarily through rainfall, springs, cisterns, and seasonal wadis rather than large-scale canal systems. However, local irrigation was practiced where springs permitted — Jericho's lush cultivation depended on the Elisha spring, and Solomon's gardens (Ecclesiastes 2:6) involved irrigation pools. The image of a well-watered garden as an emblem of divine blessing runs throughout the Old Testament (Isaiah 58:11; Jeremiah 31:12), while drought and unwatered land symbolize divine judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "irrigation", "isbe": "irrigation"},
        "key_refs": ["Deuteronomy 11:10", "Isaiah 58:11", "Ecclesiastes 2:6"]
    },
    "isaac": {
        "id": "isaac",
        "term": "Isaac",
        "category": "people",
        "intro": "<p>Isaac (Hebrew <em>Yitzhak</em>, meaning <em>laughter</em>) was the son of Abraham and Sarah, born in their extreme old age as the miraculous fulfillment of God's covenant promise (Genesis 17:19; 21:1–3). His name commemorates both the laughter of disbelief with which his parents received the original announcement (Genesis 17:17; 18:12) and the joyful laughter of fulfillment at his birth (Genesis 21:6). Isaac is the child of promise — the heir through whom Abraham's descendants would be reckoned (Romans 9:7; Galatians 4:28) — and his birth over against the natural impossibility of Sarah's barrenness establishes the pattern of divine election: \"not the children of the flesh... but the children of the promise are counted as offspring\" (Romans 9:8).</p><p>The defining event of Isaac's life is the binding (<em>Akedah</em>) on Mount Moriah, where Abraham was commanded to offer him and was stopped by the angel of the LORD at the moment of sacrifice (Genesis 22). This near-sacrifice is the supreme test of Abraham's faith and the occasion of God's sworn covenant oath (Genesis 22:15–18). Isaac himself is relatively passive in the narrative — a figure through whom the promise passes rather than a man of dramatic action — though his blessing of Jacob and Esau (Genesis 27) drives the next generation's story. The New Testament cites him as a type of the resurrection (Hebrews 11:19).</p>",
        "hitchcock_meaning": "laughter",
        "source_ids": {"easton": "isaac", "smith": "isaac", "isbe": "isaac"},
        "key_refs": ["Genesis 21:3", "Genesis 22:1", "Romans 9:7", "Hebrews 11:17"]
    },
    "isaiah": {
        "id": "isaiah",
        "term": "Isaiah",
        "category": "people",
        "intro": "<p>Isaiah (Hebrew <em>Yeshayahu</em>, meaning <em>the salvation of the LORD</em>) was the son of Amoz and one of the greatest of the writing prophets of Israel, active in Jerusalem during the reigns of Uzziah, Jotham, Ahaz, and Hezekiah — a ministry spanning approximately 740–700 BC (Isaiah 1:1). He was a court prophet with direct access to the kings of Judah and played a decisive role in the crisis of the Assyrian invasion under Sennacherib, when he counseled Hezekiah to trust God rather than Egypt and prophesied the miraculous deliverance of Jerusalem (Isaiah 36–37; 2 Kings 19–20). Jewish tradition preserved in the Talmud and in the pseudepigraphical <em>Martyrdom of Isaiah</em> holds that he was killed by being sawn in two during the reign of Manasseh (cf. Hebrews 11:37).</p><p>Isaiah's ministry combined political counsel with the most soaring and theologically rich prophecy in the Hebrew canon. The great visions of his call (Isaiah 6), the Immanuel prophecy (Isaiah 7:14), the servant songs (Isaiah 42–53), and the New Creation (Isaiah 65–66) place him at the center of both Old Testament theology and New Testament citation. The Gospels, Acts, and Paul quote Isaiah more than any other prophet. The New Testament's announcement of Jesus as the fulfillment of Isaiah's servant who bears the sins of many (Isaiah 53; Acts 8:32–33) makes Isaiah indispensable to understanding the atonement.</p>",
        "hitchcock_meaning": "the salvation of the Lord",
        "source_ids": {"easton": "isaiah", "smith": "isaiah", "isbe": "isaiah"},
        "key_refs": ["Isaiah 1:1", "Isaiah 6:1", "Isaiah 53:4", "2 Kings 19:20"]
    },
    "isaiah-the-book-of": {
        "id": "isaiah-the-book-of",
        "term": "Isaiah, The Book of",
        "category": "concepts",
        "intro": "<p>The Book of Isaiah is the longest of the prophetic books and the most frequently quoted in the New Testament, standing at the head of the Major Prophets. Its sixty-six chapters fall naturally into two major sections: chapters 1–39, dominated by oracles of judgment against Judah, Israel, and the surrounding nations, punctuated by historical narratives from Hezekiah's reign; and chapters 40–66, which shift to consolation, restoration, and the vision of a new exodus and new creation. The transition at chapter 40 — \"Comfort, comfort my people\" — is among the most famous passages in the Hebrew Bible and is quoted in all four Gospels as the introduction to John the Baptist's ministry (Matthew 3:3; Mark 1:3; Luke 3:4; John 1:23).</p><p>The question of the book's authorship has been central in modern biblical scholarship. Traditional interpretation ascribes the entire book to the eighth-century prophet Isaiah son of Amoz. Critical scholarship since the eighteenth century has argued that chapters 40–55 (\"Deutero-Isaiah\") and 56–66 (\"Trito-Isaiah\") reflect a later period, with chapters 40–55 addressing the Babylonian exile by name (Isaiah 44:28; 45:1). The New Testament cites both halves of the book under the name Isaiah (John 12:38–41), supporting the unity of the book's canonical witness. Isaiah's servant songs (42:1–4; 49:1–6; 50:4–9; 52:13–53:12) are the most christologically rich texts in the Old Testament.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "isaiah-the-book-of"},
        "key_refs": ["Isaiah 1:1", "Isaiah 40:1", "Isaiah 53:1", "Matthew 3:3"]
    },
    "iscah": {
        "id": "iscah",
        "term": "Iscah",
        "category": "people",
        "intro": "<p>Iscah (meaning <em>she who looks out</em> or <em>one who anoints</em>) was the daughter of Haran and sister of Milcah, mentioned in Genesis 11:29 in the genealogical table of Terah's family at Ur of the Chaldees. Haran was the brother of Abraham, who died before his father Terah in the land of his nativity. Milcah, Iscah's sister, married Nahor, Abraham's other brother, and became the grandmother of Rebekah through their son Bethuel (Genesis 22:20–23).</p><p>Iscah herself receives no further narrative in Scripture. An ancient Jewish tradition, followed by Josephus and some early Christian interpreters, identified Iscah with Sarah, Abraham's wife — on the grounds that Sarah was Terah's daughter by another wife, making Abraham and Sarah half-siblings (Genesis 20:12), and that Iscah (\"she who looks out\") could describe the beautiful and watchful Sarah. This identification remains uncertain and is not accepted by most modern interpreters, but it reflects the early interest in harmonizing the genealogical data of Genesis 11.</p>",
        "hitchcock_meaning": "he that anoints; who looks",
        "source_ids": {"easton": "iscah", "smith": "iscah", "isbe": "iscah"},
        "key_refs": ["Genesis 11:29", "Genesis 11:31"]
    },
    "iscariot": {
        "id": "iscariot",
        "term": "Iscariot",
        "category": "people",
        "intro": "<p>Iscariot is the surname of Judas, the disciple who betrayed Jesus, and also of his father Simon (John 6:71; 13:26). The meaning and origin of the name have been debated: the most widely held interpretation derives it from the Hebrew <em>ish Qeriyoth</em> — \"man of Kerioth\" — identifying Judas as coming from Kerioth, a town in Judah (Joshua 15:25) or possibly Kerioth in Moab (Jeremiah 48:24). This would make Judas the only non-Galilean among the twelve apostles. Alternative derivations have proposed Aramaic terms for \"dagger-man\" (assassin) or \"red\" or \"liar,\" but the geographic derivation remains most plausible.</p><p>Judas served as the treasurer of the apostolic group (John 12:6; 13:29) and is consistently named last in the apostolic lists with the designation \"who betrayed him\" (Matthew 10:4; Mark 3:19; Luke 6:16). For thirty pieces of silver he led the temple authorities to arrest Jesus in Gethsemane (Matthew 26:14–16, 47–50). His subsequent remorse, return of the money, and death by hanging (Matthew 27:3–5; Acts 1:18–19) are recorded in terms that echo Old Testament prophetic patterns. Peter interprets the betrayal as a fulfillment of Psalms 41:9 and 69:25, and his replacement by Matthias restores the number of the twelve apostles.</p>",
        "hitchcock_meaning": "a man of murder; a hireling",
        "source_ids": {"easton": "iscariot", "smith": "iscariot", "isbe": "iscariot"},
        "key_refs": ["Matthew 26:14", "John 12:6", "Acts 1:18", "Matthew 27:3"]
    },
    "ish-bosheth": {
        "id": "ish-bosheth",
        "term": "Ish-bosheth",
        "category": "people",
        "intro": "<p>Ish-bosheth (meaning <em>man of shame</em>) was the youngest surviving son of Saul who was installed as king over Israel by Abner, Saul's general, following Saul's death at Mount Gilboa (2 Samuel 2:8–10). His original name was Esh-baal (<em>man of Baal</em>) according to 1 Chronicles 8:33 and 9:39 — the name Ish-bosheth being a later scribal substitution that replaced the Baal element with <em>bosheth</em> (shame), a common practice in the transmission of names containing Baal. He ruled for two years from Mahanaim in Transjordan over the northern tribes while David reigned in Hebron over Judah.</p><p>Ish-bosheth's reign was marked by the long war between his house and David's (2 Samuel 3:1) and by his fatal conflict with Abner over a concubine of Saul's (2 Samuel 3:7–11), which led Abner to transfer his allegiance to David. Shortly after Abner's assassination by Joab, Ish-bosheth was murdered in his bed by two of his own captains, Baanah and Rechab, who brought his severed head to David expecting a reward — and were instead executed for their treachery (2 Samuel 4:5–12). David's reaction established his consistent principle of not profiting from violence against Saul's house.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ish-bosheth", "isbe": "ish-bosheth"},
        "key_refs": ["2 Samuel 2:8", "2 Samuel 3:7", "2 Samuel 4:5", "1 Chronicles 8:33"]
    },
    "ishbak": {
        "id": "ishbak",
        "term": "Ishbak",
        "category": "people",
        "intro": "<p>Ishbak (meaning <em>leaving</em> or <em>who is empty</em>) was one of the sons of Abraham by his concubine Keturah, listed in Genesis 25:2 and 1 Chronicles 1:32. He was a brother of Zimran, Jokshan, Medan, Midian, and Shuah — the six sons born to Abraham after Sarah's death who became ancestors of the peoples of northern Arabia and the surrounding regions. Abraham gave gifts to these sons and sent them away from Isaac eastward, to the east country (Genesis 25:6), separating them from the line of the covenant promise that passed exclusively through Isaac.</p><p>Ishbak's descendants are not separately traced in Scripture, and no tribe or people group is definitively identified with his name. He represents one of the many lines of descent from Abraham that populated the ancient Near Eastern world beyond the covenant community, illustrating that the scope of Abraham's fatherhood extended beyond Israel even as the covenant promise was narrowed to the Isaacline.</p>",
        "hitchcock_meaning": "who is empty or exhausted; leaving",
        "source_ids": {"easton": "ishbak", "smith": "ishbak", "isbe": "ishbak"},
        "key_refs": ["Genesis 25:2", "1 Chronicles 1:32"]
    },
    "ishbi-benob": {
        "id": "ishbi-benob",
        "term": "Ishbi-benob",
        "category": "people",
        "intro": "<p>Ishbi-benob (meaning <em>my seat at Nob</em> or <em>respiration; conversion</em>) was one of the Rephaim — the race of giant warriors — who confronted David in battle late in his reign (2 Samuel 21:16–17). He bore a new bronze spear weighing three hundred shekels and was girded with a new sword, and he sought to kill David. Abishai son of Zeruiah came to David's rescue and killed Ishbi-benob. The incident prompted David's commanders to swear that he would no longer go out with them to battle, for fear that the light of Israel would be extinguished.</p><p>Ishbi-benob is one of four descendants of the giant (Rapha) in Gath whose deaths at the hands of David's warriors are recorded in 2 Samuel 21:15–22 — a passage that closes the narrative of the Philistine wars and represents the final victories of David's military career. The Rephaim, or giants, appear throughout the conquest narratives as the aboriginal warrior-race of Canaan whose continued presence posed a physical threat to Israel long after the main campaigns.</p>",
        "hitchcock_meaning": "respiration; conversion; taking",
        "source_ids": {"easton": "ishbi-benob", "isbe": "ishbi-benob"},
        "key_refs": ["2 Samuel 21:16", "2 Samuel 21:17"]
    },
    "ishi": {
        "id": "ishi",
        "term": "Ishi",
        "category": "concepts",
        "intro": "<p>Ishi (<em>my husband</em>) is a symbolic name in Hosea 2:16, part of God's oracle of restoration to unfaithful Israel: \"And it shall come to pass in that day, saith the LORD, that thou shalt call me Ishi; and shalt call me no more Baali.\" The verse draws on the double meaning of Hebrew terms for husband: <em>ishi</em> (my man/husband, intimate and personal) versus <em>baali</em> (my master/lord, also the name of the Canaanite deity Baal). In the restored relationship God promises, Israel will address him with the intimacy of a wife toward a loving husband rather than the servile address of a subject to a master — or worse, with the name of a pagan god.</p><p>The theological force of the verse lies in the marriage metaphor that runs throughout Hosea: Israel's pursuit of Baal worship is an act of marital unfaithfulness, and the divine promise is restoration of a right covenantal marriage. By eliminating <em>Baali</em> from Israel's vocabulary — \"For I will take away the names of Baalim out of her mouth\" (Hosea 2:17) — God both breaks the idolatrous association and transforms the covenantal address into one of intimacy. The passage is foundational to the New Testament's use of the betrothal and marriage metaphor for the relationship between Christ and the church.</p>",
        "hitchcock_meaning": "salvation",
        "source_ids": {"easton": "ishi", "smith": "ishi"},
        "key_refs": ["Hosea 2:16", "Hosea 2:17"]
    },
    "ishmael": {
        "id": "ishmael",
        "term": "Ishmael",
        "category": "people",
        "intro": "<p>Ishmael (meaning <em>God hears</em>) was Abraham's firstborn son, born of Hagar the Egyptian maidservant when Sarah was still barren (Genesis 16:1–15). The name was given by God before his birth, in response to Hagar's cry of affliction in the wilderness, and commemorates the divine hearing of human distress. Ishmael was circumcised at age thirteen when Abraham received the covenant of circumcision (Genesis 17:23–26), and for thirteen years he was Abraham's only son and presumed heir.</p><p>The birth of Isaac displaced Ishmael from the covenant inheritance, and tension between Sarah and Hagar led to Ishmael's expulsion with his mother into the wilderness of Beersheba (Genesis 21:9–21). God appeared to Hagar there and renewed his promise that Ishmael would become a great nation — a promise fulfilled in the twelve princes who descended from him (Genesis 25:12–18), generally associated with the nomadic peoples of northern Arabia. In Galatians 4:21–31 Paul reads Ishmael as an allegory of the Mosaic covenant and fleshly religion (born \"according to the flesh\") in contrast to Isaac as the child of the promise and type of spiritual freedom. Ishmael appears at Abraham's burial alongside Isaac (Genesis 25:9), suggesting a final reconciliation between the two lines.</p>",
        "hitchcock_meaning": "God that hears",
        "source_ids": {"easton": "ishmael", "smith": "ishmael", "isbe": "ishmael"},
        "key_refs": ["Genesis 16:15", "Genesis 21:14", "Genesis 25:9", "Galatians 4:23"]
    },
    "ishmaiah": {
        "id": "ishmaiah",
        "term": "Ishmaiah",
        "category": "people",
        "intro": "<p>Ishmaiah (meaning <em>heard by Jehovah</em> or <em>obeying the Lord</em>) is the name of two men in the period of David's reign. (1.) A Gibeonite warrior who joined David at Ziklag during his time as a fugitive from Saul, listed in 1 Chronicles 12:4 as one of the mighty men of the thirty and described as a warrior capable of wielding both shield and spear against Saul's forces. Gibeonite warriors joining David's cause is notable given the complex history between Saul and the Gibeonites recorded in 2 Samuel 21. (2.) Ishmaiah son of Obadiah, appointed as the officer over the tribe of Zebulun in David's administrative organization of military districts (1 Chronicles 27:19).</p><p>Both figures represent the administrative and military network David built from men who were loyal to him before his kingship was formally established — a network that formed the backbone of his rule over all Israel.</p>",
        "hitchcock_meaning": "hearing or obeying the Lord",
        "source_ids": {"easton": "ishmaiah", "smith": "ishmaiah", "isbe": "ishmaiah"},
        "key_refs": ["1 Chronicles 12:4", "1 Chronicles 27:19"]
    },
    "ishmeelites": {
        "id": "ishmeelites",
        "term": "Ishmeelites",
        "category": "concepts",
        "intro": "<p>Ishmeelites is the Authorized Version spelling of Ishmaelites — the descendants of Ishmael, Abraham's son by Hagar. In Genesis 37:25–28 and 39:1 the caravan of traders who purchased Joseph from his brothers and brought him down to Egypt are called both Ishmeelites and Midianites in close proximity (Genesis 37:28, 36), a textual phenomenon that has generated considerable discussion: most interpreters understand the terms as overlapping designations for the nomadic trading peoples of the region, or take the Midianites as a separate group who purchased Joseph from the Ishmaelites.</p><p>The Ishmaelites appear again in Judges 8:24 in the narrative of Gideon's victory over Midian, where the Midianite warriors are said to have worn gold earrings \"because they were Ishmaelites\" — suggesting the terms were used interchangeably for related nomadic groups in the biblical period. Psalm 83:6 lists the Ishmaelites among the coalition of nations plotting against Israel. The trading role of the Ishmaelites in the Joseph narrative — carrying spices, balm, and myrrh to Egypt — reflects the well-attested caravan trade between Arabia and Egypt that passed through Canaan throughout the second millennium BC.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ishmeelites", "isbe": "ishmeelites"},
        "key_refs": ["Genesis 37:28", "Genesis 39:1", "Judges 8:24"]
    },
    "ishtob": {
        "id": "ishtob",
        "term": "Ishtob",
        "category": "places",
        "intro": "<p>Ishtob (meaning <em>man of Tob</em>) was one of the small Aramaean (Syrian) kingdoms or city-states east of the Jordan that the Ammonites hired to fight against David when they realized they had become odious to him following their mistreatment of David's ambassadors (2 Samuel 10:6, 8). The men of Ishtob contributed twelve thousand soldiers to the coalition force. The region of Tob is mentioned earlier in Judges 11:3, 5, where Jephthah fled to the land of Tob after being driven out by his brothers and gathered worthless men around him there.</p><p>Ishtob's territory is generally located in the Transjordan northeast of the Sea of Galilee, in the region between Bashan and the Aramaean kingdoms further north. The coalition of Ammon, Beth-rehob, Zoba, Maacah, and Ishtob against David was decisively defeated by Joab and Abishai in the ensuing battle, after which the Aramaean kings submitted to David and became his vassals.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ishtob", "smith": "ishtob"},
        "key_refs": ["2 Samuel 10:6", "2 Samuel 10:8", "Judges 11:3"]
    },
    "island": {
        "id": "island",
        "term": "Island",
        "category": "concepts",
        "intro": "<p>Island in the biblical text translates primarily the Hebrew <em>'i</em> (plural <em>'iyyim</em>), a word whose range of meaning is broader than its English equivalent. It can denote coastal lands, distant shores, and inhabited regions across the sea — essentially any territory reached by water. The ancient Israelite conception of geography placed the land of Canaan at the center; distant coastlands and Mediterranean islands (Cyprus, Crete, Greece, and beyond) were <em>'iyyim</em> — lands at the far edges of the known world.</p><p>Isaiah uses the term extensively in his universal vision: the coastlands and islands are called to listen (Isaiah 42:4, 10; 49:1), they will wait for God's law, and they will be renewed in the coming restoration. This geographic expansion of the prophetic address to distant shores reflects the scope of Isaiah's vision of God's rule over all nations. In the New Testament context, islands appear as locations of significant events: Paul was shipwrecked on Malta (Acts 28:1–10); Patmos was the island of John's exile where he received the Revelation (Revelation 1:9); and Cyprus, Crete, and other Mediterranean islands were visited during the missionary journeys, confirming the fulfillment of the gospel reaching the distant coastlands.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "island"},
        "key_refs": ["Isaiah 42:4", "Isaiah 49:1", "Acts 28:1", "Revelation 1:9"]
    },
    "israel": {
        "id": "israel",
        "term": "Israel",
        "category": "people",
        "intro": "<p>Israel is the name given to Jacob after his night of wrestling with God at the ford of Jabbok (Genesis 32:28): \"Your name shall no longer be called Jacob, but Israel, for you have striven with God and with men, and have prevailed.\" The name is interpreted in the text as <em>he who strives with God</em> or <em>God strives</em> (Hebrew <em>yisra'el</em>, combining the root <em>sarah</em>, to strive or rule, with <em>'El</em>, God). It was reaffirmed at Bethel (Genesis 35:10). From this personal name the descendants of Jacob's twelve sons became the twelve tribes of Israel, and the name extended to denote the nation they formed — first united under the monarchy, then divided after Solomon's death into the northern kingdom of Israel and the southern kingdom of Judah.</p><p>In the prophets, \"Israel\" oscillates between the ten-tribe northern kingdom (which ceased to exist after the Assyrian conquest of 722 BC), the covenantal people as a whole, and the restored remnant of future promise. The New Testament applies the name to the church in Galatians 6:16 (\"the Israel of God\") and to the faithful remnant within ethnic Israel (Romans 9:6: \"For not all who are descended from Israel belong to Israel\"), while also affirming the continuing significance of ethnic Israel in Romans 9–11. The name thus carries both historical particularity and eschatological breadth throughout Scripture.</p>",
        "hitchcock_meaning": "who prevails with God",
        "source_ids": {"easton": "israel", "smith": "israel", "isbe": "israel"},
        "key_refs": ["Genesis 32:28", "Genesis 35:10", "Romans 9:6", "Galatians 6:16"]
    },
    "israel-kingdom-of": {
        "id": "israel-kingdom-of",
        "term": "Israel, Kingdom of",
        "category": "places",
        "intro": "<p>The Kingdom of Israel (also called the Northern Kingdom or Ephraim) was the state formed when ten of the twelve tribes seceded from the united monarchy following Solomon's death around 930 BC. The immediate trigger was Rehoboam's refusal to lighten the burden of taxation and forced labor that had characterized Solomon's reign (1 Kings 12:1–20). Jeroboam son of Nebat, who had returned from exile in Egypt, became the first king of the northern kingdom. To prevent his subjects from traveling to Jerusalem for worship and potentially reconverting to Davidic allegiance, Jeroboam established golden calves at Bethel and Dan (1 Kings 12:28–30) — an act the books of Kings treat as the paradigmatic sin that brought the kingdom to ruin.</p><p>The northern kingdom lasted approximately two centuries (930–722 BC), encompassing nineteen kings across nine dynasties, none of whom are given a positive theological verdict in Kings. The kingdom fell to the Assyrian empire under Sargon II in 722 BC (2 Kings 17:1–6); its population was deported and replaced with foreign settlers who mixed with remaining Israelites to produce the Samaritans. The prophets Elijah, Elisha, Amos, and Hosea ministered primarily in the northern kingdom. The theological explanation for the fall is given in 2 Kings 17:7–23: persistent covenantal unfaithfulness and idolatry.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "israel-kingdom-of", "smith": "israel-kingdom-of", "isbe": "israel-kingdom-of"},
        "key_refs": ["1 Kings 12:20", "1 Kings 12:28", "2 Kings 17:6", "2 Kings 17:22"]
    },
    "issachar": {
        "id": "issachar",
        "term": "Issachar",
        "category": "people",
        "intro": "<p>Issachar (meaning <em>reward</em> or <em>hired</em>) was the ninth son of Jacob and fifth son of Leah (Genesis 30:17–18). His name commemorates Leah's interpretation of his conception as God's reward (<em>sakar</em>) for her giving her maidservant Zilpah to Jacob — or alternatively, as the wages of her \"hiring\" Jacob from Rachel with the mandrakes (Genesis 30:14–16). His birth completes the first group of Leah's sons before her daughters Dinah and the sons of the concubines are enumerated. Jacob's blessing in Genesis 49:14–15 describes Issachar as \"a strong donkey, crouching between the sheepfolds,\" seeing that rest was good and bowing his shoulder to bear burdens — an oracle interpreted as describing the tribe's character of agricultural industriousness and possible tribute-paying to neighboring powers.</p><p>The tribe of Issachar settled in the fertile valley of Jezreel, one of the most productive agricultural regions of Canaan. At the first census the tribe numbered 54,400 men (Numbers 2:5–6), and it contributed men of understanding of the times to David's cause (1 Chronicles 12:32). The territory of Issachar is described in Joshua 19:17–23. The tribe's position in the Jezreel Valley made it both prosperous and vulnerable to military pressure from the north and east throughout the period of the judges and the monarchy.</p>",
        "hitchcock_meaning": "reward; recompense",
        "source_ids": {"easton": "issachar", "smith": "issachar", "isbe": "issachar"},
        "key_refs": ["Genesis 30:18", "Genesis 49:14", "Numbers 2:5", "1 Chronicles 12:32"]
    },
    "italian-band": {
        "id": "italian-band",
        "term": "Italian Band",
        "category": "concepts",
        "intro": "<p>The Italian Band (also called the Italian cohort) was the Roman military unit in which Cornelius, the centurion of Caesarea, served when he received the vision that led to the first Gentile baptism (Acts 10:1). A Roman cohort was a unit of approximately 480–600 soldiers, one-tenth of a legion. The designation \"Italian\" indicates the cohort was composed of volunteers from Italy rather than provincial auxiliaries — a mark of status that cohered with Cornelius's evident standing as a man of influence and religious devotion.</p><p>The historicity of an Italian cohort stationed in Caesarea has been confirmed by inscriptional evidence: a cohort known as the <em>Cohors II Italica Civium Romanorum</em> is attested in Syria during the first century. Acts 10 identifies Cornelius as a God-fearer — a Gentile attached to the Jewish synagogue who observed Jewish ethical monotheism without full conversion. His encounter with Peter, triggered by the parallel visions of Cornelius and Peter (Acts 10:3–16), marks the decisive moment in the early church's recognition that the gospel and the gift of the Holy Spirit were for Gentiles without prior circumcision (Acts 10:44–48; 11:18).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "italian-band", "smith": "italian-band", "isbe": "italian-band"},
        "key_refs": ["Acts 10:1"]
    },
    "italy": {
        "id": "italy",
        "term": "Italy",
        "category": "places",
        "intro": "<p>Italy in the New Testament refers to the Roman peninsula that formed the geographic and political heart of the Roman Empire. The name occurs four times in the New Testament. Acts 18:2 mentions that Aquila and Priscilla had recently come from Italy when expelled by the Claudian edict against Jews in Rome (around AD 49). Acts 27:1 and 6 describe Paul's voyage to Italy as a prisoner, ultimately bound for Rome to appear before Caesar. Hebrews 13:24 includes the greeting \"they of Italy salute you\" — a phrase that may indicate the letter was either written from Italy or addressed to an Italian congregation.</p><p>Italy's significance in the biblical narrative is primarily as the location of Rome, the seat of imperial power. Paul's letter to the Romans, written before his arrival, anticipated a visit en route to Spain (Romans 15:24, 28). His actual arrival in Rome (Acts 28:14–16) fulfills the divine word that Paul would testify there (Acts 23:11). The spread of the gospel to Rome — \"to the ends of the earth\" in one sense of Acts 1:8 — represents the completion of the geographic arc of Acts from Jerusalem outward to the imperial capital.</p>",
        "hitchcock_meaning": "abounding with calves or heifers",
        "source_ids": {"easton": "italy", "smith": "italy", "isbe": "italy"},
        "key_refs": ["Acts 18:2", "Acts 27:1", "Hebrews 13:24", "Romans 15:24"]
    },
    "ithamar": {
        "id": "ithamar",
        "term": "Ithamar",
        "category": "people",
        "intro": "<p>Ithamar (meaning <em>island of the palm-tree</em> or <em>land of palms</em>) was the fourth and youngest son of Aaron, born before the consecration of the tabernacle (Exodus 6:23). He and his brothers Nadab, Abihu, and Eleazar were consecrated as priests with Aaron at the establishment of the Levitical priesthood (Leviticus 8–9). When Nadab and Abihu died for offering unauthorized fire before the LORD (Leviticus 10:1–2), Eleazar and Ithamar continued as priests under their father Aaron.</p><p>Ithamar was assigned specific administrative responsibilities for the tabernacle: he oversaw the work of the Gershonite and Merarite Levites in transporting the tabernacle's structural components (Numbers 4:28, 33). After the settlement in Canaan, the priestly house of Ithamar continued alongside the house of Eleazar; Eli the high priest at Shiloh (1 Samuel 1–4) belonged to Ithamar's line, and the high priesthood passed to this family during the period of the judges and early monarchy. David organized the priestly courses (1 Chronicles 24:1–6), at which time eight of the twenty-four courses were assigned to descendants of Ithamar and sixteen to descendants of Eleazar.</p>",
        "hitchcock_meaning": "island of the palm-tree",
        "source_ids": {"easton": "ithamar", "smith": "ithamar", "isbe": "ithamar"},
        "key_refs": ["Exodus 6:23", "Leviticus 10:6", "Numbers 4:28", "1 Chronicles 24:4"]
    },
    "ithrite": {
        "id": "ithrite",
        "term": "Ithrite",
        "category": "people",
        "intro": "<p>Ithrite is a designation applied to two of David's thirty mighty warriors: Ira and Gareb, listed in 2 Samuel 23:38 and 1 Chronicles 11:40. The term likely indicates membership in a clan or family group — the Ithrites — mentioned in 1 Chronicles 2:53 among the families of Kiriath-jearim: the Ithrites, Puthites, Shumathites, and Mishraites. Kiriath-jearim, the city where the ark of the LORD rested for twenty years before David brought it to Jerusalem (1 Samuel 7:1–2), was a significant location, and men from this vicinity evidently joined David's military establishment.</p><p>Beyond the clan name and the two warriors it identifies, the Ithrites receive no further narrative in Scripture. Their inclusion among David's elite thirty reinforces the picture of David drawing loyal warriors from diverse clans and towns throughout Israel during both his outlaw years and his reign.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ithrite", "smith": "ithrite", "isbe": "ithrite"},
        "key_refs": ["2 Samuel 23:38", "1 Chronicles 11:40", "1 Chronicles 2:53"]
    },
    "ittai": {
        "id": "ittai",
        "term": "Ittai",
        "category": "people",
        "intro": "<p>Ittai (meaning <em>with the LORD</em> or <em>near</em>) is the name of two men in David's time. (1.) Ittai the Gittite, a Philistine from Gath who led six hundred men in loyal service to David during Absalom's rebellion (2 Samuel 15:18–22). When David urged him to return, saying he had arrived only the day before and had no reason to share in the king's uncertain fortunes, Ittai responded with words of extraordinary loyalty reminiscent of Ruth's pledge to Naomi: \"As the LORD lives, and as my lord the king lives, wherever my lord the king shall be, whether in death or life, even there also will thy servant be\" (2 Samuel 15:21). He was appointed as one of three commanders over David's army alongside Joab and Abishai in the battle against Absalom (2 Samuel 18:2).</p><p>(2.) Ittai son of Ribai from Gibeah of Benjamin, one of David's thirty mighty warriors (2 Samuel 23:29; 1 Chronicles 11:31). The Gittite Ittai stands as one of the most compelling examples in Scripture of a foreign-born convert whose loyalty to Israel's king surpassed that of native Israelites during the crisis of Absalom's coup.</p>",
        "hitchcock_meaning": "near; timely; or, with the Lord",
        "source_ids": {"easton": "ittai", "smith": "ittai", "isbe": "ittai"},
        "key_refs": ["2 Samuel 15:19", "2 Samuel 15:21", "2 Samuel 18:2", "2 Samuel 23:29"]
    },
    "ituraea": {
        "id": "ituraea",
        "term": "Ituraea",
        "category": "places",
        "intro": "<p>Ituraea was a district northeast of Palestine in the region of Mount Lebanon and Anti-Lebanon, associated with the Iturean people — possibly descendants of Jetur, a son of Ishmael (Genesis 25:15; 1 Chronicles 1:31). By the Hellenistic and early Roman periods, the Itureans were known as skilled archers and mountain warriors. Luke 3:1 identifies Ituraea as part of the tetrarchy of Philip son of Herod the Great: \"Philip being tetrarch of Ituraea and of the region of Trachonitis.\" Philip's combined territory covered the largely Gentile regions northeast of the Sea of Galilee and east of the Jordan headwaters.</p><p>The exact boundaries of Ituraea in the first century are uncertain; it is generally located in the Bekaa Valley and the slopes of Mount Lebanon. The region's inclusion in Philip's tetrarchy placed it under Roman-supervised Herodian administration from 4 BC until Philip's death in AD 34, after which it was incorporated into the Roman province of Syria. Ituraea's sole New Testament mention serves to date the beginning of John the Baptist's ministry and thus the inauguration of the gospel narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ituraea", "smith": "ituraea", "isbe": "ituraea"},
        "key_refs": ["Luke 3:1", "Genesis 25:15"]
    },
    "ivah": {
        "id": "ivah",
        "term": "Ivah",
        "category": "places",
        "intro": "<p>Ivah (also spelled Avva or Ava, meaning <em>overturning</em>) was a city of the Assyrian empire from which colonists were deported to repopulate Samaria after the Assyrian conquest of the northern kingdom of Israel in 722 BC (2 Kings 17:24). These settlers brought their own gods with them, and 2 Kings 17:31 records that the Avvites made Nibhaz and Tartak, names otherwise unknown in ancient Near Eastern records.</p><p>Ivah appears again in the Rabshakeh's taunt speech before Jerusalem (2 Kings 18:34; 19:13; Isaiah 36:19; 37:13): the Assyrian envoy asks where are the gods of Hamath, Arpad, Sepharvaim, Hena, and Ivah — cities whose gods had failed to protect them from Assyrian conquest — as proof that the LORD could not protect Jerusalem either. The rhetorical strategy equates the God of Israel with the defeated gods of these nations. Hezekiah's prayer in response (2 Kings 19:14–19) acknowledges that the Assyrians had indeed destroyed those nations and their gods, but affirms that the LORD is the living God whose alone is different in kind from idols of wood and stone. The divine answer through Isaiah vindicates this distinction.</p>",
        "hitchcock_meaning": "iniquity",
        "source_ids": {"easton": "ivah", "smith": "ivah", "isbe": "ivah"},
        "key_refs": ["2 Kings 17:24", "2 Kings 18:34", "Isaiah 36:19"]
    },
    "ivory": {
        "id": "ivory",
        "term": "Ivory",
        "category": "concepts",
        "intro": "<p>Ivory (Hebrew <em>shen</em>, tooth, and <em>shenhabbim</em>, teeth of elephants) was one of the most prized luxury materials in the ancient Near East, imported to Israel and Judah via long-distance trade. Solomon's trading fleet brought ivory along with gold, silver, apes, and peacocks from Ophir (1 Kings 10:22), and his famous throne was made of ivory overlaid with gold (1 Kings 10:18; 2 Chronicles 9:17). The house Ahab built in Samaria was called the \"ivory house\" (1 Kings 22:39), and the excavation of Samaria by archaeologists in the twentieth century recovered hundreds of ivory carvings confirming the biblical account of ivory luxury in the northern palace.</p><p>The prophets condemned ivory as emblematic of oppressive wealth: Amos 6:4 denounces those who \"lie upon beds of ivory and stretch themselves upon their couches\" while careless of the ruin of Joseph. The Psalms use ivory as imagery for beauty (Psalm 45:8). In Revelation 18:12, ivory is listed among the luxury goods of Babylon whose trade is destroyed by divine judgment — a catalog that situates ivory alongside fine linen, gold, and silk as markers of imperial excess. Ivory came primarily from African and Indian elephants; the extinction of Syrian elephants (a subspecies mentioned in ancient Near Eastern records) may partly explain the increasing rarity and value of ivory in the later biblical period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ivory", "smith": "ivory", "isbe": "ivory"},
        "key_refs": ["1 Kings 10:18", "1 Kings 22:39", "Amos 6:4", "Revelation 18:12"]
    },
    "izhar": {
        "id": "izhar",
        "term": "Izhar",
        "category": "people",
        "intro": "<p>Izhar (meaning <em>oil</em> or <em>anointed</em>, perhaps reflecting the shining quality of oil) was one of the four sons of Kohath and grandson of Levi (Exodus 6:18, 21; Numbers 3:19). His brothers were Amram, Hebron, and Uzziel. Amram's line produced Moses and Aaron; Izhar's line produced Korah. The Izharite family was assigned specific duties in the transport and care of the tabernacle (Numbers 4:1–20), carrying the holy furnishings covered in their prescribed wrappings.</p><p>Izhar's prominence in the genealogical record is partly defined by his most significant descendant: Korah son of Izhar, who led the rebellion against Moses and Aaron in the wilderness (Numbers 16:1). The Izharite connection to the Korahite rebellion marks the family line with both honor (Levitical service) and notoriety (covenantal mutiny). Despite this, the sons of Korah survived the judgment (Numbers 26:11) and became a distinguished guild of temple musicians and gatekeepers under David and Solomon — the Korahite psalms (Psalms 42, 44–49, 84–85, 87–88) bearing their name.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "izhar", "smith": "izhar", "isbe": "izhar"},
        "key_refs": ["Exodus 6:18", "Exodus 6:21", "Numbers 16:1", "Numbers 26:11"]
    },
    "izrahite": {
        "id": "izrahite",
        "term": "Izrahite",
        "category": "people",
        "intro": "<p>Izrahite is the designation of Shamhuth, the officer in charge of David's fifth monthly division of the military organization described in 1 Chronicles 27:8. Each of the twelve divisions served one month per year under its appointed commander, with the king maintaining a rotating force of twenty-four thousand men at readiness throughout the year. Shamhuth the Izrahite commanded this rotation during the fifth month.</p><p>The clan name Izrahite is not fully explained in the text. It may be related to Zerah, one of the sons of Judah (Genesis 38:30; Numbers 26:20), with Izrahite meaning \"belonging to the Zerahite family\" — a variation of the Zerahite designation found elsewhere in the Davidic military lists (1 Chronicles 27:11, 13). If so, Shamhuth belonged to the Judahite clan descended from Zerah, a family that also produced notable military figures in David's service. The Izrahite designation survives only in this single verse.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "izrahite", "smith": "izrahite", "isbe": "izrahite"},
        "key_refs": ["1 Chronicles 27:8"]
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
