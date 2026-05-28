#!/usr/bin/env python3
"""Write book introduction JSON files for all remaining Bible books."""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'books', 'introductions')
os.makedirs(OUT, exist_ok=True)

BOOKS = [

# ─── Old Testament ────────────────────────────────────────────────────────────

{"id":"exodus","title":"Exodus","author":"Moses (traditional)","date":"15th–13th century BC",
"setting":"Continues directly from Genesis, tracing Israel's growth into a nation in Egypt and God's dramatic redemption through Moses.",
"purpose":"To show that the God of the patriarchs kept his covenant promises, redeemed his people from slavery, constituted them as a nation at Sinai, and established the pattern of worship by which he would dwell among them.",
"themes":["Redemption from slavery","The name and character of God (YHWH)","The plagues and signs","The Passover as a type of Christ","The Sinai covenant and the law","The tabernacle as God's dwelling place","Holiness and the presence of God"],
"outline":[
  {"label":"Israel in Egypt: Oppression and Moses' Call","chapters":"1–6","ref":"Exodus 1:1"},
  {"label":"The Plagues and the Passover","chapters":"7–12","ref":"Exodus 7:1"},
  {"label":"The Exodus and Journey to Sinai","chapters":"13–18","ref":"Exodus 13:1"},
  {"label":"The Sinai Covenant and the Law","chapters":"19–24","ref":"Exodus 19:1"},
  {"label":"Tabernacle Instructions and the Golden Calf","chapters":"25–34","ref":"Exodus 25:1"},
  {"label":"Building the Tabernacle","chapters":"35–40","ref":"Exodus 35:1"}
],"key_verse":"Exodus 6:7",
"timeline":{"date":"~1446 or ~1250 BC (event)","before":[{"label":"Israel in Egypt — Genesis ends","ref":"Genesis 50:26"}],"after":[{"label":"Leviticus — laws of the tabernacle","ref":"Leviticus 1:1"}]}},

{"id":"leviticus","title":"Leviticus","author":"Moses (traditional)","date":"15th–13th century BC",
"setting":"Delivered at Mount Sinai immediately after the tabernacle was completed (Exodus 40). The entire book records divine speech addressed to Moses at the tent of meeting.",
"purpose":"To instruct the newly redeemed nation in how to approach a holy God through sacrifice, purity, and covenant obedience. The central call — 'Be holy, for I am holy' (11:44) — shapes the entire book.",
"themes":["Holiness and the holiness of God","The sacrificial system and atonement","Clean and unclean distinctions","The Day of Atonement","The Holiness Code (chs. 17–26)","Jubilee and redemption"],
"outline":[
  {"label":"Laws of Sacrifice","chapters":"1–7","ref":"Leviticus 1:1"},
  {"label":"Ordination of Priests","chapters":"8–10","ref":"Leviticus 8:1"},
  {"label":"Clean and Unclean Laws","chapters":"11–15","ref":"Leviticus 11:1"},
  {"label":"The Day of Atonement","chapters":"16","ref":"Leviticus 16:1"},
  {"label":"The Holiness Code","chapters":"17–26","ref":"Leviticus 17:1"},
  {"label":"Vows and Tithes","chapters":"27","ref":"Leviticus 27:1"}
],"key_verse":"Leviticus 17:11",
"timeline":{"date":"~1446–1405 BC","before":[{"label":"Tabernacle completed","ref":"Exodus 40:1"}],"after":[{"label":"Numbers — census and wilderness journey","ref":"Numbers 1:1"}]}},

{"id":"numbers","title":"Numbers","author":"Moses (traditional)","date":"15th–13th century BC",
"setting":"Covers the wilderness wandering between Sinai and the plains of Moab — a period of approximately 38 years following Israel's refusal to enter Canaan at Kadesh Barnea.",
"purpose":"To record the failure of the Exodus generation (who died in the wilderness) and the preparation of the new generation to enter the Promised Land, showing that unbelief forfeits the covenant's blessings.",
"themes":["God's faithfulness despite Israel's rebellion","The cost of unbelief and disobedience","The bronze serpent (typology of Christ — John 3:14)","Priestly duties and Levitical service","The second census and the new generation"],
"outline":[
  {"label":"Census and Preparation at Sinai","chapters":"1–10","ref":"Numbers 1:1"},
  {"label":"From Sinai to Kadesh: Rebellion","chapters":"11–14","ref":"Numbers 11:1"},
  {"label":"Wilderness Wanderings","chapters":"15–21","ref":"Numbers 15:1"},
  {"label":"From Moab to the Plains: The New Generation","chapters":"22–36","ref":"Numbers 22:1"}
],"key_verse":"Numbers 14:11",
"timeline":{"date":"~1446–1406 BC","before":[{"label":"Law and tabernacle at Sinai","ref":"Leviticus 1:1"}],"after":[{"label":"Deuteronomy — Moses' farewell speeches","ref":"Deuteronomy 1:1"}]}},

{"id":"deuteronomy","title":"Deuteronomy","author":"Moses, with an account of his death added (Deut. 34) by Joshua or a later hand","date":"~15th–13th century BC",
"setting":"The plains of Moab, east of the Jordan, on the eve of the conquest. Moses delivers three farewell speeches to the new generation who will enter Canaan.",
"purpose":"To renew the Sinai covenant with the second generation — calling them to undivided love for YHWH, obedience to his law, and faithfulness when they settle in the land. Deuteronomy is quoted more by the NT than any other OT book.",
"themes":["The Shema: undivided love for God","Covenant renewal — blessings and curses","The uniqueness of YHWH (monotheism)","Memory and the danger of forgetting","The coming prophet like Moses (18:15-18, fulfilled in Jesus)","Justice and care for the vulnerable"],
"outline":[
  {"label":"First Speech: Historical Prologue","chapters":"1–4","ref":"Deuteronomy 1:1"},
  {"label":"Second Speech: The Law Restated","chapters":"5–26","ref":"Deuteronomy 5:1"},
  {"label":"Covenant Renewal — Blessings and Curses","chapters":"27–30","ref":"Deuteronomy 27:1"},
  {"label":"Joshua Commissioned; Moses' Death","chapters":"31–34","ref":"Deuteronomy 31:1"}
],"key_verse":"Deuteronomy 6:4",
"timeline":{"date":"~1406 BC","before":[{"label":"40 years of wilderness wandering","ref":"Numbers 14:33"}],"after":[{"label":"Joshua — the conquest of Canaan","ref":"Joshua 1:1"}]}},

{"id":"joshua","title":"Joshua","author":"Largely Joshua himself, with additions after his death (possibly by Phinehas or Samuel)","date":"~1400–1380 BC",
"setting":"The conquest and settlement of Canaan following the death of Moses. Joshua leads Israel across the Jordan into the Promised Land.",
"purpose":"To show that God kept his covenant promise to give Israel the land — and that success came through faith and obedience, while failure came through compromise with idolatry.",
"themes":["Covenant faithfulness — God gives the land","Faith and obedience as the path to blessing","The ban (herem) and holy war","Division of the land among the tribes","Covenant renewal at Shechem","Rahab and the inclusion of Gentiles by faith"],
"outline":[
  {"label":"Preparation and the Jordan Crossing","chapters":"1–5","ref":"Joshua 1:1"},
  {"label":"The Conquest — Central, Southern, Northern","chapters":"6–12","ref":"Joshua 6:1"},
  {"label":"Division of the Land","chapters":"13–21","ref":"Joshua 13:1"},
  {"label":"Covenant Renewal and Joshua's Farewell","chapters":"22–24","ref":"Joshua 22:1"}
],"key_verse":"Joshua 1:9",
"timeline":{"date":"~1406–1380 BC","before":[{"label":"Moses' death; commissioning of Joshua","ref":"Deuteronomy 34:1"}],"after":[{"label":"Judges — cycles of apostasy and deliverance","ref":"Judges 1:1"}]}},

{"id":"judges","title":"Judges","author":"Possibly Samuel (Jewish tradition); the book reflects a perspective after the monarchy began","date":"~1050–1000 BC (composition), events ~1380–1050 BC",
"setting":"The period between Joshua's death and the rise of the monarchy — a cycle of apostasy, oppression, repentance, and deliverance repeated seven times.",
"purpose":"To show that covenant unfaithfulness to YHWH leads to national decline, and to prepare the reader for the need for a king who would lead Israel in covenant faithfulness — pointing ultimately to the King of kings.",
"themes":["The sin cycle: apostasy → oppression → repentance → deliverance","The failure of Israel to complete the conquest","The deterioration of Israel's spiritual condition","Surprising deliverers (Deborah, Gideon, Samson)","The chaos of life without godly leadership (chs. 17–21)"],
"outline":[
  {"label":"Introduction: Incomplete Conquest and Apostasy","chapters":"1–2","ref":"Judges 1:1"},
  {"label":"The Six Major and Six Minor Judges","chapters":"3–16","ref":"Judges 3:7"},
  {"label":"Appendix: Micah's Idol and the Levite's Concubine","chapters":"17–21","ref":"Judges 17:1"}
],"key_verse":"Judges 21:25",
"timeline":{"date":"~1380–1050 BC","before":[{"label":"Joshua's death","ref":"Joshua 24:29"}],"after":[{"label":"Ruth — faithfulness during the Judges period","ref":"Ruth 1:1"}]}},

{"id":"ruth","title":"Ruth","author":"Unknown; the Talmud attributes it to Samuel","date":"~1050–1000 BC (composition); events during the period of Judges",
"setting":"Moab and Bethlehem during the days of the Judges. Ruth, a Moabite widow, accompanies her Israelite mother-in-law Naomi back to Bethlehem, where she encounters Boaz the kinsman-redeemer.",
"purpose":"To show God's providential care for the faithful amid suffering, to demonstrate that covenant loyalty (hesed) crosses ethnic boundaries, and to provide the genealogy of King David — placing him in a line that included a Gentile woman of great faith.",
"themes":["Hesed — loyal, covenant love","Providence and God's quiet sovereignty","The kinsman-redeemer (goel) as a type of Christ","Faithful Gentiles and inclusion in Israel","Redemption, restoration, and new beginnings"],
"outline":[
  {"label":"Naomi and Ruth: Tragedy and Loyalty in Moab","chapters":"1","ref":"Ruth 1:1"},
  {"label":"Ruth Gleans in Boaz's Field","chapters":"2","ref":"Ruth 2:1"},
  {"label":"Ruth Appeals to Boaz as Kinsman-Redeemer","chapters":"3","ref":"Ruth 3:1"},
  {"label":"Boaz Redeems Ruth; the Genealogy of David","chapters":"4","ref":"Ruth 4:1"}
],"key_verse":"Ruth 1:16",
"timeline":{"date":"~1100 BC (events)","before":[{"label":"The Judges period","ref":"Judges 2:16"}],"after":[{"label":"David's reign; Ruth is his great-grandmother","ref":"1 Samuel 16:13"}]}},

{"id":"1samuel","title":"1 Samuel","author":"Unknown; Samuel, Nathan, and Gad are named in 1 Chron. 29:29 as sources","date":"~960–900 BC (composition); events ~1100–1010 BC",
"setting":"The transition from the period of Judges to the monarchy — Samuel as the last judge and first prophet, Saul as the first king, and David as God's chosen king.",
"purpose":"To trace the rise and fall of Saul and the rise of David, showing that true kingship requires a heart wholly devoted to God. The book also introduces Hannah's song (ch. 2) as a theological template for the whole narrative.",
"themes":["The heart that God seeks: David vs. Saul","Samuel as prophet, priest, and judge","The failure of human expectations (Saul)","The anointing of David — God's surprising choices","The ark of the covenant and God's presence","Covenant faithfulness and its absence"],
"outline":[
  {"label":"Samuel: Birth, Call, and Ministry","chapters":"1–7","ref":"1 Samuel 1:1"},
  {"label":"Saul Anointed and His Early Reign","chapters":"8–15","ref":"1 Samuel 8:1"},
  {"label":"Saul's Rejection and David's Rise","chapters":"16–31","ref":"1 Samuel 16:1"}
],"key_verse":"1 Samuel 16:7",
"timeline":{"date":"~1100–1010 BC","before":[{"label":"The Judges and Samuel's birth","ref":"Judges 21:25"}],"after":[{"label":"2 Samuel — David's reign in Jerusalem","ref":"2 Samuel 1:1"}]}},

{"id":"2samuel","title":"2 Samuel","author":"Unknown; sources include the records of Nathan and Gad (1 Chron. 29:29)","date":"~960–900 BC (composition); events ~1010–970 BC",
"setting":"David's reign in Hebron (over Judah) and then Jerusalem (over all Israel), including his great sins of adultery and murder and the Absalom rebellion.",
"purpose":"To present David as the model covenant king — whose throne God promised would endure forever (2 Sam. 7) — while honestly recording his catastrophic failures and their consequences, pointing forward to the greater Son of David.",
"themes":["The Davidic covenant (ch. 7) — the promise of an eternal throne","David as a type of Christ","Sin, repentance, and consequences","The justice of God in David's family","Jerusalem and the ark of the covenant"],
"outline":[
  {"label":"David's Reign Established in Judah and Jerusalem","chapters":"1–10","ref":"2 Samuel 1:1"},
  {"label":"David's Sin with Bathsheba and Murder of Uriah","chapters":"11–12","ref":"2 Samuel 11:1"},
  {"label":"Absalom's Rebellion and Its Aftermath","chapters":"13–20","ref":"2 Samuel 13:1"},
  {"label":"Epilogue: David's Song, Mighty Men, and Census","chapters":"21–24","ref":"2 Samuel 21:1"}
],"key_verse":"2 Samuel 7:16",
"timeline":{"date":"~1010–970 BC","before":[{"label":"Saul's death; David anointed king","ref":"1 Samuel 31:1"}],"after":[{"label":"1 Kings — Solomon's reign and the divided kingdom","ref":"1 Kings 1:1"}]}},

{"id":"1kings","title":"1 Kings","author":"Unknown; Jewish tradition attributes it to Jeremiah","date":"~620–550 BC (composition); events ~970–850 BC",
"setting":"The last days of David, Solomon's glorious reign, and the division of the kingdom into Israel (north) and Judah (south) following Solomon's death, through Ahab and Elijah.",
"purpose":"To show that Israel's history is governed by covenant faithfulness: obedience brings blessing, idolatry brings judgment. The division of the kingdom is the direct consequence of Solomon's unfaithfulness.",
"themes":["Solomon's wisdom and temple","Covenant obedience and apostasy","The divided kingdom","Elijah the prophet and the contest on Carmel","Baal worship and YHWH's exclusivity","Temple worship vs. idolatry at Bethel and Dan"],
"outline":[
  {"label":"David's Death; Solomon's Accession","chapters":"1–2","ref":"1 Kings 1:1"},
  {"label":"Solomon's Wisdom, Temple, and Apostasy","chapters":"3–11","ref":"1 Kings 3:1"},
  {"label":"The Divided Kingdom: Rehoboam to Ahab","chapters":"12–22","ref":"1 Kings 12:1"}
],"key_verse":"1 Kings 8:23",
"timeline":{"date":"~970–850 BC","before":[{"label":"David's reign and the Davidic covenant","ref":"2 Samuel 7:1"}],"after":[{"label":"2 Kings — fall of Israel and Judah","ref":"2 Kings 1:1"}]}},

{"id":"2kings","title":"2 Kings","author":"Unknown; Jewish tradition attributes it to Jeremiah","date":"~550 BC (composition); events ~850–586 BC",
"setting":"The ministries of Elisha and later prophets, the fall of the northern kingdom of Israel to Assyria (722 BC), the reforms of Hezekiah and Josiah, and the fall of Jerusalem to Babylon (586 BC).",
"purpose":"To show that the covenant curses of Deuteronomy 28 inevitably came upon a nation that persisted in idolatry, and that even godly kings like Hezekiah and Josiah could only delay, not avert, the judgment earned by generations of apostasy.",
"themes":["The fulfillment of Deuteronomic covenant curses","Elisha's ministry and miracles","The Assyrian conquest of Israel","Hezekiah's faith and Sennacherib's defeat","Josiah's reforms and the book of the law","The Babylonian exile as covenant judgment"],
"outline":[
  {"label":"Elisha's Ministry; Israel's Decline","chapters":"1–17","ref":"2 Kings 1:1"},
  {"label":"Hezekiah and the Assyrian Crisis","chapters":"18–20","ref":"2 Kings 18:1"},
  {"label":"Manasseh to the Fall of Jerusalem","chapters":"21–25","ref":"2 Kings 21:1"}
],"key_verse":"2 Kings 17:18",
"timeline":{"date":"~850–586 BC","before":[{"label":"Elijah and the northern kingdom","ref":"1 Kings 17:1"}],"after":[{"label":"Exile in Babylon; Ezekiel and Daniel ministries","ref":"Daniel 1:1"}]}},

{"id":"1chronicles","title":"1 Chronicles","author":"Ezra (Jewish tradition)","date":"~450–400 BC (post-exile)",
"setting":"Written for the returning exiles, beginning with genealogies from Adam and focusing on David's reign — especially the preparations for the temple.",
"purpose":"To give the post-exilic community their identity as the covenant people of God, to highlight David's role in establishing temple worship, and to show that God's purposes for Israel continue despite the exile.",
"themes":["Genealogies as covenant history from Adam","David's focus on temple preparation","The Levitical priesthood and worship","God's faithfulness across generations","Israel's identity as the people of YHWH"],
"outline":[
  {"label":"Genealogies: Adam to the Return","chapters":"1–9","ref":"1 Chronicles 1:1"},
  {"label":"Saul's Death and David's Coronation","chapters":"10–12","ref":"1 Chronicles 10:1"},
  {"label":"The Ark Brought to Jerusalem","chapters":"13–17","ref":"1 Chronicles 13:1"},
  {"label":"David's Wars and Temple Preparations","chapters":"18–29","ref":"1 Chronicles 18:1"}
],"key_verse":"1 Chronicles 29:11",
"timeline":{"date":"Events ~1010–970 BC; written ~450 BC","before":[{"label":"The exile to Babylon","ref":"2 Kings 25:1"}],"after":[{"label":"2 Chronicles — Solomon through the exile","ref":"2 Chronicles 1:1"}]}},

{"id":"2chronicles","title":"2 Chronicles","author":"Ezra (Jewish tradition)","date":"~450–400 BC (post-exile)",
"setting":"Continues 1 Chronicles from Solomon's reign through the destruction of Jerusalem and the edict of Cyrus, which ends the book on a note of hope.",
"purpose":"To call the post-exilic community back to proper worship and covenant loyalty, focusing especially on faithful and unfaithful kings of Judah and their relationship to temple worship.",
"themes":["The temple as the center of covenant life","The role of repentance in covenant restoration","Faithful kings — Solomon, Jehoshaphat, Hezekiah, Josiah","The Levitical priesthood and the Psalms","The hope of return (Cyrus's edict)"],
"outline":[
  {"label":"Solomon's Reign and the Temple","chapters":"1–9","ref":"2 Chronicles 1:1"},
  {"label":"The Divided Kingdom: Rehoboam to Ahaz","chapters":"10–28","ref":"2 Chronicles 10:1"},
  {"label":"Hezekiah's and Josiah's Reforms","chapters":"29–35","ref":"2 Chronicles 29:1"},
  {"label":"Judah's Fall and Cyrus's Edict","chapters":"36","ref":"2 Chronicles 36:1"}
],"key_verse":"2 Chronicles 7:14",
"timeline":{"date":"Events ~970–539 BC; written ~450 BC","before":[{"label":"1 Chronicles — David's preparation","ref":"1 Chronicles 29:1"}],"after":[{"label":"Ezra — the return from exile","ref":"Ezra 1:1"}]}},

{"id":"ezra","title":"Ezra","author":"Ezra (Jewish tradition; may have also compiled Nehemiah and Chronicles)","date":"~450–400 BC",
"setting":"The first two returns of Jewish exiles from Babylon to Jerusalem — first under Zerubbabel (~538 BC) to rebuild the temple, then under Ezra himself (~458 BC) to restore covenant faithfulness.",
"purpose":"To show that God kept his word through Cyrus (fulfilling Isaiah 44:28) and that the returned exiles faced the ongoing temptation of compromise with the nations — requiring continuous renewal of covenant commitment.",
"themes":["The faithfulness of God to restore his people","The rebuilt temple as a sign of continuity","Opposition to God's purposes","Intermarriage and covenant purity","Ezra as scribe and teacher of the law","The return as a second Exodus"],
"outline":[
  {"label":"The First Return Under Zerubbabel","chapters":"1–6","ref":"Ezra 1:1"},
  {"label":"Ezra's Return and the Crisis of Mixed Marriages","chapters":"7–10","ref":"Ezra 7:1"}
],"key_verse":"Ezra 7:10",
"timeline":{"date":"~538–458 BC","before":[{"label":"Cyrus's decree ending the exile","ref":"2 Chronicles 36:22"}],"after":[{"label":"Nehemiah — rebuilding the walls","ref":"Nehemiah 1:1"}]}},

{"id":"nehemiah","title":"Nehemiah","author":"Nehemiah (memoir sections); possibly compiled by Ezra","date":"~430–400 BC",
"setting":"Jerusalem under Persian rule (~445 BC). Nehemiah, the king's cupbearer, returns to rebuild Jerusalem's walls over fierce opposition, then addresses social injustice and covenant violations.",
"purpose":"To show that covenant renewal requires both practical action (rebuilding the wall) and spiritual reform (re-reading the law, putting away foreign wives, restoring Sabbath observance) — and that God answers prayer and gives success to his servants.",
"themes":["Prayer as the foundation of action","Leadership, courage, and opposition","The reading of the law and covenant renewal","Social justice — debt, slavery, and exploitation","Sabbath and covenant practices","Jerusalem as the city of God's people"],
"outline":[
  {"label":"Nehemiah's Commission and the Walls Rebuilt","chapters":"1–7","ref":"Nehemiah 1:1"},
  {"label":"Ezra Reads the Law; Covenant Renewal","chapters":"8–10","ref":"Nehemiah 8:1"},
  {"label":"Repopulation of Jerusalem and Nehemiah's Reforms","chapters":"11–13","ref":"Nehemiah 11:1"}
],"key_verse":"Nehemiah 8:10",
"timeline":{"date":"~445–430 BC","before":[{"label":"Ezra's return and reforms","ref":"Ezra 7:1"}],"after":[{"label":"Malachi — the last OT prophet","ref":"Malachi 1:1"}]}},

{"id":"esther","title":"Esther","author":"Unknown; possibly Mordecai or Ezra","date":"~480 BC (events); written ~400 BC",
"setting":"The Persian court of Susa under King Ahasuerus (Xerxes I), as the Jewish people living in the diaspora face annihilation through the plot of Haman the Agagite.",
"purpose":"To show God's providential preservation of his covenant people even when his name is not mentioned and his presence seems absent — and to explain the origin of the Feast of Purim.",
"themes":["Providence: God's hidden hand in history","Courage and risk: 'if I perish, I perish'","Reversal: the enemy destroyed by his own scheme","The survival of the Jewish people as a theological fact","Identity and faithfulness in exile","Celebration and the feast of Purim"],
"outline":[
  {"label":"Vashti Deposed; Esther Becomes Queen","chapters":"1–2","ref":"Esther 1:1"},
  {"label":"Haman's Plot Against the Jews","chapters":"3–4","ref":"Esther 3:1"},
  {"label":"Esther's Intervention and Haman's Fall","chapters":"5–7","ref":"Esther 5:1"},
  {"label":"The Jews Vindicated; Purim Established","chapters":"8–10","ref":"Esther 8:1"}
],"key_verse":"Esther 4:14",
"timeline":{"date":"~480 BC","before":[{"label":"Zerubbabel's return and temple rebuilding","ref":"Ezra 1:1"}],"after":[{"label":"Ezra's return to Jerusalem","ref":"Ezra 7:1"}]}},

{"id":"job","title":"Job","author":"Unknown; Job himself, Moses, and Solomon have been suggested","date":"Unknown; the events may reflect the patriarchal period; composition may be much later",
"setting":"The land of Uz — outside Israel, in the east. Job is described as 'blameless and upright' (1:1). The book opens with a heavenly scene in which God allows Satan to test him.",
"purpose":"To probe the questions of innocent suffering, the justice of God, and the limits of human understanding — and to call the sufferer to trust God's wisdom even when his ways are past finding out.",
"themes":["The suffering of the righteous","The limits of human wisdom (the friends' failure)","God's sovereignty and freedom","The heavenly court and spiritual warfare","Lament as a legitimate response to suffering","The answer of the whirlwind: God's transcendence","The restoration of Job"],
"outline":[
  {"label":"Prologue: Job's Suffering Permitted","chapters":"1–2","ref":"Job 1:1"},
  {"label":"Job and His Three Friends: Three Cycles","chapters":"3–31","ref":"Job 3:1"},
  {"label":"Elihu's Speeches","chapters":"32–37","ref":"Job 32:1"},
  {"label":"God Speaks from the Whirlwind","chapters":"38–41","ref":"Job 38:1"},
  {"label":"Epilogue: Job Restored","chapters":"42","ref":"Job 42:1"}
],"key_verse":"Job 19:25",
"timeline":{"date":"Unknown; patriarchal setting likely","before":[],"after":[{"label":"Psalms — the poetry of Israel's worship","ref":"Psalms 1:1"}]}},

{"id":"proverbs","title":"Proverbs","author":"Solomon (chs. 1–29), Agur (ch. 30), Lemuel's mother (ch. 31); collected under Solomon's patronage","date":"~950 BC (Solomon's era); final compilation possibly ~700 BC (Hezekiah's men, 25:1)",
"setting":"A royal wisdom school, addressing a young man preparing for life. The book presents Wisdom as a divine gift available to all who fear the LORD.",
"purpose":"To impart practical, God-centered wisdom for navigating all of life — family, work, speech, wealth, friendship — on the foundation that 'the fear of the LORD is the beginning of wisdom' (1:7; 9:10).",
"themes":["The fear of the LORD as wisdom's foundation","Wisdom personified (especially chs. 1–9)","Speech: words that heal vs. words that destroy","Work, diligence, and laziness","Friendship and counsel","Sexual purity and faithfulness in marriage","The Excellent Wife (ch. 31) as Wisdom embodied"],
"outline":[
  {"label":"In Praise of Wisdom: Discourses to a Son","chapters":"1–9","ref":"Proverbs 1:1"},
  {"label":"The Proverbs of Solomon","chapters":"10–22:16","ref":"Proverbs 10:1"},
  {"label":"Sayings of the Wise","chapters":"22:17–24","ref":"Proverbs 22:17"},
  {"label":"More Proverbs of Solomon (Hezekiah's edition)","chapters":"25–29","ref":"Proverbs 25:1"},
  {"label":"Agur, Lemuel, and the Excellent Wife","chapters":"30–31","ref":"Proverbs 30:1"}
],"key_verse":"Proverbs 3:5",
"timeline":{"date":"~950–700 BC","before":[{"label":"Solomon's temple and reign","ref":"1 Kings 3:1"}],"after":[{"label":"Ecclesiastes — wisdom's limits","ref":"Ecclesiastes 1:1"}]}},

{"id":"ecclesiastes","title":"Ecclesiastes","author":"Qohelet ('the Preacher/Assembler'), identified as Solomon by tradition though his identity is debated","date":"~940–700 BC",
"setting":"A royal sage reflects on a lifetime of wisdom, wealth, and pleasure, testing whether any human enterprise produces lasting meaning. The word 'vanity' (hebel, 'vapor/breath') occurs 38 times.",
"purpose":"To confront the reader with the limits of all earthly pursuits — wisdom, pleasure, work, wealth — under the sun, and to call for reverent trust in God as the only stable reality in a transient world.",
"themes":["Vanity (hebel) — the transience of all things","Death as the great equalizer","Enjoyment as a gift from God within limits","Wisdom's limits: not the ultimate answer","The fear of God as the sum of wisdom","Time, seasons, and Providence (ch. 3)"],
"outline":[
  {"label":"Theme: All is Vanity","chapters":"1:1–11","ref":"Ecclesiastes 1:1"},
  {"label":"Wisdom, Pleasure, and Toil — All Tested","chapters":"1:12–6:12","ref":"Ecclesiastes 1:12"},
  {"label":"Practical Wisdom under the Sun","chapters":"7–11","ref":"Ecclesiastes 7:1"},
  {"label":"Conclusion: Fear God and Keep His Commandments","chapters":"12","ref":"Ecclesiastes 12:1"}
],"key_verse":"Ecclesiastes 12:13",
"timeline":{"date":"~940 BC (if Solomon); composition possibly later","before":[{"label":"Proverbs — practical wisdom","ref":"Proverbs 1:1"}],"after":[{"label":"Song of Solomon — wisdom on love","ref":"Song of Solomon 1:1"}]}},

{"id":"songofsolomon","title":"Song of Solomon","author":"Solomon (title, 1:1), though this may indicate Solomonic patronage","date":"~950 BC or later",
"setting":"A collection of love poems celebrating the beauty of human romantic love between a man and a woman, set in the landscape of Israel.",
"purpose":"To celebrate the goodness of God-given sexual love within marriage as a creation gift, and — in the allegorical reading recognized by both Jewish and Christian tradition — to depict God's covenant love for his people.",
"themes":["The beauty and goodness of human love","Longing, union, and separation","The beloved as garden and the lover's delight","Exclusivity and covenant in love","God's love for Israel / Christ's love for the church (allegorical)"],
"outline":[
  {"label":"The Beloved's Longing","chapters":"1–2","ref":"Song of Solomon 1:1"},
  {"label":"Night and Day: Seeking and Finding","chapters":"3–5","ref":"Song of Solomon 3:1"},
  {"label":"Praise of the Beloved; Love's Triumph","chapters":"6–8","ref":"Song of Solomon 6:1"}
],"key_verse":"Song of Solomon 8:6",
"timeline":{"date":"~950 BC","before":[{"label":"Proverbs and Ecclesiastes — wisdom literature","ref":"Proverbs 1:1"}],"after":[{"label":"Isaiah — prophecy of redemption","ref":"Isaiah 1:1"}]}},

{"id":"isaiah","title":"Isaiah","author":"Isaiah son of Amoz; critical scholarship posits two or three authors (chs. 1–39 and 40–66), though the NT consistently attributes the whole to Isaiah",
"date":"~740–700 BC (Isaiah's ministry); possibly extending to 680 BC",
"setting":"Judah under kings Uzziah, Jotham, Ahaz, and Hezekiah — a period of Assyrian threat, internal corruption, and spiritual declension. Isaiah ministers as the Assyrian empire rises and Jerusalem is miraculously delivered.",
"purpose":"To call Judah to covenant faithfulness, to announce the coming judgment of exile, and — uniquely among the prophets — to set this judgment in the context of stunning promises of redemption, the Servant of the LORD, and a new creation.",
"themes":["The holiness of God ('the Holy One of Israel' — 25x)","Judgment on Judah, Israel, and the nations","The Servant Songs (42, 49, 50, 52:13–53:12)","The Suffering Servant as the atonement for sin","The new exodus and return from exile","The new creation: new heavens and new earth","The highway of holiness"],
"outline":[
  {"label":"Book of Judgment (Prophecies to Israel and Nations)","chapters":"1–39","ref":"Isaiah 1:1"},
  {"label":"The Book of Comfort — Return from Exile","chapters":"40–55","ref":"Isaiah 40:1"},
  {"label":"The New Community and New Creation","chapters":"56–66","ref":"Isaiah 56:1"}
],"key_verse":"Isaiah 53:5",
"timeline":{"date":"~740–680 BC","before":[{"label":"The divided monarchy; Amos and Hosea in the north","ref":"Amos 1:1"}],"after":[{"label":"Jeremiah — the fall of Jerusalem","ref":"Jeremiah 1:1"}]}},

{"id":"jeremiah","title":"Jeremiah","author":"Jeremiah son of Hilkiah, with his secretary Baruch son of Neriah","date":"~627–580 BC (Jeremiah's ministry; the book was compiled over this period)",
"setting":"Judah's final decades before the Babylonian exile — from Josiah's reign through the fall of Jerusalem (586 BC) and the flight to Egypt, where Jeremiah dies.",
"purpose":"To call Judah to repentance in the face of certain judgment, to announce the new covenant (ch. 31) that would replace the broken Sinai covenant, and to show that the prophet who speaks God's word faithfully will suffer rejection.",
"themes":["The new covenant written on the heart (31:31-34)","Faithless covenant — Judah as an unfaithful wife","Jeremiah's confessions — the cost of prophetic ministry","Babylon as God's instrument of judgment","The Rechabites as a model of covenant faithfulness","Restoration after exile (chs. 30–33, 'the Book of Comfort')"],
"outline":[
  {"label":"Jeremiah's Call and Early Ministry","chapters":"1–6","ref":"Jeremiah 1:1"},
  {"label":"Temple Sermons and Conflict with False Prophets","chapters":"7–29","ref":"Jeremiah 7:1"},
  {"label":"The Book of Comfort: New Covenant","chapters":"30–33","ref":"Jeremiah 30:1"},
  {"label":"The Fall of Jerusalem and Its Aftermath","chapters":"34–52","ref":"Jeremiah 34:1"}
],"key_verse":"Jeremiah 31:33",
"timeline":{"date":"~627–580 BC","before":[{"label":"Josiah's reforms","ref":"2 Kings 22:1"}],"after":[{"label":"Lamentations — mourning Jerusalem's fall","ref":"Lamentations 1:1"}]}},

{"id":"lamentations","title":"Lamentations","author":"Jeremiah (Jewish and early Christian tradition); the text is anonymous","date":"~586 BC, shortly after the fall of Jerusalem",
"setting":"Jerusalem immediately after the Babylonian destruction of the city and temple. Five poems of intense grief over the desolation.",
"purpose":"To give voice to the corporate grief of the covenant people over God's judgment, to acknowledge the justice of that judgment, and to cling to the hope of God's mercy in the midst of suffering.",
"themes":["Grief and lament as a legitimate spiritual practice","God's justice in the judgment of Jerusalem","Clinging to hope: 'his mercies never come to an end' (3:22-23)","The personification of Zion as a grieving woman","Petition for restoration"],
"outline":[
  {"label":"Poem 1: Zion's Desolation (22 verses, acrostic)","chapters":"1","ref":"Lamentations 1:1"},
  {"label":"Poem 2: God's Anger","chapters":"2","ref":"Lamentations 2:1"},
  {"label":"Poem 3: Personal Lament and Hope (66 verses)","chapters":"3","ref":"Lamentations 3:1"},
  {"label":"Poem 4: The Siege's Horror","chapters":"4","ref":"Lamentations 4:1"},
  {"label":"Poem 5: Prayer for Restoration","chapters":"5","ref":"Lamentations 5:1"}
],"key_verse":"Lamentations 3:22",
"timeline":{"date":"~586 BC","before":[{"label":"Fall of Jerusalem to Babylon","ref":"2 Kings 25:1"}],"after":[{"label":"Ezekiel — prophecy from Babylon","ref":"Ezekiel 1:1"}]}},

{"id":"ezekiel","title":"Ezekiel","author":"Ezekiel son of Buzi, a priest and prophet among the exiles in Babylon","date":"~593–571 BC (the book covers exactly 22 years)",
"setting":"Among the first group of exiles by the Chebar canal in Babylon, before and after the fall of Jerusalem (586 BC). Ezekiel's visions are among the most elaborate in the Bible.",
"purpose":"To explain the fall of Jerusalem as God's judgment on covenant unfaithfulness (God's glory departed — 8–11), to indict Israel's leaders and people, and to promise a breathtaking restoration — new heart, new spirit, new temple, and new creation.",
"themes":["The glory of God (kavod YHWH) — departing and returning","The watchman's responsibility","Individual accountability before God","The dry bones — resurrection and national restoration","The new covenant: a new heart and new spirit","The eschatological temple (chs. 40–48)","Gog and Magog"],
"outline":[
  {"label":"Ezekiel's Call and Warnings to Jerusalem","chapters":"1–24","ref":"Ezekiel 1:1"},
  {"label":"Oracles Against Foreign Nations","chapters":"25–32","ref":"Ezekiel 25:1"},
  {"label":"Restoration Oracles: Dry Bones, Shepherd, New Temple","chapters":"33–48","ref":"Ezekiel 33:1"}
],"key_verse":"Ezekiel 36:26",
"timeline":{"date":"~593–571 BC","before":[{"label":"Jerusalem's fall","ref":"2 Kings 25:1"}],"after":[{"label":"Daniel — God's sovereignty over Babylon","ref":"Daniel 1:1"}]}},

{"id":"daniel","title":"Daniel","author":"Daniel (affirmed by Jesus in Matthew 24:15); critical scholarship dates chapters 7–12 to the Maccabean period (~165 BC)","date":"~605–535 BC (events); composition debated",
"setting":"The Babylonian and early Persian courts, where Daniel and his three friends serve as exiles. The book divides into court narratives (chs. 1–6) and apocalyptic visions (chs. 7–12).",
"purpose":"To show God's sovereignty over the pagan nations and his certain vindication of his people, calling persecuted Jews to faithful endurance in the confidence that the 'Son of Man' will receive an everlasting kingdom.",
"themes":["God's sovereignty over history and kingdoms","Faithful witness under pagan pressure","The four world empires and the coming kingdom of God","The Son of Man (7:13-14) — cited by Jesus at his trial","The resurrection at the end of time","Apocalyptic symbolism: beasts, numbers, angels"],
"outline":[
  {"label":"Faithfulness at the Babylonian Court","chapters":"1–6","ref":"Daniel 1:1"},
  {"label":"Apocalyptic Visions of World Empires","chapters":"7–12","ref":"Daniel 7:1"}
],"key_verse":"Daniel 7:13",
"timeline":{"date":"~605–535 BC","before":[{"label":"The Babylonian exile","ref":"2 Kings 25:1"}],"after":[{"label":"Cyrus's decree; the return from exile","ref":"Ezra 1:1"}]}},

{"id":"hosea","title":"Hosea","author":"Hosea son of Beeri, prophet to the northern kingdom of Israel","date":"~755–722 BC (ministry ending just before or during Samaria's fall)",
"setting":"The northern kingdom in its final decades of decline before the Assyrian conquest (722 BC). Hosea's marriage to Gomer, who was unfaithful, becomes a living parable of Israel's unfaithfulness to YHWH.",
"purpose":"To call Israel to return to YHWH with repentance, to expose the depth of their covenant unfaithfulness (adultery is the dominant image), and to declare God's astounding, unrelenting love that will not let his people go.",
"themes":["God as the faithful husband; Israel as the unfaithful wife","Knowledge of God (da'at Elohim)","Hesed — covenant love and loyalty","Judgment as a consequence of apostasy","Hope: God will heal and restore (chs. 11, 14)","The Exodus as the paradigm of redemption"],
"outline":[
  {"label":"Hosea's Marriage as Parable","chapters":"1–3","ref":"Hosea 1:1"},
  {"label":"Israel's Unfaithfulness and Coming Judgment","chapters":"4–10","ref":"Hosea 4:1"},
  {"label":"God's Persistent Love and Promise of Restoration","chapters":"11–14","ref":"Hosea 11:1"}
],"key_verse":"Hosea 6:6",
"timeline":{"date":"~755–722 BC","before":[{"label":"Amos — judgment on Israel","ref":"Amos 1:1"}],"after":[{"label":"Fall of Samaria to Assyria","ref":"2 Kings 17:6"}]}},

{"id":"joel","title":"Joel","author":"Joel son of Pethuel","date":"Uncertain — either pre-exilic (~835–800 BC) or post-exilic (~400 BC); the book's reference to the day of the LORD and lack of mention of Assyria/Babylon suggest an early date to many scholars",
"setting":"A catastrophic locust plague serves as the occasion for Joel's prophecy — a sign of the approaching Day of the LORD. The book calls the nation to lament and repentance.",
"purpose":"To call all of Judah to genuine repentance in the face of divine judgment, and to promise that upon repentance God will restore and pour out his Spirit on all flesh — a promise Peter declares fulfilled at Pentecost (Acts 2).",
"themes":["The Day of the LORD — judgment and salvation","The locust plague as divine warning","Repentance: 'return to me with all your heart'","The outpouring of the Spirit on all flesh (2:28-32)","Restoration: God will repay what the locusts devoured","Judgment on the nations in the Valley of Decision"],
"outline":[
  {"label":"The Locust Plague and Call to Lament","chapters":"1–2:17","ref":"Joel 1:1"},
  {"label":"God's Promise of Restoration","chapters":"2:18–27","ref":"Joel 2:18"},
  {"label":"The Day of the LORD — Spirit and Judgment","chapters":"2:28–3:21","ref":"Joel 2:28"}
],"key_verse":"Joel 2:28",
"timeline":{"date":"~835 or ~400 BC (debated)","before":[],"after":[{"label":"Peter quotes Joel 2 at Pentecost","ref":"Acts 2:16"}]}},

{"id":"amos","title":"Amos","author":"Amos of Tekoa — a shepherd and dresser of sycamore figs, not a professional prophet","date":"~760–750 BC (during the reign of Jeroboam II of Israel and Uzziah of Judah)",
"setting":"A period of prosperity in the northern kingdom of Israel, masking deep social injustice and religious formalism. Amos comes from Judah to preach against the complacent northern elite.",
"purpose":"To announce God's judgment on the nations and especially on Israel for social oppression, idolatry, and the corruption of justice — and to call the nation back to covenant faithfulness.",
"themes":["God's universal moral judgment on all nations","Social justice: the oppression of the poor","Empty religion vs. true covenant faithfulness","'Let justice roll down like waters' (5:24)","The Day of the LORD as darkness, not light","The plumb line of God's righteous standard","Restoration after judgment (9:11-15)"],
"outline":[
  {"label":"Oracles Against the Nations","chapters":"1–2","ref":"Amos 1:1"},
  {"label":"Sermons Against Israel","chapters":"3–6","ref":"Amos 3:1"},
  {"label":"Five Visions of Judgment","chapters":"7–9:10","ref":"Amos 7:1"},
  {"label":"Promise of Restoration","chapters":"9:11–15","ref":"Amos 9:11"}
],"key_verse":"Amos 5:24",
"timeline":{"date":"~760–750 BC","before":[{"label":"Jeroboam II's prosperous reign in Israel","ref":"2 Kings 14:23"}],"after":[{"label":"Hosea — God's love for unfaithful Israel","ref":"Hosea 1:1"}]}},

{"id":"obadiah","title":"Obadiah","author":"Obadiah (the most common name in the OT; which of several men named Obadiah wrote it is unknown)","date":"~586 BC (after the fall of Jerusalem, if the Edomite collaboration is the context) or possibly 840 BC",
"setting":"The shortest book in the OT. Edom (descendants of Esau) is condemned for gloating over Jerusalem's destruction and assisting its enemies.",
"purpose":"To pronounce God's judgment on Edom for its proud mistreatment of Israel (Jacob's brother), and to promise the ultimate vindication of God's people and the establishment of his kingdom.",
"themes":["God's judgment on those who harm his people","Edom's pride and its fall","The sin of standing aside when a brother suffers","The Day of the LORD and its reversal","The kingdom will be the LORD's"],
"outline":[
  {"label":"Judgment on Edom","chapters":"1–14","ref":"Obadiah 1:1"},
  {"label":"The Day of the LORD and Israel's Restoration","chapters":"15–21","ref":"Obadiah 1:15"}
],"key_verse":"Obadiah 1:15",
"timeline":{"date":"~586 BC","before":[{"label":"Fall of Jerusalem","ref":"2 Kings 25:1"}],"after":[{"label":"Edom's later disappearance from history","ref":"Malachi 1:3"}]}},

{"id":"jonah","title":"Jonah","author":"Unknown; Jonah son of Amittai is the protagonist (see 2 Kings 14:25)","date":"~760 BC (if Jonah wrote it); possibly later",
"setting":"The Assyrian capital Nineveh — Israel's feared enemy — to which Jonah is called to preach. The book is unusual among the prophets in being entirely narrative.",
"purpose":"To reveal the breadth of God's compassion — extending to Gentile enemies — and to challenge Jewish exclusivism. Jonah is a mirror of Israel's own reluctance to be a light to the nations.",
"themes":["God's compassion for all nations, even enemies","The folly and futility of fleeing from God","Repentance and divine relenting from judgment","Jonah as a type of Christ (Matthew 12:40)","The Ninevites' repentance contrasted with Israel's hardness","God's sovereignty over creation"],
"outline":[
  {"label":"Jonah Flees; the Storm and the Fish","chapters":"1","ref":"Jonah 1:1"},
  {"label":"Jonah's Prayer from the Fish's Belly","chapters":"2","ref":"Jonah 2:1"},
  {"label":"Nineveh Repents","chapters":"3","ref":"Jonah 3:1"},
  {"label":"Jonah's Anger and God's Rebuke","chapters":"4","ref":"Jonah 4:1"}
],"key_verse":"Jonah 4:11",
"timeline":{"date":"~760 BC","before":[{"label":"Jeroboam II's reign (Jonah was his contemporary)","ref":"2 Kings 14:25"}],"after":[{"label":"Nineveh's later destruction (Nahum)","ref":"Nahum 1:1"}]}},

{"id":"micah","title":"Micah","author":"Micah of Moresheth, a rural Judean prophet contemporary with Isaiah","date":"~735–700 BC (during Jotham, Ahaz, and Hezekiah's reigns)",
"setting":"Judah and Samaria on the eve of the Assyrian crisis. Micah was a rural prophet — his perspective contrasts with the urban elite whom he condemns.",
"purpose":"To pronounce judgment on both Israel and Judah for injustice, false prophecy, and corrupt leadership, and to announce the coming messianic king born in Bethlehem who will shepherd the flock.",
"themes":["God's case against corrupt leadership and false prophets","Social justice: land theft, exploitation of the poor","Judgment on both Israel and Judah","The messianic king born in Bethlehem (5:2)","'What does the LORD require of you?' (6:8)","Restoration after exile"],
"outline":[
  {"label":"Judgment on Samaria and Jerusalem","chapters":"1–3","ref":"Micah 1:1"},
  {"label":"Promise of Restoration and the Messianic King","chapters":"4–5","ref":"Micah 4:1"},
  {"label":"God's Lawsuit against Israel and Hope","chapters":"6–7","ref":"Micah 6:1"}
],"key_verse":"Micah 6:8",
"timeline":{"date":"~735–700 BC","before":[{"label":"Isaiah — the great prophet of Judah","ref":"Isaiah 1:1"}],"after":[{"label":"Hezekiah's reforms","ref":"2 Kings 18:1"}]}},

{"id":"nahum","title":"Nahum","author":"Nahum the Elkoshite (location unknown)","date":"~663–612 BC (after the fall of Thebes and before Nineveh's fall)",
"setting":"Nineveh, the capital of the brutal Assyrian empire, is now the target of God's judgment — about 150 years after Jonah's mission there.",
"purpose":"To announce the certain fall of Nineveh as a comfort to Judah suffering under Assyrian cruelty, and to demonstrate that God's long-delayed judgment on arrogant oppressors will surely come.",
"themes":["The avenging justice of God","God as refuge for those who trust him","The fall of the proud — Nineveh as a case study","Comfort for the oppressed: your enemy will be destroyed","The limits of imperial power"],
"outline":[
  {"label":"God's Character: Jealous, Avenging, Patient — but Just","chapters":"1:1–14","ref":"Nahum 1:1"},
  {"label":"The Vision of Nineveh's Fall","chapters":"1:15–3:19","ref":"Nahum 1:15"}
],"key_verse":"Nahum 1:7",
"timeline":{"date":"~663–612 BC","before":[{"label":"Jonah's mission to Nineveh","ref":"Jonah 3:1"}],"after":[{"label":"Nineveh falls to Babylon and Medes, 612 BC","ref":"Zephaniah 2:13"}]}},

{"id":"habakkuk","title":"Habakkuk","author":"Habakkuk the prophet (nothing more is known of him)","date":"~609–598 BC (after Josiah's death, before or during Babylon's rise)",
"setting":"Judah under Jehoiakim, as Babylon is rising as the new world power. Habakkuk dares to complain directly to God about injustice and receives an unsettling answer.",
"purpose":"To wrestle with the problem of God's justice — if God is sovereign, why does he tolerate evil in his own people, and why does he use an even more wicked nation to judge them? The book arrives at sovereign trust: 'the righteous shall live by his faith' (2:4).",
"themes":["Honest prayer: bringing complaints to God","'Why do you tolerate evil?' — theodicy","The righteous shall live by faith (2:4 — quoted 3x in NT)","God's sovereignty over history, including wicked instruments","The oracle against Babylon","Trust and worship despite circumstances (ch. 3 psalm)"],
"outline":[
  {"label":"First Dialogue: Habakkuk's Complaint","chapters":"1:1–11","ref":"Habakkuk 1:1"},
  {"label":"Second Dialogue: God's Answer","chapters":"1:12–2:20","ref":"Habakkuk 1:12"},
  {"label":"Habakkuk's Psalm of Trust","chapters":"3","ref":"Habakkuk 3:1"}
],"key_verse":"Habakkuk 2:4",
"timeline":{"date":"~609–598 BC","before":[{"label":"Josiah's death at Megiddo","ref":"2 Kings 23:29"}],"after":[{"label":"Jeremiah — the fall of Jerusalem","ref":"Jeremiah 1:1"}]}},

{"id":"zephaniah","title":"Zephaniah","author":"Zephaniah son of Cushi (descendant of Hezekiah, according to the genealogy in 1:1)","date":"~630–625 BC (during Josiah's early reign, before his reforms)",
"setting":"Judah under Josiah, before the reforms of 621 BC. Zephaniah's message of sweeping judgment on Judah and the nations precedes Josiah's revival.",
"purpose":"To announce the coming Day of the LORD as a comprehensive judgment on all nations and on Judah's syncretism, calling Judah to seek the LORD before the day of wrath, and promising a remnant that will rejoice in God's salvation.",
"themes":["The Day of the LORD — cosmic judgment ('dies irae')","God's judgment on Judah's religious syncretism","Judgment on Nineveh, Moab, Ammon, Ethiopia, Philistia","The remnant: humble and lowly, trusting in YHWH","The great reversal: God will rejoice over his people (3:17)"],
"outline":[
  {"label":"Universal Judgment on Judah and the Nations","chapters":"1:1–3:8","ref":"Zephaniah 1:1"},
  {"label":"Call to Repentance and Promise of Restoration","chapters":"3:9–20","ref":"Zephaniah 3:9"}
],"key_verse":"Zephaniah 3:17",
"timeline":{"date":"~630–625 BC","before":[{"label":"Manasseh's idolatrous reign","ref":"2 Kings 21:1"}],"after":[{"label":"Josiah's reforms, 621 BC","ref":"2 Kings 22:1"}]}},

{"id":"haggai","title":"Haggai","author":"Haggai the prophet","date":"520 BC — the most precisely dated minor prophet (four oracles given in the second year of Darius, 520 BC)",
"setting":"Jerusalem after the first return under Zerubbabel. The temple foundation has been laid but the work has stopped for 16 years. The people are building their own houses while God's house lies in ruins.",
"purpose":"To stir the returned exiles to resume building the temple, showing that the community's poverty and frustration are directly tied to their neglect of God's house — and to promise greater glory to the rebuilt temple than the former.",
"themes":["Seeking God's kingdom first","The connection between covenant faithfulness and blessing","Encouragement to Zerubbabel: 'I am with you'","The greater glory of the second temple (Messianic)","Haggai 2:6-9 as a promise fulfilled in Christ (Hebrews 12:26)"],
"outline":[
  {"label":"Call to Rebuild: 'Consider your ways'","chapters":"1","ref":"Haggai 1:1"},
  {"label":"The Greater Glory of the Second Temple","chapters":"2:1–9","ref":"Haggai 2:1"},
  {"label":"The Blessing of Covenant Obedience","chapters":"2:10–23","ref":"Haggai 2:10"}
],"key_verse":"Haggai 2:9",
"timeline":{"date":"520 BC","before":[{"label":"Return from exile under Zerubbabel, 538 BC","ref":"Ezra 1:1"}],"after":[{"label":"Zechariah — visions of restoration, also 520 BC","ref":"Zechariah 1:1"}]}},

{"id":"zechariah","title":"Zechariah","author":"Zechariah son of Berechiah, a priest who prophesied alongside Haggai","date":"~520–480 BC (chapters 9–14 may be later)",
"setting":"Jerusalem immediately after Haggai's ministry, with the temple under construction. The book contains eight night visions (chs. 1–6) and then two burdens (chs. 9–14) with extensive messianic prophecy.",
"purpose":"To encourage the post-exilic community with visions of God's sovereign purposes for Jerusalem, to announce the coming of the messianic king (9:9 — quoted at the Triumphal Entry), and to paint an apocalyptic picture of the final victory of God.",
"themes":["God's jealousy for Jerusalem and his people","The high priest Joshua as a type of the Messiah","The Branch (6:12) — the messianic king-priest","The triumphal king on a donkey (9:9)","Thirty pieces of silver (11:12-13)","The piercing of Christ (12:10)","The cosmic battle and the LORD's coming as king"],
"outline":[
  {"label":"Eight Night Visions","chapters":"1–6","ref":"Zechariah 1:1"},
  {"label":"Questions about Fasting; Promises of Restoration","chapters":"7–8","ref":"Zechariah 7:1"},
  {"label":"First Burden: The Coming King","chapters":"9–11","ref":"Zechariah 9:1"},
  {"label":"Second Burden: The Day of the LORD","chapters":"12–14","ref":"Zechariah 12:1"}
],"key_verse":"Zechariah 9:9",
"timeline":{"date":"~520–480 BC","before":[{"label":"Haggai — temple rebuilding","ref":"Haggai 1:1"}],"after":[{"label":"Malachi — the final OT prophet","ref":"Malachi 1:1"}]}},

{"id":"malachi","title":"Malachi","author":"Malachi ('my messenger') — whether a personal name or a title is debated","date":"~450–430 BC, roughly contemporary with Nehemiah's second visit to Jerusalem",
"setting":"The post-exilic community a generation after Ezra and Nehemiah, whose reforms had eroded. Priests are offering blemished sacrifices, tithes are withheld, intermarriage is rampant, and people question God's justice.",
"purpose":"To call a disillusioned, compromising community back to covenant faithfulness through a series of disputations, and to close the OT canon with the promise of Elijah before the great and terrible Day of the LORD — fulfilled in John the Baptist.",
"themes":["God's love despite Israel's doubt","Corrupt worship and blemished sacrifices","Marriage faithfulness and divorce","Tithing and covenant faithfulness","The 'messenger of the covenant' (3:1) — John the Baptist","The coming Day of the LORD: the sun of righteousness (4:2)","Elijah who is to come (4:5-6)"],
"outline":[
  {"label":"God's Love for Israel (Disputation 1)","chapters":"1:1–5","ref":"Malachi 1:1"},
  {"label":"Corrupt Priests (Disputation 2)","chapters":"1:6–2:9","ref":"Malachi 1:6"},
  {"label":"Faithless Marriages (Disputation 3)","chapters":"2:10–16","ref":"Malachi 2:10"},
  {"label":"'Where is the God of Justice?' (Disputation 4–5)","chapters":"2:17–3:5","ref":"Malachi 2:17"},
  {"label":"Tithes and Robbing God (Disputation 6)","chapters":"3:6–12","ref":"Malachi 3:6"},
  {"label":"The Coming Day and Elijah (Disputation 7)","chapters":"3:13–4:6","ref":"Malachi 3:13"}
],"key_verse":"Malachi 3:1",
"timeline":{"date":"~450–430 BC","before":[{"label":"Nehemiah's reforms","ref":"Nehemiah 13:1"}],"after":[{"label":"400 years of silence → John the Baptist","ref":"Matthew 3:1"}]}},

# ─── New Testament ─────────────────────────────────────────────────────────────

{"id":"mark","title":"Mark","author":"John Mark, companion of Paul and Barnabas, recording Peter's eyewitness testimony (Papias, ~120 AD)","date":"~AD 45–65 (possibly the earliest Gospel written)",
"setting":"The earliest and most action-packed Gospel — the word 'immediately' (εὐθύς) appears ~41 times. Written likely in Rome for a Gentile audience familiar with Roman customs.",
"purpose":"To present Jesus as the powerful Son of God and suffering Servant — the one who came 'not to be served but to serve, and to give his life as a ransom for many' (10:45). Mark's Gospel is the Gospel of the cross.",
"themes":["Jesus as the Son of God with power over all things","The messianic secret — Jesus repeatedly silences those healed","Service and sacrifice: the way of the cross","Discipleship — the disciples repeatedly misunderstand","The suffering Son of Man","The immediacy and urgency of the Kingdom"],
"outline":[
  {"label":"The Beginning: Baptism and Temptation","chapters":"1:1–13","ref":"Mark 1:1"},
  {"label":"Galilean Ministry: Teaching and Miracles","chapters":"1:14–8:26","ref":"Mark 1:14"},
  {"label":"Peter's Confession and the Road to Jerusalem","chapters":"8:27–10:52","ref":"Mark 8:27"},
  {"label":"The Passion Week in Jerusalem","chapters":"11–15","ref":"Mark 11:1"},
  {"label":"Resurrection and the Great Commission","chapters":"16","ref":"Mark 16:1"}
],"key_verse":"Mark 10:45",
"timeline":{"date":"~AD 27–30 (events); ~AD 45–65 (writing)","before":[{"label":"John the Baptist's ministry","ref":"Mark 1:2"}],"after":[{"label":"Luke's more detailed account","ref":"Luke 1:1"}]}},

{"id":"luke","title":"Luke","author":"Luke, physician and companion of Paul (Colossians 4:14); the 'we' passages in Acts confirm his presence","date":"~AD 60–63",
"setting":"Addressed to Theophilus (a Gentile of some standing — 'most excellent'), Luke writes the most literary and historically grounded of the Gospels, beginning with formal historiographic prologue (1:1-4).",
"purpose":"To give Theophilus (and all readers) 'certainty concerning the things you have been taught' — a carefully researched, orderly account of Jesus' life, with particular attention to prayer, the Holy Spirit, the poor, women, and Gentiles.",
"themes":["Jesus as Savior of all — especially the marginalized","Prayer as the constant heartbeat of Jesus' ministry","The Holy Spirit in Jesus' life and ministry","Women as key witnesses and disciples","The journey to Jerusalem as the central narrative (9:51–19:44)","Parables found only in Luke (Prodigal Son, Good Samaritan, Pharisee/Tax Collector)","The Resurrection as vindication"],
"outline":[
  {"label":"Prologue and Birth Narratives","chapters":"1–2","ref":"Luke 1:1"},
  {"label":"Preparation and Galilean Ministry","chapters":"3–9:50","ref":"Luke 3:1"},
  {"label":"The Journey to Jerusalem","chapters":"9:51–19:44","ref":"Luke 9:51"},
  {"label":"The Passion Week and Resurrection","chapters":"19:45–24:53","ref":"Luke 19:45"}
],"key_verse":"Luke 19:10",
"timeline":{"date":"~AD 27–30 (events); ~AD 60–63 (writing)","before":[{"label":"Mark's shorter account","ref":"Mark 1:1"}],"after":[{"label":"Acts — the sequel by the same author","ref":"Acts 1:1"}]}},

{"id":"1corinthians","title":"1 Corinthians","author":"Paul, the apostle, with Sosthenes, from Ephesus","date":"~AD 53–55",
"setting":"The church at Corinth — a prosperous, cosmopolitan, deeply divided congregation in a major port city. Paul founded the church on his second missionary journey and now writes to address a series of reported problems.",
"purpose":"To address multiple crises in the Corinthian church: divisions, sexual immorality, lawsuits, food offered to idols, the misuse of spiritual gifts, and confusion about the resurrection — all rooted in an over-realized eschatology and worldly wisdom.",
"themes":["The cross as the wisdom and power of God (chs. 1–4)","Sexual ethics and the body as God's temple","Marriage, singleness, and the coming Lord","Love as the supreme gift (ch. 13)","Order in worship and the Lord's Supper","The resurrection as the foundation of Christian hope (ch. 15)","Spiritual gifts used for edification, not display"],
"outline":[
  {"label":"Divisions and the Wisdom of the Cross","chapters":"1–4","ref":"1 Corinthians 1:1"},
  {"label":"Sexual Immorality and Marriage","chapters":"5–7","ref":"1 Corinthians 5:1"},
  {"label":"Food Offered to Idols; Rights and Freedom","chapters":"8–11","ref":"1 Corinthians 8:1"},
  {"label":"Spiritual Gifts, Love, and Worship Order","chapters":"12–14","ref":"1 Corinthians 12:1"},
  {"label":"The Resurrection of the Dead","chapters":"15","ref":"1 Corinthians 15:1"},
  {"label":"Closing Instructions and Greetings","chapters":"16","ref":"1 Corinthians 16:1"}
],"key_verse":"1 Corinthians 15:3",
"timeline":{"date":"~AD 53–55","before":[{"label":"Paul's founding visit to Corinth (Acts 18)","ref":"Acts 18:1"}],"after":[{"label":"2 Corinthians — Paul defends his apostleship","ref":"2 Corinthians 1:1"}]}},

{"id":"2corinthians","title":"2 Corinthians","author":"Paul, the apostle, with Timothy, from Macedonia","date":"~AD 55–57",
"setting":"Paul writes after a painful visit to Corinth and a severe letter (now lost). A portion of the church has been reconciled to him; others follow 'super-apostles' who challenge his authority. The letter is the most autobiographical of Paul's letters.",
"purpose":"To defend the authentic apostolic ministry (suffering, weakness, and the power of Christ) against the polished self-promoters, to complete the collection for Jerusalem's poor, and to reaffirm the glory of the new covenant.",
"themes":["Strength through weakness — God's power in frailty","The new covenant and its surpassing glory","The suffering apostle as a living sermon","Comfort through shared suffering","Genuine vs. counterfeit apostleship","Generosity as grace — the Jerusalem collection","The thorn in the flesh: 'my grace is sufficient'"],
"outline":[
  {"label":"Paul's Ministry of Comfort and Reconciliation","chapters":"1–7","ref":"2 Corinthians 1:1"},
  {"label":"The Collection for Jerusalem","chapters":"8–9","ref":"2 Corinthians 8:1"},
  {"label":"Paul's Apostolic Defense (the 'Fool's Speech')","chapters":"10–13","ref":"2 Corinthians 10:1"}
],"key_verse":"2 Corinthians 12:9",
"timeline":{"date":"~AD 55–57","before":[{"label":"1 Corinthians and a painful visit","ref":"1 Corinthians 1:1"}],"after":[{"label":"Romans — written from Corinth, AD 57","ref":"Romans 1:1"}]}},

{"id":"colossians","title":"Colossians","author":"Paul, the apostle, with Timothy, from prison (~AD 60–62)","date":"~AD 60–62 (one of the 'prison epistles')",
"setting":"The church at Colossae — a city in the Lycus valley of Asia Minor — which Paul never personally visited but founded through his convert Epaphras. A dangerous syncretistic philosophy ('the Colossian heresy') has infiltrated the church.",
"purpose":"To refute a false teaching that diminished Christ by supplementing him with angelic powers, ascetic rules, and mystical visions — and to show that Christ is the fullness of God, the head of all creation and the church, in whom all things hold together.",
"themes":["The supremacy and sufficiency of Christ (1:15-20)","Christ as the image of the invisible God — the pre-eminent one","Fullness (πλήρωμα) in Christ alone","Warning against syncretism and human philosophy","The new humanity in Christ: putting off the old, putting on the new","Household code: Spirit-filled relationships"],
"outline":[
  {"label":"The Supremacy of Christ — the Hymn","chapters":"1:1–23","ref":"Colossians 1:1"},
  {"label":"Paul's Ministry and the Colossian Heresy","chapters":"1:24–2:23","ref":"Colossians 1:24"},
  {"label":"New Life in Christ — Put Off and Put On","chapters":"3–4","ref":"Colossians 3:1"}
],"key_verse":"Colossians 1:17",
"timeline":{"date":"~AD 60–62","before":[{"label":"Epaphras brings word of Colossian problems","ref":"Colossians 1:7"}],"after":[{"label":"Philemon — a personal letter from the same imprisonment","ref":"Philemon 1:1"}]}},

{"id":"1thessalonians","title":"1 Thessalonians","author":"Paul, Silas, and Timothy, from Corinth","date":"~AD 50–51 — possibly Paul's earliest surviving letter",
"setting":"The young church in Thessalonica (Macedonia), founded by Paul on his second missionary journey but quickly abandoned under persecution. Timothy has just returned with good news about the church's faith.",
"purpose":"To commend the Thessalonians' faith and love, to answer anxious questions about believers who have died before Christ's return, and to encourage further growth in holiness while they wait for the Lord.",
"themes":["Thanksgiving for persevering faith","The Second Coming (parousia) as comfort and hope","The resurrection of believers at the parousia","Holiness and sexual purity in the meantime","Encouragement to workers and the idle","'Rejoice always, pray without ceasing, give thanks'"],
"outline":[
  {"label":"Thanksgiving and Paul's Ministry at Thessalonica","chapters":"1–3","ref":"1 Thessalonians 1:1"},
  {"label":"The Call to Holiness","chapters":"4:1–12","ref":"1 Thessalonians 4:1"},
  {"label":"The Parousia and Those Who Have Died","chapters":"4:13–5:11","ref":"1 Thessalonians 4:13"},
  {"label":"Final Instructions","chapters":"5:12–28","ref":"1 Thessalonians 5:12"}
],"key_verse":"1 Thessalonians 4:13",
"timeline":{"date":"~AD 50–51","before":[{"label":"Paul's founding visit to Thessalonica (Acts 17)","ref":"Acts 17:1"}],"after":[{"label":"2 Thessalonians — clarifying the Day of the Lord","ref":"2 Thessalonians 1:1"}]}},

{"id":"2thessalonians","title":"2 Thessalonians","author":"Paul, Silas, and Timothy","date":"~AD 50–52 (shortly after 1 Thessalonians)",
"setting":"The same Thessalonian church, apparently still unsettled about the return of Christ — now troubled by a false report claiming the Day of the Lord has already come.",
"purpose":"To correct the false teaching that the Day of the Lord has already arrived, to instruct the church on the events preceding Christ's return (the apostasy and the 'man of lawlessness'), and to address idleness in the community.",
"themes":["The man of lawlessness and the apostasy before the Day","God's righteous judgment: relief for the persecuted, punishment for persecutors","Christian calling and election","'If anyone is unwilling to work, let him not eat' — against idleness","Standing firm and holding to apostolic teaching"],
"outline":[
  {"label":"Thanksgiving and Encouragement in Persecution","chapters":"1","ref":"2 Thessalonians 1:1"},
  {"label":"The Man of Lawlessness and the Day of the Lord","chapters":"2","ref":"2 Thessalonians 2:1"},
  {"label":"Instructions on Orderly Living","chapters":"3","ref":"2 Thessalonians 3:1"}
],"key_verse":"2 Thessalonians 2:15",
"timeline":{"date":"~AD 50–52","before":[{"label":"1 Thessalonians — first letter","ref":"1 Thessalonians 1:1"}],"after":[{"label":"Galatians or 1 Corinthians","ref":"Galatians 1:1"}]}},

{"id":"1timothy","title":"1 Timothy","author":"Paul, the apostle (disputed by some scholars; affirmed by Paul and tradition)","date":"~AD 62–65",
"setting":"Written to Timothy, Paul's young co-worker, left at Ephesus to correct false teaching and establish proper church order. One of three 'pastoral epistles' (1 & 2 Timothy, Titus).",
"purpose":"To equip Timothy to lead the Ephesian church well — confronting false teachers, establishing proper worship and prayer, qualifications for overseers and deacons, care for widows, and Timothy's own conduct as a minister of the gospel.",
"themes":["Sound doctrine vs. empty speculation","Qualifications for church leaders (overseers and deacons)","Public worship: prayer for all people","Women in the assembly","Care for widows and elders","Godliness with contentment as great gain","Timothy's personal charge to fight the good fight"],
"outline":[
  {"label":"False Teachers and Proper Worship","chapters":"1–2","ref":"1 Timothy 1:1"},
  {"label":"Qualifications for Overseers and Deacons","chapters":"3","ref":"1 Timothy 3:1"},
  {"label":"Instructions for Timothy's Ministry","chapters":"4–5","ref":"1 Timothy 4:1"},
  {"label":"Wealth, Contentment, and the Good Fight","chapters":"6","ref":"1 Timothy 6:1"}
],"key_verse":"1 Timothy 3:15",
"timeline":{"date":"~AD 62–65","before":[{"label":"Paul's release from first Roman imprisonment","ref":"Philippians 1:25"}],"after":[{"label":"Titus — similar instructions for Crete","ref":"Titus 1:1"}]}},

{"id":"2timothy","title":"2 Timothy","author":"Paul, the apostle, from prison in Rome (second imprisonment)","date":"~AD 67, shortly before Paul's execution",
"setting":"Paul's last letter — written from prison expecting his imminent death (4:6-8). He writes to summon Timothy to come and to charge him to guard the gospel faithfully in the coming days of difficulty.",
"purpose":"To give Timothy a final charge to preach the word, endure hardship, guard sound doctrine, and not be ashamed of the gospel or of Paul the prisoner — as Paul himself faces death with confidence in the resurrection.",
"themes":["Faithful endurance in suffering","The sufficiency of Scripture (3:16-17)","Sound doctrine in the face of apostasy","Paul's confident farewell: 'I have finished the race'","The charge to 'preach the word, in season and out of season'","Passing the gospel on: faithful men teaching faithful men (2:2)"],
"outline":[
  {"label":"Thanksgiving and Call to Boldness","chapters":"1","ref":"2 Timothy 1:1"},
  {"label":"A Good Soldier, Workman, and Vessel","chapters":"2","ref":"2 Timothy 2:1"},
  {"label":"Godlessness in the Last Days; Scripture's Sufficiency","chapters":"3","ref":"2 Timothy 3:1"},
  {"label":"Paul's Final Charge and Farewell","chapters":"4","ref":"2 Timothy 4:1"}
],"key_verse":"2 Timothy 4:7",
"timeline":{"date":"~AD 67","before":[{"label":"Paul's first Roman imprisonment (Philippians)","ref":"Philippians 1:1"}],"after":[{"label":"Paul's execution under Nero, ~AD 67–68","ref":"2 Timothy 4:6"}]}},

{"id":"titus","title":"Titus","author":"Paul, the apostle","date":"~AD 62–65",
"setting":"Written to Titus, Paul's co-worker left in Crete to appoint elders and correct problems in the churches there. Crete had a reputation for immorality (Paul quotes the Cretan poet Epimenides, 1:12).",
"purpose":"To equip Titus to establish godly leadership, teach sound doctrine to different groups (older men, older women, young men, slaves), and combat the Jewish-Christian false teachers who were disrupting households.",
"themes":["Qualifications for elders","Sound doctrine producing godly living","Grace as the foundation of ethical transformation","Good works as the natural fruit of the gospel","The appearing of Christ as motivation for holiness","Titus's authority and the rejection of divisive people"],
"outline":[
  {"label":"Qualifications for Elders and Refuting False Teaching","chapters":"1","ref":"Titus 1:1"},
  {"label":"Sound Doctrine for All Groups","chapters":"2","ref":"Titus 2:1"},
  {"label":"Saved to Do Good Works; Final Instructions","chapters":"3","ref":"Titus 3:1"}
],"key_verse":"Titus 2:11",
"timeline":{"date":"~AD 62–65","before":[{"label":"Paul's work on Crete (Acts 27 passes Crete)","ref":"Titus 1:5"}],"after":[{"label":"2 Timothy — Paul's final letter","ref":"2 Timothy 1:1"}]}},

{"id":"philemon","title":"Philemon","author":"Paul, the apostle, with Timothy, from prison","date":"~AD 60–62 (same imprisonment as Colossians)",
"setting":"The shortest of Paul's letters — a personal note to Philemon, a wealthy Christian whose slave Onesimus has run away, met Paul, been converted, and is being returned. The letter does not directly call for Onesimus's freedom but masterfully implies it.",
"purpose":"To appeal to Philemon to receive Onesimus back as 'a beloved brother' rather than a runaway slave — modeling the social transformation that the gospel works within existing social structures, without political revolution.",
"themes":["The gospel's power to transform social relationships","Brotherhood in Christ transcending social hierarchy","Paul's appeal rather than command — the ethic of love","Forgiveness and restoration","The intercession of Christ modeled in Paul's plea"],
"outline":[
  {"label":"Greeting and Thanksgiving for Philemon","chapters":"1–7","ref":"Philemon 1:1"},
  {"label":"Paul's Appeal for Onesimus","chapters":"8–21","ref":"Philemon 1:8"},
  {"label":"Final Greetings","chapters":"22–25","ref":"Philemon 1:22"}
],"key_verse":"Philemon 1:16",
"timeline":{"date":"~AD 60–62","before":[{"label":"Same imprisonment as Colossians and Ephesians","ref":"Colossians 4:9"}],"after":[{"label":"Paul's release and resumed travels","ref":"Philippians 1:25"}]}},

{"id":"hebrews","title":"Hebrews","author":"Unknown (Paul, Apollos, Priscilla, Barnabas, and Luke have all been suggested); Origen: 'only God knows'","date":"~AD 60–70 (before Jerusalem's fall, since the temple is spoken of as still standing)","setting":"Written to Jewish Christians under pressure to revert to Judaism — possibly in Rome (13:24) or Palestine. The argument is sophisticated and steeped in the OT.",
"purpose":"To demonstrate the absolute superiority of Christ over all the institutions of Judaism — prophets, angels, Moses, the Aaronic priesthood, the old covenant, and the tabernacle — and to call the readers to persevering faith rather than apostasy.",
"themes":["Jesus as the final and superior word of God","Jesus as high priest after the order of Melchizedek","The new covenant superseding the old (Jeremiah 31 fulfilled)","The heavenly tabernacle and the once-for-all sacrifice","The 'hall of faith' — the OT witnesses who died in hope","Perseverance and the danger of drifting away","The discipline of sonship"],
"outline":[
  {"label":"The Supremacy of the Son over Prophets and Angels","chapters":"1–2","ref":"Hebrews 1:1"},
  {"label":"Jesus Greater than Moses and Joshua","chapters":"3–4","ref":"Hebrews 3:1"},
  {"label":"Jesus as Great High Priest — Melchizedek Order","chapters":"5–7","ref":"Hebrews 5:1"},
  {"label":"The New Covenant and the Better Sacrifice","chapters":"8–10","ref":"Hebrews 8:1"},
  {"label":"The Hall of Faith and Endurance","chapters":"11–12","ref":"Hebrews 11:1"},
  {"label":"Practical Exhortations","chapters":"13","ref":"Hebrews 13:1"}
],"key_verse":"Hebrews 4:14",
"timeline":{"date":"~AD 60–70","before":[{"label":"Paul's letters (if Pauline authorship is correct)","ref":"Romans 1:1"}],"after":[{"label":"Destruction of the temple, AD 70","ref":"Matthew 24:2"}]}},

{"id":"james","title":"James","author":"James, the brother of Jesus and leader of the Jerusalem church (not James the apostle, who was martyred ~AD 44)","date":"~AD 45–50, possibly the earliest NT letter",
"setting":"Written to 'the twelve tribes in the Dispersion' — Jewish Christians scattered outside Palestine. James draws heavily on the wisdom tradition and on Jesus' teaching (especially the Sermon on the Mount).",
"purpose":"To call Christians to a faith that works — testing the genuineness of faith by its practical outworking in trials, speech control, generosity, and prayer. James is the Proverbs of the NT.",
"themes":["Trials as the testing and maturing of faith","Wisdom from above vs. worldly wisdom","Taming the tongue — the power of words","Faith without works is dead (ch. 2)","Favoritism and the sin of partiality","The power of prayer (ch. 5)","The rich and the poor"],
"outline":[
  {"label":"Trials and Wisdom","chapters":"1","ref":"James 1:1"},
  {"label":"Faith and Partiality; Faith and Works","chapters":"2","ref":"James 2:1"},
  {"label":"Taming the Tongue; Worldly Wisdom","chapters":"3","ref":"James 3:1"},
  {"label":"Quarrels, Humility, and Boasting","chapters":"4","ref":"James 4:1"},
  {"label":"Warning to the Rich; Patience and Prayer","chapters":"5","ref":"James 5:1"}
],"key_verse":"James 2:26",
"timeline":{"date":"~AD 45–50","before":[{"label":"Jerusalem Council, ~AD 49","ref":"Acts 15:13"}],"after":[{"label":"James's martyrdom under Annas II, ~AD 62","ref":"Acts 12:17"}]}},

{"id":"1peter","title":"1 Peter","author":"Peter, the apostle, with Silvanus as secretary, from Rome ('Babylon' — 5:13)","date":"~AD 62–64",
"setting":"Written to Christians scattered across Asia Minor (modern Turkey) facing social hostility and possibly persecution under Nero. The letter is rich in OT quotation and early creedal material.",
"purpose":"To encourage suffering believers to stand firm in God's grace — grounding their endurance in the hope of Christ's resurrection and return, and calling them to holy conduct that adorns the gospel before watching pagans.",
"themes":["The living hope of the resurrection","Suffering as a participation in Christ's suffering","Holy living as aliens and strangers","The church as a royal priesthood and holy nation","Submission to governing authorities and household structures","Christ's descent and proclamation to spirits in prison","The elder's charge"],
"outline":[
  {"label":"Greeting and the Living Hope","chapters":"1:1–12","ref":"1 Peter 1:1"},
  {"label":"Holy Living as God's People","chapters":"1:13–2:12","ref":"1 Peter 1:13"},
  {"label":"Submission in Society and the Household","chapters":"2:13–3:22","ref":"1 Peter 2:13"},
  {"label":"Suffering for Righteousness; Final Exhortations","chapters":"4–5","ref":"1 Peter 4:1"}
],"key_verse":"1 Peter 1:3",
"timeline":{"date":"~AD 62–64","before":[{"label":"Paul's prison epistles — same era","ref":"Ephesians 1:1"}],"after":[{"label":"2 Peter — Peter's final letter","ref":"2 Peter 1:1"}]}},

{"id":"2peter","title":"2 Peter","author":"Peter, the apostle (some scholars dispute; 2 Pet. 3:1 presupposes 1 Peter by the same author)","date":"~AD 64–68, before Peter's execution",
"setting":"Peter writes from awareness of his approaching death (1:14) to counter the growing influence of false teachers who deny the return of Christ and use Christian freedom as license for immorality.",
"purpose":"To call the church to grow in knowledge of Christ and the Scriptures, to warn against false teachers who distort the apostolic message, and to affirm the certain coming of the Day of the Lord despite the scoffers.",
"themes":["Growth in Christian virtue and knowledge","The divine origin and authority of Scripture (1:20-21)","Warning against false teachers and their destruction","The Day of the Lord — certain, though delayed","God's patience, not weakness: 'not wishing that any should perish'","The new heavens and new earth"],
"outline":[
  {"label":"Grow in Grace and Knowledge","chapters":"1","ref":"2 Peter 1:1"},
  {"label":"Warning Against False Teachers","chapters":"2","ref":"2 Peter 2:1"},
  {"label":"The Day of the Lord and the New Creation","chapters":"3","ref":"2 Peter 3:1"}
],"key_verse":"2 Peter 3:9",
"timeline":{"date":"~AD 64–68","before":[{"label":"1 Peter and growing persecution","ref":"1 Peter 1:1"}],"after":[{"label":"Peter's martyrdom under Nero","ref":"John 21:18"}]}},

{"id":"1john","title":"1 John","author":"John the apostle (same author as the Gospel and 2–3 John; no formal address)","date":"~AD 90–95",
"setting":"Written to a community disrupted by secessionists — former members who have left, denying that Jesus came in the flesh and claiming a superior knowledge (proto-Gnosticism). John writes with pastoral urgency.",
"purpose":"To give Christians assurance of eternal life by setting out three tests of authentic Christian faith — belief in the incarnate Christ, love of the brothers, and righteousness of life — and to expose those who fail these tests.",
"themes":["God is light; walking in the light","Assurance of salvation through the three tests","Love for one another as the mark of genuine faith","The incarnation — 'in the flesh' — is non-negotiable","Confession of sin and God's faithfulness to forgive","The world vs. the children of God","The love of God as the ground of our love"],
"outline":[
  {"label":"Introduction: The Word of Life","chapters":"1:1–4","ref":"1 John 1:1"},
  {"label":"God is Light — Walk in the Light","chapters":"1:5–2:27","ref":"1 John 1:5"},
  {"label":"God's Children — Righteousness and Love","chapters":"2:28–4:21","ref":"1 John 2:28"},
  {"label":"Faith's Victory and Eternal Life","chapters":"5","ref":"1 John 5:1"}
],"key_verse":"1 John 4:19",
"timeline":{"date":"~AD 90–95","before":[{"label":"Gospel of John — also from Ephesus","ref":"John 1:1"}],"after":[{"label":"2 John and 3 John — short letters from the same elder","ref":"2 John 1:1"}]}},

{"id":"2john","title":"2 John","author":"'The elder' — John the apostle","date":"~AD 90–95",
"setting":"The shortest book in the NT (13 verses). Addressed to 'the elect lady and her children' — likely a local church and its members — warning against welcoming false teachers who deny the incarnation.",
"purpose":"To warn against showing hospitality to teachers who deny that Jesus Christ has come in the flesh — participating in such false teaching by welcoming them — while calling the community to love and to walk in the commandments.",
"themes":["Truth and love walking together","The test of Christology: Jesus came in the flesh","The danger of extending hospitality to false teachers","The commandment to love one another","'Walking in truth'"],
"outline":[
  {"label":"Greeting in Truth and Love","chapters":"1–3","ref":"2 John 1:1"},
  {"label":"Walk in Love and Truth","chapters":"4–6","ref":"2 John 1:4"},
  {"label":"Warning Against Deceivers","chapters":"7–11","ref":"2 John 1:7"},
  {"label":"Closing Hope to Visit","chapters":"12–13","ref":"2 John 1:12"}
],"key_verse":"2 John 1:9",
"timeline":{"date":"~AD 90–95","before":[{"label":"1 John — the full exposition","ref":"1 John 1:1"}],"after":[{"label":"3 John — letter about hospitality","ref":"3 John 1:1"}]}},

{"id":"3john","title":"3 John","author":"'The elder' — John the apostle","date":"~AD 90–95",
"setting":"A personal letter to Gaius, commending his hospitality to traveling missionaries, while condemning Diotrephes who refuses to receive them and maligns the elder.",
"purpose":"To commend the faithful Gaius for supporting missionaries and to censure Diotrephes for his divisive, power-hungry behavior — providing a snapshot of conflict over authority and hospitality in the early church.",
"themes":["Hospitality as partnership in the truth","Walking in the truth","Contrasting models: Gaius and Demetrius (good) vs. Diotrephes (bad)","Imitating good, not evil","Love in truth and deed"],
"outline":[
  {"label":"Praise for Gaius's Faithful Love","chapters":"1–8","ref":"3 John 1:1"},
  {"label":"Condemnation of Diotrephes","chapters":"9–11","ref":"3 John 1:9"},
  {"label":"Commendation of Demetrius and Closing","chapters":"12–14","ref":"3 John 1:12"}
],"key_verse":"3 John 1:4",
"timeline":{"date":"~AD 90–95","before":[{"label":"2 John — the companion letter","ref":"2 John 1:1"}],"after":[{"label":"Jude — written around the same era","ref":"Jude 1:1"}]}},

{"id":"jude","title":"Jude","author":"Jude, brother of Jesus and of James (Jude 1; Matthew 13:55)","date":"~AD 65–80",
"setting":"Written to an unspecified community (possibly Jewish Christian) facing the infiltration of ungodly men who pervert God's grace into licentiousness and deny Jesus Christ.",
"purpose":"To urge Christians to 'contend for the faith that was once for all delivered to the saints' against antinomian false teachers — using OT examples (fallen angels, Sodom, Cain, Balaam, Korah) to demonstrate that judgment on such people is certain.",
"themes":["Contend earnestly for the faith","The danger of antinomianism — grace as license for sin","OT examples of judgment","The preserved and called","Build yourself up in faith, prayer, and love","The doxology: God who keeps his people from stumbling"],
"outline":[
  {"label":"Greeting and the Reason for Writing","chapters":"1–4","ref":"Jude 1:1"},
  {"label":"OT Examples of Judgment on the Ungodly","chapters":"5–16","ref":"Jude 1:5"},
  {"label":"Exhortations to the Faithful; Doxology","chapters":"17–25","ref":"Jude 1:17"}
],"key_verse":"Jude 1:3",
"timeline":{"date":"~AD 65–80","before":[{"label":"James — the other letter from Jesus' brothers","ref":"James 1:1"}],"after":[{"label":"Revelation — the closing of the canon","ref":"Revelation 1:1"}]}},

]  # end BOOKS list

skipped = []
written = []
for b in BOOKS:
    path = os.path.join(OUT, b['id'] + '.json')
    if os.path.exists(path):
        skipped.append(b['id'])
        continue
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
    written.append(b['id'])

print(f"Written: {len(written)} files")
print(f"Skipped (already exist): {len(skipped)} files")
if written:
    print("New:", ', '.join(written))
