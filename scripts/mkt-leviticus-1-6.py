"""
MKT Leviticus chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-leviticus-1-6.py

Covers the five major offering types and their procedural regulations:
ch. 1 — burnt offerings (עֹלָה); ch. 2 — grain offerings (מִנְחָה);
ch. 3 — fellowship/peace offerings (שְׁלָמִים); ch. 4 — sin offerings (חַטָּאת)
graduated by offender rank; ch. 5 — guilt/trespass offerings (אָשָׁם) including
poverty accommodations; ch. 6 — perpetual-fire law and priestly portions.

Translation decisions:
- H3068 (יהוה): "the LORD" in L/M, same as Genesis and Exodus convention.
- H430 (אֱלֹהִים): "God" — consistent with prior scripts.
- H5315 (נֶפֶשׁ): In ritual contexts = "anyone/a person" not the Greek 'soul';
  L="soul" (preserves strangeness of Hebrew idiom), M="anyone/a person", T="they/someone".
- H5930 (עֹלָה): "burnt offering" in L/M/T — the complete-combustion offering.
- H4503 (מִנְחָה): "grain offering" in L/M/T — KJV "meat offering" is archaic;
  modern "grain offering" correctly identifies the flour/oil base.
- H8002 (שְׁלָמִים): L="peace offering", M="fellowship offering", T="fellowship sacrifice" —
  the שָׁלוֹם root points to well-being and wholeness shared between God and offerer.
- H2403 (חַטָּאת): "sin offering" in L/M; T may note its purification-of-sanctuary function.
- H817 (אָשָׁם): L="trespass offering", M="guilt offering", T="reparation offering" —
  restitution is central; the term carries more than moral guilt, it implies a debt.
- H3899 (לֶחֶם): "food" when applied to divine offerings (3:11, 3:16) — the term is
  literally "bread/food"; the priestly theology views the burnt fat as God's food portion.
- H801 (אִשֶּׁה): L="offering made by fire", M="food offering", T="fire offering" —
  the formulaic gift element of sacrifices offered by combustion.
- H5207+H7381 (rêah nîhôah): "pleasing aroma" throughout — the standard acceptance
  formula; L="sweet savour" is archaic but preserved in L for source texture.
- H3722 (כָּפַר): "make atonement" in L/M; T varies — "cover guilt", "make expiation",
  "purge away sin" — the root meaning is to cover or wipe clean.
- H7522 (רָצוֹן): at 1:3 "of his own free will / to be accepted" — voluntary presentation
  before the LORD as the condition of acceptance.
- H1285 (בְּרִית) at 2:13: "covenant" — salt as covenant-sealer; the phrase "salt of the
  covenant of your God" recalls the permanence and binding nature of all Israel's offerings.
- H6944 (קֹדֶשׁ): "holy" / "most holy" — the superlative (qodesh qodashim) applied to
  sin and guilt offerings indicates the highest degree of sacred status.
- H2708/H2706 (חֻקָּה/חֹק): "perpetual statute" in L, "lasting ordinance" in M,
  "permanent rule" or "unbreakable law" in T — the term denotes a fixed, recurring obligation.
- Aspect: Hebrew imperfect in commands = ongoing obligation "you shall / you must".
  Waw-consecutive narrates procedure: "he shall... he shall..." sequences.
- Gradated sin offerings (ch. 4): the text explicitly keys the offering to social rank
  (anointed priest → whole congregation → ruler → common person). T surfaces this intentional
  design — the system of accountability descends from leaders to the people.
- Poverty accommodation (5:7–13): the threefold tier (lamb → birds → flour) is a structural
  mercy provision. T notes this rather than flattening it into procedural instruction.
- Ch. 6 perpetual fire (6:13): the altar fire was kindled by divine fire (Lev 9:24);
  maintaining it was not merely practical but theological — the meeting-point between God and
  Israel must always be active.
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

LEVITICUS = {
  "1": {
    "1": {
      "L": "And the LORD called to Moses and spoke to him out of the tent of meeting, saying,",
      "M": "The LORD called to Moses and spoke to him from the tent of meeting, saying,",
      "T": "The LORD called Moses by name and spoke to him from the tent of meeting:"
    },
    "2": {
      "L": "Speak to the children of Israel and say to them: If any man of you brings an offering to the LORD, he shall bring his offering from the herd or from the flock.",
      "M": "Speak to the Israelites and say to them: When any of you brings an offering to the LORD, bring it from the herd or from the flock.",
      "T": "Tell the Israelites: When any of you wants to bring an offering to the LORD, bring an animal from the herd or the flock."
    },
    "3": {
      "L": "If his offering is a burnt sacrifice from the herd, he shall offer a male without blemish; he shall present it at the door of the tent of meeting of his own voluntary will before the LORD.",
      "M": "If the offering is a burnt offering from the herd, he must present a male without defect at the entrance to the tent of meeting so that he may be accepted before the LORD.",
      "T": "If the offering is a whole burnt offering from the herd, it must be a flawless male, brought willingly to the entrance of the tent of meeting where the LORD will accept it."
    },
    "4": {
      "L": "And he shall lay his hand upon the head of the burnt offering, and it shall be accepted for him to make atonement for him.",
      "M": "He must lay his hand on the head of the burnt offering, and it will be accepted on his behalf to make atonement for him.",
      "T": "He lays his hand on the animal's head — transferring his identity to the offering — and the LORD accepts it to cover his guilt."
    },
    "5": {
      "L": "And he shall slaughter the bull before the LORD; and Aaron's sons the priests shall bring the blood and sprinkle the blood round about upon the altar that is at the door of the tent of meeting.",
      "M": "He slaughters the bull before the LORD, and Aaron's sons the priests bring the blood and sprinkle it all around on the altar at the entrance to the tent of meeting.",
      "T": "He slaughters the animal before the LORD; the priests carry the blood and dash it around every side of the altar at the tent entrance — blood that marks the boundary between death and life."
    },
    "6": {
      "L": "And he shall flay the burnt offering and cut it up into its pieces.",
      "M": "He skins the burnt offering and cuts it into pieces.",
      "T": "He skins the carcass and cuts it into portions."
    },
    "7": {
      "L": "And the sons of Aaron the priest shall put fire upon the altar and lay the wood in order upon the fire.",
      "M": "The sons of Aaron the priest put fire on the altar and arrange the wood on the fire.",
      "T": "Aaron's sons kindle the altar fire and stack the wood in order on it."
    },
    "8": {
      "L": "And Aaron's sons the priests shall lay the parts, the head, and the fat, in order on the wood that is on the fire which is upon the altar.",
      "M": "Aaron's sons the priests arrange the pieces — the head and the fat — in order on the wood burning on the altar.",
      "T": "The priests lay out all the portions — head, fat, and body pieces — in proper order on the burning wood."
    },
    "9": {
      "L": "But its inwards and its legs he shall wash with water; and the priest shall burn all on the altar as a burnt sacrifice, an offering made by fire, a sweet savour unto the LORD.",
      "M": "He washes the internal organs and the legs with water, and the priest burns everything on the altar as a burnt offering — a food offering, a pleasing aroma to the LORD.",
      "T": "The internal organs and legs are washed clean with water; then the priest burns the whole animal on the altar — a fragrant offering wholly given to the LORD."
    },
    "10": {
      "L": "And if his offering for a burnt sacrifice be of the flocks, namely of the sheep or of the goats, he shall bring a male without blemish.",
      "M": "If the offering for a burnt sacrifice is from the flock — whether sheep or goat — he must bring a male without defect.",
      "T": "If the offering comes from the flock — sheep or goat — it must be a flawless male."
    },
    "11": {
      "L": "And he shall kill it on the north side of the altar before the LORD; and Aaron's sons the priests shall sprinkle its blood upon the altar round about.",
      "M": "He slaughters it on the north side of the altar before the LORD, and Aaron's sons the priests sprinkle its blood around the altar.",
      "T": "It is slaughtered at the north side of the altar — the LORD's side — and the priests dash its blood around the altar."
    },
    "12": {
      "L": "And he shall cut it into his pieces, with his head and his fat; and the priest shall lay them in order on the wood that is on the fire upon the altar.",
      "M": "He cuts it into pieces — head and fat included — and the priest arranges them in order on the wood burning on the altar.",
      "T": "He cuts it into portions, head and fat included, and the priest arrays them on the burning wood."
    },
    "13": {
      "L": "But he shall wash the inwards and the legs with water; and the priest shall bring it all and burn it upon the altar; it is a burnt sacrifice, an offering made by fire, a sweet savour unto the LORD.",
      "M": "He washes the entrails and legs with water, and the priest offers and burns everything on the altar — a burnt offering, a food offering, a pleasing aroma to the LORD.",
      "T": "The entrails and legs are washed, then the priest burns everything on the altar — a whole offering, fragrant and wholly given to the LORD."
    },
    "14": {
      "L": "And if his burnt sacrifice to the LORD be of fowls, then he shall bring his offering from turtledoves or from young pigeons.",
      "M": "If his burnt offering to the LORD is a bird, he must bring either a turtledove or a young pigeon.",
      "T": "If someone's means allows only a bird for a burnt offering to the LORD, let it be a turtledove or a young pigeon."
    },
    "15": {
      "L": "And the priest shall bring it unto the altar and wring off its head and burn it on the altar; and the blood thereof shall be wrung out at the side of the altar.",
      "M": "The priest brings it to the altar, wrings off its head, and burns it on the altar; the blood is drained out against the side of the altar.",
      "T": "The priest brings the bird to the altar, wrings off its head and burns it; the blood is squeezed out along the altar's side."
    },
    "16": {
      "L": "And he shall pluck away its crop with its feathers and cast it beside the altar on the east part, in the place of the ashes.",
      "M": "He removes the crop and feathers and throws them beside the altar on the east side, in the ash heap.",
      "T": "The crop and feathers are discarded in the ash pit on the east side of the altar."
    },
    "17": {
      "L": "And he shall cleave it with its wings but shall not divide it asunder; and the priest shall burn it upon the altar, upon the wood that is upon the fire; it is a burnt sacrifice, an offering made by fire, a sweet savour unto the LORD.",
      "M": "He splits the bird at its wings without dividing it completely; the priest burns it on the altar on the burning wood — it is a burnt offering, a food offering, a pleasing aroma to the LORD.",
      "T": "He splits it open by its wings without tearing it apart, and the priest burns it whole on the altar — a fragrant offering wholly surrendered to the LORD."
    }
  },
  "2": {
    "1": {
      "L": "And when any soul will offer a grain offering unto the LORD, his offering shall be of fine flour; and he shall pour oil upon it and put frankincense upon it.",
      "M": "When anyone brings a grain offering to the LORD, it is to be of fine flour, with oil poured on it and frankincense placed on it.",
      "T": "When someone wants to bring a grain offering to the LORD, let it be of fine flour: oil drizzled over it, frankincense laid upon it."
    },
    "2": {
      "L": "And he shall bring it to Aaron's sons the priests; and the priest shall take thereout his handful of the flour and of the oil, with all the frankincense thereof; and the priest shall burn the memorial of it upon the altar, an offering made by fire, a sweet savour unto the LORD.",
      "M": "He brings it to Aaron's sons the priests; the priest takes a handful of the flour and oil along with all the frankincense and burns it as the memorial portion on the altar — a food offering, a pleasing aroma to the LORD.",
      "T": "He brings it to the priests; a priest takes a representative handful — the flour, oil, and all the frankincense — and burns it on the altar as a token of the whole, fragrant before the LORD."
    },
    "3": {
      "L": "And the remnant of the grain offering shall be Aaron's and his sons'; it is a thing most holy of the offerings of the LORD made by fire.",
      "M": "The remainder of the grain offering belongs to Aaron and his sons; it is a most holy part of the LORD's food offerings.",
      "T": "The rest of the grain offering belongs to Aaron and his sons — a most holy share of what has been offered to the LORD."
    },
    "4": {
      "L": "And if thou bring an oblation of a grain offering baken in the oven, it shall be unleavened cakes of fine flour mingled with oil, or unleavened wafers anointed with oil.",
      "M": "If you bring a grain offering baked in an oven, it must be unleavened loaves of fine flour mixed with oil, or unleavened wafers spread with oil.",
      "T": "If your grain offering is oven-baked, it must be unleavened — either flat loaves of fine flour kneaded with oil, or thin wafers spread with oil."
    },
    "5": {
      "L": "And if thy oblation be a grain offering baked in a pan, it shall be of fine flour unleavened, mingled with oil.",
      "M": "If your offering is a grain offering prepared on a griddle, it is to be of fine flour with oil, and it must be unleavened.",
      "T": "If the offering is cooked on a flat griddle, use fine flour mixed with oil, and make it without leaven."
    },
    "6": {
      "L": "Thou shalt part it in pieces and pour oil thereon; it is a grain offering.",
      "M": "Break it into pieces and pour oil on it; it is a grain offering.",
      "T": "Break it into pieces and drizzle oil over it — this is a grain offering."
    },
    "7": {
      "L": "And if thy oblation be a grain offering baked in the frying pan, it shall be made of fine flour with oil.",
      "M": "If your offering is a grain offering prepared in a deep pan, it is to be made of fine flour with oil.",
      "T": "If the offering is made in a covered pan, prepare it from fine flour and oil."
    },
    "8": {
      "L": "And thou shalt bring the grain offering that is made of these things unto the LORD; and when it is presented unto the priest, he shall bring it unto the altar.",
      "M": "Bring the grain offering made in any of these ways to the LORD; when it is presented to the priest, he carries it to the altar.",
      "T": "Whatever form it takes, bring the grain offering to the LORD; the priest receives it and takes it to the altar."
    },
    "9": {
      "L": "And the priest shall take from the grain offering a memorial thereof and shall burn it upon the altar, an offering made by fire, a sweet savour unto the LORD.",
      "M": "The priest takes the memorial portion from the grain offering and burns it on the altar — a food offering, a pleasing aroma to the LORD.",
      "T": "The priest lifts out the token portion and burns it on the altar, its aroma rising to the LORD."
    },
    "10": {
      "L": "And that which is left of the grain offering shall be Aaron's and his sons'; it is a thing most holy of the offerings of the LORD made by fire.",
      "M": "The remainder of the grain offering belongs to Aaron and his sons — a most holy portion of the LORD's food offerings.",
      "T": "The rest belongs to Aaron and the priests — their sacred portion from the offerings given to the LORD."
    },
    "11": {
      "L": "No grain offering which ye shall bring unto the LORD shall be made with leaven; for ye shall burn no leaven nor any honey in any offering of the LORD made by fire.",
      "M": "No grain offering brought to the LORD is to be made with yeast, because you are not to burn any yeast or honey in a food offering to the LORD.",
      "T": "Never put yeast or honey into any grain offering burned to the LORD — they ferment and corrupt, and only what is pure may be given to him in fire."
    },
    "12": {
      "L": "As for the oblation of the firstfruits, ye shall offer them unto the LORD; but they shall not be burnt on the altar for a sweet savour.",
      "M": "You may bring firstfruits as an offering to the LORD, but they are not to be burned on the altar as a pleasing aroma.",
      "T": "Firstfruits offerings belong to the LORD, but they are not burned on the altar — they are set apart for another purpose."
    },
    "13": {
      "L": "And every oblation of thy grain offering shalt thou season with salt; neither shalt thou suffer the salt of the covenant of thy God to be lacking from thy grain offering: with all thine offerings thou shalt offer salt.",
      "M": "Season every grain offering with salt; do not leave out the salt of the covenant with your God from your grain offering — add salt to all your offerings.",
      "T": "Salt every grain offering without exception — salt is the sign of the covenant between you and your God. The covenant cannot be offered without its seal: salt."
    },
    "14": {
      "L": "And if thou offer a grain offering of thy firstfruits unto the LORD, thou shalt offer for the grain offering of thy firstfruits green ears of corn dried by fire, even corn beaten out of full ears.",
      "M": "If you offer a grain offering of firstfruits to the LORD, offer it as heads of new grain roasted in fire — kernels beaten from fresh ears.",
      "T": "When you bring a firstfruits grain offering to the LORD, use freshly harvested grain — roasted over fire and coarsely ground from ripe ears."
    },
    "15": {
      "L": "And thou shalt put oil upon it and lay frankincense thereon; it is a grain offering.",
      "M": "Put oil on it and lay frankincense over it — it is a grain offering.",
      "T": "Drizzle oil on it and place frankincense on top — it is a grain offering to the LORD."
    },
    "16": {
      "L": "And the priest shall burn the memorial of it, even part of the beaten corn thereof, and part of the oil thereof, with all the frankincense thereof; it is an offering made by fire unto the LORD.",
      "M": "The priest burns the memorial portion — some of the crushed grain, some of the oil, and all the frankincense — as a food offering to the LORD.",
      "T": "The priest burns the token portion — grain, oil, and all the frankincense — as a fragrant offering to the LORD."
    }
  },
  "3": {
    "1": {
      "L": "And if his oblation be a sacrifice of peace offering, if he offer it of the herd, whether it be a male or female, he shall offer it without blemish before the LORD.",
      "M": "If someone's offering is a fellowship offering and it is an animal from the herd, whether male or female, he must offer one without defect before the LORD.",
      "T": "When the offering is a fellowship sacrifice from the herd — whether male or female — it must be flawless, presented before the LORD."
    },
    "2": {
      "L": "And he shall lay his hand upon the head of his offering and kill it at the door of the tent of meeting; and Aaron's sons the priests shall sprinkle the blood upon the altar round about.",
      "M": "He lays his hand on the head of the offering and slaughters it at the entrance to the tent of meeting; Aaron's sons the priests throw the blood against the altar on all sides.",
      "T": "He lays his hand on the animal's head, then slaughters it at the tent entrance; the priests throw the blood against every side of the altar."
    },
    "3": {
      "L": "And he shall offer of the sacrifice of the peace offering an offering made by fire unto the LORD; the fat that covereth the inwards, and all the fat that is upon the inwards,",
      "M": "From the fellowship offering he presents a food offering to the LORD: the fat covering the entrails and all the fat on the entrails,",
      "T": "He presents to the LORD the fatty portions of the fellowship offering: the fat surrounding the internal organs and all the fat within,"
    },
    "4": {
      "L": "And the two kidneys, and the fat that is on them, which is by the flanks, and the caul above the liver, with the kidneys, it shall he take away.",
      "M": "the two kidneys and the fat around them near the loins, and the fatty lobe attached to the liver, which he removes with the kidneys.",
      "T": "the two kidneys and their surrounding fat at the flanks, and the liver's fatty lobe — all removed along with the kidneys."
    },
    "5": {
      "L": "And Aaron's sons shall burn it on the altar upon the burnt sacrifice, which is upon the wood that is on the fire; it is an offering made by fire, of a sweet savour unto the LORD.",
      "M": "Aaron's sons burn these on the altar on top of the burnt offering resting on the burning wood — it is a food offering, a pleasing aroma to the LORD.",
      "T": "The priests burn these portions on the altar, laid on the burnt offering already burning there — a fragrant offering given to the LORD."
    },
    "6": {
      "L": "And if his offering for a sacrifice of peace offering unto the LORD be of the flock, male or female, he shall offer it without blemish.",
      "M": "If the fellowship offering to the LORD is from the flock, whether male or female, it must be without defect.",
      "T": "If the fellowship offering comes from the flock — sheep or goat, male or female — it must be without flaw."
    },
    "7": {
      "L": "If he offer a lamb for his offering, then shall he offer it before the LORD.",
      "M": "If he brings a lamb as his offering, he presents it before the LORD,",
      "T": "If it is a lamb, he presents it before the LORD,"
    },
    "8": {
      "L": "And he shall lay his hand upon the head of his offering and kill it before the tent of meeting; and Aaron's sons shall sprinkle the blood thereof round about upon the altar.",
      "M": "lays his hand on the animal's head, and slaughters it before the tent of meeting; Aaron's sons throw its blood against the altar all around.",
      "T": "lays his hand on its head, slaughters it before the tent of meeting, and the priests throw the blood around every side of the altar."
    },
    "9": {
      "L": "And he shall offer of the sacrifice of the peace offering an offering made by fire unto the LORD; the fat thereof, and the whole rump, it shall he take off hard by the backbone; and the fat that covereth the inwards, and all the fat that is upon the inwards,",
      "M": "From the fellowship offering he presents a food offering to the LORD: the fat, the whole fat tail removed close to the backbone, the fat covering the entrails and all the fat on the entrails,",
      "T": "From the lamb he presents the LORD's portion: the fat — including the entire fatty tail, removed near the backbone — and all the fat around the internal organs."
    },
    "10": {
      "L": "And the two kidneys, and the fat that is upon them, which is by the flanks, and the caul above the liver, with the kidneys, it shall he take away.",
      "M": "the two kidneys and the fat around them near the loins, and the fatty lobe of the liver, which he removes with the kidneys.",
      "T": "the two kidneys with their flank fat, and the liver's fatty lobe removed with the kidneys."
    },
    "11": {
      "L": "And the priest shall burn it upon the altar; it is the food of the offering made by fire unto the LORD.",
      "M": "The priest burns these on the altar; it is the food of a food offering to the LORD.",
      "T": "The priest burns it all on the altar — this is the food offered to the LORD."
    },
    "12": {
      "L": "And if his offering be a goat, then he shall offer it before the LORD,",
      "M": "If his offering is a goat, he presents it before the LORD,",
      "T": "If it is a goat, he brings it before the LORD,"
    },
    "13": {
      "L": "And he shall lay his hand upon the head of it and kill it before the tent of meeting; and the sons of Aaron shall sprinkle the blood thereof upon the altar round about.",
      "M": "lays his hand on its head, and slaughters it before the tent of meeting; the sons of Aaron throw its blood against the altar all around.",
      "T": "lays his hand on its head, slaughters it before the tent of meeting, and the priests throw the blood around all sides of the altar."
    },
    "14": {
      "L": "And he shall offer thereof his offering, even an offering made by fire unto the LORD; the fat that covereth the inwards, and all the fat that is upon the inwards,",
      "M": "From it he presents his offering, a food offering to the LORD: the fat covering the entrails and all the fat on the entrails,",
      "T": "He presents from it the LORD's portion — a fire offering — beginning with all the fat around the internal organs:"
    },
    "15": {
      "L": "And the two kidneys, and the fat that is upon them, which is by the flanks, and the caul above the liver, with the kidneys, it shall he take away.",
      "M": "the two kidneys and the fat around them near the loins, and the fatty lobe of the liver, which he removes with the kidneys.",
      "T": "the two kidneys and their flank fat, and the fatty lobe of the liver removed with the kidneys."
    },
    "16": {
      "L": "And the priest shall burn them upon the altar; it is the food of the offering made by fire for a sweet savour: all the fat is the LORD's.",
      "M": "The priest burns these on the altar as food, a food offering, a pleasing aroma; all fat belongs to the LORD.",
      "T": "The priest burns it all on the altar — a fragrant offering, the food of the LORD. All fat belongs to the LORD alone."
    },
    "17": {
      "L": "It shall be a perpetual statute for your generations throughout all your dwellings, that ye eat neither fat nor blood.",
      "M": "This is a lasting ordinance for all your generations wherever you live: you must not eat any fat or any blood.",
      "T": "For all generations and wherever you live, this rule stands without exception: you must not eat fat, and you must not eat blood."
    }
  },
  "4": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, saying: If a soul sin through ignorance against any of the commandments of the LORD concerning things which ought not to be done, and shall do against any of them,",
      "M": "Say to the Israelites: When anyone sins unintentionally against any of the LORD's commands about things that must not be done, and violates any one of them,",
      "T": "Tell the Israelites: If any person commits an unintentional sin — doing something the LORD has forbidden without fully knowing it —"
    },
    "3": {
      "L": "If the priest that is anointed do sin according to the sin of the people, then let him bring for his sin, which he hath sinned, a young bullock without blemish unto the LORD for a sin offering.",
      "M": "if it is the anointed priest who sins and brings guilt on the people, he must bring a young bull without defect to the LORD as a sin offering for the sin he has committed.",
      "T": "if it is the anointed priest who sins — and his sin spreads guilt throughout the community — he must bring a flawless young bull to the LORD as a sin offering."
    },
    "4": {
      "L": "And he shall bring the bullock unto the door of the tent of meeting before the LORD; and shall lay his hand upon the bullock's head, and kill the bullock before the LORD.",
      "M": "He brings the bull to the entrance of the tent of meeting before the LORD, lays his hand on the bull's head, and slaughters it before the LORD.",
      "T": "He brings the bull to the entrance of the tent of meeting, lays his hand on its head — bearing the weight of the sin himself — and slaughters it before the LORD."
    },
    "5": {
      "L": "And the priest that is anointed shall take of the bullock's blood and bring it to the tent of meeting.",
      "M": "The anointed priest takes some of the bull's blood and carries it into the tent of meeting.",
      "T": "The anointed priest takes some of the bull's blood and brings it into the tent of meeting."
    },
    "6": {
      "L": "And the priest shall dip his finger in the blood and sprinkle of the blood seven times before the LORD, in front of the veil of the sanctuary.",
      "M": "He dips his finger in the blood and sprinkles it seven times before the LORD, in front of the curtain of the sanctuary.",
      "T": "He dips his finger in the blood and flicks it seven times toward the curtain of the inner sanctuary — before the LORD himself."
    },
    "7": {
      "L": "And the priest shall put some of the blood upon the horns of the altar of sweet incense before the LORD, which is in the tent of meeting; and shall pour all the blood of the bullock at the bottom of the altar of the burnt offering, which is at the door of the tent of meeting.",
      "M": "The priest puts some of the blood on the horns of the altar of fragrant incense that stands before the LORD in the tent of meeting; he pours the rest of the blood at the base of the altar of burnt offering at the entrance to the tent of meeting.",
      "T": "He puts blood on the horns of the incense altar before the LORD inside the tent, and pours the remaining blood at the foot of the burnt-offering altar at the tent entrance — blood marking every sacred boundary."
    },
    "8": {
      "L": "And he shall take off from it all the fat of the bullock for the sin offering; the fat that covereth the inwards, and all the fat that is upon the inwards,",
      "M": "He removes all the fat from the bull of the sin offering: the fat covering the entrails and all the fat on the entrails,",
      "T": "He removes all the fatty portions from the sin-offering bull: the fat covering the entrails and all the fat within,"
    },
    "9": {
      "L": "And the two kidneys, and the fat that is upon them, which is by the flanks, and the caul above the liver, with the kidneys, it shall he take away,",
      "M": "the two kidneys and the fat around them near the loins, and the fatty lobe of the liver, which he removes with the kidneys —",
      "T": "the two kidneys with their flank fat, and the liver's fatty lobe removed with them —"
    },
    "10": {
      "L": "as it was taken off from the bullock of the sacrifice of peace offerings; and the priest shall burn them upon the altar of the burnt offering.",
      "M": "just as they are removed from the ox of the fellowship offering; the priest burns them on the altar of burnt offering.",
      "T": "the same portions taken for the fellowship offering. The priest burns them all on the altar."
    },
    "11": {
      "L": "And the skin of the bullock, and all his flesh, with his head, and with his legs, and his inwards, and his dung,",
      "M": "The hide of the bull with all its flesh — head, legs, entrails, and dung —",
      "T": "But the hide, flesh, head, legs, entrails, and dung of the bull —"
    },
    "12": {
      "L": "even the whole bullock shall he carry forth without the camp unto a clean place, where the ashes are poured out, and burn him on the wood with fire; where the ashes are poured out shall he be burnt.",
      "M": "the entire bull he carries outside the camp to the clean place where the ashes are disposed of, and burns it on a wood fire there.",
      "T": "he carries the whole carcass to the clean ash-disposal site outside the camp and burns it there on a wood fire. It must burn where the ashes are poured out."
    },
    "13": {
      "L": "And if the whole congregation of Israel sin through ignorance, and the thing be hid from the eyes of the assembly, and they have done somewhat against any of the commandments of the LORD concerning things which should not be done, and are guilty;",
      "M": "If the whole Israelite community sins unintentionally and the matter is hidden from their assembly, doing something against any of the LORD's commands that must not be done, and they become guilty —",
      "T": "If the whole community of Israel sins unintentionally — the whole assembly failing together, without anyone seeing the full picture — violating one of the LORD's prohibitions and incurring guilt —"
    },
    "14": {
      "L": "When the sin, which they have sinned against it, is known, then the congregation shall offer a young bullock for the sin, and bring him before the tent of meeting.",
      "M": "when the sin they committed becomes known, the assembly must bring a young bull as a sin offering and present it before the tent of meeting.",
      "T": "once they discover the sin, the whole community brings a young bull as a sin offering and presents it before the tent of meeting."
    },
    "15": {
      "L": "And the elders of the congregation shall lay their hands upon the head of the bullock before the LORD; and the bullock shall be killed before the LORD.",
      "M": "The elders of the community lay their hands on the head of the bull before the LORD, and the bull is slaughtered before the LORD.",
      "T": "The community elders lay their hands on the bull's head on behalf of the whole assembly, and the bull is slaughtered before the LORD."
    },
    "16": {
      "L": "And the priest that is anointed shall bring of the bullock's blood to the tent of meeting.",
      "M": "The anointed priest brings some of the bull's blood into the tent of meeting,",
      "T": "The anointed priest brings blood from the bull into the tent of meeting,"
    },
    "17": {
      "L": "And the priest shall dip his finger in some of the blood and sprinkle it seven times before the LORD, even before the veil.",
      "M": "dips his finger in the blood, and sprinkles it seven times before the LORD, in front of the curtain.",
      "T": "dips his finger in the blood and flicks it seven times before the LORD's presence at the veil."
    },
    "18": {
      "L": "And he shall put some of the blood upon the horns of the altar which is before the LORD, that is in the tent of meeting; and shall pour out all the blood at the bottom of the altar of the burnt offering, which is at the door of the tent of meeting.",
      "M": "He puts some of the blood on the horns of the altar before the LORD in the tent of meeting and pours out the rest at the base of the altar of burnt offering at the entrance to the tent.",
      "T": "He puts blood on the horns of the altar inside the tent before the LORD, then pours the rest at the foot of the burnt-offering altar at the tent entrance."
    },
    "19": {
      "L": "And he shall take all his fat from him and burn it upon the altar.",
      "M": "He removes all the fat and burns it on the altar.",
      "T": "He strips off all the fat and burns it on the altar."
    },
    "20": {
      "L": "And he shall do with the bullock as he did with the bullock for a sin offering, so shall he do with this; and the priest shall make an atonement for them, and it shall be forgiven them.",
      "M": "He does with this bull exactly as he did with the bull of the sin offering for the anointed priest; the priest makes atonement for them, and they are forgiven.",
      "T": "The entire procedure follows what was prescribed for the priest's own sin offering. The priest makes atonement for the community, and they are forgiven."
    },
    "21": {
      "L": "And he shall carry forth the bullock without the camp and burn him as he burned the first bullock; it is a sin offering for the congregation.",
      "M": "He carries the bull outside the camp and burns it as he burned the first bull — it is the sin offering for the assembly.",
      "T": "The carcass is taken outside the camp and burned just like the first — it is the community's sin offering."
    },
    "22": {
      "L": "When a ruler hath sinned, and done somewhat through ignorance against any of the commandments of the LORD his God concerning things which should not be done, and is guilty;",
      "M": "When a leader sins unintentionally, violating any one of the commands of the LORD his God about things not to be done, and realizes his guilt,",
      "T": "When a ruler sins unintentionally against a command of the LORD his God — doing what must not be done — and realizes his guilt,"
    },
    "23": {
      "L": "Or if his sin, wherein he hath sinned, come to his knowledge; he shall bring his offering, a kid of the goats, a male without blemish.",
      "M": "when his sin becomes known to him, he must bring a male goat without defect as his offering.",
      "T": "when the sin he committed comes to light, he brings a flawless male goat as his offering."
    },
    "24": {
      "L": "And he shall lay his hand upon the head of the goat and kill it in the place where they kill the burnt offering before the LORD; it is a sin offering.",
      "M": "He lays his hand on the goat's head and slaughters it in the place where burnt offerings are slaughtered before the LORD — it is a sin offering.",
      "T": "He lays his hand on the goat's head, then slaughters it where burnt offerings are killed — before the LORD. It is a sin offering."
    },
    "25": {
      "L": "And the priest shall take of the blood of the sin offering with his finger, and put it upon the horns of the altar of burnt offering, and shall pour out his blood at the bottom of the altar of burnt offering.",
      "M": "The priest takes some of the blood of the sin offering with his finger and puts it on the horns of the altar of burnt offering, pouring the rest at the base of the altar.",
      "T": "The priest takes blood on his finger, applies it to the altar horns, and pours the rest at the altar's base."
    },
    "26": {
      "L": "And he shall burn all his fat upon the altar, as the fat of the sacrifice of peace offerings; and the priest shall make an atonement for him as concerning his sin, and it shall be forgiven him.",
      "M": "He burns all the fat on the altar as with the fellowship offering; the priest makes atonement for the ruler for his sin, and he is forgiven.",
      "T": "All the fat is burned on the altar, just as with the fellowship offering. The priest makes atonement for the ruler's sin, and he is forgiven."
    },
    "27": {
      "L": "And if any one of the common people sin through ignorance, while he doeth somewhat against any of the commandments of the LORD concerning things which ought not to be done, and be guilty;",
      "M": "If any ordinary person sins unintentionally, violating any of the LORD's commands about things not to be done, and realizes his guilt,",
      "T": "If any ordinary member of the community sins unintentionally against any of the LORD's commands — doing what must not be done — and realizes his guilt,"
    },
    "28": {
      "L": "Or if his sin, which he hath sinned, come to his knowledge; then he shall bring his offering, a kid of the goats, a female without blemish, for his sin which he hath sinned.",
      "M": "when the sin he committed becomes known to him, he shall bring a female goat without defect as his offering for the sin he committed.",
      "T": "when the sin comes to light, he brings a flawless female goat as his sin offering."
    },
    "29": {
      "L": "And he shall lay his hand upon the head of the sin offering, and slay the sin offering in the place of the burnt offering.",
      "M": "He lays his hand on the head of the sin offering and slaughters it at the place for burnt offerings.",
      "T": "He lays his hand on its head and slaughters it at the place of burnt offerings."
    },
    "30": {
      "L": "And the priest shall take of the blood thereof with his finger, and put it upon the horns of the altar of burnt offering, and shall pour out all the blood thereof at the bottom of the altar.",
      "M": "The priest takes some of its blood with his finger, puts it on the horns of the altar of burnt offering, and pours out the rest at the base of the altar.",
      "T": "The priest dabs blood on the altar horns with his finger and pours the rest at the base."
    },
    "31": {
      "L": "And he shall take away all the fat thereof, as the fat is taken away from off the sacrifice of peace offerings; and the priest shall burn it upon the altar for a sweet savour unto the LORD; and the priest shall make an atonement for him, and it shall be forgiven him.",
      "M": "He removes all the fat as it is removed from the fellowship offering, and the priest burns it on the altar as a pleasing aroma to the LORD; the priest makes atonement for him, and he is forgiven.",
      "T": "He removes all the fat as with the fellowship offering, and the priest burns it — a pleasing aroma to the LORD. Atonement is made, and the person is forgiven."
    },
    "32": {
      "L": "And if he bring a lamb for a sin offering, he shall bring it a female without blemish.",
      "M": "If he brings a lamb as his sin offering, he must bring a female without defect.",
      "T": "If the offering is a lamb rather than a goat, it must be a flawless female."
    },
    "33": {
      "L": "And he shall lay his hand upon the head of the sin offering and slay it for a sin offering in the place where they kill the burnt offering.",
      "M": "He lays his hand on the head of the sin offering and slaughters it as a sin offering at the place for burnt offerings.",
      "T": "He lays his hand on its head and slaughters it as a sin offering at the place of burnt offerings."
    },
    "34": {
      "L": "And the priest shall take of the blood of the sin offering with his finger and put it upon the horns of the altar of burnt offering and shall pour out all the blood thereof at the bottom of the altar.",
      "M": "The priest takes some of the blood of the sin offering with his finger, puts it on the horns of the altar of burnt offering, and pours the rest at the base of the altar.",
      "T": "The priest applies blood to the altar horns and pours the rest at the altar's base."
    },
    "35": {
      "L": "And he shall take away all the fat thereof, as the fat of the lamb is taken away from the sacrifice of the peace offerings; and the priest shall burn them upon the altar, according to the offerings made by fire unto the LORD; and the priest shall make an atonement for his sin that he hath committed, and it shall be forgiven him.",
      "M": "He removes all the fat just as the fat of the lamb is removed from the fellowship offering, and the priest burns it on the altar on top of the LORD's food offerings; the priest makes atonement for the sin he committed, and he is forgiven.",
      "T": "All fat is removed as with the fellowship lamb; the priest burns it on the altar along with the other offerings. Atonement is made for the sin, and the person is forgiven."
    }
  },
  "5": {
    "1": {
      "L": "And if a soul sin, and hear the voice of swearing, and is a witness, whether he hath seen or known of it; if he do not utter it, then he shall bear his iniquity.",
      "M": "If someone sins by not speaking up when called to testify as a witness — whether he has seen or knows of the matter — he bears the guilt.",
      "T": "If someone hears a public oath demanding testimony and stays silent — though they saw or knew something — they bear the guilt of their silence."
    },
    "2": {
      "L": "Or if a soul touch any unclean thing, whether it be a carcass of an unclean beast, or a carcass of unclean cattle, or the carcass of unclean creeping things, and if it be hidden from him, and he also be unclean, and be guilty;",
      "M": "Or if someone touches any unclean thing — the carcass of an unclean wild animal, an unclean domestic animal, or an unclean swarming creature — even if he was unaware of it and later realizes he is unclean, he is guilty.",
      "T": "Or if someone touches something ritually unclean — any dead unclean animal, domestic or wild, or crawling creature — even unknowingly, when the uncleanness becomes apparent, they are guilty."
    },
    "3": {
      "L": "Or if he touch the uncleanness of man, whatsoever uncleanness it be that a man shall be defiled withal, and it be hid from him; when he knoweth of it, then he shall be guilty.",
      "M": "Or if he touches any human uncleanness — any form of it that makes a person unclean — and was unaware of it, when he realizes it he is guilty.",
      "T": "Or if someone touches human ritual impurity of any kind without knowing it, when they realize it they are guilty."
    },
    "4": {
      "L": "Or if a soul swear, pronouncing with his lips to do evil, or to do good, whatsoever it be that a man shall pronounce with an oath, and it be hid from him; when he knoweth of it, then he shall be guilty in one of these.",
      "M": "Or if someone rashly takes an oath with his lips — to do something harmful or beneficial, whatever it may be — and it later slips from his mind, when he realizes it he is guilty.",
      "T": "Or if someone swears impulsively — pledging to do either harm or good — and then forgets about it, when they remember they are guilty."
    },
    "5": {
      "L": "And it shall be when he shall be guilty in one of these things, that he shall confess that he hath sinned in that thing:",
      "M": "When anyone is guilty in any of these cases, they must confess the sin they have committed,",
      "T": "When guilt is realized in any of these cases, the person must confess the specific sin openly —"
    },
    "6": {
      "L": "And he shall bring his trespass offering unto the LORD for his sin which he hath sinned, a female from the flock, a lamb or a kid of the goats, for a sin offering; and the priest shall make an atonement for him concerning his sin.",
      "M": "and bring to the LORD as his guilt offering for the sin committed, a female animal from the flock — a lamb or a female goat — as a sin offering; the priest makes atonement for him for his sin.",
      "T": "then bring a female from the flock — lamb or female goat — as a sin offering. The priest makes atonement, and the guilt is covered."
    },
    "7": {
      "L": "And if he be not able to bring a lamb, then he shall bring for his trespass, which he hath committed, two turtledoves or two young pigeons, unto the LORD; one for a sin offering and the other for a burnt offering.",
      "M": "If he cannot afford a lamb, he brings two turtledoves or two young pigeons to the LORD for the sin he committed — one as a sin offering and the other as a burnt offering.",
      "T": "If a lamb is beyond someone's means, they bring two turtledoves or two young pigeons — one for the sin offering, the other for a burnt offering. The law bends to meet the poor."
    },
    "8": {
      "L": "And he shall bring them unto the priest, who shall offer that which is for the sin offering first, and wring off his head from his neck, but shall not divide it asunder.",
      "M": "He brings them to the priest, who offers the sin offering first; he wrings its head from its neck without completely severing it.",
      "T": "He brings both to the priest, who prepares the sin offering first: wringing the head partly from the neck without separating it."
    },
    "9": {
      "L": "And he shall sprinkle of the blood of the sin offering upon the side of the altar; and the rest of the blood shall be wrung out at the bottom of the altar; it is a sin offering.",
      "M": "He sprinkles some of the blood of the sin offering against the side of the altar; the rest is drained at the base — it is a sin offering.",
      "T": "He sprinkles the blood against the altar's side; the remainder drains down to the base. This is the sin offering."
    },
    "10": {
      "L": "And he shall offer the second for a burnt offering, according to the manner; and the priest shall make an atonement for him for his sin which he hath sinned, and it shall be forgiven him.",
      "M": "He offers the second bird as a burnt offering according to the prescribed procedure; the priest makes atonement for his sin and he is forgiven.",
      "T": "The second bird is offered as a burnt offering by the proper procedure. Atonement is made and the person is forgiven."
    },
    "11": {
      "L": "But if he be not able to bring two turtledoves or two young pigeons, then he that sinned shall bring for his offering the tenth part of an ephah of fine flour for a sin offering; he shall put no oil upon it, neither shall he put any frankincense thereon; for it is a sin offering.",
      "M": "If he cannot afford even two turtledoves or pigeons, he brings as his sin offering a tenth of an ephah of fine flour; he must put no oil or frankincense on it, because it is a sin offering.",
      "T": "If even two birds are too much, a tenth of an ephah of fine flour serves as a sin offering — no oil, no frankincense; it is a sin offering, not a grain offering. God makes provision for the poorest."
    },
    "12": {
      "L": "Then shall he bring it to the priest, and the priest shall take his handful of it, even a memorial thereof, and burn it on the altar, according to the offerings made by fire unto the LORD; it is a sin offering.",
      "M": "He brings it to the priest, who takes a handful as the memorial portion and burns it on the altar along with the LORD's food offerings — it is a sin offering.",
      "T": "The priest takes a representative handful, burns it on the altar with the other offerings — it is a sin offering."
    },
    "13": {
      "L": "And the priest shall make an atonement for him as touching his sin that he hath sinned in one of these, and it shall be forgiven him; and the remnant shall be the priest's, as a grain offering.",
      "M": "The priest makes atonement for the sin committed in any of these cases, and the person is forgiven; the remainder belongs to the priest, as with the grain offering.",
      "T": "Atonement is made for whichever sin was committed, and forgiveness follows. The rest of the flour belongs to the priest as his portion, like any grain offering."
    },
    "14": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "15": {
      "L": "If a soul commit a trespass and sin through ignorance in the holy things of the LORD, then he shall bring for his trespass unto the LORD a ram without blemish out of the flocks, with thy estimation by shekels of silver, after the shekel of the sanctuary, for a trespass offering.",
      "M": "If anyone violates the sacred things of the LORD unintentionally — committing a trespass — he must bring to the LORD a flawless ram from the flock as a guilt offering, valued in silver shekels according to the sanctuary shekel.",
      "T": "When someone inadvertently misuses any of the LORD's sacred things — trespassing on what has been set apart — they bring a flawless ram as a guilt offering, its worth assessed in sanctuary shekels. The offense was against the holy; the restitution must match."
    },
    "16": {
      "L": "And he shall make amends for the harm that he hath done in the holy thing and shall add the fifth part thereto and give it unto the priest; and the priest shall make an atonement for him with the ram of the trespass offering, and it shall be forgiven him.",
      "M": "He must make restitution for the harm done to the holy thing and add a fifth of its value, giving it to the priest; the priest makes atonement with the ram of the guilt offering, and he is forgiven.",
      "T": "He pays full restitution for what was misused from the holy things, adding a fifth of the value — and the priest makes atonement with the guilt-offering ram. The debt is paid; the person is forgiven."
    },
    "17": {
      "L": "And if a soul sin and commit any of these things which are forbidden to be done by the commandments of the LORD; though he wist it not, yet is he guilty, and shall bear his iniquity.",
      "M": "If anyone sins by doing something the LORD has forbidden — even without knowing it — when they realize it, they are guilty and bear their iniquity.",
      "T": "If someone sins against any of the LORD's commands without knowing it, their ignorance does not remove the guilt — when awareness comes, so does accountability."
    },
    "18": {
      "L": "And he shall bring a ram without blemish out of the flock, with thy estimation, for a trespass offering, unto the priest; and the priest shall make an atonement for him concerning his ignorance wherein he erred and wist it not, and it shall be forgiven him.",
      "M": "He must bring to the priest a flawless ram from the flock, valued accordingly, as a guilt offering; the priest makes atonement for the unintentional error, and he is forgiven.",
      "T": "He brings a flawless ram, assessed at proper value, as a guilt offering; the priest makes atonement for the mistake, and forgiveness follows."
    },
    "19": {
      "L": "It is a trespass offering; he hath certainly trespassed against the LORD.",
      "M": "It is a guilt offering — he has truly incurred guilt before the LORD.",
      "T": "This is a guilt offering. The debt to the LORD is real, even when the offense was unintended."
    }
  },
  "6": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "If a soul sin and commit a trespass against the LORD, and lie unto his neighbour in that which was delivered him to keep, or in fellowship, or in a thing taken away by violence, or hath deceived his neighbour;",
      "M": "If someone sins by committing a trespass against the LORD — deceiving a neighbor about a deposit or security, through robbery, or by defrauding a neighbor —",
      "T": "When someone wrongs their neighbor and thereby wrongs the LORD — by lying about a deposit, a pledge, or stolen property, or by defrauding them —"
    },
    "3": {
      "L": "Or have found that which was lost and lieth concerning it, and sweareth falsely; in any of all these that a man doeth, sinning therein:",
      "M": "or has found lost property and lied about it, swearing falsely — in any of these sins that a person commits —",
      "T": "or has found something that was lost and lied about it, sealing the lie with a false oath — in any of these —"
    },
    "4": {
      "L": "Then it shall be because he hath sinned and is guilty, that he shall restore that which he took violently away, or the thing which he hath deceitfully gotten, or that which was delivered him to keep, or the lost thing which he found,",
      "M": "when he has sinned and realizes his guilt, he must return what he took by robbery, what he gained by fraud, what was entrusted to him, or the lost thing he found,",
      "T": "once guilt is acknowledged, full restitution is required: return the stolen goods, the fraudulent gain, the entrusted deposit, the found property —"
    },
    "5": {
      "L": "Or all that about which he hath sworn falsely; he shall even restore it in the principal, and shall add the fifth part more thereto, and give it unto him to whom it appertaineth, in the day of his trespass offering.",
      "M": "or anything about which he swore falsely. He must make full restitution, adding a fifth of the value, and give it to its owner on the day of his guilt offering.",
      "T": "everything about which he swore falsely — returned in full plus twenty percent, paid back to the rightful owner on the very day atonement is made."
    },
    "6": {
      "L": "And he shall bring his trespass offering unto the LORD, a ram without blemish out of the flock, with thy estimation, for a trespass offering, unto the priest.",
      "M": "He brings to the LORD his guilt offering — a flawless ram from the flock, at the proper assessment — to the priest.",
      "T": "Then he brings his guilt offering to the LORD: a flawless ram at assessed value, given to the priest."
    },
    "7": {
      "L": "And the priest shall make an atonement for him before the LORD; and it shall be forgiven him for any thing of all that he hath done in trespassing therein.",
      "M": "The priest makes atonement for him before the LORD, and he is forgiven for anything he did to incur guilt.",
      "T": "The priest makes atonement before the LORD, and forgiveness follows — for all the wrongs done against the neighbor, and through them, against God."
    },
    "8": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "9": {
      "L": "Command Aaron and his sons, saying: This is the law of the burnt offering; it is the burnt offering, because of the burning upon the altar all night unto the morning, and the fire of the altar shall be burning in it.",
      "M": "Command Aaron and his sons: This is the instruction for the burnt offering. The burnt offering is to remain on the altar hearth all night until morning, with the fire on the altar kept burning.",
      "T": "Give Aaron and his sons this instruction about the burnt offering: the offering stays on the altar hearth all through the night until morning. The altar fire must never go out."
    },
    "10": {
      "L": "And the priest shall put on his linen garment, and his linen breeches shall he put upon his flesh, and take up the ashes which the fire hath consumed with the burnt offering on the altar, and he shall put them beside the altar.",
      "M": "The priest puts on his linen robe and linen undergarments, takes up the ashes remaining from the burnt offering on the altar, and places them beside the altar.",
      "T": "In the morning the priest dresses in his full linen vestments and removes the ashes left by the burning — setting them beside the altar."
    },
    "11": {
      "L": "And he shall put off his garments and put on other garments, and carry forth the ashes without the camp unto a clean place.",
      "M": "Then he changes into other clothes and carries the ashes outside the camp to a clean place.",
      "T": "He changes into ordinary clothes and carries the ashes to the clean disposal place outside the camp."
    },
    "12": {
      "L": "And the fire upon the altar shall be burning in it; it shall not be put out; and the priest shall burn wood on it every morning, and lay the burnt offering in order upon it; and he shall burn thereon the fat of the peace offerings.",
      "M": "The fire on the altar must be kept burning; it must not go out. Every morning the priest burns wood on it, arranges the burnt offering on it, and burns the fat of the fellowship offerings on it.",
      "T": "The altar fire must burn without ceasing. Every morning the priest feeds it with fresh wood, arranges the day's burnt offering on it, and burns the fat portions of the fellowship offerings — the fire is never allowed to die."
    },
    "13": {
      "L": "The fire shall ever be burning upon the altar; it shall never go out.",
      "M": "The fire shall be kept burning on the altar continually; it must not go out.",
      "T": "Let the fire on the altar burn always — day and night, without ceasing. It must never go out."
    },
    "14": {
      "L": "And this is the law of the grain offering; the sons of Aaron shall offer it before the LORD, before the altar.",
      "M": "This is the instruction for the grain offering. Aaron's sons are to offer it before the LORD, in front of the altar.",
      "T": "This is the instruction for the grain offering. Aaron's sons present it before the LORD at the altar."
    },
    "15": {
      "L": "And he shall take of it his handful, of the flour of the grain offering, and of the oil thereof, and all the frankincense which is upon the grain offering, and shall burn it upon the altar for a sweet savour, even the memorial of it, unto the LORD.",
      "M": "A priest takes from it a handful of fine flour, along with the oil and all the frankincense on the grain offering, and burns it on the altar as a pleasing aroma — the memorial portion to the LORD.",
      "T": "The priest takes a representative handful — flour, oil, and all the frankincense — and burns it on the altar as the token portion, a fragrant offering to the LORD."
    },
    "16": {
      "L": "And the remainder thereof shall Aaron and his sons eat; with unleavened bread shall it be eaten in the holy place; in the court of the tent of meeting they shall eat it.",
      "M": "Aaron and his sons eat what remains. They eat it without yeast in the holy place — in the court of the tent of meeting.",
      "T": "Aaron and his sons eat the rest — without leaven, in the holy courtyard of the tent of meeting. Sacred food must be eaten in a sacred space."
    },
    "17": {
      "L": "It shall not be baken with leaven. I have given it unto them for their portion of my offerings made by fire; it is most holy, as is the sin offering, and as the trespass offering.",
      "M": "It must not be baked with yeast. I have given it as their share of my food offerings; it is most holy, like the sin offering and the guilt offering.",
      "T": "No yeast. I have given this to them as their permanent portion of my fire offerings — it is most holy, ranked with the sin offering and guilt offering."
    },
    "18": {
      "L": "All the males among the children of Aaron shall eat of it. It shall be a statute for ever in your generations concerning the offerings of the LORD made by fire; every one that toucheth them shall be holy.",
      "M": "Every male among Aaron's descendants may eat it; it is a permanent statute through your generations regarding the LORD's food offerings. Whoever touches them becomes holy.",
      "T": "Any male in Aaron's line may eat it — a permanent entitlement across all generations. Whoever touches these holy offerings is made holy by the contact."
    },
    "19": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "20": {
      "L": "This is the offering of Aaron and of his sons, which they shall offer unto the LORD in the day when he is anointed; the tenth part of an ephah of fine flour for a grain offering perpetual, half of it in the morning and half thereof at night.",
      "M": "This is the offering Aaron and his sons are to bring to the LORD on the day of anointing: a tenth of an ephah of fine flour as a regular grain offering — half in the morning and half in the evening.",
      "T": "On the day a priest is anointed, this is the grain offering he must bring to the LORD: one-tenth of an ephah of fine flour, half offered in the morning, half at evening. It continues as a regular offering."
    },
    "21": {
      "L": "In a pan it shall be made with oil; and when it is baked thou shalt bring it in; and the baken pieces of the grain offering shalt thou offer for a sweet savour unto the LORD.",
      "M": "It shall be made with oil on a griddle; bring it well mixed and offer the baked pieces as a grain offering, a pleasing aroma to the LORD.",
      "T": "Prepare it on a griddle with oil — bring it well-mixed, baked into pieces. Offer it as a grain offering, a fragrant gift to the LORD."
    },
    "22": {
      "L": "And the priest of his sons that is anointed in his stead shall offer it; it is a statute for ever unto the LORD; it shall be wholly burnt.",
      "M": "The priest anointed to succeed him shall offer it — a permanent statute to the LORD. It is to be entirely burned.",
      "T": "Every high priest, upon taking office, must keep up this offering — a permanent obligation to the LORD, fully burned without any portion kept."
    },
    "23": {
      "L": "For every grain offering for the priest shall be wholly burnt; it shall not be eaten.",
      "M": "Every grain offering from a priest shall be entirely burned — none of it may be eaten.",
      "T": "When the offering comes from a priest himself, it must be entirely burned — no portion belongs to the priest; it goes wholly to the LORD."
    },
    "24": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "25": {
      "L": "Speak unto Aaron and to his sons, saying: This is the law of the sin offering; in the place where the burnt offering is killed shall the sin offering be killed before the LORD; it is most holy.",
      "M": "Say to Aaron and his sons: This is the instruction for the sin offering. The sin offering is to be slaughtered before the LORD at the same place where the burnt offering is slaughtered — it is most holy.",
      "T": "Tell Aaron and his sons: This is the rule for sin offerings. The sin offering is slaughtered in the same place as the burnt offering — before the LORD — and it is most holy."
    },
    "26": {
      "L": "The priest that offereth it for sin shall eat it; in the holy place shall it be eaten, in the court of the tent of meeting.",
      "M": "The priest who offers it as a sin offering shall eat it; it is to be eaten in a holy place — in the court of the tent of meeting.",
      "T": "The priest who performs the sin offering eats his portion — in the holy courtyard of the tent of meeting, nowhere else."
    },
    "27": {
      "L": "Whatsoever shall touch the flesh thereof shall be holy; and when there is sprinkled of the blood thereof upon any garment, thou shalt wash that whereon it was sprinkled in the holy place.",
      "M": "Whatever touches its flesh becomes holy; and if any of its blood is sprinkled on a garment, wash the garment in a holy place.",
      "T": "Whatever touches the sin-offering meat becomes holy — set apart. If blood is sprinkled on clothing, the garment must be washed right there in the holy court."
    },
    "28": {
      "L": "But the earthen vessel wherein it is sodden shall be broken; and if it be sodden in a brasen vessel, it shall be both scoured and rinsed in water.",
      "M": "The clay pot it was cooked in must be broken; if it was cooked in a bronze pot, the pot must be scoured and rinsed with water.",
      "T": "The clay pot used for cooking the sin offering must be smashed — the holiness has permeated it and cannot be cleaned away. A bronze pot can be scrubbed and rinsed."
    },
    "29": {
      "L": "All the males among the priests shall eat thereof; it is most holy.",
      "M": "Every male among the priests may eat it; it is most holy.",
      "T": "Any male priest may eat it — it is most holy."
    },
    "30": {
      "L": "And no sin offering whereof any of the blood is brought into the tabernacle of the congregation to reconcile withal in the holy place shall be eaten; it shall be burnt in the fire.",
      "M": "But no sin offering may be eaten if its blood has been brought into the tent of meeting to make atonement in the holy place — it must be burned in the fire.",
      "T": "Any sin offering whose blood was brought inside the tent of meeting — used to make atonement in the inner sanctuary — may not be eaten. It must be burned entirely."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'leviticus')
        merge_tier(existing, LEVITICUS, tier_key)
        save(tier_dir, 'leviticus', existing)
    print('Leviticus 1–6 written.')

if __name__ == '__main__':
    main()
