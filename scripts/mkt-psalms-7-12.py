"""
MKT Psalms chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-7-12.py

Psalms context: These six psalms span lament (7, 9, 10, 12), hymn (8), and trust (11).
They are all attributed to David in their superscriptions. Psalms 9 and 10 form a
connected acrostic in Hebrew (aleph-bet split across both psalms). The interlinear
includes superscription content within v1 for all six psalms.

Translation decisions:

- H3068 (יהוה): "LORD" in L/M; "LORD" in T. The divine name is rendered with small-caps
  convention throughout all tiers — the personal covenant name is too theologically
  significant to substitute or paraphrase.

- H430 (אֱלֹהִים): "God" across all tiers. The generic term for deity; no ambiguity in
  these psalms that requires "gods" or "divine beings."

- H5315 (נֶפֶשׁ): "soul" in L; "soul" or "life" in M depending on context; "life/self/being"
  in T when the physical/embodied sense is primary. In Ps 7:2 "soul" = the psalmist's life
  being threatened, rendered "life" in T for clarity. In Ps 7:5, context is physical threat,
  so "life" in T.

- H2617 (חֶסֶד): Does not appear in these psalms, but חָסִיד (hasid, "godly/faithful/loyal")
  appears in Ps 12:1. Rendered "godly" in L/M and "person of integrity/faithfulness" in T.

- H6664/H6666 (צֶדֶק/צְדָקָה) and H6663 (צָדַק): "righteousness/righteous" in L/M;
  "justice/righteous/just" in T depending on legal or moral register.

- H7307 (רוּחַ): Does not appear in these psalms.

- Selah (H5542): Retained as "Selah" in L and M. In T, rendered "Selah" with a brief
  gloss in Ps 9:16 only (where "Higgaion. Selah" appears) since Higgaion is obscure.

- Superscriptions: Included within v1 (as the interlinear presents them). L renders
  them in plain transliteration/translation. M includes them with contextual notation.
  T integrates them as a brief orienting header line, then blank line before the poem.

- Poetry line structure in T: Each parallel colon in synonymous/antithetical parallelism
  is separated by \n. Single-line verses where both cola belong to one thought may remain
  as one sentence.

- H7451 (רַע) / H7564 (רִשְׁעָה): "evil/wickedness" — "wicked" in L/M; "wicked/evil"
  maintained in T; no flattening to "bad."

- H6041 (עָנִי) / H34 (אֶבְיוֹן): "poor/afflicted/needy" — both rendered to distinguish
  in L; "poor" and "needy" in M; in T, "the poor," "the powerless," "the helpless" as
  context warrants.

- Psalm 8 anthropology: H120 (אָדָם) and H1121 (בֵּן) combined as "what is man... son of
  man" — preserved in L/M; T unpacks the meditation on human insignificance-yet-dignity.

- Psalm 8:5 — H430 (אֱלֹהִים) in "made him a little lower than אֱלֹהִים": could be "God,"
  "angels," or "heavenly beings." LXX reads "angels"; Hebrews 2:7 quotes it of Christ.
  L/M use "heavenly beings" to preserve ambiguity; T uses "the divine" to honor both
  readings.

- Psalm 10: A lament without a superscription (continues the acrostic from Ps 9). The
  Hebrew alphabet acrostic explains the somewhat fragmented structure of Ps 10 — each
  section begins with the next letter. Noted but not marked in the text.

- Psalm 12:1 — H4100 (מִי) / faithfulness context: "the godly man" (H2623, חָסִיד)
  ceases / the faithful (H530, אֱמוּנָה) disappear — both have covenant-loyalty overtones
  beyond generic morality. T reflects "the covenant-faithful" and "the loyal."

- OT quotation: Psalm 8 is cited in Heb 2:6-8 and 1 Cor 15:27. The translation preserves
  "son of man" (H1121 + H120 = "son of adam") in L; M uses "human being"; T uses "mortals"
  for the humility aspect.
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


PSALMS = {
  "7": {
    "1": {
      "L": "A Shiggaion of David, which he sang to the LORD, concerning the words of Cush the Benjaminite. O LORD my God, in you I take refuge; save me and deliver me from all who pursue me,",
      "M": "A Shiggaion of David, sung to the LORD concerning Cush the Benjaminite. O LORD my God, in you I take refuge; save me and deliver me from all my pursuers,",
      "T": "A Shiggaion — a passionate lament — that David sang to the LORD, prompted by the accusations of Cush the Benjaminite.\n\nO LORD, you are my God. I run to you for shelter. Save me. Rescue me from everyone who is hunting me down."
    },
    "2": {
      "L": "lest like a lion they tear my soul, rending it in pieces, with none to deliver.",
      "M": "lest they tear my soul apart like a lion, mauling it with no one to rescue.",
      "T": "If you don't act, my life is finished —\nthey will rip it open like a lion shreds its prey,\nand no one will be there to pull me free."
    },
    "3": {
      "L": "O LORD my God, if I have done this, if there is iniquity in my hands,",
      "M": "O LORD my God, if I have done this — if there is guilt on my hands —",
      "T": "LORD my God, here is my oath: if I have done what they claim, if my hands carry any such guilt —"
    },
    "4": {
      "L": "if I have repaid evil to him who was at peace with me, or plundered my enemy without cause —",
      "M": "if I have repaid evil to one who was at peace with me, or stripped my enemy without cause —",
      "T": "if I have betrayed a friend who trusted me, if I have plundered someone who had done me no harm —"
    },
    "5": {
      "L": "let the enemy pursue my soul and overtake it, and let him trample my life to the ground and lay my glory in the dust. Selah",
      "M": "then let the enemy pursue and overtake me, trample my life into the ground, and lay my honor in the dust. Selah",
      "T": "then let my enemies catch me.\nLet them grind my life into the dirt.\nLet everything I stand for be buried in the dust. Selah"
    },
    "6": {
      "L": "Arise, O LORD, in your anger; lift yourself up against the fury of my enemies. Awake for me — you have commanded judgment!",
      "M": "Rise up, O LORD, in your anger; rouse yourself against the rage of my enemies. Bestir yourself — you have decreed judgment!",
      "T": "Rise up, LORD! Let your anger do what it must.\nStand against my enemies' rage.\nYou are the one who has decreed justice — now see it through!"
    },
    "7": {
      "L": "Let the assembly of the peoples surround you; and over them return on high.",
      "M": "Let the assembly of the peoples gather around you, and take your seat on high above them.",
      "T": "Let the nations assemble in your court.\nThen take your throne above them all."
    },
    "8": {
      "L": "The LORD judges the peoples; judge me, O LORD, according to my righteousness and according to my integrity within me.",
      "M": "The LORD judges the peoples; vindicate me, O LORD, according to my righteousness and the integrity that is in me.",
      "T": "You are the judge of every nation — judge me too, LORD,\nby the measure of my righteousness, by the integrity you know is in me."
    },
    "9": {
      "L": "Let the evil of the wicked come to an end, but establish the righteous; for the righteous God tests hearts and minds.",
      "M": "Let the wickedness of the wicked come to an end and establish the righteous, for the righteous God searches hearts and minds.",
      "T": "Bring the wicked's career of evil to its end.\nBut let the righteous stand firm.\nYou are the God who searches inward — every heart, every motive — and you are just."
    },
    "10": {
      "L": "My shield is God Most High, who saves the upright in heart.",
      "M": "My shield is God, the Most High, who saves those who are upright in heart.",
      "T": "God himself — the Most High — is the shield that covers me,\nthe one who rescues every honest soul."
    },
    "11": {
      "L": "God is a righteous judge, and a God who feels indignation every day.",
      "M": "God is a righteous judge, a God who expresses indignation every day.",
      "T": "God is a judge — a just one.\nEvery single day, wickedness provokes his righteous anger."
    },
    "12": {
      "L": "If one does not repent, God will whet his sword; he has bent and strung his bow.",
      "M": "If a man does not repent, God will sharpen his sword; he has bent his bow and strung it.",
      "T": "He has sharpened his sword.\nHe has bent the bow and set the string.\nHe waits — but if the wicked will not turn, he is ready."
    },
    "13": {
      "L": "He has prepared his deadly weapons; he makes his arrows into fiery shafts.",
      "M": "He has prepared deadly weapons against the persecutors; his arrows will be fiery shafts.",
      "T": "His arsenal is stocked — weapons made for the kill.\nHis arrows are aflame, aimed at those who drive others down."
    },
    "14": {
      "L": "Behold, the wicked one conceives evil, is pregnant with trouble, and gives birth to lies.",
      "M": "Look: the wicked person conceives evil, becomes pregnant with mischief, and gives birth to deception.",
      "T": "Watch how the wicked work:\nThey conceive their scheme, carry it to term,\nand what they finally deliver is one more lie."
    },
    "15": {
      "L": "He dug a pit and hollowed it out, and fell into the hole he himself had made.",
      "M": "He dug a pit, made it deep, and fell into the very pit he made.",
      "T": "He dug a trap.\nHe made it deep.\nThen he fell into it himself."
    },
    "16": {
      "L": "His mischief returns upon his own head, and his violence descends upon his own skull.",
      "M": "His mischief comes back on his own head; his violence falls down on his own skull.",
      "T": "All his cruelty loops back on him.\nThe violence he launched lands on his own head."
    },
    "17": {
      "L": "I will give thanks to the LORD according to his righteousness, and I will sing praise to the name of the LORD Most High.",
      "M": "I will give thanks to the LORD for his righteousness, and sing praise to the name of the LORD Most High.",
      "T": "For this — for all of it — I will praise him.\nI will sing to the LORD who is just.\nI will lift my voice to the name of the LORD Most High."
    }
  },
  "8": {
    "1": {
      "L": "A Psalm of David; to the Chief Musician, on the Gittith. O LORD our Lord, how excellent is your name in all the earth! You have set your glory above the heavens.",
      "M": "A Psalm of David, for the choir director, to be played on the Gittith. O LORD our Lord, how majestic is your name throughout all the earth! You have placed your glory above the heavens.",
      "T": "A Psalm of David, for the choirmaster, to the melody of 'the Gittith.'\n\nLORD — our Lord —\nhow magnificent your name is across all the earth!\nYour splendor towers above the heavens themselves."
    },
    "2": {
      "L": "Out of the mouth of babes and nursing infants you have established strength, because of your foes, to silence the enemy and the avenger.",
      "M": "From the mouths of children and nursing infants you have ordained praise, because of your enemies, to silence the foe and the avenger.",
      "T": "Even the voices of children — of babies still at the breast —\nyou have shaped into a fortress of praise,\nto stop the mouths of your enemies, to silence every rebel cry."
    },
    "3": {
      "L": "When I consider your heavens, the work of your fingers, the moon and the stars, which you have set in place —",
      "M": "When I look at your heavens, the work of your fingers — the moon and the stars that you have established —",
      "T": "When I look up at the night sky — your sky —\nat the moon, at those uncountable stars,\nthe intricate handiwork of your fingers —"
    },
    "4": {
      "L": "what is man that you are mindful of him, and the son of man that you care for him?",
      "M": "what is humanity that you give it a thought? What is a human being that you attend to him?",
      "T": "— what is a human being, that you would spend a thought on us?\nWho are we — this fleeting dust — that you would pay us any personal attention?"
    },
    "5": {
      "L": "Yet you have made him a little lower than the heavenly beings, and crowned him with glory and honor.",
      "M": "Yet you have made him just a little lower than the heavenly beings, and crowned him with glory and honor.",
      "T": "Yet you made us barely a step below the divine.\nYou set glory like a crown on our heads.\nYou invested us with honor."
    },
    "6": {
      "L": "You have given him dominion over the works of your hands; you have put all things under his feet:",
      "M": "You have given him dominion over the works of your hands; you have placed everything under his feet:",
      "T": "You have put him in charge of everything your hands have made.\nEvery created thing — you have laid it at his feet:"
    },
    "7": {
      "L": "all sheep and oxen, and also the beasts of the field,",
      "M": "all sheep and cattle, and also the wild animals,",
      "T": "herds and flocks, every domesticated creature,\nand all the wildlife of the open country,"
    },
    "8": {
      "L": "the birds of the heavens and the fish of the sea, whatever passes through the paths of the seas.",
      "M": "the birds of the sky and the fish of the sea, whatever moves along the ocean's currents.",
      "T": "birds overhead, fish threading through the sea's dark paths —\neverything that moves in the deep channels of the ocean."
    },
    "9": {
      "L": "O LORD our Lord, how excellent is your name in all the earth!",
      "M": "O LORD our Lord, how majestic is your name throughout all the earth!",
      "T": "LORD — our Lord —\nhow magnificent your name is across all the earth!"
    }
  },
  "9": {
    "1": {
      "L": "A Psalm of David; to the Chief Musician, on Muth-labben. I will praise you, O LORD, with my whole heart; I will declare all your marvelous deeds.",
      "M": "A Psalm of David, for the choir director, set to 'Muth-labben.' I will give thanks to you, LORD, with my whole heart; I will tell of all your wonderful works.",
      "T": "A Psalm of David, for the choirmaster, to be sung to 'Muth-labben.'\n\nWith everything in me — my whole heart — I will praise you, LORD.\nI will tell the full account of every wonder you have done."
    },
    "2": {
      "L": "I will be glad and exult in you; I will sing praise to your name, O Most High.",
      "M": "I will rejoice and be glad in you; I will sing praise to your name, O Most High.",
      "T": "In you I find a joy that rises to exultation.\nTo you, Most High, I will sing."
    },
    "3": {
      "L": "When my enemies turn back, they stumble and perish before your face.",
      "M": "When my enemies turn back, they stumble and perish at your presence.",
      "T": "When my enemies turn and run,\nthey trip, they crumble — right there before your face."
    },
    "4": {
      "L": "For you have maintained my just cause; you sat on the throne, judging righteously.",
      "M": "For you upheld my right and my cause; you sat on the throne, judging with righteousness.",
      "T": "You stepped in for me — you took up my case as your own.\nFrom your throne you rendered justice: the right verdict, the only verdict."
    },
    "5": {
      "L": "You have rebuked the nations; you have destroyed the wicked; you have blotted out their name forever and ever.",
      "M": "You rebuked the nations and destroyed the wicked; you blotted out their name forever and ever.",
      "T": "You confronted the nations and they broke.\nYou destroyed the wicked — and more: you erased their name,\nwiped it clean so that nothing of them remains, now or ever."
    },
    "6": {
      "L": "The enemy has come to an end in everlasting ruin; you have uprooted their cities; their very memory has perished.",
      "M": "The enemy has come to an end in perpetual ruin; you uprooted their cities; their very memory has perished.",
      "T": "The enemy is finished — buried in permanent ruin.\nYou tore their cities out by the roots.\nNothing remains. Not even a memory."
    },
    "7": {
      "L": "But the LORD sits enthroned forever; he has established his throne for judgment.",
      "M": "But the LORD sits enthroned forever; he has set his throne for judgment.",
      "T": "But the LORD — he endures.\nHe sits on his throne forever.\nHe has fixed that throne as the seat of justice."
    },
    "8": {
      "L": "He will judge the world with righteousness; he will judge the peoples with equity.",
      "M": "He judges the world with righteousness; he rules the peoples with equity.",
      "T": "He will judge the whole world — and he will do it right.\nEvery people, every nation: he will deal with them in perfect fairness."
    },
    "9": {
      "L": "The LORD is a stronghold for the oppressed, a stronghold in times of trouble.",
      "M": "The LORD is a refuge for the oppressed, a stronghold in times of trouble.",
      "T": "For those being crushed — the ground-down, the powerless —\nthe LORD is a high fortress.\nWhen trouble closes in, he is the place to run."
    },
    "10": {
      "L": "Those who know your name put their trust in you, for you, O LORD, have not forsaken those who seek you.",
      "M": "Those who know your name will trust in you, for you, LORD, have never abandoned those who seek you.",
      "T": "Knowing you — truly knowing who you are — is the surest ground for trust.\nYou have never once abandoned anyone who came looking for you, LORD. Not once."
    },
    "11": {
      "L": "Sing praises to the LORD who dwells in Zion; declare his deeds among the peoples!",
      "M": "Sing praises to the LORD who dwells in Zion; declare his deeds among the nations!",
      "T": "Sing to the LORD, the God who makes Zion his home!\nBroadcast what he has done — let every nation hear it!"
    },
    "12": {
      "L": "For he who avenges blood is mindful of them; he does not forget the cry of the afflicted.",
      "M": "For the one who avenges bloodshed is mindful of them; he does not forget the cry of the humble.",
      "T": "He takes note of every act of bloodshed.\nHe holds in memory every cry that ever came from the afflicted.\nNot one of those cries has been forgotten."
    },
    "13": {
      "L": "Have mercy on me, O LORD! See my affliction from those who hate me, O you who lift me up from the gates of death —",
      "M": "Be gracious to me, O LORD! See the suffering I endure from those who hate me — you who lift me back from the very gates of death —",
      "T": "Have mercy on me, LORD. Look at what hatred does to a person.\nYou are the one who can haul me back from death's own gate —"
    },
    "14": {
      "L": "that I may recount all your praises in the gates of the daughter of Zion, that I may rejoice in your salvation.",
      "M": "so that I may declare all your praises in the gates of daughter Zion, and rejoice in your salvation.",
      "T": "— so that I can stand in the gates of Zion and tell the full story:\nhow you saved me. Every detail. And I will be glad."
    },
    "15": {
      "L": "The nations have sunk in the pit they made; in the net they hid, their own foot has been caught.",
      "M": "The nations have sunk in the pit they made; their own foot was caught in the net they concealed.",
      "T": "The nations dug a pit.\nThey fell into it.\nThey laid a trap.\nTheir own feet walked into it."
    },
    "16": {
      "L": "The LORD has made himself known; he has executed judgment. The wicked are snared in the work of their own hands. Higgaion. Selah",
      "M": "The LORD has made himself known by executing judgment; the wicked are ensnared by the work of their own hands. Higgaion. Selah",
      "T": "The LORD has made himself unmistakable:\nhe does justice, and the wicked are caught — caught in the very thing they built to trap others.\n[Higgaion — a meditation. Pause and reflect.] Selah"
    },
    "17": {
      "L": "The wicked shall return to Sheol, all the nations that forget God.",
      "M": "The wicked will return to Sheol, all the nations that forget God.",
      "T": "The wicked are headed for Sheol — the place of the forgotten dead.\nEvery nation that has turned its back on God will follow them there."
    },
    "18": {
      "L": "For the needy shall not always be forgotten, and the hope of the poor shall not perish forever.",
      "M": "For the needy will not always be forgotten, nor will the hope of the poor perish forever.",
      "T": "But the poor will not be erased from memory.\nThe hope of the afflicted will not be deferred forever.\nIt will not perish."
    },
    "19": {
      "L": "Arise, O LORD! Let not man prevail; let the nations be judged before you!",
      "M": "Rise up, O LORD! Let not man have his way; let the nations be judged in your presence!",
      "T": "Rise up, LORD — do not let mere human arrogance win the day.\nBring the nations before your court."
    },
    "20": {
      "L": "Put them in fear, O LORD! Let the nations know they are but men. Selah",
      "M": "Strike them with fear, O LORD! Let the nations know they are only human. Selah",
      "T": "Put the fear of you into them, LORD.\nLet the nations discover what they truly are — mortal, finite, just men. Selah"
    }
  },
  "10": {
    "1": {
      "L": "Why, O LORD, do you stand far off? Why do you hide yourself in times of trouble?",
      "M": "Why, O LORD, do you stand at a distance? Why do you hide yourself in times of trouble?",
      "T": "LORD, why are you so far away?\nWhy do you hide — especially now, when trouble has swallowed everything?"
    },
    "2": {
      "L": "In arrogance the wicked hotly pursues the poor; let them be caught in the schemes they have devised.",
      "M": "In his arrogance the wicked person persecutes the poor; let him be caught in the very schemes he has devised.",
      "T": "With pride as his engine, the wicked hunts the helpless.\nLet him be snared in the very traps he designed."
    },
    "3": {
      "L": "For the wicked boasts of the desire of his soul, and the one who is greedy curses and renounces the LORD.",
      "M": "For the wicked person boasts of the cravings of his heart, and the greedy curses and spurns the LORD.",
      "T": "The wicked is proud of what he wants — he boasts about his appetites.\nThe greedy man curses the LORD and dismisses him without a thought."
    },
    "4": {
      "L": "The wicked, in the pride of his face, does not seek him; in all his thoughts, there is no room for God.",
      "M": "In his arrogance the wicked person does not seek God; in all his thinking, there is no place for God.",
      "T": "The wicked, in his pride, never once looks up toward God.\nHis entire frame of thought has no room for God — none."
    },
    "5": {
      "L": "His ways prosper at all times; your judgments are high, out of his sight; as for all his foes, he puffs at them.",
      "M": "His ways always succeed; your judgments are too high for him to perceive; he sneers at all his enemies.",
      "T": "Everything he does seems to work — at least for now.\nYour judgments are far above him; he cannot see them, never looks for them.\nAs for his enemies, he blows at them like smoke."
    },
    "6": {
      "L": "He says in his heart, 'I shall not be moved; throughout all generations I shall not meet adversity.'",
      "M": "He says in his heart, 'I will never be shaken; through all generations I will face no trouble.'",
      "T": "He tells himself: 'I am immovable. Nothing will shake me.\nNo setback will ever reach me — not now, not ever.'"
    },
    "7": {
      "L": "His mouth is full of cursing and deceit and oppression; under his tongue are mischief and iniquity.",
      "M": "His mouth is full of cursing, deceit, and fraud; under his tongue are trouble and wickedness.",
      "T": "His every word is a weapon — curses, lies, manipulation.\nHidden beneath his tongue: harm he is already planning, evil he is about to do."
    },
    "8": {
      "L": "He sits in ambush in the villages; in secret places he murders the innocent. His eyes stealthily watch for the helpless.",
      "M": "He lurks in ambush near the villages; in hiding places he kills the innocent. His eyes are set to watch for the helpless.",
      "T": "He lies in wait near the villages — in the shadows, watching.\nHe kills the innocent.\nHis eyes are fixed on the vulnerable, tracking them."
    },
    "9": {
      "L": "He lurks in secret like a lion in its den; he lies in wait to seize the poor; he seizes the poor and drags him into his net.",
      "M": "He crouches like a lion in his lair; he lies in wait to catch the poor; he catches the poor by dragging them into his net.",
      "T": "He crouches in the underbrush like a lion before it springs.\nHe lunges — and the poor person is caught,\ndragged into the net before they even knew it was there."
    },
    "10": {
      "L": "He crouches, he bows down, and the helpless fall by his might.",
      "M": "He crouches and springs, and the helpless fall by his strength.",
      "T": "He coils. He pounces. And the helpless collapse under him."
    },
    "11": {
      "L": "He says in his heart, 'God has forgotten; he has hidden his face; he will never see it.'",
      "M": "He says in his heart, 'God has forgotten; he has hidden his face; he will never notice.'",
      "T": "He assures himself: 'God has forgotten all about this.\nHe has looked away. He will never see what I am doing.'"
    },
    "12": {
      "L": "Arise, O LORD! O God, lift up your hand! Do not forget the humble!",
      "M": "Rise up, O LORD! O God, lift up your hand! Do not forget the afflicted!",
      "T": "Rise up, LORD! Raise your hand, O God!\nDo not forget the people who have no one else."
    },
    "13": {
      "L": "Why does the wicked renounce God and say in his heart, 'You will not call to account'?",
      "M": "Why does the wicked person despise God and say in his heart, 'You won't call me to account'?",
      "T": "How can the wicked go on dismissing you, LORD — telling himself you will not act, will not demand an answer?"
    },
    "14": {
      "L": "But you do see! You observe trouble and grief to take it into your hands. The helpless commits himself to you; you have been the helper of the fatherless.",
      "M": "But you do see! You observe trouble and grief and take it into your hands. The helpless person entrusts himself to you; you have always been the helper of the fatherless.",
      "T": "But you do see — you see it all.\nTrouble, grief, every grievance — you take it all in and hold it.\nThe helpless have nowhere else to go but you,\nand you have always been the one who defends the fatherless."
    },
    "15": {
      "L": "Break the arm of the wicked and evildoer; call his wickedness to account till you find none.",
      "M": "Break the arm of the wicked and the evildoer; call his wickedness to account until there is none left.",
      "T": "Shatter the power of the wicked.\nPursue every last thread of their evil until nothing remains — until there is nothing left to find."
    },
    "16": {
      "L": "The LORD is King forever and ever; the nations shall perish from his land.",
      "M": "The LORD is King for ever and ever; the nations will vanish from his land.",
      "T": "The LORD reigns. He has always reigned. He will always reign.\nAnd those nations that have lived by violence — they will be swept from his land."
    },
    "17": {
      "L": "O LORD, you hear the desire of the humble; you will strengthen their heart; you will incline your ear",
      "M": "LORD, you have heard the desire of the humble; you will strengthen their heart; you will turn your ear",
      "T": "LORD, you have heard what the humble long for.\nYou strengthen their resolve. You lean in to listen."
    },
    "18": {
      "L": "to do justice to the fatherless and the oppressed, so that man who is of the earth will strike terror no more.",
      "M": "to vindicate the fatherless and the oppressed, so that mortal man will no longer strike terror.",
      "T": "You act for the orphan, for the crushed.\nYou make sure that no mere mortal can go on terrorizing others without a reckoning."
    }
  },
  "11": {
    "1": {
      "L": "A Psalm of David; to the Chief Musician. In the LORD I take refuge; how can you say to my soul, 'Flee like a bird to your mountain'?",
      "M": "A Psalm of David, for the choir director. In the LORD I take refuge. How can you say to me, 'Fly to your mountain like a bird'?",
      "T": "A Psalm of David, for the choirmaster.\n\nThe LORD is where I shelter. So why do you keep urging me to flee — 'Get out, like a bird escaping to the hills!'"
    },
    "2": {
      "L": "For behold, the wicked bend the bow; they have fitted their arrow to the string to shoot in the dark at the upright in heart.",
      "M": "For look — the wicked string the bow; they have set their arrows on the string to shoot in the darkness at the upright in heart.",
      "T": "Yes — the wicked have strung their bows.\nThey have arrows on the string, aimed and ready.\nThey intend to shoot from the shadows at those whose hearts are right."
    },
    "3": {
      "L": "If the foundations are destroyed, what can the righteous do?",
      "M": "If the foundations are destroyed, what can the righteous do?",
      "T": "And if everything foundational collapses — what ground is left for the righteous to stand on?"
    },
    "4": {
      "L": "The LORD is in his holy temple; the LORD's throne is in heaven. His eyes see; his eyelids test the children of man.",
      "M": "The LORD is in his holy temple; the LORD's throne is in heaven. His eyes observe; his eyelids examine the children of mankind.",
      "T": "But the LORD is in his holy temple.\nHis throne is fixed in heaven.\nHis eyes are open — they see everything.\nHis searching gaze examines every human being."
    },
    "5": {
      "L": "The LORD tests the righteous, but his soul hates the wicked and him who loves violence.",
      "M": "The LORD tests the righteous, but his soul hates the wicked and the one who loves violence.",
      "T": "He tests the righteous — that testing is his way of knowing them.\nBut the wicked, the violence-lovers — his whole being recoils from them."
    },
    "6": {
      "L": "Let him rain coals on the wicked; fire and sulfur and a scorching wind shall be the portion of their cup.",
      "M": "Let him rain down coals on the wicked; fire and sulfur and a scorching wind will be the lot assigned to their cup.",
      "T": "On the wicked he rains down fire and burning sulfur.\nA searing wind — that is what fills their cup to the brim."
    },
    "7": {
      "L": "For the LORD is righteous; he loves righteous deeds; the upright shall behold his face.",
      "M": "For the LORD is righteous; he loves righteous deeds; the upright will see his face.",
      "T": "The LORD is just — that is who he is.\nHe loves justice — it is what he does.\nAnd those who are truly upright? They will see him face to face."
    }
  },
  "12": {
    "1": {
      "L": "A Psalm of David; to the Chief Musician, on the Sheminith. Help, O LORD! For the godly person ceases; the faithful have vanished from among the children of men.",
      "M": "A Psalm of David, for the choir director, to be played on the Sheminith — the eight-stringed instrument. Help us, LORD! For the godly are gone; the faithful have vanished from among humanity.",
      "T": "A Psalm of David, for the choirmaster, to be played on the lower eight-stringed instrument.\n\nLord, we need you — urgently. The person of integrity has disappeared.\nThe loyal have become an endangered species. Where have they all gone?"
    },
    "2": {
      "L": "Everyone speaks falsehood to his neighbor; with flattering lips and a double heart they speak.",
      "M": "Everyone lies to his neighbor; they speak with flattering lips and a divided heart.",
      "T": "Lies are the common currency now.\nEveryone flatters their neighbor while thinking something entirely different —\na smooth face, a divided heart."
    },
    "3": {
      "L": "May the LORD cut off all flattering lips and the tongue that speaks great things,",
      "M": "May the LORD cut off all flattering lips and every tongue that boasts,",
      "T": "Let the LORD silence those smooth tongues.\nLet him cut off every mouth that flatters and brags."
    },
    "4": {
      "L": "those who say, 'With our tongue we will prevail; our lips are our own — who is master over us?'",
      "M": "those who say, 'With our words we will prevail; our lips are our own — who can lord it over us?'",
      "T": "They are saying: 'Words are our weapons. We will win with our mouths.\nWho has any authority over us?'"
    },
    "5": {
      "L": "'Because the poor are plundered, because the needy groan, I will now arise,' says the LORD; 'I will place him in the safety for which he longs.'",
      "M": "'Because the poor are oppressed and the needy groan, I will now arise,' says the LORD. 'I will set them in the safety they long for.'",
      "T": "'Enough,' says the LORD. 'The poor are being robbed. The needy are crying out.\nNow I am rising. I will set them in the safety they have longed for.'"
    },
    "6": {
      "L": "The words of the LORD are pure words, like silver refined in a furnace on the ground, purified seven times.",
      "M": "The words of the LORD are pure words, like silver refined in a furnace in the ground, purified seven times.",
      "T": "What the LORD says is nothing like human speech.\nHis words are pure: silver smelted down, refined until only the finest remains —\npurified seven times over. Flawless."
    },
    "7": {
      "L": "You, O LORD, will keep them; you will guard us from this generation forever.",
      "M": "You, O LORD, will keep them; you will protect us from this generation forever.",
      "T": "You will keep your people, LORD.\nYou will hold us against everything this corrupt generation tries to do."
    },
    "8": {
      "L": "On every side the wicked prowl, as vileness is exalted among the children of man.",
      "M": "The wicked parade on every side when what is vile is honored among humanity.",
      "T": "The wicked strut freely on every side,\nwhile what is depraved is celebrated — that is the world we are living in."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 7–12 written.')

if __name__ == '__main__':
    main()
