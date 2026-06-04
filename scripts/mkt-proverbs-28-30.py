"""
MKT Proverbs chapters 28–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-28-30.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" in L/M; "the LORD" in T — consistent with chs 1–21.

- H8451 (תּוֹרָה, torah): "law" in L/M. In T, "God's instruction" where the full sense of
  covenant-structured teaching is foregrounded, but "law" maintained where "keeping the law"
  is the natural idiom (28:4, 7, 9; 29:18). Consistent with chs 1–21.

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L; "detestable" in M; "abomination" in T.
  Consistent with chs 10–21.

- H7307 (רוּחַ, ruach):
  * 29:11 = personal spirit / inner life of a fool ("all his mind" / "all his spirit") —
    clearly not wind/breath; rendered "spirit" in L, "feelings" in M, "spirit" in T.
  * 30:4 = the wind gathered in fists — rendered "wind" in L/M/T (cosmic sense).

- H5315 (נֶפֶשׁ, nephesh): "soul" in L. Contextually in M/T:
  * 28:17 = person's life; rendered "guilt" / "person's blood-guilt" in context.
  * 29:24 = reflexive (hates his own soul) — "himself" in M/T.
  * 29:25 = hated by; "his life at risk" in M.

- H6588 (פֶּשַׁע, pesha'): "transgression" in L; "transgression" or "sin" in M/T per context.

- H1800 (דַּל) / H7326 (רוּשׁ): both rendered "poor" — contextually same referent in these
  chapters. No distinction forced.

- Antithetical couplet structure (chs 28–29): Maintained rigorously. Every L preserves the
  Hebrew structure. Every M reads as one complete English sentence. T expands the contrast
  without flattening it.

- Chapter 30 genre: Agur's words (vv 1–9) are a distinct wisdom form — radical confession of
  ignorance followed by a two-part petition. The numerical sayings (vv 15b–33) are a separate
  genre: X/X+1 lists cataloguing four exemplars of a type. L/M preserve list structure. T
  unpacks the theological or observational point each list is making.

- 30:1 textual note: "Ithiel" and "Ucal" follow the Hebrew MT as proper names of recipients.
  An alternative reading treats them as phrases ("I am weary, O God / I can prevail") based
  on re-division of consonants (followed by some modern scholars). L/M follow MT names; T
  acknowledges the posture of the speech.

- 30:31 textual note: H4975 (מֹתְנַיִם) literally "loins" — the creature intended is
  uncertain; KJV "greyhound," some moderns "strutting rooster" or "war-horse." Rendered
  "strutting rooster" in M/T as the most linguistically supported modern reading.

- Gnomic aspect: Hebrew imperfect/participle throughout rendered as simple present or future;
  timeless observation is the register in both ch 28–29 and the numerical sayings of ch 30.

- H2617 (חֶסֶד, hesed): does not appear directly in chs 28–30.
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
  "28": {
    "1": {
      "L": "The wicked flee when no man pursueth, but the righteous are as bold as a lion.",
      "M": "The wicked flee when no one pursues, but the righteous are as bold as a young lion.",
      "T": "The guilty run without reason — the very silence feels like pursuit. But the righteous have nothing to fear; they stand as calm and unshakeable as a lion."
    },
    "2": {
      "L": "For the transgression of a land many are its princes, but by a man of understanding and knowledge the state thereof shall be prolonged.",
      "M": "When a land is in transgression, it has many rulers; but through a man of understanding and knowledge its stability endures.",
      "T": "A sinful nation churns through rulers — the instability at the top mirrors the corruption below. But a leader with real wisdom and discernment can hold a nation together."
    },
    "3": {
      "L": "A poor man that oppresseth the poor is like a sweeping rain which leaveth no food.",
      "M": "A poor man who oppresses the poor is like a sweeping rain that leaves no food.",
      "T": "A poor person who exploits others who are poor is as destructive as a violent storm that sweeps everything away and leaves nothing to eat. There is no more bitter betrayal than this."
    },
    "4": {
      "L": "They that forsake the law praise the wicked, but such as keep the law contend with them.",
      "M": "Those who forsake the law praise the wicked, but those who keep the law contend with them.",
      "T": "When people abandon God's instruction, they end up applauding what is evil — their moral compass inverts. Those who hold to the law see clearly enough to push back."
    },
    "5": {
      "L": "Evil men understand not judgment, but they that seek the LORD understand all things.",
      "M": "Evil men do not understand justice, but those who seek the LORD understand it fully.",
      "T": "The wicked cannot perceive justice because they do not want to — their eyes are not aimed at it. Those who seek the LORD find their whole understanding illuminated."
    },
    "6": {
      "L": "Better is the poor that walketh in his uprightness than he that is perverse in his ways, though he be rich.",
      "M": "Better is the poor man who walks in his integrity than the one who is perverse in his ways, even if he is rich.",
      "T": "Poverty with integrity beats wealth with corruption — every time. The rich man whose ways are twisted has purchased his position at too high a price."
    },
    "7": {
      "L": "Whoso keepeth the law is a wise son, but he that is a companion of riotous men shameth his father.",
      "M": "Whoever keeps the law is a wise son, but a companion of gluttons brings shame on his father.",
      "T": "A son who holds to wisdom and God's instruction honors his father. The son who runs with those who devour everything carelessly shames the man who raised him."
    },
    "8": {
      "L": "He that by usury and unjust gain increaseth his substance, he shall gather it for him that will pity the poor.",
      "M": "Whoever increases wealth by interest and dishonest gain gathers it for one who will be generous to the poor.",
      "T": "Wealth accumulated through exploitative interest is not really yours — you are holding it temporarily for the generous person who will eventually redistribute it to the poor. The LORD sees to this."
    },
    "9": {
      "L": "He that turneth away his ear from hearing the law, even his prayer shall be abomination.",
      "M": "Whoever turns his ear away from the law — even his prayer is detestable.",
      "T": "When a person deliberately refuses to hear God's instruction, the prayer that same mouth offers becomes repugnant to God. You cannot close your ears to his word and expect him to hear your words."
    },
    "10": {
      "L": "Whoso causeth the righteous to go astray in an evil way, he shall fall himself into his own pit; but the upright shall have good things in possession.",
      "M": "Whoever leads the righteous astray will fall into his own pit, but the blameless will receive a good inheritance.",
      "T": "The trap you lay for someone whose path is straight will become your own trap. You will fall into it. The blameless, meanwhile, will inherit what is good — because they were walking toward it all along."
    },
    "11": {
      "L": "The rich man is wise in his own eyes, but the poor that hath understanding searcheth him out.",
      "M": "A rich man is wise in his own eyes, but a poor man with understanding sees right through him.",
      "T": "The rich man's self-confidence about his own wisdom is an illusion. The poor man who has real discernment can read him immediately — and what he finds does not confirm the rich man's opinion of himself."
    },
    "12": {
      "L": "When righteous men do rejoice, there is great glory; but when the wicked rise, a man is hidden.",
      "M": "When the righteous triumph, there is great rejoicing, but when the wicked rise to power, people go into hiding.",
      "T": "When the righteous are winning, it is cause for celebration — things are as they should be. When the wicked gain the upper hand, people vanish. Power in the wrong hands empties the public square."
    },
    "13": {
      "L": "He that covereth his sins shall not prosper, but whoso confesseth and forsaketh them shall have mercy.",
      "M": "Whoever conceals his sins will not prosper, but whoever confesses and forsakes them will find mercy.",
      "T": "Covering up sin does not make it go away — it blocks the way forward. The only path that leads somewhere is confession plus forsaking: naming the thing and turning away from it. That is the road to mercy."
    },
    "14": {
      "L": "Happy is the man that feareth alway, but he that hardeneth his heart shall fall into mischief.",
      "M": "Happy is the one who fears the LORD continually, but whoever hardens his heart will fall into calamity.",
      "T": "The person who maintains a healthy fear — of God, of consequences, of the weight of their choices — is actually blessed. The person who hardens their heart against all of that is walking steadily toward destruction."
    },
    "15": {
      "L": "As a roaring lion and a ranging bear, so is a wicked ruler over the poor people.",
      "M": "Like a roaring lion or a charging bear, so is a wicked ruler over a poor people.",
      "T": "A ruthless ruler preying on powerless people is what a bear looks like to its prey and what a lion sounds like to anyone who hears it — terrifying, unstoppable, and without restraint."
    },
    "16": {
      "L": "The prince that wanteth understanding is also a great oppressor, but he that hateth covetousness shall prolong his days.",
      "M": "A ruler who lacks discernment is a great oppressor, but whoever hates unjust gain will prolong his days.",
      "T": "Without wisdom, power becomes cruelty. The ruler who does not understand will default to exploitation. The ruler who despises crooked gain will rule long — integrity sustains what force cannot."
    },
    "17": {
      "L": "A man that doeth violence to the blood of any person shall flee to the pit; let no man stay him.",
      "M": "A man burdened with the guilt of another's blood will flee to the pit; let no one help him.",
      "T": "The blood of an innocent person weighs its killer down and will drive them eventually into the pit they cannot escape. No one should try to stop that end. Let justice run its course."
    },
    "18": {
      "L": "Whoso walketh uprightly shall be saved, but he that is perverse in his ways shall fall at once.",
      "M": "Whoever walks with integrity will be saved, but the one who is crooked in his ways will fall suddenly.",
      "T": "The path of integrity leads to being saved. The twisted path leads suddenly — without warning — to a fall. You may not see it coming, but the crooked path has its own end."
    },
    "19": {
      "L": "He that tilleth his land shall have plenty of bread, but he that followeth after vain persons shall have poverty enough.",
      "M": "Whoever works his land will have plenty of bread, but whoever chases empty pursuits will have plenty of poverty.",
      "T": "Honest labor on real ground produces real food. Chasing after worthless things — people, schemes, fantasies — produces real poverty. The harvest always matches the work."
    },
    "20": {
      "L": "A faithful man shall abound with blessings, but he that maketh haste to be rich shall not be innocent.",
      "M": "A faithful man will abound with blessings, but whoever is eager to get rich quickly will not go unpunished.",
      "T": "Faithfulness — steady, reliable, trustworthy in the long run — leads to an abundance of blessing. But the person who is always looking for the shortcut to wealth will pay for it."
    },
    "21": {
      "L": "To have respect of persons is not good; for for a piece of bread that man will transgress.",
      "M": "To show partiality is not good, yet for a mere piece of bread a man will commit a wrong.",
      "T": "Favoritism corrupts justice. But the observation here is even grimmer: people will sell their integrity for almost nothing — a scrap of bread. Corruption does not require large bribes."
    },
    "22": {
      "L": "He that hasteth to be rich hath an evil eye, and considereth not that poverty shall come upon him.",
      "M": "A man who is eager to get rich has a greedy eye and does not realize that poverty is coming for him.",
      "T": "The miser's eye is always calculating — fixed on getting, never giving. What he cannot see is that the same greed driving him toward wealth is quietly driving him toward poverty. He does not see it coming."
    },
    "23": {
      "L": "He that rebuketh a man afterwards shall find more favour than he that flattereth with the tongue.",
      "M": "Whoever rebukes a person will afterward find more favor than the one who flatters with the tongue.",
      "T": "The person who tells you the hard truth earns more genuine goodwill than the flatterer ever can. Flattery feels good in the moment but leaves nothing behind. Honest rebuke, received, builds actual trust."
    },
    "24": {
      "L": "Whoso robbeth his father or his mother, and saith, It is no transgression; the same is the companion of a destroyer.",
      "M": "Whoever robs his father or mother and says 'There is nothing wrong with it' is a partner to a man who destroys.",
      "T": "Stealing from your own parents is bad enough. But the person who does it and feels no guilt — who says out loud 'There is nothing wrong with this' — has already joined themselves to those who wreck everything they touch."
    },
    "25": {
      "L": "He that is of a proud heart stirreth up strife, but he that putteth his trust in the LORD shall be made fat.",
      "M": "A greedy person stirs up strife, but whoever trusts in the LORD will prosper.",
      "T": "The person who is always grasping — whose soul feels permanently empty and keeps stirring up conflict trying to fill itself — is its own worst enemy. Trusting the LORD, by contrast, is the path to genuine flourishing."
    },
    "26": {
      "L": "He that trusteth in his own heart is a fool; but whoso walketh wisely, he shall be delivered.",
      "M": "Whoever trusts his own heart is a fool, but whoever walks in wisdom will be kept safe.",
      "T": "Self-trust — relying on your own judgment and instincts as though your heart were reliable — is the definition of foolishness. Walking in wisdom is something else entirely: it knows better than to trust itself."
    },
    "27": {
      "L": "He that giveth unto the poor shall not lack, but he that hideth his eyes shall have many a curse.",
      "M": "Whoever gives to the poor will not lack, but whoever hides his eyes from them will get many curses.",
      "T": "Give to the poor and you will not go without — generosity carries its own provision. Turn your eyes away, pretend not to see the need, and you accumulate curses instead of blessings."
    },
    "28": {
      "L": "When the wicked rise, men hide themselves; but when they perish, the righteous increase.",
      "M": "When the wicked rise to power, people go into hiding; but when the wicked perish, the righteous multiply.",
      "T": "The health of a society can be measured by where people are: in hiding, or in the open. When the wicked rule, people disappear. When wickedness is removed, the righteous come out and grow."
    }
  },
  "29": {
    "1": {
      "L": "He that being often reproved hardeneth his neck shall suddenly be destroyed, and that without remedy.",
      "M": "A man who is often reproved but stiffens his neck will suddenly be broken beyond remedy.",
      "T": "There are people who receive correction again and again and refuse every time to change. One day the breaking comes — sudden, total, with no path back. The repeated warning was the mercy; its end is the reckoning."
    },
    "2": {
      "L": "When the righteous are in authority, the people rejoice; but when the wicked beareth rule, the people mourn.",
      "M": "When the righteous are in authority, the people rejoice; when the wicked rule, the people groan.",
      "T": "The condition of the people reflects the character of their rulers. Righteous leadership produces public joy. Wicked leadership produces public grief. This is not a political observation; it is a theological one."
    },
    "3": {
      "L": "Whoso loveth wisdom rejoiceth his father, but he that keepeth company with harlots spendeth his substance.",
      "M": "Whoever loves wisdom brings his father joy, but a companion of prostitutes wastes his wealth.",
      "T": "A son who genuinely loves wisdom is a gift to his father. A son who runs with prostitutes will have no wealth left — and will have given his father grief instead of joy."
    },
    "4": {
      "L": "The king by judgment establisheth the land, but he that receiveth gifts overthroweth it.",
      "M": "A king establishes the land through justice, but one who accepts bribes tears it down.",
      "T": "Justice from the top builds a stable country. A king who takes bribes dismantles it — one corrupt decision at a time — until the whole structure has been quietly destroyed."
    },
    "5": {
      "L": "A man that flattereth his neighbour spreadeth a net for his feet.",
      "M": "A man who flatters his neighbor spreads a net for his feet.",
      "T": "Flattery is not kindness — it is a trap. The person who tells you only what you want to hear is not building you up; they are setting a snare beneath your next step."
    },
    "6": {
      "L": "In the transgression of an evil man there is a snare, but the righteous doth sing and rejoice.",
      "M": "In the transgression of an evil man there is a snare, but the righteous sing and rejoice.",
      "T": "The evil person's own wrongdoing becomes the trap they fall into — every sin carries the mechanism of its own consequence. The righteous, who carry no such hidden snares, simply sing."
    },
    "7": {
      "L": "The righteous considereth the cause of the poor, but the wicked regardeth not to know it.",
      "M": "The righteous man considers the cause of the poor; the wicked man does not care to understand it.",
      "T": "The righteous person has developed an instinct for justice that extends to those with no power to advocate for themselves. The wicked person does not merely fail to act — they choose not to understand, because understanding would cost them something."
    },
    "8": {
      "L": "Scornful men bring a city into a snare, but wise men turn away wrath.",
      "M": "Scornful men inflame a city, but wise men turn away wrath.",
      "T": "Mockers are social arsonists — they inflame whatever they touch. Wise people do the opposite: they de-escalate, absorb tension, and redirect anger before it burns everything down."
    },
    "9": {
      "L": "If a wise man contendeth with a foolish man, whether he rage or laugh, there is no rest.",
      "M": "If a wise man goes to court with a fool, the fool only rages and laughs, and there is no quiet.",
      "T": "Engaging a fool in serious argument is an exercise in futility. They alternate between explosive anger and ridicule — and there is no resolution, no rest. The wise person cannot reason with someone who has no interest in reason."
    },
    "10": {
      "L": "The bloodthirsty hate the upright, but the just seek his soul.",
      "M": "Bloodthirsty men hate the upright, but the righteous seek to protect his life.",
      "T": "Those who have blood on their hands despise the blameless — the righteous person's existence is an implicit rebuke to them. The righteous, by contrast, work to protect the innocent rather than destroy them."
    },
    "11": {
      "L": "A fool uttereth all his spirit, but a wise man keepeth it in till afterwards.",
      "M": "A fool vents all his feelings, but a wise man quietly holds it back.",
      "T": "The fool's inner life comes straight out — all of it, without filter. The wise person has learned the discipline of not saying everything they feel the moment they feel it. Restraint is a form of wisdom."
    },
    "12": {
      "L": "If a ruler hearken to lies, all his servants are wicked.",
      "M": "If a ruler listens to lies, all his officials become wicked.",
      "T": "The character of those surrounding a leader reflects what that leader tolerates. A ruler who listens to false reports is inviting corruption throughout his whole administration. What he accepts in counsel, he breeds in staff."
    },
    "13": {
      "L": "The poor and the deceitful man meet together; the LORD lighteneth both their eyes.",
      "M": "The poor man and the oppressor have this in common: the LORD gives light to the eyes of both.",
      "T": "Despite every difference in power and position, the poor and their oppressor share one thing: both received their eyes from the LORD. Both are accountable to him. This is a quiet equalizer — God is watching both."
    },
    "14": {
      "L": "The king that faithfully judgeth the poor, his throne shall be established for ever.",
      "M": "A king who judges the poor with faithfulness — his throne will be established forever.",
      "T": "The test of a king's justice is not how he treats the powerful but how he treats the powerless. The king who judges the poor faithfully builds his throne on something that cannot be moved."
    },
    "15": {
      "L": "The rod and reproof give wisdom, but a child left to himself bringeth his mother to shame.",
      "M": "The rod and reproof give wisdom, but a child left to himself brings shame to his mother.",
      "T": "Discipline — both the physical correction and the verbal rebuke — is how wisdom is formed in a child. The child who is never corrected, left entirely to their own devices, becomes someone who makes their mother ashamed. Freedom from all discipline is not a gift."
    },
    "16": {
      "L": "When the wicked are multiplied, transgression increaseth, but the righteous shall see their fall.",
      "M": "When the wicked increase, transgression increases, but the righteous will see their downfall.",
      "T": "More wicked people means more wrongdoing — it multiplies along with them. But the righteous have a long enough view: they will see the day when the wicked collapse. They just may have to wait for it."
    },
    "17": {
      "L": "Correct thy son, and he shall give thee rest; yea, he shall give delight unto thy soul.",
      "M": "Discipline your son, and he will give you rest; he will give delight to your soul.",
      "T": "The son you correct now is the son who will bring you peace later. Discipline now produces rest — actual, earned, lasting rest — and the deep satisfaction of seeing someone you shaped become someone worth knowing."
    },
    "18": {
      "L": "Where there is no vision, the people perish; but he that keepeth the law, happy is he.",
      "M": "Where there is no prophetic vision, the people are unrestrained; but blessed is the one who keeps the law.",
      "T": "Without a vision from God — without the word being proclaimed — people lose any sense of limit and wander. But the person who holds to God's instruction is genuinely blessed: they have a compass even when everyone else is drifting."
    },
    "19": {
      "L": "A servant will not be corrected by words; for though he understand he will not answer.",
      "M": "A servant cannot be corrected by mere words; he understands but will not respond.",
      "T": "Words alone do not correct everyone. Some people hear, understand, and still do not change — not because they lack comprehension but because there are no real consequences. Understanding without accountability produces no response."
    },
    "20": {
      "L": "Seest thou a man that is hasty in his words? there is more hope of a fool than of him.",
      "M": "Do you see a man who is hasty in his words? There is more hope for a fool than for him.",
      "T": "The person who always speaks before they think is in a worse position than the fool — and the fool's position is already bad. At least the fool might be correctable. The quick-tongued person has already committed to their worst impulses before correction can reach them."
    },
    "21": {
      "L": "He that delicately bringeth up his servant from a child shall have him become his son at the length.",
      "M": "Whoever pampers his servant from childhood will find that in the end he has become like a son.",
      "T": "Treat your servant too softly from the start and you will find them expecting a son's privileges — and you will have yourself to blame. The relationship has been reshaped by how it was handled from the beginning."
    },
    "22": {
      "L": "An angry man stirreth up strife, and a furious man aboundeth in transgression.",
      "M": "An angry man stirs up strife, and a hot-tempered man abounds in transgression.",
      "T": "Anger is a multiplication principle. The angry person does not just suffer alone — they spread conflict. And the person whose anger runs hot will find transgression following them everywhere, because rage does not stop at one offense."
    },
    "23": {
      "L": "A man's pride shall bring him low, but honour shall uphold the humble in spirit.",
      "M": "A man's pride will bring him low, but the one who is humble in spirit will obtain honor.",
      "T": "Pride and honor travel in opposite directions. The person who thinks highly of themselves is on a descent — slow or sudden, it goes down. The person who holds themselves humbly before God and others is being lifted."
    },
    "24": {
      "L": "Whoso is partner with a thief hateth his own soul; he heareth cursing, and bewrayeth it not.",
      "M": "Whoever partners with a thief hates himself; he hears the curse but does not disclose it.",
      "T": "Partnering with a thief is self-destructive — the person who does it hates themselves without knowing it. When the curse is pronounced for those who know and say nothing, they hear it and stay silent, and the curse settles on them. Their silence is their sentence."
    },
    "25": {
      "L": "The fear of man bringeth a snare, but whoso putteth his trust in the LORD shall be safe.",
      "M": "The fear of man lays a snare, but whoever trusts in the LORD is kept safe.",
      "T": "Letting what other people think determine what you do is a trap. It enslaves you to the shifting opinions of people who have no real power over your ultimate fate. Trust the LORD instead — he is the only one high enough to stand above the snare."
    },
    "26": {
      "L": "Many seek the ruler's favour, but every man's judgment cometh from the LORD.",
      "M": "Many seek the ruler's favor, but justice for a man comes from the LORD.",
      "T": "Everyone crowds around those with power, trying to get access and secure favor. But the final word on justice belongs to the LORD — not to any ruler. Human favor is a crowded, unreliable thing."
    },
    "27": {
      "L": "An unjust man is an abomination to the just, and he that is upright in the way is abomination to the wicked.",
      "M": "An unjust man is an abomination to the righteous, and the one who walks uprightly is an abomination to the wicked.",
      "T": "The moral division between the righteous and the wicked is absolute and mutual. The righteous find the unjust man repugnant. The wicked find the upright person equally repugnant. This is not a personality conflict — it is a fundamental incompatibility of character."
    }
  },
  "30": {
    "1": {
      "L": "The words of Agur the son of Jakeh, even the prophecy: the man spake unto Ithiel, even unto Ithiel and Ucal:",
      "M": "The words of Agur son of Jakeh. The oracle. The man spoke to Ithiel, to Ithiel and Ucal:",
      "T": "These are the words of Agur son of Jakeh — a pronouncement from one who describes himself as having nothing. He speaks to Ithiel and Ucal, but what follows is a confession that belongs to everyone."
    },
    "2": {
      "L": "Surely I am more brutish than any man, and have not the understanding of a man.",
      "M": "Surely I am more brutish than any man and do not have the understanding of a human being.",
      "T": "Agur opens with radical self-deprecation: he knows nothing, he is more animal than human, he lacks the basic understanding that others seem to have. This is not false humility — it is the starting posture of real wisdom."
    },
    "3": {
      "L": "I neither learned wisdom, nor have the knowledge of the holy.",
      "M": "I have not learned wisdom, nor have I knowledge of the Holy One.",
      "T": "He has not completed the course of wisdom. More than that — he has no experiential knowledge of God. This admission is the beginning of real wisdom. You cannot fill a cup that believes it is already full."
    },
    "4": {
      "L": "Who hath ascended up into heaven, or descended? who hath gathered the wind in his fists? who hath bound the waters in a garment? who hath established all the ends of the earth? what is his name, and what is his son's name, if thou canst tell?",
      "M": "Who has ascended to heaven and come back down? Who has gathered the wind in his fists? Who has wrapped up the waters in a garment? Who has established all the ends of the earth? What is his name, and what is his son's name — surely you know?",
      "T": "A cascade of unanswerable cosmic questions: who has navigated between heaven and earth? Who controls the wind and waters? Who shaped the whole world? These are not trivia — they are the backdrop against which human wisdom is shown to be tiny. And the question about the son's name carries a mystery the reader feels without being able to answer."
    },
    "5": {
      "L": "Every word of God is pure; he is a shield unto them that put their trust in him.",
      "M": "Every word of God proves true; he is a shield to those who take refuge in him.",
      "T": "After the confession of ignorance, this is the pivot: there is one reliable source of knowledge — God's word. It does not mislead. And the God who speaks it is also a protector for those who shelter in him."
    },
    "6": {
      "L": "Add thou not unto his words, lest he reprove thee, and thou be found a liar.",
      "M": "Do not add to his words, lest he rebuke you and you be found a liar.",
      "T": "What God has said is sufficient — do not supplement it. Adding to divine speech is not creative interpretation; it is a form of lying. And the rebuke that follows is correction from the one who knows what he actually said."
    },
    "7": {
      "L": "Two things have I required of thee; deny me them not before I die:",
      "M": "Two things I ask of you; do not deny them to me before I die:",
      "T": "The sage makes two requests — not demands, not elaborate schemes. Two things. He makes them before he dies, because he knows his time is limited and these two things matter most."
    },
    "8": {
      "L": "Remove far from me vanity and lies; give me neither poverty nor riches; feed me with food convenient for me:",
      "M": "Keep falsehood and lies far from me; give me neither poverty nor riches — feed me with just what I need,",
      "T": "The first request: keep dishonesty at a distance — both the falsehood in speech and the self-deception of vanity. The second: not poverty, not riches — just enough. The middle path of sufficiency."
    },
    "9": {
      "L": "Lest I be full and deny thee, and say, Who is the LORD? or lest I be poor, and steal, and take the name of my God in vain.",
      "M": "lest I be full and deny you, saying 'Who is the LORD?' — or lest I be poor and steal and profane the name of my God.",
      "T": "The danger of wealth: when you have enough, you forget you need God and begin to question whether he exists or matters. The danger of poverty: desperation drives you to steal and dishonor the God you claimed. Both extremes are spiritual traps. The middle ground is safer."
    },
    "10": {
      "L": "Accuse not a servant unto his master, lest he curse thee, and thou be found guilty.",
      "M": "Do not slander a servant to his master, lest he curse you and you be found guilty.",
      "T": "Do not carry tales about a servant to their employer — the servant has no one to defend them, and the wrong you do to the defenseless falls back on you. The curse of the powerless is not a small thing."
    },
    "11": {
      "L": "There is a generation that curseth their father, and doth not bless their mother.",
      "M": "There is a generation that curses its father and does not bless its mother.",
      "T": "Agur now catalogs types of people. First: those who invert the honor they owe their parents. They curse the father who shaped them. They withhold even basic blessing from their mother."
    },
    "12": {
      "L": "There is a generation that are pure in their own eyes, and yet is not washed from their filthiness.",
      "M": "There is a generation that is pure in its own eyes but has not been washed from its filth.",
      "T": "A generation of self-righteous people who have never confronted what is actually wrong with them. They see themselves as clean. They are not. Their vision is simply too self-congratulatory to see the filth."
    },
    "13": {
      "L": "There is a generation, O how lofty are their eyes! and their eyelids are lifted up.",
      "M": "There is a generation — how lofty are their eyes, how high their eyelids are lifted!",
      "T": "The prideful look is catalogued: eyes that look down on everyone else, eyelids raised in permanent condescension. They carry their arrogance in their very gaze."
    },
    "14": {
      "L": "There is a generation, whose teeth are as swords, and their jaw teeth as knives, to devour the poor from off the earth, and the needy from among men.",
      "M": "There is a generation whose teeth are swords and whose fangs are knives — to devour the poor from the earth and the needy from among mankind.",
      "T": "The predatory generation: those who consume the vulnerable with the same efficiency that weapons cut. The poor and the needy are their food. This is an accusation about how whole societies can be organized around exploitation."
    },
    "15": {
      "L": "The horseleach hath two daughters, crying, Give, give. There are three things that are never satisfied, yea, four things say not, It is enough:",
      "M": "The leech has two daughters: 'Give' and 'Give.' Three things are never satisfied; four never say 'Enough':",
      "T": "The leech — ancient symbol of insatiable appetite — has two daughters and they are both named 'Give.' This opens the numerical sayings: three things, four things, that never reach saturation. Appetite without end is the theme."
    },
    "16": {
      "L": "The grave; and the barren womb; the earth that is not filled with water; and the fire that saith not, It is enough.",
      "M": "Sheol, the barren womb, the earth that is never satisfied with water, and the fire that never says 'Enough.'",
      "T": "Four bottomless things: the realm of the dead — it never stops receiving. The childless womb — longing without end. The dry earth that drinks and always needs more. Fire — consuming, never full. These are the images of insatiability."
    },
    "17": {
      "L": "The eye that mocketh at his father, and despiseth to obey his mother, the ravens of the valley shall pick it out, and the young eagles shall eat it.",
      "M": "The eye that mocks a father and scorns to obey a mother will be picked out by the ravens of the valley and eaten by the young eagles.",
      "T": "The mocking eye — the eye that looks at parents with contempt — will end up exposed in a valley, picked clean by ravens and eagles. The proud gaze that would not honor its parents will have no honorable burial, just birds. This is poetic justice."
    },
    "18": {
      "L": "There be three things which are too wonderful for me, yea, four which I know not:",
      "M": "Three things are too wonderful for me; four I do not understand:",
      "T": "Another numerical group — this time about mystery. Not mystery as ignorance but as wonder: these four things are beyond full explanation, and Agur is honest enough to say so."
    },
    "19": {
      "L": "The way of an eagle in the air; the way of a serpent upon a rock; the way of a ship in the midst of the sea; and the way of a man with a maid.",
      "M": "the way of an eagle in the sky, the way of a serpent on a rock, the way of a ship in the heart of the sea, and the way of a man with a young woman.",
      "T": "Four things that leave no trace but are unmistakable in motion: the eagle's flight, the serpent's glide, the ship's passage through open water, and the way a man moves toward a woman. All four are fluid, purposeful, and finally mysterious."
    },
    "20": {
      "L": "Such is the way of an adulterous woman; she eateth, and wipeth her mouth, and saith, I have done no wickedness.",
      "M": "Such is the way of an adulteress: she eats and wipes her mouth and says, 'I have done nothing wrong.'",
      "T": "The contrast with vv 18–19: where those four ways carry wonder, the adulteress's way also leaves no trace — but by design. She finishes what she does, wipes her mouth, and declares herself innocent. The ease of her denial is itself the horror."
    },
    "21": {
      "L": "For three things the earth is disquieted, and for four which it cannot bear:",
      "M": "Under three things the earth trembles; under four it cannot bear up:",
      "T": "Another group of four — but now things so wrong that the earth itself is disturbed. The cosmos is not indifferent to social disorder."
    },
    "22": {
      "L": "For a servant when he reigneth; and a fool when he is filled with meat;",
      "M": "a servant when he reigns, and a fool when he is full of food,",
      "T": "First: the servant who has come to power. Second: the fool who has a full stomach. Both are problems — the first because authority requires a different formation than servitude; the second because a satiated fool becomes insufferable."
    },
    "23": {
      "L": "For an odious woman when she is married; and an handmaid that is heir to her mistress.",
      "M": "an unloved woman when she gets a husband, and a maidservant who displaces her mistress.",
      "T": "Third: the woman who was overlooked and knows it — once she gets what she wanted, the bitterness is barely concealed. Fourth: the servant girl who has risen to take her mistress's place. Each is a social inversion that strains the fabric."
    },
    "24": {
      "L": "There be four things which are little upon the earth, but they are exceeding wise:",
      "M": "Four things on earth are small, but they are exceedingly wise:",
      "T": "A reversal: after the four things that cannot be borne, four that are tiny but wise. Small is not the same as weak; smallness can contain surprising intelligence."
    },
    "25": {
      "L": "The ants are a people not strong, yet they prepare their meat in the summer;",
      "M": "the ants are a people not strong, yet they prepare their food in the summer;",
      "T": "The ant: tiny, vulnerable, physically weak. But they plan ahead, they work in the season for working, and when winter comes they have food. Wisdom here is foresight without strength."
    },
    "26": {
      "L": "The conies are but a feeble folk, yet make they their houses in the rocks;",
      "M": "the rock badgers are a feeble people, yet they make their homes in the cliffs;",
      "T": "The rock badger: small and soft, not built for fighting. But they have the wisdom to find shelter in stone. What they lack in strength they make up in judgment about where to live."
    },
    "27": {
      "L": "The locusts have no king, yet go they forth all of them by bands;",
      "M": "the locusts have no king, yet all of them march out in formation;",
      "T": "Locusts have no commander, no hierarchy — and yet they move in perfect coordination. There is wisdom in how they organize themselves without needing to be organized. A rebuke, perhaps, to human dependence on hierarchy alone."
    },
    "28": {
      "L": "The spider taketh hold with her hands, and is in kings' palaces.",
      "M": "the lizard you can take in your hands, yet it is found in kings' palaces.",
      "T": "The lizard — easily caught, utterly unheroic — climbs to the highest rooms. It gets into places that armies cannot. Persistence and access are a form of achievement that strength cannot replicate."
    },
    "29": {
      "L": "There be three things which go well, yea, four are comely in going:",
      "M": "Three things are majestic in their stride; four are stately in their going:",
      "T": "Another set of four, this time about dignity of movement — things that are worth watching when they walk or go."
    },
    "30": {
      "L": "A lion which is strongest among beasts, and turneth not away for any;",
      "M": "the lion, which is mightiest among beasts and does not turn back before any;",
      "T": "The lion moves without hesitation — it does not recalculate or back away. Its power is matched by an unhurried, unstoppable gait. Dignity here is courage made visible in motion."
    },
    "31": {
      "L": "A greyhound; an he goat also; and a king, against whom there is no rising up.",
      "M": "a strutting rooster, a he-goat, and a king with his army arrayed before him.",
      "T": "The rooster, the he-goat, and the king flanked by those who march for him — three images of visible authority and confidence. Each moves in a way that announces its own power."
    },
    "32": {
      "L": "If thou hast done foolishly in lifting up thyself, or if thou hast thought evil, lay thine hand upon thy mouth.",
      "M": "If you have been foolish, exalting yourself, or if you have devised evil, put your hand over your mouth.",
      "T": "Two warnings at the close: if you have made yourself look bigger than you are, stop talking. If you have been plotting harm, stop talking. The hand over the mouth is the gesture of someone who has realized they need to be quiet."
    },
    "33": {
      "L": "Surely the churning of milk bringeth forth butter, and the wringing of the nose bringeth forth blood: so the forcing of wrath bringeth forth strife.",
      "M": "For as pressing milk produces curds and pressing the nose produces blood, so pressing anger produces strife.",
      "T": "The conclusion: cause and effect is inexorable. You press milk, you get curds. You press the nose, you get blood. You press human anger — keep provoking it, keep stirring it — and you get strife. Every time. No exceptions."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 28–30 written.')

if __name__ == '__main__':
    main()
