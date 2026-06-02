"""
MKT Exodus chapters 37–40 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-37-40.py

Covers the completion of the tabernacle's construction: Bezaleel makes the sacred furniture
(ch. 37), the bronze altar, laver, court, and materials accounting (ch. 38), the priestly
vestments and presentation to Moses (ch. 39), and Moses erecting the tabernacle with the
divine cloud-glory filling it (ch. 40).

Translation decisions:
- H3068 (יהוה): "the LORD" in L/M/T — consistent with all prior Exodus scripts
- H430 (אֱלֹהִים): "God" — consistent with prior scripts
- H4908 (מִשְׁכָּן): "tabernacle" in L/M; T uses "tabernacle" also (the glory-filling of ch. 40
  makes "dwelling" redundantly obvious — the act itself shows God dwelling there)
- H168 (אֹהֶל מוֹעֵד): "tent of meeting" throughout — NOT "tent of the congregation" (KJV);
  מוֹעֵד = appointed meeting-place, not a general assembly
- H727 (אָרוֹן): "ark" throughout; appositional phrases ("of the testimony," "of the covenant")
  carried where the Hebrew has them
- H3727 (כַּפֹּרֶת): "mercy seat" in all tiers — the kapporeth is the lid of the ark and the
  locus of atonement (from כָּפַר, to cover/atone); "atonement cover" is accurate but breaks
  the established register; "mercy seat" retained
- H3742 (כְּרוּב): "cherubim" throughout (Hebrew plural already; no "cherubs")
- H4501 (מְנוֹרָה): "lampstand" in all tiers — "candlestick" (KJV) is an anachronism for
  an oil-burning lamp on a stand
- H7848 (שִׁטִּים): "acacia" in all tiers — "shittim wood" (KJV) is an obscure transliteration;
  the Sinai acacia (Acacia tortilis) is the actual tree
- H5178 (נְחֹשֶׁת): "bronze" in all tiers — "brass" (KJV) is an anachronism; the material
  is copper alloy (bronze), not the zinc-copper alloy (brass) unknown in the ancient Near East
- H3519 (כָּבוֹד): "glory" in L/M; T expands to "radiant glory" at 40:34-35 where the
  luminous filling of the tabernacle is the climax of the book
- H6944 (קֹדֶשׁ): "holy" / "holiness" throughout; "HOLINESS TO THE LORD" on the gold plate
  (39:30) rendered in capitals to reflect the Hebrew engraving convention
- H3899 הַפָּנִים (bread of the Presence): "bread of the Presence" in M/T; L="showbread" only
  where the Hebrew has the full construct phrase; "shewbread" (KJV) is archaic
- Breastplate gemstones (39:10-13): Hebrew gem names are uncertain. L uses traditional KJV
  renderings as closest to the Masoretic tradition; M/T use the best modern scholarly consensus:
  H124 (אֹדֶם) sardius → carnelian; H6357 (פִּטְדָה) topaz → topaz/chrysolite; H1304 (בָּרֶקֶת)
  carbuncle → emerald; H5306 (נֹפֶךְ) emerald → turquoise; H5601 (סַפִּיר) sapphire → lapis
  lazuli; H3095 (יַהֲלֹם) diamond → moonstone/crystal; H8658 (תַּרְשִׁישׁ) beryl → beryl/
  chrysolite; H7718 (שֹׁהַם) onyx → onyx; H3471 (יָשְׁפֵה) jasper → jasper
- "As the LORD commanded Moses" refrain (appears ~18x in chs 39-40): kept verbatim in L/M;
  T occasionally adds "exactly" or "precisely" to honor its structural weight — this refrain
  is the theological spine of the final two chapters, showing total covenant obedience
- The cloud and fire (40:34-38): climax of Exodus; the tabernacle becomes God's dwelling
  among Israel. T surfaces the glory as the book's resolution: God now moves with his people.
- 38:8 (laver from women's mirrors): a remarkable detail — women surrendered polished metal
  mirrors (a luxury item) for sacred use; M/T preserve this note explicitly
- 38:21-31 (material accounting): the precision of inventory mirrors the precision of obedience;
  the silver bekah per person (38:26) echoes the census of ch. 30 and the 603,550 total
- Verbal aspect: the Waw-consecutive perfect in chs. 37-39 expresses completed narrative past
  ("he made," "he overlaid"); in ch. 40 the jussive/imperfect shifts to direct divine command
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

EXODUS = {
  "37": {
    "1": {
      "L": "And Bezaleel made the ark of acacia wood: two cubits and a half its length, and a cubit and a half its breadth, and a cubit and a half its height.",
      "M": "Bezaleel made the ark of acacia wood — two and a half cubits long, one and a half cubits wide, and one and a half cubits high.",
      "T": "Bezaleel built the ark from acacia wood: two and a half cubits long, a cubit and a half wide, a cubit and a half tall."
    },
    "2": {
      "L": "And he overlaid it with pure gold within and without, and made for it a crown of gold round about.",
      "M": "He overlaid it with pure gold inside and out, and made a gold molding around it.",
      "T": "He sheathed it in pure gold inside and outside, then ran a gold molding around the top."
    },
    "3": {
      "L": "And he cast for it four rings of gold at its four corners — two rings on one side and two rings on the other side of it.",
      "M": "He cast four gold rings for its four corners — two on one side and two on the other.",
      "T": "He cast four gold rings for the four corners, two on each side."
    },
    "4": {
      "L": "And he made poles of acacia wood and overlaid them with gold.",
      "M": "He made the carrying poles of acacia wood and overlaid them with gold.",
      "T": "He shaped the carrying poles from acacia wood and overlaid them with gold."
    },
    "5": {
      "L": "And he put the poles into the rings on the sides of the ark to carry the ark.",
      "M": "He inserted the poles through the rings on the sides of the ark for carrying it.",
      "T": "He threaded the poles through the rings along the ark's sides so it could be lifted and carried."
    },
    "6": {
      "L": "And he made the mercy seat of pure gold: two cubits and a half its length and a cubit and a half its breadth.",
      "M": "He made the mercy seat of pure gold — two and a half cubits long and one and a half cubits wide.",
      "T": "He fashioned the mercy seat from pure gold: two and a half cubits long, a cubit and a half wide."
    },
    "7": {
      "L": "And he made two cherubim of gold, of beaten work, at the two ends of the mercy seat:",
      "M": "He made two cherubim of hammered gold at the two ends of the mercy seat.",
      "T": "He shaped two cherubim from hammered gold, one at each end of the mercy seat."
    },
    "8": {
      "L": "one cherub at this end and one cherub at that end; of the mercy seat he made the cherubim at its two ends.",
      "M": "One cherub was at one end and the other at the other end — the cherubim were made as one piece with the mercy seat at each end.",
      "T": "One cherub stood at one end, one at the other — both formed as a single piece with the mercy seat."
    },
    "9": {
      "L": "And the cherubim spread out their wings above, overshadowing the mercy seat with their wings, and their faces were toward one another — toward the mercy seat were the faces of the cherubim.",
      "M": "The cherubim spread their wings upward, overshadowing the mercy seat, facing each other with their faces turned toward the mercy seat.",
      "T": "The cherubim spread their wings upward, sheltering the mercy seat beneath them — their faces turned toward one another, inclined downward toward the mercy seat."
    },
    "10": {
      "L": "And he made the table of acacia wood: two cubits its length, and a cubit its breadth, and a cubit and a half its height.",
      "M": "He made the table of acacia wood — two cubits long, one cubit wide, and one and a half cubits high.",
      "T": "He built the table from acacia wood: two cubits long, one cubit wide, a cubit and a half high."
    },
    "11": {
      "L": "And he overlaid it with pure gold and made for it a crown of gold round about.",
      "M": "He overlaid it with pure gold and made a gold molding around it.",
      "T": "He covered it with pure gold and set a gold molding around the top."
    },
    "12": {
      "L": "And he made for it a border of a handbreadth round about, and made a crown of gold for its border round about.",
      "M": "He made a rim of a handbreadth around it and a gold molding along the rim all around.",
      "T": "He added a frame a handbreadth wide around the table's edge, with a gold molding running along the top of the frame."
    },
    "13": {
      "L": "And he cast for it four rings of gold and put the rings on the four corners that were at its four feet.",
      "M": "He cast four gold rings and attached them at the four corners where the legs met the top.",
      "T": "He cast four gold rings and fixed them at the four leg-corners of the table."
    },
    "14": {
      "L": "The rings were close against the border, as places for the poles to carry the table.",
      "M": "The rings were set close to the rim — housings for the poles used to carry the table.",
      "T": "The rings sat just inside the rim, positioned to receive the carrying poles."
    },
    "15": {
      "L": "And he made the poles of acacia wood and overlaid them with gold to carry the table.",
      "M": "He made the carrying poles of acacia wood and overlaid them with gold.",
      "T": "He made the poles from acacia wood and overlaid them with gold."
    },
    "16": {
      "L": "And he made the vessels upon the table — its dishes and its spoons and its bowls and its covers to pour with — of pure gold.",
      "M": "He made the utensils for the table of pure gold: its plates, its incense dishes, its bowls, and its pitchers for the drink offerings.",
      "T": "He fashioned all the table's serving vessels from pure gold — plates, incense dishes, bowls, and pitchers for the drink offerings."
    },
    "17": {
      "L": "And he made the lampstand of pure gold; of beaten work he made the lampstand — its base and its shaft, its cups, its buds, and its flowers were of the same piece.",
      "M": "He made the lampstand of pure gold — hammered out as one piece — its base, shaft, cups, buds, and blossoms all of the same.",
      "T": "He hammered the lampstand from a single piece of pure gold: base, shaft, almond-shaped cups, calyx buds, and open blossoms — all one."
    },
    "18": {
      "L": "And six branches going out of its sides: three branches of the lampstand out of one side of it, and three branches of the lampstand out of the other side of it.",
      "M": "Six branches extended from its sides — three from one side and three from the other.",
      "T": "Six branches spread from the central shaft — three on each side."
    },
    "19": {
      "L": "Three cups made like almonds, with a bud and a flower, in one branch; and three cups made like almonds, with a bud and a flower, in another branch — so for the six branches going out of the lampstand.",
      "M": "Each of the six branches had three almond-shaped cups, each with a bud and a blossom.",
      "T": "Every branch bore three almond-shaped cups — each with a calyx bud and an open blossom — on all six branches."
    },
    "20": {
      "L": "And in the lampstand were four cups made like almonds, with its buds and its flowers.",
      "M": "The central shaft of the lampstand had four almond-shaped cups with their buds and blossoms.",
      "T": "The shaft itself bore four almond-shaped cups with buds and blossoms."
    },
    "21": {
      "L": "And a bud under two branches of the same, and a bud under two branches of the same, and a bud under two branches of the same — for the six branches going out of it.",
      "M": "There was a bud beneath every pair of branches — one bud per pair, for the three pairs.",
      "T": "Below each pair of branches was a calyx bud — one bud per pair, three pairs in all."
    },
    "22": {
      "L": "Their buds and their branches were of the same — all of it was one beaten work of pure gold.",
      "M": "The buds and branches were all of one piece — the entire lampstand hammered from a single mass of pure gold.",
      "T": "Buds, branches, every detail — hammered from one undivided piece of pure gold."
    },
    "23": {
      "L": "And he made its seven lamps and its snuffers and its trays of pure gold.",
      "M": "He made its seven lamps, its wick trimmers, and its tray dishes of pure gold.",
      "T": "He fashioned seven lamps for it, along with its wick trimmers and catch-trays — all pure gold."
    },
    "24": {
      "L": "Of a talent of pure gold he made it and all its vessels.",
      "M": "He made it and all its utensils from a talent of pure gold.",
      "T": "The lampstand and all its accessories required a full talent of pure gold."
    },
    "25": {
      "L": "And he made the incense altar of acacia wood: a cubit its length, and a cubit its breadth — foursquare — and two cubits its height; its horns were of the same.",
      "M": "He made the incense altar from acacia wood — one cubit square and two cubits high — with horns formed from the same piece.",
      "T": "He made the incense altar from acacia wood: one cubit on each side, a perfect square, two cubits tall, with horns carved from the same piece."
    },
    "26": {
      "L": "And he overlaid it with pure gold — its top and its sides round about and its horns — and made for it a crown of gold round about.",
      "M": "He overlaid it with pure gold — top, sides, and horns — and made a gold molding around it.",
      "T": "He overlaid every surface with pure gold — top, sides, and horns — and set a gold molding around the top."
    },
    "27": {
      "L": "And he made for it two rings of gold under its crown at its two corners on both its sides, as places for the poles to carry it.",
      "M": "He made two gold rings beneath the molding on both sides as holders for the carrying poles.",
      "T": "He fastened two gold rings beneath the molding, one on each side, to receive the carrying poles."
    },
    "28": {
      "L": "And he made the poles of acacia wood and overlaid them with gold.",
      "M": "He made the carrying poles of acacia wood and overlaid them with gold.",
      "T": "He made the poles from acacia wood and overlaid them with gold."
    },
    "29": {
      "L": "And he made the holy anointing oil and the pure fragrant incense, according to the work of the perfumer.",
      "M": "He also prepared the holy anointing oil and the pure aromatic incense — the skilled work of a perfumer.",
      "T": "He also compounded the sacred anointing oil and the pure aromatic incense — the craft of a master perfumer."
    }
  },
  "38": {
    "1": {
      "L": "And he made the altar of burnt offering of acacia wood — five cubits its length and five cubits its breadth, foursquare — and three cubits its height.",
      "M": "He made the altar of burnt offering from acacia wood — five cubits square and three cubits high.",
      "T": "He built the burnt offering altar from acacia wood: five cubits on each side — a perfect square — and three cubits high."
    },
    "2": {
      "L": "And he made its horns on its four corners — its horns were of the same — and he overlaid it with bronze.",
      "M": "He made horns at its four corners from the same piece and overlaid the whole altar with bronze.",
      "T": "He fashioned horns at all four corners from the same piece, then overlaid everything with bronze."
    },
    "3": {
      "L": "And he made all the vessels of the altar: the pots and the shovels and the basins and the forks and the firepans — all its vessels he made of bronze.",
      "M": "He made all the altar's utensils from bronze: the pots, shovels, basins, flesh-hooks, and firepans.",
      "T": "Every implement for the altar was fashioned from bronze: pots, shovels, tossing-bowls, flesh-hooks, and firepans."
    },
    "4": {
      "L": "And he made for the altar a grate of bronze network under its ledge, from below to its midpoint.",
      "M": "He made a bronze lattice grating for the altar, fitted beneath its ledge, extending to the altar's midpoint.",
      "T": "He made a bronze lattice grating for the altar, set beneath the surrounding ledge and reaching halfway up."
    },
    "5": {
      "L": "And he cast four rings for the four corners of the bronze grate, as places for the poles.",
      "M": "He cast four rings at the four corners of the bronze grating to hold the carrying poles.",
      "T": "He cast four rings at the four corners of the grating to receive the carrying poles."
    },
    "6": {
      "L": "And he made the poles of acacia wood and overlaid them with bronze.",
      "M": "He made the carrying poles of acacia wood and overlaid them with bronze.",
      "T": "He made the poles from acacia wood and overlaid them with bronze."
    },
    "7": {
      "L": "And he put the poles into the rings on the sides of the altar to carry it with them; he made it hollow with boards.",
      "M": "He inserted the poles through the rings on the altar's sides for transport; the altar was made hollow with planks.",
      "T": "He threaded the poles through the rings on both sides so the altar could be carried; the altar itself was built hollow of planks."
    },
    "8": {
      "L": "And he made the laver of bronze and its base of bronze from the mirrors of the women who served at the entrance of the tent of meeting.",
      "M": "He made the bronze basin and its bronze stand from the polished metal mirrors of the women who gathered to serve at the entrance to the tent of meeting.",
      "T": "He cast the bronze basin and its stand from the polished metal mirrors surrendered by the women who served at the entrance of the tent of meeting — a luxury offered for sacred use."
    },
    "9": {
      "L": "And he made the court: for the south side, southward, the curtains of the court were of fine twined linen, a hundred cubits.",
      "M": "He made the court: along the south side the curtains were of fine twisted linen, a hundred cubits long.",
      "T": "He constructed the court: the south side had curtains of fine twisted linen running a hundred cubits."
    },
    "10": {
      "L": "Their pillars were twenty and their sockets twenty, of bronze; the hooks of the pillars and their bands were of silver.",
      "M": "They hung on twenty posts with twenty bronze bases; the hooks and bands on the posts were silver.",
      "T": "Twenty posts on twenty bronze bases supported them; the hooks and connecting bands were silver."
    },
    "11": {
      "L": "And for the north side the curtains were a hundred cubits; their pillars twenty and their sockets twenty, of bronze; the hooks of the pillars and their bands of silver.",
      "M": "The north side likewise had curtains of a hundred cubits, with twenty posts and twenty bronze bases; hooks and bands were silver.",
      "T": "The north side matched: a hundred cubits of curtains on twenty posts in twenty bronze bases, silver hooks and bands."
    },
    "12": {
      "L": "And for the west side the curtains were fifty cubits; their pillars ten and their sockets ten; the hooks of the pillars and their bands of silver.",
      "M": "The west side had curtains of fifty cubits on ten posts with ten bases; hooks and bands were silver.",
      "T": "The west side had fifty cubits of curtains on ten posts and ten bases, with silver hooks and bands."
    },
    "13": {
      "L": "And for the east side eastward, fifty cubits.",
      "M": "The east side extended fifty cubits.",
      "T": "The east face was fifty cubits across."
    },
    "14": {
      "L": "The curtains for one side of the gate were fifteen cubits; their pillars three and their sockets three.",
      "M": "Curtains fifteen cubits long hung on three posts with three bases on one side of the entrance.",
      "T": "On one side of the entrance, fifteen cubits of curtains hung on three posts with three bases."
    },
    "15": {
      "L": "And for the other side — on this hand and that hand of the gate of the court — curtains were fifteen cubits; their pillars three and their sockets three.",
      "M": "The same arrangement was on the other side of the court gate: fifteen cubits of curtains with three posts and three bases.",
      "T": "The same framed the other side of the entrance — fifteen cubits of curtains, three posts, three bases."
    },
    "16": {
      "L": "All the curtains of the court round about were of fine twined linen.",
      "M": "All the curtains surrounding the court were made of fine twisted linen.",
      "T": "Every curtain enclosing the court was woven from fine twisted linen."
    },
    "17": {
      "L": "The sockets for the pillars were of bronze; the hooks of the pillars and their bands were of silver; and the overlaying of their capitals was of silver; and all the pillars of the court were banded with silver.",
      "M": "The post bases were bronze; the hooks and bands were silver; the tops of the posts were overlaid with silver — all the court's posts were silver-crowned.",
      "T": "The bases were bronze, but every hook, connecting band, and post-cap was silver — the entire court ringed with silver-topped pillars."
    },
    "18": {
      "L": "And the screen of the gate of the court was embroidery of blue and purple and scarlet and fine twined linen; and twenty cubits was its length and five cubits its height, corresponding to the curtains of the court.",
      "M": "The screen for the court gate was embroidered in blue, purple, and scarlet on fine twisted linen — twenty cubits wide and five cubits high, matching the court curtains.",
      "T": "The entrance screen was embroidered in blue, purple, and scarlet on fine twisted linen — twenty cubits wide and five cubits tall, matching the surrounding curtains in height."
    },
    "19": {
      "L": "And their pillars were four, and their sockets four, of bronze; their hooks of silver, and the overlaying of their capitals and their bands of silver.",
      "M": "This screen hung on four posts with four bronze bases; the hooks were silver and the post-tops were overlaid with silver.",
      "T": "Four posts on four bronze bases held it in place, with silver hooks and silver-overlaid tops."
    },
    "20": {
      "L": "And all the tent pegs for the tabernacle and for the court round about were of bronze.",
      "M": "All the tent pegs for the tabernacle and the surrounding court were bronze.",
      "T": "Every tent peg used throughout the tabernacle and its court was bronze."
    },
    "21": {
      "L": "This is the accounting of the tabernacle, the tabernacle of the testimony, as counted at the commandment of Moses — the service of the Levites by the hand of Ithamar son of Aaron the priest.",
      "M": "This is the record of the materials for the tabernacle — the tabernacle of the testimony — compiled at Moses' command under Ithamar son of Aaron the priest, who oversaw the Levites' work.",
      "T": "What follows is the official inventory of the tabernacle — the tabernacle of the covenant — compiled at Moses' command, with Ithamar son of Aaron the priest overseeing the Levitical accounting."
    },
    "22": {
      "L": "And Bezaleel son of Uri son of Hur of the tribe of Judah made all that the LORD commanded Moses.",
      "M": "Bezaleel son of Uri son of Hur, of the tribe of Judah, made everything the LORD had commanded Moses.",
      "T": "Bezaleel son of Uri son of Hur — of the tribe of Judah — built every piece exactly as the LORD had commanded Moses."
    },
    "23": {
      "L": "And with him was Oholiab son of Ahisamach of the tribe of Dan — an engraver and a skilled craftsman and an embroiderer in blue and purple and scarlet and fine linen.",
      "M": "Working with him was Oholiab son of Ahisamach of the tribe of Dan — an engraver, a master craftsman, and an embroiderer in blue, purple, and scarlet on fine linen.",
      "T": "His partner was Oholiab son of Ahisamach of Dan — engraver, master craftsman, and embroiderer in blue, purple, and scarlet linen."
    },
    "24": {
      "L": "All the gold that was used in the work, in all the work of the sanctuary — the gold of the wave offering — was twenty-nine talents and seven hundred and thirty shekels, by the shekel of the sanctuary.",
      "M": "The total gold used in the sanctuary work — the gold from the wave offering — came to twenty-nine talents and seven hundred thirty shekels, by the sanctuary standard.",
      "T": "The total gold expended in the sanctuary's construction — brought as a wave offering — came to twenty-nine talents and seven hundred thirty shekels by the sanctuary weight."
    },
    "25": {
      "L": "And the silver of those numbered of the congregation was a hundred talents and a thousand seven hundred and seventy-five shekels, by the shekel of the sanctuary.",
      "M": "The silver from those counted in the community came to one hundred talents and one thousand seven hundred seventy-five shekels, by the sanctuary standard.",
      "T": "The silver tallied from the community census came to one hundred talents and seventeen hundred seventy-five shekels by the sanctuary weight."
    },
    "26": {
      "L": "A beka for every head — that is, half a shekel, by the shekel of the sanctuary — for everyone who passed through the counting, from twenty years old and upward, for six hundred and three thousand five hundred and fifty men.",
      "M": "That is, a half-shekel — one beka — for each person counted, everyone twenty years and older: a total of 603,550 men.",
      "T": "Half a shekel per person — one beka apiece — levied on every man twenty years or older counted in the census: 603,550 men in all."
    },
    "27": {
      "L": "And the hundred talents of silver were for casting the sockets of the sanctuary and the sockets of the veil — a hundred sockets from the hundred talents, a talent for a socket.",
      "M": "The hundred talents of silver were cast into the hundred bases for the sanctuary frames and the inner veil — one talent per base.",
      "T": "The hundred talents went entirely to casting the hundred bases — the sanctuary's structural footings and the veil's posts — one talent per base."
    },
    "28": {
      "L": "And of the thousand seven hundred and seventy-five shekels he made hooks for the pillars and overlaid their capitals and banded them.",
      "M": "From the remaining seventeen hundred seventy-five shekels he made the hooks, overlaid the post-tops, and made the connecting bands.",
      "T": "The remaining seventeen hundred seventy-five shekels provided the hooks, the silver caps, and the bands for all the court posts."
    },
    "29": {
      "L": "And the bronze of the wave offering was seventy talents and two thousand four hundred shekels.",
      "M": "The bronze from the wave offering totaled seventy talents and two thousand four hundred shekels.",
      "T": "The bronze brought as an offering totaled seventy talents and twenty-four hundred shekels."
    },
    "30": {
      "L": "And with it he made the sockets of the entrance of the tent of meeting, and the bronze altar, and the bronze grate for it, and all the vessels of the altar,",
      "M": "With this he made the bases for the entrance of the tent of meeting, the bronze altar with its bronze grating, and all the altar's utensils,",
      "T": "From this he cast the threshold-bases of the tent of meeting, the bronze altar and its lattice grating, and all the altar's implements,"
    },
    "31": {
      "L": "and the sockets of the court round about, and the sockets of the gate of the court, and all the tent pegs of the tabernacle, and all the tent pegs of the court round about.",
      "M": "the bases for the surrounding court and the court gate, and all the tent pegs for the tabernacle and the surrounding court.",
      "T": "the bases for the entire surrounding court and its gate, and every peg used throughout the tabernacle and its court."
    }
  },
  "39": {
    "1": {
      "L": "And of the blue and purple and scarlet they made woven garments for serving in the holy place, and made the holy garments for Aaron — as the LORD commanded Moses.",
      "M": "From the blue, purple, and scarlet material they made the vestments for service in the sanctuary, and the sacred garments for Aaron, just as the LORD had commanded Moses.",
      "T": "From the blue, purple, and scarlet yarn they wove the vestments for holy service and the sacred garments for Aaron — all exactly as the LORD commanded Moses."
    },
    "2": {
      "L": "And he made the ephod of gold, blue and purple and scarlet and fine twined linen.",
      "M": "He made the ephod of gold, blue, purple, scarlet, and fine twisted linen.",
      "T": "He crafted the ephod from gold thread woven with blue, purple, and scarlet yarn on fine twisted linen."
    },
    "3": {
      "L": "And they beat the gold into thin plates and cut it into wires to work it into the blue and into the purple and into the scarlet and into the fine linen, in skilled work.",
      "M": "They hammered the gold into flat sheets, cut it into threads, and wove these threads through the blue, purple, and scarlet yarn and the fine linen — the work of a master craftsman.",
      "T": "They hammered the gold flat, cut it into wire-thin threads, and wove them through the blue, purple, and scarlet yarns and the fine linen — a craftsman's precision art."
    },
    "4": {
      "L": "Shoulder pieces were made for it, coupled together; at its two edges it was coupled together.",
      "M": "The ephod had shoulder pieces made and joined at its two upper edges.",
      "T": "Two shoulder pieces were attached, joining the front and back panels at the top edges."
    },
    "5": {
      "L": "And the skillfully woven waistband of his ephod that was on it was of the same, of the same work: gold, blue and purple and scarlet and fine twined linen — as the LORD commanded Moses.",
      "M": "The decorated waistband of the ephod was made the same way and of the same materials — gold, blue, purple, scarlet, and fine twisted linen — just as the LORD commanded Moses.",
      "T": "The ephod's integrated sash was of the same weave and same materials — gold, blue, purple, scarlet, fine linen — exactly as the LORD commanded Moses."
    },
    "6": {
      "L": "And they worked the onyx stones, enclosed in settings of gold, engraved as signet engravings with the names of the children of Israel.",
      "M": "They mounted the onyx stones in gold filigree settings and engraved them with the names of the Israelites, as one engraves a signet seal.",
      "T": "They set the onyx stones in gold filigree mounts and engraved on them the names of Israel's twelve tribes — cut as cleanly as a seal."
    },
    "7": {
      "L": "And he set them on the shoulder pieces of the ephod — stones of remembrance for the children of Israel — as the LORD commanded Moses.",
      "M": "He fastened them on the shoulder pieces of the ephod as memorial stones for the Israelites, just as the LORD had commanded Moses.",
      "T": "He mounted them on the ephod's shoulder pieces — memorial stones for the twelve tribes of Israel — exactly as the LORD commanded Moses."
    },
    "8": {
      "L": "And he made the breastplate in skilled work, like the work of the ephod: of gold, blue and purple and scarlet and fine twined linen.",
      "M": "He made the breastplate using the same skilled technique as the ephod: gold, blue, purple, scarlet, and fine twisted linen.",
      "T": "He wove the breastplate in the same master-craftsman style as the ephod — gold thread through blue, purple, scarlet, and fine twisted linen."
    },
    "9": {
      "L": "It was foursquare; they made the breastplate doubled — a span its length and a span its breadth, doubled.",
      "M": "They folded it double to make it square — a span long and a span wide.",
      "T": "Folded double to make a perfect square — a span in each direction."
    },
    "10": {
      "L": "And they set in it four rows of stones: a row of a sardius, a topaz, and a carbuncle — this was the first row.",
      "M": "They mounted four rows of precious stones in it. The first row: a carnelian, a topaz, and an emerald.",
      "T": "Into the breastplate they set four rows of gemstones. First row: carnelian, topaz, emerald."
    },
    "11": {
      "L": "And the second row: an emerald, a sapphire, and a diamond.",
      "M": "The second row: a turquoise, a lapis lazuli, and a moonstone.",
      "T": "Second row: turquoise, lapis lazuli, moonstone."
    },
    "12": {
      "L": "And the third row: a jacinth, an agate, and an amethyst.",
      "M": "The third row: a jacinth, an agate, and an amethyst.",
      "T": "Third row: jacinth, agate, amethyst."
    },
    "13": {
      "L": "And the fourth row: a beryl, an onyx, and a jasper — enclosed in settings of gold in their mounting.",
      "M": "The fourth row: a beryl, an onyx, and a jasper — all set in gold filigree.",
      "T": "Fourth row: beryl, onyx, jasper — each gem held in a gold filigree mount."
    },
    "14": {
      "L": "And the stones were according to the names of the children of Israel, twelve, according to their names — engravings like a signet, each one with his name, for the twelve tribes.",
      "M": "There was one stone for each of the twelve tribes of Israel — each engraved like a signet seal with the name of one tribe.",
      "T": "Twelve stones, one for each tribe of Israel — every stone engraved with a tribe's name, cut with the precision of a seal-maker."
    },
    "15": {
      "L": "And they made upon the breastplate chains of twisted work — wreathen chains of pure gold.",
      "M": "They made braided chains of pure gold for the breastplate.",
      "T": "They braided chains of pure gold for the breastplate."
    },
    "16": {
      "L": "And they made two settings of gold and two gold rings and put the two rings on the two ends of the breastplate.",
      "M": "They made two gold settings and two gold rings, attaching the rings to the two upper corners of the breastplate.",
      "T": "They made two gold mounts and two gold rings and fastened the rings to the breastplate's upper corners."
    },
    "17": {
      "L": "And they put the two wreathen chains of gold in the two rings at the ends of the breastplate.",
      "M": "They attached the two braided gold chains to the two rings at the top of the breastplate.",
      "T": "The two braided chains were threaded through the rings at the breastplate's upper corners."
    },
    "18": {
      "L": "And the two ends of the two wreathen chains they fastened in the two settings and put them on the shoulder pieces of the ephod, in front.",
      "M": "The other ends of the chains they fastened to the two gold mounts on the ephod's front shoulder pieces.",
      "T": "The chains' other ends they secured in the gold mounts on the ephod's shoulder pieces, in front."
    },
    "19": {
      "L": "And they made two rings of gold and put them on the two ends of the breastplate, on its edge on the inward side facing the ephod.",
      "M": "They made two more gold rings and attached them to the lower corners of the breastplate — on the inner edge facing the ephod.",
      "T": "Two more rings they fixed at the lower corners of the breastplate, on the inside edge that rested against the ephod."
    },
    "20": {
      "L": "And they made two golden rings and fastened them on the two shoulder pieces of the ephod underneath, in front at its joining, above the skillfully woven waistband of the ephod.",
      "M": "They also made two gold rings and attached them to the lower front of the ephod's shoulder pieces, just above where they joined — above the ephod's waistband.",
      "T": "They fastened two more rings to the lower front of the ephod's shoulder pieces — just above where the sash began."
    },
    "21": {
      "L": "And they bound the breastplate by its rings to the rings of the ephod with a blue cord, so that it was above the skillfully woven waistband of the ephod, and that the breastplate might not come loose from the ephod — as the LORD commanded Moses.",
      "M": "They tied the breastplate's lower rings to the ephod's rings with a blue cord so that the breastplate sat above the waistband and could not swing loose from the ephod — just as the LORD commanded Moses.",
      "T": "Using a blue cord, they lashed the breastplate's lower rings to the ephod's rings, anchoring it above the waistband so it could not come free — exactly as the LORD had commanded Moses."
    },
    "22": {
      "L": "And he made the robe of the ephod of woven work, entirely of blue.",
      "M": "He made the robe for the ephod entirely of woven blue.",
      "T": "He wove the robe of the ephod entirely in blue — a single seamless piece."
    },
    "23": {
      "L": "And the hole of the robe was in its midst, like the hole of a coat of mail, with a bound edge all around the hole so that it would not tear.",
      "M": "The robe had a woven neck opening at its center — like the neck of a soldier's tunic — with a bound edge all around to prevent tearing.",
      "T": "The neck opening was woven into the center of the garment, its edges bound like a warrior's tunic so the fabric would not split under use."
    },
    "24": {
      "L": "And they made on the hem of the robe pomegranates of blue and purple and scarlet and twisted linen.",
      "M": "They made pomegranates of blue, purple, and scarlet yarn on fine twisted linen to hang around the robe's hem.",
      "T": "Around the robe's hem they attached pomegranates woven in blue, purple, and scarlet on fine twisted linen."
    },
    "25": {
      "L": "And they made bells of pure gold and put the bells between the pomegranates on the hem of the robe round about, between the pomegranates.",
      "M": "They made bells of pure gold and placed them alternating with the pomegranates all around the hem.",
      "T": "Between the pomegranates they hung pure gold bells, alternating all the way around the hem."
    },
    "26": {
      "L": "A bell and a pomegranate, a bell and a pomegranate, on the hem of the robe round about, for ministering — as the LORD commanded Moses.",
      "M": "Bell and pomegranate, bell and pomegranate, alternating all around the hem — for wear when ministering — just as the LORD commanded Moses.",
      "T": "Bell, pomegranate, bell, pomegranate — alternating all the way around the hem for sacred service. Exactly as the LORD commanded Moses."
    },
    "27": {
      "L": "And they made the tunics of fine linen, woven work, for Aaron and for his sons,",
      "M": "They made woven linen tunics for Aaron and his sons,",
      "T": "They wove fine linen tunics for Aaron and his sons,"
    },
    "28": {
      "L": "and the turban of fine linen, and the ornate headbands of fine linen, and the linen undergarments of fine twined linen,",
      "M": "the turban of fine linen, the ornate headbands of fine linen, and the undergarments of fine twisted linen,",
      "T": "the fine linen turban, the fine linen headbands, the fine linen undergarments,"
    },
    "29": {
      "L": "and the sash of fine twined linen and blue and purple and scarlet, embroidered work — as the LORD commanded Moses.",
      "M": "and the sash of fine twisted linen embroidered with blue, purple, and scarlet — just as the LORD commanded Moses.",
      "T": "and the embroidered sash of fine twisted linen worked through with blue, purple, and scarlet — all as the LORD commanded Moses."
    },
    "30": {
      "L": "And they made the plate of the holy crown of pure gold and wrote upon it an inscription like the engravings of a signet: HOLINESS TO THE LORD.",
      "M": "They made the sacred plate of pure gold and engraved on it, as one engraves a seal: HOLINESS TO THE LORD.",
      "T": "They made the sacred gold medallion and engraved on it — sharp and permanent as a seal — the words: HOLINESS TO THE LORD."
    },
    "31": {
      "L": "And they tied on it a lace of blue to fasten it on the turban above — as the LORD commanded Moses.",
      "M": "They attached a blue cord to it to tie it to the front of the turban — just as the LORD had commanded Moses.",
      "T": "A blue cord was threaded through it for tying it to the front of the turban — exactly as the LORD commanded Moses."
    },
    "32": {
      "L": "Thus all the work of the tabernacle of the tent of meeting was finished, and the children of Israel did according to all that the LORD commanded Moses — so they did.",
      "M": "So all the work on the tabernacle — the tent of meeting — was completed. The Israelites had done everything just as the LORD had commanded Moses.",
      "T": "Every part of the tabernacle — the tent of meeting — was now finished. The Israelites had carried out every command the LORD had given Moses. They had done it all."
    },
    "33": {
      "L": "And they brought the tabernacle to Moses: the tent and all its furnishings, its clasps, its frames, its bars, and its pillars and its sockets,",
      "M": "They brought everything to Moses: the tabernacle with all its components — its clasps, frames, crossbars, pillars, and bases,",
      "T": "They brought the completed tabernacle to Moses — the tent itself and every accessory: clasps, frames, crossbars, pillars, bases,"
    },
    "34": {
      "L": "and the covering of rams' skins dyed red, and the covering of fine leather, and the curtain of the veil,",
      "M": "the covering of ram skins dyed red, the covering of fine leather, and the inner curtain veil,",
      "T": "the red-dyed ram-skin covering, the outer fine-leather covering, and the inner veil,"
    },
    "35": {
      "L": "the ark of the testimony with its poles and the mercy seat,",
      "M": "the ark of the testimony with its carrying poles and the mercy seat,",
      "T": "the ark of the covenant with its poles and the mercy seat,"
    },
    "36": {
      "L": "the table with all its vessels and the showbread,",
      "M": "the table with all its utensils and the bread of the Presence,",
      "T": "the table with its vessels and the arranged bread of the Presence,"
    },
    "37": {
      "L": "the pure lampstand with its lamps, the lamps to be set in order, and all its vessels, and the oil for the light,",
      "M": "the pure gold lampstand with its lamps arranged in order, all its utensils, and the oil for the light,",
      "T": "the golden lampstand with its seven lamps set in order, its accessories, and the lamp oil,"
    },
    "38": {
      "L": "and the golden altar, and the anointing oil, and the fragrant incense, and the screen for the entrance of the tent,",
      "M": "the golden incense altar, the anointing oil, the aromatic incense, and the hanging screen for the tent entrance,",
      "T": "the golden incense altar, the anointing oil, the fragrant incense, and the entrance screen,"
    },
    "39": {
      "L": "the bronze altar and its bronze grate, its poles and all its vessels, the laver and its base,",
      "M": "the bronze altar with its bronze grating, its carrying poles and all its utensils, and the bronze basin with its stand,",
      "T": "the bronze altar with its lattice grating, poles, and implements, the bronze basin and its stand,"
    },
    "40": {
      "L": "the curtains of the court, its pillars and its sockets, and the screen of the gate of the court, its cords and its tent pegs, and all the furnishings for the service of the tabernacle, for the tent of meeting,",
      "M": "the curtains of the court with their pillars and bases, the screen for the court gate with its ropes and tent pegs, and all the equipment for the tabernacle — the tent of meeting,",
      "T": "the court curtains with their pillars and bases, the gate screen with its ropes and pegs — all the equipment for the tent of meeting,"
    },
    "41": {
      "L": "the garments of service for ministering in the holy place, the holy garments for Aaron the priest, and the garments of his sons for ministering in the priest's office.",
      "M": "the woven vestments for serving in the sanctuary, the sacred garments for Aaron the priest, and the garments of his sons for serving as priests.",
      "T": "the vestments for holy service, the sacred garments of Aaron the priest, and the garments of his sons for their priestly ministry."
    },
    "42": {
      "L": "According to all that the LORD commanded Moses, so the children of Israel did all the work.",
      "M": "The Israelites had done all the work exactly as the LORD had commanded Moses.",
      "T": "The Israelites executed every part of the work precisely as the LORD had commanded Moses."
    },
    "43": {
      "L": "And Moses looked upon all the work, and behold, they had done it; as the LORD had commanded, so they had done. And Moses blessed them.",
      "M": "Moses inspected all the work and saw that they had done it just as the LORD commanded. And Moses blessed them.",
      "T": "Moses reviewed the entire construction. When he saw that every piece had been made exactly as the LORD commanded — he blessed them."
    }
  },
  "40": {
    "1": {
      "L": "And the LORD spoke to Moses, saying:",
      "M": "Then the LORD said to Moses:",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "'On the first day of the first month you shall erect the tabernacle of the tent of meeting.'",
      "M": "'On the first day of the first month, set up the tabernacle — the tent of meeting.'",
      "T": "'On the first day of the new year, erect the tabernacle — the tent of meeting.'"
    },
    "3": {
      "L": "'And you shall place therein the ark of the testimony and screen the ark with the veil.'",
      "M": "'Put the ark of the testimony inside and screen it with the inner veil.'",
      "T": "'Place the ark of the covenant inside, then draw the inner veil before it.'"
    },
    "4": {
      "L": "'And you shall bring in the table and set in order what belongs on it, and you shall bring in the lampstand and light its lamps.'",
      "M": "'Bring in the table and arrange what belongs on it; bring in the lampstand and light its lamps.'",
      "T": "'Bring in the table and set it in order; bring in the lampstand and light its lamps.'"
    },
    "5": {
      "L": "'And you shall set the golden altar of incense before the ark of the testimony and hang up the screen of the entrance of the tabernacle.'",
      "M": "'Set the golden incense altar before the ark of the testimony, and hang the entrance screen.'",
      "T": "'Place the golden incense altar in front of the ark, and hang the entrance screen.'"
    },
    "6": {
      "L": "'And you shall set the altar of burnt offering before the entrance of the tabernacle of the tent of meeting.'",
      "M": "'Place the altar of burnt offering at the entrance to the tabernacle — the tent of meeting.'",
      "T": "'Set the burnt offering altar at the tabernacle's entrance.'"
    },
    "7": {
      "L": "'And you shall set the laver between the tent of meeting and the altar and put water in it.'",
      "M": "'Place the basin between the tent of meeting and the altar and fill it with water.'",
      "T": "'Set the bronze basin between the tent of meeting and the altar, and fill it with water.'"
    },
    "8": {
      "L": "'And you shall set up the court round about and hang up the screen of the gate of the court.'",
      "M": "'Set up the surrounding court and hang the screen at the court gate.'",
      "T": "'Erect the surrounding court and hang the entrance screen.'"
    },
    "9": {
      "L": "'And you shall take the anointing oil and anoint the tabernacle and all that is in it, and consecrate it and all its furnishings, and it shall be holy.'",
      "M": "'Take the anointing oil and anoint the tabernacle and everything in it; consecrate it and all its furnishings, and it will be holy.'",
      "T": "'Take the anointing oil and anoint the tabernacle — every part of it — and consecrate it with all its furnishings. It will become most holy.'"
    },
    "10": {
      "L": "'And you shall anoint the altar of burnt offering and all its vessels and consecrate the altar, and the altar shall be most holy.'",
      "M": "'Anoint the altar of burnt offering with all its utensils and consecrate it, and it will be most holy.'",
      "T": "'Anoint the bronze altar and all its implements — consecrate it, and it will be most holy.'"
    },
    "11": {
      "L": "'And you shall anoint the laver and its base and consecrate it.'",
      "M": "'Anoint the basin and its stand and consecrate them.'",
      "T": "'Anoint the basin and its stand and consecrate them.'"
    },
    "12": {
      "L": "'And you shall bring Aaron and his sons to the entrance of the tent of meeting and wash them with water.'",
      "M": "'Bring Aaron and his sons to the entrance of the tent of meeting and wash them with water.'",
      "T": "'Bring Aaron and his sons to the tent of meeting's entrance and wash them with water.'"
    },
    "13": {
      "L": "'And you shall put on Aaron the holy garments and anoint him and consecrate him, that he may minister to me in the priest's office.'",
      "M": "'Dress Aaron in the sacred garments, anoint him, and consecrate him so that he may serve me as priest.'",
      "T": "'Clothe Aaron in the sacred vestments, anoint him, and consecrate him — that he may serve before me as priest.'"
    },
    "14": {
      "L": "'And you shall bring his sons and clothe them with tunics.'",
      "M": "'Bring his sons and clothe them with tunics.'",
      "T": "'Bring his sons and put the tunics on them.'"
    },
    "15": {
      "L": "'And you shall anoint them as you anointed their father, that they may minister to me in the priest's office, and their anointing shall be an everlasting priesthood throughout their generations.'",
      "M": "'Anoint them as you anointed their father so they may serve me as priests. Their anointing will establish a lasting priesthood throughout their generations.'",
      "T": "'Anoint them just as you anointed their father, that they may serve before me as priests. This anointing will inaugurate an enduring priestly line for all their descendants.'"
    },
    "16": {
      "L": "Thus Moses did; according to all that the LORD commanded him, so he did.",
      "M": "Moses did everything just as the LORD had commanded him.",
      "T": "Moses carried out every one of these commands. He did exactly as the LORD had instructed."
    },
    "17": {
      "L": "And it came to pass in the first month of the second year, on the first day of the month, that the tabernacle was erected.",
      "M": "On the first day of the first month of the second year, the tabernacle was set up.",
      "T": "On the first day of the first month of the second year — exactly one year from the Exodus — the tabernacle was raised."
    },
    "18": {
      "L": "And Moses erected the tabernacle and laid its sockets and set up its frames and put in its crossbars and erected its pillars.",
      "M": "Moses set up the tabernacle: he put in the bases, stood up the frames, inserted the crossbars, and raised the pillars.",
      "T": "Moses assembled the tabernacle: he laid the bases, stood the frames upright, fitted the crossbars, and raised the pillars."
    },
    "19": {
      "L": "And he spread the tent over the tabernacle and put the covering of the tent above it — as the LORD commanded Moses.",
      "M": "He spread the tent covering over the tabernacle and laid the outer cover on top — just as the LORD had commanded Moses.",
      "T": "He spread the tent covering over the frame, then laid the outer cover on top — as the LORD commanded Moses."
    },
    "20": {
      "L": "And he took and put the testimony into the ark, and set the poles on the ark, and put the mercy seat above on the ark.",
      "M": "He took the testimony tablets and placed them in the ark, inserted the carrying poles, and set the mercy seat on top.",
      "T": "He placed the covenant tablets inside the ark, fitted the carrying poles, and set the mercy seat over the top."
    },
    "21": {
      "L": "And he brought the ark into the tabernacle and hung up the screening veil and screened the ark of the testimony — as the LORD commanded Moses.",
      "M": "He brought the ark into the tabernacle and hung the inner veil, screening off the ark of the testimony — just as the LORD had commanded Moses.",
      "T": "He carried the ark into the inner room and drew the veil across, shielding the ark — exactly as the LORD commanded Moses."
    },
    "22": {
      "L": "And he set the table in the tent of meeting, on the north side of the tabernacle, outside the veil.",
      "M": "He set up the table in the tent of meeting on the north side of the tabernacle, outside the inner veil.",
      "T": "He placed the table on the north side of the tent, outside the inner veil."
    },
    "23": {
      "L": "And he set in order the bread upon it before the LORD — as the LORD commanded Moses.",
      "M": "He arranged the bread on the table before the LORD, just as the LORD had commanded Moses.",
      "T": "He arranged the bread of the Presence on it before the LORD — as the LORD commanded Moses."
    },
    "24": {
      "L": "And he put the lampstand in the tent of meeting, opposite the table, on the south side of the tabernacle.",
      "M": "He placed the lampstand in the tent of meeting on the south side, opposite the table.",
      "T": "He set the lampstand on the south side of the tent, directly across from the table."
    },
    "25": {
      "L": "And he lit the lamps before the LORD — as the LORD commanded Moses.",
      "M": "He lit the lamps before the LORD, just as the LORD had commanded Moses.",
      "T": "He lit the lamps before the LORD — as the LORD commanded Moses."
    },
    "26": {
      "L": "And he set the golden altar in the tent of meeting before the veil,",
      "M": "He placed the golden incense altar in the tent of meeting in front of the inner veil,",
      "T": "He positioned the golden incense altar before the inner veil,"
    },
    "27": {
      "L": "and he burned fragrant incense on it — as the LORD commanded Moses.",
      "M": "and burned aromatic incense on it, just as the LORD had commanded Moses.",
      "T": "and burned fragrant incense on it — as the LORD commanded Moses."
    },
    "28": {
      "L": "And he hung up the screen of the entrance of the tabernacle.",
      "M": "He hung the screen at the tabernacle's entrance.",
      "T": "He hung the entrance screen."
    },
    "29": {
      "L": "And he set the altar of burnt offering at the entrance of the tabernacle of the tent of meeting and offered on it the burnt offering and the grain offering — as the LORD commanded Moses.",
      "M": "He placed the altar of burnt offering at the entrance to the tabernacle — the tent of meeting — and offered burnt offerings and grain offerings on it, just as the LORD had commanded Moses.",
      "T": "He positioned the burnt offering altar at the tabernacle's entrance and offered the first burnt offering and grain offering on it — precisely as the LORD commanded Moses."
    },
    "30": {
      "L": "And he set the laver between the tent of meeting and the altar and put water there for washing,",
      "M": "He placed the basin between the tent of meeting and the altar and filled it with water for washing,",
      "T": "He set the basin between the tent and the altar and filled it with water for ritual washing,"
    },
    "31": {
      "L": "and Moses and Aaron and his sons washed their hands and their feet from it,",
      "M": "and Moses, Aaron, and Aaron's sons washed their hands and feet at it,",
      "T": "and Moses, Aaron, and Aaron's sons washed their hands and feet at it —"
    },
    "32": {
      "L": "when they went into the tent of meeting and when they came near the altar, they washed — as the LORD commanded Moses.",
      "M": "Whenever they entered the tent of meeting or approached the altar, they washed — just as the LORD had commanded Moses.",
      "T": "every time they entered the tent of meeting or drew near the altar, they washed. As the LORD commanded Moses."
    },
    "33": {
      "L": "And he erected the court round about the tabernacle and the altar and hung up the screen of the gate of the court. So Moses finished the work.",
      "M": "He set up the surrounding court around the tabernacle and altar and hung the screen at the court gate. So Moses completed the work.",
      "T": "He raised the surrounding court around the tabernacle and altar and hung the gate screen. And with that, Moses finished the work."
    },
    "34": {
      "L": "Then the cloud covered the tent of meeting and the glory of the LORD filled the tabernacle.",
      "M": "Then the cloud covered the tent of meeting, and the glory of the LORD filled the tabernacle.",
      "T": "Then the cloud descended and covered the tent of meeting — and the glory of the LORD flooded the tabernacle."
    },
    "35": {
      "L": "And Moses was not able to enter the tent of meeting, for the cloud settled on it and the glory of the LORD filled the tabernacle.",
      "M": "Moses was unable to enter the tent of meeting, because the cloud had settled on it and the glory of the LORD filled the tabernacle.",
      "T": "Moses could not enter the tent of meeting — the cloud had come to rest upon it and the radiant glory of the LORD filled it from within."
    },
    "36": {
      "L": "And whenever the cloud was taken up from over the tabernacle, the children of Israel set out on all their journeys,",
      "M": "Whenever the cloud lifted from above the tabernacle, the Israelites set out on the next stage of their journey,",
      "T": "Whenever the cloud lifted from the tabernacle, Israel broke camp and moved out,"
    },
    "37": {
      "L": "but if the cloud was not taken up, then they did not set out until the day it was taken up.",
      "M": "but if the cloud did not lift, they did not set out — not until the day it lifted.",
      "T": "but when the cloud did not lift, they stayed put — until it moved."
    },
    "38": {
      "L": "For the cloud of the LORD was on the tabernacle by day, and fire was in it by night, before the eyes of all the house of Israel, throughout all their journeys.",
      "M": "The cloud of the LORD rested on the tabernacle by day, and fire glowed in the cloud by night — visible to all the house of Israel throughout all their travels.",
      "T": "The LORD's cloud rested over the tabernacle all day; fire burned within it through every night — a sign visible to every Israelite throughout every stage of the journey."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 37–40 written.')

if __name__ == '__main__':
    main()
