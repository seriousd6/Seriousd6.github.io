"""
MKT Joshua chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-joshua-19-24.py

Covers: The final six tribal allotments — Simeon (nested in Judah), Zebulun, Issachar, Asher,
Naphtali, Dan — with Joshua's own inheritance at Timnath-serah and the formal close of the
land distribution at Shiloh (ch. 19); cities of refuge appointed (ch. 20); forty-eight Levitical
cities assigned, with the great theological summary of fulfilment (ch. 21); the eastern tribes
return and build an altar at the Jordan, triggering a near-civil-war resolved by the Phinehas
delegation (ch. 22); Joshua's farewell address (ch. 23); covenant renewal at Shechem, Joshua's
death, burial of Joseph's bones and Eleazar (ch. 24).

Translation decisions:
- H3068 (יהוה): "LORD" (small caps) L/M; "the LORD" T — consistent with mkt-joshua-1-6.py
- H430 (אֱלֹהִים): "God" all tiers
- H5159 (נַחֲלָה) / H5157 (נָחַל): "inheritance" all tiers — dominant term throughout chs. 19–21
- H1366 (גְּבוּל): "border/coast" L; "territory/border" M; "boundary" T
- H4054 (מִגְרָשׁ): "suburbs" (KJV) rendered "pasturelands" in all tiers — refers to open land
  around Levitical cities for livestock; "suburbs" is archaic and misleading
- H4733 (מִקְלָט): "refuge" all tiers — "cities of refuge" kept as compound noun
- H1350 (גֹּאֵל) + H1818 (דָּם): "avenger of blood" L/M/T — the kinsman-redeemer role
  exercised as blood-duty; T surfaces the social institution's dual function (justice / mercy)
- H7523 (רָצַח): "kill / manslayer" L; "kills / manslayer" M/T — distinct from H2026 (הָרַג)
  "murder" in that the cities protect the unintentional killer pending judgment
- H1697 (דָּבָר): "word / thing" contextually; in 21:45 / 23:14: "word / promise"
- H4196 (מִזְבֵּחַ): "altar" all tiers — central to the ch. 22 controversy
- H5707 (עֵד): "witness" all tiers — the name of the altar in ch. 22 ("Ed")
- H410 / H430 / H3068 triple invocation (22:22): preserved literally in L as "El, God, the LORD";
  M renders as "The Mighty One, God, the LORD!" (triple solemn oath-formula); T notes its
  force as an adjuration calling God himself as witness
- H1285 (בְּרִית): "covenant" all tiers — ch. 24 covenant renewal
- H5315 (נֶפֶשׁ): "soul" L; "heart/life/soul" M/T by context — ch. 23:14 uses "heart and soul"
- H571 (אֱמֶת): "truth" L; "faithfulness" M; "fidelity" T — ch. 24:14
- H8549 (תָּמִים): "wholeness" L; "sincerity" M; "integrity" T — ch. 24:14
- H6918 (קָדוֹשׁ): "holy" all tiers — ch. 24:19 "a holy God" (plural adjective; qualitative)
- H7067 (קַנָּא): "jealous" L/M; "fiercely loyal" T — ch. 24:19; divine jealousy = intolerance
  of divided allegiance, not envy; T surfaces the covenant-loyalty force
- H5104 (נָהָר) "the River" = the Euphrates, unnamed in Hebrew; L: "the River"; M: "the
  Euphrates"; T: "the great Euphrates" — ch. 24:2–3
- H6880 (צִרְעָה) "the hornet" — ch. 24:12; likely a divine instrument of psychological terror
  (cf. Deut 7:20; Exod 23:28); may be literal hornets or metaphor; L/M: "the hornet";
  T notes the ambiguity and Deut 7 echo
- H7307 (רוּחַ) not prominent in chs. 19–24; where present, context determines rendering
- H2617 (חֶסֶד): does not appear prominently in these chapters
- Ch. 19:9 note: Simeon nested inside Judah echoes Jacob's dying curse (Gen 49:5-7) —
  "I will scatter them in Israel"; the allotment is not punishment but fulfillment of prophecy
- Ch. 19:47 note: Dan's failure to hold its allotted territory (cf. Judg 1:34) leads to the
  northern migration and conquest of Leshem/Laish; the episode anticipates Judges
- Ch. 19:51 note: Conclusion of all allotments at Shiloh before the tent of meeting — the
  tabernacle at Shiloh is the institutional center until the ark's capture in 1 Sam 4
- Ch. 21:43-45 note: These three verses are the theological heart of Joshua — total fulfilment
  of the land promises. Not a single word of the LORD's promise went unfulfilled. T must be
  eloquent; these verses answer Genesis 12:1-3 and Deut 28's blessings fully
- Ch. 22:5 note: Joshua's five-fold charge (love / walk / keep / cling / serve) mirrors Deut
  6:5 and 10:12-13 — T notes the Shema echo
- Ch. 22:20 note: Achan reference — ch. 7's principle that one man's unfaithfulness brings
  corporate judgment is invoked; the altar appears as potential community-level sin
- Ch. 23:1 note: "rest" (H5117 נוּחַ) — the book's central theme; Joshua's farewell opens
  by declaring the rest secured, then warns it can be forfeited
- Ch. 23:13 note: "snares and traps, scourges on your sides and thorns in your eyes" — Exod
  23:33 and Deut 7:16 echoes; the nations left among Israel will reverse the promise if Israel
  assimilates to them
- Ch. 24:1 note: Shechem is laden with patriarchal memory — Abraham's first altar in Canaan
  (Gen 12:6-7), Jacob's purchase of the parcel and purging of foreign gods (Gen 33:18-20;
  35:2-4); T draws the typological arc
- Ch. 24:2-13 note: The historical recital follows a covenant lawsuit (ריב) pattern common in
  ancient Near Eastern treaties: sovereign's acts enumerated before loyalty demands are made;
  T notes this diplomatic-legal form
- Ch. 24:19-20 note: Joshua's "you cannot serve the LORD" is a prophetic challenge, not despair
  — he is testing the depth of the commitment; T surfaces this rhetorical function
- Ch. 24:27 note: The stone "heard" all the words of the LORD — Hebrew personification of the
  memorial witness; echoes the Laban/Jacob pillar at Mizpah (Gen 31:48); inanimate creation
  summoned as covenant witness anticipates Deut 32:1 and Isa 1:2
- Ch. 24:32 note: Joseph's bones complete a chain of promise 400 years long — Jacob's oath
  (Gen 50:25), Moses carrying them from Egypt (Exod 13:19), now buried in Jacob's own
  purchased field at Shechem — the only plot of Canaanite land the patriarchs legally owned
- Ch. 24:33 note: Three burials end the book — Joshua, Joseph's bones, Eleazar — the generation
  of conquest rests in the land; the door opens onto Judges
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
  "19": {
    "1": {
      "L": "And the second lot came out for Simeon, for the tribe of the children of Simeon according to their families. And their inheritance was within the inheritance of the children of Judah.",
      "M": "The second lot came out for the tribe of the Simeonites, according to their families. Their inheritance lay within the territory of the Judahites.",
      "T": "The second lot fell to Simeon. The Simeonites received their allotment nested inside Judah's territory — already hinting at the fragmentation Jacob had foreseen when he cursed the violence of Simeon and Levi."
    },
    "2": {
      "L": "And they had in their inheritance Beersheba, Sheba, and Moladah,",
      "M": "Their inheritance included Beersheba, Sheba, and Moladah,",
      "T": "Their towns were: Beersheba, Sheba, and Moladah —"
    },
    "3": {
      "L": "and Hazar-shual, Balah, and Azem,",
      "M": "Hazar-shual, Balah, and Azem,",
      "T": "Hazar-shual, Balah, and Azem,"
    },
    "4": {
      "L": "and Eltolad, Bethul, and Hormah,",
      "M": "Eltolad, Bethul, and Hormah,",
      "T": "Eltolad, Bethul, and Hormah,"
    },
    "5": {
      "L": "and Ziklag, Beth-marcaboth, and Hazar-susah,",
      "M": "Ziklag, Beth-marcaboth, and Hazar-susah,",
      "T": "Ziklag, Beth-marcaboth, and Hazar-susah,"
    },
    "6": {
      "L": "and Beth-lebaoth and Sharuhen — thirteen cities and their villages;",
      "M": "Beth-lebaoth and Sharuhen — thirteen cities with their villages.",
      "T": "Beth-lebaoth and Sharuhen — thirteen cities in all, with their surrounding villages."
    },
    "7": {
      "L": "Ain, Rimmon, Ether, and Ashan — four cities and their villages;",
      "M": "Ain, Rimmon, Ether, and Ashan — four cities with their villages;",
      "T": "and also Ain, Rimmon, Ether, and Ashan — four more towns with their villages."
    },
    "8": {
      "L": "and all the villages that were around these cities as far as Baalath-beer, Ramah of the Negeb. This is the inheritance of the tribe of the children of Simeon according to their families.",
      "M": "and all the villages around these cities as far as Baalath-beer, which is Ramah of the Negeb. This is the inheritance of the tribe of the Simeonites according to their families.",
      "T": "together with all the settlements around these towns stretching to Baalath-beer, also called Ramah of the Negeb. That is the full inheritance of the tribe of Simeon, assigned according to their clans."
    },
    "9": {
      "L": "Out of the share of the children of Judah was the inheritance of the children of Simeon, because the portion of the children of Judah was too large for them. Therefore the children of Simeon had their inheritance within their inheritance.",
      "M": "The inheritance of the Simeonites was taken from the allotment of Judah, because Judah's share was more than they needed. So the Simeonites received their inheritance within Judah's territory.",
      "T": "Simeon's share was carved out of Judah's — Judah's allotment had been too large for them to fill. So Simeon settled within Judah, a tribe without its own borders, just as Jacob had foretold."
    },
    "10": {
      "L": "And the third lot came up for the children of Zebulun according to their families. And the boundary of their inheritance reached as far as Sarid.",
      "M": "The third lot came out for the Zebulunites according to their families. Their boundary ran as far as Sarid.",
      "T": "The third lot fell to Zebulun. Their boundary extended as far as Sarid."
    },
    "11": {
      "L": "Then their border went up westward to Maralah and reached to Dabbesheth, and reached to the wadi that is opposite Jokneam.",
      "M": "Their border went up westward to Maralah, reached Dabbesheth, and extended to the wadi east of Jokneam.",
      "T": "Going westward, the line climbed to Maralah, touched Dabbesheth, and ran on to the ravine east of Jokneam."
    },
    "12": {
      "L": "Then it turned from Sarid toward the sunrise in the direction of Chisloth-tabor, and went out to Daberath, and went up to Japhia.",
      "M": "Turning eastward from Sarid toward the sunrise, it went to Chisloth-tabor, then out to Daberath, and up to Japhia.",
      "T": "From Sarid the line swung east toward the sunrise — to Chisloth-tabor, then to Daberath, and up to Japhia."
    },
    "13": {
      "L": "From there it passed along on the east to Gath-hepher, to Eth-kazin, and went out to Rimmon which extends toward Neah.",
      "M": "Continuing eastward it went to Gath-hepher and Eth-kazin, and out to Rimmon, curving around toward Neah.",
      "T": "Eastward still, the boundary reached Gath-hepher and Eth-kazin, and ended at Rimmon on its way around toward Neah."
    },
    "14": {
      "L": "Then the border curved around it on the north to Hannathon, and its outgoings were at the Valley of Iphtahel.",
      "M": "The border then curved around on the north side to Hannathon, ending at the Valley of Iphtahel.",
      "T": "On the north the line curved around to Hannathon and terminated at the Valley of Iphtahel."
    },
    "15": {
      "L": "Kattath, Nahalal, Shimron, Idalah, and Bethlehem — twelve cities with their villages.",
      "M": "The included towns were: Kattath, Nahalal, Shimron, Idalah, and Bethlehem — twelve cities with their villages.",
      "T": "Within this boundary: Kattath, Nahalal, Shimron, Idalah, and Bethlehem — twelve towns in all, each with its surrounding villages."
    },
    "16": {
      "L": "This is the inheritance of the children of Zebulun according to their families — these cities and their villages.",
      "M": "This is the inheritance of the Zebulunites according to their families — these cities and their villages.",
      "T": "That is Zebulun's inheritance, assigned by clan — those towns and their outlying settlements."
    },
    "17": {
      "L": "The fourth lot came out for Issachar, for the children of Issachar according to their families.",
      "M": "The fourth lot came out for Issachar, for the Issacharites according to their families.",
      "T": "The fourth lot fell to Issachar, allotted to the Issacharites according to their clans."
    },
    "18": {
      "L": "And their territory included Jezreel, Chesulloth, and Shunem,",
      "M": "Their territory included Jezreel, Chesulloth, and Shunem,",
      "T": "Their towns included Jezreel, Chesulloth, and Shunem —"
    },
    "19": {
      "L": "Hapharaim, Shion, and Anaharath,",
      "M": "Hapharaim, Shion, and Anaharath,",
      "T": "Hapharaim, Shion, and Anaharath,"
    },
    "20": {
      "L": "Rabbith, Kishion, and Abez,",
      "M": "Rabbith, Kishion, and Abez,",
      "T": "Rabbith, Kishion, and Abez,"
    },
    "21": {
      "L": "Remeth, En-gannim, En-haddah, and Beth-pazzez.",
      "M": "Remeth, En-gannim, En-haddah, and Beth-pazzez.",
      "T": "Remeth, En-gannim, En-haddah, and Beth-pazzez."
    },
    "22": {
      "L": "And the border reached to Tabor, Shahazimah, and Beth-shemesh, and the outgoings of their border were at the Jordan — sixteen cities with their villages.",
      "M": "The boundary reached Tabor, Shahazimah, and Beth-shemesh, ending at the Jordan — sixteen cities with their villages.",
      "T": "The boundary ran to Tabor, Shahazimah, and Beth-shemesh and ended at the Jordan — sixteen towns in all, with their villages."
    },
    "23": {
      "L": "This is the inheritance of the tribe of the children of Issachar according to their families — the cities and their villages.",
      "M": "This is the inheritance of the tribe of the Issacharites according to their families — these cities and their villages.",
      "T": "That is Issachar's inheritance, assigned by clan — those cities and their outlying villages."
    },
    "24": {
      "L": "And the fifth lot came out for the tribe of the children of Asher according to their families.",
      "M": "The fifth lot came out for the tribe of the Asherites according to their families.",
      "T": "The fifth lot fell to Asher, distributed among their clans."
    },
    "25": {
      "L": "And their territory included Helkath, Hali, Beten, and Achshaph,",
      "M": "Their territory included Helkath, Hali, Beten, and Achshaph,",
      "T": "Their towns included Helkath, Hali, Beten, and Achshaph —"
    },
    "26": {
      "L": "and Alammelech, Amad, and Mishal. And it reached to Carmel westward and to Shihor-libnath.",
      "M": "Alammelech, Amad, and Mishal. The territory reached Carmel to the west and Shihor-libnath.",
      "T": "Alammelech, Amad, and Mishal — with the boundary reaching westward to Carmel and to Shihor-libnath."
    },
    "27": {
      "L": "Then it turned toward the sunrise to Beth-dagon, reached to Zebulun and to the Valley of Iphtahel northward, then to Beth-emek and Neiel, and went out to Cabul on the north,",
      "M": "The border then turned eastward to Beth-dagon, touched Zebulun and the Valley of Iphtahel on the north, went to Beth-emek and Neiel, and extended to Cabul on the north.",
      "T": "Turning east, the line went to Beth-dagon, touched Zebulun and the Valley of Iphtahel on the north, continued to Beth-emek and Neiel, and reached Cabul on the north."
    },
    "28": {
      "L": "and Ebron, Rehob, Hammon, and Kanah, as far as Great Sidon.",
      "M": "including Ebron, Rehob, Hammon, and Kanah, as far as Great Sidon.",
      "T": "and on to Ebron, Rehob, Hammon, and Kanah — all the way up to Greater Sidon on the Phoenician coast."
    },
    "29": {
      "L": "Then the border turned to Ramah and to the fortified city of Tyre. And the border turned to Hosah, and its outgoings were at the sea by the region of Achzib,",
      "M": "The border then turned to Ramah and the fortified city of Tyre, curved to Hosah, and ended at the sea in the area of Achzib,",
      "T": "The boundary turned to Ramah, touched the fortress city of Tyre, curved to Hosah, and reached the Mediterranean at Achzib on the coast —"
    },
    "30": {
      "L": "Ummah, Aphek, and Rehob — twenty-two cities with their villages.",
      "M": "along with Ummah, Aphek, and Rehob — twenty-two cities with their villages.",
      "T": "with Ummah, Aphek, and Rehob included — twenty-two towns with their surrounding settlements."
    },
    "31": {
      "L": "This is the inheritance of the tribe of the children of Asher according to their families — these cities with their villages.",
      "M": "This is the inheritance of the tribe of the Asherites according to their families — these cities with their villages.",
      "T": "That is Asher's inheritance, assigned by clan — those cities and their villages."
    },
    "32": {
      "L": "The sixth lot came out for the children of Naphtali — for the children of Naphtali according to their families.",
      "M": "The sixth lot came out for the Naphtalites, according to their families.",
      "T": "The sixth lot fell to Naphtali, distributed among their clans."
    },
    "33": {
      "L": "And their border ran from Heleph, from the oak at Zaanannim, and Adami-nekeb, and Jabneel, to Lakkum, and its outgoings were at the Jordan.",
      "M": "Their boundary ran from Heleph, from the great oak at Zaanannim, through Adami-nekeb and Jabneel, to Lakkum, and ended at the Jordan.",
      "T": "Their boundary started at Heleph — at the great oak of Zaanannim — ran through Adami-nekeb and Jabneel to Lakkum, and ended at the Jordan."
    },
    "34": {
      "L": "Then the border turned westward to Aznoth-tabor and went out from there to Hukkok, touching Zebulun on the south and Asher on the west, and Judah at the Jordan toward the sunrise.",
      "M": "The border then turned westward to Aznoth-tabor, went out to Hukkok, touching Zebulun on the south, Asher on the west, and Judah at the Jordan toward the east.",
      "T": "Turning west, the line went to Aznoth-tabor and out to Hukkok — bordering Zebulun to the south, Asher to the west, and Judah along the Jordan to the east."
    },
    "35": {
      "L": "The fortified cities were Ziddim, Zer, Hammath, Rakkath, and Chinnereth,",
      "M": "The fortified cities were Ziddim, Zer, Hammath, Rakkath, and Chinnereth,",
      "T": "Naphtali's fortified towns were: Ziddim, Zer, Hammath, Rakkath, and Chinnereth —"
    },
    "36": {
      "L": "and Adamah, Ramah, and Hazor,",
      "M": "Adamah, Ramah, and Hazor,",
      "T": "Adamah, Ramah, and Hazor,"
    },
    "37": {
      "L": "and Kedesh, Edrei, and En-hazor,",
      "M": "Kedesh, Edrei, and En-hazor,",
      "T": "Kedesh, Edrei, and En-hazor,"
    },
    "38": {
      "L": "and Iron, Migdal-el, Horem, Beth-anath, and Beth-shemesh — nineteen cities with their villages.",
      "M": "Iron, Migdal-el, Horem, Beth-anath, and Beth-shemesh — nineteen cities with their villages.",
      "T": "Iron, Migdal-el, Horem, Beth-anath, and Beth-shemesh — nineteen cities in all, with their villages."
    },
    "39": {
      "L": "This is the inheritance of the tribe of the children of Naphtali according to their families — the cities and their villages.",
      "M": "This is the inheritance of the tribe of the Naphtalites according to their families — these cities and their villages.",
      "T": "That is Naphtali's inheritance, assigned by clan — those towns and their surrounding villages."
    },
    "40": {
      "L": "The seventh lot came out for the tribe of the children of Dan according to their families.",
      "M": "The seventh lot came out for the tribe of the Danites according to their families.",
      "T": "The seventh and final lot fell to Dan, distributed among their clans."
    },
    "41": {
      "L": "And the territory of their inheritance was Zorah, Eshtaol, and Ir-shemesh,",
      "M": "Their allotted territory included Zorah, Eshtaol, and Ir-shemesh,",
      "T": "Their assigned towns included Zorah, Eshtaol, and Ir-shemesh —"
    },
    "42": {
      "L": "and Shaalabbin, Aijalon, and Ithlah,",
      "M": "Shaalabbin, Aijalon, and Ithlah,",
      "T": "Shaalabbin, Aijalon, and Ithlah,"
    },
    "43": {
      "L": "and Elon, Timnah, and Ekron,",
      "M": "Elon, Timnah, and Ekron,",
      "T": "Elon, Timnah, and Ekron,"
    },
    "44": {
      "L": "and Eltekeh, Gibbethon, and Baalath,",
      "M": "Eltekeh, Gibbethon, and Baalath,",
      "T": "Eltekeh, Gibbethon, and Baalath,"
    },
    "45": {
      "L": "and Jehud, Bene-berak, and Gath-rimmon,",
      "M": "Jehud, Bene-berak, and Gath-rimmon,",
      "T": "Jehud, Bene-berak, and Gath-rimmon,"
    },
    "46": {
      "L": "and Me-jarkon and Rakkon, with the territory opposite Joppa.",
      "M": "Me-jarkon and Rakkon, with the territory facing Joppa.",
      "T": "and Me-jarkon and Rakkon, with the coastal area across from Joppa."
    },
    "47": {
      "L": "But the territory of the children of Dan was lost to them. So the children of Dan went up and fought against Leshem, and took it and struck it with the edge of the sword. They took possession of it and settled in it, and called Leshem, Dan, after the name of Dan their father.",
      "M": "When the Danites failed to hold their allotted territory, they went up and attacked Leshem. They captured it, put it to the sword, took possession of it, and settled there, renaming it Dan after their ancestor.",
      "T": "Dan could not hold the territory they had been given — the Amorites pressed them back into the hills. So they went north, attacked the city of Leshem, and conquered it by the sword. They settled there and renamed it Dan after their ancestor — but the original allotment remained beyond their reach, a sign of the troubles ahead in Judges."
    },
    "48": {
      "L": "This is the inheritance of the tribe of the children of Dan according to their families — these cities with their villages.",
      "M": "This is the inheritance of the tribe of the Danites according to their families — these cities with their villages.",
      "T": "That is Dan's inheritance, assigned by clan — those towns with their surrounding villages."
    },
    "49": {
      "L": "When they had finished distributing the land for inheritance by its boundaries, the children of Israel gave an inheritance among themselves to Joshua the son of Nun.",
      "M": "When they had finished allotting the land according to its boundaries, the Israelites gave Joshua son of Nun an inheritance among them.",
      "T": "When all the tribal allotments had been settled boundary by boundary, the Israelites as a whole gave Joshua son of Nun his own share among them — last of all, after every tribe had received its portion."
    },
    "50": {
      "L": "According to the word of the LORD, they gave him the city he asked for — Timnath-serah in the hill country of Ephraim. And he built the city and settled in it.",
      "M": "At the LORD's command they gave him the city he requested: Timnath-serah in the hill country of Ephraim. He rebuilt the city and settled there.",
      "T": "Following the LORD's direction, they gave Joshua the city he had asked for — Timnath-serah in Ephraim's hill country. He rebuilt it from the ground up and made it his home: the leader who had received no land until last now settled in the highlands he had first scouted forty-five years before."
    },
    "51": {
      "L": "These are the inheritances which Eleazar the priest and Joshua the son of Nun and the heads of the fathers of the tribes of the children of Israel distributed by lot in Shiloh before the LORD, at the door of the tent of meeting. So they finished dividing the land.",
      "M": "These are the inheritances that Eleazar the priest, Joshua son of Nun, and the heads of the ancestral tribes of Israel assigned by lot at Shiloh before the LORD, at the entrance to the tent of meeting. And so the distribution of the land was complete.",
      "T": "These are all the allotments that Eleazar the priest and Joshua son of Nun and the tribal heads assigned by lot before the LORD at Shiloh, at the entrance to the tent of meeting. The land had been divided. The promise, from Genesis onward, had reached its geographical fulfilment."
    }
  },
  "20": {
    "1": {
      "L": "Then the LORD spoke to Joshua, saying,",
      "M": "The LORD said to Joshua:",
      "T": "The LORD spoke to Joshua:"
    },
    "2": {
      "L": "\"Speak to the children of Israel, saying, 'Designate for yourselves the cities of refuge, of which I spoke to you through Moses,",
      "M": "\"Tell the Israelites: 'Set apart for yourselves the cities of refuge that I commanded through Moses —",
      "T": "\"Say to the Israelites: 'Establish the cities of refuge I ordained through Moses —'"
    },
    "3": {
      "L": "'so that any manslayer who kills a person without intent or unknowingly may flee there. They shall be for you a refuge from the avenger of blood.",
      "M": "'so that anyone who kills a person accidentally or unintentionally may flee there for sanctuary from the blood avenger.",
      "T": "'so that anyone who takes a life by accident — unintentionally, without forethought or hatred — can flee to safety from the avenger of blood. The cities are Israel's provision for mercy in a world where blood cries out for blood.'"
    },
    "4": {
      "L": "'He shall flee to one of those cities, stand at the entrance of the city gate, and state his case in the hearing of the elders of that city. Then they shall take him into the city to themselves and give him a place that he may dwell among them.",
      "M": "'When the person flees to one of these cities and stops at the city gate, he must present his case to the elders of that city. They are to admit him into the city and give him a place to live among them.",
      "T": "'He is to present himself at the gate and state his case before the city elders. They must bring him inside, assign him lodging, and receive him as their own — the community standing between him and lethal vengeance while his case awaits full judgment.'"
    },
    "5": {
      "L": "'And if the avenger of blood pursues him, they shall not hand the slayer over into his hand, because he struck his neighbor without intent and without hating him beforehand.",
      "M": "'If the blood avenger pursues him, they must not surrender the accused, because he struck the person unintentionally and without prior malice.",
      "T": "'If the blood avenger comes in pursuit, the city must not surrender the fugitive — for he acted without premeditation, without hatred. The city's protection is the difference between justice and mob vengeance.'"
    },
    "6": {
      "L": "'He shall remain in that city until he stands before the congregation for judgment, until the death of the high priest who is in those days. Then the slayer may return and go to his own city and to his own house, to the city from which he fled.'\"",
      "M": "'He is to stay in that city until he has stood trial before the congregation, and until the death of the high priest who is serving at that time. After that, the manslayer may return to his own town and house, the one he fled from.'\"",
      "T": "'He stays there — protected — until the congregation adjudicates his case, and until the sitting high priest dies. The high priest's death functions as a kind of corporate atonement that releases the fugitive. Only then may he go home. This is how Israel keeps justice and mercy together.'"
    },
    "7": {
      "L": "So they set apart Kedesh in Galilee in the hill country of Naphtali, Shechem in the hill country of Ephraim, and Kiriath-arba — that is, Hebron — in the hill country of Judah.",
      "M": "So they designated Kedesh in Galilee in the hill country of Naphtali, Shechem in the hill country of Ephraim, and Kiriath-arba (that is, Hebron) in the hill country of Judah.",
      "T": "They set apart three cities west of the Jordan: Kedesh in Galilee among Naphtali's hills, Shechem in Ephraim's hill country, and Kiriath-arba — ancient Hebron — in the Judahite highlands."
    },
    "8": {
      "L": "And beyond the Jordan east of Jericho, they appointed Bezer in the wilderness on the plain from the tribe of Reuben, Ramoth in Gilead from the tribe of Gad, and Golan in Bashan from the tribe of Manasseh.",
      "M": "And east of the Jordan, across from Jericho, they appointed Bezer in the desert plateau from the tribe of Reuben, Ramoth in Gilead from the tribe of Gad, and Golan in Bashan from the tribe of Manasseh.",
      "T": "East of the Jordan — three more cities to mirror the three in the west: Bezer on the Reubenite plateau, Ramoth in Gilead for Gad, and Golan in Bashan for Manasseh. Six cities in all, accessible to every Israelite no matter where they lived."
    },
    "9": {
      "L": "These were the appointed cities for all the children of Israel, and for the alien sojourning among them, so that anyone who kills a person unintentionally might flee there and not die by the hand of the avenger of blood, until he stands before the congregation.",
      "M": "These were the designated cities for all the Israelites and for the foreigners living among them, so that anyone who accidentally killed someone could flee there and not be killed by the blood avenger before standing trial before the congregation.",
      "T": "These six cities were open to every Israelite and to every foreigner living among them. Accidental death need not trigger an endless cycle of reprisal. Israel was given institutions of mercy — a mark that the LORD's justice was not raw vengeance but ordered, restorable life."
    }
  },
  "21": {
    "1": {
      "L": "Then the heads of the fathers of the Levites came near to Eleazar the priest, and to Joshua the son of Nun, and to the heads of the fathers of the tribes of the children of Israel.",
      "M": "The heads of the Levitical families came to Eleazar the priest, to Joshua son of Nun, and to the heads of the ancestral tribes of Israel.",
      "T": "Now the Levitical clan heads came before Eleazar the priest, Joshua son of Nun, and the tribal leaders of Israel."
    },
    "2": {
      "L": "And they spoke to them at Shiloh in the land of Canaan, saying, 'The LORD commanded through Moses that we be given cities to dwell in, with their pasturelands for our livestock.'",
      "M": "At Shiloh in the land of Canaan, they said, 'The LORD commanded through Moses that we be given towns to live in, with their surrounding pasturelands for our livestock.'",
      "T": "Speaking at Shiloh in Canaan, they said: 'The LORD charged Moses that we Levites be given towns to settle in, with open land around them for our flocks and herds.'"
    },
    "3": {
      "L": "So the children of Israel gave to the Levites, out of their inheritance, by the command of the LORD, these cities and their pasturelands.",
      "M": "So the Israelites, obeying the LORD's command, gave the Levites these towns and their pasturelands from their own inheritance.",
      "T": "At the LORD's command, the Israelites gave the Levites towns and surrounding pasturelands from their own tribal portions."
    },
    "4": {
      "L": "And the lot came out for the families of the Kohathites. The children of Aaron the priest, who were of the Levites, received by lot thirteen cities from the tribe of Judah, the tribe of Simeon, and the tribe of Benjamin.",
      "M": "The first lot fell to the Kohathite families. The descendants of Aaron the priest, being Levites, received thirteen cities by lot from the tribes of Judah, Simeon, and Benjamin.",
      "T": "The first lot fell to the Kohathites. Aaron's priestly descendants received thirteen cities by lot from the tribes of Judah, Simeon, and Benjamin — settled in the south, near Jerusalem, where the priestly duties would one day be centred."
    },
    "5": {
      "L": "And the rest of the children of Kohath received by lot ten cities from the families of the tribe of Ephraim, from the tribe of Dan, and from the half-tribe of Manasseh.",
      "M": "The remaining Kohathite families received ten cities by lot from the tribes of Ephraim, Dan, and the half-tribe of Manasseh.",
      "T": "The other Kohathite families received ten cities by lot from Ephraim, Dan, and the western half of Manasseh."
    },
    "6": {
      "L": "And the children of Gershon received by lot thirteen cities from the families of the tribe of Issachar, from the tribe of Asher, from the tribe of Naphtali, and from the half-tribe of Manasseh in Bashan.",
      "M": "The Gershonites received thirteen cities by lot from the tribes of Issachar, Asher, Naphtali, and the half-tribe of Manasseh in Bashan.",
      "T": "The Gershonites received thirteen cities by lot from Issachar, Asher, Naphtali, and the eastern half of Manasseh in Bashan."
    },
    "7": {
      "L": "The children of Merari by their families received twelve cities from the tribe of Reuben, from the tribe of Gad, and from the tribe of Zebulun.",
      "M": "The Merarite families received twelve cities from the tribes of Reuben, Gad, and Zebulun.",
      "T": "The Merarites received twelve cities from Reuben, Gad, and Zebulun."
    },
    "8": {
      "L": "And the children of Israel gave to the Levites these cities with their pasturelands by lot, as the LORD had commanded through Moses.",
      "M": "The Israelites gave these cities with their pasturelands to the Levites by lot, just as the LORD had commanded through Moses.",
      "T": "The whole allocation was carried out by lot, exactly as the LORD had instructed through Moses. The Levites, who had received no tribal territory, were given homes distributed throughout the land — permanently embedded among all Israel."
    },
    "9": {
      "L": "Out of the tribe of the children of Judah and out of the tribe of the children of Simeon they gave these cities, which are here mentioned by name.",
      "M": "From the tribes of Judah and Simeon they gave the following cities, which are listed here by name.",
      "T": "From Judah and Simeon came the following cities, listed here by name:"
    },
    "10": {
      "L": "The children of Aaron, of the families of the Kohathites who were of the children of Levi, had the first lot, and they gave them:",
      "M": "The descendants of Aaron — Kohathite Levites — received the first lot:",
      "T": "Aaron's descendants — Kohathite Levites — drew the first lot and were given:"
    },
    "11": {
      "L": "Kiriath-arba — Arba being the father of Anak — that is, Hebron, in the hill country of Judah, with the pasturelands around it.",
      "M": "Kiriath-arba (that is, Hebron — Arba was the forefather of Anak) in the hill country of Judah, with its surrounding pasturelands.",
      "T": "Kiriath-arba — Hebron, city of the ancient giant Arba — in Judah's hill country, with open pastureland all around it."
    },
    "12": {
      "L": "But the fields of the city and its villages they gave to Caleb the son of Jephunneh as his possession.",
      "M": "But the fields and villages belonging to the city they gave to Caleb son of Jephunneh as his personal possession.",
      "T": "The surrounding farmlands and outlying villages, however, belonged to Caleb son of Jephunneh as his personal inheritance — the city and the countryside divided between priest and warrior."
    },
    "13": {
      "L": "And to the children of Aaron the priest they gave Hebron — a city of refuge for the manslayer — with its pasturelands; Libnah with its pasturelands,",
      "M": "To the priestly descendants of Aaron they gave Hebron — a city of refuge for the manslayer — with its pasturelands; and Libnah with its pasturelands,",
      "T": "To Aaron's priestly line: Hebron — a city of refuge for those who kill unintentionally — with open pastureland, and Libnah with its pastureland,"
    },
    "14": {
      "L": "Jattir with its pasturelands, Eshtemoa with its pasturelands,",
      "M": "Jattir with its pasturelands, Eshtemoa with its pasturelands,",
      "T": "Jattir with its pastureland, Eshtemoa with its pastureland,"
    },
    "15": {
      "L": "Holon with its pasturelands, Debir with its pasturelands,",
      "M": "Holon with its pasturelands, Debir with its pasturelands,",
      "T": "Holon with its pastureland, Debir with its pastureland,"
    },
    "16": {
      "L": "Ain with its pasturelands, Juttah with its pasturelands, and Beth-shemesh with its pasturelands — nine cities from those two tribes.",
      "M": "Ain with its pasturelands, Juttah with its pasturelands, and Beth-shemesh with its pasturelands — nine cities from those two tribes.",
      "T": "Ain with its pastureland, Juttah with its pastureland, and Beth-shemesh with its pastureland — nine cities drawn from Judah and Simeon."
    },
    "17": {
      "L": "And from the tribe of Benjamin: Gibeon with its pasturelands, Geba with its pasturelands,",
      "M": "From the tribe of Benjamin: Gibeon with its pasturelands, Geba with its pasturelands,",
      "T": "From Benjamin: Gibeon with its pastureland, Geba with its pastureland,"
    },
    "18": {
      "L": "Anathoth with its pasturelands, and Almon with its pasturelands — four cities.",
      "M": "Anathoth with its pasturelands, and Almon with its pasturelands — four cities.",
      "T": "Anathoth with its pastureland, and Almon with its pastureland — four cities."
    },
    "19": {
      "L": "All the cities of the children of Aaron, the priests, were thirteen cities with their pasturelands.",
      "M": "All the cities of the priestly line of Aaron came to thirteen, with their surrounding pasturelands.",
      "T": "In total, the Aaronic priests received thirteen cities with open pastureland — housed throughout the south, close to the heartland of Israel's future worship."
    },
    "20": {
      "L": "And the families of the children of Kohath — the Levites remaining of the children of Kohath — had their allotted cities from the tribe of Ephraim.",
      "M": "The rest of the Kohathite Levites — those families not descended from Aaron — received their cities from the tribe of Ephraim.",
      "T": "The remaining Kohathite families — those not of Aaron's priestly line — received their cities from Ephraim:"
    },
    "21": {
      "L": "They gave them Shechem — a city of refuge for the manslayer — with its pasturelands in the hill country of Ephraim; and Gezer with its pasturelands,",
      "M": "They gave them Shechem — a city of refuge — with its pasturelands in the hill country of Ephraim, and Gezer with its pasturelands,",
      "T": "Shechem — another city of refuge for the unintentional killer — in Ephraim's hill country, with pastureland, and Gezer with its pastureland,"
    },
    "22": {
      "L": "Kibzaim with its pasturelands, and Beth-horon with its pasturelands — four cities.",
      "M": "Kibzaim with its pasturelands, and Beth-horon with its pasturelands — four cities.",
      "T": "Kibzaim with its pastureland, and Beth-horon with its pastureland — four cities."
    },
    "23": {
      "L": "And from the tribe of Dan: Eltekeh with its pasturelands, Gibbethon with its pasturelands,",
      "M": "From the tribe of Dan: Eltekeh with its pasturelands, Gibbethon with its pasturelands,",
      "T": "From Dan: Eltekeh with its pastureland, Gibbethon with its pastureland,"
    },
    "24": {
      "L": "Aijalon with its pasturelands, Gath-rimmon with its pasturelands — four cities.",
      "M": "Aijalon with its pasturelands, Gath-rimmon with its pasturelands — four cities.",
      "T": "Aijalon with its pastureland, Gath-rimmon with its pastureland — four cities."
    },
    "25": {
      "L": "And from the half-tribe of Manasseh: Taanach with its pasturelands, and Gath-rimmon with its pasturelands — two cities.",
      "M": "From the half-tribe of Manasseh: Taanach with its pasturelands, and Gath-rimmon with its pasturelands — two cities.",
      "T": "From the western half of Manasseh: Taanach with its pastureland, and Gath-rimmon with its pastureland — two cities."
    },
    "26": {
      "L": "All the cities for the remaining families of the children of Kohath were ten cities with their pasturelands.",
      "M": "All the cities of the remaining Kohathite families came to ten with their pasturelands.",
      "T": "The non-Aaronic Kohathites received ten cities in total with their pastureland."
    },
    "27": {
      "L": "And to the children of Gershon, of the Levitical families, from the other half-tribe of Manasseh: Golan in Bashan — a city of refuge for the manslayer — with its pasturelands; and Beeshterah with its pasturelands — two cities.",
      "M": "To the Gershonite Levites, from the other half-tribe of Manasseh: Golan in Bashan — a city of refuge — with its pasturelands; and Beeshterah with its pasturelands — two cities.",
      "T": "To the Gershonites, from the eastern half of Manasseh: Golan in Bashan — a city of refuge — with its pastureland, and Beeshterah with its pastureland — two cities."
    },
    "28": {
      "L": "And from the tribe of Issachar: Kishon with its pasturelands, Daberath with its pasturelands,",
      "M": "From the tribe of Issachar: Kishon with its pasturelands, Daberath with its pasturelands,",
      "T": "From Issachar: Kishon with its pastureland, Daberath with its pastureland,"
    },
    "29": {
      "L": "Jarmuth with its pasturelands, En-gannim with its pasturelands — four cities.",
      "M": "Jarmuth with its pasturelands, En-gannim with its pasturelands — four cities.",
      "T": "Jarmuth with its pastureland, En-gannim with its pastureland — four cities."
    },
    "30": {
      "L": "And from the tribe of Asher: Mishal with its pasturelands, Abdon with its pasturelands,",
      "M": "From the tribe of Asher: Mishal with its pasturelands, Abdon with its pasturelands,",
      "T": "From Asher: Mishal with its pastureland, Abdon with its pastureland,"
    },
    "31": {
      "L": "Helkath with its pasturelands, and Rehob with its pasturelands — four cities.",
      "M": "Helkath with its pasturelands, and Rehob with its pasturelands — four cities.",
      "T": "Helkath with its pastureland, and Rehob with its pastureland — four cities."
    },
    "32": {
      "L": "And from the tribe of Naphtali: Kedesh in Galilee — a city of refuge for the manslayer — with its pasturelands; Hammoth-dor with its pasturelands, and Kartan with its pasturelands — three cities.",
      "M": "From the tribe of Naphtali: Kedesh in Galilee — a city of refuge — with its pasturelands; Hammoth-dor with its pasturelands, and Kartan with its pasturelands — three cities.",
      "T": "From Naphtali: Kedesh in Galilee — another city of refuge for the accidental killer — with its pastureland, Hammoth-dor with its pastureland, and Kartan with its pastureland — three cities."
    },
    "33": {
      "L": "All the cities of the Gershonites according to their families were thirteen cities with their pasturelands.",
      "M": "All the cities of the Gershonites by their families came to thirteen with their pasturelands.",
      "T": "The Gershonites received thirteen cities in total with their pastureland."
    },
    "34": {
      "L": "And to the families of the children of Merari — the remaining Levites — from the tribe of Zebulun: Jokneam with its pasturelands, and Kartah with its pasturelands,",
      "M": "To the Merarite Levites, the remaining families, from the tribe of Zebulun: Jokneam with its pasturelands, and Kartah with its pasturelands,",
      "T": "To the Merarites — the last of the Levitical families — from Zebulun: Jokneam with its pastureland, and Kartah with its pastureland,"
    },
    "35": {
      "L": "Dimnah with its pasturelands, and Nahalal with its pasturelands — four cities.",
      "M": "Dimnah with its pasturelands, and Nahalal with its pasturelands — four cities.",
      "T": "Dimnah with its pastureland, and Nahalal with its pastureland — four cities."
    },
    "36": {
      "L": "And from the tribe of Reuben: Bezer with its pasturelands, Jahaz with its pasturelands,",
      "M": "From the tribe of Reuben: Bezer with its pasturelands, Jahaz with its pasturelands,",
      "T": "From Reuben: Bezer with its pastureland, Jahaz with its pastureland,"
    },
    "37": {
      "L": "Kedemoth with its pasturelands, and Mephaath with its pasturelands — four cities.",
      "M": "Kedemoth with its pasturelands, and Mephaath with its pasturelands — four cities.",
      "T": "Kedemoth with its pastureland, and Mephaath with its pastureland — four cities."
    },
    "38": {
      "L": "And from the tribe of Gad: Ramoth in Gilead — a city of refuge for the manslayer — with its pasturelands; Mahanaim with its pasturelands,",
      "M": "From the tribe of Gad: Ramoth in Gilead — a city of refuge — with its pasturelands; Mahanaim with its pasturelands,",
      "T": "From Gad: Ramoth in Gilead — a city of refuge — with its pastureland, and Mahanaim with its pastureland,"
    },
    "39": {
      "L": "Heshbon with its pasturelands, and Jazer with its pasturelands — four cities.",
      "M": "Heshbon with its pasturelands, and Jazer with its pasturelands — four cities.",
      "T": "Heshbon with its pastureland, and Jazer with its pastureland — four cities."
    },
    "40": {
      "L": "All the cities of the children of Merari by their families — those remaining of the Levitical families — were twelve cities.",
      "M": "All the cities assigned to the Merarites, the remaining Levitical families, by their lots, came to twelve cities.",
      "T": "The Merarites received twelve cities in all — the last allocation, completing the Levitical distribution."
    },
    "41": {
      "L": "All the cities of the Levites within the possession of the children of Israel were forty-eight cities with their pasturelands.",
      "M": "The total number of Levitical cities within the Israelite territory was forty-eight cities with their pasturelands.",
      "T": "In all, forty-eight cities with their surrounding pasturelands were set aside for the Levites within Israel's territories — one tribe distributed among all the others, as the LORD had ordained through Moses."
    },
    "42": {
      "L": "Each of these cities had its pasturelands surrounding it. So it was with all these cities.",
      "M": "Every one of these cities had its own surrounding pasturelands; it was the same for all these cities.",
      "T": "Every single one of these forty-eight cities had open common land around it for livestock — the same provision for each. The Levites had no tribal territory, but they had a home everywhere."
    },
    "43": {
      "L": "And the LORD gave to Israel all the land that he swore to give to their fathers. And they took possession of it and settled in it.",
      "M": "So the LORD gave Israel all the land he had sworn to give their ancestors. They took possession of it and settled there.",
      "T": "The LORD gave Israel every part of the land he had sworn to their ancestors. They took possession of it and lived in it."
    },
    "44": {
      "L": "And the LORD gave them rest all around, just as he had sworn to their fathers. And not one of all their enemies had withstood them, for the LORD had given all their enemies into their hands.",
      "M": "The LORD gave them rest on every side, just as he had sworn to their ancestors. Not one of all their enemies had withstood them, for the LORD had given all their enemies into their hands.",
      "T": "The LORD gave them rest — unbroken, complete — on every side. Not one enemy stood firm before them. Every foe fell into Israel's hand, because the LORD fought for them. What he swore, he kept."
    },
    "45": {
      "L": "Not one word of all the good words that the LORD had spoken to the house of Israel failed. All came to pass.",
      "M": "Not a single word of all the good things the LORD had promised to the house of Israel went unfulfilled. Everything came true.",
      "T": "Not one word. Not one promise. Every good thing the LORD had spoken to Israel came to pass without exception. The land, the rest, the victory, the Levitical cities, the cities of refuge — all of it. Genesis 12 had promised a land, a people, a blessing. Joshua 21 is the answer."
    }
  },
  "22": {
    "1": {
      "L": "Then Joshua called together the Reubenites and the Gadites and the half-tribe of Manasseh",
      "M": "Then Joshua summoned the Reubenites, the Gadites, and the half-tribe of Manasseh",
      "T": "Joshua summoned the Reubenites, the Gadites, and the half-tribe of Manasseh —"
    },
    "2": {
      "L": "and said to them: \"You have kept all that Moses the servant of the LORD commanded you, and you have obeyed my voice in all that I commanded you.",
      "M": "and said to them: \"You have done everything Moses the servant of the LORD commanded you, and you have obeyed my voice in everything I commanded you.",
      "T": "and addressed them: \"You have kept every command Moses the LORD's servant laid on you. Every order I gave, you obeyed."
    },
    "3": {
      "L": "You have not abandoned your brothers these many days — to this very day — but have kept the charge of the commandment of the LORD your God.",
      "M": "All this time — these many days right up to today — you have not deserted your fellow Israelites but have faithfully kept the charge the LORD your God gave you.",
      "T": "You have not abandoned your brothers — not in all these years of fighting — but held to the LORD's charge without fail."
    },
    "4": {
      "L": "And now the LORD your God has given rest to your brothers, as he promised them. Therefore now, turn and go to your tents, to the land of your possession that Moses the servant of the LORD gave you beyond the Jordan.",
      "M": "Now the LORD your God has granted your fellow Israelites the rest he promised. So now, go back to your tents, to the land that Moses the LORD's servant gave you on the other side of the Jordan.",
      "T": "Now the LORD your God has settled your brothers in the rest he promised them. The war is over. Go home — back to your tents, to the land east of the Jordan that Moses gave you."
    },
    "5": {
      "L": "Only take great care to do the commandment and the law that Moses the servant of the LORD commanded you: to love the LORD your God, to walk in all his ways, to keep his commandments, to cling to him, and to serve him with all your heart and with all your soul.\"",
      "M": "But be very careful to observe the commandment and the law that Moses the LORD's servant gave you: to love the LORD your God, to walk in all his ways, to keep his commands, to hold fast to him, and to serve him with all your heart and all your soul.\"",
      "T": "Only — take this with you: be diligent, deeply careful, to live by the commandment and Torah Moses gave you. Love the LORD your God. Walk in all his ways. Keep his commands. Hold fast to him. Serve him with your whole heart and your whole self. This is the Shema lived out. Do not let distance make you forget.\""
    },
    "6": {
      "L": "So Joshua blessed them and sent them away, and they went to their tents.",
      "M": "Then Joshua blessed them and sent them on their way, and they went to their tents.",
      "T": "Joshua gave them his blessing and released them, and they set out for home."
    },
    "7": {
      "L": "Now to the one half of the tribe of Manasseh Moses had given a possession in Bashan, but to the other half Joshua had given a possession among their brothers on the west side of the Jordan. And when Joshua sent them away to their tents and blessed them,",
      "M": "Moses had given the eastern half of the tribe of Manasseh their territory in Bashan, but Joshua had given the western half a share among their brothers on the west side of the Jordan. When Joshua sent them away to their homes and blessed them,",
      "T": "Half of Manasseh had received their land in Bashan from Moses; the other half Joshua had settled west of the Jordan among their brothers. As Joshua dismissed the eastern half and blessed them,"
    },
    "8": {
      "L": "he said to them, \"Return to your tents with great wealth and with very large herds, with silver, gold, bronze, iron, and very much clothing. Divide the spoil of your enemies with your brothers.\"",
      "M": "he said: \"Return to your homes with great wealth — large herds, silver, gold, bronze, iron, and abundant clothing. Share the plunder of your enemies with your fellow Israelites.\"",
      "T": "he told them: \"Take home great wealth — abundant flocks, silver and gold, bronze and iron, clothing in abundance. Divide the enemy's spoil generously with the brothers you fought alongside.\""
    },
    "9": {
      "L": "So the children of Reuben and the children of Gad and the half-tribe of Manasseh departed and went from the children of Israel at Shiloh, which is in the land of Canaan, to go to the land of Gilead — to the land of their possession, which they had taken according to the word of the LORD through Moses.",
      "M": "So the Reubenites, Gadites, and half-tribe of Manasseh left the Israelites at Shiloh in Canaan and set out for the land of Gilead — the territory that was their own, which they had acquired according to the LORD's command through Moses.",
      "T": "The Reubenites, Gadites, and half-tribe of Manasseh left their brothers at Shiloh in Canaan and headed for Gilead — the land they had earned by their service, granted them as the LORD had commanded through Moses."
    },
    "10": {
      "L": "And when they came to the region of the Jordan that is in the land of Canaan, the children of Reuben and the children of Gad and the half-tribe of Manasseh built there an altar by the Jordan — an imposing altar in appearance.",
      "M": "When they reached the region near the Jordan that is still in the land of Canaan, the Reubenites, Gadites, and half-tribe of Manasseh built an altar there by the Jordan — a very large altar.",
      "T": "When they reached the Jordan on the Canaan side, before crossing over, the Reubenites, Gadites, and half-tribe of Manasseh built a large, prominent altar by the river — conspicuous, impossible to miss."
    },
    "11": {
      "L": "And the children of Israel heard it said, \"Behold, the children of Reuben and the children of Gad and the half-tribe of Manasseh have built an altar at the frontier of the land of Canaan, in the region of the Jordan, on the side belonging to the children of Israel.\"",
      "M": "The Israelites received the report: \"The Reubenites, Gadites, and half-tribe of Manasseh have built an altar at the entrance to the land of Canaan, in the region of the Jordan, on the Israelite side.\"",
      "T": "Word reached the rest of Israel: \"The Reubenites, Gadites, and half-tribe of Manasseh have built an altar at the border of Canaan — right at the Jordan, on our side of the river.\""
    },
    "12": {
      "L": "When the children of Israel heard it, the whole congregation of the children of Israel gathered at Shiloh to go up to war against them.",
      "M": "When the Israelites heard this, the entire Israelite community assembled at Shiloh and prepared to go to war against them.",
      "T": "The response was swift and alarmed. The whole Israelite community assembled at Shiloh, ready to march to war. An altar built outside the sanctioned worship site looked like a second center of religion — apostasy in stone."
    },
    "13": {
      "L": "Then the children of Israel sent to the children of Reuben and to the children of Gad and to the half-tribe of Manasseh in the land of Gilead — Phinehas the son of Eleazar the priest,",
      "M": "But first the Israelites sent a delegation to Reuben, Gad, and the half-tribe of Manasseh in Gilead: Phinehas son of Eleazar the priest,",
      "T": "But before attacking, Israel sent an embassy to Gilead — Phinehas son of Eleazar the priest leading the delegation —"
    },
    "14": {
      "L": "and with him ten princes — one prince from each tribal house of all the tribes of Israel — each one the head of his father's house among the clans of Israel.",
      "M": "and with him ten leaders — one from each tribe of Israel, every one a head of his tribal clan.",
      "T": "with ten senior leaders, one from every tribe — men of real authority, representing all Israel."
    },
    "15": {
      "L": "They came to the children of Reuben and to the children of Gad and to the half-tribe of Manasseh in the land of Gilead and spoke with them, saying,",
      "M": "They went to the Reubenites, Gadites, and half-tribe of Manasseh in Gilead and said to them:",
      "T": "They arrived in Gilead and laid the charge before the eastern tribes:"
    },
    "16": {
      "L": "\"Thus says the whole congregation of the LORD: What is this treachery that you have committed against the God of Israel, turning away today from following the LORD by building yourselves an altar, to rebel against the LORD this day?",
      "M": "\"This is what the whole community of the LORD says: How could you commit this treachery against the God of Israel by turning away from the LORD and building yourselves an altar — rebelling against him today?",
      "T": "\"The entire assembly of the LORD sends this charge: What is this betrayal against Israel's God? You have turned away from the LORD by building yourselves an altar — as if in defiance of him today."
    },
    "17": {
      "L": "Is the iniquity of Peor too little for us — from which we have not cleansed ourselves to this day — and for which a plague came upon the congregation of the LORD?",
      "M": "Was the sin of Peor not enough? We have still not fully cleansed ourselves of it, and it brought a plague on the LORD's community!",
      "T": "Have we already forgotten Peor? That sin clung to us; the plague it brought has barely faded from memory. Are you bringing another Peor upon us?"
    },
    "18": {
      "L": "And now you too are turning away from the LORD! If you rebel against the LORD today, he will be angry with the whole congregation of Israel tomorrow.",
      "M": "And now you are turning away from the LORD! If you rebel against the LORD today, tomorrow he will be angry with the entire community of Israel.",
      "T": "And now you are turning away from the LORD! If you rebel today, his anger will fall on all of Israel tomorrow — not just you. That is how it works: one community's sin, everyone's judgment."
    },
    "19": {
      "L": "But if the land of your possession is unclean, cross over into the land of the LORD's possession where the LORD's tabernacle stands, and take your possession among us. Only do not rebel against the LORD or against us by building yourselves an altar other than the altar of the LORD our God.",
      "M": "If the land you possess is somehow unclean, then cross over into the land where the LORD's tabernacle stands and take your share among us. But do not rebel against the LORD or against us by building an altar other than the altar of the LORD our God.",
      "T": "If you feel cut off — if the east bank feels spiritually outside the LORD's presence — then come over. Cross the Jordan and settle among us in the land of the LORD's tabernacle. We will make room for you. But do not erect a rival altar. There is only one place, one worship, one people before the LORD."
    },
    "20": {
      "L": "Was it not Achan the son of Zerah who acted treacherously in the matter of the devoted things, and wrath fell on all the congregation of Israel? And he was not the only one who perished for his iniquity.\"",
      "M": "Remember Achan son of Zerah — he acted treacherously in the matter of the devoted things, and the LORD's anger fell on all Israel. He was not the only one who died for that sin.\"",
      "T": "Remember Achan son of Zerah. His private act of treachery in the matter of the devoted goods brought the LORD's wrath down on the whole congregation. He was not alone in dying for it — thirty-six men fell at Ai. One man's sin; all Israel bleeds. This altar carries the same risk.\""
    },
    "21": {
      "L": "Then the children of Reuben and the children of Gad and the half-tribe of Manasseh answered and said to the heads of the clans of Israel:",
      "M": "Then the Reubenites, Gadites, and half-tribe of Manasseh answered the heads of the Israelite clans:",
      "T": "The eastern tribes answered the Israelite leaders directly and solemnly:"
    },
    "22": {
      "L": "\"El, God, the LORD! El, God, the LORD! He knows! And let Israel itself know! If it was in rebellion or in treachery against the LORD, do not spare us this day.",
      "M": "\"The Mighty One, God, the LORD! The Mighty One, God, the LORD! He knows this, and let Israel know! If this was rebellion or treachery against the LORD, do not spare us today.",
      "T": "\"El, God, the LORD — El, God, the LORD! He himself is our witness. The triple name is our oath. Let all Israel hear: if we built this altar in rebellion or in treachery against the LORD, then do not spare us."
    },
    "23": {
      "L": "If we have built ourselves an altar to turn away from following the LORD, or if we did so to offer burnt offerings or grain offerings on it, or to offer peace offerings on it, let the LORD himself require it.",
      "M": "If we built it to turn away from the LORD, or to offer burnt offerings, grain offerings, or fellowship offerings on it — may the LORD himself call us to account.",
      "T": "If we built this altar to worship elsewhere — to offer sacrifices apart from the tabernacle — let the LORD deal with us. We invoke him as our judge."
    },
    "24": {
      "L": "But truly we did this out of concern, for a reason, saying: In time to come your children might say to our children, 'What have you to do with the LORD, the God of Israel?",
      "M": "But in fact we did this out of anxiety, for a specific reason: we were afraid that in the future your children might say to our children, 'What do you have to do with the LORD, the God of Israel?",
      "T": "But here is the truth. We acted out of fear — a real fear. We thought: someday your descendants will say to our descendants, 'You have no part in the LORD, the God of Israel.'"
    },
    "25": {
      "L": "For the LORD has made the Jordan a boundary between us and you, you children of Reuben and children of Gad. You have no portion in the LORD.' And so your children might cause our children to stop fearing the LORD.",
      "M": "For the LORD has made the Jordan a boundary between us and you Reubenites and Gadites — you have no share in the LORD.' So your descendants might lead ours to stop worshipping the LORD.",
      "T": "The Jordan would become a theological wall. 'The LORD's land is over there,' they'd say. 'You're on the outside.' And our children would gradually drift from the LORD, told they do not belong."
    },
    "26": {
      "L": "So we said: Let us now build an altar, not for burnt offering and not for sacrifice,",
      "M": "That is why we said: Let us build an altar — but not for burnt offerings or sacrifices.",
      "T": "So we said: build an altar — not as a place of worship, but as a statement of identity."
    },
    "27": {
      "L": "but to be a witness between us and you and our generations after us, that we do perform the service of the LORD before him with our burnt offerings, our sacrifices, and our peace offerings — so that your children may not say to our children in time to come: 'You have no portion in the LORD.'",
      "M": "It is to be a witness between us and you and the generations that come after us — that we will serve the LORD before him with our burnt offerings, sacrifices, and fellowship offerings. Then your descendants cannot say to ours: 'You have no share in the LORD.'",
      "T": "A witness — standing in stone between us and you and every generation to come. When anyone says 'the eastern tribes have no part in the LORD,' this altar says: we serve him. We always have. We always will. It is not a competing sanctuary; it is a monument to our common belonging."
    },
    "28": {
      "L": "Therefore we said: If they say this to us or to our generations in time to come, we will say: 'Look at the replica of the altar of the LORD, which our fathers made — not for burnt offering, nor for sacrifice, but it is a witness between us and you.'",
      "M": "So we thought: if they ever make this accusation against us or our descendants, we can answer: 'Look at the copy of the LORD's altar that our ancestors built — not for burnt offerings or sacrifices, but as a witness between us and you.'",
      "T": "If the accusation ever comes — in our day or our children's day — we point to this: 'See this altar? It is a replica. Not a rival. Our ancestors built it not for sacrifice but as a declaration: we belong to the LORD alongside you.'"
    },
    "29": {
      "L": "Far be it from us that we should rebel against the LORD and turn away today from following the LORD by building an altar for burnt offering, grain offering, or sacrifice besides the altar of the LORD our God that stands before his tabernacle!\"",
      "M": "Far be it from us to rebel against the LORD or to turn away from him today by building an altar for burnt offerings, grain offerings, or sacrifices — other than the altar of the LORD our God that stands before his tabernacle!\"",
      "T": "God forbid that we would rebel. God forbid that we would build a second worship center to rival the LORD's altar at the tabernacle. We are not splitting Israel. We are declaring ourselves bound to it.\""
    },
    "30": {
      "L": "When Phinehas the priest and the leaders of the congregation — the heads of the clans of Israel who were with him — heard the words that the children of Reuben and Gad and Manasseh spoke, it pleased them.",
      "M": "When Phinehas the priest and the leaders of the community — the heads of the Israelite clans with him — heard what the Reubenites, Gadites, and Manassites said, they were satisfied.",
      "T": "When Phinehas and the delegation heard the eastern tribes' explanation, they were convinced and relieved."
    },
    "31": {
      "L": "And Phinehas the son of Eleazar the priest said to the children of Reuben and the children of Gad and the children of Manasseh, 'Today we know that the LORD is in our midst, because you have not committed this treachery against the LORD. You have now delivered the children of Israel from the hand of the LORD.'",
      "M": "Phinehas son of Eleazar said to the Reubenites, Gadites, and Manassites, 'Today we know that the LORD is among us, because you have not been unfaithful to him. You have rescued the Israelites from the LORD's judgment.'",
      "T": "Phinehas spoke: 'Now we know the LORD is still in our midst — because you did not betray him. You have spared Israel from the LORD's hand. There will be no judgment, no war. We go home at peace.'"
    },
    "32": {
      "L": "And Phinehas the son of Eleazar the priest and the leaders returned from the children of Reuben and the children of Gad out of the land of Gilead to the land of Canaan, to the children of Israel, and brought back word to them.",
      "M": "Then Phinehas son of Eleazar and the leaders returned from Gilead to the land of Canaan and brought back word to the Israelites.",
      "T": "Phinehas and the leaders made the journey back from Gilead to Canaan and reported everything to the Israelites."
    },
    "33": {
      "L": "And the report was good in the eyes of the children of Israel. And the children of Israel blessed God and did not speak of going up against them in war, to destroy the land where the children of Reuben and Gad settled.",
      "M": "The report pleased the Israelites, and they praised God. They spoke no more about going to war against the Reubenites and Gadites or about destroying the land where they had settled.",
      "T": "The report brought relief. Israel praised God and dropped all talk of war. The crisis that might have torn the nation apart was resolved by a delegation, a conversation, and a willingness to hear the other side before attacking."
    },
    "34": {
      "L": "And the children of Reuben and the children of Gad called the altar Ed — for, they said, \"It is a witness between us that the LORD is God.\"",
      "M": "The Reubenites and Gadites named the altar Ed — \"Witness\" — saying, \"It is a witness between us that the LORD is God.\"",
      "T": "The Reubenites and Gadites named the altar 'Ed' — Witness. 'This altar stands as testimony between us,' they said, 'that the LORD is God.' A name carved in the stone of conflict, testifying to a unity barely preserved."
    }
  },
  "23": {
    "1": {
      "L": "A long time afterward, when the LORD had given rest to Israel from all their surrounding enemies, and Joshua was old and advanced in years,",
      "M": "After a long time, when the LORD had given Israel rest from all their surrounding enemies and Joshua was old and getting on in years,",
      "T": "A long time passed. The LORD had given Israel complete rest from all surrounding enemies. Joshua was very old now — and he knew the time had come to speak."
    },
    "2": {
      "L": "Joshua called all Israel — its elders and heads, its judges and officers — and said to them: \"I am old and advanced in years.",
      "M": "Joshua summoned all Israel — its elders, leaders, judges, and officers — and said to them: \"I am now old and very advanced in years.",
      "T": "He summoned all Israel — elders, leaders, judges, officers — and said: \"I am old. The years have piled up on me."
    },
    "3": {
      "L": "And you yourselves have seen all that the LORD your God has done to all these nations before you, for it is the LORD your God who has fought for you.",
      "M": "You yourselves have seen everything the LORD your God has done to all these nations for your sake — it was the LORD your God who fought for you.",
      "T": "You have seen it all with your own eyes — what the LORD your God has done to every nation he drove out before you. He fought for you. Every victory was his."
    },
    "4": {
      "L": "Behold, I have allotted to you as an inheritance for your tribes these nations that remain, along with all the nations I have already cut off, from the Jordan to the Great Sea toward the setting of the sun.",
      "M": "See, I have allotted to your tribes as an inheritance the remaining nations — along with all the nations I have already wiped out — from the Jordan to the Mediterranean Sea in the west.",
      "T": "Look at the land: I have assigned to your tribes what remains — both the nations already cut off and those still lingering — from the Jordan all the way west to the Mediterranean."
    },
    "5": {
      "L": "The LORD your God will push them back before you and drive them out of your sight. And you shall possess their land, just as the LORD your God promised you.",
      "M": "The LORD your God himself will push them back and drive them away from you. You will take possession of their land, just as the LORD your God promised you.",
      "T": "The LORD your God will push them back before you and drive them from your sight. You will possess their land — just as the LORD promised. Not by your strength; by his fidelity to his word."
    },
    "6": {
      "L": "Therefore be very strong to keep and to do all that is written in the Book of the Law of Moses, turning aside from it neither to the right nor to the left,",
      "M": "Be very strong in keeping and doing everything written in the Book of the Law of Moses, without turning aside from it to the right or to the left,",
      "T": "Therefore be deeply courageous — courageous enough to keep and obey everything written in the Book of the Torah of Moses. Do not swerve from it in any direction."
    },
    "7": {
      "L": "so that you may not mix with these nations remaining among you, nor make mention of the names of their gods, nor swear by them, nor serve them, nor bow down to them,",
      "M": "so that you will not associate with these nations that remain among you, invoke the names of their gods, swear by them, serve them, or bow down to them.",
      "T": "Do not mix with the nations still living among you. Do not invoke the names of their gods. Do not swear oaths by them, serve them, or bow to them. The danger is not violence but assimilation."
    },
    "8": {
      "L": "but you shall cling to the LORD your God, as you have done to this day.",
      "M": "Instead, hold fast to the LORD your God, as you have done to this day.",
      "T": "Cling to the LORD your God instead — the way you have, to your credit, done up to today."
    },
    "9": {
      "L": "For the LORD has driven out before you great and strong nations. As for you, no man has been able to stand against you to this day.",
      "M": "The LORD has driven out great and powerful nations before you. To this day no one has been able to withstand you.",
      "T": "The LORD has displaced great and powerful nations before you. No one has been able to stand against you — not to this day."
    },
    "10": {
      "L": "One man of you puts a thousand to flight, for the LORD your God is he who fights for you, as he promised you.",
      "M": "One of you can rout a thousand, because the LORD your God fights for you, just as he promised.",
      "T": "One of you can route a thousand — not because Israel is exceptional but because the LORD your God does the fighting. He said he would. He has."
    },
    "11": {
      "L": "Take great care therefore for your souls, to love the LORD your God.",
      "M": "So be very careful in your hearts to love the LORD your God.",
      "T": "Watch your hearts — this is the single thing that matters: love the LORD your God."
    },
    "12": {
      "L": "For if you turn back and cling to the remnant of these nations remaining among you, and intermarry with them, going into them and they into you,",
      "M": "But if you turn away and ally yourselves with the nations left among you, intermarrying with them and they with you,",
      "T": "But if you turn back — if you cling to whatever remnants of these nations remain and intermarry with them —"
    },
    "13": {
      "L": "know for certain that the LORD your God will no longer drive out these nations before you. They shall be a snare and a trap for you, a whip on your sides and thorns in your eyes, until you perish from off this good land that the LORD your God has given you.",
      "M": "then know with certainty that the LORD your God will no longer drive out these nations before you. Instead, they will be snares and traps for you, whips on your backs and thorns in your eyes, until you perish from this good land the LORD your God has given you.",
      "T": "— know this for certain: the LORD your God will drive no more nations out before you. The remaining peoples will become traps for your feet, snares around your neck, whips on your sides, and thorns in your eyes — until you are swept off this good land. The promise has a reverse side: the land can be lost."
    },
    "14": {
      "L": "\"And now I am going the way of all the earth. You know in your hearts and souls — all of you — that not one word has failed of all the good words that the LORD your God spoke concerning you. All have come to pass for you; not one word has failed.",
      "M": "\"Now I am about to go the way of all the earth. You know with all your heart and soul that not one of all the good promises the LORD your God made to you has failed. Every one has been fulfilled — not one has failed.",
      "T": "\"I am walking the road every person walks — the way of all the earth. I will not be here much longer. But hear this before I go: you know in your heart of hearts, every one of you, that not a single good promise the LORD your God gave you has gone unmet. All of it came true. Every word."
    },
    "15": {
      "L": "But just as all the good words that the LORD your God spoke to you have come upon you, so the LORD will bring upon you all the evil things, until he has destroyed you from off this good land that the LORD your God has given you.",
      "M": "But just as every good thing the LORD your God promised you has come upon you, so he will also bring upon you every evil he has threatened, until he destroys you from this good land the LORD has given you.",
      "T": "But the same LORD who kept every good promise is also bound to keep every warning. If you break faith, the evil he promised will come as surely as the good did. He will drive you from this land."
    },
    "16": {
      "L": "If you transgress the covenant of the LORD your God, which he commanded you, and go and serve other gods and bow down to them, then the anger of the LORD will be kindled against you, and you will perish quickly from off this good land that he has given you.\"",
      "M": "If you violate the covenant of the LORD your God — which he commanded you — and go and worship other gods and bow down to them, the LORD's anger will burn against you, and you will quickly perish from this good land he has given you.\"",
      "T": "The trigger is this: transgress the covenant. Go and serve other gods, bow to them — and the LORD's anger will ignite. You will not linger in the land. You will lose it quickly. The good land is a gift held by covenant faithfulness, not by right of possession.\""
    }
  },
  "24": {
    "1": {
      "L": "And Joshua gathered all the tribes of Israel to Shechem and called for the elders of Israel and for its heads and for its judges and for its officers. And they presented themselves before God.",
      "M": "Joshua assembled all the tribes of Israel at Shechem and summoned the elders, leaders, judges, and officers of Israel. They presented themselves before God.",
      "T": "Joshua gathered all Israel to Shechem — the place where Abraham first built an altar in Canaan, where Jacob buried the foreign gods under the oak, where Israel has always stood at turning points. The elders, leaders, judges, and officers assembled. They stood before God."
    },
    "2": {
      "L": "And Joshua said to all the people: \"Thus says the LORD, the God of Israel: 'Long ago your fathers lived beyond the River — Terah, the father of Abraham and the father of Nahor — and they served other gods.",
      "M": "Joshua said to all the people: \"This is what the LORD, the God of Israel, says: 'Long ago your ancestors — Terah, the father of Abraham and Nahor — lived beyond the Euphrates River and worshipped other gods.",
      "T": "Joshua addressed the whole assembly with the LORD's own words: \"This is what the LORD, Israel's God, says: 'Long before any of you, your ancestors — Terah, father of Abraham and Nahor — lived east of the great Euphrates. And they worshipped other gods. Your story begins in idolatry.'"
    },
    "3": {
      "L": "'Then I took your father Abraham from beyond the River and led him through all the land of Canaan, and multiplied his offspring. I gave him Isaac.",
      "M": "'But I took your ancestor Abraham from beyond the Euphrates, led him through all of Canaan, and gave him many descendants. I gave him Isaac.",
      "T": "'But I took Abraham — I went to him in that distant land and brought him out. I led him through every part of Canaan. I multiplied his descendants. I gave him Isaac.'"
    },
    "4": {
      "L": "'And to Isaac I gave Jacob and Esau. To Esau I gave the hill country of Seir to possess. But Jacob and his children went down to Egypt.",
      "M": "'To Isaac I gave Jacob and Esau. I gave the hill country of Seir to Esau as his possession, but Jacob and his family went down to Egypt.",
      "T": "'To Isaac I gave Jacob and Esau. Esau got the hills of Seir. Jacob went another way — down into Egypt with all his children. I was present in all of it.'"
    },
    "5": {
      "L": "'Then I sent Moses and Aaron and I plagued Egypt according to what I did in its midst. And afterward I brought you out.",
      "M": "'Then I sent Moses and Aaron, and I struck Egypt with plagues — everything I did there. And afterward I brought you out.",
      "T": "'I sent Moses and Aaron. I broke Egypt with plagues. And then I brought you out — not you by your own strength, but you by my outstretched hand.'"
    },
    "6": {
      "L": "'I brought your fathers out of Egypt, and you came to the sea. And the Egyptians pursued your fathers with chariots and horsemen to the Red Sea.",
      "M": "'I brought your ancestors out of Egypt, and you came to the sea. The Egyptians pursued them with chariots and cavalry to the Red Sea.",
      "T": "'I brought your ancestors out of Egypt. You came to the sea — and Pharaoh's chariot corps and cavalry chased you all the way to the Red Sea.'"
    },
    "7": {
      "L": "'And when they cried to the LORD, he put darkness between you and the Egyptians and brought the sea upon them and covered them. And your eyes saw what I did in Egypt. And you lived in the wilderness a long time.",
      "M": "'When they cried out to the LORD, he put darkness between you and the Egyptians. He brought the sea over them and covered them. Your eyes saw what I did in Egypt. Then you lived in the wilderness for a long time.",
      "T": "'They cried to me. I put darkness between you and Egypt, and I brought the sea down on them. They were swallowed. Your own ancestors saw it with their eyes — what I did. And then came the wilderness, the long years of formation.'"
    },
    "8": {
      "L": "'Then I brought you to the land of the Amorites who lived beyond the Jordan. They fought against you, and I gave them into your hand. You possessed their land and I destroyed them before you.",
      "M": "'I brought you to the land of the Amorites east of the Jordan. They fought against you, and I gave them into your hands. You took possession of their land and I destroyed them before you.",
      "T": "'I brought you to Amorite territory east of the Jordan. They fought you — and I handed them to you. You took their land. I destroyed them before you. Notice who is the actor in every clause.'"
    },
    "9": {
      "L": "'Then Balak the son of Zippor, king of Moab, arose and fought against Israel. And he sent and called for Balaam the son of Beor to curse you.",
      "M": "'Then Balak son of Zippor, the king of Moab, prepared to fight against Israel. He sent for Balaam son of Beor to put a curse on you.",
      "T": "'Balak king of Moab then marshaled his forces and hired the famous prophet Balaam son of Beor to curse you and break your momentum.'"
    },
    "10": {
      "L": "'But I was not willing to listen to Balaam. Therefore he blessed you continually. And I delivered you from his hand.",
      "M": "'But I would not listen to Balaam. Instead, he blessed you again and again. So I rescued you from his power.",
      "T": "'I refused to hear Balaam's curse. Every attempt came out as blessing. I overruled him. I delivered you from that threat without you firing a single arrow.'"
    },
    "11": {
      "L": "'And you crossed over the Jordan and came to Jericho. And the leaders of Jericho fought against you — the Amorites, the Perizzites, the Canaanites, the Hittites, the Girgashites, the Hivites, and the Jebusites — and I gave them into your hand.",
      "M": "'You crossed the Jordan and came to Jericho. The people of Jericho fought against you — the Amorites, Perizzites, Canaanites, Hittites, Girgashites, Hivites, and Jebusites — and I gave them into your hand.",
      "T": "'You crossed the Jordan and arrived at Jericho. Coalition upon coalition of Canaanite peoples came out against you — seven peoples in the list — and I gave every one of them into your hand.'"
    },
    "12": {
      "L": "'And I sent the hornet before you, which drove out before you the two kings of the Amorites — not by your sword or by your bow.",
      "M": "'I sent the hornet ahead of you, which drove out the two Amorite kings before you — not by your sword or bow.",
      "T": "'I sent the hornet before you — a divine terror that broke the Amorite kings before you arrived. Not by your sword. Not by your bow. You did not win this land; I gave it.'"
    },
    "13": {
      "L": "'I gave you a land on which you had not labored and cities that you had not built, and you dwell in them. You eat from vineyards and olive groves that you did not plant.'",
      "M": "'I gave you a land you did not work for and cities you did not build — you live in them. You eat from vineyards and olive groves you did not plant.'",
      "T": "'You are eating from vines you did not plant, living in cities you did not build, working soil you did not clear. Every meal in this land is a grace. Remember that.'"
    },
    "14": {
      "L": "\"Now therefore fear the LORD and serve him in wholeness and in truth. Put away the gods that your fathers served beyond the River and in Egypt, and serve the LORD.",
      "M": "\"Now therefore fear the LORD and serve him with complete sincerity and faithfulness. Throw away the gods your ancestors worshipped beyond the Euphrates and in Egypt, and serve the LORD.",
      "T": "\"Now — in light of all of that — fear the LORD. Serve him in integrity and genuine fidelity. Clear out the household gods your ancestors carried from Mesopotamia and Egypt. Serve the LORD alone."
    },
    "15": {
      "L": "And if it is evil in your eyes to serve the LORD, choose this day whom you will serve — whether the gods your fathers served beyond the River, or the gods of the Amorites in whose land you dwell. But as for me and my house, we will serve the LORD.\"",
      "M": "But if you are unwilling to serve the LORD, then choose today whom you will serve — the gods your ancestors served beyond the Euphrates, or the gods of the Amorites in whose land you now live. But as for me and my household, we will serve the LORD.\"",
      "T": "And if serving the LORD feels like too much — if you are not ready to commit — then choose. Choose openly: the gods of Mesopotamia, the gods of Canaan around you? Pick one. But I have already chosen. My house has chosen. We will serve the LORD.\""
    },
    "16": {
      "L": "And the people answered and said: \"Far be it from us to forsake the LORD to serve other gods!",
      "M": "The people replied: \"Far be it from us to forsake the LORD and serve other gods!",
      "T": "The people answered: \"We would never forsake the LORD to serve other gods!"
    },
    "17": {
      "L": "For it is the LORD our God who brought us and our fathers up from the land of Egypt, from the house of slavery, and who did those great signs before our eyes and guarded us in all the way that we went and among all the peoples through whom we passed.",
      "M": "For the LORD our God brought us and our ancestors up from Egypt, out of the land of slavery. He performed those great signs before our eyes and protected us all along the way and among all the peoples we passed through.",
      "T": "It is the LORD our God who brought us and our ancestors up from Egypt — from slavery. We saw the great signs with our own eyes. He protected us every step of the way, through every nation we passed through."
    },
    "18": {
      "L": "And the LORD drove out before us all the peoples, even the Amorites who dwelt in the land. Therefore we also will serve the LORD, for he is our God.\"",
      "M": "The LORD drove out before us all the nations, including the Amorites who lived in this land. So we too will serve the LORD, because he is our God.\"",
      "T": "The LORD drove out all the peoples — the Amorites and every other nation — from before us. Therefore we will serve the LORD. He is our God. The people spoke with apparent sincerity — three times over they would commit (vv. 16-18, 21, 24).\""
    },
    "19": {
      "L": "But Joshua said to the people: \"You are not able to serve the LORD, for he is a holy God. He is a jealous God. He will not forgive your transgressions or your sins.",
      "M": "Joshua said to the people: \"You are not able to serve the LORD. He is a holy God; he is a jealous God. He will not forgive your rebellion and your sins.",
      "T": "But Joshua stopped them with a word they did not expect: \"You cannot serve the LORD. Not like this. Not in your own strength, not with this quick enthusiasm. He is a holy God — utterly set apart, terrifyingly pure. He is fiercely loyal and will not share his people with any other. He does not overlook rebellion or dismiss sin."
    },
    "20": {
      "L": "If you forsake the LORD and serve foreign gods, he will turn and do you harm and destroy you after he has done you good.\"",
      "M": "If you forsake the LORD and serve foreign gods, he will turn and bring disaster on you and destroy you, even after he has been good to you.\"",
      "T": "If you forsake him for foreign gods, he will turn against you. All the good he has done for you will become the measure of the harm he brings. He is not indifferent to betrayal. I am not trying to discourage you — I am making sure you know what you are committing to.\""
    },
    "21": {
      "L": "And the people said to Joshua: \"No — we will serve the LORD.\"",
      "M": "But the people said to Joshua: \"No! We will serve the LORD.\"",
      "T": "The people would not be deterred: \"No — we mean it. We will serve the LORD.\""
    },
    "22": {
      "L": "Then Joshua said to the people: \"You are witnesses against yourselves that you have chosen the LORD, to serve him.\" And they said: \"We are witnesses.\"",
      "M": "Then Joshua declared: \"You are witnesses against yourselves that you have chosen the LORD — to serve him.\" \"We are witnesses,\" they replied.",
      "T": "Joshua pressed it to the formal conclusion: \"You have heard yourselves. You are your own witnesses — you have chosen the LORD, to serve him.\" \"We are witnesses,\" they said. The covenant is made in the most unbreakable form: sworn before God with themselves as witness."
    },
    "23": {
      "L": "\"Now then, put away the foreign gods that are among you, and incline your hearts to the LORD, the God of Israel.\"",
      "M": "\"Now then,\" he said, \"throw away the foreign gods that are among you and turn your hearts fully to the LORD, the God of Israel.\"",
      "T": "\"Then act on it,\" Joshua said. \"Get rid of the foreign gods still hiding among you. Turn your hearts all the way toward the LORD, the God of Israel. Words are not enough; the idols must go.\""
    },
    "24": {
      "L": "And the people said to Joshua: \"The LORD our God we will serve, and his voice we will obey.\"",
      "M": "The people answered Joshua: \"We will serve the LORD our God and obey his voice.\"",
      "T": "The people made their final, complete commitment: \"The LORD our God — him we will serve. His voice — we will obey it.\" Two promises: worship and obedience. The whole of covenant life."
    },
    "25": {
      "L": "So Joshua made a covenant with the people that day, and set for them a statute and an ordinance at Shechem.",
      "M": "On that day Joshua made a covenant with the people and drew up for them a binding rule and regulation at Shechem.",
      "T": "Joshua formalized it that same day — a covenant, with a statute and a binding ordinance, made at Shechem. This is the second covenant-making at Shechem; the land had been received; now the allegiance is sworn."
    },
    "26": {
      "L": "And Joshua wrote these words in the Book of the Law of God. And he took a large stone and set it up there under the oak that was by the sanctuary of the LORD.",
      "M": "Joshua recorded these things in the Book of the Law of God. Then he took a large stone and set it up under the oak near the sanctuary of the LORD.",
      "T": "Joshua wrote the covenant into the Book of the Law of God, and then took a great stone and set it upright under the oak at the LORD's sanctuary at Shechem — the same tree near which Jacob once buried the foreign gods. The stone would outlast the witnesses."
    },
    "27": {
      "L": "And Joshua said to all the people: \"Behold, this stone shall be a witness against us, for it has heard all the words of the LORD that he spoke to us. And it shall be a witness against you, lest you deal falsely with your God.\"",
      "M": "Joshua said to all the people: \"See — this stone will be a witness against us. It has heard all the words the LORD spoke to us today. It will be a witness against you if you are ever false to your God.\"",
      "T": "Joshua told the assembly: \"This stone has ears. It has heard every word the LORD spoke today, every word you spoke in reply. Creation stands as covenant witness — as it does in the song of Moses, as it will in the prophets. If you break faith with your God, this stone testifies against you.\""
    },
    "28": {
      "L": "So Joshua sent the people away, each to his own inheritance.",
      "M": "Then Joshua dismissed the people, each to their own inheritance.",
      "T": "Joshua released the people, sending each family back to its own land. The covenant was sealed."
    },
    "29": {
      "L": "After these things Joshua the son of Nun, the servant of the LORD, died, being one hundred and ten years old.",
      "M": "After all this, Joshua son of Nun, the servant of the LORD, died at the age of a hundred and ten.",
      "T": "After these events, Joshua son of Nun, the servant of the LORD, died at one hundred and ten years old. He had earned Moses' title: the servant of the LORD."
    },
    "30": {
      "L": "And they buried him in the boundary of his inheritance at Timnath-serah, which is in the hill country of Ephraim, north of the mountain of Gaash.",
      "M": "They buried him in the territory he had inherited — at Timnath-serah in the hill country of Ephraim, north of Mount Gaash.",
      "T": "He was buried at Timnath-serah in the Ephraimite hills — the city he had asked for last, after all others had received theirs. He was laid to rest in the land he had given his life to secure."
    },
    "31": {
      "L": "And Israel served the LORD all the days of Joshua and all the days of the elders who outlived Joshua and who had known all the work that the LORD did for Israel.",
      "M": "Israel served the LORD throughout Joshua's lifetime and throughout the lifetime of the elders who outlived him — those who had personally witnessed all that the LORD had done for Israel.",
      "T": "All the days Joshua lived, Israel served the LORD. And still after his death, the elders who had lived through the conquest — who remembered what they had seen with their own eyes — kept Israel on course. The faithfulness of a generation can carry the next one, for a time."
    },
    "32": {
      "L": "And the bones of Joseph, which the children of Israel had brought up from Egypt, they buried at Shechem, in the piece of ground that Jacob bought from the sons of Hamor the father of Shechem for one hundred pieces of silver. And it became an inheritance for the children of Joseph.",
      "M": "The bones of Joseph, which the Israelites had brought from Egypt, were buried at Shechem in the plot of ground Jacob had bought from the sons of Hamor, the father of Shechem, for a hundred pieces of silver. This became the inheritance of Joseph's descendants.",
      "T": "And at Shechem, they buried the bones of Joseph. Brought from Egypt by Moses (Exod 13:19), carried through forty years of wilderness, crossed through the Jordan — Joseph had asked for this (Gen 50:25), Jacob had sworn to it. Now the bones came to rest in the only piece of Canaanite soil the patriarchs had ever legally owned — the field Jacob bought from Hamor's sons. Promise kept across four hundred years."
    },
    "33": {
      "L": "And Eleazar the son of Aaron died, and they buried him at Gibeah of Phinehas his son, which had been given to him in the hill country of Ephraim.",
      "M": "Eleazar son of Aaron also died, and was buried at Gibeah, which had been given to his son Phinehas in the hill country of Ephraim.",
      "T": "Eleazar son of Aaron died and was buried at Gibeah — a hill in Ephraim given to his son Phinehas. Three burials close the book: Joshua the leader, Joseph the patriarch, Eleazar the priest. The generation of deliverance rests in the promised land. The door of Joshua closes; the door of Judges opens."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'joshua')
        merge_tier(existing, JOSHUA, tier_key)
        save(tier_dir, 'joshua', existing)
    print('Joshua 19–24 written.')

if __name__ == '__main__':
    main()
