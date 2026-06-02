"""
MKT Leviticus chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-leviticus-19-24.py

Covers: Holiness Code — ethical and ritual laws (ch. 19), penalty laws for violations (ch. 20),
priestly holiness and disqualifications (chs. 21–22), the sacred calendar of appointed times (ch. 23),
tabernacle lampstand and showbread with the blasphemer incident and lex talionis (ch. 24).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — matches prior Leviticus scripts
- H430 (אֱלֹהִים): "God" in all three tiers
- H817 (אָשָׁם): L/M="guilt offering"; T="reparation offering" — matches LEV-2
- H2403 (חַטָּאת): "sin offering" in all three tiers
- H8002 (שֶׁלֶם): L="peace offering", M/T="fellowship offering" — matches LEV-2
- H5930 (עֹלָה): "burnt offering" in all three tiers
- H4503 (מִנְחָה): "grain offering" in all three tiers
- H3722 (כָּפַר): L/M="make atonement"; T="atone / make atonement"
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" in all three tiers
- H6944 (קֹדֶשׁ): "holy" in L/M; "holy/sacred" by context in T
- H5315 (נֶפֶשׁ): "person" in legal/penalty clauses; embodied self elsewhere
- H2931/H2889 (טָמֵא/טָהוֹר): L/M="unclean/clean"; T="impure/pure"
- H4150 (מוֹעֵד) as feast-calendar term: L="feasts/appointed times"; M="appointed festivals"; T="appointed times"
- "I am the LORD" formula (אֲנִי יְהוָה): preserved verbatim in all three tiers throughout ch. 19's
  refrain — the repetition is intentional and must not be varied or omitted
- 19:18 "love your neighbor as yourself": T gives the great commandment explicit cadence without
  altering its force; Jesus cites this as the second great commandment (Matt 22:39)
- 19:34 echoes 19:18 — the love-command extended to the ger (sojourner); T surfaces the echo
- Orlah law (19:23–25): "uncircumcised" fruit (H6189 עָרֵל) preserved in L; T uses "forbidden" —
  the three-year fruit is off-limits like the uncircumcised; fourth year holy, fifth year free
- Ch. 23 Day of Atonement: "afflict your souls" (H6031 עִנָּה) = self-denial/fasting; L preserves
  "afflict"; M="deny yourselves"; T="fast and humble yourselves" — covers the full self-denial regimen
- Feast of Booths (H5521 סֻכּוֹת): "booths" in L/M; T "temporary shelters" or "booths" — the
  memorial character (wilderness wandering) is surfaced in 23:43
- Lex talionis (24:19–20): L/M preserve the exact formula; T notes it establishes proportionality,
  not a command for mandatory literal retaliation
- Pure olive oil (24:2): "beaten" = first-pressing, pre-crush oil — clearest and purest grade
- Showbread (24:5–9): twelve loaves = twelve tribes; "bread of the presence" (לֶחֶם הַפָּנִים)
- Blasphemer (24:10–23): mixed parentage (Israelite mother, Egyptian father) noted; legal ruling
  applies equally to native and foreigner (24:22) — the case generates the universal law
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
  "19": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto all the congregation of the children of Israel, and say unto them, Ye shall be holy: for I the LORD your God am holy.",
      "M": "Speak to the entire congregation of Israel and say to them: You shall be holy, for I the LORD your God am holy.",
      "T": "Address the whole congregation of Israel: Be holy — for I, the LORD your God, am holy."
    },
    "3": {
      "L": "Ye shall fear every man his mother, and his father, and keep my sabbaths: I am the LORD your God.",
      "M": "Every one of you shall revere his mother and his father and keep my sabbaths: I am the LORD your God.",
      "T": "Revere your father and your mother — every one of you. Keep my sabbaths. I am the LORD your God."
    },
    "4": {
      "L": "Turn ye not unto idols, nor make to yourselves molten gods: I am the LORD your God.",
      "M": "Do not turn to idols or make for yourselves cast metal images of gods: I am the LORD your God.",
      "T": "Do not turn toward worthless idols or cast metal images and call them gods. I am the LORD your God."
    },
    "5": {
      "L": "And if ye offer a sacrifice of peace offerings unto the LORD, ye shall offer it at your own will.",
      "M": "When you offer a fellowship sacrifice to the LORD, offer it so that it may be accepted on your behalf.",
      "T": "When you bring a fellowship offering to the LORD, bring it in the right spirit so it will be received."
    },
    "6": {
      "L": "It shall be eaten the same day ye offer it, and on the morrow: and if ought remain until the third day, it shall be burnt in the fire.",
      "M": "It shall be eaten on the day you offer it, or on the next day. But whatever remains until the third day must be burned up with fire.",
      "T": "Eat the fellowship sacrifice the day you offer it, or the next — nothing beyond. Whatever reaches the third day goes into the fire."
    },
    "7": {
      "L": "And if it be eaten at all on the third day, it is abominable; it shall not be accepted.",
      "M": "If any of it is eaten on the third day, it is tainted and will not be accepted.",
      "T": "Eat it on the third day and it becomes offensive — the offering is invalidated, not received."
    },
    "8": {
      "L": "Therefore every one that eateth it shall bear his iniquity, because he hath profaned the hallowed thing of the LORD: and that soul shall be cut off from among his people.",
      "M": "Everyone who eats it shall bear his guilt, because he has profaned what is holy to the LORD; that person shall be cut off from the people.",
      "T": "Anyone who eats it carries the guilt himself — he has profaned what is consecrated to the LORD. That person is cut off from Israel."
    },
    "9": {
      "L": "And when ye reap the harvest of your land, thou shalt not wholly reap the corners of thy field, neither shalt thou gather the gleanings of thy harvest.",
      "M": "When you reap the harvest of your land, do not reap all the way to the edge of your field, and do not gather the gleanings of your harvest.",
      "T": "When you harvest your fields, do not clear the corners all the way to the edge, and do not pick up what falls behind the harvesters."
    },
    "10": {
      "L": "And thou shalt not glean thy vineyard, neither shalt thou gather every grape of thy vineyard; thou shalt leave them for the poor and stranger: I am the LORD your God.",
      "M": "Do not strip your vineyard bare or gather every fallen grape. Leave them for the poor and for the foreigner: I am the LORD your God.",
      "T": "Do not strip your vineyard clean or pick up every fallen grape. Leave something for the poor and the stranger among you. I am the LORD your God."
    },
    "11": {
      "L": "Ye shall not steal, neither deal falsely, neither lie one to another.",
      "M": "You shall not steal, deal falsely, or lie to one another.",
      "T": "Do not steal. Do not deceive. Do not lie to one another."
    },
    "12": {
      "L": "And ye shall not swear by my name falsely, neither shalt thou profane the name of thy God: I am the LORD.",
      "M": "You shall not swear by my name falsely, and so profane the name of your God: I am the LORD.",
      "T": "Do not invoke my name to back a lie — that profanes the name of your God. I am the LORD."
    },
    "13": {
      "L": "Thou shalt not defraud thy neighbour, neither rob him: the wages of him that is hired shall not abide with thee all night until the morning.",
      "M": "You shall not defraud your neighbor or rob him. The wages of a hired worker shall not remain with you overnight until morning.",
      "T": "Do not cheat your neighbor or rob him. Pay a hired worker his wages the same day — do not hold it back overnight."
    },
    "14": {
      "L": "Thou shalt not curse the deaf, nor put a stumblingblock before the blind, but shalt fear thy God: I am the LORD.",
      "M": "You shall not curse the deaf or put a stumbling block before the blind. You shall fear your God: I am the LORD.",
      "T": "Do not curse the person who cannot hear your insult. Do not place an obstacle before the blind. Fear your God. I am the LORD."
    },
    "15": {
      "L": "Ye shall do no unrighteousness in judgment: thou shalt not respect the person of the poor, nor honour the person of the mighty: but in righteousness shalt thou judge thy neighbour.",
      "M": "You shall not render unjust judgment; you shall not show partiality to the poor or deference to the great — judge your neighbor righteously.",
      "T": "In the courtroom, do not tilt the scales — neither toward the poor out of sympathy nor toward the powerful out of fear. Judge every neighbor by what is right."
    },
    "16": {
      "L": "Thou shalt not go up and down as a talebearer among thy people: neither shalt thou stand against the blood of thy neighbour; I am the LORD.",
      "M": "You shall not go around spreading slander among your people. You shall not take a stand that endangers your neighbor's life: I am the LORD.",
      "T": "Do not spread gossip through the community. Do not stand by while your neighbor's blood is shed. I am the LORD."
    },
    "17": {
      "L": "Thou shalt not hate thy brother in thine heart: thou shalt in any wise rebuke thy neighbour, and not suffer sin upon him.",
      "M": "You shall not hate your brother in your heart. You shall surely rebuke your neighbor, so that you do not bear sin because of him.",
      "T": "Do not carry hatred toward your neighbor hidden in your heart. Speak openly — rebuke him when he sins. Otherwise you share the guilt."
    },
    "18": {
      "L": "Thou shalt not avenge, nor bear any grudge against the children of thy people, but thou shalt love thy neighbour as thyself: I am the LORD.",
      "M": "You shall not take vengeance or bear a grudge against the children of your people, but you shall love your neighbor as yourself: I am the LORD.",
      "T": "Do not take revenge. Do not nurse a grudge against anyone in your community. Love your neighbor as you love yourself. I am the LORD."
    },
    "19": {
      "L": "Ye shall keep my statutes. Thou shalt not let thy cattle gender with a diverse kind: thou shalt not sow thy field with mingled seed: neither shall a garment mingled of linen and woollen come upon thee.",
      "M": "Keep my statutes. You shall not let your animals breed with a different kind. You shall not sow your field with two kinds of seed. You shall not wear a garment woven of two kinds of material.",
      "T": "Keep my statutes: do not crossbreed your livestock, do not plant your field with mixed seeds, and do not wear fabric woven from two different materials."
    },
    "20": {
      "L": "And whosoever lieth carnally with a woman, that is a bondmaid, betrothed to an husband, and not at all redeemed, nor freedom given her; she shall be scourged; they shall not be put to death, because she was not free.",
      "M": "If a man has sexual relations with a female slave who is betrothed to another man but has not been ransomed or given her freedom, there shall be an indemnity; but they shall not be put to death because she had not been freed.",
      "T": "If a man has sexual relations with a female slave who is betrothed but not yet freed, they are not executed — she was not free. But there must be a formal penalty."
    },
    "21": {
      "L": "And he shall bring his trespass offering unto the LORD, unto the door of the tabernacle of the congregation, even a ram for a trespass offering.",
      "M": "He shall bring his guilt offering to the LORD at the entrance of the tent of meeting — a ram as a guilt offering.",
      "T": "The man must bring his reparation offering to the LORD at the tent of meeting entrance — a ram."
    },
    "22": {
      "L": "And the priest shall make an atonement for him with the ram of the trespass offering before the LORD for his sin which he hath done: and the sin which he hath done shall be forgiven him.",
      "M": "The priest shall make atonement for him with the ram of the guilt offering before the LORD for the sin he committed, and he will be forgiven for it.",
      "T": "The priest makes atonement for him with the reparation ram before the LORD, covering the sin he committed. He is forgiven."
    },
    "23": {
      "L": "And when ye shall come into the land, and shall have planted all manner of trees for food, then ye shall count the fruit thereof as uncircumcised: three years shall it be as uncircumcised unto you: it shall not be eaten of.",
      "M": "When you enter the land and plant any kind of fruit tree, you shall treat its fruit as forbidden: three years it shall be forbidden to you and must not be eaten.",
      "T": "When you enter the land and plant any fruit tree, treat its fruit as off-limits for the first three years — forbidden; do not eat it."
    },
    "24": {
      "L": "But in the fourth year all the fruit thereof shall be holy to praise the LORD withal.",
      "M": "In the fourth year all its fruit shall be holy, an offering of praise to the LORD.",
      "T": "In the fourth year the entire yield is consecrated — a gift of praise to the LORD."
    },
    "25": {
      "L": "And in the fifth year shall ye eat of the fruit thereof, that it may yield unto you the increase thereof: I am the LORD your God.",
      "M": "In the fifth year you may eat its fruit so that it may yield its increase for you: I am the LORD your God.",
      "T": "Only in the fifth year may you eat the fruit freely — and by then the tree will give its full yield. I am the LORD your God."
    },
    "26": {
      "L": "Ye shall not eat any thing with the blood: neither shall ye use enchantment, nor observe times.",
      "M": "You shall not eat anything with the blood. You shall not practice divination or look for omens.",
      "T": "Do not eat anything with the blood still in it. Do not practice divination or try to read omens."
    },
    "27": {
      "L": "Ye shall not round the corners of your heads, neither shalt thou mar the corners of thy beard.",
      "M": "You shall not round off the hair on your temples or clip the edges of your beard.",
      "T": "Do not shave the sides of your head or trim the edges of your beard in the manner of the nations."
    },
    "28": {
      "L": "Ye shall not make any cuttings in your flesh for the dead, nor print any marks upon you: I am the LORD.",
      "M": "You shall not make cuts in your flesh for the dead or tattoo marks on yourselves: I am the LORD.",
      "T": "Do not gash your flesh in mourning rites for the dead. Do not mark your body with tattoos. I am the LORD."
    },
    "29": {
      "L": "Do not prostitute thy daughter, to cause her to be a whore; lest the land fall to whoredom, and the land become full of wickedness.",
      "M": "Do not dishonor your daughter by making her a prostitute, or the land will fall into prostitution and become filled with depravity.",
      "T": "Do not exploit your daughter by forcing her into prostitution — it debases her and corrupts the whole land."
    },
    "30": {
      "L": "Ye shall keep my sabbaths, and reverence my sanctuary: I am the LORD.",
      "M": "You shall keep my sabbaths and revere my sanctuary: I am the LORD.",
      "T": "Keep my sabbaths. Hold my sanctuary in reverence. I am the LORD."
    },
    "31": {
      "L": "Regard not them that have familiar spirits, neither seek after wizards, to be defiled by them: I am the LORD your God.",
      "M": "Do not turn to mediums or spiritists; do not seek them out, making yourselves unclean by them: I am the LORD your God.",
      "T": "Do not consult mediums or spiritists. Do not go looking for them — you would defile yourselves. I am the LORD your God."
    },
    "32": {
      "L": "Thou shalt rise up before the hoary head, and honour the face of the old man, and fear thy God: I am the LORD.",
      "M": "You shall stand up before the elderly and honor the face of an old person, and you shall fear your God: I am the LORD.",
      "T": "Rise when an elderly person enters the room. Honor the aged. In doing so you honor your God. I am the LORD."
    },
    "33": {
      "L": "And if a stranger sojourn with thee in your land, ye shall not vex him.",
      "M": "When a foreigner sojourns with you in your land, you shall not oppress him.",
      "T": "When a foreigner lives among you in your land, do not oppress him."
    },
    "34": {
      "L": "But the stranger that dwelleth with you shall be unto you as one born among you, and thou shalt love him as thyself; for ye were strangers in the land of Egypt: I am the LORD your God.",
      "M": "The foreigner who lives with you shall be to you as a native-born among you. You shall love him as yourself, for you were foreigners in the land of Egypt: I am the LORD your God.",
      "T": "Treat the foreigner who lives among you as one of your own people — love him as you love yourself. You know what it is to be a stranger: you were foreigners in Egypt. I am the LORD your God."
    },
    "35": {
      "L": "Ye shall do no unrighteousness in judgment, in meteyard, in weight, or in measure.",
      "M": "You shall do no wrong in judgment, in measures of length, weight, or quantity.",
      "T": "Do not cheat in any measurement — not in length, weight, or volume."
    },
    "36": {
      "L": "Just balances, just weights, a just ephah, and a just hin, shall ye have: I am the LORD your God, which brought you out of the land of Egypt.",
      "M": "You shall have honest scales, honest weights, an honest ephah, and an honest hin: I am the LORD your God, who brought you out of the land of Egypt.",
      "T": "Use accurate scales, honest weights, a correct ephah, a correct hin — in every transaction. I am the LORD your God, who brought you out of Egypt."
    },
    "37": {
      "L": "Therefore shall ye observe all my statutes, and all my judgments, and do them: I am the LORD.",
      "M": "You shall keep all my statutes and all my rules and carry them out: I am the LORD.",
      "T": "Keep every statute and carry out every ruling I have given. I am the LORD."
    }
  },
  "20": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Again, thou shalt say to the children of Israel, Whosoever he be of the children of Israel, or of the strangers that sojourn in Israel, that giveth any of his seed unto Molech; he shall surely be put to death: the people of the land shall stone him with stones.",
      "M": "Say to the Israelites: Any person — whether Israelite or foreigner living in Israel — who gives any of his children to Molech shall be put to death; the people of the land shall stone him.",
      "T": "Tell Israel: any person — Israelite or resident foreigner — who sacrifices a child to Molech shall be executed by the community with stones."
    },
    "3": {
      "L": "And I will set my face against that man, and will cut him off from among his people; because he hath given of his seed unto Molech, to defile my sanctuary, and to profane my holy name.",
      "M": "I will set my face against that man and will cut him off from among his people, because he has given his children to Molech, defiling my sanctuary and profaning my holy name.",
      "T": "I myself will turn against that man and cut him off from his people — he has given his child to Molech, defiling my sanctuary and profaning my holy name."
    },
    "4": {
      "L": "And if the people of the land do any ways hide their eyes from the man, when he giveth of his seed unto Molech, and kill him not:",
      "M": "If the people of the land close their eyes to what that man does when he gives his children to Molech and do not put him to death,",
      "T": "If the community deliberately ignores what he is doing — watches him sacrifice his child to Molech and does nothing —"
    },
    "5": {
      "L": "Then I will set my face against that man, and against his family, and will cut him off, and all that go a whoring after him, to commit whoredom with Molech, from among their people.",
      "M": "then I will set my face against that man and his family, and I will cut off from among their people both him and all who follow him in prostituting themselves to Molech.",
      "T": "then I will turn against that man and his whole household — and against all who follow him in this faithless pursuit of Molech. I will cut them all off from Israel."
    },
    "6": {
      "L": "And the soul that turneth after such as have familiar spirits, and after wizards, to go a whoring after them, I will even set my face against that soul, and will cut him off from among his people.",
      "M": "The person who turns to mediums and spiritists, prostituting themselves to them — I will set my face against that person and cut them off from among the people.",
      "T": "Anyone who turns to mediums and spiritists — chasing after them — I will set my face against that person and cut them off from Israel."
    },
    "7": {
      "L": "Sanctify yourselves therefore, and be ye holy: for I am the LORD your God.",
      "M": "Consecrate yourselves therefore, and be holy, for I am the LORD your God.",
      "T": "Therefore consecrate yourselves and be holy — I am the LORD your God."
    },
    "8": {
      "L": "And ye shall keep my statutes, and do them: I am the LORD which sanctify you.",
      "M": "Keep my statutes and do them: I am the LORD who sanctifies you.",
      "T": "Keep my statutes and carry them out. I am the LORD who sets you apart."
    },
    "9": {
      "L": "For every one that curseth his father or his mother shall be surely put to death: he hath cursed his father or his mother; his blood shall be upon him.",
      "M": "Anyone who curses his father or his mother shall be put to death; he has cursed his father or mother, and his blood is on his own head.",
      "T": "Whoever curses his father or his mother shall be put to death. He has cursed his own parents — the blood-guilt is his alone."
    },
    "10": {
      "L": "And the man that committeth adultery with another man's wife, even he that committeth adultery with his neighbour's wife, the adulterer and the adulteress shall surely be put to death.",
      "M": "If a man commits adultery with another man's wife — with the wife of his neighbor — both the adulterer and the adulteress shall be put to death.",
      "T": "A man who commits adultery with another man's wife — both the man and the woman shall be put to death."
    },
    "11": {
      "L": "And the man that lieth with his father's wife hath uncovered his father's nakedness: both of them shall surely be put to death; their blood shall be upon them.",
      "M": "If a man lies with his father's wife, he has uncovered his father's nakedness; both of them shall be put to death, and their blood is upon them.",
      "T": "A man who lies with his father's wife has violated his father's honor — both shall be put to death; the blood-guilt is theirs."
    },
    "12": {
      "L": "And if a man lie with his daughter in law, both of them shall surely be put to death: they have wrought confusion; their blood shall be upon them.",
      "M": "If a man lies with his daughter-in-law, both of them shall be put to death; they have committed perversion; their blood is upon them.",
      "T": "A man who lies with his daughter-in-law — both shall be put to death. They have committed depravity; the blood-guilt is theirs."
    },
    "13": {
      "L": "If a man also lie with mankind, as he lieth with a woman, both of them have committed an abomination: they shall surely be put to death; their blood shall be upon them.",
      "M": "If a man lies with a male as with a woman, both of them have committed an abomination; they shall be put to death, and their blood is upon them.",
      "T": "If a man lies with a man as with a woman, both have committed what the law names an abomination. Both shall be put to death; the blood-guilt is theirs."
    },
    "14": {
      "L": "And if a man take a wife and her mother, it is wickedness: they shall be burnt with fire, both he and they; that there be no wickedness among you.",
      "M": "If a man marries a woman and her mother, it is depravity; both he and they shall be burned with fire, so that there may be no depravity among you.",
      "T": "If a man takes both a woman and her mother as wives, it is wickedness — all three shall be burned. Such depravity must not take root among you."
    },
    "15": {
      "L": "And if a man lie with a beast, he shall surely be put to death: and ye shall slay the beast.",
      "M": "If a man has sexual relations with an animal, he shall be put to death, and you shall kill the animal.",
      "T": "A man who has sexual relations with an animal shall be put to death — and the animal killed as well."
    },
    "16": {
      "L": "And if a woman approach unto any beast, and lie down thereto, thou shalt kill the woman, and the beast: they shall surely be put to death; their blood shall be upon them.",
      "M": "If a woman approaches any animal to lie with it, you shall kill both the woman and the animal; they shall be put to death, and their blood is upon them.",
      "T": "If a woman presents herself to an animal for sexual contact, both the woman and the animal shall be put to death; the blood-guilt is theirs."
    },
    "17": {
      "L": "And if a man shall take his sister, his father's daughter, or his mother's daughter, and see her nakedness, and she see his nakedness; it is a wicked thing; and they shall be cut off in the sight of their people: he hath uncovered his sister's nakedness; he shall bear his iniquity.",
      "M": "If a man takes his sister — his father's daughter or his mother's daughter — and they see each other's nakedness, it is a shameful thing; they shall be cut off in the sight of their people. He has uncovered his sister's nakedness and shall bear his guilt.",
      "T": "If a man has sexual relations with his sister — born of his father or his mother — they are cut off before the community. He has dishonored his sister and must bear his guilt."
    },
    "18": {
      "L": "And if a man shall lie with a woman having her sickness, and shall uncover her nakedness; he hath discovered her fountain, and she hath uncovered the fountain of her blood: and both of them shall be cut off from among their people.",
      "M": "If a man lies with a woman during her menstrual period and uncovers her nakedness, he has exposed her flow and she has uncovered the source of her flow — both of them shall be cut off from among their people.",
      "T": "If a man lies with a woman during her menstrual period, both have exposed what was to remain private — both are cut off from Israel."
    },
    "19": {
      "L": "And thou shalt not uncover the nakedness of thy mother's sister, nor of thy father's sister: for he uncovereth his near kin: they shall bear their iniquity.",
      "M": "You shall not uncover the nakedness of your mother's sister or your father's sister, for that is uncovering one's own kin; they shall bear their guilt.",
      "T": "Do not have sexual relations with your mother's sister or your father's sister — they are close kin. Both parties bear the guilt."
    },
    "20": {
      "L": "And if a man shall lie with his uncle's wife, he hath uncovered his uncle's nakedness: they shall bear their sin; they shall die childless.",
      "M": "If a man lies with his uncle's wife, he has violated his uncle's honor; both shall bear their sin and die childless.",
      "T": "A man who lies with his uncle's wife dishonors his uncle. Both carry the guilt — and they will die childless."
    },
    "21": {
      "L": "And if a man shall take his brother's wife, it is an unclean thing: he hath uncovered his brother's nakedness; they shall be childless.",
      "M": "If a man takes his brother's wife, it is an indecency; he has uncovered his brother's nakedness; they shall be childless.",
      "T": "Taking one's brother's wife is an indecency — he has dishonored his brother. They will be childless."
    },
    "22": {
      "L": "Ye shall therefore keep all my statutes, and all my judgments, and do them: that the land, whither I bring you to dwell therein, spue you not out.",
      "M": "Keep all my statutes and all my rules and carry them out, so that the land where I am bringing you to live does not vomit you out.",
      "T": "Keep every statute and carry out every ruling — or the land I am bringing you into will vomit you out, as it vomited out the nations before you."
    },
    "23": {
      "L": "And ye shall not walk in the manners of the nation, which I cast out before you: for they committed all these things, and therefore I abhorred them.",
      "M": "You shall not walk in the customs of the nation that I am driving out before you, for they did all these things, and I grew to detest them.",
      "T": "Do not live by the practices of the nations I am expelling before you. They did all these things — that is why I have come to detest them."
    },
    "24": {
      "L": "But I have said unto you, Ye shall inherit their land, and I will give it unto you to possess it, a land that floweth with milk and honey: I am the LORD your God, which have separated you from other people.",
      "M": "But I have told you: you will inherit their land, and I will give it to you to possess — a land flowing with milk and honey. I am the LORD your God who has set you apart from all other peoples.",
      "T": "I have told you: their land will be yours — a land flowing with milk and honey. I am the LORD your God who has separated you from all the nations of the earth."
    },
    "25": {
      "L": "Ye shall therefore put difference between clean beasts and unclean, and between unclean fowls and clean: and ye shall not make your souls abominable by beast, or by fowl, or by any manner of living thing that creepeth on the ground, which I have separated from you as unclean.",
      "M": "You shall therefore make a distinction between clean animals and unclean, and between unclean birds and clean. You shall not make yourselves detestable by any animal, bird, or anything that swarms on the ground, which I have set apart from you as unclean.",
      "T": "Keep the distinction I have given you between clean and unclean animals, between clean and unclean birds. Do not make yourselves detestable by eating what I have set apart from you as impure."
    },
    "26": {
      "L": "And ye shall be holy unto me: for I the LORD am holy, and have severed you from other people, that ye should be mine.",
      "M": "You shall be holy to me, for I the LORD am holy and have separated you from the peoples that you should be mine.",
      "T": "Be holy to me — for I the LORD am holy. I have set you apart from all other peoples so that you would be mine."
    },
    "27": {
      "L": "A man also or woman that hath a familiar spirit, or that is a wizard, shall surely be put to death: they shall stone them with stones: their blood shall be upon them.",
      "M": "A man or woman who is a medium or spiritist shall be put to death; they shall be stoned with stones, and their blood is upon them.",
      "T": "Any man or woman who practices as a medium or spiritist shall be put to death by stoning. The blood-guilt is their own."
    }
  },
  "21": {
    "1": {
      "L": "And the LORD said unto Moses, Speak unto the priests the sons of Aaron, and say unto them, There shall none be defiled for the dead among his people:",
      "M": "The LORD said to Moses: Speak to the priests, the sons of Aaron, and say to them: A priest shall not defile himself for a dead person among his people,",
      "T": "The LORD told Moses to speak to the priests — Aaron's sons — with this word: a priest must not make himself ritually impure by contact with the dead among his people,"
    },
    "2": {
      "L": "But for his kin, that is near unto him, that is, for his mother, and for his father, and for his son, and for his daughter, and for his brother,",
      "M": "except for his close relatives: his mother, his father, his son, his daughter, his brother,",
      "T": "except for his nearest blood relatives: mother, father, son, daughter, brother,"
    },
    "3": {
      "L": "And for his sister a virgin, that is nigh unto him, which hath had no husband; for her may he be defiled.",
      "M": "and for his unmarried sister who is close to him because she has no husband — for her he may defile himself.",
      "T": "and for an unmarried sister still in his household — for her he may become impure."
    },
    "4": {
      "L": "But he shall not defile himself, being a chief man among his people, to profane himself.",
      "M": "But as a leader among his people he shall not defile himself in a way that would profane him.",
      "T": "As a man who holds sacred office, he must not defile himself in any way that would dishonor that office."
    },
    "5": {
      "L": "They shall not make baldness upon their head, neither shall they shave off the corner of their beard, nor make any cuttings in their flesh.",
      "M": "Priests shall not shave their heads, clip the edges of their beards, or make cuts in their flesh.",
      "T": "Priests may not shave their heads, trim the edges of their beards, or gash their bodies — the mourning rites of the nations are forbidden to them."
    },
    "6": {
      "L": "They shall be holy unto their God, and not profane the name of their God: for the offerings of the LORD made by fire, and the bread of their God, they do offer: therefore they shall be holy.",
      "M": "They shall be holy to their God and must not profane the name of their God, for they offer the food offerings of the LORD, the bread of their God; therefore they shall be holy.",
      "T": "They are consecrated to their God and must not profane his name — they present the LORD's fire offerings, the food of their God. Therefore they must be holy."
    },
    "7": {
      "L": "They shall not take a wife that is a whore, or profane; neither shall they take a woman put away from her husband: for he is holy unto his God.",
      "M": "They shall not marry a woman who has been a prostitute or one who has been dishonored, nor shall they marry a woman divorced from her husband, for the priest is holy to his God.",
      "T": "A priest may not marry a woman who has been a prostitute or one of degraded status, nor a divorced woman — for the priest is holy to his God."
    },
    "8": {
      "L": "Thou shalt sanctify him therefore; for he offereth the bread of thy God: he shall be holy unto thee: for I the LORD, which sanctify you, am holy.",
      "M": "Regard him as holy, because he presents the bread of your God. He shall be holy to you, for I the LORD, who sanctifies you, am holy.",
      "T": "Honor the priest as holy, for he presents the food of your God. He must be holy to you — I, the LORD who sets you apart, am holy."
    },
    "9": {
      "L": "And the daughter of any priest, if she profane herself by playing the whore, she profaneth her father: she shall be burnt with fire.",
      "M": "If a priest's daughter profanes herself by becoming a prostitute, she profanes her father; she shall be burned with fire.",
      "T": "If a priest's daughter turns to prostitution, she dishonors her father and his sacred office — she shall be burned."
    },
    "10": {
      "L": "And he that is the high priest among his brethren, upon whose head the anointing oil was poured, and that is consecrated to put on the garments, shall not uncover his head, nor rend his clothes;",
      "M": "The high priest — the one among his brothers on whose head the anointing oil has been poured and who has been ordained to wear the priestly garments — shall not let his hair hang loose or tear his clothes.",
      "T": "The high priest — anointed with oil and ordained to wear the sacred vestments — must never dishevel his hair in mourning or tear his garments."
    },
    "11": {
      "L": "Neither shall he go in to any dead body, nor defile himself for his father, or for his mother;",
      "M": "He shall not go near any dead body or defile himself, even for his father or his mother.",
      "T": "He may not come near any dead body — not even for his father, not even for his mother."
    },
    "12": {
      "L": "Neither shall he go out of the sanctuary, nor profane the sanctuary of his God; for the crown of the anointing oil of his God is upon him: I am the LORD.",
      "M": "He shall not leave the sanctuary or profane the sanctuary of his God, for the consecration of the anointing oil of his God is upon him: I am the LORD.",
      "T": "He must not leave the sanctuary or dishonor the sanctuary of his God — the anointing oil marks him as wholly set apart. I am the LORD."
    },
    "13": {
      "L": "And he shall take a wife in her virginity.",
      "M": "He shall take a wife in her virginity.",
      "T": "The high priest must marry a virgin."
    },
    "14": {
      "L": "A widow, or a divorced woman, or profane, or an harlot, these shall he not take: but he shall take a virgin of his own people to wife.",
      "M": "A widow, a divorced woman, a degraded woman, or a prostitute — these he shall not marry. He shall marry a virgin from his own people.",
      "T": "He may not marry a widow, a divorcée, a woman of degraded status, or a prostitute. His wife must be a virgin from among his own people."
    },
    "15": {
      "L": "Neither shall he profane his seed among his people: for I the LORD do sanctify him.",
      "M": "He shall not dishonor his descendants among his people, for I the LORD sanctify him.",
      "T": "He must not compromise the holiness of his descendants among the people — I the LORD am the one who consecrates him."
    },
    "16": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "17": {
      "L": "Speak unto Aaron, saying, Whosoever he be of thy seed in their generations that hath any blemish, let him not approach to offer the bread of his God.",
      "M": "Say to Aaron: No man of your descendants throughout their generations who has a blemish may come near to offer the bread of his God.",
      "T": "Tell Aaron: none of his descendants, in any generation, who has a physical defect may come forward to present the food of his God."
    },
    "18": {
      "L": "For whatsoever man he be that hath a blemish, he shall not approach: a blind man, or a lame, or he that hath a flat nose, or any thing superfluous,",
      "M": "No man who has a blemish shall come near: no one who is blind or lame, no one with a disfigured face or any deformity,",
      "T": "None may come near who has a blemish — whether blind or lame, disfigured in face, or with any malformation,"
    },
    "19": {
      "L": "Or a man that is brokenfooted, or brokenhanded,",
      "M": "no one with a broken foot or a broken hand,",
      "T": "with a broken foot or broken hand,"
    },
    "20": {
      "L": "Or crookbackt, or a dwarf, or that hath a blemish in his eye, or be scurvy, or scabbed, or hath his stones broken:",
      "M": "no one who is hunchbacked or a dwarf, or who has a defect in his eye, a skin disease, scabs, or crushed testicles.",
      "T": "hunchbacked or dwarfed, with diseased eyes, a skin condition, scabs, or damaged reproductive organs."
    },
    "21": {
      "L": "No man that hath a blemish of the seed of Aaron the priest shall come nigh to offer the offerings of the LORD made by fire: he hath a blemish; he shall not come nigh to offer the bread of his God.",
      "M": "No descendant of Aaron the priest who has a blemish shall come near to offer the LORD's food offerings. He has a blemish; he shall not come near to present the bread of his God.",
      "T": "Any descendant of Aaron with such a defect may not come forward to offer the LORD's fire offerings. He has a blemish and may not present the food of his God."
    },
    "22": {
      "L": "He shall eat the bread of his God, both of the most holy, and of the holy.",
      "M": "He may still eat the bread of his God — both the most holy portions and the ordinary holy portions.",
      "T": "He is still a priest and may eat from the holy food — both the most holy portions and the ordinary sacred portions."
    },
    "23": {
      "L": "Only he shall not go in unto the vail, nor come nigh unto the altar, because he hath a blemish; that he profane not my sanctuaries: for I the LORD do sanctify them.",
      "M": "But he shall not go in front of the veil or come near the altar, because he has a blemish, lest he profane my sanctuaries; for I am the LORD who sanctifies them.",
      "T": "But he may not enter behind the veil or approach the altar — his blemish would profane the sacred space. I am the LORD who consecrates these places."
    },
    "24": {
      "L": "And Moses told it unto Aaron, and to his sons, and unto all the children of Israel.",
      "M": "So Moses told this to Aaron and his sons and to all the people of Israel.",
      "T": "Moses conveyed all this to Aaron, to his sons, and to the whole community of Israel."
    }
  },
  "22": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto Aaron and to his sons, that they separate themselves from the holy things of the children of Israel, and that they profane not my holy name in those things which they hallow unto me: I am the LORD.",
      "M": "Speak to Aaron and his sons so that they handle with care the holy offerings of the Israelites and do not profane my holy name in the things they dedicate to me: I am the LORD.",
      "T": "Tell Aaron and his sons: they must handle Israel's holy offerings with the greatest care, or they will profane my holy name. I am the LORD."
    },
    "3": {
      "L": "Say unto them, Whosoever he be of all your seed among your generations, that goeth unto the holy things, which the children of Israel hallow unto the LORD, having his uncleanness upon him, that soul shall be cut off from my presence: I am the LORD.",
      "M": "Say to them: Any person among your descendants throughout your generations who approaches the holy offerings that the Israelites dedicate to the LORD while in a state of uncleanness shall be cut off from my presence: I am the LORD.",
      "T": "Tell them: any of their descendants who approaches Israel's holy offerings while ritually impure shall be cut off from my presence. I am the LORD."
    },
    "4": {
      "L": "What man soever of the seed of Aaron is a leper, or hath a running issue; he shall not eat of the holy things, until he be clean. And whoso toucheth any thing that is unclean by the dead, or a man whose seed goeth from him;",
      "M": "No descendant of Aaron who has a skin disease or a discharge may eat of the holy offerings until he is clean. Anyone who has touched something defiled by a corpse or who has had a seminal emission,",
      "T": "Any of Aaron's descendants who has a skin disease or a bodily discharge may not eat the holy portions until he is clean. Anyone who has touched a corpse-contaminated object or has had a seminal emission,"
    },
    "5": {
      "L": "Or whosoever toucheth any creeping thing, whereby he may be made unclean, or a man of whom he may take uncleanness, whatsoever uncleanness he hath;",
      "M": "or who has touched any swarming thing by which he would be made unclean, or any person by whom he would become unclean — whatever his uncleanness may be —",
      "T": "or who has touched any creature that makes him impure, or any person in a state of impurity — whatever form the impurity takes —"
    },
    "6": {
      "L": "The soul that hath touched any such shall be unclean until even, and shall not eat of the holy things, unless he wash his flesh with water.",
      "M": "the person who has touched any of these shall be unclean until evening and shall not eat of the holy offerings unless he has bathed his body in water.",
      "T": "that person is impure until evening and may not eat from the holy portions unless he has bathed. There are no shortcuts to ritual cleansing."
    },
    "7": {
      "L": "And when the sun is down, he shall be clean, and shall afterward eat of the holy things; because it is his food.",
      "M": "When the sun has set he shall be clean, and afterward he may eat of the holy offerings, for they are his food.",
      "T": "When the sun goes down he is clean — then and only then may he eat the holy food, for it is his appointed provision."
    },
    "8": {
      "L": "That which dieth of itself, or is torn with beasts, he shall not eat to defile himself therewith: I am the LORD.",
      "M": "He shall not eat anything that died naturally or was torn by wild animals, which would make him unclean: I am the LORD.",
      "T": "He must not eat any animal that died on its own or was killed by a wild animal — that would defile him. I am the LORD."
    },
    "9": {
      "L": "They shall therefore keep mine ordinance, lest they bear sin for it, and die therefore, if they profane it: I the LORD do sanctify them.",
      "M": "They shall therefore keep my charge so that they do not bear sin and die through it if they profane it: I the LORD sanctify them.",
      "T": "Let them keep my charge — if they profane it they will bear sin and die for it. I the LORD am the one who sanctifies them."
    },
    "10": {
      "L": "There shall no stranger eat of the holy thing: a sojourner of the priest, or an hired servant, shall not eat of the holy thing.",
      "M": "No layperson shall eat of the holy offering. No guest of the priest or hired worker may eat of the holy offering.",
      "T": "No outsider may eat the holy portions — not even a priest's resident guest or his hired worker."
    },
    "11": {
      "L": "But if the priest buy any soul with his money, he shall eat of it, and he that is born in his house: they shall eat of his meat.",
      "M": "But if a priest buys a slave with his money, that slave may eat of it, and those born in his household may eat of his food.",
      "T": "If a priest purchases a slave, that slave becomes part of the household and may eat the holy food — as may anyone born in the priest's house."
    },
    "12": {
      "L": "If the priest's daughter also be married unto a stranger, she may not eat of an offering of the holy things.",
      "M": "If a priest's daughter marries a layman, she may not eat of the contribution of holy offerings.",
      "T": "If a priest's daughter marries someone outside the priestly line, she loses access to the holy offerings."
    },
    "13": {
      "L": "But if the priest's daughter be a widow, or divorced, and have no child, and is returned unto her father's house, as in her youth, she shall eat of her father's meat: but there shall no stranger eat thereof.",
      "M": "But if the priest's daughter is widowed or divorced, without children, and returns to her father's household as in her youth, she may eat of her father's food. But no layperson shall eat of it.",
      "T": "But if a priest's daughter is widowed or divorced and childless and returns to her father's home, she may once again eat from the holy portions. No layperson may eat them, though."
    },
    "14": {
      "L": "And if a man eat of the holy thing unwittingly, then he shall put the fifth part thereof unto it, and shall give it unto the priest with the holy thing.",
      "M": "If a man eats of a holy offering without being aware of it, he shall add one-fifth of its value to it and give the holy offering to the priest.",
      "T": "If someone accidentally eats a holy portion, he must repay its full value plus a twenty-percent penalty, handing it over to the priest."
    },
    "15": {
      "L": "And they shall not profane the holy things of the children of Israel, which they offer unto the LORD;",
      "M": "The priests shall not allow the holy offerings of the Israelites that they present to the LORD to be profaned,",
      "T": "The priests must ensure that Israel's holy offerings to the LORD are not profaned —"
    },
    "16": {
      "L": "Or suffer them to bear the iniquity of trespass, when they eat their holy things: for I the LORD do sanctify them.",
      "M": "lest they allow people to eat the holy offerings and so bring guilt upon them; for I the LORD sanctify them.",
      "T": "otherwise those who eat improperly will carry guilt. I the LORD am the one who sanctifies these offerings."
    },
    "17": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "18": {
      "L": "Speak unto Aaron, and to his sons, and unto all the children of Israel, and say unto them, Whatsoever he be of the house of Israel, or of the strangers in Israel, that will offer his oblation for all his vows, and for all his freewill offerings, which they will offer unto the LORD for a burnt offering;",
      "M": "Speak to Aaron and his sons and to all the Israelites and say to them: When any person of the house of Israel or any foreigner living in Israel presents an offering to the LORD — whether for any of his vows or any freewill offering offered as a burnt offering —",
      "T": "Tell Aaron and his sons and all Israel: whether an Israelite or a foreigner living among you brings a burnt offering — as a vow or as a freewill gift —"
    },
    "19": {
      "L": "Ye shall offer at your own will a male without blemish, of the beeves, of the sheep, or of the goats.",
      "M": "for it to be accepted on your behalf you shall offer a male without blemish from the cattle, the sheep, or the goats.",
      "T": "it must be a flawless male — from cattle, sheep, or goats — for it to be accepted."
    },
    "20": {
      "L": "But whatsoever hath a blemish, that shall ye not offer: for it shall not be acceptable for you.",
      "M": "You shall not offer anything that has a blemish, for it will not be accepted on your behalf.",
      "T": "Anything with a defect will not be accepted — do not offer it."
    },
    "21": {
      "L": "And whosoever offereth a sacrifice of peace offerings unto the LORD to accomplish his vow, or a freewill offering in beeves or sheep, it shall be perfect to be accepted; there shall be no blemish therein.",
      "M": "When anyone offers a fellowship sacrifice to the LORD — whether to fulfill a vow or as a freewill offering from the herd or flock — it must be unblemished to be accepted; there shall be no defect in it.",
      "T": "Anyone who offers a fellowship sacrifice to the LORD — whether fulfilling a vow or bringing a spontaneous gift from the herd or flock — must bring what is perfect. No blemish is acceptable."
    },
    "22": {
      "L": "Blind, or broken, or maimed, or having a wen, or scurvy, or scabbed, ye shall not offer these unto the LORD, nor make an offering by fire of them upon the altar unto the LORD.",
      "M": "You shall not offer to the LORD animals that are blind, injured, maimed, with a growth, diseased, or scabby. You shall not put any of these on the altar as a food offering to the LORD.",
      "T": "Do not bring to the LORD any animal that is blind, injured, maimed, oozing, diseased, or scabbed. None of these may go on the altar as a fire offering."
    },
    "23": {
      "L": "Either a bullock or a lamb that hath any thing superfluous or lacking in his parts, that mayest thou offer for a freewill offering; but for a vow it shall not be accepted.",
      "M": "An ox or sheep that is overdeveloped or underdeveloped may be offered as a freewill offering, but it will not be accepted to fulfill a vow.",
      "T": "An animal that is overdeveloped or stunted in a limb may be offered as a spontaneous freewill gift — but not to fulfill a vow."
    },
    "24": {
      "L": "Ye shall not offer unto the LORD that which is bruised, or crushed, or broken, or cut; neither shall ye make any offering thereof in your land.",
      "M": "You shall not offer to the LORD an animal whose testicles are bruised, crushed, torn, or cut off; you shall not do this in your land.",
      "T": "Any animal with mutilated, crushed, or surgically altered reproductive organs may not be offered to the LORD anywhere in your land."
    },
    "25": {
      "L": "Neither from a stranger's hand shall ye offer the bread of your God of any of these; because their corruption is in them, and blemishes be in them: they shall not be accepted for you.",
      "M": "Neither shall you accept such animals from a foreigner's hand to present as the food of your God, for their corruption is in them, with their blemishes — they will not be accepted on your behalf.",
      "T": "Do not accept animals with these defects even from a foreigner who wishes to offer — their blemishes disqualify them regardless of who presents them."
    },
    "26": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "27": {
      "L": "When a bullock, or a sheep, or a goat, is brought forth, then it shall be seven days under the dam; and from the eighth day and thenceforth it shall be accepted for an offering made by fire unto the LORD.",
      "M": "When a calf or lamb or goat is born, it shall remain with its mother for seven days. From the eighth day onward it may be accepted as a food offering to the LORD.",
      "T": "A calf, lamb, or kid must stay with its mother for seven days. From the eighth day on it may be offered to the LORD."
    },
    "28": {
      "L": "And whether it be cow or ewe, ye shall not kill it and her young both in one day.",
      "M": "Whether it is a cow or a ewe, you shall not slaughter it and its young on the same day.",
      "T": "Do not slaughter an animal and its offspring on the same day — cow and calf, ewe and lamb."
    },
    "29": {
      "L": "And when ye will offer a sacrifice of thanksgiving unto the LORD, offer it at your own will.",
      "M": "When you offer a sacrifice of thanksgiving to the LORD, offer it so that it may be accepted on your behalf.",
      "T": "When you bring a thanksgiving sacrifice to the LORD, bring it willingly and in the right spirit so it will be received."
    },
    "30": {
      "L": "On the same day it shall be eaten up; ye shall leave none of it until the morrow: I am the LORD.",
      "M": "It shall be eaten on the same day; you shall leave none of it until morning: I am the LORD.",
      "T": "Eat it the same day — nothing left until morning. I am the LORD."
    },
    "31": {
      "L": "Therefore shall ye keep my commandments, and do them: I am the LORD.",
      "M": "You shall keep my commandments and carry them out: I am the LORD.",
      "T": "Keep my commandments and carry them out. I am the LORD."
    },
    "32": {
      "L": "Neither shall ye profane my holy name; but I will be hallowed among the children of Israel: I am the LORD which hallow you,",
      "M": "You shall not profane my holy name, but I will be treated as holy among the Israelites. I am the LORD who sanctifies you,",
      "T": "Do not profane my holy name. I will be treated as holy in the midst of Israel — I am the LORD who sets you apart,"
    },
    "33": {
      "L": "That brought you out of the land of Egypt, to be your God: I am the LORD.",
      "M": "who brought you out of the land of Egypt to be your God: I am the LORD.",
      "T": "who brought you out of Egypt to be your God. I am the LORD."
    }
  },
  "23": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Speak unto the children of Israel, and say unto them, Concerning the feasts of the LORD, which ye shall proclaim to be holy convocations, even these are my feasts.",
      "M": "Speak to the Israelites and say to them: These are the appointed festivals of the LORD that you shall proclaim as sacred assemblies — they are my appointed festivals.",
      "T": "Tell the Israelites: These are the LORD's appointed times, which you shall declare as sacred assemblies. They belong to me."
    },
    "3": {
      "L": "Six days shall work be done: but the seventh day is the sabbath of rest, an holy convocation; ye shall do no work therein: it is the sabbath of the LORD in all your dwellings.",
      "M": "Six days shall work be done, but the seventh day is a sabbath of complete rest, a sacred assembly; you shall do no work. It is a sabbath to the LORD in all your dwelling places.",
      "T": "Work may be done on six days, but the seventh is the Sabbath — a day of complete rest, a sacred assembly. Do no work on it. It is the LORD's Sabbath wherever you live."
    },
    "4": {
      "L": "These are the feasts of the LORD, even holy convocations, which ye shall proclaim in their seasons.",
      "M": "These are the appointed festivals of the LORD, the sacred assemblies that you shall proclaim at their appointed times.",
      "T": "These are the LORD's appointed times — sacred assemblies to be proclaimed at their set seasons."
    },
    "5": {
      "L": "In the fourteenth day of the first month at even is the LORD's passover.",
      "M": "On the fourteenth day of the first month at twilight is the LORD's Passover.",
      "T": "The fourteenth day of the first month at dusk: the LORD's Passover."
    },
    "6": {
      "L": "And on the fifteenth day of the same month is the feast of unleavened bread unto the LORD: seven days ye must eat unleavened bread.",
      "M": "On the fifteenth day of the same month is the Festival of Unleavened Bread to the LORD; for seven days you shall eat unleavened bread.",
      "T": "The fifteenth day of that same month begins the Festival of Unleavened Bread to the LORD — seven days of eating bread without yeast."
    },
    "7": {
      "L": "In the first day ye shall have an holy convocation: ye shall do no servile work therein.",
      "M": "On the first day you shall have a sacred assembly; you shall do no ordinary work.",
      "T": "On the first day there is a sacred assembly — do no regular work."
    },
    "8": {
      "L": "But ye shall offer an offering made by fire unto the LORD seven days: in the seventh day is an holy convocation: ye shall do no servile work therein.",
      "M": "But you shall present food offerings to the LORD for seven days. The seventh day also is a sacred assembly; you shall do no ordinary work.",
      "T": "Present fire offerings to the LORD each of the seven days. On the seventh day, again, a sacred assembly — do no ordinary work."
    },
    "9": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "10": {
      "L": "Speak unto the children of Israel, and say unto them, When ye be come into the land which I give unto you, and shall reap the harvest thereof, then ye shall bring a sheaf of the firstfruits of your harvest unto the priest:",
      "M": "Speak to the Israelites and say to them: When you enter the land that I am giving you and harvest its grain, you shall bring a sheaf of the firstfruits of your harvest to the priest.",
      "T": "Tell Israel: when you enter the land I am giving you and begin harvesting, bring the first sheaf of your harvest to the priest."
    },
    "11": {
      "L": "And he shall wave the sheaf before the LORD, to be accepted for you: on the morrow after the sabbath the priest shall wave it.",
      "M": "He shall wave the sheaf before the LORD so that it will be accepted on your behalf; the priest shall wave it on the day after the Sabbath.",
      "T": "The priest waves it before the LORD so that it is accepted for you. This takes place on the day after the Sabbath."
    },
    "12": {
      "L": "And ye shall offer that day when ye wave the sheaf an he lamb without blemish of the first year for a burnt offering unto the LORD.",
      "M": "On the day you wave the sheaf, you shall also offer a yearling male lamb without blemish as a burnt offering to the LORD.",
      "T": "On the day of the wave offering, also bring a flawless yearling lamb as a burnt offering to the LORD."
    },
    "13": {
      "L": "And the meat offering thereof shall be two tenth deals of fine flour mingled with oil, an offering made by fire unto the LORD for a sweet savour: and the drink offering thereof shall be of wine, the fourth part of an hin.",
      "M": "The accompanying grain offering shall be two-tenths of an ephah of fine flour mixed with oil — a food offering to the LORD of pleasing aroma — along with a drink offering of a quarter of a hin of wine.",
      "T": "Accompanying it: a grain offering of two-tenths of an ephah of fine flour mixed with oil, a fire offering of pleasing aroma to the LORD, and a drink offering of a quarter of a hin of wine."
    },
    "14": {
      "L": "And ye shall eat neither bread, nor parched corn, nor green ears, until the selfsame day that ye have brought an offering unto your God: it shall be a statute for ever throughout your generations in all your dwellings.",
      "M": "You shall eat no bread, parched grain, or fresh grain until this very day, when you have brought the offering of your God: it is a permanent statute throughout your generations in all your dwelling places.",
      "T": "Eat no bread from the new harvest, no roasted grain, no fresh ears — until the day you bring this offering to your God. This is a permanent law in every generation, wherever you live."
    },
    "15": {
      "L": "And ye shall count unto you from the morrow after the sabbath, from the day that ye brought the sheaf of the wave offering; seven sabbaths shall be complete:",
      "M": "From the day after the Sabbath — the day you bring the wave offering sheaf — you shall count seven complete weeks.",
      "T": "Starting from the day after the Sabbath when you presented the wave sheaf, count out seven full weeks —"
    },
    "16": {
      "L": "Even unto the morrow after the seventh sabbath shall ye number fifty days; and ye shall offer a new meat offering unto the LORD.",
      "M": "You shall count fifty days to the day after the seventh Sabbath; then you shall present a new grain offering to the LORD.",
      "T": "fifty days in all, bringing you to the day after the seventh Sabbath. On that fiftieth day, present a new grain offering to the LORD."
    },
    "17": {
      "L": "Ye shall bring out of your habitations two wave loaves of two tenth deals: they shall be of fine flour; they shall be baken with leaven; they are the firstfruits unto the LORD.",
      "M": "From your dwelling places you shall bring two loaves of bread as a wave offering, each of two-tenths of an ephah of fine flour, baked with yeast — firstfruits to the LORD.",
      "T": "Bring two leavened loaves from your homes — each of two-tenths of an ephah of fine flour — as a wave offering to the LORD. These are the firstfruits."
    },
    "18": {
      "L": "And ye shall offer with the bread seven lambs without blemish of the first year, and one young bullock, and two rams: they shall be for a burnt offering unto the LORD, with their meat offering, and their drink offerings, even an offering made by fire, of sweet savour unto the LORD.",
      "M": "With the bread you shall offer seven yearling lambs without blemish, one young bull, and two rams as a burnt offering to the LORD, along with their grain offerings and drink offerings — a food offering of pleasing aroma to the LORD.",
      "T": "Along with the bread, offer seven flawless yearling lambs, one young bull, and two rams — all as burnt offerings to the LORD, with their grain and drink offerings. A pleasing aroma to the LORD."
    },
    "19": {
      "L": "Then ye shall sacrifice one kid of the goats for a sin offering, and two lambs of the first year for a sacrifice of peace offerings.",
      "M": "You shall also offer one male goat as a sin offering and two yearling lambs as a fellowship sacrifice.",
      "T": "Also sacrifice a male goat as a sin offering and two yearling lambs as fellowship offerings."
    },
    "20": {
      "L": "And the priest shall wave them with the bread of the firstfruits for a wave offering before the LORD, with the two lambs: they shall be holy to the LORD for the priest.",
      "M": "The priest shall wave them — the two lambs — along with the bread of the firstfruits as a wave offering before the LORD. They are holy to the LORD and belong to the priest.",
      "T": "The priest waves the two lambs with the firstfruits bread before the LORD. These belong to the LORD — and go to the priest."
    },
    "21": {
      "L": "And ye shall proclaim on the selfsame day, that it may be an holy convocation unto you: ye shall do no servile work therein: it shall be a statute for ever in all your dwellings throughout your generations.",
      "M": "On that same day you shall proclaim a sacred assembly; you shall do no ordinary work. It is a permanent statute in all your dwelling places throughout your generations.",
      "T": "Declare that same day a sacred assembly — do no regular work. This is a permanent statute in every generation, wherever you live."
    },
    "22": {
      "L": "And when ye reap the harvest of your land, thou shalt not make clean riddance of the corners of thy field when thou reapest, neither shalt thou gather any gleaning of thy harvest: thou shalt leave them unto the poor, and to the stranger: I am the LORD your God.",
      "M": "When you reap the harvest of your land, do not reap all the way to the edges of your field or gather the gleanings of your harvest. Leave them for the poor and for the foreigner: I am the LORD your God.",
      "T": "When you harvest your land, do not strip the corners or pick up the gleanings. Leave these for the poor and the foreigner. I am the LORD your God."
    },
    "23": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "24": {
      "L": "Speak unto the children of Israel, saying, In the seventh month, in the first day of the month, shall ye have a sabbath, a memorial of blowing of trumpets, an holy convocation.",
      "M": "Speak to the Israelites: On the first day of the seventh month you shall have a sabbath — a day of solemn rest, commemorated with trumpet blasts, a sacred assembly.",
      "T": "Tell Israel: the first day of the seventh month is a day of solemn rest, marked by trumpet blasts — a sacred assembly."
    },
    "25": {
      "L": "Ye shall do no servile work therein: but ye shall offer an offering made by fire unto the LORD.",
      "M": "You shall do no ordinary work, but you shall present a food offering to the LORD.",
      "T": "Do no regular work — bring a fire offering to the LORD."
    },
    "26": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "27": {
      "L": "Also on the tenth day of this seventh month there shall be a day of atonement: it shall be an holy convocation unto you; and ye shall afflict your souls, and offer an offering made by fire unto the LORD.",
      "M": "On the tenth day of this seventh month is the Day of Atonement. It shall be a sacred assembly for you; you shall deny yourselves and present a food offering to the LORD.",
      "T": "The tenth day of the seventh month is the Day of Atonement — a sacred assembly. Fast and humble yourselves. Bring a fire offering to the LORD."
    },
    "28": {
      "L": "And ye shall do no work in that same day: for it is a day of atonement, to make an atonement for you before the LORD your God.",
      "M": "You shall do no work on that day, for it is the Day of Atonement to make atonement for you before the LORD your God.",
      "T": "Do no work at all on that day — it is the Day of Atonement, when atonement is made for you before the LORD your God."
    },
    "29": {
      "L": "For whatsoever soul it be that shall not be afflicted in that same day, he shall be cut off from among his people.",
      "M": "Anyone who does not deny himself on that day shall be cut off from his people.",
      "T": "Anyone who does not fast and humble himself on that day shall be cut off from the people."
    },
    "30": {
      "L": "And whatsoever soul it be that doeth any work in that same day, the same soul will I destroy from among his people.",
      "M": "And any person who does any work on that day — that person I will destroy from among the people.",
      "T": "Anyone who works on that day — I will destroy that person from among my people."
    },
    "31": {
      "L": "Ye shall do no manner of work: it shall be a statute for ever throughout your generations in all your dwellings.",
      "M": "You shall do no work at all. It is a permanent statute throughout your generations in all your dwelling places.",
      "T": "Do no work of any kind. This is a permanent law in every generation, wherever you live."
    },
    "32": {
      "L": "It shall be unto you a sabbath of rest, and ye shall afflict your souls: in the ninth day of the month at even, from even unto even, shall ye celebrate your sabbath.",
      "M": "It shall be to you a sabbath of solemn rest, and you shall deny yourselves. From the evening of the ninth day of the month to the following evening — from evening to evening — you shall keep your sabbath.",
      "T": "It is a Sabbath of solemn rest — you shall fast. The day begins at sundown on the ninth and runs through the following sundown: evening to evening, you observe the Sabbath."
    },
    "33": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "34": {
      "L": "Speak unto the children of Israel, saying, The fifteenth day of this seventh month shall be the feast of tabernacles for seven days unto the LORD.",
      "M": "Speak to the Israelites: On the fifteenth day of this seventh month is the Festival of Booths, lasting seven days, to the LORD.",
      "T": "Tell Israel: the fifteenth day of the seventh month begins the Festival of Booths — seven days to the LORD."
    },
    "35": {
      "L": "On the first day shall be an holy convocation: ye shall do no servile work therein.",
      "M": "On the first day shall be a sacred assembly; you shall do no ordinary work.",
      "T": "On the first day there is a sacred assembly — do no ordinary work."
    },
    "36": {
      "L": "Seven days ye shall offer an offering made by fire unto the LORD: on the eighth day shall be an holy convocation unto you; and ye shall offer an offering made by fire unto the LORD: it is a solemn assembly; and ye shall do no servile work therein.",
      "M": "For seven days you shall present food offerings to the LORD. The eighth day shall be a sacred assembly for you; you shall present a food offering to the LORD. It is a closing assembly; you shall do no ordinary work.",
      "T": "Present fire offerings to the LORD for seven days. The eighth day is a sacred assembly — bring a fire offering to the LORD. It is a solemn closing assembly; do no ordinary work."
    },
    "37": {
      "L": "These are the feasts of the LORD, which ye shall proclaim to be holy convocations, to offer an offering made by fire unto the LORD, a burnt offering, and a grain offering, a sacrifice, and drink offerings, every thing upon his day:",
      "M": "These are the appointed festivals of the LORD that you shall proclaim as sacred assemblies — to present food offerings to the LORD: burnt offerings, grain offerings, sacrifices, and drink offerings, each on its proper day —",
      "T": "These are the LORD's appointed times, which you are to declare as sacred assemblies. On each one, bring the required offerings — burnt offerings, grain offerings, fellowship sacrifices, and drink offerings — each in its proper season."
    },
    "38": {
      "L": "Beside the sabbaths of the LORD, and beside your gifts, and beside all your vows, and beside all your freewill offerings, which ye give unto the LORD.",
      "M": "These are in addition to the sabbaths of the LORD and in addition to your gifts, all your vows, and all your freewill offerings that you give to the LORD.",
      "T": "These appointed festivals come on top of the regular sabbaths, your personal gifts, vows, and freewill offerings to the LORD."
    },
    "39": {
      "L": "Also in the fifteenth day of the seventh month, when ye have gathered in the fruit of the land, ye shall keep a feast unto the LORD seven days: on the first day shall be a sabbath, and on the eighth day shall be a sabbath.",
      "M": "Also on the fifteenth day of the seventh month, when you have gathered in the produce of the land, you shall celebrate the festival of the LORD for seven days. The first day shall be a day of rest and the eighth day shall be a day of rest.",
      "T": "Once the harvest is gathered in — on the fifteenth of the seventh month — celebrate the LORD's festival for seven days: the first day is a rest-day, the eighth day also a rest-day."
    },
    "40": {
      "L": "And ye shall take you on the first day the boughs of goodly trees, branches of palm trees, and the boughs of thick trees, and willows of the brook; and ye shall rejoice before the LORD your God seven days.",
      "M": "On the first day you shall take the fruit of majestic trees, palm branches, boughs of leafy trees, and willows from the brook, and you shall rejoice before the LORD your God for seven days.",
      "T": "On the first day, take the finest fruit, palm fronds, branches from leafy trees, and willows from the stream — and rejoice before the LORD your God for the full seven days."
    },
    "41": {
      "L": "And ye shall keep it a feast unto the LORD seven days in the year. It shall be a statute for ever in your generations: ye shall celebrate it in the seventh month.",
      "M": "You shall celebrate it as a festival to the LORD for seven days every year. It is a permanent statute throughout your generations; you shall celebrate it in the seventh month.",
      "T": "Keep this festival to the LORD for seven days every year — a permanent law in every generation — always in the seventh month."
    },
    "42": {
      "L": "Ye shall dwell in booths seven days; all that are Israelites born shall dwell in booths:",
      "M": "You shall dwell in booths for seven days. All native Israelites shall dwell in booths,",
      "T": "For seven days live in temporary shelters. Every native Israelite shall live in booths —"
    },
    "43": {
      "L": "That your generations may know that I made the children of Israel to dwell in booths, when I brought them out of the land of Egypt: I am the LORD your God.",
      "M": "so that your generations may know that I made the Israelites dwell in booths when I brought them out of the land of Egypt: I am the LORD your God.",
      "T": "so that every generation remembers: when I brought Israel out of Egypt, they lived in temporary shelters in the wilderness. I am the LORD your God."
    },
    "44": {
      "L": "And Moses declared unto the children of Israel the feasts of the LORD.",
      "M": "So Moses declared to the Israelites the appointed festivals of the LORD.",
      "T": "Moses announced to the Israelites all the LORD's appointed festivals."
    }
  },
  "24": {
    "1": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "2": {
      "L": "Command the children of Israel, that they bring unto thee pure oil olive beaten for the light, to cause the lamps to burn continually.",
      "M": "Command the Israelites to bring you pure oil of pressed olives for the light, to keep a lamp burning continually.",
      "T": "Command Israel to bring you pure beaten olive oil for the light — to keep lamps burning without interruption."
    },
    "3": {
      "L": "Without the vail of the testimony, in the tabernacle of the congregation, shall Aaron order it from the evening unto the morning before the LORD continually: it shall be a statute for ever in your generations.",
      "M": "Outside the curtain of the testimony in the tent of meeting, Aaron shall tend it from evening to morning before the LORD continually. It is a permanent statute throughout your generations.",
      "T": "In the tent of meeting, outside the curtain that screens the ark of the covenant, Aaron must tend the lamps every evening until morning before the LORD — a permanent responsibility in every generation."
    },
    "4": {
      "L": "He shall order the lamps upon the pure candlestick before the LORD continually.",
      "M": "He shall tend the lamps on the pure gold lampstand before the LORD continually.",
      "T": "He must keep the lamps of the pure gold lampstand in order before the LORD at all times."
    },
    "5": {
      "L": "And thou shalt take fine flour, and bake twelve cakes thereof: two tenth deals shall be in one cake.",
      "M": "You shall take fine flour and bake twelve loaves; each loaf shall contain two-tenths of an ephah.",
      "T": "Take fine flour and bake twelve loaves — two-tenths of an ephah each."
    },
    "6": {
      "L": "And thou shalt set them in two rows, six on a row, upon the pure table before the LORD.",
      "M": "You shall set them in two rows, six in a row, on the pure gold table before the LORD.",
      "T": "Arrange them in two rows of six on the pure gold table before the LORD."
    },
    "7": {
      "L": "And thou shalt put pure frankincense upon each row, that it may be on the bread for a memorial, even an offering made by fire unto the LORD.",
      "M": "You shall place pure frankincense on each row as a token offering alongside the bread, a food offering to the LORD.",
      "T": "Place pure frankincense on each row — it stands as a memorial offering to the LORD in place of the bread."
    },
    "8": {
      "L": "Every sabbath he shall set it in order before the LORD continually, being taken from the children of Israel by an everlasting covenant.",
      "M": "Every Sabbath day Aaron shall arrange it before the LORD continually — it is from the Israelites, a covenant forever.",
      "T": "Every Sabbath the bread is renewed before the LORD — a standing covenant offering from Israel, renewed without interruption."
    },
    "9": {
      "L": "And it shall be Aaron's and his sons'; and they shall eat it in the holy place: for it is most holy unto him of the offerings of the LORD made by fire by a perpetual statute.",
      "M": "It shall belong to Aaron and his sons, and they shall eat it in a holy place, for it is most holy to him among the LORD's food offerings — a perpetual due.",
      "T": "The bread belongs to Aaron and his sons, who eat it in the sacred precinct. It is most holy — their standing share from the LORD's offerings, a provision that never lapses."
    },
    "10": {
      "L": "And the son of an Israelite woman, whose father was an Egyptian, went out among the children of Israel: and this son of the Israelite woman and a man of Israel strove together in the camp;",
      "M": "Now the son of an Israelite woman and an Egyptian father went out among the Israelites. In the camp, this son of the Israelite woman got into a fight with an Israelite man.",
      "T": "A man of mixed parentage — his mother an Israelite, his father an Egyptian — went out among the Israelites and got into a fight with an Israelite."
    },
    "11": {
      "L": "And the Israelitish woman's son blasphemed the name of the LORD, and cursed. And they brought him unto Moses: (and his mother's name was Shelomith, the daughter of Dibri, of the tribe of Dan:)",
      "M": "In the fight the Israelite woman's son blasphemed the Name and cursed it. They brought him to Moses. His mother's name was Shelomith, daughter of Dibri, of the tribe of Dan.",
      "T": "During the fight he blasphemed the Name of the LORD and cursed it. He was brought to Moses. His mother was Shelomith, daughter of Dibri, of the tribe of Dan."
    },
    "12": {
      "L": "And they put him in ward, that the mind of the LORD might be shewed them.",
      "M": "They put him in custody until the LORD's will should be made clear to them.",
      "T": "They held him in custody while they waited for the LORD's ruling on what to do."
    },
    "13": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD spoke to Moses:"
    },
    "14": {
      "L": "Bring forth him that hath cursed without the camp; and let all that heard him lay their hands upon his head, and let all the congregation stone him.",
      "M": "Bring out the one who has cursed outside the camp, and let all who heard him lay their hands on his head, and let the whole congregation stone him.",
      "T": "Take the blasphemer outside the camp. Let all who heard him place their hands on his head — then let the whole congregation stone him."
    },
    "15": {
      "L": "And thou shalt speak unto the children of Israel, saying, Whosoever curseth his God shall bear his sin.",
      "M": "Tell the Israelites: Anyone who curses his God shall bear the guilt.",
      "T": "Tell Israel: anyone who curses his God carries the guilt."
    },
    "16": {
      "L": "And he that blasphemeth the name of the LORD, he shall surely be put to death, and all the congregation shall certainly stone him: as well the stranger, as he that is born in the land, when he blasphemeth the name of the LORD, shall be put to death.",
      "M": "Whoever blasphemes the name of the LORD shall be put to death; the entire congregation shall stone him. The foreigner as well as the native-born — when he blasphemes the Name — shall be put to death.",
      "T": "Whoever blasphemes the Name of the LORD shall be put to death — the whole congregation stones him. This applies equally to the foreigner and the native-born Israelite: blaspheme the Name, and die."
    },
    "17": {
      "L": "And he that killeth any man shall surely be put to death.",
      "M": "Anyone who kills a human being shall be put to death.",
      "T": "Anyone who takes a human life shall be put to death."
    },
    "18": {
      "L": "And he that killeth a beast shall make it good; beast for beast.",
      "M": "Anyone who kills an animal shall make restitution for it — life for life.",
      "T": "Anyone who kills another's animal must make restitution — life for life."
    },
    "19": {
      "L": "And if a man cause a blemish in his neighbour; as he hath done, so shall it be done to him;",
      "M": "If anyone injures his neighbor, as he has done it shall be done to him:",
      "T": "If anyone injures a neighbor — the same injury shall be returned to him:"
    },
    "20": {
      "L": "Breach for breach, eye for eye, tooth for tooth: as he hath caused a blemish in a man, so shall it be done to him again.",
      "M": "fracture for fracture, eye for eye, tooth for tooth. As he has injured a person, so shall he be injured.",
      "T": "fracture for fracture, eye for eye, tooth for tooth. Whatever injury he inflicted — the same measure is inflicted on him. The law establishes proportionality, not unlimited vengeance."
    },
    "21": {
      "L": "And he that killeth a beast, he shall restore it: and he that killeth a man, he shall be put to death.",
      "M": "Whoever kills an animal shall make restitution for it, and whoever kills a person shall be put to death.",
      "T": "Kill an animal: pay for it. Kill a person: die for it."
    },
    "22": {
      "L": "Ye shall have one manner of law, as well for the stranger, as for one of your own country: for I am the LORD your God.",
      "M": "You shall have the same law for the foreigner as for the native-born, for I am the LORD your God.",
      "T": "One law applies to everyone — foreigner and native-born alike. I am the LORD your God."
    },
    "23": {
      "L": "And Moses spake to the children of Israel, that they should bring forth him that had cursed out of the camp, and stone him with stones. And the children of Israel did as the LORD commanded Moses.",
      "M": "So Moses spoke to the Israelites, and they brought out of the camp the one who had cursed and stoned him with stones. The Israelites did as the LORD had commanded Moses.",
      "T": "Moses gave the command to Israel. They brought the blasphemer outside the camp and stoned him. Israel did exactly as the LORD had commanded Moses."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'leviticus')
        merge_tier(existing, LEVITICUS, tier_key)
        save(tier_dir, 'leviticus', existing)
    print('Leviticus 19–24 written.')

if __name__ == '__main__':
    main()
