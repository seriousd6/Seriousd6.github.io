"""
MKT Numbers chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-numbers-7-12.py

Covers: dedication offerings of the twelve leaders (ch. 7), lampstand and Levite
consecration (ch. 8), Passover provisions and the cloud-pillar (ch. 9), silver trumpets
and the departure from Sinai (ch. 10), grumbling, quail, and the seventy elders (ch. 11),
Miriam and Aaron's challenge and Miriam's leprosy (ch. 12).

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps) in L/M; "the LORD" in T — matches Exodus/Leviticus
- H430 (אֱלֹהִים): "God" in all tiers
- H5387 (נָשִׂיא): "leader" throughout, not "prince" — these are tribal chieftains, not royalty
- H2598 (חֲנֻכָּה): "dedication" in all tiers — the consecration of the altar by gifts
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" in all tiers
- H4908 (מִשְׁכָּן): "tabernacle" in L/M; "tabernacle" in T (well established)
- H5930 (עֹלָה): "burnt offering" all tiers
- H2403 (חַטָּאת): "sin offering" all tiers
- H8002 (שֶׁלֶם): "fellowship offering" in M/T; "peace offering" in L (preserves traditional term for L-tier transparency)
- H4503 (מִנְחָה): "grain offering" all tiers
- H6453 (פֶּסַח): "Passover" all tiers
- H6051 (עָנָן): "cloud" all tiers — the divine cloud-presence
- H4478 (מָן): "manna" all tiers
- H7958 (שְׂלָו): "quails" L/M; "quails" T — the term is specific enough
- H7307 (רוּחַ): In ch. 11:17,25,26,29 = the divine spirit distributed from Moses to the elders
  → L/M="spirit", T="the Spirit" (capitalized, divine gift);
  In 11:31 = the wind the LORD sent to carry quails = L/M="a wind", T="a great wind"
- H6879 (צָרַע): L/M="leprous"; T="struck with a skin disease" — the Hebrew term covers
  various skin conditions and is not certainly Hansen's disease; T clarifies without
  mistranslating the gravity
- H6035 (עָנָו): "meek" in L/M at 12:3; T="humble beyond all measure" — the superlative
  form is deliberate; Moses's humility is presented as the reason he alone hears God directly
- H3727 (כַּפֹּרֶת): "mercy seat" L; "atonement cover" M; "mercy seat" T (iconic; T can keep
  the traditional rendering when it communicates the theological richness)
- H7086 (קְעָרָה): "charger/dish" — silver plate for grain offering; L="charger", M/T="dish"
- H4219 (מִזְרָק): "bowl/basin" — the shallower silver vessel; L="bowl", M/T="basin"
- H3709 (כַּף): "spoon/pan" — actually a ladle or concave hand-shaped vessel for incense;
  L="spoon", M="pan", T="ladle"
- H5715 (עֵדוּת): "testimony/covenant document" — the tablets in the ark; L/M="testimony",
  T="the covenant document"
- Chapter 7 note: The identical offering from each tribe over twelve days signals the theological
  equality of all Israel before God. T tier varies slightly while preserving the liturgical
  repetition; the repetition is meaningful, not editorial carelessness.
- Chapter 10:35-36 note: These two verses are bracketed in some manuscripts with inverted nuns,
  possibly marking them as a floating unit; the MT text is followed here without comment in the
  verse itself. They are echoed in Ps 68:1. Rendered with poetic force in T tier.
- Chapter 11 note: Moses's lament in vv. 11-15 is one of the rawest complaints in the Pentateuch —
  the language of pregnancy and nursing ("Have I conceived this people?") is deliberately shocking.
  T tier preserves the rhetorical force.
- Hobab (10:29): Identified as Moses's father-in-law here, though Jethro is named elsewhere;
  Hebrew allows "relative by marriage"; the translation follows MT and renders "father-in-law"
  in L/M while T notes the ambiguity implicitly by using "kinsman by marriage."
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
  "7": {
    "1": {
      "L": "And it came to pass on the day that Moses had fully set up the tabernacle, and had anointed it and sanctified it and all its furnishings, and the altar and all its vessels, and had anointed them and sanctified them,",
      "M": "On the day Moses finished setting up the tabernacle, he anointed and consecrated it together with all its furnishings, and anointed and consecrated the altar and all its utensils.",
      "T": "The day Moses completed the tabernacle's erection — anointing every piece, consecrating altar and furnishings alike —"
    },
    "2": {
      "L": "that the princes of Israel, heads of the houses of their fathers, who were the leaders of the tribes, who stood over them that were numbered, offered:",
      "M": "the leaders of Israel — heads of their ancestral houses, leaders of the tribes, those who had overseen the census — drew near",
      "T": "the twelve tribal leaders came forward: one from each tribe, head of his ancestral house, the man responsible for his tribe's census registration."
    },
    "3": {
      "L": "And they brought their offering before the LORD, six covered wagons and twelve oxen: a wagon for every two of the princes and for each one an ox; and they brought them before the tabernacle.",
      "M": "They brought their offering before the LORD — six covered carts and twelve oxen: one cart for every two leaders and one ox for each leader — and presented them before the tabernacle.",
      "T": "Twelve oxen, six covered wagons: one ox per leader, one wagon per pair. They brought them all before the LORD at the tabernacle — a practical gift for holy work."
    },
    "4": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "5": {
      "L": "Take it of them, that they may be to do the service of the tabernacle of the congregation; and thou shalt give them unto the Levites, to every man according to his service.",
      "M": "Accept these from them for the work of the tent of meeting, and give them to the Levites — each man a portion according to the service he performs.",
      "T": "Accept these gifts for the tent of meeting's transport. Distribute them to the Levites, each group receiving what matches the weight of its assignment."
    },
    "6": {
      "L": "And Moses took the wagons and the oxen, and gave them unto the Levites.",
      "M": "Moses took the carts and the oxen and distributed them to the Levites.",
      "T": "Moses accepted the wagons and oxen and apportioned them to the Levites."
    },
    "7": {
      "L": "Two wagons and four oxen he gave unto the sons of Gershon, according to their service.",
      "M": "Two carts and four oxen he gave to the sons of Gershon, proportioned to their service.",
      "T": "The Gershonites — charged with carrying the tabernacle's woven curtains and coverings — received two wagons and four oxen."
    },
    "8": {
      "L": "And four wagons and eight oxen he gave unto the sons of Merari, according to their service, under the hand of Ithamar the son of Aaron the priest.",
      "M": "Four carts and eight oxen he gave to the sons of Merari, according to their service, under the supervision of Ithamar son of Aaron the priest.",
      "T": "The Merarites — carrying the tabernacle's heavier framework of boards, bars, and bases — received four wagons and eight oxen, supervised by Ithamar son of Aaron."
    },
    "9": {
      "L": "But unto the sons of Kohath he gave none: because the service of the sanctuary belonging unto them was that they should bear it upon their shoulders.",
      "M": "But he gave nothing to the sons of Kohath, because their duty was to carry the holy things, which had to be borne on their shoulders.",
      "T": "The Kohathites received no wagons. The holiest objects — ark, table, lampstand, altars — could not be carted; they were to be borne on human shoulders, carried close."
    },
    "10": {
      "L": "And the princes offered for the dedicating of the altar in the day that it was anointed, even the princes offered their offering before the altar.",
      "M": "The leaders brought dedication offerings for the altar on the day it was anointed; the leaders presented their offering before the altar.",
      "T": "As the altar was anointed, all twelve leaders came forward with dedication offerings — each one presenting his tribute before the newly consecrated altar."
    },
    "11": {
      "L": "And the LORD said unto Moses, They shall offer their offering, each prince on his day, for the dedicating of the altar.",
      "M": "The LORD said to Moses: Each leader shall present his offering on his own day for the dedication of the altar.",
      "T": "The LORD told Moses: give each leader his own day — twelve offerings over twelve days, one tribe at a time, the altar's dedication unhurried and complete."
    },
    "12": {
      "L": "And he that offered his offering the first day was Nahshon the son of Amminadab, of the tribe of Judah:",
      "M": "The one who offered his offering on the first day was Nahshon son of Amminadab, of the tribe of Judah.",
      "T": "Day one: Nahshon son of Amminadab, leader of Judah."
    },
    "13": {
      "L": "And his offering was one silver charger, the weight thereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them were full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "14": {
      "L": "One spoon of ten shekels of gold, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "15": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "16": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "17": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Nahshon the son of Amminadab.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Nahshon son of Amminadab.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Nahshon son of Amminadab's complete offering."
    },
    "18": {
      "L": "On the second day Nethaneel the son of Zuar, prince of Issachar, did offer:",
      "M": "On the second day Nethaneel son of Zuar, leader of Issachar, offered his offering.",
      "T": "Day two: Nethaneel son of Zuar, leader of Issachar."
    },
    "19": {
      "L": "He offered for his offering one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "20": {
      "L": "One spoon of gold of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "21": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "22": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "23": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Nethaneel the son of Zuar.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Nethaneel son of Zuar.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Nethaneel son of Zuar's complete offering."
    },
    "24": {
      "L": "On the third day Eliab the son of Helon, prince of the children of Zebulun:",
      "M": "On the third day Eliab son of Helon, leader of Zebulun, offered his offering.",
      "T": "Day three: Eliab son of Helon, leader of Zebulun."
    },
    "25": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "26": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "27": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "28": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "29": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Eliab the son of Helon.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Eliab son of Helon.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Eliab son of Helon's complete offering."
    },
    "30": {
      "L": "On the fourth day Elizur the son of Shedeur, prince of the children of Reuben:",
      "M": "On the fourth day Elizur son of Shedeur, leader of Reuben, offered his offering.",
      "T": "Day four: Elizur son of Shedeur, leader of Reuben."
    },
    "31": {
      "L": "His offering was one silver charger of the weight of an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "32": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "33": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "34": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "35": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Elizur the son of Shedeur.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Elizur son of Shedeur.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Elizur son of Shedeur's complete offering."
    },
    "36": {
      "L": "On the fifth day Shelumiel the son of Zurishaddai, prince of the children of Simeon:",
      "M": "On the fifth day Shelumiel son of Zurishaddai, leader of Simeon, offered his offering.",
      "T": "Day five: Shelumiel son of Zurishaddai, leader of Simeon."
    },
    "37": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "38": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "39": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "40": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "41": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Shelumiel the son of Zurishaddai.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Shelumiel son of Zurishaddai.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Shelumiel son of Zurishaddai's complete offering."
    },
    "42": {
      "L": "On the sixth day Eliasaph the son of Deuel, prince of the children of Gad:",
      "M": "On the sixth day Eliasaph son of Deuel, leader of Gad, offered his offering.",
      "T": "Day six: Eliasaph son of Deuel, leader of Gad."
    },
    "43": {
      "L": "His offering was one silver charger of the weight of an hundred and thirty shekels, a silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "44": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "45": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "46": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "47": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Eliasaph the son of Deuel.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Eliasaph son of Deuel.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Eliasaph son of Deuel's complete offering."
    },
    "48": {
      "L": "On the seventh day Elishama the son of Ammihud, prince of the children of Ephraim:",
      "M": "On the seventh day Elishama son of Ammihud, leader of Ephraim, offered his offering.",
      "T": "Day seven: Elishama son of Ammihud, leader of Ephraim."
    },
    "49": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "50": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "51": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "52": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "53": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Elishama the son of Ammihud.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Elishama son of Ammihud.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Elishama son of Ammihud's complete offering."
    },
    "54": {
      "L": "On the eighth day offered Gamaliel the son of Pedahzur, prince of the children of Manasseh:",
      "M": "On the eighth day Gamaliel son of Pedahzur, leader of Manasseh, offered his offering.",
      "T": "Day eight: Gamaliel son of Pedahzur, leader of Manasseh."
    },
    "55": {
      "L": "His offering was one silver charger of the weight of an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "56": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "57": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "58": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "59": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Gamaliel the son of Pedahzur.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Gamaliel son of Pedahzur.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Gamaliel son of Pedahzur's complete offering."
    },
    "60": {
      "L": "On the ninth day Abidan the son of Gideoni, prince of the children of Benjamin:",
      "M": "On the ninth day Abidan son of Gideoni, leader of Benjamin, offered his offering.",
      "T": "Day nine: Abidan son of Gideoni, leader of Benjamin."
    },
    "61": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "62": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "63": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "64": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "65": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Abidan the son of Gideoni.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Abidan son of Gideoni.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Abidan son of Gideoni's complete offering."
    },
    "66": {
      "L": "On the tenth day Ahiezer the son of Ammishaddai, prince of the children of Dan:",
      "M": "On the tenth day Ahiezer son of Ammishaddai, leader of Dan, offered his offering.",
      "T": "Day ten: Ahiezer son of Ammishaddai, leader of Dan."
    },
    "67": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "68": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "69": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "70": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "71": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Ahiezer the son of Ammishaddai.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Ahiezer son of Ammishaddai.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Ahiezer son of Ammishaddai's complete offering."
    },
    "72": {
      "L": "On the eleventh day Pagiel the son of Ocran, prince of the children of Asher:",
      "M": "On the eleventh day Pagiel son of Ocran, leader of Asher, offered his offering.",
      "T": "Day eleven: Pagiel son of Ocran, leader of Asher."
    },
    "73": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "74": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "75": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "76": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "77": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Pagiel the son of Ocran.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Pagiel son of Ocran.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Pagiel son of Ocran's complete offering."
    },
    "78": {
      "L": "On the twelfth day Ahira the son of Enan, prince of the children of Naphtali:",
      "M": "On the twelfth day Ahira son of Enan, leader of Naphtali, offered his offering.",
      "T": "Day twelve: Ahira son of Enan, leader of Naphtali."
    },
    "79": {
      "L": "His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a grain offering:",
      "M": "His offering was one silver dish weighing 130 shekels and one silver basin of 70 shekels, by the sanctuary shekel — both filled with fine flour mixed with oil as a grain offering;",
      "T": "One silver dish of 130 shekels, one silver basin of 70 shekels — sanctuary weight, both filled with fine flour blended with oil as a grain offering;"
    },
    "80": {
      "L": "One golden spoon of ten shekels, full of incense:",
      "M": "one gold pan of 10 shekels, full of incense;",
      "T": "one gold ladle of 10 shekels, filled with incense;"
    },
    "81": {
      "L": "One young bullock, one ram, one lamb of the first year, for a burnt offering:",
      "M": "one bull, one ram, one yearling male lamb — for a burnt offering;",
      "T": "one bull, one ram, one yearling lamb — all for the burnt offering;"
    },
    "82": {
      "L": "One kid of the goats for a sin offering:",
      "M": "one male goat — for a sin offering;",
      "T": "one male goat — the sin offering;"
    },
    "83": {
      "L": "And for a sacrifice of peace offerings, two oxen, five rams, five he goats, five lambs of the first year: this was the offering of Ahira the son of Enan.",
      "M": "and for the fellowship offering: two oxen, five rams, five male goats, five yearling lambs. This was the offering of Ahira son of Enan.",
      "T": "and for the fellowship offering: two bulls, five rams, five male goats, five yearling lambs. This was Ahira son of Enan's complete offering — the last of the twelve."
    },
    "84": {
      "L": "This was the dedication of the altar, in the day when it was anointed, by the princes of Israel: twelve chargers of silver, twelve silver bowls, twelve spoons of gold:",
      "M": "This was the dedication offering for the altar at its anointing, brought by the leaders of Israel: twelve silver dishes, twelve silver basins, twelve gold pans.",
      "T": "The twelve-day dedication of the altar yielded this: twelve silver dishes, twelve silver basins, twelve gold incense ladles — one set per tribe, identical in every case."
    },
    "85": {
      "L": "Each charger of silver weighing an hundred and thirty shekels, each bowl seventy: all the silver vessels weighed two thousand and four hundred shekels, after the shekel of the sanctuary:",
      "M": "Each silver dish weighed 130 shekels and each basin 70. All the silver vessels together: 2,400 shekels by the sanctuary shekel.",
      "T": "Each dish: 130 shekels; each basin: 70 shekels. Total silver: 2,400 sanctuary shekels — a precise accounting before the LORD."
    },
    "86": {
      "L": "The golden spoons were twelve, full of incense, weighing ten shekels apiece, after the shekel of the sanctuary: all the gold of the spoons was an hundred and twenty shekels:",
      "M": "The twelve gold pans, each full of incense and weighing 10 shekels by the sanctuary shekel — all the gold of the pans amounted to 120 shekels.",
      "T": "Twelve gold ladles at 10 shekels each, all filled with incense: 120 shekels of gold total — the fragrance of twelve tribes rising before God."
    },
    "87": {
      "L": "All the oxen for the burnt offering were twelve bullocks, the rams twelve, the lambs of the first year twelve, with their meat offering: and the kids of the goats for sin offering twelve:",
      "M": "All the animals for the burnt offering: twelve bulls, twelve rams, twelve yearling male lambs with their grain offerings. For the sin offering: twelve male goats.",
      "T": "The burnt offerings in total: twelve bulls, twelve rams, twelve yearling lambs with accompanying grain offerings. Sin offerings: twelve male goats — one tribe's guilt, one tribe's atonement, twelve times over."
    },
    "88": {
      "L": "And all the oxen for the sacrifice of the peace offerings were twenty and four bullocks, the rams sixty, the he goats sixty, the lambs of the first year sixty. This was the dedication of the altar, after that it was anointed.",
      "M": "All the animals for the fellowship offering: twenty-four bulls, sixty rams, sixty male goats, sixty yearling lambs. This was the dedication offering for the altar after it was anointed.",
      "T": "The fellowship offerings in total: 24 bulls, 60 rams, 60 male goats, 60 yearling lambs. This was the complete dedication of the altar. Twelve days, twelve tribes, one consecrated altar — Israel united in worship."
    },
    "89": {
      "L": "And when Moses was gone into the tabernacle of the congregation to speak with him, then he heard the voice of one speaking unto him from off the mercy seat that was upon the ark of testimony, from between the two cherubims: and he spake unto him.",
      "M": "When Moses went into the tent of meeting to speak with the LORD, he heard the voice speaking to him from above the atonement cover that was on the ark of the covenant document, from between the two cherubim. And the LORD spoke to him.",
      "T": "When Moses entered the tent of meeting to speak with God, he heard the voice coming from above the mercy seat — from between the two cherubim over the ark of the covenant. The LORD spoke to him from that place, face to presence."
    }
  },
  "8": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto Aaron, and say unto him, When thou lightest the lamps, the seven lamps shall give light over against the candlestick.",
      "M": "Speak to Aaron and tell him: When you set up the lamps, the seven lamps are to light the space in front of the lampstand.",
      "T": "Tell Aaron: when he mounts the seven lamps, they are to cast their light forward — illuminating the space before the lampstand itself."
    },
    "3": {
      "L": "And Aaron did so; he lighted the lamps thereof over against the candlestick, as the LORD commanded Moses.",
      "M": "Aaron did so; he set up the lamps to face the front of the lampstand, as the LORD had commanded Moses.",
      "T": "Aaron obeyed — he arranged the lamps to shine forward, exactly as the LORD had commanded Moses."
    },
    "4": {
      "L": "And this work of the candlestick was of beaten gold, unto the shaft thereof, unto the flowers thereof, was beaten work: according unto the pattern which the LORD had shewed Moses, so he made the candlestick.",
      "M": "The lampstand was made of hammered gold from its base to its blossoms — all of beaten work, made according to the pattern the LORD had shown Moses.",
      "T": "The lampstand was hammered gold throughout — shaft to blossoms, every part beaten from a single piece — exactly matching the design the LORD had shown Moses on the mountain."
    },
    "5": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "6": {
      "L": "Take the Levites from among the children of Israel, and cleanse them.",
      "M": "Take the Levites from among the Israelites and cleanse them.",
      "T": "Separate the Levites from the rest of Israel and purify them."
    },
    "7": {
      "L": "And thus shalt thou do unto them, to cleanse them: Sprinkle water of purifying upon them, and let them shave all their flesh, and let them wash their clothes, and so make themselves clean.",
      "M": "This is how you shall cleanse them: sprinkle purification water on them; have them shave their whole body, wash their clothes, and so make themselves clean.",
      "T": "The purification rite: sprinkle cleansing water over them, have them shave their entire body, wash their garments — and they will be clean."
    },
    "8": {
      "L": "Then let them take a young bullock with his meat offering, even fine flour mingled with oil, and another young bullock shalt thou take for a sin offering.",
      "M": "Then they shall take a young bull with its grain offering of fine flour mixed with oil, and you shall take a second young bull for a sin offering.",
      "T": "They are then to bring two young bulls: one as a burnt offering with a fine-flour-and-oil grain offering alongside it, and one as a sin offering."
    },
    "9": {
      "L": "And thou shalt bring the Levites before the tabernacle of the congregation: and thou shalt gather the whole assembly of the children of Israel together:",
      "M": "You shall bring the Levites before the tent of meeting and assemble the whole community of Israel.",
      "T": "Bring the Levites to the tent of meeting entrance and gather all Israel around them."
    },
    "10": {
      "L": "And thou shalt bring the Levites before the LORD: and the children of Israel shall put their hands upon the Levites:",
      "M": "You shall present the Levites before the LORD, and the Israelites shall lay their hands on the Levites.",
      "T": "Present the Levites before the LORD. Then the whole Israelite assembly shall lay their hands on the Levites —"
    },
    "11": {
      "L": "And Aaron shall offer the Levites before the LORD for an offering of the children of Israel, that they may execute the service of the LORD.",
      "M": "and Aaron shall present the Levites before the LORD as a wave offering from the Israelites, so that they may carry out the LORD's service.",
      "T": "and Aaron shall present them to the LORD as a wave offering on Israel's behalf — a living gift dedicated to the LORD's service."
    },
    "12": {
      "L": "And the Levites shall lay their hands upon the heads of the bullocks: and thou shalt offer the one for a sin offering, and the other for a burnt offering, unto the LORD, to make an atonement for the Levites.",
      "M": "The Levites shall lay their hands on the heads of the bulls; and you shall offer one as a sin offering and the other as a burnt offering to the LORD, to make atonement for the Levites.",
      "T": "The Levites press their hands on the bulls' heads, transferring guilt. One bull becomes the sin offering, one the burnt offering — atonement for the Levites before they enter service."
    },
    "13": {
      "L": "And thou shalt set the Levites before Aaron, and before his sons, and offer them for an offering unto the LORD.",
      "M": "You shall station the Levites before Aaron and his sons and present them as a wave offering to the LORD.",
      "T": "Station the Levites before Aaron and his sons and lift them as a dedicated offering to the LORD."
    },
    "14": {
      "L": "Thus shalt thou separate the Levites from among the children of Israel: and the Levites shall be mine.",
      "M": "In this way you shall set the Levites apart from the Israelites, and the Levites shall be mine.",
      "T": "This is how the Levites are formally distinguished from the rest of Israel — they belong to the LORD."
    },
    "15": {
      "L": "And after that shall the Levites go in to do the service of the tabernacle of the congregation: and thou shalt cleanse them, and offer them for an offering.",
      "M": "After this, the Levites shall come to serve at the tent of meeting. You shall cleanse them and present them as a wave offering.",
      "T": "After the purification and the presentation, the Levites may take up their service at the tent of meeting."
    },
    "16": {
      "L": "For they are wholly given unto me from among the children of Israel; instead of such as open every womb, even instead of the firstborn of all the children of Israel, have I taken them unto me.",
      "M": "For they are wholly given to me from among the Israelites. I have taken them for myself in place of all who first open the womb — in place of every firstborn among the Israelites.",
      "T": "The Levites belong entirely to me. I have taken them as a substitute for every firstborn son in Israel — every firstborn who opened a womb in the land."
    },
    "17": {
      "L": "For all the firstborn of the children of Israel are mine, both man and beast: on the day that I smote every firstborn in the land of Egypt I sanctified them for myself.",
      "M": "For every firstborn among the Israelites is mine, both human and animal. On the day I struck every firstborn in Egypt I set them apart for myself.",
      "T": "Every Israelite firstborn — human and animal — belongs to me. The day I struck Egypt's firstborn, I consecrated Israel's firstborn as my own."
    },
    "18": {
      "L": "And I have taken the Levites for all the firstborn of the children of Israel.",
      "M": "And I have taken the Levites in place of all the firstborn among the Israelites.",
      "T": "Now the Levites stand in the place of those firstborns — given to me instead."
    },
    "19": {
      "L": "And I have given the Levites as a gift to Aaron and to his sons from among the children of Israel, to do the service of the children of Israel in the tabernacle of the congregation, and to make an atonement for the children of Israel: that there be no plague among the children of Israel, when the children of Israel come nigh unto the sanctuary.",
      "M": "I have given the Levites as a gift to Aaron and his sons from among the Israelites, to serve on behalf of the Israelites at the tent of meeting and to make atonement for them, so that no plague strikes the Israelites when they approach the sanctuary.",
      "T": "I give the Levites to Aaron and his sons as a gift — assigned from Israel to serve Israel at the tent of meeting and to provide atonement, so that approaching the holy sanctuary does not cost Israel their lives."
    },
    "20": {
      "L": "And Moses, and Aaron, and all the congregation of the children of Israel, did to the Levites according unto all that the LORD commanded Moses concerning the Levites, so did the children of Israel unto them.",
      "M": "Moses, Aaron, and the whole community of Israel did to the Levites everything the LORD commanded Moses about them. The Israelites did this to the Levites.",
      "T": "Moses, Aaron, and the entire community of Israel carried out everything the LORD had commanded regarding the Levites — without exception."
    },
    "21": {
      "L": "And the Levites were purified, and they washed their clothes; and Aaron offered them as an offering before the LORD; and Aaron made an atonement for them to cleanse them.",
      "M": "The Levites purified themselves and washed their clothes. Aaron presented them as a wave offering before the LORD and made atonement for them to cleanse them.",
      "T": "The Levites underwent purification, washed their garments, and Aaron waved them before the LORD and made atonement for them. They were clean."
    },
    "22": {
      "L": "And after that went the Levites in to do their service in the tabernacle of the congregation before Aaron, and before his sons: as the LORD had commanded Moses concerning the Levites, so did they unto them.",
      "M": "After this the Levites went in to perform their service at the tent of meeting, before Aaron and his sons, just as the LORD had commanded Moses about the Levites — so it was done.",
      "T": "From that day on, the Levites took up their duties at the tent of meeting under Aaron and his sons — everything performed exactly as the LORD had commanded."
    },
    "23": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "24": {
      "L": "This is it that belongeth unto the Levites: from twenty and five years old and upward they shall go in to wait upon the service of the tabernacle of the congregation:",
      "M": "This is what applies to the Levites: from twenty-five years old and upward they shall enter to serve in the work of the tent of meeting.",
      "T": "The Levites begin active service at age twenty-five — from that point they join the workforce of the tent of meeting."
    },
    "25": {
      "L": "And from the age of fifty years they shall cease waiting upon the service thereof, and shall serve no more:",
      "M": "And from age fifty they shall retire from the service work and serve no longer.",
      "T": "At fifty they retire from the strenuous labor and serve no more in that capacity."
    },
    "26": {
      "L": "But shall minister with their brethren in the tabernacle of the congregation, to keep the charge, and shall do no service. Thus shalt thou do unto the Levites touching their charge.",
      "M": "They may assist their fellow Levites at the tent of meeting by keeping the charge, but they shall perform no heavy work. This is how you shall assign the Levites' duties.",
      "T": "They may still assist their fellow Levites — helping, advising, keeping watch — but the heavy lifting is done. This is the Levites' life cycle of service."
    }
  },
  "9": {
    "1": {
      "L": "And the LORD spake unto Moses in the wilderness of Sinai, in the first month of the second year after they were come out of the land of Egypt, saying,",
      "M": "The LORD spoke to Moses in the wilderness of Sinai, in the first month of the second year after the exodus from Egypt, saying,",
      "T": "In the first month of the second year out of Egypt — still in the Sinai wilderness — the LORD spoke to Moses:"
    },
    "2": {
      "L": "Let the children of Israel also keep the passover at his appointed season.",
      "M": "Let the Israelites keep the Passover at its appointed time.",
      "T": "The Israelites are to observe the Passover at its appointed time."
    },
    "3": {
      "L": "In the fourteenth day of this month, at even, ye shall keep it in his appointed season: according to all the rites of it, and according to all the ceremonies thereof, shall ye keep it.",
      "M": "On the fourteenth day of this month, at twilight, you shall keep it at its appointed time, following all its statutes and all its ordinances.",
      "T": "On the fourteenth day of this month, at twilight, observe it — every rite, every ordinance, exactly as established."
    },
    "4": {
      "L": "And Moses spake unto the children of Israel, that they should keep the passover.",
      "M": "Moses told the Israelites to keep the Passover.",
      "T": "Moses relayed this to the Israelites, and they prepared to keep the Passover."
    },
    "5": {
      "L": "And they kept the passover on the fourteenth day of the first month at even in the wilderness of Sinai: according to all that the LORD commanded Moses, so did the children of Israel.",
      "M": "They kept the Passover on the fourteenth day of the first month at twilight in the wilderness of Sinai. The Israelites did everything the LORD had commanded Moses.",
      "T": "On the fourteenth day of the first month, at twilight, in the Sinai wilderness, the Israelites kept the Passover — every detail as the LORD had commanded."
    },
    "6": {
      "L": "And there were certain men, who were defiled by the dead body of a man, that they could not keep the passover on that day: and they came before Moses and before Aaron on that day:",
      "M": "But there were some men who were ceremonially unclean because of a human corpse and could not keep the Passover on that day. They came before Moses and Aaron that day",
      "T": "Some men, however, were impure from contact with a human corpse and could not join the Passover. They came to Moses and Aaron that day —"
    },
    "7": {
      "L": "And those men said unto him, We are defiled by the dead body of a man: wherefore are we kept back, that we may not offer an offering of the LORD in his appointed season among the children of Israel?",
      "M": "and said to him, We are unclean because of a corpse. Why should we be excluded from bringing the LORD's offering at its appointed time among the Israelites?",
      "T": "and said: 'We are impure from handling the dead. Why should we be shut out from offering to the LORD at the time appointed for all Israel?'"
    },
    "8": {
      "L": "And Moses said unto them, Stand still, and I will hear what the LORD will command concerning you.",
      "M": "Moses said to them, Wait here, and I will hear what the LORD commands about you.",
      "T": "Moses said: 'Wait. I will take your case to the LORD and hear what he says.'"
    },
    "9": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "10": {
      "L": "Speak unto the children of Israel, saying, If any man of you or of your posterity shall be unclean by reason of a dead body, or be in a journey afar off, yet he shall keep the passover unto the LORD.",
      "M": "Tell the Israelites: If any of you or your descendants is unclean because of a corpse, or is away on a long journey, he may still keep the Passover to the LORD.",
      "T": "Tell Israel: if anyone is impure from a corpse, or is on a long journey at Passover time, they are not simply excluded — they may still keep the Passover to the LORD."
    },
    "11": {
      "L": "The fourteenth day of the second month at even they shall keep it, and eat it with unleavened bread and bitter herbs.",
      "M": "They shall keep it on the fourteenth day of the second month at twilight, eating it with unleavened bread and bitter herbs.",
      "T": "They observe it one month later: the fourteenth of the second month, at twilight — with unleavened bread and bitter herbs, the full Passover meal."
    },
    "12": {
      "L": "They shall leave none of it unto the morning, nor break any bone of it: according to all the ordinances of the passover they shall keep it.",
      "M": "They shall leave none of it until morning and shall not break any of its bones. They shall observe it according to all the statutes of the Passover.",
      "T": "No leftovers into morning, no broken bones — the make-up Passover follows every regulation of the original."
    },
    "13": {
      "L": "But the man that is clean, and is not in a journey, and forbeareth to keep the passover, even the same soul shall be cut off from among his people: because he brought not the offering of the LORD in his appointed season, the man shall bear his sin.",
      "M": "But the man who is clean and not on a journey and yet fails to keep the Passover — that person shall be cut off from among his people. Because he did not bring the LORD's offering at the appointed time, that man shall bear his guilt.",
      "T": "But a person who is clean and not traveling and simply neglects the Passover — that person is cut off from Israel. Skipping the appointed offering without cause is a rejection of the covenant; the guilt rests on him alone."
    },
    "14": {
      "L": "And if a stranger shall sojourn among you, and will keep the passover unto the LORD; according to the ordinance of the passover, and according to the manner thereof, so shall he do: ye shall have one ordinance, both for the stranger, and for him that was born in the land.",
      "M": "If a foreigner residing among you wants to keep the Passover to the LORD, he must do so according to the statutes and ordinances of the Passover. You shall have one statute, both for the resident alien and for the native-born.",
      "T": "If a foreigner living among Israel wants to keep the Passover to the LORD, let him — but he must observe every regulation of it. One law, one table: resident alien and native-born stand equal before this feast."
    },
    "15": {
      "L": "And on the day that the tabernacle was reared up the cloud covered the tabernacle, namely, the tent of the testimony: and at even there was upon the tabernacle as it were the appearance of fire, until the morning.",
      "M": "On the day the tabernacle was set up, the cloud covered the tabernacle — the tent of the covenant document — and at evening it appeared over the tabernacle like fire until morning.",
      "T": "The day the tabernacle was erected, the cloud settled over it — the tent housing the covenant. From evening onward it appeared as fire, glowing through the night until dawn."
    },
    "16": {
      "L": "So it was alway: the cloud covered it by day, and the appearance of fire by night.",
      "M": "This was the regular pattern: the cloud covered it by day and the appearance of fire by night.",
      "T": "This was constant: cloud by day, fire by night — the LORD's visible presence, never absent."
    },
    "17": {
      "L": "And when the cloud was taken up from the tabernacle, then after that the children of Israel journeyed: and in the place where the cloud abode, there the children of Israel pitched their tents.",
      "M": "Whenever the cloud lifted from above the tabernacle, the Israelites set out. And wherever the cloud settled, there the Israelites camped.",
      "T": "When the cloud lifted, Israel moved. When the cloud settled, Israel stopped and made camp. The cloud was their compass and their command."
    },
    "18": {
      "L": "At the commandment of the LORD the children of Israel journeyed, and at the commandment of the LORD they pitched: as long as the cloud abode upon the tabernacle they rested in their tents.",
      "M": "At the LORD's command the Israelites set out, and at the LORD's command they camped. As long as the cloud rested over the tabernacle, they stayed in camp.",
      "T": "March and rest — both were ordered by the LORD. As long as the cloud stayed, they stayed; when it moved, they moved."
    },
    "19": {
      "L": "And when the cloud tarried long upon the tabernacle many days, then the children of Israel kept the charge of the LORD, and journeyed not.",
      "M": "When the cloud remained over the tabernacle for many days, the Israelites kept the LORD's charge and did not set out.",
      "T": "When the cloud lingered for many days, Israel held its position — keeping watch, keeping faith, going nowhere until the LORD said otherwise."
    },
    "20": {
      "L": "And so it was, when the cloud was a few days upon the tabernacle; according to the commandment of the LORD they abode in their tents, and according to the commandment of the LORD they journeyed.",
      "M": "Sometimes the cloud remained over the tabernacle for only a few days; at the LORD's command they remained in camp, and at the LORD's command they set out.",
      "T": "When the cloud stayed only a few days, they stayed a few days — then moved at the LORD's signal. Short stop or long stop: always his call."
    },
    "21": {
      "L": "And so it was, when the cloud abode from even unto the morning, and that the cloud was taken up in the morning, then they journeyed: whether it was by day or by night that the cloud was taken up, they journeyed.",
      "M": "Sometimes the cloud remained only from evening until morning; when the cloud lifted in the morning, they set out. Whether by day or by night the cloud lifted, they set out.",
      "T": "Even a cloud that settled at evening and lifted by morning was command enough — they broke camp and marched. Day departure or night departure: they followed."
    },
    "22": {
      "L": "Or whether it were two days, or a month, or a year, that the cloud tarried upon the tabernacle, remaining thereon, the children of Israel abode in their tents, and journeyed not: but when it was taken up, they journeyed.",
      "M": "Whether the cloud remained for two days, a month, or a year over the tabernacle, the Israelites stayed in camp and did not set out. But when it lifted, they set out.",
      "T": "Two days, a month, a year — length made no difference. Israel waited as long as the cloud stayed, then moved the moment it lifted. Their calendar was the presence of God."
    },
    "23": {
      "L": "At the commandment of the LORD they rested in the tents, and at the commandment of the LORD they journeyed: they kept the charge of the LORD, at the commandment of the LORD by the hand of Moses.",
      "M": "At the LORD's command they camped, and at the LORD's command they set out. They kept the LORD's charge at the LORD's command through Moses.",
      "T": "Camp and march — always at the LORD's command, always through Moses. This was the discipline of a people learning to be led by God."
    }
  },
  "10": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Make thee two trumpets of silver; of a whole piece shalt thou make them: that thou mayest use them for the calling of the assembly, and for the journeying of the camps.",
      "M": "Make two silver trumpets; make them of hammered silver. They shall serve to summon the assembly and to signal the camps to set out.",
      "T": "Make two trumpets of hammered silver — for calling the assembly to gather and for signaling the camps to march."
    },
    "3": {
      "L": "And when they shall blow with them, both the trumpets shall sound, that all the assembly shall assemble themselves to thee at the door of the tabernacle of the congregation.",
      "M": "When both are blown, the whole assembly shall gather to you at the entrance of the tent of meeting.",
      "T": "Both trumpets sounding together: the signal for the entire assembly to gather at the tent of meeting entrance."
    },
    "4": {
      "L": "And if they blow but with one trumpet, then the princes, which are heads of the thousands of Israel, shall gather themselves unto thee.",
      "M": "If only one is blown, only the leaders — the heads of Israel's thousands — shall gather to you.",
      "T": "One trumpet only: the leaders assemble, not the whole people. Different calls carry different summons."
    },
    "5": {
      "L": "When ye blow an alarm, then the camps that lie on the east parts shall take their journey.",
      "M": "When you blow an alarm, the camps on the east side shall set out.",
      "T": "A blast alarm: the eastern camps break camp and march."
    },
    "6": {
      "L": "When ye blow an alarm the second time, then the camps that lie on the south side shall take their journey: they shall blow an alarm for their journeys.",
      "M": "When you blow an alarm a second time, the camps on the south side shall set out. An alarm shall be sounded for each journey.",
      "T": "A second alarm: the southern camps march. Each departure from camp is announced this way."
    },
    "7": {
      "L": "But when the congregation is to be gathered together, ye shall blow, but ye shall not sound an alarm.",
      "M": "But when the assembly is to be gathered, you shall blow without an alarm call.",
      "T": "When gathering the assembly — not departing, just meeting — blow the trumpets without the alarm pattern."
    },
    "8": {
      "L": "And the sons of Aaron, the priests, shall blow with the trumpets; and they shall be to you for an ordinance for ever throughout your generations.",
      "M": "The priests, the sons of Aaron, shall blow the trumpets. This shall be a permanent statute throughout your generations.",
      "T": "The trumpets belong to Aaron's sons — only priests may sound them. This is a permanent ordinance through every generation."
    },
    "9": {
      "L": "And if ye go to war in your land against the enemy that oppresseth you, then ye shall blow an alarm with the trumpets; and ye shall be remembered before the LORD your God, and ye shall be saved from your enemies.",
      "M": "When you go to war in your land against an enemy who attacks you, sound an alarm with the trumpets. You will be remembered before the LORD your God and saved from your enemies.",
      "T": "When you go to war in your land and face an enemy pressing down on you — sound the alarm. The sound will rise before the LORD your God; he will remember you and you will be delivered."
    },
    "10": {
      "L": "Also in the day of your gladness, and in your solemn days, and in the beginnings of your months, ye shall blow with the trumpets over your burnt offerings, and over the sacrifices of your peace offerings; that they shall be to you for a memorial before your God: I am the LORD your God.",
      "M": "On your joyful days — your appointed festivals and the beginnings of your months — you shall blow the trumpets over your burnt offerings and your fellowship offerings. They will be a reminder before your God. I am the LORD your God.",
      "T": "Blow the trumpets also on joyful days — festivals, new moon celebrations — over the burnt offerings and fellowship sacrifices. The sound announces your worship before God and calls his attention to you. I am the LORD your God."
    },
    "11": {
      "L": "And it came to pass on the twentieth day of the second month, in the second year, that the cloud was taken up from off the tabernacle of the testimony.",
      "M": "On the twentieth day of the second month of the second year, the cloud lifted from above the tabernacle of the covenant.",
      "T": "On the twentieth day of the second month of the second year, the cloud over the tabernacle rose. It was time to leave Sinai."
    },
    "12": {
      "L": "And the children of Israel took their journeys out of the wilderness of Sinai; and the cloud rested in the wilderness of Paran.",
      "M": "The Israelites set out from the wilderness of Sinai, stage by stage, and the cloud came to rest in the wilderness of Paran.",
      "T": "Israel marched out of the Sinai wilderness in ordered stages, the cloud moving ahead of them until it settled in the Paran wilderness."
    },
    "13": {
      "L": "And they first took their journey according to the commandment of the LORD by the hand of Moses.",
      "M": "They set out for the first time at the LORD's command through Moses.",
      "T": "This was Israel's first march since the tabernacle's completion — ordered by the LORD through Moses."
    },
    "14": {
      "L": "In the first place went the standard of the camp of the children of Judah according to their armies: and over his host was Nahshon the son of Amminadab.",
      "M": "The standard of the camp of Judah set out first, by their regiments, with Nahshon son of Amminadab commanding their force.",
      "T": "Judah's division led the march, regiment by regiment. Nahshon son of Amminadab at the head."
    },
    "15": {
      "L": "And over the host of the tribe of Issachar was Nethaneel the son of Zuar.",
      "M": "Over the force of the tribe of Issachar was Nethaneel son of Zuar.",
      "T": "Issachar's regiment followed, under Nethaneel son of Zuar."
    },
    "16": {
      "L": "And over the host of the tribe of Zebulun was Eliab the son of Helon.",
      "M": "Over the force of the tribe of Zebulun was Eliab son of Helon.",
      "T": "Then Zebulun, under Eliab son of Helon."
    },
    "17": {
      "L": "And the tabernacle was taken down; and the sons of Gershon and the sons of Merari set forward, bearing the tabernacle.",
      "M": "The tabernacle was taken down, and the sons of Gershon and the sons of Merari set out, carrying the tabernacle.",
      "T": "Behind Judah came the Gershonites and Merarites, bearing the dismantled tabernacle — the structure moving with the people."
    },
    "18": {
      "L": "And the standard of the camp of Reuben set forward according to their armies: and over his host was Elizur the son of Shedeur.",
      "M": "The standard of the camp of Reuben set out by their regiments, with Elizur son of Shedeur commanding their force.",
      "T": "Next: Reuben's division, Elizur son of Shedeur commanding."
    },
    "19": {
      "L": "And over the host of the tribe of Simeon was Shelumiel the son of Zurishaddai.",
      "M": "Over the force of the tribe of Simeon was Shelumiel son of Zurishaddai.",
      "T": "Simeon followed, under Shelumiel son of Zurishaddai."
    },
    "20": {
      "L": "And over the host of the tribe of Gad was Eliasaph the son of Deuel.",
      "M": "Over the force of the tribe of Gad was Eliasaph son of Deuel.",
      "T": "Then Gad, under Eliasaph son of Deuel."
    },
    "21": {
      "L": "And the Kohathites set forward, bearing the sanctuary: and the other did set up the tabernacle against they came.",
      "M": "The Kohathites set out, carrying the holy objects. The others would set up the tabernacle before they arrived.",
      "T": "The Kohathites marched in the middle of the column carrying the sanctuary's sacred objects — ark, altars, lampstand. The Gershonites and Merarites ahead of them would have the tabernacle structure erected before the Kohathites arrived with the furnishings."
    },
    "22": {
      "L": "And the standard of the camp of the children of Ephraim set forward according to their armies: and over his host was Elishama the son of Ammihud.",
      "M": "The standard of the camp of Ephraim set out by their regiments, with Elishama son of Ammihud commanding their force.",
      "T": "Ephraim's division came next — Elishama son of Ammihud leading."
    },
    "23": {
      "L": "And over the host of the tribe of Manasseh was Gamaliel the son of Pedahzur.",
      "M": "Over the force of the tribe of Manasseh was Gamaliel son of Pedahzur.",
      "T": "Manasseh followed, under Gamaliel son of Pedahzur."
    },
    "24": {
      "L": "And over the host of the tribe of Benjamin was Abidan the son of Gideoni.",
      "M": "Over the force of the tribe of Benjamin was Abidan son of Gideoni.",
      "T": "Benjamin followed, under Abidan son of Gideoni."
    },
    "25": {
      "L": "And the standard of the camp of the children of Dan set forward, which was the rereward of all the camps throughout their hosts: and over his host was Ahiezer the son of Ammishaddai.",
      "M": "The standard of the camp of Dan set out — the rear guard of all the camps, by their regiments — with Ahiezer son of Ammishaddai commanding their force.",
      "T": "Dan's division brought up the rear — the rear guard of the entire column — Ahiezer son of Ammishaddai commanding."
    },
    "26": {
      "L": "And over the host of the tribe of Asher was Pagiel the son of Ocran.",
      "M": "Over the force of the tribe of Asher was Pagiel son of Ocran.",
      "T": "Asher followed, under Pagiel son of Ocran."
    },
    "27": {
      "L": "And over the host of the tribe of Naphtali was Ahira the son of Enan.",
      "M": "Over the force of the tribe of Naphtali was Ahira son of Enan.",
      "T": "Naphtali last, under Ahira son of Enan — and so the column closed."
    },
    "28": {
      "L": "Thus were the journeyings of the children of Israel according to their armies, when they set forward.",
      "M": "These were the marching orders of the Israelites, by their regiments, when they set out.",
      "T": "This was Israel's order of march — twelve tribes in sequence, a people on the move with their God."
    },
    "29": {
      "L": "And Moses said unto Hobab, the son of Raguel the Midianite, Moses' father in law, We are journeying unto the place of which the LORD said, I will give it you: come thou with us, and we will do thee good; for the LORD hath spoken good concerning Israel.",
      "M": "Moses said to Hobab son of Raguel the Midianite, Moses' father-in-law: We are setting out for the place the LORD said he would give us. Come with us and we will treat you well, for the LORD has promised good things to Israel.",
      "T": "Moses said to Hobab — son of Raguel, his kinsman by marriage — 'We are moving toward the land the LORD promised to give us. Come with us. We will treat you well, for the LORD has spoken good things over Israel.'"
    },
    "30": {
      "L": "And he said unto him, I will not go; but I will depart to mine own land, and to my kindred.",
      "M": "But he said to him, I will not go; I will return to my own land and my own people.",
      "T": "Hobab said: 'I will not come. I am going back to my own land, my own people.'"
    },
    "31": {
      "L": "And he said, Leave us not, I pray thee; forasmuch as thou knowest how we are to encamp in the wilderness, and thou mayest be to us instead of eyes.",
      "M": "Moses said, Please do not leave us, for you know how we are to camp in the wilderness, and you will serve as eyes for us.",
      "T": "Moses pressed him: 'Do not leave us, please. You know this wilderness — where to camp, where water is, what dangers lie ahead. You would be our eyes.'"
    },
    "32": {
      "L": "And it shall be, if thou go with us, yea, it shall be, that what goodness the LORD shall do unto us, the same will we do unto thee.",
      "M": "And if you come with us, whatever good the LORD does for us, we will share with you.",
      "T": "Come with us. Whatever blessing the LORD brings upon us, you will share in it."
    },
    "33": {
      "L": "And they departed from the mount of the LORD three days' journey: and the ark of the covenant of the LORD went before them in the three days' journey, to search out a resting place for them.",
      "M": "They set out from the mountain of the LORD on a three days' journey, with the ark of the LORD's covenant going before them on those three days to find a resting place for them.",
      "T": "They departed from Sinai — the mountain of the LORD — and traveled three days. The ark of the covenant went ahead of them those three days, scouting their resting place."
    },
    "34": {
      "L": "And the cloud of the LORD was upon them by day, when they went out of the camp.",
      "M": "The cloud of the LORD was over them by day when they set out from the camp.",
      "T": "By day, the LORD's cloud spread over them as they marched — shelter and presence both."
    },
    "35": {
      "L": "And it came to pass, when the ark set forward, that Moses said, Rise up, LORD, and let thine enemies be scattered; and let them that hate thee flee before thee.",
      "M": "Whenever the ark set out, Moses said: Rise up, LORD! Let your enemies be scattered; let those who hate you flee before you!",
      "T": "Each time the ark lifted and Israel began to march, Moses would call out: 'Rise, LORD! Let your enemies scatter! Let those who hate you turn and run before you!'"
    },
    "36": {
      "L": "And when it rested, he said, Return, O LORD, unto the many thousands of Israel.",
      "M": "And when it came to rest, he would say: Return, O LORD, to the countless thousands of Israel.",
      "T": "And when the ark settled and the camp was made, Moses said: 'Return, LORD — to the ten thousand thousands of Israel.' The prayers framed every march."
    }
  },
  "11": {
    "1": {
      "L": "And when the people complained, it displeased the LORD: and the LORD heard it; and his anger was kindled; and the fire of the LORD burnt among them, and consumed them that were in the uttermost parts of the camp.",
      "M": "The people complained in the hearing of the LORD about their hardships. When the LORD heard it, his anger was kindled, and fire from the LORD burned among them and consumed some who were at the edge of the camp.",
      "T": "The people began to complain — and the LORD heard it and his anger flared. Fire broke out from the LORD and burned along the edges of the camp, consuming those who had voiced the complaint."
    },
    "2": {
      "L": "And the people cried unto Moses; and when Moses prayed unto the LORD, the fire was quenched.",
      "M": "The people cried out to Moses, and when Moses prayed to the LORD, the fire died down.",
      "T": "The people cried to Moses. Moses prayed to the LORD, and the fire died."
    },
    "3": {
      "L": "And he called the name of that place Taberah: because the fire of the LORD burnt among them.",
      "M": "So that place was called Taberah, because fire from the LORD had burned among them.",
      "T": "The place was named Taberah — Burning — because the LORD's fire had burned there."
    },
    "4": {
      "L": "And the mixt multitude that was among them fell a lusting: and the children of Israel also wept again, and said, Who shall give us flesh to eat?",
      "M": "The mixed multitude among them had a strong craving, and the Israelites also wept again and said, Who will give us meat to eat?",
      "T": "The mixed crowd among them gave way to craving — and the craving spread. The Israelites wept and demanded: 'Who will give us meat?'"
    },
    "5": {
      "L": "We remember the fish, which we did eat in Egypt freely; the cucumbers, and the melons, and the leeks, and the onions, and the garlick:",
      "M": "We remember the fish we ate in Egypt free of charge — the cucumbers, the melons, the leeks, the onions, the garlic.",
      "T": "They remembered: 'In Egypt we had fish — free fish. Cucumbers, melons, leeks, onions, garlic —'"
    },
    "6": {
      "L": "But now our soul is dried away: there is nothing at all, beside this manna, before our eyes.",
      "M": "But now our appetite has withered; there is nothing at all to look at except this manna.",
      "T": "— 'and now our appetite has shriveled. There is nothing. Nothing except this manna, every day, nothing but manna.'"
    },
    "7": {
      "L": "And the manna was as coriander seed, and the colour thereof as the colour of bdellium.",
      "M": "The manna was like coriander seed and its appearance like the appearance of bdellium resin.",
      "T": "The manna was white as bdellium resin, small and round as coriander seed."
    },
    "8": {
      "L": "And the people went about, and gathered it, and ground it in mills, or beat it in a mortar, and baked it in pans, and made cakes of it: and the taste of it was as the taste of fresh oil.",
      "M": "The people went around gathering it; they ground it in mills or beat it in mortars, then cooked it in pots and made loaves from it. It tasted like rich oil.",
      "T": "People gathered it each morning, ground it in mills or crushed it in mortars, cooked it in pots or baked it into flat cakes. It tasted of rich olive oil. It was bread from heaven — and they were tired of it."
    },
    "9": {
      "L": "And when the dew fell upon the camp in the night, the manna fell upon it.",
      "M": "When the dew settled on the camp in the night, the manna settled with it.",
      "T": "It appeared with the dew every night, covering the camp by morning."
    },
    "10": {
      "L": "Then Moses heard the people weep throughout their families, every man in the door of his tent: and the anger of the LORD was kindled greatly; Moses also was displeased.",
      "M": "Moses heard the people weeping throughout their clans, everyone at the door of his tent. The anger of the LORD blazed hot, and Moses was also distressed.",
      "T": "Moses heard the sound of weeping rising from every family, from the entrance of every tent — a camp of grief and complaint. The LORD's anger blazed, and Moses himself was stricken."
    },
    "11": {
      "L": "And Moses said unto the LORD, Wherefore hast thou afflicted thy servant? and wherefore have I not found favour in thy sight, that thou layest the burden of all this people upon me?",
      "M": "Moses said to the LORD: Why have you brought this trouble on your servant? Why have I not found favor in your sight, that you lay the burden of all this people on me?",
      "T": "Moses cried out to the LORD: 'Why have you done this to me — your servant? What have I done to lose your favor? Why have you put the weight of all this people on my shoulders?'"
    },
    "12": {
      "L": "Have I conceived all this people? have I begotten them, that thou shouldest say unto me, Carry them in thy bosom, as a nursing father beareth the sucking child, unto the land which thou swarest unto their fathers?",
      "M": "Did I conceive all this people? Did I give birth to them, that you should say to me, Carry them in your arms, as a nursing father carries a nursing child, to the land you swore to their ancestors?",
      "T": "'Did I conceive this people? Did I give birth to them — that you tell me to carry them in my arms like a nursing mother carries an infant, all the way to the land you promised their fathers?'"
    },
    "13": {
      "L": "Whence should I have flesh to give unto all this people? for they weep unto me, saying, Give us flesh, that we may eat.",
      "M": "Where am I to get meat to give to all this people? For they weep before me and say, Give us meat to eat.",
      "T": "'Where am I supposed to get meat for six hundred thousand people who are weeping in my face demanding to be fed?'"
    },
    "14": {
      "L": "I am not able to bear all this people alone, because it is too heavy for me.",
      "M": "I am not able to carry all this people alone; it is too heavy for me.",
      "T": "'I cannot carry this people alone. The weight is crushing me.'"
    },
    "15": {
      "L": "And if thou deal thus with me, kill me, I pray thee, out of hand, if I have found favour in thy sight; and let me not see my wretchedness.",
      "M": "If this is how you are going to treat me, kill me right now — if I have found favor in your sight — and do not let me face my own ruin.",
      "T": "'If this is what you intend for me — if I truly have found favor with you — then kill me now. Do not let me watch myself fail. Death is better than this.'"
    },
    "16": {
      "L": "And the LORD said unto Moses, Gather unto me seventy men of the elders of Israel, whom thou knowest to be the elders of the people, and officers over them; and bring them unto the tabernacle of the congregation, that they may stand there with thee.",
      "M": "The LORD said to Moses: Gather for me seventy men from the elders of Israel — men you know to be elders and officers of the people — and bring them to the tent of meeting, so that they may stand there with you.",
      "T": "The LORD responded to Moses — not with rebuke but with a solution: 'Gather seventy men, known elders and officers of Israel, and bring them to the tent of meeting. They will stand with you.'"
    },
    "17": {
      "L": "And I will come down and talk with thee there: and I will take of the spirit which is upon thee, and will put it upon them; and they shall bear the burden of the people with thee, that thou bear it not thyself alone.",
      "M": "I will come down and speak with you there. I will take some of the spirit that is on you and put it on them. They will share the burden of the people with you so that you do not carry it alone.",
      "T": "'I will come down and speak with you there. I will take of the Spirit that rests on you and distribute it among them — and they will share the burden of leading this people, so you are not carrying it alone.'"
    },
    "18": {
      "L": "And say thou unto the people, Sanctify yourselves against to morrow, and ye shall eat flesh: for ye have wept in the ears of the LORD, saying, Who shall give us flesh to eat? for it was well with us in Egypt: therefore the LORD will give you flesh, and ye shall eat.",
      "M": "And say to the people: Consecrate yourselves for tomorrow, and you will eat meat. For you have wept in the LORD's hearing and said, Who will give us meat to eat? It was better for us in Egypt. Therefore the LORD will give you meat, and you will eat.",
      "T": "'And tell the people: prepare yourselves for tomorrow — you will eat meat. You have wept in the LORD's ears, insisting Egypt was better. Fine. The LORD will give you what you demand.'"
    },
    "19": {
      "L": "Ye shall not eat one day, nor two days, nor five days, neither ten days, nor twenty days;",
      "M": "You will not eat it for just one day, or two days, or five days, or ten days, or twenty days,",
      "T": "'Not one day, not two, not five, not ten, not twenty —'"
    },
    "20": {
      "L": "But even a whole month, until it come out at your nostrils, and it be loathsome unto you: because that ye have despised the LORD which is among you, and have wept before him, saying, Why came we forth out of Egypt?",
      "M": "but a whole month, until it comes out of your nostrils and becomes repulsive to you — because you have rejected the LORD who is among you and have wept before him, saying, Why did we ever leave Egypt?",
      "T": "'— but a full month, until meat is coming out of your nostrils and you are sick of it. Because you have despised the LORD who is living among you and wept as though Egypt was life and Sinai was death.'"
    },
    "21": {
      "L": "And Moses said, The people, among whom I am, are six hundred thousand footmen; and thou hast said, I will give them flesh, that they may eat a whole month.",
      "M": "But Moses said: The people I am among number six hundred thousand foot soldiers, and you have said, I will give them meat to eat for a whole month!",
      "T": "Moses pressed back: 'Six hundred thousand fighting men — not counting women and children. You are saying you will give all of them meat for a solid month?'"
    },
    "22": {
      "L": "Shall the flocks and the herds be slain for them, to suffice them? or shall all the fish of the sea be gathered together for them, to suffice them?",
      "M": "Would enough flocks and herds be slaughtered to provide for them? Would all the fish of the sea be gathered together to provide for them?",
      "T": "'Slaughter every flock and herd — would that be enough? Drain the sea of its fish — would that be enough?'"
    },
    "23": {
      "L": "And the LORD said unto Moses, Is the LORD'S hand waxed short? thou shalt see now whether my word shall come to pass unto thee or not.",
      "M": "The LORD said to Moses: Is the LORD's hand too short? Now you will see whether my word comes true for you or not.",
      "T": "The LORD answered Moses: 'Is my arm too short? You will see today whether what I say happens or not.'"
    },
    "24": {
      "L": "And Moses went out, and told the people the words of the LORD, and gathered the seventy men of the elders of the people, and set them round about the tabernacle.",
      "M": "Moses went out and told the people the LORD's words, then gathered seventy of the elders of the people and positioned them around the tent.",
      "T": "Moses went out, relayed the LORD's words to the people, and then gathered the seventy elders and positioned them in a circle around the tent of meeting."
    },
    "25": {
      "L": "And the LORD came down in a cloud, and spake unto him, and took of the spirit that was upon him, and gave it unto the seventy elders: and it came to pass, that, when the spirit rested upon them, they prophesied, and did not cease.",
      "M": "Then the LORD came down in the cloud and spoke to him. He took some of the spirit that was on Moses and gave it to the seventy elders. When the spirit rested on them, they prophesied — but they did so only that once.",
      "T": "The LORD came down in the cloud and spoke with Moses. He took of the Spirit that rested on Moses and distributed it among the seventy elders. When the Spirit came to rest on each of them, they prophesied — a single outpouring, a sign that the Spirit had come."
    },
    "26": {
      "L": "But there remained two of the men in the camp, the name of the one was Eldad, and the name of the other Medad: and the spirit rested upon them; and they were of them that were written, but went not out unto the tabernacle: and they prophesied in the camp.",
      "M": "Two men had remained in the camp — one named Eldad and the other Medad. The spirit rested on them as well; they were among those registered but had not gone out to the tent. And they prophesied in the camp.",
      "T": "Two of the seventy — Eldad and Medad — had not come out to the tent. They were on the list; the Spirit came to them where they were. They prophesied right there in the camp."
    },
    "27": {
      "L": "And there ran a young man, and told Moses, and said, Eldad and Medad do prophesy in the camp.",
      "M": "A young man ran and told Moses: Eldad and Medad are prophesying in the camp!",
      "T": "A young man ran to Moses: 'Eldad and Medad — they're prophesying in the camp!'"
    },
    "28": {
      "L": "And Joshua the son of Nun, the servant of Moses, one of his young men, answered and said, My lord Moses, forbid them.",
      "M": "Joshua son of Nun, who had been Moses' assistant since his youth, said: My lord Moses, stop them!",
      "T": "Joshua son of Nun — Moses' aide from his youth — spoke up: 'My lord Moses, put a stop to this!'"
    },
    "29": {
      "L": "And Moses said unto him, Enviest thou for my sake? would God that all the LORD'S people were prophets, and that the LORD would put his spirit upon them!",
      "M": "Moses said to him: Are you jealous on my behalf? Would that all the LORD's people were prophets and that the LORD would put his spirit on them!",
      "T": "Moses said: 'Are you protecting my reputation? Don't. I wish all the LORD's people were prophets — that the LORD would pour out his Spirit on every one of them!'"
    },
    "30": {
      "L": "And Moses gat him into the camp, he and the elders of Israel.",
      "M": "Then Moses and the elders of Israel returned to the camp.",
      "T": "Moses and the elders returned to the camp."
    },
    "31": {
      "L": "And there went forth a wind from the LORD, and brought quails from the sea, and let them fall by the camp, as it were a day's journey on this side, and as it were a day's journey on the other side, round about the camp, and as it were two cubits high upon the face of the earth.",
      "M": "Then a wind went out from the LORD and drove quails from the sea. It dropped them beside the camp — a day's journey in every direction around the camp, about three feet deep on the surface of the ground.",
      "T": "A great wind from the LORD swept quails in from the sea and dumped them around the camp — a day's journey out in every direction, lying thick on the ground to a depth of about three feet."
    },
    "32": {
      "L": "And the people stood up all that day, and all that night, and all the next day, and they gathered the quails: he that gathered least gathered ten homers: and they spread them all abroad for themselves round about the camp.",
      "M": "The people spent all that day, all that night, and all the next day gathering quails. The least any one gathered was ten homers. They spread them out around the camp to dry.",
      "T": "All day, all night, all the next day — the people gathered quails in a frenzy. Even the smallest haul was ten homers. They spread them out around the camp to dry in the sun."
    },
    "33": {
      "L": "And while the flesh was yet between their teeth, ere it was chewed, the wrath of the LORD was kindled against the people, and the LORD smote the people with a very great plague.",
      "M": "While the meat was still between their teeth, before it was chewed, the anger of the LORD blazed against the people, and the LORD struck the people with a very great plague.",
      "T": "The meat was still in their mouths — not yet swallowed — when the LORD's anger broke over the camp. He struck the people with a devastating plague."
    },
    "34": {
      "L": "And he called the name of that place Kibrothhattaavah: because there they buried the people that lusted.",
      "M": "So that place was called Kibroth-hattaavah — the Graves of Craving — because there they buried the people who had craved.",
      "T": "The place was named Kibroth-hattaavah — Graves of Craving — because the people who craved were buried there."
    },
    "35": {
      "L": "And the people journeyed from Kibrothhattaavah unto Hazeroth; and abode at Hazeroth.",
      "M": "From Kibroth-hattaavah the people traveled to Hazeroth, and they stayed at Hazeroth.",
      "T": "From Graves of Craving, Israel moved on to Hazeroth, where they stopped and made camp."
    }
  },
  "12": {
    "1": {
      "L": "And Miriam and Aaron spake against Moses because of the Ethiopian woman whom he had married: for he had married an Ethiopian woman.",
      "M": "Miriam and Aaron spoke against Moses because of the Cushite woman he had married — for he had married a Cushite woman.",
      "T": "Miriam and Aaron turned on Moses over his Cushite wife — he had married a Cushite woman, and they made it the occasion for a broader challenge to his authority."
    },
    "2": {
      "L": "And they said, Hath the LORD indeed spoken only by Moses? hath he not spoken also by us? And the LORD heard it.",
      "M": "They said: Has the LORD spoken only through Moses? Has he not also spoken through us? And the LORD heard it.",
      "T": "'Has the LORD spoken only through Moses? Has he not spoken through us as well?' The LORD heard every word."
    },
    "3": {
      "L": "Now the man Moses was very meek, above all the men which were upon the face of the earth.",
      "M": "Now Moses was a very humble man, more humble than anyone else on the face of the earth.",
      "T": "Moses himself said nothing. The text pauses to note: Moses was the most humble man on earth — and his silence here is that humility on display."
    },
    "4": {
      "L": "And the LORD spake suddenly unto Moses, and unto Aaron, and unto Miriam, Come out ye three unto the tabernacle of the congregation. And they three came out.",
      "M": "At once the LORD said to Moses, Aaron, and Miriam: Come out, you three, to the tent of meeting. And the three of them came out.",
      "T": "Suddenly the LORD spoke — to all three at once: 'The three of you — come to the tent of meeting. Now.' All three went."
    },
    "5": {
      "L": "And the LORD came down in the pillar of the cloud, and stood in the door of the tabernacle, and called Aaron and Miriam: and they both came forth.",
      "M": "The LORD came down in a pillar of cloud and stood at the entrance of the tent, and called Aaron and Miriam. Both of them stepped forward.",
      "T": "The LORD descended in a pillar of cloud and took his place at the tent entrance. He called Aaron and Miriam forward — and they came."
    },
    "6": {
      "L": "And he said, Hear now my words: If there be a prophet among you, I the LORD will make myself known unto him in a vision, and will speak unto him in a dream.",
      "M": "He said: Hear my words. When there is a prophet among you, I the LORD make myself known to him in a vision; I speak with him in a dream.",
      "T": "'Listen to me. When I have a prophet among my people, I make myself known in visions, I speak in dreams.'"
    },
    "7": {
      "L": "My servant Moses is not so, who is faithful in all mine house.",
      "M": "Not so with my servant Moses. He is faithful in all my house.",
      "T": "'Not so with my servant Moses. He is faithful in my entire household — trusted with everything.'"
    },
    "8": {
      "L": "With him will I speak mouth to mouth, even apparently, and not in dark speeches; and the similitude of the LORD shall he behold: wherefore then were ye not afraid to speak against my servant Moses?",
      "M": "With him I speak mouth to mouth, clearly and not in riddles, and he sees the form of the LORD. Why then were you not afraid to speak against my servant Moses?",
      "T": "'With Moses I speak directly — mouth to mouth, face to presence, plainly and not in riddles. He has seen the very form of the LORD. How then did you dare speak against him?'"
    },
    "9": {
      "L": "And the anger of the LORD was kindled against them; and he departed.",
      "M": "The anger of the LORD burned against them, and he departed.",
      "T": "The LORD's anger burned against them — and he left."
    },
    "10": {
      "L": "And the cloud departed from off the tabernacle; and, behold, Miriam became leprous, white as snow: and Aaron looked upon Miriam, and, behold, she was leprous.",
      "M": "When the cloud withdrew from over the tent, Miriam was leprous — white as snow. Aaron turned toward Miriam, and she was leprous.",
      "T": "As the cloud lifted from the tent, Miriam was struck — a severe skin disease, white as snow. Aaron turned and saw her."
    },
    "11": {
      "L": "And Aaron said unto Moses, Alas, my lord, I beseech thee, lay not the sin upon us, wherein we have done foolishly, and wherein we have sinned.",
      "M": "Aaron said to Moses: Oh, my lord, please do not lay on us the guilt of the sin we have foolishly committed.",
      "T": "Aaron turned to Moses: 'My lord — please — do not hold this sin against us. We acted like fools; we have sinned.'"
    },
    "12": {
      "L": "Let her not be as one dead, of whom the flesh is half consumed when he cometh out of his mother's womb.",
      "M": "Do not let her be like one stillborn, whose flesh is half eaten away when it comes out of the womb.",
      "T": "'Do not let her be like a stillborn child — flesh already half consumed at the moment of birth.'"
    },
    "13": {
      "L": "And Moses cried unto the LORD, saying, Heal her now, O God, I beseech thee.",
      "M": "Moses cried out to the LORD: O God, please heal her!",
      "T": "Moses cried out to the LORD: 'God — please! Heal her!'"
    },
    "14": {
      "L": "And the LORD said unto Moses, If her father had but spit in her face, should she not be ashamed seven days? let her be shut out from the camp seven days, and after that let her be received in again.",
      "M": "The LORD said to Moses: If her father had merely spit in her face, would she not be in disgrace for seven days? Let her be confined outside the camp for seven days; after that she may be brought back in.",
      "T": "The LORD said to Moses: 'If her father had only spat in her face, she would bear the shame seven days. She is to be shut outside the camp seven days. After that, she is received back in.'"
    },
    "15": {
      "L": "And Miriam was shut out from the camp seven days: and the people journeyed not till Miriam was brought in again.",
      "M": "So Miriam was confined outside the camp for seven days, and the people did not set out until Miriam was brought back in.",
      "T": "Miriam was shut outside the camp seven days. Israel did not march. The entire people waited — seven days — until Miriam was restored."
    },
    "16": {
      "L": "And afterward the people removed from Hazeroth, and pitched in the wilderness of Paran.",
      "M": "After that the people moved from Hazeroth and camped in the wilderness of Paran.",
      "T": "Then Israel moved on from Hazeroth and made camp in the Paran wilderness."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'numbers')
        merge_tier(existing, NUMBERS, tier_key)
        save(tier_dir, 'numbers', existing)
    print('Numbers 7–12 written.')

if __name__ == '__main__':
    main()
