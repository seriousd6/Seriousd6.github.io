"""
BP Article Synthesis — k1: Kabzeel → Kore
Covers Easton entries: Kabzeel through Kore (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-k1.py
Run: python3 scripts/bp-k1.py
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
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "kabzeel": {
        "id": "kabzeel",
        "term": "Kabzeel",
        "category": "places",
        "intro": "<p>Kabzeel (meaning <em>the congregation of God</em>) was a city in the extreme south of Judah, on the border with Idumaea (Edom), listed among the towns of the Negev in Joshua 15:21. It was the birthplace of Benaiah son of Jehoiada, one of David's three chief mighty men who slew two lion-like men of Moab, descended into a pit on a snowy day and killed a lion, and struck down an impressive Egyptian warrior with the Egyptian's own spear. Benaiah rose to command David's bodyguard (the Cherethites and Pelethites) and later became commander-in-chief of Solomon's army.</p><p>After the Babylonian exile, the city was resettled by returning Judeans and appears in Nehemiah 11:25 as Jekabzeel—a slightly altered form of the name suggesting either scribal variation or the site's restoration under a renewed covenant identity. Its precise modern location in the Negev has not been definitively established, though proposals have included sites in the Beersheba basin. Kabzeel's claim to biblical memory rests primarily on its association with the family of Benaiah, whose exceptional military career elevated him to the highest ranks of Israel's leadership.</p>",
        "sections": [],
        "hitchcock_meaning": "the congregation of God",
        "source_ids": {"easton": "kabzeel", "smith": "kabzeel", "isbe": "kabzeel"},
        "key_refs": ["Joshua 15:21", "2 Samuel 23:20", "Nehemiah 11:25"]
    },
    "kadesh": {
        "id": "kadesh",
        "term": "Kadesh",
        "category": "places",
        "intro": "<p>Kadesh (meaning <em>holy</em> or <em>sacred</em>) designates two distinct sites in the biblical record. Kadesh-barnea, the more prominent, was the oasis in the Wilderness of Paran where Israel camped for extended periods during the Exodus. It was from here that Moses sent the twelve spies into Canaan (Numbers 13), and the faithless report of ten of them condemned a generation to forty years of wilderness wandering. Miriam died and was buried at Kadesh (Numbers 20:1), and it was also the scene of Moses's failure at the waters of Meribah, which cost him entry into the promised land. The site is identified with Ain el-Qudeirat in the northeastern Sinai.</p><p>A second Kadesh, known as Kadesh on the Orontes, was the sacred city of the Hittites on the left bank of the Orontes River in Syria, site of the famous Battle of Kadesh (c. 1274 BC) between Pharaoh Ramesses II and the Hittite king Muwatalli II—one of the earliest recorded pitched battles in history and the occasion of one of antiquity's first known peace treaties. This northern Kadesh is distinct from the Israelite Kadesh-barnea but shares the same root meaning of holiness, suggesting both sites were regarded as sacred in their respective traditions.</p>",
        "sections": [],
        "hitchcock_meaning": "holiness",
        "source_ids": {"easton": "kadesh", "isbe": "kadesh-barnea"},
        "key_refs": ["Numbers 13:26", "Numbers 20:1", "Numbers 20:13", "Deuteronomy 1:46"]
    },
    "kadmiel": {
        "id": "kadmiel",
        "term": "Kadmiel",
        "category": "people",
        "intro": "<p>Kadmiel (meaning <em>before God</em> or <em>God of antiquity</em>) was a prominent Levite who returned from the Babylonian exile with Zerubbabel in the first wave of returning exiles. His family is listed in Ezra 2:40 and Nehemiah 7:43 as belonging to the Levitical contingent that came back to reestablish temple worship in Jerusalem. Kadmiel and his sons played active roles in the post-exilic reconstruction and religious renewal.</p><p>He is specifically named in Nehemiah 9:4–5 among the Levites who stood on the platform leading the great assembly in confession and praise during the covenant renewal ceremony, and he appears again in Nehemiah 10:9 as one of the Levites who set their seal to the solemn covenant. In Nehemiah 12:8 and 12:24 he is listed among the Levitical leaders overseeing the praise and thanksgiving at the dedication of the rebuilt walls. Kadmiel's repeated appearance in the key moments of post-exilic Jewish life makes him one of the more prominent Levitical figures in the restoration community.</p>",
        "sections": [],
        "hitchcock_meaning": "God of antiquity; God of the beginning",
        "source_ids": {"easton": "kadmiel", "smith": "kadmiel", "isbe": "kadmiel"},
        "key_refs": ["Ezra 2:40", "Nehemiah 9:4", "Nehemiah 10:9", "Nehemiah 12:8"]
    },
    "kadmonites": {
        "id": "kadmonites",
        "term": "Kadmonites",
        "category": "people",
        "intro": "<p>The Kadmonites (<em>orientals</em> or <em>easterners</em>) were a Canaanite or semi-nomadic tribe included in the list of peoples whose land God promised to Abraham in Genesis 15:19. Listed alongside the Kenites and Kenizzites in the covenant oracle, the Kadmonites are otherwise unattested in Scripture—they appear in this single reference as part of the enumeration of ten nations inhabiting the territory between the River of Egypt and the Euphrates that constituted the full extent of the Abrahamic land grant.</p><p>The name derives from the Hebrew root meaning <em>east</em> or <em>ancient</em>, suggesting they were either an eastern people or one of the primordial inhabitants of the region. Their absence from the conquest narratives of Joshua suggests they had been absorbed, displaced, or assimilated long before Israel arrived—or that the Genesis 15 list represents a more expansive vision of the promised territory than what the conquest actually secured. The Kadmonites stand as one of several pre-Israelite peoples whose identity and fate remain obscure beyond their mention in the Abrahamic covenant.</p>",
        "sections": [],
        "hitchcock_meaning": "ancients; chiefs of the East",
        "source_ids": {"easton": "kadmonites", "smith": "kadmonites"},
        "key_refs": ["Genesis 15:19"]
    },
    "kanah": {
        "id": "kanah",
        "term": "Kanah",
        "category": "places",
        "intro": "<p>Kanah (meaning <em>reedy</em> or <em>of reeds</em>) refers to two distinct biblical locations. The more geographically significant was a brook or stream forming the boundary between the tribes of Ephraim and Manasseh in the central hill country, flowing westward toward the Mediterranean. The Kanah brook is mentioned in Joshua 16:8 and 17:9 as a landmark in the tribal boundary descriptions, and its identification with the modern Wadi Qana (which drains the western slopes of the Samarian hills) is generally accepted.</p><p>A second Kanah was a town in the territory of Asher (Joshua 19:28), located in the northern coastal region near Tyre and Sidon. This Kanah has been identified with Qana el-Jalil, a village in the hills east of Tyre. The shared name reflects the common occurrence of reed-beds along streams and near springs throughout ancient Palestine. The brook Kanah's role as a tribal boundary marker gives it greater significance in the biblical land allotments than the town, whose only mention is in the Asherite city list.</p>",
        "sections": [],
        "hitchcock_meaning": "of reeds",
        "source_ids": {"easton": "kanah", "smith": "kanah", "isbe": "kanah"},
        "key_refs": ["Joshua 16:8", "Joshua 17:9", "Joshua 19:28"]
    },
    "kareah": {
        "id": "kareah",
        "term": "Kareah",
        "category": "people",
        "intro": "<p>Kareah (meaning <em>bald</em>) was the father of Johanan and Jonathan, two military commanders who initially remained loyal to Gedaliah, the governor appointed by Nebuchadnezzar over the remnant left in Judah after the Babylonian destruction of Jerusalem. His sons warned Gedaliah of Ishmael's plot to assassinate him—a warning the governor fatally ignored (Jeremiah 40:13–16).</p><p>After Ishmael murdered Gedaliah, it was Johanan son of Kareah who led the military commanders in pursuing Ishmael, rescuing the captives he was taking toward Ammon, and then—against Jeremiah's explicit counsel—leading the remaining Judeans down to Egypt for fear of Babylonian reprisals. Kareah is mentioned only as the patronymic of his more famous son Johanan, and his own background and history are unknown. The name appears repeatedly in the Jeremiah narrative (40:8, 13, 15, 16; 41:11, 13, 14, 16; 42:1, 8; 43:2, 4, 5) as a consistent identifier for this prominent military officer in the crisis period after Jerusalem's fall.</p>",
        "sections": [],
        "hitchcock_meaning": "bald; ice",
        "source_ids": {"easton": "kareah", "smith": "kareah", "isbe": "kareah"},
        "key_refs": ["Jeremiah 40:8", "Jeremiah 40:13", "Jeremiah 41:11", "Jeremiah 43:4"]
    },
    "karkaa": {
        "id": "karkaa",
        "term": "Karkaa",
        "category": "places",
        "intro": "<p>Karkaa (meaning <em>floor</em> or <em>bottom</em>) was a place on the southern boundary of Judah, mentioned in Joshua 15:3 as a landmark in the boundary description running from the Scorpion Pass toward Azmon and the Brook of Egypt. It lay roughly midway between the Ascent of Akrabbim and Azmon in the Negev wilderness, and served as one of the reference points delineating Judah's southernmost extent.</p><p>Beyond this single boundary reference, Karkaa is entirely unknown in the biblical narrative and has not been positively identified by archaeology. Its name suggesting a flat or level area—perhaps a basin or valley floor visible as a landmark from the surrounding ridge terrain—is consistent with the kind of natural feature used to fix boundary lines in the Negev. The extreme south of Judah where Karkaa lay was arid desert transitioning toward the Sinai peninsula, inhabited by only the most marginal agricultural communities and traversed by caravan routes connecting Canaan to Egypt.</p>",
        "sections": [],
        "hitchcock_meaning": "floor; dissolving cold",
        "source_ids": {"easton": "karkaa"},
        "key_refs": ["Joshua 15:3"]
    },
    "karkor": {
        "id": "karkor",
        "term": "Karkor",
        "category": "places",
        "intro": "<p>Karkor (meaning <em>foundation</em> or <em>they rested</em>) was a place in the open desert wastes east of the Jordan where Zebah and Zalmunna, the two kings of Midian, had encamped with the remnant of their army after the main Midianite force had been routed by Gideon. Judges 8:10 records that fifteen thousand men remained of the vast host, the rest having fallen in battle.</p><p>Gideon pursued them all the way to Karkor with his three hundred men, launched a surprise attack from the direction of the nomads' route east of Nobah and Jogbehah, and routed the entire army, capturing the two kings. The location of Karkor is uncertain but was evidently deep in the Transjordanian desert, far enough from Israelite territory that the Midianites considered themselves safe from pursuit. Gideon's relentless chase to Karkor—refusing food and rest even when the men of Succoth and Penuel refused to provision him—became legendary as one of the most dramatic military pursuits in the period of the Judges.</p>",
        "sections": [],
        "hitchcock_meaning": "they rested; foundation; soft ground",
        "source_ids": {"easton": "karkor", "smith": "karkor", "isbe": "karkor"},
        "key_refs": ["Judges 8:10", "Judges 8:12"]
    },
    "kartah": {
        "id": "kartah",
        "term": "Kartah",
        "category": "places",
        "intro": "<p>Kartah (meaning <em>city</em>) was a town in the tribal territory of Zebulun assigned to the Levites of the Merarite clan, listed in Joshua 21:34 as one of the cities given to the Levites from Zebulun's inheritance. It appears only in this Levitical city list and is not mentioned elsewhere in the biblical narrative.</p><p>Kartah's location within Zebulun's territory placed it in the lower Galilee region, the fertile area between the Jezreel Valley and the hills above the Sea of Galilee. Its Levitical designation meant it served as a center for priestly instruction and religious life for the surrounding population. The site has not been positively identified by modern archaeology, as many of the smaller Levitical cities in the northern tribes lack clear physical correlates. The city list in Joshua 21 reflects the Deuteronomic ideal of a network of Levitical teaching centers distributed throughout the tribal lands.</p>",
        "sections": [],
        "hitchcock_meaning": "calling; meeting",
        "source_ids": {"easton": "kartah", "smith": "kartah", "isbe": "kartah"},
        "key_refs": ["Joshua 21:34"]
    },
    "kartan": {
        "id": "kartan",
        "term": "Kartan",
        "category": "places",
        "intro": "<p>Kartan (meaning <em>double city</em>) was a town of Naphtali assigned to the Gershonite Levites, appearing in Joshua 21:32 as one of three cities from Naphtali given to the Gershonites. It is identified with Kirjathaim of 1 Chronicles 6:76, where the same Levitical assignment is recorded under a slightly different form of the name. The dual form of the name (<em>kartan</em> suggesting two components or two quarters) may reflect an ancient settlement that grew from paired villages.</p><p>Naphtali's territory lay in the upper Galilee region, and Kartan's location there placed it in one of the northernmost districts of ancient Israel. The identification with Kirjathaim allows tentative localization somewhere in the highlands of northern Galilee, though the precise site remains unidentified. Like other Levitical cities, Kartan's significance derived not from its size but from its function as a pastoral and instructional center for the tribe of Naphtali, maintaining the Levitical presence in a territory prone to foreign religious influence due to its proximity to Phoenicia and Aram.</p>",
        "sections": [],
        "hitchcock_meaning": "double city",
        "source_ids": {"easton": "kartan", "smith": "kartan", "isbe": "kartan"},
        "key_refs": ["Joshua 21:32", "1 Chronicles 6:76"]
    },
    "kattath": {
        "id": "kattath",
        "term": "Kattath",
        "category": "places",
        "intro": "<p>Kattath was a town of the tribe of Asher, listed in Joshua 19:15 among the cities of Zebulun's or Asher's allotment. It has been identified by some scholars with Kitron (Judges 1:30), from which the Zebulunites failed to drive out the Canaanite inhabitants, and also with Kana el-Jalil. The town appears only in the boundary and city lists of Joshua, receiving no narrative treatment elsewhere in Scripture.</p><p>Its location in the lower Galilee region, where the territories of several northern tribes overlapped and intersected with Canaanite population centers, explains why Zebulun's inability to fully possess such towns is noted in Judges 1. The Canaanites of Kattath/Kitron were not expelled but subjected to forced labor—an accommodation that the Deuteronomic historian viewed as a failure of the conquest ideal. The town's obscurity in subsequent biblical history suggests it remained a minor settlement in the Galilean highlands.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kattath", "smith": "kattath", "isbe": "kattath"},
        "key_refs": ["Joshua 19:15", "Judges 1:30"]
    },
    "kedar": {
        "id": "kedar",
        "term": "Kedar",
        "category": "people",
        "intro": "<p>Kedar (meaning <em>dark-skinned</em> or <em>sorrow</em>) was the second son of Ishmael (Genesis 25:13) and the ancestor of a powerful confederation of Arab tribes that inhabited the desert regions between Arabia and the Fertile Crescent. The Kedarites became one of the most prominent desert peoples of the ancient Near East, known as skilled archers and traders who managed vast flocks and drove the caravan trade routes through the Syrian and Arabian deserts. Their black tents became proverbial: the Song of Solomon's opening verse compares the beloved to <em>the tents of Kedar</em> as a symbol of striking, sun-darkened beauty.</p><p>The prophets addressed Kedar frequently, reflecting the tribe's significance as a contemporary geopolitical force. Isaiah 21:16–17 and 42:11 refer to Kedar in oracles concerning the desert peoples; Jeremiah 2:10 uses the Kedarites as an example of nations loyal to their gods in contrast to faithless Israel. Ezekiel 27:21 lists Kedar among the trading partners of Tyre, supplying lambs, rams, and goats. Psalm 120:5 expresses the anguish of dwelling among those who hate peace by comparing it to sojourning with Kedar. In later tradition, the Kedarites were identified with the Arabs and the lineage of the Prophet Muhammad traces through Ishmael.</p>",
        "sections": [],
        "hitchcock_meaning": "blackness; sorrow",
        "source_ids": {"easton": "kedar", "smith": "kedar", "isbe": "kedar"},
        "key_refs": ["Genesis 25:13", "Psalm 120:5", "Isaiah 42:11", "Jeremiah 2:10"]
    },
    "kedemah": {
        "id": "kedemah",
        "term": "Kedemah",
        "category": "people",
        "intro": "<p>Kedemah (meaning <em>eastward</em> or <em>ancient</em>) was the last-named of the twelve sons of Ishmael listed in Genesis 25:15 and 1 Chronicles 1:31. As one of Ishmael's sons, he became the ancestor of an Arabian tribe or clan whose territory lay in the eastern or southeastern desert regions. The name's association with the east (<em>qedem</em>) suggests his descendants occupied territory in the direction of the sunrise from Canaan—the broad region of the northern Arabian peninsula or Syrian desert.</p><p>Like most of Ishmael's sons, Kedemah appears only in the genealogical list and receives no further narrative treatment in Scripture. The twelve sons of Ishmael correspond to twelve princes who became heads of clans and tribes, inhabiting the region from Havilah to Shur, across the face of Egypt in the direction of Assyria (Genesis 25:18). These twelve mirror the twelve sons of Jacob and the twelve sons of Nahor, reflecting a broader biblical pattern of twelve-tribe groupings as the organizing unit of ethnic and territorial identity.</p>",
        "sections": [],
        "hitchcock_meaning": "oriental; ancient; first",
        "source_ids": {"easton": "kedemah", "smith": "kedemah", "isbe": "kedemah"},
        "key_refs": ["Genesis 25:15", "1 Chronicles 1:31"]
    },
    "kedemoth": {
        "id": "kedemoth",
        "term": "Kedemoth",
        "category": "places",
        "intro": "<p>Kedemoth (meaning <em>beginnings</em> or <em>easternmost</em>) was a Levitical city in the territory of Reuben east of the Jordan, assigned to the Levites of the Merarite clan (Joshua 13:18; 21:37; 1 Chronicles 6:79). Moses sent messengers from the wilderness of Kedemoth to Sihon king of Heshbon with a peaceful request for passage through his territory, an overture that Sihon refused, triggering the battle that gave Israel its first Transjordanian territory (Deuteronomy 2:26–37).</p><p>The city's location in the Reubenite tableland east of the Dead Sea placed it in the fertile highland region between the Arnon and Jabbok rivers. The identification with a site near modern Khirbet er-Remeil has been proposed, though certainty is elusive. As a Levitical city in Transjordan, Kedemoth served as an administrative and religious center for the tribes of Reuben and Gad. Its connection to Moses's diplomatic overture before the conquest of Sihon gives it historical significance as the point of departure for Israel's first major military engagement east of the Jordan.</p>",
        "sections": [],
        "hitchcock_meaning": "antiquity; old age",
        "source_ids": {"easton": "kedemoth", "smith": "kedemoth", "isbe": "kedemoth"},
        "key_refs": ["Deuteronomy 2:26", "Joshua 13:18", "Joshua 21:37"]
    },
    "kedesh": {
        "id": "kedesh",
        "term": "Kedesh",
        "category": "places",
        "intro": "<p>Kedesh (meaning <em>sanctuary</em> or <em>holy place</em>) was the name of several distinct cities in ancient Israel. The most significant was Kedesh in Naphtali (also called Kedesh-naphtali), a fortified city in the upper Galilee region that served as one of the six cities of refuge—the nearest refuge for a manslayer fleeing from the region north of the Jordan. It was the home of Barak son of Abinoam, the military commander whom Deborah summoned to fight against Sisera's forces, and it was in Kedesh that Barak mustered the ten thousand warriors of Naphtali and Zebulun for the battle of Kishon (Judges 4:6–10).</p><p>Kedesh was also a Levitical city assigned to the Gershonite Levites (Joshua 21:32; 1 Chronicles 6:76). Tiglath-pileser III of Assyria captured Kedesh during his campaign against the northern kingdom circa 733 BC (2 Kings 15:29), deporting its population as part of the systematic dismantling of Israel. A second Kedesh lay in the extreme south of Judah (Joshua 15:23), and a third in Issachar (1 Chronicles 6:72). The northern Kedesh is identified with Tell Qades, near the modern Israeli-Lebanese border.</p>",
        "sections": [],
        "hitchcock_meaning": "holiness; sanctuary",
        "source_ids": {"easton": "kedesh", "smith": "kedesh", "isbe": "kedesh"},
        "key_refs": ["Joshua 20:7", "Joshua 21:32", "Judges 4:6", "2 Kings 15:29"]
    },
    "kedron": {
        "id": "kedron",
        "term": "Kedron",
        "category": "places",
        "intro": "<p>Kedron (a variant spelling of Kidron) was the valley running between the eastern wall of Jerusalem and the Mount of Olives, mentioned in John 18:1 as the brook which Jesus crossed with his disciples on the way to Gethsemane. The name means <em>turbid</em> or <em>dark</em>, reflecting the seasonal stream's character—dry in summer but flowing dark and murky after winter rains. In the Fourth Gospel, John uses the Cedron/Kedron spelling, which may reflect the Greek form of the Hebrew Kidron.</p><p>The crossing of this valley in the final night of Jesus's life was laden with symbolic resonance: David had crossed the Kidron weeping during Absalom's rebellion (2 Samuel 15:23), and the valley had served as the eastern boundary of Jerusalem's sacred precincts, beyond which idolatrous objects were thrown and burned by reforming kings. Jesus's crossing of Kedron to the garden where Judas knew to find him echoed David's flight while also moving toward the fulfillment of what David's psalms had foreshadowed regarding betrayal and suffering.</p>",
        "sections": [],
        "hitchcock_meaning": "obscure; making black or sad",
        "source_ids": {"easton": "kedron", "smith": "kedron", "isbe": "kidron"},
        "key_refs": ["John 18:1", "2 Samuel 15:23", "1 Kings 2:37"]
    },
    "kehelathah": {
        "id": "kehelathah",
        "term": "Kehelathah",
        "category": "places",
        "intro": "<p>Kehelathah (meaning <em>assembly</em> or <em>a convocation</em>) was one of the stations of the Israelites during their forty years of wilderness wandering, listed in Numbers 33:22–23 between Rissah and Mount Shepher. It was one of approximately forty named stopping points in the wilderness itinerary of Numbers 33, recording Israel's journey from Egypt to the plains of Moab.</p><p>The location of Kehelathah is entirely unknown and has not been identified by archaeology or geography. Many of the wilderness stations in Numbers 33 remain unlocatable, as the specific route Israel took through the Sinai peninsula cannot be reconstructed with certainty. Kehelathah's name, suggesting a gathering or assembly place, may indicate a location where the entire Israelite community converged after marching in smaller groups—perhaps a natural water source or broad valley that could accommodate the large company. It stands as one of the many incidental place-names that preserve the memory of Israel's desert sojourn without providing narrative content beyond the bare fact of encampment.</p>",
        "sections": [],
        "hitchcock_meaning": "assembly; congregation",
        "source_ids": {"easton": "kehelathah", "smith": "kehelathah", "isbe": "kehelathah"},
        "key_refs": ["Numbers 33:22", "Numbers 33:23"]
    },
    "keilah": {
        "id": "keilah",
        "term": "Keilah",
        "category": "places",
        "intro": "<p>Keilah (meaning <em>citadel</em> or <em>fortress</em>) was a city in the Shephelah lowlands of Judah, listed in Joshua 15:44. It gained prominence in the narrative of David's outlaw period: when the Philistines were raiding the threshing floors of Keilah, David inquired of God and received permission to attack and relieve the city, rescuing it despite his men's reluctance. David successfully drove off the Philistines, saving Keilah and taking their livestock as spoil.</p><p>The rescue proved a double test of loyalty: Saul immediately marched to besiege the city to capture David, and David inquired of God again, learning that the men of Keilah—the very people he had saved—would hand him over to Saul to save themselves. David and his six hundred men departed before Saul arrived. This episode illustrated both David's generosity toward those outside his immediate following and the cold calculus of political loyalty in a city that owed him its survival. Keilah is generally identified with Khirbet Qila in the Judean foothills southwest of Bethlehem.</p>",
        "sections": [],
        "hitchcock_meaning": "she that divides or cuts",
        "source_ids": {"easton": "keilah", "smith": "keilah", "isbe": "keilah"},
        "key_refs": ["Joshua 15:44", "1 Samuel 23:1", "1 Samuel 23:5", "1 Samuel 23:12"]
    },
    "kelita": {
        "id": "kelita",
        "term": "Kelita",
        "category": "people",
        "intro": "<p>Kelita (meaning <em>dwarf</em> or possibly <em>gathered</em>) was a Levite who assisted Ezra in the public reading and exposition of the Law to the assembled people in Jerusalem after the return from Babylonian exile. Nehemiah 8:7 lists him among the thirteen Levites who stood on the platform with Ezra, helping the people understand the Torah that was being read—explaining its meaning and giving the sense so that the hearers could comprehend what was being read. He is also known by the name Kelaiah.</p><p>Kelita appears again in Nehemiah 10:10 as one of the Levites who set their seal to the solemn covenant renewal that followed Ezra's reading of the Law and the great assembly of repentance. His role in both the didactic and covenantal aspects of the post-exilic religious revival places him among the core group of Levitical teachers who made the Torah accessible to the restored community. The Levites' teaching function described in Nehemiah 8 is one of the most vivid pictures in the Old Testament of corporate scripture education.</p>",
        "sections": [],
        "hitchcock_meaning": "dwarf; curtailed",
        "source_ids": {"easton": "kelita", "smith": "kelita", "isbe": "kelita"},
        "key_refs": ["Nehemiah 8:7", "Nehemiah 10:10"]
    },
    "kemuel": {
        "id": "kemuel",
        "term": "Kemuel",
        "category": "people",
        "intro": "<p>Kemuel (meaning <em>helper of God</em> or <em>assembly of God</em>) is the name of three distinct figures in the Old Testament. The most genealogically significant was the third son of Nahor, Abraham's brother, by his wife Milcah (Genesis 22:21). Through his son Aram, Kemuel became the ancestor of the Aramean peoples—making him the Nahorite parallel to Abraham's Israelite lineage, with both families playing prominent roles in the patriarchal narratives.</p><p>A second Kemuel was the son of Shiphtan from the tribe of Ephraim, appointed as one of the twelve leaders who assisted in dividing the land of Canaan among the tribes (Numbers 34:24). A third Kemuel was the father of Hashabiah, the Levitical overseer of the tribe of Levi in David's administrative organization (1 Chronicles 27:17). The name's theological meaning—<em>God raises up</em> or <em>God assembles</em>—reflects the Hebrew naming convention of expressing faith in divine action, and its occurrence in three different tribal contexts suggests it was a widely used name in ancient Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "God hath raised up; or the congregation of God",
        "source_ids": {"easton": "kemuel", "smith": "kemuel", "isbe": "kemuel"},
        "key_refs": ["Genesis 22:21", "Numbers 34:24", "1 Chronicles 27:17"]
    },
    "kenath": {
        "id": "kenath",
        "term": "Kenath",
        "category": "places",
        "intro": "<p>Kenath (meaning <em>possession</em>) was a city of Gilead or Bashan in the Transjordanian highlands, captured by Nobah of the tribe of Manasseh who renamed it Nobah after himself (Numbers 32:42). The renaming proved impermanent—it continued to be known by its original name in later tradition. The city is mentioned alongside Beeshterah and other Bashan settlements in the records of Manassite expansion east of the Jordan.</p><p>Kenath is identified with Qanawat (ancient Canatha) in the region of the Hauran in modern Syria, a site where substantial Roman-era ruins survive. The Decapolis city of Canatha lay in the same region, and the connection between ancient Kenath and this later settlement is generally accepted. In 1 Chronicles 2:23, Kenath and its daughter-villages are said to have been taken from Manasseh by Geshur and Aram—a reversal of the earlier Israelite conquest suggesting the city changed hands multiple times as regional powers competed for control of the fertile Hauran plateau.</p>",
        "sections": [],
        "hitchcock_meaning": "possession; purchase",
        "source_ids": {"easton": "kenath", "smith": "kenath", "isbe": "kenath"},
        "key_refs": ["Numbers 32:42", "1 Chronicles 2:23"]
    },
    "kenaz": {
        "id": "kenaz",
        "term": "Kenaz",
        "category": "people",
        "intro": "<p>Kenaz (meaning <em>this purchase</em> or <em>hunter</em>) was the name of several figures in the Old Testament. The most historically significant was a son of Eliphaz and grandson of Esau, who became one of the chiefs of Edom (Genesis 36:11, 15, 42). From this Kenaz descended the Kenizzites, a people associated with the southern regions of Canaan and later absorbed into the tribe of Judah. The Kenizzite connection is significant because both Caleb and Othniel, prominent figures in the conquest period, are identified as Kenizzites who became fully integrated into the tribe of Judah.</p><p>Othniel son of Kenaz was the first judge of Israel, delivering the nation from the oppression of Cushan-rishathaim king of Mesopotamia (Judges 3:9–11). He was the younger brother of Caleb (or Caleb's nephew, depending on how the genealogical language is construed), and his exploits included capturing Kiriath-sepher and winning Achsah, Caleb's daughter, as his wife. A third Kenaz was a grandson of Caleb through his son Elah (1 Chronicles 4:15). The Kenaz lineage thus produced two of Israel's greatest early leaders and represents one of the most successful examples of non-Israelite integration into the covenant people.</p>",
        "sections": [],
        "hitchcock_meaning": "this purchase; this lamentation",
        "source_ids": {"easton": "kenaz", "smith": "kenaz", "isbe": "kenaz"},
        "key_refs": ["Genesis 36:11", "Numbers 32:12", "Joshua 15:17", "Judges 3:9"]
    },
    "kenites": {
        "id": "kenites",
        "term": "Kenites",
        "category": "people",
        "intro": "<p>The Kenites (meaning <em>smiths</em> or <em>metalworkers</em>) were a nomadic tribe of metalworkers who inhabited the desert regions between Canaan and the Sinai peninsula. Moses's father-in-law Jethro (also called Reuel and Hobab) was a Kenite, and his family joined Israel during the wilderness period, providing invaluable expertise in desert navigation. The close relationship between Israel and the Kenites continued through the period of the Judges and into the monarchy.</p><p>Jael, the wife of Heber the Kenite, achieved fame by killing the Canaanite general Sisera in her tent after the battle of Kishon (Judges 4–5). The Kenites who settled near Arad in the Negev maintained friendly relations with both Israel and the surrounding peoples. Saul warned the Kenites to separate themselves from the Amalekites before he attacked the latter, in recognition of their kindness to Israel during the Exodus (1 Samuel 15:6). The Rechabites, that distinctively ascetic community of vine-abstaining tent-dwellers who appear in Jeremiah 35, were Kenites according to 1 Chronicles 2:55—preserving their nomadic identity well into the late monarchic period.</p>",
        "sections": [],
        "hitchcock_meaning": "possession; purchase",
        "source_ids": {"easton": "kenites", "isbe": "kenites"},
        "key_refs": ["Judges 1:16", "Judges 4:17", "1 Samuel 15:6", "1 Chronicles 2:55"]
    },
    "kenizzite": {
        "id": "kenizzite",
        "term": "Kenizzite",
        "category": "people",
        "intro": "<p>The Kenizzites were a people descended from Kenaz son of Eliphaz, grandson of Esau, whose territory was included in the land promised to Abraham in Genesis 15:19 alongside the Kadmonites and Kenites. They inhabited the region south and southeast of Canaan—the fringes of Edomite territory that bordered the Negev and Judean wilderness. The Kenizzites were ultimately absorbed into the tribe of Judah, with the Calebite and Othnielite families providing the clearest evidence of this integration.</p><p>Caleb son of Jephunneh is identified as a Kenizzite in Numbers 32:12 and Joshua 14:6, 14, yet he is fully incorporated into the tribe of Judah as prince and spy. Othniel son of Kenaz, the first judge, similarly represents Kenizzite lineage serving at the heart of Israelite leadership. The Kenizzite absorption into Judah illustrates the broader pattern in the Conquest narratives whereby non-Israelite peoples who aligned with Israel's covenant purpose were incorporated rather than destroyed—foreshadowing the New Testament theme of Gentile inclusion in the covenant people of God.</p>",
        "sections": [],
        "hitchcock_meaning": "possession of Kenaz",
        "source_ids": {"easton": "kenizzite", "smith": "kenizzite", "isbe": "kenizzite"},
        "key_refs": ["Genesis 15:19", "Numbers 32:12", "Joshua 14:6"]
    },
    "kerchief": {
        "id": "kerchief",
        "term": "Kerchief",
        "category": "concepts",
        "intro": "<p>Kerchief appears only in Ezekiel 13:18 and 13:21 (KJV) as an article associated with the false prophetesses of Israel—women who <em>sew kerchiefs upon all arm-holes</em> (mispads upon all joints of the hand) in connection with their divination practices. The Hebrew term <em>kĕsātôt</em> (rendered kerchiefs or magic bands) refers to some form of cloth binding or covering used in the sorcerous rites these women practiced, possibly worn by clients seeking oracles or used to bind the wrists and hands during prophetic performance.</p><p>The precise nature of these garments and their function in the divinatory ritual is unclear; they may have been bands placed on the arms of those seeking oracles, or coverings placed over the head during trance states. God's condemnation through Ezekiel was that these false prophetesses were ensnaring souls for hire, pronouncing life and death at their own discretion rather than speaking the word of the LORD. The tearing off of these kerchiefs in Ezekiel 13:21 symbolizes the invalidation of their prophetic pretensions—God himself would deliver his people from their manipulation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kerchief", "isbe": "kerchief"},
        "key_refs": ["Ezekiel 13:18", "Ezekiel 13:21"]
    },
    "keren-happuch": {
        "id": "keren-happuch",
        "term": "Keren-happuch",
        "category": "people",
        "intro": "<p>Keren-happuch (meaning <em>horn of eye-paint</em> or <em>cosmetic box</em>) was the name of Job's third daughter, born after his restoration to prosperity following his ordeal of suffering. Along with her sisters Jemimah and Keziah, she is specifically mentioned by name at the conclusion of the book of Job (42:14), and the text notes that there were no women as beautiful as Job's daughters in all the land. Job gave them an inheritance among their brothers—an unusual provision in a patriarchal society, indicating their honored status.</p><p>The naming of the three daughters—Jemimah (dove), Keziah (cassia), and Keren-happuch (cosmetic horn)—with names evoking beauty and fragrance reflects the aesthetic restoration of Job's household after his suffering. In contrast to the beginning of the book where Job's seven sons and three daughters are listed without names, the restored daughters are named individually, suggesting that what was lost and restored was not merely numerical equivalence but the vivid particularity of persons and relationships. The beauty of these daughters, noted with unusual emphasis, functions as a final emblem of Job's complete restoration.</p>",
        "sections": [],
        "hitchcock_meaning": "the horn or child of beauty",
        "source_ids": {"easton": "keren-happuch", "isbe": "keren-happuch"},
        "key_refs": ["Job 42:14", "Job 42:15"]
    },
    "kerioth": {
        "id": "kerioth",
        "term": "Kerioth",
        "category": "places",
        "intro": "<p>Kerioth (meaning <em>cities</em> or <em>the callings</em>) refers to two or possibly three distinct biblical locations. The most historically significant is Kerioth-hezron in the south of Judah (Joshua 15:25), believed by many commentators to be the birthplace of Judas Iscariot—the name Iscariot (<em>Ish-Kerioth</em>) possibly meaning <em>man of Kerioth</em>. If this etymology is correct, Judas was from a Judean town rather than from Galilee, making him a geographic outsider within the predominantly Galilean disciples.</p><p>A second Kerioth was a city of Moab, mentioned in Jeremiah 48:24, 41 and Amos 2:2 in oracles of judgment. Amos 2:2 threatens that fire will devour the palaces of Kerioth and Moab will die in tumult, suggesting it was a major Moabite city. The Moabite Stone (Mesha Stele) mentions Kerioth as the seat of a significant sanctuary, possibly of the god Chemosh, indicating its religious centrality in Moab. This Moabite Kerioth is tentatively identified with el-Qreiyat south of the Arnon River in modern Jordan.</p>",
        "sections": [],
        "hitchcock_meaning": "the cities; the callings",
        "source_ids": {"easton": "kerioth", "smith": "kerioth", "isbe": "kerioth"},
        "key_refs": ["Joshua 15:25", "Amos 2:2", "Jeremiah 48:24"]
    },
    "kesitah": {
        "id": "kesitah",
        "term": "Kesitah",
        "category": "concepts",
        "intro": "<p>Kesitah (Hebrew <em>qĕśîṭâ</em>) was an ancient unit of monetary value mentioned three times in the Old Testament—Genesis 33:19, Joshua 24:32, and Job 42:11. The term is of uncertain meaning and has been translated variously as a piece of money, a piece of silver, a lamb, or a unit of exchange. The Septuagint renders it as <em>amnos</em> (lamb) in Genesis, suggesting a connection to livestock values, while the Vulgate gives <em>agnus</em> (lamb) as well—indicating the ancient translators understood it as a lamb-equivalent unit of exchange.</p><p>In each of its three occurrences, the kesitah appears as a unit of commercial transaction: Jacob paid one hundred kesitahs for the plot of ground at Shechem where he pitched his tent; Joshua buried Joseph's bones on this same purchased ground; and Job's comforters each brought him a gold ring and one kesitah after his restoration. The kesitah may represent a pre-coinage form of commodity money, where livestock or a standardized weight of precious metal served as the unit of exchange. Its archaic nature and limited occurrences suggest it was an early monetary form that fell out of common use as weighed silver replaced it.</p>",
        "sections": [],
        "hitchcock_meaning": "a certain weight or sum of money",
        "source_ids": {"easton": "kesitah", "isbe": "kesitah"},
        "key_refs": ["Genesis 33:19", "Joshua 24:32", "Job 42:11"]
    },
    "kettle": {
        "id": "kettle",
        "term": "Kettle",
        "category": "concepts",
        "intro": "<p>The kettle (Hebrew <em>dûd</em>, meaning <em>boiling</em> or <em>basket</em>) was a large pot used for cooking, mentioned in the Old Testament in several contexts. The same Hebrew word is rendered variously as pot, basket, caldron, and kettle depending on the context: it appears as a cooking vessel for meat (1 Samuel 2:14), as a basket for figs (Jeremiah 24:2), and metaphorically as the <em>seething pot</em> in Job 41:20 describing the breath of Leviathan.</p><p>The prophet Samuel's context is particularly illuminating: the sons of Eli's priests sent a servant with a three-pronged fork to thrust into the kettle, pan, or caldron where the sacrificial meat was boiling, taking whatever the fork brought up as the priest's portion—a practice the text condemns as violation of the proper priestly dues. In Micah 3:3, the prophetic condemnation of corrupt leaders is expressed in terms of butchers: they chop my people in pieces like meat into the kettle. The kettle thus functioned as both an ordinary household and temple cooking vessel and a vivid metaphor for exploitation and judgment in prophetic rhetoric.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kettle", "smith": "kettle", "isbe": "kettle"},
        "key_refs": ["1 Samuel 2:14", "Job 41:20", "Micah 3:3"]
    },
    "keturah": {
        "id": "keturah",
        "term": "Keturah",
        "category": "people",
        "intro": "<p>Keturah (meaning <em>incense</em> or <em>she who makes fragrant smoke</em>) was the wife Abraham married after Sarah's death, by whom he had six sons: Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah. She is described as Abraham's wife in Genesis 25:1 and as his concubine in 1 Chronicles 1:32, a difference that may reflect her subordinate legal status relative to Sarah or a later tradition distinguishing her from Abraham's primary wife.</p><p>Through her sons Abraham became the ancestor of numerous Arabian and Midianite peoples. Midian, her fourth son, became the ancestor of the Midianites—the tribe of Moses's father-in-law and the nation that later oppressed Israel in Gideon's time. Jokshan's son Sheba gave his name to the Sabaean people of southern Arabia, from whom the Queen of Sheba came. Abraham gave gifts to all his sons by Keturah and sent them east, away from Isaac, to whom he gave everything he had (Genesis 25:5–6). Keturah's sons thus represent the broader Semitic family radiating outward from the Abrahamic center, with Isaac as the chosen line of promise.</p>",
        "sections": [],
        "hitchcock_meaning": "that makes the incense to fume",
        "source_ids": {"easton": "keturah", "smith": "keturah", "isbe": "keturah"},
        "key_refs": ["Genesis 25:1", "Genesis 25:4", "Genesis 25:6", "1 Chronicles 1:32"]
    },
    "key": {
        "id": "key",
        "term": "Key",
        "category": "concepts",
        "intro": "<p>The key in the biblical world was both a practical instrument for opening doors and locks and a powerful symbol of authority, access, and delegated power. Ancient keys in Palestine were typically made of wood, with pegs corresponding to bolt holes, and could be quite large—so large that they were carried on the shoulder, which gives force to Isaiah 22:22's promise to Eliakim: <em>I will place on his shoulder the key of the house of David</em>. This passage became paradigmatic for the biblical theology of the key as symbol of royal stewardship.</p><p>Jesus's promise to Peter in Matthew 16:19—<em>I will give you the keys of the kingdom of heaven</em>—draws on this Isaianic background, granting Peter representative authority in the church's governance. Revelation 1:18 presents the risen Christ holding <em>the keys of death and of Hades</em>, symbolizing his resurrection power over the ultimate boundaries. In Revelation 3:7 Christ is described as <em>the holy one, the true one, who has the key of David, who opens and no one will shut, who shuts and no one opens</em>—a direct echo of Isaiah 22:22, completing the typological arc from Eliakim as royal steward to Christ as the ultimate key-holder of God's household.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "key", "smith": "key", "isbe": "key"},
        "key_refs": ["Isaiah 22:22", "Matthew 16:19", "Revelation 1:18", "Revelation 3:7"]
    },
    "kezia": {
        "id": "kezia",
        "term": "Kezia",
        "category": "people",
        "intro": "<p>Kezia (meaning <em>cassia</em>, a fragrant spice bark) was the second of the three daughters born to Job after his restoration from affliction. Along with Jemimah (dove) and Keren-happuch (cosmetic horn), she is listed by name in Job 42:14 as one of the three most beautiful women in the land. Like her sisters, she received an inheritance from her father alongside her brothers—a notable departure from the norm of male-only inheritance that echoes the precedent set by the daughters of Zelophehad.</p><p>The naming of Kezia after cassia, a sweet-smelling spice derived from the bark of a tree related to cinnamon, fits the aesthetic and aromatic quality of her sisters' names. Cassia was used in the holy anointing oil (Exodus 30:24), in temple incense, and as a luxury import—its use as a name suggests sweetness, value, and beauty. The Book of Job's careful naming of the restored daughters (in contrast to the unnamed children at the story's beginning) signals that Job's restoration involved not generic replacement but the vivid particular gift of these three individuals.</p>",
        "sections": [],
        "hitchcock_meaning": "superficies; the angles",
        "source_ids": {"easton": "kezia", "smith": "kezia", "isbe": "kezia"},
        "key_refs": ["Job 42:14", "Job 42:15"]
    },
    "keziz": {
        "id": "keziz",
        "term": "Keziz",
        "category": "places",
        "intro": "<p>Keziz (or Emek-keziz, meaning <em>abrupt</em> or <em>cut off</em>) was a city in the tribal territory of Benjamin, listed in Joshua 18:21 among the towns of Benjamin's allotment in the first district nearest the Jordan. The name suggests a topographical feature—perhaps a steeply cut valley or a place defined by a sharp declivity or ravine in the landscape.</p><p>The city is mentioned only in this boundary and city list and receives no further treatment in the biblical narrative, making its precise location unknown. Benjamin's territory in the central hill country between Judah and Ephraim included several towns whose names are preserved only in Joshua's lists without subsequent historical development. The recovery of these names from the land allotments reflects the Joshua compiler's concern to document the legal tribal inheritances even for settlements that played no further role in the narrated history of Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "end; extremity",
        "source_ids": {"easton": "keziz", "smith": "keziz", "isbe": "keziz"},
        "key_refs": ["Joshua 18:21"]
    },
    "kibroth-hattaavah": {
        "id": "kibroth-hattaavah",
        "term": "Kibroth-hattaavah",
        "category": "places",
        "intro": "<p>Kibroth-hattaavah (meaning <em>the graves of craving</em> or <em>the graves of lust</em>) was an Israelite encampment in the Sinai wilderness named to commemorate a divine judgment. Numbers 11 records that when the mixed multitude and Israelites craved meat and complained against the manna, God sent an abundance of quail—but while the people were still eating, divine anger was kindled and he struck down many of them with a severe plague. They buried those who had craved meat at this site and named it accordingly.</p><p>The episode represents a paradigmatic case of what the Psalms call testing God in the wilderness (Psalm 78:18–31; 106:14). Israel's craving for the foods of Egypt—the fish, cucumbers, melons, leeks, onions, and garlic they remembered so fondly—expressed a deeper rejection of both the manna as divine provision and the desert journey toward the promised land. Paul cites this event in 1 Corinthians 10:6 as a warning against craving evil things, making Kibroth-hattaavah a typological warning for the church. The place-name itself functions as a monument to the spiritual danger of letting appetite override gratitude.</p>",
        "sections": [],
        "hitchcock_meaning": "the graves of lust",
        "source_ids": {"easton": "kibroth-hattaavah", "isbe": "kibroth-hattaavah"},
        "key_refs": ["Numbers 11:34", "Numbers 33:16", "Psalm 78:31", "1 Corinthians 10:6"]
    },
    "kibzaim": {
        "id": "kibzaim",
        "term": "Kibzaim",
        "category": "places",
        "intro": "<p>Kibzaim (meaning <em>two heaps</em>) was a city in the territory of Ephraim assigned to the Kohathite Levites, listed in Joshua 21:22. It is identified with Jokmeam of 1 Chronicles 6:68, where the same Levitical assignment is recorded under an alternative form of the name. The dual form of the name may reflect an ancient double-village or a settlement spread across two hills.</p><p>Kibzaim's location in Ephraim placed it in the central highlands, and its Levitical designation made it one of the teaching and pastoral centers for Ephraim's tribal territory. The Kohathites, who were responsible for carrying the sacred furniture of the tabernacle during the wilderness period, received cities spread throughout Judah, Simeon, Benjamin, Ephraim, Dan, and the half-tribe of Manasseh—a geographic distribution ensuring Levitical presence throughout the settled land. Kibzaim's precise location in Ephraim has not been positively identified by modern archaeology.</p>",
        "sections": [],
        "hitchcock_meaning": "congregation; double gathering",
        "source_ids": {"easton": "kibzaim", "smith": "kibzaim", "isbe": "kibzaim"},
        "key_refs": ["Joshua 21:22", "1 Chronicles 6:68"]
    },
    "kid": {
        "id": "kid",
        "term": "Kid",
        "category": "concepts",
        "intro": "<p>The kid (the young of the goat) was one of the most common food animals in ancient Israel, used widely in meals of celebration and hospitality. Abraham served a kid prepared with milk to the three divine visitors at Mamre (Genesis 18:8, where the calf and meal were accompanied by curds and milk); Rebekah prepared two kids for Isaac to carry out Jacob's deception of the birthright blessing; and Samson brought a kid as a gift when visiting his Philistine wife at Timnah.</p><p>The Mosaic law's thrice-repeated prohibition, <em>You shall not boil a young goat in its mother's milk</em> (Exodus 23:19; 34:26; Deuteronomy 14:21), became the foundational text for the rabbinic laws of kashrut separating meat and dairy. The kid was also used in sacrificial contexts: the red heifer ceremony, Passover preparations, and various guilt offerings could involve goats. The prodigal son's older brother notes bitterly that he was never given even a kid for a celebration with his friends (Luke 15:29), underscoring the modest cost of such hospitality and thus the generosity of the father's feast for the returning prodigal.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kid", "smith": "kid", "isbe": "kid"},
        "key_refs": ["Genesis 27:9", "Exodus 23:19", "Judges 14:6", "Luke 15:29"]
    },
    "kidron": {
        "id": "kidron",
        "term": "Kidron",
        "category": "places",
        "intro": "<p>The Kidron (meaning <em>turbid</em> or <em>dark stream</em>) was the valley and seasonal brook running along the eastern side of Jerusalem between the city wall and the Mount of Olives, draining southward toward the Dead Sea. In summer it was dry; after winter rains it ran with dark, muddy water. The valley served as the eastern boundary of the sacred precincts of ancient Jerusalem, and crossing it carried symbolic weight in the biblical narrative.</p><p>Several defining moments of Israelite and Jewish history occurred at the Kidron: King David crossed it weeping during Absalom's rebellion; Shimei's crossing of it cost him his life by Asolomon's order; reforming kings Asa, Hezekiah, and Josiah threw the implements of idolatry into the Kidron valley to defile them. On the night of his arrest, Jesus crossed the Kidron with his disciples to go to the Garden of Gethsemane (John 18:1)—a crossing that early Christian interpretation linked typologically to David's weeping flight. The Kidron valley is identified in Jehoshaphat's vision (Joel 3:2, 12) with the eschatological Valley of Judgment.</p>",
        "sections": [],
        "hitchcock_meaning": "obscure; making black or sad",
        "source_ids": {"easton": "kidron", "isbe": "kidron"},
        "key_refs": ["2 Samuel 15:23", "1 Kings 2:37", "John 18:1", "Joel 3:12"]
    },
    "kinah": {
        "id": "kinah",
        "term": "Kinah",
        "category": "places",
        "intro": "<p>Kinah (meaning <em>an elegy</em> or <em>lamentation</em>) was a city in the extreme south of Judah, listed in Joshua 15:22 among the towns in the southernmost district of Judah near the border with Edom. It was located near the Edomite frontier in the arid Negev region, the dry southern highlands where permanent settlement was marginal and population sparse.</p><p>The city's evocative name—derived from the Hebrew word for funeral dirge or lamentation (<em>qînâ</em>)—is unusual as a place name and has prompted speculation about the site's association with mourning customs, perhaps the burial place of a notable individual or the scene of some forgotten tragedy. It is thought by some to have been inhabited by the Kenites (whose name bears a related root), who settled in this region of Judah after accompanying Israel from the wilderness. Kinah appears only in the Joshuanic city list and is not otherwise attested in biblical history, making its precise identification uncertain.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Kenah; lamentation",
        "source_ids": {"easton": "kinah", "isbe": "kinah"},
        "key_refs": ["Joshua 15:22"]
    },
    "kine": {
        "id": "kine",
        "term": "Kine",
        "category": "concepts",
        "intro": "<p>Kine is the archaic plural of <em>cow</em>, used in the King James Version to render the Hebrew <em>pārôt</em> (cows, from <em>pārâ</em>, a fruitful cow). Cattle were central to the agricultural and sacrificial economy of ancient Israel, providing draft power, dairy products, leather, and sacrificial animals. The most famous occurrence of kine in Scripture is Pharaoh's dream in Genesis 41, where seven fat cows (<em>pārôt</em>) were devoured by seven lean cows emerging from the Nile—a vision interpreted by Joseph as seven years of abundance followed by seven years of famine.</p><p>The fat and lean kine of Pharaoh's dream became proverbial images of prosperity and privation throughout Western culture. The image of cows emerging from the Nile reflects the Egyptian agricultural reality: the Nile's annual flooding determined the richness of the harvest, and cattle fattened on the lush riverside vegetation were a natural symbol of abundance. The Israelite context for kine extends from the red heifer of Numbers 19 (used in purification rites) to the nursing cows that miraculously carried the ark directly to Beth-shemesh despite the lowing for their calves (1 Samuel 6:7–12).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kine", "smith": "kine", "isbe": "cattle"},
        "key_refs": ["Genesis 41:2", "Genesis 41:26", "Numbers 19:2", "1 Samuel 6:7"]
    },
    "king": {
        "id": "king",
        "term": "King",
        "category": "concepts",
        "intro": "<p>The king in ancient Israel was the supreme human authority, responsible for military leadership, judicial decisions, and the enforcement of covenant law. The Hebrew <em>melek</em> (king, from a root meaning to reign or counsel) occurs over 2,500 times in the Old Testament, reflecting the centrality of the institution to Israelite political and religious life. Kingship in Israel emerged late—after approximately 350 years of the judges—in response to military pressure from the Philistines and popular demand for a permanent human leader like the surrounding nations.</p><p>The theological tension of Israelite kingship runs through the entire narrative from Judges to the Prophets: God himself was Israel's true king, and the request for a human king was both accommodated and judged as a form of rejection of divine kingship (1 Samuel 8:7). Deuteronomy 17:14–20 established the law of the king, limiting his power and requiring him to copy and read the Torah daily. The failure of most kings to live by these standards is the Deuteronomic History's central critique. The prophetic vision resolved the tension eschatologically: a future Davidic king would rule in perfect justice and peace, a king in whom divine and human kingship would be united—fulfilled in New Testament theology by Jesus, the King of Kings.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "king", "smith": "king", "isbe": "king"},
        "key_refs": ["1 Samuel 8:7", "Deuteronomy 17:15", "Psalm 2:6", "Revelation 19:16"]
    },
    "kingdom-of-god": {
        "id": "kingdom-of-god",
        "term": "Kingdom of God",
        "category": "concepts",
        "intro": "<p>The Kingdom of God (also called the Kingdom of Heaven in Matthew, following Jewish reverence for the divine name) is the central theme of Jesus's proclamation and one of the most theologically rich concepts in the New Testament. In its most basic sense it denotes the reign or sovereignty of God—not a geographical territory but a dynamic rule exercised over those who submit to God's authority. The Kingdom is both present and future: present in Jesus's ministry (<em>the kingdom of God has come upon you</em>, Matthew 12:28; Luke 11:20) and yet awaiting a future consummation in glory.</p><p>Jesus's parables of the kingdom (Matthew 13) explore its mysterious growth from small beginnings (mustard seed, leaven), its mixed character in the present age (wheat and tares), its supreme value (hidden treasure, pearl of great price), and its final sorting (dragnet). The Sermon on the Mount describes the character of those who belong to the kingdom (the Beatitudes). Paul declares it to be not eating and drinking but righteousness, peace, and joy in the Holy Spirit (Romans 14:17). The prayer Jesus taught his disciples—<em>Thy kingdom come, thy will be done</em>—places kingdom longing at the heart of Christian spirituality, orienting the community toward its arrival while living in its present reality.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kingdom-of-god", "isbe": "kingdom-of-god"},
        "key_refs": ["Matthew 6:10", "Matthew 13:31", "Luke 17:21", "Romans 14:17"]
    },
    "kingly-office-of-christ": {
        "id": "kingly-office-of-christ",
        "term": "Kingly Office of Christ",
        "category": "concepts",
        "intro": "<p>The kingly office of Christ is one of the three munus (offices) of Christ—prophet, priest, and king—a threefold classification developed in Reformed theology to systematize the work of the Messiah. The anointing of prophets, priests, and kings in the Old Testament was understood as a typological prefiguring of the one Messiah (<em>anointed one</em>) who would fulfill all three roles. Christ's kingly office refers to his exercise of sovereign authority over the universe, his church, and his enemies.</p><p>Scripture describes Christ's kingship in several dimensions: the eternal, divine reign he shares with the Father; the mediatorial kingship given to the incarnate Son (Psalm 2; Matthew 28:18, <em>all authority in heaven and on earth has been given to me</em>); and the eschatological consummation when he delivers the kingdom to the Father after defeating all enemies including death (1 Corinthians 15:24–28). The present exercise of his reign takes place primarily through the gospel and the Holy Spirit, and the church is the outpost of his kingdom in the world. The confession <em>Jesus is Lord</em> (Romans 10:9; 1 Corinthians 12:3) is fundamentally a declaration of his kingly authority over the believer's life.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kingly-office-of-christ", "isbe": "offices-of-christ"},
        "key_refs": ["Psalm 2:6", "Matthew 28:18", "1 Corinthians 15:25", "Revelation 17:14"]
    },
    "kings-the-books-of": {
        "id": "kings-the-books-of",
        "term": "Kings, The Books of",
        "category": "concepts",
        "intro": "<p>The Books of Kings (originally a single book in the Hebrew canon, divided into 1 and 2 Kings in the Septuagint) cover the history of the Israelite monarchy from the last days of David through the fall of Jerusalem to Babylon in 586 BC and the subsequent release of Jehoiachin from Babylonian prison in 562 BC. Together with Samuel and the book of Judges, they form the Deuteronomistic History—a sustained theological interpretation of Israel's monarchic period through the lens of Deuteronomy's covenant theology.</p><p>The evaluative formula applied to each king—whether he did right or evil in the eyes of the LORD, and whether he maintained or abolished the high places—reveals the theological framework: covenant faithfulness to the LORD alone, centralized at the Jerusalem temple, is the standard against which every king is measured. The northern kingdom's kings are uniformly condemned for following the sin of Jeroboam; the southern kings are mixed, with eight receiving positive evaluations and twelve negative. The books were probably compiled in their present form during the Babylonian exile, and their concluding note about Jehoiachin's release suggests a moment of faint hope amid the catastrophe of exile—a hint that God's covenant with David was not entirely extinguished.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kings-the-books-of", "isbe": "kings-books-of"},
        "key_refs": ["1 Kings 11:6", "2 Kings 17:18", "2 Kings 25:27"]
    },
    "kings-dale": {
        "id": "kings-dale",
        "term": "King's Dale",
        "category": "places",
        "intro": "<p>The King's Dale (also known as the King's Valley) is mentioned twice in Scripture. In Genesis 14:17, after Abraham's defeat of the four kings, the king of Sodom came out to meet him in the King's Valley—the same location where Melchizedek king of Salem blessed Abraham and was given a tithe. The name suggests it was a valley associated with royal meetings or ceremonial gatherings, possibly near Jerusalem.</p><p>The second reference is in 2 Samuel 18:18, where Absalom during his lifetime had erected for himself a pillar in the King's Valley, saying he had no son to keep his memory alive—a poignant note given that his sons are mentioned elsewhere and the text may reflect a moment of insecurity about his legacy. This Absalom's pillar was still known in the narrator's day. Josephus identified the King's Valley with the Kidron valley, and the ancient so-called Tomb of Absalom still standing in the Kidron valley may be a later monument inspired by this tradition, though it dates to the first century BC at earliest.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kings-dale", "isbe": "kings-dale"},
        "key_refs": ["Genesis 14:17", "2 Samuel 18:18"]
    },
    "kinsman": {
        "id": "kinsman",
        "term": "Kinsman",
        "category": "concepts",
        "intro": "<p>The kinsman-redeemer (Hebrew <em>gōʾēl</em>, from a root meaning to redeem or reclaim) was a specific legal institution in Israelite law whereby the nearest male relative had both the right and the obligation to redeem the property, person, or honor of a kinsman in distress. The <em>gōʾēl</em> could purchase back land sold under economic duress (Leviticus 25:25), redeem a kinsman sold into slavery (Leviticus 25:47–49), avenge the blood of a murdered relative, and perform levirate marriage to raise up offspring for a deceased brother (Deuteronomy 25:5–10).</p><p>The Book of Ruth dramatizes the kinsman-redeemer institution through Boaz's redemption of Naomi's land and marriage to Ruth, recovering both the family property and the family line through a deceased kinsman. The anonymous nearer kinsman who declined his redemption right because of the complication of marrying Ruth cleared the way for Boaz. Paul's theology of redemption employs kinsman-redeemer imagery: Christ as the one who became related to humanity through the incarnation in order to exercise the redeemer's right, paying the price to liberate those in bondage to sin and death. The <em>gōʾēl</em> theology thus provides one of the richest Old Testament typological backgrounds for the atonement.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kinsman", "isbe": "goel"},
        "key_refs": ["Leviticus 25:25", "Ruth 3:9", "Ruth 4:4", "Job 19:25"]
    },
    "kir": {
        "id": "kir",
        "term": "Kir",
        "category": "places",
        "intro": "<p>Kir (meaning <em>a city</em>, <em>wall</em>, or <em>meeting</em>) was a region or city to which Tiglath-pileser III of Assyria deported the Syrian (Aramean) population of Damascus after his conquest of that city in 732 BC (2 Kings 16:9; Amos 1:5). The location of Kir is uncertain; it was evidently a distant territory within the Assyrian empire where conquered peoples were resettled to break their national cohesion. Isaiah 22:6 mentions Kir alongside Elam as supplying warriors for the siege of Jerusalem, suggesting it may have been in the region of Media or Elam (modern western Iran).</p><p>Amos 9:7 provides a striking theological use of Kir: God declares he brought the Philistines from Caphtor and the Syrians from Kir, just as he brought Israel from Egypt—asserting divine sovereignty over the migrations of all nations, not Israel alone. This suggests Kir was regarded as the ancient homeland of the Arameans, with their migration from Kir to Damascus being their foundational national story, analogous to Israel's Exodus. The Assyrian deportation of Damascus's population back to Kir thus represented a kind of reverse-Exodus—a poetic justice matching the crime of aggression against Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "a city; wall; meeting",
        "source_ids": {"easton": "kir", "smith": "kir", "isbe": "kir"},
        "key_refs": ["2 Kings 16:9", "Amos 1:5", "Amos 9:7", "Isaiah 22:6"]
    },
    "kir-of-moab": {
        "id": "kir-of-moab",
        "term": "Kir of Moab",
        "category": "places",
        "intro": "<p>Kir of Moab (meaning <em>wall of Moab</em> or <em>city of Moab</em>) was one of the two principal strongholds of Moab—along with Ar of Moab—mentioned in Isaiah 15:1 in the oracle against Moab. The destruction of Kir of Moab in a single night is the opening image of Isaiah's Moab lament, a poem notable for its emotional depth and sympathy for Moab's suffering even while announcing divine judgment. Isaiah 16:7 and Jeremiah 48:31, 36 extend the lament.</p><p>Kir of Moab is generally identified with the modern Kerak (ancient Kir-hareseth), a spectacularly fortified hilltop town approximately seventeen miles south of the Arnon River in modern Jordan. The site sits on a ridge nearly 3,000 feet above sea level, surrounded by deep valleys on three sides, making it one of the most naturally defensible positions in the entire Transjordanian plateau—consistent with its biblical designation as a stronghold. The Crusader castle still standing at Kerak occupies the same strategic hilltop that made it so militarily significant in antiquity.</p>",
        "sections": [],
        "hitchcock_meaning": "city of Moab",
        "source_ids": {"easton": "kir-of-moab", "smith": "kir-of-moab", "isbe": "kir"},
        "key_refs": ["Isaiah 15:1", "Isaiah 16:7", "Jeremiah 48:31"]
    },
    "kir-haraseth": {
        "id": "kir-haraseth",
        "term": "Kir-haraseth",
        "category": "places",
        "intro": "<p>Kir-haraseth (meaning <em>built fortress</em> or possibly <em>city of potsherds</em>) was the chief fortified city of Moab, identified with modern Kerak in Jordan. It appears most dramatically in 2 Kings 3, when the combined forces of Israel, Judah, and Edom besieged the city during the campaign of Joram king of Israel against the Moabite king Mesha. When all seemed lost, Mesha sacrificed his firstborn son on the city wall as a burnt offering to his god Chemosh—an act so horrifying that the attacking coalition withdrew, with a great wrath coming against Israel.</p><p>The theological interpretation of this withdrawal has puzzled commentators: the text simply records that a great indignation (<em>qeṣep gādôl</em>) came against Israel, without specifying its source. Whatever its cause, the siege was lifted and Kir-haraseth remained unconquered. The city's name appears in Isaiah's oracle against Moab (Isaiah 16:7, 11) and in Jeremiah 48:31, 36, where the prophets lament the destruction of this stronghold in terms of genuine pathos for Moab's suffering. The Moabite Stone (Mesha Stele) confirms Mesha as a historical king, though it presents the conflict from his perspective as a victory.</p>",
        "sections": [],
        "hitchcock_meaning": "a city demolished or wall of burnt brick",
        "source_ids": {"easton": "kir-haraseth", "isbe": "kir-haraseth"},
        "key_refs": ["2 Kings 3:25", "2 Kings 3:27", "Isaiah 16:7", "Jeremiah 48:36"]
    },
    "kirjath": {
        "id": "kirjath",
        "term": "Kirjath",
        "category": "places",
        "intro": "<p>Kirjath (meaning <em>city</em> or <em>a city, a vocation, a meeting</em>) was a city belonging to the tribe of Benjamin, listed in Joshua 18:28 among Benjamin's cities. It is generally identified with Kirjath-jearim (city of forests), the famous location where the ark of the covenant rested for twenty years after its return from the Philistines. The abbreviated form Kirjath in Joshua 18:28 is likely the same site as Kirjath-jearim, which stood on the boundary between Judah and Benjamin at a prominent hilltop location controlling the road from the coastal plain to Jerusalem.</p><p>The modern identification is with Abu Ghosh or Tell el-Azhar near the village of Deir el-Azar, approximately nine miles west of Jerusalem on the road to Jaffa. The name Kirjath as a standalone designation reflects the ancient practice of using the generic word for city as a proper noun, perhaps when a particular city was so well known in its region that the full compound name was unnecessary. The same site appears under multiple names in the biblical record, reflecting its importance as a major landmark on the routes into the Judean highlands.</p>",
        "sections": [],
        "hitchcock_meaning": "city; vocation; meeting",
        "source_ids": {"easton": "kirjath", "smith": "kirjath", "isbe": "kirjath"},
        "key_refs": ["Joshua 18:28"]
    },
    "kirjath-arba": {
        "id": "kirjath-arba",
        "term": "Kirjath-arba",
        "category": "places",
        "intro": "<p>Kirjath-arba (meaning <em>city of Arba</em> or <em>city of the four</em>) was the ancient Canaanite name of Hebron, the prominent city in the hill country of Judah where Abraham, Sarah, Isaac, Rebekah, Jacob, and Leah were all buried in the cave of Machpelah. The name derived from Arba, who is described in Joshua 14:15 as <em>the greatest man among the Anakim</em>—one of the giant pre-Israelite inhabitants of Canaan. The site retained its ancient designation alongside the new name Hebron well into the period of the Judges.</p><p>Caleb son of Jephunneh was given Kirjath-arba as his inheritance, and he drove out from it the three sons of Anak: Sheshai, Ahiman, and Talmai (Joshua 15:14; Judges 1:10–11). The city became one of the six cities of refuge in Israel (Joshua 20:7) and was assigned to the Kohathite Levites (Joshua 21:11–13). Kirjath-arba also appears in Nehemiah 11:25 as a resettlement site after the Babylonian exile. The modern city of Hebron, with its patriarchal tomb of Machpelah (now the Ibrahim Mosque/Cave of Machpelah), preserves the memory of this ancient sacred site.</p>",
        "sections": [],
        "hitchcock_meaning": "city of four; fourth city",
        "source_ids": {"easton": "kirjath-arba", "isbe": "kirjath-arba"},
        "key_refs": ["Genesis 23:2", "Joshua 14:15", "Joshua 20:7", "Judges 1:10"]
    },
    "kirjath-huzoth": {
        "id": "kirjath-huzoth",
        "term": "Kirjath-huzoth",
        "category": "places",
        "intro": "<p>Kirjath-huzoth (meaning <em>city of streets</em> or <em>populous city</em>) was a Moabite city where Balak king of Moab took the prophet Balaam after he arrived from Pethor in Mesopotamia, having been summoned to curse Israel. Numbers 22:39 records their journey together to this city, where Balak offered oxen and sheep sacrifices before they proceeded to the high places of Baal to begin the attempted oracles against Israel.</p><p>The city's location in Moab and its role as the first stopping point before the high places suggests it was a significant urban center in the Moabite heartland, perhaps near the northern Moabite plateau. Its identification with a specific modern site is uncertain. The Kirjath-huzoth episode marks the beginning of the Balaam narrative's movement toward its climax: despite Balak's repeated attempts to get Balaam to curse Israel from different vantage points, God turned each oracle into a blessing, culminating in the famous Messianic prophecy of the Star out of Jacob (Numbers 24:17). Kirjath-huzoth thus stands at the threshold of one of the Old Testament's most remarkable prophetic sequences.</p>",
        "sections": [],
        "hitchcock_meaning": "city of streets; populous city",
        "source_ids": {"easton": "kirjath-huzoth", "isbe": "kirjath-huzoth"},
        "key_refs": ["Numbers 22:39", "Numbers 22:41"]
    },
    "kirjath-jearim": {
        "id": "kirjath-jearim",
        "term": "Kirjath-jearim",
        "category": "places",
        "intro": "<p>Kirjath-jearim (meaning <em>city of jaars</em>, forests or thickets) was a Gibeonite town that made a treaty with Joshua and was never conquered (Joshua 9:17). It became most famous as the resting place of the ark of the covenant: after the Philistines returned the ark following the disasters at Ashdod, Gath, and Ekron, it came to Beth-shemesh and then to Kirjath-jearim, where it remained in the house of Abinadab on the hill for twenty years—the entire period from its return until David brought it to Jerusalem (1 Samuel 7:1–2; 2 Samuel 6).</p><p>It was during this period that the ark was under the care of Eleazar son of Abinadab, and in Kirjath-jearim that Samuel began his ministry of calling Israel to repentance (1 Samuel 7:2–6). The city also appears as the birthplace of the prophet Uriah son of Shemaiah, who prophesied during Jehoiakim's reign and was later executed (Jeremiah 26:20–23). The site is identified with Tell el-Azhar/Deir el-Azar on a prominent hill nine miles west of Jerusalem, a location from which the ridge leading toward Jerusalem and the strategic roads of the Judean highlands are visible.</p>",
        "sections": [],
        "hitchcock_meaning": "city of woods",
        "source_ids": {"easton": "kirjath-jearim", "isbe": "kirjath-jearim"},
        "key_refs": ["Joshua 9:17", "1 Samuel 7:1", "2 Samuel 6:2", "Jeremiah 26:20"]
    },
    "kirjath-sannah": {
        "id": "kirjath-sannah",
        "term": "Kirjath-sannah",
        "category": "places",
        "intro": "<p>Kirjath-sannah (meaning <em>city of the palm</em> or <em>city of instruction/teaching</em>) is listed in Joshua 15:49 as a town of Judah in the hill country district, identified as the same site as Kirjath-sepher (<em>city of books</em>) and Debir. The name variation likely reflects either different etymological traditions for the same place or a scribal variant. Debir was a city of the Anakim that Caleb promised as a bride-price to whoever could capture it.</p><p>Othniel son of Kenaz, Caleb's younger brother (or nephew), captured Kirjath-sannah/Debir and won Caleb's daughter Achsah as his wife. Achsah then boldly asked her father for springs of water to go with the land she had received, and Caleb gave her both the upper and lower springs—a vignette that presents the distribution of the conquered land in terms of women's initiative and patriarchal generosity. Debir later became a Levitical city assigned to the Kohathites (Joshua 21:15; 1 Chronicles 6:58). Archaeological excavation of the most likely candidate site, Khirbet Rabud, has revealed Iron Age remains consistent with the biblical period.</p>",
        "sections": [],
        "hitchcock_meaning": "city of enmity; or of a bush; or of a palm tree",
        "source_ids": {"easton": "kirjath-sannah", "isbe": "kirjath-sannah"},
        "key_refs": ["Joshua 15:49", "Joshua 15:15", "Judges 1:12", "Joshua 21:15"]
    },
    "kirjath-sepher": {
        "id": "kirjath-sepher",
        "term": "Kirjath-sepher",
        "category": "places",
        "intro": "<p>Kirjath-sepher (meaning <em>city of books</em> or <em>city of the scribes</em>) was the ancient name of Debir, one of the Anakite cities in the hill country of Judah. The name's literary connotation—a city associated with writing, records, or learning—has intrigued scholars, suggesting it may have housed a scribal school, archive, or treaty documents in the pre-Israelite period. It was one of the major Canaanite cities in the southern highlands that fell to Israel during the conquest.</p><p>Caleb offered his daughter Achsah as a prize to whoever captured Kirjath-sepher (Joshua 15:16; Judges 1:12), and Othniel son of Kenaz took it. The site is identified by most archaeologists with Khirbet Rabud, a prominent mound in the hill country of Judah southwest of Hebron, where remains from the Late Bronze Age and Iron Age have been found. The city later became a Levitical city for the Kohathites. Kirjath-sepher's dual name—city of books in the Canaanite period, Debir in the Israelite—may preserve the memory of its earlier function as a center of scribal activity under the pre-Israelite administration.</p>",
        "sections": [],
        "hitchcock_meaning": "city of letters; or of the book",
        "source_ids": {"easton": "kirjath-sepher", "isbe": "kirjath-sepher"},
        "key_refs": ["Joshua 15:15", "Joshua 15:16", "Judges 1:11", "Judges 1:12"]
    },
    "kirjathaim": {
        "id": "kirjathaim",
        "term": "Kirjathaim",
        "category": "places",
        "intro": "<p>Kirjathaim (meaning <em>two cities</em> or <em>double city</em>) refers to two distinct biblical sites. The first was a city east of the Jordan in the territory allotted to Reuben, mentioned in Numbers 32:37 and Joshua 13:19. It is identified with Khirbet el-Qureiyeh (or Qaryatein) on the Moabite plateau, and appears in Jeremiah 48:1, 23 and Ezekiel 25:9 in prophetic oracles against Moab—apparently having reverted to Moabite control by the time of those prophecies. The Mesha Stele also mentions this city.</p><p>A second Kirjathaim was a city of Naphtali listed in 1 Chronicles 6:76 as assigned to the Gershonite Levites, where it is equated with Kartan of Joshua 21:32. Genesis 14:5 mentions Shaveh-kiriathaim (<em>plain of Kirjathaim</em>) as the location where the eastern coalition kings defeated the Emims during the campaign of Chedorlaomer—a reference to the Moabite site, which was ancient enough by Abraham's time to have already been associated with a named plain. The dual form of the name (<em>-aim</em>) in both Hebrew and Akkadian (qiryatayn) confirms a double settlement at both sites.</p>",
        "sections": [],
        "hitchcock_meaning": "the two cities; callings; or meetings",
        "source_ids": {"easton": "kirjathaim", "isbe": "kirjathaim"},
        "key_refs": ["Genesis 14:5", "Numbers 32:37", "Joshua 13:19", "Jeremiah 48:1"]
    },
    "kish": {
        "id": "kish",
        "term": "Kish",
        "category": "people",
        "intro": "<p>Kish was a Benjaminite, the son of Abiel and father of Saul—thus the paternal grandfather of Israel's first king. He is described as a man of wealth and standing in his tribe (1 Samuel 9:1). The providential occasion of Saul's introduction to Samuel arose from the search for Kish's lost donkeys: Saul and a servant went looking for them throughout the hill country of Ephraim and Benjamin, and when they could not find them, the servant suggested consulting the nearby man of God (Samuel). The lost donkeys became the occasion of Saul's anointing.</p><p>Kish himself plays no further narrative role after establishing the lineage of Saul. The name Kish appears several other times in the Old Testament for unrelated individuals: a Levite of the family of Merari (1 Chronicles 23:21; 24:29), a Levite among the temple purifiers in Hezekiah's time (2 Chronicles 29:12), and most significantly in the book of Esther as the ancestor of Mordecai (Esther 2:5)—a Benjaminite lineage that deliberately parallels Saul's descent from Kish, setting up the thematic contrast between Mordecai's faithfulness and Saul's earlier failure with the Amalekites.</p>",
        "sections": [],
        "hitchcock_meaning": "hard; difficult; straw; for age",
        "source_ids": {"easton": "kish", "smith": "kish", "isbe": "kish"},
        "key_refs": ["1 Samuel 9:1", "1 Samuel 9:3", "2 Samuel 21:14", "Esther 2:5"]
    },
    "kishion": {
        "id": "kishion",
        "term": "Kishion",
        "category": "places",
        "intro": "<p>Kishion (meaning <em>hardness</em> or <em>soreness</em>) was a city in the territory of Issachar assigned to the Gershonite Levites, listed in Joshua 19:20 and 21:28. It is identified with Kedesh of Issachar in 1 Chronicles 6:72, where the same Levitical assignment is recorded under a variant name. The site lay in the fertile territory of Issachar in the lower Galilee and Jezreel Valley region.</p><p>Kishion appears only in these city and boundary lists and receives no narrative treatment in the biblical history. As a Levitical city in one of Israel's most agriculturally productive territories, it served as a center for the Gershonite priests and Levites who were responsible for the outer coverings and screen hangings of the tabernacle during the wilderness period. The territory of Issachar, praised in Jacob's blessing as a strong donkey lying between two burdens willing to yield itself to labor (Genesis 49:14–15), provided the agricultural bounty that sustained the Levites assigned to Kishion.</p>",
        "sections": [],
        "hitchcock_meaning": "hardness; soreness",
        "source_ids": {"easton": "kishion", "smith": "kishion", "isbe": "kishion"},
        "key_refs": ["Joshua 19:20", "Joshua 21:28", "1 Chronicles 6:72"]
    },
    "kishon": {
        "id": "kishon",
        "term": "Kishon",
        "category": "places",
        "intro": "<p>The Kishon (meaning <em>winding</em> or <em>hard</em>) was a seasonal river of central Palestine, rising on the slopes of Mount Tabor and in the hills of Gilboa before flowing northwestward through the Jezreel Valley to drain into the Mediterranean near Haifa at the foot of Mount Carmel. For much of the year a series of pools, it could become a raging torrent in the rainy season when the flat valley floor turned to mud and flooded.</p><p>Two of the most dramatic events in Israel's history unfolded at the Kishon. In Deborah and Barak's battle against Sisera, God threw the Canaanite chariot army into panic—and then the Kishon swept them away, transforming Sisera's greatest military asset (chariots, which required firm ground) into a liability in the flooded plain (Judges 4–5). The Song of Deborah celebrates: <em>The torrent Kishon swept them away, the ancient torrent, the torrent Kishon</em> (Judges 5:21). Centuries later, Elijah executed the 450 prophets of Baal at the Kishon after the fire contest on Mount Carmel (1 Kings 18:40). The Kishon thus became associated with two great divine victories over paganism in Israel's national memory.</p>",
        "sections": [],
        "hitchcock_meaning": "hard; sore",
        "source_ids": {"easton": "kishon", "smith": "kishon", "isbe": "kishon"},
        "key_refs": ["Judges 4:7", "Judges 5:21", "1 Kings 18:40", "Psalm 83:9"]
    },
    "kiss": {
        "id": "kiss",
        "term": "Kiss",
        "category": "concepts",
        "intro": "<p>The kiss in the biblical world carried a range of social and religious meanings quite different from modern Western conventions. Kissing expressed familial affection (Genesis 29:13; Luke 15:20), reconciliation (Genesis 33:4; Luke 15:20 of the father embracing the prodigal), farewell (Ruth 1:14), and reverence or homage—<em>Kiss the Son, lest he be angry</em> (Psalm 2:12) uses the kiss as an act of submission to royal authority. Worshippers kissing the calves of Baal (1 Kings 19:18; Hosea 13:2) represented the act of religious devotion.</p><p>In the New Testament, the <em>holy kiss</em> or <em>kiss of love</em> became a distinctive mark of Christian community, commanded by Paul in Romans 16:16, 1 Corinthians 16:20, 2 Corinthians 13:12, and 1 Thessalonians 5:26, and by Peter in 1 Peter 5:14. This ritual greeting expressed the equality and brotherhood of all believers across social distinctions. Judas's betrayal of Jesus with a kiss (Matthew 26:48–49) made the greeting an instrument of treachery, giving the kiss of Judas its permanent place in the language of betrayal. The woman who anointed Jesus's feet with her tears and kissed them (Luke 7:38, 45) expressed the grateful devotion that Jesus contrasted with his host Simon's withholding of the customary guest kiss.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kiss", "smith": "kiss", "isbe": "kiss"},
        "key_refs": ["Psalm 2:12", "Luke 7:45", "Romans 16:16", "Matthew 26:48"]
    },
    "kite": {
        "id": "kite",
        "term": "Kite",
        "category": "concepts",
        "intro": "<p>The kite was an unclean bird of prey listed among the forbidden foods in Mosaic dietary law (Leviticus 11:14; Deuteronomy 14:13). The Hebrew term <em>dayyâ</em> denotes a keen-sighted bird of the hawk family, and ancient translations have rendered it variously as kite, black kite, or vulture—the broad-winged soaring raptors common over the Palestinian landscape. Its unclean status derived from its carnivorous and scavenging habits, which placed it in the category of blood-consuming predators excluded from Israelite diet.</p><p>Job 28:7 uses the kite's exceptional eyesight as a metaphor for the inaccessibility of wisdom: <em>The path no bird of prey knows, and the kite's eye has not seen it</em>—even the most visually acute creature in the sky cannot discern the way to wisdom, which is God's alone to know and grant. The kite's appearance in both the dietary lists and the wisdom literature reflects its familiarity in the Palestinian sky, where several species of kite and harrier were common year-round residents or seasonal migrants, visible circling high over the hills and valleys of Canaan in their characteristic searching flight.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kite", "smith": "kite", "isbe": "kite"},
        "key_refs": ["Leviticus 11:14", "Deuteronomy 14:13", "Job 28:7"]
    },
    "kithlish": {
        "id": "kithlish",
        "term": "Kithlish",
        "category": "places",
        "intro": "<p>Kithlish (meaning <em>man's wall</em> or <em>it is a wall</em>) was a town in the lowland district of Judah, listed in Joshua 15:40 among the cities in the second group of Shephelah towns. Its location in the Judean foothills placed it in the transitional zone between the coastal plain and the highland core of Judah, a strategically and agriculturally significant region contested between Israel and the Philistines throughout the monarchic period.</p><p>Kithlish is not mentioned elsewhere in the biblical narrative, and its precise location has not been established by archaeology. The Shephelah towns listed with it in Joshua 15—including Lachish, Eglon, Cabbon, Lahmam, and Makkedah—were among the strategically important fortress cities that controlled access to the interior of Judah, and Kithlish presumably served a similar function in its district. Its limited biblical footprint reflects the fate of many secondary towns in the Shephelah that were overshadowed by more prominent neighbors in both historical records and archaeological investigation.</p>",
        "sections": [],
        "hitchcock_meaning": "it is a wall; the congregation of God",
        "source_ids": {"easton": "kithlish", "smith": "kithlish", "isbe": "kithlish"},
        "key_refs": ["Joshua 15:40"]
    },
    "kitron": {
        "id": "kitron",
        "term": "Kitron",
        "category": "places",
        "intro": "<p>Kitron (meaning <em>knotty</em> or <em>making sweet</em>) was a city in the territory of Zebulun from which the Zebulunites failed to drive out the Canaanite inhabitants, according to Judges 1:30. Instead, the Canaanites were put to forced labor—a failure of the complete dispossession that the conquest ideology of Deuteronomy required. This accommodation of Canaanites within Zebulun's territory was part of a broader pattern in Judges 1 where multiple northern tribes similarly failed to complete the conquest.</p><p>Kitron is identified with Kattath (Joshua 19:15) and has been associated with Kana el-Jalil in the lower Galilee. The Judges 1 narrative of partial conquest serves as the theological prologue to the entire book of Judges, explaining how the ongoing presence of Canaanites among Israel became the occasion for the cycle of apostasy, oppression, and deliverance that defines the period. Kitron's surviving Canaanite population, reduced to servitude rather than expelled, represents the seeds of the religious compromise that would later draw Zebulun and the other northern tribes into syncretistic worship of Canaanite gods.</p>",
        "sections": [],
        "hitchcock_meaning": "making sweet; binding; knotty",
        "source_ids": {"easton": "kitron", "smith": "kitron", "isbe": "kitron"},
        "key_refs": ["Judges 1:30", "Joshua 19:15"]
    },
    "kittim": {
        "id": "kittim",
        "term": "Kittim",
        "category": "people",
        "intro": "<p>Kittim (also spelled Chittim) was a son of Javan (Greece) in the table of nations (Genesis 10:4; 1 Chronicles 1:7), giving his name to an island people of the Mediterranean. In its most specific sense, Kittim referred to the inhabitants of Cyprus and particularly the city of Kition (modern Larnaka), and the name appears in early texts in association with the island. The identification expanded over time to encompass other Mediterranean island peoples—Macedonians, Romans, and western sea powers generally.</p><p>In prophetic literature, Kittim underwent a significant semantic expansion. Numbers 24:24 uses it in Balaam's oracle: <em>ships shall come from Kittim and shall afflict Asshur and Eber</em>—applied by later interpreters variously to the Greeks under Alexander or to Rome. Daniel 11:30 refers to ships of Kittim that came against the king of the North (Antiochus IV Epiphanes), a reference confirmed by historical records of Roman envoys who humiliated Antiochus at Alexandria in 168 BC. The Dead Sea Scrolls use Kittim extensively as a code name for Rome, reflecting the term's continued evolution from Cyprus to the dominant western imperial power of each successive era.</p>",
        "sections": [],
        "hitchcock_meaning": "breaking; bruising small; gold; coloring",
        "source_ids": {"easton": "kittim", "smith": "kittim", "isbe": "kittim"},
        "key_refs": ["Genesis 10:4", "Numbers 24:24", "Daniel 11:30", "Isaiah 23:1"]
    },
    "knead": {
        "id": "knead",
        "term": "Knead",
        "category": "concepts",
        "intro": "<p>Kneading—working dough with the hands to develop its gluten structure before baking—was a central domestic activity in the ancient Israelite household. The Hebrew <em>lûš</em> (to knead) describes this process of working flour mixed with water, oil, and sometimes leaven into a cohesive, pliable dough. Women were the primary bread-makers in Israelite households, and the kneading trough (<em>mišʿeret</em>) was a basic piece of domestic equipment.</p><p>Kneading appears in several narrative contexts: Abraham instructed Sarah to <em>quickly make ready three measures of fine flour, knead it, and make cakes</em> for his divine guests (Genesis 18:6); the woman of En-dor kneaded dough to make bread for Saul before his last battle (1 Samuel 28:24); and Tamar kneaded dough to make cakes for her brother Amnon in the episode that ended in his assault on her (2 Samuel 13:8). Hosea 7:4 uses the image of a heated oven in the context of kneading and fermentation as a metaphor for the heated conspiracies of Israel's corrupt court. Paul's use of the kneading and leavening metaphor (1 Corinthians 5:6–7; Galatians 5:9) to describe the spread of sin or false teaching drew on the household familiarity with this daily process.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "knead", "isbe": "bread"},
        "key_refs": ["Genesis 18:6", "1 Samuel 28:24", "Hosea 7:4", "1 Corinthians 5:6"]
    },
    "kneading-trough": {
        "id": "kneading-trough",
        "term": "Kneading-trough",
        "category": "concepts",
        "intro": "<p>The kneading trough (Hebrew <em>mišʿeret</em>) was the vessel in which dough was mixed and worked before baking. In ancient households it was typically a wooden bowl or basin of sufficient size to accommodate several pounds of flour at once. After kneading, the dough was left in the trough to rise if leavened, or baked immediately if unleavened.</p><p>The kneading trough appears in two significant biblical contexts. In the Passover narrative (Exodus 12:34), the Israelites departed Egypt so hastily that they could not wait for their bread to rise—they bound their kneading troughs with their unleavened dough on their shoulders and took them along. This detail explains the origin of the unleavened bread of Passover and is cited annually in the Passover haggadah as evidence of the haste of the Exodus. In Moses's blessing of Israel (Deuteronomy 28:5, 17), the kneading trough is specifically listed among the things that will be blessed in obedience or cursed in disobedience—reflecting the vessel's centrality to daily food supply and household prosperity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "kneading-trough", "isbe": "kneading-trough"},
        "key_refs": ["Exodus 12:34", "Deuteronomy 28:5", "Deuteronomy 28:17"]
    },
    "knife": {
        "id": "knife",
        "term": "Knife",
        "category": "concepts",
        "intro": "<p>Knives in the biblical world served multiple practical, ritual, and symbolic functions. The Hebrew <em>ḥereb</em> (literally <em>the waster</em>) typically denotes a sharp instrument and is used for both sword and knife, while <em>maʾākelet</em> (from a root meaning to consume or eat) denotes a sacrificial or slaughter knife specifically. Stone knives (flint) were explicitly used for circumcision even into the Iron Age, as in Exodus 4:25 (Zipporah's flint knife) and Joshua 5:2–3 (stone knives for the mass circumcision at Gilgal)—a remarkable retention of Neolithic technology for sacred rites long after metal had become standard.</p><p>The knife appears in some of Scripture's most dramatic moments: Abraham raised a knife to sacrifice Isaac before the angel stopped him (Genesis 22:6, 10); the concubine's body was cut in twelve pieces with a knife in the terrible episode of Judges 19:29. Levitical law specified how sacrificial animals were to be slaughtered, and the priests' knife-work at the altar was governed by detailed regulations. In Ezra 1:9, knives are listed among the temple vessels returned by Cyrus—the sacrificial equipment whose return signaled the resumption of proper temple worship.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "knife", "smith": "knife", "isbe": "knife"},
        "key_refs": ["Genesis 22:6", "Joshua 5:2", "Judges 19:29", "Ezra 1:9"]
    },
    "knock": {
        "id": "knock",
        "term": "Knock",
        "category": "concepts",
        "intro": "<p>Knocking at doors is an action whose cultural significance in the biblical world differed from Western conventions. Easton notes that Orientals do not knock when entering another's house but call out from outside the door—knocking being associated with the gesture of requesting entry when a locked or bolted door is the barrier. In the New Testament, knocking functions as a powerful metaphor for prayer and divine access.</p><p>Jesus's Sermon on the Mount teaching—<em>Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you</em> (Matthew 7:7–8; Luke 11:9–10)—uses the knocking image for persistent, confident prayer. The parable of the friend at midnight (Luke 11:5–8) extends the image to urgent nocturnal petition. In Revelation 3:20, Christ himself stands at the door and knocks: <em>If anyone hears my voice and opens the door, I will come in to him and eat with him, and he with me</em>—an image of personal fellowship offered to the church at Laodicea. The domesticity of the image—knocking at a door, awaiting a response—captures both the intimacy and the respect for human response embedded in the biblical understanding of divine-human relationship.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "knock", "isbe": "knock"},
        "key_refs": ["Matthew 7:7", "Luke 11:9", "Acts 12:16", "Revelation 3:20"]
    },
    "knop": {
        "id": "knop",
        "term": "Knop",
        "category": "concepts",
        "intro": "<p>Knops (from the Old English <em>cnop</em>, a knob or button) were ornamental rounded protuberances used in the furnishings of the tabernacle and temple. Two distinct Hebrew terms are rendered knop in the KJV: <em>kaphtor</em>, which denotes the almond-blossom-shaped ornaments on the golden lampstand (Exodus 25:31–36), carved alternately with flowers and buds along each of the seven branches; and <em>peqāʿîm</em>, the gourd-like ornamental carvings that encircled the walls of Solomon's temple interior (1 Kings 6:18; 7:24) and decorated the bronze sea's rim.</p><p>The lampstand's almond-shaped knops have been interpreted symbolically as representing fruitfulness and the awakened life of the Spirit—the almond being the first tree to flower in spring, a symbol of vigilance and readiness. The term <em>kaphtor</em> also appears as a place name (Caphtor, the homeland of the Philistines), suggesting the ornamental form may have been associated with Aegean or Cretan artistic traditions. The careful description of these architectural and liturgical details in Exodus and Kings reflects the importance of beauty and craftsmanship in the construction of sacred space.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "knop", "smith": "knop", "isbe": "knop"},
        "key_refs": ["Exodus 25:31", "Exodus 25:33", "1 Kings 6:18", "1 Kings 7:24"]
    },
    "koa": {
        "id": "koa",
        "term": "Koa",
        "category": "people",
        "intro": "<p>Koa appears only once in Scripture, in Ezekiel 23:23, listed alongside Pekod and Shoa as Babylonian and Assyrian peoples who would come against the apostate Jerusalem (symbolized as Oholibah). The name is likely a reference to a specific province, tribe, or people within the Babylonian or eastern Mesopotamian sphere. Some scholars have identified Koa with the Qutu (Gutians), a people from the Zagros mountains east of the Tigris, or with a region known in cuneiform sources as Qa'a or Qawe.</p><p>Ezekiel's vision in chapter 23 presents an allegory of two sisters, Oholah (Samaria) and Oholibah (Jerusalem), who prostituted themselves to Assyrian and Babylonian lovers. The enumeration of Koa, Shoa, and Pekod alongside Babylonian and Chaldean warriors represents the broad coalition of eastern peoples that Nebuchadnezzar could marshal against Judah. Koa's obscurity in the biblical record—appearing only in this single prophetic text—reflects its status as a peripheral eastern people known to Ezekiel's Babylonian audience but less familiar in the biblical mainstream.</p>",
        "sections": [],
        "hitchcock_meaning": "hope; a congregation",
        "source_ids": {"easton": "koa", "smith": "koa", "isbe": "koa"},
        "key_refs": ["Ezekiel 23:23"]
    },
    "kohath": {
        "id": "kohath",
        "term": "Kohath",
        "category": "people",
        "intro": "<p>Kohath was the second son of Levi (Genesis 46:11; Exodus 6:16), and through him descended the most sacred branch of the Levitical priesthood. His son Amram was the father of Moses, Aaron, and Miriam—making Kohath the great-grandfather of Israel's greatest prophet and its first high priest. This genealogical centrality gave the Kohathites primacy of honor among the three Levitical clans (Gershon, Kohath, and Merari).</p><p>In the wilderness organization described in Numbers 3–4, the Kohathites were assigned the most sacred task: carrying the ark of the covenant, the table of showbread, the lampstand, the altars, and the other sanctuary vessels when Israel moved camp. They were required to carry these items on their shoulders using poles—never on carts—after the priests had wrapped each piece in its protective coverings. The prohibition against touching the holy things on pain of death (Numbers 4:15) underscored the awesome responsibility of their role. This portable temple service in the wilderness foreshadowed the later fixed priesthood, and the Kohathite families of Samuel's lineage and the sons of Korah (who wrote many Psalms) show the broad spiritual influence of Kohath's descendants.</p>",
        "sections": [],
        "hitchcock_meaning": "congregation; wrinkle; bluntness",
        "source_ids": {"easton": "kohath", "smith": "kohath", "isbe": "kohath"},
        "key_refs": ["Genesis 46:11", "Exodus 6:18", "Numbers 3:27", "Numbers 4:15"]
    },
    "kohathites": {
        "id": "kohathites",
        "term": "Kohathites",
        "category": "people",
        "intro": "<p>The Kohathites were the descendants of Kohath son of Levi, forming the first and most honored of the three Levitical divisions (Kohathites, Gershonites, and Merarites). Their distinctive responsibility in the wilderness tabernacle was the carrying and care of the most sacred objects: the ark, the table of showbread, the lampstand, the golden altar, and all the vessels of the sanctuary. Only the Aaronic priests could prepare these items for transport, wrapping them in their appointed coverings; the Kohathites then carried them on their shoulders using poles, never touching the holy objects themselves.</p><p>Moses and Aaron were Kohathites through their father Amram, giving the family its supreme prestige. In the land settlement, the Kohathites received twenty-three cities distributed among Judah, Simeon, Benjamin, Ephraim, Dan, and the half-tribe of Manasseh (Joshua 21:4–26). The sons of Korah, who composed several Psalms (42, 44–49, 84–85, 87–88), were Kohathites who had survived Korah's rebellion and maintained a distinguished role in temple music and worship. Hezekiah's and Josiah's reformations both involved Kohathites in the cleansing and restoration of the temple.</p>",
        "sections": [],
        "hitchcock_meaning": "descendants of Kohath",
        "source_ids": {"easton": "kohathites", "isbe": "kohathites"},
        "key_refs": ["Numbers 3:27", "Numbers 4:4", "Joshua 21:4", "2 Chronicles 34:12"]
    },
    "korah": {
        "id": "korah",
        "term": "Korah",
        "category": "people",
        "intro": "<p>Korah was the name of several figures in the Old Testament, the most prominent being Korah son of Izhar, a Kohathite Levite who led the most serious internal rebellion against the authority of Moses and Aaron recorded in the Pentateuch. Numbers 16 describes how Korah, together with the Reubenites Dathan and Abiram and 250 leading men of the congregation, challenged Moses's and Aaron's exclusive priestly authority, asserting that all the congregation was holy and that Moses had exalted himself above the assembly of the LORD.</p><p>The divine judgment was swift and dramatic: the earth opened and swallowed Korah, Dathan, and Abiram with their households, and fire from God consumed the 250 who had offered incense. Korah's sons, however, did not die (Numbers 26:11), and their descendants became prominent temple musicians and gatekeepers—the Sons of Korah who composed or performed Psalms 42, 44–49, 84–85, and 87–88. Other figures named Korah include a son of Esau (Genesis 36:5) and various Calebite figures in Chronicles genealogies. Jude 11 uses Korah's rebellion as a paradigm of those who despise authority and perish in their own presumption.</p>",
        "sections": [],
        "hitchcock_meaning": "baldness; ice; hail",
        "source_ids": {"easton": "korah", "smith": "korah", "isbe": "korah"},
        "key_refs": ["Numbers 16:1", "Numbers 16:32", "Numbers 26:11", "Jude 1:11"]
    },
    "korahites": {
        "id": "korahites",
        "term": "Korahites",
        "category": "people",
        "intro": "<p>The Korahites were the portion of the Kohathite Levites descended from Korah son of Izhar. Despite their ancestor's rebellion against Moses and Aaron, the Korahite family was not extinguished—Numbers 26:11 explicitly notes that Korah's sons did not die in the earth-swallowing judgment. They became established as doorkeepers and musicians of the tabernacle and later the temple, contributing significantly to Israel's worship tradition.</p><p>As gatekeepers, the Korahites guarded the threshold of the sacred precincts, a role reflected in Psalm 84:10: <em>I would rather be a doorkeeper in the house of my God than dwell in the tents of wickedness</em>—a psalm attributed to the Sons of Korah. David organized 212 Korahites as gatekeepers for the ark (1 Chronicles 9:19; 26:1–19). Their military function as guardians of the camp entrance in the wilderness evolved into the permanent temple gatekeeping role. Several Korahites are named in 2 Chronicles 20:19 as leading in worship during Jehoshaphat's fast, and in Nehemiah's time Korahite gatekeepers were among those resettled in Jerusalem after the exile.</p>",
        "sections": [],
        "hitchcock_meaning": "descendants of Korah",
        "source_ids": {"easton": "korahites", "isbe": "korahites"},
        "key_refs": ["Numbers 26:11", "1 Chronicles 9:19", "Psalm 84:10", "2 Chronicles 20:19"]
    },
    "kore": {
        "id": "kore",
        "term": "Kore",
        "category": "people",
        "intro": "<p>Kore (meaning <em>partridge</em>) was the name of two individuals in the post-exilic period. The first was a Levite of the family of Asaph, the son of Imnah, who was a gatekeeper of the eastern gate and was appointed by King Hezekiah during his religious reformation to oversee the freewill offerings brought to God—ensuring their proper distribution to the priests and Levites in their cities (2 Chronicles 31:14).</p><p>A second Kore was a Levite of the Korahite family, the son of Asaph, listed in 1 Chronicles 9:19 (and 26:1 in connection with his son Shallum, who headed the Korahite gatekeepers). The Korahite gatekeepers traced their lineage to Phinehas son of Eleazar, who had charge of the threshold of the tent of meeting. The gatekeeper function these Kore-related families exercised was both a practical role—controlling access to sacred precincts—and a symbol of the careful maintenance of boundaries between the holy and common that was central to Israelite worship theology.</p>",
        "sections": [],
        "hitchcock_meaning": "partridge; calling",
        "source_ids": {"easton": "kore", "smith": "kore", "isbe": "kore"},
        "key_refs": ["1 Chronicles 9:19", "2 Chronicles 31:14"]
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
    print(f'BP k1: Kabzeel → Kore: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
