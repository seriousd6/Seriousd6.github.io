#!/usr/bin/env python3
import json, os

OUT_DIR = '../data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def merge_article(slug, data):
    path = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

ARTICLES = {
"zibiah": {
  "id": "zibiah",
  "term": "Zibiah",
  "category": "people",
  "intro": "<p>Zibiah (meaning: <em>deer; goat</em>) was a woman of Beer-sheba and the mother of Joash king of Judah. She is mentioned in <strong>2 Kings 12:1</strong> and <strong>2 Chronicles 24:1</strong>, both of which note that Joash began to reign when he was seven years old and that his mother's name was Zibiah of Beer-sheba. Beyond her name and hometown, nothing further is recorded of her in Scripture.</p><p>Her son Joash (also called Jehoash) was hidden in the temple for six years while Athaliah usurped the throne; when he was brought out and crowned, the faithful priest Jehoiada guided the early years of his reign, during which the temple was repaired.</p>",
  "sections": [],
  "hitchcock_meaning": "the Lord dwells; deer; goat",
  "source_ids": ["easton"],
  "key_refs": ["2 Kings 12:1", "2 Chronicles 24:1"]
},

"zichri": {
  "id": "zichri",
  "term": "Zichri",
  "category": "people",
  "intro": "<p>Zichri (meaning: <em>that remembers; that is a man</em>) is the name of several men in the Old Testament, mostly Benjamites and Levites. (1.) A chief of Benjamin (<strong>1 Chr. 8:19</strong>). (2.) Another Benjamite chief of the same chapter (<strong>1 Chr. 8:23</strong>). Further bearers of the name appear in 1 Chronicles 9:15 (a Levite ancestor of temple musicians), 26:25 (a Levite over the Reubenite treasuries), and 27:16 (father of the officer over Reuben). In <strong>2 Chronicles 17:16</strong> Zichri is the father of Amasiah, a volunteer warrior under Jehoshaphat; in <strong>28:7</strong> a mighty man of Ephraim named Zichri slew three of Ahaz's chief officers.</p><p>The name was evidently common in Israel across several centuries and appears among both priestly and military families. Smith and Easton list the first two Benjamite occurrences as the primary entries.</p>",
  "sections": [],
  "hitchcock_meaning": "that remembers; that is a man",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Chronicles 8:19", "1 Chronicles 8:23", "2 Chronicles 17:16", "2 Chronicles 28:7"]
},

"ziddim": {
  "id": "ziddim",
  "term": "Ziddim",
  "category": "places",
  "intro": "<p>Ziddim (meaning: <em>huntings; treasons; destructions</em>) was a fortified city in the tribal territory of Naphtali, listed among the towns allotted to that tribe in <strong>Joshua 19:35</strong>. Easton's dictionary tentatively identifies it with Kefr-Hattin — the \"village of the Hittites\" — located approximately five miles west of Tiberias on the western ridge overlooking the Sea of Galilee.</p><p>The site lies in the fertile lower Galilee region. Beyond the single reference in Joshua's allotment list, Ziddim appears nowhere else in Scripture, and its identification with Kefr-Hattin remains uncertain. The area around Tiberias was heavily settled in the Old Testament period as part of the heartland of Naphtali.</p>",
  "sections": [],
  "hitchcock_meaning": "huntings; treasons; destructions",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 19:35"]
},

"zidkijah": {
  "id": "zidkijah",
  "term": "Zidkijah",
  "category": "people",
  "intro": "<p>Zidkijah (meaning: <em>justice of the Lord</em>) is listed among those who sealed the covenant renewal under Nehemiah recorded in <strong>Nehemiah 10:1</strong>. He appears first on the list of signatories, after Nehemiah the governor himself, suggesting a position of some prominence among the priests or leaders of restored Jerusalem. No further biographical details are given.</p><p>The name is a variant form of Zedekiah and shares its theological declaration that the LORD is righteousness. The covenant sealed in Nehemiah 10 bound the returnees to keep the law of Moses, to avoid intermarriage with surrounding peoples, to observe the sabbath, to forgo the seventh-year harvest, and to maintain the temple and its offerings.</p>",
  "sections": [],
  "hitchcock_meaning": "justice of the Lord",
  "source_ids": ["easton"],
  "key_refs": ["Nehemiah 10:1"]
},

"zidon": {
  "id": "zidon",
  "term": "Zidon",
  "category": "places",
  "intro": "<p>Zidon (meaning: <em>hunting; fishing; venison</em>) — also spelled Sidon — was an ancient Phoenician city on the Mediterranean coast approximately 25 miles north of Tyre. It received its name from Sidon, the \"first-born\" of Canaan and grandson of Noah (<strong>Gen. 10:15</strong>, <strong>19</strong>), and was the oldest and at one time the greatest of the Phoenician cities. It served as the mother city of Tyre and carried on extensive maritime commerce. The territory of Zidon was assigned to the tribe of Asher (<strong>Josh. 19:28</strong>), but Israel never subdued it (<strong>Judg. 1:31</strong>).</p><p>The Zidonians periodically oppressed Israel (Judg. 10:12), and Solomon married Zidonian women who led him into the worship of Ashtoreth (<strong>1 Kings 11:1, 33</strong>). The prophets Isaiah, Jeremiah, and Ezekiel all pronounced oracles against Zidon (<strong>Isa. 23:2–12</strong>; <strong>Jer. 47:4</strong>; <strong>Ezek. 28:21–22</strong>). Jesus visited the region of Tyre and Sidon (<strong>Matt. 15:21</strong>; <strong>Mark 7:24</strong>), and people from there came to hear him (<strong>Luke 6:17</strong>). Paul stopped at Sidon on his voyage to Rome (<strong>Acts 27:3</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "hunting; fishing; venison",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 10:15", "1 Kings 11:1", "Matthew 15:21", "Acts 27:3"]
},

