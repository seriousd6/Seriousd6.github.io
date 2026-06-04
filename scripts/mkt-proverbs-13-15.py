"""
MKT Proverbs chapters 13–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-13-15.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" (all caps) in L/M; "the LORD" in T — consistent with chs. 1–12.

- H2451 (חָכְמָה, chokmah): "wisdom" in all tiers — consistent with chs. 1–12.

- H5315 (נֶפֶשׁ, nephesh): Context-driven:
  * 13:2 = "soul" (the treacherous soul desires violence — full embodied person)
  * 13:4 = "soul" (soul of the sluggard / soul of the diligent — appetite and drive)
  * 13:19 = "soul" (desire accomplished is sweet to the soul)
  * 13:25 = "soul" (eats to the satisfying of his soul)

- H7307 (רוּחַ, ruach): 14:29 = "spirit" (hasty of spirit — character quality, temperament, not divine Spirit).

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L; "detestable" in M; context-driven in T.
  Appears in: 13:19, 15:8, 15:9, 15:26.

- H7585 (שְׁאוֹל, sheol): "hell" in L (consistent with prior Proverbs scripts); "Sheol" in T
  where the theological precision is helpful (15:11, 15:24).

- H6106 (עֶצֶם, etsem): "bones" throughout — both 14:30 (envy = rottenness of bones) and
  15:30 (good report makes bones fat). Preserved as the most striking, accurate image.

- H2617 (חֶסֶד, hesed): 14:22 = "loyal love / steadfast love" — when parallel with
  H571 emet (faithfulness/truth), the covenantal weight of hesed is fully present.
  Rendered "loyal love" in M and "covenant love" in T to distinguish from generic mercy.

- H6627 (תּוֹצָאוֹת, totsa'ot, life/living = "fountain of life"): 13:14, 14:27 — "fountain of
  life" in all tiers. Key image recurring from ch. 10.

- H3820 (לֵב, lev): "heart" in all tiers — the seat of will, emotion, and intellect combined.

- H6086+H2416 (tree of life): 13:12, 15:4 — "tree of life" preserved in all tiers. The
  image echoes Gen 2–3 and Prov 3:18.

- H7626 (שֵׁבֶט, shebet): "rod" in all tiers (13:24) — the rod of discipline is a concrete
  Hebrew idiom for parental correction. Not softened to "discipline" in L tier.

- H191 (אֱוִיל, 'evil) vs H3684 (כְּסִיל, kesil): Both rendered "fool" in L/M for
  readability. T tier distinguishes where context warrants.

- Antithetical couplet structure: Chapters 13–15 continue the paired A/B form of chs. 10–12.
  L/M preserve both poles. T may expand or add interpretive depth but always holds both.

- Gnomic aspect: Imperfect and participle forms throughout are timeless generalities.
  Rendered as simple present or future in English throughout.

- 13:12 ("hope deferred"): One of the most psychologically resonant verses in Proverbs.
  T tier draws out the somatic/physiological weight of prolonged deferred expectation.

- 14:12 ("a way that seems right"): The theological weight of this warning is significant.
  It cannot be flattened. T tier holds the full unease without ornamenting it.

- 14:31 (oppressing the poor = insulting the Maker): The social justice dimension here is
  direct. God is the Maker of the poor; harm done to them touches him personally.

- 15:11 (Sheol and Abaddon before the LORD): "Hell and destruction" in L (KJV idiom);
  "Death and Destruction" in M; "Sheol and Abaddon" in T for theological precision.

- 15:33 (fear of LORD = instruction of wisdom; humility before honor): Closing verse of ch.
  15 functions as a hinge — summarizing the epistemology of the entire Proverbs project.
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
  "13": {
    "1": {
      "L": "A wise son heareth a father's instruction, but a scorner heareth not rebuke.",
      "M": "A wise son heeds his father's instruction, but a mocker does not listen to rebuke.",
      "T": "The son who has become wise is the one who listened to his father. The mocker shuts his ears to any correction — and that is precisely what makes him a mocker."
    },
    "2": {
      "L": "Of the fruit of his mouth a man shall eat good, but the soul of the treacherous shall eat violence.",
      "M": "A man eats well from the fruit of his words, but the soul of the treacherous craves violence.",
      "T": "Your words produce what you live on — speak well and you nourish yourself and others. The treacherous person, however, wants something different: violence is what they hunger for."
    },
    "3": {
      "L": "He that guardeth his mouth keepeth his life, but he that openeth wide his lips shall have destruction.",
      "M": "Whoever guards his mouth protects his life, but whoever speaks without restraint will come to ruin.",
      "T": "A guarded mouth is a protected life. Reckless speech, by contrast, opens the door to destruction — a door the fool does not realize he has just opened."
    },
    "4": {
      "L": "The soul of the sluggard desireth and hath nothing, but the soul of the diligent is made fat.",
      "M": "The soul of a lazy person craves and gets nothing, but the diligent soul is richly satisfied.",
      "T": "The sluggard wants everything but does the work for nothing. Desire disconnected from effort produces exactly what it deserves — nothing. The diligent person wants and works — and ends up more than satisfied."
    },
    "5": {
      "L": "A righteous man hateth lying, but a wicked man is loathsome and cometh to shame.",
      "M": "A righteous man hates falsehood, but a wicked man acts disgracefully and brings shame.",
      "T": "The righteous person has a visceral reaction against lying — they cannot stand it. The wicked person has grown so comfortable with dishonesty that they have become repulsive to those around them."
    },
    "6": {
      "L": "Righteousness keepeth him that is upright in his way, but wickedness overthroweth the sinner.",
      "M": "Righteousness guards the one who walks uprightly, but wickedness brings down the sinner.",
      "T": "Righteousness is active — it guards the person who walks in it. Wickedness is also active — it topples the person who walks in it. What you walk in, walks with you."
    },
    "7": {
      "L": "There is that maketh himself rich yet hath nothing, and there is that maketh himself poor yet hath great riches.",
      "M": "One person acts rich and has nothing; another acts poor yet has great wealth.",
      "T": "Two illusions: the person who performs wealth but possesses none — all show, no substance. And the person who performs poverty but holds great riches. Appearances deceive in both directions."
    },
    "8": {
      "L": "The ransom of a man's life are his riches, but the poor heareth no rebuke.",
      "M": "A man's wealth may ransom his life, but a poor man hears no threatening.",
      "T": "Wealth has one advantage: it can buy your way out of danger. The poor person faces a different reality — there are no ransom demands for someone who has nothing. Their poverty is, in a strange way, also their protection."
    },
    "9": {
      "L": "The light of the righteous rejoiceth, but the lamp of the wicked shall be put out.",
      "M": "The light of the righteous shines with joy, but the lamp of the wicked will be extinguished.",
      "T": "The righteous have a light that glows with vitality — it rejoices. The wicked also have a lamp, but it is already running down. It will be put out. This is not a threat; it is an observation about what they are holding."
    },
    "10": {
      "L": "Only by pride cometh contention, but with the well-advised is wisdom.",
      "M": "Pride produces nothing but conflict, but wisdom is found in those who take counsel.",
      "T": "Pride is the engine behind most conflicts — it starts them, fuels them, will not let them end. Wisdom does not live in the proud; it lives in people who have learned to take advice."
    },
    "11": {
      "L": "Wealth gotten by vanity shall be diminished, but he that gathereth by labour shall increase.",
      "M": "Wealth gained by fraud will shrink, but whoever gathers it gradually through labor will see it grow.",
      "T": "Easy money disappears fast — it does not have the staying power of what is built slowly. The patient accumulator, gathering piece by piece through honest work, sees their wealth grow."
    },
    "12": {
      "L": "Hope deferred maketh the heart sick, but a desire accomplished is a tree of life.",
      "M": "Hope deferred makes the heart grow sick, but a longing fulfilled is a tree of life.",
      "T": "Waiting for what you need — hoping for it to come while it does not — wears on the soul in a specific, physical way. But the moment desire is met, something like a tree of life is planted in you: nourishing, renewing, generative."
    },
    "13": {
      "L": "Whoso despiseth the word shall be destroyed, but he that feareth the commandment shall be rewarded.",
      "M": "Whoever despises instruction will be brought to ruin, but whoever respects the commandment will be rewarded.",
      "T": "Treating God's word with contempt is self-destruction in slow motion. Treating it with reverence — actually taking it seriously — brings its own reward."
    },
    "14": {
      "L": "The law of the wise is a fountain of life, to depart from the snares of death.",
      "M": "The teaching of the wise is a fountain of life, turning one away from the traps of death.",
      "T": "The wise person's teaching is life-giving and practical: it not only refreshes you, it steers you away from the traps that would kill you. That is a fountain worth drinking from."
    },
    "15": {
      "L": "Good understanding giveth favour, but the way of the treacherous is hard.",
      "M": "Good understanding wins favor, but the way of the treacherous leads to their ruin.",
      "T": "Genuine good sense earns the goodwill of those around you. The treacherous, by contrast, have chosen a road that is harsh — hard going, and inevitably destructive."
    },
    "16": {
      "L": "Every prudent man dealeth with knowledge, but a fool layeth open his folly.",
      "M": "Every prudent person acts from knowledge, but a fool broadcasts his foolishness.",
      "T": "The prudent person brings knowledge to everything they do — you can see it in how they act. The fool cannot help revealing what he is. He puts it on display without meaning to."
    },
    "17": {
      "L": "A wicked messenger falleth into mischief, but a faithful ambassador is health.",
      "M": "A wicked messenger causes harm, but a trustworthy envoy brings healing.",
      "T": "The quality of a message is only as good as the character of the messenger. A messenger whose character is bent causes damage wherever he goes. The trustworthy one carries healing with him."
    },
    "18": {
      "L": "Poverty and shame shall be to him that refuseth instruction, but he that regardeth reproof shall be honoured.",
      "M": "Poverty and disgrace come to whoever refuses discipline, but honor comes to whoever accepts correction.",
      "T": "The person who cannot bear to be corrected will end up poor and disgraced — they paid a very high price to protect their ego. The one who learns to receive correction is honored."
    },
    "19": {
      "L": "The desire accomplished is sweet to the soul, but it is abomination to fools to depart from evil.",
      "M": "A longing fulfilled is sweet to the soul, but fools find it revolting to turn from evil.",
      "T": "When a real longing is met, the sweetness goes all the way down. But here is the strange thing: the fool finds the idea of turning away from evil genuinely offensive — more offensive than evil itself."
    },
    "20": {
      "L": "He that walketh with wise men shall be wise, but a companion of fools shall suffer harm.",
      "M": "Walk with the wise and you will become wise, but whoever befriends fools will suffer harm.",
      "T": "Who you spend time with shapes who you become — this is not a metaphor, it is a mechanism. Walk with the wise and wisdom gradually forms in you. Keep company with fools and the damage is just as real."
    },
    "21": {
      "L": "Evil pursueth sinners, but good shall be repayed to the righteous.",
      "M": "Calamity pursues sinners, but the righteous will be rewarded with good.",
      "T": "Sin carries misfortune in its wake — it follows the sinner like a creditor. The righteous, however, move through life drawing good toward them — not as a transaction, but because they walk in alignment with how things actually work."
    },
    "22": {
      "L": "A good man leaveth an inheritance to his children's children, and the wealth of the sinner is laid up for the just.",
      "M": "A good man leaves an inheritance for his grandchildren, but the wealth of a sinner is stored up for the righteous.",
      "T": "The good person thinks long — not just for today or next year, but for grandchildren not yet born. The sinner accumulates too, but what they store up ends up in the hands of the righteous. Providence is longer than wickedness."
    },
    "23": {
      "L": "Much food is in the tillage of the poor, but there is that is destroyed for want of judgment.",
      "M": "The land of the poor may produce abundant food, but it is swept away through injustice.",
      "T": "The poor person's field could feed them — the potential is there. But injustice can destroy everything: bad laws, corrupt officials, abusive landlords. Potential is not the same as outcome when the powerful are corrupt."
    },
    "24": {
      "L": "He that spareth his rod hateth his son, but he that loveth him chasteneth him betimes.",
      "M": "Whoever spares the rod hates his son, but whoever loves him disciplines him while there is time.",
      "T": "Refusing to discipline a child is not kindness — it is a form of contempt, a giving up on them. Genuine love takes the harder road: consistent, early, persistent discipline. It costs more but gives more."
    },
    "25": {
      "L": "The righteous eateth to the satisfying of his soul, but the belly of the wicked shall want.",
      "M": "The righteous eat until they are satisfied, but the stomach of the wicked goes hungry.",
      "T": "There is a quiet justice in appetite itself: the righteous find satisfaction — they eat until full. The wicked remain hungry no matter what they accumulate."
    }
  },
  "14": {
    "1": {
      "L": "Every wise woman buildeth her house, but the foolish woman teareth it down with her hands.",
      "M": "A wise woman builds up her household, but a foolish woman tears hers down with her own hands.",
      "T": "Wisdom in a woman becomes the structural force of her household — she builds it. Folly does the opposite, and does the work personally: with her own hands, she dismantles everything."
    },
    "2": {
      "L": "He that walketh in his uprightness feareth the LORD, but he that is perverse in his ways despiseth him.",
      "M": "Whoever walks in uprightness fears the LORD, but whoever is crooked in his ways despises him.",
      "T": "How you live is a theological statement. The upright life declares that you fear the LORD. The crooked life declares, whether you realize it or not, that you despise him."
    },
    "3": {
      "L": "In the mouth of the foolish is a rod of pride, but the lips of the wise shall preserve them.",
      "M": "A fool's talk brings punishment upon himself, but the lips of the wise protect them.",
      "T": "The fool's arrogant speech is the very thing that beats him — his pride becomes the rod that falls on his own back. The wise person's lips do the opposite: they protect him."
    },
    "4": {
      "L": "Where no oxen are, the crib is clean, but much increase is by the strength of the ox.",
      "M": "Where there are no oxen, the stall is clean, but much increase comes through the strength of an ox.",
      "T": "No oxen means no mess in the stall — everything is clean, organized, tidy. But it also means no work gets done and no harvest comes in. Some messes are the cost of fruitfulness. This applies well beyond farming."
    },
    "5": {
      "L": "A faithful witness will not lie, but a false witness will utter lies.",
      "M": "An honest witness does not lie, but a false witness breathes out lies.",
      "T": "Two kinds of witness — one whose character is bound up with truth, and one whose words pour out lies like breathing. You can tell the difference by what comes naturally to them."
    },
    "6": {
      "L": "A scorner seeketh wisdom and findeth it not, but knowledge is easy unto him that understandeth.",
      "M": "A mocker looks for wisdom but does not find it, but knowledge comes easily to a person of understanding.",
      "T": "The mocker chases wisdom and keeps missing it — because the door to wisdom is humility, and he will not go through it. The person who has already grasped the first principle finds that everything else comes naturally after."
    },
    "7": {
      "L": "Go from the presence of a foolish man, when thou perceivest not in him the lips of knowledge.",
      "M": "Stay away from a foolish person — there is no knowledge on his lips.",
      "T": "Some conversations are not worth having. When you realize there is no knowledge in what someone is saying — no wisdom, no insight, only noise — the wise thing is to leave."
    },
    "8": {
      "L": "The wisdom of the prudent is to understand his own way, but the folly of fools is deceit.",
      "M": "The wisdom of the prudent is to understand his way, but the folly of fools is self-deception.",
      "T": "Wisdom starts with self-knowledge: the prudent person actually understands what they are doing and where they are going. The fool's problem goes deeper — folly is built on self-deception. He does not know what he is doing and does not want to know."
    },
    "9": {
      "L": "Fools make a mock at guilt, but among the upright there is favour.",
      "M": "Fools scoff at making amends for sin, but among the upright there is goodwill.",
      "T": "The fool treats the need for atonement as something to laugh at — guilt and the repair of it are beneath him. The upright, who take both sin and restoration seriously, live in the atmosphere of God's favor."
    },
    "10": {
      "L": "The heart knoweth its own bitterness, and a stranger doth not intermeddle with its joy.",
      "M": "Each heart knows its own sorrow, and no outsider can fully share its joy.",
      "T": "You are the only one inside your own experience. Your deepest grief is known only to you — no one else fully enters it. Your deepest joy is also private in a way — no outsider can quite get inside it. This is not a complaint about loneliness; it is simply true."
    },
    "11": {
      "L": "The house of the wicked shall be overthrown, but the tabernacle of the upright shall flourish.",
      "M": "The household of the wicked will be ruined, but the tent of the upright will flourish.",
      "T": "The wicked build structures that look solid — but they will be pulled down. The upright, even living in something as modest as a tent, have something that grows and flourishes. The foundation matters more than the material."
    },
    "12": {
      "L": "There is a way which seemeth right unto a man, but the end thereof are the ways of death.",
      "M": "There is a path that seems right to a person, but it leads to death in the end.",
      "T": "This verse does not ask you to doubt every decision. But it warns you: the most dangerous roads look reasonable from the beginning. You can be walking toward death and have no idea, because everything seemed right when you started."
    },
    "13": {
      "L": "Even in laughter the heart is sorrowful, and the end of that mirth is heaviness.",
      "M": "Even in laughter the heart may ache, and the end of joy can be sorrow.",
      "T": "Human happiness is complicated. Laughter and grief coexist in the same moment — the heart can carry both. And the brightest celebrations sometimes lead straight into grief. This is not cynicism; it is honesty."
    },
    "14": {
      "L": "The backslider in heart shall be filled with his own ways, and a good man shall be satisfied from himself.",
      "M": "One who turns away from faithfulness is filled with the results of his own choices, but a good man finds satisfaction within himself.",
      "T": "The apostate — the one who turns away from God and goodness — gets the natural return on what they have invested in: themselves, their appetites, their schemes. They get full of it. The good person, by contrast, has genuine satisfaction — built in, not dependent on others."
    },
    "15": {
      "L": "The simple believeth every word, but the prudent man looketh well to his going.",
      "M": "The naive person believes everything he hears, but the prudent person gives careful thought to his steps.",
      "T": "Credulity — believing everything — is not virtue; it is vulnerability. The prudent person does not take every claim at face value but looks carefully at where each path leads before they walk it."
    },
    "16": {
      "L": "A wise man feareth and departeth from evil, but the fool rageth and is confident.",
      "M": "A wise man fears and turns from evil, but a fool is reckless and overconfident.",
      "T": "Wisdom includes a kind of healthy fear — the awareness of real danger that causes you to step back. The fool has no such instinct: he blows past every warning sign with total confidence, and that confidence is itself the problem."
    },
    "17": {
      "L": "He that is soon angry dealeth foolishly, and a man of wicked devices is hated.",
      "M": "A quick-tempered person acts foolishly, and a person who schemes wickedly is despised.",
      "T": "Quick anger leads to foolish actions — you act before you think. But there is another kind of bad actor: the deliberate schemer, who is hated not for losing control but for using control in the wrong direction."
    },
    "18": {
      "L": "The simple inherit folly, but the prudent are crowned with knowledge.",
      "M": "The naive end up with folly as their inheritance, but the prudent are crowned with knowledge.",
      "T": "It is what you end up with that reveals who you are. The simple person — who believes everything, questions nothing — inherits folly: it is the natural yield of their naivety. The prudent person gets crowned with knowledge: not just information, but the ability to navigate life well."
    },
    "19": {
      "L": "The evil bow down before the good, and the wicked at the gates of the righteous.",
      "M": "Evil people will bow before those who are good, and the wicked at the gates of the righteous.",
      "T": "This proverb describes the final alignment of things. The wicked will not always hold the upper hand. In the end, they are the ones who bow — standing at the gates of the righteous, looking up."
    },
    "20": {
      "L": "The poor is hated even of his own neighbour, but the rich hath many friends.",
      "M": "Even his neighbor dislikes a poor person, but a rich person has many friends.",
      "T": "This is not a moral prescription — it is a social observation, and a bitter one. Poverty repels even those closest to you. Wealth attracts people who may have no real loyalty at all. Both facts are unpleasant. The verse invites reflection, not imitation."
    },
    "21": {
      "L": "He that despiseth his neighbour sinneth, but he that hath mercy on the poor, happy is he.",
      "M": "Whoever despises his neighbor is sinning, but blessed is whoever shows kindness to the poor.",
      "T": "The natural response to poverty — contempt, avoidance — is called what it is: sin. The opposite response — showing mercy to the poor — is called something else: blessed. The moral calculus here is exact."
    },
    "22": {
      "L": "Do they not err that devise evil? But mercy and truth shall be to them that devise good.",
      "M": "Do not those who plot evil go astray? But those who plan good find loyal love and faithfulness.",
      "T": "Evil planning is a form of self-deception: the schemers think they are being smart, but they are wandering off course. Those who plan for good find that covenant love and faithfulness meet them — as if goodness travels with its reward."
    },
    "23": {
      "L": "In all labour there is profit, but the talk of the lips tendeth only to want.",
      "M": "There is profit in all hard work, but mere talk leads only to poverty.",
      "T": "Any actual work produces something — this is almost universally true. But talk without work produces exactly nothing. The person who substitutes talking about doing things for actually doing them ends up with nothing."
    },
    "24": {
      "L": "The crown of the wise is their riches, but the foolishness of fools remaineth folly.",
      "M": "The wealth of the wise is their crown, but fools' folly is folly to the end.",
      "T": "Wise people's prosperity adorns them — it fits who they are. But the fool's folly is just folly: no amount of accumulation transforms it into wisdom. What you are determines what your wealth looks like."
    },
    "25": {
      "L": "A true witness delivereth souls, but a deceitful witness speaketh lies.",
      "M": "A truthful witness saves lives, but a false witness deals in lies.",
      "T": "What is at stake in truthful testimony is human life. The honest witness can rescue someone from false accusation, from wrongful punishment, from death. The false witness takes that same power and inverts it."
    },
    "26": {
      "L": "In the fear of the LORD is strong confidence, and his children shall have a place of refuge.",
      "M": "The fear of the LORD is a source of strong confidence, and his children will find refuge in him.",
      "T": "The person who fears the LORD does not walk through life anxious — they walk in confident security. That security is not just personal: it extends to their children. What they have built in their own lives becomes shelter for the next generation."
    },
    "27": {
      "L": "The fear of the LORD is a fountain of life, to depart from the snares of death.",
      "M": "The fear of the LORD is a fountain of life, turning one away from the traps of death.",
      "T": "Fear of the LORD as a fountain of life — the image is worth sitting with. It does not merely sustain; it actively turns you away from the death-traps that surround any human life. The fear of God is practical protection."
    },
    "28": {
      "L": "In the multitude of people is the king's honour, but in the want of people is the destruction of the prince.",
      "M": "A large population is a king's glory, but a prince is ruined by a lack of people.",
      "T": "A ruler's greatness is measured in the people he governs — without them he is nothing. Power is relational: you cannot have it alone."
    },
    "29": {
      "L": "He that is slow to wrath is of great understanding, but he that is hasty of spirit exalteth folly.",
      "M": "Whoever is slow to anger shows great understanding, but a quick temper elevates foolishness.",
      "T": "Patience in the face of provocation is not weakness — it is a sign of deep understanding. The person who flares up quickly does something more damaging than just losing their temper: they elevate folly, they give it a platform, they make it louder."
    },
    "30": {
      "L": "A sound heart is the life of the flesh, but envy is the rottenness of the bones.",
      "M": "A calm and contented heart brings health to the body, but envy eats away at the bones.",
      "T": "Inner peace is physically restorative — the body lives differently when the heart is calm. Envy works the other way: it does not just disturb the mind, it works its way into the bones, into what is most structural and load-bearing in you, and rots it."
    },
    "31": {
      "L": "He that oppresseth the poor reproacheth his Maker, but he that honoureth him hath mercy on the needy.",
      "M": "Whoever oppresses the poor insults their Maker, but whoever shows kindness to the needy honors him.",
      "T": "When you mistreat the poor you are not just committing a social wrong — you are making a statement about God. He made them. Contempt for the creature is contempt for the Creator. Conversely, the one who shows mercy to the needy is honoring the One who made them."
    },
    "32": {
      "L": "The wicked is driven away in his wickedness, but the righteous hath hope in his death.",
      "M": "The wicked are brought down by their own evil, but the righteous have hope even in death.",
      "T": "The wicked person is driven away — destroyed by the very thing they chose. But the righteous person has something the wicked do not: hope. Even at death. That hope does not evaporate at the border of life."
    },
    "33": {
      "L": "Wisdom resteth in the heart of him that hath understanding, but that which is in the midst of fools is made known.",
      "M": "Wisdom quietly rests in the heart of the discerning, but it makes itself known even among fools.",
      "T": "The discerning person's wisdom is not on permanent display — it rests, quiet and deep. But even in a crowd of fools, wisdom has a way of making itself visible. It cannot remain hidden forever."
    },
    "34": {
      "L": "Righteousness exalteth a nation, but sin is a reproach to any people.",
      "M": "Righteousness lifts a nation up, but sin brings disgrace to any people.",
      "T": "This applies not just to individuals but to entire peoples. A nation shaped by righteousness is elevated — there is a moral gravity here. Sin, wherever it takes root in a people, produces shame: it degrades what was being built."
    },
    "35": {
      "L": "The king's favour is toward a wise servant, but his wrath is against him that causeth shame.",
      "M": "A king's favor rests on a servant who acts wisely, but his anger falls on one who acts shamefully.",
      "T": "In any governing structure, performance and character both matter to the one at the top. The servant who brings wisdom to his work earns favor. The one who brings shame earns wrath. Authority notices."
    }
  },
  "15": {
    "1": {
      "L": "A soft answer turneth away wrath, but a grievous word stirreth up anger.",
      "M": "A gentle answer turns away anger, but a harsh word stirs up wrath.",
      "T": "The choice you make in the moment of conflict — what to say and how to say it — determines what happens next. A measured, gentle answer deflects the anger entirely. The harsh word, by contrast, is gasoline."
    },
    "2": {
      "L": "The tongue of the wise useth knowledge aright, but the mouth of fools poureth out foolishness.",
      "M": "The tongue of the wise presents knowledge rightly, but the mouth of fools gushes foolishness.",
      "T": "Wisdom is not just about what you know — it is about what you do with what you know. The wise person speaks accurately and helpfully. The fool does not filter: foolishness pours out of them without restraint."
    },
    "3": {
      "L": "The eyes of the LORD are in every place, beholding the evil and the good.",
      "M": "The LORD's eyes are everywhere, watching both the evil and the good.",
      "T": "There is no unobserved corner of human activity — no transaction, no conversation, no private thought beyond the scope of God's sight. Both the evil and the good are watched. This should frighten the wicked and steady the righteous."
    },
    "4": {
      "L": "A wholesome tongue is a tree of life, but perverseness therein is a breach in the spirit.",
      "M": "A wholesome tongue is a tree of life, but a twisted tongue crushes the spirit.",
      "T": "A sound, gentle tongue is generative — it gives life the way a tree does, steadily and organically. The warped tongue does the opposite: it creates fractures in the spirit — damage that goes deep and takes time to heal."
    },
    "5": {
      "L": "A fool despiseth his father's instruction, but he that regardeth reproof is prudent.",
      "M": "A fool rejects his father's discipline, but whoever accepts correction shows good sense.",
      "T": "The most basic wisdom test: can you receive instruction from your own father? The fool cannot — he rejects it. The person who can receive correction, wherever it comes from, has the foundational quality of prudence."
    },
    "6": {
      "L": "In the house of the righteous is much treasure, but in the revenues of the wicked is trouble.",
      "M": "The household of the righteous holds great treasure, but the income of the wicked brings trouble.",
      "T": "What the righteous accumulate is genuine wealth — real treasure in the house. What the wicked earn comes bundled with trouble. The income looks the same on paper but has completely different content."
    },
    "7": {
      "L": "The lips of the wise disperse knowledge, but the heart of the foolish doeth not so.",
      "M": "The lips of the wise spread knowledge, but the minds of fools do not.",
      "T": "The wise person's words scatter knowledge like seeds — wherever they speak, something useful lands. The fool's heart, by contrast, has nothing to give. The lips of the wise are connected to something deep. The fool's are not."
    },
    "8": {
      "L": "The sacrifice of the wicked is an abomination to the LORD, but the prayer of the upright is his delight.",
      "M": "The LORD detests the sacrifice of the wicked, but the prayer of the upright is his delight.",
      "T": "God is not interested in religious performance from people who have not brought their lives into alignment with him. The wicked person's sacrifice, however elaborate, repels him. The upright person's prayer — however plain — is what he takes genuine pleasure in."
    },
    "9": {
      "L": "The way of the wicked is an abomination unto the LORD, but he loveth him that followeth after righteousness.",
      "M": "The LORD detests the way of the wicked, but he loves whoever earnestly pursues righteousness.",
      "T": "God's response to the wicked and the righteous is personal, not merely judicial. He finds the wicked person's path repellent — it offends him. And the one who chases after righteousness? He loves them. This is covenantal language."
    },
    "10": {
      "L": "Correction is grievous unto him that forsaketh the way, and he that hateth reproof shall die.",
      "M": "There is harsh discipline for the one who leaves the right path, and whoever hates correction will die.",
      "T": "Leaving the right path is not a neutral choice — it calls harsh correction down on you. And if you cannot tolerate being corrected? You are not just choosing discomfort; you are choosing death. The stakes of refusing reproof are that high."
    },
    "11": {
      "L": "Hell and destruction are before the LORD, how much more then the hearts of the children of men.",
      "M": "Death and Destruction lie open before the LORD — how much more the hearts of people!",
      "T": "Sheol and Abaddon — the realm of the dead and the place of ruin — are fully open to God's sight. If those hidden depths are transparent to him, then the human heart — which we think of as private — is thoroughly exposed. God knows what we carry inside us."
    },
    "12": {
      "L": "A scorner loveth not one that reproveth him, neither will he go unto the wise.",
      "M": "A mocker does not like being corrected and will not seek the company of the wise.",
      "T": "The mocker's aversion to correction is self-sealing: he hates being reproved, so he avoids the people who would reprove him — the wise. This means he is also avoiding the thing that would help him most, and he does it deliberately."
    },
    "13": {
      "L": "A merry heart maketh a cheerful countenance, but by sorrow of heart the spirit is broken.",
      "M": "A joyful heart makes a bright face, but a crushed spirit shows in the countenance.",
      "T": "The inner life always surfaces. Joy in the heart comes out in the face — it is irrepressible. And deep sorrow does not stay inside either: it breaks through, bends the spirit, makes itself visible. We cannot fully hide what we carry."
    },
    "14": {
      "L": "The heart of him that hath understanding seeketh knowledge, but the mouth of fools feedeth on foolishness.",
      "M": "A discerning heart is always seeking knowledge, but the mouth of a fool feeds on folly.",
      "T": "Understanding is an appetite: the discerning person perpetually hungers for more knowledge, keeps seeking it, can never quite get enough. The fool has a different diet — foolishness is what satisfies him, and he goes back for more."
    },
    "15": {
      "L": "All the days of the afflicted are evil, but he that is of a merry heart hath a continual feast.",
      "M": "All the days of the afflicted are miserable, but a joyful heart provides a constant feast.",
      "T": "The suffering person experiences every day as hard — not because things always go wrong, but because suffering colors everything. The person with a joyful heart has the opposite experience: every ordinary day is a feast. The inner disposition determines the flavor of the ordinary."
    },
    "16": {
      "L": "Better is little with the fear of the LORD than great treasure and trouble therewith.",
      "M": "Better to have little with the fear of the LORD than great wealth with turmoil.",
      "T": "Small resources held in the fear of God are worth more than large resources held in anxiety and spiritual distance. This reversal is one of Proverbs' signature moves: redefining value from the inside out."
    },
    "17": {
      "L": "Better is a dinner of herbs where love is, than a stalled ox and hatred therewith.",
      "M": "Better a simple meal where love is present than a lavish feast accompanied by hatred.",
      "T": "The quality of what happens at a table is determined not by the food but by what the people around it carry. A pot of vegetables eaten in genuine love outweighs the best feast eaten in hostility. What is between people matters more than what is on the table."
    },
    "18": {
      "L": "A wrathful man stirreth up strife, but he that is slow to anger appeaseth contention.",
      "M": "A hot-tempered man stirs up conflict, but whoever is slow to anger quiets it.",
      "T": "The angry person is a conflict-generator — their presence makes things worse. The patient person has the opposite effect: they appease, they de-escalate, they create the conditions for resolution. Both are multiplying something."
    },
    "19": {
      "L": "The way of the slothful man is as a hedge of thorns, but the way of the upright is made plain.",
      "M": "The path of the lazy is like a hedgerow of thorns, but the road of the upright is a level highway.",
      "T": "The lazy person's road is not merely difficult — it is hostile, full of obstacles, constantly cutting them. The upright person's road, by contrast, is cleared and level. Righteousness makes the way easier; laziness makes it impassable."
    },
    "20": {
      "L": "A wise son maketh a glad father, but a foolish man despiseth his mother.",
      "M": "A wise son brings his father joy, but a foolish man shows contempt for his mother.",
      "T": "Wisdom and folly have parents who feel them. The wise child is a father's ongoing joy. The foolish person, by contrast, has contempt for the very person who gave them life. That says something about what folly has done to them."
    },
    "21": {
      "L": "Folly is joy to him that is destitute of wisdom, but a man of understanding walketh uprightly.",
      "M": "Folly is entertaining to a person who lacks judgment, but a person of understanding walks straight.",
      "T": "The senseless person genuinely enjoys foolishness — it is entertainment to them. The person of understanding does not find foolishness amusing; they have somewhere to go, and they walk a straight line to get there."
    },
    "22": {
      "L": "Without counsel purposes are disappointed, but in the multitude of counsellors they are established.",
      "M": "Plans fail where there is no guidance, but with many counselors they succeed.",
      "T": "Big plans require input. Going it alone is not the same as being self-sufficient — it is a reliable path to failure. The more qualified advisors you bring around your plans, the better your chances of seeing those plans come to pass."
    },
    "23": {
      "L": "A man hath joy by the answer of his mouth, and a word spoken in due season, how good is it!",
      "M": "A person finds joy in giving the right answer, and how good is a timely word!",
      "T": "There is a specific satisfaction in saying exactly the right thing at exactly the right moment — the speaker and hearer both feel it. A well-timed word is one of the most useful things one human being can offer another."
    },
    "24": {
      "L": "The way of life is above to the wise, that he may depart from hell beneath.",
      "M": "The way of life leads upward for the wise, so that they may avoid Sheol below.",
      "T": "The wise person's trajectory is literally upward — moving toward life, not toward death. The direction they travel is away from Sheol, the realm of the dead beneath. Every good decision is a step in the right direction."
    },
    "25": {
      "L": "The LORD will destroy the house of the proud, but he will establish the border of the widow.",
      "M": "The LORD will pull down the house of the proud, but he maintains the widow's property lines.",
      "T": "The proud person builds something impressive — and God tears it down. The widow, who has no one to protect her boundary markers, has them maintained by God himself. Power protects itself; vulnerability is guarded by the LORD."
    },
    "26": {
      "L": "The thoughts of the wicked are an abomination to the LORD, but the words of the pure are pleasant words.",
      "M": "The LORD detests the plans of the wicked, but pure words are pleasing to him.",
      "T": "God looks at the interior. The wicked person's thoughts — not just their actions — are already an abomination to him. The pure person's words, however, are pleasant. What is inside comes out — and God receives it."
    },
    "27": {
      "L": "He that is greedy of gain troubleth his own house, but he that hateth gifts shall live.",
      "M": "Whoever is greedy for gain brings trouble to his own household, but whoever refuses bribes will live.",
      "T": "The greedy person thinks they are acquiring for themselves and their family, but the method contaminates the home. Unjust gain breeds trouble — it comes home with you. The one who refuses bribes chooses something better: life."
    },
    "28": {
      "L": "The heart of the righteous studieth to answer, but the mouth of the wicked poureth out evil things.",
      "M": "The heart of the righteous weighs its answer carefully, but the mouth of the wicked blurts out evil.",
      "T": "The righteous person does not speak reflexively — they think before they answer. There is something careful, considered, weighing going on inside before the words come out. The wicked person has no such governor: evil simply pours out of them."
    },
    "29": {
      "L": "The LORD is far from the wicked, but he heareth the prayer of the righteous.",
      "M": "The LORD is distant from the wicked, but he hears the prayer of the righteous.",
      "T": "Distance and nearness with God are moral, not spatial. The wicked person's prayers are not received — God is far from them in the most relevant sense. The righteous person speaks and is heard. Prayer only works when the relationship works."
    },
    "30": {
      "L": "The light of the eyes rejoiceth the heart, and a good report maketh the bones fat.",
      "M": "Bright eyes make the heart glad, and good news refreshes the whole body.",
      "T": "Joy comes through the eyes and into the heart — both literally and figuratively. Good news does something physical: it gets into the bones, makes them fat, renews the body from the inside. Good news is nourishing."
    },
    "31": {
      "L": "The ear that heareth the reproof of life abideth among the wise.",
      "M": "The ear that heeds life-giving correction will find its home among the wise.",
      "T": "There is a specific kind of rebuke — one that leads to life, not just to shame. The person who can recognize that kind of correction and actually hear it ends up where they belong: among the wise. The ear that listens its way to wisdom."
    },
    "32": {
      "L": "He that refuseth instruction despiseth his own soul, but he that heareth reproof getteth understanding.",
      "M": "Whoever refuses correction despises himself, but whoever accepts reproof gains insight.",
      "T": "Refusing instruction is a form of self-contempt — you are deciding that you are not worth improving. Accepting correction, however uncomfortable, is the opposite: it is taking your own development seriously. The one who learns gains understanding as the direct result."
    },
    "33": {
      "L": "The fear of the LORD is the instruction of wisdom, and before honour is humility.",
      "M": "The fear of the LORD is training in wisdom, and humility comes before honor.",
      "T": "The fear of the LORD is not the end of the journey — it is the curriculum. Everything else in wisdom flows from learning to stand correctly before God. And the order matters: humility first, then honor. You cannot skip the first step and get to the second."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 13–15 written.')

if __name__ == '__main__':
    main()
