"""
MKT Leviticus chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-leviticus-7-12.py

Covers: guilt-offering law completion (ch. 7), ordination of Aaron and sons (ch. 8),
Aaron's inaugural offerings and the divine fire (ch. 9), Nadab and Abihu's unauthorized fire
and priestly conduct laws (ch. 10), dietary laws (ch. 11), purification after childbirth (ch. 12).

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M; "the LORD" in T — matches Exodus
- H430 (אֱלֹהִים): "God" in all three tiers — matches Exodus
- H817 (אָשָׁם): L/M="guilt offering" (more precise than KJV "trespass offering");
  T="reparation offering" — the asham addresses breach of a sacred obligation and requires
  both sacrifice and monetary restitution; "guilt" is the standard scholarly rendering
- H2403 (חַטָּאת): "sin offering" in all three tiers — uncontested
- H8002 (שֶׁלֶם): L="peace offering", M/T="fellowship offering" — the shelem involves
  communal eating that enacts covenant communion; "fellowship" captures this better than "peace"
- H5930 (עֹלָה): "burnt offering" in all three tiers — standard
- H4503 (מִנְחָה): "grain offering" in all three tiers (not KJV "meat offering")
- H5315 (נֶפֶשׁ): "person" in penalty clauses (ch. 7); the embodied self, not a disembodied soul
- H2931/H2889 (טָמֵא/טָהוֹר): L/M="unclean/clean"; T="impure/pure" or "defiled/clean"
- H8251 (שֶׁקֶץ): L/M="abomination/detestable thing"; T="detestable" — strong ritual-revulsion term
- H3722 (כָּפַר): L/M="make atonement"; T="atone" — the kipper rite enacts removal of impurity/guilt
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" in all three tiers (KJV "tabernacle of the congregation")
- H6944 (קֹדֶשׁ): "holy" in L/M; "holy/sacred/set apart" in T by context
- Strange fire (אֵשׁ זָרָה) at 10:1: L="strange fire", M="unauthorized fire", T="unholy fire" —
  the problem is fire not commanded by God; T clarifies the nature of the violation
- H7307 (רוּחַ): not prominent in these chapters
- H2617 (חֶסֶד): not prominent in these chapters
- Childbirth purity (ch. 12): the doubled days for a daughter are not explained; T preserves the
  asymmetry without harmonizing; the purification offering restores the mother to full covenant standing
- Bird identification (ch. 11): following most probable Hebrew identifications based on LXX and
  modern scholarship; exact species uncertain for several terms
- Ordination idiom (מִלֻּאִים / "filling the hand") at ch. 8: L="ordination", M="ordination",
  T="investing with priestly office" — the idiom pictures hands filled with the first sacrificial
  portion as the gesture that transfers authority
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
  "7": {
    "1": {
      "L": "Likewise this is the law of the guilt offering; it is most holy.",
      "M": "This is the law of the guilt offering; it is most holy.",
      "T": "This is the ruling for the reparation offering: it is most holy."
    },
    "2": {
      "L": "In the place where they kill the burnt offering they shall kill the guilt offering, and its blood he shall sprinkle upon the altar round about.",
      "M": "The guilt offering shall be slaughtered in the same place where the burnt offering is slaughtered, and its blood shall be thrown against all sides of the altar.",
      "T": "The reparation offering is slaughtered in the same place as the burnt offering — its blood dashed against every side of the altar."
    },
    "3": {
      "L": "And he shall offer all the fat thereof: the fat tail, and the fat that covereth the inwards,",
      "M": "He shall offer all the fat from it: the fat tail and the fat covering the entrails,",
      "T": "All its fat is offered: the fat tail and the fat layer covering the entrails,"
    },
    "4": {
      "L": "and the two kidneys, and the fat that is on them, which is by the flanks, and the caul that is above the liver, with the kidneys, it shall he take away.",
      "M": "the two kidneys with the fat on them at the loins, and the long lobe of the liver, which he shall remove with the kidneys.",
      "T": "the two kidneys with their loin fat, and the lobe of the liver removed along with the kidneys."
    },
    "5": {
      "L": "And the priest shall burn them upon the altar for an offering made by fire unto the LORD; it is a guilt offering.",
      "M": "The priest shall burn them on the altar as a food offering to the LORD; it is a guilt offering.",
      "T": "The priest burns all of it on the altar as a fire offering to the LORD — this is the reparation offering."
    },
    "6": {
      "L": "Every male among the priests shall eat thereof; it shall be eaten in the holy place; it is most holy.",
      "M": "Every male among the priests may eat it. It shall be eaten in a holy place; it is most holy.",
      "T": "Any male priest may eat it — but only in the sacred precinct, for it is most holy."
    },
    "7": {
      "L": "As the sin offering is, so is the guilt offering; there is one law for them; the priest that maketh atonement therewith shall have it.",
      "M": "The guilt offering is like the sin offering; one law governs them both. The priest who makes atonement with it shall have it.",
      "T": "Guilt offering and sin offering follow the same rule: the priest who performs the rite of atonement keeps the meat."
    },
    "8": {
      "L": "And the priest that offereth any man's burnt offering, even the priest shall have to himself the skin of the burnt offering which he hath offered.",
      "M": "The priest who offers a man's burnt offering shall keep for himself the hide of the burnt offering he has offered.",
      "T": "The priest who presents anyone's burnt offering gets to keep the animal's hide for himself."
    },
    "9": {
      "L": "And all the grain offering that is baked in the oven, and all that is dressed in the fryingpan, and in the pan, shall be the priest's that offereth it.",
      "M": "Every grain offering baked in the oven and every grain offering prepared in a pan or on a griddle shall belong to the priest who offers it.",
      "T": "Every grain offering — whether baked in an oven, cooked in a pan, or grilled on a griddle — belongs to the priest who presents it."
    },
    "10": {
      "L": "And every grain offering mingled with oil, and dry, shall all the sons of Aaron have, one as much as another.",
      "M": "Every grain offering, whether mixed with oil or dry, shall be shared equally among all the sons of Aaron.",
      "T": "All grain offerings — whether mixed with oil or dry — are divided equally among Aaron's sons."
    },
    "11": {
      "L": "And this is the law of the sacrifice of peace offerings, which he shall offer unto the LORD.",
      "M": "This is the law of the sacrifice of fellowship offerings that one may offer to the LORD.",
      "T": "This is the ruling for the fellowship offering brought to the LORD."
    },
    "12": {
      "L": "If he offer it for a thanksgiving, then he shall offer with the sacrifice of thanksgiving unleavened cakes mingled with oil, and unleavened wafers anointed with oil, and cakes mingled with oil, of fine flour, fried.",
      "M": "If he offers it as a thanksgiving sacrifice, along with it he shall offer unleavened loaves mixed with oil, unleavened wafers spread with oil, and loaves of fine flour well mixed with oil.",
      "T": "If the offering expresses thanksgiving, it comes with three kinds of unleavened bread: loaves mixed with oil, wafers spread with oil, and fine-flour cakes blended with oil."
    },
    "13": {
      "L": "Besides the cakes, he shall offer for his offering leavened bread with the sacrifice of thanksgiving of his peace offerings.",
      "M": "Along with the unleavened cakes, he shall bring leavened bread as his offering with his thanksgiving fellowship offering.",
      "T": "Alongside the unleavened breads, leavened loaves are also offered with the thanksgiving fellowship sacrifice."
    },
    "14": {
      "L": "And of it he shall offer one out of the whole oblation for an heave offering unto the LORD, and it shall be the priest's that sprinkleth the blood of the peace offerings.",
      "M": "He shall present one from each offering as a contribution to the LORD; it shall belong to the priest who throws the blood of the fellowship offerings.",
      "T": "One loaf from each type is set apart as a gift to the LORD and goes to the priest who dashes the fellowship blood against the altar."
    },
    "15": {
      "L": "And the flesh of the sacrifice of his peace offerings for thanksgiving shall be eaten the same day that it is offered; he shall not leave any of it until the morning.",
      "M": "The meat of the thanksgiving fellowship offering shall be eaten on the day it is offered; none of it may be left until morning.",
      "T": "The meat of a thanksgiving fellowship offering must be eaten the same day — nothing left over until morning."
    },
    "16": {
      "L": "But if the sacrifice of his offering be a vow, or a freewill offering, it shall be eaten the same day that he offereth his sacrifice; and on the morrow also the remainder of it shall be eaten.",
      "M": "But if his sacrifice is a vow offering or a freewill offering, it shall be eaten on the day he offers it, and whatever remains may also be eaten the next day.",
      "T": "If the fellowship offering fulfills a vow or is a spontaneous gift, the meat may be eaten that day and the next."
    },
    "17": {
      "L": "But the remainder of the flesh of the sacrifice on the third day shall be burnt with fire.",
      "M": "Any flesh remaining from the sacrifice on the third day must be burned up with fire.",
      "T": "Whatever remains on the third day must be burned — it may not be eaten."
    },
    "18": {
      "L": "And if any of the flesh of the sacrifice of his peace offerings be eaten at all on the third day, it shall not be accepted, neither shall it be imputed unto him that offereth it; it shall be an abomination, and the soul that eateth of it shall bear his iniquity.",
      "M": "If any of the fellowship offering is eaten on the third day, it will not be accepted; it will not be credited to the one who offers it. It is tainted meat, and whoever eats it will bear the guilt.",
      "T": "If anyone eats it on the third day, the sacrifice is rejected — it earns the offerer no credit. The meat has become offensive, and whoever eats it carries the guilt."
    },
    "19": {
      "L": "And the flesh that toucheth any unclean thing shall not be eaten; it shall be burnt with fire; and as for the flesh, all that be clean shall eat thereof.",
      "M": "Meat that touches anything unclean shall not be eaten; it must be burned up with fire. As for clean meat, all who are ritually clean may eat it.",
      "T": "Meat that contacts anything impure must be burned, not eaten. Only those who are ritually clean may eat from the clean portions."
    },
    "20": {
      "L": "But the soul that eateth of the flesh of the sacrifice of peace offerings, that pertain unto the LORD, having his uncleanness upon him, even that soul shall be cut off from his people.",
      "M": "But if a person eats the flesh of the LORD's fellowship offering while he is in a state of uncleanness, that person shall be cut off from his people.",
      "T": "Anyone who eats from the LORD's fellowship offering while ritually impure shall be cut off from the community of Israel."
    },
    "21": {
      "L": "Moreover the soul that shall touch any unclean thing, as the uncleanness of man, or any unclean beast, or any abominable unclean thing, and eat of the flesh of the sacrifice of peace offerings, which pertain unto the LORD, even that soul shall be cut off from his people.",
      "M": "If anyone touches anything unclean — whether human uncleanness, an unclean animal, or any unclean detestable thing — and then eats of the LORD's fellowship offering, that person shall be cut off from the people.",
      "T": "If someone has touched anything defiling — a human impurity, an unclean animal, or any detestable thing — and then eats from the LORD's fellowship offering, that person is cut off from Israel."
    },
    "22": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "23": {
      "L": "Speak unto the children of Israel, saying, Ye shall eat no manner of fat, of ox, or of sheep, or of goat.",
      "M": "Tell the people of Israel: You shall eat no fat — whether from ox, sheep, or goat.",
      "T": "Tell the people of Israel: eat no fat — whether from cattle, sheep, or goat."
    },
    "24": {
      "L": "And the fat of the beast that dieth of itself, and the fat of that which is torn with beasts, may be used in any other use; but ye shall in no wise eat of it.",
      "M": "The fat of an animal that dies of itself or is torn by wild animals may be put to any other use, but you must not eat it.",
      "T": "Fat from an animal that died naturally or was killed by a predator may be used for other purposes — but it may never be eaten."
    },
    "25": {
      "L": "For whosoever eateth the fat of the beast, of which men offer an offering made by fire unto the LORD, even the soul that eateth it shall be cut off from his people.",
      "M": "For anyone who eats the fat of an animal from which a food offering may be made to the LORD shall be cut off from his people.",
      "T": "Anyone who eats fat from an animal eligible for offering to the LORD is cut off from Israel."
    },
    "26": {
      "L": "Moreover ye shall eat no manner of blood, whether it be of fowl or of beast, in any of your dwellings.",
      "M": "You shall eat no blood of any kind — whether of bird or animal — in any of your dwelling places.",
      "T": "Eat no blood — neither bird blood nor animal blood — in any place where you live."
    },
    "27": {
      "L": "Whatsoever soul it be that eateth any manner of blood, even that soul shall be cut off from his people.",
      "M": "Whoever eats any blood shall be cut off from his people.",
      "T": "Anyone who eats blood in any form shall be cut off from the people."
    },
    "28": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "29": {
      "L": "Speak unto the children of Israel, saying, He that offereth the sacrifice of his peace offerings unto the LORD shall bring his oblation unto the LORD of the sacrifice of his peace offerings.",
      "M": "Tell the people of Israel: Whoever offers a fellowship sacrifice to the LORD must bring to the LORD his own offering from the fellowship sacrifice.",
      "T": "Tell Israel: the one who brings a fellowship offering must personally present his portion of it to the LORD."
    },
    "30": {
      "L": "His own hands shall bring the offerings of the LORD made by fire, the fat with the breast, it shall he bring, that the breast may be waved for a wave offering before the LORD.",
      "M": "His own hands shall bring the LORD's food offerings — the fat together with the breast — so that the breast may be presented as a wave offering before the LORD.",
      "T": "He must carry it with his own hands — the fat and the breast together — so that the breast can be lifted and waved before the LORD."
    },
    "31": {
      "L": "And the priest shall burn the fat upon the altar; but the breast shall be Aaron's and his sons'.",
      "M": "The priest shall burn the fat on the altar, but the breast belongs to Aaron and his sons.",
      "T": "The fat goes up in flames on the altar; the breast goes to Aaron and his sons."
    },
    "32": {
      "L": "And the right shoulder shall ye give unto the priest for an heave offering out of the sacrifices of your peace offerings.",
      "M": "You shall give the right thigh to the priest as a contribution from your fellowship offerings.",
      "T": "The right thigh is given to the priest as a sacred gift from the fellowship offerings."
    },
    "33": {
      "L": "He among the sons of Aaron, that offereth the blood of the peace offerings, and the fat, shall have the right shoulder for his part.",
      "M": "The son of Aaron who offers the blood and fat of the fellowship offering shall have the right thigh as his portion.",
      "T": "The priest who handles the blood and fat of the fellowship offering receives the right thigh as his share."
    },
    "34": {
      "L": "For the wave breast and the heave shoulder have I taken of the children of Israel from off the sacrifices of their peace offerings, and have given them unto Aaron the priest and unto his sons by a statute for ever from among the children of Israel.",
      "M": "For I have taken the breast that is waved and the thigh that is contributed from the Israelites' fellowship offerings and have given them as a perpetual portion to Aaron the priest and his sons.",
      "T": "I have permanently set aside the wave breast and the raised thigh from Israel's fellowship offerings and given them to Aaron and his sons — a standing provision that never lapses."
    },
    "35": {
      "L": "This is the portion of the anointing of Aaron, and of the anointing of his sons, out of the offerings of the LORD made by fire, in the day when he presented them to minister unto the LORD in the priest's office;",
      "M": "This is the portion allotted to Aaron and his sons from the LORD's food offerings, from the day they were presented to serve the LORD as priests.",
      "T": "This is the allotment set aside for Aaron and his sons from the LORD's offerings — their due from the day they were installed to serve as priests."
    },
    "36": {
      "L": "which the LORD commanded to be given them of the children of Israel, in the day that he anointed them, by a statute for ever throughout their generations.",
      "M": "The LORD commanded that this be given to them by the Israelites — a permanent statute throughout their generations, from the day of their anointing.",
      "T": "The LORD himself commanded Israel to provide this from the day he anointed them — a perpetual statute binding on every generation."
    },
    "37": {
      "L": "This is the law of the burnt offering, of the grain offering, and of the sin offering, and of the guilt offering, and of the consecrations, and of the sacrifice of the peace offerings;",
      "M": "This is the law of the burnt offering, the grain offering, the sin offering, the guilt offering, the ordination offering, and the fellowship offering,",
      "T": "This concludes the law of the burnt offering, the grain offering, the sin offering, the reparation offering, the ordination offering, and the fellowship offering —"
    },
    "38": {
      "L": "which the LORD commanded Moses in mount Sinai, in the day that he commanded the children of Israel to offer their oblations unto the LORD, in the wilderness of Sinai.",
      "M": "which the LORD commanded Moses on Mount Sinai on the day he directed the Israelites to bring their offerings to the LORD in the wilderness of Sinai.",
      "T": "all of it commanded by the LORD to Moses on Mount Sinai, the day he charged Israel to bring their offerings to him in the Sinai wilderness."
    }
  },
  "8": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Take Aaron and his sons with him, and the garments, and the anointing oil, and a bullock for the sin offering, and two rams, and a basket of unleavened bread;",
      "M": "Bring Aaron and his sons, the priestly garments, the anointing oil, the bull for the sin offering, the two rams, and the basket of unleavened bread.",
      "T": "Gather Aaron and his sons, the priestly vestments, the anointing oil, the bull for the sin offering, the two rams, and the basket of unleavened bread."
    },
    "3": {
      "L": "And gather thou all the congregation together unto the door of the tabernacle of the congregation.",
      "M": "And assemble the whole congregation at the entrance of the tent of meeting.",
      "T": "Summon the whole congregation to the entrance of the tent of meeting."
    },
    "4": {
      "L": "And Moses did as the LORD commanded him; and the assembly was gathered together unto the door of the tabernacle of the congregation.",
      "M": "Moses did as the LORD commanded him, and the congregation assembled at the entrance of the tent of meeting.",
      "T": "Moses did everything the LORD commanded, and the whole congregation gathered at the tent of meeting entrance."
    },
    "5": {
      "L": "And Moses said unto the congregation, This is the thing which the LORD commanded to be done.",
      "M": "And Moses said to the congregation, This is what the LORD has commanded to be done.",
      "T": "Moses addressed the congregation: 'What you are about to witness is exactly what the LORD has commanded.'"
    },
    "6": {
      "L": "And Moses brought Aaron and his sons, and washed them with water.",
      "M": "Then Moses brought Aaron and his sons forward and washed them with water.",
      "T": "Moses brought Aaron and his sons forward and bathed them with water."
    },
    "7": {
      "L": "And he put upon him the coat, and girded him with the girdle, and clothed him with the robe, and put the ephod upon him, and he girded him with the curious girdle of the ephod, and bound it unto him therewith.",
      "M": "He put the tunic on Aaron and tied the sash around him, then clothed him with the robe and placed the ephod on him. He fastened the skillfully woven band of the ephod around him, binding it in place.",
      "T": "He dressed Aaron in the linen tunic, tied the sash, put on the outer robe, placed the ephod over it, and secured the woven band of the ephod, fastening it all together."
    },
    "8": {
      "L": "And he put the breastplate upon him; also he put in the breastplate the Urim and the Thummim.",
      "M": "He placed the breastpiece on him, and in the breastpiece he put the Urim and the Thummim.",
      "T": "He set the breastpiece over Aaron's chest and placed the Urim and Thummim inside it — the instruments of divine decision."
    },
    "9": {
      "L": "And he put the mitre upon his head; also upon the mitre, even upon his forefront, did he put the golden plate, the holy crown; as the LORD commanded Moses.",
      "M": "He set the turban on his head, and on the front of the turban he placed the golden plate — the holy crown — just as the LORD had commanded Moses.",
      "T": "He placed the turban on Aaron's head and fixed the golden plate — the holy diadem — to its front, exactly as the LORD had commanded."
    },
    "10": {
      "L": "And Moses took the anointing oil, and anointed the tabernacle and all that was therein, and sanctified them.",
      "M": "Moses then took the anointing oil and anointed the tabernacle and everything in it, consecrating them.",
      "T": "Moses took the anointing oil and anointed the tabernacle and all its furnishings, setting them apart as holy."
    },
    "11": {
      "L": "And he sprinkled thereof upon the altar seven times, and anointed the altar and all his vessels, both the laver and his foot, to sanctify them.",
      "M": "He sprinkled some of the oil on the altar seven times, then anointed the altar and all its utensils, as well as the basin and its stand, to consecrate them.",
      "T": "He sprinkled oil on the altar seven times, then anointed the altar with all its utensils and the bronze basin with its base — setting each one apart."
    },
    "12": {
      "L": "And he poured of the anointing oil upon Aaron's head, and anointed him, to sanctify him.",
      "M": "He poured some of the anointing oil on Aaron's head and anointed him to consecrate him.",
      "T": "He poured the anointing oil over Aaron's head, consecrating him for his office."
    },
    "13": {
      "L": "And Moses brought Aaron's sons, and put coats upon them, and girded them with girdles, and put bonnets upon them; as the LORD commanded Moses.",
      "M": "Moses then brought Aaron's sons forward, clothed them in tunics, tied sashes around them, and put caps on their heads, as the LORD had commanded Moses.",
      "T": "Moses clothed Aaron's sons in their tunics, tied their sashes, and placed caps on their heads — all exactly as the LORD had commanded."
    },
    "14": {
      "L": "And he brought the bullock for the sin offering: and Aaron and his sons laid their hands upon the head of the bullock for the sin offering.",
      "M": "He then brought the bull for the sin offering, and Aaron and his sons laid their hands on its head.",
      "T": "He brought the sin-offering bull forward, and Aaron and his sons pressed their hands against its head."
    },
    "15": {
      "L": "And he slew it; and Moses took the blood, and put it upon the horns of the altar round about with his finger, and purified the altar, and poured the blood at the bottom of the altar, and sanctified it, to make reconciliation upon it.",
      "M": "Moses slaughtered it and took the blood. With his finger he put blood on each horn of the altar, purifying it, then poured the rest of the blood at the base of the altar, consecrating it to make atonement.",
      "T": "Moses slaughtered the bull and put blood on every horn of the altar with his finger, purifying it. He poured the remaining blood at the altar's base — cleansing and consecrating it for atonement."
    },
    "16": {
      "L": "And he took all the fat that was upon the inwards, and the caul above the liver, and the two kidneys, and their fat, and Moses burned it upon the altar.",
      "M": "He took all the fat on the entrails, the long lobe of the liver, and the two kidneys with their fat, and Moses burned them on the altar.",
      "T": "He removed all the fat from the entrails, the liver lobe, and the kidneys with their fat, and burned them on the altar."
    },
    "17": {
      "L": "But the bullock, and his hide, his flesh, and his dung, he burnt with fire without the camp; as the LORD commanded Moses.",
      "M": "But the bull — its hide, its flesh, and its dung — he burned up with fire outside the camp, as the LORD commanded Moses.",
      "T": "The rest of the bull — hide, flesh, and dung — was burned outside the camp, as the LORD had commanded."
    },
    "18": {
      "L": "And he brought the ram for the burnt offering: and Aaron and his sons laid their hands upon the head of the ram.",
      "M": "Next he brought the ram for the burnt offering, and Aaron and his sons laid their hands on its head.",
      "T": "Then he brought the ram for the burnt offering. Aaron and his sons laid their hands on its head."
    },
    "19": {
      "L": "And he killed it; and Moses sprinkled the blood upon the altar round about.",
      "M": "Moses slaughtered it and threw the blood against all sides of the altar.",
      "T": "Moses slaughtered it and dashed the blood against every side of the altar."
    },
    "20": {
      "L": "And he cut the ram into pieces; and Moses burnt the head, and the pieces, and the fat.",
      "M": "He cut the ram into pieces, and Moses burned the head and the pieces and the fat.",
      "T": "He cut the ram into pieces and burned the head, the pieces, and the fat."
    },
    "21": {
      "L": "And he washed the inwards and the legs in water; and Moses burnt the whole ram upon the altar: it was a burnt sacrifice for a sweet savour, and an offering made by fire unto the LORD; as the LORD commanded Moses.",
      "M": "He washed the entrails and the legs with water, and Moses burned the whole ram on the altar. It was a burnt offering with a pleasing aroma, a food offering to the LORD, as the LORD commanded Moses.",
      "T": "He washed the entrails and legs, then burned the entire ram on the altar — a whole burnt offering, a pleasing aroma to the LORD, done exactly as commanded."
    },
    "22": {
      "L": "And he brought the other ram, the ram of consecration: and Aaron and his sons laid their hands upon the head of the ram.",
      "M": "Then he brought the second ram, the ordination ram, and Aaron and his sons laid their hands on its head.",
      "T": "He brought the second ram — the ordination ram. Aaron and his sons laid their hands on its head."
    },
    "23": {
      "L": "And he slew it; and Moses took of the blood of it, and put it upon the tip of Aaron's right ear, and upon the thumb of his right hand, and upon the great toe of his right foot.",
      "M": "Moses slaughtered it and took some of the blood and put it on the lobe of Aaron's right ear, on the thumb of his right hand, and on the big toe of his right foot.",
      "T": "Moses slaughtered it and daubed blood on the lobe of Aaron's right ear, the thumb of his right hand, and the big toe of his right foot — ear to hear, hand to act, foot to walk in holiness."
    },
    "24": {
      "L": "And he brought Aaron's sons, and Moses put of the blood upon the tip of their right ear, and upon the thumbs of their right hands, and upon the great toes of their right feet: and Moses sprinkled the blood upon the altar round about.",
      "M": "Moses brought Aaron's sons forward and put blood on the lobes of their right ears, on the thumbs of their right hands, and on the big toes of their right feet. Then he threw the rest of the blood against all sides of the altar.",
      "T": "He did the same for Aaron's sons — blood on the right ear, right thumb, and right big toe — then dashed the remaining blood against every side of the altar."
    },
    "25": {
      "L": "And he took the fat, and the rump, and all the fat that was upon the inwards, and the caul above the liver, and the two kidneys, and their fat, and the right shoulder.",
      "M": "He took the fat, the fat tail, all the fat on the entrails, the long lobe of the liver, the two kidneys with their fat, and the right thigh,",
      "T": "He set aside the fat, the fat tail, all the internal fat, the liver lobe, the kidneys with their fat, and the right thigh —"
    },
    "26": {
      "L": "And out of the basket of unleavened bread, that was before the LORD, he took one unleavened cake, and a cake of oiled bread, and one wafer, and put them on the fat, and upon the right shoulder.",
      "M": "and from the basket of unleavened bread before the LORD he took one unleavened loaf, one loaf of oiled bread, and one wafer, and placed them on the fat pieces and on the right thigh.",
      "T": "and from the unleavened bread basket he took one plain loaf, one oil-bread loaf, and one wafer, laying them on top of the fat and the right thigh."
    },
    "27": {
      "L": "And he put all upon Aaron's hands, and upon his sons' hands, and waved them for a wave offering before the LORD.",
      "M": "He placed all of this in the hands of Aaron and his sons and waved it as a wave offering before the LORD.",
      "T": "He filled Aaron's hands and his sons' hands with all of it and waved the whole bundle before the LORD."
    },
    "28": {
      "L": "And Moses took them from off their hands, and burnt them on the altar upon the burnt offering: they were consecrations for a sweet savour: it is an offering made by fire unto the LORD.",
      "M": "Moses then took them from their hands and burned them on the altar along with the burnt offering. This was an ordination offering with a pleasing aroma, a food offering to the LORD.",
      "T": "Moses took everything from their hands and burned it on the altar with the burnt offering — an ordination sacrifice of pleasing aroma to the LORD."
    },
    "29": {
      "L": "And Moses took the breast, and waved it for a wave offering before the LORD: for of the ram of consecration it was Moses' part; as the LORD commanded Moses.",
      "M": "Moses took the breast and waved it as a wave offering before the LORD. It was Moses' portion from the ordination ram, as the LORD had commanded.",
      "T": "Moses took the breast for himself and waved it before the LORD — his own portion from the ordination ram, as the LORD had commanded."
    },
    "30": {
      "L": "And Moses took of the anointing oil, and of the blood which was upon the altar, and sprinkled it upon Aaron, and upon his garments, and upon his sons, and upon his sons' garments with him; and sanctified Aaron, and his garments, and his sons, and his sons' garments with him.",
      "M": "Then Moses took some of the anointing oil and some of the blood from the altar and sprinkled both on Aaron, on his garments, and on his sons and their garments. So he consecrated Aaron, his garments, and his sons with their garments.",
      "T": "Moses took the anointing oil mixed with altar blood and sprinkled it over Aaron and his sons, over their vestments — consecrating them all together, priest and clothing alike."
    },
    "31": {
      "L": "And Moses said unto Aaron and to his sons, Boil the flesh at the door of the tabernacle of the congregation: and there eat it with the bread that is in the basket of consecrations, as I commanded, saying, Aaron and his sons shall eat it.",
      "M": "Moses said to Aaron and his sons, Boil the meat at the entrance of the tent of meeting and eat it there with the bread in the ordination basket, as I was commanded: Aaron and his sons shall eat it.",
      "T": "Moses told Aaron and his sons: 'Cook the meat at the tent of meeting entrance and eat it there with the bread from the ordination basket. This is what was commanded — Aaron and his sons eat it.'"
    },
    "32": {
      "L": "And that which remaineth of the flesh and of the bread shall ye burn with fire.",
      "M": "Whatever remains of the meat and the bread you shall burn with fire.",
      "T": "Whatever meat or bread is left over must be burned."
    },
    "33": {
      "L": "And ye shall not go out of the door of the tabernacle of the congregation in seven days, until the days of your consecration be at an end: for seven days shall he consecrate you.",
      "M": "You shall not leave the entrance of the tent of meeting for seven days, until your ordination is complete. For seven days he will ordain you.",
      "T": "Do not leave the tent of meeting entrance for seven days — the ordination takes the full seven days to complete."
    },
    "34": {
      "L": "As he hath done this day, so the LORD hath commanded to do, to make an atonement for you.",
      "M": "What has been done today the LORD has commanded to be done in order to make atonement for you.",
      "T": "Everything done today was commanded by the LORD to cover your sins and consecrate you for service."
    },
    "35": {
      "L": "Therefore shall ye abide at the door of the tabernacle of the congregation day and night seven days, and keep the charge of the LORD, that ye die not: for so I am commanded.",
      "M": "You must remain at the entrance of the tent of meeting day and night for seven days, carrying out the LORD's charge, so that you do not die — for so I have been commanded.",
      "T": "Stay at the tent of meeting entrance day and night for seven days, keeping the watch the LORD has set. Your lives depend on it — I am under the same command."
    },
    "36": {
      "L": "So Aaron and his sons did all things which the LORD commanded by the hand of Moses.",
      "M": "So Aaron and his sons did everything the LORD had commanded through Moses.",
      "T": "Aaron and his sons did everything the LORD had commanded through Moses — without exception."
    }
  },
  "9": {
    "1": {
      "L": "And it came to pass on the eighth day, that Moses called Aaron and his sons, and the elders of Israel;",
      "M": "On the eighth day Moses called Aaron and his sons and the elders of Israel.",
      "T": "On the eighth day — the first day after the ordination week — Moses summoned Aaron and his sons along with the elders of Israel."
    },
    "2": {
      "L": "And he said unto Aaron, Take thee a young calf for a sin offering, and a ram for a burnt offering, without blemish, and offer them before the LORD.",
      "M": "He said to Aaron, Take a bull calf without blemish for a sin offering and a ram without blemish for a burnt offering, and offer them before the LORD.",
      "T": "He told Aaron: 'Take a flawless bull calf as your sin offering and a flawless ram as a burnt offering, and present them before the LORD.'"
    },
    "3": {
      "L": "And unto the children of Israel thou shalt speak, saying, Take ye a kid of the goats for a sin offering; and a calf and a lamb, both of the first year, without blemish, for a burnt offering;",
      "M": "Tell the Israelites: Take a male goat for a sin offering, and a calf and a lamb — both yearlings without blemish — for a burnt offering,",
      "T": "Tell Israel to bring: a male goat for a sin offering, and a yearling calf and a yearling lamb — all without blemish — for a burnt offering,"
    },
    "4": {
      "L": "Also a bullock and a ram for peace offerings, to sacrifice before the LORD; and a grain offering mingled with oil: for to day the LORD will appear unto you.",
      "M": "and an ox and a ram for fellowship offerings to sacrifice before the LORD, along with a grain offering mixed with oil. For today the LORD will appear to you.",
      "T": "and an ox and a ram for fellowship offerings before the LORD, with a grain offering mixed with oil. Today the LORD himself will appear to you."
    },
    "5": {
      "L": "And they brought that which Moses commanded before the tabernacle of the congregation: and all the congregation drew near and stood before the LORD.",
      "M": "They brought what Moses commanded before the tent of meeting, and all the congregation drew near and stood before the LORD.",
      "T": "Everything Moses commanded was brought before the tent of meeting. The whole congregation assembled and stood before the LORD."
    },
    "6": {
      "L": "And Moses said, This is the thing which the LORD commanded that ye should do: and the glory of the LORD shall appear unto you.",
      "M": "Moses said, This is what the LORD commanded you to do, so that the glory of the LORD may appear to you.",
      "T": "Moses announced: 'This is what the LORD commanded. Do it — and the glory of the LORD will appear among you.'"
    },
    "7": {
      "L": "And Moses said unto Aaron, Go unto the altar, and offer thy sin offering, and thy burnt offering, and make an atonement for thyself, and for the people: and offer the offering of the people, and make an atonement for them; as the LORD commanded.",
      "M": "Moses said to Aaron, Come forward to the altar and offer your sin offering and your burnt offering to make atonement for yourself and for the people. Then bring the people's offering and make atonement for them, as the LORD commanded.",
      "T": "Moses told Aaron: 'Step forward to the altar. Offer your own sin offering and burnt offering first — atone for yourself. Then bring the people's offerings and atone for them. This is what the LORD commanded.'"
    },
    "8": {
      "L": "Aaron therefore went unto the altar, and slew the calf of the sin offering, which was for himself.",
      "M": "So Aaron went to the altar and slaughtered the calf of the sin offering for himself.",
      "T": "Aaron stepped up to the altar and slaughtered the sin-offering calf — his own offering first."
    },
    "9": {
      "L": "And the sons of Aaron brought the blood unto him: and he dipped his finger in the blood, and put it upon the horns of the altar, and poured out the blood at the bottom of the altar.",
      "M": "Aaron's sons brought the blood to him. He dipped his finger in the blood, put it on the horns of the altar, and poured out the rest at the base of the altar.",
      "T": "His sons handed him the blood. Aaron dipped his finger and marked every horn of the altar, then poured the remaining blood at its base."
    },
    "10": {
      "L": "But the fat, and the kidneys, and the caul above the liver of the sin offering, he burnt upon the altar; as the LORD commanded Moses.",
      "M": "The fat, the kidneys, and the long lobe of the liver from the sin offering he burned on the altar, as the LORD had commanded Moses.",
      "T": "The fat, kidneys, and liver lobe he burned on the altar — exactly as the LORD had commanded Moses."
    },
    "11": {
      "L": "And the flesh and the hide he burnt with fire without the camp.",
      "M": "The flesh and the hide he burned up with fire outside the camp.",
      "T": "The flesh and hide he burned outside the camp."
    },
    "12": {
      "L": "And he slew the burnt offering; and Aaron's sons presented unto him the blood, which he sprinkled round about upon the altar.",
      "M": "Then he slaughtered the burnt offering, and Aaron's sons handed him the blood, which he threw against all sides of the altar.",
      "T": "He slaughtered the burnt offering. His sons handed him the blood, and he dashed it against every side of the altar."
    },
    "13": {
      "L": "And they presented the burnt offering unto him, with the pieces thereof, and the head: and he burnt them upon the altar.",
      "M": "They handed him the pieces of the burnt offering, including the head, and he burned them on the altar.",
      "T": "His sons handed him the pieces and the head, and he burned them all on the altar."
    },
    "14": {
      "L": "And he did wash the inwards and the legs, and burnt them upon the burnt offering on the altar.",
      "M": "He washed the entrails and the legs and burned them with the burnt offering on the altar.",
      "T": "He washed the entrails and legs, then burned them with the rest of the burnt offering."
    },
    "15": {
      "L": "And he brought the people's offering, and took the goat, which was the sin offering for the people, and slew it, and offered it for sin, as the first.",
      "M": "Then he presented the people's offering. He took the goat of the sin offering for the people, slaughtered it, and offered it for sin, as he had done with the first.",
      "T": "Next he handled the people's offerings. The sin-offering goat was slaughtered and offered for the people's sin, following the same rite as his own."
    },
    "16": {
      "L": "And he brought the burnt offering, and offered it according to the manner.",
      "M": "He brought the burnt offering and offered it according to the prescribed manner.",
      "T": "He presented the burnt offering according to the established procedure."
    },
    "17": {
      "L": "And he brought the grain offering, and took an handful thereof, and burnt it upon the altar, beside the burnt sacrifice of the morning.",
      "M": "He brought the grain offering, took a handful of it, and burned it on the altar, in addition to the morning burnt offering.",
      "T": "He presented the grain offering, burned a symbolic handful on the altar — adding this to the morning burnt offering already on the fire."
    },
    "18": {
      "L": "He slew also the bullock and the ram for a sacrifice of peace offerings, which was for the people: and Aaron's sons presented unto him the blood, which he sprinkled upon the altar round about,",
      "M": "He slaughtered the ox and the ram as the fellowship sacrifice for the people. Aaron's sons handed him the blood, which he threw against all sides of the altar.",
      "T": "He slaughtered the ox and the ram — the people's fellowship offerings. His sons handed him the blood, which he dashed against every side of the altar."
    },
    "19": {
      "L": "And the fat of the bullock and of the ram, the rump, and that which covereth the inwards, and the kidneys, and the caul above the liver:",
      "M": "The fat pieces from the ox and the ram — the fat tail, the covering fat, the kidneys, and the long lobe of the liver —",
      "T": "The fat portions from both animals — the fat tail, the internal fat layer, the kidneys, the liver lobe —"
    },
    "20": {
      "L": "And they put the fat upon the breasts, and he burnt the fat upon the altar.",
      "M": "they placed the fat pieces on the breasts, and Aaron burned the fat on the altar.",
      "T": "were laid on the breasts, then Aaron burned the fat on the altar."
    },
    "21": {
      "L": "And the breasts and the right shoulder Aaron waved for a wave offering before the LORD; as Moses commanded.",
      "M": "The breasts and the right thigh Aaron waved as a wave offering before the LORD, as Moses had commanded.",
      "T": "The breasts and the right thigh Aaron lifted and waved before the LORD — the wave offering, as Moses had directed."
    },
    "22": {
      "L": "And Aaron lifted up his hand toward the people, and blessed them, and came down from offering of the sin offering, and the burnt offering, and peace offerings.",
      "M": "Then Aaron lifted up his hands toward the people and blessed them, and came down after offering the sin offering, the burnt offering, and the fellowship offerings.",
      "T": "Aaron turned toward the people, raised his hands, and blessed them. Then he came down from the altar, having completed the sin offering, burnt offering, and fellowship offerings."
    },
    "23": {
      "L": "And Moses and Aaron went into the tabernacle of the congregation, and came out, and blessed the people: and the glory of the LORD appeared unto all the people.",
      "M": "Moses and Aaron went into the tent of meeting, and when they came out they blessed the people. And the glory of the LORD appeared to all the people.",
      "T": "Moses and Aaron went together into the tent of meeting. When they came out, they blessed the people — and the glory of the LORD blazed into view before the entire assembly."
    },
    "24": {
      "L": "And there came a fire out from before the LORD, and consumed upon the altar the burnt offering and the fat: which when all the people saw, they shouted, and fell on their faces.",
      "M": "Fire came out from before the LORD and consumed the burnt offering and the fat pieces on the altar. When all the people saw it, they shouted with joy and fell on their faces.",
      "T": "Fire burst out from the presence of the LORD and devoured the burnt offering and the fat on the altar. When the people saw it, they erupted in a shout — and fell on their faces before God."
    }
  },
  "10": {
    "1": {
      "L": "And Nadab and Abihu, the sons of Aaron, took either of them his censer, and put fire therein, and put incense thereon, and offered strange fire before the LORD, which he commanded them not.",
      "M": "Now Nadab and Abihu, the sons of Aaron, each took his censer, put fire in it, laid incense on it, and offered unauthorized fire before the LORD — fire he had not commanded them to offer.",
      "T": "Then Nadab and Abihu, Aaron's sons, each grabbed his incense censer, loaded it with fire and incense, and offered unholy fire before the LORD — something he had never commanded."
    },
    "2": {
      "L": "And there went out fire from the LORD, and devoured them, and they died before the LORD.",
      "M": "Fire came out from before the LORD and consumed them, and they died before the LORD.",
      "T": "Fire came out from the presence of the LORD and consumed them. They died before the LORD."
    },
    "3": {
      "L": "Then Moses said unto Aaron, This is it that the LORD spake, saying, I will be sanctified in them that come nigh me, and before all the people I will be glorified. And Aaron held his peace.",
      "M": "Then Moses said to Aaron, This is what the LORD meant when he said: Among those who approach me I will show myself holy, and before all the people I will be honored. And Aaron was silent.",
      "T": "Moses said to Aaron: 'This is what the LORD meant: those who draw near to me must treat me as holy — and before all the people I must be seen as glorious.' Aaron said nothing."
    },
    "4": {
      "L": "And Moses called Mishael and Elzaphan, the sons of Uzziel the uncle of Aaron, and said unto them, Come near, carry your brethren from before the sanctuary out of the camp.",
      "M": "Moses called Mishael and Elzaphan, sons of Uzziel the uncle of Aaron, and said to them, Come forward and carry your cousins away from the front of the sanctuary, out of the camp.",
      "T": "Moses summoned Mishael and Elzaphan — cousins of Aaron through Uzziel — and told them: 'Come and carry your kinsmen away from the sanctuary and out of the camp.'"
    },
    "5": {
      "L": "So they went near, and carried them in their coats out of the camp; as Moses had said.",
      "M": "They came forward and carried them out of the camp in their tunics, as Moses had directed.",
      "T": "They came and carried the two bodies — still in their priestly tunics — out of the camp, as Moses had said."
    },
    "6": {
      "L": "And Moses said unto Aaron, and unto Eleazar and unto Ithamar, his sons, Uncover not your heads, neither rend your clothes; lest ye die, and lest wrath come upon all the people: but let your brethren, the whole house of Israel, bewail the burning which the LORD hath kindled.",
      "M": "Moses said to Aaron and to his sons Eleazar and Ithamar: Do not let your hair hang loose or tear your clothes, or you will die and wrath will come on the whole congregation. But let all your fellow Israelites mourn the burning that the LORD has kindled.",
      "T": "Moses told Aaron and his remaining sons Eleazar and Ithamar: 'Do not dishevel your hair or tear your clothes in mourning — that would bring death on you and God's anger on the whole congregation. Let the rest of Israel mourn this fire the LORD has kindled. But not you.'"
    },
    "7": {
      "L": "And ye shall not go out from the door of the tabernacle of the congregation, lest ye die: for the anointing oil of the LORD is upon you. And they did according to the word of Moses.",
      "M": "Do not leave the entrance of the tent of meeting, or you will die, for the anointing oil of the LORD is on you. And they did as Moses said.",
      "T": "Do not leave the tent of meeting entrance — leaving would bring death on you, for you bear the LORD's anointing oil. They obeyed."
    },
    "8": {
      "L": "And the LORD spake unto Aaron, saying,",
      "M": "The LORD said to Aaron,",
      "T": "The LORD spoke directly to Aaron:"
    },
    "9": {
      "L": "Do not drink wine nor strong drink, thou, nor thy sons with thee, when ye go into the tabernacle of the congregation, lest ye die: it shall be a statute for ever throughout your generations:",
      "M": "You and your sons must not drink wine or strong drink when you enter the tent of meeting, or you will die. This is a permanent statute throughout your generations.",
      "T": "You and your sons are forbidden to drink wine or strong drink before entering the tent of meeting — it is a death sentence if you do. This is a permanent law for every generation of priests."
    },
    "10": {
      "L": "And that ye may put difference between holy and unholy, and between unclean and clean;",
      "M": "You must distinguish between the holy and the common, and between the unclean and the clean,",
      "T": "You must be able to tell the difference between what is holy and what is common, between what is impure and what is clean —"
    },
    "11": {
      "L": "And that ye may teach the children of Israel all the statutes which the LORD hath spoken unto them by the hand of Moses.",
      "M": "and you must teach the Israelites all the statutes the LORD has spoken to them through Moses.",
      "T": "and you must teach Israel all the statutes the LORD spoke through Moses. A priest who cannot discern cannot teach."
    },
    "12": {
      "L": "And Moses spake unto Aaron, and unto Eleazar and unto Ithamar, his sons that were left, Take the grain offering that remaineth of the offerings of the LORD made by fire, and eat it without leaven beside the altar: for it is most holy:",
      "M": "Moses spoke to Aaron and to his surviving sons Eleazar and Ithamar: Take the grain offering that remains from the LORD's food offerings and eat it without yeast beside the altar, for it is most holy.",
      "T": "Moses told Aaron and his two remaining sons: 'Take the leftover grain offering from the LORD's fire offerings and eat it unleavened beside the altar — it is most holy.'"
    },
    "13": {
      "L": "And ye shall eat it in the holy place, because it is thy due, and thy sons' due, of the sacrifices of the LORD made by fire: for so I am commanded.",
      "M": "Eat it in a holy place, because it is your due and your sons' due from the LORD's food offerings. So I have been commanded.",
      "T": "Eat it in the sacred precinct — this is your portion and your sons' portion from the LORD's offerings. This is what I was commanded."
    },
    "14": {
      "L": "And the wave breast and heave shoulder shall ye eat in a clean place; thou, and thy sons, and thy daughters with thee: for they be thy due, and thy sons' due, which are given out of the sacrifices of peace offerings of the children of Israel.",
      "M": "But the wave breast and the contributed thigh you may eat in a clean place — you, your sons, and your daughters with you — for they are your due and your sons' due, given from Israel's fellowship offerings.",
      "T": "The wave breast and the raised thigh may be eaten in any ritually clean place — you, your sons, your daughters together — for these are the family's portion from Israel's fellowship offerings."
    },
    "15": {
      "L": "The heave shoulder and the wave breast shall they bring with the offerings made by fire of the fat, to wave it for a wave offering before the LORD; and it shall be thine, and thy sons' with thee, by a statute for ever; as the LORD hath commanded.",
      "M": "The contributed thigh and the wave breast are to be brought with the fat portions of the food offerings, to be waved as a wave offering before the LORD. They shall belong to you and your children as a permanent due, as the LORD has commanded.",
      "T": "The raised thigh and the wave breast are brought with the fat offerings and waved before the LORD — then given permanently to you and your descendants. The LORD has commanded it."
    },
    "16": {
      "L": "And Moses diligently sought the goat of the sin offering, and, behold, it was burnt; and he was angry with Eleazar and Ithamar, the sons of Aaron which were left alive, saying,",
      "M": "Moses inquired carefully about the goat of the sin offering and found that it had been burned up. He was angry with Eleazar and Ithamar, Aaron's surviving sons, and said,",
      "T": "Moses then looked for the sin-offering goat — and found it had been burned entirely. He was furious with Eleazar and Ithamar and demanded:"
    },
    "17": {
      "L": "Wherefore have ye not eaten the sin offering in the holy place, seeing it is most holy, and God hath given it you to bear the iniquity of the congregation, to make atonement for them before the LORD?",
      "M": "Why did you not eat the sin offering in the sanctuary? It is most holy, and God gave it to you to carry the guilt of the congregation and to make atonement for them before the LORD.",
      "T": "'Why did you not eat the sin offering in the sanctuary? It is most holy. God gave it to you for exactly this — to bear the congregation's guilt and atone for them before the LORD. You were supposed to eat it.'"
    },
    "18": {
      "L": "Behold, the blood of it was not brought in within the holy place: ye should indeed have eaten it in the sanctuary, as I commanded.",
      "M": "Its blood was not brought into the inner sanctuary, so you should certainly have eaten it in the sanctuary, as I commanded.",
      "T": "'Since its blood was not brought into the inner sanctuary, you were required to eat it in the holy place. That was the command.'"
    },
    "19": {
      "L": "And Aaron said unto Moses, Behold, this day have they offered their sin offering and their burnt offering before the LORD; and such things have befallen me: and if I had eaten the sin offering to day, should it have been accepted in the sight of the LORD?",
      "M": "Aaron said to Moses, Look — today they have offered their sin offering and their burnt offering before the LORD. Yet things like this have happened to me. If I had eaten the sin offering today, would it have been acceptable to the LORD?",
      "T": "Aaron answered Moses quietly: 'Today my sons offered their sin offering and burnt offering before the LORD. And look at what has happened to me. Could I have eaten the sin offering today — in this grief — and would the LORD have found it acceptable?'"
    },
    "20": {
      "L": "And when Moses heard that, he was content.",
      "M": "When Moses heard this, he was satisfied.",
      "T": "When Moses heard Aaron's answer, he accepted it."
    }
  },
  "11": {
    "1": {
      "L": "And the LORD spake unto Moses and to Aaron, saying unto them,",
      "M": "The LORD spoke to Moses and Aaron, saying to them,",
      "T": "The LORD spoke to Moses and Aaron together:"
    },
    "2": {
      "L": "Speak unto the children of Israel, saying, These are the beasts which ye shall eat among all the beasts that are on the earth.",
      "M": "Tell the people of Israel: These are the animals you may eat from among all the animals on earth.",
      "T": "Tell the people of Israel which land animals they may eat."
    },
    "3": {
      "L": "Whatsoever parteth the hoof, and is clovenfooted, and cheweth the cud, among the beasts, that shall ye eat.",
      "M": "Any animal that has a divided hoof, is completely split-hoofed, and chews the cud — that you may eat.",
      "T": "Any land animal that has a fully split hoof and chews its cud may be eaten."
    },
    "4": {
      "L": "Nevertheless these shall ye not eat of them that chew the cud, or of them that divide the hoof: as the camel, because he cheweth the cud, but divideth not the hoof; he is unclean unto you.",
      "M": "But among the cud-chewing and hoof-dividing animals, these you shall not eat: the camel — it chews the cud but does not have a divided hoof; it is unclean to you.",
      "T": "But these fail one of the two tests. The camel chews the cud but its hoof is not split — it is impure for you."
    },
    "5": {
      "L": "And the coney, because he cheweth the cud, but divideth not the hoof; he is unclean unto you.",
      "M": "The rock badger — it chews the cud but does not have a divided hoof; it is unclean to you.",
      "T": "The rock badger chews the cud but has no split hoof — it is impure for you."
    },
    "6": {
      "L": "And the hare, because he cheweth the cud, but divideth not the hoof; he is unclean unto you.",
      "M": "The hare — it chews the cud but does not have a divided hoof; it is unclean to you.",
      "T": "The hare chews the cud but has no split hoof — it is impure for you."
    },
    "7": {
      "L": "And the swine, though he divide the hoof, and be clovenfooted, yet he cheweth not the cud; he is unclean to you.",
      "M": "The pig — it has a divided, split hoof, but it does not chew the cud; it is unclean to you.",
      "T": "The pig has a fully split hoof but does not chew its cud — it is impure for you."
    },
    "8": {
      "L": "Of their flesh shall ye not eat, and their carcase shall ye not touch; they are unclean to you.",
      "M": "You shall not eat their flesh, and you shall not touch their carcasses; they are unclean to you.",
      "T": "Do not eat their meat. Do not even touch their carcasses — they are impure to you."
    },
    "9": {
      "L": "These shall ye eat of all that are in the waters: whatsoever hath fins and scales in the waters, in the seas, and in the rivers, them shall ye eat.",
      "M": "Of all that live in the water — in the seas and streams — you may eat whatever has fins and scales.",
      "T": "In the water — sea or river — eat whatever has both fins and scales."
    },
    "10": {
      "L": "And all that have not fins and scales in the seas, and in the rivers, of all that move in the waters, and of any living thing which is in the waters, they shall be an abomination unto you.",
      "M": "But anything in the seas or streams that does not have fins and scales — whether among the swarming creatures or the other living things in the waters — it is detestable to you.",
      "T": "Anything in the water without fins and scales — every swarming sea creature, every other water-dweller — is detestable to you."
    },
    "11": {
      "L": "They shall be even an abomination unto you; ye shall not eat of their flesh, but ye shall have their carcases in abomination.",
      "M": "They shall remain detestable to you; you shall not eat their flesh and you shall detest their carcasses.",
      "T": "They are to remain detestable — do not eat their flesh, and treat their carcasses as something repugnant."
    },
    "12": {
      "L": "Whatsoever hath no fins nor scales in the waters, that shall be an abomination unto you.",
      "M": "Everything in the waters that does not have fins and scales is detestable to you.",
      "T": "No fins, no scales — detestable."
    },
    "13": {
      "L": "And these are they which ye shall have in abomination among the fowls; they shall not be eaten, they are an abomination: the eagle, and the ossifrage, and the ospray,",
      "M": "These are the birds you shall detest; they must not be eaten — they are detestable: the eagle, the bearded vulture, the black vulture,",
      "T": "Among birds, these are detestable — do not eat them: the eagle, the bearded vulture, the black vulture,"
    },
    "14": {
      "L": "And the vulture, and the kite after his kind;",
      "M": "the red kite, the black kite of any kind,",
      "T": "the red kite, the black kite — any of their kind,"
    },
    "15": {
      "L": "Every raven after his kind;",
      "M": "every kind of raven,",
      "T": "every kind of raven,"
    },
    "16": {
      "L": "And the owl, and the night hawk, and the cuckow, and the hawk after his kind,",
      "M": "the horned owl, the screech owl, the sea gull, the hawk of any kind,",
      "T": "the horned owl, the screech owl, the sea gull, every kind of hawk,"
    },
    "17": {
      "L": "And the little owl, and the cormorant, and the great owl,",
      "M": "the little owl, the cormorant, the short-eared owl,",
      "T": "the little owl, the cormorant, the short-eared owl,"
    },
    "18": {
      "L": "And the swan, and the pelican, and the gier eagle,",
      "M": "the barn owl, the tawny owl, the carrion vulture,",
      "T": "the barn owl, the tawny owl, the carrion vulture,"
    },
    "19": {
      "L": "And the stork, the heron after her kind, and the lapwing, and the bat.",
      "M": "the stork, the heron of any kind, the hoopoe, and the bat.",
      "T": "the stork, every kind of heron, the hoopoe, and the bat."
    },
    "20": {
      "L": "All fowls that creep, going upon all four, shall be an abomination unto you.",
      "M": "All winged insects that go on all fours are detestable to you.",
      "T": "All winged insects that walk on four legs are detestable."
    },
    "21": {
      "L": "Yet these may ye eat of every flying creeping thing that goeth upon all four, which have legs above their feet, to leap withal upon the earth;",
      "M": "But among all the winged insects that go on all fours, you may eat those that have jointed legs above their feet for hopping on the ground —",
      "T": "However, some winged insects that walk on four legs you may eat — specifically those with jointed hind legs for leaping:"
    },
    "22": {
      "L": "Even these of them ye may eat; the locust after his kind, and the bald locust after his kind, and the beetle after his kind, and the grasshopper after his kind.",
      "M": "of them you may eat: the locust of any kind, the bald locust of any kind, the cricket of any kind, and the grasshopper of any kind.",
      "T": "any kind of locust, any kind of migratory locust, any kind of cricket, any kind of grasshopper — all of these may be eaten."
    },
    "23": {
      "L": "But all other flying creeping things, which have four feet, shall be an abomination unto you.",
      "M": "But all other winged insects with four feet are detestable to you.",
      "T": "All other four-legged winged insects are detestable."
    },
    "24": {
      "L": "And for these ye shall be unclean: whosoever toucheth the carcase of them shall be unclean until the even.",
      "M": "By these you will become unclean. Whoever touches their carcasses will be unclean until evening.",
      "T": "Contact with their carcasses makes you impure until evening."
    },
    "25": {
      "L": "And whosoever beareth ought of the carcase of them shall wash his clothes, and be unclean until the even.",
      "M": "Whoever picks up any part of their carcass must wash his clothes and will be unclean until evening.",
      "T": "Whoever carries any part of their carcass must wash his clothes and remains impure until evening."
    },
    "26": {
      "L": "The carcases of every beast which divideth the hoof, and is not clovenfooted, nor cheweth the cud, are unclean unto you: every one that toucheth them shall be unclean.",
      "M": "Every animal that has a divided hoof but is not completely split-hoofed, or does not chew the cud — their carcasses are unclean to you. Anyone who touches them will be unclean.",
      "T": "Any animal that divides the hoof partially but not fully, or that does not chew its cud — touching its carcass makes a person impure."
    },
    "27": {
      "L": "And whatsoever goeth upon his paws, among all manner of beasts that go on all four, those are unclean unto you: whoso toucheth their carcase shall be unclean until the even.",
      "M": "Every animal that walks on its paws among the four-footed animals is unclean to you. Whoever touches their carcass will be unclean until evening.",
      "T": "Among four-footed animals, any that walk on paws — cats, dogs, lions — are impure to you. Touch their carcasses: impure until evening."
    },
    "28": {
      "L": "And he that beareth the carcase of them shall wash his clothes, and be unclean until the even: they are unclean unto you.",
      "M": "Whoever carries their carcasses must wash his clothes and will be unclean until evening. They are unclean to you.",
      "T": "Carry their carcasses: wash your clothes, remain impure until evening."
    },
    "29": {
      "L": "These also shall be unclean unto you among the creeping things that creep upon the earth; the weasel, and the mouse, and the tortoise after his kind,",
      "M": "These are unclean to you among the creatures that move along the ground: the weasel, the mouse, the great lizard of any kind,",
      "T": "Among ground-crawling creatures, these are impure to you: the weasel, the mouse, the great lizard in any variety,"
    },
    "30": {
      "L": "And the ferret, and the chameleon, and the lizard, and the snail, and the mole.",
      "M": "the gecko, the monitor lizard, the wall lizard, the skink, and the chameleon.",
      "T": "the gecko, the monitor lizard, the wall lizard, the skink, and the chameleon."
    },
    "31": {
      "L": "These are unclean to you among all that creep: whosoever doth touch them, when they be dead, shall be unclean until the even.",
      "M": "These are unclean to you among all the swarming creatures. Whoever touches them after they have died will be unclean until evening.",
      "T": "These are impure to you among all swarming things. Touch a dead one: impure until evening."
    },
    "32": {
      "L": "And upon whatsoever any of them, when they are dead, doth fall, it shall be unclean; whether it be any vessel of wood, or raiment, or skin, or sack, whatsoever vessel it be, wherein any work is done, it must be put into water, and it shall be unclean until the even; so it shall be cleansed.",
      "M": "When one of them dies and falls on something — whether a wooden article, clothing, leather, or a sack — any article that can be used for any purpose must be immersed in water. It will be unclean until evening and then it will be clean.",
      "T": "If a dead one falls on any object — wooden utensil, garment, leather item, sack — that object must be soaked in water. It remains impure until evening, then it is clean."
    },
    "33": {
      "L": "And every earthen vessel, whereinto any of them falleth, whatsoever is in it shall be unclean; and ye shall break it.",
      "M": "If any of them falls into a clay pot, everything in it becomes unclean, and you must break the pot.",
      "T": "If one falls into a clay pot, everything inside it is impure — and the pot itself must be smashed."
    },
    "34": {
      "L": "Of all meat which may be eaten, that on which such water cometh shall be unclean: and all drink that may be drunk in every such vessel shall be unclean.",
      "M": "Any food that could be eaten and that has been dampened by water from such a vessel will be unclean. Any liquid that could be drunk from such a vessel will be unclean.",
      "T": "Any edible food that water from such a vessel touches becomes impure. Any drinkable liquid from such a vessel is impure."
    },
    "35": {
      "L": "And every thing whereupon any part of their carcase falleth shall be unclean; whether it be oven, or ranges for pots, they shall be broken down: for they are unclean, and shall be unclean unto you.",
      "M": "Anything on which part of their carcass falls will be unclean. An oven or cooking range must be torn down; they are unclean and will remain unclean for you.",
      "T": "If any part of their carcass falls on an oven or cooking stove, it must be demolished — such things become permanently impure."
    },
    "36": {
      "L": "Nevertheless a fountain or pit, wherein there is plenty of water, shall be clean: but that which toucheth their carcase shall be unclean.",
      "M": "A spring or cistern collecting water will remain clean, but anyone who touches a carcass in it will be unclean.",
      "T": "A natural spring or a cistern remains clean even if a carcass falls into it — but whoever touches the carcass in the water becomes impure."
    },
    "37": {
      "L": "And if any part of their carcase fall upon any sowing seed which is to be sown, it shall be clean.",
      "M": "If any part of their carcass falls on seed that is to be planted, the seed remains clean.",
      "T": "If a carcass falls on dry seed grain set aside for planting, the seed remains clean."
    },
    "38": {
      "L": "But if any water be put upon the seed, and any part of their carcase fall thereon, it shall be unclean unto you.",
      "M": "But if water has been put on the seed and a part of their carcass falls on it, the seed is unclean to you.",
      "T": "But if the seed has been wet and a carcass falls on it, it becomes impure."
    },
    "39": {
      "L": "And if any beast, of which ye may eat, die; he that toucheth the carcase thereof shall be unclean until the even.",
      "M": "If an animal that you are allowed to eat dies, whoever touches its carcass will be unclean until evening.",
      "T": "Even a clean animal that dies naturally — touch its carcass and you are impure until evening."
    },
    "40": {
      "L": "And he that eateth of the carcase of it shall wash his clothes, and be unclean until the even: he also that beareth the carcase of it shall wash his clothes, and be unclean until the even.",
      "M": "Anyone who eats from its carcass must wash his clothes and will be unclean until evening. Anyone who picks up the carcass must wash his clothes and will be unclean until evening.",
      "T": "Eat from its carcass: wash your clothes, impure until evening. Carry its carcass: wash your clothes, impure until evening."
    },
    "41": {
      "L": "And every creeping thing that creepeth upon the earth shall be an abomination; it shall not be eaten.",
      "M": "Every creature that swarms on the ground is detestable; it must not be eaten.",
      "T": "Every ground-swarming creature is detestable — none may be eaten."
    },
    "42": {
      "L": "Whatsoever goeth upon the belly, and whatsoever goeth upon all four, or whatsoever hath more feet among all creeping things that creep upon the earth, them ye shall not eat; for they are an abomination.",
      "M": "Whatever moves on its belly, whatever goes on all fours, whatever has many feet — every creature that swarms on the ground — you shall not eat, for they are detestable.",
      "T": "Anything that slithers on its belly, walks on four legs, or has many legs — any ground-swarming creature — is detestable and may not be eaten."
    },
    "43": {
      "L": "Ye shall not make yourselves abominable with any creeping thing that creepeth, neither shall ye make yourselves unclean with them, that ye should be defiled thereby.",
      "M": "Do not defile yourselves by any of the swarming creatures; do not make yourselves unclean by means of them or become impure through them.",
      "T": "Do not make yourselves detestable by eating any swarming thing. Do not defile yourselves through them."
    },
    "44": {
      "L": "For I am the LORD your God: ye shall therefore sanctify yourselves, and ye shall be holy; for I am holy: neither shall ye defile yourselves with any manner of creeping thing that creepeth upon the earth.",
      "M": "For I am the LORD your God. Consecrate yourselves and be holy, because I am holy. Do not defile yourselves with any swarming creature that moves on the ground.",
      "T": "For I am the LORD your God. Set yourselves apart — be holy — because I am holy. Do not defile yourselves with any ground-crawling creature."
    },
    "45": {
      "L": "For I am the LORD that bringeth you up out of the land of Egypt, to be your God: ye shall therefore be holy, for I am holy.",
      "M": "For I am the LORD who brought you up out of Egypt to be your God; therefore be holy, because I am holy.",
      "T": "I am the LORD who brought you up out of Egypt to be your God. I am holy — therefore you must be holy."
    },
    "46": {
      "L": "This is the law of the beasts, and of the fowl, and of every living creature that moveth in the waters, and of every creature that creepeth upon the earth:",
      "M": "This is the law concerning animals, birds, every living creature that moves through the water, and every creature that swarms on the ground,",
      "T": "This is the comprehensive ruling covering land animals, birds, every creature that moves through water, and every swarming ground creature —"
    },
    "47": {
      "L": "To make a difference between the unclean and the clean, and between the beast that may be eaten and the beast that may not be eaten.",
      "M": "to make a distinction between the unclean and the clean, and between the living creatures that may be eaten and those that may not be eaten.",
      "T": "establishing the difference between the impure and the pure, between what Israel may eat and what they must not touch."
    }
  },
  "12": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, saying, If a woman have conceived seed, and born a man child: then she shall be unclean seven days; according to the days of the separation for her infirmity shall she be unclean.",
      "M": "Tell the people of Israel: When a woman conceives and gives birth to a boy, she will be unclean for seven days — the same as during the time of her monthly separation.",
      "T": "Tell Israel: when a woman bears a son, she is impure for seven days — the same length as her menstrual impurity."
    },
    "3": {
      "L": "And in the eighth day the flesh of his foreskin shall be circumcised.",
      "M": "On the eighth day the boy's foreskin shall be circumcised.",
      "T": "On the eighth day the boy shall be circumcised."
    },
    "4": {
      "L": "And she shall then continue in the blood of her purifying three and thirty days; she shall touch no hallowed thing, nor come into the sanctuary, until the days of her purifying be fulfilled.",
      "M": "Then she shall remain in a state of blood purification for thirty-three days. She must not touch anything holy or enter the sanctuary until her days of purification are complete.",
      "T": "After those seven days she enters a thirty-three-day purification period. During this time she may not touch anything consecrated or enter the sanctuary — until the full purification is complete."
    },
    "5": {
      "L": "But if she bear a maid child, then she shall be unclean two weeks, as in her separation: and she shall continue in the blood of her purifying three score and six days.",
      "M": "If she gives birth to a girl, she will be unclean for two weeks, as during her menstruation. Then she shall continue in her blood purification for sixty-six days.",
      "T": "If she bears a daughter, the initial impurity is two weeks — double — and the subsequent purification period is sixty-six days."
    },
    "6": {
      "L": "And when the days of her purifying are fulfilled, for a son, or for a daughter, she shall bring a lamb of the first year for a burnt offering, and a young pigeon, or a turtledove, for a sin offering, unto the door of the tabernacle of the congregation, unto the priest:",
      "M": "When the days of her purification are complete — for a son or a daughter — she shall bring to the priest at the entrance of the tent of meeting a yearling lamb as a burnt offering and a young pigeon or turtledove as a sin offering.",
      "T": "When the purification period ends — whether for a son or a daughter — she brings two offerings to the priest at the tent of meeting: a yearling lamb as a burnt offering and a young pigeon or turtledove as a sin offering."
    },
    "7": {
      "L": "Who shall offer it before the LORD, and make an atonement for her; and she shall be cleansed from the issue of her blood. This is the law for her that hath born a male or a female.",
      "M": "The priest shall offer it before the LORD and make atonement for her, and she will be clean from her flow of blood. This is the law for the woman who gives birth to a boy or a girl.",
      "T": "The priest presents both before the LORD and makes atonement for her. She is then ritually clean from her blood discharge. This is the ruling for any mother, whether her child is a son or a daughter."
    },
    "8": {
      "L": "And if she be not able to bring a lamb, then she shall bring two turtles, or two young pigeons; the one for the burnt offering, and the other for a sin offering: and the priest shall make an atonement for her, and she shall be clean.",
      "M": "If she cannot afford a lamb, she shall bring two turtledoves or two young pigeons — one for a burnt offering and the other for a sin offering. The priest shall make atonement for her, and she will be clean.",
      "T": "If a lamb is beyond her means, two turtledoves or two young pigeons serve the same purpose — one for the burnt offering, one for the sin offering. The priest makes atonement, and she is clean. No mother is barred from purification by poverty."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'leviticus')
        merge_tier(existing, LEVITICUS, tier_key)
        save(tier_dir, 'leviticus', existing)
    print('Leviticus 7–12 written.')

if __name__ == '__main__':
    main()
