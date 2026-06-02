"""
MKT Leviticus chapters 25–27 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-leviticus-25-27.py

Covers: Sabbatical year and Jubilee (ch. 25); Blessings and Curses (ch. 26);
Vows, Valuations, and Tithes (ch. 27).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — matches all prior Leviticus scripts
- H430 (אֱלֹהִים): "God" in all three tiers
- H3104 (יוֹבֵל): "jubilee" / "Jubilee" — kept as the institution name in all tiers;
  T capitalises "Jubilee" to mark it as a named calendar institution
- H1350 (גָּאַל) kinsman-redeemer: L/M="redeem/redeemer"; T surfaces the patron-client
  and kinship-obligation dynamic explicitly where context warrants
- H2764 (חֵרֶם): L/M="devoted thing"; T="what is placed under the ban / cherem" —
  the irrevocable dedication that cannot be redeemed or sold; distinct from ordinary vows
- H5315 (נֶפֶשׁ): "person" in legal/penalty clauses throughout (embodied self, not immaterial soul)
- H8057/H8063 (שָׂדֶה אֲחֻזָּה): "field of his possession / inherited field" — ancestral land
  distinguished from purchased land in ch. 27 valuations
- H4503 (מִנְחָה): not prominent here; offering terms from prior scripts carried forward
- Ch. 25 Jubilee theology: the land belongs to the LORD (v. 23); Israel are tenants.
  T surfaces this landlord-tenant framework throughout the redemption laws.
- Ch. 25 slavery distinction: Israelite debt-servants treated as hired workers (vv. 39–43);
  foreign slaves may be held permanently (vv. 44–46). T notes the theological grounding
  ("they are my servants" v. 42) without harmonising the ethical tension.
- Ch. 26 Blessings and Curses: four escalating curse cycles (vv. 14–17, 18–20, 21–22, 23–26,
  27–39), each introduced by "if you will not listen." T preserves the escalating rhetoric.
- Ch. 26 exile theology: the land's sabbath rest during exile (vv. 34–35, 43) is interpreted
  as the land receiving what was denied it — T surfaces this irony explicitly.
- Ch. 26 restoration promise (vv. 40–45): conditional on confession; T names the uncircumcised
  heart as the barrier that must be broken. The covenant trilogy (Jacob–Isaac–Abraham) noted
  in reverse chronological order — echoes the exile-to-origins logic.
- Ch. 27 valuation tables: L reproduces the age-band and shekel amounts verbatim;
  M restates in natural English; T notes the economic and social logic where non-obvious.
- H5769 (עוֹלָם): "for ever / permanent / perpetual" — context determines; L=literal,
  M="permanent/perpetual," T adds interpretive gloss where needed.
- Sanctuary shekel (27:25): twenty gerahs — noted in T as the standard weight reference
  that underlies all valuations in the chapter.
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
  "25": {
    "1": {
      "L": "And the LORD spake unto Moses in mount Sinai, saying,",
      "M": "The LORD spoke to Moses on Mount Sinai, saying,",
      "T": "The LORD spoke to Moses on Mount Sinai:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and say unto them: When ye come into the land which I give you, then shall the land keep a sabbath unto the LORD.",
      "M": "Speak to the Israelites and say to them: When you come into the land that I am giving you, the land shall observe a sabbath to the LORD.",
      "T": "Tell Israel: when you enter the land I am giving you, the land itself must keep a Sabbath to the LORD."
    },
    "3": {
      "L": "Six years thou shalt sow thy field, and six years thou shalt prune thy vineyard, and gather in the fruit thereof;",
      "M": "For six years you shall sow your field and prune your vineyard and gather its fruit,",
      "T": "For six years sow your fields, prune your vines, and gather the harvest."
    },
    "4": {
      "L": "But in the seventh year shall be a sabbath of rest unto the land, a sabbath for the LORD: thou shalt neither sow thy field, nor prune thy vineyard.",
      "M": "but in the seventh year the land shall have a sabbath of complete rest — a sabbath to the LORD. You shall not sow your field or prune your vineyard.",
      "T": "But in the seventh year the land has its Sabbath — a year of complete rest belonging to the LORD. Do not sow. Do not prune."
    },
    "5": {
      "L": "That which groweth of its own accord of thy harvest thou shalt not reap, neither gather the grapes of thy vine undressed: for it is a year of rest unto the land.",
      "M": "Whatever the land produces on its own you shall not reap, and the grapes of your unpruned vine you shall not gather, for it is a year of rest for the land.",
      "T": "What grows on its own you must not harvest; the grapes of the untended vine you must not pick — it is the land's year of rest."
    },
    "6": {
      "L": "And the sabbath of the land shall be food for you: for thee, and for thy servant, and for thy maid, and for thy hired servant, and for thy stranger that sojourneth with thee,",
      "M": "But the sabbath produce of the land shall be food for all of you — for you, your male servant, your female servant, your hired worker, and the foreigner who lives among you,",
      "T": "What the land yields on its own in that sabbath year is food for everyone — you, your servants, your hired workers, and the foreigner living among you."
    },
    "7": {
      "L": "And for thy cattle, and for the beast that are in thy land, shall all the increase thereof be meat.",
      "M": "and for your livestock and the wild animals in your land — all its produce may be used as food.",
      "T": "Even your livestock and the wild animals in the land may eat what it produces."
    },
    "8": {
      "L": "And thou shalt number seven sabbaths of years unto thee, seven times seven years; and the space of the seven sabbaths of years shall be unto thee forty and nine years.",
      "M": "You shall count seven weeks of years — seven times seven years — so that the period of seven weeks of years gives you forty-nine years.",
      "T": "Count seven Sabbath years — seven times seven — forty-nine years in all."
    },
    "9": {
      "L": "Then shalt thou cause the trumpet of the jubilee to sound on the tenth day of the seventh month, in the day of atonement shall ye make the trumpet sound throughout all your land.",
      "M": "Then on the tenth day of the seventh month — the Day of Atonement — you shall sound the loud trumpet throughout all your land.",
      "T": "On the tenth day of the seventh month — the Day of Atonement — sound the ram's horn across the whole land."
    },
    "10": {
      "L": "And ye shall hallow the fiftieth year, and proclaim liberty throughout all the land unto all the inhabitants thereof: it shall be a jubilee unto you; and ye shall return every man unto his possession, and ye shall return every man unto his family.",
      "M": "You shall consecrate the fiftieth year and proclaim freedom throughout the land to all its inhabitants. It shall be a jubilee for you, and each of you shall return to his property and to his family.",
      "T": "Consecrate the fiftieth year. Proclaim freedom throughout the land to all its inhabitants. It is the Jubilee — every person returns to his ancestral land and to his family."
    },
    "11": {
      "L": "A jubilee shall that fiftieth year be unto you: ye shall not sow, neither reap that which groweth of itself in it, nor gather the grapes in it of thy vine undressed.",
      "M": "That fiftieth year shall be a jubilee for you; you shall not sow or reap its spontaneous growth or harvest the grapes of its untended vine.",
      "T": "The fiftieth year is the Jubilee — do not sow, do not reap what grows on its own, do not gather grapes from untended vines."
    },
    "12": {
      "L": "For it is the jubilee; it shall be holy unto you: ye shall eat the increase thereof out of the field.",
      "M": "For it is the jubilee; it shall be holy to you. You may eat what it produces directly from the field.",
      "T": "The Jubilee is holy. Eat what the land freely gives — take it directly from the field."
    },
    "13": {
      "L": "In the year of this jubilee ye shall return every man unto his possession.",
      "M": "In this year of jubilee each of you shall return to his own property.",
      "T": "In the Jubilee year, every person returns to his ancestral land."
    },
    "14": {
      "L": "And if thou sell ought unto thy neighbour, or buyest ought of thy neighbour's hand, ye shall not oppress one another:",
      "M": "If you sell something to your neighbor or buy from your neighbor's hand, do not oppress one another.",
      "T": "When you buy or sell anything to a neighbor, deal honestly — do not exploit one another."
    },
    "15": {
      "L": "According to the number of years after the jubilee thou shalt buy of thy neighbour, and according unto the number of years of the fruits he shall sell unto thee:",
      "M": "According to the number of years after the jubilee you shall buy from your neighbor, and according to the number of years of harvests remaining he shall sell to you.",
      "T": "The price reflects the number of harvests left before the next Jubilee — more years remaining, higher the price; fewer years, lower."
    },
    "16": {
      "L": "According to the multitude of years thou shalt increase the price thereof, and according to the fewness of years thou shalt diminish the price of it: for according to the number of the years of the fruits doth he sell unto thee.",
      "M": "You shall increase the price for more years and decrease it for fewer years, for it is the number of annual harvests that he is selling to you.",
      "T": "Many harvests to come: higher price. Few harvests left: lower price. What is really being sold is the right to harvest — not the land itself."
    },
    "17": {
      "L": "Ye shall not therefore oppress one another; but thou shalt fear thy God: for I am the LORD your God.",
      "M": "You shall not oppress one another, but you shall fear your God; for I am the LORD your God.",
      "T": "Do not exploit one another in these transactions. Fear your God — I am the LORD your God."
    },
    "18": {
      "L": "Wherefore ye shall do my statutes, and keep my judgments, and do them; and ye shall dwell in the land in safety.",
      "M": "Therefore you shall carry out my statutes and keep my rules and do them, and you will live securely in the land.",
      "T": "Keep my statutes and carry out my rulings — then you will live safely in the land."
    },
    "19": {
      "L": "And the land shall yield her fruit, and ye shall eat your fill, and dwell therein in safety.",
      "M": "The land will yield its fruit and you will eat your fill and dwell in it securely.",
      "T": "The land will yield its harvest, you will eat to the full, and you will live there in safety."
    },
    "20": {
      "L": "And if ye shall say, What shall we eat the seventh year? behold, we shall not sow, nor gather in our increase:",
      "M": "If you ask, 'What shall we eat in the seventh year, since we do not sow or gather in our harvest?'",
      "T": "You may wonder: what will we eat in the seventh year, if we cannot sow or gather the harvest?"
    },
    "21": {
      "L": "Then I will command my blessing upon you in the sixth year, and it shall bring forth fruit for three years.",
      "M": "I will command my blessing on you in the sixth year so that it will yield a crop sufficient for three years.",
      "T": "I will send my blessing in the sixth year so that the harvest is enough for three years."
    },
    "22": {
      "L": "And ye shall sow the eighth year, and eat yet of old fruit until the ninth year; until her fruits come in ye shall eat of the old store.",
      "M": "You will sow in the eighth year and eat from the old harvest until the ninth year — until the new harvest comes in, you will eat of the old.",
      "T": "You sow again in the eighth year. You eat from the stored harvest all through the eighth year and into the ninth — until the new crop is ready, the old sustains you."
    },
    "23": {
      "L": "The land shall not be sold for ever: for the land is mine; for ye are strangers and sojourners with me.",
      "M": "The land shall not be sold permanently, for the land is mine; you are but aliens and sojourners with me.",
      "T": "The land may never be sold in permanent transfer — it belongs to me. You are resident aliens on my land, my tenants."
    },
    "24": {
      "L": "And in all the land of your possession ye shall grant a redemption for the land.",
      "M": "Throughout the land that you hold as a possession, you shall allow the land to be redeemed.",
      "T": "Across all the land you hold, the right of redemption must always remain open."
    },
    "25": {
      "L": "If thy brother be waxen poor, and hath sold away some of his possession, and if any of his kin come to redeem it, then shall he redeem that which his brother sold.",
      "M": "If your brother becomes poor and sells some of his property, his nearest redeemer shall come and redeem what his brother has sold.",
      "T": "If a fellow Israelite falls into poverty and sells some of his land, his nearest kinsman may act as redeemer and buy it back."
    },
    "26": {
      "L": "And if the man have none to redeem it, and himself be able to redeem it;",
      "M": "If a man has no one to redeem it for him but he himself becomes prosperous enough to redeem it,",
      "T": "If the man has no kinsman-redeemer but later earns enough to redeem it himself,"
    },
    "27": {
      "L": "Then let him count the years of the sale thereof, and restore the overplus unto the man to whom he sold it; that he may return unto his possession.",
      "M": "he shall calculate the years since the sale and refund the balance to the man he sold it to, and so return to his property.",
      "T": "he calculates what the buyer has already received, pays back the balance, and reclaims his land."
    },
    "28": {
      "L": "But if he be not able to restore it to him, then that which is sold shall remain in the hand of him that hath bought it until the year of jubilee: and in the jubilee it shall go out, and he shall return unto his possession.",
      "M": "But if he cannot afford to pay it back, what he sold shall remain in the hand of the buyer until the year of jubilee; in the jubilee it shall be released and he shall return to his property.",
      "T": "If he cannot afford to buy it back, the land stays with the buyer until the Jubilee — then it is released and returns to its original owner."
    },
    "29": {
      "L": "And if a man sell a dwelling house in a walled city, then he may redeem it within a whole year after it is sold; within a full year may he redeem it.",
      "M": "If a man sells a dwelling house in a walled city, he may redeem it within one full year of its sale; he may redeem it during that year.",
      "T": "A house inside a walled city: the seller has exactly one full year to buy it back."
    },
    "30": {
      "L": "And if it be not redeemed within the space of a full year, then the house that is in the walled city shall be established for ever to him that bought it throughout his generations: it shall not go out in the jubilee.",
      "M": "If it is not redeemed within a full year, the house in the walled city shall belong permanently to the buyer and his descendants throughout their generations; it does not go free in the jubilee.",
      "T": "If not redeemed within the year, the house becomes the buyer's permanently — in perpetuity — and it does not return in the Jubilee."
    },
    "31": {
      "L": "But the houses of the villages which have no wall round about them shall be counted as the fields of the country: they may be redeemed, and they shall go out in the jubilee.",
      "M": "But houses in villages without surrounding walls shall be treated like open-field land — they may be redeemed, and they shall be released in the jubilee.",
      "T": "Houses in unwalled villages are treated like farmland — they can be redeemed at any time and return in the Jubilee."
    },
    "32": {
      "L": "Notwithstanding the cities of the Levites, and the houses of the cities of their possession, may the Levites redeem at any time.",
      "M": "As for the cities of the Levites — the houses in the cities that are their possession — the Levites may redeem at any time.",
      "T": "Exception: the Levites may always redeem their houses in their designated cities, at any time."
    },
    "33": {
      "L": "And if a man purchase of the Levites, then the house that was sold, and the city of his possession, shall go out in the year of jubilee: for the houses of the cities of the Levites are their possession among the children of Israel.",
      "M": "If someone buys a house from the Levites, the sold house in the Levitical city shall be released in the year of jubilee, for the houses in the Levitical cities are the Levites' permanent possession among the Israelites.",
      "T": "If anyone purchases a house in a Levitical city, it returns in the Jubilee — those cities are the Levites' permanent inheritance among Israel."
    },
    "34": {
      "L": "But the field of the suburbs of their cities may not be sold; for it is their perpetual possession.",
      "M": "But the open land around their cities may not be sold, for it is their permanent possession.",
      "T": "The grazing land around the Levitical cities cannot be sold at all — it is the Levites' permanent inheritance."
    },
    "35": {
      "L": "And if thy brother be waxen poor, and fallen in decay with thee; then thou shalt relieve him: yea, though he be a stranger, or a sojourner; that he may live with thee.",
      "M": "If your brother becomes poor and cannot support himself beside you, you shall support him — whether he is a native or a foreigner — that he may live alongside you.",
      "T": "If a fellow Israelite falls into poverty and can no longer support himself beside you, support him — whether he is a native or a resident foreigner — so he can go on living with you."
    },
    "36": {
      "L": "Take thou no usury of him, or increase: but fear thy God; that thy brother may live with thee.",
      "M": "Do not take interest or profit from him, but fear your God, that your brother may live beside you.",
      "T": "Do not charge him interest or demand a profit — fear your God instead, so that your neighbor can survive."
    },
    "37": {
      "L": "Thou shalt not give him thy money upon usury, nor lend him thy victuals for increase.",
      "M": "You shall not lend him money at interest or give him food for profit.",
      "T": "Do not lend money at interest. Do not sell him food at a markup."
    },
    "38": {
      "L": "I am the LORD your God, which brought you forth out of the land of Egypt, to give you the land of Canaan, and to be your God.",
      "M": "I am the LORD your God, who brought you out of the land of Egypt to give you the land of Canaan and to be your God.",
      "T": "I am the LORD your God, who brought you out of Egypt to give you Canaan and to be your God."
    },
    "39": {
      "L": "And if thy brother that dwelleth by thee be waxen poor, and be sold unto thee; thou shalt not compel him to serve as a bondservant:",
      "M": "If your brother beside you becomes poor and sells himself to you, you shall not make him work as a slave.",
      "T": "If a fellow Israelite falls so deep into poverty that he must sell himself to you, do not treat him as a slave."
    },
    "40": {
      "L": "But as an hired servant, and as a sojourner, he shall be with thee, and shall serve thee unto the year of jubilee:",
      "M": "He shall be with you as a hired worker and as a resident alien; he shall serve you until the year of jubilee.",
      "T": "Treat him as a hired worker, a fellow resident — he serves you until the Jubilee."
    },
    "41": {
      "L": "And then shall he depart from thee, both he and his children with him, and shall return unto his own family, and unto the possession of his fathers shall he return.",
      "M": "Then he shall go free from you — he and his children with him — and return to his family and to the ancestral property of his fathers.",
      "T": "Then he goes free — he and his children — to return to his family and his ancestral land."
    },
    "42": {
      "L": "For they are my servants, which I brought forth out of the land of Egypt: they shall not be sold as bondmen.",
      "M": "For they are my servants, whom I brought out of the land of Egypt; they shall not be sold as slaves.",
      "T": "They are my servants — I brought them out of Egypt. They must not be sold as slaves."
    },
    "43": {
      "L": "Thou shalt not rule over him with rigour; but shalt fear thy God.",
      "M": "You shall not rule over him harshly but shall fear your God.",
      "T": "Do not treat him harshly. Fear your God."
    },
    "44": {
      "L": "Both thy bondmen, and thy bondmaids, which thou shalt have, shall be of the heathen that are round about you; of them shall ye buy bondmen and bondmaids.",
      "M": "As for your male and female slaves — they may be from the nations that are around you; from them you may buy male and female slaves.",
      "T": "Your permanent slaves are to come from the surrounding nations — you may purchase them."
    },
    "45": {
      "L": "Moreover of the children of the strangers that do sojourn among you, of them shall ye buy, and of their families that are with you, which they begat in your land: and they shall be your possession.",
      "M": "You may also buy from the children of foreigners who sojourn among you, and from their families that are with you who were born in your land; they shall become your property.",
      "T": "You may also purchase from the children of foreigners living among you — from those born in your land. They may become your property."
    },
    "46": {
      "L": "And ye shall take them as an inheritance for your children after you, to inherit them for a possession; they shall be your bondmen for ever: but over your brethren the children of Israel, ye shall not rule one over another with rigour.",
      "M": "You may leave them to your children after you as an inheritance and hold them as property permanently; they shall be your slaves. But over your fellow Israelites, you shall not rule one over another harshly.",
      "T": "They can be passed on to your children as permanent property. But over your fellow Israelites, you must never exercise the harsh dominion of a slave-master."
    },
    "47": {
      "L": "And if a sojourner or stranger wax rich by thee, and thy brother that dwelleth by him wax poor, and sell himself unto the stranger or sojourner by thee, or to the stock of the stranger's family:",
      "M": "If a sojourner or foreigner among you becomes rich and your brother beside him becomes poor and sells himself to the foreigner sojourning with you, or to a member of the foreigner's family,",
      "T": "If a foreigner living among you prospers while a fellow Israelite beside him falls into poverty and sells himself to that foreigner or to a member of his household —"
    },
    "48": {
      "L": "After that he is sold he may be redeemed again; one of his brethren may redeem him:",
      "M": "after he is sold he retains the right of redemption; one of his brothers may redeem him,",
      "T": "even then he retains the right to be redeemed. A kinsman may redeem him —"
    },
    "49": {
      "L": "Either his uncle, or his uncle's son, may redeem him, or any that is nigh of kin unto him of his family may redeem him; or if he be able, he may redeem himself.",
      "M": "his uncle or his uncle's son may redeem him, or any close relative from his family may redeem him; or if he becomes prosperous, he may redeem himself.",
      "T": "his uncle, his uncle's son, or any near relative from his clan may do so. Or if he prospers, he may redeem himself."
    },
    "50": {
      "L": "And he shall reckon with him that bought him from the year that he was sold to him unto the year of jubilee: and the price of his sale shall be according unto the number of years, according to the time of an hired servant shall it be with him.",
      "M": "He shall reckon with his buyer from the year he sold himself up to the year of jubilee; the price of his release shall be based on the number of years remaining, calculated at the rate of a hired worker's wages.",
      "T": "He and his master calculate: from the year he was sold to the Jubilee, how many years remain? The redemption price is based on that period, treating each year as wages owed a hired worker."
    },
    "51": {
      "L": "If there be yet many years behind, according unto them he shall give again the price of his redemption out of the money that he was bought for.",
      "M": "If there are many years remaining, he shall refund a proportionate portion of his purchase price as the redemption payment.",
      "T": "If many years remain before the Jubilee, he refunds a larger portion of the purchase price."
    },
    "52": {
      "L": "And if there remain but few years unto the year of jubilee, then he shall count with him, and according unto his years shall he give him again the price of his redemption.",
      "M": "And if few years remain until the year of jubilee, he shall calculate with him; he shall repay according to the years remaining as his redemption payment.",
      "T": "If only a few years remain, the redemption payment is proportionally smaller."
    },
    "53": {
      "L": "And as a yearly hired servant shall he be with him: and the other shall not rule over him with rigour in thy sight.",
      "M": "He shall be with his master as a worker hired year by year; and the other shall not rule over him harshly in your sight.",
      "T": "He is to be treated as an annual wage-worker. The foreigner must not rule over him harshly — Israel is watching."
    },
    "54": {
      "L": "And if he be not redeemed in these years, then he shall go out in the year of jubilee, both he and his children with him.",
      "M": "And if he is not redeemed in these ways, he shall go free in the year of jubilee — he and his children with him.",
      "T": "If he is not redeemed through any of these means, the Jubilee sets him free — along with his children."
    },
    "55": {
      "L": "For unto me the children of Israel are servants; they are my servants whom I brought forth out of the land of Egypt: I am the LORD your God.",
      "M": "For to me the Israelites are servants; they are my servants whom I brought out of the land of Egypt: I am the LORD your God.",
      "T": "The Israelites are my servants — mine. I brought them out of Egypt. I am the LORD your God."
    }
  },
  "26": {
    "1": {
      "L": "Ye shall make you no idols nor graven image, neither rear you up a standing image, neither shall ye set up any image of stone in your land, to bow down unto it: for I am the LORD your God.",
      "M": "You shall make for yourselves no idols and set up no carved image or sacred pillar; you shall not set up any figured stone in your land to bow down to it, for I am the LORD your God.",
      "T": "Make no idols, erect no carved image or sacred pillar, set up no figured stone for worship. I am the LORD your God."
    },
    "2": {
      "L": "Ye shall keep my sabbaths, and reverence my sanctuary: I am the LORD.",
      "M": "Keep my sabbaths and revere my sanctuary: I am the LORD.",
      "T": "Keep my Sabbaths. Hold my sanctuary in reverence. I am the LORD."
    },
    "3": {
      "L": "If ye walk in my statutes, and keep my commandments, and do them;",
      "M": "If you walk in my statutes and keep my commandments and do them,",
      "T": "If you live by my statutes and keep my commandments —"
    },
    "4": {
      "L": "Then I will give you rain in due season, and the land shall yield her increase, and the trees of the field shall yield their fruit.",
      "M": "I will give you your rains in their season, and the land shall yield its produce, and the trees of the field shall yield their fruit.",
      "T": "I will send rain in season. The land will yield its harvest. The trees will bear fruit."
    },
    "5": {
      "L": "And your threshing shall reach unto the vintage, and the vintage shall reach unto the sowing time: and ye shall eat your bread to the full, and dwell in your land safely.",
      "M": "Your threshing shall last until the grape harvest, and the grape harvest shall last until sowing time; you shall eat your bread to the full and dwell in your land securely.",
      "T": "The harvest will keep you busy until the grape harvest, and the grape harvest until planting time — abundance all year. You will eat your fill and live in your land without fear."
    },
    "6": {
      "L": "And I will give peace in the land, and ye shall lie down, and none shall make you afraid: and I will rid evil beasts out of the land, neither shall the sword go through your land.",
      "M": "I will give peace in the land, and you will lie down with no one to make you afraid. I will remove dangerous animals from the land, and no sword shall pass through your land.",
      "T": "I will give peace to the land. You will lie down and no one will terrify you. I will drive dangerous animals from the land. No war will cross your borders."
    },
    "7": {
      "L": "And ye shall chase your enemies, and they shall fall before you by the sword.",
      "M": "You shall chase your enemies, and they shall fall before you by the sword.",
      "T": "When enemies come, you will pursue them — they will fall before you by the sword."
    },
    "8": {
      "L": "And five of you shall chase an hundred, and an hundred of you shall put ten thousand to flight: and your enemies shall fall before you by the sword.",
      "M": "Five of you shall chase a hundred, and a hundred of you shall chase ten thousand, and your enemies shall fall before you by the sword.",
      "T": "Five of you will rout a hundred. A hundred of you will put ten thousand to flight. Your enemies will fall by the sword before you."
    },
    "9": {
      "L": "For I will have respect unto you, and make you fruitful, and multiply you, and establish my covenant with you.",
      "M": "I will turn to you and make you fruitful and multiply you, and I will confirm my covenant with you.",
      "T": "I will look on you with favor, make you fruitful, multiply your numbers, and uphold my covenant with you."
    },
    "10": {
      "L": "And ye shall eat old store, and bring forth the old because of the new.",
      "M": "You shall eat the stored harvest from past years and clear out the old to make room for the new.",
      "T": "You will still be eating from the previous year's harvest when the new crop forces it out — abundance upon abundance."
    },
    "11": {
      "L": "And I will set my tabernacle among you: and my soul shall not abhor you.",
      "M": "I will set my dwelling among you, and I will not abhor you.",
      "T": "I will make my home among you and will not reject you."
    },
    "12": {
      "L": "And I will walk among you, and will be your God, and ye shall be my people.",
      "M": "I will walk among you and will be your God, and you shall be my people.",
      "T": "I will walk among you. I will be your God. You will be my people."
    },
    "13": {
      "L": "I am the LORD your God, which brought you forth out of the land of Egypt, that ye should not be their bondmen; and I have broken the bands of your yoke, and made you go upright.",
      "M": "I am the LORD your God, who brought you out of the land of Egypt so that you would not be their slaves. I broke the bars of your yoke and made you walk upright.",
      "T": "I am the LORD your God, who brought you out of Egypt — out of slavery. I snapped the yoke from your neck and made you stand upright. That freedom is what is at stake."
    },
    "14": {
      "L": "But if ye will not hearken unto me, and will not do all these commandments;",
      "M": "But if you will not listen to me and will not carry out all these commandments,",
      "T": "But if you refuse to listen — if you will not carry out all these commandments —"
    },
    "15": {
      "L": "And if ye shall despise my statutes, or if your soul abhor my judgments, so that ye will not do all my commandments, but that ye break my covenant:",
      "M": "if you despise my statutes, if your soul abhors my rules so that you will not carry out all my commandments and so break my covenant,",
      "T": "if you despise my statutes, if you loathe my rulings so completely that you refuse all my commands and break my covenant —"
    },
    "16": {
      "L": "I also will do this unto you; I will even appoint over you terror, consumption, and the burning ague, that shall consume the eyes, and cause sorrow of heart: and ye shall sow your seed in vain, for your enemies shall eat it.",
      "M": "then I in turn will do this to you: I will visit you with sudden terror, with wasting disease and fever that consume the eyes and cause the heart to pine. You shall sow your seed in vain, for your enemies shall eat it.",
      "T": "then I will bring on you sudden terror — wasting disease and burning fever that dim your eyes and drain your life away. You will plant, but your enemies will eat the harvest."
    },
    "17": {
      "L": "And I will set my face against you, and ye shall be slain before your enemies: they that hate you shall reign over you; and ye shall flee when none pursueth you.",
      "M": "I will set my face against you, and you shall be struck down before your enemies. Those who hate you shall rule over you, and you shall flee when no one pursues you.",
      "T": "I will set my face against you. You will be struck down before your enemies. Those who hate you will dominate you. You will run in panic when no one is even chasing you."
    },
    "18": {
      "L": "And if ye will not yet for all this hearken unto me, then I will punish you seven times more for your sins.",
      "M": "And if for all this you still will not listen to me, then I will punish you seven times more for your sins.",
      "T": "If after all this you still refuse to listen, I will multiply your punishment sevenfold."
    },
    "19": {
      "L": "And I will break the pride of your power; and I will make your heaven as iron, and your earth as brass:",
      "M": "I will break your proud power. I will make your sky like iron and your earth like bronze,",
      "T": "I will shatter the pride your strength gives you. Your sky will be iron — no rain. Your earth will be bronze — no harvest."
    },
    "20": {
      "L": "And your strength shall be spent in vain: for your land shall not yield her increase, neither shall the trees of the land yield their fruits.",
      "M": "and your strength shall be spent in vain, for your land shall not yield its produce, and the trees of the land shall not yield their fruit.",
      "T": "All your labor will be wasted — the land yields nothing, the trees bear nothing."
    },
    "21": {
      "L": "And if ye walk contrary unto me, and will not hearken unto me; I will bring seven times more plagues upon you according to your sins.",
      "M": "Then if you walk contrary to me and will not listen to me, I will continue to strike you seven times for your sins.",
      "T": "If you keep defying me — still refusing to listen — I will strike you again, sevenfold, fitting the punishment to the sin."
    },
    "22": {
      "L": "I will also send wild beasts among you, which shall rob you of your children, and destroy your cattle, and make you few in number; and your high ways shall be desolate.",
      "M": "I will let loose wild animals among you, which shall bereave you of your children, destroy your livestock, and make you few in number, so that your roads shall become desolate.",
      "T": "I will unleash wild animals against you. They will tear your children away, decimate your livestock, shrink your numbers — and the roads will go empty."
    },
    "23": {
      "L": "And if ye will not be reformed by me by these things, but will walk contrary unto me;",
      "M": "And if by these things you are not disciplined by me and you still walk contrary to me,",
      "T": "If these things still do not bring you to repentance — if you continue to defy me —"
    },
    "24": {
      "L": "Then will I also walk contrary unto you, and will punish you yet seven times for your sins.",
      "M": "then I also will walk contrary to you, and I myself will strike you sevenfold for your sins.",
      "T": "then I myself will be your adversary and multiply your punishment sevenfold for your sins."
    },
    "25": {
      "L": "And I will bring a sword upon you, that shall avenge the quarrel of my covenant: and when ye are gathered together within your cities, I will send the pestilence among you; and ye shall be delivered into the hand of the enemy.",
      "M": "I will bring a sword against you that will execute the vengeance of my covenant, and when you are gathered in your cities I will send pestilence among you, and you shall be delivered into the hand of the enemy.",
      "T": "I will bring war against you — war that avenges the broken covenant. When you crowd into your cities for safety, I will send plague among you, and you will be handed over to the enemy."
    },
    "26": {
      "L": "And when I have broken the staff of your bread, ten women shall bake your bread in one oven, and they shall deliver you your bread again by weight: and ye shall eat, and not be satisfied.",
      "M": "When I break your supply of bread, ten women shall bake your bread in a single oven and shall dole out your bread by weight, and you shall eat and not be satisfied.",
      "T": "I will cut off your food supply. Ten women will share one oven — bread rationed out by weight — and you will eat but never feel full."
    },
    "27": {
      "L": "And if ye will not for all this hearken unto me, but walk contrary unto me;",
      "M": "And if in spite of all this you will not listen to me, but still walk contrary to me,",
      "T": "If even this does not bring you to obedience — if you still defy me —"
    },
    "28": {
      "L": "Then I will walk contrary unto you also in fury; and I, even I, will chastise you seven times for your sins.",
      "M": "then I will walk contrary to you in anger, and I myself will discipline you seven times for your sins.",
      "T": "then I will confront you in fury — I myself — and punish you sevenfold for your sins."
    },
    "29": {
      "L": "And ye shall eat the flesh of your sons, and the flesh of your daughters shall ye eat.",
      "M": "You shall eat the flesh of your sons, and you shall eat the flesh of your daughters.",
      "T": "You will eat the flesh of your own sons and daughters — the final horror of famine and siege."
    },
    "30": {
      "L": "And I will destroy your high places, and cut down your images, and cast your carcases upon the carcases of your idols, and my soul shall abhor you.",
      "M": "I will destroy your high places and cut down your incense altars and cast your dead bodies on the lifeless forms of your idols, and my soul shall abhor you.",
      "T": "I will demolish your high places, cut down your incense altars, and pile your corpses on the rubble of your idols. I will reject you utterly."
    },
    "31": {
      "L": "And I will make your cities waste, and bring your sanctuaries unto desolation, and I will not smell the savour of your sweet odours.",
      "M": "I will lay your cities in ruins and bring your sanctuaries to desolation, and I will not smell your pleasing offerings.",
      "T": "I will reduce your cities to rubble and make your sanctuaries desolate. I will no longer receive your offerings — their fragrance means nothing to me now."
    },
    "32": {
      "L": "And I will bring the land into desolation: and your enemies which dwell therein shall be astonished at it.",
      "M": "I will make the land desolate so that your enemies who settle in it shall be appalled by it.",
      "T": "The land itself will become a wasteland — so utterly destroyed that even your conquerors will be shocked by it."
    },
    "33": {
      "L": "And I will scatter you among the heathen, and will draw out a sword after you: and your land shall be desolate, and your cities waste.",
      "M": "I will scatter you among the nations, and I will unsheathe the sword against you; your land shall be a desolation, and your cities shall be a waste.",
      "T": "I will scatter you among the nations and pursue you with the sword. Your land will lie in ruin. Your cities will be empty ruins."
    },
    "34": {
      "L": "Then shall the land enjoy her sabbaths, as long as it lieth desolate, and ye be in your enemies' land; even then shall the land rest, and enjoy her sabbaths.",
      "M": "Then the land shall enjoy its sabbaths all the days that it lies desolate while you are in your enemies' land. Even then the land shall rest and enjoy its sabbaths.",
      "T": "Only then, while the land lies empty and you are in exile, will it enjoy all the sabbath years you denied it. The land gets its rest — at your expense."
    },
    "35": {
      "L": "As long as it lieth desolate it shall rest; because it did not rest in your sabbaths, when ye dwelt upon it.",
      "M": "All the days that it lies desolate it shall have the rest that it did not have on your sabbaths when you were living in it.",
      "T": "Every year of exile is a sabbath for the land — the rest it was owed but never given while you lived on it."
    },
    "36": {
      "L": "And upon them that are left alive of you I will send a faintness into their hearts in the lands of their enemies; and the sound of a shaken leaf shall chase them; and they shall flee, as fleeing from a sword; and they shall fall when none pursueth.",
      "M": "As for those of you who survive, I will bring fear into their hearts in the lands of their enemies, so that the sound of a driven leaf shall put them to flight, and they shall flee as one flees from the sword, and they shall fall when no one pursues them.",
      "T": "Those who survive among your enemies will be paralyzed with fear. The rustling of a leaf will send them running as if from a sword — they will stumble and fall though no one is chasing them."
    },
    "37": {
      "L": "And they shall fall one upon another, as it were before a sword, when none pursueth: and ye shall have no power to stand before your enemies.",
      "M": "They shall stumble over one another, as before a sword, when none pursues; and you shall have no power to stand before your enemies.",
      "T": "They will trip over each other in the rout — as if fleeing a sword, with no enemy in sight. You will be unable to make a stand."
    },
    "38": {
      "L": "And ye shall perish among the heathen, and the land of your enemies shall eat you up.",
      "M": "You shall perish among the nations, and the land of your enemies shall consume you.",
      "T": "You will waste away among the nations. The foreign lands will swallow you up."
    },
    "39": {
      "L": "And they that are left of you shall pine away in their iniquity in your enemies' lands; and also in the iniquities of their fathers shall they pine away with them.",
      "M": "And those of you who survive shall rot away in their iniquity in the lands of your enemies; they shall also rot away in the iniquities of their fathers.",
      "T": "The survivors will waste away in exile, weighed down by their own sins — and by the accumulated guilt of their ancestors."
    },
    "40": {
      "L": "If they shall confess their iniquity, and the iniquity of their fathers, with their trespass which they trespassed against me, and that also they have walked contrary unto me;",
      "M": "But if they confess their iniquity and the iniquity of their fathers — the treachery they committed against me and their walking contrary to me,",
      "T": "But if they confess — their sin and their fathers' sin, the faithlessness they showed me, the defiance they lived in —"
    },
    "41": {
      "L": "And that I also have walked contrary unto them, and have brought them into the land of their enemies; if then their uncircumcised hearts be humbled, and they then accept of the punishment of their iniquity:",
      "M": "so that I walked contrary to them and brought them into the land of their enemies — if then their uncircumcised hearts are humbled and they accept the punishment of their iniquity,",
      "T": "and acknowledge that my judgment drove them into exile — if their stubborn, uncircumcised hearts finally humble themselves and they accept the consequences of their sin —"
    },
    "42": {
      "L": "Then will I remember my covenant with Jacob, and also my covenant with Isaac, and also my covenant with Abraham will I remember; and I will remember the land.",
      "M": "then I will remember my covenant with Jacob, and I will remember my covenant with Isaac and my covenant with Abraham, and I will remember the land.",
      "T": "then I will remember my covenant — with Jacob, with Isaac, with Abraham — and I will remember the land."
    },
    "43": {
      "L": "The land also shall be left of them, and shall enjoy her sabbaths, while she lieth desolate without them: and they shall accept of the punishment of their iniquity: because, even because they despised my judgments, and because their soul abhorred my statutes.",
      "M": "The land shall be forsaken by them and shall enjoy its sabbaths while it lies desolate without them. They shall make payment for their iniquity, precisely because they rejected my rules and their soul abhorred my statutes.",
      "T": "The land will lie empty, enjoying its sabbath rest — the rest they never gave it. They will pay for their sin. The cause was plain: they despised my rulings and loathed my statutes."
    },
    "44": {
      "L": "And yet for all that, when they be in the land of their enemies, I will not cast them away, neither will I abhor them, to destroy them utterly, and to break my covenant with them: for I am the LORD their God.",
      "M": "Yet for all that, when they are in the land of their enemies, I will not reject them or abhor them so as to destroy them utterly and break my covenant with them, for I am the LORD their God.",
      "T": "And yet — even in exile — I will not reject them or loathe them to the point of annihilation. I will not break my covenant with them. I am the LORD their God."
    },
    "45": {
      "L": "But I will for their sakes remember the covenant of their ancestors, whom I brought forth out of the land of Egypt in the sight of the heathen, that I might be their God: I am the LORD.",
      "M": "But I will remember for their sake the covenant with their forebears, whom I brought out of the land of Egypt in the sight of the nations, that I might be their God: I am the LORD.",
      "T": "For their sake I will remember the covenant I made with their ancestors — whom I brought out of Egypt before the watching nations, to be their God. I am the LORD."
    },
    "46": {
      "L": "These are the statutes and judgments and laws, which the LORD made between him and the children of Israel in mount Sinai by the hand of Moses.",
      "M": "These are the statutes, the rules, and the laws that the LORD established between himself and the Israelites on Mount Sinai through Moses.",
      "T": "These are the statutes, the rulings, and the laws the LORD established with Israel at Mount Sinai through Moses."
    }
  },
  "27": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and say unto them, When a man shall make a singular vow, the persons shall be for the LORD by thy estimation.",
      "M": "Speak to the Israelites and say to them: When a man makes a special vow to the LORD involving the valuation of a person,",
      "T": "Tell Israel: when a man makes a special vow — dedicating a person to the LORD — the following valuations apply:"
    },
    "3": {
      "L": "And thy estimation shall be of the male from twenty years old even unto sixty years old, even thy estimation shall be fifty shekels of silver, after the shekel of the sanctuary.",
      "M": "the valuation for a male from twenty to sixty years of age shall be fifty shekels of silver according to the sanctuary shekel.",
      "T": "A male between twenty and sixty years of age: fifty shekels of silver by the sanctuary standard."
    },
    "4": {
      "L": "And if it be a female, then thy estimation shall be thirty shekels.",
      "M": "For a female the valuation shall be thirty shekels.",
      "T": "A female of the same age range: thirty shekels."
    },
    "5": {
      "L": "And if it be from five years old even unto twenty years old, then thy estimation shall be of the male twenty shekels, and for the female ten shekels.",
      "M": "From five to twenty years of age: for a male, twenty shekels; for a female, ten shekels.",
      "T": "Ages five to twenty — male: twenty shekels. Female: ten shekels."
    },
    "6": {
      "L": "And if it be from a month old even unto five years old, then thy estimation shall be of the male five shekels of silver, and for the female thy estimation shall be three shekels of silver.",
      "M": "From one month to five years old: for a male, five shekels of silver; for a female, three shekels of silver.",
      "T": "One month to five years — male: five shekels. Female: three shekels."
    },
    "7": {
      "L": "And if it be from sixty years old and above; if it be a male, then thy estimation shall be fifteen shekels, and for the female ten shekels.",
      "M": "Sixty years of age and above: for a male, fifteen shekels; for a female, ten shekels.",
      "T": "Sixty years and above — male: fifteen shekels. Female: ten shekels."
    },
    "8": {
      "L": "But if he be poorer than thy estimation, then he shall present himself before the priest, and the priest shall value him; according to his ability that vowed shall the priest value him.",
      "M": "But if the person who makes the vow is too poor to pay the standard valuation, he shall be presented before the priest, and the priest shall assess him according to what he who made the vow can afford.",
      "T": "If the person who made the vow cannot afford the standard amount, he comes before the priest, who sets a valuation he can actually pay."
    },
    "9": {
      "L": "And if it be a beast, whereof men bring an offering unto the LORD, all that any man giveth of such unto the LORD shall be holy.",
      "M": "If the vow involves an animal from among those that may be offered to the LORD, whatever is given to the LORD shall be holy.",
      "T": "If the vow is of a clean animal that could be offered to the LORD, every such animal given becomes holy."
    },
    "10": {
      "L": "He shall not alter it, nor change it, a good for a bad, or a bad for a good: and if he shall at all change beast for beast, then it and the exchange thereof shall be holy.",
      "M": "He shall not exchange it or substitute another for it, good for bad or bad for good. And if he does make an exchange, animal for animal, then both it and its substitute shall be holy.",
      "T": "He must not swap it — not a good animal for a bad one, not a bad for a good. If he does make a substitution, both the original and the substitute become holy."
    },
    "11": {
      "L": "And if it be any unclean beast, of which they do not offer a sacrifice unto the LORD, then he shall present the beast before the priest:",
      "M": "If the vow involves an unclean animal — one that cannot be offered as a sacrifice to the LORD — then the animal shall be presented before the priest,",
      "T": "If the vow involves an unclean animal that cannot be offered, he brings it before the priest,"
    },
    "12": {
      "L": "And the priest shall value it, whether it be good or bad: as thou valuest it, who art the priest, so shall it be.",
      "M": "and the priest shall assess its value, whether it is good or bad. Whatever the priest values it at, so it shall be.",
      "T": "who assesses its value — good quality or poor. The priest's word is final."
    },
    "13": {
      "L": "But if he will at all redeem it, then he shall add a fifth part thereof unto thy estimation.",
      "M": "But if he wants to redeem it, he shall add a fifth of its value to the assessment.",
      "T": "If the owner wants to buy it back, he must pay the assessed value plus twenty percent."
    },
    "14": {
      "L": "And when a man shall sanctify his house to be holy unto the LORD, then the priest shall estimate it, whether it be good or bad: as the priest shall estimate it, so shall it stand.",
      "M": "When a man dedicates his house as something holy to the LORD, the priest shall assess its value, whether good or bad. As the priest values it, so it shall stand.",
      "T": "If a man dedicates his house to the LORD as a holy thing, the priest assesses it — high quality or low. The priest's valuation stands."
    },
    "15": {
      "L": "And if he that sanctified it will redeem his house, then he shall add the fifth part of the money of thy estimation unto it, and it shall be his.",
      "M": "And if the man who dedicated it wants to redeem his house, he shall add a fifth to the assessed price, and it shall be his.",
      "T": "If he wants to buy it back, he pays the assessed value plus twenty percent — and the house returns to him."
    },
    "16": {
      "L": "And if a man shall sanctify unto the LORD some part of a field of his possession, then thy estimation shall be according to the seed thereof: an homer of barley seed shall be valued at fifty shekels of silver.",
      "M": "If a man dedicates to the LORD part of his inherited field, its valuation shall be set according to the amount of seed required for it: fifty shekels of silver per homer of barley seed.",
      "T": "If a man dedicates part of his family's farmland to the LORD, the valuation is based on how much seed it takes to sow it — fifty shekels of silver per homer of barley seed."
    },
    "17": {
      "L": "If he sanctify his field from the year of jubilee, according to thy estimation it shall stand.",
      "M": "If he dedicates his field from the year of jubilee, it shall stand at the full assessed value.",
      "T": "If he dedicates it right after the Jubilee, the full valuation applies."
    },
    "18": {
      "L": "But if he sanctify his field after the jubilee, then the priest shall reckon unto him the money according to the years that remain, even unto the year of the jubilee, and it shall be abated from thy estimation.",
      "M": "But if he dedicates his field after the jubilee, the priest shall calculate the price according to the years remaining until the next jubilee, and a reduction shall be made from the standard valuation.",
      "T": "If he dedicates it later in the jubilee cycle, the priest calculates the years remaining to the Jubilee and reduces the valuation accordingly."
    },
    "19": {
      "L": "And if he that sanctified the field will in any wise redeem it, then he shall add the fifth part of the money of thy estimation unto it, and it shall be assured to him.",
      "M": "If the man who dedicated the field wants to redeem it, he shall add a fifth of the assessed value to it, and it shall be confirmed to him.",
      "T": "If he wants to redeem the dedicated field, he pays the assessed value plus twenty percent — and the field is securely his again."
    },
    "20": {
      "L": "And if he will not redeem the field, or if he have sold the field to another man, it shall not be redeemed any more.",
      "M": "But if he does not redeem the field, or if he has sold the field to another man, it may no longer be redeemed.",
      "T": "If he does not redeem it — or if he has already sold it to someone else — the option to redeem is gone."
    },
    "21": {
      "L": "But the field, when it goeth out in the jubilee, shall be holy unto the LORD, as a field devoted; the possession thereof shall be the priest's.",
      "M": "When the field is released in the jubilee, it shall be holy to the LORD as a field that has been devoted; it shall belong to the priest.",
      "T": "When the Jubilee comes, that field becomes permanently holy to the LORD — like land placed under the ban. It becomes priestly property."
    },
    "22": {
      "L": "And if a man sanctify unto the LORD a field which he hath bought, which is not of the fields of his possession;",
      "M": "If a man dedicates to the LORD a field that he has purchased — which is not part of his hereditary fields —",
      "T": "If a man dedicates to the LORD a purchased field (not his family's ancestral land),"
    },
    "23": {
      "L": "Then the priest shall reckon unto him the worth of thy estimation, even unto the year of the jubilee: and he shall give thine estimation in that day, as a holy thing unto the LORD.",
      "M": "then the priest shall calculate the assessed value up to the year of jubilee, and he shall pay the assessed amount on that day as a holy gift to the LORD.",
      "T": "the priest calculates its value based on the years remaining to the Jubilee, and the man pays that amount to the LORD as a holy offering on the spot."
    },
    "24": {
      "L": "In the year of the jubilee the field shall return unto him of whom it was bought, even to him to whom the possession of the land did belong.",
      "M": "In the year of jubilee the field shall return to the one from whom he bought it — to the one to whom the land originally belonged.",
      "T": "At the Jubilee the field reverts to the person he bought it from — the original owner of that land."
    },
    "25": {
      "L": "And all thy estimations shall be according to the shekel of the sanctuary: twenty gerahs shall be the shekel.",
      "M": "All your assessments shall be according to the sanctuary shekel: twenty gerahs to the shekel.",
      "T": "All monetary valuations in these laws use the sanctuary standard: twenty gerahs to the shekel."
    },
    "26": {
      "L": "Only the firstling of the beasts, which should be the LORD's firstling, no man shall sanctify it; whether it be ox, or sheep: it is the LORD's.",
      "M": "But no one may dedicate the firstborn of animals, since the firstborn already belongs to the LORD — whether it is an ox or a sheep, it belongs to the LORD.",
      "T": "The firstborn of any animal cannot be dedicated — it already belongs to the LORD. You cannot give what is already his."
    },
    "27": {
      "L": "And if it be of an unclean beast, then he shall redeem it according to thine estimation, and shall add a fifth part of it thereto: or if it be not redeemed, then it shall be sold according to thy estimation.",
      "M": "But if the firstborn is of an unclean animal, he may redeem it at the assessed value plus a fifth; or if it is not redeemed, it shall be sold at the assessed value.",
      "T": "If the firstborn is an unclean animal, it may be redeemed at its assessed value plus twenty percent. If not redeemed, the priest sells it at the assessed price."
    },
    "28": {
      "L": "Notwithstanding no devoted thing, that a man shall devote unto the LORD of all that he hath, both of man and beast, and of the field of his possession, shall be sold or redeemed: every devoted thing is most holy unto the LORD.",
      "M": "But no devoted thing — anything that a man devotes to the LORD from what he has, whether a person, animal, or inherited field — may be sold or redeemed. Every devoted thing is most holy to the LORD.",
      "T": "But the cherem — anything irrevocably devoted to the LORD, whether person, animal, or ancestral land — cannot be sold or bought back. What is placed under the ban is most holy to the LORD."
    },
    "29": {
      "L": "None devoted, which shall be devoted of men, shall be redeemed; but shall surely be put to death.",
      "M": "No person devoted — placed under the ban — may be ransomed; he shall surely be put to death.",
      "T": "A person placed under the ban of destruction cannot be redeemed. He shall be put to death."
    },
    "30": {
      "L": "And all the tithe of the land, whether of the seed of the land, or of the fruit of the tree, is the LORD's: it is holy unto the LORD.",
      "M": "Every tithe of the land — whether of the seed of the land or of the fruit of the trees — belongs to the LORD; it is holy to the LORD.",
      "T": "A tenth of the land's produce — grain or fruit — belongs to the LORD. It is holy."
    },
    "31": {
      "L": "And if a man will at all redeem ought of his tithes, he shall add thereto the fifth part thereof.",
      "M": "If a man wants to redeem any part of his tithe, he shall add a fifth of its value to it.",
      "T": "If someone wants to redeem part of his tithe in cash, he pays its value plus twenty percent."
    },
    "32": {
      "L": "And concerning the tithe of the herd, or of the flock, even of whatsoever passeth under the rod, the tenth shall be holy unto the LORD.",
      "M": "Every tithe of herd or flock — every tenth animal of all that pass under the shepherd's rod — shall be holy to the LORD.",
      "T": "For herd and flock, every tenth animal that passes under the counting rod becomes holy to the LORD."
    },
    "33": {
      "L": "He shall not search whether it be good or bad, neither shall he change it: and if he change it at all, then both it and the change thereof shall be holy; it shall not be redeemed.",
      "M": "He shall not make a distinction between good and bad or make a substitution for it. If he does make a substitution, then both it and the substitute shall be holy; it shall not be redeemed.",
      "T": "The owner must not select which animal — picking only the best or worst. Whatever is tenth belongs to the LORD. If he tries to make a swap, both animals become holy and neither can be redeemed."
    },
    "34": {
      "L": "These are the commandments, which the LORD commanded Moses for the children of Israel in mount Sinai.",
      "M": "These are the commandments that the LORD commanded Moses for the Israelites on Mount Sinai.",
      "T": "These are the commandments the LORD gave to Moses for Israel on Mount Sinai."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'leviticus')
        merge_tier(existing, LEVITICUS, tier_key)
        save(tier_dir, 'leviticus', existing)
    print('Leviticus 25–27 written.')

if __name__ == '__main__':
    main()
