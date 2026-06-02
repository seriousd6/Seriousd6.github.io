"""
MKT Leviticus chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-leviticus-13-18.py

Covers: skin-disease diagnosis laws (ch. 13), skin-disease purification rites (ch. 14),
bodily-discharge laws (ch. 15), the Day of Atonement / Yom Kippur (ch. 16), blood laws (ch. 17),
forbidden sexual relations (ch. 18).

Translation decisions (carrying forward from mkt-leviticus-7-12.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — consistent with prior scripts
- H430 (אֱלֹהִים): "God" in all three tiers
- H2403 (חַטָּאת): "sin offering" in all three tiers
- H817 (אָשָׁם): L/M="guilt offering"; T="reparation offering"
- H5930 (עֹלָה): "burnt offering" in all three tiers
- H8002 (שֶׁלֶם): L="peace offering"; M/T="fellowship offering"
- H4503 (מִנְחָה): "grain offering" in all three tiers
- H3722 (כָּפַר): L/M="make atonement"; T="atone" or "make atonement"
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" in all three tiers
- H6944 (קֹדֶשׁ): "holy" in L/M; T context-sensitive
- H2931/H2889 (טָמֵא/טָהוֹר): L/M="unclean/clean"; T="impure/pure" or "defiled/clean"

New contested terms in chapters 13–18:
- H6883 (צָרַעַת) tsara'at: L/M="skin disease" (NOT "leprosy" — modern lepra/Hansen's disease is
  a different pathology; tsara'at includes fungal conditions, eczema, and other dermatoses);
  T="defiling skin disease" or "scale disease" — the priestly category covers skin, cloth, and
  house surfaces, making a biological identification impossible.
- H5061 (נֶגַע) nega': L/M="mark/affliction" (context: "the mark" when referring to a specific
  lesion, "affliction" in general diagnostic phrasing); T="the diseased mark" or "the affliction"
- H934 (בַּהֶרֶת) baheret: L/M="bright spot"; T="gleaming patch" — a specific lesion type
- H7613 (שְׂאֵת) se'et: L="swelling/rising"; M/T="swelling" — another lesion type
- H4556 (מִסְפַּחַת) sappahat: L/M="scab"; T="eruption" — a third lesion type
- H5799 (עֲזָאזֵל) Azazel (16:8,10,26): The most disputed term in Leviticus. Possible readings:
  (a) proper name of a wilderness demon (Milgrom, Levine); (b) "for removal/dismissal" (Tawil);
  (c) "the goat of departure" (LXX). The scapegoat carries Israel's confessed sin to a "cut-off"
  place. L/M="Azazel" (preserve the term); T="the wilderness wilderness — the goat of removal";
  the ritual effect (transfer and elimination of sin) is foregrounded in T.
- H3727 (כַּפֹּרֶת) kapporet: L/M="atonement cover"; T="the cover that atones / the mercy seat" —
  from H3722 kaphar; the golden lid of the ark where blood is sprinkled on Yom Kippur; KJV "mercy
  seat" is interpretively rich but opaque; "atonement cover" follows modern scholarship (NIV, ESV).
- H6172 (עֶרְוָה) ervah: "nakedness" — the euphemism throughout ch. 18 for sexual relations and
  the genitals; "to uncover nakedness" = to have sexual intercourse. L="nakedness"; M="nakedness
  (sexual relations)"; T="intimate relations" or "nakedness" depending on context.
- H4432 (מֹלֶךְ) Molech (18:21): The Ammonite deity associated with child sacrifice. L/M="Molech";
  T="Molech" — the name is retained in all tiers; the act condemned is giving children to pass
  through fire as an offering.
- H5315 (נֶפֶשׁ) nephesh (17:11,14): L="life/soul"; M="life"; T="the life-force" — in ch. 17 the
  classic nephesh-in-the-blood statement explains the blood prohibition: blood carries the life.
- H5079 (נִדָּה) niddah (15:19ff, 18:19): L/M="menstrual separation"; T="menstrual impurity" —
  the monthly separation period; the term implies withdrawal, not shame.
- H2154 (זִמָּה) zimmah (18:17): L/M="depravity"; T="moral corruption"
- H8397 (תֶּבֶל) tevel (18:23): L/M="perversion"; T="a confusion of kinds" — the term connotes
  mixing categories that belong separate (like kilayim); used for bestiality specifically.
- H8441 (תּוֹעֵבָה) to'evah: L/M="abomination"; T="an abomination" — already handled; the term
  describes acts that are ritually and morally repugnant to God
- Day of Atonement affliction (H6031 עָנָה): L="afflict yourselves"; M="practice self-denial";
  T="fast and humble yourselves" — the idiom refers to fasting and penitential practices.
- H8167 (שַׁבַּת שַׁבָּתוֹן) shabbat shabbaton (16:31): L="a Sabbath of solemn rest";
  M="a solemn Sabbath of complete rest"; T="a day of full Sabbath rest and fasting" — a
  heightened Sabbath form indicating maximum observance.
- House disease (14:33-53): The application of tsara'at to houses is unique. The priestly category
  is extended to structures — perhaps mold, salt efflorescence, or mineral staining. T treats it
  as a "defiling growth" without over-specifying the pathology.
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
  "13": {
    "1": {
      "L": "And the LORD spake unto Moses and Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD spoke to Moses and Aaron together:"
    },
    "2": {
      "L": "When a man shall have in the skin of his flesh a rising, a scab, or bright spot, and it be in the skin of his flesh like the plague of leprosy; then he shall be brought unto Aaron the priest, or unto one of his sons the priests:",
      "M": "When a person has a swelling, scab, or bright spot on the skin of his body, and it resembles a skin disease, he shall be brought to Aaron the priest or to one of his sons the priests.",
      "T": "If anyone develops a swelling, an eruption, or a gleaming patch on the skin of the body that looks like a defiling skin disease, he must be brought to Aaron the priest or one of his priestly sons."
    },
    "3": {
      "L": "And the priest shall look on the plague in the skin of the flesh: and when the hair in the plague is turned white, and the plague in sight be deeper than the skin of his flesh, it is a plague of leprosy: and the priest shall look on him, and pronounce him unclean.",
      "M": "The priest shall examine the mark on the skin of his body. If the hair in the mark has turned white and the mark appears to be deeper than the skin, it is a skin disease. When the priest has examined him, he shall pronounce him unclean.",
      "T": "The priest examines the mark on the skin. If the hair in the affected area has turned white and the lesion appears to go deeper than the surrounding skin, it is a defiling skin disease — the priest pronounces him impure."
    },
    "4": {
      "L": "If the bright spot be white in the skin of his flesh, and in sight be not deeper than the skin, and the hair thereof be not turned white; then the priest shall shut up him that hath the plague seven days:",
      "M": "But if the bright spot is white on the skin of his body and does not appear deeper than the skin, and its hair has not turned white, the priest shall isolate the affected person for seven days.",
      "T": "If the gleaming patch is white but not visibly deeper than the skin, and the hair in it has not turned white, the priest places the person under a seven-day watch."
    },
    "5": {
      "L": "And the priest shall look on him the seventh day: and, behold, if the plague in his sight be at a stay, and the plague spread not in the skin; then the priest shall shut him up seven days more:",
      "M": "On the seventh day the priest shall examine him, and if the mark looks unchanged and has not spread in the skin, the priest shall isolate him for another seven days.",
      "T": "On the seventh day the priest examines him again. If the mark looks the same and has not spread, he extends the isolation another seven days."
    },
    "6": {
      "L": "And the priest shall look on him again the seventh day: and, behold, if the plague be somewhat dark, and the plague spread not in the skin, the priest shall pronounce him clean: it is but a scab: and he shall wash his clothes, and be clean.",
      "M": "And the priest shall examine him again on the seventh day, and if the mark has faded and has not spread in the skin, the priest shall pronounce him clean; it is only a scab. He shall wash his clothes and be clean.",
      "T": "At the end of the second seven days, if the mark has faded and not spread, the priest declares him clean — it was only an eruption. He washes his clothes and is clean."
    },
    "7": {
      "L": "But if the scab spread much abroad in the skin, after that he hath been seen of the priest for his cleansing, he shall be seen of the priest again:",
      "M": "But if the scab has spread widely on the skin after the priest examined him for his cleansing, he shall appear before the priest again.",
      "T": "But if the eruption has spread considerably after the priest examined him for his cleansing, he must return for another examination."
    },
    "8": {
      "L": "And if the priest see that, behold, the scab spreadeth in the skin, then the priest shall pronounce him unclean: it is a leprosy.",
      "M": "If the priest examines and the scab has spread in the skin, the priest shall pronounce him unclean: it is a skin disease.",
      "T": "If the priest sees that the eruption has spread, he pronounces the person impure — it is a defiling skin disease."
    },
    "9": {
      "L": "When the plague of leprosy is in a man, then he shall be brought unto the priest;",
      "M": "When a skin disease is on a person, he shall be brought to the priest.",
      "T": "Whenever someone has a defiling skin disease, he is brought to the priest."
    },
    "10": {
      "L": "And the priest shall see him: and, behold, if the rising be white in the skin, and it have turned the hair white, and there be quick raw flesh in the rising;",
      "M": "The priest shall examine him, and if the swelling is white in the skin and has turned the hair white and there is raw exposed flesh in the swelling,",
      "T": "The priest examines him. If the swelling is white, the hair in it has turned white, and raw flesh is visible in the swelling —"
    },
    "11": {
      "L": "It is an old leprosy in the skin of his flesh, and the priest shall pronounce him unclean, and shall not shut him up: for he is unclean.",
      "M": "it is a chronic skin disease in the skin of his body, and the priest shall pronounce him unclean. He shall not isolate him, for he is already unclean.",
      "T": "this is a long-established skin disease. The priest pronounces him impure without quarantine — the disease is clearly established."
    },
    "12": {
      "L": "And if a leprosy break out abroad in the skin, and the leprosy cover all the skin of him that hath the plague from his head even to his foot, wheresoever the priest looketh;",
      "M": "But if the skin disease breaks out and covers all the skin of the afflicted person from head to foot, everywhere the priest looks,",
      "T": "But if the disease breaks out and spreads to cover the entire body — from head to foot, wherever the priest looks —"
    },
    "13": {
      "L": "Then the priest shall consider: and, behold, if the leprosy have covered all his flesh, he shall pronounce him clean that hath the plague: it is all turned white: he is clean.",
      "M": "then the priest shall examine him, and if the disease has covered all his body, he shall pronounce him clean. Since it has all turned white, he is clean.",
      "T": "the priest makes his assessment: if the disease has covered the entire body and turned it white, he pronounces the person clean. Complete whitening, paradoxically, signals cleanliness."
    },
    "14": {
      "L": "But when raw flesh appeareth in him, he shall be unclean.",
      "M": "But when raw flesh appears on him, he shall be unclean.",
      "T": "The moment raw flesh appears, however, he is impure."
    },
    "15": {
      "L": "And the priest shall see the raw flesh, and pronounce him unclean: for the raw flesh is unclean: it is a leprosy.",
      "M": "The priest shall examine the raw flesh and pronounce him unclean: the raw flesh is unclean; it is a skin disease.",
      "T": "The priest sees the raw flesh and pronounces him impure — raw flesh is a mark of active disease."
    },
    "16": {
      "L": "Or if the raw flesh turn again, and be changed unto white, he shall come unto the priest;",
      "M": "But if the raw flesh turns white again, he shall come to the priest,",
      "T": "If the raw flesh later turns white, he returns to the priest."
    },
    "17": {
      "L": "And the priest shall see him: and, behold, if the plague be turned into white; then the priest shall pronounce him clean that hath the plague: he is clean.",
      "M": "and the priest shall examine him. If the mark has turned white, the priest shall pronounce the afflicted person clean: he is clean.",
      "T": "The priest examines him. If the whole affected area has turned white, the priest pronounces him clean."
    },
    "18": {
      "L": "The flesh also, in which, even in the skin thereof, was a boil, and is healed,",
      "M": "When the body has a boil on the skin and it heals,",
      "T": "When a boil has appeared on the body and healed,"
    },
    "19": {
      "L": "And in the place of the boil there be a white rising, or a bright spot, white and somewhat reddish, and it be shewed to the priest;",
      "M": "but in the place of the boil there is a white swelling or a reddish-white bright spot, he shall show it to the priest.",
      "T": "but a white swelling or a reddish-white gleaming patch appears in the healed spot, the person shows it to the priest."
    },
    "20": {
      "L": "And if, when the priest seeth it, behold, it be in sight lower than the skin, and the hair thereof be turned white; the priest shall pronounce him unclean: it is a plague of leprosy broken out of the boil.",
      "M": "If the priest examines it and it appears deeper than the surrounding skin and its hair has turned white, the priest shall pronounce him unclean: it is a skin disease that has broken out in the boil.",
      "T": "If the priest sees it is deeper than the surrounding skin and the hair in it has turned white, he pronounces the person impure — a skin disease has erupted at the site of the old boil."
    },
    "21": {
      "L": "But if the priest look on it, and, behold, there be no white hairs therein, and if it be not lower than the skin, but be somewhat dark; then the priest shall shut him up seven days:",
      "M": "But if the priest examines it and finds no white hair in it, it is not deeper than the skin, and it has faded, the priest shall isolate him for seven days.",
      "T": "But if the priest finds no white hair in it, it is no deeper than the skin, and it has faded, the person is quarantined seven days."
    },
    "22": {
      "L": "And if it spread much abroad in the skin, then the priest shall pronounce him unclean: it is a plague.",
      "M": "If it spreads widely in the skin, the priest shall pronounce him unclean: it is a diseased mark.",
      "T": "If it spreads, the priest pronounces him impure — it is a diseased mark."
    },
    "23": {
      "L": "But if the bright spot stay in his place, and spread not, it is a burning boil; and the priest shall pronounce him clean.",
      "M": "But if the bright spot remains in one place and has not spread, it is the scar of the boil, and the priest shall pronounce him clean.",
      "T": "If the gleaming patch stays put and has not spread, it is simply the scar of the healed boil — the priest pronounces the person clean."
    },
    "24": {
      "L": "Or if there be any flesh, in the skin whereof there is a hot burning, and the quick flesh that burneth have a white bright spot, somewhat reddish, or white;",
      "M": "When the body has a burn scar on the skin and the raw flesh of the burn becomes a reddish-white or white bright spot,",
      "T": "When someone has been burned and the scar develops a reddish-white or white gleaming patch in the healing flesh,"
    },
    "25": {
      "L": "Then the priest shall look upon it: and, behold, if the hair in the bright spot be turned white, and it appear deeper than the skin; it is a leprosy broken out of the burning: wherefore the priest shall pronounce him unclean: it is the plague of leprosy.",
      "M": "the priest shall examine it. If the hair in the bright spot has turned white and it appears deeper than the skin, it is a skin disease that has erupted in the burn. The priest shall pronounce him unclean: it is a skin disease.",
      "T": "the priest examines it. If the hair in the patch has turned white and the lesion appears deeper than the skin, a defiling skin disease has erupted in the burn wound — the priest pronounces him impure."
    },
    "26": {
      "L": "But if the priest look on it, and, behold, there be no white hair in the bright spot, and it be no lower than the skin, but be somewhat dark; then the priest shall shut him up seven days:",
      "M": "But if the priest examines it and there is no white hair in the bright spot, it is not deeper than the skin, and it has faded, the priest shall isolate him for seven days.",
      "T": "But if there is no white hair in it, it is no deeper than the skin, and it has faded — seven days of quarantine."
    },
    "27": {
      "L": "And the priest shall look upon him the seventh day: and if it be spread much abroad in the skin, then the priest shall pronounce him unclean: it is the plague of leprosy.",
      "M": "On the seventh day the priest shall examine him. If it has spread widely in the skin, the priest shall pronounce him unclean: it is a skin disease.",
      "T": "On the seventh day, if the patch has spread significantly, the priest pronounces impurity — it is a skin disease."
    },
    "28": {
      "L": "And if the bright spot stay in his place, and spread not in the skin, but it be somewhat dark; it is a rising of the burning, and the priest shall pronounce him clean: for it is an inflammation of the burning.",
      "M": "But if the bright spot has stayed in its place and has not spread in the skin, and has faded, it is the swelling from the burn. The priest shall pronounce him clean: it is the scar of the burn.",
      "T": "But if the patch has stayed in place, has not spread, and has faded, it is the residual swelling from the burn — not a disease. The priest pronounces the person clean."
    },
    "29": {
      "L": "If a man or woman have a plague upon the head or the beard;",
      "M": "When a man or a woman has a mark on the head or the chin,",
      "T": "When anyone — man or woman — develops a mark on the scalp or chin area,"
    },
    "30": {
      "L": "Then the priest shall see the plague: and, behold, if it be in sight deeper than the skin; and there be in it a yellow thin hair; then the priest shall pronounce him unclean: it is a dry scall, even a leprosy upon the head or beard.",
      "M": "the priest shall examine the mark. If it appears deeper than the skin and there is thin yellow hair in it, the priest shall pronounce him unclean. It is a scall — a skin disease of the head or chin.",
      "T": "the priest examines it. If it appears deeper than the skin and contains thin, yellowish hair, the priest pronounces impurity — it is a scalp itch, a skin disease of the head or chin area."
    },
    "31": {
      "L": "And if the priest look on the plague of the scall, and, behold, it be not in sight deeper than the skin, and that there be no black hair in it; then the priest shall shut up him that hath the plague of the scall seven days:",
      "M": "But if the priest examines the itch and it does not appear deeper than the skin and there is no black hair in it, the priest shall isolate the person with the itch for seven days.",
      "T": "But if the itch appears no deeper than the skin and contains no black hair, the person is placed under seven-day quarantine."
    },
    "32": {
      "L": "And in the seventh day the priest shall look at the plague: and, behold, if the scall spread not, and there be in it no yellow hair, and the scall be not in sight deeper than the skin;",
      "M": "On the seventh day the priest shall examine the mark. If the itch has not spread and there is no yellow hair in it and the itch appears no deeper than the skin,",
      "T": "On the seventh day, if the itch has not spread, still shows no yellow hair, and is no deeper than the skin —"
    },
    "33": {
      "L": "He shall be shaven, but the scall shall he not shave; and the priest shall shut up him that hath the scall yet other seven days:",
      "M": "he shall shave himself, but he shall not shave the itch area. The priest shall isolate him who has the itch for another seven days.",
      "T": "the person shaves all hair except the affected patch, and the priest extends the quarantine another seven days."
    },
    "34": {
      "L": "And in the seventh day the priest shall look on the scall: and, behold, if the scall be not spread in the skin, nor be in sight deeper than the skin; then the priest shall pronounce him clean: and he shall wash his clothes, and be clean.",
      "M": "On the seventh day the priest shall examine the itch. If the itch has not spread in the skin and does not appear deeper than the skin, the priest shall pronounce him clean. He shall wash his clothes and be clean.",
      "T": "On the seventh day, if the itch has not spread and remains no deeper than the skin, the priest pronounces him clean. He washes his clothes and is clean."
    },
    "35": {
      "L": "But if the scall spread much in the skin after his cleansing;",
      "M": "But if the itch spreads widely in the skin after his cleansing,",
      "T": "If the itch spreads significantly after the priest has declared cleanliness —"
    },
    "36": {
      "L": "Then the priest shall look on him: and, behold, if the scall be spread in the skin, the priest shall not seek for yellow hair; he is unclean.",
      "M": "the priest shall examine him. If the itch has spread in the skin, the priest need not look for yellow hair: he is unclean.",
      "T": "the priest examines him again. If it has spread, the yellow-hair test is unnecessary — the spread itself establishes impurity."
    },
    "37": {
      "L": "But if the scall be in his sight at a stay, and that there be black hair grown up therein; the scall is healed, he is clean: and the priest shall pronounce him clean.",
      "M": "But if the itch appears unchanged and black hair has grown in it, the itch is healed — he is clean. The priest shall pronounce him clean.",
      "T": "But if the itch appears stable and black hair has grown back in it, the itch is healed — the priest pronounces him clean."
    },
    "38": {
      "L": "If a man also or a woman have in the skin of their flesh bright spots, even white bright spots;",
      "M": "When a man or woman has bright spots on the skin of the body — white bright spots —",
      "T": "When a man or woman has white gleaming patches on the skin of the body,"
    },
    "39": {
      "L": "Then the priest shall look: and, behold, if the bright spots in the skin of their flesh be darkish white; it is a freckled spot that groweth in the skin; he is clean.",
      "M": "the priest shall examine them. If the bright spots on the skin are dull white, it is a harmless eruption that has broken out in the skin — the person is clean.",
      "T": "the priest examines them. If the patches are dull, faded white, it is a harmless surface eruption — the person is clean."
    },
    "40": {
      "L": "And the man whose hair is fallen off his head, he is bald; yet is he clean.",
      "M": "If a man's hair has fallen from his head, he is bald, but he is clean.",
      "T": "Baldness from the top of the head is not a disease — the man is clean."
    },
    "41": {
      "L": "And he that hath his hair fallen off from the part of his head toward his face, he is forehead bald: yet is he clean.",
      "M": "If he has lost hair from the front of his head, he has a receding hairline, but he is clean.",
      "T": "Frontal baldness likewise makes no one impure — clean."
    },
    "42": {
      "L": "And if there be in the bald head, or bald forehead, a white reddish sore; it is a leprosy sprung up in his bald head, or his bald forehead.",
      "M": "But if there is a reddish-white mark on the bald head or bald forehead, it is a skin disease erupting on the bald head or forehead.",
      "T": "But if a reddish-white mark appears on the bald scalp or bald forehead, a defiling skin disease has broken out there."
    },
    "43": {
      "L": "Then the priest shall look upon it: and, behold, if the rising of the sore be white reddish in his bald head, or in his bald forehead, as the leprosy appeareth in the skin of the flesh;",
      "M": "The priest shall examine him. If the swelling of the mark is reddish-white on his bald head or bald forehead and appears like a skin disease in the skin of the body,",
      "T": "The priest examines it. If the swelling on the bald area is reddish-white and looks the same as a skin disease on the body —"
    },
    "44": {
      "L": "He is a leprous man, he is unclean: the priest shall pronounce him utterly unclean; his plague is in his head.",
      "M": "the man has a skin disease; he is unclean. The priest shall pronounce him unclean: his affliction is on his head.",
      "T": "the man has a defiling skin disease and is impure. The priest pronounces him unclean — the affliction is on his head."
    },
    "45": {
      "L": "And the leper in whom the plague is, his clothes shall be rent, and his head bare, and he shall put a covering upon his upper lip, and shall cry, Unclean, unclean.",
      "M": "The person who has the skin disease shall wear torn clothes, let his hair hang loose, cover his upper lip, and cry out, 'Unclean! Unclean!'",
      "T": "The person declared impure must wear torn clothing, keep his hair disheveled, cover his mouth, and call out wherever he goes: 'Unclean! Unclean!' — the outward signs of ritual exclusion."
    },
    "46": {
      "L": "All the days wherein the plague shall be in him he shall be defiled; he is unclean: he shall dwell alone; without the camp shall his habitation be.",
      "M": "He shall remain unclean all the days he has the disease. He is unclean and must live apart — his dwelling place shall be outside the camp.",
      "T": "For as long as the disease is active, he is impure. He lives alone, outside the camp — separated from the covenant community until the disease is healed."
    },
    "47": {
      "L": "The garment also that the plague of leprosy is in, whether it be a woollen garment, or a linen garment;",
      "M": "When a skin disease mark appears on a garment — whether a wool garment or a linen garment,",
      "T": "The priestly category of defiling skin disease extends to garments — wool or linen:"
    },
    "48": {
      "L": "Whether it be in the warp, or woof; of linen, or of woollen; whether in a skin, or in any thing made of skin;",
      "M": "in the warp or the woof of linen or wool, or in leather or any article made of leather —",
      "T": "in the warp threads or the woof threads of linen or wool, or in leather goods of any kind —"
    },
    "49": {
      "L": "And if the plague be greenish or reddish in the garment, or in the skin, either in the warp, or in the woof, or in any thing of skin; it is a plague of leprosy, and shall be shewed unto the priest:",
      "M": "if the mark on the garment, leather, warp, woof, or any leather article is greenish or reddish, it is a mark of skin disease and must be shown to the priest.",
      "T": "if the mark is greenish or reddish — on garment, leather, warp, or woof — it is a diseased mark and must be brought to the priest."
    },
    "50": {
      "L": "And the priest shall look upon the plague, and shut up it that hath the plague seven days:",
      "M": "The priest shall examine the mark and quarantine the afflicted article for seven days.",
      "T": "The priest examines it and quarantines the afflicted article for seven days."
    },
    "51": {
      "L": "And he shall look on the plague on the seventh day: if the plague be spread in the garment, either in the warp, or in the woof, or in a skin, or in any work that is made of skin; the plague is a fretting leprosy; it is unclean.",
      "M": "On the seventh day he shall examine the mark. If the mark has spread on the garment — in the warp, the woof, the leather, or any leather article — the mark is a malignant skin disease; it is unclean.",
      "T": "On the seventh day, if the mark has spread through the fabric or leather, it is a destructive disease — the article is impure."
    },
    "52": {
      "L": "He shall therefore burn that garment, whether warp or woof, in woollen or in linen, or any thing of skin, wherein the plague is: for it is a fretting leprosy; it shall be burnt in the fire.",
      "M": "He shall burn the garment — whether in warp or woof, wool or linen — or any leather article in which the mark appears. For it is a malignant skin disease; it must be burned up with fire.",
      "T": "Burn it — garment, warp, woof, wool, linen, or leather — whatever carries the destructive mark. Fire, not quarantine."
    },
    "53": {
      "L": "And if the priest shall look, and, behold, the plague have not spread in the garment, either in the warp, or in the woof, or in any thing of skin;",
      "M": "But if the priest examines and the mark has not spread in the garment — in the warp, woof, or any leather —",
      "T": "But if the priest finds the mark has not spread in the garment, warp, woof, or leather —"
    },
    "54": {
      "L": "Then the priest shall command that they wash the thing wherein the plague is, and he shall shut it up seven days more:",
      "M": "the priest shall command that the afflicted article be washed and shall quarantine it for another seven days.",
      "T": "he orders the afflicted article washed and imposes another seven days of quarantine."
    },
    "55": {
      "L": "And the priest shall look on the plague, after that it is washed: and, behold, if the plague have not changed his colour, and the plague be not spread; it is unclean; thou shalt burn it in the fire; it is fret inward, whether it be bare within or without.",
      "M": "The priest shall examine the mark after it has been washed. If the mark has not changed its appearance and has not spread, it is unclean; you shall burn it with fire. It is a deep stain — whether on the inside or outside of the fabric.",
      "T": "After washing, if the mark has not faded and has not spread, it is impure — burn it. Whether the discoloration is inside or outside the weave, it is a deep-seated stain."
    },
    "56": {
      "L": "And if the priest look, and, behold, the plague be somewhat dark after the washing of it; then he shall rend it out of the garment, or out of the skin, or out of the warp, or out of the woof:",
      "M": "But if the priest examines it after washing and the mark has faded, he shall tear out that part from the garment, the leather, the warp, or the woof.",
      "T": "If after washing the mark has visibly faded, the priest tears that section out of the garment or leather."
    },
    "57": {
      "L": "And if it appear still in the garment, either in the warp, or in the woof, or in any thing of skin; it is a spreading plague: thou shalt burn that wherein the plague is with fire.",
      "M": "But if it still appears in the garment — in the warp, woof, or any leather article — it is a spreading mark; burn with fire the article in which the mark appears.",
      "T": "If the mark keeps reappearing in the garment, warp, woof, or leather, it is spreading — burn that article."
    },
    "58": {
      "L": "And the garment, either warp, or woof, or whatsoever thing of skin it be, which thou shalt wash, if the plague be departed from them, then it shall be washed again, and shall be clean.",
      "M": "But the garment — whether warp, woof, or any leather article — that you wash and from which the mark departs shall be washed a second time and be clean.",
      "T": "A garment, warp, woof, or leather article from which the mark has fully departed after washing shall be washed again and declared clean."
    },
    "59": {
      "L": "This is the law of the plague of leprosy in a garment of woollen or linen, either in the warp, or woof, or any thing of skins, to pronounce it clean, or to pronounce it unclean.",
      "M": "This is the law for a mark of skin disease on a garment of wool or linen, in the warp or woof, or on any leather article — to pronounce it clean or to pronounce it unclean.",
      "T": "This is the comprehensive ruling for diagnosing a defiling mark in wool or linen garments, warp or woof threads, or any leather goods — determining what is clean and what is impure."
    }
  },
  "14": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "This shall be the law of the leper in the day of his cleansing: He shall be brought unto the priest:",
      "M": "This is the law for the person with a skin disease on the day of his cleansing: he shall be brought to the priest.",
      "T": "This is the procedure for the day when someone is declared clean from a skin disease — the person is brought to the priest."
    },
    "3": {
      "L": "And the priest shall go forth out of the camp; and the priest shall look, and, behold, if the plague of leprosy be healed in the leper;",
      "M": "The priest shall go outside the camp and examine. If the skin disease has been healed in the person with the disease,",
      "T": "The priest goes outside the camp to examine him. If the skin disease has indeed healed —"
    },
    "4": {
      "L": "Then shall the priest command to take for him that is to be cleansed two birds alive and clean, and cedar wood, and scarlet, and hyssop:",
      "M": "the priest shall command that two living clean birds, cedar wood, crimson yarn, and hyssop be brought for the one to be cleansed.",
      "T": "the priest orders four things for the cleansing rite: two living clean birds, cedar wood, crimson yarn, and hyssop."
    },
    "5": {
      "L": "And the priest shall command that one of the birds be killed over running water in an earthen vessel:",
      "M": "The priest shall command that one of the birds be slaughtered over fresh running water in a clay pot.",
      "T": "One bird is slaughtered over fresh water in a clay pot — the blood mingles with living water."
    },
    "6": {
      "L": "As for the living bird, he shall take it, and the cedar wood, and the scarlet, and the hyssop, and shall dip them and the living bird in the blood of the bird that was killed over the running water:",
      "M": "He shall take the living bird with the cedar wood, the crimson yarn, and the hyssop and dip them together with the living bird in the blood of the slaughtered bird over the fresh water.",
      "T": "The living bird, cedar wood, crimson yarn, and hyssop are all dipped together in the blood-and-water mixture — binding life to the symbols of purification."
    },
    "7": {
      "L": "And he shall sprinkle upon him that is to be cleansed from the leprosy seven times, and shall pronounce him clean, and shall let the living bird loose into the open field.",
      "M": "He shall sprinkle it seven times on the one to be cleansed from the skin disease and declare him clean, then release the living bird into the open field.",
      "T": "The priest sprinkles the person seven times, pronounces him clean, then releases the living bird into the open field — the bird carries the disease away."
    },
    "8": {
      "L": "And he that is to be cleansed shall wash his clothes, and shave off all his hair, and wash himself in water, that he may be clean: and after that he shall come into the camp, but shall tarry abroad out of his tent seven days.",
      "M": "The one being cleansed shall wash his clothes, shave off all his hair, and bathe in water; then he shall be clean. After that he may enter the camp, but he must live outside his tent for seven days.",
      "T": "The cleansed person washes clothes, shaves all hair, and bathes — then he is clean and may enter the camp. But he waits outside his own tent for seven more days, easing back into community life."
    },
    "9": {
      "L": "But it shall be on the seventh day, that he shall shave all his hair off his head and his beard and his eyebrows, even all his hair he shall shave off: and he shall wash his clothes, also he shall wash his flesh in water, and he shall be clean.",
      "M": "On the seventh day he shall shave off all his hair — his head, beard, and eyebrows — every hair. He shall wash his clothes and bathe his body in water, and he shall be clean.",
      "T": "On the seventh day he shaves completely — head, beard, eyebrows, every hair — washes his clothes, bathes. Full cleansing before reintegration."
    },
    "10": {
      "L": "And on the eighth day he shall take two he lambs without blemish, and one ewe lamb of the first year without blemish, and three tenth deals of fine flour for a grain offering, mingled with oil, and one log of oil.",
      "M": "On the eighth day he shall take two male lambs without blemish, one yearling ewe lamb without blemish, three-tenths of an ephah of fine flour mixed with oil as a grain offering, and one log of oil.",
      "T": "On the eighth day the full offering sequence begins: two flawless male lambs, one flawless yearling ewe, three-tenths of an ephah of fine flour mixed with oil, and one log of oil."
    },
    "11": {
      "L": "And the priest that maketh him clean shall present the man that is to be made clean, and those things, before the LORD, at the door of the tabernacle of the congregation:",
      "M": "The priest who is cleansing him shall present the man being cleansed, along with these offerings, before the LORD at the entrance of the tent of meeting.",
      "T": "The priest presents the man being cleansed with all his offerings before the LORD at the tent of meeting entrance."
    },
    "12": {
      "L": "And the priest shall take one he lamb, and offer him for a trespass offering, and the log of oil, and wave them for a wave offering before the LORD:",
      "M": "The priest shall take one male lamb and offer it as a guilt offering, along with the log of oil, waving them as a wave offering before the LORD.",
      "T": "The priest takes one lamb as a reparation offering and the log of oil and waves them before the LORD — the guilt offering comes first."
    },
    "13": {
      "L": "And he shall slay the lamb in the place where he shall kill the sin offering and the burnt offering, in the holy place: for as the sin offering is the priest's, so is the trespass offering: it is most holy:",
      "M": "He shall slaughter the lamb in the place where the sin offering and burnt offering are slaughtered — in the holy place. The guilt offering, like the sin offering, belongs to the priest: it is most holy.",
      "T": "The guilt-offering lamb is slaughtered in the sacred precinct, as for the sin offering and burnt offering. Like the sin offering, it belongs to the officiating priest — it is most holy."
    },
    "14": {
      "L": "And the priest shall take some of the blood of the trespass offering, and the priest shall put it upon the tip of the right ear of him that is to be cleansed, and upon the thumb of his right hand, and upon the great toe of his right foot:",
      "M": "The priest shall take some of the blood of the guilt offering and put it on the lobe of the right ear of the person being cleansed, on the thumb of his right hand, and on the big toe of his right foot.",
      "T": "The priest takes blood from the reparation offering and touches it to three points: the right earlobe, the right thumb, the right big toe — ear to hear, hand to act, foot to walk in clean ways."
    },
    "15": {
      "L": "And the priest shall take some of the log of oil, and pour it into the palm of his own left hand:",
      "M": "The priest shall take some of the log of oil and pour it into the palm of his own left hand.",
      "T": "The priest pours oil from the log into his left palm."
    },
    "16": {
      "L": "And the priest shall dip his right finger in the oil that is in his left hand, and shall sprinkle of the oil with his finger seven times before the LORD:",
      "M": "The priest shall dip his right finger in the oil in his left palm and sprinkle some of the oil seven times before the LORD.",
      "T": "With his right finger he sprinkles oil seven times before the LORD."
    },
    "17": {
      "L": "And of the rest of the oil that is in his hand shall the priest put upon the tip of the right ear of him that is to be cleansed, and upon the thumb of his right hand, and upon the great toe of his right foot, upon the blood of the trespass offering:",
      "M": "The rest of the oil in his palm the priest shall put on the lobe of the right ear of the person being cleansed, on the thumb of his right hand, and on the big toe of his right foot — on top of the blood of the guilt offering.",
      "T": "The remaining oil goes to the same three spots where the blood was placed — right earlobe, right thumb, right big toe — oil layered over blood."
    },
    "18": {
      "L": "And the remnant of the oil that is in the priest's hand he shall pour upon the head of him that is to be cleansed: and the priest shall make an atonement for him before the LORD.",
      "M": "The rest of the oil in the priest's palm he shall pour on the head of the person being cleansed. The priest shall make atonement for him before the LORD.",
      "T": "The priest pours what remains on the head of the one being cleansed, then makes atonement for him before the LORD."
    },
    "19": {
      "L": "And the priest shall offer the sin offering, and make an atonement for him that is to be cleansed from his uncleanness; and afterward he shall kill the burnt offering:",
      "M": "The priest shall offer the sin offering and make atonement for the one being cleansed from his uncleanness, and afterward shall slaughter the burnt offering.",
      "T": "The sin offering is presented next — atonement for the uncleanness itself — then the burnt offering follows."
    },
    "20": {
      "L": "And the priest shall offer the burnt offering and the grain offering upon the altar: and the priest shall make an atonement for him, and he shall be clean.",
      "M": "The priest shall offer the burnt offering and the grain offering on the altar. The priest shall make atonement for him, and he shall be clean.",
      "T": "Burnt offering and grain offering complete the sequence on the altar. The priest makes atonement and the person is clean — fully restored to the community."
    },
    "21": {
      "L": "And if he be poor, and cannot get so much; then he shall take one lamb for a trespass offering to be waved, to make an atonement for him, and one tenth deal of fine flour mingled with oil for a grain offering, and a log of oil;",
      "M": "But if he is poor and cannot afford these, he shall take one lamb as a guilt offering to be waved to make atonement for him, one-tenth of an ephah of fine flour mixed with oil as a grain offering, and a log of oil,",
      "T": "For someone who cannot afford the full offering: one lamb as a reparation offering, one-tenth ephah of fine flour mixed with oil, and a log of oil —"
    },
    "22": {
      "L": "And two turtledoves, or two young pigeons, such as he is able to get; and the one shall be a sin offering, and the other a burnt offering.",
      "M": "and two turtledoves or two young pigeons — whatever he can afford — one as a sin offering and the other as a burnt offering.",
      "T": "plus two turtledoves or two young pigeons — one sin offering, one burnt offering. What he can afford is enough."
    },
    "23": {
      "L": "And he shall bring them on the eighth day for his cleansing unto the priest, unto the door of the tabernacle of the congregation, before the LORD.",
      "M": "On the eighth day he shall bring them to the priest for his cleansing, to the entrance of the tent of meeting before the LORD.",
      "T": "On the eighth day he brings these to the priest at the tent of meeting entrance before the LORD."
    },
    "24": {
      "L": "And the priest shall take the lamb of the trespass offering, and the log of oil, and the priest shall wave them for a wave offering before the LORD:",
      "M": "The priest shall take the guilt-offering lamb and the log of oil and wave them as a wave offering before the LORD.",
      "T": "The priest waves the guilt-offering lamb and the oil before the LORD."
    },
    "25": {
      "L": "And he shall kill the lamb of the trespass offering, and the priest shall take some of the blood of the trespass offering, and put it upon the tip of the right ear of him that is to be cleansed, and upon the thumb of his right hand, and upon the great toe of his right foot:",
      "M": "He shall slaughter the guilt-offering lamb, and the priest shall take some of its blood and put it on the lobe of the right ear of the person being cleansed, on the thumb of his right hand, and on the big toe of his right foot.",
      "T": "The guilt-offering lamb is slaughtered. Blood touches the right earlobe, right thumb, right big toe of the person being cleansed."
    },
    "26": {
      "L": "And the priest shall pour of the oil into the palm of his own left hand:",
      "M": "The priest shall pour some of the oil into the palm of his own left hand,",
      "T": "The priest pours oil into his left palm,"
    },
    "27": {
      "L": "And the priest shall sprinkle with his right finger some of the oil that is in his left hand seven times before the LORD:",
      "M": "and with his right finger shall sprinkle some of the oil in his left palm seven times before the LORD.",
      "T": "and sprinkles oil seven times before the LORD with his right finger."
    },
    "28": {
      "L": "And the priest shall put of the oil that is in his hand upon the tip of the right ear of him that is to be cleansed, and upon the thumb of his right hand, and upon the great toe of his right foot, upon the place of the blood of the trespass offering:",
      "M": "The priest shall put some of the oil in his hand on the lobe of the right ear of the one being cleansed, on the thumb of his right hand, and on the big toe of his right foot — on the place of the blood of the guilt offering.",
      "T": "Oil is placed on the same three points where the blood was — right earlobe, right thumb, right big toe."
    },
    "29": {
      "L": "And the rest of the oil that is in the priest's hand he shall put upon the head of him that is to be cleansed, to make an atonement for him before the LORD.",
      "M": "The rest of the oil in the priest's hand he shall put on the head of the person being cleansed, to make atonement for him before the LORD.",
      "T": "The remaining oil is poured on the head of the one being cleansed — atonement made before the LORD."
    },
    "30": {
      "L": "And he shall offer the one of the turtledoves, or of the young pigeons, such as he can get;",
      "M": "He shall then offer one of the turtledoves or young pigeons — whichever he can afford —",
      "T": "Then comes whichever bird offering the person can afford —"
    },
    "31": {
      "L": "Even such as he is able to get, the one for a sin offering, and the other for a burnt offering, with the grain offering: and the priest shall make an atonement for him that is to be cleansed before the LORD.",
      "M": "one as a sin offering and the other as a burnt offering, together with the grain offering. The priest shall make atonement before the LORD for the one being cleansed.",
      "T": "one for a sin offering, one for a burnt offering, with the grain offering. The priest makes atonement before the LORD — poverty is no barrier to cleansing."
    },
    "32": {
      "L": "This is the law of him in whom is the plague of leprosy, whose hand is not able to get that which pertaineth to his cleansing.",
      "M": "This is the law for the person who has a skin disease but cannot afford the offerings for his cleansing.",
      "T": "This is the provision for anyone with a skin disease who lacks the means for the standard offering."
    },
    "33": {
      "L": "And the LORD spake unto Moses and unto Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD spoke to Moses and Aaron:"
    },
    "34": {
      "L": "When ye be come into the land of Canaan, which I give to you for a possession, and I put the plague of leprosy in a house of the land of your possession;",
      "M": "When you enter the land of Canaan, which I am giving you as a possession, and I put a mark of skin disease on a house in the land you possess,",
      "T": "When you enter the land I am giving you, and a defiling growth appears on a house you occupy —"
    },
    "35": {
      "L": "And he whose house it is shall come and tell the priest, saying, It seemeth to me there is as it were a plague in the house:",
      "M": "the owner of the house shall come and tell the priest: 'Something that looks like a disease has appeared in my house.'",
      "T": "the owner reports to the priest: 'Something like a diseased mark has appeared in my house.'"
    },
    "36": {
      "L": "Then the priest shall command that they empty the house, before the priest go in to examine the plague, that all that is in the house be not made unclean: and afterward the priest shall go in to examine the house:",
      "M": "The priest shall command that the house be emptied before he goes in to examine the mark, so that everything in it does not become unclean. After that the priest shall go in to examine the house.",
      "T": "The priest orders the house emptied before he enters to examine it — this prevents everything inside from becoming impure by association. Then the priest inspects."
    },
    "37": {
      "L": "And he shall look on the plague, and, behold, if the plague be in the walls of the house with hollow strakes, greenish or reddish, which in sight are lower than the wall;",
      "M": "He shall examine the mark. If the marks in the walls of the house are greenish or reddish streaks that appear to be set below the surface of the wall,",
      "T": "If the marks on the walls are greenish or reddish streaks that appear to go deeper than the wall surface —"
    },
    "38": {
      "L": "Then the priest shall go out of the house to the door of the house, and shut up the house seven days:",
      "M": "the priest shall go out of the house to the doorway and quarantine the house for seven days.",
      "T": "the priest steps out to the doorway and places the house under seven-day quarantine."
    },
    "39": {
      "L": "And the priest shall come again the seventh day, and shall look: and, behold, if the plague be spread in the walls of the house;",
      "M": "The priest shall return on the seventh day and look. If the marks have spread on the walls of the house,",
      "T": "On the seventh day, if the marks have spread on the walls —"
    },
    "40": {
      "L": "Then the priest shall command that they take away the stones in which the plague is, and they shall cast them into an unclean place without the city:",
      "M": "the priest shall command that the stones in which the mark appears be torn out and thrown into an unclean place outside the city.",
      "T": "the priest orders the diseased stones removed and dumped outside the city in an impure place."
    },
    "41": {
      "L": "And he shall cause the house to be scraped within round about, and they shall pour out the dust that they scrape off without the city into an unclean place:",
      "M": "The house shall be scraped all around on the inside, and the plaster scraped off shall be dumped outside the city in an unclean place.",
      "T": "The entire interior is scraped down, and all the debris taken outside the city to an impure site."
    },
    "42": {
      "L": "And they shall take other stones, and put them in the place of those stones; and he shall take other mortar, and shall plaister the house.",
      "M": "Other stones shall be taken and put in place of the removed stones, and new plaster shall be used to re-plaster the house.",
      "T": "New stones replace the old; new plaster covers the walls."
    },
    "43": {
      "L": "And if the plague come again, and break out in the house, after that he hath taken away the stones, and after he hath scraped the house, and after it is plaistered;",
      "M": "If the disease comes back and breaks out in the house after the stones have been removed, the house has been scraped, and it has been re-plastered,",
      "T": "If the disease returns and reappears after all the work — stones removed, walls scraped, house replastered —"
    },
    "44": {
      "L": "Then the priest shall come and look, and, behold, if the plague be spread in the house, it is a fretting leprosy in the house: it is unclean.",
      "M": "the priest shall come and examine. If the mark has spread in the house, it is a malignant disease in the house: it is unclean.",
      "T": "the priest returns for examination. If the mark has spread despite all remediation, it is a destructive disease in the house — the house is impure."
    },
    "45": {
      "L": "And he shall break down the house, the stones of it, and the timber thereof, and all the mortar of the house; and he shall carry them forth out of the city into an unclean place.",
      "M": "He shall tear down the house — its stones, its timber, and all the plaster — and carry them outside the city to an unclean place.",
      "T": "The house is demolished completely — stones, timber, plaster — and all of it carried outside the city to an impure site."
    },
    "46": {
      "L": "Moreover he that goeth into the house all the while that it is shut up shall be unclean until the even.",
      "M": "Anyone who goes into the house during the time it is quarantined shall be unclean until evening.",
      "T": "Entering the quarantined house makes a person impure until evening."
    },
    "47": {
      "L": "And he that lieth in the house shall wash his clothes; and he that eateth in the house shall wash his clothes.",
      "M": "Whoever sleeps in the house must wash his clothes, and whoever eats in the house must wash his clothes.",
      "T": "Sleep in the quarantined house: wash your clothes. Eat in it: wash your clothes."
    },
    "48": {
      "L": "And if the priest shall come in, and look upon it, and, behold, the plague hath not spread in the house, after the house was plaistered: then the priest shall pronounce the house clean, because the plague is healed.",
      "M": "But if the priest comes and examines it and the mark has not spread in the house after it was re-plastered, the priest shall pronounce the house clean: the disease is healed.",
      "T": "But if the priest examines after replastering and the mark has not spread, the priest pronounces the house clean — the disease has been arrested."
    },
    "49": {
      "L": "And he shall take to cleanse the house two birds, and cedar wood, and scarlet, and hyssop:",
      "M": "To purify the house he shall take two birds, cedar wood, crimson yarn, and hyssop.",
      "T": "The same four elements used for personal cleansing serve the house: two birds, cedar wood, crimson yarn, hyssop."
    },
    "50": {
      "L": "And he shall kill the one of the birds over running water in an earthen vessel:",
      "M": "He shall slaughter one of the birds over fresh water in a clay pot.",
      "T": "One bird is slaughtered over fresh water in a clay vessel."
    },
    "51": {
      "L": "And he shall take the cedar wood, and the hyssop, and the scarlet, and the living bird, and dip them in the blood of the slain bird, and in the running water, and sprinkle the house seven times:",
      "M": "He shall take the cedar wood, hyssop, crimson yarn, and the living bird and dip them in the blood of the slaughtered bird and the fresh water and sprinkle the house seven times.",
      "T": "Cedar wood, hyssop, crimson yarn, and living bird are all dipped in blood-and-water and used to sprinkle the house seven times."
    },
    "52": {
      "L": "And he shall cleanse the house with the blood of the bird, and with the running water, and with the living bird, and with the cedar wood, and with the hyssop, and with the scarlet:",
      "M": "He shall purify the house with the blood of the bird and the fresh water and the living bird and the cedar wood and the hyssop and the crimson yarn.",
      "T": "The house is purified by the blood, the living water, the living bird, the cedar, the hyssop, the crimson — a full-spectrum purification rite."
    },
    "53": {
      "L": "But he shall let go the living bird out of the city into the open fields, and make an atonement for the house: and it shall be clean.",
      "M": "Then he shall release the living bird outside the city into the open field. He has made atonement for the house and it is clean.",
      "T": "The living bird is released outside the city into open country — carrying the defilement away. Atonement is made for the house; it is clean."
    },
    "54": {
      "L": "This is the law for all manner of plague of leprosy, and scall,",
      "M": "This is the law for every kind of skin disease — for an itch,",
      "T": "This is the comprehensive ruling for every form of defiling skin disease — for an itch,"
    },
    "55": {
      "L": "And for the leprosy of a garment, and of a house,",
      "M": "for disease in a garment and in a house,",
      "T": "for disease in clothing and in buildings,"
    },
    "56": {
      "L": "And for a rising, and for a scab, and for a bright spot:",
      "M": "for a swelling, a scab, and a bright spot —",
      "T": "for swelling, eruption, and gleaming patch —"
    },
    "57": {
      "L": "To teach when it is unclean, and when it is clean: this is the law of leprosy.",
      "M": "to teach when something is unclean and when it is clean. This is the law of skin disease.",
      "T": "establishing which conditions are impure and which are clean. This is the full ruling on defiling skin disease."
    }
  },
  "15": {
    "1": {
      "L": "And the LORD spake unto Moses and to Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD spoke to Moses and Aaron:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and say unto them, When any man hath a running issue out of his flesh, because of his issue he is unclean.",
      "M": "Tell the people of Israel: When any man has a bodily discharge, his discharge makes him unclean.",
      "T": "Tell Israel: when a man has an abnormal bodily discharge, the discharge renders him impure."
    },
    "3": {
      "L": "And this shall be his uncleanness in his issue: whether his flesh run with his issue, or his flesh be stopped from his issue, it is his uncleanness.",
      "M": "This is his uncleanness in his discharge: whether his body lets the discharge flow or blocks it, he is unclean.",
      "T": "Whether the discharge flows freely or is intermittent, he is impure — the condition itself creates the impurity."
    },
    "4": {
      "L": "Every bed, whereon he lieth that hath the issue, is unclean: and every thing, whereon he sitteth, shall be unclean.",
      "M": "Every bed that the man with the discharge lies on will be unclean, and every seat he sits on will be unclean.",
      "T": "Every surface he lies on becomes impure; every surface he sits on becomes impure."
    },
    "5": {
      "L": "And whosoever toucheth his bed shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Anyone who touches his bed shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Touch his bed: wash clothes, bathe, impure until evening."
    },
    "6": {
      "L": "And he that sitteth on any thing whereon he sat that hath the issue shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Whoever sits on anything that the man with the discharge sat on shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Sit on what he sat on: wash clothes, bathe, impure until evening."
    },
    "7": {
      "L": "And he that toucheth the flesh of him that hath the issue shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Whoever touches the body of the man with the discharge shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Touch his body: wash clothes, bathe, impure until evening."
    },
    "8": {
      "L": "And if he that hath the issue spit upon him that is clean; then he shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "If the man with the discharge spits on someone who is clean, that person shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Even his saliva transfers impurity — anyone he spits on washes clothes, bathes, remains impure until evening."
    },
    "9": {
      "L": "And what saddle soever he rideth upon that hath the issue shall be unclean.",
      "M": "Every saddle that the man with the discharge rides on will be unclean.",
      "T": "Any saddle he rides on is impure."
    },
    "10": {
      "L": "And whosoever toucheth any thing that was under him shall be unclean until the even: and he that beareth any of those things shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Anyone who touches anything that was beneath him will be unclean until evening. Whoever carries those things shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Touch anything that was under him: impure until evening. Carry it: wash clothes, bathe, impure until evening."
    },
    "11": {
      "L": "And whomsoever he toucheth that hath the issue, and hath not rinsed his hands in water, he shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Anyone the man with the discharge touches without having first rinsed his hands in water shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "If he touches someone without rinsing his hands first, that person washes clothes, bathes, remains impure until evening."
    },
    "12": {
      "L": "And the vessel of earth, that he toucheth which hath the issue, shall be broken: and every vessel of wood shall be rinsed in water.",
      "M": "Any clay vessel the man with the discharge touches shall be broken, and any wooden utensil shall be rinsed with water.",
      "T": "Clay vessels he touches must be smashed; wooden ones rinsed with water."
    },
    "13": {
      "L": "And when he that hath an issue is cleansed of his issue; then he shall number to himself seven days for his cleansing, and wash his clothes, and bathe his flesh in running water, and shall be clean.",
      "M": "When the man with the discharge is cleansed from his discharge, he shall count seven days for his cleansing, wash his clothes, and bathe in fresh running water, and he will be clean.",
      "T": "When the discharge stops, he counts seven days, washes his clothes, bathes in running water — then he is clean."
    },
    "14": {
      "L": "And on the eighth day he shall take to him two turtledoves, or two young pigeons, and come before the LORD unto the door of the tabernacle of the congregation, and give them unto the priest:",
      "M": "On the eighth day he shall take two turtledoves or two young pigeons, come before the LORD to the entrance of the tent of meeting, and give them to the priest.",
      "T": "On the eighth day he brings two turtledoves or two young pigeons to the priest at the tent of meeting entrance."
    },
    "15": {
      "L": "And the priest shall offer them, the one for a sin offering, and the other for a burnt offering; and the priest shall make an atonement for him before the LORD for his issue.",
      "M": "The priest shall offer them — one as a sin offering and the other as a burnt offering. The priest shall make atonement for him before the LORD for his discharge.",
      "T": "The priest offers one as a sin offering and one as a burnt offering, making atonement before the LORD for the discharge — restoration complete."
    },
    "16": {
      "L": "And if any man's seed of copulation go out from him, then he shall wash all his flesh in water, and be unclean until the even.",
      "M": "If a man has a seminal emission, he shall bathe his whole body in water and be unclean until evening.",
      "T": "A man who has a seminal emission bathes his entire body and is impure until evening."
    },
    "17": {
      "L": "And every garment, and every skin, whereon is the seed of copulation, shall be washed with water, and be unclean until the even.",
      "M": "Every garment or leather on which there is a seminal emission shall be washed with water and be unclean until evening.",
      "T": "Any garment or leather that has the emission on it is washed — impure until evening."
    },
    "18": {
      "L": "The woman also with whom man shall lie with seed of copulation, they shall both bathe themselves in water, and be unclean until the even.",
      "M": "If a man lies with a woman and there is a seminal emission, both shall bathe in water and be unclean until evening.",
      "T": "Sexual intercourse requires both partners to bathe afterward — both are impure until evening."
    },
    "19": {
      "L": "And if a woman have an issue, and her issue in her flesh be blood, she shall be put apart seven days: and whosoever toucheth her shall be unclean until the even.",
      "M": "When a woman has a discharge and her discharge in her body is blood, she shall be in her menstrual separation for seven days. Whoever touches her will be unclean until evening.",
      "T": "When a woman's discharge is blood — her monthly cycle — she is in menstrual separation for seven days. Anyone who touches her is impure until evening."
    },
    "20": {
      "L": "And every thing that she lieth upon in her separation shall be unclean: every thing also that she sitteth upon shall be unclean.",
      "M": "Everything she lies on during her separation will be unclean, and everything she sits on will be unclean.",
      "T": "Everything she lies on and everything she sits on during her separation is impure."
    },
    "21": {
      "L": "And whosoever toucheth her bed shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Anyone who touches her bed shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Touch her bed: wash clothes, bathe, impure until evening."
    },
    "22": {
      "L": "And whosoever toucheth any thing that she sat upon shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Whoever touches anything she sat on shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Touch anything she sat on: wash clothes, bathe, impure until evening."
    },
    "23": {
      "L": "And if it be on her bed, or on any thing whereon she sitteth, when he toucheth it, he shall be unclean until the even.",
      "M": "Whether on the bed or on whatever she sits on — when he touches it, he will be unclean until evening.",
      "T": "Bed or seat — touching either makes the person impure until evening."
    },
    "24": {
      "L": "And if any man lie with her at all, and her flowers be upon him, he shall be unclean seven days; and all the bed whereon he lieth shall be unclean.",
      "M": "If any man lies with her and her menstrual flow comes upon him, he shall be unclean for seven days, and every bed he lies on shall be unclean.",
      "T": "If a man has sexual relations with her and her menstrual impurity transfers to him, he becomes impure for seven full days — and every bed he uses during that time is impure."
    },
    "25": {
      "L": "And if a woman have an issue of her blood many days out of the time of her separation, or if it run beyond the time of her separation; all the days of the issue of her unclean discharge shall be as the days of her separation: she shall be unclean.",
      "M": "If a woman has a discharge of blood for many days when it is not the time of her menstrual separation, or if the discharge runs beyond the usual time of her separation, she shall be unclean for all the days of her unclean discharge, just as in the time of her menstrual separation.",
      "T": "If a woman's blood discharge occurs outside her regular cycle or lasts beyond it, she is impure for the duration of that discharge — the same rules apply as for her monthly separation."
    },
    "26": {
      "L": "Every bed whereon she lieth all the days of her issue shall be unto her as the bed of her separation: and whatsoever she sitteth upon shall be unclean, as the uncleanness of her separation.",
      "M": "Every bed she lies on during her discharge days shall be like her menstrual bed — unclean. Everything she sits on will be unclean, as in the uncleanness of her menstrual separation.",
      "T": "Every bed and every seat she uses during the extended discharge carries the same impurity as during her regular monthly separation."
    },
    "27": {
      "L": "And whosoever toucheth those things shall be unclean, and shall wash his clothes, and bathe himself in water, and be unclean until the even.",
      "M": "Whoever touches them will be unclean; he shall wash his clothes and bathe in water, and be unclean until evening.",
      "T": "Anyone who touches these surfaces washes clothes, bathes, remains impure until evening."
    },
    "28": {
      "L": "But if she be cleansed of her issue, then she shall number to herself seven days, and after that she shall be clean.",
      "M": "But when she is cleansed from her discharge, she shall count seven days and then she will be clean.",
      "T": "When the discharge stops, she counts seven days — then she is clean."
    },
    "29": {
      "L": "And on the eighth day she shall take unto her two turtles, or two young pigeons, and bring them unto the priest, to the door of the tabernacle of the congregation.",
      "M": "On the eighth day she shall take two turtledoves or two young pigeons and bring them to the priest at the entrance of the tent of meeting.",
      "T": "On the eighth day she brings two turtledoves or two young pigeons to the priest at the tent of meeting entrance."
    },
    "30": {
      "L": "And the priest shall offer the one for a sin offering, and the other for a burnt offering; and the priest shall make an atonement for her before the LORD for the issue of her uncleanness.",
      "M": "The priest shall offer one as a sin offering and the other as a burnt offering. The priest shall make atonement for her before the LORD for her unclean discharge.",
      "T": "Sin offering and burnt offering — the priest makes atonement before the LORD for her. The extended discharge required priestly restoration, not just the passage of time."
    },
    "31": {
      "L": "Thus shall ye separate the children of Israel from their uncleanness; that they die not in their uncleanness, when they defile my tabernacle that is among them.",
      "M": "You shall thus keep the people of Israel separate from their uncleanness, lest they die in their uncleanness by defiling my tabernacle that is in their midst.",
      "T": "This is why Israel must be kept separate from impurity: the tabernacle dwells in their midst. Impurity that reaches the sanctuary brings death — the entire purity system exists to protect the dwelling of the holy God among an unholy people."
    },
    "32": {
      "L": "This is the law of him that hath an issue, and of him whose seed goeth from him, and is defiled therewith;",
      "M": "This is the law for the man with a discharge, and for the man who has a seminal emission and becomes unclean thereby,",
      "T": "This is the ruling for the man with an abnormal discharge and for the man with a seminal emission,"
    },
    "33": {
      "L": "And of her that is sick of her flowers, and of him that hath an issue, of the man, and of the woman, and of him that lieth with her that is unclean.",
      "M": "and for the woman in her menstrual separation, and for the man or woman with a discharge, and for the man who lies with a woman who is unclean.",
      "T": "for the woman in her menstrual separation, for anyone with an extended discharge, and for the man who has relations with a woman in her impurity."
    }
  },
  "16": {
    "1": {
      "L": "And the LORD spake unto Moses after the death of the two sons of Aaron, when they offered before the LORD, and died;",
      "M": "The LORD spoke to Moses after the death of Aaron's two sons, who died when they came before the LORD.",
      "T": "The LORD spoke to Moses in the aftermath of Nadab and Abihu's death — they who died when they drew near the LORD without authorization."
    },
    "2": {
      "L": "And the LORD said unto Moses, Speak unto Aaron thy brother, that he come not at all times into the holy place within the vail before the mercy seat, which is upon the ark; that he die not: for I will appear in the cloud upon the mercy seat.",
      "M": "The LORD said to Moses: Tell your brother Aaron that he must not come at any time he pleases into the holy place inside the veil, before the atonement cover on the ark, or he will die. For I appear in the cloud over the atonement cover.",
      "T": "Tell Aaron: access to the Most Holy Place is not open to him at will. To enter whenever he pleases is to die — for I appear in the cloud over the atonement cover. The divine presence is not to be approached casually."
    },
    "3": {
      "L": "Thus shall Aaron come into the holy place: with a young bullock for a sin offering, and a ram for a burnt offering.",
      "M": "Aaron may enter the holy place only in this way: with a bull calf for a sin offering and a ram for a burnt offering.",
      "T": "Aaron may enter only by this prescribed path: a bull calf as his personal sin offering and a ram for a burnt offering."
    },
    "4": {
      "L": "He shall put on the holy linen coat, and he shall have the linen breeches upon his flesh, and shall be girded with a linen girdle, and with the linen mitre shall he be covered: these are holy garments; therefore shall he wash his flesh in water, and so put them on.",
      "M": "He shall wear the holy linen tunic, put linen trousers on his body, tie a linen sash, and cover his head with a linen turban. These are holy garments. He shall bathe his body in water and put them on.",
      "T": "He enters in plain linen — not the ornate high-priestly garments. Linen tunic, linen trousers, linen sash, linen turban — these are the simple holy garments worn into God's direct presence. He bathes first, then dresses."
    },
    "5": {
      "L": "And he shall take of the congregation of the children of Israel two kids of the goats for a sin offering, and one ram for a burnt offering.",
      "M": "From the congregation of Israel he shall take two male goats for a sin offering and one ram for a burnt offering.",
      "T": "From the congregation he takes two male goats for the sin offering — the two-goat drama is Israel's offering — and one ram for a burnt offering."
    },
    "6": {
      "L": "And Aaron shall offer his bullock of the sin offering, which is for himself, and make an atonement for himself, and for his house.",
      "M": "Aaron shall present the bull of his sin offering and make atonement for himself and his household.",
      "T": "Aaron begins with atonement for himself and his household — the priest must be clean before he can atone for others."
    },
    "7": {
      "L": "And he shall take the two goats, and present them before the LORD at the door of the tabernacle of the congregation.",
      "M": "He shall take the two goats and present them before the LORD at the entrance of the tent of meeting.",
      "T": "Both goats are brought and presented before the LORD at the tent of meeting entrance."
    },
    "8": {
      "L": "And Aaron shall cast lots upon the two goats; one lot for the LORD, and the other lot for the scapegoat.",
      "M": "Aaron shall cast lots over the two goats — one lot for the LORD and one lot for Azazel.",
      "T": "Aaron casts lots to divide the two goats: one lot falls for the LORD, one for Azazel — the wilderness goat of removal."
    },
    "9": {
      "L": "And Aaron shall bring the goat upon which the LORD'S lot fell, and offer him for a sin offering.",
      "M": "Aaron shall present the goat on which the LORD's lot fell and offer it as a sin offering.",
      "T": "The goat that the lot assigns to the LORD is offered as a sin offering."
    },
    "10": {
      "L": "But the goat, on which the lot fell for the scapegoat, shall be presented alive before the LORD, to make an atonement with him, and to let him go for a scapegoat into the wilderness.",
      "M": "The goat on which the lot for Azazel fell shall be presented alive before the LORD to make atonement over it, then sent away to Azazel into the wilderness.",
      "T": "The Azazel goat stays alive — it is presented before the LORD for the atonement-confession rite, then sent away into the wilderness as the goat of removal."
    },
    "11": {
      "L": "And Aaron shall bring the bullock of the sin offering, which is for himself, and shall make an atonement for himself, and for his house, and shall kill the bullock of the sin offering which is for himself:",
      "M": "Aaron shall bring the bull of his sin offering and make atonement for himself and his household, and he shall slaughter the bull of his sin offering.",
      "T": "Aaron slaughters his bull first — personal atonement before he can mediate atonement for others."
    },
    "12": {
      "L": "And he shall take a censer full of burning coals of fire from off the altar before the LORD, and his hands full of sweet incense beaten small, and bring it within the vail:",
      "M": "He shall take a censer full of burning coals from the altar before the LORD, and two handfuls of finely ground fragrant incense, and bring them inside the veil.",
      "T": "He fills a censer with live coals from the altar before the LORD, takes two handfuls of ground fragrant incense, and carries them inside the veil — into the Most Holy Place."
    },
    "13": {
      "L": "And he shall put the incense upon the fire before the LORD, that the cloud of the incense may cover the mercy seat that is upon the testimony, that he die not:",
      "M": "He shall put the incense on the fire before the LORD so that the cloud of incense covers the atonement cover on the testimony, that he may not die.",
      "T": "He puts the incense on the coals before the LORD — the cloud of incense envelops the atonement cover. The incense cloud screens Aaron from the direct sight of God — without it, he would die."
    },
    "14": {
      "L": "And he shall take of the blood of the bullock, and sprinkle it with his finger upon the mercy seat eastward; and before the mercy seat shall he sprinkle of the blood with his finger seven times.",
      "M": "He shall take some of the bull's blood and sprinkle it with his finger on the front of the atonement cover on the east side. Before the atonement cover he shall sprinkle some of the blood seven times with his finger.",
      "T": "He takes some of the bull's blood and sprinkles it on the east face of the atonement cover with his finger, then sprinkles seven times in front of the cover — blood meeting the place where God meets humanity."
    },
    "15": {
      "L": "Then shall he kill the goat of the sin offering, that is for the people, and bring his blood within the vail, and do with that blood as he did with the blood of the bullock, and sprinkle it upon the mercy seat, and before the mercy seat:",
      "M": "Then he shall slaughter the goat of the sin offering for the people and bring its blood inside the veil. He shall do with that blood as he did with the bull's blood — sprinkle it on and before the atonement cover.",
      "T": "He slaughters the sin-offering goat for the people and brings its blood inside the veil. The same act repeated: blood on and before the atonement cover — this time for the whole congregation."
    },
    "16": {
      "L": "And he shall make an atonement for the holy place, because of the uncleanness of the children of Israel, and because of their transgressions in all their sins: and so shall he do for the tabernacle of the congregation, that remaineth among them in the midst of their uncleanness.",
      "M": "Thus he shall make atonement for the holy place because of the uncleanness of the Israelites and because of their transgressions, all their sins. He shall do the same for the tent of meeting, which dwells with them in the midst of their impurity.",
      "T": "By this rite he atones for the holy place itself — Israel's accumulated impurity and transgressions contaminate even the sanctuary. The same atonement covers the tent of meeting, which stands in the midst of an impure people."
    },
    "17": {
      "L": "And there shall be no man in the tabernacle of the congregation when he goeth in to make an atonement in the holy place, until he come out, and have made an atonement for himself, and for his household, and for all the congregation of Israel.",
      "M": "No one shall be in the tent of meeting from the time he enters to make atonement in the holy place until he comes out, having made atonement for himself, his household, and all the congregation of Israel.",
      "T": "No one else enters the tent of meeting from when Aaron goes in until he comes out. The moment demands absolute solitude — Aaron stands alone between the holy God and the whole congregation of Israel."
    },
    "18": {
      "L": "And he shall go out unto the altar that is before the LORD, and make an atonement for it; and shall take of the blood of the bullock, and of the blood of the goat, and put it upon the horns of the altar round about.",
      "M": "He shall come out to the altar that is before the LORD and make atonement for it. He shall take some of the blood of the bull and some of the blood of the goat and put it on all the horns of the altar.",
      "T": "Coming out, he moves to the altar before the LORD and atones for that too. Mixed blood — from the bull and the goat — is applied to every horn of the altar."
    },
    "19": {
      "L": "And he shall sprinkle of the blood upon it with his finger seven times, and cleanse it, and hallow it from the uncleanness of the children of Israel.",
      "M": "He shall sprinkle some of the blood on it with his finger seven times, cleansing it and consecrating it from the uncleanness of Israel.",
      "T": "Seven sprinklings of blood cleanse the altar from the accumulated impurity of Israel — consecrating it fresh for a new year of service."
    },
    "20": {
      "L": "And when he hath made an end of reconciling the holy place, and the tabernacle of the congregation, and the altar, he shall bring the live goat:",
      "M": "When he has finished atoning for the holy place, the tent of meeting, and the altar, he shall present the live goat.",
      "T": "With the sanctuary, the tent, and the altar all atoned for, the Azazel goat is brought forward — the second movement of Yom Kippur."
    },
    "21": {
      "L": "And Aaron shall lay both his hands upon the head of the live goat, and confess over him all the iniquities of the children of Israel, and all their transgressions in all their sins, putting them upon the head of the goat, and shall send him away by the hand of a fit man into the wilderness:",
      "M": "Aaron shall lay both his hands on the head of the live goat and confess over it all the iniquities of the Israelites and all their transgressions — all their sins. He shall put them on the head of the goat and send it away by the hand of a designated man into the wilderness.",
      "T": "Aaron places both hands on the head of the live goat and confesses over it — naming all Israel's iniquities, transgressions, and sins. The laying on of hands transfers the full weight of the nation's guilt onto the goat, which is then led away into the wilderness by a designated man."
    },
    "22": {
      "L": "And the goat shall bear upon him all their iniquities unto a land not inhabited: and he shall let go the goat in the wilderness.",
      "M": "The goat shall carry all their iniquities to an uninhabited land, and he shall release the goat in the wilderness.",
      "T": "The goat carries Israel's sins to a desolate, uninhabited place — a land of no return. There the guilt is released, far from the community and far from God's house."
    },
    "23": {
      "L": "And Aaron shall come into the tabernacle of the congregation, and shall put off the linen garments, which he put on when he went into the holy place, and shall leave them there:",
      "M": "Aaron shall come into the tent of meeting and take off the linen garments he put on when he entered the holy place, and he shall leave them there.",
      "T": "Aaron returns to the tent of meeting and removes the plain linen garments worn into the Most Holy Place. They are left there — the garments that entered God's presence are not worn again."
    },
    "24": {
      "L": "And he shall wash his flesh with water in the holy place, and put on his garments, and come forth, and offer his burnt offering, and the burnt offering of the people, and make an atonement for himself, and for the people.",
      "M": "He shall bathe his body in water in the holy place, put on his regular garments, come out and offer his burnt offering and the burnt offering of the people, and make atonement for himself and for the people.",
      "T": "He bathes in the sacred precinct, dresses in his regular priestly garments, and comes out to offer the burnt offerings — his own and the people's — completing the atonement of the day."
    },
    "25": {
      "L": "And the fat of the sin offering shall he burn upon the altar.",
      "M": "The fat of the sin offering he shall burn on the altar.",
      "T": "The fat portions of the sin offerings are burned on the altar."
    },
    "26": {
      "L": "And he that let go the goat for the scapegoat shall wash his clothes, and bathe his flesh in water, and afterward come into the camp.",
      "M": "The man who led away the goat for Azazel shall wash his clothes and bathe his body in water, and after that he may come into the camp.",
      "T": "The man who led the goat away has carried proximity to the sin-laden animal — he washes clothes and bathes before returning to the camp."
    },
    "27": {
      "L": "And the bullock for the sin offering, and the goat for the sin offering, whose blood was brought in to make an atonement in the holy place, shall one carry forth without the camp; and they shall burn in the fire their skins, and their flesh, and their dung.",
      "M": "The bull for the sin offering and the goat for the sin offering, whose blood was brought inside to make atonement in the holy place, shall be carried outside the camp and burned up with fire — their skins, their flesh, and their dung.",
      "T": "The bull and goat whose blood was used inside the Most Holy Place are burned completely outside the camp — hides, flesh, offal — nothing kept. The sin bearer cannot be eaten."
    },
    "28": {
      "L": "And he that burneth them shall wash his clothes, and bathe his flesh in water, and afterward he shall come into the camp.",
      "M": "The man who burns them shall wash his clothes and bathe his body in water, and afterward he may come into the camp.",
      "T": "The man who burns them also cleanses himself — wash clothes, bathe — before returning to camp."
    },
    "29": {
      "L": "And this shall be a statute for ever unto you: that in the seventh month, on the tenth day of the month, ye shall afflict your souls, and do no work at all, whether it be one of your own country, or a stranger that sojourneth among you:",
      "M": "This shall be a statute forever for you: in the seventh month, on the tenth day of the month, you shall practice self-denial and shall do no work — whether the native-born or the alien dwelling among you.",
      "T": "This is a permanent statute: the tenth day of the seventh month is the Day of Atonement. Israelite and resident alien alike — fast and humble yourselves, do no work. The calendar makes Yom Kippur annual and universal within Israel's community."
    },
    "30": {
      "L": "For on that day shall the priest make an atonement for you, to cleanse you, that ye may be clean from all your sins before the LORD.",
      "M": "For on this day atonement shall be made for you to cleanse you. From all your sins before the LORD you shall be clean.",
      "T": "On this one day, once a year, atonement is made for the whole community — every sin, cleanly dealt with before the LORD. The clean slate is the gift of Yom Kippur."
    },
    "31": {
      "L": "It shall be a sabbath of rest unto you, and ye shall afflict your souls, by a statute for ever.",
      "M": "It is a solemn Sabbath of complete rest for you, and you shall practice self-denial — a statute forever.",
      "T": "It is a Sabbath of complete, solemn rest — fast and be still. This is the permanent law."
    },
    "32": {
      "L": "And the priest, whom he shall anoint, and whom he shall consecrate to minister in the priest's office in his father's stead, shall make the atonement, and shall put on the linen clothes, even the holy garments:",
      "M": "The priest who is anointed and ordained to serve as priest in his father's place shall make the atonement. He shall put on the linen garments — the holy garments.",
      "T": "When Aaron dies, his anointed and ordained successor will perform this rite — dressed in the same plain holy linen, entering the same way. The ritual does not depend on Aaron personally; it is built into the priestly office itself."
    },
    "33": {
      "L": "And he shall make an atonement for the holy sanctuary, and he shall make an atonement for the tabernacle of the congregation, and for the altar, and he shall make an atonement for the priests, and for all the people of the congregation.",
      "M": "He shall make atonement for the holy sanctuary, the tent of meeting, and the altar, and he shall make atonement for the priests and for all the people of the assembly.",
      "T": "The scope of atonement on this day covers everything: the inner sanctuary, the tent, the altar, the priests themselves, the entire congregation. Nothing and no one is excluded."
    },
    "34": {
      "L": "And this shall be an everlasting statute unto you, to make an atonement for the children of Israel for all their sins once a year. And he did as the LORD commanded Moses.",
      "M": "This shall be a permanent statute for you: atonement shall be made for Israel once a year from all their sins. And Aaron did as the LORD commanded Moses.",
      "T": "Once a year — always and only once — complete atonement is made for all Israel's sins. Aaron did as the LORD commanded Moses. The Day of Atonement is established."
    }
  },
  "17": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto Aaron, and unto his sons, and unto all the children of Israel, and say unto them; This is the thing which the LORD hath commanded, saying,",
      "M": "Speak to Aaron and his sons and to all the people of Israel and say to them: This is what the LORD has commanded:",
      "T": "Tell Aaron, his sons, and all Israel: this is what the LORD commands —"
    },
    "3": {
      "L": "What man soever there be of the house of Israel, that killeth an ox, or lamb, or goat, in the camp, or that killeth it out of the camp,",
      "M": "Any man of Israel who slaughters an ox, a lamb, or a goat — whether inside the camp or outside the camp —",
      "T": "Any Israelite who slaughters a domestic animal — ox, sheep, or goat — whether inside the camp or outside it —"
    },
    "4": {
      "L": "And bringeth it not unto the door of the tabernacle of the congregation, to offer an offering unto the LORD before the tabernacle of the LORD; blood shall be imputed unto that man; he hath shed blood; and that man shall be cut off from among his people:",
      "M": "and does not bring it to the entrance of the tent of meeting to present as an offering to the LORD before the tabernacle of the LORD — bloodguilt shall be charged to that man. He has shed blood, and that man shall be cut off from among his people.",
      "T": "but does not bring it to the tent of meeting entrance to offer before the LORD — bloodguilt is charged to that man. He has shed blood. He is cut off from his people. All legitimate slaughter must pass through the altar."
    },
    "5": {
      "L": "To the end that the children of Israel may bring their sacrifices, which they offer in the open field, even that they may bring them unto the LORD, unto the door of the tabernacle of the congregation, unto the priest, and offer them for peace offerings unto the LORD.",
      "M": "This is so that the Israelites may bring the animals they now slaughter in the open field to the LORD — to the entrance of the tent of meeting to the priest — and sacrifice them as fellowship offerings to the LORD.",
      "T": "The purpose is to channel all Israel's animal offerings through the single legitimate altar. What was once slaughtered wherever becomes a fellowship offering at the tent of meeting."
    },
    "6": {
      "L": "And the priest shall sprinkle the blood upon the altar of the LORD at the door of the tabernacle of the congregation, and burn the fat for a sweet savour unto the LORD.",
      "M": "The priest shall throw the blood against the LORD's altar at the entrance of the tent of meeting and burn the fat as a pleasing aroma to the LORD.",
      "T": "The priest dashes the blood on the LORD's altar and burns the fat — a pleasing aroma. The meal becomes an act of worship."
    },
    "7": {
      "L": "And they shall no more offer their sacrifices unto devils, after whom they have gone a whoring. This shall be a statute for ever unto them throughout their generations.",
      "M": "They shall no longer sacrifice their offerings to the goat-demons after whom they have been prostituting themselves. This shall be a permanent statute throughout their generations.",
      "T": "The deeper reason: Israel has been offering to goat-demons — the spirit-beings of the wilderness. This law cuts that off permanently. All sacrifice must go to the LORD and to him alone. A permanent statute."
    },
    "8": {
      "L": "And thou shalt say unto them, Whatsoever man there be of the house of Israel, or of the strangers which sojourn among you, that offereth a burnt offering or sacrifice,",
      "M": "Say to them: Any man of Israel or any alien dwelling among you who offers a burnt offering or any sacrifice",
      "T": "Say to them: any Israelite or resident alien who brings a burnt offering or other sacrifice —"
    },
    "9": {
      "L": "And bringeth it not unto the door of the tabernacle of the congregation, to offer it unto the LORD; even that man shall be cut off from among his people.",
      "M": "and does not bring it to the entrance of the tent of meeting to offer it to the LORD — that man shall be cut off from his people.",
      "T": "but does not bring it to the tent of meeting entrance to offer to the LORD — that person is cut off from the community. No private altars; no rival shrines."
    },
    "10": {
      "L": "And whatsoever man there be of the house of Israel, or of the strangers that sojourn among you, that eateth any manner of blood; I will even set my face against that soul that eateth blood, and will cut him off from among his people.",
      "M": "Any man of Israel or any alien dwelling among you who eats any blood — I will set my face against that person who eats blood and will cut him off from his people.",
      "T": "Any Israelite or resident alien who eats blood in any form — I will set my face against that person and cut them off. This is a direct divine sanction, not merely a ritual infraction."
    },
    "11": {
      "L": "For the life of the flesh is in the blood: and I have given it to you upon the altar to make an atonement for your souls: for it is the blood that maketh an atonement for the soul.",
      "M": "For the life of the flesh is in the blood, and I have given it to you on the altar to make atonement for your lives. It is the blood that makes atonement by virtue of the life.",
      "T": "Here is why: blood carries the life-force of the creature. I have assigned it to the altar to make atonement for human life — life ransoms life. This is the theological foundation of the entire sacrificial system."
    },
    "12": {
      "L": "Therefore I said unto the children of Israel, No soul of you shall eat blood, neither shall any stranger that sojourneth among you eat blood.",
      "M": "Therefore I have said to the Israelites: no one among you — and no alien among you — shall eat blood.",
      "T": "That is why no one in Israel — and no resident alien — may eat blood. It belongs to the altar."
    },
    "13": {
      "L": "And whatsoever man there be of the children of Israel, or of the strangers that sojourn among you, which hunteth and catcheth any beast or fowl that may be eaten; he shall even pour out the blood thereof, and cover it with dust.",
      "M": "Any man of Israel or alien dwelling among you who hunts and catches a game animal or bird that may be eaten shall pour out its blood and cover it with earth.",
      "T": "When an Israelite or resident alien hunts and kills a game animal or bird that is clean for eating, he pours out the blood and covers it with soil — returning the life to the earth, refusing to consume it."
    },
    "14": {
      "L": "For it is the life of all flesh; the blood of it is for the life thereof: therefore I said unto the children of Israel, Ye shall eat the blood of no manner of flesh: for the life of all flesh is the blood thereof: whosoever eateth it shall be cut off.",
      "M": "For the life of every creature — its blood is its life. Therefore I said to the Israelites: you shall not eat the blood of any creature, for the life of every creature is its blood. Whoever eats it shall be cut off.",
      "T": "The life of every creature is its blood — blood and life are one. Therefore: no blood of any creature may be eaten by anyone in Israel. Eat it and be cut off. The prohibition is grounded in the sanctity of life itself."
    },
    "15": {
      "L": "And every soul that eateth that which died of itself, or that which was torn with beasts, whether it be one of your own country, or a stranger, shall both wash his clothes, and bathe himself in water, and be unclean until the even: then shall he be clean.",
      "M": "Every person — native or alien — who eats an animal that died naturally or was torn by wild animals shall wash his clothes and bathe in water, and be unclean until evening; then he will be clean.",
      "T": "Anyone who eats an animal that died on its own or was killed by a predator — their blood was not properly drained — must wash clothes, bathe, and wait until evening. Then clean."
    },
    "16": {
      "L": "But if he wash them not, nor bathe his flesh; then he shall bear his iniquity.",
      "M": "But if he does not wash his clothes and does not bathe, he shall bear the guilt.",
      "T": "If he skips the washing and bathing, he bears the guilt himself — the cleansing is required, not optional."
    }
  },
  "18": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and say unto them, I am the LORD your God.",
      "M": "Speak to the people of Israel and say to them: I am the LORD your God.",
      "T": "Tell Israel: I am the LORD your God."
    },
    "3": {
      "L": "After the doings of the land of Egypt, wherein ye dwelt, shall ye not do: and after the doings of the land of Canaan, whither I bring you, shall ye not do: neither shall ye walk in their statutes.",
      "M": "You shall not do as they do in the land of Egypt, where you used to live, and you shall not do as they do in the land of Canaan, where I am bringing you. You shall not walk in their statutes.",
      "T": "Egypt behind you, Canaan ahead — you shall not live by the customs of either. What the nations do, you shall not do. You are not shaped by where you were or where you are going; you are shaped by who I am."
    },
    "4": {
      "L": "Ye shall do my judgments, and keep mine ordinances, to walk therein: I am the LORD your God.",
      "M": "You shall observe my rules and keep my statutes and walk in them. I am the LORD your God.",
      "T": "Walk in my rules and keep my statutes. I am the LORD your God — that is the only identity that determines how you live."
    },
    "5": {
      "L": "Ye shall therefore keep my statutes, and my judgments: which if a man do, he shall live in them: I am the LORD.",
      "M": "Keep my statutes and my rules. By doing them a person shall live — I am the LORD.",
      "T": "Keep my statutes and rules. The one who does them lives by them — real life, life as God intended. I am the LORD."
    },
    "6": {
      "L": "None of you shall approach to any that is near of kin to him, to uncover their nakedness: I am the LORD.",
      "M": "None of you shall approach any close relative to have sexual relations. I am the LORD.",
      "T": "No one is to have sexual relations with a close relative. I am the LORD — the prohibition has the full force of divine authority."
    },
    "7": {
      "L": "The nakedness of thy father, or the nakedness of thy mother, shalt thou not uncover: she is thy mother; thou shalt not uncover her nakedness.",
      "M": "You shall not have sexual relations with your father or your mother. She is your mother; you shall not have sexual relations with her.",
      "T": "Do not have sexual relations with your father or your mother. She is your mother — this boundary is absolute."
    },
    "8": {
      "L": "The nakedness of thy father's wife shalt thou not uncover: it is thy father's nakedness.",
      "M": "You shall not have sexual relations with your father's wife. It is your father's nakedness.",
      "T": "Do not have sexual relations with your father's wife — even a stepmother. She belongs to your father's intimate sphere; to violate her is to violate him."
    },
    "9": {
      "L": "The nakedness of thy sister, the daughter of thy father, or daughter of thy mother, whether she be born at home, or born abroad, even their nakedness thou shalt not uncover.",
      "M": "You shall not have sexual relations with your sister — your father's daughter or your mother's daughter, whether born at home or outside. You shall not have sexual relations with her.",
      "T": "Do not have sexual relations with your sister — full sister or half-sister, raised in the same home or not. The sibling bond forecloses this."
    },
    "10": {
      "L": "The nakedness of thy son's daughter, or of thy daughter's daughter, even their nakedness thou shalt not uncover: for theirs is thine own nakedness.",
      "M": "You shall not have sexual relations with your son's daughter or your daughter's daughter, for their nakedness is your own nakedness.",
      "T": "Do not have sexual relations with your granddaughter — son's or daughter's. In harming them you harm yourself — their nakedness is an extension of your own."
    },
    "11": {
      "L": "The nakedness of thy father's wife's daughter, begotten of thy father, she is thy sister, thou shalt not uncover her nakedness.",
      "M": "You shall not have sexual relations with the daughter of your father's wife, begotten of your father — she is your sister; you shall not have sexual relations with her.",
      "T": "The daughter your father had by his wife — your half-sister on his side — is your sister. Do not have sexual relations with her."
    },
    "12": {
      "L": "Thou shalt not uncover the nakedness of thy father's sister: she is thy father's near kinswoman.",
      "M": "You shall not have sexual relations with your father's sister. She is your father's blood relative.",
      "T": "Do not have sexual relations with your father's sister — she is your father's own kin, and therefore yours."
    },
    "13": {
      "L": "Thou shalt not uncover the nakedness of thy mother's sister: for she is thy mother's near kinswoman.",
      "M": "You shall not have sexual relations with your mother's sister, for she is your mother's blood relative.",
      "T": "Do not have sexual relations with your mother's sister — she is your mother's kin."
    },
    "14": {
      "L": "Thou shalt not uncover the nakedness of thy father's brother, thou shalt not approach to his wife: she is thine aunt.",
      "M": "You shall not have sexual relations with your father's brother. You shall not approach his wife; she is your aunt.",
      "T": "Do not violate your father's brother's household — do not have sexual relations with his wife. She is your aunt."
    },
    "15": {
      "L": "Thou shalt not uncover the nakedness of thy daughter in law: she is thy son's wife; thou shalt not uncover her nakedness.",
      "M": "You shall not have sexual relations with your daughter-in-law. She is your son's wife; you shall not have sexual relations with her.",
      "T": "Do not have sexual relations with your daughter-in-law. She is your son's wife — that relationship belongs to him."
    },
    "16": {
      "L": "Thou shalt not uncover the nakedness of thy brother's wife: it is thy brother's nakedness.",
      "M": "You shall not have sexual relations with your brother's wife. It is your brother's nakedness.",
      "T": "Do not have sexual relations with your brother's wife. She belongs to his intimate sphere — to have her is to violate him."
    },
    "17": {
      "L": "Thou shalt not uncover the nakedness of a woman and her daughter, neither shalt thou take her son's daughter, or her daughter's daughter, to uncover her nakedness; for they are her near kinswomen: it is wickedness.",
      "M": "You shall not have sexual relations with a woman and her daughter. You shall not take her son's daughter or her daughter's daughter to have sexual relations with her. They are close relatives — it is depravity.",
      "T": "Do not have sexual relations with a woman and also with her daughter, or her granddaughter. They are close kin to each other; to take them together or in succession is moral corruption — it twists the bonds that define a family."
    },
    "18": {
      "L": "Neither shalt thou take a wife to her sister, to vex her, to uncover her nakedness, beside the other in her life time.",
      "M": "You shall not take a woman as a rival wife to her sister, uncovering her nakedness while her sister is still alive.",
      "T": "Do not marry a woman's sister as a rival while the first sister is still living. The anguish of such rivalry makes the arrangement an act of cruelty. Sisters are not competitors."
    },
    "19": {
      "L": "Also thou shalt not approach unto a woman to uncover her nakedness, as long as she is put apart for her uncleanness.",
      "M": "You shall not have sexual relations with a woman during the uncleanness of her menstrual separation.",
      "T": "Do not have sexual relations with a woman during her menstrual impurity. Her body in its monthly cycle is not to be violated."
    },
    "20": {
      "L": "Moreover thou shalt not lie carnally with thy neighbour's wife, to defile thyself with her.",
      "M": "You shall not have sexual relations with your neighbor's wife, defiling yourself with her.",
      "T": "Do not have sexual relations with your neighbor's wife. It defiles you — and it destroys him."
    },
    "21": {
      "L": "And thou shalt not let any of thy seed pass through the fire to Molech, neither shalt thou profane the name of thy God: I am the LORD.",
      "M": "You shall not give any of your children to be offered to Molech, and so profane the name of your God. I am the LORD.",
      "T": "Do not give any of your children as an offering to Molech. To do so is to profane the name of your God — you cannot worship Molech and call yourself the LORD's. I am the LORD."
    },
    "22": {
      "L": "Thou shalt not lie with mankind, as with womankind: it is abomination.",
      "M": "You shall not lie with a male as with a woman; it is an abomination.",
      "T": "Male-with-male sexual intercourse — this is an abomination."
    },
    "23": {
      "L": "Neither shalt thou lie with any beast to defile thyself therewith: neither shall any woman stand before a beast to lie down thereto: it is confusion.",
      "M": "You shall not have sexual relations with any animal, defiling yourself with it. A woman shall not stand before an animal to mate with it. It is a perversion.",
      "T": "Do not have sexual relations with an animal — man or woman. This is a confusion of kinds, a violation of the boundaries built into creation itself."
    },
    "24": {
      "L": "Defile not ye yourselves in any of these things: for in all these the nations are defiled which I cast out before you:",
      "M": "Do not defile yourselves by any of these things, for by all these practices the nations I am driving out before you have defiled themselves.",
      "T": "Do not defile yourselves through any of these acts. The nations currently occupying the land defiled themselves by all of them."
    },
    "25": {
      "L": "And the land is defiled: therefore I do visit the iniquity thereof upon it, and the land itself vomiteth out her inhabitants.",
      "M": "The land became defiled; I punished it for its iniquity, and the land vomited out its inhabitants.",
      "T": "And the land became defiled. The land itself is a moral actor in this theology — I punished its iniquity, and the land vomited out those who corrupted it. This is why those nations are being displaced."
    },
    "26": {
      "L": "Ye shall therefore keep my statutes and my judgments, and shall not commit any of these abominations; neither any of your own nation, nor any stranger that sojourneth among you:",
      "M": "But you shall keep my statutes and my rules and commit none of these abominations — neither the native-born nor the alien who dwells among you.",
      "T": "You shall keep my statutes and rules. None of these abominations — Israelite or resident alien. The moral law applies to all who live in the land."
    },
    "27": {
      "L": "(For all these abominations have the men of the land done, which were before you, and the land is defiled;)",
      "M": "For all these abominations were done by the people of the land before you, and the land became defiled.",
      "T": "The people before you did all these things. That is why the land became defiled."
    },
    "28": {
      "L": "That the land spue not you out also, when ye defile it, as it spued out the nations that were before you.",
      "M": "Lest the land vomit you out when you defile it, as it vomited out the nation before you.",
      "T": "Do not defile the land — or it will vomit you out too, just as it vomited them. Israel is not exempt from the land's moral logic."
    },
    "29": {
      "L": "For whosoever shall commit any of these abominations, even the souls that commit them shall be cut off from among their people.",
      "M": "For anyone who commits any of these abominations — the persons who do them shall be cut off from among their people.",
      "T": "Anyone who does these things is cut off from the community. The penalty is exclusion — severing from the covenant people."
    },
    "30": {
      "L": "Therefore shall ye keep mine ordinance, that ye commit not any one of these abominable customs, which were committed before you, and that ye defile not yourselves therein: I am the LORD your God.",
      "M": "Keep my charge: do not practice any of these abominable customs that were practiced before you, and do not defile yourselves by them. I am the LORD your God.",
      "T": "Keep my charge: do not practice these abominations that your predecessors practiced; do not defile yourselves through them. I am the LORD your God — your identity is determined by who I am, not by what the nations do."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'leviticus')
        merge_tier(existing, LEVITICUS, tier_key)
        save(tier_dir, 'leviticus', existing)
    print('Leviticus 13–18 written.')

if __name__ == '__main__':
    main()
