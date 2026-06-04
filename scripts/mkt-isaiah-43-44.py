"""
MKT Isaiah chapters 43–44 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-43-44.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers — consistent with prior Isaiah scripts.
- H7307 (רוּחַ): 44:3 "my Spirit" (uppercase, all tiers) — context is unambiguously the divine
  Spirit of Yahweh poured out on Israel's offspring; divine agency is explicit.
- H1350 (גָּאַל): "redeemed" / "Redeemer" — covenantal kinsman-redeemer language; the
  obligation-bound relative who buys back what was lost; distinct from H6299 (פָּדָה, "ransom").
- H5315 (נֶפֶשׁ): 43:4 "life" — the exchange is for Israel's persons/lives, not immaterial souls;
  rendered "life" (L/M) and "life" (T) consistently with context.
- H6588 (פֶּשַׁע): "transgressions" (L/M) / "rebellions" (T) — willful covenant violation; T
  uses "rebellions" to surface the defiance inherent in the word.
- H2403 (חֵטְא): "sins" throughout — the default moral failure word.
- H5771 (עָוֹן): "iniquities" (L/M) / "guilt" (T) — accumulated moral debt; T uses "guilt"
  to surface the weight-bearing connotation.
- H6459 (פֶּסֶל): "graven image" (L, traditional) / "carved idol" (M) / "idol" (T) —
  the hand-carved cult object; L retains the older English rendering to mark the category.
- H8414 (תֹּהוּ): 44:9 "nothing" / "worthless" / "futile" — the same root as Gen 1:2 "formless
  void"; the idols share the character of pre-creation chaos; T makes this connection explicit.
- H3484 (יְשֻׁרוּן): 44:2 "Jeshurun" — a term of endearment for Israel, root probably "upright";
  retained as a proper name in all tiers; rare (Deut 32:15; 33:5, 26; Isa 44:2 only).
- H5650 (עֶבֶד): "servant" throughout — Israel as covenant servant; consistent with all prior
  Isaiah scripts.
- H1254 (בָּרָא): 44:24 "made" (L/M) — the verb used exclusively of God's creative act; T
  makes the uniqueness explicit with "by myself."
- H3335 (יָצַר): "formed" throughout — the potter-image, God shaping from the inside; distinct
  from בָּרָא but used in synonymous parallelism.
- H7462 (רָעָה): 44:28 "shepherd" — Cyrus as Yahweh's shepherd is a deliberate inversion of
  normal imagery; a pagan king serves as God's instrument; T makes the theological weight plain.
- H3887 (מֵלִיץ): 43:27 "spokesmen" (L) / "intermediaries" (M) / "representatives" (T) —
  the term covers prophets, priests, court mediators; "representatives" surfaces the full range.
- 43:13 — "From eternity / before the day was" (H3117 yom): the Hebrew is terse; the sense is
  God's eternal priority before created time; L = "from eternity," T makes this explicit.
- 43:14 — The Chaldean "cry" in their ships: the Hebrew "their shout of joy" refers to their
  boasting pride in their fleet; as Yahweh drives them down as fugitives, that pride becomes
  lamentation; T renders the ironic reversal.
- 43:27 — "Your first father sinned": traditionally Jacob/Israel the patriarch (or even Adam);
  the point is the unbroken chain of covenant failure from the very beginning.
- 43:28 — "princes of the sanctuary": temple officials whose dignity Yahweh strips away as
  judgment on corporate sin; part of the covenant lawsuit closure.
- 44:28 — Cyrus by name: naming a specific foreign king ~150 years before his birth is one of
  Isaiah's most striking prophecies (Cyrus reigned c. 559–530 BCE). The T tier renders this
  with the theological weight the text intends — Yahweh's sovereignty over history naming the
  very instrument of Israel's release before he exists.
- Poetry/prose: Both ch. 43 and ch. 44:1-8, 21-28 are prophetic poetry; T uses line breaks.
  Ch. 44:9-20 (the idol-maker satire) is satirical prose-poetry; T retains prose but with
  heightened ironic edge — the deadpan observation is part of the rhetoric.
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

ISAIAH = {
  "43": {
    "1": {
      "L": "But now, thus says the LORD who created you, O Jacob, and he who formed you, O Israel: Fear not, for I have redeemed you; I have called you by your name — you are mine.",
      "M": "But now, this is what the LORD says — he who created you, Jacob, and formed you, Israel: 'Do not be afraid, for I have redeemed you; I have called you by name — you are mine.'",
      "T": "But now — hear this, Jacob;\nlisten, Israel, whom God formed:\nDo not be afraid.\nI have redeemed you.\nI called you by your own name —\nyou are mine."
    },
    "2": {
      "L": "When you pass through the waters, I will be with you; and through the rivers, they shall not overflow you. When you walk through the fire, you shall not be burned; and the flame shall not kindle upon you.",
      "M": "When you pass through the waters, I will be with you; through the rivers, they will not overwhelm you. When you walk through the fire, you will not be scorched; the flame will not set you ablaze.",
      "T": "When you wade through the waters, I will be there;\nthe rivers will not sweep you away.\nWhen you walk through the fire,\nyou will not be burned —\nnot a flame will touch you."
    },
    "3": {
      "L": "For I am the LORD your God, the Holy One of Israel, your Savior. I give Egypt as your ransom, Ethiopia and Seba in exchange for you.",
      "M": "For I am the LORD your God, the Holy One of Israel, your Savior. I give Egypt as your ransom, Ethiopia and Seba in your place.",
      "T": "For I am Yahweh your God,\nthe Holy One of Israel — your Savior.\nI give Egypt as the price of your rescue,\nEthiopia and Seba in exchange for you."
    },
    "4": {
      "L": "Because you were precious in my sight, and honorable, and I have loved you, therefore I give men in return for you, and peoples in exchange for your life.",
      "M": "Because you are precious in my eyes and honored, and because I love you, I will give people in exchange for you, nations in place of your life.",
      "T": "Because you are precious to me,\nbecause I hold you in honor,\nbecause I love you —\nI will give up whole nations for you,\npeoples in exchange for your life."
    },
    "5": {
      "L": "Fear not, for I am with you; I will bring your offspring from the east, and I will gather you from the west.",
      "M": "Do not be afraid, for I am with you. I will bring your offspring from the east and gather you from the west.",
      "T": "Do not be afraid — I am with you.\nI will bring your children back from the east\nand gather you from the west."
    },
    "6": {
      "L": "I will say to the north, Give them up! and to the south, Do not withhold; bring my sons from far away and my daughters from the ends of the earth,",
      "M": "I will say to the north, 'Give them back!' and to the south, 'Do not hold them back.' Bring my sons from far away, my daughters from the ends of the earth —",
      "T": "I will command the north: Let them go!\nI will tell the south: Don't hold them back!\nBring my sons from far away —\nbring my daughters from the ends of the earth —"
    },
    "7": {
      "L": "everyone who is called by my name, whom I have created for my glory, whom I have formed, indeed whom I have made.",
      "M": "everyone who bears my name, whom I created for my glory, whom I formed and made.",
      "T": "everyone who carries my name,\neveryone I created for my glory,\neveryone I formed and made."
    },
    "8": {
      "L": "Bring out the people who are blind, even though they have eyes, and the deaf, even though they have ears.",
      "M": "Bring out the people who are blind — though they have eyes — and those who are deaf — though they have ears!",
      "T": "Bring out the people who have eyes but cannot see,\nwho have ears but cannot hear."
    },
    "9": {
      "L": "Let all the nations be gathered together, and let the peoples be assembled. Who among them can declare this, and show us former things? Let them bring forth their witnesses to justify themselves, or let them hear and say, It is truth.",
      "M": "Let all the nations gather together; let the peoples assemble. Who among them declared this, or foretold us what has happened before? Let them bring their witnesses to prove themselves right — or let them hear and say, 'It is true.'",
      "T": "Let every nation gather,\nlet every people assemble.\nWho among them predicted this?\nWho announced what came before?\nLet them bring their witnesses to make their case —\nor let them hear and admit: it is true."
    },
    "10": {
      "L": "You are my witnesses, declares the LORD, and my servant whom I have chosen, so that you may know and believe me and understand that I am he. Before me no god was formed, nor shall there be any after me.",
      "M": "'You are my witnesses,' declares the LORD, 'along with my servant whom I have chosen — so that you may know and believe me and understand that I am the one. Before me no god was formed, and after me there will be none.'",
      "T": "'You are my witnesses,' declares Yahweh —\n'you and my servant whom I chose —\nso that you would know this, trust this, understand:\nI am the one.\nBefore me there was no god formed;\nafter me — none.'"
    },
    "11": {
      "L": "I, even I, am the LORD, and besides me there is no savior.",
      "M": "I, I am the LORD, and apart from me there is no savior.",
      "T": "I — I alone — am Yahweh.\nApart from me, there is no one who saves."
    },
    "12": {
      "L": "I have declared and have saved and have shown, when there was no strange god among you; and you are my witnesses, declares the LORD, and I am God.",
      "M": "I declared, I saved, and I proclaimed — when there was no foreign god among you. 'You are my witnesses,' declares the LORD, 'and I am God.'",
      "T": "I was the one who declared it.\nI was the one who saved.\nI proclaimed it —\nwhen no foreign god was among you.\n'You are my witnesses,' declares Yahweh.\n'And I am God.'"
    },
    "13": {
      "L": "Yes, from eternity I am he; and there is none who can deliver from my hand. I work, and who shall reverse it?",
      "M": "Even from eternity I am he. No one can deliver from my hand. When I act, who can reverse it?",
      "T": "Before created time began, I was.\nNo one can snatch anything from my hand.\nWhen I act — who undoes what I do?"
    },
    "14": {
      "L": "Thus says the LORD, your Redeemer, the Holy One of Israel: For your sake I have sent to Babylon and will bring them all down as fugitives — the Chaldeans — in the ships which were their boast.",
      "M": "This is what the LORD says — your Redeemer, the Holy One of Israel: 'For your sake I am sending against Babylon and will bring down all of them as fugitives — even the Chaldeans — in the ships that were once their pride.'",
      "T": "Here is what Yahweh says —\nyour Redeemer, the Holy One of Israel:\n'For your sake I have sent against Babylon\nand will drive all the Chaldeans down as refugees —\ninto the very ships they once prided themselves on.'"
    },
    "15": {
      "L": "I am the LORD, your Holy One, the Creator of Israel, your King.",
      "M": "I am the LORD, your Holy One, Israel's Creator, your King.",
      "T": "I am Yahweh, your Holy One,\nCreator of Israel,\nyour King."
    },
    "16": {
      "L": "Thus says the LORD, who makes a way through the sea and a path through the mighty waters,",
      "M": "This is what the LORD says — he who makes a way through the sea and a path through the mighty waters,",
      "T": "Here is what Yahweh says —\nhe who once opened a road through the sea\nand a path through the raging waters,"
    },
    "17": {
      "L": "who brings out chariot and horse, army and warrior together; they lie down, they cannot rise; they are extinguished, quenched like a wick:",
      "M": "who brought out chariot and horse, army and warrior together — they lay down and could not rise; they were extinguished, quenched like a wick:",
      "T": "who drove out chariot and horse,\narmy and champion together —\nthey lay down and could not rise again,\nsnuffed out like a burning wick:"
    },
    "18": {
      "L": "Do not remember the former things, and do not consider the things of old.",
      "M": "'Do not remember the former things, or consider the events of long ago.'",
      "T": "'Stop dwelling on what happened before.\nStop thinking about the old days.'"
    },
    "19": {
      "L": "Behold, I am doing a new thing; now it springs forth — do you not perceive it? I will make a way in the wilderness and rivers in the desert.",
      "M": "'Look — I am doing something new; even now it springs up. Do you not see it? I am making a way in the wilderness and rivers in the desert.'",
      "T": "'Look — I am doing something completely new.\nEven now it is breaking through — do you see it?\nI am opening a road through the wilderness\nand rivers through the barren desert.'"
    },
    "20": {
      "L": "The wild beasts will honor me — the jackals and the ostriches — because I give water in the wilderness and rivers in the desert, to give drink to my chosen people,",
      "M": "The wild animals will honor me — the jackals and the ostriches — because I provide water in the wilderness and rivers in the desert, to give drink to my chosen people,",
      "T": "Even the wild animals will honor me —\nthe desert jackals and the ostriches —\nbecause I bring water into the wilderness\nand rivers into the desert,\nto quench the thirst of my chosen people,"
    },
    "21": {
      "L": "the people whom I formed for myself, that they would declare my praise.",
      "M": "the people I formed for myself, that they might declare my praise.",
      "T": "the people I shaped for myself —\nso they would tell everyone what I have done."
    },
    "22": {
      "L": "Yet you have not called upon me, O Jacob; surely you have grown weary of me, O Israel.",
      "M": "Yet, Jacob, you have not called on me; you have grown weary of me, O Israel.",
      "T": "And yet, Jacob — you never called on me.\nIsrael — you grew tired of me."
    },
    "23": {
      "L": "You have not brought me the sheep of your burnt offerings, and with your sacrifices you have not honored me. I have not burdened you with offerings, nor wearied you with incense.",
      "M": "You have not brought me sheep for burnt offerings, and your sacrifices have not honored me. I have not burdened you with grain offerings or wearied you with incense.",
      "T": "You brought me no sheep for burnt offerings.\nYour sacrifices brought me no honor.\nI never loaded you down with offerings —\nnever wore you out with demands for incense."
    },
    "24": {
      "L": "You have not bought me sweet cane with money, nor have you satisfied me with the fat of your sacrifices; but you have burdened me with your sins and wearied me with your iniquities.",
      "M": "You have not bought me fragrant calamus with money, nor have you satisfied me with the fat of your sacrifices. But you have burdened me with your sins and wearied me with your iniquities.",
      "T": "You spent no silver to buy me sweet cane;\nyou did not satisfy me with the fat of your offerings.\nBut you have loaded me down with your sins —\nworn me out with your rebellions."
    },
    "25": {
      "L": "I, even I, am he who blots out your transgressions for my own sake, and I will not remember your sins.",
      "M": "I, I am the one who blots out your transgressions for my own sake, and I will not remember your sins.",
      "T": "And yet — I, I myself am the one\nwho wipes away your rebellions —\nfor my own sake, not yours.\nI will not hold your sins against you."
    },
    "26": {
      "L": "Put me in remembrance; let us argue together; set forth your case, that you may be declared right.",
      "M": "Put me in remembrance; let us argue the matter together. Present your case, that you may be proved innocent.",
      "T": "Remind me, then — let us take this to court.\nPresent your case.\nMake your argument.\nSee if you can be acquitted."
    },
    "27": {
      "L": "Your first father sinned, and your spokesmen have transgressed against me.",
      "M": "Your first ancestor sinned, and your intermediaries have rebelled against me.",
      "T": "Your first father sinned.\nEvery representative you ever had has betrayed me."
    },
    "28": {
      "L": "So I profaned the princes of the sanctuary, and I delivered Jacob to the ban of destruction and Israel to reviling.",
      "M": "So I allowed the sanctuary's leaders to be defiled, and I gave Jacob over to destruction and Israel to scorn.",
      "T": "So I stripped the sanctuary's leaders of their dignity\nand gave Jacob over to total destruction —\nIsrael to contempt and insult."
    }
  },
  "44": {
    "1": {
      "L": "Yet now hear, O Jacob my servant, and Israel whom I have chosen.",
      "M": "But now listen, Jacob my servant — Israel, whom I have chosen!",
      "T": "Even so — listen now, Jacob my servant.\nIsrael — you whom I chose — hear this."
    },
    "2": {
      "L": "Thus says the LORD who made you, who formed you from the womb and will help you: Fear not, O Jacob my servant, and you, Jeshurun, whom I have chosen.",
      "M": "This is what the LORD says — he who made you, who formed you in the womb, and who will help you: 'Do not be afraid, Jacob my servant, Jeshurun whom I have chosen.'",
      "T": "Here is what Yahweh says —\nhe who made you, who shaped you before you were born,\nwho will sustain you:\n'Do not fear, Jacob my servant,\nJeshurun whom I chose.'"
    },
    "3": {
      "L": "For I will pour water on the thirsty land and streams on the dry ground; I will pour out my Spirit upon your offspring and my blessing upon your descendants.",
      "M": "For I will pour water on the thirsty land and streams on the dry ground; I will pour out my Spirit on your offspring, and my blessing on your children.",
      "T": "For I will pour water on the parched land\nand floods on the dry ground.\nI will pour out my Spirit on your children —\nmy blessing on those who come after you."
    },
    "4": {
      "L": "And they will spring up among the grass, as willows by streams of water.",
      "M": "They will spring up among the grass like willows beside flowing streams.",
      "T": "They will rise up like grass in a meadow,\nlike willows planted by running water."
    },
    "5": {
      "L": "One will say, I am the LORD's; another will call himself by the name of Jacob; and another will write on his hand, The LORD's, and will surname himself by the name of Israel.",
      "M": "One will say, 'I belong to the LORD,' and another will take the name Jacob as his own. One will write on his hand, 'The LORD's,' and will be called by the name of Israel.",
      "T": "One person will say, 'I belong to Yahweh.'\nAnother will take on the name of Jacob.\nAnother will write on his hand: 'Yahweh's' —\nand adopt the name Israel as his own."
    },
    "6": {
      "L": "Thus says the LORD, the King of Israel and his Redeemer, the LORD of hosts: I am the first and I am the last; and besides me there is no God.",
      "M": "This is what the LORD says — Israel's King and Redeemer, the LORD of hosts: 'I am the first and I am the last; apart from me there is no God.'",
      "T": "Here is what Yahweh says —\nIsrael's King and Kinsman-Redeemer,\nYahweh of armies:\n'I am the first. I am the last.\nBetween those two, there is no other God.'"
    },
    "7": {
      "L": "Who is like me? Let him proclaim it. Let him declare it and set it in order for me — since I appointed the ancient people. And let them declare what will happen, and the things that are coming.",
      "M": "Who is like me? Let him come forward, announce it, and lay it out before me. Who has declared from of old what is to come, since I established the ancient people? Let them tell us what lies ahead.",
      "T": "Who is my equal? Let him step forward and say so.\nLet him declare and set it out before me:\nwho has announced events from the beginning,\nas I have since I first set this people in place?\nLet them tell what is coming — what is still ahead."
    },
    "8": {
      "L": "Fear not, nor be dismayed. Have I not told you from of old and declared it? You are my witnesses. Is there a God besides me? There is no Rock; I know not any.",
      "M": "Do not tremble, do not be afraid. Did I not tell you long ago and declare it? You are my witnesses: is there any God apart from me? There is no Rock — I know of none.",
      "T": "Do not tremble. Do not be afraid.\nHave I not been saying this all along —\ndeclaring it from the beginning?\nYou yourselves are my witnesses:\nIs there any God besides me?\nThere is no Rock — none that I know of."
    },
    "9": {
      "L": "All who fashion idols are nothing, and the things they delight in do not profit; their witnesses neither see nor know, so that they will be put to shame.",
      "M": "All who fashion idols are worthless, and the things they prize are of no use. Their own witnesses can neither see nor know — so they will be put to shame.",
      "T": "All idol-makers amount to nothing.\nThe things they prize so highly — useless, every one.\nTheir own witnesses are blind and ignorant.\nThey will be disgraced."
    },
    "10": {
      "L": "Who fashions a god or casts a metal image that is profitable for nothing?",
      "M": "Who would shape a god or cast a metal idol that profits him nothing?",
      "T": "Who would go to the trouble of shaping a god — casting a metal image that does nothing for anyone?"
    },
    "11": {
      "L": "Behold, all his companions will be put to shame, and the craftsmen who are only human. Let them all assemble together, let them stand up; they will tremble, they will be disgraced together.",
      "M": "Look — all his associates will be put to shame, and the craftsmen are, after all, only human. Let them assemble together and stand up; they will be terrified and shamed together.",
      "T": "All who are part of this trade will be shamed. The craftsmen who make idols — they are only human. Let them all come together and take a stand. They will be terrified. They will be disgraced. Every last one."
    },
    "12": {
      "L": "The ironsmith fashions it, working over the coals with his tools; he shapes it with hammers and works it with his strong arm. He grows hungry and his strength fails; he drinks no water and becomes faint.",
      "M": "The blacksmith works the iron over burning coals; he beats it into shape with hammers, forging it with his strong arm. But he grows hungry and loses his strength; if he drinks no water, he grows faint.",
      "T": "The blacksmith heats the iron in his forge, beats it into shape with his hammer, works it with his powerful arms. But he grows hungry and loses his strength. If he forgets to drink, he faints."
    },
    "13": {
      "L": "The carpenter stretches out a measuring line; he marks it out with a stylus. He works it with planes and marks it with a compass. He shapes it into the form of a man, with the beauty of a man, to remain in a house.",
      "M": "The carpenter measures the wood with a line; he draws an outline with chalk. He shapes it with chisels and marks it with a compass, carving it into the shape of a man — a handsome human figure — to be set up in a house.",
      "T": "The carpenter takes his measuring line, chalks it out, works the wood with chisels, traces curves with his compass — and slowly it takes the form of a person, a beautiful human figure, to be placed inside a house."
    },
    "14": {
      "L": "He cuts down cedars for himself; he takes a cypress or an oak, and he lets them grow strong among the trees of the forest. He planted a cedar and the rain nourished it.",
      "M": "He cuts down cedars; he selects a cypress or an oak and lets it grow strong among the trees of the forest. He planted it, and the rain made it grow.",
      "T": "He goes out and cuts down cedars — or chooses a cypress, an oak — lets them grow strong in the forest. He planted it. The rain made it grow."
    },
    "15": {
      "L": "Then it serves as fuel for a man. He takes part of it and warms himself; he kindles a fire and bakes bread. Also he makes a god and worships it; he makes it a carved idol and bows down before it.",
      "M": "Then the wood serves as fuel for the man. He burns part of it to warm himself; he kindles a fire and bakes bread. But he also fashions a god from it and worships it — carves an idol and bows down to it.",
      "T": "Then that same tree becomes his fuel. He burns part of it. Warms himself. Bakes his bread. And then — with another piece — he carves a god. He bows down to it. He worships it."
    },
    "16": {
      "L": "Half of it he burns in the fire; over the embers he roasts meat and eats. He warms himself and says, Aha, I am warm; I have seen the fire.",
      "M": "Half of it he burns in the fire; over the coals he roasts meat, eats his fill, and warms himself, saying, 'Aha, I am warm; I can feel the heat.'",
      "T": "Half he burns in the fire. Over the coals he roasts his meat, eats his fill. He warms himself and says, 'Good — I can feel the warmth of the fire.'"
    },
    "17": {
      "L": "And the rest of it he makes into a god, his idol, and bows down to it and worships it. He prays to it and says, Deliver me, for you are my god.",
      "M": "But the rest of the wood he makes into his god, into a carved image, and bows down to it and worships it. He prays to it and says, 'Save me — you are my god.'",
      "T": "And then, with what is left, he makes his god — a carved image. He bows down to it. He worships it. He prays to it: 'Save me — you are my god!'"
    },
    "18": {
      "L": "They do not know, nor do they understand, for their eyes are smeared over so that they cannot see, and their hearts, so that they cannot comprehend.",
      "M": "They have no knowledge or understanding; their eyes are plastered shut so they cannot see, and their minds are closed so they cannot grasp it.",
      "T": "They do not know. They do not understand. Their eyes have been sealed shut so they cannot see. Their hearts have been closed so they cannot grasp what they are doing."
    },
    "19": {
      "L": "And no one takes it to heart; there is neither knowledge nor understanding to say: Half of it I burned in the fire; I also baked bread over its coals; I roasted meat and ate it. And shall I make the rest an abomination? Shall I bow down to a piece of wood?",
      "M": "No one stops to think; no one has the knowledge or insight to say: 'Half of this I burned — I even baked bread over its coals; I roasted meat and ate it. Should I really make an abomination out of what is left? Should I bow down to a block of wood?'",
      "T": "No one pauses to think. No one has the insight or the will to say: 'I just burned half this tree to roast my dinner — baked bread on its coals, ate my fill. And now I am going to make the rest into an idol? Bow down to a piece of wood?'"
    },
    "20": {
      "L": "He feeds on ashes; a deluded heart has led him astray. He cannot deliver his soul, nor can he say, Is there not a lie in my right hand?",
      "M": "He is feeding on ashes; a deceived mind has led him astray. He cannot save himself or bring himself to say, 'Is this thing in my hand not a fraud?'",
      "T": "He is eating ashes and doesn't know it. A deceived heart has led him off the path. He cannot rescue himself — cannot ask the honest question: 'Is what I am holding in my hand a lie?'"
    },
    "21": {
      "L": "Remember these things, O Jacob, and O Israel, for you are my servant. I have formed you; you are my servant. O Israel, you will not be forgotten by me.",
      "M": "Remember all this, Jacob and Israel, for you are my servant. I formed you; you are my servant. Israel, I will not forget you.",
      "T": "Remember all this, Jacob.\nKeep it in mind, Israel —\nyou are my servant.\nI formed you. You belong to me.\nIsrael — I will not forget you."
    },
    "22": {
      "L": "I have blotted out your transgressions like a thick cloud, and your sins like a cloud. Return to me, for I have redeemed you.",
      "M": "I have swept away your transgressions like a cloud, your sins like morning mist. Return to me, for I have redeemed you.",
      "T": "I have swept your rebellions away like a morning mist —\nyour sins like a cloud scattered by the wind.\nReturn to me —\nfor I have redeemed you."
    },
    "23": {
      "L": "Sing, O heavens, for the LORD has done it! Shout, O depths of the earth! Break forth into singing, O mountains, O forest, and every tree in it! For the LORD has redeemed Jacob and will glorify himself in Israel.",
      "M": "Shout for joy, O heavens, for the LORD has done it! Shout aloud, O depths of the earth! Burst into song, O mountains, O forest, every tree in it! For the LORD has redeemed Jacob and displays his glory in Israel.",
      "T": "Heavens, shout for joy — Yahweh has done it!\nEarth, shout from your depths!\nMountains, forests, every tree — break into singing!\nFor Yahweh has redeemed Jacob\nand shown his glory in Israel."
    },
    "24": {
      "L": "Thus says the LORD, your Redeemer, and he who formed you from the womb: I am the LORD who made all things, who alone stretched out the heavens, who spread out the earth — by myself,",
      "M": "This is what the LORD says — your Redeemer, who formed you in the womb: 'I am the LORD who made all things; I alone stretched out the heavens; by myself I spread out the earth —'",
      "T": "Here is what Yahweh says —\nyour Redeemer, who shaped you before birth:\n'I am Yahweh, maker of all things.\nI alone stretched out the sky.\nI spread out the earth — by myself —'"
    },
    "25": {
      "L": "who frustrates the signs of false prophets and makes diviners look foolish, who turns the wise backward and makes their knowledge into folly,",
      "M": "who thwarts the omens of impostors and makes fools of diviners, who turns back the wise and makes their knowledge into nonsense,",
      "T": "'who exposes the signs of charlatans as frauds,\nwho makes diviners look foolish,\nwho reverses the thinking of the wise\nand reduces their knowledge to nonsense,'"
    },
    "26": {
      "L": "who confirms the word of his servant and fulfills the counsel of his messengers, who says of Jerusalem, She shall be inhabited, and of the cities of Judah, They shall be rebuilt, and I will raise up their ruins,",
      "M": "who fulfills the word of his servant and carries out the plan of his messengers, who says about Jerusalem, 'It will be inhabited,' and about the towns of Judah, 'They will be rebuilt, and I will raise up their ruins,'",
      "T": "'who confirms every word my servant has spoken,\nwho carries out every plan my messengers have declared —\nwho says of Jerusalem: it will be lived in again;\nwho says of the cities of Judah: they will be rebuilt;\nwho says of their ruins: I will raise them up,'"
    },
    "27": {
      "L": "who says to the deep, Be dried up! and I will dry up your rivers,",
      "M": "who commands the ocean depths, 'Dry up!' and says to the rivers, 'I will make you run dry,'",
      "T": "'who says to the deep: Dry up!\nwho says to the rivers: I will drain you dry,'"
    },
    "28": {
      "L": "who says of Cyrus, He is my shepherd, and he shall fulfill all my purpose, saying of Jerusalem, She shall be built, and of the temple, Your foundation shall be laid.",
      "M": "who says of Cyrus, 'He is my shepherd; he will carry out everything I want him to do,' who says of Jerusalem, 'She will be rebuilt,' and of the temple, 'Your foundation will be laid.'",
      "T": "'who says of Cyrus: he is my shepherd —\nhe will carry out everything I intend.\nHe will say of Jerusalem: rebuild it.\nHe will say of the temple: lay its foundation.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 43–44 written.')

if __name__ == '__main__':
    main()
