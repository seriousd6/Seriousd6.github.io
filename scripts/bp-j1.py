#!/usr/bin/env python3
"""BP J1 — Jaakan → Jediael (75 articles)."""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    p = os.path.join(OUT_DIR, f'{slug}.json')
    with open(p, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
"jaakan": {
    "term": "Jaakan",
    "category": "names",
    "intro": "<p>Jaakan (meaning <em>tribulation; labor</em>), also called Akan or Jakan (Gen. 36:27; 1 Chr. 1:42), was a Horite chief in Edom, the son of Ezer and grandson of Seir. His descendants gave their name to Beeroth-bene-jaakan (\"wells of the sons of Jaakan\"), a stopping point in Israel's wilderness journey listed in Numbers 33:31–32 and Deuteronomy 10:6. The name appears in slightly varied forms in the biblical text — Jaakan, Akan, and Jakan — reflecting the normal orthographic variation in ancient Semitic names.</p>",
    "hitchcock_meaning": "tribulation; labor",
    "source_ids": {"easton": "jaakan"},
    "key_refs": ["Numbers 33:31", "Deuteronomy 10:6", "Genesis 36:27"]
},
"jaakobah": {
    "term": "Jaakobah",
    "category": "names",
    "intro": "<p>Jaakobah (meaning <em>supplanter; deceiver; the heel</em>, essentially the same as Jacob) was a prince or chief of the tribe of Simeon, listed among those whose families increased greatly during the days of King Hezekiah and who expelled the Meunites to occupy the valley of Gedor in the Negev (1 Chr. 4:36–41). He appears only in this genealogical and historical summary of Simeon's later territorial expansion and is not otherwise mentioned in the biblical narrative.</p>",
    "hitchcock_meaning": "supplanter; deceiver; the heel",
    "source_ids": {"easton": "jaakobah"},
    "key_refs": ["1 Chronicles 4:36"]
},
"jaala": {
    "term": "Jaala",
    "category": "names",
    "intro": "<p>Jaala (also Jaalah; meaning <em>ascending; a little doe or goat</em>) was the ancestor of a family of temple servants (Nethinim) who returned with Zerubbabel from the Babylonian exile (Ezra 2:56; Neh. 7:58). The Nethinim were assistants to the Levites in temple service, and their faithful return to Jerusalem after the exile contributed to the restoration of temple worship. Jaala appears only in these census lists from the post-exilic period.</p>",
    "hitchcock_meaning": "ascending; a little doe or goat",
    "source_ids": {"easton": "jaala"},
    "key_refs": ["Ezra 2:56", "Nehemiah 7:58"]
},
"jaalam": {
    "term": "Jaalam",
    "category": "names",
    "intro": "<p>Jaalam (meaning <em>hidden; young man; heir</em>) was the second son of Esau by Aholibamah, the daughter of Anah (Gen. 36:5, 14, 18; 1 Chr. 1:35). He was one of the chiefs (dukes) who came out of Esau in the land of Edom. The Genesis 36 genealogy establishes the lineage of the Edomite clans who would be perpetual neighbors of Israel, and Jaalam is one of Edom's founding tribal ancestors. Nothing further is recorded about him.</p>",
    "hitchcock_meaning": "hidden; young man; heir",
    "source_ids": {"easton": "jaalam"},
    "key_refs": ["Genesis 36:5", "Genesis 36:18", "1 Chronicles 1:35"]
},
"jaanai": {
    "term": "Jaanai",
    "category": "names",
    "intro": "<p>Jaanai (meaning <em>answering; afflicting; making poor</em>) was a chief of the tribe of Gad, listed among the heads of the Gadite families who dwelt in Gilead in Bashan (1 Chr. 5:12). He appears only in this genealogical register of the Gadites and is not otherwise mentioned in the biblical narrative. The Gadite chiefs were men of valor who occupied the trans-Jordan territories east of the Sea of Galilee.</p>",
    "hitchcock_meaning": "answering; afflicting; making poor",
    "source_ids": {"easton": "jaanai"},
    "key_refs": ["1 Chronicles 5:12"]
},
"jaare-oregim": {
    "term": "Jaare-oregim",
    "category": "names",
    "intro": "<p>Jaare-oregim was the father of Elhanan the Bethlehemite, who slew a Philistine giant during David's wars (2 Sam. 21:19). The parallel account in 1 Chronicles 20:5 names the father as Jair, and identifies the victim as Lahmi the brother of Goliath — a difference that has generated much textual discussion. Most scholars regard the Samuel text as containing a scribal error and the Chronicles text as preserving the original reading. The name <em>oregim</em> means \"weavers\" and may be a scribal intrusion from the end of the verse where Goliath's spear staff is compared to a weaver's beam.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jaare-oregim"},
    "key_refs": ["2 Samuel 21:19", "1 Chronicles 20:5"]
},
"jaasau": {
    "term": "Jaasau",
    "category": "names",
    "intro": "<p>Jaasau (meaning <em>doing; my doing</em>) was one of the Israelites who had married foreign wives during the Babylonian exile period and was required by Ezra's reform to put away his foreign wife (Ezra 10:37). He is listed among the sons of Bani who responded to Ezra's call for covenant renewal and racial separation. The episode reflects the post-exilic concern for preserving the community's identity and covenant obligations.</p>",
    "hitchcock_meaning": "doing; my doing",
    "source_ids": {"easton": "jaasau"},
    "key_refs": ["Ezra 10:37"]
},
"jaasiel": {
    "term": "Jaasiel",
    "category": "names",
    "intro": "<p>Jaasiel (meaning <em>God's work</em>) is the name of two men. (1.) A Mesobaite, one of David's mighty men listed in 1 Chronicles 11:47. (2.) The son of Abner, who was appointed leader of the tribe of Benjamin in David's administrative organization (1 Chr. 27:21). The name expresses the conviction that God himself is at work in the lives of his people — a sentiment common to many Hebrew theophoric names from the period of the united monarchy.</p>",
    "hitchcock_meaning": "God's work",
    "source_ids": {"easton": "jaasiel"},
    "key_refs": ["1 Chronicles 11:47", "1 Chronicles 27:21"]
},
"jaaz-aniah": {
    "term": "Jaaz-aniah",
    "category": "names",
    "intro": "<p>Jaaz-aniah (meaning <em>the strength of the Lord</em>, similar to Jaaziel) appears in two distinct contexts. (1.) A Rechabite chief whose faithfulness to the Rechabite vow of abstinence from wine Jeremiah used as an object lesson of covenantal faithfulness (Jer. 35:3). The Rechabites honored their ancestor Jonadab's command not to drink wine, live in houses, or plant vineyards — in contrast to Israel's persistent disobedience of God's commands. (2.) A son of Shaphan seen in Ezekiel's vision of idolatry practiced by Jerusalem's elders in a secret chamber of the temple (Ezek. 8:11).</p>",
    "hitchcock_meaning": "the strength of the Lord",
    "source_ids": {"easton": "jaaz-aniah"},
    "key_refs": ["Jeremiah 35:3", "Ezekiel 8:11"]
},
"jaazer": {
    "term": "Jaazer",
    "category": "places",
    "intro": "<p>Jaazer (meaning <em>God helps</em>) was an Amorite city east of the Jordan River in the region of Gilead, captured by the Israelites as they passed through Transjordan (Num. 21:32). It was subsequently assigned to the tribe of Gad (Num. 32:1, 35; Josh. 13:25) and designated a Levitical city for the Merarites (Josh. 21:39; 1 Chr. 6:81). The city was known for its excellent pasturage and came under Moabite control in later periods (Isa. 16:8–9; Jer. 48:32). David sent officials there to conduct a census of the Gadites (1 Chr. 26:31).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jaazer"},
    "key_refs": ["Numbers 32:1", "Joshua 13:25", "Isaiah 16:8"]
},
"jaaziah": {
    "term": "Jaaziah",
    "category": "names",
    "intro": "<p>Jaaziah (meaning <em>the strength of the Lord</em>) was a Levite of the family of Merari, listed in the organization of temple service under David (1 Chr. 24:26–27). He had three sons — Beno, Shoham, and Zaccur — who were assigned responsibilities in the temple. The Merarites were the third division of the Levites responsible for transporting and caring for the structural elements of the tabernacle. Jaaziah appears only in this administrative record.</p>",
    "hitchcock_meaning": "the strength of the Lord",
    "source_ids": {"easton": "jaaziah"},
    "key_refs": ["1 Chronicles 24:26"]
},
"jaaziel": {
    "term": "Jaaziel",
    "category": "names",
    "intro": "<p>Jaaziel (meaning <em>the strength of the Lord</em>, variant of Jaaziah) was a Levitical musician appointed by David to play the harp (<em>psaltery</em>) when the ark of the covenant was brought up to Jerusalem (1 Chr. 15:18, 20). He was among the second rank of gate-keepers and instrumentalists who accompanied the ark procession. In 1 Chronicles 16:5 the same individual appears to be called Aziel. The name reflects the devout conviction that God himself is the source of the worshiper's strength.</p>",
    "hitchcock_meaning": "the strength of the Lord",
    "source_ids": {"easton": "jaaziel"},
    "key_refs": ["1 Chronicles 15:18", "1 Chronicles 15:20"]
},
"jabal": {
    "term": "Jabal",
    "category": "people",
    "intro": "<p>Jabal (meaning <em>which glides away</em>) was the son of Lamech and Adah, a descendant of Cain, described as \"the father of such as dwell in tents, and of such as have cattle\" (Gen. 4:20). He is presented as the ancestor of the pastoral nomadic way of life — those who raised livestock and lived in portable tents. His brother Jubal was the ancestor of musicians, and his half-brother Tubal-cain was the ancestor of metalworkers. These three brothers represent the three primary cultural streams of early human civilization: pastoral nomadism, music and the arts, and metalworking. The genealogy of Cain's line (Gen. 4:17–24) culminates in Lamech's violent boast, contrasting with the godly line of Seth.</p>",
    "hitchcock_meaning": "which glides away",
    "source_ids": {"easton": "jabal"},
    "key_refs": ["Genesis 4:20"]
},
"jabbok": {
    "term": "Jabbok",
    "category": "places",
    "intro": "<p>Jabbok (meaning <em>emptying; pouring out; wrestling</em>) is the stream that flows westward from the mountains of Gilead and empties into the Jordan River approximately midway between the Sea of Galilee and the Dead Sea. It is identified with the modern Nahr ez-Zerqa (\"Blue River\"). The Jabbok marked the northern border of the territory of Sihon king of the Amorites and the southern boundary of the Ammonites (Num. 21:24; Deut. 3:16; Josh. 12:2). Its most famous appearance in Scripture is the night Jacob wrestled with the divine Stranger on its bank as he prepared to meet Esau after twenty years — the mysterious encounter in which Jacob's name was changed to Israel and his hip was put out of joint (Gen. 32:22–32). The river's name and the wrestling narrative share a common Hebrew root (<em>yabok / abak</em>).</p>",
    "hitchcock_meaning": "evacuation; dissipation; wrestling",
    "source_ids": {"easton": "jabbok", "smith": "jabbok"},
    "key_refs": ["Genesis 32:22", "Numbers 21:24", "Deuteronomy 3:16"]
},
"jabesh": {
    "term": "Jabesh",
    "category": "places",
    "intro": "<p>Jabesh (meaning <em>dryness; confusion; shame</em>) is used both as an abbreviation for Jabesh-gilead (see that entry) and as the name of the father of Shallum, who killed Zechariah king of Israel and seized the throne (2 Kings 15:10–14). The town of Jabesh-gilead was located east of the Jordan in the highlands of Gilead. It had a special connection with Saul: when the Ammonite king Nahash threatened the city, Saul rescued it (1 Sam. 11:1–11), and it was the men of Jabesh-gilead who honorably retrieved Saul's body from the Philistine wall of Beth-shan after his death (1 Sam. 31:11–13).</p>",
    "hitchcock_meaning": "dryness; confusion; shame",
    "source_ids": {"easton": "jabesh"},
    "key_refs": ["1 Samuel 11:1", "1 Samuel 31:11", "2 Kings 15:10"]
},
"jabesh-gilead": {
    "term": "Jabesh-Gilead",
    "category": "places",
    "intro": "<p>Jabesh-gilead was a town in the highlands of Gilead east of the Jordan, within the territory of the half-tribe of Manasseh, visible from Beth-shan across the valley. Its first mention involves a grim episode: after the civil war over the outrage at Gibeah, the town's inhabitants were destroyed for failing to join Israel's assembly, with 400 virgin daughters preserved as wives for the surviving Benjaminites (Judg. 21:8–14). Its most honored moment came when Saul gathered his forces to rescue the town from Nahash the Ammonite's threat to gouge out the right eye of every inhabitant (1 Sam. 11:1–11). This event catalyzed Saul's recognition as king. After Saul's death at Gilboa, the men of Jabesh-gilead — remembering Saul's deliverance — traveled all night to retrieve his body from the wall of Beth-shan, gave it honorable burial, and fasted seven days (1 Sam. 31:11–13; 2 Sam. 2:4–6).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jabesh-gilead", "smith": "jabesh-gilead"},
    "key_refs": ["Judges 21:8", "1 Samuel 11:1", "1 Samuel 31:11"]
},
"jabez": {
    "term": "Jabez",
    "category": "people",
    "intro": "<p>Jabez (meaning <em>sorrow; trouble</em>) was a man of Judah, mentioned in a brief and striking parenthesis in 1 Chronicles 4:9–10: \"And Jabez was more honourable than his brethren: and his mother called his name Jabez, saying, Because I bare him with sorrow. And Jabez called on the God of Israel, saying, Oh that thou wouldest bless me indeed, and enlarge my coast, and that thine hand might be with me, and that thou wouldest keep me from evil, that it may not grieve me! And God granted him that which he requested.\" His name meant \"pain\" or \"sorrow\" — a burden he overcame through prayer. The prayer of Jabez, with its fourfold request for blessing, territory, divine presence, and protection from evil, became celebrated in Christian devotional literature. A place called Jabez, inhabited by families of scribes, is also mentioned in 1 Chronicles 2:55.</p>",
    "hitchcock_meaning": "sorrow; trouble",
    "source_ids": {"easton": "jabez"},
    "key_refs": ["1 Chronicles 4:9", "1 Chronicles 4:10"]
},
"jabin": {
    "term": "Jabin",
    "category": "people",
    "intro": "<p>Jabin (meaning <em>discerner; the wise</em>) is the name of two kings of Hazor in northern Canaan. (1.) Jabin king of Hazor formed a great northern coalition against Joshua at the time of the conquest, but was defeated at the Waters of Merom; Hazor was then burned (Josh. 11:1–14). (2.) A later king of Hazor (likely a dynastic name) who oppressed Israel for twenty years, employing Sisera as his military commander with 900 iron chariots. The prophetess Deborah and the general Barak rallied Israel against him; his forces were routed at the river Kishon, and Sisera was killed by Jael (Judg. 4–5). The victory is celebrated in the song of Deborah, one of the oldest poems in the Bible. Psalm 83:9 invokes the defeat of Jabin as a model for prayers against Israel's enemies.</p>",
    "hitchcock_meaning": "he that understands; building",
    "source_ids": {"easton": "jabin", "smith": "jabin"},
    "key_refs": ["Joshua 11:1", "Judges 4:2", "Judges 4:24", "Psalms 83:9"]
},
"jabneel": {
    "term": "Jabneel",
    "category": "places",
    "intro": "<p>Jabneel (meaning <em>building of God</em>) appears as the name of two places. (1.) A town on the northern boundary of Judah near the Mediterranean coast (Josh. 15:11), identified with the later Jabneh or Jamnia, an important city southwest of Joppa. After the fall of Jerusalem in 70 A.D., Jabneh became the seat of the reconstituted Sanhedrin and the center of rabbinic Judaism where the canon of the Hebrew Bible was discussed. (2.) A town on the southern boundary of Naphtali (Josh. 19:33). Uzziah king of Judah broke down the wall of Jabneel (2 Chr. 26:6).</p>",
    "hitchcock_meaning": "building of God",
    "source_ids": {"easton": "jabneel"},
    "key_refs": ["Joshua 15:11", "2 Chronicles 26:6"]
},
"jabneh": {
    "term": "Jabneh",
    "category": "places",
    "intro": "<p>Jabneh was a Philistine city on the coastal plain whose wall was broken down by Uzziah king of Judah as part of his military expansion into Philistine territory (2 Chr. 26:6). It is identified with the Jabneel of Joshua 15:11 and the later Jamnia of the Hellenistic and Roman periods. After 70 A.D., Jamnia (Jabneh) became the most important center of Jewish learning in Palestine, replacing Jerusalem as the seat of rabbinic authority.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jabneh"},
    "key_refs": ["2 Chronicles 26:6"]
},
"jachan": {
    "term": "Jachan",
    "category": "names",
    "intro": "<p>Jachan (meaning <em>wearing out; oppressing</em>) was a Gadite chief listed among the heads of family clans in 1 Chronicles 5:13. He belonged to the trans-Jordan settlement of Gad in the territory of Gilead and Bashan, one of the leaders of the tribe whose genealogy is recorded alongside accounts of their warfare against the Hagrites and their settlement east of the Jordan. No further narrative details about Jachan are preserved in Scripture.</p>",
    "hitchcock_meaning": "wearing out; oppressing",
    "source_ids": {"easton": "jachan"},
    "key_refs": ["1 Chronicles 5:13"]
},
"jachin": {
    "term": "Jachin",
    "category": "names",
    "intro": "<p>Jachin (meaning <em>he that strengthens and makes steadfast</em>) is the name of several persons and one of the two bronze pillars of Solomon's temple (see Jachin and Boaz). As a personal name: (1.) The fourth son of Simeon (Gen. 46:10; Ex. 6:15), ancestor of the Jachinite clan (Num. 26:12). (2.) The head of the twenty-first course of priests in David's organization (1 Chr. 24:17). (3.) A priest who returned from exile (1 Chr. 9:10; Neh. 11:10). The name was popular in priestly circles, perhaps because it expressed the stability of divine support for the worshiping community.</p>",
    "hitchcock_meaning": "he that strengthens and makes steadfast",
    "source_ids": {"easton": "jachin"},
    "key_refs": ["Genesis 46:10", "1 Kings 7:21", "1 Chronicles 24:17"]
},
"jachin-and-boaz": {
    "term": "Jachin and Boaz",
    "category": "concepts",
    "intro": "<p>Jachin and Boaz were the two great bronze pillars erected at the entrance of Solomon's temple in Jerusalem (1 Kings 7:15–22; 2 Chr. 3:15–17). Each pillar was 18 cubits high (approximately 27 feet) and 12 cubits in circumference, topped with an elaborate capital of lily-work and chains decorated with pomegranates. Jachin (\"he shall establish\") stood on the right (south) side of the entrance, and Boaz (\"in it is strength\") on the left (north). Their precise function has been debated: whether they were structural supports, freestanding memorial pillars, or great lamp-stands. Their names together may have proclaimed a royal dedication formula: \"He shall establish in strength.\" Both pillars were destroyed and carried to Babylon when Nebuchadnezzar sacked Jerusalem (2 Kings 25:13; Jer. 52:17–23).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jachin-and-boaz"},
    "key_refs": ["1 Kings 7:21", "2 Chronicles 3:17", "2 Kings 25:13"]
},
"jacinth": {
    "term": "Jacinth",
    "category": "concepts",
    "intro": "<p>Jacinth (hyacinth) is a precious stone of deep reddish-blue or violet color appearing in the book of Revelation. It is listed as the eleventh foundation stone of the New Jerusalem (Rev. 21:20) and appears in the description of the locust-horsemen: \"breastplates of fire, and of jacinth, and brimstone\" (Rev. 9:17), where the color is part of a terrifying vision. The Hebrew word <em>leshem</em> in Exodus 28:19 (the ninth stone of the high priest's breastplate) may correspond to jacinth or to the amber-orange topaz, but exact identification is uncertain due to the imprecision of ancient gem nomenclature. The stone was prized in antiquity for its transparency and deep color.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jacinth"},
    "key_refs": ["Revelation 21:20", "Revelation 9:17", "Exodus 28:19"]
},
"jacob": {
    "term": "Jacob",
    "category": "people",
    "intro": "<p>Jacob (meaning <em>one who supplants; he follows on the heel</em>) was the younger of Isaac's twin sons and the third of the patriarchs, whose name was changed to Israel after his night of wrestling at the Jabbok (Gen. 32:28). Born grasping his brother Esau's heel (Gen. 25:26), Jacob's life was marked by struggle, cunning, and a deepening relationship with God. He obtained the birthright from Esau for a bowl of stew (Gen. 25:29–34) and secured the blessing by deceiving his blind father Isaac (Gen. 27). He fled to Haran, where he served Laban twenty years, married Leah and Rachel, and fathered twelve sons — the fathers of the twelve tribes of Israel. His encounter with God at Bethel (Gen. 28) and his name-change to Israel at Peniel (Gen. 32:28) mark the decisive turning points of his spiritual journey. In his old age he moved to Egypt at Joseph's invitation, blessed the pharaoh (Gen. 47:10), and delivered prophetic blessings to his twelve sons (Gen. 49) before dying and being carried back to Canaan for burial in Machpelah. Paul cites the election of Jacob over Esau as a supreme example of divine sovereign grace (Rom. 9:11–13).</p>",
    "hitchcock_meaning": "that supplants, undermines; the heel",
    "source_ids": {"easton": "jacob", "smith": "jacob", "isbe": "jacob"},
    "key_refs": ["Genesis 25:26", "Genesis 28:12", "Genesis 32:28", "Romans 9:13"]
},
"jacobs-well": {
    "term": "Jacob's Well",
    "category": "places",
    "intro": "<p>Jacob's Well is a site in the ancient city of Sychar (Shechem) in Samaria where Jesus' encounter with the Samaritan woman took place (John 4:5–6). The well was dug by Jacob in the \"parcel of ground\" he purchased from Hamor's sons near Shechem (Gen. 33:19; Josh. 24:32) — ground he later gave to his son Joseph (Gen. 48:22). At approximately 100 feet deep, cut through limestone and fed by both springs and percolation, it is one of the few Gospel sites whose identification is virtually certain; it has been visited by pilgrims since at least the 4th century. Jesus' conversation here with the Samaritan woman, in which he offered \"living water\" welling up to eternal life (John 4:10–14), is one of the richest dialogues in the Gospels.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jacobs-well"},
    "key_refs": ["John 4:6", "John 4:14", "Genesis 33:19"]
},
"jaddua": {
    "term": "Jaddua",
    "category": "names",
    "intro": "<p>Jaddua (meaning <em>known</em>) is the name of two men. (1.) A Levite who sealed the covenant of national renewal under Nehemiah (Neh. 10:21). (2.) The high priest who is mentioned as the last high priest named in the book of Nehemiah (Neh. 12:11, 22), serving in the days of Darius the Persian. Josephus records a tradition that this Jaddua was high priest when Alexander the Great visited Jerusalem (c. 332 B.C.) and was shown the prophecy of Daniel concerning the Greek conquest, but this is not confirmed by Scripture. The genealogy through Jaddua represents the line of high priests into the early Hellenistic period.</p>",
    "hitchcock_meaning": "known",
    "source_ids": {"easton": "jaddua"},
    "key_refs": ["Nehemiah 12:11", "Nehemiah 10:21"]
},
"jadon": {
    "term": "Jadon",
    "category": "names",
    "intro": "<p>Jadon the Meronothite was one of those who helped Nehemiah repair the walls of Jerusalem after the return from exile, working on the section opposite the broad wall (Neh. 3:7). He is listed alongside Melatiah the Gibeonite. The Meronothites were inhabitants of Meronoth, a place in Benjamin or Judah. Beyond this one mention in the wall-repair register, nothing else is known of Jadon from Scripture.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jadon"},
    "key_refs": ["Nehemiah 3:7"]
},
"jael": {
    "term": "Jael",
    "category": "people",
    "intro": "<p>Jael (meaning <em>he that ascends; a kid</em>) was the wife of Heber the Kenite, celebrated in the song of Deborah as \"blessed above women\" for her killing of Sisera, the Canaanite general who commanded Jabin's 900 iron chariots (Judg. 4:17–22; 5:24–27). When Sisera's army was routed by Barak and Deborah at the Kishon River, he fled on foot and sought refuge with Jael's household, which was at peace with Jabin's king. Jael welcomed him, hid him under a rug, gave him milk when he asked for water, and when he slept drove a tent peg through his temple with a mallet, killing him. The act is morally complex — scholars debate whether it constituted a betrayal of hospitality or a legitimate act of resistance — but the narrative and the song celebrate it as God's vindication of Israel through an unexpected instrument.</p>",
    "hitchcock_meaning": "he that ascends; a kid",
    "source_ids": {"easton": "jael", "smith": "jael"},
    "key_refs": ["Judges 4:17", "Judges 4:21", "Judges 5:24"]
},
"jagur": {
    "term": "Jagur",
    "category": "places",
    "intro": "<p>Jagur (meaning <em>husbandman; stranger</em>) was a town in the extreme south of Judah, near the Edomite border, listed among the southern cities allotted to Judah in Joshua 15:21. It is grouped with Kabzeel and Eder in the Negev district. The site has not been positively identified in modern surveys. It appears only in this boundary and city list and plays no further role in the biblical narrative.</p>",
    "hitchcock_meaning": "husbandman; stranger",
    "source_ids": {"easton": "jagur"},
    "key_refs": ["Joshua 15:21"]
},
"jah": {
    "term": "Jah",
    "category": "concepts",
    "intro": "<p>Jah is a poetic contraction of <em>YHWH</em> (Yahweh), the covenant name of Israel's God, used especially in poetry and doxology. It appears 49 times in the Hebrew Bible, most frequently in the Psalms, and is embedded in the exclamation <em>Hallelujah</em> (\"praise Yah\"). The form appears explicitly in Psalm 68:4: \"Extol him that rideth upon the heavens by his name JAH, and rejoice before him.\" It also appears in compound names like Elijah (<em>Eliyahu</em>, \"my God is Yah\"), Isaiah (<em>Yesha'yahu</em>, \"salvation of Yah\"), and Jeremiah (<em>Yirmeyahu</em>). The name points to the eternal, self-existent being of God — the One who IS.</p>",
    "hitchcock_meaning": "the everlasting",
    "source_ids": {"easton": "jah"},
    "key_refs": ["Psalms 68:4", "Revelation 19:1"]
},
"jahath": {
    "term": "Jahath",
    "category": "names",
    "intro": "<p>Jahath (meaning <em>broken in pieces; descending</em>) is the name of several men. (1.) A son of Reaiah, descendant of Judah (1 Chr. 4:2). (2.) A Levite, son of Libni, a Gershonite (1 Chr. 6:20, 43). (3.) A son of Shimei, a Gershonite Levite in David's organization (1 Chr. 23:10–11). (4.) An Izharite Levite in David's service (1 Chr. 24:22). (5.) A Merarite Levite who supervised repairs to the temple under Josiah (2 Chr. 34:12). The name was common among the Levitical families, suggesting a hereditary usage within particular clans.</p>",
    "hitchcock_meaning": "broken in pieces; descending",
    "source_ids": {"easton": "jahath"},
    "key_refs": ["1 Chronicles 6:20", "2 Chronicles 34:12"]
},
"jahaz": {
    "term": "Jahaz",
    "category": "places",
    "intro": "<p>Jahaz (also Jahaza or Jahzah; meaning <em>quarrel; dispute</em>) was the site of Israel's decisive battle against Sihon king of the Amorites, in which Moses led Israel to victory and took possession of all Sihon's land (Num. 21:23–25; Deut. 2:32–36; Judg. 11:20). The city was subsequently assigned to Reuben (Josh. 13:18) and designated a Levitical city (Josh. 21:36; 1 Chr. 6:78). The Moabite Stone (Mesha Stele, 9th century B.C.) mentions Jahaz as having been taken from Israel by Moab, and both Isaiah and Jeremiah include it in their prophecies against Moab (Isa. 15:4; Jer. 48:21, 34). The site is identified in the area of the Medeba plateau in modern Jordan.</p>",
    "hitchcock_meaning": "quarrel; dispute",
    "source_ids": {"easton": "jahaz"},
    "key_refs": ["Numbers 21:23", "Deuteronomy 2:32", "Isaiah 15:4"]
},
"jahaziel": {
    "term": "Jahaziel",
    "category": "people",
    "intro": "<p>Jahaziel (meaning <em>seeing God; beheld by God</em>) is most significantly a Levite of the sons of Asaph who received a prophetic word from the Spirit of the LORD when Jehoshaphat's prayer sought deliverance from a vast coalition of Moabites and Ammonites: \"Thus saith the LORD unto you, Be not afraid nor dismayed by reason of this great multitude; for the battle is not yours, but God's\" (2 Chr. 20:14–17). Acting on the prophecy, Jehoshaphat sent singers before the army praising God; when they arrived at the battleground, the enemy coalition had already destroyed one another. This Jahaziel was a Levitical prophet in the tradition of prophetic music and intercession. Other men named Jahaziel appear in the lists of Benjaminite warriors who joined David (1 Chr. 12:4) and in post-exilic registers (Ezra 8:5).</p>",
    "hitchcock_meaning": "seeing God",
    "source_ids": {"easton": "jahaziel"},
    "key_refs": ["2 Chronicles 20:14", "2 Chronicles 20:17"]
},
"jahdai": {
    "term": "Jahdai",
    "category": "names",
    "intro": "<p>Jahdai was a man of Judah listed in the genealogical records of 1 Chronicles 2:47, whose sons — Regem, Jotham, Geshan, Pelet, Ephah, and Shaaph — are named. He appears in the family line of Caleb through a concubine, within the complex genealogical account of Judah's descendants. No further narrative details about Jahdai appear in Scripture; his significance is solely genealogical.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jahdai"},
    "key_refs": ["1 Chronicles 2:47"]
},
"jahzeel": {
    "term": "Jahzeel",
    "category": "names",
    "intro": "<p>Jahzeel (also Jahziel; meaning <em>God hasteth; God divideth</em>) was the firstborn son of Naphtali and ancestor of the Jahzeelite clan (Gen. 46:24; Num. 26:48; 1 Chr. 7:13). As one of the seventy who went down to Egypt with Jacob (Gen. 46:24), he was among the founding generation of the tribe of Naphtali. His descendants formed one of the principal clans of that tribe in the subsequent census registers.</p>",
    "hitchcock_meaning": "God hasteth, or divideth",
    "source_ids": {"easton": "jahzeel"},
    "key_refs": ["Genesis 46:24", "Numbers 26:48"]
},
"jahzerah": {
    "term": "Jahzerah",
    "category": "names",
    "intro": "<p>Jahzerah was a priest listed among those who settled in Jerusalem after the return from Babylonian exile (1 Chr. 9:12), a descendant of Immer through Meshullam and Meshillemith. He served in the restored temple community. The parallel list in Nehemiah 11:13 gives the name as Ahasai or Ahzai, a variant form. He represents the continuity of priestly families across the exile — the same family lines serving in the temple before and after the Babylonian captivity.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jahzerah"},
    "key_refs": ["1 Chronicles 9:12"]
},
"jailer": {
    "term": "Jailer",
    "category": "people",
    "intro": "<p>The jailer of Philippi is the unnamed official in charge of the prison where Paul and Silas were held after being beaten and imprisoned for casting a spirit of divination out of a slave girl (Acts 16:23–34). At midnight, while Paul and Silas were praying and singing hymns, a great earthquake opened the prison doors and loosed all the prisoners' chains. The jailer, waking and assuming all had escaped, was about to kill himself when Paul called out to stop him. The jailer came trembling, fell before Paul and Silas, and asked the central question: \"What must I do to be saved?\" — to which Paul answered, \"Believe on the Lord Jesus Christ, and thou shalt be saved, and thy house.\" That night the jailer washed their wounds, and he and his entire household were baptized, \"rejoicing\" in their new faith. The episode is one of the most vivid conversion accounts in Acts.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jailer"},
    "key_refs": ["Acts 16:27", "Acts 16:30", "Acts 16:33"]
},
"jair": {
    "term": "Jair",
    "category": "people",
    "intro": "<p>Jair (meaning <em>he diffuses light; my light</em>) is the name of several men, the most notable being: (1.) The son of Segub and grandson of Hezron of Judah, who through his mother's family had connections to Manasseh. He conquered 23 cities in Gilead and named them \"Havoth-jair\" (\"villages of Jair,\" Num. 32:41; Deut. 3:14; 1 Chr. 2:22). (2.) Jair the Gileadite, the ninth judge of Israel, who judged Israel for 22 years and had 30 sons who rode 30 donkeys and held 30 cities in Gilead (also called Havoth-jair, Judg. 10:3–5). (3.) The father of Mordecai the cousin of Esther (Esth. 2:5). (4.) The father of Elhanan who slew Lahmi the brother of Goliath (1 Chr. 20:5). The name's use across multiple prominent figures reflects its continued popularity.</p>",
    "hitchcock_meaning": "my light; who diffuses light",
    "source_ids": {"easton": "jair"},
    "key_refs": ["Numbers 32:41", "Judges 10:3", "Esther 2:5"]
},
"jairus": {
    "term": "Jairus",
    "category": "people",
    "intro": "<p>Jairus was a ruler (<em>archisynagōgos</em>) of the synagogue at Capernaum whose only daughter, twelve years old, was dying. He fell at Jesus' feet and pleaded for her life, and Jesus went with him (Mark 5:22–24; Luke 8:41–42). While en route, the woman with the issue of blood was healed, and then messengers arrived from Jairus's house saying his daughter had died. Jesus said to Jairus, \"Fear not: believe only, and she shall be made whole\" (Luke 8:50). Taking Peter, James, and John, and the parents, Jesus went to the house, dismissed the mourners, took the girl by the hand, and said \"Talitha cumi\" (Mark 5:41) — \"Damsel, arise\" — and she rose immediately. It is one of three recorded resurrections by Jesus, alongside Lazarus and the widow's son at Nain.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jairus"},
    "key_refs": ["Mark 5:22", "Mark 5:41", "Luke 8:50"]
},
"jakeh": {
    "term": "Jakeh",
    "category": "names",
    "intro": "<p>Jakeh was the father of Agur, the author (or compiler) of the wisdom collection in Proverbs 30: \"The words of Agur the son of Jakeh, even the prophecy: the man spake unto Ithiel, even unto Ithiel and Ucal\" (Prov. 30:1). Nothing is known of Jakeh beyond this paternal identification. Some scholars have proposed that \"Agur the son of Jakeh\" is a symbolic name for Solomon or another Israelite sage, but the conventional reading treats Agur as a separate wisdom figure. The words of Proverbs 30 include memorable numerical proverbs and a humble confession of ignorance before the majesty of God.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jakeh"},
    "key_refs": ["Proverbs 30:1"]
},
"jakim": {
    "term": "Jakim",
    "category": "names",
    "intro": "<p>Jakim (meaning <em>rising; confirming; establishing</em>) is the name of two men. (1.) A son of Shimei, a Benjaminite (1 Chr. 8:19). (2.) The head of the twelfth course of priests in David's organization of temple worship (1 Chr. 24:12). As with many of the priestly names in Chronicles, Jakim appears only in the administrative lists and plays no further narrative role in the biblical text.</p>",
    "hitchcock_meaning": "rising; confirming; establishing",
    "source_ids": {"easton": "jakim"},
    "key_refs": ["1 Chronicles 24:12", "1 Chronicles 8:19"]
},
"jalon": {
    "term": "Jalon",
    "category": "names",
    "intro": "<p>Jalon (meaning <em>tarrying; murmuring</em>) was a son of Ezra of the tribe of Judah (1 Chr. 4:17), listed in the genealogical record of Caleb's descendants. He appears only in this genealogical table, alongside his brothers Jether and Mered (who married an Egyptian princess). No further details about Jalon's life or significance are preserved in the biblical text.</p>",
    "hitchcock_meaning": "tarrying; murmuring",
    "source_ids": {"easton": "jalon"},
    "key_refs": ["1 Chronicles 4:17"]
},
"jambres": {
    "term": "Jambres",
    "category": "names",
    "intro": "<p>Jambres was one of the Egyptian magicians who opposed Moses before Pharaoh (2 Tim. 3:8). He is named alongside Jannes: \"Now as Jannes and Jambres withstood Moses, so do these also resist the truth: men of corrupt minds, reprobate concerning the faith.\" Their names do not appear in the Exodus narrative itself but were preserved in Jewish oral tradition and apocryphal writings (including the <em>Damascus Document</em> and the <em>Targum of Pseudo-Jonathan</em> on Exodus 7:11). Paul invokes them as examples of false teachers who mimic true religion while opposing genuine faith — a pattern Paul sees repeating in the last days.</p>",
    "hitchcock_meaning": "poverty; bitter; a rebel",
    "source_ids": {"easton": "jambres"},
    "key_refs": ["2 Timothy 3:8", "Exodus 7:11"]
},
"james": {
    "term": "James",
    "category": "people",
    "intro": "<p>James (the English form of Jacob) is the name of several men in the New Testament. (1.) James the son of Zebedee and Salome, brother of John the apostle — one of Jesus' inner circle of three (with Peter and John) who witnessed the Transfiguration (Matt. 17:1), the raising of Jairus's daughter (Mark 5:37), and the Gethsemane agony (Matt. 26:37). He was the first of the apostles to be martyred, beheaded by Herod Agrippa I around 44 A.D. (Acts 12:2). (2.) James the son of Alphaeus, another of the Twelve, sometimes called \"James the Less\" (Mark 15:40). (3.) James the brother of the Lord (Matt. 13:55; Gal. 1:19) — skeptical during Jesus' ministry (John 7:5) but transformed by a post-resurrection appearance to him (1 Cor. 15:7) into the leader of the Jerusalem church (Acts 15:13; 21:18; Gal. 2:9, 12). He authored the Epistle of James and was martyred around 62 A.D.</p>",
    "hitchcock_meaning": "same as Jacob",
    "source_ids": {"easton": "james", "smith": "james", "isbe": "james"},
    "key_refs": ["Matthew 17:1", "Acts 12:2", "Galatians 1:19", "Acts 15:13"]
},
"james-epistle-of": {
    "term": "James, Epistle of",
    "category": "concepts",
    "intro": "<p>The Epistle of James is a New Testament letter addressed \"to the twelve tribes which are scattered abroad\" (James 1:1), written by James the brother of the Lord and leader of the Jerusalem church, probably before 62 A.D. when James was martyred. It is intensely practical — often compared to Proverbs — addressing the challenges of Christian living: trials and perseverance (1:2–12), hearing and doing the word (1:22–25), avoiding partiality toward the wealthy (2:1–13), the relationship of faith and works (2:14–26), control of the tongue (3:1–12), conflict and prayer (4–5). Its famous teaching that \"faith without works is dead\" (2:17, 26) has sometimes been read in tension with Paul's emphasis on faith alone, but the two apostles address different opponents: James counters cheap faith that produces no fruit; Paul counters works-righteousness that excludes grace. Martin Luther's doubts about its canonical status did not prevent its widespread reception in the church. It was among the later books to receive universal canonical recognition.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "james-epistle-of", "isbe": "james-epistle-of"},
    "key_refs": ["James 1:2", "James 2:17", "James 5:16", "Galatians 2:9"]
},
"jannes": {
    "term": "Jannes",
    "category": "names",
    "intro": "<p>Jannes was one of the Egyptian magicians who, along with Jambres, opposed Moses before Pharaoh (2 Tim. 3:8). Their names are not found in the Exodus narrative but appear in ancient Jewish traditions and apocryphal texts, including the Targum of Pseudo-Jonathan (Ex. 7:11) and the Damascus Document from Qumran. Paul invokes them in 2 Timothy 3 as prototypes of false teachers in the last days — men of corrupt minds who resist the truth as Jannes and Jambres resisted Moses. The tradition was apparently well-known enough that Paul could cite it without explanation.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jannes"},
    "key_refs": ["2 Timothy 3:8", "Exodus 7:11"]
},
"janoah": {
    "term": "Janoah",
    "category": "places",
    "intro": "<p>Janoah (meaning <em>resting; tarrying</em>) appears in two contexts. (1.) A city on the northern border of Ephraim (Josh. 16:6–7), usually identified with modern Yanun southeast of Nablus. (2.) A town in Naphtali captured by the Assyrian king Tiglath-pileser III (also called Pul) in his campaigns against Israel during the reign of Pekah king of Israel (2 Kings 15:29). The Assyrian conquest of these northern territories was the beginning of the end for the northern kingdom, which fell completely in 722 B.C.</p>",
    "hitchcock_meaning": "resting; tarrying",
    "source_ids": {"easton": "janoah"},
    "key_refs": ["Joshua 16:6", "2 Kings 15:29"]
},
"janum": {
    "term": "Janum",
    "category": "places",
    "intro": "<p>Janum (meaning <em>sleeping</em>) was a town in the hill country of Judah, listed among the cities allotted to Judah in Joshua 15:53. It appears in the group of towns in the southern Judean highlands district alongside Aphekah and Humtah. The site has not been positively identified with any known modern location. It plays no further role in the biblical narrative beyond this allotment list.</p>",
    "hitchcock_meaning": "sleeping",
    "source_ids": {"easton": "janum"},
    "key_refs": ["Joshua 15:53"]
},
"japheth": {
    "term": "Japheth",
    "category": "people",
    "intro": "<p>Japheth (meaning <em>wide spreading</em> or possibly <em>the beautiful</em>) was the eldest (or second, depending on interpretation) son of Noah who entered the ark with his wife and survived the flood (Gen. 5:32; 6:10; 7:13). After the flood, when Shem and Japheth honorably covered their drunken father's nakedness, Noah blessed Japheth: \"God shall enlarge Japheth, and he shall dwell in the tents of Shem; and Canaan shall be his servant\" (Gen. 9:27). His descendants — listed in Genesis 10:2–5 — are the nations of the north and west: Gomer (Cimmerians), Magog, Madai (Medes), Javan (Greeks/Ionians), Tubal, Meshech, and Tiras. These became the peoples of Asia Minor, the Aegean, and Europe. The \"enlargement of Japheth\" was interpreted by many church fathers as prophesying the expansion of Gentile peoples into the covenant blessings of Shem (Israel).</p>",
    "hitchcock_meaning": "wide spreading",
    "source_ids": {"easton": "japheth", "smith": "japheth"},
    "key_refs": ["Genesis 9:27", "Genesis 10:2", "Genesis 5:32"]
},
"japhia": {
    "term": "Japhia",
    "category": "names",
    "intro": "<p>Japhia (meaning <em>enlightening; appearing</em>) is the name of two men and one place. (1.) The king of Lachish who joined the Amorite coalition against Gibeon and was defeated and killed by Joshua at the battle of Aijalon (Josh. 10:3, 26). (2.) One of David's sons born at Jerusalem (2 Sam. 5:15; 1 Chr. 3:7; 14:6). (3.) A border town on the southern boundary of Zebulun (Josh. 19:12), identified with modern Yafa, a village near Nazareth. The name's use for both a person and place is common in biblical Hebrew.</p>",
    "hitchcock_meaning": "enlightening; appearing",
    "source_ids": {"easton": "japhia"},
    "key_refs": ["Joshua 10:3", "2 Samuel 5:15", "Joshua 19:12"]
},
"japho": {
    "term": "Japho",
    "category": "places",
    "intro": "<p>Japho (Hebrew form of Joppa; meaning <em>fairness; comeliness</em>) was the ancient seaport on the Mediterranean coast of Israel assigned to the tribe of Dan (Josh. 19:46). It is the modern city of Jaffa, now incorporated into Tel Aviv. It was the port through which the cedars of Lebanon for Solomon's temple were floated as rafts and received (2 Chr. 2:16; Ezra 3:7). Jonah embarked from Joppa on his ill-fated voyage to Tarshish (Jon. 1:3). In the New Testament, the apostle Peter raised Tabitha (Dorcas) from the dead at Joppa (Acts 9:36–42) and received his vision of the great sheet on a rooftop there (Acts 10:9–16), leading to the conversion of Cornelius.</p>",
    "hitchcock_meaning": "fairness; comeliness",
    "source_ids": {"easton": "japho"},
    "key_refs": ["Joshua 19:46", "Jonah 1:3", "Acts 9:36", "Acts 10:9"]
},
"jared": {
    "term": "Jared",
    "category": "names",
    "intro": "<p>Jared (meaning <em>descent; a ruling; commanding</em>) was the fifth antediluvian patriarch in the line from Seth to Noah — the son of Mahalaleel and father of Enoch (Gen. 5:15–20; 1 Chr. 1:2; Luke 3:37). He lived 962 years, the second-longest lifespan recorded in Scripture after Methuselah. At age 162 he became the father of Enoch, who \"walked with God\" and was taken without dying (Gen. 5:21–24). Jared appears in Luke's genealogy of Jesus in the line from Adam to Christ. In the extra-biblical book of 1 Enoch, Jared is associated with the coming of the Watchers (fallen angels) to earth — a tradition not found in Scripture.</p>",
    "hitchcock_meaning": "a ruling; commanding; coming down",
    "source_ids": {"easton": "jared"},
    "key_refs": ["Genesis 5:15", "Luke 3:37"]
},
"jarib": {
    "term": "Jarib",
    "category": "names",
    "intro": "<p>Jarib (meaning <em>fighting; chiding; multiplying; avenging</em>) is the name of three men. (1.) A son of Simeon (1 Chr. 4:24), also called Jachin (Gen. 46:10; Ex. 6:15). (2.) One of the leaders Ezra sent to Casiphia to obtain Levites for the return from Babylonian exile (Ezra 8:16). (3.) One of the priests who had married foreign wives and agreed to put them away at Ezra's reform (Ezra 10:18). The name appears in a range of historical contexts across the Persian-period restoration community.</p>",
    "hitchcock_meaning": "fighting; chiding; multiplying; avenging",
    "source_ids": {"easton": "jarib"},
    "key_refs": ["1 Chronicles 4:24", "Ezra 8:16", "Ezra 10:18"]
},
"jarmuth": {
    "term": "Jarmuth",
    "category": "places",
    "intro": "<p>Jarmuth (meaning <em>height; fearing death</em>) was an important Canaanite city in the Shephelah of Judah whose king Piram joined the Amorite coalition against Gibeon after Israel's treaty with the Gibeonites. Joshua defeated this coalition at Aijalon (Josh. 10:3–5, 23) and the king of Jarmuth was executed (Josh. 10:26). The city was assigned to Judah (Josh. 15:35) and resettled by Jews after the exile (Neh. 11:29). It is identified with modern Khirbet Yarmuk. Jarmuth was also a Levitical city in Issachar (Josh. 21:29), called Remeth in Joshua 19:21.</p>",
    "hitchcock_meaning": "fearing, or seeing, or throwing down, death",
    "source_ids": {"easton": "jarmuth"},
    "key_refs": ["Joshua 10:3", "Joshua 15:35", "Nehemiah 11:29"]
},
"jashen": {
    "term": "Jashen",
    "category": "names",
    "intro": "<p>Jashen was the father of several members of David's elite corps of mighty men (2 Sam. 23:32): \"the sons of Jashen, Jonathan.\" The parallel text in 1 Chronicles 11:34 reads \"the sons of Hashem the Gizonite,\" suggesting Jashen and Hashem may be variant forms of the same name, or that the text has been abbreviated. Whether Jashen himself was a warrior or simply the patriarch of a warrior family is unclear from the text.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jashen"},
    "key_refs": ["2 Samuel 23:32"]
},
"jasher": {
    "term": "Jasher",
    "category": "concepts",
    "intro": "<p>The Book of Jasher (Hebrew <em>sēfer hayy<em>āsh</em>ār</em>, \"Book of the Upright\" or \"Book of the Just\") was an ancient Israelite collection of poetry or heroic song, cited twice in the Old Testament. Joshua 10:13 quotes from it the poetic command for the sun and moon to stand still at Aijalon. Second Samuel 1:18 directs that the lament of David over Saul and Jonathan (\"the song of the bow\") be taught to the children of Judah, and that it is written in the Book of Jasher. The book is not otherwise preserved; various later works claiming this title are medieval forgeries. The LXX renders \"the Book of the Upright One,\" suggesting a collection of noble deeds and patriotic poetry analogous to other lost national song-books of the ancient world.</p>",
    "hitchcock_meaning": "righteous; upright",
    "source_ids": {"easton": "jasher"},
    "key_refs": ["Joshua 10:13", "2 Samuel 1:18"]
},
"jashobeam": {
    "term": "Jashobeam",
    "category": "people",
    "intro": "<p>Jashobeam (meaning <em>the people sitting; or to whom the people return</em>) the Hachmonite was chief of David's three most elite warriors and first of his mighty men (1 Chr. 11:11). He lifted his spear against 300 men at one time and killed them. The parallel text in 2 Samuel 23:8 calls him Adino the Eznite and credits him with slaying 800 at one time. He also commanded the first monthly division of David's army (1 Chr. 27:2) and was one of the men from the tribes of Manasseh who deserted Saul and joined David at Ziklag (1 Chr. 12:6). He represents the pinnacle of individual military heroism in David's service.</p>",
    "hitchcock_meaning": "the people sitting; or captivity of the people",
    "source_ids": {"easton": "jashobeam"},
    "key_refs": ["1 Chronicles 11:11", "1 Chronicles 27:2"]
},
"jashub": {
    "term": "Jashub",
    "category": "names",
    "intro": "<p>Jashub (meaning <em>a returning; a controversy; a dwelling place</em>) is the name of three men. (1.) The third son of Issachar (Num. 26:24; 1 Chr. 7:1), called Job in Genesis 46:13, and ancestor of the Jashubite clan. (2.) One of the sons of Bani who agreed to put away their foreign wives at Ezra's reform (Ezra 10:29). (3.) Jashub-lehem is also mentioned as a descendant of Shelah in 1 Chronicles 4:22, though this may be a place name rather than a personal name.</p>",
    "hitchcock_meaning": "a returning; a controversy; a dwelling place",
    "source_ids": {"easton": "jashub"},
    "key_refs": ["Numbers 26:24", "Ezra 10:29"]
},
"jason": {
    "term": "Jason",
    "category": "people",
    "intro": "<p>Jason (meaning <em>he that cures</em>) was a Jewish Christian of Thessalonica who provided hospitality to Paul and Silas during their mission there (Acts 17:5–9). When the Thessalonian Jews incited a mob and assaulted his house looking for Paul and Silas, they dragged Jason and some other believers before the city rulers, accusing them of harboring men who \"have turned the world upside down\" and of acting contrary to Caesar's decrees by saying Jesus is king. Jason gave security and was released. He may be the same Jason Paul calls his \"kinsman\" (fellow Jew) who sends greetings in Romans 16:21.</p>",
    "hitchcock_meaning": "he that cures",
    "source_ids": {"easton": "jason"},
    "key_refs": ["Acts 17:5", "Acts 17:9", "Romans 16:21"]
},
"jasper": {
    "term": "Jasper",
    "category": "concepts",
    "intro": "<p>Jasper (Hebrew <em>yashpheh</em>; Greek <em>iaspis</em>) is a precious stone appearing in the high priest's breastplate (Ex. 28:20; 39:13) and in the eschatological visions of Scripture. Ancient jasper was probably not the opaque stone known today by that name but a translucent gem of various colors — perhaps a form of chalcedony or green quartz. In Revelation, the glory of God shines \"like a jasper stone, clear as crystal\" (Rev. 4:3; 21:11), and the first foundation of the New Jerusalem's wall is jasper (Rev. 21:18–19). The wall of the New Jerusalem itself is built of jasper. Its use to describe divine radiance suggests it was prized for brilliance and clarity.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jasper"},
    "key_refs": ["Exodus 28:20", "Revelation 4:3", "Revelation 21:18"]
},
"jattir": {
    "term": "Jattir",
    "category": "places",
    "intro": "<p>Jattir was a city in the hill country of Judah listed among the cities given to Judah in Joshua's allotment (Josh. 15:48) and designated a Levitical city given to the sons of Aaron the priest (Josh. 21:14; 1 Chr. 6:57). After his victory over the Amalekites, David sent a portion of the spoils to the elders of Jattir among the various towns that had sheltered him during his outlaw years (1 Sam. 30:27). It is generally identified with Khirbet Attir in the southern Judean highlands.</p>",
    "hitchcock_meaning": "a remnant; excellent",
    "source_ids": {"easton": "jattir"},
    "key_refs": ["Joshua 15:48", "Joshua 21:14", "1 Samuel 30:27"]
},
"javan": {
    "term": "Javan",
    "category": "people",
    "intro": "<p>Javan (meaning <em>deceiver; one who makes sad</em>) was the fourth son of Japheth and grandson of Noah (Gen. 10:2; 1 Chr. 1:5), whose descendants settled in Greece — specifically Ionia (the western coast of Asia Minor and the Aegean islands). In Hebrew, Greece is consistently called <em>Yāwān</em> (Javan), reflecting the connection between the name and the Ionians who were among the earliest and most prominent Greeks known to the ancient Near East. Daniel's vision of the swift goat conquering the ram refers to the Greek king (<em>melek Yāwān</em>, Dan. 8:21; 10:20; 11:2). Zechariah 9:13 speaks of God raising Judah against Greece. Ezekiel lists Javan among Tyre's trading partners (Ezek. 27:13, 19). The sons of Javan — Elishah, Tarshish, Kittim, and Dodanim — represent the various Greek and island peoples (Gen. 10:4).</p>",
    "hitchcock_meaning": "deceiver; one who makes sad",
    "source_ids": {"easton": "javan"},
    "key_refs": ["Genesis 10:2", "Daniel 8:21", "Zechariah 9:13"]
},
"javelin": {
    "term": "Javelin",
    "category": "concepts",
    "intro": "<p>A javelin was a light throwing spear used in ancient warfare. In Scripture it appears most memorably in the hands of King Saul, who twice hurled his javelin at David as he played the harp (1 Sam. 18:10–11; 19:9–10) and once at his own son Jonathan (1 Sam. 20:33). Phinehas used a javelin (Hebrew <em>rōmaḥ</em>) to execute Zimri and Cozbi in their act of brazen idolatry (Num. 25:7–8), an act of priestly zeal that God credited to him for righteousness. Goliath is described as carrying a bronze javelin slung between his shoulders (1 Sam. 17:6). The javelin illustrates several different themes: royal rage, priestly zeal, and martial power.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "javelin"},
    "key_refs": ["1 Samuel 18:10", "Numbers 25:7", "1 Samuel 17:6"]
},
"jaw-bone": {
    "term": "Jaw-bone",
    "category": "concepts",
    "intro": "<p>The jaw-bone of an ass was the improvised weapon with which Samson slew a thousand Philistines at Lehi (Judg. 15:15–17). After the Philistines bound him and delivered him over, the Spirit of the LORD came upon Samson, the ropes burst, and he seized a fresh jaw-bone and struck down a thousand men. He then composed a brief battle poem: \"With the jaw-bone of an ass, heaps upon heaps, with the jaw of an ass have I slain a thousand men.\" The place was called Ramath-lehi (\"the hill of the jaw-bone\") in commemoration. Immediately after the battle, dying of thirst, Samson cried to God and water miraculously came from a hollow in Lehi. The episode illustrates Samson's pattern of supernatural strength combined with personal vulnerability.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jaw-bone"},
    "key_refs": ["Judges 15:15", "Judges 15:17"]
},
"jealousy": {
    "term": "Jealousy",
    "category": "concepts",
    "intro": "<p>Jealousy in Scripture encompasses both human and divine dimensions. In human experience, sexual jealousy — suspicion of a spouse's fidelity — is described as one of the most powerful and consuming passions (Prov. 6:34; Song 8:6; Num. 5:14). The \"jealousy offering\" of Numbers 5 provided a judicial process for resolving accusations of adultery. The \"image of jealousy\" in Ezekiel 8:3–5 refers to an idol that provoked God's jealousy by claiming what belonged to him alone. Most significantly, Scripture describes God himself as \"jealous\" (<em>qannāʾ</em>): \"for I the LORD thy God am a jealous God\" (Ex. 20:5; 34:14). Divine jealousy is not a petty emotion but the passionate protection of an exclusive covenant relationship — God's insistence that Israel worship him alone, which is the proper response to his nature and his saving acts. Paul speaks of a \"godly jealousy\" with which he guards the Corinthians' singular devotion to Christ (2 Cor. 11:2).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jealousy"},
    "key_refs": ["Exodus 20:5", "Numbers 5:14", "Song of Solomon 8:6", "2 Corinthians 11:2"]
},
"jealousy-offering": {
    "term": "Jealousy Offering",
    "category": "concepts",
    "intro": "<p>The jealousy offering (Hebrew <em>minḥat qĕnā'ōt</em>) was the grain offering a husband brought to the tabernacle when he suspected his wife of adultery but had no witnesses (Num. 5:11–31). Made of barley meal without oil or frankincense (unlike regular grain offerings), it was called a \"memorial\" offering that would \"bring iniquity to remembrance.\" The accused woman was brought before the priest, who made her drink the \"bitter water\" — water mixed with dust from the tabernacle floor — with a pronounced curse. If guilty, she would suffer physical consequences; if innocent, she would be unharmed and cleared. The ritual served as a divinely guaranteed ordeal that protected both the accused innocent wife and the integrity of the covenant community. The emphasis on God as the judge reflects the limitation of human judicial process where no human witness was available.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jealousy-offering"},
    "key_refs": ["Numbers 5:15", "Numbers 5:18", "Numbers 5:27"]
},
"jealousy-image-of": {
    "term": "Jealousy, Image of",
    "category": "concepts",
    "intro": "<p>The \"image of jealousy\" was an idolatrous object seen by the prophet Ezekiel in his vision of the abominations being practiced in the Jerusalem temple (Ezek. 8:3–5). He was taken in vision to the north gate of the inner court where he saw this image standing in the entrance — an idol provoking God's jealous response because it claimed the worship that belonged to God alone in his own sanctuary. The image may have been an Asherah pole or a statue of a foreign deity installed by the apostate priests of Ezekiel's day. The vision of this image was the first of four escalating abominations Ezekiel saw in the temple precincts (Ezek. 8:5–16), culminating in the departure of the divine Glory from the temple (Ezek. 10–11).</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jealousy-image-of"},
    "key_refs": ["Ezekiel 8:3", "Ezekiel 8:5", "2 Kings 21:7"]
},
"jealousy-waters-of": {
    "term": "Jealousy, Waters of",
    "category": "concepts",
    "intro": "<p>The waters of jealousy (or \"bitter water\") were the ceremonial drink prescribed in Numbers 5:17–27 for the ordeal of a woman accused of adultery by her jealous husband but without witnesses. The priest took holy water in an earthen vessel, mixed it with dust from the tabernacle floor, wrote the curses on a scroll and washed the ink into the water, then made the woman drink it. The Hebrew phrase <em>mê hammārîm</em> means \"bitter waters\" or \"waters of testing.\" If the woman was guilty, the water would cause physical harm; if innocent, she would be unharmed. The ritual served as a divinely supervised legal mechanism ensuring that neither innocent women nor the covenant community would suffer injustice when human evidence was unavailable.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jealousy-waters-of"},
    "key_refs": ["Numbers 5:17", "Numbers 5:24", "Numbers 5:27"]
},
"jearim": {
    "term": "Jearim",
    "category": "places",
    "intro": "<p>Jearim (meaning <em>a leap; woods; forests</em>) appears in the phrase \"Mount Jearim\" or \"Chesalon\" — a mountain on the northern border of Judah (Josh. 15:10). The same mountain is also called Chesalon. Kiriath-jearim (\"city of forests\") is a more prominent location with the same root name, a Gibeonite city where the ark of the covenant rested for twenty years after being returned from the Philistines until David brought it to Jerusalem (1 Sam. 7:1–2; 2 Sam. 6:2; Ps. 132:6). The ark's time at Kiriath-jearim was the formative period of Samuel's ministry and the transition to the monarchy.</p>",
    "hitchcock_meaning": "a leap; woods",
    "source_ids": {"easton": "jearim"},
    "key_refs": ["Joshua 15:10", "1 Samuel 7:1", "Psalms 132:6"]
},
"jebus": {
    "term": "Jebus",
    "category": "places",
    "intro": "<p>Jebus (meaning <em>treading under foot; manger</em>) was the Canaanite name for the city later known as Jerusalem, inhabited by the Jebusites (Josh. 15:8; 18:16, 28; Judg. 19:10–11; 1 Chr. 11:4–5). Despite being assigned to Benjamin (Josh. 18:28), the Israelites failed to conquer it after the initial campaigns. It remained a Jebusite stronghold throughout the period of the judges. When David became king over all Israel, he captured \"the stronghold of Zion\" — the fortress of Jebus — which the Jebusites boasted even the lame and blind could defend (2 Sam. 5:6–9; 1 Chr. 11:4–8), and he renamed it the City of David. Jerusalem's pre-Israelite name Jebus is a reminder that the most sacred city of Israel was originally a foreign stronghold transformed by divine purpose.</p>",
    "hitchcock_meaning": "treading under foot; manger",
    "source_ids": {"easton": "jebus"},
    "key_refs": ["Joshua 15:8", "2 Samuel 5:6", "1 Chronicles 11:4"]
},
"jebusites": {
    "term": "Jebusites",
    "category": "people",
    "intro": "<p>The Jebusites were the Canaanite inhabitants of Jebus (later Jerusalem), descended from Canaan son of Ham (Gen. 10:16; 15:21). They appear consistently in the lists of nations to be dispossessed from the land (Ex. 3:8, 17; Deut. 7:1; Josh. 3:10). Despite being in the territory allotted to Benjamin and Judah, neither tribe fully dislodged them (Josh. 15:63; Judg. 1:21), and the Jebusites held their stronghold on the hill of Zion until David's capture of the city. Araunah (or Ornan) the Jebusite owned the threshing floor David purchased to build an altar where the destroying angel stopped (2 Sam. 24:16–24; 1 Chr. 21:18–26) — the site that became the location of Solomon's temple. The peaceful integration of some Jebusites into Israel (Zech. 9:7 may allude to this) stands alongside the general dispossession of Canaanite peoples.</p>",
    "hitchcock_meaning": None,
    "source_ids": {"easton": "jebusites", "smith": "jebusites"},
    "key_refs": ["Genesis 10:16", "Joshua 15:63", "2 Samuel 5:6", "2 Samuel 24:18"]
},
"jecoliah": {
    "term": "Jecoliah",
    "category": "names",
    "intro": "<p>Jecoliah (also spelled Jecholiah; meaning <em>perfection or power of the LORD</em>) was the wife of King Amaziah of Judah and mother of King Uzziah (also called Azariah), who reigned for 52 years and was one of Judah's most prosperous kings (2 Kings 15:2; 2 Chr. 26:3). She was from Jerusalem. Her name, along with those of other queens mother in the Kings formula, represents the Deuteronomistic historian's practice of recording maternal lineage as part of the royal evaluation formula for each Judean king.</p>",
    "hitchcock_meaning": "perfection, or power, of the Lord",
    "source_ids": {"easton": "jecoliah"},
    "key_refs": ["2 Kings 15:2", "2 Chronicles 26:3"]
},
"jedaiah": {
    "term": "Jedaiah",
    "category": "names",
    "intro": "<p>Jedaiah (meaning <em>the hand of the LORD; confessing the LORD</em>) is the name of several men. (1.) A Simeonite chief (1 Chr. 4:37). (2.) A priest who helped repair the Jerusalem wall (Neh. 3:10). (3.) The head of the second course of priests in David's organization (1 Chr. 24:7) — one of the most important priestly families, as this family was specifically named by Zerubbabel's administration when the temple service was restored (Ezra 2:36; Neh. 7:39; 1 Chr. 9:10). (4.) A priest who returned from Babylon with Zerubbabel (Neh. 12:6, 19). (5.) One of those who brought offerings of gold and silver from Babylon for the temple (Zech. 6:10, 14). The multiple uses reflect the name's popularity in priestly circles.</p>",
    "hitchcock_meaning": "the hand of the Lord; confessing the Lord",
    "source_ids": {"easton": "jedaiah"},
    "key_refs": ["1 Chronicles 24:7", "Ezra 2:36", "Zechariah 6:10"]
},
"jediael": {
    "term": "Jediael",
    "category": "names",
    "intro": "<p>Jediael (meaning <em>the science or knowledge of God</em>) is the name of three men in the Old Testament. (1.) A son of Benjamin (1 Chr. 7:6, 10–11) whose family was reckoned among the mighty men of valor. (2.) A Manassehite warrior who deserted Saul and joined David at Ziklag (1 Chr. 12:20). (3.) A son of Shimri, one of David's mighty men (1 Chr. 11:45). The name reflects a theological conviction that true knowledge — the kind that matters — is knowledge of God, a theme common in biblical wisdom and covenant literature.</p>",
    "hitchcock_meaning": "the science, or knowledge, of God",
    "source_ids": {"easton": "jediael"},
    "key_refs": ["1 Chronicles 7:6", "1 Chronicles 12:20", "1 Chronicles 11:45"]
},
}

wrote = 0
skipped = 0
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
        wrote += 1
    else:
        skipped += 1

print(f"BP j1: Jaakan → Jediael: wrote {wrote}, skipped {skipped} existing.")
