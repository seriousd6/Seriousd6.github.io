"""
MKT Proverbs chapters 16–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-16-18.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" (all caps) in L/M; "the LORD" in T — consistent with chs. 1–12.

- H5315 (נֶפֶשׁ, nephesh): Context-driven throughout:
  * 16:17 = "life" (keeping his way preserves his life — holistic embodied self, not soul)
  * 16:26 = "appetite" (hunger drives the laborer — nephesh as craving/need)
  * 18:7 = "very life" (lips are a snare for his soul — existential jeopardy)

- H7307 (רוּחַ, ruach): Context-driven:
  * 16:2 = "spirits" (LORD weighs the spirits = interior character — not the divine Spirit)
  * 16:18 = "spirit" (haughty spirit precedes a fall — character disposition)
  * 16:19 = "spirit" (humble spirit — character quality)
  * 16:32 = "spirit" (ruling one's spirit = self-mastery)
  * 17:22 = "spirit" (broken spirit dries the bones — emotional/psychological state)
  * 17:27 = "spirit" (excellent/calm spirit — steady temperament)
  * 18:14 = "spirit" (the spirit sustains infirmity; wounded spirit — psychological resilience)

- H2617 (חֶסֶד, hesed): 16:6 — "faithful love" in M, "covenant love" in T (full theological
  weight here — iniquity being atoned for by mercy and truth is covenantal language, not just
  behavioral kindness). Differs from ch. 11 usage where behavioral "kindness" was preferred.

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L; "detestable" in M; T may expand where useful.
  * 16:5 = proud heart; 16:12 = kings committing wickedness; 17:15 = perverting justice.

- H191 (אֱוִיל, 'evil) vs. H3684 (כְּסִיל, kesil): Both rendered "fool" in L/M.
  T tier notes the distinction where context reveals it:
  * 191 = the morally corrupt fool who despises restraint (16:22)
  * 3684 = the self-satisfied, unteachable fool (17:10, 17:12, 17:16, 18:2, 18:6, 18:7)

- H7081 (קֶסֶם, qesem), 16:10: "divine sentence" — an oracle-like utterance. The ideal king's
  word in ancient Near Eastern theology had quasi-prophetic authority. Rendered "oracle" in M/T
  to preserve the weight without confusing it with a Hebrew prophetic oracle.

- H4633 (מַעַרְכֵי, ma'arkhe), 16:1: "preparations/arrangements of the heart" — intentional
  planning and ordering of thoughts. L: "preparations"; M: "plans"; T: expands the idea.

- Antithetical couplets: Chapters 16–18 mix antithetical, synonymous, and comparative couplets.
  16 is particularly dense with divine sovereignty proverbs (vv. 1, 2, 3, 4, 7, 9, 11, 33).
  L/M preserve the formal structure of each couplet. T expands meaning while keeping both poles.

- Gnomic aspect: Timeless present throughout. Hebrew imperfect/participle rendered as simple
  present or future — not past tense.

- 16:18 ("pride goes before destruction"): The most famous proverb in this section. H1347
  (ge'ah = pride) and H7307 (ruach = spirit) are carefully distinguished from the YHWH-speech
  of adjacent verses. T tier surfaces the internal logic.

- 16:25: Exact repetition of 14:12 in Hebrew. Both chapters include this identical proverb.
  Rendered identically to maintain coherence — the repetition is intentional emphasis.

- 17:8 (bribe as charm stone): Observational, not endorsement. The verse describes how the
  bribe-giver perceives his own tool. T tier makes this explicit.

- 17:15 (justifying the wicked / condemning the righteous): Both judicial perversions are paired
  as equally abominable. T tier holds both without softening either direction.

- 18:1 (the isolating person): H8454 (tushiyyah = sound wisdom/practical judgment) and H6504
  (parad = to separate). The verse critiques self-directed isolation that severs from community
  and corporate wisdom. T tier draws this out.

- 18:10–11: Intentional contrast — the LORD's name as actual strong tower (v10) vs. the rich
  man's wealth as an imagined high wall (v11). T tier makes the comparison explicit.

- 18:19 (offended brother): The Hebrew is difficult; the text contrasts a brother offended
  (harder than a fortified city to win) with disputes among brothers (like bars of a castle).
  The relational damage of broken brotherhood is the point.

- 18:24: H7489 (ra'a) here = "come to ruin/be broken" — many companions can lead to ruin.
  Contrast with the singular friend who sticks closer than a brother. Both halves matter for
  the meaning.
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


PROVERBS = {
  "16": {
    "1": {
      "L": "The preparations of the heart in man, and the answer of the tongue, is from the LORD.",
      "M": "The plans of the heart belong to man, but the right answer of the tongue comes from the LORD.",
      "T": "We can arrange our thoughts as carefully as we like — the heart's preparations are ours to make. But what actually comes out at the right moment, with the right weight? That comes from the LORD."
    },
    "2": {
      "L": "All the ways of a man are clean in his own eyes, but the LORD weigheth the spirits.",
      "M": "All a man's ways seem right to him, but the LORD weighs the spirits.",
      "T": "Everyone thinks their own conduct is pure — we are all blind to our own distortions. But the LORD does not consult our self-assessment. He weighs the spirit, the actual character beneath the behavior."
    },
    "3": {
      "L": "Commit thy works unto the LORD, and thy thoughts shall be established.",
      "M": "Commit your work to the LORD, and your plans will be established.",
      "T": "Roll your work entirely onto the LORD — hand it over — and what you are planning will find its footing. The act of surrender is what gives the plan stability."
    },
    "4": {
      "L": "The LORD hath made all things for himself, yea even the wicked for the day of evil.",
      "M": "The LORD has made everything for its purpose, even the wicked for the day of disaster.",
      "T": "Everything that exists has a purpose the LORD assigned to it — nothing is accidental. Even the wicked person exists within this design: there is a day of reckoning they are being prepared for, and the LORD holds that day too."
    },
    "5": {
      "L": "Every one that is proud in heart is an abomination to the LORD; though hand join in hand, he shall not be unpunished.",
      "M": "Everyone with a proud heart is detestable to the LORD; be assured — they will not go unpunished.",
      "T": "The proud heart — the one that inflates itself before God and others — is precisely what the LORD finds most repugnant. And no matter how many powerful allies the proud man assembles, he will not escape the reckoning."
    },
    "6": {
      "L": "By mercy and truth iniquity is purged, and by the fear of the LORD men depart from evil.",
      "M": "By faithful love and truth iniquity is atoned for, and by the fear of the LORD people turn from evil.",
      "T": "Covenant love and faithfulness — these are what cover what we have done wrong, what provide the atonement iniquity requires. And the fear of the LORD is what keeps us from going wrong in the first place."
    },
    "7": {
      "L": "When a man's ways please the LORD, he maketh even his enemies to be at peace with him.",
      "M": "When a person's ways please the LORD, he makes even their enemies live at peace with them.",
      "T": "When your life is oriented toward what pleases the LORD, even your enemies cannot sustain their hostility against you. The LORD himself makes peace happen — it is not your diplomacy that achieves it."
    },
    "8": {
      "L": "Better is a little with righteousness than great revenues without right.",
      "M": "Better is a little with righteousness than great income without justice.",
      "T": "A modest income earned honestly is worth more than wealth accumulated through injustice. The amount is not the point — the means is."
    },
    "9": {
      "L": "A man's heart deviseth his way, but the LORD directeth his steps.",
      "M": "A man's heart plans his way, but the LORD directs his steps.",
      "T": "We plan our route carefully in our minds — and then the LORD redirects our actual feet. Human planning is real, but it is always nested inside something larger and wiser."
    },
    "10": {
      "L": "A divine sentence is in the lips of the king; his mouth transgresseth not in judgment.",
      "M": "An oracle is on the lips of the king; in giving judgment his mouth does not err.",
      "T": "The wise king speaks with something beyond mere human authority — his words in judgment carry the weight of a divine sentence. This is the ideal: a ruler whose mouth is so formed by wisdom that it becomes an instrument of right judgment."
    },
    "11": {
      "L": "A just weight and balance are the LORD's; all the weights of the bag are his work.",
      "M": "Honest scales and balances belong to the LORD; all the weights in the bag are his concern.",
      "T": "The LORD is the original guarantor of honest commerce. Accurate weights are not just good business practice — they express his character. He made the standard; every honest weight in your bag reflects his work."
    },
    "12": {
      "L": "It is an abomination to kings to commit wickedness, for the throne is established by righteousness.",
      "M": "It is detestable for kings to commit wickedness, for a throne is made secure by righteousness.",
      "T": "The king who practices wickedness saws at the legs of his own throne. Power can only sustain itself when it is grounded in righteousness — that is what actually holds authority together."
    },
    "13": {
      "L": "Righteous lips are the delight of kings, and they love him that speaketh right.",
      "M": "Righteous lips are the delight of kings, and they love the one who speaks honestly.",
      "T": "The king who has any wisdom knows that honest counsel is his greatest asset. Righteous speech — not flattery — is what great leaders genuinely want from those around them."
    },
    "14": {
      "L": "The wrath of a king is as messengers of death, but a wise man will pacify it.",
      "M": "A king's wrath is like messengers of death, but a wise person will appease it.",
      "T": "When a king's anger turns against you, the danger is real — royal wrath in the ancient world meant death could arrive at any moment. The wise person knows how to calm that anger before it reaches its final conclusion."
    },
    "15": {
      "L": "In the light of the king's countenance is life, and his favour is as a cloud of the latter rain.",
      "M": "In the light of the king's face is life, and his favor is like a cloud of spring rain.",
      "T": "Royal approval brings life — in the ancient world, the king's favor meant protection, provision, and access. His goodwill is like a spring rain cloud arriving at exactly the right time: everything that needs it gets drenched."
    },
    "16": {
      "L": "How much better is it to get wisdom than gold, and to get understanding rather than silver!",
      "M": "How much better to gain wisdom than gold, and to choose understanding over silver!",
      "T": "Gold is valuable. Wisdom is worth more — by so much that the comparison barely holds. Silver can be counted and stored; understanding cannot be bought at any price."
    },
    "17": {
      "L": "The highway of the upright is to depart from evil; he that keepeth his way preserveth his life.",
      "M": "The road of the upright leads away from evil; whoever keeps to that road protects his life.",
      "T": "The path the upright take has a built-in direction: away from evil. This is not incidental — it is the whole definition of the road. Stay on it, and your life is protected."
    },
    "18": {
      "L": "Pride goeth before destruction, and an haughty spirit before a fall.",
      "M": "Pride goes before destruction, and a haughty spirit before a fall.",
      "T": "Pride announces its own end. You can see it coming: first the swelling of self, the contempt for others — then the collapse. The haughty spirit always precedes the fall, as reliably as dawn precedes the day."
    },
    "19": {
      "L": "Better it is to be of an humble spirit with the lowly than to divide the spoil with the proud.",
      "M": "It is better to be humble in spirit with the poor than to share plunder with the proud.",
      "T": "The company of the humble — even when they have little — is worth more than a seat at the table of the proud, even when the spoils are being divided. Whatever the proud are sharing, you do not want a share of what comes next."
    },
    "20": {
      "L": "He that handleth a matter wisely shall find good, and whoso trusteth in the LORD, happy is he.",
      "M": "Whoever handles a matter wisely will find good, and blessed is the one who trusts in the LORD.",
      "T": "Wisdom in the handling of any situation leads to good outcomes. And the person who trusts the LORD has already found the deepest source of that wisdom — the well from which all good handling flows."
    },
    "21": {
      "L": "The wise in heart shall be called prudent, and the sweetness of the lips increaseth learning.",
      "M": "The wise in heart is called discerning, and pleasant words increase the ability to learn.",
      "T": "A wise heart earns a reputation over time — people recognize it and name it. And there is real power in pleasant speech: it opens people, so they can actually receive what is being said."
    },
    "22": {
      "L": "Understanding is a wellspring of life unto him that hath it, but the instruction of fools is folly.",
      "M": "Understanding is a fountain of life to those who have it, but the instruction fools give is only folly.",
      "T": "Genuine understanding is a spring of life — it keeps producing. But whatever fools teach is only more folly. Their instruction is not information; it is the transmission of their own emptiness."
    },
    "23": {
      "L": "The heart of the wise teacheth his mouth, and addeth learning to his lips.",
      "M": "The heart of the wise teaches his mouth and adds persuasiveness to his words.",
      "T": "The wise person's interior life disciplines their speech. What is in the heart shapes what comes out of the mouth — and when the heart is wise, the words that follow carry weight and open understanding in whoever hears them."
    },
    "24": {
      "L": "Pleasant words are as an honeycomb, sweet to the soul and health to the bones.",
      "M": "Pleasant words are like a honeycomb — sweet to the soul and healing to the bones.",
      "T": "There are words that do to the soul what honey does to the tongue — sweet going in, and healing all the way through. Good words, spoken well, are genuinely therapeutic."
    },
    "25": {
      "L": "There is a way that seemeth right unto a man, but the end thereof are the ways of death.",
      "M": "There is a path that seems right to a person, but its end is the way of death.",
      "T": "The most dangerous roads are the ones that look fine from where you are standing. A path can feel right, seem reasonable, look straight — and lead straight to death. Self-assessment alone is not enough."
    },
    "26": {
      "L": "He that laboureth laboureth for himself, for his mouth craveth it of him.",
      "M": "A worker's appetite works for him; his hunger drives him on.",
      "T": "Hunger is an honest motivator. The laborer works because he has to eat — and that need is not a burden, it is what keeps him going. The body's demands serve the person's genuine good."
    },
    "27": {
      "L": "An ungodly man diggeth up evil, and in his lips there is as a burning fire.",
      "M": "A worthless man digs up evil, and his words burn like fire.",
      "T": "The scoundrel goes looking for evil — excavating it from the past, digging it up from wherever it can be found. And when he finds it, his lips carry it like burning coals: his words scorch whoever they touch."
    },
    "28": {
      "L": "A froward man soweth strife, and a whisperer separateth chief friends.",
      "M": "A perverse man stirs up conflict, and a gossip drives close friends apart.",
      "T": "The twisted person's specialty is conflict — they plant it everywhere they go. And the gossip does something quieter but just as destructive: they work their way between people who are close and separate them."
    },
    "29": {
      "L": "A violent man enticeth his neighbour and leadeth him into the way that is not good.",
      "M": "A violent man entices his neighbor and leads him down a path that is not good.",
      "T": "The violent person does not work alone — they recruit. They draw their neighbor in, make it seem appealing, and then lead them down a road that is genuinely harmful. The seduction is part of the violence."
    },
    "30": {
      "L": "He shutteth his eyes to devise froward things; moving his lips he bringeth evil to pass.",
      "M": "He who closes his eyes schemes perversity; he who purses his lips brings evil to pass.",
      "T": "Watch the body language of the schemer: closed eyes to focus on the plan, working lips as he calculates. Both are tells — a body in the act of plotting harm. The evil is not accidental; it is engineered."
    },
    "31": {
      "L": "The hoary head is a crown of glory; it is found in the way of righteousness.",
      "M": "Gray hair is a crown of glory; it is found on the path of righteousness.",
      "T": "Old age is an honor — the gray head is a crown, not a liability. But the glory belongs to old age arrived at through righteousness. The long life of the wicked is not this. Only the life well-lived earns the crown."
    },
    "32": {
      "L": "He that is slow to anger is better than the mighty, and he that ruleth his spirit than he that taketh a city.",
      "M": "Whoever is slow to anger is better than the mighty, and whoever rules his spirit is better than one who captures a city.",
      "T": "The person who can govern their own anger has achieved something more impressive than military conquest. Taking a city requires brute force. Mastering your own spirit requires a discipline most warriors never find."
    },
    "33": {
      "L": "The lot is cast into the lap, but the whole disposing thereof is of the LORD.",
      "M": "The lot is cast into the lap, but its every decision comes from the LORD.",
      "T": "Chance — or what looks like chance — is still under divine governance. The lot falls where it falls. But the outcome? That is the LORD's. Nothing that appears random is outside his reach."
    }
  },
  "17": {
    "1": {
      "L": "Better is a dry morsel with quietness therewith than an house full of sacrifices with strife.",
      "M": "Better a dry morsel in peace than a house full of feasting with strife.",
      "T": "A dry crust eaten in a quiet house is worth more than a lavish feast where people are fighting. The food matters far less than what surrounds it."
    },
    "2": {
      "L": "A wise servant shall have rule over a son that causeth shame, and shall have part of the inheritance among the brethren.",
      "M": "A wise servant will rule over a son who causes shame and will share in the inheritance among brothers.",
      "T": "The meritocracy of wisdom overturns birth privilege. A servant who is genuinely wise will end up with more authority — and more inheritance — than a son who lives in shame. Character outranks family position."
    },
    "3": {
      "L": "The fining pot is for silver and the furnace for gold, but the LORD trieth the hearts.",
      "M": "The crucible is for silver and the furnace for gold, and the LORD tests hearts.",
      "T": "Heat is how you find out what is real in metal. The LORD uses the same principle on people — he tests hearts not to destroy them, but to find out what they are genuinely made of."
    },
    "4": {
      "L": "A wicked doer giveth heed to false lips, and a liar giveth ear to a naughty tongue.",
      "M": "An evil person listens to wicked lips, and a liar pays attention to a destructive tongue.",
      "T": "Like seeks like. The person who does evil is drawn to the speech of other evildoers — those mischievous lips speak a language they recognize. Liars listen to the destructive tongue because it sounds familiar."
    },
    "5": {
      "L": "Whoso mocketh the poor reproacheth his Maker, and he that is glad at calamities shall not be unpunished.",
      "M": "Whoever mocks the poor insults his Maker, and whoever gloats over disaster will not go unpunished.",
      "T": "To despise a poor person is to insult the God who made them — you cannot separate the creature from the Creator. And to take pleasure in another's catastrophe is a darkness that will find its own reckoning."
    },
    "6": {
      "L": "Children's children are the crown of old men, and the glory of children are their fathers.",
      "M": "Grandchildren are the crown of the elderly, and children find their glory in their fathers.",
      "T": "Old age is crowned by the sight of grandchildren. And children, in turn, look to their fathers as their own kind of glory — the visible source of who they are. Family is one of the primary structures of human flourishing."
    },
    "7": {
      "L": "Excellent speech becometh not a fool; much less do lying lips a prince.",
      "M": "Fine speech does not suit a fool; much less do lying lips suit a ruler.",
      "T": "There is a mismatch between elevated speech and the fool who delivers it — it simply does not fit. But the mismatch runs the other way too: a ruler speaking lies is an even greater absurdity. Authority and dishonesty cannot long coexist."
    },
    "8": {
      "L": "A gift is as a precious stone in the eyes of him that hath it; whithersoever it turneth, it prospereth.",
      "M": "A bribe is like a charm stone in the eyes of the one who uses it; wherever he turns, he seems to succeed.",
      "T": "The bribe-giver sees his money as a kind of magic — he believes that greasing palms opens every door. And in the short term, he is often right. This is observation, not endorsement: the world as it actually works, not the world as it should."
    },
    "9": {
      "L": "He that covereth a transgression seeketh love, but he that repeateth a matter separateth very friends.",
      "M": "Whoever covers an offense seeks love, but whoever keeps bringing it up drives close friends apart.",
      "T": "Love chooses to cover what was done wrong — to bury it rather than display it. The opposite choice — constantly repeating a grievance, bringing it up again and again — drives apart even the closest friendship."
    },
    "10": {
      "L": "A reproof entereth more into a wise man than an hundred stripes into a fool.",
      "M": "A rebuke penetrates more deeply into a wise person than a hundred blows into a fool.",
      "T": "A single word of correction lands harder on a wise person than a hundred lashes on a fool. The wise person is open; the fool is closed. You can beat a fool all day and nothing gets through."
    },
    "11": {
      "L": "An evil man seeketh only rebellion; therefore a cruel messenger shall be sent against him.",
      "M": "An evil man seeks only rebellion, and a merciless messenger will be sent against him.",
      "T": "The evil person has one agenda: to rebel against order, authority, and the LORD's way. And what they call down on themselves matches: a relentless agent of judgment sent to meet them."
    },
    "12": {
      "L": "Let a bear robbed of her whelps meet a man, rather than a fool in his folly.",
      "M": "Better to encounter a bear robbed of her cubs than a fool caught up in his foolishness.",
      "T": "An enraged bear is at least predictable danger. A fool in full flight of his folly is something worse — you cannot reason with him, you cannot escape what he has already set in motion, and there is no telling what he will do next."
    },
    "13": {
      "L": "Whoso rewardeth evil for good, evil shall not depart from his house.",
      "M": "Whoever returns evil for good — evil will not leave his house.",
      "T": "The person who repays kindness with harm brings a curse into their own household. You cannot treat good as something to exploit without the consequences settling permanently in your home."
    },
    "14": {
      "L": "The beginning of strife is as when one letteth out water; therefore leave off contention before it be meddled with.",
      "M": "The start of conflict is like a crack letting out water; so abandon the dispute before it breaks open.",
      "T": "Once strife begins, it is like water springing from a crack — small at first, then impossible to stop. The wise move is to walk away from the dispute before it reaches that point. After the crack opens, it is too late."
    },
    "15": {
      "L": "He that justifieth the wicked, and he that condemneth the just, even they both are abomination to the LORD.",
      "M": "Both the one who acquits the wicked and the one who condemns the righteous are detestable to the LORD.",
      "T": "Two perversions of justice — declaring the guilty innocent and condemning the innocent guilty — both are equally abominable in the LORD's sight. Corrupt verdicts, regardless of their direction, are offensive to him. The scales of justice are his concern."
    },
    "16": {
      "L": "Wherefore is there a price in the hand of a fool to get wisdom, seeing he hath no heart to it?",
      "M": "Why should a fool have money to buy wisdom when he has no desire for it?",
      "T": "What is the point of a fool having the means to acquire wisdom, when the one thing that would make wisdom possible — the will to receive it — is entirely absent? Money cannot buy what the mind refuses to accept."
    },
    "17": {
      "L": "A friend loveth at all times, and a brother is born for adversity.",
      "M": "A friend loves at all times, and a brother is born for times of adversity.",
      "T": "True friendship does not ebb and flow with circumstances — it holds. And a brother is specifically made for the hard times: born for the day when everything goes wrong and you need someone who will not run."
    },
    "18": {
      "L": "A man void of understanding striketh hands, and becometh surety in the presence of his friend.",
      "M": "A person who lacks good sense gives a pledge of surety in the presence of his neighbor.",
      "T": "The person without judgment seals deals they should not seal — standing as guarantor for debts that are not theirs, in front of witnesses. The handshake that commits you to someone else's failure is a sign that wisdom has not yet arrived."
    },
    "19": {
      "L": "He loveth transgression that loveth strife; and he that exalteth his gate seeketh destruction.",
      "M": "Whoever loves quarreling loves transgression, and whoever raises his gate courts destruction.",
      "T": "The love of conflict and the love of sin are the same thing — you cannot have one without the other. And the person who inflates their own importance, building themselves too high, is asking for the fall that must follow."
    },
    "20": {
      "L": "He that hath a froward heart findeth no good, and he that hath a perverse tongue falleth into mischief.",
      "M": "Whoever has a crooked heart finds no good, and whoever has a perverse tongue falls into trouble.",
      "T": "A bent interior cannot produce a straight outcome — the crooked heart cannot find what is genuinely good. And the tongue trained on distortion eventually says the wrong thing at the wrong moment and falls into its own trap."
    },
    "21": {
      "L": "He that begetteth a fool doeth it to his sorrow, and the father of a fool hath no joy.",
      "M": "Whoever fathers a fool does so to his grief, and the father of a fool has no joy.",
      "T": "There is a particular sorrow attached to watching a child choose foolishness. The father of a fool has no delight in that child — grief is what replaces it. This is honest acknowledgment of what folly costs families."
    },
    "22": {
      "L": "A merry heart doeth good like a medicine, but a broken spirit drieth the bones.",
      "M": "A joyful heart is good medicine, but a broken spirit dries up the bones.",
      "T": "The body follows the spirit more than we know. A heart full of genuine joy is therapeutic — it heals from the inside. A spirit that is crushed does the opposite: it takes the moisture out of life, drying the person from within."
    },
    "23": {
      "L": "A wicked man taketh a gift out of the bosom to pervert the ways of judgment.",
      "M": "A wicked man accepts a bribe in secret to pervert the course of justice.",
      "T": "The bribe moves from hand to pocket in the shadows — slipped away before anyone sees. And what it purchases is the corruption of justice: verdicts shaped by money instead of truth. This is wickedness in one of its most structural forms."
    },
    "24": {
      "L": "Wisdom is before the face of him that hath understanding, but the eyes of a fool are in the ends of the earth.",
      "M": "Wisdom is right in front of the one who has understanding, but the eyes of a fool wander to the ends of the earth.",
      "T": "The person of understanding does not have to look far for wisdom — it is right in front of them. The fool's eyes are everywhere else: the horizon, the next thing, the far distance. Wisdom is always nearby; only fools have to search the whole earth for it."
    },
    "25": {
      "L": "A foolish son is a grief to his father, and bitterness to her that bare him.",
      "M": "A foolish son is grief to his father and bitterness to the mother who bore him.",
      "T": "Foolishness costs. The foolish child costs the father ongoing grief, and costs the mother something even deeper — the bitterness of watching what you gave life to choose destruction."
    },
    "26": {
      "L": "Also to punish the just is not good, nor to strike princes for equity.",
      "M": "It is not good to fine an innocent person, or to strike the noble simply for acting rightly.",
      "T": "Punishing the righteous is a perversion of justice — hitting the person whose only offense was doing right. To strike the upright for their integrity is to turn the whole system of order upside down."
    },
    "27": {
      "L": "He that hath knowledge spareth his words, and a man of understanding is of an excellent spirit.",
      "M": "Whoever has knowledge restrains his words, and a person of understanding has a calm spirit.",
      "T": "The knowledgeable person does not feel the need to fill every silence — they choose their words carefully, knowing that fewer words carry more weight. The person of real understanding is steady in spirit: not volatile, not easily rattled."
    },
    "28": {
      "L": "Even a fool, when he holdeth his peace, is counted wise, and he that shutteth his lips is esteemed a man of understanding.",
      "M": "Even a fool who stays silent is considered wise, and the one who keeps his lips shut is thought to be discerning.",
      "T": "Silence is the fool's best disguise. Stay quiet, and even those who are not wise may pass as discerning — no one can see the emptiness while the lips are closed. This is not advice to deceive but a warning about how much speech reveals."
    }
  },
  "18": {
    "1": {
      "L": "Through desire a man having separated himself seeketh and intermeddleth with all wisdom.",
      "M": "Whoever isolates himself pursues his own desires and disregards all sound wisdom.",
      "T": "The person who separates from community to pursue their own agenda is really just following their appetites — and in doing so, they break themselves off from the very wisdom that others might have offered them. Self-isolation in pursuit of private will is the opposite of growth."
    },
    "2": {
      "L": "A fool hath no delight in understanding, but that his heart may discover itself.",
      "M": "A fool takes no pleasure in understanding, but only in self-expression.",
      "T": "The fool's goal in conversation is not to learn — it is to talk. They have no interest in understanding anything; what they want is to hear themselves and have their own thoughts received. Understanding is the last thing they came for."
    },
    "3": {
      "L": "When the wicked cometh, then cometh also contempt, and with ignominy reproach.",
      "M": "When wickedness comes, contempt comes with it, and along with disgrace comes reproach.",
      "T": "Wickedness does not travel alone — contempt is always in the baggage. The person who carries disgrace into a room brings reproach right behind them. Character and its consequences are always paired."
    },
    "4": {
      "L": "The words of a man's mouth are as deep waters, and the wellspring of wisdom as a flowing brook.",
      "M": "The words of a person's mouth are deep waters, and the fountain of wisdom is a flowing stream.",
      "T": "There is depth in human speech that is hard to fathom — words go down into hidden places. The wisdom that flows from the truly wise is something different: not a still deep pool but a moving stream, always available, always renewing."
    },
    "5": {
      "L": "It is not good to accept the person of the wicked, to overthrow the righteous in judgment.",
      "M": "It is not good to show partiality to the wicked by denying justice to the righteous.",
      "T": "Letting the wicked off because of who they are — while using judgment as a weapon against the innocent — poisons everything it touches. The scales of justice have to weigh the act, not the person's status."
    },
    "6": {
      "L": "A fool's lips enter into contention, and his mouth calleth for strokes.",
      "M": "A fool's lips walk him into arguments, and his mouth calls out for a beating.",
      "T": "The fool's mouth writes checks that his body has to cash. He talks himself into one fight after another — and the conclusion of his speech is always the same: someone eventually hits him."
    },
    "7": {
      "L": "A fool's mouth is his destruction, and his lips are the snare of his soul.",
      "M": "A fool's mouth is his ruin, and his lips are a trap for his very life.",
      "T": "The fool is self-trapped. The mouth that destroys him, the lips that snare him — they are his own. He did not need enemies; his own speech was sufficient to bring him down."
    },
    "8": {
      "L": "The words of a talebearer are as wounds, and they go down into the innermost parts of the belly.",
      "M": "The words of a gossip are like choice morsels; they sink down into the inner depths.",
      "T": "Gossip goes down easy — that is the danger. What the gossip says is received like something tasty, and it does not stay on the surface. It sinks into the innermost places, where it does its real damage long after the conversation ends."
    },
    "9": {
      "L": "He also that is slothful in his work is brother to him that is a great waster.",
      "M": "Whoever is lazy in his work is kin to the one who destroys.",
      "T": "Laziness and destruction are family. The person who will not work is not merely failing to build — they are, in effect, tearing things down. Negligence and active sabotage produce similar results."
    },
    "10": {
      "L": "The name of the LORD is a strong tower; the righteous runneth into it and is safe.",
      "M": "The name of the LORD is a strong tower; the righteous run to it and are protected.",
      "T": "In the ancient world, the fortified tower was where you ran when everything outside became dangerous. The LORD's name — his revealed character, his presence — is that tower. The righteous person knows where to go when threat arrives."
    },
    "11": {
      "L": "The rich man's wealth is his strong city, and as an high wall in his own conceit.",
      "M": "A rich man's wealth is his strong city, and like a high wall in his imagination.",
      "T": "The rich man builds a psychological fortress out of his money — in his mind, the wealth is a high wall that nothing can breach. It is an imagination. Compare this with verse 10: the LORD's name is an actual tower; wealth is only a mental image of one."
    },
    "12": {
      "L": "Before destruction the heart of man is haughty, and before honour is humility.",
      "M": "Before destruction a person's heart is proud, but humility comes before honor.",
      "T": "The sequence is consistent: pride predicts destruction, humility predicts honor. You can trace the trajectory from the posture of the heart — the direction you are headed announces itself."
    },
    "13": {
      "L": "He that answereth a matter before he heareth it, it is folly and shame unto him.",
      "M": "To answer before listening is folly and disgrace.",
      "T": "The person who answers before the other person is finished speaking has already revealed something about themselves. It is not just impolite — it is foolish, and it ends in shame. You cannot respond well to what you have not yet heard."
    },
    "14": {
      "L": "The spirit of a man will sustain his infirmity, but a wounded spirit who can bear?",
      "M": "A man's spirit can endure sickness, but a crushed spirit — who can bear it?",
      "T": "Physical illness, even severe illness, can be survived when the spirit inside is strong. But crush the spirit — break the will, the hope, the sense of meaning — and there is nothing left to endure with. A wounded spirit is the one injury that cannot simply be carried."
    },
    "15": {
      "L": "The heart of the prudent getteth knowledge, and the ear of the wise seeketh knowledge.",
      "M": "The discerning heart acquires knowledge, and the ear of the wise seeks more of it.",
      "T": "The prudent person is always in acquisition mode — gathering knowledge wherever they go. The wise person's ear is not passive; it is actively looking for knowledge in what it hears. Both the heart and the ear are engaged."
    },
    "16": {
      "L": "A man's gift maketh room for him, and bringeth him before great men.",
      "M": "A person's gift opens doors and brings him before important people.",
      "T": "A well-placed gift creates access — it makes room in circles that would otherwise be closed. This is observation of how the world operates, not necessarily approval of it."
    },
    "17": {
      "L": "He that is first in his own cause seemeth just, but his neighbour cometh and searcheth him.",
      "M": "The first to state his case seems right, until another comes and examines him.",
      "T": "Everyone sounds convincing when they are the only voice in the room. The first account frames everything. But then the other side arrives and begins to probe — and the picture changes. This is why judgment should always wait for cross-examination."
    },
    "18": {
      "L": "The lot causeth contentions to cease, and parteth between the mighty.",
      "M": "The lot settles disputes and parts the mighty from each other.",
      "T": "When two powerful people cannot reach agreement, the lot cuts the knot. It removes the ego from the equation and settles what argument could not. This is not fatalism — it is practical wisdom about when to stop fighting for position."
    },
    "19": {
      "L": "A brother offended is harder to be won than a strong city, and their contentions are like the bars of a castle.",
      "M": "A brother who has been offended is harder to win back than a fortified city, and disputes between brothers are like the bars of a citadel.",
      "T": "The hardest kind of reconciliation involves a brother who was wronged. Close relationship plus deep wound creates a barrier harder to breach than fortress walls. The quarrels of brothers are heavier than other quarrels — the shared history makes every grievance load-bearing."
    },
    "20": {
      "L": "A man's belly shall be satisfied with the fruit of his mouth, and with the increase of his lips shall he be filled.",
      "M": "A person is satisfied by the fruit of his words, and by the produce of his lips he is filled.",
      "T": "What you say produces real outcomes — you eat what your words have grown. This works both ways: the person who speaks well reaps the harvest of that speech; the person whose words are corrupt also reaps exactly what they have said."
    },
    "21": {
      "L": "Death and life are in the power of the tongue, and they that love it shall eat the fruit thereof.",
      "M": "Death and life are in the power of the tongue, and those who love it will eat its fruit.",
      "T": "The tongue is lethal or life-giving — that is not poetry, it is physics. Words have killed people and brought people to life. Whatever you do with your tongue, be clear: you will eat what it produces."
    },
    "22": {
      "L": "Whoso findeth a wife findeth a good thing, and obtaineth favour of the LORD.",
      "M": "Whoever finds a wife finds a good thing and receives favor from the LORD.",
      "T": "Marriage is not merely a human arrangement — finding a good wife is a gift with the LORD's fingerprints on it. He is the one from whom favor comes, and a good marriage is one form that favor takes."
    },
    "23": {
      "L": "The poor useth intreaties, but the rich answereth roughly.",
      "M": "The poor person speaks with pleas, but the rich person answers harshly.",
      "T": "The economic gap shows up in speech. The poor person has to beg — their position requires pleading. The rich person has no need to be careful with words — they can be as rough as they like, and their wealth will absorb the consequences. This is description, not approval."
    },
    "24": {
      "L": "A man that hath friends must shew himself friendly, and there is a friend that sticketh closer than a brother.",
      "M": "There are companions who lead to ruin, but there is a friend who sticks closer than a brother.",
      "T": "Not all friendship is equal. Many companions can actually be destructive — too many connections, none deep enough. But somewhere there is the friend who holds on when everything falls apart — tighter than a brother, closer than blood. That person is rare and worth everything."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 16–18 written.')

if __name__ == '__main__':
    main()
