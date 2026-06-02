"""
MKT Joshua chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-joshua-13-18.py

Covers: Remaining unconquered land and the Transjordanian allotments for Reuben, Gad,
and half-Manasseh confirmed (ch. 13); introduction to Cisjordanian allotment and Caleb's
bold claim of Hebron at age 85 (ch. 14); Judah's full boundary and city list, including
Caleb's capture of Hebron and Debir, and Achsah's request for water springs (ch. 15);
Ephraim's boundary and the failure at Gezer (ch. 16); Manasseh's allotment, Zelophehad's
daughters, and the house of Joseph's complaint (ch. 17); the assembly at Shiloh, Joshua's
rebuke, the land survey, and Benjamin's allotment (ch. 18).

Translation decisions (carried forward from mkt-joshua-1-6.py):
- H3068 (יהוה): "LORD" (small caps convention) L/M; "the LORD" T
- H430 (אֱלֹהִים): "God" all tiers
- H5159 (נַחֲלָה): "inheritance" all tiers — the theological weight of חֶלֶק ("portion/share")
  is preserved where both roots appear together by using "allotment" or "portion" as
  a secondary rendering; "inheritance" signals the covenant-grant framework
- H1486 (גּוֹרָל): "lot" all tiers — casting lots is not random chance but divine decision
- H2505 (חָלַק): "divide/distribute/allot" — context determines English rendering; T
  occasionally uses "apportion" to signal the covenantal framework
- H1366 (גְּבוּל): "border/coast" L; "boundary/territory/border" M; "boundary/territory" T
- H5157 (נָחַל): "give as inheritance/receive as inheritance" — active/passive per subject
- H3423 (יָרַשׁ): "possess/drive out/dispossess" — context determines: driving out enemies vs.
  taking ownership; the failure to drive out (vv. 13:13, 15:63, 16:10, 17:12–13) is a
  recurring theological alarm, rendered consistently as "drive out" / "expel"
- H1121 + H3478 (בְּנֵי יִשְׂרָאֵל): "children of Israel" L; "Israelites" M; "Israel/Israelites" T
- H7626 (שֵׁבֶט) / H4294 (מַטֶּה): both "tribe" all tiers
- H4940 (מִשְׁפָּחָה): "families" L; "clans" M/T
- H2617 (חֶסֶד): not a primary term in these chapters; consistent with prior scripts where
  it appears — "kindness/faithful kindness/steadfast loyal love"
- Caleb's "wholly followed" (H4390 מָלֵא + H310 אַחֲרֵי): "wholly followed" L;
  "wholeheartedly followed" M; "followed with his whole heart" T — 14:8,9,14 — this is
  one of the OT's most striking statements of total devotion; T surfaces its force
- Ch. 13:14,33 note: Levi's inheritance being the LORD himself (not territory) is the
  theological counterpoint to all the boundary lists; T makes the contrast explicit
- Ch. 14:10-11 note: Caleb at 85 claiming a fortified mountain is a faith-act, not boasting;
  T honours this by framing his speech as faith-evidence, not self-promotion
- Ch. 15:15 note: Kiriath-sepher = "City of the Book/Scroll" — T preserves this meaning
- Ch. 15:18-19 note: Achsah's request for springs (H4599 מַיִם) is a woman exercising
  initiative to secure resources; T renders her voice with appropriate directness
- Ch. 16:10 / 17:12-13 note: Failure to expel Canaanites is a recurring covenant-obedience
  failure; T notes its theological weight in 17:13 where the pattern is most explicit
- Ch. 17:14-18 note: Joseph's complaint and Joshua's answer — Joshua refuses to accommodate
  faithlessness; "the forest highlands are yours — clear them" is a command that iron
  chariots cannot neutralize a God-given mandate; T surfaces this
- Ch. 18:1 note: Shiloh as the new cultic center — the tent of meeting moves from Gilgal;
  this is a major theological development; T marks the significance
- Ch. 18:3 note: Joshua's rebuke — "slack" (H7503 רָפָה) implies not laziness but failure
  of nerve/faith; T renders this as "dragging your feet" to convey the spiritual failure
- Geographic boundary formulae ("goings out thereof were at the sea", "coast thereof")
  are rendered consistently: L preserves the formulaic idiom; M uses natural English;
  T uses the same natural English as M unless a verse has theological significance
- City lists (ch. 15 vv. 20-62, ch. 18 vv. 21-28): L preserves the Hebrew proper-noun
  forms; M uses standard English conventional spellings; T matches M — no interpretive
  gain from varying city names
- Rephaim / Anakim / Giblites: all rendered as standard transliterations across all tiers
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

JOSHUA = {
  "13": {
    "1": {
      "L": "Now Joshua was old, advanced in years. And the LORD said to him, You are old and advanced in years, and there remaineth yet very much land to be possessed.",
      "M": "When Joshua was old and advanced in years, the LORD said to him, 'You are old and well along in years, and a great deal of land still remains to be taken over.'",
      "T": "By the time Joshua was old and far along in years, the LORD said to him: 'You are old, and much of your life is behind you — yet a great deal of land remains to be possessed.'"
    },
    "2": {
      "L": "This is the land that yet remaineth: all the regions of the Philistines and all the Geshurites,",
      "M": "This is the land that remains: all the territory of the Philistines and all of the Geshurites,",
      "T": "This is what has not yet been taken: the entire Philistine country and all the territory of the Geshurites,"
    },
    "3": {
      "L": "from the Shihor which is east of Egypt, northward to the border of Ekron — reckoned as Canaanite — the five lords of the Philistines: the Gazathites, the Ashdothites, the Eshkalonites, the Gittites, and the Ekronites; also the Avvim,",
      "M": "from the Shihor east of Egypt northward to Ekron — which is counted as Canaanite — namely the five Philistine lords of Gaza, Ashdod, Ashkelon, Gath, and Ekron; and the Avvim",
      "T": "from the Shihor River east of Egypt all the way north to the border of Ekron — territory reckoned as Canaanite — covering the five Philistine city-lords ruling Gaza, Ashdod, Ashkelon, Gath, and Ekron; and the Avvim"
    },
    "4": {
      "L": "in the south; all the land of the Canaanites and Mearah that belongeth to the Sidonians, to Aphek, to the border of the Amorites,",
      "M": "to the south, all the Canaanite land and Mearah belonging to the Sidonians, reaching to Aphek at the border of the Amorites,",
      "T": "to the south — all the Canaanite territory, including the cave-country of Mearah belonging to the Sidonians, extending to Aphek at the Amorite frontier,"
    },
    "5": {
      "L": "and the land of the Giblites, and all Lebanon toward the sunrise, from Baalgad below Mount Hermon unto the entrance of Hamath,",
      "M": "the land of the Giblites, and all of Lebanon on the east — from Baalgad below Mount Hermon to Lebo-hamath,",
      "T": "the Gebalite territories and all of Lebanon stretching east — from Baalgad at the foot of Mount Hermon all the way to Lebo-hamath in the north,"
    },
    "6": {
      "L": "all the inhabitants of the hill country from Lebanon unto Misrephoth-maim, even all the Sidonians — them will I drive out from before the children of Israel. Only allot it to Israel for an inheritance as I have commanded thee.",
      "M": "all the inhabitants of the mountain region from Lebanon to Misrephoth-maim, all the Sidonians — I will drive them out from before the Israelites. Only be sure to allot this land to Israel as their inheritance, as I commanded you.",
      "T": "every person settled in the highlands from Lebanon to Misrephoth-maim — all the Sidonians. I myself will drive them out from before Israel. For now, your task is simply to allot the land to Israel as I commanded you."
    },
    "7": {
      "L": "Now therefore divide this land for an inheritance unto the nine tribes and the half-tribe of Manasseh.",
      "M": "Now divide this land as an inheritance for the nine tribes and the half-tribe of Manasseh.",
      "T": "So divide this land now and grant it as a lasting inheritance to the nine tribes and the half-tribe of Manasseh."
    },
    "8": {
      "L": "With the Reubenites and the Gadites, the other half-tribe received their inheritance which Moses gave them beyond the Jordan eastward, even as Moses the servant of the LORD gave them:",
      "M": "The Reubenites and Gadites, together with the other half-tribe of Manasseh, had already received the inheritance Moses gave them east of the Jordan — just as Moses the LORD's servant had assigned to them.",
      "T": "The Reubenites, Gadites, and the other half-tribe of Manasseh had already received their portion — Moses had assigned their inheritance east of the Jordan, exactly as the LORD's servant Moses had granted it:"
    },
    "9": {
      "L": "from Aroer that is on the bank of the river Arnon, and the city that is in the midst of the valley, and all the plain of Medeba unto Dibon,",
      "M": "from Aroer on the bank of the Arnon River and the town in the middle of the gorge, all the plateau of Medeba as far as Dibon,",
      "T": "starting from Aroer on the rim of the Arnon Gorge — including the town in the gorge itself — along the entire plateau of Medeba as far as Dibon,"
    },
    "10": {
      "L": "and all the cities of Sihon king of the Amorites who reigned in Heshbon, unto the border of the children of Ammon,",
      "M": "all the cities of Sihon king of the Amorites who had reigned in Heshbon, up to the border of the Ammonites,",
      "T": "and all the cities that had been Sihon's — the Amorite king who once ruled from Heshbon — extending to the Ammonite border,"
    },
    "11": {
      "L": "and Gilead, and the territory of the Geshurites and Maacathites, and all Mount Hermon, and all Bashan unto Salcah,",
      "M": "and Gilead, the territory of the Geshurites and the Maacathites, all of Mount Hermon, and all of Bashan as far as Salecah —",
      "T": "and Gilead, the Geshurite and Maacathite territories, all of Mount Hermon, and all of Bashan as far north as Salecah —"
    },
    "12": {
      "L": "all the kingdom of Og in Bashan who reigned in Ashtaroth and in Edrei — he was of the remnant of the giants. Moses smote them and drove them out.",
      "M": "the entire kingdom of Og of Bashan, who had ruled in Ashtaroth and Edrei. He was one of the last of the Rephaim. Moses defeated and dispossessed them.",
      "T": "the whole kingdom of Og in Bashan, who had ruled from Ashtaroth and Edrei — one of the last survivors of the Rephaim. Moses struck them down and drove them out."
    },
    "13": {
      "L": "Nevertheless the children of Israel did not drive out the Geshurites nor the Maacathites; but the Geshurites and the Maacathites dwell among the Israelites unto this day.",
      "M": "But the Israelites did not drive out the Geshurites or the Maacathites; they live among the Israelites to this day.",
      "T": "However, Israel never expelled the Geshurites or the Maacathites — they have lived among Israel's people from that day to this."
    },
    "14": {
      "L": "Only to the tribe of Levi he gave none inheritance; the offerings made by fire to the LORD God of Israel are their inheritance, as he said unto them.",
      "M": "He gave no inheritance to the tribe of Levi. Their inheritance was the offerings made by fire to the LORD God of Israel, as he had promised them.",
      "T": "The tribe of Levi received no territorial inheritance. Their inheritance was the LORD's own offerings made by fire — the LORD God of Israel himself had declared this would be their portion."
    },
    "15": {
      "L": "And Moses gave unto the tribe of the children of Reuben inheritance according to their families.",
      "M": "Moses gave an inheritance to the tribe of Reuben according to their clans.",
      "T": "Moses assigned the tribal inheritance of Reuben to their various clans."
    },
    "16": {
      "L": "And their territory was from Aroer that is on the bank of the river Arnon, and the city that is in the midst of the valley, and all the plain by Medeba,",
      "M": "Their territory ran from Aroer on the bank of the Arnon and the town in the middle of the gorge, over all the plateau by Medeba,",
      "T": "Their territory stretched from Aroer on the rim of the Arnon Gorge — including the town in the gorge's heart — across the entire plateau near Medeba,"
    },
    "17": {
      "L": "Heshbon and all her cities that are in the plain; Dibon, and Bamoth-baal, and Beth-baal-meon,",
      "M": "Heshbon and all its surrounding towns on the plateau: Dibon, Bamoth-baal, Beth-baal-meon,",
      "T": "Heshbon with its outlying towns on the plateau — Dibon, Bamoth-baal, Beth-baal-meon,"
    },
    "18": {
      "L": "and Jahazah, and Kedemoth, and Mephaath,",
      "M": "Jahaz, Kedemoth, Mephaath,",
      "T": "Jahaz, Kedemoth, Mephaath,"
    },
    "19": {
      "L": "and Kirjathaim, and Sibmah, and Zereth-shahar in the mount of the valley,",
      "M": "Kiriathaim, Sibmah, Zereth-shahar on the hill above the valley,",
      "T": "Kiriathaim, Sibmah, Zereth-shahar on the valley ridge,"
    },
    "20": {
      "L": "and Beth-peor, and Ashdoth-pisgah, and Beth-jeshimoth,",
      "M": "Beth-peor, the slopes of Pisgah, and Beth-jeshimoth —",
      "T": "Beth-peor, the Pisgah slopes, and Beth-jeshimoth —"
    },
    "21": {
      "L": "and all the cities of the plain, and all the kingdom of Sihon king of the Amorites who reigned in Heshbon, whom Moses smote with the princes of Midian: Evi and Rekem and Zur and Hur and Reba, princes of Sihon, who dwelt in the land.",
      "M": "all the cities of the plateau and the entire kingdom of Sihon king of the Amorites who reigned in Heshbon — whom Moses struck down along with the chiefs of Midian: Evi, Rekem, Zur, Hur, and Reba, princes of Sihon, who lived in the country.",
      "T": "all the plateau towns, the whole domain of Sihon the Amorite king of Heshbon — Moses struck him down along with the Midianite chieftains Evi, Rekem, Zur, Hur, and Reba, nobles who had lived in that land under Sihon."
    },
    "22": {
      "L": "Balaam also the son of Beor, the soothsayer, did the children of Israel slay with the sword among them that were slain.",
      "M": "The Israelites also put to the sword Balaam son of Beor, the diviner, along with the others they killed.",
      "T": "Israel also killed Balaam son of Beor — the diviner — by the sword, among all the others who fell."
    },
    "23": {
      "L": "And the border of the children of Reuben was the Jordan and the coast thereof. This was the inheritance of the children of Reuben according to their families, the cities and the villages thereof.",
      "M": "The Jordan and its floodplain formed the western boundary of Reuben. This was the inheritance of the Reubenites according to their clans — the towns and their surrounding villages.",
      "T": "The Jordan River and its bank formed Reuben's western border. Such was the inheritance of Reuben by clan — their towns and villages."
    },
    "24": {
      "L": "And Moses gave inheritance unto the tribe of Gad, even unto the children of Gad, according to their families.",
      "M": "Moses gave an inheritance to the tribe of Gad according to their clans.",
      "T": "Moses assigned the inheritance of Gad to their clans."
    },
    "25": {
      "L": "And their territory was Jazer, and all the cities of Gilead, and half the land of the children of Ammon, unto Aroer that is before Rabbah,",
      "M": "Their territory included Jazer and all the towns of Gilead, half the land of the Ammonites as far as Aroer east of Rabbah,",
      "T": "Gad's territory took in Jazer and all the towns of Gilead, the half of Ammonite land up to Aroer east of Rabbah,"
    },
    "26": {
      "L": "and from Heshbon unto Ramath-mizpeh, and Betonim; and from Mahanaim unto the border of Debir,",
      "M": "from Heshbon to Ramath-mizpah and Betonim, from Mahanaim to the border of Debir,",
      "T": "stretching from Heshbon to Ramath-mizpah and Betonim, from Mahanaim to the Debir boundary,"
    },
    "27": {
      "L": "and in the valley, Beth-haram and Beth-nimrah and Succoth and Zaphon, the rest of the kingdom of Sihon king of Heshbon, with the Jordan as border unto the edge of the sea of Chinnereth on the other side of Jordan eastward.",
      "M": "and in the valley: Beth-haram, Beth-nimrah, Succoth, and Zaphon — the remaining portion of the kingdom of Sihon king of Heshbon, with the Jordan as its boundary to the lower end of the Sea of Chinnereth east of the Jordan.",
      "T": "and in the rift valley: Beth-haram, Beth-nimrah, Succoth, and Zaphon — the remaining portions of Sihon's kingdom — bounded by the Jordan to the southern tip of the Sea of Chinnereth on the east side of the river."
    },
    "28": {
      "L": "This is the inheritance of the children of Gad according to their families, the cities and the villages thereof.",
      "M": "This was the inheritance of the Gadites according to their clans — the towns and their surrounding villages.",
      "T": "Such was Gad's inheritance by clan — their towns and villages."
    },
    "29": {
      "L": "And Moses gave inheritance unto the half tribe of Manasseh; and this was the possession of the half tribe of the children of Manasseh by their families.",
      "M": "Moses gave an inheritance to the half-tribe of Manasseh according to their clans.",
      "T": "Moses assigned the inheritance of the half-tribe of Manasseh to their clans."
    },
    "30": {
      "L": "And their territory was from Mahanaim, all Bashan, all the kingdom of Og king of Bashan, and all the towns of Jair which are in Bashan — threescore cities.",
      "M": "Their territory ran from Mahanaim through all of Bashan — the entire kingdom of Og king of Bashan, including all sixty towns of Jair in Bashan.",
      "T": "Their domain began at Mahanaim and extended through all of Bashan — Og's entire former kingdom — including all sixty towns of Jair in Bashan."
    },
    "31": {
      "L": "And half Gilead, and Ashtaroth, and Edrei, cities of the kingdom of Og in Bashan — these were for the children of Machir the son of Manasseh, even for the half of the children of Machir, by their families.",
      "M": "Half of Gilead and the cities of Ashtaroth and Edrei — the royal cities of Og in Bashan — were given to the descendants of Machir son of Manasseh, to one half of them according to their clans.",
      "T": "Half of Gilead, plus Ashtaroth and Edrei — Og's royal cities in Bashan — went to the descendants of Machir son of Manasseh, to half their number, by their clans."
    },
    "32": {
      "L": "These are the countries which Moses did distribute for inheritance in the plains of Moab, on the other side Jordan, by Jericho eastward.",
      "M": "These were the portions Moses distributed as inheritances in the plains of Moab, east of the Jordan opposite Jericho.",
      "T": "These were the allotments Moses made in the plains of Moab — east of the Jordan, across from Jericho."
    },
    "33": {
      "L": "But unto the tribe of Levi Moses gave not any inheritance: the LORD God of Israel is their inheritance, as he said unto them.",
      "M": "But Moses gave no inheritance to the tribe of Levi; the LORD God of Israel was their inheritance, as he had told them.",
      "T": "But Moses gave the tribe of Levi no land at all. The LORD God of Israel himself is their inheritance — just as he promised them. No borders, no cities, no territory: only God."
    }
  },
  "14": {
    "1": {
      "L": "And these are the countries which the children of Israel inherited in the land of Canaan, which Eleazar the priest, and Joshua the son of Nun, and the heads of the fathers of the tribes of the children of Israel distributed for inheritance to them.",
      "M": "These are the territories the Israelites received as their inheritance in Canaan, distributed by Eleazar the priest, Joshua son of Nun, and the family heads of Israel's tribes.",
      "T": "These are the portions the Israelites inherited in Canaan — distributed by Eleazar the priest, Joshua son of Nun, and the heads of the ancestral families of Israel's tribes."
    },
    "2": {
      "L": "By lot was their inheritance, as the LORD commanded by Moses, for the nine tribes and for the half tribe.",
      "M": "Their inheritance was assigned by lot, as the LORD had commanded through Moses, for the nine and a half tribes.",
      "T": "The lots fell as the LORD had commanded through Moses — distributing the land among the nine and a half tribes."
    },
    "3": {
      "L": "For Moses had given the inheritance of two tribes and an half tribe on the other side Jordan; but unto the Levites he gave none inheritance among them.",
      "M": "For Moses had already given the inheritance of the two and a half tribes on the east side of the Jordan, but he gave no inheritance to the Levites among them.",
      "T": "Moses had already settled the two and a half tribes east of the Jordan, and he had given the Levites no territorial inheritance at all."
    },
    "4": {
      "L": "For the children of Joseph were two tribes, Manasseh and Ephraim: therefore they gave no part unto the Levites in the land, save cities to dwell in, with their suburbs for their cattle and for their substance.",
      "M": "The descendants of Joseph had become two tribes, Manasseh and Ephraim. No portion of land was given to the Levites — only towns to live in, with pasturelands for their flocks and herds.",
      "T": "Joseph's line had split into two tribes — Manasseh and Ephraim — which kept the tribal count at twelve even without Levi. The Levites received no territory, only towns to live in with pasturelands for their livestock."
    },
    "5": {
      "L": "As the LORD commanded Moses, so the children of Israel did, and they divided the land.",
      "M": "The Israelites did as the LORD commanded Moses, and they partitioned the land.",
      "T": "Israel carried out what the LORD had commanded Moses, and the land was divided."
    },
    "6": {
      "L": "Then the children of Judah came unto Joshua in Gilgal: and Caleb the son of Jephunneh the Kenezite said unto him, Thou knowest the thing that the LORD said unto Moses the man of God concerning me and thee in Kadesh-barnea.",
      "M": "The men of Judah approached Joshua at Gilgal. Caleb son of Jephunneh the Kenizzite said to him, 'You know what the LORD told Moses the man of God about you and me at Kadesh-barnea.'",
      "T": "Then the tribe of Judah came to Joshua at Gilgal. Caleb son of Jephunneh the Kenizzite stepped forward and said: 'You know the word the LORD spoke to Moses the man of God concerning you and me at Kadesh-barnea.'"
    },
    "7": {
      "L": "Forty years old was I when Moses the servant of the LORD sent me from Kadesh-barnea to espy out the land; and I brought him back word as it was in mine heart.",
      "M": "I was forty years old when Moses the LORD's servant sent me from Kadesh-barnea to scout the land. I brought back an honest report, exactly what was in my heart.",
      "T": "I was forty years old when Moses the LORD's servant sent me from Kadesh-barnea to scout out the land. I came back and gave him my honest report — I told him exactly what I believed."
    },
    "8": {
      "L": "Nevertheless my brethren that went up with me made the heart of the people melt; but I wholly followed the LORD my God.",
      "M": "My fellow scouts made the people's courage fail, but I followed the LORD my God wholeheartedly.",
      "T": "My fellow spies drained the courage out of the whole people — but I followed the LORD my God with my whole heart."
    },
    "9": {
      "L": "And Moses sware on that day, saying, Surely the land whereon thy feet have trodden shall be thine inheritance, and thy children's for ever, because thou hast wholly followed the LORD my God.",
      "M": "On that day Moses solemnly swore, 'The land your feet have walked on will be your inheritance and your descendants' forever, because you have wholeheartedly followed the LORD my God.'",
      "T": "That very day Moses swore an oath: 'The land your feet have walked will belong to you and your descendants as a permanent inheritance — because you followed the LORD my God with your whole heart.'"
    },
    "10": {
      "L": "And now, behold, the LORD hath kept me alive, as he said, these forty and five years, even since the LORD spake this word unto Moses, while the children of Israel wandered in the wilderness: and now, lo, I am this day fourscore and five years old.",
      "M": "Now see — the LORD has kept me alive for forty-five years, just as he promised, ever since he spoke this word to Moses while Israel was in the wilderness. And today I am eighty-five years old!",
      "T": "And look — the LORD has kept me alive exactly as he promised. Forty-five years have passed since the LORD spoke that word to Moses, all through Israel's wilderness years. Today I am eighty-five years old!"
    },
    "11": {
      "L": "As yet I am as strong this day as I was in the day that Moses sent me: as my strength was then, even so is my strength now, for war, both to go out and to come in.",
      "M": "I am still as strong today as I was when Moses sent me. My strength for battle and for every activity is the same now as it was then.",
      "T": "My strength is the same today as it was when Moses sent me. I can still march, still fight, still lead — just as I could at forty."
    },
    "12": {
      "L": "Now therefore give me this mountain, whereof the LORD spake in that day; for thou heardest in that day how the Anakims were there, and that the cities were great and fenced: if so be the LORD will be with me, then I shall be able to drive them out, as the LORD said.",
      "M": "So give me this hill country that the LORD promised that day! You yourself heard how the Anakites were there with their great fortified cities. If the LORD is with me, I will drive them out just as he said.",
      "T": "So now — give me this mountain! The LORD spoke about it on that day, and you yourself heard how the Anakim were there with their great walled cities. If the LORD is with me — as I know he will be — I will drive them out, just as he promised."
    },
    "13": {
      "L": "And Joshua blessed him, and gave unto Caleb the son of Jephunneh Hebron for an inheritance.",
      "M": "Then Joshua blessed Caleb son of Jephunneh and gave him Hebron as his inheritance.",
      "T": "Joshua blessed him and gave Hebron to Caleb son of Jephunneh as his inheritance."
    },
    "14": {
      "L": "Hebron therefore became the inheritance of Caleb the son of Jephunneh the Kenezite unto this day, because that he wholly followed the LORD God of Israel.",
      "M": "Hebron has belonged to Caleb son of Jephunneh the Kenizzite as his inheritance to this day, because he wholeheartedly followed the LORD God of Israel.",
      "T": "Hebron has been Caleb son of Jephunneh the Kenizzite's inheritance from that day to this — because he followed the LORD God of Israel with his whole heart."
    },
    "15": {
      "L": "And the name of Hebron before was Kirjath-arba; which Arba was a great man among the Anakims. And the land had rest from war.",
      "M": "Hebron's former name was Kiriath-arba, named after Arba, the greatest of the Anakites. And the land had rest from war.",
      "T": "Hebron had once been called Kiriath-arba — 'City of Arba' — after Arba, the greatest warrior among the Anakim. And the land had rest from war."
    }
  },
  "15": {
    "1": {
      "L": "This then was the lot of the tribe of the children of Judah by their families; even to the border of Edom, the wilderness of Zin southward was the uttermost part of the south coast.",
      "M": "The territory allotted to Judah according to their clans extended to the border of Edom, with the Wilderness of Zin in the far south as its southern boundary.",
      "T": "This was the allotment for the tribe of Judah by their clans: along the Edomite border in the south, with the Wilderness of Zin marking the southernmost edge."
    },
    "2": {
      "L": "And their south border was from the shore of the salt sea, from the bay that looketh southward.",
      "M": "Their southern boundary started at the bay at the south end of the Dead Sea.",
      "T": "The southern boundary began at the southern bay of the Dead Sea."
    },
    "3": {
      "L": "And it went out to the south side to Maale-acrabbim, and passed along to Zin, and ascended up on the south side unto Kadesh-barnea, and passed along to Hezron, and went up to Addar, and fetched a compass to Karka.",
      "M": "It ran south of the Ascent of Akrabbim, crossed to Zin, went up south of Kadesh-barnea, passed along to Hezron, went up to Addar, and curved around to Karka.",
      "T": "running south of the Ascent of Scorpions, crossing through Zin, passing south of Kadesh-barnea, continuing along to Hezron, up to Addar, curving around to Karka,"
    },
    "4": {
      "L": "From thence it passed toward Azmon, and went out unto the river of Egypt; and the goings out of that coast were at the sea: this shall be your south coast.",
      "M": "from there it went to Azmon and reached the Wadi of Egypt, ending at the Mediterranean. This was their southern boundary.",
      "T": "on to Azmon, then out along the Wadi of Egypt and ending at the sea. That was their southern line."
    },
    "5": {
      "L": "And the east border was the salt sea, even unto the end of Jordan. And their border in the quarter northward was from the bay of the sea at the uttermost part of Jordan.",
      "M": "The eastern boundary was the Dead Sea as far as the mouth of the Jordan. The northern boundary began at the bay at the mouth of the Jordan.",
      "T": "The eastern boundary ran along the Dead Sea to the mouth of the Jordan. The northern boundary started from the sea's bay at the Jordan's outlet."
    },
    "6": {
      "L": "And the border went up to Beth-hoglah, and passed along by the north of Beth-arabah; and the border went up to the stone of Bohan the son of Reuben.",
      "M": "The boundary went up to Beth-hoglah and continued north of Beth-arabah, then up to the Stone of Bohan son of Reuben.",
      "T": "The border ran up to Beth-hoglah, passed north of Beth-arabah, and climbed to the Stone of Bohan son of Reuben."
    },
    "7": {
      "L": "And the border went up toward Debir from the valley of Achor, and so northward, looking toward Gilgal, that is before the going up to Adummim, which is on the south side of the river: and the border passed toward the waters of En-shemesh, and the goings out thereof were at En-rogel.",
      "M": "The boundary went up toward Debir from the Valley of Achor, then north toward Gilgal facing the Ascent of Adummim south of the valley. It passed along to the waters of En-shemesh, ending at En-rogel.",
      "T": "From the Valley of Achor the line climbed toward Debir, then turned northward toward Gilgal — opposite the Ascent of Adummim on the valley's south slope — passing the springs of En-shemesh and ending at En-rogel."
    },
    "8": {
      "L": "And the border went up by the valley of the son of Hinnom unto the south side of the Jebusite; the same is Jerusalem: and the border went up to the top of the mountain that lieth before the valley of Hinnom westward, which is at the end of the valley of the giants northward.",
      "M": "The boundary went up through the Valley of Ben-hinnom to the south slope of the Jebusite city — that is Jerusalem — and then up to the mountaintop west of the Hinnom Valley, at the northern end of the Valley of Rephaim.",
      "T": "From there the border climbed through the Valley of Ben-hinnom to the south slope of Jebusite Jerusalem, then up to the hilltop west of the Hinnom Valley — at the northern end of the Valley of Rephaim."
    },
    "9": {
      "L": "And the border was drawn from the top of the hill unto the fountain of the water of Nephtoah, and went out to the cities of mount Ephron; and the border was drawn to Baalah, which is Kirjath-jearim.",
      "M": "From the mountaintop the boundary ran to the spring of the waters of Nephtoah, passed to the towns of Mount Ephron, and extended to Baalah — that is Kiriath-jearim.",
      "T": "From the hilltop the line ran to the spring at Nephtoah, to the towns of Mount Ephron, and on to Baalah — the same place as Kiriath-jearim."
    },
    "10": {
      "L": "And the border compassed from Baalah westward unto mount Seir, and passed along unto the side of mount Jearim, which is Chesalon, on the north side, and went down to Beth-shemesh, and passed on to Timnah.",
      "M": "From Baalah the boundary turned west to Mount Seir, ran along to the north side of Mount Jearim — that is Chesalon — came down to Beth-shemesh, and continued to Timnah.",
      "T": "From Baalah the line turned west to Mount Seir, ran along the north flank of Mount Jearim — that is Chesalon — descended to Beth-shemesh, and continued on to Timnah."
    },
    "11": {
      "L": "And the border went out unto the side of Ekron northward; and the border was drawn to Shicron, and passed along to mount Baalah, and went out unto Jabneel; and the goings out of the border were at the sea.",
      "M": "The boundary went out to the north slope of Ekron, turned to Shikkeron, ran along to Mount Baalah, and extended to Jabneel. The boundary ended at the sea.",
      "T": "The border continued to the north side of Ekron, swung around to Shikkeron, along Mount Baalah to Jabneel — and the sea marked the end."
    },
    "12": {
      "L": "And the west border was to the great sea, and the coast thereof. This is the coast of the children of Judah round about according to their families.",
      "M": "The western boundary was the Mediterranean coastline. These were the boundaries of Judah on all sides, according to their clans.",
      "T": "The western border was simply the Mediterranean Sea. These were Judah's boundaries on every side, by their clans."
    },
    "13": {
      "L": "And unto Caleb the son of Jephunneh he gave a part among the children of Judah, according to the commandment of the LORD to Joshua, even the city of Arba the father of Anak, which city is Hebron.",
      "M": "In keeping with the LORD's command to Joshua, Caleb son of Jephunneh was given a portion within Judah's territory — the city of Arba, father of Anak, which is Hebron.",
      "T": "Following the LORD's command to Joshua, Caleb son of Jephunneh received his portion within Judah — Kiriath-arba, city of Arba the ancestor of Anak, which is Hebron."
    },
    "14": {
      "L": "And Caleb drove thence the three sons of Anak: Sheshai, and Ahiman, and Talmai, the children of Anak.",
      "M": "Caleb drove out from there the three Anakites — Sheshai, Ahiman, and Talmai, descendants of Anak.",
      "T": "Caleb drove out the three sons of Anak from Hebron — Sheshai, Ahiman, and Talmai."
    },
    "15": {
      "L": "And he went up thence to the inhabitants of Debir: and the name of Debir before was Kirjath-sepher.",
      "M": "From there he went up against the people of Debir, formerly known as Kiriath-sepher.",
      "T": "From Hebron he marched against Debir — once called Kiriath-sepher, the City of the Scroll."
    },
    "16": {
      "L": "And Caleb said, He that smiteth Kirjath-sepher, and taketh it, to him will I give Achsah my daughter to wife.",
      "M": "Caleb said, 'Whoever attacks Kiriath-sepher and captures it — I will give him my daughter Achsah as his wife.'",
      "T": "Caleb announced: 'Whoever strikes Kiriath-sepher and takes it, I will give him my daughter Achsah as his wife.'"
    },
    "17": {
      "L": "And Othniel the son of Kenaz, the brother of Caleb, took it: and he gave him Achsah his daughter to wife.",
      "M": "Othniel son of Kenaz, Caleb's younger brother, took it. So Caleb gave him his daughter Achsah as his wife.",
      "T": "Othniel son of Kenaz — Caleb's own brother — took the city. Caleb gave him Achsah as promised."
    },
    "18": {
      "L": "And it came to pass, as she came unto him, that she moved him to ask of her father a field: and she lighted off her ass; and Caleb said unto her, What wouldest thou?",
      "M": "When Achsah arrived, she urged Othniel to ask her father for a field. As she got down from her donkey, Caleb asked her, 'What do you want?'",
      "T": "When Achsah arrived, she persuaded Othniel to ask her father for farmland. She slipped off her donkey, and Caleb asked her: 'What do you need?'"
    },
    "19": {
      "L": "Who answered, Give me a blessing; for thou hast given me a south land; give me also springs of water. And he gave her the upper springs, and the nether springs.",
      "M": "She replied, 'Give me a gift. You've given me dry southern land — please give me springs of water too.' So he gave her the upper and lower springs.",
      "T": "'Give me a blessing,' she said. 'You've given me the Negev — arid land. Give me the springs of water too.' So he gave her both the upper springs and the lower springs."
    },
    "20": {
      "L": "This is the inheritance of the tribe of the children of Judah according to their families.",
      "M": "This was the inheritance of the tribe of Judah according to their clans.",
      "T": "Such was the inheritance of Judah by their clans."
    },
    "21": {
      "L": "And the uttermost cities of the tribe of the children of Judah toward the coast of Edom southward were Kabzeel, and Eder, and Jagur,",
      "M": "The southernmost towns of the tribe of Judah, toward the border of Edom, were: Kabzeel, Eder, Jagur,",
      "T": "Judah's southernmost towns, near the Edomite border, included: Kabzeel, Eder, Jagur,"
    },
    "22": {
      "L": "and Kinah, and Dimonah, and Adadah,",
      "M": "Kinah, Dimonah, Adadah,",
      "T": "Kinah, Dimonah, Adadah,"
    },
    "23": {
      "L": "and Kedesh, and Hazor, and Ithnan,",
      "M": "Kedesh, Hazor, Ithnan,",
      "T": "Kedesh, Hazor, Ithnan,"
    },
    "24": {
      "L": "Ziph, and Telem, and Bealoth,",
      "M": "Ziph, Telem, Bealoth,",
      "T": "Ziph, Telem, Bealoth,"
    },
    "25": {
      "L": "and Hazor-hadattah, and Kerioth-hezron, which is Hazor,",
      "M": "Hazor-hadattah, Kerioth-hezron — that is, Hazor —",
      "T": "Hazor-hadattah, Kerioth-hezron (which is Hazor),"
    },
    "26": {
      "L": "Amam, and Shema, and Moladah,",
      "M": "Amam, Shema, Moladah,",
      "T": "Amam, Shema, Moladah,"
    },
    "27": {
      "L": "and Hazargaddah, and Heshmon, and Beth-palet,",
      "M": "Hazar-gaddah, Heshmon, Beth-pelet,",
      "T": "Hazar-gaddah, Heshmon, Beth-pelet,"
    },
    "28": {
      "L": "and Hazarshual, and Beer-sheba, and Bizjothjah,",
      "M": "Hazar-shual, Beersheba, Biziothiah,",
      "T": "Hazar-shual, Beersheba, Biziothiah,"
    },
    "29": {
      "L": "Baalah, and Iim, and Azem,",
      "M": "Baalah, Iim, Ezem,",
      "T": "Baalah, Iim, Ezem,"
    },
    "30": {
      "L": "and Eltolad, and Chesil, and Hormah,",
      "M": "Eltolad, Chesil, Hormah,",
      "T": "Eltolad, Chesil, Hormah,"
    },
    "31": {
      "L": "and Ziklag, and Madmannah, and Sansannah,",
      "M": "Ziklag, Madmannah, Sansannah,",
      "T": "Ziklag, Madmannah, Sansannah,"
    },
    "32": {
      "L": "and Lebaoth, and Shilhim, and Ain, and Rimmon: all the cities are twenty and nine, with their villages.",
      "M": "Lebaoth, Shilhim, Ain, and Rimmon — twenty-nine towns in all, with their surrounding villages.",
      "T": "Lebaoth, Shilhim, Ain, and Rimmon. Twenty-nine towns in all, with their villages."
    },
    "33": {
      "L": "And in the valley, Eshtaol, and Zoreah, and Ashnah,",
      "M": "In the Shephelah: Eshtaol, Zorah, Ashnah,",
      "T": "In the foothills of the Shephelah: Eshtaol, Zorah, Ashnah,"
    },
    "34": {
      "L": "and Zanoah, and En-gannim, Tappuah, and Enam,",
      "M": "Zanoah, En-gannim, Tappuah, Enam,",
      "T": "Zanoah, En-gannim, Tappuah, Enam,"
    },
    "35": {
      "L": "Jarmuth, and Adullam, Socoh, and Azekah,",
      "M": "Jarmuth, Adullam, Socoh, Azekah,",
      "T": "Jarmuth, Adullam, Socoh, Azekah,"
    },
    "36": {
      "L": "and Sharaim, and Adithaim, and Gederah, and Gederothaim; fourteen cities with their villages.",
      "M": "Shaaraim, Adithaim, Gederah, and Gederothaim — fourteen towns with their villages.",
      "T": "Shaaraim, Adithaim, Gederah, and Gederothaim. Fourteen towns with their villages."
    },
    "37": {
      "L": "Zenan, and Hadashah, and Migdal-gad,",
      "M": "Zenan, Hadashah, Migdal-gad,",
      "T": "Zenan, Hadashah, Migdal-gad,"
    },
    "38": {
      "L": "and Dilean, and Mizpeh, and Joktheel,",
      "M": "Dilean, Mizpeh, Joktheel,",
      "T": "Dilean, Mizpeh, Joktheel,"
    },
    "39": {
      "L": "Lachish, and Bozkath, and Eglon,",
      "M": "Lachish, Bozkath, Eglon,",
      "T": "Lachish, Bozkath, Eglon,"
    },
    "40": {
      "L": "and Cabbon, and Lahmam, and Kithlish,",
      "M": "Cabbon, Lahmas, Kithlish,",
      "T": "Cabbon, Lahmas, Kithlish,"
    },
    "41": {
      "L": "and Gederoth, Beth-dagon, and Naamah, and Makkedah; sixteen cities with their villages.",
      "M": "Gederoth, Beth-dagon, Naamah, and Makkedah — sixteen towns with their villages.",
      "T": "Gederoth, Beth-dagon, Naamah, and Makkedah. Sixteen towns with their villages."
    },
    "42": {
      "L": "Libnah, and Ether, and Ashan,",
      "M": "Libnah, Ether, Ashan,",
      "T": "Libnah, Ether, Ashan,"
    },
    "43": {
      "L": "and Jiphtah, and Ashnah, and Nezib,",
      "M": "Iphtah, Ashnah, Nezib,",
      "T": "Iphtah, Ashnah, Nezib,"
    },
    "44": {
      "L": "and Keilah, and Achzib, and Mareshah; nine cities with their villages.",
      "M": "Keilah, Achzib, and Mareshah — nine towns with their villages.",
      "T": "Keilah, Achzib, and Mareshah. Nine towns with their villages."
    },
    "45": {
      "L": "Ekron, with her towns and her villages.",
      "M": "Ekron with its surrounding towns and villages;",
      "T": "Ekron with its towns and villages;"
    },
    "46": {
      "L": "From Ekron even unto the sea, all that lay near Ashdod, with their villages.",
      "M": "from Ekron to the sea, all the territory near Ashdod, with their villages;",
      "T": "from Ekron to the coast — all the territory near Ashdod — with their villages;"
    },
    "47": {
      "L": "Ashdod with her towns and her villages, Gaza with her towns and her villages, unto the river of Egypt, and the great sea, and the border thereof.",
      "M": "Ashdod with its towns and villages, Gaza with its towns and villages, extending to the Wadi of Egypt and the coast of the Great Sea.",
      "T": "Ashdod with its towns and villages, Gaza with its towns and villages, reaching the Wadi of Egypt and the Mediterranean as its border."
    },
    "48": {
      "L": "And in the mountains, Shamir, and Jattir, and Socoh,",
      "M": "In the hill country: Shamir, Jattir, Socoh,",
      "T": "In the highlands: Shamir, Jattir, Socoh,"
    },
    "49": {
      "L": "and Dannah, and Kirjath-sannah, which is Debir,",
      "M": "Dannah, Kiriath-sannah — that is, Debir —",
      "T": "Dannah, Kiriath-sannah (which is Debir),"
    },
    "50": {
      "L": "and Anab, and Eshtemoh, and Anim,",
      "M": "Anab, Eshtemoh, Anim,",
      "T": "Anab, Eshtemoh, Anim,"
    },
    "51": {
      "L": "and Goshen, and Holon, and Giloh; eleven cities with their villages.",
      "M": "Goshen, Holon, and Giloh — eleven towns with their villages.",
      "T": "Goshen, Holon, and Giloh. Eleven towns with their villages."
    },
    "52": {
      "L": "Arab, and Dumah, and Eshean,",
      "M": "Arab, Dumah, Eshan,",
      "T": "Arab, Dumah, Eshan,"
    },
    "53": {
      "L": "and Janum, and Beth-tappuah, and Aphekah,",
      "M": "Janum, Beth-tappuah, Aphekah,",
      "T": "Janum, Beth-tappuah, Aphekah,"
    },
    "54": {
      "L": "and Humtah, and Kirjath-arba, which is Hebron, and Zior; nine cities with their villages.",
      "M": "Humtah, Kiriath-arba — that is, Hebron — and Zior; nine towns with their villages.",
      "T": "Humtah, Kiriath-arba (that is, Hebron), and Zior. Nine towns with their villages."
    },
    "55": {
      "L": "Maon, Carmel, and Ziph, and Juttah,",
      "M": "Maon, Carmel, Ziph, Juttah,",
      "T": "Maon, Carmel, Ziph, Juttah,"
    },
    "56": {
      "L": "and Jezreel, and Jokdeam, and Zanoah,",
      "M": "Jezreel, Jokdeam, Zanoah,",
      "T": "Jezreel, Jokdeam, Zanoah,"
    },
    "57": {
      "L": "Cain, Gibeah, and Timnah; ten cities with their villages.",
      "M": "Kain, Gibeah, and Timnah — ten towns with their villages.",
      "T": "Kain, Gibeah, and Timnah. Ten towns with their villages."
    },
    "58": {
      "L": "Halhul, Beth-zur, and Gedor,",
      "M": "Halhul, Beth-zur, Gedor,",
      "T": "Halhul, Beth-zur, Gedor,"
    },
    "59": {
      "L": "and Maarath, and Beth-anoth, and Eltekon; six cities with their villages.",
      "M": "Maarath, Beth-anoth, and Eltekon — six towns with their villages.",
      "T": "Maarath, Beth-anoth, and Eltekon. Six towns with their villages."
    },
    "60": {
      "L": "Kirjath-baal, which is Kirjath-jearim, and Rabbah; two cities with their villages.",
      "M": "Kiriath-baal — that is, Kiriath-jearim — and Rabbah; two towns with their villages.",
      "T": "Kiriath-baal (that is, Kiriath-jearim) and Rabbah. Two towns with their villages."
    },
    "61": {
      "L": "In the wilderness, Beth-arabah, Middin, and Secacah,",
      "M": "In the wilderness: Beth-arabah, Middin, Secacah,",
      "T": "In the desert wilderness: Beth-arabah, Middin, Secacah,"
    },
    "62": {
      "L": "and Nibshan, and the city of Salt, and En-gedi; six cities with their villages.",
      "M": "Nibshan, the City of Salt, and En-gedi — six towns with their villages.",
      "T": "Nibshan, the City of Salt, and En-gedi. Six towns with their villages."
    },
    "63": {
      "L": "As for the Jebusites the inhabitants of Jerusalem, the children of Judah could not drive them out: but the Jebusites dwell with the children of Judah at Jerusalem unto this day.",
      "M": "But the Israelites could not drive out the Jebusites who lived in Jerusalem. To this day the Jebusites live there among the people of Judah.",
      "T": "The Jebusites who lived in Jerusalem, however, Judah could not expel. The Jebusites have lived there among Judah's people from that day to this — a failure that will have long consequences."
    }
  },
  "16": {
    "1": {
      "L": "And the lot of the children of Joseph fell from Jordan by Jericho, unto the water of Jericho on the east, to the wilderness that goeth up from Jericho throughout mount Bethel,",
      "M": "The allotment for the descendants of Joseph began at the Jordan by Jericho, east of the Jericho spring, and went through the wilderness up from Jericho into the hill country to Bethel.",
      "T": "The allotment for the house of Joseph started at the Jordan near Jericho — at the springs east of Jericho — and ran through the desert up into the highlands toward Bethel."
    },
    "2": {
      "L": "And goeth out from Bethel to Luz, and passeth along unto the borders of Archi to Ataroth,",
      "M": "From Bethel it went to Luz and ran along to the border of the Archites at Ataroth.",
      "T": "From Bethel the line passed through Luz and ran along to Ataroth, on the Archite frontier."
    },
    "3": {
      "L": "And goeth down westward to the coast of Japhleti, unto the coast of Beth-horon the nether, and to Gezer: and the goings out thereof are at the sea.",
      "M": "It descended westward through Japhletite territory to the region of Lower Beth-horon and Gezer, ending at the sea.",
      "T": "The boundary descended westward through Japhletite territory to Lower Beth-horon and on to Gezer, where it ended at the sea."
    },
    "4": {
      "L": "So the children of Joseph, Manasseh and Ephraim, took their inheritance.",
      "M": "So the descendants of Joseph — Manasseh and Ephraim — received their inheritance.",
      "T": "In this way Joseph's two sons — Manasseh and Ephraim — received their inheritance."
    },
    "5": {
      "L": "And the border of the children of Ephraim according to their families was thus: even the border of their inheritance on the east side was Atarothaddar, unto Beth-horon the upper.",
      "M": "The territory of the Ephraimites by their clans was bordered on the east by Ataroth-addar and extended to Upper Beth-horon.",
      "T": "The boundary of Ephraim by their clans: on the eastern side it ran from Ataroth-addar to Upper Beth-horon."
    },
    "6": {
      "L": "And the border went out toward the sea to Michmethah on the north side; and the border went about eastward unto Taanath-shiloh, and passed by it on the east to Janohah.",
      "M": "The boundary extended to the sea on the north side at Michmethath, then turned east toward Taanath-shiloh, passing it on the east to Janoah.",
      "T": "On the north the border ran to the sea at Michmethath, then curved eastward to Taanath-shiloh and along to Janoah."
    },
    "7": {
      "L": "And it went down from Janohah to Ataroth, and to Naarah, and came to Jericho, and went out at Jordan.",
      "M": "From Janoah it went down to Ataroth and Naarah, touched Jericho, and came out at the Jordan.",
      "T": "From Janoah it descended to Ataroth and Naarah, skirted Jericho, and met the Jordan."
    },
    "8": {
      "L": "The border went out from Tappuah westward unto the river Kanah; and the goings out thereof were at the sea. This is the inheritance of the tribe of the children of Ephraim by their families.",
      "M": "The boundary ran from Tappuah westward to the Kanah Ravine and ended at the sea. This was the inheritance of the tribe of Ephraim by their clans.",
      "T": "The border ran from Tappuah westward along the Kanah Ravine to the sea. This was Ephraim's inheritance by their clans."
    },
    "9": {
      "L": "And the separate cities for the children of Ephraim were among the inheritance of the children of Manasseh, all the cities with their villages.",
      "M": "Some cities were set apart for Ephraim within the territory of Manasseh — all those towns with their villages.",
      "T": "There were also towns reserved for Ephraim within Manasseh's territory, along with all their surrounding villages."
    },
    "10": {
      "L": "And they drave not out the Canaanites that dwelt in Gezer: but the Canaanites dwell among the Ephraimites unto this day, and serve under tribute.",
      "M": "But the Ephraimites did not drive out the Canaanites living in Gezer. The Canaanites have lived among the Ephraimites to this day, though subject to forced labor.",
      "T": "However, Ephraim never expelled the Canaanites living in Gezer. They remain among Ephraim's people to this day — pressed into labor, but not driven out. The pattern of incomplete obedience continues."
    }
  },
  "17": {
    "1": {
      "L": "There was also a lot for the tribe of Manasseh; for he was the firstborn of Joseph; to wit, for Machir the firstborn of Manasseh, the father of Gilead: because he was a man of war, therefore he had Gilead and Bashan.",
      "M": "Now for the tribe of Manasseh — as Joseph's firstborn son, Machir the firstborn of Manasseh, the father of Gilead, was given Gilead and Bashan because he was a man of war.",
      "T": "The allotment for Manasseh — the firstborn of Joseph: Machir, Manasseh's firstborn and father of Gilead, was granted Gilead and Bashan because he was a warrior."
    },
    "2": {
      "L": "There was also a lot for the rest of the children of Manasseh by their families; for the children of Abiezer, and for the children of Helek, and for the children of Asriel, and for the children of Shechem, and for the children of Hepher, and for the children of Shemida: these were the male children of Manasseh the son of Joseph by their families.",
      "M": "The remaining Manassites were allotted land by their clans: the clans of Abiezer, Helek, Asriel, Shechem, Hepher, and Shemida — the male descendants of Manasseh son of Joseph.",
      "T": "The remaining clans of Manasseh also received portions — the clans of Abiezer, Helek, Asriel, Shechem, Hepher, and Shemida: the male descendants of Manasseh son of Joseph."
    },
    "3": {
      "L": "But Zelophehad, the son of Hepher, the son of Gilead, the son of Machir, the son of Manasseh, had no sons, but daughters: and these are the names of his daughters, Mahlah, and Noah, Hoglah, Milcah, and Tirzah.",
      "M": "But Zelophehad son of Hepher, son of Gilead, son of Machir, son of Manasseh, had no sons — only daughters, named Mahlah, Noah, Hoglah, Milcah, and Tirzah.",
      "T": "Zelophehad son of Hepher — son of Gilead, son of Machir, son of Manasseh — had no sons, only daughters: Mahlah, Noah, Hoglah, Milcah, and Tirzah."
    },
    "4": {
      "L": "And they came near before Eleazar the priest, and before Joshua the son of Nun, and before the princes, saying, The LORD commanded Moses to give us an inheritance among our brethren. Therefore according to the commandment of the LORD he gave them an inheritance among the brethren of their father.",
      "M": "They appeared before Eleazar the priest, Joshua son of Nun, and the leaders, saying, 'The LORD commanded Moses to give us an inheritance among our relatives.' So Joshua gave them an inheritance among their father's brothers, following the LORD's command.",
      "T": "They appeared before Eleazar the priest, Joshua son of Nun, and the assembly's leaders and said: 'The LORD commanded Moses to give us an inheritance among our relatives.' Following the LORD's command, Joshua gave them an inheritance among their father's brothers."
    },
    "5": {
      "L": "And there fell ten portions to Manasseh, beside the land of Gilead and Bashan, which were on the other side Jordan,",
      "M": "So Manasseh received ten portions in addition to the land of Gilead and Bashan east of the Jordan,",
      "T": "So Manasseh received ten portions west of the Jordan — in addition to Gilead and Bashan on the east —"
    },
    "6": {
      "L": "because the daughters of Manasseh had an inheritance among his sons: and the rest of Manasseh's sons had the land of Gilead.",
      "M": "because Manasseh's daughters inherited among his sons. The rest of Manasseh's sons had the land of Gilead.",
      "T": "because Manasseh's daughters received their portion alongside his sons. The remaining sons held the land of Gilead."
    },
    "7": {
      "L": "And the coast of Manasseh was from Asher to Michmethah, that lieth before Shechem; and the border went along on the right hand unto the inhabitants of En-tappuah.",
      "M": "The territory of Manasseh extended from Asher to Michmethath east of Shechem. The border then turned south to the inhabitants of En-tappuah.",
      "T": "Manasseh's border ran from Asher to Michmethath east of Shechem, then turned southward toward the settlement of En-tappuah."
    },
    "8": {
      "L": "Now Manasseh had the land of Tappuah: but Tappuah on the border of Manasseh belonged to the children of Ephraim.",
      "M": "Manasseh had the surrounding land of Tappuah, but the town of Tappuah on the Manasseh border belonged to the Ephraimites.",
      "T": "The lands around Tappuah were Manasseh's, but the town of Tappuah itself — right on the border — belonged to Ephraim."
    },
    "9": {
      "L": "And the coast descended unto the river Kanah, southward of the river: these cities of Ephraim are among the cities of Manasseh: the coast of Manasseh also was on the north side of the river, and the outgoings of it were at the sea.",
      "M": "The boundary descended to the Kanah Ravine, following the south side of the ravine. These Ephraimite towns lay within Manasseh's territory; Manasseh's border was on the north side of the ravine and ended at the sea.",
      "T": "The border went down along the Kanah Ravine — on the south bank. The Ephraimite towns here were set within Manasseh's territory; Manasseh's northern line ran along the ravine to the sea."
    },
    "10": {
      "L": "Southward it was Ephraim's, and northward it was Manasseh's, and the sea is his border; and they met together in Asher on the north, and in Issachar on the east.",
      "M": "The territory to the south was Ephraim's and to the north was Manasseh's, with the sea as its western boundary. On the north they bordered Asher and on the east they bordered Issachar.",
      "T": "South of the ravine was Ephraim; north was Manasseh. The sea formed the western edge. Asher lay to the north and Issachar to the east."
    },
    "11": {
      "L": "And Manasseh had in Issachar and in Asher Beth-shean and her towns, and Ibleam and her towns, and the inhabitants of Dor and her towns, and the inhabitants of En-dor and her towns, and the inhabitants of Taanach and her towns, and the inhabitants of Megiddo and her towns, even three countries.",
      "M": "Within the territory of Issachar and Asher, Manasseh held Beth-shean with its towns, Ibleam with its towns, the people of Dor with its towns, the people of En-dor with its towns, the people of Taanach with its towns, and the people of Megiddo with its towns — those three highland districts.",
      "T": "Manasseh also held enclaves within Issachar and Asher: Beth-shean with its surrounding towns, Ibleam with its towns, Dor with its towns, En-dor with its towns, Taanach with its towns, and Megiddo with its towns — those three highland regions."
    },
    "12": {
      "L": "Yet the children of Manasseh could not drive out the inhabitants of those cities; but the Canaanites would dwell in that land.",
      "M": "But the Manassites were unable to drive out the people of those towns; the Canaanites persisted in living in that region.",
      "T": "But the Manassites could not expel the Canaanites from those towns — the Canaanites held their ground in that land."
    },
    "13": {
      "L": "Yet it came to pass, when the children of Israel were waxen strong, that they put the Canaanites to tribute; but did not utterly drive them out.",
      "M": "When the Israelites grew stronger, they subjected the Canaanites to forced labor but did not drive them out completely.",
      "T": "When Israel's strength grew, they put the Canaanites to forced labor — but they never fully drove them out. Tribute is not obedience; this half-measure will bear bitter fruit."
    },
    "14": {
      "L": "And the children of Joseph spake unto Joshua, saying, Why hast thou given me but one lot and one portion to inherit, seeing I am a great people, forasmuch as the LORD hath blessed me hitherto?",
      "M": "The descendants of Joseph said to Joshua, 'Why have you given us only one allotment and one portion? We are a numerous people — the LORD has richly blessed us!'",
      "T": "The descendants of Joseph confronted Joshua: 'Why have you given us only a single lot? We are a great people — the LORD has blessed us abundantly. One portion is not enough!'"
    },
    "15": {
      "L": "And Joshua answered them, If thou be a great people, then get thee up to the wood country, and cut down for thyself there in the land of the Perizzites and of the giants, if mount Ephraim be too narrow for thee.",
      "M": "Joshua replied, 'If you are such a great people, go up into the forest and clear land there in the territory of the Perizzites and Rephaim, since the hill country of Ephraim is too small for you.'",
      "T": "'If you are such a great people,' Joshua answered, 'go up into the forest and clear it for yourselves in the Perizzite and Rephaim country. If the highlands of Ephraim can't contain you, make room for yourselves there.'"
    },
    "16": {
      "L": "And the children of Joseph said, The hill country is not enough for us: and all the Canaanites that dwell in the land of the valley have chariots of iron, both they who are of Beth-shean and her towns, and they who are of the valley of Jezreel.",
      "M": "The Josephites replied, 'The hill country is not enough for us, and all the Canaanites in the lowland have iron chariots — both those in Beth-shean and its towns, and those in the Valley of Jezreel.'",
      "T": "The Josephites pushed back: 'The highlands aren't enough. And the Canaanites in the valley have iron chariots — those in Beth-shean and its towns, those in the Valley of Jezreel. We cannot face them.'"
    },
    "17": {
      "L": "And Joshua spake unto the house of Joseph, even to Ephraim and to Manasseh, saying, Thou art a great people, and hast great power: thou shalt not have one lot only.",
      "M": "But Joshua said to the house of Joseph — to Ephraim and Manasseh: 'You are a great people and have great power. You will not have just one allotment.'",
      "T": "Joshua stood firm with the house of Joseph — Ephraim and Manasseh both: 'You are a great people with great strength. You will not have just one portion.'"
    },
    "18": {
      "L": "But the mountain shall be thine; for it is a wood, and thou shalt cut it down: and the outgoings of it shall be thine: for thou shalt drive out the Canaanites, though they have iron chariots, and though they be strong.",
      "M": "'The forested hill country will be yours. Clear it, and it will be yours to its farthest limits. You will drive out the Canaanites, even though they have iron chariots and are strong.'",
      "T": "'The forest highlands are yours — all of them. Clear them. The whole range will be yours to its farthest edge. And you will drive out the Canaanites, iron chariots and all. Their strength is no match for the one who gave you this land.'"
    }
  },
  "18": {
    "1": {
      "L": "And the whole congregation of the children of Israel assembled together at Shiloh, and set up the tent of meeting there. And the land was subdued before them.",
      "M": "The entire Israelite community assembled at Shiloh, where they set up the tent of meeting. The land had been subdued before them.",
      "T": "The whole assembly of Israel gathered at Shiloh and erected the tent of meeting there. The land was subdued — this gathering at Shiloh marks a new center of worship, the ark finding its first permanent home in the promised land."
    },
    "2": {
      "L": "And there remained among the children of Israel seven tribes, which had not yet received their inheritance.",
      "M": "But seven Israelite tribes had not yet received their allotment.",
      "T": "Seven tribes of Israel, however, still had not been given their inheritance."
    },
    "3": {
      "L": "And Joshua said unto the children of Israel, How long are ye slack to go in to possess the land, which the LORD God of your fathers hath given you?",
      "M": "Joshua asked the Israelites, 'How long will you put off going in to claim the land the LORD God of your ancestors has given you?'",
      "T": "Joshua challenged the people: 'How long will you drag your feet about going in to take hold of the land the LORD God of your ancestors has given you?'"
    },
    "4": {
      "L": "Give out from among you three men for each tribe: and I will send them, and they shall rise, and go through the land, and describe it according to the inheritance of them; and they shall come again to me.",
      "M": "Appoint three men from each tribe. I will send them out to travel through the land and write a description of it in terms suitable for distributing as an inheritance. They will bring the report to me.",
      "T": "Choose three men from each tribe. I will send them out to survey the land — to walk through it and write a description of it for distributing as inheritances. Bring their report back to me."
    },
    "5": {
      "L": "And they shall divide it into seven parts: Judah shall abide in their coast on the south, and the house of Joseph shall abide in their coasts on the north.",
      "M": "They are to divide the land into seven sections. Judah will stay in its territory to the south, and the house of Joseph will remain in its territory to the north.",
      "T": "They are to divide it into seven portions. Judah keeps its territory in the south, Joseph's house keeps its territory in the north."
    },
    "6": {
      "L": "Ye shall therefore describe the land into seven parts, and bring the description hither to me, that I may cast lots for you here before the LORD our God.",
      "M": "After you have written descriptions of the seven sections, bring them here to me, and I will cast lots for you before the LORD our God.",
      "T": "Write down the seven sections and bring the description to me here. I will cast the lots for you in the presence of the LORD our God."
    },
    "7": {
      "L": "But the Levites have no part among you; for the priesthood of the LORD is their inheritance: and Gad, and Reuben, and half the tribe of Manasseh, have received their inheritance beyond Jordan on the east, which Moses the servant of the LORD gave them.",
      "M": "The Levites have no share among you, for the priestly service of the LORD is their inheritance. And Gad, Reuben, and the half-tribe of Manasseh have already received their inheritance east of the Jordan, which Moses the LORD's servant gave them.",
      "T": "Remember: the Levites get no land portion among you — the LORD's priesthood is their inheritance. And Gad, Reuben, and the half-tribe of Manasseh have already been settled east of the Jordan by Moses the LORD's servant."
    },
    "8": {
      "L": "And the men arose, and went away: and Joshua charged them that went to describe the land, saying, Go and walk through the land, and describe it, and come again to me, that I may here cast lots for you before the LORD in Shiloh.",
      "M": "The men got up and went. Joshua commanded those going to map the land: 'Go and walk through the land, write up a description, and come back to me. I will cast lots for you here before the LORD in Shiloh.'",
      "T": "The men rose up and went. Joshua gave them their charge: 'Travel through the land, write up a full description, and return to me — I will cast the lots for you here before the LORD at Shiloh.'"
    },
    "9": {
      "L": "And the men went and passed through the land, and described it by cities into seven parts in a book, and came again to Joshua to the host at Shiloh.",
      "M": "The men went and traveled through the land. They mapped it town by town in seven sections, recorded in a document, and returned to Joshua at the camp at Shiloh.",
      "T": "The men traveled through the land, recorded all the towns in seven sections in a written document, and brought it back to Joshua at the Shiloh camp."
    },
    "10": {
      "L": "And Joshua cast lots for them in Shiloh before the LORD: and there Joshua divided the land unto the children of Israel according to their divisions.",
      "M": "Joshua cast lots for them before the LORD in Shiloh. There Joshua distributed the land to the Israelites according to their allotted portions.",
      "T": "Joshua cast the lots before the LORD at Shiloh, and there he distributed the land to each of the remaining tribes — the LORD's own allocation, made known through the lot."
    },
    "11": {
      "L": "And the lot of the tribe of the children of Benjamin came up according to their families: and the coast of their lot came forth between the children of Judah and the children of Joseph.",
      "M": "The lot for the tribe of Benjamin came up according to their clans. Their allotted territory fell between the territories of Judah and Joseph.",
      "T": "The lot for the tribe of Benjamin fell to their clans. Their territory lay between Judah and Joseph — held between the two great houses."
    },
    "12": {
      "L": "And their border on the north side was from Jordan; and the border went up to the side of Jericho on the north side, and went up through the mountains westward; and the goings out thereof were at the wilderness of Beth-aven.",
      "M": "Their northern boundary started at the Jordan, went up the north slope of Jericho, climbed westward through the hill country, and ended at the wilderness of Beth-aven.",
      "T": "Benjamin's northern border started at the Jordan, climbed the north slope of Jericho, went up westward through the highlands, and came out at the wilderness of Beth-aven."
    },
    "13": {
      "L": "And the border went over from thence toward Luz, to the side of Luz, which is Bethel, southward; and the border descended to Atarothadar, near the hill that lieth on the south side of the nether Beth-horon.",
      "M": "From there the border went to Luz — the south side of Luz, that is Bethel — and came down to Ataroth-addar near the hill south of Lower Beth-horon.",
      "T": "From there it ran past Luz — the south side of Luz, which is Bethel — then descended to Ataroth-addar near the hill south of Lower Beth-horon."
    },
    "14": {
      "L": "And the border was drawn thence, and compassed the corner of the sea southward, from the hill that lieth before Beth-horon southward; and the goings out thereof were at Kirjath-baal, which is Kirjath-jearim, a city of the children of Judah: this was the west quarter.",
      "M": "The border then curved around on the west side going south from the hill south of Beth-horon, ending at Kiriath-baal — that is Kiriath-jearim, a Judahite city. This was the western side.",
      "T": "The border curved westward, going south from the hill south of Beth-horon, and ended at Kiriath-baal — that is, Kiriath-jearim, a Judahite city. That was the western side."
    },
    "15": {
      "L": "And the south quarter was from the end of Kirjath-jearim, and the border went out on the west, and went out to the well of waters of Nephtoah.",
      "M": "The southern side began at the outskirts of Kiriath-jearim. The border went westward to the spring of the waters of Nephtoah.",
      "T": "The southern boundary began at the edge of Kiriath-jearim. From there it ran west to the spring at Nephtoah."
    },
    "16": {
      "L": "And the border came down to the end of the mountain that lieth before the valley of the son of Hinnom, and which is in the valley of the giants on the north, and descended to the valley of Hinnom, to the side of Jebusi on the south, and descended to En-rogel.",
      "M": "The border came down to the edge of the hill facing the Valley of Ben-hinnom, at the north end of the Valley of Rephaim. It continued down into the Hinnom Valley along the southern slope of Jebusi and went down to En-rogel.",
      "T": "The border descended to the far end of the hill above the Valley of Ben-hinnom, at the north tip of the Valley of Rephaim. From there it dropped into the Hinnom Valley along the south slope of Jebusite Jerusalem and down to En-rogel."
    },
    "17": {
      "L": "And was drawn from the north, and went forth to En-shemesh, and went forth toward Geliloth, which is over against the going up of Adummim, and descended to the stone of Bohan the son of Reuben.",
      "M": "From En-rogel it bent northward to En-shemesh, passed on to Geliloth opposite the Ascent of Adummim, and descended to the Stone of Bohan son of Reuben.",
      "T": "From En-rogel the line bent north to En-shemesh, passed toward Geliloth opposite the Ascent of Adummim, and dropped to the Stone of Bohan son of Reuben."
    },
    "18": {
      "L": "And passed along toward the side over against Arabah northward, and went down unto Arabah.",
      "M": "The border continued north along the slope opposite the Arabah and went down into the Arabah.",
      "T": "The border then ran north along the slope above the Arabah valley and descended into it."
    },
    "19": {
      "L": "And the border passed along to the side of Beth-hoglah northward: and the outgoings of the border were at the north bay of the salt sea at the south end of Jordan: this was the south coast.",
      "M": "The boundary ran along the north side of Beth-hoglah and ended at the northern bay of the Dead Sea, at the mouth of the Jordan. This was the southern boundary.",
      "T": "The line ran along the north side of Beth-hoglah and came to an end at the north bay of the Dead Sea, where the Jordan empties in. That was the southern boundary."
    },
    "20": {
      "L": "And Jordan was the border of it on the east side. This was the inheritance of the children of Benjamin, by the coasts thereof round about, according to their families.",
      "M": "The Jordan formed the eastern boundary. This was the inheritance of Benjamin according to its boundaries on all sides, by their clans.",
      "T": "The Jordan served as the eastern border. This was Benjamin's inheritance — its full boundaries on every side — allotted to their clans."
    },
    "21": {
      "L": "Now the cities of the tribe of the children of Benjamin according to their families were Jericho, and Beth-hoglah, and the valley of Keziz,",
      "M": "The towns belonging to the tribe of Benjamin by their clans were: Jericho, Beth-hoglah, the Valley of Keziz,",
      "T": "Benjamin's towns by their clans included: Jericho, Beth-hoglah, the Valley of Keziz,"
    },
    "22": {
      "L": "and Beth-arabah, and Zemaraim, and Beth-el,",
      "M": "Beth-arabah, Zemaraim, Bethel,",
      "T": "Beth-arabah, Zemaraim, Bethel,"
    },
    "23": {
      "L": "and Avim, and Parah, and Ophrah,",
      "M": "Avvim, Parah, Ophrah,",
      "T": "Avvim, Parah, Ophrah,"
    },
    "24": {
      "L": "and Chepharhaammonai, and Ophni, and Gaba; twelve cities with their villages.",
      "M": "Chephar-ammoni, Ophni, and Geba — twelve towns with their villages.",
      "T": "Chephar-ammoni, Ophni, and Geba. Twelve towns with their villages."
    },
    "25": {
      "L": "Gibeon, and Ramah, and Beeroth,",
      "M": "Gibeon, Ramah, Beeroth,",
      "T": "Gibeon, Ramah, Beeroth,"
    },
    "26": {
      "L": "and Mizpeh, and Chephirah, and Mozah,",
      "M": "Mizpah, Chephirah, Mozah,",
      "T": "Mizpah, Chephirah, Mozah,"
    },
    "27": {
      "L": "and Rekem, and Irpeel, and Taralah,",
      "M": "Rekem, Irpeel, Taralah,",
      "T": "Rekem, Irpeel, Taralah,"
    },
    "28": {
      "L": "and Zelah, Eleph, and Jebusi, which is Jerusalem, Gibeath, and Kirjath; fourteen cities with their villages. This is the inheritance of the children of Benjamin according to their families.",
      "M": "Zelah, Haeleph, Jebus — that is Jerusalem — Gibeah, and Kiriath — fourteen towns with their villages. This was the inheritance of Benjamin according to their clans.",
      "T": "Zelah, Haeleph, Jebus — that is, Jerusalem — Gibeah, and Kiriath. Fourteen towns with their villages. This was Benjamin's inheritance by their clans."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'joshua')
        merge_tier(existing, JOSHUA, tier_key)
        save(tier_dir, 'joshua', existing)
    print('Joshua 13–18 written.')

if __name__ == '__main__':
    main()
