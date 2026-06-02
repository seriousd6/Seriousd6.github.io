"""
MKT Numbers chapters 31–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-numbers-31-36.py

Covers: the war against Midian (ch. 31), the Transjordanian settlement of Reuben and Gad (ch. 32),
the wilderness itinerary from Rameses to Moab (ch. 33), the boundaries of Canaan (ch. 34),
Levitical cities and the cities of refuge / homicide law (ch. 35), and the daughters of
Zelophehad's marriage ruling and tribal-inheritance principle (ch. 36).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — matches prior Numbers scripts
- H430 (אֱלֹהִים): "God" in all tiers
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" all tiers
- H4908 (מִשְׁכָּן): "tabernacle" all tiers
- H5930 (עֹלָה): "burnt offering" all tiers
- H2403 (חַטָּאת): "sin offering" all tiers
- H8002 (שֶׁלֶם): "peace offering" in L; "fellowship offering" in M/T
- H4503 (מִנְחָה): "grain offering" all tiers
- H7998 (שָׁלָל) / H4455 (מַלְקוֹחַ): "spoil/plunder" and "prey/captives" — L preserves
  both terms; M/T use "plunder" and "captives" where context requires
- H7523 (רָצַח): "murder/murderer" all tiers — the intentional killing word, distinct from
  H5221 (נָכָה, "strike/slay") used for unintentional killing; this distinction drives ch. 35
- H1350 (גָּאַל): "blood avenger" L/M; "blood-avenger" T — the kinsman with right of execution
- H4733 (מִקְלָט): "refuge" all tiers — the technical term for the asylum cities
- H5159 (נַחֲלָה): "inheritance/possession" — "inheritance" in all tiers; tribal land-holding
- H1366 (גְּבוּל): "border/boundary" — "border" in L; "boundary" in M/T
- H3017 (יוֹבֵל): "Jubilee" all tiers
- H5387 (נָשִׂיא): "leader" in all tiers, not "prince" — matches prior Numbers scripts
- H4080 (מִדְיָן): "Midian/Midianites" all tiers
- Chapter 31 note: Moses's anger at sparing the Midianite women (vv.14-18) is explicitly tied
  to the Peor apostasy (ch. 25) and Balaam's counsel. T tier makes this connection explicit.
  The gold offering in vv.50-54 is a spontaneous atonement gesture by the officers — not
  commanded; note this in T tier.
- Chapter 31, v.17-18: The harsh commands are historically and theologically difficult.
  L/M render accurately; T does not soften but notes the Peor connection as the stated reason.
- Chapter 32: Moses's speech invoking the spy narrative (vv.8-15) is a deliberate echo of
  Numbers 13-14. T tier surfaces this intertextual weight.
- Chapter 33: The itinerary is a liturgical retrospective — a formal recitation, not merely a
  route description. T tier honours the solemn character of selected stops: Rephidim, Sinai,
  Kibroth-hattaavah, Hazeroth, Kadesh, Mount Hor (Aaron's death). The long undifferentiated
  middle section (vv.19-36) is preserved fully but T tier uses brief, evocative renderings.
- Chapter 33:38: Aaron's death date (fortieth year, first of fifth month) is precisely dated —
  this is a rare chronological anchor; T tier notes the finality.
- Chapter 34: Boundary geography is L/M prose; T tier notes the theological claim (this is
  given land, not conquered territory) at the boundary summary verses.
- Chapter 35: The homicide law distinguishes intent by weapon type, ambush, and enmity —
  a proto-jurisprudential taxonomy. T tier surfaces the underlying principle at each step.
  The "high priest's death as release" concept (vv.25,28) is theologically significant:
  the unintentional killer is bound to the city until death purifies the land; the high priest
  functions as a kind of corporate sin-bearer here. T tier notes this.
- Chapter 35:33-34: Blood pollution of the land is literal, not metaphorical in the Hebrew
  worldview. T tier honours this without domesticating it.
- Chapter 36: The daughters of Zelophehad case resolves the tension between women's
  inheritance rights (ch. 27) and tribal land retention. T tier notes that both values are
  honoured simultaneously — neither overrides the other.
- Verse 36:13: The final verse of Numbers functions as a colophon for the whole book;
  T tier marks this closure.
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
  "31": {
    "1": {
      "L": "And the LORD spoke to Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "Then the LORD said to Moses,"
    },
    "2": {
      "L": "Avenge the children of Israel on the Midianites; afterward you shall be gathered to your people.",
      "M": "\"Take full vengeance for the Israelites on the Midianites; after that you will be gathered to your people.\"",
      "T": "\"Exact Israel's vengeance on the Midianites — this is the last task before you are taken home to your ancestors.\""
    },
    "3": {
      "L": "And Moses spoke to the people, saying, Arm men from among you for the war, that they may go against Midian and execute the LORD's vengeance on Midian.",
      "M": "Moses said to the people, \"Arm men from among you for war so that they may march against Midian and carry out the LORD's vengeance.\"",
      "T": "Moses addressed the people: \"Equip a fighting force from your number. They will march against Midian and execute the LORD's own vengeance.\""
    },
    "4": {
      "L": "A thousand from each tribe, a thousand from each tribe throughout all the tribes of Israel, you shall send to the war.",
      "M": "Send one thousand from each tribe of Israel — one thousand per tribe — to the war.",
      "T": "Draw a thousand men from each tribe — every tribe equal, every tribe accountable — to make up the force."
    },
    "5": {
      "L": "So there were mustered out of the thousands of Israel a thousand from each tribe, twelve thousand armed for war.",
      "M": "Out of Israel's thousands, one thousand from each tribe were drafted — twelve thousand troops armed for war.",
      "T": "Twelve thousand warriors, a thousand from each tribe, were mustered and sent into battle."
    },
    "6": {
      "L": "And Moses sent them, a thousand from each tribe, to the war — with Phinehas the son of Eleazar the priest, who carried the sacred vessels and the trumpets for the alarm in his hand.",
      "M": "Moses dispatched them — a thousand from each tribe — with Phinehas son of Eleazar the priest, who carried the sacred vessels and the alarm trumpets.",
      "T": "Moses sent the force — twelve thousand strong — with Phinehas son of Eleazar serving as the priestly representative, bearing the sacred implements and the alarm trumpets."
    },
    "7": {
      "L": "And they warred against Midian, as the LORD commanded Moses, and they killed every male.",
      "M": "They waged war against Midian, as the LORD commanded Moses, and killed every male.",
      "T": "They struck Midian exactly as the LORD had ordered — every man was put to the sword."
    },
    "8": {
      "L": "And the kings of Midian they killed in addition to the rest of their slain — Evi and Rekem and Zur and Hur and Reba, the five kings of Midian; and Balaam the son of Beor they killed with the sword.",
      "M": "Among those killed were the five kings of Midian: Evi, Rekem, Zur, Hur, and Reba. They also killed Balaam son of Beor with the sword.",
      "T": "Among the fallen were Midian's five kings: Evi, Rekem, Zur, Hur, and Reba. Balaam son of Beor — the seer who set the Peor trap — was also cut down."
    },
    "9": {
      "L": "And the children of Israel took captive the women of Midian and their little ones; and all their cattle and all their flocks and all their goods they took as spoil.",
      "M": "The Israelites took the Midianite women and children captive and seized all their livestock, flocks, and goods as plunder.",
      "T": "Israel's army took the women and children prisoner, driving off every herd, every flock, every possession as spoil."
    },
    "10": {
      "L": "And all their cities in their settlements and all their encampments they burned with fire.",
      "M": "All their settled cities and all their encampments they burned to the ground.",
      "T": "Every city, every encampment Midian had occupied was put to the torch."
    },
    "11": {
      "L": "And they took all the spoil and all the prey, both of man and of beast.",
      "M": "They gathered all the plunder — both human captives and animals.",
      "T": "Everything was taken: every prisoner, every animal, every article of value."
    },
    "12": {
      "L": "And they brought the captives and the prey and the spoil to Moses and to Eleazar the priest and to the congregation of the children of Israel, at the camp at the plains of Moab by the Jordan near Jericho.",
      "M": "They brought the captives, plunder, and spoil to Moses, Eleazar the priest, and the whole Israelite congregation at the camp on the plains of Moab, beside the Jordan near Jericho.",
      "T": "The army returned to camp on the Moabite plains by the Jordan at Jericho, bringing before Moses, Eleazar, and the whole assembly every prisoner, every animal, and every piece of plunder."
    },
    "13": {
      "L": "And Moses and Eleazar the priest and all the leaders of the congregation went out to meet them outside the camp.",
      "M": "Moses, Eleazar the priest, and all the community leaders went out to meet the army outside the camp.",
      "T": "Moses, Eleazar, and all the tribal leaders marched out beyond the camp to receive the returning army."
    },
    "14": {
      "L": "And Moses was angry with the officers of the army — the commanders of thousands and the commanders of hundreds — who came from service in the battle.",
      "M": "But Moses was furious with the military officers, the commanders of thousands and of hundreds, who had returned from the campaign.",
      "T": "Moses met them with fury. He turned on the officers — every commander of a thousand, every commander of a hundred who had come back from the field."
    },
    "15": {
      "L": "And Moses said to them, Have you kept all the women alive?",
      "M": "Moses said to them, \"Have you let all the women live?\"",
      "T": "\"You kept the women alive?\" Moses demanded."
    },
    "16": {
      "L": "Behold, these women, through the counsel of Balaam, caused the children of Israel to act treacherously against the LORD in the matter of Peor, and a plague came upon the congregation of the LORD.",
      "M": "\"These very women, following Balaam's advice, led the Israelites to betray the LORD in the matter of Peor — and that brought the plague on the LORD's congregation.\"",
      "T": "\"These are the very women who, at Balaam's instruction, lured Israel into the Baal-worship at Peor. That faithlessness triggered the plague that struck down thousands in the LORD's own congregation.\""
    },
    "17": {
      "L": "Now therefore kill every male among the little ones; and every woman who has known a man by lying with him, kill.",
      "M": "\"Now kill every male child, and kill every woman who has had sexual relations with a man.\"",
      "T": "\"Execute every male child. Execute every woman who has been with a man.\""
    },
    "18": {
      "L": "But all the young girls who have not known a man by lying with him, keep alive for yourselves.",
      "M": "\"But all the young girls who have not had relations with a man, keep alive for yourselves.\"",
      "T": "\"Only the girls who have never been with a man may be kept alive.\""
    },
    "19": {
      "L": "And you, encamp outside the camp seven days; whoever has killed any person and whoever has touched any slain, purify yourselves and your captives on the third day and on the seventh day.",
      "M": "\"You must remain outside the camp for seven days. Anyone who has killed or touched a corpse must purify themselves and their captives on the third day and on the seventh day.\"",
      "T": "\"All who have killed or touched the dead are now ritually impure. Remain outside the camp for seven days, purifying yourselves and your captives on the third day and the seventh.\""
    },
    "20": {
      "L": "And you shall purify every garment and every thing made of skin and every work of goats' hair and every vessel of wood.",
      "M": "\"Purify every garment, every article of leather, everything made of goats' hair, and every wooden article.\"",
      "T": "\"Everything you brought back from battle — clothing, leather goods, woven fabrics, wooden vessels — must be purified.\""
    },
    "21": {
      "L": "And Eleazar the priest said to the men of war who had gone into the battle, This is the statute of the law that the LORD commanded Moses:",
      "M": "Eleazar the priest said to the soldiers who had gone to war, \"This is the ordinance the LORD commanded through Moses:\"",
      "T": "Eleazar spoke to the veterans as they waited outside the camp: \"Here is what the LORD's law requires regarding what you have brought back:\""
    },
    "22": {
      "L": "Only the gold and the silver, the bronze, the iron, the tin, and the lead —",
      "M": "\"Gold, silver, bronze, iron, tin, and lead —\"",
      "T": "\"Gold, silver, bronze, iron, tin, lead —\""
    },
    "23": {
      "L": "every thing that can withstand fire, you shall make go through fire, and it shall be clean; but it shall also be purified with the water of purification; and everything that cannot withstand fire you shall pass through water.",
      "M": "\"— everything that can withstand fire must be passed through fire and will then be clean; but it must also be rinsed with the purification water. Whatever fire would destroy must be passed through water.\"",
      "T": "\"— whatever survives fire must be passed through fire, then rinsed with the purification water. Whatever fire would destroy must be washed in water instead.\""
    },
    "24": {
      "L": "And you shall wash your garments on the seventh day and be clean, and afterward you may come into the camp.",
      "M": "\"Wash your clothing on the seventh day, and you will be clean; then you may enter the camp.\"",
      "T": "\"On the seventh day wash all your clothing. Once you are clean, you may return to the community.\""
    },
    "25": {
      "L": "And the LORD spoke to Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD then addressed Moses:"
    },
    "26": {
      "L": "Take the sum of the plunder that was taken, of man and of beast, you and Eleazar the priest and the heads of the fathers' houses of the congregation;",
      "M": "\"Take a full count of all the plunder captured, both persons and animals — you, Eleazar the priest, and the tribal leaders of the congregation.\"",
      "T": "\"Inventory everything captured — every person, every animal — you and Eleazar and the tribal heads together.\""
    },
    "27": {
      "L": "and divide the plunder into two parts between the warriors who went out to battle and the whole congregation.",
      "M": "\"Divide the plunder equally between the warriors who fought and the rest of the congregation.\"",
      "T": "\"Split the spoil in half: one portion to the fighting men, the other to the whole community.\""
    },
    "28": {
      "L": "And levy for the LORD a tribute from the men of war who went out to battle: one soul out of five hundred, from the persons and from the cattle and from the donkeys and from the sheep;",
      "M": "\"From the warrior's half, levy a tribute for the LORD: one in five hundred from the persons, cattle, donkeys, and sheep.\"",
      "T": "\"From the soldiers' share, one in five hundred of every category — people, cattle, donkeys, sheep — belongs to the LORD as tribute.\""
    },
    "29": {
      "L": "take it from their half and give it to Eleazar the priest as a contribution to the LORD.",
      "M": "\"Take it from their share and present it to Eleazar the priest as a contribution to the LORD.\"",
      "T": "\"Draw that amount from their share and present it to Eleazar as an offering lifted to the LORD.\""
    },
    "30": {
      "L": "And from the children of Israel's half you shall take one drawn out of every fifty, from the persons, from the cattle, from the donkeys, and from the flocks — from every kind of animal — and give them to the Levites who keep charge of the LORD's tabernacle.",
      "M": "\"From the Israelites' half, take one out of every fifty — from persons, cattle, donkeys, and flocks, every kind of animal — and give them to the Levites who maintain the LORD's tabernacle.\"",
      "T": "\"From the community's share, one in fifty of everything — persons and animals alike — goes to the Levites who serve at the LORD's tabernacle.\""
    },
    "31": {
      "L": "And Moses and Eleazar the priest did as the LORD commanded Moses.",
      "M": "Moses and Eleazar the priest did exactly as the LORD commanded Moses.",
      "T": "Moses and Eleazar carried out everything the LORD had ordered."
    },
    "32": {
      "L": "Now the prey remaining from the plunder that the army had taken was: six hundred and seventy-five thousand sheep,",
      "M": "The remaining plunder the fighting men had taken came to six hundred seventy-five thousand sheep,",
      "T": "The total inventory of what the army had captured: six hundred seventy-five thousand sheep;"
    },
    "33": {
      "L": "and seventy-two thousand cattle,",
      "M": "seventy-two thousand cattle,",
      "T": "seventy-two thousand cattle;"
    },
    "34": {
      "L": "and sixty-one thousand donkeys,",
      "M": "sixty-one thousand donkeys,",
      "T": "sixty-one thousand donkeys;"
    },
    "35": {
      "L": "and thirty-two thousand persons in all, of the women who had not known a man by lying with him.",
      "M": "and thirty-two thousand young women who had not had relations with a man.",
      "T": "thirty-two thousand young women who had not known a man."
    },
    "36": {
      "L": "And the half — the portion of those who had gone out to war — was in number three hundred and thirty-seven thousand five hundred sheep;",
      "M": "The warrior's half: three hundred thirty-seven thousand five hundred sheep;",
      "T": "The soldiers' share: three hundred thirty-seven thousand five hundred sheep;"
    },
    "37": {
      "L": "and the LORD's tribute from the sheep was six hundred and seventy-five;",
      "M": "the LORD's tribute from the sheep, six hundred seventy-five;",
      "T": "the LORD's levy from the sheep: six hundred seventy-five;"
    },
    "38": {
      "L": "and the cattle were thirty-six thousand, of which the LORD's tribute was seventy-two;",
      "M": "the cattle were thirty-six thousand, with the LORD's tribute being seventy-two;",
      "T": "thirty-six thousand cattle, the LORD's portion being seventy-two;"
    },
    "39": {
      "L": "and the donkeys were thirty thousand five hundred, of which the LORD's tribute was sixty-one;",
      "M": "the donkeys were thirty thousand five hundred, with the LORD's tribute being sixty-one;",
      "T": "thirty thousand five hundred donkeys, sixty-one for the LORD;"
    },
    "40": {
      "L": "and the persons were sixteen thousand, of whom the LORD's tribute was thirty-two persons.",
      "M": "the persons were sixteen thousand, with the LORD's tribute being thirty-two.",
      "T": "sixteen thousand persons, thirty-two of whom were designated the LORD's tribute."
    },
    "41": {
      "L": "And Moses gave the tribute that was the LORD's contribution to Eleazar the priest, as the LORD commanded Moses.",
      "M": "Moses gave the tribute — the LORD's contribution — to Eleazar the priest, as the LORD had commanded.",
      "T": "Moses handed over the LORD's entire allotted portion to Eleazar, exactly as he had been instructed."
    },
    "42": {
      "L": "And from the children of Israel's half, which Moses divided from the men who went to war —",
      "M": "From the Israelites' half — which Moses had separated from the fighting men's share —",
      "T": "From the half allocated to the community at large,"
    },
    "43": {
      "L": "the congregation's half was three hundred and thirty-seven thousand five hundred sheep,",
      "M": "the congregation received three hundred thirty-seven thousand five hundred sheep,",
      "T": "the community received: three hundred thirty-seven thousand five hundred sheep,"
    },
    "44": {
      "L": "and thirty-six thousand cattle,",
      "M": "thirty-six thousand cattle,",
      "T": "thirty-six thousand cattle,"
    },
    "45": {
      "L": "and thirty thousand five hundred donkeys,",
      "M": "thirty thousand five hundred donkeys,",
      "T": "thirty thousand five hundred donkeys,"
    },
    "46": {
      "L": "and sixteen thousand persons —",
      "M": "and sixteen thousand persons.",
      "T": "and sixteen thousand persons."
    },
    "47": {
      "L": "and from the children of Israel's half, Moses took one of every fifty, both of persons and of cattle, and gave them to the Levites who kept charge of the LORD's tabernacle, as the LORD commanded Moses.",
      "M": "From the Israelites' half, Moses took one out of every fifty — persons and animals alike — and gave them to the Levites who maintained the LORD's tabernacle, as the LORD had commanded.",
      "T": "From Israel's portion, Moses took one in fifty of persons and animals and gave them to the Levites who serve the tabernacle — following the LORD's explicit command to the letter."
    },
    "48": {
      "L": "And the officers who were over the thousands of the army — the commanders of thousands and the commanders of hundreds — came near to Moses,",
      "M": "The military officers — commanders of thousands and of hundreds — came forward to Moses",
      "T": "Then the entire officer corps — every commander of a thousand, every commander of a hundred — came forward to Moses."
    },
    "49": {
      "L": "and said to Moses, Your servants have taken a count of the warriors under our command, and not a man of us is missing.",
      "M": "and said, \"We have tallied every soldier under our command, and not one man is unaccounted for.\"",
      "T": "They said: \"We have mustered every man who served under us. Not one is missing.\""
    },
    "50": {
      "L": "And we have brought the LORD's offering — what each man found: articles of gold, armlets and bracelets, signet rings, earrings, and pendants — to make atonement for ourselves before the LORD.",
      "M": "\"So we have brought an offering to the LORD from what each man acquired: gold articles — armlets, bracelets, signet rings, earrings, and pendants — to make atonement for ourselves before the LORD.\"",
      "T": "\"So we have brought to the LORD a voluntary offering: the gold jewelry each of us took as personal spoil — armlets, bracelets, signet rings, earrings, pendants — to atone for our own souls before the LORD. No command required. We offer it because every man came home.\""
    },
    "51": {
      "L": "And Moses and Eleazar the priest received from them the gold, all the worked articles.",
      "M": "Moses and Eleazar the priest received the gold from them — all the worked articles.",
      "T": "Moses and Eleazar accepted it all — every piece of crafted gold."
    },
    "52": {
      "L": "And all the gold of the contribution that they offered to the LORD — from the commanders of thousands and the commanders of hundreds — was sixteen thousand seven hundred and fifty shekels.",
      "M": "The total gold of the offering presented to the LORD by the commanders of thousands and hundreds came to sixteen thousand seven hundred fifty shekels.",
      "T": "The gold those officers brought before the LORD totaled sixteen thousand seven hundred fifty shekels — a massive spontaneous offering."
    },
    "53": {
      "L": "For the warriors had taken spoil, every man for himself.",
      "M": "The rank-and-file soldiers had each taken spoil for themselves.",
      "T": "The common soldiers, unlike their officers, had kept their personal plunder without offering it — which was within their rights."
    },
    "54": {
      "L": "And Moses and Eleazar the priest received the gold from the commanders of thousands and hundreds and brought it into the tent of meeting as a memorial for the children of Israel before the LORD.",
      "M": "Moses and Eleazar the priest received the gold from the commanders and brought it into the tent of meeting as a memorial for the Israelites before the LORD.",
      "T": "Moses and Eleazar carried every gram of that donated gold into the tent of meeting — a memorial laid before the LORD on behalf of all Israel, testifying that the LORD had brought every man home."
    }
  },
  "32": {
    "1": {
      "L": "Now the children of Reuben and the children of Gad had a very great multitude of livestock; and when they saw the land of Jazer and the land of Gilead, behold, the place was a place for livestock.",
      "M": "The Reubenites and Gadites owned very large herds. When they saw that the lands of Jazer and Gilead were good pastureland,",
      "T": "The tribes of Reuben and Gad owned enormous herds. When they surveyed Jazer and Gilead and saw prime grazing country,"
    },
    "2": {
      "L": "The children of Gad and the children of Reuben came and spoke to Moses and to Eleazar the priest and to the leaders of the congregation, saying,",
      "M": "the Gadites and Reubenites came to Moses, Eleazar the priest, and the community leaders, saying,",
      "T": "they brought their case to Moses, Eleazar, and the tribal leadership."
    },
    "3": {
      "L": "Ataroth and Dibon and Jazer and Nimrah and Heshbon and Elealeh and Sebam and Nebo and Beon —",
      "M": "\"Ataroth, Dibon, Jazer, Nimrah, Heshbon, Elealeh, Sebam, Nebo, and Beon —\"",
      "T": "\"The country of Ataroth, Dibon, Jazer, Nimrah, Heshbon, Elealeh, Sebam, Nebo, and Beon —\""
    },
    "4": {
      "L": "the land that the LORD struck down before the congregation of Israel — it is a land for livestock, and your servants have livestock.",
      "M": "\"— the land the LORD struck down before the Israelite congregation — is livestock country, and your servants have livestock.\"",
      "T": "\"— the very territory the LORD opened before Israel — it is rich grazing land, and we have herds to fill it.\""
    },
    "5": {
      "L": "And they said, If we have found favor in your sight, let this land be given to your servants as a possession; do not bring us across the Jordan.",
      "M": "\"If we have found favor with you, please give this land to us as our possession. Do not make us cross the Jordan.\"",
      "T": "\"If we have found any favor with you, grant us this land as our holding. We ask not to be taken across the Jordan.\""
    },
    "6": {
      "L": "And Moses said to the children of Gad and to the children of Reuben, Shall your brothers go to war while you sit here?",
      "M": "Moses replied to the Gadites and Reubenites, \"Are your brothers to go off to war while you settle here?\"",
      "T": "Moses's response was sharp: \"Your brothers are going to war, and you want to stay behind?\""
    },
    "7": {
      "L": "Why will you discourage the heart of the children of Israel from going over into the land that the LORD has given them?",
      "M": "\"Why would you discourage the Israelites from crossing into the land the LORD has given them?\"",
      "T": "\"Why would you drain the courage from all Israel — the resolve it takes to enter the land the LORD has promised?\""
    },
    "8": {
      "L": "Your fathers did this when I sent them from Kadesh-barnea to survey the land.",
      "M": "\"Your ancestors did the same thing when I sent them from Kadesh-barnea to scout the land.\"",
      "T": "\"Your ancestors pulled this same move when I sent them from Kadesh-barnea to reconnoiter the land.\""
    },
    "9": {
      "L": "And when they went up to the Valley of Eshcol and surveyed the land, they discouraged the heart of the children of Israel from going into the land that the LORD had given them.",
      "M": "\"They went up to the Valley of Eshcol, surveyed the land, then turned the heart of the Israelites away from entering the land the LORD had given them.\"",
      "T": "\"They reached the Eshcol valley, took one look, and came back to drain all hope from the congregation — turned the people's heart away from the land God was giving them.\""
    },
    "10": {
      "L": "And the LORD's anger was kindled on that day, and he swore, saying,",
      "M": "\"The LORD's anger blazed that day and he swore:\"",
      "T": "\"The LORD's anger ignited. He swore an oath:\""
    },
    "11": {
      "L": "Surely none of the men who came up from Egypt from twenty years old and upward shall see the land that I swore to Abraham, to Isaac, and to Jacob — because they did not wholly follow me —",
      "M": "\"'Not one of the men who came out of Egypt, twenty years old or above, will ever see the land I swore to give Abraham, Isaac, and Jacob — because they did not follow me wholeheartedly.'\"",
      "T": "\"'Not one man who left Egypt — no one twenty or older — will lay eyes on the land I promised Abraham, Isaac, and Jacob. They refused to follow me with an undivided heart.'\""
    },
    "12": {
      "L": "except Caleb the son of Jephunneh the Kenizzite and Joshua the son of Nun, because they have wholly followed the LORD.",
      "M": "\"'Only Caleb son of Jephunneh the Kenizzite and Joshua son of Nun were exceptions — they followed the LORD completely.'\"",
      "T": "\"'The only exceptions: Caleb son of Jephunneh and Joshua son of Nun. They gave the LORD their undivided loyalty.'\""
    },
    "13": {
      "L": "And the LORD's anger was kindled against Israel, and he made them wander in the wilderness forty years until all the generation that had done evil in the sight of the LORD was consumed.",
      "M": "\"The LORD's anger burned against Israel and he made them wander in the wilderness forty years, until every person who had sinned against him was gone.\"",
      "T": "\"The LORD held Israel to that oath — forty years in the wilderness, until the entire faithless generation was spent and gone.\""
    },
    "14": {
      "L": "And behold, you have risen up in your fathers' place, a brood of sinful men, to augment still further the fierce anger of the LORD against Israel.",
      "M": "\"And here you are — sons of sinful men — risen in your fathers' footsteps, ready to stoke the LORD's burning anger against Israel still further.\"",
      "T": "\"And now here you stand: sons of the very men who failed. A second crop of faithlessness, poised to add more fuel to the LORD's righteous anger.\""
    },
    "15": {
      "L": "For if you turn away from following him, he will again leave them in the wilderness, and you will destroy all this people.",
      "M": "\"If you turn away from following him, he will again abandon them in the wilderness, and you will have destroyed all this people.\"",
      "T": "\"If you defect — if you hold back — he will abandon Israel in the wilderness again, and every last life lost will be on your hands.\""
    },
    "16": {
      "L": "And they came near to him and said, We will build sheepfolds here for our flocks and cities for our little ones,",
      "M": "They came forward and said, \"We will build sheepfolds here for our livestock and towns for our children,\"",
      "T": "The two tribes stepped up with a counter-offer: \"Let us build pens for our herds and walled towns for our families here —\""
    },
    "17": {
      "L": "and we ourselves will arm and go quickly before the children of Israel until we have brought them to their place; and our little ones shall dwell in the fortified cities because of the inhabitants of the land.",
      "M": "\"— but we ourselves will arm for battle and march ahead of the Israelites until every tribe is settled. Our children will remain in the fortified towns, safe from the local population.\"",
      "T": "\"— and we will arm ourselves and march at the front of Israel's column until every tribe is settled in its land. Our families will be secure in walled towns while we are fighting. We ask nothing for ourselves until Israel's task is complete.\""
    },
    "18": {
      "L": "We will not return to our homes until every one of the children of Israel has received his inheritance.",
      "M": "\"We will not return home until every Israelite has received his inheritance.\"",
      "T": "\"Not a single man of us comes home until every Israelite is standing on his own land.\""
    },
    "19": {
      "L": "For we will not inherit with them on the other side of the Jordan and beyond, because our inheritance has fallen to us on this side of the Jordan toward the sunrise.",
      "M": "\"We will not take any inheritance with them across the Jordan, because our inheritance has come to us here on the east side.\"",
      "T": "\"Our portion is here, east of the Jordan. We claim nothing west of the river — that belongs to the rest of Israel. We take only what is already ours.\""
    },
    "20": {
      "L": "And Moses said to them, If you will do this — if you will arm for war before the LORD,",
      "M": "Moses replied, \"If you will truly do this — if you will arm yourselves for battle before the LORD,\"",
      "T": "Moses accepted the terms: \"If you will do this — if you march armed before the LORD into the fight,\""
    },
    "21": {
      "L": "and every armed man of you will cross the Jordan before the LORD until he has driven his enemies out before him,",
      "M": "\"and all your armed men cross the Jordan before the LORD until he has expelled his enemies before him,\"",
      "T": "\"if every fighting man of yours crosses the Jordan before the LORD, pressing forward until he drives his enemies from the land —\""
    },
    "22": {
      "L": "and the land is subdued before the LORD, then afterward you shall return, and you will be free of obligation before the LORD and before Israel; and this land shall be your possession before the LORD.",
      "M": "\"— and when the land is subdued before the LORD, you may return. You will be free of obligation before the LORD and Israel, and this land will be yours.\"",
      "T": "\"— and when the land lies at rest before the LORD, then come back. You will have discharged every obligation, and this territory will be permanently yours under the LORD's authority.\""
    },
    "23": {
      "L": "But if you will not do so, behold, you have sinned against the LORD; and know that your sin will find you out.",
      "M": "\"But if you do not do this, you have sinned against the LORD, and know that your sin will find you out.\"",
      "T": "\"But if you fail — if you go back on your word — you will have sinned against the LORD. And sins of this kind do not stay hidden: they hunt you down.\""
    },
    "24": {
      "L": "Build cities for your little ones and folds for your flocks, and do what you have promised.",
      "M": "\"Go ahead — build towns for your children and pens for your flocks, and carry out what you have promised.\"",
      "T": "\"Go build your towns and your sheep pens. But hold to every word you have spoken.\""
    },
    "25": {
      "L": "And the children of Gad and the children of Reuben said to Moses, Your servants will do as my lord commands.",
      "M": "The Gadites and Reubenites said to Moses, \"Your servants will do as my lord commands.\"",
      "T": "The Gadites and Reubenites answered: \"We will do exactly what you have commanded.\""
    },
    "26": {
      "L": "Our little ones, our wives, our flocks, and all our livestock shall remain there in the cities of Gilead;",
      "M": "\"Our children, wives, flocks, and all our livestock will remain in the cities of Gilead;\"",
      "T": "\"Our families — children, wives, herds, and flocks — will stay in the Gilead towns.\""
    },
    "27": {
      "L": "but your servants will cross over, every man armed for war before the LORD to battle, as my lord says.",
      "M": "\"but we your servants will cross over, every one of us armed for war, before the LORD to battle, as my lord says.\"",
      "T": "\"Every fighting man among us will cross over, fully armed, marching before the LORD — exactly as you have said.\""
    },
    "28": {
      "L": "So Moses gave command concerning them to Eleazar the priest and to Joshua the son of Nun and to the heads of the fathers' houses of the tribes of the children of Israel.",
      "M": "Moses then gave instructions about them to Eleazar the priest, Joshua son of Nun, and the tribal leaders of the Israelites.",
      "T": "Moses formalized the agreement, laying out its terms before Eleazar, Joshua, and the tribal chieftains of Israel."
    },
    "29": {
      "L": "And Moses said to them, If the children of Gad and the children of Reuben cross the Jordan with you, every man armed for war before the LORD, and the land is subdued before you, then you shall give them the land of Gilead as a possession;",
      "M": "Moses said: \"If the Gadites and Reubenites cross the Jordan armed before the LORD and the land is subdued, give them Gilead as their possession.\"",
      "T": "\"Should the Gadites and Reubenites cross fully armed and fight alongside you until the land is subdued — award them Gilead as their permanent holding.\""
    },
    "30": {
      "L": "but if they will not cross with you armed, they shall have possessions among you in the land of Canaan.",
      "M": "\"But if they do not cross over armed, they will receive their share in Canaan like everyone else.\"",
      "T": "\"But if they renege — if they will not cross armed — they forfeit their separate claim and receive their portion in Canaan alongside the rest of Israel.\""
    },
    "31": {
      "L": "And the children of Gad and the children of Reuben answered, saying, What the LORD has spoken to your servants, so will we do.",
      "M": "The Gadites and Reubenites replied, \"What the LORD has said, we will do.\"",
      "T": "Gad and Reuben replied without hesitation: \"Whatever the LORD has spoken — we will carry it out.\""
    },
    "32": {
      "L": "We will cross armed before the LORD into the land of Canaan, and the possession of our inheritance shall remain with us on this side of the Jordan.",
      "M": "\"We will cross over armed before the LORD into Canaan, and our inherited possession will remain here on the east side of the Jordan.\"",
      "T": "\"We will march armed before the LORD into Canaan. Our inheritance, however, stays here east of the river — that is settled.\""
    },
    "33": {
      "L": "And Moses gave to them — to the children of Gad and to the children of Reuben and to the half-tribe of Manasseh the son of Joseph — the kingdom of Sihon king of the Amorites and the kingdom of Og king of Bashan, the land with its cities and their territories, the cities of the surrounding land.",
      "M": "Moses assigned to the Gadites, the Reubenites, and the half-tribe of Manasseh son of Joseph the kingdom of Sihon king of the Amorites and the kingdom of Og king of Bashan — the land with its cities and surrounding territories.",
      "T": "Moses awarded Gad, Reuben, and the half-tribe of Manasseh all the territory once held by Sihon king of the Amorites and Og king of Bashan — every city and its surrounding countryside."
    },
    "34": {
      "L": "And the children of Gad built Dibon and Ataroth and Aroer,",
      "M": "The Gadites rebuilt Dibon, Ataroth, and Aroer,",
      "T": "The tribe of Gad set to work: they rebuilt Dibon, Ataroth, Aroer,"
    },
    "35": {
      "L": "and Atroth-shophan and Jazer and Jogbehah,",
      "M": "Atroth-shophan, Jazer, and Jogbehah,",
      "T": "Atroth-shophan, Jazer, Jogbehah,"
    },
    "36": {
      "L": "and Beth-nimrah and Beth-haran — fortified cities — and sheepfolds.",
      "M": "Beth-nimrah and Beth-haran — all fortified cities — along with sheepfolds.",
      "T": "Beth-nimrah and Beth-haran — all walled and fortified, with pens for their herds."
    },
    "37": {
      "L": "And the children of Reuben built Heshbon and Elealeh and Kiriathaim,",
      "M": "The Reubenites rebuilt Heshbon, Elealeh, and Kiriathaim,",
      "T": "Reuben rebuilt Heshbon, Elealeh, Kiriathaim,"
    },
    "38": {
      "L": "and Nebo and Baal-meon — their names being changed — and Sibmah; and they gave other names to the cities they built.",
      "M": "Nebo and Baal-meon — renaming them — and Sibmah; they gave the rebuilt cities new names.",
      "T": "Nebo, Baal-meon — renamed — and Sibmah; the rebuilt cities received new identities."
    },
    "39": {
      "L": "And the sons of Machir the son of Manasseh went to Gilead and captured it, and dispossessed the Amorites who were there.",
      "M": "The sons of Machir son of Manasseh went to Gilead, captured it, and drove out the Amorites who lived there.",
      "T": "The clan of Machir son of Manasseh struck out toward Gilead, seized it, and expelled the Amorites who had held it."
    },
    "40": {
      "L": "And Moses gave Gilead to Machir the son of Manasseh, and he settled in it.",
      "M": "Moses assigned Gilead to Machir son of Manasseh, and he settled there.",
      "T": "Moses formalized the grant: Gilead to Machir — and Machir made it home."
    },
    "41": {
      "L": "And Jair the son of Manasseh went and captured their villages and called them Havvoth-jair.",
      "M": "Jair son of Manasseh went and took the surrounding villages, which he named Havvoth-jair.",
      "T": "Jair son of Manasseh swept through the surrounding settlements, took them all, and renamed the whole district Havvoth-jair — the Villages of Jair."
    },
    "42": {
      "L": "And Nobah went and captured Kenath and its villages and called it Nobah after his own name.",
      "M": "Nobah went and captured Kenath and its surrounding villages, naming the place Nobah after himself.",
      "T": "Nobah seized Kenath and its satellite towns, stamping his own name on the captured city."
    }
  },
  "33": {
    "1": {
      "L": "These are the stages of the children of Israel when they went out of the land of Egypt by their armies, under the hand of Moses and Aaron.",
      "M": "These are the stages of the Israelites' journey out of Egypt, organized under the command of Moses and Aaron.",
      "T": "Here is the full record of Israel's journey out of Egypt — every camp, every march, every station the LORD's people passed through under Moses and Aaron."
    },
    "2": {
      "L": "And Moses wrote down their starting points stage by stage, by the commandment of the LORD; and these are their stages according to their starting points:",
      "M": "By the LORD's command, Moses recorded their departures stage by stage. These are the stages listed by their starting points:",
      "T": "At the LORD's direction Moses wrote it all down — a record of every departure, every leg of the journey, preserved in order."
    },
    "3": {
      "L": "They departed from Rameses in the first month, on the fifteenth day of the first month; on the day after the Passover the children of Israel went out boldly in the sight of all the Egyptians,",
      "M": "They set out from Rameses in the first month, on the fifteenth day — the day after the Passover — in full sight of all the Egyptians, going out boldly.",
      "T": "They marched out of Rameses on the fifteenth of the first month — the morning after the Passover — in full view of Egypt, openly, under no concealment."
    },
    "4": {
      "L": "while the Egyptians were burying all their firstborn, whom the LORD had struck down among them; on their gods also the LORD executed judgments.",
      "M": "while the Egyptians were burying their firstborn, whom the LORD had struck down; the LORD had also executed judgment on their gods.",
      "T": "Behind them, Egypt was burying its dead — every firstborn the LORD had struck. Not a single Egyptian god had been able to protect its people."
    },
    "5": {
      "L": "And the children of Israel set out from Rameses and camped at Succoth.",
      "M": "The Israelites moved from Rameses and camped at Succoth.",
      "T": "First stage: Rameses to Succoth."
    },
    "6": {
      "L": "And they set out from Succoth and camped at Etham, which is on the edge of the wilderness.",
      "M": "From Succoth they moved to Etham, at the edge of the wilderness.",
      "T": "Succoth to Etham, where the desert begins."
    },
    "7": {
      "L": "And they set out from Etham and turned back to Pi-hahiroth, which is east of Baal-zephon; and they camped before Migdol.",
      "M": "From Etham they turned back toward Pi-hahiroth, opposite Baal-zephon, and camped before Migdol.",
      "T": "Etham to Pi-hahiroth — a seeming retreat, camping in front of Migdol with the sea before them."
    },
    "8": {
      "L": "And they set out from before Hahiroth and passed through the midst of the sea into the wilderness; they went a three days' journey in the wilderness of Etham and camped at Marah.",
      "M": "From Hahiroth they passed through the middle of the sea into the wilderness, traveled three days through the wilderness of Etham, and camped at Marah.",
      "T": "From Hahiroth they walked into the sea and out the other side — then three days into the Etham wilderness to Marah, where the water was bitter."
    },
    "9": {
      "L": "And they set out from Marah and came to Elim; at Elim there were twelve springs of water and seventy palm trees, and they camped there.",
      "M": "From Marah they came to Elim, where there were twelve springs and seventy palms, and they camped there.",
      "T": "Marah to Elim — twelve springs and seventy palms, a welcome rest after the bitter water."
    },
    "10": {
      "L": "And they set out from Elim and camped by the Red Sea.",
      "M": "From Elim they camped by the Red Sea.",
      "T": "Elim to the shore of the Red Sea."
    },
    "11": {
      "L": "And they set out from the Red Sea and camped in the wilderness of Sin.",
      "M": "From the Red Sea they moved to the wilderness of Sin.",
      "T": "The Red Sea to the wilderness of Sin."
    },
    "12": {
      "L": "And they set out from the wilderness of Sin and camped at Dophkah.",
      "M": "From the wilderness of Sin they camped at Dophkah.",
      "T": "Wilderness of Sin to Dophkah."
    },
    "13": {
      "L": "And they set out from Dophkah and camped at Alush.",
      "M": "From Dophkah they camped at Alush.",
      "T": "Dophkah to Alush."
    },
    "14": {
      "L": "And they set out from Alush and camped at Rephidim, where there was no water for the people to drink.",
      "M": "From Alush they camped at Rephidim — and there was no water for the people to drink.",
      "T": "Alush to Rephidim, where there was no water — where Moses struck the rock and water came."
    },
    "15": {
      "L": "And they set out from Rephidim and camped in the wilderness of Sinai.",
      "M": "From Rephidim they camped in the wilderness of Sinai.",
      "T": "Rephidim to Sinai — the mountain where the covenant was sealed."
    },
    "16": {
      "L": "And they set out from the wilderness of Sinai and camped at Kibroth-hattaavah.",
      "M": "From the wilderness of Sinai they camped at Kibroth-hattaavah.",
      "T": "Sinai to Kibroth-hattaavah — the Graves of Craving, named for those who died demanding meat."
    },
    "17": {
      "L": "And they set out from Kibroth-hattaavah and camped at Hazeroth.",
      "M": "From Kibroth-hattaavah they camped at Hazeroth.",
      "T": "Kibroth-hattaavah to Hazeroth — where Miriam's skin turned white as snow."
    },
    "18": {
      "L": "And they set out from Hazeroth and camped at Rithmah.",
      "M": "From Hazeroth they camped at Rithmah.",
      "T": "Hazeroth to Rithmah."
    },
    "19": {
      "L": "And they set out from Rithmah and camped at Rimmon-perez.",
      "M": "From Rithmah they camped at Rimmon-perez.",
      "T": "Rithmah to Rimmon-perez."
    },
    "20": {
      "L": "And they set out from Rimmon-perez and camped at Libnah.",
      "M": "From Rimmon-perez they camped at Libnah.",
      "T": "Rimmon-perez to Libnah."
    },
    "21": {
      "L": "And they set out from Libnah and camped at Rissah.",
      "M": "From Libnah they camped at Rissah.",
      "T": "Libnah to Rissah."
    },
    "22": {
      "L": "And they set out from Rissah and camped at Kehelathah.",
      "M": "From Rissah they camped at Kehelathah.",
      "T": "Rissah to Kehelathah."
    },
    "23": {
      "L": "And they set out from Kehelathah and camped at Mount Shepher.",
      "M": "From Kehelathah they camped at Mount Shepher.",
      "T": "Kehelathah to Mount Shepher."
    },
    "24": {
      "L": "And they set out from Mount Shepher and camped at Haradah.",
      "M": "From Mount Shepher they camped at Haradah.",
      "T": "Mount Shepher to Haradah."
    },
    "25": {
      "L": "And they set out from Haradah and camped at Makheloth.",
      "M": "From Haradah they camped at Makheloth.",
      "T": "Haradah to Makheloth."
    },
    "26": {
      "L": "And they set out from Makheloth and camped at Tahath.",
      "M": "From Makheloth they camped at Tahath.",
      "T": "Makheloth to Tahath."
    },
    "27": {
      "L": "And they set out from Tahath and camped at Terah.",
      "M": "From Tahath they camped at Terah.",
      "T": "Tahath to Terah."
    },
    "28": {
      "L": "And they set out from Terah and camped at Mithkah.",
      "M": "From Terah they camped at Mithkah.",
      "T": "Terah to Mithkah."
    },
    "29": {
      "L": "And they set out from Mithkah and camped at Hashmonah.",
      "M": "From Mithkah they camped at Hashmonah.",
      "T": "Mithkah to Hashmonah."
    },
    "30": {
      "L": "And they set out from Hashmonah and camped at Moseroth.",
      "M": "From Hashmonah they camped at Moseroth.",
      "T": "Hashmonah to Moseroth."
    },
    "31": {
      "L": "And they set out from Moseroth and camped at Bene-jaakan.",
      "M": "From Moseroth they camped at Bene-jaakan.",
      "T": "Moseroth to Bene-jaakan."
    },
    "32": {
      "L": "And they set out from Bene-jaakan and camped at Hor-haggidgad.",
      "M": "From Bene-jaakan they camped at Hor-haggidgad.",
      "T": "Bene-jaakan to Hor-haggidgad."
    },
    "33": {
      "L": "And they set out from Hor-haggidgad and camped at Jotbathah.",
      "M": "From Hor-haggidgad they camped at Jotbathah.",
      "T": "Hor-haggidgad to Jotbathah."
    },
    "34": {
      "L": "And they set out from Jotbathah and camped at Abronah.",
      "M": "From Jotbathah they camped at Abronah.",
      "T": "Jotbathah to Abronah."
    },
    "35": {
      "L": "And they set out from Abronah and camped at Ezion-geber.",
      "M": "From Abronah they camped at Ezion-geber.",
      "T": "Abronah to Ezion-geber."
    },
    "36": {
      "L": "And they set out from Ezion-geber and camped in the wilderness of Zin — that is, Kadesh.",
      "M": "From Ezion-geber they camped in the wilderness of Zin — that is, Kadesh.",
      "T": "Ezion-geber to the wilderness of Zin — Kadesh, where the scouts' verdict condemned a generation."
    },
    "37": {
      "L": "And they set out from Kadesh and camped at Mount Hor, at the edge of the land of Edom.",
      "M": "From Kadesh they camped at Mount Hor, on the border of Edom.",
      "T": "Kadesh to Mount Hor, at Edom's boundary — where the high priesthood changed hands."
    },
    "38": {
      "L": "And Aaron the priest went up Mount Hor at the commandment of the LORD and died there, in the fortieth year after the children of Israel came out of the land of Egypt, on the first day of the fifth month.",
      "M": "Aaron the priest went up Mount Hor at the LORD's command and died there in the fortieth year after the Israelites left Egypt, on the first day of the fifth month.",
      "T": "At the LORD's direct command, in the fortieth year — the first of the fifth month — Aaron the priest climbed Mount Hor and did not come down."
    },
    "39": {
      "L": "And Aaron was a hundred and twenty-three years old when he died at Mount Hor.",
      "M": "Aaron was one hundred twenty-three years old when he died at Mount Hor.",
      "T": "Aaron was a hundred and twenty-three years old. He died on the mountain."
    },
    "40": {
      "L": "And the Canaanite, the king of Arad, who lived in the Negeb in the land of Canaan, heard of the coming of the children of Israel.",
      "M": "The Canaanite king of Arad, who lived in the Negeb in Canaan, heard that the Israelites were approaching.",
      "T": "Word reached the Canaanite king of Arad, ruling the Negeb, that Israel was on the move."
    },
    "41": {
      "L": "And they set out from Mount Hor and camped at Zalmonah.",
      "M": "From Mount Hor they camped at Zalmonah.",
      "T": "Mount Hor to Zalmonah."
    },
    "42": {
      "L": "And they set out from Zalmonah and camped at Punon.",
      "M": "From Zalmonah they camped at Punon.",
      "T": "Zalmonah to Punon."
    },
    "43": {
      "L": "And they set out from Punon and camped at Oboth.",
      "M": "From Punon they camped at Oboth.",
      "T": "Punon to Oboth."
    },
    "44": {
      "L": "And they set out from Oboth and camped at Iye-abarim, on the border of Moab.",
      "M": "From Oboth they camped at Iye-abarim, on Moab's border.",
      "T": "Oboth to Iye-abarim — the edge of Moab."
    },
    "45": {
      "L": "And they set out from Iyim and camped at Dibon-gad.",
      "M": "From Iyim they camped at Dibon-gad.",
      "T": "Iyim to Dibon-gad."
    },
    "46": {
      "L": "And they set out from Dibon-gad and camped at Almon-diblathaim.",
      "M": "From Dibon-gad they camped at Almon-diblathaim.",
      "T": "Dibon-gad to Almon-diblathaim."
    },
    "47": {
      "L": "And they set out from Almon-diblathaim and camped in the mountains of Abarim, before Nebo.",
      "M": "From Almon-diblathaim they camped in the Abarim mountains, before Nebo.",
      "T": "Almon-diblathaim to the Abarim heights — Nebo in view, the mountain Moses would climb at the end."
    },
    "48": {
      "L": "And they set out from the mountains of Abarim and camped in the plains of Moab by the Jordan near Jericho.",
      "M": "From the Abarim mountains they camped in the plains of Moab by the Jordan at Jericho.",
      "T": "The Abarim mountains to the plains of Moab by the Jordan — and there the journey ended."
    },
    "49": {
      "L": "They camped by the Jordan from Beth-jeshimoth as far as Abel-shittim in the plains of Moab.",
      "M": "Their camp stretched along the Jordan from Beth-jeshimoth to Abel-shittim in the plains of Moab.",
      "T": "The camp spread from Beth-jeshimoth to Abel-shittim — the final staging ground, Canaan visible across the river."
    },
    "50": {
      "L": "And the LORD spoke to Moses in the plains of Moab by the Jordan near Jericho, saying,",
      "M": "The LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying,",
      "T": "There on the Moabite plains, with Canaan across the river, the LORD addressed Moses:"
    },
    "51": {
      "L": "Speak to the children of Israel and say to them, When you cross the Jordan into the land of Canaan,",
      "M": "\"Tell the Israelites: When you cross the Jordan into Canaan,\"",
      "T": "\"Tell the people: The moment you cross the Jordan into Canaan,\""
    },
    "52": {
      "L": "you shall drive out all the inhabitants of the land from before you and destroy all their figured stones and destroy all their molten images and demolish all their high places;",
      "M": "\"drive out all the land's inhabitants, smash all their carved stones, destroy all their cast metal images, and tear down all their high places.\"",
      "T": "\"drive out every inhabitant. Shatter every carved idol, melt every cast image, level every high place. Leave nothing standing that could become a snare.\""
    },
    "53": {
      "L": "and you shall take possession of the land and live in it, for I have given the land to you to possess it.",
      "M": "\"Take possession of the land and live in it, for I have given it to you.\"",
      "T": "\"Occupy the land and make it your home — it is a gift from me, formally given, and it is yours.\""
    },
    "54": {
      "L": "And you shall divide the land by lot for an inheritance according to your clans. To a large group you shall give a large inheritance, and to a small group you shall give a small inheritance; wherever the lot falls for anyone, that shall be his. You shall inherit according to the tribes of your fathers.",
      "M": "\"Distribute the land by lot among your clans — larger groups receive larger allotments, smaller groups smaller ones. The lot decides each person's place; inherit according to your ancestral tribes.\"",
      "T": "\"The land is apportioned by lot according to tribal size — proportionate, fair, decided by the LORD's own hand in the casting. Each tribe holds what the lot assigns. No tribe is favored; the LORD oversees the distribution.\""
    },
    "55": {
      "L": "But if you do not drive out the inhabitants of the land from before you, then those of them that you let remain will be as pricks in your eyes and thorns in your sides, and they will trouble you in the land where you dwell.",
      "M": "\"But if you do not drive out the land's inhabitants, those you leave will be thorns in your eyes and splinters in your sides — they will harass you in the land where you live.\"",
      "T": "\"But leave the population intact, and they will be gravel in your eyes and splinters in your flesh — gnawing at you generation after generation in the very land I am giving you.\""
    },
    "56": {
      "L": "And it will be that as I planned to do to them, I will do to you.",
      "M": "\"And what I had planned to do to them, I will do to you.\"",
      "T": "\"Fail at this, and the judgment I reserved for them I will turn on you instead.\""
    }
  },
  "34": {
    "1": {
      "L": "And the LORD spoke to Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Command the children of Israel and say to them, When you come into the land of Canaan — this is the land that shall fall to you as an inheritance, the land of Canaan with its boundaries —",
      "M": "\"Command the Israelites: When you enter the land of Canaan, this is the land allotted to you as your inheritance — the land of Canaan within these boundaries:\"",
      "T": "\"Tell Israel: When you enter Canaan, the land I am assigning you as your permanent inheritance has these boundaries:\""
    },
    "3": {
      "L": "your southern side shall be from the wilderness of Zin along the edge of Edom, and your southern border shall run from the end of the Salt Sea on the east;",
      "M": "\"Your southern boundary runs from the wilderness of Zin along Edom's flank; the southeastern corner begins at the far end of the Dead Sea.\"",
      "T": "\"The southern boundary: from the wilderness of Zin, hugging Edom, east to the tip of the Salt Sea.\""
    },
    "4": {
      "L": "and your border shall turn from the south to the Ascent of Akrabbim and cross to Zin, and its limit shall be south of Kadesh-barnea; then it shall go on to Hazar-addar and cross to Azmon;",
      "M": "\"From the eastern corner it curves up the Scorpion Ascent, crosses to Zin, runs south of Kadesh-barnea, then continues to Hazar-addar and on to Azmon.\"",
      "T": "\"Trace it: up the Scorpion Pass, across to Zin, south of Kadesh-barnea, on to Hazar-addar, then Azmon.\""
    },
    "5": {
      "L": "and the border shall turn from Azmon to the Brook of Egypt, and its termination shall be at the sea.",
      "M": "\"From Azmon the border turns to the Wadi of Egypt and ends at the Mediterranean Sea.\"",
      "T": "\"From Azmon west to the Wadi of Egypt — and there the southern border meets the sea.\""
    },
    "6": {
      "L": "And as for the western border, you shall have the Great Sea; this shall be your western border.",
      "M": "\"Your western border is the Mediterranean — the Great Sea itself.\"",
      "T": "\"The western boundary is the Great Sea. No drawn line needed — just coastline.\""
    },
    "7": {
      "L": "This shall be your northern border: from the Great Sea you shall draw a line to Mount Hor;",
      "M": "\"Your northern border: from the Great Sea, draw it to Mount Hor;\"",
      "T": "\"Northern boundary: from the Great Sea to Mount Hor;\""
    },
    "8": {
      "L": "from Mount Hor you shall draw a line to Lebo-hamath, and the termination of the border shall be at Zedad;",
      "M": "\"from Mount Hor extend it to the entrance of Hamath; the border ends at Zedad;\"",
      "T": "\"Mount Hor to the pass of Hamath, ending at Zedad;\""
    },
    "9": {
      "L": "and the border shall extend to Ziphron, and its end shall be at Hazar-enan; this shall be your northern border.",
      "M": "\"from there it continues to Ziphron and ends at Hazar-enan. That is the northern border.\"",
      "T": "\"on to Ziphron, then Hazar-enan — that is where the north ends.\""
    },
    "10": {
      "L": "And you shall mark out your eastern border from Hazar-enan to Shepham;",
      "M": "\"For the eastern border, mark it from Hazar-enan to Shepham;\"",
      "T": "\"Eastern boundary: from Hazar-enan to Shepham;\""
    },
    "11": {
      "L": "and the border shall descend from Shepham to Riblah on the east side of Ain; and the border shall descend and reach to the eastern shoulder of the Sea of Kinnereth;",
      "M": "\"the border descends from Shepham to Riblah, east of Ain, continues down to the eastern slope of the Sea of Kinnereth;\"",
      "T": "\"down from Shepham to Riblah on the east side of Ain, then south to the eastern shore of the Sea of Kinnereth;\""
    },
    "12": {
      "L": "and the border shall go down along the Jordan, and its end shall be at the Salt Sea. This shall be your land according to its borders all around.",
      "M": "\"then it follows the Jordan down to the Dead Sea. That is your land, bounded on all sides.\"",
      "T": "\"then south along the Jordan to the Dead Sea. Within these lines — sea to salt sea, mountain to river — lies the land that is yours.\""
    },
    "13": {
      "L": "And Moses commanded the children of Israel, saying, This is the land that you shall inherit by lot, which the LORD has commanded to give to the nine and a half tribes;",
      "M": "Moses told the Israelites: \"This is the land you will receive by lot — what the LORD has commanded to give to the nine and a half tribes.\"",
      "T": "Moses addressed the assembly: \"The entire territory just described is what the LORD has ordered apportioned among nine and a half tribes by lot.\""
    },
    "14": {
      "L": "for the tribe of the children of Reuben by their fathers' houses and the tribe of the children of Gad by their fathers' houses have received their inheritance; and the half-tribe of Manasseh has received its inheritance;",
      "M": "\"The tribe of Reuben, the tribe of Gad, and the half-tribe of Manasseh have already received their inheritance.\"",
      "T": "\"Reuben, Gad, and half of Manasseh are already settled east of the Jordan — they receive nothing west of the river.\""
    },
    "15": {
      "L": "the two tribes and the half-tribe have received their inheritance beyond the Jordan at Jericho, eastward toward the sunrise.",
      "M": "\"Those two and a half tribes have received their portions on the east side of the Jordan, at Jericho, facing the sunrise.\"",
      "T": "\"Those two and a half tribes are planted east of the river, the Jordan at their backs, facing the rising sun.\""
    },
    "16": {
      "L": "And the LORD spoke to Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD continued:"
    },
    "17": {
      "L": "These are the names of the men who shall divide the land for you as an inheritance: Eleazar the priest and Joshua the son of Nun.",
      "M": "\"These are the men who will divide the land as your inheritance: Eleazar the priest and Joshua son of Nun.\"",
      "T": "\"Eleazar the priest and Joshua son of Nun will oversee the allotment.\""
    },
    "18": {
      "L": "And you shall appoint one leader from each tribe to divide the land for inheritance.",
      "M": "\"Appoint one leader from each tribe to assist in dividing the land.\"",
      "T": "\"Each tribe will also designate one leader to serve on the allocation commission.\""
    },
    "19": {
      "L": "And these are the names of the men: from the tribe of Judah, Caleb the son of Jephunneh;",
      "M": "\"The names are: for Judah — Caleb son of Jephunneh;\"",
      "T": "\"The commissioners: Judah sends Caleb son of Jephunneh;\""
    },
    "20": {
      "L": "and from the tribe of the children of Simeon, Shemuel the son of Ammihud;",
      "M": "\"for Simeon — Shemuel son of Ammihud;\"",
      "T": "\"Simeon sends Shemuel son of Ammihud;\""
    },
    "21": {
      "L": "from the tribe of Benjamin, Elidad the son of Chislon;",
      "M": "\"for Benjamin — Elidad son of Chislon;\"",
      "T": "\"Benjamin sends Elidad son of Chislon;\""
    },
    "22": {
      "L": "and from the tribe of the children of Dan a leader, Bukki the son of Jogli;",
      "M": "\"for Dan — Bukki son of Jogli;\"",
      "T": "\"Dan sends Bukki son of Jogli;\""
    },
    "23": {
      "L": "from the children of Joseph: from the tribe of the children of Manasseh a leader, Hanniel the son of Ephod;",
      "M": "\"for Manasseh — Hanniel son of Ephod;\"",
      "T": "\"Manasseh sends Hanniel son of Ephod;\""
    },
    "24": {
      "L": "and from the tribe of the children of Ephraim a leader, Kemuel the son of Shiphtan;",
      "M": "\"for Ephraim — Kemuel son of Shiphtan;\"",
      "T": "\"Ephraim sends Kemuel son of Shiphtan;\""
    },
    "25": {
      "L": "and from the tribe of the children of Zebulun a leader, Elizaphan the son of Parnach;",
      "M": "\"for Zebulun — Elizaphan son of Parnach;\"",
      "T": "\"Zebulun sends Elizaphan son of Parnach;\""
    },
    "26": {
      "L": "and from the tribe of the children of Issachar a leader, Paltiel the son of Azzan;",
      "M": "\"for Issachar — Paltiel son of Azzan;\"",
      "T": "\"Issachar sends Paltiel son of Azzan;\""
    },
    "27": {
      "L": "and from the tribe of the children of Asher a leader, Ahihud the son of Shelomi;",
      "M": "\"for Asher — Ahihud son of Shelomi;\"",
      "T": "\"Asher sends Ahihud son of Shelomi;\""
    },
    "28": {
      "L": "and from the tribe of the children of Naphtali a leader, Pedahel the son of Ammihud.",
      "M": "\"and for Naphtali — Pedahel son of Ammihud.\"",
      "T": "\"and Naphtali sends Pedahel son of Ammihud.\""
    },
    "29": {
      "L": "These are those whom the LORD commanded to divide the inheritance for the children of Israel in the land of Canaan.",
      "M": "These are the men the LORD commissioned to divide the inheritance among the Israelites in Canaan.",
      "T": "These twelve, under Eleazar and Joshua, are the LORD's appointed commissioners for dividing the promised land among his people."
    }
  },
  "35": {
    "1": {
      "L": "And the LORD spoke to Moses in the plains of Moab by the Jordan near Jericho, saying,",
      "M": "The LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying,",
      "T": "The LORD spoke to Moses on the Moabite plains by the Jordan:"
    },
    "2": {
      "L": "Command the children of Israel to give to the Levites, from the inheritance of their possession, cities to dwell in; and you shall also give to the Levites pastureland around the cities.",
      "M": "\"Command the Israelites to give the Levites, from their inherited land, towns to live in along with surrounding pasturelands.\"",
      "T": "\"When Israel takes possession of the land, each tribe must carve out towns from its inheritance and give them to the Levites to live in — with open pastureland surrounding each town.\""
    },
    "3": {
      "L": "The cities shall be theirs to dwell in, and their pasturelands shall be for their cattle and for their livestock and for all their animals.",
      "M": "\"The towns will be for the Levites to live in; the surrounding pasturelands will be for their livestock and animals.\"",
      "T": "\"The towns are for the Levites' households; the pasturelands are for their herds. They receive no farmland, but they must have somewhere to live.\""
    },
    "4": {
      "L": "And the pasturelands of the cities that you give to the Levites shall extend from the wall of the city outward a thousand cubits all around.",
      "M": "\"The pasturelands given to the Levitical towns must extend a thousand cubits from the town wall outward in every direction.\"",
      "T": "\"Each town's pasture extends a thousand cubits out from the wall — a protective ring of open ground on all sides.\""
    },
    "5": {
      "L": "And you shall measure outside the city on the east side two thousand cubits, and on the south side two thousand cubits, and on the west side two thousand cubits, and on the north side two thousand cubits — the city being in the center; this shall be the pastureland of the cities for them.",
      "M": "\"Measure two thousand cubits on each side — east, south, west, and north — with the town at the center. That defines the pastureland for the Levitical towns.\"",
      "T": "\"Two thousand cubits on each of the four sides, the town at the center of that square — that is the pasture boundary.\""
    },
    "6": {
      "L": "And among the cities that you give to the Levites you shall include six cities of refuge, which you shall provide for the manslayer to flee to; and in addition to them you shall give forty-two cities.",
      "M": "\"Among the towns you give the Levites, include six cities of refuge where a person who kills accidentally may flee. Add forty-two other towns to these.\"",
      "T": "\"Six of the Levitical towns must be designated as cities of refuge — a protected destination for anyone who kills unintentionally. The remaining forty-two towns complete the Levites' allotment.\""
    },
    "7": {
      "L": "All the cities that you give to the Levites shall be forty-eight cities with their pasturelands.",
      "M": "\"The Levites' total is forty-eight towns with their surrounding pasturelands.\"",
      "T": "\"Forty-eight towns in all, each with its pasture, drawn proportionally from every tribe — that is the Levites' civic inheritance in a land they will never personally farm.\""
    },
    "8": {
      "L": "And as for the cities that you shall give from the possession of the children of Israel, from those with many you shall take many, and from those with few you shall take few; each shall give some of his cities to the Levites in proportion to the inheritance that he inherits.",
      "M": "\"When taking towns from Israel's holdings, take more from larger tribes and fewer from smaller ones — each tribe gives in proportion to its inherited land.\"",
      "T": "\"Proportion matters: the tribe that inherits the most gives the most towns; the smallest tribe gives fewer. The Levites draw from every tribe without overburdening any one of them.\""
    },
    "9": {
      "L": "And the LORD spoke to Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD continued:"
    },
    "10": {
      "L": "Speak to the children of Israel and say to them, When you cross the Jordan into the land of Canaan,",
      "M": "\"Tell the Israelites: When you cross the Jordan into Canaan,\"",
      "T": "\"Tell Israel: Once you are across the Jordan,\""
    },
    "11": {
      "L": "you shall select cities to be cities of refuge for you, so that the manslayer who kills any person unintentionally may flee there.",
      "M": "\"designate cities of refuge where a person who kills someone accidentally may escape.\"",
      "T": "\"establish cities of refuge — places a person can run to after killing someone without malice or premeditation.\""
    },
    "12": {
      "L": "And the cities shall be for you a refuge from the avenger, so that the manslayer may not die before standing trial before the congregation.",
      "M": "\"These cities will protect the manslayer from the blood avenger until the case is judged by the community.\"",
      "T": "\"They exist to protect an accidental killer from the blood-avenger — to guarantee that no one is executed before the community has heard the full case.\""
    },
    "13": {
      "L": "And of the cities that you give, there shall be six cities of refuge for you.",
      "M": "\"You shall designate six cities of refuge.\"",
      "T": "\"Six cities — that is the refuge network Israel is to maintain.\""
    },
    "14": {
      "L": "Three cities you shall give beyond the Jordan, and three cities you shall give in the land of Canaan; they shall be cities of refuge.",
      "M": "\"Place three on the east side of the Jordan and three in Canaan proper.\"",
      "T": "\"Three east of the Jordan, three west — covering the whole extent of the land.\""
    },
    "15": {
      "L": "These six cities shall be a refuge for the children of Israel and for the resident alien and for the sojourner among them, so that anyone who kills any person unintentionally may flee there.",
      "M": "\"These six cities of refuge are open to Israelites, resident aliens, and foreigners among you — for anyone who kills unintentionally.\"",
      "T": "\"The refuge is not for Israelites alone. The alien living in your midst, the passing stranger — anyone who kills without intent has the same right to flee, the same claim on the city's protection.\""
    },
    "16": {
      "L": "But if he struck him with an iron object so that he died, he is a murderer; the murderer shall certainly be put to death.",
      "M": "\"If someone strikes another with an iron implement and causes death, that person is a murderer who must be executed.\"",
      "T": "\"Iron weapon, death — murder. There is no ambiguity, no refuge available. The killer must die.\""
    },
    "17": {
      "L": "And if he struck him with a stone in his hand by which a man may die, and he died, he is a murderer; the murderer shall certainly be put to death.",
      "M": "\"If someone strikes another with a stone large enough to kill and the person dies, that is murder — the murderer must be executed.\"",
      "T": "\"Stone large enough to kill, and the person dies — murder. The murderer must be executed.\""
    },
    "18": {
      "L": "Or if he struck him with a wooden hand weapon by which a man may die, and he died, he is a murderer; the murderer shall certainly be put to death.",
      "M": "\"If someone strikes another with a wooden weapon capable of causing death and the person dies, that is murder — the murderer must be executed.\"",
      "T": "\"Wooden weapon, death — same verdict. The weapon's material is irrelevant; what matters is capacity to kill and the act of using it.\""
    },
    "19": {
      "L": "The blood avenger shall himself put the murderer to death; when he meets him, he shall put him to death.",
      "M": "\"The blood avenger shall execute the murderer — when he encounters him, he shall put him to death.\"",
      "T": "\"The right to execute belongs to the blood-avenger — the nearest male kin of the victim. When he finds the killer outside any city of refuge, he may act.\""
    },
    "20": {
      "L": "And if he pushed him out of hatred, or hurled something at him while lying in wait so that he died,",
      "M": "\"But if someone pushed another out of hatred, or hurled something at them while lying in ambush, and the person died,\"",
      "T": "\"If the killing was driven by hatred — a shove from behind, a thrown weapon from hiding —\""
    },
    "21": {
      "L": "or if in enmity he struck him with his hand so that he died, the one who struck him shall certainly be put to death; he is a murderer. The blood avenger shall put the murderer to death when he meets him.",
      "M": "\"or struck them with the fist out of enmity and caused death — that person is a murderer who must be executed. The blood avenger shall kill the murderer when they meet.\"",
      "T": "\"or struck down with bare hands in an act of hatred — that is murder. No refuge. The blood-avenger has the right to act on sight.\""
    },
    "22": {
      "L": "But if he pushed him suddenly without enmity, or hurled something at him without lying in wait,",
      "M": "\"But if someone shoved another suddenly, without hostility, or accidentally threw something at them without lying in ambush,\"",
      "T": "\"Suppose the push was sudden, no hatred involved — a collision, an accident — or something thrown without any intent to harm:\""
    },
    "23": {
      "L": "or without seeing him let fall upon him any stone by which a man may die, and he was not his enemy and did not seek his harm,",
      "M": "\"or accidentally dropped a lethal stone on someone — without them being enemies and without any malicious intent —\"",
      "T": "\"suppose a heavy stone falls on someone with no premeditation, no prior enmity:\""
    },
    "24": {
      "L": "then the congregation shall judge between the slayer and the blood avenger according to these ordinances.",
      "M": "\"then the community must judge between the killer and the blood avenger according to these regulations.\"",
      "T": "\"the community serves as court. The congregation hears both sides and applies these laws.\""
    },
    "25": {
      "L": "And the congregation shall rescue the manslayer from the hand of the blood avenger, and the congregation shall return him to his city of refuge to which he had fled; and he shall live in it until the death of the high priest who was anointed with the holy oil.",
      "M": "\"The congregation must protect the manslayer from the blood avenger and return him to his city of refuge. He must remain there until the death of the high priest who was anointed with the sacred oil.\"",
      "T": "\"If the community rules accidental killing, they protect the manslayer — escorting him back to his city of refuge. He stays there until the high priest dies. The high priest's death is his release.\""
    },
    "26": {
      "L": "But if the manslayer shall ever go outside the boundary of his city of refuge to which he had fled,",
      "M": "\"But if the manslayer ever ventures outside the boundary of the city of refuge to which he fled,\"",
      "T": "\"If the manslayer steps beyond the boundary of his assigned city —\""
    },
    "27": {
      "L": "and the blood avenger finds him outside the boundary of his city of refuge, and the blood avenger kills the manslayer, he shall not be guilty of blood.",
      "M": "\"and the blood avenger finds him there and kills him, the avenger bears no guilt.\"",
      "T": "\"— and the blood-avenger finds him there and kills him, the avenger has committed no crime. The manslayer's protection ended the moment he crossed the city line.\""
    },
    "28": {
      "L": "For he must remain in his city of refuge until the death of the high priest; after the death of the high priest the manslayer may return to the land of his possession.",
      "M": "\"The manslayer must stay in the city of refuge until the high priest dies; only then may he return to his own land.\"",
      "T": "\"His obligation is clear: stay within the city until the high priest dies. When that day comes, he walks free — back to his own land, untouchable by the avenger.\""
    },
    "29": {
      "L": "And these things shall be a statute of judgment for you throughout your generations in all your dwelling places.",
      "M": "\"These regulations shall be a permanent law throughout your generations wherever you live.\"",
      "T": "\"This is settled law — permanent, applicable wherever Israel lives, binding on every generation.\""
    },
    "30": {
      "L": "Whoever kills any person, the murderer shall be put to death on the evidence of witnesses; but one witness shall not testify against a person to cause him to die.",
      "M": "\"Anyone who kills must be executed on the testimony of witnesses; but no single witness alone may testify to put a person to death.\"",
      "T": "\"Execution requires witnesses — plural. One person's word alone cannot send someone to their death. This is Israel's protection against vengeance masquerading as justice.\""
    },
    "31": {
      "L": "Moreover you shall accept no ransom for the life of a murderer who is guilty of death; he shall certainly be put to death.",
      "M": "\"You must not accept a ransom payment instead of the death of a murderer who deserves to die — he must be executed.\"",
      "T": "\"Blood money cannot buy a murderer's life. No ransom. The death penalty for deliberate homicide is not negotiable and not commutable by any payment.\""
    },
    "32": {
      "L": "And you shall accept no ransom for him who has fled to his city of refuge, that he might return to live in the land before the death of the priest.",
      "M": "\"Nor may you accept payment that would allow a manslayer to leave his city of refuge and resettle in the land before the high priest's death.\"",
      "T": "\"The manslayer cannot buy early release from his city. No payment, no exception, no early parole before the high priest's natural death. Both rules — no ransom for the murderer, no early exit for the manslayer — guard the same conviction: life is not a commodity.\""
    },
    "33": {
      "L": "So you shall not pollute the land where you are; for blood defiles the land; and no atonement can be made for the land for the blood that is shed in it, except by the blood of him who shed it.",
      "M": "\"Do not defile the land where you live; bloodshed defiles the land, and there is no atonement for it except through the blood of the one who shed it.\"",
      "T": "\"Murder defiles the land itself — not metaphorically but actually. The only purification for shed blood is the blood of the one who shed it. There is no ritual substitute, no offering that cleans what a murderer has stained.\""
    },
    "34": {
      "L": "And you shall not defile the land in which you dwell, in the midst of which I dwell; for I the LORD dwell in the midst of the children of Israel.",
      "M": "\"Do not defile the land in which you live — the land where I myself dwell; for I, the LORD, dwell among the Israelites.\"",
      "T": "\"Here is the deepest reason: I live here. The LORD dwells among Israel. A defiled land is an affront to the holy God whose home it is. Keep it clean — not for your own sake alone, but because the one who inhabits it is holy.\""
    }
  },
  "36": {
    "1": {
      "L": "And the heads of the fathers' houses of the families of the children of Gilead the son of Machir the son of Manasseh, of the families of the sons of Joseph, came near and spoke before Moses and before the leaders, the heads of the fathers' houses of the children of Israel,",
      "M": "The heads of the clans of Gilead son of Machir, son of Manasseh, of the families of Joseph's descendants, came forward and addressed Moses and the tribal leaders, the heads of the Israelite clans.",
      "T": "The clan-heads of the Gilead line — Machir's family within Manasseh, Joseph's descendants — brought a case before Moses and the tribal leadership of Israel."
    },
    "2": {
      "L": "and said, The LORD commanded my lord to give the land by lot as an inheritance to the children of Israel, and my lord was commanded by the LORD to give the inheritance of Zelophehad our brother to his daughters.",
      "M": "They said: \"The LORD commanded that the land be distributed by lot to the Israelites. Our lord was also commanded by the LORD to give our kinsman Zelophehad's inheritance to his daughters.\"",
      "T": "\"The LORD ordered the land distributed by lot,\" they said. \"And we accept that the LORD ordered Zelophehad's inheritance to pass to his daughters.\""
    },
    "3": {
      "L": "Now if they are married to any of the sons of the other tribes of the children of Israel, then their inheritance will be taken from the inheritance of our fathers and added to the inheritance of the tribe to which they belong; so it will be taken away from the allotment of our inheritance.",
      "M": "\"But if those daughters marry into another tribe of Israel, their inheritance will pass out of our tribal portion and into the tribe they marry into — our territory shrinks permanently.\"",
      "T": "\"But consider: if they marry into another tribe, their inherited land goes with them. Our tribal holding shrinks. The land the LORD gave us walks away through marriage.\""
    },
    "4": {
      "L": "And when the Jubilee of the children of Israel comes, then their inheritance will be added to the inheritance of the tribe to which they belong; and their inheritance will be taken from the inheritance of the tribe of our fathers.",
      "M": "\"And when the Jubilee comes, their inheritance will stay with the tribe they married into — our original allotment is permanently reduced.\"",
      "T": "\"Not even the Jubilee restores it. The Jubilee returns land to its original family line — but if those daughters are now in another tribe, that is the family line the land returns to. Once lost through marriage, it is lost for good.\""
    },
    "5": {
      "L": "And Moses commanded the children of Israel according to the word of the LORD, saying, The tribe of the sons of Joseph speaks rightly.",
      "M": "At the LORD's direction Moses told the Israelites: \"What the tribe of Joseph's descendants says is correct.\"",
      "T": "Moses received the LORD's ruling and announced it to the assembly: \"The Josephite clans are right.\""
    },
    "6": {
      "L": "This is what the LORD commands concerning the daughters of Zelophehad: Let them marry whom they think best; only they must marry within the clan of their father's tribe.",
      "M": "\"Here is the LORD's ruling on Zelophehad's daughters: they may marry anyone they wish, but only within their father's tribal clan.\"",
      "T": "\"Zelophehad's daughters may marry any man they choose — they are free. But they must choose from within their own tribe. That is the LORD's ruling.\""
    },
    "7": {
      "L": "So no inheritance shall be transferred from one tribe to another tribe; for each of the children of Israel shall hold fast to the inheritance of the tribe of his fathers.",
      "M": "\"No inheritance is to pass from one tribe to another; every Israelite is to keep the ancestral tribal inheritance intact.\"",
      "T": "\"The principle: tribal inheritances do not cross tribal lines. Each tribe holds what it was given. This is what it means to be a people with a God-apportioned land.\""
    },
    "8": {
      "L": "And every daughter who possesses an inheritance in any tribe of the children of Israel shall become the wife of one from the clan of her father's tribe, so that every Israelite may possess the inheritance of his fathers.",
      "M": "\"Every daughter in Israel who inherits land must marry within her father's tribal clan, so that every Israelite retains the inheritance of their ancestors.\"",
      "T": "\"The same principle applies to every daughter who inherits in any tribe: marry within your father's clan. The land stays where it was planted.\""
    },
    "9": {
      "L": "No inheritance shall be transferred from one tribe to another tribe, for each of the tribes of the children of Israel shall hold fast to its own inheritance.",
      "M": "\"No tribal inheritance may move from one tribe to another; every tribe of Israel shall keep its own allotment.\"",
      "T": "\"Israel's map must not be redrawn by marriage. Every tribe keeps its boundaries. The land the LORD assigned remains where he assigned it.\""
    },
    "10": {
      "L": "Even as the LORD commanded Moses, so did the daughters of Zelophehad.",
      "M": "The daughters of Zelophehad did exactly as the LORD commanded through Moses.",
      "T": "The daughters of Zelophehad complied without hesitation, doing precisely what the LORD had directed."
    },
    "11": {
      "L": "For Mahlah, Tirzah, Hoglah, Milcah, and Noah, the daughters of Zelophehad, were married to sons of their uncles.",
      "M": "Mahlah, Tirzah, Hoglah, Milcah, and Noah — the daughters of Zelophehad — married their cousins, the sons of their uncles.",
      "T": "Mahlah, Tirzah, Hoglah, Milcah, Noah — all five daughters married within the Manasseh clan, choosing their cousins."
    },
    "12": {
      "L": "They were married into the clans of the sons of Manasseh the son of Joseph, and their inheritance remained in the tribe of their father's clan.",
      "M": "They married into the clans of Manasseh son of Joseph, and their inheritance remained within their father's tribal clan.",
      "T": "Their inheritance stayed in Manasseh — right where it began. The land did not move."
    },
    "13": {
      "L": "These are the commandments and the ordinances that the LORD commanded through Moses to the children of Israel in the plains of Moab by the Jordan near Jericho.",
      "M": "These are the commandments and ordinances that the LORD gave through Moses to the Israelites on the plains of Moab by the Jordan at Jericho.",
      "T": "These were the final legal rulings the LORD delivered through Moses to Israel — spoken on the plains of Moab, within sight of the Jordan, on the threshold of the promised land. Here Numbers ends."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'numbers')
        merge_tier(existing, NUMBERS, tier_key)
        save(tier_dir, 'numbers', existing)
    print('Numbers 31–36 written.')

if __name__ == '__main__':
    main()
