"""
MKT Job chapters 19–21 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-19-21.py

=== Contested-term decisions ===

H1350  (גֹּאֵל, go'el): "Redeemer" (L/M/T) — capital R across all tiers.
       The go'el is the kinsman who acts on behalf of one who cannot help himself
       (see Ruth, Lev 25). Job's use is cosmic: he names a heavenly vindicator who
       will stand on his behalf. "Vindicator" is defensible but "Redeemer" carries
       the full legal-redemptive weight and is retained here as the established
       rendering. In 19:25 this is Job's great confession of faith against all evidence.

H7706  (שַׁדַּי, Shaddai): "Shaddai" (L) / "the Almighty" (M/T) — carried from chs 13–15.
       Appears in 21:15, 21:20.

H5315  (נֶפֶשׁ, nefesh): "soul" in 21:25 — rendered as embodied self in anguish,
       not Greek immaterial soul. "In the bitterness of his soul" = visceral, bodily grief.

H7307  (רוּחַ, ruach): context-driven throughout —
       19:17 — "breath" (Job's literal breath is repulsive to his wife)
       21:4  — "spirit" (Job's impatient inner disposition)
       21:18 — "wind" (the wind that carries chaff)

H120   (אָדָם, adam): "man" in all tiers for generic humanity (20:4, 20:29, 21:33).

H2611  (חָנֵף, chaneph): "hypocrite" (L — KJV tradition retained) / "godless" (M/T).
       Appears in 20:5. Root = profane, irreligious; M/T use "godless" for semantic
       precision.

H7585  (שְׁאוֹל, Sheol): "Sheol" (L/M); "the realm of the dead" (T). In 21:13.

H433   (אֱלוֹהַּ, Eloah): "God" in all tiers (19:26, 20:15, 20:23, 21:9, 21:14, 21:19, 21:22).

H430   (אֱלֹהִים, Elohim): "God" in all tiers (20:29).

=== 19:25–27 — The great confession ===

These three verses are the theological apex of the book and among the most disputed
in the OT. Three decisions:

1. H1350 (go'el) = "Redeemer" (see above). Capitalized to mark Job's confessional
   weight; it is not a generic description but a legal-theological claim.

2. H6083 (עָפָר, afar): "dust / earth" in 19:25 — "he shall stand upon the earth/dust."
   L renders "dust" (the most literal gloss); M/T use "earth" for natural English.

3. 19:26a (מֵעוֹר נִקְּפוּ זֹאת): the MT is notoriously compressed and uncertain.
   "After my skin is thus destroyed" is the most defensible reading. The key
   theological claim in 19:26b ("yet from my flesh I shall see God") uses
   מִבְּשָׂרִי — either "from within my flesh" (bodily resurrection reading) or
   "apart from my flesh" (disembodied vision). The context of v27 ("my own eyes
   shall behold") strongly favors the bodily-vision reading: Job expects personal,
   embodied sight of God. L and M render "from within my flesh"; T makes the
   bodily expectation explicit without over-translating.

4. 19:27c — H2436 (חֵיק, cheq) = "bosom/inmost being." Often translated "heart"
   or "reins" (KJV: "my reins be consumed within me"). The consuming intensity of
   longing hollows him out. Rendered "heart fails within me" in L/M; T makes the
   emotional meaning explicit.

=== Textual note on 19:28 ===

The Kethib reads בִּי ("in me"); some MSS read בוֹ ("in him" — the wicked one).
The Kethib is preferred: Job quotes what his accusers say — the root of the trouble
is "in him (me)" — setting up the warning in v29. The syntax "if ye say... seeing
the root..." is a conditional: Job anticipates their retort and preemptively counters.

=== Chapter 21 structure ===

Job's counterargument to Zophar (ch 20). The argument is empirical and devastating:
the wicked demonstrably prosper (vv 7–16), they die comfortably (vv 13, 23–24),
and the retribution theology is built on selective observation. vv 17–18 are
Job's rhetorical questions challenging the frequency of divine punishment; he is
not asserting that God never punishes but that the friends have elevated occasional
examples into invariable laws. vv 22–26 produce the bitter climax: the righteous
and the wicked die alike, and the grave makes no distinctions. v 34 is Job's
devastating summary: all the comfort offered has been built on falsehood.

=== Aspect notes ===

Ch 19 mixes perfects (completed actions — what God has already done to Job) with
imperfects/jussives (the wish of vv 23–25). The shift in v 25 to confident imperfect
"יָקוּם" (he shall stand) is a declaration, not a wish — Job moves from lament to
conviction. T captures this shift.

Ch 20 uses predominantly imperfects for the fate-of-the-wicked sequence, conveying
the relentless ongoing pattern. T renders them as vivid present tense.

Ch 21 uses rhetorical questions (vv 4, 7, 17, 22, 28) and imperatives (vv 2–5).
The imperative forms in v 2 are second-person plural commands — Job is addressing
the whole group of friends.
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
  "19": {
    "1": {
      "L": "Then Job answered and said:",
      "M": "Then Job answered:",
      "T": "Job spoke:"
    },
    "2": {
      "L": "How long will ye vex my soul and crush me in pieces with words?",
      "M": "How long will you torment me and crush my soul with words?",
      "T": "How much longer will you do this? Wearing down my soul, grinding it to pieces with speech after speech?"
    },
    "3": {
      "L": "These ten times ye have reproached me; ye are not ashamed that ye deal hardly with me.",
      "M": "Ten times now you have reproached me; you are not ashamed to wrong me.",
      "T": "Ten times over you have heaped shame on me, and not once have you had the decency to feel embarrassed about it. You keep going."
    },
    "4": {
      "L": "And be it indeed that I have erred, mine error lodgeth within myself.",
      "M": "Even if I have truly erred, my error rests with me alone.",
      "T": "And suppose I have gone wrong — suppose that is even true — it is my error to bear, not yours. My failure stays inside my own walls. It is not your business."
    },
    "5": {
      "L": "If indeed ye magnify yourselves against me and plead my disgrace against me,",
      "M": "If you truly exalt yourselves over me and press my disgrace against me as evidence,",
      "T": "If you insist on towering over me, using my suffering as the proof of your case against me —"
    },
    "6": {
      "L": "know then that God hath overthrown me and compassed me about with his net.",
      "M": "then know that God has overthrown me and thrown his net around me.",
      "T": "— then you have it backwards. God is the one who put me here. He upended my life and pulled the net tight around me. I did not manufacture this suffering."
    },
    "7": {
      "L": "Behold, I cry out of wrong but I am not heard; I cry aloud but there is no judgment.",
      "M": "I shout 'Injustice!' but no one answers; I call for justice but there is no verdict.",
      "T": "I shout it into the void: this is wrong. Nothing comes back. I cry as loudly as my lungs allow for a hearing, for justice — and the silence returns empty. No answer. No verdict."
    },
    "8": {
      "L": "He hath fenced up my way that I cannot pass, and he hath set darkness upon my paths.",
      "M": "He has blocked my way so I cannot pass; he has set darkness over my paths.",
      "T": "Every way out has been walled shut. He has turned the paths I could travel into dead ends, into darkness. I cannot move in any direction without hitting what he has placed there."
    },
    "9": {
      "L": "He hath stripped me of my glory and taken the crown from my head.",
      "M": "He has stripped me of my honor and taken the crown from my head.",
      "T": "The dignity I had — the standing, the weight I carried among my people — stripped away. The crown that once sat on my head has been lifted and taken. He did that."
    },
    "10": {
      "L": "He hath broken me down on every side, and I am gone; mine hope hath he pulled up like a tree.",
      "M": "He has broken me down on every side and I am gone; he has pulled up my hope like a tree.",
      "T": "Broken from every direction — not one side, all of them. I am gone. The hope I had, the deep-rooted expectation that things could still turn — he pulled it up the way you pull a tree out of the ground."
    },
    "11": {
      "L": "He hath also kindled his anger against me, and he counteth me unto him as one of his enemies.",
      "M": "He has kindled his wrath against me and counted me as one of his enemies.",
      "T": "The wrath he lit against me is the wrath he lights against his enemies. That is what I am to him now — enemy. Not servant, not worshiper, not beloved. Enemy. He has reclassified me."
    },
    "12": {
      "L": "His troops come together and raise their way against me; they encamp round about my tabernacle.",
      "M": "His troops advance together; they heap up siege ramps against me and encamp around my tent.",
      "T": "He has sent an army. They come in formation — troops in coordinated advance — heaping up siege works and pitching camp in a circle around everything I have left. My tent is their target."
    },
    "13": {
      "L": "He hath put my brethren far from me, and mine acquaintance are verily estranged from me.",
      "M": "He has put my brothers far from me, and those who knew me have become wholly estranged.",
      "T": "The people closest to me — brothers, the ones who had known me for years — God moved them away. They are strange to me now, estranged the way foreigners are strange, as if we never shared a history."
    },
    "14": {
      "L": "My kinsfolk have failed and my familiar friends have forgotten me.",
      "M": "My relatives have failed me, and my familiar friends have forgotten me.",
      "T": "The extended family — failed. Gone when I needed them. The intimate friends — they have forgotten me as though I never existed in their world. Erased from the people who should have been my anchors."
    },
    "15": {
      "L": "They that dwell in mine house and my maids count me for a stranger; I am an alien in their sight.",
      "M": "Those living in my house and my female servants count me as a stranger; I am a foreigner in their eyes.",
      "T": "Inside my own household — the people I employed, the servants who have lived under my roof — they look at me and see a stranger. A foreigner. In my own house I do not belong."
    },
    "16": {
      "L": "I called unto my servant, and he gave me no answer; I entreated him with my mouth.",
      "M": "I called my servant, but he gave me no answer; I had to beg him with my own mouth.",
      "T": "I called out to my servant — my own servant — and he did not answer. I had to plead with him, from my own mouth, to move. The authority I carried is simply gone."
    },
    "17": {
      "L": "My breath is offensive to my wife, and I am loathsome to the children of my own body.",
      "M": "My breath is repulsive to my wife; I am loathsome to the sons of my own body.",
      "T": "My wife cannot bear the smell of my breath. My own children — born of my own body — find me repellent. The intimacy that was my home is now a place where I generate disgust."
    },
    "18": {
      "L": "Even young children despise me; I arise and they speak against me.",
      "M": "Even young children despise me; when I stand up they speak against me.",
      "T": "Children — small children — look at me with contempt. When I get to my feet they mock me. The most vulnerable people in my world, the ones who should look up to me, look down."
    },
    "19": {
      "L": "All my intimate friends abhor me, and they whom I loved are turned against me.",
      "M": "All my closest companions abhor me; those I loved have turned against me.",
      "T": "The people in my inner circle — the ones I trusted with everything, the ones I loved — every one of them has turned. The inner circle has become the circle of my accusers."
    },
    "20": {
      "L": "My bone cleaveth to my skin and to my flesh, and I am escaped with the skin of my teeth.",
      "M": "My bones cling to my skin and flesh; I have escaped with only the skin of my teeth.",
      "T": "I am nothing but bone and skin — the flesh has wasted until there is nothing to separate skeleton from surface. I am alive, but just barely — by the narrowest margin, the thinnest skin of my teeth."
    },
    "21": {
      "L": "Have pity upon me, have pity upon me, O ye my friends, for the hand of God hath touched me.",
      "M": "Have pity on me, have pity on me, O my friends, for the hand of God has struck me.",
      "T": "Pity. I am asking for pity — not justice, not an argument, just pity. You are the people who are supposed to be my friends. Look at me. The hand of God has come down on me. That is all I am asking you to see."
    },
    "22": {
      "L": "Why do ye persecute me as God, and are not satisfied with my flesh?",
      "M": "Why do you pursue me like God, and are not satisfied with my flesh?",
      "T": "Is one prosecutor not enough? You join in, matching God's relentless intensity. My suffering is not sufficient. My flesh has not been eaten away enough to satisfy you yet?"
    },
    "23": {
      "L": "Oh that my words were now written! Oh that they were inscribed in a book!",
      "M": "O that my words were written down! O that they were inscribed in a book!",
      "T": "I want a record. I want this documented — not whispered between people who will forget it, but written down, committed to a scroll, preserved."
    },
    "24": {
      "L": "That they were graven with an iron pen and lead in the rock for ever!",
      "M": "That with an iron pen and lead they were cut into the rock forever!",
      "T": "Better still — chisel them into stone. Iron pen in the rock, channels filled with lead so the letters hold their shape for centuries. I want this to outlast me, outlast my detractors, outlast the argument itself."
    },
    "25": {
      "L": "For I know that my Redeemer liveth, and that he shall stand at the last upon the dust.",
      "M": "For I know that my Redeemer lives, and that at the last he will stand upon the earth.",
      "T": "I know this. Whatever else I do not know — this I know: my Redeemer is alive. The one who will vindicate me, who stands as my go'el before the court of heaven — he lives. And in the end, at the very last, he will take his stand on this very earth."
    },
    "26": {
      "L": "And after my skin hath been thus destroyed, yet from within my flesh I shall see God,",
      "M": "And after my skin is thus destroyed, yet from within my flesh I shall see God,",
      "T": "Even when this skin is stripped away and destroyed — and it may well be — I will still see God. Not from outside the body, not as a ghost — from within flesh, from within a body that was mine. A vision earned through this very suffering."
    },
    "27": {
      "L": "whom I myself shall see, and mine own eyes shall behold, and not a stranger; my heart faileth within me.",
      "M": "whom I myself shall see, and my own eyes shall behold — not a stranger's eyes. My heart fails within me with longing.",
      "T": "That sight — God seen with my own eyes, not someone else's account, not secondhand — mine. The longing is so overwhelming it hollows me out; my heart collapses inward at the thought of it."
    },
    "28": {
      "L": "If ye should say, 'Why do we persecute him?' seeing the root of the matter is found in him —",
      "M": "If you say, 'Why are we still pursuing him?' when the root of the trouble lies within him —",
      "T": "And if you try to justify it by saying 'We are only following the logic — the root of his trouble lies within him' —"
    },
    "29": {
      "L": "— be ye afraid of the sword; for wrath bringeth the punishment of the sword, that ye may know there is a judgment.",
      "M": "— then fear the sword, for wrath brings the sword's punishment, so that you may know there is indeed a judgment.",
      "T": "— then fear what is coming. The sword has a punishment, and that punishment is born of wrath — not Job's, but God's. Know this: there is a judgment, and it does not always fall where you think it does."
    }
  },
  "20": {
    "1": {
      "L": "Then Zophar the Naamathite answered and said:",
      "M": "Then Zophar the Naamathite answered:",
      "T": "Zophar of Naamah replied:"
    },
    "2": {
      "L": "Therefore do my thoughts cause me to answer, and because of this I make haste.",
      "M": "Therefore my thoughts push me to answer; I feel urgency within me.",
      "T": "Something in me forces a response. I cannot hold it — my thoughts are pressing out and the haste to speak is real."
    },
    "3": {
      "L": "I have heard the check of my reproach, and a spirit beyond my understanding causeth me to answer.",
      "M": "I hear reproof that dishonors me, and a spirit from beyond my understanding compels me to respond.",
      "T": "What Job said was an insult to everything I stand for. And something in me — deeper than my own thinking — is driving me to speak. Call it conviction; it will not let me stay silent."
    },
    "4": {
      "L": "Knowest thou not this of old, since man was placed upon the earth,",
      "M": "Do you not know this from of old, since man was set upon the earth,",
      "T": "This is ancient wisdom — older than this argument, older than any of us. Has it not been established since the beginning of human time, since the first man was placed on this earth?"
    },
    "5": {
      "L": "that the triumphing of the wicked is short, and the joy of the hypocrite but for a moment?",
      "M": "that the triumph of the wicked is short, and the joy of the godless lasts but a moment?",
      "T": "The wicked appear to thrive — but it never lasts. The success they build is brief; the joy they feel is measured in moments. This is what history testifies across every generation."
    },
    "6": {
      "L": "Though his excellency mount up to the heavens and his head reach unto the clouds —",
      "M": "Though his greatness mounts to the heavens and his head reaches the clouds —",
      "T": "Let him ascend as high as he wants — let his achievements stack to the sky and his pride touch the clouds —"
    },
    "7": {
      "L": "— he shall perish for ever like his own dung; they which have seen him shall say, 'Where is he?'",
      "M": "— he will perish forever like his own dung; those who saw him will say, 'Where is he?'",
      "T": "— he will disappear. And not a dignified exit: like dung. Gone, leaving only the stench of memory. The people who saw him at his height will look at where he stood and ask, 'Where did he go?'"
    },
    "8": {
      "L": "He shall fly away as a dream, and shall not be found; yea, he shall be chased away as a vision of the night.",
      "M": "He flies away like a dream and cannot be found; he is chased off like a vision of the night.",
      "T": "He evaporates the way a dream does — vivid in the moment, gone completely when you open your eyes. A night vision dispersed by morning, holding nothing."
    },
    "9": {
      "L": "The eye also which saw him shall see him no more; neither shall his place any more behold him.",
      "M": "The eye that saw him will see him no more; his own place will no longer recognize him.",
      "T": "The people who watched his success will never see it again. The seat he occupied — the place where his power was felt — will have no memory of him."
    },
    "10": {
      "L": "His children shall seek to please the poor, and his hands shall restore their goods.",
      "M": "His children will seek favor from the poor, and his hands will give back their wealth.",
      "T": "His children will end up begging the poor for mercy. The wealth he seized — his heirs' hands will have to pay it back. There is a restitution built into the universe."
    },
    "11": {
      "L": "His bones are full of the sin of his youth, which shall lie down with him in the dust.",
      "M": "His bones are full of the sins of his youth; they will lie down with him in the dust.",
      "T": "The sins committed in his prime — when the energy and opportunity were greatest — those sins are embedded in his bones. When he lies down in the dust, they go down with him. They have nowhere else to go."
    },
    "12": {
      "L": "Though wickedness be sweet in his mouth, though he hide it under his tongue —",
      "M": "Though evil is sweet in his mouth and he hides it under his tongue —",
      "T": "He has learned to love what is wrong. The taste of it is sweet — he rolls it in his mouth, hides it under his tongue, savors it before swallowing —"
    },
    "13": {
      "L": "— though he spare it, and forsake it not, but keep it still within his mouth —",
      "M": "— though he spares it and will not let it go, but keeps it lodged in his mouth —",
      "T": "— reluctant to release it, holding it carefully, unwilling to lose the pleasure before he must —"
    },
    "14": {
      "L": "— yet his meat is turned in his bowels; it is the gall of asps within him.",
      "M": "— yet his food turns in his stomach; it becomes cobra venom inside him.",
      "T": "— but what he swallowed turns. The sweetness curdles. What felt like food becomes poison — the venom of a cobra working through his system from within."
    },
    "15": {
      "L": "He hath swallowed down riches, and shall vomit them up again; God shall cast them out of his belly.",
      "M": "He swallowed wealth down, and will vomit it up again; God will expel it from his belly.",
      "T": "Everything he consumed — all the wealth he took in and thought he owned — it will come back up. He cannot keep what he has swallowed. God will force it out."
    },
    "16": {
      "L": "He shall suck the poison of asps; the viper's tongue shall slay him.",
      "M": "He will suck the venom of cobras; the tongue of the viper will kill him.",
      "T": "What he put in his mouth will kill him. He sucked on the nectar of wickedness — and the tongue of the viper delivers the payment. The sweetness was never what it seemed."
    },
    "17": {
      "L": "He shall not see the rivers, the floods, the brooks of honey and butter.",
      "M": "He will not look on the rivers, the streams, the brooks flowing with honey and butter.",
      "T": "The land of abundance — honey and cream, rivers running with richness — he will never see it. All the good things he anticipated and thought he had secured will be taken from sight."
    },
    "18": {
      "L": "That which he laboured for shall he restore, and shall not swallow it down; according to his substance shall the restitution be, and he shall not rejoice.",
      "M": "He must restore the fruits of his labor without consuming them; according to his wealth the restitution will be, and he will not rejoice in it.",
      "T": "Everything he worked for, everything accumulated through toil and scheme — it all has to go back. He cannot keep it. He cannot even swallow the satisfaction of having had it. The accounting strips it away."
    },
    "19": {
      "L": "Because he hath oppressed and forsaken the poor; because he hath violently seized a house which he builded not.",
      "M": "For he oppressed and abandoned the poor; he seized a house he did not build.",
      "T": "Here is the moral root of it: he crushed people beneath him and walked away. He grabbed what belonged to others — houses they built with their own hands — and called it his. The injustice is specific. It has names and addresses."
    },
    "20": {
      "L": "Surely he shall not feel quietness in his belly; he shall not save of that which he desired.",
      "M": "He will not feel peace within; he will retain nothing of what he desired.",
      "T": "He was never satisfied — the craving had no bottom. And because of that, nothing he desired will remain in his hands. The restlessness that drove him to accumulate ensures he keeps none of it."
    },
    "21": {
      "L": "There shall none of his meat be left; therefore shall no man look for his goods.",
      "M": "None of his food is left; therefore no one will inherit his property.",
      "T": "He ate everything he had. No remnant, no estate, no goods left for anyone. The feast is over and the table is bare."
    },
    "22": {
      "L": "In the fulness of his sufficiency he shall be in straits; every hand of the wicked shall come upon him.",
      "M": "In the very fullness of his plenty he will be in distress; every hand of the wretched will come against him.",
      "T": "At the exact moment when he seems to have reached the peak of abundance — that is when the walls close in. Every person he has wronged turns on him at once."
    },
    "23": {
      "L": "When he is about to fill his belly, God shall cast the fury of his wrath upon him and rain it upon him while he is eating.",
      "M": "When he is set to fill his belly, God will hurl his fierce wrath upon him and rain it down on him as he eats.",
      "T": "The moment of satisfaction — mouth open, about to consume — and that is when God's burning wrath falls. Not later. Now. While he is eating."
    },
    "24": {
      "L": "He shall flee from the iron weapon, and the bow of bronze shall strike him through.",
      "M": "He flees from the iron weapon, and the bronze bow strikes him through.",
      "T": "He runs from one weapon — only to meet another. He dodges iron and bronze finds him. There is no direction to flee. The armory of judgment has no gaps."
    },
    "25": {
      "L": "The arrow is drawn and cometh out of his body; the flashing point passeth through his gall; terrors are upon him.",
      "M": "The arrow is drawn; it passes through his body; the shining blade comes out through his gall; terrors overwhelm him.",
      "T": "The weapon goes in and comes out the other side. The shining blade passes through the gall. And in that moment, terrors multiply — not just the wound but the sudden total recognition of what is happening to him."
    },
    "26": {
      "L": "All darkness is stored up for his treasures; a fire not blown shall consume him; it shall go ill with him that is left in his tabernacle.",
      "M": "All darkness is kept in store for his treasures; a fire not fanned by wind shall consume him; disaster will fall on what remains in his tent.",
      "T": "Everything accumulated — the treasure rooms, the stored wealth — they are held in darkness, for darkness. A fire that needs no wind will find him. Even the survivors left in his household will not escape the disaster."
    },
    "27": {
      "L": "The heaven shall reveal his iniquity, and the earth shall rise up against him.",
      "M": "The heavens will expose his guilt, and the earth will rise up against him.",
      "T": "Everything is against him. The sky above bears witness — it opens and his guilt is visible to all. The earth beneath rises as if creation itself joins the prosecution."
    },
    "28": {
      "L": "The increase of his house shall depart, and his goods shall flow away in the day of his anger.",
      "M": "The produce of his house will depart; his possessions will pour away in the day of his anger.",
      "T": "His entire household output — everything the estate produced, everything stored behind those walls — carried away. On the day of wrath it flows out like water finding its level, and nothing dams it."
    },
    "29": {
      "L": "This is the portion of a wicked man from God, and the heritage appointed to him by God.",
      "M": "This is the portion of the wicked man from God — the heritage decreed for him by God.",
      "T": "There it is — the full inheritance of the wicked. This is what God has appointed. Not arbitrary, not accidental — decreed. The inheritance is exact, and it is terrible."
    }
  },
  "21": {
    "1": {
      "L": "But Job answered and said:",
      "M": "But Job answered:",
      "T": "Job responded:"
    },
    "2": {
      "L": "Hear diligently my speech, and let this be your consolations.",
      "M": "Listen carefully to what I say; let this be your consolation.",
      "T": "You want to comfort me? Then actually listen. That is all I am asking — let your listening be the comfort."
    },
    "3": {
      "L": "Suffer me that I may speak; and after that I have spoken, mock on.",
      "M": "Bear with me so I may speak; and after I have spoken, mock away.",
      "T": "Give me the floor for just a moment. When I am done, all the mocking you want — go ahead. But first: let me speak."
    },
    "4": {
      "L": "As for me, is my complaint to man? And if it were so, why should not my spirit be impatient?",
      "M": "As for me, is my complaint directed to man? Why then should I not be impatient?",
      "T": "My complaint is not a social grievance. I am not arguing with people — I am arguing with God. Given that, is it any wonder my spirit is running short on patience?"
    },
    "5": {
      "L": "Mark me, and be astonished, and lay your hand upon your mouth.",
      "M": "Look at me and be appalled; lay your hand over your mouth.",
      "T": "Look. Really look at me. Let what you see stop the words in your throat — lay your hand over your mouth and just look. The sight is worth more than any argument."
    },
    "6": {
      "L": "Even when I remember I am troubled, and trembling seizeth my flesh.",
      "M": "Even when I think of it I am troubled, and shuddering seizes my flesh.",
      "T": "The subject I am about to raise — when I let it fully land — I am shaken to the core. My flesh trembles with it. It disturbs everything."
    },
    "7": {
      "L": "Wherefore do the wicked live, grow old, yea, grow mighty in power?",
      "M": "Why do the wicked go on living, grow old, and even grow mighty in power?",
      "T": "Here is the question your theology cannot answer: Why do the wicked live long and well? Why do they grow old in strength rather than dying young and diminished?"
    },
    "8": {
      "L": "Their seed is established with them before their faces, and their offspring before their eyes.",
      "M": "Their children are established around them, and their offspring before their eyes.",
      "T": "Their families thrive — children and grandchildren, rooted and visible, right before the wicked man's eyes. Established. Secure. Everything Zophar said would be stripped from the wicked? The wicked man is watching it grow."
    },
    "9": {
      "L": "Their houses are safe from fear, neither is the rod of God upon them.",
      "M": "Their houses are safe from fear; the rod of God is not upon them.",
      "T": "The home life of the wicked is quiet. No dread at the door, no sense that judgment is near. The rod of God — which Eliphaz and Zophar assured us falls on the wicked — is simply not there."
    },
    "10": {
      "L": "Their bull gendereth and faileth not; their cow calveth and casteth not her calf.",
      "M": "Their bull breeds without fail; their cow calves and does not miscarry.",
      "T": "Even their livestock thrive. The bull services and never misses. The cow delivers healthy calves without losing them. The prosperity extends to every corner of their estate."
    },
    "11": {
      "L": "They send forth their little ones like a flock, and their children dance.",
      "M": "Their little ones run out like a flock, and their children dance.",
      "T": "Their children pour out to play like lambs released to pasture. They dance. Joy. Abundance. Life. Everything the theology of retribution says their parents should be denied."
    },
    "12": {
      "L": "They take the timbrel and harp, and rejoice at the sound of the pipe.",
      "M": "They take up timbrel and harp and rejoice at the sound of the flute.",
      "T": "Music in the house of the wicked. Timbrel and lyre and the sweet sound of the flute. They celebrate — and the theology that says this will be snatched from them momentarily fails to describe what is actually happening."
    },
    "13": {
      "L": "They spend their days in prosperity, and in a moment go down to Sheol.",
      "M": "They spend their days in prosperity and go down to Sheol in an instant.",
      "T": "Their lives are spent in comfort and ease — and then they die quickly, painlessly. They go down to the realm of the dead in a moment, without lingering suffering. This is not what your theology predicts."
    },
    "14": {
      "L": "Yet they say to God, 'Depart from us; we do not desire the knowledge of thy ways.'",
      "M": "Yet they say to God, 'Leave us alone; we have no desire to know your ways.'",
      "T": "And in the middle of all this prosperity — what do they say? They say to God: Go away. We do not want you. We have no interest in your paths. They enjoy abundance while dismissing the Giver."
    },
    "15": {
      "L": "Who is the Almighty that we should serve him? And what profit have we if we pray to him?",
      "M": "Who is the Almighty that we should serve him? What do we gain by praying to him?",
      "T": "Their theology is naked pragmatism: 'What's in it for us? If Shaddai doesn't deliver a measurable return on service, why bother?' They weigh God on the scales of profit and loss."
    },
    "16": {
      "L": "Lo, their prosperity is not in their own hand; the counsel of the wicked is far from me.",
      "M": "Their prosperity is not in their own hand — the counsel of the wicked I keep far from me.",
      "T": "I want to be clear — I am not endorsing them. Their prosperity is not something they built; it is simply what has been given. And I do not want their philosophy. I am making an observation about reality, not a recommendation."
    },
    "17": {
      "L": "How oft is the lamp of the wicked put out? And how oft cometh their calamity upon them? God distributeth sorrows in his anger.",
      "M": "How often is the lamp of the wicked actually extinguished? How often does disaster come upon them? Does God distribute pain in his anger?",
      "T": "You say it happens all the time — but does it? How often, really, does the wicked man's lamp go dark? How often does disaster arrive on schedule? I am asking honestly. You are asserting a pattern; I am questioning whether the pattern actually holds."
    },
    "18": {
      "L": "They are as straw before the wind, and as chaff that the storm carrieth away.",
      "M": "They are as straw before the wind, and chaff swept away by the tempest.",
      "T": "That is the picture your theology paints — the wicked, weightless as chaff, snatched up by every wind. But that is not what I observe. The wicked are often the ones still standing when the wind has passed."
    },
    "19": {
      "L": "God layeth up his iniquity for his children; he rewardeth him and he shall know it.",
      "M": "You say God stores up punishment for his children; God repays the man himself and he will know it.",
      "T": "You might argue: God delays, saves the reckoning for the children. But that raises a further question — if the punishment goes to the children, what does the man himself experience in his own lifetime?"
    },
    "20": {
      "L": "Let his own eyes see his destruction; let him drink of the wrath of the Almighty.",
      "M": "Let his own eyes see his destruction; let him drink of the wrath of the Almighty.",
      "T": "If the punishment goes to his children, that is no satisfaction. Let the man himself see with his own eyes what he has brought on himself. Let him personally drink the cup of Shaddai's wrath — otherwise what is the moral point?"
    },
    "21": {
      "L": "For what pleasure hath he in his house after him, when the number of his months is cut off?",
      "M": "For what pleasure does he take in his house after him, when the number of his months is severed?",
      "T": "Once the man is dead — once his months are cut off — what does he care what happens to his household? He is gone. The theological argument about delayed punishment collapses at this point."
    },
    "22": {
      "L": "Shall any teach God knowledge? seeing he judgeth those that are high.",
      "M": "Will anyone teach God knowledge? He is the one who judges those on high.",
      "T": "Job pauses and acknowledges the limit: no one can instruct God. He who judges even the highest beings needs no curriculum from us. The question of why the wicked prosper is his to answer, not ours to resolve."
    },
    "23": {
      "L": "One dieth in his full strength, being wholly at ease and at rest,",
      "M": "One person dies in full vigor, completely at ease and secure,",
      "T": "One man dies at the height of his powers — peaceful, undisturbed, everything intact. No suffering announced his end. He simply stepped out of life at its best."
    },
    "24": {
      "L": "his sides full of milk and his bones moistened with marrow.",
      "M": "his sides full of milk and his bones saturated with marrow.",
      "T": "His body is a picture of abundance — vigorous, well-nourished, marrow filling every bone. This is not the wasted death of someone under divine judgment. This is a man leaving life at its peak."
    },
    "25": {
      "L": "And another dieth in the bitterness of his soul, and never eateth with pleasure.",
      "M": "And another dies in bitterness of soul, having never tasted what is good.",
      "T": "Meanwhile another man — perhaps a righteous one — dies in anguish. Bitter to the end. Never having tasted what the prosperous wicked man consumed in abundance. Where is the retribution theology in that?"
    },
    "26": {
      "L": "They shall lie down alike in the dust, and the worms shall cover them.",
      "M": "They lie down together in the dust, and worms cover them both.",
      "T": "In the end — the grave. The prosperous wicked and the suffering righteous end up in the same place: dust, covered by worms. The soil does not distinguish. Death is Job's bitter answer to the equality argument: only here are all made equal, and that is not the comfort anyone wanted."
    },
    "27": {
      "L": "Behold, I know your thoughts and the devices which ye wrongfully imagine against me.",
      "M": "I know your thoughts and the schemes you wrongfully contrive against me.",
      "T": "I see exactly what you are doing. I know the framework of thought behind your speeches — the scheme underneath all the theology. You are constructing a case against me. I know the blueprint."
    },
    "28": {
      "L": "For ye say, 'Where is the house of the prince? And where are the dwelling-places of the wicked?'",
      "M": "For you say, 'Where is the house of the noble man? Where are the dwelling places of the wicked?'",
      "T": "You think you are making an empirical point: 'Show us the house of the powerful wicked man — it will be in ruins.' You are so certain of the pattern."
    },
    "29": {
      "L": "Have ye not asked them that go by the way? And do ye not know their tokens?",
      "M": "Have you not asked those who travel the roads? Do you not know their signs?",
      "T": "Ask anyone who actually moves through the world, watches who thrives and who does not. They carry the evidence. Their accounts are the data. You have been theorizing; they have been observing."
    },
    "30": {
      "L": "That the wicked is spared in the day of calamity and is brought through to the day of wrath.",
      "M": "That the wicked is spared on the day of disaster and delivered through to the day of wrath.",
      "T": "The testimony from those travelers: the wicked man gets through. The day of calamity comes — and he is spared. He is escorted safely through it, preserved for yet another chapter. The judgment everyone predicts keeps not arriving."
    },
    "31": {
      "L": "Who shall declare his way to his face? And who shall repay him what he hath done?",
      "M": "Who will tell him to his face what he has done? Who will repay him for his deeds?",
      "T": "Nobody. That is the point. No one confronts him directly. No one makes him account for what he has done. He moves through life unchallenged — protected by his own power and by the apparent silence of heaven."
    },
    "32": {
      "L": "Yet shall he be carried to the grave, and a watch shall be kept over his tomb.",
      "M": "Yet he is borne to the grave, and a vigil is kept over his tomb.",
      "T": "Even his death is honored. He is carried to burial with ceremony. Guards watch over his tomb. The man who never answered for anything dies with dignity and is given a state funeral."
    },
    "33": {
      "L": "The clods of the valley are sweet to him, and every man shall follow after him, as before him was a countless number.",
      "M": "The clods of the valley lie sweetly upon him; every person follows after him, as numberless are those who went before.",
      "T": "Even the earth over his grave is gentle. He lies easy in the ground — sweetness even in death. After him come the mourners, the whole procession of those who honored him in life. Before him, an uncountable multitude of the dead. He is not alone. He is not disgraced."
    },
    "34": {
      "L": "How then comfort ye me in vain, seeing in your answers there remaineth falsehood?",
      "M": "How then do you comfort me with empty words, when nothing but falsehood remains in your answers?",
      "T": "So explain to me: how does any of what you have said constitute comfort? Every answer you have given is built on a falsehood — the falsehood that the righteous suffer and the wicked perish according to a tidy pattern. The data says otherwise. Your comfort is empty."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 19–21 written.')

if __name__ == '__main__':
    main()
