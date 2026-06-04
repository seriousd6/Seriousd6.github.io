"""
MKT Psalms chapters 25–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-25-30.py

=== Overview of this unit ===

Ps 25 (22 v) — Acrostic prayer of trust and petition (aleph–taw structure; English
    translation does not reproduce the acrostic). The psalm moves between personal
    petition (vv1–7), theological reflection on God's ways (vv8–14), and renewed
    personal plea (vv15–21), closing with a communal coda (v22). H5475 (sod, v14)
    is the pivot word: the LORD shares his inner counsel with those who fear him.

Ps 26 (12 v) — Declaration of integrity and petition for vindication. David submits
    himself to divine examination and distinguishes his life from the wicked. The
    ritual gesture of washing hands (v6) before approaching the altar sets the legal
    register: he is not guilty; he loves God's house. H3629 (kelayot, v2) = kidneys
    as the seat of the moral imagination, rendered "inmost self" in M.

Ps 27 (14 v) — Two-movement psalm: supreme confidence (vv1–6) followed by urgent
    prayer (vv7–14). The opening declaration "The LORD is my light and my salvation"
    is the theological summit of the first movement. v4's "one thing" is the single-
    minded desire for God's presence that underlies everything else. v13 contains a
    particle suggesting "I would have despaired—unless I had believed": T surfaces
    this implicit conditional force. v14's double "wait for the LORD" is the closing
    command, addressed as much to David himself as to any hearer.

Ps 28 (9 v) — Prayer for justice and deliverance that pivots to praise. David fears
    being swept away with the wicked (vv1–4) on the basis that the wicked ignore
    God's works (v5). The pivot comes at v6 with "Blessed be the LORD!" — the answer
    has already been received in spirit. v8 identifies "his anointed" (H4899, mashiach)
    with the king; the Davidic covenant horizon is the same as Ps 18:50.

Ps 29 (11 v) — The voice of the LORD in the storm. Seven occurrences of qol YHWH
    ("the voice of the LORD", vv3–9) march across the poem like thunder: over the
    waters, breaking cedars, flashing fire, shaking the wilderness, calving deer. The
    heavenly audience (v1, H1121 H410 bene elim, "sons of the mighty") is called to
    worship the one who commands what they cannot. H3999 (mabbul, v10) = the primordial
    Flood of Genesis 6–9 — not just any flood; the LORD who sat over that chaos still
    sits enthroned. The psalm closes (v11) by turning the storm's power into a blessing
    for God's people.

Ps 30 (12 v) — Thanksgiving song for deliverance from near-death. The superscription
    links it to the dedication of the temple/house (H2598, chanukkat = same root as
    Hanukkah). The argument of vv8–10 is bold: the psalmist appeals to God's self-
    interest — what does God gain from a dead worshiper? H4234 (machol, v11) = dancing.
    H3519 (kavod, v12) = "glory/spirit" — consistent with Ps 16:9 decision, rendered
    "spirit" in M and "whole self" in T to maintain the body-parts parallelism.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M throughout. In T: "LORD"
    consistently — no "Yahweh" substitution. The warmth of direct address preserved.
    Consistent with all prior MKT Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. No note needed per verse.

H136 (אֲדֹנָי, Adonai, Ps 30:8): "the Lord" in L, "the Lord" in M, "my Master" in T.
    The distinction between YHWH and Adonai is preserved as in Ps 16:2; Ps 28 does
    not use Adonai.

H2617 (חֶסֶד, chesed, Ps 25:6,7,10; 26:3): "steadfast love" in all tiers. Consistent
    with all prior MKT scripts. Chesed = covenantal loyalty actively expressed.

H571 (אֶמֶת, emet, Ps 25:5,10; 26:3): "truth" in L; "faithfulness" in M/T. The
    semantic range covers both stable truth and covenant trustworthiness. In contexts
    alongside chesed, the covenant-loyalty sense dominates; "faithfulness" better
    captures the relational register than "truth" alone.

H5475 (סוֹד, sod, Ps 25:14): "secret" in L (classic KJV tradition). In M: "confides
    in." In T: "inner counsel." The word denotes the inner circle of intimate deliberation
    — the counsel shared between close associates. The glossary primary "assembly" is
    too weak; the context is covenantal intimacy, not a formal gathering.

H5315 (נֶפֶשׁ, nefesh): "soul" in L throughout. In M/T: "soul" or "life" or "self"
    by context. Ps 25:1,13,20 — embodied self; Ps 26:9 — "my life"; Ps 28:2 — implied
    in prayer. Not the Greek immaterial soul; nefesh is the whole living person.

H3629 (כְּלָיוֹת, kelayot, Ps 26:2): "kidneys" in L (anatomically accurate). In M:
    "inmost self." In T: "deepest self." The kidneys were the seat of moral conscience
    and interior wisdom in Hebrew thought. Consistent with Ps 16:7 decision.

H1121 + H410 (בְּנֵי אֵלִים, bene elim, Ps 29:1): Literally "sons of the gods/El."
    L: "sons of the mighty" — literalistic but accessible. M: "heavenly beings" — modern
    scholarly consensus (ESV, NRSV). T: "powers of the heavenly court" — makes the
    divine-council dimension explicit. These are angelic or divine beings called to
    worship YHWH as supreme; the Canaanite cognate is baal's council, here repurposed.

H3999 (מַבּוּל, mabbul, Ps 29:10): "Flood" (capitalized) in all tiers. This is the
    technical term for the Genesis Flood (used exclusively in Gen 6–11 and here). The
    LORD who commanded the primordial chaos still sits enthroned above it. T surfaces
    the "primordial" register explicitly.

H2598 (חֲנֻכַּת, chanukkat, Ps 30 superscription): "dedication" in all tiers.
    Same root as Hanukkah. The psalm was used at the rededication of the temple; the
    original dedication context is David's. Transliteration not used — "Dedication" is
    the clear English equivalent.

H3519 (כָּבוֹד, kavod, Ps 30:12): "glory" in L. In M: "spirit" (following the body-
    parts sequence: heart / spirit / flesh from Ps 16:9). In T: "whole self" — reading
    kavod as the most excellent part of the self, the seat of praise. Documented
    deviation from the primary gloss "glory"; consistent with Ps 16:9 decision.

H4234 (מָחוֹל, machol, Ps 30:11): "dancing" in all tiers. The word specifically denotes
    dance; no ambiguity.

=== Aspect and tense notes ===

Ps 25 — Mix of perfect and imperfect: vv2–3 use H982 (batach, perfect) = "I have
    trusted / I have put my hope" — completed orientations with present force. v5 uses
    imperfect for "I wait" (ongoing). v8 uses participle ("the one who teaches") — ongoing
    habitual action. M/T render in natural English, respecting the aspectual distinctions.

Ps 26 — v1 H982 (batach, perfect) "I have trusted" — same completed-trust pattern as
    Ps 13:5 and 25:2. vv2–5 use perfect verbs for David's character description — these
    are completed habits, not one-time acts; M renders as present English ("I walk").

Ps 27 — v1 nominal clauses (no verbs) in Hebrew: "The LORD — my light, my salvation" —
    pure predication, not a verb form. L/M use "is" for natural English; T preserves the
    staccato force. vv13–14 shift to confident assertion and imperative.

Ps 28 — v5 "he will tear down" (imperfect, future) vs v6 "he has heard" (perfect) —
    the shift marks the psalmist's faith: the future judgment is certain, and the past
    answer is already claimed by faith even before it arrives.

Ps 29 — All qol YHWH clauses are stative/participial in feel; the "voice" is both the
    sound and the agent. T tier uses short declarative sentences to hammer the rhythm.

Ps 30 — vv6–7 use two perfects describing David's former prosperity ("I said," "you
    made strong") followed by imperfect "I was terrified" — narrative past sequence.
    v11 uses perfects for completed acts: "you have turned ... you have loosed ... you
    have clothed" — the transformation is already accomplished.

=== OT echo notes ===

Ps 25:14 — "The secret of the LORD is with those who fear him": echoes the Wisdom
    tradition where knowledge and the fear of the LORD are inseparable (Prov 1:7; 9:10).
    The covenant (H1285, berit) is made known to the same people — covenant and wisdom
    are linked here, not separated.

Ps 27:1 — "The LORD is my light" evokes the priestly blessing's "the LORD make his face
    shine upon you" (Num 6:25) and anticipates the Servant of Isaiah ("I will make you a
    light to the nations," Isa 49:6). Light as divine presence is the shared register.

Ps 28:8 — "The LORD is the saving strength of his anointed" — the Davidic covenant
    language (2 Sam 7; Ps 18:50; Ps 2:2). The mashiach here is the king; the NT reads
    this typologically toward the ultimate anointed.

Ps 29 — The whole psalm echoes Canaanite storm-god (Baal) hymns, deliberately repurposing
    the genre to declare YHWH's supremacy. The heavenly assembly (v1) is Baal's council;
    the storm theophany is Baal's signature; here all of it belongs to Israel's God. The
    theological move is polemical and triumphant.

Ps 29:10 — "The LORD sat enthroned at the Flood" echoes Gen 1 (Spirit over the waters)
    and the Noah narrative. God was sovereign over the greatest chaos; he is sovereign now.

Ps 30:3 — "You have brought up my soul from Sheol" uses the language of resurrection
    before resurrection is fully developed as a doctrine. The NT will find here a pattern
    that points beyond individual rescue to the resurrection of Christ.
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

  # ============================================================
  # Psalm 25 — Acrostic Prayer: Guidance, Forgiveness, Trust
  # ============================================================
  "25": {
    "1": {
      "L": "A Psalm of David. To you, O LORD, I lift up my soul.",
      "M": "A Psalm of David. To you, LORD, I lift up my soul.",
      "T": "Of David.\nTo you, LORD—I raise my whole self up."
    },
    "2": {
      "L": "O my God, in you I trust; let me not be put to shame; let not my enemies exult over me.",
      "M": "O my God, in you I trust; do not let me be put to shame; do not let my enemies triumph over me.",
      "T": "My God, I have put my trust in you.\nDo not let me be disgraced.\nDo not let my enemies stand over me in triumph."
    },
    "3": {
      "L": "Indeed, none who wait for you shall be put to shame; they shall be ashamed who are treacherous without cause.",
      "M": "Indeed, no one who waits for you will be put to shame; those who betray without reason will be the ones shamed.",
      "T": "No one who waits for you ends in disgrace.\nShame is reserved for those who betray without cause."
    },
    "4": {
      "L": "Make me to know your ways, O LORD; teach me your paths.",
      "M": "Make your ways known to me, O LORD; teach me your paths.",
      "T": "Show me how you move through the world, LORD.\nTeach me the routes you travel."
    },
    "5": {
      "L": "Lead me in your truth and teach me, for you are the God of my salvation; for you I wait all the day long.",
      "M": "Lead me in your faithfulness and teach me, for you are the God of my salvation; I wait for you all day long.",
      "T": "Guide me in your faithfulness—teach me its paths.\nYou are my saving God.\nAll day long I am waiting—and only for you."
    },
    "6": {
      "L": "Remember your mercy, O LORD, and your steadfast love, for they have been from of old.",
      "M": "Remember your compassion, O LORD, and your steadfast love, for they have been from everlasting.",
      "T": "Remember your compassion, LORD, and your steadfast love—\nthese have been your character from before time remembers."
    },
    "7": {
      "L": "Remember not the sins of my youth or my transgressions; according to your steadfast love remember me, for the sake of your goodness, O LORD!",
      "M": "Do not hold against me the sins of my youth or my rebellions; according to your steadfast love, remember me—for your goodness' sake, O LORD.",
      "T": "Do not remember what I was when I was young—\nthe rebellions, the failures.\nRemember me instead through the lens of your steadfast love,\nbecause of who you are, LORD."
    },
    "8": {
      "L": "Good and upright is the LORD; therefore he instructs sinners in the way.",
      "M": "The LORD is good and upright; therefore he teaches sinners the right way.",
      "T": "The LORD is good and straight—and precisely because of that,\nhe teaches those who have gone wrong how to find the road again."
    },
    "9": {
      "L": "He leads the humble in what is right and teaches the humble his way.",
      "M": "He guides the humble in justice and teaches the humble his way.",
      "T": "The lowly, the teachable—\nhe leads them in the right direction\nand shows them personally how he moves."
    },
    "10": {
      "L": "All the paths of the LORD are steadfast love and faithfulness, for those who keep his covenant and his testimonies.",
      "M": "All the LORD's paths are steadfast love and faithfulness, for those who keep his covenant and his decrees.",
      "T": "Every road the LORD walks is paved with steadfast love and faithfulness—\nand this is the lived experience of everyone who keeps his covenant."
    },
    "11": {
      "L": "For your name's sake, O LORD, pardon my guilt, for it is great.",
      "M": "For your name's sake, O LORD, forgive my guilt, for it is very great.",
      "T": "For the honor of your own name, LORD—forgive me.\nMy guilt is heavy. You know how great it is."
    },
    "12": {
      "L": "Who is the man who fears the LORD? Him will he instruct in the way that he should choose.",
      "M": "Who is the one who fears the LORD? The LORD will instruct him in the way he should take.",
      "T": "Who is the person who truly reveres the LORD?\nGod will personally show them which road to take."
    },
    "13": {
      "L": "His soul shall abide in well-being, and his offspring shall inherit the land.",
      "M": "He will dwell in prosperity, and his children will inherit the land.",
      "T": "Their life will rest in good things,\nand their descendants will have the land as their own."
    },
    "14": {
      "L": "The secret of the LORD is with those who fear him, and he makes his covenant known to them.",
      "M": "The LORD confides in those who fear him, and makes his covenant known to them.",
      "T": "The LORD lets those who revere him into his inner counsel—\nhe shares the secret of his covenant with them."
    },
    "15": {
      "L": "My eyes are ever toward the LORD, for he will pluck my feet out of the net.",
      "M": "My eyes are always toward the LORD, for he will free my feet from the trap.",
      "T": "My eyes are fixed on the LORD—only him.\nHe is the one who will pull my feet free of whatever snare is set."
    },
    "16": {
      "L": "Turn to me and be gracious to me, for I am lonely and afflicted.",
      "M": "Turn to me and be merciful to me, for I am alone and in distress.",
      "T": "Turn toward me. Show me your mercy.\nI am alone out here—and I am suffering."
    },
    "17": {
      "L": "The troubles of my heart are enlarged; bring me out of my distresses.",
      "M": "The troubles of my heart have multiplied; bring me out of my anguish.",
      "T": "The anguish inside me has been growing.\nBring me out of the tight place I am in."
    },
    "18": {
      "L": "Look upon my affliction and my trouble, and forgive all my sins.",
      "M": "Look at my affliction and my trouble, and forgive all my sins.",
      "T": "See what I am carrying—the suffering, the hardship.\nAnd forgive every sin that brought me here."
    },
    "19": {
      "L": "Consider how many are my enemies and with what violent hatred they hate me.",
      "M": "Consider how many are my foes, and how violently they hate me.",
      "T": "Look at how many there are—the ones set against me.\nTheir hatred is not mild. It is violent and relentless."
    },
    "20": {
      "L": "Oh, guard my soul and deliver me! Let me not be put to shame, for I take refuge in you.",
      "M": "Guard my soul and rescue me! Do not let me be put to shame, for I take shelter in you.",
      "T": "Keep my life safe—bring me through.\nDo not let me be humiliated.\nYou are where I have taken cover."
    },
    "21": {
      "L": "May integrity and uprightness preserve me, for I wait for you.",
      "M": "May integrity and uprightness protect me, as I wait for you.",
      "T": "Let my whole life—its honesty, its uprightness—stand as my defense,\nwhile I wait for you."
    },
    "22": {
      "L": "Redeem Israel, O God, out of all his troubles.",
      "M": "Redeem Israel, O God, from all their troubles.",
      "T": "God—redeem Israel.\nBring your whole people out of every trouble they carry."
    }
  },

  # ============================================================
  # Psalm 26 — Walk of Integrity; Petition for Vindication
  # ============================================================
  "26": {
    "1": {
      "L": "A Psalm of David. Vindicate me, O LORD, for I have walked in my integrity, and I have trusted in the LORD without wavering.",
      "M": "A Psalm of David. Vindicate me, O LORD, for I have walked in integrity and trusted in the LORD without faltering.",
      "T": "Of David.\nDeclare me innocent, LORD—I ask it.\nI have walked a straight road; I have trusted you without turning aside."
    },
    "2": {
      "L": "Examine me, O LORD, and prove me; test my heart and my kidneys.",
      "M": "Test me, O LORD, and try me; examine my heart and my inmost self.",
      "T": "Test me, LORD. Run the examination.\nLook into my heart and into my deepest self."
    },
    "3": {
      "L": "For your steadfast love is before my eyes, and I have walked in your faithfulness.",
      "M": "For your steadfast love is before my eyes, and I have conducted myself in your faithfulness.",
      "T": "Your steadfast love has been constantly in view for me.\nI have walked by the light of your faithfulness."
    },
    "4": {
      "L": "I have not sat with men of falsehood, nor do I go in with those who hide themselves.",
      "M": "I do not sit with deceitful men or associate with hypocrites.",
      "T": "I have not made my home among liars.\nI do not keep company with those who wear a mask."
    },
    "5": {
      "L": "I hate the assembly of evildoers, and I will not sit with the wicked.",
      "M": "I hate the company of evildoers and refuse to sit with the wicked.",
      "T": "The gathering of evil people—I want nothing to do with it.\nI will not take my seat among the wicked."
    },
    "6": {
      "L": "I wash my hands in innocence and go around your altar, O LORD,",
      "M": "I wash my hands in innocence and take my place at your altar, O LORD,",
      "T": "I wash my hands in innocence\nand take my place beside your altar, LORD—"
    },
    "7": {
      "L": "proclaiming thanksgiving with a loud voice and telling all your wondrous deeds.",
      "M": "lifting my voice in thanksgiving and recounting all your wonderful works.",
      "T": "my voice lifted in praise,\nand the story of everything you have done pouring out of me."
    },
    "8": {
      "L": "O LORD, I love the habitation of your house and the place where your glory dwells.",
      "M": "LORD, I love the dwelling place of your house and the place where your glory lives.",
      "T": "LORD, I love where you live—\nthis house, and especially the place where your glory makes its home."
    },
    "9": {
      "L": "Do not sweep away my soul with sinners, nor my life with bloodthirsty men,",
      "M": "Do not take away my life with sinners or with those who shed blood,",
      "T": "Do not sweep me away with people who are headed for ruin—\nwith those whose hands are soaked in violence."
    },
    "10": {
      "L": "in whose hands is wickedness and whose right hands are full of bribes.",
      "M": "in whose hands are evil schemes and whose right hands are full of bribes.",
      "T": "Their hands run with evil schemes.\nTheir right hands clutch the money that bought their verdicts."
    },
    "11": {
      "L": "But as for me, I walk in my integrity; redeem me and be gracious to me.",
      "M": "But as for me, I walk in my integrity; redeem me and show me your grace.",
      "T": "My own road is different: I walk with a whole heart.\nBuy me back from danger, LORD. Be merciful."
    },
    "12": {
      "L": "My foot stands on level ground; in the great assembly I will bless the LORD.",
      "M": "My foot stands on level ground; in the great congregation I will praise the LORD.",
      "T": "My feet are on solid, level ground.\nIn the full assembly of the people I will bless the LORD."
    }
  },

  # ============================================================
  # Psalm 27 — Light and Salvation; Confidence and Prayer
  # ============================================================
  "27": {
    "1": {
      "L": "A Psalm of David. The LORD is my light and my salvation; whom shall I fear? The LORD is the stronghold of my life; of whom shall I be afraid?",
      "M": "A Psalm of David. The LORD is my light and my salvation—whom shall I fear? The LORD is the fortress of my life—of whom shall I be afraid?",
      "T": "Of David.\nThe LORD is my light—he is my rescue.\nWho is there left to fear?\nThe LORD is the fortified wall around my life.\nWho has any power to terrify me?"
    },
    "2": {
      "L": "When evildoers assailed me to eat up my flesh—my adversaries and enemies—they stumbled and fell.",
      "M": "When evildoers came against me to devour my flesh—my adversaries and foes—they stumbled and fell.",
      "T": "When my enemies advanced to tear me apart—\nadversaries, hostile forces pressing in—\nthey tripped over themselves and went down."
    },
    "3": {
      "L": "Though an army encamp against me, my heart shall not fear; though war arise against me, yet I am confident.",
      "M": "Even if an army surrounds me, my heart will not fear; even if war breaks out against me, I will still be confident.",
      "T": "Let an entire army set up camp against me—\nmy heart is not afraid.\nLet war itself break out at my door—\nI am still sure of this."
    },
    "4": {
      "L": "One thing I have asked of the LORD, that will I seek: that I may dwell in the house of the LORD all the days of my life, to behold the beauty of the LORD and to inquire in his temple.",
      "M": "One thing I have asked of the LORD, and that I will pursue: to dwell in the house of the LORD all the days of my life, to gaze on the beauty of the LORD and to seek him in his temple.",
      "T": "One thing—I have asked it, and I keep asking—\nthat I might live inside the LORD's presence\nevery remaining day of my life:\nto look at his beauty,\nto meet with him in his temple."
    },
    "5": {
      "L": "For in the day of trouble he will hide me in his shelter; he will conceal me under the cover of his tent; he will set me high upon a rock.",
      "M": "For in the day of trouble he will hide me in his dwelling; he will conceal me under the shelter of his tent; he will set me securely on a rock.",
      "T": "Because when trouble comes he will tuck me inside his own home.\nHe will hide me in the deepest recess of his tent.\nHe will lift me up and set me on a rock too high for trouble to reach."
    },
    "6": {
      "L": "And now my head shall be lifted up above my enemies all around me, and I will offer in his tent sacrifices with shouts of joy; I will sing and make melody to the LORD.",
      "M": "And now my head will be raised above my enemies who surround me, and in his tent I will offer sacrifices with shouts of joy; I will sing and make music to the LORD.",
      "T": "Even now my head rises above the enemies encircling me.\nIn his tent I will bring offerings—shouts of joy going up with the smoke.\nI will sing. I will play music for the LORD."
    },
    "7": {
      "L": "Hear, O LORD, when I cry aloud; be gracious to me and answer me!",
      "M": "Hear, O LORD, when I cry aloud; be merciful to me and answer me.",
      "T": "LORD—hear me. I am calling out.\nShow me your grace. Answer."
    },
    "8": {
      "L": "You have said, 'Seek my face!' My heart says to you, 'Your face, LORD, do I seek.'",
      "M": "'Seek my face'—so you have spoken. My heart answers you: 'Your face, LORD, I am seeking.'",
      "T": "When you said, 'Come and find me'—\nmy heart immediately answered:\n'I am looking for your face, LORD. Only your face.'"
    },
    "9": {
      "L": "Do not hide your face from me; do not turn your servant away in anger. You have been my help; do not cast me off or forsake me, O God of my salvation.",
      "M": "Do not hide your face from me; do not turn your servant away in anger. You have been my help; do not abandon or forsake me, O God of my salvation.",
      "T": "Do not turn your face away from me.\nDo not send your servant away in anger—you, who have always been my help.\nDo not drop me. Do not walk away.\nYou are the God who saves me."
    },
    "10": {
      "L": "For my father and my mother have forsaken me, but the LORD will take me in.",
      "M": "Even if my father and mother abandon me, the LORD will receive me.",
      "T": "Even if my own father and mother should let me go—\nthe LORD gathers me in."
    },
    "11": {
      "L": "Teach me your way, O LORD, and lead me on a level path because of my enemies.",
      "M": "Teach me your way, O LORD, and lead me on a straight path because of my enemies.",
      "T": "Teach me your way, LORD.\nLead me on the level road—my enemies are watching every misstep I make."
    },
    "12": {
      "L": "Give me not up to the desire of my adversaries, for false witnesses have risen against me and breathe out violence.",
      "M": "Do not hand me over to the will of my adversaries, for false witnesses have arisen against me and breathe out cruelty.",
      "T": "Do not hand me over to what my enemies want.\nFalse witnesses have stood up against me—\nthey breathe out violence with every word they say."
    },
    "13": {
      "L": "I believe that I shall see the goodness of the LORD in the land of the living!",
      "M": "I am certain I will see the goodness of the LORD in the land of the living.",
      "T": "I would have collapsed—except that I believe this:\nI will see the goodness of the LORD here,\nin this present life, while I am still among the living."
    },
    "14": {
      "L": "Wait for the LORD! Be strong, and let your heart take courage; wait for the LORD!",
      "M": "Wait for the LORD! Be strong, and let your heart be courageous; wait for the LORD!",
      "T": "Wait for the LORD.\nDig in. Let courage take root in your heart.\nWait—keep waiting—for the LORD."
    }
  },

  # ============================================================
  # Psalm 28 — Prayer for Justice; Pivot to Praise
  # ============================================================
  "28": {
    "1": {
      "L": "A Psalm of David. To you, O LORD, I cry; my rock, do not be silent to me, lest, if you are silent to me, I become like those who go down to the pit.",
      "M": "A Psalm of David. To you, O LORD, I call; my Rock, do not be deaf to me. If you remain silent, I will be like those who go down to the grave.",
      "T": "Of David.\nI am calling out to you, LORD.\nMy Rock—do not go quiet on me.\nIf you say nothing, I am no better than those already sinking into the grave."
    },
    "2": {
      "L": "Hear the voice of my pleas for mercy when I cry to you for help, when I lift up my hands toward your innermost sanctuary.",
      "M": "Hear my cry for mercy as I call to you for help, as I lift my hands toward your Most Holy Place.",
      "T": "Hear what I am asking for—mercy—\nas I reach my hands out in prayer toward the innermost place of your house."
    },
    "3": {
      "L": "Do not drag me off with the wicked, with workers of evil, who speak peace with their neighbors while evil is in their hearts.",
      "M": "Do not sweep me away with the wicked or with evildoers, who speak peace to their neighbors while plotting evil in their hearts.",
      "T": "Do not sweep me away with those who are wicked—\nwith people who carry smooth words on their lips\nwhile their hearts are scheming harm."
    },
    "4": {
      "L": "Give to them according to their work and according to the evil of their deeds; give to them according to the work of their hands; render them their due reward.",
      "M": "Pay them back for what they have done, according to the evil of their deeds; repay them for the work of their hands; give them what they deserve.",
      "T": "Let them receive exactly what they have given.\nMatch their deeds—returned in full.\nGive them the wages their work has earned."
    },
    "5": {
      "L": "Because they do not regard the works of the LORD or the work of his hands, he will tear them down and not build them up.",
      "M": "Because they take no account of the LORD's works or of what his hands have done, he will pull them down and not rebuild them.",
      "T": "They never once noticed what God was doing in the world around them—\nnever saw his hand at work.\nSo he will dismantle them. And not rebuild."
    },
    "6": {
      "L": "Blessed be the LORD! For he has heard the voice of my pleas for mercy.",
      "M": "Praise the LORD! For he has heard my cry for mercy.",
      "T": "Let the LORD be praised!\nHe heard what I was asking him for."
    },
    "7": {
      "L": "The LORD is my strength and my shield; in him my heart trusts, and I am helped; my heart exults, and with my song I give thanks to him.",
      "M": "The LORD is my strength and my shield; my heart trusts in him and I am helped; my heart leaps for joy, and with my song I give thanks to him.",
      "T": "The LORD is my strength—my shield.\nI trusted my heart to him—and I was rescued.\nMy heart is leaping now.\nI am singing my thanks."
    },
    "8": {
      "L": "The LORD is the strength of his people; he is the saving refuge of his anointed.",
      "M": "The LORD is the strength of his people; he is the saving fortress of his anointed one.",
      "T": "The LORD is strength to his whole people—\nthe fortress of safety for the one he has anointed."
    },
    "9": {
      "L": "Oh, save your people and bless your heritage; shepherd them and carry them forever.",
      "M": "Save your people and bless your heritage; be their shepherd and carry them forever.",
      "T": "Save your people, LORD. Bless what belongs to you.\nBe their shepherd. Carry them.\nDo it forever."
    }
  },

  # ============================================================
  # Psalm 29 — The Voice of the LORD in the Storm (7× qol YHWH)
  # ============================================================
  "29": {
    "1": {
      "L": "A Psalm of David. Ascribe to the LORD, O sons of the mighty, ascribe to the LORD glory and strength.",
      "M": "A Psalm of David. Ascribe to the LORD, O heavenly beings, ascribe to the LORD glory and strength.",
      "T": "Of David.\nYou powers of the heavenly court—give to the LORD!\nGive him glory. Give him the strength that is his."
    },
    "2": {
      "L": "Ascribe to the LORD the glory due his name; worship the LORD in the splendor of holiness.",
      "M": "Give the LORD the glory due his name; worship the LORD in the splendor of his holiness.",
      "T": "Render to the LORD the honor that belongs to his name.\nWorship him—prostrate in the blazing splendor of his holiness."
    },
    "3": {
      "L": "The voice of the LORD is over the waters; the God of glory thunders, the LORD, over many waters.",
      "M": "The voice of the LORD is over the waters; the God of glory thunders—the LORD, over mighty waters.",
      "T": "Now his voice rolls over the waters.\nThe God of glory—thundering—\nthe LORD over oceans without count."
    },
    "4": {
      "L": "The voice of the LORD is powerful; the voice of the LORD is full of majesty.",
      "M": "The voice of the LORD is powerful; the voice of the LORD is majestic.",
      "T": "His voice: pure power.\nHis voice: breathtaking majesty."
    },
    "5": {
      "L": "The voice of the LORD breaks the cedars; the LORD breaks the cedars of Lebanon.",
      "M": "The voice of the LORD shatters the cedars; the LORD shatters the cedars of Lebanon.",
      "T": "His voice splits the great cedars—\nthe LORD tears apart even the cedars of Lebanon."
    },
    "6": {
      "L": "He makes Lebanon to skip like a calf, and Sirion like a young wild ox.",
      "M": "He makes Lebanon skip like a calf, and Sirion like a young wild ox.",
      "T": "Lebanon bucks like a calf at the sound.\nSirion leaps like a young bull."
    },
    "7": {
      "L": "The voice of the LORD flashes forth flames of fire.",
      "M": "The voice of the LORD strikes with flashes of lightning.",
      "T": "His voice—and the air ignites."
    },
    "8": {
      "L": "The voice of the LORD shakes the wilderness; the LORD shakes the wilderness of Kadesh.",
      "M": "The voice of the LORD shakes the wilderness; the LORD shakes the wilderness of Kadesh.",
      "T": "His voice convulses the desert—\neven the wilderness of Kadesh shudders at the sound."
    },
    "9": {
      "L": "The voice of the LORD makes the deer give birth and strips the forests bare; and in his temple all say, 'Glory!'",
      "M": "The voice of the LORD causes the deer to writhe in labor and strips the forests bare; and in his temple all cry, 'Glory!'",
      "T": "His voice sends the deer into sudden labor—\nstrips the forest down to bare wood.\nAnd in his temple, every voice: Glory!"
    },
    "10": {
      "L": "The LORD sat enthroned at the Flood; the LORD sits enthroned as King forever.",
      "M": "The LORD sat enthroned over the Flood; the LORD sits enthroned as King forever.",
      "T": "The LORD sat above the primordial Flood—sovereign over the greatest chaos the world has ever seen.\nThe LORD sits now, as he always has, enthroned as King forever."
    },
    "11": {
      "L": "May the LORD give strength to his people! May the LORD bless his people with peace!",
      "M": "The LORD gives strength to his people; the LORD blesses his people with peace.",
      "T": "The LORD gives his people the same strength he displayed in the storm.\nHe blesses them—with peace."
    }
  },

  # ============================================================
  # Psalm 30 — Song of Thanksgiving; Dedication of the House
  # ============================================================
  "30": {
    "1": {
      "L": "A Psalm. A Song for the Dedication of the Temple. Of David. I will extol you, O LORD, for you have lifted me up and have not let my enemies rejoice over me.",
      "M": "A Psalm. A Song for the Dedication of the Temple. Of David. I exalt you, O LORD, for you have lifted me up and have not let my enemies gloat over me.",
      "T": "A Song for the Dedication of the House—of David.\nI will lift you high, LORD—because you lifted me.\nYou did not let my enemies stand over me and celebrate."
    },
    "2": {
      "L": "O LORD my God, I cried to you for help, and you healed me.",
      "M": "O LORD my God, I cried to you for help, and you healed me.",
      "T": "LORD, my God—I cried out to you,\nand you healed me."
    },
    "3": {
      "L": "O LORD, you have brought up my soul from Sheol; you have kept me alive from those who go down to the pit.",
      "M": "LORD, you brought my soul up from the realm of the dead; you restored my life from among those who descend to the pit.",
      "T": "You pulled my whole self back from Sheol, LORD—\nback from the very edge of the grave."
    },
    "4": {
      "L": "Sing praises to the LORD, O you his saints, and give thanks to his holy name.",
      "M": "Sing praises to the LORD, O you his faithful ones, and give thanks to his holy name.",
      "T": "Sing praise to the LORD, all who belong to him.\nLet his holy name hear your gratitude."
    },
    "5": {
      "L": "For his anger is but for a moment, and his favor is for a lifetime; weeping may lodge for the night, but joy comes in the morning.",
      "M": "For his anger lasts only a moment, but his favor lasts a lifetime; weeping may remain through the night, but joy arrives with the morning.",
      "T": "His anger lasts only a moment—but his favor runs the whole length of a life.\nTears may move in for the night—\nbut by morning: singing."
    },
    "6": {
      "L": "As for me, I said in my prosperity, 'I shall never be moved.'",
      "M": "When I was prosperous, I said, 'I will never be shaken.'",
      "T": "In my comfortable days I said to myself:\n'Nothing will ever move me from this.'"
    },
    "7": {
      "L": "By your favor, O LORD, you made my mountain stand strong; you hid your face; I was dismayed.",
      "M": "By your favor, LORD, you had made my mountain stand firm; when you hid your face, I was terrified.",
      "T": "You, LORD, by your sheer goodwill, had made my life as solid as a mountain.\nThen you turned your face away—\nand I fell to pieces."
    },
    "8": {
      "L": "To you, O LORD, I cried, and to the Lord I pleaded for mercy:",
      "M": "To you, LORD, I called out; to the Lord I made my appeal:",
      "T": "So I called out to you, LORD—to you, my Master.\nI laid out my case:"
    },
    "9": {
      "L": "What profit is there in my blood, if I go down to the pit? Will the dust praise you? Will it tell of your faithfulness?",
      "M": "What is gained if I die and go down to the grave? Can the dust praise you? Can it proclaim your faithfulness?",
      "T": "'What exactly do you gain from my death?\nIf I go down into the grave, can dust lift its voice to you?\nCan dust testify to your faithfulness?'"
    },
    "10": {
      "L": "Hear, O LORD, and be merciful to me! O LORD, be my helper!",
      "M": "Hear me, LORD, and have mercy on me! LORD, be my helper!",
      "T": "Hear me, LORD.\nBe merciful to me.\nBe the one who helps me."
    },
    "11": {
      "L": "You have turned for me my mourning into dancing; you have loosed my sackcloth and clothed me with gladness,",
      "M": "You have turned my mourning into dancing; you have removed my sackcloth and clothed me with joy,",
      "T": "And you did it—you turned my mourning into dancing.\nYou took the mourning-cloth off me\nand wrapped me in gladness."
    },
    "12": {
      "L": "that my glory may sing praises to you and not be silent. O LORD my God, I will give thanks to you forever.",
      "M": "so that my spirit may sing your praise and not be silent. O LORD my God, I will give you thanks forever.",
      "T": "So that everything in me—my whole self—might sing to you without stopping.\nLORD, my God:\nI will thank you forever."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 25-30 written.')

if __name__ == '__main__':
    main()
