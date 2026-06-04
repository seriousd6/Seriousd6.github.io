"""
MKT Psalms chapters 34–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-34-36.py

=== Overview of this unit ===

Ps 34 — Acrostic Praise After Deliverance (22 verses): An aleph-bet acrostic (one Hebrew
         letter per verse; waw is skipped and a pe added at the close — a known variant of
         the form). The superscription links it to 1 Sam 21:10-15, though the king there
         is called "Achish"; "Abimelech" is likely a dynastic title for Philistine rulers
         (as "Pharaoh" for Egyptian ones). Structure: personal thanksgiving (vv1-10) →
         wisdom instruction to the young (vv11-14) → theological contrasts (vv15-22).
         V20 ("not one of his bones is broken") is applied to Jesus in John 19:36.
         V8 ("taste and see") is echoed in 1 Peter 2:3.

Ps 35 — Lament Calling for Divine Intervention Against Unjust Enemies (28 verses): An
         imprecatory psalm in three strophes, each ending with a vow of praise (v9-10,
         v18, v27-28). The psalmist describes faithful covenant conduct toward those who
         later became his enemies (vv13-14), heightening the injustice. V19 ("hate me
         without cause") is applied by Jesus to himself in John 15:25.
         The shift from third-person enemies to second-person prayer (vv22-28) is the
         psalm's rhetorical climax.

Ps 36 — Contrast: Human Wickedness / Divine Attributes (12 verses): Two movement psalm.
         Vv1-4 describe the inner logic of the wicked — sin delivers its own oracle
         (H5002, נְאֻם ne'um) from within his heart. Vv5-9 celebrate four divine
         attributes in ascending cosmic scale. Vv10-12 close with a petition for protection
         and a vision of the wicked's ruin. The H2617 (hesed) language of vv5/7/10 frames
         the psalm's theological centre.

=== Superscriptions ===

Following the convention of PSA-1 through PSA-4 (mkt-psalms-1-6.py through
mkt-psalms-19-24.py), superscription text is merged into v1 of each psalm,
separated from the verse body by a double blank in T tier.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M throughout, maintaining the established PSA small-caps
      convention. In T tier: "the LORD" — the Psalter's liturgical voice is preserved.
      Not switched to "Yahweh" here; no prior script in this book made that switch.

H430  (אֱלֹהִים, Elohim): "God" in all tiers. Ps 36:7 uses El (H410) vocatively; rendered
      "O God" in L/M and "O God" in T.

H410  (אֵל, El, Ps 36:6 "mountains of God/El"): The phrase הַרְרֵי אֵל is a Hebrew
      superlative: "mightiest mountains / mountains of God." L: "mighty mountains" (ESV
      tradition). M/T: "towering mountains" with T adding interpretive force.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M. In T tier, contextual rendering:
      - Ps 34:2 "my soul will boast" → "my whole self"
      - Ps 35:3 "say to my soul" → "speak this word to my deepest self"
      - Ps 35:9 "my soul shall rejoice" → "my whole self will burst out"
      - Ps 35:12 "bereaving my soul" → "my soul" (idiomatic, context of desolation)
      - Ps 35:13 "I humbled my soul" → idiom for fasting; "I humbled myself"
      - Ps 35:17 "my darling/only one" (יָחִיד yachid = precious/unique life) → "my only life"
      - Ps 36:9 — nefesh does not appear in Ps 36

H7307 (רוּחַ, ruach, Ps 34:18): Here used of the human "spirit" — "those crushed in spirit."
      Lowercase throughout. Not the divine Spirit; context is human suffering.

H2617 (חֶסֶד, hesed, Ps 36:5,7,10): "Steadfast love" in all tiers — MKT standard.
      "Mercy" (KJV) is avoided; "lovingkindness" (NASB) is too opaque in modern English.

H5002 (נְאֻם, ne'um, Ps 36:1): Normally "oracle/utterance" — the word used for prophetic
      divine pronouncements. Here inverted: sin/transgression speaks its own oracle from
      within the wicked heart. L: "oracle of transgression." M: "the voice of transgression."
      T: "Transgression delivers its oracle" — to foreground the structural irony.

H5542 (סֶלָה, selah): Not present in Psalms 34, 35, or 36. No selah appears in any of
      the three chapters covered by this script.

H6918 (קָדוֹשׁ, qadosh, Ps 34:9 "saints/holy ones"): "Holy ones" in L, "holy people" in M,
      "all who belong to him" in T — those consecrated to the LORD's service.

H1732 (David, in superscriptions): Rendered as "of David" or "A Psalm of David" following
      established PSA convention. The preposition lamed is relational (attributed to David),
      not necessarily authorial.

=== OT echoes and NT connections ===

- Ps 34:8 → 1 Pet 2:3: "Taste and see" language applied to experiencing Christ
- Ps 34:20 → John 19:36: "Not one of his bones will be broken" applied to the crucifixion
- Ps 35:19 → John 15:25: "They hated me without cause" applied to Jesus by Jesus himself
- Ps 36:9 "the fountain of life" → John 4 (living water), Rev 22:1 (river of life)
- Ps 36:6 "great deep" (תְּהוֹם) → Gen 1:2 intertextual echo; God's justice is as
  primordially vast and inscrutable as the creation-deep

=== Aspect and tense notes ===

Hebrew perfect and imperfect verbs in lament and praise psalms often express timeless
realities ("the LORD is near") or ongoing/continuous action, not one-time past events.
Where context demands, present tense is used even when the Hebrew perfect occurs.
The acrostic structure of Ps 34 does not affect tense decisions.
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
  "34": {
    "1": {
      "L": "A Psalm of David, when he changed his behavior before Abimelech, who drove him away, and he departed. I will bless the LORD at all times; his praise shall continually be in my mouth.",
      "M": "A Psalm of David, when he pretended to be insane before Abimelech, who drove him away, and he left. I will bless the LORD at all times; his praise will always be on my lips.",
      "T": "A Psalm of David, when he feigned madness before Abimelech, who expelled him, and he went away.\n\nI will bless the LORD at all times;\nhis praise will never leave my lips."
    },
    "2": {
      "L": "My soul will boast in the LORD; the humble shall hear and be glad.",
      "M": "My soul boasts in the LORD; the humble will hear and be glad.",
      "T": "In the LORD my whole self will boast;\nlet the humble hear it and rejoice."
    },
    "3": {
      "L": "O magnify the LORD with me, and let us exalt his name together.",
      "M": "Magnify the LORD with me, and let us exalt his name together.",
      "T": "Come, make the LORD great with me;\nlet us lift his name higher together."
    },
    "4": {
      "L": "I sought the LORD and he answered me, and from all my fears he delivered me.",
      "M": "I sought the LORD, and he answered me; he delivered me from all my fears.",
      "T": "I sought the LORD, and he answered;\nfrom every fear that gripped me he set me free."
    },
    "5": {
      "L": "They looked to him and were radiant, and their faces were not ashamed.",
      "M": "Those who look to him are radiant with joy, and their faces will never be ashamed.",
      "T": "All who look to him become radiant;\ntheir faces will never be covered with shame."
    },
    "6": {
      "L": "This poor man cried, and the LORD heard him, and out of all his troubles he saved him.",
      "M": "This poor man cried, and the LORD heard him; he saved him out of all his troubles.",
      "T": "Here — one man in poverty cried out,\nand the LORD heard him\nand rescued him from every trouble."
    },
    "7": {
      "L": "The angel of the LORD encamps around those who fear him, and delivers them.",
      "M": "The angel of the LORD encamps around those who fear him and rescues them.",
      "T": "The angel of the LORD stations himself\naround those who fear the LORD\nand brings them to safety."
    },
    "8": {
      "L": "O taste and see that the LORD is good! Blessed is the man who takes refuge in him!",
      "M": "Taste and see that the LORD is good! Blessed is the person who takes refuge in him!",
      "T": "Come and taste — find out for yourself that the LORD is good.\nBlessed is the one who shelters in him."
    },
    "9": {
      "L": "O fear the LORD, you his holy ones, for those who fear him have no lack.",
      "M": "Fear the LORD, you his holy people, for those who fear him lack nothing.",
      "T": "Fear the LORD, all you who belong to him —\nthose who fear him go without nothing."
    },
    "10": {
      "L": "Young lions suffer want and hunger, but those who seek the LORD lack no good thing.",
      "M": "Young lions go hungry and lack food, but those who seek the LORD lack no good thing.",
      "T": "Young lions may prowl hungry,\nbut those who seek the LORD want for nothing good."
    },
    "11": {
      "L": "Come, children, listen to me; the fear of the LORD I will teach you.",
      "M": "Come, children, listen to me; I will teach you the fear of the LORD.",
      "T": "Come, my children — listen to me;\nI will teach you what it means to fear the LORD."
    },
    "12": {
      "L": "Who is the man who desires life, who loves many days to see good?",
      "M": "Who is the person who desires life and loves long days to enjoy what is good?",
      "T": "Who here wants a full life —\nlongs for many days stretched out to see what is good?"
    },
    "13": {
      "L": "Keep your tongue from evil and your lips from speaking deceit.",
      "M": "Keep your tongue from evil and your lips from speaking lies.",
      "T": "Guard your tongue from what causes harm;\nkeep your lips from every form of deception."
    },
    "14": {
      "L": "Depart from evil and do good; seek peace and pursue it.",
      "M": "Turn from evil and do good; seek peace and go after it.",
      "T": "Turn your back on evil — do what is right;\nhunt down peace and run after it."
    },
    "15": {
      "L": "The eyes of the LORD are toward the righteous, and his ears toward their cry for help.",
      "M": "The LORD's eyes are on the righteous and his ears are open to their cry.",
      "T": "The LORD's eyes are fixed on the righteous;\nhis ears are tuned to every cry they raise."
    },
    "16": {
      "L": "The face of the LORD is against those who do evil, to cut off their remembrance from the earth.",
      "M": "The LORD turns his face against those who do evil, to erase all memory of them from the earth.",
      "T": "The LORD sets his face against evildoers\nto wipe every trace of them from the earth."
    },
    "17": {
      "L": "The righteous cry, and the LORD hears, and from all their troubles he delivers them.",
      "M": "The righteous cry out, and the LORD hears; he delivers them from all their troubles.",
      "T": "The righteous cry out — the LORD hears;\nfrom every trouble he brings them out."
    },
    "18": {
      "L": "The LORD is near to the brokenhearted and saves the crushed in spirit.",
      "M": "The LORD is close to the brokenhearted and rescues those whose spirit is crushed.",
      "T": "The LORD stays close to those whose hearts are broken;\nhe rescues those whose spirit has been ground to dust."
    },
    "19": {
      "L": "Many are the afflictions of the righteous, but from all of them the LORD delivers him.",
      "M": "The righteous face many afflictions, but the LORD delivers them from all of them.",
      "T": "The righteous face trouble after trouble —\nbut the LORD delivers them from every one."
    },
    "20": {
      "L": "He guards all his bones; not one of them is broken.",
      "M": "He protects all his bones; not one of them will be broken.",
      "T": "He guards every bone in his body —\nnot one of them will be broken."
    },
    "21": {
      "L": "Evil shall slay the wicked, and those who hate the righteous shall be condemned.",
      "M": "Evil will slay the wicked, and those who hate the righteous will be condemned.",
      "T": "Evil will be the undoing of the wicked;\nthose who hate the righteous will face their own condemnation."
    },
    "22": {
      "L": "The LORD redeems the soul of his servants; none of those who take refuge in him shall be condemned.",
      "M": "The LORD redeems the lives of his servants; none who take refuge in him will be condemned.",
      "T": "The LORD ransoms the lives of those who serve him;\nnot one who shelters in him will ever be condemned."
    }
  },
  "35": {
    "1": {
      "L": "A Psalm of David. Plead my cause, O LORD, with those who strive against me; fight against those who fight against me!",
      "M": "A Psalm of David. Contend, O LORD, against those who contend with me; fight against those who fight against me!",
      "T": "A Psalm of David.\n\nTake up my case, LORD, against those who take up arms against me;\nfight those who fight me."
    },
    "2": {
      "L": "Take hold of shield and buckler and rise for my help!",
      "M": "Take up your shield and armor and come to my aid!",
      "T": "Grip your shield and buckler;\nrise up to fight for me."
    },
    "3": {
      "L": "Draw out the spear and stop the way against those who pursue me; say to my soul, 'I am your salvation!'",
      "M": "Brandish the spear and block the path of those who pursue me; say to my soul, 'I am your deliverance!'",
      "T": "Raise your spear — cut off the path of those who hunt me;\nspeak this word to my deepest self: 'I am the one who saves you.'"
    },
    "4": {
      "L": "Let them be put to shame and dishonor who seek my life; let them be turned back and confused who devise evil against me.",
      "M": "Let those who seek my life be put to shame and humiliated; let those who plot evil against me be turned back in confusion.",
      "T": "Let those who pursue my life be driven back in shame;\nlet all who scheme to harm me reel in humiliation."
    },
    "5": {
      "L": "Let them be as chaff before the wind, with the angel of the LORD driving them away.",
      "M": "Let them be like chaff before the wind, with the angel of the LORD driving them off.",
      "T": "Drive them like chaff before the wind;\nlet the angel of the LORD scatter them."
    },
    "6": {
      "L": "Let their way be dark and slippery, with the angel of the LORD pursuing them.",
      "M": "Make their path dark and treacherous, with the angel of the LORD pursuing them.",
      "T": "Make their road dark and ice-slick;\nsend the angel of the LORD to hound them without rest."
    },
    "7": {
      "L": "For without cause they hid their net for me; without cause they dug a pit for my soul.",
      "M": "For without reason they concealed their net to trap me; without reason they dug a pit for my life.",
      "T": "They laid a hidden net to catch me — unprovoked;\nthey dug a pit to take my life — for no reason at all."
    },
    "8": {
      "L": "Let destruction come upon him when he does not know it; let the net he hid ensnare him; let him fall in it to his ruin.",
      "M": "May ruin overtake him when he least expects it; may the net he hid catch him; may he fall in it to his destruction.",
      "T": "Let devastation come on him out of nowhere;\nlet the very net he hid close around him;\nlet him plunge headlong into his own pit."
    },
    "9": {
      "L": "Then my soul shall rejoice in the LORD, exulting in his salvation.",
      "M": "Then my soul will rejoice in the LORD, exulting in his deliverance.",
      "T": "Then my whole self will burst into joy before the LORD,\nexulting in the rescue he brings."
    },
    "10": {
      "L": "All my bones shall say, 'O LORD, who is like you, who delivers the poor from him who is too strong, the poor and needy from him who robs him?'",
      "M": "Every bone in my body will say, 'LORD, who is like you? Who rescues the poor from those who overpower them, the poor and needy from those who rob them?'",
      "T": "Every bone I have will shout:\n'LORD — who can compare to you?\nYou rescue the helpless from those who crush them;\nthe poor and vulnerable from those who strip them bare.'"
    },
    "11": {
      "L": "Malicious witnesses rise up; they ask me about things I do not know.",
      "M": "Malicious witnesses rise against me; they charge me with things I know nothing of.",
      "T": "Hostile witnesses surge to their feet;\nthey interrogate me about things I never did."
    },
    "12": {
      "L": "They repay me evil for good; my soul is bereaved.",
      "M": "They repay me evil for good, leaving my soul desolate.",
      "T": "Good they return with evil —\nand my soul is left utterly alone."
    },
    "13": {
      "L": "But I, when they were sick — sackcloth was my clothing; I humbled my soul with fasting; and my prayer returned into my own bosom.",
      "M": "But when they were sick, I wore sackcloth and humbled myself with fasting; my prayer returned to my own chest.",
      "T": "But when they were sick I put on sackcloth;\nI bowed myself low with fasting.\nMy prayer curved back upon my own breast —\nand still I kept on praying."
    },
    "14": {
      "L": "I went about as though he were my friend or my brother; as one mourning his mother I bowed in mourning.",
      "M": "I acted like one grieving for a dear friend or brother; I bowed down in mourning as one who weeps for his mother.",
      "T": "I moved among them as one weeping for a close friend, a brother;\nI was bowed down in grief as though mourning my own mother."
    },
    "15": {
      "L": "But at my stumbling they rejoiced and gathered; the assailants gathered against me — I did not know it. They tore at me without ceasing.",
      "M": "But when I stumbled, they rejoiced and gathered together; attackers assembled against me without my knowing, and tore at me relentlessly.",
      "T": "But the moment I fell they celebrated and closed in;\nstrangers I had never known rallied against me\nand tore at me without stopping."
    },
    "16": {
      "L": "Like profane mockers at a feast, they gnashed their teeth at me.",
      "M": "Like godless mockers at a banquet, they gnashed their teeth at me.",
      "T": "Like sneering gluttons who mock the sacred,\nthey bared their teeth at me."
    },
    "17": {
      "L": "How long, O Lord, will you look on? Rescue my soul from their destruction, my only one from the lions!",
      "M": "How long, O Lord, will you keep watching? Rescue my life from their devastation, my precious self from these lions!",
      "T": "Lord — how long will you just look on?\nSave my life from their rampage;\nrescue my only life from the grip of these lions."
    },
    "18": {
      "L": "I will give you thanks in the great congregation; in the mighty throng I will praise you.",
      "M": "I will give you thanks in the great assembly; among the vast multitude I will praise you.",
      "T": "I will thank you in the great congregation;\nbefore the vast throng I will sing your praise."
    },
    "19": {
      "L": "Let not those who are wrongfully my enemies rejoice over me; let not those who hate me without cause wink the eye.",
      "M": "Do not let my enemies gloat over me without cause; do not let those who hate me without reason exchange knowing glances.",
      "T": "Do not let my unjust enemies celebrate my fall;\ndo not let those who hate me for nothing\nexchange triumphant glances."
    },
    "20": {
      "L": "For they do not speak peace, but against those who are quiet in the land they devise words of deceit.",
      "M": "For they do not pursue peace; instead they invent slanders against those who live quietly in the land.",
      "T": "They have no intention of making peace —\nthey brew up lies against those who only want to live undisturbed."
    },
    "21": {
      "L": "They open wide their mouths against me; they say, 'Aha! Aha! Our eyes have seen it!'",
      "M": "They open their mouths wide against me and say, 'Aha! Aha! We have seen it with our own eyes!'",
      "T": "They gape their mouths wide at me:\n'Aha! Aha! — we saw it ourselves, with our own eyes!'"
    },
    "22": {
      "L": "You have seen, O LORD; be not silent! O Lord, be not far from me!",
      "M": "You have seen this, LORD; do not stay silent. Lord, do not stay far from me.",
      "T": "You have seen it, LORD — do not keep silent!\nDo not stay far away, my Lord."
    },
    "23": {
      "L": "Stir up yourself and awake for my vindication, for my cause, my God and my Lord!",
      "M": "Arise and wake yourself to my defense, for my cause, my God and my Lord!",
      "T": "Rouse yourself — stir yourself awake, Lord!\nDefend my case; it is your cause too,\nmy God and my Lord."
    },
    "24": {
      "L": "Judge me, O LORD my God, according to your righteousness, and let them not rejoice over me!",
      "M": "Vindicate me, LORD my God, according to your righteousness, and do not let them triumph over me.",
      "T": "Give me the justice your righteousness demands, LORD my God;\ndo not hand them the victory over me."
    },
    "25": {
      "L": "Let them not say in their hearts, 'Aha, our heart's desire!' Let them not say, 'We have swallowed him up.'",
      "M": "Do not let them say in their hearts, 'Aha, just what we wanted!' Do not let them say, 'We have devoured him!'",
      "T": "Do not let them say in their hearts: 'Exactly what we wanted!'\nDo not let them say: 'We swallowed him whole!'"
    },
    "26": {
      "L": "Let them be ashamed and confounded altogether who rejoice at my calamity! Let them be clothed with shame and dishonor who magnify themselves against me!",
      "M": "Let all who rejoice at my misfortune be put to shame and humiliated together; let those who exalt themselves against me be clothed with shame and disgrace.",
      "T": "Let everyone who celebrates my ruin\nbe covered in shame and left in confusion.\nLet those who puff themselves up against me\nbe wrapped in disgrace like a garment."
    },
    "27": {
      "L": "Let those who delight in my righteousness shout for joy and be glad and say evermore, 'Great is the LORD, who delights in the welfare of his servant!'",
      "M": "Let those who delight in my vindication shout for joy and be glad, and let them say always, 'Great is the LORD, who takes pleasure in the welfare of his servant!'",
      "T": "But let those who want justice for me\nshout for joy and be glad,\nand say without stopping:\n'The LORD is great — he takes delight\nin the well-being of the one who serves him!'"
    },
    "28": {
      "L": "Then my tongue shall speak of your righteousness and of your praise all the day long.",
      "M": "Then my tongue will proclaim your righteousness and your praise all day long.",
      "T": "Then my tongue will tell of your righteousness\nand sing your praise all day long."
    }
  },
  "36": {
    "1": {
      "L": "To the chief Musician. A Psalm of David, the servant of the LORD. An oracle of transgression speaks to the wicked within his heart: there is no fear of God before his eyes.",
      "M": "To the choirmaster. A Psalm of David, the servant of the LORD. The voice of transgression speaks deep within the heart of the wicked: there is no fear of God before his eyes.",
      "T": "To the worship leader. A Psalm of David, servant of the LORD.\n\nTransgression delivers its oracle to the wicked\nfrom within his own heart:\nthere is no fear of God behind his eyes."
    },
    "2": {
      "L": "For he flatters himself in his own eyes, that his iniquity cannot be found out and hated.",
      "M": "For he deceives himself into thinking his guilt cannot be discovered and condemned.",
      "T": "He has convinced himself his guilt will never come to light —\nthat it cannot be exposed and despised."
    },
    "3": {
      "L": "The words of his mouth are iniquity and deceit; he has ceased to act wisely and do good.",
      "M": "His mouth pours out wickedness and deception; he has stopped acting wisely or doing good.",
      "T": "Everything he says breeds harm and lies;\nhe has abandoned wisdom\nand cannot find his way to good."
    },
    "4": {
      "L": "He devises mischief upon his bed; he sets himself in a way that is not good; he does not reject evil.",
      "M": "On his bed he hatches schemes; he places himself on a path that is not good; he refuses to reject evil.",
      "T": "He lies on his bed planning trouble;\nhe puts himself on a road that leads nowhere good\nand never turns away from evil."
    },
    "5": {
      "L": "Your steadfast love, O LORD, is in the heavens; your faithfulness reaches to the clouds.",
      "M": "Your steadfast love, LORD, reaches to the heavens; your faithfulness extends to the clouds.",
      "T": "Your steadfast love, LORD, spans the height of the heavens;\nyour faithfulness rises to the clouds."
    },
    "6": {
      "L": "Your righteousness is like the mighty mountains; your judgments are like the great deep; man and beast you save, O LORD.",
      "M": "Your righteousness towers like the mighty mountains; your judgments plunge as deep as the ocean; you preserve both human and animal, O LORD.",
      "T": "Your righteousness stands like the towering mountain ranges of God;\nyour justice runs as deep as the primordial ocean.\nYou preserve life, LORD — human life and animal life alike."
    },
    "7": {
      "L": "How precious is your steadfast love, O God! The children of man take refuge in the shadow of your wings.",
      "M": "How priceless is your steadfast love, O God! The children of humanity take refuge under the shadow of your wings.",
      "T": "How unspeakably precious is your steadfast love, O God!\nAll who are human run to shelter\nunder the shadow of your wings."
    },
    "8": {
      "L": "They are abundantly satisfied from the fatness of your house, and you make them drink from the river of your delights.",
      "M": "They feast on the richness of your house, and you give them drink from the river of your pleasures.",
      "T": "They feast on the abundance of your house;\nyou give them to drink from the river of your own delights."
    },
    "9": {
      "L": "For with you is the fountain of life; in your light do we see light.",
      "M": "For with you is the fountain of life; by your light we see light.",
      "T": "With you is the source of all life;\nby your light we finally see everything clearly."
    },
    "10": {
      "L": "Continue your steadfast love to those who know you, and your righteousness to the upright in heart.",
      "M": "Extend your steadfast love to those who know you, and your righteousness to the upright in heart.",
      "T": "Keep on showing your steadfast love to those who know you;\nstretch your righteousness over the straight-hearted."
    },
    "11": {
      "L": "Let not the foot of pride come upon me, nor the hand of the wicked drive me away.",
      "M": "Let not the foot of arrogance trample me, nor the hand of the wicked drive me from my place.",
      "T": "Do not let the arrogant trample over me;\ndo not let the hand of the wicked push me out."
    },
    "12": {
      "L": "There the workers of iniquity are fallen; they are thrust down and cannot rise.",
      "M": "There the evildoers lie fallen; they have been thrust down and cannot get up.",
      "T": "There — look — the evildoers have fallen;\nthey were hurled down\nand cannot rise again."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 34–36 written.')

if __name__ == '__main__':
    main()