"zif": {
  "id": "zif",
  "term": "Zif",
  "category": "concepts",
  "intro": "<p>Zif (meaning: <em>brightness; comeliness</em>) was the ancient Hebrew name for the second month of the sacred calendar, called Iyar by the Jews of the post-exilic period. It corresponded roughly to April–May in the modern calendar. The name appears only twice in Scripture, both times in connection with Solomon's temple: <strong>1 Kings 6:1</strong> records that Solomon began building the temple \"in the month Zif, which is the second month,\" and <strong>1 Kings 6:37</strong> notes that the foundation was laid in the month of Zif.</p><p>The month of Zif falls in the spring, after Abib/Nisan (the Passover month), when the land of Israel is in full bloom — consistent with the meaning \"brightness\" or \"the flower month.\" After the Babylonian exile, Hebrew months were increasingly referred to by Babylonian names, and Zif gave way to Iyar in common usage.</p>",
  "sections": [],
  "hitchcock_meaning": "this or that; brightness; comeliness",
  "source_ids": ["easton"],
  "key_refs": ["1 Kings 6:1", "1 Kings 6:37"]
},

"ziha": {
  "id": "ziha",
  "term": "Ziha",
  "category": "people",
  "intro": "<p>Ziha (meaning: <em>brightness; whiteness; drought</em>) is the name of two men in the books of Ezra and Nehemiah. (1.) The head of a family of Nethinim (temple servants) who returned from Babylonian exile with Zerubbabel (<strong>Ezra 2:43</strong>; <strong>Neh. 7:46</strong>). (2.) A ruler or overseer among the Nethinim in Jerusalem after the return (<strong>Neh. 11:21</strong>).</p><p>The Nethinim were a class of temple servants assigned to assist the Levites in the lower duties of the sanctuary. They were numerous enough to appear in the return lists under their clan heads, and Ziha evidently represented a significant family group among them. Whether the two men named Ziha are related or the same individual at different points in his life cannot be determined from the text.</p>",
  "sections": [],
  "hitchcock_meaning": "brightness; whiteness; drought",
  "source_ids": ["easton"],
  "key_refs": ["Ezra 2:43", "Nehemiah 7:46", "Nehemiah 11:21"]
},

"ziklag": {
  "id": "ziklag",
  "term": "Ziklag",
  "category": "places",
  "intro": "<p>Ziklag was a town in the Negeb, the dry south country of Judah, first mentioned in the allotment list of Joshua (<strong>Josh. 15:31</strong>) and reassigned to the tribe of Simeon (<strong>Josh. 19:5</strong>). By the time of David's flight from Saul it was under Philistine control. When David went to Gath and presented himself to Achish the king, Achish granted him Ziklag as a place of residence (<strong>1 Sam. 27:6</strong>). David dwelt there for a year and four months, raiding the Geshurites and others while misleading Achish into thinking he was attacking Judah.</p><p>During David's absence with the Philistine army for the campaign that ended at Jezreel, the Amalekites raided and burned Ziklag, taking its inhabitants captive. David pursued them and recovered all the people and plunder (<strong>1 Sam. 30</strong>). It was at Ziklag that David received news of Saul's death (<strong>2 Sam. 1:1</strong>). From this time forward the city \"pertained to the kings of Judah\" (1 Sam. 27:6). It was resettled after the return from exile (<strong>Neh. 11:28</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "measure pressed down",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Samuel 27:6", "1 Samuel 30:1", "2 Samuel 1:1", "Joshua 15:31"]
},

"zillah": {
  "id": "zillah",
  "term": "Zillah",
  "category": "people",
  "intro": "<p>Zillah (meaning: <em>shadow; the tingling of the ear</em>) was one of the two wives of Lamech, a descendant of Cain in the antediluvian genealogy of <strong>Genesis 4:19–22</strong>. By Lamech she bore Tubal-cain, the forger of cutting instruments of bronze and iron, and his sister Naamah. Zillah's co-wife was Adah, mother of Jabal and Jubal.</p><p>Lamech's address to his wives in <strong>Genesis 4:23–24</strong> — the \"Song of the Sword\" — is the earliest recorded poem in Scripture and reflects a boast of vengeance far exceeding the divine protection granted to Cain. Zillah and Adah are thus witnesses to the culture of violence and craft that characterized the line of Cain before the flood.</p>",
  "sections": [],
  "hitchcock_meaning": "shadow; the tingling of the ear",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 4:19", "Genesis 4:22", "Genesis 4:23"]
},

"zilpah": {
  "id": "zilpah",
  "term": "Zilpah",
  "category": "people",
  "intro": "<p>Zilpah (meaning: <em>distillation from the mouth</em>) was the maidservant given to Leah by her father Laban, and subsequently given by Leah to Jacob as a secondary wife (<strong>Gen. 30:9–13</strong>). By Jacob, Zilpah bore two sons: Gad and Asher. Gad's name commemorated the good fortune Leah perceived in his birth; Asher's name expressed Leah's happiness. Both became heads of tribes in Israel.</p><p>Like Bilhah (Rachel's maidservant), Zilpah's sons were reckoned as fully tribal sons of Jacob and listed among the twelve tribes. Zilpah is mentioned in the genealogical summary of <strong>Genesis 35:26</strong> and in the roster of those who went down to Egypt with Jacob (<strong>Gen. 46:18</strong>), where her four grandsons are also listed.</p>",
  "sections": [],
  "hitchcock_meaning": "distillation from the mouth",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 30:9", "Genesis 35:26", "Genesis 46:18"]
},

