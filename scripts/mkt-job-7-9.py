"""
MKT Job chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-7-9.py

=== Contested-term decisions ===

H582  (אֱנוֹשׁ, enosh): "mortal" (L) / "man" (M) / "frail mortal" or "human being" (T)
      — enosh is the specifically fragile word for humanity; distinct from adam.
      Job deploys it precisely to underscore human smallness before God.

H7307 (רוּחַ, ruach): context-driven across all three tiers:
      7:7  — "breath" (life as exhalation: fleeting, vaporous)
      7:11 — "spirit" (anguish of spirit: inner affective life)
      8:2  — "wind" (Bildad: Job's words are empty air)
      9:18 — "breath" (God will not let him catch his breath)
      Capitalised "Spirit" not used here; in Job the divine agent is always El/Shaddai,
      and ruach in ch.7–9 refers to Job's inner state or to wind/air, not the divine Spirit.

H5315 (נֶפֶשׁ, nefesh): "soul" where inner agony is in view (7:11, 7:15);
      "life" where existence is the referent (9:21).
      Never rendered as immaterial Greek soul — always embodied self.

H7706 (שַׁדַּי, Shaddai): L keeps the proper name "Shaddai"; M/T render "the Almighty."
      The name carries the force of overwhelming, terrifying divine power — important
      context in ch.9 where Job wrestles with God's unanswerable might.

H433  (אֱלוֹהַּ, Eloah): singular divine name common in Job. Rendered "God" in all tiers.

H410  (אֵל, El): "God" in all tiers; the most frequent divine name in chs.7–9.

H7293 (רַהַב, Rahab): the mythological sea-dragon of chaos, attested in ancient Near Eastern
      literature and alluded to in Job 9:13. L/M retain "Rahab" with contextual gloss;
      T unpacks as "chaos-dragon" to surface the mythological register.

H7585 (שְׁאוֹל, Sheol): kept as "Sheol" in L/M; T renders "the realm of the dead" in 7:9
      to make the referent transparent for modern readers.

=== Aspect and tense notes ===

Job 7–9 is Hebrew poetry (except the brief narrative bridge formulas in 8:1 and 9:1).
Verbal stems are predominantly imperfect (ongoing/repeated) and perfect (completed).
The T tier attempts to honour this aspect: Job's suffering is not a single event
but an ongoing, recurring experience — rendered with present and present-perfect tenses
where Hebrew imperfect appears.

=== Structural notes ===

Ch.7: Job's soliloquy addressed to God — shifts from third-person lament (vv.1–6)
to direct second-person address to God (vv.7–21). The inversion of Psalm 8
("What is man?" asked in despair rather than wonder) reaches its climax at v.17.

Ch.8: Bildad's first speech — confident, somewhat dismissive. Uses nature wisdom
(papyrus/reed, vv.11–19) and appeals to tradition (vv.8–10). His logic is impeccable
and his empathy is absent.

Ch.9: Job's response — the most theologically dense of the three chapters. Job
acknowledges God's power fully (vv.2–12) but turns it against the possibility of
justice (vv.13–24). The longing for an arbitrator (v.33) is one of the most
significant anticipations in the OT of a mediator figure.

=== OT echo notes ===

Job 7:17–18 deliberately inverts Psalm 8:4–5 (ESV). Where Psalm 8 marvels that God
pays attention to frail humanity with grace, Job reads the same divine attention as
claustrophobic surveillance. The echo is intentional and marked in T tier.

Job 9:8 echoes cosmogonic hymns; "treading on the waves of the sea" reappears in
Matthew 14:25 and Mark 6:48 — NT readers will hear the resonance.
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


JOB = {
  "7": {
    "1": {
      "L": "Is there not appointed service for a mortal on earth? Are not his days like the days of a hired laborer?",
      "M": "Does not man have hard service on earth, and are not his days like those of a hired worker?",
      "T": "Every human life on earth is forced labor — our days grinding past like a hired hand's dreary shift, with no end in sight."
    },
    "2": {
      "L": "Like a servant who pants for the shadow, and like a hired laborer who looks for his wages —",
      "M": "Like a servant longing for the shade, like a worker waiting eagerly for his pay —",
      "T": "We are like slaves gasping for shade in the heat, like day laborers watching the sun to know when they will finally be paid."
    },
    "3": {
      "L": "So I am made to inherit months of emptiness, and nights of trouble are appointed to me.",
      "M": "So I am allotted months of futility, and wearisome nights are assigned to me.",
      "T": "My inheritance is hollow months — an endless rotation of nights that bring nothing but anguish and no rest."
    },
    "4": {
      "L": "When I lie down I say, 'When shall I arise?' The night drags on, and I am filled with tossings until the dawn.",
      "M": "When I lie down I say, 'When will I get up?' But the night stretches long and I toss about until dawn.",
      "T": "I lie down asking when morning will come; the night sprawls before me, endless, and I writhe until the first grey light — and then the cycle begins again."
    },
    "5": {
      "L": "My flesh is clothed with worms and clods of dust; my skin breaks open and runs.",
      "M": "My flesh is covered with worms and a crust of earth; my skin cracks and oozes.",
      "T": "My body has become a horror — worms and crusted earth fused to my skin, which splits open and weeps without healing."
    },
    "6": {
      "L": "My days are swifter than a weaver's shuttle and come to an end without hope.",
      "M": "My days are swifter than a weaver's shuttle, and they end without hope.",
      "T": "My life races past like a shuttle flying across the loom — and when it reaches the edge, there is nothing there. No hope waiting on the other side."
    },
    "7": {
      "L": "Remember that my life is a breath; my eye will see good no more.",
      "M": "Remember that my life is but a breath; my eyes will never again see happiness.",
      "T": "Remember, O God — my life is a single breath. One exhale and it is gone. I will not see anything good again."
    },
    "8": {
      "L": "The eye of him who sees me will see me no more; your eyes will look upon me, but I will not be.",
      "M": "The eye of whoever sees me now will see me no more; you will look for me, but I will be gone.",
      "T": "Anyone who looks at me now will never look at me again. Even you, God — you will search for me and find nothing."
    },
    "9": {
      "L": "As a cloud fades away and vanishes, so one who goes down to Sheol does not come up.",
      "M": "As a cloud vanishes and is gone, so the one who descends to Sheol does not come up.",
      "T": "A cloud dissolves into nothing — and that is the story of every person who goes down to the realm of the dead. They do not rise."
    },
    "10": {
      "L": "He does not return to his house, nor does his place know him anymore.",
      "M": "He will never return home, and his place will know him no more.",
      "T": "He will never walk through his own door again. His home will forget him. His chair will stand empty until someone else sits in it."
    },
    "11": {
      "L": "Therefore I will not restrain my mouth; I will speak in the anguish of my spirit; I will complain in the bitterness of my soul.",
      "M": "Therefore I will not hold back; I will speak in the anguish of my spirit and complain in the bitterness of my soul.",
      "T": "So — I refuse to be silent. My spirit is in agony and I will say so. My whole being is bitter and I will voice every syllable of it."
    },
    "12": {
      "L": "Am I the sea, or a sea monster, that you have set a watch over me?",
      "M": "Am I the sea, or a sea monster, that you place a guard over me?",
      "T": "What am I to you — the primordial sea? A chaos-dragon that must be restrained? Why do you guard me as if I were a cosmic threat?"
    },
    "13": {
      "L": "When I say, 'My couch will comfort me, my bed will ease my complaint' —",
      "M": "When I say, 'My bed will comfort me; my couch will ease my complaint' —",
      "T": "Sometimes I tell myself: at least I have my bed. At least sleep will bring some relief from this grief —"
    },
    "14": {
      "L": "— then you frighten me with dreams and terrify me with visions,",
      "M": "— but then you terrify me with dreams and frighten me with visions,",
      "T": "— but even sleep you have turned into a weapon. You send nightmares to shatter the one small shelter I have left."
    },
    "15": {
      "L": "so that my soul would choose strangling, and death rather than my bones.",
      "M": "so that I would choose strangulation and death rather than this suffering in my body.",
      "T": "And so I find myself choosing suffocation — death itself would be cleaner than this prolonged torment in my own decaying flesh."
    },
    "16": {
      "L": "I loathe it; I would not live forever. Let me alone, for my days are a breath.",
      "M": "I am through with it; I would not live forever. Leave me be, for my days are only a breath.",
      "T": "I am done. I do not want eternal life — I can barely endure the life I have. Leave me alone. I am nothing more than a breath of air."
    },
    "17": {
      "L": "What is man, that you make so much of him, and that you set your heart upon him —",
      "M": "What is man, that you should make so much of him, and that you fix your attention on him —",
      "T": "What is a human being, that you should pour such attention on him? Why have you fixed your heart on something so small and so fragile —"
    },
    "18": {
      "L": "— visiting him every morning and testing him every moment?",
      "M": "— testing him every morning, examining him every moment?",
      "T": "— scrutinizing him every single morning, probing him every single moment, never letting one instant pass unwatched?"
    },
    "19": {
      "L": "How long will you not look away from me and not let me alone until I swallow my saliva?",
      "M": "How long will you not look away from me, or leave me alone long enough to swallow?",
      "T": "Will you never avert your gaze? Not even long enough for me to draw one breath? To swallow my own spit?"
    },
    "20": {
      "L": "If I have sinned, what have I done to you, O watcher of men? Why have you made me your target, so that I am a burden to myself?",
      "M": "If I have sinned, what have I done to you, O watcher of mankind? Why have you made me your target, till I am a burden to myself?",
      "T": "Even if I have sinned — what damage does that do to you, Keeper of humanity? Why make me your personal target until I have become a burden to my own soul?"
    },
    "21": {
      "L": "Why do you not pardon my transgression and take away my iniquity? For now I shall lie down in the dust, and you will seek me earnestly, but I shall not be.",
      "M": "Why do you not pardon my offense and forgive my sin? For soon I shall lie down in the dust; you will search for me diligently, but I will be gone.",
      "T": "Why not simply forgive me? Wipe it away. Because soon I will be dust — and you will come looking for someone to answer, and find nothing. No one left to punish. No one left to forgive."
    }
  },
  "8": {
    "1": {
      "L": "Then Bildad the Shuhite answered and said:",
      "M": "Then Bildad the Shuhite answered and said:",
      "T": "Then Bildad the Shuhite broke in:"
    },
    "2": {
      "L": "How long will you speak these things? And how long shall the words of your mouth be a mighty wind?",
      "M": "How long will you say such things? The words of your mouth are nothing but a mighty blast of wind.",
      "T": "How long are you going to keep this up? Everything you have said is so much hot air — powerful and meaningless."
    },
    "3": {
      "L": "Does God pervert justice? Does the Almighty pervert righteousness?",
      "M": "Does God distort justice? Does the Almighty corrupt what is right?",
      "T": "Can you honestly think God distorts justice? That the Almighty would bend what is right? The very idea is absurd — it dismantles his entire nature."
    },
    "4": {
      "L": "If your children sinned against him, he delivered them into the power of their transgression.",
      "M": "If your children sinned against him, he gave them over to the consequences of their own sin.",
      "T": "Your children sinned, and they received exactly what sin earns. God was not arbitrary. He did not reach in and harm them — he simply withdrew his hand."
    },
    "5": {
      "L": "If you will seek God earnestly and make supplication to the Almighty —",
      "M": "If you will seek God earnestly and plead with the Almighty for grace —",
      "T": "But you — if you would only turn to God seriously, if you would humble yourself before the Almighty —"
    },
    "6": {
      "L": "if you are pure and upright, surely then he will rouse himself for you and restore your righteous dwelling —",
      "M": "if you are pure and upright, surely then he will act on your behalf and restore your righteous home —",
      "T": "— if you have actually been living with integrity, then God will awaken on your behalf. He will set your household right again and more than right."
    },
    "7": {
      "L": "though your beginning was small, your latter end shall greatly increase.",
      "M": "Though your beginnings were humble, your latter years will be far greater.",
      "T": "Whatever you have lost — think of it as a seed. What God restores will dwarf what you ever had before."
    },
    "8": {
      "L": "For please inquire of the former age and attend to the things their fathers searched out —",
      "M": "Ask the former generations and give heed to the wisdom our ancestors have searched out —",
      "T": "Do not rely on your own brief experience alone. Go back to the generations before you. Ask what our fathers discovered when they probed these questions."
    },
    "9": {
      "L": "for we are but of yesterday and know nothing, for our days on earth are a shadow.",
      "M": "for we are but of yesterday and know nothing; our days on earth are but a shadow.",
      "T": "We are newcomers to the world — barely a day old. Our lives are shadows cast on the ground. The ancients saw deeper because they lived longer in the fear of God."
    },
    "10": {
      "L": "Will they not teach you and tell you, and utter words from their understanding?",
      "M": "Will they not teach you, tell you, and speak from the depths of their understanding?",
      "T": "The accumulated wisdom of those who came before will speak — if only we will stop talking long enough to hear it."
    },
    "11": {
      "L": "Can papyrus grow tall where there is no marsh? Can reeds flourish without water?",
      "M": "Can papyrus grow where there is no marsh? Can reeds flourish without water?",
      "T": "A reed does not grow in dry sand. Papyrus does not bloom where there is no water. Nature does not lie — and neither does the moral order."
    },
    "12": {
      "L": "While still in its greenness, not yet cut down, it withers before any other plant.",
      "M": "Though it is still green and not yet cut, it withers before any other herb.",
      "T": "The moment the water disappears, that flourishing reed collapses before anything else. Green one moment — withered the next. That is how it goes."
    },
    "13": {
      "L": "Such are the paths of all who forget God; the hope of the godless will perish.",
      "M": "Such is the end of all who forget God; the hope of the godless will come to nothing.",
      "T": "The same withering overtakes everyone who forgets God. Their hope is a reed without water — it will die, and die faster than anything else around it."
    },
    "14": {
      "L": "His confidence is cut off, and his trust is a spider's house.",
      "M": "What he trusts in will be cut off, and his confidence is like a spider's web.",
      "T": "Everything the godless man leans on will give way. His security is a spider's web — it looks like structure, but it holds nothing and tears at the first touch."
    },
    "15": {
      "L": "He leans on his house, but it does not stand; he holds fast to it, but it does not endure.",
      "M": "He leans against his house, but it does not stand; he clings to it, but it will not hold.",
      "T": "He throws his full weight on his own arrangements — and they collapse under him. He grips the web and it tears."
    },
    "16": {
      "L": "He is well watered before the sun, and his shoots spread over his garden.",
      "M": "He is well watered in the sunshine, his shoots spreading over the garden.",
      "T": "For a season he looks magnificent — green, full, healthy, branches arching wide over everything around him."
    },
    "17": {
      "L": "His roots are entwined around the stone heap; he gazes upon a house of stones.",
      "M": "His roots twine around the pile of stones; he forces his way into a stony place.",
      "T": "His roots grip the very rocks — he seems immovable, permanent, woven into the landscape itself."
    },
    "18": {
      "L": "If he is swept from his place, then it denies him: 'I have not seen you.'",
      "M": "But if he is destroyed from his place, it says to him: 'I have never seen you.'",
      "T": "But let him be removed — and the stone will say: 'I never knew you.' The ground will not even remember that he stood there."
    },
    "19": {
      "L": "Behold, this is the joy of his way, and from the earth others will spring up.",
      "M": "Behold, such is the joy of his path; and from the earth others will spring up in his place.",
      "T": "That is all his flourishing amounted to. He is gone, and from the same soil someone else is already rising to take his place."
    },
    "20": {
      "L": "Behold, God will not reject a blameless person, nor will he take the hand of evildoers.",
      "M": "God does not reject the blameless, nor does he take hold of the hand of wrongdoers.",
      "T": "God has not abandoned integrity. He does not patron or protect those who do evil. The moral order is still in place."
    },
    "21": {
      "L": "He will yet fill your mouth with laughter and your lips with shouts of joy.",
      "M": "He will yet fill your mouth with laughter and your lips with joyful shouts.",
      "T": "Job, he will fill your mouth with laughter again. The shout of joy — you thought it was gone forever, but it will return."
    },
    "22": {
      "L": "Those who hate you will be clothed with shame, and the tent of the wicked will be no more.",
      "M": "Your enemies will be clothed with shame, and the tent of the wicked will vanish.",
      "T": "Your enemies will wear shame like a garment they cannot take off. The wicked man's dwelling — every trace of it — will be erased."
    }
  },
  "9": {
    "1": {
      "L": "Then Job answered and said:",
      "M": "Then Job answered:",
      "T": "Job replied:"
    },
    "2": {
      "L": "Truly I know it is so. But how can a mortal be in the right before God?",
      "M": "Indeed, I know this is true. But how can a man be justified before God?",
      "T": "Yes — I know that much is right. But the real question is not theological. It is survival. How does a frail human being stand before God and be found innocent?"
    },
    "3": {
      "L": "If one wished to contend with him, one could not answer him one out of a thousand times.",
      "M": "If one wished to dispute with him, one could not answer him once in a thousand attempts.",
      "T": "If you actually tried to bring a case against God, you could not get even one argument in edgewise out of a thousand. He would answer before you finished framing your question."
    },
    "4": {
      "L": "He is wise in heart and mighty in strength — who has hardened himself against him and come out unscathed?",
      "M": "God is wise in heart and mighty in strength — who has defied him and survived intact?",
      "T": "He is brilliant in mind and immovable in power. No one has squared off against him and walked away whole. The record is clear: no one."
    },
    "5": {
      "L": "He who removes mountains, and they know it not, when he overturns them in his anger —",
      "M": "He removes mountains before they know it, overturning them in his anger —",
      "T": "He dismantles mountains and the mountains do not even realize what is happening until it is already done — that is how total his power is —"
    },
    "6": {
      "L": "who shakes the earth out of its place, so that its pillars tremble —",
      "M": "who shakes the earth from its place so that its pillars quake —",
      "T": "— who can rattle the entire earth loose from its foundations, leaving the pillars of the world shuddering —"
    },
    "7": {
      "L": "who commands the sun and it does not rise, and seals up the stars —",
      "M": "who commands the sun not to rise, and seals up the stars —",
      "T": "— who can silence the sun with a single word, who can lock the stars away so they give no light —"
    },
    "8": {
      "L": "who alone stretched out the heavens and treads on the heights of the sea —",
      "M": "who alone stretched out the heavens and walks on the crests of the sea —",
      "T": "— the one who spread the heavens wide by himself, who walks the crests of the waves as easily as level ground —"
    },
    "9": {
      "L": "who made the Bear and Orion, the Pleiades and the chambers of the south —",
      "M": "who made the Bear, Orion, and the Pleiades, and the constellations of the southern sky —",
      "T": "— who crafted the Bear and Orion and the Pleiades, the whole wheeling architecture of the night sky, every constellation in its chamber —"
    },
    "10": {
      "L": "who does great things past finding out, and marvelous things without number.",
      "M": "who does great things beyond comprehension and marvelous things without number.",
      "T": "His works are beyond calculation and beyond comprehension — wonder upon wonder upon wonder, and no end to them."
    },
    "11": {
      "L": "Lo, he passes by me, and I do not see him; he moves on, and I do not perceive him.",
      "M": "When he passes by me, I cannot see him; when he moves on, I cannot perceive him.",
      "T": "He sweeps right past me and I see nothing. He is there and then gone, and I have not detected even the edge of his passing."
    },
    "12": {
      "L": "Behold, he seizes — who can turn him back? Who will say to him, 'What are you doing?'",
      "M": "If he snatches something away, who can stop him? Who will dare say to him, 'What are you doing?'",
      "T": "He takes what he wants. Who stops him? Who dares ask him to account for himself?"
    },
    "13": {
      "L": "God will not turn back his anger; beneath him the helpers of Rahab bowed down.",
      "M": "God does not restrain his anger; even the allies of Rahab crouched beneath him.",
      "T": "Even the chaos-dragon Rahab and all his armies were crushed before God. He does not calm his wrath for myths, let alone for men."
    },
    "14": {
      "L": "How then can I answer him, or choose out my words with him?",
      "M": "How then can I answer him, or select my words to argue before him?",
      "T": "If chaos-monsters cannot withstand him — what am I supposed to say? What words would I even choose for a case I cannot win?"
    },
    "15": {
      "L": "Though I were righteous, I could not answer him; I could only implore grace from my judge.",
      "M": "Even if I were righteous, I could not answer him; I would have to plead for mercy to my own judge.",
      "T": "Even if I were completely innocent, I could not mount a defense. I would have to beg for mercy from the very one who is prosecuting me — the judge who is also the plaintiff."
    },
    "16": {
      "L": "If I called and he answered me, I would not believe he was truly listening to my voice.",
      "M": "If I summoned him and he responded, I still could not believe he was truly listening to me.",
      "T": "Even if he answered my summons, I could not trust the encounter. He is too far beyond me. How could I know he was actually hearing my words, and not simply humoring the noise I make?"
    },
    "17": {
      "L": "For he crushes me with a tempest and multiplies my wounds without cause.",
      "M": "For he would crush me with a storm and multiply my wounds for no reason.",
      "T": "He would simply overwhelm me — a whirlwind of affliction with no reason given. Wound upon wound piled on for nothing."
    },
    "18": {
      "L": "He will not let me recover my breath, but fills me with bitterness.",
      "M": "He does not let me catch my breath, but fills me with bitter suffering.",
      "T": "He gives no space to breathe — no pause between one agony and the next. Only bitterness, filling every hollow place inside me."
    },
    "19": {
      "L": "If it is strength — behold, he is mighty! If it is justice — who will summon him?",
      "M": "If it is a contest of strength, he is the stronger; if it is a matter of justice, who can summon him to court?",
      "T": "Contest of raw power? He wins without effort. Legal process? You cannot even serve him papers. There is no arena in which this match is remotely fair."
    },
    "20": {
      "L": "Though I were righteous, my own mouth would condemn me; though I were blameless, he would prove me perverse.",
      "M": "If I justified myself, my own mouth would condemn me; if I declared myself blameless, he would prove me twisted.",
      "T": "If I tried to argue my innocence, my own tongue would betray me before I finished the sentence. If I claimed to be whole, the mere encounter with him would expose every crack in me."
    },
    "21": {
      "L": "I am blameless; I do not know my own self; I despise my life.",
      "M": "Though I am blameless, I do not trust my own self-knowledge; I despise my own life.",
      "T": "I am blameless — and yet I can no longer trust what I know about myself. And as for this life of mine? I am done with it."
    },
    "22": {
      "L": "It is all one; therefore I say: he destroys both the blameless and the wicked.",
      "M": "It is all the same to me; this is why I say: he destroys the blameless and the wicked alike.",
      "T": "And this is what I have concluded: it makes no difference. God sweeps away the innocent and the guilty in the same motion. The moral accounting does not add up."
    },
    "23": {
      "L": "When disaster suddenly kills, he mocks at the despair of the innocent.",
      "M": "When sudden disaster brings death, he mocks at the calamity of the innocent.",
      "T": "When catastrophe strikes and the innocent die without warning — God laughs at their terror. That is what it looks like from where I stand, though I cannot bring myself to rest there."
    },
    "24": {
      "L": "The earth is given into the hand of the wicked; he covers the faces of its judges. If not he, then who?",
      "M": "The earth is given into the power of the wicked; he blindfolds its judges. If not he, then who?",
      "T": "The world is handed over to the wicked. The ones who should see justice done — God has covered their eyes. If not God, who arranged this? Someone tell me."
    },
    "25": {
      "L": "Now my days are swifter than a runner; they flee away and see no good.",
      "M": "My days are swifter than a runner; they flee away, seeing no good.",
      "T": "My days sprint past with nothing to stop them and nothing good to pause for. They arrive empty and leave the same way."
    },
    "26": {
      "L": "They pass by like boats of reed, like an eagle swooping on its prey.",
      "M": "They glide away like skiffs of reed, like an eagle diving on its prey.",
      "T": "Like a reed skiff skimming the surface of the water. Like an eagle folding its wings for the kill — that fast, and that final."
    },
    "27": {
      "L": "If I say, 'I will forget my complaint, I will set aside my sad face, and be cheerful' —",
      "M": "If I say, 'I will forget my complaint, I will put on a cheerful face and be bright' —",
      "T": "Sometimes I think: what if I simply changed my approach? Forgot the grief, forced a smile, decided to act as if things were well —"
    },
    "28": {
      "L": "I am afraid of all my suffering, for I know you will not hold me innocent.",
      "M": "I dread all my suffering, for I know you will not acquit me.",
      "T": "— but then the dread rises again. All these wounds. And I know — I simply know — that you will not clear my name. The fear will not let me rest."
    },
    "29": {
      "L": "I shall be found wicked; why then do I labor in vain?",
      "M": "If I am condemned already, why do I exhaust myself for nothing?",
      "T": "The verdict is already written. I am condemned before I open my mouth. Then why am I wearing myself out on a case that is already closed?"
    },
    "30": {
      "L": "If I wash myself with snow water and cleanse my hands with lye —",
      "M": "Even if I washed myself with snow water and cleansed my hands with soap —",
      "T": "Even if I scrubbed myself clean — snow water, the strongest soap — until every stain and trace of impurity was gone —"
    },
    "31": {
      "L": "— then you would plunge me into a pit, so that my own garments would abhor me.",
      "M": "— you would still plunge me into a slime pit so that my own clothes would recoil from me.",
      "T": "— you would thrust me into a pit of filth the moment I tried to stand clean. Even my own clothes would be revolted by what you had made of me."
    },
    "32": {
      "L": "For he is not a man as I am, that I could answer him, that we might come to court together.",
      "M": "For he is not a man as I am, that I could answer him or that we could appear in court together.",
      "T": "He is not human. I cannot meet him on equal terms. We cannot stand before the same judge, because there is no judge above him. There is no court that holds both of us."
    },
    "33": {
      "L": "There is no arbiter between us who might lay his hand upon us both.",
      "M": "There is no umpire between us who could place his hand upon us both.",
      "T": "If only there were a mediator — someone who could lay a hand on each of us, who could hold the space between God and man and make the encounter possible. But no such person exists."
    },
    "34": {
      "L": "Let him take his rod away from me, and let not the terror of him terrify me.",
      "M": "Let him remove his rod from me, and let his terror not overwhelm me.",
      "T": "If only he would set down the rod. If only his sheer presence did not shatter every thought I am trying to form before I can speak it."
    },
    "35": {
      "L": "Then I would speak, and I would not fear him, for I am not so within myself.",
      "M": "Then I would speak without fear, for I am not so in myself.",
      "T": "Then — then I could speak. I could say what needs to be said without the fear crushing the words before they reach my lips. But I am not there. I am not that person. Not yet. Not like this."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 7–9 written.')

if __name__ == '__main__':
    main()
