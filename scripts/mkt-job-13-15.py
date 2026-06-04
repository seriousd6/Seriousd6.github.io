"""
MKT Job chapters 13–15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-13-15.py

=== Contested-term decisions ===

H582  (אֱנוֹשׁ, enosh): "mortal" (L) / "mortal man" (M) / "frail mortal" (T) — carried
      forward from chs.7–9. Enosh names humanity in its weakness and transience;
      Job and Eliphaz both use it deliberately in chs.14–15 to foreground fragility.

H120  (אָדָם, adam): "man" in all tiers when it means generic humanity (14:1; 15:16).
      15:7 ("Art thou the first man ever born?") carries a possible echo of the
      Adamic/primordial figure — T surfaces this as "the first Adam."

H1397 (גֶּבֶר, gever): "man" (L/M) / "mortal man" or "one" (T) — the strong word for
      the able-bodied male; appears in 14:10, 14:14. In context the strength of the
      word sharpens the pathos: even the vigorous man dies.

H7307 (רוּחַ, ruach): context-driven throughout —
      15:2  — "east wind" / "hot wind" — Eliphaz: Job's words are empty bluster
      15:13 — "spirit" — Job's inner disposition turned against God
      15:30 — "breath" — God's own breath/word that destroys the wicked's branches
      Capitalised "Spirit" not used; in chs.13–15 ruach refers to wind, attitude, or breath.

H5315 (נֶפֶשׁ, nefesh): "life" (13:14 — life held in hand as mortal risk); "soul" (14:22 —
      the mourning inner self of the dying man). Always embodied self, not Greek soul.

H7706 (שַׁדַּי, Shaddai): "Shaddai" (L) / "the Almighty" (M/T) — carried from chs.7–9.
      Appears in 13:3 and 15:25; both instances are contexts of confrontation or defiance.

H410  (אֵל, El): "God" in all tiers. Appears throughout.

H433  (אֱלוֹהַּ, Eloah): "God" in all tiers (15:8).

H7585 (שְׁאוֹל, Sheol): "Sheol" (L/M); "the realm of the dead" (T). Appears in 14:13.

H2611 (חָנֵף, chaneph): "hypocrite" (L — KJV tradition retained); "godless" (M/T).
      Root means profane, irreligious — L uses the traditional English rendering for
      recognisability; M/T use "godless" for semantic precision.

H3176 (יָחַל, yachal): "trust / hope / wait" — 13:15 is the crux: the MT reads
      "lo yachal" (he has no hope) vs. Qere "lo yachal" (he hopes in him). Following
      the Qere (which the KJV and most major translations adopt): "yet I will hope/trust
      in him." T renders this as the paradox it is — defiant faith against all logic.

=== Aspect and tense notes ===

Ch.13 mixes perfect and imperfect verbs throughout Job's speech. The imperfects (ongoing
action) dominate his description of his determination (v.3, 13, 15) — rendered as present
tense in M/T to capture the volitional aspect: "I will speak / I will argue."

Ch.14 is the most consistently poetic section. Imperfects denote ongoing or repeated states
of the human condition. The optative/wish construction (v.13: "O that thou wouldest...") is
the subjunctive of hope — T intensifies the conditional longing.

Ch.15 uses perfects for Eliphaz's accusations (completed acts: "you have undermined fear,"
"your mouth has declared your guilt"). The fate-of-the-wicked section (vv.20–35) shifts
entirely to imperfects — the wicked's torment is a continuing, unending experience. T
renders these as relentless present-tense description.

=== Structural notes ===

Ch.13: Job's address falls in two parts:
  vv.1–16 — Rebuttal of friends (they are liars, physicians of nothing, whitewash-artists)
  vv.17–27 — Direct address to God: formal legal deposition. Job orders his case (v.18)
             and demands God show him his charges (v.23).
  v.15 ("Though he slay me, yet will I hope in him") is the hinge — defiant trust in the
       face of imminent death; one of the most theologically significant verses in the book.
  v.28 functions as a coda: Job's body is already wasting like a moth-eaten garment.

Ch.14: A sustained elegy moving from brevity (vv.1–6) → contrast with a tree (vv.7–12)
       → the wish to hide in Sheol and be renewed (vv.13–17) → the collapse of that hope
       (vv.18–22). The tree comparison is central: a tree cut down will sprout again (v.7),
       but man, once dead, does not rise (v.12). The irony is that wood has more hope than
       flesh. The chapter ends not with resurrection hope but with the dead man still
       feeling his own pain and grief — the body is the locus of experience.

Ch.15: Eliphaz is sharper and more dismissive here than in ch.4. His Socratic challenge
       (vv.7–9) mocks Job's implicit claim to wisdom. The fate-of-the-wicked poem
       (vv.17–35) is meant to be a warning to Job — Eliphaz assumes Job is the wicked man
       described. T surfaces this subtext.

=== OT echo notes ===

14:1–2 echoes Psalm 103:15–16 and will itself be echoed in Job 38's divine speeches.
       The flower/shadow comparison is a wisdom commonplace, but Job's use is desolate
       rather than consoling.

14:14 "If a man die, shall he live again?" anticipates the central NT resurrection question.
      T notes this as the great unresolved question of the OT, answered only in Christ.

15:7–8 echoes primordial Adam traditions and possibly Proverbs 8:25 (Wisdom's prior
       birth before the hills). Eliphaz parodies the figure of primordial Wisdom/Man
       to mock Job's apparent self-elevation.

15:16 ("who drinks iniquity like water") parallels the wicked of Proverbs. T surfaces
      the contrast with ch.14's dying righteous man.
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
  "13": {
    "1": {
      "L": "Lo, all this mine eye hath seen, mine ear hath heard and understood it.",
      "M": "My eye has seen all of this; my ear has heard and understood it.",
      "T": "I have not missed a thing. My eyes have taken in everything you said; my ears have heard and turned it over. I understand it all."
    },
    "2": {
      "L": "What ye know, the same do I know also; I am not inferior unto you.",
      "M": "What you know, I know as well — I am not less than you.",
      "T": "Everything you claim to know — I know it too. I am not your intellectual inferior. Do not speak to me as if I were."
    },
    "3": {
      "L": "Surely I would speak to the Almighty, and I desire to reason with God.",
      "M": "I want to speak directly to the Almighty; I long to argue my case before God.",
      "T": "I am done with you. I want to take this to God himself — to Shaddai — and make my argument there, where it actually matters."
    },
    "4": {
      "L": "But ye are forgers of lies; ye are all physicians of no value.",
      "M": "But you — you are fabricators of lies; you are doctors who prescribe nothing but worthless remedies.",
      "T": "You are counterfeit healers. You show up with your theology and your diagnoses, and every word of it is a lie manufactured to fit your system. You are worse than useless."
    },
    "5": {
      "L": "O that ye would altogether hold your peace! And it should be your wisdom.",
      "M": "If only you would keep completely silent — that itself would be wisdom on your part.",
      "T": "The wisest thing you could do right now is say nothing. Your silence would be worth more than every word you have spoken."
    },
    "6": {
      "L": "Hear now my reasoning, and hearken to the pleadings of my lips.",
      "M": "Hear my argument now, and listen carefully to the pleadings of my lips.",
      "T": "Now hear me out. This is my case. Listen to the words forming on my lips — give them the hearing you have not given them yet."
    },
    "7": {
      "L": "Will ye speak wickedly for God? And talk deceitfully for him?",
      "M": "Will you speak falsehood on God's behalf? Will you tell lies for his sake?",
      "T": "You think you are defending God — but you are lying for him. Is that what he wants? Theological advocates who falsify the facts to protect his reputation?"
    },
    "8": {
      "L": "Will ye show partiality for him? Will ye contend for God?",
      "M": "Will you plead his case with favoritism? Will you act as God's lawyer?",
      "T": "You are prejudging the case before it has been heard and rigging it in his favor. Do you think God needs that? Needs you to shade the truth for him?"
    },
    "9": {
      "L": "Is it good that he should search you out? Or as one deceiveth a man, will ye so deceive him?",
      "M": "Will it go well when he examines you? Will you deceive him as one deceives a mortal man?",
      "T": "Think about what happens when God turns his scrutiny on you. You scheme to deceive him the way you would deceive a mortal — but he sees straight through every layer of it."
    },
    "10": {
      "L": "He will surely reprove you if ye do secretly show partiality.",
      "M": "He will certainly call you out if you show favoritism in secret.",
      "T": "The partiality you practice behind closed doors — he will expose it and answer for it. There is no private theology he cannot see."
    },
    "11": {
      "L": "Shall not his majesty terrify you? And his dread fall upon you?",
      "M": "Will not his majesty strike terror into you, and his dread overwhelm you?",
      "T": "His sheer greatness should have stopped your mouths by now. The weight of who he is — doesn't that land on you? Doesn't it silence the easy answers?"
    },
    "12": {
      "L": "Your memorable sayings are proverbs of ashes; your defenses are defenses of clay.",
      "M": "Your wise maxims are proverbs of ash; your arguments are arguments of clay.",
      "T": "All your celebrated wisdom — reduce it to its substance: ash. Blow on it and it scatters. Everything you have built your case on is clay, and clay does not hold."
    },
    "13": {
      "L": "Hold your peace from me, that I may speak; and let come upon me what will.",
      "M": "Be silent and leave me alone so I can speak; let whatever comes, come.",
      "T": "All of you — stop. I need silence, and I need it now. I am going to speak, and whatever happens to me for it, so be it. I accept the cost."
    },
    "14": {
      "L": "Why should I take my flesh in my teeth, and put my life in my hand?",
      "M": "Why do I risk my flesh in my teeth and put my life in my own hands?",
      "T": "I know I am taking a mortal risk — holding my life loosely in open hands — but the alternative is silence, and silence would be worse than death."
    },
    "15": {
      "L": "Though he slay me, yet will I hope in him; but I will surely defend my own ways before him.",
      "M": "Though he kills me, yet I will hope in him — but I will defend my own conduct before him.",
      "T": "Even if he kills me for it — and he might — I still hold to him. That is the paradox I cannot escape: I trust the one who is destroying me. But I will not surrender my case. I will argue my conduct before him to the last breath."
    },
    "16": {
      "L": "Even this shall be my salvation, that a godless person shall not come before him.",
      "M": "This itself will be my deliverance — no godless man can stand in his presence.",
      "T": "My very act of coming before God is proof of something. A genuinely godless person would never dare approach him. The fact that I press toward him is itself my argument."
    },
    "17": {
      "L": "Hear diligently my speech, and let my declaration be in your ears.",
      "M": "Listen carefully to my words; let my declaration reach your ears.",
      "T": "Let this land. I am not ranting. This is a prepared statement — hear every word."
    },
    "18": {
      "L": "Behold now, I have ordered my cause; I know that I shall be justified.",
      "M": "Look — I have laid out my case; I know that I will be vindicated.",
      "T": "I have marshaled my arguments. This is not desperation — this is reasoned confidence. When my case is heard, I will be cleared."
    },
    "19": {
      "L": "Who is he that will contend with me? For then I would be silent and give up the ghost.",
      "M": "Who is there who will bring a charge against me? For if there is one, I will be silent and die.",
      "T": "Is there anyone willing to press charges against me — actually answer me? If no one can, then I have proven my point. And if I must be silent, I would rather die than go back to this."
    },
    "20": {
      "L": "Only do not two things unto me; then will I not hide myself from your face.",
      "M": "Only do not do these two things to me, and I will not hide from your presence.",
      "T": "I am not asking for much, God. Just two concessions — grant them, and I will step out from hiding and face you."
    },
    "21": {
      "L": "Remove your hand far from me, and let not the dread of you terrify me.",
      "M": "Take your hand off me, and do not let terror of you overwhelm me.",
      "T": "First: withdraw your crushing hand. I cannot think, let alone speak, while that weight is on me. Second: take away the raw terror your presence generates. I need to be able to breathe in order to speak."
    },
    "22": {
      "L": "Then call, and I will answer; or let me speak, and you answer me.",
      "M": "Then call, and I will answer; or let me speak first, and you answer me.",
      "T": "The format doesn't matter: you start or I start. Either way — let us have this conversation. One of us speaks and the other answers. That is all I am asking."
    },
    "23": {
      "L": "How many are my iniquities and my sins? Make me know my transgression and my sin.",
      "M": "How many are my iniquities and sins? Tell me my transgression and my sin.",
      "T": "Just show me the charges. How many counts? What exactly am I accused of? I cannot defend myself against an indictment I have never seen."
    },
    "24": {
      "L": "Why do you hide your face, and count me as your enemy?",
      "M": "Why do you hide your face from me and treat me as your enemy?",
      "T": "Why the silence? Why do you turn away? You are treating me as if I were your opponent — but I am the work of your hands. When did I become your enemy?"
    },
    "25": {
      "L": "Will you frighten a windblown leaf? And will you chase dry stubble?",
      "M": "Will you pursue a leaf tossed in the wind? Will you hunt down dry stubble?",
      "T": "Look at me. I am a leaf in a gale — nothing. Dry stubble. This is your quarry? You are the Almighty, and this — this is what you are running down?"
    },
    "26": {
      "L": "For you write bitter things against me, and make me to inherit the iniquities of my youth.",
      "M": "You write bitter charges against me and saddle me with the sins of my youth.",
      "T": "The indictment you have written is bitter — and it reaches all the way back to what I did when I was young. You are holding everything. Every youthful stumble is in the file."
    },
    "27": {
      "L": "You put my feet in the stocks, and watch all my paths; you trace the prints of my feet.",
      "M": "You put my feet in stocks, you keep watch over all my paths, you mark the very prints of my feet.",
      "T": "My feet are locked. You monitor every path I move on. You trace my footprints in the dust — each one recorded, each one held against me. There is no movement of mine you do not track."
    },
    "28": {
      "L": "And he wastes away like a rotten thing, like a garment that is moth-eaten.",
      "M": "And I waste away like something rotten, like a garment eaten through by moths.",
      "T": "And this is what I am reduced to — a body rotting from the inside, a garment the moths have eaten until there is more hole than cloth. This is the man you are prosecuting so carefully."
    }
  },
  "14": {
    "1": {
      "L": "Man born of woman is few of days and full of trouble.",
      "M": "Man born of woman is short-lived and full of turmoil.",
      "T": "Every human being born of a woman lives briefly and lives hard. That is the baseline condition — short days, full of trouble. Start there."
    },
    "2": {
      "L": "He comes forth like a flower and withers; he flees like a shadow and does not last.",
      "M": "He comes up like a flower and then wilts; he passes like a shadow and does not endure.",
      "T": "He blooms for a moment — brilliant, briefly — and then he is cut. He moves across the ground like a shadow: real, but never solid, never staying."
    },
    "3": {
      "L": "And upon such a one do you fix your eyes, and bring him into judgment before you?",
      "M": "Yet on such a creature do you fix your eyes, and bring him into court before you?",
      "T": "And this — this brief, fragile, troubled thing — is the one you are scrutinizing? You open your eyes on him, this creature who barely lasts, and drag him into court?"
    },
    "4": {
      "L": "Who can bring a clean thing out of an unclean? Not one.",
      "M": "Who can bring something pure from something impure? No one can.",
      "T": "The problem runs deeper than conduct. Who produces something clean from something unclean? No one. The impurity goes all the way down. This is the condition he was born into."
    },
    "5": {
      "L": "Since his days are determined, the number of his months is with you; you have set his bounds that he cannot pass —",
      "M": "Since his days are fixed, the number of his months determined by you, the limit set that he cannot cross —",
      "T": "His days are already counted in your ledger. The months are numbered. You have drawn the line he cannot step past. All of it was set before he drew his first breath —"
    },
    "6": {
      "L": "— look away from him so he may rest, till he has served out his day like a hired hand.",
      "M": "— look away from him so he can rest, until he has completed his time like a hired worker.",
      "T": "— so give him this: look away. Let him breathe. Let him serve out his brief shift on earth without your gaze bearing down on him every moment, like a hired hand working toward the end of his day."
    },
    "7": {
      "L": "For there is hope for a tree — if it is cut down it will sprout again, and its shoots will not fail.",
      "M": "For there is hope for a tree: if it is cut down, it will sprout again, and its new growth will not stop.",
      "T": "A tree has better prospects than a man. Cut it down and it still comes back — new shoots rising from the old root, persistent, unkillable. The tree's hope outlasts the axe."
    },
    "8": {
      "L": "Though its root grows old in the earth and its stump dies in the ground —",
      "M": "Though its root grows old in the earth and its stump dies in the soil —",
      "T": "Even if the root has aged and the stump has decayed and every surface sign of life has disappeared into the ground —"
    },
    "9": {
      "L": "— yet at the scent of water it will bud and bring forth branches like a young plant.",
      "M": "— yet at the smell of water it will bud and put out branches like a new plant.",
      "T": "— one hint of water and it remembers itself. It buds. It puts out branches as if it were young again, as if the axe had never fallen."
    },
    "10": {
      "L": "But man dies and is laid low; man breathes his last, and where is he?",
      "M": "But man dies and lies helpless; he breathes his last — and where is he?",
      "T": "But a man dies. He collapses, spent. He takes his last breath — and then? Where does he go? The tree comes back. The man does not. The question hangs in the air unanswered."
    },
    "11": {
      "L": "As waters fail from the sea, and the river decays and dries up —",
      "M": "As water vanishes from a lake, and a river wastes away and dries up —",
      "T": "The way a lake evaporates in a drought, the way a river shrinks and cracks into mud and dust —"
    },
    "12": {
      "L": "— so man lies down and rises not; till the heavens are no more they will not awake, nor be roused from their sleep.",
      "M": "— so man lies down and does not rise; until the heavens are no more, they will not wake or be roused from their sleep.",
      "T": "— that is how a man lies down in death. He does not get up. Not until the heavens themselves dissolve will the dead be stirred from their sleep. And who has ever seen the heavens dissolve?"
    },
    "13": {
      "L": "O that you would hide me in Sheol, that you would conceal me until your wrath is past, that you would set me a fixed time and remember me!",
      "M": "O that you would hide me in Sheol, shelter me until your anger passes, set a fixed time for me, and then remember me!",
      "T": "Here is what I actually want — I want to be hidden. Tucked into the realm of the dead, out of reach of your wrath, until your anger burns itself out. And then — then I want you to set a date on your calendar and come back for me. Remember that I was here."
    },
    "14": {
      "L": "If a man dies, shall he live again? All the days of my appointed service I will wait, until my relief comes.",
      "M": "If a man dies, will he live again? Through all my days of hard service I will wait until my release comes.",
      "T": "If a man dies — can he possibly live again? That is the question. I do not know the answer. But I will do this: I will wait through every day of this hard conscription, right to the end, holding for that moment when something changes. When relief comes."
    },
    "15": {
      "L": "You will call, and I will answer you; you will long for the work of your hands.",
      "M": "You will call out to me, and I will answer; you will long for the work of your hands.",
      "T": "I imagine a day when you call my name and I answer you. When you — the one who made me — actually miss me. When the work of your hands is something you long to hold again rather than something you are pursuing to destroy."
    },
    "16": {
      "L": "For now you number my steps; you do not fail to watch over my sin.",
      "M": "But now you count my every step and watch over my sin without fail.",
      "T": "Instead of that longing, right now I get surveillance. Every step counted. Every fault logged. The tenderness I imagined is not what I have — what I have is a ledger."
    },
    "17": {
      "L": "My transgression is sealed up in a pouch, and you have plastered over my iniquity.",
      "M": "My transgression is sealed in a bag, and you have stitched up my guilt.",
      "T": "My sins are documented, packaged, sealed — every one preserved in evidence. Sewn shut so nothing escapes, so nothing is forgotten, so everything can be produced at the right moment."
    },
    "18": {
      "L": "But the falling mountain crumbles away, and the rock is moved from its place;",
      "M": "But a mountain eroding comes to nothing, and the rock is dislodged from its place;",
      "T": "And even the mountain — that immovable thing — wears down and collapses. The boulder is pried from where it has always stood —"
    },
    "19": {
      "L": "the waters wear away the stones; its torrents wash away the soil of the earth; and you destroy the hope of man.",
      "M": "water wears down the stones; floods wash away the soil of the earth — and so you wash away the hope of man.",
      "T": "— the relentless water grinds the stone to sand; the flood strips the topsoil and carries it off. And that is what you do to human hope. You erode it the same way. Patient. Persistent. Total."
    },
    "20": {
      "L": "You overpower him forever, and he passes; you change his face and send him away.",
      "M": "You overpower him completely and he is gone; you alter his countenance and send him away.",
      "T": "You overwhelm him and he passes from the scene — permanently. You change his face until it is no longer recognizable, and you dismiss him from the world."
    },
    "21": {
      "L": "His sons come to honor, and he does not know it; they are brought low, and he does not perceive them.",
      "M": "His sons rise to honor, but he does not know it; they are brought low, but he is not aware.",
      "T": "His children go on without him — they rise, they fall, they succeed and fail — and he knows none of it. Not a word reaches him. He is gone from the story while the story continues."
    },
    "22": {
      "L": "He feels only the pain of his own body, and mourns only for himself.",
      "M": "He feels only the pain within him and mourns only over himself.",
      "T": "The last things that remain for the dying man are entirely personal — the ache of his own body, the grief of his own soul. That is all that is left to him. Pain. Mourning. Himself."
    }
  },
  "15": {
    "1": {
      "L": "Then Eliphaz the Temanite answered and said:",
      "M": "Then Eliphaz the Temanite answered:",
      "T": "Eliphaz the Temanite spoke again:"
    },
    "2": {
      "L": "Should a wise man utter vain knowledge, and fill his belly with the east wind?",
      "M": "Should a wise man answer with empty words, filling himself with the hot east wind?",
      "T": "Is this what wisdom sounds like? Hot, empty, directional as the east wind — blowing hard and carrying nothing?"
    },
    "3": {
      "L": "Should he reason with unprofitable talk, and with speeches by which he can do no good?",
      "M": "Should he argue with worthless words, with speeches that accomplish nothing?",
      "T": "You have been building arguments that produce nothing — no light, no correction, no movement toward truth. Why are you still speaking?"
    },
    "4": {
      "L": "You even undermine the fear of God and restrain prayer before him.",
      "M": "You are actually undermining the fear of God and hindering prayer before him.",
      "T": "Do you realize what you are doing? Every word you say chips away at the foundations — the awe of God, the posture of prayer. You are making it harder for anyone near you to stand rightly before him."
    },
    "5": {
      "L": "For your mouth speaks from your iniquity, and you choose the tongue of the crafty.",
      "M": "Your mouth reveals your own guilt; you have adopted the tongue of the cunning.",
      "T": "The guilt is already audible. What comes out of your mouth is shaped by what is wrong in you — and the cleverness of your arguments only confirms it. You are not speaking from righteousness; you are speaking from craft."
    },
    "6": {
      "L": "Your own mouth condemns you, and not I; your own lips testify against you.",
      "M": "Your own mouth condemns you, not I; your very lips bear witness against you.",
      "T": "I am not even necessary as a prosecutor. You have done it yourself. Every sentence you have spoken is evidence. I only need to present the transcript."
    },
    "7": {
      "L": "Were you the first man ever born? Were you brought forth before the hills?",
      "M": "Are you the first man who was ever born? Were you shaped before the hills?",
      "T": "Are you the primordial Man — the first Adam — present before creation itself, formed before the mountains were set in place? Because that is what you would need to be to talk this way."
    },
    "8": {
      "L": "Have you listened in on the secret counsel of God? And do you restrain wisdom to yourself?",
      "M": "Have you been present in God's secret council? Do you think wisdom belongs to you alone?",
      "T": "Were you admitted to the divine assembly — the inner circle where God deliberates? Is that where you are drawing your conclusions from? Or have you appointed yourself custodian of wisdom no one else gets to access?"
    },
    "9": {
      "L": "What do you know that we do not know? What do you understand that we do not?",
      "M": "What do you know that we do not? What insight have you that we lack?",
      "T": "Point it out to me. Show me the thing you see that none of the rest of us see. We are listening."
    },
    "10": {
      "L": "Among us are both the gray-haired and the very aged, older by far than your father.",
      "M": "Among us are both the gray-haired and the very aged, men far older than your father.",
      "T": "Tradition stands with us. Men older than your father — men who have seen far more — are on our side of this argument. What you are offering is not insight; it is the impatience of youth dressed as wisdom."
    },
    "11": {
      "L": "Are the consolations of God too small for you, and the gentle word that comes to you?",
      "M": "Are God's consolations not enough for you — the gentle word he has offered you?",
      "T": "God has not left you without comfort. There have been gentle words, reasonable perspectives, offered carefully. Are those not enough? Do you need something more dramatic to satisfy you?"
    },
    "12": {
      "L": "Why does your heart carry you away, and why do your eyes flash —",
      "M": "Why does your heart carry you away? Why do your eyes flare —",
      "T": "What is happening inside you? Your heart runs away and your eyes blaze — where is this passion coming from, and where is it taking you?"
    },
    "13": {
      "L": "— that you turn your spirit against God and let such words go out of your mouth?",
      "M": "— that you turn your spirit against God and pour out such words from your mouth?",
      "T": "— straight into opposition against God himself. Your own spirit has wheeled around and is facing him down. And you let the words just come — every one of them aimed at him."
    },
    "14": {
      "L": "What is man, that he can be clean? And he who is born of woman, that he can be righteous?",
      "M": "What is a mortal man, that he could be clean? Can one born of woman be righteous?",
      "T": "No mortal born of a woman can stand clean before God — Job has said this himself. What makes him think his case is any different? The limitation is built into what we are."
    },
    "15": {
      "L": "Behold, God puts no trust in his holy ones, and the heavens are not clean in his sight.",
      "M": "God does not even trust his holy ones; the heavens themselves are not clean in his sight.",
      "T": "Even the heavenly beings — those nearest to him — do not earn his unqualified trust. Even the sky above is less than perfectly clean before his eyes. And yet Job expects to be found righteous?"
    },
    "16": {
      "L": "How much more abominable and corrupt is man, who drinks iniquity like water!",
      "M": "How much more abominable and vile is man, who laps up wickedness like water!",
      "T": "That is the condition of the holy beings. Now consider man — who doesn't merely live with wickedness nearby but drinks it down like water, taking it into himself without thinking, every day, all the time."
    },
    "17": {
      "L": "I will show you; hear me, and what I have seen I will declare —",
      "M": "I will show you — listen to me; I will declare what I have seen —",
      "T": "Let me lay out what I have witnessed. Just listen. This is not my theory — this is what observation of the world confirms:"
    },
    "18": {
      "L": "— what wise men have told, and their fathers have not concealed,",
      "M": "— what wise men have declared, passed down from their fathers without concealment,",
      "T": "— what has been handed down through generation after generation of wise men who refused to hide it:"
    },
    "19": {
      "L": "to whom alone the land was given, when no foreigner passed among them —",
      "M": "to those whose land was their own alone, before foreigners came among them —",
      "T": "— a tradition from the ancient days, when the land still belonged purely to those who had always known it, before the world got complicated:"
    },
    "20": {
      "L": "The wicked man writhes in pain all his days, and few years are stored up for the ruthless.",
      "M": "The wicked man twists in anguish all his days; the years allotted to the tyrant are numbered.",
      "T": "The wicked man's life is pain — not as occasional punishment but as the permanent texture of his existence. Every day is labor. And his years are not many, however much he grasps for them."
    },
    "21": {
      "L": "A dreadful sound is in his ears; in his time of peace a destroyer comes upon him.",
      "M": "A sound of terror is always in his ears; in his moments of peace the destroyer strikes him.",
      "T": "He cannot turn off the alarm. Even in his best moments — the quiet ones, the prosperous ones — he hears it: something is coming. And it is. The destroyer arrives exactly when he thought he was safe."
    },
    "22": {
      "L": "He does not believe he will return from darkness, and he is appointed for the sword.",
      "M": "He has no hope of escaping from the darkness; he is marked for the sword.",
      "T": "Deep down he knows there is no way out of the darkness he lives in. He is a man with a sword already drawn for him, already waiting. He senses it constantly."
    },
    "23": {
      "L": "He wanders abroad for bread, saying, 'Where is it?' He knows that the day of darkness is close at hand.",
      "M": "He wanders in search of food, crying, 'Where is it?' He knows the day of darkness is ready and near.",
      "T": "He roams looking for bread — and not out of abundance, out of desperation. Hungry and driven. All the while knowing, at the back of his mind, that the dark day is already prepared and waiting just around the corner."
    },
    "24": {
      "L": "Distress and anguish terrify him; they overwhelm him like a king marshaled for battle.",
      "M": "Distress and anguish terrorize him; they overpower him like a king advancing to battle.",
      "T": "Distress and anguish come for him like a war king with a full army — organized, irresistible, advancing without hesitation. The wicked man's inner life is a siege he cannot withstand."
    },
    "25": {
      "L": "Because he has stretched out his hand against God and defied the Almighty,",
      "M": "For he has stretched out his hand against God and defied the Almighty,",
      "T": "This is the root of all of it: he squared off against God. He stretched his arm out against the Almighty as if it were a fair contest —"
    },
    "26": {
      "L": "running against him neck-first, upon the thick bosses of his shields,",
      "M": "charging at him neck-forward, pressing against the thick boss of his shield,",
      "T": "— running straight at him, head down, neck exposed, shield raised like he could take the impact. Like he stood a chance."
    },
    "27": {
      "L": "because he has covered his face with his fat and made his flanks thick with flesh —",
      "M": "He has become fat-faced, his sides padded with flesh —",
      "T": "He fattened himself on his own prosperity until his own body became an insulation against reality — rolls of wealth wrapped around him, making him feel invulnerable. Invulnerability is an illusion."
    },
    "28": {
      "L": "he inhabits ruined cities, houses that no one lives in, which are ready to become heaps —",
      "M": "he makes his home in ruined cities, in houses no one else inhabits, houses on the verge of collapse —",
      "T": "The end result: he takes up residence in the abandoned and broken places. Cities with no one left in them. Houses waiting to become rubble. That is what his empire amounts to."
    },
    "29": {
      "L": "he will not be rich, nor will his wealth endure, nor will his possessions spread over the earth.",
      "M": "He will not remain wealthy; his substance will not last; he will not extend his holdings over the earth.",
      "T": "The money will not hold. The property will not grow. The reach he imagined — empire, inheritance, legacy — none of it will materialize. What he built will not stand."
    },
    "30": {
      "L": "He will not escape from darkness; flame will dry up his shoots, and by the breath of God's mouth he will be swept away.",
      "M": "He will not escape from the darkness; flame will wither his branches, and by the breath of God's mouth he will be swept away.",
      "T": "There is no exit from the darkness that is closing in on him. Fire takes his branches. And then — the single most devastating thing — the breath of God's own mouth, and he is simply gone. Not struck down in a great battle. Blown away."
    },
    "31": {
      "L": "Let him not trust in emptiness, deceiving himself, for emptiness will be his repayment.",
      "M": "Let him not deceive himself by trusting in what is empty, for emptiness will be his only return.",
      "T": "The delusion must be named: he is investing everything in nothing. And nothing has an exact rate of return — you get back exactly what you put in."
    },
    "32": {
      "L": "It will be paid off before his day comes, and his branch will not be green.",
      "M": "It will be completed before his time; his branch will not stay green.",
      "T": "The account comes due before he is ready. His branch withers before the season ends. There is no late harvest waiting for him."
    },
    "33": {
      "L": "He will shake off his unripe grape like the vine, and cast off his blossom like the olive tree.",
      "M": "He will shed his unripe grapes like the vine, and drop his blossoms like the olive tree.",
      "T": "Before anything can ripen, it falls. The grapes shaken loose while still sour. The blossoms gone before they become fruit. Every promise, every potential — let go before it can be completed."
    },
    "34": {
      "L": "For the company of the godless will be barren, and fire will consume the tents of bribery.",
      "M": "For the assembly of the godless will be desolate, and fire will consume the tents of corruption.",
      "T": "Whatever community the godless build among themselves — it will be hollow. And the wealth accumulated through bribes and corruption? Fire does not negotiate. The tents burn."
    },
    "35": {
      "L": "They conceive mischief and bring forth evil, and their inmost parts prepare deceit.",
      "M": "They conceive trouble and give birth to evil; their inmost being produces only deceit.",
      "T": "This is what they generate — the whole reproductive cycle of wickedness. Trouble conceived in the dark, evil born into the light, deception incubating in the belly. What comes out of them cannot be anything else, because it is what they are made of."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 13–15 written.')

if __name__ == '__main__':
    main()