"zilthai": {
  "id": "zilthai",
  "term": "Zilthai",
  "category": "people",
  "intro": "<p>Zilthai (meaning: <em>my shadow; my talk</em> — understood as \"protection of Jehovah\") is the name of two men in the Davidic-era records of Chronicles. (1.) A chief of the tribe of Benjamin (<strong>1 Chr. 8:20</strong>), listed among the sons of Shimhi. (2.) One of the captains of Manasseh who defected to David at Ziklag before the battle with the Philistines at Jezreel (<strong>1 Chr. 12:20</strong>); these Manassite officers brought military strength to David's cause at a critical moment.</p><p>No further biographical details are given for either man. The name appears in two distinct contexts — tribal genealogy and military allegiance — suggesting it was used across different families and periods within Israel.</p>",
  "sections": [],
  "hitchcock_meaning": "my shadow; my talk",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 8:20", "1 Chronicles 12:20"]
},

"zimmah": {
  "id": "zimmah",
  "term": "Zimmah",
  "category": "people",
  "intro": "<p>Zimmah (meaning: <em>thought; wickedness</em>) is the name of several Gershonite Levites in the genealogies of Chronicles. (1.) A Gershonite Levite in the lineage recorded in <strong>1 Chronicles 6:20</strong>. (2.) Another Gershonite Levite appearing in a parallel genealogy at <strong>1 Chronicles 6:42</strong>. (3.) The father of Joah, who was one of the Levites who assisted Hezekiah in the cleansing of the temple (<strong>2 Chr. 29:12</strong>).</p><p>The presence of the same name at several points in the Gershonite lineage is consistent with the pattern of reusing ancestral names across generations. The Joah son of Zimmah who served under Hezekiah represents the family's continued Levitical service in the era of temple reform.</p>",
  "sections": [],
  "hitchcock_meaning": "thought; wickedness",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 6:20", "1 Chronicles 6:42", "2 Chronicles 29:12"]
},

"zimran": {
  "id": "zimran",
  "term": "Zimran",
  "category": "people",
  "intro": "<p>Zimran (meaning: <em>song; singer; vine</em>) was the first-named of the six sons born to Abraham by Keturah, his wife after the death of Sarah (<strong>Gen. 25:2</strong>; <strong>1 Chr. 1:32</strong>). The six sons — Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah — became ancestors of Arab peoples of the eastern and southern regions. Abraham sent them eastward with gifts, away from Isaac, before his death.</p><p>Zimran's descendants are not further identified in Scripture. Some early commentators connected the name with a region or people in northwestern Arabia, but the identification is uncertain. Zimran stands at the head of the Keturite line, distinct from both the Ishmaelie and the Ishmaelite genealogies, representing another strand of Abrahamic descent.</p>",
  "sections": [],
  "hitchcock_meaning": "song; singer; vine",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 25:2", "1 Chronicles 1:32"]
},

"zimri": {
  "id": "zimri",
  "term": "Zimri",
  "category": "people",
  "intro": "<p>Zimri (meaning: <em>praiseworthy</em>) is the name of several men in the Old Testament, two of whom are prominent. (1.) A son of Salu of the tribe of Simeon who brazenly brought a Midianite woman into the Israelite camp during the plague at Shittim. Phinehas the priest ran them both through with a spear, ending the plague and earning Phinehas an eternal covenant of priesthood (<strong>Num. 25:6–15</strong>). (2.) An army officer who murdered King Elah of Israel and seized the throne (<strong>1 Kings 16:8–20</strong>). His reign lasted only seven days: when the army heard what he had done, they acclaimed Omri as king. Omri besieged Tirzah, and when Zimri saw the city was taken he burned the palace over himself and perished.</p><p>Zimri's name became a byword for treachery. When Jehu killed Joram, Jezebel taunted him by calling him \"Zimri, murderer of his master\" (<strong>2 Kings 9:31</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "praiseworthy",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 25:6", "1 Kings 16:9", "2 Kings 9:31"]
},

"zin": {
  "id": "zin",
  "term": "Zin",
  "category": "places",
  "intro": "<p>Zin was a wilderness region forming the southeastern boundary of the land of Canaan and adjoining the wilderness of Paran. It is first mentioned when the twelve spies sent from Kadesh-barnea traversed it (<strong>Num. 13:21</strong>); the southern border of the promised land ran through it (<strong>Num. 34:3–4</strong>). Kadesh (Kadesh-barnea) lay within the wilderness of Zin (<strong>Num. 27:14</strong>; <strong>33:36</strong>).</p><p>The wilderness of Zin is to be distinguished from the wilderness of Sin (the Desert of Sinai, between Elim and Sinai, <strong>Ex. 16:1</strong>). Zin corresponds to the northeastern portion of the Sinai Peninsula, roughly the modern Desert of et-Tih east of the Gulf of Suez. It was in this region that Miriam died and was buried, and where the congregation quarreled with Moses over water at Meribah-kadesh (<strong>Num. 20:1–13</strong>), leading to the exclusion of Moses and Aaron from the promised land.</p>",
  "sections": [],
  "hitchcock_meaning": "buckler; coldness",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 13:21", "Numbers 20:1", "Numbers 27:14", "Numbers 34:3"]
},

