"""
BP Article Synthesis — h1: Habakkuk → Harbona
Covers Easton entries: Habakkuk through Harbona (75 entries)

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

Script: scripts/bp-h1.py
Run: python3 scripts/bp-h1.py
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
    "habakkuk": {
        "id": "habakkuk",
        "term": "Habakkuk",
        "category": "people",
        "intro": "<p>Habakkuk (meaning <em>he that embraces</em> or <em>a wrestler</em>) was the eighth of the twelve minor prophets. Of his personal history little is reliably known; he was likely a member of the Levitical choir and a contemporary of Jeremiah and Zephaniah, placing his ministry around the late seventh century B.C., during the rise of the Babylonian empire under Nebuchadnezzar.</p><p>His prophecy is remarkable for its dialogic structure: Habakkuk dares to bring a complaint directly to God about the apparent triumph of wickedness in Judah, and then about God's choice of the violent Chaldeans as an instrument of judgment. The divine answer—<em>the just shall live by his faith</em> (Hab. 2:4)—became foundational to New Testament theology, quoted in Romans 1:17, Galatians 3:11, and Hebrews 10:38. The book closes with a magnificent psalm of theophany and trust.</p>",
        "hitchcock_meaning": "he that embraces; a wrestler",
        "source_ids": {"easton": "habakkuk", "isbe": "habakkuk"},
        "key_refs": ["Habakkuk 1:2", "Habakkuk 2:4", "Habakkuk 3:2", "Romans 1:17"]
    },
    "habakkuk-prophecies-of": {
        "id": "habakkuk-prophecies-of",
        "term": "Habakkuk, Prophecies of",
        "category": "concepts",
        "intro": "<p>The prophecies of Habakkuk constitute a brief but theologically rich book of three chapters, probably written around 650–605 B.C. The book opens with a sustained dialogue between the prophet and God: Habakkuk laments the unchecked violence and injustice within Judah; God responds that the Chaldeans will be raised up as an instrument of judgment; Habakkuk then protests that using a more wicked nation to punish Judah seems unjust; and God answers with the vision of the proud versus the righteous, culminating in the seminal declaration that <em>the just shall live by his faith</em> (Hab. 2:4).</p><p>Chapter 3 is a psalm of theophanic vision in which the prophet rehearses God's mighty acts in creation and the exodus as the ground of trust despite circumstances. The New Testament writers drew heavily on Habakkuk: Paul cites 2:4 twice as scriptural warrant for justification by faith (Romans 1:17; Galatians 3:12), and Hebrews 10:37–38 applies the text to the persevering faith of the early church awaiting Christ's return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "habakkuk-prophecies-of"},
        "key_refs": ["Romans 1:17", "Galatians 3:12", "Hebrews 10:37", "Hebrews 10:38"]
    },
    "habergeon": {
        "id": "habergeon",
        "term": "Habergeon",
        "category": "concepts",
        "intro": "<p>Habergeon is an Old English word denoting a short coat of mail or breastplate, used in older Bible translations for two distinct Hebrew terms. In Job 41:26 it renders a piece of armor that proves useless against the formidable hide of the Leviathan. In the Pentateuchal passages (Exodus 28:32; 39:23) it translates a term referring to the opening or collar of the high priest's robe, reinforced so that it would not tear—a garment feature ensuring the integrity of the sacred vestment during temple service.</p><p>The armor sense reflects the widespread use of scale or chain mail in the ancient Near East. Both Assyrian reliefs and Egyptian tomb paintings depict soldiers in short mail coats protecting the torso. The priestly application illustrates how the same term could span sacred and military contexts in the ancient world, with translators often choosing context-appropriate renderings.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "habergeon", "smith": "habergeon", "isbe": "habergeon"},
        "key_refs": ["Job 41:26", "Exodus 28:32", "Exodus 28:39"]
    },
    "habitation": {
        "id": "habitation",
        "term": "Habitation",
        "category": "concepts",
        "intro": "<p>Habitation in Scripture functions both as a literal term for dwelling places and as a rich theological metaphor. God himself is repeatedly described as the <em>habitation</em> of his people—the dwelling in whom they find security and rest (Ps. 71:3; 91:9). Conversely, God's own habitation is variously located in the highest heavens (Ps. 89:14), in Zion (Ps. 132:13), and, in the New Testament fulfillment, in the body of Christ and in the gathered community of believers (Eph. 2:22).</p><p>The theme of divine habitation runs through the entire canon: the tabernacle and temple were built as earthly dwelling places for God's name and glory, while the prophets foresaw a time when God would dwell among his people in a deeper sense. Ephesians 2:22 captures the New Testament development: Gentile and Jewish believers together are built into a holy temple, a habitation of God through the Spirit—the ultimate fulfillment of the dwelling-place motif.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "habitation", "isbe": "habitation"},
        "key_refs": ["Psalms 71:3", "Psalms 91:9", "Psalms 89:14", "Psalms 132:13", "Ephesians 2:22"]
    },
    "habor": {
        "id": "habor",
        "term": "Habor",
        "category": "places",
        "intro": "<p>Habor (meaning <em>a partaker</em> or <em>united stream</em>) was a river or district in the Assyrian empire to which captive Israelites from the northern kingdom were deported following the fall of Samaria in 722 B.C. (2 Kings 17:6; 18:11; 1 Chr. 5:26). It is generally identified with the Khabur River, a major tributary of the upper Euphrates in what is now northeastern Syria, flowing through a fertile region that became a site of Israelite exile settlements.</p><p>The Khabur valley was strategically important in Mesopotamian geography and appears in Assyrian royal annals as a region of population transfers. The biblical references indicate that Israelites from the tribes of Reuben, Gad, and half of Manasseh were settled there after the Assyrian campaigns, representing one of the earliest mass deportations of covenant people from their land—a pattern that would reach its culmination with Judah's Babylonian exile a century later.</p>",
        "hitchcock_meaning": "a partaker; a companion",
        "source_ids": {"easton": "habor", "smith": "habor", "isbe": "habor"},
        "key_refs": ["1 Chronicles 5:26", "2 Kings 17:6", "2 Kings 18:11"]
    },
    "hachilah": {
        "id": "hachilah",
        "term": "Hachilah",
        "category": "places",
        "intro": "<p>Hachilah (meaning <em>the darksome hill</em>) was one of the peaks of the long ridge running south of Hebron in the hill country of Judah. It appears in the narrative of David's flight from Saul: at Hachilah, David hid among the Ziphites who betrayed his location to the king, and Saul pursued him there with three thousand men (1 Sam. 23:19; 26:1–3). On a second visit, David secretly entered Saul's camp at night while the king slept and took his spear and water cruse—proof of his restraint in not harming the Lord's anointed.</p><p>The hill of Hachilah illustrates the terrain of southern Judah that made pursuit and concealment both possible: a broken landscape of ridges, ravines, and wilderness areas that provided natural refuge for outlaws and fugitives. Its exact modern identification is uncertain, though it lay in the wilderness of Ziph southeast of Hebron.</p>",
        "hitchcock_meaning": "my hope is in her",
        "source_ids": {"easton": "hachilah"},
        "key_refs": ["1 Samuel 23:19", "1 Samuel 26:1", "1 Samuel 26:13"]
    },
    "hadad": {
        "id": "hadad",
        "term": "Hadad",
        "category": "people",
        "intro": "<p>Hadad (meaning <em>joy</em>, <em>noise</em>, or <em>the thunderer</em>) was the name of several biblical figures and also the principal storm and weather deity of the Aramaean (Syrian) pantheon, corresponding to the Canaanite Baal and Babylonian Adad. As a divine name, Hadad appears embedded in compound names such as Hadadezer and Ben-hadad, reflecting the deity's prominence in Syro-Palestinian religion. In Zechariah 12:11, the mourning of Hadad-rimmon commemorates a lamentation rite associated with this deity.</p><p>As a personal name, Hadad is borne by several Edomite figures: an ancient Edomite king listed in the pre-monarchic king list of Genesis 36 (vv. 35–36, 39), and Hadad the Edomite, an adversary whom God raised up against Solomon after the death of Joab (1 Kings 11:14–22). The latter had fled as a child to Egypt during Joab's campaign against Edom and was given a wife from Pharaoh's household, returning to oppose Solomon's reign.</p>",
        "hitchcock_meaning": "joy; noise; clamor",
        "source_ids": {"easton": "hadad", "smith": "hadad", "isbe": "hadad"},
        "key_refs": ["Genesis 36:35", "1 Kings 11:14", "1 Chronicles 1:46", "1 Chronicles 1:50"]
    },
    "hadad-rimmon": {
        "id": "hadad-rimmon",
        "term": "Hadad-rimmon",
        "category": "places",
        "intro": "<p>Hadad-rimmon was a place in the valley of Megiddo associated with a notable lamentation remembered in Zechariah 12:11: <em>In that day shall there be a great mourning in Jerusalem, as the mourning of Hadad-rimmon in the valley of Megiddon.</em> The name compounds the names of two Syrian deities—Hadad, the storm god, and Rimmon, the thunder deity—suggesting the site held cultic significance connected to Aramaean religious practice that had penetrated into Israelite territory.</p><p>Most commentators identify the mourning of Hadad-rimmon with the national lamentation that arose at Megiddo following the death of King Josiah in battle against Pharaoh Necho (2 Chr. 35:22–25), though some view it as a reference to a seasonal mourning ritual for the dying-and-rising deity. Zechariah uses the image to describe the intense grief that will accompany Israel's future recognition of the one they have pierced—a passage cited in John 19:37.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hadad-rimmon"},
        "key_refs": ["Zechariah 12:11", "2 Chronicles 35:22"]
    },
    "hadadezer": {
        "id": "hadadezer",
        "term": "Hadadezer",
        "category": "people",
        "intro": "<p>Hadadezer (meaning <em>Hadad is help</em> or <em>beauty of assistance</em>), also called Hadarezer, was king of Zobah, an Aramaean state in the region north and northeast of Damascus. He was the most powerful Syrian ruler of his era and the dominant adversary David faced in his northern campaigns. David defeated Hadadezer twice: first when Hadadezer was attempting to extend his border to the Euphrates (2 Sam. 8:3–8), and again when Hadadezer gathered a large coalition to support the Ammonites against David (2 Sam. 10:15–19).</p><p>After the second defeat, the Aramaean vassals of Hadadezer made peace with Israel and became subject to David (2 Sam. 10:19). The spoil from these victories—shields of gold, and vast quantities of brass—was dedicated to the Lord and later used in Solomon's temple construction (1 Chr. 18:8). Hadadezer's defeats marked a critical expansion of Israelite power throughout greater Syria.</p>",
        "hitchcock_meaning": "beauty of assistance",
        "source_ids": {"easton": "hadadezer", "smith": "hadadezer", "isbe": "hadadezer"},
        "key_refs": ["2 Samuel 8:3", "2 Samuel 10:17", "1 Chronicles 18:8"]
    },
    "hadar": {
        "id": "hadar",
        "term": "Hadar",
        "category": "people",
        "intro": "<p>Hadar (meaning <em>power</em> or <em>greatness</em>) is the name of two Old Testament figures. The first was a son of Ishmael, Abraham's son by Hagar, listed among the twelve princes of Ishmael's line (Gen. 25:15; 1 Chr. 1:30). The second was an Edomite king, the son of Bedad, who reigned in Pau and whose wife was Mehetabel (Gen. 36:39; 1 Chr. 1:50–51). He appears in the pre-monarchic king list of Edom, a series of rulers who preceded the establishment of the Israelite monarchy.</p><p>The name also appears in a variant form as Hadad in some manuscript traditions of the Edomite king list (compare Gen. 36:39 with 1 Chr. 1:50), reflecting a common scribal interchange between the Hebrew letters <em>resh</em> and <em>daleth</em>. Both figures are obscure beyond their genealogical entries, but they illustrate the antiquity and reach of the Ishmaelite and Edomite tribal networks surrounding ancient Israel.</p>",
        "hitchcock_meaning": "power; greatness",
        "source_ids": {"easton": "hadar", "smith": "hadar", "isbe": "hadar"},
        "key_refs": ["Genesis 25:15", "Genesis 36:39", "1 Chronicles 1:30", "1 Chronicles 1:50"]
    },
    "hadarezer": {
        "id": "hadarezer",
        "term": "Hadarezer",
        "category": "people",
        "intro": "<p>Hadarezer (meaning <em>Adod is his help</em>) is the form of the name Hadadezer used in several passages (2 Sam. 8:3; 1 Chr. 18:3–10), reflecting a common variant spelling of the Aramaean king of Zobah. The interchange between <em>Hadad</em> and <em>Hadad</em> in the name reflects the close similarity between the Hebrew letters <em>resh</em> and <em>daleth</em> in ancient script, which frequently led to scribal confusion in transmission.</p><p>Hadarezer was defeated by David in his northern campaigns, and the account in 1 Chronicles 18 mirrors that of 2 Samuel 8: David struck down 22,000 Aramaeans, took the golden shields of Hadarezer's servants, captured Betah and Berothai, and received tribute from the subject kingdoms. Tou, king of Hamath—Hadarezer's adversary—sent his son Hadoram with gold, silver, and bronze to congratulate David on the victory (1 Chr. 18:10). See also <strong>Hadadezer</strong>.</p>",
        "hitchcock_meaning": "same as Hadadezer",
        "source_ids": {"easton": "hadarezer", "smith": "hadarezer", "isbe": "hadarezer"},
        "key_refs": ["2 Samuel 8:3", "1 Chronicles 18:3", "1 Chronicles 18:10"]
    },
    "hadashah": {
        "id": "hadashah",
        "term": "Hadashah",
        "category": "places",
        "intro": "<p>Hadashah (meaning <em>new</em>) was a city in the lowland district (Shephelah) of the tribal territory of Judah, listed among the towns in Joshua 15:37. It appears in a cluster of settlement names in the valley region between the hill country of Judah and the coastal plain, an area that was strategically contested between Israelite and Philistine influence during the pre-monarchic and early monarchic periods.</p><p>The site has not been positively identified with a modern location, though several candidates in the Shephelah have been proposed by scholars. The brevity of its biblical mention and the lack of narrative context associated with it suggest it was a small agricultural town rather than a significant administrative center. Its inclusion in the Judahite town list of Joshua 15 indicates it was a recognized settlement within the tribal allotment at the time of conquest and distribution.</p>",
        "hitchcock_meaning": "news; a month",
        "source_ids": {"easton": "hadashah", "smith": "hadashah", "isbe": "hadashah"},
        "key_refs": ["Joshua 15:37"]
    },
    "hadassah": {
        "id": "hadassah",
        "term": "Hadassah",
        "category": "people",
        "intro": "<p>Hadassah (meaning <em>a myrtle</em> or <em>joy</em>) was the Hebrew name of Esther, the Jewish heroine of the book bearing her Persian name. She was the daughter of Abihail, of the tribe of Benjamin, and had been raised by her cousin Mordecai after the death of her parents (Esth. 2:7, 15). She became queen of Persia when King Ahasuerus (Xerxes I) chose her to replace the deposed queen Vashti following a kingdom-wide search.</p><p>The use of her Hebrew name only at her first introduction (Esth. 2:7) and then exclusively by her Persian name Esther throughout the narrative may reflect her concealment of her Jewish identity at Mordecai's instruction—a detail central to the plot of the book, since her intervention to save the Jews from Haman's genocide depended on the element of surprise when she revealed her people's identity to the king. The name Hadassah connects her to the myrtle tree, a symbol of peace and joy in Hebrew tradition.</p>",
        "hitchcock_meaning": "a myrtle; joy",
        "source_ids": {"easton": "hadassah", "smith": "hadassah", "isbe": "hadassah"},
        "key_refs": ["Esther 2:7", "Esther 2:15"]
    },
    "hadattah": {
        "id": "hadattah",
        "term": "Hadattah",
        "category": "places",
        "intro": "<p>Hadattah (meaning <em>new</em>) was one of the towns in the extreme south of Judah, in the Negev district near the border with Edom (Josh. 15:25). Its name appears in conjunction with Hazor in the Judahite town list, and some interpreters read <em>Hazor-Hadattah</em> as a compound place-name meaning <em>New Hazor</em>, distinguishing it from other towns named Hazor in the region. The Negev settlement pattern reflected in Joshua 15 represents an arid but populated frontier zone that Israel inherited from prior Canaanite and Edomite occupation.</p><p>Like many of the obscure Negev sites in the Joshua town lists, Hadattah has not been definitively located archaeologically. The region was subject to shifting habitation patterns due to its dependence on seasonal rainfall and cistern water, and many settlements in the area appear and disappear from the biblical record across different periods of Israelite history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hadattah", "smith": "hadattah", "isbe": "hadattah"},
        "key_refs": ["Joshua 15:25"]
    },
    "hades": {
        "id": "hades",
        "term": "Hades",
        "category": "concepts",
        "intro": "<p>Hades (Greek, meaning <em>that which is out of sight</em> or <em>the unseen realm</em>) is the New Testament term used to translate the Hebrew <em>Sheol</em>—the place of the dead in the underworld. In the Greek Old Testament (Septuagint), Hades consistently renders Sheol, designating the shadowy abode where the dead were understood to exist in a diminished state beneath the earth. The English word <em>hell</em> in older translations often renders Hades, though modern versions typically transliterate it directly.</p><p>In the New Testament, Hades is contrasted with heaven: Christ descended to Hades (Acts 2:27, citing Ps. 16:10) and holds its keys (Rev. 1:18). Jesus' parable of the rich man and Lazarus (Luke 16:23) depicts Hades as a place of conscious existence divided by a great gulf between torment and comfort. At the final judgment, Death and Hades give up their dead and are themselves cast into the lake of fire (Rev. 20:13–14), indicating that Hades is a temporary state preceding the final resurrection and judgment rather than the eternal final state.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hades", "smith": "hades", "isbe": "hades"},
        "key_refs": ["Matthew 11:23", "Luke 16:23", "Acts 2:27", "Revelation 1:18"]
    },
    "hadid": {
        "id": "hadid",
        "term": "Hadid",
        "category": "places",
        "intro": "<p>Hadid (meaning <em>rejoicing</em> or <em>sharp</em>) was a town in the territory of Benjamin, situated in the Shephelah west of Jerusalem near the ancient road from Joppa to Jerusalem. It is identified with modern el-Haditheh, approximately three miles northeast of Lydda (Lod). The town appears in the lists of returning exiles who came back to Judah after the Babylonian captivity: 721 men of Lod, Hadid, and Ono returned with Zerubbabel (Ezra 2:33; Neh. 7:37).</p><p>Hadid's prominence in the post-exilic period suggests it was a settled and recognizable community in the Benjamin-Judah border zone. The grouping with Lod and Ono in both Ezra and Nehemiah indicates these three towns formed a recognized cluster in the coastal plain approaching Jerusalem, an area important for commerce and travel on the main western approach to the capital.</p>",
        "hitchcock_meaning": "rejoicing; sharp",
        "source_ids": {"easton": "hadid", "smith": "hadid", "isbe": "hadid"},
        "key_refs": ["Ezra 2:33", "Nehemiah 7:37"]
    },
    "hadlai": {
        "id": "hadlai",
        "term": "Hadlai",
        "category": "people",
        "intro": "<p>Hadlai (meaning <em>loitering</em> or <em>hindering</em>) was an Ephraimite, the father of Amasa, who is mentioned in a single passage recounting the aftermath of Pekah's raid on Judah. When the Israelite army under Pekah brought 200,000 Judahite captives to Samaria, a prophet named Oded met them and condemned the action. Amasa son of Hadlai was among the leading men of Ephraim who responded to the prophet's rebuke by refusing to allow the captives to be brought in and insisting they be clothed, fed, and returned to their kinsmen in Judah (2 Chr. 28:12).</p><p>This episode—a rare instance of northern Israelites acting with compassion toward Judahite prisoners—illustrates the continuing fraternal bond between the divided kingdoms even in a period of deep political hostility. Hadlai himself is mentioned only as the father of Amasa and has no independent narrative role beyond his patronymic.</p>",
        "hitchcock_meaning": "loitering; hindering",
        "source_ids": {"easton": "hadlai", "smith": "hadlai", "isbe": "hadlai"},
        "key_refs": ["2 Chronicles 28:12"]
    },
    "hadoram": {
        "id": "hadoram",
        "term": "Hadoram",
        "category": "people",
        "intro": "<p>Hadoram (meaning <em>their beauty</em> or <em>their power</em>) is the name of three distinct biblical figures. The first was a son of Joktan in the Table of Nations and an ancestor of an Arabian tribal people (Gen. 10:27; 1 Chr. 1:21). The second was the son of Tou (or Toi), king of Hamath, whom his father sent to David to congratulate him on his victory over Hadadezer of Zobah; he brought gold, silver, and bronze as gifts (2 Sam. 8:10; 1 Chr. 18:10, where his name appears as Joram). The third was the officer in charge of the forced labor under both David (2 Sam. 20:24, as Adoram) and Solomon and later Rehoboam; it was this Hadoram whom the northern tribes stoned to death when Rehoboam sent him to them following the revolt of the ten tribes (2 Chr. 10:18).</p><p>The stoning of Hadoram/Adoram marks the decisive rupture of the united monarchy: the act of violence against the labor overseer forced Rehoboam to flee to Jerusalem and confirmed the permanent division of the kingdom.</p>",
        "hitchcock_meaning": "their beauty; their power",
        "source_ids": {"easton": "hadoram", "smith": "hadoram", "isbe": "hadoram"},
        "key_refs": ["1 Chronicles 18:10", "2 Chronicles 10:18", "Genesis 10:27"]
    },
    "hadrach": {
        "id": "hadrach",
        "term": "Hadrach",
        "category": "places",
        "intro": "<p>Hadrach (meaning <em>point</em> or <em>joy of tenderness</em>) was a country or territory mentioned once in Scripture, in Zechariah 9:1: <em>The burden of the word of the LORD in the land of Hadrach, and Damascus shall be the rest thereof.</em> It appears alongside Damascus, Hamath, Tyre, Sidon, and several Philistine cities in an oracle of judgment against the nations surrounding Israel, likely dating to the late sixth or early fifth century B.C.</p><p>Hadrach has been identified with a region and city called <em>Hatarikka</em> in Assyrian annals, located in northern Syria between Hamath and the Orontes, mentioned in records of Assyrian campaigns in the eighth century B.C. Its inclusion in Zechariah's oracle alongside other well-known Syrian and Phoenician territories confirms it as a real geopolitical entity in the ancient Near East, even though it is unknown outside this single biblical reference and Assyrian sources.</p>",
        "hitchcock_meaning": "point; joy of tenderness",
        "source_ids": {"easton": "hadrach", "smith": "hadrach", "isbe": "hadrach"},
        "key_refs": ["Zechariah 9:1"]
    },
    "haemorrhoids": {
        "id": "haemorrhoids",
        "term": "Haemorrhoids",
        "category": "concepts",
        "intro": "<p>Haemorrhoids (also spelled <em>hemorrhoids</em>; rendered <em>emerods</em> in older translations) are mentioned in Scripture in connection with the plague God sent upon the Philistines when they captured the ark of the covenant and placed it in the temple of Dagon at Ashdod (1 Sam. 5:6, 9, 12; 6:4–5). The affliction spread from Ashdod to Gath and Ekron as the ark was moved from city to city, causing panic among the Philistine population. When the Philistines returned the ark to Israel, they sent five golden images of the tumors and five golden mice as a guilt offering.</p><p>The Hebrew term <em>ophalim</em> is generally understood to refer to swollen tumors or growths associated with the disease. Some scholars have proposed that the plague involved bubonic plague transmitted by rodents—explaining both the tumors (swollen lymph nodes or buboes) and the golden mice—while others maintain the traditional interpretation of hemorrhoidal disease. The episode served to demonstrate to both Philistines and Israelites that Yahweh's power accompanied the ark even in enemy territory.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "haemorrhoids"},
        "key_refs": ["1 Samuel 5:6", "1 Samuel 5:9", "1 Samuel 6:4"]
    },
    "haft": {
        "id": "haft",
        "term": "Haft",
        "category": "concepts",
        "intro": "<p>Haft is an archaic English term for the handle of a blade weapon, appearing once in the Authorized Version in the account of Ehud's assassination of the Moabite king Eglon: <em>and the haft also went in after the blade; and the fat closed upon the blade</em> (Judg. 3:22). The Hebrew word <em>nitstsab</em> refers to the hilt or handle of Ehud's double-edged short sword (or dagger), which sank so deeply into Eglon's obese body that even the handle disappeared into the flesh.</p><p>The grim detail serves a narrative purpose in the Ehud story, explaining why the attendants found the chamber doors locked and delayed their entry, allowing Ehud to escape. The passage is notable for its vivid, unsentimental description of the assassination—part of the Deuteronomistic history's frank portrayal of the often violent means by which God delivered Israel from oppression during the period of the judges.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "haft"},
        "key_refs": ["Judges 3:22"]
    },
    "hagar": {
        "id": "hagar",
        "term": "Hagar",
        "category": "people",
        "intro": "<p>Hagar (meaning <em>a stranger</em> or <em>one that fears</em>) was an Egyptian slave woman, the handmaid of Sarah, who became the mother of Ishmael by Abraham. When Sarah remained childless after many years, she gave Hagar to Abraham as a concubine according to the custom of the time. After Hagar conceived and began to despise her mistress, conflict arose; Hagar fled but was sent back by an angel with the promise that her son would be the father of a great nation (Gen. 16:1–14). The divine messenger named the child Ishmael (<em>God hears</em>) and promised that Ishmael would be a wild and contentious man.</p><p>After the birth of Isaac, Hagar and Ishmael were expelled from Abraham's household at Sarah's insistence (Gen. 21:9–21). In the wilderness of Beersheba, when their water was exhausted, God again appeared to Hagar, opened her eyes to a well, and renewed the promise concerning Ishmael's descendants. Paul later uses Hagar allegorically in Galatians 4:24–31 as a symbol of the covenant of law given at Sinai, contrasted with Sarah as a symbol of the covenant of promise.</p>",
        "hitchcock_meaning": "a stranger; one that fears",
        "source_ids": {"easton": "hagar", "smith": "hagar", "isbe": "hagar"},
        "key_refs": ["Genesis 16:1", "Genesis 21:9", "Genesis 21:14", "Galatians 4:24"]
    },
    "hagarene": {
        "id": "hagarene",
        "term": "Hagarene",
        "category": "people",
        "intro": "<p>Hagarene (also Hagarite) designates members of a tribal people descended from or associated with Hagar, dwelling east and southeast of Gilead in the Transjordanian region. The Hagarites appear in three biblical contexts. First, they are listed among the enemies of Israel in a prayer-psalm of Asaph (Ps. 83:6), grouped with Gebal, Ammon, Amalek, and other foes who conspired against Israel. Second, the Transjordanian tribes of Reuben, Gad, and half-Manasseh warred against the Hagarites and defeated them during the reign of Saul, taking their flocks and settling in their territory (1 Chr. 5:10–22).</p><p>Additionally, two individuals are designated Hagarene: Jaziz the Hagarite, who oversaw David's royal flocks (1 Chr. 27:31), and one of David's mighty men whose father was a Hagarite (1 Chr. 11:38). These individual examples show that Hagarites could serve in the Israelite royal administration, indicating a degree of integration alongside the tribal enmity reflected in the military accounts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hagarene"},
        "key_refs": ["1 Chronicles 5:10", "1 Chronicles 27:31", "Psalms 83:6"]
    },
    "haggai": {
        "id": "haggai",
        "term": "Haggai",
        "category": "people",
        "intro": "<p>Haggai (meaning <em>feast</em> or <em>festive</em>) was one of the twelve minor prophets and the first prophet to minister in Judah following the return from Babylonian exile. He was a contemporary of Zechariah and worked alongside him in the critical period of 520–516 B.C. during the rebuilding of the Jerusalem temple under the governor Zerubbabel and the high priest Joshua. The book of Ezra identifies Haggai and Zechariah as the prophets who stirred the returned community to resume the temple construction that had stalled for about sixteen years (Ezra 5:1; 6:14).</p><p>All of Haggai's four recorded messages are precisely dated to the second year of Darius I (520 B.C.). His preaching challenged the people's misplaced priorities—they had built their own houses while the Lord's house lay waste—and promised that the glory of the rebuilt temple would surpass that of Solomon's temple through the coming of the <em>desire of all nations</em> (Hag. 2:7). He also announced a divine shaking of the heavens, earth, and nations, interpreted by the New Testament writer of Hebrews as pointing to the unshakeable kingdom of Christ (Heb. 12:26–28).</p>",
        "hitchcock_meaning": "feast; solemnity",
        "source_ids": {"easton": "haggai", "smith": "haggai", "isbe": "haggai"},
        "key_refs": ["Ezra 5:1", "Ezra 6:14", "Haggai 2:7", "Hebrews 12:26"]
    },
    "haggai-book-of": {
        "id": "haggai-book-of",
        "term": "Haggai, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Haggai consists of two brief chapters containing four precisely dated prophetic oracles delivered in 520 B.C., the second year of Darius I of Persia. Each oracle is introduced with a specific day, month, and year, making Haggai the most precisely dated book in the entire Old Testament. The collection is short—only 38 verses—but historically significant: it preserves the prophetic voice that restarted the stalled temple reconstruction in Jerusalem after the return from Babylonian exile.</p><p>The first oracle rebukes the returned exiles for prioritizing their own houses while the temple lay unbuilt, warning that their agricultural failures are divine discipline for this neglect (1:1–11). The second oracle encourages the builders by promising that God's Spirit remains among them and that the latter glory of this house will exceed the former (2:1–9). The third and fourth oracles address the people's ritual uncleanness and promise a reversal of the agricultural curse (2:10–19), followed by a messianic promise to Zerubbabel as God's chosen signet-ring—a symbolic restoration of the Davidic line after the disgrace of Jeconiah (2:20–23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "haggai-book-of"},
        "key_refs": ["Haggai 1:1", "Haggai 2:7", "Haggai 2:22", "Hebrews 12:26"]
    },
    "haggith": {
        "id": "haggith",
        "term": "Haggith",
        "category": "people",
        "intro": "<p>Haggith (meaning <em>festive</em> or <em>the dancer</em>) was one of the wives of King David and the mother of Adonijah, David's fourth son (2 Sam. 3:4; 1 Chr. 3:2). Adonijah was born to David in Hebron during his early reign, before the capture of Jerusalem. His mother's name appears in the narrative primarily to identify his lineage in the succession crisis at the end of David's life.</p><p>When David was elderly and declining, Adonijah—who was handsome and had been little disciplined by his father—exalted himself and attempted to seize the throne before David's death, hosting a feast at En-rogel without inviting Solomon, Nathan the prophet, or the loyal military men (1 Kings 1:5–10). Bathsheba and Nathan intervened to ensure Solomon's anointing as king, and Adonijah's premature bid for power ultimately led to his execution when he requested Abishag the Shunammite as a wife—a request Solomon interpreted as a veiled claim to the throne (1 Kings 2:13–25).</p>",
        "hitchcock_meaning": "rejoicing",
        "source_ids": {"easton": "haggith", "smith": "haggith", "isbe": "haggith"},
        "key_refs": ["2 Samuel 3:4", "1 Kings 1:5", "1 Chronicles 3:2"]
    },
    "hagiographa": {
        "id": "hagiographa",
        "term": "Hagiographa",
        "category": "concepts",
        "intro": "<p>Hagiographa (Greek, meaning <em>holy writings</em>) is the term used for the third and final division of the Hebrew Bible, known in Hebrew as <em>Ketuvim</em> (Writings). The Hebrew canon is traditionally divided into Torah (Law), Nevi'im (Prophets), and Ketuvim (Writings), with the Hagiographa comprising the third section. It includes the Psalms, Proverbs, Job, the five Megilloth (Song of Songs, Ruth, Lamentations, Ecclesiastes, Esther), Daniel, Ezra-Nehemiah, and Chronicles.</p><p>Jesus appears to allude to this tripartite canonical structure in Luke 24:44 when he refers to <em>the law of Moses, and the prophets, and the psalms</em>—using Psalms to represent the Ketuvim, as the first and largest book of the Writings. The process by which these books were recognized as canonical was gradual, with debates in early Judaism continuing into the rabbinic period over the status of books such as Ecclesiastes and the Song of Solomon, though all were eventually accepted as scripture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hagiographa", "isbe": "hagiographa"},
        "key_refs": ["Luke 24:44"]
    },
    "hail": {
        "id": "hail",
        "term": "Hail",
        "category": "concepts",
        "intro": "<p>Hail (frozen rain-drops) appears in Scripture as both a natural phenomenon and an instrument of divine judgment. The most memorable biblical hailstorm was the seventh plague of Egypt (Ex. 9:22–26), in which devastating hail, mingled with fire, struck down people, livestock, and crops throughout Egypt while Goshen was supernaturally spared. Joshua's battle at Gibeon saw God send great stones of hail upon the fleeing Amorites, killing more than the Israelites had slain by sword (Josh. 10:11). Prophetic literature employs hail as a symbol of coming divine wrath (Isa. 28:2; Ezek. 13:11; Rev. 8:7; 16:21).</p><p>The greeting <em>Hail!</em> (from the Hebrew and Greek words for <em>peace</em> and <em>rejoice</em>) is the salutation used by the angel Gabriel to Mary at the Annunciation (Luke 1:28) and by the soldiers who mocked Jesus during his passion (Matt. 27:29), setting a striking contrast between genuine reverence and contemptuous irony in the Gospel narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hail"},
        "key_refs": ["Exodus 9:22", "Joshua 10:11", "Luke 1:28", "Matthew 27:29"]
    },
    "hair": {
        "id": "hair",
        "term": "Hair",
        "category": "concepts",
        "intro": "<p>Hair in the Bible carries a range of symbolic and social meanings that differed significantly from modern Western conventions. In ancient Israel and the broader Near East, men generally wore their hair and beards long, while the Egyptians were distinguished by shaving both head and beard (Gen. 41:14). The Nazirite vow prohibited cutting the hair as a sign of consecration to God (Num. 6:5); the long hair of Samson was the visible token of his Nazirite strength (Judg. 16:17). Shaving or tearing the hair was a sign of mourning and humiliation (Ezra 9:3; Jer. 7:29).</p><p>The New Testament addresses hair primarily in its teaching on propriety in worship (1 Cor. 11:14–15), where Paul argues from nature and custom that long hair is a woman's glory and functions as a natural covering. Women's elaborate hairstyles are cautioned against in 1 Timothy 2:9 and 1 Peter 3:3 as external adornments that can substitute for the inner beauty of godly character. Luke 7:38 records Mary's wiping of Jesus' feet with her hair as an act of extravagant devotion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hair", "smith": "hair", "isbe": "hair"},
        "key_refs": ["1 Corinthians 11:14", "1 Corinthians 11:15", "1 Timothy 2:9", "Luke 7:38"]
    },
    "hakkoz": {
        "id": "hakkoz",
        "term": "Hakkoz",
        "category": "people",
        "intro": "<p>Hakkoz (meaning <em>a thorn</em> or <em>summer; an end</em>) was the head of the seventh of the twenty-four courses of priests organized by David for service in the sanctuary (1 Chr. 24:10). His descendants returned from the Babylonian exile with Zerubbabel, but were excluded from the priesthood because they could not document their genealogy from the priestly registry (Ezra 2:61; Neh. 7:63–64).</p><p>The genealogical disqualification of the sons of Hakkoz illustrates the importance the post-exilic community placed on demonstrable priestly lineage as a condition of cultic service—a safeguard against unauthorized men assuming sacred roles. The situation was resolved for some descendants: Meremoth son of Urijah son of Hakkoz is mentioned as participating in the repair of the Jerusalem wall under Nehemiah (Neh. 3:4, 21), suggesting that the lineage question was eventually resolved for that branch of the family.</p>",
        "hitchcock_meaning": "a thorn; summer; an end",
        "source_ids": {"easton": "hakkoz", "smith": "hakkoz", "isbe": "hakkoz"},
        "key_refs": ["1 Chronicles 24:10", "Ezra 2:61", "Nehemiah 3:4"]
    },
    "halah": {
        "id": "halah",
        "term": "Halah",
        "category": "places",
        "intro": "<p>Halah was a district of the Assyrian empire to which the population of the northern kingdom of Israel was deported after the fall of Samaria in 722 B.C. under Shalmaneser V and Sargon II (2 Kings 17:6; 18:11; 1 Chr. 5:26). It is mentioned alongside the Habor River, the cities of the Medes, and Gozan as the destinations of the exiled Israelites—a deliberate Assyrian policy of population transfer designed to prevent conquered peoples from reconstituting national identity and resistance.</p><p>The precise location of Halah remains debated. Several scholarly proposals place it in the upper Tigris or Khabur River regions of Mesopotamia, where Assyrian administrative records mention settled deportee communities. The deportation to Halah, along with the other named regions, effectively ended the northern kingdom's political existence and permanently dispersed the majority of the ten northern tribes from their ancestral territory.</p>",
        "hitchcock_meaning": "a moist table",
        "source_ids": {"easton": "halah", "smith": "halah", "isbe": "halah"},
        "key_refs": ["2 Kings 17:6", "2 Kings 18:11", "1 Chronicles 5:26"]
    },
    "halak": {
        "id": "halak",
        "term": "Halak",
        "category": "places",
        "intro": "<p>Halak (meaning <em>smooth</em> or <em>bald</em>), referred to as the <em>Mount Halak</em> or <em>smooth mountain</em>, marked the southern limit of Joshua's military campaigns in Canaan: <em>Joshua smote all their kings from the mount Halak, that goeth up to Seir, even unto Baal-gad in the valley of Lebanon under mount Hermon</em> (Josh. 11:17; 12:7). It thus defined the extreme southern boundary of Joshua's conquests, corresponding to the northern boundary of Edom.</p><p>The mountain is generally identified with a prominent bare or white chalk ridge in the Negev region, possibly Jebel Halaq in the Negeb, rising near the road between Beersheba and Petra. Its description as going up <em>to Seir</em> (Edom) places it in the southern hill country approaching the Arabah and Edomite territory, consistent with its role as a natural geographic boundary marker for the extent of the Israelite conquest.</p>",
        "hitchcock_meaning": "part",
        "source_ids": {"easton": "halak", "smith": "halak"},
        "key_refs": ["Joshua 11:17", "Joshua 12:7"]
    },
    "halhul": {
        "id": "halhul",
        "term": "Halhul",
        "category": "places",
        "intro": "<p>Halhul (meaning <em>full of hollows</em> or <em>grief</em>) was a town in the highlands of Judah, listed in the Judahite town catalog of Joshua 15:58 alongside Beth-zur and Gedor. It is identified with the modern Arab village of Halhul, situated approximately four miles north of Hebron on the road to Jerusalem—one of the few biblical sites that has preserved its ancient name virtually unchanged into the modern period.</p><p>The site sits on a ridge at an elevation of about 1,000 meters above sea level, offering commanding views of the surrounding hill country. Archaeological surveys have found evidence of occupation from the Bronze Age through the Roman period, confirming its antiquity as a settled community. Halhul appears only in the Joshua town list and has no narrative events associated with it in the biblical text, but its location in the heart of the Judahite hill country gave it strategic significance on the main north-south mountain road through Judah.</p>",
        "hitchcock_meaning": "grief; looking for grief",
        "source_ids": {"easton": "halhul", "smith": "halhul", "isbe": "halhul"},
        "key_refs": ["Joshua 15:58"]
    },
    "hall": {
        "id": "hall",
        "term": "Hall",
        "category": "concepts",
        "intro": "<p>Hall in the biblical context refers to an open court or large covered vestibule rather than an interior corridor. The Greek word <em>aule</em> (Luke 22:55; rendered <em>palace</em> in some translations and <em>court</em> in the RV) denotes the open courtyard of a house or palace where people gathered—the outdoor space enclosed by the surrounding structure. It was in such a court that Peter warmed himself at a fire and denied Jesus three times during the trial before the high priest.</p><p>The <em>hall of judgment</em> (Gr. <em>praetorium</em>; Matt. 27:27; John 18:28) refers to the official headquarters of the Roman governor—in Jerusalem, either Herod's palace on the western hill or the Antonia Fortress adjacent to the temple. Jesus was led into this praetorium hall for interrogation by Pilate. In the Old Testament, temple halls (Heb. <em>ulam</em>) designate the portico or porch of the sanctuary, and Solomon's palace complex included a <em>hall of pillars</em> and a <em>hall of judgment</em> (1 Kings 7:6–7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hall", "smith": "hall", "isbe": "hall"},
        "key_refs": ["Luke 22:55", "Matthew 26:69", "John 18:28", "Matthew 27:27"]
    },
    "hallel": {
        "id": "hallel",
        "term": "Hallel",
        "category": "concepts",
        "intro": "<p>Hallel (Hebrew, meaning <em>praise</em>) is the name given to a group of six Psalms—113 through 118—used in Jewish liturgy as a unified act of praise. These psalms were sung during the major pilgrimage festivals (Passover, Weeks, Tabernacles, and Hanukkah) and at the Passover Seder. Psalms 113–114 were traditionally sung before the Passover meal, and 115–118 were sung after, corresponding to the <em>hymn</em> sung by Jesus and his disciples at the conclusion of the Last Supper (Matt. 26:30; Mark 14:26).</p><p>The Hallel group begins with the summons to praise (<em>Hallelujah</em>) and traces God's saving acts from the exodus (Ps. 114) to the universal sovereignty of the LORD (Ps. 117) and the declaration of his enduring steadfast love (Ps. 118). Psalm 118's cry of <em>Hosanna</em> and the statement <em>Blessed is he who comes in the name of the LORD</em> (v. 26) were quoted by the crowds at Jesus' triumphal entry into Jerusalem (Matt. 21:9), linking the Hallel to the passion narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hallel", "isbe": "hallel"},
        "key_refs": ["Psalms 113:1", "Psalms 118:26", "Matthew 26:30", "Mark 14:26"]
    },
    "hallelujah": {
        "id": "hallelujah",
        "term": "Hallelujah",
        "category": "concepts",
        "intro": "<p>Hallelujah (Hebrew, meaning <em>praise ye Jehovah</em>) is a compound imperative combining <em>hallelu</em> (<em>praise ye</em>) and <em>Jah</em> (the abbreviated form of the divine name Yahweh). It appears as an exclamation of praise in many of the Psalms (e.g., 106, 111–113, 117, 135, 146–150), typically opening or closing a psalm, and became a standard liturgical expression in both Jewish and Christian worship. The Septuagint transliterates it as <em>Allelouia</em>, the form that passed into Greek, Latin, and all Western Christian traditions.</p><p>In the New Testament, Hallelujah appears exclusively in Revelation 19:1–6, in a passage depicting the heavenly multitude's fourfold shout of praise celebrating God's judgment on Babylon and the coming of the marriage of the Lamb. The fourfold repetition—<em>Alleluia!</em> (vv. 1, 3, 4, 6)—echoes the Hallel psalms and creates the climactic doxological moment of the Apocalypse. The word has remained untranslated in Christian liturgy across all centuries and traditions, functioning as a universal cry of worship recognizable across linguistic boundaries.</p>",
        "hitchcock_meaning": "praise the Lord",
        "source_ids": {"easton": "hallelujah", "smith": "hallelujah", "isbe": "hallelujah"},
        "key_refs": ["Revelation 19:1", "Revelation 19:3", "Revelation 19:4", "Revelation 19:6"]
    },
    "hallow": {
        "id": "hallow",
        "term": "Hallow",
        "category": "concepts",
        "intro": "<p>Hallow means to render sacred, to consecrate, or to treat as holy. The term appears in the Old Testament in contexts of priestly consecration (Ex. 28:38; 29:1) and sabbath observance, and in the New Testament in the Lord's Prayer: <em>hallowed be thy name</em> (Matt. 6:9; Luke 11:2). To hallow something is to set it apart from ordinary use and designate it as belonging to or worthy of God.</p><p>The concept is closely related to the Hebrew <em>qadash</em> (to sanctify, make holy) and the Greek <em>hagiazo</em> (to sanctify, treat as holy). In the priestly legislation of Leviticus, numerous objects, persons, days, and places were hallowed through prescribed rituals of anointing, blood sprinkling, and dedication. The prayer that God's name be hallowed—the first petition of the Lord's Prayer—reflects the desire that God's character and reputation be honored, acknowledged, and glorified among all peoples, rather than blasphemed or treated as ordinary.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hallow"},
        "key_refs": ["Exodus 28:38", "Exodus 29:1", "Matthew 6:9"]
    },
    "halt": {
        "id": "halt",
        "term": "Halt",
        "category": "concepts",
        "intro": "<p>Halt in biblical usage means <em>lame</em> or <em>limping</em>, referring to a physical disability affecting gait. Jacob's limp after wrestling with the divine figure at Peniel (Gen. 32:31) became a permanent memorial of that encounter, and Israel's dietary prohibition against eating the sinew of the thigh (Gen. 32:32) was traced to this wound. The psalmist uses the image of halting to describe the condition of his own suffering and vulnerability (Ps. 38:17).</p><p>The phrase <em>to halt between two opinions</em> in 1 Kings 18:21 uses the same Hebrew root with the metaphorical sense of <em>limping</em> or <em>wavering</em>—Elijah challenges the people of Israel who are <em>limping</em> between Baal and Yahweh, undecided in their allegiance. Jesus' healing of the lame and halt (Matt. 15:30–31; Luke 14:21) was a fulfillment of messianic expectation derived from Isaiah 35:6 (<em>then shall the lame man leap as a hart</em>), demonstrating the kingdom's restorative power.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "halt", "isbe": "halt"},
        "key_refs": ["Genesis 32:31", "1 Kings 18:21", "Psalms 38:17"]
    },
    "ham": {
        "id": "ham",
        "term": "Ham",
        "category": "people",
        "intro": "<p>Ham (meaning <em>hot</em>, <em>heat</em>, or <em>brown</em>) was the second of Noah's three sons and, according to Genesis 10, the ancestor of the peoples of Africa and the ancient Near East: Egypt (<em>Mizraim</em>), Canaan, Cush (Ethiopia), and Phut (Libya) are listed among his descendants (Gen. 10:6). The name Ham is also used in the Psalms as a poetic name for Egypt: <em>the land of Ham</em> (Ps. 105:23, 27; 106:22), reflecting the ancient connection between the name and Egyptian civilization.</p><p>Ham's moral failure occurs in Genesis 9:22–24 when he <em>saw the nakedness of his father</em> while Noah lay drunk in his tent and told his brothers rather than covering Noah discreetly. The precise nature of his offense has been debated, but the canonical narrative treats it as a serious violation of honor and shame conventions, resulting in Noah's curse upon Ham's son Canaan—a curse invoked throughout Israel's later interactions with Canaanite peoples. Ham himself is not cursed, only his son, a distinction that has theological and historical significance.</p>",
        "hitchcock_meaning": "hot; heat; brown",
        "source_ids": {"easton": "ham", "smith": "ham"},
        "key_refs": ["Genesis 5:32", "Genesis 9:22", "Genesis 10:6", "Psalms 105:23"]
    },
    "haman": {
        "id": "haman",
        "term": "Haman",
        "category": "people",
        "intro": "<p>Haman (meaning <em>noise</em> or <em>tumult</em>; of Persian origin), son of Hammedatha the Agagite, was the grand vizier of the Persian king Ahasuerus (Xerxes I) and the principal antagonist of the book of Esther. Elevated above all other nobles, Haman demanded prostration from the royal servants, and when Mordecai the Jew refused on religious grounds, Haman determined not merely to destroy Mordecai but to annihilate every Jew in the Persian empire. He persuaded the king to issue a decree authorizing the genocide, casting lots (<em>pur</em>) to determine the optimal date for the massacre—the origin of the festival of Purim.</p><p>Haman's downfall came through a series of dramatic reversals: the king's sleepless night led him to honor Mordecai for an old service just as Haman arrived to request Mordecai's execution; Esther's two banquets revealed both her petition and Haman's identity as the threat; and Haman was hanged on the very gallows he had prepared for Mordecai (Esth. 7:10). The narrative is often read as a paradigmatic story of divine providence overturning the schemes of the wicked.</p>",
        "hitchcock_meaning": "noise; tumult",
        "source_ids": {"easton": "haman", "smith": "haman", "isbe": "haman"},
        "key_refs": ["Esther 3:1", "Esther 3:5", "Esther 7:9", "Esther 7:10"]
    },
    "hamath": {
        "id": "hamath",
        "term": "Hamath",
        "category": "places",
        "intro": "<p>Hamath (meaning <em>fortress</em> or <em>citadel</em>) was the capital of an important Aramaean kingdom in the upper Orontes valley of what is now central Syria, situated approximately 200 kilometers north of Damascus. It appears in the Bible as the ideal northern boundary of the promised land: <em>from the wilderness of Zin unto where one entereth Hamath</em> and the <em>entrance of Hamath</em> define Israel's northern limit in the promises of Numbers 34:8, Joshua 13:5, and the ideal extent of the Davidic-Solomonic empire (1 Kings 8:65).</p><p>Hamath had a complex relationship with Israel: its king Tou sent his son with tribute after David's defeat of Hadadezer of Zobah, acknowledging Israelite supremacy (2 Sam. 8:9–10). Solomon built store cities in Hamath-zobah (2 Chr. 8:3–4). The Assyrian deportation of Israel's population to Hamath (2 Kings 17:24) and the city's fall to Assyria (Isa. 10:9; Jer. 49:23; Amos 6:2) signal the expansion of Mesopotamian power that engulfed both Syria and Israel. Modern Hama preserves the ancient name.</p>",
        "hitchcock_meaning": "anger; heat; a wall",
        "source_ids": {"easton": "hamath", "smith": "hamath", "isbe": "hamath"},
        "key_refs": ["Numbers 13:21", "Numbers 34:8", "2 Samuel 8:9", "Amos 6:2"]
    },
    "hamath-zobah": {
        "id": "hamath-zobah",
        "term": "Hamath-zobah",
        "category": "places",
        "intro": "<p>Hamath-zobah (meaning <em>the fortress of Zobah</em> or <em>heat of an army</em>) appears in a single verse recording Solomon's military campaign: <em>he went to Hamath-zobah, and prevailed against it</em> (2 Chr. 8:3). The designation combines the names of two Aramaean territories—Hamath on the upper Orontes and Zobah, the kingdom that David had defeated—suggesting the region had been reconstituted or still bore the name of the earlier Aramean power.</p><p>Solomon's subjugation of Hamath-zobah marked the practical realization of the northern boundaries promised to Israel, allowing him to build Tadmor in the wilderness and other store cities in the region (2 Chr. 8:4). Some scholars identify this campaign with an attempt to secure the northern trade routes, since Hamath sat astride the main corridor between Mesopotamia and the Levantine coast. The passage demonstrates that Solomon's reign, like David's, involved active military control of northern Syria rather than merely diplomatic relations.</p>",
        "hitchcock_meaning": "the heat, or the wall, of an army",
        "source_ids": {"easton": "hamath-zobah", "isbe": "hamath-zobah"},
        "key_refs": ["2 Chronicles 8:3"]
    },
    "hammath": {
        "id": "hammath",
        "term": "Hammath",
        "category": "places",
        "intro": "<p>Hammath (meaning <em>warm springs</em>) was one of the fortified cities in the tribal territory of Naphtali, listed in Joshua 19:35 among the fenced cities assigned to that tribe after the conquest. It is generally identified with the site of hot springs on the western shore of the Sea of Galilee, just south of Tiberias—the same springs known in the New Testament period as Emmaus or Hammath, and today as Hamat Tverya, where hot sulfur springs have been famous since antiquity.</p><p>The city may be identical with or closely related to Hammon (1 Chr. 6:76) and Hammoth-dor (Josh. 21:32), which were Levitical cities also in Naphtali associated with warm springs. If so, it represents the same geographical location appearing under slightly variant names across different source documents. The site's hot springs made it a natural gathering point throughout the ancient and classical periods and are still a tourist attraction today.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hammath", "smith": "hammath", "isbe": "hammath"},
        "key_refs": ["Joshua 19:35"]
    },
    "hammedatha": {
        "id": "hammedatha",
        "term": "Hammedatha",
        "category": "people",
        "intro": "<p>Hammedatha (meaning <em>he that troubles the law</em>) was the father of Haman, the villain of the book of Esther. He is designated <em>the Agagite</em> (Esth. 3:1; 8:5; 9:24), a designation linking Haman's lineage to Agag, king of the Amalekites whom Saul failed to execute as commanded by Samuel (1 Sam. 15:8–9). This genealogical connection sets up the Esther narrative as a continuation of the long enmity between Israel and Amalek: Haman the Agagite's attempt to destroy the Jews echoes the Amalekite pattern of opposition to God's people, while Mordecai the Benjaminite's role parallels Saul's failed duty.</p><p>Hammedatha himself has no independent narrative role in the text and is known only as Haman's father. His name appears repeatedly in the formulaic designation <em>Haman the son of Hammedatha the Agagite</em>, which emphasizes Haman's ethnic and genealogical identity as the source of his hostility to Mordecai and the Jewish people.</p>",
        "hitchcock_meaning": "he that troubles the law",
        "source_ids": {"easton": "hammedatha", "smith": "hammedatha", "isbe": "hammedatha"},
        "key_refs": ["Esther 3:1", "Esther 8:5", "Esther 9:24"]
    },
    "hammelech": {
        "id": "hammelech",
        "term": "Hammelech",
        "category": "people",
        "intro": "<p>Hammelech (meaning <em>the king</em> or <em>a counselor</em>) appears in two passages in Jeremiah (36:26; 38:6) as a personal name or title. Jerahmeel the son of Hammelech was one of three men sent by King Jehoiakim to arrest Jeremiah and Baruch after the scroll of Jeremiah's prophecies was read to the king (Jer. 36:26). Malchiah the son of Hammelech owned the dungeon pit into which the officials cast Jeremiah during the siege of Jerusalem (Jer. 38:6).</p><p>The phrase <em>son of Hammelech</em> literally means <em>son of the king</em> in Hebrew (<em>ben-hammelek</em>), and many scholars interpret this not as a proper name but as a title designating royal princes or members of the royal family. If so, Jerahmeel and Malchiah were both members of the Davidic royal household acting in official capacities during the final years of the kingdom of Judah before the Babylonian conquest.</p>",
        "hitchcock_meaning": "a king; a counselor",
        "source_ids": {"easton": "hammelech", "smith": "hammelech", "isbe": "hammelech"},
        "key_refs": ["Jeremiah 36:26", "Jeremiah 38:6"]
    },
    "hammer": {
        "id": "hammer",
        "term": "Hammer",
        "category": "concepts",
        "intro": "<p>Hammer in Scripture refers to several distinct tools and carries significant figurative weight. The Hebrew <em>pattish</em> was used by gold-beaters and smiths (Isa. 41:7; 44:12), while <em>maqabah</em> denotes a stone-working mallet (Isa. 44:12). The wooden mallet (<em>halamuth</em>) used by Jael to drive a tent peg through Sisera's skull (Judg. 4:21; 5:26) appears in one of the most dramatic passages of the book of Judges. The absence of the sound of hammers during the temple construction reflects a reverent silence in which all stones were pre-cut off-site (1 Kings 6:7).</p><p>Figuratively, the hammer is a powerful image in the prophets. Jeremiah uses it twice: once to describe God's word as a hammer that breaks the rock in pieces (Jer. 23:29), and once to designate Babylon as God's war hammer by which he shattered nations—before itself being destroyed (Jer. 51:20–23). The prophetic use of the hammer image captures both the irresistible force of divine judgment and the equally irresistible penetrating power of the word of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hammer", "isbe": "hammer"},
        "key_refs": ["Judges 4:21", "Jeremiah 23:29", "Jeremiah 50:23", "Isaiah 44:12"]
    },
    "hammoleketh": {
        "id": "hammoleketh",
        "term": "Hammoleketh",
        "category": "people",
        "intro": "<p>Hammoleketh (meaning <em>the queen</em>) was the daughter of Machir, the son of Manasseh, and thus a granddaughter of Joseph's son Manasseh. She is mentioned in the genealogy of 1 Chronicles 7:17–18 as the sister of Gilead, and the text records that she bore three sons: Ishhod, Abiezer, and Mahlah. The name <em>hammoleketh</em> (literally <em>the queen</em> in Hebrew, with the definite article) suggests she held a position of significance or authority within the Manassite clan, though the nature of that status is not elaborated.</p><p>Her descendant Abiezer gave his name to the Abiezrite clan of Manasseh, making her an important matriarchal figure in the tribal genealogy. The judge Gideon was an Abiezrite (Judg. 6:11, 34), meaning Hammoleketh is an ancestress of Gideon—one of the most prominent figures in the book of Judges.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hammoleketh", "smith": "hammoleketh"},
        "key_refs": ["1 Chronicles 7:17", "1 Chronicles 7:18"]
    },
    "hammon": {
        "id": "hammon",
        "term": "Hammon",
        "category": "places",
        "intro": "<p>Hammon (meaning <em>warm springs</em> or <em>the sun</em>) is the name of two places in the Old Testament. The first was a town in the tribal territory of Asher (Josh. 19:28), situated near the Phoenician coast in the region that would later include Tyre and Sidon. Its exact identification is uncertain, though some scholars propose a site near modern Umm el-Awamid south of Tyre.</p><p>The second Hammon was a Levitical city in the territory of Naphtali (1 Chr. 6:76), likely the same site as Hammath (Josh. 19:35) and Hammoth-dor (Josh. 21:32), all of which are associated with warm springs near the Sea of Galilee. The slight variations in the name across different passages likely reflect scribal variants of the same geographical designation referring to the well-known hot springs on the western shore of the Sea of Galilee south of Tiberias.</p>",
        "hitchcock_meaning": "heat; the sun",
        "source_ids": {"easton": "hammon", "smith": "hammon", "isbe": "hammon"},
        "key_refs": ["Joshua 19:28", "1 Chronicles 6:76"]
    },
    "hammoth-dor": {
        "id": "hammoth-dor",
        "term": "Hammoth-dor",
        "category": "places",
        "intro": "<p>Hammoth-dor (meaning <em>warm springs of Dor</em>) was a Levitical city in the tribal territory of Naphtali, assigned to the Gershonite families of the Levites in Joshua 21:32. It is almost certainly the same location as Hammath (Josh. 19:35) and Hammon (1 Chr. 6:76), reflecting slight textual variations for the same site—the warm springs on the western shore of the Sea of Galilee near what became the city of Tiberias.</p><p>The designation as a city of refuge and Levitical city indicates its administrative and religious importance in northern Israel. The hot springs at this location were famous throughout the ancient and classical periods; later known as Emmaus-Nicopolis by Greek and Roman writers, the site became a spa resort in the Herodian era. The hot spring complex at modern Hamat Tverya (Hammat Tiberias) preserves the ancient name and continues to be used, with a significant ancient mosaic synagogue floor discovered there by excavators.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hammoth-dor", "isbe": "hammoth-dor"},
        "key_refs": ["Joshua 21:32"]
    },
    "hamon": {
        "id": "hamon",
        "term": "Hamon",
        "category": "places",
        "intro": "<p>Hamon appears in Easton's dictionary as a cross-reference directing the reader to Baal-hamon, a place name appearing once in the Song of Solomon (8:11): <em>Solomon had a vineyard at Baal-hamon; he let out the vineyard unto keepers.</em> The name means <em>lord of the multitude</em> or <em>possessor of a crowd</em>, and the location of Baal-hamon has not been identified with certainty, though some interpreters place it in the hill country of Judah or Samaria.</p><p>In the Song of Solomon, the reference to Solomon's Baal-hamon vineyard appears in a context where the beloved contrasts her own vineyard—her own self—with Solomon's wealth (8:11–12), using the vineyard image to assert her autonomy and the uniqueness of her relationship with her beloved. The mention of Baal-hamon thus functions primarily as a literary foil rather than a geographically significant location.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hamon"},
        "key_refs": ["Song of Solomon 8:11"]
    },
    "hamon-gog": {
        "id": "hamon-gog",
        "term": "Hamon-gog",
        "category": "places",
        "intro": "<p>Hamon-gog (meaning <em>the multitude of Gog</em>) is the name given in Ezekiel's prophetic vision to the valley where the vast army of Gog would be buried after their catastrophic defeat at the hands of God's judgment upon the mountains of Israel (Ezek. 39:11, 15). The burying of the horde would take seven months and require a dedicated team of grave-diggers; travelers passing through the valley were instructed to mark any discovered bones for collection so the land would be cleansed of the defilement of the unburied dead.</p><p>The valley is also called the valley of the travelers, and it is described as blocking the way east of the sea—possibly a reference to the Dead Sea region. Hamon-gog functions in Ezekiel 38–39 as a powerful symbol of the completeness of God's victory over the enemies of his people in the eschatological age, with the scale of the burial emphasizing the magnitude of the force that God overthrows. The feast for birds and beasts following the slaughter (Ezek. 39:17–20) is echoed in Revelation 19:17–21.</p>",
        "hitchcock_meaning": "the multitude of Gog",
        "source_ids": {"easton": "hamon-gog", "isbe": "hamon-gog"},
        "key_refs": ["Ezekiel 39:11", "Ezekiel 39:15"]
    },
    "hamonah": {
        "id": "hamonah",
        "term": "Hamonah",
        "category": "places",
        "intro": "<p>Hamonah (meaning <em>his multitude</em> or <em>his uproar</em>) is the name figuratively given in Ezekiel's prophecy to the town near the valley of Hamon-gog where Gog's vast defeated army would be buried: <em>And also the name of the city shall be Hamonah</em> (Ezek. 39:16). The name derives from the same root as Hamon-gog and emphasizes the theme of the multitude of enemies that God will overwhelm in the eschatological battle.</p><p>Hamonah is a prophetic or visionary place name rather than an identifiable historical city; its significance is symbolic, signifying the permanent memorial that would mark the place of Gog's destruction. Like many place names in Ezekiel's vision of the restored land and the defeat of Gog (Ezek. 38–39), it belongs to the literature of apocalyptic geography—locations that carry theological meaning in a future scenario rather than references to existing cities in the prophet's own time.</p>",
        "hitchcock_meaning": "his multitude; his uproar",
        "source_ids": {"easton": "hamonah", "smith": "hamonah", "isbe": "hamonah"},
        "key_refs": ["Ezekiel 39:16"]
    },
    "hamor": {
        "id": "hamor",
        "term": "Hamor",
        "category": "people",
        "intro": "<p>Hamor (meaning <em>an ass</em> or <em>clay</em>) was a Hivite prince, the father of Shechem, from whom Jacob purchased a plot of ground at the city of Shechem for one hundred pieces of silver (Gen. 33:18–20; Acts 7:16). This plot became the burial site of Joseph's bones after the Exodus (Josh. 24:32). Hamor's son Shechem violated Jacob's daughter Dinah, then sought to marry her, leading to the negotiation in which Hamor proposed intermarriage between the Hivites and Israelites—a proposal Jacob's sons accepted deceitfully and then avenged by slaughtering the men of Shechem while they were recovering from circumcision (Gen. 34).</p><p>Hamor represents the Canaanite inhabitants of the central highlands with whom Israel's patriarchal ancestors had complex and often violent interactions. The land purchase at Shechem—parallel to Abraham's purchase of Machpelah—established an Israelite legal claim to a parcel in the heart of Canaan long before the conquest under Joshua.</p>",
        "hitchcock_meaning": "an ass; clay; dirt",
        "source_ids": {"easton": "hamor", "smith": "hamor", "isbe": "hamor"},
        "key_refs": ["Genesis 33:19", "Genesis 34:2", "Acts 7:16", "Joshua 24:32"]
    },
    "hamul": {
        "id": "hamul",
        "term": "Hamul",
        "category": "people",
        "intro": "<p>Hamul (meaning <em>godly</em> or <em>merciful</em>, also interpreted as <em>spared</em>) was the younger of the two sons of Pharez (Perez), son of Judah and Tamar (Gen. 46:12; 1 Chr. 2:5). He accompanied Jacob's family to Egypt during the famine and became the ancestor of the Hamulite clan within the tribe of Judah (Num. 26:21). His brother was Hezron, whose genealogy becomes more prominent in the messianic line of David (1 Chr. 2:9–15; Ruth 4:18–22; Matt. 1:3).</p><p>Hamul's significance is primarily genealogical: as a son of Perez and a grandson of Judah, he belongs to the line that Genesis 49:10 identifies as the bearer of the royal scepter of Israel. His descendants formed one of the recognized clans of the tribe at the time of the second census in Numbers 26, confirming the continuity of his line through the wilderness period.</p>",
        "hitchcock_meaning": "godly; merciful",
        "source_ids": {"easton": "hamul", "smith": "hamul", "isbe": "hamul"},
        "key_refs": ["Genesis 46:12", "Numbers 26:21", "1 Chronicles 2:5"]
    },
    "hamutal": {
        "id": "hamutal",
        "term": "Hamutal",
        "category": "people",
        "intro": "<p>Hamutal (meaning <em>the shadow of his heat</em> or <em>kinsman of the dew</em>) was the daughter of Jeremiah of Libnah and one of the wives of King Josiah. She was the mother of two kings of Judah: Jehoahaz (also called Shallum), who reigned for three months after Josiah's death before being deposed by Pharaoh Necho (2 Kings 23:31), and Zedekiah (also called Mattaniah), the last king of Judah, who reigned eleven years before the Babylonian destruction of Jerusalem (2 Kings 24:18).</p><p>Hamutal's two sons thus bookended the tragic final decades of the Judahite monarchy. She is mentioned only to identify the mothers of the kings, following the Deuteronomistic historian's standard pattern of recording the queen mother's name and hometown. The fact that both of her sons reigned during the period of national crisis—Assyrian domination followed by Babylonian conquest—gives her maternal role a poignant dimension in the narrative of Judah's fall.</p>",
        "hitchcock_meaning": "the shadow of his heat",
        "source_ids": {"easton": "hamutal", "smith": "hamutal", "isbe": "hamutal"},
        "key_refs": ["2 Kings 23:31", "2 Kings 24:18"]
    },
    "hanameel": {
        "id": "hanameel",
        "term": "Hanameel",
        "category": "people",
        "intro": "<p>Hanameel (meaning <em>the grace that comes from God</em> or <em>gift of God</em>) was the cousin of the prophet Jeremiah, the son of Jeremiah's uncle Shallum. During the final siege of Jerusalem by the Babylonians, while Jeremiah was confined in the court of the guard, Hanameel came to him and asked him to exercise the kinsman-redeemer's right by purchasing a field at Anathoth in Benjamin—the ancestral property that Hanameel wished to sell (Jer. 32:6–15).</p><p>Jeremiah's purchase of the field—weighing out seventeen shekels of silver, signing the deed, sealing it, and depositing it with Baruch in an earthen vessel for long-term preservation—was a deliberate prophetic sign-act performed at God's command. At the very moment when Jerusalem was falling and the land seemed lost, Jeremiah bought land as a public testimony that <em>houses and fields and vineyards shall again be bought in this land</em> (Jer. 32:15), affirming faith in the future restoration despite the present disaster.</p>",
        "hitchcock_meaning": "the grace that comes from God; gift of God",
        "source_ids": {"easton": "hanameel", "smith": "hanameel"},
        "key_refs": ["Jeremiah 32:6", "Jeremiah 32:9", "Jeremiah 32:15"]
    },
    "hanan": {
        "id": "hanan",
        "term": "Hanan",
        "category": "people",
        "intro": "<p>Hanan (meaning <em>full of grace</em> or <em>merciful</em>) is the name of several individuals in the Old Testament. The most significant include: a Benjaminite listed in the genealogy of 1 Chronicles 8:23; one of David's thirty mighty warriors, the son of Maacah (1 Chr. 11:43); and Hanan the son of Igdaliah, a prophet whose sons maintained a chamber in the temple where Jeremiah brought the Rechabites to test their commitment to their ancestral vow of abstinence (Jer. 35:4). In the post-exilic period, several men named Hanan appear: as a Levite who helped Ezra explain the law (Neh. 8:7), as a temple servant whose descendants returned from exile (Ezra 2:46; Neh. 7:49), and as a signatory to Nehemiah's covenant renewal (Neh. 10:22, 26).</p><p>The frequency of the name reflects the popularity of names built on the Hebrew root <em>hnn</em> (grace, favor) in ancient Israel, a root that also underlies names like Hannah, Hananiah, Hanani, and the Greek form John (Johanan = Yahweh is gracious).</p>",
        "hitchcock_meaning": "full of grace",
        "source_ids": {"easton": "hanan", "smith": "hanan", "isbe": "hanan"},
        "key_refs": ["1 Chronicles 11:43", "Jeremiah 35:4", "Nehemiah 8:7"]
    },
    "hananeel": {
        "id": "hananeel",
        "term": "Hananeel",
        "category": "places",
        "intro": "<p>Hananeel (meaning <em>grace</em> or <em>gift of God</em>) was a tower in the northern section of the walls of Jerusalem, mentioned in Nehemiah's account of the wall-building (Neh. 3:1; 12:39) and in two prophetic passages. Jeremiah 31:38 includes the tower of Hananeel in his description of the future restored Jerusalem—a city whose boundaries from the tower of Hananeel to the Corner Gate would be rebuilt to the LORD, holy and never again uprooted. Zechariah 14:10 similarly uses the tower of Hananeel to describe the geographical extent of the elevated Jerusalem in the messianic age.</p><p>The tower stood near the Sheep Gate at the northeast corner of the city and is thought to be identical with or closely associated with the tower of Meah (Neh. 3:1; 12:39). Its position on the vulnerable northern approach to the city—where Jerusalem's natural topographical defenses were weakest—made it a critical fortification element. The tower's inclusion in the prophetic visions of Jerusalem's restoration underlines the physical concreteness of those hopes.</p>",
        "hitchcock_meaning": "grace, or gift, of God",
        "source_ids": {"easton": "hananeel", "smith": "hananeel"},
        "key_refs": ["Nehemiah 3:1", "Jeremiah 31:38", "Zechariah 14:10"]
    },
    "hanani": {
        "id": "hanani",
        "term": "Hanani",
        "category": "people",
        "intro": "<p>Hanani (meaning <em>my grace</em> or <em>my mercy</em>) is the name of several individuals in the Old Testament. The most notable is Hanani the seer (or prophet), the father of the prophet Jehu son of Hanani (1 Kings 16:7; 2 Chr. 19:2). This Hanani rebuked King Asa of Judah for relying on the king of Syria rather than on God in his conflict with Israel, and was imprisoned by the king for this prophetic rebuke—an early example of a prophet suffering for his message (2 Chr. 16:7–10).</p><p>A second Hanani was Nehemiah's brother, who came from Jerusalem to Susa with news of the broken walls of Jerusalem, triggering Nehemiah's grief, prayer, and eventual mission to rebuild them (Neh. 1:2). He later served as a ruler of Jerusalem in the post-exilic community (Neh. 7:2). Among the musicians, Hanani son of Heman was one of David's appointed Levitical singers (1 Chr. 25:4, 25). Several others bearing the name appear in post-exilic lists and in the priestly families of the period of Nehemiah (Neh. 12:36).</p>",
        "hitchcock_meaning": "my grace; my mercy",
        "source_ids": {"easton": "hanani", "smith": "hanani", "isbe": "hanani"},
        "key_refs": ["2 Chronicles 16:7", "Nehemiah 1:2", "Nehemiah 7:2"]
    },
    "hananiah": {
        "id": "hananiah",
        "term": "Hananiah",
        "category": "people",
        "intro": "<p>Hananiah (meaning <em>Jehovah has given</em> or <em>grace of the Lord</em>) is one of the most frequently occurring names in the Old Testament, borne by at least fourteen individuals. The most prominent include: Hananiah the Hebrew name of Shadrach, one of Daniel's three companions who refused to bow to Nebuchadnezzar's golden image and was cast into the fiery furnace (Dan. 1:6–7; 3:12–30); Hananiah the false prophet of Gibeon who broke Jeremiah's wooden yoke and predicted the return of Babylonian exiles within two years, for which lie Jeremiah prophesied his death within the year—and he died that same year (Jer. 28:1–17); and Hananiah the son of Zerubbabel, who appears in the post-exilic genealogy (1 Chr. 3:19).</p><p>The widespread use of the name reflects the theological importance of the divine name Yahweh (<em>Jah</em>) in Israelite personal naming patterns, where names expressing God's graciousness and gifts were among the most popular categories throughout the biblical period.</p>",
        "hitchcock_meaning": "grace; mercy; gift of the Lord",
        "source_ids": {"easton": "hananiah", "smith": "hananiah", "isbe": "hananiah"},
        "key_refs": ["Daniel 1:6", "Jeremiah 28:1", "Jeremiah 28:17", "1 Chronicles 3:19"]
    },
    "hand": {
        "id": "hand",
        "term": "Hand",
        "category": "concepts",
        "intro": "<p>The hand in Scripture carries extensive literal and figurative significance. Literally, it denotes the human hand as an instrument of labor, power, and touch—Galen called it <em>the instrument of instruments</em>, and the Bible reflects this universal human experience. The laying on of hands was used for blessing (Gen. 48:14), priestly consecration (Num. 8:10), and healing (Mark 6:5), as well as for the transfer of sin to a sacrificial animal (Lev. 1:4).</p><p>Figuratively, <em>the hand of God</em> is one of the most pervasive biblical metaphors for divine power and providential action: the exodus from Egypt was accomplished by <em>a mighty hand and an outstretched arm</em> (Deut. 26:8); God's hand disciplines the wicked (Ps. 9:16); and nothing can be snatched from the Father's hand (John 10:29). The gesture of lifting hands in prayer signifies supplication and surrender (Ps. 28:2; 1 Tim. 2:8). To wash the hands signifies innocence (Ps. 26:6; Matt. 27:24), while clean hands are a sign of integrity before God (Job 17:9; Ps. 24:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hand", "isbe": "hand"},
        "key_refs": ["Isaiah 1:15", "1 Timothy 2:8", "Psalms 9:16", "John 10:29"]
    },
    "handbreadth": {
        "id": "handbreadth",
        "term": "Handbreadth",
        "category": "concepts",
        "intro": "<p>Handbreadth was a basic unit of linear measurement in the ancient world, defined as the width of four fingers held together across the palm of the hand—approximately three to four inches (7.5–10 cm) in modern equivalents. In tabernacle construction, a handbreadth described the width of the golden border around the table of showbread (Ex. 25:25; 37:12) and the thickness of the rim of the bronze sea in Solomon's temple (1 Kings 7:26; 2 Chr. 4:5).</p><p>The Psalmist uses the handbreadth figuratively to express the brevity of human life: <em>thou hast made my days as a handbreadth; and mine age is as nothing before thee</em> (Ps. 39:5)—contrasting the fleeting span of human existence with the eternal perspective of God. The handbreadth belonged to a system of body-based measurements common throughout the ancient Near East, including the cubit (elbow to fingertip), span (spread hand from thumb to little finger), and finger-width, all of which appear in the technical specifications of Israelite sacred architecture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "handbreadth", "isbe": "handbreadth"},
        "key_refs": ["Exodus 25:25", "Exodus 37:12", "Psalms 39:5"]
    },
    "handkerchief": {
        "id": "handkerchief",
        "term": "Handkerchief",
        "category": "concepts",
        "intro": "<p>Handkerchief (Greek <em>soudarion</em>) appears several times in the New Testament with somewhat varied usages, not always corresponding to the modern article. In Acts 19:12, handkerchiefs and aprons taken from Paul's body were carried to the sick, who were healed and from whom evil spirits departed—a striking extension of healing power through physical contact reminiscent of the healing of the woman who touched Jesus' garment (Mark 5:27–30). This passage reflects a practice of contact relics in apostolic ministry.</p><p>The <em>soudarion</em> was a cloth used to wipe sweat from the face or to wrap the head of the dead (John 11:44; 20:7). In John 20:7 it is specifically the cloth that had been around Jesus' head in the tomb, found folded apart from the burial linen—a detail the evangelist notes in support of the resurrection account. In the parable of the talents, one servant hid his master's money wrapped in a <em>soudarion</em> (Luke 19:20), using it as a simple cloth covering.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "handkerchief", "isbe": "handkerchief"},
        "key_refs": ["Acts 19:12", "John 11:44", "John 20:7", "Luke 19:20"]
    },
    "handmaid": {
        "id": "handmaid",
        "term": "Handmaid",
        "category": "concepts",
        "intro": "<p>Handmaid (Hebrew <em>shiphchah</em> or <em>amah</em>; Greek <em>doule</em>) denotes a female servant or slave, occupying a recognized social position in ancient Israelite households that was distinct from but related to the role of wife. The institution of giving a handmaid to a husband when the wife was barren (as with Sarah and Hagar in Gen. 16:1–3, and Rachel and Leah with their servants in Gen. 30:3–12) was a well-attested legal provision in ancient Near Eastern law codes. Children born of such unions could be claimed as the legal children of the mistress.</p><p>The term also carries a meaning of humility and submission: Ruth refers to herself as a handmaid before Boaz (Ruth 3:9), and Hannah acknowledges herself as God's handmaid in her prayer of distress (1 Sam. 1:11). Most significantly, Mary describes herself as <em>the handmaid of the Lord</em> at the Annunciation (Luke 1:38, 48)—a declaration of complete surrender that became the model of Christian discipleship. The language of servanthood here is not degradation but the highest form of willing obedience.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "handmaid", "isbe": "handmaid"},
        "key_refs": ["Genesis 16:1", "Ruth 3:9", "Luke 1:38", "Luke 1:48"]
    },
    "handwriting": {
        "id": "handwriting",
        "term": "Handwriting",
        "category": "concepts",
        "intro": "<p>Handwriting in biblical usage refers specifically to the <em>handwriting of ordinances</em> (Greek <em>cheirographon</em>) mentioned in Colossians 2:14, where Paul declares that Christ has blotted out <em>the handwriting of ordinances that was against us, which was contrary to us, and took it out of the way, nailing it to his cross.</em> The <em>cheirographon</em> was a technical term in the Greco-Roman world for a handwritten certificate of debt—a bond or IOU signed by the debtor acknowledging what was owed.</p><p>Paul applies this legal metaphor to the Mosaic law and the moral demands of God's ordinances that humanity has violated: Christ's cross simultaneously cancels the certificate of debt and publicly triumphs over the powers that wielded the law as a weapon of condemnation. The image of nailing the document to the cross may reflect the Roman practice of posting the charges against a condemned criminal above his cross (as with the titulus above Jesus' head in John 19:19). The passage is central to Paul's theology of atonement as redemption from legal indebtedness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "handwriting", "isbe": "handwriting"},
        "key_refs": ["Colossians 2:14"]
    },
    "hanes": {
        "id": "hanes",
        "term": "Hanes",
        "category": "places",
        "intro": "<p>Hanes (meaning <em>banishment of grace</em>) was a place in Egypt mentioned once in Isaiah 30:4 in connection with the futile embassy Judah sent to Egypt seeking political and military alliance against Assyria: <em>For his princes were at Zoan, and his ambassadors came to Hanes.</em> The oracle condemns this reliance on Egypt as a broken reed that will pierce rather than support the hand that leans on it (Isa. 30:1–7; 36:6).</p><p>Hanes has been identified by many scholars with Heracleopolis Magna (modern Ihnasya el-Medina), a significant city on the west bank of the Bahr Yusef canal in Middle Egypt, approximately 80 miles south of Cairo. It served as a capital during Egypt's Ninth and Tenth Dynasties and remained an important cult center of Herishef throughout Egyptian history. If this identification is correct, the mention of Zoan (Tanis, in the Delta) and Hanes in the same verse suggests that Judah's envoys were traveling deep into Egypt for this alliance—evidence of how desperate the political situation had become under Assyrian pressure.</p>",
        "hitchcock_meaning": "banishment of grace",
        "source_ids": {"easton": "hanes", "smith": "hanes", "isbe": "hanes"},
        "key_refs": ["Isaiah 30:4"]
    },
    "hanging": {
        "id": "hanging",
        "term": "Hanging",
        "category": "concepts",
        "intro": "<p>Hanging in the Old Testament primarily refers to two distinct practices: execution by hanging (or suspension after death), and the curtains or screens hung in the tabernacle. As a punishment, hanging in ancient Israel typically meant exposure of a body after death as a sign of God's curse and public disgrace—not execution by neck-breaking suspension as in later practice. Deuteronomy 21:22–23 legislates that a hanged man's body must be buried the same day because <em>he that is hanged is accursed of God</em>; the body must not defile the land. Gibeonites demanded that Saul's sons be hanged (2 Sam. 21:6), and Haman was hanged on his own gallows (Esth. 7:10).</p><p>The tabernacle curtains (Ex. 27:9; 35:17; 38:9; Num. 3:26) were screens of fine twisted linen hung on pillars to form the court of the tabernacle and to screen the entrance to the tabernacle proper. These <em>hangings</em> defined the sacred boundary between the ordinary and the holy precincts. Paul cites Deuteronomy 21:23 in Galatians 3:13 to argue that Christ became a curse for us by being hung on a tree—the ultimate identification with the accursed condition that brings redemption.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "hanging", "isbe": "hanging"},
        "key_refs": ["Deuteronomy 21:22", "Deuteronomy 21:23", "Esther 7:10", "Galatians 3:13"]
    },
    "hannah": {
        "id": "hannah",
        "term": "Hannah",
        "category": "people",
        "intro": "<p>Hannah (meaning <em>gracious</em>, <em>merciful</em>, or <em>favor</em>) was one of the two wives of Elkanah, a Levite of Ramathaim-zophim in the hill country of Ephraim. She was barren while Elkanah's other wife Peninnah had children, and Peninnah's taunting provoked Hannah to deep grief. At the sanctuary in Shiloh, Hannah poured out her distress in a prayer so fervent that the priest Eli mistook her for drunk; when he learned she was praying, he blessed her. She vowed that if God gave her a son she would dedicate him to the LORD as a Nazirite all his life (1 Sam. 1:1–28).</p><p>God answered Hannah's prayer, and she bore Samuel—arguably the most pivotal figure in Israel's transition from the judges to the monarchy. She kept her vow by bringing the weaned child to Shiloh to serve under Eli. Hannah's prayer of thanksgiving (1 Sam. 2:1–10) is a remarkable theological poem anticipating the reversal of human fortunes under God's sovereign hand; it served as the direct model for Mary's Magnificat (Luke 1:46–55), making Hannah a type of the mother of the Lord.</p>",
        "hitchcock_meaning": "gracious; merciful; he that gives",
        "source_ids": {"easton": "hannah", "smith": "hannah", "isbe": "hannah"},
        "key_refs": ["1 Samuel 1:11", "1 Samuel 1:20", "1 Samuel 2:1", "Luke 1:46"]
    },
    "hanniel": {
        "id": "hanniel",
        "term": "Hanniel",
        "category": "people",
        "intro": "<p>Hanniel (meaning <em>grace</em> or <em>mercy of God</em>) is the name of two Old Testament figures. The first was a chief of the tribe of Manasseh, the son of Ephod, appointed by Moses as one of the representatives responsible for dividing the land of Canaan among the tribes (Num. 34:23)—one of a group of ten tribal leaders, one per tribe, designated to supervise the distribution of the promised land after the conquest.</p><p>The second Hanniel was a son of Ulla in the tribe of Asher, listed in the genealogy of 1 Chronicles 7:39 among the sons of Asher who were capable warriors and heads of their clans. Both figures appear only in their respective genealogical or administrative contexts and have no further narrative involvement in the biblical text. The name belongs to the family of theophoric names built on the divine name <em>El</em> (God) combined with the root of grace (<em>hnn</em>), reflecting the Israelite practice of naming children to express theological truths about God's character.</p>",
        "hitchcock_meaning": "grace or mercy of God",
        "source_ids": {"easton": "hanniel", "isbe": "hanniel"},
        "key_refs": ["Numbers 34:23", "1 Chronicles 7:39"]
    },
    "hanun": {
        "id": "hanun",
        "term": "Hanun",
        "category": "people",
        "intro": "<p>Hanun (meaning <em>gracious</em> or <em>merciful</em>) is the name of two individuals in the Old Testament. The more significant was Hanun son of Nahash, king of Ammon. When David sent ambassadors to express condolences at Nahash's death, Hanun's advisors persuaded him that the envoys were spies. He humiliated them by shaving off half their beards and cutting their garments to their hips before sending them away—a diplomatic insult that triggered a major military conflict (2 Sam. 10:1–14; 1 Chr. 19:1–19). The Ammonites and their Syrian allies were decisively defeated in two campaigns that extended Israelite dominance in Transjordan and Syria.</p><p>A second Hanun was a post-exilic figure who took part in Nehemiah's repair of the Jerusalem walls, rebuilding a section of the valley gate and part of the wall of the Pool of Shelah (Neh. 3:13, 30). The name's meaning of gracious mercy stands in ironic contrast to the actions of the Ammonite king whose diplomatic insult precipitated a war.</p>",
        "hitchcock_meaning": "gracious; merciful",
        "source_ids": {"easton": "hanun", "smith": "hanun", "isbe": "hanun"},
        "key_refs": ["2 Samuel 10:1", "2 Samuel 10:4", "Nehemiah 3:13"]
    },
    "hara": {
        "id": "hara",
        "term": "Hara",
        "category": "places",
        "intro": "<p>Hara (meaning <em>a hill</em> or <em>mountainous land</em>) was a province of the Assyrian empire to which Israelite exiles from the Transjordanian tribes of Reuben, Gad, and half-Manasseh were deported when the Assyrian king Tilgath-pilneser (Tiglath-pileser III) carried them away captive (1 Chr. 5:26). It is mentioned alongside the Habor River, the Gozan River, and the cities of the Medes as exile destinations.</p><p>Hara is mentioned only in this single verse, which has led some textual scholars to propose that the word <em>hara</em> may be a scribal corruption of <em>Hara</em> (Hebrew for <em>mountains</em>), that it might be the same as the cities of the Medes mentioned in 2 Kings 17:6, or that it designates a specific Assyrian administrative district not yet identified in extrabiblical sources. The Assyrian policy of dispersing conquered populations across the empire's different provinces was systematic, and the mention of multiple destinations for the Israelite exiles reflects the administrative reality of that policy.</p>",
        "hitchcock_meaning": "a hill; showing forth",
        "source_ids": {"easton": "hara", "smith": "hara", "isbe": "hara"},
        "key_refs": ["1 Chronicles 5:26"]
    },
    "haradah": {
        "id": "haradah",
        "term": "Haradah",
        "category": "places",
        "intro": "<p>Haradah (meaning <em>fright</em> or <em>fear</em>, possibly <em>well of great fear</em>) was one of the forty-two stations of the Israelite wilderness journey, listed in the detailed itinerary of Numbers 33. It appears as the twenty-fifth encampment, situated between Makheloth and Tahath (Num. 33:24–25), in the long sequence of stations that the Israelites traversed after leaving Sinai and before arriving in the plains of Moab.</p><p>Like the majority of the wilderness stations, Haradah has not been identified with a specific modern site. The attempt to map the Exodus route has occupied scholars for centuries, with multiple competing proposals for the path from Egypt through the Sinai Peninsula to Transjordan. Haradah's name—suggesting fear or trembling—may reflect a memorable event or natural feature at that location, though no narrative is attached to it in the biblical text. The preservation of such specific names in the Numbers itinerary suggests the list derives from authentic records of the journey.</p>",
        "hitchcock_meaning": "well of great fear",
        "source_ids": {"easton": "haradah", "smith": "haradah", "isbe": "haradah"},
        "key_refs": ["Numbers 33:24"]
    },
    "haran": {
        "id": "haran",
        "term": "Haran",
        "category": "places",
        "intro": "<p>Haran designates both a person and an important city in the patriarchal narratives. As a person, Haran was the eldest son of Terah and the younger brother of Abraham, the father of Lot and of Milcah (Gen. 11:26–31). He died in Ur of the Chaldees before his father Terah, the first recorded death in the patriarchal genealogies. As a city, Haran (also spelled Charran) was a major commercial center in northwestern Mesopotamia on the Balikh River, a tributary of the Euphrates in what is now southeastern Turkey, where Terah's family settled after leaving Ur (Gen. 11:31–32).</p><p>Haran the city was where Terah died and where Abraham received the divine call to continue to Canaan (Gen. 12:1–5; Acts 7:2–4). It was also the home of Abraham's relatives, including Laban, to whom Rebekah belonged (Gen. 24:10) and to whom Jacob fled after deceiving Esau (Gen. 27:43). Haran was a well-attested Assyrian city, an important center of moon-god worship, and a major point on the ancient caravan routes connecting Mesopotamia with the Levant. Assyrian records confirm its prominence, and 2 Kings 19:12 mentions its conquest by Assyria.</p>",
        "hitchcock_meaning": "mountainous country",
        "source_ids": {"easton": "haran", "smith": "haran"},
        "key_refs": ["Genesis 11:31", "Genesis 12:1", "Acts 7:2", "2 Kings 19:12"]
    },
    "harbona": {
        "id": "harbona",
        "term": "Harbona",
        "category": "people",
        "intro": "<p>Harbona (a Persian name meaning <em>ass-driver</em>) was one of the seven chamberlains or eunuchs who served King Ahasuerus (Xerxes I) at the royal court of Persia. He is mentioned twice in the book of Esther: first in the opening chapter (Esth. 1:10) among the seven officials sent to summon Queen Vashti to the royal banquet, and second in the climactic scene of Haman's downfall (Esth. 7:9).</p><p>Harbona's second appearance is pivotal: as Esther has just revealed Haman's plot to destroy the Jews, and the king rises in fury from the banquet and walks into the palace garden, Harbona speaks up to inform the king that Haman has built a gallows fifty cubits high in his own courtyard for the purpose of hanging Mordecai—the very man who saved the king's life. The king's immediate response, <em>Hang him thereon</em>, seals Haman's fate. Whether Harbona's intervention was providential loyalty to Mordecai or simple courtly opportunism, his single sentence becomes the turning point of the entire narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "harbona", "smith": "harbona"},
        "key_refs": ["Esther 1:10", "Esther 7:9"]
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
    print(f'BP h1: Habakkuk → Harbona: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
