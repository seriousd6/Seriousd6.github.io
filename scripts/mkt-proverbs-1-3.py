"""
MKT Proverbs chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-1-3.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" (all caps) in L/M; "the LORD" in T. Consistent with
  the entire OT series.

- H2451/H2454 (חָכְמָה/חָכְמוֹת, chokmah/chokmoth): "wisdom" in all tiers. The
  plural form in 1:20 (chokmoth) is a Hebrew intensive plural indicating the fullness
  of Wisdom — rendered with Lady Wisdom imagery in T tier.

- H2617 (חֶסֶד, hesed): In 3:3 paired with 'emet. L/M: "steadfast love"; T: "covenant
  love." No single English word captures covenant loyalty + active kindness. "Mercy"
  (KJV) is too weak; "steadfast love" is the consensus scholarly rendering.

- H7307 (רוּחַ, ruach): In 1:23 ("I will pour out my spirit") — Wisdom is the
  speaker, not God directly. All tiers: lowercase "spirit" — this is Wisdom's own
  animation/insight being offered, not the divine Spirit in the technical theological
  sense. Documented as a deviation from KJV.

- H5315 (נֶפֶשׁ, nephesh): "soul" in 2:10; 3:22. The embodied self, not a Greek
  immaterial soul. "Inner being" or "soul" preferred over "life" where the emphasis
  is on interiority.

- H1285 (בְּרִית, berith): "covenant" in 2:17. The woman forsakes the "covenant
  of her God" — likely the marriage covenant made before God, not a general
  religious obligation.

- H5475 (סוֹד, sod): In 3:32, "secret counsel / intimate circle." L: "secret
  counsel"; M: "inner circle"; T: "council." The sod is the inner circle of
  trusted confidants — here God's.

- H2454 (chokmoth, plural/personified): Lady Wisdom in 1:20-33 — the personified
  Wisdom who cries out publicly. T tier leans into this personification.

- H7496 (רְפָאִים, Rephaim): 2:18 "shades" / the dead spirits. L: "the dead";
  M: "the spirits of the dead"; T: implied in "death" destination.

- Proverbs 1:17 (the bird/net proverb): The Hebrew is ironic — the bird sees the
  trap and avoids it; the violent men set a trap for others but it catches themselves
  (v18). The T tier makes this ironic reversal explicit.

- Aspect notes: Most Proverbs sentences are gnomic present (timeless truths),
  corresponding to the Hebrew participial or imperfect used for general statements.
  These are rendered as simple present or future in English.

- Proverbs 1:7 is the theological motto ("fear of the LORD = beginning of knowledge")
  and frames the entire book. All three tiers treat it as the programmatic statement
  it is.

- Chapter 3:18 ("tree of life"): Deliberate echo of Gen 2:9; 3:22,24. T tier notes
  this echo explicitly.

- Chapter 3:19-20 (wisdom in creation): Closely parallels Job 38-39 and Proverbs
  8:22-31. The LORD uses wisdom/understanding/knowledge as the instruments of
  creation. T tier draws out the implication that pursuing wisdom connects the
  student to the creative order itself.
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
  "1": {
    "1": {
      "L": "The proverbs of Solomon, son of David, king of Israel:",
      "M": "The proverbs of Solomon, son of David, king of Israel:",
      "T": "The collected wisdom-sayings of Solomon, son of David, king of Israel."
    },
    "2": {
      "L": "To know wisdom and instruction, to perceive the words of understanding;",
      "M": "For learning wisdom and discipline, for understanding insightful words;",
      "T": "These sayings exist to cultivate wisdom and discipline — to help you understand what genuine insight means."
    },
    "3": {
      "L": "To receive instruction in wise dealing, in righteousness, justice, and equity;",
      "M": "To gain training in wise conduct — in righteousness, justice, and integrity;",
      "T": "To shape the kind of person who deals wisely, who lives with justice and does what is right."
    },
    "4": {
      "L": "To give prudence to the simple, knowledge and discretion to the young man;",
      "M": "To give shrewdness to the naive and knowledge and discernment to the young —",
      "T": "To sharpen the mind of the inexperienced, and give the young man the judgment he lacks."
    },
    "5": {
      "L": "A wise man will hear and increase in learning, and a man of understanding will acquire wise counsel,",
      "M": "Let the wise hear and grow in learning; let the discerning acquire skill in guidance,",
      "T": "Even the wise should keep listening and keep growing. The person of real discernment learns how to navigate."
    },
    "6": {
      "L": "To understand a proverb and a saying, the words of the wise and their riddles.",
      "M": "To understand a proverb and its meaning, the words of the wise and their enigmas.",
      "T": "To grasp a proverb and the layered meaning beneath it — to hear what the sages say and wrestle with the riddle."
    },
    "7": {
      "L": "The fear of the LORD is the beginning of knowledge; fools despise wisdom and instruction.",
      "M": "The fear of the LORD is the beginning of knowledge; fools despise wisdom and discipline.",
      "T": "It all starts here: the fear of the LORD is the foundation of true knowledge. Only fools despise wisdom and refuse correction."
    },
    "8": {
      "L": "Hear, my son, your father's instruction, and forsake not your mother's law;",
      "M": "Listen, my son, to your father's instruction, and do not abandon your mother's teaching;",
      "T": "My son, take your father's correction to heart. Do not walk away from what your mother taught you."
    },
    "9": {
      "L": "For they are a garland of grace for your head and chains for your neck.",
      "M": "They will be a graceful garland on your head and a chain of honor around your neck.",
      "T": "Keep these words and they will adorn you — a wreath of honor on your head, a chain around your neck that marks you as someone worth knowing."
    },
    "10": {
      "L": "My son, if sinners entice you, do not consent.",
      "M": "My son, if sinners entice you, do not yield.",
      "T": "My son, when violent people try to pull you in — refuse."
    },
    "11": {
      "L": "If they say, 'Come with us, let us lie in wait for blood; let us lurk privily for the innocent without cause;'",
      "M": "If they say, 'Come with us — let us lie in wait for someone's blood, let us ambush the innocent for no reason;'",
      "T": "They will say: 'Come on, join us — we'll wait in the dark for someone, we'll trap the innocent who has done nothing to us.'"
    },
    "12": {
      "L": "Like Sheol let us swallow them alive, and whole, like those who go down to the pit;",
      "M": "We will swallow them alive like Sheol, whole like those who descend to the grave;",
      "T": "We'll devour them alive — the way death swallows the living, the way the grave takes them whole."
    },
    "13": {
      "L": "We shall find all precious goods; we shall fill our houses with plunder;",
      "M": "We will find every kind of treasure and fill our homes with loot;",
      "T": "Think of what we'll gain — every valuable thing, our homes packed with the spoils."
    },
    "14": {
      "L": "Cast your lot among us; we will all have one purse —",
      "M": "Throw in your lot with us; we will share a common purse —",
      "T": "Join us, take your share of the risk, share in the reward. We are all in this together."
    },
    "15": {
      "L": "My son, do not walk in the way with them; hold back your foot from their path,",
      "M": "My son, do not walk on their road; keep your feet far from their path;",
      "T": "My son — do not go with them. Not one step down their road."
    },
    "16": {
      "L": "For their feet run to evil and they make haste to shed blood.",
      "M": "Their feet run toward evil and they rush to shed blood.",
      "T": "They do not walk into violence — they run. Their feet know no other direction."
    },
    "17": {
      "L": "Surely in vain is the net spread in the sight of any bird;",
      "M": "How futile to spread a net in full view of the bird you intend to catch.",
      "T": "Even a bird knows to flee a trap it can see. These men are less perceptive than birds — and just as doomed."
    },
    "18": {
      "L": "But they lie in wait for their own blood; they lurk privily for their own lives.",
      "M": "These men lie in wait for their own blood; they ambush their own lives.",
      "T": "The trap they are setting? It is for themselves. The blood they hunger for turns out to be their own."
    },
    "19": {
      "L": "So are the ways of everyone greedy for gain; it takes away the life of its possessors.",
      "M": "Such is the fate of everyone who is greedy for unjust gain — it costs them their lives.",
      "T": "Greed for violent profit always works this way: the man who pursues it ends up destroying himself."
    },
    "20": {
      "L": "Wisdom cries aloud in the open squares; in the streets she raises her voice;",
      "M": "Wisdom cries out in the streets; in the public squares she raises her voice;",
      "T": "Lady Wisdom is not hidden in a library — she shouts in the street, she calls out in every marketplace."
    },
    "21": {
      "L": "At the head of the noisy streets she cries out; at the openings of the city gates she speaks her words:",
      "M": "At the head of the busy thoroughfares she calls; at the gates of the city she speaks:",
      "T": "At the busiest crossroads, at the city gate where everyone passes — she raises her voice where no one can claim they never heard."
    },
    "22": {
      "L": "How long, O simple ones, will you love simplicity? And scoffers delight in their scoffing? And fools hate knowledge?",
      "M": "How long, you naive ones, will you love foolishness? How long will scoffers delight in their scorn and fools hate knowledge?",
      "T": "How long? How long will the naive stay naive — happy to remain that way? How long will the cynics keep mocking what they refuse to learn, and the fools keep hating the very knowledge that could save them?"
    },
    "23": {
      "L": "Turn at my reproof; behold, I will pour out my spirit to you; I will make known my words to you.",
      "M": "Turn back at my rebuke. Look — I will pour out my spirit to you; I will make my words known to you.",
      "T": "Come back when I call you — even now. I will open everything up: pour out my insight, show you what I know."
    },
    "24": {
      "L": "Because I have called and you refused; I have stretched out my hand and no one regarded,",
      "M": "But I called and you refused; I stretched out my hand and no one paid attention;",
      "T": "You were warned. I called out and you walked past. I reached out and you turned away."
    },
    "25": {
      "L": "Because you have set at nought all my counsel and would have none of my reproof,",
      "M": "You rejected all my advice and would accept none of my correction —",
      "T": "Every word of guidance I offered — you ignored it. Every correction I gave — you refused."
    },
    "26": {
      "L": "I also will laugh at your calamity; I will mock when your terror comes,",
      "M": "I will laugh at your calamity; I will mock when terror strikes you,",
      "T": "When disaster comes — and it will — do not expect my sympathy. I will be the one who laughs."
    },
    "27": {
      "L": "When your terror comes like a storm and your calamity like a whirlwind, when distress and anguish come upon you.",
      "M": "When terror sweeps over you like a storm and your calamity arrives like a whirlwind, when distress and anguish overwhelm you.",
      "T": "Your disaster will come like a sudden storm — all at once, no warning. Panic. Anguish. The whirlwind you chose."
    },
    "28": {
      "L": "Then they will call upon me, but I will not answer; they will seek me diligently and not find me.",
      "M": "Then they will call on me, but I will not answer; they will search for me but will not find me.",
      "T": "That is when they will finally come looking for me. And I will not be there."
    },
    "29": {
      "L": "Because they hated knowledge and did not choose the fear of the LORD,",
      "M": "Because they hated knowledge and did not choose to fear the LORD,",
      "T": "It comes to this: they despised the very thing that could have saved them, and refused to walk in the fear of the LORD."
    },
    "30": {
      "L": "They would have none of my counsel and despised all my reproof.",
      "M": "They wanted none of my advice and rejected every correction I offered.",
      "T": "They waved off every word of wisdom. Every attempt at correction — beneath them."
    },
    "31": {
      "L": "Therefore they shall eat the fruit of their own way and be filled with their own devices.",
      "M": "So they will eat the fruit of their own path and be gorged on their own schemes.",
      "T": "The harvest they chose: their own choices, their own destruction. They will eat until they are sick of themselves."
    },
    "32": {
      "L": "For the turning away of the simple will kill them, and the complacency of fools will destroy them;",
      "M": "The waywardness of the naive will kill them, and the complacency of fools will be their ruin;",
      "T": "Naivety kills — not by accident but by the steady refusal to learn. And the fool's comfortable life? It is the anesthetic that makes the destruction complete."
    },
    "33": {
      "L": "But whoever listens to me will dwell safely and will be quiet from fear of evil.",
      "M": "But whoever listens to me will live in security and be free from the dread of harm.",
      "T": "Those who listen — and only those — will live without fear. They will lie down in peace."
    }
  },
  "2": {
    "1": {
      "L": "My son, if you receive my words and treasure up my commandments with you,",
      "M": "My son, if you accept my words and store up my commands within you,",
      "T": "My son, this is how wisdom comes: take what I say seriously; keep my instructions close."
    },
    "2": {
      "L": "Making your ear attentive to wisdom and inclining your heart to understanding,",
      "M": "Turning your ear toward wisdom and directing your heart to understanding,",
      "T": "Orient yourself: lean toward wisdom with your ear; bend your whole inner life toward understanding."
    },
    "3": {
      "L": "Yea, if you cry out for insight and raise your voice for understanding,",
      "M": "Yes, if you call out for discernment and cry aloud for understanding,",
      "T": "Don't just sit and wait for it — call for it. Pursue understanding the way a desperate person calls for help."
    },
    "4": {
      "L": "If you seek her as silver and search for her as for hidden treasures,",
      "M": "If you search for it like silver and dig for it like buried treasure,",
      "T": "Treat wisdom the way a man treats silver — hunt for it, dig for it, refuse to stop until you find it."
    },
    "5": {
      "L": "Then you will understand the fear of the LORD and find the knowledge of God.",
      "M": "Then you will understand what it means to fear the LORD and you will find the knowledge of God.",
      "T": "When you pursue it that way, the fear of the LORD becomes real to you, and you will know God — not merely know about him."
    },
    "6": {
      "L": "For the LORD gives wisdom; from his mouth come knowledge and understanding.",
      "M": "For the LORD gives wisdom; from his mouth flow knowledge and understanding.",
      "T": "Wisdom does not come from within you — it comes from the LORD. Every word of real knowledge begins with him."
    },
    "7": {
      "L": "He stores up sound wisdom for the upright; he is a shield to those who walk in integrity,",
      "M": "He stores up proven wisdom for the upright; he is a shield for those who live with integrity,",
      "T": "He has reserves of proven wisdom laid up for those who live honestly. He stands between them and every threat."
    },
    "8": {
      "L": "Keeping the paths of justice and watching over the way of his faithful ones.",
      "M": "He guards the paths of justice and protects the way of those who are faithful to him.",
      "T": "Every road that leads to righteousness — he watches it. His covenant people walk under his care."
    },
    "9": {
      "L": "Then you will understand righteousness and justice and equity, every good path.",
      "M": "Then you will understand what is right and just and fair — every good way of living.",
      "T": "Once wisdom enters you, the moral landscape clears: you see what is right, what is just, what is fair — and you know the difference."
    },
    "10": {
      "L": "For wisdom will enter your heart, and knowledge will be pleasant to your soul;",
      "M": "For wisdom will enter your heart and knowledge will delight your inner being;",
      "T": "Wisdom does not stay outside you — it takes up residence in you, and when it does, knowing becomes something you love."
    },
    "11": {
      "L": "Discretion will keep you; understanding will guard you,",
      "M": "Discretion will watch over you; understanding will protect you,",
      "T": "Discernment becomes your bodyguard; understanding stands at your door."
    },
    "12": {
      "L": "To deliver you from the way of evil, from the man who speaks perverse things,",
      "M": "Delivering you from the path of evil and from those who speak twisted things,",
      "T": "It saves you from the road that ends badly, and from the kind of people whose words are bent toward harm."
    },
    "13": {
      "L": "Who leave the paths of uprightness to walk in the ways of darkness,",
      "M": "Who abandon the straight paths and choose to walk in darkness,",
      "T": "They once knew the right way and turned their backs on it, choosing to live in the dark."
    },
    "14": {
      "L": "Who rejoice in doing evil and delight in the perverseness of the wicked,",
      "M": "Who take pleasure in evil and celebrate every kind of wrongdoing,",
      "T": "Darkness is no mere mistake for them — they have learned to enjoy it. Evil is their entertainment."
    },
    "15": {
      "L": "Whose ways are crooked and who are devious in their paths.",
      "M": "Their ways are crooked and their paths are twisted.",
      "T": "Every road they walk bends away from what is good."
    },
    "16": {
      "L": "To deliver you from the strange woman, from the foreigner who flatters with her words,",
      "M": "It will also save you from the immoral woman — from the seductive stranger with her smooth words,",
      "T": "Wisdom will also guard you from the woman who will destroy you — who draws you in with flattery."
    },
    "17": {
      "L": "Who forsakes the companion of her youth and forgets the covenant of her God.",
      "M": "She has abandoned the partner of her youth and forgotten the covenant she made before God.",
      "T": "She walked away from her husband and discarded the oath she swore before God. Loyalty means nothing to her."
    },
    "18": {
      "L": "For her house sinks down to death and her paths to the dead.",
      "M": "For her house leads down to death and her paths go to the spirits of the dead.",
      "T": "Going home with her means one thing: death. The path into her house slopes downward — it only ends one way."
    },
    "19": {
      "L": "None who go to her return, nor do they attain the paths of life.",
      "M": "None who enter her house return; they never find their way back to the paths of life.",
      "T": "This is not something you recover from. Those who take that path do not come back."
    },
    "20": {
      "L": "So that you may walk in the way of the good and keep the paths of the righteous.",
      "M": "All this so that you will walk in the path of the good and stay on the road of the righteous.",
      "T": "The whole point of wisdom's protection is this: to keep you on the right road, among people worth knowing."
    },
    "21": {
      "L": "For the upright will dwell in the land, and those of integrity will remain in it,",
      "M": "For the righteous will live in the land, and those of integrity will remain in it,",
      "T": "Uprightness has a future in this world — the honest, the people of real integrity, they are the ones who last."
    },
    "22": {
      "L": "But the wicked will be cut off from the land, and the treacherous will be rooted out of it.",
      "M": "But the wicked will be cut off from the land, and the unfaithful will be uprooted from it.",
      "T": "But the wicked? They will be removed — not displaced, uprooted. Nothing of them will remain."
    }
  },
  "3": {
    "1": {
      "L": "My son, do not forget my law, but let your heart keep my commandments;",
      "M": "My son, do not forget my instruction, but let your heart hold on to my commands;",
      "T": "My son, don't just hear these words — let them take root in you. Keep them."
    },
    "2": {
      "L": "For length of days and years of life and peace they will add to you.",
      "M": "They will add to you a long life, many years of living, and peace.",
      "T": "Keep them, and your life will be longer than it would have been, richer than you imagined — whole."
    },
    "3": {
      "L": "Let not steadfast love and faithfulness forsake you; bind them about your neck; write them on the tablet of your heart.",
      "M": "Let steadfast love and faithfulness never leave you; wear them like a necklace; inscribe them on your heart.",
      "T": "Covenant love and integrity — do not let them slip away. Tie them around your neck so you carry them wherever you go; carve them into the center of who you are."
    },
    "4": {
      "L": "So you will find favor and good understanding in the sight of God and man.",
      "M": "Then you will find favor and a good reputation in the eyes of God and people.",
      "T": "Live this way and you will have two things money cannot buy: the approval of God and the genuine respect of people."
    },
    "5": {
      "L": "Trust in the LORD with all your heart, and do not lean on your own understanding.",
      "M": "Trust in the LORD with all your heart and do not depend on your own insight.",
      "T": "Give the LORD your complete confidence — not a careful, measured faith but all of you. And let go of the idea that your own reasoning is enough."
    },
    "6": {
      "L": "In all your ways acknowledge him, and he will make your paths straight.",
      "M": "Acknowledge him in everything you do, and he will direct your steps.",
      "T": "In every decision, every road — bring him in. He will clear the way."
    },
    "7": {
      "L": "Be not wise in your own eyes; fear the LORD and depart from evil.",
      "M": "Do not think of yourself as wise; fear the LORD and turn from evil.",
      "T": "The most dangerous posture is to trust your own cleverness. Fear the LORD instead, and make evil something you keep walking away from."
    },
    "8": {
      "L": "It will be healing to your navel and refreshment to your bones.",
      "M": "This will bring health to your whole body and strength to your bones.",
      "T": "Fear of the LORD is not just a spiritual posture — it makes you well. The whole person, body and strength included."
    },
    "9": {
      "L": "Honor the LORD with your substance and with the firstfruits of all your increase;",
      "M": "Honor the LORD with your wealth and with the first portion of all you produce;",
      "T": "The way you use what you own is a statement about what you worship. Honor the LORD first — off the top, before anything else."
    },
    "10": {
      "L": "Then your barns will be filled with plenty, and your vats will burst with new wine.",
      "M": "Then your barns will overflow with abundance and your wine vats will brim with new wine.",
      "T": "The one who gives the LORD his due finds that what remains is more than enough. Abundance follows generosity."
    },
    "11": {
      "L": "My son, do not despise the LORD's discipline, and do not be weary of his correction;",
      "M": "My son, do not reject the LORD's discipline or resent his correction;",
      "T": "My son, when the LORD corrects you — receive it. Do not wave it off. Do not exhaust yourself fighting something he means for your good."
    },
    "12": {
      "L": "For the LORD corrects the one he loves, as a father the son in whom he delights.",
      "M": "For the LORD corrects those he loves, just as a father disciplines the son he takes delight in.",
      "T": "Correction is not rejection — it is what love looks like from above. The LORD disciplines you because you are his, the way a father who loves his child does not let him go wrong without saying something."
    },
    "13": {
      "L": "Happy is the man who finds wisdom, and the man who obtains understanding;",
      "M": "How happy is the person who finds wisdom, the one who gains understanding;",
      "T": "There is no greater happiness than the moment wisdom becomes yours — real wisdom, the kind that reshapes how you see everything."
    },
    "14": {
      "L": "For the gain from her is better than gain from silver, and her profit than fine gold;",
      "M": "Her return is better than the return on silver, and her profit better than fine gold;",
      "T": "Every investment in wisdom pays better than silver. Better than gold. Far better."
    },
    "15": {
      "L": "She is more precious than rubies, and nothing you desire compares with her.",
      "M": "She is more valuable than precious gems; nothing you could want measures up to her.",
      "T": "Whatever you think you most want in life — wisdom is worth more."
    },
    "16": {
      "L": "Length of days is in her right hand; in her left hand are riches and honor.",
      "M": "In her right hand is long life; in her left hand are wealth and honor.",
      "T": "She carries long life in one hand and wealth and honor in the other. She gives both freely — but only to those who pursue her."
    },
    "17": {
      "L": "Her ways are ways of pleasantness, and all her paths are peace.",
      "M": "Her ways are pleasant and all her paths lead to peace.",
      "T": "The life shaped by wisdom is not grinding or austere — it is genuinely good, and the destination is shalom."
    },
    "18": {
      "L": "She is a tree of life to those who lay hold of her, and blessed is everyone who holds her fast.",
      "M": "She is a tree of life to those who grasp her; those who hold on to her are called blessed.",
      "T": "Lady Wisdom is the tree of life — the image from the garden. Those who hold on to her are alive, and they are blessed."
    },
    "19": {
      "L": "The LORD by wisdom founded the earth; by understanding he established the heavens.",
      "M": "By wisdom the LORD laid the foundation of the earth; by understanding he set the heavens in place.",
      "T": "Creation itself was an act of wisdom — the LORD shaped the earth and hung the heavens in their place through the same wisdom he now offers to you."
    },
    "20": {
      "L": "By his knowledge the depths were broken up, and the clouds drop the dew.",
      "M": "Through his knowledge the deep waters opened up and the clouds let fall their dew.",
      "T": "The same knowledge that cracked open the primordial depths and calls the morning dew down from the clouds — that knowledge is what wisdom gives you access to."
    },
    "21": {
      "L": "My son, let them not depart from your eyes; keep sound wisdom and discretion;",
      "M": "My son, keep these in view; hold on to sound wisdom and discernment;",
      "T": "My son, do not let them slip away. Keep proven wisdom and clear judgment always within reach."
    },
    "22": {
      "L": "They will be life for your soul and grace for your neck.",
      "M": "They will bring life to your soul and beauty to your neck.",
      "T": "They give life from the inside out — sustaining your soul and showing in how you carry yourself."
    },
    "23": {
      "L": "Then you will walk in your way safely, and your foot will not stumble.",
      "M": "Then you will go on your way in security, without stumbling.",
      "T": "With wisdom as your guide, you can walk without fear — the path ahead is solid."
    },
    "24": {
      "L": "When you lie down, you will not be afraid; when you lie down, your sleep will be sweet.",
      "M": "When you lie down, you will not be afraid; your sleep will be peaceful.",
      "T": "Rest comes easily to the wise — no fear in the night, sleep that is genuinely restoring."
    },
    "25": {
      "L": "Do not be afraid of sudden terror or of the desolation of the wicked when it comes;",
      "M": "Do not fear sudden catastrophe or the destruction that falls on the wicked;",
      "T": "The sudden disasters that overtake the wicked — they are not your portion. You do not need to live afraid of them."
    },
    "26": {
      "L": "For the LORD will be your confidence and will keep your foot from being caught.",
      "M": "For the LORD will be your security and will keep you from every snare.",
      "T": "The LORD himself is your stability — he watches where your foot falls."
    },
    "27": {
      "L": "Do not withhold good from those to whom it is due, when it is in the power of your hand to do it.",
      "M": "Do not withhold good from those who deserve it when you have the ability to give it.",
      "T": "When you can help someone who needs it, help them. Do not hold back what is genuinely owed."
    },
    "28": {
      "L": "Do not say to your neighbor, 'Go, and come again, tomorrow I will give it,' when you have it with you.",
      "M": "Do not tell your neighbor, 'Come back later — I'll help you tomorrow,' when you can help now.",
      "T": "Do not send someone away with a promise when you could fulfill it today. 'Tomorrow' from someone with the means is just a polite refusal."
    },
    "29": {
      "L": "Do not devise evil against your neighbor, who dwells securely beside you.",
      "M": "Do not plot harm against your neighbor, who lives beside you in trust.",
      "T": "The neighbor who trusts you enough to live beside you — do not take advantage of that trust to harm them."
    },
    "30": {
      "L": "Do not contend with a man without cause, if he has done you no harm.",
      "M": "Do not pick a fight without cause with someone who has done you no harm.",
      "T": "Quarreling for its own sake is a fool's hobby. If someone has not wronged you, let it go."
    },
    "31": {
      "L": "Do not envy the violent man and do not choose any of his ways;",
      "M": "Do not envy the violent person or choose to follow any of his paths;",
      "T": "When a ruthless person seems to prosper — do not let that impress you. Do not envy his results enough to imitate his methods."
    },
    "32": {
      "L": "For the devious is an abomination to the LORD, but with the upright is his secret counsel.",
      "M": "For the LORD detests the devious, but the upright are in his confidence.",
      "T": "The crooked are detestable to the LORD. But the honest? They are admitted to his council — they are the ones he trusts."
    },
    "33": {
      "L": "The LORD's curse is on the house of the wicked, but he blesses the dwelling of the righteous.",
      "M": "The LORD's curse rests on the house of the wicked, but he blesses the home of the righteous.",
      "T": "Two households: one under the LORD's curse, one under his blessing. The difference is not wealth — it is righteousness."
    },
    "34": {
      "L": "Surely he scorns the scorners, but gives grace to the humble.",
      "M": "He mocks the mockers himself, but shows favor to the humble.",
      "T": "The mocker who laughs at wisdom will find that God laughs at him. But those who come with humility — he meets them with grace."
    },
    "35": {
      "L": "The wise will inherit glory, but fools get shame.",
      "M": "The wise will inherit honor, but fools are left with disgrace.",
      "T": "Wisdom leads to glory; foolishness leads to shame. That is the summary of the whole matter."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 1–3 written.')

if __name__ == '__main__':
    main()