"zina": {
  "id": "zina",
  "term": "Zina",
  "category": "people",
  "intro": "<p>Zina (meaning: <em>shining; going back</em>) was a son of Shimei the Gershonite Levite (<strong>1 Chr. 23:10</strong>). He is listed among the sons of Shimei in the organization of the Levites under David's administration, though the parallel verse (<strong>1 Chr. 23:11</strong>) names his brother Zizah as the one who, together with Jeush, formed a unit counted as a single father's house because their combined number was small. The two names Zina and Zizah may represent variant forms of the same name or a scribal variation between manuscripts.</p>",
  "sections": [],
  "hitchcock_meaning": "shining; going back",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 23:10"]
},

"zion": {
  "id": "zion",
  "term": "Zion",
  "category": "places",
  "intro": "<p>Zion (meaning: <em>monument; raised up</em>) was originally the southeastern hill of Jerusalem — the ridge David captured from the Jebusites and fortified as his royal citadel, calling it \"the city of David\" (<strong>2 Sam. 5:7</strong>; <strong>1 Kings 8:1</strong>). It stood south of the Moriah ridge (the temple mount), separated from it by the Tyropoeon valley. When Solomon built the temple on Moriah and transferred the ark there, the name Zion extended by association to the temple mount and to Jerusalem as a whole.</p><p>In the Psalms and the Prophets, Zion becomes a theological name for the dwelling place of God among his people (<strong>Ps. 87:2</strong>; <strong>Ps. 149:2</strong>; <strong>Isa. 33:14</strong>; <strong>Joel 2:1</strong>). The prophets lament its fall and promise its restoration. In the New Testament, Hebrews 12:22 identifies \"Mount Zion\" with the heavenly Jerusalem, the city of the living God; Revelation 14:1 pictures the Lamb standing on Mount Zion with the 144,000. Zion thus moves from a physical hilltop to the ultimate symbol of God's redeemed community.</p>",
  "sections": [],
  "hitchcock_meaning": "monument; raised up; sepulcher",
  "source_ids": ["easton"],
  "key_refs": ["2 Samuel 5:7", "Psalms 87:2", "Hebrews 12:22", "Revelation 14:1"]
},

"zior": {
  "id": "zior",
  "term": "Zior",
  "category": "places",
  "intro": "<p>Zior (meaning: <em>littleness</em>) was a city in the hill country of Judah, listed among the towns allotted to that tribe in <strong>Joshua 15:54</strong>. Easton identifies it with the modern village of Si'air, located approximately four and a half miles north-northeast of Hebron in the highlands of Judah. It appears only in this one verse in the allotment list and is not mentioned elsewhere in Scripture.</p><p>Si'air (Khirbet Si'ir) sits in the same mountainous district as Hebron and Debir, a region that played a central role in the early Israelite settlement of Canaan. The name Zior — suggesting smallness — is consistent with a minor village in the broader Hebron highlands.</p>",
  "sections": [],
  "hitchcock_meaning": "ship of him that watches",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 15:54"]
},

"ziph": {
  "id": "ziph",
  "term": "Ziph",
  "category": "places",
  "intro": "<p>Ziph (meaning: <em>falsehood; flowing</em>) is the name of a man and of two cities. (1.) A descendant of Judah through Jehaleleel (<strong>1 Chr. 4:16</strong>). (2.) A city in the southern Negeb of Judah (<strong>Josh. 15:24</strong>), probably near the pass of Sufah. (3.) A city in the hill country of Judah (<strong>Josh. 15:55</strong>), identified with Tell ez-Zif, about five miles southeast of Hebron. This third Ziph is the most prominent: David hid in the wilderness near it during his flight from Saul (<strong>1 Sam. 23:19</strong>), and the Ziphites twice betrayed his location to Saul. Psalm 54 is titled \"when the Ziphites came and told Saul.\" The city was later fortified by Rehoboam (<strong>2 Chr. 11:8</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "this mouth or mouthful; falsehood",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 15:55", "1 Samuel 23:19", "Psalms 54:1", "2 Chronicles 11:8"]
},

"ziphah": {
  "id": "ziphah",
  "term": "Ziphah",
  "category": "people",
  "intro": "<p>Ziphah was a descendant of Judah through Jehaleleel, listed in the genealogical records of <strong>1 Chronicles 4:16</strong> alongside his brothers Ziph, Tiria, and Asareel. He is mentioned only in this single genealogical verse and nothing further is recorded of him in Scripture.</p><p>The name Ziphah appears to be a variant or feminine form of Ziph, and the grouping of Ziph and Ziphah as brothers suggests either a wordplay in the naming conventions of the period or a genealogical connection between the city of Ziph and this family in the tribe of Judah.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 4:16"]
},

"ziphron": {
  "id": "ziphron",
  "term": "Ziphron",
  "category": "places",
  "intro": "<p>Ziphron (meaning: <em>falsehood of a song; rejoicing</em>) was a town on the northern border of the land of Canaan as defined in <strong>Numbers 34:9</strong>, lying southeast of Hamath. It served as one of the boundary markers delimiting the northern extent of the promised land. Its precise location has not been established with certainty by modern archaeology.</p><p>The northern border description in Numbers 34 runs from the Great Sea (Mediterranean) eastward through Hazar-enan and Ziphron to Hazar-enan, defining an idealized boundary that Israel rarely controlled fully during the monarchy period. Ziphron appears only in this boundary passage and is otherwise unattested in Scripture.</p>",
  "sections": [],
  "hitchcock_meaning": "falsehood of a song; rejoicing",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 34:9"]
},

