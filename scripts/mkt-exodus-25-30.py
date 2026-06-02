"""
MKT Exodus chapters 25–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-exodus-25-30.py

Covers the Tabernacle blueprint: furnishings (ch. 25), structure (ch. 26), courtyard and
altar (ch. 27), priestly garments (ch. 28), ordination ceremony and daily offering (ch. 29),
and the incense altar, atonement tax, laver, anointing oil, and sacred incense (ch. 30).

Translation decisions:
- H3068 (יהוה): "the LORD" in L/M/T — matches Genesis/Exodus convention
- H430 (אֱלֹהִים): "God" throughout
- H4908 (מִשְׁכָּן, mishkan): "tabernacle" in L/M; "sacred dwelling" in T where
  the dwelling-presence theme is foregrounded — root שכן means to dwell/abide;
  the whole structure is God's house among his people
- H727 (אָרוֹן): "ark" in all tiers — no better English term for the chest
- H3727 (כַּפֹּרֶת, kapporet): L="mercy seat" (historic), M="atonement cover",
  T="cover of atonement" — the site of Yom Kippur blood application; NT ἱλαστήριον
  (Rom 3:25, Heb 9:5) is drawn from this word
- H3742 (כְּרוּב): "cherub/cherubim" in all tiers — no adequate English rendering
- H7848 (שִׁטָּה, shittim): L="shittim wood", M/T="acacia wood" — the lightweight,
  hard, rot-resistant desert wood used throughout the tabernacle
- H651 (אֵפוֹד, ephod): "ephod" in all tiers — no English equivalent for this
  sacred garment worn only by the high priest
- H2833 (חֹשֶׁן, khoshen): L/M="breastpiece", T="sacred breastpiece" or
  "breastpiece of judgment" — carries Urim and Thummim and the twelve tribal stones
- H224 (אוּרִים) H8550 (תֻּמִּים): "Urim and Thummim" in all tiers — kept as
  proper names; meaning uncertain (possibly "Lights and Perfections" or "Oracles and
  Truth"); these were the priestly lots for discerning the divine will
- H5930 (עֹלָה, olah): L/M="burnt offering", T="whole burnt offering" — name means
  "that which ascends"; the entire animal is consumed
- H2403 (חַטָּאת, khatta't): L/M="sin offering", T="purification offering" — modern
  scholarship notes the primary function is purging sacred space, not merely personal sin
- H8002 (שֶׁלֶם, shelem): L="peace offering", M="fellowship offering",
  T="well-being offering" — communal meal aspect is foregrounded in T
- H4394 (מִלּוּאִים, milu'im): "ordination/consecration" — literally "filling of the
  hand"; the ram of consecration is the ram of milu'im
- H8548 (תָּמִיד, tamid): L="continual", M="regular", T="perpetual" —
  the daily morning and evening offering is the heartbeat of Israel's worship calendar
- H5258 (נֶסֶד, nesekh): "drink offering" / T="libation" — the wine poured out
- H4196 (מִזְבֵּחַ): "altar" in all tiers
- H5315 (נֶפֶשׁ): "soul" / "life" — at 30:12, "ransom for his soul/life"
- H6944 (קֹדֶשׁ): "holy" or "sanctuary" depending on grammatical context
- H6725 (צִיץ) at 28:36-38: "plate" (L), "plate" (M), "medallion" (T) — the gold
  diadem on the high priest's turban bearing "HOLY TO THE LORD"
- Divine name H3068 in 28:36: rendered in small caps as "the LORD" per convention;
  the plate text "HOLY TO THE LORD" uses all caps in the English tradition
- H7004 (קְטֹרֶת): "incense" — the sacred compound burned on the golden altar
- H4503 (מִנְחָה): "grain offering" in all tiers (in this context)
- Lex talionis principle from ch. 21 does not recur; ch. 25-30 is purely cultic
- OT intertextuality: ch. 25:22 — God speaking from between the cherubim echoes
  Numbers 7:89; ch. 29:45-46 — "I will dwell among them" becomes the telos of the
  entire Exodus narrative; Revelation 21:3 is the eschatological fulfillment
- The tamid (29:38-42) is the structural basis of all Jewish daily prayer (Shacharit
  and Mincha) and is quoted in Acts 3:1 and Hebrews 7:27, 9:6
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
  "25": {
    "1": {
      "L": "And the LORD spoke unto Moses, saying,",
      "M": "The LORD said to Moses,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "'Speak unto the children of Israel, that they bring me an offering; of every man that giveth it willingly with his heart ye shall take my offering.'",
      "M": "'Tell the Israelites to bring me an offering. You are to receive the offering for me from everyone whose heart moves them to give.'",
      "T": "'Tell the people of Israel to bring me a contribution. Receive it from every person whose heart moves them freely — this is my offering.'"
    },
    "3": {
      "L": "'And this is the offering which ye shall take of them: gold, and silver, and brass,'",
      "M": "'These are the offerings you are to receive from them: gold, silver and bronze,'",
      "T": "'Here is what you shall receive: gold, silver, and bronze;'"
    },
    "4": {
      "L": "'and blue, and purple, and scarlet, and fine linen, and goats' hair,'",
      "M": "'blue, purple and scarlet yarn and fine linen; goat hair,'",
      "T": "'blue, purple, and scarlet yarn; fine woven linen; goat hair;'"
    },
    "5": {
      "L": "'and rams' skins dyed red, and badgers' skins, and shittim wood,'",
      "M": "'ram skins dyed red, and hides of sea cows; acacia wood,'",
      "T": "'ram skins dyed red; fine leather; acacia wood;'"
    },
    "6": {
      "L": "'oil for the light, spices for anointing oil, and for sweet incense,'",
      "M": "'olive oil for the light; spices for the anointing oil and for the fragrant incense,'",
      "T": "'olive oil for the lamps; spices for the sacred anointing oil and for the fragrant incense;'"
    },
    "7": {
      "L": "'onyx stones, and stones to be set in the ephod, and in the breastplate.'",
      "M": "'onyx stones and other gems to be mounted on the ephod and breastpiece.'",
      "T": "'onyx stones and other precious stones to be set in the ephod and in the breastpiece.'"
    },
    "8": {
      "L": "'And let them make me a sanctuary; that I may dwell among them.'",
      "M": "'Then have them make a sanctuary for me, and I will dwell among them.'",
      "T": "'Let them make me a holy place — a sanctuary — so that I may live among them.'"
    },
    "9": {
      "L": "'According to all that I shew thee, after the pattern of the tabernacle, and the pattern of all the instruments thereof, even so shall ye make it.'",
      "M": "'Make it exactly as I show you — the plan of the tabernacle and the plan of all its furnishings.'",
      "T": "'Build it precisely according to everything I am about to show you — the design of the dwelling and the design of all its furnishings, exactly so.'"
    },
    "10": {
      "L": "'And they shall make an ark of shittim wood: two cubits and a half shall be the length thereof, and a cubit and a half the breadth thereof, and a cubit and a half the height thereof.'",
      "M": "'Have them make an ark of acacia wood — two and a half cubits long, a cubit and a half wide, and a cubit and a half high.'",
      "T": "'They shall construct a chest of acacia wood — two and a half cubits long, one and a half wide, one and a half high. This is the ark, the place where my covenant words will rest.'"
    },
    "11": {
      "L": "'And thou shalt overlay it with pure gold, within and without shalt thou overlay it, and shalt make upon it a crown of gold round about.'",
      "M": "'Overlay it with pure gold, both inside and out, and make a gold molding around it.'",
      "T": "'Overlay it entirely with pure gold — inside and out — and run a gold molding around its top edge.'"
    },
    "12": {
      "L": "'And thou shalt cast four rings of gold for it, and put them in the four corners thereof; and two rings shall be in the one side of it, and two rings in the other side of it.'",
      "M": "'Cast four gold rings for it and fasten them to its four feet, with two rings on one side and two rings on the other.'",
      "T": "'Cast four rings of gold and attach them to its four lower corners — two on each side — to receive the carrying poles.'"
    },
    "13": {
      "L": "'And thou shalt make staves of shittim wood, and overlay them with gold.'",
      "M": "'Make poles of acacia wood and overlay them with gold.'",
      "T": "'Make carrying poles of acacia wood, overlaid with gold.'"
    },
    "14": {
      "L": "'And thou shalt put the staves into the rings by the sides of the ark, that the ark may be borne with them.'",
      "M": "'Insert the poles into the rings on the sides of the ark to carry it.'",
      "T": "'Slide the poles through the rings on either side of the ark — they are how it will be carried.'"
    },
    "15": {
      "L": "'The staves shall be in the rings of the ark; they shall not be taken from it.'",
      "M": "'The poles are to remain in the rings of the ark; they are not to be removed.'",
      "T": "'The poles must stay in the rings at all times — they are never to be removed from the ark.'"
    },
    "16": {
      "L": "'And thou shalt put into the ark the testimony which I shall give thee.'",
      "M": "'Then place in the ark the tablets of the covenant law, which I will give you.'",
      "T": "'Into the ark you shall place the testimony — the tablets of the covenant — that I will give you.'"
    },
    "17": {
      "L": "'And thou shalt make a mercy seat of pure gold: two cubits and a half shall be the length thereof, and a cubit and a half the breadth thereof.'",
      "M": "'Make an atonement cover of pure gold — two and a half cubits long and a cubit and a half wide.'",
      "T": "'Fashion a cover of atonement from pure gold — two and a half cubits long, one and a half wide. This is the kapporet, the seat of my presence.'"
    },
    "18": {
      "L": "'And thou shalt make two cherubims of gold, of beaten work shalt thou make them, in the two ends of the mercy seat.'",
      "M": "'And make two cherubim out of hammered gold at the two ends of the cover.'",
      "T": "'Hammer two cherubim from gold and attach them to the two ends of the cover — one cherub at each end.'"
    },
    "19": {
      "L": "'And make one cherub on the one end, and the other cherub on the other end: even of the mercy seat shall ye make the cherubims on the two ends thereof.'",
      "M": "'Make one cherub on one end and the second cherub on the other end; make the cherubim of one piece with the cover, at the two ends.'",
      "T": "'One cherub at this end, one cherub at that end — hammered from the same piece of gold as the cover, a single seamless whole.'"
    },
    "20": {
      "L": "'And the cherubims shall stretch forth their wings on high, covering the mercy seat with their wings, and their faces shall look one to another; toward the mercy seat shall the faces of the cherubims be.'",
      "M": "'The cherubim are to have their wings spread upward, overshadowing the cover with their wings. They shall face each other, looking toward the cover.'",
      "T": "'The cherubim spread their wings upward, arching over and sheltering the cover. Their faces turn toward each other, both gazing down toward the cover of atonement — the throne of mercy.'"
    },
    "21": {
      "L": "'And thou shalt put the mercy seat above upon the ark; and in the ark thou shalt put the testimony that I shall give thee.'",
      "M": "'Place the cover on top of the ark and put in the ark the tablets of the covenant law that I will give you.'",
      "T": "'Set the cover of atonement on top of the ark, and place the covenant tablets inside it.'"
    },
    "22": {
      "L": "'And there I will meet with thee, and I will commune with thee from above the mercy seat, from between the two cherubims which are upon the ark of the testimony, of all things which I will give thee in commandment unto the children of Israel.'",
      "M": "'There, above the cover between the two cherubim that are over the ark of the covenant law, I will meet with you and give you all my commands for the Israelites.'",
      "T": "'There I will meet with you. From above the cover, from between the two cherubim that stand over the ark of the testimony, I will speak to you — giving you all that I command for the people of Israel. The ark is my address; the cover is where heaven and earth touch.'"
    },
    "23": {
      "L": "'Thou shalt also make a table of shittim wood: two cubits shall be the length thereof, and a cubit the breadth thereof, and a cubit and a half the height thereof.'",
      "M": "'Make a table of acacia wood — two cubits long, a cubit wide and a cubit and a half high.'",
      "T": "'Make a table of acacia wood — two cubits long, one cubit wide, one and a half cubits high. On it the bread of the Presence will be kept before me always.'"
    },
    "24": {
      "L": "'And thou shalt overlay it with pure gold, and make thereto a crown of gold round about.'",
      "M": "'Overlay it with pure gold and make a gold molding around it.'",
      "T": "'Overlay it with pure gold and run a gold molding around the top.'"
    },
    "25": {
      "L": "'Also thou shalt make unto it a border of an hand breadth round about, and thou shalt make a golden crown to the border thereof round about.'",
      "M": "'Also make around it a rim a handbreadth wide and put a gold molding on the rim.'",
      "T": "'Add a frame one handbreadth wide around the top edge, and put a gold molding along that frame.'"
    },
    "26": {
      "L": "'And thou shalt make for it four rings of gold, and put the rings in the four corners that are on the four feet thereof.'",
      "M": "'Make four gold rings for it and fasten them to the four corners, where the four legs are.'",
      "T": "'Cast four gold rings and fasten them at the four corners where the legs are.'"
    },
    "27": {
      "L": "'Over against the border shall the rings be for places of the staves to bear the table.'",
      "M": "'The rings are to be close to the rim to hold the poles used in carrying the table.'",
      "T": "'The rings should sit beside the frame — they receive the carrying poles.'"
    },
    "28": {
      "L": "'And thou shalt make the staves of shittim wood, and overlay them with gold, that the table may be borne with them.'",
      "M": "'Make the poles of acacia wood, overlay them with gold and carry the table with them.'",
      "T": "'Make the carrying poles of acacia wood, overlay them with gold — they will bear the table.'"
    },
    "29": {
      "L": "'And thou shalt make the dishes thereof, and spoons thereof, and covers thereof, and bowls thereof, to cover withal: of pure gold shalt thou make them.'",
      "M": "'And make its plates and dishes and its pitchers and bowls for the pouring of offerings; make them of pure gold.'",
      "T": "'Fashion its plates and dishes, its pitchers and bowls for the drink offerings — all of pure gold.'"
    },
    "30": {
      "L": "'And thou shalt set upon the table shewbread before me alway.'",
      "M": "'Put the bread of the Presence on this table to be before me at all times.'",
      "T": "'Keep the bread of the Presence on this table before me at all times — twelve loaves, one for each tribe, renewed each Sabbath. This is the table of fellowship with the Living God.'"
    },
    "31": {
      "L": "'And thou shalt make a candlestick of pure gold: of beaten work shall the candlestick be made: his shaft, and his branches, his bowls, his knops, and his flowers, shall be of the same.'",
      "M": "'Make a lampstand of pure gold. Hammer out its base and shaft, and make its floral cups, buds and blossoms of one piece with it.'",
      "T": "'Hammer a lampstand from a single piece of pure gold — base, shaft, cups shaped like almond blossoms, knobs, and petals, all of one hammered piece.'"
    },
    "32": {
      "L": "'And six branches shall come out of the sides of it; three branches of the candlestick out of the one side, and three branches of the candlestick out of the other side:'",
      "M": "'Six branches are to extend from the sides of the lampstand — three on one side and three on the other.'",
      "T": "'Six branches extend from its sides — three from each side, like a tree whose light reaches in every direction.'"
    },
    "33": {
      "L": "'Three bowls made like unto almonds, with a knop and a flower in one branch; and three bowls made like almonds in the other branch, with a knop and a flower: so in the six branches that come out of the candlestick.'",
      "M": "'Three cups shaped like almond flowers with buds and blossoms are to be on one branch, three on the next branch, and the same for all six branches extending from the lampstand.'",
      "T": "'Each branch bears three almond-blossom cups, each with bud and petal — the same design repeated on all six branches. The lampstand blooms like the almond, the first tree to wake from winter, a sign of watchful life.'"
    },
    "34": {
      "L": "'And in the candlestick shall be four bowls made like unto almonds, with their knops and their flowers.'",
      "M": "'And on the lampstand there are to be four cups shaped like almond flowers with buds and blossoms.'",
      "T": "'The central shaft bears four almond-blossom cups with buds and petals.'"
    },
    "35": {
      "L": "'And there shall be a knop under two branches of the same, and a knop under two branches of the same, and a knop under two branches of the same, according to the six branches that proceed out of the candlestick.'",
      "M": "'One bud shall be under the first pair of branches extending from the lampstand, a second bud under the second pair, and a third bud under the third pair — six branches in all.'",
      "T": "'A single knob at the base of each pair of branches supports them — one knob for each pair, all three knobs integral to the shaft.'"
    },
    "36": {
      "L": "'Their knops and their branches shall be of the same: all it shall be one beaten work of pure gold.'",
      "M": "'The buds and branches shall all be of one piece with the lampstand, the whole thing hammered from a single piece of pure gold.'",
      "T": "'Everything — knobs, branches, cups, shaft — hammered from a single talent of pure gold, seamless. No joint, no weld; one unbroken piece.'"
    },
    "37": {
      "L": "'And thou shalt make the seven lamps thereof: and they shall light the lamps thereof, that they may give light over against it.'",
      "M": "'Then make its seven lamps and set them up on it so that they light the space in front of it.'",
      "T": "'Light its seven lamps so they cast their light forward, illuminating the space before the lampstand. Seven — the number of completeness — for the light that never goes out.'"
    },
    "38": {
      "L": "'And the tongs thereof, and the snuffdishes thereof, shall be of pure gold.'",
      "M": "'Its wick trimmers and trays are to be of pure gold.'",
      "T": "'Its snuffers and trays — all of pure gold.'"
    },
    "39": {
      "L": "'Of a talent of pure gold shall he make it, with all these vessels.'",
      "M": "'It is to be made of a talent of pure gold, including all these accessories.'",
      "T": "'One full talent of pure gold for the lampstand and all its accessories — a king's weight of gold for the light that represents God's presence in the holy place.'"
    },
    "40": {
      "L": "'And look that thou make them after their pattern, which was shewed thee in the mount.'",
      "M": "'See that you make them according to the plan shown you on the mountain.'",
      "T": "'Make everything exactly according to the design you were shown on the mountain. Not your invention — God's.'"
    }
  },
  "26": {
    "1": {
      "L": "Moreover thou shalt make the tabernacle with ten curtains of fine twined linen, and blue, and purple, and scarlet: with cherubims of cunning work shalt thou make them.",
      "M": "Make the tabernacle with ten curtains of finely twisted linen and blue, purple and scarlet yarn, with cherubim woven into them by a skilled craftsman.",
      "T": "Construct the tabernacle with ten curtains — fine woven linen worked in blue, purple, and scarlet — with cherubim figures skillfully woven throughout. The heavenly guardians adorn the place where God dwells."
    },
    "2": {
      "L": "The length of one curtain shall be eight and twenty cubits, and the breadth of one curtain four cubits: and every one of the curtains shall have one measure.",
      "M": "Each curtain is to be twenty-eight cubits long and four cubits wide — all the curtains the same size.",
      "T": "Each curtain: twenty-eight cubits long, four wide — every one the same, uniformity in worship."
    },
    "3": {
      "L": "The five curtains shall be coupled together one to another; and other five curtains shall be coupled one to another.",
      "M": "Join five of the curtains together, and do the same with the other five.",
      "T": "Join five curtains into one panel; join the other five into a second panel."
    },
    "4": {
      "L": "And thou shalt make loops of blue upon the edge of the one curtain from the selvedge in the coupling; and likewise shalt thou make in the uttermost edge of another curtain, in the coupling of the second.",
      "M": "Make loops of blue yarn along the edge of the end curtain in one set, and do the same with the end curtain in the other set.",
      "T": "Sew blue loops along the outer edge of each end panel — corresponding loops that will align when the two panels are joined."
    },
    "5": {
      "L": "Fifty loops shalt thou make in the one curtain, and fifty loops shalt thou make in the edge of the curtain that is in the coupling of the second; that the loops may take hold one of another.",
      "M": "Make fifty loops on one curtain and fifty loops on the end curtain of the other set, with the loops opposite each other.",
      "T": "Fifty loops on each outer edge — fifty on the first panel's end, fifty on the second — aligned so they clasp together perfectly."
    },
    "6": {
      "L": "And thou shalt make fifty taches of gold, and couple the curtains together with the taches: and it shall be one tabernacle.",
      "M": "Then make fifty gold clasps and use them to fasten the curtains together so that the tabernacle is a unit.",
      "T": "Fifty gold clasps to join the two panels into one — the tabernacle becomes a single, seamless whole. Gold for the innermost layer, because this touches the holy of holies."
    },
    "7": {
      "L": "And thou shalt make curtains of goats' hair to be a covering upon the tabernacle: eleven curtains shalt thou make.",
      "M": "Make curtains of goat hair for the tent over the tabernacle — eleven curtains in all.",
      "T": "Over the inner linen curtains lay an outer covering of eleven goat-hair panels — the tent that shelters the dwelling."
    },
    "8": {
      "L": "The length of one curtain shall be thirty cubits, and the breadth of one curtain four cubits: and the eleven curtains shall be all of one measure.",
      "M": "Each curtain is to be thirty cubits long and four cubits wide — all eleven the same size.",
      "T": "Each panel: thirty cubits long, four wide — all eleven the same."
    },
    "9": {
      "L": "And thou shalt couple five curtains by themselves, and six curtains by themselves, and shalt double the sixth curtain in the forefront of the tabernacle.",
      "M": "Join five of the curtains together into one set and six into another. Fold the sixth curtain double at the front of the tent.",
      "T": "Join five panels into one set, six into another. Fold the sixth panel double at the entrance — this creates the extra length needed to cover the front."
    },
    "10": {
      "L": "And thou shalt make fifty loops on the edge of the one curtain that is outmost in the coupling, and fifty loops in the edge of the curtain which coupleth the second.",
      "M": "Make fifty loops along the edge of the outermost curtain in one set and fifty loops along the edge of the outermost curtain in the other set.",
      "T": "Fifty loops on the outer edge of each joined set, corresponding with each other."
    },
    "11": {
      "L": "And thou shalt make fifty taches of brass, and put the taches into the loops, and couple the tent together, that it may be one.",
      "M": "Then make fifty bronze clasps and put them through the loops to fasten the tent together as a unit.",
      "T": "Fifty bronze clasps — bronze for the outer layer, as befits what faces the world — to join the tent panels into one."
    },
    "12": {
      "L": "And the remnant that remaineth of the curtains of the tent, the half curtain that remaineth, shall hang over the backside of the tabernacle.",
      "M": "The extra length of the tent curtains — the half curtain that is left over — is to hang down at the rear of the tabernacle.",
      "T": "The remaining half panel hangs down over the back of the dwelling — nothing wasted, everything purposeful."
    },
    "13": {
      "L": "And a cubit on the one side, and a cubit on the other side of that which remaineth in the length of the curtains of the tent, it shall hang over the sides of the tabernacle on this side and on that side, to cover it.",
      "M": "The tent curtains will be a cubit longer on each side; what is left will hang down on the sides of the tabernacle to cover it.",
      "T": "One cubit of overhang on each side covers and protects the dwelling from the elements — the tent wraps it completely."
    },
    "14": {
      "L": "And thou shalt make a covering for the tent of rams' skins dyed red, and a covering above of badgers' skins.",
      "M": "Make for the tent a covering of ram skins dyed red, and over that a covering of the finest leather.",
      "T": "Over the goat-hair tent, a waterproof covering of ram skins dyed red, and over that a protective layer of fine leather. Three layers — the holy wrapped in the ordinary."
    },
    "15": {
      "L": "And thou shalt make boards for the tabernacle of shittim wood standing up.",
      "M": "Make upright frames for the tabernacle of acacia wood.",
      "T": "Construct upright frames of acacia wood to form the walls of the dwelling."
    },
    "16": {
      "L": "Ten cubits shall be the length of a board, and a cubit and a half shall be the breadth of one board.",
      "M": "Each frame is to be ten cubits long and a cubit and a half wide.",
      "T": "Each frame: ten cubits tall, one and a half wide."
    },
    "17": {
      "L": "Two tenons shall there be in one board, set in order one against another: thus shalt thou make for all the boards of the tabernacle.",
      "M": "Each frame is to have two projections set parallel to each other. Make all the frames of the tabernacle in this way.",
      "T": "Each frame has two tenons for fitting into the silver sockets — make every frame the same way."
    },
    "18": {
      "L": "And thou shalt make the boards for the tabernacle, twenty boards on the south side southward.",
      "M": "Make twenty frames for the south side of the tabernacle,",
      "T": "Twenty frames for the south wall,"
    },
    "19": {
      "L": "And thou shalt make forty sockets of silver under the twenty boards; two sockets under one board for his two tenons, and two sockets under another board for his two tenons.",
      "M": "and make forty silver bases to go under them — two bases for each frame, one under each projection.",
      "T": "with forty silver bases beneath them — two bases per frame, one socket for each tenon. The structure rests on silver — the ransom metal of the covenant."
    },
    "20": {
      "L": "And for the second side of the tabernacle on the north side there shall be twenty boards:",
      "M": "For the north side of the tabernacle, make twenty frames",
      "T": "Twenty frames for the north wall"
    },
    "21": {
      "L": "And their forty sockets of silver; two sockets under one board, and two sockets under another board.",
      "M": "with forty silver bases — two under each frame.",
      "T": "with forty silver bases, two per frame."
    },
    "22": {
      "L": "And for the sides of the tabernacle westward thou shalt make six boards.",
      "M": "Make six frames for the far end, the west side, of the tabernacle,",
      "T": "Six frames for the rear wall, the western end."
    },
    "23": {
      "L": "And two boards shalt thou make for the corners of the tabernacle in the two sides.",
      "M": "and make two frames for the corners at the far end.",
      "T": "Two additional corner frames for the rear corners."
    },
    "24": {
      "L": "And they shall be coupled together beneath, and they shall be coupled together above the head of it unto one ring: thus shall it be for them both; they shall be for the two corners.",
      "M": "At these two corners the frames are to be double from the bottom all the way to the top, fitted into a single ring; both corners are to be made this way.",
      "T": "These corner frames are joined from base to top into a single ring — braced for strength, double thickness where the walls meet."
    },
    "25": {
      "L": "And they shall be eight boards, and their sockets of silver, sixteen sockets; two sockets under one board, and two sockets under another board.",
      "M": "So there will be eight frames and sixteen silver bases, two under each frame.",
      "T": "Eight frames total for the rear wall, sixteen silver bases — two per frame."
    },
    "26": {
      "L": "And thou shalt make bars of shittim wood; five for the boards of the one side of the tabernacle,",
      "M": "Also make crossbars of acacia wood: five for the frames on one side of the tabernacle,",
      "T": "Make five horizontal crossbars of acacia wood for each side wall"
    },
    "27": {
      "L": "And five bars for the boards of the other side of the tabernacle, and five bars for the boards of the side of the tabernacle, for the two sides westward.",
      "M": "five for the frames on the other side, and five for the frames on the west end.",
      "T": "and five for the other side wall, and five for the rear — fifteen bars in all to hold the structure rigid."
    },
    "28": {
      "L": "And the middle bar in the midst of the boards shall reach from end to end.",
      "M": "The middle crossbar is to extend from end to end at the middle of the frames.",
      "T": "The central crossbar runs the full length of each wall through the middle of the frames — the spine of the dwelling."
    },
    "29": {
      "L": "And thou shalt overlay the boards with gold, and make their rings of gold for places for the bars; and thou shalt overlay the bars with gold.",
      "M": "Overlay the frames with gold and make gold rings to hold the crossbars. Also overlay the crossbars with gold.",
      "T": "Overlay the frames with gold; make gold rings to hold the bars; overlay the bars themselves with gold — even the structure is pure gold beneath the curtains."
    },
    "30": {
      "L": "And thou shalt rear up the tabernacle according to the fashion thereof which was shewed thee in the mount.",
      "M": "Set up the tabernacle according to the plan shown you on the mountain.",
      "T": "Erect the tabernacle exactly as it was shown to you on the mountain — divine architecture, not human invention."
    },
    "31": {
      "L": "And thou shalt make a vail of blue, and purple, and scarlet, and fine twined linen: with cherubims shall it be made of cunning work.",
      "M": "Make a curtain of blue, purple and scarlet yarn and finely twisted linen, with cherubim woven into it by a skilled craftsman.",
      "T": "Weave a veil of blue, purple, and scarlet — fine linen with cherubim woven in by a master craftsman. This veil divides the habitable from the inviolable, the holy from the most holy."
    },
    "32": {
      "L": "And thou shalt hang it upon four pillars of shittim wood overlaid with gold: their hooks shall be of gold, upon the four sockets of silver.",
      "M": "Hang it with gold hooks on four posts of acacia wood overlaid with gold and standing on four silver bases.",
      "T": "Hang it on four acacia posts overlaid with gold, with gold hooks, set in four silver bases — the veil suspended between heaven's claim and human access."
    },
    "33": {
      "L": "And thou shalt hang up the vail under the taches, that thou mayest bring in thither within the vail the ark of the testimony: and the vail shall divide unto you between the holy place and the most holy.",
      "M": "Hang the curtain from the clasps and place the ark of the covenant law behind the curtain. The curtain will separate the holy place from the most holy place.",
      "T": "Hang the veil below the clasps and bring the ark of the testimony through it into the inner chamber. The veil divides the holy place from the most holy place — the graduated approach to the Holy One."
    },
    "34": {
      "L": "And thou shalt put the mercy seat upon the ark of the testimony in the most holy place.",
      "M": "Put the atonement cover on the ark of the covenant law in the most holy place.",
      "T": "Set the cover of atonement on the ark of the testimony in the most holy place — the innermost point of the entire universe, where God's presence rests."
    },
    "35": {
      "L": "And thou shalt set the table without the vail, and the candlestick over against the table on the side of the tabernacle toward the south: and thou shalt put the table on the north side.",
      "M": "Place the table outside the curtain on the north side of the tabernacle and put the lampstand opposite it on the south side.",
      "T": "Outside the veil: the table on the north, the lampstand on the south, facing each other — bread and light, sustenance and illumination, in the holy place."
    },
    "36": {
      "L": "And thou shalt make an hanging for the door of the tent, of blue, and purple, and scarlet, and fine twined linen, wrought with needlework.",
      "M": "For the entrance to the tent make a curtain of blue, purple and scarlet yarn and finely twisted linen — the work of an embroiderer.",
      "T": "For the tent entrance, weave a screen of blue, purple, scarlet, and fine linen — needle-worked, beautiful, welcoming and yet marking the threshold of the sacred."
    },
    "37": {
      "L": "And thou shalt make for the hanging five pillars of shittim wood, and overlay them with gold, and their hooks shall be of gold: and thou shalt cast five sockets of brass for them.",
      "M": "Make five posts of acacia wood for the curtain and overlay them with gold. Hang gold hooks on them and cast five bronze bases for them.",
      "T": "Five acacia posts overlaid with gold, gold hooks, bronze bases — the entrance frame. Bronze for the world-facing threshold, gold for what belongs to God."
    }
  },
  "27": {
    "1": {
      "L": "And thou shalt make an altar of shittim wood, five cubits long, and five cubits broad; the altar shall be foursquare: and the height thereof shall be three cubits.",
      "M": "Build an altar of acacia wood, five cubits long and five cubits wide — the altar is to be square — and three cubits high.",
      "T": "Build an altar of acacia wood — five cubits square and three cubits high. At this altar, the gifts of the people rise to God in smoke."
    },
    "2": {
      "L": "And thou shalt make the horns of it upon the four corners thereof: his horns shall be of the same: and thou shalt overlay it with brass.",
      "M": "Make a horn at each of the four corners, so that the horns and the altar are of one piece, and overlay the altar with bronze.",
      "T": "Fashion a horn at each corner, projecting upward, of one piece with the altar — these are where the blood of atonement is applied. Overlay the whole with bronze."
    },
    "3": {
      "L": "And thou shalt make his pans to receive his ashes, and his shovels, and his basons, and his fleshhooks, and his firepans: all the vessels thereof thou shalt make of brass.",
      "M": "Make all its utensils of bronze — its pots to remove the ashes, and its shovels, sprinkling bowls, meat forks and firepans.",
      "T": "Ash buckets, shovels, sprinkling bowls, flesh forks, fire pans — every utensil of bronze. Every tool of worship has its proper form."
    },
    "4": {
      "L": "And thou shalt make for it a grate of network of brass; and upon the net shalt thou make four brasen rings in the four corners thereof.",
      "M": "Make a bronze grating, a network for it, and make four bronze rings at the four corners of the network.",
      "T": "Make a bronze grating — a lattice of metalwork — and attach four bronze rings at its four corners."
    },
    "5": {
      "L": "And thou shalt put it under the compass of the altar beneath, that the net may be even to the midst of the altar.",
      "M": "Put it under the ledge of the altar so that it is halfway up the altar.",
      "T": "Set the grating halfway up the altar, just below the rim — so the coals have air and the fire burns fully."
    },
    "6": {
      "L": "And thou shalt make staves for the altar, staves of shittim wood, and overlay them with brass.",
      "M": "Make poles of acacia wood for the altar and overlay them with bronze.",
      "T": "Make carrying poles of acacia wood, overlaid with bronze."
    },
    "7": {
      "L": "And the staves shall be put into the rings, and the staves shall be upon the two sides of the altar, to bear it.",
      "M": "The poles are to be inserted into the rings so they are on two sides of the altar when it is carried.",
      "T": "The poles slide through the rings on either side — the altar travels with Israel; worship is not bound to one geography."
    },
    "8": {
      "L": "Hollow with boards shalt thou make it: as it was shewed thee in the mount, so shall they make it.",
      "M": "Make the altar hollow, out of boards. It is to be made just as shown you on the mountain.",
      "T": "Make it hollow — a wooden frame. Build it exactly as the vision showed you on the mountain."
    },
    "9": {
      "L": "And thou shalt make the court of the tabernacle: for the south side southward there shall be hangings for the court of fine twined linen of an hundred cubits long for one side:",
      "M": "Make a courtyard for the tabernacle. The south side shall have curtains of finely twisted linen, a hundred cubits long,",
      "T": "Now make a courtyard around the tabernacle. The south wall: one hundred cubits of fine linen curtaining —"
    },
    "10": {
      "L": "And the twenty pillars thereof and their twenty sockets shall be of brass; the hooks of the pillars and their fillets shall be of silver.",
      "M": "with twenty posts and twenty bronze bases and with silver hooks and bands on the posts.",
      "T": "twenty bronze-socketed posts, silver hooks and bands. Bronze at the base where it meets the earth; silver above, gleaming in the sun."
    },
    "11": {
      "L": "And likewise for the north side in length there shall be hangings of an hundred cubits long, and his twenty pillars and their twenty sockets of brass; the hooks of the pillars and their fillets of silver.",
      "M": "The north side shall also be a hundred cubits long with twenty posts and twenty bronze bases and with silver hooks and bands on the posts.",
      "T": "The north wall mirrors the south: one hundred cubits, twenty posts, bronze bases, silver hooks and bands."
    },
    "12": {
      "L": "And for the breadth of the court on the west side shall be hangings of fifty cubits: their pillars ten, and their sockets ten.",
      "M": "The west end of the courtyard shall be fifty cubits wide and have ten posts and ten bases.",
      "T": "The western end: fifty cubits of curtain, ten posts, ten bases."
    },
    "13": {
      "L": "And the breadth of the court on the east side eastward shall be fifty cubits.",
      "M": "The east end, toward the sunrise, shall also be fifty cubits wide.",
      "T": "The eastern end — the entrance side, facing the sunrise — is also fifty cubits wide."
    },
    "14": {
      "L": "The hangings of one side of the gate shall be fifteen cubits: their pillars three, and their sockets three.",
      "M": "Curtains fifteen cubits long are to be on one side of the entrance, with three posts and three bases,",
      "T": "Fifteen cubits of curtaining on one side of the gate — three posts, three bases —"
    },
    "15": {
      "L": "And on the other side shall be hangings fifteen cubits: their pillars three, and their sockets three.",
      "M": "and curtains fifteen cubits long are to be on the other side, with three posts and three bases.",
      "T": "and fifteen cubits on the other side — three posts, three bases. Twenty cubits remain for the gate itself."
    },
    "16": {
      "L": "And for the gate of the court shall be an hanging of twenty cubits, of blue, and purple, and scarlet, and fine twined linen, wrought with needlework: and their pillars shall be four, and their sockets four.",
      "M": "For the entrance to the courtyard, provide a curtain twenty cubits long, of blue, purple and scarlet yarn and finely twisted linen — the work of an embroiderer — with four posts and four bases.",
      "T": "The gateway screen is twenty cubits wide — woven in blue, purple, scarlet, and fine linen by a skilled embroiderer. Four posts, four bases. Even the entrance to the courtyard is beautiful, because those who draw near to God come through a place worthy of God."
    },
    "17": {
      "L": "All the pillars round about the court shall be filleted with silver; their hooks shall be of silver, and their sockets of brass.",
      "M": "All the posts around the courtyard are to have silver bands and hooks, and bronze bases.",
      "T": "Every post around the entire courtyard: silver bands and silver hooks, bronze bases — uniform, consistent, no diminishing of honor as you move away from the center."
    },
    "18": {
      "L": "The length of the court shall be an hundred cubits, and the breadth fifty every where, and the height five cubits of fine twined linen, and their sockets of brass.",
      "M": "The courtyard shall be a hundred cubits long and fifty cubits wide, with curtains of finely twisted linen five cubits high, and with bronze bases.",
      "T": "The courtyard in full: one hundred cubits long, fifty wide, five cubits high — fine linen walls enclosing the sacred space. Bronze foundations."
    },
    "19": {
      "L": "All the vessels of the tabernacle in all the service thereof, and all the pins thereof, and all the pins of the court, shall be of brass.",
      "M": "All the other articles used in the tabernacle, whatever their function, including all the tent pegs for it and those for the courtyard, are to be of bronze.",
      "T": "Every peg, every stake, every tool of service for the tabernacle and courtyard — bronze. The practical equipment of worship is not beneath God's specifications."
    },
    "20": {
      "L": "And thou shalt command the children of Israel, that they bring thee pure oil olive beaten for the light, to cause the lamp to burn always.",
      "M": "Command the Israelites to bring you clear oil of pressed olives for the light so that the lamps may be kept burning.",
      "T": "Command the people of Israel to bring you pure pressed olive oil for the lamp — so the light in the holy place burns without ceasing. The lamp is never to go out; God's presence is always illuminated."
    },
    "21": {
      "L": "In the tabernacle of the congregation, without the vail which is before the testimony, Aaron and his sons shall order it from evening to morning before the LORD: it shall be a statute for ever unto their generations on the behalf of the children of Israel.",
      "M": "In the tent of meeting, outside the curtain that shields the ark of the covenant law, Aaron and his sons are to tend the lamps before the LORD from evening till morning. This is to be a lasting ordinance among the Israelites for the generations to come.",
      "T": "In the tent of meeting, outside the veil before the ark of the testimony, Aaron and his sons maintain the light — from evening to morning, before the LORD. A perpetual statute for all generations of Israel. The priests are custodians of the light; they keep watch through the night so God's presence is never without its witness."
    }
  },
  "28": {
    "1": {
      "L": "And take thou unto thee Aaron thy brother, and his sons with him, from among the children of Israel, that he may minister unto me in the priest's office, even Aaron, Nadab and Abihu, Eleazar and Ithamar, Aaron's sons.",
      "M": "Have Aaron your brother brought to you from among the Israelites, along with his sons Nadab and Abihu, Eleazar and Ithamar, so they may serve me as priests.",
      "T": "Bring Aaron your brother and his sons — Nadab, Abihu, Eleazar, and Ithamar — out from among the Israelites to serve me as priests. From the whole nation, these are set apart."
    },
    "2": {
      "L": "And thou shalt make holy garments for Aaron thy brother for glory and for beauty.",
      "M": "Make sacred garments for your brother Aaron to give him dignity and honor.",
      "T": "Make sacred garments for Aaron your brother — garments that speak of dignity and beauty. The priest who stands before God must be clothed in a way that honors God."
    },
    "3": {
      "L": "And thou shalt speak unto all that are wise hearted, whom I have filled with the spirit of wisdom, that they may make Aaron's garments to consecrate him, that he may minister unto me in the priest's office.",
      "M": "Tell all the skilled workers to whom I have given wisdom in such matters that they are to make garments for Aaron, for his consecration, so he may serve me as priest.",
      "T": "Speak to every craftsman whose heart I have filled with skill — commission them to make Aaron's garments for his ordination, so he may minister as my priest. The gift of skill is from God; it is put to its highest use in service to God."
    },
    "4": {
      "L": "And these are the garments which they shall make; a breastplate, and an ephod, and a robe, and a broidered coat, a mitre, and a girdle: and they shall make holy garments for Aaron thy brother, and his sons, that he may minister unto me in the priest's office.",
      "M": "These are the garments they are to make: a breastpiece, an ephod, a robe, a woven tunic, a turban and a sash. They are to make these sacred garments for your brother Aaron and his sons, so they may serve me as priests.",
      "T": "The garments to be made: a breastpiece, an ephod, a robe, an embroidered tunic, a turban, and a sash. Make these sacred garments for Aaron and his sons, so they may minister as my priests."
    },
    "5": {
      "L": "And they shall take gold, and blue, and purple, and scarlet, and fine linen.",
      "M": "Have them use gold, and blue, purple and scarlet yarn, and fine linen.",
      "T": "The materials: gold thread, blue, purple, and scarlet yarn, and fine linen — the same elements that mark God's dwelling throughout."
    },
    "6": {
      "L": "And they shall make the ephod of gold, of blue, and of purple, of scarlet, and fine twined linen, with cunning work.",
      "M": "Make the ephod of gold, and of blue, purple and scarlet yarn, and of finely twisted linen — the work of a skilled craftsman.",
      "T": "Craft the ephod from gold thread and blue, purple, and scarlet yarn woven into fine linen — the highest craft for the highest garment."
    },
    "7": {
      "L": "It shall have the two shoulderpieces thereof joined at the two edges thereof; and so it shall be joined together.",
      "M": "It is to have two shoulder pieces attached to two of its corners, so it can be fastened.",
      "T": "Two shoulder pieces join the front and back at the top, fastening the ephod securely to Aaron's shoulders."
    },
    "8": {
      "L": "And the curious girdle of the ephod, which is upon it, shall be of the same, according to the work thereof; even of gold, of blue, and purple, and scarlet, and fine twined linen.",
      "M": "Its skillfully woven waistband is to be like it — of one piece with the ephod and made with gold, and with blue, purple and scarlet yarn, and with finely twisted linen.",
      "T": "The waistband of the ephod is woven from the same materials — gold, blue, purple, scarlet, fine linen — and is one piece with the ephod, not a separate addition."
    },
    "9": {
      "L": "And thou shalt take two onyx stones, and grave on them the names of the children of Israel:",
      "M": "Take two onyx stones and engrave on them the names of the sons of Israel",
      "T": "Take two onyx stones and engrave on them the names of the twelve sons of Israel —"
    },
    "10": {
      "L": "Six of their names on one stone, and the other six names of the rest on the other stone, according to their birth.",
      "M": "six names on one stone and the remaining six on the other, in the order of their birth.",
      "T": "six names on one stone, six on the other, in birth order. Israel's sons are named on the high priest's shoulders: he carries the nation before God."
    },
    "11": {
      "L": "With the work of an engraver in stone, like the engravings of a signet, shalt thou engrave the two stones with the names of the children of Israel: thou shalt make them to be set in ouches of gold.",
      "M": "Engrave the names of the sons of Israel on the two stones the way a gem cutter engraves a seal. Then mount the stones in gold filigree settings.",
      "T": "Engrave the stones like a master gem cutter engraves a seal — permanent, precise — and set them in gold filigree work."
    },
    "12": {
      "L": "And thou shalt put the two stones upon the shoulders of the ephod for stones of memorial unto the children of Israel: and Aaron shall bear their names before the LORD upon his two shoulders for a memorial.",
      "M": "Fasten the two stones on the shoulder pieces of the ephod as memorial stones for the sons of Israel. Aaron is to bear the names on his shoulders as a memorial before the LORD.",
      "T": "Set the two stones on the shoulder pieces of the ephod — memorial stones for the sons of Israel. When Aaron stands before the LORD, he carries the nation's name on his shoulders. The priest is the bearer of his people."
    },
    "13": {
      "L": "And thou shalt make ouches of gold;",
      "M": "Make gold filigree settings",
      "T": "Fashion gold filigree settings"
    },
    "14": {
      "L": "And two chains of pure gold at the ends; of wreathen work shalt thou make them, and fasten the wreathen chains to the ouches.",
      "M": "and two braided chains of pure gold, like a rope, and attach the chains to the settings.",
      "T": "and two braided gold chains — twisted like rope — attached to the filigree settings. These will connect the shoulder stones to the breastpiece."
    },
    "15": {
      "L": "And thou shalt make the breastplate of judgment with cunning work; after the work of the ephod thou shalt make it; of gold, of blue, and of purple, and of scarlet, and of fine twined linen, shalt thou make it.",
      "M": "Fashion a breastpiece for making decisions — the work of a skilled craftsman. Make it like the ephod: of gold, and of blue, purple and scarlet yarn, and of finely twisted linen.",
      "T": "Make the sacred breastpiece — the breastpiece of judgment, for discerning God's will — crafted with the same skill and the same materials as the ephod: gold, blue, purple, scarlet, fine linen."
    },
    "16": {
      "L": "Foursquare it shall be being doubled; a span shall be the length thereof, and a span shall be the breadth thereof.",
      "M": "It is to be square — a span long and a span wide — and folded double.",
      "T": "It shall be square and folded double — one span each way — forming a pouch."
    },
    "17": {
      "L": "And thou shalt set in it settings of stones, even four rows of stones: the first row shall be a sardius, a topaz, and a carbuncle: this shall be the first row.",
      "M": "Then mount four rows of precious stones on it. The first row shall be carnelian, chrysolite and beryl;",
      "T": "Set four rows of stones in it. First row: carnelian, chrysolite, emerald —"
    },
    "18": {
      "L": "And the second row shall be an emerald, a sapphire, and a diamond.",
      "M": "the second row shall be turquoise, lapis lazuli and moonstone;",
      "T": "second row: turquoise, lapis lazuli, moonstone —"
    },
    "19": {
      "L": "And the third row a ligure, an agate, and an amethyst.",
      "M": "the third row shall be jacinth, agate and amethyst;",
      "T": "third row: jacinth, agate, amethyst —"
    },
    "20": {
      "L": "And the fourth row a beryl, and an onyx, and a jasper: they shall be set in gold in their inclosings.",
      "M": "the fourth row shall be chrysolite, onyx and jasper. Mount them in gold filigree settings.",
      "T": "fourth row: chrysolite, onyx, jasper — all set in gold. Twelve stones for twelve tribes."
    },
    "21": {
      "L": "And the stones shall be with the names of the children of Israel, twelve, according to their names, like the engravings of a signet; every one with his name shall they be according to the twelve tribes.",
      "M": "There are to be twelve stones, one for each of the names of the sons of Israel, each engraved like a seal with the name of one of the twelve tribes.",
      "T": "Twelve stones, one for each tribe — each engraved with a name like a royal seal. Israel's identity is literally written on the heart of the high priest."
    },
    "22": {
      "L": "And thou shalt make upon the breastplate chains at the ends of wreathen work of pure gold.",
      "M": "For the breastpiece make braided chains of pure gold, like a rope.",
      "T": "Attach twisted gold chains — braided like rope — at the top corners of the breastpiece."
    },
    "23": {
      "L": "And thou shalt make upon the breastplate two rings of gold, and shalt put the two rings on the two ends of the breastplate.",
      "M": "Make two gold rings for it and attach the two rings to two corners of the breastpiece.",
      "T": "Two gold rings at the upper corners of the breastpiece —"
    },
    "24": {
      "L": "And thou shalt put the two wreathen chains of gold in the two rings which are on the ends of the breastplate.",
      "M": "Fasten the two gold chains to the two rings at the corners of the breastpiece,",
      "T": "thread the two braided gold chains through these rings,"
    },
    "25": {
      "L": "And the other two ends of the two wreathen chains thou shalt fasten in the two ouches, and put them on the shoulderpieces of the ephod before it.",
      "M": "and the other ends of the chains to the two settings, attaching them to the shoulder pieces of the ephod at the front.",
      "T": "and attach the other ends to the filigree settings on the ephod's shoulder pieces — at the front. The breastpiece hangs from the ephod; the names of the tribes hang over Aaron's heart."
    },
    "26": {
      "L": "And thou shalt make two rings of gold, and thou shalt put them upon the two ends of the breastplate in the border thereof, which is in the side of the ephod inward.",
      "M": "Make two more gold rings and attach them to the other two corners of the breastpiece on the inside edge next to the ephod.",
      "T": "Make two more gold rings for the lower inner corners of the breastpiece — the corners that face the ephod."
    },
    "27": {
      "L": "And two other rings of gold thou shalt make, and shalt put them on the two sides of the ephod underneath, toward the forepart thereof, over against the other coupling thereof, above the curious girdle of the ephod.",
      "M": "Make two more gold rings and attach them to the bottom of the shoulder pieces on the front of the ephod, close to the seam just above the waistband of the ephod.",
      "T": "And two more gold rings on the lower front of the ephod's shoulder pieces, just above the waistband — these anchor the breastpiece at the bottom."
    },
    "28": {
      "L": "And they shall bind the breastplate by the rings thereof unto the rings of the ephod with a lace of blue, that it may be above the curious girdle of the ephod, and that the breastplate be not loosed from the ephod.",
      "M": "The rings of the breastpiece are to be tied to the rings of the ephod with blue cord, connecting it to the waistband, so that the breastpiece will not swing out from the ephod.",
      "T": "Tie the breastpiece's lower rings to the ephod's rings with blue cord, keeping the breastpiece snug above the waistband — so it never slips loose. The sacred garments form a unified whole."
    },
    "29": {
      "L": "And Aaron shall bear the names of the children of Israel in the breastplate of judgment upon his heart, when he goeth in unto the holy place, for a memorial before the LORD continually.",
      "M": "Whenever Aaron enters the holy place, he will bear the names of the sons of Israel over his heart on the breastpiece of judgment as a continuing memorial before the LORD.",
      "T": "Every time Aaron enters the holy place, he carries Israel's twelve names over his heart. He is their representative before God — bearing them into the divine presence that ordinary Israelites cannot enter. A memorial, a pleading, a perpetual act of intercession."
    },
    "30": {
      "L": "And thou shalt put in the breastplate of judgment the Urim and the Thummim; and they shall be upon Aaron's heart, when he goeth in before the LORD: and Aaron shall bear the judgment of the children of Israel upon his heart before the LORD continually.",
      "M": "Also put the Urim and the Thummim in the breastpiece, so they may be over Aaron's heart whenever he enters the presence of the LORD. Thus Aaron will always bear the means of making decisions for the Israelites over his heart before the LORD.",
      "T": "Place the Urim and Thummim inside the breastpiece — the sacred lots by which God's will is discerned. They rest over Aaron's heart when he stands before the LORD. He does not guess; he does not speculate: he inquires of God, and God answers. The high priest carries Israel's judgment into the very presence of the Judge."
    },
    "31": {
      "L": "And thou shalt make the robe of the ephod all of blue.",
      "M": "Make the robe of the ephod entirely of blue cloth.",
      "T": "Make the robe worn under the ephod entirely of blue — the color of heaven, worn next to the priest's body."
    },
    "32": {
      "L": "And there shall be an hole in the top of it, in the midst thereof: it shall have a binding of woven work round about the hole of it, as it were the hole of an habergeon, that it be not rent.",
      "M": "There shall be a woven opening for the head in its center, with a woven collar around the opening, like the collar of body armor, so it will not tear.",
      "T": "The neck opening must have a woven reinforced edge — like the collar of a battle garment — so the robe does not tear. The high priest's garments are never to be damaged. Aaron's predecessor-desecration is the warning: garments torn in the holy place call down death."
    },
    "33": {
      "L": "And beneath upon the hem of it thou shalt make pomegranates of blue, and of purple, and of scarlet, round about the hem thereof; and bells of gold between them round about:",
      "M": "Make pomegranates of blue, purple and scarlet yarn around the hem of the robe, with gold bells between them.",
      "T": "Around the hem of the robe: pomegranates of blue, purple, and scarlet alternating with gold bells — pomegranate, bell, pomegranate, bell, all the way around."
    },
    "34": {
      "L": "A golden bell and a pomegranate, a golden bell and a pomegranate, upon the hem of the robe round about.",
      "M": "The alternating gold bells and pomegranates are to be around the hem of the robe.",
      "T": "The pomegranates represent fruitfulness and the fullness of the law; the bells announce the priest's movement. Everyone outside must know when Aaron is moving through the holy place, lest anyone enter unexpectedly into the zone of holiness and die."
    },
    "35": {
      "L": "And it shall be upon Aaron to minister: and his sound shall be heard when he goeth in unto the holy place before the LORD, and when he cometh out, that he die not.",
      "M": "Aaron must wear it when he ministers. The sound of the bells will be heard when he enters the holy place before the LORD and when he comes out, so that he will not die.",
      "T": "Aaron wears this robe whenever he ministers. The sound of the bells is heard as he enters the holy place before the LORD and as he leaves — so that he will not die. The sound signals his continued life; silence would mean catastrophe."
    },
    "36": {
      "L": "And thou shalt make a plate of pure gold, and grave upon it, like the engravings of a signet, HOLINESS TO THE LORD.",
      "M": "Make a plate of pure gold and engrave on it as you would engrave a seal: HOLY TO THE LORD.",
      "T": "Engrave a medallion of pure gold with the words: HOLY TO THE LORD — cut deep as a royal seal. This is the crown of the high priest's identity: not his own name, but a declaration of whose he is."
    },
    "37": {
      "L": "And thou shalt put it on a blue lace, that it may be upon the mitre; upon the forefront of the mitre it shall be.",
      "M": "Fasten a blue cord to it to attach it to the turban; it is to be on the front of the turban.",
      "T": "Attach it to the turban with a blue cord, worn on the front of the turban — the first thing anyone sees when the high priest faces them."
    },
    "38": {
      "L": "And it shall be upon Aaron's forehead, that Aaron may bear the iniquity of the holy things, which the children of Israel shall hallow in all their holy gifts; and it shall be always upon his forehead, that they may be accepted before the LORD.",
      "M": "It will be on Aaron's forehead, and he will bear the guilt involved in the sacred gifts the Israelites consecrate, whatever their gifts may be. It will be on Aaron's forehead continually so that they will be acceptable to the LORD.",
      "T": "It rests on Aaron's forehead — and through it, Aaron absorbs whatever fault or impurity taints the sacred offerings of Israel. Their gifts come before God imperfect; the high priest bears the discrepancy on his forehead. It is always there so that Israel's offerings are always accepted. The priest takes on what would otherwise disqualify."
    },
    "39": {
      "L": "And thou shalt embroider the coat of fine linen, and thou shalt make the mitre of fine linen, and thou shalt make the girdle of needlework.",
      "M": "Weave the tunic of fine linen and make the turban of fine linen. The sash is to be the work of an embroiderer.",
      "T": "Weave the tunic of fine linen; fashion the turban of fine linen; embroider the sash — each piece given the craft it deserves."
    },
    "40": {
      "L": "And for Aaron's sons thou shalt make coats, and thou shalt make for them girdles, and bonnets shalt thou make for them, for glory and for beauty.",
      "M": "Make tunics, sashes and caps for Aaron's sons to give them dignity and honor.",
      "T": "For Aaron's sons: tunics, sashes, and caps — made for dignity and beauty. Even the lesser priests wear garments worthy of their calling."
    },
    "41": {
      "L": "And thou shalt put them upon Aaron thy brother, and his sons with him; and shalt anoint them, and consecrate them, and sanctify them, that they may minister unto me in the priest's office.",
      "M": "After you put these clothes on your brother Aaron and his sons, anoint and ordain them. Consecrate them so they may serve me as priests.",
      "T": "Dress Aaron and his sons, anoint them, fill their hands with offerings, and sanctify them — so they may serve as my priests. Clothing alone does not make the priest; the anointing sets them apart."
    },
    "42": {
      "L": "And thou shalt make them linen breeches to cover their nakedness; from the loins even unto the thighs they shall reach:",
      "M": "Make linen undergarments as a covering for the body, reaching from the waist to the thigh.",
      "T": "Make linen undergarments covering from the waist to the thigh — modesty before God is not optional."
    },
    "43": {
      "L": "And they shall be upon Aaron, and upon his sons, when they come in unto the tabernacle of the congregation, or when they come near unto the altar to minister in the holy place; that they bear not iniquity, and die: it shall be a statute for ever unto him and his seed after him.",
      "M": "Aaron and his sons must wear them whenever they enter the tent of meeting or approach the altar to minister in the holy place, so that they will not incur guilt and die. This is to be a lasting ordinance for Aaron and his descendants.",
      "T": "Aaron and his sons must wear them whenever they enter the tent of meeting or approach the altar — so they do not incur guilt and die. A permanent statute for Aaron and all his descendants: the holy place requires full priestly dress. To enter improperly is to die."
    }
  },
  "29": {
    "1": {
      "L": "And this is the thing that thou shalt do unto them to hallow them, to minister unto me in the priest's office: Take one young bullock, and two rams without blemish,",
      "M": "This is what you are to do to consecrate them, so they may serve me as priests: Take a young bull and two rams without defect.",
      "T": "This is the ordination ceremony — how you will set them apart to minister as my priests: bring a young bull and two rams, each without defect."
    },
    "2": {
      "L": "And unleavened bread, and cakes unleavened tempered with oil, and wafers unleavened anointed with oil: of wheaten flour shalt thou make them.",
      "M": "And from the finest wheat flour, without yeast, make bread, and make thick loaves mixed with oil, and thin loaves brushed with oil.",
      "T": "From the finest wheat flour make unleavened bread: plain loaves, loaves mixed with oil, and thin wafers brushed with oil — no leaven, for this is consecration, not ordinary food."
    },
    "3": {
      "L": "And thou shalt put them into one basket, and bring them in the basket, with the bullock and the two rams.",
      "M": "Put them in a basket and present them along with the bull and the two rams.",
      "T": "Place all the bread in a basket and bring it, along with the bull and the two rams, to the tent entrance."
    },
    "4": {
      "L": "And Aaron and his sons thou shalt bring unto the door of the tabernacle of the congregation, and shalt wash them with water.",
      "M": "Bring Aaron and his sons to the entrance to the tent of meeting and wash them with water.",
      "T": "Bring Aaron and his sons to the entrance of the tent of meeting and wash them with water. Ordination begins with cleansing — the priest approaches God washed."
    },
    "5": {
      "L": "And thou shalt take the garments, and put upon Aaron the coat, and the robe of the ephod, and the ephod, and the breastplate, and gird him with the curious girdle of the ephod:",
      "M": "Take the garments and dress Aaron with the tunic, the robe of the ephod, the ephod itself and the breastpiece. Fasten the ephod on him by its skillfully woven waistband.",
      "T": "Dress Aaron: first the tunic, then the robe of the ephod, then the ephod itself, and the breastpiece — and fasten the ephod's waistband around him. Layer by layer, he becomes the high priest."
    },
    "6": {
      "L": "And thou shalt put the mitre upon his head, and put the holy crown upon the mitre.",
      "M": "Put the turban on his head and attach the sacred emblem to the turban.",
      "T": "Place the turban on his head and affix the sacred medallion — HOLY TO THE LORD — to the front of the turban. The last thing put on is the first thing seen."
    },
    "7": {
      "L": "Then shalt thou take the anointing oil, and pour it upon his head, and anoint him.",
      "M": "Take the anointing oil and anoint him by pouring it on his head.",
      "T": "Pour the sacred anointing oil on his head — the anointing makes him the Anointed One, the Meshiach, the one set apart by God's own authority."
    },
    "8": {
      "L": "And thou shalt bring his sons, and put coats upon them.",
      "M": "Bring his sons and dress them in tunics",
      "T": "Now bring Aaron's sons and dress them in their tunics"
    },
    "9": {
      "L": "And thou shalt gird them with girdles, Aaron and his sons, and put the bonnets on them: and the priest's office shall be theirs for a perpetual statute: and thou shalt consecrate Aaron and his sons.",
      "M": "and put caps on them. Then tie sashes on Aaron and his sons. The priesthood is theirs by a lasting ordinance. In this way you shall ordain Aaron and his sons.",
      "T": "and tie sashes on them and set caps on their heads. The priesthood belongs to them by perpetual statute — it is their inheritance from God, not an achievement. Consecrate Aaron and his sons."
    },
    "10": {
      "L": "And thou shalt cause a bullock to be brought before the tabernacle of the congregation: and Aaron and his sons shall put their hands upon the head of the bullock.",
      "M": "Bring the bull to the front of the tent of meeting, and Aaron and his sons shall lay their hands on its head.",
      "T": "Bring the bull before the tent of meeting. Aaron and his sons lay their hands on its head — the gesture of identification, of transferring guilt. The animal stands in for the people."
    },
    "11": {
      "L": "And thou shalt kill the bullock before the LORD, by the door of the tabernacle of the congregation.",
      "M": "Slaughter it in the LORD's presence at the entrance to the tent of meeting.",
      "T": "Slaughter the bull before the LORD at the tent entrance. Life given so that others may draw near."
    },
    "12": {
      "L": "And thou shalt take of the blood of the bullock, and put it upon the horns of the altar with thy finger, and pour all the blood beside the bottom of the altar.",
      "M": "Take some of the bull's blood and put it on the horns of the altar with your finger, and pour out the rest of the blood at the base of the altar.",
      "T": "With your finger, apply blood to the horns of the altar — the four points of contact between sacrifice and God. Pour the remaining blood at the base of the altar. The altar is purged, made ready for holy use."
    },
    "13": {
      "L": "And thou shalt take all the fat that covereth the inwards, and the caul that is above the liver, and the two kidneys, and the fat that is upon them, and burn them upon the altar.",
      "M": "Take all the fat around the internal organs, the long lobe of the liver, and both kidneys with the fat on them, and burn them on the altar.",
      "T": "Take the fat that covers the entrails, the liver's lobe, and the two kidneys with their surrounding fat — and burn it all on the altar. These are the richest parts, the best given to God."
    },
    "14": {
      "L": "But the flesh of the bullock, and his skin, and his dung, shalt thou burn with fire without the camp: it is a sin offering.",
      "M": "But burn the bull's flesh and its hide and its intestines outside the camp. It is a sin offering.",
      "T": "The flesh, hide, and offal of the bull are burned outside the camp — because this is a purification offering. What bears the impurity does not come to the altar; it is removed far from the holy place."
    },
    "15": {
      "L": "Thou shalt also take one ram; and Aaron and his sons shall put their hands upon the head of the ram.",
      "M": "Take one of the rams, and Aaron and his sons shall lay their hands on its head.",
      "T": "Now take the first ram. Aaron and his sons lay their hands on its head."
    },
    "16": {
      "L": "And thou shalt slay the ram, and thou shalt take his blood, and sprinkle it round about upon the altar.",
      "M": "Slaughter it and take the blood and splash it against the sides of the altar.",
      "T": "Slaughter it; take the blood and dash it against the altar on all sides."
    },
    "17": {
      "L": "And thou shalt cut the ram in pieces, and wash the inwards of him, and his legs, and put them unto his pieces, and unto his head.",
      "M": "Cut the ram into pieces and wash the internal organs and the legs, putting them with the head and the other pieces.",
      "T": "Cut the ram in pieces, wash the entrails and legs, and reassemble all the pieces with the head."
    },
    "18": {
      "L": "And thou shalt burn the whole ram upon the altar: it is a burnt offering unto the LORD: it is a sweet savour, an offering made by fire unto the LORD.",
      "M": "Then burn the entire ram on the altar. It is a burnt offering to the LORD, a food offering, an aroma pleasing to the LORD.",
      "T": "Burn the whole ram on the altar — a whole burnt offering to the LORD, a pleasing aroma, a fire-offering that ascends entirely to God. Nothing held back."
    },
    "19": {
      "L": "And thou shalt take the other ram; and Aaron and his sons shall put their hands upon the head of the ram.",
      "M": "Take the other ram, and Aaron and his sons shall lay their hands on its head.",
      "T": "Take the second ram — the ram of ordination. Aaron and his sons lay their hands on its head."
    },
    "20": {
      "L": "Then shalt thou kill the ram, and take of his blood, and put it upon the tip of the right ear of Aaron, and upon the tip of the right ear of his sons, and upon the thumb of their right hand, and upon the great toe of their right foot, and sprinkle the blood upon the altar round about.",
      "M": "Slaughter it, take some of its blood and put it on the lobes of the right ears of Aaron and his sons, on the thumbs of their right hands, and on the big toes of their right feet. Then splash blood against the sides of the altar.",
      "T": "Slaughter it. Apply blood to the right earlobe of Aaron and each of his sons — the organ of hearing, to consecrate what they hear. Then to the right thumb — to consecrate what they do with their hands. Then to the right big toe — to consecrate where they walk. Sprinkle the rest on the altar. The priest is consecrated from ear to toe; every faculty set apart."
    },
    "21": {
      "L": "And thou shalt take of the blood that is upon the altar, and of the anointing oil, and sprinkle it upon Aaron, and upon his garments, and upon his sons, and upon the garments of his sons with him: and he shall be hallowed, and his garments, and his sons, and his sons' garments with him.",
      "M": "And take some of the blood on the altar and some of the anointing oil and sprinkle it on Aaron and his garments and on his sons and their garments. Then he and his sons and their garments will be consecrated.",
      "T": "Sprinkle blood from the altar mixed with anointing oil on Aaron and his garments, on his sons and their garments. The garments become holy along with the men who wear them. Priest and vestments are inseparable in the eyes of God."
    },
    "22": {
      "L": "Also thou shalt take of the ram the fat and the rump, and the fat that covereth the inwards, and the caul above the liver, and the two kidneys, and the fat that is upon them, and the right shoulder; for it is a ram of consecration:",
      "M": "From this ram take the fat, the fat tail, the fat around the internal organs, the long lobe of the liver, both kidneys with the fat on them, and the right thigh. This is the ordination ram.",
      "T": "From the ordination ram take: the fat, the fat tail, the covering fat of the entrails, the liver's lobe, the two kidneys with their fat, and the right thigh — the prime cut, the best, for this is the ram of consecration."
    },
    "23": {
      "L": "And one loaf of bread, and one cake of oiled bread, and one wafer out of the basket of the unleavened bread that is before the LORD:",
      "M": "From the basket of bread made without yeast, which is before the LORD, take one round loaf, one thick loaf with olive oil, and one thin loaf.",
      "T": "From the basket before the LORD: one plain loaf, one oiled loaf, one thin wafer — the bread that belongs to God."
    },
    "24": {
      "L": "And thou shalt put all in the hands of Aaron, and in the hands of his sons; and shalt wave them for a wave offering before the LORD.",
      "M": "Put all these in the hands of Aaron and his sons and have them wave them before the LORD as a wave offering.",
      "T": "Place all of it — the fat portions and the bread — in the hands of Aaron and his sons. Let them wave it before the LORD — this is the 'filling of the hands,' the act that defines ordination. The priest's hands are literally filled with his first offering."
    },
    "25": {
      "L": "And thou shalt receive them of their hands, and burn them upon the altar for a burnt offering, for a sweet savour before the LORD: it is an offering made by fire unto the LORD.",
      "M": "Then take them from their hands and burn them on the altar along with the burnt offering for a pleasing aroma to the LORD, a food offering to the LORD.",
      "T": "Take the portions from their hands and burn them on the altar with the burnt offering — a pleasing aroma rising before the LORD. The first priestly act is completed."
    },
    "26": {
      "L": "And thou shalt take the breast of the ram of Aaron's consecration, and wave it for a wave offering before the LORD: and it shall be thy part.",
      "M": "After you take the breast of the ordination ram belonging to Aaron, wave it before the LORD as a wave offering; it will be your share.",
      "T": "Take the breast of Aaron's ordination ram and wave it before the LORD — this breast becomes your own portion, Moses. The one who ordains the priest receives a share."
    },
    "27": {
      "L": "And thou shalt sanctify the breast of the wave offering, and the shoulder of the heave offering, which is waved, and which is heaved up, of the ram of the consecration, even of that which is for Aaron, and of that which is for his sons:",
      "M": "Consecrate those parts of the ordination ram that belong to Aaron and his sons: the breast that was waved and the thigh that was presented.",
      "T": "Set apart the waved breast and the presented thigh of the ordination ram as sacred — belonging to Aaron and his sons."
    },
    "28": {
      "L": "And it shall be Aaron's and his sons' by a statute for ever from the children of Israel: for it is an heave offering: and it shall be an heave offering from the children of Israel of the sacrifice of their peace offerings, even their heave offering unto the LORD.",
      "M": "This is always to be the regular share from the Israelites for Aaron and his sons. It is the contribution the Israelites are to make to the LORD from their fellowship offerings.",
      "T": "This becomes a permanent statute: the breast and the thigh belong to Aaron and his sons forever, contributed by Israel from their fellowship offerings. The priest is sustained by the gifts of the people he mediates for."
    },
    "29": {
      "L": "And the holy garments of Aaron shall be his sons' after him, to be anointed therein, and to be consecrated in them.",
      "M": "Aaron's sacred garments will belong to his descendants after him, so that they can be anointed and ordained in them.",
      "T": "Aaron's sacred garments pass to his sons after him — they are worn at each subsequent ordination. The office outlasts the man; the garments are the continuity."
    },
    "30": {
      "L": "And that son that is priest in his stead shall put them on seven days, when he cometh into the tabernacle of the congregation to minister in the holy place.",
      "M": "The son who succeeds him as priest and comes to the tent of meeting to minister in the holy place is to wear them seven days.",
      "T": "Whichever son succeeds Aaron as high priest wears the garments for seven full days upon entering the tent of meeting — the same seven-day pattern of consecration, repeated for every generation."
    },
    "31": {
      "L": "And thou shalt take the ram of the consecration, and seethe his flesh in the holy place.",
      "M": "Take the ram of the ordination and cook the meat in a sacred place.",
      "T": "Boil the ordination ram's meat in a sacred location."
    },
    "32": {
      "L": "And Aaron and his sons shall eat the flesh of the ram, and the bread that is in the basket, by the door of the tabernacle of the congregation.",
      "M": "At the entrance to the tent of meeting, Aaron and his sons are to eat the meat of the ram and the bread that is in the basket.",
      "T": "At the tent's entrance, Aaron and his sons eat the ram's flesh and the bread from the basket. Ordination ends with a sacred meal — priest and God's provision consumed together."
    },
    "33": {
      "L": "And they shall eat those things wherewith the atonement was made, to consecrate and to sanctify them: but a stranger shall not eat thereof, because they are holy.",
      "M": "They are to eat these offerings by which atonement was made for their ordination and consecration. But no one else may eat them, because they are sacred.",
      "T": "They eat the very offerings through which their atonement was made and their ordination completed. No outsider may eat — these things are holy, consumed only by those who have been made holy through them."
    },
    "34": {
      "L": "And if ought of the flesh of the consecrations, or of the bread, remain unto the morning, then thou shalt burn the remainder with fire: it shall not be eaten, because it is holy.",
      "M": "If any of the meat of the ordination ram or any bread is left over till morning, burn it up. It must not be eaten, because it is sacred.",
      "T": "If any meat or bread remains until morning, burn it — it must not be eaten. That which belongs to God's holy day does not carry over. Each day's worship is complete in itself."
    },
    "35": {
      "L": "And thus shalt thou do unto Aaron, and to his sons, according to all things which I have commanded thee: seven days shalt thou consecrate them.",
      "M": "Do for Aaron and his sons everything I have commanded you, taking seven days to ordain them.",
      "T": "Carry out every part of this ceremony for Aaron and his sons, exactly as I have commanded, for seven full days. Ordination is not rushed. Seven days — the fullness of a week, the number of completion."
    },
    "36": {
      "L": "And thou shalt offer every day a bullock for a sin offering for atonement: and thou shalt cleanse the altar, when thou hast made an atonement for it, and thou shalt anoint it, to sanctify it.",
      "M": "Sacrifice a bull each day as a sin offering to make atonement. Purify the altar by making atonement for it, and anoint it to consecrate it.",
      "T": "Each day of the seven, offer a bull as a purification offering. Purge the altar through the atonement rite, and anoint it to consecrate it. The altar itself must be made holy before it can make others holy."
    },
    "37": {
      "L": "Seven days thou shalt make an atonement for the altar, and sanctify it; and it shall be an altar most holy: whatsoever toucheth the altar shall be holy.",
      "M": "For seven days make atonement for the altar and consecrate it. Then the altar will be most holy, and whatever touches it will be holy.",
      "T": "Seven days of atonement for the altar; at the end it is most holy — so holy that whatever touches it is drawn into its holiness. The altar becomes a holy magnet."
    },
    "38": {
      "L": "Now this is that which thou shalt offer upon the altar; two lambs of the first year day by day continually.",
      "M": "This is what you are to offer on the altar regularly each day: two lambs a year old.",
      "T": "This is the perpetual offering — the tamid — that will be offered on the altar every single day: two one-year-old lambs."
    },
    "39": {
      "L": "The one lamb thou shalt offer in the morning; and the other lamb thou shalt offer at even:",
      "M": "Offer one in the morning and the other at twilight.",
      "T": "One lamb at dawn. One lamb at dusk. Morning and evening, the day is bracketed by worship."
    },
    "40": {
      "L": "And with the one lamb a tenth deal of flour mingled with the fourth part of an hin of beaten oil; and the fourth part of an hin of wine for a drink offering.",
      "M": "With the first lamb offer a tenth of an ephah of the finest flour mixed with a quarter of a hin of oil from pressed olives, and a quarter of a hin of wine as a drink offering.",
      "T": "With the morning lamb: a tenth of an ephah of fine flour mixed with a quarter hin of pressed olive oil, and a quarter hin of wine as a libation."
    },
    "41": {
      "L": "And the other lamb thou shalt offer at even, and shalt do thereto according to the meat offering of the morning, and according to the drink offering thereof, for a sweet savour, an offering made by fire unto the LORD.",
      "M": "Sacrifice the other lamb at twilight with the same grain offering and drink offering that you offer in the morning. This is a food offering, a pleasing aroma to the LORD.",
      "T": "The evening lamb with the same grain offering and libation as the morning — a pleasing aroma, a fire-offering ascending to the LORD. Day begins and ends in worship."
    },
    "42": {
      "L": "This shall be a continual burnt offering throughout your generations at the door of the tabernacle of the congregation before the LORD: where I will meet you, to speak there unto thee.",
      "M": "For the generations to come this burnt offering is to be made regularly at the entrance to the tent of meeting, before the LORD. There I will meet you and speak to you.",
      "T": "This perpetual burnt offering continues through all your generations — offered at the entrance of the tent of meeting before the LORD. It is the standing appointment: the place where God meets his people, day after day, without fail."
    },
    "43": {
      "L": "And there I will meet with the children of Israel, and the tabernacle shall be sanctified by my glory.",
      "M": "There also I will meet with the Israelites, and the place will be consecrated by my glory.",
      "T": "There I will meet with all of Israel — and the dwelling will be made holy by my glory. God's presence sanctifies the place where he chooses to be."
    },
    "44": {
      "L": "And I will sanctify the tabernacle of the congregation, and the altar: I will sanctify also both Aaron and his sons, to minister to me in the priest's office.",
      "M": "So I will consecrate the tent of meeting and the altar and will consecrate Aaron and his sons to serve me as priests.",
      "T": "I will consecrate the tent of meeting. I will consecrate the altar. I will consecrate Aaron and his sons. God himself does the consecrating — human ceremony is the vehicle, but divine action is the reality."
    },
    "45": {
      "L": "And I will dwell among the children of Israel, and will be their God.",
      "M": "Then I will dwell among the Israelites and be their God.",
      "T": "And I will dwell among the people of Israel and be their God. This is the purpose of everything — the ark, the curtains, the priests, the offerings: God coming home to live among his people."
    },
    "46": {
      "L": "And they shall know that I am the LORD their God, that brought them forth out of the land of Egypt, that I may dwell among them: I am the LORD their God.",
      "M": "They will know that I am the LORD their God, who brought them out of Egypt so that I might dwell among them. I am the LORD their God.",
      "T": "They will know it: I am the LORD their God — the one who brought them out of Egypt for this very purpose, that I might dwell in the midst of them. The Exodus was not only liberation from slavery. It was the beginning of the journey home to God. I am the LORD their God."
    }
  },
  "30": {
    "1": {
      "L": "And thou shalt make an altar to burn incense upon: of shittim wood shalt thou make it.",
      "M": "Make an altar of acacia wood for burning incense.",
      "T": "Build an altar of acacia wood for burning incense. This altar stands before the veil — the fragrance of prayer ascending before the throne."
    },
    "2": {
      "L": "A cubit shall be the length thereof, and a cubit the breadth thereof; foursquare shall it be: and two cubits shall be the height thereof: the horns thereof shall be of the same.",
      "M": "It is to be square, a cubit long and a cubit wide, and two cubits high — its horns of one piece with it.",
      "T": "One cubit square, two cubits tall — twice the height of its width, proportioned like a pillar. Its horns of one piece with it."
    },
    "3": {
      "L": "And thou shalt overlay it with pure gold, the top thereof, and the sides thereof round about, and the horns thereof; and thou shalt make unto it a crown of gold round about.",
      "M": "Overlay the top and all the sides and the horns with pure gold, and make a gold molding around it.",
      "T": "Overlay its top, sides, and horns entirely with pure gold, and add a gold molding around the top. Gold throughout — this altar touches the holiest space."
    },
    "4": {
      "L": "And two golden rings shalt thou make to it under the crown of it, by the two corners thereof, upon the two sides of it shalt thou make it; and they shall be for places for the staves to bear it withal.",
      "M": "Make two gold rings for it below the molding — one on opposite sides — to hold the poles used to carry it.",
      "T": "Two gold rings below the molding, one on each side, for the carrying poles."
    },
    "5": {
      "L": "And thou shalt make the staves of shittim wood, and overlay them with gold.",
      "M": "Make the poles of acacia wood and overlay them with gold.",
      "T": "Carrying poles of acacia wood overlaid with gold."
    },
    "6": {
      "L": "And thou shalt put it before the vail that is by the ark of the testimony, before the mercy seat that is over the testimony, where I will meet with thee.",
      "M": "Put the altar in front of the curtain that shields the ark of the covenant law — before the atonement cover that is over the tablets of the covenant law — where I will meet with you.",
      "T": "Place it before the veil that hangs before the ark of the testimony — before the cover of atonement. This is where I will meet with you. The incense altar marks the approach to the divine address."
    },
    "7": {
      "L": "And Aaron shall burn thereon sweet incense every morning: when he dresseth the lamps, he shall burn incense upon it.",
      "M": "Aaron must burn fragrant incense on the altar every morning when he tends the lamps.",
      "T": "Every morning when Aaron tends the lamps, he burns fragrant incense on this altar. Prayer accompanies the lighting of the light — they are one act of approach."
    },
    "8": {
      "L": "And when Aaron lighteth the lamps at even, he shall burn incense upon it, a perpetual incense before the LORD throughout your generations.",
      "M": "He must burn incense again when he lights the lamps at twilight so incense will burn regularly before the LORD for the generations to come.",
      "T": "And at twilight when he lights the lamps again, he burns incense again. Morning and evening — the perpetual incense before the LORD, rising without ceasing through all your generations."
    },
    "9": {
      "L": "Ye shall offer no strange incense thereon, nor burnt sacrifice, nor meat offering; neither shall ye pour drink offering thereon.",
      "M": "Do not offer on this altar any other incense or any burnt offering or grain offering, and do not pour a drink offering on it.",
      "T": "On this altar: only the sacred incense. No other incense — nothing unauthorized. No burnt offering, no grain offering, no libation. This altar has one purpose: to carry the fragrance of prayer before God."
    },
    "10": {
      "L": "And Aaron shall make an atonement upon the horns of it once in a year with the blood of the sin offering of atonements: once in the year shall he make atonement upon it throughout your generations: it is most holy unto the LORD.",
      "M": "Once a year Aaron shall make atonement on its horns. This annual atonement must be made with the blood of the atoning sin offering for the generations to come. It is most holy to the LORD.",
      "T": "Once a year — on the Day of Atonement — Aaron applies blood to its horns, making atonement for it. The incense altar too must be purged of accumulated impurity. Once a year, through all generations. It is most holy to the LORD."
    },
    "11": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "Then the LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "12": {
      "L": "'When thou takest the sum of the children of Israel after their number, then shall they give every man a ransom for his soul unto the LORD, when thou numberest them; that there be no plague among them, when thou numberest them.'",
      "M": "'When you take a census of the Israelites to count them, each one must pay the LORD a ransom for his life at the time he is counted. Then no plague will come on them when you number them.'",
      "T": "'When you take a census of Israel and number the people, each person counted must give the LORD a ransom for his life. To be counted is to be known by God — and every life before God requires atonement. Without this, the census itself brings death.'"
    },
    "13": {
      "L": "'This they shall give, every one that passeth among them that are numbered, half a shekel after the shekel of the sanctuary: a shekel is twenty gerahs: an half shekel shall be the offering of the LORD.'",
      "M": "'Each one who crosses over to those already counted is to give a half shekel, according to the sanctuary shekel, which weighs twenty gerahs. This half shekel is an offering to the LORD.'",
      "T": "'Every person who is numbered gives half a shekel — by the sanctuary standard, where twenty gerahs make a shekel. A half shekel: the same for each person. This is the atonement levy for the LORD.'"
    },
    "14": {
      "L": "'Every one that passeth among them that are numbered, from twenty years old and above, shall give an offering unto the LORD.'",
      "M": "'All who cross over, those twenty years old or more, are to give an offering to the LORD.'",
      "T": "'Everyone twenty years and older who is counted must give this offering to the LORD. No exemptions — adulthood brings accountability.'"
    },
    "15": {
      "L": "'The rich shall not give more, and the poor shall not give less than half a shekel, when they give an offering unto the LORD, to make an atonement for your souls.'",
      "M": "'The rich are not to give more than a half shekel and the poor are not to give less when you make the offering to the LORD to atone for your lives.'",
      "T": "'The rich give no more; the poor give no less: half a shekel each. Before God, atonement is equal. Wealth buys no extra standing; poverty does not diminish it. One price for all lives.'"
    },
    "16": {
      "L": "'And thou shalt take the atonement money of the children of Israel, and shalt appoint it for the service of the tabernacle of the congregation; that it may be a memorial unto the children of Israel before the LORD, to make an atonement for your souls.'",
      "M": "'Receive the atonement money from the Israelites and use it for the service of the tent of meeting. It will be a memorial for the Israelites before the LORD, making atonement for your lives.'",
      "T": "'Collect this atonement money from Israel and direct it to the service of the tent of meeting. It becomes a memorial before the LORD — Israel's collective ransom, remembered before God. The tent of God's presence is sustained by the ransom of God's people.'"
    },
    "17": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "Then the LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "18": {
      "L": "'Thou shalt also make a laver of brass, and his foot also of brass, to wash withal: and thou shalt put it between the tabernacle of the congregation and the altar, and thou shalt put water therein.'",
      "M": "'Make a bronze basin, with its bronze stand, for washing. Place it between the tent of meeting and the altar, and put water in it.'",
      "T": "'Make a bronze basin on a bronze stand and place it between the tent of meeting and the altar. Fill it with water. Between sacrifice and the holy place stands the water of cleansing.'"
    },
    "19": {
      "L": "'For Aaron and his sons shall wash their hands and their feet thereat:'",
      "M": "'Aaron and his sons are to wash their hands and feet with water from it.'",
      "T": "'Aaron and his sons wash their hands and feet from it — hands for what they do, feet for where they go.'"
    },
    "20": {
      "L": "'When they go into the tabernacle of the congregation, they shall wash with water, that they die not; or when they come near to the altar to minister, to burn offering made by fire unto the LORD:'",
      "M": "'Whenever they enter the tent of meeting, they shall wash with water so that they will not die. Also, when they approach the altar to minister by presenting a food offering to the LORD,'",
      "T": "'Every time they enter the tent of meeting, they wash — so that they will not die. Every time they approach the altar to offer a fire-offering to the LORD, they wash. The penalty for unwashed approach is death. Holiness requires clean hands.'"
    },
    "21": {
      "L": "'So they shall wash their hands and their feet, that they die not: and it shall be a statute for ever to them, even to him and to his seed throughout their generations.'",
      "M": "'they shall wash their hands and feet so that they will not die. This is to be a lasting ordinance for Aaron and his descendants for the generations to come.'",
      "T": "'They wash hands and feet — so they will not die. A permanent statute for Aaron and all his descendants through every generation. The requirement of cleansing never lapses.'"
    },
    "22": {
      "L": "Moreover the LORD spake unto Moses, saying,",
      "M": "Then the LORD said to Moses,",
      "T": "The LORD said to Moses:"
    },
    "23": {
      "L": "'Take thou also unto thee principal spices, of pure myrrh five hundred shekels, and of sweet cinnamon half so much, even two hundred and fifty shekels, and of sweet calamus two hundred and fifty shekels,'",
      "M": "'Take the following fine spices: 500 shekels of liquid myrrh, half as much — that is, 250 shekels — of fragrant cinnamon, 250 shekels of fragrant calamus,'",
      "T": "'Take the choicest spices: five hundred shekels of liquid myrrh, two hundred fifty shekels of fragrant cinnamon, two hundred fifty shekels of aromatic calamus —'"
    },
    "24": {
      "L": "'And of cassia five hundred shekels, after the shekel of the sanctuary, and of oil olive an hin:'",
      "M": "'500 shekels of cassia — all according to the sanctuary shekel — and a hin of olive oil.'",
      "T": "'five hundred shekels of cassia — measured by the sanctuary shekel — and one hin of olive oil.'"
    },
    "25": {
      "L": "'And thou shalt make it an oil of holy ointment, an ointment compound after the art of the apothecary: it shall be an holy anointing oil.'",
      "M": "'Make these into a sacred anointing oil, a fragrant blend, the work of a perfumer. It will be the sacred anointing oil.'",
      "T": "'Blend these into a sacred anointing oil — mixed by a skilled perfumer, holy. This is the oil that sets people and things apart for God.'"
    },
    "26": {
      "L": "'And thou shalt anoint the tabernacle of the congregation therewith, and the ark of the testimony,'",
      "M": "'Use it to anoint the tent of meeting, the ark of the covenant law,'",
      "T": "'With this oil anoint the tent of meeting and the ark of the testimony —'"
    },
    "27": {
      "L": "'And the table and all his vessels, and the candlestick and his vessels, and the altar of incense,'",
      "M": "'the table and all its articles, the lampstand and its accessories, the altar of incense,'",
      "T": "'the table and all its articles, the lampstand and its accessories, the incense altar —'"
    },
    "28": {
      "L": "'And the altar of burnt offering with all his vessels, and the laver and his foot:'",
      "M": "'the altar of burnt offering and all its utensils, and the basin with its stand.'",
      "T": "'the altar of burnt offering and all its utensils, the basin and its stand.'"
    },
    "29": {
      "L": "'And thou shalt sanctify them, that they may be most holy: whatsoever toucheth them shall be holy.'",
      "M": "'You shall consecrate them so they will be most holy, and whatever touches them will be holy.'",
      "T": "'Consecrate them all so they become most holy. Whatever touches them is drawn into their holiness. The anointing transfers sacred status.'"
    },
    "30": {
      "L": "'And thou shalt anoint Aaron and his sons, and consecrate them, that they may minister unto me in the priest's office.'",
      "M": "'Anoint Aaron and his sons and consecrate them to serve me as priests.'",
      "T": "'Anoint Aaron and his sons and consecrate them — so they may minister to me as priests. The same oil that anoints the furniture anoints the people. Priest and sanctuary share one consecration.'"
    },
    "31": {
      "L": "'And thou shalt speak unto the children of Israel, saying, This shall be an holy anointing oil unto me throughout your generations.'",
      "M": "'Say to the Israelites, \"This is to be my sacred anointing oil for the generations to come.\"'",
      "T": "'Tell the Israelites: this oil is the sacred anointing oil before me for all your generations.'"
    },
    "32": {
      "L": "'Upon man's flesh shall it not be poured, neither shall ye make any other like it, after the composition of it: it is holy, and it shall be holy unto you.'",
      "M": "'Do not pour it on anyone else's body and do not make any other oil using the same formula. It is sacred, and you are to consider it sacred.'",
      "T": "'Do not pour it on an ordinary person's body. Do not replicate its formula for personal use. It is holy — reserved entirely for God's purposes. To misuse it is to treat the holy as ordinary.'"
    },
    "33": {
      "L": "'Whosoever compoundeth any like it, or whosoever putteth any of it upon a stranger, shall even be cut off from his people.'",
      "M": "'Whoever makes perfume like it and puts it on anyone who is not a priest must be cut off from their people.'\"",
      "T": "'Anyone who makes a copy of this oil, or who anoints an unauthorized person with it, shall be cut off from the people. The boundary of the holy is not to be crossed.'"
    },
    "34": {
      "L": "And the LORD said unto Moses, 'Take unto thee sweet spices, stacte, and onycha, and galbanum; these sweet spices with pure frankincense: of each shall there be a like weight:'",
      "M": "Then the LORD said to Moses, 'Take fragrant spices — gum resin, onycha and galbanum — and pure frankincense, all in equal amounts,'",
      "T": "The LORD said to Moses: 'Take these fragrant spices in equal parts — stacte, onycha, galbanum, and pure frankincense —'"
    },
    "35": {
      "L": "'And thou shalt make it a perfume, a confection after the art of the apothecary, tempered together, pure and holy:'",
      "M": "'and make a fragrant blend of incense, the work of a perfumer. It is to be salted and pure and sacred.'",
      "T": "'and blend them into a sacred incense — a perfumer's craft, salted, pure, and holy. Nothing improvised; God specifies the fragrance of his house.'"
    },
    "36": {
      "L": "'And thou shalt beat some of it very small, and put of it before the testimony in the tabernacle of the congregation, where I will meet with thee: it shall be unto you most holy.'",
      "M": "'Grind some of it to powder and place it in front of the ark of the covenant law in the tent of meeting, where I will meet with you. It shall be most holy to you.'",
      "T": "'Grind some of it fine and place it before the ark of testimony in the tent of meeting — where I meet with you. It is most holy to you. The finest incense marks the closest point of access to God.'"
    },
    "37": {
      "L": "'And as for the perfume which thou shalt make, ye shall not make to yourselves according to the composition thereof: it shall be unto thee holy for the LORD.'",
      "M": "'Do not make any incense with this formula for yourselves; consider it holy to the LORD.'",
      "T": "'Do not make this incense formula for your own use. It belongs entirely to the LORD — holy to him alone.'"
    },
    "38": {
      "L": "'Whoever shall make like unto that, to smell thereto, shall even be cut off from his people.'",
      "M": "'Whoever makes incense like it to enjoy its fragrance must be cut off from their people.'\"",
      "T": "'Anyone who makes this blend to enjoy as personal fragrance shall be cut off from the people. What is holy to God is not to be domesticated for human pleasure.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'exodus')
        merge_tier(existing, EXODUS, tier_key)
        save(tier_dir, 'exodus', existing)
    print('Exodus 25–30 written.')

if __name__ == '__main__':
    main()
