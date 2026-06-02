"""
MKT Numbers chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-numbers-1-6.py

Covers: census of the twelve tribes at Sinai (ch. 1), arrangement of the camp by tribal
standards (ch. 2), census and duties of the Levites as substitute for the firstborn (ch. 3),
service assignments for Kohath/Gershon/Merari ages 30–50 (ch. 4), expulsion of the impure
and the sotah ordeal for suspected adultery (ch. 5), the Nazirite vow with the Aaronic
blessing (ch. 6).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — consistent with Leviticus/Exodus
- H430 (אֱלֹהִים): "God" in all tiers
- H168 + H4150 (אֹהֶל מוֹעֵד): "tent of meeting" in all tiers
- H4908 (מִשְׁכָּן): "tabernacle" in L/M; "dwelling" in T where covenant-presence sense is foregrounded
- H6485 (פָּקַד): L="number", M="enroll/count", T="muster" — the verb carries military review connotation;
  the Niphal הַפְּקֻדִים = "those mustered/enrolled"
- H5387 (נָשִׂיא): L="prince", M="leader", T="chieftain" — clan head, not a royal title
- H6635 (צָבָא): L="host", M="army", T="fighting force" — this is a military census
- H1714 (דֶּגֶל): L/M="standard", T="battle standard"
- H5712 (עֵדָה): "congregation" in L/M; "community" in T
- H5315 (נֶפֶשׁ): "person" in legal/penalty clauses — not a disembodied soul
- H5139 (נָזִיר): L="Nazarite", M="Nazirite", T="one consecrated"
- H7965 (שָׁלוֹם): "peace" in L/M; "wholeness and peace" in T at 6:26 — shalom is comprehensive well-being
- H7307 (רוּחַ): at 5:14 "spirit of jealousy" — L/M="spirit of jealousy", T="surge of jealous suspicion"
- H1288 (בָּרַךְ): "bless" in all tiers
- H8104 (שָׁמַר): "keep/guard" in all tiers — the keeping is protective
- Aaronic blessing (6:24–26): one of the oldest attested Hebrew texts (Ketef Hinnom amulets, ~600 BCE);
  three progressively expansive lines; "make his face shine" = radiant divine favor;
  "lift up his face" = favorable regard, opposite of "hiding the face" which signals rejection
- Sotah rite (5:11–31): a public ordeal functioning as a divine verdict; God is the judge when
  human evidence is absent; the bitter water either convicts or exonerates
- Kohathite danger (4:15–20): touching the uncovered holy objects means death; the layered
  coverings are not merely practical but protective — the holiness of God requires mediation
- Firstborn exchange (3:12–13, 3:40–51): the Levites replace the firstborn claimed at Passover;
  the 273 excess firstborns are redeemed at 5 shekels each = 1,365 shekels total
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
  "1": {
    "1": {
      "L": "And the LORD spoke unto Moses in the wilderness of Sinai, in the tent of meeting, on the first day of the second month, in the second year after they came out of the land of Egypt, saying,",
      "M": "The LORD spoke to Moses in the wilderness of Sinai, in the tent of meeting, on the first day of the second month in the second year after they came out of the land of Egypt, saying,",
      "T": "The LORD spoke to Moses from the tent of meeting in the wilderness of Sinai — on the first of the second month, in the second year after the exodus — saying,"
    },
    "2": {
      "L": "Take ye the sum of all the congregation of the children of Israel, by their families, by their ancestral houses, according to the number of names, every male, by their skulls;",
      "M": "Take a census of the entire congregation of Israel, by their clans and their ancestral houses, counting every male by name, head by head.",
      "T": "Take a full count of all the Israelite community — by clans, by ancestral households — recording by name every male, one by one."
    },
    "3": {
      "L": "From twenty years old and upward, all who are able to go out to the host in Israel — you and Aaron shall number them by their armies.",
      "M": "Number all in Israel who are twenty years old or more and able to serve in the army. You and Aaron shall enroll them regiment by regiment.",
      "T": "Every man twenty years and older who is fit for military service — you and Aaron shall muster them into their fighting companies."
    },
    "4": {
      "L": "And with you there shall be a man of each tribe, each man being the head of his ancestral house.",
      "M": "With you shall stand one man from each tribe, each the head of his ancestral house.",
      "T": "One man from every tribe shall stand beside you — each the recognized head of his family's line."
    },
    "5": {
      "L": "And these are the names of the men who shall stand with you: of Reuben, Elizur son of Shedeur;",
      "M": "These are the names of the men who shall stand with you: from Reuben, Elizur son of Shedeur;",
      "T": "These are the men appointed to stand with you: from Reuben, Elizur son of Shedeur;"
    },
    "6": {
      "L": "Of Simeon, Shelumiel son of Zurishaddai;",
      "M": "from Simeon, Shelumiel son of Zurishaddai;",
      "T": "from Simeon, Shelumiel son of Zurishaddai;"
    },
    "7": {
      "L": "Of Judah, Nahshon son of Amminadab;",
      "M": "from Judah, Nahshon son of Amminadab;",
      "T": "from Judah, Nahshon son of Amminadab;"
    },
    "8": {
      "L": "Of Issachar, Nethanel son of Zuar;",
      "M": "from Issachar, Nethanel son of Zuar;",
      "T": "from Issachar, Nethanel son of Zuar;"
    },
    "9": {
      "L": "Of Zebulun, Eliab son of Helon;",
      "M": "from Zebulun, Eliab son of Helon;",
      "T": "from Zebulun, Eliab son of Helon;"
    },
    "10": {
      "L": "Of the sons of Joseph: of Ephraim, Elishama son of Ammihud; of Manasseh, Gamaliel son of Pedahzur;",
      "M": "from the sons of Joseph: from Ephraim, Elishama son of Ammihud; from Manasseh, Gamaliel son of Pedahzur;",
      "T": "from Joseph's line: from Ephraim, Elishama son of Ammihud; from Manasseh, Gamaliel son of Pedahzur;"
    },
    "11": {
      "L": "Of Benjamin, Abidan son of Gideoni;",
      "M": "from Benjamin, Abidan son of Gideoni;",
      "T": "from Benjamin, Abidan son of Gideoni;"
    },
    "12": {
      "L": "Of Dan, Ahiezer son of Ammishaddai;",
      "M": "from Dan, Ahiezer son of Ammishaddai;",
      "T": "from Dan, Ahiezer son of Ammishaddai;"
    },
    "13": {
      "L": "Of Asher, Pagiel son of Ochran;",
      "M": "from Asher, Pagiel son of Ochran;",
      "T": "from Asher, Pagiel son of Ochran;"
    },
    "14": {
      "L": "Of Gad, Eliasaph son of Deuel;",
      "M": "from Gad, Eliasaph son of Deuel;",
      "T": "from Gad, Eliasaph son of Deuel;"
    },
    "15": {
      "L": "Of Naphtali, Ahira son of Enan.",
      "M": "from Naphtali, Ahira son of Enan.",
      "T": "from Naphtali, Ahira son of Enan."
    },
    "16": {
      "L": "These were the chosen of the congregation, the leaders of the tribes of their fathers, the heads of the thousands of Israel.",
      "M": "These were the designated leaders of the congregation, the chiefs of their ancestral tribes, the heads of the clans of Israel.",
      "T": "These were Israel's appointed spokesmen — the tribal heads, each the commanding figure of his people's clan."
    },
    "17": {
      "L": "And Moses and Aaron took these men, who are named by their names.",
      "M": "Moses and Aaron took these men who had been designated by name,",
      "T": "Moses and Aaron gathered the men who had been named,"
    },
    "18": {
      "L": "and they assembled all the congregation together on the first day of the second month, and they registered their descent by their families, by their ancestral houses, according to the number of names from twenty years old and upward, head by head.",
      "M": "and assembled the entire congregation on the first day of the second month. The people declared their ancestry by their clans and ancestral houses, and all males twenty years old and upward were counted one by one.",
      "T": "and convened the full community on the first of the second month. Each person traced his lineage by clan and ancestral household; every male twenty and older was registered individually."
    },
    "19": {
      "L": "As the LORD commanded Moses, so he numbered them in the wilderness of Sinai.",
      "M": "Just as the LORD had commanded Moses, so he counted them in the wilderness of Sinai.",
      "T": "Moses conducted the census in the wilderness of Sinai, exactly as the LORD had commanded."
    },
    "20": {
      "L": "And the children of Reuben, Israel's firstborn, their generations by their families, by their ancestral houses, according to the number of names, every male head by head, from twenty years old and upward, all who were able to go to war —",
      "M": "The descendants of Reuben — Israel's firstborn — recorded by their families, by their ancestral houses, by the count of their names, every male twenty years and older who was able to serve in the army —",
      "T": "Reuben, firstborn of Israel: men registered by clan and ancestral household, every male twenty and older fit for battle —"
    },
    "21": {
      "L": "those numbered of them, of the tribe of Reuben, were forty-six thousand five hundred.",
      "M": "those enrolled from the tribe of Reuben were forty-six thousand five hundred.",
      "T": "the muster of Reuben: forty-six thousand five hundred."
    },
    "22": {
      "L": "Of the children of Simeon, their generations by their families, by their ancestral houses, those numbered of them, according to the number of names, every male head by head, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Simeon, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Simeon: registered by clan and household, every male twenty and older fit for battle —"
    },
    "23": {
      "L": "those numbered of them, of the tribe of Simeon, were fifty-nine thousand three hundred.",
      "M": "those enrolled from the tribe of Simeon were fifty-nine thousand three hundred.",
      "T": "the muster of Simeon: fifty-nine thousand three hundred."
    },
    "24": {
      "L": "Of the children of Gad, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Gad, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Gad: registered by clan and household, every male twenty and older fit for battle —"
    },
    "25": {
      "L": "those numbered of them, of the tribe of Gad, were forty-five thousand six hundred and fifty.",
      "M": "those enrolled from the tribe of Gad were forty-five thousand six hundred and fifty.",
      "T": "the muster of Gad: forty-five thousand six hundred and fifty."
    },
    "26": {
      "L": "Of the children of Judah, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Judah, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Judah: registered by clan and household, every male twenty and older fit for battle —"
    },
    "27": {
      "L": "those numbered of them, of the tribe of Judah, were seventy-four thousand six hundred.",
      "M": "those enrolled from the tribe of Judah were seventy-four thousand six hundred.",
      "T": "the muster of Judah: seventy-four thousand six hundred — the largest of the eastern camp."
    },
    "28": {
      "L": "Of the children of Issachar, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Issachar, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Issachar: registered by clan and household, every male twenty and older fit for battle —"
    },
    "29": {
      "L": "those numbered of them, of the tribe of Issachar, were fifty-four thousand four hundred.",
      "M": "those enrolled from the tribe of Issachar were fifty-four thousand four hundred.",
      "T": "the muster of Issachar: fifty-four thousand four hundred."
    },
    "30": {
      "L": "Of the children of Zebulun, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Zebulun, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Zebulun: registered by clan and household, every male twenty and older fit for battle —"
    },
    "31": {
      "L": "those numbered of them, of the tribe of Zebulun, were fifty-seven thousand four hundred.",
      "M": "those enrolled from the tribe of Zebulun were fifty-seven thousand four hundred.",
      "T": "the muster of Zebulun: fifty-seven thousand four hundred."
    },
    "32": {
      "L": "Of the children of Joseph, of the children of Ephraim, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Joseph — the descendants of Ephraim — recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Ephraim, from the house of Joseph: registered by clan and household, every male twenty and older fit for battle —"
    },
    "33": {
      "L": "those numbered of them, of the tribe of Ephraim, were forty thousand five hundred.",
      "M": "those enrolled from the tribe of Ephraim were forty thousand five hundred.",
      "T": "the muster of Ephraim: forty thousand five hundred."
    },
    "34": {
      "L": "Of the children of Joseph, of the children of Manasseh, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Joseph — the descendants of Manasseh — recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Manasseh, also from the house of Joseph: registered by clan and household, every male twenty and older fit for battle —"
    },
    "35": {
      "L": "those numbered of them, of the tribe of Manasseh, were thirty-two thousand two hundred.",
      "M": "those enrolled from the tribe of Manasseh were thirty-two thousand two hundred.",
      "T": "the muster of Manasseh: thirty-two thousand two hundred."
    },
    "36": {
      "L": "Of the children of Benjamin, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Benjamin, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Benjamin: registered by clan and household, every male twenty and older fit for battle —"
    },
    "37": {
      "L": "those numbered of them, of the tribe of Benjamin, were thirty-five thousand four hundred.",
      "M": "those enrolled from the tribe of Benjamin were thirty-five thousand four hundred.",
      "T": "the muster of Benjamin: thirty-five thousand four hundred."
    },
    "38": {
      "L": "Of the children of Dan, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Dan, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Dan: registered by clan and household, every male twenty and older fit for battle —"
    },
    "39": {
      "L": "those numbered of them, of the tribe of Dan, were sixty-two thousand seven hundred.",
      "M": "those enrolled from the tribe of Dan were sixty-two thousand seven hundred.",
      "T": "the muster of Dan: sixty-two thousand seven hundred."
    },
    "40": {
      "L": "Of the children of Asher, their generations by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Asher, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Asher: registered by clan and household, every male twenty and older fit for battle —"
    },
    "41": {
      "L": "those numbered of them, of the tribe of Asher, were forty-one thousand five hundred.",
      "M": "those enrolled from the tribe of Asher were forty-one thousand five hundred.",
      "T": "the muster of Asher: forty-one thousand five hundred."
    },
    "42": {
      "L": "Of the children of Naphtali, throughout their generations, by their families, by their ancestral houses, according to the number of names, from twenty years old and upward, all who were able to go to war —",
      "M": "From the descendants of Naphtali, throughout their generations, recorded by their families and ancestral houses, every male twenty years and older who was able to serve in the army —",
      "T": "Naphtali: registered by clan and household, every male twenty and older fit for battle —"
    },
    "43": {
      "L": "those numbered of them, of the tribe of Naphtali, were fifty-three thousand four hundred.",
      "M": "those enrolled from the tribe of Naphtali were fifty-three thousand four hundred.",
      "T": "the muster of Naphtali: fifty-three thousand four hundred."
    },
    "44": {
      "L": "These are those who were numbered, whom Moses and Aaron numbered, with the princes of Israel, twelve men, each one for his ancestral house.",
      "M": "These are those enrolled — Moses and Aaron and the twelve leaders of Israel, one man per ancestral house, who conducted the enrollment.",
      "T": "These were counted by Moses, Aaron, and the twelve tribal chieftains — one per ancestral house — each responsible for his own people's muster."
    },
    "45": {
      "L": "And all the children of Israel who were numbered, by their ancestral houses, from twenty years old and upward, all who were able to go to war in Israel —",
      "M": "All the Israelites twenty years and older who were able to serve in the army, enrolled by their ancestral houses —",
      "T": "All Israelites twenty and older who were fit for battle, registered by ancestral households —"
    },
    "46": {
      "L": "all those numbered were six hundred and three thousand five hundred and fifty.",
      "M": "the total enrolled was six hundred three thousand five hundred and fifty.",
      "T": "came to six hundred three thousand five hundred and fifty men — Israel's fighting force at Sinai."
    },
    "47": {
      "L": "But the Levites according to the tribe of their fathers were not numbered among them.",
      "M": "The Levites, however, were not enrolled among them by their ancestral tribe.",
      "T": "The Levites alone were not enrolled in this military census — they stood apart by God's design."
    },
    "48": {
      "L": "For the LORD had spoken unto Moses, saying,",
      "M": "For the LORD had said to Moses,",
      "T": "For the LORD had instructed Moses:"
    },
    "49": {
      "L": "Only the tribe of Levi you shall not number, nor take their sum among the children of Israel.",
      "M": "Do not count the tribe of Levi or include them in the census of the Israelites.",
      "T": "Do not number Levi or include them in the count of Israel's fighting men."
    },
    "50": {
      "L": "But thou shalt appoint the Levites over the tabernacle of the testimony, and over all the vessels thereof, and over all things that belong to it; they shall bear the tabernacle and all the vessels thereof, and they shall minister unto it, and shall encamp round about the tabernacle.",
      "M": "Instead, appoint the Levites over the tabernacle of the testimony, over all its furnishings and all that belongs to it. They shall carry the tabernacle and all its vessels, they shall minister to it, and they shall camp around it.",
      "T": "Assign the Levites instead to the tabernacle of the covenant: they will bear it, tend all its furnishings, perform its service, and encamp as its living guard on every side."
    },
    "51": {
      "L": "And when the tabernacle sets out, the Levites shall take it down; and when the tabernacle is to be pitched, the Levites shall set it up; and the stranger who comes near shall be put to death.",
      "M": "When the tabernacle moves, the Levites shall take it apart; when it is to be set up, the Levites shall erect it. Any unauthorized person who comes near shall be put to death.",
      "T": "When the camp moves, Levites dismantle and carry the tabernacle; when the camp halts, they erect it again. Any outsider who approaches it dies."
    },
    "52": {
      "L": "The children of Israel shall pitch their tents, every man by his own camp and every man by his own standard, by their armies.",
      "M": "The Israelites shall camp each by his own company, each person under his own tribal standard throughout their regiments.",
      "T": "Each Israelite camps by his own unit, under the battle standard of his tribe."
    },
    "53": {
      "L": "But the Levites shall encamp around the tabernacle of the testimony, that there may be no wrath upon the congregation of the children of Israel; and the Levites shall keep the charge of the tabernacle of the testimony.",
      "M": "The Levites shall camp around the tabernacle of the testimony so that wrath does not fall on the congregation of Israel; the Levites shall keep watch over the tabernacle of the testimony.",
      "T": "The Levites form a sacred perimeter around the tabernacle of the covenant — standing between the congregation and the holiness that would consume anyone who trespassed it. They bear responsibility for the tabernacle."
    },
    "54": {
      "L": "And the children of Israel did according to all that the LORD commanded Moses; so they did.",
      "M": "The Israelites did everything the LORD had commanded Moses; so they did.",
      "T": "The Israelites carried out every command the LORD had given Moses — completely and without exception."
    }
  },
  "2": {
    "1": {
      "L": "And the LORD spoke unto Moses and unto Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD gave Moses and Aaron this instruction:"
    },
    "2": {
      "L": "The children of Israel shall pitch their tents every man by his own standard, with the ensigns of their ancestral houses; they shall pitch far off around the tent of meeting.",
      "M": "The Israelites shall camp, each by his own standard and under the ensigns of his ancestral house, at a distance around the tent of meeting.",
      "T": "Every Israelite shall camp under his tribal banner, his family's ensign identifying his place — each unit encircling the tent of meeting from a respectful distance."
    },
    "3": {
      "L": "And on the east side, toward the rising of the sun, those of the standard of the camp of Judah shall pitch according to their armies; and the prince of Judah shall be Nahshon son of Amminadab.",
      "M": "On the east side, toward the sunrise, the standard of the camp of Judah shall camp by their regiments. The leader of Judah is Nahshon son of Amminadab.",
      "T": "On the east — the side of the sunrise — Judah's battle standard leads the first camp, with Nahshon son of Amminadab as its commander."
    },
    "4": {
      "L": "And his army, and those enrolled of them, were seventy-four thousand six hundred.",
      "M": "Those enrolled in his regiment were seventy-four thousand six hundred.",
      "T": "Judah's muster: seventy-four thousand six hundred."
    },
    "5": {
      "L": "And those who encamp next to him shall be the tribe of Issachar; and the prince of Issachar shall be Nethanel son of Zuar.",
      "M": "Camping next to them shall be the tribe of Issachar, with Nethanel son of Zuar as its leader.",
      "T": "Encamped alongside Judah: Issachar, under Nethanel son of Zuar."
    },
    "6": {
      "L": "And his army, and those enrolled of them, were fifty-four thousand four hundred.",
      "M": "Those enrolled were fifty-four thousand four hundred.",
      "T": "Issachar's muster: fifty-four thousand four hundred."
    },
    "7": {
      "L": "Then the tribe of Zebulun; and the prince of Zebulun shall be Eliab son of Helon.",
      "M": "Then the tribe of Zebulun, with Eliab son of Helon as its leader.",
      "T": "And Zebulun alongside them, under Eliab son of Helon."
    },
    "8": {
      "L": "And his army, and those enrolled of them, were fifty-seven thousand four hundred.",
      "M": "Those enrolled were fifty-seven thousand four hundred.",
      "T": "Zebulun's muster: fifty-seven thousand four hundred."
    },
    "9": {
      "L": "All those enrolled of the camp of Judah were one hundred and eighty-six thousand four hundred, by their armies. They shall set out first.",
      "M": "The total enrolled in the camp of Judah was one hundred eighty-six thousand four hundred, by their regiments. They shall march first.",
      "T": "The eastern camp of Judah — Judah, Issachar, and Zebulun together — numbered one hundred eighty-six thousand four hundred. They lead the march."
    },
    "10": {
      "L": "On the south side shall be the standard of the camp of Reuben according to their armies; and the prince of Reuben shall be Elizur son of Shedeur.",
      "M": "On the south side, the standard of the camp of Reuben shall be by their regiments. The leader of Reuben is Elizur son of Shedeur.",
      "T": "On the south: Reuben's battle standard commands the second camp, with Elizur son of Shedeur as its chief."
    },
    "11": {
      "L": "And his army, and those enrolled of them, were forty-six thousand five hundred.",
      "M": "Those enrolled in his regiment were forty-six thousand five hundred.",
      "T": "Reuben's muster: forty-six thousand five hundred."
    },
    "12": {
      "L": "And those who encamp next to him shall be the tribe of Simeon; and the prince of Simeon shall be Shelumiel son of Zurishaddai.",
      "M": "Camping next to them shall be the tribe of Simeon, with Shelumiel son of Zurishaddai as its leader.",
      "T": "Alongside Reuben: Simeon, under Shelumiel son of Zurishaddai."
    },
    "13": {
      "L": "And his army, and those enrolled of them, were fifty-nine thousand three hundred.",
      "M": "Those enrolled were fifty-nine thousand three hundred.",
      "T": "Simeon's muster: fifty-nine thousand three hundred."
    },
    "14": {
      "L": "Then the tribe of Gad; and the prince of Gad shall be Eliasaph son of Reuel.",
      "M": "Then the tribe of Gad, with Eliasaph son of Reuel as its leader.",
      "T": "And Gad alongside them, under Eliasaph son of Reuel."
    },
    "15": {
      "L": "And his army, and those enrolled of them, were forty-five thousand six hundred and fifty.",
      "M": "Those enrolled were forty-five thousand six hundred and fifty.",
      "T": "Gad's muster: forty-five thousand six hundred and fifty."
    },
    "16": {
      "L": "All those enrolled of the camp of Reuben were one hundred and fifty-one thousand four hundred and fifty, by their armies. They shall set out second.",
      "M": "The total enrolled in the camp of Reuben was one hundred fifty-one thousand four hundred and fifty, by their regiments. They shall march second.",
      "T": "The southern camp of Reuben — Reuben, Simeon, and Gad — numbered one hundred fifty-one thousand four hundred and fifty. They march second."
    },
    "17": {
      "L": "Then the tent of meeting shall set out, the camp of the Levites in the midst of the camps; as they camp, so they shall set out, every man in his place, by their standards.",
      "M": "The tent of meeting shall then move, with the Levite camp in the middle. Each person in his position, under their standards — as they camp, so they shall march.",
      "T": "In the center of the procession comes the tent of meeting, carried by the Levites. They march at Israel's heart, surrounded by the tribal camps, each unit moving in its ordained place."
    },
    "18": {
      "L": "On the west side shall be the standard of the camp of Ephraim according to their armies; and the prince of Ephraim shall be Elishama son of Ammihud.",
      "M": "On the west side, the standard of the camp of Ephraim shall be by their regiments. The leader of Ephraim is Elishama son of Ammihud.",
      "T": "On the west: Ephraim's standard leads the third camp, with Elishama son of Ammihud as its chief."
    },
    "19": {
      "L": "And his army, and those enrolled of them, were forty thousand five hundred.",
      "M": "Those enrolled in his regiment were forty thousand five hundred.",
      "T": "Ephraim's muster: forty thousand five hundred."
    },
    "20": {
      "L": "And next to him shall be the tribe of Manasseh; and the prince of Manasseh shall be Gamaliel son of Pedahzur.",
      "M": "Next to them shall be the tribe of Manasseh, with Gamaliel son of Pedahzur as its leader.",
      "T": "Alongside Ephraim: Manasseh, the brother tribe, under Gamaliel son of Pedahzur."
    },
    "21": {
      "L": "And his army, and those enrolled of them, were thirty-two thousand two hundred.",
      "M": "Those enrolled were thirty-two thousand two hundred.",
      "T": "Manasseh's muster: thirty-two thousand two hundred."
    },
    "22": {
      "L": "Then the tribe of Benjamin; and the prince of Benjamin shall be Abidan son of Gideoni.",
      "M": "Then the tribe of Benjamin, with Abidan son of Gideoni as its leader.",
      "T": "And Benjamin alongside them, under Abidan son of Gideoni."
    },
    "23": {
      "L": "And his army, and those enrolled of them, were thirty-five thousand four hundred.",
      "M": "Those enrolled were thirty-five thousand four hundred.",
      "T": "Benjamin's muster: thirty-five thousand four hundred."
    },
    "24": {
      "L": "All those enrolled of the camp of Ephraim were one hundred and eight thousand one hundred, by their armies. They shall set out third.",
      "M": "The total enrolled in the camp of Ephraim was one hundred eight thousand one hundred, by their regiments. They shall march third.",
      "T": "The western camp of Ephraim — Ephraim, Manasseh, and Benjamin — numbered one hundred eight thousand one hundred. They march third."
    },
    "25": {
      "L": "On the north side shall be the standard of the camp of Dan according to their armies; and the prince of Dan shall be Ahiezer son of Ammishaddai.",
      "M": "On the north side, the standard of the camp of Dan shall be by their regiments. The leader of Dan is Ahiezer son of Ammishaddai.",
      "T": "On the north: Dan's standard commands the rear camp, with Ahiezer son of Ammishaddai as its chief."
    },
    "26": {
      "L": "And his army, and those enrolled of them, were sixty-two thousand seven hundred.",
      "M": "Those enrolled in his regiment were sixty-two thousand seven hundred.",
      "T": "Dan's muster: sixty-two thousand seven hundred."
    },
    "27": {
      "L": "And those who encamp next to him shall be the tribe of Asher; and the prince of Asher shall be Pagiel son of Ochran.",
      "M": "Camping next to them shall be the tribe of Asher, with Pagiel son of Ochran as its leader.",
      "T": "Alongside Dan: Asher, under Pagiel son of Ochran."
    },
    "28": {
      "L": "And his army, and those enrolled of them, were forty-one thousand five hundred.",
      "M": "Those enrolled were forty-one thousand five hundred.",
      "T": "Asher's muster: forty-one thousand five hundred."
    },
    "29": {
      "L": "Then the tribe of Naphtali; and the prince of Naphtali shall be Ahira son of Enan.",
      "M": "Then the tribe of Naphtali, with Ahira son of Enan as its leader.",
      "T": "And Naphtali alongside them, under Ahira son of Enan."
    },
    "30": {
      "L": "And his army, and those enrolled of them, were fifty-three thousand four hundred.",
      "M": "Those enrolled were fifty-three thousand four hundred.",
      "T": "Naphtali's muster: fifty-three thousand four hundred."
    },
    "31": {
      "L": "All those enrolled of the camp of Dan were one hundred and fifty-seven thousand six hundred. They shall set out last, by their standards.",
      "M": "The total enrolled in the camp of Dan was one hundred fifty-seven thousand six hundred. They shall march last, by their standards.",
      "T": "The northern camp of Dan — Dan, Asher, and Naphtali — numbered one hundred fifty-seven thousand six hundred. They march as the rear guard, each under their standards."
    },
    "32": {
      "L": "These are those enrolled of the children of Israel by their ancestral houses; all those enrolled in the camps by their armies were six hundred and three thousand five hundred and fifty.",
      "M": "These are the Israelites enrolled by their ancestral houses. The total enrolled in all the camps, by their regiments, was six hundred three thousand five hundred and fifty.",
      "T": "All told, the Israelites registered by ancestral household — every fighting man across all four encampments — came to six hundred three thousand five hundred and fifty."
    },
    "33": {
      "L": "But the Levites were not enrolled among the children of Israel, as the LORD commanded Moses.",
      "M": "The Levites were not enrolled among the Israelites, as the LORD had commanded Moses.",
      "T": "The Levites remained uncounted in this census — just as the LORD had commanded Moses."
    },
    "34": {
      "L": "And the children of Israel did according to all that the LORD commanded Moses; so they camped by their standards, and so they set out, every man by his clan, according to his ancestral house.",
      "M": "The Israelites did everything the LORD had commanded Moses: they camped by their standards and they marched each by his clan, according to his ancestral house.",
      "T": "Israel obeyed entirely: they camped and marched as the LORD had ordered — each man under his clan's standard, each unit in its appointed place."
    }
  },
  "3": {
    "1": {
      "L": "Now these are the generations of Aaron and Moses in the day that the LORD spoke with Moses on Mount Sinai.",
      "M": "These are the descendants of Aaron and Moses at the time the LORD spoke with Moses on Mount Sinai.",
      "T": "This is the family record of Aaron and Moses from the time the LORD spoke to Moses at Sinai."
    },
    "2": {
      "L": "And these are the names of the sons of Aaron: Nadab the firstborn, and Abihu, Eleazar, and Ithamar.",
      "M": "The names of Aaron's sons were Nadab the firstborn, Abihu, Eleazar, and Ithamar.",
      "T": "Aaron's sons were Nadab — the firstborn — then Abihu, Eleazar, and Ithamar."
    },
    "3": {
      "L": "These are the names of the sons of Aaron, the anointed priests, whom he consecrated to minister in the priest's office.",
      "M": "These are the names of Aaron's sons, the anointed priests who were ordained to serve as priests.",
      "T": "These were Aaron's sons — anointed and installed in their priestly office to serve before God."
    },
    "4": {
      "L": "And Nadab and Abihu died before the LORD when they offered strange fire before the LORD in the wilderness of Sinai, and they had no children; and Eleazar and Ithamar ministered as priests in the presence of Aaron their father.",
      "M": "Nadab and Abihu died before the LORD when they offered unauthorized fire before the LORD in the wilderness of Sinai; they had no sons. So Eleazar and Ithamar served as priests during the lifetime of Aaron their father.",
      "T": "Nadab and Abihu died in the LORD's presence — struck down for offering unauthorized fire in the Sinai wilderness, leaving no sons. After them, Eleazar and Ithamar carried out the priestly ministry under their father Aaron's oversight."
    },
    "5": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "6": {
      "L": "Bring the tribe of Levi near and set them before Aaron the priest, that they may minister unto him.",
      "M": "Bring the tribe of Levi forward and present them to Aaron the priest, so they may serve him.",
      "T": "Bring the Levites forward and place them in service to Aaron the priest — assigned to assist him."
    },
    "7": {
      "L": "And they shall keep his charge and the charge of the whole congregation before the tent of meeting, to do the service of the tabernacle.",
      "M": "They shall fulfill the duties assigned to him and the entire congregation in front of the tent of meeting by performing the service of the tabernacle.",
      "T": "They will carry out Aaron's responsibilities and the congregation's obligations before the tent of meeting — managing the entire service of the dwelling."
    },
    "8": {
      "L": "And they shall keep all the furnishings of the tent of meeting, and the charge of the children of Israel, to do the service of the tabernacle.",
      "M": "They shall be responsible for all the furnishings of the tent of meeting and fulfill the duties of the Israelites by performing the service of the tabernacle.",
      "T": "They will care for every piece of equipment in the tent of meeting and perform the Israelites' sacred service on their behalf."
    },
    "9": {
      "L": "And thou shalt give the Levites unto Aaron and to his sons; they are wholly given unto him from the children of Israel.",
      "M": "Give the Levites to Aaron and his sons; they are wholly given to him from among the Israelites.",
      "T": "The Levites are given entirely to Aaron and his sons — a dedicated gift from the whole people of Israel."
    },
    "10": {
      "L": "And thou shalt appoint Aaron and his sons, and they shall keep their priesthood; and the stranger who comes near shall be put to death.",
      "M": "Appoint Aaron and his sons to serve; they shall maintain their priestly duties. Any unauthorized person who comes near shall be put to death.",
      "T": "Commission Aaron and his sons to guard the priesthood. Any outsider who intrudes into that sacred office is to be executed."
    },
    "11": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "12": {
      "L": "And I, behold, I have taken the Levites from among the children of Israel instead of every firstborn who opens the womb among the children of Israel; and the Levites shall be mine.",
      "M": "Behold, I have taken the Levites from among the Israelites as substitutes for every firstborn who opens the womb among the Israelites. The Levites shall be mine.",
      "T": "I myself have taken the Levites from Israel to stand in place of every firstborn son — the one who first opens the womb. They are mine."
    },
    "13": {
      "L": "For every firstborn is mine; on the day that I struck down all the firstborn in the land of Egypt, I consecrated to myself all the firstborn in Israel, both man and beast; they shall be mine; I am the LORD.",
      "M": "For every firstborn is mine; when I struck down all the firstborn in Egypt, I set apart for myself all the firstborn of Israel, human and animal alike. They are mine. I am the LORD.",
      "T": "Every firstborn belongs to me — I claimed them all when I struck down Egypt's firstborn. From that day, every firstborn of Israel, man and beast, is consecrated to me. I am the LORD."
    },
    "14": {
      "L": "And the LORD spoke unto Moses in the wilderness of Sinai, saying,",
      "M": "The LORD spoke to Moses in the wilderness of Sinai, saying,",
      "T": "The LORD spoke again to Moses in the Sinai wilderness:"
    },
    "15": {
      "L": "Number the children of Levi by their ancestral houses, by their families; every male from a month old and upward you shall number.",
      "M": "Count the Levites by their ancestral houses and families; count every male from a month old and upward.",
      "T": "Enroll the Levites by their ancestral households and clans — counting every male from a month old and older."
    },
    "16": {
      "L": "And Moses numbered them according to the word of the LORD, as he was commanded.",
      "M": "So Moses counted them just as the LORD had directed.",
      "T": "Moses obeyed, numbering them exactly as the LORD commanded."
    },
    "17": {
      "L": "And these were the sons of Levi by their names: Gershon, and Kohath, and Merari.",
      "M": "The sons of Levi by name were Gershon, Kohath, and Merari.",
      "T": "Levi's sons were three: Gershon, Kohath, and Merari."
    },
    "18": {
      "L": "And these are the names of the sons of Gershon by their families: Libni and Shimei.",
      "M": "The sons of Gershon by their clans were Libni and Shimei.",
      "T": "Gershon's sons were Libni and Shimei — the two clans of Gershon."
    },
    "19": {
      "L": "And the sons of Kohath by their families: Amram, and Izhar, Hebron, and Uzziel.",
      "M": "The sons of Kohath by their clans were Amram, Izhar, Hebron, and Uzziel.",
      "T": "Kohath's sons were Amram, Izhar, Hebron, and Uzziel — four clans."
    },
    "20": {
      "L": "And the sons of Merari by their families: Mahli and Mushi. These are the families of the Levites according to their ancestral houses.",
      "M": "The sons of Merari by their clans were Mahli and Mushi. These are the Levite clans according to their ancestral houses.",
      "T": "Merari's sons were Mahli and Mushi. These, then, are the Levite clans, each organized within its ancestral house."
    },
    "21": {
      "L": "Of Gershon was the family of the Libnites and the family of the Shimites; these are the families of the Gershonites.",
      "M": "From Gershon came the clan of Libni and the clan of Shimei; these are the Gershonite clans.",
      "T": "The Gershonite branch divided into the Libni clan and the Shimei clan."
    },
    "22": {
      "L": "Those numbered of them, according to the count of all males from a month old and upward, those numbered of them were seven thousand five hundred.",
      "M": "The total count of all males from a month old and upward was seven thousand five hundred.",
      "T": "The Gershonite males — from one month and older — numbered seven thousand five hundred."
    },
    "23": {
      "L": "The families of the Gershonites shall encamp behind the tabernacle, on the west.",
      "M": "The Gershonite clans shall camp behind the tabernacle, on the west side.",
      "T": "The Gershonites camp on the western side — behind the tabernacle."
    },
    "24": {
      "L": "And the chief of the ancestral house of the Gershonites shall be Eliasaph son of Lael.",
      "M": "The head of the Gershonite ancestral house is Eliasaph son of Lael.",
      "T": "Their clan chief is Eliasaph son of Lael."
    },
    "25": {
      "L": "And the charge of the sons of Gershon in the tent of meeting shall be: the tabernacle, the tent with its covering, the screen for the entrance to the tent of meeting,",
      "M": "The Gershonites in the tent of meeting shall be responsible for the tabernacle, the tent with its covering, and the screen at the entrance to the tent of meeting,",
      "T": "The Gershonites are entrusted with the outer shell of the tabernacle: the fabric dwelling itself, the tent covering that overlays it, and the screen at its entrance —"
    },
    "26": {
      "L": "the hangings of the court, and the screen for the entrance to the court that is around the tabernacle and the altar, and its cords — all the service pertaining to these.",
      "M": "the courtyard curtains and the screen at the entrance to the courtyard surrounding the tabernacle and the altar, and all the ropes — all the service involving these things.",
      "T": "the courtyard hangings, the entrance screen, all the ropes — everything related to the outer fabric structure of the complex."
    },
    "27": {
      "L": "And of Kohath was the family of the Amramites, the family of the Izharites, the family of the Hebronites, and the family of the Uzzielites; these are the families of the Kohathites.",
      "M": "From Kohath came the clan of Amram, the clan of Izhar, the clan of Hebron, and the clan of Uzziel; these are the Kohathite clans.",
      "T": "The Kohathite branch divided into four clans: Amram, Izhar, Hebron, and Uzziel."
    },
    "28": {
      "L": "In the count of all males from a month old and upward, there were eight thousand six hundred, keeping the charge of the sanctuary.",
      "M": "Counting all males from a month old and upward, there were eight thousand six hundred, responsible for the care of the sanctuary.",
      "T": "The Kohathite males — from one month and older — numbered eight thousand six hundred; they bear the charge of the sanctuary itself."
    },
    "29": {
      "L": "The families of the sons of Kohath shall encamp on the south side of the tabernacle.",
      "M": "The Kohathite clans shall camp on the south side of the tabernacle.",
      "T": "The Kohathites camp on the southern side."
    },
    "30": {
      "L": "And the chief of the ancestral house of the Kohathite clans shall be Elizaphan son of Uzziel.",
      "M": "The head of the Kohathite ancestral house is Elizaphan son of Uzziel.",
      "T": "Their clan chief is Elizaphan son of Uzziel."
    },
    "31": {
      "L": "And their charge shall be: the ark, the table, the lampstand, the altars, the vessels of the sanctuary with which they minister, the screen, and all the service pertaining to these.",
      "M": "They shall be responsible for the ark, the table, the lampstand, the altars, the vessels of the sanctuary used in worship, the curtain, and all the service involving these.",
      "T": "The Kohathites guard the most sacred objects: the ark, the table of the Presence, the lampstand, the altars, the sacred vessels — the very heart of Israel's worship."
    },
    "32": {
      "L": "And Eleazar the son of Aaron the priest shall be chief over the chiefs of the Levites, having oversight of those who keep the charge of the sanctuary.",
      "M": "Eleazar son of Aaron the priest shall be chief over the leaders of the Levites, with oversight of those who keep the charge of the sanctuary.",
      "T": "Eleazar, Aaron's son and a priest himself, stands as commander over all the Levite chiefs — the overseer of the entire sanctuary guard."
    },
    "33": {
      "L": "Of Merari was the family of the Mahlites and the family of the Mushites; these are the families of Merari.",
      "M": "From Merari came the clan of Mahli and the clan of Mushi; these are the Merarite clans.",
      "T": "The Merarite branch divided into two clans: Mahli and Mushi."
    },
    "34": {
      "L": "And those numbered of them, according to the count of all males from a month old and upward, were six thousand two hundred.",
      "M": "The total count of all males from a month old and upward was six thousand two hundred.",
      "T": "The Merarite males — from one month and older — numbered six thousand two hundred."
    },
    "35": {
      "L": "And the chief of the ancestral house of the families of Merari was Zuriel son of Abihail; they shall encamp on the north side of the tabernacle.",
      "M": "The head of the Merarite ancestral house was Zuriel son of Abihail. They shall camp on the north side of the tabernacle.",
      "T": "Their clan chief is Zuriel son of Abihail; the Merarites camp on the northern side."
    },
    "36": {
      "L": "And the assigned charge of the sons of Merari was: the frames of the tabernacle, the bars, the pillars, the sockets, and all their accessories — all the service pertaining to these;",
      "M": "The Merarites were responsible for the frames of the tabernacle, the bars, the pillars, the sockets, and all their accessories — all the service relating to these;",
      "T": "The Merarites bear the structural skeleton of the tabernacle: the wooden frames, the crossbars, the upright pillars, the socket bases — every piece of the rigid superstructure."
    },
    "37": {
      "L": "and the pillars around the court with their sockets, their pegs, and their cords.",
      "M": "also the pillars of the surrounding courtyard with their sockets, pegs, and ropes.",
      "T": "They also handle the courtyard pillars with their bases, stakes, and ropes."
    },
    "38": {
      "L": "And those who were to encamp before the tabernacle on the east, before the tent of meeting toward the sunrise, were Moses and Aaron and his sons, keeping the charge of the sanctuary as a duty for the Israelites; and the unauthorized person who came near was to be put to death.",
      "M": "Moses, Aaron, and his sons were to camp in front of the tabernacle, on the east side toward the sunrise. They were responsible for the sanctuary on behalf of the Israelites. Any unauthorized person who came near was to be put to death.",
      "T": "Moses, Aaron, and Aaron's sons camped on the east — directly before the tent of meeting, facing the sunrise. They held the foremost charge: guarding the sanctuary on behalf of all Israel. Any outsider who approached was to die."
    },
    "39": {
      "L": "All those numbered of the Levites, whom Moses and Aaron numbered at the commandment of the LORD, by their families, all the males from a month old and upward, were twenty-two thousand.",
      "M": "All the Levites Moses and Aaron counted at the LORD's command, by their clans — every male from a month old and upward — came to twenty-two thousand.",
      "T": "The full Levite census — conducted by Moses and Aaron under the LORD's command, every male from a month and older across all the clans — came to twenty-two thousand."
    },
    "40": {
      "L": "And the LORD said to Moses: Number all the firstborn males of the children of Israel from a month old and upward, and take the count of their names.",
      "M": "The LORD said to Moses, 'Count every firstborn male among the Israelites from a month old and upward, and record their names.'",
      "T": "The LORD told Moses: 'Now count every firstborn male in Israel from a month old and older — by name.'"
    },
    "41": {
      "L": "And you shall take the Levites for me — I am the LORD — instead of all the firstborn among the children of Israel; and the cattle of the Levites instead of all the firstlings among the cattle of the children of Israel.",
      "M": "Take the Levites for me — I am the LORD — in place of all the firstborn Israelites, and the Levites' livestock in place of all the firstborn livestock of the Israelites.",
      "T": "Take the Levites as mine — I am the LORD — as substitutes for every firstborn son in Israel, and their livestock as substitutes for every firstborn animal in Israel."
    },
    "42": {
      "L": "And Moses numbered, as the LORD commanded him, all the firstborn among the children of Israel.",
      "M": "So Moses counted all the firstborn among the Israelites, as the LORD had commanded.",
      "T": "Moses obeyed and counted every firstborn in Israel."
    },
    "43": {
      "L": "And all the firstborn males by the count of names, from a month old and upward, of those numbered of them, were twenty-two thousand two hundred and seventy-three.",
      "M": "All the firstborn males registered by name from a month old and upward came to twenty-two thousand two hundred and seventy-three.",
      "T": "The total: twenty-two thousand two hundred and seventy-three firstborn males, one month and older."
    },
    "44": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "45": {
      "L": "Take the Levites instead of all the firstborn among the children of Israel, and the cattle of the Levites instead of their cattle; and the Levites shall be mine; I am the LORD.",
      "M": "Take the Levites in place of all the firstborn Israelites, and the Levites' livestock in place of their livestock. The Levites are mine; I am the LORD.",
      "T": "Take the Levites in exchange for all of Israel's firstborn — and their animals in exchange for Israel's firstborn animals. The Levites belong to me. I am the LORD."
    },
    "46": {
      "L": "And for the redemption of the two hundred and seventy-three of the firstborn of the children of Israel who exceed the Levites,",
      "M": "For the redemption of the two hundred and seventy-three firstborn Israelites who exceed the number of Levites,",
      "T": "But there are two hundred and seventy-three firstborn sons with no Levite counterpart to substitute for them —"
    },
    "47": {
      "L": "you shall take five shekels apiece, by the head; you shall take them according to the sanctuary shekel — the shekel being twenty gerahs.",
      "M": "you shall collect five shekels per person, reckoned in the sanctuary shekel — the shekel being twenty gerahs.",
      "T": "for each of them you shall collect five shekels, weighed by the sanctuary standard of twenty gerahs per shekel."
    },
    "48": {
      "L": "And you shall give the money by which the excess number of them is redeemed to Aaron and to his sons.",
      "M": "Give the redemption money to Aaron and his sons.",
      "T": "The redemption silver goes to Aaron and his sons."
    },
    "49": {
      "L": "And Moses took the redemption money from those who were over and above those redeemed by the Levites.",
      "M": "So Moses took the redemption money from those who exceeded the number redeemed by the Levites.",
      "T": "Moses collected the redemption payment for those two hundred and seventy-three who had no Levite substitute."
    },
    "50": {
      "L": "From the firstborn of the children of Israel he took the money — one thousand three hundred and sixty-five shekels, by the sanctuary shekel.",
      "M": "From the firstborn Israelites he received one thousand three hundred and sixty-five shekels, by the sanctuary shekel.",
      "T": "The total collected from Israel's firstborn came to one thousand three hundred and sixty-five shekels, weighed by the sanctuary standard."
    },
    "51": {
      "L": "And Moses gave the redemption money to Aaron and to his sons, according to the word of the LORD, as the LORD commanded Moses.",
      "M": "Moses gave the redemption money to Aaron and his sons, just as the LORD had commanded.",
      "T": "Moses handed the silver to Aaron and his sons — fulfilling the word of the LORD exactly as commanded."
    }
  },
  "4": {
    "1": {
      "L": "And the LORD spoke unto Moses and unto Aaron, saying,",
      "M": "The LORD said to Moses and Aaron,",
      "T": "The LORD said to Moses and Aaron:"
    },
    "2": {
      "L": "Take a census of the sons of Kohath from among the children of Levi, by their clans and their ancestral houses,",
      "M": "Take a census of the Kohathites from among the Levites, by their clans and ancestral houses,",
      "T": "Count the Kohathites within Levi — by clans and ancestral households —"
    },
    "3": {
      "L": "from thirty years old up to fifty years old, everyone who can enter the service to do the work in the tent of meeting.",
      "M": "everyone from thirty to fifty years old who is qualified to perform service in the tent of meeting.",
      "T": "specifically those between thirty and fifty years old who are in the prime of service for the tent of meeting."
    },
    "4": {
      "L": "This is the service of the sons of Kohath in the tent of meeting: the most holy things.",
      "M": "This is the work assigned to the Kohathites in the tent of meeting: the care of the most holy objects.",
      "T": "The Kohathites have the most demanding assignment: the most holy objects themselves."
    },
    "5": {
      "L": "When the camp is to move, Aaron and his sons shall go in and take down the covering veil and cover the ark of the testimony with it.",
      "M": "When the camp sets out, Aaron and his sons shall go in and take down the curtain of the screen and cover the ark of the testimony with it.",
      "T": "When the camp is about to move, Aaron and his sons enter first: they take down the inner curtain and drape it over the ark of the covenant."
    },
    "6": {
      "L": "Then they shall put on it a covering of fine leather and spread over it a cloth all of blue; and they shall insert its poles.",
      "M": "Over that they shall spread a covering of fine leather and place over it a blue cloth, then insert the carrying poles.",
      "T": "Over the curtain they lay a durable hide, then a cloth of solid blue, and they slide in the carrying poles — ready for transport."
    },
    "7": {
      "L": "And over the table of the Presence they shall spread a blue cloth and put on it the dishes, the spoons, the bowls, and the flagons for the drink offering; the regular bread shall also be on it.",
      "M": "Over the table of the Presence they shall spread a blue cloth and place on it the plates, the dishes, the bowls, and the pitchers for the drink offering; the bread of the Presence shall remain on it.",
      "T": "The table of the Presence is draped in blue cloth, with all its vessels arranged in place — the plates, saucers, bowls, and pitchers for the drink offering, and the display bread still set upon it."
    },
    "8": {
      "L": "Then they shall spread over them a cloth of scarlet and cover it with a covering of fine leather, and shall insert its poles.",
      "M": "They shall cover these with a scarlet cloth, then put over it a covering of fine leather, and insert its poles.",
      "T": "A scarlet overlay goes on top, then fine leather, then in go the poles."
    },
    "9": {
      "L": "And they shall take a blue cloth and cover the lampstand of the light, with its lamps, its tongs, its snuff dishes, and all the oil vessels with which it is tended,",
      "M": "They shall take a blue cloth and cover the lampstand of the light, its lamps, its snuffers, its trays, and all the oil containers used to tend it,",
      "T": "The lampstand and all its components — lamps, snuffers, trays, the oil flasks — are wrapped in blue cloth,"
    },
    "10": {
      "L": "and they shall put it and all its vessels within a covering of fine leather and put it on the carrying frame.",
      "M": "and place it with all its utensils within a covering of fine leather, and put it on the carrying frame.",
      "T": "then placed inside a leather cover and laid on the carrying frame."
    },
    "11": {
      "L": "And over the golden altar they shall spread a blue cloth and cover it with a covering of fine leather, and shall insert its poles.",
      "M": "Over the golden altar they shall spread a blue cloth, cover it with fine leather, and insert its poles.",
      "T": "The golden incense altar gets its own blue cloth covering, then a leather wrap, and its poles."
    },
    "12": {
      "L": "And they shall take all the vessels of ministry with which they minister in the sanctuary, and put them in a blue cloth, cover them with a covering of fine leather, and put them on the carrying frame.",
      "M": "They shall take all the utensils of service used in the sanctuary, wrap them in a blue cloth, cover them with fine leather, and place them on the carrying frame.",
      "T": "Every other vessel of sanctuary service is wrapped in blue, covered in leather, and loaded onto the carrying frame."
    },
    "13": {
      "L": "And they shall remove the ashes from the altar and spread a purple cloth over it.",
      "M": "They shall clear the ashes from the altar and spread a purple cloth over it.",
      "T": "The bronze altar is cleared of its ashes and draped in a purple covering."
    },
    "14": {
      "L": "And they shall put on it all the vessels that are used for it: the censers, the forks, the shovels, and the basins — all the vessels of the altar; and they shall spread over it a covering of fine leather, and insert its poles.",
      "M": "They shall place on it all its utensils — the fire pans, the forks, the shovels, and the basins — all the altar vessels; then spread a covering of fine leather over it, and insert its poles.",
      "T": "All the altar tools — the fire pans, flesh hooks, shovels, basins — are laid upon it, a leather cover goes over everything, and the poles go in."
    },
    "15": {
      "L": "And when Aaron and his sons have finished covering the sanctuary and all the furnishings of the sanctuary as the camp sets forward, after that the sons of Kohath shall come to carry it, but they must not touch the holy things, lest they die. These are the things of the tent of meeting that the sons of Kohath are to carry.",
      "M": "When Aaron and his sons have finished covering the sanctuary and all its furnishings as the camp moves out, the Kohathites shall come to carry the load. But they must not touch the holy things, or they will die. These are the objects from the tent of meeting that the Kohathites shall carry.",
      "T": "Only after Aaron and his sons have completed every covering may the Kohathites approach to lift their loads. The holy objects must not be touched — to touch them is to die. These are the sacred things the Kohathites carry."
    },
    "16": {
      "L": "And Eleazar the son of Aaron the priest shall have charge of the oil for the light, the fragrant incense, the regular grain offering, and the anointing oil, with the oversight of the whole tabernacle and all that is in it — the sanctuary and its furnishings.",
      "M": "Eleazar son of Aaron the priest shall be responsible for the oil of the light, the fragrant incense, the regular grain offering, and the anointing oil — overseeing the whole tabernacle and everything in it, the sanctuary and all its furnishings.",
      "T": "Eleazar the priest holds personal oversight of the consumables: the lamp oil, the incense blend, the daily grain offering, the anointing oil — and through them, supervisory responsibility for the entire tabernacle complex."
    },
    "17": {
      "L": "And the LORD spoke unto Moses and unto Aaron, saying,",
      "M": "The LORD said to Moses and Aaron,",
      "T": "The LORD said to Moses and Aaron:"
    },
    "18": {
      "L": "Let not the tribe of the families of the Kohathites be cut off from among the Levites,",
      "M": "Do not let the Kohathite clan be cut off from among the Levites.",
      "T": "Take care that the Kohathite branch of Levi is not destroyed —"
    },
    "19": {
      "L": "but thus do unto them so that they may live and not die when they approach the most holy things: Aaron and his sons shall go in and appoint each one to his task and his burden.",
      "M": "but do this for them so that they may live and not die when they come near the most holy things: Aaron and his sons shall go in and assign each person to his task and his load.",
      "T": "deal with them correctly so they stay alive when they approach those most holy objects: Aaron and his sons must go in first and assign each Kohathite to his specific object and specific duty."
    },
    "20": {
      "L": "They shall not go in to look at the holy things even for a moment, lest they die.",
      "M": "But the Kohathites themselves must not go in to look at the holy things even for a moment, or they will die.",
      "T": "The Kohathites must not enter and catch even a glance of the holy things while uncovered. A single look means death."
    },
    "21": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "22": {
      "L": "Take a census of the sons of Gershon also, by their ancestral houses, by their families;",
      "M": "Take a census of the Gershonites as well, by their ancestral houses and clans.",
      "T": "Count the Gershonites too — by ancestral household and clan."
    },
    "23": {
      "L": "from thirty years old up to fifty years old you shall number them, all who can enter to do the service, to do the work in the tent of meeting.",
      "M": "Count all those from thirty to fifty years old who qualify to serve and work in the tent of meeting.",
      "T": "Those between thirty and fifty who are qualified for the service — count them all."
    },
    "24": {
      "L": "This is the service of the families of the Gershonites: serving and bearing burdens.",
      "M": "This is the work assigned to the Gershonite clans: service and carrying.",
      "T": "The Gershonites handle the fabric work — carrying and setting up the coverings and curtains."
    },
    "25": {
      "L": "They shall carry the curtains of the tabernacle and the tent of meeting, its covering, the covering of fine leather that is on top of it, the screen for the entrance of the tent of meeting,",
      "M": "They shall carry the curtains of the tabernacle and the tent of meeting, its covering and the leather covering over it, the screen at the entrance to the tent of meeting,",
      "T": "They carry the tabernacle curtains, the tent covering, the outer leather layer, the entrance screen —"
    },
    "26": {
      "L": "the hangings of the court, the screen for the entrance of the gate of the court that is around the tabernacle and the altar, their cords, and all the equipment for their service; and they shall do all that needs to be done with these things.",
      "M": "the courtyard hangings, the screen at the gate of the courtyard surrounding the tabernacle and the altar, their ropes, and all the equipment for this service. They shall do all the work relating to these items.",
      "T": "the courtyard hangings, the entrance screen, all the ropes — everything fabric that encloses the sacred compound."
    },
    "27": {
      "L": "All the service of the Gershonites, in all their carrying and in all their service, shall be at the direction of Aaron and his sons; and you shall assign to them as their charge all that they are to carry.",
      "M": "All the work of the Gershonites, in all their carrying and in all their service, shall be done under the direction of Aaron and his sons. You shall assign them the specific items they are to carry.",
      "T": "Every aspect of the Gershonite work — each load, each duty — is performed under Aaron and his sons' orders. You are to assign them their specific responsibilities."
    },
    "28": {
      "L": "This is the service of the Gershonite families in the tent of meeting; and their oversight shall be under the hand of Ithamar the son of Aaron the priest.",
      "M": "This is the work of the Gershonite clans in the tent of meeting; their supervision falls under Ithamar son of Aaron the priest.",
      "T": "This is the Gershonite mandate in the tent of meeting — supervised by Ithamar, Aaron's son."
    },
    "29": {
      "L": "As for the sons of Merari, you shall list them by their clans and their ancestral houses;",
      "M": "As for the Merarites, count them by their clans and ancestral houses.",
      "T": "Count the Merarites the same way — by clans and ancestral households."
    },
    "30": {
      "L": "from thirty years old up to fifty years old you shall number them, everyone who can enter the service to do the work of the tent of meeting.",
      "M": "Count all from thirty to fifty years old who qualify to work in the tent of meeting.",
      "T": "Those between thirty and fifty who qualify for this work — count them all."
    },
    "31": {
      "L": "And this is their charge, what they are to carry as their whole service in the tent of meeting: the frames of the tabernacle, its bars, its pillars, and its sockets;",
      "M": "This is what they are responsible to carry as their entire service in the tent of meeting: the frames of the tabernacle, its crossbars, its pillars, and its bases;",
      "T": "The Merarites carry the structural skeleton: the frames, crossbars, pillars, and socket-bases of the tabernacle —"
    },
    "32": {
      "L": "the pillars of the court all around with their sockets, their pegs, and their cords, with all the equipment for their service; and you shall assign to each man by name the items he is to carry.",
      "M": "and the surrounding courtyard pillars with their bases, pegs, and ropes — all the equipment for this service. You shall assign each man by name to the specific items he is to carry.",
      "T": "the courtyard pillars with their bases, stakes, and ropes. Each man is assigned by name to his specific piece of equipment."
    },
    "33": {
      "L": "This is the service of the families of the Merarites, all their service in the tent of meeting, under the oversight of Ithamar the son of Aaron the priest.",
      "M": "This is the work of the Merarite clans, all their service in the tent of meeting, under the oversight of Ithamar son of Aaron the priest.",
      "T": "This is the Merarite assignment in the tent of meeting — also supervised by Ithamar, Aaron's son."
    },
    "34": {
      "L": "And Moses and Aaron and the chiefs of the congregation numbered the Kohathites by their clans and their ancestral houses,",
      "M": "Moses, Aaron, and the leaders of the congregation counted the Kohathites by their clans and ancestral houses,",
      "T": "Moses, Aaron, and the tribal leaders conducted the Kohathite count by clans and households —"
    },
    "35": {
      "L": "from thirty years old up to fifty years old, everyone who could enter the service for work in the tent of meeting.",
      "M": "counting all from thirty to fifty years old who qualified to serve in the tent of meeting.",
      "T": "every Kohathite man between thirty and fifty fit for service."
    },
    "36": {
      "L": "And those numbered of them by their clans were two thousand seven hundred and fifty.",
      "M": "Those enrolled from their clans numbered two thousand seven hundred and fifty.",
      "T": "The Kohathite muster came to two thousand seven hundred and fifty."
    },
    "37": {
      "L": "These are those who were numbered of the Kohathite clans, all who served in the tent of meeting, whom Moses and Aaron numbered according to the commandment of the LORD through Moses.",
      "M": "These are those enrolled from the Kohathite clans — all who served in the tent of meeting — whom Moses and Aaron counted according to the LORD's command given through Moses.",
      "T": "These were the registered Kohathite servants of the tent of meeting — numbered by Moses and Aaron at the direct command of the LORD."
    },
    "38": {
      "L": "And those numbered of the sons of Gershon, by their clans and their ancestral houses,",
      "M": "The Gershonites enrolled by their clans and ancestral houses —",
      "T": "The Gershonite enrollment by clans and households —"
    },
    "39": {
      "L": "from thirty years old up to fifty years old, everyone who could enter for service, for work in the tent of meeting —",
      "M": "all from thirty to fifty years old who qualified to work in the tent of meeting —",
      "T": "every man between thirty and fifty fit for service —"
    },
    "40": {
      "L": "those numbered of them, by their clans and their ancestral houses, were two thousand six hundred and thirty.",
      "M": "numbered two thousand six hundred and thirty.",
      "T": "came to two thousand six hundred and thirty."
    },
    "41": {
      "L": "These are those who were numbered of the Gershonite clans, all who served in the tent of meeting, whom Moses and Aaron numbered according to the commandment of the LORD.",
      "M": "These are those enrolled from the Gershonite clans — all who served in the tent of meeting — counted by Moses and Aaron at the LORD's command.",
      "T": "These were the registered Gershonite servants — counted by Moses and Aaron as the LORD commanded."
    },
    "42": {
      "L": "And those numbered of the Merarite clans, by their clans and their ancestral houses,",
      "M": "The Merarites enrolled by their clans and ancestral houses —",
      "T": "The Merarite enrollment by clans and households —"
    },
    "43": {
      "L": "from thirty years old up to fifty years old, everyone who could enter for service, for work in the tent of meeting —",
      "M": "all from thirty to fifty years old who qualified to work in the tent of meeting —",
      "T": "every man between thirty and fifty fit for service —"
    },
    "44": {
      "L": "those numbered of them, by their clans, were three thousand two hundred.",
      "M": "numbered three thousand two hundred.",
      "T": "came to three thousand two hundred."
    },
    "45": {
      "L": "These are those who were numbered of the Merarite clans, whom Moses and Aaron numbered according to the commandment of the LORD through Moses.",
      "M": "These are those enrolled from the Merarite clans — counted by Moses and Aaron according to the LORD's command.",
      "T": "These were the registered Merarite servants — counted by Moses and Aaron as the LORD commanded."
    },
    "46": {
      "L": "All those who were numbered of the Levites, whom Moses and Aaron and the chiefs of Israel numbered, by their clans and their ancestral houses,",
      "M": "All the Levites whom Moses, Aaron, and the leaders of Israel enrolled, by their clans and ancestral houses —",
      "T": "All the Levites enrolled by Moses, Aaron, and the tribal leaders — by clans and households —"
    },
    "47": {
      "L": "from thirty years old up to fifty years old, everyone who could qualify to do the work of service and the work of bearing burdens in the tent of meeting —",
      "M": "from thirty to fifty years old, every man who could qualify to perform the service work and the carrying work in the tent of meeting —",
      "T": "every man between thirty and fifty capable of service and carrying in the tent of meeting —"
    },
    "48": {
      "L": "those numbered of them were eight thousand five hundred and eighty.",
      "M": "numbered eight thousand five hundred and eighty.",
      "T": "came to eight thousand five hundred and eighty."
    },
    "49": {
      "L": "According to the commandment of the LORD through Moses, each one was numbered to his service and to his burden; thus they were numbered by him, as the LORD commanded Moses.",
      "M": "Each was numbered by the LORD's command through Moses — each assigned to his service and his load. So they were counted, as the LORD commanded Moses.",
      "T": "The LORD's command through Moses specified each man's duty and each man's load. Every assignment was made with divine precision, just as the LORD had instructed."
    }
  },
  "5": {
    "1": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "2": {
      "L": "Command the children of Israel to put out of the camp every leper, and every one who has a discharge, and everyone who is unclean through contact with the dead;",
      "M": "Command the Israelites to send outside the camp every person with a skin disease, everyone with a bodily discharge, and everyone who has become unclean by contact with a corpse.",
      "T": "Give Israel this command: anyone with a skin disease, anyone with a bodily discharge, and anyone defiled by contact with the dead must be sent outside the camp."
    },
    "3": {
      "L": "both male and female you shall put out — outside the camp you shall put them, that they may not defile their camp, in the midst of which I dwell.",
      "M": "Send them out, both male and female, that they may not defile the camp where I dwell.",
      "T": "Male and female alike — they must go outside. The camp is where I dwell; it must not be defiled."
    },
    "4": {
      "L": "And the children of Israel did so and put them outside the camp; as the LORD had spoken to Moses, so the children of Israel did.",
      "M": "The Israelites did so and put them outside the camp, just as the LORD had spoken to Moses.",
      "T": "Israel obeyed: the unclean were expelled from the camp, exactly as the LORD had said."
    },
    "5": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "6": {
      "L": "Say to the children of Israel: When a man or woman commits any sin that people commit, acting unfaithfully against the LORD, and that person is guilty,",
      "M": "Say to the Israelites: When a man or woman commits any of the sins that people commit, acting in breach of faith against the LORD, that person is guilty,",
      "T": "Tell the Israelites: when anyone — man or woman — commits a wrong against another person, they have also broken faith with the LORD. They bear that guilt."
    },
    "7": {
      "L": "he shall confess the sin that he has done. He shall make full restitution for his wrong, adding a fifth to it and giving it to him whom he wronged.",
      "M": "that person shall confess the sin committed, make full restitution for the wrong, and add one-fifth of its value — giving it to the one who was wronged.",
      "T": "Guilt requires a full public confession, then restoration: the full amount owed plus a twenty-percent premium, paid directly to the injured party."
    },
    "8": {
      "L": "But if the man has no kinsman to whom restitution may be made for the wrong, then the restitution for the wrong shall go to the LORD for the priest, besides the ram of atonement with which atonement is made for him.",
      "M": "But if the wronged person has no relative to receive the restitution, then the restitution shall go to the LORD for the priest, in addition to the ram used to make atonement.",
      "T": "If the wronged party is dead and has no surviving heir, the restitution goes to the LORD — paid through the priest — along with the atonement ram. The wrong must still be righted."
    },
    "9": {
      "L": "And every contribution, all the holy gifts of the children of Israel that they bring to the priest, shall be his.",
      "M": "Every contribution — all the holy gifts that the Israelites bring to the priest — shall belong to the priest.",
      "T": "Every offering that Israelites bring to the priest — every holy gift — becomes the priest's."
    },
    "10": {
      "L": "Each man's holy gifts shall be his; whatever any man gives to the priest shall be his.",
      "M": "Each person's sacred gifts belong to that person; whatever one gives to the priest is the priest's.",
      "T": "What you designate as sacred is yours to give; once you give it to the priest, it is fully his."
    },
    "11": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "12": {
      "L": "Speak to the children of Israel and say to them: If any man's wife goes astray and acts unfaithfully against him,",
      "M": "Say to the Israelites: If a man's wife goes astray and acts unfaithfully against him,",
      "T": "Tell the Israelites: if a wife turns aside and acts faithlessly against her husband —"
    },
    "13": {
      "L": "and a man lies with her carnally, and it is hidden from the eyes of her husband, and she is undetected though she has defiled herself, and there is no witness against her, and she was not caught in the act,",
      "M": "if another man has lain with her, and it is hidden from her husband's knowledge, and she is not discovered even though she has defiled herself — there being no witness against her and she not caught in the act —",
      "T": "if she has been intimate with another man, undetected, with no witness and no evidence to bring the matter to light —"
    },
    "14": {
      "L": "and if the spirit of jealousy comes upon him and he is jealous of his wife when she has defiled herself, or if the spirit of jealousy comes upon him and he is jealous of his wife when she has not defiled herself —",
      "M": "if a spirit of jealousy comes over the husband and he becomes suspicious of his wife who has defiled herself, or if a spirit of jealousy comes over him and he becomes suspicious of his wife when she has not defiled herself —",
      "T": "if a surge of jealous suspicion overtakes the husband — whether his wife has in fact been unfaithful or whether she is innocent —"
    },
    "15": {
      "L": "then the man shall bring his wife to the priest and bring her offering for her: a tenth of an ephah of barley flour. He shall pour no oil on it and put no frankincense on it, for it is a grain offering of jealousy, a grain offering of remembrance, bringing iniquity to remembrance.",
      "M": "the man shall bring his wife to the priest and bring her offering — a tenth of an ephah of barley flour. He shall put no oil on it and add no frankincense, for it is a grain offering of jealousy — a grain offering of remembrance that calls sin to mind.",
      "T": "then the husband must bring his wife to the priest, along with an offering: a tenth of an ephah of barley flour — no oil, no incense. It is the jealousy offering, a memorial offering that summons hidden sin into God's sight."
    },
    "16": {
      "L": "And the priest shall bring her near and set her before the LORD.",
      "M": "The priest shall bring her forward and present her before the LORD.",
      "T": "The priest brings the woman forward and places her before the LORD."
    },
    "17": {
      "L": "And the priest shall take holy water in an earthenware vessel and take some of the dust that is on the floor of the tabernacle and put it into the water.",
      "M": "The priest shall take some holy water in a clay vessel and take some of the dust from the floor of the tabernacle and put it into the water.",
      "T": "He takes sacred water in a clay jar, adds dust from the tabernacle floor — earth from God's holy dwelling mixed into the water of judgment."
    },
    "18": {
      "L": "And the priest shall set the woman before the LORD and unbind the hair of the woman's head and place in her hands the grain offering of remembrance, which is the grain offering of jealousy. And in the priest's hand shall be the bitter water that brings the curse.",
      "M": "The priest shall present the woman before the LORD, let down her hair, and place in her hands the grain offering of remembrance — the jealousy offering. The priest shall hold in his hand the bitter water that brings the curse.",
      "T": "The priest presents the woman before the LORD and loosens her hair — a sign of the accused standing exposed before divine judgment. Her hands hold the jealousy offering; the priest holds the bitter, curse-bearing water."
    },
    "19": {
      "L": "And the priest shall put her under oath and say to the woman: If no man has lain with you, and if you have not gone astray into uncleanness while under your husband's authority, be free from this bitter water that brings the curse.",
      "M": "The priest shall administer the oath to her: 'If no man has lain with you, and if you have not strayed into impurity while under your husband's authority, be free from this bitter water that brings the curse.'",
      "T": "The priest then speaks the oath over her: 'If you are innocent — if no man has been with you, if you have not wandered into defilement — then this bitter water will not harm you. Be free.'"
    },
    "20": {
      "L": "But if you have gone astray, though under your husband's authority, and if you have defiled yourself, and some man other than your husband has lain with you —",
      "M": "But if you have gone astray while under your husband's authority, if you have defiled yourself and some man other than your husband has lain with you —",
      "T": "But if you have been unfaithful — if another man has been with you while you were bound to your husband —"
    },
    "21": {
      "L": "then the priest shall put the woman under the oath of cursing and say to the woman — may the LORD make you a curse and an oath among your people, when the LORD makes your thigh fall away and your belly swell;",
      "M": "the priest shall invoke the curse upon the woman and say to her: 'May the LORD make you a source of cursing and an object of oath-swearing among your people, when the LORD causes your womb to miscarry and your abdomen to swell.'",
      "T": "then the priest pronounces the curse: 'May the LORD make you an example and a byword among your people — your body bearing the visible mark of the faithlessness you have hidden.'"
    },
    "22": {
      "L": "and this water that brings the curse shall enter your belly and make your belly swell and your thigh fall away. And the woman shall say: Amen, Amen.",
      "M": "May this water that brings the curse go into your body to cause your abdomen to swell and your womb to shrink.' And the woman shall say, 'Amen, Amen.'",
      "T": "May this water enter you and do what guilt demands.' The woman must respond: 'Amen, amen' — agreeing to stand under the verdict, whatever it may be."
    },
    "23": {
      "L": "Then the priest shall write these curses in a book and wash them off into the bitter water.",
      "M": "The priest shall write these curses in a scroll and wash them off into the bitter water.",
      "T": "The priest writes the curse on a scroll, then dissolves the ink into the bitter water — making the woman drink the written judgment."
    },
    "24": {
      "L": "And he shall make the woman drink the bitter water that brings the curse, and the water that brings the curse shall enter into her and become bitter.",
      "M": "He shall make the woman drink the bitter water that brings the curse; the water that brings the curse shall enter her and cause bitterness.",
      "T": "She drinks the water. The curse-bearing judgment enters her."
    },
    "25": {
      "L": "And the priest shall take the grain offering of jealousy out of the woman's hand and shall wave the offering before the LORD and bring it to the altar.",
      "M": "Then the priest shall take the grain offering of jealousy from the woman's hand, wave it before the LORD, and bring it to the altar.",
      "T": "The priest receives the jealousy offering from her hands, waves it before the LORD, and carries it to the altar."
    },
    "26": {
      "L": "And the priest shall take a handful of the offering, as its memorial portion, and burn it on the altar, and afterward shall make the woman drink the water.",
      "M": "The priest shall take a handful of the grain offering as its memorial portion and burn it on the altar, and afterward make the woman drink the water.",
      "T": "A handful is burned on the altar as the token offering; then the woman drinks the water."
    },
    "27": {
      "L": "And when he has made her drink the water, then if she has defiled herself and has acted unfaithfully against her husband, the water that brings the curse shall enter into her and cause bitter pain, and her belly shall swell, and her thigh shall fall away, and the woman shall become a curse among her people.",
      "M": "When he has made her drink the water, if she has defiled herself and acted unfaithfully against her husband, the water that brings the curse shall cause bitter pain to enter her, her abdomen will swell, and her womb will waste away, and she will become a curse among her people.",
      "T": "If she is guilty, the water works: bitter pain takes hold, her body manifests the judgment, and she becomes a public warning to her community. The hidden sin is brought into the open by God himself."
    },
    "28": {
      "L": "But if the woman has not defiled herself and is clean, then she shall be free and shall conceive children.",
      "M": "But if the woman has not defiled herself and is clean, she will be free from harm and will be able to bear children.",
      "T": "But if she is innocent, the water leaves her unharmed. She goes free — cleared by the same ordeal that would have condemned her, and given back the promise of children."
    },
    "29": {
      "L": "This is the law in cases of jealousy, when a wife, though under her husband's authority, goes astray and defiles herself,",
      "M": "This is the law for cases of jealousy, when a wife goes astray while under her husband's authority and defiles herself,",
      "T": "This is the ruling for cases of suspected marital unfaithfulness —"
    },
    "30": {
      "L": "or when the spirit of jealousy comes upon a man and he is jealous of his wife; then he shall set the woman before the LORD, and the priest shall apply all this law to her.",
      "M": "or when the spirit of jealousy comes over a man and he becomes jealous of his wife; then he shall bring the woman before the LORD, and the priest shall carry out all these procedures.",
      "T": "when jealous suspicion seizes a husband. He brings his wife before the LORD, the priest applies the full procedure, and the verdict belongs to God alone."
    },
    "31": {
      "L": "The man shall be free from iniquity, but the woman shall bear her iniquity.",
      "M": "The man will be free of guilt, and the woman will bear her own iniquity.",
      "T": "The husband is cleared by bringing the matter to God. The woman stands accountable for whatever she has done — or has not done, in which case she too goes free."
    }
  },
  "6": {
    "1": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "2": {
      "L": "Speak to the children of Israel and say to them: When either a man or a woman makes a special vow, the vow of a Nazirite, to separate himself to the LORD,",
      "M": "Say to the Israelites: When a man or woman takes the special vow of a Nazirite, setting themselves apart for the LORD,",
      "T": "Tell the Israelites: when a man or woman takes a Nazirite vow — consecrating themselves in a special way to the LORD —"
    },
    "3": {
      "L": "he shall separate himself from wine and strong drink; he shall drink no vinegar of wine or vinegar of strong drink, and shall not drink any juice of grapes or eat grapes, fresh or dried.",
      "M": "that person shall abstain from wine and beer, not drink any wine vinegar or beer vinegar, nor drink grape juice, nor eat fresh or dried grapes.",
      "T": "they must abstain completely from anything vine-related — no wine, no beer, no grape juice, no fresh grapes, no raisins. The vine is off-limits entirely."
    },
    "4": {
      "L": "All the days of his separation he shall eat nothing that is produced by the grapevine, not even the seeds or the skins.",
      "M": "During the entire period of the Nazirite vow, that person shall not eat anything made from the grapevine, not even the seeds or the grape skins.",
      "T": "For the full duration of the vow, nothing from the vine — not even the seeds or the outer skin."
    },
    "5": {
      "L": "All the days of his vow of separation, no razor shall come upon his head; until the days are fulfilled when he separates himself to the LORD, he shall be holy, letting the hair of his head grow long.",
      "M": "During the entire period of the Nazirite vow, no razor shall touch his head. The Nazirite is holy to the LORD until the days of his separation are complete; he shall let the hair of his head grow freely.",
      "T": "No razor touches his head for the entire vow period. He is holy to the LORD; his uncut hair is the visible sign of that consecration, growing freely as his dedication to God."
    },
    "6": {
      "L": "All the days that he separates himself to the LORD he shall not go near a dead body.",
      "M": "Throughout the period of separation, the Nazirite shall not go near a dead body.",
      "T": "During the Nazirite period, he must not approach any corpse — not even a family member's."
    },
    "7": {
      "L": "Not even for his father, his mother, his brother, or his sister — he shall not make himself unclean for them when they die, because the consecration of God is on his head.",
      "M": "Even if his father, mother, brother, or sister dies, he shall not defile himself, because the sign of God's consecration is on his head.",
      "T": "Even for a father, mother, brother, or sister who dies — he does not defile himself. The sacred vow-crown is on his head; that takes precedence over even the most binding family obligation."
    },
    "8": {
      "L": "All the days of his separation he is holy to the LORD.",
      "M": "The Nazirite is holy to the LORD throughout the entire period of separation.",
      "T": "For the whole duration of the vow, he is completely holy — set apart for the LORD."
    },
    "9": {
      "L": "If any man dies very suddenly beside him and he defiles his consecrated head, then he shall shave his head on the day of his cleansing; on the seventh day he shall shave it.",
      "M": "If someone dies suddenly in his presence and he defiles his consecrated head, he shall shave his head on the day of his cleansing — the seventh day.",
      "T": "But if someone suddenly dies beside him — defiling the Nazirite's consecrated head through no intention of his own — he must shave his head on the seventh day, the day of his purification."
    },
    "10": {
      "L": "And on the eighth day he shall bring two turtledoves or two young pigeons to the priest, to the entrance of the tent of meeting.",
      "M": "On the eighth day he shall bring to the priest at the entrance of the tent of meeting two turtledoves or two young pigeons.",
      "T": "On the eighth day he comes to the priest at the tent of meeting with two turtledoves or two young pigeons."
    },
    "11": {
      "L": "And the priest shall offer one as a sin offering and the other as a burnt offering, and make atonement for him, because he sinned by reason of the dead. And he shall consecrate his head that same day.",
      "M": "The priest shall offer one as a sin offering and the other as a burnt offering and make atonement for him, because he became unclean by contact with the dead. He shall re-consecrate his head that same day.",
      "T": "The priest offers one for sin and one as a burnt offering, making atonement for the accidental defilement. The Nazirite's head is re-consecrated the same day."
    },
    "12": {
      "L": "And he shall separate to the LORD the days of his separation and bring a male lamb a year old as a guilt offering; but the previous days shall be void, because his separation was defiled.",
      "M": "He shall devote himself again to the LORD for the full term of his separation and bring a year-old male lamb as a guilt offering. The earlier days shall not count, because his separation was defiled.",
      "T": "He begins the vow period again from scratch, bringing a guilt offering to cover the interruption. The days before the defilement are forfeited — the vow restarts."
    },
    "13": {
      "L": "Now this is the law for the Nazirite: when the days of his separation are fulfilled, he shall be brought to the entrance of the tent of meeting.",
      "M": "This is the law of the Nazirite: when the days of his separation are complete, he shall be brought to the entrance of the tent of meeting.",
      "T": "When the Nazirite's full period of dedication is complete, this is the concluding ritual: he comes to the tent of meeting."
    },
    "14": {
      "L": "And he shall bring his offering to the LORD: one male lamb a year old without blemish for a burnt offering, and one ewe lamb a year old without blemish for a sin offering, and one ram without blemish for a peace offering,",
      "M": "He shall present his offering to the LORD: one unblemished year-old male lamb for a burnt offering, one unblemished year-old female lamb for a sin offering, and one unblemished ram for a fellowship offering,",
      "T": "He brings the LORD a complete offering: a yearling lamb as a burnt offering, a yearling ewe as a sin offering, and a ram as a fellowship offering — all without defect."
    },
    "15": {
      "L": "and a basket of unleavened bread, loaves of fine flour mixed with oil, and unleavened wafers smeared with oil, and their grain offering and their drink offerings.",
      "M": "along with a basket of unleavened bread — fine flour loaves mixed with oil and unleavened wafers brushed with oil — and their accompanying grain offerings and drink offerings.",
      "T": "A basket of unleavened bread — both the mixed loaves and the oil-brushed wafers — comes with the appropriate grain and drink offerings."
    },
    "16": {
      "L": "And the priest shall bring them before the LORD and offer his sin offering and his burnt offering.",
      "M": "The priest shall bring these before the LORD and sacrifice his sin offering and burnt offering.",
      "T": "The priest presents everything before the LORD and offers the sin offering and the burnt offering."
    },
    "17": {
      "L": "And he shall offer the ram as a sacrifice of peace offerings to the LORD, with the basket of unleavened bread; the priest shall also offer its grain offering and its drink offering.",
      "M": "He shall present the ram as a fellowship offering to the LORD, along with the basket of unleavened bread; the priest shall also offer its grain offering and drink offering.",
      "T": "Then the ram becomes the fellowship offering to the LORD — the communal meal sacrifice — accompanied by the unleavened bread, grain offering, and drink offering."
    },
    "18": {
      "L": "And the Nazirite shall shave his consecrated head at the entrance of the tent of meeting and shall take the hair from his consecrated head and put it on the fire that is under the sacrifice of the peace offerings.",
      "M": "The Nazirite shall shave his consecrated head at the entrance of the tent of meeting and take the hair from his consecrated head and put it on the fire under the fellowship offering.",
      "T": "At the tent entrance, the Nazirite shaves off the hair that has been growing throughout his vow — the visible sign of his consecration — and places it on the fire of the fellowship sacrifice."
    },
    "19": {
      "L": "And the priest shall take the boiled shoulder of the ram and one unleavened loaf from the basket and one unleavened wafer, and shall put them on the hands of the Nazirite after he has shaved his consecrated head.",
      "M": "The priest shall take the boiled shoulder of the ram, one unleavened loaf from the basket, and one unleavened wafer, and place them in the hands of the Nazirite after he has shaved his consecrated head.",
      "T": "The priest takes the cooked shoulder of the ram plus one loaf and one wafer from the unleavened basket and places them in the Nazirite's own hands."
    },
    "20": {
      "L": "And the priest shall wave them as a wave offering before the LORD; they are holy, for the priest, with the breast of the wave offering and the thigh of the heave offering; and after that the Nazirite may drink wine.",
      "M": "The priest shall wave them as a wave offering before the LORD. This is a holy portion for the priest, along with the breast of the wave offering and the thigh of the contribution offering. After this, the Nazirite may drink wine.",
      "T": "With the Nazirite's hands holding the food, the priest waves everything before the LORD — a joint presentation. These portions go to the priest; the vow is complete, and the Nazirite is free to drink wine again."
    },
    "21": {
      "L": "This is the law of the Nazirite who takes a vow. His offering to the LORD shall be according to his vow as a Nazirite, besides what else he can afford; according to his vow that he takes, so he shall do according to the law of his separation.",
      "M": "This is the law of the Nazirite who makes a vow. He shall bring to the LORD the offering required by his Nazirite vow, in addition to whatever else he can afford. In accordance with his vow, he shall carry out everything required by the law of his separation.",
      "T": "This is the governing rule for anyone who takes the Nazirite vow: the specified offerings are the minimum; he may bring more according to his means. He has vowed, and the vow must be fulfilled to the letter."
    },
    "22": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "23": {
      "L": "Speak to Aaron and his sons, saying: Thus you shall bless the children of Israel; say to them:",
      "M": "Tell Aaron and his sons: This is how you are to bless the Israelites. Say to them:",
      "T": "Say this to Aaron and his sons: This is the blessing you shall pronounce over Israel — these exact words:"
    },
    "24": {
      "L": "The LORD bless you and keep you;",
      "M": "May the LORD bless you and keep you;",
      "T": "May the LORD bless you and keep you safe —"
    },
    "25": {
      "L": "the LORD make his face shine upon you and be gracious to you;",
      "M": "may the LORD make his face shine on you and be gracious to you;",
      "T": "may the LORD make his face shine toward you and show you his grace —"
    },
    "26": {
      "L": "the LORD lift up his face toward you and give you peace.",
      "M": "may the LORD lift up his face toward you and grant you peace.",
      "T": "may the LORD lift his face toward you and give you wholeness and peace."
    },
    "27": {
      "L": "So they shall put my name upon the children of Israel, and I will bless them.",
      "M": "This is how they will put my name on the Israelites, and I will bless them.",
      "T": "By this blessing they place my name upon my people — and I myself will bless them."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'numbers')
        merge_tier(existing, NUMBERS, tier_key)
        save(tier_dir, 'numbers', existing)
    print('Numbers 1–6 written.')

if __name__ == '__main__':
    main()