"zippor": {
  "id": "zippor",
  "term": "Zippor",
  "category": "people",
  "intro": "<p>Zippor (meaning: <em>bird; sparrow; crown; desert</em>) was the father of Balak, king of Moab during the time of Israel's wilderness wanderings (<strong>Num. 22:2, 4</strong>). When the Israelites camped on the plains of Moab near the Jordan, Balak son of Zippor was alarmed by their numbers and sent messengers to Balaam the prophet to come and curse them. God turned each of Balaam's intended curses into blessings. Balak is repeatedly identified by his patronymic \"son of Zippor\" throughout Numbers 22–24, though Zippor himself receives no further description.</p><p>The name Zippor (\"bird\") is consistent with Moabite personal nomenclature. Its bearer was apparently a previous king of Moab or a prominent noble whose lineage conferred legitimacy on Balak's reign.</p>",
  "sections": [],
  "hitchcock_meaning": "bird; sparrow; crown; desert",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 22:2", "Numbers 22:4", "Numbers 23:18"]
},

"zipporah": {
  "id": "zipporah",
  "term": "Zipporah",
  "category": "people",
  "intro": "<p>Zipporah (meaning: <em>beauty; trumpet; mourning</em> — i.e., \"little bird\") was a daughter of Reuel (Jethro), priest of Midian, and the wife of Moses (<strong>Ex. 2:21</strong>). Moses married her after fleeing Egypt and defending Jethro's daughters at a well. She bore him two sons, Gershom and Eliezer.</p><p>Zipporah plays a striking role in the difficult passage of <strong>Exodus 4:24–26</strong>, where the Lord threatened Moses on the journey back to Egypt and Zipporah circumcised their son and touched Moses's feet with the foreskin, declaring \"You are a bridegroom of blood to me.\" This averted the divine threat. When Moses later led the Israelites out of Egypt, Zipporah and her sons, who had apparently returned to Midian (<strong>Ex. 18:2–6</strong>), were brought back to him by Jethro at the mountain of God. Her subsequent fate is not recorded.</p>",
  "sections": [],
  "hitchcock_meaning": "beauty; trumpet; mourning",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 2:21", "Exodus 4:25", "Exodus 18:2"]
},

"zithri": {
  "id": "zithri",
  "term": "Zithri",
  "category": "people",
  "intro": "<p>Zithri (meaning: <em>to hide; demolished</em> — or \"the Lord protects\") was a Levite of the Kohathite clan, listed as a son of Uzziel, brother of Mishael and Elzaphan (<strong>Ex. 6:22</strong>). He appears in the Levitical genealogy of Exodus as a nephew of Aaron and a cousin of Moses, part of the generation that served during the Exodus and wilderness period. No further deeds or biography are recorded for him in Scripture.</p><p>The sons of Uzziel are referenced in Numbers 3:30 as heads of Kohathite clans responsible for the most sacred items of the tabernacle. Zithri's inclusion in the Exodus genealogy places him within the inner circles of the Levitical hierarchy, though he remains a minor figure compared to his more prominent cousin-relatives.</p>",
  "sections": [],
  "hitchcock_meaning": "to hide; demolished",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 6:22"]
},

"ziz": {
  "id": "ziz",
  "term": "Ziz",
  "category": "places",
  "intro": "<p>Ziz (meaning: <em>flower; branch; a lock of hair</em>) was the name of a pass or ascent leading up from the Dead Sea region toward the wilderness of Judah. It appears in <strong>2 Chronicles 20:16</strong>, where the Lord tells Jehoshaphat through the Levite Jahaziel that the vast Moabite-Ammonite army was coming up by the ascent of Ziz and would be found at the end of the valley before the wilderness of Jeruel.</p><p>Easton identifies the ascent of Ziz with a pass near En-gedi that leads upward from the Dead Sea toward Tekoa. The modern Tell Hasasah is suggested as the site. Jehoshaphat's army went out to face the invaders and found them already dead — the armies had turned on one another — and spent three days collecting the plunder.</p>",
  "sections": [],
  "hitchcock_meaning": "flower; branch; a lock of hair",
  "source_ids": ["easton"],
  "key_refs": ["2 Chronicles 20:16"]
},

"ziza": {
  "id": "ziza",
  "term": "Ziza",
  "category": "people",
  "intro": "<p>Ziza (meaning: <em>same as Zina</em> — splendour; abundance) is the name of two men in Chronicles. (1.) A prince of the tribe of Simeon who led an expansion into the valley of Gedor and dispossessed the Hamites there during the days of Hezekiah (<strong>1 Chr. 4:37–43</strong>). (2.) A son of Rehoboam by his favorite wife Maachah daughter of Absalom (<strong>2 Chr. 11:20</strong>). Rehoboam had eighteen wives and sixty concubines; Maachah was preeminent among them, and Ziza was one of the sons he particularly honored.</p><p>The name Ziza appears to be a variant of Zina and carries a similar meaning of brightness or abundance. The two men who bear it are separated by about two centuries and belong to entirely different tribes.</p>",
  "sections": [],
  "hitchcock_meaning": "same as Zina",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 4:37", "2 Chronicles 11:20"]
},

