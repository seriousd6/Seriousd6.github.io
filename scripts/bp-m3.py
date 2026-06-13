#!/usr/bin/env python3
"""BP M3: Mercurius → Misham (75 Easton entries)"""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(fp):
        with open(fp) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    with open(fp, 'w') as f:
        json.dump(data, f, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "mercurius": {
        "id": "mercurius",
        "term": "Mercurius",
        "category": "concepts",
        "intro": "<p>Mercurius (the Latin form of Hermes, the Greek messenger deity) appears in the New Testament in the account of Paul and Barnabas's mission to Lystra. When Paul healed a man lame from birth, the Lycaonian crowd concluded that the gods had come down in human form, calling Barnabas Zeus and Paul Mercurius, <em>because he was the chief speaker</em> (Acts 14:12). The identification reflects the ancient conception of Hermes as the eloquent herald and messenger of the gods — a role the crowd saw mirrored in Paul's preaching.</p><p>The episode illustrates both the deep-seated polytheism of Asia Minor in the first century and the challenge it posed to the proclamation of monotheistic Christianity. Paul and Barnabas tore their clothes in horror and struggled to prevent the crowds from offering sacrifices to them, insisting they were mere mortals bringing news of the living God. The incident at Lystra demonstrates how the gospel's miraculous deeds were liable to be absorbed into existing religious frameworks unless its preachers actively reframed them.</p>",
        "sections": [],
        "hitchcock_meaning": "an orator; an interpreter",
        "source_ids": {"easton": "mercurius"},
        "key_refs": ["Acts 14:12"]
    },
    "mercy": {
        "id": "mercy",
        "term": "Mercy",
        "category": "concepts",
        "intro": "<p>Mercy, in biblical theology, denotes the disposition of God to withhold deserved punishment and to show compassion toward the guilty or suffering. The Hebrew word most commonly translated <em>mercy</em> is <em>hesed</em> — a covenant term encompassing steadfast love, loyalty, and kindness — while <em>rahamim</em> (compassion, from the word for <em>womb</em>) conveys tender parental feeling. Together they capture the two dimensions of divine mercy: covenantal faithfulness to those in relationship with God and spontaneous compassion toward the weak and broken.</p><p>The Old Testament celebrates mercy as one of God's defining attributes: <em>the LORD, the LORD God, merciful and gracious</em> (Exodus 34:6). The Psalms repeatedly ground prayer for deliverance in God's mercy rather than human merit. In the New Testament, mercy is enacted supremely in the person of Jesus, who showed <em>hesed</em> toward the sick, sinners, and outcasts, and whose atoning death is described as God's <em>mercy seat</em> (Romans 3:25). Christian ethics grounds the obligation to show mercy to others in the mercy already received: <em>blessed are the merciful, for they shall obtain mercy</em> (Matthew 5:7).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mercy", "isbe": "mercy"},
        "key_refs": ["Exodus 34:6", "Psalms 85:10", "Matthew 5:7", "Romans 3:25"]
    },
    "mercy-seat": {
        "id": "mercy-seat",
        "term": "Mercy-seat",
        "category": "concepts",
        "intro": "<p>The mercy-seat (<em>kapporeth</em> in Hebrew, from the root <em>kaphar</em>, to cover or atone) was the solid gold lid of the Ark of the Covenant, measuring two and a half cubits long and one and a half cubits wide (Exodus 25:17). At each end stood a golden cherub with wings outstretched to cover it, and the space between the cherubim was considered the earthly throne of God — the place where the invisible divine presence was localized and where the LORD declared he would meet with Moses and give his commands (Exodus 25:22).</p><p>The mercy-seat received its most significant role on the Day of Atonement (Yom Kippur), when the high priest entered the Holy of Holies and sprinkled sacrificial blood on it seven times to make atonement for the sins of the entire nation (Leviticus 16:14–15). The Greek New Testament renders <em>kapporeth</em> as <em>hilasterion</em> — the same word Paul uses in Romans 3:25 to describe Christ as the one whom God set forth as a <em>propitiation</em> (mercy-seat) through faith in his blood. The writer of Hebrews also identifies Christ as the High Priest who entered the true heavenly sanctuary with his own blood (Hebrews 9:5, 11–12), fulfilling and superseding the Mosaic institution.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mercy-seat"},
        "key_refs": ["Exodus 25:17", "Leviticus 16:14", "Hebrews 9:5", "Romans 3:25"]
    },
    "mered": {
        "id": "mered",
        "term": "Mered",
        "category": "people",
        "intro": "<p>Mered (meaning <em>rebellious</em> or <em>ruling</em>) was a descendant of Judah mentioned only in the genealogical lists of 1 Chronicles 4:17. He is noted there as the husband of two women: Bithiah, a daughter of Pharaoh who had married into Israel, and an unnamed Jewish wife, by whom he had three sons. The brief notice is remarkable chiefly for the mention of an Egyptian princess among Mered's wives, suggesting intermarriage between Israelite tribal families and Egyptian nobility — a striking detail preserved in the Judahite genealogies.</p>",
        "sections": [],
        "hitchcock_meaning": "rebellious, ruling",
        "source_ids": {"easton": "mered"},
        "key_refs": ["1 Chronicles 4:17"]
    },
    "meremoth": {
        "id": "meremoth",
        "term": "Meremoth",
        "category": "people",
        "intro": "<p>Meremoth (meaning <em>bitterness</em> or <em>myrrh of death</em>) was the name of at least two figures in post-exilic Judah. The most prominent was Meremoth son of Uriah the priest, who played a prominent administrative role in the restoration community: he received and weighed the silver and gold vessels that Ezra brought back from Babylon (Ezra 8:33) and repaired two sections of the Jerusalem wall during Nehemiah's rebuilding effort (Nehemiah 3:4, 21). A second Meremoth was among the priests who returned with Zerubbabel (Nehemiah 12:3). The repetition of the name suggests it was a family name in priestly circles.</p>",
        "sections": [],
        "hitchcock_meaning": "bitterness; myrrh of death",
        "source_ids": {"easton": "meremoth"},
        "key_refs": ["Ezra 8:33", "Nehemiah 3:4", "Nehemiah 12:3"]
    },
    "merib-baal": {
        "id": "merib-baal",
        "term": "Merib-baal",
        "category": "people",
        "intro": "<p>Merib-baal was the son of Jonathan and grandson of King Saul, better known by the alternative name Mephibosheth. The name Merib-baal — possibly meaning <em>Baal contends</em> or <em>the lord pleads</em> — appears in the genealogical lists of 1 Chronicles 8:34 and 9:40, while in the narrative sections of 2 Samuel he is called Mephibosheth, a name apparently substituting <em>bosheth</em> (shame) for the Baal element, following a scribal convention that replaced Baal-compound names to avoid honoring the Canaanite deity. He was lame in both feet from a childhood fall during the panic following his father's and grandfather's deaths at Jezreel (2 Samuel 4:4).</p><p>His life was transformed when King David, honoring his covenant with Jonathan, brought him to Jerusalem and restored all of Saul's land to him, seating him at the royal table <em>as one of the king's sons</em> (2 Samuel 9:11). He is a striking figure of grace — a crippled member of the defeated royal house restored by covenantal loyalty.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "merib-baal"},
        "key_refs": ["2 Samuel 4:4", "2 Samuel 9:6", "1 Chronicles 8:34"]
    },
    "meribah": {
        "id": "meribah",
        "term": "Meribah",
        "category": "places",
        "intro": "<p>Meribah (meaning <em>strife</em> or <em>quarrel</em>) was the name given to two sites in the Sinai wilderness where Israel contended with Moses over the lack of water. The first Meribah was at Rephidim, early in the wilderness journey, where Moses struck the rock at Horeb and water gushed out (Exodus 17:7) — the site is also called Massah (<em>testing</em>). The second Meribah, also called Meribah-kadesh or <em>the waters of Meribah</em>, occurred in the wilderness of Zin near Kadesh, where Moses struck the rock twice instead of speaking to it as God commanded (Numbers 20:10–13).</p><p>The incident at Meribah-kadesh was theologically decisive for Moses: because he did not honor God as holy before the assembly, he was barred from entering Canaan. Psalm 81:7 and Psalm 95:8 use Meribah as a paradigm of faithlessness and the hardening of hearts, urging Israel to hear God's voice rather than repeat the provocation in the wilderness.</p>",
        "sections": [],
        "hitchcock_meaning": "dispute; quarrel",
        "source_ids": {"easton": "meribah", "smith": "meribah"},
        "key_refs": ["Exodus 17:7", "Numbers 20:13", "Psalms 81:7", "Deuteronomy 33:8"]
    },
    "merodach": {
        "id": "merodach",
        "term": "Merodach",
        "category": "concepts",
        "intro": "<p>Merodach (Hebrew form of the Babylonian <em>Marduk</em>) was the supreme deity of the Babylonian pantheon. His name appears in the Old Testament primarily in prophetic condemnation: Jeremiah 50:2 announces that <em>Merodach is dismayed</em> as part of the declaration of Babylon's coming fall. Marduk rose to supremacy during the Old Babylonian period and was celebrated in the creation epic <em>Enuma Elish</em> as the god who slew the chaos dragon Tiamat and fashioned the world from her body.</p><p>The name Merodach is embedded in several Babylonian royal names familiar from the Bible: Merodach-baladan (Isaiah 39:1), Evil-merodach (2 Kings 25:27), and Bel-shazzar. Jeremiah's taunt against Merodach represents a characteristic prophetic polemic against the gods of the nations — entities whom the prophets regarded as powerless before the sovereign God of Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "bitter contrition",
        "source_ids": {"easton": "merodach", "smith": "merodach", "isbe": "merodach"},
        "key_refs": ["Jeremiah 50:2", "Isaiah 46:1"]
    },
    "merodach-baladan": {
        "id": "merodach-baladan",
        "term": "Merodach-baladan",
        "category": "people",
        "intro": "<p>Merodach-baladan (Babylonian: <em>Marduk-apla-iddina</em>, meaning <em>Marduk has given a son</em>) was a Chaldean chieftain who twice seized the throne of Babylon — first around 721–710 BC and again briefly in 703 BC. He is notable in biblical history as the king who sent envoys with letters and a present to King Hezekiah of Judah upon hearing that Hezekiah had been ill (Isaiah 39:1; 2 Kings 20:12). The mission was almost certainly diplomatic as well, designed to cultivate an anti-Assyrian alliance.</p><p>Hezekiah's fateful decision to show the envoys all his treasuries prompted a stark oracle from Isaiah: everything shown to the Babylonians would one day be carried off to Babylon, and Hezekiah's own sons would serve as eunuchs in the Babylonian court — a prophecy fulfilled more than a century later under Nebuchadnezzar.</p>",
        "sections": [],
        "hitchcock_meaning": "bitter contrition, without judgment",
        "source_ids": {"easton": "merodach-baladan", "isbe": "merodach-baladan"},
        "key_refs": ["Isaiah 39:1", "2 Kings 20:12", "2 Chronicles 32:31"]
    },
    "merom": {
        "id": "merom",
        "term": "Merom",
        "category": "places",
        "intro": "<p>Merom (meaning <em>eminences</em> or <em>high places</em>) was the body of water and surrounding region in northern Galilee where Joshua achieved a decisive victory over a Canaanite coalition led by Jabin king of Hazor. Joshua 11:5 describes a confederation of northern Canaanite kings assembling <em>at the waters of Merom</em> to fight Israel. Joshua attacked suddenly and routed them, pursuing the survivors as far as Zidon and Misrephoth-maim. The victory broke the last organized Canaanite resistance in the north.</p><p>The waters of Merom are generally identified with Lake Huleh (the ancient Semechonitis), a marshy lake in the upper Jordan valley north of the Sea of Galilee, though some scholars dispute the exact location. The battle at Merom completed the military subjugation of Canaan begun at Jericho and Ai.</p>",
        "sections": [],
        "hitchcock_meaning": "eminences; elevations",
        "source_ids": {"easton": "merom", "smith": "merom"},
        "key_refs": ["Joshua 11:5", "Joshua 11:7"]
    },
    "meronothite": {
        "id": "meronothite",
        "term": "Meronothite",
        "category": "people",
        "intro": "<p>Meronothite is a gentillic designation appearing twice in the Old Testament, referring to inhabitants of an otherwise unidentified place called Meronoth. Jehdeiah the Meronothite served as the royal official in charge of David's donkeys (1 Chronicles 27:30), and Jadon the Meronothite is listed among those who repaired the Jerusalem wall during Nehemiah's rebuilding (Nehemiah 3:7). The location of Meronoth is uncertain; it may have been in Galilee or in the vicinity of Gibeon.</p>",
        "sections": [],
        "hitchcock_meaning": "my singing; rejoicing; bearing rule",
        "source_ids": {"easton": "meronothite"},
        "key_refs": ["1 Chronicles 27:30", "Nehemiah 3:7"]
    },
    "meroz": {
        "id": "meroz",
        "term": "Meroz",
        "category": "places",
        "intro": "<p>Meroz was an Israelite settlement cursed in the Song of Deborah (Judges 5:23) for failing to come to the aid of Israel in the battle against Sisera. The angel of the LORD pronounced a bitter curse on its inhabitants: <em>Curse Meroz, said the angel of the LORD, curse its inhabitants thoroughly, because they did not come to the help of the LORD, to the help of the LORD against the mighty.</em> The location of Meroz is unknown; various sites in the Jezreel valley and upper Galilee have been proposed. Its infamy rests entirely on this single verse, making it a biblical byword for culpable neutrality when covenant solidarity required action.</p>",
        "sections": [],
        "hitchcock_meaning": "secret, leanness",
        "source_ids": {"easton": "meroz"},
        "key_refs": ["Judges 5:23"]
    },
    "mesha": {
        "id": "mesha",
        "term": "Mesha",
        "category": "people",
        "intro": "<p>Mesha was the name of several biblical figures, the most significant being Mesha king of Moab, who rebelled against Israel after the death of Ahab. According to 2 Kings 3:4–5, Mesha had been a sheep breeder who paid a massive annual tribute to Israel: one hundred thousand lambs and the wool of one hundred thousand rams. After Ahab died, Mesha refused to pay the tribute, prompting a joint military campaign by Jehoram of Israel, Jehoshaphat of Judah, and the king of Edom.</p><p>Mesha is independently attested in the famous Mesha Stele (the Moabite Stone, discovered in 1868), on which he records his victories over Israel in his own words — one of the most important extra-biblical inscriptions relating to Old Testament history. The stele mentions Israel, the house of Omri, the town of Nebo, and the divine name Chemosh, providing remarkable confirmation of the biblical account. Other figures named Mesha include a descendant of Caleb (1 Chronicles 2:42) and a territorial boundary of the Joktanites (Genesis 10:30).</p>",
        "sections": [],
        "hitchcock_meaning": "burden; salvation",
        "source_ids": {"easton": "mesha", "smith": "mesha", "isbe": "mesha"},
        "key_refs": ["2 Kings 3:4", "Genesis 10:30", "1 Chronicles 2:42"]
    },
    "meshach": {
        "id": "meshach",
        "term": "Meshach",
        "category": "people",
        "intro": "<p>Meshach was the Babylonian name given to Mishael, one of the three Jewish companions of Daniel who were taken to Babylon during Nebuchadnezzar's deportation of Jerusalem's nobility. His Hebrew name Mishael means <em>who is asked for or lent</em>; his Babylonian name Meshach is generally taken to mean <em>who is drawn by force</em> — a renaming designed to sever the young men's identities from their Hebrew religious roots (Daniel 1:7).</p><p>Meshach, along with Shadrach and Abednego, became the central figures of one of Scripture's most celebrated acts of civil disobedience. When commanded to worship Nebuchadnezzar's golden image on the plain of Dura, the three refused, declaring: <em>our God whom we serve is able to deliver us from the burning fiery furnace</em> — and even if he did not, they would not serve the king's gods (Daniel 3:17–18). Cast into a furnace heated seven times hotter than normal, they were unharmed, and a mysterious fourth figure appeared walking with them in the flames.</p>",
        "sections": [],
        "hitchcock_meaning": "that draws with force",
        "source_ids": {"easton": "meshach", "isbe": "meshach"},
        "key_refs": ["Daniel 1:7", "Daniel 3:12", "Daniel 3:25"]
    },
    "meshech": {
        "id": "meshech",
        "term": "Meshech",
        "category": "people",
        "intro": "<p>Meshech was a son of Japheth and grandson of Noah (Genesis 10:2), whose descendants gave their name to a people and region in the ancient Near East. In the Table of Nations they are listed alongside Tubal and Javan as northern peoples beyond the civilized world known to Israel. Ezekiel pairs Meshech and Tubal repeatedly as merchants trading in human slaves and bronze vessels with Tyre (Ezekiel 27:13) and as northern confederates of Gog who will invade Israel in the eschatological battle (Ezekiel 38:2–3; 39:1).</p><p>Psalm 120:5 uses Meshech as a symbol of exile among barbarous peoples: <em>Woe is me that I sojourn in Meshech, that I dwell among the tents of Kedar.</em> Ancient sources associate Meshech with the Mushki people of Anatolia (modern Turkey), though later speculative identification with Moscow has no scholarly basis. The name also appears in 1 Chronicles 1:5 and as a personal name in 1 Chronicles 1:17.</p>",
        "sections": [],
        "hitchcock_meaning": "who is drawn by force",
        "source_ids": {"easton": "meshech", "smith": "meshech", "isbe": "meshech"},
        "key_refs": ["Genesis 10:2", "Ezekiel 38:2", "Psalms 120:5"]
    },
    "meshelemiah": {
        "id": "meshelemiah",
        "term": "Meshelemiah",
        "category": "people",
        "intro": "<p>Meshelemiah (meaning <em>peace of the Lord</em> or <em>perfection of the Lord</em>) was a Levite of the family of Obed-edom who served as a gatekeeper of the tabernacle and later the temple in the time of David. He is listed among the chief porters appointed to guard the thresholds of the sanctuary (1 Chronicles 26:1–2, 9). His sons were also gatekeepers: Zechariah, his firstborn, is specifically noted for his discernment and counsel. The family's role as keepers of the temple gates was a distinguished Levitical office in Israel's liturgical organization.</p>",
        "sections": [],
        "hitchcock_meaning": "peace, or perfection, of the Lord",
        "source_ids": {"easton": "meshelemiah"},
        "key_refs": ["1 Chronicles 26:1", "1 Chronicles 26:9"]
    },
    "meshillemoth": {
        "id": "meshillemoth",
        "term": "Meshillemoth",
        "category": "people",
        "intro": "<p>Meshillemoth was the name of two figures in the Old Testament. The first was an Ephraimite whose son Berechiah opposed the plan to enslave Judahite captives after a victory of Pekah king of Israel, appealing to the law and the LORD's anger (2 Chronicles 28:12). The second was an ancestor of a priestly family that settled in Jerusalem after the exile (Nehemiah 11:13). The name likely derives from the same root as Meshullam, meaning <em>peace</em> or <em>recompense</em>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meshillemoth"},
        "key_refs": ["2 Chronicles 28:12", "Nehemiah 11:13"]
    },
    "meshullam": {
        "id": "meshullam",
        "term": "Meshullam",
        "category": "people",
        "intro": "<p>Meshullam (meaning <em>peaceable</em> or <em>perfect</em>) was one of the most common names in post-exilic Israel, borne by more than twenty distinct individuals in the Old Testament. Among the most notable: Meshullam son of Shaphan, whose grandson Ahikam protected the prophet Jeremiah (2 Kings 22:3); a high priestly ancestor in 1 Chronicles 9:11; Meshullam who repaired two sections of the Jerusalem wall during Nehemiah's rebuilding (Nehemiah 3:4, 30); and a Levite who assisted Ezra in teaching the law (Nehemiah 8:4). The frequency of the name reflects the importance of shalom-derived names in Israelite onomastics.</p>",
        "sections": [],
        "hitchcock_meaning": "peaceable; perfect; their parables",
        "source_ids": {"easton": "meshullam"},
        "key_refs": ["2 Kings 22:3", "Nehemiah 3:4", "1 Chronicles 9:11"]
    },
    "meshullemeth": {
        "id": "meshullemeth",
        "term": "Meshullemeth",
        "category": "people",
        "intro": "<p>Meshullemeth was the daughter of Haruz of Jotbah and the wife of King Manasseh of Judah, making her the mother of King Amon (2 Kings 21:19). She appears only in the regnal formula introducing Amon's reign. Her name is the feminine form of Meshullam, meaning <em>peaceable</em>. As the queen mother during Amon's two-year reign, she would have held the honored title of <em>gebirah</em> (great lady) at the Judahite court.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meshullemeth"},
        "key_refs": ["2 Kings 21:19"]
    },
    "mesopotamia": {
        "id": "mesopotamia",
        "term": "Mesopotamia",
        "category": "places",
        "intro": "<p>Mesopotamia (Greek: <em>land between the rivers</em>) denotes the broad alluvial plain between the Tigris and Euphrates rivers, roughly corresponding to modern Iraq. In the Old Testament the region is most often called Aram-Naharaim (<em>Aram of the two rivers</em>), and it figures prominently as the ancestral homeland of the patriarchs. Abraham came from Ur of the Chaldees in southern Mesopotamia; his servant traveled to Mesopotamia to find a wife for Isaac (Genesis 24:10); and Jacob fled there and spent twenty years in Paddan-aram.</p><p>Mesopotamia was also a source of political and military threat: Cushan-rishathaim, king of Mesopotamia, oppressed Israel for eight years before Othniel delivered them (Judges 3:8–10). The region encompassed the great empires of Sumer, Akkad, Babylon, and Assyria — the civilizations that successively shaped and threatened ancient Israel. In Acts 2:9 Mesopotamia is listed among the regions from which Jewish pilgrims came to Jerusalem at Pentecost.</p>",
        "sections": [],
        "hitchcock_meaning": "between two rivers",
        "source_ids": {"easton": "mesopotamia", "smith": "mesopotamia"},
        "key_refs": ["Genesis 24:10", "Judges 3:8", "Acts 2:9"]
    },
    "mess": {
        "id": "mess",
        "term": "Mess",
        "category": "concepts",
        "intro": "<p>A <em>mess</em>, in the biblical context, is a portion of food sent to a guest or set before a person at table. The word appears in the KJV in the account of Joseph's dinner with his brothers in Egypt: Joseph sent messes to his brothers from his own table, but Benjamin's mess was five times larger than those of his brothers (Genesis 43:34). The term also appears in 2 Samuel 11:8, where David sends a <em>mess of meat</em> to Uriah the Hittite. The usage reflects ancient Near Eastern practices of honoring a guest or displaying favor by the size and richness of the portion sent from the host's table.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mess"},
        "key_refs": ["Genesis 43:34", "2 Samuel 11:8"]
    },
    "messenger": {
        "id": "messenger",
        "term": "Messenger",
        "category": "concepts",
        "intro": "<p>A messenger in the biblical world was any person — human or divine — sent to carry a communication, command, or covenant. The Hebrew <em>malak</em> and Greek <em>angelos</em> both mean <em>messenger</em>, and both are translated variously as <em>messenger</em>, <em>angel</em>, or <em>envoy</em> depending on context. Human messengers served as diplomatic envoys between kings (1 Kings 20:2), military liaisons (2 Samuel 11:19), and personal carriers of letters and gifts.</p><p>The theological significance of messengers is seen in the prophetic usage: the prophets frequently understood themselves as messengers of the divine council, delivering a <em>Thus says the LORD</em> as a royal herald delivered a king's decree. Malachi 3:1 announces the coming of <em>my messenger</em> who will prepare the way — a text applied in the New Testament to John the Baptist. The concept of messenger underlies the biblical theology of prophecy, angels, and apostleship.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "messenger", "isbe": "messenger"},
        "key_refs": ["Malachi 3:1", "Matthew 11:10", "Isaiah 42:19"]
    },
    "messiah": {
        "id": "messiah",
        "term": "Messiah",
        "category": "concepts",
        "intro": "<p>Messiah (Hebrew <em>mashiach</em>; Greek <em>Christos</em>) means <em>anointed one</em> and refers to the person set apart for a sacred role by the rite of anointing with oil. In the Old Testament, priests, kings, and at least one prophet were anointed to their offices (Exodus 28:41; 1 Samuel 9:16; 1 Kings 19:16), and the reigning Israelite king was regularly called <em>the LORD's anointed.</em> The word in its eschatological sense — a future deliverer who would restore Israel and inaugurate God's kingdom — developed especially in the psalms and prophetic literature.</p><p>Daniel 9:25–26 uses <em>Messiah</em> as a title for the expected deliverer. The New Testament identifies Jesus of Nazareth as the fulfillment of all messianic expectation: his baptism, transfiguration, and resurrection confirm his anointing as prophet, priest, and king. Peter's confession <em>You are the Christ</em> (Matthew 16:16) and Jesus's own acceptance of the title before the high priest (Mark 14:62) are pivotal moments. <em>Christ</em> begins as a title but becomes effectively a second name for Jesus throughout the epistles.</p>",
        "sections": [],
        "hitchcock_meaning": "anointed",
        "source_ids": {"easton": "messiah", "smith": "messiah", "isbe": "messiah"},
        "key_refs": ["Daniel 9:25", "Matthew 16:16", "John 1:41", "Acts 2:36"]
    },
    "metheg-ammah": {
        "id": "metheg-ammah",
        "term": "Metheg-ammah",
        "category": "places",
        "intro": "<p>Metheg-ammah (meaning <em>bridle of bondage</em> or <em>bridle of the mother city</em>) appears in 2 Samuel 8:1, where David is said to have taken it from the Philistines — an event parallel to 1 Chronicles 18:1, which substitutes <em>Gath and its villages.</em> The term has been understood both as a place name (likely Gath, the major Philistine city) and as a more abstract expression denoting the key position or metropolis of Philistia. Most scholars identify Metheg-ammah with Gath and its surrounding dependent towns. David's capture of it ended Philistine control over key parts of the Shephelah.</p>",
        "sections": [],
        "hitchcock_meaning": "bridle of bondage",
        "source_ids": {"easton": "metheg-ammah"},
        "key_refs": ["2 Samuel 8:1", "1 Chronicles 18:1"]
    },
    "methusael": {
        "id": "methusael",
        "term": "Methusael",
        "category": "people",
        "intro": "<p>Methusael (meaning <em>who demands his death</em>, or possibly <em>man of God</em>) was a Cainite, the son of Mehujael and the father of Lamech in the line of Cain (Genesis 4:18). He is distinct from the antediluvian patriarch Methuselah, who was in the Sethite line. Methusael appears only in the genealogy of Genesis 4, where the parallel structure of the Cainite and Sethite lines uses similar names (Methusael / Methuselah; Lamech / Lamech) — a feature scholars often read as either literary parallelism or evidence of shared underlying traditions.</p>",
        "sections": [],
        "hitchcock_meaning": "who demands his death",
        "source_ids": {"easton": "methusael"},
        "key_refs": ["Genesis 4:18"]
    },
    "methuselah": {
        "id": "methuselah",
        "term": "Methuselah",
        "category": "people",
        "intro": "<p>Methuselah (meaning uncertain; possibly <em>man of the javelin</em> or <em>his death shall bring</em>) was the son of Enoch and the grandfather of Noah, and holds the biblical record for longevity — 969 years (Genesis 5:27), the longest lifespan recorded in Scripture. He was born when his father Enoch was 65, and Enoch's subsequent walk with God and translation without death (Genesis 5:22–24) sets his son's birth as a spiritual turning point. Methuselah fathered Lamech at age 187, and Lamech fathered Noah. According to the chronology of Genesis 5, Methuselah died in the year of the Flood — a fact that has prompted centuries of speculation about whether he perished in it.</p><p>Luke's genealogy of Jesus includes Methuselah (Luke 3:37), tracing the messianic line through Seth back to Adam. His name has become proverbial for extreme old age in Western culture.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "methuselah", "smith": "methuselah"},
        "key_refs": ["Genesis 5:21", "Genesis 5:27", "Luke 3:37"]
    },
    "mezahab": {
        "id": "mezahab",
        "term": "Mezahab",
        "category": "people",
        "intro": "<p>Mezahab (meaning <em>gilded</em> or <em>whose waters are gold</em>) was the grandfather of Mehetabel, who was the wife of Hadar (or Hadad), one of the kings of Edom listed in Genesis 36:39 and 1 Chronicles 1:50. He appears only in these genealogical notices. The name may suggest a place rather than a person — some scholars read it as a toponym, <em>waters of gold</em>, denoting a location associated with the Edomite royal family.</p>",
        "sections": [],
        "hitchcock_meaning": "gilded",
        "source_ids": {"easton": "mezahab"},
        "key_refs": ["Genesis 36:39", "1 Chronicles 1:50"]
    },
    "miamin": {
        "id": "miamin",
        "term": "Miamin",
        "category": "people",
        "intro": "<p>Miamin (meaning <em>the right hand</em>) was the name of two figures in post-exilic Judah. One was a priest who returned from Babylon with Zerubbabel (Nehemiah 12:5), and another was among the Israelites who had married foreign women and agreed to divorce them in accordance with Ezra's reform (Ezra 10:25). The name is a variant spelling of Miniamin. As a priestly name it suggests an honorific connection to the right hand — the position of favor and strength.</p>",
        "sections": [],
        "hitchcock_meaning": "the right hand",
        "source_ids": {"easton": "miamin"},
        "key_refs": ["Nehemiah 12:5", "Ezra 10:25"]
    },
    "mibhar": {
        "id": "mibhar",
        "term": "Mibhar",
        "category": "people",
        "intro": "<p>Mibhar (meaning <em>chosen</em> or <em>youth</em>) was one of David's thirty mighty warriors listed in 1 Chronicles 11:38, described as the son of Hagri. He may be the same individual called Bani the Gadite in the parallel list of 2 Samuel 23:36. The discrepancy between the two lists has been attributed to copying errors in the transmission of the text. Mibhar's inclusion among the thirty indicates he was one of the elite soldiers who formed David's bodyguard and fighting force.</p>",
        "sections": [],
        "hitchcock_meaning": "chosen; youth",
        "source_ids": {"easton": "mibhar"},
        "key_refs": ["1 Chronicles 11:38"]
    },
    "mibsam": {
        "id": "mibsam",
        "term": "Mibsam",
        "category": "people",
        "intro": "<p>Mibsam (meaning <em>smelling sweet</em>) was the name of two individuals in the Old Testament. The first was the fourth son of Ishmael and Abraham's concubine Hagar, listed among the twelve princes of Ishmael (Genesis 25:13; 1 Chronicles 1:29). The second was a descendant of Simeon, son of Shallum (1 Chronicles 4:25). The Ishmaelite Mibsam may have given his name to an Arabian tribe known for fragrant spices.</p>",
        "sections": [],
        "hitchcock_meaning": "smelling sweet",
        "source_ids": {"easton": "mibsam"},
        "key_refs": ["Genesis 25:13", "1 Chronicles 4:25"]
    },
    "mibzar": {
        "id": "mibzar",
        "term": "Mibzar",
        "category": "people",
        "intro": "<p>Mibzar (meaning <em>defending</em> or <em>a fortress</em>) was one of the chiefs (dukes) of Edom listed in the genealogies of Genesis 36:42 and 1 Chronicles 1:53. The Edomite chiefs in these lists are understood to be clan leaders or petty rulers of specific territories within Edom. Some scholars identify Mibzar with the fortified city of Bozrah or another Edomite stronghold, reading the name as a toponym that became a tribal designation.</p>",
        "sections": [],
        "hitchcock_meaning": "defending; forbidding; taking away",
        "source_ids": {"easton": "mibzar"},
        "key_refs": ["Genesis 36:42", "1 Chronicles 1:53"]
    },
    "micah": {
        "id": "micah",
        "term": "Micah",
        "category": "people",
        "intro": "<p>Micah (meaning <em>who is like God?</em> — a shortened form of Micaiah) was the name of several Old Testament figures, the most important being Micah the prophet of Moresheth and Micah the Ephraimite idolater. The Ephraimite Micah of Judges 17–18 was a man in the hill country of Ephraim who stole silver from his mother, then used it to make idols after she consecrated the money to the LORD. He installed a shrine and a private priest — illustrating the religious anarchy of the period when <em>every man did what was right in his own eyes.</em> A wandering Levite became his priest, and when the tribe of Dan migrated north, they seized both the Levite and the idols for their own sanctuary at Dan.</p><p>A separate Micah was a descendant of Jonathan son of Saul (1 Chronicles 8:34–35). The prophet Micah of Moresheth is treated separately under Micah, Book of.</p>",
        "sections": [],
        "hitchcock_meaning": "poor; humble",
        "source_ids": {"easton": "micah", "smith": "micah"},
        "key_refs": ["Judges 17:1", "Judges 18:30", "1 Chronicles 8:34"]
    },
    "micah-book-of": {
        "id": "micah-book-of",
        "term": "Micah, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Micah is the sixth of the twelve Minor Prophets, the work of Micah of Moresheth — a town in the Shephelah of Judah — who prophesied during the reigns of Jotham, Ahaz, and Hezekiah (approximately 735–700 BC), a contemporary of Isaiah. The book addresses Judah and Samaria on the eve of the Assyrian crisis, condemning social injustice, corrupt rulers, false prophets, and religious formalism while alternating with passages of remarkable consolation.</p><p>Micah contains some of the most memorable oracles in the prophetic canon. The climactic indictment of 6:8 — <em>He has shown you, O man, what is good; and what does the LORD require of you but to do justice, love kindness, and walk humbly with your God</em> — is one of Scripture's most celebrated ethical summaries. Equally famous is the Bethlehem oracle of 5:2, <em>But you, Bethlehem Ephrathah... from you shall come forth for me one who is to be ruler in Israel</em>, cited at Jesus's birth in Matthew 2:6. Micah 4:1–4 contains the vision of universal peace when nations beat their swords into plowshares — a passage nearly identical to Isaiah 2:2–4.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "micah-book-of", "isbe": "micah-book-of"},
        "key_refs": ["Micah 5:2", "Micah 6:8", "Matthew 2:6", "1 Kings 22:28"]
    },
    "micaiah": {
        "id": "micaiah",
        "term": "Micaiah",
        "category": "people",
        "intro": "<p>Micaiah son of Imlah was a prophet of the LORD in the northern kingdom during the reign of Ahab, famous for his courageous confrontation with the court prophets in 1 Kings 22. When Ahab and Jehoshaphat sought prophetic confirmation for their planned campaign against Ramoth-gilead, four hundred court prophets unanimously predicted victory. Micaiah alone spoke the truth: he saw Israel scattered on the mountains like sheep without a shepherd and described a vision of the divine council in which a lying spirit had been sent into the mouths of Ahab's prophets.</p><p>For this, Micaiah was struck, imprisoned, and given only bread and water until Ahab's return — but Ahab did not return; he was killed in battle just as Micaiah had prophesied. The episode is a sustained meditation on true versus false prophecy, the courage required to speak God's word against royal pressure, and the sovereignty of divine purpose. A different Micaiah, daughter of Uriel, was the mother of King Abijah (2 Chronicles 13:2).</p>",
        "sections": [],
        "hitchcock_meaning": "who is like to God?",
        "source_ids": {"easton": "micaiah", "smith": "micaiah"},
        "key_refs": ["1 Kings 22:8", "1 Kings 22:17", "1 Kings 22:28"]
    },
    "micha": {
        "id": "micha",
        "term": "Micha",
        "category": "people",
        "intro": "<p>Micha (a variant of Micah, meaning <em>who is like God?</em>) was the name of several minor figures in the Old Testament genealogies and lists. The most notable was Micha son of Mephibosheth (Merib-baal), the grandson of Jonathan and great-grandson of King Saul (2 Samuel 9:12), who is listed with a family of descendants in 1 Chronicles 8:35. Another Micha was among the Levites who sealed Nehemiah's covenant (Nehemiah 10:11), and a third was an ancestor of a family of Asaphite temple singers (Nehemiah 11:17, 22).</p>",
        "sections": [],
        "hitchcock_meaning": "same as Micaiah",
        "source_ids": {"easton": "micha"},
        "key_refs": ["2 Samuel 9:12", "1 Chronicles 8:35", "Nehemiah 10:11"]
    },
    "michael": {
        "id": "michael",
        "term": "Michael",
        "category": "people",
        "intro": "<p>Michael (meaning <em>who is like God?</em>) is the name of numerous figures in the Old Testament genealogies, and more significantly the name of the archangel who appears in Daniel, Jude, and Revelation as the heavenly defender of Israel and leader of the divine armies. In Daniel 10:13 and 10:21, Michael is described as <em>one of the chief princes</em> who came to assist the angelic messenger against the prince of Persia, and as <em>your prince</em> — the angelic guardian of Israel. Daniel 12:1 identifies Michael as the great prince who will stand up for Israel in the final tribulation.</p><p>In the New Testament, Jude 9 refers to Michael the archangel's dispute with the devil over the body of Moses — a tradition also preserved in early Jewish literature. Revelation 12:7–9 portrays Michael and his angels fighting the dragon (Satan) in a cosmic war and casting him out of heaven. Michael is thus the preeminent warrior angel in biblical tradition, whose name — <em>who is like God?</em> — functions as a battle cry against all who would usurp divine glory.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "michael", "smith": "michael", "isbe": "michael"},
        "key_refs": ["Daniel 10:13", "Daniel 12:1", "Jude 1:9", "Revelation 12:7"]
    },
    "michaiah": {
        "id": "michaiah",
        "term": "Michaiah",
        "category": "people",
        "intro": "<p>Michaiah is a variant spelling of Micaiah, meaning <em>who is like God?</em> It appears as the name of several minor figures: a Levite sent by Jehoshaphat to teach the law in the cities of Judah (2 Chronicles 17:7); the daughter of Uriel of Gibeah, who was the mother of King Abijah of Judah (2 Chronicles 13:2); and a priest who participated in Nehemiah's dedication of the Jerusalem wall (Nehemiah 12:41–42). The variant spelling reflects standard orthographic variation in Hebrew name transmission.</p>",
        "sections": [],
        "hitchcock_meaning": "Michael, same as Micah",
        "source_ids": {"easton": "michaiah"},
        "key_refs": ["2 Chronicles 17:7", "2 Chronicles 13:2", "Nehemiah 12:41"]
    },
    "michal": {
        "id": "michal",
        "term": "Michal",
        "category": "people",
        "intro": "<p>Michal was the younger daughter of King Saul and the first wife of David, whose story traces an arc from romantic devotion to bitter estrangement. She fell in love with David and Saul exploited this, making her hand conditional on David bringing one hundred Philistine foreskins as a bride-price — hoping the task would get David killed (1 Samuel 18:20–27). When Saul later sent men to kill David, Michal helped him escape through a window, placing a household idol in his bed to deceive the pursuers (1 Samuel 19:12–17).</p><p>During David's outlawed years, Saul gave Michal to another man, Palti son of Laish. When David became king, he demanded her return as part of a political settlement with the house of Saul (2 Samuel 3:13–16). The reunion was loveless: when David danced before the ark of the LORD, Michal despised him in her heart, and David's rebuke concluded with the notice that she had no children to the day of her death (2 Samuel 6:23). Her story is a study in the human costs of political marriage and dynastic conflict.</p>",
        "sections": [],
        "hitchcock_meaning": "who is perfect?",
        "source_ids": {"easton": "michal", "smith": "michal"},
        "key_refs": ["1 Samuel 18:27", "1 Samuel 19:12", "2 Samuel 6:16", "2 Samuel 6:23"]
    },
    "michmash": {
        "id": "michmash",
        "term": "Michmash",
        "category": "places",
        "intro": "<p>Michmash (also Michmas) was a town in the tribe of Benjamin, approximately seven miles north of Jerusalem in the hill country, sitting at the top of a pass that commanded the approach from the Jordan valley to the central highlands. Its name may mean <em>hidden</em> or <em>treasure.</em> The town is best known as the site of one of the most dramatic military episodes in the early monarchy: Saul and Jonathan's campaign against the Philistines in 1 Samuel 13–14.</p><p>The Philistines had stationed a large garrison at Michmash, and the pass was so narrow that the Philistine sentinels could see across to the Hebrew side. Jonathan and his armor-bearer crossed the pass secretly and attacked the Philistine outpost alone, trusting God to give them victory — and a divinely-sent panic swept through the Philistine camp, triggering a rout. Isaiah 10:28–29 lists Michmash among the towns on Sennacherib's line of march toward Jerusalem. Ezra 2:27 records that men of Michmas returned from the Babylonian exile.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "michmash", "smith": "michmash", "isbe": "michmash"},
        "key_refs": ["1 Samuel 13:11", "1 Samuel 14:14", "Isaiah 10:28", "Ezra 2:27"]
    },
    "michmethah": {
        "id": "michmethah",
        "term": "Michmethah",
        "category": "places",
        "intro": "<p>Michmethah was a place on the border between Ephraim and Manasseh, mentioned in the boundary descriptions of Joshua 16:6 and 17:7. It lay east of Shechem and served as a landmark for both tribal territories. The exact location is uncertain; some scholars identify it with Khirbet Julejil or another site near modern Nablus (ancient Shechem). Its significance in the text is purely geographical — a fixed reference point for delineating the complex tribal boundaries of central Canaan.</p>",
        "sections": [],
        "hitchcock_meaning": "the gift or death of a striker",
        "source_ids": {"easton": "michmethah"},
        "key_refs": ["Joshua 16:6", "Joshua 17:7"]
    },
    "michri": {
        "id": "michri",
        "term": "Michri",
        "category": "people",
        "intro": "<p>Michri (meaning <em>selling</em> or <em>of a price</em>) was a Benjaminite, the ancestor of Elah son of Uzzi, who is listed among those who settled in Jerusalem after the exile (1 Chronicles 9:8). He appears only in this genealogical notice and is otherwise unknown. The Benjaminite settlers in post-exilic Jerusalem were drawn from several clans, and Michri's family was evidently among those with the right of settlement in the city by virtue of tribal lineage.</p>",
        "sections": [],
        "hitchcock_meaning": "selling",
        "source_ids": {"easton": "michri"},
        "key_refs": ["1 Chronicles 9:8"]
    },
    "michtam": {
        "id": "michtam",
        "term": "Michtam",
        "category": "concepts",
        "intro": "<p>Michtam is a Hebrew term of uncertain meaning found in the superscriptions of six psalms: Psalms 16, 56–60. All six are attributed to David. The word has been interpreted variously as <em>golden psalm</em> (from <em>kethem</em>, gold), a <em>psalm engraved</em> (for permanence), a <em>secret</em> or <em>expiation psalm,</em> or a liturgical genre designation whose exact meaning was already lost by the time of the Septuagint translators. The Septuagint renders the term as <em>stelography</em> (inscription on a pillar), while modern scholars remain divided between musical, liturgical, and literary interpretations. Despite the uncertainty, the six Michtam psalms include some of the most theologically rich in the Psalter, notably Psalm 16 with its Resurrection resonances (Acts 2:25–28).</p>",
        "sections": [],
        "hitchcock_meaning": "golden psalm",
        "source_ids": {"easton": "michtam", "isbe": "michtam"},
        "key_refs": ["Psalms 16:1", "Psalms 56:1", "Acts 2:25"]
    },
    "middin": {
        "id": "middin",
        "term": "Middin",
        "category": "places",
        "intro": "<p>Middin (meaning <em>judgment</em>) was a town in the wilderness district of Judah listed among the six cities in that barren region in Joshua 15:61. It was located somewhere in the Judean wilderness west of the Dead Sea, in the general vicinity of En-gedi and Secacah. The exact site has not been positively identified, though some scholars associate it with a ruin near the northwestern shore of the Dead Sea. Like the other wilderness towns of Judah, Middin was likely a small settlement servicing trade and pasture in an arid landscape.</p>",
        "sections": [],
        "hitchcock_meaning": "judgment; striving",
        "source_ids": {"easton": "middin"},
        "key_refs": ["Joshua 15:61"]
    },
    "midian": {
        "id": "midian",
        "term": "Midian",
        "category": "people",
        "intro": "<p>Midian was the fourth son of Abraham by his concubine Keturah (Genesis 25:2) and the eponymous ancestor of the Midianites, a confederation of nomadic and semi-nomadic tribes that ranged across the desert regions east and south of Canaan — the Sinai peninsula, the Gulf of Aqabah, and northwestern Arabia. The Midianites appear repeatedly in the biblical narrative in both friendly and hostile roles. Moses fled to Midian after killing an Egyptian, married Zipporah the daughter of the Midianite priest Jethro (also called Reuel), and received pastoral hospitality there for forty years.</p><p>The same Jethro later gave Moses practical wisdom about judicial administration (Exodus 18). Yet during the wilderness period the Midianites also seduced Israel into idolatry at Baal-peor (Numbers 25), and in the time of the judges a Midianite coalition oppressed Israel for seven years until Gideon's dramatic defeat of their army (Judges 6–8). Isaiah 9:4 and 10:26 invoke the <em>day of Midian</em> as a paradigm of sudden divine deliverance.</p>",
        "sections": [],
        "hitchcock_meaning": "judgment; covering; habit",
        "source_ids": {"easton": "midian", "smith": "midian"},
        "key_refs": ["Genesis 25:2", "Exodus 2:15", "Numbers 25:17", "Judges 6:2"]
    },
    "midianite": {
        "id": "midianite",
        "term": "Midianite",
        "category": "people",
        "intro": "<p>The Midianites were the descendants of Midian son of Abraham and Keturah, a nomadic people occupying the desert regions east of the Gulf of Aqabah and the Sinai peninsula. They were camel-herding traders and raiders who played an ambivalent role in Israelite history. Joseph was sold to Midianite merchants traveling to Egypt (Genesis 37:28), and Moses spent forty years in Midian as son-in-law to the priest Jethro. Yet Midianite women were central to the Baal-peor apostasy (Numbers 25), prompting the command to treat Midian as an enemy and the punitive war of Numbers 31.</p><p>The Midianite oppression in the era of the judges (Judges 6–8), when Midianite raiders annually plundered Israel's harvests using camels, represents the climax of their antagonism. Gideon's rout of the Midianite army with three hundred men became a defining miracle of divine intervention in Israelite memory (Isaiah 9:4; Psalm 83:9).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "midianite", "smith": "midianite"},
        "key_refs": ["Genesis 37:28", "Numbers 25:17", "Judges 6:1", "Psalms 83:9"]
    },
    "midwife": {
        "id": "midwife",
        "term": "Midwife",
        "category": "concepts",
        "intro": "<p>The midwife (<em>meyaledet</em> in Hebrew, from the root <em>yalad</em>, to bear a child) was a woman who assisted in childbirth and played an important social and religious role in ancient Israelite society. The earliest named midwives in Scripture are Shiphrah and Puah, the Hebrew midwives who defied Pharaoh's command to kill all male Hebrew infants at birth, fearing God more than the king (Exodus 1:15–21). Their act of conscience is the Bible's first recorded instance of civil disobedience, and they were rewarded with households of their own.</p><p>Midwives also appear in the birth narratives of Rachel (Genesis 35:17) and Tamar (Genesis 38:28), where they tied a scarlet thread on the first hand to emerge. The midwife's role included catching the child, cutting the umbilical cord, washing and salting the newborn, and swaddling it — a picture evoked in Ezekiel 16:4 as a metaphor for Jerusalem's origins.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "midwife", "isbe": "midwife"},
        "key_refs": ["Exodus 1:15", "Genesis 35:17", "Genesis 38:28"]
    },
    "migdal-edar": {
        "id": "migdal-edar",
        "term": "Migdal-Edar",
        "category": "places",
        "intro": "<p>Migdal-Edar (Hebrew: <em>tower of the flock</em>) was the place near Bethlehem where Jacob pitched his tent after Rachel's death during the birth of Benjamin (Genesis 35:21). Its name suggests a watchtower used by shepherds to guard their flocks in the Bethlehem highlands — a feature of the pastoral landscape still visible in the region. Micah 4:8 uses the phrase <em>tower of the flock</em> (<em>Migdal-Eder</em>) as a poetic designation for Jerusalem or Zion in a prophecy of restoration, addressing the daughter of Zion as the guardian of God's flock.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "migdal-edar"},
        "key_refs": ["Genesis 35:21", "Micah 4:8"]
    },
    "migdal-el": {
        "id": "migdal-el",
        "term": "Migdal-el",
        "category": "places",
        "intro": "<p>Migdal-el (meaning <em>tower of God</em>) was a fortified city in the territory of Naphtali, listed in Joshua 19:38 among the cities allotted to that tribe. Its exact location is uncertain; various sites in upper Galilee have been proposed. The name suggests a prominent defensive tower or fortress, possibly associated with a sanctuary, that served as a regional landmark. It appears only in this single administrative list.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "migdal-el"},
        "key_refs": ["Joshua 19:38"]
    },
    "migdal-gad": {
        "id": "migdal-gad",
        "term": "Migdal-gad",
        "category": "places",
        "intro": "<p>Migdal-gad (meaning <em>tower of Gad</em>) was a town in the lowland district of Judah listed in Joshua 15:37 among the cities of the Shephelah. Its location in the foothills west of Hebron placed it in a strategically and agriculturally valuable zone. The name suggests a fortified tower associated with the god Gad — a deity of fortune — though by the time of Israel's occupation the name likely served purely as a toponym. The site has not been positively identified.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "migdal-gad"},
        "key_refs": ["Joshua 15:37"]
    },
    "migdol": {
        "id": "migdol",
        "term": "Migdol",
        "category": "places",
        "intro": "<p>Migdol (meaning <em>a tower</em> or <em>fortress</em>) was the name of one or more sites on the northeastern border of Egypt, near the Reed Sea. The Israelites camped near Migdol during the Exodus before the crossing of the sea (Exodus 14:2; Numbers 33:7), and Jeremiah and Ezekiel mention it as one of the places in Egypt where Jewish refugees settled after Jerusalem's fall (Jeremiah 44:1; 46:14; Ezekiel 29:10; 30:6). The repetition suggests Migdol was a well-known Egyptian border fortress commanding the approaches from Canaan, functioning as a military and administrative gateway.</p>",
        "sections": [],
        "hitchcock_meaning": "a tower",
        "source_ids": {"easton": "migdol", "smith": "migdol"},
        "key_refs": ["Exodus 14:2", "Jeremiah 44:1", "Ezekiel 29:10"]
    },
    "migron": {
        "id": "migron",
        "term": "Migron",
        "category": "places",
        "intro": "<p>Migron (meaning <em>a precipice</em> or <em>fear</em>) was a place in the territory of Benjamin associated with Saul's military movements during the campaign at Michmash (1 Samuel 14:2). It lay near Gibeah and Michmash. Isaiah 10:28 lists Migron on Sennacherib's line of march toward Jerusalem: <em>He has come to Aiath, he has passed through Migron; at Michmash he stores his baggage.</em> The site is likely identifiable with a location in the narrow Benjamin plateau north of Jerusalem, though the exact identification is disputed.</p>",
        "sections": [],
        "hitchcock_meaning": "fear; farm; throat",
        "source_ids": {"easton": "migron"},
        "key_refs": ["1 Samuel 14:2", "Isaiah 10:28"]
    },
    "mikloth": {
        "id": "mikloth",
        "term": "Mikloth",
        "category": "people",
        "intro": "<p>Mikloth (meaning <em>staves</em> or <em>little voices</em>) was the name of two figures in David's era. One was a Benjaminite who settled in Jerusalem (1 Chronicles 8:32; 9:37–38), a descendant of Jeiel the father of Gibeon. The other Mikloth was the deputy commander of the second monthly division of David's army, serving under Dodai the Ahohite (1 Chronicles 27:4). The administrative division system described in 1 Chronicles 27 rotated military service through the year, with each division responsible for one month.</p>",
        "sections": [],
        "hitchcock_meaning": "little wants; little voices; looking downward",
        "source_ids": {"easton": "mikloth"},
        "key_refs": ["1 Chronicles 8:32", "1 Chronicles 27:4"]
    },
    "milaiai": {
        "id": "milaiai",
        "term": "Milaiai",
        "category": "people",
        "intro": "<p>Milaiai was a priest and musician who participated in the dedication of the rebuilt walls of Jerusalem under Nehemiah, playing a musical instrument in one of the two great processions that Nehemiah organized around the wall (Nehemiah 12:36). He is otherwise unknown. His inclusion in the list underscores the musical and celebratory character of the wall dedication, which involved Levitical singers, priests with trumpets, and joyful processional liturgy as the community reconsecrated the city's defenses to the LORD.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "milaiai"},
        "key_refs": ["Nehemiah 12:36"]
    },
    "mildew": {
        "id": "mildew",
        "term": "Mildew",
        "category": "concepts",
        "intro": "<p>Mildew (<em>yerakon</em> in Hebrew, literally <em>paleness</em> or <em>yellowness</em>) is paired with <em>blight</em> (<em>shiddaphon</em>) throughout the Old Testament as one of the agricultural curses threatened for covenant disobedience. Deuteronomy 28:22 lists mildew among the disasters God will send upon disobedient Israel, and the pairing recurs in Amos 4:9, Haggai 2:17, and in Solomon's dedicatory prayer at the temple (1 Kings 8:37; 2 Chronicles 6:28). Mildew represents the fungal or climatic blight that destroys grain crops, turning them yellow and hollow rather than ripe and full.</p><p>The same Hebrew word can also refer to the pale greenish discoloration of human faces from illness or terror (Jeremiah 30:6), linking the agricultural and human applications of the concept. Both uses point to the same theological reality: the withering of life and fruitfulness under divine judgment.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mildew"},
        "key_refs": ["Deuteronomy 28:22", "1 Kings 8:37", "Amos 4:9", "Haggai 2:17"]
    },
    "mile": {
        "id": "mile",
        "term": "Mile",
        "category": "concepts",
        "intro": "<p>The mile mentioned in the New Testament (Matthew 5:41) is the Roman mile (<em>milion</em>), a unit of distance equal to one thousand double paces (<em>mille passuum</em>), approximately 4,854 English feet or about 1,478 meters — slightly shorter than the modern statute mile. Roman roads were marked with milestones (<em>milliaria</em>) throughout the empire, making the mile a familiar unit of distance in the Greco-Roman world. Jesus's instruction <em>whoever compels you to go one mile, go with him two</em> refers specifically to the Roman legal right of <em>angareia</em> — the commandeering of civilians to carry soldiers' equipment for one Roman mile — a common imposition in occupied Palestine.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mile"},
        "key_refs": ["Matthew 5:41"]
    },
    "miletus": {
        "id": "miletus",
        "term": "Miletus",
        "category": "places",
        "intro": "<p>Miletus was one of the great cities of ancient Ionia on the western coast of Asia Minor (modern Turkey), situated near the mouth of the Meander River approximately 36 miles south of Ephesus. In the classical period it was renowned for its philosophers (Thales, Anaximander, Anaximenes), its wool trade, and its extensive network of colonies around the Black Sea and Mediterranean. By Paul's day it had declined from its classical height but remained a significant harbor city.</p><p>Miletus figures in the New Testament as the site of Paul's farewell address to the Ephesian elders on his third missionary journey (Acts 20:15–38). Rather than visiting Ephesus and potentially being detained, Paul summoned the elders to meet him at Miletus, where he delivered his most personal recorded speech — reviewing his ministry among them, warning of coming wolves, and commending them to God and the word of his grace. He also left Trophimus sick at Miletus on a later journey (2 Timothy 4:20).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "miletus", "smith": "miletus", "isbe": "miletus"},
        "key_refs": ["Acts 20:15", "Acts 20:17", "2 Timothy 4:20"]
    },
    "milk": {
        "id": "milk",
        "term": "Milk",
        "category": "concepts",
        "intro": "<p>Milk was a staple of the ancient Israelite diet, produced from cows, goats, sheep, and camels. It was consumed fresh, curdled into yogurt (<em>hemah</em>), or made into cheese. The phrase <em>a land flowing with milk and honey</em> (first used in Exodus 3:8) became the standard biblical epitome for the abundance and fertility of Canaan, evoking pastoral and agricultural prosperity. Milk is also a symbol of doctrinal nurture in the New Testament: Peter urges new believers to <em>desire the pure milk of the word</em> (1 Peter 2:2), while Paul uses the milk/solid food contrast to distinguish elementary teaching from mature theology (1 Corinthians 3:2; Hebrews 5:12–14).</p><p>The law's prohibition <em>you shall not boil a kid in its mother's milk</em> (Exodus 23:19; Deuteronomy 14:21) has been widely understood as the basis for the Jewish dietary custom of separating meat and dairy, though its original intent may have been to prohibit a specific Canaanite cultic practice.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "milk", "isbe": "milk"},
        "key_refs": ["Exodus 3:8", "1 Peter 2:2", "1 Corinthians 3:2", "Exodus 23:19"]
    },
    "mill": {
        "id": "mill",
        "term": "Mill",
        "category": "concepts",
        "intro": "<p>The mill (<em>reḥayim</em> in Hebrew, dual form reflecting the two stones) was a household implement used to grind grain into flour, consisting of two circular millstones — a lower stationary stone (<em>pelaḥ taḥtit</em>) and an upper rotating stone (<em>rekeb</em>). Grinding was daily domestic labor performed primarily by women and female slaves. The sound of millstones was so characteristic of inhabited life that its cessation became a symbol of desolation: Jeremiah 25:10 lists the sound of millstones going silent among the signs of judgment, and Revelation 18:22 echoes this in the lament over Babylon.</p><p>Millstones were legally protected from seizure as pledges for debt (Deuteronomy 24:6) because they were essential for daily survival. Jesus references the millstone in a warning about causing children to stumble: <em>it would be better for him to have a great millstone fastened around his neck and to be drowned in the depth of the sea</em> (Matthew 18:6).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mill", "isbe": "mill"},
        "key_refs": ["Deuteronomy 24:6", "Jeremiah 25:10", "Matthew 18:6", "Revelation 18:22"]
    },
    "millennium": {
        "id": "millennium",
        "term": "Millennium",
        "category": "concepts",
        "intro": "<p>The Millennium (from Latin <em>mille annum</em>, a thousand years) refers to the period described in Revelation 20:1–7, during which Satan is bound in the abyss, the martyred saints reign with Christ, and the first resurrection takes place. The passage has generated three major interpretive traditions: <strong>premillennialism</strong>, which understands the thousand years as a literal future reign of Christ on earth after his return; <strong>postmillennialism</strong>, which sees the millennium as a golden age of gospel expansion before the second coming; and <strong>amillennialism</strong>, which interprets the thousand years symbolically as the entire church age between Christ's resurrection and return, during which Satan is already bound (in the sense of limited power over the nations).</p><p>All three traditions affirm the final defeat of Satan, the resurrection of the dead, and the last judgment at the end of the thousand years. The debate concerns the sequence and nature of these eschatological events. The term millennium does not appear in the Old Testament, though the prophetic hope for a transformed earth, universal knowledge of God, and messianic reign (Isaiah 11; 65; Micah 4) provides the OT backdrop for the NT concept.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "millennium", "isbe": "millennium"},
        "key_refs": ["Revelation 20:1", "Revelation 20:4", "Revelation 20:6"]
    },
    "millet": {
        "id": "millet",
        "term": "Millet",
        "category": "concepts",
        "intro": "<p>Millet (<em>dochan</em> in Hebrew) was a cereal grain cultivated in ancient Palestine alongside wheat, barley, and spelt. It appears in the Old Testament in two significant contexts: as an ingredient in the multi-grain bread Ezekiel was commanded to bake as a symbolic act (Ezekiel 4:9), and implicitly as one of the food supplies of the ancient Near East. Millet is a small-seeded grass — probably <em>Panicum miliaceum</em> (common millet) or <em>Sorghum bicolor</em> — that tolerates poor soils and dry conditions better than wheat, making it a staple food of the poor and a famine-resistant crop in marginal agricultural regions.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "millet"},
        "key_refs": ["Ezekiel 4:9"]
    },
    "millo": {
        "id": "millo",
        "term": "Millo",
        "category": "places",
        "intro": "<p>Millo (meaning <em>fullness</em>, likely referring to a filled-in terrace or earthwork) was a structural feature of ancient Jerusalem, associated with the defense and expansion of the city at several periods. David built <em>from the Millo inward</em> after capturing Jerusalem from the Jebusites (2 Samuel 5:9), indicating it was a pre-Israelite fortification feature at the north of the original City of David. Solomon later built up the Millo as part of his extensive building program, filling in the Kidron valley slope with terraces to support expanded construction (1 Kings 9:15, 24; 11:27).</p><p>Joash was assassinated at <em>the house of Millo on the way that goes down to Silla</em> (2 Kings 12:20). Hezekiah later repaired and strengthened the Millo as part of Jerusalem's defenses against Sennacherib (2 Chronicles 32:5). Archaeological excavations in the City of David have identified a massive stepped stone structure that many scholars identify as the Millo.</p>",
        "sections": [],
        "hitchcock_meaning": "fullness",
        "source_ids": {"easton": "millo", "smith": "millo"},
        "key_refs": ["2 Samuel 5:9", "1 Kings 9:15", "2 Chronicles 32:5"]
    },
    "mincing": {
        "id": "mincing",
        "term": "Mincing",
        "category": "concepts",
        "intro": "<p>Mincing appears in Isaiah 3:16 in the KJV as a description of the affected, dainty walk of the proud women of Jerusalem: <em>they walk with outstretched necks, glancing wantonly with their eyes, mincing along as they go, tinkling with their feet.</em> The Hebrew verb (<em>tapheph</em>) conveys the idea of short, tripping steps — an affectation designed to attract attention and display the ankle ornaments (anklets with bells) that the wealthy women wore. The passage is part of Isaiah's extended indictment of Jerusalem's vain luxury culture before the Assyrian crisis, cataloguing the elaborate jewelry and finery that would soon be replaced by mourning and deprivation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mincing"},
        "key_refs": ["Isaiah 3:16"]
    },
    "mine": {
        "id": "mine",
        "term": "Mine",
        "category": "concepts",
        "intro": "<p>Mining for metals and precious stones was practiced in the ancient Near East from prehistoric times, and several biblical passages attest to its familiarity in Israel. Job 28:1–11 contains the Bible's most extended treatment of mining — a poetic passage describing the miner's heroic descent into the earth to extract silver, gold, iron, and copper from darkness and rock. The passage uses the marvel of mining technology as a foil for the claim that wisdom cannot be found by human effort: <em>But where can wisdom be found?</em> (Job 28:12).</p><p>The Arabah region south of the Dead Sea was known for copper deposits (Deuteronomy 8:9 speaks of a land <em>whose hills you can dig copper</em>). The mines of Sinai (turquoise, copper), Egypt's gold mines in Nubia, and the iron mines of the Syrian steppe all feature in the broader ancient Near Eastern context of Israel's material culture.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mine", "isbe": "mine"},
        "key_refs": ["Deuteronomy 8:9", "Job 28:1", "Job 28:12"]
    },
    "minister": {
        "id": "minister",
        "term": "Minister",
        "category": "concepts",
        "intro": "<p>In biblical usage, a minister is one who serves another in an official or personal capacity. The Hebrew <em>mesharet</em> (servant, attendant) and Greek <em>diakonos</em> (deacon, servant) both convey the idea of active, purposeful service. In the Old Testament, Joshua was Moses's minister (<em>mesharet</em>), attending him personally (Exodus 24:13); the Levites ministered to the priests in the sanctuary (Numbers 3:6); and angels are called God's ministers who do his will (Psalm 103:21).</p><p>In the New Testament, <em>diakonos</em> designates both the general servant of all (as Jesus taught: <em>whoever would be great among you must be your servant</em>, Matthew 20:26) and the specific church office of deacon. Paul calls himself a minister of the new covenant (2 Corinthians 3:6) and of the gospel (Colossians 1:23). Civil rulers are also described as <em>ministers of God</em> for justice (Romans 13:4). The concept of ministry is thus deeply tied in Scripture to the reversal of status — the greatest as servant of all.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "minister", "isbe": "minister"},
        "key_refs": ["Exodus 24:13", "Matthew 20:26", "Romans 13:4", "2 Corinthians 3:6"]
    },
    "minni": {
        "id": "minni",
        "term": "Minni",
        "category": "places",
        "intro": "<p>Minni was a kingdom or territory called upon in Jeremiah's oracle against Babylon (Jeremiah 51:27) to join the alliance that would overthrow Babylon: <em>Set up a banner in the land, blow the trumpet among the nations, prepare the nations against her, call together against her the kingdoms of Ararat, Minni, and Ashkenaz.</em> Minni is generally identified with Mannai (Mannaea), an ancient kingdom south of Lake Urmia in northwestern Iran — a significant power in the ninth through seventh centuries BC that was a neighbor and sometimes rival of Urartu (Ararat) and was eventually absorbed into the Median empire. Jeremiah's oracle anticipates the alliance of northern peoples that would indeed overthrow Babylon.</p>",
        "sections": [],
        "hitchcock_meaning": "reckoned; prepared",
        "source_ids": {"easton": "minni"},
        "key_refs": ["Jeremiah 51:27"]
    },
    "minnith": {
        "id": "minnith",
        "term": "Minnith",
        "category": "places",
        "intro": "<p>Minnith was an Ammonite city mentioned in Judges 11:33 as the eastern limit of Jephthah's victory over the Ammonites: he struck them <em>from Aroer to the vicinity of Minnith, twenty cities.</em> The city also appears in Ezekiel 27:17, where it is listed alongside Judah and Israel as a source of wheat traded with Tyre — <em>they traded in your market wheat of Minnith, millet, honey, oil, and balm.</em> This suggests Minnith was located in the fertile agricultural zone east of the Jordan, probably in the highlands of ancient Ammon (modern Jordan). The exact site has not been positively identified.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Minni",
        "source_ids": {"easton": "minnith"},
        "key_refs": ["Judges 11:33", "Ezekiel 27:17"]
    },
    "minstrel": {
        "id": "minstrel",
        "term": "Minstrel",
        "category": "concepts",
        "intro": "<p>A minstrel in the biblical context was a professional musician, particularly one who played stringed instruments to create the conditions for prophetic inspiration or ceremonial mourning. The most notable instance is 2 Kings 3:15, where the prophet Elisha called for a minstrel: <em>But now bring me a minstrel. And when the minstrel played, the hand of the LORD came upon him.</em> This unusual account suggests that music could prepare a prophet's spirit to receive divine communication — a practice with parallels in other ancient Near Eastern prophetic traditions.</p><p>In Matthew 9:23, Jesus encountered minstrels (flute players) making a noise at the house of Jairus's daughter, performing the customary professional mourning rites. Jesus dismissed them before raising the child. The Hebrew <em>menagen</em> and Greek <em>auletes</em> (flute player) represent the same social function: trained musicians who served both sacred and secular needs.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "minstrel"},
        "key_refs": ["2 Kings 3:15", "Matthew 9:23"]
    },
    "mint": {
        "id": "mint",
        "term": "Mint",
        "category": "concepts",
        "intro": "<p>Mint (<em>heduosmon</em> in Greek, literally <em>sweet-smelling</em>) is a fragrant herb mentioned in the New Testament in Jesus's rebuke of the scribes and Pharisees: <em>You tithe mint and dill and cumin, and have neglected the weightier matters of the law: justice and mercy and faithfulness</em> (Matthew 23:23; Luke 11:42). The Pharisaic practice of tithing even tiny garden herbs like mint demonstrated meticulous attention to the letter of the law (Leviticus 27:30 required tithing of all produce), which Jesus does not criticize in itself — <em>these you ought to have done</em> — but contrasts with neglect of more fundamental obligations.</p><p>Mint was widely cultivated in Palestine for culinary and medicinal use. The species is likely <em>Mentha longifolia</em> (horsemint), which grows wild in moist areas throughout the region.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mint"},
        "key_refs": ["Matthew 23:23", "Luke 11:42"]
    },
    "miracle": {
        "id": "miracle",
        "term": "Miracle",
        "category": "concepts",
        "intro": "<p>A miracle, in biblical theology, is an extraordinary event that demonstrates divine power operating beyond or contrary to the ordinary course of nature, performed to confirm a divine message, authenticate a divine messenger, or accomplish a redemptive purpose. The Old Testament uses several terms: <em>ot</em> (sign), <em>mopheth</em> (wonder), and <em>niflaot</em> (wonders, marvelous things). The New Testament employs <em>semeion</em> (sign), <em>teras</em> (wonder), and <em>dynamis</em> (mighty work or power), often in combination.</p><p>Biblical miracles cluster around the great moments of redemptive history: the Exodus from Egypt, the wilderness period, the ministry of Elijah and Elisha, and supremely the ministry of Jesus and the early church. Jesus's miracles are presented in the Gospels as signs of the kingdom of God breaking into the present age — healing the sick, raising the dead, and commanding nature and demons. John's Gospel selects seven signs to demonstrate that Jesus is the Christ, the Son of God (John 20:30–31). Paul reports that the signs of an apostle included miracles performed in the Spirit (2 Corinthians 12:12).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "miracle", "smith": "miracle", "isbe": "miracle"},
        "key_refs": ["John 2:11", "John 20:30", "Acts 2:22", "2 Corinthians 12:12"]
    },
    "miriam": {
        "id": "miriam",
        "term": "Miriam",
        "category": "people",
        "intro": "<p>Miriam was the elder sister of Moses and Aaron, a prophetess and leader in Israel during the Exodus generation. Her name (meaning <em>rebellion</em> or possibly a variant of Mary) appears first in the account of infant Moses's rescue, where she watched over her baby brother in the basket on the Nile and arranged for their mother to nurse him under Pharaoh's daughter (Exodus 2:4–8). After the crossing of the Reed Sea, Miriam led the women of Israel in the first victory song recorded in Scripture, tambourine in hand: <em>Sing to the LORD, for he has triumphed gloriously</em> (Exodus 15:20–21).</p><p>Micah 6:4 names Miriam alongside Moses and Aaron as joint leaders of the Exodus community — a rare acknowledgment of female leadership in the Pentateuch. Her story also contains a cautionary episode: she and Aaron spoke against Moses over his Cushite wife and challenged his unique prophetic authority; Miriam alone was struck with <em>tzara'at</em> (leprosy), healed after seven days at Moses's intercession (Numbers 12). She died at Kadesh and was buried there (Numbers 20:1).</p>",
        "sections": [],
        "hitchcock_meaning": "rebellion",
        "source_ids": {"easton": "miriam", "smith": "miriam", "isbe": "miriam"},
        "key_refs": ["Exodus 2:4", "Exodus 15:20", "Numbers 12:10", "Micah 6:4"]
    },
    "misdeem": {
        "id": "misdeem",
        "term": "Misdeem",
        "category": "concepts",
        "intro": "<p>Misdeem is an archaic English verb meaning <em>to misjudge</em> or <em>to form a wrong opinion about.</em> It appears in the KJV rendering of Deuteronomy 1:27 in some older English versions, translating the Hebrew term for the people's false accusation that the LORD hated them and had brought them out of Egypt to destroy them in the wilderness. The word reflects the biblical concern with accurately discerning God's purposes and intentions — the opposite of misdeemance is the faith that trusts God's declarations about his own character against all negative appearances.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "misdeem"},
        "key_refs": ["Deuteronomy 1:27"]
    },
    "misgab": {
        "id": "misgab",
        "term": "Misgab",
        "category": "places",
        "intro": "<p>Misgab (meaning <em>the high fortress</em> or <em>lofty refuge</em>) appears in Jeremiah 48:1 in the KJV as a place in Moab: <em>Woe to Nebo! for it is spoiled; Kiriathaim is confounded and taken; Misgab is confounded and dismayed.</em> Most modern translations render <em>misgab</em> as a common noun — <em>the stronghold</em> — rather than as a proper place name, understanding Jeremiah to be lamenting the fall of Moab's fortresses generally. Whether it names a specific fortress or denotes Moabite strength as a concept, the oracle announces its vulnerability before the coming judgment.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "misgab"},
        "key_refs": ["Jeremiah 48:1"]
    },
    "mishael": {
        "id": "mishael",
        "term": "Mishael",
        "category": "people",
        "intro": "<p>Mishael (meaning <em>who is what God is?</em> or <em>who is asked for or lent</em>) was the Hebrew name of the companion of Daniel given the Babylonian name Meshach (Daniel 1:6–7). He was among the Judahite nobles taken to Babylon by Nebuchadnezzar and trained for royal service. Along with Shadrach and Abednego, he refused to worship Nebuchadnezzar's golden image and was cast into the fiery furnace — emerging unharmed in the company of a mysterious fourth figure (Daniel 3).</p><p>Two other figures named Mishael appear in the Old Testament: a Levite who was a cousin of Moses and Aaron (Exodus 6:22; Leviticus 10:4), who helped remove the bodies of Nadab and Abihu after they were struck dead for offering unauthorized fire; and a man who stood at Ezra's left hand when Ezra read the law to the assembly (Nehemiah 8:4).</p>",
        "sections": [],
        "hitchcock_meaning": "who is asked for or lent",
        "source_ids": {"easton": "mishael"},
        "key_refs": ["Daniel 1:6", "Daniel 3:12", "Exodus 6:22", "Nehemiah 8:4"]
    },
    "mishal": {
        "id": "mishal",
        "term": "Mishal",
        "category": "places",
        "intro": "<p>Mishal (also spelled Misheal, meaning <em>parables</em> or <em>request</em>) was a Levitical city in the territory of Asher allotted to the Gershonite Levites (Joshua 21:30; 1 Chronicles 6:74). It appears also in the list of Asher's cities in Joshua 19:26 (as Miseal). The exact location is unknown; it was somewhere in the coastal plain of Galilee. As a Levitical city it served as a residence for Levitical families in the Asherite territory, following the Mosaic provision for Levites to live distributed among the tribes rather than holding a territorial portion of their own.</p>",
        "sections": [],
        "hitchcock_meaning": "parables; governing",
        "source_ids": {"easton": "mishal"},
        "key_refs": ["Joshua 19:26", "Joshua 21:30", "1 Chronicles 6:74"]
    },
    "misham": {
        "id": "misham",
        "term": "Misham",
        "category": "people",
        "intro": "<p>Misham (meaning <em>their savior</em> or <em>swift</em>) was a Benjaminite, the son of Elpaal, listed in the genealogy of 1 Chronicles 8:12 among those who built Ono and Lod with their villages. This brief mention preserves the memory of a Benjaminite clan leader who was involved in building or rebuilding towns in the Shephelah region west of Jerusalem — towns that appear again in the post-exilic lists of Ezra and Nehemiah as settlements of the returning exiles. Misham is otherwise unknown.</p>",
        "sections": [],
        "hitchcock_meaning": "their savior; taking away",
        "source_ids": {"easton": "misham"},
        "key_refs": ["1 Chronicles 8:12"]
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
    print(f'BP m3: Mercurius → Misham: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__':
    main()
