"""
MKT 1 Kings chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1kings-7-9.py

Translation decisions:
- H3068 (יהוה): "LORD" in L/M throughout; "the LORD" in T — consistent with mkt-1kings-1-6.py.
- H430 (אֱלֹהִים): "God" in all tiers.
- H8034 (shem / name): The Deuteronomistic "name theology" is central to ch 8.
  The LORD causes his name to dwell in the temple (8:16, 17, 19, 20, 29, etc.).
  L/M: "name"; T: rendered naturally but the theological weight is noted in key verses.
- H2617 (חֶסֶד): 8:23 — L "mercy/covenant," M "steadfast love," T "faithful love."
  Consistent with 1-6 script: covenantal, active kindness.
- H7725 (shub / turn): In ch 8 prayer, context-specific:
  8:33,35,47,48 = Israel turning back in repentance: L "turn again," M "return/repent,"
  T "turn back / come to their senses."
- H5545 (salach / forgive): "forgive" all tiers throughout ch 8 prayer.
- H1285 (berit / covenant): "covenant" all tiers (ark of the covenant in 8:1,6,21).
- H1004 (bayit / house): "house" or "palace" rendered by context.
  For temple: "house of the LORD" or "the house"; for palace: "palace" or "house."
  The wordplay (bayit = temple + dynasty) is surfaced in T at 8:16 and 9:5.
- H3678 (kisse / throne): "throne" all tiers.
- H2181 (Hiram the craftsman, ch 7): distinct from Hiram king of Tyre (ch 9).
  In ch 7 he is Solomon's hired craftsman; in ch 9 he is the Tyrian king.
- H3220 (yam / sea): The "molten sea" in 7:23-26 is a great bronze basin, not an ocean.
  L: "molten sea," M: "molten sea," T: "the great Sea."
- Architectural terms (ch 7): "chapiter" → "capital"; "base/stand" for the bronze laver-stands;
  "laver" retained in L, rendered "basin" in M/T.
- H3548 (kohen / priest): "priest" all tiers.
- Aspect: waw-consecutive imperfects throughout = narrative past (simple past in English).
  Solomon's prayer in ch 8 uses conditional sentences (if...then); subjunctive moods preserved.
- OT echoes:
  - 8:10-11: Cloud filling the temple echoes Exod 40:34-35 (the tabernacle cloud). T notes this
    explicitly — the temple is the heir of the tabernacle's glory.
  - 8:27: "Heaven and the heaven of heavens cannot contain you" — a key anti-idolatry statement;
    the temple is not a container for God but a focus for prayer. T draws this out.
  - 8:51: "iron furnace" for Egypt echoes Deut 4:20. T notes it.
  - 8:56: "not one word has failed" echoes Josh 21:45; 23:14. T notes the fulfillment theme.
  - 9:4-5: The conditional covenant echoes the Sinai covenant structure (Lev 26, Deut 28-30).
    T surfaces the Deuteronomistic framework: obedience → blessing; disobedience → exile.
  - 9:7: "proverb and byword" echoes Deut 28:37. T notes this is the exile warning made explicit.
- Chapter 7 note: The architectural description of Hiram's bronze work (7:13-51) is among the
  most technically dense passages in Kings. L preserves archaic terms (chapiter, undersetters,
  knops) without explanation; M modernizes them; T focuses on the overall theological significance
  of the furnishings — the Sea, the lavers, the pillars — as symbols of creation and order.
- Jachin/Boaz (7:21): The pillar names are preserved without translation in all tiers.
  A gloss is provided in T: Jachin ("He establishes") and Boaz ("In him is strength").
- Chapter 8 note: Solomon's prayer (vv. 22-53) is the Deuteronomistic theological heart of Kings.
  Seven petitions structure it (vv. 31-51). T draws out the cumulative logic: wherever Israel
  is — in the land, in drought, in war, in exile — prayer toward this house reaches heaven.
- 8:65 textual note: MT reads "seven days and seven days, even fourteen days" —
  the feast of dedication plus the Feast of Tabernacles. V66's "eighth day" refers to
  the solemn assembly following the seven-day Feast of Tabernacles. All tiers translate MT.
- Chapter 9 note: The second divine appearance to Solomon (9:1-9) directly mirrors ch 3.
  But the tone shifts: where ch 3 was promise, ch 9 is conditional warning.
  T surfaces this tension — the same God who gave Solomon wealth now announces the terms
  under which the temple itself could be destroyed. This is the literary pivot of 1 Kings.
- Cabul (9:13): The name may be a pun on Heb. "as nothing" (ke-bal) or an Aramaic word
  meaning "bond/obligation." The name is preserved in all tiers; T notes the irony of
  Israel's finest king paying twenty cities for timber and gold.
- Forced labor (9:20-22): The text carefully distinguishes Israelite military service from
  Canaanite forced labor. T notes the uncomfortable parallel to Deut 17:16 (no multiplication
  of chariots) and the social fault lines this creates — seeds of the later division.
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
  "7": {
    "1": {
      "L": "And Solomon was building his own house thirteen years, and he finished all his house.",
      "M": "Solomon spent thirteen years building his own palace, and he completed it.",
      "T": "Solomon took thirteen years to build his own palace—and finished every part of it."
    },
    "2": {
      "L": "He built the House of the Forest of Lebanon; its length a hundred cubits, and its breadth fifty cubits, and its height thirty cubits, upon four rows of cedar pillars, with cedar beams upon the pillars.",
      "M": "He built the House of the Forest of Lebanon: a hundred cubits long, fifty wide, and thirty high, resting on four rows of cedar pillars with cedar beams above them.",
      "T": "He built the House of the Forest of Lebanon—a hundred cubits long, fifty wide, thirty high—supported by four rows of cedar pillars with cedar beams above."
    },
    "3": {
      "L": "And it was covered with cedar above the beams that were upon five-and-forty pillars, fifteen in a row.",
      "M": "The ceiling was of cedar above the beams, which rested on forty-five pillars—fifteen to each row.",
      "T": "A cedar ceiling covered the beams above forty-five pillars arranged fifteen per row."
    },
    "4": {
      "L": "And there were windows in three rows, and light over against light in three tiers.",
      "M": "There were windows set in three rows, with each window facing its opposite across three levels.",
      "T": "Three rows of windows faced each other on three tiers, letting light fall symmetrically."
    },
    "5": {
      "L": "And all the doors and doorposts had square frames, and window was over against window in three tiers.",
      "M": "All the doorways and doorframes were rectangular, and the windows faced each other in three tiers.",
      "T": "Every door and doorframe was square; the windows faced each other across three levels."
    },
    "6": {
      "L": "And he made the Hall of Pillars; its length fifty cubits, and its breadth thirty cubits, and a porch before them, with pillars and a threshold before them.",
      "M": "He also built the Hall of Pillars: fifty cubits long and thirty cubits wide, with a colonnaded porch across the front.",
      "T": "He also built the Hall of Pillars—fifty cubits long, thirty wide—with a columned porch across the front."
    },
    "7": {
      "L": "And he made the Hall of the Throne where he was to judge, even the Hall of Judgment, and it was covered with cedar from floor to floor.",
      "M": "He made the Hall of the Throne—the Hall of Judgment—where he would pronounce verdicts. It was paneled with cedar from floor to ceiling.",
      "T": "He built the Hall of the Throne—the Hall of Justice—where Solomon would pronounce judgment. Cedar covered it from floor to ceiling."
    },
    "8": {
      "L": "His own house where he was to live, in the other court inside the porch, was like this work. He also made a house for Pharaoh's daughter whom he had taken, like this porch.",
      "M": "His own residence, set in a second courtyard behind the porch, was built to the same design. He also built a palace for Pharaoh's daughter, whom he had married, to the same design.",
      "T": "His personal residence—set in a second courtyard behind the Hall of Pillars—was built to the same design. He also built a matching palace for Pharaoh's daughter, whom he had taken in marriage."
    },
    "9": {
      "L": "All these were of costly stones, cut to measure, sawed with saws on the inside and on the outside, even from the foundation to the coping, and so on the outside to the great court.",
      "M": "All these structures were built of costly hewn stones trimmed to exact measurements, sawed smooth on every face, from foundation to roofline, and on to the great outer court.",
      "T": "All these buildings were of costly hewn stone—precisely measured, sawn smooth on every face—from foundation to roofline, extending outward to the great outer court."
    },
    "10": {
      "L": "The foundation was of costly stones, even great stones, stones of ten cubits and stones of eight cubits.",
      "M": "The foundation stones were massive—costly cut stones, some measuring ten cubits and others eight cubits.",
      "T": "The foundation blocks were enormous—costly hewn stones, some ten cubits long, some eight."
    },
    "11": {
      "L": "And above were costly stones, cut to measure, and cedar.",
      "M": "Above the foundation were more costly stones cut to measure, and cedar timber.",
      "T": "Above them came more precisely hewn stones of equal quality, and cedar."
    },
    "12": {
      "L": "And the great court round about had three rows of hewed stones and a row of cedar beams, both for the inner court of the house of the LORD and for the porch of the house.",
      "M": "The great outer court was enclosed by three courses of dressed stone and one course of cedar beams—the same construction used for the inner court of the LORD's house and for the temple entrance hall.",
      "T": "The great outer court was bordered by three rows of hewn stone and one of cedar beams—the same as the inner court of the LORD's house and the temple porch."
    },
    "13": {
      "L": "And King Solomon sent and fetched Hiram out of Tyre.",
      "M": "King Solomon sent to Tyre and brought Hiram.",
      "T": "King Solomon sent to Tyre and summoned Hiram."
    },
    "14": {
      "L": "He was the son of a widow of the tribe of Naphtali, and his father was a man of Tyre, a worker in brass. He was filled with wisdom and understanding and skill to work all works in brass. He came to King Solomon and did all his work.",
      "M": "He was the son of a widow from the tribe of Naphtali, and his father was a Tyrian bronze craftsman. He was filled with wisdom, understanding, and skill for working every kind of bronze. He came to King Solomon and carried out all his bronze work.",
      "T": "He was the son of a Naphtalite widow; his father was a Tyrian bronze craftsman. Hiram himself was filled with wisdom, understanding, and skill in all bronze work. He came to King Solomon and executed everything Solomon required."
    },
    "15": {
      "L": "For he cast two pillars of brass, of eighteen cubits high apiece; and a line of twelve cubits did compass either of them about.",
      "M": "He cast two bronze pillars, each eighteen cubits tall, with a circumference of twelve cubits.",
      "T": "He cast two bronze pillars, each eighteen cubits high, with a circumference of twelve cubits."
    },
    "16": {
      "L": "And he made two chapiters of molten brass, to set upon the tops of the pillars; the height of the one chapiter was five cubits, and the height of the other chapiter was five cubits.",
      "M": "He cast two capitals of bronze to set on the tops of the pillars, each five cubits high.",
      "T": "He cast two bronze capitals to crown the tops of the pillars, each five cubits high."
    },
    "17": {
      "L": "And nets of checker work and wreaths of chain work for the chapiters which were upon the top of the pillars; seven for the one chapiter and seven for the other chapiter.",
      "M": "He made latticework of checkerwork design and twisted chain garlands for the capitals—seven rows for each capital.",
      "T": "He fashioned latticed checkerwork and chains of twisted cord for the capitals—seven rows per capital."
    },
    "18": {
      "L": "And he made the pillars, and two rows round about upon the one network, to cover the chapiters that were upon the top, with pomegranates; and so did he for the other chapiter.",
      "M": "He made two rows of pomegranates around each piece of latticework to cover the capital on top—the same for both pillars.",
      "T": "Two rows of pomegranates encircled the latticework covering each capital—the same arrangement for both pillars."
    },
    "19": {
      "L": "And the chapiters that were upon the top of the pillars in the porch were of lily work, four cubits.",
      "M": "The capitals on top of the porch pillars were designed as lily flowers, four cubits high.",
      "T": "The capitals topping the porch pillars were shaped like lilies, four cubits high."
    },
    "20": {
      "L": "And the chapiters upon the two pillars had pomegranates also above, over against the belly which was by the network; and the pomegranates were two hundred in rows round about upon the other chapiter.",
      "M": "The capitals on both pillars also had pomegranates above, beside the rounded section adjacent to the latticework—two hundred pomegranates in rows encircling each capital.",
      "T": "Above the rounded bulge beside each lattice, two hundred pomegranates encircled each capital in rows—on both pillars."
    },
    "21": {
      "L": "And he set up the pillars in the porch of the temple; and he set up the right pillar, and called the name thereof Jachin; and he set up the left pillar, and called the name thereof Boaz.",
      "M": "He erected the pillars at the entrance of the temple. He set up the right pillar and named it Jachin, and he erected the left pillar and named it Boaz.",
      "T": "He erected the pillars at the temple entrance. The right pillar he named Jachin ('He establishes'); the left pillar he named Boaz ('In him is strength')."
    },
    "22": {
      "L": "And upon the top of the pillars was lily work; so was the work of the pillars finished.",
      "M": "The tops of the pillars were crowned with lily-work. So the work of the pillars was complete.",
      "T": "The tops were finished with lily-work. The pillars were done."
    },
    "23": {
      "L": "And he made a molten sea, ten cubits from the one brim to the other; it was round all about, and its height was five cubits; and a line of thirty cubits did compass it round about.",
      "M": "He made the molten sea: a circular cast-metal basin ten cubits from rim to rim, five cubits high, with a circumference of thirty cubits.",
      "T": "He cast the great Sea: a circular bronze basin ten cubits across, five cubits deep, thirty cubits around."
    },
    "24": {
      "L": "And under the brim of it round about there were knops compassing it, ten in a cubit, compassing the sea round about; the knops were cast in two rows, when it was cast.",
      "M": "Under the rim gourd-shaped ornaments encircled the sea—ten per cubit—cast in two rows as part of the original casting.",
      "T": "Below the rim, two rows of gourd-shaped knobs encircled the entire Sea—ten per cubit—cast as one piece with the basin."
    },
    "25": {
      "L": "It stood upon twelve oxen, three looking toward the north, and three looking toward the west, and three looking toward the south, and three looking toward the east; and the sea was set above upon them, and all their hinder parts were inward.",
      "M": "It rested on twelve bronze oxen: three facing north, three facing west, three facing south, three facing east—with all their hindquarters pointing inward and the sea set on top of them.",
      "T": "The Sea rested on twelve bronze oxen—three facing north, three west, three south, three east—all with their hindquarters turned inward."
    },
    "26": {
      "L": "And it was an hand breadth thick, and the brim thereof was wrought like the brim of a cup, with flowers of lilies; it contained two thousand baths.",
      "M": "The metal was a handbreadth thick. The rim was shaped like a cup's brim, like lily petals. It held two thousand baths.",
      "T": "A handbreadth thick, its rim shaped like a lily-flower cup. It held two thousand baths."
    },
    "27": {
      "L": "And he made ten bases of brass; four cubits was the length of one base, and four cubits the breadth thereof, and three cubits the height of it.",
      "M": "He made ten bronze stands, each four cubits long, four cubits wide, and three cubits high.",
      "T": "He made ten bronze stands—each four cubits long, four wide, three high."
    },
    "28": {
      "L": "And the work of the bases was on this manner: they had borders, and the borders were between the ledges.",
      "M": "The stands were constructed with panels set within frames.",
      "T": "Each stand was built with panels fitted within frames."
    },
    "29": {
      "L": "And on the borders that were between the ledges were lions, oxen, and cherubims; and upon the ledges there was a base above; and beneath the lions and oxen were certain additions made of thin work.",
      "M": "On the panels between the frames were carved lions, oxen, and cherubim. Above and below the figures were garlands of hammered metalwork.",
      "T": "On the panels were lions, oxen, and cherubim. Garlands of hammered metal ran above and below the figures."
    },
    "30": {
      "L": "And every base had four brasen wheels, and plates of brass; and the four corners thereof had undersetters; under the laver were undersetters molten, at the side of every addition.",
      "M": "Each stand had four bronze wheels with bronze axles, and four corner supports. The supports were cast with garlands on either side.",
      "T": "Each stand rolled on four bronze wheels with bronze axles. Four corner supports held the basin, with garlands flanking every mounting."
    },
    "31": {
      "L": "And the mouth of it within the chapiter and above was a cubit; but the mouth thereof was round after the work of the base, a cubit and a half; and also upon the mouth of it were gravings with their borders, foursquare, not round.",
      "M": "The stand's collar projected one cubit above the top; the circular opening was set on a base a cubit and a half deep, and around the opening were carvings and square panels.",
      "T": "A collar one cubit high rose above the top of each stand. The circular opening rested on a base a cubit and a half deep, surrounded by square carved panels."
    },
    "32": {
      "L": "And under the borders were four wheels; and the axletrees of the wheels were joined to the base; and the height of a wheel was a cubit and half a cubit.",
      "M": "Four wheels were set under the panels, with axles fixed into the stand. Each wheel measured a cubit and a half in diameter.",
      "T": "Four wheels beneath the panels were joined by axles fixed into the stand. Each wheel was a cubit and a half in diameter."
    },
    "33": {
      "L": "And the fashion of the wheels was like the fashion of a chariot wheel; their axletrees, and their naves, and their felloes, and their spokes, were all molten.",
      "M": "The wheels were made like chariot wheels—their axles, hubs, spokes, and rims all of cast bronze.",
      "T": "The wheels were chariot-style: axles, hubs, spokes, and rims all cast in bronze."
    },
    "34": {
      "L": "And there were four undersetters to the four corners of one base; and the undersetters were of the very base itself.",
      "M": "There were four corner supports at the four corners of each stand, cast as one piece with the stand itself.",
      "T": "Four corner supports—cast as one with the stand—stood at each corner."
    },
    "35": {
      "L": "And in the top of the base was there a round compass of half a cubit high; and on the top of the base the ledges thereof and the borders thereof were of the same.",
      "M": "At the top of each stand was a round band half a cubit high, and its projections and panels were all cast as one piece with it.",
      "T": "A circular band half a cubit high crowned each stand, its projections and panels all one piece with it."
    },
    "36": {
      "L": "For on the plates of the ledges thereof, and on the borders thereof, he graved cherubims, lions, and palm trees, according to the proportion of every one, and additions round about.",
      "M": "On the panels and borders he engraved cherubim, lions, and palm trees proportioned to each surface, with garlands all around.",
      "T": "On every panel and border he engraved cherubim, lions, and palm trees—each proportioned to its space—with garlands encircling everything."
    },
    "37": {
      "L": "After this manner he made the ten bases; all of them had one casting, one measure, and one size.",
      "M": "He made all ten stands by this same design—identical cast, identical measurements, identical form.",
      "T": "He made all ten stands the same way: one mold, one size, one form."
    },
    "38": {
      "L": "Then made he ten lavers of brass; one laver contained forty baths, and every laver was four cubits; and upon every one of the ten bases one laver.",
      "M": "He also made ten bronze basins, each holding forty baths and measuring four cubits across—one basin for each of the ten stands.",
      "T": "He made ten bronze basins, one per stand—each holding forty baths, four cubits across."
    },
    "39": {
      "L": "And he put five bases on the right side of the house, and five on the left side of the house; and he set the sea on the right side of the house eastward over against the south.",
      "M": "He placed five stands on the south side of the house and five on the north side. He set the sea on the south side at the southeast corner.",
      "T": "Five stands he positioned on the south side of the temple, five on the north. The Sea he placed at the southeast corner."
    },
    "40": {
      "L": "And Hiram made the lavers, and the shovels, and the basons. So Hiram made an end of doing all the work that he made for King Solomon for the house of the LORD:",
      "M": "Hiram also made the basins, shovels, and bowls. So Hiram completed all the work he had done for King Solomon on the house of the LORD:",
      "T": "Hiram made the basins, shovels, and bowls as well. And with that, Hiram completed all the work he had done for King Solomon on the LORD's house:"
    },
    "41": {
      "L": "The two pillars, and the two bowls of the chapiters that were on the top of the two pillars; and the two networks, to cover the two bowls of the chapiters which were upon the top of the pillars;",
      "M": "the two pillars; the two bowl-shaped capitals on top of the pillars; the two pieces of latticework covering those bowls;",
      "T": "the two pillars; the two bowl-shaped capitals crowning them; the two latticed coverings for the bowls;"
    },
    "42": {
      "L": "And four hundred pomegranates for the two networks, even two rows of pomegranates for one network, to cover the two bowls of the chapiters that were upon the pillars;",
      "M": "the four hundred pomegranates for the two pieces of latticework—two rows of pomegranates per piece—covering the two bowl-shaped capitals on the pillars;",
      "T": "four hundred pomegranates for the two lattices—two rows per lattice—covering the bowl-shaped capitals;"
    },
    "43": {
      "L": "And the ten bases, and ten lavers on the bases;",
      "M": "the ten stands and the ten basins on them;",
      "T": "the ten stands and their ten basins;"
    },
    "44": {
      "L": "And one sea, and twelve oxen under the sea;",
      "M": "the one sea and the twelve oxen beneath it;",
      "T": "the one Sea and the twelve oxen beneath it;"
    },
    "45": {
      "L": "And the pots, and the shovels, and the basons; and all these vessels, which Hiram made to King Solomon for the house of the LORD, were of bright brass.",
      "M": "and the pots, shovels, and basins. All these vessels that Hiram made for King Solomon for the house of the LORD were of burnished bronze.",
      "T": "and the pots, shovels, and basins. Every vessel Hiram made for the LORD's house was of polished bronze."
    },
    "46": {
      "L": "In the plain of Jordan did the king cast them, in the clay ground between Succoth and Zarthan.",
      "M": "The king had them cast in the clay soil of the Jordan plain between Succoth and Zarethan.",
      "T": "The king had them all cast in the clay soil of the Jordan Valley between Succoth and Zarethan."
    },
    "47": {
      "L": "And Solomon left all the vessels unweighed, because they were exceeding many; neither was the weight of the brass found out.",
      "M": "Solomon left all the vessels unweighed because there were so many; the total weight of the bronze was never determined.",
      "T": "Solomon never weighed the bronze—there was so much of it that the total was never tallied."
    },
    "48": {
      "L": "And Solomon made all the vessels that pertained unto the house of the LORD: the altar of gold, and the table of gold whereupon the shewbread was,",
      "M": "Solomon also made all the furnishings for the LORD's house: the gold altar and the gold table on which the bread of the Presence stood,",
      "T": "Solomon also furnished the LORD's house: the gold altar, the gold table for the bread of the Presence,"
    },
    "49": {
      "L": "And the candlesticks of pure gold, five on the right side, and five on the left, before the oracle, with the flowers, and the lamps, and the tongs of gold,",
      "M": "ten lampstands of pure gold—five on the right and five on the left before the inner sanctuary—with their flowers, lamps, and tongs of gold;",
      "T": "ten lampstands of pure gold—five right, five left before the inner sanctuary—with flowers, lamps, and tongs, all gold;"
    },
    "50": {
      "L": "And the bowls, and the snuffers, and the basons, and the spoons, and the censers of pure gold; and the hinges of gold, both for the doors of the inner house, the most holy place, and for the doors of the house, to wit, of the temple.",
      "M": "the cups, snuffers, basins, dishes, and fire pans of pure gold; and the gold hinges for the doors of the Most Holy Place and for the doors of the main hall.",
      "T": "cups, snuffers, basins, spoons, and fire pans of pure gold; and gold hinges for the doors of the Most Holy Place and for the doors of the main hall."
    },
    "51": {
      "L": "So was ended all the work that King Solomon made for the house of the LORD. And Solomon brought in the things which David his father had dedicated; even the silver, and the gold, and the vessels, did he put among the treasures of the house of the LORD.",
      "M": "All the work King Solomon did on the house of the LORD was now complete. He brought in the things his father David had dedicated—the silver, the gold, and the vessels—and placed them in the treasuries of the LORD's house.",
      "T": "All the work King Solomon had done on the LORD's house was finished. He brought in the silver, gold, and vessels that his father David had dedicated, and stored them in the treasuries of the LORD's house."
    }
  },
  "8": {
    "1": {
      "L": "Then Solomon assembled the elders of Israel, and all the heads of the tribes, the chief of the fathers of the children of Israel, unto King Solomon in Jerusalem, that they might bring up the ark of the covenant of the LORD out of the city of David, which is Zion.",
      "M": "Solomon summoned to Jerusalem all the elders of Israel, all the heads of the tribes, and the leaders of the family clans of Israel, to bring up the ark of the covenant of the LORD from the city of David—that is, Zion.",
      "T": "Solomon assembled all the elders of Israel—the heads of the tribes and the leaders of every family—summoned to Jerusalem to bring up the ark of the covenant of the LORD from the city of David, which is Zion."
    },
    "2": {
      "L": "And all the men of Israel assembled themselves unto King Solomon at the feast in the month Ethanim, which is the seventh month.",
      "M": "All the men of Israel gathered to King Solomon at the festival in the month of Ethanim—the seventh month.",
      "T": "All Israel assembled to King Solomon at the great feast in the month of Ethanim—the seventh month."
    },
    "3": {
      "L": "And all the elders of Israel came, and the priests took up the ark.",
      "M": "When all the elders of Israel arrived, the priests took up the ark.",
      "T": "When all the elders of Israel had gathered, the priests lifted the ark."
    },
    "4": {
      "L": "And they brought up the ark of the LORD, and the tabernacle of the congregation, and all the holy vessels that were in the tabernacle, even those did the priests and the Levites bring up.",
      "M": "They brought up the ark of the LORD along with the tent of meeting and all the sacred vessels that were in it. The priests and Levites carried them.",
      "T": "They brought up the ark of the LORD, the tent of meeting, and all the sacred vessels that had been kept there. The priests and Levites carried everything."
    },
    "5": {
      "L": "And King Solomon, and all the congregation of Israel, that were assembled unto him, were with him before the ark, sacrificing sheep and oxen, that could not be told nor numbered for multitude.",
      "M": "King Solomon and the whole assembly of Israel gathered before the ark, sacrificing sheep and oxen too numerous to count.",
      "T": "King Solomon and the entire assembly of Israel stood before the ark, offering sheep and oxen in numbers too great to count."
    },
    "6": {
      "L": "And the priests brought in the ark of the covenant of the LORD unto his place, into the oracle of the house, to the most holy place, even under the wings of the cherubims.",
      "M": "The priests brought the ark of the covenant of the LORD to its place in the inner sanctuary—the Most Holy Place—under the wings of the cherubim.",
      "T": "The priests carried the ark of the covenant of the LORD to its resting place: the Most Holy Place—beneath the spread wings of the cherubim."
    },
    "7": {
      "L": "For the cherubims spread forth their two wings over the place of the ark, and the cherubims covered the ark and the staves thereof above.",
      "M": "The cherubim spread their wings over the place of the ark, sheltering the ark and its carrying poles above.",
      "T": "The cherubim spread their wings over the ark's place, overshadowing both the ark and its poles."
    },
    "8": {
      "L": "And they drew out the staves, that the ends of the staves were seen out in the holy place before the oracle, and they were not seen without; and there they are unto this day.",
      "M": "The poles were extended so that their tips were visible from the Holy Place at the front of the inner sanctuary, though not from outside. And they remain there to this day.",
      "T": "The poles were long enough that their tips showed from the Holy Place just outside the inner sanctuary—but not from outside the building. They are still there to this day."
    },
    "9": {
      "L": "There was nothing in the ark save the two tables of stone, which Moses put there at Horeb, when the LORD made a covenant with the children of Israel, when they came out of the land of Egypt.",
      "M": "The ark contained nothing except the two stone tablets that Moses had placed there at Horeb, where the LORD made a covenant with Israel when they came out of Egypt.",
      "T": "The ark contained only the two stone tablets Moses had placed there at Horeb—the covenant the LORD made with Israel when he brought them out of Egypt."
    },
    "10": {
      "L": "And it came to pass, when the priests were come out of the holy place, that the cloud filled the house of the LORD,",
      "M": "When the priests came out of the Holy Place, a cloud filled the house of the LORD,",
      "T": "When the priests came out of the Holy Place, a cloud filled the house of the LORD—"
    },
    "11": {
      "L": "So that the priests could not stand to minister because of the cloud; for the glory of the LORD had filled the house of the LORD.",
      "M": "so thick that the priests could not stand to minister, for the glory of the LORD had filled the house of the LORD.",
      "T": "so thick that the priests could not remain to serve. The glory of the LORD had filled his house—as it had once filled the tabernacle."
    },
    "12": {
      "L": "Then spake Solomon, The LORD said that he would dwell in the thick darkness.",
      "M": "Then Solomon said, 'The LORD has declared that he would dwell in thick darkness.'",
      "T": "Then Solomon said: 'The LORD has declared that he would dwell in thick darkness.'"
    },
    "13": {
      "L": "I have surely built thee a house to dwell in, a settled place for thee to abide in forever.",
      "M": "I have truly built you an exalted house—a permanent dwelling place for you to inhabit forever.",
      "T": "I have truly built you a magnificent house—a settled place for you to dwell in forever."
    },
    "14": {
      "L": "And the king turned his face about, and blessed all the congregation of Israel; and all the congregation of Israel stood.",
      "M": "Then the king turned and blessed the whole assembly of Israel while they were all standing.",
      "T": "Then the king turned to face the whole assembly of Israel—all standing—and blessed them."
    },
    "15": {
      "L": "And he said, Blessed be the LORD God of Israel, which spake with his mouth unto David my father, and hath with his hand fulfilled it, saying,",
      "M": "He said, 'Blessed be the LORD, the God of Israel, who spoke with his own mouth to my father David and has fulfilled it with his own hand, saying:'",
      "T": "He said: 'Blessed be the LORD, the God of Israel! He spoke it to my father David with his own mouth—and has fulfilled it with his own hand:'"
    },
    "16": {
      "L": "Since the day that I brought forth my people Israel out of Egypt, I chose no city out of all the tribes of Israel to build an house, that my name might be therein; but I chose David to be over my people Israel.",
      "M": "From the day I brought my people Israel out of Egypt, I chose no city from any tribe of Israel in which to build a house where my name would dwell. But I chose David to rule my people Israel.",
      "T": "From the day I brought my people Israel out of Egypt, I chose no city among all Israel's tribes for a house where my name would dwell. But I chose David to lead my people Israel."
    },
    "17": {
      "L": "And it was in the heart of David my father to build an house for the name of the LORD God of Israel.",
      "M": "It was the desire of my father David to build a house for the name of the LORD, the God of Israel.",
      "T": "My father David set his heart on building a house for the name of the LORD, the God of Israel."
    },
    "18": {
      "L": "And the LORD said unto David my father, Whereas it was in thine heart to build an house unto my name, thou didst well that it was in thine heart.",
      "M": "But the LORD said to my father David: You did well to have it in your heart to build a house for my name.",
      "T": "But the LORD said to my father: You did well to set your heart on building a house for my name."
    },
    "19": {
      "L": "Nevertheless thou shalt not build the house; but thy son that shall come forth out of thy loins, he shall build the house unto my name.",
      "M": "Nevertheless, you yourself shall not build the house; your own son shall build the house for my name.",
      "T": "Nevertheless, the building is not yours to do. Your son—your own flesh—he will build the house for my name."
    },
    "20": {
      "L": "And the LORD hath performed his word that he spake, and I am risen up in the room of David my father, and sit on the throne of Israel, as the LORD promised, and have built an house for the name of the LORD God of Israel.",
      "M": "The LORD has kept the promise he made. I have succeeded my father David and sit on the throne of Israel, just as the LORD promised, and I have built the house for the name of the LORD, the God of Israel.",
      "T": "The LORD has kept his word. I have succeeded my father David, I sit on Israel's throne as the LORD promised—and I have built the house for the name of the LORD, the God of Israel."
    },
    "21": {
      "L": "And I have set there a place for the ark, wherein is the covenant of the LORD, which he made with our fathers, when he brought them out of the land of Egypt.",
      "M": "And I have provided a place for the ark—the ark that holds the covenant of the LORD which he made with our fathers when he brought them out of Egypt.",
      "T": "And I have prepared a place for the ark—the ark that holds the covenant the LORD made with our fathers when he brought them out of Egypt."
    },
    "22": {
      "L": "And Solomon stood before the altar of the LORD in the presence of all the congregation of Israel, and spread forth his hands toward heaven:",
      "M": "Solomon stood before the altar of the LORD before the whole assembly of Israel and spread out his hands toward heaven.",
      "T": "Solomon stood before the altar of the LORD, facing the whole assembly of Israel, and spread his hands toward heaven."
    },
    "23": {
      "L": "And he said, LORD God of Israel, there is no God like thee, in heaven above, or on earth beneath, who keepest covenant and mercy with thy servants that walk before thee with all their heart:",
      "M": "He said, 'LORD, God of Israel, there is no God like you in heaven above or on earth below—you who keep covenant and steadfast love for your servants who walk before you with all their heart.'",
      "T": "He said: 'LORD, God of Israel, there is no God like you—in heaven above or on earth beneath. You keep covenant and faithful love for your servants who walk before you with their whole heart.'"
    },
    "24": {
      "L": "Who hast kept with thy servant David my father that thou promisedst him; thou spakest also with thy mouth, and hast fulfilled it with thine hand, as it is this day.",
      "M": "You kept the promise you made to your servant David my father—what you spoke with your mouth you have fulfilled with your hand, as this day shows.",
      "T": "You kept the promise you made to your servant, my father David. You spoke it with your mouth, and today you have fulfilled it with your hand."
    },
    "25": {
      "L": "Therefore now, LORD God of Israel, keep with thy servant David my father that thou promisedst him, saying, There shall not fail thee a man in my sight to sit on the throne of Israel; so that thy children take heed to their way, that they walk before me as thou hast walked before me.",
      "M": "Now therefore, LORD God of Israel, keep for your servant David my father what you promised him: You shall never lack a man to sit before me on the throne of Israel—provided your sons are careful in their walk before me as you walked before me.",
      "T": "Now therefore, LORD God of Israel, keep the promise you made to your servant, my father David: you will never lack a man to sit before you on Israel's throne—so long as his sons walk before you as David walked before you."
    },
    "26": {
      "L": "And now, O God of Israel, let thy word, I pray thee, be verified, which thou spakest unto thy servant David my father.",
      "M": "And now, O God of Israel, let the word you spoke to your servant David my father be fulfilled.",
      "T": "Now, O God of Israel, let the word you spoke to your servant David be confirmed."
    },
    "27": {
      "L": "But will God indeed dwell on the earth? behold, the heaven and heaven of heavens cannot contain thee; how much less this house that I have builded?",
      "M": "But will God truly dwell on the earth? Even the highest heavens cannot contain you—how much less this house I have built!",
      "T": "But can God truly dwell on the earth? The highest heavens cannot contain you—how much less this house I have built! The temple is not a container for God but a place where God hears prayer."
    },
    "28": {
      "L": "Yet have thou respect unto the prayer of thy servant, and to his supplication, O LORD my God, to hearken unto the cry and to the prayer, which thy servant prayeth before thee to day:",
      "M": "Yet give attention to your servant's prayer and plea, O LORD my God, and listen to the cry and the prayer your servant brings before you today—",
      "T": "Yet hear your servant's prayer and supplication, O LORD my God. Listen to the cry and the prayer your servant offers before you today—"
    },
    "29": {
      "L": "That thine eyes may be open toward this house night and day, even toward the place of which thou hast said, My name shall be there; that thou mayest hearken unto the prayer which thy servant shall make toward this place.",
      "M": "that your eyes may be open toward this house night and day—the place where you have said your name will dwell—so that you may hear the prayer your servant makes toward this place.",
      "T": "may your eyes be open toward this house night and day—the place where you have said your name will dwell—that you may hear every prayer directed toward this place."
    },
    "30": {
      "L": "And hearken thou to the supplication of thy servant, and of thy people Israel, when they shall pray toward this place; and hear thou in heaven thy dwelling place; and when thou hearest, forgive.",
      "M": "Hear the plea of your servant and of your people Israel when they pray toward this place. Hear in heaven your dwelling place, and when you hear, forgive.",
      "T": "Hear the plea of your servant and of your people Israel when they pray toward this place. Hear in heaven—your true dwelling place—and when you hear, forgive."
    },
    "31": {
      "L": "If any man trespass against his neighbour, and an oath be laid upon him to cause him to swear, and the oath come before thine altar in this house:",
      "M": "If someone sins against a neighbor and is required to take an oath, and comes before your altar in this house to swear—",
      "T": "If someone wrongs a neighbor and is required to swear an oath, and comes before your altar in this house to swear—"
    },
    "32": {
      "L": "Then hear thou in heaven, and do, and judge thy servants, condemning the wicked, to bring his way upon his head; and justifying the righteous, to give him according to his righteousness.",
      "M": "then hear in heaven and act. Judge your servants: condemn the guilty by bringing his deed on his own head, and vindicate the innocent by rewarding him according to his righteousness.",
      "T": "hear in heaven and act. Judge your servants: bring the guilty man's conduct back on his own head, and vindicate the innocent—reward him according to his righteousness."
    },
    "33": {
      "L": "When thy people Israel be smitten down before the enemy, because they have sinned against thee, and shall turn again to thee, and confess thy name, and pray, and make supplication unto thee in this house:",
      "M": "When your people Israel are defeated by an enemy because they have sinned against you, and they turn back to you, confess your name, and pray and plead with you in this house—",
      "T": "When your people Israel are struck down before an enemy because they have sinned against you, and they turn back, confess your name, and pray and plead in this house—"
    },
    "34": {
      "L": "Then hear thou in heaven, and forgive the sin of thy people Israel, and bring them again unto the land which thou gavest unto their fathers.",
      "M": "then hear in heaven and forgive the sin of your people Israel and bring them back to the land you gave to their fathers.",
      "T": "hear in heaven, forgive the sin of your people Israel, and restore them to the land you gave their ancestors."
    },
    "35": {
      "L": "When heaven is shut up, and there is no rain, because they have sinned against thee; if they pray toward this place, and confess thy name, and turn from their sin, when thou afflictest them:",
      "M": "When the sky is shut up and there is no rain because the people have sinned against you, if they pray toward this place, acknowledge your name, and turn from their sin as you discipline them—",
      "T": "When the sky is sealed and there is no rain because they have sinned against you—if they pray toward this place, confess your name, and turn from their sin under your discipline—"
    },
    "36": {
      "L": "Then hear thou in heaven, and forgive the sin of thy servants, and of thy people Israel, that thou teach them the good way wherein they should walk, and give rain upon thy land, which thou hast given to thy people for an inheritance.",
      "M": "then hear in heaven, forgive the sin of your servants your people Israel, teach them the right way to walk, and send rain on your land that you gave to your people as their inheritance.",
      "T": "hear in heaven, forgive the sin of your servants your people Israel, teach them the right path, and send rain on the land you gave them as their inheritance."
    },
    "37": {
      "L": "If there be in the land famine, if there be pestilence, blasting, mildew, locust, or if there be caterpillar; if their enemy besiege them in the land of their cities; whatsoever plague, whatsoever sickness there be;",
      "M": "If there is famine in the land, or pestilence, blight or mildew, locusts or grasshoppers, or if the enemy besieges their cities—whatever plague or sickness there is—",
      "T": "When the land suffers famine, pestilence, blight or mildew, locust swarms or grasshoppers; when enemies besiege their towns; whatever plague or illness strikes—"
    },
    "38": {
      "L": "What prayer and supplication soever be made by any man, or by all thy people Israel, which shall know every man the plague of his own heart, and spread forth his hands toward this house:",
      "M": "whatever prayer or plea is made by any person or by all your people Israel—each knowing the affliction of his own heart—and they stretch out their hands toward this house,",
      "T": "whatever prayer or plea any person makes—each one knowing the wound of his own heart—and stretches his hands toward this house:"
    },
    "39": {
      "L": "Then hear thou in heaven thy dwelling place, and forgive, and do, and give to every man according to his ways, whose heart thou knowest; (for thou, even thou only, knowest the hearts of all the children of men;)",
      "M": "then hear in heaven your dwelling place, forgive, and act. Give to each person according to his ways, whose heart you know—for you alone know the heart of every human being—",
      "T": "hear in heaven—your true dwelling place. Forgive, and act. Give to each person according to his ways, whose heart you know—for you alone know every human heart—"
    },
    "40": {
      "L": "That they may fear thee all the days that they live in the land which thou gavest unto our fathers.",
      "M": "so that they may fear you all the days they live in the land you gave to our fathers.",
      "T": "that they may live in reverence before you all their days in the land you gave our fathers."
    },
    "41": {
      "L": "Moreover concerning a stranger, that is not of thy people Israel, but cometh out of a far country for thy name's sake;",
      "M": "Moreover, when a foreigner—someone not of your people Israel—comes from a distant land because of your name,",
      "T": "When a foreigner—not of your people Israel—comes from a distant land because of your name:"
    },
    "42": {
      "L": "(For they shall hear of thy great name, and of thy strong hand, and of thy stretched out arm;) when he shall come and pray toward this house;",
      "M": "(for they will hear of your great name and your mighty, outstretched arm)—when he comes and prays toward this house,",
      "T": "they will hear of your great name and your mighty, outstretched arm. When he comes and prays toward this house,"
    },
    "43": {
      "L": "Hear thou in heaven thy dwelling place, and do according to all that the stranger calleth to thee for; that all people of the earth may know thy name, to fear thee, as do thy people Israel; and that they may know that this house, which I have built, is called by thy name.",
      "M": "hear in heaven your dwelling place and grant everything for which the foreigner prays—so that all peoples of the earth may know your name and fear you as your people Israel do, and may know that this house I have built bears your name.",
      "T": "hear in heaven—your true dwelling—and grant whatever the foreigner asks, so that all the peoples of the earth may know your name and fear you as your people Israel do, and know that this house I built is called by your name."
    },
    "44": {
      "L": "If thy people go out to battle against their enemy, whithersoever thou shalt send them, and shall pray unto the LORD toward the city which thou hast chosen, and toward the house that I have built for thy name:",
      "M": "When your people go out to war against their enemy by whatever way you send them, and they pray to the LORD toward the city you have chosen and the house I have built for your name,",
      "T": "When your people go out to battle against an enemy—wherever you send them—and they pray to the LORD toward the city you have chosen and the house I have built for your name,"
    },
    "45": {
      "L": "Then hear thou in heaven their prayer and their supplication, and maintain their cause.",
      "M": "then hear their prayer and plea in heaven and uphold their cause.",
      "T": "hear their prayer and plea in heaven and uphold their cause."
    },
    "46": {
      "L": "If they sin against thee, (for there is no man that sinneth not,) and thou be angry with them, and deliver them to the enemy, so that they carry them away captives unto the land of the enemy, far or near;",
      "M": "If they sin against you—for there is no one who does not sin—and you are angry and hand them over to the enemy, so they are carried off as captives to a distant or nearby land,",
      "T": "If they sin against you—for no one is without sin—and you are angry and hand them over to enemies who carry them off to a far or near land in captivity,"
    },
    "47": {
      "L": "Yet if they shall bethink themselves in the land whither they were carried captives, and repent, and make supplication unto thee in the land of them that carried them captives, saying, We have sinned, and have done perversely, we have committed wickedness;",
      "M": "yet if in the land of their captivity they come to their senses and repent, and pray to you in their captors' land, saying, We have sinned, we have done wrong, we have acted wickedly—",
      "T": "if in their captors' land they come to their senses, repent, and cry out to you—We have sinned, we have done wrong, we have acted wickedly—"
    },
    "48": {
      "L": "And so return unto thee with all their heart, and with all their soul, in the land of their enemies, which led them away captive, and pray unto thee toward their land, which thou gavest unto their fathers, the city which thou hast chosen, and the house which I have built for thy name:",
      "M": "if they return to you with all their heart and soul in the land of their enemies, and pray toward their own land that you gave their ancestors, the city you have chosen, and the house I have built for your name,",
      "T": "if they return to you with their whole heart and soul in the land of their captors—praying toward their land, the city you have chosen, the house I have built for your name—"
    },
    "49": {
      "L": "Then hear thou their prayer and their supplication in heaven thy dwelling place, and maintain their cause,",
      "M": "then hear their prayer and their plea from heaven, your dwelling place, and uphold their cause—",
      "T": "hear their prayer and plea in heaven—your true dwelling place—and uphold their cause:"
    },
    "50": {
      "L": "And forgive thy people that have sinned against thee, and all their transgressions wherein they have transgressed against thee, and give them compassion before them who carried them captive, that they may have compassion on them:",
      "M": "forgive your people who have sinned against you and all their transgressions, and move their captors to show them compassion—",
      "T": "forgive your people who sinned against you—all their transgressions—and move their captors to show them compassion,"
    },
    "51": {
      "L": "For they be thy people, and thine inheritance, which thou broughtest forth out of Egypt, from the midst of the furnace of iron:",
      "M": "for they are your people, your own inheritance, whom you brought out of Egypt, out of that iron-smelting furnace.",
      "T": "for they are your people—your own inheritance—whom you brought out of Egypt's iron furnace."
    },
    "52": {
      "L": "That thine eyes may be open unto the supplication of thy servant, and unto the supplication of thy people Israel, to hearken unto them in all that they call for unto thee.",
      "M": "May your eyes be open to your servant's plea and to your people Israel's plea, listening to them whenever they call on you.",
      "T": "May your eyes be open to your servant's prayer and to your people Israel's prayer—listening to them in everything they cry out to you."
    },
    "53": {
      "L": "For thou didst separate them from among all the people of the earth, to be thine inheritance, as thou spakest by the hand of Moses thy servant, when thou broughtest our fathers out of Egypt, O Lord GOD.",
      "M": "For you separated them from all the peoples of the earth to be your inheritance, as you declared through your servant Moses when you brought our fathers out of Egypt, O Lord GOD.",
      "T": "For you set them apart from all the peoples of the earth to be your inheritance—as you declared through your servant Moses when you brought our fathers out of Egypt. O Lord GOD."
    },
    "54": {
      "L": "And it was so, that when Solomon had made an end of praying all this prayer and supplication unto the LORD, he arose from before the altar of the LORD, from kneeling on his knees with his hands spread up to heaven.",
      "M": "When Solomon had finished this entire prayer and supplication to the LORD, he rose from before the altar where he had been kneeling with his hands spread toward heaven.",
      "T": "When Solomon had finished the entire prayer and supplication to the LORD, he rose from before the altar. He had been kneeling with his hands stretched toward heaven."
    },
    "55": {
      "L": "And he stood, and blessed all the congregation of Israel with a loud voice, saying,",
      "M": "He stood and blessed the whole assembly of Israel with a loud voice:",
      "T": "Standing, he blessed the entire assembly of Israel with a loud voice:"
    },
    "56": {
      "L": "Blessed be the LORD, that hath given rest unto his people Israel, according to all that he promised: there hath not failed one word of all his good promise, which he promised by the hand of Moses his servant.",
      "M": "Blessed be the LORD, who has given rest to his people Israel in keeping with all his promises. Not one word has fallen to the ground of all the good promises he made through his servant Moses.",
      "T": "Blessed be the LORD, who has given his people Israel rest—just as he promised. Not one word of all his good promises spoken through his servant Moses has gone unfulfilled."
    },
    "57": {
      "L": "The LORD our God be with us, as he was with our fathers: let him not leave us, nor forsake us:",
      "M": "May the LORD our God be with us as he was with our fathers. May he never abandon or forsake us,",
      "T": "May the LORD our God be with us as he was with our fathers. May he never leave or forsake us—"
    },
    "58": {
      "L": "That he may incline our hearts unto him, to walk in all his ways, and to keep his commandments, and his statutes, and his judgments, which he commanded our fathers.",
      "M": "that he may incline our hearts toward him, to walk in all his ways and keep his commandments, statutes, and ordinances that he commanded our fathers.",
      "T": "but incline our hearts toward him—to walk in all his ways, keeping his commandments, his statutes, and his ordinances that he gave our fathers."
    },
    "59": {
      "L": "And let these my words, wherewith I have made supplication before the LORD, be nigh unto the LORD our God day and night, that he maintain the cause of his servant, and the cause of his people Israel at all times, as the matter shall require:",
      "M": "May these words of mine with which I have prayed before the LORD remain near to the LORD our God day and night, that he may uphold the cause of his servant and the cause of his people Israel, each day as the need arises,",
      "T": "May these words I have prayed before the LORD remain before him day and night, so that he upholds the cause of his servant and of his people Israel—each day as each day demands,"
    },
    "60": {
      "L": "That all the people of the earth may know that the LORD is God, and that there is none else.",
      "M": "so that all the peoples of the earth may know that the LORD is God—there is no other.",
      "T": "so that all the peoples of the earth may know: the LORD is God. There is no other."
    },
    "61": {
      "L": "Let your heart therefore be perfect with the LORD our God, to walk in his statutes, and to keep his commandments, as at this day.",
      "M": "May your heart be wholly devoted to the LORD our God, walking in his statutes and keeping his commandments, as you do today.",
      "T": "Let your heart be wholly true to the LORD your God—walk in his statutes, keep his commandments, as you are doing this very day."
    },
    "62": {
      "L": "And the king, and all Israel with him, offered sacrifice before the LORD.",
      "M": "Then the king and all Israel offered sacrifices before the LORD.",
      "T": "Then the king and all Israel offered sacrifices before the LORD."
    },
    "63": {
      "L": "And Solomon offered a sacrifice of peace offerings, which he offered unto the LORD, two and twenty thousand oxen, and an hundred and twenty thousand sheep. So the king and all the children of Israel dedicated the house of the LORD.",
      "M": "Solomon offered as a peace offering to the LORD twenty-two thousand oxen and a hundred and twenty thousand sheep. So the king and all the people of Israel dedicated the house of the LORD.",
      "T": "Solomon offered as peace offerings twenty-two thousand oxen and a hundred and twenty thousand sheep. So the king and all Israel dedicated the LORD's house."
    },
    "64": {
      "L": "The same day did the king hallow the middle of the court that was before the house of the LORD: for there he offered burnt offerings, and meat offerings, and the fat of the peace offerings; because the brasen altar that was before the LORD was too little to receive the burnt offerings, and meat offerings, and the fat of the peace offerings.",
      "M": "That same day the king consecrated the middle of the court in front of the LORD's house, for he offered the burnt offerings, the grain offerings, and the fat portions of the peace offerings there—because the bronze altar before the LORD was too small to hold them all.",
      "T": "That same day the king consecrated the middle of the courtyard before the LORD's house—the bronze altar was too small—and there he offered the burnt offerings, the grain offerings, and the fat portions of the peace offerings."
    },
    "65": {
      "L": "And at that time Solomon held a feast, and all Israel with him, a great congregation, from the entering in of Hamath unto the river of Egypt, before the LORD our God, seven days and seven days, even fourteen days.",
      "M": "At that time Solomon held the feast, and all Israel with him—a great assembly from Lebo-hamath to the Brook of Egypt—before the LORD our God, for seven days and seven days: fourteen days in all.",
      "T": "Solomon and all Israel—a great assembly from Lebo-hamath to the Brook of Egypt—celebrated before the LORD their God for seven days and another seven: fourteen days in all."
    },
    "66": {
      "L": "On the eighth day he sent the people away; and they blessed the king, and went unto their tents joyful and glad of heart for all the goodness that the LORD had done for David his servant, and for Israel his people.",
      "M": "On the eighth day he dismissed the people. They blessed the king and went to their homes full of joy and gladness for all the goodness the LORD had shown to his servant David and to his people Israel.",
      "T": "On the eighth day he sent the people home. They blessed the king and returned to their tents with hearts full of joy and gladness—for all the goodness the LORD had shown to his servant David and to his people Israel."
    }
  },
  "9": {
    "1": {
      "L": "And it came to pass, when Solomon had finished the building of the house of the LORD, and the king's house, and all Solomon's desire which he was pleased to do,",
      "M": "When Solomon had finished building the house of the LORD and the royal palace and all that he had desired to build,",
      "T": "When Solomon had completed the house of the LORD, the royal palace, and everything he had desired to build,"
    },
    "2": {
      "L": "That the LORD appeared to Solomon the second time, as he had appeared unto him at Gibeon.",
      "M": "the LORD appeared to Solomon a second time, just as he had appeared to him at Gibeon.",
      "T": "the LORD appeared to Solomon a second time—just as he had appeared to him at Gibeon."
    },
    "3": {
      "L": "And the LORD said unto him, I have heard thy prayer and thy supplication, that thou hast made before me: I have hallowed this house, which thou hast built, to put my name there for ever; and mine eyes and mine heart shall be there perpetually.",
      "M": "The LORD said to him, 'I have heard your prayer and your plea that you made before me. I have consecrated this house you have built by putting my name there forever. My eyes and my heart will be there at all times.'",
      "T": "The LORD said to him: 'I have heard your prayer and your plea before me. I have set apart this house you have built—my name is there forever. My eyes and my heart will be there for all time.'"
    },
    "4": {
      "L": "And if thou wilt walk before me, as David thy father walked, in integrity of heart, and in uprightness, to do according to all that I have commanded thee, and wilt keep my statutes and my judgments:",
      "M": "As for you, if you walk before me as your father David walked—with integrity and uprightness, doing all I have commanded you and keeping my statutes and ordinances—",
      "T": "As for you: if you walk before me as your father David walked—with wholehearted integrity, doing all I have commanded, keeping my statutes and ordinances—"
    },
    "5": {
      "L": "Then I will establish the throne of thy kingdom upon Israel for ever, as I promised to David thy father, saying, There shall not fail thee a man upon the throne of Israel.",
      "M": "then I will establish your royal throne over Israel forever, as I promised your father David: you will never lack a man on the throne of Israel.",
      "T": "then I will establish your throne over Israel forever—as I promised your father David: Israel's throne will never lack a man from your line."
    },
    "6": {
      "L": "But if ye shall at all turn from following me, ye or your children, and will not keep my commandments and my statutes which I have set before you, but go and serve other gods, and worship them:",
      "M": "But if you or your children turn away from following me and do not keep my commandments and statutes that I have placed before you, and instead go and serve other gods and worship them,",
      "T": "But if you or your children turn aside from following me—refusing the commandments and statutes I have set before you—and instead go and serve other gods and bow down to them,"
    },
    "7": {
      "L": "Then will I cut off Israel out of the land which I have given them; and this house, which I have hallowed for my name, will I cast out of my sight; and Israel shall be a proverb and a byword among all people:",
      "M": "then I will cut off Israel from the land I have given them, and I will cast from my sight this house I consecrated for my name. Israel will become a proverb and a mockery among all peoples.",
      "T": "then I will cut Israel off from the land I gave them and expel from my sight this house I consecrated for my name. Israel will become a proverb and a byword among all nations—as Deuteronomy warned."
    },
    "8": {
      "L": "And at this house, which is high, every one that passeth by it shall be astonished, and shall hiss; and they shall say, Why hath the LORD done thus unto this land, and to this house?",
      "M": "This exalted house will become a ruin. Everyone who passes by will be appalled and will hiss, saying, Why has the LORD done this to this land and this house?",
      "T": "This house, now so magnificent, will lie in ruins. Every passerby will be appalled and will hiss: Why has the LORD done this to this land and this house?"
    },
    "9": {
      "L": "And they shall answer, Because they forsook the LORD their God, who brought forth their fathers out of the land of Egypt, and have taken hold upon other gods, and have worshipped them, and served them: therefore hath the LORD brought upon them all this evil.",
      "M": "The answer will be: Because they abandoned the LORD their God who brought their fathers out of Egypt, and took hold of other gods, worshiping and serving them—that is why the LORD brought all this disaster on them.",
      "T": "The answer will be: Because they abandoned the LORD their God who brought their fathers out of Egypt, and they took hold of other gods—worshiping and serving them. That is why the LORD brought all this disaster on them."
    },
    "10": {
      "L": "And it came to pass at the end of twenty years, when Solomon had built the two houses, the house of the LORD, and the king's house,",
      "M": "After twenty years, during which Solomon built the two buildings—the house of the LORD and the royal palace—",
      "T": "Twenty years passed while Solomon built the two great buildings—the LORD's house and his own palace."
    },
    "11": {
      "L": "Now Hiram the king of Tyre had furnished Solomon with cedar trees and fir trees, and with gold, according to all his desire; that then King Solomon gave Hiram twenty cities in the land of Galilee.",
      "M": "Since Hiram king of Tyre had supplied Solomon with cedar, cypress, and gold in whatever amount he needed, King Solomon gave Hiram twenty cities in the territory of Galilee.",
      "T": "Hiram king of Tyre had supplied Solomon with all the cedar, cypress, and gold he needed. In return, King Solomon gave Hiram twenty towns in the Galilee region."
    },
    "12": {
      "L": "And Hiram came out from Tyre to see the cities which Solomon had given him; and they pleased him not.",
      "M": "But when Hiram came from Tyre to inspect the towns Solomon had given him, they did not please him.",
      "T": "But when Hiram came from Tyre to inspect the towns Solomon had given him, he was not pleased."
    },
    "13": {
      "L": "And he said, What cities are these which thou hast given me, my brother? And he called them the land of Cabul unto this day.",
      "M": "He said, 'What are these towns you have given me, my brother?' So they were called the land of Cabul—as they are known to this day.",
      "T": "He said: 'What kind of towns are these you have given me, my brother?' So the area was called the land of Cabul—a name it bears to this day. The payment of twenty towns for cedar, cypress, and gold was hardly a fair exchange."
    },
    "14": {
      "L": "And Hiram sent to the king sixscore talents of gold.",
      "M": "Hiram had sent the king a hundred and twenty talents of gold.",
      "T": "Hiram had sent the king a hundred and twenty talents of gold."
    },
    "15": {
      "L": "And this is the reason of the levy which King Solomon raised; for to build the house of the LORD, and his own house, and Millo, and the wall of Jerusalem, and Hazor, and Megiddo, and Gezer.",
      "M": "This is the account of the forced labor King Solomon conscripted to build the house of the LORD, his own palace, the Millo, the wall of Jerusalem, and the cities of Hazor, Megiddo, and Gezer.",
      "T": "This is a record of the forced labor Solomon levied—for building the LORD's house, his own palace, the Millo, the Jerusalem wall, and the fortified cities of Hazor, Megiddo, and Gezer."
    },
    "16": {
      "L": "(For Pharaoh king of Egypt had gone up, and taken Gezer, and burnt it with fire, and slain the Canaanites that dwelt in the city, and given it for a present unto his daughter, Solomon's wife:",
      "M": "(Pharaoh king of Egypt had captured Gezer, burned it down, killed the Canaanites who lived there, and given it as a wedding gift to his daughter, Solomon's wife.",
      "T": "(Pharaoh king of Egypt had come up and captured Gezer, burned it, killed the Canaanites who lived there, and given it as a dowry to his daughter—Solomon's wife."
    },
    "17": {
      "L": "And Solomon built Gezer, and Bethhoron the nether,",
      "M": "So Solomon rebuilt Gezer) and Lower Beth-horon,",
      "T": "Solomon rebuilt Gezer) and also Lower Beth-horon,"
    },
    "18": {
      "L": "And Baalath, and Tadmor in the wilderness, in the land,",
      "M": "Baalath, and Tamar in the wilderness,",
      "T": "Baalath, and Tamar in the wilderness,"
    },
    "19": {
      "L": "And all the cities of store that Solomon had, and cities for his chariots, and cities for his horsemen, and that which Solomon desired to build in Jerusalem, and in Lebanon, and in all the land of his dominion.",
      "M": "and all his store cities, his chariot cities, his cavalry cities, and whatever Solomon desired to build in Jerusalem, Lebanon, and throughout his entire realm.",
      "T": "and all his storage cities, chariot cities, and cavalry towns—and everything else Solomon wanted to build in Jerusalem, Lebanon, and throughout his entire domain."
    },
    "20": {
      "L": "And all the people that were left of the Amorites, Hittites, Perizzites, Hivites, and Jebusites, which were not of the children of Israel,",
      "M": "All the non-Israelite peoples that remained in the land—Amorites, Hittites, Perizzites, Hivites, and Jebusites—",
      "T": "The non-Israelite peoples remaining in the land—Amorites, Hittites, Perizzites, Hivites, and Jebusites—"
    },
    "21": {
      "L": "Their children that were left after them in the land, whom the children of Israel also were not able utterly to destroy, upon those did Solomon levy a tribute of bondservice unto this day.",
      "M": "their descendants still in the land—those the Israelites had been unable to destroy completely—Solomon conscripted as forced laborers, and they remain so to this day.",
      "T": "their descendants who remained—those Israel had never been able to destroy—Solomon put to forced labor. They remain so to this day."
    },
    "22": {
      "L": "But of the children of Israel did Solomon make no bondmen; but they were men of war, and his servants, and his princes, and his captains, and rulers of his chariots, and his horsemen.",
      "M": "But Solomon did not make any Israelites into slaves; they served as soldiers, his officials, commanders, captains, chariot commanders, and horsemen.",
      "T": "But Solomon did not conscript Israelites as slaves. They served as soldiers, officials, commanders, captains, chariot officers, and cavalry—a distinction that would prove fragile."
    },
    "23": {
      "L": "These were the chief of the officers that were over Solomon's work, five hundred and fifty, which bare rule over the people that wrought in the work.",
      "M": "These were Solomon's chief officers over his workforce: five hundred and fifty, who supervised the people doing the labor.",
      "T": "Five hundred and fifty chief officers supervised Solomon's workforce and oversaw all the labor."
    },
    "24": {
      "L": "But Pharaoh's daughter came up out of the city of David unto her house which Solomon had built for her: then did he build Millo.",
      "M": "Pharaoh's daughter moved from the city of David into her own palace that Solomon had built for her. Then he built the Millo.",
      "T": "Pharaoh's daughter moved from the city of David into the palace Solomon had built for her. After that he built the Millo."
    },
    "25": {
      "L": "And three times in a year did Solomon offer burnt offerings and peace offerings upon the altar which he built unto the LORD, and he burnt incense upon the altar that was before the LORD. So he finished the house.",
      "M": "Three times a year Solomon offered burnt offerings and peace offerings on the altar he had built for the LORD. So he completed the house.",
      "T": "Three times a year Solomon offered burnt offerings and peace offerings on the altar he had built for the LORD, and burned incense before the LORD. So the house was complete."
    },
    "26": {
      "L": "And King Solomon made a navy of ships in Eziongeber, which is beside Eloth, on the shore of the Red sea, in the land of Edom.",
      "M": "King Solomon built a fleet of ships at Ezion-geber, near Eloth on the shore of the Red Sea, in the land of Edom.",
      "T": "King Solomon built a fleet of ships at Ezion-geber, near Eloth on the shore of the Red Sea, in the land of Edom."
    },
    "27": {
      "L": "And Hiram sent in the navy his servants, shipmen that had knowledge of the sea, with the servants of Solomon.",
      "M": "Hiram sent his own servants—experienced sailors who knew the sea—to serve alongside Solomon's men.",
      "T": "Hiram sent his own sailors with the fleet—men who knew the sea—to serve alongside Solomon's servants."
    },
    "28": {
      "L": "And they came to Ophir, and fetched from thence gold, four hundred and twenty talents, and brought it to King Solomon.",
      "M": "They sailed to Ophir and brought back four hundred and twenty talents of gold to King Solomon.",
      "T": "They sailed to Ophir and returned with four hundred and twenty talents of gold for King Solomon."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1kings')
        merge_tier(existing, KINGS, tier_key)
        save(tier_dir, '1kings', existing)
    print('1 Kings 7–9 written.')

if __name__ == '__main__':
    main()