"zizah": {
  "id": "zizah",
  "term": "Zizah",
  "category": "people",
  "intro": "<p>Zizah was a Gershonite Levite, listed as one of the sons of Shimei in the organization of Levitical clans under David (<strong>1 Chr. 23:11</strong>). His brothers were Jahath, Zina (or Zina's variant Zizah itself — the texts show a minor variation), and Jeush. Because Jeush and Zizah had few sons, they were reckoned together as a single father's house rather than being divided into separate clans.</p><p>Zizah may be the same individual as Zina in <strong>1 Chronicles 23:10</strong>, with the two names representing a scribal variation or alternate form within the tradition. The Gershonite Levites under David's organization were responsible for portions of the tabernacle's fabric coverings and for musical service in the sanctuary.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 23:11"]
},

"zoan": {
  "id": "zoan",
  "term": "Zoan",
  "category": "places",
  "intro": "<p>Zoan (meaning: <em>motion; place of departure</em>) was an ancient and strategically important city of Lower Egypt, called Tanis by the Greeks, on the eastern bank of the Tanitic branch of the Nile. It was founded seven years after Hebron in Canaan (<strong>Num. 13:22</strong>), suggesting great antiquity. It served as the capital of the Hyksos (Shepherd kings) who ruled Egypt for more than 500 years, and as a frontier town of Goshen, the region where Israel settled.</p><p>Psalm 78:12, 43 refers to the \"field of Zoan\" as the location of the plagues and wonders Moses performed before Pharaoh, which strongly implies that the court of the Exodus Pharaoh was located here. Isaiah's oracles against Egypt mention Zoan's princes and counselors as failing in wisdom (<strong>Isa. 19:11–13</strong>), and Ezekiel prophesies its judgment alongside Memphis and Thebes (<strong>Ezek. 30:14</strong>). Extensive mounds of ruins at modern San el-Hagar mark the site of the ancient city.</p>",
  "sections": [],
  "hitchcock_meaning": "motion",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 13:22", "Psalms 78:12", "Isaiah 19:11", "Ezekiel 30:14"]
},

"zoar": {
  "id": "zoar",
  "term": "Zoar",
  "category": "places",
  "intro": "<p>Zoar (meaning: <em>little; small</em>) was one of the five cities of the plain, originally called Bela (<strong>Gen. 14:2, 8</strong>), located on the east or southeast shore of the Dead Sea. When the Lord rained fire and sulfur on Sodom and Gomorrah, Lot pleaded for Zoar to be spared because of its smallness, and God granted the request (<strong>Gen. 19:20–22</strong>). Lot and his daughters fled there, though he soon left for the hills because he feared remaining in the city.</p><p>Zoar appears in the death of Moses narrative as a landmark visible from Mount Pisgah (<strong>Deut. 34:3</strong>). Both Isaiah (15:5) and Jeremiah (48:34) mention it in oracles against Moab, indicating it survived into the prophetic era as a recognizable place. Its ruins have been tentatively identified at Tell esh-Shaghur at the opening of the ravine of Kerak on the southeastern shore of the Dead Sea.</p>",
  "sections": [],
  "hitchcock_meaning": "little; small",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 19:22", "Genesis 19:30", "Deuteronomy 34:3", "Isaiah 15:5"]
},

"zobah": {
  "id": "zobah",
  "term": "Zobah",
  "category": "places",
  "intro": "<p>Zobah (also Aram-Zobah) was an Aramaean (Syrian) kingdom south of Coele-Syria, extending from the eastern slopes of the Lebanon range northward and eastward toward the Euphrates. It was one of several powerful Aramaean states that Israel encountered at the height of its power under Saul and David. Saul fought against the kings of Zobah (<strong>1 Sam. 14:47</strong>), and David later defeated Hadadezer king of Zobah in a major battle, capturing his officers and taking vast quantities of bronze from the Zobahite cities (<strong>2 Sam. 8:3–12</strong>).</p><p>When the Ammonites hired Aramaean mercenaries against David, the forces included soldiers from Zobah (<strong>2 Sam. 10:6</strong>). After David's victories, Zobah declined in significance. Psalm 60's title connects the psalm to a war against Aram-Zobah, placing the composition in this period. By Solomon's time, Rezon, a former servant of Hadadezer, had seized Damascus and became Israel's adversary (<strong>1 Kings 11:23–25</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "Zobebah, an army; warring",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 14:47", "2 Samuel 8:3", "2 Samuel 10:6", "Psalms 60:1"]
},

"zohar": {
  "id": "zohar",
  "term": "Zohar",
  "category": "people",
  "intro": "<p>Zohar (meaning: <em>white; bright; dryness</em>) is the name of two men in the Pentateuch. (1.) The father of Ephron the Hittite, from whom Abraham purchased the cave of Machpelah as a burial site for Sarah (<strong>Gen. 23:8</strong>). Abraham addressed Ephron as \"son of Zohar\" in the formal negotiation before the Hittite community, indicating Zohar was a man of standing. (2.) A son of Simeon, listed among those who went down to Egypt with Jacob (<strong>Gen. 46:10</strong>; <strong>Ex. 6:15</strong>). In Numbers 26:13 his name appears as Zerah, suggesting a variant spelling.</p><p>The two men named Zohar lived in the same general period — the patriarchal era — but in entirely different contexts, one as a Hittite elder and one as a son of Israel.</p>",
  "sections": [],
  "hitchcock_meaning": "white; bright; dryness",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 23:8", "Genesis 46:10", "Exodus 6:15"]
},

