"""
BP Article Synthesis — b3: Bered → Bless
Covers Easton entries: Bered through Bless (75 entries)

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
  - events:   title is clearly an event

Script: scripts/bp-b3.py
Run: python3 scripts/bp-b3.py
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
    "bered": {
        "id": "bered", "term": "Bered", "category": "people",
        "intro": "<p>Bered (meaning: <em>hail</em>) is a name shared by a place and a person in the Old Testament. As a place, Bered was a town in the south of Palestine in the desert of Shur, near the well Lahai-roi where the angel of the Lord appeared to Hagar. It lay along the ancient caravan route between Canaan and Egypt, in the region traversed by Abraham and later by Isaac.</p><p>As a person, Bered was a son of Shuthelah and grandson of Ephraim, listed in the tribal genealogy of 1 Chronicles 7. His line was among those born to Ephraim after the grief of losing sons to the men of Gath who raided their livestock; Ephraim mourned them many days, and his brethren came to comfort him. Bered thus belongs to the generation of Ephraimites who resettled and rebuilt the tribe's presence in Canaan after early losses.</p>",
        "sections": [], "hitchcock_meaning": "hail",
        "source_ids": {"easton": "bered", "smith": "bered"},
        "key_refs": ["Genesis 16:14", "1 Chronicles 7:20"]
    },
    "beriah": {
        "id": "beriah", "term": "Beriah", "category": "people",
        "intro": "<p>Beriah (meaning: <em>in fellowship</em> or <em>in evil</em>) is a name borne by four men in the Old Testament, the name's dual meaning possibly reflecting the varying circumstances of their birth. The most prominent is Beriah the son of Asher, one of the seventy souls who went down to Egypt with Jacob. His descendants—the Beriites—are numbered in the Mosaic census and formed part of the tribe of Asher's settlement in northern Canaan.</p><p>A second Beriah was a son of Ephraim, born after his father had mourned the slaughter of his sons by the men of Gath; the name was given because <em>it went evil with his house</em> at that time. Two more men named Beriah appear in Benjamite and Levitical genealogies in Chronicles. Together these figures span several tribes and periods, making Beriah one of the more widely distributed personal names in the Old Testament genealogical traditions.</p>",
        "sections": [], "hitchcock_meaning": "in fellowship; in envy",
        "source_ids": {"easton": "beriah", "smith": "beriah"},
        "key_refs": ["Genesis 46:17", "1 Chronicles 7:20", "1 Chronicles 8:13"]
    },
    "bernice": {
        "id": "bernice", "term": "Bernice", "category": "people",
        "intro": "<p>Bernice (meaning: <em>one that brings victory</em>) was the eldest daughter of Herod Agrippa I and sister of both Agrippa II and Drusilla. After the early death of her first husband Marcus, son of the Alexandrian Jew Alexander, she was married to her uncle Herod of Chalcis and bore him two sons. She later lived with her brother Agrippa II in a relationship that attracted scandalous comment from Roman writers including Juvenal and Josephus.</p><p>Bernice appears in Acts 25–26, where she is present with Agrippa II at Caesarea when Paul defends himself before Festus the Roman governor. She listens to Paul's extended address in which he recounts his conversion and his commission to preach the gospel. Agrippa's famous half-serious response—<em>Almost thou persuadest me to be a Christian</em>—was spoken in the context of this audience in which Bernice participated. She later became the mistress of the Roman general Titus before he became emperor, and accompanied him briefly to Rome.</p>",
        "sections": [], "hitchcock_meaning": "one that brings victory",
        "source_ids": {"easton": "bernice", "isbe": "bernice"},
        "key_refs": ["Acts 25:13", "Acts 25:23", "Acts 26:30"]
    },
    "berodach-baladan": {
        "id": "berodach-baladan", "term": "Berodach-baladan", "category": "people",
        "intro": "<p>Berodach-baladan (meaning: <em>the son of death</em>; also written Merodach-baladan in Isaiah) was the king of Babylon who sent a friendly diplomatic mission to Hezekiah king of Judah when he heard that Hezekiah had recovered from a severe illness. The embassy included a letter and a gift, and Hezekiah in his pride showed the messengers all his treasuries—his silver, gold, spices, oil, armory, and everything in his storehouses—an act of imprudence that prompted Isaiah's stern warning of coming Babylonian captivity.</p><p>Berodach-baladan is identified with the historical Marduk-apla-iddina II, a Chaldean chieftain who twice seized the Babylonian throne in the late eighth century BC, challenging Assyrian dominance. His diplomatic contact with Hezekiah likely reflected a desire to forge a western anti-Assyrian alliance, placing the biblical account within the documented political struggles of the period. The episode in 2 Kings 20 and Isaiah 39 is significant as an early prophetic anticipation of the Babylonian exile.</p>",
        "sections": [], "hitchcock_meaning": "the son of death",
        "source_ids": {"easton": "berodach-baladan", "isbe": "berodach-baladan"},
        "key_refs": ["2 Kings 20:12", "Isaiah 39:1", "2 Kings 20:17"]
    },
    "beryl": {
        "id": "beryl", "term": "Beryl", "category": "concepts",
        "intro": "<p>Beryl is the rendering of the Hebrew word <em>tarshish</em> in the Authorized Version, a precious stone named after the city from which it was imported. It was set in the fourth row of the High Priest's breastplate of judgment, alongside jasper and onyx, and bore the name of one of the twelve tribes of Israel. The precise identification of the stone is uncertain—translators have variously rendered <em>tarshish</em> as beryl, chrysolite, or topaz across different versions.</p><p>Beryl appears in several visionary contexts in Scripture. The prophet Ezekiel describes the wheels of the divine chariot as the color of beryl, conveying radiant brilliance. Daniel sees a heavenly figure whose body was like beryl and whose face shone like lightning. In the New Jerusalem of Revelation, beryl forms the eighth foundation of the city wall. The stone's associations with divine glory, priestly service, and eschatological architecture give it theological weight beyond its purely mineralogical identity.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beryl", "smith": "beryl", "isbe": "beryl"},
        "key_refs": ["Exodus 28:20", "Ezekiel 1:16", "Daniel 10:6", "Revelation 21:20"]
    },
    "besom": {
        "id": "besom", "term": "Besom", "category": "concepts",
        "intro": "<p>Besom is an archaic English word for a broom or sweeping instrument, used once in the Authorized Version of Isaiah 14:23 to translate the Hebrew word meaning <em>sweeper</em>. The passage belongs to Isaiah's taunt song against Babylon, in which God declares that he will make Babylon a possession of the bittern and pools of water and sweep it with the besom of destruction. The image conveys total and irreversible obliteration—as a broom sweeps a floor bare.</p><p>The metaphor draws on the mundane domestic act of sweeping to describe cosmic-scale divine judgment, a rhetorical device characteristic of the prophets who ground the most solemn pronouncements in everyday imagery. The word's rarity in biblical usage—it appears only this once—makes it one of the more archaic and distinctive terms in the King James translation. Modern versions typically render it simply as <em>the broom of destruction</em>, preserving the sweep metaphor without the unfamiliar vocabulary.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "besom", "smith": "besom", "isbe": "besom"},
        "key_refs": ["Isaiah 14:23"]
    },
    "besor": {
        "id": "besor", "term": "Besor", "category": "places",
        "intro": "<p>Besor (meaning: <em>glad news</em> or <em>cold</em>) was a ravine or brook in the extreme southwest of Judah, on the route toward the Egyptian border. It marks the site of one of the most humanly significant episodes in David's wilderness years: when David and his men pursued the Amalekites who had raided and burned Ziklag and carried off the wives and children of all the fighters, two hundred of the six hundred men were too exhausted to cross the brook Besor and remained behind.</p><p>The theological importance of Besor lies in the principle David established afterward. When the victorious four hundred returned with recovered families and Amalekite spoil, some of the fighters refused to share the plunder with those who had stayed by the supplies at the brook. David overruled them, establishing as a statute in Israel that <em>as his share is that goes down to the battle, so shall his share be that stays by the baggage; they shall share alike</em>—a principle of covenantal equity that acknowledged different forms of service as equally valid contributions to the common cause.</p>",
        "sections": [], "hitchcock_meaning": "glad news; incarnation",
        "source_ids": {"easton": "besor"},
        "key_refs": ["1 Samuel 30:9", "1 Samuel 30:10", "1 Samuel 30:21"]
    },
    "bestead": {
        "id": "bestead", "term": "Bestead", "category": "concepts",
        "intro": "<p>Bestead is an archaic English term appearing once in the Authorized Version of Isaiah 8:21, where it translates a Hebrew root meaning <em>to oppress</em> or <em>to be in circumstances of hardship</em>. The verse describes those who are <em>hardly bestead and hungry</em>—that is, sorely pressed and famished—as they pass through the land in the darkness of divine judgment. It occurs within Isaiah's oracle of impending Assyrian devastation that contrasts the darkness of unbelief with the light promised in the Messianic vision that follows.</p><p>The word bestead (past participle of <em>bestead</em>, meaning placed in a particular situation, from Old English <em>stede</em>, a place) passed out of common English usage by the early modern period, making it one of the more opaque terms in the King James translation. The Revised Version replaces it with <em>sore distressed</em>, and most modern translations simply render it as <em>hard pressed</em> or <em>distressed</em>. Its occurrence in the darkness oracle of Isaiah 8 places it within one of the most theologically charged passages in the prophetic literature, immediately preceding the announcement of the child born in Galilee.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bestead", "isbe": "bestead"},
        "key_refs": ["Isaiah 8:21"]
    },
    "betah": {
        "id": "betah", "term": "Betah", "category": "places",
        "intro": "<p>Betah (meaning: <em>confidence</em>) was a city belonging to Hadadezer king of Zobah, a powerful Aramaean kingdom northeast of Israel. When David defeated Hadadezer in battle as he extended his kingdom toward the Euphrates, he captured large quantities of brass—bronze—from Betah and from Berothai, another of Hadadezer's cities. This metal later became a significant resource for Solomon's temple construction.</p><p>In the parallel account of 1 Chronicles 18:8, the city is called Tibhath rather than Betah, reflecting variant spellings in the textual tradition. The city lay in the Beqa valley or the region of Zobah in modern Syria. Its mention in the context of David's northern campaigns illustrates the scope of the Davidic kingdom at its height, when Israel's military dominance extended to control over the bronze-producing centers of Aram. The captured bronze was dedicated to the Lord and set aside for eventual temple use by Solomon.</p>",
        "sections": [], "hitchcock_meaning": "confidence",
        "source_ids": {"easton": "betah", "smith": "betah", "isbe": "betah"},
        "key_refs": ["2 Samuel 8:8", "1 Chronicles 18:8"]
    },
    "beth": {
        "id": "beth", "term": "Beth",
        "category": "concepts",
        "intro": "<p>Beth is the Hebrew word for <em>house</em> or <em>dwelling-place</em>, corresponding to the second letter of the Hebrew alphabet and appearing as a common prefix in biblical place names throughout the land of Canaan and the surrounding regions. When prefixed to another word, beth typically identifies a place as the <em>house</em> or <em>temple</em> of whatever deity, feature, or commodity the second element names, reflecting the ancient Semitic practice of naming settlements for their dominant feature or patron.</p><p>The beth- compounds in the Bible number in the dozens: Bethel (house of God), Bethlehem (house of bread), Bethsaida (house of fish), Bethany (house of dates or affliction), Bethesda (house of mercy), Beth-shemesh (house of the sun), and many more. Each preserves a fragment of Canaanite or early Israelite religious and agricultural geography. The word itself carries theological resonance, as God declares his intention to dwell among his people—to make his <em>beth</em> among them—a promise progressively fulfilled through tabernacle, temple, incarnation, and the new Jerusalem.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth", "smith": "beth"},
        "key_refs": []
    },
    "beth-anath": {
        "id": "beth-anath", "term": "Beth-anath", "category": "places",
        "intro": "<p>Beth-anath (meaning: <em>house of response</em> or <em>temple of Anath</em>) was one of the fenced cities in the tribal territory of Naphtali in northern Canaan. Its name suggests it may have been a cultic site dedicated to Anath, the Canaanite goddess of war and hunting who was frequently paired with Baal in the Ugaritic texts. The city was assigned to Naphtali but the tribe failed to drive out the Canaanite inhabitants, who continued to live there as a tributary population within Israel.</p><p>The site is tentatively identified with Ainata, a village approximately six miles west of Kedesh in Upper Galilee, though the identification is not certain. Beth-anath appears in the tribal allotment lists of Joshua 19 and in Judges 1's account of the incomplete conquest. The persistence of Canaanite populations in cities like Beth-anath, despite their assignment to Israelite tribes, became a recurring source of religious syncretism and the fulfillment of the prophetic warnings about the dangers of coexistence with Canaan's inhabitants.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-anath", "isbe": "beth-anath"},
        "key_refs": ["Joshua 19:38", "Judges 1:33"]
    },
    "beth-anoth": {
        "id": "beth-anoth", "term": "Beth-anoth", "category": "places",
        "intro": "<p>Beth-anoth (meaning: <em>house of answers</em> or <em>temple of Anath</em>) was a city in the mountainous district of Judah, listed in the sixth group of Judah's towns in Joshua 15:59. Like its northern counterpart Beth-anath in Naphtali, its name likely reflects a Canaanite religious connection to the goddess Anath. The city lay in the highlands south of Jerusalem.</p><p>Beth-anoth has been identified with modern Beit Ainun, approximately three miles northeast of Hebron in the southern Judean hills. Beyond its single appearance in Joshua's tribal boundary lists, the town plays no role in the narrative portions of Scripture. Its preservation in the allotment records of Joshua demonstrates the detailed administrative awareness of Israelite settlement geography in the highland regions of Judah, even for towns that appear only once in the biblical canon.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-anoth", "isbe": "beth-anoth"},
        "key_refs": ["Joshua 15:59"]
    },
    "beth-arabah": {
        "id": "beth-arabah", "term": "Beth-arabah", "category": "places",
        "intro": "<p>Beth-arabah (meaning: <em>house of the desert</em> or <em>house of the Arabah</em>) was a city situated in the sunken rift valley of the Jordan and the Dead Sea—the region known as the Arabah. It lay on the boundary between the tribes of Judah and Benjamin, appearing in the boundary lists of both tribes in Joshua 15 and 18. The town thus occupied a strategically sensitive position at the tribal frontier in the Jordan valley.</p><p>The location of Beth-arabah is associated with the eastern fringe of Benjamin's territory, near the crossing points of the lower Jordan. It was listed among the six cities of Judah in the wilderness district alongside Nibshan, the City of Salt, and En-gedi. The description of the Arabah as a wilderness region—hot, arid, and lying well below sea level—makes Beth-arabah one of the most geographically distinctive of the Judean lowland settlements, situated in territory quite different from the hill country towns that characterize most of Judah's inheritance.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-arabah", "isbe": "beth-arabah"},
        "key_refs": ["Joshua 15:61", "Joshua 18:22"]
    },
    "beth-aram": {
        "id": "beth-aram", "term": "Beth-aram", "category": "places",
        "intro": "<p>Beth-aram (meaning: <em>house of height</em> or <em>mountain-house</em>) was a fortified town in the territory of Gad, situated approximately three miles east of the Jordan River opposite Jericho. It is mentioned in the list of cities built or rebuilt by the Gadites following their settlement east of Jordan. The town is probably the same as Beth-haram mentioned in Numbers 32:36, where it appears as one of the fenced cities and sheepfolds constructed by the tribe of Gad.</p><p>In later periods, Beth-aram is identified with Livias or Julias, the city renamed by Herod Antipas in honor of Livia, the wife of Augustus Caesar. The site of modern Tell er-Rameh in the Jordan valley corresponds to this location. Its position directly opposite Jericho made it strategically significant for controlling movement across the Jordan fords, and the Gadite fortification of the city reflects their responsibility for defending the eastern flank of the Israelite settlement.</p>",
        "sections": [], "hitchcock_meaning": "house of height",
        "source_ids": {"easton": "beth-aram"},
        "key_refs": ["Joshua 13:27", "Numbers 32:36"]
    },
    "beth-arbel": {
        "id": "beth-arbel", "term": "Beth-arbel", "category": "places",
        "intro": "<p>Beth-arbel (meaning: <em>house of God's ambush</em> or <em>house of God's court</em>) is mentioned once in the Old Testament in the prophet Hosea's warning to Israel. Hosea alludes to a catastrophic military destruction at Beth-arbel as a historical reference his audience would recognize, though the specific event is not recorded elsewhere in the biblical narrative. The destruction was apparently so savage that it served as a byword for total military annihilation, with mothers dashed in pieces upon their children.</p><p>The site is commonly identified with Irbid in the Gilead region of modern Jordan, or alternatively with Arbela in Galilee (modern Khirbet Irbid near the Sea of Galilee). Josephus mentions Arbela in Galilee as the scene of a significant military engagement, lending some support to the Galilean identification. The passage in Hosea 10:14 uses the memory of Beth-arbel as a warning that the same fate awaits Israel's fortified cities if the nation continues in its rebellion against God.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-arbel", "isbe": "beth-arbel"},
        "key_refs": ["Hosea 10:14"]
    },
    "beth-aven": {
        "id": "beth-aven", "term": "Beth-aven", "category": "places",
        "intro": "<p>Beth-aven (meaning: <em>house of nothingness</em> or <em>house of idols</em>) was originally a place in the mountains of Benjamin, east of Bethel, near the pass of Michmash. It appears in Joshua's battle narratives as a landmark in the Benjamite highlands, and in the account of Saul's early military campaigns when the Philistines encamped at Michmash to the east of Beth-aven.</p><p>The name's theological significance is greatest in the prophet Hosea, who repeatedly uses <em>Beth-aven</em> as a derisive substitute for Bethel (meaning <em>house of God</em>), renaming it the <em>house of emptiness</em> or <em>house of wickedness</em> to mock the golden calf worship established there by Jeroboam I. Where once Jacob had met God at Bethel, Hosea saw only idolatry deserving the name <em>Beth-aven</em>. The prophetic wordplay—turning <em>El</em> (God) to <em>aven</em> (nothingness)—became a devastating theological comment on Israel's religious apostasy in the northern kingdom.</p>",
        "sections": [], "hitchcock_meaning": "the house of vanity; of iniquity of trouble",
        "source_ids": {"easton": "beth-aven", "isbe": "beth-aven"},
        "key_refs": ["Joshua 7:2", "1 Samuel 13:5", "Hosea 4:15", "Hosea 5:8"]
    },
    "beth-barah": {
        "id": "beth-barah", "term": "Beth-barah", "category": "places",
        "intro": "<p>Beth-barah (meaning: <em>house of the ford</em> or <em>house of crossing</em>) was a strategic ford or crossing point on the Jordan River, south of the scene of Gideon's victory over the Midianites. When Gideon pursued the fleeing Midianite army, he sent word to the Ephraimites to cut off the retreat by seizing the waters—the fords of the Jordan—before the Midianites, specifically naming Beth-barah and the Jordan as the positions to secure.</p><p>The Ephraimites responded successfully, capturing the two Midianite princes Oreb and Zeeb at the fords—Oreb at the rock of Oreb and Zeeb at the winepress of Zeeb. Beth-barah is generally identified with the ford or crossing point known from other sources, possibly near where the Jabbok river meets the Jordan. Its strategic importance as a river crossing made control of it decisive in cutting off enemy retreat, and Gideon's quick thinking in dispatching the Ephraimites there turned a pursuit into a comprehensive victory.</p>",
        "sections": [], "hitchcock_meaning": "the chosen house",
        "source_ids": {"easton": "beth-barah", "isbe": "beth-barah"},
        "key_refs": ["Judges 7:24"]
    },
    "beth-car": {
        "id": "beth-car", "term": "Beth-car", "category": "places",
        "intro": "<p>Beth-car (meaning: <em>sheep-house</em> or <em>house of the lamb</em>) was a place west of Mizpeh to which the Israelites pursued the Philistines after their great victory under Samuel's leadership. The pursuit began when the Lord thundered with a great thunder against the Philistines and threw them into confusion, and Israel struck them down from Mizpeh to below Beth-car. The victory was commemorated by Samuel with the setting up of a stone called Ebenezer, saying, <em>Thus far the Lord has helped us.</em></p><p>The exact location of Beth-car is unknown. It lay somewhere to the west of Mizpeh in the territory of Benjamin or the western highlands, marking the furthest extent of the Israelite pursuit on that occasion. The battle itself was a pivotal moment in the early monarchy period: Samuel had gathered Israel to repentance at Mizpeh, and the divine intervention validated his prophetic leadership and temporarily subdued Philistine pressure on Israel's territory throughout Samuel's lifetime.</p>",
        "sections": [], "hitchcock_meaning": "the house of the lamb",
        "source_ids": {"easton": "beth-car", "isbe": "beth-car"},
        "key_refs": ["1 Samuel 7:11"]
    },
    "beth-dagon": {
        "id": "beth-dagon", "term": "Beth-dagon", "category": "places",
        "intro": "<p>Beth-dagon (meaning: <em>house of Dagon</em> or <em>temple of Dagon</em>) was the name of two towns in ancient Palestine, both named for the Philistine and Canaanite grain deity Dagon. The first lay in the lowland territory of Judah near Philistia, in the Shephelah region; it is identified with modern Beit Dejan west of Lydda. The second Beth-dagon lay in the tribal territory of Asher in the north, mentioned in the boundary description of Asher's lot.</p><p>The name preserves evidence of the widespread Dagon cult in pre-Israelite Canaan, where temples to this deity existed at major Philistine centers including Gaza and Ashdod. The most dramatic episode involving Dagon occurs not at either Beth-dagon but at Ashdod, where the ark of the covenant was placed in the temple of Dagon and the idol twice fell prostrate before it. The place names Beth-dagon indicate that Dagon worship had penetrated far beyond the Philistine pentapolis into the broader Canaanite world before Israel's arrival.</p>",
        "sections": [], "hitchcock_meaning": "the house of corn, or of fish",
        "source_ids": {"easton": "beth-dagon", "isbe": "beth-dagon"},
        "key_refs": ["Joshua 15:41", "Joshua 19:27"]
    },
    "beth-diblathaim": {
        "id": "beth-diblathaim", "term": "Beth-diblathaim", "category": "places",
        "intro": "<p>Beth-diblathaim (meaning: <em>house of two cakes of figs</em> or <em>house of the two fig-cakes</em>) was a city of Moab mentioned in Jeremiah's oracle of judgment against the Moabite cities. The same place appears to be called Almon-diblathaim in the wilderness itinerary of Numbers 33:46-47, where it marks one of Israel's encampments in the region of Moab during the wilderness journey, and Diblathaim in Ezekiel 6:14.</p><p>The town's location is uncertain, though it lay in the plateau of Moab east of the Dead Sea. Jeremiah's oracle against Moab in chapter 48 lists it alongside Dibon, Nebo, and Kiriathaim as cities that would share in Moab's coming desolation, using the formula of naming multiple cities to convey the comprehensive scope of the judgment. The name's reference to fig-cakes may indicate an agricultural district known for this product, or may preserve the name of an early Moabite settlement whose etymology had been lost by the time of the biblical record.</p>",
        "sections": [], "hitchcock_meaning": "house of dry figs",
        "source_ids": {"easton": "beth-diblathaim", "isbe": "beth-diblathaim"},
        "key_refs": ["Jeremiah 48:22", "Numbers 33:46"]
    },
    "beth-gamul": {
        "id": "beth-gamul", "term": "Beth-gamul", "category": "places",
        "intro": "<p>Beth-gamul (meaning: <em>camel-house</em> or <em>house of recompense</em>) was a city in the plain country of Moab, denounced by the prophet Jeremiah as part of his extended oracle against Moab in chapter 48. Jeremiah lists it among the cities of the Moabite plateau that would experience divine judgment, including Dibon, Kiriathaim, Beth-meon, and others. The oracle pronounces shame and ruin upon each city in turn.</p><p>The site is tentatively identified with Um el-Jemal, a ruined city near Bozrah in the Hauran region of modern Jordan, though other identifications have been proposed. The name's reference to camels may indicate the city served as a camel-trading post or watering station on the trans-Jordanian caravan routes. Its single appearance in Jeremiah's oracle preserves its place in the geographical memory of Moab's settlement landscape even though nothing further is known of its history.</p>",
        "sections": [], "hitchcock_meaning": "house of recompense, or of the camel",
        "source_ids": {"easton": "beth-gamul", "isbe": "beth-gamul"},
        "key_refs": ["Jeremiah 48:23"]
    },
    "beth-gilgal": {
        "id": "beth-gilgal", "term": "Beth-gilgal", "category": "places",
        "intro": "<p>Beth-gilgal (meaning: <em>house of Gilgal</em>) was a place near Jerusalem from which singers and Levites gathered for the celebration of the dedication of the rebuilt walls of Jerusalem under Nehemiah. The name suggests it was a settlement in the vicinity of the famous Gilgal associated with Israel's initial crossing of the Jordan, though it may represent a different site closer to Jerusalem.</p><p>The Nehemiah passage provides the only biblical reference to Beth-gilgal, in the context of the great public ceremony of wall dedication that involved two processions of thanksgiving moving in opposite directions around the city walls. The Levites from surrounding towns and villages gathered to participate in the celebration with musical instruments and singing. Beth-gilgal's inclusion among these gathering places indicates it was a recognized Levitical or priestly settlement in the Jerusalem area during the postexilic period of the restoration community.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-gilgal", "isbe": "beth-gilgal"},
        "key_refs": ["Nehemiah 12:29"]
    },
    "beth-haccerem": {
        "id": "beth-haccerem", "term": "Beth-haccerem", "category": "places",
        "intro": "<p>Beth-haccerem (meaning: <em>house of the vineyard</em>) was a place in the tribe of Judah that served as a signal station during times of military threat. The prophet Jeremiah cites it as a lookout point where a beacon fire was to be raised as a warning signal to the surrounding region when the enemy advanced from the north. The site's elevated position made it suitable for this defensive communication role.</p><p>In the book of Nehemiah, Beth-haccerem appears as the administrative district over which Malchijah the son of Rechab was ruler, and he rebuilt the Dung Gate of Jerusalem as his portion of the wall-building project under Nehemiah. The site is commonly identified with Ramat Rahel, an archaeological site between Jerusalem and Bethlehem that has yielded evidence of Iron Age occupation including royal storage jars stamped with the <em>lamelech</em> seal, consistent with its administrative role in the monarchy period.</p>",
        "sections": [], "hitchcock_meaning": "house of the vineyard",
        "source_ids": {"easton": "beth-haccerem"},
        "key_refs": ["Nehemiah 3:14", "Jeremiah 6:1"]
    },
    "beth-horon": {
        "id": "beth-horon", "term": "Beth-horon", "category": "places",
        "intro": "<p>Beth-horon (meaning: <em>house of the hollow</em> or <em>house of the cavern</em>) was the name of two towns—Upper Beth-horon and Lower Beth-horon—situated in the territory of Ephraim on the strategic pass leading from the Shephelah coastal plain up into the central highlands near Jerusalem. The pass of Beth-horon was one of the most militarily significant routes in all of Palestine, commanding access between the coastal lowlands and the Judean highlands.</p><p>Beth-horon was built or rebuilt by Sherah, the daughter of Ephraim—one of the rare instances in the Old Testament where a woman is credited with founding cities. The pass became the scene of several decisive military engagements: Joshua's great victory over the five Amorite kings when the Lord hurled great stones from heaven and the sun stood still; the route of Philistine retreat after their defeat at the time of Samuel; and a theater of conflict in the Maccabean wars centuries later. Solomon fortified both the upper and lower towns as part of his system of strategic defense for the approaches to Jerusalem.</p>",
        "sections": [], "hitchcock_meaning": "house of wrath",
        "source_ids": {"easton": "beth-horon", "isbe": "beth-horon"},
        "key_refs": ["Joshua 10:10", "1 Chronicles 7:24", "2 Chronicles 8:5"]
    },
    "beth-jeshimoth": {
        "id": "beth-jeshimoth", "term": "Beth-jeshimoth", "category": "places",
        "intro": "<p>Beth-jeshimoth (meaning: <em>house of wastes</em> or <em>house of desolations</em>) was a town in the plain of Moab east of the Jordan, in the region of the Dead Sea. It served as one of the encampment stations of Israel near Abel-shittim during the final stages of the wilderness journey, in the fertile plain between the Jordan and the highlands of Moab. The Israelites were camped in this region when the incident of Baal-peor and the subsequent census occurred.</p><p>After the conquest, Beth-jeshimoth lay within the territory assigned to the tribe of Reuben, east of the Dead Sea. Ezekiel later includes it among the cities of Moab that would experience judgment, paired with Baal-meon and Kiriathaim, predicting that the land of Moab and Ammon would become a possession of the children of the east. The site is generally identified with Tell el-'Azeimeh near the northeastern shore of the Dead Sea.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-jeshimoth", "isbe": "beth-jeshimoth"},
        "key_refs": ["Numbers 33:49", "Joshua 12:3", "Ezekiel 25:9"]
    },
    "beth-le-aphrah": {
        "id": "beth-le-aphrah", "term": "Beth-le-Aphrah", "category": "places",
        "intro": "<p>Beth-le-Aphrah (meaning: <em>house of dust</em>) is a town mentioned in Micah's lamentation over the towns of the Shephelah threatened by Assyrian invasion. The Authorized Version renders the Hebrew as <em>in the house of Aphrah</em> while the Revised Version treats it as the proper name of a town. Micah employs a series of puns on town names to convey the nature of the coming judgment: Beth-le-Aphrah, the house of dust, is told to roll itself in the dust—its very name becoming the description of its humiliation.</p><p>The prophetic wordplay in Micah 1:10–16 is one of the most concentrated examples of paronomasia in Hebrew poetry, with each town's name or meaning illuminating the character of its coming judgment or flight. Beth-le-Aphrah is tentatively identified with et-Taiyibeh in the Shephelah, southeast of Ashdod, though the identification is uncertain. Its significance in the biblical record is limited to this single prophetic reference, where it serves as an element in Micah's lament over the cities of the western approaches to Jerusalem.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-le-aphrah"},
        "key_refs": ["Micah 1:10"]
    },
    "beth-peor": {
        "id": "beth-peor", "term": "Beth-peor", "category": "places",
        "intro": "<p>Beth-peor (meaning: <em>house of Peor</em> or <em>temple of Baal-peor</em>) was a place in Moab on the east side of the Jordan, opposite Jericho, in the territory later assigned to Reuben. Its name identifies it as a cultic site associated with Baal-peor, the local manifestation of Baal worshipped on Mount Peor, and the town's religious character gives it particular significance in the narrative of Israel's wilderness period.</p><p>Beth-peor is most notable as the location near which Moses delivered his final addresses to Israel recorded in Deuteronomy: <em>in the valley opposite Beth-peor, in the land of Moab.</em> It is also the region where Moses died and was buried in an unknown location, with the text noting his burial place was <em>in the valley in the land of Moab opposite Beth-peor.</em> The proximity to the site of Baal-peor's worship makes the selection of this region for Moses's final ministry and burial site a theologically charged detail: the liberator who had led Israel through the temptation of Baal-peor spoke his last words and was buried in its shadow.</p>",
        "sections": [], "hitchcock_meaning": "house of gaping, or opening",
        "source_ids": {"easton": "beth-peor", "isbe": "beth-peor"},
        "key_refs": ["Deuteronomy 3:29", "Deuteronomy 4:46", "Deuteronomy 34:6", "Joshua 13:20"]
    },
    "beth-phage": {
        "id": "beth-phage", "term": "Beth-phage", "category": "places",
        "intro": "<p>Beth-phage (meaning: <em>house of the unripe fig</em> or <em>house of early figs</em>) was a village on the Mount of Olives, on the road between Jerusalem and Jericho, close to Bethany. It appears in all three Synoptic Gospels in connection with the Triumphal Entry of Jesus into Jerusalem: it was near Beth-phage that Jesus sent two disciples ahead to find the donkey and colt on which he would ride into the city.</p><p>The precise location of Beth-phage is uncertain, but it lay between Bethany and Jerusalem on the southeastern slope of the Mount of Olives. A medieval church marks the traditional site. The Triumphal Entry from Beth-phage fulfilled the prophecy of Zechariah 9:9—<em>behold, your king is coming to you, humble and mounted on a donkey</em>—and the crowd's acclamation of Jesus with palm branches and the cry of <em>Hosanna to the Son of David</em> gave the event its popular designation as Palm Sunday in Christian tradition. Beth-phage thus stands at the beginning of Holy Week in the Gospel narrative.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-phage"},
        "key_refs": ["Matthew 21:1", "Mark 11:1", "Luke 19:29"]
    },
    "beth-shean": {
        "id": "beth-shean", "term": "Beth-shean", "category": "places",
        "intro": "<p>Beth-shean (meaning: <em>house of security</em> or <em>house of rest</em>) was one of the most strategically important cities of ancient Canaan, situated at the junction of the Jordan valley and the Jezreel valley at the foot of Mount Gilboa. It commanded the main route between the coast and Transjordan and between northern and southern Canaan. Assigned to Manasseh, it was one of the cities the tribe failed to possess, and its Canaanite inhabitants remained under tribute rather than being expelled.</p><p>Beth-shean's most dramatic biblical episode is the aftermath of the battle of Mount Gilboa, where the Philistines fastened the bodies of Saul and his sons to the city walls and placed Saul's armor in the temple of Ashtaroth. The men of Jabesh-gilead, remembering Saul's deliverance of their city, traveled through the night to retrieve the bodies and give them honorable burial. The site is one of the most extensively excavated in Palestine, with occupation levels spanning from the Neolithic period through the Islamic era, making it a uniquely valuable archaeological witness to the cultural continuity of this strategic crossroads city.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-shean"},
        "key_refs": ["1 Chronicles 7:29", "1 Samuel 31:10", "1 Samuel 31:12", "2 Samuel 21:12"]
    },
    "beth-shemesh": {
        "id": "beth-shemesh", "term": "Beth-shemesh", "category": "places",
        "intro": "<p>Beth-shemesh (meaning: <em>house of the sun</em>) was the name of several towns in ancient Palestine, the most significant being the Levitical city in the territory of Judah at the foot of the Judean hills, near the Sorek valley. This Beth-shemesh was a priestly city assigned to the sons of Aaron, situated on the northern border of Judah where the Shephelah meets the highland country. It commanded one of the main routes from the coastal plain to Jerusalem.</p><p>Beth-shemesh is most famous as the destination of the ark of the covenant when the Philistines returned it on a cart drawn by two milk cows. The ark came to rest in the field of Joshua the Beth-shemeshite, where it was received with joy and sacrifices—but the men of Beth-shemesh were struck down because they looked into the ark, and seventy men died. The city later witnessed the battle between Amaziah of Judah and Joash of Israel, in which Amaziah was defeated and captured. A second Beth-shemesh lay in the territory of Issachar, and a third in Naphtali.</p>",
        "sections": [], "hitchcock_meaning": "house of the sun",
        "source_ids": {"easton": "beth-shemesh", "isbe": "beth-shemesh"},
        "key_refs": ["Joshua 21:16", "1 Samuel 6:15", "Joshua 15:10", "2 Kings 14:11"]
    },
    "beth-tappuah": {
        "id": "beth-tappuah", "term": "Beth-tappuah", "category": "places",
        "intro": "<p>Beth-tappuah (meaning: <em>house of apples</em>) was a town in the hill country of Judah, listed in the second group of Judah's highland cities in Joshua 15:53. It lay in the region between Hebron and the Shephelah, approximately five miles west of Hebron. The town is identified with modern Tuffuh, a village in the West Bank south of Bethlehem, preserving in its modern name a clear echo of the ancient toponym.</p><p>The name suggests the town was situated in apple-growing country or near an orchard of significance in the ancient period. Beyond its single appearance in Joshua's tribal allotment lists, Beth-tappuah plays no narrative role in the Old Testament. The mention of apples or apple trees in the Song of Solomon as symbols of refreshment and shade reflects the value of these fruit trees in the Palestinian highlands, and the name Beth-tappuah preserves that agricultural memory at a specific geographical location in southern Judah.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beth-tappuah", "isbe": "beth-tappuah"},
        "key_refs": ["Joshua 15:53"]
    },
    "bethabara": {
        "id": "bethabara", "term": "Bethabara", "category": "places",
        "intro": "<p>Bethabara (meaning: <em>house of the ford</em> or <em>house of crossing</em>) is a place named in the Authorized Version of John 1:28 as the location east of the Jordan where John the Baptist was conducting his ministry of baptism when the delegation from Jerusalem came to question him. The Revised Version and most modern manuscripts read <em>Bethany beyond the Jordan</em> instead, which Origen already preferred in the third century on the grounds that no Bethabara could be located on the Jordan.</p><p>The place is probably to be identified with Beth-barah, the ford of the Jordan mentioned in the Gideon narrative of Judges 7:24. It lay somewhere in the lower Jordan valley, east of the river, in the region of Perea or the territory beyond Jordan. The site carries extraordinary theological significance as the location where John baptized Jesus, where the Holy Spirit descended as a dove, and where the Father's voice declared from heaven: <em>This is my beloved Son, with whom I am well pleased.</em> Pilgrims have venerated various sites on the Jordan's east bank as candidates for this location.</p>",
        "sections": [], "hitchcock_meaning": "the house of confidence",
        "source_ids": {"easton": "bethabara", "smith": "bethabara", "isbe": "bethabara"},
        "key_refs": ["John 1:28"]
    },
    "bethany": {
        "id": "bethany", "term": "Bethany", "category": "places",
        "intro": "<p>Bethany (meaning: <em>house of dates</em> or <em>house of affliction</em>) was a village on the eastern slope of the Mount of Olives, about two miles from Jerusalem on the road to Jericho. It was the home of Mary, Martha, and their brother Lazarus, and became one of Jesus's most frequented stopping places during his final weeks of ministry in Judea. The village's proximity to Jerusalem made it a natural base for Jesus and his disciples when he entered the city for the Passover.</p><p>Bethany is the site of several of the most theologically significant events in the Gospels: the raising of Lazarus from the dead—Jesus's most dramatic sign before his own resurrection and the immediate catalyst for the Sanhedrin's decision to execute him; the anointing of Jesus with costly nard by Mary of Bethany, which Jesus interpreted as preparation for his burial; and the final blessing and ascension of Jesus, which Luke locates as happening in the vicinity of Bethany. A second Bethany, beyond the Jordan, is mentioned in John 1:28 as John the Baptist's baptizing location. The village is identified with modern al-Eizariya (from Lazarus) on the West Bank.</p>",
        "sections": [], "hitchcock_meaning": "the house of song; the house of affliction",
        "source_ids": {"easton": "bethany", "smith": "bethany", "isbe": "bethany"},
        "key_refs": ["John 11:1", "Mark 11:11", "Matthew 26:6", "Luke 24:50"]
    },
    "bethel": {
        "id": "bethel", "term": "Bethel", "category": "places",
        "intro": "<p>Bethel (meaning: <em>house of God</em>) was a city in central Palestine approximately ten miles north of Jerusalem, at the head of the pass leading through the highlands of Benjamin and Ephraim. Its history in the biblical narrative spans from the patriarchs to the exile, making it one of the most theologically freighted cities in the Old Testament. Originally called Luz, it received the name Bethel when Jacob, fleeing from Esau, dreamed of a ladder reaching to heaven with angels ascending and descending, and heard God renew the Abrahamic promises. He anointed the stone on which he had slept and vowed that if God brought him safely home, this place would be his God's house.</p><p>Jacob returned to Bethel after his years in Paddan-aram, and God appeared to him there again, reaffirming the change of his name to Israel. After the Conquest, Bethel served as a worship site for Israel, and the ark rested there for a period. Its theological trajectory darkened irreversibly when Jeroboam I established one of his golden calves at Bethel as a rival to Jerusalem worship, making it the cult center of the northern kingdom's state religion. The prophets Amos and Hosea directed their most pointed oracles against Bethel's idolatry. Josiah's reform eventually extended to Bethel, where he defiled and destroyed the high place and fulfilled the ancient prophecy of the man of God from Judah.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bethel", "smith": "bethel", "isbe": "bethel"},
        "key_refs": ["Genesis 28:19", "Genesis 12:8", "1 Kings 12:29", "Amos 5:5"]
    },
    "bethelite": {
        "id": "bethelite", "term": "Bethelite", "category": "concepts",
        "intro": "<p>Bethelite is a gentile adjective designating a native or inhabitant of Bethel. The term appears once in the Old Testament as the identifier of Hiel the Bethelite, who rebuilt Jericho during the reign of King Ahab of Israel. When Hiel laid the foundation of Jericho, his firstborn son Abiram died, and when he set up its gates, his youngest son Segub died—a fulfillment of the curse Joshua had pronounced five centuries earlier: <em>Cursed before the Lord be the man who rises up and rebuilds this city, Jericho. At the cost of his firstborn shall he lay its foundation, and at the cost of his youngest son shall he set up its gates.</em></p><p>The identification of Hiel as a Bethelite connects him to the city that had become the center of Jeroboam's calf worship, suggesting a link between the religious corruption of Bethel and Hiel's disregard for the ancient Mosaic prohibition. The episode demonstrates the continuing authority of Joshua's covenant curse even generations after it was pronounced, and serves as a warning within the broader Kings narrative that the word of the Lord through his servants does not return void, however long the interval before fulfillment.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bethelite", "isbe": "bethelite"},
        "key_refs": ["1 Kings 16:34", "Joshua 6:26"]
    },
    "bether": {
        "id": "bether", "term": "Bether", "category": "places",
        "intro": "<p>Bether (meaning: <em>dissection</em> or <em>separation</em>) refers to certain mountains mentioned in the Song of Solomon 2:17, where the lover is compared to a young gazelle leaping upon the mountains of Bether. The precise location of these mountains is unknown, and scholars are divided over whether Bether is a proper place name or a poetic description meaning the <em>divided</em> or <em>cleft mountains</em>—referring to the rugged terrain of the Lebanese or Judean highlands.</p><p>Some commentators have identified Bether with Bittir, a site southwest of Jerusalem known from the Bar Kokhba revolt (AD 132–135) when it served as a Jewish stronghold, while others see it as a generic description of rugged landscape used for poetic effect. In the allegorical interpretation of the Song of Solomon, the mountains of Bether have been understood as representing the separation between the lover and beloved, obstacles that the beloved longs to see overcome. Whether literal or poetic, the image conveys geographical grandeur and the eagerness of love's pursuit across difficult terrain.</p>",
        "sections": [], "hitchcock_meaning": "division, or in the trial",
        "source_ids": {"easton": "bether", "smith": "bether", "isbe": "bether"},
        "key_refs": ["Song of Solomon 2:17"]
    },
    "bethesda": {
        "id": "bethesda", "term": "Bethesda", "category": "places",
        "intro": "<p>Bethesda (meaning: <em>house of mercy</em> or <em>house of grace</em>) was a pool with five covered colonnades near the Sheep Gate of Jerusalem, described in John 5:2 as the location where a great crowd of sick people—blind, lame, and paralyzed—lay waiting for the moving of the waters. The popular belief was that when an angel periodically stirred the pool, the first person to enter the water afterward would be healed of whatever disease they had.</p><p>Bethesda is the setting of Jesus's healing of the man who had been an invalid for thirty-eight years. Jesus approached the man, learned how long he had been ill, and commanded him simply: <em>Rise, take up your bed, and walk.</em> The man was instantly healed, without entering the water. The healing occurred on the Sabbath, and the controversy over carrying the bed on the Sabbath triggered one of the key confrontations over Sabbath observance in John's Gospel. Archaeological excavations in Jerusalem near the Church of St. Anne have uncovered a twin-pool complex with connecting channels that matches John's description well and is widely identified as the Bethesda site.</p>",
        "sections": [], "hitchcock_meaning": "house of pity or mercy",
        "source_ids": {"easton": "bethesda", "smith": "bethesda", "isbe": "bethesda"},
        "key_refs": ["John 5:2", "John 5:8", "John 5:16"]
    },
    "bethlehem": {
        "id": "bethlehem", "term": "Bethlehem", "category": "places",
        "intro": "<p>Bethlehem (meaning: <em>house of bread</em>) was a small town in the hill country of Judah approximately six miles south of Jerusalem, originally called Ephrath or Ephrathah. It held a central place in both Testaments disproportionate to its modest size. The town is first mentioned as the site of Rachel's tomb, where she died in childbirth. It was the ancestral home of the clan of Jesse and the birthplace of David, who was anointed king there by Samuel from among the eight sons of Jesse.</p><p>Bethlehem's supreme theological significance lies in its role as the birthplace of Jesus Christ. Micah 5:2 had prophesied that from Bethlehem Ephrathah, though it was little among the clans of Judah, one would come forth whose goings forth are from of old, from everlasting—a ruler in Israel. Matthew and Luke record the fulfillment of this prophecy: Jesus was born in Bethlehem during the reign of Herod the Great, when Mary and Joseph had come there for the Roman census. Herod's subsequent massacre of the male children of Bethlehem two years old and under, in an attempt to eliminate the infant king, fulfills Jeremiah's lament of Rachel weeping for her children. Bethlehem remains one of Christianity's holiest sites, with the Church of the Nativity marking the traditional birthplace.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bethlehem", "smith": "bethlehem", "isbe": "bethlehem"},
        "key_refs": ["Micah 5:2", "Ruth 4:11", "Matthew 2:1", "Luke 2:4", "Genesis 35:19"]
    },
    "bethsaida": {
        "id": "bethsaida", "term": "Bethsaida", "category": "places",
        "intro": "<p>Bethsaida (meaning: <em>house of fish</em> or <em>house of hunting</em>) was the name of two or possibly one town on the northern shore of the Sea of Galilee with exceptional significance in the Gospel narratives. The western Bethsaida was a fishing village in Galilee, the native town of the apostles Peter, Andrew, and Philip. It lay near Capernaum and served as a center of Jesus's Galilean ministry. The eastern Bethsaida—or Bethsaida Julias—was rebuilt and renamed by Philip the Tetrarch in honor of the daughter of Augustus.</p><p>Bethsaida is the setting for several of Jesus's most notable miracles: the feeding of the five thousand in a deserted place near Bethsaida; the healing of a blind man at Bethsaida with a gradual two-stage process unique among the Gospel miracles; and likely the setting for Peter's walking on water. Despite this concentration of miraculous works, Jesus pronounced woe upon Bethsaida for its failure to repent, comparing it unfavorably to Tyre and Sidon: <em>Woe to you, Bethsaida! For if the mighty works done in you had been done in Tyre and Sidon, they would have repented long ago in sackcloth and ashes.</em></p>",
        "sections": [], "hitchcock_meaning": "house of fruits, or of food, or of snares",
        "source_ids": {"easton": "bethsaida", "smith": "bethsaida", "isbe": "bethsaida"},
        "key_refs": ["John 1:44", "Luke 9:10", "Mark 8:22", "Matthew 11:21"]
    },
    "bethuel": {
        "id": "bethuel", "term": "Bethuel", "category": "people",
        "intro": "<p>Bethuel (meaning: <em>filiation of God</em> or <em>man of God</em>) was the son of Nahor by his wife Milcah, making him the nephew of Abraham. He was the father of both Rebekah and Laban, and thus the grandfather of Jacob and Esau through Rebekah's marriage to Isaac. His lineage made him the link between the family of Terah and the next generation of the patriarchal line, placing him at a critical juncture in the genealogical history of Israel.</p><p>Bethuel's most significant appearance is in the account of Abraham's servant's mission to find a wife for Isaac from among Abraham's kindred in Paddan-aram. When the servant arrived at the household and recounted how the Lord had guided him to Rebekah, Bethuel and Laban replied together that the thing proceeded from the Lord and they could say neither good nor bad. Bethuel appears to have died or become inactive shortly after this episode, as subsequent negotiations for Rebekah's departure were conducted by Laban alone. His son Laban became the more prominent figure in the family, hosting Jacob during his twenty years of service. Also, a town in the tribe of Simeon bears the name Bethuel in 1 Chronicles 4:30.</p>",
        "sections": [], "hitchcock_meaning": "filiation of God",
        "source_ids": {"easton": "bethuel", "smith": "bethuel"},
        "key_refs": ["Genesis 22:22", "Genesis 24:15", "Genesis 24:47", "Genesis 24:50"]
    },
    "bethzur": {
        "id": "bethzur", "term": "Bethzur", "category": "places",
        "intro": "<p>Bethzur (meaning: <em>house of rock</em>) was a town in the mountainous region of Judah, approximately four miles north of Hebron. It is listed among the cities of the hill country of Judah in Joshua 15:58 and was one of fifteen cities in that administrative district. King Rehoboam fortified it as part of his system of defensive cities protecting the southern approaches to Jerusalem after the division of the kingdom, along with Lachish, Azekah, Adoraim, and others.</p><p>Bethzur became strategically critical during the Maccabean period, when it served as a major fortress on the southern frontier of Judea. Judas Maccabaeus defeated a Seleucid force there in 165 BC, and the city changed hands multiple times during the subsequent decades of conflict between the Maccabees and the Seleucid empire. The site, identified with Khirbet et-Tubeiqah north of Hebron, has been excavated and shows extensive occupation from the Middle Bronze Age through the Byzantine period. Its position dominating the road from the Negev into the Judean highlands made it perennially important for controlling access to Jerusalem from the south.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bethzur", "smith": "bethzur"},
        "key_refs": ["Joshua 15:58", "2 Chronicles 11:7"]
    },
    "betroth": {
        "id": "betroth", "term": "Betroth", "category": "concepts",
        "intro": "<p>Betrothal in the ancient Israelite context was a formal legal agreement to marry, far more binding than a modern engagement and carrying near the full legal weight of marriage itself. The betrothal typically occurred a year or more before the actual wedding ceremony and cohabitation. A betrothed woman was legally considered a wife: violation of her by another man was treated as adultery, and if a man died after betrothal, his intended was considered a widow. The betrothal was solemnized through a formal declaration and usually accompanied by a bride price paid to the woman's family.</p><p>The Mosaic law addressed betrothal with specific regulations distinguishing between violations of betrothed women in city and country settings. Joseph's intention to divorce Mary quietly when he discovered her pregnancy reflects the legal seriousness of their betrothal, since breaking a betrothal required a formal certificate of divorce. The language of betrothal carries rich theological weight in the Old Testament prophets, where God declares to Israel: <em>I will betroth you to me forever; I will betroth you in righteousness and justice, in steadfast love and mercy</em>—making the covenant relationship between God and his people a marriage entered through divine initiative and faithfulness.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "betroth", "isbe": "betroth"},
        "key_refs": ["Deuteronomy 28:30", "Hosea 2:19", "Matthew 1:18"]
    },
    "beulah": {
        "id": "beulah", "term": "Beulah", "category": "concepts",
        "intro": "<p>Beulah (meaning: <em>married</em>) is a metaphorical name used in Isaiah 62:4 as a prophetic designation for the land of Israel in the coming age of restoration. The verse sets two contrasting pairs of names against each other: the land that had been called <em>Desolate</em> and the nation that had been called <em>Forsaken</em> would be renamed <em>Hephzibah</em> (my delight is in her) and <em>Beulah</em> (married), because the Lord delights in Israel and the land shall be married—espoused anew to God after the estrangement of exile.</p><p>The marital metaphor underlying Beulah draws on the prophetic tradition, most fully developed in Hosea and Jeremiah, of understanding the covenant relationship between the Lord and Israel as a marriage. Exile and judgment represent the rupture of that covenant marriage; restoration represents a new betrothal and renewed union. John Bunyan immortalized the name in <em>Pilgrim's Progress</em>, where Beulah Land is the country of heavenly rest near the Celestial City, a usage that entered Christian hymnody and devotional literature and made Beulah a familiar symbol of eschatological peace and blessing far beyond its single prophetic occurrence.</p>",
        "sections": [], "hitchcock_meaning": "married",
        "source_ids": {"easton": "beulah", "smith": "beulah", "isbe": "beulah"},
        "key_refs": ["Isaiah 62:4"]
    },
    "bewray": {
        "id": "bewray", "term": "Bewray", "category": "concepts",
        "intro": "<p>Bewray is an archaic English verb meaning <em>to reveal</em>, <em>to disclose</em>, or <em>to betray</em>—functionally equivalent to modern English <em>betray</em> or <em>expose</em>. It appears several times in the Authorized Version, including Proverbs 27:16, where it describes the difficulty of restraining a contentious woman: <em>whosoever hideth her hideth the wind, and the ointment of his right hand, which bewrayeth itself</em>. In Matthew 26:73, the bystanders tell Peter that his speech <em>bewrayeth</em> him—his Galilean accent reveals or betrays his identity as one of Jesus's companions.</p><p>The word derives from Old English and Middle English, being used by Chaucer and other medieval writers in the sense of accusation or revelation. By the time of the King James translators in 1611 it was already becoming archaic, and modern versions replace it with <em>reveals</em>, <em>betrays</em>, or <em>gives away</em>. The Matthew 26 instance is theologically significant as the moment when Peter's accent identifies him to the servants in the high priest's courtyard, precipitating his third denial of Jesus before the cock crowed.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bewray"},
        "key_refs": ["Proverbs 27:16", "Matthew 26:73", "Isaiah 16:3"]
    },
    "beyond": {
        "id": "beyond", "term": "Beyond", "category": "concepts",
        "intro": "<p>Beyond, when used with reference to the Jordan River in the Pentateuch and early historical books, carries a specific directional meaning that depends on the vantage point of the author. Moses, writing on the east bank of the Jordan, uses <em>beyond the Jordan</em> to refer to the west side of the river—the direction in which he could not go but toward which Israel was heading. The phrase therefore describes Canaan proper from the perspective of the wilderness camp in Moab.</p><p>This seemingly simple directional term became a source of discussion for commentators who noticed the apparent anachronism: Genesis 50:10-11 uses <em>beyond the Jordan</em> of a location west of the river in a narrative set when Israel had not yet crossed. The later historical books use the phrase with greater variation, sometimes meaning the Transjordanian region (east of the Jordan, the <em>beyond the Jordan</em> of later readers in Canaan) and sometimes preserving the Mosaic perspective. The Deuteronomic formula <em>this side of the Jordan</em> and <em>beyond the Jordan</em> thus encapsulates the geographical and compositional complexity of the Pentateuchal tradition.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "beyond", "isbe": "beyond"},
        "key_refs": ["Genesis 50:10", "Deuteronomy 1:1", "Genesis 50:11"]
    },
    "bezaleel": {
        "id": "bezaleel", "term": "Bezaleel", "category": "people",
        "intro": "<p>Bezaleel (meaning: <em>in the shadow of God</em>, i.e., <em>under his protection</em>) was the chief craftsman appointed by God to execute the artistic work of the tabernacle in the wilderness. He was the son of Uri and grandson of Hur, of the tribe of Judah. God declared that he had filled Bezaleel with the Spirit of God, with ability and intelligence, with knowledge and all craftsmanship, to devise artistic designs, to work in gold, silver, and bronze, in cutting stones for setting, in carving wood, and in every craft.</p><p>Bezaleel worked alongside Oholiab of the tribe of Dan and taught others to join in the skilled labor of tabernacle construction. Together they were responsible for the ark of the covenant, the table of showbread, the lampstand, the incense altar, the courtyard furnishings, and the priestly garments—virtually every element of the sanctuary. Bezaleel represents in Scripture the principle that artistic skill and craftsmanship, when exercised in service of divine worship, is itself a manifestation of the Spirit's gifting. A second Bezaleel appears in Ezra 10:30 as one of the Israelites who had taken a foreign wife during the exile period.</p>",
        "sections": [], "hitchcock_meaning": "in the shadow of God",
        "source_ids": {"easton": "bezaleel", "smith": "bezaleel"},
        "key_refs": ["Exodus 31:2", "Exodus 35:30", "Exodus 36:1"]
    },
    "bezek": {
        "id": "bezek", "term": "Bezek", "category": "places",
        "intro": "<p>Bezek (meaning: <em>lightning</em> or <em>scattering</em>) was a place in the mountainous region of Judah and the residence of Adoni-bezek, a Canaanite king of formidable reputation. After the death of Joshua, the tribes of Judah and Simeon went up to battle against the Canaanites, and they found and fought Adoni-bezek at Bezek, defeating him and capturing him there. The capture of Adoni-bezek is notable for the poetic justice of his punishment: his thumbs and great toes were cut off, and he acknowledged that he had done the same to seventy kings who gathered scraps under his table.</p><p>A second Bezek appears in 1 Samuel 11:8 as the place where Saul mustered his army before relieving the siege of Jabesh-gilead by the Ammonites. This Bezek was in a different location, probably in the northern part of Manasseh, suited for the mustering of a northern coalition to march against Nahash the Ammonite. The two uses of the name suggest either a common toponym applied to more than one site or a very large territory. The first Bezek is the more theologically significant, illustrating the principle of retribution embedded in Israel's conquest narratives.</p>",
        "sections": [], "hitchcock_meaning": "lightning; in the chains",
        "source_ids": {"easton": "bezek", "smith": "bezek", "isbe": "bezek"},
        "key_refs": ["Judges 1:5", "1 Samuel 11:8"]
    },
    "bezer": {
        "id": "bezer", "term": "Bezer", "category": "places",
        "intro": "<p>Bezer (meaning: <em>ore of gold or silver</em> or <em>stronghold</em>) was a city in the wilderness on the eastern plateau of Reuben, designated as one of the three cities of refuge east of the Jordan River. Moses set aside Bezer along with Ramoth in Gilead and Golan in Bashan as Transjordanian cities to which a person who had killed someone unintentionally could flee and find protection from the avenger of blood until a trial could determine the nature of the killing.</p><p>Bezer was also a Levitical city assigned from the tribe of Reuben to the Merarite family of Levites. The site is not certainly identified, though some scholars propose Umm el-'Amad north of Medeba as the location. A second person named Bezer appears in the genealogy of the tribe of Asher in 1 Chronicles 7:37, as the son of Zophah—a minor figure known only from the genealogical record. The city of refuge bears the greater significance, representing the Mosaic legal provision for manslaughter that balanced justice with mercy in the Israelite legal system.</p>",
        "sections": [], "hitchcock_meaning": "vine branches",
        "source_ids": {"easton": "bezer", "smith": "bezer", "isbe": "bezer"},
        "key_refs": ["Deuteronomy 4:43", "Joshua 20:8", "1 Chronicles 6:78"]
    },
    "bible": {
        "id": "bible", "term": "Bible", "category": "concepts",
        "intro": "<p>Bible is the English form of the Greek <em>biblia</em>, meaning <em>books</em>—a plural noun that came to be treated as a singular in the fifth century AD, when it began to be applied to the entire collection of sacred writings of the Old and New Testaments. The Greek word derives from <em>byblos</em>, the inner bark of the papyrus plant used for writing material, which gave its name to the Phoenician city of Byblos (Gebal), a major export center for papyrus writing materials in the ancient Mediterranean world. The Latin Vulgate's single-volume Bible made the plural <em>biblia</em> feel singular, and the usage fixed itself in European languages.</p><p>The Bible consists of the sixty-six books of the Protestant canon—thirty-nine in the Old Testament and twenty-seven in the New—though the Roman Catholic and Eastern Orthodox traditions include additional deuterocanonical books. The New Testament designates its own core as <em>the scriptures</em> and treats the Old Testament as sacred writings whose fulfillment it records. Jesus affirmed the indestructibility of Scripture, declaring that not one jot or tittle would pass from the law until all was fulfilled. The Bible's claim to be divinely inspired, profitable for teaching and training in righteousness, is foundational to its reception throughout the history of Christianity and Judaism.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bible", "smith": "bible"},
        "key_refs": ["2 Peter 1:20", "Romans 1:2", "2 Timothy 3:16", "Matthew 5:18"]
    },
    "bier": {
        "id": "bier", "term": "Bier", "category": "concepts",
        "intro": "<p>A bier is the frame or open coffin on which a dead body was laid and carried to the place of burial. In the ancient Israelite practice reflected in the Old Testament and New Testament, burial took place soon after death—typically the same day—and the body was wrapped in linen cloths and carried on an open bier in a procession to the tomb. Unlike the closed coffins used in Egypt, the Palestinian practice used an open stretcher or frame on which the wrapped body could be seen.</p><p>The most vivid New Testament reference to a bier is in Luke 7:14, where Jesus encountered the funeral procession of the only son of a widow of Nain and touched the bier, commanding the dead man to arise. The bearers stopped, the young man sat up and began to speak, and Jesus gave him to his mother. The touch of the bier—which would have made Jesus ceremonially unclean—was immediately superseded by the life-giving word of the one who is the resurrection and the life. The episode demonstrates the compassion of Christ toward widows and his authority over death, which the crowd recognized as the appearance of a great prophet.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bier", "smith": "bier", "isbe": "bier"},
        "key_refs": ["Luke 7:14"]
    },
    "bigtha": {
        "id": "bigtha", "term": "Bigtha", "category": "people",
        "intro": "<p>Bigtha (meaning: <em>garden</em> or <em>gift of fortune</em>) was one of the seven eunuchs or chamberlains who served in the court of King Ahasuerus of Persia and had charge of the royal harem. He is named in Esther 1:10 alongside Mehuman, Biztha, Harbona, Abagtha, Zethar, and Carcas as among those commanded by the king to bring Queen Vashti before the royal banquet to display her beauty to the assembled princes and nobles of the Persian empire.</p><p>When Vashti refused the royal summons, the sequence of events began that would lead to Esther's elevation as queen and ultimately to the deliverance of the Jewish people from Haman's plot. Bigtha's role in this narrative is minimal—a functionary executing the royal command that Vashti then refused—but his position as a named royal chamberlain reflects the detailed court setting within which the book of Esther unfolds its drama of providential deliverance. The naming of all seven chamberlains adds historical specificity to the Persian court background of the narrative.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bigtha", "smith": "bigtha", "isbe": "bigtha"},
        "key_refs": ["Esther 1:10"]
    },
    "bigthan": {
        "id": "bigthan", "term": "Bigthan", "category": "people",
        "intro": "<p>Bigthan (also written Bigthana; meaning: <em>in the press</em> or <em>giving meat</em>) was a royal eunuch who kept the door in the court of King Ahasuerus of Persia. Together with a colleague named Teresh, he conspired to assassinate the king—a plot that Mordecai, sitting at the king's gate, happened to discover and report to Queen Esther, who passed the information to the king with appropriate credit to Mordecai.</p><p>An investigation confirmed the truth of the report, the conspirators were hanged on the gallows, and the incident was recorded in the royal chronicles in Mordecai's name. This seemingly minor episode becomes pivotal to the book of Esther's providential plot: on the night Haman came to request Mordecai's execution, the king could not sleep and had the chronicles read to him, and the account of Mordecai's unrewarded service was read at that moment. The king's subsequent honoring of Mordecai humiliated Haman at the very point he had come to secure Mordecai's death, turning the tide of the entire narrative toward the Jewish community's deliverance.</p>",
        "sections": [], "hitchcock_meaning": "in the press; giving meat",
        "source_ids": {"easton": "bigthan"},
        "key_refs": ["Esther 2:21", "Esther 6:1", "Esther 6:2"]
    },
    "bildad": {
        "id": "bildad", "term": "Bildad", "category": "people",
        "intro": "<p>Bildad (meaning: <em>old friendship</em> or <em>son of contention</em>) was the second of Job's three friends who came to comfort him in his affliction. He is called <em>the Shuhite</em>, probably identifying him as a member of the tribe or district of Shuah, associated with one of the sons of Abraham by Keturah who settled in Arabia. Like his companions Eliphaz and Zophar, Bildad came with genuine intentions of comfort but became an articulate defender of traditional theological orthodoxy at the expense of pastoral sensitivity.</p><p>Bildad speaks three times in the dialogues of Job. His speeches consistently appeal to the wisdom of the ancestors and traditional doctrine: suffering is the consequence of sin, and if Job's children died it was because they sinned. He urges Job to seek God and trust that the righteous are rewarded and the wicked destroyed. His second speech contains an extended and vivid description of the fate of the wicked that Job finds deeply offensive in his circumstances. Bildad speaks briefer and briefer speeches as the dialogues progress, his third speech being only six verses long. At the end of the book, God declares that he is angry with Eliphaz, Bildad, and Zophar because they have not spoken what is right about him, as his servant Job has.</p>",
        "sections": [], "hitchcock_meaning": "old friendship",
        "source_ids": {"easton": "bildad", "smith": "bildad", "isbe": "bildad"},
        "key_refs": ["Job 8:1", "Job 18:1", "Job 25:1", "Job 42:9"]
    },
    "bilgah": {
        "id": "bilgah", "term": "Bilgah", "category": "people",
        "intro": "<p>Bilgah (meaning: <em>ancient countenance</em> or <em>cheerful</em>) is a name shared by two men in the Old Testament. The first was a priest who headed the fifteenth of the twenty-four courses of priests organized by David for rotating service at the temple. Each course served for one week at a time in a prescribed rotation, and the Bilgah course would have been responsible for temple service twice a year in the regular cycle established before the temple was built.</p><p>The second Bilgah was a priest who returned from the Babylonian captivity with Zerubbabel in the first great wave of the return recorded in Nehemiah 12:5. His name also appears slightly later in the same chapter as Bilgai in the list of those who sealed the covenant under Nehemiah. The priestly course tradition established by David thus persisted through the exile and into the restoration period, with the family of Bilgah representing a strand of continuity in Levitical service from the Davidic organization through the return and rebuilding of the postexilic community.</p>",
        "sections": [], "hitchcock_meaning": "ancient countenance",
        "source_ids": {"easton": "bilgah", "smith": "bilgah"},
        "key_refs": ["1 Chronicles 24:14", "Nehemiah 12:5"]
    },
    "bilhah": {
        "id": "bilhah", "term": "Bilhah", "category": "people",
        "intro": "<p>Bilhah (meaning: <em>faltering</em> or <em>bashful</em>) was the handmaid of Rachel whom Laban gave to his daughter as a servant when Rachel married Jacob. When Rachel saw that she was barren while Leah bore sons freely, she gave Bilhah to Jacob as a concubine to bear children on Rachel's behalf—the ancient practice of surrogate motherhood through a servant woman. Bilhah bore Jacob two sons: Dan, whose name Rachel explained as God having judged her and listened to her voice; and Naphtali, whose name she explained as having prevailed over her sister with mighty wrestlings.</p><p>The sons of Bilhah thus became two of the twelve tribes of Israel, their ancestry as the sons of a handmaid rather than a principal wife reflected in their lower status in some later tribal rankings. A later episode records that Reuben, Jacob's firstborn, lay with Bilhah his father's concubine, an act of transgression that Jacob noted on his deathbed and that contributed to Reuben forfeiting the birthright. Bilhah's name also appears as a place name—a town in the territory of Simeon—in 1 Chronicles 4:29.</p>",
        "sections": [], "hitchcock_meaning": "who is old or confused",
        "source_ids": {"easton": "bilhah", "smith": "bilhah"},
        "key_refs": ["Genesis 29:29", "Genesis 30:3", "Genesis 30:6", "Genesis 35:22"]
    },
    "bilshan": {
        "id": "bilshan", "term": "Bilshan", "category": "people",
        "intro": "<p>Bilshan (meaning: <em>son of the tongue</em> or <em>eloquent</em>) was a man of some note who returned from the Babylonian captivity with Zerubbabel and Jeshua in the first great return of exiles to the land of Israel, recorded in both Ezra 2:2 and Nehemiah 7:7. He is listed among the leaders of the returning community alongside Zerubbabel, Jeshua, Nehemiah, Azariah, Raamiahm Nahamani, Mordecai, and others who led the initial wave of return.</p><p>Beyond this single identification as a leader of the returning exiles, nothing further is known of Bilshan. His name appears in both the Ezra and Nehemiah versions of the return list with minor spelling variations, as is common in the parallel genealogical records of the restoration period. His inclusion among the named leaders of the return indicates that he held a position of responsibility in organizing or leading the journey back to Judah, though the nature of his leadership role is not specified. The eloquence suggested by his name may have qualified him for some administrative or representative function in the community.</p>",
        "sections": [], "hitchcock_meaning": "in the tongue",
        "source_ids": {"easton": "bilshan", "smith": "bilshan", "isbe": "bilshan"},
        "key_refs": ["Ezra 2:2", "Nehemiah 7:7"]
    },
    "bird": {
        "id": "bird", "term": "Bird", "category": "concepts",
        "intro": "<p>Birds in the Old Testament are classified under the Mosaic law into clean and unclean categories, the distinctions roughly corresponding to diet and habitat. Clean birds—those permitted for food and sacrifice—are not listed by species but by implication: any bird not on the prohibited list. The prohibited unclean birds in Leviticus 11 and Deuteronomy 14 include eagles, vultures, ospreys, kites, ravens, owls, nighthawks, seagulls, hawks, cormorants, ibis, storks, herons, and bats. The underlying principle appears to be the avoidance of birds of prey and carrion-eaters.</p><p>Birds played multiple roles in Israelite worship and daily life. Doves and pigeons were offered in sacrifice as a provision for the poor who could not afford larger animals, and two doves or pigeons were the offering prescribed for various purification rites. The release of a live bird over running water was part of the cleansing ritual for healed lepers. In the creation narrative God makes birds on the fifth day alongside sea creatures. The New Testament uses birds as examples of divine providence—the Father feeds them, yet they neither sow nor reap—to argue for trusting God for human needs. The dove became the symbol of the Holy Spirit at Jesus's baptism, drawing on the Genesis image of the Spirit hovering over the waters.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bird"},
        "key_refs": ["Leviticus 1:14", "Leviticus 14:4", "Genesis 1:20", "Matthew 6:26"]
    },
    "birsha": {
        "id": "birsha", "term": "Birsha", "category": "people",
        "intro": "<p>Birsha (meaning: <em>an evil</em> or <em>a son who beholds</em>) was the king of Gomorrah at the time of the invasion of the four eastern kings under Chedorlaomer of Elam. He joined the coalition of five kings of the cities of the plain—Sodom, Gomorrah, Admah, Zeboiim, and Zoar—who had been subject to Chedorlaomer for twelve years before rebelling in the thirteenth year. In the fourteenth year, Chedorlaomer and his allied kings came and defeated the five in the Valley of Siddim, capturing Lot and his possessions along with the people and goods of Sodom and Gomorrah.</p><p>The rescue mission by Abraham recovered Lot and the captured people and goods, and Abraham's subsequent meeting with Melchizedek and his refusal of the king of Sodom's offer are the theologically significant aftermath of the battle. Birsha himself plays no further role in the narrative beyond providing the political context for Lot's capture and Abraham's military intervention. His name appears only in Genesis 14:2, making him one of the minor royal figures whose brief mention anchors the patriarchal narrative in a political landscape of city-states and regional military coalitions.</p>",
        "sections": [], "hitchcock_meaning": "an evil; a son who beholds",
        "source_ids": {"easton": "birsha", "smith": "birsha", "isbe": "birsha"},
        "key_refs": ["Genesis 14:2"]
    },
    "birth": {
        "id": "birth", "term": "Birth", "category": "concepts",
        "intro": "<p>Birth customs in the ancient Israelite world followed patterns common to the broader ancient Near East while incorporating distinctive elements tied to covenant identity. As soon as a child was born, it was washed, rubbed with salt—a practice Ezekiel mentions as having been neglected in the metaphorical birth of Jerusalem—and wrapped in linen swaddling bands. The salt rubbing may have served antiseptic or symbolic purposes, associated with covenant and preservation. Luke's account of Jesus's birth at Bethlehem echoes these customs when Mary wraps the infant in swaddling cloths and lays him in a manger.</p><p>The Mosaic law prescribed specific purification periods for mothers after childbirth: forty days of uncleanness after the birth of a son and eighty days after a daughter, followed by prescribed sacrifices for purification. Male infants were circumcised on the eighth day, incorporating them into the covenant community. The birth of a son was generally cause for greater celebration than a daughter in the ancient patriarchal context, though the daughters of Zelophehad successfully challenged the assumption that daughters were unimportant heirs in the Mosaic period. The new birth metaphor Jesus employs in John 3—birth from water and Spirit—draws on physical birth as the analogy for entry into the kingdom of God.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "birth", "isbe": "birth"},
        "key_refs": ["Ezekiel 16:4", "Luke 2:7", "Leviticus 12:1", "John 3:3"]
    },
    "birth-day": {
        "id": "birth-day", "term": "Birth-day", "category": "concepts",
        "intro": "<p>Birthday observances in the biblical record are associated primarily with royal courts and Gentile custom rather than with ordinary Israelite practice. The earliest clear biblical reference to a birthday celebration is the account of Pharaoh's birthday feast in Genesis 40:20, at which the chief butler was restored to his position and the chief baker was executed—the fulfillment of Joseph's interpretations of their dreams in prison. The pattern of birthday celebration as a royal feast at which gifts are given and dramatic decisions made reappears in the New Testament.</p><p>The most theologically significant birthday narrative in Scripture is Herod Antipas's birthday banquet in Matthew 14:6-11 and Mark 6:21-28, at which Herodias's daughter danced, Herod made a rash oath to give her whatever she asked, and she requested the head of John the Baptist on a platter. Herod was reluctant but complied, unwilling to refuse before his guests, and John was beheaded in prison. The association of birthday feasts with dark outcomes in both Genesis and the Gospels may reflect an ancient Jewish ambivalence toward birthday celebration as a Gentile practice. Job's sons held regular feasts on their birthdays that Job sanctified with burnt offerings as a precaution.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "birth-day"},
        "key_refs": ["Genesis 40:20", "Job 1:4", "Matthew 14:6"]
    },
    "birthright": {
        "id": "birthright", "term": "Birthright", "category": "concepts",
        "intro": "<p>The birthright in ancient Israel designated the special privileges belonging to the firstborn son, including a double portion of the inheritance, the priestly role within the family, and the leadership position among the brothers. Under the Mosaic law, the father was explicitly forbidden from transferring the double portion to the son of a favored wife if there was an older son by a less favored wife, protecting the firstborn's legal entitlement regardless of parental preference. The firstborn also had a special consecration to the Lord, requiring redemption through a prescribed payment.</p><p>The most theologically charged birthright narrative is Esau's sale of his birthright to Jacob for a meal of bread and lentil stew, described as a moment of despising his birthright for immediate gratification. The New Testament cites Esau as a warning against godless and worldless behavior, one who sold his inheritance for a single meal and afterward found no place for repentance though he sought it with tears. Reuben forfeited the firstborn's honor through moral failure, and his double portion passed to the sons of Joseph—Ephraim and Manasseh—each receiving a tribal allotment. The theological resonance of the birthright narrative extends into Paul's discussion of divine election and the choosing of the younger son over the elder in the purposes of God.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "birthright", "smith": "birthright", "isbe": "birthright"},
        "key_refs": ["Genesis 25:33", "Deuteronomy 21:15", "Genesis 49:4", "Hebrews 12:16"]
    },
    "bishop": {
        "id": "bishop", "term": "Bishop", "category": "concepts",
        "intro": "<p>Bishop (from the Greek <em>episkopos</em>, meaning <em>overseer</em> or <em>guardian</em>) was a term used in the New Testament for a leader in the early Christian community, equivalent in that period to <em>elder</em> (<em>presbyteros</em>). The two terms appear to be used interchangeably in the apostolic period: Paul addresses the elders (presbyteroi) of Ephesus in Acts 20:17 and describes them as overseers (episkopoi) appointed by the Holy Spirit to care for the flock. Similarly in Titus 1:5-7, he moves seamlessly from speaking of elders to bishops in describing the same role.</p><p>The qualifications for the office are set out in 1 Timothy 3 and Titus 1, emphasizing moral integrity, ability to teach, household management, freedom from recent conversion, good reputation among outsiders, sobriety, and hospitality. The bishop was to be the husband of one wife, temperate, self-controlled, and not a lover of money. The subsequent development of the monarchical episcopate—with a single bishop presiding over multiple elders in a region—emerged in the second century, represented in the letters of Ignatius of Antioch, and became the normative form of church governance in most Christian traditions. The New Testament itself presents a more collegial pattern of leadership by a body of bishop-elders in each local church.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bishop", "smith": "bishop", "isbe": "bishop"},
        "key_refs": ["Acts 20:17", "Philippians 1:1", "1 Timothy 3:1", "Titus 1:7"]
    },
    "bit": {
        "id": "bit", "term": "Bit", "category": "concepts",
        "intro": "<p>Bit (Hebrew <em>metheg</em>) refers to the curb or restraining device placed in the mouths of horses and other animals to direct and control their movement. In Psalm 32:9, the word is used as a metaphor for the kind of mindless submission God does not want from his people: <em>Be not like a horse or a mule, without understanding, which must be curbed with bit and bridle, or it will not stay near you.</em> The image contrasts the unthinking obedience of an animal constrained by physical force with the willing, understanding trust God desires from his people.</p><p>The same Hebrew word is translated <em>bridle</em> in 2 Kings 19:28 and Isaiah 37:29, where God declares to the Assyrian king Sennacherib: <em>I will put my hook in your nose and my bit in your mouth, and I will turn you back on the way by which you came.</em> The reversal of the human use of bit and bridle—with God applying the restraint to the arrogant king—makes the image a vehicle for divine sovereignty over the nations. James 3:3 uses the bit as an illustration of the tongue's potential for control: just as a small bit controls a large horse, so the tongue—though small—directs the whole course of human life.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bit"},
        "key_refs": ["Psalms 32:9", "2 Kings 19:28", "James 3:3"]
    },
    "bith-ron": {
        "id": "bith-ron", "term": "Bith-ron", "category": "places",
        "intro": "<p>Bith-ron (meaning: <em>the broken or divided place</em> or <em>the gorge</em>) was a district in the Arabah or Jordan valley region east of the river, through which Abner and his men passed during their retreat from the battle at Gibeon. After the violent encounter between Joab's men and Abner's men of Israel at the Pool of Gibeon—which resulted in the death of Asahel and twenty of David's servants—Abner and his Benjamites fled through the Arabah toward the Jordan and crossed over, passing through all Bith-ron before reaching Mahanaim.</p><p>The district of Bith-ron has not been positively identified, but it appears to designate a section of the Jordan valley cleft or a tributary wadi on the east side of the river, between the Jordan crossing and Mahanaim in Gilead. The name, suggesting a divided or cut-through landscape, fits a ravine or gorge cut by one of the tributaries flowing into the Jordan from the eastern plateau. It appears only in this single reference in 2 Samuel 2:29, serving as a geographical waypoint in Abner's retreat narrative during the civil conflict between the houses of Saul and David.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bith-ron"},
        "key_refs": ["2 Samuel 2:29"]
    },
    "bithynia": {
        "id": "bithynia", "term": "Bithynia", "category": "places",
        "intro": "<p>Bithynia was a Roman province in northwest Asia Minor, situated along the southern shore of the Propontis (Sea of Marmara) and the Black Sea (Pontus Euxinus). It was formed as a Roman province in 74 BC, often administered together with Pontus as a single province under a proconsular governor. The territory included fertile coastal lowlands and was one of the more prosperous regions of Asia Minor.</p><p>Bithynia appears twice in the New Testament in significant missional contexts. In Acts 16:7, Paul and his companions attempted to enter Bithynia on the second missionary journey but were prevented by the Spirit of Jesus—one of the most striking narrative instances of the Spirit redirecting missionary plans. This redirection led instead to the Macedonian vision and the opening of the gospel in Europe. In 1 Peter 1:1, Peter addresses his letter to the elect exiles of the dispersion in Pontus, Galatia, Cappadocia, Asia, and Bithynia—indicating that Christian communities had been established there, whether by subsequent missionary work or through the movement of believers from other regions. Pliny the Younger's famous letter to Trajan around AD 112, written as governor of Bithynia, provides valuable external testimony to the rapid growth of Christianity in the province.</p>",
        "sections": [], "hitchcock_meaning": "violent precipitation",
        "source_ids": {"easton": "bithynia", "smith": "bithynia", "isbe": "bithynia"},
        "key_refs": ["Acts 16:7", "1 Peter 1:1"]
    },
    "bitter": {
        "id": "bitter", "term": "Bitter",
        "category": "concepts",
        "intro": "<p>Bitterness in Scripture functions both as a physical quality and as a rich symbolic register for affliction, misery, grief, and spiritual estrangement. In its literal sense, bitter water figures most prominently in the wilderness narrative at Marah, where Israel's complaint about undrinkable water was answered when Moses threw a tree into the water and it became sweet—a foundational demonstration of divine provision that also served as a test of Israel's trust. The waters of jealousy described in Numbers 5, administered to women suspected of adultery, were also bitter.</p><p>Symbolically, bitterness denotes the experience of slavery and oppression: the Egyptians made Israel's lives bitter with hard service before the Exodus, and the Passover meal included bitter herbs as a memorial of that bitterness. Naomi renamed herself Mara (bitter) because the Almighty had dealt bitterly with her in her bereavement. The Chaldeans are called the <em>bitter and hasty nation</em> in Habakkuk's complaint about divine justice. In the New Testament, Peter warns Simon Magus that he is in the gall of bitterness and bond of iniquity, and Hebrews warns against any root of bitterness springing up to cause trouble in the community. Revelation's angel gives John a scroll sweet as honey in the mouth but bitter in the stomach—the bittersweet nature of prophetic commission.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bitter"},
        "key_refs": ["Exodus 1:14", "Ruth 1:20", "Exodus 15:23", "Hebrews 12:15"]
    },
    "bittern": {
        "id": "bittern", "term": "Bittern", "category": "concepts",
        "intro": "<p>Bittern is the rendering in the Authorized Version of the Hebrew word <em>qippod</em> (or <em>qippoz</em>), appearing three times in prophetic oracles of desolation against Babylon, Idumea (Edom), and Nineveh. The precise identification of the bird is debated: the Revised Version renders it as <em>porcupine</em> or <em>hedgehog</em> in some passages, while others maintain the bittern—a large, solitary marsh bird known for its booming call—as a plausible rendering. Modern translations vary considerably between bittern, hedgehog, owl, and other creatures.</p><p>Whatever the specific animal, the function in all three passages is consistent: the creature is a symbol of desolate, uninhabited wasteland. When Isaiah announces the coming destruction of Babylon, he declares that bitterns will possess its pools and that God will sweep it with the besom of destruction. In Isaiah 34, the similar oracle against Idumea presents a gallery of desert creatures—pelicans, ravens, owls, jackals, and bitterns—inhabiting the ruined land. Zephaniah's oracle against Nineveh likewise populates its ruins with this creature. The prophetic imagination uses the appearance of wilderness animals in formerly populous cities as the most vivid possible image of complete divine judgment.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bittern", "smith": "bittern", "isbe": "bittern"},
        "key_refs": ["Isaiah 14:23", "Isaiah 34:11", "Zephaniah 2:14"]
    },
    "bitumen": {
        "id": "bitumen", "term": "Bitumen", "category": "concepts",
        "intro": "<p>Bitumen is a natural mineral pitch or asphalt found in deposits throughout the ancient Near East, particularly in the region around the Dead Sea and in Mesopotamia. The Hebrew word <em>chemar</em>, translated as <em>slime</em> in the Authorized Version and <em>bitumen</em> in the Revised Version, refers to this sticky, waterproofing substance. The Valley of Siddim near the Dead Sea was full of <em>slime pits</em>—bitumen deposits—which the kings of Sodom and Gomorrah fell into when their forces were routed by the four eastern kings.</p><p>Bitumen served two crucial functions in biblical narrative. Noah's ark was pitched—waterproofed—inside and out with pitch (<em>kopher</em>), a related substance. The basket of papyrus reeds in which Moses's mother concealed her infant son on the Nile was similarly daubed with bitumen and pitch to make it watertight. In both cases, a humble waterproofing material becomes the means of preserving life in a life-threatening situation involving water. Bitumen was also extensively used in Babylonian construction, where it served as mortar for the great ziggurats and city walls—the context in which Genesis 11:3 mentions it for the Tower of Babel.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bitumen", "isbe": "bitumen"},
        "key_refs": ["Genesis 11:3", "Genesis 14:10", "Exodus 2:3"]
    },
    "black": {
        "id": "black", "term": "Black", "category": "concepts",
        "intro": "<p>Black in the biblical world functioned both as a literal color description and as a symbol carrying primarily negative or somber associations. In its literal uses, black describes the color of human hair (as opposed to white or gray, which indicated age or leprosy), the dark of night, the raven's plumage, the color of horses in prophetic visions, and the darkening of skin from famine or disease. Jeremiah laments that Zion's Nazirites—once purer than snow and whiter than milk—are now blacker than soot, their appearance unrecognized in the streets.</p><p>Symbolically, black is associated with mourning, disaster, and divine judgment. The sky turning black represents storm and judgment, as in Elijah's vision of the coming rain cloud black as ink. The black horse of Revelation 6:5 is associated with famine and scarcity. Job describes his skin as black and falling from his body in his affliction. In Proverbs 7:9, black describes the darkness of night in which the adulteress ensnares the young man—a moral darkness matching the physical. The Song of Solomon stands as an exception: the beloved describes herself as <em>black but beautiful</em>, her color the result of sun exposure rather than shame, and her beauty is affirmed without qualification by her lover.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "black", "isbe": "black"},
        "key_refs": ["Lamentations 4:8", "Revelation 6:5", "Song of Solomon 1:5"]
    },
    "blade": {
        "id": "blade", "term": "Blade", "category": "concepts",
        "intro": "<p>Blade in the Authorized Version refers primarily to the flat, cutting portion of a sword or other edged weapon, as distinct from the handle or hilt. The word appears in the account of Ehud's assassination of Eglon king of Moab, where the blade of Ehud's double-edged dagger—a cubit long—disappeared completely into the king's body, hilt and all, because of the king's great girth. The same Hebrew word is used in Job 39:23 for the glittering point of a spear and in Nahum 3:3 for the flashing sword of attacking cavalry.</p><p>In a different sense, <em>blade</em> is used in Matthew 13:26 in the parable of the wheat and tares, where the blade refers to the sprouting of grain—the first appearance of the shoots before the head develops. Jesus uses this stage of plant growth to describe the simultaneous appearance of the weeds among the wheat, a situation the householder addresses with the instruction to let both grow together until the harvest. The word's agricultural usage in the New Testament parable stands in sharp contrast to its predominantly military uses in the Old Testament, reflecting the range of the English word blade across both natural and combat contexts.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "blade"},
        "key_refs": ["Judges 3:22", "Matthew 13:26", "Job 39:23"]
    },
    "blains": {
        "id": "blains", "term": "Blains", "category": "concepts",
        "intro": "<p>Blains is an archaic English term for blisters, boils, or pustules, used in the Authorized Version to describe the sixth plague of Egypt in Exodus 9:9-10. Moses and Aaron took handfuls of ashes from a kiln and threw them into the air before Pharaoh, and they became fine dust over all the land of Egypt and caused boils breaking out in blisters—<em>blains</em>—on both humans and animals throughout Egypt. The magicians themselves were so afflicted they could not stand before Moses.</p><p>In Deuteronomy 28:27 and 28:35, a similar affliction—the <em>botch of Egypt</em>—is listed among the curses that would fall on Israel if they disobeyed the covenant, explicitly recalling the Egyptian plague as a reference point for divine judgment. The sixth plague is notable for being the first Egyptian plague from which the magicians could not even pretend to replicate the sign; their own bodies bore the evidence of divine power. The medical nature of the affliction has been variously identified as anthrax, smallpox, or another pustular disease, though exact diagnosis across millennia is speculative.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "blains", "smith": "blains", "isbe": "blains"},
        "key_refs": ["Exodus 9:9", "Exodus 9:10", "Deuteronomy 28:27"]
    },
    "blasphemy": {
        "id": "blasphemy", "term": "Blasphemy", "category": "concepts",
        "intro": "<p>Blasphemy in its primary biblical sense denotes speech or action that dishonors God—speaking against his name, his character, or his works in a way that denies his majesty, goodness, or power. The Old Testament prescribes the death penalty for blasphemy: the law of Leviticus 24:10-16 records the case of the son of an Israelite woman and an Egyptian father who blasphemed the Name and cursed God, and was stoned by the whole congregation. The same law applies equally to the native Israelite and the sojourner.</p><p>Blasphemy carries particular weight in the New Testament context, where Jesus declares that blasphemy against the Holy Spirit—the deliberate and persistent attribution of his work by the Spirit to Satan—is an unforgivable sin that will never be forgiven in this age or the age to come. The authorities accused Jesus himself of blasphemy for claiming the authority to forgive sins and for declaring himself the Son of God, making blasphemy the formal charge on which he was condemned before the Sanhedrin. The book of Revelation describes the beast as covered with blasphemous names and as opening its mouth in blasphemy against God. The New Testament broadens the concept to include any slander against God's name caused by the misconduct of those who bear it: <em>the name of God is blasphemed among the Gentiles because of you</em>.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "blasphemy", "smith": "blasphemy", "isbe": "blasphemy"},
        "key_refs": ["Leviticus 24:16", "Matthew 12:31", "Mark 14:64", "Revelation 13:6"]
    },
    "blastus": {
        "id": "blastus", "term": "Blastus", "category": "people",
        "intro": "<p>Blastus (meaning: <em>that buds or brings forth</em>) was the personal chamberlain of King Herod Agrippa I, the grandson of Herod the Great who ruled Judea from AD 41-44 and is mentioned in Acts 12 as the king who executed James the apostle and imprisoned Peter. Blastus appears in Acts 12:20 in the account of the delegation from Tyre and Sidon who sought a peaceful resolution to Herod's anger toward their cities, for which they depended on Herod's territory for their food supply.</p><p>The Tyrians and Sidonians, having made Blastus their ally—presumably through bribery or personal persuasion—used his influence to secure an audience with Herod and petition for peace. The subsequent account records that when Herod addressed the assembled crowd in his royal robes, the people shouted that it was the voice of a god and not of a man, and immediately an angel of the Lord struck him down because he did not give God the glory. He was eaten by worms and died. Blastus is significant only as the intermediary through whom the coastal cities gained access to the king, but his position as the chamberlain—the gatekeeper of royal access—gave him considerable informal influence in the Herodian court.</p>",
        "sections": [], "hitchcock_meaning": "that buds or brings forth",
        "source_ids": {"easton": "blastus", "smith": "blastus", "isbe": "blastus"},
        "key_refs": ["Acts 12:20"]
    },
    "blemish": {
        "id": "blemish", "term": "Blemish", "category": "concepts",
        "intro": "<p>Blemish in the Mosaic law designated physical imperfections or deformities that disqualified men from serving as priests and animals from being offered in sacrifice. The laws of Leviticus 21:17-23 specify that no man of Aaron's offspring who has a blemish—including blindness, lameness, a mutilated face, a limb too long, an injured foot or hand, a hunchback, dwarf, defective eyesight, itching disease, or crushed testicles—may approach to offer God's food offerings. Such men could eat the sacred offerings but could not serve at the altar.</p><p>The same principle applied to animals: only unblemished animals—without any physical defect—could be presented as burnt offerings, peace offerings, or vow offerings to the Lord. The requirement for physical perfection was not a statement about the value of disabled persons but a typological principle: the sacrificial system required symbols of wholeness and completeness to represent the perfect offering to a holy God. The New Testament interprets Christ's sacrifice as the fulfillment of this requirement: he is described as a lamb without blemish or spot, whose perfect sacrifice achieves what the repeated blemish-free animal offerings could only foreshadow. Paul applies the same standard to the church, which Christ presents to himself as holy and without blemish.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "blemish", "isbe": "blemish"},
        "key_refs": ["Leviticus 21:17", "Leviticus 22:19", "1 Peter 1:19", "Ephesians 5:27"]
    },
    "bless": {
        "id": "bless", "term": "Bless", "category": "concepts",
        "intro": "<p>Blessing in the biblical world operates in several directions simultaneously and is one of the richest theological concepts in Scripture. God blesses his creatures when he confers good things upon them—life, fruitfulness, prosperity, and peace—as in the creation blessing of Genesis 1:22 and the patriarchal blessings of Abraham. Humans bless God when they praise and thank him for his goodness, acknowledging him as the source of all good gifts. Humans bless one another through words of benediction and intercession that invoke God's favor on the recipient, as in Aaron's priestly blessing of Numbers 6:24-26 or the patriarchal deathbed blessings.</p><p>The theology of blessing reaches its culmination in the Abrahamic covenant promise that through Abraham all the families of the earth would be blessed—a promise Paul interprets in Galatians 3 as fulfilled in Christ, through whom the blessing of Abraham comes to the Gentiles by faith. Jesus's Beatitudes in the Sermon on the Mount pronounce divine blessing (Greek <em>makarios</em>, also translated <em>happy</em> or <em>fortunate</em>) on those whose condition and character receive God's approval, often reversing worldly assessments of who is enviable. The book of Revelation concludes with seven beatitudes, the last announcing blessed those who wash their robes in the blood of the Lamb, granting them access to the tree of life in the new creation.</p>",
        "sections": [], "hitchcock_meaning": None,
        "source_ids": {"easton": "bless", "isbe": "bless"},
        "key_refs": ["Genesis 1:22", "Numbers 6:24", "Genesis 12:3", "Galatians 3:14"]
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
    print(f'BP b3: Bered → Bless: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
