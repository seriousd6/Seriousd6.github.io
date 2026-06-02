"""
MKT Deuteronomy chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-deuteronomy-1-6.py

Covers: Moses' retrospective address — departure from Horeb (ch. 1); wilderness wandering
around Edom/Moab/Ammon, conquest of Sihon (ch. 2); conquest of Og, Transjordan allotments,
Moses forbidden from crossing (ch. 3); the great exhortation against idolatry, Israel's
uniqueness, cities of refuge, covenant preamble (ch. 4); the Decalogue with Deuteronomy's
distinctive rationale — Sabbath grounded in Exodus not creation, people's fear, Moses as
mediator (ch. 5); the Shema, the great commandment, catechism of the Exodus (ch. 6).

Translation decisions (carrying forward from mkt-deuteronomy-7-12.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — consistent with prior Deuteronomy scripts
- H430 (אֱלֹהִים): "God" all tiers
- H2617 (חֶסֶד): "steadfast love" all tiers
- H1285 (בְּרִית): "covenant" all tiers
- H5315 (נֶפֶשׁ): "soul" L/M; "whole self" T — embodied self, not Greek immaterial soul
- H8085 (שָׁמַע): "hear" L; "obey/heed" M where obedience dominates; T surfaces both
- H3820/H3824 (לֵב/לֵבָב): "heart" all tiers; לֵבָב (full form) = inner totality — noted in Shema
- H5971 (עַם): "people" all tiers
- H8451 (תּוֹרָה): "law" L/M; "instruction/teaching" T — in 1:5 and 4:8, 44 this is the Mosaic corpus
- H4687 (מִצְוָה): "commandment(s)" all tiers
- H2706 (חֹק): "statute(s)" all tiers
- H4941 (מִשְׁפָּט): "rule(s)/ordinance(s)" L; "rule(s)" M; "justice/ruling" T depending on context
- H5707 (עֵד): "testimony/testimonies" all tiers
- H3519 (כָּבוֹד): "glory" all tiers
- H6918 (קָדוֹשׁ): "holy" all tiers
- H157 (אָהַב): "love" all tiers — in 6:5 this is covenantal command-love, not sentiment
- H3966 (מְאֹד): "might" L/M; "strength" T in 6:5 — the Shema's three-part formula
- H7307 (רוּחַ): "spirit" all tiers (2:30 — Sihon's spirit hardened)
- H2617 note: steadfast love appears in 5:10 with the Decalogue — "showing steadfast love to thousands"
- Ch. 1 note: Moses' speech is retrospective — all verbs are narrative past (waw-consecutive imperfect).
  L preserves the Hebrew reported-speech structure; T notes where quoted speech shifts register.
- Ch. 1:31 note: "as a man carries his son" — the father-son metaphor for God's wilderness care is
  theologically freighted; T draws this out.
- Ch. 2:30 note: God hardens Sihon's spirit (H7307 רוּחַ + H3824 לֵבָב) — divine sovereignty in
  conquest. T notes the parallel with Pharaoh's hardened heart in Exodus.
- Ch. 3:23-26 note: Moses' prayer to enter Canaan and God's refusal is one of the most poignant
  moments in the Torah. T renders Moses' plea with its theological weight intact.
- Ch. 4:12 note: "You heard the sound of words but saw no form" — the aniconic theology of
  Deuteronomy's core: God's self-revelation is verbal, not visual. T makes this explicit.
- Ch. 4:20 note: "iron furnace" for Egypt — the smelting metaphor implies both suffering and
  purification. T draws the refinement implication.
- Ch. 4:24 note: "consuming fire, jealous God" — H7067 (קַנָּא) is the divine-name form of jealousy;
  it denotes the exclusive covenant claim of a patron, not petty resentment. T notes this.
- Ch. 4:29 note: "with all your heart and with all your soul" — this formula anticipates the Shema
  (6:5) and anchors both texts in covenant loyalty. T notes the anticipation.
- Ch. 5:3 note: "Not with our fathers but with us" — present-tense covenant participation; each
  generation stands at Sinai. T makes this re-enactment theology explicit.
- Ch. 5:12-15 note: Deuteronomy's Sabbath rationale differs from Exodus 20:11 (creation rest);
  here the reason is the Exodus from slavery. T surfaces this theological shift.
- Ch. 5:29 note: "Oh that they had such a heart as this always" — divine pathos; God's longing for
  Israel's sustained obedience. T renders this as grief-tinged desire.
- Ch. 6:4 note (THE SHEMA): "The LORD our God, the LORD is one" — H259 (אֶחָד) = one/unique.
  The sentence is a declaration of YHWH's sole claim, not merely numerical monotheism. T renders
  the covenantal exclusivity: this God alone is Israel's God. The three-part formula of 6:5
  (heart/soul/might) encompasses the totality of a person — L preserves the tripartite structure;
  T renders it as whole-person covenant allegiance.
- Ch. 6:7 note: H8150 (שִׁנַּנְתָּם) = "sharpen/repeat earnestly" — the Piel intensive suggests
  drilling the words into children, not casual mention. T renders this as deliberate formation.
- Ch. 6:10-12 note: The danger-of-prosperity warning (cisterns, vineyards you did not dig/plant)
  is Deuteronomy's central anxiety: forgetting God when the gift replaces the Giver. T draws out
  the theological irony of abundance becoming amnesia.
- H2764 (חֵרֶם): "devoted to destruction" all tiers (2:34, 3:6) — the herem ban; L/M keep the
  technical term; T notes the theological rationale (removing contamination from covenant space).
- H5157 (נָחַל): "inherit/possess" — "inherit" when the theological dimension of gift is primary.
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
  "1": {
    "1": {
      "L": "These are the words that Moses spoke unto all Israel beyond the Jordan, in the wilderness, in the Arabah, over against Suph, between Paran and Tophel, and Laban, and Hazeroth, and Dizahab.",
      "M": "These are the words that Moses spoke to all Israel beyond the Jordan—in the wilderness, in the Arabah opposite Suph, between Paran and Tophel, Laban, Hazeroth, and Dizahab.",
      "T": "These are the words Moses spoke to all Israel on the east side of the Jordan—in the wilderness, in the Arabah plain facing Suph, between Paran and Tophel, Laban, Hazeroth, and Dizahab."
    },
    "2": {
      "L": "It is eleven days' journey from Horeb by the way of Mount Seir unto Kadesh-barnea.",
      "M": "It is eleven days' journey from Horeb by the way of Mount Seir to Kadesh-barnea.",
      "T": "(Eleven days' march from Horeb by way of Mount Seir brings you to Kadesh-barnea — yet Israel took forty years.)"
    },
    "3": {
      "L": "And it came to pass in the fortieth year, in the eleventh month, on the first day of the month, that Moses spoke unto the children of Israel according unto all that the LORD had given him in commandment unto them,",
      "M": "In the fortieth year, on the first day of the eleventh month, Moses spoke to the people of Israel according to all that the LORD had commanded him to tell them.",
      "T": "It was the fortieth year, the eleventh month, the first day of the month — and Moses addressed all Israel, saying everything the LORD had commanded him to say."
    },
    "4": {
      "L": "after he had slain Sihon the king of the Amorites, who dwelt in Heshbon, and Og the king of Bashan, who dwelt at Astaroth in Edrei.",
      "M": "This was after he had defeated Sihon king of the Amorites, who lived in Heshbon, and Og king of Bashan, who lived in Astaroth and Edrei.",
      "T": "This came after Israel had defeated Sihon king of the Amorites, who ruled from Heshbon, and Og king of Bashan, who ruled from Astaroth and Edrei."
    },
    "5": {
      "L": "Beyond the Jordan, in the land of Moab, Moses undertook to explain this law, saying,",
      "M": "Beyond the Jordan, in the land of Moab, Moses began to expound this law, saying,",
      "T": "East of the Jordan, in the land of Moab, Moses set himself to unfold this instruction, saying:"
    },
    "6": {
      "L": "The LORD our God spoke unto us in Horeb, saying, Ye have dwelt long enough at this mountain.",
      "M": "The LORD our God spoke to us at Horeb, saying, 'You have stayed long enough at this mountain.'",
      "T": "The LORD our God spoke to us at Horeb: 'You have been at this mountain long enough.'"
    },
    "7": {
      "L": "Turn you and take your journey, and go to the hill country of the Amorites, and unto all the places nigh thereunto, in the Arabah, in the hills, and in the lowland, and in the south, and by the sea side, to the land of the Canaanites, and unto Lebanon, unto the great river, the river Euphrates.",
      "M": "Turn and set out on your journey, and go to the hill country of the Amorites and to all their neighbors in the Arabah, in the hill country and in the lowland and in the Negeb and by the seacoast, the land of the Canaanites, and to Lebanon, as far as the great river, the river Euphrates.",
      "T": "Turn and move out. Go to the Amorite highlands and to every neighboring region — the Arabah plain, the hill country, the foothills, the Negeb, the coastland, the whole land of Canaan, and Lebanon, all the way to the great river Euphrates."
    },
    "8": {
      "L": "Behold, I have set the land before you: go in and possess the land which the LORD sware unto your fathers, to Abraham, to Isaac, and to Jacob, to give unto them and to their seed after them.",
      "M": "See, I have set the land before you. Go in and take possession of the land that the LORD swore to your fathers—to Abraham, to Isaac, and to Jacob—to give to them and to their offspring after them.",
      "T": "Look — I am placing the land before you. Enter and take possession of the land the LORD promised under oath to your ancestors Abraham, Isaac, and Jacob, swearing to give it to them and to their descendants."
    },
    "9": {
      "L": "And I spoke unto you at that time, saying, I am not able to bear you myself alone.",
      "M": "And I said to you at that time, 'I am not able to carry you by myself alone.'",
      "T": "At that time I told you: 'I cannot handle you alone.'"
    },
    "10": {
      "L": "The LORD your God hath multiplied you, and behold, ye are this day as the stars of heaven for multitude.",
      "M": "The LORD your God has multiplied you so that you are today as numerous as the stars of heaven.",
      "T": "The LORD your God has made you as numerous as the stars of the sky — see how many you are today."
    },
    "11": {
      "L": "The LORD, the God of your fathers, make you a thousand times as many as ye are, and bless you, as he hath promised you!",
      "M": "May the LORD, the God of your fathers, increase you a thousand times more and bless you, as he has promised you!",
      "T": "May the LORD, the God of your ancestors, multiply you a thousandfold and bless you exactly as he has promised!"
    },
    "12": {
      "L": "How can I myself alone bear your cumbrance and your burden and your strife?",
      "M": "How can I alone bear the weight of you, your burden, and your disputes?",
      "T": "But how can I alone carry the load of you — your needs, your conflicts, your endless disputes?"
    },
    "13": {
      "L": "Take you wise men and understanding, and known among your tribes, and I will make them rulers over you.",
      "M": "Choose wise, understanding, and experienced men from your tribes, and I will appoint them as your leaders.",
      "T": "Choose from your tribes men who are wise, discerning, and well-respected, and I will set them over you as leaders."
    },
    "14": {
      "L": "And ye answered me and said, The thing which thou hast spoken is good for us to do.",
      "M": "And you answered me, 'The thing you have said is good for us to do.'",
      "T": "You agreed: 'What you have said is the right thing to do.'"
    },
    "15": {
      "L": "So I took the chief of your tribes, wise men and known, and made them heads over you, captains over thousands, and captains over hundreds, and captains over fifties, and captains over tens, and officers among your tribes.",
      "M": "So I took the heads of your tribes, wise and experienced men, and appointed them as your leaders—commanders of thousands, hundreds, fifties, and tens, and officers throughout your tribes.",
      "T": "So I took the leading men of your tribes — wise, proven, respected — and installed them as your commanders: over thousands, hundreds, fifties, and tens, with officers throughout all your clans."
    },
    "16": {
      "L": "And I charged your judges at that time, saying, Hear the causes between your brethren, and judge righteously between every man and his brother, and the stranger that is with him.",
      "M": "And I charged your judges at that time: 'Hear the cases between your fellow Israelites, and judge fairly between a man and his brother and the foreigner living with him.'",
      "T": "I charged your judges at that time: 'Listen carefully to every dispute among your people — render fair verdicts between fellow Israelites and foreigners alike.'"
    },
    "17": {
      "L": "Ye shall not respect persons in judgment; ye shall hear the small and the great alike; ye shall not be afraid of the face of man; for the judgment is God's. And the cause that is too hard for you, ye shall bring unto me, and I will hear it.",
      "M": "You must not show partiality in judgment; hear the small and the great alike; do not be intimidated by anyone, for the judgment belongs to God. Whatever case is too difficult for you, bring to me and I will hear it.",
      "T": "Show no favoritism in court — hear the powerless and the powerful on equal terms. Fear no one, for when you judge you act on God's behalf. And when a case is beyond you, bring it to me."
    },
    "18": {
      "L": "And I commanded you at that time all the things which ye should do.",
      "M": "And I commanded you at that time all the things you should do.",
      "T": "I gave you all your instructions at that time."
    },
    "19": {
      "L": "And we journeyed from Horeb, and went through all that great and terrible wilderness which ye saw, by the way of the hill country of the Amorites, as the LORD our God commanded us; and we came to Kadesh-barnea.",
      "M": "Then we set out from Horeb and traveled through all that great and terrifying wilderness you have seen, on the way to the hill country of the Amorites, as the LORD our God commanded us. And we came to Kadesh-barnea.",
      "T": "We left Horeb and marched through that vast, fearsome wilderness you know so well — the road toward the Amorite highlands, just as the LORD our God had ordered — and arrived at Kadesh-barnea."
    },
    "20": {
      "L": "And I said unto you, Ye are come unto the hill country of the Amorites, which the LORD our God doth give unto us.",
      "M": "And I said to you, 'You have come to the hill country of the Amorites, which the LORD our God is giving us.'",
      "T": "I told you: 'You have reached the Amorite highlands — the very land the LORD our God is handing over to us.'"
    },
    "21": {
      "L": "Behold, the LORD thy God hath set the land before thee: go up, take possession, as the LORD, the God of thy fathers, hath spoken unto thee; fear not, neither be dismayed.",
      "M": "See, the LORD your God has set the land before you. Go up, take possession, as the LORD, the God of your fathers, has told you. Do not fear or be discouraged.",
      "T": "Look — the LORD your God has laid this land open before you. Go up and take it, just as the LORD your ancestors' God told you. Don't be afraid. Don't lose heart."
    },
    "22": {
      "L": "And ye came near unto me every one of you, and said, Let us send men before us, that they may search the land for us, and bring us word again of the way by which we must go up, and the cities unto which we shall come.",
      "M": "Then all of you came up to me and said, 'Let us send men ahead to explore the land for us and bring back a report about which route to take and what cities we will encounter.'",
      "T": "Then all of you came to me with a request: 'Let us send scouts ahead to survey the land and bring back word about what route to take and what towns we will face.'"
    },
    "23": {
      "L": "And the thing pleased me well; and I took twelve men of you, one man for every tribe.",
      "M": "The proposal seemed good to me, so I took twelve men from among you, one from each tribe.",
      "T": "I thought it a good plan, so I selected twelve men — one from each tribe."
    },
    "24": {
      "L": "And they turned and went up into the hill country, and came unto the valley of Eshcol, and spied it out.",
      "M": "They set out and went up into the hill country, came to the Valley of Eshcol, and scouted it out.",
      "T": "They went up into the highlands, reached the Eshcol Valley, and thoroughly surveyed it."
    },
    "25": {
      "L": "And they took in their hands of the fruit of the land, and brought it down unto us, and brought us word again, and said, It is a good land which the LORD our God doth give unto us.",
      "M": "They took some of the fruit of the land in their hands and brought it down to us, and they reported back, saying, 'It is a good land that the LORD our God is giving us.'",
      "T": "They brought back samples of the land's produce and reported: 'It is a good land — the LORD our God is truly giving it to us.'"
    },
    "26": {
      "L": "Yet ye would not go up, but rebelled against the commandment of the LORD your God.",
      "M": "But you would not go up, and you rebelled against the command of the LORD your God.",
      "T": "But you refused to go. You defied the direct command of the LORD your God."
    },
    "27": {
      "L": "And ye murmured in your tents, and said, Because the LORD hated us, he hath brought us forth out of the land of Egypt, to deliver us into the hand of the Amorites, to destroy us.",
      "M": "And you grumbled in your tents, saying, 'Because the LORD hated us, he brought us out of Egypt to hand us over to the Amorites, to destroy us.'",
      "T": "You grumbled in your tents: 'It's because the LORD hates us that he led us out of Egypt — just to hand us to the Amorites to be slaughtered.'"
    },
    "28": {
      "L": "Whither shall we go up? our brethren have made our heart to melt, saying, The people are greater and taller than we; the cities are great and walled up to heaven; and moreover we have seen the sons of the Anakim there.",
      "M": "Where can we go? Our brothers have made our hearts melt, saying, \"The people are greater and taller than we are; the cities are large and fortified up to heaven; and we even saw Anakite giants there.\"",
      "T": "Where are we even going? Our own brothers have drained all our courage: 'The people there are bigger and stronger than us. Their cities have walls reaching to the sky. We saw giants — Anakites — with our own eyes.'"
    },
    "29": {
      "L": "Then I said unto you, Dread not, neither be afraid of them.",
      "M": "Then I said to you, 'Do not be terrified or afraid of them.'",
      "T": "I told you: 'Don't be terrified. Don't be afraid of them.'"
    },
    "30": {
      "L": "The LORD your God who goeth before you, he shall fight for you, according to all that he did for you in Egypt before your eyes,",
      "M": "The LORD your God who goes before you will himself fight for you, just as he did for you in Egypt before your eyes,",
      "T": "The LORD your God goes before you — he will fight for you, exactly as he fought for you in Egypt when you watched with your own eyes."
    },
    "31": {
      "L": "and in the wilderness, where thou hast seen how that the LORD thy God bare thee, as a man doth bear his son, in all the way that ye went, until ye came unto this place.",
      "M": "and in the wilderness, where you saw how the LORD your God carried you, as a man carries his son, all the way that you traveled until you reached this place.",
      "T": "And in the wilderness you saw it firsthand — the LORD your God carried you the whole way, the way a father lifts and carries his child, all the road from Egypt to this very place."
    },
    "32": {
      "L": "Yet in this thing ye did not believe the LORD your God,",
      "M": "Yet in spite of all this you did not trust the LORD your God,",
      "T": "And yet, after all that, you still did not trust the LORD your God."
    },
    "33": {
      "L": "who went before you in the way, to seek you out a place to pitch your tents in, in fire by night, to shew you by what way ye should go, and in the cloud by day.",
      "M": "who went before you on the way to find you a place to camp—in fire by night to show you the route, and in the cloud by day.",
      "T": "The very God who walked ahead of you, scouting out your campsites — guiding you with fire at night to show the way and with cloud cover by day."
    },
    "34": {
      "L": "And the LORD heard the voice of your words, and was wroth, and sware, saying,",
      "M": "And the LORD heard the sound of your words and was angry, and he swore, saying,",
      "T": "The LORD heard every word you said. His anger blazed, and he swore:"
    },
    "35": {
      "L": "Surely there shall not one of these men of this evil generation see that good land, which I sware to give unto your fathers,",
      "M": "Not one of the men of this wicked generation shall see the good land that I swore to give to your fathers,",
      "T": "'Not one person from this wicked generation will ever see the good land I swore to give your ancestors —'"
    },
    "36": {
      "L": "save Caleb the son of Jephunneh; he shall see it; and to him will I give the land that he hath trodden upon, and to his children, because he hath wholly followed the LORD.",
      "M": "except Caleb the son of Jephunneh. He shall see it, and to him and to his children I will give the land he has trodden, because he has wholly followed the LORD.",
      "T": "'— no one except Caleb son of Jephunneh. He will see it. I will give him and his descendants the ground his feet have walked on, because he followed the LORD with an undivided heart.'"
    },
    "37": {
      "L": "Also the LORD was angry with me for your sakes, saying, Thou also shalt not go in thither.",
      "M": "The LORD was also angry with me on your account, saying, 'You also shall not go in there.'",
      "T": "The LORD was also angry with me on your account: 'You, too, will not enter.'"
    },
    "38": {
      "L": "Joshua the son of Nun, which standeth before thee, he shall go in thither: encourage him; for he shall cause Israel to inherit it.",
      "M": "Joshua son of Nun, who stands before you—he shall go in. Encourage him, for he will lead Israel to inherit the land.",
      "T": "Joshua son of Nun, who serves at your side — he will go in. Strengthen him, because he is the one who will settle Israel in the land.'"
    },
    "39": {
      "L": "Moreover your little ones, which ye said should be a prey, and your children, which in that day had no knowledge of good or evil, they shall go in thither, and unto them will I give it, and they shall possess it.",
      "M": "And your little ones, who you said would become prey, and your children who today have no knowledge of good or evil—they shall go in. I will give it to them, and they shall possess it.",
      "T": "Your young children — the ones you said would be captured, who cannot yet tell good from evil — they will enter. I will give the land to them, and they will take possession of it."
    },
    "40": {
      "L": "But as for you, turn you, and take your journey into the wilderness by the way of the Red Sea.",
      "M": "But as for you, turn back and journey into the wilderness in the direction of the Red Sea.",
      "T": "As for you — turn around and head back into the wilderness toward the Red Sea."
    },
    "41": {
      "L": "Then ye answered and said unto me, We have sinned against the LORD, we will go up and fight, according to all that the LORD our God commanded us. And ye girded on every man his weapons of war, and were ready to go up into the hill country.",
      "M": "Then you answered me, 'We have sinned against the LORD. We will go up and fight, just as the LORD our God commanded us.' And every one of you put on his weapons of war and thought it easy to go up into the hill country.",
      "T": "You turned around then and told me: 'We have sinned against the LORD. Now we will go up and fight — exactly as the LORD our God commanded.' You buckled on your weapons, casually, as if marching up to that hill country were nothing."
    },
    "42": {
      "L": "And the LORD said unto me, Say unto them, Go not up, neither fight; for I am not among you; lest ye be smitten before your enemies.",
      "M": "But the LORD said to me, 'Tell them: Do not go up, and do not fight, for I am not in your midst. Otherwise you will be defeated before your enemies.'",
      "T": "But the LORD told me: 'Tell them — don't go up, don't fight. I am not with you. If you go, your enemies will crush you.'"
    },
    "43": {
      "L": "So I spake unto you; and ye would not hear; but ye rebelled against the commandment of the LORD, and went presumptuously up into the hill country.",
      "M": "So I told you, but you would not listen; you rebelled against the LORD's command and arrogantly went up into the hill country.",
      "T": "I told you all of this. You refused to listen. You defied the LORD's command and marched into those hills with reckless pride."
    },
    "44": {
      "L": "And the Amorites, which dwelt in that mountain, came out against you, and chased you, as bees do, and beat you down in Seir, even unto Hormah.",
      "M": "And the Amorites who lived in those hills came out against you and chased you like bees, beating you back through Seir as far as Hormah.",
      "T": "The Amorites who lived in those hills swarmed out at you like bees, driving you back through Seir all the way to Hormah."
    },
    "45": {
      "L": "And ye returned and wept before the LORD; but the LORD would not hearken to your voice, nor give ear unto you.",
      "M": "And you came back and wept before the LORD, but the LORD would not listen to your voice or pay attention to you.",
      "T": "You came back weeping before the LORD — but the LORD would not hear. He had no ear for you."
    },
    "46": {
      "L": "So ye abode in Kadesh many days, according unto the days that ye abode there.",
      "M": "So you remained at Kadesh a long time — all those days you stayed there.",
      "T": "And so you settled at Kadesh for a long time — all those wasted days."
    }
  },
  "2": {
    "1": {
      "L": "Then we turned, and took our journey into the wilderness by the way of the Red Sea, as the LORD spake unto me: and we compassed mount Seir many days.",
      "M": "Then we turned and journeyed into the wilderness in the direction of the Red Sea, as the LORD had told me, and we traveled around Mount Seir for many days.",
      "T": "We turned back toward the Red Sea wilderness, as the LORD had directed me, and spent many days circling Mount Seir."
    },
    "2": {
      "L": "And the LORD spake unto me, saying,",
      "M": "Then the LORD said to me,",
      "T": "Then the LORD spoke to me:"
    },
    "3": {
      "L": "Ye have compassed this mountain long enough: turn you northward.",
      "M": "'You have been going around this mountain long enough. Turn north.'",
      "T": "'You have circled this mountain long enough. Turn north.'"
    },
    "4": {
      "L": "And command thou the people, saying, Ye are to pass through the border of your brethren the children of Esau, which dwell in Seir; and they shall be afraid of you: take ye good heed unto yourselves therefore;",
      "M": "Command the people: You are about to pass through the territory of your brothers, the Esau people who live in Seir. They will be afraid of you, so be very careful.",
      "T": "Give this order to the people: You are about to pass through the land of your brothers, Esau's descendants who live in Seir. They will be wary of you, so take great care."
    },
    "5": {
      "L": "contend not with them; for I will not give you of their land, no, not so much as for the sole of the foot to tread on; because I have given mount Seir unto Esau for a possession.",
      "M": "Do not provoke them, for I will not give you any of their land—not even enough to set a foot on—because I have given Mount Seir to Esau as a possession.",
      "T": "Do not pick a fight with them. I will not give you so much as a footprint of their territory, because I gave Mount Seir to Esau as his inheritance."
    },
    "6": {
      "L": "Ye shall purchase food of them for money, that ye may eat; and ye shall also buy water of them for money, that ye may drink.",
      "M": "You shall buy food from them with money so you may eat, and you shall also buy water from them with money so you may drink.",
      "T": "Pay for any food you eat from them, and pay for any water you drink — money for everything."
    },
    "7": {
      "L": "For the LORD thy God hath blessed thee in all the work of thy hand: he hath known thy walking through this great wilderness: these forty years the LORD thy God hath been with thee; thou hast lacked nothing.",
      "M": "For the LORD your God has blessed you in all the work of your hands. He has watched over your journey through this great wilderness. These forty years the LORD your God has been with you, and you have lacked nothing.",
      "T": "The LORD your God has blessed everything your hands have done. He has followed every step of your march through this immense wilderness. Forty years — and the LORD your God has been with you every day. You have never gone without."
    },
    "8": {
      "L": "So we passed by from our brethren the children of Esau, which dwelt in Seir, from the way of the Arabah from Elath, and from Ezion-geber. And we turned and passed by the way of the wilderness of Moab.",
      "M": "So we went past our brothers, the Esau people who live in Seir, away from the Arabah road from Elath and Ezion-geber, and turned and went in the direction of the wilderness of Moab.",
      "T": "We skirted past our brothers the Esau clan living in Seir, leaving the Arabah road near Elath and Ezion-geber behind us, and turned toward the Moab wilderness."
    },
    "9": {
      "L": "And the LORD said unto me, Distress not Moab, neither contend with them in battle: for I will not give thee of his land for a possession; because I have given Ar unto the children of Lot for a possession.",
      "M": "And the LORD said to me, 'Do not harass Moab or engage them in battle, for I will not give you any of their land as a possession, because I have given Ar to the people of Lot as a possession.'",
      "T": "The LORD told me: 'Do not threaten Moab or provoke them to fight. I will not give you any of their land, because I gave Ar to Lot's descendants as their inheritance.'"
    },
    "10": {
      "L": "(The Emim dwelt therein aforetime, a people great, and many, and tall, as the Anakim:",
      "M": "(The Emim formerly lived there—a people great, numerous, and tall as the Anakim.",
      "T": "(Formerly the Emim had lived there — a great, numerous people, as tall as the Anakim."
    },
    "11": {
      "L": "these also are accounted Rephaim, as the Anakim; but the Moabites call them Emim.",
      "M": "They are counted as Rephaim, like the Anakim, though the Moabites call them Emim.",
      "T": "Like the Anakim, they were counted as Rephaim, though the Moabites called them Emim."
    },
    "12": {
      "L": "And in Seir dwelt the Horites aforetime; but the children of Esau succeeded them, and destroyed them from before them, and dwelt in their stead; as Israel did unto the land of his possession, which the LORD gave unto them.)",
      "M": "The Horites also formerly lived in Seir, but the people of Esau dispossessed them, destroyed them, and settled in their place—just as Israel did to the land of their possession that the LORD gave them.)",
      "T": "In Seir, the Horites had lived earlier, but Esau's people drove them out, annihilated them, and took their place — just as Israel did in the land the LORD gave them.)"
    },
    "13": {
      "L": "Now rise up, said I, and get you over the brook Zered. And we went over the brook Zered.",
      "M": "The LORD said, 'Now rise up and cross the brook Zered.' So we crossed the brook Zered.",
      "T": "Then came the order: 'Rise up and cross the Zered Valley.' So we crossed it."
    },
    "14": {
      "L": "And the days in which we came from Kadesh-barnea, until we were come over the brook Zered, were thirty and eight years; until all the generation of the men of war were wasted out from among the host, as the LORD sware unto them.",
      "M": "The time between leaving Kadesh-barnea and crossing the brook Zered was thirty-eight years, until the entire generation of fighting men had died out from the camp, as the LORD had sworn would happen.",
      "T": "From the departure at Kadesh-barnea to the crossing of the Zered was thirty-eight years — until every soldier from that condemned generation had died out of the camp, just as the LORD had sworn."
    },
    "15": {
      "L": "For indeed the hand of the LORD was against them, to discomfit them from among the host, until they were consumed.",
      "M": "For indeed the LORD's hand was against them, to destroy them from the camp, until they had all perished.",
      "T": "The LORD's own hand was working against them — picking them off from the camp until the last one was gone."
    },
    "16": {
      "L": "So it came to pass, when all the men of war were consumed and dead from among the people,",
      "M": "So when all the men of war had finally died out from among the people,",
      "T": "Once the last of those soldiers had died,"
    },
    "17": {
      "L": "that the LORD spake unto me, saying,",
      "M": "the LORD said to me,",
      "T": "the LORD spoke to me:"
    },
    "18": {
      "L": "Thou art to pass over through Ar, the border of Moab, this day:",
      "M": "'Today you are to cross the border of Moab at Ar,'",
      "T": "'Today you cross into Moab at Ar.'"
    },
    "19": {
      "L": "and when thou comest nigh over against the children of Ammon, distress them not, nor contend with them: for I will not give thee of the land of the children of Ammon any possession; because I have given it unto the children of Lot for a possession.",
      "M": "'and when you approach the territory of the Ammonites, do not harass them or engage them in battle, for I will not give you any of the land of the Ammonites as a possession, because I have given it to the sons of Lot as a possession.'",
      "T": "'When you come near Ammonite territory, do not threaten them and do not attack them. I will not give you any part of their land, because I gave it to Lot's descendants.'"
    },
    "20": {
      "L": "(That also is accounted a land of Rephaim: Rephaim dwelt therein aforetime; but the Ammonites call them Zamzummim;",
      "M": "(That region is also counted as land of the Rephaim. Rephaim formerly lived there, though the Ammonites called them Zamzummim.",
      "T": "(That region was also known as Rephaim territory. Rephaim once lived there — the Ammonites called them Zamzummim."
    },
    "21": {
      "L": "a people great, and many, and tall, as the Anakim; but the LORD destroyed them before them; and they succeeded them, and dwelt in their stead:",
      "M": "They were a people great, numerous, and tall as the Anakim; but the LORD destroyed them before the Ammonites, who dispossessed them and settled in their place,",
      "T": "They were as great and tall as the Anakim — but the LORD swept them away before the Ammonites, who took over and settled the land."
    },
    "22": {
      "L": "as he did for the children of Esau, which dwelt in Seir, when he destroyed the Horites from before them; and they succeeded them, and dwelt in their stead even unto this day.",
      "M": "as he did for the people of Esau who live in Seir, when he destroyed the Horites before them; they dispossessed them and settled in their place to this day.)",
      "T": "The same thing he did for the Esau clan in Seir — he cleared out the Horites, and Esau's people took over. They are still there today.)"
    },
    "23": {
      "L": "and the Avvim, which dwelt in villages unto Gaza, the Caphtorim, which came forth from Caphtor, destroyed them, and dwelt in their stead.)",
      "M": "As for the Avvim, who lived in villages as far as Gaza, the Caphtorim, coming from Caphtor, destroyed them and settled in their place.)",
      "T": "And the Avvim who lived in villages all the way to Gaza — the Caphtorim came out from Caphtor and wiped them out, taking over their territory.)"
    },
    "24": {
      "L": "Rise ye up, take your journey, and pass over the river Arnon: behold, I have given into thine hand Sihon the Amorite, king of Heshbon, and his land: begin to possess it, and contend with him in battle.",
      "M": "'Rise up, set out on your journey, and cross the Valley of the Arnon. Look — I have given into your hand Sihon the Amorite, king of Heshbon, and his land. Begin to take possession, and engage him in battle.'",
      "T": "'Move out and cross the Arnon Valley. I am handing over to you Sihon the Amorite king of Heshbon and his whole land. Begin the conquest. Engage him in battle.'"
    },
    "25": {
      "L": "This day will I begin to put the dread of thee and the fear of thee upon the peoples that are under the whole heaven, who shall hear report of thee, and shall tremble, and be in anguish because of thee.",
      "M": "'This day I will begin to put the dread and fear of you upon all the peoples under heaven. When they hear news of you, they will tremble and writhe in anguish because of you.'",
      "T": "'Starting today I will spread terror of you across every nation under heaven. Word of you will reach them and they will shake — panic-stricken at the sound of your name.'"
    },
    "26": {
      "L": "And I sent messengers out of the wilderness of Kedemoth unto Sihon king of Heshbon with words of peace, saying,",
      "M": "So I sent messengers from the wilderness of Kedemoth to Sihon king of Heshbon with an offer of peace, saying,",
      "T": "I sent envoys from the Kedemoth wilderness to Sihon king of Heshbon with a peaceful message:"
    },
    "27": {
      "L": "Let me pass through thy land: I will go along by the high way, I will neither turn unto the right hand nor to the left.",
      "M": "'Let me pass through your land. I will travel only on the road, turning neither to the right nor to the left.'",
      "T": "'Let us pass through your land. We will stay on the main road — we will not turn right or left.'"
    },
    "28": {
      "L": "Thou shalt sell me food for money, that I may eat; and give me water for money, that I may drink: only let me pass through on my feet;",
      "M": "'You shall sell me food for money so I may eat, and give me water for money so I may drink. I only want to pass through on foot,'",
      "T": "'Sell us food for money and water for money — we only want to walk through.'"
    },
    "29": {
      "L": "as the children of Esau which dwell in Seir, and the Moabites which dwell in Ar, did unto me; until I shall pass over Jordan into the land which the LORD our God giveth us.",
      "M": "'just as the sons of Esau who live in Seir and the Moabites who live in Ar did for me—until I cross the Jordan into the land the LORD our God is giving us.'",
      "T": "'The Esau clan in Seir and the Moabites in Ar did the same for us. We just want to cross the Jordan into the land the LORD our God is giving us.'"
    },
    "30": {
      "L": "But Sihon king of Heshbon would not let us pass by him: for the LORD thy God hardened his spirit, and made his heart obstinate, that he might deliver him into thy hand, as appeareth this day.",
      "M": "But Sihon king of Heshbon would not let us pass through, for the LORD your God had made his spirit obstinate and his heart stubborn, in order to give him into your hand, as it stands today.",
      "T": "But Sihon king of Heshbon refused to let us through. The LORD your God had hardened his will and made his heart unyielding — just as he had done with Pharaoh — so that Sihon would be delivered into your hands, as happened that very day."
    },
    "31": {
      "L": "And the LORD said unto me, Behold, I have begun to deliver up Sihon and his land before thee: begin to possess, that thou mayest inherit his land.",
      "M": "And the LORD said to me, 'Behold, I have begun to give Sihon and his land over to you. Begin to take possession, that you may occupy his land.'",
      "T": "The LORD told me: 'I have already started delivering Sihon and his land to you. Begin the conquest — take his land as your own.'"
    },
    "32": {
      "L": "Then Sihon came out against us, he and all his people, unto battle at Jahaz.",
      "M": "Then Sihon came out against us, he and all his people, to do battle at Jahaz.",
      "T": "Sihon marched out to meet us with his whole army at Jahaz."
    },
    "33": {
      "L": "And the LORD our God delivered him up before us; and we smote him, and his sons, and all his people.",
      "M": "And the LORD our God delivered him over to us, and we defeated him, his sons, and all his people.",
      "T": "The LORD our God handed him over to us. We struck him down — him, his sons, his entire army."
    },
    "34": {
      "L": "And we took all his cities at that time, and utterly destroyed every city, the men, and the women, and the little ones; we left none remaining:",
      "M": "We captured all his cities at that time and devoted every city to destruction—men, women, and children. We left no survivors.",
      "T": "We captured every one of his cities and placed them under the ban — men, women, children, every soul. Not one survivor."
    },
    "35": {
      "L": "only the cattle we took for a prey unto ourselves, with the spoil of the cities which we had taken.",
      "M": "Only the livestock we took as spoil for ourselves, along with the plunder of the captured cities.",
      "T": "Only the livestock and the spoil of the cities we kept for ourselves."
    },
    "36": {
      "L": "From Aroer, which is on the edge of the valley of Arnon, and from the city that is in the valley, even unto Gilead, there was not a city too high for us; the LORD our God delivered all unto us:",
      "M": "From Aroer on the edge of the Valley of the Arnon, and from the city in the valley, as far as Gilead—there was not a city too strong for us. The LORD our God gave them all into our hands.",
      "T": "From Aroer on the rim of the Arnon Valley, from the city in the gorge, all the way to Gilead — every single city fell. Not one stood against us. The LORD our God delivered them all."
    },
    "37": {
      "L": "Only unto the land of the children of Ammon thou camest not near; unto all the side of the river Jabbok, and the cities of the hill country, and wheresoever the LORD our God forbade us.",
      "M": "Only to the land of the Ammonites you did not go near—all along the bank of the river Jabbok and the cities of the hill country, whatever the LORD our God had forbidden us.",
      "T": "Only Ammonite territory we did not touch — the whole Jabbok riverbank and the highlands beyond, everywhere the LORD our God had placed off limits."
    }
  },
  "3": {
    "1": {
      "L": "Then we turned, and went up the way to Bashan: and Og the king of Bashan came out against us, he and all his people, to battle at Edrei.",
      "M": "Then we turned and went up the road to Bashan. And Og king of Bashan came out against us, he and all his people, to battle at Edrei.",
      "T": "We turned and marched north toward Bashan. Og king of Bashan came out to meet us at Edrei — him and his entire army."
    },
    "2": {
      "L": "And the LORD said unto me, Fear him not: for I have delivered him, and all his people, and his land, into thy hand; and thou shalt do unto him as thou didst unto Sihon king of the Amorites, which dwelt at Heshbon.",
      "M": "But the LORD said to me, 'Do not fear him, for I have given him and all his people and his land into your hand. Do to him as you did to Sihon king of the Amorites who lived at Heshbon.'",
      "T": "The LORD told me: 'Don't be afraid of him. I am handing him over to you — him, his whole army, his entire land. Deal with him the same way you dealt with Sihon the Amorite king of Heshbon.'"
    },
    "3": {
      "L": "So the LORD our God delivered into our hands Og also, the king of Bashan, and all his people: and we smote him until none was left to him remaining.",
      "M": "So the LORD our God gave into our hands Og also, king of Bashan, and all his people. We struck him down until not one survivor remained.",
      "T": "The LORD our God delivered Og king of Bashan into our hands as well — him and every last one of his soldiers. We destroyed them completely."
    },
    "4": {
      "L": "And we took all his cities at that time; there was not a city which we took not from them; threescore cities, all the region of Argob, the kingdom of Og in Bashan.",
      "M": "We captured all his cities at that time. There was not a city we did not take from them—sixty cities, the entire region of Argob, the kingdom of Og in Bashan.",
      "T": "We seized all his cities at that time — every single one, sixty cities in all, the whole Argob region, Og's entire kingdom in Bashan."
    },
    "5": {
      "L": "All these cities were fenced with high walls, gates, and bars; besides exceeding many unwalled towns.",
      "M": "All these were cities fortified with high walls, gates, and bars, besides very many unwalled villages.",
      "T": "Every one of these cities was walled — massive walls with reinforced gates — not to mention the many open villages around them."
    },
    "6": {
      "L": "And we utterly destroyed them, as we did unto Sihon king of Heshbon, utterly destroying the men, women, and children of every city.",
      "M": "We devoted them to destruction, as we had done to Sihon king of Heshbon, putting every city under the ban—men, women, and children.",
      "T": "We placed them all under the ban, as we had done with Sihon at Heshbon — men, women, and children devoted to destruction."
    },
    "7": {
      "L": "But all the cattle, and the spoil of the cities, we took for a prey to ourselves.",
      "M": "But all the livestock and the plunder from the cities we kept for ourselves.",
      "T": "Only the livestock and the plunder of the cities we kept."
    },
    "8": {
      "L": "And we took at that time out of the hand of the two kings of the Amorites the land that was beyond Jordan, from the valley of Arnon unto mount Hermon;",
      "M": "At that time we took the land east of the Jordan from the two Amorite kings—from the Valley of the Arnon to Mount Hermon.",
      "T": "So at that time we took from these two Amorite kings all the land east of the Jordan — from the Arnon gorge all the way to Mount Hermon."
    },
    "9": {
      "L": "(which Hermon the Sidonians call Sirion; and the Amorites call it Senir;)",
      "M": "(Hermon is called Sirion by the Sidonians and Senir by the Amorites.)",
      "T": "(The Sidonians call Hermon 'Sirion'; the Amorites call it 'Senir.')"
    },
    "10": {
      "L": "all the cities of the plain, and all Gilead, and all Bashan, unto Salecah and Edrei, cities of the kingdom of Og in Bashan.",
      "M": "—all the cities of the plateau, all Gilead, and all Bashan as far as Salecah and Edrei, cities of Og's kingdom in Bashan.",
      "T": "Every city on the tableland, all of Gilead, all of Bashan as far as Salecah and Edrei — all of it had been Og's kingdom."
    },
    "11": {
      "L": "(For only Og king of Bashan remained of the remnant of the Rephaim; behold, his bedstead was a bedstead of iron; is it not in Rabbah of the children of Ammon? nine cubits was the length thereof, and four cubits the breadth of it, after the cubit of a man.)",
      "M": "(For only Og king of Bashan was left of the remnant of the Rephaim. His bed was a bed of iron—is it not still in Rabbah of the Ammonites?—nine cubits long and four cubits wide, by the common cubit.)",
      "T": "(Og king of Bashan was the last of the Rephaim. His iron bed is a matter of record — it is still in Rabbah of the Ammonites, nine standard cubits long and four wide.)"
    },
    "12": {
      "L": "And this land, which we possessed at that time, from Aroer, which is by the river Arnon, and half mount Gilead, and the cities thereof, gave I unto the Reubenites and to the Gadites:",
      "M": "This land that we took possession of at that time—from Aroer by the Arnon River and half the hill country of Gilead with its cities—I gave to the Reubenites and the Gadites.",
      "T": "The territory we took — from Aroer on the Arnon and the southern half of Gilead with its towns — I assigned to the Reubenites and Gadites."
    },
    "13": {
      "L": "and the rest of Gilead, and all Bashan, the kingdom of Og, gave I unto the half tribe of Manasseh; all the region of Argob, with all Bashan, which was called the land of Rephaim.",
      "M": "The rest of Gilead and all Bashan, the kingdom of Og, I gave to the half-tribe of Manasseh. (The whole region of Argob in Bashan was called the land of the Rephaim.",
      "T": "The rest of Gilead and all Bashan — Og's entire kingdom — I gave to the half-tribe of Manasseh. (All the Argob region in Bashan bore the name 'land of the Rephaim.'"
    },
    "14": {
      "L": "Jair the son of Manasseh took all the region of Argob, unto the border of the Geshurites and the Maacathites; and called them, even Bashan, after his own name, Havvoth-jair, unto this day.)",
      "M": "Jair the Manassite took all the region of Argob as far as the border of the Geshurites and the Maacathites. He named those villages, that is, Bashan, Havvoth-jair—as it is still called today.)",
      "T": "Jair son of Manasseh captured all the Argob region up to the Geshurite and Maacathite borders and named those settlements Havvoth-jair — 'Jair's Villages' — a name they still carry today.)"
    },
    "15": {
      "L": "And I gave Gilead unto Machir.",
      "M": "To Machir I gave Gilead.",
      "T": "Gilead I gave to Machir."
    },
    "16": {
      "L": "And unto the Reubenites and unto the Gadites I gave from Gilead even unto the river Arnon, the middle of the river, and the border thereof, even unto the river Jabbok, which is the border of the children of Ammon;",
      "M": "To the Reubenites and Gadites I gave the territory from Gilead down to the Arnon Valley, with the middle of the valley as the boundary, as far as the Jabbok River, which is the Ammonite border.",
      "T": "To Reuben and Gad I gave the territory from Gilead south to the Arnon — with the valley's midpoint as the dividing line — as far north as the Jabbok, which marks the Ammonite boundary."
    },
    "17": {
      "L": "the Arabah also, and the Jordan, and the border thereof, from Chinnereth even unto the sea of the Arabah, even the Salt Sea, under the slopes of Pisgah eastward.",
      "M": "The Arabah as well, with the Jordan as the western boundary, from Chinnereth down to the Sea of the Arabah, the Salt Sea, below the slopes of Pisgah on the east.",
      "T": "Also the Arabah plain, bounded on the west by the Jordan — from Lake Chinnereth south to the Arabah Sea, the Salt Sea, along the base of the Pisgah slopes on the eastern side."
    },
    "18": {
      "L": "And I commanded you at that time, saying, The LORD your God hath given you this land to possess it: ye shall pass over armed before your brethren the children of Israel, all that are meet for the war.",
      "M": "At that time I commanded you: The LORD your God has given you this land to possess. All your fighting men shall cross over armed before your fellow Israelites.",
      "T": "At that time I gave this charge: The LORD your God has given you this land. Every fighting man among you must cross over in full battle array before your fellow Israelites."
    },
    "19": {
      "L": "But your wives, and your little ones, and your cattle, (for I know that ye have much cattle,) shall abide in your cities which I have given you;",
      "M": "But your wives, your little ones, and your livestock (I know you have much livestock) shall remain in the cities I have given you,",
      "T": "Your wives, children, and livestock — and I know you have substantial herds — stay in the towns I have given you."
    },
    "20": {
      "L": "until the LORD have given rest unto your brethren, as well as unto you, and until they also possess the land which the LORD your God giveth them beyond the Jordan: and then shall ye return every man unto his possession which I have given you.",
      "M": "until the LORD gives rest to your fellow Israelites as he has given rest to you, and they too take possession of the land that the LORD your God is giving them across the Jordan. After that, each of you may return to the possession I have given you.",
      "T": "Stay there until the LORD gives your fellow Israelites the same secure rest he has given you, and they too have settled into the land the LORD your God is granting them west of the Jordan. Then you may each return home to your own inheritance."
    },
    "21": {
      "L": "And I commanded Joshua at that time, saying, Thine eyes have seen all that the LORD your God hath done unto these two kings: so shall the LORD do unto all the kingdoms whither thou goest.",
      "M": "At that time I commanded Joshua: 'Your eyes have seen everything the LORD your God has done to these two kings. The LORD will do the same to all the kingdoms you are about to enter.'",
      "T": "I also charged Joshua at that time: 'You have seen with your own eyes what the LORD your God did to these two kings. He will do the same to every kingdom you cross into.'"
    },
    "22": {
      "L": "Ye shall not fear them: for the LORD your God he shall fight for you.",
      "M": "'Do not fear them, for the LORD your God himself fights for you.'",
      "T": "'Don't be afraid of any of them — the LORD your God is the one doing the fighting.'"
    },
    "23": {
      "L": "And I besought the LORD at that time, saying,",
      "M": "And I pleaded with the LORD at that time, saying,",
      "T": "At that time I pleaded with the LORD:"
    },
    "24": {
      "L": "O Lord GOD, thou hast begun to shew thy servant thy greatness, and thy mighty hand: for what god is there in heaven or in earth, that can do according to thy works, and according to thy mighty acts?",
      "M": "'O Lord GOD, you have only begun to show your servant your greatness and your mighty hand. What god is there in heaven or on earth who can perform deeds and mighty acts like yours?'",
      "T": "'O Lord GOD — you have barely begun to display your greatness and the power of your hand to your servant. What god exists, anywhere in heaven or earth, who can do anything remotely like what you do?'"
    },
    "25": {
      "L": "I pray thee, let me go over, and see the good land that is beyond Jordan, that goodly mountain, and Lebanon.",
      "M": "'Please let me cross over and see the good land beyond the Jordan—that good hill country and Lebanon.'",
      "T": "'Please — let me cross over and see this good land beyond the Jordan, those beautiful highlands, and Lebanon.'"
    },
    "26": {
      "L": "But the LORD was wroth with me for your sakes, and hearkened not unto me: and the LORD said unto me, Let it suffice thee; speak no more unto me of this matter.",
      "M": "But the LORD was angry with me on your account and would not listen to me. The LORD said to me, 'That is enough from you; do not speak to me of this matter again.'",
      "T": "But the LORD was angry with me on your account and would not hear me. 'Enough,' the LORD said. 'Do not bring this up again.'"
    },
    "27": {
      "L": "Get thee up into the top of Pisgah, and lift up thine eyes westward, and northward, and southward, and eastward, and behold it with thine eyes: for thou shalt not go over this Jordan.",
      "M": "'Go up to the top of Pisgah and look westward, northward, southward, and eastward. Look at it carefully with your eyes, for you shall not cross this Jordan.'",
      "T": "'Go up to the summit of Pisgah. Look west, north, south, east — drink it in with your eyes. But you will not cross this Jordan.'"
    },
    "28": {
      "L": "But charge Joshua, and encourage him, and strengthen him: for he shall go over before this people, and he shall cause them to inherit the land which thou shalt see.",
      "M": "'But commission Joshua, and encourage him and strengthen him, for he shall cross over at the head of this people and shall lead them to inherit the land you will see.'",
      "T": "'Instead, appoint Joshua. Encourage him and make him strong — he is the one who will lead this people across and settle them in the land you see from that peak.'"
    },
    "29": {
      "L": "So we abode in the valley over against Beth-peor.",
      "M": "So we remained in the valley opposite Beth-peor.",
      "T": "And we stayed in the valley facing Beth-peor."
    }
  },
  "4": {
    "1": {
      "L": "And now, O Israel, hearken unto the statutes and unto the ordinances, which I teach you, to do them; that ye may live, and go in and possess the land which the LORD, the God of your fathers, giveth you.",
      "M": "And now, O Israel, listen to the statutes and rules I am teaching you to follow, so that you may live and go in and take possession of the land that the LORD, the God of your fathers, is giving you.",
      "T": "And now, Israel — hear the statutes and rulings I am teaching you to live by, so that you may live, enter, and take possession of the land the LORD your ancestors' God is giving you."
    },
    "2": {
      "L": "Ye shall not add unto the word which I command you, neither shall ye diminish from it, that ye may keep the commandments of the LORD your God which I command you.",
      "M": "You shall not add to the word that I command you, nor take from it, so that you may keep the commandments of the LORD your God that I am commanding you.",
      "T": "Do not add a single word to what I am commanding you, and do not subtract from it either. Keep the commandments of the LORD your God exactly as I give them."
    },
    "3": {
      "L": "Your eyes have seen what the LORD did because of Baal-peor: for all the men that followed Baal-peor, the LORD thy God hath destroyed them from among you.",
      "M": "Your eyes have seen what the LORD did at Baal-peor—the LORD your God destroyed from among you every man who followed the Baal of Peor.",
      "T": "Your own eyes saw what the LORD did at Baal-peor. Every Israelite who ran after the Baal of Peor — the LORD your God wiped him out of your community."
    },
    "4": {
      "L": "But ye that did cleave unto the LORD your God are alive every one of you this day.",
      "M": "But you who held fast to the LORD your God are all alive today.",
      "T": "But every one of you who clung to the LORD your God is standing here alive today."
    },
    "5": {
      "L": "Behold, I have taught you statutes and ordinances, even as the LORD my God commanded me, that ye should do so in the midst of the land whither ye go in to possess it.",
      "M": "See, I have taught you statutes and rules, as the LORD my God commanded me, so that you should do them in the land you are entering to possess.",
      "T": "Look — I have taught you statutes and rulings exactly as the LORD my God commanded me. These are what you are to live by in the land you are entering to take as your own."
    },
    "6": {
      "L": "Keep therefore and do them; for this is your wisdom and your understanding in the sight of the peoples, that shall hear all these statutes, and say, Surely this great nation is a wise and understanding people.",
      "M": "Keep and carry out these statutes, for this will be your wisdom and understanding before the other peoples, who will hear all these statutes and say, 'Surely this great nation is a wise and understanding people.'",
      "T": "Observe and obey them — this is what will make you wise and discerning in the eyes of the nations. When they hear all these laws they will say, 'This great nation — what a wise and understanding people.'"
    },
    "7": {
      "L": "For what great nation is there, that hath a god so nigh unto them, as the LORD our God is whensoever we call upon him?",
      "M": "For what great nation has a god as close to it as the LORD our God is to us whenever we call upon him?",
      "T": "What great nation has a god who draws as near as the LORD our God comes to us every time we call?"
    },
    "8": {
      "L": "And what great nation is there, that hath statutes and ordinances so righteous as all this law, which I set before you this day?",
      "M": "And what great nation has statutes and rules as righteous as this entire law I am setting before you today?",
      "T": "And what great nation has a body of law as just as the whole instruction I am laying before you today?"
    },
    "9": {
      "L": "Only take heed to thyself, and keep thy soul diligently, lest thou forget the things which thine eyes saw, and lest they depart from thy heart all the days of thy life; but make them known unto thy children and thy children's children;",
      "M": "But be careful, and guard yourselves diligently, lest you forget the things your eyes have seen, and lest they pass from your heart all the days of your life. Teach them to your children and your children's children.",
      "T": "But take great care — guard your whole self with diligence — so that you do not forget what your eyes have seen, and those sights do not fade from your heart as long as you live. Teach them to your children and grandchildren."
    },
    "10": {
      "L": "the day that thou stoodest before the LORD thy God in Horeb, when the LORD said unto me, Gather me the people together, and I will make them hear my words, that they may learn to fear me all the days that they live upon the earth, and that they may teach their children.",
      "M": "Tell them about the day you stood before the LORD your God at Horeb, when the LORD said to me, 'Gather the people to me so I may let them hear my words, that they may learn to fear me all the days they live on the earth, and that they may teach their children so.'",
      "T": "Tell them about the day you stood before the LORD your God at Horeb — when the LORD told me: 'Assemble the people before me. I will let them hear my own words, so they will learn to hold me in awe all their days on this earth, and so they will pass this awe on to their children.'"
    },
    "11": {
      "L": "And ye came near and stood under the mountain; and the mountain burned with fire unto the heart of heaven, with darkness, cloud, and thick darkness.",
      "M": "And you came near and stood at the foot of the mountain while the mountain burned with fire up to the heart of heaven, wrapped in darkness, cloud, and deep gloom.",
      "T": "You came forward and stood at the base of the mountain. The mountain was blazing — fire reaching into the sky itself — wrapped in dark cloud and deep, impenetrable gloom."
    },
    "12": {
      "L": "And the LORD spake unto you out of the midst of the fire: ye heard the voice of words, but ye saw no form; only a voice.",
      "M": "Then the LORD spoke to you out of the midst of the fire. You heard the sound of words but saw no form—there was only a voice.",
      "T": "The LORD spoke to you from inside the fire. You heard words — clear, intelligible speech — but you saw no shape, no body, no form. Only a voice."
    },
    "13": {
      "L": "And he declared unto you his covenant, which he commanded you to perform, even ten commandments; and he wrote them upon two tables of stone.",
      "M": "He declared to you his covenant, which he commanded you to keep—the Ten Commandments—and he wrote them on two tablets of stone.",
      "T": "He proclaimed his covenant to you — the Ten Commandments, which he ordered you to perform — and he inscribed them on two stone tablets."
    },
    "14": {
      "L": "And the LORD commanded me at that time to teach you statutes and ordinances, that ye might do them in the land whither ye go over to possess it.",
      "M": "And the LORD commanded me at that time to teach you statutes and rules for you to carry out in the land you are crossing over to possess.",
      "T": "At that same time the LORD directed me to teach you these statutes and rules — so you would know how to live in the land you are entering to possess."
    },
    "15": {
      "L": "Take ye therefore good heed unto yourselves; for ye saw no manner of form on the day that the LORD spake unto you in Horeb out of the midst of the fire:",
      "M": "Therefore watch yourselves very carefully. Since you saw no form on the day the LORD spoke to you at Horeb out of the midst of the fire,",
      "T": "Watch yourselves with the greatest care. You saw no shape, no figure, no form at all on the day the LORD spoke to you at Horeb out of the fire."
    },
    "16": {
      "L": "lest ye corrupt yourselves, and make you a graven image in the form of any figure, the likeness of male or female,",
      "M": "do not act corruptly by making for yourselves a carved image in the form of any figure—the likeness of male or female,",
      "T": "Do not degrade yourselves by carving an idol in any shape — male or female,"
    },
    "17": {
      "L": "the likeness of any beast that is on the earth, the likeness of any winged fowl that flieth in the heavens,",
      "M": "the likeness of any animal on the earth, the likeness of any winged bird that flies in the sky,",
      "T": "any creature that walks the earth, any bird that flies,"
    },
    "18": {
      "L": "the likeness of any thing that creepeth on the ground, the likeness of any fish that is in the water under the earth:",
      "M": "the likeness of anything that creeps on the ground, the likeness of any fish in the water beneath the earth.",
      "T": "anything that creeps on the ground, any fish in the waters below."
    },
    "19": {
      "L": "and lest thou lift up thine eyes unto heaven, and when thou seest the sun and the moon and the stars, even all the host of heaven, thou be drawn away and worship them, and serve them, which the LORD thy God hath allotted unto all the peoples under the whole heaven.",
      "M": "And beware lest you lift your eyes to heaven and see the sun and moon and stars—the whole host of heaven—and be drawn away to bow down and serve them, things the LORD your God has allotted to all the peoples under the whole heaven.",
      "T": "And do not crane your eyes toward heaven either — seeing the sun and moon and all the starry host and being seduced into bowing to them. Those heavenly bodies the LORD your God has assigned to be for the other nations; they are not your God."
    },
    "20": {
      "L": "But the LORD hath taken you, and brought you forth out of the iron furnace, out of Egypt, to be unto him a people of inheritance, as ye are this day.",
      "M": "But the LORD has taken you and brought you out of the iron furnace, out of Egypt, to be a people belonging to his own inheritance, as you are today.",
      "T": "But you — the LORD pulled you out of Egypt, that iron furnace, that place of smelting suffering, to be his own people, his personal inheritance. That is who you are today."
    },
    "21": {
      "L": "Furthermore the LORD was angry with me for your sakes, and sware that I should not go over Jordan, and that I should not go in unto that good land, which the LORD thy God giveth thee for an inheritance:",
      "M": "Furthermore, the LORD was angry with me on your account and swore that I would not cross the Jordan and would not enter the good land the LORD your God is giving you as your inheritance.",
      "T": "The LORD was also angry with me — on your account — and swore an oath that I would never cross the Jordan, never enter the good land the LORD your God is giving you as your inheritance."
    },
    "22": {
      "L": "but I must die in this land, I must not go over Jordan: but ye shall go over, and possess that good land.",
      "M": "I must die in this land; I am not to cross the Jordan. But you shall cross over and possess that good land.",
      "T": "I will die here on this side. I will not cross the Jordan. But you will cross — and you will possess that good land."
    },
    "23": {
      "L": "Take heed unto yourselves, lest ye forget the covenant of the LORD your God, which he made with you, and make you a graven image in the form of anything which the LORD thy God hath forbidden thee.",
      "M": "Be careful not to forget the covenant of the LORD your God that he made with you, and make a carved image in the form of anything the LORD your God has forbidden you.",
      "T": "Guard yourselves: do not forget the covenant the LORD your God made with you — and do not violate it by carving an idol in any form he has prohibited."
    },
    "24": {
      "L": "For the LORD thy God is a consuming fire, even a jealous God.",
      "M": "For the LORD your God is a consuming fire, a jealous God.",
      "T": "The LORD your God is a consuming fire. He is a jealous God — he will not share his covenant claim on you with any rival."
    },
    "25": {
      "L": "When thou shalt beget children, and children's children, and ye shall have been long in the land, and shall corrupt yourselves, and make a graven image in the form of anything, and shall do that which is evil in the sight of the LORD thy God, to provoke him to anger:",
      "M": "When you have children and grandchildren and have grown old in the land, and if you act corruptly by making a carved image in the form of anything and do what is evil in the sight of the LORD your God so as to provoke him to anger,",
      "T": "When you have raised children and grandchildren and have put down deep roots in the land — if you then corrupt yourselves by carving any idol and doing what the LORD your God sees as evil, provoking his anger,"
    },
    "26": {
      "L": "I call heaven and earth to witness against you this day, that ye shall soon utterly perish from off the land whereunto ye go over Jordan to possess it; ye shall not prolong your days upon it, but shall utterly be destroyed.",
      "M": "I call heaven and earth as witnesses against you today that you will quickly perish from the land you are crossing the Jordan to possess. You will not live long in it but will be utterly destroyed.",
      "T": "I am summoning heaven and earth as witnesses against you right now: you will be swept quickly from the land you are entering across the Jordan. You will not last long there — you will be obliterated."
    },
    "27": {
      "L": "And the LORD shall scatter you among the peoples, and ye shall be left few in number among the nations, whither the LORD shall lead you away.",
      "M": "The LORD will scatter you among the peoples, and you will be left few in number among the nations where the LORD will drive you.",
      "T": "The LORD will scatter you among the nations, and only a remnant of you will survive in the foreign lands to which he drives you."
    },
    "28": {
      "L": "And there ye shall serve gods, the work of men's hands, wood and stone, which neither see, nor hear, nor eat, nor smell.",
      "M": "And there you will serve gods made by human hands—wood and stone—that can neither see, nor hear, nor eat, nor smell.",
      "T": "There you will worship gods of wood and stone, made by human hands — objects that cannot see, cannot hear, cannot eat, cannot even smell an offering."
    },
    "29": {
      "L": "But from thence ye shall seek the LORD thy God, and thou shalt find him, if thou search after him with all thy heart and with all thy soul.",
      "M": "But from there you will seek the LORD your God and you will find him, if you search for him with all your heart and with all your soul.",
      "T": "But even from there — if you seek the LORD your God, you will find him. Search for him with your whole heart and whole self, and he is there."
    },
    "30": {
      "L": "When thou art in tribulation, and all these things are come upon thee, in the latter days thou shalt return to the LORD thy God, and hearken unto his voice:",
      "M": "When you are in distress and all these things have come upon you, in the latter days you will return to the LORD your God and listen to his voice.",
      "T": "When you are in deep trouble — when all of this has come crashing down on you — in those final desperate days you will turn back to the LORD your God and obey him."
    },
    "31": {
      "L": "for the LORD thy God is a merciful God; he will not fail thee, neither destroy thee, nor forget the covenant of thy fathers which he sware unto them.",
      "M": "For the LORD your God is a merciful God. He will not abandon you or destroy you or forget the covenant with your fathers that he swore to them.",
      "T": "For the LORD your God is a God of compassion. He will not abandon you. He will not destroy you. He will not forget the covenant he swore on oath to your ancestors."
    },
    "32": {
      "L": "For ask now of the days that are past, which were before thee, since the day that God created man upon the earth, and ask from the one end of heaven unto the other, whether there hath been any such thing as this great thing is, or hath been heard like it:",
      "M": "For ask now about the former days that were before you, since the day God created mankind on the earth, and search from one end of heaven to the other: has any such great thing as this ever happened, or has anything like it been heard of?",
      "T": "Search through all of recorded time — from the day God created humanity until today. Scan every corner of the sky. Has anything like this ever happened? Has anything like it ever been heard of?"
    },
    "33": {
      "L": "Did ever people hear the voice of God speaking out of the midst of the fire, as thou hast heard, and live?",
      "M": "Did any people ever hear the voice of God speaking out of the midst of fire, as you have heard, and survive?",
      "T": "Has any nation ever heard God's own voice thundering from inside fire — as you heard it — and lived?"
    },
    "34": {
      "L": "Or hath God assayed to go and take him a nation from the midst of another nation, by trials, by signs, and by wonders, and by war, and by a mighty hand, and by a stretched out arm, and by great terrors, according to all that the LORD your God did for you in Egypt before your eyes?",
      "M": "Or has any god ever attempted to go and take one nation out of the midst of another nation—by tests, by signs and wonders, by war, by a mighty hand and an outstretched arm, and by great terrors—like all that the LORD your God did for you in Egypt before your eyes?",
      "T": "Has any god ever attempted to extract one nation from the heart of another nation — using trial-ordeals, signs, wonders, war, a strong hand, an outstretched arm, and terrifying deeds — everything the LORD your God did for you in Egypt right before your eyes?"
    },
    "35": {
      "L": "Unto thee it was shewed, that thou mightest know that the LORD he is God; there is none else besides him.",
      "M": "To you it was shown so that you would know that the LORD is God; there is no other besides him.",
      "T": "You were shown all of this so that you would know: the LORD alone is God. There is no other."
    },
    "36": {
      "L": "Out of heaven he made thee to hear his voice, that he might instruct thee: and upon earth he shewed thee his great fire; and thou heardest his words out of the midst of the fire.",
      "M": "Out of heaven he let you hear his voice to discipline you, and on earth he showed you his great fire, and you heard his words out of the midst of the fire.",
      "T": "He let you hear his voice from heaven to form you as his people. On earth he let you see his great fire, and from inside that fire you heard his words."
    },
    "37": {
      "L": "And because he loved thy fathers, and chose their seed after them, and brought thee out with his presence, with his great power, out of Egypt;",
      "M": "And because he loved your fathers and chose their descendants after them, he brought you out of Egypt himself, with his great power,",
      "T": "Because he loved your ancestors and chose their descendants after them, he brought you out of Egypt personally — with his own great power —"
    },
    "38": {
      "L": "to drive out nations from before thee greater and mightier than thou art, to bring thee in, to give thee their land for an inheritance, as it is this day.",
      "M": "to drive out before you nations greater and mightier than you, to bring you in and give you their land as an inheritance, as it is today.",
      "T": "displacing nations larger and stronger than you, to bring you in and give you their land as your inheritance — which is exactly what has happened."
    },
    "39": {
      "L": "Know therefore this day, and lay it to thine heart, that the LORD he is God in heaven above, and upon the earth beneath: there is none else.",
      "M": "Know therefore today, and take it to heart, that the LORD is God in heaven above and on the earth beneath—there is no other.",
      "T": "Know it today — let it sink deep into your heart: the LORD is God in the heavens above and on the earth below. There is no other."
    },
    "40": {
      "L": "And thou shalt keep his statutes, and his commandments, which I command thee this day, that it may go well with thee, and with thy children after thee, and that thou mayest prolong thy days upon the land, which the LORD thy God giveth thee, for ever.",
      "M": "Therefore keep his statutes and commandments that I am giving you today, so that it may go well with you and with your children after you, and so that you may live long in the land that the LORD your God is giving you for all time.",
      "T": "Therefore keep his statutes and commandments — the ones I am giving you today — so that things go well for you and for your children after you, and so that you may live long in the land the LORD your God is giving you as a permanent inheritance."
    },
    "41": {
      "L": "Then Moses set apart three cities beyond the Jordan toward the sunrising;",
      "M": "Then Moses set apart three cities in the east beyond the Jordan,",
      "T": "At that point Moses designated three cities on the east side of the Jordan —"
    },
    "42": {
      "L": "that the manslayer might flee thither, which should kill his neighbour unawares, and hated him not in times past; and that fleeing unto one of these cities he might live:",
      "M": "so that a manslayer could flee there—anyone who kills his neighbor unintentionally without prior enmity—and by fleeing to one of these cities could live.",
      "T": "places where someone who had accidentally killed a neighbor — with no prior hatred or intent — could flee and be safe."
    },
    "43": {
      "L": "Bezer in the wilderness, in the plain country, for the Reubenites; and Ramoth in Gilead, for the Gadites; and Golan in Bashan, for the Manassites.",
      "M": "Bezer in the wilderness on the tableland for the Reubenites; Ramoth in Gilead for the Gadites; and Golan in Bashan for the Manassites.",
      "T": "Bezer in the plateau wilderness for Reuben, Ramoth in Gilead for Gad, and Golan in Bashan for Manasseh."
    },
    "44": {
      "L": "And this is the law which Moses set before the children of Israel:",
      "M": "This is the law that Moses set before the people of Israel.",
      "T": "This is the instruction Moses laid before the people of Israel."
    },
    "45": {
      "L": "these are the testimonies, and the statutes, and the ordinances, which Moses spake unto the children of Israel, after they came forth out of Egypt,",
      "M": "These are the testimonies, the statutes, and the rules that Moses spoke to the Israelites after they came out of Egypt,",
      "T": "These are the covenant declarations, the statutes, and the rulings Moses gave Israel after they left Egypt —"
    },
    "46": {
      "L": "beyond the Jordan, in the valley over against Beth-peor, in the land of Sihon king of the Amorites, which dwelt in Heshbon, whom Moses and the children of Israel smote, when they came forth out of Egypt:",
      "M": "east of the Jordan in the valley opposite Beth-peor, in the land of Sihon king of the Amorites, who lived at Heshbon, whom Moses and the Israelites defeated after coming out of Egypt.",
      "T": "given in the valley facing Beth-peor, in the territory of Sihon king of the Amorites at Heshbon, whom Moses and Israel had defeated on the way out of Egypt."
    },
    "47": {
      "L": "And they possessed his land, and the land of Og king of Bashan, two kings of the Amorites, which were beyond the Jordan toward the sunrising;",
      "M": "They had taken possession of his land and the land of Og king of Bashan—the two Amorite kings east of the Jordan—",
      "T": "They had taken over his land and the land of Og king of Bashan — the two Amorite kings east of the Jordan —"
    },
    "48": {
      "L": "from Aroer, which is on the edge of the valley of Arnon, even unto mount Sirion, which is Hermon,",
      "M": "from Aroer on the rim of the Valley of the Arnon as far as Mount Sirion—that is, Hermon—",
      "T": "from Aroer on the Arnon rim all the way to Mount Sirion (that is, Hermon),"
    },
    "49": {
      "L": "and all the Arabah beyond the Jordan eastward, even unto the sea of the Arabah, under the slopes of Pisgah.",
      "M": "along with all the Arabah east of the Jordan as far as the Sea of the Arabah, under the slopes of Pisgah.",
      "T": "together with the entire Arabah east of the Jordan as far as the Salt Sea below the Pisgah slopes."
    }
  },
  "5": {
    "1": {
      "L": "And Moses called unto all Israel, and said unto them, Hear, O Israel, the statutes and the ordinances which I speak in your ears this day, that ye may learn them, and observe to do them.",
      "M": "Moses summoned all Israel and said to them: Hear, O Israel, the statutes and rules I am speaking in your hearing today, so that you may learn them and be careful to do them.",
      "T": "Moses called all Israel together and addressed them: Hear this, Israel — the statutes and rulings I am declaring to you today. Learn them. Live by them."
    },
    "2": {
      "L": "The LORD our God made a covenant with us in Horeb.",
      "M": "The LORD our God made a covenant with us at Horeb.",
      "T": "The LORD our God made a covenant with us at Horeb."
    },
    "3": {
      "L": "The LORD made not this covenant with our fathers, but with us, even us, who are all of us here alive this day.",
      "M": "It was not with our fathers that the LORD made this covenant, but with us—us, all of us who are here and alive today.",
      "T": "Not with our ancestors did the LORD cut this covenant — with us. With us, every one of us standing here alive today. We are Sinai."
    },
    "4": {
      "L": "The LORD spake with you face to face in the mount out of the midst of the fire,",
      "M": "The LORD spoke with you face to face at the mountain, out of the midst of the fire.",
      "T": "The LORD spoke with you face to face at that mountain, from inside the fire."
    },
    "5": {
      "L": "(I stood between the LORD and you at that time, to shew you the word of the LORD: for ye were afraid by reason of the fire, and went not up into the mount;) saying,",
      "M": "I stood between the LORD and you at that time to declare the word of the LORD to you, for you were afraid of the fire and did not go up onto the mountain. He said:",
      "T": "(I stood between the LORD and you, carrying his words to you — because the fire terrified you and you would not go up onto the mountain. He said:)"
    },
    "6": {
      "L": "I am the LORD thy God, which brought thee out of the land of Egypt, from the house of bondage.",
      "M": "'I am the LORD your God, who brought you out of the land of Egypt, out of the house of slavery.'",
      "T": "'I am the LORD your God who brought you out of Egypt, out of the slave house.'"
    },
    "7": {
      "L": "Thou shalt have none other gods before me.",
      "M": "'You shall have no other gods before me.'",
      "T": "'No other gods — none — alongside me.'"
    },
    "8": {
      "L": "Thou shalt not make thee a graven image, nor any likeness of anything that is in heaven above, or that is in the earth beneath, or that is in the waters beneath the earth:",
      "M": "'You shall not make for yourself a carved image—any likeness of what is in heaven above, or on earth beneath, or in the water under the earth.'",
      "T": "'Do not carve yourself an idol — no representation of anything in the skies above, the earth below, or the waters underground.'"
    },
    "9": {
      "L": "thou shalt not bow down thyself unto them, nor serve them: for I the LORD thy God am a jealous God, visiting the iniquity of the fathers upon the children, and upon the third and upon the fourth generation of them that hate me,",
      "M": "'You shall not bow down to them or serve them; for I the LORD your God am a jealous God, visiting the iniquity of the fathers upon the children to the third and fourth generation of those who hate me,'",
      "T": "'Do not bow down to them or worship them. I, the LORD your God, am a jealous God — I will hold accountable the families of those who reject me, down to the third and fourth generation,'"
    },
    "10": {
      "L": "and shewing mercy unto thousands of them that love me and keep my commandments.",
      "M": "'but showing steadfast love to thousands of those who love me and keep my commandments.'",
      "T": "'but lavishing steadfast love on thousands of generations of those who love me and keep my commandments.'"
    },
    "11": {
      "L": "Thou shalt not take the name of the LORD thy God in vain: for the LORD will not hold him guiltless that taketh his name in vain.",
      "M": "'You shall not take the name of the LORD your God in vain, for the LORD will not hold guiltless whoever takes his name in vain.'",
      "T": "'Do not treat the name of the LORD your God as worthless. The LORD will not let anyone off who degrades his name.'"
    },
    "12": {
      "L": "Keep the sabbath day to sanctify it, as the LORD thy God hath commanded thee.",
      "M": "'Observe the Sabbath day, to keep it holy, as the LORD your God commanded you.'",
      "T": "'Guard the Sabbath day — set it apart as holy — as the LORD your God has commanded.'"
    },
    "13": {
      "L": "Six days thou shalt labour, and do all thy work:",
      "M": "'Six days you shall labor and do all your work,'",
      "T": "'Six days you work and accomplish everything you need to.'"
    },
    "14": {
      "L": "but the seventh day is a sabbath unto the LORD thy God: in it thou shalt not do any work, thou, nor thy son, nor thy daughter, nor thy manservant, nor thy maidservant, nor thine ox, nor thine ass, nor any of thy cattle, nor thy stranger that is within thy gates; that thy manservant and thy maidservant may rest as well as thou.",
      "M": "'but the seventh day is a Sabbath to the LORD your God. On it you shall not do any work—you, your son, your daughter, your male servant, your female servant, your ox, your donkey, any of your livestock, or the sojourner within your gates—so that your male and female servants may rest just as you do.'",
      "T": "'but the seventh day is a Sabbath belonging to the LORD your God. That day, no work — not you, not your son or daughter, not your male or female servant, not your ox or donkey or any animal, not the foreigner living in your community. Your servants must rest just as you do.'"
    },
    "15": {
      "L": "And thou shalt remember that thou wast a servant in the land of Egypt, and that the LORD thy God brought thee out thence by a mighty hand and by a stretched out arm: therefore the LORD thy God commanded thee to keep the sabbath day.",
      "M": "'Remember that you were a slave in the land of Egypt, and the LORD your God brought you out from there with a mighty hand and an outstretched arm. Therefore the LORD your God commanded you to keep the Sabbath day.'",
      "T": "'Remember: you were a slave in Egypt. The LORD your God pulled you out of there with a powerful hand and an outstretched arm. That is exactly why the LORD your God commands the Sabbath — rest is what freedom looks like.'"
    },
    "16": {
      "L": "Honour thy father and thy mother, as the LORD thy God hath commanded thee; that thy days may be long, and that it may go well with thee, in the land which the LORD thy God giveth thee.",
      "M": "'Honor your father and your mother, as the LORD your God commanded you, that your days may be long and that things may go well with you in the land the LORD your God is giving you.'",
      "T": "'Give your father and mother the honor they are due — as the LORD your God commanded — so that your life may be long and good in the land the LORD your God is giving you.'"
    },
    "17": {
      "L": "Thou shalt not kill.",
      "M": "'You shall not murder.'",
      "T": "'Do not commit murder.'"
    },
    "18": {
      "L": "Neither shalt thou commit adultery.",
      "M": "'You shall not commit adultery.'",
      "T": "'Do not commit adultery.'"
    },
    "19": {
      "L": "Neither shalt thou steal.",
      "M": "'You shall not steal.'",
      "T": "'Do not steal.'"
    },
    "20": {
      "L": "Neither shalt thou bear false witness against thy neighbour.",
      "M": "'You shall not give false testimony against your neighbor.'",
      "T": "'Do not testify falsely against your neighbor.'"
    },
    "21": {
      "L": "Neither shalt thou covet thy neighbour's wife, neither shalt thou desire thy neighbour's house, his field, or his manservant, or his maidservant, his ox, or his ass, or any thing that is thy neighbour's.",
      "M": "'You shall not covet your neighbor's wife. And you shall not desire your neighbor's house, his field, his male servant, his female servant, his ox, his donkey, or anything that belongs to your neighbor.'",
      "T": "'Do not covet your neighbor's wife. Do not crave your neighbor's house, field, servants, ox, donkey — anything that belongs to them.'"
    },
    "22": {
      "L": "These words the LORD spake unto all your assembly in the mount out of the midst of the fire, of the cloud, and of the thick darkness, with a great voice: and he added no more. And he wrote them upon two tables of stone, and delivered them unto me.",
      "M": "These words the LORD spoke to all your assembly at the mountain out of the midst of the fire, the cloud, and the thick darkness, with a loud voice; and he added no more. He wrote them on two tablets of stone and gave them to me.",
      "T": "These words — only these — the LORD spoke to your whole assembly at the mountain, from inside the fire and cloud and deep darkness, with a great voice that did not continue. He wrote them on two stone tablets and gave them to me."
    },
    "23": {
      "L": "And it came to pass, when ye heard the voice out of the midst of the darkness, while the mountain did burn with fire, that ye came near unto me, even all the heads of your tribes, and your elders;",
      "M": "And when you heard the voice out of the midst of the darkness while the mountain was burning with fire, all the heads of your tribes and your elders came near to me.",
      "T": "When you heard that voice out of the darkness — while the mountain blazed with fire — all your tribal leaders and elders came forward to me."
    },
    "24": {
      "L": "and ye said, Behold, the LORD our God hath shewed us his glory and his greatness, and we have heard his voice out of the midst of the fire: we have seen this day that God doth talk with man, and he liveth.",
      "M": "And you said, 'The LORD our God has shown us his glory and greatness, and we have heard his voice out of the midst of the fire. Today we have seen that God speaks with man, and man still lives.'",
      "T": "You said: 'The LORD our God has shown us his glory and his greatness. We heard his voice from inside the fire. Today we have seen that God can speak directly to a human being and that person can still be alive.'"
    },
    "25": {
      "L": "Now therefore why should we die? for this great fire will consume us: if we hear the voice of the LORD our God any more, then we shall die.",
      "M": "'But now why should we die? For this great fire will consume us. If we hear the voice of the LORD our God any longer, we shall die.'",
      "T": "'But why should we die? This fire will devour us. If we keep hearing the LORD our God speak directly, we will not survive.'"
    },
    "26": {
      "L": "For who is there of all flesh, that hath heard the voice of the living God speaking out of the midst of the fire, as we have, and lived?",
      "M": "'For who among all flesh has ever heard the voice of the living God speaking from the midst of fire as we have, and lived?'",
      "T": "'Who among all mortal flesh has ever heard the living God speak from fire the way we have — and lived through it?'"
    },
    "27": {
      "L": "Go thou near, and hear all that the LORD our God shall say: and speak thou unto us all that the LORD our God shall speak unto thee; and we will hear it, and do it.",
      "M": "'Go near and hear everything the LORD our God says, and you speak to us all that the LORD our God speaks to you. We will listen and do it.'",
      "T": "'You go close — you hear everything the LORD our God says — then tell us. We will listen and we will obey.'"
    },
    "28": {
      "L": "And the LORD heard the voice of your words, when ye spake unto me; and the LORD said unto me, I have heard the voice of the words of this people, which they have spoken unto thee: they have well said all that they have spoken.",
      "M": "And the LORD heard your words when you spoke to me. And the LORD said to me, 'I have heard the words of this people, which they have spoken to you. They are right in all that they have said.'",
      "T": "The LORD heard what you said to me. He told me: 'I have heard what this people said to you. They have spoken rightly.'"
    },
    "29": {
      "L": "Oh that there were such a heart in them, that they would fear me, and keep all my commandments always, that it might be well with them, and with their children for ever!",
      "M": "'If only they had such a heart as this always, to fear me and keep all my commandments, so that it might go well with them and with their children forever!'",
      "T": "'Oh, if only this heart of theirs would hold — that they would remain this ready to hold me in awe and keep all my commandments, always, so things would go well for them and their children forever.'"
    },
    "30": {
      "L": "Go say to them, Get you into your tents again.",
      "M": "'Go, tell them, Return to your tents.'",
      "T": "'Go tell them: return to your tents.'"
    },
    "31": {
      "L": "But as for thee, stand thou here by me, and I will speak unto thee all the commandment, and the statutes, and the ordinances, which thou shalt teach them, that they may do them in the land which I give them to possess it.",
      "M": "'But as for you, stand here with me, and I will tell you the whole commandment, the statutes and rules, that you shall teach them—so that they may do them in the land I am giving them to possess.'",
      "T": "'But you — stand here with me. I will give you the full body of commandment, statutes, and rulings that you are to teach them, so they know how to live in the land I am giving them.'"
    },
    "32": {
      "L": "Ye shall observe to do therefore as the LORD your God hath commanded you: ye shall not turn aside to the right hand or to the left.",
      "M": "You shall be careful therefore to do as the LORD your God commanded you. You shall not turn aside to the right or to the left.",
      "T": "Be careful to do exactly what the LORD your God commanded you. Do not veer off to the right or the left."
    },
    "33": {
      "L": "Ye shall walk in all the way which the LORD your God hath commanded you, that ye may live, and that it may be well with you, and that ye may prolong your days in the land which ye shall possess.",
      "M": "You shall walk in all the way that the LORD your God has commanded you, so that you may live, and it may go well with you, and you may have long life in the land you are going to possess.",
      "T": "Walk the whole road the LORD your God has marked out — so you may live, so things go well for you, so you have long years in the land you are about to possess."
    }
  },
  "6": {
    "1": {
      "L": "Now this is the commandment, the statutes, and the ordinances, which the LORD your God commanded to teach you, that ye might do them in the land whither ye go over to possess it:",
      "M": "Now this is the commandment—the statutes and the rules—that the LORD your God commanded me to teach you, so that you may do them in the land you are going over to possess,",
      "T": "This is the full body of command — the statutes and rulings — the LORD your God directed me to teach you, so you may live by them in the land you are crossing over to take as your own."
    },
    "2": {
      "L": "that thou mightest fear the LORD thy God, to keep all his statutes and his commandments, which I command thee, thou, and thy son, and thy son's son, all the days of thy life; and that thy days may be prolonged.",
      "M": "so that you may fear the LORD your God, you and your son and your grandson, by keeping all his statutes and commandments that I command you, all the days of your life, and that your days may be long.",
      "T": "— that you may hold the LORD your God in genuine awe, you and your children and your grandchildren, by keeping every statute and commandment I am giving you, all the days of your life, and so live long."
    },
    "3": {
      "L": "Hear therefore, O Israel, and observe to do it; that it may be well with thee, and that ye may increase mightily, as the LORD God of thy fathers hath promised thee, in the land that floweth with milk and honey.",
      "M": "Hear therefore, O Israel, and be careful to do it, that it may go well with you and that you may multiply greatly, as the LORD, the God of your fathers, promised you, in a land flowing with milk and honey.",
      "T": "Listen then, Israel — take care to obey — so that things go well for you and you flourish greatly, just as the LORD your ancestors' God promised, in a land overflowing with milk and honey."
    },
    "4": {
      "L": "Hear, O Israel: the LORD our God, the LORD is one:",
      "M": "Hear, O Israel: The LORD our God, the LORD is one.",
      "T": "Hear this, Israel: The LORD is our God. The LORD alone."
    },
    "5": {
      "L": "and thou shalt love the LORD thy God with all thy heart, and with all thy soul, and with all thy might.",
      "M": "And you shall love the LORD your God with all your heart and with all your soul and with all your might.",
      "T": "Love the LORD your God with everything you have — every capacity of your inner life, your whole self, all your strength."
    },
    "6": {
      "L": "And these words, which I command thee this day, shall be upon thy heart:",
      "M": "And these words that I command you today shall be on your heart.",
      "T": "These words I am commanding you today must live in your heart."
    },
    "7": {
      "L": "and thou shalt teach them diligently unto thy children, and shalt talk of them when thou sittest in thy house, and when thou walkest by the way, and when thou liest down, and when thou risest up.",
      "M": "You shall teach them earnestly to your children and shall speak of them when you sit in your house, and when you walk by the way, and when you lie down, and when you rise up.",
      "T": "Drill them into your children. Talk about them when you sit at home and when you are on the road, when you lie down at night and when you get up in the morning."
    },
    "8": {
      "L": "And thou shalt bind them for a sign upon thy hand, and they shall be as frontlets between thine eyes.",
      "M": "You shall bind them as a sign on your hand, and they shall be as frontlets between your eyes.",
      "T": "Bind them to your hand as a visible reminder. Fasten them between your eyes as a mark of who you are."
    },
    "9": {
      "L": "And thou shalt write them on the door posts of thy house, and upon thy gates.",
      "M": "You shall write them on the doorposts of your house and on your gates.",
      "T": "Write them on the doorposts of your house and on your gates."
    },
    "10": {
      "L": "And it shall be, when the LORD thy God shall bring thee into the land which he sware unto thy fathers, to Abraham, to Isaac, and to Jacob, to give thee great and goodly cities, which thou buildedst not,",
      "M": "And when the LORD your God brings you into the land he swore to your fathers—to Abraham, to Isaac, and to Jacob—to give you, with great and good cities that you did not build,",
      "T": "When the LORD your God brings you into the land he swore on oath to give your ancestors — Abraham, Isaac, Jacob — with flourishing cities you did not build,"
    },
    "11": {
      "L": "and houses full of all good things, which thou filledst not, and wells digged, which thou diggedst not, vineyards and olive trees, which thou plantedst not; when thou shalt have eaten and be full;",
      "M": "and houses filled with all good things that you did not fill, and cisterns cut out that you did not cut, and vineyards and olive trees that you did not plant—and when you eat and are full,",
      "T": "houses stocked with everything good you never stocked, cisterns hewn from rock you never dug, vineyards and olive groves you never planted — when you eat there and are full and satisfied —"
    },
    "12": {
      "L": "then beware lest thou forget the LORD, which brought thee forth out of the land of Egypt, from the house of bondage.",
      "M": "then take care that you do not forget the LORD who brought you out of the land of Egypt, out of the house of slavery.",
      "T": "beware: do not forget the LORD who pulled you out of Egypt, out of that slave house."
    },
    "13": {
      "L": "Thou shalt fear the LORD thy God; and him shalt thou serve, and shalt swear by his name.",
      "M": "You shall fear the LORD your God. You shall serve him and swear by his name.",
      "T": "The LORD your God — fear him, serve him, swear your oaths by his name alone."
    },
    "14": {
      "L": "Ye shall not go after other gods, of the gods of the peoples which are round about you;",
      "M": "You shall not go after other gods, the gods of the peoples who are around you,",
      "T": "Do not go chasing after other gods — the gods of the peoples surrounding you —"
    },
    "15": {
      "L": "for a jealous God, even the LORD thy God, is in the midst of thee; lest the anger of the LORD thy God be kindled against thee, and he destroy thee from off the face of the earth.",
      "M": "for the LORD your God in your midst is a jealous God—lest the anger of the LORD your God be kindled against you and he destroy you from the face of the earth.",
      "T": "because the LORD your God who lives among you is a jealous God. If his anger is ignited against you, he will sweep you off the face of the earth."
    },
    "16": {
      "L": "Ye shall not tempt the LORD your God, as ye tempted him in Massah.",
      "M": "You shall not put the LORD your God to the test, as you tested him at Massah.",
      "T": "Do not test the LORD your God the way you tested him at Massah."
    },
    "17": {
      "L": "Ye shall diligently keep the commandments of the LORD your God, and his testimonies, and his statutes, which he hath commanded thee.",
      "M": "You shall diligently keep the commandments of the LORD your God, and his testimonies and his statutes, which he has commanded you.",
      "T": "Keep the commandments of the LORD your God with diligence — his covenant declarations, his statutes, everything he has commanded."
    },
    "18": {
      "L": "And thou shalt do that which is right and good in the sight of the LORD; that it may be well with thee, and that thou mayest go in and possess the good land which the LORD sware unto thy fathers,",
      "M": "And you shall do what is right and good in the sight of the LORD, so that it may go well with you and you may go in and possess the good land that the LORD swore to give to your fathers,",
      "T": "Do what is right and good in the LORD's eyes — so things go well for you, and you enter and possess the good land the LORD swore to give your ancestors,"
    },
    "19": {
      "L": "by thrusting out all thine enemies from before thee, as the LORD hath spoken.",
      "M": "by thrusting out all your enemies from before you, as the LORD has promised.",
      "T": "driving out all your enemies before you, exactly as the LORD promised."
    },
    "20": {
      "L": "When thy son asketh thee in time to come, saying, What mean the testimonies, and the statutes, and the ordinances, which the LORD our God hath commanded you?",
      "M": "When your son asks you in time to come, 'What is the meaning of the testimonies and the statutes and the rules that the LORD our God has commanded you?'",
      "T": "When your son asks you someday — 'What is the meaning of all these declarations, statutes, and rulings the LORD our God gave you?' —"
    },
    "21": {
      "L": "then thou shalt say unto thy son, We were Pharaoh's bondmen in Egypt; and the LORD brought us out of Egypt with a mighty hand:",
      "M": "then you shall say to your son, 'We were Pharaoh's slaves in Egypt. And the LORD brought us out of Egypt with a mighty hand.'",
      "T": "tell him: 'We were slaves to Pharaoh in Egypt. The LORD brought us out of Egypt with a powerful hand.'"
    },
    "22": {
      "L": "and the LORD shewed signs and wonders, great and sore, upon Egypt, upon Pharaoh, and upon all his household, before our eyes:",
      "M": "And the LORD showed great and devastating signs and wonders against Egypt and Pharaoh and all his household, before our eyes.",
      "T": "'The LORD unleashed great and terrible signs and wonders on Egypt, on Pharaoh, on his entire court — right before our eyes.'"
    },
    "23": {
      "L": "and he brought us out from thence, that he might bring us in, to give us the land which he sware unto our fathers.",
      "M": "And he brought us out from there, that he might bring us in and give us the land that he swore to give to our fathers.",
      "T": "'He brought us out of there in order to bring us here — to give us this land he promised our ancestors on oath.'"
    },
    "24": {
      "L": "And the LORD commanded us to do all these statutes, to fear the LORD our God, for our good always, and for our life, as it is at this day.",
      "M": "And the LORD commanded us to do all these statutes, to fear the LORD our God, for our good always, and to keep us alive, as we are this day.",
      "T": "'The LORD commanded us to live by all these statutes — to hold him in awe — for our own lasting good and to keep us alive, which is exactly where we are today.'"
    },
    "25": {
      "L": "And it shall be righteousness unto us, if we observe to do all this commandment before the LORD our God, as he hath commanded us.",
      "M": "And it will be righteousness for us if we are careful to do all this commandment before the LORD our God, as he has commanded us.",
      "T": "'And this is what counts as righteousness for us — keeping this whole body of command before the LORD our God, just as he commanded.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'deuteronomy')
        merge_tier(existing, DEUTERONOMY, tier_key)
        save(tier_dir, 'deuteronomy', existing)
    print('Deuteronomy 1–6 written.')

if __name__ == '__main__':
    main()