"zoheleth": {
  "id": "zoheleth",
  "term": "Zoheleth",
  "category": "places",
  "intro": "<p>Zoheleth (meaning: <em>that creeps; slides; or draws</em>) was a rocky plateau or stone ledge near the village of Siloam and the spring of En-rogel in the Kidron valley southeast of Jerusalem. It is mentioned in <strong>1 Kings 1:9</strong> as the place where Adonijah slaughtered oxen, fat cattle, and sheep in a feast to which he invited all his brothers and the royal officers — but not Solomon, Zadok the priest, Nathan the prophet, or Benaiah.</p><p>While this feast was in progress at Zoheleth, Nathan alerted Bathsheba and they informed David, who immediately ordered Solomon anointed king at the Gihon spring. When the shout of the city reached Adonijah's guests at Zoheleth, they fled in terror. Adonijah himself fled to take hold of the horns of the altar and was pardoned by Solomon, at least temporarily.</p>",
  "sections": [],
  "hitchcock_meaning": "that creeps, slides, or draws",
  "source_ids": ["easton"],
  "key_refs": ["1 Kings 1:9", "1 Kings 1:49"]
},

"zoheth": {
  "id": "zoheth",
  "term": "Zoheth",
  "category": "people",
  "intro": "<p>Zoheth (meaning: <em>separation; amazing</em>) was a son of Ishi, listed in the genealogy of the tribe of Judah in <strong>1 Chronicles 4:20</strong>. He and his brother Ben-zoheth are named among the descendants of Ishi, but no further biographical information is given. The passage situates him in the post-settlement genealogical records of Judah, though the precise period he lived in cannot be determined from the genealogy alone.</p>",
  "sections": [],
  "hitchcock_meaning": "separation; amazing",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 4:20"]
},

"zophah": {
  "id": "zophah",
  "term": "Zophah",
  "category": "people",
  "intro": "<p>Zophah (meaning: <em>viol; honeycomb</em>) was a son of Helem (also called Hotham) and a chief of the tribe of Asher, listed in the genealogy of <strong>1 Chronicles 7:35–36</strong>. His sons are enumerated in verse 36 as Suah, Harnepher, Shual, Beri, Imrah, Bezer, Hod, Shamma, Shilshah, Ithran, and Beera — a substantial list of Asherite family heads. Nothing further is recorded of Zophah himself beyond his lineage and the names of his sons.</p>",
  "sections": [],
  "hitchcock_meaning": "viol; honeycomb",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 7:35"]
},

"zophar": {
  "id": "zophar",
  "term": "Zophar",
  "category": "people",
  "intro": "<p>Zophar (meaning: <em>rising early; crown</em>) was one of the three friends of Job who came to console him in his suffering (<strong>Job 2:11</strong>). He is identified as a Naamathite, from some place called Naamah whose location is uncertain. Zophar is the harshest of the three friends: in his two speeches (chapters 11 and 20) he accuses Job most bluntly of secret sin, insists that God is exacting less from Job than his guilt deserves (<strong>Job 11:6</strong>), and paints a vivid picture of the wicked man's certain downfall.</p><p>Job receives no speech from Zophar in the third cycle, suggesting the dialogue broke down. At the end, God rebukes all three friends for not speaking what is right about him as his servant Job had done (<strong>Job 42:7–9</strong>), and they are required to offer burnt offerings with Job interceding for them.</p>",
  "sections": [],
  "hitchcock_meaning": "rising early; crown",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Job 2:11", "Job 11:1", "Job 20:1", "Job 42:9"]
},

"zophim-field-of": {
  "id": "zophim-field-of",
  "term": "Zophim, Field of",
  "category": "places",
  "intro": "<p>The Field of Zophim (meaning: <em>field of watchers</em>) was a location in Moab on the range of Pisgah, to which Balak brought Balaam for his second attempt to curse Israel (<strong>Num. 23:14</strong>). From this elevated vantage point Balaam looked out over the Israelite encampment and, as before, could speak only the word the Lord gave him — a blessing rather than the curse Balak had hired him to pronounce.</p><p>The name \"field of watchers\" suggests a high lookout point where sentinels could survey the surrounding terrain. Easton tentatively identifies it with the modern Tal'at-es-Safa on the Pisgah ridge. The scene at Zophim is part of the extended Balaam narrative that spans Numbers 22–24 and culminates in Balaam's final oracles concerning the star from Jacob.</p>",
  "sections": [],
  "hitchcock_meaning": "field of watchers",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 23:14"]
},

"zorah": {
  "id": "zorah",
  "term": "Zorah",
  "category": "places",
  "intro": "<p>Zorah (meaning: <em>leprosy; scab; hornet</em>) was a town in the Shephelah (the hill country foothills) of Judah, assigned to the tribe of Dan (<strong>Josh. 19:41</strong>), and earlier listed among Judah's towns (<strong>Josh. 15:33</strong>, as Zoreah). It is most famous as the birthplace and burial place of Samson, whose father Manoah was a Danite from Zorah (<strong>Judg. 13:2</strong>). The spirit of the Lord began to stir Samson \"between Zorah and Eshtaol\" (<strong>Judg. 13:25</strong>), and his body was buried between these two towns after the collapse of the temple of Dagon (<strong>Judg. 16:31</strong>).</p><p>Zorah overlooks the valley of Sorek and was later fortified by Rehoboam as part of his defense network (<strong>2 Chr. 11:10</strong>). The Danite spies who went north to find new territory for the tribe also passed through Zorah and Eshtaol (<strong>Judg. 18:2</strong>). It is identified with the modern village of Sur'ah in the Wady Surar, about 8 miles west of Jerusalem.</p>",
  "sections": [],
  "hitchcock_meaning": "leprosy; scab; hornet",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Judges 13:2", "Judges 16:31", "Joshua 15:33", "2 Chronicles 11:10"]
},

