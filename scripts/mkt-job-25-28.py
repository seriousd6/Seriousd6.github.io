"""
MKT Job chapters 25–28 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-25-28.py

=== Overview of this unit ===

Ch 25 — Bildad's third (and final) speech: 6 verses. The shortest speech in the book.
         Theology of divine majesty and human unworthiness — compressed and cold.
Ch 26 — Job's response: sarcastic rebuttal (vv.1–4) followed by a magnificent cosmic
         hymn to divine power (vv.5–14), outstripping anything the friends have said.
Ch 27 — Job's integrity oath under the very God who is tormenting him (vv.1–6), then a
         curse on his enemies (v.7), then the fate of the wicked (vv.13–23) — ironically
         using the friends' own weapon.
Ch 28 — The Hymn to Wisdom: where is wisdom found? Not in the deep, not in the market,
         not visible to falcon or lion. Only God knows. The human answer: fear of the
         Lord. One of the finest poems in the Hebrew Bible.

=== Contested-term decisions ===

H410  (אֵל, El): "God" in all tiers. Standard Job usage.
H433  (אֱלוֹהַּ, Eloah): "God" in all tiers (singular poetic form; Job uses it heavily).
H7706 (שַׁדַּי, Shaddai): "the Almighty" in all tiers — title is too resonant to reduce.
H136  (אֲדֹנָי, Adonai, 28:28): "the Lord" in L/M; "the Lord" in T. Adonai rather than
      the tetragrammaton; "the Lord" with initial cap is accurate.
H3068 (יהוה): not present in these chapters (poetic core of Job uses El/Eloah/Shaddai).

H7307 (רוּחַ, ruach): rendered by context:
      26:13 — "his Spirit" (divine agency adorning the heavens) — capital S; L/M/T.
      27:3  — "the spirit of God" in L; "God's breath" in T — the animating breath-spirit.
      28:25 — "the wind" (context is measuring weather phenomena) — lower case, natural.

H5315 (נֶפֶשׁ, nefesh): embodied self throughout; not the Greek immaterial soul.
      27:2  — "my soul" in L; "me" in M; "everything inside me" in T.
      27:8  — "his soul" in L; "his life" in M/T — the life-force God withdraws.

H2451 (חָכְמָה, chokmah): "wisdom" throughout; the entire theme of ch.28.
H998  (בִּינָה, binah): "understanding" throughout; paired with wisdom in ch.28.
H3374 (יִרְאָה, yirah): "the fear of" in L/M; "reverent awe" or "fear" in T (28:28).

H2611 (חָנֵף, chaneph, 27:8): "hypocrite" in L (KJV tradition, retained for L only);
      "godless" in M/T. Carried forward from chs.13–18.
H7563 (רָשָׁע, rasha): "wicked" in all tiers. Dominant throughout ch.27's fate poem.

H7293 (רַהַב, Rahab, 26:12): the chaos-monster — the personified primordial sea of disorder.
      L: "Rahab" (the proper name, retained). M: "the sea dragon" (gloss for clarity).
      T: "Rahab, the chaos-dragon" — surfaces the mythological register deliberately.
      This is not the Rahab of Joshua 2; it is the Canaanite / ANE sea-monster motif
      that the Psalmists and Isaiah also deploy (Ps 89:10; Isa 51:9).

H1281 (בָּרִחַ, bariach, 26:13): "the fleeing serpent" / "the twisting serpent" —
      Leviathan-adjacent imagery; forms a pair with Rahab. L: "the fleeing serpent."
      M: "the twisting serpent." T: "the ancient serpent that fled."

H7496 (רְפָאִים, rephaim, 26:5): the shades of the dead under the waters. L: "the shades."
      M: "the dead" for readability. T: "the shades of the departed."

H11   (אֲבַדּוֹן, Abaddon): "Abaddon" in all tiers — the abyss beneath Sheol; a proper
      name retained across all tiers for its resonance.
H7585 (שְׁאוֹל, Sheol): "Sheol" in all tiers — preserved as a proper name.

H120  (אָדָם, adam, 25:6; 28:28): "man/mankind" in L/M; "human being/mankind" in T.
H582  (אֱנוֹשׁ, enosh, 25:6; 28:13): "man/mortal" in L; "mortal/human being" in T.

=== Aspect and tense notes ===

Ch.25: Bildad's speech uses perfects to state settled theological facts (God's dominion
       is established; the heavens are not clean). The rhetorical questions (vv.4–6) are
       present-tense challenges. T should preserve the compressed, conclusory quality —
       Bildad is not arguing; he is declaring verdicts.

Ch.26: The sarcastic rhetorical questions (vv.2–4) are completed acts — Job addresses
       what Bildad just finished doing. The cosmic hymn (vv.5–14) is in the perfect
       (established acts of creation and ongoing governance). T renders the hymn with
       cadence — it should read like a poem, not a theology lecture.

Ch.27: The oath formula ("As God lives") sets the solemn mode. Job's integrity statements
       (vv.4–6) are strong imperfects of resolve ("will not / shall not"). The fate-of-the-
       wicked section (vv.13–23) uses imperfects throughout — the doom rolls forward,
       ongoing, relentless, never finished. T surfaces this as a grinding present.

Ch.28: The Hymn to Wisdom uses a narrative past for the mining description (vv.1–11),
       then a searching present for the wisdom-quest (vv.12–19, 20–22), then a past
       narrative for God's creative acts (vv.25–27). The refrain (vv.12, 20) is identical
       in the Hebrew — T should honor that structural echo.

=== OT echo notes ===

26:12 — Rahab as chaos-monster echoes Ps 89:10; Isa 51:9. T surfaces this register.
26:13 — "crooked/fleeing serpent" echoes Isa 27:1 (Leviathan). Job and Second Isaiah
         draw from the same ANE mythological pool to describe God's victory over chaos.
27:2  — Job swears by the God who wronged him. This is a remarkable inversion: the
         divine name invoked as guarantor against the divine actor. T notes the paradox.
28:28 — "Fear of the Lord is wisdom" echoes Prov 1:7 and Ps 111:10. But in Job's
         context the statement is more tragic: wisdom, after all this searching, turns
         out to be not a discovery but a posture — not acquired but inhabited. T honors
         both the echo and the particular weight it carries in Job's situation.

=== Structural notes ===

Ch.26 vv.5–14 form a carefully ordered hymn: from the underworld up (v.5–6), to the
cosmic frame (v.7), to the waters (v.8), to the divine throne (v.9), to the horizon
(v.10), to the pillars of heaven (v.11), to the sea and its monster (v.12), to the
heavens above (v.13), and finally the humbling conclusion: all this is the fringe (v.14).
The movement is vertical — from Sheol at the bottom to the heavens at the top — and the
final verse zooms out to show the entire survey was the hem of God's robe.

Ch.28 has a two-refrain structure (vv.12 and 20 are identical). The poem breaks into:
stanza A (vv.1–11): what humans CAN find — mineral wealth, in the deepest dark;
stanza B (vv.12–19): what they CANNOT buy — wisdom, at any price;
stanza C (vv.20–27): where wisdom actually lives — with God, woven into creation;
conclusion (v.28): what wisdom looks like for humans — fear of the Lord.
T should honor the stanzaic structure by giving each stanza a distinct texture.
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
  # ============================================================
  # Chapter 25 — Bildad's Third Speech: Six Verses of Cold Theology
  # ============================================================
  "25": {
    "1": {
      "L": "And Bildad the Shuhite answered and said:",
      "M": "Then Bildad the Shuhite answered:",
      "T": "Bildad the Shuhite spoke:"
    },
    "2": {
      "L": "Dominion and dread are with him; he maketh peace in his high places.",
      "M": "Dominion and dread belong to him; he makes peace in his high places.",
      "T": "Power and dread — these are his, and nothing beside. In the heights above all heights, he holds everything in order. Peace in his realm is not negotiated; it is imposed."
    },
    "3": {
      "L": "Is there any number to his armies? And upon whom doth not his light arise?",
      "M": "Can his armies be counted? Upon whom does his light not rise?",
      "T": "Who could count the armies of God? His light falls on everyone — no corner is dark enough to escape it. These are not arguments; these are settled facts Bildad is reciting from a safe distance."
    },
    "4": {
      "L": "How then can a man be justified with God? Or how can he be clean who is born of a woman?",
      "M": "How can any mortal be declared righteous before God? How can anyone born of a woman be clean?",
      "T": "Which means — and this is the point Bildad has been building toward — no human being can stand as righteous before God. Born of a woman: already compromised, already too small, too earthy, too mortal to meet the standard of infinite holiness."
    },
    "5": {
      "L": "Behold, even the moon shineth not, and the stars are not pure in his sight.",
      "M": "Even the moon gives no real light before him; the very stars are not pure in his sight.",
      "T": "The moon — that great lamp hung in the sky — gives no light that holds before him. The stars that burn cold across the heavens: they are not clean enough. Not pure enough. If the lights of heaven fall short, the argument runs itself to its conclusion."
    },
    "6": {
      "L": "How much less man, that is a maggot, and the son of man, that is a worm!",
      "M": "How much less a mortal, who is a maggot, and a human being, who is a worm!",
      "T": "And if the stars are not pure enough — what then is the human being? A maggot. That is Bildad's word. The son of man: a worm. He has compressed his entire theology into two words, and he does not notice how much they leave out — the image of God, the covenant, the innocent man sitting in front of him."
    }
  },

  # ============================================================
  # Chapter 26 — Job's Rebuttal: Sarcasm + Cosmic Hymn
  # ============================================================
  "26": {
    "1": {
      "L": "But Job answered and said:",
      "M": "Then Job answered:",
      "T": "Job answered:"
    },
    "2": {
      "L": "How hast thou helped him that is without power! How hast thou saved the arm that hath no strength!",
      "M": "What help you have given to the powerless! What strength you have brought to the feeble arm!",
      "T": "Magnificent. The man without strength is now fully rescued, thanks to your words. The arm that could not lift itself has been saved by your intervention. Well done, Bildad."
    },
    "3": {
      "L": "How hast thou counselled him that hath no wisdom! And how plentifully hast thou declared sound understanding!",
      "M": "What counsel you have given to one with no wisdom! How abundantly you have set out sound understanding!",
      "T": "And the wisdom — poured out in such abundance. Every fact laid bare, every principle of theology delivered at full volume. To a man who apparently had nothing before you arrived."
    },
    "4": {
      "L": "To whom hast thou uttered words? And whose spirit came out from thee?",
      "M": "Who are you addressing with these words? And whose spirit was speaking through you?",
      "T": "One question: who exactly are you talking to? I am not in need of your philosophy. And — since we are asking — whose spirit produced all this? Because I do not hear God in it. I hear Bildad."
    },
    "5": {
      "L": "The shades tremble beneath the waters and those that dwell under them.",
      "M": "The shades of the dead tremble under the waters, even those who dwell beneath them.",
      "T": "Here is what I know about God — and it is more than you have said. Even the dead — the shades in the deep — tremble. Below the water, below the ocean floor, the realm of the departed shudders before him."
    },
    "6": {
      "L": "Sheol is naked before him, and Abaddon hath no covering.",
      "M": "Sheol is laid bare before him, and Abaddon has no covering.",
      "T": "Sheol itself — the realm of the dead — stands naked and exposed before him. And Abaddon, the abyss beneath Sheol, wears no veil from his sight. Nothing is hidden from him. Not even death's deepest room."
    },
    "7": {
      "L": "He stretcheth out the north over empty space and hangeth the earth upon nothing.",
      "M": "He stretches out the north over the void and hangs the earth on nothing.",
      "T": "He has stretched the northern sky over empty space — the void, the formless nothing — and suspended the whole earth on nothing. No foundation beneath, no pillar below. The earth hangs by his will alone. Bildad described his armies. I am describing his cosmology."
    },
    "8": {
      "L": "He bindeth up the waters in his thick clouds, and the cloud is not rent under them.",
      "M": "He wraps the waters in his thick clouds, and the cloud holds without bursting.",
      "T": "He holds the water in the clouds — wraps it in vapor, which should not be able to hold it — and the clouds do not tear under the weight. They hold because he holds them."
    },
    "9": {
      "L": "He holdeth back the face of his throne and spreadeth his cloud over it.",
      "M": "He screens the face of his throne and spreads his cloud over it.",
      "T": "The throne of God is veiled — hidden behind cloud. Not because he is absent; because the full sight of him would overwhelm. He covers his throne for the sake of what is beneath it."
    },
    "10": {
      "L": "He hath drawn a circular bound upon the face of the waters at the boundary of light and darkness.",
      "M": "He has drawn a circle on the face of the waters, marking the boundary between light and dark.",
      "T": "Where the light ends and the dark begins — he drew that line. Precisely there. The horizon is not an accident; it is the boundary he set between day and night, a decree inscribed on the surface of the sea."
    },
    "11": {
      "L": "The pillars of heaven tremble and are astonished at his rebuke.",
      "M": "The pillars of heaven tremble and are stunned at his rebuke.",
      "T": "Even the cosmic pillars — the supports of the sky, the foundations of what holds heaven up — shake when he speaks in anger. They are not just shaken; they are stunned. His rebuke alone is enough to make the frame of the universe react."
    },
    "12": {
      "L": "By his power he stilleth the sea; by his understanding he smiteth through Rahab.",
      "M": "By his power he calmed the sea; by his understanding he crushed the sea dragon.",
      "T": "With raw power he quieted the sea — that ancient, unruly force. And Rahab, the chaos-dragon, the primordial monster that personifies disorder: he struck it down. Not with brute force alone — with understanding. Chaos was defeated by wisdom."
    },
    "13": {
      "L": "By his Spirit the heavens were adorned; his hand hath pierced the fleeing serpent.",
      "M": "His Spirit made the heavens beautiful; his hand transfixed the twisting serpent.",
      "T": "The Spirit went out from him and the heavens themselves became beautiful — ordered, luminous. And the serpent that fled, the ancient serpent that twisted and writhed through chaos: his hand reached it. Nothing that flees from him escapes. Even the crooked, primordial thing was pierced."
    },
    "14": {
      "L": "Lo, these are the outskirts of his ways; and how faint a whisper is heard of him! The thunder of his power — who can understand it?",
      "M": "These things are but the edges of his ways; how faint a whisper we catch of him! The thunder of his full power — who can comprehend it?",
      "T": "Everything Job has just described — all of it — is the fringe. The outermost edge of what can be said about God. What we actually hear of him is a faint whisper at the limit of human perception. The full thunder of his power: no one can comprehend it. Job knows this, and says so. That is the difference between him and his friends."
    }
  },

  # ============================================================
  # Chapter 27 — Job's Oath + Fate of the Wicked
  # ============================================================
  "27": {
    "1": {
      "L": "Moreover Job continued his parable and said:",
      "M": "And Job again took up his discourse and said:",
      "T": "Job continued, taking up his speech again:"
    },
    "2": {
      "L": "As God liveth, who hath taken away my right, and the Almighty, who hath made my soul bitter —",
      "M": "As God lives, who has denied me justice, and the Almighty, who has made me bitter —",
      "T": "I swear by God — the very God who has stripped me of my right, the Almighty who has made everything inside me bitter. I swear by him, because he is the only one left to swear by. Even when the oath runs against him, he is still the only witness I have."
    },
    "3": {
      "L": "All the while my breath is in me, and the spirit of God is in my nostrils —",
      "M": "For as long as my breath remains and God's breath is in my nostrils —",
      "T": "— while I still breathe. While the life God gave me still moves in my nostrils. While there is anything left of me here —"
    },
    "4": {
      "L": "My lips shall not speak wickedness, nor my tongue utter deceit.",
      "M": "My lips will not speak wickedness, and my tongue will not utter deception.",
      "T": "— I will not lie. Not here, not to make peace. I will not say that wickedness came out of my own mouth and deserved this. I will not let my tongue manufacture a deception that satisfies your theology at the cost of the truth."
    },
    "5": {
      "L": "Far be it from me to justify you; till I die I will not remove mine integrity from me.",
      "M": "God forbid that I should agree you are right; until I die I will not surrender my integrity.",
      "T": "Never. I will not vindicate you — not your argument, not your verdict on me. I refuse. Whatever I lose, I will not surrender integrity. I will carry it to my death before I let it go. It is the last thing I have that cannot be taken."
    },
    "6": {
      "L": "My righteousness I hold fast and will not let it go; my heart reproacheth me not for any of my days.",
      "M": "I hold fast to my righteousness and will not release it; my heart does not condemn me for a single day I have lived.",
      "T": "I have lived a full life and held the record in my own hands, and my heart will not accuse me. Not one day. My conscience is not against me. My righteousness holds me and I hold it. Neither of us will let go."
    },
    "7": {
      "L": "Let mine enemy be as the wicked and he that riseth up against me as the unrighteous.",
      "M": "Let my enemy be treated as the wicked, and whoever rises against me as the unrighteous.",
      "T": "Anyone who wants my downfall — let them have what the wicked get. Let them be on the receiving end of the theology you have been deploying against me. Because I am not the wicked man. And I am willing to let God sort the evidence."
    },
    "8": {
      "L": "For what is the hope of the hypocrite though he gain, when God taketh away his soul?",
      "M": "For what hope does the godless man have, however much he gains, when God takes away his life?",
      "T": "Here is the real question: what does the godless man hope for, in the end? He may have gained everything — accumulated, profited, built an empire. But when God takes the life he built on — what is any of it worth? The gains evaporate with the life that held them."
    },
    "9": {
      "L": "Will God hear his cry when trouble cometh upon him?",
      "M": "Will God hear his cry when trouble comes upon him?",
      "T": "And when the disaster arrives — and it does arrive, for such a man — does God answer the prayer? When the godless man finally cries out, is anyone listening? That question deserves the silence it gets."
    },
    "10": {
      "L": "Will he delight himself in the Almighty? Will he always call upon God?",
      "M": "Does he take delight in the Almighty? Does he call upon God at all times?",
      "T": "Has he cultivated any living relationship with the Almighty? Has prayer been his habit — a daily practice, a genuine delight — or only something he reaches for when the disaster is already at his door? The answer speaks for itself."
    },
    "11": {
      "L": "I will teach you concerning the hand of God; that which is with the Almighty I will not conceal.",
      "M": "I will instruct you about the hand of God; I will not hide what the Almighty has shown me.",
      "T": "I will tell you what I actually know. The hand of God — how it works, what it does — I will instruct you in this. I will not withhold the truth of it. Unlike what you have done to me with your doctrine."
    },
    "12": {
      "L": "Behold, all ye yourselves have seen it; why then are ye altogether vain?",
      "M": "Look — you yourselves have seen all this; why then have you become so thoroughly empty?",
      "T": "You have all seen with your own eyes the same creation I see, the same evidence I have. So why has your theology become such emptiness — such wind, such vapor? You had the truth in front of you. Where did you go with it?"
    },
    "13": {
      "L": "This is the portion of a wicked man with God and the heritage of oppressors which they receive of the Almighty.",
      "M": "This is the lot God assigns to a wicked man, and the inheritance oppressors receive from the Almighty.",
      "T": "Now: the fate of the wicked. Not because I am wicked — I have just established that under oath — but because you want to talk about it. Fine. Here is what the wicked actually receive. Not what I receive, but what they receive. Listen carefully to the difference."
    },
    "14": {
      "L": "If his children be multiplied, it is for the sword; and his offspring shall not be satisfied with bread.",
      "M": "If his children multiply, it is only for the sword; his descendants will not have enough to eat.",
      "T": "Many children — and what does it get him? The sword. More descendants means more targets for catastrophe. His line, his offspring: they will not eat. There is no abundance waiting for the family of the wicked, however large that family grows."
    },
    "15": {
      "L": "Those that remain of him shall be buried in death, and his widows shall not weep.",
      "M": "His survivors will be buried by plague, and his widows will not weep for them.",
      "T": "Whatever is left of him — whoever survives the sword and the famine — will be buried by pestilence. And the widows will not weep. Not from hardness of heart: from isolation so complete that grief cannot find its way to the surface."
    },
    "16": {
      "L": "Though he heap up silver as the dust and prepare raiment as the clay —",
      "M": "Though he pile up silver like dust and lay up clothing as plentiful as clay —",
      "T": "Say he accumulated everything. Silver in heaps like dirt, piled up past counting. Clothing stored in quantities no one could ever wear. All that material wealth, all that visible abundance —"
    },
    "17": {
      "L": "He may prepare it, but the just shall put it on, and the innocent shall divide the silver.",
      "M": "He may store it all up, but the righteous man will wear it, and the innocent will share out the silver.",
      "T": "— he does not keep it. The righteous man wears his clothing. The innocent man divides his silver. The wicked man is the procurement department for the people he spent his life despising. Everything he gathered passes to the ones he looked down on."
    },
    "18": {
      "L": "He buildeth his house as a moth buildeth it, and as a booth that the watchman maketh.",
      "M": "He builds his house as a moth builds its web, and like the temporary shelter a watchman puts up.",
      "T": "The house he built — it is a moth's work. Light, fragile, gone at the first hard touch. A temporary watchman's hut, put up for a season and abandoned when the season ends. He built it and called it permanent. It was never permanent."
    },
    "19": {
      "L": "The rich man lieth down and shall not be gathered again; he openeth his eyes, and is not.",
      "M": "The rich man lies down, but is not gathered to his fathers; he opens his eyes, and is gone.",
      "T": "He goes to sleep wealthy. He wakes — and he is gone. Or: he wakes and finds everything gone. One night's sleep is the hinge on which his entire life turns. He is not gathered in with anyone. He ends alone in his disappearing."
    },
    "20": {
      "L": "Terrors overtake him like waters; a tempest stealeth him away in the night.",
      "M": "Terrors sweep over him like a flood; a storm carries him off in the night.",
      "T": "In the night — which he thought was safe — the terrors come like rushing water. A whirlwind. A storm that no one predicted. And it steals him away while he sleeps. The powerful man does not disappear in public; he disappears in the dark, when no one is watching."
    },
    "21": {
      "L": "The east wind carrieth him away and he departeth; and a storm hurleth him out of his place.",
      "M": "The east wind sweeps him away and he is gone; a storm flings him from his home.",
      "T": "The east wind — the desert wind, the scorching, stripping wind — picks him up. He goes. There is no resistance possible against it. And the storm hurls him away from the place he called his own, the home he built his identity around. Distance. Dislocation. He is somewhere else now, and he cannot find his way back."
    },
    "22": {
      "L": "For God shall cast upon him and not spare; he would fain flee out of his hand.",
      "M": "For God hurls his power at him without mercy; the man would desperately flee from his hand.",
      "T": "God himself drives this. He throws his power at the wicked man without any mercy, without restraint. And the wicked man — all that wealth, all that confidence — now he only wants to run. He would flee from God's hand if he could. But there is nowhere to go."
    },
    "23": {
      "L": "Men shall clap their hands at him and shall hiss him out of his place.",
      "M": "Men clap their hands at him and hiss him away from his home.",
      "T": "And the crowd watches the end of it. They clap — not in applause; the clapping of contempt, the rhythmic mockery of the powerful brought low. They hiss. He is chased out of his place by the sound of other people's derision. The man who was feared becomes a figure of public scorn."
    }
  },

  # ============================================================
  # Chapter 28 — The Hymn to Wisdom
  # ============================================================
  "28": {
    # --- Stanza A: What Humans CAN Find (vv.1–11) ---
    "1": {
      "L": "Surely there is a mine for the silver and a place for gold where they refine it.",
      "M": "Surely silver has its mine, and gold a place where it is refined.",
      "T": "There is a place you can go to find silver. You can locate the vein, trace it through rock, bring it up and smelt it. Gold has its mine, its smelter, its process, its address in the earth."
    },
    "2": {
      "L": "Iron is taken out of the earth, and copper is molten out of the stone.",
      "M": "Iron is taken from the earth, and copper is smelted from ore.",
      "T": "Iron comes out of the ground. Copper melts out of rock. These are findable, locatable, extractable things. The earth gives them up if you know where to look and are willing to do the work."
    },
    "3": {
      "L": "He setteth a limit to the darkness and searcheth out to its furthest reach the stone in thick darkness and in the shadow of death.",
      "M": "A miner sets a limit to the darkness and searches to its utmost depth for stone in deep shadow.",
      "T": "The miner puts an end to the dark — drives it back with a torch, pushes down into the shaft past where any natural light reaches. He goes into the shadow that feels like death itself, the deep dark where sunlight has never been, and he finds the stone there."
    },
    "4": {
      "L": "A shaft is broken open far from men's dwellings; forgotten by the foot of travelers, they hang far from others, they swing.",
      "M": "Far from where people live, a shaft is sunk; forgotten by travelers' feet, the miners dangle far from others and sway.",
      "T": "Deep in the earth, removed from every ordinary path, a shaft opens where no traveler thinks to look. The workers go down into it, swinging in the dark far below the surface world, suspended by ropes, forgotten by anyone above. They are among the most isolated workers on earth."
    },
    "5": {
      "L": "As for the earth, out of it cometh bread, but under it is turned up as it were fire.",
      "M": "The earth produces bread from its surface, but underneath it is turned up as though by fire.",
      "T": "The same earth that grows grain on its surface — underneath, it burns. The farmer and the miner work the same earth in opposite directions: one cultivates the top, tending what grows upward; the other excavates the bottom, where the rock is hot as fire."
    },
    "6": {
      "L": "The stones of it are the place of sapphires, and it hath dust of gold.",
      "M": "Its stones are the source of sapphires, and it holds flakes of gold.",
      "T": "Down there: sapphires set in the stone, gold in the dust. Beauty buried in the dark — present, findable, waiting."
    },
    "7": {
      "L": "A path that no bird of prey knoweth and which the falcon's eye hath not seen.",
      "M": "A path no bird of prey knows, unseen by the eye of the falcon.",
      "T": "The falcon — whose eye is the sharpest thing that moves through the air — has not seen this path. The bird of prey that spots a mouse from a hundred feet up: it does not know where the miner's road goes. No winged creature has found it."
    },
    "8": {
      "L": "The lion's whelps have not trodden it, nor the fierce lion passed by it.",
      "M": "The lion's cubs have not walked it, nor the fierce lion passed over it.",
      "T": "The most fearless predators on land — the lion's young who know no fear, the fierce lion itself — have not walked this road. The boldest natural creatures cannot go where the miner goes."
    },
    "9": {
      "L": "He putteth forth his hand upon the flint; he overturneth mountains by the roots.",
      "M": "He puts his hand to the flint; he uproots mountains from their foundations.",
      "T": "The miner's hand touches the hardest rock — flint — and works it. He overturns mountains from their deepest roots. This creature who is dust has the audacity to reach into the rock and reorganize the earth."
    },
    "10": {
      "L": "He cutteth out channels among the rocks; his eye seeth every precious thing.",
      "M": "He cuts channels through the rocks; his eye takes in every precious thing.",
      "T": "Through solid rock, he cuts channels — turns stone into rivers by force of will and labor. And whatever is valuable down there, his eye finds it. The human eye in the dark, in the depths: it finds the things no natural eye has ever reached."
    },
    "11": {
      "L": "He bindeth the streams from overflowing, and the thing that is hidden he bringeth to light.",
      "M": "He holds back the streams from seeping through, and brings hidden things out to the light.",
      "T": "Where water seeps through and threatens to flood the shaft, he stops it, holds it back. And what was buried in absolute darkness — the hidden thing, the secret thing — he brings it out into the light. This is the extraordinary achievement of human ingenuity: reaching into the secret places of the earth and making them yield."
    },
    # --- Refrain 1 + Stanza B: What Cannot Be Bought (vv.12–19) ---
    "12": {
      "L": "But where shall wisdom be found, and where is the place of understanding?",
      "M": "But where shall wisdom be found? And where is the place of understanding?",
      "T": "And now the question beneath the poem, the question the poem has been building toward: man can find silver. Man can locate gold. Man can sink shafts into the deepest dark and bring up sapphires. But wisdom — where is that found? Where do you go to locate understanding? Is there a vein for it? A shaft you can sink?"
    },
    "13": {
      "L": "Man knoweth not the price thereof, neither is it found in the land of the living.",
      "M": "No mortal knows the path to it, and it is not found in the land of the living.",
      "T": "No human being knows the way. No expedition has located it. The entire land of the living — everywhere people actually go, everywhere any foot has been — it is not there."
    },
    "14": {
      "L": "The deep saith, It is not in me; and the sea saith, It is not with me.",
      "M": "The deep says, 'It is not in me,' and the sea says, 'It is not with me.'",
      "T": "Go down to the primordial abyss, the deep beneath all deeps: 'Not here.' Cross to the sea, the vast and ancient ocean that seems to hold everything: 'Not here either.' Even the great waters, which hold so much, do not hold this."
    },
    "15": {
      "L": "It cannot be gotten for gold, neither shall silver be weighed for the price thereof.",
      "M": "It cannot be bought with gold, and its price cannot be paid in silver.",
      "T": "It is not purchasable. Gold will not buy it. Silver — you could weigh it out all day, balance after balance — cannot meet the price. There is no transaction available that exchanges wealth for wisdom."
    },
    "16": {
      "L": "It cannot be valued with the gold of Ophir, with the precious onyx or the sapphire.",
      "M": "It cannot be matched against the gold of Ophir, the precious onyx, or the sapphire.",
      "T": "Not comparable to the finest gold — the gold of Ophir, which was the ancient world's standard for excellence in precious things. Not equivalent to onyx, not priced at the level of sapphire. The poem is working through the entire catalog of precious materials, and none of them serve."
    },
    "17": {
      "L": "Gold and crystal cannot equal it, nor shall the exchange for it be in vessels of fine gold.",
      "M": "Gold and crystal cannot match its worth; it cannot be exchanged for any item of fine gold.",
      "T": "Gold and crystal together — all the beauty and rarity of both combined — cannot equal it. You cannot walk into any market and exchange something for wisdom. There is no item of fine gold that represents its value. The categories of commerce simply do not apply."
    },
    "18": {
      "L": "No mention shall be made of coral or of crystal; for the price of wisdom is above rubies.",
      "M": "Coral and crystal are not even worth mentioning; the value of wisdom is above rubies.",
      "T": "Coral — forget it. Crystal — not worth bringing up in the same conversation. Even rubies, which represent extraordinary value: wisdom is above them. All other precious things drop off the bottom of the scale when you are trying to price wisdom."
    },
    "19": {
      "L": "The topaz of Ethiopia shall not equal it, neither shall it be valued with pure gold.",
      "M": "The topaz of Cush cannot compare with it; it cannot be priced against pure gold.",
      "T": "Ethiopia's topaz — the finest gems from the south — cannot stand in the same sentence as wisdom. Pure gold: inadequate. The poem has exhausted every precious thing available to the ancient world. None of them serve. The search by wealth has failed completely."
    },
    # --- Refrain 2 + Stanza C: Where Wisdom Actually Lives (vv.20–27) ---
    "20": {
      "L": "Whence then cometh wisdom, and where is the place of understanding?",
      "M": "Where then does wisdom come from? And where is the place of understanding?",
      "T": "The question again — the same question, word for word. It has not been answered by listing everything that is not wisdom, every place it cannot be found. The refrain returns: where does wisdom actually come from?"
    },
    "21": {
      "L": "Seeing it is hid from the eyes of all the living and concealed from the fowls of the air.",
      "M": "It is hidden from the eyes of every living creature and kept from the sight of the birds of the sky.",
      "T": "Hidden from every living being. Concealed from the birds of the air — and we have established that the birds have the sharpest eyes. Even they cannot find wisdom by searching. The most acute natural sight on earth cannot locate it."
    },
    "22": {
      "L": "Abaddon and Death say, We have heard a rumor of it with our ears.",
      "M": "Abaddon and Death say, 'We have heard only a rumor of it.'",
      "T": "Even Abaddon — the place of destruction at the uttermost depth — even Death itself: they have only heard rumors of wisdom. They are not its location. They have a faint, distant report, a whisper of something they have never possessed. Even the realms beyond death know wisdom only from a distance."
    },
    "23": {
      "L": "God understandeth the way thereof and he knoweth the place thereof.",
      "M": "God understands the way to it and knows its location.",
      "T": "Only God. He knows the way to wisdom — not a rumor, not an echo, not the faint report that reaches even to Abaddon. He knows the actual path. He knows exactly where it lives, because he put it there."
    },
    "24": {
      "L": "For he looketh to the ends of the earth and seeth under the whole heaven.",
      "M": "For he looks to the ends of the earth and sees everything under all of heaven.",
      "T": "He can see it because he sees everything. The ends of the earth — visible to him. Everything under the entire span of heaven — visible to him. Nothing is at the edge of his sight, beyond his range. And wisdom, being woven into the fabric of creation, is entirely visible to its creator."
    },
    "25": {
      "L": "When he made a weight for the wind and measured out the waters by measure —",
      "M": "When he assigned a weight to the wind and measured the waters —",
      "T": "When he built the world: the wind — which seems weightless, unmeasurable, wild — he assigned it a weight. The waters — which seem boundless, uncontainable — he measured. These are the acts of one who has a precise, knowing relationship with every aspect of reality."
    },
    "26": {
      "L": "When he made a decree for the rain and a path for the lightning of the thunder —",
      "M": "When he established a decree for the rain and a path for the lightning and thunder —",
      "T": "— when he set the rain under law, gave the lightning its route through the sky, assigned thunder its voice. All of these things that seem random and uncontrolled are operating under decrees he laid down before we arrived."
    },
    "27": {
      "L": "Then did he see it and declare it; he prepared it and searched it out fully.",
      "M": "Then he saw it and made it known; he established it and fully searched it out.",
      "T": "At that moment of creation — when the world was being ordered — he saw wisdom. He declared it into being. He established it as part of the fabric of everything. He searched it out completely, from every angle. Wisdom was not an afterthought; it was woven into the act of making the world."
    },
    # --- Conclusion (v.28) ---
    "28": {
      "L": "And unto man he said: Behold, the fear of the Lord — that is wisdom; and to depart from evil is understanding.",
      "M": "And to mankind he said: The fear of the Lord is wisdom, and to turn from evil is understanding.",
      "T": "After all the places wisdom is not — after the deep, the sea, the gold, the birds, the realm of death itself — here is the answer given to human beings: the fear of the Lord. Reverent awe before the one who saw wisdom at creation and wove it into the world. And turning away from evil — that is understanding. Not something you acquire and possess; something you inhabit. Not found at the bottom of a shaft; found in the posture of a life."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 25–28 written.')

if __name__ == '__main__':
    main()
