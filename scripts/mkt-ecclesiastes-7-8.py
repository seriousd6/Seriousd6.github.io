"""
MKT Ecclesiastes chapters 7–8 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ecclesiastes-7-8.py

Translation decisions:

- H1892 (הֶבֶל, hevel): "vapor" in L (literal image — mist, breath, steam); "futility" in M
  (primary conceptual gloss for natural English); T varies by context, using either the vapor
  metaphor or its full existential weight. NOTE: ECC-1a/1b agents should be consistent with
  this if they modify their renderings — this is the first Ecclesiastes script executed.

- H3068 (יהוה, YHWH): does not appear in Ecclesiastes 7–8 in extant MT. Ecclesiastes uses
  H430 (הָאֱלֹהִים, ha-elohim) exclusively, almost always with the article — "the God" / "God."
  L/M: "God"; T: "God" throughout.

- H430 (אֱלֹהִים, elohim) + article: Ecclesiastes uniquely uses "ha-elohim" (the God) rather
  than bare elohim, creating a somewhat distant, philosophically measured tone. L preserves "God"
  (the article is grammatically part of the name-complex in Hebrew); M: "God"; T: sometimes
  unpacks the distancing function.

- H7307 (רוּחַ, ruach): in 7:8 "patient in spirit" — ruach here = inner disposition, not Spirit
  as divine entity. L: "spirit"; M: "spirit"; T: "inner disposition." In 8:8 "no one has power
  over the spirit to restrain the spirit" — likely refers to the animating life-breath, not wind.
  L: "spirit"; M/T: "life-breath."

- H7451 (רָע, ra'): "evil/bad/harm" — context determines. As adjective, rendered "evil" or
  "harmful"; as noun, "harm" or "evil thing." L follows the nuance; M/T disambiguate.

- H2617 (חֶסֶד): does not appear in these chapters.

- H5315 (נֶפֶשׁ, nephesh): 7:28 "which my soul has sought" — the seeking self, the whole
  searching person. L: "soul"; M: "I"; T: "my whole searching self."

- H4191 (מוּת, muth) / death imagery: 7:1–4 is a sustained meditation on death-day as better
  than birth-day. The T tier engages the theology without softening it.

- Textual note — 8:10: The MT reads יִשְׁתַּכְּחוּ (were forgotten), from root שכח (to forget).
  Several modern translations read יְשֻׁבְּחוּ (were praised) from root שבח (to praise), following
  some LXX and Syriac variants. The interlinear supports the MT "forgotten" reading, which is
  retained in L/M. The T tier notes the irony of forgotten wickedness.

- 7:26-28 (the woman passage): The Preacher reports finding one wise man in a thousand but no
  wise woman. L/M render this as reported observation. T acknowledges the ambiguity — this may
  reflect (a) the Preacher's own cultural situatedness, (b) his personal failed search connected
  to the Solomon tradition (1 Kings 11, many foreign wives leading to apostasy), or (c) an ironic
  note that wisdom is rare among all humanity, male and female. The T tier holds the tension
  rather than resolving it in either a misogynist or sanitizing direction.

- 7:16-17 (the two excesses): "Be not overly righteous / be not overly wicked." Not an
  endorsement of moral mediocrity, but a warning against performance-righteousness that destroys
  the practitioner and against reckless wickedness that cuts life short. T unpacks this distinction.

- Aspect notes: Hebrew imperfect and perfect forms in Ecclesiastes often have a gnomic quality
  (general present-tense truths) rather than strict tense. The T tier uses present tense for
  these gnomic forms throughout. Specific reported observations use past tense.

- Hebrew poetry: chs 7–8 are predominantly prose argument with proverbial inserts. Chapter 7:1–8
  contains a series of "better-than" (tov min) comparative proverbs. The T tier preserves the
  rhetorical structure of these comparisons without imposing artificial line breaks on the prose.
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


ECCLESIASTES = {
  "7": {
    "1": {
      "L": "A good name is better than precious ointment, and the day of death than the day of one's birth.",
      "M": "A good name is better than fine perfume, and the day of death than the day of birth.",
      "T": "The Hebrew links shem (name) and shemen (oil) — a good name and fine oil share their sound but not their permanence. Perfume dissipates; a good name endures. And the day of death ranks above the day of birth because at death the whole of a life can be measured, whereas birth is only unrealized possibility. You do not yet know what a birth-day means; a death-day declares it."
    },
    "2": {
      "L": "It is better to go to the house of mourning than to go to the house of feasting, for that is the end of all mankind, and the living will lay it to heart.",
      "M": "It is better to go to a house of mourning than to a house of feasting, for death is the end of every person, and the living should take it to heart.",
      "T": "A funeral is a more honest environment than a party. At a feast you can pretend that things will go on indefinitely; at a funeral the pretense collapses. The living person who attends a funeral and takes it to heart — who allows the sight of mortality to shape how they live — has done something a banquet cannot offer them."
    },
    "3": {
      "L": "Sorrow is better than laughter, for by sadness of countenance the heart is made better.",
      "M": "Sorrow is better than laughter, for a sad face does the heart good.",
      "T": "The paradox is real: grief improves the heart while laughter often leaves it unchanged. The sad face — the face that has looked honestly at hard things — belongs to a person whose inner life has been deepened by that looking. Laughter skims the surface; sorrow goes through."
    },
    "4": {
      "L": "The heart of the wise is in the house of mourning, but the heart of fools is in the house of mirth.",
      "M": "The heart of the wise is drawn to the house of mourning, but the heart of fools is drawn to the house of mirth.",
      "T": "Where you are pulled when you have a choice reveals who you are. Wise people are drawn toward the places where reality is not managed — toward grief, toward limit, toward honest reckoning. Fools flee into noise and pleasure. The fool's mirth is not harmless; it is a form of avoidance that keeps the heart in permanent shallowness."
    },
    "5": {
      "L": "It is better for a man to hear the rebuke of the wise than to hear the song of fools.",
      "M": "It is better to hear the rebuke of the wise than to hear the song of fools.",
      "T": "The wise person's rebuke is uncomfortable; it costs something to receive it. The fool's song is pleasant; it costs nothing and gives nothing. The man who chooses the song has chosen comfort over improvement. The man who chooses the rebuke has chosen the harder and more useful gift."
    },
    "6": {
      "L": "For like the crackling of thorns under a pot, so is the laughter of a fool; this also is vapor.",
      "M": "For like the crackling of thorns under a pot, so is the laughter of a fool — this too is futility.",
      "T": "Thorn-wood makes a quick, loud fire that produces impressive noise and heat and then burns out almost immediately, leaving less than proper fuel would have left. Fool's laughter is exactly this: attention-getting, briefly warming, and gone — producing no lasting heat, no lasting light. The Preacher names it vapor, because it is all surface and no substance."
    },
    "7": {
      "L": "Surely oppression makes a wise man foolish, and a bribe corrupts the heart.",
      "M": "Surely oppression makes a fool of a wise man, and a bribe corrupts the heart.",
      "T": "Sustained injustice can break even a wise person's capacity for clear thought. The wise person who is ground down by oppression long enough may begin to act like a fool — desperate, reactive, stripped of the perspective that made them wise. And a bribe does not merely purchase a verdict; it corrupts the heart that receives it, distorting judgment at the root."
    },
    "8": {
      "L": "Better is the end of a thing than its beginning, and better is a patient spirit than a proud spirit.",
      "M": "The end of a matter is better than its beginning, and patience of spirit is better than pride of spirit.",
      "T": "At the beginning of a thing you have only hope and energy; at the end you have evidence. The end is where you actually learn whether what you began was worth beginning. And the patient spirit — the one that can wait, that does not need to prevail immediately — outlasts the proud spirit that demands recognition before the matter is complete."
    },
    "9": {
      "L": "Be not hasty in your spirit to become angry, for anger lodges in the bosom of fools.",
      "M": "Do not be hasty in your spirit to become angry, for anger rests in the lap of fools.",
      "T": "Anger wants to take up permanent residence. In the person who has not checked it, anger settles into the chest like a tenant who never leaves — shaping every response, coloring every perception. The wise person evicts it; the fool gives it a home and calls it righteous."
    },
    "10": {
      "L": "Do not say, 'Why were the former days better than these?' for it is not from wisdom that you ask this.",
      "M": "Do not say, 'Why were the former days better than these?' for it is not from wisdom that you ask this.",
      "T": "Nostalgia mistakes the direction of wisdom. The former days were not actually better — you simply cannot remember their actual weight. And the question 'why were things better before?' keeps your attention fixed on a past that cannot be recovered rather than on the present where wisdom can actually operate. The Preacher does not forbid grief or memory; he forbids the untested assumption that then was better than now."
    },
    "11": {
      "L": "Wisdom is good with an inheritance; indeed, it is an advantage for those who see the sun.",
      "M": "Wisdom, like an inheritance, is a good thing; it benefits those who see the sun.",
      "T": "Wisdom and material resources work better together than either works alone. An inheritance without wisdom gets wasted; wisdom without resources is constrained. Together they produce the kind of life that is genuinely advantageous — not merely surviving under the sun but flourishing in it."
    },
    "12": {
      "L": "For the protection of wisdom is like the protection of money, and the advantage of knowledge is this: wisdom preserves the life of him who has it.",
      "M": "For wisdom protects just as money protects, but the advantage of knowledge is that wisdom preserves the life of its possessor.",
      "T": "Money and wisdom both function as shelter — they create options, reduce vulnerability, protect from the worst outcomes. But here they diverge: money can run out, can be stolen, can fail. Wisdom preserves life itself. It is not merely a resource management tool; it is the orientation that allows a person to remain alive in a deep sense — not just biologically, but as an integrated human being."
    },
    "13": {
      "L": "Consider the work of God: who can make straight what he has made crooked?",
      "M": "Consider what God has done: who can straighten what he has made crooked?",
      "T": "Some things in the world are set by God and cannot be corrected by human effort. This is not fatalism — it is the Preacher's insistence on accurate mapping of what is and is not in human hands. The wisdom that tries to straighten what God has made crooked is wasted; the wisdom that accepts the crooked thing and works within it is genuine. Seeing clearly what you cannot change is the beginning of acting wisely within it."
    },
    "14": {
      "L": "In the day of good fortune, be joyful, and in the day of adversity, consider: God has made the one as well as the other, so that man may not find out anything that will be after him.",
      "M": "In good times, enjoy what you have; but in bad times consider this — God has made both the one and the other, so that no one can discover what the future holds.",
      "T": "The right response to prosperity is not anxiety about losing it but genuine enjoyment of what is present. The right response to adversity is not despair but reflection: this too is God's making. And God has arranged things so that the future remains opaque. You cannot read what is coming from what is present. This inaccessibility of the future is not a punishment; it is the architecture of a life that must be lived forward in trust."
    },
    "15": {
      "L": "All this I have seen in my days of vapor: there is a righteous man who perishes in his righteousness, and there is a wicked man who prolongs his life in his wickedness.",
      "M": "In my futile days I have seen everything: a righteous man perishing in his righteousness, and a wicked man living long in his wickedness.",
      "T": "The Preacher reports what he has actually observed, not what the tidy moral schema would predict. Righteousness does not insulate against early death. Wickedness does not guarantee an early grave. He has seen both inverted outcomes with his own eyes, during the days of his own brief, vapor-like life. He does not explain this away or deny it. He names it, and goes on thinking."
    },
    "16": {
      "L": "Be not overly righteous, and do not make yourself too wise. Why should you destroy yourself?",
      "M": "Do not be excessively righteous, and do not make yourself overly wise. Why should you ruin yourself?",
      "T": "This is not permission to be wicked. The Preacher is warning against a performance of righteousness so extreme, so rigid, so self-conscious that it collapses under its own weight and destroys the person practicing it. Hyper-scrupulosity is its own trap — it produces not holiness but a kind of spiritual self-destruction. The person who must be righteous in every conceivable corner, who cannot allow themselves a moment of ordinary life, will break."
    },
    "17": {
      "L": "Be not overly wicked, neither be a fool. Why should you die before your time?",
      "M": "Do not be excessively wicked, and do not be a fool. Why die before your time?",
      "T": "The matching warning on the other side. Reckless wickedness is not sophisticated freedom — it is the short path to premature destruction. The fool who treats wickedness as strength or cleverness as license is shortening his own life. Both the over-righteous and the recklessly wicked are destroying themselves; the Preacher wants neither outcome."
    },
    "18": {
      "L": "It is good that you should take hold of this, and from the other not let your hand go; for the one who fears God shall come forth from them all.",
      "M": "It is good to grasp the one and not release the other, for the one who fears God will avoid both extremes.",
      "T": "The fear of God is the practical path through both dangers. It is not a middle path of moral mediocrity — splitting the difference between too righteous and too wicked. It is the orientation that allows a person to navigate the extremes that destroy: grounding in God produces the stability that neither hyper-scrupulosity nor recklessness can provide. The God-fearer comes through both where others fall."
    },
    "19": {
      "L": "Wisdom gives the wise man more strength than ten rulers who are in a city.",
      "M": "Wisdom strengthens the wise more than ten rulers in a city.",
      "T": "Ten rulers in a city represent the maximum of organized institutional power. Wisdom, held by a single person, exceeds all of it. This is not because wisdom makes you politically powerful but because wisdom allows you to navigate what power cannot manage — the deep complexity of living well, the questions that authority cannot answer by decree."
    },
    "20": {
      "L": "For there is not a righteous man on earth who does good and never sins.",
      "M": "Indeed, there is no righteous person on earth who always does good and never sins.",
      "T": "This verse contextualizes the warning about over-righteousness in v16. The reason one should not become hyper-scrupulous about righteousness is that the project is impossible for anyone. Universal moral fallibility is not a counsel of despair but a description of reality that genuine wisdom accepts. The person who knows they will sometimes sin is better positioned to live honestly than the one who has convinced themselves they never do."
    },
    "21": {
      "L": "Do not take to heart all the things that people say, lest you hear your servant cursing you.",
      "M": "Do not pay attention to everything people say, or you may hear your own servant cursing you.",
      "T": "If you make yourself fully available to every word spoken about you — especially the negative ones — you will live in a state of perpetual wound. People say unkind things. Even people who depend on you and whom you treat well will, in an unguarded moment, curse you. If you let every such word reach the center of your identity, you will be perpetually destabilized. Some distance from your own reputation is not arrogance; it is sanity."
    },
    "22": {
      "L": "For many times your own heart knows that you yourself also have cursed others.",
      "M": "For your own heart knows that you too have cursed others many times.",
      "T": "Before you close around the wound of someone else's curse, your own heart reminds you: you have done this exact thing. You have muttered against the powerful, against those who employed you, against those who had what you wanted. The curse you overheard is the same currency you have spent. This does not make the servant's curse acceptable; it makes vengeful reaction absurd."
    },
    "23": {
      "L": "All this I have tested by wisdom; I said, 'I will be wise,' but it was far from me.",
      "M": "All this I have tested by wisdom; I said, 'I will be wise' — but wisdom was far from me.",
      "T": "The Preacher has applied his most disciplined intellectual effort to everything he has just described. He set out to be wise — comprehensively, definitively wise. And he discovered that wisdom in its full form kept receding. The more he pursued it, the more clearly he saw that its deepest form was beyond his reach. This is not failure; it is honest reporting of what rigorous self-examination discovers."
    },
    "24": {
      "L": "That which exists is far off and very deep; who can find it out?",
      "M": "Whatever exists is far off and utterly deep — who can discover it?",
      "T": "Reality is more complex than any investigative system. The depth of what exists — even in a single human life, let alone the whole of creation — exceeds what can be plumbed by inquiry, however sustained. The Preacher does not say this as a reason to stop thinking; he says it as the honest conclusion of having thought very hard. The limits of wisdom are only visible to those who have actually pressed against them."
    },
    "25": {
      "L": "I turned my heart to know and to search and to seek out wisdom and the scheme of things, and to know the wickedness of folly and the foolishness that is madness.",
      "M": "I turned my mind to know, to investigate, and to seek out wisdom and the explanation of things — to know that wickedness is folly and that foolishness is madness.",
      "T": "The intellectual program is vast: not only wisdom but its opposite, not only folly but the variety of foolishness all the way to madness. He wants a comprehensive account — a reckoning that includes the whole range of human experience, from its best expression to its worst. This is not a detached academic exercise; it is the kind of total searching that only someone who genuinely wants to understand can sustain."
    },
    "26": {
      "L": "And I find more bitter than death the woman whose heart is snares and nets, and whose hands are fetters. He who pleases God escapes her, but the sinner is taken by her.",
      "M": "And I find more bitter than death the woman whose heart is a trap, whose hands are chains. The one who pleases God escapes her, but the sinner is caught by her.",
      "T": "What the Preacher has found in his searching is something more bitter than death — a figure of entrapment whose very heart is constructed to catch. Whether this is a specific category of seductive woman, the Strange Woman personified from Proverbs' tradition, or a metaphor for any path that leads the searcher away from wisdom, the moral line is clear: the one whose life pleases God is not caught; the sinner is. The trap does not grab randomly — it selects by the quality of your orientation."
    },
    "27": {
      "L": "Behold, this is what I found, says the Preacher, counting one by one to find the sum,",
      "M": "Here is what I found, says the Preacher, adding one thing to another to find the result:",
      "T": "The Preacher steps back and marks the weight of what he is about to report. This is not casual observation; it is the output of systematic counting — working through instance after instance, accumulating evidence, trying to arrive at a sum that means something. What follows is that sum."
    },
    "28": {
      "L": "which my soul has continually sought but I have not found: one man among a thousand I have found, but a woman among all these I have not found.",
      "M": "I have continually searched but not found: one man in a thousand I have found, but not one woman among all these.",
      "T": "The Preacher counts the wise across his lifetime of searching and finds the ratio devastating: one truly wise person in a thousand men. And among women — by his own accounting — none. Modern readers rightly pause here. The Preacher is a man of his culture, possibly writing out of the tradition of Solomon whose thousand foreign wives led to apostasy (1 Kings 11). His spiritual ledger may reflect the damage done in that tradition more than a universal claim about women's capacity for wisdom. What is not in doubt is the main point: wisdom is vanishingly rare across all humanity. The one-in-a-thousand figure is not praise of men; it is near-total indictment of them too."
    },
    "29": {
      "L": "See, this alone I have found: God made mankind upright, but they have sought out many schemes.",
      "M": "This alone I have found: God made human beings upright, but they have gone in search of many devices.",
      "T": "Here is the bottom of the Preacher's accounting. The original design was integrity — uprightness, straightforwardness, alignment between what a person is and what they do. What human beings have done with that design is fill it with devices and schemes, elaborate strategies for getting what they want by means other than integrity. The complexity of the moral landscape is not God's doing; it is humanity's self-generated departure from a simpler and better starting point."
    }
  },
  "8": {
    "1": {
      "L": "Who is like the wise man? And who knows the interpretation of a thing? A man's wisdom makes his face shine, and the hardness of his face is changed.",
      "M": "Who is like the wise man? Who else knows the meaning of a matter? A person's wisdom brightens his face and transforms its harsh expression.",
      "T": "Wisdom is rare — who has it? But it is also visible: the wise person's face shows it. The harsh, defensive grimness that comes from not understanding what is happening around you relaxes when wisdom arrives. You can tell a wise person partly because they have stopped bracing against reality; they have stopped trying to harden their face against what they don't know. Wisdom makes the face open."
    },
    "2": {
      "L": "I say: Keep the king's command, because of the oath of God.",
      "M": "I counsel you: keep the king's command, and do so because of your oath before God.",
      "T": "Political loyalty is grounded in something deeper than mere pragmatism. You keep the king's command not simply because disobedience is dangerous but because you made an oath before God to do so. The obligation runs through God, not just through fear of the king. This makes the loyalty genuine rather than merely self-interested, and it also implies limits: an oath before God can only bind you to what God would permit."
    },
    "3": {
      "L": "Be not hasty to leave his presence; do not persist in an evil matter, for he does whatever he pleases.",
      "M": "Do not be in a hurry to leave the king's presence; do not persist in a bad cause, for he does whatever he wants.",
      "T": "Two practical counsels about navigating royal authority: do not storm out in anger — the exit you make in haste will define how the king sees you from that moment on — and do not become the person who keeps pushing a position the king has already rejected. The king has the power to act on his will; the wise person operates within that reality rather than against it."
    },
    "4": {
      "L": "For the word of a king is supreme, and who may say to him, 'What are you doing?'",
      "M": "For the king's word is absolute, and no one can say to him, 'What are you doing?'",
      "T": "This is not an endorsement of royal tyranny but a description of ancient political reality. Royal power was not accountable in the way ordinary social power was. The wise person navigates this as a fact rather than fighting it as an injustice in each individual encounter. Knowing that the king is not answerable to you does not mean accepting whatever the king does; it means choosing your engagements strategically."
    },
    "5": {
      "L": "Whoever keeps the commandment will not experience an evil thing, and the wise heart will know both time and judgment.",
      "M": "Whoever obeys his command will come to no harm, and the wise heart will know the proper time and way.",
      "T": "Here is the practical advantage of wisdom in a political environment: the wise person not only avoids harm by complying with legitimate authority — they also develop the discernment to know when the time is right and what the right course of action looks like. This is not mere compliance; it is the deeper skill of reading situations well enough to act rightly within them."
    },
    "6": {
      "L": "For there is a time and a way for every matter, though man's trouble is heavy on him.",
      "M": "For every purpose has its proper time and method, though a person's trouble weighs heavily on him.",
      "T": "Every situation has a right moment and a right approach. But knowing what they are presses down on the person who must find them. The knowledge that a right time exists does not automatically grant access to it; discovering it requires the kind of patient discernment that is itself a weight to carry. The heaviness is real. The Preacher does not pretend that wisdom makes life light."
    },
    "7": {
      "L": "For he does not know what will be, for who can tell him when it will be?",
      "M": "For no one knows what is coming, and who can tell him how it will come?",
      "T": "The fundamental condition of all human decision-making: you are acting without full information about what is coming. No one has the data needed to act with perfect wisdom. This is not a reason for paralysis; it is the honest admission that every action is taken in partial light. The wise person acts anyway, without pretending to certainty they do not have."
    },
    "8": {
      "L": "No man has power over the spirit to retain the spirit, nor power over the day of death; and there is no discharge in war, nor will wickedness deliver those who practice it.",
      "M": "No one has power over the life-breath to restrain it, and no one has power over the day of death. There is no release from that battle, and wickedness will not save those who pursue it.",
      "T": "Four domains where human power ends completely: no one can hold their own life-breath in when it is departing; no one controls the day they will die; no soldier can buy a discharge from the war that has already claimed them; and no amount of wickedness, however cleverly deployed, will rescue the person who has given themselves to it. These four together define the outer boundary of what human agency can accomplish. Beyond this boundary, something else holds authority."
    },
    "9": {
      "L": "All this I have observed while applying my heart to all the work that is done under the sun, while man lords it over man to his hurt.",
      "M": "All this I observed while applying my mind to everything done under the sun — a time when one person dominates another to their own harm.",
      "T": "The Preacher has been watching. He has not theorized in isolation; he has attended carefully to what actually happens when human beings exercise power over each other. And what he consistently observes is that the person doing the dominating damages themselves in the process. Power exercised over others at their expense turns out also to be power exercised at the dominator's own expense. The harm flows both ways."
    },
    "10": {
      "L": "And so I saw the wicked buried — they had come and gone from the holy place, and they were forgotten in the city where they had done such things. This also is vapor.",
      "M": "Then I saw the wicked buried — they had come and gone from the sacred place, and they were soon forgotten in the very city where they had done such things. This too is futility.",
      "T": "The scandal the Preacher observes is not just that the wicked died — it is that they received burial, that they had regular access to the holy place, and that they were forgotten once gone. Not condemned, not exposed, not prosecuted — forgotten. The city that should have remembered their deeds chose not to. This erasure of accountability is its own form of vapor: it looks like something (order, religion, civic memory) but amounts to nothing."
    },
    "11": {
      "L": "Because the sentence against an evil deed is not executed speedily, the heart of the children of man is fully set to do evil.",
      "M": "When the sentence for a wrong is not carried out quickly, the human heart is emboldened to do evil.",
      "T": "Delayed justice is not neutral — it actively teaches the wrong lesson. When people observe that evil actions carry no immediate consequence, they read that as permission. The heart is not a passive object; it is an agent that interprets what it sees and draws conclusions. What it concludes from unpunished wickedness is that wickedness is safe. This is why the speed of justice matters beyond efficiency: it is forming the moral imagination of everyone who watches."
    },
    "12": {
      "L": "Though a sinner does evil a hundred times and prolongs his life, yet I know that it will be well with those who fear God, who fear before him.",
      "M": "Although a sinner does evil a hundred times and still lives long, I know that it will go well with those who fear God, who stand in awe before him.",
      "T": "The Preacher holds both realities in the same sentence without resolving them. He has just described the problem: the wicked live long and go unpunished. He does not retract that observation. And yet — and this is the weight of the word 'yet' — he knows that the God-fearer is in a fundamentally different situation. Both things are true simultaneously. This is not naive piety; it is the harder faith that refuses to let observed injustice cancel the conviction that God-orientation is the right way to live."
    },
    "13": {
      "L": "But it will not be well with the wicked, neither will he lengthen his days like a shadow, because he does not fear before God.",
      "M": "But it will not go well with the wicked, and their days will not lengthen like a shadow, because they do not fear God.",
      "T": "The shadow is precisely the right image for the wicked person's extended life: long, but without substance. A shadow stretches a long way but has no weight, no depth, no reality of its own. The life of the person who refuses the fear of God may extend in calendar terms, but it does not deepen or fill. It lengthens without gaining meaning, which is a form of diminishment, not growth."
    },
    "14": {
      "L": "There is a vapor that takes place on earth: there are righteous people to whom it happens according to the deeds of the wicked, and there are wicked people to whom it happens according to the deeds of the righteous. I said that this also is vapor.",
      "M": "There is a futility that occurs on earth: the righteous get what the wicked deserve, and the wicked get what the righteous deserve. I said that this too is futility.",
      "T": "The Preacher brings the observation to its sharpest point. The moral order does not merely fail occasionally — it sometimes inverts entirely. The righteous receive the punishment that wickedness should have earned, and the wicked receive the reward that righteousness should have produced. The Preacher does not explain this, does not offer a theodicy, does not say 'but in the end it will be set right.' He calls it vapor. The inversion of justice is itself a form of unreality — something that looks like order but is in fact disorder at the foundation. And he keeps living and thinking within it."
    },
    "15": {
      "L": "And I commend joy, for man has nothing better under the sun than to eat and to drink and to be joyful, for this will go with him in his toil through the days of his life that God has given him under the sun.",
      "M": "So I commend joy — for there is nothing better for people under the sun than to eat and drink and be glad. This accompanies them in their work through all the days of life that God has given them under the sun.",
      "T": "Given that the big explanations are unavailable, given that the moral order is not reliably visible, given that wisdom cannot fully map the work of God — the Preacher commends joy. Not as a consolation prize or an escape, but as a genuine good that God has arranged within human life. The food, the drink, the gladness of a day's work completed: these are what God has given, and they are sufficient to constitute a real life. The joy is not about ignoring the problems; it is about not being so consumed by the unsolvable problems that you miss the actual gifts."
    },
    "16": {
      "L": "When I applied my heart to know wisdom and to see the business that is done on earth — for neither day nor night does one see sleep with his eyes —",
      "M": "When I applied my mind to know wisdom and to observe all the activity carried on upon the earth — for neither day nor night do people see sleep —",
      "T": "The one who really tries to understand how the world works never fully stops. The business of human life under the sun is relentless; there is always more to observe, more to analyze, more to reckon with. The Preacher is describing the exhausting but necessary discipline of total attention — the kind that does not shut off when the sun goes down because the questions do not shut off either."
    },
    "17": {
      "L": "then I saw all the work of God, that man cannot find out the work that is done under the sun. However much man may toil in seeking, he will not find it out. Even if a wise man claims to know, he cannot find it out.",
      "M": "then I saw all the work of God — that no one can discover what is done under the sun. No matter how much one labors in searching, they will not find it out. Even if the wise claim to know, they cannot find it out.",
      "T": "This is the chapter's conclusion and one of Ecclesiastes' central claims: God's work is finally inaccessible to even the most thorough human investigation. The Preacher has been maximally honest about how hard he has looked. He is not a person who gave up easily, or searched carelessly. He looked with everything he had. And he could not find the full account of what God is doing. Not only that: the wise person who claims to have found it has not. The claim to comprehensive understanding of God's work is itself a kind of foolishness — the last trap for the person who has been wise about almost everything else."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ecclesiastes')
        merge_tier(existing, ECCLESIASTES, tier_key)
        save(tier_dir, 'ecclesiastes', existing)
    print('Ecclesiastes 7–8 written.')

if __name__ == '__main__':
    main()
