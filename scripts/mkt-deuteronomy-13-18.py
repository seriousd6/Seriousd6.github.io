"""
MKT Deuteronomy chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-deuteronomy-13-18.py

Covers: the test of false prophets and the apostate city (ch. 13); dietary laws and tithing
(ch. 14); the year of release, Hebrew slave law, and firstlings (ch. 15); the three annual feasts,
appointment of judges, and prohibition of cultic objects (ch. 16); unblemished sacrifice, the
central tribunal, and the king's law (ch. 17); Levitical provision, abominations of divination,
and the Prophet like Moses (ch. 18).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — matches prior Numbers/Exodus/Leviticus scripts
- H430 (אֱלֹהִים): "God" in all tiers
- H5315 (נֶפֶשׁ): "soul" in L/M; "whole being" in T (ch. 13:3) — embodied self, not Greek immaterial soul
- H1285 (בְּרִית): "covenant" in all tiers (17:2)
- H8451 (תּוֹרָה): "law" in L/M; "instruction" or "law" in T depending on whether a relational
  or juridical sense is primary — e.g., 17:18-19 "copy of this law" kept as "law" throughout
  since the physical act of writing is in view
- H5030 (נָבִיא): "prophet" in all tiers
- H2492 (חָלַם) / H2493 (חֲלוֹם): "dreamer" / "dream" in all tiers
- H226 (אוֹת) / H4159 (מוֹפֵת): "sign" / "wonder" in L/M; "miraculous sign" / "portent" in T
- H1100 (בְּלִיַּעַל) ch. 13:13: "worthless men" in L/M; "ringleaders of ruin" in T — the term
  denotes moral emptiness and the chaos that follows; "sons of Belial" is the literal but
  "ringleaders of ruin" captures the T tier's aim to surface the social damage
- H5459 (סְגֻלָּה) ch. 14:2: "treasured possession" in L/M; "his very own treasured people" in T
  — patron-client covenant language; the LORD has made Israel his personal estate
- H8059 (שְׁמִטָּה) ch. 15:1-2: "release" in L; "debt-release" concept named explicitly in T —
  this is the sabbatical year cancellation of debt; radical economic grace, not merely a ritual
- H4428 (מֶלֶךְ) ch. 17: "king" in all tiers; T notes the anti-accumulation logic at vv. 16-17
- H8549 (תָּמִים) ch. 18:13: "blameless" in L/M; "whole-hearted" in T — integrity, not perfection
- H6944 (קֹדֶשׁ): "holy" in L/M; context-driven in T ("holy" or "set apart to the LORD")
- Deut 13: The false prophet test is theological, not merely predictive — even if the sign
  comes true, the destination is what disqualifies the prophet. T tier makes this priority explicit.
- Deut 13:5 "purge the evil from your midst": the phrase is a legal formula; T surfaces its
  communal protective function, not merely punitive.
- Deut 14:1 "children of the LORD your God": "sons" is H1121 (בֵּן); T renders "children" to
  preserve the relational intimacy without implying only males.
- Deut 15:4 "there will be no poor among you": the Hebrew has an optative force; T notes
  the conditional: this will be true if — and only if — the command is obeyed.
- Deut 15:11 "the poor will never cease": in tension with v. 4 — v. 4 is the covenant ideal;
  v. 11 is the realistic expectation. Both are true; T surfaces both without harmonizing them away.
- Deut 16:19 "bribe blinds the eyes of the wise": T notes this applies specifically to those
  with discernment; corruption is most dangerous among people who should know better.
- Deut 17:14-20 king's law: written before Israel has a king; T notes this reads like a
  negative portrait of Solomon's failures (horses from Egypt, 700 wives, vast gold) — a law
  given as a warning that became a judgment.
- Deut 18:15 "a prophet like me": the climax of the section on true prophecy; T surfaces the
  eschatological weight — this points beyond any single successor to the prophetic tradition
  and carries Johannine resonance (John 1:21; 6:14; Acts 3:22).
- Deut 18:22 true/false prophet test (word comes to pass) is the second side of a two-part
  discernment test: ch. 13 tests destination (theological content); ch. 18 tests accuracy
  (fulfillment). Together: a true prophet leads toward the LORD and his words come true.
- Verb aspect observed throughout: waw-consecutive imperfects in narrative portions rendered
  as narrative past; imperatives preserved as imperatives in L/M; T surfaces aspect nuance.
- Divine passive: "as he has sworn" (17:20; 13:17) implies the LORD as agent; preserved
  in all tiers; T notes where the oath activates the covenant promise.
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

DEUTERONOMY = {
  "13": {
    "1": {
      "L": "If a prophet or a dreamer of dreams arises among you and gives you a sign or a wonder,",
      "M": "If a prophet or a dreamer of dreams arises among you and gives you a sign or a wonder,",
      "T": "Suppose a prophet or a dream-visionary appears among you and offers you a miraculous sign or a portent,"
    },
    "2": {
      "L": "and the sign or the wonder comes to pass, of which he spoke to you, saying, 'Let us go after other gods, whom you have not known, and let us serve them,'",
      "M": "and that sign or wonder actually comes to pass, while he says, 'Let us go after other gods — gods you have not known — and let us serve them,'",
      "T": "and the sign actually comes to pass — yet he uses it to say, 'Come, let us follow other gods, gods you have never known; let us worship them' —"
    },
    "3": {
      "L": "you shall not listen to the words of that prophet or that dreamer of dreams, for the LORD your God is testing you, to know whether you love the LORD your God with all your heart and with all your soul.",
      "M": "you shall not listen to the words of that prophet or that dreamer, for the LORD your God is testing you to find out whether you love the LORD your God with all your heart and with all your soul.",
      "T": "do not obey that prophet or that dreamer. The LORD your God is testing you — testing whether you love him with your whole heart and your whole being. The sign's accuracy is not the test; the destination is."
    },
    "4": {
      "L": "You shall walk after the LORD your God and fear him, and keep his commandments and obey his voice, and you shall serve him and hold fast to him.",
      "M": "You shall follow the LORD your God, fear him, keep his commandments, obey his voice, serve him, and hold fast to him.",
      "T": "Walk with the LORD your God. Fear him, keep his commands, listen to his voice, serve him, and cling to him — these are the marks of genuine loyalty."
    },
    "5": {
      "L": "But that prophet or that dreamer of dreams shall be put to death, because he has spoken revolt against the LORD your God who brought you out of the land of Egypt and redeemed you out of the house of slavery, to thrust you out of the way that the LORD your God commanded you to walk in. So you shall purge the evil from your midst.",
      "M": "That prophet or dreamer must be put to death, because he has incited rebellion against the LORD your God who brought you out of Egypt and redeemed you from slavery — he tried to drive you off the path the LORD your God commanded you to walk. So purge the evil from your midst.",
      "T": "That prophet or dreamer must be executed. He incited rebellion against the LORD your God — the God who freed you from Egypt and bought you back from slavery — trying to push you off the path the LORD set for you. The community's purity depends on removing such a corrupting influence."
    },
    "6": {
      "L": "If your brother, the son of your mother, or your son or your daughter or the wife of your embrace or your friend who is as your own soul entices you secretly, saying, 'Let us go and serve other gods,' which you have not known, you or your fathers,",
      "M": "If your brother — your mother's son — or your son or daughter, or the wife of your embrace, or your closest friend secretly entices you, saying, 'Let us go and serve other gods' — gods that neither you nor your ancestors have known —",
      "T": "Even if it is your own brother — your mother's child — or your son, your daughter, the wife you hold dear, or a friend closer than your own life who secretly tries to lure you, saying, 'Come, let us serve other gods — gods our families never knew —'"
    },
    "7": {
      "L": "namely, of the gods of the peoples who are all around you, whether near you or far from you, from the one end of the earth to the other end of the earth,",
      "M": "— gods of the peoples around you, whether near or far, from one end of the earth to the other —",
      "T": "— the gods of the surrounding nations, near neighbors or distant peoples, from one horizon to the other —"
    },
    "8": {
      "L": "you shall not consent to him, nor listen to him; nor shall your eye pity him, nor shall you spare him or conceal him.",
      "M": "you shall not consent to him, nor listen to him. Your eye shall not pity him; you shall not spare him or conceal him.",
      "T": "you must not give in to that person or listen to them. Show no pity. Spare nothing. Conceal nothing. The closeness of the relationship is precisely what makes the danger so acute."
    },
    "9": {
      "L": "But you shall surely kill him. Your hand shall be first against him to put him to death, and afterward the hand of all the people.",
      "M": "Rather, you shall certainly put him to death. Your hand shall be the first raised against him, and afterward the hand of all the people.",
      "T": "You must execute him. And you shall be the first to raise your hand against him before the whole community does the same. The personal cost proves the public commitment."
    },
    "10": {
      "L": "You shall stone him with stones until he dies, because he sought to drive you away from the LORD your God who brought you out of the land of Egypt, out of the house of slavery.",
      "M": "You shall stone him to death, because he tried to turn you away from the LORD your God who brought you out of Egypt, out of the house of slavery.",
      "T": "Stone him until he is dead. He attempted to sever you from the LORD your God — the one who brought you up out of Egypt, out of the slave-house. That betrayal warrants no lesser judgment."
    },
    "11": {
      "L": "And all Israel shall hear and fear and never do such an evil thing as this among you again.",
      "M": "And all Israel shall hear and be afraid, so that no one ever does such an evil thing among you again.",
      "T": "When all Israel hears what was done, a healthy fear will settle over the community — and no one will dare repeat such wickedness."
    },
    "12": {
      "L": "If you hear in one of your cities, which the LORD your God is giving you to dwell there, someone saying,",
      "M": "If you hear in one of your cities — which the LORD your God is giving you to live in — that someone is saying,",
      "T": "If word reaches you that in one of the towns the LORD your God has given you to settle in, people are saying,"
    },
    "13": {
      "L": "Certain worthless men have gone out from among you and have drawn away the inhabitants of their city, saying, 'Let us go and serve other gods,' which you have not known,'",
      "M": "Certain worthless men have gone out from among you and have led astray the inhabitants of their town, saying, 'Let us go and serve other gods — gods you have not known' —",
      "T": "ringleaders of ruin have emerged from within the town itself and have drawn its residents into apostasy, urging them to worship gods they never knew —"
    },
    "14": {
      "L": "then you shall inquire and make search and ask diligently; and behold, if it is true and certain that such an abomination has been done among you,",
      "M": "then you shall investigate thoroughly and inquire carefully; and if it proves true and certain that such a detestable thing has been done among you,",
      "T": "then you must conduct a thorough investigation — inquire, examine, question carefully. Only if the evidence is conclusive and the abomination confirmed"
    },
    "15": {
      "L": "you shall surely strike the inhabitants of that city with the edge of the sword, devoting it to destruction — all who are in it and its livestock — with the edge of the sword.",
      "M": "you shall certainly strike down the inhabitants of that city with the sword, devoting it to complete destruction — all who are in it and its livestock — with the sword.",
      "T": "shall you put every inhabitant of that city to the sword — human and animal alike — consecrating it to total destruction."
    },
    "16": {
      "L": "You shall gather all its spoil into the middle of its open square and burn with fire the city and all its spoil, the whole of it, for the LORD your God; and it shall be a heap of ruins forever; it shall never be rebuilt.",
      "M": "You shall gather all its plunder into the center of its public square and burn the city and all its plunder as a whole offering to the LORD your God. It shall be a permanent ruin; it must never be rebuilt.",
      "T": "Pile all the city's goods into the town square and burn everything — city and contents together — as a total offering given over to the LORD your God. Let it remain a heap of rubble forever. It must never rise again."
    },
    "17": {
      "L": "None of the devoted things shall stick to your hand, that the LORD may turn from his fierce anger and show you mercy and have compassion on you and multiply you, as he swore to your fathers,",
      "M": "None of the devoted things shall cling to your hand, so that the LORD may turn from his burning anger, show you mercy, and have compassion on you, and multiply you as he swore to your fathers,",
      "T": "Let none of the condemned goods touch your hands. Only then will the LORD relent from his blazing anger, extend his mercy, and deal with you in compassion — multiplying you just as he swore by oath to your ancestors."
    },
    "18": {
      "L": "when you obey the voice of the LORD your God, keeping all his commandments that I am commanding you today, doing what is right in the eyes of the LORD your God.",
      "M": "when you obey the voice of the LORD your God by keeping all his commandments that I am commanding you today, doing what is right in the sight of the LORD your God.",
      "T": "This promise activates when you listen to the LORD's voice — obeying all the commands I am giving you today, doing what is right and good in his sight."
    }
  },
  "14": {
    "1": {
      "L": "You are the children of the LORD your God. You shall not cut yourselves or make any baldness on your foreheads for the dead.",
      "M": "You are the children of the LORD your God. You shall not gash yourselves or shave the front of your head in mourning for the dead.",
      "T": "You are the LORD your God's own children. That identity forbids the grief-rites of the nations — cutting your bodies or shaving your foreheads in mourning. Who you are determines how you grieve."
    },
    "2": {
      "L": "For you are a people holy to the LORD your God, and the LORD has chosen you to be a people for his treasured possession, out of all the peoples who are on the face of the earth.",
      "M": "For you are a people holy to the LORD your God, and the LORD has chosen you to be his treasured possession from all the peoples on the face of the earth.",
      "T": "You are a people set apart as sacred to the LORD your God. He has chosen you — out of all peoples on earth — to be his very own treasured people. This election, not mere custom, is the foundation of the laws that follow."
    },
    "3": {
      "L": "You shall not eat any abominable thing.",
      "M": "You shall not eat any detestable thing.",
      "T": "You shall eat nothing the LORD has designated as unclean."
    },
    "4": {
      "L": "These are the animals you may eat: the ox, the sheep, the goat,",
      "M": "These are the animals you may eat: the ox, the sheep, and the goat;",
      "T": "These are the animals permitted for food: cattle, sheep, and goat;"
    },
    "5": {
      "L": "the deer, the gazelle, the roebuck, the wild goat, the ibex, the antelope, and the mountain sheep.",
      "M": "the deer, the gazelle, the roe deer, the wild goat, the ibex, the antelope, and the mountain sheep.",
      "T": "the deer, the gazelle, the roe deer, the wild goat, the ibex, the antelope, and the mountain sheep."
    },
    "6": {
      "L": "Every animal that parts the hoof and has the hoof cleft in two and chews the cud, among the animals — that you may eat.",
      "M": "You may eat any animal that has completely split hooves and chews the cud.",
      "T": "The rule for land animals: split hooves completely divided, and the animal chews the cud — both marks together qualify it for your table."
    },
    "7": {
      "L": "Yet of those that chew the cud or of those that have the hoof divided, these you shall not eat: the camel, the hare, and the rock badger, because they chew the cud but do not part the hoof — they are unclean for you.",
      "M": "However, among those that chew the cud or have split hooves, these you shall not eat: the camel, the hare, and the rock badger — for though they chew the cud, they do not have split hooves. They are unclean for you.",
      "T": "Among animals that partly meet the criteria, these are excluded: the camel, the hare, and the rock badger — they chew the cud but their hooves are not split. Meeting only one condition is not enough; they are unclean for you."
    },
    "8": {
      "L": "And the pig, because it parts the hoof but does not chew the cud — it is unclean for you. You shall not eat their flesh, and you shall not touch their carcasses.",
      "M": "And the pig — though it has split hooves, it does not chew the cud. It is unclean for you. You shall not eat their meat or touch their carcasses.",
      "T": "The pig likewise: it has split hooves but does not chew the cud. That disqualifies it. Avoid its meat entirely, and do not even handle its carcass."
    },
    "9": {
      "L": "Of all that are in the waters you may eat these: everything that has fins and scales you may eat.",
      "M": "Of all creatures living in the water, you may eat those that have fins and scales.",
      "T": "For creatures of the water, the rule is simple: fins and scales — both present, the creature is clean and may be eaten."
    },
    "10": {
      "L": "And whatever does not have fins and scales you shall not eat; it is unclean for you.",
      "M": "But whatever lacks fins or scales you shall not eat; it is unclean for you.",
      "T": "Anything that lives in water but lacks fins or scales is unclean — it may not be eaten."
    },
    "11": {
      "L": "You may eat all clean birds.",
      "M": "You may eat any clean bird.",
      "T": "Any bird that is clean may be eaten."
    },
    "12": {
      "L": "But these are the ones from which you shall not eat: the eagle, the bearded vulture, and the black vulture,",
      "M": "These are the birds you shall not eat: the eagle, the bearded vulture, and the black vulture;",
      "T": "The following birds are excluded from your diet: the eagle, the bearded vulture, the black vulture,"
    },
    "13": {
      "L": "the kite, the falcon, and every kind of kite,",
      "M": "the kite and any kind of falcon,",
      "T": "the kite and every species of falcon,"
    },
    "14": {
      "L": "every raven of any kind,",
      "M": "every kind of raven,",
      "T": "every species of raven,"
    },
    "15": {
      "L": "the ostrich, the nighthawk, the sea gull, and every kind of hawk,",
      "M": "the ostrich, the nighthawk, the sea gull, and every kind of hawk,",
      "T": "the ostrich, the nighthawk, the sea gull, every species of hawk,"
    },
    "16": {
      "L": "the little owl, the great owl, and the barn owl,",
      "M": "the little owl, the screech owl, and the barn owl,",
      "T": "the little owl, the screech owl, the barn owl,"
    },
    "17": {
      "L": "the pelican, the carrion vulture, and the cormorant,",
      "M": "the pelican, the carrion vulture, and the cormorant,",
      "T": "the pelican, the carrion vulture, the cormorant,"
    },
    "18": {
      "L": "the stork, every kind of heron, the hoopoe, and the bat.",
      "M": "the stork, any kind of heron, the hoopoe, and the bat.",
      "T": "the stork, every species of heron, the hoopoe, and the bat."
    },
    "19": {
      "L": "And all winged swarming things are unclean for you; they shall not be eaten.",
      "M": "All winged insects are unclean for you; they shall not be eaten.",
      "T": "All winged insects are unclean — none of them may be eaten."
    },
    "20": {
      "L": "All clean birds you may eat.",
      "M": "But all clean birds you may eat.",
      "T": "Every clean bird, however, is permitted."
    },
    "21": {
      "L": "You shall not eat anything that dies of itself. You may give it to the sojourner who is within your gates, that he may eat it, or you may sell it to a foreigner; for you are a people holy to the LORD your God. You shall not boil a young goat in its mother's milk.",
      "M": "You shall not eat anything that dies of itself. You may give it to the foreigner living in your town to eat, or you may sell it to an outsider — for you are a people holy to the LORD your God. You shall not boil a young goat in its mother's milk.",
      "T": "An animal that died on its own — you may not eat it. Give it to a resident foreigner or sell it to a passing outsider. The reason is your identity: you are a people set apart as sacred to the LORD your God. And do not cook a kid in its own mother's milk — the mixing of life and death in the very source of nourishment is incompatible with who you are."
    },
    "22": {
      "L": "You shall tithe all the yield of your seed that comes from the field year by year.",
      "M": "You shall tithe all the yield of your seed that comes from the field each year.",
      "T": "Set aside a tenth of everything your fields produce — year after year, without exception."
    },
    "23": {
      "L": "And before the LORD your God, in the place that he will choose to make his name dwell there, you shall eat the tithe of your grain, of your wine, and of your oil, and the firstborn of your herd and flock, that you may learn to fear the LORD your God always.",
      "M": "And in the presence of the LORD your God, at the place he will choose to make his name dwell, you shall eat the tithe of your grain, wine, and oil, and the firstborn of your herd and flock, so that you may learn to fear the LORD your God always.",
      "T": "Bring these tithes to the place the LORD will designate as the home of his name, and eat them there in his presence — the tithe of your grain, wine, and oil, and the firstborn of your herds and flocks. This annual journey and shared meal before the LORD teaches you, year after year, what it means to revere him."
    },
    "24": {
      "L": "And if the way is too long for you, so that you are not able to carry the tithe, when the LORD your God blesses you, because the place is too far from you which the LORD your God will choose to set his name there,",
      "M": "But if the distance is too great for you to carry the tithe — because the place where the LORD your God will choose to put his name is too far away, and because the LORD your God has blessed you —",
      "T": "If the journey is too long and your harvest too large to carry all the way to the chosen place — the LORD's own blessing creating the problem —"
    },
    "25": {
      "L": "then you shall turn it into money and bind up the money in your hand and go to the place that the LORD your God will choose.",
      "M": "then you shall exchange the tithe for money, and take the money in hand to the place that the LORD your God will choose.",
      "T": "then convert your tithe into silver, travel to the designated place with the money in hand,"
    },
    "26": {
      "L": "And you shall spend the money for whatever you desire — for oxen, or sheep, or wine, or strong drink, or whatever your soul craves — and you shall eat there before the LORD your God and rejoice, you and your household.",
      "M": "and spend the money for whatever you desire — cattle, sheep, wine, strong drink, or whatever you want — and eat there before the LORD your God and rejoice, you and your household.",
      "T": "and spend it freely on whatever you wish — cattle, sheep, wine, even strong drink, whatever your heart desires — and eat it as a feast before the LORD your God. You and your whole family are to rejoice in his presence. The point is celebration, not mere compliance."
    },
    "27": {
      "L": "And you shall not neglect the Levite who is within your towns, for he has no portion or inheritance with you.",
      "M": "And do not neglect the Levite who lives in your towns, for he has no portion or inheritance among you.",
      "T": "And do not forget the Levite living in your community. He has no land of his own among you — he depends on what you share."
    },
    "28": {
      "L": "At the end of every three years you shall bring out all the tithe of your produce in the same year and lay it up within your towns,",
      "M": "At the end of every three years you shall bring out all the tithe of your produce from that year and store it within your towns,",
      "T": "Every third year, instead of taking the tithe to the central sanctuary, bring it out and store it in your own towns —"
    },
    "29": {
      "L": "and the Levite, because he has no portion or inheritance with you, and the sojourner, the fatherless, and the widow who are within your towns shall come and eat and be satisfied, that the LORD your God may bless you in all the work of your hands that you do.",
      "M": "so that the Levite — who has no portion or inheritance among you — and the resident foreigner, the fatherless, and the widow within your towns may come and eat and be satisfied. Then the LORD your God will bless you in all the work of your hands.",
      "T": "— so that the Levite, the resident foreigner, the orphan, and the widow, all of them landless and dependent, can come and eat their fill. Care for the vulnerable is not optional charity; it is the condition under which the LORD promises to bless everything you do."
    }
  },
  "15": {
    "1": {
      "L": "At the end of every seven years you shall grant a release.",
      "M": "At the end of every seven years you shall grant a release.",
      "T": "Every seventh year you shall enact a complete release of debts."
    },
    "2": {
      "L": "And this is the manner of the release: every creditor shall release what he has lent to his neighbor. He shall not exact it of his neighbor, his brother, because the LORD's release has been proclaimed.",
      "M": "And this is how the release shall work: every creditor shall cancel what he has lent to his neighbor. He must not press his neighbor or his brother for repayment, because the LORD's release has been proclaimed.",
      "T": "Here is how it works: every lender cancels whatever he is owed by a fellow Israelite. He may not collect from his neighbor or his brother — because the LORD himself has declared this a year of release. The debt is gone, not deferred."
    },
    "3": {
      "L": "You may exact it of a foreigner, but whatever of yours is with your brother your hand shall release.",
      "M": "You may collect from a foreigner, but whatever your brother owes you, you must release.",
      "T": "You may still press a foreigner for repayment, but whatever an Israelite brother owes you — you let it go."
    },
    "4": {
      "L": "But there will be no poor among you; for the LORD will bless you in the land that the LORD your God is giving you for an inheritance to possess —",
      "M": "There need be no poor among you, for the LORD will surely bless you in the land that the LORD your God is giving you as an inheritance to possess —",
      "T": "In principle, there ought to be no poverty among you at all — because the LORD will richly bless you in the land he is giving you as your inheritance —"
    },
    "5": {
      "L": "if only you carefully obey the voice of the LORD your God, being careful to do all this commandment that I am commanding you today.",
      "M": "if only you carefully obey the voice of the LORD your God, being diligent to keep all this commandment that I am commanding you today.",
      "T": "but this is conditional: it depends entirely on your faithful obedience to the LORD your God, carefully carrying out every command I am giving you today."
    },
    "6": {
      "L": "For the LORD your God will bless you, as he promised you, and you shall lend to many nations but shall not borrow, and you shall rule over many nations but they shall not rule over you.",
      "M": "For the LORD your God will bless you as he has promised, and you will lend to many nations but not borrow, and you will rule over many nations but they will not rule over you.",
      "T": "When you obey, the blessing will be so abundant that you become the lender, not the debtor; the leader among nations, not the subordinate. The LORD's promise is as firm as the condition you must meet."
    },
    "7": {
      "L": "If among you, one of your brothers should become poor, in any of your towns within your land that the LORD your God is giving you, you shall not harden your heart or shut your hand against your poor brother.",
      "M": "If there is a poor person among you, one of your brothers, in any of your towns in the land that the LORD your God is giving you, you shall not harden your heart or shut your hand against your poor brother.",
      "T": "When one of your fellow Israelites falls into poverty — in any of the towns the LORD your God is giving you — do not let your heart grow cold toward him or keep your hand clenched shut. He is your brother."
    },
    "8": {
      "L": "But you shall open wide your hand to him and lend him sufficient for his need, whatever it may be.",
      "M": "Instead, you shall open your hand wide to him and lend him whatever he needs, enough for his lack.",
      "T": "Open your hand wide. Lend him enough to cover what he lacks, whatever that is. Generosity is the expected response, not the exceptional one."
    },
    "9": {
      "L": "Take care lest there be an unworthy thought in your heart and you say, 'The seventh year, the year of release is near,' and your eye look grudgingly on your poor brother, and you give him nothing, and he cry to the LORD against you, and you be guilty of sin.",
      "M": "Guard against an unworthy thought in your heart: 'The seventh year, the year of release, is near,' so that you look with hostility on your poor brother and give him nothing. He will cry to the LORD against you, and you will be found guilty of sin.",
      "T": "Watch your own heart carefully. The thought that will tempt you is this: 'The release year is almost here — why lend now when the debt will be cancelled soon?' If that calculation hardens your eye against a poor brother and you give him nothing, he will cry to the LORD — and the LORD will hear, and you will be culpable."
    },
    "10": {
      "L": "You shall give to him freely, and your heart shall not be grudging when you give to him, because for this the LORD your God will bless you in all your work and in all that you undertake.",
      "M": "Give to him generously, and do not be reluctant when you give, for because of this the LORD your God will bless you in all your work and in everything you put your hand to.",
      "T": "Give freely, without internal resentment. The LORD your God will bless you in direct proportion to the openhandedness you show — in your work, in every enterprise. Generosity and prosperity are not in competition."
    },
    "11": {
      "L": "For the poor will never cease out of the land. Therefore I command you, 'You shall open wide your hand to your brother, to the needy and to the poor in your land.'",
      "M": "For there will never cease to be poor people in the land. That is why I am commanding you to open your hand wide to your brother — to the needy and poor in your land.",
      "T": "The poor will always be among you — that is the realistic expectation, standing alongside the covenant ideal of verse 4. Both are true. And precisely because poverty persists, the command must be repeated: open your hand, always and without exception, to every needy and poor person in your land."
    },
    "12": {
      "L": "If your brother, a Hebrew man or a Hebrew woman, is sold to you, he shall serve you six years, and in the seventh year you shall let him go free from you.",
      "M": "If your brother, a Hebrew man or a Hebrew woman, is sold to you and serves you six years, then in the seventh year you shall set him free.",
      "T": "If a fellow Israelite — man or woman — sells himself into your service, he works for you six years. In the seventh year he goes free. The sabbatical principle governs persons as well as debts."
    },
    "13": {
      "L": "And when you let him go free from you, you shall not let him go away empty-handed.",
      "M": "And when you set him free, you shall not send him away empty-handed.",
      "T": "When you release him, do not send him out with nothing."
    },
    "14": {
      "L": "You shall furnish him liberally out of your flock, out of your threshing floor, and out of your winepress. As the LORD your God has blessed you, you shall give to him.",
      "M": "You shall supply him generously from your flock, your threshing floor, and your winepress. Give to him as the LORD your God has blessed you.",
      "T": "Equip him well from your flock, your grain, and your wine — proportional to the blessing the LORD your God has given you. The measure of your giving is the measure of what you have received."
    },
    "15": {
      "L": "You shall remember that you were a slave in the land of Egypt, and the LORD your God redeemed you; therefore I command you this today.",
      "M": "Remember that you were a slave in Egypt, and the LORD your God redeemed you; that is why I am commanding you this today.",
      "T": "The whole law rests on memory: you were once a slave in Egypt, and the LORD paid your ransom and set you free. This is not a rule imposed from outside — it is an obligation that flows from who you are and what was done for you."
    },
    "16": {
      "L": "But if he says to you, 'I will not go out from you,' because he loves you and your household, since he is well off with you,",
      "M": "But if the servant says to you, 'I do not want to leave you,' because he loves you and your household and is well-off with you,",
      "T": "But suppose the servant chooses to stay. He has come to love you and your household, and the life he has with you is genuinely good."
    },
    "17": {
      "L": "then you shall take an awl and put it through his ear into the door, and he shall be your slave forever. And you shall do the same to your female slave.",
      "M": "then you shall take an awl and pierce his ear against the door, and he shall be your servant permanently. Do the same for your female servant.",
      "T": "Then take an awl, press his ear to the doorpost, and pierce it through. He becomes your servant for life, by his own public choice — the doorpost is the household boundary; the pierced ear is the mark of belonging. Do the same for a female servant who chooses to stay."
    },
    "18": {
      "L": "It shall not seem hard to you when you let him go free from you, for at half the cost of a hired worker he has served you six years. So the LORD your God will bless you in all that you do.",
      "M": "Do not find it difficult when you set him free, for he has served you six years at half the cost of a hired worker. And the LORD your God will bless you in everything you do.",
      "T": "Do not resent the release — he has given you six years of service at a fraction of what a hired worker would cost. You have received full value. The LORD your God will bless you in all you do when you release him with a generous heart."
    },
    "19": {
      "L": "All the firstborn males that are born among your herd and your flock you shall dedicate to the LORD your God. You shall do no work with the firstborn of your herd, nor shear the firstborn of your flock.",
      "M": "You shall set apart for the LORD your God every firstborn male born of your herd and your flock. You shall not put the firstborn of your herd to work, and you shall not shear the firstborn of your flock.",
      "T": "Every firstborn male of your cattle and your sheep belongs to the LORD your God — dedicate it at birth. Put it to no work. Do not shear it. It is the LORD's, set apart from first breath."
    },
    "20": {
      "L": "You shall eat it before the LORD your God year by year at the place that the LORD will choose, you and your household.",
      "M": "Year by year you shall eat it before the LORD your God at the place the LORD will choose — you and your household.",
      "T": "Year after year, bring it to the place the LORD designates and eat it there in his presence — you and your whole family together."
    },
    "21": {
      "L": "But if it has any blemish — if it is lame or blind or has any serious blemish whatever — you shall not sacrifice it to the LORD your God.",
      "M": "But if it has any defect — if it is lame or blind or has any serious flaw — you do not sacrifice it to the LORD your God.",
      "T": "If the animal has any defect — lameness, blindness, any significant impairment — it is not suitable as an offering to the LORD your God. Only what is whole belongs on the altar."
    },
    "22": {
      "L": "You shall eat it within your towns. The unclean and the clean alike may eat it, as though it were a gazelle or a deer.",
      "M": "You shall eat it within your own towns — the ceremonially unclean and the clean may eat it alike, just as you would eat a gazelle or a deer.",
      "T": "Then eat it locally — in your own town — without the restrictions of a sacred meal. Ritually clean or unclean, the whole household can share it, like any wild game."
    },
    "23": {
      "L": "Only you shall not eat its blood; you shall pour it out on the ground like water.",
      "M": "Only do not eat its blood; pour it out on the ground like water.",
      "T": "One rule remains: never eat the blood. Pour it out on the ground like water — blood is life, and life belongs to the LORD."
    }
  },
  "16": {
    "1": {
      "L": "Observe the month of Abib and keep the Passover to the LORD your God, for in the month of Abib the LORD your God brought you out of Egypt by night.",
      "M": "Observe the month of Abib and celebrate the Passover to the LORD your God, for in the month of Abib the LORD your God brought you out of Egypt by night.",
      "T": "Keep watch for the month of Abib — the first green-grain month of spring — and celebrate Passover to the LORD your God. It was in that month, in the darkness of night, that the LORD your God led you out of Egypt."
    },
    "2": {
      "L": "And you shall offer the Passover sacrifice to the LORD your God from the flock or the herd, at the place that the LORD will choose to make his name dwell there.",
      "M": "You shall sacrifice the Passover offering to the LORD your God — from the flock or the herd — at the place the LORD will choose to establish his name.",
      "T": "Sacrifice the Passover animal — drawn from your flock or herd — to the LORD your God at the central sanctuary he designates as the dwelling-place of his name."
    },
    "3": {
      "L": "You shall eat no leavened bread with it. Seven days you shall eat it with unleavened bread, the bread of affliction — for you came out of the land of Egypt in haste — that all the days of your life you may remember the day when you came out of the land of Egypt.",
      "M": "You shall eat no leavened bread with it. For seven days you shall eat unleavened bread — the bread of affliction — because you left Egypt in haste. You shall remember the day you came out of Egypt all the days of your life.",
      "T": "Eat no leavened bread with it. Seven days you eat unleavened bread — 'the bread of affliction' — because you left Egypt in hurried flight. The flat bread that cannot rise is edible memory: it keeps the Exodus from becoming a distant story and makes it present in your mouth, year after year, your whole life long."
    },
    "4": {
      "L": "No leaven shall be seen with you in all your territory for seven days, nor shall any of the flesh that you sacrifice on the evening of the first day remain all night until morning.",
      "M": "No leaven shall be seen anywhere in your territory for seven days; and none of the flesh you sacrifice on the evening of the first day shall remain until morning.",
      "T": "For those seven days, not a trace of leaven anywhere in your land. And whatever you sacrifice at the evening of the first day must be consumed entirely by morning — nothing carried over."
    },
    "5": {
      "L": "You may not offer the Passover sacrifice within any of your towns that the LORD your God is giving you,",
      "M": "You may not sacrifice the Passover within any of your towns that the LORD your God is giving you.",
      "T": "The Passover sacrifice may not be offered in just any town the LORD your God gives you."
    },
    "6": {
      "L": "but at the place that the LORD your God will choose, to make his name dwell in it, there you shall offer the Passover sacrifice, in the evening at sunset, at the time you came out of Egypt.",
      "M": "Rather, at the place the LORD your God will choose to make his name dwell, there you shall sacrifice the Passover — in the evening, at sunset, at the very time you came out of Egypt.",
      "T": "It must be offered at the single place the LORD designates as the home of his name — in the evening, when the sun has just set, recreating in time the very hour of the original Exodus."
    },
    "7": {
      "L": "And you shall cook it and eat it at the place that the LORD your God will choose. And in the morning you shall turn and go to your tents.",
      "M": "You shall cook and eat it at the place the LORD your God will choose, and in the morning you shall return to your tents.",
      "T": "Roast the animal and eat it there at the sacred site. Come morning, turn and make your way home."
    },
    "8": {
      "L": "For six days you shall eat unleavened bread, and on the seventh day there shall be a solemn assembly to the LORD your God. You shall do no work on it.",
      "M": "For six days you shall eat unleavened bread, and on the seventh day there shall be a solemn assembly for the LORD your God — you shall do no work on that day.",
      "T": "Six days of unleavened bread, and the seventh day is set apart as a sacred gathering before the LORD your God. No ordinary work on that day — the week closes with rest and worship."
    },
    "9": {
      "L": "You shall count seven weeks. Begin to count the seven weeks from the time the sickle is first put to the standing grain.",
      "M": "Count off seven weeks. Start counting the seven weeks from when the sickle is first put to the standing grain.",
      "T": "Count seven full weeks — starting from the day the sickle first touches the standing grain at harvest."
    },
    "10": {
      "L": "Then you shall keep the Feast of Weeks to the LORD your God with the tribute of a freewill offering from your hand, which you shall give as the LORD your God blesses you.",
      "M": "Then you shall celebrate the Feast of Weeks to the LORD your God with a freewill offering from your hand — give in proportion to how the LORD your God has blessed you.",
      "T": "Then celebrate the Feast of Weeks before the LORD your God, bringing a freewill offering calculated by one measure only: how much the LORD has blessed you. The gift mirrors the grace received."
    },
    "11": {
      "L": "And you shall rejoice before the LORD your God — you and your son and your daughter, your male servant and your female servant, the Levite who is within your towns, the sojourner, the fatherless, and the widow who are among you — at the place that the LORD your God will choose, to make his name dwell there.",
      "M": "You shall rejoice before the LORD your God — you, your son and daughter, your male and female servants, the Levite within your towns, and the sojourner, the fatherless, and the widow who live among you — at the place the LORD your God will choose to make his name dwell.",
      "T": "The feast is for everyone: you, your children, your servants, the landless Levite in your community, and every vulnerable person living among you — the foreigner, the orphan, the widow. Rejoice before the LORD at his chosen place. The feast table is deliberately inclusive."
    },
    "12": {
      "L": "You shall remember that you were a slave in Egypt, and you shall be careful to observe these statutes.",
      "M": "Remember that you were a slave in Egypt, and be careful to observe these statutes.",
      "T": "The memory of Egypt anchors these laws: you were once the vulnerable outsider. That memory is what forbids you from excluding the vulnerable from your feast."
    },
    "13": {
      "L": "You shall keep the Feast of Booths seven days, when you have gathered in the produce from your threshing floor and your winepress.",
      "M": "You shall celebrate the Feast of Booths for seven days, when you have gathered in the produce from your threshing floor and your winepress.",
      "T": "At the end of the harvest — when grain and wine are stored and the fields are bare — celebrate the Feast of Booths for seven days."
    },
    "14": {
      "L": "You shall rejoice in your feast — you and your son and your daughter, your male servant and your female servant, the Levite, the sojourner, the fatherless, and the widow who are within your towns.",
      "M": "You shall rejoice in your feast — you, your son and daughter, your male and female servants, the Levite, the sojourner, the fatherless, and the widow in your towns.",
      "T": "And rejoice at the feast — again, with the same full circle of people: family, servants, the landless Levite, the resident foreigner, the orphan, the widow. No one who lives among you is excluded from the celebration."
    },
    "15": {
      "L": "For seven days you shall keep the feast to the LORD your God at the place that the LORD will choose, because the LORD your God will bless you in all your produce and in all the work of your hands, and you will be altogether joyful.",
      "M": "For seven days you shall keep the feast to the LORD your God at the place he will choose, for the LORD your God will bless you in all your produce and in all the work of your hands; and you shall be completely joyful.",
      "T": "Seven days at the place the LORD designates. The ground of the joy is not merely the harvest — it is that the LORD your God has blessed you in it. Gratitude is the proper response to provision, and it should be expressed to the full."
    },
    "16": {
      "L": "Three times a year all your males shall appear before the LORD your God at the place that he will choose: at the Feast of Unleavened Bread, at the Feast of Weeks, and at the Feast of Booths. They shall not appear before the LORD empty-handed.",
      "M": "Three times a year all your males shall appear before the LORD your God at the place he will choose: at the Feast of Unleavened Bread, at the Feast of Weeks, and at the Feast of Booths. They shall not appear before the LORD empty-handed.",
      "T": "Three times every year, every man makes a pilgrimage to the central sanctuary: at Unleavened Bread, at Weeks, and at Booths. And no one comes empty-handed — you bring what corresponds to how the LORD has blessed you."
    },
    "17": {
      "L": "Every man shall give as he is able, according to the blessing of the LORD your God that he has given you.",
      "M": "Every man shall give as he is able, in proportion to the blessing the LORD your God has given him.",
      "T": "The measure of the gift is the measure of the blessing received. This is the principle that prevents both the burden of excessive giving and the empty-handedness of giving nothing."
    },
    "18": {
      "L": "You shall appoint judges and officers in all your towns that the LORD your God is giving you, according to your tribes, and they shall judge the people with righteous judgment.",
      "M": "You shall appoint judges and officials throughout all your towns that the LORD your God is giving you, according to your tribes, and they shall judge the people with just decisions.",
      "T": "Appoint judges and enforcement officials in every town the LORD your God is giving you — structured by tribe, covering the whole land. Their mandate is justice: fair, impartial, and consistent."
    },
    "19": {
      "L": "You shall not pervert justice. You shall not show partiality, and you shall not accept a bribe, for a bribe blinds the eyes of the wise and subverts the cause of the righteous.",
      "M": "Do not pervert justice; do not show favoritism; do not accept a bribe — for a bribe blinds the eyes of the wise and twists the words of the innocent.",
      "T": "Three prohibitions for judges: do not pervert the outcome; do not favor any party; do not accept payment for verdicts. The warning about bribes is telling — they do not merely corrupt the corrupt, they blind the wise. Bribery is most dangerous when it reaches the discerning."
    },
    "20": {
      "L": "Justice, and only justice, you shall pursue, that you may live and inherit the land that the LORD your God is giving you.",
      "M": "Justice, and justice alone, you shall pursue — so that you may live and possess the land the LORD your God is giving you.",
      "T": "Justice — justice alone — is your single pursuit. The doubled word is emphatic: nothing else qualifies. Life in the land, and possession of the land, depend on it."
    },
    "21": {
      "L": "You shall not plant any tree as an Asherah beside the altar of the LORD your God that you shall make.",
      "M": "You shall not set up any wooden Asherah pole beside the altar of the LORD your God that you build.",
      "T": "Do not plant any sacred tree as an Asherah beside the altar of the LORD your God. The fertility-cult pole belongs to another religion entirely and has no place alongside the LORD's altar."
    },
    "22": {
      "L": "And you shall not set up a stone pillar, for the LORD your God hates these.",
      "M": "And do not erect a sacred stone pillar, for the LORD your God hates these.",
      "T": "And do not erect a standing stone — the sacred pillar of Canaanite worship. The LORD your God hates these. They import a theology incompatible with everything the covenant represents."
    }
  },
  "17": {
    "1": {
      "L": "You shall not sacrifice to the LORD your God an ox or a sheep in which is a blemish, any defect whatever, for that is an abomination to the LORD your God.",
      "M": "You shall not sacrifice to the LORD your God an ox or a sheep that has a defect, any serious flaw whatever — that is detestable to the LORD your God.",
      "T": "What you offer to the LORD your God must be without defect. Bringing a flawed animal — any blemish, any impairment — to the altar is not a minor oversight; it is an abomination. The offering reflects what you think of the one you are offering it to."
    },
    "2": {
      "L": "If there is found among you, within any of your towns that the LORD your God is giving you, a man or a woman who does what is evil in the sight of the LORD your God, in transgressing his covenant,",
      "M": "If there is found among you, in any of your towns that the LORD your God is giving you, a man or a woman who does what is evil in the sight of the LORD your God by transgressing his covenant —",
      "T": "If it comes to light that someone within your community — in any town the LORD your God has given you — is doing what is evil in the LORD's sight, violating the very covenant that defines Israel's identity —"
    },
    "3": {
      "L": "and has gone and served other gods and worshiped them, or the sun or the moon or any of the host of heaven, which I have not commanded,",
      "M": "— and has gone and served other gods and bowed down to them, or to the sun or the moon or any of the heavenly host, which I have not commanded —",
      "T": "— if that person has bowed before other gods, worshiped the sun or moon or any force of the heavens — things I have never authorized —"
    },
    "4": {
      "L": "and it is told you and you hear of it, then you shall inquire diligently, and behold, if it is true and certain that such an abomination has been done in Israel,",
      "M": "and you are informed and hear about it, then you shall investigate diligently; and if it is true and confirmed that such a detestable thing has been done in Israel,",
      "T": "and the report reaches you — then investigate thoroughly. If the evidence is solid and the charge confirmed that this abomination has been committed within Israel,"
    },
    "5": {
      "L": "then you shall bring out to your gates that man or that woman who has done this evil thing, and you shall stone that man or woman to death with stones.",
      "M": "then bring that man or woman to your town gate and stone them to death.",
      "T": "bring that man or woman to the town gate and execute them by stoning. The gate is the threshold between the community and the world outside; the execution there both removes the corruption and makes the judgment public."
    },
    "6": {
      "L": "On the evidence of two witnesses or of three witnesses the one who is to die shall be put to death; a person shall not be put to death on the evidence of one witness.",
      "M": "A person shall be put to death only on the testimony of two or three witnesses; no one is to be executed on the testimony of a single witness.",
      "T": "No execution on the word of a single witness alone — at least two, preferably three, are required. The standard of evidence protects the accused even in capital cases."
    },
    "7": {
      "L": "The hand of the witnesses shall be first against him to put him to death, and afterward the hand of all the people. So you shall purge the evil from your midst.",
      "M": "The witnesses shall be first to put him to death, and then all the people shall follow. So you shall purge the evil from your midst.",
      "T": "The witnesses cast the first stones — their testimony and their hands are bound together, preventing false accusation. Then the whole community joins. The evil is purged from Israel's midst; the community takes responsibility for its own purity."
    },
    "8": {
      "L": "If any case arises requiring a decision between one kind of homicide and another, one kind of legal right and another, or one kind of assault and another — any case within your towns that is too difficult for you — then you shall arise and go up to the place that the LORD your God will choose.",
      "M": "If a case arises that is too difficult for your local court — involving disputed homicide, disputed legal rights, or disputed assault — then you shall go up to the place the LORD your God will choose.",
      "T": "When a local court faces a case too complex for its competence — disputed homicide classifications, tangled legal claims, contested assault — the community does not simply guess. There is a court of appeal: go up to the place the LORD has designated."
    },
    "9": {
      "L": "And you shall come to the Levitical priests and to the judge who is in office in those days, and you shall inquire of them, and they shall declare to you the decision of the case.",
      "M": "You shall go to the Levitical priests and to the judge who is serving at that time, and you shall consult them, and they shall give you the verdict.",
      "T": "Present the case to the Levitical priests and the sitting judge. They will hear it and render a binding ruling. The authority is institutional and current — 'the judge in office in those days' is the person with legitimate authority now, not in some idealized past."
    },
    "10": {
      "L": "Then you shall do according to what they declare to you from that place that the LORD will choose, and you shall be careful to do according to all that they direct you.",
      "M": "You shall carry out the verdict they announce to you from that place the LORD will choose, and be careful to do all they instruct you.",
      "T": "Whatever ruling they issue from the designated place — carry it out. Follow every instruction carefully. The central tribunal exists precisely so that local variation and corruption do not fragment Israel's justice."
    },
    "11": {
      "L": "According to the instructions that they give you, and according to the verdict which they pronounce to you, you shall do. You shall not turn aside from the verdict that they declare to you, either to the right hand or to the left.",
      "M": "According to the instruction they give you and the verdict they pronounce, you shall act. Do not deviate from what they declare to you — neither to the right nor to the left.",
      "T": "Follow their instruction and their ruling exactly — not veering right or left. The consistency of obedience to a central judgment is what makes the legal system function as a national system."
    },
    "12": {
      "L": "The man who acts presumptuously by not obeying the priest who stands to minister there before the LORD your God, or the judge, that man shall die. So you shall purge the evil from Israel.",
      "M": "The man who acts arrogantly by refusing to obey the priest who stands to minister before the LORD your God, or the judge — that man shall die. So you shall purge the evil from Israel.",
      "T": "Anyone who defies the ruling — who treats the central tribunal with contempt and refuses to comply — shall be put to death. There is no appeals process beyond the designated court. Defiance of lawful authority is itself the crime, and it carries capital consequences. The evil must be cleared from Israel."
    },
    "13": {
      "L": "And all the people shall hear and fear and not act presumptuously again.",
      "M": "And all the people shall hear and be afraid, and they will not act presumptuously again.",
      "T": "The public nature of the judgment produces its deterrent effect: all Israel hears, all Israel fears, and the temptation toward arrogant defiance is checked."
    },
    "14": {
      "L": "When you come to the land that the LORD your God is giving you, and you possess it and dwell in it and then say, 'I will set a king over me, like all the nations that are around me,'",
      "M": "When you come to the land the LORD your God is giving you and have taken possession and settled in it, and you say, 'I want to set a king over me, like all the nations around me,'",
      "T": "When you have entered the land the LORD your God is giving you, settled into it, and a generation arises that says, 'We want a king — like every other nation has' —"
    },
    "15": {
      "L": "you may indeed set a king over you whom the LORD your God will choose. One from among your brothers you shall set as king over you. You may not put a foreigner over you, who is not your brother.",
      "M": "you may set a king over you — but he must be the one the LORD your God chooses. Set one from among your brothers as king over you; you may not put a foreigner over you, who is not your brother.",
      "T": "you may have a king — but on these terms: the LORD your God designates him; he must be a fellow Israelite, not a foreigner. The king serves within the covenant community and must be of it."
    },
    "16": {
      "L": "Only he must not acquire many horses for himself or cause the people to return to Egypt in order to acquire many horses, since the LORD has said to you, 'You shall never return that way again.'",
      "M": "But he must not acquire many horses for himself or send people back to Egypt to get more horses, since the LORD has told you, 'You shall never return that way again.'",
      "T": "He must not build up a cavalry — that means Egypt, and Egypt means slavery and old allegiances. The LORD has closed that road: 'You shall never return that way again.' A king who stockpiles horses is already turning back toward bondage."
    },
    "17": {
      "L": "And he must not acquire many wives for himself, lest his heart turn away, nor shall he acquire for himself excessive silver and gold.",
      "M": "He must not take many wives for himself, so his heart is not led astray, nor shall he accumulate excessive silver and gold for himself.",
      "T": "He must not multiply wives — political marriages pull the heart toward foreign loyalties and foreign gods, as Solomon's seven hundred wives would prove. And he must not hoard silver and gold — wealth accumulation is power accumulation, and it corrupts. The king's three forbidden accumulations — horses, wives, gold — are the three vectors of imperial power."
    },
    "18": {
      "L": "And when he sits on the throne of his kingdom, he shall write for himself in a book a copy of this law, approved by the Levitical priests.",
      "M": "When he takes the throne of his kingdom, he shall write for himself in a book a copy of this law, verified by the Levitical priests.",
      "T": "When he takes the throne, he must write out by hand his own personal copy of this law — authenticated by the Levitical priests. Not a copy made for him, but one he writes himself. The act of writing is the act of internalization."
    },
    "19": {
      "L": "And it shall be with him, and he shall read in it all the days of his life, that he may learn to fear the LORD his God by keeping all the words of this law and these statutes, and doing them,",
      "M": "It shall be with him, and he shall read in it all the days of his life, that he may learn to fear the LORD his God by keeping all the words of this law and these statutes and doing them,",
      "T": "He keeps it beside him and reads it every day of his reign — not as a legal reference but as a daily discipline that teaches him to fear the LORD his God, and to live by every word of the covenant. The king is Israel's reader-in-chief, shaped by the same Word that shapes the people."
    },
    "20": {
      "L": "that his heart may not be lifted up above his brothers, and that he may not turn aside from the commandment, either to the right hand or to the left, so that he may continue long in his kingdom, he and his children, in the midst of Israel.",
      "M": "so that his heart will not be lifted up above his brothers, and so that he will not turn from the commandment to the right or to the left — and thus he may reign long, he and his sons, in the midst of Israel.",
      "T": "The daily reading guards against the king's greatest temptation: elevation above his own people. He is a brother who happens to hold authority, not a sovereign above the covenant. If he stays within these boundaries, his dynasty endures. If he turns aside — as nearly every king of Israel eventually will — the law itself stands as witness against him."
    }
  },
  "18": {
    "1": {
      "L": "The Levitical priests — all the tribe of Levi — shall have no portion or inheritance with Israel. They shall eat the LORD's food offerings as their inheritance.",
      "M": "The Levitical priests — the whole tribe of Levi — shall have no territorial portion or inheritance among Israel. They shall live on the LORD's food offerings as their inheritance.",
      "T": "The entire tribe of Levi — the priests and all Levites — receives no land grant among the other tribes. Their sustenance comes from the LORD's own altar offerings. The LORD himself is their inheritance."
    },
    "2": {
      "L": "They shall have no inheritance among their brothers; the LORD is their inheritance, as he promised them.",
      "M": "They shall have no inheritance among their brothers; the LORD is their inheritance, as he said to them.",
      "T": "No tribal land, no private holdings — the LORD himself is what Levi possesses. This is the promise given to them, and it is a higher thing than real estate."
    },
    "3": {
      "L": "And this shall be the priests' due from the people, from those who offer a sacrifice, whether an ox or a sheep: they shall give to the priest the shoulder and the two cheeks and the stomach.",
      "M": "This shall be the priests' portion from the people: from those who sacrifice an ox or a sheep, the priest shall receive the shoulder, the two jaws, and the stomach.",
      "T": "Here is the specific provision: from every animal sacrificed — whether cattle or sheep — the priest receives the shoulder, the two cheeks, and the stomach. These portions are his by right, not charity."
    },
    "4": {
      "L": "The firstfruits of your grain, of your wine, and of your oil, and the first fleece of your sheep, you shall give him.",
      "M": "You shall give him the firstfruits of your grain, new wine, and oil, and the first shearing of your sheep.",
      "T": "Additionally: the first yield of your grain, wine, and oil, and the first clippings from your flocks — these belong to the priest. First and best, in every harvest and every shearing."
    },
    "5": {
      "L": "For the LORD your God has chosen him out of all your tribes to stand and minister in the name of the LORD, him and his sons forever.",
      "M": "For the LORD your God has chosen him out of all your tribes to stand and minister in the name of the LORD — him and his sons forever.",
      "T": "The reason for the provision is the calling: the LORD himself chose Levi from all Israel's tribes to stand before him and serve in his name. That sacred work is permanent, and it requires adequate support."
    },
    "6": {
      "L": "And if a Levite comes from any of your towns out of all Israel, where he lived — and he may come whenever he desires — to the place that the LORD will choose,",
      "M": "If a Levite comes from any town throughout Israel where he has been living — and he may come whenever he wishes — to the place the LORD will choose,",
      "T": "Now suppose a Levite from anywhere in Israel decides to travel to the central sanctuary — leaving whatever town he has been settled in, coming of his own free choice."
    },
    "7": {
      "L": "then he may minister in the name of the LORD his God, like all his fellow Levites who stand to minister there before the LORD.",
      "M": "he may minister in the name of the LORD his God, just as all his fellow Levites who stand before the LORD there do.",
      "T": "He is entitled to serve at the altar in the name of the LORD his God, on equal footing with every other Levite already stationed there. There is no two-tier system."
    },
    "8": {
      "L": "They shall have equal portions to eat, besides what comes from the sale of his patrimony.",
      "M": "They shall have equal shares to eat, besides what he has from the sale of his family inheritance.",
      "T": "Equal portions for all — the traveling Levite receives the same as the established ones. Whatever private income he may have from selling inherited property is his in addition."
    },
    "9": {
      "L": "When you come into the land that the LORD your God is giving you, you shall not learn to imitate the detestable practices of those nations.",
      "M": "When you enter the land the LORD your God is giving you, do not learn to imitate the detestable practices of those nations.",
      "T": "When you enter the land the LORD your God is giving you, do not look to the nations you are displacing and imitate their religious practices. What they do is an abomination — do not be drawn to it by curiosity or cultural pressure."
    },
    "10": {
      "L": "There shall not be found among you anyone who burns his son or his daughter as an offering, or who practices divination or tells fortunes or interprets omens, or a sorcerer,",
      "M": "No one among you shall sacrifice his son or daughter in the fire, practice divination, tell fortunes, interpret omens, or practice sorcery,",
      "T": "None of this shall exist among you: no one who passes a child through fire in offering; no diviner, no fortune-teller, no reader of omens, no sorcerer —"
    },
    "11": {
      "L": "or one who casts a spell, or a medium, or a spiritist, or one who inquires of the dead.",
      "M": "or anyone who casts spells, consults a medium or spiritist, or calls up the dead.",
      "T": "— no one who casts binding spells, no medium, no spiritist, no one who attempts to speak with the dead."
    },
    "12": {
      "L": "For whoever does these things is an abomination to the LORD; and because of these abominations the LORD your God is driving them out before you.",
      "M": "For anyone who does these things is detestable to the LORD, and because of these detestable practices the LORD your God is driving those nations out before you.",
      "T": "Everyone who practices these things is an abomination to the LORD. This is precisely why the LORD your God is expelling those nations from the land ahead of you — their practices have made them incompatible with the LORD's presence."
    },
    "13": {
      "L": "You shall be blameless before the LORD your God.",
      "M": "You shall be blameless before the LORD your God.",
      "T": "You must be whole-hearted before the LORD your God — undivided in allegiance, with no part of your religious life reaching toward these other powers."
    },
    "14": {
      "L": "For these nations, which you are about to dispossess, listen to fortune-tellers and to diviners. But as for you, the LORD your God has not allowed you to do this.",
      "M": "For these nations you are about to dispossess listen to fortune-tellers and diviners. But as for you, the LORD your God has not permitted you to do this.",
      "T": "The nations you are replacing turned to fortune-tellers and diviners when they needed guidance. That is the path they chose. The LORD your God has placed you on a different path — and closed the other one off entirely."
    },
    "15": {
      "L": "The LORD your God will raise up for you a prophet like me from among you, from your brothers — it is to him you shall listen.",
      "M": "The LORD your God will raise up for you a prophet like me from your midst, from your brothers — you must listen to him.",
      "T": "But here is what the LORD will provide instead of divination: a prophet, raised up from among your own people — someone like me, a brother. Listen to him. This is the great promise of the chapter: the LORD will not leave his people without a voice."
    },
    "16": {
      "L": "This is in accordance with all that you asked of the LORD your God at Horeb on the day of the assembly, when you said, 'Let me not hear again the voice of the LORD my God or see this great fire any more, lest I die.'",
      "M": "This is exactly what you asked of the LORD your God at Horeb on the day of the assembly, when you said, 'Let me not hear the voice of the LORD my God again or see this great fire anymore, or I will die.'",
      "T": "This promise answers a request Israel itself made. At Horeb, at the foot of the mountain in fire and thunder, the people cried: 'We cannot bear direct access to the LORD — we will die. Do not let us hear that voice directly again.' The prophet is the answer to that prayer: mediated revelation, sustainable access to the living God."
    },
    "17": {
      "L": "And the LORD said to me, 'They have spoken well what they have spoken.'",
      "M": "The LORD said to me, 'What they have said is right.'",
      "T": "And the LORD agreed: 'They have spoken well.' The request for a mediating prophet was not a failure of faith but a realistic recognition of the human condition before divine holiness."
    },
    "18": {
      "L": "'I will raise up for them a prophet like you from among their brothers. And I will put my words in his mouth, and he shall speak to them all that I command him.'",
      "M": "'I will raise up for them a prophet like you from among their brothers. I will put my words in his mouth, and he shall speak to them all that I command him.'",
      "T": "'I will raise up from among their own kin a prophet in your likeness, Moses. I will place my own words in his mouth — he will not speak from himself — and he will deliver to them exactly what I command.' The true prophet is identified by this: he speaks the LORD's words, not his own."
    },
    "19": {
      "L": "'And whoever will not listen to my words that he shall speak in my name, I myself will require it of him.'",
      "M": "'And if anyone will not listen to my words that the prophet speaks in my name, I myself will hold that person accountable.'",
      "T": "'Anyone who refuses to listen when the prophet speaks my words in my name — I will call that person to account personally. To reject the prophet's word is to reject mine.'"
    },
    "20": {
      "L": "'But the prophet who presumes to speak a word in my name that I have not commanded him to speak, or who speaks in the name of other gods — that same prophet shall die.'",
      "M": "'But the prophet who presumes to speak a word in my name that I have not commanded him to say, or who speaks in the name of other gods — that prophet shall die.'",
      "T": "'On the other side: any prophet who fabricates a divine message — claiming my authority for words I never gave — or who speaks in the name of other gods altogether, shall be executed. The prophetic office carries the highest responsibility, and its abuse is a capital offense.'"
    },
    "21": {
      "L": "And if you say in your heart, 'How shall we know the word that the LORD has not spoken?'",
      "M": "And if you ask, 'How can we know whether a word was not spoken by the LORD?'",
      "T": "The inevitable question will arise: how do we tell the genuine prophet from the fabricator? The test is practical:"
    },
    "22": {
      "L": "when a prophet speaks in the name of the LORD, if the word does not come to pass or come true, that is a word that the LORD has not spoken; the prophet has spoken it presumptuously. You need not be afraid of him.",
      "M": "when a prophet speaks in the name of the LORD and the word is not fulfilled or does not come about — that is a word the LORD has not spoken. The prophet has spoken presumptuously; you need not fear him.",
      "T": "if a prophet's word, spoken in the LORD's name, fails to come true — the LORD did not say it. That prophet spoke from his own presumption. Do not fear him or treat his words as authoritative. Read this test alongside chapter 13: there the question was destination — does the prophet lead toward the LORD or away? Here the question is accuracy — does the word come true? A genuine prophet must pass both tests: right direction and fulfilled prediction."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'deuteronomy')
        merge_tier(existing, DEUTERONOMY, tier_key)
        save(tier_dir, 'deuteronomy', existing)
    print('Deuteronomy 13–18 written.')

if __name__ == '__main__':
    main()
