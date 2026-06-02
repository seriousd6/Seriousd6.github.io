"""
MKT Numbers chapters 25–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-numbers-25-30.py

Covers: Israel's apostasy at Baal Peor and Phinehas's zeal (ch. 25), second census of
Israel by tribes (ch. 26), daughters of Zelophehad's inheritance ruling and Joshua's
commission (ch. 27), calendar of appointed daily/Sabbath/monthly offerings and Passover/
Weeks (ch. 28), seventh-month festival offerings — Trumpets, Atonement, Tabernacles,
closing assembly (ch. 29), and laws of vows for men and women (ch. 30).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — consistent with mkt-numbers-7-12
- H430 (אֱלֹהִים): "God" all tiers
- H5387 (נָשִׂיא): "leader" not "prince" — tribal chieftains, consistent with prior scripts
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" all tiers
- H4908 (מִשְׁכָּן): "tabernacle" all tiers
- H5930 (עֹלָה): "burnt offering" all tiers
- H2403 (חַטָּאת): "sin offering" all tiers
- H8002 (שֶׁלֶם): "peace offering" L; "fellowship offering" M/T
- H4503 (מִנְחָה): "grain offering" all tiers
- H5262 (נֶסֶךְ): "drink offering" all tiers
- H7307 (רוּחַ): Context-dependent:
  - Ch. 27:16,18 = divine endowment for leadership → L/M "spirit"; T "the Spirit" (capitalized)
- H6775 (צָמַד): "joined" in L; "attached himself" M; "yoked himself" T
- H7065/H7068 (קָנָא/קִנְאָה): "zeal/jealousy" — Phinehas = zeal; God = jealous wrath;
  T surfaces the double meaning: Phinehas's human zeal mirrors and deflects divine jealousy
- H1285 (בְּרִית): "covenant" all tiers (ch. 25: "covenant of peace"; "covenant of everlasting priesthood")
- H3363 (יָקַע): "hang up before the LORD" L; "put to death publicly before the LORD" M;
  "expose publicly before the LORD" T — exact method uncertain; public judicial display is clear
- H8643 (תְּרוּעָה): "blowing of trumpets" L; "trumpet blasting" M; T = "day of trumpet blasts"
  (the origin of Rosh Hashanah)
- H6116 (עֲצֶרֶת): "solemn assembly" L/M; "closing assembly" T (the 8th day of Tabernacles)
- H5088 (נֶדֶר): "vow" all tiers
- H7621 (שְׁבֻעָה): "oath" all tiers
- H631/H632 (אָסַר/אִסָּר): "bind/bond" L/M; "binding pledge" T
- H5106 (נוּא): "disallow" L/M; "annul/object" T
- H6565 (פָּרַר): "make void" L/M; "annul" T
- H5315 (נֶפֶשׁ): "soul" L (in vow context = the person who binds themselves);
  M/T = "herself/himself" or "this obligation upon her"
- Chapter 25 note: The Baal Peor incident is told with extreme economy — Phinehas's act
  takes three words in Hebrew. The text does not moralize; the plague stopping is the verdict.
  T tier preserves the stark brevity while surfacing the theological freight.
- Chapter 26 note: The census is theologically purposeful — a new generation counts itself
  after the Sinai generation perished. The climax is v.64-65: not one person from the first
  census appears here except Caleb and Joshua. T tier varies for major tribes and notes
  significant genealogical details (Korah's sons surviving, Zelophehad's daughters named).
- Chapter 27 note: Daughters of Zelophehad is the first recorded legal test case extending
  women's inheritance rights. The LORD rules explicitly in their favor. T tier surfaces the
  judicial significance. Joshua's commission uses H7307 (רוּחַ) — "in whom is the Spirit" —
  linking leadership to the Spirit given to the seventy elders (ch. 11).
- Chapters 28-29 note: The seven days of Tabernacles feature a bull count that decreases
  from 13 to 7 (total: 70). Rabbinic tradition reads these as intercession for the 70 nations.
  T tier notes this at 29:39.
- Chapter 30 note: Vow laws assume patriarchal household authority (father over daughter,
  husband over wife) but include a key protection: the LORD forgives the woman when her vow
  is legitimately annulled. Widows and divorced women hold full responsibility for their vows.
  T tier surfaces these distinctions without editorializing.
"""
import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

