"""
BP Article Synthesis — b1: Baal → Barsabas
Covers Easton entries: Baal through Barsabas (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-b1.py
Run: python3 scripts/bp-b1.py
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
    "baal": {
        "id": "baal",
        "term": "Baal",
        "category": "concepts",
        "intro": "<p>Baal (meaning <em>lord</em> or <em>master</em>) was the principal male deity of the Phoenicians and Canaanites, and the chief rival to the worship of Yahweh throughout Israel's history in the land. The name functioned both as a common noun meaning owner or husband and as the proper name of the storm and fertility god worshipped across the ancient Near East under regional variants. In Canaan, Baal was understood as the son of El and the lord of rain and agricultural abundance — making his cult directly competitive with Israel's covenant claim that Yahweh alone sent the rain and gave the harvest.</p><p>The contest between Baal worship and the religion of Israel is a recurring crisis in the historical and prophetic books. The worst outbreak came under Ahab and Jezebel, who established a state cult of Baal in Samaria and systematically persecuted Yahweh's prophets. Elijah's confrontation with the prophets of Baal on Mount Carmel (1 Kings 18) was the dramatic turning point, demonstrating that the God of Israel controlled both the drought and the rain. The prophets Hosea, Jeremiah, and Ezekiel consistently denounce Baal worship as spiritual adultery against the covenant. The compound place and divine names beginning with Baal throughout the text reflect the pervasive presence of this cult in the landscape and religious life of Canaan.</p>",
        "hitchcock_meaning": "master; lord",
        "source_ids": {"easton": "baal", "smith": "baal"},
        "key_refs": ["Judges 2:11", "1 Kings 18:18", "Jeremiah 2:23", "Hosea 2:17"]
    },
    "baal-berith": {
        "id": "baal-berith",
        "term": "Baal-berith",
        "category": "concepts",
        "intro": "<p>Baal-berith (meaning <em>covenant lord</em> or <em>lord of the covenant</em>) was the name of the Baal worshipped at Shechem after the death of Gideon. When Israel again went after the Baals, Shechem's temple of Baal-berith became a center of idolatrous worship, and its treasury funded Abimelech's violent seizure of power — he hired worthless men with seventy pieces of silver from the house of Baal-berith and used them to murder his seventy half-brothers on a single stone (Judges 9:4). The same temple is called the house of El-berith in Judges 9:46.</p><p>The deity's name suggests a god of covenants or treaties — possibly a patron of commercial and political agreements in the Shechemite community. His worship represents the type of syncretism the Deuteronomic historians repeatedly warn against: a covenant people turning to a covenant lord who was not the God of Israel. The idol's treasury funding fratricidal violence becomes a pointed irony in the narrative of Judges 9.</p>",
        "hitchcock_meaning": "idol of the covenant",
        "source_ids": {"easton": "baal-berith", "isbe": "baal-berith"},
        "key_refs": ["Judges 8:33", "Judges 9:4", "Judges 9:46"]
    },
    "baal-gad": {
        "id": "baal-gad",
        "term": "Baal-gad",
        "category": "places",
        "intro": "<p>Baal-gad (meaning <em>lord of fortune</em> or <em>lord of the troop</em>) was a Canaanite city in the valley of Lebanon at the foot of Mount Hermon, marking the northern limit of Joshua's conquest. It appears three times in Joshua (11:17; 12:7; 13:5) as the northernmost point of the territory Joshua cleared of kings, with the southern limit being Mount Halak toward Seir. Despite its identification as conquered territory, the surrounding region remained incompletely subdued at Joshua's death.</p><p>The site is identified by most scholars with the area of Baalbek or with Hasbeiya near the sources of the Jordan. The name preserves the memory of a Baal cult at this northern sanctuary. The city's existence at the headwaters of the Jordan underscores how deeply Baal worship was embedded in the geography of the land Israel was entering, with sacred sites bearing the deity's name from the far north to the plains of Moab.</p>",
        "hitchcock_meaning": "idol of fortune or felicity",
        "source_ids": {"easton": "baal-gad", "isbe": "baal-gad"},
        "key_refs": ["Joshua 11:17", "Joshua 12:7", "Joshua 13:5"]
    },
    "baal-hamon": {
        "id": "baal-hamon",
        "term": "Baal-hamon",
        "category": "places",
        "intro": "<p>Baal-hamon (meaning <em>place of a multitude</em> or <em>lord who rules a crowd</em>) was a place where Solomon maintained an extensive vineyard, mentioned only in Song of Solomon 8:11. The text says Solomon let out the vineyard to keepers, each of whom was to bring a thousand pieces of silver for its fruit, while the beloved keeps her own vineyard. The location is unknown and is not identified with any other biblical site with confidence.</p><p>The name's association with abundance — a <em>multitude</em> or <em>crowd</em> — suits its context as the site of a notably productive vineyard. Some interpreters understand the passage as figurative rather than geographical. In any case, Baal-hamon appears only in this single lyrical context and carries no further narrative significance in the biblical text.</p>",
        "hitchcock_meaning": "who rules a crowd",
        "source_ids": {"easton": "baal-hamon", "isbe": "baal-hamon"},
        "key_refs": ["Song of Solomon 8:11"]
    },
    "baal-hanan": {
        "id": "baal-hanan",
        "term": "Baal-hanan",
        "category": "people",
        "intro": "<p>Baal-hanan (meaning <em>lord of grace</em>) is the name of two men in the Old Testament. The first was a king of Edom, the son of Achbor, listed in the catalogue of Edomite kings who reigned before any king ruled Israel (Genesis 36:38–39; 1 Chronicles 1:49–50). He succeeded Shaul of Rehoboth and was himself succeeded by Hadar. These early Edomite rulers are listed without dates or narrative detail, forming part of the genealogical bridge between Esau and the later Edomite nation.</p><p>The second Baal-hanan was an officer under David, appointed as overseer of the olive trees and sycamore trees in the lowland Shephelah region (1 Chronicles 27:28). He is listed among David's property managers alongside those responsible for the various agricultural assets of the royal household. The name, despite containing the element Baal, was evidently in common use as a personal name in Israel without necessarily implying devotion to the Canaanite deity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baal-hanan", "isbe": "baal-hanan"},
        "key_refs": ["Genesis 36:38", "1 Chronicles 1:49", "1 Chronicles 27:28"]
    },
    "baal-hazor": {
        "id": "baal-hazor",
        "term": "Baal-hazor",
        "category": "places",
        "intro": "<p>Baal-hazor (meaning <em>Baal's village</em> or <em>having a courtyard</em>) was a place on the border region between Ephraim and Benjamin where Absalom kept his sheep-shearers. It was there that Absalom invited all the king's sons to a feast and had his servants kill Amnon in revenge for the rape of his sister Tamar — the act that precipitated Absalom's three-year exile to Geshur (2 Samuel 13:23). The site is mentioned once in the narrative and is identified by some scholars with Tell Asur, approximately five miles northeast of Bethel at an elevation of about 3,300 feet.</p><p>The name also appears in Nehemiah 11:33 in the form Hazor, as a town resettled by Benjaminites after the return from exile, though the identification with the same site is uncertain. Baal-hazor is remembered primarily as the setting of the fratricide that began the long sequence of events culminating in Absalom's rebellion against David.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baal-hazor", "isbe": "baal-hazor"},
        "key_refs": ["2 Samuel 13:23"]
    },
    "baal-hermon": {
        "id": "baal-hermon",
        "term": "Baal-hermon",
        "category": "places",
        "intro": "<p>Baal-hermon (meaning <em>lord of Hermon</em> or <em>possessor of destruction</em>) refers to a location near Mount Hermon associated with Baal worship. It appears in two distinct contexts: in Judges 3:3 as a northern boundary marker indicating Canaanite territory not yet subdued — the Hivites who dwell on Mount Lebanon from Mount Baal-hermon to the entrance of Hamath — and in 1 Chronicles 5:23 as part of the territory settled by the half-tribe of Manasseh in the east, ranging from Bashan to Baal-hermon and Senir and Mount Hermon.</p><p>The name preserves the memory of a Baal sanctuary at or near Hermon, a prominent peak long associated with divine presence in the ancient Near East. Mount Hermon itself was called Senir by the Amorites and Sirion by the Sidonians, reflecting its regional significance as a landmark and sacred site. The presence of a Baal cult at this northern mountain illustrates the geographic reach of Canaanite religion into the territories Israel partially settled.</p>",
        "hitchcock_meaning": "possessor of destruction or of a devoted thing",
        "source_ids": {"easton": "baal-hermon", "isbe": "baal-hermon"},
        "key_refs": ["Judges 3:3", "1 Chronicles 5:23"]
    },
    "baal-meon": {
        "id": "baal-meon",
        "term": "Baal-meon",
        "category": "places",
        "intro": "<p>Baal-meon (meaning <em>lord of dwelling</em> or <em>master of the house</em>) was a town on the Transjordanian plateau assigned to the tribe of Reuben, listed in Numbers 32:38 among the cities rebuilt by Reubenites — the text notes that the names were changed, suggesting a renaming of Canaanite sacred sites. It is also called Beth-meon (Jeremiah 48:23), Beth-baal-meon (Joshua 13:17), and Beth-baalmeon (1 Chronicles 5:8). The site is identified with the modern Maan, about nine miles south-southwest of Heshbon.</p><p>By the time of Ezekiel and Jeremiah, Baal-meon had fallen under Moabite control — both prophets mention it in their oracles against Moab (Jeremiah 48:23; Ezekiel 25:9). Its history illustrates the contested nature of Transjordanian territory throughout the biblical period, with Israelite tribal settlement giving way to Moabite resettlement after the fall of the northern kingdom.</p>",
        "hitchcock_meaning": "idol or master of the house",
        "source_ids": {"easton": "baal-meon", "isbe": "baal-meon"},
        "key_refs": ["Numbers 32:38", "Joshua 13:17", "Jeremiah 48:23"]
    },
    "baal-peor": {
        "id": "baal-peor",
        "term": "Baal-peor",
        "category": "concepts",
        "intro": "<p>Baal-peor (meaning <em>lord of the opening</em> or <em>master of the gap</em>) was the god of the Moabites worshipped at Peor, whose cult Israel fell into during the wilderness period through the seduction of Moabite and Midianite women (Numbers 25:1–9). The incident — in which Israel <em>joined himself unto Baal-peor</em> and ate sacrifices to the dead — provoked a plague that killed 24,000 people before it was stopped by Phinehas's act of zealous judgment. The event at Peor became a paradigmatic warning throughout subsequent Scripture.</p><p>Deuteronomy 4:3 cites Baal-peor as a lesson in the consequences of following other gods, and Psalm 106:28–29 includes the incident in its catalogue of Israel's wilderness sins. Hosea 9:10 uses Peor as the defining moment of Israel's spiritual corruption: <em>they went to Baal-peor, and separated themselves unto that shame</em>. The New Testament alludes to Balaam's role in advising the Midianites to use this strategy against Israel (2 Peter 2:15; Revelation 2:14). The name was also applied to a mountain near Jericho where Balak brought Balaam to curse Israel.</p>",
        "hitchcock_meaning": "master of the opening",
        "source_ids": {"easton": "baal-peor", "isbe": "baal-peor"},
        "key_refs": ["Numbers 25:3", "Deuteronomy 4:3", "Numbers 31:16", "Psalms 106:28"]
    },
    "baal-perazim": {
        "id": "baal-perazim",
        "term": "Baal-perazim",
        "category": "places",
        "intro": "<p>Baal-perazim (meaning <em>lord of breaches</em> or <em>Baal of bursting forth</em>) was the site of one of David's victories over the Philistines shortly after his consolidation of the kingdom. When the Philistines spread themselves in the valley of Rephaim south of Jerusalem, David inquired of God and received permission to attack; his forces broke through the enemy like a bursting flood of waters, and David named the place accordingly — <em>The LORD has broken through my enemies before me, like a breaking forth of waters</em> (2 Samuel 5:20; 1 Chronicles 14:11).</p><p>The name's Baal element does not imply deity worship but reflects the common use of Baal as a place-name element meaning <em>lord</em> or <em>owner</em> in Canaanite topography. Isaiah 28:21 later refers to the LORD rising up as at Baal-perazim as an image of sudden, powerful divine action in judgment — turning the memory of Israel's military victory into a type of God's judgments against his own people.</p>",
        "hitchcock_meaning": "god of divisions",
        "source_ids": {"easton": "baal-perazim", "isbe": "baal-perazim"},
        "key_refs": ["2 Samuel 5:20", "1 Chronicles 14:11", "Isaiah 28:21"]
    },
    "baal-shalisha": {
        "id": "baal-shalisha",
        "term": "Baal-shalisha",
        "category": "places",
        "intro": "<p>Baal-shalisha (meaning <em>lord of Shalisha</em> or <em>the god who presides over three</em>) was a place from which a man brought twenty loaves of barley bread and fresh ears of grain to the prophet Elisha at Gilgal during a time of famine (2 Kings 4:42). Elisha commanded that the food be distributed to a hundred men; his servant protested the inadequacy, but Elisha repeated the command, and the people ate and had food left over — a miracle closely parallel in form to the feeding of the multitudes in the Gospels.</p><p>The location of Baal-shalisha is generally identified with the land of Shalisha mentioned in 1 Samuel 9:4, in the hill country of Ephraim. The episode at Baal-shalisha is one of several miracle accounts clustered in 2 Kings 4–5 that establish Elisha's prophetic authority as Elijah's successor, demonstrating divine provision through his ministry.</p>",
        "hitchcock_meaning": "the god that presides over three",
        "source_ids": {"easton": "baal-shalisha"},
        "key_refs": ["2 Kings 4:42"]
    },
    "baal-tamar": {
        "id": "baal-tamar",
        "term": "Baal-tamar",
        "category": "places",
        "intro": "<p>Baal-tamar (meaning <em>lord of the palm tree</em> or <em>master of the palm trees</em>) was a place in the territory of Benjamin near Gibeah of Saul, mentioned in Judges 20:33 as the position from which the Israelite forces deployed in their third and final assault on Gibeah during the civil war against Benjamin triggered by the crime of Gibeah. The Israelites rose from their position at Baal-tamar while a rear ambush emerged from its concealed place west of Gibeah, surrounding the Benjaminites.</p><p>The site is also associated with the palm tree of Deborah, where the prophetess held court between Ramah and Bethel in Judges 4:5, though the identification is not certain. Baal-tamar is remembered primarily as a tactical position in one of the most violent episodes of the period of the judges, the near-annihilation of the tribe of Benjamin.</p>",
        "hitchcock_meaning": "master of the palm-tree",
        "source_ids": {"easton": "baal-tamar", "isbe": "baal-tamar"},
        "key_refs": ["Judges 20:33"]
    },
    "baal-zebub": {
        "id": "baal-zebub",
        "term": "Baal-zebub",
        "category": "concepts",
        "intro": "<p>Baal-zebub (meaning <em>lord of flies</em>) was the god of the Philistines at Ekron, consulted by the Israelite king Ahaziah when he fell through a lattice in his upper chamber and was injured. Ahaziah sent messengers to inquire of Baal-zebub whether he would recover from his injury — a consultation the prophet Elijah intercepted with a divine counter-message: because the king had sent to inquire of Baal-zebub rather than of the God of Israel, he would not leave his bed but would die (2 Kings 1:2–3, 16). The king died as prophesied.</p><p>The name reappears in the New Testament as Beelzebub (the Greek form), used by the Pharisees as a designation for the prince of demons (Matthew 12:24; Mark 3:22; Luke 11:15). Jesus's opponents accused him of casting out demons by the power of Beelzebub, prompting his famous argument that a kingdom divided against itself cannot stand. The transformation from a local Philistine deity into a name for Satan's leadership reflects the evolution of Jewish angelology and demonology in the intertestamental period.</p>",
        "hitchcock_meaning": "god of the fly",
        "source_ids": {"easton": "baal-zebub"},
        "key_refs": ["2 Kings 1:2", "2 Kings 1:3", "Matthew 12:24"]
    },
    "baal-zephon": {
        "id": "baal-zephon",
        "term": "Baal-zephon",
        "category": "places",
        "intro": "<p>Baal-zephon (meaning <em>Baal of the north</em> or <em>lord of the watch-tower</em>) was an Egyptian location on or near the shores of the Gulf of Suez, mentioned as a landmark in the account of Israel's departure from Egypt. Exodus 14:2 records God's instruction to Moses to tell Israel to encamp before Pi-hahiroth, between Migdol and the sea, before Baal-zephon — the position that would appear to trap them against the water and prompt Pharaoh to pursue. Numbers 33:7 repeats the encampment at Pi-hahiroth, which is before Baal-zephon.</p><p>The site preserves the name of a Baal sanctuary in Egyptian territory, a reminder that Semitic religion and place-names had penetrated into the Delta region through centuries of cultural contact. The exact location remains disputed, as the identification depends on the broader question of the route of the Exodus, but it was evidently a recognizable landmark to both Israel and Egypt at the time of the crossing.</p>",
        "hitchcock_meaning": "the idol or possession of the north",
        "source_ids": {"easton": "baal-zephon", "isbe": "baal-zephon"},
        "key_refs": ["Exodus 14:2", "Numbers 33:7"]
    },
    "baalah": {
        "id": "baalah",
        "term": "Baalah",
        "category": "places",
        "intro": "<p>Baalah (meaning <em>mistress</em> or <em>city</em>) is a place-name applied to several distinct sites in the Old Testament. The most significant is Baalah of Judah, also called Kirjath-jearim (city of forests) and Kirjath-baal — the town where the ark of the covenant rested for twenty years after its return from the Philistines, until David brought it to Jerusalem (2 Samuel 6:2; 1 Chronicles 13:6). A second Baalah was a town in the south of Judah (Joshua 15:29), identified with Bilhah in 1 Chronicles 4:29. A third was a mountain on the border of Judah (Joshua 15:11).</p><p>The name's root — the feminine form of Baal — suggests these sites had at some point been associated with Canaanite religious practice, though their later Israelite usage was entirely dissociated from any divine name. The ark's long sojourn at Kirjath-baal/Baalah of Judah is the theologically significant association, making this village the custodian of Israel's most sacred object through the turbulent years of Saul's reign.</p>",
        "hitchcock_meaning": "her idol; she that is governed or subdued",
        "source_ids": {"easton": "baalah", "smith": "baalah", "isbe": "baalah"},
        "key_refs": ["Joshua 15:10", "2 Samuel 6:2", "1 Chronicles 13:6"]
    },
    "baalath": {
        "id": "baalath",
        "term": "Baalath",
        "category": "places",
        "intro": "<p>Baalath (meaning <em>a rejoicing</em> or <em>our proud lord</em>) was a town in the territory of the tribe of Dan, mentioned in Joshua 19:44. It was later fortified by Solomon as part of his defensive building program (1 Kings 9:18; 2 Chronicles 8:6) — the same passage that records the building of Tadmor in the wilderness. Solomon's fortification of Baalath likely reflected its strategic location in the lowland Shephelah region between the Philistine coast and the Judean highlands.</p><p>The site has been tentatively identified with various locations in the Shephelah, though no consensus identification has emerged. Its fortification by Solomon alongside Hazor, Megiddo, and Gezer reflects the king's systematic strengthening of the land's defensive infrastructure, using his vast labor resources to secure the borders of his domain.</p>",
        "hitchcock_meaning": "a rejoicing; our proud lord",
        "source_ids": {"easton": "baalath", "smith": "baalath", "isbe": "baalath"},
        "key_refs": ["Joshua 19:44", "1 Kings 9:18", "2 Chronicles 8:6"]
    },
    "baalath-beer": {
        "id": "baalath-beer",
        "term": "Baalath-beer",
        "category": "places",
        "intro": "<p>Baalath-beer (meaning <em>Baalah of the well</em>) was a town at the southern boundary of the tribe of Simeon, listed in Joshua 19:8 as Baalath-beer, Ramath of the south — identifying it as the southernmost settlement of Simeon's inheritance. It is likely the same as Baal mentioned in 1 Chronicles 4:33 and possibly related to Beer-sheba or another well-site in the Negev region. The double name combines the feminine Baal element with the word for well, suggesting a sacred spring or well associated with local cult.</p><p>Like many of the Simeonite towns, Baalath-beer was located in territory that overlapped with Judah's southern inheritance and was susceptible to pressure from desert peoples. The tribe of Simeon gradually lost its distinct identity as it was absorbed into Judah, and its cities are often listed without further narrative development.</p>",
        "hitchcock_meaning": "subjected pit",
        "source_ids": {"easton": "baalath-beer", "isbe": "baalath-beer"},
        "key_refs": ["Joshua 19:8", "1 Chronicles 4:33"]
    },
    "baalbec": {
        "id": "baalbec",
        "term": "Baalbec",
        "category": "places",
        "intro": "<p>Baalbec (called by the Greeks <em>Heliopolis</em>, city of the sun) was a magnificent city in the valley between Lebanon and Anti-Lebanon, known in antiquity for its celebrated temple of the sun-god. The city stood at an elevation of approximately 3,800 feet in the Beqaa Valley, roughly fifty miles north of Damascus. Its enormous temple complex, the ruins of which remain among the most impressive in the ancient world, featured temples to Jupiter, Bacchus, and Venus built during the Roman imperial period.</p><p>Though not named in the biblical text by this Greek form, Baalbec is believed by many scholars to be the Baal-gad of Joshua or to be associated with the region of Lebanon mentioned in connection with Solomon's building activities. The cedars of Lebanon that supplied Solomon's temple were transported from the forests surrounding this area. The site represents the enduring presence of solar Baal worship in the northern reaches of what the biblical world considered the promised land's outer boundaries.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baalbec"},
        "key_refs": ["1 Kings 7:2", "2 Chronicles 9:16"]
    },
    "baale-of-judah": {
        "id": "baale-of-judah",
        "term": "Baale of Judah",
        "category": "places",
        "intro": "<p>Baale of Judah (meaning <em>lords of Judah</em>) is the name used in 2 Samuel 6:2 for the city from which David brought up the ark of the Lord to Jerusalem. The parallel passage in 1 Chronicles 13:6 uses the full form Kirjath-jearim (city of forests), establishing that Baale of Judah is another name for the same site — also called Baalah (Joshua 15:9–10) and Kirjath-baal (Joshua 18:14). The ark had rested there in the house of Abinadab on the hill for twenty years after its return from the Philistines.</p><p>The use of the name Baale of Judah in the Samuel narrative, alongside the ark's transfer to Jerusalem, reflects the complex nomenclature of the site. David's expedition to bring the ark from this city was marked by the death of Uzzah and a three-month delay at the house of Obed-edom, before the ark was successfully installed in Jerusalem with great celebration.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baale-of-judah", "smith": "baale-of-judah"},
        "key_refs": ["2 Samuel 6:2", "1 Chronicles 13:6"]
    },
    "baali": {
        "id": "baali",
        "term": "Baali",
        "category": "concepts",
        "intro": "<p>Baali (meaning <em>my lord</em> or <em>my master</em>) is a Hebrew term of address used for a husband in the possessive form of Baal. In Hosea 2:16, God addresses Israel through the prophet with the declaration that in the day of restoration she will no longer call him <em>Baali</em> (my Baal, my lord-master) but <em>Ishi</em> (my husband, my man) — a shift from the language of ownership and lordship to the language of intimate marital relationship. The prophet reproaches the Jewish community for using the term <em>Baali</em> for God, as the same word was also the name of the Canaanite deity Baal.</p><p>The passage is part of Hosea's extended marriage metaphor, in which Israel's unfaithfulness to God is portrayed as adultery, and God's restoration of Israel is portrayed as a new covenant of betrothal. The name change from Baali to Ishi signals not merely a linguistic shift but a new quality of relationship — one that removes all ambiguity between the worship of Yahweh and the cult of Baal.</p>",
        "hitchcock_meaning": "my idol; lord over me",
        "source_ids": {"easton": "baali", "smith": "baali", "isbe": "baali"},
        "key_refs": ["Hosea 2:16"]
    },
    "baalim": {
        "id": "baalim",
        "term": "Baalim",
        "category": "concepts",
        "intro": "<p>Baalim is the Hebrew plural of Baal, referring collectively to the various local manifestations and images of the Baal deity worshipped throughout Canaan and the surrounding region. Each Canaanite locality had its own Baal — lord of that particular territory or natural feature — and the Baalim collectively represented the full range of these local fertility and storm deities. Israel's apostasy is repeatedly described in the historical books as going after the Baalim (Judges 2:11; 1 Samuel 7:4), abandoning the covenant God for the regional lords of the land.</p><p>The Deuteronomic historians use Baalim as a shorthand for the full spectrum of Canaanite idolatry. Samuel's demand that Israel put away the Baalim and the Ashtaroth before the Lord would deliver them from the Philistines (1 Samuel 7:3–4) established the pattern: repentance required the concrete removal of idols, not merely verbal profession. The prophets, especially Hosea and Jeremiah, use the Baalim as the paradigmatic example of Israel's repeated infidelity to the exclusive covenant relationship with Yahweh.</p>",
        "hitchcock_meaning": "idols; masters; false gods",
        "source_ids": {"easton": "baalim", "smith": "baalim", "isbe": "baalim"},
        "key_refs": ["Judges 2:11", "1 Samuel 7:4"]
    },
    "baalis": {
        "id": "baalis",
        "term": "Baalis",
        "category": "people",
        "intro": "<p>Baalis (meaning <em>a rejoicing</em> or <em>a proud lord</em>) was the king of the Ammonites during the period immediately following the Babylonian destruction of Jerusalem in 586 B.C. He appears in Jeremiah 40:14 as the instigator of the assassination plot against Gedaliah, the Jewish governor appointed by Nebuchadnezzar over the remnant left in Judah. Johanan son of Kareah warned Gedaliah that Baalis had sent Ishmael son of Netaniah to kill him, but Gedaliah refused to believe the report.</p><p>Gedaliah was subsequently murdered by Ishmael as Johanan had warned, along with the Babylonian soldiers stationed with him (Jeremiah 41:1–3). The assassination destroyed the fragile Judahite community under Babylonian rule and precipitated the flight of the remaining population to Egypt against Jeremiah's counsel. Baalis's role in sponsoring the murder reflects Ammonite opportunism in the power vacuum left by Babylon's conquest of Judah.</p>",
        "hitchcock_meaning": "a rejoicing; a proud lord",
        "source_ids": {"easton": "baalis", "smith": "baalis", "isbe": "baalis"},
        "key_refs": ["Jeremiah 40:14"]
    },
    "baana": {
        "id": "baana",
        "term": "Baana",
        "category": "people",
        "intro": "<p>Baana (meaning <em>son of affliction</em>) is the name of two or three men in the Old Testament. Two of Solomon's twelve district officers bore this name: the first was responsible for the regions of Taanach, Megiddo, and Beth-shean (1 Kings 4:12), and the second governed Asher and Bealoth (1 Kings 4:16). A third Baana was the father of Zadok, one of those who helped rebuild the walls of Jerusalem under Nehemiah's direction (Nehemiah 3:4).</p><p>The two Solomonic officers bear the same name and served in the same administrative system but governed different districts. Their roles were to supply provisions for the royal household for one month each year, rotating the obligation among twelve governors to prevent excessive burden on any single region. The name Baana appears without narrative development beyond these administrative listings.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baana", "smith": "baana", "isbe": "baana"},
        "key_refs": ["1 Kings 4:12", "1 Kings 4:16", "Nehemiah 3:4"]
    },
    "baanah": {
        "id": "baanah",
        "term": "Baanah",
        "category": "people",
        "intro": "<p>Baanah (meaning <em>in affliction</em> or <em>son of affliction</em>) is the name of several men in the Old Testament. The most prominent were the two sons of Rimmon the Beerothite — Baanah and Rechab — captains of raiding parties under Ish-bosheth, Saul's surviving son. They murdered Ish-bosheth as he lay on his bed at midday and brought his head to David at Hebron, expecting reward. Instead David had them both executed, their hands and feet cut off and hung by the pool of Hebron (2 Samuel 4:5–12). David's response demonstrated that he had not sought the throne through violence against Saul's house.</p><p>Other men named Baanah include one of David's thirty warriors (2 Samuel 23:29; 1 Chronicles 11:30), an ancestor of a family that returned from exile with Zerubbabel (Ezra 2:2; Nehemiah 7:7), and one of those who sealed the covenant under Nehemiah (Nehemiah 10:27).</p>",
        "hitchcock_meaning": "in the answer; in affliction",
        "source_ids": {"easton": "baanah", "smith": "baanah", "isbe": "baanah"},
        "key_refs": ["2 Samuel 4:2", "2 Samuel 4:12", "2 Samuel 23:29"]
    },
    "baasha": {
        "id": "baasha",
        "term": "Baasha",
        "category": "people",
        "intro": "<p>Baasha (meaning <em>bravery</em> or <em>he who lays waste</em>) was the third king of the northern kingdom of Israel and the founder of a short-lived dynasty. He came to power c. 909 B.C. by assassinating Nadab, son of Jeroboam I, at the siege of Gibbethon — fulfilling the prophecy of Ahijah against Jeroboam's house — and proceeded to kill all of Jeroboam's descendants, eliminating the rival dynasty entirely. His reign of twenty-four years was characterized by perpetual war with Judah, particularly with King Asa.</p><p>Baasha's military pressure against Judah prompted Asa to make an alliance with Ben-hadad of Syria, who invaded Israel from the north and forced Baasha to abandon his fortification of Ramah. The prophet Jehu son of Hanani announced divine judgment against Baasha for walking in all the sins of Jeroboam and for destroying Jeroboam's house while doing no differently himself — the same condemnation that had fallen on the dynasty he replaced. His son Elah succeeded him but reigned only two years before being assassinated in the same pattern, ending the dynasty Baasha had established.</p>",
        "hitchcock_meaning": "he that seeks, or lays waste",
        "source_ids": {"easton": "baasha", "smith": "baasha", "isbe": "baasha"},
        "key_refs": ["1 Kings 15:33", "1 Kings 16:1", "2 Chronicles 16:1"]
    },
    "babe": {
        "id": "babe",
        "term": "Babe",
        "category": "concepts",
        "intro": "<p>Babe is used in Scripture both literally for infants and young children and metaphorically for spiritual immaturity. Jesus praised God for hiding things from the wise and learned and revealing them to <em>babes</em> (Matthew 11:25; Luke 10:21), using the term for those who are humble and receptive rather than self-sufficient — a reversal of human estimations of wisdom. In Romans 2:20, Paul uses the term ironically of the Jew who considers himself an instructor of <em>babes</em>, implying a condescending posture toward Gentiles.</p><p>Paul's metaphorical use in 1 Corinthians 3:1 is the most theologically developed: he was unable to address the Corinthians as spiritual people but as <em>babes in Christ</em>, able to receive only milk, not solid food, because of their carnality and divisions. The writer of Hebrews (5:13) similarly contrasts those who need milk — unskilled in the word of righteousness — with those who are mature. The babe metaphor thus marks the beginning of the Christian life as the standard assumes growth toward maturity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "babe", "isbe": "babe"},
        "key_refs": ["Matthew 11:25", "1 Corinthians 3:1", "Hebrews 5:13"]
    },
    "babel-tower-of": {
        "id": "babel-tower-of",
        "term": "Babel, tower of",
        "category": "places",
        "intro": "<p>The tower of Babel was a structure built by the post-flood human community on the plain of Shinar as an expression of unified ambition — <em>a city and a tower, whose top may reach unto heaven</em> (Genesis 11:4). The project was motivated by the desire to make a name for themselves and to avoid being scattered abroad, in direct tension with the divine command to fill the earth. The tower is generally understood as a type of Mesopotamian ziggurat — a stepped temple-tower — though its exact nature and scale are unknown beyond the brief biblical account.</p><p>The divine response was to confuse the builders' language and scatter them across the earth — the etiological explanation for the diversity of human languages and the dispersal of nations. The name Babel (<em>confusion</em>) plays on the Hebrew root <em>balal</em>, to confuse, though in Akkadian Babylon means <em>gate of god</em>. The narrative of Babel frames the table of nations in Genesis 10 and establishes the condition of divided, dispersed humanity that the Abrahamic covenant (Genesis 12) begins to address — eventually finding its reversal in the Pentecost event of Acts 2, where divided languages are momentarily transcended.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "babel-tower-of", "isbe": "babel-tower-of"},
        "key_refs": ["Genesis 11:1", "Genesis 11:4", "Genesis 11:9"]
    },
    "babylon": {
        "id": "babylon",
        "term": "Babylon",
        "category": "places",
        "intro": "<p>Babylon (the Greek form of the Semitic <em>Babilu</em>, meaning <em>gate of God</em>) was the capital of the Babylonian Empire and one of the most significant cities in biblical history. Situated on the Euphrates in the plain of Shinar in southern Mesopotamia, it was already ancient when it rose to imperial dominance under Nebuchadnezzar II (r. 605–562 B.C.), who rebuilt it into one of the ancient world's most magnificent cities. The hanging gardens and the great ziggurat Etemenanki were among its wonders. Its theological significance in the Old Testament is dominated by the Babylonian exile — the deportation of the Jewish people that Jeremiah prophesied would last seventy years (Jeremiah 25:12) and that Cyrus's decree ended in 538 B.C.</p><p>In prophetic literature, Babylon functions both as a historical empire and as a theological symbol of human arrogance, oppression, and enmity toward God's people. Isaiah 13–14 and 47, Jeremiah 50–51, and Daniel all address Babylon's rise and fall. In the New Testament, 1 Peter 5:13 uses Babylon as a cryptonym, almost certainly for Rome — the imperial power of Peter's day — and Revelation 17–18 develops Babylon as the supreme symbol of the world's system opposed to God, whose fall is announced with the words <em>Babylon the great is fallen, is fallen</em>.</p>",
        "hitchcock_meaning": "same as Babel; confusion",
        "source_ids": {"easton": "babylon", "smith": "babylon"},
        "key_refs": ["Jeremiah 25:12", "Jeremiah 50:2", "Daniel 2:31", "Revelation 18:2"]
    },
    "babylon-kingdom-of": {
        "id": "babylon-kingdom-of",
        "term": "Babylon, kingdom of",
        "category": "places",
        "intro": "<p>The kingdom of Babylon, also called the land of the Chaldeans, was the Neo-Babylonian Empire that rose to dominance under Nabopolassar and his son Nebuchadnezzar II following the fall of Assyria. Its heartland was southern Mesopotamia — the ancient region of Sumer and Akkad — with Babylon as its capital. The empire stretched from the Persian Gulf to the Mediterranean, incorporating Judah, Syria, and Egypt's border regions into its sphere of control. Nebuchadnezzar's campaigns against Jerusalem in 605, 597, and 586 B.C. resulted in the destruction of the temple and the deportation of the Jewish population in successive waves.</p><p>The biblical characterization of Babylon as an instrument of divine judgment on Israel (Jeremiah, Ezekiel, Daniel) is paired with equally strong prophecies of Babylon's own eventual judgment and destruction (Isaiah 43–47; Jeremiah 50–51). The empire fell to Cyrus the Great of Persia in 539 B.C., as Daniel had foretold through the vision of the statue and the hand writing on the wall. The Chronicler's account (2 Chronicles 36:20–23) frames the entire Babylonian exile within the larger story of divine faithfulness — ending with Cyrus's decree and the return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "babylon-kingdom-of"},
        "key_refs": ["Jeremiah 24:5", "Isaiah 43:14", "2 Chronicles 36:20", "Daniel 5:30"]
    },
    "babylonish-garment": {
        "id": "babylonish-garment",
        "term": "Babylonish garment",
        "category": "concepts",
        "intro": "<p>A Babylonish garment was a richly embroidered or woven robe produced at Babylon and prized throughout the ancient world for its elaborate ornamentation. Babylon was renowned in antiquity for its luxury textile industry, producing garments of exceptional quality and color that were traded across the Near East. Such a garment was among the items Achan confessed to hiding when he violated the ban (herem) on the spoils of Jericho: <em>I saw among the spoils a goodly Babylonish garment, and two hundred shekels of silver, and a wedge of gold</em> (Joshua 7:21).</p><p>The episode of Achan's sin explains Israel's surprising defeat at Ai after the miraculous victory at Jericho. Achan's covetousness — triggered by the sight of a beautiful foreign garment — illustrates the danger of what the eye sees and the hand desires in violation of divine command. The garment's Babylonian origin made it emblematic of the tempting luxury of foreign culture, the same cultural seduction the prophets would later warn against as Israel encountered greater wealth and power in the nations surrounding her.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "babylonish-garment", "smith": "babylonish-garment", "isbe": "babylonish-garment"},
        "key_refs": ["Joshua 7:21"]
    },
    "baca-valley-of": {
        "id": "baca-valley-of",
        "term": "Baca, Valley of",
        "category": "places",
        "intro": "<p>The Valley of Baca appears in Psalm 84:6, where the pilgrim passing through it makes it a place of springs — <em>the rain also filleth the pools</em>. The Hebrew <em>baca</em> may mean weeping or the balsam tree, and the valley has been understood either as a real arid valley on the pilgrim route to Jerusalem or as a metaphor for a place of hardship and tears. The Revised Version renders it the <em>valley of weeping</em>, while the margin suggests the <em>valley of balsam trees</em>.</p><p>The passage is set within the great pilgrimage psalm celebrating the blessedness of those who dwell in God's house and whose hearts are set on the ways to Zion. The Valley of Baca becomes a place of transformation in the psalm's vision: the pilgrim who passes through it does not merely endure it but converts it — their very passing through a desolate place produces springs. The image has been widely understood in Christian devotion as a picture of spiritual transformation, where trial becomes the occasion for grace.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baca-valley-of"},
        "key_refs": ["Psalms 84:6"]
    },
    "backbite": {
        "id": "backbite",
        "term": "Backbite",
        "category": "concepts",
        "intro": "<p>Backbiting in Scripture refers to speaking evil of someone in their absence — malicious gossip or slander that undermines a person's reputation without confronting them directly. Psalm 15:3 includes <em>he that backbiteth not with his tongue</em> among the characteristics of the person who may dwell on God's holy hill, placing freedom from slander among the marks of genuine integrity. Proverbs 25:23 notes that a backbiting tongue produces angry countenance, just as the north wind produces rain.</p><p>Paul lists backbiting among the vices that characterized pagan society in its rejection of God (Romans 1:30) and expresses concern that he will find it present in the Corinthian church (2 Corinthians 12:20), alongside contentions, envyings, and other relational sins. The biblical vocabulary for this sin — including slander, tale-bearing, and whispering — reflects a consistent concern with the destructive social power of speech used to harm rather than build up. James 3 and 4 develop the theme most fully: the tongue set on fire by hell, and the commandment not to speak evil of one another.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "backbite", "isbe": "backbite"},
        "key_refs": ["Psalms 15:3", "Proverbs 25:23", "Romans 1:30", "2 Corinthians 12:20"]
    },
    "backslide": {
        "id": "backslide",
        "term": "Backslide",
        "category": "concepts",
        "intro": "<p>Backsliding refers to a falling away or apostasy from a previously held religious commitment — a drawing back from the living God into sin, unbelief, or idolatry. The term appears prominently in Jeremiah and Hosea as a description of Israel's recurring pattern of covenant unfaithfulness: <em>The backsliding Israel hath justified herself more than treacherous Judah</em> (Jeremiah 3:11). Proverbs 14:14 notes that the backslider in heart shall be filled with his own ways — the consequences of departure from God are self-generated.</p><p>In the New Testament, the concept appears without the specific Hebrew term in warnings about apostasy and falling away. Paul warns of a coming departure from the faith (2 Thessalonians 2:3; 1 Timothy 4:1), and the writer of Hebrews devotes extensive argument to the danger and irrecoverability of deliberate apostasy (Hebrews 6:4–6; 10:26–31, 38–39). The consistent biblical pattern treats backsliding not as inevitable but as a mortal danger with genuine remedies: confession, repentance, and return to God, as Jeremiah 3:22 and Hosea 14:1–4 make plain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "backslide", "isbe": "backslide"},
        "key_refs": ["Proverbs 14:14", "Jeremiah 3:11", "Hebrews 6:4", "Hebrews 10:38"]
    },
    "badger": {
        "id": "badger",
        "term": "Badger",
        "category": "concepts",
        "intro": "<p>Badger is the traditional English rendering of the Hebrew <em>tachash</em>, used to describe the material for the outer covering of the tabernacle and the protective coverings for the ark and sacred vessels during transport (Exodus 25:5; 26:14; Numbers 4:6–25). The identification of <em>tachash</em> with the European badger is almost certainly incorrect for geographical reasons, and modern scholarship has proposed alternatives including dugong (sea cow), dolphin, porpoise, or a type of fine leather. The Septuagint translates the term as <em>hyakinthine</em> (blue or violet colored), suggesting a dyed material.</p><p>Ezekiel 16:10 refers to God clothing Jerusalem with <em>badgers' skin</em> (tachash) sandals, using the material as a symbol of fine, luxurious provision. Whatever the precise identification, tachash was evidently a durable, waterproof, and perhaps distinctive material — suitable for protecting the most sacred objects of Israel's worship from the elements during the wilderness journeys.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "badger", "isbe": "badger"},
        "key_refs": ["Exodus 25:5", "Exodus 26:14", "Numbers 4:6"]
    },
    "bag": {
        "id": "bag",
        "term": "Bag",
        "category": "concepts",
        "intro": "<p>Bags in Scripture refer to several distinct types of containers used for carrying money, goods, or provisions. The cone-shaped pocket in which Naaman bound two talents of silver is mentioned in 2 Kings 5:23; the Hebrew <em>tsror</em> denotes a small bundle or purse used to carry coins (Deuteronomy 25:13; Proverbs 16:11; Micah 6:11). Isaiah 3:22 refers to women's bags among the ornamental accessories the prophet announces will be taken away in judgment. The Greek <em>balantion</em> in Luke's Gospel denotes a purse or money bag.</p><p>Haggai 1:6 employs the image of a bag with holes — earning wages only to put them into a perforated bag — as a vivid picture of the economic futility the post-exilic community experienced while neglecting the rebuilding of the temple. Judas Iscariot carried the disciples' common money bag (John 12:6; 13:29), and his betrayal of Jesus for thirty pieces of silver is foreshadowed in John's note that he was a thief who pilfered from what was put into it.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bag", "smith": "bag", "isbe": "bag"},
        "key_refs": ["2 Kings 5:23", "Deuteronomy 25:13", "Haggai 1:6"]
    },
    "bahurim": {
        "id": "bahurim",
        "term": "Bahurim",
        "category": "places",
        "intro": "<p>Bahurim (meaning <em>young men</em> or <em>choice warriors</em>) was a village east of Jerusalem on the road to the Jordan, in the territory of Benjamin. It appears several times in the narrative of David's reign. After Abner took Michal from Paltiel and returned her to David, Paltiel followed her weeping as far as Bahurim before turning back (2 Samuel 3:16). When David fled Jerusalem during Absalom's rebellion, Shimei son of Gera came from Bahurim, cursing David and throwing stones at him (2 Samuel 16:5) — an act David forbade his men to punish, later regretting his leniency in his deathbed instructions to Solomon.</p><p>Jonathan and Ahimaaz hid in a well at Bahurim while carrying intelligence from Hushai to David, concealed by a woman who spread a covering over the well (2 Samuel 17:18). The village is identified with the modern Ras et-Tmim northeast of Jerusalem, and it was home to Azmaveth, one of David's thirty heroes (2 Samuel 23:31).</p>",
        "hitchcock_meaning": "choice; warlike; valiant",
        "source_ids": {"easton": "bahurim", "smith": "bahurim", "isbe": "bahurim"},
        "key_refs": ["2 Samuel 3:16", "2 Samuel 16:5", "2 Samuel 17:18"]
    },
    "bajith": {
        "id": "bajith",
        "term": "Bajith",
        "category": "places",
        "intro": "<p>Bajith (meaning <em>house</em>) is mentioned in Isaiah 15:2 in the oracle against Moab: <em>He is gone up to Bajith, and to Dibon, the high places, to weep</em>. The verse describes the Moabites going to their temples and high places in mourning over the coming destruction. Most modern translations render <em>bajith</em> simply as <em>the house</em> (referring to a temple or sanctuary), and some scholars understand it not as a proper place-name but as the common noun for a house or temple of Moab.</p><p>If a proper name, Bajith may designate a specific Moabite cultic site associated with a national temple. Its pairing with Dibon — a well-known Moabite city — suggests a location in the Moabite plateau east of the Dead Sea. The Isaiah oracle describes the comprehensive mourning that would sweep through Moab's cities and sanctuaries in the face of Assyrian invasion.</p>",
        "hitchcock_meaning": "a house",
        "source_ids": {"easton": "bajith", "smith": "bajith", "isbe": "bajith"},
        "key_refs": ["Isaiah 15:2"]
    },
    "bake": {
        "id": "bake",
        "term": "Bake",
        "category": "concepts",
        "intro": "<p>Baking bread in ancient Israel was a daily domestic task typically performed by women, though professional bakers operated in towns and royal households. Genesis 18:6 records Sarah kneading three seahs of fine flour and baking cakes when Abraham received the three visitors at Mamre; Leviticus 26:26 uses the image of ten women baking in a single oven as a sign of famine and scarcity. Samuel warns that a king will take daughters to be bakers (1 Samuel 8:13), and Jeremiah 37:21 records that the prophet was given a daily ration of bread from the bakers' street in Jerusalem during his imprisonment.</p><p>The Hebrew word <em>aphah</em> and its cognates cover the full range of baking activity. Ancient ovens were heated clay pots or stone-lined pits fueled by wood or dried grass; Hosea 7:4–6 uses the image of an oven heated by a baker as a metaphor for the smoldering passions of Israel's political intrigues. The daily provision of manna in the wilderness and the priestly showbread replaced the ordinary cycle of baking for the Israelite community in the desert period, establishing bread as both a subsistence staple and a vehicle of divine provision.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bake", "smith": "bake"},
        "key_refs": ["Genesis 18:6", "Leviticus 26:26", "Hosea 7:4"]
    },
    "bake-meats": {
        "id": "bake-meats",
        "term": "Bake-meats",
        "category": "concepts",
        "intro": "<p>Bake-meats is an archaic English term for baked provisions or confections prepared by a baker. It appears in Genesis 40:17 in the account of the chief baker's dream while imprisoned with Joseph in Egypt: he dreamed of three baskets of white bread on his head, with the top basket containing all manner of bake-meats (<em>works of the baker</em>) for Pharaoh, which birds were eating. Joseph's interpretation of the dream — the three baskets representing three days, after which Pharaoh would hang the baker and birds would eat his flesh — was fulfilled precisely on Pharaoh's birthday.</p><p>The term represents the range of goods a royal court baker would prepare: fine breads, pastries, and confections. The contrast between the cupbearer's dream (pressing grapes into Pharaoh's cup) and the baker's dream (birds consuming the provisions before they reach Pharaoh) underlies the contrasting interpretations Joseph gave — restoration to office for the one, death for the other.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bake-meats"},
        "key_refs": ["Genesis 40:17"]
    },
    "balaam": {
        "id": "balaam",
        "term": "Balaam",
        "category": "people",
        "intro": "<p>Balaam (meaning <em>lord of the people</em> or according to some interpreters <em>foreigner</em> or <em>glutton</em>) was a Mesopotamian diviner from Pethor on the Euphrates, hired by Balak king of Moab to curse Israel as they camped in the plains of Moab before the conquest. The narrative in Numbers 22–24 is one of the most distinctive in the Pentateuch: God permitted Balaam to go but intervened through a speaking donkey and an angel to correct his course. Despite Balak's repeated attempts to prompt a curse, Balaam could only bless Israel, delivering four oracles of increasing grandeur — culminating in the Messianic star prophecy of Numbers 24:17.</p><p>Yet the same narrative tradition associates Balaam with the counsel that introduced Baal-peor worship into Israel through Moabite and Midianite women (Numbers 31:16; Revelation 2:14) — the strategy that accomplished through seduction what could not be accomplished through direct cursing. This double profile — the man who spoke God's word faithfully yet counseled Israel's corruption for payment — made Balaam the paradigmatic example of false prophecy motivated by greed. Peter, Jude, and Revelation each invoke <em>the way of Balaam</em> or <em>the error of Balaam</em> as a warning against mercenary religion.</p>",
        "hitchcock_meaning": "the ancient of the people; the stranger who devours",
        "source_ids": {"easton": "balaam", "smith": "balaam", "isbe": "balaam"},
        "key_refs": ["Numbers 22:5", "Numbers 23:7", "2 Peter 2:15", "Revelation 2:14"]
    },
    "baladan": {
        "id": "baladan",
        "term": "Baladan",
        "category": "people",
        "intro": "<p>Baladan was the father of Merodach-baladan, king of Babylon. He is mentioned only in the patronymic: <em>Merodach-baladan, the son of Baladan, king of Babylon</em> (2 Kings 20:12; Isaiah 39:1). Merodach-baladan sent envoys with letters and gifts to Hezekiah when the Judahite king recovered from his illness — an embassy that likely had political motives, as Merodach-baladan was at that time seeking allies against Assyrian power. Hezekiah showed the Babylonian envoys all his treasures, prompting Isaiah's prophecy that all those treasures would one day be carried to Babylon.</p><p>Baladan himself is otherwise unknown in the biblical text. His son Merodach-baladan is well attested in Assyrian and Babylonian records as the Chaldean chieftain who twice seized the Babylonian throne and proved one of Sargon II's most persistent opponents. Baladan's significance is entirely derived from his role as the named father of this historically prominent king.</p>",
        "hitchcock_meaning": "one without judgment",
        "source_ids": {"easton": "baladan", "smith": "baladan", "isbe": "baladan"},
        "key_refs": ["2 Kings 20:12", "Isaiah 39:1"]
    },
    "balah": {
        "id": "balah",
        "term": "Balah",
        "category": "places",
        "intro": "<p>Balah was a city in the southern territory of the tribe of Simeon, listed in Joshua 19:3 among the towns of Simeon's inheritance within Judah's allotment. It is also called Bilhah in 1 Chronicles 4:29, reflecting variant transmission of the name in the Hebrew text, and is possibly the same as Baalah in Joshua 15:29. The Simeonite towns in this region lay in the arid Negev south of Beer-sheba, a zone susceptible to the encroachment of desert peoples and subject to periodic resettlement.</p><p>Balah receives no further narrative treatment in Scripture and is known only from its listing in the tribal boundary and city records of Joshua and Chronicles. Like many Simeonite settlements, it likely became absorbed into the territory of Judah as that tribe's dominance in the south grew and Simeon's distinct identity diminished.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "balah", "smith": "balah", "isbe": "balah"},
        "key_refs": ["Joshua 19:3", "1 Chronicles 4:29"]
    },
    "balak": {
        "id": "balak",
        "term": "Balak",
        "category": "people",
        "intro": "<p>Balak (meaning <em>empty</em> or <em>spoiler</em>) was the son of Zippor and king of Moab when Israel camped in the plains of Moab before the conquest of Canaan. Alarmed by Israel's military victories over Sihon and Og, Balak sent to the Euphrates to hire Balaam to curse Israel, believing that Balaam's blessing and cursing had decisive power. The narrative of Numbers 22–24 shows Balak making three attempts to position Balaam advantageously — at Bamoth-baal, Pisgah, and Peor — each time receiving a blessing rather than a curse.</p><p>Balak's frustration mounts through the narrative until he dismisses Balaam without the payment he promised. In Joshua 24:9, Joshua recounts Balak's hostility in his rehearsal of Israel's history, and Micah 6:5 invokes Balak and Balaam together as examples of how God turned a potential curse into blessing. The book of Revelation's letter to Pergamum (Revelation 2:14) accuses false teachers of holding to the teaching of Balaam who taught Balak to put a stumbling block before Israel — connecting Balak to the subsequent Baal-peor apostasy.</p>",
        "hitchcock_meaning": "who lays waste or destroys",
        "source_ids": {"easton": "balak", "smith": "balak", "isbe": "balak"},
        "key_refs": ["Numbers 22:2", "Numbers 22:4", "Joshua 24:9", "Micah 6:5"]
    },
    "balance": {
        "id": "balance",
        "term": "Balance",
        "category": "concepts",
        "intro": "<p>The balance or scales was the primary instrument of commercial weight measurement in the ancient Near East and appears throughout Scripture both as a practical object and as a moral symbol. The Hebrew <em>kaneh</em> (measuring rod or scale) and <em>moznaim</em> (balance, literally <em>two ears</em>) refer to the two-pan balance suspended from a central beam. Leviticus 19:36 commands just balances and just weights as an expression of covenant ethics in commerce. Proverbs 11:1 declares that a false balance is an abomination to the LORD but a just weight is his delight.</p><p>The theological range of the metaphor is wide. Isaiah 46:6 pictures idolaters weighing gold in the balance to hire a goldsmith. Ezekiel 5:1 uses the balance to weigh divided portions of the prophet's hair in an enacted sign. Daniel 5:27 announces God's judgment on Belshazzar with the word <em>Tekel</em> — <em>thou art weighed in the balances, and art found wanting</em>. Revelation 6:5 places a balance in the hand of the rider on the black horse, symbolizing the economic scarcity of the third seal.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "balance", "isbe": "balance"},
        "key_refs": ["Leviticus 19:36", "Proverbs 11:1", "Daniel 5:27", "Revelation 6:5"]
    },
    "baldness": {
        "id": "baldness",
        "term": "Baldness",
        "category": "concepts",
        "intro": "<p>Baldness in ancient Israel could arise from natural causes, disease, or as a deliberately induced sign of mourning and grief. Natural baldness was uncommon and apparently considered unusual enough to be remarked upon — the taunting of Elisha as <em>bald head</em> (2 Kings 2:23) reflects this. Priestly law distinguished between the bald-headed man whose hair fell from the front (forehead) or the back, declaring he was clean as long as no reddish-white infection appeared (Leviticus 13:40–44).</p><p>Induced baldness — shaving the head — was a recognized sign of mourning across the ancient Near East (Job 1:20; Micah 1:16) and appears in the covenant curses of Deuteronomy 28:35 and in prophetic laments. Isaiah 3:24 lists baldness as a substitution for well-set hair among the judgments that would come upon the daughters of Zion. Ezekiel 5:1 uses shaving the head as an enacted prophetic sign of Jerusalem's fate. The Nazirite vow, by contrast, involved refraining from cutting hair as a sign of consecration, making baldness in that context a marker of vow completion rather than mourning.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baldness", "smith": "baldness", "isbe": "baldness"},
        "key_refs": ["2 Kings 2:23", "Isaiah 3:24", "Ezekiel 5:1", "Jeremiah 7:29"]
    },
    "balm": {
        "id": "balm",
        "term": "Balm",
        "category": "concepts",
        "intro": "<p>Balm in Scripture refers to an aromatic resinous substance prized for its medicinal and trade value. The Hebrew <em>tsori</em> (rendered balm in the KJV) is a product of Gilead, referred to in Jeremiah 8:22 and 46:11 as a medicine famous for its healing properties. Gilead east of the Jordan was known for its medicinal plants, and balm of Gilead became a byword for restorative medicine. The balm carried by Ishmaelite traders passing through Dothan — spices, balm, and myrrh going down to Egypt — was among the goods that provided Joseph's brothers the opportunity to sell him into slavery (Genesis 37:25).</p><p>Jacob sent balm among the gifts given to the unnamed official in Egypt (Genesis 43:11) and Ezekiel 27:17 lists balm among Judah's exports to Tyre. Jeremiah's rhetorical question — <em>Is there no balm in Gilead; is there no physician there?</em> (Jeremiah 8:22) — uses the famous remedy as a figure for the spiritual healing that Israel refuses, though the remedy is available. The passage became foundational in Christian hymnody as a metaphor for the healing available in Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "balm", "smith": "balm", "isbe": "balm"},
        "key_refs": ["Genesis 37:25", "Jeremiah 8:22", "Jeremiah 46:11", "Ezekiel 27:17"]
    },
    "bamah": {
        "id": "bamah",
        "term": "Bamah",
        "category": "places",
        "intro": "<p>Bamah (meaning <em>a height</em> or <em>high place</em>) is the Hebrew term for an elevated site used for worship, appearing as a common noun throughout the historical and prophetic books and as a proper name in a few passages. Ezekiel 20:29 uses the word pointedly, quoting God's question to Israel: <em>What is the high place whereunto ye go? And the name thereof is called Bamah unto this day</em> — a divine challenge to the continuing practice of high place worship long after the Sinai covenant prohibited it.</p><p>Numbers 22:41 mentions Bamoth-baal as the place where Balak first brought Balaam, and the term Bamah at Ezekiel 36:2 is used by the enemies of Israel to taunt the land. The high places were a persistent problem in Israel's religious history: built originally as local worship sites, they became associated with Canaanite fertility rites and survived even through the reforms of good kings like Asa and Jehoshaphat, who removed the great altars but left the bamoth standing. Only Hezekiah and Josiah conducted comprehensive destructions of the high places.</p>",
        "hitchcock_meaning": "an eminence or high place",
        "source_ids": {"easton": "bamah", "smith": "bamah", "isbe": "bamah"},
        "key_refs": ["Ezekiel 20:29", "Numbers 22:41"]
    },
    "bamoth": {
        "id": "bamoth",
        "term": "Bamoth",
        "category": "places",
        "intro": "<p>Bamoth (meaning <em>heights</em>) was the forty-seventh station of the Israelites in the wilderness, recorded in Numbers 21:19–20 as the stopping point between Nahaliel and the top of Pisgah overlooking the valley of Moab. The full form Bamoth-baal (heights of Baal) appears in Numbers 22:41 and Joshua 13:17, indicating that this region of high ground in Moab was associated with Baal worship. The name reflects the common Canaanite practice of locating sacred sites on elevated ground.</p><p>The Israelites passed through Bamoth as they approached the territory of Sihon and Og east of the Jordan, moving toward their final encampment on the plains of Moab opposite Jericho. The station is mentioned in the route itinerary of Numbers 33 and represents the final stages of the forty-year wilderness journey before the conquest began.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bamoth"},
        "key_refs": ["Numbers 21:19", "Numbers 21:20"]
    },
    "bamoth-baal": {
        "id": "bamoth-baal",
        "term": "Bamoth-baal",
        "category": "places",
        "intro": "<p>Bamoth-baal (meaning <em>heights of Baal</em>) was a place in the plains of Moab or on the plateau north of the Arnon, mentioned in Numbers 22:41 as the first vantage point from which Balak brought Balaam to view and curse Israel. From this height Balaam could see the outermost edge of the Israelite camp. The site is also listed in Joshua 13:17 among the cities in the plain assigned to the tribe of Reuben in the Transjordanian allotment, and Numbers 21:28 connects it with Heshbon.</p><p>Like many sites in Moabite territory, Bamoth-baal reflects the pervasive presence of Baal worship in the elevated places of the region. Its use as the first viewing platform in the Balaam narrative establishes the thematic connection between high places, Baal, and the attempt to invoke supernatural cursing against Israel — all elements that will recur in the Baal-peor episode that follows the Balaam oracles.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bamoth-baal"},
        "key_refs": ["Numbers 22:41", "Joshua 13:17"]
    },
    "bands": {
        "id": "bands",
        "term": "Bands",
        "category": "concepts",
        "intro": "<p>Bands in Scripture carry several metaphorical meanings relating to binding, connection, and restraint. Hosea 11:4 describes God drawing Israel with <em>bands of love</em> and cords of a man — a tender image of divine guidance as opposed to coercive control. Psalm 2:3 puts the rebellious nations' cry of <em>Let us break their bands asunder, and cast away their cords</em> as a figure of throwing off God's sovereign rule. The contrast in these two uses — bands of love versus bonds to be broken — captures the ambivalence the concept carries.</p><p>In the New Testament, Paul uses the image of bands positively for the body of Christ. Colossians 2:19 describes the head from which the whole body, held together by joints and bands, grows with the growth of God. Colossians 3:14 calls love the <em>bond of perfectness</em> that unites all virtues. Ephesians 4:3 urges maintaining the unity of the Spirit in the bond of peace. The image of Ezekiel 34:27 — breaking the bands of the yoke — becomes a picture of liberation from oppressive servitude, reversing the negative connotation of constraint into an image of redemptive freedom.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bands"},
        "key_refs": ["Hosea 11:4", "Psalms 2:3", "Colossians 2:19", "Colossians 3:14"]
    },
    "bani": {
        "id": "bani",
        "term": "Bani",
        "category": "people",
        "intro": "<p>Bani (meaning <em>built</em>) is the name of several men in the Old Testament, most prominent in the post-exilic records. One was a Gadite, one of David's thirty warriors listed in 2 Samuel 23:36 (and possibly the Mebunnai of 2 Samuel 23:27 in 1 Chronicles 11:29). Others named Bani include ancestors of families who returned from Babylonian exile (Ezra 2:10; Nehemiah 7:15), and several men who had taken foreign wives and are listed in Ezra 10:29, 34, and 38. A Levite named Bani assisted in explaining the law to the people during Ezra's great reading (Nehemiah 8:7) and sealed the covenant (Nehemiah 10:13).</p><p>The frequency of the name Bani in the post-exilic records reflects its use as a clan identifier rather than necessarily a single individual. The family of Bani contributed significantly to the returnee community, with their ancestor's name heading a recognizable clan group throughout the Persian period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bani", "smith": "bani", "isbe": "bani"},
        "key_refs": ["2 Samuel 23:36", "Ezra 2:10", "Nehemiah 8:7"]
    },
    "banner": {
        "id": "banner",
        "term": "Banner",
        "category": "concepts",
        "intro": "<p>Banners and standards in ancient Israel served both military and religious functions. The Hebrew <em>degel</em> denotes the larger standards by which three-tribe divisions of the Israelite camp were organized in the wilderness (Numbers 1:52; 2:2–31), with four great standards marking the four quarters of the camp around the tabernacle. The <em>nes</em> (signal or ensign) was a pole raised on a high place as a rallying point for troops or as a signal visible from a distance. Moses raised a bronze serpent on a <em>nes</em> in the wilderness (Numbers 21:8–9).</p><p>The theological use of banner imagery is especially rich in the Psalms and prophets. God is called Jehovah-nissi — <em>the LORD is my banner</em> — at the defeat of Amalek (Exodus 17:15). Song of Solomon 2:4 declares that the king's <em>banner over me was love</em>, an image of protective and claiming love. Isaiah develops the eschatological use most fully: a <em>root of Jesse</em> will stand as an ensign for the peoples, and to it the nations will seek (Isaiah 11:10). The banner imagery thus moves from military organization to a messianic symbol of universal gathering.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "banner", "smith": "banner", "isbe": "banner"},
        "key_refs": ["Numbers 2:2", "Exodus 17:15", "Isaiah 11:10"]
    },
    "banquet": {
        "id": "banquet",
        "term": "Banquet",
        "category": "concepts",
        "intro": "<p>Banquets and feasts in Scripture served social, religious, and celebratory functions in both testaments. The book of Esther pivots on two banquets hosted by Ahasuerus and two intimate banquets hosted by Esther for the king and Haman, at the second of which Esther revealed Haman's plot against her people (Esther 5–7). The hospitality banquet appears at critical narrative moments: Abraham's feast for his three visitors, the celebration at Jacob and Laban's covenant, the great feasts of Solomon's dedication. Peter identifies the pagan <em>banqueting</em> of the Gentile world as a mark of former life to be abandoned (1 Peter 4:3).</p><p>Theologically, the banquet becomes a primary metaphor for the messianic age. Isaiah 25:6 describes the LORD of hosts making for all peoples on his mountain a feast of rich food and well-aged wine. Jesus's parables of the great banquet (Luke 14:15–24) and the wedding feast (Matthew 22:1–14) cast the kingdom of God as a lavish meal to which many are invited but few respond. The marriage supper of the Lamb (Revelation 19:9) brings the banquet imagery to its eschatological culmination.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "banquet", "isbe": "banquet"},
        "key_refs": ["Esther 5:1", "Esther 7:1", "Isaiah 25:6", "Revelation 19:9"]
    },
    "baptism-for-the-dead": {
        "id": "baptism-for-the-dead",
        "term": "Baptism for the dead",
        "category": "concepts",
        "intro": "<p>Baptism for the dead is mentioned only once in the New Testament, in 1 Corinthians 15:29: <em>Else what shall they do which are baptized for the dead, if the dead rise not at all? why are they then baptized for the dead?</em> Paul's use of the practice is rhetorical rather than prescriptive — he invokes it as evidence that even those who denied the resurrection implicitly acted as if the dead could benefit from the rites of the living. He does not endorse or explain the practice but uses it as an ad hominem argument for the resurrection.</p><p>The interpretation of the verse is among the most disputed in the Pauline letters, with over two hundred proposed explanations in the scholarly literature. The most common readings include: baptism performed vicariously on behalf of deceased catechumens who died before receiving it; baptism performed in the hope of reunion with deceased believers; or baptism performed as a symbolic identification with the death and resurrection of Christ that would be meaningless without an actual resurrection. The practice itself, whatever its precise form, does not appear elsewhere in the New Testament, and the mainstream Christian tradition has not adopted it as a legitimate rite.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baptism-for-the-dead", "isbe": "baptism-for-the-dead"},
        "key_refs": ["1 Corinthians 15:29"]
    },
    "baptism-of-christ": {
        "id": "baptism-of-christ",
        "term": "Baptism of Christ",
        "category": "concepts",
        "intro": "<p>The baptism of Jesus by John in the Jordan River marks the inauguration of Jesus's public ministry and is recorded in all four Gospels. Matthew 3:13–17 presents the fullest account, including Jesus's explanation to John — <em>suffer it to be so now: for thus it becometh us to fulfil all righteousness</em> — in response to John's hesitation to baptize the one greater than himself. At the moment of Jesus's baptism, the heavens opened, the Spirit descended as a dove, and a divine voice declared: <em>This is my beloved Son, in whom I am well pleased</em> — the trinitarian disclosure that frames the entire subsequent ministry.</p><p>Jesus also uses the term baptism metaphorically in Luke 12:50 to describe his coming passion: <em>I have a baptism to be baptized with; and how am I straitened till it be accomplished!</em> This baptism of suffering — his death and burial — corresponds in Paul's theology to the believer's baptism into Christ's death and resurrection (Romans 6:3–4). The baptism of Christ thus functions both as a historical inaugural event and as a theological type of the death and new life that Christian baptism signifies.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baptism-of-christ"},
        "key_refs": ["Matthew 3:15", "Matthew 3:17", "Luke 12:50"]
    },
    "baptism-christian": {
        "id": "baptism-christian",
        "term": "Baptism, Christian",
        "category": "concepts",
        "intro": "<p>Christian baptism is an ordinance instituted by Christ in the Great Commission — <em>Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit</em> (Matthew 28:19) — and administered throughout the book of Acts as the rite of incorporation into the Christian community. It is distinguished from Jewish proselyte baptism and from John's baptism of repentance by its trinitarian formula and its connection to faith in the risen Christ and reception of the Holy Spirit.</p><p>Paul's theology of baptism in Romans 6:3–4 and Colossians 2:12 presents it as a sign and seal of union with Christ in his death and resurrection — the believer is buried with Christ through baptism into death and raised with him to new life. The relation between the outward rite and inward reality is treated differently in the traditions: some understand baptism as instrumental (effecting what it signifies) while others treat it as a public declaration of grace already received. Peter's language in 1 Peter 3:21 — <em>baptism doth also now save us... not the putting away of the filth of the flesh, but the answer of a good conscience toward God</em> — has been foundational in this discussion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baptism-christian"},
        "key_refs": ["Matthew 28:19", "Romans 6:3", "Colossians 2:12", "1 Peter 3:21"]
    },
    "baptism-johns": {
        "id": "baptism-johns",
        "term": "Baptism, John's",
        "category": "concepts",
        "intro": "<p>John's baptism was a rite of repentance and preparation for the coming kingdom, distinct from both Jewish proselyte baptism and the later Christian ordinance. John administered it in the Jordan River to those who confessed their sins and turned from them in anticipation of the one who would come after him and baptize with the Holy Spirit and fire (Matthew 3:11). Jesus himself submitted to John's baptism, not because he needed repentance but to <em>fulfil all righteousness</em> — to identify fully with sinful humanity and inaugurate his messianic mission.</p><p>The book of Acts records that John's baptism remained in circulation decades after Pentecost. Apollos, an eloquent Alexandrian who taught about Jesus accurately, knew only the baptism of John and needed fuller instruction from Priscilla and Aquila (Acts 18:24–26). At Ephesus, Paul encountered disciples who had received only John's baptism, were unaware of the Holy Spirit, and were subsequently baptized in the name of the Lord Jesus and received the Spirit through Paul's laying on of hands (Acts 19:1–7). John's baptism was thus preparatory and incomplete — sufficient for its moment but pointing toward a fuller reality it did not itself convey.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "baptism-johns"},
        "key_refs": ["Matthew 3:11", "Acts 18:24", "Acts 19:4"]
    },
    "bar": {
        "id": "bar",
        "term": "Bar",
        "category": "concepts",
        "intro": "<p>Bar in Scripture refers to several different objects depending on context. As a wooden or iron beam, it was the means by which a gate or door was secured (Nehemiah 3:3, 6, 13–15; Isaiah 45:2). In Job 38:10 God asks whether Job decreed the sea's bars and doors — the bars here being the limits set on the ocean's boundaries. Jonah 2:6 uses the image of earth's bars closing over the prophet in the depth of the sea as a figure of entombment from which God raised him.</p><p>The bar also appears as a structural element of the tabernacle and its frame — horizontal poles (Hebrew <em>beriach</em>) that held the boards of the tabernacle together (Exodus 26:26–29). Isaiah 45:2 speaks of God cutting in sunder the bars of iron as a figure of removing all obstacles before Cyrus. Amos 1:5 pronounces judgment by breaking the bar of Damascus. In each case the bar represents the system that holds things shut or together — whether a city gate, the ocean's bounds, or an empire's defenses.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bar"},
        "key_refs": ["Nehemiah 3:3", "Job 38:10", "Jonah 2:6", "Isaiah 45:2"]
    },
    "bar-jesus": {
        "id": "bar-jesus",
        "term": "Bar-jesus",
        "category": "people",
        "intro": "<p>Bar-jesus (meaning <em>son of Joshua</em> or <em>son of Jesus</em>) was the patronymic of Elymas the sorcerer, a Jewish false prophet attached to Sergius Paulus, the proconsul of Cyprus, at Paphos. When Barnabas and Saul arrived at Paphos during the first missionary journey and the proconsul sought to hear the word of God, Bar-jesus opposed them and tried to turn Sergius Paulus away from the faith. Paul fixed his gaze on him, called him a son of the devil and an enemy of all righteousness, and pronounced blindness upon him (Acts 13:6–12).</p><p>Bar-jesus was immediately struck blind, and when the proconsul saw what happened, he believed — astonished at the teaching of the Lord. The episode marks Paul's first recorded miracle and the effective beginning of his apostolic authority. The name Elymas is thought to derive from an Arabic word meaning <em>sage</em> or <em>wise man</em>, reflecting his role as a court diviner. His confrontation with Paul represents the recurring clash between apostolic power and the magical arts in Acts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bar-jesus", "isbe": "bar-jesus"},
        "key_refs": ["Acts 13:6", "Acts 13:8", "Acts 13:11"]
    },
    "bar-jona": {
        "id": "bar-jona",
        "term": "Bar-jona",
        "category": "people",
        "intro": "<p>Bar-jona (meaning <em>son of Jonah</em> or <em>son of John</em>) is the Aramaic patronymic of Simon Peter, used by Jesus in two key passages. In Matthew 16:17, after Peter's confession that Jesus is the Christ the Son of the living God, Jesus responds: <em>Blessed art thou, Simon Bar-jona: for flesh and blood hath not revealed it unto thee, but my Father which is in heaven.</em> The use of the full Aramaic name at this moment of revelation emphasizes the personal and direct nature of the divine disclosure.</p><p>In John 1:42, Jesus gives Simon the new name Peter (Cephas) at their first meeting: <em>Thou art Simon the son of Jona: thou shalt be called Cephas.</em> The father's name appears as Jonah in Matthew, Jona in John, and John in John 21:15–17 — variations likely representing different Aramaic and Greek forms of the same name. Bar-jona as a designation thus identifies Peter within his family lineage before he received the name by which history knows him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bar-jona"},
        "key_refs": ["Matthew 16:17", "John 1:42"]
    },
    "barabbas": {
        "id": "barabbas",
        "term": "Barabbas",
        "category": "people",
        "intro": "<p>Barabbas (meaning <em>son of Abba</em> or <em>son of a father</em>, with a secondary interpretation of <em>son of shame</em>) was a notorious prisoner held by Pilate at the time of Jesus's trial. Mark 15:7 describes him as one who had committed murder in the insurrection, and Luke 23:19 confirms he had been imprisoned for sedition and murder. John 18:40 adds that he was a robber. Pilate, exercising the Passover custom of releasing a prisoner chosen by the crowd, offered the people a choice between Jesus and Barabbas.</p><p>The crowd's choice of Barabbas over Jesus — instigated by the chief priests — is the culminating irony of the passion narrative in the Synoptic Gospels: the guilty go free while the innocent is condemned to death. Theological reflection has seen in this exchange a enacted parable of substitutionary atonement — the guilty Barabbas walking free because Jesus takes his place. Acts 3:14 recalls the choice starkly: <em>ye denied the Holy One and the Just, and desired a murderer to be granted unto you.</em></p>",
        "hitchcock_meaning": "son of shame, confusion",
        "source_ids": {"easton": "barabbas", "smith": "barabbas", "isbe": "barabbas"},
        "key_refs": ["Matthew 27:16", "Mark 15:7", "John 18:40", "Acts 3:14"]
    },
    "barachel": {
        "id": "barachel",
        "term": "Barachel",
        "category": "people",
        "intro": "<p>Barachel (meaning <em>whom God has blessed</em> or <em>that bows before God</em>) was a Buzite of the family of Ram and the father of Elihu, the fourth and final of Job's friends to speak. His identification as a Buzite places Elihu's family in the territory of Buz, a region associated with the descendants of Abraham's nephew Nahor (Genesis 22:21). Elihu is distinguished from the three earlier friends — Eliphaz, Bildad, and Zophar — both by his youth and by the explicitly named family lineage provided through Barachel.</p><p>Barachel himself appears only in the identification of his son and is otherwise unknown in Scripture. Elihu's extended speeches in Job 32–37 are notable for their different theological approach — he rebukes not only Job but the three friends, and his speeches prepare the way for the divine speeches from the whirlwind that follow.</p>",
        "hitchcock_meaning": "that bows before God",
        "source_ids": {"easton": "barachel", "smith": "barachel", "isbe": "barachel"},
        "key_refs": ["Job 32:2", "Job 32:6"]
    },
    "barachias-berechiah": {
        "id": "barachias-berechiah",
        "term": "Barachias, Berechiah",
        "category": "people",
        "intro": "<p>Barachias (the Greek form of the Hebrew Berechiah, meaning <em>blessed by Jehovah</em> or <em>whom Jehovah has blessed</em>) was the father of the prophet Zechariah and the son of Iddo (Zechariah 1:1, 7). He belongs to the post-exilic priestly lineage, and his son Zechariah was both a prophet and a priest who ministered alongside Haggai in encouraging the rebuilding of the temple after the return from Babylon.</p><p>The name Barachias appears in Matthew 23:35 in a textually disputed context where Jesus speaks of <em>Zacharias son of Barachias, whom ye slew between the temple and the altar.</em> The identification here is debated: it may refer to the Zechariah of 2 Chronicles 24:20–21 (son of Jehoiada), the Zechariah of the prophetic book, or another person of the same name. The verse has generated significant scholarly discussion given the difficulty of reconciling the parentage given in Matthew with the Chronicles account.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barachias-berechiah"},
        "key_refs": ["Zechariah 1:1", "Zechariah 1:7", "Matthew 23:35"]
    },
    "barak": {
        "id": "barak",
        "term": "Barak",
        "category": "people",
        "intro": "<p>Barak (meaning <em>lightning</em>) was the son of Abinoam from Kedesh in Naphtali, the military commander who led Israel's forces against the Canaanite general Sisera under the direction of the prophetess Deborah. When Deborah summoned Barak and delivered the divine command to assemble ten thousand men of Naphtali and Zebulun at Mount Tabor, Barak agreed to go only on condition that Deborah accompany him — a condition she accepted while prophesying that the honor of the victory would go to a woman rather than to him (Judges 4:8–9). At Deborah's signal, Barak led his forces down from Tabor and routed Sisera's nine hundred iron chariots in the Kishon valley.</p><p>Sisera fled on foot and was killed by Jael the wife of Heber the Kenite, fulfilling Deborah's prophecy. The victory is celebrated in the Song of Deborah (Judges 5), one of the oldest and most poetically complex passages in the Old Testament. Despite the qualification attached to his initial response, Barak is listed in Hebrews 11:32 among the heroes of faith whose deeds of valor and military leadership were accomplished through trust in God.</p>",
        "hitchcock_meaning": "thunder; in vain",
        "source_ids": {"easton": "barak", "smith": "barak", "isbe": "barak"},
        "key_refs": ["Judges 4:6", "Judges 4:16", "Judges 5:1", "Hebrews 11:32"]
    },
    "barbarian": {
        "id": "barbarian",
        "term": "Barbarian",
        "category": "concepts",
        "intro": "<p>Barbarian is a Greek word used in the New Testament to denote anyone who did not speak Greek — the term originated in the Greek perception of foreign speech as sounding like <em>bar-bar</em>, an onomatopoeia for unintelligible noise. In Romans 1:14, Paul declares himself a debtor both to Greeks and to barbarians, to the wise and to the unwise — using the Greek-barbarian distinction as a comprehensive way of describing all of humanity as his field of evangelistic responsibility. Colossians 3:11 lists Barbarian alongside Scythian, slave and free, as distinctions dissolved in Christ.</p><p>In Acts 28:1–4, the inhabitants of Malta are called <em>barbaroi</em> — translated as <em>barbarous people</em> — with no negative connotation, simply indicating they were non-Greek speakers. The Maltese showed Paul and his companions unusual kindness, and Paul's survival of a viper's bite led them to regard him as a god. By New Testament times, <em>barbarian</em> was a neutral ethnic-linguistic descriptor rather than the pejorative it later became in Western usage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barbarian", "smith": "barbarian"},
        "key_refs": ["Romans 1:14", "Colossians 3:11", "Acts 28:1", "Acts 28:2"]
    },
    "barber": {
        "id": "barber",
        "term": "Barber",
        "category": "concepts",
        "intro": "<p>The barber appears only once in the Old Testament, in Ezekiel 5:1, where God commands the prophet: <em>take thee a sharp knife, take thee a barber's razor, and cause it to pass upon thine head and upon thy beard.</em> This enacted sign — dividing the shaved hair into three portions representing the three fates of Jerusalem's inhabitants during the siege — assumes the barber's razor as a familiar instrument. Barbers in the ancient Near East were artisans who cut both hair and beards using iron or bronze razors.</p><p>The Nazirite vow prohibited the use of a razor on the head during the period of separation (Numbers 6:5), and Samson's strength was bound up with his Nazirite hair — Delilah's having a man shave off his seven locks (Judges 16:19) represented the profaning of his consecration. Isaiah 7:20 employs the metaphor of the Lord shaving with a hired razor from beyond the Euphrates — the king of Assyria — to describe the complete stripping of the land. The razor and the barber thus serve both practical and potent symbolic functions in the prophetic text.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barber", "isbe": "barber"},
        "key_refs": ["Ezekiel 5:1", "Numbers 6:5", "Judges 16:19"]
    },
    "barefoot": {
        "id": "barefoot",
        "term": "Barefoot",
        "category": "concepts",
        "intro": "<p>Going barefoot in Scripture carried several distinct symbolic meanings. It was a mark of mourning and distress — Isaiah 20:2–4 records the prophet walking naked and barefoot for three years as a sign of the shame that would come upon Egypt and Cush when they were led away captive by Assyria. David went up the ascent of the Mount of Olives barefoot and weeping during Absalom's rebellion (2 Samuel 15:30), a vivid image of royal humiliation. The removal of sandals was also a sign of reverence before the divine presence: God commanded Moses at the burning bush and Joshua before the captain of the Lord's army to remove their sandals, for the ground was holy.</p><p>The transfer or surrender of a sandal had legal significance in Israelite custom: in Ruth 4:7–8, the kinsman-redeemer drew off his sandal to formalize the cession of his right of redemption to Boaz. John the Baptist's declaration that he was unworthy to remove the sandals of the one coming after him (Matthew 3:11; John 1:27) employed the language of the lowest slave service to express the infinite disparity between his ministry and that of Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barefoot", "isbe": "barefoot"},
        "key_refs": ["Isaiah 20:2", "2 Samuel 15:30", "Exodus 3:5"]
    },
    "bariah": {
        "id": "bariah",
        "term": "Bariah",
        "category": "people",
        "intro": "<p>Bariah (meaning <em>fugitive</em>) was one of the five sons of Shemaiah listed in the post-exilic genealogy of 1 Chronicles 3:22, in the royal line of David descended through Zerubbabel. The text notes that Shemaiah had six sons — Hattush, Igal, Bariah, Neariah, Shaphat, and one more — making Bariah a member of the Davidic lineage in the Persian period. His father Shemaiah is counted along with the six sons in the genealogical count as seven.</p><p>Bariah appears only in this genealogical record and receives no individual narrative treatment. His significance is entirely genealogical — he represents the continuation of the Davidic royal line through the post-exilic period, maintaining the lineage that Jewish expectation associated with the coming Messiah.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "bariah", "smith": "bariah", "isbe": "bariah"},
        "key_refs": ["1 Chronicles 3:22"]
    },
    "barkos": {
        "id": "barkos",
        "term": "Barkos",
        "category": "people",
        "intro": "<p>Barkos (meaning <em>painter</em> or <em>partly colored</em>) was the ancestor of a family of Nethinim — temple servants — who returned from Babylonian exile with Zerubbabel and are listed in both Ezra 2:53 and Nehemiah 7:55. The Nethinim were dedicated servants attached to the temple who performed menial tasks in support of the Levitical worship, their origin traced to the Gibeonites assigned by Joshua as hewers of wood and drawers of water for the congregation.</p><p>Barkos appears only in these two parallel lists and is otherwise unknown in the biblical text. His family's inclusion among the returning Nethinim confirms the continuity of this class of temple servants from the pre-exilic period through the restoration, contributing to the reconstitution of the full temple service in Jerusalem under Zerubbabel and Ezra.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barkos", "smith": "barkos", "isbe": "barkos"},
        "key_refs": ["Ezra 2:53", "Nehemiah 7:55"]
    },
    "barley": {
        "id": "barley",
        "term": "Barley",
        "category": "concepts",
        "intro": "<p>Barley was one of the most important cereal crops in ancient Israel and Egypt, grown more widely than wheat because of its greater drought tolerance and its ability to ripen earlier. It was extensively cultivated in Egypt (Exodus 9:31), where the hailstorm plague destroyed it while wheat was not yet ripe. In Palestine, barley was a staple food of the common people and of the poor — the barley harvest in spring (Ruth 1:22; 2:23) preceded the wheat harvest and provided the grain used in bread for much of the population.</p><p>Barley appears in several key narrative moments: Gideon's dream of a loaf of barley bread tumbling into the Midianite camp and overturning a tent (Judges 7:13–14) was interpreted as a sign of Israel's victory. Elisha miraculously fed a hundred men with twenty barley loaves (2 Kings 4:42–44). In John 6:9, 13, the five barley loaves used in the feeding of the five thousand are explicitly noted as barley — the bread of the poor — making the miracle's abundance over common provision all the more striking. Barley was also used as animal fodder (1 Kings 4:28) and as a standard in valuations under the Mosaic law (Leviticus 27:16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barley", "smith": "barley", "isbe": "barley"},
        "key_refs": ["Exodus 9:31", "Ruth 1:22", "2 Kings 4:42", "John 6:9"]
    },
    "barn": {
        "id": "barn",
        "term": "Barn",
        "category": "concepts",
        "intro": "<p>Barns or granaries in ancient Israel were storage facilities for grain, typically underground pits or stone-lined chambers rather than the free-standing wooden structures of later Western usage. The Hebrew terms include <em>mamegura</em> (storehouse, Deuteronomy 28:8; Haggai 2:19) and <em>asam</em> (granary, Proverbs 3:10; Joel 1:17). Job 39:12 uses the word in the context of the harvest ox and the threshing floor. Luke 12:18 uses the Greek <em>apotheke</em> for the barns the rich fool plans to tear down and replace with larger ones to store his abundant harvest.</p><p>The theological resonance of barns in Scripture is primarily related to the tension between human self-sufficiency and trust in God's provision. Jesus's parable of the rich fool (Luke 12:16–21) turns on the fatal presumption of a man who secured his future against want by building bigger barns but failed to reckon with the uncertainty of life itself. The alternative posture — trusting God to provide like the birds of the air, who neither sow nor reap nor gather into barns — is the counter-image Jesus offers (Matthew 6:26).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barn", "isbe": "barn"},
        "key_refs": ["Deuteronomy 28:8", "Haggai 2:19", "Luke 12:18"]
    },
    "barnabas": {
        "id": "barnabas",
        "term": "Barnabas",
        "category": "people",
        "intro": "<p>Barnabas (meaning <em>son of consolation</em> or <em>son of exhortation</em>) was the surname given by the apostles to Joses, a Levite from Cyprus, whose original name was Joseph. He first appears in Acts 4:36–37 selling a field and laying the proceeds at the apostles' feet — an act of exemplary generosity that introduces him as a model of the community life described in Acts 4. He played a pivotal role in the early Jerusalem church by vouching for the newly converted Saul at a time when the apostles were afraid of him (Acts 9:27), and by traveling to Antioch to investigate the new Gentile mission, where he discerned the grace of God and encouraged the believers.</p><p>Barnabas brought Paul from Tarsus to Antioch (Acts 11:25–26), and the two served together as the primary missionary team of the Jerusalem church's first deliberate outreach. They traveled together on the first missionary journey through Cyprus and Asia Minor (Acts 13–14), returned to the Jerusalem Council (Acts 15), and then separated over a disagreement about John Mark — Barnabas took Mark to Cyprus while Paul chose Silas. Paul's later references to Barnabas (1 Corinthians 9:6; Galatians 2:1, 9, 13) confirm his continued significance in the apostolic circle.</p>",
        "hitchcock_meaning": "son of the prophet, or of consolation",
        "source_ids": {"easton": "barnabas", "smith": "barnabas", "isbe": "barnabas"},
        "key_refs": ["Acts 4:36", "Acts 9:27", "Acts 11:25", "Acts 14:11"]
    },
    "barrel": {
        "id": "barrel",
        "term": "Barrel",
        "category": "concepts",
        "intro": "<p>Barrel in the King James Version translates the Hebrew <em>kad</em>, a wide-mouthed vessel used for carrying and storing water, flour, or other provisions. The same word is translated <em>pitcher</em> elsewhere. In the account of Elijah and the widow of Zarephath (1 Kings 17:12–16), the widow's barrel of meal and cruse of oil miraculously sustained her and Elijah through the drought — neither the barrel of meal wasted nor the cruse of oil failed, according to the word of God spoken through Elijah. The miracle became a touchstone of divine provision in the most extreme circumstances.</p><p>The vessel also appears in Gideon's stratagem at the battle with Midian (Judges 7:16), where each of the three hundred men carried a pitcher (kad) containing a torch — smashing the pitchers at the signal to create a sudden blaze of light and sound that routed the Midianite camp. In Genesis 24:14–20, Rebekah drew water from the well in her pitcher for Abraham's servant and his camels, the act by which she was identified as Isaac's destined wife.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barrel", "isbe": "barrel"},
        "key_refs": ["1 Kings 17:12", "1 Kings 17:14", "1 Kings 17:16"]
    },
    "barren": {
        "id": "barren",
        "term": "Barren",
        "category": "concepts",
        "intro": "<p>Barrenness — the inability to bear children — was considered a severe affliction and social stigma in ancient Israel, where fruitfulness was understood as divine blessing and childlessness as either divine displeasure or mysterious withholding. Sarah, Rebekah, Rachel, Hannah, and the Shunammite woman all suffered barrenness before divine intervention brought them children whose births were pivotal for the redemptive narrative. The anguish of the barren woman — most fully expressed in Hannah's prayer in 1 Samuel 1 — became a biblical archetype of prayer from desperation.</p><p>The prophets and Psalms use barrenness and fruitfulness as theological metaphors. Isaiah 54:1 addresses the <em>barren one who did not bear</em> with the counter-intuitive promise that her children will be more than those of the married woman — a passage Paul applies to the Gentile church in Galatians 4:27. Luke 1 places the birth of John the Baptist within this tradition: Elizabeth, barren and well past childbearing age, conceives in fulfillment of the pattern that God opens the womb of those whose situation is humanly hopeless to announce a decisive moment in redemptive history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "barren"},
        "key_refs": ["Genesis 16:2", "1 Samuel 1:6", "Isaiah 54:1", "Luke 1:7"]
    },
    "barsabas": {
        "id": "barsabas",
        "term": "Barsabas",
        "category": "people",
        "intro": "<p>Barsabas (meaning <em>son of rest</em> or <em>son of return</em>) is the surname of two men in the New Testament. The first was Joseph Barsabas, also called Justus, who was one of the two candidates proposed by the Jerusalem church to replace Judas Iscariot as the twelfth apostle (Acts 1:23). He had been with Jesus from John's baptism to the ascension — meeting the qualification stated in Acts 1:21–22 — and was thus a companion of Jesus throughout his ministry. The lot fell on Matthias rather than Joseph, but Barsabas disappears from the narrative without any indication of disappointment or diminishment.</p><p>The second Barsabas was Judas Barsabas, one of the leading men chosen by the Jerusalem council to accompany Paul and Barnabas to Antioch with the letter settling the circumcision controversy (Acts 15:22, 27, 32). He is described as a prophet who exhorted and strengthened the Antiochene believers. The surname Barsabas suggests a family or clan name, and the two men may have been brothers.</p>",
        "hitchcock_meaning": "son of return; son of rest",
        "source_ids": {"easton": "barsabas", "smith": "barsabas"},
        "key_refs": ["Acts 1:23", "Acts 15:22", "Acts 15:32"]
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
    print(f'BP b1: Baal → Barsabas: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
