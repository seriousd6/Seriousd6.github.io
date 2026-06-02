"""
MKT Numbers chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-numbers-19-24.py

Covers: the red heifer ordinance for corpse-impurity (ch. 19), Miriam's death/Waters of
Meribah/Aaron's death (ch. 20), bronze serpent/Song of the Well/defeat of Sihon and Og
(ch. 21), Balak summons Balaam (ch. 22), Balaam's first two oracles (ch. 23), Balaam's
third and fourth oracles including the Star oracle (ch. 24).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — consistent with prior Numbers scripts
- H430 (אֱלֹהִים) / H410 (אֵל): "God" in all tiers
- H2403 (חַטָּאת): In ch. 19 rendered "purification offering" (not "sin offering") in all
  tiers — the rite is entirely about removing corpse-defilement, not expiating moral guilt;
  same Hebrew word, different cultic function. Elsewhere in range, no חַטָּאת occurs.
- H5079 (נִדָּה): L="water of separation", M="purification water", T="water that removes
  defilement" — נִדָּה ordinarily denotes menstrual impurity but here describes the
  special category of corpse-uncleanness for which this water is the remedy
- H5315 (נֶפֶשׁ): "person" in L/M; "anyone/person" in T — in ch. 19 this means the
  embodied individual, not an immaterial soul; the KJV "soul" is misleading here
- H8314 (שָׂרָף): "fiery serpents" (L), "venomous snakes" (M), "burning serpents" (T) —
  שָׂרָף means burning/fiery, describing either the bright color or the burning sensation
  of the venom; NT echo in John 3:14 noted in T tier for 21:8-9
- H5178 (נְחֹשֶׁת): "brass" (L), "bronze" (M/T) — bronze is the historically accurate term
- H5251 (נֵס): "pole" all tiers
- H4912 (מָשָׁל): "parable" (L), "oracle" (M/T) — Balaam's speeches are formal prophetic
  discourses, not proverbs; the mashal genre in prophetic usage signals elevated, poetic speech
- H5002 (נְאֻם): "hath said" (L), "says" (M), "the word of" (T) — the prophetic utterance formula
- H7307 (רוּחַ): In 24:2 = "Spirit of God" all tiers, capitalized — this is unambiguously
  divine inspiration coming upon Balaam; no wind or breath reading is possible here
- H7706 (שַׁדַּי): "Almighty" all tiers — ancient divine epithet in the Balaam oracles
- H5945 (עֶלְיוֹן): "Most High" all tiers
- H779 (אָרַר) and H6895 (קָבַב): both rendered "curse"; H6895 is the more active cursing
  (to bore into / actively harm) — T tier occasionally distinguishes
- H1288 (בָּרַךְ): "bless/blessed" all tiers
- H2763 (חֵרֶם/חָרַם): L="utterly destroy", M="completely destroy", T="devote to
  destruction" — the herem; in 21:3 T surfaces the covenantal-vow dimension
- H168+H4150 (אֹהֶל מוֹעֵד): "tent of meeting" all tiers
- H5553 (סֶלַע): "rock" all tiers — the crag at Meribah; Moses's failure was to strike it
  rather than speak to it; T tier surfaces the theological significance of the act
- H4809 (מְרִיבָה): kept as proper noun "Meribah" with gloss; means Strife/Contention
- H860 (אָתוֹן): "donkey" all tiers — the she-ass in the Balaam narrative
- H4397 (מַלְאָךְ): "angel" all tiers; in 22:22ff this is the angel of the LORD as a
  physical blocking presence
- 24:17 note: The Star and Scepter oracle is one of the OT's most contested messianic texts.
  T tier surfaces the eschatological weight without over-determining the referent. The oracle
  is intentionally telescopic — immediate horizon (David), ultimate horizon (the Messiah).
  "Children of Sheth" = all humanity (per the parallelism with Moab), not just Moabites.
- Chapter 19 note: The red heifer ritual is the paradigmatic "statute whose reason is not
  given" (ḥoq) in rabbinic tradition — the priest who performs it becomes impure while
  purifying others. T tier notes this paradox in key verses.
- Chapter 20 note: Moses's sin at Meribah is one of the Pentateuch's deepest theological
  puzzles. The failure may be: (a) striking instead of speaking, (b) the "must WE bring
  water" (taking credit), (c) calling Israel rebels in anger, or (d) all three. T tier
  preserves the ambiguity and the weight of the judgment.
- Balaam narrative note: Balaam is a pagan diviner who receives genuine divine speech. The
  irony that his donkey sees the angel before he does is deliberate narrative commentary
  on spiritual perception. T tier preserves this irony.
- Song of the Well (21:17-18) and taunt-song (21:27-30): rendered as poetry in T tier with
  line breaks preserved.
- Balaam's oracles (23:7-10, 18-24, 24:3-9, 15-19): elevated poetic register in T tier
  with colon-line structure where the Hebrew parallelism is clear.
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
  "19": {
    "1": {
      "L": "And the LORD spake unto Moses and unto Aaron, saying,",
      "M": "The LORD spoke to Moses and Aaron, saying,",
      "T": "The LORD gave this charge to Moses and Aaron:"
    },
    "2": {
      "L": "This is the ordinance of the law which the LORD hath commanded, saying: Speak unto the children of Israel, that they bring thee a red heifer without spot, wherein is no blemish, and upon which never came yoke.",
      "M": "This is the statute of the law that the LORD has commanded: Speak to the Israelites and have them bring you a red heifer without defect, one with no blemish on which no yoke has ever been placed.",
      "T": "Here is the law's requirement that the LORD has commanded: Tell the Israelites to bring you a red heifer — unblemished, spotless, never broken to a yoke."
    },
    "3": {
      "L": "And ye shall give her unto Eleazar the priest, that he may bring her forth without the camp, and one shall slay her before his face:",
      "M": "You shall give her to Eleazar the priest, who shall take her outside the camp, where she is to be slaughtered before him.",
      "T": "Give her to Eleazar the priest. She is to be led outside the camp and slaughtered there in his presence."
    },
    "4": {
      "L": "And Eleazar the priest shall take of her blood with his finger, and sprinkle of her blood directly before the tent of meeting seven times:",
      "M": "Eleazar the priest shall take some of her blood with his finger and sprinkle it seven times toward the front of the tent of meeting.",
      "T": "Eleazar takes some of her blood on his finger and sprinkles it seven times toward the tent of meeting."
    },
    "5": {
      "L": "And one shall burn the heifer in his sight; her skin, and her flesh, and her blood, with her dung, shall he burn:",
      "M": "Then the heifer is to be burned in his sight — her hide, her flesh, her blood, and her dung.",
      "T": "The whole animal is burned before him — hide, flesh, blood, and all."
    },
    "6": {
      "L": "And the priest shall take cedar wood, and hyssop, and scarlet, and cast it into the midst of the burning of the heifer.",
      "M": "The priest shall then take cedar wood, hyssop, and scarlet yarn and throw them into the fire where the heifer is burning.",
      "T": "The priest throws cedar wood, hyssop, and scarlet thread into the blaze — the same materials used in other cleansing rites."
    },
    "7": {
      "L": "Then the priest shall wash his clothes, and he shall bathe his flesh in water, and afterward he shall come into the camp; and the priest shall be unclean until the even.",
      "M": "The priest must wash his clothes and bathe himself in water; after that he may return to the camp, but he will be unclean until evening.",
      "T": "The officiating priest must wash his clothes and bathe — only after that may he re-enter the camp, though he remains ritually unclean until sunset. He who purifies others is rendered impure."
    },
    "8": {
      "L": "And he that burneth her shall wash his clothes in water, and bathe his flesh in water, and shall be unclean until the even.",
      "M": "The man who burned the heifer must also wash his clothes and bathe in water; he too will be unclean until evening.",
      "T": "The man who burned her likewise washes his clothes and bathes; he too is unclean until sunset."
    },
    "9": {
      "L": "And a man that is clean shall gather up the ashes of the heifer, and lay them up without the camp in a clean place; and it shall be kept for the congregation of the children of Israel for a water of separation: it is a purification offering.",
      "M": "A man who is clean shall gather up the heifer's ashes and store them outside the camp in a clean place; they are to be held in reserve for the whole Israelite community to be used in the purification water. It is a purification offering.",
      "T": "A ritually clean man gathers the ashes and deposits them outside the camp in a clean place. They are held in reserve — a standing supply of purification water for the whole congregation. This is a purification rite, not an atonement for moral sin but a remedy for the defilement of death."
    },
    "10": {
      "L": "And he that gathereth the ashes of the heifer shall wash his clothes, and be unclean until the even: and it shall be unto the children of Israel, and unto the stranger that sojourneth among them, for a statute for ever.",
      "M": "The one who gathers the ashes must wash his clothes and will be unclean until evening. This is a permanent statute for the Israelites and for any foreigner living among them.",
      "T": "Even the man who gathers the ashes must wash his clothes and remains unclean until sunset. This ordinance stands forever — it applies equally to native Israelites and to resident aliens among them."
    },
    "11": {
      "L": "He that toucheth the dead body of any man shall be unclean seven days.",
      "M": "Anyone who touches a human corpse will be unclean for seven days.",
      "T": "Touch a dead person's body — anyone's — and you are unclean for seven full days."
    },
    "12": {
      "L": "He shall purify himself with it on the third day, and on the seventh day he shall be clean: but if he purify not himself the third day, then the seventh day he shall not be clean.",
      "M": "He is to cleanse himself with the purification water on the third day and on the seventh day, and then he will be clean; but if he fails to cleanse himself on the third day, he will not be clean on the seventh.",
      "T": "He must undergo purification on the third day and again on the seventh — both applications are required. Skip the third-day rite and the seventh day brings no cleansing."
    },
    "13": {
      "L": "Whosoever toucheth the dead body of any man that is dead, and purifieth not himself, defileth the tabernacle of the LORD; and that soul shall be cut off from Israel: because the water of separation was not sprinkled upon him, he shall be unclean; his uncleanness is yet upon him.",
      "M": "Anyone who touches a corpse and does not purify himself defiles the LORD's tabernacle; that person shall be cut off from Israel. Because the purification water was not sprinkled on him, he remains unclean — his uncleanness still clings to him.",
      "T": "Touch a corpse and refuse purification, and you contaminate the LORD's own dwelling. The penalty is expulsion from Israel. The purification water was never applied; the defilement stands. He carries it into every sacred space he enters."
    },
    "14": {
      "L": "This is the law, when a man dieth in a tent: all that come into the tent, and all that is in the tent, shall be unclean seven days.",
      "M": "This is the ruling when someone dies in a tent: all who enter the tent and everything in it will be unclean for seven days.",
      "T": "Here is the ruling for a death inside a dwelling: everyone who enters that tent, and everything inside it, is unclean for seven days."
    },
    "15": {
      "L": "And every open vessel, which hath no covering bound upon it, is unclean.",
      "M": "Every open container with no lid fastened on it will be unclean.",
      "T": "Any container left uncovered — no lid tied down — is contaminated."
    },
    "16": {
      "L": "And whosoever toucheth one that is slain with a sword in the open fields, or a dead body, or a bone of a man, or a grave, shall be unclean seven days.",
      "M": "Anyone who touches in the open field a person killed by a sword, or a corpse, or a human bone, or a grave, will be unclean for seven days.",
      "T": "Out in the open — touch someone killed by the sword, any human corpse, a human bone, even a grave — and you incur seven days of uncleanness."
    },
    "17": {
      "L": "And for an unclean person they shall take of the ashes of the burnt heifer of purification for sin, and running water shall be put thereto in a vessel:",
      "M": "For an unclean person, some of the ashes of the burnt purification offering shall be taken and fresh water added to them in a vessel.",
      "T": "For the unclean person, take some of the heifer's ashes and add fresh spring water to them in a vessel."
    },
    "18": {
      "L": "And a clean person shall take hyssop, and dip it in the water, and sprinkle it upon the tent, and upon all the vessels, and upon the persons that were there, and upon him that touched a bone, or one slain, or one dead, or a grave:",
      "M": "A clean person shall take hyssop, dip it in the water, and sprinkle it on the tent, on all the vessels, on all the people who were there, and on anyone who touched a bone, a person killed in battle, a corpse, or a grave.",
      "T": "A ritually clean person takes a bunch of hyssop, dips it in this water, and sprinkles everything contaminated — the tent itself, all the furnishings, every person who was there, and anyone who touched bone, slain man, corpse, or grave."
    },
    "19": {
      "L": "And the clean person shall sprinkle upon the unclean on the third day, and on the seventh day: and on the seventh day he shall purify himself, and wash his clothes, and bathe himself in water, and shall be clean at even.",
      "M": "The clean person shall sprinkle the unclean person on the third day and on the seventh day; on the seventh day the unclean person shall purify himself, wash his clothes, and bathe in water, and will be clean at evening.",
      "T": "The sprinkling happens twice: third day and seventh day. On the seventh the person undergoing purification washes his clothes, bathes, and is fully clean by sunset."
    },
    "20": {
      "L": "But the man that shall be unclean, and shall not purify himself, that soul shall be cut off from among the congregation, because he hath defiled the sanctuary of the LORD: the water of separation hath not been sprinkled upon him; he is unclean.",
      "M": "But the person who is unclean and does not purify himself shall be cut off from the congregation; he has defiled the LORD's sanctuary. The purification water was not sprinkled on him; he is unclean.",
      "T": "The unclean person who refuses purification is cut off from the assembly. He has defiled the LORD's sanctuary. The cleansing rite was never performed; his defilement remains upon him."
    },
    "21": {
      "L": "And it shall be a perpetual statute unto them, that he that sprinkleth the water of separation shall wash his clothes; and he that toucheth the water of separation shall be unclean until even.",
      "M": "This is a permanent statute: the one who sprinkles the purification water must wash his clothes, and whoever touches the purification water will be unclean until evening.",
      "T": "This statute stands forever: the one who performs the sprinkling must wash his clothes afterward. Even contact with the purification water itself renders a person unclean until sunset — the paradox of a holy remedy that defiles its handler."
    },
    "22": {
      "L": "And whatsoever the unclean person toucheth shall be unclean; and the soul that toucheth it shall be unclean until even.",
      "M": "Whatever the unclean person touches will be unclean, and anyone who touches it will be unclean until evening.",
      "T": "Uncleanness spreads by contact: whatever an unclean person handles becomes unclean; whoever then touches that object is unclean until sunset."
    }
  },
  "20": {
    "1": {
      "L": "Then came the children of Israel, even the whole congregation, into the desert of Zin in the first month: and the people abode in Kadesh; and Miriam died there, and was buried there.",
      "M": "In the first month the whole Israelite community came to the Desert of Zin and settled at Kadesh. There Miriam died and was buried.",
      "T": "In the first month the whole community reached the Desert of Zin and camped at Kadesh. There Miriam died. There she was buried."
    },
    "2": {
      "L": "And there was no water for the congregation: and they gathered themselves together against Moses and against Aaron.",
      "M": "There was no water for the community, and they assembled against Moses and Aaron.",
      "T": "There was no water. The community turned on Moses and Aaron."
    },
    "3": {
      "L": "And the people chode with Moses, and spake, saying, Would God that we had died when our brethren died before the LORD!",
      "M": "The people quarreled with Moses, saying, 'If only we had perished when our brothers died before the LORD!'",
      "T": "'Better to have died alongside our kinsmen!' they railed at Moses. 'We would rather have fallen before the LORD with them!'"
    },
    "4": {
      "L": "And why have ye brought up the congregation of the LORD into this wilderness, that we and our cattle should die there?",
      "M": "'Why did you bring the LORD's congregation into this wilderness for us and our livestock to die here?'",
      "T": "'Why did you drag us — and our animals — into this wasteland to die?'"
    },
    "5": {
      "L": "And wherefore have ye made us to come up out of Egypt, to bring us in unto this evil place? it is no place of seed, or of figs, or of vines, or of pomegranates; neither is there any water to drink.",
      "M": "'Why did you lead us up from Egypt to this wretched place? There is no grain, no figs, no vines, no pomegranates, and no water to drink.'",
      "T": "'This is a place of nothing — no crops, no fruit, not even water. Why did you bring us out of Egypt for this?'"
    },
    "6": {
      "L": "And Moses and Aaron went from the presence of the congregation unto the door of the tent of meeting, and they fell upon their faces: and the glory of the LORD appeared unto them.",
      "M": "Moses and Aaron went from the assembly to the entrance of the tent of meeting and fell facedown, and the glory of the LORD appeared to them.",
      "T": "Moses and Aaron withdrew from the crowd to the entrance of the tent of meeting and fell prostrate. There the glory of the LORD appeared to them."
    },
    "7": {
      "L": "And the LORD spake unto Moses, saying,",
      "M": "The LORD spoke to Moses, saying,",
      "T": "The LORD addressed Moses:"
    },
    "8": {
      "L": "Take the rod, and gather thou the assembly together, thou, and Aaron thy brother, and speak ye unto the rock before their eyes; and it shall give forth his water, and thou shalt bring forth to them water out of the rock: so thou shalt give the congregation and their beasts drink.",
      "M": "'Take the staff, and assemble the community — you and your brother Aaron. Speak to the rock before their eyes, and it will yield its water; you will bring water out of the rock for the community and their livestock to drink.'",
      "T": "'Take your staff. Gather everyone — you and Aaron together. Speak to the rock while they all watch. The rock will give its water, and you will provide drink for the congregation and their animals.'"
    },
    "9": {
      "L": "And Moses took the rod from before the LORD, as he commanded him.",
      "M": "So Moses took the staff from before the LORD, as he had commanded.",
      "T": "Moses took the staff from before the LORD, as he was told."
    },
    "10": {
      "L": "And Moses and Aaron gathered the congregation together before the rock, and he said unto them, Hear now, ye rebels; must we fetch you water out of this rock?",
      "M": "Moses and Aaron gathered the assembly in front of the rock. Moses said to them, 'Listen, you rebels! Must we bring water out of this rock for you?'",
      "T": "'Listen, you rebels!' Moses cried when the assembly had gathered at the rock. 'Are we to pull water out of this rock for you?' — claiming the act as his own, not God's."
    },
    "11": {
      "L": "And Moses lifted up his hand, and with his rod he smote the rock twice: and the water came out abundantly, and the congregation drank, and their beasts also.",
      "M": "Then Moses raised his hand and struck the rock twice with his staff. Water poured out abundantly, and the congregation and their livestock drank.",
      "T": "Moses raised his hand and struck the rock — not once but twice. Water gushed out in abundance. The people drank, and so did their animals. But Moses had spoken when he should have spoken, and struck when he should have spoken."
    },
    "12": {
      "L": "And the LORD said unto Moses and Aaron, Because ye believed me not, to sanctify me in the eyes of the children of Israel, therefore ye shall not bring this congregation into the land which I have given them.",
      "M": "But the LORD said to Moses and Aaron, 'Because you did not trust me enough to uphold my holiness before the Israelites, you will not lead this congregation into the land I am giving them.'",
      "T": "'You did not trust me,' the LORD told Moses and Aaron. 'You did not honor my holiness before Israel's eyes. For that, neither of you will lead this people into the land I am giving them.' The sentence was final."
    },
    "13": {
      "L": "This is the water of Meribah; because the children of Israel strove with the LORD, and he was sanctified in them.",
      "M": "These are the waters of Meribah, where the Israelites quarreled with the LORD and he showed himself holy among them.",
      "T": "These became the waters of Meribah — 'Strife.' Israel quarreled with the LORD here. And here, despite human failure, the LORD vindicated his own holiness."
    },
    "14": {
      "L": "And Moses sent messengers from Kadesh unto the king of Edom, Thus saith thy brother Israel, Thou knowest all the travail that hath befallen us:",
      "M": "Moses sent messengers from Kadesh to the king of Edom: 'Your brother Israel says this: You know all the hardship we have experienced —'",
      "T": "From Kadesh, Moses sent word to Edom's king: 'Your brother Israel has a message for you. You know the suffering we have endured —'"
    },
    "15": {
      "L": "How our fathers went down into Egypt, and we have dwelt in Egypt a long time; and the Egyptians vexed us, and our fathers:",
      "M": "'how our ancestors went down to Egypt, and we lived there a long time. The Egyptians oppressed us and our ancestors,'",
      "T": "'our ancestors went down to Egypt; we lived there for generations. The Egyptians dealt harshly with us and our forebears,'"
    },
    "16": {
      "L": "And when we cried unto the LORD, he heard our voice, and sent an angel, and hath brought us forth out of Egypt: and, behold, we are in Kadesh, a city in the uttermost of thy border:",
      "M": "'but when we cried to the LORD, he heard our voice and sent a messenger who brought us out of Egypt. Now we are at Kadesh, a town on the edge of your territory.'",
      "T": "'We cried to the LORD, and he heard us. He sent his messenger and brought us out of Egypt. We stand now at Kadesh — right on your border.'"
    },
    "17": {
      "L": "Let us pass, I pray thee, through thy country: we will not pass through the fields, or through the vineyards, neither will we drink of the water of the wells: we will go by the king's high way, we will not turn to the right hand nor to the left, until we have passed thy borders.",
      "M": "'Please let us pass through your country. We will not go through fields or vineyards or drink well water; we will travel the King's Highway and not turn aside to the right or left until we have crossed your territory.'",
      "T": "'Give us passage through your land. We will not enter your fields or vineyards; we will not draw from your wells. We ask only for the main road — straight through, without straying, until we have cleared your borders.'"
    },
    "18": {
      "L": "And Edom said unto him, Thou shalt not pass by me, lest I come out against thee with the sword.",
      "M": "But Edom answered, 'You may not pass through. If you try, we will come against you with the sword.'",
      "T": "Edom's answer was blunt: 'You shall not pass. Try it, and we meet you with drawn swords.'"
    },
    "19": {
      "L": "And the children of Israel said unto him, We will go by the high way: and if I and my cattle drink of thy water, then I will pay for it: I will only, without doing any thing else, go through on my feet.",
      "M": "The Israelites replied, 'We will go by the main road, and if we or our livestock drink any of your water, we will pay for it. We are asking only for the right of passage.'",
      "T": "Israel pressed back: 'We will stay on the road. If any of us — person or animal — drinks from your water, we will pay the price. We are asking nothing more than passage.'"
    },
    "20": {
      "L": "And he said, Thou shalt not go through. And Edom came out against him with much people, and with a strong hand.",
      "M": "But Edom said, 'You shall not pass,' and came out against them with a large and powerful army.",
      "T": "Edom remained unmoved: 'You shall not pass.' And Edom marched out with a great force to enforce that refusal."
    },
    "21": {
      "L": "Thus Edom refused to give Israel passage through his border: wherefore Israel turned away from him.",
      "M": "Since Edom refused to let Israel pass through its territory, Israel turned away from them.",
      "T": "Edom shut the door. Israel had to find another way."
    },
    "22": {
      "L": "And the children of Israel, even the whole congregation, journeyed from Kadesh, and came unto mount Hor.",
      "M": "The whole Israelite community set out from Kadesh and came to Mount Hor.",
      "T": "The entire community broke camp from Kadesh and traveled to Mount Hor."
    },
    "23": {
      "L": "And the LORD spake unto Moses and Aaron in mount Hor, by the coast of the land of Edom, saying,",
      "M": "At Mount Hor, at the border of Edom, the LORD said to Moses and Aaron,",
      "T": "At Mount Hor — right on Edom's boundary — the LORD addressed Moses and Aaron:"
    },
    "24": {
      "L": "Aaron shall be gathered unto his people: for he shall not enter into the land which I have given unto the children of Israel, because ye rebelled against my word at the water of Meribah.",
      "M": "'Aaron is about to be gathered to his people. He will not enter the land I am giving the Israelites, because both of you rebelled against my command at the waters of Meribah.'",
      "T": "'Aaron's time has come. He will be gathered to his ancestors and will never set foot in the land I am giving Israel. At Meribah you both defied my word.'"
    },
    "25": {
      "L": "Take Aaron and Eleazar his son, and bring them up unto mount Hor:",
      "M": "'Take Aaron and his son Eleazar and bring them up Mount Hor.'",
      "T": "'Bring Aaron and his son Eleazar up the mountain.'"
    },
    "26": {
      "L": "And strip Aaron of his garments, and put them upon Eleazar his son: and Aaron shall be gathered unto his people, and shall die there.",
      "M": "'Remove Aaron's priestly vestments and put them on his son Eleazar. Aaron will be gathered to his people — he will die there.'",
      "T": "'Take Aaron's vestments from him and place them on Eleazar. Aaron will die on that mountain and be gathered to his ancestors.'"
    },
    "27": {
      "L": "And Moses did as the LORD commanded: and they went up into mount Hor in the sight of all the congregation.",
      "M": "Moses did as the LORD commanded. They climbed Mount Hor in the sight of the whole community.",
      "T": "Moses obeyed. They ascended Mount Hor in full view of the entire community."
    },
    "28": {
      "L": "And Moses stripped Aaron of his garments, and put them upon Eleazar his son; and Aaron died there in the top of the mount: and Moses and Eleazar came down from the mount.",
      "M": "Moses removed Aaron's vestments and put them on his son Eleazar. Aaron died there on the mountaintop, and Moses and Eleazar descended.",
      "T": "There at the summit Moses removed Aaron's priestly robes and placed them on Eleazar. Aaron died at the top of the mountain. Moses and Eleazar came down alone."
    },
    "29": {
      "L": "And when all the congregation saw that Aaron was dead, they mourned for Aaron thirty days, even all the house of Israel.",
      "M": "When the whole community saw that Aaron had died, all the house of Israel mourned for him thirty days.",
      "T": "When the people saw that Aaron was gone, all Israel mourned him for thirty days."
    }
  },
  "21": {
    "1": {
      "L": "And when king Arad the Canaanite, which dwelt in the south, heard tell that Israel came by the way of the spies; then he fought against Israel, and took some of them prisoners.",
      "M": "When the Canaanite king of Arad, who lived in the Negev, heard that Israel was coming along the road to Atharim, he attacked Israel and captured some of them.",
      "T": "The Canaanite king of Arad ruled the Negev. When he heard Israel was approaching along the Atharim route, he struck — and took prisoners."
    },
    "2": {
      "L": "And Israel vowed a vow unto the LORD, and said, If thou wilt indeed deliver this people into my hand, then I will utterly destroy their cities.",
      "M": "Israel made a vow to the LORD: 'If you will deliver this people into our hands, we will completely destroy their cities.'",
      "T": "Israel made a solemn pledge to the LORD: 'Give us victory over them, and we will devote every one of their towns to destruction.'"
    },
    "3": {
      "L": "And the LORD hearkened to the voice of Israel, and delivered up the Canaanites; and they utterly destroyed them and their cities: and he called the name of the place Hormah.",
      "M": "The LORD listened to Israel's plea and gave the Canaanites into their hands. They completely destroyed them and their towns, and the place was named Hormah.",
      "T": "The LORD heard and gave the Canaanites over. Every person, every town — devoted to destruction. The place was called Hormah: Utter Ruin."
    },
    "4": {
      "L": "And they journeyed from mount Hor by the way of the Red sea, to compass the land of Edom: and the soul of the people was much discouraged because of the way.",
      "M": "They traveled from Mount Hor along the road to the Red Sea to go around Edom, but the people grew impatient along the way.",
      "T": "Setting out from Mount Hor by the Red Sea road to bypass Edom, the people's spirit snapped. The long detour broke them."
    },
    "5": {
      "L": "And the people spake against God, and against Moses, Wherefore have ye brought us up out of Egypt to die in the wilderness? for there is no bread, neither is there any water; and our soul loatheth this light bread.",
      "M": "The people spoke against God and against Moses: 'Why have you brought us up out of Egypt to die in the wilderness? There is no bread! There is no water! And we detest this miserable food!'",
      "T": "The people turned against God and Moses: 'Why drag us from Egypt into this wilderness to die? No real food, no water — and we are sick of this worthless bread!'"
    },
    "6": {
      "L": "And the LORD sent fiery serpents among the people, and they bit the people; and much people of Israel died.",
      "M": "Then the LORD sent venomous snakes among them; they bit the people, and many Israelites died.",
      "T": "The LORD sent burning serpents into the camp. They bit the people, and many in Israel died."
    },
    "7": {
      "L": "Therefore the people came to Moses, and said, We have sinned, for we have spoken against the LORD, and against thee; pray unto the LORD, that he take away the serpents from us. And Moses prayed for the people.",
      "M": "The people came to Moses and said, 'We have sinned by speaking against the LORD and against you. Pray that the LORD will take the snakes away.' So Moses prayed for the people.",
      "T": "The people came to Moses: 'We have sinned. We spoke against the LORD and against you — pray for us, that he remove the serpents.' Moses prayed on their behalf."
    },
    "8": {
      "L": "And the LORD said unto Moses, Make thee a fiery serpent, and set it upon a pole: and it shall come to pass, that every one that is bitten, when he looketh upon it, shall live.",
      "M": "The LORD said to Moses, 'Make a venomous snake and mount it on a pole; anyone who is bitten and looks at it will live.'",
      "T": "The LORD gave Moses this remedy: 'Make a bronze snake and lift it on a pole. Let any man who has been bitten look up at it — he will live.' The look of faith, not the ritual object itself, was the cure."
    },
    "9": {
      "L": "And Moses made a serpent of brass, and put it upon a pole, and it came to pass, that if a serpent had bitten any man, when he beheld the serpent of brass, he lived.",
      "M": "So Moses made a bronze snake and mounted it on a pole. When anyone who had been bitten looked at the bronze snake, they lived.",
      "T": "Moses made a serpent of bronze and raised it on the pole. Whenever someone bitten looked at it, they survived — a sign that would one day point beyond itself to a greater lifting up."
    },
    "10": {
      "L": "And the children of Israel set forward, and pitched in Oboth.",
      "M": "The Israelites moved on and camped at Oboth.",
      "T": "Israel pressed on and camped at Oboth."
    },
    "11": {
      "L": "And they journeyed from Oboth, and pitched at Ijeabarim, in the wilderness which is before Moab, toward the sunrising.",
      "M": "Setting out from Oboth, they camped at Iye-abarim in the wilderness east of Moab.",
      "T": "From Oboth they pressed on to Iye-abarim, in the wilderness east of Moab."
    },
    "12": {
      "L": "From thence they removed, and pitched in the valley of Zared.",
      "M": "From there they set out and camped in the valley of Zered.",
      "T": "They moved again and camped in the Wadi Zered."
    },
    "13": {
      "L": "From thence they removed, and pitched on the other side of Arnon, which is in the wilderness that cometh out of the coasts of the Amorites: for Arnon is the border of Moab, between Moab and the Amorites.",
      "M": "Setting out from there, they camped on the other side of the Arnon, which flows through the wilderness from the Amorite border; for the Arnon is the boundary between Moab and the Amorites.",
      "T": "From there they crossed to the far bank of the Arnon, the river that cuts through the desert along the Amorite frontier. The Arnon was Moab's northern border."
    },
    "14": {
      "L": "Wherefore it is said in the book of the wars of the LORD, What he did in the Red sea, and in the brooks of Arnon,",
      "M": "That is why the Book of the Wars of the LORD says: '...Waheb in Suphah and the wadis — the Arnon'",
      "T": "An ancient battle-song in the Book of the Wars of the LORD records it: 'The action at Waheb in Suphah, the wadis of the Arnon —'"
    },
    "15": {
      "L": "And at the stream of the brooks that goeth down to the dwelling of Ar, and lieth upon the border of Moab.",
      "M": "'and the slope of the wadis that leads to the settlement of Ar, resting on the border of Moab.'",
      "T": "'the gorges falling toward Ar, lying along Moab's boundary.' So the ancient song records the boundary."
    },
    "16": {
      "L": "And from thence they went to Beer: that is the well whereof the LORD spake unto Moses, Gather the people together, and I will give them water.",
      "M": "From there they went to Beer, the well where the LORD said to Moses, 'Assemble the people, and I will give them water.'",
      "T": "From there to Beer — the Well. It was here the LORD told Moses: 'Gather the people and I will give them water.'"
    },
    "17": {
      "L": "Then Israel sang this song, Spring up, O well; sing ye unto it:",
      "M": "Then Israel sang this song: 'Spring up, O well — sing to it!'",
      "T": "Then Israel sang:\n'Spring up, O well — sing to it!'"
    },
    "18": {
      "L": "The princes digged the well, the nobles of the people digged it, by the direction of the lawgiver, with their staves. And from the wilderness they went to Mattanah:",
      "M": "'A well dug by princes, sunk by the nobles of the people, with the scepter, with their own staffs.' From the wilderness they went on to Mattanah,",
      "T": "'A well the princes dug,\nthe people's nobles sank it —\nwith the scepter, with their own staffs.'\nFrom the wilderness they journeyed on to Mattanah,"
    },
    "19": {
      "L": "And from Mattanah to Nahaliel: and from Nahaliel to Bamoth:",
      "M": "from Mattanah to Nahaliel, from Nahaliel to Bamoth,",
      "T": "then Nahaliel, then Bamoth,"
    },
    "20": {
      "L": "And from Bamoth in the valley, that is in the country of Moab, to the top of Pisgah, which looketh toward Jeshimon.",
      "M": "and from Bamoth to the valley in Moab, where the peak of Pisgah overlooks the wasteland.",
      "T": "to the valley in Moab below Pisgah's summit, looking out over the desert."
    },
    "21": {
      "L": "And Israel sent messengers unto Sihon king of the Amorites, saying,",
      "M": "Israel sent messengers to Sihon king of the Amorites, saying,",
      "T": "Israel sent an embassy to Sihon, king of the Amorites:"
    },
    "22": {
      "L": "Let me pass through thy land: we will not turn into the fields, or into the vineyards; we will not drink of the waters of the well: but we will go along by the king's high way, until we be past thy borders.",
      "M": "'Let us pass through your land. We will not turn into fields or vineyards or drink well water; we will go along the King's Highway until we have crossed your territory.'",
      "T": "'Grant us passage through your land. We will not touch your fields or vineyards or draw from your wells — only the King's Highway, straight through.'"
    },
    "23": {
      "L": "And Sihon would not suffer Israel to pass through his border: but Sihon gathered all his people together, and went out against Israel into the wilderness: and he came to Jahaz, and fought against Israel.",
      "M": "But Sihon would not let Israel pass. He mustered all his people and marched out into the wilderness against Israel; he came to Jahaz and fought Israel.",
      "T": "Sihon refused. He mobilized his entire force and marched into the wilderness to meet Israel. They clashed at Jahaz."
    },
    "24": {
      "L": "And Israel smote him with the edge of the sword, and possessed his land from Arnon unto Jabbok, even unto the children of Ammon: for the border of the children of Ammon was strong.",
      "M": "Israel defeated him with the sword and took possession of his land from the Arnon to the Jabbok, up to the Ammonite border, which was well fortified.",
      "T": "Israel cut Sihon down and took his entire territory — from the Arnon River to the Jabbok, as far as the Ammonite border, which stopped their advance."
    },
    "25": {
      "L": "And Israel took all these cities: and Israel dwelt in all the cities of the Amorites, in Heshbon, and in all the villages thereof.",
      "M": "Israel captured all these towns and settled in all the Amorite towns, including Heshbon and all its surrounding settlements.",
      "T": "Every Amorite city fell to Israel. They settled Heshbon and all the villages around it."
    },
    "26": {
      "L": "For Heshbon was the city of Sihon the king of the Amorites, who had fought against the former king of Moab, and taken all his land out of his hand, even unto Arnon.",
      "M": "Heshbon was the royal city of Sihon king of the Amorites, who had fought against the previous king of Moab and taken all his land as far as the Arnon.",
      "T": "Heshbon was Sihon's capital. He had seized it — and all Moabite territory north to the Arnon — from Moab's former king."
    },
    "27": {
      "L": "Wherefore they that speak in proverbs say, Come into Heshbon, let the city of Sihon be built and prepared:",
      "M": "That is why the poets say: 'Come to Heshbon! Let it be rebuilt, let the city of Sihon be restored!'",
      "T": "The old war-singers put it this way:\n'Come to Heshbon! Let it be rebuilt!\nLet Sihon's city be restored!'"
    },
    "28": {
      "L": "For there is a fire gone out of Heshbon, a flame from the city of Sihon: it hath consumed Ar of Moab, and the lords of the high places of Arnon.",
      "M": "'For fire came out from Heshbon, a flame from Sihon's city; it devoured Ar of Moab and swallowed the heights of the Arnon.'",
      "T": "'But fire roared out from Heshbon,\nflames from Sihon's own city —\nscorching Ar of Moab,\nconsuming the hilltop lords of the Arnon.'"
    },
    "29": {
      "L": "Woe to thee, Moab! thou art undone, O people of Chemosh: he hath given his sons that escaped, and his daughters, into captivity unto Sihon king of the Amorites.",
      "M": "'Woe to you, Moab! You are ruined, O people of Chemosh! He gave his sons as fugitives and his daughters as captives to Sihon king of the Amorites.'",
      "T": "'Ruin on you, Moab!\nYou are destroyed, people of Chemosh!\nYour god surrendered sons to flight,\ndaughters into captivity —\ninto the hands of Sihon, Amorite king.'"
    },
    "30": {
      "L": "We have shot at them; Heshbon is perished even unto Dibon, and we have laid them waste even unto Nophah, which reacheth unto Medeba.",
      "M": "'But we have struck them down — Heshbon is ruined as far as Dibon; we have laid waste as far as Nophah, which reaches to Medeba.'",
      "T": "'We have shot them down!\nHeshbon in ruins all the way to Dibon,\nlaid waste to Nophah,\nthe destruction reaching Medeba.'"
    },
    "31": {
      "L": "Thus Israel dwelt in the land of the Amorites.",
      "M": "So Israel settled in the land of the Amorites.",
      "T": "And Israel made the Amorites' land its own."
    },
    "32": {
      "L": "And Moses sent to spy out Jaazer, and they took the villages thereof, and drove out the Amorites that were there.",
      "M": "Moses sent scouts to Jazer, and they captured its surrounding settlements and drove out the Amorites who were there.",
      "T": "Moses sent scouts to Jazer. They took the surrounding villages and expelled the Amorites."
    },
    "33": {
      "L": "And they turned and went up by the way of Bashan: and Og the king of Bashan went out against them, he and all his people, to the battle at Edrei.",
      "M": "Then they turned and went up the road to Bashan, and Og king of Bashan came out against them with all his people to fight at Edrei.",
      "T": "They pivoted north toward Bashan. Og — its king — marched out with his entire army to engage them at Edrei."
    },
    "34": {
      "L": "And the LORD said unto Moses, Fear him not: for I have delivered him into thy hand, and all his people, and his land; and thou shalt do to him as thou didst unto Sihon king of the Amorites, which dwelt at Heshbon.",
      "M": "The LORD said to Moses, 'Do not fear him, for I have delivered him into your hand — him, his people, and his land. Do to him what you did to Sihon king of the Amorites who lived at Heshbon.'",
      "T": "'Do not be afraid of him,' the LORD told Moses. 'I am handing him over to you — Og, his army, his entire territory. Deal with him exactly as you dealt with Sihon of Heshbon.'"
    },
    "35": {
      "L": "So they smote him, and his sons, and all his people, until there was none left him alive: and they possessed his land.",
      "M": "So they struck him down along with his sons and his whole army, leaving no survivors, and took possession of his land.",
      "T": "Israel struck Og down — sons, army, every last man. No one was left. They took the land."
    }
  },
  "22": {
    "1": {
      "L": "And the children of Israel set forward, and pitched in the plains of Moab on this side Jordan by Jericho.",
      "M": "The Israelites traveled on and camped in the plains of Moab across the Jordan from Jericho.",
      "T": "Israel moved on and made camp on the plains of Moab, across the Jordan from Jericho."
    },
    "2": {
      "L": "And Balak the son of Zippor saw all that Israel had done to the Amorites.",
      "M": "Balak son of Zippor saw all that Israel had done to the Amorites.",
      "T": "Balak son of Zippor had watched Israel dismantle the Amorites."
    },
    "3": {
      "L": "And Moab was sore afraid of the people, because they were many: and Moab was distressed because of the children of Israel.",
      "M": "Moab was terrified of the people because they were so numerous, and Moab was filled with dread because of the Israelites.",
      "T": "The sheer size of Israel's force filled Moab with dread."
    },
    "4": {
      "L": "And Moab said unto the elders of Midian, Now shall this company lick up all that are round about us, as the ox licketh up the grass of the field. And Balak the son of Zippor was king of the Moabites at that time.",
      "M": "Moab said to the elders of Midian, 'This horde will lick up everything around us the way an ox licks up the grass of the field.' Balak son of Zippor was king of Moab at that time.",
      "T": "Moab's leaders told the Midianite elders: 'This horde will strip us bare like an ox grazing through a field.' Balak son of Zippor was Moab's king then."
    },
    "5": {
      "L": "He sent messengers therefore unto Balaam the son of Beor to Pethor, which is by the river of the land of the children of his people, to call him, saying, Behold, there is a people come out from Egypt: behold, they cover the face of the earth, and they abide over against me:",
      "M": "He sent messengers to Balaam son of Beor at Pethor, near the Euphrates in the land of his people, with this message: 'A people has come out of Egypt; they cover the face of the land and are camped right next to me.'",
      "T": "He dispatched messengers to Balaam son of Beor, a diviner at Pethor by the great river in his homeland: 'A people has come up out of Egypt — they cover the whole face of the land. They are camped at my doorstep.'"
    },
    "6": {
      "L": "Come now therefore, I pray thee, curse me this people; for they are too mighty for me: peradventure I shall prevail, that we may smite them, and that I may drive them out of the land: for I wot that he whom thou blessest is blessed, and he whom thou cursest is cursed.",
      "M": "'Please come and curse these people for me, because they are too powerful for me. Perhaps then I can defeat them and drive them out of the land. For I know that whoever you bless is blessed, and whoever you curse is cursed.'",
      "T": "'Come and curse them for me — they are too strong for me to fight alone. With your curse I might drive them out. I know your power: your blessing holds, and your curse lands.'"
    },
    "7": {
      "L": "And the elders of Moab and the elders of Midian departed with the rewards of divination in their hand; and they came unto Balaam, and spake unto him the words of Balak.",
      "M": "The elders of Moab and Midian left with divination fees in hand, came to Balaam, and delivered Balak's message.",
      "T": "Moab's and Midian's elders set out, carrying Balak's payment for divination. They arrived at Balaam's house and delivered the king's proposal."
    },
    "8": {
      "L": "And he said unto them, Lodge here this night, and I will bring you word again, as the LORD shall speak unto me: and the princes of Moab abode with Balaam.",
      "M": "He said to them, 'Spend the night here, and I will report back to you whatever the LORD tells me.' So the Moabite princes stayed with Balaam.",
      "T": "'Stay the night,' Balaam told them. 'I will bring you the LORD's answer in the morning.' The Moabite princes lodged with him."
    },
    "9": {
      "L": "And God came unto Balaam, and said, What men are these with thee?",
      "M": "God came to Balaam and asked, 'Who are these men with you?'",
      "T": "God came to Balaam that night: 'Who are these men staying with you?'"
    },
    "10": {
      "L": "And Balaam said unto God, Balak the son of Zippor, king of Moab, hath sent unto me, saying,",
      "M": "Balaam told God, 'Balak son of Zippor, king of Moab, sent them with this message:'",
      "T": "'Balak son of Zippor, king of Moab, has sent them,' Balaam answered."
    },
    "11": {
      "L": "Behold, there is a people come out of Egypt, which covereth the face of the earth: come now, curse me them; peradventure I shall be able to overcome them, and drive them out.",
      "M": "'A people has come out of Egypt and covers the face of the land. Come and curse them for me — perhaps I will then be able to fight them and drive them away.'",
      "T": "'He says a people came from Egypt and has covered the whole land. He wants me to curse them so he can fight them and expel them.'"
    },
    "12": {
      "L": "And God said unto Balaam, Thou shalt not go with them; thou shalt not curse the people: for they are blessed.",
      "M": "God said to Balaam, 'Do not go with them. Do not curse the people, because they are blessed.'",
      "T": "'Do not go with them,' God said. 'You will not curse this people — they are blessed.'"
    },
    "13": {
      "L": "And Balaam rose up in the morning, and said unto the princes of Balak, Get you into your land: for the LORD refuseth to give me leave to go with you.",
      "M": "Balaam got up in the morning and said to Balak's princes, 'Go back to your own land; the LORD has refused to let me come with you.'",
      "T": "At daybreak Balaam turned the delegation away: 'Return to your own country. The LORD will not permit me to go with you.'"
    },
    "14": {
      "L": "And the princes of Moab rose up, and they went unto Balak, and said, Balaam refuseth to come with us.",
      "M": "The Moabite princes returned to Balak and said, 'Balaam refused to come with us.'",
      "T": "The delegation went back to Balak: 'Balaam would not come.'"
    },
    "15": {
      "L": "And Balak sent yet again princes, more, and more honourable than they.",
      "M": "Balak sent other princes, more numerous and more distinguished than the first.",
      "T": "Balak sent a second delegation — larger, more prestigious than the first."
    },
    "16": {
      "L": "And they came to Balaam, and said to him, Thus saith Balak the son of Zippor, Let nothing, I pray thee, hinder thee from coming unto me:",
      "M": "They came to Balaam and said, 'This is what Balak son of Zippor says: Please do not let anything keep you from coming to me.'",
      "T": "They delivered Balak's message to Balaam: 'King Balak will not take no for an answer. Nothing must prevent you from coming.'"
    },
    "17": {
      "L": "For I will promote thee unto very great honour, and I will do whatsoever thou sayest unto me: come therefore, I pray thee, curse me this people.",
      "M": "'I will reward you very handsomely and do whatever you say. Please come and curse these people for me.'",
      "T": "'The king will honor you beyond measure — name your terms. Only come and curse this people.'"
    },
    "18": {
      "L": "And Balaam answered and said unto the servants of Balak, If Balak would give me his house full of silver and gold, I cannot go beyond the word of the LORD my God, to do less or more.",
      "M": "But Balaam replied to Balak's servants, 'Even if Balak gave me his palace full of silver and gold, I could not go beyond the command of the LORD my God, to do anything less or more.'",
      "T": "Balaam was unswayed: 'Tell Balak this: even if he handed me a palace full of silver and gold, I cannot step one inch past the word of the LORD my God — not in any direction.'"
    },
    "19": {
      "L": "Now therefore, I pray you, tarry ye also here this night, that I may know what the LORD will say unto me more.",
      "M": "'Nevertheless, stay here tonight as well, and I will find out what more the LORD says to me.'",
      "T": "'But stay another night. I will see if the LORD has anything more to say to me.'"
    },
    "20": {
      "L": "And God came unto Balaam at night, and said unto him, If the men come to call thee, rise up, and go with them; but yet the word which I shall say unto thee, that shalt thou do.",
      "M": "That night God came to Balaam and said, 'Since these men have come to call you, go with them — but do only what I tell you.'",
      "T": "God came to Balaam again in the night: 'If these men are calling you, go with them. But you will say exactly what I command you to say, and nothing else.'"
    },
    "21": {
      "L": "And Balaam rose up in the morning, and saddled his ass, and went with the princes of Moab.",
      "M": "Balaam got up in the morning, saddled his donkey, and went with the Moabite princes.",
      "T": "In the morning Balaam saddled his donkey and set out with the Moabite delegation."
    },
    "22": {
      "L": "And God's anger was kindled because he went: and the angel of the LORD stood in the way for an adversary against him. Now he was riding upon his ass, and his two servants were with him.",
      "M": "But God was angry that he went, and the angel of the LORD stood in the road to oppose him. Balaam was riding his donkey, and his two servants were with him.",
      "T": "But God's anger burned. The angel of the LORD took up a position in the road to block him. Balaam rode his donkey, two servants alongside."
    },
    "23": {
      "L": "And the ass saw the angel of the LORD standing in the way, and his sword drawn in his hand: and the ass turned aside out of the way, and went into the field: and Balaam smote the ass, to turn her into the way.",
      "M": "The donkey saw the angel of the LORD standing in the road with his sword drawn, so she turned off the road and went into a field. Balaam beat her to get her back on the road.",
      "T": "The donkey saw the angel of the LORD standing in the path, sword drawn, and veered off the road into a field. Balaam beat her to force her back. He saw nothing."
    },
    "24": {
      "L": "Then the angel of the LORD stood in a path of the vineyards, a wall being on this side, and a wall on that side.",
      "M": "Then the angel of the LORD moved to a narrow path between two vineyards, with a wall on each side.",
      "T": "The angel moved ahead to a vineyard path, stone walls pressing in on both sides."
    },
    "25": {
      "L": "And when the ass saw the angel of the LORD, she thrust herself unto the wall, and crushed Balaam's foot against the wall: and he smote her again.",
      "M": "When the donkey saw the angel of the LORD, she pressed herself against the wall, crushing Balaam's foot against it, and he beat her again.",
      "T": "The donkey saw the angel again and pressed hard against the wall, crushing Balaam's foot. He beat her again."
    },
    "26": {
      "L": "And the angel of the LORD went further, and stood in a narrow place, where was no way to turn either to the right hand or to the left.",
      "M": "The angel of the LORD moved on ahead and stood in a narrow place where there was no room to turn either right or left.",
      "T": "The angel moved a third time — to a place so narrow there was nowhere to go but forward."
    },
    "27": {
      "L": "And when the ass saw the angel of the LORD, she fell down under Balaam: and Balaam's anger was kindled, and he smote the ass with a staff.",
      "M": "When the donkey saw the angel of the LORD, she lay down under Balaam. He was furious and beat her with his staff.",
      "T": "The donkey simply stopped and lay down beneath him. Balaam's rage boiled over; he struck her with his staff."
    },
    "28": {
      "L": "And the LORD opened the mouth of the ass, and she said unto Balaam, What have I done unto thee, that thou hast smitten me these three times?",
      "M": "Then the LORD opened the donkey's mouth, and she said to Balaam, 'What have I done to you that you have beaten me these three times?'",
      "T": "The LORD gave the donkey a voice: 'What have I done to you,' she asked Balaam, 'that you have beaten me three times?'"
    },
    "29": {
      "L": "And Balaam said unto the ass, Because thou hast mocked me: I would there were a sword in mine hand, for now would I kill thee.",
      "M": "Balaam answered the donkey, 'You have made a fool of me! If only I had a sword in my hand — I would kill you right now!'",
      "T": "'You have humiliated me!' Balaam answered. 'If I had a sword, you would already be dead!' The prophet rages at his donkey, blind to the real threat."
    },
    "30": {
      "L": "And the ass said unto Balaam, Am not I thine ass, upon which thou hast ridden ever since I was thine unto this day? was I ever wont to do so unto thee? And he said, Nay.",
      "M": "The donkey replied, 'Am I not your own donkey, which you have always ridden? Have I ever done this to you before?' 'No,' he admitted.",
      "T": "'I have carried you faithfully since the day you first owned me,' the donkey replied. 'When have I ever done anything like this?' 'Never,' Balaam admitted."
    },
    "31": {
      "L": "Then the LORD opened the eyes of Balaam, and he saw the angel of the LORD standing in the way, and his sword drawn in his hand: and he bowed down his head, and fell flat on his face.",
      "M": "Then the LORD opened Balaam's eyes, and he saw the angel of the LORD standing in the road with his sword drawn. He bowed low and fell facedown.",
      "T": "Only then did the LORD open Balaam's eyes. He saw what the donkey had seen all along: the angel of the LORD blocking the road, sword drawn. Balaam threw himself down on his face."
    },
    "32": {
      "L": "And the angel of the LORD said unto him, Wherefore hast thou smitten thine ass these three times? behold, I went out to withstand thee, because thy way is perverse before me:",
      "M": "The angel of the LORD said to him, 'Why have you beaten your donkey three times? I came here to oppose you, because your path is reckless before me.'",
      "T": "'Why have you beaten your donkey three times?' the angel demanded. 'I came out to block you. The path you are taking is leading you to ruin.'"
    },
    "33": {
      "L": "And the ass saw me, and turned from me these three times: unless she had turned from me, surely now also I had slain thee, and saved her alive.",
      "M": "'The donkey saw me and turned away from me three times. If she had not turned away, I would certainly have killed you by now, though I would have spared her.'",
      "T": "'Your donkey saw me each time and turned aside. Had she not turned away, I would have killed you. I would have let her live.' The irony is complete: the animal was wiser than the prophet."
    },
    "34": {
      "L": "And Balaam said unto the angel of the LORD, I have sinned; for I knew not that thou stoodest in the way against me: now therefore, if it displease thee, I will get me back again.",
      "M": "Balaam said to the angel of the LORD, 'I have sinned. I did not know you were standing in the road to oppose me. If you are displeased, I will go back.'",
      "T": "'I have sinned,' Balaam said. 'I did not see you there. If this displeases you, I will turn around.'"
    },
    "35": {
      "L": "And the angel of the LORD said unto Balaam, Go with the men: but only the word that I shall speak unto thee, that thou shalt speak. So Balaam went with the princes of Balak.",
      "M": "The angel of the LORD told him, 'Go with the men, but speak only what I tell you.' So Balaam went on with Balak's princes.",
      "T": "'Continue with them,' the angel said, 'but your mouth will speak only what I give you.' Balaam went on with the Moabite nobles."
    },
    "36": {
      "L": "And when Balak heard that Balaam was come, he went out to meet him unto a city of Moab, which is in the border of Arnon, which is in the utmost coast of the border.",
      "M": "When Balak heard that Balaam was coming, he went out to meet him at the Moabite city on the Arnon, at the farthest point of the border.",
      "T": "Hearing that Balaam was on his way, Balak rode out to meet him at a frontier city on the Arnon, at the very edge of his territory."
    },
    "37": {
      "L": "And Balak said unto Balaam, Did I not earnestly send unto thee to call thee? wherefore camest thou not unto me? am I not able indeed to promote thee to honour?",
      "M": "Balak said to Balaam, 'Did I not send urgently to call you? Why didn't you come right away? Am I not able to honor you richly?'",
      "T": "'I sent for you twice!' Balak said. 'Why did you not come the first time? Do you think I cannot reward you?'"
    },
    "38": {
      "L": "And Balaam said unto Balak, Lo, I am come unto thee: have I now any power at all to say any thing? the word that God putteth in my mouth, that shall I speak.",
      "M": "Balaam replied, 'Well, I am here now. But understand this: I have no power to say anything on my own. I will speak only what God puts in my mouth.'",
      "T": "'I am here,' Balaam answered, 'but hear me clearly: I have no power to say whatever I please. I will speak whatever God places in my mouth, and only that.'"
    },
    "39": {
      "L": "And Balaam went with Balak, and they came unto Kirjathhuzoth.",
      "M": "Balaam went with Balak to Kiriath-huzoth.",
      "T": "Balaam accompanied Balak to Kiriath-huzoth."
    },
    "40": {
      "L": "And Balak offered oxen and sheep, and sent to Balaam, and to the princes that were with him.",
      "M": "Balak sacrificed cattle and sheep and sent portions to Balaam and the princes who were with him.",
      "T": "Balak offered cattle and sheep, distributing portions to Balaam and the nobles of the delegation."
    },
    "41": {
      "L": "And it came to pass on the morrow, that Balak took Balaam, and brought him up into the high places of Baal, that thence he might see the utmost part of the people.",
      "M": "The next morning Balak took Balaam up to Bamoth-baal, where he could see a portion of the Israelites.",
      "T": "At dawn Balak brought Balaam to the high place of Baal, where he could survey the outer edge of Israel's camp."
    }
  },
  "23": {
    "1": {
      "L": "And Balaam said unto Balak, Build me here seven altars, and prepare me here seven oxen and seven rams.",
      "M": "Balaam said to Balak, 'Build me seven altars here and prepare seven bulls and seven rams.'",
      "T": "Balaam gave Balak his instructions: 'Build seven altars here and bring seven bulls and seven rams.'"
    },
    "2": {
      "L": "And Balak did as Balaam had spoken; and Balak and Balaam offered on every altar a bullock and a ram.",
      "M": "Balak did as Balaam said, and they offered a bull and a ram on each altar.",
      "T": "Balak complied. Together they offered a bull and a ram on each of the seven altars."
    },
    "3": {
      "L": "And Balaam said unto Balak, Stand by thy burnt offering, and I will go: peradventure the LORD will come to meet me: and whatsoever he sheweth me I will tell thee. And he went to an high place.",
      "M": "'Stand here by your burnt offering,' Balaam told Balak, 'while I go off. Perhaps the LORD will come to meet me, and whatever he reveals I will tell you.' And he went to a bare height.",
      "T": "'Stay here by your sacrifice,' Balaam told Balak. 'I will go seek a meeting with the LORD. Whatever he shows me, I will report.' He went alone to a bare hilltop."
    },
    "4": {
      "L": "And God met Balaam: and he said unto him, I have prepared seven altars, and I have offered upon every altar a bullock and a ram.",
      "M": "God met with Balaam, who said, 'I have set up seven altars and offered a bull and a ram on each one.'",
      "T": "God met him there. Balaam reported his ritual: 'I have prepared seven altars — a bull and a ram on each.'"
    },
    "5": {
      "L": "And the LORD put a word in Balaam's mouth, and said, Return unto Balak, and thus thou shalt speak.",
      "M": "The LORD put a word in Balaam's mouth and said, 'Go back to Balak and give him this message.'",
      "T": "The LORD gave Balaam the words and sent him back: 'Return to Balak and speak this.'"
    },
    "6": {
      "L": "And he returned unto him, and, lo, he stood by his burnt sacrifice, he, and all the princes of Moab.",
      "M": "When Balaam returned, Balak was standing by his burnt offering with all the Moabite princes.",
      "T": "Balaam returned to find Balak waiting at the sacrifice, the Moabite nobles arrayed around him."
    },
    "7": {
      "L": "And he took up his parable, and said, Balak the king of Moab hath brought me from Aram, out of the mountains of the east, saying, Come, curse me Jacob, and come, defy Israel:",
      "M": "Balaam delivered his oracle: 'Balak has brought me from Aram, from the mountains of the east — the king of Moab saying, Come, curse Jacob for me; come, denounce Israel.'",
      "T": "Balaam took up his prophetic discourse:\n'Balak king of Moab brought me from Aram,\nfrom the mountains of the east —\n\"Come, curse Jacob for me;\ncome, denounce Israel.\"'"
    },
    "8": {
      "L": "How shall I curse, whom God hath not cursed? or how shall I defy, whom the LORD hath not defied?",
      "M": "'But how can I curse whom God has not cursed? How can I denounce whom the LORD has not denounced?'",
      "T": "'How shall I curse what God has not cursed?\nHow shall I denounce what the LORD has not denounced?'"
    },
    "9": {
      "L": "For from the top of the rocks I see him, and from the hills I behold him: lo, the people shall dwell alone, and shall not be reckoned among the nations.",
      "M": "'From the rocky peaks I see them, from the hills I gaze down: here is a people who live apart and do not count themselves among the nations.'",
      "T": "'From rocky heights I look down,\nfrom the hills I survey them:\nA people that lives apart,\nnot reckoned among the nations —\nsingular, set aside.'"
    },
    "10": {
      "L": "Who can count the dust of Jacob, and the number of the fourth part of Israel? Let me die the death of the righteous, and let my last end be like his!",
      "M": "'Who can count the dust of Jacob or number the multitudes of Israel? May I die the death of the upright, and may my end be like theirs!'",
      "T": "'Who can count the dust of Jacob —\nnumber the myriads of Israel?\nLet me die as the righteous die!\nLet my end be like theirs!'"
    },
    "11": {
      "L": "And Balak said unto Balaam, What hast thou done unto me? I took thee to curse mine enemies, and, behold, thou hast blessed them altogether.",
      "M": "Balak said to Balaam, 'What have you done to me? I brought you to curse my enemies, but you have blessed them outright!'",
      "T": "'What have you done?' Balak demanded. 'I brought you here to curse my enemies, and you have blessed them wholesale!'"
    },
    "12": {
      "L": "And he answered and said, Must I not take heed to speak that which the LORD hath put in my mouth?",
      "M": "Balaam answered, 'Must I not be careful to say exactly what the LORD puts in my mouth?'",
      "T": "'Am I not bound to speak exactly what the LORD places in my mouth?' Balaam replied."
    },
    "13": {
      "L": "And Balak said unto him, Come, I pray thee, with me unto another place, from whence thou mayest see them; thou shalt see but the utmost part of them, and shalt not see them all: and curse me them from thence.",
      "M": "Balak said to him, 'Come with me to another place where you can see them — only the outskirts of the camp, not the whole mass of them — and curse them for me from there.'",
      "T": "'Come to a different vantage point,' Balak urged. 'From there you will see only the edge of their camp, not the full host. Perhaps a different view will allow you to curse them.'"
    },
    "14": {
      "L": "And he brought him into the field of Zophim, to the top of Pisgah, and built seven altars, and offered a bullock and a ram on every altar.",
      "M": "He took him to the field of Zophim on the top of Pisgah and built seven altars, offering a bull and a ram on each.",
      "T": "Balak led him to the lookout field on Pisgah's summit. Again seven altars; again a bull and a ram on each."
    },
    "15": {
      "L": "And he said unto Balak, Stand here by thy burnt offering, while I meet the LORD yonder.",
      "M": "Balaam said to Balak, 'Stand here by your burnt offering while I meet with the LORD over there.'",
      "T": "'Remain here by the sacrifice,' Balaam told Balak. 'I will meet the LORD over there.'"
    },
    "16": {
      "L": "And the LORD met Balaam, and put a word in his mouth, and said, Go again unto Balak, and say thus.",
      "M": "The LORD met with Balaam and put words in his mouth, then said, 'Go back to Balak and say this.'",
      "T": "The LORD met him and placed words in his mouth: 'Return to Balak and say this.'"
    },
    "17": {
      "L": "And when he came to him, behold, he stood by his burnt offering, and the princes of Moab with him. And Balak said unto him, What hath the LORD spoken?",
      "M": "When Balaam came back, Balak was standing by his offering with the Moabite princes. 'What has the LORD said?' Balak asked.",
      "T": "Balak stood at the altar, princes beside him. 'What has the LORD said?' he asked."
    },
    "18": {
      "L": "And he took up his parable, and said, Rise up, Balak, and hear; hearken unto me, thou son of Zippor:",
      "M": "Balaam took up his oracle: 'Arise, Balak, and listen! Hear me, son of Zippor!'",
      "T": "Balaam began his second oracle:\n'Rise up, Balak — listen!\nSon of Zippor, attend to me!'"
    },
    "19": {
      "L": "God is not a man, that he should lie; neither the son of man, that he should repent: hath he said, and shall he not do it? or hath he spoken, and shall he not make it good?",
      "M": "'God is not a man who lies, nor a son of man who changes his mind. Does he speak and not act? Does he promise and not fulfill?'",
      "T": "'God is not human — he does not lie.\nHe is not mortal — he does not change his mind.\nHas he ever spoken without acting?\nHas he ever promised without delivering?'"
    },
    "20": {
      "L": "Behold, I have received commandment to bless: and he hath blessed; and I cannot reverse it.",
      "M": "'I have received a command to bless; he has blessed, and I cannot reverse it.'",
      "T": "'I received the command to bless.\nHe has blessed.\nI cannot undo it.'"
    },
    "21": {
      "L": "He hath not beheld iniquity in Jacob, neither hath he seen perverseness in Israel: the LORD his God is with him, and the shout of a king is among them.",
      "M": "'He has not seen iniquity in Jacob nor found trouble in Israel. The LORD their God is with them; the acclamation of a king is among them.'",
      "T": "'God looks on Jacob and sees no iniquity;\nhe surveys Israel and finds no perverseness.\nThe LORD their God is with them,\nand the shout of a king rises from their camp.'"
    },
    "22": {
      "L": "God brought them out of Egypt; he hath as it were the strength of an unicorn.",
      "M": "'God brought them out of Egypt with the power of a wild ox.'",
      "T": "'God brought them out of Egypt —\nhe acts with the strength of a wild ox.'"
    },
    "23": {
      "L": "Surely there is no enchantment against Jacob, neither is there any divination against Israel: according to this time it shall be said of Jacob and of Israel, What hath God wrought!",
      "M": "'There is no omen that works against Jacob, no divination that prevails against Israel. In due time it will be said of Jacob and Israel: See what God has done!'",
      "T": "'No curse holds against Jacob;\nno divination has power over Israel.\nIn its own time this will be said of Jacob and Israel:\nLook what God has done!'"
    },
    "24": {
      "L": "Behold, the people shall rise up as a great lion, and lift up himself as a young lion: he shall not lie down until he eat of the prey, and drink the blood of the slain.",
      "M": "'The people rise like a lioness; they rouse themselves like a lion that does not rest until it devours its prey and drinks the blood of the slain.'",
      "T": "'They rise like a lioness aroused for the hunt,\nlike a lion that will not lie down until the kill is made —\nuntil it has eaten and drunk the blood of the slain.'"
    },
    "25": {
      "L": "And Balak said unto Balaam, Neither curse them at all, nor bless them at all.",
      "M": "Balak said to Balaam, 'Neither curse them at all nor bless them at all!'",
      "T": "'Then say nothing at all!' Balak snapped. 'No curse — but no blessing either!'"
    },
    "26": {
      "L": "But Balaam answered and said unto Balak, Told not I thee, saying, All that the LORD speaketh, that I must do?",
      "M": "Balaam replied to Balak, 'Did I not tell you that I must do everything the LORD says?'",
      "T": "'Did I not warn you from the start?' Balaam answered. 'Whatever the LORD speaks, that is what I will say.'"
    },
    "27": {
      "L": "And Balak said unto Balaam, Come, I pray thee, I will bring thee unto another place; peradventure it will please God that thou mayest curse me them from thence.",
      "M": "Then Balak said, 'Come, let me take you to another place. Maybe it will please God for you to curse them from there.'",
      "T": "'One more try,' Balak insisted. 'Perhaps God will be pleased with a different spot and you will be able to curse them from there.'"
    },
    "28": {
      "L": "And Balak brought Balaam unto the top of Peor, that looketh toward Jeshimon.",
      "M": "Balak led Balaam to the top of Peor, which overlooks the wasteland.",
      "T": "Balak brought him to the summit of Peor, overlooking the desert."
    },
    "29": {
      "L": "And Balaam said unto Balak, Build me here seven altars, and prepare me here seven bullocks and seven rams.",
      "M": "Balaam said to Balak, 'Build me seven altars here and prepare seven bulls and seven rams.'",
      "T": "Same ritual again: 'Build seven altars,' Balaam said, 'and bring seven bulls and seven rams.'"
    },
    "30": {
      "L": "And Balak did as Balaam had said, and offered a bullock and a ram on every altar.",
      "M": "Balak did as Balaam directed and offered a bull and a ram on each altar.",
      "T": "Balak obeyed, offering a bull and a ram on each of the seven altars."
    }
  },
  "24": {
    "1": {
      "L": "And when Balaam saw that it pleased the LORD to bless Israel, he went not, as at other times, to seek for enchantments, but he set his face toward the wilderness.",
      "M": "When Balaam saw that it pleased the LORD to bless Israel, he did not resort to divination as before but turned to face the wilderness.",
      "T": "Balaam understood now: the LORD had determined to bless Israel. He abandoned divination altogether and turned to face the open desert."
    },
    "2": {
      "L": "And Balaam lifted up his eyes, and he saw Israel abiding in his tents according to their tribes; and the Spirit of God came upon him.",
      "M": "He looked out and saw Israel encamped tribe by tribe, and the Spirit of God came on him.",
      "T": "He saw Israel spread out in orderly tribal camps, and the Spirit of God came upon him."
    },
    "3": {
      "L": "And he took up his parable, and said, Balaam the son of Beor hath said, and the man whose eyes are open hath said:",
      "M": "He delivered his oracle: 'The utterance of Balaam son of Beor, the utterance of the man whose eyes are clear —'",
      "T": "His third oracle:\n'The word of Balaam son of Beor,\nthe word of the man whose eyes are opened —'"
    },
    "4": {
      "L": "He hath said, which heard the words of God, which saw the vision of the Almighty, falling into a trance, but having his eyes open:",
      "M": "'The utterance of one who hears God's words and sees a vision from the Almighty, who falls prostrate with eyes wide open:'",
      "T": "'who hears the words of God,\nwho sees what the Almighty shows,\nwho falls in a trance, yet sees with open eyes.'"
    },
    "5": {
      "L": "How goodly are thy tents, O Jacob, and thy tabernacles, O Israel!",
      "M": "'How beautiful are your tents, Jacob, your dwelling places, Israel!'",
      "T": "'How beautiful your tents, O Jacob!\nYour encampments, O Israel!'"
    },
    "6": {
      "L": "As the valleys are they spread forth, as gardens by the river's side, as the trees of lign aloes which the LORD hath planted, and as cedar trees beside the waters.",
      "M": "'Like valleys stretching out, like gardens beside a river, like aloe trees planted by the LORD, like cedars beside the waters.'",
      "T": "'Like broad valleys, like gardens along a river,\nlike aloe trees the LORD himself has planted,\nlike cedar trees beside living water.'"
    },
    "7": {
      "L": "He shall pour the water out of his buckets, and his seed shall be in many waters, and his king shall be higher than Agag, and his kingdom shall be exalted.",
      "M": "'Water will flow from his buckets, his seed will have abundant water; his king will be greater than Agag, and his kingdom will be exalted.'",
      "T": "'Water overflows his pails —\nhis seed grows in abundant streams.\nHis king will rise greater than Agag;\nhis kingdom will be lifted up.'"
    },
    "8": {
      "L": "God brought him forth out of Egypt; he hath as it were the strength of an unicorn: he shall eat up the nations his enemies, and shall break their bones, and pierce them through with his arrows.",
      "M": "'God brought him out of Egypt with the strength of a wild ox. He will devour hostile nations, crush their bones, and shatter them with his arrows.'",
      "T": "'God brought him out of Egypt —\npowerful as a wild ox.\nHe will consume the nations that oppose him,\ncrush their bones,\npierce them through with his arrows.'"
    },
    "9": {
      "L": "He couched, he lay down as a lion, and as a great lion: who shall stir him up? Blessed is he that blesseth thee, and cursed is he that curseth thee.",
      "M": "'He crouches and lies down like a lion or a lioness; who dares rouse him? Blessed is everyone who blesses you, and cursed is everyone who curses you.'",
      "T": "'He crouches, lies down like a lion,\nlike the king of beasts —\nwho would dare to rouse him?\nBlessed are those who bless you;\ncursed are those who curse you.'"
    },
    "10": {
      "L": "And Balak's anger was kindled against Balaam, and he smote his hands together: and Balak said unto Balaam, I called thee to curse mine enemies, and, behold, thou hast altogether blessed them these three times.",
      "M": "Balak was furious with Balaam. He struck his palms together and said, 'I called you to curse my enemies, but you have blessed them three times over!'",
      "T": "Balak erupted in fury. He clapped his hands together: 'I brought you here to curse my enemies, and you have blessed them three times running!'"
    },
    "11": {
      "L": "Therefore now flee thou to thy place: I thought to promote thee unto great honour; but, lo, the LORD hath kept thee back from honour.",
      "M": "'Now get back to where you came from! I intended to honor you greatly, but the LORD has kept that honor from you.'",
      "T": "'Go home! I intended to make you rich and famous, but the LORD has denied you that reward.'"
    },
    "12": {
      "L": "And Balaam said unto Balak, Spake I not also to thy messengers which thou sentest unto me, saying,",
      "M": "Balaam answered Balak, 'Did I not tell your messengers from the very beginning:'",
      "T": "'Did I not tell your very first delegation,' Balaam replied to Balak,'"
    },
    "13": {
      "L": "If Balak would give me his house full of silver and gold, I cannot go beyond the commandment of the LORD, to do either good or bad of mine own mind; but what the LORD saith, that will I speak?",
      "M": "'Even if Balak gave me his palace full of silver and gold, I could not go against the LORD's command to do anything good or bad of my own will — whatever the LORD says, that is what I speak.'",
      "T": "'Even a palace full of silver and gold could not move me past the LORD's command. I have no will in this matter. What the LORD says is what comes out of my mouth.'"
    },
    "14": {
      "L": "And now, behold, I go unto my people: come therefore, and I will advertise thee what this people shall do to thy people in the latter days.",
      "M": "'Now I am going back to my own people. But let me warn you what this people will do to your people in the days to come.'",
      "T": "'I am returning to my own people. But hear this first — what Israel will do to Moab in the days to come.'"
    },
    "15": {
      "L": "And he took up his parable, and said, Balaam the son of Beor hath said, and the man whose eyes are open hath said:",
      "M": "He delivered his oracle: 'The utterance of Balaam son of Beor, the utterance of the man whose eyes are clear —'",
      "T": "He began a fourth oracle:\n'The word of Balaam son of Beor,\nthe word of the man whose eyes are opened —'"
    },
    "16": {
      "L": "He hath said, which heard the words of God, and knew the knowledge of the most High, which saw the vision of the Almighty, falling into a trance, but having his eyes open:",
      "M": "'The utterance of one who hears God's words and knows the knowledge of the Most High, who sees the vision of the Almighty, who falls prostrate with eyes wide open:'",
      "T": "'who hears the words of God,\nwho knows what the Most High knows,\nwho sees what the Almighty shows —\nfalling in a trance, yet seeing with open eyes.'"
    },
    "17": {
      "L": "I shall see him, but not now: I shall behold him, but not nigh: there shall come a Star out of Jacob, and a Sceptre shall rise out of Israel, and shall smite the corners of Moab, and destroy all the children of Sheth.",
      "M": "'I see him, but not now; I behold him, but not near. A Star will come out of Jacob, a Scepter will rise from Israel; he will crush the skulls of Moab and destroy all the sons of Sheth.'",
      "T": "'I see him — but not yet; I behold him — still far off.\nA Star rises from Jacob;\na Scepter advances from Israel.\nHe will shatter Moab's pride;\nhe will destroy all the children of Sheth.'\nThis oracle looks beyond its own horizon — first to David, ultimately to the one who is greater than David."
    },
    "18": {
      "L": "And Edom shall be a possession, Seir also shall be a possession for his enemies; and Israel shall do valiantly.",
      "M": "'Edom will be conquered; Seir, his enemy, will also be conquered. But Israel will act valiantly.'",
      "T": "'Edom will fall before him — Seir too, his enemies both.\nIsrael will rise to greatness.'"
    },
    "19": {
      "L": "Out of Jacob shall come he that shall have dominion, and shall destroy him that remaineth of the city.",
      "M": "'A ruler will come out of Jacob and destroy the survivors of the city.'",
      "T": "'Out of Jacob will come the ruler\nwho sweeps away what remains of every city.'"
    },
    "20": {
      "L": "And when he looked on Amalek, he took up his parable, and said, Amalek was the first of the nations; but his latter end shall be that he perish for ever.",
      "M": "Then Balaam saw Amalek and delivered this oracle: 'Amalek was first among the nations, but their end is destruction.'",
      "T": "Balaam turned his gaze toward Amalek and spoke:\n'Amalek rose first among the nations —\nbut their end is eternal ruin.'"
    },
    "21": {
      "L": "And he looked on the Kenites, and took up his parable, and said, Strong is thy dwellingplace, and thou puttest thy nest in a rock.",
      "M": "He looked at the Kenites and said: 'Your dwelling place is secure; your nest is set in rock.'",
      "T": "He looked at the Kenites:\n'Your home is stronghold,\nyour nest built in the rock —'"
    },
    "22": {
      "L": "Nevertheless the Kenite shall be wasted, until Asshur shall carry thee away captive.",
      "M": "'Yet the Kenite will be destroyed when Asshur takes you captive.'",
      "T": "'— yet even Kain will be ruined;\nAsshur will carry you into exile.'"
    },
    "23": {
      "L": "And he took up his parable, and said, Alas, who shall live when God doeth this!",
      "M": "Then he spoke another oracle: 'Alas, who can survive when God brings this about?'",
      "T": "'Alas — who survives when God unleashes this?'"
    },
    "24": {
      "L": "And ships shall come from the coast of Chittim, and shall afflict Asshur, and shall afflict Eber, and he also shall perish for ever.",
      "M": "'Ships will come from the coasts of Kittim; they will oppress Asshur and Eber, but they too will come to ruin.'",
      "T": "'Fleets from Kittim will come,\nand they will humble Asshur, humble Eber —\nbut they in turn will also perish.'"
    },
    "25": {
      "L": "And Balaam rose up, and went and returned to his place: and Balak also went his way.",
      "M": "Then Balaam got up and returned home, and Balak went his way.",
      "T": "With that, Balaam set out on the road back to his homeland. Balak went his own way."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'numbers')
        merge_tier(existing, NUMBERS, tier_key)
        save(tier_dir, 'numbers', existing)
    print('Numbers 19–24 written.')

if __name__ == '__main__':
    main()
