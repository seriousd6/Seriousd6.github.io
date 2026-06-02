"""
MKT Deuteronomy chapters 25–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-deuteronomy-25-30.py

Covers: judicial flogging limits (ch. 25); the muzzled ox and levirate marriage (ch. 25);
the sandal-removal ceremony (halitzah, ch. 25); honest weights and measures (ch. 25);
the command to blot out Amalek (ch. 25); firstfruits liturgy and the creed of origins
(ch. 26); tithe declaration (ch. 26); mutual covenant avowal between Israel and the LORD
(ch. 26); the stone monument and altar at Ebal (ch. 27); the dodecalogue of curses —
twelve public curses answered by congregational Amen (ch. 27); blessings for obedience
(ch. 28:1–14); the extended curses for disobedience — siege, plague, exile (ch. 28:15–68);
the Moab covenant renewal and its basis in historical memory (ch. 29); the promise of
restoration after exile and heart-circumcision (ch. 30); "the word is near you" (ch. 30);
the final call: choose life or death (ch. 30).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M (small-caps convention); "the LORD" in T — consistent
  with all prior Deuteronomy scripts
- H430 (אֱלֹהִים): "God" in all tiers
- H6 (אֹבֵד): "perishing" (26:5) — the great creed "A wandering/perishing Aramean was
  my father." The root means to be lost/about to perish; L renders "perishing," M uses
  "wandering" (the more idiomatic rendering in English tradition), T notes both senses:
  Jacob's father Laban pursued him to destroy; the clan was small and near extinction —
  the ambiguity is meaningful
- H761 (אֲרַמִּי): "Aramean" — Jacob's father-in-law Laban was Aramean; LXX renders this
  as "my father abandoned/left Syria"; T surfaces the historical referent clearly
- H2992/H2993/H2994 (יָבַם/יָבָם/יְבָמָה): levirate duty, husband's brother, brother's
  wife — L uses technical phrase "perform the duty of a husband's brother"; M uses
  "fulfill levirate duty" / "brother-in-law"; T surfaces the institution's purpose
  (preserve the name and inheritance of the dead) and names it "levirate obligation"
- H2502 (חָלַץ): "loose/remove" — the sandal ceremony; L "looses," M "removes," T explains
  the halitzah rite as a public release from levirate obligation, carrying permanent shame
- H5459 (סְגֻלָּה): "treasured possession/peculiar people" (26:18) — L "peculiar people,"
  M "treasured possession," T surfaces the covenant ownership language: Israel is the LORD's
  personal property in the sense of a sovereign's most valued holding
- H559 in the mutual avowal (26:17–18): "avouched/declared" — both parties formally
  assert a covenant commitment; L "avouched," M "declared," T "sworn by word and deed"
- H1285 (בְּרִית): "covenant" — prominent in ch. 29; consistent with prior scripts
- H4135 (מוּל): "circumcise" — 30:6 "the LORD will circumcise your heart"; L preserves
  the literal image; M keeps "circumcise your heart"; T: God will cut away the uncircumcised
  resistance from within so that love for him becomes natural
- H5315 (נֶפֶשׁ): "soul" in the Shema-formula contexts (30:2, 30:6, 30:10) — here the
  Deuteronomic formula "heart and soul" is formulaic for total devotion; keep "soul"
  in these contexts (contrast 19:21 where "life" fits better for the lex talionis)
- H3824 (לֵב): "heart" all tiers — the most repeated word in chs. 29–30
- H1697 (דָּבָר): "word/thing" — in 30:14 "the word is very near you"; L "word," M "word,"
  T the commandment itself — not a distant abstraction but the shape of daily life
- H8441 (תּוֹעֵבָה): "abomination" all tiers — matches all prior scripts
- H2764 (חֵרֶם) does not appear in this range
- H7307 (רוּחַ) does not appear in this range
- The curses of ch. 28 (vv. 15–68) are the most extensive in the Torah. The T tier honors
  their cumulative rhetorical force — they are not softened; their function is to make the
  cost of covenant-breaking feel total and inescapable before the covenant is sealed
- Ch. 29:29 "secret things belong to the LORD our God; revealed things belong to us":
  T tier marks this as the hinge between divine sovereignty and human responsibility —
  we are not responsible for what we cannot know, but fully responsible for what we have
- Ch. 30:11–14 ("the word is not in heaven...it is very near you"): Paul cites this
  passage in Romans 10:6–8 applying it to the word of faith about Christ. T tier notes
  this trajectory without anachronism, focusing on the original meaning: Moses insists
  that the Torah is not a remote ideal but a lived, embodied practice within reach
- Poetic/rhetorical refrains ("so that it may go well with you"; "choose life that you
  may live"): preserved verbatim in L/M, given expressive cadence in T
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
  "25": {
    "1": {
      "L": "If there is a dispute between men and they come to judgment, and the judges decide between them, justifying the righteous and condemning the wicked —",
      "M": "When men have a dispute and bring it to court, the judges shall decide the case, acquitting the innocent and condemning the guilty.",
      "T": "When a dispute between men reaches the courts and the judges must decide — they acquit the innocent and condemn the guilty. The legal system exists to produce exactly this result."
    },
    "2": {
      "L": "and if the wicked man deserves to be beaten, the judge shall cause him to lie down and be beaten in his presence with a number of stripes according to his guilt.",
      "M": "If the guilty party deserves to be flogged, the judge shall have him lie down and be struck in his presence with the number of lashes his offense warrants.",
      "T": "If the guilty man deserves corporal punishment, the judge administers it personally — the man lies down before the court, and the strokes are counted according to his offense. Justice is witnessed, not delegated anonymously."
    },
    "3": {
      "L": "Forty stripes he may give him, and not exceed. Lest if he should exceed and beat him above these with many stripes, then your brother would be degraded in your eyes.",
      "M": "He may receive up to forty lashes, but no more. If the punishment exceeds that, your fellow Israelite would be publicly degraded before your eyes.",
      "T": "Forty stripes is the absolute limit — not one more. The purpose of punishment is to correct, not to humiliate. Beyond forty, the beating becomes degradation, and the law will not permit that — even the guilty man remains your brother."
    },
    "4": {
      "L": "You shall not muzzle an ox when it treads out grain.",
      "M": "Do not muzzle an ox while it is threshing.",
      "T": "The ox that works the threshing floor must be allowed to eat as it works. You may not muzzle it. The laborer — even an animal — shares in the fruit of its labor. (Paul will later apply this principle to the support of those who labor in the word.)"
    },
    "5": {
      "L": "If brothers dwell together and one of them dies and has no son, the wife of the dead shall not be married outside to a stranger. Her husband's brother shall go in to her and take her as his wife and perform the duty of a husband's brother to her.",
      "M": "When brothers live together and one of them dies without a son, his widow must not marry outside the family. Her brother-in-law shall marry her and fulfill the levirate duty toward her.",
      "T": "When brothers share a household and one dies leaving no son, his widow may not simply marry outside the family. Her brother-in-law has the first obligation — the levirate duty: to marry her, carry on the dead man's line, and preserve his name in Israel."
    },
    "6": {
      "L": "And the firstborn whom she bears shall succeed in the name of his dead brother, that his name may not be blotted out from Israel.",
      "M": "The first son she bears shall carry on the name of the dead brother, so that his name is not wiped out from Israel.",
      "T": "The first son born of this levirate union legally inherits the dead man's name. In the ancient world, a man without a son had no future — the levirate obligation is how Israel ensures that the covenant can hold a place even for those who die young and childless."
    },
    "7": {
      "L": "And if the man does not want to take his brother's wife, then his brother's wife shall go up to the gate to the elders and say, 'My husband's brother refuses to raise up a name for his brother in Israel; he is not willing to perform the duty of a husband's brother to me.'",
      "M": "But if the man refuses to marry his brother's widow, she shall go to the elders at the city gate and say, 'My brother-in-law refuses to perpetuate his brother's name in Israel — he will not fulfill his levirate duty to me.'",
      "T": "If the brother-in-law refuses, the widow takes the matter to the city gate — to the elders, the public legal forum. 'He refuses,' she says. 'He will not perform the obligation that the law and his family require of him.' The refusal is not private; it becomes a public matter."
    },
    "8": {
      "L": "Then the elders of his city shall call him and speak to him, and if he stands firm and says, 'I do not want to take her,'",
      "M": "The elders of the town shall summon him and speak with him. If he stands firm and says, 'I refuse to marry her,'",
      "T": "The elders summon him and reason with him. If after their counsel he still stands firm — 'I will not do it' —"
    },
    "9": {
      "L": "then his brother's wife shall come to him in the presence of the elders and loose his sandal from off his foot and spit in his face and answer and say, 'So shall it be done to the man who does not build up his brother's house.'",
      "M": "his sister-in-law shall come to him before the elders, remove his sandal from his foot, spit in his face, and declare, 'This is what is done to the man who will not build up his brother's family.'",
      "T": "his brother's widow steps forward before the whole assembly of elders. She removes his sandal — the symbol of his claim and standing — and spits in his face. 'This is what becomes of the man who refuses to build up his brother's house.' The halitzah ceremony is complete: he is publicly shamed for his refusal, and she is freed."
    },
    "10": {
      "L": "And his name shall be called in Israel, 'The house of him whose sandal was loosed.'",
      "M": "His family shall be known in Israel as 'The house of the unsandaled man.'",
      "T": "From that day forward, his family carries the name: 'The house of the man whose sandal was removed.' Shame becomes hereditary when a man refuses a covenant obligation."
    },
    "11": {
      "L": "When men fight together, one man with another, and the wife of the one draws near to rescue her husband from the hand of him who is striking him and she puts out her hand and seizes him by his private parts,",
      "M": "If two men are fighting and the wife of one of them intervenes to rescue her husband by grabbing his opponent by the genitals,",
      "T": "If two men are brawling and one man's wife runs in to rescue her husband by seizing his attacker by the genitals —"
    },
    "12": {
      "L": "you shall cut off her hand. Your eye shall not pity.",
      "M": "you shall cut off her hand. Show no pity.",
      "T": "her hand is to be cut off. No pity. The law draws an absolute line at this form of assault, whatever the intention behind it. Even well-meaning intervention does not excuse the act."
    },
    "13": {
      "L": "You shall not have in your bag two kinds of weights, a large and a small.",
      "M": "Do not carry two different sets of weights in your bag — one heavier, one lighter.",
      "T": "Do not keep two sets of weights in your market bag — a large one for buying and a small one for selling. A double standard in the marketplace is a form of theft dressed as commerce."
    },
    "14": {
      "L": "You shall not have in your house two kinds of measures, a large and a small.",
      "M": "Do not keep two different measures in your house — one larger, one smaller.",
      "T": "The same principle applies to measuring containers in your house. One standard, honestly applied — that is what the covenant community requires of its members in trade."
    },
    "15": {
      "L": "A full and just weight you shall have, a full and just measure you shall have, that your days may be long in the land that the LORD your God is giving you.",
      "M": "You shall have accurate and honest weights and measures, so that you may live long in the land the LORD your God is giving you.",
      "T": "Keep accurate, honest weights. Keep accurate, honest measures. The promise of long life in the land is attached to this mundane commercial honesty — because a community that cheats in trade cannot hold together, and the land requires a community that does."
    },
    "16": {
      "L": "For all who do such things — all who do unrighteously — are an abomination to the LORD your God.",
      "M": "Everyone who does these things — all who act dishonestly — is an abomination to the LORD your God.",
      "T": "Every person who engages in fraudulent trade is an abomination to the LORD. The language is the strongest in the vocabulary of holiness. Dishonest business is not a minor failing; it is a desecration."
    },
    "17": {
      "L": "Remember what Amalek did to you on the way as you came out of Egypt —",
      "M": "Remember what the Amalekites did to you on the road when you came out of Egypt —",
      "T": "Carry this in your memory: what Amalek did to Israel on the road out of Egypt."
    },
    "18": {
      "L": "how he met you on the way and struck your rear, all who were faint and weary at your rear, when you were faint and weary, and he did not fear God.",
      "M": "They attacked you on the road and cut down all those who were straggling at the rear — the faint and the weary — when you were exhausted. They had no fear of God.",
      "T": "Amalek struck from behind — not in open battle against the fighting men, but preying on the stragglers: the weak, the exhausted, those who could not keep up. It was an act of calculated cowardice, driven by no fear of God. Remember who they are."
    },
    "19": {
      "L": "Therefore when the LORD your God gives you rest from all your enemies around you in the land that the LORD your God is giving you for an inheritance to possess, you shall blot out the memory of Amalek from under heaven. Do not forget.",
      "M": "When the LORD your God gives you rest from all your enemies in the land he is giving you to possess, you shall blot out the name of Amalek from under heaven. Do not forget.",
      "T": "When the LORD has brought you to rest in the land — when the wars of settlement are over and peace surrounds you — then blot out the memory of Amalek from under heaven. Not before. And do not forget. The command to forget Amalek is itself a command never to forget what Amalek did."
    }
  },
  "26": {
    "1": {
      "L": "And it shall be when you come into the land that the LORD your God is giving you for an inheritance and you possess it and dwell in it,",
      "M": "When you have come into the land the LORD your God is giving you as your inheritance, and you take possession of it and settle there,",
      "T": "When you arrive in the land, take hold of it, and make it your home —"
    },
    "2": {
      "L": "you shall take some of the first of all the fruit of the ground which you harvest from your land that the LORD your God is giving you, and you shall put it in a basket, and you shall go to the place that the LORD your God will choose, to make his name dwell there.",
      "M": "take the first of all the produce you harvest from the soil of the land the LORD your God is giving you, put it in a basket, and go to the place the LORD your God will choose as his dwelling.",
      "T": "take the very first of everything your ground yields — the firstfruits — and carry it in a basket to the place where the LORD has set his name. The land produces because he gave it; the firstfruits belong to him."
    },
    "3": {
      "L": "And you shall go to the priest who is in office at that time and say to him, 'I declare today to the LORD your God that I have come into the land that the LORD swore to our fathers to give us.'",
      "M": "Go to the priest on duty at that time and say, 'I declare today before the LORD your God that I have come into the land he swore to our ancestors to give us.'",
      "T": "Present yourself to the officiating priest and make a formal declaration: 'I am here. I stand in the land the LORD swore to our fathers. What was promised has come to pass.' The ritual turns history into present-tense witness."
    },
    "4": {
      "L": "Then the priest shall take the basket from your hand and set it down before the altar of the LORD your God.",
      "M": "The priest shall take the basket from your hand and set it down before the altar of the LORD your God.",
      "T": "The priest receives the basket from your hands and places it before the LORD's altar. The firstfruits are presented — the transaction of gratitude is made visible."
    },
    "5": {
      "L": "And you shall answer and say before the LORD your God, 'A perishing Aramean was my father, and he went down to Egypt and sojourned there with few men; and he became there a nation, great, mighty, and populous.",
      "M": "Then you shall declare before the LORD your God: 'My father was a wandering Aramean. He went down to Egypt with only a few people and lived there as a foreigner. There he became a great, mighty, and numerous nation.",
      "T": "'A wandering Aramean — a man near perishing — was my father. He went down to Egypt with a handful of people and lived there as an alien. From that small beginning, he became a great, mighty, and populous nation.' This is the creed of origins: Israel begins not in triumph but in smallness and vulnerability, sustained only by the LORD's faithfulness."
    },
    "6": {
      "L": "And the Egyptians dealt harshly with us and afflicted us and laid upon us hard bondage.",
      "M": "But the Egyptians treated us harshly, oppressed us, and imposed ruthless forced labor on us.",
      "T": "Egypt did not receive Israel as guests forever. The Egyptians turned on us — harsh treatment, oppression, grinding labor. The descent into slavery is said plainly, without drama. It happened."
    },
    "7": {
      "L": "Then we cried to the LORD, the God of our fathers, and the LORD heard our voice and saw our affliction, our toil, and our oppression.",
      "M": "Then we cried to the LORD, the God of our ancestors, and the LORD heard our voice and saw our misery, our hardship, and our oppression.",
      "T": "We cried out to the LORD — the God of our fathers. And he heard. He saw the affliction, saw the exhaustion, saw the oppression with eyes that do not overlook. The cry that rose from Egypt was not unanswered."
    },
    "8": {
      "L": "And the LORD brought us out of Egypt with a mighty hand and an outstretched arm, with great terribleness, and with signs, and with wonders.",
      "M": "The LORD brought us out of Egypt with a mighty hand and an outstretched arm, with great awe-inspiring acts and with signs and wonders.",
      "T": "The LORD brought us out — not by gradual improvement but by intervention: a mighty hand, an arm stretched out in power, acts so terrifying to witness that the nations heard and trembled, and signs and wonders that made the cosmos itself obey."
    },
    "9": {
      "L": "And he brought us into this place and gave us this land, a land flowing with milk and honey.",
      "M": "He brought us to this place and gave us this land, a land flowing with milk and honey.",
      "T": "And he brought us here. To this place. To this land — abundant, flowing with milk and honey. The whole journey, from Aramean wanderer to standing on your own soil, was his doing."
    },
    "10": {
      "L": "And now, behold, I have brought the first of the fruit of the ground which you, O LORD, have given me.' And you shall set it down before the LORD your God and bow down before the LORD your God.",
      "M": "And now, LORD, I bring the firstfruits of the soil you have given me.' Then set the basket down before the LORD your God and bow in worship before him.",
      "T": "'And now — here. I bring the first of what this ground has produced, the ground you gave me.' Set the basket down. Bow. The creed ends in an act of worship: the story moves from history into present gratitude."
    },
    "11": {
      "L": "And you shall rejoice in all the good that the LORD your God has given you and your house — you, and the Levite, and the sojourner who is among you.",
      "M": "Rejoice in all the good things the LORD your God has given to you and your household — you, the Levite, and the foreigner living among you.",
      "T": "Then celebrate — genuinely and inclusively. The rejoicing is not private; it extends to the Levite who has no land of his own, and to the foreigner who lives among you. The LORD's goodness overflows every boundary of belonging."
    },
    "12": {
      "L": "When you have finished paying all the tithe of your produce in the third year, which is the year of tithing, giving it to the Levite, the sojourner, the fatherless, and the widow, so that they may eat within your towns and be filled,",
      "M": "When you have finished setting aside a full tithe of your produce in the third year — the year of the tithe — and have given it to the Levite, the foreigner, the fatherless, and the widow, so that they may eat their fill in your towns,",
      "T": "In the third year — the tithe year — when you have completed distributing the full tenth of your produce to the Levite, the immigrant, the orphan, and the widow, so that every one of them has eaten and been satisfied —"
    },
    "13": {
      "L": "then you shall say before the LORD your God, 'I have removed the sacred portion from my house, and I have also given it to the Levite, the sojourner, the fatherless, and the widow, according to all your commandment that you commanded me. I have not transgressed any of your commandments, nor have I forgotten any.",
      "M": "then you shall declare before the LORD your God: 'I have removed from my house the sacred portion and given it to the Levite, the foreigner, the fatherless, and the widow, exactly as you commanded. I have not violated any of your commands or forgotten any.",
      "T": "'I have cleared the sacred portion out of my house,' you declare before the LORD. 'I have given it exactly as you commanded — to the Levite, the immigrant, the orphan, the widow. I have not bent your commandments, and I have not let any of them slip from memory."
    },
    "14": {
      "L": "I have not eaten from it while in mourning, or removed any of it while I was unclean, or offered any of it to the dead. I have obeyed the voice of the LORD my God. I have done according to all that you commanded me.",
      "M": "I have not eaten from it while mourning, nor handled it while unclean, nor offered any of it to the dead. I have obeyed the LORD my God; I have done everything you commanded me.",
      "T": "'I did not eat from the tithe while in mourning — ritual impurity did not touch it. I did not divert any of it to funeral offerings for the dead. I obeyed. I did it all.' This is not a boast; it is a covenant audit, a formal attestation of faithfulness."
    },
    "15": {
      "L": "Look down from your holy habitation, from heaven, and bless your people Israel and the ground that you have given us, as you swore to our fathers — a land flowing with milk and honey.",
      "M": "Look down from your holy dwelling in heaven and bless your people Israel and the land you have given us — just as you swore to our ancestors — a land flowing with milk and honey.",
      "T": "'Now look down from your holy place, from heaven — look down and bless your people Israel. Bless the ground you gave us, the land of your promise to our fathers, the land flowing with milk and honey.' The tithe declaration ends as a prayer: faithfulness rendered, blessing requested."
    },
    "16": {
      "L": "This day the LORD your God commands you to do these statutes and rules. You shall therefore be careful to do them with all your heart and with all your soul.",
      "M": "Today the LORD your God commands you to follow these statutes and ordinances. Keep them with all your heart and with all your soul.",
      "T": "This day — not eventually, not in theory — the LORD commands you. These statutes are in force now. Obey them with your whole heart and your whole self. Total devotion is the only sufficient response to total covenant love."
    },
    "17": {
      "L": "You have declared today that the LORD is your God, and that you will walk in his ways, and keep his statutes and his commandments and his rules, and will obey his voice.",
      "M": "Today you have declared the LORD to be your God, pledging to walk in his ways, to keep his statutes, commandments, and ordinances, and to obey him.",
      "T": "You have sworn it by your word and your presence here: the LORD is your God. You will walk in his ways. You will keep his statutes, commandments, and ordinances. You will listen to his voice. Israel makes the first avowal — the covenant is a mutual declaration."
    },
    "18": {
      "L": "And the LORD has declared today that you are his people, his treasured possession, as he has promised you, and that you are to keep all his commandments,",
      "M": "And the LORD has declared today that you are his treasured people, as he promised — a people who will keep all his commandments.",
      "T": "And the LORD has sworn it from his side: you are his treasured possession — סְגֻלָּה, the term a sovereign uses for his most prized holding. Israel is not a random collection of tribes; Israel is the LORD's own people, claimed by him in covenant. And this treasured status comes with obligation: keep his commandments."
    },
    "19": {
      "L": "and that he will set you in praise and in fame and in honor high above all nations that he has made, and that you shall be a people holy to the LORD your God, as he has spoken.",
      "M": "and that he will set you in praise, fame, and honor high above all nations he has made, and that you will be a people holy to the LORD your God, as he has promised.",
      "T": "The LORD will exalt Israel above all the nations he has made — in praise, in renown, in honor. And the crown of that elevation is holiness: to be a people consecrated to the LORD your God. This is what being raised high means. Not geopolitical dominance — a different kind of greatness altogether."
    }
  },
  "27": {
    "1": {
      "L": "Now Moses and the elders of Israel commanded the people, saying, 'Keep all the commandments that I command you today.'",
      "M": "Moses and the elders of Israel gave this charge to the people: 'Keep every commandment I am giving you today.'",
      "T": "Moses and the elders speak together as one voice to the whole assembly: 'Keep all of this. Every commandment, given today, is binding.' The elders standing beside Moses underscore that this is not one man's word — it is the covenant community's charge."
    },
    "2": {
      "L": "And on the day you cross over the Jordan to the land that the LORD your God is giving you, you shall set up large stones and plaster them with plaster.",
      "M": "On the day you cross the Jordan into the land the LORD your God is giving you, set up large stones and coat them with plaster.",
      "T": "The day you cross the Jordan — the moment of entry — set up large stones and plaster them smooth. This act is commanded for that specific day: the covenant law is to be inscribed on the threshold of the land itself."
    },
    "3": {
      "L": "And you shall write on them all the words of this law when you cross to enter the land that the LORD your God is giving you, a land flowing with milk and honey, as the LORD, the God of your fathers, has promised you.",
      "M": "Write on these stones all the words of this law when you cross over, entering the land the LORD your God is giving you — a land flowing with milk and honey — as the LORD, the God of your ancestors, promised you.",
      "T": "Write every word of this law on those stones when you cross over. The land's identity is defined by the covenant that governs life within it: milk and honey are not its only promise — the words of the law are the terms on which the land is held."
    },
    "4": {
      "L": "And when you have crossed over the Jordan, you shall set up these stones on Mount Ebal, as I command you today, and you shall plaster them with plaster.",
      "M": "When you have crossed the Jordan, set up these stones on Mount Ebal as I am commanding you today, and plaster them.",
      "T": "The location is Ebal — the mountain of curse, not Gerizim the mountain of blessing. The law is erected where the curses are pronounced. This is not arbitrary: the law stands as warning, as the thing that defines what blessing and curse mean."
    },
    "5": {
      "L": "And there you shall build an altar to the LORD your God, an altar of stones. You shall wield no iron tool on them.",
      "M": "There you shall build an altar to the LORD your God out of stones that no iron tool has touched.",
      "T": "Beside the inscribed stones, build an altar — rough, unhewn stones, no iron used on them. What is offered on this altar must not be shaped by human craft. The holiness of the offering demands an altar that has not been worked, only gathered."
    },
    "6": {
      "L": "You shall build the altar of the LORD your God with whole stones and you shall offer burnt offerings on it to the LORD your God.",
      "M": "Build the altar of the LORD your God with uncut stones and offer burnt offerings on it to the LORD your God.",
      "T": "Whole, unworked stones — that is the altar. On it, offer burnt offerings to the LORD. The transition from law written in stone to offerings on stone marks the movement from word to worship."
    },
    "7": {
      "L": "And you shall offer peace offerings and shall eat there and rejoice before the LORD your God.",
      "M": "You shall also sacrifice peace offerings and eat them there, rejoicing in the presence of the LORD your God.",
      "T": "Offer peace offerings and eat them there — at the place of the law, at the altar on the mountain. Rejoice before the LORD. The covenant is celebrated with a meal in his presence: this is the character of the relationship."
    },
    "8": {
      "L": "And you shall write on the stones all the words of this law very plainly.",
      "M": "Write all the words of this law on the stones very clearly.",
      "T": "Write the law clearly — every word, legible, unambiguous. The law is not esoteric. It is not hidden. It is posted in public, in plain script, where all can read it. Clarity is part of its justice."
    },
    "9": {
      "L": "Then Moses and the Levitical priests said to all Israel, 'Keep silence and hear, O Israel: this day you have become the people of the LORD your God.",
      "M": "Then Moses and the Levitical priests spoke to all Israel: 'Be silent, Israel, and listen — today you have become the people of the LORD your God.",
      "T": "Moses and the Levitical priests call for silence — a silence that falls across all Israel: 'Listen. Today. This is the day: you have become the people of the LORD your God.' Not gradually, not eventually. Today, in this ceremony, in this act of covenant-making, the identity is sealed."
    },
    "10": {
      "L": "You shall therefore obey the voice of the LORD your God, keeping his commandments and his statutes, which I command you today.'",
      "M": "Obey the LORD your God by keeping his commandments and statutes that I am giving you today.'",
      "T": "Because you are his people, obey his voice. Keep his commandments and statutes — these are the terms of your identity. The ceremony does not end with a declaration; it ends with a command."
    },
    "11": {
      "L": "That same day Moses commanded the people, saying,",
      "M": "On that same day Moses gave this command to the people:",
      "T": "On that same day — the day of crossing, the day of the ceremony at Ebal — Moses gave the following assignment:"
    },
    "12": {
      "L": "'When you have crossed over the Jordan, these shall stand on Mount Gerizim to bless the people: Simeon, Levi, Judah, Issachar, Joseph, and Benjamin.",
      "M": "'After you cross the Jordan, these tribes shall stand on Mount Gerizim to pronounce the blessing: Simeon, Levi, Judah, Issachar, Joseph, and Benjamin.",
      "T": "'Six tribes take their place on Gerizim — the mountain of blessing: Simeon, Levi, Judah, Issachar, Joseph, Benjamin. These are largely the tribes of Leah and Rachel's sons."
    },
    "13": {
      "L": "'And these shall stand on Mount Ebal for the curse: Reuben, Gad, Asher, Zebulun, Dan, and Naphtali.",
      "M": "'And these tribes shall stand on Mount Ebal for the curse: Reuben, Gad, Asher, Zebulun, Dan, and Naphtali.",
      "T": "'And six tribes stand on Ebal — the mountain of curse: Reuben, Gad, Asher, Zebulun, Dan, Naphtali. The geography of the ceremony makes the covenant choice visually inescapable: blessing on one mountain, curse on the other, and Israel standing between them."
    },
    "14": {
      "L": "And the Levites shall declare to all the men of Israel with a loud voice:",
      "M": "The Levites shall call out to all the Israelites in a loud voice:",
      "T": "The Levites stand in the valley between the two mountains and call out to all Israel in a voice that carries to both peaks:"
    },
    "15": {
      "L": "'Cursed be the man who makes a carved or cast image, an abomination to the LORD, a thing made by the hands of a craftsman, and sets it up in secret.' And all the people shall answer and say, 'Amen.'",
      "M": "'Cursed is the man who carves or casts an idol — an abomination to the LORD, the work of human hands — and sets it up in secret.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the man who makes a carved or cast idol — an abomination to the LORD, fashioned by human craft — and installs it where no one can see.' The first curse targets hidden idolatry: the worship that looks outwardly clean. The whole assembly answers: 'Amen.' Let it be so."
    },
    "16": {
      "L": "'Cursed be he who dishonors his father or his mother.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who treats his father or mother with contempt.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the one who treats father or mother with contempt.' The family is the first social institution; to dishonor its foundation is to begin the unraveling of everything. 'Amen.'"
    },
    "17": {
      "L": "'Cursed be he who moves his neighbor's landmark.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who moves his neighbor's boundary marker.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the one who shifts a neighbor's boundary stone.' Land is divinely apportioned inheritance; to move the marker is to steal what God gave. 'Amen.'"
    },
    "18": {
      "L": "'Cursed be he who misleads a blind man on the road.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who leads a blind person astray on the road.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the one who sends a blind man wandering off the road.' The law cannot easily punish cruelty to those who cannot testify against their abuser. So the covenant curse covers what the court cannot always reach. 'Amen.'"
    },
    "19": {
      "L": "'Cursed be he who perverts the justice due to the sojourner, the fatherless, and the widow.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who denies justice to the foreigner, the fatherless, or the widow.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the one who twists justice against the immigrant, the orphan, or the widow.' These three — the vulnerable trifecta of Deuteronomy — are under divine protection. Pervert their rights and the covenant itself becomes your prosecutor. 'Amen.'"
    },
    "20": {
      "L": "'Cursed be he who lies with his father's wife, for he uncovers his father's skirt.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who sleeps with his father's wife, for he has violated his father's marriage.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the man who sleeps with his father's wife — for in doing so he uncovers his father's skirt, seizing what belongs to another man within his own household.' The household's sexual integrity protects the father's honor and the family order. 'Amen.'"
    },
    "21": {
      "L": "'Cursed be he who lies with any kind of animal.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who has sexual relations with any animal.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is anyone who violates the boundary between human and beast.' The curse is stark because the violation is stark — a crossing of the boundary built into creation. 'Amen.'"
    },
    "22": {
      "L": "'Cursed be he who lies with his sister, whether the daughter of his father or the daughter of his mother.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who sleeps with his sister, whether she is his father's daughter or his mother's daughter.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the man who lies with his sister — whether through his father's line or his mother's.' The family is not a pool of sexual options; the bonds of siblinghood are inviolable. 'Amen.'"
    },
    "23": {
      "L": "'Cursed be he who lies with his mother-in-law.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who sleeps with his mother-in-law.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the man who lies with his mother-in-law.' Marriage creates family bonds that carry sexual prohibitions as strictly as blood relations. 'Amen.'"
    },
    "24": {
      "L": "'Cursed be he who strikes down his neighbor in secret.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who secretly attacks his neighbor.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the one who strikes a neighbor in secret.' Hidden violence — the kind that leaves no witness — falls under the covenant curse when it escapes the court. 'Amen.'"
    },
    "25": {
      "L": "'Cursed be he who accepts a bribe to shed innocent blood.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who accepts a bribe to kill an innocent person.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is the one who takes a payment to have an innocent person killed.' Hired murder, paid assassination, bribery that turns the legal system into a weapon against the guiltless — all one curse. 'Amen.'"
    },
    "26": {
      "L": "'Cursed be he who does not confirm the words of this law by doing them.' And all the people shall say, 'Amen.'",
      "M": "'Cursed is anyone who does not uphold the words of this law by carrying them out.' And all the people shall say, 'Amen.'",
      "T": "'Cursed is anyone who does not hold this entire law in place by living it out.' The twelfth and final curse is the comprehensive one: it covers everything the previous eleven did not name. The law is not a menu; it is a whole. To treat it selectively is to fall under this curse. All Israel answers: 'Amen.'"
    }
  },
  "28": {
    "1": {
      "L": "And if you faithfully obey the voice of the LORD your God, being careful to do all his commandments that I command you today, the LORD your God will set you high above all the nations of the earth.",
      "M": "If you fully obey the LORD your God and carefully follow all his commands I give you today, the LORD your God will set you high above all the nations on earth.",
      "T": "If you hear the voice of the LORD your God and take care to do every commandment given today — not selectively, but all of them — the LORD will lift you above every nation on earth."
    },
    "2": {
      "L": "And all these blessings shall come upon you and overtake you, if you obey the voice of the LORD your God.",
      "M": "All these blessings will come upon you and overtake you if you obey the LORD your God.",
      "T": "These blessings will not wait for you to arrive at them — they will overtake you. Obedience will be outrun by blessing."
    },
    "3": {
      "L": "Blessed shall you be in the city, and blessed shall you be in the field.",
      "M": "You will be blessed in the city and blessed in the country.",
      "T": "Wherever you are — city or open field — blessing will find you there."
    },
    "4": {
      "L": "Blessed shall be the fruit of your womb, the fruit of your ground, and the fruit of your cattle — the increase of your herds and the young of your flock.",
      "M": "The fruit of your womb will be blessed, and the crops of your land, and the young of your livestock — the calves of your herds and the lambs of your flocks.",
      "T": "Blessing on your children, blessing on your crops, blessing on your livestock — calves and lambs born healthy and multiplying. The whole created economy of your household will flourish."
    },
    "5": {
      "L": "Blessed shall be your basket and your kneading bowl.",
      "M": "Your basket and your kneading bowl will be blessed.",
      "T": "The basket you bring to harvest, the bowl where bread is made — the ordinary vessels of daily sustenance — blessed."
    },
    "6": {
      "L": "Blessed shall you be when you come in, and blessed shall you be when you go out.",
      "M": "You will be blessed when you come in and blessed when you go out.",
      "T": "Coming in, going out — the full arc of your day — under blessing."
    },
    "7": {
      "L": "The LORD will cause your enemies who rise against you to be defeated before you. They shall come out against you one way and flee before you seven ways.",
      "M": "The LORD will cause the enemies who rise up against you to be defeated before you. They will come at you from one direction but flee from you in seven.",
      "T": "Your enemies will march on you in formation — and scatter in seven directions before you. The LORD will rout them. Military coherence against you will collapse into chaos."
    },
    "8": {
      "L": "The LORD will command the blessing on you in your barns and in all that you undertake. And he will bless you in the land that the LORD your God is giving you.",
      "M": "The LORD will send a blessing on your barns and on everything you put your hand to. He will bless you in the land the LORD your God is giving you.",
      "T": "The LORD commands blessing into your storehouses, into every enterprise you begin. The blessing is not accidental — the LORD sends it, actively, into the land he gives."
    },
    "9": {
      "L": "The LORD will establish you as a people holy to himself, as he has sworn to you, if you keep the commandments of the LORD your God and walk in his ways.",
      "M": "The LORD will establish you as his holy people, as he swore to you, if you keep his commands and walk in his ways.",
      "T": "The LORD will establish you as the people he swore you would be — a holy people, set apart to him. But this establishment requires your faithfulness: keep his commands, walk in his ways. Holiness is not automatic; it is covenantal."
    },
    "10": {
      "L": "And all the peoples of the earth shall see that you are called by the name of the LORD, and they shall be afraid of you.",
      "M": "All the peoples of the earth will see that you bear the name of the LORD, and they will be in awe of you.",
      "T": "The nations will see that the LORD's name is on you — that you are claimed, identified, marked as his — and awe will take hold of them. Israel's faithfulness becomes a testimony to the nations about who the LORD is."
    },
    "11": {
      "L": "And the LORD will make you abound in prosperity — in the fruit of your womb and in the fruit of your livestock and in the fruit of your ground — in the land that the LORD swore to your fathers to give you.",
      "M": "The LORD will grant you abundant prosperity — in the fruit of your body, in the offspring of your livestock, and in the produce of your soil — in the land he swore to give your ancestors.",
      "T": "The LORD will make you overflow — children, animals, crops — in the land he promised your fathers. Abundance in every dimension of life in the land."
    },
    "12": {
      "L": "The LORD will open to you his good treasury, the heavens, to give the rain to your land in its season and to bless all the work of your hands. And you shall lend to many nations, but you shall not borrow.",
      "M": "The LORD will open his abundant storehouse — the sky — to send rain on your land in season and to bless all your work. You will lend to many nations but will borrow from none.",
      "T": "The LORD opens heaven itself — his treasury — and sends rain at the right time to your land, blessing every project you undertake. You become a creditor nation, lending to many, borrowing from none. Blessing reverses the posture of weakness."
    },
    "13": {
      "L": "And the LORD will make you the head and not the tail, and you shall only go up and not down, if you obey the commandments of the LORD your God, which I command you today, being careful to do them,",
      "M": "The LORD will make you the head, not the tail; you will always rise, never fall — if you listen to the commands of the LORD your God that I give you today and follow them carefully,",
      "T": "The LORD will make you the head — the leading nation — not the tail, the subordinate follower. Up, not down. But this elevation is conditional: only if you obey, carefully and completely, every commandment given today —"
    },
    "14": {
      "L": "and if you do not turn aside from any of the words that I command you today, to the right hand or to the left, to go after other gods to serve them.",
      "M": "and if you do not turn aside from any of the commands I give you today, to the right or to the left, by going after other gods to serve them.",
      "T": "and if you do not veer left or right from everything commanded today — most critically, if you do not drift after other gods to serve them. That single drift undoes everything."
    },
    "15": {
      "L": "But if you will not obey the voice of the LORD your God or be careful to do all his commandments and his statutes that I command you today, then all these curses shall come upon you and overtake you.",
      "M": "But if you do not obey the LORD your God and do not carefully follow all his commands and statutes I give you today, all these curses will come on you and overtake you.",
      "T": "But if you will not hear the LORD's voice — if you refuse the full weight of his commandments and statutes — then everything that follows will come upon you. The curses will not wait for you either. They will pursue and overtake you, just as the blessings would have."
    },
    "16": {
      "L": "Cursed shall you be in the city, and cursed shall you be in the field.",
      "M": "You will be cursed in the city and cursed in the country.",
      "T": "The blessing catalog is now inverted. Cursed in the city. Cursed in the field. Nowhere is exempt."
    },
    "17": {
      "L": "Cursed shall be your basket and your kneading bowl.",
      "M": "Your basket and your kneading bowl will be cursed.",
      "T": "The vessels of daily sustenance — now cursed. What should have held bread holds nothing."
    },
    "18": {
      "L": "Cursed shall be the fruit of your womb and the fruit of your ground, the increase of your herds and the young of your flock.",
      "M": "The fruit of your womb will be cursed, along with the crops of your land, the calves of your herds, and the lambs of your flocks.",
      "T": "Children, crops, livestock — the whole life of the land, cursed at its source."
    },
    "19": {
      "L": "Cursed shall you be when you come in, and cursed shall you be when you go out.",
      "M": "You will be cursed when you come in and cursed when you go out.",
      "T": "Coming in, going out — no moment of the day escapes the shadow."
    },
    "20": {
      "L": "The LORD will send on you curses, confusion, and frustration in all that you undertake to do, until you are destroyed and perish quickly on account of the evil of your deeds, because you have forsaken me.",
      "M": "The LORD will send on you disaster, confusion, and failure in everything you undertake, until you are quickly destroyed and perish — because of the evil you have done in forsaking him.",
      "T": "The LORD himself sends the curses — not random misfortune but directed judgment: confusion, futility, and failure in every enterprise, until you are swiftly destroyed. The source of all of it is stated plainly: you have forsaken him."
    },
    "21": {
      "L": "The LORD will make the pestilence stick to you until he has consumed you off the land that you are entering to take possession of it.",
      "M": "The LORD will plague you with disease until he has wiped you out from the land you are entering to possess.",
      "T": "Plague will cling to you — not visiting and passing, but clinging — until it has consumed you out of the land you were given."
    },
    "22": {
      "L": "The LORD will strike you with wasting disease and with fever, inflammation and fiery heat, and with drought and with blight and with mildew. They shall pursue you until you perish.",
      "M": "The LORD will strike you with tuberculosis, fever, inflammation, scorching heat, and drought — with blight and mildew. These afflictions will pursue you until you perish.",
      "T": "Wasting sickness, burning fever, inflammation, scorching heat — and then the land itself turns against you: drought, blight, mildew on the grain. These are not separate punishments; they are a coordinated pursuit until you are finished."
    },
    "23": {
      "L": "And the heavens over your head shall be bronze, and the earth under you shall be iron.",
      "M": "The sky above you will be like bronze, the ground beneath you like iron.",
      "T": "Sky of bronze: no rain falls. Ground of iron: nothing penetrates, nothing grows. Heaven shut above, earth closed below — a total reversal of the creation's generosity."
    },
    "24": {
      "L": "The LORD will make the rain of your land powder. From heaven dust shall come down on you until you are destroyed.",
      "M": "The LORD will turn the rain of your land into dust and powder; it will come down from the sky until you are destroyed.",
      "T": "Where rain should fall, dust falls instead — powder drifting down from a sky that should be giving water. The blessing of rain becomes its mockery."
    },
    "25": {
      "L": "The LORD will cause you to be defeated before your enemies. You shall go out one way against them and flee seven ways before them. And you shall be a horror to all the kingdoms of the earth.",
      "M": "The LORD will cause you to be routed before your enemies. You will march out against them from one direction but flee in seven — you will become a thing of horror to all the kingdoms of the earth.",
      "T": "The military picture is perfectly inverted from the blessing: you march out in formation and scatter in seven directions before your enemies. The nations that would have feared you will shudder at your ruin instead."
    },
    "26": {
      "L": "And your dead body shall be food for all birds of the air and for the beasts of the earth, and there shall be no one to frighten them away.",
      "M": "Your dead bodies will become food for all the birds and the wild animals, and there will be no one to frighten them away.",
      "T": "The fallen are left in the field without burial — the ultimate degradation in the ancient world. No one to drive away the scavengers. No dignity in death for those who refused dignity in covenant."
    },
    "27": {
      "L": "The LORD will strike you with the boils of Egypt, and with tumors and scabs and itch, of which you cannot be healed.",
      "M": "The LORD will afflict you with the boils of Egypt and with tumors, festering sores, and an itch that cannot be healed.",
      "T": "The plagues of Egypt — which were judgment on your oppressors — will now fall on you. Boils, tumors, festering sores, unrelenting itch. You will carry Egypt's judgment in your own flesh."
    },
    "28": {
      "L": "The LORD will strike you with madness and blindness and confusion of mind,",
      "M": "The LORD will afflict you with madness, blindness, and confusion of mind.",
      "T": "The inner world collapses alongside the outer: madness, blindness, bewilderment — the mind itself becomes the site of the curse."
    },
    "29": {
      "L": "and you shall grope at noonday as the blind grope in darkness, and you shall not prosper in your ways. And you shall be only oppressed and robbed continually, and there shall be no one to help you.",
      "M": "At midday you will grope about like a blind person in the dark. You will be unsuccessful in everything you do; day after day you will be oppressed and robbed, with no one to rescue you.",
      "T": "At high noon — when sight should be most certain — you will grope like a man blind in darkness. Everything you attempt will come to nothing. You will be perpetually robbed, perpetually oppressed, and no one will come."
    },
    "30": {
      "L": "You shall betroth a wife, but another man shall ravish her. You shall build a house, but you shall not dwell in it. You shall plant a vineyard, but you shall not enjoy its fruit.",
      "M": "You will be pledged to a woman, but another man will sleep with her. You will build a house, but you will not live in it. You will plant a vineyard, but you will not enjoy its fruit.",
      "T": "Every investment of love, labor, and hope will be stolen from you before you can enjoy it. Your betrothed taken by another man. Your house built for someone else. Your vineyard harvested by another's hands. The curse is not merely poverty — it is dispossession of what you yourself created."
    },
    "31": {
      "L": "Your ox shall be slaughtered before your eyes, but you shall not eat any of it. Your donkey shall be seized before your face, but it shall not be restored to you. Your sheep shall be given to your enemies, and there shall be no one to help you.",
      "M": "Your ox will be slaughtered in your sight, but you will eat none of it. Your donkey will be stolen right in front of you and not returned. Your sheep will be handed over to your enemies, and no one will rescue them.",
      "T": "Your animals killed or taken while you watch, helpless. Your ox slaughtered before your eyes and not a mouthful given to you. Your donkey seized, your flock handed to enemies. Ownership becomes a torment: you possess and immediately lose."
    },
    "32": {
      "L": "Your sons and your daughters shall be given to another people, while your eyes look on and fail with longing for them all day long, but you shall be helpless.",
      "M": "Your sons and daughters will be given to another nation while you watch — your eyes straining with longing for them all day long, but powerless to do anything.",
      "T": "Your children will be taken — given to a foreign nation — while you stand and watch. Your eyes will scan the horizon for them until they fail. And you will have no power to stop it. This is the cruelest catalog entry: not property lost, but children."
    },
    "33": {
      "L": "A nation that you have not known shall eat up the fruit of your ground and all your labors, and you shall be only oppressed and crushed continually,",
      "M": "A nation you do not know will devour the produce of your soil and all your labor. You will be oppressed and crushed relentlessly,",
      "T": "Everything your labor has produced — the fruit of your ground, all your work — will be consumed by a people you do not even know. You will be oppressed and ground down without pause."
    },
    "34": {
      "L": "so that you are driven mad by the sights that your eyes see.",
      "M": "until you are driven mad by what you see.",
      "T": "What your own eyes witness will drive you insane. There is no emotional resource left for what is coming."
    },
    "35": {
      "L": "The LORD will strike you on the knees and on the legs with grievous boils of which you cannot be healed, from the sole of your foot to the crown of your head.",
      "M": "The LORD will afflict your knees and legs with painful, incurable boils — from the sole of your foot to the top of your head.",
      "T": "The disease works from the ground up: sores on the feet and legs that will not heal, spreading upward without stopping. The body becomes uninhabitable."
    },
    "36": {
      "L": "The LORD will bring you and your king whom you set over you to a nation that neither you nor your fathers have known. And there you shall serve other gods of wood and stone.",
      "M": "The LORD will drive you and the king you set over you to a nation unknown to you or your ancestors, where you will serve gods of wood and stone.",
      "T": "Exile. You and your king — whoever you elevated — will be marched to a land you have never known. And there, in a land where the LORD seems absent, you will end up serving the idols of wood and stone that this very law forbids. Exile undoes everything."
    },
    "37": {
      "L": "And you shall become a horror, a proverb, and a byword among all the peoples where the LORD will lead you away.",
      "M": "You will become a thing of horror and an object of ridicule and mockery among all the nations where the LORD drives you.",
      "T": "Among the nations you will become a proverb — a cautionary tale, a subject for mockery. 'Did you hear what happened to Israel?' The name that should have carried honor becomes a byword for catastrophe."
    },
    "38": {
      "L": "You shall carry much seed into the field and shall gather in little, for the locust shall devour it.",
      "M": "You will plant much seed but harvest little, because locusts will eat it.",
      "T": "You plant generously — and locusts devour before you can harvest. Effort without return."
    },
    "39": {
      "L": "You shall plant vineyards and dress them, but you shall neither drink of the wine nor gather the grapes, for the worm shall eat them.",
      "M": "You will plant and tend vineyards but drink no wine and gather no grapes, because worms will eat them.",
      "T": "You plant a vineyard, tend every vine — and worms consume it before a grape can be gathered. The care you pour into the land produces nothing for you."
    },
    "40": {
      "L": "You shall have olive trees throughout all your territory, but you shall not anoint yourself with the oil, for your olives shall drop off.",
      "M": "You will have olive trees throughout your land but will not use the oil, because the olives will drop off.",
      "T": "Olive trees across the land — and the olives fall before they ripen. No oil for food, for lamp, for anointing. The trees stand like promises that are never kept."
    },
    "41": {
      "L": "You shall father sons and daughters, but they shall not be yours, for they shall go into captivity.",
      "M": "You will have sons and daughters but you will not keep them, because they will go into captivity.",
      "T": "You will raise children — and they will be taken. Captivity empties the household of its future. You are a parent without children to show for it."
    },
    "42": {
      "L": "The cricket shall possess all your trees and the fruit of your ground.",
      "M": "Swarms of locusts will take over all your trees and the crops of your land.",
      "T": "The insects inherit what you cannot keep. Your land, your trees, your crops — all pass to creatures that feel nothing about your loss."
    },
    "43": {
      "L": "The sojourner who is among you shall rise higher and higher above you, and you shall come down lower and lower.",
      "M": "The foreigner living among you will rise higher and higher while you sink lower and lower.",
      "T": "The foreigner in your midst — the one who was supposed to depend on your charity — will rise above you while you descend. Social hierarchy inverted: the immigrant climbs while the native sinks."
    },
    "44": {
      "L": "He shall lend to you, and you shall not lend to him. He shall be the head, and you shall be the tail.",
      "M": "He will lend to you, but you will not lend to him. He will be the head, and you will be the tail.",
      "T": "He lends; you borrow. He leads; you follow. The blessing of being the head and not the tail has perfectly reversed. Every category of the blessing becomes a category of curse."
    },
    "45": {
      "L": "All these curses shall come upon you and pursue you and overtake you until you are destroyed, because you did not obey the voice of the LORD your God, to keep his commandments and his statutes that he commanded you.",
      "M": "All these curses will come upon you. They will pursue and overtake you until you are destroyed, because you did not obey the LORD your God and observe the commands and decrees he gave you.",
      "T": "Everything listed will come. Nothing listed will be avoided. The curses pursue and overtake — using the same language as the blessings that would have done the same. The reason: you did not obey the voice of the LORD your God."
    },
    "46": {
      "L": "They shall be a sign and a wonder against you and your offspring forever.",
      "M": "They will be a sign and a wonder against you and your descendants forever.",
      "T": "The curses themselves will become a sign — visible evidence, for all generations to come, of what covenant unfaithfulness costs. The destruction of Israel is not simply an event; it is a warning written in history."
    },
    "47": {
      "L": "Because you did not serve the LORD your God with joyfulness and gladness of heart, because of the abundance of all things,",
      "M": "Because you did not serve the LORD your God joyfully and gladly in the time of prosperity,",
      "T": "The indictment is precise: not that you failed in adversity, but that you refused to serve the LORD with joy and gladness when you had everything — when abundance surrounded you and gratitude was the only reasonable response."
    },
    "48": {
      "L": "therefore you shall serve your enemies whom the LORD will send against you, in hunger and thirst, in nakedness, and lacking everything. And he will put a yoke of iron on your neck until he has destroyed you.",
      "M": "you will serve the enemies the LORD sends against you in hunger, thirst, nakedness, and dire poverty. He will put an iron yoke on your neck until he has destroyed you.",
      "T": "You would not serve the LORD freely, in joy — so you will serve enemies in chains: hungry, thirsty, naked, destitute. An iron yoke on your neck until you are consumed. The service you refused in freedom becomes the service you endure in slavery."
    },
    "49": {
      "L": "The LORD will bring a nation against you from far away, from the end of the earth, swooping down like an eagle, a nation whose language you do not understand,",
      "M": "The LORD will bring against you a nation from far away, from the ends of the earth, that swoops down like an eagle — a nation whose language you will not understand,",
      "T": "A nation from the far edge of the world will descend on you like an eagle striking — fast, merciless, from a height you cannot anticipate. You will not speak their language. There will be no negotiation. They are the instrument of the LORD's judgment."
    },
    "50": {
      "L": "a hard-faced nation who shall not respect the old or show mercy to the young.",
      "M": "a fierce-looking nation without respect for the old or pity for the young.",
      "T": "They are relentless: no deference to age, no mercy to youth. The two categories that every human culture instinctively protects — the elderly and children — these will find no protection from this enemy."
    },
    "51": {
      "L": "It shall eat the offspring of your cattle and the fruit of your ground, until you are destroyed — also leaving you neither grain nor wine nor oil, nor the increase of your herds or the young of your flock, until they have caused you to perish.",
      "M": "They will devour the young of your livestock and the crops of your land until you are destroyed. They will leave you no grain, new wine, or olive oil, nor the calves of your herds or the lambs of your flocks until they have ruined you.",
      "T": "They consume everything: livestock, crops, grain, wine, oil — methodically, until nothing remains and you are ruined. Not accidental. Systematic. The ancient economy of blessing in reverse."
    },
    "52": {
      "L": "They shall besiege you in all your towns until your high and fortified walls — in which you trusted — come down throughout all your land. And they shall besiege you in all your towns throughout all your land that the LORD your God has given you.",
      "M": "They will lay siege to all your cities throughout your land until the high, fortified walls in which you trusted fall down. They will besiege all the cities throughout the land the LORD your God has given you.",
      "T": "The siege comes to every city. The high walls you built and trusted — they will come down. The land the LORD gave you becomes a geography of sieges, one after another, until the last fortification falls."
    },
    "53": {
      "L": "And you shall eat the fruit of your womb — the flesh of your sons and daughters whom the LORD your God has given you — in the siege and in the distress with which your enemy shall distress you.",
      "M": "In the desperation of the siege your enemies impose on you, you will eat the flesh of your own children — your sons and daughters whom the LORD your God has given you.",
      "T": "The siege reaches its most terrible depth: starvation so complete that parents consume their children. This is not rhetorical exaggeration — it happened during the siege of Jerusalem (2 Kings 6; Lamentations 4). The curse names the absolute bottom of human degradation."
    },
    "54": {
      "L": "The man who is the most tender and refined among you will begrudge food to his brother, to the wife he embraces, and to the last of his children whom he has left,",
      "M": "Even the most sensitive and refined man among you will become stingy with his brother, the wife he loves, and his surviving children,",
      "T": "The man of refinement and sensitivity — the one you would have expected to be last to crack — will look at his own brother, his beloved wife, his remaining children with a miser's eye."
    },
    "55": {
      "L": "so that he will not give to any of them any of the flesh of his children whom he is eating, because he has nothing left for himself, in the siege and in the distress with which your enemy shall distress you in all your towns.",
      "M": "refusing to share with any of them the flesh of his own children that he is eating — because nothing is left. Such is the distress your enemy will inflict on you in all your towns.",
      "T": "He will not share even a morsel of his children's flesh with the people he once loved most. The siege has reduced him to something he could not have imagined himself becoming. This is what the absence of covenant faithfulness ultimately produces."
    },
    "56": {
      "L": "The most tender and refined woman among you, who would not venture to set the sole of her foot on the ground because she was so delicate and refined, will begrudge to the husband she embraces and to her son and to her daughter",
      "M": "The most delicate and sensitive woman among you — so refined she would never place her foot on the ground — will begrudge the husband she loves and her son and daughter",
      "T": "And the woman of greatest delicacy — the one whose life was sheltered, who barely let her feet touch the ground — she too will turn with a miser's gaze on her husband, her son, her daughter."
    },
    "57": {
      "L": "her afterbirth that comes out from between her feet and her children whom she bears, because she will eat them secretly, for lack of all things, in the siege and in the distress with which your enemy shall distress you in your towns.",
      "M": "even the afterbirth from her womb and the children she bears — she will secretly eat them, so dire will be her need during the siege your enemies will impose on all your towns.",
      "T": "She will consume in secret what no language can adequately describe — the afterbirth, her newborn — because the siege has taken everything and she has nothing. This is the terminus of the curses, the uttermost point of what covenant breach costs. Moses names it because it happened, and it will happen again."
    },
    "58": {
      "L": "If you are not careful to do all the words of this law that are written in this book, that you may fear this glorious and awesome name — the LORD your God —",
      "M": "If you do not carefully follow all the words of this law, which are written in this book, and do not revere this glorious and awesome name — the LORD your God —",
      "T": "After all that has been described, the condition is restated: if you will not keep every word of this law, written in this book — if you will not stand in awe of the LORD your God whose name is glorious and terrifying —"
    },
    "59": {
      "L": "then the LORD will bring on you and your offspring extraordinary afflictions — afflictions severe and lasting, and sicknesses grievous and lasting.",
      "M": "the LORD will send you and your descendants extraordinary disasters — severe and prolonged plagues, terrible and lingering sicknesses.",
      "T": "the LORD will make your plagues extraordinary: severe, prolonged, unprecedented. The sicknesses: grievous, lasting, refusing to lift. The word 'extraordinary' in Hebrew is the same word used for the miracles of the Exodus — the same intensity of divine action, now in judgment."
    },
    "60": {
      "L": "And he will bring upon you again all the diseases of Egypt, of which you were afraid, and they shall cling to you.",
      "M": "He will bring on you all the diseases of Egypt that you dreaded, and they will cling to you.",
      "T": "The plagues of Egypt — from which Israel was specifically protected — will be turned on Israel. Everything you were rescued from, everything that terrified you watching your oppressors suffer, will now cling to you."
    },
    "61": {
      "L": "Also every sickness and every affliction that is not recorded in the book of this law, the LORD will bring upon you until you are destroyed.",
      "M": "The LORD will also bring on you every kind of sickness and disaster not recorded in this Book of the Law, until you are destroyed.",
      "T": "And the list is not exhaustive. Every disease and disaster not even named here — the LORD will bring that too. The catalog of curses has no floor."
    },
    "62": {
      "L": "Whereas you were as numerous as the stars of heaven, you shall be left few in number, because you did not obey the voice of the LORD your God.",
      "M": "You who were as numerous as the stars in the sky will be left but few in number, because you did not obey the LORD your God.",
      "T": "The stars of heaven were the promise — countless descendants for Abraham. That promise does not cancel the curse. You will be reduced to a remnant, few in number, because you refused the voice that gave you the stars."
    },
    "63": {
      "L": "And as the LORD took delight in doing you good and multiplying you, so the LORD will take delight in bringing ruin on you and destroying you. And you shall be plucked off the land that you are entering to take possession of it.",
      "M": "Just as the LORD delighted in making you prosper and multiply, so he will delight in bringing you to ruin and destruction. You will be torn from the land you are entering to possess.",
      "T": "The same divine energy that delighted in blessing you will be turned to your undoing — with the same focus, the same intensity. This is the most sobering statement in the passage: the LORD who loved to bless will not be reluctant when judgment comes. You will be uprooted from the land entirely."
    },
    "64": {
      "L": "And the LORD will scatter you among all peoples, from one end of the earth to the other, and there you shall serve other gods of wood and stone, which neither you nor your fathers have known.",
      "M": "The LORD will scatter you among all nations, from one end of the earth to the other. There you will serve gods of wood and stone that neither you nor your ancestors have known.",
      "T": "Scattered. Among all peoples. From one edge of the world to the other. No community, no land, no temple. And in that diaspora, in the spiritual disorientation of exile, you will find yourselves doing what the law absolutely forbids: serving the idols of nations you never knew."
    },
    "65": {
      "L": "Among those nations you shall find no respite, and there shall be no resting place for the sole of your foot. The LORD will give you a trembling heart and failing eyes and a despairing soul.",
      "M": "Among those nations you will find no repose, no resting place for the sole of your foot. There the LORD will give you an anxious mind, failing eyes, and a despairing heart.",
      "T": "No rest anywhere. No place where your foot can settle and say: this is home. The LORD will give you an anxious heart — always unsettled, always afraid — and eyes that fail from searching for something they cannot find, and a spirit that has given up."
    },
    "66": {
      "L": "Your life shall hang in doubt before you. Night and day you shall be in dread and have no assurance of your life.",
      "M": "Your life will hang in the balance — you will live in constant dread, day and night, never sure of your survival.",
      "T": "Your life will hang suspended — not quite lost, not secure — day and night, never certain whether the next moment is the last. This is the psychological experience of exile: perpetual precarity."
    },
    "67": {
      "L": "In the morning you shall say, 'If only it were evening!' and at evening you shall say, 'If only it were morning!' — because of the dread that your heart shall feel, and the sights that your eyes shall see.",
      "M": "In the morning you will say, 'If only it were evening!' and in the evening you will say, 'If only it were morning!' — because of the terror that grips your heart and the sights that your eyes will see.",
      "T": "Morning will come and you will wish for night — to stop seeing. Evening will come and you will wish for morning — to stop lying awake in terror. The passage of time offers no relief, only the alternation of two kinds of suffering. What your eyes have seen cannot be unseen."
    },
    "68": {
      "L": "And the LORD will bring you back in ships to Egypt, a journey that I promised you, 'You shall never see it again.' And there you shall offer yourselves for sale to your enemies as male and female slaves, but there will be no buyer.",
      "M": "The LORD will send you back to Egypt in ships, along a route I said you would never travel again. There you will offer yourselves for sale as male and female slaves, but no one will buy you.",
      "T": "The final curse is a terrible irony: return to Egypt — the very place the LORD delivered you from — not as a conquered people marched overland, but as cargo shipped across the sea. You will try to sell yourselves into slavery, to at least have a master's protection, and find that you are worth nothing. No one will buy. The end of the covenant curse is not captivity — it is abandonment so complete that even captivity is unavailable."
    }
  },
  "29": {
    "1": {
      "L": "These are the words of the covenant that the LORD commanded Moses to make with the people of Israel in the land of Moab, besides the covenant that he had made with them at Horeb.",
      "M": "These are the terms of the covenant the LORD commanded Moses to make with the Israelites in Moab, in addition to the covenant he had made with them at Horeb.",
      "T": "A second covenant. The Horeb covenant is not replaced — this Moab covenant supplements it. Two covenants, the same LORD, the same people, the same obligations now restated as Israel stands on the edge of the land."
    },
    "2": {
      "L": "And Moses summoned all Israel and said to them: 'You have seen all that the LORD did before your eyes in the land of Egypt — to Pharaoh and to all his servants and to all his land —",
      "M": "Moses summoned all Israel and said to them: 'You have seen with your own eyes everything the LORD did in Egypt to Pharaoh, to all his officials, and to his whole land —",
      "T": "'You were there,' Moses begins. 'You saw it with your own eyes — what the LORD did in Egypt: to Pharaoh, to his officials, to the whole land.'"
    },
    "3": {
      "L": "the great trials that your eyes saw, the signs and those great wonders.",
      "M": "those great trials, the signs and wonders you saw with your own eyes.",
      "T": "The trials were great. The signs unmistakable. The wonders beyond any natural explanation. Israel stood there and watched. Memory of what was seen is the foundation of what is now required."
    },
    "4": {
      "L": "But to this day the LORD has not given you a heart to understand or eyes to see or ears to hear.",
      "M": "Yet to this day the LORD has not given you a mind that understands or eyes that see or ears that hear.",
      "T": "And yet — to this day — the LORD has not given you a heart to understand what you witnessed. Eyes that see but do not perceive. Ears that hear but do not comprehend. Seeing and understanding are not the same thing; full comprehension is itself a divine gift."
    },
    "5": {
      "L": "I have led you forty years in the wilderness. Your clothes have not worn out on you, and your sandals have not worn off your feet.",
      "M": "For forty years I led you through the wilderness. Your clothes did not wear out, and your sandals did not wear out on your feet.",
      "T": "Forty years in the wilderness. Clothing that did not wear out. Sandals that did not fail. The miracle of provision was so ordinary, so constant, that it became invisible. This is what Israel did not perceive: that the everyday sustaining of their lives was itself an act of God."
    },
    "6": {
      "L": "You have not eaten bread, and you have not drunk wine or strong drink, so that you might know that I am the LORD your God.",
      "M": "You ate no bread and drank no wine or other fermented drink — so that you would know that I am the LORD your God.",
      "T": "No bread from agriculture. No wine from viticulture. The normal economy was suspended so that you would have to see: your life came directly from the LORD. Every meal in the wilderness was a testimony. Did you take the testimony seriously?"
    },
    "7": {
      "L": "And when you came to this place, Sihon the king of Heshbon and Og the king of Bashan came out against us to battle, but we defeated them.",
      "M": "When you reached this place, Sihon king of Heshbon and Og king of Bashan came out to fight against us, and we defeated them.",
      "T": "At the border of the land, two kings stood against you — Sihon of Heshbon and Og of Bashan — and the LORD gave them into your hand. The military victories at the threshold of the land are part of the evidence."
    },
    "8": {
      "L": "We took their land and gave it as an inheritance to the Reubenites, the Gadites, and the half-tribe of Manasseh.",
      "M": "We took their land and gave it as an inheritance to the Reubenites, the Gadites, and the half-tribe of Manasseh.",
      "T": "The land of those defeated kings was apportioned to Reuben, Gad, and half of Manasseh — already you have seen the LORD deliver on his promise of land. The covenant works."
    },
    "9": {
      "L": "Therefore keep the words of this covenant and do them, that you may prosper in all that you do.",
      "M": "Observe the terms of this covenant and carry them out, so that you may be successful in everything you do.",
      "T": "This is the conclusion the history demands: keep the covenant. Do it. The evidence of the LORD's faithfulness across forty years and two military victories is the ground on which obedience is required. Prospering in everything you do follows from faithfulness to the terms."
    },
    "10": {
      "L": "You are standing today, all of you, before the LORD your God — your heads, your tribes, your elders, and your officers, all the men of Israel,",
      "M": "All of you are standing today in the presence of the LORD your God — your leaders and chief men, your elders and officials, and all the other men of Israel,",
      "T": "The entire covenant community stands here: leaders, elders, officials — and all the men of Israel. No rank is exempt, no person excluded. This covenant is made with everybody."
    },
    "11": {
      "L": "your little ones, your wives, and the sojourner who is in your camp, from the one who chops your wood to the one who draws your water —",
      "M": "together with your children and wives, and the foreigners living in your camp who chop your wood and carry your water.",
      "T": "And beyond the full male citizenry: your children, your wives, and the foreigners in the camp — even the woodcutters and water-carriers, the workers at the bottom of the social structure. The covenant community is more inclusive than the list of warriors."
    },
    "12": {
      "L": "so that you may enter into the sworn covenant of the LORD your God, which the LORD your God is making with you today,",
      "M": "You are here to enter into a covenant with the LORD your God, a covenant the LORD is making with you today and sealing with an oath,",
      "T": "The purpose of this gathering: to enter the covenant sworn before the LORD — a covenant ratified by oath, made today."
    },
    "13": {
      "L": "that he may establish you today as his people, and that he may be your God, as he promised you, and as he swore to your fathers, to Abraham, to Isaac, and to Jacob.",
      "M": "to confirm you this day as his people, that he may be your God as he promised you and as he swore to your ancestors Abraham, Isaac, and Jacob.",
      "T": "The covenant does two things simultaneously: it establishes you as his people and him as your God. He swore this to Abraham, Isaac, and Jacob — and that ancient oath is now sealed again with you. The covenant connects you backward through the patriarchs and forward through every generation."
    },
    "14": {
      "L": "It is not with you alone that I am making this sworn covenant,",
      "M": "I am making this covenant, with its oath, not only with you who stand here today before the LORD our God",
      "T": "This covenant is not limited to the people standing in this assembly."
    },
    "15": {
      "L": "but with those who are standing here with us today before the LORD our God, and also with those who are not here with us today.",
      "M": "but also with those who are not here with us today.",
      "T": "It reaches forward to those who are not yet born — every generation of Israel that will live under its terms. The covenant made today binds people who are not in the assembly. Covenant identity is transgenerational."
    },
    "16": {
      "L": "You know how we lived in the land of Egypt, and how we came through the midst of the nations through which you passed.",
      "M": "You remember how we lived in Egypt and how we traveled through the nations on your way here.",
      "T": "You know the road you traveled. You know Egypt. You passed through foreign nations and saw their ways."
    },
    "17": {
      "L": "And you have seen their detestable things, their idols of wood and stone, of silver and gold, that were among them.",
      "M": "You saw their detestable images — their idols of wood, stone, silver, and gold.",
      "T": "You saw what the nations worship: their idols of wood, stone, silver, gold — detestable things, beautiful to look at, utterly empty. You have seen what the alternative to the LORD actually is."
    },
    "18": {
      "L": "Beware lest there be among you a man or woman or clan or tribe whose heart is turning away today from the LORD our God to go and serve the gods of those nations. Beware lest there be among you a root bearing poisonous and bitter fruit —",
      "M": "Make sure there is no man or woman, clan or tribe among you today whose heart turns away from the LORD our God to go and worship the gods of those nations. Make sure there is no root among you that produces such bitter poison —",
      "T": "Watch carefully. The danger is not always visible: a heart turning away in secret, a root of bitterness growing underground, a person who has seen the idols and been drawn to them without anyone knowing. One root of apostasy left alive will spread."
    },
    "19": {
      "L": "one who, when he hears the words of this sworn covenant, blesses himself in his heart, saying, 'I shall be safe, though I walk in the stubbornness of my heart.' This will lead to the sweeping away of moist and dry alike.",
      "M": "one who hears the terms of this oath and yet reassures himself, thinking, 'I will be safe, even though I persist in going my own way.' This attitude will bring disaster on the whole community.",
      "T": "The most dangerous person in the assembly is the one who hears every word of this covenant — the blessings, the curses, the warnings — and privately tells himself: 'I'll be fine. I'll do as I please and nothing bad will happen to me.' That self-deception is not merely personal error; it is poison. The moist and the dry both go down together."
    },
    "20": {
      "L": "The LORD will not be willing to forgive him, but rather the anger of the LORD and his jealousy will smoke against that man, and every curse written in this book will settle on him, and the LORD will blot out his name from under heaven.",
      "M": "The LORD will never pardon him. Instead, the LORD's anger and his jealousy will burn against that person; all the curses written in this book will fall on him and the LORD will blot out his name from under heaven.",
      "T": "The LORD will not forgive this man. His anger and his jealousy — the fierce covenantal love that will not share his people with idols — will burn against him. Every curse in this book comes to rest on him personally. And his name will be erased from under heaven. He wanted to disappear into the crowd — instead he is singled out for complete obliteration."
    },
    "21": {
      "L": "And the LORD will single him out from all the tribes of Israel for calamity, in accordance with all the curses of the covenant written in this Book of the Law.",
      "M": "The LORD will single him out from all the tribes of Israel for disaster, in keeping with all the curses of the covenant written in this Book of the Law.",
      "T": "The man who tried to hide among the tribes — who thought his private apostasy was safe — will be extracted and identified. The LORD singles him out. There is no hiding in the crowd from a covenant LORD who sees every heart."
    },
    "22": {
      "L": "And the generation to come, your children who rise up after you, and the foreigner who comes from a far land, will say, when they see the afflictions of that land and the sicknesses with which the LORD has made it sick —",
      "M": "Your descendants who follow you and foreigners who come from distant lands will see the calamities that fall on that land and the diseases with which the LORD has afflicted it.",
      "T": "Future generations — your own descendants and foreigners who come to see — will look on the ruined land and the diseases that have struck it, and they will ask the inevitable question:"
    },
    "23": {
      "L": "the whole land burned out with brimstone and salt, nothing sown and nothing growing, where no plant can sprout, an overthrow like that of Sodom and Gomorrah, Admah, and Zeboiim, which the LORD overthrew in his anger and wrath —",
      "M": "They will see the whole land laid waste with burning sulfur and salt — nothing planted, nothing sprouting, no vegetation growing on it. It will be like the destruction of Sodom and Gomorrah, Admah and Zeboyim, which the LORD overthrew in fierce anger.",
      "T": "The land will look like Sodom — sulfur, salt, no seed taking root, no plant growing. The very soil sterile. And every visitor will know: this is what divine wrath looks like when it falls on a people who violated their covenant. Sodom stands in Scripture as the paradigm of total judgment; Israel's unfaithfulness could bring Israel to the same place."
    },
    "24": {
      "L": "all the nations will ask, 'Why has the LORD done thus to this land? What caused this great outburst of anger?'",
      "M": "All the nations will ask: 'Why has the LORD done this to this land? Why this fierce, burning anger?'",
      "T": "'Why?' the nations ask. 'What did this people do? What could provoke the LORD of all creation to destroy the very land he gave?' The question is the opening for the testimony."
    },
    "25": {
      "L": "Then people will say, 'It is because they abandoned the covenant of the LORD, the God of their fathers, which he made with them when he brought them out of the land of Egypt,",
      "M": "And the answer will be: 'It is because this people abandoned the covenant of the LORD, the God of their ancestors, the covenant he made with them when he brought them out of Egypt.",
      "T": "And the answer comes: 'Because they abandoned the covenant.' The entire catastrophe is traceable to one act: they forsook the agreement the LORD made with them when he brought them out of Egypt."
    },
    "26": {
      "L": "and went and served other gods and worshiped them — gods whom they had not known and whom he had not allotted to them.",
      "M": "They went and worshiped other gods and bowed down to them — gods they had not known, gods he had not given them.",
      "T": "They went after gods they did not know — gods the LORD had never assigned to them, gods with no claim on their allegiance whatsoever. The choice was gratuitous, inexplicable, and fatal."
    },
    "27": {
      "L": "Therefore the anger of the LORD was kindled against this land, bringing upon it all the curses written in this book,",
      "M": "Therefore the LORD's anger burned against this land, so that he brought on it all the curses written in this book.",
      "T": "The LORD's anger ignited — and he brought every curse in this book upon the land. The curses are not empty rhetoric; they are the documented terms of what covenant-breaking costs."
    },
    "28": {
      "L": "and the LORD uprooted them from their land in anger and fury and great wrath and cast them into another land, as they are to this day.'",
      "M": "In furious anger and great wrath the LORD uprooted them from their land and thrust them into another land, as it is now.'",
      "T": "In anger, in fury, in great wrath — the LORD pulled them up by the roots from the land he gave them and threw them into another land. This is the exile Moses foresees from Moab, centuries before it happens. The answer the nations will give is the one Moses is now providing in advance."
    },
    "29": {
      "L": "The secret things belong to the LORD our God, but the things that are revealed belong to us and to our children forever, that we may do all the words of this law.",
      "M": "The secret things belong to the LORD our God, but the things revealed belong to us and to our children forever, so that we may follow all the words of this law.",
      "T": "Here is the boundary: the hidden things — why specific events happen when they do, how divine providence works in detail, what God has not chosen to disclose — these belong to him. What has been revealed — this law, this covenant, these commands — belongs to us and to every generation after us, as the permanent basis of responsible living. We are not accountable for what we cannot know. We are fully accountable for what we have been given."
    }
  },
  "30": {
    "1": {
      "L": "And when all these things come upon you — the blessing and the curse, which I have set before you — and you call them to mind among all the nations where the LORD your God has driven you,",
      "M": "When all these things have happened to you — the blessings and the curses I have described — and you take them to heart among the nations where the LORD your God has scattered you,",
      "T": "When everything that has been described comes to pass — blessing and curse alike — and you find yourself in exile among the nations, and the memory of what you forfeited finally breaks through —"
    },
    "2": {
      "L": "and return to the LORD your God, you and your children, and obey his voice in all that I command you today, with all your heart and with all your soul,",
      "M": "and when you and your children return to the LORD your God and obey him with all your heart and with all your soul according to everything I command you today,",
      "T": "and you return — you and your children — to the LORD your God, obeying his voice with every part of what you are: heart, soul, the full weight of your being, in line with everything commanded today —"
    },
    "3": {
      "L": "then the LORD your God will restore your fortunes and have mercy on you, and he will gather you again from all the peoples where the LORD your God has scattered you.",
      "M": "then the LORD your God will restore your fortunes and have compassion on you, and gather you again from all the nations where he scattered you.",
      "T": "then the LORD your God will turn your captivity, will have compassion on you, will gather you in from all the nations where he scattered you. Exile is not the final word. Return is built into the covenant."
    },
    "4": {
      "L": "If your outcasts are in the uttermost parts of heaven, from there the LORD your God will gather you, and from there he will take you.",
      "M": "Even if you are exiled to the farthest horizon, the LORD your God will gather you from there and bring you back.",
      "T": "Even to the outermost edge of the world — if that is where exile has taken you — the LORD will reach. There is no distance so great that it places you beyond his gathering. This is the promise beneath the curses."
    },
    "5": {
      "L": "And the LORD your God will bring you into the land that your fathers possessed, that you may possess it. And he will make you more prosperous and numerous than your fathers.",
      "M": "The LORD your God will bring you to the land your ancestors possessed, and you will take possession of it. He will make you more prosperous and numerous than your ancestors.",
      "T": "He will bring you back to the land — your ancestral land, the land of the promise — and you will repossess it. More than that: he will multiply you and prosper you beyond the generation of your fathers. Restoration exceeds what was lost."
    },
    "6": {
      "L": "And the LORD your God will circumcise your heart and the heart of your offspring, so that you will love the LORD your God with all your heart and with all your soul, that you may live.",
      "M": "The LORD your God will circumcise your heart and the hearts of your descendants, so that you will love him with all your heart and with all your soul, and so that you may live.",
      "T": "And this is the deepest promise: the LORD will do what you have never been able to do by discipline alone. He will circumcise your heart — cut away the thick, resistant skin around it — and your children's hearts too. The result: you will love the LORD your God with your whole heart and your whole soul. Not as a commandment straining against your nature, but as what flows naturally from a heart God has opened. This is the new covenant heart that Jeremiah will later describe in full."
    },
    "7": {
      "L": "And the LORD your God will put all these curses on your enemies and on those who hate you and persecute you.",
      "M": "The LORD your God will inflict all these curses on your enemies and on those who hate and persecute you.",
      "T": "The curses do not disappear in restoration — they are redirected. What fell on Israel for unfaithfulness will fall on the enemies who persecuted Israel. The curse-list of chapter 28 becomes the fate of those who made Israel suffer."
    },
    "8": {
      "L": "And you shall again obey the voice of the LORD and keep all his commandments that I command you today.",
      "M": "You will again obey the LORD and follow all his commands I am giving you today.",
      "T": "And you will obey. Not straining against it — obey. Every commandment commanded today will be kept. The circumcised heart makes what was impossible possible."
    },
    "9": {
      "L": "The LORD your God will make you abundantly prosperous in all the work of your hand, in the fruit of your womb and in the fruit of your cattle and in the fruit of your ground. For the LORD will again take delight in prospering you, as he took delight in your fathers,",
      "M": "The LORD your God will make you most prosperous in all the work of your hands — in the children you bear, your livestock, and your crops. The LORD will again delight in your well-being, just as he delighted in your ancestors,",
      "T": "The LORD will make you overflow with prosperity — in work, in children, in animals, in crops. He will again delight in prospering you — the same delight he had in your fathers. The covenant joy returns. The LORD wants to bless; exile was the wound, restoration is the healing."
    },
    "10": {
      "L": "when you obey the voice of the LORD your God, to keep his commandments and his statutes that are written in this Book of the Law, when you turn to the LORD your God with all your heart and with all your soul.",
      "M": "if you obey the LORD your God and keep his commands and decrees written in this Book of the Law, and if you turn to him with all your heart and with all your soul.",
      "T": "All of this restoration flows through the same channel it always has: obedience to the voice of the LORD, keeping the commandments and statutes of this book, turning to him with your whole heart and soul. The law has not changed. What changes, after the circumcision of the heart, is the nature of the person keeping it."
    },
    "11": {
      "L": "For this commandment that I command you today is not too hard for you, neither is it far off.",
      "M": "Now what I am commanding you today is not too difficult for you or beyond your reach.",
      "T": "Moses answers the objection before it is raised: this is not too hard. It is not some transcendent, unreachable standard that only perfect people could meet. The commandment is not in a realm you cannot enter."
    },
    "12": {
      "L": "It is not in heaven, that you should say, 'Who will ascend to heaven for us and bring it to us, that we may hear it and do it?'",
      "M": "It is not up in heaven, so that you have to ask, 'Who will ascend into heaven to get it and proclaim it to us so we can obey it?'",
      "T": "It is not in heaven — as if you needed a heavenly mediator to retrieve a divine secret and bring it down to earth for you. No one has to make that journey. The law is not stored somewhere inaccessible."
    },
    "13": {
      "L": "Neither is it beyond the sea, that you should say, 'Who will go over the sea for us and bring it to us, that we may hear it and do it?'",
      "M": "Nor is it beyond the sea, so that you have to ask, 'Who will cross the sea to get it and proclaim it to us so we can obey it?'",
      "T": "It is not across the sea — beyond the known world, requiring a voyage into the unknown. No one has to travel there on your behalf. The commandment is not hidden in the distant, the exotic, the inaccessible."
    },
    "14": {
      "L": "But the word is very near you. It is in your mouth and in your heart, so that you can do it.",
      "M": "No, the word is very near you; it is in your mouth and in your heart so you may obey it.",
      "T": "The word is very near you. In your mouth — already spoken, familiar, known. In your heart — already internalized, already part of who you are. The commandment is the shape of the life you are already living. You can do this. (Paul will cite these very words in Romans 10 to describe how near the word of faith about Christ is — the trajectory from Torah to gospel runs through this sentence.)"
    },
    "15": {
      "L": "See, I have set before you today life and good, death and evil.",
      "M": "See, I set before you today life and prosperity, death and destruction.",
      "T": "Moses lays it out with stark clarity: two paths, two destinations. Life and good on one side. Death and evil on the other. Both are real. Both are available. Both are in front of you today."
    },
    "16": {
      "L": "If you obey the commandments of the LORD your God that I command you today, by loving the LORD your God, by walking in his ways, and by keeping his commandments and his statutes and his rules, then you shall live and multiply, and the LORD your God will bless you in the land that you are entering to take possession of it.",
      "M": "For I command you today to love the LORD your God, to walk in his ways, and to keep his commands, decrees, and laws; then you will live and increase, and the LORD your God will bless you in the land you are entering to possess.",
      "T": "Obedience, love, walking in his ways, keeping his commandments — these are the path to life: multiply in the land, be blessed by the LORD in the land he is giving you. The life promised is not primarily eternal life in a future realm — it is life now, in this land, under this LORD, full and flourishing."
    },
    "17": {
      "L": "But if your heart turns away, and you will not hear, but are drawn away to bow down to other gods and serve them,",
      "M": "But if your heart turns away and you refuse to listen, and if you are drawn away to bow down to other gods and worship them,",
      "T": "But if your heart turns aside — if you stop listening, if the pull of other gods draws you into worship of them —"
    },
    "18": {
      "L": "I declare to you today that you shall surely perish. You shall not live long in the land that you are crossing the Jordan to enter and possess.",
      "M": "I declare to you this day that you will certainly be destroyed. You will not live long in the land you are crossing the Jordan to enter and possess.",
      "T": "I tell you plainly: you will perish. The land you are about to enter will not hold you long. The choice is that binary. That consequential."
    },
    "19": {
      "L": "I call heaven and earth to witness against you today, that I have set before you life and death, blessing and curse. Therefore choose life, that you and your offspring may live,",
      "M": "This day I call the heavens and the earth as witnesses against you that I have set before you life and death, blessings and curses. Now choose life, so that you and your children may live",
      "T": "Heaven and earth are called as witnesses. The entire created order hears this moment. Life and death. Blessing and curse. Both laid out. Both available. Moses does not end with description — he ends with an imperative: choose life. That you may live. That your children may live."
    },
    "20": {
      "L": "loving the LORD your God, obeying his voice and holding fast to him, for he is your life and length of days, that you may dwell in the land that the LORD swore to your fathers, to Abraham, to Isaac, and to Jacob, to give them.",
      "M": "by loving the LORD your God, listening to his voice, and holding fast to him. For the LORD is your life, and he will give you many years in the land he swore to give to your ancestors Abraham, Isaac, and Jacob.",
      "T": "Choosing life means: loving the LORD your God. Obeying his voice. Holding fast to him — clinging, not drifting. Because he is your life. Not a condition of your life. Not the source of your blessings. He himself is your life — and therefore the length of your days in the land he swore to Abraham, to Isaac, to Jacob. This is the final word of Moses's great sermon: cling to the LORD, for he is life itself."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'deuteronomy')
        merge_tier(existing, DEUTERONOMY, tier_key)
        save(tier_dir, 'deuteronomy', existing)
    print('Deuteronomy 25–30 written.')

if __name__ == '__main__':
    main()
