"""
MKT Proverbs chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-10-12.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" (all caps) in L/M; "the LORD" in T — consistent with chs. 1–3.

- H2451 (חָכְמָה, chokmah): "wisdom" in all tiers — consistent with chs. 1–3.

- H5315 (נֶפֶשׁ, nephesh): Context-driven across these chapters:
  * 10:3 = "appetite" (hunger context — the LORD will not let the righteous go hungry)
  * 11:17 = "self" (the kind man does good to himself)
  * 11:25 = "generous soul" (preserving the idiom "a blessed soul")
  * 11:30 = "people" (he who wins souls = draws people to wisdom)
  * 12:10 = "life/wellbeing" (the righteous cares for his animal's life)

- H7307 (רוּחַ, ruach):
  * 11:13 = "spirit" (faithful spirit = character quality, not divine Spirit)
  * 11:29 = "wind" (inherit the wind = inherit nothing — literal Hebrew idiom)

- H2617 (חֶסֶד, hesed): In 11:17, used adjectivally as "merciful/kind man." Rendered
  "kind" in all tiers — the behavioral expression of covenant loyalty, not the full
  theological weight of chesed (no covenantal partner-relationship implied). Documented
  as context deviation.

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L; "detestable" in M; "abomination" or
  expanded in T, depending on what the verse requires.

- Antithetical couplet structure: Chapters 10–12 are almost entirely antithetical couplets
  (A, but B). L/M preserve this structure faithfully. T may expand the contrast but
  always maintains both poles.

- Gnomic aspect: These proverbs use Hebrew imperfect/participle for timeless statements.
  Rendered as simple present or future in English — not past tense.

- H2742 (חָרוּץ, charuts): "diligent/diligence" across all uses (10:4, 12:24, 12:27).
  The word means sharp, decisive effort — not just busyness.

- H191 (אֱוִיל, 'evil) vs. H3684 (כְּסִיל, kesil): Two distinct Hebrew words for "fool."
  'Evil (191) = the morally corrupt fool who despises wisdom. Kesil (3684) = the
  stubborn, self-satisfied, complacent fool. Both rendered "fool" in L/M for readability,
  but T tier may distinguish where context permits.

- 10:12 ("love covers all sins"): Quoted in 1 Pet 4:8 and alluded to in Jas 5:20.
  T tier notes the NT weight without being anachronistic.

- 11:22 (gold ring in pig's snout): Comparative proverb about beauty without discretion.
  T tier draws out the absurdity of the image — not merely decorative observation.

- 11:31 ("If the righteous is repaid on earth..."): Quoted in 1 Pet 4:18 (LXX version).
  T tier holds the sobering logic without softening it.

- 12:1 ("he who hates reproof is brutish"): H1198 ba'ar = like an animal, brutish.
  L: "brutish"; M: "a fool" (softened for readability); T: draws out the animalistic
  stubbornness implied.

- 12:28 ("in its pathway there is no death"): A striking affirmation — the righteous
  path leads to life without end. T tier holds the hope without flattening it.
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
  "10": {
    "1": {
      "L": "The proverbs of Solomon: a wise son maketh glad a father, but a foolish son is the heaviness of his mother.",
      "M": "The proverbs of Solomon: a wise son brings joy to his father, but a foolish son brings grief to his mother.",
      "T": "The child who grows into wisdom is a father's delight. The one who chooses folly becomes his mother's sorrow."
    },
    "2": {
      "L": "Treasures of wickedness profit nothing, but righteousness delivereth from death.",
      "M": "Ill-gotten wealth profits nothing, but righteousness delivers from death.",
      "T": "Wealth gained through wickedness cannot save you when it matters most. Only righteousness delivers from death."
    },
    "3": {
      "L": "The LORD will not suffer the appetite of the righteous to famish, but he thrusteth away the craving of the wicked.",
      "M": "The LORD does not let the righteous go hungry, but he thwarts the craving of the wicked.",
      "T": "The LORD will not leave the righteous to starve — but whatever the wicked hunger for, he drives it away."
    },
    "4": {
      "L": "He becometh poor that worketh with a slack hand, but the hand of the diligent maketh rich.",
      "M": "A slack hand leads to poverty, but the hand of the diligent brings wealth.",
      "T": "Work carelessly and you will end up with nothing. Work with diligence and you will end up with more than enough."
    },
    "5": {
      "L": "A son who gathereth in summer is prudent, but a son who sleepeth in harvest causeth shame.",
      "M": "A wise son gathers crops in summer, but a son who sleeps through the harvest brings shame.",
      "T": "The wise child works while the season allows. The one who sleeps through harvest is a disgrace to his family."
    },
    "6": {
      "L": "Blessings are upon the head of the righteous, but violence covereth the mouth of the wicked.",
      "M": "Blessings crown the head of the righteous, but the mouth of the wicked conceals violence.",
      "T": "The righteous walk under a canopy of blessing. The wicked carry violence in their mouths — hidden until it erupts."
    },
    "7": {
      "L": "The memory of the righteous is blessed, but the name of the wicked shall rot.",
      "M": "The memory of the righteous is a blessing, but the name of the wicked rots.",
      "T": "When a righteous person is remembered, it is with gratitude and honor. When the wicked are remembered at all — their name decays."
    },
    "8": {
      "L": "The wise in heart will receive commandments, but a prating fool shall fall.",
      "M": "The wise in heart accepts instruction, but the babbling fool will come to ruin.",
      "T": "The person with genuine wisdom listens to instruction and takes it in. The fool talks his way to his own downfall."
    },
    "9": {
      "L": "He that walketh in integrity walketh securely, but he that perverteth his ways shall be found out.",
      "M": "Whoever walks with integrity walks in security, but whoever twists his ways will be exposed.",
      "T": "The person of integrity has nothing to hide and nothing to fear. The one who cheats and corners ends up exposed."
    },
    "10": {
      "L": "He that winketh the eye causeth grief, but the prating fool shall fall.",
      "M": "The one who winks with malice stirs up trouble, but the babbling fool will come to ruin.",
      "T": "A conspiratorial wink — a gesture of hidden mischief — creates grief. The fool who cannot stop talking will eventually say something that brings him down."
    },
    "11": {
      "L": "The mouth of the righteous is a well of life, but violence covereth the mouth of the wicked.",
      "M": "The mouth of the righteous is a fountain of life, but the mouth of the wicked conceals violence.",
      "T": "What flows from the righteous person's mouth gives life to those around them. What is hidden in the wicked person's mouth is violence."
    },
    "12": {
      "L": "Hatred stirreth up strifes, but love covereth all transgressions.",
      "M": "Hatred stirs up conflict, but love covers all offenses.",
      "T": "Hatred finds every fault and inflames every wound. Love chooses not to keep score — it covers sins rather than broadcasting them."
    },
    "13": {
      "L": "Wisdom is found on the lips of him that hath understanding, but a rod is for the back of him that is void of understanding.",
      "M": "On the lips of the discerning, wisdom is found; but a rod belongs on the back of the one who lacks good sense.",
      "T": "Open the mouth of someone with genuine discernment and wisdom falls out. Open the mouth of a fool and all you can do is reach for the rod."
    },
    "14": {
      "L": "Wise men store up knowledge, but the mouth of the fool is near destruction.",
      "M": "Wise people store up knowledge, but the mouth of a fool brings destruction near.",
      "T": "The wise accumulate knowledge the way a trader accumulates goods — carefully, over time. The fool opens his mouth and catastrophe comes rushing to meet him."
    },
    "15": {
      "L": "The rich man's wealth is his strong city; the destruction of the poor is their poverty.",
      "M": "A wealthy person's riches are like a fortified city to him; poverty is the ruin of the poor.",
      "T": "The wealthy man has a wall around him — his money buys options, security, influence. The poor person's poverty is precisely what destroys him: no margin, no buffer, no escape. This is observation, not approval."
    },
    "16": {
      "L": "The labour of the righteous tendeth to life; the fruit of the wicked to sin.",
      "M": "The earnings of the righteous lead to life, but the income of the wicked leads to sin.",
      "T": "Every effort the righteous person makes produces life. Every gain the wicked person accumulates is already corruption."
    },
    "17": {
      "L": "He that keepeth instruction is in the way of life, but he that forsaketh reproof erreth.",
      "M": "Whoever keeps instruction is on the path of life, but whoever abandons correction goes astray.",
      "T": "The one who takes correction to heart is on a life-giving road. The one who refuses correction does not just wander — they lead others astray with them."
    },
    "18": {
      "L": "He that concealeth hatred hath lying lips, and he that uttereth slander is a fool.",
      "M": "Whoever conceals hatred has lying lips, and whoever spreads slander is a fool.",
      "T": "Two kinds of liar: the one who smiles to your face while hating you, and the one who says openly what he should not say at all. Both are fools."
    },
    "19": {
      "L": "In the multitude of words transgression is not lacking, but he that refraineth his lips is wise.",
      "M": "When words are many, sin is not far off, but whoever holds back his words is prudent.",
      "T": "The more you talk, the more chances you give yourself to sin. Knowing when to stop talking is one of wisdom's most underrated skills."
    },
    "20": {
      "L": "The tongue of the righteous is choice silver; the heart of the wicked is of little worth.",
      "M": "The tongue of the righteous is like choice silver; the heart of the wicked has little value.",
      "T": "What the righteous person says is worth its weight in silver — refined, valuable, real. What the wicked person thinks? Worth nothing."
    },
    "21": {
      "L": "The lips of the righteous feed many, but fools die for lack of sense.",
      "M": "The lips of the righteous feed many, but fools die because they lack good judgment.",
      "T": "The righteous person's words are nourishment — many people thrive because of what they say. Fools destroy themselves through their own empty-headedness."
    },
    "22": {
      "L": "The blessing of the LORD maketh rich, and he addeth no sorrow with it.",
      "M": "The blessing of the LORD is what truly makes rich, and he adds no sorrow to it.",
      "T": "When the LORD blesses you with wealth, there is no hidden cost — no grief attached, no price paid in pain. That is what separates his blessing from what you can grab on your own."
    },
    "23": {
      "L": "To do mischief is as sport to a fool, but a man of understanding hath wisdom.",
      "M": "Doing wrong is like a game to a fool, but wisdom is the delight of a person of understanding.",
      "T": "The fool finds wickedness entertaining — mischief is his hobby. The person who genuinely understands takes wisdom as his pleasure instead."
    },
    "24": {
      "L": "The fear of the wicked shall come upon him, but the desire of the righteous shall be granted.",
      "M": "What the wicked fears will come upon him, but the longing of the righteous will be fulfilled.",
      "T": "The wicked person's deepest terror becomes his reality. The righteous person's deepest desire — the LORD gives it."
    },
    "25": {
      "L": "As the whirlwind passeth, so the wicked is no more, but the righteous is an everlasting foundation.",
      "M": "When the storm passes, the wicked are gone, but the righteous stand on an everlasting foundation.",
      "T": "The wicked are swept away like leaves in a whirlwind — present one moment, gone the next. The righteous are built on something that does not move."
    },
    "26": {
      "L": "As vinegar to the teeth and as smoke to the eyes, so is the sluggard to them that send him.",
      "M": "As vinegar is to the teeth and smoke to the eyes, so is a lazy person to those who employ him.",
      "T": "Sending a lazy person to do your work is like biting into something sour — irritating, disappointing, nothing you can fix. It sets your teeth on edge every time."
    },
    "27": {
      "L": "The fear of the LORD prolongeth days, but the years of the wicked shall be shortened.",
      "M": "The fear of the LORD adds length to life, but the years of the wicked are cut short.",
      "T": "Walking in the fear of the LORD lengthens a life. The wicked person's years, by contrast, are already numbered down — cut short before their time."
    },
    "28": {
      "L": "The hope of the righteous shall be gladness, but the expectation of the wicked shall perish.",
      "M": "The hope of the righteous brings joy, but the expectation of the wicked comes to nothing.",
      "T": "The righteous person has genuine hope — and it delivers. The wicked person's hopes vanish when they need them most."
    },
    "29": {
      "L": "The way of the LORD is strength to the upright, but destruction to the workers of iniquity.",
      "M": "The LORD's way is a stronghold for the blameless, but it means ruin for those who do evil.",
      "T": "The same road — the LORD's way — functions differently depending on who walks it. For the upright it is a fortress. For evildoers it is the thing that destroys them."
    },
    "30": {
      "L": "The righteous shall never be removed, but the wicked shall not inhabit the earth.",
      "M": "The righteous will never be dislodged, but the wicked will not remain in the land.",
      "T": "The righteous are immovable — there is no force that will uproot them. The wicked will not last in the land God gives."
    },
    "31": {
      "L": "The mouth of the righteous bringeth forth wisdom, but the perverse tongue shall be cut off.",
      "M": "The mouth of the righteous produces wisdom, but the perverse tongue will be cut off.",
      "T": "From the righteous person's mouth comes wisdom — a natural overflow. The tongue that twists truth will eventually be silenced permanently."
    },
    "32": {
      "L": "The lips of the righteous know what is acceptable, but the mouth of the wicked speaketh perverseness.",
      "M": "The lips of the righteous know what is pleasing, but the mouth of the wicked speaks only what is perverse.",
      "T": "The righteous person has an instinct for what is fitting — they know what to say and when. The wicked person's mouth is trained on perversity."
    }
  },
  "11": {
    "1": {
      "L": "A false balance is an abomination to the LORD, but a just weight is his delight.",
      "M": "Dishonest scales are detestable to the LORD, but an accurate weight is his delight.",
      "T": "The LORD takes commerce seriously. Rigged scales — fraud dressed as trade — he calls an abomination. Honest weights, by contrast, are something he takes genuine pleasure in."
    },
    "2": {
      "L": "When pride cometh, then cometh shame, but with the humble is wisdom.",
      "M": "When pride arrives, disgrace follows, but with the humble comes wisdom.",
      "T": "Pride does not travel alone — it always brings dishonor in its wake. Wisdom, however, chooses to travel with the humble."
    },
    "3": {
      "L": "The integrity of the upright shall guide them, but the perverseness of transgressors shall destroy them.",
      "M": "The integrity of the upright guides them, but the treachery of the faithless destroys them.",
      "T": "The upright person's integrity works like a compass — always pointing toward the right road. The treacherous person's own dishonesty is the thing that brings them down."
    },
    "4": {
      "L": "Riches profit not in the day of wrath, but righteousness delivereth from death.",
      "M": "Wealth is of no use on the day of wrath, but righteousness delivers from death.",
      "T": "When judgment comes — the kind of day that strips everything down to what you are — wealth is useless. Only righteousness has any currency in that moment."
    },
    "5": {
      "L": "The righteousness of the blameless shall direct his way, but the wicked shall fall by his own wickedness.",
      "M": "The righteousness of the blameless makes his way straight, but the wicked fall by their own wickedness.",
      "T": "The blameless person's righteousness clears the road ahead of them. The wicked person trips over their own wickedness — they do it to themselves."
    },
    "6": {
      "L": "The righteousness of the upright shall deliver them, but transgressors shall be taken by their own evil desire.",
      "M": "The righteousness of the upright rescues them, but the treacherous are trapped by their own evil desires.",
      "T": "Uprightness is a rescue — it saves the person who practices it. The treacherous, however, are caught in the trap of their own cravings."
    },
    "7": {
      "L": "When the wicked man dieth, his expectation perisheth, and the hope of unjust men perisheth.",
      "M": "When a wicked man dies, his expectation perishes, and the hope placed in wrongdoers comes to nothing.",
      "T": "Death settles everything. The wicked person's hopes — all the things they counted on — evaporate at death. Whatever they expected from their schemes comes to nothing."
    },
    "8": {
      "L": "The righteous is delivered out of trouble, and the wicked cometh in his place.",
      "M": "The righteous are rescued from trouble, and the wicked take their place in it.",
      "T": "The righteous person escapes the trouble that was meant for them — and the wicked person steps into it instead."
    },
    "9": {
      "L": "An hypocrite with his mouth destroyeth his neighbour, but through knowledge shall the just be delivered.",
      "M": "Through his words the godless person destroys his neighbor, but the righteous are saved through knowledge.",
      "T": "The godless person uses speech as a weapon — words that ruin the people around them. The righteous person's knowledge of what is true becomes their protection."
    },
    "10": {
      "L": "When it goeth well with the righteous, the city rejoiceth, and when the wicked perish, there is shouting.",
      "M": "When the righteous prosper, the city rejoices, and when the wicked perish, there are shouts of joy.",
      "T": "A city takes on the character of the people who run it. When the righteous flourish, the whole community thrives. When the wicked fall, the city breathes out in relief."
    },
    "11": {
      "L": "By the blessing of the upright the city is exalted, but by the mouth of the wicked it is overthrown.",
      "M": "By the blessing of the upright the city is lifted up, but by the mouth of the wicked it is torn down.",
      "T": "What comes from the upright — their lives, their words, their work — builds the city up. What the wicked say tears it down."
    },
    "12": {
      "L": "He that is void of wisdom despiseth his neighbour, but a man of understanding holdeth his peace.",
      "M": "Whoever despises his neighbor lacks good sense, but a man of understanding stays silent.",
      "T": "Contempt for a neighbor is a sure sign of foolishness. The person with real understanding knows when not to speak — especially when speaking would only tear down."
    },
    "13": {
      "L": "A talebearer revealeth secrets, but he that is of a faithful spirit concealeth a matter.",
      "M": "Whoever goes about gossiping reveals secrets, but a person of faithful spirit keeps confidence.",
      "T": "The gossip cannot help themselves — every confidence is a potential broadcast. The trustworthy person treats what is shared in private as sacred. Their spirit is faithful."
    },
    "14": {
      "L": "Where no counsel is, the people fall, but in the multitude of counsellors there is safety.",
      "M": "Without guidance, a people falls, but with many counselors comes safety.",
      "T": "Without wise steering, a community loses its way. The more good advisors you surround yourself with, the better your chances of getting through."
    },
    "15": {
      "L": "He that is surety for a stranger shall smart for it, but he that hateth suretyship is secure.",
      "M": "Whoever gives surety for a stranger will suffer harm, but whoever refuses such pledges is safe.",
      "T": "Guaranteeing the debts of someone you don't truly know is a reliable way to suffer. The person wise enough to refuse such pledges protects themselves."
    },
    "16": {
      "L": "A gracious woman retaineth honour, and ruthless men retain riches.",
      "M": "A gracious woman gains honor, but ruthless men gain only wealth.",
      "T": "A woman of grace earns something that lasts — honor and the respect that follows. Violent men can accumulate money, but it is a poor substitute for what she has."
    },
    "17": {
      "L": "The merciful man doeth good to his own soul, but the cruel troubleth his own flesh.",
      "M": "A kind man benefits himself, but the cruel person causes harm to himself.",
      "T": "Kindness and cruelty both come back to their source. The kind person builds something in themselves. The cruel person tears themselves apart — the harm they do to others always reaches them."
    },
    "18": {
      "L": "The wicked worketh a deceitful work, but to him that soweth righteousness shall be a sure reward.",
      "M": "The wicked earns deceptive wages, but whoever sows righteousness gains a sure reward.",
      "T": "The wicked person's earnings are a lie — they seem like income but they cannot be held. The one who sows righteousness, however, reaps something that is genuinely real."
    },
    "19": {
      "L": "As righteousness tendeth to life, so he that pursueth evil pursueth it to his own death.",
      "M": "Genuine righteousness leads to life, but whoever pursues evil runs toward his own death.",
      "T": "Righteousness and life travel together. Evil and death are also inseparable — and the person who chases evil is running straight toward death without knowing it."
    },
    "20": {
      "L": "They that are of a froward heart are abomination to the LORD, but such as are blameless in their way are his delight.",
      "M": "Those with crooked hearts are detestable to the LORD, but those whose ways are blameless are his delight.",
      "T": "The LORD takes note of what is bent in us and what is straight. The twisted heart repels him. The blameless life — that is what he takes genuine pleasure in."
    },
    "21": {
      "L": "Though hand join in hand, the wicked shall not go unpunished, but the seed of the righteous shall be delivered.",
      "M": "Be assured: the wicked will not go unpunished, but the offspring of the righteous will escape.",
      "T": "No matter how many allies the wicked man gathers, justice will find him. The righteous person's children, however, have a way of escape."
    },
    "22": {
      "L": "As a jewel of gold in a swine's snout, so is a fair woman who is without discretion.",
      "M": "Like a gold ring in a pig's snout is a beautiful woman who lacks discretion.",
      "T": "Beauty without wisdom is as absurd as expensive jewelry on a pig — both are wasted, and one of them is in the wrong place entirely."
    },
    "23": {
      "L": "The desire of the righteous is only good, but the expectation of the wicked is wrath.",
      "M": "The desire of the righteous ends in good, but the hope of the wicked brings wrath.",
      "T": "The righteous want what is genuinely good — and that is what their desire comes to. The wicked hope for what they hope for, and find wrath instead."
    },
    "24": {
      "L": "There is that scattereth and yet increaseth, and there is that withholdeth more than is meet, but it tendeth to poverty.",
      "M": "One person gives freely and grows richer, while another withholds what he should give and only grows poorer.",
      "T": "The world runs on a different economy than we expect: the generous person gets more. The person who hoards what should be shared ends up with less. This defies logic — but it is what happens."
    },
    "25": {
      "L": "The generous soul shall be made fat, and he that watereth shall be watered also himself.",
      "M": "A generous person will be enriched, and whoever waters others will himself be watered.",
      "T": "Generosity is self-replenishing. The one who blesses others becomes more blessed. The one who pours out finds that something pours back in."
    },
    "26": {
      "L": "He that withholdeth grain, the people shall curse him, but blessing shall be upon the head of him that selleth it.",
      "M": "The people curse whoever hoards grain, but blessings fall on the head of whoever sells it.",
      "T": "Hoarding food in a time of scarcity earns contempt. The one who makes it available — even for profit — is celebrated. Commerce in essentials is a blessing when it actually gets goods to people."
    },
    "27": {
      "L": "He that diligently seeketh good procureth favour, but he that seeketh mischief, it shall come upon him.",
      "M": "Whoever earnestly seeks good will gain favor, but evil comes upon whoever pursues it.",
      "T": "What you pursue has a way of finding you. Seek good — you will find favor. Chase after evil — and evil will catch you."
    },
    "28": {
      "L": "He that trusteth in his riches shall fall, but the righteous shall flourish as a branch.",
      "M": "Whoever trusts in his wealth will fall, but the righteous will flourish like a fresh branch.",
      "T": "Money is not a foundation — it is a platform that collapses. The righteous person, who trusts in something else, grows the way a healthy branch grows: alive, upward, persistent."
    },
    "29": {
      "L": "He that troubleth his own house shall inherit the wind, and the fool shall be servant to the wise of heart.",
      "M": "Whoever brings trouble on his own household will inherit the wind, and the fool will end up serving the wise of heart.",
      "T": "Tear your own household apart and you inherit exactly what you earned — nothing at all, just wind. And the fool who thought he could make his own way ends up in service to the person who actually had wisdom."
    },
    "30": {
      "L": "The fruit of the righteous is a tree of life, and he that winneth souls is wise.",
      "M": "The fruit of the righteous is a tree of life, and whoever wins people to wisdom is wise.",
      "T": "The righteous person's life is generative — what they produce becomes life for others, like a tree that gives fruit and shade and seed. And the one who draws others toward wisdom? That is the highest form of wisdom itself."
    },
    "31": {
      "L": "Behold, the righteous shall be recompensed in the earth; much more the wicked and the sinner.",
      "M": "If the righteous receive what they deserve on earth, how much more the wicked and the sinner!",
      "T": "If even the righteous face consequences for their actions in this life — what happens to the wicked? The math is sobering."
    }
  },
  "12": {
    "1": {
      "L": "Whoso loveth instruction loveth knowledge, but he that hateth reproof is brutish.",
      "M": "Whoever loves discipline loves knowledge, but whoever hates correction is without understanding.",
      "T": "Love of learning and love of correction are the same thing — you cannot have one without the other. Anyone who hates being corrected has given up on growing. That is not wisdom; it is an animal stubbornness."
    },
    "2": {
      "L": "A good man obtaineth favour of the LORD, but a man of wicked devices will he condemn.",
      "M": "A good man obtains favor from the LORD, but a man who schemes wickedly he condemns.",
      "T": "The LORD notices the character behind the actions. The person of genuine goodness finds favor with him. The schemer — the one whose mind runs on wicked plans — finds condemnation instead."
    },
    "3": {
      "L": "A man shall not be established by wickedness, but the root of the righteous shall not be moved.",
      "M": "No one is made secure by wickedness, but the root of the righteous will not be shaken.",
      "T": "Wickedness cannot provide real stability — whatever is built on it will shift. The righteous person, however, is rooted — and roots do not move when the storms come."
    },
    "4": {
      "L": "A virtuous woman is a crown to her husband, but she that causeth shame is as rottenness in his bones.",
      "M": "An excellent wife is a crown to her husband, but she who brings shame is like decay in his bones.",
      "T": "A woman of strength and character crowns her husband — she is his greatest asset, his visible honor. The one who brings shame does not just hurt him — she rots him from the inside."
    },
    "5": {
      "L": "The thoughts of the righteous are right, but the counsels of the wicked are deceit.",
      "M": "The plans of the righteous are just, but the schemes of the wicked are deceitful.",
      "T": "What goes on inside a person tells you everything. The righteous person's inner life runs on justice. The wicked person's plans are built on deception — all the way down."
    },
    "6": {
      "L": "The words of the wicked are to lie in wait for blood, but the mouth of the upright shall deliver them.",
      "M": "The words of the wicked set an ambush for blood, but the mouth of the upright delivers people.",
      "T": "The wicked use words as weapons — every sentence is an ambush laid for someone. The upright use words differently: they rescue people."
    },
    "7": {
      "L": "The wicked are overthrown and are not, but the house of the righteous shall stand.",
      "M": "The wicked are overthrown and are gone, but the house of the righteous stands firm.",
      "T": "The wicked are toppled. They go down and are not replaced — they simply are not. But what the righteous build outlasts them."
    },
    "8": {
      "L": "A man shall be commended according to his wisdom, but he that is of a perverse heart shall be despised.",
      "M": "A man is praised according to his wisdom, but one with a twisted mind is despised.",
      "T": "Wisdom earns its reputation over time — people eventually recognize it and honor it. A warped way of thinking earns something else: contempt."
    },
    "9": {
      "L": "He that is lightly esteemed and hath a servant is better than he that honoureth himself and lacketh bread.",
      "M": "It is better to be of humble standing and have food than to put on airs and lack bread.",
      "T": "A person who admits their modest circumstances but actually eats well is better off than the one who performs greatness while their cupboards are empty."
    },
    "10": {
      "L": "A righteous man regardeth the life of his animal, but the tender mercies of the wicked are cruel.",
      "M": "A righteous man cares for the wellbeing of his animal, but even the compassion of the wicked is cruel.",
      "T": "The righteous person's character extends all the way to how they treat their animals. The wicked person's attempts at kindness are cruel — not intentionally, perhaps, but because cruelty is built into who they are."
    },
    "11": {
      "L": "He that tilleth his land shall be satisfied with bread, but he that followeth vain persons is void of understanding.",
      "M": "Whoever works his land will have plenty of bread, but whoever chases empty pursuits lacks good sense.",
      "T": "Ground worked patiently produces food. Empty pursuits produce nothing. The person who cannot tell the difference — who chases fantasies while real work waits — lacks basic wisdom."
    },
    "12": {
      "L": "The wicked desireth the catch of evil men, but the root of the righteous yieldeth fruit.",
      "M": "The wicked crave what evil people catch, but the root of the righteous produces its own fruit.",
      "T": "The wicked see the ill-gotten gains of other wicked people and want them. But what they are chasing is borrowed — taken from others. The righteous person grows something of their own: rooted, organic, lasting."
    },
    "13": {
      "L": "The wicked is snared by the transgression of his lips, but the just shall come out of trouble.",
      "M": "An evil man is trapped by the sins of his lips, but the righteous escapes from trouble.",
      "T": "What the wicked man says builds the cage that holds him — his own words become his trap. The righteous person, however, finds a way out."
    },
    "14": {
      "L": "A man shall be satisfied with good by the fruit of his mouth, and the recompence of a man's hands shall be rendered to him.",
      "M": "From the fruit of his words a man is satisfied with good, and the work of his hands comes back to him.",
      "T": "What you say and what you do both return to you. The fruit of your words nourishes you — or poisons you. The work of your hands finds its way back."
    },
    "15": {
      "L": "The way of a fool is right in his own eyes, but he that hearkeneth to counsel is wise.",
      "M": "The path of a fool seems right to him, but a wise person listens to counsel.",
      "T": "The fool's deepest problem is that he cannot see his own foolishness — his path looks perfectly fine from where he stands. The wise person knows their own perspective is incomplete and so they listen."
    },
    "16": {
      "L": "A fool's wrath is presently known, but a prudent man covereth shame.",
      "M": "A fool's annoyance is known at once, but a prudent person overlooks an insult.",
      "T": "Fools wear their emotions on the outside — the moment someone offends them, everyone knows it. The prudent person has learned to absorb an insult without broadcasting it."
    },
    "17": {
      "L": "He that speaketh truth sheweth forth righteousness, but a false witness speaketh deceit.",
      "M": "A truthful witness gives honest testimony, but a false witness speaks lies.",
      "T": "In any dispute, everything depends on whether the witness tells the truth. The honest witness is an instrument of justice. The false witness brings only lies — and injustice follows."
    },
    "18": {
      "L": "There is that speaketh like the piercings of a sword, but the tongue of the wise is health.",
      "M": "Reckless words pierce like a sword, but the tongue of the wise brings healing.",
      "T": "Words can cut. The person who speaks carelessly — whose words have no filter between thought and mouth — can wound as deeply as a sword. The wise person's words do the opposite: they heal."
    },
    "19": {
      "L": "The lip of truth shall be established for ever, but a lying tongue is but for a moment.",
      "M": "Truthful lips stand firm forever, but a lying tongue lasts only a moment.",
      "T": "Truth holds. A lying tongue has a shorter lifespan than it thinks — it lasts only until the truth arrives."
    },
    "20": {
      "L": "Deceit is in the heart of them that devise evil, but to the counsellors of peace is joy.",
      "M": "Deceit fills the heart of those who plan evil, but those who counsel peace find joy.",
      "T": "Inside the schemer is deceit — it is not just their method, it is their interior. Inside those who work for peace is joy. The inside always tells you."
    },
    "21": {
      "L": "There shall no evil happen to the just, but the wicked shall be filled with mischief.",
      "M": "No harm happens to the righteous, but the wicked are filled with trouble.",
      "T": "The righteous are not immune to hardship — but the specific harm that falls on the wicked finds another destination. The wicked, however, get exactly what their lives are calling toward."
    },
    "22": {
      "L": "Lying lips are abomination to the LORD, but they that deal truly are his delight.",
      "M": "Lying lips are detestable to the LORD, but those who act faithfully are his delight.",
      "T": "The LORD has strong feelings about truth. Lying lips — the habitual choice to deceive — are an abomination to him. But those who deal faithfully, whose word matches reality — they are what he delights in."
    },
    "23": {
      "L": "A prudent man concealeth knowledge, but the heart of fools proclaimeth foolishness.",
      "M": "A prudent man conceals what he knows, but the heart of a fool broadcasts its folly.",
      "T": "The wise person does not advertise everything they know — discernment includes knowing when to speak and when to keep quiet. The fool, by contrast, has no filter: their folly comes out whether they intend it to or not."
    },
    "24": {
      "L": "The hand of the diligent shall bear rule, but the slothful shall be put to forced labour.",
      "M": "The diligent hand will rule, but the lazy will be put to forced labor.",
      "T": "Diligence eventually leads to authority. Laziness leads to servitude. The lazy person who expects leisure will find themselves at the bottom of someone else's structure."
    },
    "25": {
      "L": "Heaviness in the heart of a man maketh it stoop, but a good word maketh it glad.",
      "M": "Anxiety in a man's heart weighs him down, but a good word makes him glad.",
      "T": "Worry is a heavy thing — it bends a person. But a word spoken at the right moment with the right intent can lift the weight entirely. This is not a small thing."
    },
    "26": {
      "L": "The righteous is more excellent than his neighbour, but the way of the wicked seduceth them.",
      "M": "The righteous man guides his neighbor well, but the way of the wicked leads them astray.",
      "T": "The righteous person's life has a gravitational pull — they draw others toward the right path. The wicked person's way has a different pull: it misleads whoever follows."
    },
    "27": {
      "L": "The slothful man roasteth not that which he took in hunting, but the substance of a diligent man is precious.",
      "M": "The lazy man does not even bother to prepare his game, but the wealth of a diligent man is a precious thing.",
      "T": "The lazy person cannot follow through on the effort they start — they hunt but cannot be bothered to cook what they caught. Meanwhile, everything the diligent person accumulates has value, because it came from sustained effort."
    },
    "28": {
      "L": "In the way of righteousness is life, and in the pathway thereof there is no death.",
      "M": "In the path of righteousness is life, and along that road there is no death.",
      "T": "The righteous road leads to life — and it is a road without a dead end. Righteousness and life are the same destination, and the path never arrives anywhere else."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 10–12 written.')

if __name__ == '__main__':
    main()
