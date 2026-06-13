#!/usr/bin/env python3
"""BP Z1: Zaanaim → Zibia (75 Easton entries)"""
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
    "zaanaim": {
        "id": "zaanaim",
        "term": "Zaanaim",
        "category": "places",
        "intro": "<p>Zaanaim (also Zaanannim) was a place near Kedesh in the territory of Naphtali, mentioned in Judges 4:11 as the location where Heber the Kenite had pitched his tent, separated from the rest of the Kenite clans. It was in the plain of Zaanannim near Kedesh that Jael wife of Heber killed the fleeing Canaanite general Sisera (Judges 4:17–21). The site appears in Joshua 19:33 as a boundary marker of Naphtali. The exact location is uncertain, though some scholars identify it with Khan et-Tujjar (Khan of the Merchants) southeast of Tabor.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zaanaim", "smith": "zaanaim", "isbe": "zaanaim"},
        "key_refs": ["Judges 4:11", "Judges 4:17", "Joshua 19:33"]
    },
    "zaanan": {
        "id": "zaanan",
        "term": "Zaanan",
        "category": "places",
        "intro": "<p>Zaanan was a town in the Shephelah of Judah mentioned by the prophet Micah in a sequence of wordplays on place names in the Shephelah, lamenting the coming Assyrian invasion: <em>the inhabitant of Zaanan does not come out</em> (Micah 1:11). The name means <em>place of flocks</em> or <em>land of going forth</em>, and Micah's wordplay plays on the idea that the people of Zaanan would not <em>go forth</em> (come out), despite the root of their city's name suggesting movement. Some identify Zaanan with Zenan of Joshua 15:37, a town in the same district.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zaanan", "smith": "zaanan", "isbe": "zaanan"},
        "key_refs": ["Micah 1:11", "Joshua 15:37"]
    },
    "zaanannim": {
        "id": "zaanannim",
        "term": "Zaanannim",
        "category": "places",
        "intro": "<p>Zaanannim is another spelling of Zaanaim, the plain near Kedesh in Naphtali where Heber the Kenite encamped and where Jael killed Sisera (Judges 4:11). The name may mean <em>wanderings</em> or refer to a type of tree (the terebinth). The Septuagint sometimes renders the location as <em>the oak in Bezaanannim</em>. The site is a landmark in the narrative of Deborah and Barak's victory over Jabin king of Hazor and serves as the setting for one of Scripture's most memorable episodes of unexpected deliverance.</p>",
        "sections": [],
        "hitchcock_meaning": "movings; a person asleep",
        "source_ids": {"easton": "zaanannim"},
        "key_refs": ["Judges 4:11"]
    },
    "zaavan": {
        "id": "zaavan",
        "term": "Zaavan",
        "category": "people",
        "intro": "<p>Zaavan (also spelled Zavan) was a son of Ezer, one of the Horite clan chiefs of Seir in Edom (Genesis 36:27; 1 Chronicles 1:42). The Horites were the original inhabitants of the region of Seir before the Edomites (descendants of Esau) settled there (Deuteronomy 2:12, 22). Zaavan appears only in these genealogical lists and is otherwise unknown in the biblical narrative. The name may mean <em>trembling</em> or <em>troubled</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "trembling",
        "source_ids": {"easton": "zaavan", "isbe": "zaavan"},
        "key_refs": ["Genesis 36:27", "1 Chronicles 1:42"]
    },
    "zabad": {
        "id": "zabad",
        "term": "Zabad",
        "category": "people",
        "intro": "<p>Zabad is a name borne by several biblical figures. (1.) A son of Nathan of Judah, in the genealogy of the house of Jerahmeel (1 Chronicles 2:36–37). (2.) An Ephraimite slain by the Gathites for cattle-raiding (1 Chronicles 7:21). (3.) One of David's mighty warriors, the son of Ahlai (1 Chronicles 11:41). (4.) A conspirator who killed King Joash of Judah; he is called Jozachar in 2 Kings 12:21 and Zabad in 2 Chronicles 24:26. Three individuals named Zabad appear among those who had taken foreign wives in Ezra 10:27, 33, 43. The name means <em>gift</em> or <em>endowed</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "dowry; endowed",
        "source_ids": {"easton": "zabad", "smith": "zabad", "isbe": "zabad"},
        "key_refs": ["1 Chronicles 2:36", "1 Chronicles 11:41", "2 Chronicles 24:26"]
    },
    "zabbai": {
        "id": "zabbai",
        "term": "Zabbai",
        "category": "people",
        "intro": "<p>Zabbai is the name of two biblical individuals. (1.) One of those who had taken foreign wives after the exile, listed in the penitential assembly convened by Ezra (Ezra 10:28). (2.) The father of Baruch, who worked on the wall of Jerusalem beside the Broad Wall under Nehemiah (Nehemiah 3:20). The name may mean <em>pure</em> or <em>flowing</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "flowing",
        "source_ids": {"easton": "zabbai", "smith": "zabbai", "isbe": "zabbai"},
        "key_refs": ["Ezra 10:28", "Nehemiah 3:20"]
    },
    "zabbud": {
        "id": "zabbud",
        "term": "Zabbud",
        "category": "people",
        "intro": "<p>Zabbud was the son of Bigvai, one of those who returned from Babylonian exile to Jerusalem with Ezra in the second return (Ezra 8:14). He and Uthai led a group of 70 males from the family of Bigvai. The name means <em>given</em> or <em>endowed</em> — a variant of Zabad. He is otherwise unknown in the biblical narrative.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zabbud", "smith": "zabbud", "isbe": "zabbud"},
        "key_refs": ["Ezra 8:14"]
    },
    "zabdi": {
        "id": "zabdi",
        "term": "Zabdi",
        "category": "people",
        "intro": "<p>Zabdi is the name of four biblical individuals. (1.) An ancestor of Achan who hid the accursed spoil of Jericho (Joshua 7:1, 17–18). He is called Zimri in 1 Chronicles 2:6. (2.) A Benjamite (1 Chronicles 8:19). (3.) A Levite, overseer of the wine cellars under David (1 Chronicles 27:27). (4.) A Levite who offered a prayer at the dedication of Jerusalem's walls under Nehemiah (Nehemiah 11:17), called Zichri in 1 Chronicles 9:15. The name means <em>my gift</em> or <em>the LORD is my endowment</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Zabad",
        "source_ids": {"easton": "zabdi", "smith": "zabdi", "isbe": "zabdi"},
        "key_refs": ["Joshua 7:1", "1 Chronicles 27:27"]
    },
    "zabdiel": {
        "id": "zabdiel",
        "term": "Zabdiel",
        "category": "people",
        "intro": "<p>Zabdiel is the name of two biblical individuals. (1.) The father of Jashobeam, David's chief military officer for the first month (1 Chronicles 27:2). (2.) A leading priest who returned to Jerusalem after the exile; his son Jehoel was the father of 128 mighty men of valor (Nehemiah 11:14). The name means <em>my gift is God</em> or <em>God has endowed</em>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zabdiel", "smith": "zabdiel", "isbe": "zabdiel"},
        "key_refs": ["1 Chronicles 27:2", "Nehemiah 11:14"]
    },
    "zabud": {
        "id": "zabud",
        "term": "Zabud",
        "category": "people",
        "intro": "<p>Zabud was the son of Nathan and <em>principal officer, the king's friend</em> under Solomon (1 Kings 4:5). He held a special position of personal companionship with the king — <em>king's friend</em> was a recognized court title in ancient Near Eastern royal administrations, denoting an intimate counselor with direct access to the king. Zabud was likely the son of the prophet Nathan who served David, making him a trusted figure in the Davidic royal household. He appears only in this brief administrative list and is not mentioned elsewhere.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zabud", "smith": "zabud", "isbe": "zabud"},
        "key_refs": ["1 Kings 4:5"]
    },
    "zabulon": {
        "id": "zabulon",
        "term": "Zabulon",
        "category": "places",
        "intro": "<p>Zabulon is the Greek form of Zebulun, used in the New Testament. Matthew 4:13–15 quotes Isaiah 9:1–2 concerning <em>the land of Zabulon and the land of Nephthalim</em> in connection with Jesus's settlement in Capernaum and the beginning of his Galilean ministry: <em>the people dwelling in darkness have seen a great light.</em> This fulfillment text links the region of the northern tribes, historically vulnerable to Assyrian invasion and deportation, with the light of the Messiah's ministry among those same Galilean territories. See also the article on Zebulun.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zabulon", "smith": "zabulon", "isbe": "zabulon"},
        "key_refs": ["Matthew 4:13", "Isaiah 9:1"]
    },
    "zaccai": {
        "id": "zaccai",
        "term": "Zaccai",
        "category": "people",
        "intro": "<p>Zaccai was the head of a family of 760 members who returned to Jerusalem from the Babylonian exile with Zerubbabel (Ezra 2:9; Nehemiah 7:14). The family is simply listed among the families identified by their ancestor's name who came back in the first return. Zaccai himself presumably lived in the pre-exilic period; the family preserved his name as its founding figure through the exile. The name means <em>pure</em> or <em>just</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "pure meat; just",
        "source_ids": {"easton": "zaccai", "smith": "zaccai", "isbe": "zaccai"},
        "key_refs": ["Ezra 2:9", "Nehemiah 7:14"]
    },
    "zacchaeus": {
        "id": "zacchaeus",
        "term": "Zacchaeus",
        "category": "people",
        "intro": "<p>Zacchaeus (Greek form of the Hebrew Zaccai, meaning <em>pure</em>) was the chief tax-collector (<em>architelones</em>) at Jericho, described as wealthy, who climbed a sycamore tree to see Jesus as he passed through the city (Luke 19:1–10). As a senior customs official in one of Judea's most commercially important cities — Jericho controlled the balsam trade — Zacchaeus would have been both prosperous and despised, since tax-collectors worked for the Roman system and were considered collaborators and extortionists.</p><p>Jesus stopped beneath the tree, called Zacchaeus by name, and invited himself to the tax-collector's house, declaring: <em>I must stay at your house today.</em> The crowd grumbled that Jesus had gone to stay with a sinner. But Zacchaeus stood and declared: <em>Behold, Lord, the half of my goods I give to the poor. And if I have defrauded anyone of anything, I restore it fourfold.</em> Jesus responded: <em>Today salvation has come to this house, since he also is a son of Abraham. For the Son of Man came to seek and to save the lost</em> — a statement that crystallizes the purpose of the entire Lukan narrative.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zacchaeus", "smith": "zacchaeus", "isbe": "zacchaeus"},
        "key_refs": ["Luke 19:1", "Luke 19:8", "Luke 19:9", "Luke 19:10"]
    },
    "zaccur": {
        "id": "zaccur",
        "term": "Zaccur",
        "category": "people",
        "intro": "<p>Zaccur is a name shared by several biblical figures. (1.) The father of Shammua, the spy sent from the tribe of Reuben to explore Canaan (Numbers 13:4). (2.) A son of Imri, who helped repair the wall of Jerusalem under Nehemiah (Nehemiah 3:2). (3.) A Levite who set his seal to the covenant under Nehemiah (Nehemiah 10:12). (4.) A Levite musician and son of Asaph (1 Chronicles 25:2, 10; Nehemiah 12:35). (5.) A son of Mattaniah, one of the treasury overseers under Nehemiah (Nehemiah 13:13). The name means <em>mindful</em> or <em>remembered</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "of the male kind; mindful",
        "source_ids": {"easton": "zaccur", "smith": "zaccur", "isbe": "zaccur"},
        "key_refs": ["Numbers 13:4", "Nehemiah 3:2", "1 Chronicles 25:2"]
    },
    "zachariah": {
        "id": "zachariah",
        "term": "Zachariah",
        "category": "people",
        "intro": "<p>Zachariah (meaning <em>the LORD has remembered</em>) was the son and successor of Jeroboam II as king of Israel, the fourteenth king of the northern kingdom (2 Kings 14:29; 15:8–12). He reigned only six months before being publicly assassinated by Shallum son of Jabesh at Ibleam. His death fulfilled the promise God had made to Jehu that his dynasty would continue to the fourth generation (2 Kings 10:30), which it did through Jehoahaz, Joash, Jeroboam II, and Zachariah. With his assassination, the Jehu dynasty came to an end and Israel entered a period of rapid political instability leading to its fall to Assyria in 722 BC.</p>",
        "sections": [],
        "hitchcock_meaning": "memory of the Lord",
        "source_ids": {"easton": "zachariah", "smith": "zachariah", "isbe": "zachariah"},
        "key_refs": ["2 Kings 14:29", "2 Kings 15:8", "2 Kings 15:12", "2 Kings 10:30"]
    },
    "zacharias": {
        "id": "zacharias",
        "term": "Zacharias",
        "category": "people",
        "intro": "<p>Zacharias is the Greek form of Zechariah. (1.) The father of John the Baptist, a priest of the division of Abijah who ministered in the Jerusalem temple (Luke 1:5–79). During his priestly service, the angel Gabriel appeared to him at the altar of incense and announced that his barren wife Elizabeth would bear a son who would go before the Lord in the spirit and power of Elijah. Zacharias doubted, and was struck mute until the child was born and named. His canticle at John's naming — the Benedictus (Luke 1:67–79) — is a major christological hymn of the nativity narratives. (2.) The son of Barachias, mentioned by Jesus in Matthew 23:35 and Luke 11:51 as the last of the prophets murdered in the temple, <em>slain between the altar and the sanctuary</em> — likely Zechariah son of Jehoiada of 2 Chronicles 24:20–21, though the name Barachias raises questions about the identification.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zacharias", "smith": "zacharias"},
        "key_refs": ["Luke 1:5", "Luke 1:67", "Matthew 23:35"]
    },
    "zacher": {
        "id": "zacher",
        "term": "Zacher",
        "category": "people",
        "intro": "<p>Zacher was a son of Jehiel (also called Gibeon), the ancestor of Saul, listed in the Benjamite genealogy of 1 Chronicles 8:31. He is called Zechariah in the parallel list of 1 Chronicles 9:37. Gibeon was the patriarch of the Gibeonite branch of Benjamin from which Saul's family descended (1 Chronicles 9:35–39). Zacher appears only in these genealogical lists and plays no named role in the biblical narrative beyond establishing the lineage. The name is a shortened form of Zechariah, meaning <em>remembered</em> or <em>memorial</em>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zacher", "smith": "zacher", "isbe": "zacher"},
        "key_refs": ["1 Chronicles 8:31", "1 Chronicles 9:37"]
    },
    "zadok": {
        "id": "zadok",
        "term": "Zadok",
        "category": "people",
        "intro": "<p>Zadok (meaning <em>righteous</em>) was the high priest during the reigns of David and Solomon and the founding figure of the Zadokite priestly line that served Jerusalem until the Maccabean period. He was of the line of Eleazar son of Aaron (2 Samuel 8:17; 1 Chronicles 24:3). He is first mentioned joining David at Hebron with 22 commanders (1 Chronicles 12:27–28). During Absalom's rebellion, Zadok remained loyal and helped send intelligence to David through his son Ahimaaz (2 Samuel 15:24–29, 35–36; 17:15–21).</p><p>When Adonijah attempted to seize the throne before David's death, Zadok did not join the conspiracy; instead Nathan the prophet and Zadok anointed Solomon king by David's command (1 Kings 1:32–45). Solomon rewarded Zadok's loyalty by making him sole high priest, replacing Abiathar who had supported Adonijah (1 Kings 2:35). The Zadokite monopoly on the Jerusalem priesthood was so complete that Ezekiel's vision of the restored temple reserved the inner altar ministry exclusively for <em>the Levitical priests, the sons of Zadok</em> (Ezekiel 44:15; 40:46).</p>",
        "sections": [],
        "hitchcock_meaning": "just; justified",
        "source_ids": {"easton": "zadok", "smith": "zadok", "isbe": "zadok"},
        "key_refs": ["2 Samuel 8:17", "1 Kings 1:39", "1 Kings 2:35", "Ezekiel 44:15"]
    },
    "zair": {
        "id": "zair",
        "term": "Zair",
        "category": "places",
        "intro": "<p>Zair was the site where Joram king of Judah fought against Edom after the Edomites had revolted from Judah's rule (2 Kings 8:21). Joram went to Zair by night with all his chariots, was surrounded by the Edomites, and managed to break through with his chariot commanders, though the people fled to their tents. This battle marked the beginning of Edom's successful break from Judean control, a revolt that had been prophesied (Genesis 27:40). The location of Zair is uncertain; some equate it with Zoar near the Dead Sea, others with Zior in the hill country of Judah (Joshua 15:54).</p>",
        "sections": [],
        "hitchcock_meaning": "little; afflicted; in tribulation",
        "source_ids": {"easton": "zair", "smith": "zair", "isbe": "zair"},
        "key_refs": ["2 Kings 8:21"]
    },
    "zalmon": {
        "id": "zalmon",
        "term": "Zalmon",
        "category": "places",
        "intro": "<p>Zalmon is the name of two biblical sites. (1.) A hill near Shechem, from which Abimelech and his men cut down boughs to burn the stronghold of Shechem with its people inside (Judges 9:48). The attack destroyed the tower of Shechem and killed approximately a thousand men and women sheltering there. (2.) Zalmon is also mentioned in Psalm 68:14 in a striking image: <em>when the Almighty scattered kings there, snow fell on Zalmon</em> — possibly a metaphorical description of warriors falling pale as snow on the dark mountain, or a reference to a specific battle. The Zalmon near Shechem is likely identified with Jebel Suleiman or a nearby ridge.</p><p>Zalmon the Ahohite was also one of David's thirty mighty warriors (2 Samuel 23:28; 1 Chronicles 11:29), called Ilai in the Chronicles parallel.</p>",
        "sections": [],
        "hitchcock_meaning": "his shade; his image",
        "source_ids": {"easton": "zalmon", "smith": "zalmon", "isbe": "zalmon"},
        "key_refs": ["Judges 9:48", "Psalm 68:14", "2 Samuel 23:28"]
    },
    "zalmonah": {
        "id": "zalmonah",
        "term": "Zalmonah",
        "category": "places",
        "intro": "<p>Zalmonah was one of the camping stations of Israel in the wilderness, listed between Punon and Oboth in Numbers 33:41–42. The Israelites encamped there after departing from Mount Hor, in the circuit around Edom. The name may mean <em>shady</em> or relate to the root for <em>image</em> or <em>darkness</em>. The site has not been securely identified, though it lay in the Wadi Arabah south of the Dead Sea in the general region of modern Jordan. It is mentioned only in this wilderness itinerary list.</p>",
        "sections": [],
        "hitchcock_meaning": "the shade; the sound of the number; his shadow",
        "source_ids": {"easton": "zalmonah", "smith": "zalmonah", "isbe": "zalmonah"},
        "key_refs": ["Numbers 33:41"]
    },
    "zalmunna": {
        "id": "zalmunna",
        "term": "Zalmunna",
        "category": "people",
        "intro": "<p>Zalmunna was one of the two kings of Midian (along with Zebah) whom Gideon defeated and captured after the great rout at the spring of Harod (Judges 8:4–21). After the main Midianite army was routed, Gideon pursued the retreating kings across the Jordan with his 300 exhausted men. He asked the men of Succoth and Peniel for provisions, and when they refused to help, he threatened and later executed judgment on them. Capturing Zebah and Zalmunna at Karkor, Gideon returned and killed them himself to avenge his brothers slain at Tabor. Psalm 83:11 invokes the defeat of Zalmunna as a model for God's future judgment on Israel's enemies: <em>make their nobles like Zebah and Zalmunna.</em></p>",
        "sections": [],
        "hitchcock_meaning": "shadow; image; idol forbidden",
        "source_ids": {"easton": "zalmunna", "smith": "zalmunna"},
        "key_refs": ["Judges 8:5", "Judges 8:21", "Psalm 83:11"]
    },
    "zamzummims": {
        "id": "zamzummims",
        "term": "Zamzummims",
        "category": "people",
        "intro": "<p>The Zamzummims (also written Zuzims, Genesis 14:5) were a people of great stature who originally inhabited the land of Ammon before the Ammonites dispossessed them (Deuteronomy 2:20). They are described as a numerous and tall people like the Anakim. Deuteronomy 2:20 notes that the Ammonites called them Zamzummims, while Genesis 14:5 calls them Zuzims at Ham. Together with the Emim (dispossessed by Moab) and the Horim of Seir (dispossessed by Edom), the Zamzummims represent the pre-Israelite giants whose removal by these nations was seen as providential preparation for the peoples who would eventually become Israel's neighbors east of the Jordan.</p>",
        "sections": [],
        "hitchcock_meaning": "projects of crimes; enormous crimes",
        "source_ids": {"easton": "zamzummims"},
        "key_refs": ["Deuteronomy 2:20", "Genesis 14:5"]
    },
    "zanoah": {
        "id": "zanoah",
        "term": "Zanoah",
        "category": "places",
        "intro": "<p>Zanoah is the name of two towns in Judah. (1.) A town in the lowland (Shephelah) of Judah (Joshua 15:34), whose inhabitants helped repair the Valley Gate of Jerusalem under Nehemiah (Nehemiah 3:13) — a notably large section: five hundred cubits of wall. (2.) A town in the hill country of Judah (Joshua 15:56), apparently near Maon and Carmel. Additionally, a Calebite clan called Zanoah appears in the genealogy of Judah (1 Chronicles 4:18), perhaps the founding family of the town. The name may mean <em>abandoned</em> or <em>forgetfulness</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "forgetfulness; desertion",
        "source_ids": {"easton": "zanoah", "smith": "zanoah", "isbe": "zanoah"},
        "key_refs": ["Joshua 15:34", "Nehemiah 3:13"]
    },
    "zaphnath-paaneah": {
        "id": "zaphnath-paaneah",
        "term": "Zaphnath-paaneah",
        "category": "names",
        "intro": "<p>Zaphnath-paaneah was the Egyptian name given to Joseph by Pharaoh when he elevated him to the position of vizier over all Egypt (Genesis 41:45). The meaning of the name has been much debated: proposed interpretations include <em>revealer of secrets</em>, <em>the man to whom secrets are revealed</em>, <em>God speaks and lives</em>, <em>the bread of life of the age</em>, or in Egyptian <em>djed-nṯr-iw.f-ˁnḫ</em> meaning <em>God speaks and he lives</em>. The giving of an Egyptian name to a Hebrew vizier is consistent with Egyptian practice of assimilation of foreigners into the royal court, as confirmed by parallels in Egyptian administrative texts. The name signals Joseph's complete integration into Egyptian royal administration while the narrative maintains his Israelite identity.</p>",
        "sections": [],
        "hitchcock_meaning": "one who discovers hidden things",
        "source_ids": {"easton": "zaphnath-paaneah"},
        "key_refs": ["Genesis 41:45"]
    },
    "zarephath": {
        "id": "zarephath",
        "term": "Zarephath",
        "category": "places",
        "intro": "<p>Zarephath (meaning <em>smelting-shop</em> or <em>refinery</em>, Luke 4:26 <em>Sarepta</em>) was a small Phoenician coastal town between Tyre and Sidon, now identified with Sarafand about a mile from the coast. It was here that the prophet Elijah was sustained during the great three-and-a-half-year drought in the reign of Ahab. God directed him to a widow there — a Phoenician woman, not an Israelite — who miraculously fed Elijah with the last of her flour and oil, which were then replenished daily for the duration of the famine (1 Kings 17:8–16). When her son died, Elijah raised him to life (1 Kings 17:17–24).</p><p>Jesus cited this episode in his synagogue sermon at Nazareth (Luke 4:25–26) to illustrate that prophetic ministry is not confined to Israel: <em>there were many widows in Israel in the days of Elijah... yet Elijah was sent to none of them but only to Zarephath, in the land of Sidon, to a woman who was a widow.</em> Obadiah 20 lists Zarephath as a territory that will be recovered in the eschatological restoration.</p>",
        "sections": [],
        "hitchcock_meaning": "ambush of the mouth",
        "source_ids": {"easton": "zarephath", "smith": "zarephath", "isbe": "zarephath"},
        "key_refs": ["1 Kings 17:9", "1 Kings 17:14", "Luke 4:26", "Obadiah 20"]
    },
    "zaretan": {
        "id": "zaretan",
        "term": "Zaretan",
        "category": "places",
        "intro": "<p>Zaretan (also Zererath, Zeredah, Zarthan) was a place near the Jordan River associated with two significant events. When Israel crossed the Jordan into Canaan, the waters coming down from the north piled up in a heap <em>very far away, at a city called Adam, beside Zaretan</em> (Joshua 3:16), creating a dry crossing approximately 30 miles long. This miraculous crossing deliberately echoed the crossing of the Red Sea. Later, Solomon cast the bronze vessels for the temple in the clay ground of the Jordan valley <em>between Succoth and Zaretan</em> (1 Kings 7:46; 2 Chronicles 4:17 reads <em>Zeredah</em>). The exact site is uncertain but is generally placed near the confluence of the Jabbok with the Jordan.</p>",
        "sections": [],
        "hitchcock_meaning": "tribulation; perplexity",
        "source_ids": {"easton": "zaretan"},
        "key_refs": ["Joshua 3:16", "1 Kings 7:46"]
    },
    "zareth-shahar": {
        "id": "zareth-shahar",
        "term": "Zareth-shahar",
        "category": "places",
        "intro": "<p>Zareth-shahar (meaning <em>the splendor of dawn</em>) was a city in the territory allotted to the tribe of Reuben east of the Jordan, listed in Joshua 13:19 as situated <em>on the hill of the valley.</em> The exact location is unknown, though the name suggests a site with a notable eastern exposure or prominence. It appears only in this boundary list and plays no further role in the biblical narrative. Its placement among Reubenite cities in the Moabite plateau connects it to the broader Transjordanian territory taken from Sihon king of the Amorites.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zareth-shahar"},
        "key_refs": ["Joshua 13:19"]
    },
    "zarthan": {
        "id": "zarthan",
        "term": "Zarthan",
        "category": "places",
        "intro": "<p>Zarthan is an alternate spelling of Zaretan, used in 1 Kings 4:12 in the description of the administrative district of Baana son of Ahilud, which stretched from Taanach and Megiddo to all of Beth-shean by Zarthan below Jezreel. The same site appears as Zaretan in Joshua 3:16 (the Jordan crossing) and 1 Kings 7:46 (bronze casting for the temple). The variant spellings reflect different textual traditions and the difficulty of consistently transcribing place names across the Hebrew manuscripts. All references point to a location in the Jordan valley near the confluence of the Jordan and one of its tributaries.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zarthan", "smith": "zarthan", "isbe": "zarthan"},
        "key_refs": ["1 Kings 4:12", "1 Kings 7:46", "Joshua 3:16"]
    },
    "zatthu": {
        "id": "zatthu",
        "term": "Zatthu",
        "category": "people",
        "intro": "<p>Zatthu (also Zattu) was the ancestor of a family of 945 members who returned to Jerusalem from Babylonian exile with Zerubbabel (Ezra 2:8; Nehemiah 7:13). Some members of his family had intermarried with foreign women and are listed in Ezra 10:27 as participants in the penitential assembly that dissolved those marriages. A Zatthu also set his seal to Nehemiah's covenant of renewal (Nehemiah 10:14). The family appears to have been a substantial one in the early post-exilic community.</p>",
        "sections": [],
        "hitchcock_meaning": "olive tree",
        "source_ids": {"easton": "zatthu", "isbe": "zatthu"},
        "key_refs": ["Ezra 2:8", "Nehemiah 7:13", "Nehemiah 10:14"]
    },
    "zattu": {
        "id": "zattu",
        "term": "Zattu",
        "category": "people",
        "intro": "<p>Zattu is an alternate spelling of Zatthu — the head of a family among the returning exiles (Ezra 2:8; Nehemiah 7:13), with 845 or 945 members returning in the first wave under Zerubbabel (the numbers differ between Ezra and Nehemiah). Members of the family are named in Ezra 10:27 for having taken foreign wives. A Zattu appears in Nehemiah 10:14 among those who sealed the covenant of renewed obedience after Ezra's reading of the Law. The name may be related to an Akkadian or Aramaic root meaning <em>olive</em> or <em>noble.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zattu", "smith": "zattu", "isbe": "zattu"},
        "key_refs": ["Ezra 2:8", "Ezra 10:27", "Nehemiah 10:14"]
    },
    "zaza": {
        "id": "zaza",
        "term": "Zaza",
        "category": "people",
        "intro": "<p>Zaza was a son of Jonathan, listed in the genealogy of the sons of Jerahmeel in the tribe of Judah (1 Chronicles 2:33). He is mentioned only in this genealogical record and plays no further role in the biblical narrative. His brother was Peleth. The name may mean <em>belonging to all</em>. Zaza represents one of the many minor figures preserved in the Chronicler's extensive genealogical record of the tribes of Israel, whose names were maintained in the communal memory of Judah even without narrative significance.</p>",
        "sections": [],
        "hitchcock_meaning": "belonging to all",
        "source_ids": {"easton": "zaza", "smith": "zaza", "isbe": "zaza"},
        "key_refs": ["1 Chronicles 2:33"]
    },
    "zeal": {
        "id": "zeal",
        "term": "Zeal",
        "category": "concepts",
        "intro": "<p>Zeal in biblical vocabulary designates an earnest, passionate commitment to God and his honor — an inner fire that resists the compromise of what is sacred. The classic Old Testament exemplar is Phinehas, whose <em>zeal for God</em> in executing the Israelite man and Moabite woman who profaned the tabernacle stayed the plague and was credited to him as righteousness (Numbers 25:11–13; Psalm 106:30–31). Elijah twice declares: <em>I have been very jealous for the LORD, the God of hosts</em> (1 Kings 19:10, 14), where <em>jealous</em> and <em>zealous</em> translate the same Hebrew root <em>qin'ah</em>.</p><p>The New Testament distinguishes enlightened zeal from misdirected zeal: Paul acknowledges that his pre-conversion persecution of the church was <em>zeal</em> (Philippians 3:6), while acknowledging that Israel's zeal for God was <em>not according to knowledge</em> (Romans 10:2). Jesus's cleansing of the temple was associated with Psalm 69:9: <em>zeal for your house has consumed me</em> (John 2:17). Paul commends zeal in Romans 12:11 — <em>not slothful in zeal, fervent in spirit, serving the Lord</em> — and in 2 Corinthians 9:2 praises the Corinthians' <em>zeal</em> as stirring up others to generosity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zeal"},
        "key_refs": ["Numbers 25:11", "John 2:17", "Romans 10:2", "Philippians 3:6"]
    },
    "zealots": {
        "id": "zealots",
        "term": "Zealots",
        "category": "concepts",
        "intro": "<p>The Zealots were a Jewish political-religious movement that originated with Judas the Galilean (or Gaulonite), who led a revolt against the Roman census of 6 AD (Acts 5:37; Josephus, <em>Antiquities</em> 18.1). Their core principle was that paying tribute to Rome violated the exclusive kingship of God over Israel. Josephus describes them as a fourth sect alongside the Pharisees, Sadducees, and Essenes — sharing the Pharisees' theology but adding a radical political program. They refused submission to any earthly ruler and advocated violent resistance to Roman occupation.</p><p>The Zealot movement intensified through the first century and was a major force in the Jewish revolt of 66–70 AD, including the defense of Jerusalem against Vespasian and Titus. Their armed wing, the Sicarii (from Latin <em>sica</em>, dagger), carried concealed daggers and assassinated collaborators. Simon <em>the Zealot</em>, one of the twelve apostles (Luke 6:15; Acts 1:13), was apparently associated with or named after this movement, though Jesus's choice of both a Zealot and a tax-collector (Matthew) among his disciples is theologically significant — the kingdom transcending the political divisions of the day.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zealots"},
        "key_refs": ["Acts 5:37", "Luke 6:15", "Acts 1:13"]
    },
    "zebadiah": {
        "id": "zebadiah",
        "term": "Zebadiah",
        "category": "people",
        "intro": "<p>Zebadiah (meaning <em>the LORD has endowed</em>) is borne by nine biblical individuals. The most prominent are: (1.) A son of Asahel, nephew of Joab, who served as a military officer under Joash in the fourth month rotation (1 Chronicles 27:7). (2.) A Levite sent by Jehoshaphat to teach the Law throughout Judah (2 Chronicles 17:8). (3.) The son of Ishmael, a leader of Judah appointed by Jehoshaphat to administer civil affairs (2 Chronicles 19:11). (4.) The son of Michael, leader of 80 men from the family of Shephatiah who returned with Ezra from Babylon (Ezra 8:8). Several others of this name appear in 1 Chronicles and in the list of those with foreign wives in Ezra 10.</p>",
        "sections": [],
        "hitchcock_meaning": "portion of the Lord; the Lord is my portion",
        "source_ids": {"easton": "zebadiah", "smith": "zebadiah", "isbe": "zebadiah"},
        "key_refs": ["1 Chronicles 27:7", "2 Chronicles 17:8", "Ezra 8:8"]
    },
    "zebah": {
        "id": "zebah",
        "term": "Zebah",
        "category": "people",
        "intro": "<p>Zebah (meaning <em>sacrifice</em> or <em>victim</em>) was one of the two kings of Midian whom Gideon pursued and captured after the rout at the spring of Harod (Judges 8:4–21). He and Zalmunna had commanded the Midianite confederation that had oppressed Israel for seven years. After Gideon's 300 men routed the main army by their night attack, he pursued the fleeing kings across the Jordan. When captured, Zebah and Zalmunna acknowledged that the men they had killed at Tabor looked like Gideon — his brothers. Gideon executed them himself as a blood-avenger rather than allowing his son Jether to do it. Psalm 83:11 calls on God to make Israel's future enemies like Zebah and Zalmunna.</p>",
        "sections": [],
        "hitchcock_meaning": "victim; sacrifice",
        "source_ids": {"easton": "zebah", "smith": "zebah"},
        "key_refs": ["Judges 8:5", "Judges 8:21", "Psalm 83:11"]
    },
    "zebaim": {
        "id": "zebaim",
        "term": "Zebaim",
        "category": "places",
        "intro": "<p>Zebaim appears in Ezra 2:57 and Nehemiah 7:59 as the home of a family of <em>the sons of Solomon's servants</em> — temple servants who returned from Babylonian exile with Zerubbabel. The sons of Pochereth-hazzebaim (meaning <em>gazelle</em>) returned among this group. The name Zebaim may mean <em>gazelles</em> or <em>roe-bucks</em> and likely designates a place rather than a person. The site has not been identified, and the reference appears only in these two parallel administrative lists of returning exiles.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zebaim", "smith": "zebaim", "isbe": "zebaim"},
        "key_refs": ["Ezra 2:57", "Nehemiah 7:59"]
    },
    "zebedee": {
        "id": "zebedee",
        "term": "Zebedee",
        "category": "people",
        "intro": "<p>Zebedee was a Galilean fisherman, the husband of Salome (daughter of Mary Cleophas, sister of Mary the mother of Jesus, according to some traditions), and the father of James and John, two of Jesus's inner circle of disciples (Matthew 4:21; 27:56; Mark 15:40). He operated a fishing business at Capernaum with hired servants, suggesting a degree of prosperity (Mark 1:20). When Jesus called James and John, they immediately left their father and his hired men in the boat — a decisive break with their family livelihood. Zebedee himself makes no further significant appearance in the Gospels, and tradition records nothing of his subsequent history. Salome was among the women at the crucifixion and at the empty tomb (Mark 15:40; 16:1).</p>",
        "sections": [],
        "hitchcock_meaning": "abundant; portion",
        "source_ids": {"easton": "zebedee", "smith": "zebedee", "isbe": "zebedee"},
        "key_refs": ["Matthew 4:21", "Mark 1:19", "Mark 15:40"]
    },
    "zeboim": {
        "id": "zeboim",
        "term": "Zeboim",
        "category": "places",
        "intro": "<p>Zeboim (also Zeboiim) is the name of two biblical locations. (1.) One of the five cities of the plain (along with Sodom, Gomorrah, Admah, and Bela/Zoar) whose king was defeated by Chedorlaomer in the battle of the Vale of Siddim (Genesis 14:2, 8). When God destroyed Sodom and Gomorrah for their wickedness, Zeboim and Admah were also destroyed, while Bela (Zoar) was spared at Lot's request. Hosea 11:8 references their destruction as a measure of God's threatened judgment against Israel — yet God's love restrained him from making Ephraim like Zeboim. (2.) A town in Benjamin, resettled after the exile (Nehemiah 11:34). A valley of Hyenas (<em>ge ha-zebo'im</em>) in Benjamin is also mentioned in 1 Samuel 13:18.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zeboim", "smith": "zeboim", "isbe": "zeboim"},
        "key_refs": ["Genesis 14:2", "Hosea 11:8", "Nehemiah 11:34"]
    },
    "zebudah": {
        "id": "zebudah",
        "term": "Zebudah",
        "category": "people",
        "intro": "<p>Zebudah was the mother of Jehoiakim king of Judah, daughter of Pedaiah of Rumah (2 Kings 23:36). She is identified in the regnal summary at the beginning of Jehoiakim's reign, following the standard formula for Judean kings that names both the king's age at accession and his mother. Jehoiakim (originally named Eliakim) was placed on the throne by Pharaoh Neco after he deposed his brother Jehoahaz, and he reigned eleven years. His reign was marked by subservience to Egypt and then Babylon and by hostility to the prophet Jeremiah. The name Zebudah means <em>endowed</em> or <em>given.</em></p>",
        "sections": [],
        "hitchcock_meaning": "endowed; endowing",
        "source_ids": {"easton": "zebudah", "smith": "zebudah", "isbe": "zebudah"},
        "key_refs": ["2 Kings 23:36"]
    },
    "zebul": {
        "id": "zebul",
        "term": "Zebul",
        "category": "people",
        "intro": "<p>Zebul was the ruler (governor or prefect) of Shechem under Abimelech during the latter's short-lived kingship (Judges 9:28–41). When Gaal son of Ebed stirred up the Shechemites against Abimelech, Zebul sent a secret warning to Abimelech advising him to march against the city at night. The next morning, Zebul taunted Gaal — <em>Where is your mouth now, you who said, 'Who is Abimelech that we should serve him?'</em> — as Abimelech's forces appeared. When Gaal and his brothers fled, Zebul expelled them from Shechem. He disappears from the narrative after this episode, which ended with Abimelech destroying Shechem and killing its inhabitants.</p>",
        "sections": [],
        "hitchcock_meaning": "a habitation",
        "source_ids": {"easton": "zebul", "smith": "zebul", "isbe": "zebul"},
        "key_refs": ["Judges 9:28", "Judges 9:36", "Judges 9:41"]
    },
    "zebulonite": {
        "id": "zebulonite",
        "term": "Zebulonite",
        "category": "names",
        "intro": "<p>Zebulonite is the gentile term for a member of the tribe of Zebulun. It appears in Judges 12:11–12 in connection with Elon the Zebulonite, one of the minor judges who governed Israel for ten years and was buried at Aijalon in the land of Zebulun. The designation simply identifies him as belonging to Zebulun. Members of Zebulun are called Zebulunites in Numbers 26:27, where the clans of Zebulun are enumerated after the second wilderness census. The tribe was known for its maritime and commercial character, consistent with Jacob's blessing that Zebulun would dwell at the shore of the sea and become a haven for ships (Genesis 49:13).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zebulonite", "smith": "zebulonite", "isbe": "zebulonite"},
        "key_refs": ["Judges 12:11", "Numbers 26:27"]
    },
    "zebulun": {
        "id": "zebulun",
        "term": "Zebulun",
        "category": "people",
        "intro": "<p>Zebulun (meaning <em>dwelling</em> or <em>honor</em>) was the sixth and youngest son of Jacob and Leah (Genesis 30:20). Leah named him saying, <em>God has endowed me with a good endowment; now my husband will honor me, because I have borne him six sons.</em> He had three sons: Sered, Elon, and Jahleel (Genesis 46:14). Jacob's blessing for Zebulun (Genesis 49:13) predicted: <em>Zebulun shall dwell at the shore of the sea; he shall become a haven for ships, and his border shall be at Sidon</em> — pointing toward maritime trade and Phoenician connections, though Zebulun's historical territory was actually inland between Issachar and Asher.</p><p>The tribe of Zebulun played a significant role in Israel's early history: Zebulunites fought valiantly against Sisera (Judges 4–5; Psalm 68:27), and Elon the Zebulonite judged Israel for ten years (Judges 12:11–12). The tribe's territory in lower Galilee was prophetically linked by Isaiah 9:1–2 and Matthew 4:13–15 to the region where the Messiah's light would dawn.</p>",
        "sections": [],
        "hitchcock_meaning": "Zebulon, dwelling; habitation",
        "source_ids": {"easton": "zebulun", "smith": "zebulun", "isbe": "zebulun"},
        "key_refs": ["Genesis 30:20", "Genesis 49:13", "Isaiah 9:1", "Matthew 4:13"]
    },
    "zebulun-lot-of": {
        "id": "zebulun-lot-of",
        "term": "Zebulun, Lot of",
        "category": "places",
        "intro": "<p>The lot of Zebulun was the territory allotted to the tribe of Zebulun in the distribution of Canaan under Joshua (Joshua 19:10–16). The allotment was in lower Galilee, bounded by Asher on the west and northwest, Naphtali on the north and northeast, and Issachar on the south. It included the cities of Sarid, Chisloth-tabor, Daberath, Japhia, Gath-hepher (hometown of Jonah), Beth-lehem of Zebulun (not the Bethlehem of Judah), and Bethel. The plain of Jezreel lay to the south of the territory. Though the tribe's inheritance was inland, Jacob's blessing prophesied maritime connections (Genesis 49:13) — possibly reflecting Zebulun's later role as a commercial intermediary between the Mediterranean coast and the interior trade routes.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zebulun-lot-of"},
        "key_refs": ["Joshua 19:10", "Genesis 49:13"]
    },
    "zebulun-tribe-of": {
        "id": "zebulun-tribe-of",
        "term": "Zebulun, Tribe of",
        "category": "people",
        "intro": "<p>The tribe of Zebulun descended from Zebulun the sixth son of Jacob and Leah, through his three sons Sered, Elon, and Jahleel (Numbers 26:26–27). In the first wilderness census Zebulun numbered 57,400 men of military age (Numbers 1:31); in the second census 60,500 (Numbers 26:27). The tribe settled in lower Galilee, a region of fertile land and significant commercial activity on the trade routes between Egypt and Mesopotamia.</p><p>Zebulunites were praised for risking their lives in Deborah's victory over Sisera (Judges 5:18) and responded to David's call in significant numbers (1 Chronicles 12:33). When Hezekiah sent invitations to observe the Passover, some from Zebulun humbled themselves and came to Jerusalem (2 Chronicles 30:10–11). The tribe's territory, later part of the Assyrian province of Megiddo after the deportations of 733–732 BC, was prophetically described as the land where the Messiah's light would dawn (Isaiah 9:1–2; Matthew 4:15).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zebulun-tribe-of"},
        "key_refs": ["Numbers 1:31", "Judges 5:18", "Isaiah 9:1"]
    },
    "zechariah": {
        "id": "zechariah",
        "term": "Zechariah",
        "category": "people",
        "intro": "<p>Zechariah (meaning <em>the LORD has remembered</em>) is one of the most common names in the Old Testament, borne by over thirty individuals. The most prominent are: (1.) Zechariah the prophet, son of Berechiah, grandson of Iddo (Zechariah 1:1; Ezra 5:1; 6:14), who prophesied in Jerusalem beginning in 520 BC, contemporaneously with Haggai. His book (Zechariah 1–14) contains eight night visions, a series of oracles, and two apocalyptic sections (chs. 9–14) rich in messianic content: the humble king entering Jerusalem on a donkey (9:9), thirty pieces of silver (11:12–13), the pierced one whom they look upon (12:10), and the shepherd struck and the sheep scattered (13:7).</p><p>(2.) Zechariah king of Israel, son of Jeroboam II, who reigned six months before being assassinated by Shallum (2 Kings 15:8–12) — see Zachariah. (3.) Zechariah son of Jehoiada the priest, who was stoned in the temple court under Joash for his prophetic reproof, saying: <em>the LORD sees and avenge</em> (2 Chronicles 24:20–22). Jesus cited this as the last murder of a prophet (Matthew 23:35; Luke 11:51). (4.) Zechariah the father of John the Baptist: see Zacharias.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Zachariah",
        "source_ids": {"easton": "zechariah", "smith": "zechariah"},
        "key_refs": ["Zechariah 1:1", "Zechariah 9:9", "Zechariah 12:10", "2 Chronicles 24:21"]
    },
    "zedad": {
        "id": "zedad",
        "term": "Zedad",
        "category": "places",
        "intro": "<p>Zedad was a place on the northern boundary of the promised land as described in both Numbers 34:8 and Ezekiel 47:15. The boundary runs from the entrance of Hamath (the Beqa Valley between Lebanon and Anti-Lebanon) past Zedad toward Ziphron. The site is generally identified with Sadad, a village about 70 miles northeast of Damascus in modern Syria, on the road between Homs and Damascus. The biblical geography of the northern border is difficult to reconstruct precisely, but Zedad served as one of the landmark points defining the idealized extent of Israel's promised territory.</p>",
        "sections": [],
        "hitchcock_meaning": "his side; his hunting",
        "source_ids": {"easton": "zedad", "smith": "zedad", "isbe": "zedad"},
        "key_refs": ["Numbers 34:8", "Ezekiel 47:15"]
    },
    "zedekiah": {
        "id": "zedekiah",
        "term": "Zedekiah",
        "category": "people",
        "intro": "<p>Zedekiah (meaning <em>the LORD is my righteousness</em>) was the last king of Judah (597–586 BC), placed on the throne by Nebuchadnezzar after the deportation of Jehoiachin. His original name was Mattaniah; Nebuchadnezzar changed it to Zedekiah. He was the third son of Josiah and thus uncle to Jehoiachin (2 Kings 24:17–18). His eleven-year reign was marked by vacillation between submission to Babylon and appeals to Egypt, by hostility to Jeremiah whose counsel he privately sought but publicly ignored, and ultimately by a catastrophic rebellion against Babylon.</p><p>Nebuchadnezzar besieged Jerusalem for eighteen months (589–586 BC). Zedekiah attempted to escape through the breach in the wall by night, was caught on the plains of Jericho, brought to Nebuchadnezzar at Riblah, and forced to watch his sons killed before his eyes — the last thing he saw, for his eyes were then put out and he was carried in bronze chains to Babylon (2 Kings 25:4–7; Jeremiah 52:7–11). Jerusalem was burned, and the temple destroyed. Ezekiel had prophesied that Zedekiah would die in Babylon but would not <em>see</em> it — fulfilled precisely (Ezekiel 12:13).</p>",
        "sections": [],
        "hitchcock_meaning": "the Lord is my justice; the justice of the Lord",
        "source_ids": {"easton": "zedekiah", "smith": "zedekiah"},
        "key_refs": ["2 Kings 24:17", "2 Kings 25:7", "Jeremiah 52:11", "Ezekiel 12:13"]
    },
    "zeeb": {
        "id": "zeeb",
        "term": "Zeeb",
        "category": "people",
        "intro": "<p>Zeeb (meaning <em>wolf</em>) was one of two princes of Midian (with Oreb, meaning <em>raven</em>) captured and killed by the men of Ephraim during the rout following Gideon's defeat of the Midianite host (Judges 7:25; 8:3). The Ephraimites were called up to capture the fords of the Jordan and prevent the Midianites' escape. They captured Oreb at the rock of Oreb and Zeeb at the winepress of Zeeb, and brought their heads to Gideon across the Jordan. Isaiah 10:26 later invokes the slaughter at the rock of Oreb as a type of God's future judgment on Assyria: <em>the LORD of hosts will wield against them a whip, as when he struck Midian at the rock of Oreb.</em></p>",
        "sections": [],
        "hitchcock_meaning": "wolf",
        "source_ids": {"easton": "zeeb", "smith": "zeeb", "isbe": "zeeb"},
        "key_refs": ["Judges 7:25", "Judges 8:3", "Isaiah 10:26", "Psalm 83:11"]
    },
    "zelah": {
        "id": "zelah",
        "term": "Zelah",
        "category": "places",
        "intro": "<p>Zelah was a town in the territory of Benjamin (Joshua 18:28) and the burial place of the family of Kish: <em>they buried the bones of Saul and his son Jonathan in the country of Benjamin in Zelah, in the tomb of Kish his father</em> (2 Samuel 21:14). This burial followed David's delivery of the bones of Saul and Jonathan from Jabesh-gilead, where the Jabesh-gileadites had retrieved them after the Philistines had displayed them at Beth-shean. The interment at Zelah finally gave Saul's family an honorable burial in their ancestral territory, after which <em>God responded to the plea for the land.</em> The site has not been positively identified.</p>",
        "sections": [],
        "hitchcock_meaning": "rib; side; halting",
        "source_ids": {"easton": "zelah", "smith": "zelah"},
        "key_refs": ["Joshua 18:28", "2 Samuel 21:14"]
    },
    "zelek": {
        "id": "zelek",
        "term": "Zelek",
        "category": "people",
        "intro": "<p>Zelek the Ammonite was one of David's thirty mighty warriors (2 Samuel 23:37; 1 Chronicles 11:39). His Ammonite origin is notable since the Ammonites were generally enemies of Israel (Deuteronomy 23:3), though individuals from surrounding nations sometimes entered Israelite service — as did Uriah the Hittite, another of the thirty. Zelek's presence in David's elite corps reflects the cosmopolitan character of David's royal army, which included Cherethites, Pelethites, and various foreigners alongside Israelites. Beyond this brief listing he appears nowhere else in the biblical record.</p>",
        "sections": [],
        "hitchcock_meaning": "the shadow or noise of him that licks or laps",
        "source_ids": {"easton": "zelek", "isbe": "zelek"},
        "key_refs": ["2 Samuel 23:37", "1 Chronicles 11:39"]
    },
    "zelophehad": {
        "id": "zelophehad",
        "term": "Zelophehad",
        "category": "people",
        "intro": "<p>Zelophehad was a Manassite who died in the wilderness leaving only daughters and no sons (Numbers 27:1–11; 36:1–12; Joshua 17:3–6). His five daughters — Mahlah, Noah, Hoglah, Milcah, and Tirzah — brought their case before Moses, Eleazar, and the whole congregation, arguing that their father's name should not disappear from his clan because he had no son. Their petition succeeded: God ruled through Moses that daughters may inherit when there is no son, establishing a landmark legal precedent in Israelite property law. Numbers 36 adds the requirement that such daughters marry within their own tribe to prevent the transfer of tribal land.</p><p>Zelophehad's daughters are cited in Joshua 17:3–6 as actually receiving their inheritance, and they reappear in 1 Chronicles 7:15 in the Manassite genealogy. Their case became a touchstone for discussions of inheritance law in later rabbinic tradition.</p>",
        "sections": [],
        "hitchcock_meaning": "the shade or tingling of fear",
        "source_ids": {"easton": "zelophehad", "smith": "zelophehad", "isbe": "zelophehad"},
        "key_refs": ["Numbers 27:1", "Numbers 27:7", "Joshua 17:3"]
    },
    "zelotes": {
        "id": "zelotes",
        "term": "Zelotes",
        "category": "names",
        "intro": "<p>Zelotes is the Greek word meaning <em>zealot</em> or <em>one who is zealous</em>, used as a surname for Simon the apostle to distinguish him from Simon Peter (Luke 6:15; Acts 1:13). The surname indicates Simon's affiliation with or sympathy for the Zealot movement — the party of Jewish nationalists who refused submission to Rome and advocated violent resistance. Whether Simon remained a Zealot in the political sense after joining Jesus, or whether the surname was merely a pre-conversion designation preserved as a distinguishing title, is not made explicit in the text. Jesus's call of both a Zealot and a tax-collector (Matthew/Levi) into the same apostolic band is considered theologically significant — the kingdom transcending the era's sharpest social and political divisions.</p>",
        "sections": [],
        "hitchcock_meaning": "zealous",
        "source_ids": {"easton": "zelotes", "smith": "zelotes", "isbe": "zelotes"},
        "key_refs": ["Luke 6:15", "Acts 1:13"]
    },
    "zemaraim": {
        "id": "zemaraim",
        "term": "Zemaraim",
        "category": "places",
        "intro": "<p>Zemaraim is the name of two biblical sites. (1.) A town in the territory of Benjamin (Joshua 18:22), possibly identified with es-Sumra, northeast of Jericho. (2.) Mount Zemaraim in the hill country of Ephraim, the site of a confrontation between King Abijah of Judah and Jeroboam I of Israel (2 Chronicles 13:4). From this mount Abijah addressed the combined forces of both kingdoms before battle, rebuking Jeroboam for rebelling against the Davidic house and for introducing golden calves. Despite being outnumbered, Judah won a decisive victory because, as the text explains, <em>Judah prevailed, because they relied on the LORD, the God of their fathers</em> (2 Chronicles 13:18).</p>",
        "sections": [],
        "hitchcock_meaning": "wool; pith",
        "source_ids": {"easton": "zemaraim", "smith": "zemaraim", "isbe": "zemaraim"},
        "key_refs": ["Joshua 18:22", "2 Chronicles 13:4"]
    },
    "zemarite": {
        "id": "zemarite",
        "term": "Zemarite",
        "category": "names",
        "intro": "<p>The Zemarites were one of the Canaanite peoples descended from Canaan son of Ham, listed in the Table of Nations (Genesis 10:18; 1 Chronicles 1:16). They are generally associated with the ancient city of Sumur (Simyra) on the Phoenician coast of northern Syria, near the mouth of the Eleutheros River, known from Egyptian records and the Amarna letters. Like the Sinites and other coastal Canaanite peoples in the Table of Nations, the Zemarites represent one of the nations whose territory God promised to give to Abraham's descendants (Genesis 15:18–21). They appear only in these genealogical lists and are not mentioned in narrative contexts.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zemarite", "isbe": "zemarite"},
        "key_refs": ["Genesis 10:18", "1 Chronicles 1:16"]
    },
    "zemira": {
        "id": "zemira",
        "term": "Zemira",
        "category": "people",
        "intro": "<p>Zemira was a son of Becher, grandson of Benjamin, listed in the tribal genealogy of Benjamin in 1 Chronicles 7:8. He appears among the sons of Becher alongside eight other brothers. The Bicherites (sons of Becher) were a branch of the tribe of Benjamin numbered among the men of valor in their genealogy (1 Chronicles 7:9). Zemira appears only in this genealogical list and plays no further role in the biblical narrative. The name may mean <em>song</em> or <em>vine</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "song; vine; palm",
        "source_ids": {"easton": "zemira", "smith": "zemira"},
        "key_refs": ["1 Chronicles 7:8"]
    },
    "zenas": {
        "id": "zenas",
        "term": "Zenas",
        "category": "people",
        "intro": "<p>Zenas the lawyer was a Christian mentioned by Paul in Titus 3:13, where Paul instructs Titus: <em>Do your best to speed Zenas the lawyer and Apollos on their way; see that they lack nothing.</em> Zenas and Apollos were apparently traveling through Crete carrying this letter from Paul to Titus, and Paul asks Titus to provide for their needs before they continue their journey. The designation <em>lawyer</em> (<em>nomikos</em>) may indicate either expertise in Jewish Torah law (as a trained scribe) or in Roman civil law, though the former is more likely in a Christian context. He is otherwise unknown, though early church tradition sometimes identifies him with one of the seventy disciples.</p>",
        "sections": [],
        "hitchcock_meaning": "living",
        "source_ids": {"easton": "zenas", "smith": "zenas", "isbe": "zenas"},
        "key_refs": ["Titus 3:13"]
    },
    "zephaniah": {
        "id": "zephaniah",
        "term": "Zephaniah",
        "category": "people",
        "intro": "<p>Zephaniah (meaning <em>the LORD has hidden</em> or <em>the LORD is my treasure</em>) was the ninth of the twelve minor prophets, son of Cushi and great-great-grandson of Hezekiah. He prophesied during the reign of Josiah (640–609 BC), making him a contemporary of Jeremiah and likely contributing to the spiritual atmosphere that led to Josiah's reforms after the discovery of the Law book (621 BC). His genealogy's unusual depth (four generations back to Hezekiah) has led many to identify him as a descendant of the royal house.</p><p>The book of Zephaniah opens with one of the most sweeping declarations of universal judgment in all prophecy: <em>I will utterly sweep away everything from the face of the earth</em> (Zephaniah 1:2–3). The heart of the book is the theme of the <em>Day of the LORD</em> — a day of wrath, distress, ruin, devastation, darkness, and gloom (1:14–18) that became the basis of the medieval <em>Dies irae</em> hymn. Yet the book closes with a tender vision of the restored remnant and the LORD himself dwelling in their midst, rejoicing over his people with singing (3:14–17).</p>",
        "sections": [],
        "hitchcock_meaning": "the Lord is my secret",
        "source_ids": {"easton": "zephaniah", "smith": "zephaniah", "isbe": "zephaniah"},
        "key_refs": ["Zephaniah 1:1", "Zephaniah 1:14", "Zephaniah 3:17"]
    },
    "zephath": {
        "id": "zephath",
        "term": "Zephath",
        "category": "places",
        "intro": "<p>Zephath was a Canaanite city captured by Judah and Simeon early in the period of the judges and renamed Hormah (meaning <em>devoted to destruction</em>) after its complete destruction (Judges 1:17). The same site had previously been called Hormah after an earlier Israelite vow to destroy it (Numbers 21:3). The city lay in the Negeb, the southern wilderness region, and its location is tentatively identified with Tell esh-Sharia or Khirbet el-Meshash. Hormah was later assigned to Simeon within Judah's territory (Joshua 15:30; 19:4) and appears in the list of cities to which David sent spoil from his raid on the Amalekites (1 Samuel 30:30).</p>",
        "sections": [],
        "hitchcock_meaning": "which beholds; that attends or that covers",
        "source_ids": {"easton": "zephath", "smith": "zephath", "isbe": "zephath"},
        "key_refs": ["Judges 1:17", "Numbers 21:3"]
    },
    "zephathah": {
        "id": "zephathah",
        "term": "Zephathah",
        "category": "places",
        "intro": "<p>Zephathah was a valley near Mareshah in the Shephelah of Judah where King Asa of Judah met and defeated Zerah the Ethiopian in a massive battle (2 Chronicles 14:9–15). The Chronicler describes Zerah's army as one million men and three hundred chariots, a number generally taken as a literary expression of overwhelming force rather than a precise count. Asa's prayer before battle — <em>LORD, there is no one besides you to help, between the mighty and the weak</em> (2 Chronicles 14:11) — became a model of dependence on God in warfare, and the subsequent rout was attributed entirely to divine action. The valley is not identified with certainty, but Mareshah is located in the western Shephelah near modern Tell Sandahanna.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zephathah", "smith": "zephathah"},
        "key_refs": ["2 Chronicles 14:10", "2 Chronicles 14:11"]
    },
    "zerah": {
        "id": "zerah",
        "term": "Zerah",
        "category": "people",
        "intro": "<p>Zerah (meaning <em>sunrise</em> or <em>a rising of light</em>) is a name borne by several biblical individuals. (1.) A son of Reuel and grandson of Esau, a clan chief of Edom (Genesis 36:13, 17). (2.) Zerah and Perez were twin sons of Judah by his daughter-in-law Tamar (Genesis 38:30); Zerah thrust out his hand first and the midwife tied a scarlet thread on his wrist, but Perez broke through first, hence his name. The clan of Zerah (Zarhites) appears in Joshua 7:17–24 in the story of Achan, and in the genealogies of 1 Chronicles 2:4–6 and 9:6. (3.) Zerah the Ethiopian (Cushite) — probably Osorkon II of Egypt — who invaded Judah with a massive army in the reign of Asa and was decisively defeated at Zephathah (2 Chronicles 14:9–15). (4.) A Simeonite (Numbers 26:13; 1 Chronicles 4:24). (5.) A Levite (1 Chronicles 6:21, 41).</p>",
        "sections": [],
        "hitchcock_meaning": "same as Zarah",
        "source_ids": {"easton": "zerah", "smith": "zerah", "isbe": "zerah"},
        "key_refs": ["Genesis 38:30", "2 Chronicles 14:9", "Joshua 7:17"]
    },
    "zered": {
        "id": "zered",
        "term": "Zered",
        "category": "places",
        "intro": "<p>The brook Zered (also Wadi Zered) was the boundary stream between Moab and Edom that the Israelites crossed in their wilderness journey around Edom (Numbers 21:12; Deuteronomy 2:13–14). The crossing of the Zered marked a significant transition: it was at this point that the entire generation of men who had left Egypt in military readiness had perished over the thirty-eight years since Kadesh-barnea, just as the LORD had sworn (Deuteronomy 2:14–16). The Zered is generally identified with the modern Wadi el-Hesa, which flows into the southeastern end of the Dead Sea and forms the southern boundary of the plateau of Moab.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zered", "smith": "zered", "isbe": "zered"},
        "key_refs": ["Numbers 21:12", "Deuteronomy 2:13"]
    },
    "zereda": {
        "id": "zereda",
        "term": "Zereda",
        "category": "places",
        "intro": "<p>Zereda was the birthplace of Jeroboam son of Nebat, who would become the first king of the northern kingdom of Israel (1 Kings 11:26). It was located in the hill country of Ephraim, though the exact site is uncertain. Some scholars identify it with Zarethan of 1 Kings 7:46 (where Solomon cast the bronze vessels) or with Zeredah of 2 Chronicles 4:17. Jeroboam's Ephraimite origin from this location is noted in connection with his mother Zeruah, who was a widow. The town may be modern Deir Ghassaneh or another site in the same region.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zereda", "smith": "zereda"},
        "key_refs": ["1 Kings 11:26"]
    },
    "zeredathah": {
        "id": "zeredathah",
        "term": "Zeredathah",
        "category": "places",
        "intro": "<p>Zeredathah is named in 2 Chronicles 4:17 as the location in the Jordan valley between Succoth and Zeredathah where Hiram the craftsman cast the bronze vessels for Solomon's temple — the pillars, the sea, and the various basins and implements. The parallel passage in 1 Kings 7:46 reads <em>Zarethan</em> rather than Zeredathah, and the two are generally considered the same site or closely related locations in the Jordan valley. The clay ground of this region was ideal for casting large bronze objects. The location corresponds roughly to the junction of the Jordan and Jabbok rivers.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zeredathah", "smith": "zeredathah"},
        "key_refs": ["2 Chronicles 4:17", "1 Kings 7:46"]
    },
    "zererath": {
        "id": "zererath",
        "term": "Zererath",
        "category": "places",
        "intro": "<p>Zererath appears in Judges 7:22 in the account of Gideon's rout of the Midianites: when the three hundred men blew their trumpets and the LORD set every man's sword against his comrade throughout the Midianite camp, the army fled to <em>Beth-shittah toward Zererath, as far as the border of Abel-meholah, by Tabbath.</em> The site is otherwise unknown and its location uncertain. It may be identical with Zarethan or Zaretan in the Jordan valley, or it may be a variant form of the same toponym. The reference indicates a Midianite flight eastward toward the Jordan valley.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zererath", "smith": "zererath"},
        "key_refs": ["Judges 7:22"]
    },
    "zeresh": {
        "id": "zeresh",
        "term": "Zeresh",
        "category": "people",
        "intro": "<p>Zeresh was the wife of Haman the Agagite, the powerful official of Ahasuerus who sought to destroy the Jewish people throughout the Persian Empire (Esther 5:10, 14; 6:13). After Haman's humiliation at having to honor Mordecai publicly, he poured out his humiliation to Zeresh and his friends. Zeresh and the wise men gave Haman an ominous counsel — that if Mordecai was of Jewish origin, Haman would certainly fall before him and could not prevail. This prophetic warning went unheeded; Haman was hanged on the very gallows he had prepared for Mordecai (Esther 7:9–10). The name Zeresh may derive from a Persian root meaning <em>gold</em> or <em>misery</em>.</p>",
        "sections": [],
        "hitchcock_meaning": "misery; strange; dispersed inheritance",
        "source_ids": {"easton": "zeresh", "smith": "zeresh", "isbe": "zeresh"},
        "key_refs": ["Esther 5:10", "Esther 6:13", "Esther 7:10"]
    },
    "zeruah": {
        "id": "zeruah",
        "term": "Zeruah",
        "category": "people",
        "intro": "<p>Zeruah was the widowed mother of Jeroboam son of Nebat, who became the first king of the northern kingdom of Israel after the division of the monarchy (1 Kings 11:26). She is mentioned only in this single verse which identifies Jeroboam's parentage. Her status as a widow at the time of Jeroboam's rise is noted, perhaps to explain his ambition and self-reliance. The name means <em>leprous</em> or <em>full of ringworm</em>, though this may be a descriptive designation applied later rather than a given name. She is one of a number of widowed mothers in the Old Testament whose sons rose to prominence.</p>",
        "sections": [],
        "hitchcock_meaning": "leprous; wasp; hornet",
        "source_ids": {"easton": "zeruah", "smith": "zeruah", "isbe": "zeruah"},
        "key_refs": ["1 Kings 11:26"]
    },
    "zerubbabel": {
        "id": "zerubbabel",
        "term": "Zerubbabel",
        "category": "people",
        "intro": "<p>Zerubbabel (meaning <em>seed of Babylon</em> or <em>born in Babylon</em>) was the civil governor of Judah who led the first return of Jewish exiles from Babylon around 538 BC under the edict of Cyrus the Great (Ezra 1–2; Nehemiah 7:7). He was of the Davidic line, grandson of the exiled King Jehoiachin (1 Chronicles 3:17–19; Matthew 1:12–13 as Zorobabel). Together with the high priest Jeshua (Joshua) son of Jehozadak, he led the community that rebuilt the altar, restored the feast calendar, and laid the foundation of the second temple (Ezra 3–4).</p><p>Opposition from the peoples of the land halted construction for approximately fifteen years, until the prophets Haggai and Zechariah roused Zerubbabel and Jeshua to resume building in 520 BC (Ezra 5:1–2; Haggai 1:1–15). The temple was completed in 516 BC (Ezra 6:15). Haggai's prophecy gave Zerubbabel extraordinary messianic significance: <em>I will make you like a signet ring, for I have chosen you</em> (Haggai 2:23) — reversing the curse on his grandfather Jehoiachin (Jeremiah 22:24) and signaling the restoration of the Davidic line. Zechariah's vision of the golden lampstand with Zerubbabel's hands laying the capstone (Zechariah 4:6–10) similarly portrays him as the one through whom God would complete his purposes.</p>",
        "sections": [],
        "hitchcock_meaning": "a stranger at Babylon; dispersion of confusion",
        "source_ids": {"easton": "zerubbabel", "smith": "zerubbabel", "isbe": "zerubbabel"},
        "key_refs": ["Ezra 3:2", "Haggai 1:1", "Haggai 2:23", "Zechariah 4:9"]
    },
    "zeruiah": {
        "id": "zeruiah",
        "term": "Zeruiah",
        "category": "people",
        "intro": "<p>Zeruiah was the mother of three of David's most prominent military commanders: Joab, Abishai, and Asahel (2 Samuel 2:18; 1 Chronicles 2:16). She was a sister of David (1 Chronicles 2:16), making her sons his nephews. The consistent scriptural designation of these commanders as <em>sons of Zeruiah</em> rather than identifying them by their father (who is never named) has been noted as unusual; it may reflect that Zeruiah was the more prominent or formidable parent, or that her husband died early. David repeatedly lamented that the <em>sons of Zeruiah</em> were too hard for him (2 Samuel 3:39; 16:10; 19:22) — acknowledging their fierce loyalty but recognizing that their methods sometimes exceeded or complicated his own intentions.</p>",
        "sections": [],
        "hitchcock_meaning": "pain or tribulation of the Lord",
        "source_ids": {"easton": "zeruiah", "smith": "zeruiah", "isbe": "zeruiah"},
        "key_refs": ["2 Samuel 2:18", "1 Chronicles 2:16", "2 Samuel 3:39"]
    },
    "zetham": {
        "id": "zetham",
        "term": "Zetham",
        "category": "people",
        "intro": "<p>Zetham was a Levite of the clan of Gershon (1 Chronicles 23:8; 26:22), assigned to assist with the treasuries of the house of God in David's organization of the temple personnel. He appears in both the list of Gershonite Levites (23:8, as son of Laadan) and in the list of treasury overseers (26:22, as sons of Jehiel). The Gershonites were responsible for carrying the curtains and coverings of the Tabernacle in the wilderness period, and their descendants continued to have roles in the temple service. The name Zetham may relate to the word for <em>olive</em>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zetham", "smith": "zetham", "isbe": "zetham"},
        "key_refs": ["1 Chronicles 23:8", "1 Chronicles 26:22"]
    },
    "zethan": {
        "id": "zethan",
        "term": "Zethan",
        "category": "people",
        "intro": "<p>Zethan was a son of Bilhan and great-grandson of Benjamin, listed in the tribal genealogy of Benjamin in 1 Chronicles 7:10. He is mentioned alongside his brothers as a head of his father's household and one of the mighty warriors of Benjamin. He appears only in this genealogical record and plays no further role in the biblical narrative. The name may mean <em>olive tree</em> or relate to the root for brightness. Bilhan's other sons included Jeush, Benjamin (a second Benjamin in the Benjamite line), Ehud, Chenaanah, and others.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zethan", "smith": "zethan", "isbe": "zethan"},
        "key_refs": ["1 Chronicles 7:10"]
    },
    "zia": {
        "id": "zia",
        "term": "Zia",
        "category": "people",
        "intro": "<p>Zia was a Gadite who dwelt in Bashan, listed in the tribal genealogy of Gad in 1 Chronicles 5:13. The Gadites in Bashan are described as mighty men of valor — men able in war and skilled with shield and sword — who occupied the region east of the Jordan from Bashan to Salecah. Zia appears only in this genealogical list among seven heads of the houses of their fathers' clans. The name may mean <em>sweat</em> or <em>trembling</em>. Nothing further is known of this individual beyond the brief genealogical mention.</p>",
        "sections": [],
        "hitchcock_meaning": "sweat; swelling",
        "source_ids": {"easton": "zia", "smith": "zia", "isbe": "zia"},
        "key_refs": ["1 Chronicles 5:13"]
    },
    "ziba": {
        "id": "ziba",
        "term": "Ziba",
        "category": "people",
        "intro": "<p>Ziba was a servant of the house of Saul who came to prominence when David sought to show kindness to any surviving member of Jonathan's family for Jonathan's sake (2 Samuel 9:1–13). Ziba informed David of Mephibosheth, Jonathan's lame son, who was then brought to Jerusalem and given all the land of Saul and a permanent place at the king's table. David appointed Ziba, with his fifteen sons and twenty servants, to farm the land for Mephibosheth.</p><p>During Absalom's rebellion, Ziba met the fleeing David with provisions and made the false claim that Mephibosheth had remained in Jerusalem hoping to recover his grandfather's kingdom (2 Samuel 16:1–4). David immediately granted all Mephibosheth's property to Ziba. When David returned victorious, Mephibosheth came with a counter-narrative, and David split the property between them (2 Samuel 19:24–30) — a judgment that left the truth of Ziba's accusation unresolved in the text.</p>",
        "sections": [],
        "hitchcock_meaning": "army; fight; strength",
        "source_ids": {"easton": "ziba", "smith": "ziba", "isbe": "ziba"},
        "key_refs": ["2 Samuel 9:2", "2 Samuel 16:4", "2 Samuel 19:29"]
    },
    "zibeon": {
        "id": "zibeon",
        "term": "Zibeon",
        "category": "people",
        "intro": "<p>Zibeon was a Horite clan chief of Seir in Edom (Genesis 36:20, 24, 29; 1 Chronicles 1:38, 40). His son Anah discovered the hot springs (or mules — the Hebrew <em>yemim</em> is textually debated) in the wilderness while keeping his father's donkeys (Genesis 36:24). Anah was also the father of Oholibamah, one of Esau's wives — making Zibeon a grandfather-in-law of Esau (Genesis 36:2). Zibeon is also listed as a son of Seir the Horite in Genesis 36:20, though Genesis 36:2 appears to give him as a Hivite — a textual difficulty that has generated significant scholarly discussion about the distinction between Horites and Hivites in the biblical text.</p>",
        "sections": [],
        "hitchcock_meaning": "iniquity that dwells",
        "source_ids": {"easton": "zibeon", "smith": "zibeon", "isbe": "zibeon"},
        "key_refs": ["Genesis 36:20", "Genesis 36:24", "1 Chronicles 1:38"]
    },
    "zibia": {
        "id": "zibia",
        "term": "Zibia",
        "category": "people",
        "intro": "<p>Zibia was a son of Shaharaim by his wife Hodesh, listed in the Benjamite genealogy of 1 Chronicles 8:9. Shaharaim had sent away two previous wives, Hushim and Baara, before fathering children with Hodesh in Moab. Zibia is listed among Shaharaim's sons in Moab, representing a branch of the tribe of Benjamin with Moabite connections. He appears only in this genealogical list and plays no further role in the biblical narrative. The name means <em>gazelle</em>. He should be distinguished from Zibiah the mother of King Joash, who begins Z2.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "zibia", "smith": "zibia", "isbe": "zibia"},
        "key_refs": ["1 Chronicles 8:9"]
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
    print(f'BP Z1: Zaanaim → Zibia: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__':
    main()
