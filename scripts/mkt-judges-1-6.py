"""
MKT Judges chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-judges-1-6.py

Covers: the incomplete conquest after Joshua's death and tribal failures (ch. 1); the angel
of the LORD at Bochim and the apostasy-cycle framework (ch. 2); Othniel, Ehud, and Shamgar
as the first judges (ch. 3); Deborah and Barak vs. Sisera; Jael kills Sisera (ch. 4);
the Song of Deborah — one of the oldest Hebrew poems (ch. 5); Midianite oppression, Gideon's
call, the angel of the LORD at the winepress, the terebinth theophany, Gideon tears down
Baal's altar and receives the name Jerubbaal, the fleece tests (ch. 6).

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) L/M; "the LORD" T — consistent with
  all prior OT scripts (Genesis through Joshua and Judges 7-12)
- H430 (אֱלֹהִים): "God" all tiers when divine; "gods" when plural/pagan
- H4397 (מַלְאָךְ יהוה): "angel of the LORD" all tiers; in 2:1-4 and 6:11-22 this is a
  theophanic appearance (the angel speaks in the first person as Yahweh); T surfaces
  the identity ambiguity explicitly at 6:22 where Gideon "perceives" the angel's true
  nature — the text intends the reader to recognize a divine encounter
- H7307 (רוּחַ): "Spirit of the LORD" (capitalized) in 3:10 (Othniel) and 6:34 (Gideon) —
  standard formula for charismatic military anointing; in 6:34 Hebrew לָבַשׁ רוּחַ (the
  Spirit "clothed" Gideon) is a vivid garment metaphor; T renders "wrapped itself around"
- H8199 (שָׁפַט): "judged" L; "judged/governed" M; "led as judge" T — in Deborah's case
  (4:4-5) she genuinely adjudicated disputes, unlike warrior judges; T notes distinction
- H5031 (נְבִיאָה): "prophetess" all tiers — Deborah is the only judge explicitly called
  a prophet; T foregrounds her dual role (prophet + judge)
- H2181 (זָנָה): "went a-whoring" L; "committed spiritual adultery" M; T uses "chased
  after" with explicit note about covenant infidelity — consistent with Judges 7-12
- H1168 (בַּעַל/בְּעָלִים): "the Baals" or "Baal" per context; in 6:25-32 Baal's altar at
  Ophrah; T notes the irony of Israel tolerating a local Baal shrine in Manassite territory
- H842 (אֲשֵׁרָה): "Asherah pole" L/M; "the Asherah pole" T — the carved wooden cult
  object associated with the Canaanite goddess; not to be confused with Ashteroth
- H1285 (בְּרִית): "covenant" all tiers — in 2:1-2 the angel recites the covenant terms
  Israel has violated; T draws out the legal/oath-bound character
- H2617 (חֶסֶד): in 1:24 "kindness" L; "loyalty" M; "covenant loyalty" T — the spies'
  promise to the informant carries the weight of a binding commitment
- H5315 (נֶפֶשׁ): not prominent in chs. 1-6
- H3847+H7307 (לָבַשׁ רוּחַ) in 6:34: "the Spirit of the LORD came upon" L; "the Spirit
  of the LORD clothed Gideon" M; T: "the Spirit of the LORD wrapped itself around Gideon"
  — the Hebrew garment metaphor (רוּחַ as clothing) is theologically significant; it
  implies that Gideon was not generating his own courage but was enveloped by divine power
- Ch. 5 (Song of Deborah): T tier rendered with poetic line structure throughout —
  this is one of the oldest texts in the Hebrew Bible (ca. 12th c. BCE); its archaic
  vocabulary, tribal roll call, and victory hymn form demand cadence; L and M rendered
  as prose with approximate line breaks noted; T uses full strophic line divisions
- H8337+H3967 (שֵׁשׁ מֵאוֹת) in 3:31: Shamgar kills 600 Philistines with an oxgoad —
  the briefest judge account; T preserves the stark economy of the original
- Adoni-bezek (1:7): the lex talionis speech is notable — a pagan king acknowledges
  divine justice; T surfaces this as theological testimony from an unexpected witness
- Jael (4:17-22; 5:24-27): T notes that Jael's act is celebrated in the Song as
  divinely blessed; the ethical complexity (hospitality violated) is left unresolved by
  the text and T does not impose resolution
- Ch. 2:16-19 (apostasy cycle framework): T makes explicit the structural pattern —
  sin, oppression, cry, deliverance, apostasy again — that governs the entire book
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

JUDGES = {
  "1": {
    "1": {
      "L": "And it came to pass after the death of Joshua, that the children of Israel asked the LORD, saying, Who shall go up for us against the Canaanites first, to fight against them?",
      "M": "After the death of Joshua, the people of Israel inquired of the LORD, \"Who shall go up first for us against the Canaanites, to fight against them?\"",
      "T": "After Joshua died, Israel sought the LORD's guidance: \"Which tribe should lead our attack against the Canaanites?\""
    },
    "2": {
      "L": "And the LORD said, Judah shall go up: behold, I have delivered the land into his hand.",
      "M": "The LORD said, \"Judah shall go up; I have given the land into his hand.\"",
      "T": "The LORD answered: \"Let Judah go first. I have already given the land into their hand.\""
    },
    "3": {
      "L": "And Judah said unto Simeon his brother, Come up with me into my lot, that we may fight against the Canaanites; and I likewise will go with thee into thy lot. So Simeon went with him.",
      "M": "And Judah said to Simeon his brother, \"Come up with me into my allotted territory, that we may fight against the Canaanites; and I likewise will go with you into your allotted territory.\" So Simeon went with him.",
      "T": "Judah invited the tribe of Simeon: \"Come and fight alongside us in our territory, and we will do the same for yours.\" Simeon agreed and joined them."
    },
    "4": {
      "L": "And Judah went up; and the LORD delivered the Canaanites and the Perizzites into their hand: and they slew of them in Bezek ten thousand men.",
      "M": "So Judah went up, and the LORD gave the Canaanites and the Perizzites into their hand, and they struck down ten thousand men at Bezek.",
      "T": "Judah marched out, and the LORD gave the Canaanites and Perizzites into their hands. They killed ten thousand men at Bezek."
    },
    "5": {
      "L": "And they found Adonibezek in Bezek: and they fought against him, and they slew the Canaanites and the Perizzites.",
      "M": "They found Adoni-bezek at Bezek, and fought against him, and defeated the Canaanites and the Perizzites.",
      "T": "There they encountered Adoni-bezek and defeated him along with his Canaanite and Perizzite forces."
    },
    "6": {
      "L": "But Adonibezek fled; and they pursued after him, and caught him, and cut off his thumbs and his great toes.",
      "M": "But Adoni-bezek fled, and they pursued him and caught him and cut off his thumbs and his big toes.",
      "T": "Adoni-bezek fled, but they caught him and cut off his thumbs and big toes."
    },
    "7": {
      "L": "And Adonibezek said, Threescore and ten kings, having their thumbs and their great toes cut off, gathered their meat under my table: as I have done, so God hath requited me. And they brought him to Jerusalem, and there he died.",
      "M": "And Adoni-bezek said, \"Seventy kings with their thumbs and big toes cut off used to pick up scraps under my table. As I have done, so God has repaid me.\" And they brought him to Jerusalem, and he died there.",
      "T": "Adoni-bezek said, \"I have done this to seventy kings—made them grovel under my table for scraps. Now God has given me exactly what I dealt out.\" They took him to Jerusalem, where he died. Even a pagan king recognized the justice."
    },
    "8": {
      "L": "Now the children of Judah had fought against Jerusalem, and had taken it, and smitten it with the edge of the sword, and set the city on fire.",
      "M": "And the men of Judah fought against Jerusalem and captured it and struck it with the edge of the sword and set the city on fire.",
      "T": "The men of Judah then attacked Jerusalem, captured it, put its people to the sword, and burned the city."
    },
    "9": {
      "L": "And afterward the children of Judah went down to fight against the Canaanites, that dwelt in the mountain, and in the south, and in the valley.",
      "M": "And afterward the men of Judah went down to fight against the Canaanites who lived in the hill country, in the Negeb, and in the lowland.",
      "T": "After that they pushed on to fight the Canaanites in the highlands, the Negeb, and the western foothills."
    },
    "10": {
      "L": "And Judah went against the Canaanites that dwelt in Hebron: (now the name of Hebron before was Kirjatharba:) and they slew Sheshai, and Ahiman, and Talmai.",
      "M": "And Judah went against the Canaanites who lived in Hebron—the former name of Hebron was Kiriath-arba—and they defeated Sheshai, Ahiman, and Talmai.",
      "T": "Judah turned against Hebron—once called Kiriath-arba—and defeated the three Anakim clans there: Sheshai, Ahiman, and Talmai."
    },
    "11": {
      "L": "And from thence he went against the inhabitants of Debir: and the name of Debir before was Kirjathsepher.",
      "M": "From there he went against the inhabitants of Debir. The former name of Debir was Kiriath-sepher.",
      "T": "From Hebron they advanced on Debir—formerly known as Kiriath-sepher, the City of the Scroll."
    },
    "12": {
      "L": "And Caleb said, He that smiteth Kirjathsepher, and taketh it, to him will I give Achsah my daughter to wife.",
      "M": "And Caleb said, \"Whoever attacks Kiriath-sepher and captures it, I will give him Achsah my daughter as wife.\"",
      "T": "Caleb offered an incentive: \"Whoever takes Kiriath-sepher gets my daughter Achsah as his wife.\""
    },
    "13": {
      "L": "And Othniel the son of Kenaz, Caleb's younger brother, took it: and he gave him Achsah his daughter to wife.",
      "M": "And Othniel the son of Kenaz, Caleb's younger brother, captured it. And Caleb gave him Achsah his daughter as wife.",
      "T": "Othniel son of Kenaz—Caleb's younger brother—took the city. Caleb gave him Achsah as his wife."
    },
    "14": {
      "L": "And it came to pass, when she came to him, that she moved him to ask of her father a field: and she lighted from off her ass; and Caleb said unto her, What wilt thou?",
      "M": "When she came to him, she urged him to ask her father for a field. She dismounted from her donkey, and Caleb said to her, \"What do you want?\"",
      "T": "When Achsah arrived, she persuaded Othniel to ask her father for farmland. She got down from her donkey, and Caleb asked her, \"What do you want?\""
    },
    "15": {
      "L": "And she said unto him, Give me a blessing: for thou hast given me a south land; give me also springs of water. And Caleb gave her the upper springs and the nether springs.",
      "M": "She said to him, \"Give me a gift; since you have set me in the land of the Negeb, give me also springs of water.\" And Caleb gave her the upper springs and the lower springs.",
      "T": "She said, \"You gave me dry land in the Negeb—now give me water too.\" Caleb granted her both the upper and lower springs."
    },
    "16": {
      "L": "And the children of the Kenite, Moses' father in law, went up out of the city of palm trees with the children of Judah into the wilderness of Judah, which lieth in the south of Arad; and they went and dwelt among the people.",
      "M": "And the descendants of the Kenite, Moses' father-in-law, went up with the people of Judah from the city of palms into the wilderness of Judah, which lies in the Negeb near Arad. And they went and settled with the people.",
      "T": "The Kenites—descendants of Moses' father-in-law—traveled from Jericho with the tribe of Judah into the Judean wilderness near Arad and settled among them."
    },
    "17": {
      "L": "And Judah went with Simeon his brother, and they slew the Canaanites that inhabited Zephath, and utterly destroyed it. And the name of the city was called Hormah.",
      "M": "Then Judah went with Simeon his brother, and they defeated the Canaanites who inhabited Zephath and devoted it to destruction. So the name of the city was called Hormah.",
      "T": "Judah and Simeon together struck the Canaanites of Zephath and completely destroyed it. That is why the place was renamed Hormah—\"Destruction.\""
    },
    "18": {
      "L": "Also Judah took Gaza with the coast thereof, and Askelon with the coast thereof, and Ekron with the coast thereof.",
      "M": "Judah also captured Gaza with its territory, Ashkelon with its territory, and Ekron with its territory.",
      "T": "Judah also took the coastal cities: Gaza, Ashkelon, and Ekron, each with its surrounding villages."
    },
    "19": {
      "L": "And the LORD was with Judah; and he drave out the inhabitants of the mountain; but could not drive out the inhabitants of the valley, because they had chariots of iron.",
      "M": "And the LORD was with Judah, and he took possession of the hill country, but he could not drive out the inhabitants of the plain because they had chariots of iron.",
      "T": "The LORD was with Judah in the highlands, and they took the hill country. But the coastal plain was beyond them—the Canaanites there had iron chariots."
    },
    "20": {
      "L": "And they gave Hebron unto Caleb, as Moses said: and he expelled thence the three sons of Anak.",
      "M": "And Hebron was given to Caleb, as Moses had said. And he drove out from it the three sons of Anak.",
      "T": "Hebron was given to Caleb, as Moses had promised. He drove out the three Anakim clans from the city."
    },
    "21": {
      "L": "And the children of Benjamin did not drive out the Jebusites that inhabited Jerusalem; but the Jebusites dwell with the children of Benjamin in Jerusalem unto this day.",
      "M": "But the people of Benjamin did not drive out the Jebusites who lived in Jerusalem, so the Jebusites have lived with the people of Benjamin in Jerusalem to this day.",
      "T": "Benjamin failed to expel the Jebusites from Jerusalem. So the Jebusites lived on in the city alongside the Benjaminites—and were still there when this account was written."
    },
    "22": {
      "L": "And the house of Joseph, they also went up against Bethel: and the LORD was with them.",
      "M": "The house of Joseph also went up against Bethel, and the LORD was with them.",
      "T": "The tribes of Joseph—Ephraim and Manasseh—moved against Bethel, and the LORD was with them."
    },
    "23": {
      "L": "And the house of Joseph sent to descry Bethel. (Now the name of the city before was Luz.)",
      "M": "And the house of Joseph sent men to scout out Bethel. (The name of the city was formerly Luz.)",
      "T": "They sent scouts ahead to Bethel—the old Canaanite name of the city was Luz."
    },
    "24": {
      "L": "And the spies saw a man come forth out of the city, and they said unto him, Shew us, we pray thee, the entrance into the city, and we will shew thee mercy.",
      "M": "And the spies saw a man coming out of the city, and they said to him, \"Please show us the way into the city, and we will deal loyally with you.\"",
      "T": "The scouts spotted a man leaving the city and said to him, \"Show us how to get in, and we will treat you with covenant loyalty.\""
    },
    "25": {
      "L": "And when he shewed them the entrance into the city, they smote the city with the edge of the sword; but they let go the man and all his family.",
      "M": "And he showed them the way into the city. They struck the city with the edge of the sword, but let the man and all his family go.",
      "T": "He led them in. They put the city to the sword but kept their word—the informant and his whole family were spared."
    },
    "26": {
      "L": "And the man went into the land of the Hittites, and built a city, and called the name thereof Luz: which is the name thereof unto this day.",
      "M": "But the man went to the land of the Hittites and built a city and called its name Luz. That is its name to this day.",
      "T": "The man traveled north into Hittite territory and built a new city there, naming it Luz after the old one—and that name endures to this day."
    },
    "27": {
      "L": "Neither did Manasseh drive out the inhabitants of Bethshean and her towns, nor Taanach and her towns, nor the inhabitants of Dor and her towns, nor the inhabitants of Ibleam and her towns, nor the inhabitants of Megiddo and her towns: but the Canaanites would dwell in that land.",
      "M": "Manasseh did not drive out the inhabitants of Beth-shean and its villages, Taanach and its villages, the inhabitants of Dor and its villages, the inhabitants of Ibleam and its villages, or the inhabitants of Megiddo and its villages, for the Canaanites were determined to dwell in that land.",
      "T": "Manasseh failed to clear the major cities of the Jezreel Valley: Beth-shean, Taanach, Dor, Ibleam, Megiddo—all with their surrounding villages. The Canaanites held their ground."
    },
    "28": {
      "L": "And it came to pass, when Israel was strong, that they put the Canaanites to tribute, and did not utterly drive them out.",
      "M": "When Israel grew strong, they put the Canaanites to forced labor, but did not drive them out completely.",
      "T": "When Israel grew powerful enough, they pressed the Canaanites into forced labor—but never drove them out. Compromise replaced obedience."
    },
    "29": {
      "L": "Neither did Ephraim drive out the Canaanites that dwelt in Gezer; but the Canaanites dwelt in Gezer among them.",
      "M": "And Ephraim did not drive out the Canaanites who lived in Gezer, so the Canaanites lived in Gezer among them.",
      "T": "Ephraim left the Canaanites of Gezer in place. They lived on, mixed in with Israel."
    },
    "30": {
      "L": "Neither did Zebulun drive out the inhabitants of Kitron, nor the inhabitants of Nahalol; but the Canaanites dwelt among them, and became tributaries.",
      "M": "Zebulun did not drive out the inhabitants of Kitron or the inhabitants of Nahalol, so the Canaanites lived among them and became subject to forced labor.",
      "T": "Zebulun left Kitron and Nahalol unconquered. The Canaanites stayed on and eventually became forced laborers."
    },
    "31": {
      "L": "Neither did Asher drive out the inhabitants of Accho, nor the inhabitants of Zidon, nor of Ahlab, nor of Achzib, nor of Helbah, nor of Aphik, nor of Rehob:",
      "M": "Asher did not drive out the inhabitants of Acco, or of Sidon, or of Ahlab, or of Achzib, or of Helbah, or of Aphik, or of Rehob.",
      "T": "Asher failed completely along the northern coast: Acco, Sidon, Ahlab, Achzib, Helbah, Aphik, Rehob—all left in Canaanite hands."
    },
    "32": {
      "L": "But the Asherites dwelt among the Canaanites, the inhabitants of the land: for they did not drive them out.",
      "M": "So the Asherites lived among the Canaanites, the inhabitants of the land, for they did not drive them out.",
      "T": "Instead of Asher possessing the land, the Canaanites swallowed Asher. The tribe never drove them out."
    },
    "33": {
      "L": "Neither did Naphtali drive out the inhabitants of Bethshemesh, nor the inhabitants of Bethanath; but he dwelt among the Canaanites, the inhabitants of the land: nevertheless the inhabitants of Bethshemesh and of Bethanath became tributaries unto them.",
      "M": "Naphtali did not drive out the inhabitants of Beth-shemesh or the inhabitants of Beth-anath, so he lived among the Canaanites, the inhabitants of the land. Nevertheless, the inhabitants of Beth-shemesh and Beth-anath became forced laborers for them.",
      "T": "Naphtali likewise left Beth-shemesh and Beth-anath unconquered and settled among the Canaanites. In time they extracted forced labor from those cities, but never expelled them."
    },
    "34": {
      "L": "And the Amorites forced the children of Dan into the mountain: for they would not suffer them to come down to the valley:",
      "M": "The Amorites pressed the people of Dan back into the hill country and would not allow them to come down to the plain.",
      "T": "Dan fared worst of all—the Amorites pushed them back into the hills and refused to let them down into the valleys."
    },
    "35": {
      "L": "But the Amorites would dwell in mount Heres in Aijalon, and in Shaalbim: yet the hand of the house of Joseph prevailed, so that they became tributaries.",
      "M": "The Amorites persisted in dwelling on Mount Heres, in Aijalon, and in Shaalbim, but when the hand of the house of Joseph grew heavy against them, they became subject to forced labor.",
      "T": "The Amorites held Mount Heres, Aijalon, and Shaalbim. Only when Ephraim's power bore down on them did they submit to labor—they were never expelled."
    },
    "36": {
      "L": "And the coast of the Amorites was from the going up to Akrabbim, from the rock, and upward.",
      "M": "And the territory of the Amorites ran from the ascent of Akrabbim, from the rock and upward.",
      "T": "The Amorites held all the territory from the Scorpion Pass northward—a substantial stretch of the land Israel never took."
    }
  },
  "2": {
    "1": {
      "L": "And an angel of the LORD came up from Gilgal to Bochim, and said, I made you to go up out of Egypt, and have brought you unto the land which I sware unto your fathers; and I said, I will never break my covenant with you.",
      "M": "Now the angel of the LORD went up from Gilgal to Bochim. And he said, \"I brought you up from Egypt and led you into the land that I swore to give to your fathers. I said, 'I will never break my covenant with you,",
      "T": "The angel of the LORD traveled from Gilgal to Bochim and addressed the entire assembly: \"I brought you out of Egypt and into the land I swore to your ancestors. I bound myself: I will never break my covenant with you."
    },
    "2": {
      "L": "And ye shall make no league with the inhabitants of this land; ye shall throw down their altars: but ye have not obeyed my voice: why have ye done this?",
      "M": "and you shall make no covenant with the inhabitants of this land; you shall break down their altars.' But you have not obeyed my voice. What is this you have done?",
      "T": "My terms were simple: make no treaty with the people of this land, and tear down their altars. You obeyed neither. What have you done?"
    },
    "3": {
      "L": "Wherefore I also said, I will not drive them out from before you; but they shall be as thorns in your sides, and their gods shall be a snare unto you.",
      "M": "So now I say, I will not drive them out before you, but they shall become thorns in your sides, and their gods shall be a snare to you.\"",
      "T": "Therefore I am withdrawing my commitment to clear them out. From now on they will be thorns in your flesh, and their gods will be a trap that catches you.\""
    },
    "4": {
      "L": "And it came to pass, when the angel of the LORD spake these words unto all the children of Israel, that the people lifted up their voice, and wept.",
      "M": "As soon as the angel of the LORD spoke these words to all the people of Israel, the people lifted up their voices and wept.",
      "T": "When the angel finished speaking, the whole assembly of Israel broke into weeping."
    },
    "5": {
      "L": "And they called the name of that place Bochim: and they sacrificed there unto the LORD.",
      "M": "And they called the name of that place Bochim. And they sacrificed there to the LORD.",
      "T": "They named the place Bochim—\"Weepers\"—and offered sacrifices to the LORD there."
    },
    "6": {
      "L": "And when Joshua had let the people go, the children of Israel went every man unto his inheritance to possess the land.",
      "M": "When Joshua had dismissed the people, the people of Israel went each to his inheritance to take possession of the land.",
      "T": "The narrative steps back: when Joshua dismissed the people, each tribe had gone to claim its allotted land."
    },
    "7": {
      "L": "And the people served the LORD all the days of Joshua, and all the days of the elders that outlived Joshua, who had seen all the great works of the LORD, that he did for Israel.",
      "M": "And the people served the LORD all the days of Joshua, and all the days of the elders who outlived Joshua, who had seen all the great work that the LORD had done for Israel.",
      "T": "As long as Joshua lived, and as long as the elders who had seen the LORD's great deeds survived, Israel served the LORD."
    },
    "8": {
      "L": "And Joshua the son of Nun, the servant of the LORD, died, being an hundred and ten years old.",
      "M": "And Joshua the son of Nun, the servant of the LORD, died at the age of 110 years.",
      "T": "Joshua son of Nun, the LORD's servant, died at the age of one hundred and ten."
    },
    "9": {
      "L": "And they buried him in the border of his inheritance in Timnathheres, in the mount of Ephraim, on the north side of the hill Gaash.",
      "M": "And they buried him within the boundaries of his inheritance in Timnath-heres, in the hill country of Ephraim, north of the mountain of Gaash.",
      "T": "He was buried at Timnath-heres in the Ephraimite highlands, on the north slope of Mount Gaash."
    },
    "10": {
      "L": "And also all that generation were gathered unto their fathers: and there arose another generation after them, which knew not the LORD, nor yet the works which he did for Israel.",
      "M": "And all that generation also were gathered to their fathers. And there arose another generation after them who did not know the LORD or the work that he had done for Israel.",
      "T": "That whole generation passed away. The generation that followed had no personal knowledge of the LORD or of what he had done for Israel. Memory failed, and with it, loyalty."
    },
    "11": {
      "L": "And the children of Israel did evil in the sight of the LORD, and served Baalim:",
      "M": "And the people of Israel did what was evil in the sight of the LORD and served the Baals.",
      "T": "And Israel did what was evil in the LORD's sight: they worshiped the Baals."
    },
    "12": {
      "L": "And they forsook the LORD God of their fathers, which brought them out of the land of Egypt, and followed other gods, of the gods of the people that were round about them, and bowed themselves unto them, and provoked the LORD to anger.",
      "M": "They abandoned the LORD, the God of their fathers, who had brought them out of the land of Egypt. They went after other gods, from among the gods of the peoples who were around them, and bowed down to them. And they provoked the LORD to anger.",
      "T": "They abandoned the LORD—the God who had brought them out of Egypt—and chased after the local gods of the surrounding peoples, bowing down to them. This provoked the LORD deeply."
    },
    "13": {
      "L": "And they forsook the LORD, and served Baal and Ashtaroth.",
      "M": "They abandoned the LORD and served Baal and the Ashtoreths.",
      "T": "They turned from the LORD and gave themselves to Baal and the Ashtoreths—the storm god and the fertility goddess of Canaan."
    },
    "14": {
      "L": "And the anger of the LORD was hot against Israel, and he delivered them into the hands of spoilers that spoiled them, and he sold them into the hands of their enemies round about, so that they could not any longer stand before their enemies.",
      "M": "So the anger of the LORD was kindled against Israel, and he gave them over to plunderers who plundered them. And he sold them into the hand of their surrounding enemies, so that they could no longer stand before their enemies.",
      "T": "The LORD's anger blazed against Israel. He gave them into the hands of raiders who plundered them and sold them—as property—to the enemies pressing in from every side. They could not hold their ground."
    },
    "15": {
      "L": "Whithersoever they went out, the hand of the LORD was against them for evil, as the LORD had said, and as the LORD had sworn unto them: and they were greatly distressed.",
      "M": "Whenever they marched out, the hand of the LORD was against them for harm, as the LORD had warned, and as the LORD had sworn to them. And they were in terrible distress.",
      "T": "Every campaign ended in disaster. The LORD had sworn this would happen, and now the oath ran its course. Israel was in utter ruin."
    },
    "16": {
      "L": "Nevertheless the LORD raised up judges, which delivered them out of the hand of those that spoiled them.",
      "M": "Then the LORD raised up judges, who saved them out of the hand of those who plundered them.",
      "T": "Yet the LORD raised up judges—rescuers—to deliver them from those who were crushing them."
    },
    "17": {
      "L": "And yet they would not hearken unto their judges, but they went a whoring after other gods, and bowed themselves unto them: they turned quickly out of the way which their fathers walked in, obeying the commandments of the LORD; but they did not so.",
      "M": "Yet they did not listen to their judges, for they committed spiritual adultery after other gods and bowed down to them. They turned quickly out of the way in which their fathers had walked in obeying the commandments of the LORD, and they did not do so.",
      "T": "Yet even then they refused to listen to those judges. They kept chasing other gods, abandoning the path their ancestors had walked. The judges' authority was ignored; the covenant pattern was already broken in their own generation."
    },
    "18": {
      "L": "And when the LORD raised them up judges, then the LORD was with the judge, and delivered them out of the hand of their enemies all the days of the judge: for it repented the LORD because of their groanings by reason of them that oppressed them and vexed them.",
      "M": "Whenever the LORD raised up judges for them, the LORD was with the judge, and he saved them from the hand of their enemies all the days of the judge. For the LORD was moved to compassion by their groaning because of those who afflicted and oppressed them.",
      "T": "Whenever the LORD raised up a judge, he was with that judge, and the people experienced rescue for as long as the judge lived. For the LORD could not bear to hear their groaning under oppression—his compassion kept overriding their faithlessness."
    },
    "19": {
      "L": "And it came to pass, when the judge was dead, that they returned, and corrupted themselves more than their fathers, in following other gods to serve them, and to bow down unto them; they ceased not from their own doings, nor from their stubborn way.",
      "M": "But whenever the judge died, they turned back and were more corrupt than their fathers, going after other gods, serving them and bowing down to them. They did not drop any of their practices or their stubborn ways.",
      "T": "But each time a judge died, the people sank lower than before—deeper into idolatry, more stubborn in their ways. The cycle tightened: each apostasy worse than the last."
    },
    "20": {
      "L": "And the anger of the LORD was hot against Israel; and he said, Because that this people hath transgressed my covenant which I commanded their fathers, and have not hearkened unto my voice;",
      "M": "So the anger of the LORD was kindled against Israel, and he said, \"Because this people has transgressed my covenant that I commanded their fathers and has not obeyed my voice,",
      "T": "The LORD's anger burned against Israel. He declared: \"This people has broken the covenant I gave their ancestors and refused to obey my voice."
    },
    "21": {
      "L": "I also will not henceforth drive out any from before them of the nations which Joshua left when he died:",
      "M": "I will no longer drive out before them any of the nations that Joshua left when he died,",
      "T": "Therefore I will no longer drive out the nations Joshua left behind when he died."
    },
    "22": {
      "L": "That through them I may prove Israel, whether they will keep the way of the LORD to walk therein, as their fathers did keep it, or not.",
      "M": "in order to test Israel by them, whether they will take care to walk in the way of the LORD as their fathers did, or not.\"",
      "T": "Those nations will remain as a test—to reveal whether Israel will walk in the LORD's ways as their ancestors did, or not.\""
    },
    "23": {
      "L": "Therefore the LORD left those nations, without driving them out hastily; neither delivered he them into the hand of Joshua.",
      "M": "So the LORD left those nations, not driving them out quickly, and he did not give them into the hand of Joshua.",
      "T": "So the LORD deliberately left those nations in place, without handing them to Joshua. The test was always part of the plan."
    }
  },
  "3": {
    "1": {
      "L": "Now these are the nations which the LORD left, to prove Israel by them, even as many of Israel as had not known all the wars of Canaan;",
      "M": "Now these are the nations that the LORD left in order to test Israel by them, that is, all in Israel who had not experienced all the wars in Canaan.",
      "T": "These are the nations the LORD left in the land to test Israel—specifically those Israelites who had no personal experience of the Canaanite wars."
    },
    "2": {
      "L": "Only that the generations of the children of Israel might know, to teach them war, at the least such as before knew nothing thereof;",
      "M": "It was only so that the generations of the people of Israel might know war, to teach it to those who had not known it before.",
      "T": "There was a practical reason too: to train the younger generation in warfare—those who had never seen battle."
    },
    "3": {
      "L": "Namely, five lords of the Philistines, and all the Canaanites, and the Sidonians, and the Hivites that dwelt in mount Lebanon, from mount Baalhermon unto the entering in of Hamath.",
      "M": "These are the nations: the five lords of the Philistines and all the Canaanites and the Sidonians and the Hivites who lived on Mount Lebanon, from Mount Baal-hermon as far as Lebo-hamath.",
      "T": "The nations left in place were: the five Philistine city-states, all the Canaanites, the Sidonians, and the Hivites of the Lebanon range—from Mount Baal-hermon to the approaches of Hamath."
    },
    "4": {
      "L": "And they were to prove Israel by them, to know whether they would hearken unto the commandments of the LORD, which he commanded their fathers by the hand of Moses.",
      "M": "They were there to test Israel—to know whether Israel would obey the commandments of the LORD, which he had commanded their fathers by the hand of Moses.",
      "T": "Their purpose: to show whether Israel would actually keep the commandments the LORD gave through Moses—or not."
    },
    "5": {
      "L": "And the children of Israel dwelt among the Canaanites, Hittites, and Amorites, and Perizzites, and Hivites, and Jebusites:",
      "M": "So the people of Israel lived among the Canaanites, the Hittites, the Amorites, the Perizzites, the Hivites, and the Jebusites.",
      "T": "And Israel lived embedded among all six Canaanite peoples—Canaanites, Hittites, Amorites, Perizzites, Hivites, and Jebusites."
    },
    "6": {
      "L": "And they took their daughters to be their wives, and gave their daughters to their sons, and served their gods.",
      "M": "And they took their daughters as wives for themselves, and gave their own daughters to their sons, and served their gods.",
      "T": "They intermarried freely and adopted their gods. The assimilation was total."
    },
    "7": {
      "L": "And the children of Israel did evil in the sight of the LORD, and forgat the LORD their God, and served Baalim and the groves.",
      "M": "And the people of Israel did what was evil in the sight of the LORD. They forgot the LORD their God and served the Baals and the Asheroth.",
      "T": "Israel did what was evil before the LORD. They forgot their God entirely and gave themselves to the Baals and Asherah poles."
    },
    "8": {
      "L": "Therefore the anger of the LORD was hot against Israel, and he sold them into the hand of Chushanrishathaim king of Mesopotamia: and the children of Israel served Chushanrishathaim eight years.",
      "M": "Therefore the anger of the LORD was kindled against Israel, and he sold them into the hand of Cushan-rishathaim king of Mesopotamia. And the people of Israel served Cushan-rishathaim eight years.",
      "T": "The LORD's anger burned, and he gave Israel over to Cushan-rishathaim, king of Aram-naharaim—the land between the two great rivers. They were under his thumb for eight years."
    },
    "9": {
      "L": "And when the children of Israel cried unto the LORD, the LORD raised up a deliverer to the children of Israel, who delivered them, even Othniel the son of Kenaz, Caleb's younger brother.",
      "M": "But when the people of Israel cried out to the LORD, the LORD raised up a deliverer for the people of Israel, who saved them—Othniel the son of Kenaz, Caleb's younger brother.",
      "T": "Israel cried out to the LORD, and the LORD raised a deliverer: Othniel son of Kenaz, the same younger brother of Caleb who had taken Kiriath-sepher."
    },
    "10": {
      "L": "And the Spirit of the LORD came upon him, and he judged Israel, and went out to war: and the LORD delivered Chushanrishathaim king of Mesopotamia into his hand; and his hand prevailed against Chushanrishathaim.",
      "M": "The Spirit of the LORD was upon him, and he judged Israel. He went out to war, and the LORD gave Cushan-rishathaim king of Mesopotamia into his hand. And his hand prevailed over Cushan-rishathaim.",
      "T": "The Spirit of the LORD came upon him. He led Israel and went out to battle. The LORD gave Cushan-rishathaim into his hand, and he prevailed."
    },
    "11": {
      "L": "And the land had rest forty years. And Othniel the son of Kenaz died.",
      "M": "So the land had rest forty years. Then Othniel the son of Kenaz died.",
      "T": "The land rested for forty years. Then Othniel died."
    },
    "12": {
      "L": "And the children of Israel did evil again in the sight of the LORD: and the LORD strengthened Eglon the king of Moab against Israel, because they had done evil in the sight of the LORD.",
      "M": "And the people of Israel again did what was evil in the sight of the LORD, and the LORD strengthened Eglon the king of Moab against Israel, because they had done evil in the sight of the LORD.",
      "T": "Israel fell back into evil before the LORD—and the LORD used Eglon king of Moab as his instrument of discipline."
    },
    "13": {
      "L": "And he gathered unto him the children of Ammon and Amalek, and went and smote Israel, and possessed the city of palm trees.",
      "M": "Eglon gathered to him the Ammonites and the Amalekites, and went and defeated Israel. And they took possession of the city of palms.",
      "T": "Eglon allied with Ammon and Amalek, struck Israel, and seized Jericho—the city of palms."
    },
    "14": {
      "L": "So the children of Israel served Eglon the king of Moab eighteen years.",
      "M": "And the people of Israel served Eglon the king of Moab eighteen years.",
      "T": "Israel served Eglon of Moab for eighteen years."
    },
    "15": {
      "L": "But when the children of Israel cried unto the LORD, the LORD raised them up a deliverer, Ehud the son of Gera, a Benjamite, a man lefthanded: and by him the children of Israel sent a present unto Eglon the king of Moab.",
      "M": "Then the people of Israel cried out to the LORD, and the LORD raised up for them a deliverer, Ehud the son of Gera, the Benjamite, a left-handed man. The people of Israel sent tribute by him to Eglon the king of Moab.",
      "T": "They cried out again, and the LORD raised a deliverer: Ehud son of Gera, a Benjamite—and left-handed. The Israelites sent him to deliver their tribute payment to King Eglon of Moab."
    },
    "16": {
      "L": "But Ehud made him a dagger which had two edges, of a cubit length; and he did gird it under his raiment upon his right thigh.",
      "M": "And Ehud made for himself a sword with two edges, a cubit in length, and he bound it on his right thigh under his clothes.",
      "T": "Ehud crafted a double-edged short sword—about eighteen inches long—and strapped it on his right thigh under his clothing. A left-handed man reaching across to his right thigh would not be noticed in a security search."
    },
    "17": {
      "L": "And he brought the present unto Eglon king of Moab: and Eglon was a very fat man.",
      "M": "And he presented the tribute to Eglon king of Moab. Now Eglon was a very fat man.",
      "T": "He presented the tribute to Eglon. The king was enormously fat—a detail the narrator records with purpose."
    },
    "18": {
      "L": "And when he had made an end to offer the present, he sent away the people that bare the present.",
      "M": "And when Ehud had finished presenting the tribute, he sent away the people who had carried it.",
      "T": "After delivering the tribute, Ehud dismissed the servants who had carried it."
    },
    "19": {
      "L": "But he himself turned again from the quarries that were by Gilgal, and said, I have a secret errand unto thee, O king: who said, Keep silence. And all that stood by him went out from him.",
      "M": "But he himself turned back from the stone images near Gilgal and said, \"I have a secret message for you, O king.\" The king said, \"Silence!\" And all his attendants went out from his presence.",
      "T": "Ehud turned back at the carved-stone site near Gilgal and said, \"I have a private message for you, Your Majesty.\" The king said, \"Quiet!\" and dismissed all his attendants."
    },
    "20": {
      "L": "And Ehud came unto him; and he was sitting in a summer parlour, which he had for himself alone. And Ehud said, I have a message from God unto thee. And he arose out of his seat.",
      "M": "And Ehud came to him as he was sitting alone in his cool roof chamber. And Ehud said, \"I have a message from God for you.\" And he rose from his seat.",
      "T": "Eglon was alone in his cool upper room. Ehud said, \"I have a word from God for you.\" The king stood up to receive it—and Ehud's left hand moved."
    },
    "21": {
      "L": "And Ehud put forth his left hand, and took the dagger from his right thigh, and thrust it into his belly:",
      "M": "And Ehud reached with his left hand, took the sword from his right thigh, and thrust it into his belly.",
      "T": "Ehud drew the hidden blade with his left hand and drove it into the king's belly."
    },
    "22": {
      "L": "And the haft also went in after the blade; and the fat closed upon the blade, so that he could not draw the dagger out of his belly; and the dirt came out.",
      "M": "And the hilt also went in after the blade, and the fat closed over the blade, for he did not pull the sword out of his belly; and the dung came out.",
      "T": "The blade went in so deep that the hilt followed; the fat sealed around it. Ehud left the sword embedded—and the body's contents began to seep out."
    },
    "23": {
      "L": "Then Ehud went forth through the porch, and shut the doors of the parlour upon him, and locked them.",
      "M": "Then Ehud went out into the vestibule and shut the doors of the roof chamber on him and locked them.",
      "T": "Ehud slipped out through the porch, pulled the doors of the upper room closed behind him, and locked them."
    },
    "24": {
      "L": "When he was gone out, his servants came; and when they saw that the doors of the parlour were locked, they said, Surely he covereth his feet in his summer chamber.",
      "M": "When he had gone, the servants came, and when they saw that the doors of the roof chamber were locked, they thought, \"Surely he is relieving himself in the cool chamber.\"",
      "T": "His servants came and found the doors locked. They assumed the king was using the privy and waited politely."
    },
    "25": {
      "L": "And they tarried till they were ashamed: and, behold, he opened not the doors of the parlour: therefore they took a key, and opened them: and, behold, their lord was fallen down dead on the earth.",
      "M": "And they waited until they were embarrassed. But when he still did not open the doors of the roof chamber, they took the key and opened them, and there was their lord fallen dead on the floor.",
      "T": "They waited until the delay became awkward. Finally they unlocked the door—and found the king dead on the floor."
    },
    "26": {
      "L": "And Ehud escaped while they tarried, and passed beyond the quarries, and escaped unto Seirath.",
      "M": "Ehud escaped while they delayed, and he passed beyond the stone images and escaped to Seirath.",
      "T": "While they had been waiting, Ehud was long gone—past the carved stones, all the way to Seirath."
    },
    "27": {
      "L": "And it came to pass, when he was come, that he blew a trumpet in the mountain of Ephraim, and the children of Israel went down with him from the mount, and he before them.",
      "M": "When he arrived, he sounded the trumpet in the hill country of Ephraim. And the people of Israel went down with him from the hill country, with him leading them.",
      "T": "Reaching the Ephraimite highlands, he blew the war trumpet. Israel's warriors came streaming down from the hills—Ehud at their head."
    },
    "28": {
      "L": "And he said unto them, Follow after me: for the LORD hath delivered your enemies the Moabites into your hand. And they went down after him, and took the fords of Jordan toward Moab, and suffered not a man to pass over.",
      "M": "And he said to them, \"Follow me, for the LORD has given your enemies the Moabites into your hand.\" So they went down after him and seized the fords of the Jordan against the Moabites and allowed no one to cross over.",
      "T": "He declared, \"Follow me! The LORD has given Moab into our hands!\" They seized the Jordan crossing-points and sealed them—not a single Moabite got through."
    },
    "29": {
      "L": "And they slew of Moab at that time about ten thousand men, all lusty, and all men of valour; and there escaped not a man.",
      "M": "And they killed at that time about ten thousand of the Moabites, all strong, able-bodied men; not a man escaped.",
      "T": "At the fords they slaughtered about ten thousand Moabite warriors—every one of them a fighting man. Not one escaped."
    },
    "30": {
      "L": "So Moab was subdued that day under the hand of Israel. And the land had rest fourscore years.",
      "M": "So Moab was subdued that day under the hand of Israel. And the land had rest for eighty years.",
      "T": "Moab was broken under Israel's hand that day. The land enjoyed eighty years of peace."
    },
    "31": {
      "L": "And after him was Shamgar the son of Anath, which slew of the Philistines six hundred men with an ox goad: and he also delivered Israel.",
      "M": "After him was Shamgar the son of Anath, who killed six hundred of the Philistines with an oxgoad. He also delivered Israel.",
      "T": "After Ehud came Shamgar son of Anath. With nothing but a farmer's oxgoad, he killed six hundred Philistines—and saved Israel."
    }
  },
  "4": {
    "1": {
      "L": "And the children of Israel again did evil in the sight of the LORD, when Ehud was dead.",
      "M": "And the people of Israel again did what was evil in the sight of the LORD after Ehud died.",
      "T": "After Ehud's death, Israel fell back into evil before the LORD."
    },
    "2": {
      "L": "And the LORD sold them into the hand of Jabin king of Canaan, that reigned in Hazor; the captain of whose host was Sisera, which dwelt in Harosheth of the Gentiles.",
      "M": "And the LORD sold them into the hand of Jabin king of Canaan, who reigned in Hazor. The commander of his army was Sisera, who lived in Harosheth-hagoyim.",
      "T": "The LORD handed them over to Jabin, king of Canaan at Hazor—whose military commander, Sisera, operated from the fortress of Harosheth-hagoyim."
    },
    "3": {
      "L": "And the children of Israel cried unto the LORD: for he had nine hundred chariots of iron; and twenty years he mightily oppressed the children of Israel.",
      "M": "Then the people of Israel cried out to the LORD for help, for Sisera had 900 chariots of iron and he cruelly oppressed the people of Israel for twenty years.",
      "T": "Israel cried to the LORD for help. For twenty years Sisera had crushed them with nine hundred iron-wheeled war chariots—the heavy armor of that era."
    },
    "4": {
      "L": "And Deborah, a prophetess, the wife of Lapidoth, she judged Israel at that time.",
      "M": "Now Deborah, a prophetess, the wife of Lappidoth, was judging Israel at that time.",
      "T": "At that time Deborah—a prophetess, wife of Lappidoth—was governing Israel. She was both prophet and judge, the only one in Judges to hold both offices."
    },
    "5": {
      "L": "And she dwelt under the palm tree of Deborah between Ramah and Bethel in mount Ephraim: and the children of Israel came up to her for judgment.",
      "M": "She used to sit under the palm of Deborah between Ramah and Bethel in the hill country of Ephraim, and the people of Israel came up to her for judgment.",
      "T": "She held court under Deborah's Palm—her landmark between Ramah and Bethel in the Ephraimite hills—and the people came to her with their disputes."
    },
    "6": {
      "L": "And she sent and called Barak the son of Abinoam out of Kedeshnaphtali, and said unto him, Hath not the LORD God of Israel commanded, saying, Go and draw toward mount Tabor, and take with thee ten thousand men of the children of Naphtali and of the children of Zebulun?",
      "M": "She sent and summoned Barak the son of Abinoam from Kedesh-naphtali and said to him, \"Has not the LORD, the God of Israel, commanded you, 'Go, gather your men at Mount Tabor, taking 10,000 from the people of Naphtali and the people of Zebulun?",
      "T": "She summoned Barak son of Abinoam from Kedesh-naphtali and said: \"The LORD, Israel's God, has given you an order: march to Mount Tabor with ten thousand warriors from Naphtali and Zebulun.\""
    },
    "7": {
      "L": "And I will draw unto thee to the river Kishon Sisera, the captain of Jabin's army, with his chariots and his multitude; and I will deliver him into thine hand.",
      "M": "And I will draw out Sisera, the general of Jabin's army, to meet you by the river Kishon with his chariots and his troops, and I will give him into your hand.'?\"",
      "T": "\"I will lure Sisera and his iron chariots to the Kishon River and deliver him into your hands.\" This was the LORD's word through her."
    },
    "8": {
      "L": "And Barak said unto her, If thou wilt go with me, then I will go: but if thou wilt not go with me, then I will not go.",
      "M": "Barak said to her, \"If you will go with me, I will go, but if you will not go with me, I will not go.\"",
      "T": "Barak said, \"I'll go—but only if you come with me. If you won't come, neither will I.\""
    },
    "9": {
      "L": "And she said, I will surely go with thee: notwithstanding the journey that thou takest shall not be for thine honour; for the LORD shall sell Sisera into the hand of a woman. And Deborah arose, and went with Barak to Kedesh.",
      "M": "And she said, \"I will surely go with you. Nevertheless, the road on which you are going will not lead to your glory, for the LORD will sell Sisera into the hand of a woman.\" Then Deborah arose and went with Barak to Kedesh.",
      "T": "She said, \"I'll come. But know this: the glory of the victory will not fall to you. The LORD will give Sisera into the hand of a woman.\" She rose and went with Barak to Kedesh."
    },
    "10": {
      "L": "And Barak called Zebulun and Naphtali to Kedesh; and he went up with ten thousand men at his feet: and Deborah went up with him.",
      "M": "And Barak called out Zebulun and Naphtali to Kedesh. And 10,000 men went up at his heels, and Deborah went up with him.",
      "T": "Barak mustered Zebulun and Naphtali at Kedesh. Ten thousand men marched behind him—Deborah at his side."
    },
    "11": {
      "L": "Now Heber the Kenite, which was of the children of Hobab the father in law of Moses, had severed himself from the Kenites, and pitched his tent unto the plain of Zaanaim, which is by Kedesh.",
      "M": "Now Heber the Kenite had separated from the Kenites, the descendants of Hobab the father-in-law of Moses, and had pitched his tent as far away as the great tree in Zaanannim, which is near Kedesh.",
      "T": "A narrative detail that will matter: Heber the Kenite had broken from his clan—descendants of Moses' father-in-law—and pitched his tent near the great tree at Zaanannim, close to Kedesh."
    },
    "12": {
      "L": "And they shewed Sisera that Barak the son of Abinoam was gone up to mount Tabor.",
      "M": "When Sisera was told that Barak the son of Abinoam had gone up to Mount Tabor,",
      "T": "Word reached Sisera: Barak had positioned his forces on Mount Tabor."
    },
    "13": {
      "L": "And Sisera gathered together all his chariots, even nine hundred chariots of iron, and all the people that were with him, from Harosheth of the Gentiles unto the river of Kishon.",
      "M": "Sisera called out all his chariots—900 chariots of iron—and all the men who were with him, from Harosheth-hagoyim to the river Kishon.",
      "T": "Sisera mobilized everything: all nine hundred iron chariots and his full infantry, moving from Harosheth-hagoyim toward the Kishon."
    },
    "14": {
      "L": "And Deborah said unto Barak, Up; for this is the day in which the LORD hath delivered Sisera into thine hand: is not the LORD gone out before thee? So Barak went down from mount Tabor, and ten thousand men after him.",
      "M": "And Deborah said to Barak, \"Up! For this is the day in which the LORD has given Sisera into your hand. Does not the LORD go out before you?\" So Barak went down from Mount Tabor with 10,000 men following him.",
      "T": "Deborah gave the order: \"Now! This is the day the LORD has given Sisera into your hand. The LORD himself goes before you!\" Barak charged down from Tabor with his ten thousand."
    },
    "15": {
      "L": "And the LORD discomfited Sisera, and all his chariots, and all his host, with the edge of the sword before Barak; so that Sisera lighted down off his chariot, and fled away on his feet.",
      "M": "And the LORD routed Sisera and all his chariots and all his army before Barak by the edge of the sword. And Sisera got down from his chariot and fled away on foot.",
      "T": "The LORD threw Sisera's entire force into panic. His chariots—the great weapon of Canaanite power—became useless in the rout. Sisera abandoned his chariot and fled on foot."
    },
    "16": {
      "L": "But Barak pursued after the chariots, and after the host, unto Harosheth of the Gentiles: and all the host of Sisera fell upon the edge of the sword; and there was not a man left.",
      "M": "And Barak pursued the chariots and the army to Harosheth-hagoyim, and all the army of Sisera fell by the edge of the sword; not a man was left.",
      "T": "Barak ran the chariots all the way back to Harosheth-hagoyim. The entire Canaanite army was destroyed—not one man survived."
    },
    "17": {
      "L": "Howbeit Sisera fled away on his feet to the tent of Jael the wife of Heber the Kenite: for there was peace between Jabin the king of Hazor and the house of Heber the Kenite.",
      "M": "But Sisera fled away on foot to the tent of Jael, the wife of Heber the Kenite, for there was peace between Jabin the king of Hazor and the house of Heber the Kenite.",
      "T": "Sisera ran—on foot now—to the tent of Jael, wife of Heber the Kenite. Heber's clan had a peace treaty with Jabin, so Sisera thought he was safe."
    },
    "18": {
      "L": "And Jael went out to meet Sisera, and said unto him, Turn in, my lord, turn in to me; fear not. And when he had turned in unto her into the tent, she covered him with a mantle.",
      "M": "And Jael came out to meet Sisera and said to him, \"Turn aside, my lord; turn aside to me; do not be afraid.\" So he turned aside to her into the tent, and she covered him with a rug.",
      "T": "Jael came out to meet him. \"Come in, my lord, come in—don't be afraid.\" He entered her tent and she covered him with a blanket."
    },
    "19": {
      "L": "And he said unto her, Give me, I pray thee, a little water to drink; for I am thirsty. And she opened a bottle of milk, and gave him drink, and covered him.",
      "M": "And he said to her, \"Please give me a little water to drink, for I am thirsty.\" So she opened a skin of milk and gave him a drink and covered him.",
      "T": "He asked for water. She gave him milk—rich, sleep-inducing milk—and covered him again."
    },
    "20": {
      "L": "Again he said unto her, Stand in the door of the tent, and it shall be, when any man doth come and enquire of thee, and say, Is there any man here? that thou shalt say, No.",
      "M": "And he said to her, \"Stand at the opening of the tent, and if any man comes and asks you, 'Is anyone here?' say, 'No.'\"",
      "T": "He ordered her: \"Stand at the tent door. If anyone asks whether a man is here, say no.\" He had no power to give such an order—and she had no intention of obeying."
    },
    "21": {
      "L": "Then Jael Heber's wife took a nail of the tent, and took an hammer in her hand, and went softly unto him, and smote the nail into his temples, and fastened it into the ground: for he was fast asleep and weary. So he died.",
      "M": "But Jael the wife of Heber took a tent peg and took a hammer in her hand. Then she went quietly to him and drove the peg into his temple until it went down into the ground while he was lying fast asleep from exhaustion. So he died.",
      "T": "Jael picked up a tent peg and a mallet. She went softly to where he lay—dead with exhaustion and sleep. She drove the peg through his temple into the ground. He died."
    },
    "22": {
      "L": "And, behold, as Barak pursued Sisera, Jael came out to meet him, and said unto him, Come, and I will shew thee the man whom thou seekest. And when he came into her tent, behold, Sisera lay dead, and the nail was in his temples.",
      "M": "And behold, as Barak was pursuing Sisera, Jael went out to meet him and said to him, \"Come, and I will show you the man whom you are seeking.\" So he went in to her, and there lay Sisera dead, with the tent peg in his temple.",
      "T": "Barak arrived in pursuit. Jael came out: \"Come—I'll show you the man you're looking for.\" He entered the tent and found Sisera dead, the tent peg through his skull. Deborah's prophecy was complete."
    },
    "23": {
      "L": "So God subdued on that day Jabin the king of Canaan before the children of Israel.",
      "M": "So on that day God subdued Jabin the king of Canaan before the people of Israel.",
      "T": "On that day God broke the power of Jabin king of Canaan before Israel."
    },
    "24": {
      "L": "And the hand of the children of Israel prospered, and prevailed against Jabin the king of Canaan, until they had destroyed Jabin king of Canaan.",
      "M": "And the hand of the people of Israel pressed harder and harder against Jabin the king of Canaan, until they destroyed Jabin king of Canaan.",
      "T": "Israel's hand grew heavier and heavier against Jabin until he was completely destroyed."
    }
  },
  "5": {
    "1": {
      "L": "Then sang Deborah and Barak the son of Abinoam on that day, saying,",
      "M": "Then Deborah sang, and Barak the son of Abinoam, on that day, saying:",
      "T": "On that day Deborah sang—and Barak son of Abinoam with her:"
    },
    "2": {
      "L": "Praise ye the LORD for the avenging of Israel, when the people willingly offered themselves.",
      "M": "\"When locks went loose in Israel, when the people offered themselves willingly— bless the LORD!",
      "T": "When the warriors of Israel let their hair down free,\nwhen the people rose up as volunteers—\nbless the LORD!"
    },
    "3": {
      "L": "Hear, O ye kings; give ear, O ye princes; I, even I, will sing unto the LORD; I will sing praise to the LORD God of Israel.",
      "M": "Hear, O kings! Give ear, O princes! To the LORD I will sing; I will make melody to the LORD, the God of Israel.",
      "T": "Hear me, you kings!\nListen, you princes!\nI will sing—I myself—to the LORD;\nI will make music to the LORD, the God of Israel."
    },
    "4": {
      "L": "LORD, when thou wentest out of Seir, when thou marchedst out of the field of Edom, the earth trembled, and the heavens dropped, the clouds also dropped water.",
      "M": "LORD, when you went out from Seir, when you marched from the region of Edom, the earth trembled and the heavens dropped, yes, the clouds dropped water.",
      "T": "LORD, when you marched out from Seir,\nwhen you strode out from the fields of Edom,\nthe earth shook, the heavens poured,\nthe clouds burst open with rain."
    },
    "5": {
      "L": "The mountains melted from before the LORD, even that Sinai from before the LORD God of Israel.",
      "M": "The mountains quaked before the LORD, even Sinai before the LORD, the God of Israel.",
      "T": "The mountains convulsed before the LORD—\nthat Sinai itself trembled before the LORD, the God of Israel."
    },
    "6": {
      "L": "In the days of Shamgar the son of Anath, in the days of Jael, the highways were unoccupied, and the travellers walked through byways.",
      "M": "In the days of Shamgar the son of Anath, in the days of Jael, the highways were abandoned, and travelers kept to the byways.",
      "T": "In Shamgar's day, in Jael's day,\nthe main roads lay empty—\ntravelers crept along back paths."
    },
    "7": {
      "L": "The inhabitants of the villages ceased, they ceased in Israel, until that I Deborah arose, that I arose a mother in Israel.",
      "M": "The villagers ceased in Israel; they ceased until I arose—I, Deborah, arose as a mother in Israel.",
      "T": "Village life had died out in Israel—utterly ceased—\nuntil I arose, Deborah,\nuntil I arose, a mother in Israel."
    },
    "8": {
      "L": "They chose new gods; then was war in the gates: was there a shield or spear seen among forty thousand in Israel?",
      "M": "When new gods were chosen, then war was in the gates. Was shield or spear to be seen among forty thousand in Israel?",
      "T": "They chose new gods—and war came to their very gates.\nNot a shield, not a spear to be seen\namong forty thousand in Israel."
    },
    "9": {
      "L": "My heart is toward the governors of Israel, that offered themselves willingly among the people. Bless ye the LORD.",
      "M": "My heart goes out to the commanders of Israel who offered themselves willingly among the people. Bless the LORD.",
      "T": "My heart goes out to Israel's willing leaders,\nto all who volunteered among the people—\nbless the LORD!"
    },
    "10": {
      "L": "Speak, ye that ride on white asses, ye that sit in judgment, and walk by the way.",
      "M": "Tell of it, you who ride on tawny donkeys, you who sit on rich carpets, and you who walk by the way.",
      "T": "Speak of it—you who ride sleek white donkeys,\nyou who sit on costly saddle-blankets,\nand you who walk the road."
    },
    "11": {
      "L": "They that are delivered from the noise of archers in the places of drawing water, there shall they rehearse the righteous acts of the LORD, even the righteous acts toward the inhabitants of his villages in Israel: then shall the people of the LORD go down to the gates.",
      "M": "To the sound of musicians at the watering places, there they repeat the righteous triumphs of the LORD, the righteous triumphs of his warriors in Israel. Then the people of the LORD marched down to the gates.",
      "T": "At the watering troughs, beyond the archers' noise,\nthere they retell the LORD's righteous deeds,\nthe triumphs of his warriors in Israel—\nthen the LORD's people marched down to the gates."
    },
    "12": {
      "L": "Awake, awake, Deborah: awake, awake, utter a song: arise, Barak, and lead thy captivity captive, thou son of Abinoam.",
      "M": "Awake, awake, Deborah! Awake, awake, break out in a song! Arise, Barak, lead away your captives, O son of Abinoam.",
      "T": "Awake, awake, Deborah!\nAwake, awake, burst into song!\nRise up, Barak—lead your captives away,\nson of Abinoam!"
    },
    "13": {
      "L": "Then he made him that remaineth have dominion over the nobles among the people: the LORD made me have dominion over the mighty.",
      "M": "Then down marched the remnant of the noble; the people of the LORD marched down for me against the mighty.",
      "T": "Then the survivors marched down to the great ones;\nthe LORD's people came down for me against the warriors."
    },
    "14": {
      "L": "Out of Ephraim was there a root of them against Amalek; after thee, Benjamin, among thy people; out of Machir came down governors, and out of Zebulun they that handle the pen of the writer.",
      "M": "From Ephraim their root came down into the valley, following you, Benjamin, with your kinsmen; from Machir marched down the commanders, and from Zebulun those who bear the officer's staff.",
      "T": "From Ephraim—rooted against Amalek—they poured down;\nBenjamin, with your people, behind you;\nfrom Machir came the commanders marching;\nfrom Zebulun, those who carry the commander's staff."
    },
    "15": {
      "L": "And the princes of Issachar were with Deborah; even Issachar, and also Barak: he was sent on foot into the valley. For the divisions of Reuben there were great thoughts of heart.",
      "M": "The princes of Issachar came with Deborah; as Issachar, so was Barak; into the valley they rushed at his heels. Among the clans of Reuben there were great searchings of heart.",
      "T": "Issachar's princes marched with Deborah—\nas Issachar, so Barak—\nrushing into the valley at his feet.\nBut among Reuben's clans: great debates of conscience."
    },
    "16": {
      "L": "Why abodest thou among the sheepfolds, to hear the bleatings of the flocks? For the divisions of Reuben there were great searchings of heart.",
      "M": "Why did you sit still among the sheepfolds, to hear the whistling for the flocks? Among the clans of Reuben there were great searchings of heart.",
      "T": "Why did you stay behind with the sheep,\nlistening to the piping for the flocks?\nAmong Reuben's clans: great debates of conscience."
    },
    "17": {
      "L": "Gilead abode beyond Jordan: and why did Dan remain in ships? Asher continued on the sea shore, and abode in his breaches.",
      "M": "Gilead stayed beyond the Jordan; and Dan, why did he stay with the ships? Asher sat still at the coast of the sea, staying by his harbors.",
      "T": "Gilead camped east of the Jordan—absent.\nDan—why did you linger with your ships?\nAsher sat at the harbor, snug by his coast."
    },
    "18": {
      "L": "Zebulun and Naphtali were a people that jeoparded their lives unto the death in the high places of the field.",
      "M": "Zebulun is a people who risked their lives to the death; Naphtali, too, on the heights of the field.",
      "T": "But Zebulun—they staked their lives on the field of death.\nNaphtali too, on the open heights."
    },
    "19": {
      "L": "The kings came and fought, then fought the kings of Canaan in Taanach by the waters of Megiddo; they took no gain of money.",
      "M": "The kings came and fought; then fought the kings of Canaan at Taanach, by the waters of Megiddo. They got no plunder of silver.",
      "T": "The kings of Canaan came and fought—\nat Taanach, by the waters of Megiddo.\nThey took no silver. They got nothing."
    },
    "20": {
      "L": "They fought from heaven; the stars in their courses fought against Sisera.",
      "M": "From heaven the stars fought; from their courses they fought against Sisera.",
      "T": "From heaven the stars fought;\nfrom their courses they warred against Sisera."
    },
    "21": {
      "L": "The river of Kishon swept them away, that ancient river, the river Kishon. O my soul, thou hast trodden down strength.",
      "M": "The torrent Kishon swept them away, the ancient torrent, the torrent Kishon. March on, my soul, with might!",
      "T": "The Kishon swept them away—\nthat ancient river, the Kishon.\nMarch on, my soul—march on in strength!"
    },
    "22": {
      "L": "Then were the horsehoofs broken by the means of the pransings, the pransings of their mighty ones.",
      "M": "Then loud beat the horses' hoofs with the galloping, galloping of his steeds.",
      "T": "Then the horses' hooves hammered—\nthe pounding, pounding of the war-stallions."
    },
    "23": {
      "L": "Curse ye Meroz, said the angel of the LORD, curse ye bitterly the inhabitants thereof; because they came not to the help of the LORD, to the help of the LORD against the mighty.",
      "M": "Curse Meroz, says the angel of the LORD; curse its inhabitants thoroughly, because they did not come to the help of the LORD, to the help of the LORD against the mighty.",
      "T": "\"Curse Meroz!\" says the angel of the LORD.\n\"Curse its people bitterly—\nbecause they did not come to the LORD's aid,\nto the aid of the LORD against the warriors.\""
    },
    "24": {
      "L": "Blessed above women shall Jael the wife of Heber the Kenite be, blessed shall she be above women in the tent.",
      "M": "Most blessed of women be Jael, the wife of Heber the Kenite, of tent-dwelling women most blessed.",
      "T": "Most blessed of women is Jael—\nwife of Heber the Kenite,\nmost blessed of women who live in tents."
    },
    "25": {
      "L": "He asked water, and she gave him milk; she brought forth butter in a lordly dish.",
      "M": "He asked for water; she gave him milk. She brought him curds in a noble's bowl.",
      "T": "He asked for water; she brought him milk.\nIn a chieftain's bowl she served him curds."
    },
    "26": {
      "L": "She put her hand to the nail, and her right hand to the workmen's hammer; and with the hammer she smote Sisera, she smote off his head, when she had pierced and stricken through his temples.",
      "M": "She sent her hand to the tent peg and her right hand to the workmen's mallet. She struck Sisera; she crushed his head; she shattered and pierced his temple.",
      "T": "Her hand reached for the tent peg,\nher right hand for the mallet—\nshe struck Sisera, she crushed his head,\nshe shattered and drove through his temple."
    },
    "27": {
      "L": "At her feet he bowed, he fell, he lay down: at her feet he bowed, he fell: where he bowed, there he fell down dead.",
      "M": "Between her feet he sank, he fell, he lay still; between her feet he sank, he fell; where he sank, there he fell—dead.",
      "T": "Between her feet he sank, he fell, he lay.\nBetween her feet he sank, he fell.\nWhere he sank—there he fell. Dead."
    },
    "28": {
      "L": "The mother of Sisera looked out at a window, and cried through the lattice, Why is his chariot so long in coming? why tarry the wheels of his chariots?",
      "M": "Out of the window she peered, the mother of Sisera cried through the lattice: 'Why is his chariot so long in coming? Why tarry the hoofbeats of his chariots?'",
      "T": "Through the window she peered—Sisera's mother—\ncrying through the lattice:\n'Why is his chariot so late?\nWhy do the wheels of his chariots delay?'"
    },
    "29": {
      "L": "Her wise ladies answered her, yea, she returned answer to herself,",
      "M": "Her wisest ladies answered her; indeed, she answered herself:",
      "T": "Her wisest ladies answered her;\nand she answered herself:"
    },
    "30": {
      "L": "Have they not sped? have they not divided the prey; to every man a damsel or two; to Sisera a prey of divers colours, a prey of divers colours of needlework, of divers colours of needlework on both sides, meet for the necks of them that take the spoil?",
      "M": "'Are they not finding and dividing the spoil? A womb or two for every man; spoil of dyed materials for Sisera, spoil of dyed materials embroidered, two pieces of embroidered dyed work for the neck of the plunderer?'",
      "T": "'Are they not dividing the plunder even now?\nA girl, two girls for every man—\nfor Sisera: plunder of dyed cloth,\nplunder of embroidered cloth,\ntwo embroidered pieces for the neck of the conqueror?'"
    },
    "31": {
      "L": "So let all thine enemies perish, O LORD: but let them that love him be as the sun when he goeth forth in his might. And the land had rest forty years.",
      "M": "So may all your enemies perish, O LORD! But may those who love him be like the sun as it rises in its might.\" And the land had rest for forty years.",
      "T": "So may all your enemies perish, O LORD!\nBut let those who love you\nbe like the sun rising in full strength.\nAnd the land rested for forty years."
    }
  },
  "6": {
    "1": {
      "L": "And the children of Israel did evil in the sight of the LORD: and the LORD delivered them into the hand of Midian seven years.",
      "M": "The people of Israel did what was evil in the sight of the LORD, and the LORD gave them into the hand of Midian seven years.",
      "T": "Israel fell back into evil before the LORD, and the LORD gave them into Midian's hand for seven years."
    },
    "2": {
      "L": "And the hand of Midian prevailed against Israel: and because of the Midianites the children of Israel made them the dens which are in the mountains, and caves, and strong holds.",
      "M": "And the hand of Midian overpowered Israel, and because of Midian the people of Israel made for themselves the dens that are in the mountains and the caves and the strongholds.",
      "T": "Midian's grip was crushing. Israel was driven to hide—in mountain dens, caves, and fortified hollows."
    },
    "3": {
      "L": "And so it was, when Israel had sown, that the Midianites came up, and the Amalekites, and the children of the east, even they came up against them;",
      "M": "For whenever Israel planted crops, the Midianites and the Amalekites and the people of the East would come up against them.",
      "T": "Every time Israel planted crops, the Midianites, Amalekites, and eastern nomads came swarming in."
    },
    "4": {
      "L": "And they encamped against them, and destroyed the increase of the earth, till thou come unto Gaza, and left no sustenance for Israel, neither sheep, nor ox, nor ass.",
      "M": "They would encamp against them and devour the produce of the land, as far as Gaza, and leave no sustenance in Israel and no sheep or ox or donkey.",
      "T": "They swept through all the way to Gaza, consuming everything—every crop, every animal. They left Israel nothing."
    },
    "5": {
      "L": "For they came up with their cattle and their tents, and they came as grasshoppers for multitude; for both they and their camels were without number: and they entered into the land to destroy it.",
      "M": "For they would come up with their livestock and their tents; they would come like locusts in number—both they and their camels could not be counted—so that they laid waste the land as they came in.",
      "T": "They came in like a locust swarm—camels and tents beyond counting—and left the land stripped bare."
    },
    "6": {
      "L": "And Israel was greatly impoverished because of the Midianites; and the children of Israel cried unto the LORD.",
      "M": "And Israel was brought very low because of Midian. And the people of Israel cried out for help to the LORD.",
      "T": "Israel was reduced to destitution. They cried out to the LORD."
    },
    "7": {
      "L": "And it came to pass, when the children of Israel cried unto the LORD because of the Midianites,",
      "M": "When the people of Israel cried out to the LORD on account of the Midianites,",
      "T": "When Israel's cry reached the LORD because of Midian,"
    },
    "8": {
      "L": "That the LORD sent a prophet unto the children of Israel, which said unto them, Thus saith the LORD God of Israel, I brought you up from Egypt, and brought you forth out of the house of bondage;",
      "M": "the LORD sent a prophet to the people of Israel. And he said to them, \"Thus says the LORD, the God of Israel: I led you up from Egypt and brought you out of the house of slavery.",
      "T": "the LORD sent a prophet who delivered this word: \"Thus says the LORD, God of Israel: I brought you out of Egypt, out of the slave-house."
    },
    "9": {
      "L": "And I delivered you out of the hand of the Egyptians, and out of the hand of all that oppressed you, and drave them out from before you, and gave you their land;",
      "M": "And I delivered you from the hand of the Egyptians and from the hand of all who oppressed you, and drove them out before you and gave you their land.",
      "T": "\"I rescued you from every oppressor, cleared them from before you, and gave you their land."
    },
    "10": {
      "L": "And I said unto you, I am the LORD your God; fear not the gods of the Amorites, in whose land ye dwell: but ye have not obeyed my voice.",
      "M": "And I said to you, 'I am the LORD your God; you shall not fear the gods of the Amorites in whose land you dwell.' But you have not obeyed my voice.\"",
      "T": "\"I told you: I am the LORD your God—do not fear the gods of the Amorites in whose land you now live. But you have not listened.\" The indictment came before the deliverer."
    },
    "11": {
      "L": "And there came an angel of the LORD, and sat under an oak which was in Ophrah, that pertained unto Joash the Abiezrite: and his son Gideon threshed wheat by the winepress, to hide it from the Midianites.",
      "M": "Now the angel of the LORD came and sat under the terebinth at Ophrah, which belonged to Joash the Abiezrite, while his son Gideon was beating wheat in the winepress to hide it from the Midianites.",
      "T": "Then the angel of the LORD came and sat under the great tree at Ophrah—the estate of Joash the Abiezrite. His son Gideon was threshing wheat inside the winepress—hidden from Midianite raiders."
    },
    "12": {
      "L": "And the angel of the LORD appeared unto him, and said unto him, The LORD is with thee, thou mighty man of valour.",
      "M": "And the angel of the LORD appeared to him and said to him, \"The LORD is with you, O mighty man of valor.\"",
      "T": "The angel of the LORD appeared to him and said, \"The LORD is with you, mighty warrior.\""
    },
    "13": {
      "L": "And Gideon said unto him, Oh my Lord, if the LORD be with us, why then is all this befallen us? and where be all his miracles which our fathers told us of, saying, Did not the LORD bring us up from Egypt? but now the LORD hath forsaken us, and delivered us into the hands of the Midianites.",
      "M": "And Gideon said to him, \"Please, my lord, if the LORD is with us, why then has all this happened to us? And where are all his wonderful deeds that our fathers recounted to us, saying, 'Did not the LORD bring us up from Egypt?' But now the LORD has forsaken us and given us into the hand of Midian.\"",
      "T": "Gideon answered, \"With respect, my lord—if the LORD is with us, why is all this happening? Where are the miracles our ancestors talked about? 'The LORD brought us out of Egypt,' they said. But now the LORD has abandoned us to Midian.\""
    },
    "14": {
      "L": "And the LORD looked upon him, and said, Go in this thy might, and thou shalt save Israel from the hand of the Midianites: have not I sent thee?",
      "M": "And the LORD turned to him and said, \"Go in this might of yours and save Israel from the hand of Midian; do not I send you?\"",
      "T": "The LORD turned and looked directly at him: \"Go in the strength you have. Deliver Israel from Midian's hand. Am I not the one who sends you?\""
    },
    "15": {
      "L": "And he said unto him, Oh my Lord, wherewith shall I save Israel? behold, my family is poor in Manasseh, and I am the least in my father's house.",
      "M": "And he said to him, \"Please, Lord, how can I save Israel? Behold, my clan is the weakest in Manasseh, and I am the least in my father's house.\"",
      "T": "Gideon said, \"But Lord—how can I save Israel? My clan is the weakest in Manasseh, and I am the least person in my family.\""
    },
    "16": {
      "L": "And the LORD said unto him, Surely I will be with thee, and thou shalt smite the Midianites as one man.",
      "M": "And the LORD said to him, \"But I will be with you, and you shall strike the Midianites as one man.\"",
      "T": "The LORD said, \"I will be with you. You will strike down Midian as if it were a single man.\""
    },
    "17": {
      "L": "And he said unto him, If now I have found grace in thy sight, then shew me a sign that thou talkest with me.",
      "M": "And he said to him, \"If now I have found favor in your eyes, then show me a sign that it is you who speaks with me.",
      "T": "Gideon said, \"If I have truly found favor with you, give me a sign that it is really you speaking.\""
    },
    "18": {
      "L": "Depart not hence, I pray thee, until I come unto thee, and bring forth my present, and set it before thee. And he said, I will tarry until thou come again.",
      "M": "Please do not depart from here until I come to you and bring out my offering and set it before you.\" And he said, \"I will stay until you return.\"",
      "T": "\"Don't leave until I come back with an offering to set before you.\" The angel said, \"I will wait.\""
    },
    "19": {
      "L": "And Gideon went in, and made ready a kid, and unleavened cakes of an ephah of flour: the flesh he put in a basket, and he put the broth in a pot, and brought it out unto him under the oak, and presented it.",
      "M": "So Gideon went into his house and prepared a young goat and unleavened cakes from an ephah of flour. The meat he put in a basket, and the broth he put in a pot, and brought them to him under the terebinth and presented them.",
      "T": "Gideon went inside and prepared a young goat and a large batch of unleavened bread—the kind prepared for a guest of honor. He brought the meat in a basket and the broth in a pot to the angel under the tree."
    },
    "20": {
      "L": "And the angel of God said unto him, Take the flesh and the unleavened cakes, and lay them upon this rock, and pour out the broth. And he did so.",
      "M": "And the angel of God said to him, \"Take the meat and the unleavened cakes, and put them on this rock, and pour the broth over them.\" And he did so.",
      "T": "The angel of God said, \"Put the meat and the bread on that rock and pour the broth over them.\" Gideon did it."
    },
    "21": {
      "L": "Then the angel of the LORD put forth the end of the staff that was in his hand, and touched the flesh and the unleavened cakes; and there rose up fire out of the rock, and consumed the flesh and the unleavened cakes. Then the angel of the LORD departed out of his sight.",
      "M": "Then the angel of the LORD reached out the tip of the staff that was in his hand and touched the meat and the unleavened cakes. And fire sprang up from the rock and consumed the meat and the unleavened cakes. And the angel of the LORD vanished from his sight.",
      "T": "The angel touched the meat and bread with the tip of his staff. Fire blazed up from the rock and consumed the offering—and then the angel of the LORD was gone."
    },
    "22": {
      "L": "And when Gideon perceived that he was an angel of the LORD, Gideon said, Alas, O Lord GOD! for because I have seen an angel of the LORD face to face.",
      "M": "Then Gideon perceived that he was the angel of the LORD. And Gideon said, \"Alas, O Lord GOD! For now I have seen the angel of the LORD face to face.\"",
      "T": "Then Gideon understood what he had encountered. He cried out, \"Alas, O Lord GOD! I have seen the angel of the LORD face to face—and no one survives that!\""
    },
    "23": {
      "L": "And the LORD said unto him, Peace be unto thee; fear not: thou shalt not die.",
      "M": "But the LORD said to him, \"Peace be to you. Do not fear; you shall not die.\"",
      "T": "But the LORD spoke: \"Peace. Don't be afraid. You will not die.\""
    },
    "24": {
      "L": "Then Gideon built an altar there unto the LORD, and called it Jehovahshalom: unto this day it is yet in Ophrah of the Abiezrites.",
      "M": "Then Gideon built an altar there to the LORD and called it, The LORD Is Peace. To this day it still stands at Ophrah, which belongs to the Abiezrites.",
      "T": "Gideon built an altar there and named it Yahweh-Shalom—\"The LORD is Peace.\" It stood at Ophrah among the Abiezrites, a lasting mark of this encounter."
    },
    "25": {
      "L": "And it came to pass the same night, that the LORD said unto him, Take thy father's young bullock, even the second bullock of seven years old, and throw down the altar of Baal that thy father hath, and cut down the grove that is by it:",
      "M": "That night the LORD said to him, \"Take your father's bull, the second bull seven years old, and pull down the altar of Baal that your father has, and cut down the Asherah pole that is beside it,",
      "T": "That same night the LORD gave Gideon his first assignment: \"Take your father's second bull—the seven-year-old—and tear down your father's altar to Baal. Cut down the Asherah pole beside it."
    },
    "26": {
      "L": "And build an altar unto the LORD thy God upon the top of this rock, in the ordered place, and take the second bullock, and offer a burnt sacrifice with the wood of the grove which thou shalt cut down.",
      "M": "and build an altar to the LORD your God on the top of the stronghold here, with stones laid in due order. Then take the second bull and offer it as a burnt offering with the wood of the Asherah that you shall cut down.\"",
      "T": "\"Then build a proper altar to the LORD your God on top of this height—stones laid in order. Use the wood from the Asherah pole to burn the bull as an offering.\" The first act of calling was to dismantle the false before building the true."
    },
    "27": {
      "L": "Then Gideon took ten men of his servants, and did as the LORD had said unto him: and so it was, because he feared his father's household, and the men of the city, that he could not do it by day, that he did it by night.",
      "M": "So Gideon took ten men of his servants and did as the LORD had told him. But because he was too afraid of his father's family and the men of the town to do it by day, he did it by night.",
      "T": "Gideon obeyed—with ten servants. But he waited for darkness. He was afraid of what his family and the townspeople would do."
    },
    "28": {
      "L": "And when the men of the city arose early in the morning, behold, the altar of Baal was cast down, and the grove was cut down that was by it, and the second bullock was offered upon the altar that was built.",
      "M": "When the men of the town rose early in the morning, behold, the altar of Baal was broken down, and the Asherah beside it was cut down, and the second bull was offered on the newly built altar.",
      "T": "When morning came, the townspeople found the altar of Baal smashed, the Asherah pole felled, and a fresh bull sacrifice burning on a new altar to the LORD."
    },
    "29": {
      "L": "And they said one to another, Who hath done this thing? And when they enquired and asked, they said, Gideon the son of Joash hath done this thing.",
      "M": "And they said to one another, \"Who has done this thing?\" And after they had searched and inquired, they said, \"Gideon the son of Joash has done this thing.\"",
      "T": "The townspeople demanded, \"Who did this?\" The investigation led straight to Gideon son of Joash."
    },
    "30": {
      "L": "Then the men of the city said unto Joash, Bring out thy son, that he may die: because he hath cast down the altar of Baal, and because he hath cut down the grove that was by it.",
      "M": "Then the men of the town said to Joash, \"Bring out your son, that he may die, for he has broken down the altar of Baal and cut down the Asherah beside it.\"",
      "T": "The men of the town came to Joash: \"Hand over your son—he must die for tearing down Baal's altar and cutting down the Asherah.\""
    },
    "31": {
      "L": "And Joash said unto all that stood against him, Will ye plead for Baal? or will ye save him? he that will plead for him, let him be put to death whilst it is yet morning: if he be a god, let him plead for himself, because one hath cast down his altar.",
      "M": "But Joash said to all who stood against him, \"Will you contend for Baal? Or will you save him? Whoever contends for him shall be put to death by morning. If he is a god, let him contend for himself, because his altar has been broken down.\"",
      "T": "Joash turned on the crowd: \"Are you going to fight Baal's battles for him? Whoever defends Baal dies before morning. If he is truly a god, he can defend himself—his altar was knocked down!\""
    },
    "32": {
      "L": "Therefore on that day he called him Jerubbaal, saying, Let Baal plead against him, because he hath thrown down his altar.",
      "M": "Therefore on that day Gideon was called Jerubbaal, that is to say, \"Let Baal contend against him,\" because he had broken down his altar.",
      "T": "From that day Gideon was called Jerubbaal—\"Let Baal contest him\"—because he had torn down the altar."
    },
    "33": {
      "L": "Then all the Midianites and the Amalekites and the children of the east were gathered together, and went over, and pitched in the valley of Jezreel.",
      "M": "Now all the Midianites and the Amalekites and the people of the East came together, and they crossed the Jordan and encamped in the Valley of Jezreel.",
      "T": "Then the Midianite coalition—Midianites, Amalekites, and all the eastern tribes—crossed the Jordan and massed in the Jezreel Valley."
    },
    "34": {
      "L": "But the Spirit of the LORD came upon Gideon, and he blew a trumpet; and Abiezer was gathered after him.",
      "M": "But the Spirit of the LORD clothed Gideon, and he sounded the trumpet, and the Abiezrites were called out to follow him.",
      "T": "Then the Spirit of the LORD wrapped itself around Gideon—clothed him like a garment. He blew the trumpet, and the men of Abiezer rallied behind him."
    },
    "35": {
      "L": "And he sent messengers throughout all Manasseh; who also was gathered after him: and he sent messengers unto Asher, and unto Zebulun, and unto Naphtali; and they came up to meet them.",
      "M": "And he sent messengers throughout all Manasseh, and they too were called out to follow him. And he sent messengers to Asher, Zebulun, and Naphtali, and they came up to meet them.",
      "T": "He sent runners through all Manasseh—they rallied. He sent to Asher, Zebulun, and Naphtali—they came up to join him."
    },
    "36": {
      "L": "And Gideon said unto God, If thou wilt save Israel by mine hand, as thou hast said,",
      "M": "And Gideon said to God, \"If you will save Israel by my hand, as you have said,",
      "T": "Then Gideon said to God, \"If you are truly going to deliver Israel through me, as you said—"
    },
    "37": {
      "L": "Behold, I will put a fleece of wool in the floor; and if the dew be on the fleece only, and it be dry upon all the earth beside, then shall I know that thou wilt save Israel by mine hand, as thou hast said.",
      "M": "behold, I am laying a fleece of wool on the threshing floor. If there is dew on the fleece alone, and it is dry on all the ground, then I shall know that you will save Israel by my hand, as you have said.\"",
      "T": "\"—let me test it: I'll lay a wool fleece on the threshing floor tonight. If the fleece is wet with dew and the ground is dry, I'll know you mean to save Israel through me.\""
    },
    "38": {
      "L": "And it was so: for he rose up early on the morrow, and thrust the fleece together, and wringed the dew out of the fleece, a bowl full of water.",
      "M": "And it was so. When he rose early next morning and squeezed the fleece, he wrung enough dew from the fleece to fill a bowl with water.",
      "T": "And it was so. Next morning he squeezed the fleece—a full bowl of water wrung from it, while the ground around it was dry."
    },
    "39": {
      "L": "And Gideon said unto God, Let not thine anger be hot against me, and I will speak but this once: let me prove, I pray thee, but this once with the fleece; let it now be dry only upon the fleece, and upon all the ground let there be dew.",
      "M": "Then Gideon said to God, \"Let not your anger burn against me; let me speak just once more. Please let me test just once more with the fleece. Please let it be dry on the fleece only, and on all the ground let there be dew.\"",
      "T": "Gideon said, \"Don't be angry with me—but let me ask once more. This time let the fleece be dry and the ground wet with dew.\""
    },
    "40": {
      "L": "And God did so that night: for it was dry upon the fleece only, and there was dew on all the ground.",
      "M": "And God did so that night; and it was dry on the fleece only, and on all the ground there was dew.",
      "T": "God did it that night. The fleece lay dry; dew covered all the ground around it. Gideon's hesitation had been met with patience."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'judges')
        merge_tier(existing, JUDGES, tier_key)
        save(tier_dir, 'judges', existing)
    print('Judges 1–6 written.')

if __name__ == '__main__':
    main()
