"""
MKT Job chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-job-10-12.py

=== Contested-term decisions ===

H5315 (נֶפֶשׁ, nefesh): context-driven across all three tiers:
      10:1 (×2) — "soul" (embodied self in anguish)
      11:20     — "the ghost" in the idiom "giving up the ghost" (L/M); T: "breathe their last"
      12:10     — "the life" (life of every living thing; paired with ruach)
      Never rendered as immaterial Greek soul.

H7307 (רוּחַ, ruach): context-driven:
      10:12 — "spirit" (God's care preserved Job's inner life)
      12:10 — "the breath" (the breath of all mankind) — life as bodily breath, paired with nefesh
      No capitalised "Spirit" used; these refer to Job's inner state or creaturely breath, not divine Spirit.

H2617 (חֶסֶד, hesed): 10:12 — "covenant love" (L) / "steadfast love" (M) / "faithful love" (T).
      The richest Hebrew word for love — covenant loyalty + active kindness, untranslatable in one word.
      Job invokes it to heighten the irony: God who gave covenant love is now hunting him.

H3068 (יהוה, YHWH): 12:9 — "the LORD" (L/M) / "the LORD" (T).
      THIS IS THE ONLY OCCURRENCE OF YHWH IN JOB'S SPOKEN DIALOGUE (the Prologue uses it in the
      narrator's framing but the friends and Job typically use El/Eloah/Shaddai). Its appearance
      here is startling — Job invokes the covenantal name precisely while arguing that God's hand is
      behind all suffering and reversals. Noted in T prose but not altered in rendering.

H7706 (שַׁדַּי, Shaddai): 11:7 — "Shaddai" (L) / "the Almighty" (M/T).
      Consistent with ch.7–9 rendering. The name carries force of overwhelming divine power.

H582 (אֱנוֹשׁ, enosh): 10:4, 10:5 — "mortal" (L) / "man/human being" (M) / "frail mortal/human being" (T).
      enosh = the specifically fragile word for humanity. Job deploys it pointedly when asking
      whether God sees the way a limited, mortal creature sees.

H433 (אֱלוֹהַּ, Eloah): singular divine name common in Job. "God" in all tiers.
H410  (אֵל, El): "God" in all tiers.
H120  (אָדָם, adam): "man" (generic humanity) where it appears alongside enosh.

H7585 (שְׁאוֹל, Sheol): 11:8 — "Sheol" (L/M) / "the realm of the dead" (T), consistent with ch.7–9.

=== Structural notes ===

Ch.10: Job's extended direct address to God — the most sustained second-person argument in chs.1–14.
       Key theological move: Job uses God's own creative act (vv.8–12) as evidence against God's
       current behavior. The God who knit him together should not be hunting him like a lion (v.16).
       vv.18–22 return to the death-wish of ch.3 and close with an extended description of Sheol.

Ch.11: Zophar's first speech — the bluntest of the three friends. His tone is dismissive (vv.2–3),
       his argument retributive (vv.4–6), his theology orthodox (vv.7–9), and his application
       merciless (vv.10–12). His "if only you would repent" offer (vv.13–19) reads as sincere
       but utterly misses Job's actual situation. v.12 contains a proverb of breathtaking rudeness.

Ch.12: Job's reply — the opening of a long speech running through ch.14. Job begins with sarcasm
       (vv.2–3), moves to experience (vv.4–6), then launches a doxology of God's sovereign power
       that turns every hymnic affirmation into a demonstration that God's power overrides any
       stable moral order the friends are counting on (vv.13–25).

=== Aspect and tense notes ===

All three chapters are Hebrew poetry (except speech-frame formulas 10:1 header, 11:1, 12:1).
Job 10 uses imperfects heavily — Job's complaint is not a past event but an ongoing state.
Zophar in ch.11 uses imperfects conditionally (vv.13–19: "if you would... then you will...").
Job 12 uses perfect and imperfect alternately in the hymnic section (vv.14–25): God's acts
are both completed (perfect) and characteristic (imperfect). T tier distinguishes these where possible.

=== OT echo notes ===

Job 10:8–12 echoes Psalm 139:13–16 (God's fearful and wonderful formation of the embryo). The
contrast is stark: Psalm 139 ends in wonder and trust; Job 10 ends in a request to be left alone
to die. Same acts, opposite emotional register.

Job 12:9 — the only use of YHWH in Job's own speech. The covenantal name surfaces here in the
context of an argument about suffering and divine sovereignty — a haunting echo of Exodus 34:6–7
where YHWH reveals himself as both merciful and just.

Job 12:22–25 anticipates imagery in Daniel 2:22 (God reveals deep and hidden things) and is
echoed in NT contexts about God exposing hidden things (1 Cor 4:5, Luke 12:2–3).
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
  "10": {
    "1": {
      "L": "My soul loathes my life; I will give loose rein to my complaint; I will speak in the bitterness of my soul.",
      "M": "My soul is sick of my life; I will give free rein to my complaint; I will speak in the bitterness of my soul.",
      "T": "I am done holding back. My whole being is sick of this life — I will pour out every complaint, say every bitter thing that is inside me."
    },
    "2": {
      "L": "I will say to God: Do not condemn me; show me why you contend with me.",
      "M": "I will say to God: Do not condemn me; let me know why you bring charges against me.",
      "T": "I am going to speak directly to God: Stop declaring me guilty. Tell me what the charge is. What exactly have I done that you are pressing this case against me?"
    },
    "3": {
      "L": "Is it good to you to oppress, to despise the work of your hands, and to shine upon the counsel of the wicked?",
      "M": "Does it please you to oppress, to reject the work of your own hands, while you smile on the plans of the wicked?",
      "T": "Is this what suits you — to crush what you yourself made? To throw aside the labor of your own hands while you bless the schemes of the wicked? Someone explain how that makes sense."
    },
    "4": {
      "L": "Have you eyes of flesh? Or do you see as a mortal sees?",
      "M": "Do you have eyes of flesh? Do you see as a human being sees?",
      "T": "Do you see the way we see? Are your eyes the same as these failing mortal eyes — limited, unable to perceive the whole picture? Is that why you seem to misread what you are looking at?"
    },
    "5": {
      "L": "Are your days like the days of a mortal, or your years like the years of a man?",
      "M": "Are your days like those of a human being, or your years like a man's years?",
      "T": "Does your existence have a clock running down? Are your days numbered the way mine are? Is that why you are in such a rush to settle accounts with me now?"
    },
    "6": {
      "L": "that you search out my iniquity and inquire after my sin —",
      "M": "that you search out my wrongdoing and inquire into my sin —",
      "T": "— or is there some divine deadline I do not know about, one that has you scrambling to find evidence against me? Searching my whole life for some sin to pin down?"
    },
    "7": {
      "L": "though you know I am not wicked, and there is none who can deliver from your hand?",
      "M": "though you know I am not guilty, and no one can rescue me from your power?",
      "T": "You already know I am not wicked. You know no one can pull me free from your grip. And still you press me. Why?"
    },
    "8": {
      "L": "Your hands fashioned and made me altogether, and yet you are destroying me.",
      "M": "Your hands shaped and formed me — the whole of me — and now you turn and destroy me.",
      "T": "You made me with your own hands — shaped me, assembled me piece by piece — and now you are taking me apart the same way. The sculptor shattering his own work."
    },
    "9": {
      "L": "Remember that you made me like clay; will you return me again to dust?",
      "M": "Remember that you formed me like clay; will you now bring me back to dust?",
      "T": "You took clay and shaped it into me — remember that, because it was you who did it. And now you plan to dissolve me back into dust? Unmake what you made?"
    },
    "10": {
      "L": "Did you not pour me out like milk and curdle me like cheese?",
      "M": "Did you not pour me out like milk and curdle me like cheese?",
      "T": "You poured me out like milk and watched me coagulate into form — you were there for the whole process of my becoming, and it was entirely your doing."
    },
    "11": {
      "L": "You clothed me with skin and flesh, and wove me together with bones and sinews.",
      "M": "You clothed me with skin and flesh, and knit me together with bones and sinews.",
      "T": "You stitched me into a body — wrapped me in skin and flesh, threaded my bones and sinews together like a craftsman at work. Every layer of me is your handiwork."
    },
    "12": {
      "L": "You granted me life and covenant love, and your visitation has preserved my spirit.",
      "M": "You gave me life and steadfast love, and your watchful care preserved my spirit.",
      "T": "You gave me life — and more than that, you gave me your faithful love. Your constant attentiveness kept my spirit alive. All of this was you. Which makes what you are doing to me now all the more incomprehensible."
    },
    "13": {
      "L": "Yet these things you hid in your heart; I know that this was your intent.",
      "M": "Yet these things you hid in your heart; I know that this was your purpose all along.",
      "T": "But hidden in your heart, all along, you had a design. I see it now. The formation, the faithful love, the care — and then this. Was it arranged from the beginning?"
    },
    "14": {
      "L": "If I sin, you mark it, and you will not acquit me of my iniquity.",
      "M": "If I sin, you take note of it and will not let my guilt go.",
      "T": "The moment I step wrong — if I even step wrong — it is marked. You will not acquit me. Every failure is on record and no record is ever cleared."
    },
    "15": {
      "L": "If I am wicked, woe to me! If I am righteous, I dare not lift up my head, for I am filled with shame and sated with my affliction.",
      "M": "If I am wicked, woe to me! And if I am righteous, I still cannot hold my head up, for I am filled with shame and sunk in my affliction.",
      "T": "I lose either way. Guilty? Woe. Innocent? Still I cannot raise my head — shame presses it down, and affliction has soaked into every layer of me. There is no position in which I win."
    },
    "16": {
      "L": "And if I lift myself up, you hunt me like a lion and again display your marvels against me.",
      "M": "But if I do hold my head up, you hunt me like a fierce lion and again demonstrate your awesome power against me.",
      "T": "And if I dare to lift my head — if I show the slightest defiance — you are on me like a lion. You parade your power against me as though I were some great prize worth the hunt."
    },
    "17": {
      "L": "You renew your witnesses against me and increase your vexation toward me; wave upon wave of trouble and a host of hardships assail me.",
      "M": "You bring fresh witnesses against me and increase your anger toward me; wave after wave of trouble and a host of hardships come against me.",
      "T": "One after another — new charges, new witnesses, renewed anger. You keep escalating. Change follows change and each change brings more affliction than the last. There is no plateau. Only more."
    },
    "18": {
      "L": "Why then did you bring me out from the womb? Would that I had died and no eye had seen me!",
      "M": "Why then did you bring me out of the womb? I wish I had died and no eye had ever seen me!",
      "T": "Then why? Why did you bring me out of the womb at all? If this is what my life was going to amount to, it would have been better to die at birth — unseen, unknown, unmourned."
    },
    "19": {
      "L": "I should have been as though I had never been; I should have been carried from the womb to the grave.",
      "M": "I should never have existed; I should have been carried straight from the womb to the grave.",
      "T": "Carried from one darkness directly to another — from womb to tomb. That would have been far cleaner than this drawn-out unmaking."
    },
    "20": {
      "L": "Are not my days few? Let him cease, so I may take a little comfort before I go —",
      "M": "Are my days not few? Cease — leave me alone, that I may have a little relief before I go —",
      "T": "My days are already running out — there are not many left. Can you not give me a moment's peace? Just a little space to breathe before I go —"
    },
    "21": {
      "L": "— before I go to the land of no return, the land of darkness and the shadow of death —",
      "M": "— to the land of darkness and the shadow of death, from which there is no return —",
      "T": "— down to the land of no return, the country of darkness and death-shadow, where I will not come back from —"
    },
    "22": {
      "L": "— a land of thick gloom as darkness itself, of the shadow of death and disorder, where the light is like darkness.",
      "M": "— a land of utter gloom like thick darkness, of the shadow of death and disorder, where even the light is as darkness.",
      "T": "A country where darkness is the landscape, where what passes for light is only shadow. No order there. No morning. Darkness layered upon darkness, and the shadow of death in every direction."
    }
  },
  "11": {
    "1": {
      "L": "Then Zophar the Naamathite answered and said:",
      "M": "Then Zophar the Naamathite answered and said:",
      "T": "Zophar the Naamathite could wait no longer:"
    },
    "2": {
      "L": "Shall a multitude of words go unanswered, and a man of many lips be justified?",
      "M": "Should this flood of words go unanswered? Should a man of endless talk be counted righteous?",
      "T": "Is all of that supposed to just go unanswered? Does sheer volume of words make a man righteous? Does quantity count as a defense?"
    },
    "3": {
      "L": "Shall your empty talk silence men? When you mock, shall no man put you to shame?",
      "M": "Shall your boasting silence everyone? When you scoff, will no one rebuke you?",
      "T": "Are we all supposed to sit in silence while you go on like this? Is your scoffing at God supposed to go unchallenged? Someone needs to say something."
    },
    "4": {
      "L": "For you have said, 'My teaching is pure, and I am clean in your eyes.'",
      "M": "For you have said, 'My doctrine is right and I am clean in God's sight.'",
      "T": "You have sat there and declared your doctrine above reproach, and yourself clean in God's own eyes. The confidence is breathtaking."
    },
    "5": {
      "L": "But oh, that God would speak and open his lips against you —",
      "M": "If only God would speak and open his lips to answer you —",
      "T": "If only God himself would respond. If only he would open his mouth and tell you what he really thinks of your case —"
    },
    "6": {
      "L": "and tell you the secrets of wisdom, for it has many sides. Know that God has exacted of you less than your iniquity deserves.",
      "M": "and reveal to you the secrets of wisdom — for wisdom has more facets than you know. Know this: God has required of you less than your sin deserves.",
      "T": "— and show you what is hidden in the deep architecture of wisdom, wisdom so complex it exceeds everything you have mapped. Then you would understand what you apparently do not: God has been merciful. He has let you off lighter than you deserve."
    },
    "7": {
      "L": "Can you find out the deep things of God? Can you reach the limit of Shaddai?",
      "M": "Can you search out the deep things of God? Can you find the limit of the Almighty?",
      "T": "You think you understand God well enough to bring charges? Can any human mind reach the bottom of him — find where his wisdom and power hit their outer edge?"
    },
    "8": {
      "L": "Higher than the heavens — what can you do? Deeper than Sheol — what can you know?",
      "M": "It is higher than the heavens — what can you do? Deeper than Sheol — what can you know?",
      "T": "It towers above the highest heaven — your reach falls absurdly short. It descends below the realm of the dead — your understanding cannot follow it down. There is no measurement in heaven or earth that captures him."
    },
    "9": {
      "L": "Its measure is longer than the earth and broader than the sea.",
      "M": "Its measure is longer than the earth and broader than the sea.",
      "T": "Stretch your imagination to the ends of the earth in every direction, out to the farthest edge of the sea — and still you have not reached the boundary of God's wisdom."
    },
    "10": {
      "L": "If he passes through and imprisons and calls an assembly, who can hinder him?",
      "M": "If he sweeps through, imprisons, and convenes a court — who can stop him?",
      "T": "He acts whenever he chooses. He can sweep through, lock things down, convene judgment — and who calls him to account? No one stops what God sets in motion."
    },
    "11": {
      "L": "For he knows hollow men; he sees wickedness — does he not then observe it?",
      "M": "For he knows worthless people; when he sees iniquity, does he not take note of it?",
      "T": "God reads emptiness in a person at a glance. He sees through vanity and sin — does he somehow miss what is directly in front of him? He notices everything."
    },
    "12": {
      "L": "But a hollow man will get understanding when a wild donkey's foal is born a man.",
      "M": "A hollow-headed man will become wise when a wild donkey gives birth to a human being.",
      "T": "The day a fool gains wisdom will be the same day a wild ass gives birth to a human child — which is to say, never. Zophar is placing Job in the category of the permanently unteachable."
    },
    "13": {
      "L": "If you set your heart straight and stretch out your hands to him —",
      "M": "If you would prepare your heart and stretch out your hands toward him —",
      "T": "But if you would — if you would get your heart right, if you would reach out to him in honest submission —"
    },
    "14": {
      "L": "if wickedness is in your hand, put it far away, and let not injustice dwell in your tents —",
      "M": "if there is sin in your hand, remove it far away, and let wickedness have no place in your home —",
      "T": "— if there is evil lodged in your hands, get rid of it. Drive it out entirely. Do not let injustice keep a room under your roof —"
    },
    "15": {
      "L": "then truly you will lift up your face without blemish, and you will be firm and unafraid.",
      "M": "then surely you will lift up your face without shame; you will stand firm and have no fear.",
      "T": "Then you would be able to raise your face again — no stain, no shame. You would stand immovable, and fear would find no foothold anywhere in you."
    },
    "16": {
      "L": "For you will forget your misery; you will remember it as waters that have passed away.",
      "M": "For you will forget your suffering; you will remember it only as water that has long since flowed on.",
      "T": "The suffering you carry now will dissolve. You will look back on it the way you remember a stream that ran past years ago and moved on — nothing left but a dry bed and a distant memory."
    },
    "17": {
      "L": "And your life will be brighter than the noonday; your darkness will be like the morning.",
      "M": "Your life will shine brighter than noon; even your darkest time will be like dawn.",
      "T": "Your life would blaze at noon — and even the darkest thing you can imagine would be morning by comparison. Everything would run upward from here."
    },
    "18": {
      "L": "And you will trust, because there is hope; you will look about you and lie down in safety.",
      "M": "You will have confidence, because there is hope; you will look around you and rest in security.",
      "T": "You would find yourself trusting again — because hope would be real and solid. You would scan the horizon and find nothing threatening. You would lie down and sleep without one anxious thought."
    },
    "19": {
      "L": "You will lie down, and none will disturb you; many will entreat your favor.",
      "M": "You will lie down, and no one will make you afraid; many will come seeking your goodwill.",
      "T": "No one threatening you in the night. Many coming to court your favor — you would become the patron others seek, not the petitioner who begs."
    },
    "20": {
      "L": "But the eyes of the wicked will fail; all escape will be denied them, and their hope is the giving up of the ghost.",
      "M": "But the eyes of the wicked will fail; all means of escape will be closed to them, and their only hope is to breathe their last.",
      "T": "For the wicked, the outcome runs the other way: their sight gives out, every exit is sealed, and the only thing left to hope for is to stop hoping — to breathe their last and have it be over."
    }
  },
  "12": {
    "1": {
      "L": "Then Job answered and said:",
      "M": "Then Job answered:",
      "T": "Job fired back:"
    },
    "2": {
      "L": "Truly, you are the people, and wisdom will die with you!",
      "M": "No doubt you are the ones who know, and wisdom itself will die when you do.",
      "T": "Of course. You three are the last of the truly wise — the moment you die, wisdom dies with you. The world had better take good notes while you are still speaking."
    },
    "3": {
      "L": "But I have understanding as well as you; I am not inferior to you. Who does not know such things as these?",
      "M": "But I have a mind as well as you; I am not less than you. Who does not know such things?",
      "T": "I have a mind too. I am nobody's inferior in this conversation. Everything you have said is common knowledge — who alive does not know these things? You have been profound about nothing."
    },
    "4": {
      "L": "I am become a laughingstock to my neighbor — I who called to God and he answered me — the righteous and blameless man is a laughingstock.",
      "M": "I am a laughingstock to my friends — I who called to God and he answered me — the just and blameless man is held in contempt.",
      "T": "The man who prayed and received an answer — that is who I was. Now I am a joke to my closest friends. Righteous and blameless — and in our world, apparently, that is what earns contempt."
    },
    "5": {
      "L": "A torch is despised in the thought of one at ease, ready for those whose feet are about to slip.",
      "M": "In the mind of one who is comfortable, the lamp of the afflicted is despised — he stands ready to condemn those whose feet stumble.",
      "T": "When you are comfortable yourself, it is easy to look down on someone whose feet have slipped. The privileged man sees another's torch going out and thinks: exactly what they deserve."
    },
    "6": {
      "L": "The tents of robbers are at peace, and those who provoke God live secure — into whose hand God himself brings everything.",
      "M": "The tents of robbers are undisturbed, and those who provoke God live in safety — God himself puts things into their hand.",
      "T": "While I sit in ruins, robbers rest in their tents, undisturbed. The very people who shake their fist at God prosper. And whose hand arranges this? God's. If Zophar's moral accounting worked, none of this would be possible."
    },
    "7": {
      "L": "But ask the animals and they will teach you; the birds of the air and they will tell you.",
      "M": "Ask the animals and they will teach you; the birds of the air will tell you.",
      "T": "You want wisdom? Ask a creature. The beasts know something. The birds overhead can tell you what no human argument has yet managed to land on."
    },
    "8": {
      "L": "Or speak to the earth and it will teach you; the fish of the sea will declare it to you.",
      "M": "Or speak to the earth and it will teach you; the fish of the sea will declare it to you.",
      "T": "Or just look around. The earth itself will school you. The fish moving through the deep have always known it."
    },
    "9": {
      "L": "Who among all these does not know that the hand of the LORD has done this?",
      "M": "Who among all these does not know that the hand of the LORD has done this?",
      "T": "Every creature knows it — the LORD's hand is behind all of this. Note the name: not El, not Eloah, not Shaddai — but the LORD, the covenant name, Yahweh himself. Even in the middle of his argument about undeserved suffering, Job invokes the God who promised to be known."
    },
    "10": {
      "L": "In his hand is the life of every living thing and the breath of all mortal flesh.",
      "M": "In his hand is the life of every living creature and the breath of all human flesh.",
      "T": "Everything that breathes — every creature, every human being — holds that breath only because God holds it. The life of the entire world rests in one hand."
    },
    "11": {
      "L": "Does not the ear test words as the palate tastes food?",
      "M": "Does not the ear test words as the tongue tastes food?",
      "T": "The ear discriminates between words the way the tongue discriminates between flavors. We can tell good argument from bad, nourishment from poison. What you three have served us is not nourishing."
    },
    "12": {
      "L": "With the aged is wisdom, and with length of days comes understanding.",
      "M": "Wisdom belongs to the aged, and understanding comes with long years.",
      "T": "With the old comes wisdom; long experience brings understanding. Bildad was right about this — which is precisely why what Job is about to say should land even harder coming from a man his age."
    },
    "13": {
      "L": "With him are wisdom and might; he has counsel and understanding.",
      "M": "With God are wisdom and strength; he has counsel and understanding.",
      "T": "God has wisdom, power, counsel, and understanding — all of it. Everything the friends attribute to God, Job affirms. What follows is the devastating use of that very truth against their tidy system."
    },
    "14": {
      "L": "If he tears down, it cannot be rebuilt; if he shuts a man in, there is no opening.",
      "M": "What he tears down cannot be rebuilt; if he imprisons a man, there is no release.",
      "T": "He demolishes and nothing goes back up. He closes a door and it stays closed. No one reverses what God has set in motion — not by argument, not by innocence, not by prayer."
    },
    "15": {
      "L": "If he withholds the waters, they dry up; if he releases them, they overwhelm the land.",
      "M": "If he holds back the waters, they dry up; if he releases them, they flood the land.",
      "T": "He withholds rain — drought follows. He opens the floodgates — devastation follows. The same hand that blesses destroys. This is not a system; it is a person, and a sovereign one."
    },
    "16": {
      "L": "With him are strength and sound wisdom; the deceived and the deceiver alike belong to him.",
      "M": "With him are strength and effective wisdom; those who deceive and those who are deceived both belong to him.",
      "T": "Power and practical wisdom — both are his. And even those who deceive and those who are taken in by deception fall within his sovereignty. There is no one who stands outside his domain."
    },
    "17": {
      "L": "He leads counselors away stripped and makes fools of judges.",
      "M": "He leads counselors away stripped of dignity and turns judges into fools.",
      "T": "The wisest advisors stripped bare and marched out. The judges who ruled nations made suddenly ridiculous. This is not chaos — it is God's hand arranging things exactly as he intends."
    },
    "18": {
      "L": "He looses the bond of kings and ties a loincloth around their waist.",
      "M": "He strips kings of their authority and wraps a servant's cloth around their loins.",
      "T": "Kings in all their regalia — he undresses them. Where the belt of power once hung, now only the cloth of a prisoner. God demotes without ceremony or apology."
    },
    "19": {
      "L": "He leads priests away stripped and overthrows those long established in power.",
      "M": "He leads priests away stripped and overturns those who seemed unassailable.",
      "T": "The priests — stripped, led out, reduced to nothing. The ones who looked like permanent fixtures, the entrenched powers of every generation — toppled."
    },
    "20": {
      "L": "He removes the speech of the trusted and takes away the discernment of the elders.",
      "M": "He silences those who are trusted and strips judgment from the aged.",
      "T": "The voices everyone relied on — God silences them. The wisdom of the elders — it evaporates the moment God withdraws it. Nothing is permanent except God himself."
    },
    "21": {
      "L": "He pours contempt upon nobles and looses the belt of the strong.",
      "M": "He pours contempt on princes and loosens the strength of the mighty.",
      "T": "He saturates the nobility with contempt. The belt that held a warrior's strength together — he loosens it. The powerful collapse before they know what is happening to them."
    },
    "22": {
      "L": "He uncovers deep things out of the darkness and brings the shadow of death into the light.",
      "M": "He brings to light the deep things hidden in darkness and brings the shadow of death into the open.",
      "T": "What lies deepest in the dark — he drags it up into the light. Death-shadow itself cannot conceal what God determines to expose."
    },
    "23": {
      "L": "He makes nations great and destroys them; he spreads nations abroad and leads them away.",
      "M": "He makes nations great, then destroys them; he expands them, then scatters them.",
      "T": "He builds a nation into greatness and then dismantles it. He spreads a people across the earth and then drives them away. No nation is permanent. Every empire is on lease."
    },
    "24": {
      "L": "He takes away the understanding of the chiefs of the peoples of the earth and makes them wander in a trackless waste.",
      "M": "He strips understanding from the leaders of the peoples of the earth and makes them wander in a trackless wilderness.",
      "T": "The leaders who were supposed to know the way — he removes their sense of direction. He sets them wandering through a featureless wasteland with no path and no landmark. A kingdom without a map."
    },
    "25": {
      "L": "They grope in the dark without light, and he makes them stagger like a drunken man.",
      "M": "They grope in the dark without light, and he makes them stagger like drunkards.",
      "T": "They reach out with their hands in pitch darkness, feeling for something solid that is not there. And God keeps them staggering like drunks — leading nations nowhere, blind and reeling, unable to find even the ground beneath their feet."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'job')
        merge_tier(existing, JOB, tier_key)
        save(tier_dir, 'job', existing)
    print('Job 10–12 written.')

if __name__ == '__main__':
    main()