NUMBERS = {
  "25": {
    "1": {
      "L": "And Israel abode in Shittim, and the people began to commit whoredom with the daughters of Moab.",
      "M": "While Israel was dwelling in Shittim, the people began to commit fornication with the daughters of Moab.",
      "T": "At Shittim — with the promised land in sight across the Jordan — Israel fell into sexual immorality with the women of Moab."
    },
    "2": {
      "L": "And they called the people unto the sacrifices of their gods: and the people did eat, and bowed down to their gods.",
      "M": "The Moabite women invited the people to the sacrifices of their gods, and the people ate and bowed down to their gods.",
      "T": "Table fellowship led to worship. The women invited Israel to their sacrificial feasts — and Israel ate at pagan altars and bowed before pagan gods."
    },
    "3": {
      "L": "And Israel joined himself unto Baal-peor: and the anger of the LORD was kindled against Israel.",
      "M": "Israel yoked itself to Baal of Peor, and the LORD's anger burned against Israel.",
      "T": "Israel had yoked itself to Baal of Peor — a rival god, a dead end. The LORD's anger ignited."
    },
    "4": {
      "L": "And the LORD said unto Moses, Take all the heads of the people, and hang them up before the LORD against the sun, that the fierce anger of the LORD may be turned away from Israel.",
      "M": "The LORD said to Moses: Take all the heads of the people and put them to death publicly before the LORD in the sight of the sun, so that the fierce anger of the LORD may turn from Israel.",
      "T": "The LORD told Moses: execute the guilty leaders publicly — exposed before the LORD in broad daylight — so my burning wrath against Israel may subside."
    },
    "5": {
      "L": "And Moses said unto the judges of Israel, Slay ye every one his men that were joined unto Baal-peor.",
      "M": "Moses said to the judges of Israel: Each of you must put to death those among his men who have attached themselves to Baal of Peor.",
      "T": "Moses told the tribal judges: you are each responsible for those under your authority. Execute every man who joined himself to Baal of Peor."
    },
    "6": {
      "L": "And, behold, one of the children of Israel came and brought unto his brethren a Midianitish woman in the sight of Moses, and in the sight of all the congregation of the children of Israel, who were weeping before the door of the tabernacle of the congregation.",
      "M": "Just then, right in front of Moses and the whole congregation — who were weeping at the entrance of the tent of meeting — an Israelite man came and brought a Midianite woman to his family.",
      "T": "At the very moment the nation was weeping before the tent of meeting, an Israelite man walked up and brazenly escorted a Midianite woman into the camp — in full view of Moses and all Israel."
    },
    "7": {
      "L": "And when Phinehas, the son of Eleazar, the son of Aaron the priest, saw it, he rose up from among the congregation, and took a javelin in his hand;",
      "M": "When Phinehas son of Eleazar, son of Aaron the priest, saw it, he rose from among the congregation and took a spear in his hand.",
      "T": "Phinehas — grandson of Aaron, son of the high priest — saw what was happening. He rose from the weeping congregation, seized a spear,"
    },
    "8": {
      "L": "And he went after the man of Israel into the tent, and thrust both of them through, the man of Israel, and the woman through her belly. So the plague was stayed from the children of Israel.",
      "M": "and followed the man of Israel into the inner chamber and drove it through both of them — the man and the woman through her abdomen. So the plague stopped among the Israelites.",
      "T": "and followed the man into the inner room. One thrust killed them both. The plague stopped."
    },
    "9": {
      "L": "And those that died in the plague were twenty and four thousand.",
      "M": "Those who died in the plague numbered twenty-four thousand.",
      "T": "Twenty-four thousand were dead — the plague's toll on a single episode of faithlessness."
    },
    "10": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "11": {
      "L": "Phinehas, the son of Eleazar, the son of Aaron the priest, hath turned my wrath away from the children of Israel, while he was zealous for my sake among them, that I consumed not the children of Israel in my jealousy.",
      "M": "Phinehas son of Eleazar son of Aaron the priest has turned my wrath away from the Israelites by being zealous for my cause among them, so that I did not consume the Israelites in my jealous anger.",
      "T": "Phinehas matched my own jealous fire with his — his zeal for my honor deflected my wrath. Had he not acted, my jealousy would have consumed Israel entirely."
    },
    "12": {
      "L": "Wherefore say, Behold, I give unto him my covenant of peace:",
      "M": "Therefore say: I am giving him my covenant of peace.",
      "T": "Therefore tell him: I grant him my covenant of peace —"
    },
    "13": {
      "L": "And he shall have it, and his seed after him, even the covenant of an everlasting priesthood; because he was zealous for his God, and made an atonement for the children of Israel.",
      "M": "It shall be for him and his descendants after him a covenant of perpetual priesthood, because he was zealous for his God and made atonement for the Israelites.",
      "T": "— a covenant of everlasting priesthood for him and his line. Because he burned with zeal for his God and made atonement for Israel, the priesthood is secured through him."
    },
    "14": {
      "L": "Now the name of the Israelite that was slain, even that was slain with the Midianitish woman, was Zimri, the son of Salu, a prince of a chief house among the Simeonites.",
      "M": "The Israelite who was killed — the one killed with the Midianite woman — was Zimri son of Salu, a leader of a father's house among the Simeonites.",
      "T": "The Israelite: Zimri son of Salu — not an anonymous fool but a tribal leader, a prince of Simeon's ancestral house."
    },
    "15": {
      "L": "And the name of the Midianitish woman that was slain was Cozbi, the daughter of Zur; he was head of a people, and of a chief house in Midian.",
      "M": "The Midianite woman who was killed was Cozbi daughter of Zur; he was head of a people of a father's house in Midian.",
      "T": "The woman: Cozbi daughter of Zur — herself the daughter of a Midianite tribal chieftain. This was a deliberate provocation, not a naive entanglement."
    },
    "16": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "17": {
      "L": "Vex the Midianites, and smite them:",
      "M": "Treat the Midianites as enemies and strike them down.",
      "T": "Make war on the Midianites. Strike them."
    },
    "18": {
      "L": "For they vex you with their wiles, wherewith they have beguiled you in the matter of Peor, and in the matter of Cozbi, the daughter of a prince of Midian, their sister, which was slain in the day of the plague for Peor's sake.",
      "M": "For they dealt treacherously with you through their schemes — in the Peor affair and in the matter of Cozbi, daughter of a Midianite leader, who was killed on the day of the plague in the matter of Peor.",
      "T": "Midian engineered this. They used Cozbi as a weapon — deploying the daughter of their own chief as a deliberate snare. The plague was the consequence; Midian was the cause."
    }
  },
  "26": {
    "1": {
      "L": "And it came to pass after the plague, that the LORD spake unto Moses and unto Eleazar the son of Aaron the priest, saying,",
      "M": "After the plague, the LORD spoke to Moses and Eleazar son of Aaron the priest, saying,",
      "T": "The plague was over. A generation had been judged. The LORD now spoke to Moses and Eleazar:"
    },
    "2": {
      "L": "Take the sum of all the congregation of the children of Israel, from twenty years old and upward, throughout their fathers' houses, all that are able to go forth to war in Israel.",
      "M": "Take a census of the whole congregation of Israel — all males twenty years old and upward, by their ancestral houses, who are able to go to war.",
      "T": "Count the new generation: every Israelite male from twenty years old — the age of military service — enrolled by ancestral house."
    },
    "3": {
      "L": "And Moses and Eleazar the priest spake with them in the plains of Moab by Jordan near Jericho, saying,",
      "M": "Moses and Eleazar the priest spoke with them in the plains of Moab beside the Jordan across from Jericho, saying,",
      "T": "Moses and Eleazar issued the command in the plains of Moab, across the Jordan from Jericho — standing at the threshold of the promised land."
    },
    "4": {
      "L": "Take the sum of the people, from twenty years old and upward; as the LORD commanded Moses and the children of Israel, which went forth out of the land of Egypt.",
      "M": "Register everyone twenty years and older, as the LORD had commanded Moses — these being the Israelites who came out of Egypt.",
      "T": "Count from twenty years upward, as the LORD had commanded. These are the children of those who left Egypt, not the exodus generation itself."
    },
    "5": {
      "L": "Reuben, the eldest son of Israel: the children of Reuben; Hanoch, of whom cometh the family of the Hanochites: of Pallu, the family of the Palluites:",
      "M": "Reuben, the firstborn of Israel. Reuben's clans: from Hanoch, the Hanochites; from Pallu, the Palluites;",
      "T": "Reuben, firstborn of Israel. His clans: Hanochites from Hanoch, Palluites from Pallu;"
    },
    "6": {
      "L": "Of Hezron, the family of the Hezronites: of Carmi, the family of the Carmites.",
      "M": "from Hezron, the Hezronites; from Carmi, the Carmites.",
      "T": "Hezronites from Hezron, Carmites from Carmi."
    },
    "7": {
      "L": "These are the families of the Reubenites: and they that were numbered of them were forty and three thousand and seven hundred and thirty.",
      "M": "These are the clans of the Reubenites. Those numbered: 43,730.",
      "T": "Total Reubenites: 43,730."
    },
    "8": {
      "L": "And the sons of Pallu; Eliab.",
      "M": "The son of Pallu: Eliab.",
      "T": "Pallu's line: Eliab."
    },
    "9": {
      "L": "And the sons of Eliab; Nemuel, and Dathan, and Abiram. This is that Dathan and Abiram, which were famous in the congregation, who strove against Moses and against Aaron in the company of Korah, when they strove against the LORD:",
      "M": "The sons of Eliab: Nemuel, Dathan, and Abiram. This is the Dathan and Abiram who were prominent in the congregation — those who challenged Moses and Aaron as part of Korah's faction when they rebelled against the LORD.",
      "T": "Eliab's sons: Nemuel — and Dathan and Abiram, the two rebels who made themselves notorious by challenging Moses, Aaron, and the LORD himself in Korah's revolt."
    },
    "10": {
      "L": "And the earth opened her mouth, and swallowed them up together with Korah, when that company died, what time the fire devoured two hundred and fifty men: and they became a sign.",
      "M": "The earth opened its mouth and swallowed them along with Korah when that company died — when fire devoured the two hundred and fifty men. They became a warning sign.",
      "T": "The earth swallowed them with Korah; fire consumed the 250. Their fate was inscribed into Israel's collective memory as a permanent warning."
    },
    "11": {
      "L": "Notwithstanding the children of Korah died not.",
      "M": "But the sons of Korah did not die.",
      "T": "Korah's own sons, however, survived — their line would go on to compose many of the Psalms."
    },
    "12": {
      "L": "The sons of Simeon after their families: of Nemuel, the family of the Nemuelites: of Jamin, the family of the Jaminites: of Jachin, the family of the Jachinites:",
      "M": "The clans of Simeon: from Nemuel, the Nemuelites; from Jamin, the Jaminites; from Jachin, the Jachinites;",
      "T": "Simeon's clans: Nemuelites, Jaminites, Jachinites;"
    },
    "13": {
      "L": "Of Zerah, the family of the Zarhites: of Shaul, the family of the Shaulites.",
      "M": "from Zerah, the Zerahites; from Shaul, the Shaulites.",
      "T": "Zerahites, Shaulites."
    },
    "14": {
      "L": "These are the families of the Simeonites, twenty and two thousand and two hundred.",
      "M": "These are the clans of the Simeonites. Total: 22,200.",
      "T": "Total Simeonites: 22,200 — the smallest tribe in this census."
    },
    "15": {
      "L": "The children of Gad after their families: of Zephon, the family of the Zephonites: of Haggi, the family of the Haggites: of Shuni, the family of the Shunites:",
      "M": "The clans of Gad: from Zephon, the Zephonites; from Haggi, the Haggites; from Shuni, the Shunites;",
      "T": "Gad's clans: Zephonites, Haggites, Shunites;"
    },
    "16": {
      "L": "Of Ozni, the family of the Oznites: of Eri, the family of the Erites:",
      "M": "from Ozni, the Oznites; from Eri, the Erites;",
      "T": "Oznites, Erites;"
    },
    "17": {
      "L": "Of Arod, the family of the Arodites: and of Areli, the family of the Arelites.",
      "M": "from Arod, the Arodites; from Areli, the Arelites.",
      "T": "Arodites, Arelites."
    },
    "18": {
      "L": "These are the families of the children of Gad according to those that were numbered of them, forty thousand and five hundred.",
      "M": "These are the clans of Gad according to those numbered: 40,500.",
      "T": "Total Gadites: 40,500."
    },
    "19": {
      "L": "The sons of Judah were Er and Onan: and Er and Onan died in the land of Canaan.",
      "M": "The sons of Judah: Er and Onan. But Er and Onan died in the land of Canaan.",
      "T": "Judah's firstborn sons — Er and Onan — both died in Canaan before the exodus. Only their names survive in the genealogy."
    },
    "20": {
      "L": "And the sons of Judah after their families were; of Shelah, the family of the Shelanites: of Pharez, the family of the Pharzites: of Zerah, the family of the Zerahites.",
      "M": "The surviving clans of Judah: from Shelah, the Shelanites; from Pharez, the Pharzites; from Zerah, the Zerahites.",
      "T": "Judah's living clans: Shelanites, Pharzites, Zerahites."
    },
    "21": {
      "L": "And the sons of Pharez were; of Hezron, the family of the Hezronites: of Hamul, the family of the Hamulites.",
      "M": "The sons of Pharez: from Hezron, the Hezronites; from Hamul, the Hamulites.",
      "T": "From Pharez: Hezronites and Hamulites."
    },
    "22": {
      "L": "These are the families of Judah according to those that were numbered of them, threescore and sixteen thousand and five hundred.",
      "M": "These are the clans of Judah according to those numbered: 76,500.",
      "T": "Total Judah: 76,500 — the largest tribe in the census, consistent with the blessing of Jacob."
    },
    "23": {
      "L": "Of the sons of Issachar after their families: of Tola, the family of the Tolaites: of Pua, the family of the Punites:",
      "M": "The clans of Issachar: from Tola, the Tolaites; from Pua, the Punites;",
      "T": "Issachar's clans: Tolaites, Punites;"
    },
    "24": {
      "L": "Of Jashub, the family of the Jashubites: of Shimron, the family of the Shimronites.",
      "M": "from Jashub, the Jashubites; from Shimron, the Shimronites.",
      "T": "Jashubites, Shimronites."
    },
    "25": {
      "L": "These are the families of Issachar according to those that were numbered of them, threescore and four thousand and three hundred.",
      "M": "These are the clans of Issachar according to those numbered: 64,300.",
      "T": "Total Issachar: 64,300."
    },
    "26": {
      "L": "Of the sons of Zebulun after their families: of Sered, the family of the Sardites: of Elon, the family of the Elonites: of Jahleel, the family of the Jahleelites.",
      "M": "The clans of Zebulun: from Sered, the Sardites; from Elon, the Elonites; from Jahleel, the Jahleelites.",
      "T": "Zebulun's clans: Sardites, Elonites, Jahleelites."
    },
    "27": {
      "L": "These are the families of the Zebulunites according to those that were numbered of them, threescore thousand and five hundred.",
      "M": "These are the clans of Zebulun according to those numbered: 60,500.",
      "T": "Total Zebulun: 60,500."
    },
    "28": {
      "L": "The sons of Joseph after their families were Manasseh and Ephraim.",
      "M": "The sons of Joseph, by their clans: Manasseh and Ephraim.",
      "T": "Joseph counts through his two sons — each elevated to a full tribe."
    },
    "29": {
      "L": "Of the sons of Manasseh: of Machir, the family of the Machirites: and Machir begat Gilead: of Gilead come the family of the Gileadites.",
      "M": "From the sons of Manasseh: from Machir, the Machirites — Machir fathered Gilead — from Gilead, the Gileadites.",
      "T": "Manasseh's main line: Machir → Gilead, and from Gilead all the Gileadite clans."
    },
    "30": {
      "L": "These are the sons of Gilead: of Jeezer, the family of the Jeezerites: of Helek, the family of the Helekites:",
      "M": "The sons of Gilead: from Jeezer, the Jeezerites; from Helek, the Helekites;",
      "T": "Gilead's sons: Jeezerites, Helekites;"
    },
    "31": {
      "L": "And of Asriel, the family of the Asrielites: and of Shechem, the family of the Shechemites:",
      "M": "from Asriel, the Asrielites; from Shechem, the Shechemites;",
      "T": "Asrielites, Shechemites;"
    },
    "32": {
      "L": "And of Shemida, the family of the Shemidaites: and of Hepher, the family of the Hepherites.",
      "M": "from Shemida, the Shemidaites; from Hepher, the Hepherites.",
      "T": "Shemidaites, Hepherites."
    },
    "33": {
      "L": "And Zelophehad the son of Hepher had no sons, but daughters: and the names of the daughters of Zelophehad were Mahlah, and Noah, Hoglah, Milcah, and Tirzah.",
      "M": "Zelophehad son of Hepher had no sons, only daughters: Mahlah, Noah, Hoglah, Milcah, and Tirzah.",
      "T": "Hepher's son Zelophehad left only daughters — five of them: Mahlah, Noah, Hoglah, Milcah, and Tirzah. Their names appear here; their case will decide law in the next chapter."
    },
    "34": {
      "L": "These are the families of Manasseh, and those that were numbered of them, fifty and two thousand and seven hundred.",
      "M": "These are the clans of Manasseh. Those numbered: 52,700.",
      "T": "Total Manasseh: 52,700."
    },
    "35": {
      "L": "These are the sons of Ephraim after their families: of Shuthelah, the family of the Shuthalhites: of Becher, the family of the Bachrites: of Tahan, the family of the Tahanites.",
      "M": "The clans of Ephraim: from Shuthelah, the Shuthalhites; from Becher, the Bachrites; from Tahan, the Tahanites.",
      "T": "Ephraim's clans: Shuthalhites, Bachrites, Tahanites."
    },
    "36": {
      "L": "And these are the sons of Shuthelah: of Eran, the family of the Eranites.",
      "M": "The sons of Shuthelah: from Eran, the Eranites.",
      "T": "From Shuthelah: the Eranites."
    },
    "37": {
      "L": "These are the families of the sons of Ephraim according to those that were numbered of them, thirty and two thousand and five hundred. These are the sons of Joseph after their families.",
      "M": "These are the clans of Ephraim according to those numbered: 32,500. These are the sons of Joseph by their clans.",
      "T": "Total Ephraim: 32,500. Joseph's two tribes together: 85,200."
    },
    "38": {
      "L": "The sons of Benjamin after their families: of Bela, the family of the Belaites: of Ashbel, the family of the Ashbelites: of Ahiram, the family of the Ahiramites:",
      "M": "The clans of Benjamin: from Bela, the Belaites; from Ashbel, the Ashbelites; from Ahiram, the Ahiramites;",
      "T": "Benjamin's clans: Belaites, Ashbelites, Ahiramites;"
    },
    "39": {
      "L": "Of Shupham, the family of the Shuphamites: of Hupham, the family of the Huphamites.",
      "M": "from Shupham, the Shuphamites; from Hupham, the Huphamites.",
      "T": "Shuphamites, Huphamites."
    },
    "40": {
      "L": "And the sons of Bela were Ard and Naaman: of Ard, the family of the Ardites: and of Naaman, the family of the Naamites.",
      "M": "The sons of Bela were Ard and Naaman: from Ard, the Ardites; from Naaman, the Naamites.",
      "T": "Bela's sons Ard and Naaman each founded their own clan: Ardites and Naamites."
    },
    "41": {
      "L": "These are the sons of Benjamin after their families: and they that were numbered of them were forty and five thousand and six hundred.",
      "M": "These are the sons of Benjamin according to their clans. Those numbered: 45,600.",
      "T": "Total Benjamin: 45,600."
    },
    "42": {
      "L": "These are the sons of Dan after their families: of Shuham, the family of the Shuhamites. These are the families of Dan after their families.",
      "M": "The clans of Dan after their clans: from Shuham, the Shuhamites. These are the clans of Dan by their clans.",
      "T": "Dan's entire lineage runs through one son: Shuham — a single clan comprising the whole tribe."
    },
    "43": {
      "L": "All the families of the Shuhamites, according to those that were numbered of them, were threescore and four thousand and four hundred.",
      "M": "All the clans of the Shuhamites according to those numbered: 64,400.",
      "T": "Total Dan: 64,400 — a large tribe from a single ancestral line."
    },
    "44": {
      "L": "Of the children of Asher after their families: of Jimna, the family of the Jimnites: of Jesui, the family of the Jesuites: of Beriah, the family of the Beriites.",
      "M": "The clans of Asher: from Jimna, the Jimnites; from Jesui, the Jesuites; from Beriah, the Beriites.",
      "T": "Asher's clans: Jimnites, Jesuites, Beriites."
    },
    "45": {
      "L": "Of the sons of Beriah: of Heber, the family of the Heberites: of Malchiel, the family of the Malchielites.",
      "M": "From the sons of Beriah: from Heber, the Heberites; from Malchiel, the Malchielites.",
      "T": "Beriah's sons: Heberites and Malchielites."
    },
    "46": {
      "L": "And the name of the daughter of Asher was Serah.",
      "M": "The name of Asher's daughter was Serah.",
      "T": "A daughter of Asher: Serah — named here in a census of sons, a rare inclusion."
    },
    "47": {
      "L": "These are the families of the sons of Asher according to those that were numbered of them; who were fifty and three thousand and four hundred.",
      "M": "These are the clans of Asher according to those numbered: 53,400.",
      "T": "Total Asher: 53,400."
    },
    "48": {
      "L": "Of the sons of Naphtali after their families: of Jahzeel, the family of the Jahzeelites: of Guni, the family of the Gunites:",
      "M": "The clans of Naphtali: from Jahzeel, the Jahzeelites; from Guni, the Gunites;",
      "T": "Naphtali's clans: Jahzeelites, Gunites;"
    },
    "49": {
      "L": "Of Jezer, the family of the Jezerites: of Shillem, the family of the Shillemites.",
      "M": "from Jezer, the Jezerites; from Shillem, the Shillemites.",
      "T": "Jezerites, Shillemites."
    },
    "50": {
      "L": "These are the families of Naphtali according to their families: and they that were numbered of them were forty and five thousand and four hundred.",
      "M": "These are the clans of Naphtali according to their clans. Those numbered: 45,400.",
      "T": "Total Naphtali: 45,400."
    },
    "51": {
      "L": "These were the numbered of the children of Israel, six hundred thousand and a thousand seven hundred and thirty.",
      "M": "These were the total numbered of the Israelites: 601,730.",
      "T": "The grand total: 601,730 — a new generation, slightly fewer than the first census (603,550), ready to inherit what their parents forfeited."
    },
    "52": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "53": {
      "L": "Unto these the land shall be divided for an inheritance according to the number of names.",
      "M": "To these the land shall be divided as an inheritance according to the number of names.",
      "T": "The land will be apportioned to these — each tribe's share determined by the size of its registered population."
    },
    "54": {
      "L": "To many thou shalt give the more inheritance, and to few thou shalt give the less inheritance: to every one shall his inheritance be given according to those that were numbered of him.",
      "M": "To a larger group give a larger inheritance, and to a smaller group a smaller one. Each shall receive its inheritance proportioned to those counted.",
      "T": "More people, more land; fewer people, less. The allotment is proportionally just."
    },
    "55": {
      "L": "Notwithstanding the land shall be divided by lot: according to the names of the tribes of their fathers they shall inherit.",
      "M": "Nevertheless, the land shall be divided by lot. They shall inherit according to the names of their ancestral tribes.",
      "T": "But lot, not calculation alone, makes the final assignment — God's hand in the distribution, not merely human arithmetic."
    },
    "56": {
      "L": "According to the lot shall the possession thereof be divided between many and few.",
      "M": "By lot the possession shall be divided, whether between a larger or smaller group.",
      "T": "Lot governs all: God apportions; no one may object."
    },
    "57": {
      "L": "And these are they that were numbered of the Levites after their families: of Gershon, the family of the Gershonites: of Kohath, the family of the Kohathites: of Merari, the family of the Merarites.",
      "M": "These are the Levites enrolled by their clans: from Gershon, the Gershonites; from Kohath, the Kohathites; from Merari, the Merarites.",
      "T": "The Levites are counted separately. Their three great clans: Gershonites, Kohathites, Merarites."
    },
    "58": {
      "L": "These are the families of the Levites: the family of the Libnites, the family of the Hebronites, the family of the Mahlites, the family of the Mushites, the family of the Korathites. And Kohath begat Amram.",
      "M": "These are the Levite clans: the Libnites, the Hebronites, the Mahlites, the Mushites, and the Korathites. Kohath fathered Amram.",
      "T": "Levite sub-clans: Libnites, Hebronites, Mahlites, Mushites, and Korathites — Korah's very line, still present in Israel. Kohath's son was Amram."
    },
    "59": {
      "L": "And the name of Amram's wife was Jochebed, the daughter of Levi, whom her mother bare to Levi in Egypt: and she bare unto Amram Aaron and Moses, and Miriam their sister.",
      "M": "The name of Amram's wife was Jochebed, daughter of Levi, who was born to Levi in Egypt. She bore to Amram: Aaron, Moses, and Miriam their sister.",
      "T": "Amram's wife was Jochebed — daughter of Levi himself, born in Egypt. She is the mother of three of the most consequential figures in Israel's history: Aaron, Moses, and Miriam."
    },
    "60": {
      "L": "And unto Aaron was born Nadab, and Abihu, Eleazar, and Ithamar.",
      "M": "Aaron's sons: Nadab, Abihu, Eleazar, and Ithamar.",
      "T": "Aaron's four sons: Nadab, Abihu, Eleazar, and Ithamar."
    },
    "61": {
      "L": "And Nadab and Abihu died, when they offered strange fire before the LORD.",
      "M": "Nadab and Abihu died when they offered unauthorized fire before the LORD.",
      "T": "Nadab and Abihu are dead — struck down for offering unauthorized fire before the LORD. Of Aaron's four sons, only Eleazar and Ithamar remain."
    },
    "62": {
      "L": "And those that were numbered of them were twenty and three thousand, all males from a month old and upward: for they were not numbered among the children of Israel, because there was no inheritance given them among the children of Israel.",
      "M": "Those numbered of the Levites — all males from a month old and upward — were 23,000. They were not enrolled among the Israelites because no inheritance was given to them among the Israelites.",
      "T": "Levites: 23,000 males from a month old — counted separately because they hold no territorial inheritance. The LORD is their inheritance."
    },
    "63": {
      "L": "These are they that were numbered by Moses and Eleazar the priest, who numbered the children of Israel in the plains of Moab by Jordan near Jericho.",
      "M": "These are those numbered by Moses and Eleazar the priest, who enrolled the Israelites in the plains of Moab beside the Jordan across from Jericho.",
      "T": "This census — taken by Moses and Eleazar on the plains of Moab — was a complete registration of the new generation."
    },
    "64": {
      "L": "But among these there was not a man of them whom Moses and Aaron the priest numbered, when they numbered the children of Israel in the wilderness of Sinai.",
      "M": "But not one of these was among those Moses and Aaron had registered when they counted the Israelites in the wilderness of Sinai.",
      "T": "Not a single person from this list had appeared in the Sinai census forty years earlier."
    },
    "65": {
      "L": "For the LORD had said of them, They shall surely die in the wilderness. And there was not left a man of them, save Caleb the son of Jephunneh, and Joshua the son of Nun.",
      "M": "For the LORD had said of them: They shall surely die in the wilderness. And not one of them was left except Caleb son of Jephunneh and Joshua son of Nun.",
      "T": "The LORD's word had been kept exactly: everyone from the Sinai generation died in the wilderness. Every one. Only Caleb and Joshua appear in both censuses — the only two who had been faithful."
    }
  },
  "27": {
    "1": {
      "L": "Then came the daughters of Zelophehad, the son of Hepher, the son of Gilead, the son of Machir, the son of Manasseh, of the families of Manasseh the son of Joseph: and these are the names of his daughters; Mahlah, Noah, and Hoglah, and Milcah, and Tirzah.",
      "M": "The daughters of Zelophehad son of Hepher, son of Gilead, son of Machir, son of Manasseh — from the clans of Manasseh son of Joseph — came forward. Their names: Mahlah, Noah, Hoglah, Milcah, and Tirzah.",
      "T": "Five daughters of Zelophehad — deep in Manasseh's line, their father's name already recorded in the census — stepped forward with a legal claim. Their names: Mahlah, Noah, Hoglah, Milcah, and Tirzah."
    },
    "2": {
      "L": "And they stood before Moses, and before Eleazar the priest, and before the princes and all the congregation, by the door of the tabernacle of the congregation, saying,",
      "M": "They stood before Moses, Eleazar the priest, the leaders, and the whole congregation at the entrance of the tent of meeting, saying,",
      "T": "They stood before the full court of Israel — Moses, the high priest, the tribal leaders, all the people — at the entrance to the tent of meeting, and presented their case:"
    },
    "3": {
      "L": "Our father died in the wilderness, and he was not in the company of them that gathered themselves together against the LORD in the company of Korah; but died in his own sin, and had no sons.",
      "M": "Our father died in the wilderness. He was not among those who joined against the LORD in Korah's company; he died for his own sin and had no sons.",
      "T": "'Our father died in the wilderness — but not as a rebel. He was not with Korah. He died for his own sin, as all of that generation did. He simply had no sons.'"
    },
    "4": {
      "L": "Why should the name of our father be done away from among his family, because he hath no son? Give unto us therefore a possession among the brethren of our father.",
      "M": "Why should our father's name disappear from his clan just because he had no son? Give us a holding among our father's brothers.",
      "T": "'Why should his name vanish from his family's inheritance merely because he had daughters instead of sons? Grant us a share among our father's kinsmen.'"
    },
    "5": {
      "L": "And Moses brought their cause before the LORD.",
      "M": "Moses brought their case before the LORD.",
      "T": "Moses did not rule alone. He took their petition directly to the LORD."
    },
    "6": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD answered:"
    },
    "7": {
      "L": "The daughters of Zelophehad speak right: thou shalt surely give them a possession of an inheritance among their father's brethren; and thou shalt cause the inheritance of their father to pass unto them.",
      "M": "The daughters of Zelophehad are right. You shall certainly give them a possession as an inheritance among their father's brothers; transfer their father's inheritance to them.",
      "T": "'The daughters of Zelophehad are right. Give them an inheritance among their father's brothers — their father's share passes to them. The law changes today.'"
    },
    "8": {
      "L": "And thou shalt speak unto the children of Israel, saying, If a man die, and have no son, then ye shall cause his inheritance to pass unto his daughter.",
      "M": "Speak to the Israelites: If a man dies and has no son, his inheritance shall pass to his daughter.",
      "T": "Tell all Israel: when a man dies without a son, his inheritance passes to his daughter."
    },
    "9": {
      "L": "And if he have no daughter, then ye shall give his inheritance unto his brethren.",
      "M": "If he has no daughter, give his inheritance to his brothers.",
      "T": "No daughter? Then to his brothers."
    },
    "10": {
      "L": "And if he have no brethren, then ye shall give his inheritance unto his father's brethren.",
      "M": "If he has no brothers, give his inheritance to his father's brothers.",
      "T": "No brothers? Then to his father's brothers."
    },
    "11": {
      "L": "And if his father have no brethren, then ye shall give his inheritance unto his kinsman that is next to him of his family, and he shall possess it: and it shall be unto the children of Israel a statute of judgment, as the LORD commanded Moses.",
      "M": "And if his father has no brothers, give his inheritance to the nearest relative in his family, and he shall take possession of it. This shall be a permanent legal statute for the Israelites, as the LORD commanded Moses.",
      "T": "No father's brothers? Then the nearest kin. This ruling — daughters, brothers, father's brothers, nearest kin — is now permanent law in Israel, decreed by the LORD himself."
    },
    "12": {
      "L": "And the LORD said unto Moses, Get thee up into this mount Abarim, and see the land which I have given unto the children of Israel.",
      "M": "The LORD said to Moses: Go up into these mountains of Abarim and see the land I have given to the Israelites.",
      "T": "Then the LORD turned to Moses: climb the Abarim range. Look at the land I am giving Israel."
    },
    "13": {
      "L": "And when thou hast seen it, thou also shalt be gathered unto thy people, as Aaron thy brother was gathered.",
      "M": "When you have seen it, you too will be gathered to your people, as your brother Aaron was.",
      "T": "You will see it — but you will not enter. Like Aaron, you will be gathered to your people after that final view."
    },
    "14": {
      "L": "For ye rebelled against my commandment in the desert of Zin, in the strife of the congregation, to sanctify me at the water before their eyes: that is the water of Meribah in Kadesh in the wilderness of Zin.",
      "M": "For you rebelled against my command in the wilderness of Zin, during the community's dispute, failing to uphold my holiness before their eyes at the waters — the waters of Meribah-Kadesh in the wilderness of Zin.",
      "T": "Because at Meribah-Kadesh, when Israel was in rebellion and thirsty, you failed to honor my holiness before them. That single moment of faithlessness stands against even Moses."
    },
    "15": {
      "L": "And Moses spake unto the LORD, saying,",
      "M": "Moses spoke to the LORD, saying,",
      "T": "Moses did not protest his own sentence. He prayed for the people:"
    },
    "16": {
      "L": "Let the LORD, the God of the spirits of all flesh, set a man over the congregation,",
      "M": "May the LORD, the God of the spirits of all flesh, appoint a man over the congregation",
      "T": "'LORD — you who hold the breath of every living being — appoint someone over this congregation,"
    },
    "17": {
      "L": "Which may go out before them, and which may come in before them, and which may lead them out, and which may bring them in; that the congregation of the LORD be not as sheep which have no shepherd.",
      "M": "who will go out before them and come in before them, who will lead them out and bring them in — so that the congregation of the LORD will not be like sheep without a shepherd.",
      "T": "who will march before them and lead them back — so that the LORD's people are not left like sheep with no one to guide them.'"
    },
    "18": {
      "L": "And the LORD said unto Moses, Take thee Joshua the son of Nun, a man in whom is the spirit, and lay thine hand upon him;",
      "M": "The LORD said to Moses: Take Joshua son of Nun, a man in whom the Spirit resides, and lay your hand on him.",
      "T": "The LORD answered: take Joshua son of Nun — a man in whom the Spirit already lives — and lay your hand on him."
    },
    "19": {
      "L": "And set him before Eleazar the priest, and before all the congregation; and give him a charge in their sight.",
      "M": "Present him before Eleazar the priest and the whole congregation, and commission him in their sight.",
      "T": "Bring him before the high priest and all Israel; commission him publicly so every person witnesses it."
    },
    "20": {
      "L": "And thou shalt put some of thine honour upon him, that all the congregation of the children of Israel may be obedient.",
      "M": "Transfer some of your authority to him so that the whole congregation of Israelites will obey him.",
      "T": "Give him a portion of your own authority — enough that Israel will follow him as they have followed you."
    },
    "21": {
      "L": "And he shall stand before Eleazar the priest, who shall ask counsel for him after the judgment of Urim before the LORD: at his word shall they go out, and at his word they shall come in, both he, and all the children of Israel with him, even all the congregation.",
      "M": "He shall stand before Eleazar the priest, who shall inquire for him by the judgment of the Urim before the LORD. At his word they shall go out, and at his word they shall come in — he and all the Israelites, the whole congregation.",
      "T": "Joshua will not have Moses's direct access to God. He will consult through the Urim, mediated by the high priest. But when the priest speaks the LORD's word, all Israel moves and halts on that word."
    },
    "22": {
      "L": "And Moses did as the LORD commanded him: and he took Joshua, and set him before Eleazar the priest, and before all the congregation:",
      "M": "Moses did as the LORD commanded him. He took Joshua and presented him before Eleazar the priest and before the whole congregation.",
      "T": "Moses obeyed without delay. He brought Joshua before Eleazar and all the assembled people."
    },
    "23": {
      "L": "And he laid his hands upon him, and gave him a charge, as the LORD commanded by the hand of Moses.",
      "M": "He laid his hands on him and commissioned him, as the LORD had commanded through Moses.",
      "T": "He laid both hands on Joshua and charged him with the task — passing the mantle exactly as the LORD had specified."
    }
  },
  "28": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Command the children of Israel, and say unto them, My offering, and my bread for my sacrifices made by fire, for a sweet savour unto me, shall ye observe to offer unto me in their due season.",
      "M": "Command the Israelites: My offering — the food of my fire offerings, a pleasing aroma to me — you shall be careful to present to me at their appointed times.",
      "T": "Command Israel: the fire offerings that rise as a pleasing aroma to me must be presented at their appointed times without fail. This is my food — Israel's covenant obligation on the altar."
    },
    "3": {
      "L": "And thou shalt say unto them, This is the offering made by fire which ye shall offer unto the LORD; two lambs of the first year without spot day by day, for a continual burnt offering.",
      "M": "Say to them: This is the fire offering you shall present to the LORD — two yearling lambs without blemish each day, as a regular burnt offering.",
      "T": "The daily offering: two perfect yearling lambs, every single day without exception. This is the foundation on which all other sacrifices rest."
    },
    "4": {
      "L": "The one lamb shalt thou offer in the morning, and the other lamb shalt thou offer at even;",
      "M": "Offer one lamb in the morning and the other at twilight,",
      "T": "One at dawn, one at dusk — the day bracketed by sacrifice."
    },
    "5": {
      "L": "And a tenth part of an ephah of flour for a meat offering, mingled with the fourth part of an hin of beaten oil.",
      "M": "with a grain offering of one-tenth of an ephah of fine flour mixed with one-fourth of a hin of pressed oil.",
      "T": "Alongside the lamb: fine flour with oil — one-tenth ephah, one-quarter hin of pressed oil."
    },
    "6": {
      "L": "It is a continual burnt offering, which was ordained in mount Sinai for a sweet savour, a sacrifice made by fire unto the LORD.",
      "M": "This is the regular burnt offering, instituted at Mount Sinai as a pleasing aroma — a fire offering to the LORD.",
      "T": "This offering was established at Sinai — not an addition but the foundational rhythm of Israel's worship from the beginning."
    },
    "7": {
      "L": "And the drink offering thereof shall be the fourth part of an hin for the one lamb: in the holy place shalt thou cause the strong wine to be poured unto the LORD for a drink offering.",
      "M": "The drink offering for the first lamb: one-fourth of a hin. Pour the fermented drink as a drink offering to the LORD in the holy place.",
      "T": "One-quarter hin of fermented drink poured before the LORD in the sanctuary — wine offered to God in the place of his presence."
    },
    "8": {
      "L": "And the other lamb shalt thou offer at even: as the meat offering of the morning, and as the drink offering thereof, thou shalt offer it, a sacrifice made by fire, of a sweet savour unto the LORD.",
      "M": "Offer the second lamb at twilight with the same grain offering and drink offering as in the morning — a fire offering, a pleasing aroma to the LORD.",
      "T": "The evening lamb mirrors the morning's exactly — same grain, same drink. The day closes as it opened: with fire and aroma rising before the LORD."
    },
    "9": {
      "L": "And on the sabbath day two lambs of the first year without spot, and two tenth deals of flour for a meat offering, mingled with oil, and the drink offering thereof:",
      "M": "On the Sabbath day: two yearling lambs without blemish, a grain offering of two-tenths of an ephah of fine flour mixed with oil, and its drink offering.",
      "T": "On the Sabbath: double the daily offering — two more yearling lambs, two-tenths of flour with oil. The Sabbath is marked by abundance, not by reduction."
    },
    "10": {
      "L": "This is the burnt offering of every sabbath, beside the continual burnt offering, and his drink offering.",
      "M": "This is the Sabbath burnt offering, in addition to the regular daily burnt offering and its drink offering.",
      "T": "Sabbath additions on top of the daily — the regular offering is never suspended."
    },
    "11": {
      "L": "And in the beginnings of your months ye shall offer a burnt offering unto the LORD; two young bullocks, and one ram, seven lambs of the first year without spot;",
      "M": "At the beginning of each month, present a burnt offering to the LORD: two young bulls, one ram, and seven yearling lambs without blemish.",
      "T": "At each new moon, a full offering: two bulls, one ram, seven yearling lambs — all unblemished. Each month begins with consecration."
    },
    "12": {
      "L": "And three tenth deals of flour for a meat offering, mingled with oil, for one bullock; and two tenth deals of flour for a meat offering, mingled with oil, for one ram;",
      "M": "With each bull, a grain offering of three-tenths of an ephah of fine flour mixed with oil; with each ram, two-tenths of an ephah mixed with oil;",
      "T": "Grain alongside each animal: three-tenths ephah per bull, two-tenths per ram, all blended with oil."
    },
    "13": {
      "L": "And a several tenth deal of flour mingled with oil for a meat offering unto one lamb; for a burnt offering of a sweet savour, a sacrifice made by fire unto the LORD.",
      "M": "and one-tenth of an ephah of flour mixed with oil as a grain offering for each lamb — a burnt offering, a pleasing aroma, a fire offering to the LORD.",
      "T": "One-tenth per lamb. Every portion calculated; nothing arbitrary before the LORD."
    },
    "14": {
      "L": "And their drink offerings shall be half an hin of wine unto a bullock, and the third part of an hin unto a ram, and a fourth part of an hin unto a lamb: this is the burnt offering of every month throughout the months of the year.",
      "M": "The drink offerings: half a hin of wine for each bull, one-third of a hin for each ram, one-fourth of a hin for each lamb. This is the monthly burnt offering for every month of the year.",
      "T": "Wine portions: half a hin per bull, a third per ram, a quarter per lamb — these proportions govern every new moon, every month, year round."
    },
    "15": {
      "L": "And one kid of the goats for a sin offering unto the LORD shall be offered, beside the continual burnt offering, and his drink offering.",
      "M": "One male goat shall be offered as a sin offering to the LORD, in addition to the regular burnt offering and its drink offering.",
      "T": "Plus one goat for atonement — every new moon comes with acknowledgment of sin, not only celebration of the month."
    },
    "16": {
      "L": "And in the fourteenth day of the first month is the passover of the LORD.",
      "M": "On the fourteenth day of the first month is the LORD's Passover.",
      "T": "The fourteenth of the first month: Passover — the founding feast of Israel's identity as a redeemed people."
    },
    "17": {
      "L": "And in the fifteenth day of this month is the feast: seven days shall unleavened bread be eaten.",
      "M": "On the fifteenth day of this month is the festival; for seven days unleavened bread shall be eaten.",
      "T": "The fifteenth begins seven days of Unleavened Bread — bread without leaven, remembering the rush of redemption."
    },
    "18": {
      "L": "In the first day shall be an holy convocation; ye shall do no manner of servile work therein:",
      "M": "On the first day there shall be a holy assembly; do not do any regular work.",
      "T": "Day one: a sacred assembly, rest from ordinary labor."
    },
    "19": {
      "L": "But ye shall offer a sacrifice made by fire for a burnt offering unto the LORD; two young bullocks, and one ram, and seven lambs of the first year: they shall be unto you without blemish:",
      "M": "But you shall present a fire offering as a burnt offering to the LORD: two bulls, one ram, seven yearling lambs — all without blemish.",
      "T": "Offerings for each of the seven days: two bulls, one ram, seven yearling lambs — all perfect."
    },
    "20": {
      "L": "And their meat offering shall be of flour mingled with oil: three tenth deals shall ye offer for a bullock, and two tenth deals for a ram;",
      "M": "Their grain offering: fine flour mixed with oil — three-tenths of an ephah for each bull and two-tenths for each ram.",
      "T": "Grain: three-tenths per bull, two-tenths per ram."
    },
    "21": {
      "L": "A several tenth deal shalt thou offer for every lamb, throughout the seven lambs:",
      "M": "Offer one-tenth for each of the seven lambs.",
      "T": "One-tenth per lamb — all seven."
    },
    "22": {
      "L": "And one goat for a sin offering, to make an atonement for you.",
      "M": "And one male goat as a sin offering to make atonement for you.",
      "T": "One goat for atonement — even festival days carry this acknowledgment."
    },
    "23": {
      "L": "Ye shall offer these beside the burnt offering in the morning, which is for a continual burnt offering.",
      "M": "Offer these in addition to the morning burnt offering, which is the regular daily sacrifice.",
      "T": "All of this comes on top of the daily morning sacrifice — the festival does not replace the routine; it adds to it."
    },
    "24": {
      "L": "After this manner ye shall offer daily, throughout the seven days, the meat of the sacrifice made by fire, of a sweet savour unto the LORD: it shall be offered beside the continual burnt offering, and his drink offering.",
      "M": "In this manner, offer each day throughout the seven days the food of a fire offering — a pleasing aroma to the LORD — in addition to the regular burnt offering and its drink offering.",
      "T": "This pattern holds for all seven days of Unleavened Bread — the festive offering alongside the constant daily, holiday and routine woven together."
    },
    "25": {
      "L": "And on the seventh day ye shall have an holy convocation; ye shall do no servile work.",
      "M": "On the seventh day you shall have a holy assembly; do no regular work.",
      "T": "The seventh day closes with another sacred assembly — Unleavened Bread ends as it began, with gathered worship."
    },
    "26": {
      "L": "Also in the day of the firstfruits, when ye bring a new meat offering unto the LORD, after your weeks be out, ye shall have an holy convocation; ye shall do no servile work:",
      "M": "On the day of firstfruits, when you present a new grain offering to the LORD at your Festival of Weeks, you shall have a holy assembly; do no regular work.",
      "T": "Then at Weeks — Shavuot, the day of firstfruits, when the new harvest's grain is first offered — another sacred assembly, another day free from ordinary work."
    },
    "27": {
      "L": "But ye shall offer the burnt offering for a sweet savour unto the LORD; two young bullocks, one ram, seven lambs of the first year;",
      "M": "Present a burnt offering for a pleasing aroma to the LORD: two bulls, one ram, seven yearling lambs.",
      "T": "Shavuot's burnt offering: two bulls, one ram, seven yearling lambs."
    },
    "28": {
      "L": "And their meat offering of flour mingled with oil, three tenth deals unto one bullock, two tenth deals unto one ram,",
      "M": "With the grain offering: three-tenths of an ephah of flour mixed with oil for each bull, two-tenths for each ram,",
      "T": "Grain: three-tenths per bull, two-tenths per ram."
    },
    "29": {
      "L": "A several tenth deal unto one lamb, throughout the seven lambs;",
      "M": "One-tenth for each of the seven lambs.",
      "T": "One-tenth per lamb."
    },
    "30": {
      "L": "And one kid of the goats, to make an atonement for you.",
      "M": "One male goat to make atonement for you.",
      "T": "One goat for atonement — the harvest feast is not complete without it."
    },
    "31": {
      "L": "Ye shall offer them beside the continual burnt offering, and his meat offering, (they shall be unto you without blemish) and their drink offerings.",
      "M": "Offer these in addition to the regular burnt offering and its grain offering — they shall be without blemish — and with their drink offerings.",
      "T": "All of this alongside the regular daily sacrifice — every animal without blemish, every portion with its drink offering. This is Israel's covenant calendar through the first half of the year."
    }
  },
  "29": {
    "1": {
      "L": "And in the seventh month, on the first day of the month, ye shall have an holy convocation; ye shall do no servile work: it is a day of blowing the trumpets unto you.",
      "M": "On the first day of the seventh month you shall have a holy assembly; do no regular work. It is a day of trumpet blasting for you.",
      "T": "The first of Tishri: a sacred assembly, no labor, a day of trumpet blasts — the origin of what becomes Rosh Hashanah, the new year's awakening."
    },
    "2": {
      "L": "And ye shall offer a burnt offering for a sweet savour unto the LORD; one young bullock, one ram, and seven lambs of the first year without blemish:",
      "M": "Present a burnt offering as a pleasing aroma to the LORD: one bull, one ram, and seven yearling lambs without blemish.",
      "T": "One bull, one ram, seven yearling lambs — the offering sounding with the trumpets."
    },
    "3": {
      "L": "And their meat offering shall be of flour mingled with oil, three tenth deals for a bullock, and two tenth deals for a ram,",
      "M": "Their grain offering of flour mixed with oil: three-tenths of an ephah for the bull and two-tenths for the ram,",
      "T": "Grain: three-tenths for the bull, two-tenths for the ram."
    },
    "4": {
      "L": "And one tenth deal for one lamb, throughout the seven lambs:",
      "M": "And one-tenth for each of the seven lambs.",
      "T": "One-tenth for each of the seven lambs."
    },
    "5": {
      "L": "And one kid of the goats for a sin offering, to make an atonement for you:",
      "M": "One male goat as a sin offering to make atonement for you.",
      "T": "One goat for atonement — even the new year's trumpet day carries the weight of sin."
    },
    "6": {
      "L": "Beside the burnt offering of the month, and his meat offering, and the daily burnt offering, and his meat offering, and their drink offerings, according unto their manner, for a sweet savour, a sacrifice made by fire unto the LORD.",
      "M": "These are in addition to the monthly burnt offering with its grain offering and the daily burnt offering with its grain offering and their drink offerings, according to their prescribed manner — a fire offering, a pleasing aroma to the LORD.",
      "T": "On top of the new moon offering and the daily — the Day of Trumpets adds its own layer. Three streams of sacrifice rising together."
    },
    "7": {
      "L": "And ye shall have on the tenth day of this seventh month an holy convocation; and ye shall afflict your souls: ye shall not do any work therein:",
      "M": "On the tenth day of this seventh month you shall have a holy assembly and shall afflict yourselves; you shall do no work.",
      "T": "The tenth of Tishri: the Day of Atonement — a sacred assembly, full fasting, complete rest. This is the most solemn day in Israel's entire calendar."
    },
    "8": {
      "L": "But ye shall offer a burnt offering unto the LORD for a sweet savour; one young bullock, one ram, and seven lambs of the first year; they shall be unto you without blemish:",
      "M": "Present a burnt offering to the LORD as a pleasing aroma: one bull, one ram, and seven yearling lambs — they shall be without blemish.",
      "T": "Yom Kippur's burnt offering: one bull, one ram, seven yearling lambs — all perfect. While the nation fasts, the altar is full."
    },
    "9": {
      "L": "And their meat offering shall be of flour mingled with oil, three tenth deals to a bullock, and two tenth deals to one ram,",
      "M": "Their grain offering of flour mixed with oil: three-tenths for the bull and two-tenths for the ram,",
      "T": "Grain: three-tenths per bull, two-tenths per ram."
    },
    "10": {
      "L": "A several tenth deal for one lamb, throughout the seven lambs:",
      "M": "One-tenth for each of the seven lambs.",
      "T": "One-tenth per lamb."
    },
    "11": {
      "L": "One kid of the goats for a sin offering; beside the sin offering of atonement, and the continual burnt offering, and the meat offering of it, and their drink offerings.",
      "M": "One male goat as a sin offering, in addition to the sin offering of atonement and the regular burnt offering with its grain offering and their drink offerings.",
      "T": "Plus a sin-offering goat — alongside the special Yom Kippur rites from Leviticus 16, and on top of the daily. Atonement Day is saturated with sacrifice."
    },
    "12": {
      "L": "And on the fifteenth day of the seventh month ye shall have an holy convocation; ye shall do no servile work, and ye shall keep a feast unto the LORD seven days:",
      "M": "On the fifteenth day of the seventh month you shall have a holy assembly; do no regular work, and celebrate a feast to the LORD for seven days.",
      "T": "The fifteenth of Tishri: Tabernacles begins — seven days of feasting before the LORD. After the solemnity of Atonement comes the great joy of the harvest feast."
    },
    "13": {
      "L": "And ye shall offer a burnt offering, a sacrifice made by fire, of a sweet savour unto the LORD; thirteen young bullocks, two rams, and fourteen lambs of the first year; they shall be without blemish:",
      "M": "Present a burnt offering, a fire offering, a pleasing aroma to the LORD: thirteen young bulls, two rams, and fourteen yearling lambs — they shall be without blemish.",
      "T": "Tabernacles Day 1: thirteen bulls, two rams, fourteen yearling lambs. The thirteen bulls will count down to seven over the week — a pattern unique in Israel's calendar."
    },
    "14": {
      "L": "And their meat offering shall be of flour mingled with oil, three tenth deals unto every bullock of the thirteen bullocks, two tenth deals to each ram of the two rams,",
      "M": "Their grain offering of flour mixed with oil: three-tenths of an ephah for each of the thirteen bulls and two-tenths for each of the two rams,",
      "T": "Grain: three-tenths per bull (all thirteen), two-tenths per ram."
    },
    "15": {
      "L": "And a several tenth deal to each lamb of the fourteen lambs:",
      "M": "And one-tenth for each of the fourteen lambs.",
      "T": "One-tenth per lamb — all fourteen."
    },
    "16": {
      "L": "And one kid of the goats for a sin offering; beside the continual burnt offering, his meat offering, and his drink offering.",
      "M": "And one male goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One goat for atonement — Day 1, alongside the perpetual daily."
    },
    "17": {
      "L": "And on the second day ye shall offer twelve young bullocks, two rams, fourteen lambs of the first year without spot:",
      "M": "On the second day: twelve young bulls, two rams, fourteen yearling lambs without blemish.",
      "T": "Day 2: twelve bulls — one fewer than yesterday. Two rams and fourteen lambs remain constant throughout."
    },
    "18": {
      "L": "And their meat offering and their drink offerings for the bullocks, for the rams, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bulls, the rams, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink as prescribed, proportioned to each animal's count."
    },
    "19": {
      "L": "And one kid of the goats for a sin offering; beside the continual burnt offering, and the meat offering thereof, and their drink offerings.",
      "M": "And one male goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offerings.",
      "T": "One goat for atonement."
    },
    "20": {
      "L": "And on the third day eleven bullocks, two rams, fourteen lambs of the first year without blemish:",
      "M": "On the third day: eleven bulls, two rams, fourteen yearling lambs without blemish.",
      "T": "Day 3: eleven bulls. The count descends by one each day."
    },
    "21": {
      "L": "And their meat offering and their drink offerings for the bullocks, for the rams, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bulls, the rams, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink proportioned to each animal."
    },
    "22": {
      "L": "And one goat for a sin offering; beside the continual burnt offering, and his meat offering, and his drink offering.",
      "M": "And one goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One goat for atonement."
    },
    "23": {
      "L": "And on the fourth day ten bullocks, two rams, and fourteen lambs of the first year without blemish:",
      "M": "On the fourth day: ten bulls, two rams, and fourteen yearling lambs without blemish.",
      "T": "Day 4: ten bulls."
    },
    "24": {
      "L": "Their meat offering and their drink offerings for the bullocks, for the rams, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bulls, the rams, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink as prescribed."
    },
    "25": {
      "L": "And one kid of the goats for a sin offering; beside the continual burnt offering, his meat offering, and his drink offering.",
      "M": "And one male goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One goat for atonement."
    },
    "26": {
      "L": "And on the fifth day nine bullocks, two rams, and fourteen lambs of the first year without spot:",
      "M": "On the fifth day: nine bulls, two rams, and fourteen yearling lambs without blemish.",
      "T": "Day 5: nine bulls."
    },
    "27": {
      "L": "And their meat offering and their drink offerings for the bullocks, for the rams, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bulls, the rams, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink proportioned."
    },
    "28": {
      "L": "And one goat for a sin offering; beside the continual burnt offering, and his meat offering, and his drink offering.",
      "M": "And one goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One goat for atonement."
    },
    "29": {
      "L": "And on the sixth day eight bullocks, two rams, and fourteen lambs of the first year without blemish:",
      "M": "On the sixth day: eight bulls, two rams, and fourteen yearling lambs without blemish.",
      "T": "Day 6: eight bulls."
    },
    "30": {
      "L": "And their meat offering and their drink offerings for the bullocks, for the rams, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bulls, the rams, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink as prescribed."
    },
    "31": {
      "L": "And one goat for a sin offering; beside the continual burnt offering, his meat offering, and his drink offering.",
      "M": "And one goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One goat for atonement."
    },
    "32": {
      "L": "And on the seventh day seven bullocks, two rams, and fourteen lambs of the first year without blemish:",
      "M": "On the seventh day: seven bulls, two rams, and fourteen yearling lambs without blemish.",
      "T": "Day 7: seven bulls — the count reaches its floor. Over seven days, 70 bulls have been offered in total."
    },
    "33": {
      "L": "And their meat offering and their drink offerings for the bullocks, for the rams, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bulls, the rams, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink as prescribed for the seventh day."
    },
    "34": {
      "L": "And one goat for a sin offering; beside the continual burnt offering, his meat offering, and his drink offering.",
      "M": "And one goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One goat for atonement — the seventh day's closing."
    },
    "35": {
      "L": "On the eighth day ye shall have a solemn assembly: ye shall do no servile work therein:",
      "M": "On the eighth day you shall hold a closing assembly; do no regular work.",
      "T": "The eighth day: a final intimate gathering — the closing assembly of Tabernacles. After the great week of abundance, one quieter day to linger in the LORD's presence."
    },
    "36": {
      "L": "But ye shall offer a burnt offering, a sacrifice made by fire, of a sweet savour unto the LORD: one bullock, one ram, seven lambs of the first year without blemish:",
      "M": "Present a burnt offering, a fire offering, a pleasing aroma to the LORD: one bull, one ram, seven yearling lambs without blemish.",
      "T": "The closing day's offering: one bull, one ram, seven lambs — reduced to intimacy after seven days of abundance."
    },
    "37": {
      "L": "Their meat offering and their drink offerings for the bullock, for the ram, and for the lambs, shall be according to their number, after the manner:",
      "M": "Their grain offerings and drink offerings for the bull, the ram, and the lambs shall be according to their number, in the prescribed manner.",
      "T": "Grain and drink in their prescribed proportions."
    },
    "38": {
      "L": "And one goat for a sin offering; beside the continual burnt offering, and his meat offering, and his drink offering.",
      "M": "And one goat as a sin offering, in addition to the regular burnt offering with its grain offering and drink offering.",
      "T": "One final goat for atonement — sin addressed even on the last day."
    },
    "39": {
      "L": "These things ye shall do unto the LORD in your set feasts, beside your vows, and your freewill offerings, for your burnt offerings, and for your meat offerings, and for your drink offerings, and for your peace offerings.",
      "M": "These are what you shall offer to the LORD at your appointed festivals, in addition to your vow offerings and freewill offerings — for your burnt offerings, grain offerings, drink offerings, and fellowship offerings.",
      "T": "This complete calendar — daily, Sabbath, new moon, Passover, Weeks, Trumpets, Atonement, Tabernacles — is Israel's minimum covenant commitment. Vows and freewill offerings come on top. Over Tabernacles' seven days, 70 bulls were offered in total — one for each nation in the ancient world, making Israel's sacrifice an intercession for all humanity."
    },
    "40": {
      "L": "And Moses told the children of Israel according to all that the LORD commanded Moses.",
      "M": "Moses told the Israelites everything the LORD had commanded him.",
      "T": "Moses conveyed every detail to Israel exactly as the LORD had given it."
    }
  },
  "30": {
    "1": {
      "L": "And Moses spake unto the heads of the tribes concerning the children of Israel, saying, This is the thing which the LORD hath commanded.",
      "M": "Moses spoke to the heads of Israel's tribes, saying: This is what the LORD has commanded.",
      "T": "Moses addressed the tribal leaders directly with the LORD's instruction on vows."
    },
    "2": {
      "L": "If a man vow a vow unto the LORD, or swear an oath to bind his soul with a bond; he shall not break his word, he shall do according to all that proceedeth out of his mouth.",
      "M": "If a man makes a vow to the LORD or swears an oath to bind himself with a pledge, he must not break his word. He shall do everything he said.",
      "T": "A man who vows before the LORD — or swears an oath that binds him — is fully and unconditionally bound. His word is his obligation; he must perform every part of it."
    },
    "3": {
      "L": "If a woman also vow a vow unto the LORD, and bind herself by a bond, being in her father's house in her youth;",
      "M": "If a woman makes a vow to the LORD and binds herself with a pledge while she is in her father's household as a young woman —",
      "T": "A woman's vow, however, is subject to her household authority. If she is unmarried and living under her father when she vows —"
    },
    "4": {
      "L": "And her father hear her vow, and her bond wherewith she hath bound her soul, and her father shall hold his peace at her: then all her vows shall stand, and every bond wherewith she hath bound her soul shall stand.",
      "M": "and her father hears of her vow and the pledge she bound upon herself, but says nothing — then all her vows and every pledge binding her shall stand.",
      "T": "— and her father hears it but says nothing, her vow holds in full. Silence is consent. Every pledge she made upon herself stands."
    },
    "5": {
      "L": "But if her father disallow her in the day that he heareth; not any of her vows, or of her bonds wherewith she hath bound her soul, shall stand: and the LORD shall forgive her, because her father disallowed her.",
      "M": "But if her father disallows her on the day he hears of it, none of her vows or pledges shall stand. The LORD will forgive her, because her father disallowed her.",
      "T": "But if her father objects on the very day he hears it, not one of her vows holds. The LORD himself forgives her — the annulment is legitimate; no spiritual failure attaches to her."
    },
    "6": {
      "L": "And if she had at all an husband, when she vowed, or uttered ought out of her lips, wherewith she bound her soul;",
      "M": "If she makes a vow or rashly pledges something with her lips that binds her, and then marries —",
      "T": "If she is already married when she vows, or if a vow she made before marriage carries into her marriage —"
    },
    "7": {
      "L": "And her husband heard it, and held his peace at her in the day that he heard it: then her vows shall stand, and her bonds wherewith she bound her soul shall stand.",
      "M": "and her husband hears of it and says nothing to her on the day he hears — then her vows and the pledges binding her shall stand.",
      "T": "and her husband hears it that day and says nothing — the vow stands. His silence ratifies it."
    },
    "8": {
      "L": "But if her husband disallowed her on the day that he heard it; then he shall make her vow which she vowed, and that which she uttered with her lips, wherewith she bound her soul, of none effect: and the LORD shall forgive her.",
      "M": "But if her husband disallows her on the day he hears it, he cancels the vow she made and whatever she pledged with her lips. The LORD will forgive her.",
      "T": "If he objects on the day he hears it, every vow is annulled — whatever she spoke, whatever she pledged. The LORD forgives her; the fault is not hers."
    },
    "9": {
      "L": "But every vow of a widow, and of her that is divorced, wherewith they have bound their souls, shall stand against her.",
      "M": "Every vow of a widow or a divorced woman — any pledge with which she has bound herself — shall stand.",
      "T": "But widows and divorced women stand fully responsible for their own vows. No male authority can annul them; they hold entirely."
    },
    "10": {
      "L": "And if she vowed in her husband's house, or bound herself by a bond with an oath;",
      "M": "If she made a vow or bound herself by a pledge with an oath while living in her husband's house —",
      "T": "If she vowed while still in her husband's household —"
    },
    "11": {
      "L": "And her husband heard it, and held his peace at her, and disallowed her not: then all her vows shall stand, and every bond wherewith she bound herself shall stand.",
      "M": "and her husband heard it and said nothing and did not disallow her — then all her vows and every pledge she bound herself with shall stand.",
      "T": "and he heard it and said nothing — all her vows hold. Prolonged silence is affirmation."
    },
    "12": {
      "L": "But if her husband hath utterly made them void on the day he heard them; then whatsoever proceeded out of her lips concerning her vows, or concerning the bond of her soul, shall not stand: her husband hath made them void; and the LORD shall forgive her.",
      "M": "But if her husband completely annulled them on the day he heard them, then whatever she spoke regarding her vows or the pledges of her soul shall not stand — her husband has annulled them, and the LORD will forgive her.",
      "T": "But if he annuls them clearly on the day he hears — nothing stands. The LORD forgives her; what was undone by lawful authority was legitimately undone."
    },
    "13": {
      "L": "Every vow, and every binding oath to afflict the soul, her husband may establish it, or her husband may make it void.",
      "M": "Every vow and every binding oath of self-denial — her husband may confirm it or her husband may annul it.",
      "T": "Any vow she makes — including fasts or acts of self-denial — her husband can confirm or cancel. The authority belongs to him in this household law."
    },
    "14": {
      "L": "But if her husband altogether hold his peace at her from day to day; then he establisheth all her vows, or all her bonds, which are upon her: he confirmeth them, because he held his peace at her in the day that he heard them.",
      "M": "But if her husband says nothing to her from day to day, he confirms all her vows and pledges on her — he ratifies them, because he said nothing to her on the day he first heard them.",
      "T": "But if he hears and waits day after day without speaking, he has confirmed every vow she carries. The critical moment is the day of hearing — silence then is binding."
    },
    "15": {
      "L": "But if he shall any ways make them void after that he hath heard them; then he shall bear her iniquity.",
      "M": "But if he annuls them after he has heard them, he shall bear her guilt.",
      "T": "If he later annuls what he had already ratified by silence, he takes her guilt onto himself. The broken vow's consequence falls on him."
    },
    "16": {
      "L": "These are the statutes, which the LORD commanded Moses, between a man and his wife, between the father and his daughter, being yet in her youth in her father's house.",
      "M": "These are the statutes the LORD commanded Moses concerning the relationship between a man and his wife, and between a father and his daughter while she is still young and in her father's house.",
      "T": "These are the LORD's permanent regulations for vow-making within the household: husband and wife, father and unmarried daughter. The law acknowledges authority structures while protecting women from guilt when vows are legitimately annulled."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'numbers')
        merge_tier(existing, NUMBERS, tier_key)
        save(tier_dir, 'numbers', existing)
    print('Numbers 25–30 written.')

if __name__ == '__main__':
    main()
