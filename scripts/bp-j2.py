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
"jedidiah": {
  "id": "jedidiah", "term": "Jedidiah", "category": "people",
  "intro": "<p>Jedidiah (meaning <em>beloved of the LORD</em>) was the name given by God through the prophet Nathan to Solomon at his birth, as a token of divine favor and acceptance (<a class=\"ref\" data-ref=\"2 Samuel 12:25\">2 Samuel 12:25</a>). The name was delivered immediately after the death of the first child born to David and Bathsheba, which had been a judgment on David's sin with her. The birth of Solomon and the name Jedidiah signal God's gracious restoration of David's household despite his failure.</p><p>Solomon is not recorded as using this name publicly — he is known throughout his reign simply as Solomon (meaning <em>peaceful</em>). Jedidiah functioned as a private divine affirmation, an assurance from God himself that this child was beloved. The name has been connected typologically to the declaration over Jesus at his baptism: \"This is my beloved Son, in whom I am well pleased\" (Matthew 3:17), in which the divine affirmation of the son prefigures the greater Son of David.</p>",
  "hitchcock_meaning": "beloved of the Lord",
  "source_ids": {"easton": "jedidiah", "smith": "jedidiah", "isbe": "jedidiah"},
  "key_refs": ["2 Samuel 12:25"]
},
"jeduthun": {
  "id": "jeduthun", "term": "Jeduthun", "category": "people",
  "intro": "<p>Jeduthun (meaning <em>his law</em> or <em>giving praise</em>) was a Levite of the family of Merari appointed by David as one of the three masters of music for the sanctuary, alongside Asaph and Heman (<a class=\"ref\" data-ref=\"1 Chronicles 16:41\">1 Chronicles 16:41-42</a>; 25:1-6). His sons served in the ministry of prophesying with lyres and harps. Several psalms carry the superscription \"to Jeduthun\" or \"according to Jeduthun\" (Psalms 39, 62, 77), indicating either a musical guild associated with his name or a specific melody or style.</p><p>Jeduthun was also called Ethan (1 Chronicles 15:17, 19), suggesting the two names belonged to the same person or were closely associated figures. His ministry continued into the reign of Solomon (<a class=\"ref\" data-ref=\"2 Chronicles 35:15\">2 Chronicles 35:15</a>) and his descendants maintained their role as sanctuary singers through the post-exilic period, with Jeduthun's descendants numbered among the Levitical singers who returned from Babylon (<a class=\"ref\" data-ref=\"Nehemiah 11:17\">Nehemiah 11:17</a>).</p>",
  "hitchcock_meaning": "his law; giving praise",
  "source_ids": {"easton": "jeduthun", "smith": "jeduthun", "isbe": "jeduthun"},
  "key_refs": ["1 Chronicles 16:41", "2 Chronicles 35:15", "Nehemiah 11:17"]
},
"jegar-sahadutha": {
  "id": "jegar-sahadutha", "term": "Jegar-sahadutha", "category": "places",
  "intro": "<p>Jegar-sahadutha (Aramaic for <em>heap of witness</em>) is the name Laban the Aramean gave to the stone pillar and heap of stones that he and Jacob erected at their covenant-making on Mount Gilead (<a class=\"ref\" data-ref=\"Genesis 31:47\">Genesis 31:47</a>). Jacob gave the same memorial the Hebrew equivalent name Galeed (also meaning \"heap of witness\"), and the place was also called Mizpah (\"watchtower\") because Laban said, \"May the LORD watch between you and me when we are absent from one another.\"</p><p>The two names for a single monument — Aramaic and Hebrew — reflect the bilingualism of the patriarchal border region and the separate ethnic identities of the two parties to the covenant. The monument marked the northern boundary of Jacob's territory and served as a witness to their mutual non-aggression agreement. This is the only occurrence of Aramaic in the patriarchal narratives and one of the earliest attested examples of the Aramaic language in the Old Testament.</p>",
  "hitchcock_meaning": "heap of witness",
  "source_ids": {"easton": "jegar-sahadutha"},
  "key_refs": ["Genesis 31:47"]
},
"jehaleleel": {
  "id": "jehaleleel", "term": "Jehaleleel", "category": "people",
  "intro": "<p>Jehaleleel (also spelled Jehallelel; meaning <em>praising God</em> or <em>clearness of God</em>) is the name of two minor figures in the Old Testament. The first was a descendant of Judah through Caleb's second wife, whose sons are listed in the genealogy of 1 Chronicles 4:16 (<a class=\"ref\" data-ref=\"1 Chronicles 4:16\">1 Chronicles 4:16</a>). The second was a Levite of the family of Merari, whose son Azariah assisted in the cleansing of the temple under Hezekiah (<a class=\"ref\" data-ref=\"2 Chronicles 29:12\">2 Chronicles 29:12</a>).</p><p>Both figures are minor participants in the larger genealogical and narrative framework of Chronicles. Their inclusion reflects the Chronicler's interest in comprehensive genealogical coverage of Judah and the Levitical families whose descendants would return from exile and reconstitute the Israelite community. The name itself — praising God — is theologically appropriate for a Levite associated with temple worship.</p>",
  "hitchcock_meaning": "Jehalelel, praising God; clearness of God",
  "source_ids": {"easton": "jehaleleel", "smith": "jehaleleel"},
  "key_refs": ["1 Chronicles 4:16", "2 Chronicles 29:12"]
},
"jehdeiah": {
  "id": "jehdeiah", "term": "Jehdeiah", "category": "people",
  "intro": "<p>Jehdeiah (meaning <em>joy together</em> or <em>one Lord</em>) is the name of two minor figures in the genealogical lists of Chronicles. The first was a Levite, a descendant of Shubael, appointed to serve in the post-Davidic organization of the Levitical courses (<a class=\"ref\" data-ref=\"1 Chronicles 24:20\">1 Chronicles 24:20</a>). The second was the official appointed by David to oversee the royal donkeys — part of the administrative structure of the Davidic kingdom listed in 1 Chronicles 27 (<a class=\"ref\" data-ref=\"1 Chronicles 27:30\">1 Chronicles 27:30</a>).</p><p>Both are minor figures whose significance lies primarily in their role within the larger administrative and cultic organization that David established for the sanctuary and the kingdom. The Chronicler's detailed preservation of such names reflects his interest in documenting the full breadth of Israel's service structure.</p>",
  "hitchcock_meaning": "joy together, one Lord",
  "source_ids": {"easton": "jehdeiah", "smith": "jehdeiah", "isbe": "jehdeiah"},
  "key_refs": ["1 Chronicles 24:20", "1 Chronicles 27:30"]
},
"jehiel": {
  "id": "jehiel", "term": "Jehiel", "category": "people",
  "intro": "<p>Jehiel is the name of at least nine different individuals in the Old Testament, most of them minor Levitical or Benjamite figures. The most prominent are: the son of Hachmoni who served as a companion to David's sons (<a class=\"ref\" data-ref=\"1 Chronicles 27:32\">1 Chronicles 27:32</a>); a Levite musician appointed to play a harp before the ark during its transfer to Jerusalem (<a class=\"ref\" data-ref=\"1 Chronicles 15:18\">1 Chronicles 15:18, 20</a>); and Jehiel, the father of Gibeon, an ancestor of King Saul (<a class=\"ref\" data-ref=\"1 Chronicles 9:35\">1 Chronicles 9:35</a>).</p><p>The name (related to a root meaning \"God lives\" or \"may God live\") was common enough in Israel to be shared by many unrelated individuals. Their appearances across Chronicles, Ezra, and Nehemiah reflect the Chronicler's comprehensive genealogical interest in the families who constituted pre-exilic Israel and the post-exilic restoration community.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jehiel", "smith": "jehiel"},
  "key_refs": ["1 Chronicles 9:35", "1 Chronicles 15:18", "1 Chronicles 27:32"]
},
"jehizkiah": {
  "id": "jehizkiah", "term": "Jehizkiah", "category": "people",
  "intro": "<p>Jehizkiah (meaning <em>strength of the LORD</em>) was a leader of the tribe of Ephraim who, together with three other chieftains, opposed the prophet Oded's initiative when he met the army of Israel returning with 200,000 captives from Judah after a victory over King Ahaz (<a class=\"ref\" data-ref=\"2 Chronicles 28:12\">2 Chronicles 28:12</a>). These four leaders listened to the prophet's rebuke — that Israel had sinned in capturing their Judahite brothers — and prevailed upon the army to release the captives, clothe and feed them, and return them to Jericho.</p><p>This episode stands out as a rare moment in the divided monarchy's history when prophetic rebuke was immediately heeded and brotherly solidarity prevailed over military triumph. Jehizkiah appears only in this passage but plays a significant role in an act of covenant justice that the Chronicler preserves as a model of proper response to prophetic correction.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jehizkiah", "smith": "jehizkiah", "isbe": "jehizkiah"},
  "key_refs": ["2 Chronicles 28:12"]
},
"jehoaddan": {
  "id": "jehoaddan", "term": "Jehoaddan", "category": "people",
  "intro": "<p>Jehoaddan (meaning <em>pleasure</em> or <em>time of the LORD</em>) was the mother of King Amaziah of Judah (<a class=\"ref\" data-ref=\"2 Kings 14:2\">2 Kings 14:2</a>; 2 Chronicles 25:1), who reigned approximately 796–767 B.C. She was a native of Jerusalem. Queen mothers in the Judahite monarchy held a recognized position of honor and influence at court, and their names are regularly preserved in the royal formulae of Kings and Chronicles.</p><p>Amaziah is evaluated by the Deuteronomistic historian as one who \"did what was right in the eyes of the LORD, yet not like his father David\" — a qualified approval. His reign saw a notable victory over Edom in the Valley of Salt (2 Kings 14:7) but ended in disaster when he challenged Jehoash of Israel to battle and was decisively defeated. Jehoaddan appears only in the introductory formula of Amaziah's reign and is otherwise unknown.</p>",
  "hitchcock_meaning": "pleasure, or time, of the Lord",
  "source_ids": {"easton": "jehoaddan", "smith": "jehoaddan", "isbe": "jehoaddan"},
  "key_refs": ["2 Kings 14:2"]
},
"jehoahaz": {
  "id": "jehoahaz", "term": "Jehoahaz", "category": "people",
  "intro": "<p>Jehoahaz (meaning <em>possession of the LORD</em>) was the name of three biblical kings. (1.) Jehoahaz king of Israel, son of Jehu, who reigned approximately 814–798 B.C. His reign saw severe oppression by Syria (Hazael and Ben-hadad) under which Israel was reduced to almost no army. When Jehoahaz \"sought the LORD,\" God raised up a deliverer, though Israel did not repent of Jeroboam's sins (2 Kings 13:1-9). (2.) Jehoahaz king of Judah (also called Ahaziah), son of Jehoram, who reigned one year and was killed by Jehu (2 Chronicles 21:17; 22:1-9). (3.) Jehoahaz, also called Shallum (<a class=\"ref\" data-ref=\"2 Chronicles 21:17\">Jeremiah 22:11</a>), a son of Josiah who reigned three months before being deported to Egypt by Pharaoh Neco (2 Kings 23:31-34).</p><p>The third Jehoahaz is the subject of Jeremiah's lament (Jeremiah 22:10-12): \"Weep not for the dead, neither bemoan him: but weep sore for him that goeth away: for he shall return no more, nor see his native country.\" He died in Egypt, the first Judahite king to die in exile.</p>",
  "hitchcock_meaning": "possession of the Lord",
  "source_ids": {"easton": "jehoahaz", "smith": "jehoahaz", "isbe": "jehoahaz"},
  "key_refs": ["2 Chronicles 21:17", "2 Kings 13:1", "2 Kings 23:31", "Jeremiah 22:11"]
},
"jehoash": {
  "id": "jehoash", "term": "Jehoash", "category": "people",
  "intro": "<p>Jehoash (also Joash; meaning <em>fire of the LORD</em>) was the name of two kings. (1.) Jehoash king of Judah, son of Ahaziah, who was hidden by his aunt Jehosheba in the temple for six years while Athaliah usurped the throne. Restored to power by the priest Jehoiada at age seven, he reigned forty years (c. 835–796 B.C.) and oversaw the repair of the temple — but after Jehoiada's death fell into idolatry and had Zechariah, Jehoiada's son and a prophet, stoned (<a class=\"ref\" data-ref=\"2 Kings 11:13\">2 Kings 12</a>; 2 Chronicles 24). (2.) Jehoash king of Israel, son of Jehoahaz, who reigned c. 798–782 B.C., recovered territory from Syria as Elisha prophesied, and defeated Amaziah of Judah (<a class=\"ref\" data-ref=\"2 Kings 14:1\">2 Kings 13:10-25; 14:1-16</a>).</p><p>The death-bed scene between Elisha and Jehoash of Israel is particularly vivid: the prophet commands the king to shoot arrows eastward (a prophetic acted oracle of victory), then strike the ground — but the king strikes only three times, drawing the prophet's rebuke that he will defeat Syria only three times rather than completely (2 Kings 13:14-19).</p>",
  "hitchcock_meaning": "fire of the Lord",
  "source_ids": {"easton": "jehoash", "smith": "jehoash"},
  "key_refs": ["2 Kings 11:13", "2 Kings 12:2", "2 Kings 13:14", "2 Kings 14:1"]
},
"jehohanan": {
  "id": "jehohanan", "term": "Jehohanan", "category": "people",
  "intro": "<p>Jehohanan (meaning <em>grace</em> or <em>gift of the LORD</em>; the same name as John/Johanan) was borne by at least six individuals in the Old Testament. Notable bearers include: a Levite gatekeeper son of Meshelemiah (<a class=\"ref\" data-ref=\"1 Chronicles 26:3\">1 Chronicles 26:3</a>); a military commander under Jehoshaphat, commanding 280,000 men of Judah (<a class=\"ref\" data-ref=\"2 Chronicles 17:15\">2 Chronicles 17:15</a>); a chief of Ephraim who joined in releasing the Judahite captives brought back by Pekah's army (<a class=\"ref\" data-ref=\"2 Chronicles 28:12\">2 Chronicles 28:12</a>); and a Levitical singer and a priest during the time of Nehemiah (<a class=\"ref\" data-ref=\"Nehemiah 12:42\">Nehemiah 12:42</a>).</p><p>The name is the long form of the name ultimately shortened to Johanan, John (<em>Ioannes</em> in Greek), one of the most common Jewish names by the Second Temple period. Its meaning — grace of the LORD — was theologically apt for a name that became central to New Testament narrative through John the Baptist and the apostle John.</p>",
  "hitchcock_meaning": "grace, or mercy, or gift, of the Lord",
  "source_ids": {"easton": "jehohanan", "smith": "jehohanan", "isbe": "jehohanan"},
  "key_refs": ["1 Chronicles 26:3", "2 Chronicles 17:15", "Nehemiah 12:42"]
},
"jehoiachin": {
  "id": "jehoiachin", "term": "Jehoiachin", "category": "people",
  "intro": "<p>Jehoiachin (meaning <em>preparation</em> or <em>strength of the LORD</em>; also called Jeconiah and Coniah) was king of Judah who reigned only three months before surrendering to Nebuchadnezzar of Babylon in 597 B.C. (<a class=\"ref\" data-ref=\"2 Chronicles 36:9\">2 Chronicles 36:9-10</a>; 2 Kings 24:8-16). At eighteen years old he was taken captive to Babylon along with the temple treasures and 10,000 of Jerusalem's leading citizens — the first major deportation. He spent thirty-seven years in a Babylonian prison.</p><p>The narrative of Jehoiachin's fate takes a remarkable turn: after Nebuchadnezzar's death, his successor Evil-merodach released Jehoiachin from prison, gave him a seat of honor above all other captive kings, and provided him with a regular allowance for the rest of his life (<a class=\"ref\" data-ref=\"Jeremiah 52:28\">Jeremiah 52:28-34</a>; 2 Kings 25:27-30). This closing scene of 2 Kings — the elevation of the Davidic heir — has been read as a sign of hope for the Davidic promise's survival even in exile. Matthew's genealogy of Jesus includes Jehoiachin (\"Jechoniah\") in the line of David (Matthew 1:11-12).</p>",
  "hitchcock_meaning": "preparation, or strength, of the Lord",
  "source_ids": {"easton": "jehoiachin", "smith": "jehoiachin", "isbe": "jehoiachin"},
  "key_refs": ["2 Chronicles 36:9", "2 Kings 24:12", "Jeremiah 52:28", "Matthew 1:11"]
},
"jehoiada": {
  "id": "jehoiada", "term": "Jehoiada", "category": "people",
  "intro": "<p>Jehoiada (meaning <em>knowledge of the LORD</em>) was the high priest of Jerusalem whose decisive action preserved the Davidic dynasty and the Mosaic faith during the usurpation of Athaliah. After Athaliah seized the throne and attempted to kill all the royal heirs, Jehoiada's wife Jehosheba (his niece) hid the infant Joash in the temple for six years. In the seventh year, Jehoiada organized the palace guard and Levites, presented the child king, executed Athaliah, and destroyed the temple of Baal — restoring both the monarchy and true worship in a single coup (<a class=\"ref\" data-ref=\"2 Kings 12:2\">2 Kings 11-12</a>; 2 Chronicles 22-24).</p><p>Jehoiada served as regent and spiritual guide during Joash's minority and lived to 130 years (<a class=\"ref\" data-ref=\"2 Chronicles 22:11\">2 Chronicles 24:15</a>) — a longevity honored with royal burial in the city of David \"because he had done good in Israel.\" After his death, the king reverted to idolatry and had Jehoiada's son Zechariah stoned for his prophetic rebuke — a sin for which Joash later suffered assassination. Jehoiada stands as one of the Old Testament's great priestly figures: a keeper of the covenant when the throne failed.</p>",
  "hitchcock_meaning": "knowledge of the Lord",
  "source_ids": {"easton": "jehoiada", "smith": "jehoiada", "isbe": "jehoiada"},
  "key_refs": ["2 Samuel 8:18", "2 Kings 12:2", "2 Chronicles 22:11", "2 Chronicles 24:15"]
},
"jehoiakim": {
  "id": "jehoiakim", "term": "Jehoiakim", "category": "people",
  "intro": "<p>Jehoiakim (meaning <em>the LORD establishes</em> or <em>the LORD raises up</em>), originally named Eliakim, was king of Judah (c. 609–598 B.C.), appointed by Pharaoh Neco after deposing his brother Jehoahaz. He was a vassal first to Egypt then to Babylon and is among the most negatively portrayed kings in the Old Testament. The prophet Jeremiah repeatedly condemned him: he burned Jeremiah's scroll scroll as it was read to him in the winter house, cutting off sections and throwing them into the fire (<a class=\"ref\" data-ref=\"Jeremiah 36:23\">Jeremiah 36</a>), and he was guilty of forced labor, unjust building projects, and shedding innocent blood (Jeremiah 22:13-17).</p><p>Daniel and his companions were taken to Babylon in the first deportation during Jehoiakim's reign (<a class=\"ref\" data-ref=\"Jeremiah 22:10\">Daniel 1:1-2</a>). Jeremiah prophesied that Jehoiakim would be \"buried with the burial of a donkey\" — thrown outside Jerusalem's gates (<a class=\"ref\" data-ref=\"2 Kings 23:34\">Jeremiah 22:19</a>). His eleven-year reign represents the accelerating spiritual and political collapse of the Judean state in the years before the final destruction of Jerusalem.</p>",
  "hitchcock_meaning": "avenging, or establishing, or resurrection, of the Lord",
  "source_ids": {"easton": "jehoiakim", "smith": "jehoiakim", "isbe": "jehoiakim"},
  "key_refs": ["2 Kings 23:34", "Jeremiah 22:10", "Jeremiah 36:23", "Daniel 1:1"]
},
"jehoiarib": {
  "id": "jehoiarib", "term": "Jehoiarib", "category": "people",
  "intro": "<p>Jehoiarib (meaning <em>the LORD defends</em> or <em>the LORD fights</em>) was the head of the first of the twenty-four priestly divisions established by David for rotation of service at the sanctuary (<a class=\"ref\" data-ref=\"1 Chronicles 24:7\">1 Chronicles 24:7</a>). A Jehoiarib (or Joiarib) is also listed among the priests who returned from Babylon with Zerubbabel (<a class=\"ref\" data-ref=\"Nehemiah 7:39\">Nehemiah 12:6, 19</a>).</p><p>The name gained historical significance in the Maccabean period: the priestly family of the Maccabees (Hasmoneans) was of the Jehoiarib/Joarib course (1 Maccabees 2:1), which explains why Mattathias and his sons were so celebrated in priestly terms. The twenty-four priestly courses established by David and named in 1 Chronicles 24 became the organizational backbone of Second Temple Judaism, each course serving two weeks per year plus the great festivals.</p>",
  "hitchcock_meaning": "fighting, or multiplying, of the Lord",
  "source_ids": {"easton": "jehoiarib", "smith": "jehoiarib", "isbe": "jehoiarib"},
  "key_refs": ["1 Chronicles 9:10", "1 Chronicles 24:7", "Nehemiah 7:39"]
},
"jehonadab": {
  "id": "jehonadab", "term": "Jehonadab", "category": "people",
  "intro": "<p>Jehonadab (also Jonadab; meaning <em>the LORD is liberal</em> or <em>free giver</em>) was the son of Rechab and the founder of the Rechabite community. He commanded his descendants to drink no wine, build no houses, sow no seed, and live in tents — a covenant of nomadic simplicity and separation from the corruptions of Canaanite settled life. Jeremiah 35 records that the Rechabites, tested 250 years after Jonadab's time, remained faithful to his commands even while the rest of Judah ignored God's prophets — making them a powerful object lesson of covenant loyalty.</p><p>An earlier Jehonadab appears as a nephew of David: in 2 Samuel 13:3, Jonadab (a different person, but the same name) was the crafty counselor who advised the lovesick Amnon. The Rechabite founder is first mentioned joining Jehu's purge of the house of Ahab (<a class=\"ref\" data-ref=\"Jeremiah 35:6\">2 Kings 10:15-17</a>), where Jehu called him up into his chariot as a witness — suggesting Jehonadab was a recognized reformer and opponent of Baal worship. His descendants maintained their covenant fidelity to at least the time of Jeremiah (<a class=\"ref\" data-ref=\"Jeremiah 35:6\">Jeremiah 35:6</a>).</p>",
  "hitchcock_meaning": "Jonadab, free giver; liberality",
  "source_ids": {"easton": "jehonadab", "smith": "jehonadab", "isbe": "jehonadab"},
  "key_refs": ["2 Kings 10:15", "Jeremiah 35:6", "Jeremiah 35:18"]
},
"jehonathan": {
  "id": "jehonathan", "term": "Jehonathan", "category": "people",
  "intro": "<p>Jehonathan (meaning <em>gift of the LORD</em>; a long form of Jonathan) is the name of three minor biblical figures. A Levite teacher sent by Jehoshaphat to teach the law in the cities of Judah (<a class=\"ref\" data-ref=\"2 Chronicles 17:8\">2 Chronicles 17:8</a>); a son of Uzziah who served as overseer of David's storehouses (<a class=\"ref\" data-ref=\"1 Chronicles 27:25\">1 Chronicles 27:25</a>); and a priestly family name in the time of Nehemiah (<a class=\"ref\" data-ref=\"Nehemiah 12:18\">Nehemiah 12:18</a>).</p><p>The name is the fuller form of the famous Jonathan (Saul's son, David's covenant friend), and means the same — the LORD has given. The Levite teacher sent by Jehoshaphat reflects the king's notable initiative in establishing systematic instruction in the law throughout Judah, a reform the Chronicler presents as the foundation of Jehoshaphat's otherwise faithful reign.</p>",
  "hitchcock_meaning": "gift of the Lord; gift of a dove",
  "source_ids": {"easton": "jehonathan", "smith": "jehonathan", "isbe": "jehonathan"},
  "key_refs": ["1 Chronicles 27:25", "2 Chronicles 17:8", "Nehemiah 12:18"]
},
"jehoram": {
  "id": "jehoram", "term": "Jehoram", "category": "people",
  "intro": "<p>Jehoram (meaning <em>exaltation of the LORD</em>; also called Joram) was the name of two contemporary kings who ruled Israel and Judah simultaneously. (1.) Jehoram king of Israel, son of Ahab and Jezebel, who reigned c. 852–841 B.C. He removed the pillar of Baal his father had made but continued Jeroboam's sins. His reign saw the Moabite revolt, the ministry of Elisha, and the miraculous Syrian siege of Samaria. He was ultimately shot by Jehu and his body thrown on Naboth's field — a direct fulfillment of Elijah's prophecy (2 Kings 9:24-26). (2.) Jehoram king of Judah, son of Jehoshaphat, who reigned c. 848–841 B.C. He killed his brothers and led Judah into Baal worship under the influence of his wife Athaliah, daughter of Ahab. Elijah sent him a written prophecy of judgment, and he died of a painful intestinal disease (<a class=\"ref\" data-ref=\"2 Kings 1:17\">2 Chronicles 21</a>).</p><p>The reigns of these two Jehorams represent the peak of Omride influence in Judah through the marriage alliance, a theological crisis resolved by Jehu's purge and Jehoiada's counter-coup.</p>",
  "hitchcock_meaning": "exaltation of the Lord",
  "source_ids": {"easton": "jehoram", "smith": "jehoram"},
  "key_refs": ["2 Kings 1:17", "2 Kings 3:1", "2 Kings 9:24", "2 Chronicles 21:4"]
},
"jehoshaphat": {
  "id": "jehoshaphat", "term": "Jehoshaphat", "category": "people",
  "intro": "<p>Jehoshaphat (meaning <em>the LORD is judge</em>) was the fourth king of Judah (c. 873–848 B.C.), son of Asa, and one of the most favorably evaluated kings in the Deuteronomistic history. He removed the high places and Asherah poles, sent Levites and priests throughout Judah to teach the law, established judges in the land with explicit instructions to judge fairly in the fear of the LORD, and strengthened the military defenses of his kingdom (<a class=\"ref\" data-ref=\"2 Chronicles 17:1\">2 Chronicles 17</a>). His administrative and religious reforms are the most detailed of any Judahite king before Hezekiah.</p><p>His reign is marked by a remarkable prayer of faith before battle (2 Chronicles 20), where outnumbered by Moabites, Ammonites, and others, he led Judah in fasting and prayer, received a prophetic word, and sent singers ahead of the army praising God — whereupon the enemy forces turned on one another. His primary fault was his alliance with the house of Ahab through his son's marriage to Athaliah, which brought Baal worship into Judah. He also held court that decided the dispute between Ahab and Naboth's heirs. The Valley of Jehoshaphat (Joel 3:2, 12) bears his name as the site of eschatological judgment.</p>",
  "hitchcock_meaning": "the Lord is judge",
  "source_ids": {"easton": "jehoshaphat", "smith": "jehoshaphat"},
  "key_refs": ["2 Chronicles 17:1", "2 Chronicles 20:3", "2 Samuel 8:16", "Joel 3:2"]
},
"jehoshaphat-valley-of": {
  "id": "jehoshaphat-valley-of", "term": "Jehoshaphat, Valley of", "category": "places",
  "intro": "<p>The Valley of Jehoshaphat is the name given in Joel 3:2 and 3:12 to the site where God declares he will gather all nations for judgment: \"I will gather all nations and bring them down to the Valley of Jehoshaphat. There I will put them on trial\" (<a class=\"ref\" data-ref=\"Joel 3:2\">Joel 3:2</a>). The name means \"the LORD judges\" and may function as a symbolic or theological title rather than a specific geographical location — a place of divine verdict rather than a place on a map.</p><p>From at least the fourth century A.D., Christian and Jewish tradition has identified the Valley of Jehoshaphat with the Kidron Valley between Jerusalem and the Mount of Olives, and this remains the popular identification in modern times. The valley contains extensive ancient cemeteries, as both Jews and Muslims have sought burial near the traditional site of the final judgment. Whether or not Joel intended a specific location, the theological image — all nations gathered before the LORD for accounting — became a standard element of eschatological expectation in both Jewish and Christian interpretation.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jehoshaphat-valley-of", "smith": "jehoshaphat-valley-of", "isbe": "jehoshaphat-valley-of"},
  "key_refs": ["Joel 3:2", "Joel 3:12"]
},
"jehosheba": {
  "id": "jehosheba", "term": "Jehosheba", "category": "people",
  "intro": "<p>Jehosheba (meaning <em>fullness</em> or <em>oath of the LORD</em>; also Jehoshabeath in Chronicles) was the daughter of King Joram of Judah, sister of King Ahaziah, and wife of the high priest Jehoiada. When Athaliah seized power after Ahaziah's death and attempted to destroy all the royal offspring of Judah, it was Jehosheba who rescued the infant Joash — Ahaziah's son — from among those being killed, hiding him and his nurse in a bedroom of the temple for six years (<a class=\"ref\" data-ref=\"2 Chronicles 22:11\">2 Chronicles 22:11</a>; 2 Kings 11:2).</p><p>Jehosheba's act of courage preserved the Davidic line at its most vulnerable moment. Without her intervention, the line of David would have been extinguished in Judah by a usurping queen. Her position as both royal daughter and high priest's wife gave her unique access that made the concealment possible. She is one of the pivotal women in the Old Testament's narrative of covenant continuity, though she appears in only two brief references.</p>",
  "hitchcock_meaning": "fullness, or oath, of the Lord",
  "source_ids": {"easton": "jehosheba", "smith": "jehosheba", "isbe": "jehosheba"},
  "key_refs": ["2 Chronicles 22:11", "2 Kings 11:2"]
},
"jehovah": {
  "id": "jehovah", "term": "Jehovah", "category": "concepts",
  "intro": "<p>Jehovah is the traditional English rendering of the sacred four-letter name of God in Hebrew (<em>YHWH</em>, the Tetragrammaton). It is the distinctive, personal name of the God of Israel — not a mere title or appellative — by which he revealed himself to the patriarchs and, more fully, to Moses: \"I am the LORD [YHWH]. I appeared to Abraham, to Isaac, and to Jacob as God Almighty, but by my name the LORD [YHWH] I did not make myself fully known to them\" (<a class=\"ref\" data-ref=\"Exodus 6:2\">Exodus 6:2-3</a>). The name is connected with the verb \"to be\" (<em>hayah</em>): God revealed it at the burning bush as \"I AM WHO I AM\" (<a class=\"ref\" data-ref=\"Exodus 3:14\">Exodus 3:14</a>), expressing his self-existence, absolute being, and covenant faithfulness.</p><p>Because of the prohibition against taking God's name in vain (<a class=\"ref\" data-ref=\"Leviticus 24:16\">Leviticus 24:16</a>), Jewish tradition ceased pronouncing <em>YHWH</em> and substituted <em>Adonai</em> (Lord) when reading. The form \"Jehovah\" arose in the Middle Ages by combining the consonants of YHWH with the vowels of Adonai. Modern scholarship generally reconstructs the pronunciation as \"Yahweh.\" The name expresses God's eternal, unchanging nature: \"I the LORD do not change\" (<a class=\"ref\" data-ref=\"Malachi 3:6\">Malachi 3:6</a>).</p>",
  "hitchcock_meaning": "self-subsisting",
  "source_ids": {"easton": "jehovah", "smith": "jehovah", "isbe": "jehovah"},
  "key_refs": ["Exodus 6:2", "Exodus 3:14", "Leviticus 24:16", "Malachi 3:6"]
},
"jehovah-jireh": {
  "id": "jehovah-jireh", "term": "Jehovah-jireh", "category": "concepts",
  "intro": "<p>Jehovah-jireh (meaning <em>the LORD will see</em>, or <em>the LORD will provide</em>) is the name Abraham gave to the mountain in the land of Moriah where God provided a ram in place of Isaac at the moment of sacrifice (<a class=\"ref\" data-ref=\"Genesis 22:14\">Genesis 22:14</a>). The Hebrew verb <em>ra'ah</em> (to see) carries the double sense of seeing a need and providing for it — God sees the situation and provides what is required.</p><p>The name enshrined a theological principle that became proverbial: \"On the mount of the LORD it will be provided\" (Genesis 22:14). The ram caught in the thicket was understood from earliest times as a type of the substitutionary sacrifice that God himself would provide — the Lamb of God. The location, identified with Mount Moriah, is the same ridge on which the Jerusalem temple would later be built (2 Chronicles 3:1), linking Abraham's binding of Isaac, the Levitical sacrificial system, and ultimately Christ's crucifixion at the same site under one theological narrative of divine provision through substitutionary death.</p>",
  "hitchcock_meaning": "the Lord will provide",
  "source_ids": {"easton": "jehovah-jireh", "isbe": "jehovah-jireh"},
  "key_refs": ["Genesis 22:14"]
},
"jehovah-nissi": {
  "id": "jehovah-nissi", "term": "Jehovah-nissi", "category": "concepts",
  "intro": "<p>Jehovah-nissi (meaning <em>the LORD is my banner</em>) is the name Moses gave to the altar he erected after Israel's victory over the Amalekites at Rephidim (<a class=\"ref\" data-ref=\"Exodus 17:15\">Exodus 17:15</a>). The battle was Israel's first military engagement after the Exodus, and it was won not by Israelite military power but by the uplifted hands of Moses — whenever his hands were raised, Israel prevailed; when they fell, Amalek prevailed. Aaron and Hur supported his hands until sunset, and Joshua defeated Amalek.</p><p>The name commemorates that God, not human strength, is the standard around which Israel rallies in battle. The <em>nes</em> (banner or standard) was the rallying point for armies in ancient warfare; to declare \"the LORD is my banner\" is to claim God as the ground of military confidence and the source of victory. Isaiah 11:10 and 11:12 develop this image eschatologically: the root of Jesse will stand as a banner for the nations, and God will raise a standard to gather the scattered of Israel — pointing toward the messianic gathering under Christ.</p>",
  "hitchcock_meaning": "the Lord my banner",
  "source_ids": {"easton": "jehovah-nissi", "isbe": "jehovah-nissi"},
  "key_refs": ["Exodus 17:15", "Isaiah 11:10", "Isaiah 11:12"]
},
"jehovah-shalom": {
  "id": "jehovah-shalom", "term": "Jehovah-shalom", "category": "concepts",
  "intro": "<p>Jehovah-shalom (meaning <em>the LORD is peace</em>) is the name Gideon gave to the altar he erected at Ophrah in Manasseh on the site where the angel of the LORD appeared to him and commissioned him to deliver Israel from Midian (<a class=\"ref\" data-ref=\"Judges 6:24\">Judges 6:24</a>). The name arose from the angel's parting reassurance: after Gideon had feared death upon realizing he had seen the LORD face to face, God said, \"Peace! Do not be afraid. You are not going to die.\"</p><p>The altar commemorated God's grant of peace in the face of divine encounter — the unexpected grace that comes in place of expected judgment. The name anticipates the messianic title \"Prince of Peace\" (Isaiah 9:6) and the New Testament declaration that through Christ \"we have peace with God\" (Romans 5:1). The connection between divine encounter, the fear of death, and the surprising gift of peace is a recurring pattern in both Testaments that reaches its climax in the resurrection appearances: \"Peace be with you\" (John 20:19, 21, 26).</p>",
  "hitchcock_meaning": "the Lord send peace",
  "source_ids": {"easton": "jehovah-shalom", "isbe": "jehovah-shalom"},
  "key_refs": ["Judges 6:24", "Isaiah 9:6", "Romans 5:1"]
},
"jehovah-shammah": {
  "id": "jehovah-shammah", "term": "Jehovah-shammah", "category": "concepts",
  "intro": "<p>Jehovah-shammah (meaning <em>the LORD is there</em>) is the symbolic name given by Ezekiel in his closing vision to the restored, eschatological Jerusalem: \"And the name of the city from that time on will be: THE LORD IS THERE\" (<a class=\"ref\" data-ref=\"Ezekiel 48:35\">Ezekiel 48:35</a>). The name concludes the entire book of Ezekiel, which opened with the departure of God's glory from Jerusalem (Ezekiel 10-11) and reaches its climax in the vision of the divine glory returning to fill the new temple (Ezekiel 43:1-5).</p><p>The name is profoundly theological: the ultimate blessing of the restored city is not its architectural grandeur, its security, or its prosperity — it is the presence of God himself. This theme, that God's presence among his people is the substance of all covenant blessing, runs through Scripture from Eden (where God walked with Adam) through the tabernacle and temple to the New Testament: \"Behold, the dwelling place of God is with man. He will dwell with them\" (Revelation 21:3). Jehovah-shammah thus stands as an eschatological name for what Revelation 21 calls \"the holy city, the new Jerusalem.\"</p>",
  "hitchcock_meaning": "the Lord is there",
  "source_ids": {"easton": "jehovah-shammah", "isbe": "jehovah-shammah"},
  "key_refs": ["Ezekiel 48:35", "Ezekiel 43:1", "Revelation 21:3"]
},
"jehovah-tsidkenu": {
  "id": "jehovah-tsidkenu", "term": "Jehovah-tsidkenu", "category": "concepts",
  "intro": "<p>Jehovah-tsidkenu (meaning <em>the LORD our righteousness</em>) is the messianic title given to the coming Davidic king in Jeremiah's oracle of hope: \"In his days Judah will be saved and Israel will live in safety. This is the name by which he will be called: The LORD Our Righteousness\" (<a class=\"ref\" data-ref=\"Jeremiah 23:6\">Jeremiah 23:6</a>). The oracle comes in the context of God's promise to raise up a \"righteous Branch\" from David's line to replace the corrupt shepherds who had scattered God's flock. The same name is applied to the restored Jerusalem in Jeremiah 33:16.</p><p>The title is theologically remarkable: it attributes not merely righteousness but the name <em>YHWH</em> itself to the coming king, suggesting his divine identity. Paul's doctrine of imputed righteousness — that in Christ, sinners receive the righteousness of God as a gift through faith (Romans 3:21-22; 2 Corinthians 5:21; 1 Corinthians 1:30: \"Christ Jesus... has become for us wisdom from God — that is, our righteousness\") — is the New Testament fulfillment of Jehovah-tsidkenu: the LORD himself is the righteousness available to his people.</p>",
  "hitchcock_meaning": "the Lord our righteousness",
  "source_ids": {"easton": "jehovah-tsidkenu"},
  "key_refs": ["Jeremiah 23:6", "Jeremiah 33:16", "Romans 3:21", "1 Corinthians 1:30"]
},
"jehozabad": {
  "id": "jehozabad", "term": "Jehozabad", "category": "people",
  "intro": "<p>Jehozabad (meaning <em>the LORD has endowed</em> or <em>the LORD's dowry</em>) is the name of three biblical figures. (1.) A Levitical gatekeeper, son of Obed-edom, appointed in David's organization of the sanctuary (<a class=\"ref\" data-ref=\"1 Chronicles 26:4\">1 Chronicles 26:4</a>). (2.) One of the two servants who assassinated King Joash of Judah after the stoning of Zechariah the prophet (<a class=\"ref\" data-ref=\"2 Kings 12:21\">2 Kings 12:21</a>); Joash was killed in his bed as divine judgment for the blood of Zechariah. (3.) A military commander under Jehoshaphat commanding 180,000 men from Benjamin (<a class=\"ref\" data-ref=\"2 Chronicles 17:18\">2 Chronicles 17:18</a>).</p><p>The assassin Jehozabad is identified as the son of a Moabite woman (2 Kings 12:21), which may reflect the Chronicler's interest in the foreign connections of those who acted against the Davidic line. His action against Joash, however, is presented in the narrative context of Joash's sin in killing Zechariah, making the assassination an instrument of providential retribution.</p>",
  "hitchcock_meaning": "the Lord's dowry; having a dowry",
  "source_ids": {"easton": "jehozabad", "smith": "jehozabad", "isbe": "jehozabad"},
  "key_refs": ["1 Chronicles 26:4", "2 Kings 12:21", "2 Chronicles 17:18"]
},
"jehozadak": {
  "id": "jehozadak", "term": "Jehozadak", "category": "people",
  "intro": "<p>Jehozadak (meaning <em>justice of the LORD</em>; also Josedech or Jozadak) was the high priest of Jerusalem who was taken into exile by Nebuchadnezzar when he destroyed the city in 587/586 B.C. (<a class=\"ref\" data-ref=\"1 Chronicles 6:14\">1 Chronicles 6:14-15</a>). He was the son of Seraiah the chief priest, who was executed at Riblah (2 Kings 25:18-21), and the father of Joshua (Jeshua) the high priest who returned from exile with Zerubbabel and led the restoration of worship in Jerusalem (Ezra 3:2; Haggai 1:1).</p><p>Though Jehozadak himself never served as high priest in Jerusalem — his entire adult life was spent in Babylonian exile — he forms the crucial link in the Zadokite priestly line between the pre-exilic and post-exilic periods. His son Joshua's ministry, alongside Zerubbabel the governor, becomes the subject of significant prophetic attention in Haggai and Zechariah, who saw in their joint leadership a type of the coming Messiah who would be both king and priest.</p>",
  "hitchcock_meaning": "justice of the Lord",
  "source_ids": {"easton": "jehozadak", "smith": "jehozadak", "isbe": "jehozadak"},
  "key_refs": ["1 Chronicles 6:14", "1 Chronicles 6:15", "Ezra 3:2"]
},
"jehu": {
  "id": "jehu", "term": "Jehu", "category": "people",
  "intro": "<p>Jehu (meaning <em>the LORD is he</em>) was the military commander of Israel who was anointed by a prophet sent by Elisha to be king and to execute divine judgment on the house of Ahab (<a class=\"ref\" data-ref=\"1 Kings 16:1\">2 Kings 9-10</a>; 1 Kings 19:16). In a sweeping purge, Jehu killed King Joram of Israel, King Ahaziah of Judah, Jezebel the queen mother, all seventy sons of Ahab, the Baal priests, and all Ahab's officials and associates — fulfilling to the letter the judgment pronounced by Elijah. He reigned over Israel approximately 841–814 B.C.</p><p>Jehu is theologically complex: God commended his execution of Ahab's house as faithful obedience (2 Kings 10:30), yet Hosea 1:4 declares that God will punish the house of Jehu for \"the blood of Jezreel\" — suggesting the manner of the purge exceeded proper bounds, or that Jehu's own subsequent failures negated the commendation. Though he eliminated Baal worship from Israel, he continued the golden calves of Jeroboam and did not follow the LORD with all his heart. His dynasty was the longest in Israel's northern kingdom, lasting four generations.</p>",
  "hitchcock_meaning": "himself who exists",
  "source_ids": {"easton": "jehu", "smith": "jehu", "isbe": "jehu"},
  "key_refs": ["1 Kings 16:1", "2 Kings 9:6", "2 Kings 10:30", "Hosea 1:4"]
},
"jehucal": {
  "id": "jehucal", "term": "Jehucal", "category": "people",
  "intro": "<p>Jehucal (also Jucal; meaning <em>mighty</em> or <em>perfect</em>) was an official of King Zedekiah of Judah who, together with the priest Pashhur, was sent to Jeremiah to ask the prophet to pray for Judah as Babylon threatened the city (<a class=\"ref\" data-ref=\"Jeremiah 37:3\">Jeremiah 37:3</a>). He later appears among the princes who heard Jeremiah's counsel that the city should surrender to Babylon and had the prophet thrown into a muddy cistern to silence him (<a class=\"ref\" data-ref=\"Jeremiah 38:1\">Jeremiah 38:1</a>).</p><p>Jehucal represents the court officials who selectively approached Jeremiah when convenient but suppressed his message when it conflicted with their political interests. His sending to ask for prayer while simultaneously opposing the prophet's call to surrender illustrates the hollow religious instrumentalism of Zedekiah's court in Jerusalem's final years.</p>",
  "hitchcock_meaning": "mighty; perfect; wasted",
  "source_ids": {"easton": "jehucal", "smith": "jehucal", "isbe": "jehucal"},
  "key_refs": ["Jeremiah 37:3", "Jeremiah 38:1"]
},
"jehudi": {
  "id": "jehudi", "term": "Jehudi", "category": "people",
  "intro": "<p>Jehudi was an official of Jehoiakim's court who read the scroll of Jeremiah's prophecies aloud to the king as it was unrolled, and whom the king sent to retrieve the scroll from Baruch (<a class=\"ref\" data-ref=\"Jeremiah 36:14\">Jeremiah 36:14, 21</a>). As Jehudi read each three or four columns, Jehoiakim cut them off with a penknife and threw them into the fire — a deliberate, contemptuous destruction of the prophetic word.</p><p>Jehudi's role is that of an unwitting instrument in one of the most dramatic scenes of prophetic history: the burning of Jeremiah's scroll. His name means \"a Jew\" or \"belonging to Judah\" and his genealogy is traced four generations back (Jeremiah 36:14), suggesting he was a notable court figure. The episode immediately provokes God's command to Jeremiah to dictate a new scroll — and to add further judgments against Jehoiakim who had burned the first.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jehudi", "smith": "jehudi", "isbe": "jehudi"},
  "key_refs": ["Jeremiah 36:14", "Jeremiah 36:21"]
},
"jeiel": {
  "id": "jeiel", "term": "Jeiel", "category": "people",
  "intro": "<p>Jeiel is the name of several minor figures in Chronicles, including a Levite musician appointed by David to play the harp before the ark (<a class=\"ref\" data-ref=\"1 Chronicles 16:5\">1 Chronicles 16:5</a>), a Levite of the sons of Asaph who participated in the temple cleansing under Hezekiah (<a class=\"ref\" data-ref=\"2 Chronicles 29:13\">2 Chronicles 29:13</a>), and a military secretary under King Uzziah who kept records of the army (<a class=\"ref\" data-ref=\"2 Chronicles 26:11\">2 Chronicles 26:11</a>). The ancestor of King Saul named Jeiel (or Abiel) is also mentioned in 1 Chronicles 9:35 and 8:29.</p><p>The name (related to a root meaning \"God carries away\" or \"God heaps up\") was common enough to belong to many unrelated individuals. Their appearances throughout Chronicles reflect that book's thorough attention to the Levitical personnel, military officials, and genealogical records of the Israelite community.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jeiel", "smith": "jeiel", "isbe": "jeiel"},
  "key_refs": ["1 Chronicles 9:35", "1 Chronicles 16:5", "2 Chronicles 26:11"]
},
"jemima": {
  "id": "jemima", "term": "Jemima", "category": "names",
  "intro": "<p>Jemima (meaning <em>handsome as the day</em>, or possibly <em>dove</em> from an Arabic cognate) was the eldest of the three daughters born to Job after his restoration from affliction (<a class=\"ref\" data-ref=\"Job 42:14\">Job 42:14</a>). Her sisters were Kezia and Keren-happuch — all three names suggesting beauty and fragrance. The text explicitly notes that these daughters were the most beautiful women in all the land and that their father gave them an inheritance along with their brothers, an unusual provision that reflects Job's restored prosperity and generosity.</p><p>The names of Job's restored daughters are preserved while the names of his first daughters (who died in the catastrophe) are not — perhaps signaling that the restored life, though not identical to what was lost, is named and particular. The daughters' inheritance alongside the sons is a notable legal detail suggesting the wealth of the restoration exceeded convention. The book of Job concludes with Job living 140 more years and seeing four generations of descendants.</p>",
  "hitchcock_meaning": "handsome as the day",
  "source_ids": {"easton": "jemima", "smith": "jemima"},
  "key_refs": ["Job 42:14"]
},
"jephthah": {
  "id": "jephthah", "term": "Jephthah", "category": "people",
  "intro": "<p>Jephthah (meaning <em>whom God sets free</em> or <em>breaker through</em>) was a judge of Israel from Gilead (east of the Jordan), son of a harlot, who was driven out by his half-brothers but became a military leader of the displaced. When the Ammonites threatened Israel, the elders of Gilead appealed to Jephthah for help, and after diplomatic negotiations with Ammon failed, he led Israel to a crushing victory (<a class=\"ref\" data-ref=\"Judges 11:1\">Judges 11:1-33</a>). He judged Israel for six years.</p><p>Jephthah's vow — that he would sacrifice whatever first came through his door if God gave him victory — and its tragic fulfillment when his daughter came out dancing is one of the most debated narratives in the Old Testament (see Jephthah's Vow). Despite this, the New Testament includes him in the roll of faith's heroes (Hebrews 11:32), acknowledging his trust in God as judge between Israel and Ammon. His story also involves the Shibboleth episode (Judges 12:1-6), where fleeing Ephraimites were identified and killed at the Jordan fords by their inability to pronounce the word.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jephthah", "smith": "jephthah", "isbe": "jephthah"},
  "key_refs": ["Judges 11:1", "Judges 11:33", "Hebrews 11:32"]
},
"jephthahs-vow": {
  "id": "jephthahs-vow", "term": "Jephthah's Vow", "category": "events",
  "intro": "<p>Jephthah's vow (Judges 11:30-40) was a conditional promise made before battle against Ammon: if God gave him victory, he would sacrifice as a burnt offering whatever first came out of his door to meet him on his return. The victory was won, and his daughter — his only child — was the first to emerge, dancing with tambourines. She accepted her fate, asking only for two months to mourn her virginity with her friends in the mountains. After two months she returned, and Jephthah \"did to her as he had vowed.\"</p><p>The theological interpretation of this vow has divided commentators for centuries. The two main positions are: (1) Jephthah literally sacrificed his daughter as a burnt offering — a horrible act, but the text is silent on divine approval or disapproval, and human sacrifice was condemned in the law (Leviticus 18:21; 20:2; Deuteronomy 12:31). (2) Jephthah consecrated his daughter to lifelong virginity in temple service — the daughter's mourning of her <em>virginity</em> rather than her impending death supporting this reading. The annual four-day mourning custom established by Israelite women (Judges 11:40) fits either interpretation. The episode illustrates the moral disorder of the judges period.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jephthahs-vow"},
  "key_refs": ["Judges 11:30", "Judges 11:31", "Judges 11:39", "Leviticus 18:21"]
},
"jephunneh": {
  "id": "jephunneh", "term": "Jephunneh", "category": "people",
  "intro": "<p>Jephunneh (meaning <em>he that beholds</em>) was the father of Caleb the spy from the tribe of Judah (<a class=\"ref\" data-ref=\"Numbers 13:6\">Numbers 13:6</a>; Joshua 14:14). He is called a Kenizzite in some passages (Numbers 32:12; Joshua 14:6, 14), suggesting either a Kenizzite ancestry absorbed into Judah or an alternative tribal identification. The name identifies him primarily in relation to his more famous son.</p><p>Caleb son of Jephunneh was one of the two spies (with Joshua) who brought back a faithful report from Canaan and urged Israel to trust God and enter the land, in contrast to the ten spies who incited the people's fear. For this faith, God promised that Caleb alone among that generation would enter and inherit the land. At eighty-five he still claimed his portion — the hill country of Hebron — driving out the Anakim and taking possession of what Moses had promised him (<a class=\"ref\" data-ref=\"Joshua 14:14\">Joshua 14:14</a>).</p>",
  "hitchcock_meaning": "he that beholds",
  "source_ids": {"easton": "jephunneh", "smith": "jephunneh", "isbe": "jephunneh"},
  "key_refs": ["Numbers 13:6", "Joshua 14:14"]
},
"jerahmeel": {
  "id": "jerahmeel", "term": "Jerahmeel", "category": "people",
  "intro": "<p>Jerahmeel (meaning <em>the mercy</em> or <em>the beloved of God</em>) was primarily the eldest son of Hezron, a grandson of Judah and Tamar, and the eponymous ancestor of the Jerahmeelites — a clan in the Negev south of Judah that David had contact with during his time as a fugitive (<a class=\"ref\" data-ref=\"1 Chronicles 2:9\">1 Chronicles 2:9, 25-26</a>). The Jerahmeelites are mentioned in 1 Samuel 27:10 and 30:29 as one of the southern groups in whose territory David operated while at Ziklag.</p><p>A second Jerahmeel was a son of Kish the Merarite Levite who served in the temple service (1 Chronicles 24:29). A third was an official sent by Jehoiakim to arrest Jeremiah and Baruch after the scroll-burning episode (Jeremiah 36:26). The various Jerahmeels illustrate how a theophoric name meaning \"God's mercy\" was distributed widely across different families and periods.</p>",
  "hitchcock_meaning": "the mercy, or the beloved, of God",
  "source_ids": {"easton": "jerahmeel", "smith": "jerahmeel"},
  "key_refs": ["1 Chronicles 2:9", "1 Chronicles 2:25", "Jeremiah 36:26"]
},
"jeremiah": {
  "id": "jeremiah", "term": "Jeremiah", "category": "people",
  "intro": "<p>Jeremiah (meaning <em>the LORD exalts</em> or <em>appointed by the LORD</em>) was the great prophet of Judah's final decades, called from the womb (Jeremiah 1:5) and active from the thirteenth year of Josiah (c. 627 B.C.) through the destruction of Jerusalem in 587/586 B.C. and its immediate aftermath. Son of a priest from Anathoth in Benjamin, he ministered through the reigns of Josiah, Jehoahaz, Jehoiakim, Jehoiachin, and Zedekiah — witnessing Josiah's reforms, their reversal, Nebuchadnezzar's rise, and Jerusalem's fall.</p><p>Jeremiah is the most personally revealed prophet in the Old Testament. His \"confessions\" (Jeremiah 11–20) expose his anguish, his resentment of the prophetic calling, and his honest wrestling with God over suffering and divine justice. He proclaimed the new covenant written on hearts (Jeremiah 31:31-34 — the most-quoted OT passage in Hebrews), announced that the exile would last seventy years (Jeremiah 25:11-12), and counseled surrender to Babylon as God's will. For this he was imprisoned, thrown into a cistern, and rejected. After Jerusalem fell, he was taken against his will to Egypt, where tradition holds he died. His book is the longest in the Old Testament.</p>",
  "hitchcock_meaning": "exaltation of the Lord",
  "source_ids": {"easton": "jeremiah", "smith": "jeremiah"},
  "key_refs": ["Jeremiah 1:5", "Jeremiah 25:11", "Jeremiah 31:31", "Hebrews 8:8"]
},
"jeremiah-book-of": {
  "id": "jeremiah-book-of", "term": "Jeremiah, Book of", "category": "concepts",
  "intro": "<p>The Book of Jeremiah is the longest prophetic book in the Old Testament (and the longest book of the Bible by word count), consisting of twenty-three independent sections arranged in five main divisions. It combines biography, autobiography, prophetic oracles, laments, sign-acts, and historical narrative in a way that is notably non-chronological — the Hebrew Masoretic text and the Greek Septuagint version differ substantially in arrangement and length (the LXX is approximately one-eighth shorter and places the oracles against nations differently).</p><p>The book records Jeremiah's call, his preaching against Judah's idolatry and covenant violation, his temple sermon (Jeremiah 7; 26), his proclamation of the new covenant (Jeremiah 31), his purchase of a field in Anathoth as a symbolic act of hope during the Babylonian siege (Jeremiah 32), his suffering under Jehoiakim and Zedekiah, the fall of Jerusalem, and his forced exile to Egypt. The oracles against foreign nations (Jeremiah 46–51) form a major section. The book had profound influence on the New Testament — particularly the new covenant passage cited in Hebrews 8–10 — and on post-exilic Jewish theological reflection on sin, judgment, and future restoration.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jeremiah-book-of", "smith": "jeremiah-book-of"},
  "key_refs": ["Jeremiah 1:1", "Jeremiah 31:31", "Jeremiah 25:11", "Hebrews 8:8"]
},
"jericho": {
  "id": "jericho", "term": "Jericho", "category": "places",
  "intro": "<p>Jericho (meaning <em>his moon</em> or <em>fragrance</em>) was an ancient fortified city in the Jordan Valley, near the river at its entry into the Dead Sea, approximately 800 feet below sea level — the lowest city in the world. It was surrounded by palm groves and watered by a perennial spring (\"Elisha's Spring\"). The earliest archaeological layers at Tell es-Sultan make Jericho one of the oldest continuously occupied sites in the world, with occupation going back at least 10,000 years.</p><p>Jericho was the first city Israel conquered in Canaan under Joshua — taken by faith, without siege engines, through the miraculous collapse of its walls after seven days of priestly procession and the trumpeting of rams' horns (<a class=\"ref\" data-ref=\"Joshua 6\">Joshua 6</a>). Elisha purified its bitter spring (2 Kings 2:19-22), and the city was rebuilt under Ahab's reign under the curse Joshuah had pronounced (1 Kings 16:34). In the New Testament, Jericho appears in Jesus's encounter with Zacchaeus (Luke 19), the healing of blind Bartimaeus (Mark 10:46), and provides the setting for the parable of the Good Samaritan (Luke 10:30). The \"city of palms\" thus spans from Israel's first military miracle to Jesus's final journey toward Jerusalem.</p>",
  "hitchcock_meaning": "his moon; his month; his sweet smell",
  "source_ids": {"easton": "jericho", "smith": "jericho", "isbe": "jericho"},
  "key_refs": ["Joshua 3:16", "Joshua 6:1", "2 Kings 2:19", "Luke 19:1"]
},
"jerimoth": {
  "id": "jerimoth", "term": "Jerimoth", "category": "people",
  "intro": "<p>Jerimoth (meaning <em>he that fears death</em> or <em>rejects death</em>) is the name of at least eight minor figures in Chronicles, spanning several tribes and periods. The most notable include: Jerimoth son of David, whose daughter Mahalath was a wife of Rehoboam (2 Chronicles 11:18); a Levite musician in David's organization of the sanctuary musicians (<a class=\"ref\" data-ref=\"1 Chronicles 25:4\">1 Chronicles 25:4</a>); and a tribal officer of Naphtali under David (<a class=\"ref\" data-ref=\"1 Chronicles 27:19\">1 Chronicles 27:19</a>).</p><p>The multiple bearers of this name illustrate the Chronicler's interest in comprehensive genealogical records. The connection to David through the marriage of Rehoboam to Jerimoth's daughter Mahalath is particularly notable, as it explains the bloodline of certain later Judahite kings and reflects the web of family alliances in the early monarchy period.</p>",
  "hitchcock_meaning": "he that fears or rejects death",
  "source_ids": {"easton": "jerimoth", "smith": "jerimoth", "isbe": "jerimoth"},
  "key_refs": ["1 Chronicles 7:7", "1 Chronicles 25:4", "1 Chronicles 27:19"]
},
"jeroboam": {
  "id": "jeroboam", "term": "Jeroboam", "category": "people",
  "intro": "<p>Jeroboam was the name of two kings of the northern kingdom of Israel. (1.) Jeroboam I, son of Nebat, was an Ephraimite officer under Solomon who was told by the prophet Ahijah that he would rule ten tribes after Solomon's death (<a class=\"ref\" data-ref=\"1 Kings 11:26\">1 Kings 11:26-39</a>). After Solomon's death, his son Rehoboam's harshness provoked the northern tribes to revolt, and Jeroboam became the first king of Israel (c. 930–910 B.C.). To prevent his people from returning to Jerusalem for worship, he established two golden calves at Bethel and Dan — \"the sin of Jeroboam\" that every subsequent northern king is measured against (1 Kings 12). He also created a rival priesthood and calendar. His religious innovations are condemned as the foundational apostasy that eventually brought down the northern kingdom.</p><p>(2.) Jeroboam II (c. 793–753 B.C.) presided over the longest and most prosperous reign in the northern kingdom, recovering territory from Syria as the prophet Jonah had foretold (2 Kings 14:25). Yet he continued the sins of Jeroboam I. His reign was the context for the prophetic ministries of Amos and Hosea, who indicted the prosperity for its accompanying injustice and spiritual corruption.</p>",
  "hitchcock_meaning": "he that opposes the people",
  "source_ids": {"easton": "jeroboam", "smith": "jeroboam", "isbe": "jeroboam"},
  "key_refs": ["1 Kings 11:26", "1 Kings 12:28", "2 Kings 14:25", "Amos 7:9"]
},
"jeroham": {
  "id": "jeroham", "term": "Jeroham", "category": "people",
  "intro": "<p>Jeroham (meaning <em>high</em>, <em>merciful</em>, or <em>beloved</em>) is the name of several individuals in the Old Testament, most of them minor figures in genealogical lists. The most significant is Jeroham of Ramathaim-zophim, the father of Elkanah and grandfather of Samuel (1 Samuel 1:1) — placing this Jeroham in the direct ancestral line of Israel's great judge-prophet. A Jeroham of Dan was father of Azarel, the tribal leader of Dan under David (<a class=\"ref\" data-ref=\"1 Chronicles 27:22\">1 Chronicles 27:22</a>), and a Jeroham was among the military officers who assisted Jehoiada in placing Joash on the throne (<a class=\"ref\" data-ref=\"2 Chronicles 23:1\">2 Chronicles 23:1</a>).</p><p>Samuel's connection to Jeroham anchors the prophet's lineage in the period of the judges. Samuel is identified as an Ephraimite through his father's residence but elsewhere appears as a Levite (1 Chronicles 6:27-28, 33-34), suggesting either a Levitical family resident in Ephraim or overlapping genealogical traditions.</p>",
  "hitchcock_meaning": "high; merciful; beloved",
  "source_ids": {"easton": "jeroham", "smith": "jeroham", "isbe": "jeroham"},
  "key_refs": ["1 Samuel 1:1", "1 Chronicles 27:22", "2 Chronicles 23:1"]
},
"jerubbaal": {
  "id": "jerubbaal", "term": "Jerubbaal", "category": "people",
  "intro": "<p>Jerubbaal (meaning <em>let Baal contend</em> or <em>Baal will defend his cause</em>) was the surname given to Gideon after he tore down his father's altar of Baal and the Asherah pole at Ophrah (<a class=\"ref\" data-ref=\"Judges 6:32\">Judges 6:32</a>). His father Joash, surprising the townsmen who demanded Gideon's death, argued that if Baal were truly a god he could defend himself. The name Jerubbaal thus ironically memorialized Baal's failure to act against his own desecrator.</p><p>The name is used interchangeably with Gideon throughout the Judges narrative (<a class=\"ref\" data-ref=\"Judges 7:1\">Judges 7:1</a>; 8:29-35) and appears in Samuel's retrospective speech (1 Samuel 12:11). Jerubbesheth, a variant of the name substituting <em>bosheth</em> (shame) for Baal, appears in 2 Samuel 11:21 — a common scribal substitution in later texts to avoid speaking the Baal name. The double name reflects both the historical moment of Gideon's anti-Baal action and the scribal sensitivity about preserving the name of a Canaanite deity in the sacred text.</p>",
  "hitchcock_meaning": "he that defends Baal, let Baal defend his cause",
  "source_ids": {"easton": "jerubbaal", "isbe": "jerubbaal"},
  "key_refs": ["Judges 6:32", "Judges 7:1", "Judges 8:29", "1 Samuel 12:11"]
},
"jerubbesheth": {
  "id": "jerubbesheth", "term": "Jerubbesheth", "category": "people",
  "intro": "<p>Jerubbesheth (meaning <em>let the idol of confusion defend itself</em>) is an alternate form of the name Jerubbaal (Gideon's surname), appearing only once in Scripture — in 2 Samuel 11:21, where Joab's message to David references the death of Abimelech who was killed by a millstone dropped by a woman at Thebez. The reference is to the narrative of Judges 9, where Abimelech, Gideon's son by a concubine, attempted to establish a kingship at Shechem but was fatally wounded by a woman's millstone.</p><p>The substitution of <em>besheth</em> (shame, confusion) for <em>baal</em> (lord) is a scribal practice found in several Old Testament names where the Baal element was considered offensive. Other examples include Ish-bosheth for Eshbaal (Saul's son) and Mephibosheth for Meribbaal (Jonathan's son). This practice illustrates how later scribes and editors worked to remove or neutralize Baal theophoric elements from the names preserved in the text.</p>",
  "hitchcock_meaning": "let the idol of confusion defend itself",
  "source_ids": {"easton": "jerubbesheth", "smith": "jerubbesheth", "isbe": "jerubbesheth"},
  "key_refs": ["2 Samuel 11:21", "Judges 9:50"]
},
"jeruel": {
  "id": "jeruel", "term": "Jeruel", "category": "places",
  "intro": "<p>Jeruel (meaning <em>fear of God</em> or <em>vision of God</em>) was a wilderness area in Judah, east of the Tekoa road, where the prophet Jahaziel declared that Jehoshaphat's outnumbered army would find the invading Moabite-Ammonite coalition (<a class=\"ref\" data-ref=\"2 Chronicles 20:16\">2 Chronicles 20:16</a>). The army was told: \"You will not need to fight in this battle. Position yourselves, stand still and see the salvation of the LORD.\"</p><p>Jehoshaphat led Judah to the wilderness of Jeruel after a night of prayer and fasting, with singers going ahead of the army praising God. When they arrived, the enemy forces had already turned on each other and lay dead (<a class=\"ref\" data-ref=\"2 Chronicles 20:20\">2 Chronicles 20:20-24</a>). Jeruel appears only in this passage and is otherwise unknown — its significance entirely bound up with one of the most remarkable divine deliverances in Chronicles. The site may be in the region southeast of Bethlehem toward the Dead Sea.</p>",
  "hitchcock_meaning": "fear, or vision of God",
  "source_ids": {"easton": "jeruel", "smith": "jeruel", "isbe": "jeruel"},
  "key_refs": ["2 Chronicles 20:16", "2 Chronicles 20:20"]
},
"jerusalem": {
  "id": "jerusalem", "term": "Jerusalem", "category": "places",
  "intro": "<p>Jerusalem (meaning <em>foundation of peace</em> or <em>vision of peace</em>; called also Salem, Jebus, Ariel, and \"the city of God\") is the central city of Scripture and the most theologically significant city in human history. Situated in the hill country of Judah approximately 2,500 feet above sea level, it was captured from the Jebusites by David and made his capital (2 Samuel 5:6-9). Solomon built the first temple there, establishing the city as the permanent dwelling place of God's name and the center of Israelite worship and national identity.</p><p>Jerusalem's theological significance extends through both Testaments. The Psalms celebrate it as the city God loves above all (Psalm 87), the place of his presence (Psalm 46), and the goal of Israel's pilgrimages. The prophets envision it as the center of eschatological gathering (Isaiah 2:2-4; Zechariah 14). In the New Testament, Jesus wept over it (Luke 19:41), was crucified and rose again in its vicinity, and sent his disciples from it (Acts 1:8). Hebrews 12:22 speaks of \"the heavenly Jerusalem,\" and Revelation 21 envisions \"the holy city, new Jerusalem, coming down from God out of heaven\" as the eternal dwelling of God with his redeemed people — the ultimate fulfillment of all that earthly Jerusalem signified.</p>",
  "hitchcock_meaning": "vision of peace",
  "source_ids": {"easton": "jerusalem", "smith": "jerusalem", "isbe": "jerusalem"},
  "key_refs": ["2 Samuel 5:7", "Psalms 46:4", "Luke 19:41", "Revelation 21:2"]
},
"jerusha": {
  "id": "jerusha", "term": "Jerusha", "category": "people",
  "intro": "<p>Jerusha (also Jerushah; meaning <em>possession</em> or <em>inheritance</em>) was the wife of King Uzziah (Azariah) of Judah and the mother of King Jotham (<a class=\"ref\" data-ref=\"2 Kings 15:33\">2 Kings 15:33</a>; 2 Chronicles 27:1). She was the daughter of Zadok, though it is uncertain whether this Zadok was the high priest or another man of the same name. Jotham her son is evaluated as a righteous king who \"did what was right in the eyes of the LORD\" and continued his father Uzziah's building programs.</p><p>Jerusha is one of the queen mothers whose names are preserved in the accession formulae of Kings and Chronicles — a consistent practice that reflects the important role of the queen mother (<em>gebirah</em>) in the Judahite court. Queen mothers held official status, and their names appear in the royal records as part of the dynastic identification of each king.</p>",
  "hitchcock_meaning": "banished; possession; inheritance",
  "source_ids": {"easton": "jerusha", "smith": "jerusha", "isbe": "jerusha"},
  "key_refs": ["2 Kings 15:33"]
},
"jeshaiah": {
  "id": "jeshaiah", "term": "Jeshaiah", "category": "people",
  "intro": "<p>Jeshaiah (meaning <em>salvation of the LORD</em>) is the name of at least five individuals in the Old Testament. The most notable are: a son of Hananiah (grandson of Zerubbabel), in the Davidic genealogy (<a class=\"ref\" data-ref=\"1 Chronicles 3:21\">1 Chronicles 3:21</a>); a musician son of Jeduthun assigned to the eighth division of temple musicians (<a class=\"ref\" data-ref=\"1 Chronicles 25:3\">1 Chronicles 25:3, 15</a>); a Levite descendant of Eliezer who was a leader of the Levitical family that returned from exile with Ezra (<a class=\"ref\" data-ref=\"Ezra 8:7\">Ezra 8:7</a>); and a Levite of the sons of Merari who similarly returned with Ezra (<a class=\"ref\" data-ref=\"1 Chronicles 26:25\">1 Chronicles 26:25</a>).</p><p>The name is closely related to Isaiah (Yeshayahu) and shares the same root meaning. The presence of a Davidic descendant named Jeshaiah in the post-exilic genealogy (1 Chronicles 3:21) is of historical interest, as it shows the Davidic line continued to be traceable into the Second Temple period.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jeshaiah", "smith": "jeshaiah", "isbe": "jeshaiah"},
  "key_refs": ["1 Chronicles 3:21", "1 Chronicles 25:3", "Ezra 8:7"]
},
"jeshanah": {
  "id": "jeshanah", "term": "Jeshanah", "category": "places",
  "intro": "<p>Jeshanah (meaning <em>old</em> or <em>ancient</em>) was a town in the hill country of Ephraim that Abijah king of Judah captured from Jeroboam I along with Bethel and Ephron during the war between the divided kingdoms (<a class=\"ref\" data-ref=\"2 Chronicles 13:19\">2 Chronicles 13:19</a>). It has been tentatively identified with the village of Burj el-Isaneh northeast of Bethel.</p><p>The brief mention of Jeshanah is part of the Chronicler's account of Abijah's victory over Jeroboam, which the Chronicler presents as a divine reward for Abijah's declaration that Judah had not abandoned the LORD and his priesthood (2 Chronicles 13:10-12). The capture of several border towns in Ephraim temporarily extended Judah's territory northward, though these gains did not persist beyond Abijah's reign.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jeshanah", "smith": "jeshanah", "isbe": "jeshanah"},
  "key_refs": ["2 Chronicles 13:19"]
},
"jesharelah": {
  "id": "jesharelah", "term": "Jesharelah", "category": "people",
  "intro": "<p>Jesharelah (also Asharelah; meaning uncertain) was a son of Asaph and head of the seventh division of Levitical musicians established by David for the sanctuary (<a class=\"ref\" data-ref=\"1 Chronicles 25:14\">1 Chronicles 25:14</a>). He and his brothers and sons — fourteen in all — made up his division, serving by lot in the rotation of musical ministry.</p><p>Jesharelah appears only in this one passage. His inclusion reflects the Chronicler's thorough documentation of the twenty-four divisions of temple musicians established by David alongside the priestly courses, ensuring orderly, continuous worship of God in the sanctuary. The name variation (Asharelah in verse 2 vs. Jesharelah in verse 14) may reflect a scribal variant or a longer and shorter form of the same name.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jesharelah", "smith": "jesharelah", "isbe": "jesharelah"},
  "key_refs": ["1 Chronicles 25:14"]
},
"jeshebeab": {
  "id": "jeshebeab", "term": "Jeshebeab", "category": "people",
  "intro": "<p>Jeshebeab (meaning <em>sitting</em> or <em>captivity of the father</em>) was head of the fourteenth division of the twenty-four priestly courses established by David for rotation of service at the sanctuary (<a class=\"ref\" data-ref=\"1 Chronicles 24:13\">1 Chronicles 24:13</a>). He and his group would have served two weeks per year plus the major festivals in the regular rotation of priestly ministry.</p><p>Like many of the priestly division heads in 1 Chronicles 24, Jeshebeab appears only in this organizational list. The twenty-four courses of priests — established here in detail — became the foundational organizational structure of both the Jerusalem temple and later Jewish synagogue practice. By the New Testament period, this system was still operative: Zechariah, father of John the Baptist, served in \"the division of Abijah\" (Luke 1:5; the eighth course).</p>",
  "hitchcock_meaning": "sitting, or captivity, of the father",
  "source_ids": {"easton": "jeshebeab", "smith": "jeshebeab", "isbe": "jeshebeab"},
  "key_refs": ["1 Chronicles 24:13"]
},
"jesher": {
  "id": "jesher", "term": "Jesher", "category": "people",
  "intro": "<p>Jesher (meaning <em>right</em> or <em>upright</em>) was a son of Caleb (son of Hezron) and his wife Azubah, listed in the genealogy of Judah in 1 Chronicles (<a class=\"ref\" data-ref=\"1 Chronicles 2:18\">1 Chronicles 2:18</a>). He appears with his brothers Shobab and Ardon in a brief genealogical record with no further narrative detail.</p><p>Jesher is a minor figure whose sole significance is genealogical — part of the Chronicler's comprehensive reconstruction of the tribe of Judah's lineage. The name's meaning (\"right\" or \"upright\") is characteristic of the theophoric and virtue-naming conventions common in Israelite genealogies.</p>",
  "hitchcock_meaning": "right; singing",
  "source_ids": {"easton": "jesher", "smith": "jesher", "isbe": "jesher"},
  "key_refs": ["1 Chronicles 2:18"]
},
"jeshimon": {
  "id": "jeshimon", "term": "Jeshimon", "category": "places",
  "intro": "<p>Jeshimon (meaning <em>solitude</em> or <em>desolation</em>) refers to the barren waste or desert wilderness — possibly a common noun used as a proper name for particularly desolate regions. The word appears in Numbers 21:20 and 23:28 for the desert overlooked from the peak of Pisgah near the Dead Sea, and in 1 Samuel 23:19, 24 for the wilderness of Judah where David hid during his flight from Saul.</p><p>In the 1 Samuel passages, the Ziphites twice informed Saul that David was hiding \"in the hill of Hachilah, which is on the south of Jeshimon\" — the bleak Judean wilderness near the Dead Sea. The desolate character of the region made it both a refuge and a hardship for fugitives: difficult terrain to search, but harsh terrain to survive in. The Jeshimon thus functions in David's narrative as the wilderness experience of the king in exile, prefiguring his eventual return to power.</p>",
  "hitchcock_meaning": "solitude; desolation",
  "source_ids": {"easton": "jeshimon", "smith": "jeshimon", "isbe": "jeshimon"},
  "key_refs": ["Numbers 21:20", "Numbers 23:28", "1 Samuel 23:19"]
},
"jeshua": {
  "id": "jeshua", "term": "Jeshua", "category": "people",
  "intro": "<p>Jeshua is a later Hebrew form of the name Joshua (meaning <em>salvation of the LORD</em>, the same root as Jesus in Greek). It is borne by several post-exilic figures, most importantly: (1.) Joshua/Jeshua the high priest, son of Jehozadak, who returned from Babylon with Zerubbabel and led the restoration of the altar and the temple foundation (<a class=\"ref\" data-ref=\"Ezra 2:36\">Ezra 2:2; 3:2; Haggai 1:1; Zechariah 3</a>). He is the subject of Zechariah's vision of the high priest accused by Satan and clothed in clean garments — a vivid image of priestly restoration and atonement. (2.) A priestly course, the ninth of the twenty-four divisions (<a class=\"ref\" data-ref=\"1 Chronicles 24:11\">1 Chronicles 24:11</a>). (3.) A Levite over the tithes under Hezekiah (<a class=\"ref\" data-ref=\"2 Chronicles 31:15\">2 Chronicles 31:15</a>).</p><p>The name's identity with Jesus (Greek <em>Iesous</em> from Hebrew <em>Yeshua</em>) is not incidental: Matthew 1:21 explicitly links the name's meaning — \"he will save his people from their sins\" — to the infant's divine mission, making the naming of Jesus a theological statement about his salvific role.</p>",
  "hitchcock_meaning": "same as Joshua",
  "source_ids": {"easton": "jeshua", "smith": "jeshua", "isbe": "jeshua"},
  "key_refs": ["Ezra 2:36", "Zechariah 3:1", "Matthew 1:21"]
},
"jeshurun": {
  "id": "jeshurun", "term": "Jeshurun", "category": "names",
  "intro": "<p>Jeshurun (meaning <em>the upright one</em> or <em>the dear upright people</em>) is a poetic name for the people of Israel used in four passages of deep emotional and theological significance: Deuteronomy 32:15; 33:5, 26; and Isaiah 44:2. It is a term of affectionate address, expressing God's idealized vision of his people as upright, beloved, and chosen.</p><p>The most striking use is in Deuteronomy 32:15, where Jeshurun \"grew fat and kicked\" — prosperity led to spiritual unfaithfulness. The contrast between the name's meaning (uprightness) and the people's behavior (revolt) is deliberate and poignant: the \"dear upright people\" became anything but upright in their abundance. By contrast, Deuteronomy 33:26 uses Jeshurun in a blessing context — \"There is no one like the God of Jeshurun\" — expressing unparalleled divine majesty in relation to his treasured people. Isaiah 44:2 uses it in the context of restoration and the coming of the Spirit, addressing the people with tender assurance: \"Do not be afraid, O Jeshurun whom I have chosen.\"</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jeshurun", "smith": "jeshurun", "isbe": "jeshurun"},
  "key_refs": ["Deuteronomy 32:15", "Deuteronomy 33:5", "Deuteronomy 33:26", "Isaiah 44:2"]
},
"jesse": {
  "id": "jesse", "term": "Jesse", "category": "people",
  "intro": "<p>Jesse (meaning <em>gift</em> or <em>firm</em>; Hebrew <em>Yishai</em>) was the son of Obed, grandson of Boaz and Ruth, and the father of King David. He lived at Bethlehem of Judah and had eight sons, the youngest of whom was David (<a class=\"ref\" data-ref=\"Ruth 4:17\">Ruth 4:17, 22</a>; 1 Samuel 16). Jesse is the figure at whose home Samuel came to anoint the next king of Israel, passing over seven impressive older sons before God directed Samuel to the overlooked shepherd boy keeping the sheep.</p><p>Jesse's theological significance far exceeds his narrative role. Isaiah 11:1 prophesies that \"a shoot will come up from the stump of Jesse; from his roots a Branch will bear fruit,\" and 11:10 speaks of \"the Root of Jesse\" as a banner for the nations. These passages, taken up in Romans 15:12 and Revelation 5:5, became central messianic prophecies identifying the Messiah as a descendant of Jesse — not just of David. Paul quotes Isaiah 11:10 to support the inclusion of Gentiles in God's people (Romans 15:12). Matthew and Luke both include Jesse in Jesus's genealogy (<a class=\"ref\" data-ref=\"Matthew 1:5\">Matthew 1:5-6</a>; Luke 3:32).</p>",
  "hitchcock_meaning": "gift; oblation; one who is",
  "source_ids": {"easton": "jesse", "smith": "jesse", "isbe": "jesse"},
  "key_refs": ["Ruth 4:22", "1 Samuel 16:1", "Isaiah 11:1", "Matthew 1:5"]
},
"jesus": {
  "id": "jesus", "term": "Jesus", "category": "people",
  "intro": "<p>Jesus (Greek <em>Iesous</em>, from Hebrew <em>Yeshua</em>, meaning <em>the LORD saves</em> or <em>savior</em>) is primarily the name of Jesus Christ — the Son of God, the incarnate Word, the Messiah of Israel and Savior of the world. The name was given by divine command before his birth: \"You shall call his name Jesus, for he will save his people from their sins\" (Matthew 1:21), making the name itself a theological statement about his mission. He was born in Bethlehem of a virgin, Mary, by the Holy Spirit; lived in Nazareth; was baptized by John; conducted a three-year ministry in Galilee and Judea; was crucified under Pontius Pilate; rose on the third day; and ascended to the Father.</p><p>The name was also borne by two other New Testament figures: Joshua son of Nun (<a class=\"ref\" data-ref=\"Acts 7:45\">Acts 7:45</a>; Hebrews 4:8 — where the Authorized Version's \"Jesus\" is more accurately \"Joshua\"), and Jesus Justus, a Jewish Christian companion of Paul (<a class=\"ref\" data-ref=\"Colossians 4:11\">Colossians 4:11</a>). The name was common in Second Temple Judaism. But for Christians, as Paul declares, \"there is no other name under heaven given to mankind by which we must be saved\" (Acts 4:12), and at the name of Jesus every knee will bow (Philippians 2:10).</p>",
  "hitchcock_meaning": "savior; deliverer",
  "source_ids": {"easton": "jesus", "smith": "jesus", "isbe": "jesus"},
  "key_refs": ["Matthew 1:21", "Acts 4:12", "Philippians 2:10", "Colossians 4:11"]
},
"jether": {
  "id": "jether", "term": "Jether", "category": "people",
  "intro": "<p>Jether (meaning <em>he that excels</em> or <em>abundance</em>) is the name of several biblical figures. The most significant are: (1.) Jether, Gideon's firstborn son, who was ordered to kill the captured Midianite kings Zebah and Zalmunna, but drew back in youth and fear — whereupon the kings themselves asked Gideon to kill them, as a warrior's death was preferable to being killed by a boy (Judges 8:20). (2.) Jether the Ishmaelite, husband of David's sister Abigail and father of Amasa who later became a general under Absalom and then briefly under David (<a class=\"ref\" data-ref=\"1 Kings 2:5\">1 Kings 2:5</a>; 2 Samuel 17:25). (3.) Jether, an alternate form of Ithra, in 2 Samuel 17:25.</p><p>The episode of Gideon's firstborn illustrates the ancient code of honorable combat, while Jether the Ishmaelite's connection to the Davidic family through Amasa became the source of a complicated and ultimately fatal relationship between David and his nephew.</p>",
  "hitchcock_meaning": "he that excels",
  "source_ids": {"easton": "jether", "smith": "jether", "isbe": "jether"},
  "key_refs": ["Judges 8:20", "1 Kings 2:5", "2 Samuel 17:25"]
},
"jetheth": {
  "id": "jetheth", "term": "Jetheth", "category": "people",
  "intro": "<p>Jetheth (meaning <em>giving</em> or possibly <em>nail</em>) was one of the chiefs (<em>allophim</em>) of Edom descended from Esau, listed in the genealogy of Genesis 36:40 and 1 Chronicles 1:51. He appears only in these two parallel lists of the chiefs who governed in Edom before any king reigned over Israel.</p><p>Jetheth is a minor figure whose sole appearance is in the genealogical-administrative records of Edom. The list of Edomite chiefs in Genesis 36 is notable as one of the few detailed records of non-Israelite administration preserved in the Pentateuch, reflecting the Edomites' close kinship with Israel through the line of Esau and Jacob. These chiefs likely ruled over specific clans or districts within Edom.</p>",
  "hitchcock_meaning": "giving",
  "source_ids": {"easton": "jetheth", "smith": "jetheth", "isbe": "jetheth"},
  "key_refs": ["Genesis 36:40"]
},
"jethlah": {
  "id": "jethlah", "term": "Jethlah", "category": "places",
  "intro": "<p>Jethlah (meaning <em>hanging up</em> or <em>heaping up</em>) was a town in the territory allotted to the tribe of Dan, listed in the boundary description of Joshua 19:42. Its precise location is uncertain; it may correspond to a site in the Shephelah (western foothills) region that was part of Dan's original allotment, though much of this territory was subsequently lost to Philistine expansion that eventually led the Danites to migrate northward.</p><p>Jethlah appears only in this single boundary list and has no associated narrative. Its inclusion reflects the careful geographical documentation of the tribal allotments in Joshua 13–19, which preserves place names that would otherwise be entirely unknown. Many of the Danite border towns in this list have resisted confident modern identification.</p>",
  "hitchcock_meaning": "hanging up; heaping up",
  "source_ids": {"easton": "jethlah", "smith": "jethlah", "isbe": "jethlah"},
  "key_refs": ["Joshua 19:42"]
},
"jethro": {
  "id": "jethro", "term": "Jethro", "category": "people",
  "intro": "<p>Jethro (meaning <em>his excellence</em> or <em>his posterity</em>; also called Reuel and Hobab) was the priest of Midian and father-in-law of Moses. After Moses fled Egypt and came to Midian, he served Jethro as a shepherd for forty years and married his daughter Zipporah, who bore him Gershom and Eliezer. When Moses returned to Midian after the Exodus, Jethro brought Zipporah and the boys to meet him in the wilderness and expressed worship of the LORD: \"Now I know that the LORD is greater than all gods\" (<a class=\"ref\" data-ref=\"Exodus 18:8\">Exodus 18:8-12</a>).</p><p>Jethro's most influential contribution was organizational. Observing Moses exhausting himself judging all disputes alone, Jethro advised him to delegate authority by appointing capable men as rulers of thousands, hundreds, fifties, and tens — a hierarchical judicial system that Moses implemented (Exodus 18:13-26). This advice from a Midianite priest-father-in-law shaped Israel's administrative structure at its formation and has been cited as an early example of management delegation. The episode reflects the surprising sources from which wisdom came in the ancient world, and the canonical inclusion of a Midianite's administrative counsel reflects the narrator's confidence that true wisdom is recognizable wherever it appears.</p>",
  "hitchcock_meaning": "his excellence; his posterity",
  "source_ids": {"easton": "jethro", "smith": "jethro", "isbe": "jethro"},
  "key_refs": ["Exodus 18:8", "Exodus 18:13", "Exodus 18:21"]
},
"jetur": {
  "id": "jetur", "term": "Jetur", "category": "people",
  "intro": "<p>Jetur (meaning <em>order</em>, <em>succession</em>, or <em>mountainous</em>) was the ninth son of Ishmael (Genesis 25:15; <a class=\"ref\" data-ref=\"Genesis 25:15\">1 Chronicles 1:31</a>), and the eponymous ancestor of the Iturians — a people who occupied the region northeast of the Sea of Galilee known as Ituraea. This territory, mountainous and somewhat isolated, is mentioned in Luke 3:1 as part of the tetrarchy of Philip the tetrarch, brother of Herod Antipas.</p><p>The Itureans were renowned in antiquity as archers and skilled light cavalry, and their mercenary service was valued by various Hellenistic and Roman rulers. The Israelite tribes of Reuben, Gad, and the half-tribe of Manasseh warred against the Hagrites and Iturians (1 Chronicles 5:19) and settled in their territory. The line from Ishmael's son Jetur to the Itureaean region mentioned in the Roman administrative geography of Luke 3 is one of the more traceable genealogical continuities between the patriarchal and New Testament periods.</p>",
  "hitchcock_meaning": "order; succession; mountainous",
  "source_ids": {"easton": "jetur", "smith": "jetur", "isbe": "jetur"},
  "key_refs": ["Genesis 25:15", "1 Chronicles 5:19", "Luke 3:1"]
},
"jeuel": {
  "id": "jeuel", "term": "Jeuel", "category": "people",
  "intro": "<p>Jeuel (meaning <em>God has taken away</em> or <em>God heaping up</em>) was a descendant of Zerah (Judah's son through Tamar) through the line of Shelah, whose family settled in Jerusalem after the return from Babylon (<a class=\"ref\" data-ref=\"1 Chronicles 9:6\">1 Chronicles 9:6</a>). The number given for the Shelahite returnees — 690 men — suggests a substantial family contingent.</p><p>Jeuel appears only in this post-exilic settlement list and has no associated narrative. The genealogical lists of 1 Chronicles 9 document those who resettled Jerusalem and Judah after the Babylonian exile, providing a sociological snapshot of the early restoration community. The inclusion of Shelahite Judahites (descendants of a line often overshadowed by the Perez branch from which David came) reflects the Chronicler's interest in the comprehensive representation of the whole of Judah in the restored community.</p>",
  "hitchcock_meaning": "God hath taken away; God heaping up",
  "source_ids": {"easton": "jeuel", "smith": "jeuel", "isbe": "jeuel"},
  "key_refs": ["1 Chronicles 9:6"]
},
"jeush": {
  "id": "jeush", "term": "Jeush", "category": "people",
  "intro": "<p>Jeush (meaning <em>he that is devoured</em> or <em>assembler</em>) is the name of five individuals in the Old Testament. The most notable are: (1.) A son of Esau by his wife Oholibamah, and a chief of Edom (<a class=\"ref\" data-ref=\"Genesis 36:5\">Genesis 36:5, 14, 18</a>). (2.) A son of Eshek, a Benjamite descendant of Saul (<a class=\"ref\" data-ref=\"1 Chronicles 7:10\">1 Chronicles 7:10</a>). (3.) A Levite of the family of Gershom: since he had few sons, he and his brother Beriah were counted as one family in the Levitical census (<a class=\"ref\" data-ref=\"1 Chronicles 23:10\">1 Chronicles 23:10-11</a>).</p><p>The Edomite chief Jeush, as a son of Esau, represents the Edomite aristocracy at its founding generation — one of the chiefs who ruled in Edom before Israel had a king (Genesis 36:18). The genealogical range of the name across Edom, Benjamin, and Levi illustrates its common use in the wider Semitic onomastic tradition.</p>",
  "hitchcock_meaning": "Jeuz, he that is devoured",
  "source_ids": {"easton": "jeush", "smith": "jeush", "isbe": "jeush"},
  "key_refs": ["Genesis 36:5", "1 Chronicles 7:10", "1 Chronicles 23:10"]
},
"jew": {
  "id": "jew", "term": "Jew", "category": "concepts",
  "intro": "<p>Jew (Hebrew <em>Yehudi</em>, from the patriarch Judah) was originally a designation for members of the tribe of Judah or citizens of the kingdom of Judah. The earliest biblical use of the term in this narrow sense is 2 Kings 16:6, where Rezin of Syria \"drove the Jews from Elath.\" After the fall of the northern kingdom in 722 B.C., the term gradually expanded to describe all Israelites, as the kingdom of Judah became the surviving political expression of the people of God.</p><p>By the time of the New Testament, \"Jew\" (<em>Ioudaios</em>) had become the universal term for adherents to the religion and ethnicity rooted in the covenants with Abraham, Moses, and David — as distinct from Samaritans, Gentiles, and proselytes. Paul's argument in Romans 2:28-29 redefines the term theologically: \"A person is not a Jew who is one only outwardly... No, a person is a Jew who is one inwardly; and circumcision is circumcision of the heart.\" Galatians 3:28 further declares that in Christ \"there is neither Jew nor Greek\" — not abolishing but transcending ethnic distinction in the new covenant community (<a class=\"ref\" data-ref=\"2 Kings 16:6\">2 Kings 16:6</a>).</p>",
  "hitchcock_meaning": "same as Judah",
  "source_ids": {"easton": "jew", "smith": "jew"},
  "key_refs": ["2 Kings 16:6", "Romans 2:28", "Romans 3:29", "Galatians 3:28"]
},
"jewess": {
  "id": "jewess", "term": "Jewess", "category": "concepts",
  "intro": "<p>Jewess designates a woman of Jewish birth or religion. The term appears three times in the New Testament. Eunice, Timothy's mother, was a Jewess who had believed (<a class=\"ref\" data-ref=\"Acts 16:1\">Acts 16:1</a>) — her Jewish heritage and faith, combined with her Greek husband, produced the mixed heritage that led to Timothy's uncircumcision and Paul's decision to circumcise him as a pastoral measure. Paul commends Eunice by name in 2 Timothy 1:5, noting the sincere faith that first lived in his grandmother Lois and then in Eunice, before passing to Timothy.</p><p>Drusilla, wife of the Roman governor Felix, is identified as a Jewess (<a class=\"ref\" data-ref=\"Acts 24:24\">Acts 24:24</a>) — she was a daughter of Herod Agrippa I and had left her first husband to marry Felix. Paul's reasoning before Felix \"about faith in Christ Jesus\" was presented to an audience that included this Jewish woman. The term appears without theological weight in the New Testament, functioning simply as an ethnic designation in each case.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jewess", "smith": "jewess"},
  "key_refs": ["Acts 16:1", "2 Timothy 1:5", "Acts 24:24"]
},
"jezebel": {
  "id": "jezebel", "term": "Jezebel", "category": "people",
  "intro": "<p>Jezebel (Phoenician; meaning possibly <em>where is the prince?</em> or <em>Baal is the prince</em>; ironically rendered in Hitchcock as <em>chaste</em>) was the daughter of Ethbaal, king of Sidon, and queen of Israel as wife of King Ahab (c. 874–853 B.C.). Her marriage represented the first time the reigning king of Israel married a foreign princess who was herself devoted to a foreign deity — Baal of Sidon — and who used the power of the throne to impose that worship on Israel (<a class=\"ref\" data-ref=\"1 Kings 16:31\">1 Kings 16:31</a>; 18:19).</p><p>Jezebel massacred the prophets of the LORD, maintained 450 prophets of Baal and 400 prophets of Asherah at royal expense, intimidated Elijah into flight after Carmel, and engineered the judicial murder of Naboth to seize his vineyard for Ahab. Elijah pronounced her doom (1 Kings 21:23), and it was fulfilled when Jehu's horses trampled her and dogs consumed her body at Jezreel (<a class=\"ref\" data-ref=\"2 Kings 9:7\">2 Kings 9:30-37</a>), leaving only her skull, feet, and hands. In the New Testament, her name becomes a type: the letter to Thyatira condemns a prophetess called \"Jezebel\" who leads God's people into sexual immorality and idolatry (<a class=\"ref\" data-ref=\"Revelation 2\">Revelation 2:20</a>).</p>",
  "hitchcock_meaning": "chaste",
  "source_ids": {"easton": "jezebel", "smith": "jezebel", "isbe": "jezebel"},
  "key_refs": ["1 Kings 16:31", "1 Kings 18:19", "2 Kings 9:30", "Revelation 2:20"]
},
"jeziel": {
  "id": "jeziel", "term": "Jeziel", "category": "people",
  "intro": "<p>Jeziel was a Benjamite warrior, son of Azmaveth, who joined David at Ziklag during his time as a fugitive from Saul (<a class=\"ref\" data-ref=\"1 Chronicles 12:3\">1 Chronicles 12:3</a>). He and his brother Pelet are listed among the skilled warriors from Benjamin who could shoot arrows and use the sling with either hand and who came to David \"while he still kept himself close because of Saul the son of Kish.\"</p><p>Jeziel is one of many minor figures in the list of David's early supporters preserved in 1 Chronicles 12, a passage that documents the gradual formation of David's military strength during the years before he became king. These Benjamite supporters are theologically notable because they came from Saul's own tribe — their loyalty to David over Saul represents the recognition that God's anointing had shifted.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jeziel", "smith": "jeziel", "isbe": "jeziel"},
  "key_refs": ["1 Chronicles 12:3"]
},
"jezreel": {
  "id": "jezreel", "term": "Jezreel", "category": "places",
  "intro": "<p>Jezreel (meaning <em>God sows</em>) was an important city and the name of the broad valley in which it stood, in the territory of Issachar between Mount Carmel and the Jordan River. The city of Jezreel served as a secondary royal residence of the northern kingdom — particularly for Ahab, who had a palace there (<a class=\"ref\" data-ref=\"1 Kings 21:1\">1 Kings 21:1</a>). It was the site of Naboth's vineyard (1 Kings 21), Jezebel's death (2 Kings 9:30-37), and the burial of Joram (<a class=\"ref\" data-ref=\"2 Kings 9:14\">2 Kings 9</a>).</p><p>The Valley of Jezreel (also called the Plain of Esdraelon) is one of the great strategic corridors of the ancient Near East, running northwest to southeast across northern Israel and providing the primary passage between the coastal plain and the Jordan Valley. Major battles were fought there throughout biblical history. The name carried profound prophetic weight: Hosea 1:4-5 declared that God would \"break the bow of Israel in the Valley of Jezreel\" as judgment for the blood shed by Jehu there, but Hosea 1:11 and 2:22-23 also envision Jezreel as the site of eschatological restoration and new sowing by God.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jezreel", "smith": "jezreel", "isbe": "jezreel"},
  "key_refs": ["Joshua 19:18", "1 Kings 21:1", "2 Kings 9:14", "Hosea 1:4"]
},
"jezreel-blood-of": {
  "id": "jezreel-blood-of", "term": "Jezreel, Blood of", "category": "events",
  "intro": "<p>The blood of Jezreel refers to the mass killings carried out at Jezreel by Jehu when he executed his coup against the house of Ahab (2 Kings 9–10) — specifically the deaths of King Joram of Israel, King Ahaziah of Judah, Jezebel, and subsequently the seventy sons of Ahab whose heads were brought to Jehu at Jezreel. Though commanded by God through Elisha (2 Kings 9:6-8), the manner and scope of the bloodshed attracted prophetic criticism.</p><p>Hosea 1:4 delivers God's word to his son named Jezreel: \"I will soon punish the house of Jehu for the massacre at Jezreel, and I will put an end to the kingdom of Israel.\" This oracle creates a theological tension: God commanded the execution of Ahab's house yet also punishes Jehu's house for the blood that was shed. The resolution lies in Jehu's later apostasy and the fact that political obedience may be attended by excessive violence. The \"blood of Jezreel\" thus became a byword for violence that, even when judicially provoked, carries guilt that God will reckon.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jezreel-blood-of"},
  "key_refs": ["Hosea 1:4", "1 Kings 18:4", "2 Kings 9:6"]
},
"jezreel-day-of": {
  "id": "jezreel-day-of", "term": "Jezreel, Day of", "category": "events",
  "intro": "<p>The Day of Jezreel refers to the eschatological promise in Hosea 1:5 and 2:22-23, where the name Jezreel (<em>God sows</em>) is reinterpreted from a sign of judgment to a sign of restoration. After the oracle of judgment — God will break Israel's bow in the Valley of Jezreel (<a class=\"ref\" data-ref=\"Hosea 1:5\">Hosea 1:5</a>) — Hosea pivots dramatically: \"In the place where it was said to them, 'You are not my people,' they will be called 'children of the living God'\" (Hosea 1:10).</p><p>The Day of Jezreel is the eschatological day when God will replant and resow his people in the land — the negative meaning of the judgment name transformed into the positive meaning of the name itself (\"God sows\"). Hosea 2:22-23 develops this: God will sow Jezreel in the land, and \"I will say to those called 'Not my people,' 'You are my people'; and they will say, 'You are my God.'\" Paul quotes this passage in Romans 9:25-26 as scriptural support for the calling of Gentiles into the people of God — the \"Day of Jezreel\" fulfillment extending to all who were once \"not a people.\"</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jezreel-day-of"},
  "key_refs": ["Hosea 1:5", "Hosea 2:22", "Romans 9:25"]
},
"jezreel-ditch-of": {
  "id": "jezreel-ditch-of", "term": "Jezreel, Ditch of", "category": "places",
  "intro": "<p>The ditch (or moat) of Jezreel is mentioned in 1 Kings 21:23 in the fulfillment of Elijah's prophecy against Jezebel: \"Dogs shall eat Jezebel by the wall of Jezreel\" (or in some manuscripts, \"in the plot of ground at Jezreel\"). The precise meaning of the Hebrew term (<em>chel</em>) rendered \"ditch\" or \"rampart\" is disputed — some translations render it as \"moat,\" others as \"in the portion of Jezreel.\"</p><p>The prophecy's fulfillment is recorded in <a class=\"ref\" data-ref=\"1 Kings 21:23\">2 Kings 9:36</a>: when Jehu's servants went to bury Jezebel, they found only her skull, feet, and the palms of her hands, and Jehu recognized this as the fulfillment of Elijah's word. The ditch or wall thus marks the precise location at Jezreel where divine judgment on Jezebel was executed, tying the prophecy to a specific topographic feature of the city.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jezreel-ditch-of"},
  "key_refs": ["1 Kings 21:23", "2 Kings 9:36"]
},
"jezreel-fountain-of": {
  "id": "jezreel-fountain-of", "term": "Jezreel, Fountain of", "category": "places",
  "intro": "<p>The Fountain of Jezreel (also called the spring of Jezreel or the spring of Harod) was a water source in or near the Valley of Jezreel at the foot of Mount Gilboa, where the Israelite army camped before the battle against the Philistines in which Saul was killed (<a class=\"ref\" data-ref=\"1 Samuel 29:1\">1 Samuel 29:1</a>; Judges 7:1; 2 Samuel 23:25). In Judges 7:1, this spring — called the spring of Harod — is where Gideon's army of 32,000 was reduced to 300 by God's testing, eliminating those who knelt to drink from those who lapped water with their hands.</p><p>The spring thus provided the setting for two decisive moments in Israel's military history — Gideon's reduction of his army as an act of faith and Saul's final doomed muster before Gilboa. Identified with the modern 'Ain Jalud (Spring of Goliath) at the foot of the Gilboa ridge, it is one of the most important water sources in the valley and was strategically significant for armies moving through the region.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "jezreel-fountain-of"},
  "key_refs": ["1 Samuel 29:1", "Judges 7:1", "2 Samuel 23:25"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data): written += 1
        else: skipped += 1
    print(f'BP j2: Jedidiah → Jezreel, Fountain of: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__': main()