"zuph": {
  "id": "zuph",
  "term": "Zuph",
  "category": "people",
  "intro": "<p>Zuph (meaning: <em>that beholds; watches; roof; covering</em>) was a Kohathite Levite and an ancestor of Samuel the prophet. He is listed in <strong>1 Samuel 1:1</strong> in the genealogy of Elkanah: \"Elkanah son of Jeroham son of Elihu son of Tohu son of Zuph, an Ephraimite.\" The description \"Ephraimite\" here refers to his residence in the territory of Ephraim rather than tribal descent, as Levites lived among the other tribes. In the parallel genealogy of <strong>1 Chronicles 6:26</strong>, Zuph appears as Zophai.</p><p>The district of Zuph (the \"land of Zuph\") was named after him or his family. It was in this region that Saul and his servant searched for his father's donkeys and found the prophet Samuel instead (<strong>1 Sam. 9:5–6</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "that beholds, observes, watches; roof; covering",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 1:1", "1 Chronicles 6:26"]
},

"zuph-land-of": {
  "id": "zuph-land-of",
  "term": "Zuph, Land of",
  "category": "places",
  "intro": "<p>The Land of Zuph was a district in the hill country of Ephraim that takes its name from the Levitical ancestor Zuph, from whom Samuel's father Elkanah descended (<strong>1 Chr. 6:26</strong>, margin). It is mentioned in <strong>1 Samuel 9:5–6</strong> during the account of Saul's search for his father's lost donkeys: when the servants had passed through several districts without finding them, they entered the land of Zuph, where Saul's servant suggested consulting the man of God (Samuel) whose city was nearby.</p><p>Samuel's city, Ramah, lay within or near this district, confirming that the land of Zuph was situated in the central highlands of Benjamin and Ephraim. The district name preserved the memory of the priestly family settled there from the time of the Levitical distribution across Israel.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 9:5", "1 Samuel 9:6", "1 Chronicles 6:26"]
},

"zur": {
  "id": "zur",
  "term": "Zur",
  "category": "people",
  "intro": "<p>Zur (meaning: <em>stone; rock; that besieges</em>) is the name of two men in the Old Testament. (1.) One of the five kings of Midian defeated and killed by Israel during the campaign ordered by God in response to Midian's seduction of Israel at Baal-peor (<strong>Num. 31:8</strong>; <strong>Josh. 13:21</strong>). Zur was the father of Cozbi, the Midianite woman killed by Phinehas along with Zimri in Numbers 25. He is identified as a chief and prince of Midian. (2.) A Benjamite, son of Jehiel the father of Gibeon and his wife Maachah (<strong>1 Chr. 8:30</strong>; <strong>9:36</strong>). This Zur was thus an ancestor of the Gibeonite/Benjamite family from whom King Saul descended.</p>",
  "sections": [],
  "hitchcock_meaning": "stone; rock; that besieges",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 31:8", "Numbers 25:15", "1 Chronicles 8:30"]
},

"zuriel": {
  "id": "zuriel",
  "term": "Zuriel",
  "category": "people",
  "intro": "<p>Zuriel (meaning: <em>rock or strength of God</em>) was the son of Abihail and chief of the Merarite families of Levi at the time of the Exodus census (<strong>Num. 3:35</strong>). The Merarites were the third division of the Levites (alongside the Gershonites and Kohathites) and were responsible for the boards, bars, pillars, bases, and other structural elements of the tabernacle. Their encampment was assigned to the north side of the tabernacle.</p><p>Zuriel's name combines the common element <em>zur</em> (\"rock\") with <em>el</em> (\"God\"), a theophoric compound affirming God as the family's strength and foundation. He appears only in this one census reference and is otherwise unattested in Scripture.</p>",
  "sections": [],
  "hitchcock_meaning": "rock or strength of God",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 3:35"]
},

"zurishaddai": {
  "id": "zurishaddai",
  "term": "Zurishaddai",
  "category": "people",
  "intro": "<p>Zurishaddai (meaning: <em>the Almighty is my rock and strength</em>) was the father of Shelumiel, who served as the appointed leader of the tribe of Simeon at the time Israel was encamped at Sinai and the first census was taken (<strong>Num. 1:6</strong>; <strong>2:12</strong>). Shelumiel son of Zurishaddai commanded the Simeonite division of the camp throughout the wilderness narratives, leading them at the departure from Sinai (<strong>Num. 10:19</strong>) and presenting the Simeonite offering at the dedication of the tabernacle altar (<strong>Num. 7:36–41</strong>).</p><p>Zurishaddai himself is never mentioned apart from his role as Shelumiel's father, but the richness of his name — combining <em>zur</em> (\"rock\"), <em>shaddai</em> (\"Almighty\") — reflects the patriarchal tradition of naming children with declarations of God's power and faithfulness.</p>",
  "sections": [],
  "hitchcock_meaning": "the Almighty is my rock and strength",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 1:6", "Numbers 2:12", "Numbers 7:36", "Numbers 10:19"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP z2: Zibiah → Zurishaddai: wrote {written}, skipped {skipped} existing.")

main()
