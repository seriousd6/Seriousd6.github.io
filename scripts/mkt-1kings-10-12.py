"""
MKT 1 Kings chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1kings-10-12.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with mkt-1kings-1-6.py, mkt-1kings-13-18.py.
- H430 (אֱלֹהִים): "God" in all tiers.
- H2617 (חֶסֶד): Not prominent in chs 10–12.
- H5315 (נֶפֶשׁ): 11:37 "all that your soul desires"; L "soul," M/T "heart." In context the
  idiom is about wholehearted desire, not the Greek immortal soul.
- H7307 (רוּחַ): 10:5 "there was no more spirit in her" — the queen's breath/spirit left her
  in astonishment. L "spirit," M/T "breath." This is the embodied-self breath, not the
  divine Spirit; no capitalisation.
- H2451 (חָכְמָה / wisdom): "wisdom" throughout all tiers in ch 10 (17 occurrences).
  Ch 10 is the climax of the wisdom-motif; T notes this arc.
- H3678 (kisse / throne): "throne" all tiers.
- H4196 (mizbeach / altar): "altar" all tiers.
- H1285 (בְּרִית / covenant): Not prominent in chs 10–12.
- H4906 (maṣṣēbôt / sacred pillars): "sacred pillars" in ch 11.
- H1116 (bāmôt / high places): "high places" in L/M; T "hilltop shrines" at 11:7 where
  the cultic critique is sharpest.
- H842 (ʾăšērāh): "Asherah poles" in ch 11.
- H6253 (Ashtoreth): Preserved as proper name; "goddess of the Sidonians" gloss retained.
- H3645 (Chemosh): Preserved as proper name; "abomination of Moab" note in T.
- H4432 (Molech): Preserved as proper name; "abomination of the Ammonites."
- H4445 (Milcom): Preserved as proper name for the Ammonite deity.
- H1168 (Baal): Not prominent in this range; appears peripherally.
- H5030 (nābî'): "prophet" throughout.
- H1004 (bayit / house): "house" in all tiers — carries temple/dynasty ambiguity; in ch 11
  "house of David" is the dynasty.
- H7626 (šēbeṭ / tribe): "tribe" throughout.
- H4467 (mamlākāh / kingdom): "kingdom" throughout.
- H7307 ruach in 11:5 context: Not present; cf. above note on 10:5.
- Ch 10 — Queen of Sheba narrative: She is a type of the Gentile world drawn to God's
  wisdom through Israel. T makes this eschatological overtone explicit (cf. Matt 12:42).
  Her final gift exchange (v.13) is rendered to bring out the royal generosity of
  Solomon's return gift — "all her desire" plus his royal bounty.
- Ch 11 — Solomon's apostasy: The Deuteronomistic verdict is severe. The narrator uses
  "turned after/away" (H5186) as a technical term for covenant defection; L preserves
  this verb literally. T notes that the fracture is not political but theological.
  - 11:29–39 Ahijah's dramatic acted prophecy: Tearing the new garment into 12 pieces
    echoes later prophetic sign-acts (cf. Jer 13, Ezek 4). T makes the performative
    dimension explicit.
  - The adversaries (Hadad, Rezon, Jeroboam) are named as agents God "stirred up"
    (H6965) — the same verb used of Cyrus in Isaiah. T notes this as divine governance
    through opposition.
- Ch 12 — The kingdom divides: Rehoboam's fatal choice fulfills Ahijah's prophecy.
  - 12:15: The narrator's aside "for the turn of events was from the LORD" is the
    Deuteronomistic signature — divine providence works through human folly. T makes
    this explicit.
  - 12:16: "What portion do we have in David?" echoes Sheba's rebellion (2 Sam 20:1)
    almost verbatim — T notes the repetition as the finalisation of what that earlier
    rebellion prefigured.
  - 12:28–29 Golden calves: The formula "Here are your gods, O Israel, who brought you
    up out of Egypt" deliberately echoes Aaron's golden calf (Exod 32:4). T makes this
    explicit — Jeroboam re-enacts the wilderness apostasy at a political level.
  - 12:32–33: Jeroboam's counter-calendar — a feast in the eighth month instead of the
    seventh, "devised from his own heart." The phrase is damning in Deuteronomistic terms.
- Aspect: Waw-consecutive imperfects throughout = narrative past (simple past in English).
  Divine speeches (11:11-13, 11:31-39) use future/promise forms.
- OT echoes:
  - 10:9: The queen's blessing "because the LORD loved Israel forever" echoes Deut 7:8
    and 2 Sam 7:16. T notes this.
  - 10:26-29: Solomon's horses and chariots from Egypt directly violate Deut 17:16-17
    (the law of the king). T notes this as the narrator's subtle critique of Solomon's
    excess — the accumulation of gold, wives, and horses was exactly what the king was
    forbidden. Ch 11's fall is already prepared here.
  - 11:2: "You shall not go in to them" echoes Exod 34:16 and Deut 7:3-4.
  - 11:36: "a lamp before me in Jerusalem" — the Davidic lamp-promise echoes 2 Sam 21:17;
    1 Kgs 15:4; 2 Kgs 8:19. T traces this motif.
  - 12:28 Aaron's formula: See note above.
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

KINGS = {
  "10": {
    "1": {
      "L": "And the queen of Sheba heard of the fame of Solomon concerning the name of the LORD, and she came to test him with hard questions.",
      "M": "When the queen of Sheba heard of Solomon's fame connected with the name of the LORD, she came to test him with difficult questions.",
      "T": "When the queen of Sheba heard of Solomon's fame—fame inseparable from the name of the LORD—she came to put his wisdom to the test with probing questions."
    },
    "2": {
      "L": "And she came to Jerusalem with a very great train, with camels bearing spices and very much gold and precious stones. And she came to Solomon and spoke to him all that was in her heart.",
      "M": "She arrived in Jerusalem with a very large retinue, with camels carrying spices, great quantities of gold, and precious stones. She came to Solomon and talked with him about everything on her mind.",
      "T": "She arrived at Jerusalem with an enormous caravan—camels laden with spices, great quantities of gold, and precious stones. She came to Solomon and poured out before him everything that was in her heart."
    },
    "3": {
      "L": "And Solomon told her all her questions; there was not anything hidden from the king that he did not tell her.",
      "M": "Solomon answered all her questions; there was nothing so obscure that the king could not explain it to her.",
      "T": "Solomon answered every question she put to him. Nothing was too difficult, nothing too obscure—the king had an answer for it all."
    },
    "4": {
      "L": "And when the queen of Sheba saw all the wisdom of Solomon and the house that he had built,",
      "M": "When the queen of Sheba witnessed all of Solomon's wisdom and the palace he had built,",
      "T": "When the queen of Sheba took in the full scope of Solomon's wisdom—and saw with her own eyes the palace he had built—"
    },
    "5": {
      "L": "the food of his table, the seating of his servants, the attendance of his ministers and their clothing, his cupbearers, and his ascent by which he went up to the house of the LORD, there was no more spirit in her.",
      "M": "the food at his table, the seating of his officials, the attendance of his servants and their clothing, his cupbearers, and the stairway by which he went up to the house of the LORD—she was left breathless.",
      "T": "the food set at his table, the orderly seating of his court, the livery of his servants, his cupbearers, and the covered walkway by which he ascended to the LORD's house—the breath went out of her. She was overwhelmed."
    },
    "6": {
      "L": "And she said to the king, 'The report was true that I heard in my own land of your acts and of your wisdom,",
      "M": "She said to the king, 'The report I heard in my own country about your deeds and your wisdom was true.",
      "T": "She said to the king, 'Everything I heard back in my own land about you—your deeds, your wisdom—it was all true."
    },
    "7": {
      "L": "but I did not believe the words until I came and my own eyes had seen it. And behold, the half was not told me. Your wisdom and prosperity exceed the fame that I heard.",
      "M": "But I did not believe the reports until I came and saw it with my own eyes. And even now the half was not told me—your wisdom and your prosperity exceed the fame I heard.",
      "T": "But I didn't believe it until I came and saw it myself. And even now, what I was told was only half the truth. Your wisdom and your prosperity surpass every report I had received."
    },
    "8": {
      "L": "Happy are your men, happy are these your servants who stand before you continually and hear your wisdom!",
      "M": "How fortunate are your men! How fortunate are these servants of yours, who stand before you continually and hear your wisdom!",
      "T": "How blessed are your men! How privileged are these servants of yours, who stand before you day after day and drink in your wisdom!"
    },
    "9": {
      "L": "Blessed be the LORD your God, who delighted in you to set you on the throne of Israel! Because the LORD loved Israel forever, he made you king to do justice and righteousness.",
      "M": "Praise the LORD your God, who delighted in you and set you on the throne of Israel! Because the LORD has loved Israel forever, he has made you king to maintain justice and righteousness.",
      "T": "Blessed be the LORD your God, who delighted in you and placed you on Israel's throne! The LORD's love for Israel is everlasting, and because of that love he has made you king—to do right and to do justice."
    },
    "10": {
      "L": "And she gave the king one hundred and twenty talents of gold and very great quantities of spices and precious stones. Never again came such an abundance of spices as these which the queen of Sheba gave to King Solomon.",
      "M": "She gave the king a hundred and twenty talents of gold and very large quantities of spices and precious stones. Never again did such an abundance of spices come in as those which the queen of Sheba gave to King Solomon.",
      "T": "She presented the king with a hundred and twenty talents of gold, enormous quantities of spices, and precious stones. Never again would such a quantity of spices arrive as those the queen of Sheba gave to King Solomon."
    },
    "11": {
      "L": "And also the navy of Hiram, which carried gold from Ophir, brought in from Ophir very great quantities of almug wood and precious stones.",
      "M": "The ships of Hiram, which brought gold from Ophir, also brought in great quantities of almugwood and precious stones.",
      "T": "Hiram's fleet, which hauled gold from Ophir, also brought in vast quantities of almugwood and precious stones."
    },
    "12": {
      "L": "And the king made of the almug wood pillars for the house of the LORD and for the king's house, also lyres and harps for the singers. No such almug wood has come or been seen to this day.",
      "M": "From the almugwood the king made supports for the LORD's temple and for the royal palace, and also lyres and harps for the musicians. No such almugwood has been imported or seen to this day.",
      "T": "The king used the almugwood to make support-posts for the LORD's house and the royal palace, and also lyres and harps for the musicians. Such almugwood has never been seen before or since, to this very day."
    },
    "13": {
      "L": "And King Solomon gave to the queen of Sheba all her desire, whatever she asked, besides what he gave her of his royal bounty. So she turned and went to her own country, she and her servants.",
      "M": "King Solomon gave the queen of Sheba everything she desired and asked for, in addition to all that he gave her out of his royal generosity. Then she and her servants turned and went back to her own country.",
      "T": "King Solomon gave the queen of Sheba all she desired, whatever she asked for—and over and above that, out of his royal generosity. Then she turned and made the journey home, she and her servants."
    },
    "14": {
      "L": "Now the weight of gold that came to Solomon in one year was six hundred and sixty-six talents of gold,",
      "M": "The weight of gold that came to Solomon in a single year was six hundred and sixty-six talents,",
      "T": "The gold that arrived for Solomon in a single year weighed six hundred and sixty-six talents—"
    },
    "15": {
      "L": "besides that from the merchants and from the trade of the spice dealers and from all the kings of Arabia and from the governors of the land.",
      "M": "not counting what came from the merchants and traders, from all the kings of Arabia, and from the governors of the land.",
      "T": "and that was apart from what came in from merchants, spice traders, all the kings of Arabia, and the regional governors."
    },
    "16": {
      "L": "And King Solomon made two hundred large shields of beaten gold; six hundred shekels of gold went into each shield.",
      "M": "King Solomon made two hundred large shields of hammered gold—six hundred shekels of gold went into each shield.",
      "T": "King Solomon had two hundred large shields made of hammered gold, each one requiring six hundred shekels of gold."
    },
    "17": {
      "L": "And he made three hundred shields of beaten gold; three minas of gold went into each shield. And the king put them in the House of the Forest of Lebanon.",
      "M": "He also made three hundred smaller shields of hammered gold—three minas of gold per shield—and the king placed them in the House of the Forest of Lebanon.",
      "T": "He made three hundred smaller shields of hammered gold—three minas each—and had them all placed in the House of the Forest of Lebanon."
    },
    "18": {
      "L": "Moreover the king made a great throne of ivory and overlaid it with the finest gold.",
      "M": "The king also made a large throne of ivory and overlaid it with the finest gold.",
      "T": "The king also had a magnificent throne made of ivory, overlaid with the finest gold."
    },
    "19": {
      "L": "The throne had six steps, and the top of the throne was round at the back, and there were armrests on each side of the seat, and two lions standing beside the armrests.",
      "M": "The throne had six steps, and the back of the throne was rounded at the top. There were armrests on each side of the seat, and two lions stood beside the armrests.",
      "T": "It had six steps; the top of the throne was curved and rounded at the back. On each side of the seat were armrests, and two lions stood beside them."
    },
    "20": {
      "L": "And twelve lions stood there on the six steps on the one side and on the other. Nothing like it was ever made in any kingdom.",
      "M": "Twelve lions stood on the six steps, six on each side. Nothing like it had been made in any kingdom.",
      "T": "On the six steps, six to a side, stood twelve lions in total. Nothing like this throne existed in any kingdom on earth."
    },
    "21": {
      "L": "All King Solomon's drinking vessels were of gold, and all the vessels of the House of the Forest of Lebanon were of pure gold. None were of silver; it was not considered of any account in the days of Solomon.",
      "M": "All King Solomon's drinking cups were of gold, and all the vessels in the House of the Forest of Lebanon were of pure gold. Silver was not considered worth anything in Solomon's day.",
      "T": "Every drinking cup of King Solomon was gold, and every vessel in the House of the Forest of Lebanon was pure gold. Silver counted for nothing in those days—it was that abundant."
    },
    "22": {
      "L": "For the king had a fleet of ships of Tarshish at sea with the fleet of Hiram. Once every three years the fleet of Tarshish would come in, bringing gold, silver, ivory, apes, and peacocks.",
      "M": "The king had a fleet of Tarshish ships at sea together with Hiram's fleet. Once every three years the Tarshish fleet would arrive, bringing gold, silver, ivory, apes, and peacocks.",
      "T": "The king had a fleet of Tarshish ships sailing in partnership with Hiram's fleet. Every three years a voyage would return, laden with gold, silver, ivory, apes, and peacocks."
    },
    "23": {
      "L": "So King Solomon exceeded all the kings of the earth in riches and in wisdom.",
      "M": "King Solomon surpassed all the kings of the earth in riches and wisdom.",
      "T": "Solomon outstripped every king on earth—in wealth and in wisdom."
    },
    "24": {
      "L": "And all the earth sought the presence of Solomon to hear his wisdom, which God had put in his heart.",
      "M": "And all the peoples of the earth sought an audience with Solomon to hear the wisdom that God had placed in his heart.",
      "T": "From all over the earth people sought an audience with Solomon, drawn by the wisdom God had planted in his heart."
    },
    "25": {
      "L": "Every one of them brought his present: articles of silver and gold, garments, weapons, spices, horses, and mules, so much year by year.",
      "M": "Year after year, every visitor brought a gift—silver and gold vessels, garments, weapons, spices, horses, and mules.",
      "T": "Year after year they came, and every visitor brought a gift: silver and gold articles, garments, weapons, spices, horses, and mules."
    },
    "26": {
      "L": "And Solomon gathered together chariots and horsemen. He had fourteen hundred chariots and twelve thousand horsemen, whom he stationed in the chariot cities and with the king in Jerusalem.",
      "M": "Solomon accumulated chariots and cavalry—he had fourteen hundred chariots and twelve thousand horsemen—which he stationed in the chariot cities and with him in Jerusalem.",
      "T": "Solomon amassed chariots and cavalry: fourteen hundred chariots and twelve thousand horsemen, garrisoned in the chariot cities and stationed around him in Jerusalem."
    },
    "27": {
      "L": "And the king made silver as common in Jerusalem as stones, and he made cedars as plentiful as the sycamore trees in the Shephelah.",
      "M": "The king made silver as common in Jerusalem as stones, and cedars as plentiful as the sycamore-fig trees of the foothills.",
      "T": "The king made silver as ordinary in Jerusalem as pavement stones, and cedar wood as common as the sycamore trees of the lowlands."
    },
    "28": {
      "L": "And Solomon's horses were imported from Egypt and from Kue; the king's merchants received them from Kue at a price.",
      "M": "Solomon's horses were imported from Egypt and Kue—the king's traders received them from Kue at a fixed price.",
      "T": "Solomon's horses were imported from Egypt and Kue; the royal traders purchased them from Kue at set prices."
    },
    "29": {
      "L": "A chariot was imported from Egypt for six hundred shekels of silver and a horse for a hundred and fifty; and through them these were exported to all the kings of the Hittites and the kings of Syria.",
      "M": "A chariot cost six hundred shekels of silver when imported from Egypt, and a horse a hundred and fifty. Through the royal traders they were re-exported to all the kings of the Hittites and the kings of Aram.",
      "T": "From Egypt, a chariot went for six hundred shekels of silver, a horse for a hundred and fifty. Through the same royal agents, they were exported to all the Hittite and Aramean kings. Solomon sat at the hub of the entire trade."
    }
  },
  "11": {
    "1": {
      "L": "Now King Solomon loved many foreign women, the daughter of Pharaoh and women of the Moabites, Ammonites, Edomites, Sidonians, and Hittites,",
      "M": "King Solomon loved many foreign women—the daughter of Pharaoh as well as women from Moab, Ammon, Edom, Sidon, and among the Hittites—",
      "T": "King Solomon loved many foreign women—Pharaoh's daughter among them, plus women from Moab, Ammon, Edom, Sidon, and the Hittites—"
    },
    "2": {
      "L": "from the nations concerning which the LORD had said to the children of Israel, 'You shall not go in to them, neither shall they come in to you, for surely they will turn away your heart after their gods.' Solomon clung to these in love.",
      "M": "from nations about which the LORD had told the Israelites, 'You must not intermarry with them, nor they with you, for they will surely turn your hearts after their gods.' But Solomon clung to these women in love.",
      "T": "from the very nations about which the LORD had warned Israel: 'Do not intermarry with them—they will turn your heart to their gods.' Yet Solomon clung to these women with passion."
    },
    "3": {
      "L": "He had seven hundred wives of royal birth and three hundred concubines. And his wives turned away his heart.",
      "M": "He had seven hundred wives of royal standing and three hundred concubines. And his wives turned his heart away.",
      "T": "He had seven hundred royal wives and three hundred concubines. And it was his wives who turned his heart."
    },
    "4": {
      "L": "For it came to pass when Solomon was old, his wives turned away his heart after other gods, and his heart was not perfect with the LORD his God, as was the heart of David his father.",
      "M": "As Solomon grew old, his wives turned his heart after other gods, and his heart was not fully devoted to the LORD his God, as the heart of his father David had been.",
      "T": "When Solomon was old, his wives drew his heart away to other gods. His heart was no longer whole before the LORD his God—not as his father David's heart had been."
    },
    "5": {
      "L": "For Solomon went after Ashtoreth the goddess of the Sidonians, and after Milcom the abomination of the Ammonites.",
      "M": "Solomon followed Ashtoreth the goddess of the Sidonians, and Milcom the detestable god of the Ammonites.",
      "T": "Solomon went after Ashtoreth, the goddess of the Sidonians, and after Milcom, the detestable idol of the Ammonites."
    },
    "6": {
      "L": "And Solomon did what was evil in the sight of the LORD and did not go fully after the LORD, as David his father had done.",
      "M": "So Solomon did what was evil in the LORD's sight and did not follow the LORD completely as his father David had done.",
      "T": "Solomon did what was evil in the LORD's eyes. He did not give the LORD his full allegiance the way his father David had."
    },
    "7": {
      "L": "Then Solomon built a high place for Chemosh the abomination of Moab on the mountain that is before Jerusalem, and for Molech the abomination of the children of Ammon.",
      "M": "Then Solomon built a high place for Chemosh, the detestable god of Moab, on the hill east of Jerusalem, and for Molech, the detestable god of the Ammonites.",
      "T": "Solomon even built hilltop shrines—one for Chemosh, the detestable god of Moab, and one for Molech, the detestable god of Ammon—on the hill facing Jerusalem."
    },
    "8": {
      "L": "And likewise he did for all his foreign wives, who burned incense and sacrificed to their gods.",
      "M": "He did the same for all his foreign wives, who burned incense and offered sacrifices to their gods.",
      "T": "He built the same for all his foreign wives, and they burned incense and made offerings to their gods. The hill outside Jerusalem became a spiritual sewer of foreign cults."
    },
    "9": {
      "L": "And the LORD was angry with Solomon, because his heart was turned from the LORD, the God of Israel, who had appeared to him twice.",
      "M": "The LORD was angry with Solomon because his heart had turned away from the LORD, the God of Israel, who had appeared to him twice.",
      "T": "The LORD burned with anger against Solomon, because his heart had turned away from the LORD, the God of Israel—who had appeared to him twice in person."
    },
    "10": {
      "L": "And he had commanded him concerning this thing, that he should not go after other gods. But he did not keep what the LORD commanded.",
      "M": "He had warned him expressly about this very thing—not to follow other gods. But Solomon did not keep the LORD's command.",
      "T": "God had given him this command explicitly—do not run after other gods. But Solomon did not keep it."
    },
    "11": {
      "L": "So the LORD said to Solomon, 'Inasmuch as this has been your practice and you have not kept my covenant and my statutes, which I have commanded you, I will surely tear the kingdom away from you and give it to your servant.",
      "M": "So the LORD said to Solomon, 'Since this is what you have done—you have not kept my covenant or my statutes that I commanded you—I will certainly tear the kingdom from you and give it to one of your servants.",
      "T": "So the LORD said to Solomon: 'Because this is what you have done—because you have broken my covenant and disregarded my statutes that I commanded you—I will tear the kingdom away from you and give it to one of your servants."
    },
    "12": {
      "L": "Yet for the sake of David your father I will not do it in your days; I will tear it out of the hand of your son.",
      "M": "However, for the sake of your father David, I will not do this during your lifetime. I will tear it away from your son.",
      "T": "But not during your lifetime—for the sake of your father David. It is from your son's hand that I will tear it."
    },
    "13": {
      "L": "However, I will not tear away all the kingdom. I will give one tribe to your son, for the sake of David my servant and for the sake of Jerusalem that I have chosen.",
      "M": "Yet I will not tear away the entire kingdom. I will give one tribe to your son, for the sake of my servant David and for the sake of Jerusalem, which I have chosen.",
      "T": "Even so, I will not take the whole kingdom. I will leave one tribe for your son—for the sake of my servant David, and for the sake of Jerusalem, which I have chosen."
    },
    "14": {
      "L": "And the LORD raised up an adversary against Solomon, Hadad the Edomite. He was of the royal seed in Edom.",
      "M": "The LORD raised up an adversary against Solomon: Hadad the Edomite, who was of royal descent in Edom.",
      "T": "The LORD stirred up an adversary against Solomon: Hadad the Edomite, a man of Edom's royal line."
    },
    "15": {
      "L": "For when David was in Edom, and Joab the commander of the army went up to bury the slain, he struck down every male in Edom—",
      "M": "When David had been in Edom, Joab the army commander had gone there to bury the Israelite dead and had struck down every male in Edom—",
      "T": "Years earlier, when David's forces were in Edom, Joab the army commander had gone there to bury the fallen—and had killed every male in Edom."
    },
    "16": {
      "L": "for Joab and all Israel had remained there six months, until he had cut off every male in Edom—",
      "M": "for Joab and all Israel had stayed there six months until every male in Edom had been killed—",
      "T": "Joab and all Israel had stayed there six months until not one male was left alive in Edom."
    },
    "17": {
      "L": "but Hadad fled to Egypt, he and certain Edomites of his father's servants with him, Hadad being yet a little child.",
      "M": "But Hadad had escaped to Egypt with some Edomites, servants of his father, while Hadad was still a small boy.",
      "T": "Hadad had escaped—still just a boy—fleeing with some of his father's servants to Egypt."
    },
    "18": {
      "L": "And they arose from Midian and came to Paran, and they took men with them from Paran and came to Egypt, to Pharaoh king of Egypt, who gave him a house and assigned him food and gave him land.",
      "M": "They set out from Midian, went to Paran, gathered some men from Paran, and arrived in Egypt, where Pharaoh gave Hadad a house, provided for him, and assigned him land.",
      "T": "They set out from Midian, passed through Paran picking up men along the way, and eventually came to Egypt, where Pharaoh took Hadad in, gave him a house, provided his food, and assigned him land."
    },
    "19": {
      "L": "And Hadad found great favour in the sight of Pharaoh, so that he gave him as wife the sister of his own wife, the sister of Tahpenes the queen.",
      "M": "Hadad won great favour with Pharaoh, who gave him as his wife the sister of Pharaoh's own wife—the sister of Queen Tahpenes.",
      "T": "Hadad won such great favour with Pharaoh that Pharaoh gave him the sister of his own queen, Tahpenes, as a wife."
    },
    "20": {
      "L": "And the sister of Tahpenes bore him Genubath his son, whom Tahpenes weaned in Pharaoh's house. And Genubath was in Pharaoh's house among the sons of Pharaoh.",
      "M": "Tahpenes's sister bore him a son named Genubath, whom Tahpenes weaned in Pharaoh's household. Genubath grew up there among Pharaoh's own sons.",
      "T": "Tahpenes's sister bore Hadad a son named Genubath, whom Tahpenes herself weaned in Pharaoh's palace. Genubath was raised there alongside Pharaoh's own children."
    },
    "21": {
      "L": "But when Hadad heard in Egypt that David slept with his fathers and that Joab the commander of the army was dead, Hadad said to Pharaoh, 'Let me depart, that I may go to my own country.'",
      "M": "When Hadad in Egypt heard that David had died and that Joab the army commander was also dead, he said to Pharaoh, 'Let me go home to my own country.'",
      "T": "When news reached Hadad in Egypt that David had died and that Joab was dead too, he said to Pharaoh, 'Let me go. I want to return to my own country.'"
    },
    "22": {
      "L": "But Pharaoh said to him, 'What have you lacked with me, that you seek to go to your own country?' And he said, 'Nothing. Yet please let me go in any case.'",
      "M": "Pharaoh replied, 'What have you lacked here with me, that you want to go back to your own country?' Hadad said, 'Nothing—but please, let me go.'",
      "T": "Pharaoh said, 'What have you lacked here? Why would you want to go home?' 'Nothing,' said Hadad, 'but please—let me go.'"
    },
    "23": {
      "L": "And God also raised up against him another adversary, Rezon the son of Eliada, who had fled from his master Hadadezer king of Zobah.",
      "M": "God also raised up another adversary against Solomon: Rezon son of Eliada, who had fled from his master Hadadezer king of Zobah.",
      "T": "God raised up yet another adversary against Solomon: Rezon son of Eliada, who had defected from his master Hadadezer, king of Zobah."
    },
    "24": {
      "L": "He gathered men to him and became leader of a marauding band after David killed the men of Zobah. They went to Damascus and dwelt there and reigned in Damascus.",
      "M": "Rezon gathered men around him after David had destroyed the forces of Zobah. They went to Damascus and settled there, and he became king in Damascus.",
      "T": "After David destroyed the Zobahite forces, Rezon gathered a band of raiders and established himself in Damascus, where he became king."
    },
    "25": {
      "L": "He was an adversary of Israel all the days of Solomon, and this added to the mischief of Hadad. He reigned over Syria and hated Israel.",
      "M": "He was an adversary of Israel throughout Solomon's lifetime. Together with the trouble caused by Hadad, Rezon became a persistent threat; he ruled Aram and was hostile to Israel.",
      "T": "All Solomon's life Rezon remained a thorn in Israel's side. He ruled Aram and harboured deep hostility toward Israel—compounding the pressure from Hadad."
    },
    "26": {
      "L": "Jeroboam the son of Nebat, an Ephrathite of Zereda, a servant of Solomon, whose mother's name was Zeruah, a widow, also lifted up his hand against the king.",
      "M": "Jeroboam son of Nebat, an Ephraimite from Zeredah—one of Solomon's officials, whose mother was a widow named Zeruah—also rebelled against the king.",
      "T": "And from within the kingdom itself: Jeroboam son of Nebat, an Ephraimite from Zeredah and one of Solomon's own officials, raised his hand against the king. His mother, Zeruah, was a widow."
    },
    "27": {
      "L": "And this was the reason why he lifted up his hand against the king: Solomon built the Millo and closed up the breach of the city of David his father.",
      "M": "This is how it came about: Solomon had been building the Millo and repairing the breach in the city wall of his father David.",
      "T": "Here is the background: Solomon had been building the Millo and sealing the breaches in the wall of the city of David."
    },
    "28": {
      "L": "The man Jeroboam was a man of valour. Solomon saw that the young man was industrious, and he put him in charge of all the forced labour of the house of Joseph.",
      "M": "Jeroboam was a capable man. When Solomon saw how hardworking the young man was, he put him over all the forced labour of the house of Joseph.",
      "T": "Jeroboam was a capable, energetic man. Solomon noticed his drive and made him supervisor over all the forced labour assigned to the tribes of Joseph."
    },
    "29": {
      "L": "And at that time, when Jeroboam went out of Jerusalem, the prophet Ahijah the Shilonite found him on the road. Now he had clothed himself with a new garment, and the two of them were alone in the open country.",
      "M": "At that time, as Jeroboam was leaving Jerusalem, the prophet Ahijah the Shilonite met him on the road. Ahijah was wearing a new garment, and the two of them were alone in the countryside.",
      "T": "It was around this time that Jeroboam was leaving Jerusalem when the prophet Ahijah of Shiloh met him on the road. Ahijah was wearing a new garment—and the two of them were alone in the open fields."
    },
    "30": {
      "L": "Then Ahijah took hold of the new garment that was on him and tore it into twelve pieces.",
      "M": "Ahijah took hold of the new garment he was wearing and tore it into twelve pieces.",
      "T": "Ahijah seized the new garment he had on and tore it—twelve pieces."
    },
    "31": {
      "L": "And he said to Jeroboam, 'Take ten pieces for yourself, for thus says the LORD, the God of Israel, \"Behold, I am tearing the kingdom from the hand of Solomon and I will give you ten tribes.\"'",
      "M": "He said to Jeroboam, 'Take ten pieces for yourself. For this is what the LORD, the God of Israel, says: \"I am tearing the kingdom from Solomon's hand and giving you ten tribes.\"'",
      "T": "He said to Jeroboam: 'Take ten pieces for yourself. This is the word of the LORD, the God of Israel: \"I am tearing the kingdom out of Solomon's hand—and I am giving you ten tribes.\"'"
    },
    "32": {
      "L": "'But he shall have one tribe, for the sake of my servant David and for the sake of Jerusalem, the city that I have chosen out of all the tribes of Israel.'",
      "M": "'He will keep one tribe—for the sake of my servant David and for the sake of Jerusalem, the city I have chosen from all the tribes of Israel.'",
      "T": "'But he will retain one tribe—for the sake of my servant David, and for the sake of Jerusalem, the city I chose from all the tribes of Israel.'"
    },
    "33": {
      "L": "'Because they have forsaken me and worshipped Ashtoreth the goddess of the Sidonians, Chemosh the god of Moab, and Milcom the god of the children of Ammon, and have not walked in my ways, to do what is right in my eyes and to keep my statutes and my judgments, as David his father did.'",
      "M": "'Because they have abandoned me and worshipped Ashtoreth the goddess of the Sidonians, Chemosh the god of Moab, and Milcom the god of the Ammonites. They have not walked in my ways or done what is right in my eyes, nor kept my statutes and ordinances as David his father did.'",
      "T": "'Because they have abandoned me—gone after Ashtoreth the Sidonian goddess, Chemosh the god of Moab, Milcom the god of Ammon. They have not walked in my ways or done what is right before me, nor kept my statutes and ordinances as David their father did.'"
    },
    "34": {
      "L": "'Yet I will not take the whole kingdom out of his hand, but I will make him prince all the days of his life, for the sake of David my servant whom I chose, because he kept my commandments and my statutes.'",
      "M": "'But I will not take the whole kingdom from him. I will keep him as ruler for the rest of his life, for the sake of my servant David whom I chose, because David kept my commandments and statutes.'",
      "T": "'But I will not strip the whole kingdom from him—I will make him ruler for the rest of his life, for the sake of my servant David whom I chose. David kept my commandments and statutes.'"
    },
    "35": {
      "L": "'But I will take the kingdom out of his son's hand and give it to you—ten tribes.'",
      "M": "'I will take the kingdom from his son's hand and give it to you—ten tribes.'",
      "T": "'It is from his son's hand that I will take the kingdom and give it to you—all ten tribes.'"
    },
    "36": {
      "L": "'And to his son I will give one tribe, that David my servant may always have a lamp before me in Jerusalem, the city where I have chosen to put my name.'",
      "M": "'I will give his son one tribe, so that my servant David may always have a lamp before me in Jerusalem, the city where I have chosen to put my name.'",
      "T": "'To his son I will give one tribe—so that my servant David may always have a lamp burning before me in Jerusalem, the city I have chosen as the dwelling-place of my name.'"
    },
    "37": {
      "L": "'And you I will take, and you shall reign over all that your soul desires, and you shall be king over Israel.'",
      "M": "'I will take you, and you will reign over all that your heart desires, and you will be king over Israel.'",
      "T": "'I am taking you—and you will reign over everything your heart desires. You will be king over Israel.'"
    },
    "38": {
      "L": "'And if you will listen to all that I command you, and will walk in my ways, and do what is right in my eyes by keeping my statutes and my commandments, as David my servant did, then I will be with you and will build you a sure house, as I built for David, and I will give Israel to you.'",
      "M": "'If you obey all I command you, walk in my ways, and do what is right in my sight by keeping my statutes and commandments as my servant David did, then I will be with you. I will build you a lasting dynasty as I did for David, and I will give you Israel.'",
      "T": "'If you will listen to everything I command you, walk in my ways, and do what is right before me—keeping my statutes and commandments as my servant David did—then I will be with you. I will build you a dynasty that endures, just as I built one for David, and I will give you Israel.'"
    },
    "39": {
      "L": "'And I will afflict the offspring of David because of this, but not forever.'",
      "M": "'I will humiliate the descendants of David because of this—but not forever.'",
      "T": "'I will chasten David's line because of this—but not forever.'"
    },
    "40": {
      "L": "Solomon sought to kill Jeroboam. But Jeroboam arose and fled to Egypt, to Shishak king of Egypt, and was in Egypt until the death of Solomon.",
      "M": "Solomon tried to kill Jeroboam, but Jeroboam fled to Egypt and went to Shishak king of Egypt. He stayed in Egypt until Solomon's death.",
      "T": "Solomon moved to kill Jeroboam, but Jeroboam fled to Egypt and sought refuge with Shishak, the king of Egypt. He stayed there until Solomon died."
    },
    "41": {
      "L": "Now the rest of the acts of Solomon and all that he did, and his wisdom, are they not written in the book of the acts of Solomon?",
      "M": "As for the rest of Solomon's acts—all he did and his wisdom—are they not written in the Book of the Acts of Solomon?",
      "T": "The rest of Solomon's deeds—all that he did, and his wisdom—are they not recorded in the Book of the Acts of Solomon?"
    },
    "42": {
      "L": "And the time that Solomon reigned in Jerusalem over all Israel was forty years.",
      "M": "Solomon reigned in Jerusalem over all Israel for forty years.",
      "T": "Solomon reigned over all Israel from Jerusalem for forty years."
    },
    "43": {
      "L": "And Solomon slept with his fathers and was buried in the city of David his father. And Rehoboam his son reigned in his place.",
      "M": "Then Solomon rested with his ancestors and was buried in the city of his father David. And his son Rehoboam succeeded him as king.",
      "T": "Then Solomon died and was buried with his ancestors in the city of David his father. His son Rehoboam became king in his place."
    }
  },
  "12": {
    "1": {
      "L": "And Rehoboam went to Shechem, for all Israel had come to Shechem to make him king.",
      "M": "Rehoboam went to Shechem, because all Israel had gathered at Shechem to make him king.",
      "T": "Rehoboam went to Shechem—the whole nation had gathered there to crown him."
    },
    "2": {
      "L": "And it came to pass when Jeroboam the son of Nebat heard of it—for he was yet in Egypt, where he had fled from the presence of King Solomon—Jeroboam dwelt in Egypt.",
      "M": "When Jeroboam son of Nebat heard about it—he was still in Egypt, where he had fled from King Solomon—he remained there in Egypt.",
      "T": "Jeroboam son of Nebat heard the news while he was still in Egypt, where he had fled from Solomon. He stayed in Egypt."
    },
    "3": {
      "L": "And they sent and called him. And Jeroboam and all the assembly of Israel came and spoke to Rehoboam, saying,",
      "M": "But they sent for him, and Jeroboam came back. He and the whole assembly of Israel came to Rehoboam and said,",
      "T": "The people sent for him. Jeroboam returned, and he and the whole assembly of Israel came before Rehoboam with a demand:"
    },
    "4": {
      "L": "'Your father made our yoke heavy. Now therefore lighten the hard service of your father and his heavy yoke that he put upon us, and we will serve you.'",
      "M": "'Your father made our burden heavy. Lighten the harsh service and heavy yoke your father imposed on us, and we will serve you.'",
      "T": "'Your father loaded us down. Lighten the crushing demands and the heavy yoke he put on us, and we will serve you.'"
    },
    "5": {
      "L": "And he said to them, 'Depart for three days, then come back to me.' So the people departed.",
      "M": "He said to them, 'Go away for three days, then come back to me.' So the people went away.",
      "T": "'Give me three days,' he said, 'then return.' And the people left."
    },
    "6": {
      "L": "And King Rehoboam consulted with the elders who had stood before Solomon his father while he was alive, saying, 'How do you advise me to answer this people?'",
      "M": "King Rehoboam consulted the elders who had served his father Solomon during his lifetime. 'What is your advice?' he asked. 'How should I answer these people?'",
      "T": "King Rehoboam consulted the older advisers who had served his father Solomon. 'What do you counsel?' he asked. 'How should I answer these people?'"
    },
    "7": {
      "L": "And they spoke to him, saying, 'If you will be a servant to this people today and serve them, and answer them and speak good words to them, then they will be your servants forever.'",
      "M": "They said to him, 'If today you will be a servant to this people and serve them—answer them with kind words—they will be your servants for life.'",
      "T": "'If today you will be a servant to these people,' the elders said, 'if you serve them and answer them with generous words, they will be your loyal servants forever.'"
    },
    "8": {
      "L": "But he rejected the counsel of the elders and consulted with the young men who had grown up with him and stood before him.",
      "M": "But he rejected the advice of the elders and consulted instead the young men who had grown up with him and were serving him.",
      "T": "But Rehoboam rejected the counsel of the older men. He turned instead to the young men who had grown up with him and were now his attendants."
    },
    "9": {
      "L": "And he said to them, 'What do you advise that we answer this people who have spoken to me, saying, \"Lighten the yoke that your father put upon us\"?'",
      "M": "'What is your advice?' he said to them. 'How should we answer this people who asked me to lighten the yoke my father put on them?'",
      "T": "'What do you advise?' he asked the young men. 'These people are asking me to reduce the burden my father imposed. What should I tell them?'"
    },
    "10": {
      "L": "And the young men who had grown up with him spoke to him, saying, 'Thus shall you speak to this people who said to you, \"Your father made our yoke heavy, but you lighten it for us\": thus you shall say to them, \"My little finger is thicker than my father's waist.\"'",
      "M": "The young men who had grown up with him replied, 'This is what you should tell the people who said to you, \"Your father made our yoke heavy—you make it lighter.\" Say to them: \"My little finger is thicker than my father's waist.\"'",
      "T": "The young men who had grown up with him told him: 'Tell these people who asked you to lighten their load: \"My little finger is thicker than my father's whole body.\"'"
    },
    "11": {
      "L": "'And now, whereas my father laid on you a heavy yoke, I will add to your yoke. My father chastised you with whips, but I will chastise you with scorpions.'",
      "M": "'My father loaded you with a heavy yoke; I will add to it. My father disciplined you with whips; I will discipline you with scorpions.'",
      "T": "'My father put a heavy yoke on you—I will make it heavier. My father used whips on you—I will use scorpions.'"
    },
    "12": {
      "L": "So Jeroboam and all the people came to Rehoboam on the third day, as the king had directed, saying, 'Come back to me on the third day.'",
      "M": "Jeroboam and all the people came back to Rehoboam on the third day, just as the king had told them: 'Return to me on the third day.'",
      "T": "On the third day, as the king had said, Jeroboam and all the people returned to Rehoboam."
    },
    "13": {
      "L": "And the king answered the people harshly, and he forsook the counsel of the elders whom they had given him.",
      "M": "The king answered the people harshly, rejecting the advice the elders had given him.",
      "T": "The king answered the people harshly—he had thrown out the counsel of the elders."
    },
    "14": {
      "L": "And he spoke to them after the counsel of the young men, saying, 'My father made your yoke heavy, and I will add to your yoke. My father chastised you with whips, but I will chastise you with scorpions.'",
      "M": "He spoke according to the young men's advice: 'My father made your yoke heavy; I will add to it. My father disciplined you with whips; I will discipline you with scorpions.'",
      "T": "He took the young men's counsel and told them: 'My father made your yoke heavy—I will make it heavier. My father used whips on you—I will use scorpions.'"
    },
    "15": {
      "L": "So the king did not listen to the people, for the turn of events was from the LORD, to fulfil his word which the LORD spoke by Ahijah the Shilonite to Jeroboam the son of Nebat.",
      "M": "The king would not listen to the people, for this turn of events was from the LORD—to bring about the word the LORD had spoken through Ahijah the Shilonite to Jeroboam son of Nebat.",
      "T": "The king would not hear the people—for this turn of affairs was from the LORD himself, to fulfil what he had spoken through the prophet Ahijah to Jeroboam son of Nebat. Divine providence was working through human arrogance."
    },
    "16": {
      "L": "And when all Israel saw that the king did not listen to them, the people answered the king, saying, 'What portion do we have in David? We have no inheritance in the son of Jesse. To your tents, O Israel! Now see to your own house, O David!' So Israel departed to their tents.",
      "M": "When all Israel saw that the king would not listen to them, they answered the king: 'What share do we have in David? We have no inheritance in the son of Jesse. Back to your tents, Israel! Look after your own house now, David!' So Israel went home.",
      "T": "When all Israel saw the king would not listen, they shouted back: 'What do we owe David? We have no stake in Jesse's son! To your tents, Israel—look after your own house, David!' And Israel walked out. The cry was the same as Sheba's, from generations before—only now it was final."
    },
    "17": {
      "L": "But Rehoboam reigned over the children of Israel who lived in the cities of Judah.",
      "M": "Rehoboam continued to reign over the Israelites who were settled in the towns of Judah.",
      "T": "Rehoboam still ruled over those Israelites living in the towns of Judah."
    },
    "18": {
      "L": "Then King Rehoboam sent Adoram, who was over the forced labour, and all Israel stoned him to death. And King Rehoboam quickly mounted his chariot to flee to Jerusalem.",
      "M": "King Rehoboam sent out Adoram, who was in charge of the forced labour, but all Israel stoned him to death. King Rehoboam hurriedly climbed into his chariot to escape to Jerusalem.",
      "T": "King Rehoboam made a catastrophic miscalculation—he sent Adoram, the man in charge of forced labour, out to them. All Israel stoned him to death. Rehoboam barely made it into his chariot and fled to Jerusalem."
    },
    "19": {
      "L": "So Israel has been in rebellion against the house of David to this day.",
      "M": "So Israel has been in rebellion against the house of David to this day.",
      "T": "Israel has been in rebellion against the house of David from that day to this."
    },
    "20": {
      "L": "And it came to pass when all Israel heard that Jeroboam had returned, they sent and called him to the assembly and made him king over all Israel. There was none that followed the house of David but the tribe of Judah only.",
      "M": "When all Israel heard that Jeroboam had returned, they summoned him to the assembly and made him king over all Israel. Only the tribe of Judah followed the house of David.",
      "T": "When all Israel heard Jeroboam was back, they summoned him to the assembly and made him king over all Israel. Only the tribe of Judah remained loyal to the house of David."
    },
    "21": {
      "L": "And when Rehoboam came to Jerusalem, he assembled all the house of Judah and the tribe of Benjamin, one hundred and eighty thousand chosen warriors, to fight against the house of Israel, to restore the kingdom to Rehoboam the son of Solomon.",
      "M": "When Rehoboam arrived in Jerusalem, he mustered the whole house of Judah and the tribe of Benjamin—a hundred and eighty thousand chosen warriors—to fight against Israel and recover the kingdom for Rehoboam son of Solomon.",
      "T": "When Rehoboam reached Jerusalem, he mobilised the whole house of Judah and the tribe of Benjamin—a hundred and eighty thousand combat troops—to fight the northern kingdom and take back what he had lost."
    },
    "22": {
      "L": "But the word of God came to Shemaiah the man of God, saying,",
      "M": "But the word of God came to Shemaiah the man of God:",
      "T": "But the word of God came to Shemaiah, the man of God:"
    },
    "23": {
      "L": "'Speak to Rehoboam the son of Solomon, king of Judah, and to all the house of Judah and Benjamin, and to the rest of the people, saying,",
      "M": "'Say to Rehoboam son of Solomon, king of Judah, and to all the house of Judah and Benjamin and the rest of the people:",
      "T": "'Say to Rehoboam son of Solomon, king of Judah, and to all the house of Judah and Benjamin, and to the whole people:"
    },
    "24": {
      "L": "'Thus says the LORD: You shall not go up or fight against your brothers, the children of Israel. Let every man return to his house, for this thing is from me.' So they listened to the word of the LORD and turned back, according to the word of the LORD.",
      "M": "'This is what the LORD says: Do not go up and fight against your Israelite brothers. Let every man return home, for this thing has come from me.' They listened to the LORD's word and turned back, as the LORD had commanded.",
      "T": "'This is what the LORD says: Do not march—do not fight your Israelite brothers. Every man, go home. This is my doing.' They listened to the word of the LORD and went home. What looked like political fracture was, in the LORD's hands, a deliberate act."
    },
    "25": {
      "L": "Then Jeroboam built Shechem in the hill country of Ephraim and lived there. And he went out from there and built Penuel.",
      "M": "Jeroboam rebuilt Shechem in the hill country of Ephraim and lived there. Then he went on to build Penuel.",
      "T": "Jeroboam rebuilt Shechem in the Ephraimite highlands and made it his base. Then he also built Penuel."
    },
    "26": {
      "L": "And Jeroboam said in his heart, 'Now the kingdom may return to the house of David.",
      "M": "Jeroboam thought to himself, 'The kingdom could easily revert to the house of David.",
      "T": "But Jeroboam reasoned to himself: 'If this nation keeps going to Jerusalem, the kingdom will swing back to the house of David."
    },
    "27": {
      "L": "'If this people go up to offer sacrifices in the house of the LORD at Jerusalem, then the heart of this people will turn back to their lord, to Rehoboam king of Judah, and they will kill me and return to Rehoboam king of Judah.'",
      "M": "'If this people go up to offer sacrifices in the LORD's temple at Jerusalem, their hearts will turn back to their master Rehoboam king of Judah—they will kill me and go back to him.'",
      "T": "'If the people keep going up to offer sacrifices in the LORD's house at Jerusalem, their hearts will turn back to Rehoboam—and they'll kill me to do it.'"
    },
    "28": {
      "L": "So the king took counsel and made two calves of gold. And he said to them, 'It is too much for you to go up to Jerusalem. Behold your gods, O Israel, who brought you up out of the land of Egypt.'",
      "M": "After taking counsel, the king made two golden calves. He said to the people, 'You have been going up to Jerusalem long enough. Here are your gods, Israel, who brought you up out of Egypt.'",
      "T": "So Jeroboam took counsel—and made two golden calves. He said to the people: 'Enough of this going up to Jerusalem. Here, Israel, are your gods who brought you up out of Egypt.' He was re-enacting Aaron's sin at the foot of Sinai, deliberately or not."
    },
    "29": {
      "L": "And he set one in Bethel and he put the other in Dan.",
      "M": "He set up one in Bethel and placed the other in Dan.",
      "T": "One he set up in Bethel, the other in Dan—the northern and southern boundaries of his kingdom."
    },
    "30": {
      "L": "And this thing became a sin. The people went even to Dan to worship before the one there.",
      "M": "This became a sinful thing. The people went as far as Dan to worship the one there.",
      "T": "This became sin. The people were travelling all the way to Dan to bow before the calf there."
    },
    "31": {
      "L": "And he made houses of high places and made priests from among all the people, who were not of the sons of Levi.",
      "M": "Jeroboam built shrines on the high places and appointed priests from all sorts of people—people who were not Levites.",
      "T": "Jeroboam built shrines on the high places and appointed non-Levite priests—men from the general population. He was rebuilding Israel's religion from the ground up, in defiance of the covenant order."
    },
    "32": {
      "L": "And Jeroboam appointed a feast in the eighth month, on the fifteenth day of the month, like the feast that was in Judah, and he offered sacrifices on the altar. So he did in Bethel, sacrificing to the calves he had made. And he placed in Bethel the priests of the high places he had made.",
      "M": "Jeroboam instituted a festival on the fifteenth day of the eighth month, similar to the festival in Judah. He offered sacrifices on the altar in Bethel—sacrificing to the calves he had made—and he installed in Bethel the priests of the high places he had set up.",
      "T": "Jeroboam instituted a rival festival—the fifteenth day of the eighth month, a deliberate imitation of the feast in Judah but shifted by a month. He offered sacrifices on the altar at Bethel, sacrificing before the calves he had made, and installed his own priests at the high places there."
    },
    "33": {
      "L": "He went up to the altar that he had made in Bethel on the fifteenth day in the eighth month, in the month that he had devised from his own heart. And he instituted a feast for the children of Israel and went up to the altar to burn incense.",
      "M": "On the fifteenth day of the eighth month—the month he had devised on his own—he went up to the altar he had made in Bethel and instituted a festival for the Israelites. He went up to the altar and burned incense.",
      "T": "And on the fifteenth day of the eighth month—a date he had invented from his own imagination—he went up to the altar at Bethel, convened a festival for Israel, and burned incense. It was religion by royal decree, devised in a human heart, with no word from God."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1kings')
        merge_tier(existing, KINGS, tier_key)
        save(tier_dir, '1kings', existing)
    print('1 Kings 10–12 written.')

if __name__ == '__main__':
    main()
