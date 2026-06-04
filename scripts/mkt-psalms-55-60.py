"""
MKT Psalms chapters 55–60 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-55-60.py

=== Overview of this unit ===

Ps 55 (23 v) — Lament of David over urban treachery and betrayal by a close friend.
    Among the most personal of the Davidic laments. The famous passage vv12–14 names
    the wound precisely: not an open enemy but a trusted companion, his equal, his "familiar
    friend" (H441 aluf, one who shares confidence), who ate at his table (patron-client
    intimacy). The poem opens with anguished prayer (vv1–3), moves to the famous escape
    fantasy — wings like a dove, flight to the wilderness (vv6–8; H3123 yonah = dove,
    the same word as the Psalm 56 superscription title) — then pivots to a civic lament
    over a corrupt city (vv9–11), the betrayal confession (vv12–14), imprecatory petition
    (vv15–16), and closes with the celebrated call-to-trust: "Cast your burden on the LORD"
    (v22). The covenant-violation of v20 uses H1285 berith (covenant), signaling that the
    betrayal is not merely personal but has a covenantal dimension. v15 invokes Sheol
    (H7585) — the realm of the dead — as the fitting destination of the treacherous.
    Structurally: opening cry (vv1–3) → terror (vv4–5) → escape wish (vv6–8) → civic
    diagnosis (vv9–11) → friend-betrayal (vv12–14) → imprecation (v15) → confidence
    (vv16–18) → God's ancient verdict (v19) → covenant-treachery (vv20–21) → benediction
    and trust (vv22–23).

Ps 56 (13 v) — Michtam of David, composed when the Philistines seized him in Gath
    (1 Sam 21:10–15). A psalm of endangered trust: the refrain "In God I trust; I will
    not fear. What can flesh/man do to me?" (vv4, 11) is the structural spine. Between
    the two refrains: description of enemies (vv5–6), brief imprecatory petition (v7),
    the tenderly intimate verse 8 ("put my tears in your bottle; are they not in your
    book?"), and the pivot-verse 9 ("on the day I call, my enemies will turn back — this
    I know: God is for me"). The musical title "Jonathelemrechokim" (H3128) = "Dove of
    the Far-off Terebinths/Oaks" — a song title, probably a melody or poetic type (the
    dove = the fugitive of Ps 55:6 and David's own situation as a refugee in Philistia).
    The psalm ends in vow-fulfillment: David already walking "before God in the light of
    life" (v13), implying rescue has begun or is certain.

Ps 57 (11 v) — Michtam, Altaschith; David in the cave (1 Sam 22 / 24). A psalm of
    sheltering trust that crescendos into praise. The key movement: refuge-cry (v1) →
    confidence in God's sovereign purpose (v2) → petition for rescue (v3) → hostile
    description (v4) → refrain: exaltation of God (v5) → reversal of the trap (v6) →
    awakened heart and music (vv7–8) → praise among the nations (v9) → ground of
    praise: vastness of steadfast love (v10) → refrain repeated (v11). The double
    refrain (vv5 and 11) frames the whole as doxological. "My heart is steadfast" (v7,
    H3559 nakun = established/fixed/prepared) — the psalmist's spiritual state is
    resolved even before the physical danger is resolved. "I will awake the dawn" (v8):
    not dawn waking the psalmist but the psalmist preceding the dawn with praise — a
    bold reversal of normal order.

Ps 58 (11 v) — Michtam, Altaschith; a prophetic-imprecatory psalm addressed to corrupt
    rulers or "gods" (vv1–2). The opening crux (H482 in v1): Hebrew אֵלֶם (elem) or
    אֵלִים (elim, "mighty ones/gods/rulers"). The LXX and most modern commentators (ESV,
    NRSV, NIV) favor "you rulers/mighty ones" — addressing either corrupt human judges
    or the divine council (cf. Ps 82). The poem diagnoses wickedness as congenital (v3 —
    from the womb), compares the wicked to a deaf cobra that blocks its ear against the
    charmer (vv4–5), then launches a series of imprecations: smash their teeth (v6),
    let them dissolve like water (v7), like a melting snail (v8), like a stillborn child
    (v8), swept away before the pot even heats (v9). The climax: when the righteous see
    justice, they will rejoice (v10), and the world will acknowledge that God judges the
    earth (v11). v9 is one of the most obscure verses in the Psalter; the thornwood /
    pots / green or ablaze image means: before your pots even feel the heat (= very
    swiftly), God sweeps them away.

Ps 59 (17 v) — Michtam, Altaschith; Saul sent men to watch David's house to kill him
    (1 Sam 19:11). Structurally built around a refrain: "They return at evening, howling
    like dogs and prowling around the city" (vv6–7 = vv14–15). The enemies are depicted
    as nocturnal predators circling in the dark, all threat and bluster. God laughs at
    them (v8). The dual endings differ: the first refrain-close asks God to bring them
    down as a lesson (vv11–13); the second refrain-close ends in personal confidence and
    praise (vv16–17). "O my Strength" (H5797 uzzi) frames the psalm at v9 and v17.
    The ending "the God who shows me steadfast love" (v17) is a doxological resolution
    of the entire pursuit-crisis.

Ps 60 (12 v) — Michtam, Shushan-eduth; a national lament following military defeat,
    from the time David fought Aram-naharaim and Aram-zobah (2 Sam 8:3; 10:6–19), while
    Joab struck 12,000 Edomites in the Valley of Salt (2 Sam 8:13; 1 Chr 18:12). The
    psalm begins with the raw experience of divine rejection (vv1–3): God has broken,
    shaken, made the land reel — their defeats are his doing. v4 pivots: God has also
    given a banner for his fearers to rally to. Then vv5–8 contain a divine oracle (God
    speaks in first person) claiming all of Israel and all surrounding nations as his
    own — a war oracle of sovereignty. vv9–12 return to petition: who leads me to Edom?
    Not the armies we trusted. Only God. The close (v12) mirrors Ps 44:5 and 108:13:
    "Through God we shall do valiantly; it is he who will tread down our foes."
    "Shushan-eduth" (H7799+H5715) = "Lily of the Testimony" — a melody or psalm type.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps) in L/M throughout. In T: "the LORD."
    Consistent with all prior Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Psalms 55–60 are within Book II of the
    Psalter (Ps 42–89), the "Elohistic Psalter," which systematically uses Elohim where
    Book I would use Yahweh. The translation preserves this naturally.

H410 (אֵל, El): "God" throughout. The shorter divine title. Appears as address in
    Ps 57:2; 58:6; 59:10; 60:1, 10.

H136 (אֲדֹנָי, Adonai): "Lord" (not LORD) in L/M/T. The divine title "Lord" (sovereign),
    distinct from the divine name Yahweh (LORD). Appears at Ps 55:9; 57:9; 59:11.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T throughout. Appears prominently at
    Ps 57:3,10; 59:10,16,17. Carries covenantal loyalty + active kindness. Consistent
    with all prior Psalms scripts.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M; contextually "soul/self/life" in T.
    In Ps 55: v18 (soul ransomed from battle), v23 (not present directly). In Ps 56: vv6,13
    (life endangered, life delivered). In Ps 57: v1 (soul takes refuge). In Ps 59: vv3
    (soul / life targeted). Rendered "soul" in L/M to preserve embodied-self usage;
    "life" or "self" selectively in T where context demands it.

H1285 (בְּרִית, berith): "covenant" in all tiers. Ps 55:20 ("he broke his covenant").
    The covenant-violation dimension of the betrayal is theologically significant.

H7585 (שְׁאוֹל, Sheol): "Sheol" in all tiers. The realm of the dead. Ps 55:15.
    Not "hell" (imports later Christian/Islamic associations); "Sheol" preserves the
    Hebrew conception of the shadowy underworld without over-specifying.

H482 (Ps 58:1, אֵלֶם or אֵלִם): Rendered "rulers" in L/M/T, following ESV/NRSV/NIV
    consensus that the word addresses powerful human judges or the divine council (cf.
    Ps 82). LXX reads "righteousness" here. KJV "congregation" reflects a variant
    reading. The address "you rulers" fits the judicial theme of the whole psalm.

H4387 (מִכְתָּם, Michtam): Retained as "Michtam" in all tiers — meaning uncertain
    (possibly "inscription/golden psalm"; Targ.: "a choice psalm"). Appears in Ps 56,
    57, 58, 59, 60 superscriptions. Consistent with all prior Psalms scripts.

H516 (אַל-תַּשְׁחֵת, Al-tashheth): "Altaschith" in L (transliterated); "Do Not Destroy"
    glossed in M/T superscriptions. This designation appears in Ps 57, 58, 59 (and
    Ps 75). The phrase means "Do not destroy/corrupt." Possibly a melody title or a
    liturgical direction.

H3128 (יוֹנַת אֵלֶם רְחֹקִים, Ps 56): "Jonathelemrechokim" in L; "Dove of the Far-off
    Oaks" in M/T. This is the song/melody title of Ps 56. The "dove" (H3123 yonah)
    resonates with Ps 55:6 ("O that I had wings like a dove!") and David's fugitive
    status in Gath.

H5715+H7799 (Ps 60, Shushan-eduth): "Shushan-eduth" in L; "Lily of the Testimony"
    in M/T. A melody or psalm-type designation. Cf. Ps 80 superscription (Shoshannim
    eduth). "Lily" suggests a melody; "testimony" may refer to the covenant testimony
    or the ark.

H7307 (רוּחַ, ruach): In Ps 55:8 ("windy storm"), this is physical wind, not the
    Spirit of God. Rendered "storm" or "tempest" per context.

=== Aspect and tense notes ===

Ps 55 — The escape-wish (vv6–8) uses cohortative imperfects: "would fly," "would
    wander," "would hasten" — all expressing desire/wish. L preserves these with
    "I would." The betrayal passage (vv12–14) uses past narrative perfects: "he
    reproached," "he magnified himself." The covenant-violation of v20 is perfect
    (completed act): "he has put forth his hand." The concluding "But I will trust"
    (v23) is imperfect of ongoing resolution.

Ps 56 — The refrain (vv4, 11) uses perfect + cohortative: "I have trusted" (perfect
    of ongoing state) + "I will not fear" (negative cohortative of resolve). "I know"
    (v9, H3045) is perfect — certainty acquired. "You have kept count" (v8) is perfect
    of divine ongoing attention.

Ps 57 — "My heart is steadfast" (v7, H3559 nakun) is a Niphal perfect passive:
    "my heart has been established/made firm." Active perfects of praise in v8–9
    (cohortatives: "I will sing," "I will give thanks"). The reversal of v6 ("they
    have fallen into it themselves") is perfect — the reversal is as certain as
    completed.

Ps 58 — Jussive/cohortative imperfects drive the imprecations (vv6–9): "Let them
    dissolve," "let them be like a snail." The congenital-wickedness description
    (vv3–5) uses Niphal and Qal perfects (timeless or proverbial past).

Ps 59 — Imperfect verbs in vv6–7 and 14–15 capture habitual/repeated action
    (enemies come back every evening). Divine laughter v8 is imperfect of continued
    action. v9 "I will keep watch" (H8104) is imperfect of resolved intention.

Ps 60 — The lament (vv1–3) uses past perfects of completed divine action ("you
    have rejected," "you have made tremble"). The divine oracle (vv6–8) uses
    cohortative: "I will divide," "I will measure out" — God's resolute first-person
    claim. The closing v12 uses imperfect: ongoing valiancy "we shall do valiantly."

=== OT echo notes ===

Ps 55:17 — "Evening and morning and at noon I cry out." The triple prayer rhythm
    anticipates Daniel 6:10 (Daniel praying three times daily toward Jerusalem) and
    the later Jewish practice of shacharit/minchah/maariv (morning/afternoon/evening
    prayer). This is not a quotation but an early liturgical pattern.

Ps 55:22 — "Cast your burden upon the LORD, and he will sustain you." Quoted by
    implication in 1 Pet 5:7 ("Cast all your anxiety on him because he cares for you").
    The Hebrew H3053 (yehab) is a hapax legomenon — "burden/lot" is unique to this verse.

Ps 56:13 — "walk before God in the light of life." The phrase "light of life" recurs
    in Job 33:30; John 8:12 (Jesus: "I am the light of the world; whoever follows me
    will not walk in darkness but will have the light of life").

Ps 57:7 — "My heart is steadfast." Paul uses a cognate idea in Phil 4:7 (the peace
    of God guarding heart and mind). The psalmic resolution of the heart before
    circumstances resolve is a pattern NT letters apply to eschatological trust.

Ps 58:6 — "O God, break the teeth in their mouths." Echoes Ps 3:7 ("you have
    broken the teeth of the wicked"). The image of divine disarmament — removing
    the fang from violence — recurs across the Psalter.

Ps 60:5 — "That your beloved ones may be delivered" (H3039 yadid = beloved). The
    divine beloved in the Psalms foreshadows the "Beloved Son" language of the NT
    (Matt 3:17). Ps 60 and 108 share vv5–12 nearly verbatim — the oracle of divine
    sovereignty over nations (Ps 108:6–13 = Ps 60:5–12).

Ps 60:6–8 — The divine oracle claiming all the territories of the land (Gilead,
    Manasseh, Ephraim, Judah, Moab, Edom, Philistia) echoes the tribal allotments
    of Joshua and looks forward to Davidic/Messianic sovereignty over a unified
    kingdom. The Moab-as-washbasin / shoe-over-Edom images signify humble service
    and ownership-claim respectively — the nations are God's household.
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
  # Psalm 55 — Lament: Betrayal by a Friend, Longing to Flee
  # ============================================================
  "55": {
    "1": {
      "L": "To the chief Musician. On stringed instruments. A Maskil of David. Give ear to my prayer, O God; and do not hide yourself from my supplication.",
      "M": "To the director of music. With stringed instruments. A Maskil of David. Give ear to my prayer, O God; do not hide yourself from my plea for mercy.",
      "T": "To the choirmaster. With stringed instruments. A Maskil of David.\nHear my prayer, God.\nDon't turn away from what I'm begging you for."
    },
    "2": {
      "L": "Attend to me and answer me; I am restless in my complaint and I moan—",
      "M": "Pay attention to me and answer me; I am troubled in my lament and I am agitated—",
      "T": "Turn toward me—answer me.\nI am churning inside this lament, moaning out loud—"
    },
    "3": {
      "L": "because of the voice of the enemy, because of the oppression of the wicked; for they bring trouble upon me, and in anger they bear a grudge against me.",
      "M": "because of the threatening voice of the enemy, the oppressive presence of the wicked; they bring evil upon me, and in anger they press hard against me.",
      "T": "—because the enemy's voice is ringing in my ears,\nbecause the wicked are bearing down on me.\nThey are loading me with trouble,\nand their anger against me is personal and fierce."
    },
    "4": {
      "L": "My heart is in anguish within me; the terrors of death have fallen upon me.",
      "M": "My heart is writhing in anguish within me; the terrors of death have fallen on me.",
      "T": "My heart is in agony.\nThe terrors of death have ambushed me."
    },
    "5": {
      "L": "Fear and trembling have come upon me, and horror has overwhelmed me.",
      "M": "Fear and trembling have overtaken me, and shuddering has covered me over.",
      "T": "Fear.\nTrembling.\nHorror—\npiling over me like a wave."
    },
    "6": {
      "L": "And I said, 'O that I had wings like a dove! I would fly away and be at rest.'",
      "M": "And I said, 'If only I had wings like a dove! I would fly away and find rest.'",
      "T": "'If only I had wings—dove's wings—\nI would fly away and settle somewhere quiet.'"
    },
    "7": {
      "L": "Lo, I would wander far away; I would lodge in the wilderness. Selah",
      "M": "Yes, I would flee far away; I would make my dwelling in the wilderness. Selah",
      "T": "I would put great distance between myself and all of this.\nI would find my rest in the wilderness.\nSelah."
    },
    "8": {
      "L": "I would hasten to find shelter from the rushing wind and tempest.",
      "M": "I would hurry to my refuge from the driving wind and the storm.",
      "T": "I would run—\nto get out of this battering wind,\nout of this tempest."
    },
    "9": {
      "L": "Destroy, O Lord, divide their tongues; for I see violence and strife in the city.",
      "M": "Confuse them, O Lord, split their tongues apart; for I see violence and contention in the city.",
      "T": "Lord, scatter them.\nMix up their communications—divide their tongues.\nI have seen what fills this city: violence, fighting."
    },
    "10": {
      "L": "Day and night they go about it on its walls; and iniquity and trouble are within it.",
      "M": "Day and night they patrol its walls; iniquity and trouble are entrenched within it.",
      "T": "Day and night they circle the walls.\nAnd inside—iniquity, misery, nothing but trouble."
    },
    "11": {
      "L": "Destruction is within it; oppression and deceit do not depart from its streets.",
      "M": "Ruin is entrenched at its center; oppression and fraud never leave its public spaces.",
      "T": "Ruin is camped in the heart of the city.\nOppression and fraud have permanent addresses there.\nThey never leave."
    },
    "12": {
      "L": "For it is not an enemy who reproaches me—then I could bear it; it is not one who hates me who magnifies himself against me—then I could hide from him.",
      "M": "For it is not an enemy who insults me—that I could endure; nor is it someone who hates me who has risen up against me—from that I could hide.",
      "T": "If it were an open enemy doing this,\nI could take it.\nIf it were someone who hated me raising himself against me,\nI could find somewhere to hide."
    },
    "13": {
      "L": "But it is you—a man, my equal, my companion, my familiar friend.",
      "M": "But it is you—a person like me, my peer, my companion, the one I confided in.",
      "T": "But it's you.\nYou—my equal.\nMy companion.\nThe one I walked with, spoke with, trusted."
    },
    "14": {
      "L": "We took sweet counsel together; within the house of God we walked in the festive company.",
      "M": "We shared deep, sweet conversation together; together we walked in God's house among the festival crowd.",
      "T": "We talked together—real conversation, the kind that goes deep.\nWe walked side by side in the crowd up to the house of God."
    },
    "15": {
      "L": "Let death come upon them; let them go down to Sheol alive; for evil is in their dwelling and in their midst.",
      "M": "Let death ambush them; let them go down to Sheol alive; for wickedness lives in their dwellings and among them.",
      "T": "Let death steal over them.\nLet them go down to Sheol—alive.\nFor they are soaked through with evil:\nin their homes and in their hearts."
    },
    "16": {
      "L": "As for me, I call upon God, and the LORD will save me.",
      "M": "As for me, I will call upon God, and the LORD will rescue me.",
      "T": "As for me—I call to God.\nThe LORD will save me."
    },
    "17": {
      "L": "Evening and morning and at noon I utter my complaint and moan; and he hears my voice.",
      "M": "Evening and morning and at noon I cry out my lament and sigh; and he hears my voice.",
      "T": "Evening, morning, and noon—\nI pour out my complaint, I moan aloud.\nAnd he hears me."
    },
    "18": {
      "L": "He redeems my soul in safety from the battle that I wage, for many are against me.",
      "M": "He ransoms me safely from the battle I am in, for they are many who oppose me.",
      "T": "He delivers me unharmed from this war I'm in.\nThey outnumber me—but he brings me through in peace."
    },
    "19": {
      "L": "God will give ear and humble them—he who is enthroned from of old, Selah—because there are no changes for them, and they do not fear God.",
      "M": "God will hear and afflict them, the one who is enthroned from of old—Selah—because they show no sign of change and have no fear of God.",
      "T": "God hears, and he will bring them low—\nhe has been enthroned since time out of mind.\nSelah.\nBecause nothing ever changes them.\nNo fear of God is in them."
    },
    "20": {
      "L": "He put forth his hands against those at peace with him; he violated his covenant.",
      "M": "He raised his hand against those who were at peace with him; he broke his covenant.",
      "T": "He turned against the very ones who trusted him.\nHe shattered the covenant between them."
    },
    "21": {
      "L": "His speech was smoother than butter, yet war was in his heart; his words were softer than oil, yet they were drawn swords.",
      "M": "His words were smoother than butter, yet war was in his heart; his speech was softer than oil, but it was all drawn swords.",
      "T": "Smooth—like butter poured out—his talk.\nBut war was behind every word.\nSofter than olive oil, his speech.\nBut all of it: unsheathed blades."
    },
    "22": {
      "L": "Cast your burden upon the LORD, and he will sustain you; he will never allow the righteous to be moved.",
      "M": "Throw your burden onto the LORD, and he will hold you up; he will never let the righteous be shaken.",
      "T": "Hand your burden over to the LORD.\nHe will carry it—he will carry you.\nHe will never let the righteous be swept away."
    },
    "23": {
      "L": "But you, O God, will bring them down to the pit of destruction; bloodthirsty and deceitful men shall not live out half their days. But I will trust in you.",
      "M": "But you, O God, will bring them down into the pit of ruin; men of bloodshed and treachery will not reach half their days. But I—I will trust in you.",
      "T": "But you, O God—\nyou will bring them down into the pit of destruction.\nViolent and deceptive people will not live out even half their days.\nBut I?\nI will trust in you."
    }
  },

  # ============================================================
  # Psalm 56 — Michtam: Trust Under Pursuit in Philistia
  # ============================================================
  "56": {
    "1": {
      "L": "To the chief Musician. Upon Jonathelemrechokim. A Michtam of David, when the Philistines seized him in Gath. Be gracious to me, O God, for man tramples on me; all day long he wages war against me, oppressing me.",
      "M": "To the director of music. To the tune 'Dove of the Far-off Oaks.' A Michtam of David, when the Philistines had seized him in Gath. Be merciful to me, O God, for men are trampling on me; all day long they fight and press against me.",
      "T": "To the choirmaster. To the tune 'Dove of the Far-off Oaks.' A Michtam of David, when the Philistines seized him in Gath.\nGod, be merciful to me—\nthey are trampling me underfoot all day long,\nfighting against me without stopping."
    },
    "2": {
      "L": "My enemies trample on me all day long, for many attack me with arrogance.",
      "M": "My enemies trample on me all day long, for many are arrayed against me proudly.",
      "T": "My enemies are all over me, day after day.\nThere are so many of them, and their pride drives the attack."
    },
    "3": {
      "L": "In the day I am afraid I will trust in you.",
      "M": "When I am afraid, I will put my trust in you.",
      "T": "The moment fear hits—\nI choose to trust you."
    },
    "4": {
      "L": "In God, whose word I praise, in God I trust; I will not fear. What can flesh do to me?",
      "M": "In God—whose word I praise—in God I trust; I will not be afraid. What can a mere human being do to me?",
      "T": "In God—I praise his word.\nIn God—I trust.\nI will not be afraid.\nWhat, in the end, can a mortal do to me?"
    },
    "5": {
      "L": "All day long they twist my words; all their thoughts are against me for harm.",
      "M": "All day long they distort my words; all their scheming is against me for evil.",
      "T": "Every day they misrepresent my words, twist them.\nEvery thought in their heads about me is bent toward my destruction."
    },
    "6": {
      "L": "They stir up strife, they lurk, they mark my steps, as they lie in wait for my life.",
      "M": "They gather themselves to stir up trouble, they lie in ambush, they track my steps as they wait to take my life.",
      "T": "They huddle together to plot.\nThey crouch in hiding.\nThey track every step I take,\nwaiting for their moment to take my life."
    },
    "7": {
      "L": "For iniquity—shall they escape? In your anger cast down the peoples, O God!",
      "M": "For their crime, should they escape? In wrath cast down the peoples, O God!",
      "T": "Should they just get away with it?\nNo—in your anger, God, bring down the nations."
    },
    "8": {
      "L": "You have counted my wanderings; put my tears in your bottle. Are they not in your book?",
      "M": "You have recorded my restless wandering; store my tears in your wineskin—are they not written in your book?",
      "T": "You have kept track of all my wandering.\nEvery tear I've wept—collect them.\nHave you not written them all down in your book?"
    },
    "9": {
      "L": "On the day I call, then my enemies will turn back; this I know, that God is for me.",
      "M": "On the day I call out, my enemies will turn back; this I know: God is on my side.",
      "T": "The day I call out—that is the day my enemies retreat.\nThis I know with certainty:\nGod is for me."
    },
    "10": {
      "L": "In God, whose word I praise, in the LORD, whose word I praise,",
      "M": "In God—whose word I praise—in the LORD—whose word I praise—",
      "T": "In God—whose word I celebrate.\nIn the LORD—whose word I celebrate."
    },
    "11": {
      "L": "in God I trust; I will not fear. What can man do to me?",
      "M": "in God I trust; I will not be afraid. What can human beings do to me?",
      "T": "In God I trust.\nI will not be afraid.\nWhat can any human being ultimately do to me?"
    },
    "12": {
      "L": "Upon me, O God, are your vows; I will render thank offerings to you.",
      "M": "I have made vows to you, O God, and I will fulfill them; I will offer you my thanksgiving.",
      "T": "God, I owe you this:\nvows I made, I will keep.\nI will bring thanksgiving offerings to you."
    },
    "13": {
      "L": "For you have delivered my soul from death—yes, my feet from stumbling—that I may walk before God in the light of life.",
      "M": "For you have saved my life from death, and my feet from stumbling, so that I may walk before God in the light that belongs to the living.",
      "T": "You have delivered my whole self from death.\nYou kept my feet from slipping.\nNow I walk before God—\nin the light that only the living can see."
    }
  },

  # ============================================================
  # Psalm 57 — Michtam: Sheltering Trust in the Cave
  # ============================================================
  "57": {
    "1": {
      "L": "To the chief Musician. Altaschith. A Michtam of David, when he fled from Saul in the cave. Be merciful to me, O God, be merciful to me, for my soul takes refuge in you; in the shadow of your wings I will take refuge, until these destroying calamities pass by.",
      "M": "To the director of music. 'Do Not Destroy.' A Michtam of David, when he fled from Saul in the cave. Be merciful to me, O God, be merciful to me, for my soul takes refuge in you; in the shadow of your wings I will take shelter until the storms of destruction pass.",
      "T": "To the choirmaster. 'Do Not Destroy.' A Michtam of David, when he fled from Saul into the cave.\nBe merciful—God, be merciful—\nmy whole self runs to you for shelter.\nI hide in the shadow of your wings\nuntil the disasters that are hunting me sweep past."
    },
    "2": {
      "L": "I cry out to God Most High, to God who accomplishes all things for me.",
      "M": "I cry out to God Most High, to God who carries out his purpose for me.",
      "T": "I am crying out to the God who is most high above all—\nthe God who brings to completion everything he intends for me."
    },
    "3": {
      "L": "He will send from heaven and save me; he will reproach the one who tramples on me. Selah. God will send his steadfast love and his faithfulness.",
      "M": "He will send from heaven and rescue me; he will rebuke the one who tramples me. Selah. God will send his steadfast love and his faithfulness.",
      "T": "He will reach down from heaven and rescue me.\nHe will shame the one who is crushing me.\nSelah.\nGod dispatches his steadfast love.\nGod dispatches his faithfulness—both of them coming toward me."
    },
    "4": {
      "L": "My soul is in the midst of lions; I lie down amid those who are ablaze—sons of men whose teeth are spears and arrows, and whose tongue is a sharp sword.",
      "M": "My soul is surrounded by lions; I must lie down among those who breathe fire—human beings whose teeth are spears and arrows and whose tongue is a sharp sword.",
      "T": "I am lying down in the middle of lions—\npeople who are all fire and fury,\nwhose teeth are spears and arrows,\nwhose tongues are blades."
    },
    "5": {
      "L": "Be exalted, O God, above the heavens; let your glory be over all the earth!",
      "M": "Be exalted above the heavens, O God; let your glory be over all the earth!",
      "T": "Rise up, God—\nhigher than the heavens.\nLet your glory be spread across the whole earth."
    },
    "6": {
      "L": "They prepared a net for my feet; my soul was bowed down; they dug a pit before me; they have fallen into it themselves. Selah",
      "M": "They spread a net for my feet; my soul was beaten down; they dug a pit in my path, but they themselves have fallen into it. Selah",
      "T": "They stretched a net across my path.\nMy soul was crushed to the ground.\nThey dug a pit right in front of me—\nand fell into it themselves.\nSelah."
    },
    "7": {
      "L": "My heart is steadfast, O God, my heart is steadfast; I will sing and make music!",
      "M": "My heart is fixed, O God, my heart is firm; I will sing and make melody!",
      "T": "My heart is set firm—God, my heart is set firm.\nI will sing.\nI will make music."
    },
    "8": {
      "L": "Awake, my glory! Awake, O harp and lyre! I will awaken the dawn!",
      "M": "Awake, my honor! Awake, harp and lyre! I will rouse the dawn!",
      "T": "Wake up, everything in me that can glorify God!\nWake up, harp! Wake up, lyre!\nI will be up before the dawn—I will wake it."
    },
    "9": {
      "L": "I will give thanks to you, O Lord, among the peoples; I will sing praises to you among the nations.",
      "M": "I will give you thanks, O Lord, among the peoples; I will sing your praise among the nations.",
      "T": "I will thank you in front of all peoples, Lord.\nI will sing praise to you among the nations."
    },
    "10": {
      "L": "For your steadfast love is great to the heavens, and your faithfulness to the clouds.",
      "M": "For your steadfast love reaches to the heavens, your faithfulness to the skies.",
      "T": "Your steadfast love is so vast it reaches to the heavens.\nYour faithfulness stretches to the clouds."
    },
    "11": {
      "L": "Be exalted, O God, above the heavens; let your glory be over all the earth!",
      "M": "Be exalted above the heavens, O God; let your glory be over all the earth!",
      "T": "Rise up, God—\nhigher than the heavens.\nLet your glory be spread across the whole earth."
    }
  },

  # ============================================================
  # Psalm 58 — Michtam: Against Unjust Rulers; God Judges the Earth
  # ============================================================
  "58": {
    "1": {
      "L": "To the chief Musician. Altaschith. A Michtam of David. Do you indeed speak righteousness, O rulers? Do you judge the sons of men with equity?",
      "M": "To the director of music. 'Do Not Destroy.' A Michtam of David. Do you indeed decree what is right, you rulers? Do you judge human beings with justice?",
      "T": "To the choirmaster. 'Do Not Destroy.' A Michtam of David.\nA question for those who hold power:\nDo you actually deliver what is right?\nDo you judge human beings with fairness?"
    },
    "2": {
      "L": "No, in your heart you work iniquity; in the land you weigh out the violence of your hands.",
      "M": "No—in your heart you devise wrongs; your hands administer violence throughout the land.",
      "T": "No—your hearts are busy designing evil.\nYour hands distribute violence across the earth."
    },
    "3": {
      "L": "The wicked are estranged from the womb; they go astray from birth, speaking lies.",
      "M": "The wicked are alienated from the womb; from their very birth they go astray, speaking lies.",
      "T": "The wicked are off track from the moment they're born—\nstrangers to what is right from their mother's womb,\ngoing astray from the very start, speaking lies."
    },
    "4": {
      "L": "Their poison is like the poison of a serpent; they are like the deaf asp that stops its ear,",
      "M": "Their venom is like the venom of a snake; they are like the deaf cobra that blocks its ear,",
      "T": "Their poison—serpent-venom.\nLike a deaf adder that has blocked its own ear—"
    },
    "5": {
      "L": "which does not hear the voice of charmers, however skillful the enchanter.",
      "M": "that will not listen to the voice of those who charm, no matter how skillfully they do it.",
      "T": "—it will not hear the snake-charmer's song,\nno matter how cleverly he plays."
    },
    "6": {
      "L": "O God, break the teeth in their mouths; knock out the great teeth of the young lions, O LORD.",
      "M": "Smash their teeth in their mouths, O God; tear out the fangs of the young lions, O LORD!",
      "T": "God—knock out their teeth.\nLORD—pull the fangs from these lion cubs.\nDisarm them completely."
    },
    "7": {
      "L": "Let them dissolve like water that runs away; when he aims his arrows, let them be as if cut off.",
      "M": "Let them drain away like water flowing downhill; when they draw their bows, let their arrows fall harmless.",
      "T": "Let them drain away like water running off into nothing.\nWhen they draw their arrows, let the arrows go nowhere."
    },
    "8": {
      "L": "Let them be like the snail that melts away, like a woman's miscarriage that never sees the sun.",
      "M": "Let them be like a snail that dissolves as it goes, like a stillborn child that never sees the light of the sun.",
      "T": "Let them melt like a snail leaving its trail of slime.\nLike a baby born dead who never opened its eyes to sunlight."
    },
    "9": {
      "L": "Before your pots can feel the heat of thorns—whether green or burning—he will sweep them away.",
      "M": "Before your cooking pots have felt the heat of the thornwood—both green and dry—he will whirl them away.",
      "T": "Before your pots even feel the thornwood burning beneath them—\ngreenwood and dry wood alike—\nhe will sweep them away like a whirlwind."
    },
    "10": {
      "L": "The righteous will rejoice when he sees the vengeance; he will bathe his feet in the blood of the wicked.",
      "M": "The righteous will rejoice when they see justice carried out; they will wash their feet in the blood of the wicked.",
      "T": "The righteous will look up and rejoice\nwhen they see justice done at last.\nThey will step through the ruin of the wicked."
    },
    "11": {
      "L": "And men will say, 'Surely there is a reward for the righteous; surely there is a God who judges on earth.'",
      "M": "Then people will say, 'There really is a reward for the righteous; truly there is a God who judges the earth.'",
      "T": "And then everyone will say it:\n'There is, after all, a reward for doing what is right.\nThere is, after all, a God who judges the earth.'"
    }
  },

  # ============================================================
  # Psalm 59 — Michtam: Surrounded by Enemies; God is My Fortress
  # ============================================================
  "59": {
    "1": {
      "L": "To the chief Musician. Altaschith. A Michtam of David, when Saul sent men to watch the house in order to kill him. Deliver me from my enemies, O my God; protect me from those who rise up against me.",
      "M": "To the director of music. 'Do Not Destroy.' A Michtam of David, when Saul sent men to watch the house to kill him. Rescue me from my enemies, O my God; set me beyond the reach of those who rise up against me.",
      "T": "To the choirmaster. 'Do Not Destroy.' A Michtam of David, when Saul sent men to watch his house to kill him.\nGod—rescue me from my enemies.\nLift me up out of reach of those who are rising against me."
    },
    "2": {
      "L": "Deliver me from those who work iniquity, and save me from bloodthirsty men.",
      "M": "Rescue me from those who do evil, and save me from men who want my blood.",
      "T": "Deliver me from evil workers.\nSave me from violent men who want me dead."
    },
    "3": {
      "L": "For behold, they lie in wait for my life; the strong ones gather against me—not for my transgression or my sin, O LORD.",
      "M": "For see—they lie in ambush for my life; fierce men are gathering against me—not for any offense or sin of mine, LORD.",
      "T": "Look—they're crouched in ambush, waiting to take my life.\nPowerful men have assembled against me.\nAnd I haven't done anything wrong, LORD.\nNo transgression. No sin."
    },
    "4": {
      "L": "Without my fault, they run and prepare; awake, come to my aid and see!",
      "M": "For no fault of mine they have mobilized against me. Arouse yourself, come to meet me, and look!",
      "T": "Without any fault of mine they are up and running—ready to strike.\nWake up and come, LORD.\nLook at what is happening here."
    },
    "5": {
      "L": "You, O LORD God of hosts, God of Israel—awake to punish all the nations; be not merciful to any who treacherously do iniquity. Selah",
      "M": "You are the LORD God of hosts, the God of Israel—rouse yourself to punish all the nations; show no mercy to those who commit treason with evil intent. Selah",
      "T": "You, LORD of heavenly armies—you are Israel's God.\nWake up and deal with all the nations.\nShow no mercy to any of those who plot evil in treachery.\nSelah."
    },
    "6": {
      "L": "They return at evening; they howl like dogs and go around the city.",
      "M": "They return each evening, howling like dogs and circling around the city.",
      "T": "Every evening they come back—\nhowling like dogs,\ncircling the city."
    },
    "7": {
      "L": "Behold, they belch with their mouths; swords are in their lips—for who, they say, will hear?",
      "M": "Listen—they pour out venom with their mouths; their lips are full of swords, for they think, 'Who is going to hear?'",
      "T": "Their mouths spew poison—words like drawn swords on their lips.\nAnd they think no one is listening:\n'Who will hear us?'"
    },
    "8": {
      "L": "But you, O LORD, laugh at them; you hold all the nations in derision.",
      "M": "But you, LORD, laugh at them; you scoff at all the nations.",
      "T": "But you, LORD—you are laughing at them.\nAll the nations—you hold them in contempt."
    },
    "9": {
      "L": "O my Strength, I will watch for you; for God is my stronghold.",
      "M": "O my Strength, I will wait on you; for God is my fortress.",
      "T": "You are my Strength—I will keep watch for you.\nGod, you are the fortress I live in."
    },
    "10": {
      "L": "My God in his steadfast love will come to meet me; God will let me look on those who watch for me.",
      "M": "The God of my steadfast love will come ahead of me; God will let me look in triumph on my enemies.",
      "T": "The God of steadfast love will come out to meet me.\nGod himself will let me see my enemies brought low."
    },
    "11": {
      "L": "Do not kill them, lest my people forget; shake them by your power and bring them down, O Lord our shield.",
      "M": "Do not kill them, so my people will not forget; bring them down by your power and humble them, O Lord our shield!",
      "T": "Don't destroy them all at once—\nmy people might forget what they witnessed.\nMake them stagger.\nBring them down in full view.\nLord, you are our shield."
    },
    "12": {
      "L": "For the sin of their mouth, the word of their lips—let them be caught in their pride. For the cursing and lying that they speak,",
      "M": "For the sin of their mouths and the words of their lips, let them be ensnared in their own pride. For the cursing and deception that they utter,",
      "T": "Let their words be the trap that catches them.\nTheir pride—the very pride in their mouths—let it be what brings them down.\nFor the cursing.\nFor the lies."
    },
    "13": {
      "L": "Consume them in wrath; consume them till they are no more; and let them know that God rules in Jacob to the ends of the earth. Selah",
      "M": "Consume them in your wrath; consume them until they are no more, so that people may know that God rules over Jacob to the ends of the earth. Selah",
      "T": "Consume them in your anger.\nConsume them until nothing remains.\nLet the whole world see:\nGod rules in Jacob.\nHis authority reaches to the ends of the earth.\nSelah."
    },
    "14": {
      "L": "And they return at evening; they howl like dogs and go around the city.",
      "M": "They return each evening, howling like dogs and circling the city.",
      "T": "Evening comes around again.\nThey come back like dogs, howling.\nCircling the city."
    },
    "15": {
      "L": "They wander about for food; and if not satisfied, they will growl.",
      "M": "They roam around in search of food; they growl when they are not satisfied.",
      "T": "They prowl for food.\nIf they don't find enough, they snarl."
    },
    "16": {
      "L": "But I will sing of your strength; I will sing aloud of your steadfast love in the morning; for you have been to me a fortress and a place of refuge in the day of my distress.",
      "M": "But I will sing of your strength; I will sing aloud of your steadfast love in the morning; for you have been my fortress and my place of refuge in my day of distress.",
      "T": "But I will sing of your strength.\nIn the morning I will sing aloud of your steadfast love.\nYou have been my fortress, my shelter—\nright there in the day I needed it most."
    },
    "17": {
      "L": "O my Strength, I will sing praises to you; for God is my stronghold, the God of my steadfast love.",
      "M": "O my Strength, I will sing praise to you; for God is my fortress, the God who shows me steadfast love.",
      "T": "My Strength—I will sing to you.\nGod, you are my fortress.\nYou are the God who pours steadfast love over me."
    }
  },

  # ============================================================
  # Psalm 60 — Michtam: National Lament and Divine War Oracle
  # ============================================================
  "60": {
    "1": {
      "L": "To the chief Musician. Upon Shushan-eduth. A Michtam of David, to teach; when he strove with Aram-naharaim and Aram-zobah, and Joab returned and struck twelve thousand Edomites in the Valley of Salt. O God, you have rejected us and broken us; you have been angry; restore us now.",
      "M": "To the director of music. 'Lily of the Testimony.' A teaching Michtam of David; from when he fought Aram-naharaim and Aram-zobah, while Joab returned and struck down twelve thousand Edomites in the Valley of Salt. O God, you have rejected us and broken our defenses; you have been angry—restore us!",
      "T": "To the choirmaster. 'Lily of the Testimony.' A teaching Michtam of David, from the time he fought Aram-naharaim and Aram-zobah, while Joab was south striking twelve thousand Edomites in the Valley of Salt.\nO God—you have turned away from us.\nYou broke us.\nYou were angry.\nNow come back—restore us."
    },
    "2": {
      "L": "You have made the earth tremble; you have broken it open; repair its breaches, for it totters.",
      "M": "You have made the earth shake; you have cracked it open; heal its fractures, for it is collapsing.",
      "T": "You shook the ground beneath us.\nYou split the land apart.\nRepair the fractures—it is breaking down."
    },
    "3": {
      "L": "You have shown your people hard things; you have made us drink the wine of staggering.",
      "M": "You have put your people through severe trials; you have made us drink disorienting wine.",
      "T": "You have taken your people through hard, crushing things.\nYou handed us a cup of reeling wine—\nwe could not walk straight."
    },
    "4": {
      "L": "You have given a banner to those who fear you, that it may be raised up on account of truth. Selah",
      "M": "You have set up a banner for those who fear you, for them to rally to in the face of the enemy's bow. Selah",
      "T": "You raised a flag for those who fear you—\na rallying point,\na place to run to when the arrows are flying.\nSelah."
    },
    "5": {
      "L": "That your beloved ones may be delivered, save with your right hand and answer us.",
      "M": "Save your dear ones—rescue them by your right hand, and answer our prayer.",
      "T": "Deliver those you love, God.\nSave us with your own right hand.\nAnswer us."
    },
    "6": {
      "L": "God has spoken in his holiness: 'I will exult; I will divide up Shechem and measure out the Valley of Succoth.'",
      "M": "God has spoken in his holiness: 'I will triumph; I will divide up Shechem and portion out the Valley of Succoth.'",
      "T": "God has spoken from his sanctuary—I believe it:\n'I will triumph and claim this land as mine.\nI will divide Shechem.\nI will apportion the Valley of Succoth.'"
    },
    "7": {
      "L": "'Gilead is mine, and Manasseh is mine; Ephraim is the protection of my head; Judah is my lawgiver.'",
      "M": "'Gilead is mine, Manasseh is mine; Ephraim is my helmet; Judah is my scepter.'",
      "T": "'Gilead belongs to me. So does Manasseh.\nEphraim is the helmet on my head.\nJudah is the rod of my rule.'"
    },
    "8": {
      "L": "'Moab is my washpot; over Edom I cast my sandal; over Philistia I shout in triumph.'",
      "M": "'Moab is my washbasin; over Edom I throw my sandal; over Philistia I shout in triumph.'",
      "T": "'Moab is a washbasin—fit for washing feet.\nI toss my sandal over Edom like a man claiming what is his.\nOver Philistia I raise my victory shout.'"
    },
    "9": {
      "L": "Who will bring me to the fortified city? Who will lead me to Edom?",
      "M": "Who will bring me into the fortified city? Who will guide me all the way to Edom?",
      "T": "But who will take me into the fortress?\nWho will lead me into Edom?"
    },
    "10": {
      "L": "Is it not you, O God, who have rejected us? And will you not go out, O God, with our armies?",
      "M": "Have you not rejected us, O God? You no longer go out, God, with our armies.",
      "T": "God—it is you who turned us away.\nYou stopped marching out with our armies."
    },
    "11": {
      "L": "Give us help from trouble, for the help of man is worthless.",
      "M": "Give us help against the enemy, for human deliverance is worthless.",
      "T": "Give us real help against the enemy.\nHuman rescue amounts to nothing."
    },
    "12": {
      "L": "Through God we shall do valiantly; it is he who will tread down our enemies.",
      "M": "Through God we will do great deeds; he himself will crush our enemies.",
      "T": "Through God—we will act with power.\nHe will be the one who tramples our enemies down."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 55–60 written.')

if __name__ == '__main__':
    main()
