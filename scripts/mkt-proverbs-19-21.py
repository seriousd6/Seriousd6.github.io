"""
MKT Proverbs chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-19-21.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" in L/M; "the LORD" in T — consistent with chs. 1–18.

- H2617 (חֶסֶד, hesed): Rendered contextually:
  * 19:22 = "kindness/faithful love" — the quality that makes a person truly desirable;
    L: "kindness", M: "faithful love", T: "faithfulness shown in consistent kindness"
  * 20:28 = "steadfast love/mercy" — the pillar of kingship;
    L: "mercy", M: "steadfast love", T: "mercy and faithfulness"

- H5315 (נֶפֶשׁ, nephesh):
  * 19:2 = "soul" (desire — wanting without knowledge); L: "soul", M: "desire", T: "enthusiasm"
  * 19:15 = "soul" (idle soul goes hungry); L: "soul", M: "person", T: implied
  * 21:10 = "soul" (the wicked desire evil); L: "soul", M: "desire of the wicked", T: "appetite"

- H7307 (רוּחַ, ruach):
  * 20:27 = "spirit" (human spirit as lamp of the LORD) — clearly personal spirit, not wind/breath

- H8441 (תּוֹעֲבַת, to'evah): "abomination" in L; "detestable" in M; "abomination" in T — consistent with chs. 10–18.

- Antithetical couplet structure: Chapters 19–21 mix antithetical couplets (A, but B) with
  synonymous parallelism and occasional triplets. L/M faithfully preserve each structure.
  T may expand contrast or complete a thought, but maintains every verse's full semantic field.

- Gnomic aspect: Hebrew imperfect/participle used for timeless statements rendered as simple
  present or future in English throughout.

- Proverbs 19:5 and 19:9 are deliberate doublets (false witness). v5 says "shall not escape";
  v9 escalates to "shall perish." T tier notes the escalation between them.

- Proverbs 20:9 ("Who can say I have made my heart pure"): Rhetorical question expecting
  no answer. T tier holds the rhetorical weight — no one can. This touches on universal
  sinfulness without making it didactic.

- Proverbs 20:23 deliberately repeats 20:10 (unequal weights). Both are included fully —
  repetition in Proverbs is a rhetorical device for emphasis, not an error.

- Proverbs 21:3 ("more acceptable than sacrifice"): A recurrent prophetic-wisdom theme
  (cf. 1 Sam 15:22, Hos 6:6, Mic 6:6–8). T tier notes its depth without anachronism.

- Proverbs 21:12 ("The righteous man"): Hebrew צַדִּיק (tsaddiq) here may refer to God
  as the truly Righteous One. The verse's second clause explicitly attributes overthrow of
  the wicked to God. L/M render "The righteous" (ambiguous); T follows the interpretation
  that God is the agent.

- H191 (אֱוִיל) vs H3684 (כְּסִיל): Both rendered "fool" in L/M. T distinguishes where context
  allows — 'evil is the morally corrupt fool; kesil is the stubborn complacent fool.
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
  "19": {
    "1": {
      "L": "Better is the poor who walketh in his integrity than he who is perverse in his lips and is a fool.",
      "M": "Better is a poor man who walks in his integrity than one who is crooked in speech and is a fool.",
      "T": "Poverty paired with integrity is worth more than wealth paired with a crooked tongue. The fool who twists his words has bought his standing at too high a price."
    },
    "2": {
      "L": "Also, that the soul be without knowledge is not good; and he that hasteth with his feet sinneth.",
      "M": "Desire without knowledge is not good, and the one who moves too fast misses the way.",
      "T": "Enthusiasm without understanding is a recipe for failure. The person who acts before they think does not just slow themselves down — they sin against the path they should have taken."
    },
    "3": {
      "L": "The foolishness of man perverteth his way, and his heart fretteth against the LORD.",
      "M": "A man's own foolishness leads his way astray, yet his heart rages against the LORD.",
      "T": "When a person's own choices wreck their life, they blame God for it. Foolishness corrupts the path — but the angry heart points upward. This is one of the most honest observations in Proverbs."
    },
    "4": {
      "L": "Wealth maketh many friends, but the poor is separated from his neighbour.",
      "M": "Wealth attracts many friends, but the poor man is separated from his neighbor.",
      "T": "Money is magnetic — it draws people. Poverty does the opposite. The poor man finds himself increasingly alone — not because of who he is, but because of what he has."
    },
    "5": {
      "L": "A false witness shall not go unpunished, and he that speaketh lies shall not escape.",
      "M": "A false witness will not go unpunished, and whoever speaks lies will not escape.",
      "T": "The false witness will be held to account — eventually, in some way, there is no escape. Lies have a way of catching up to the one who breathes them out."
    },
    "6": {
      "L": "Many will intreat the favour of the prince, and every man is a friend to him that giveth gifts.",
      "M": "Many seek the favor of a generous man, and everyone is a friend to the one who gives gifts.",
      "T": "Generosity creates a crowd. It attracts friends the way bread attracts birds. The more interesting question is whether those friends would stay if the giving stopped."
    },
    "7": {
      "L": "All the brethren of the poor do hate him; how much more do his friends go far from him! He pursueth them with words, yet they are wanting.",
      "M": "All the brothers of a poor man hate him — how much more do his friends keep their distance. He may call after them, but they are gone.",
      "T": "The poor man's own family abandons him. Friends — who are even more optional — go further still. He calls out, he pleads, he chases them with words. And they are simply not there. Poverty is a kind of exile."
    },
    "8": {
      "L": "He that getteth wisdom loveth his own soul; he that keepeth understanding shall find good.",
      "M": "Whoever acquires wisdom loves himself; whoever holds to understanding will find what is good.",
      "T": "Growing in wisdom is the deepest form of self-care. The person who holds onto understanding is not just being clever — they are securing their own future good."
    },
    "9": {
      "L": "A false witness shall not go unpunished, and he that speaketh lies shall perish.",
      "M": "A false witness will not go unpunished, and whoever breathes out lies will perish.",
      "T": "The stakes escalate from v5: not just that the liar will not escape, but that they will perish. Lies do not merely catch up with you — they kill you. The false witness ends in destruction."
    },
    "10": {
      "L": "Luxury is not seemly for a fool, much less for a servant to have rule over princes.",
      "M": "Luxury does not suit a fool, and it is even worse for a slave to rule over princes.",
      "T": "Some things are out of place — not by malice but by nature. A fool living in luxury is one kind of disorder. A servant commanding princes is another, worse kind. Both upset the order that makes life workable."
    },
    "11": {
      "L": "The discretion of a man deferreth his anger, and it is his glory to pass over a transgression.",
      "M": "A man's wisdom makes him slow to anger, and it is his glory to overlook an offense.",
      "T": "Real wisdom shows up in how a person handles an insult. The wise man does not rush to anger — and his greatest honor is not in demanding justice but in choosing to let an offense go."
    },
    "12": {
      "L": "The king's wrath is as the roaring of a lion, but his favour is as dew upon the grass.",
      "M": "A king's wrath is like the roaring of a lion, but his favor is like dew upon the grass.",
      "T": "The king's anger is terrifying — you hear it before it arrives, and there is nowhere to run. His goodwill, by contrast, is gentle and life-giving, like morning dew that appears without warning and refreshes everything."
    },
    "13": {
      "L": "A foolish son is the calamity of his father, and the contentions of a wife are a continual dropping.",
      "M": "A foolish son is ruin to his father, and a wife's quarreling is like a constant drip.",
      "T": "A son who turns out foolish is catastrophe enough to call your whole life into question. A contentious wife is a different kind of disaster — less dramatic but relentless, like water dripping through a roof that cannot be stopped."
    },
    "14": {
      "L": "House and riches are the inheritance of fathers, but a prudent wife is from the LORD.",
      "M": "A house and wealth can be inherited from one's father, but a sensible wife comes from the LORD.",
      "T": "You can inherit a house. You can inherit wealth. But a wife of genuine wisdom and good character is not something anyone can hand you — she is a gift that only the LORD gives."
    },
    "15": {
      "L": "Slothfulness casteth into a deep sleep, and an idle soul shall suffer hunger.",
      "M": "Laziness brings on a deep sleep, and the idle person will go hungry.",
      "T": "Laziness has a gravity of its own — it pulls the lazy person deeper into inertia, deeper into sleep, until they are just barely awake enough to notice that they have nothing to eat."
    },
    "16": {
      "L": "He that keepeth the commandment keepeth his own soul, but he that despiseth his ways shall die.",
      "M": "Whoever keeps the commandment keeps his life, but whoever is careless about his conduct will die.",
      "T": "Obedience is a life-preserving act. To despise the LORD's ways — to treat your own conduct as a matter of indifference — is to walk toward death without knowing it."
    },
    "17": {
      "L": "He that hath pity upon the poor lendeth unto the LORD, and his good deed will he pay him again.",
      "M": "Whoever is kind to the poor lends to the LORD, and he will repay him for his deed.",
      "T": "To give to a poor person is to make the LORD your debtor — and he is the best creditor there is. What you extend in mercy to the poor, he registers as a loan and repays."
    },
    "18": {
      "L": "Chasten thy son while there is hope, and let not thy soul spare for his crying.",
      "M": "Discipline your son while there is still hope; do not indulge him to the point of his destruction.",
      "T": "Correct your child while correction can still make a difference — while there is still hope. Indulging him now, refusing discipline because the crying is painful in the moment, is how you lose him later."
    },
    "19": {
      "L": "A man of great wrath shall suffer punishment; for if thou deliver him, yet thou must do it again.",
      "M": "A man of great wrath will bear the penalty; if you rescue him, you will only have to do it again.",
      "T": "The chronically angry man keeps ending up in the consequences of his anger. If you bail him out, you have only reset the cycle — you will be doing it again. Some consequences need to be allowed to do their work."
    },
    "20": {
      "L": "Hear counsel and receive instruction, that thou mayest be wise in thy latter end.",
      "M": "Listen to counsel and accept instruction, that you may gain wisdom in the end.",
      "T": "Take in counsel now. Accept correction now. The wisdom that results is not just for today — it is for the long view, for the person you will have become at the end of your days."
    },
    "21": {
      "L": "There are many devices in a man's heart, but the counsel of the LORD, that shall stand.",
      "M": "Many are the plans in a man's heart, but the LORD's purpose is what stands.",
      "T": "You can lay out as many plans as you like — the mind is fertile ground for schemes. But only what the LORD purposes actually holds. In the end, his counsel is the only one that fully survives."
    },
    "22": {
      "L": "The desire of a man is his kindness, and a poor man is better than a liar.",
      "M": "What is desired in a person is faithful love, and a poor man is better than a liar.",
      "T": "What makes a person truly worth knowing is their faithfulness — the consistent kindness that flows from genuine covenant loyalty. And poverty beats dishonesty: the poor honest man is worth more than the rich liar."
    },
    "23": {
      "L": "The fear of the LORD tendeth to life, and he that hath it shall abide satisfied; he shall not be visited with evil.",
      "M": "The fear of the LORD leads to life; whoever has it will rest satisfied and will not be touched by evil.",
      "T": "The fear of the LORD is not merely reverence — it is a path to life. The person who lives in it finds themselves genuinely satisfied — not restless, not chasing — and harm cannot reach them."
    },
    "24": {
      "L": "A slothful man hideth his hand in his bosom, and will not so much as bring it to his mouth again.",
      "M": "The sluggard buries his hand in the dish and will not even bring it to his mouth again.",
      "T": "This is satire at its sharpest: the lazy person is so inert they cannot be bothered to eat. They reach into the bowl and leave their hand there. It is a picture of paralysis so profound it crosses into absurdity."
    },
    "25": {
      "L": "Smite a scorner, and the simple will beware; and reprove one that hath understanding, and he will understand knowledge.",
      "M": "Strike a mocker and the naive will gain caution; correct a man of understanding and he gains knowledge.",
      "T": "Punishment does different things to different people. The bystander who sees a scoffer receive discipline becomes more careful. The wise person who receives direct correction gains knowledge from it. The scoffer himself — notably — is not said to learn anything."
    },
    "26": {
      "L": "He that wasteth his father and chaseth away his mother is a son that causeth shame and bringeth reproach.",
      "M": "A son who mistreats his father and drives his mother away brings shame and disgrace.",
      "T": "To ruin your father financially and to drive your mother from the house — this son has inverted everything a family is for. The shame he brings is not mere embarrassment; it is the public exposure of a profound betrayal."
    },
    "27": {
      "L": "Cease, my son, to hear the instruction that causeth to err from the words of knowledge.",
      "M": "Stop listening to instruction, my son, and you will drift from words of knowledge.",
      "T": "The moment you stop listening to instruction, you begin to drift. The warning is in the framing: this is addressed to a son who thinks he can afford to stop. He cannot. The drift is so gradual he may not notice it until he is far from what he once knew."
    },
    "28": {
      "L": "An ungodly witness scorneth judgment, and the mouth of the wicked devoureth iniquity.",
      "M": "A corrupt witness mocks justice, and the mouth of the wicked gulps down iniquity.",
      "T": "The corrupt witness has contempt for the whole system of justice — it means nothing to them. And the wicked person does not merely tolerate wrongdoing; they swallow it eagerly, whole."
    },
    "29": {
      "L": "Judgments are prepared for scorners, and stripes for the back of fools.",
      "M": "Penalties are set in store for mockers, and beatings for the backs of fools.",
      "T": "There is a penalty waiting for the mocker — it has been prepared for them. And for the fool, the rod. These are not threats; they are a description of a just world's structure."
    }
  },
  "20": {
    "1": {
      "L": "Wine is a mocker, strong drink is raging, and whosoever is deceived thereby is not wise.",
      "M": "Wine is a mocker and strong drink a brawler, and whoever is led astray by it is not wise.",
      "T": "Wine mocks its users — it promises one thing and delivers humiliation. Strong drink brawls. The person who lets themselves be mastered by either of these has quietly abandoned wisdom."
    },
    "2": {
      "L": "The fear of a king is as the roaring of a lion; whoso provoketh him to anger sinneth against his own soul.",
      "M": "The terror of a king is like the roaring of a lion; whoever provokes him to anger puts his own life at risk.",
      "T": "The king's anger is not something to trifle with — it is the roar of a predator. Provoking it is not bravery; it is self-destruction."
    },
    "3": {
      "L": "It is an honour for a man to cease from strife, but every fool will be meddling.",
      "M": "It is an honor for a man to stay out of conflict, but every fool will be drawn into quarreling.",
      "T": "Staying out of fights takes more discipline than entering them, and that restraint is a genuine form of honor. The fool, however, cannot help himself — every dispute draws him in."
    },
    "4": {
      "L": "The sluggard will not plow by reason of the cold; therefore shall he beg in harvest and have nothing.",
      "M": "The sluggard does not plow in the cold season; at harvest he will look for food and find nothing.",
      "T": "When the hard season for plowing comes, the sluggard finds a reason not to. Harvest arrives and he appears with his hand out — and finds nothing. Every harvest is the downstream result of work done in conditions that were not comfortable."
    },
    "5": {
      "L": "Counsel in the heart of a man is like deep water, but a man of understanding will draw it out.",
      "M": "The counsel in a man's heart is like deep water, but a man of understanding draws it out.",
      "T": "Real wisdom in a person is not on the surface — it is buried deep, like water that takes effort to reach. The person with genuine understanding has the skill to draw it up from where it lives."
    },
    "6": {
      "L": "Most men will proclaim every one his own goodness, but a faithful man who can find?",
      "M": "Many people proclaim their own loyalty, but a truly faithful person — who can find?",
      "T": "Everyone tells you how trustworthy they are. Almost no one actually is. A genuinely faithful person — reliable in the small things, the long things, the secret things — is genuinely rare."
    },
    "7": {
      "L": "The just man walketh in his integrity; his children are blessed after him.",
      "M": "A righteous man who walks in his integrity — blessed are his children after him.",
      "T": "The righteous person's integrity is not only their own inheritance — it becomes their children's. Walk with integrity and you leave your family something that money cannot provide and no one can take away."
    },
    "8": {
      "L": "A king that sitteth in the throne of judgment scattereth away all evil with his eyes.",
      "M": "A king who sits on the throne of judgment scatters all evil with his eyes.",
      "T": "The king who actually judges — who sits where judgment is done and does it — disperses evil with nothing more than his gaze. Accountability alone is a form of justice."
    },
    "9": {
      "L": "Who can say, I have made my heart clean, I am pure from my sin?",
      "M": "Who can say, 'I have made my heart pure; I am clean from my sin'?",
      "T": "No one. The question is rhetorical and the silence it creates is devastating. The person who claims a heart made clean by their own effort, who says they have purged their own sin — they are wrong. This is one of Proverbs' quietest and most far-reaching statements."
    },
    "10": {
      "L": "Divers weights and divers measures, both of them alike are abomination to the LORD.",
      "M": "Unequal weights and unequal measures — both are detestable to the LORD.",
      "T": "Fraudulent scales, false measures — the LORD considers these equally detestable no matter how small the deception seems. Dishonesty in commerce is dishonesty before God."
    },
    "11": {
      "L": "Even a child is known by his doings, whether his work be pure and whether it be right.",
      "M": "Even a child is known by his actions, whether his conduct is pure and right.",
      "T": "You do not need to know someone long before their character begins to show. Even children reveal themselves in what they do — and what they do tells you whether what is being formed in them is genuinely good."
    },
    "12": {
      "L": "The hearing ear and the seeing eye, the LORD hath made even both of them.",
      "M": "The hearing ear and the seeing eye — the LORD made them both.",
      "T": "Every capacity for perception — every ear that catches truth, every eye that sees clearly — is a gift from the LORD. This is not anatomy. It is a statement about accountability: what we are equipped to perceive, we are responsible for."
    },
    "13": {
      "L": "Love not sleep, lest thou come to poverty; open thine eyes, and thou shalt be satisfied with bread.",
      "M": "Do not love sleep, or you will come to poverty; keep your eyes open and you will have plenty of food.",
      "T": "Sleep is good; love of sleep is a different thing — it is avoidance wearing the mask of rest. Open your eyes to the work that needs doing, and you will eat."
    },
    "14": {
      "L": "It is naught, it is naught, saith the buyer; but when he is gone his way, then he boasteth.",
      "M": "Bad, bad, says the buyer, but when he goes away, he boasts of his deal.",
      "T": "The buyer performs disappointment to drive down the price, then walks away boasting about the bargain he just obtained. This observation is ancient and unflattering — and has not changed."
    },
    "15": {
      "L": "There is gold, and a multitude of rubies, but the lips of knowledge are a precious jewel.",
      "M": "There is gold and plenty of rubies, but the lips that speak knowledge are the truly precious thing.",
      "T": "You can point to gold, to rubies, to the most expensive things the world offers. None of them are as rare or as valuable as a person who opens their mouth and genuine wisdom comes out."
    },
    "16": {
      "L": "Take his garment that is surety for a stranger; and take a pledge of him for a strange woman.",
      "M": "Take the garment of one who puts up security for a stranger; hold it in pledge for those who are surety for foreigners.",
      "T": "If someone has been reckless enough to guarantee a stranger's debt, take collateral — because you cannot rely on the judgment of someone who takes on risks they cannot properly assess."
    },
    "17": {
      "L": "Bread of deceit is sweet to a man, but afterwards his mouth shall be filled with gravel.",
      "M": "Bread gained by deceit is sweet to a man, but afterward his mouth will be full of gravel.",
      "T": "Dishonest gain tastes sweet going in — but what follows is the sensation of gravel in your mouth. What looked like nourishment turns out to be grit."
    },
    "18": {
      "L": "Every purpose is established by counsel, and with good advice make war.",
      "M": "Plans are established by seeking advice, and with wise guidance you can wage war.",
      "T": "No plan holds without counsel. Even the most high-stakes decisions — including the decision to go to war — succeed only when grounded in wisdom gathered from others."
    },
    "19": {
      "L": "He that goeth about as a talebearer revealeth secrets; therefore meddle not with him that flattereth with his lips.",
      "M": "The gossip reveals secrets wherever he goes; avoid anyone who talks too freely.",
      "T": "The person who gossips to you about others is already gossiping about you to others. Nothing they know is safe. Do not share yourself with them."
    },
    "20": {
      "L": "Whoso curseth his father or his mother, his lamp shall be put out in obscure darkness.",
      "M": "Whoever curses his father or his mother — his lamp will be snuffed out in deepest darkness.",
      "T": "The person who turns against the ones who gave them life will find their own light extinguished — not dimmed, but put out entirely, in the darkest possible place."
    },
    "21": {
      "L": "An inheritance may be gotten hastily at the beginning, but the end thereof shall not be blessed.",
      "M": "An inheritance quickly gained at first will not be blessed in the end.",
      "T": "Money that comes too fast, too easily, by cutting corners or pressing advantages that should not be pressed — it will not hold. The blessing that makes wealth lasting is not in the speed of accumulation; it is in the integrity of how it came."
    },
    "22": {
      "L": "Say not thou, I will recompense evil; but wait on the LORD, and he shall save thee.",
      "M": "Do not say, 'I will repay evil'; wait on the LORD and he will deliver you.",
      "T": "Resist the instinct to settle scores yourself. The LORD is a more just judge than you are, and a more powerful one. Wait on him — he will handle it."
    },
    "23": {
      "L": "Divers weights are an abomination unto the LORD, and a false balance is not good.",
      "M": "Unequal weights are detestable to the LORD, and dishonest scales are no good.",
      "T": "This doubles back to v10 — a deliberate emphasis. The LORD will not let fraud in commerce go unregistered. Both the instrument of fraud (the scale) and the evidence of it (the weights) are equally offensive to him."
    },
    "24": {
      "L": "Man's goings are of the LORD; how can a man then understand his own way?",
      "M": "A man's steps are directed by the LORD; how then can anyone understand his own path?",
      "T": "The LORD guides human steps — which means no one is fully in control of their own story. This should produce humility: if the LORD steers your path, you are not in a position to fully understand where you are or where you are going."
    },
    "25": {
      "L": "It is a snare to the man who devoureth that which is holy, and after vows to make enquiry.",
      "M": "It is a snare for a man to dedicate something rashly, and only afterward to reconsider.",
      "T": "Making a vow to God before you have thought through what it costs is a trap you set for yourself. The time for counting the cost is before the vow — not after, when you are already bound."
    },
    "26": {
      "L": "A wise king scattereth the wicked, and bringeth the wheel over them.",
      "M": "A wise king scatters the wicked and drives the threshing wheel over them.",
      "T": "A king who is actually wise does not tolerate the wicked in his midst. He separates them out — like grain from chaff — and what follows is thorough."
    },
    "27": {
      "L": "The spirit of man is the lamp of the LORD, searching all the inward parts of the belly.",
      "M": "The human spirit is the LORD's lamp, searching all the innermost parts of a person.",
      "T": "The LORD uses the human spirit as his lamp to search a person from the inside out. Your own conscience, your own inner awareness — these are not yours alone. They are instruments in God's hands."
    },
    "28": {
      "L": "Mercy and truth preserve the king, and his throne is upholden by mercy.",
      "M": "Steadfast love and faithfulness preserve the king, and his throne is upheld by faithful love.",
      "T": "A king's throne stands on two pillars: mercy and faithfulness. Not military strength, not wealth — what gives a kingship its staying power is moral. This is what holds the throne up."
    },
    "29": {
      "L": "The glory of young men is their strength, and the beauty of old men is the gray head.",
      "M": "The glory of young men is their strength, but the honor of old men is their gray hair.",
      "T": "Each season of life has its own glory. The young man's strength is real and should be used. The old man's gray hair is earned — the visible record of a life sustained — and it carries a dignity of its own."
    },
    "30": {
      "L": "The blueness of a wound cleanseth away evil, and stripes the inward parts of the belly.",
      "M": "Painful blows cleanse away evil; wounds reach the innermost parts of a person.",
      "T": "Some correction only works if it cuts deep. The disciplining blow that leaves a mark is not cruelty — it is surgery. It reaches places that gentle words cannot."
    }
  },
  "21": {
    "1": {
      "L": "The king's heart is in the hand of the LORD as the rivers of water; he turneth it whithersoever he will.",
      "M": "The king's heart is in the hand of the LORD like channels of water; he directs it wherever he pleases.",
      "T": "The king who imagines himself in control of his own decisions does not understand his situation. The LORD holds his heart the way a farmer holds irrigation channels — directing the flow wherever it is needed, effortlessly."
    },
    "2": {
      "L": "Every way of a man is right in his own eyes, but the LORD pondereth the hearts.",
      "M": "Every man thinks his own way is right, but the LORD weighs the heart.",
      "T": "Self-justification is universal — everyone believes their own choices make sense. The LORD, however, is not interested in our rationalizations. He weighs what is actually there."
    },
    "3": {
      "L": "To do justice and judgment is more acceptable to the LORD than sacrifice.",
      "M": "To do righteousness and justice is more acceptable to the LORD than sacrifice.",
      "T": "The LORD does not want religion instead of integrity. Doing what is right — actually living justly in daily life — is what he prefers to any amount of ritual offering. This runs through the whole prophetic-wisdom tradition."
    },
    "4": {
      "L": "An high look, and a proud heart, and the plowing of the wicked, is sin.",
      "M": "Haughty eyes and a proud heart — even the tillage of the wicked — are sin.",
      "T": "Pride announces itself in the eyes before anywhere else. The haughty look, the lifted heart — and even the daily work of the wicked, their ordinary 'plowing' — is sin. It is sin all the way down, not just in the obvious moments."
    },
    "5": {
      "L": "The thoughts of the diligent tend only to plenteousness, but of every one that is hasty only to want.",
      "M": "The plans of the diligent lead to abundance, but hasty action leads only to poverty.",
      "T": "Diligence and patience together are the engine of real abundance. Rushing — trying to skip steps, force outcomes, get there faster — produces the opposite: want."
    },
    "6": {
      "L": "The getting of treasures by a lying tongue is a vanity tossed to and fro of them that seek death.",
      "M": "Treasures gained by a lying tongue are a fleeting vapor — a deadly snare.",
      "T": "Wealth accumulated through lies has no more substance than mist — it moves, it fades, it cannot be held. And those who chase it are chasing a trap that kills them."
    },
    "7": {
      "L": "The robbery of the wicked shall destroy them, because they refuse to do judgment.",
      "M": "The violence of the wicked will drag them away, because they refuse to do what is right.",
      "T": "The wicked destroy themselves with their own methods. They refuse justice — and the violence they inflict on others becomes the current that finally sweeps them away."
    },
    "8": {
      "L": "The way of man is froward and strange, but as for the pure, his work is right.",
      "M": "The way of the guilty person is crooked and strange, but the conduct of the pure is upright.",
      "T": "Guilt shows in how a person moves through the world — their path is crooked, full of detours and evasions. The pure person has no such complexity. They simply walk straight."
    },
    "9": {
      "L": "It is better to dwell in a corner of the housetop than with a brawling woman in a wide house.",
      "M": "It is better to live in a corner of the roof than in a spacious house with a quarrelsome woman.",
      "T": "A corner of the roof — exposed, cramped, without comfort — is still preferable to the peace-destroying presence of someone who cannot stop quarreling. The physical space means nothing if there is no peace in it."
    },
    "10": {
      "L": "The soul of the wicked desireth evil; his neighbour findeth no favour in his eyes.",
      "M": "The wicked desire evil; they show no kindness even to their neighbor.",
      "T": "The wicked person does not just stumble into sin — they want it. Evil is their appetite. And this appetite makes them indifferent to the people around them: no mercy, no favor, nothing."
    },
    "11": {
      "L": "When the scorner is punished, the simple is made wise; and when the wise is instructed, he receiveth knowledge.",
      "M": "When a mocker is punished, the naive become wise; when a wise person receives instruction, he gains knowledge.",
      "T": "Correction works differently on different people. The mocker's punishment teaches the bystander who was watching. The wise person who receives direct instruction gains even more. The mocker himself — notably — is not said to learn anything."
    },
    "12": {
      "L": "The righteous man wisely considereth the house of the wicked, but God overthroweth the wicked for their wickedness.",
      "M": "The righteous perceive the house of the wicked; God brings the wicked down to ruin.",
      "T": "The righteous person sees clearly what is happening in the wicked person's household — the whole structure of their life. And God, the truly Righteous One, brings that structure down because of their wickedness."
    },
    "13": {
      "L": "Whoso stoppeth his ears at the cry of the poor, he also shall cry himself, but shall not be heard.",
      "M": "Whoever stops his ears at the cry of the poor will himself cry out and not be heard.",
      "T": "The person who refuses to hear the poor will eventually need to be heard themselves — and find the same silence they gave. This is not mere poetry; it is the shape of a just world."
    },
    "14": {
      "L": "A gift in secret pacifieth anger, and a reward in the bosom strong wrath.",
      "M": "A secret gift calms anger, and a concealed bribe soothes fierce wrath.",
      "T": "A gift given quietly — not publicly, not in a way that humiliates — can defuse anger that nothing else could touch. This is an observation about human nature, not an endorsement of corruption."
    },
    "15": {
      "L": "It is joy to the just to do judgment, but destruction shall be to the workers of iniquity.",
      "M": "It is a joy to the righteous to do justice, but it brings terror to evildoers.",
      "T": "The same act — justice being done — produces two completely opposite responses depending on which side you stand on. The righteous welcome it as joy. For the wicked, it is the beginning of destruction."
    },
    "16": {
      "L": "The man that wandereth out of the way of understanding shall remain in the congregation of the dead.",
      "M": "Whoever wanders from the way of understanding will come to rest among the dead.",
      "T": "To leave the road of wisdom is not a neutral decision. It leads somewhere specific — to the company of the dead. This is not just metaphor for spiritual drift; it is a warning about final destination."
    },
    "17": {
      "L": "He that loveth pleasure shall be a poor man; he that loveth wine and oil shall not be rich.",
      "M": "Whoever loves pleasure will be a poor man; whoever loves wine and olive oil will not grow rich.",
      "T": "The one who organizes their life around pleasure will end up without resources. Wine, oil, luxury — making these things your organizing principle depletes rather than builds."
    },
    "18": {
      "L": "The wicked shall be a ransom for the righteous, and the transgressor for the upright.",
      "M": "The wicked are a substitute for the righteous, and the treacherous take the place of the upright.",
      "T": "There is a divine economy operating here: the wicked end up absorbing what was meant for the righteous. The righteous go free; the wicked bear the weight of what would have fallen on them."
    },
    "19": {
      "L": "It is better to dwell in the wilderness than with a contentious and an angry woman.",
      "M": "It is better to live in a desert than with a quarrelsome and angry woman.",
      "T": "The wilderness is harsh, lonely, without comfort — but it has peace. The home with a contentious, angry woman has everything except peace. Without peace, none of the rest matters."
    },
    "20": {
      "L": "There is treasure to be desired and oil in the dwelling of the wise, but a foolish man spendeth it up.",
      "M": "Precious treasure and oil are stored in the house of the wise, but a fool quickly squanders them.",
      "T": "The wise person keeps resources — saving, building, maintaining. The fool cannot hold what he has; his hands are full of holes. Wisdom is not just knowing things; it is being able to steward them."
    },
    "21": {
      "L": "He that followeth after righteousness and mercy findeth life, righteousness, and honour.",
      "M": "Whoever pursues righteousness and steadfast love will find life, righteousness, and honor.",
      "T": "The one who chases righteousness and mercy does not end up with less — they end up with more: life, more righteousness, and honor. This is not a path of sacrifice; it is a path of accumulation — the right kind."
    },
    "22": {
      "L": "A wise man scaleth the city of the mighty, and casteth down the strength of the confidence thereof.",
      "M": "A wise man can take a city of warriors and bring down the stronghold in which they trust.",
      "T": "Wisdom defeats force. The strong city built on military might can be dismantled by someone with the right knowledge. Intelligence, properly applied, beats raw power."
    },
    "23": {
      "L": "Whoso keepeth his mouth and his tongue keepeth his soul from troubles.",
      "M": "Whoever guards his mouth and tongue keeps himself out of trouble.",
      "T": "The mouth is the great source of self-inflicted trouble. Guard it, and you protect yourself from more than you realize — most trouble begins with something someone said."
    },
    "24": {
      "L": "Proud and haughty scorner is his name, who dealeth in proud wrath.",
      "M": "Proud, haughty, 'Scoffer' is his name — he acts with overweening arrogance.",
      "T": "This is a formal naming — a precise identification of a type. Pride plus haughtiness plus scorn equals a specific kind of person who operates in arrogant rage. The name is Scoffer. It is not a compliment."
    },
    "25": {
      "L": "The desire of the slothful killeth him, for his hands refuse to labour.",
      "M": "The craving of a sluggard will be his death, because his hands refuse to work.",
      "T": "The lazy person has wants like everyone else — but unlike everyone else, they will not work to meet them. Those unfulfilled desires, piling up without being addressed, become a kind of slow death."
    },
    "26": {
      "L": "He coveteth greedily all the day long, but the righteous giveth and spareth not.",
      "M": "The wicked covet all day long, but the righteous give generously without holding back.",
      "T": "The wicked spend their whole day in appetite — wanting, craving, accumulating in their minds what they cannot acquire. The righteous spend their day differently: giving, freely, without reservation."
    },
    "27": {
      "L": "The sacrifice of the wicked is abomination; how much more when he bringeth it with a wicked mind.",
      "M": "The sacrifice of the wicked is detestable; how much more when offered with evil intent.",
      "T": "An offering from the wicked is already offensive to God — the gesture of piety from an unrighteous life is a contradiction. But when the wicked person brings their sacrifice specifically to manipulate God through religious performance, it moves from bad to worse."
    },
    "28": {
      "L": "A false witness shall perish, but the man that heareth speaketh constantly.",
      "M": "A false witness will perish, but whoever listens speaks truthfully and endures.",
      "T": "The lying witness has no future — they perish. The person who has genuinely listened, who has attended to truth, has something real to say. And they will keep saying it long after the liar is gone."
    },
    "29": {
      "L": "A wicked man hardeneth his face, but as for the upright, he directeth his way.",
      "M": "A wicked man puts on a bold face, but the upright person carefully considers his way.",
      "T": "The wicked person's boldness is a form of moral callousness — they harden their face because they have stopped caring what is right. The upright person thinks carefully about where they are going and why."
    },
    "30": {
      "L": "There is no wisdom, nor understanding, nor counsel against the LORD.",
      "M": "There is no wisdom, no understanding, no counsel that can stand against the LORD.",
      "T": "All the strategy, all the brilliance, all the human cleverness ever assembled — none of it succeeds against the LORD. This is not a threat; it is a statement about the nature of things."
    },
    "31": {
      "L": "The horse is prepared against the day of battle, but safety is of the LORD.",
      "M": "The horse is made ready for the day of battle, but victory belongs to the LORD.",
      "T": "Do your preparation — get the horse ready, make your plans, marshal your forces. But the outcome of the battle is not yours to determine. Safety, victory, survival — these are in the LORD's hands."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 19–21 written.')

if __name__ == '__main__':
    main()
