"""
MKT Psalms chapters 61–66 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-61-66.py

=== Overview of this unit ===

Ps 61 — Prayer from the Ends of the Earth; Royal Intercession (8 verses):
         A Psalm of David upon Neginah (stringed instruments). Opens with a plea
         from a place of remoteness or exile ("from the end of the earth"), seeking
         refuge in the rock that is higher than the psalmist. The middle verses (vv5–7)
         shift to prayer for the king's longevity and covenant guardians (steadfast love
         and faithfulness), likely the Davidic king — possibly David speaking about
         himself in the third person, or a court poet interceding for the king.
         Closes with a resolution to praise.

Ps 62 — God Alone; Waiting in Silence (12 verses):
         A Psalm of David, to Jeduthun (a leading Levitical musician). Famous for
         the exclusive particle אַךְ (akh, "truly/only/alone") appearing at vv1,2,4,5,6
         and for the root דּוּמִיָּה (dumiyah, "silence/stillness") as a spiritual posture.
         The refrain structure (v2 ≈ v6) and the double "God has spoken once; twice
         I have heard" wisdom form (vv11–12) are distinctive. Contrasts God's
         immovable reliability with the vanity of human power.

Ps 63 — Thirsting for God in the Wilderness (11 verses):
         A Psalm of David, written when he was in the wilderness of Judah. One of the
         most emotionally intense personal psalms: longing, thirst, physical depletion,
         night meditation, shadow-of-the-wings refuge, and confident vindication.
         H2617 (chesed, steadfast love) appears in v3, the pivot verse: "your steadfast
         love is better than life." Concludes with confident judgment on enemies.

Ps 64 — Plot and Reversal; The Tongue as Weapon (10 verses):
         A Psalm of David, to the chief Musician. An imprecatory prayer structured
         around a sharp reversal: the wicked who shoot with their tongues (vv3–6)
         are themselves shot down by God's arrow (v7); their own tongues become
         their undoing (v8). The psalm ends with a call for universal reflection on
         God's justice (v9) and rejoicing by the righteous (v10).

Ps 65 — Harvest Hymn; Praise for Creation and Providence (13 verses):
         A Psalm and Song of David, to the chief Musician. Moves from the sanctuary
         (vv1–4, forgiveness and priestly access) to the cosmos (vv5–7, God the
         Creator of mountains and seas) to agricultural abundance (vv9–13, the
         watered earth, the crowned year). The Hebrew of v1a (דּוּמִיָּה תְהִלָּה לְךָ)
         is discussed in term decisions below.

Ps 66 — Universal Call to Praise; Personal Testimony (20 verses):
         A Song or Psalm, to the chief Musician (no Davidic attribution in the MT).
         Begins as a community psalm summoning all nations to praise (vv1–7), moves
         to Israel's corporate testimony of deliverance through fire and water (vv8–12),
         then shifts dramatically to first-person singular personal vow and testimony
         (vv13–20). The shift from "we" to "I" at v13 is intentional and significant.
         Exodus echoes: v6 ("He turned the sea into dry land") = Red Sea and the Jordan.

=== Superscriptions ===

Following the convention established in PSA-1 through PSA-8, superscription text is
merged into v1 of each psalm, separated from the verse body by a blank line in T tier.

Ps 63 has no "chief Musician" notation in the MT superscription — just the historical
attribution ("when he was in the wilderness of Judah"). No performance term is given.

Ps 66 has no Davidic attribution — MT reads "to the chief Musician, a Song or Psalm"
only. L/M reflect this; T keeps it implicit.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M throughout. T tier: "the LORD." These psalms are
      in the Elohistic Psalter (Ps 42–83); YHWH appears explicitly at Ps 62:12 (where
      MT has Adonai, H136, not YHWH — see below), Ps 64:10, Ps 65:1 (implied),
      Ps 66:18 (Adonai). No shift to "Yahweh" — no prior PSA script made that move.

H430  (אֱלֹהִים, Elohim): "God" in all tiers. Dominant divine address throughout.

H136  (אֲדֹנָי, Adonai): Rendered "Lord" (capital L only, not small-caps LORD) in all
      tiers. Appears explicitly at Ps 62:12 and Ps 66:18. Adonai is the reverential
      address "my Lord/Master" and is textually distinct from YHWH.

H2617 (חֶסֶד, hesed): "steadfast love" in all tiers — MKT standard. Appears at
      Ps 62:12; Ps 63:3; Ps 66:20. Ps 63:3's "lovingkindness" in the interlinear
      surface is replaced with "steadfast love" per MKT convention.

H5315 (נֶפֶשׁ, nefesh, "soul"): "soul" in L/M. T varies: at Ps 62:1 rendered "soul"
      to preserve the meditation posture ("my soul waits in silence"); at Ps 63:1
      rendered as "soul" (thirst idiom requires it); at Ps 66:16 "for my soul" =
      "for me" in M/T to avoid awkward English.

H5542 (סֶלָה, selah): Retained as "Selah" in all tiers, appended to verse end.
      Appears at: Ps 62:4; Ps 62:8; Ps 66:4; Ps 66:7; Ps 66:15.

דּוּמִיָּה (dumiyah, "silence/stillness"): Key word in Ps 62:1,5 and Ps 65:1.
      - Ps 62:1,5: "waiteth in silence" (L), "waits in silence" / "Be still" (M/T)
        — the root conveys not passive waiting but an active, disciplined quieting of
        oneself before God while trusting.
      - Ps 65:1: Rendered "Praise awaits you in silence" (M); L preserves the
        traditional "Praise waiteth"; T: "even our silence becomes praise to you."
        The Hebrew is compressed: דּוּמִיָּה תְהִלָּה לְךָ = "silence [is] praise to you."

H4581 (מָעוֹז, ma'oz, "stronghold/fortress"): "stronghold" in L; "fortress" in M/T.
      Appears at Ps 61:3. Carries both the structural-defense and military-refuge sense.

H5703 (עַד, ad, "unto/for ever"): "for ever" in L/M; "forever" in T throughout.
      No shift from prior scripts.

H530  (אֱמוּנָה, emunah, "faithfulness/truth"): "faithfulness" in all tiers at Ps 61:7.
      The companion of hesed in the covenant pair (steadfast love + faithfulness).

H3627 (כְּלִי, keli): Not contested here; "instrument/vessel" as needed.

H7307 (רוּחַ, ruach, not appearing here): No occurrence in these psalms.

אַךְ (akh, "truly/only/surely/alone"): The exclusive particle in Ps 62. Rendered
      "truly" in L to stay close to the particle; "alone" in M/T to capture the
      exclusive trust motif ("in God alone," "for God alone").

=== OT echoes and NT connections ===

- Ps 61:5 "heritage of those who fear your name" → 1 Pet 3:9 (inheritance motif).
- Ps 62:12 "thou renderest to every man according to his work" → Matt 16:27; Rom 2:6;
  Rev 22:12 — the divine retribution formula is a recurring NT citation.
- Ps 63:3 "your steadfast love is better than life" — foundational to NT understanding
  of agape as surpassing all earthly goods.
- Ps 64:7–8 reversal pattern (plotters shot by God's arrow; tongues become their ruin)
  → Rev 19:21; James 3 (the tongue as weapon that rebounds on its wielder).
- Ps 65:4 "blessed is the one you choose and bring near" → Eph 1:4; John 6:37,44 —
  divine election and access to the sanctuary is NT background to chosenness language.
- Ps 66:6 "He turned the sea into dry land" = Exodus 14 (Red Sea) / Joshua 3 (Jordan)
  — the dual exodus memory is compressed into one line.
- Ps 66:10 "thou hast tried us as silver is tried" → 1 Pet 1:7 (faith refined like gold
  through fire).

=== Aspect and tense notes ===

Ps 61: Imperative mood (vv1,3,7) and cohortative (v8) predominate. The shift to
descriptive perfects in vv3,5 ("you have been," "you have heard") grounds the
petition in past covenant experience.

Ps 62: Present-tense rendering preferred throughout for the timeless trust statements.
Hebrew imperfects in the refrain (v2,6) express ongoing state: "I will not be greatly
shaken" = the state is ongoing, not a future prediction.

Ps 63: Imperfects expressing ongoing longing (v1–5) translated as present tense.
Perfect verbs in vv3,7 ("your steadfast love is better than life," "you have been
my help") assert completed covenant experience that grounds present confidence.

Ps 65: The harvest description (vv9–13) uses perfects of narrative experience
(what God characteristically does) rendered with English simple present to convey
timeless/habitual action.

Ps 66: Perfects in the historical recital (vv6,7,10,12) rendered with English simple
past ("he turned," "he ruleth," "thou hast proved") to anchor the memory as specific
accomplished events. The personal testimony section (vv13–20) continues in past tense
except for the vow statements (vv13,16) which are present-going-to-future.
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
  "61": {
    "1": {
      "L": "To the chief Musician upon Neginah, A Psalm of David. Hear my cry, O God; attend unto my prayer.",
      "M": "To the choirmaster, on stringed instruments. A Psalm of David. Hear my cry, O God; listen to my prayer.",
      "T": "To the worship leader, for stringed instruments. A Psalm of David.\n\nHear my cry, O God;\nlisten to my prayer."
    },
    "2": {
      "L": "From the end of the earth will I cry unto thee, when my heart is overwhelmed; lead me to the rock that is higher than I.",
      "M": "From the ends of the earth I call out to you when my heart grows faint; lead me to the rock that is higher than I.",
      "T": "From the far ends of the earth I call out to you\nwhen my heart is ready to give way —\nlead me to the rock that towers above me."
    },
    "3": {
      "L": "For thou hast been a shelter for me, and a strong tower from the enemy.",
      "M": "For you have been a shelter for me, a strong tower against the enemy.",
      "T": "You have always been my shelter,\na tower of strength against the enemy."
    },
    "4": {
      "L": "I will abide in thy tabernacle for ever; I will take refuge in the covert of thy wings. Selah.",
      "M": "I will dwell in your tent forever; I will take refuge under the shelter of your wings. Selah.",
      "T": "Let me dwell in your tent forever,\nsafe beneath the shelter of your wings. Selah."
    },
    "5": {
      "L": "For thou, O God, hast heard my vows; thou hast given me the heritage of those that fear thy name.",
      "M": "For you, O God, have heard my vows; you have given me the inheritance of those who fear your name.",
      "T": "You have heard my vows, O God;\nyou have given me the inheritance\nthat belongs to all who revere your name."
    },
    "6": {
      "L": "Thou wilt prolong the king's life; and his years as many generations.",
      "M": "You will extend the king's days; his years shall span many generations.",
      "T": "Add day upon day to the king's life;\nlet his years extend through generation after generation."
    },
    "7": {
      "L": "He shall abide before God for ever; O prepare steadfast love and faithfulness to preserve him.",
      "M": "May he dwell before God forever; appoint steadfast love and faithfulness to guard him.",
      "T": "Let him dwell in God's presence forever;\nappoint steadfast love and faithfulness\nto be his constant guardians."
    },
    "8": {
      "L": "So will I sing praise unto thy name for ever, that I may daily perform my vows.",
      "M": "So I will sing praise to your name forever, as I fulfill my vows day after day.",
      "T": "So I will praise your name forever,\nfulfilling my vows with every passing day."
    }
  },
  "62": {
    "1": {
      "L": "To the chief Musician, to Jeduthun, A Psalm of David. Truly my soul waiteth in silence upon God alone; from him cometh my salvation.",
      "M": "To the choirmaster, according to Jeduthun. A Psalm of David. Truly my soul waits in silence for God alone; from him comes my salvation.",
      "T": "To the worship leader, after the manner of Jeduthun. A Psalm of David.\n\nIn God alone my soul waits in silence;\nfrom him comes all my salvation."
    },
    "2": {
      "L": "He only is my rock and my salvation; he is my defence; I shall not be greatly moved.",
      "M": "He alone is my rock and my salvation; he is my fortress; I will not be greatly shaken.",
      "T": "He alone is my rock and my rescue,\nmy stronghold —\nI will not be greatly shaken."
    },
    "3": {
      "L": "How long will ye imagine mischief against a man? Ye shall be slain all of you; as a bowing wall shall ye be, and as a tottering fence.",
      "M": "How long will all of you assault a man? You might as well be killing him. You are like a leaning wall, like a tottering fence.",
      "T": "How long will you keep battering a man —\nas if you mean to murder him?\nYou are nothing but a leaning wall,\na fence about to topple."
    },
    "4": {
      "L": "They only consult to thrust him down from his excellency; they delight in lies; they bless with their mouth, but they curse inwardly. Selah.",
      "M": "They only plan to bring him down from his position; they delight in falsehood; with their mouths they bless, but inwardly they curse. Selah.",
      "T": "Their whole aim is to topple him from his high place;\nthey love every lie.\nWith their mouths they speak blessing,\nbut inwardly they are cursing. Selah."
    },
    "5": {
      "L": "My soul, wait thou only in silence for God; for my expectation is from him.",
      "M": "Be still before God alone, my soul; for my hope comes from him.",
      "T": "Wait in silence for God alone, my soul —\nhe is the only source from which my hope can come."
    },
    "6": {
      "L": "He only is my rock and my salvation; he is my defence; I shall not be moved.",
      "M": "He alone is my rock and my salvation; he is my fortress; I will not be shaken.",
      "T": "He alone is my rock and my rescue,\nmy stronghold —\nI will not be shaken."
    },
    "7": {
      "L": "In God is my salvation and my glory; the rock of my strength and my refuge is in God.",
      "M": "In God rests my salvation and my honor; God is the rock of my strength, my refuge.",
      "T": "My salvation and my honor rest in God;\nhe is the rock of my strength,\nmy refuge in every storm."
    },
    "8": {
      "L": "Trust in him at all times, O people; pour out your heart before him; God is a refuge for us. Selah.",
      "M": "Trust in him at all times, O people; pour out your hearts before him; God is a refuge for us. Selah.",
      "T": "Trust in him at every moment, all you people;\npour out your hearts before him —\nGod is our refuge. Selah."
    },
    "9": {
      "L": "Surely men of low degree are a breath; men of high degree are a lie; in the balances they go up; they are together lighter than breath.",
      "M": "Surely common people are only a breath, and people of rank are a deception; weighed in the scales they rise — they are lighter than a breath.",
      "T": "Common people are nothing but a breath;\nthe powerful are a fraud.\nPut them on the scales together —\nthey rise up lighter than vapor."
    },
    "10": {
      "L": "Trust not in oppression, and become not vain in robbery; if riches increase, set not your heart upon them.",
      "M": "Do not trust in extortion; do not take false pride in robbery; if wealth increases, do not set your heart on it.",
      "T": "Do not put your trust in extortion,\nor find your identity in what you have stolen.\nIf wealth piles up,\ndo not give it your heart."
    },
    "11": {
      "L": "Once God has spoken; twice have I heard this: that power belongs to God.",
      "M": "One thing God has spoken; two things I have heard: that power belongs to God.",
      "T": "God has spoken one truth\nthat I have heard confirmed again and again:\npower belongs to God alone."
    },
    "12": {
      "L": "And to thee, O Lord, belongs steadfast love; for thou dost render to every man according to his work.",
      "M": "And to you, O Lord, belongs steadfast love; for you repay each person according to their deeds.",
      "T": "And steadfast love belongs to you, O Lord —\nfor you repay every person\nexactly as their deeds deserve."
    }
  },
  "63": {
    "1": {
      "L": "A Psalm of David, when he was in the wilderness of Judah. O God, thou art my God; earnestly will I seek thee; my soul thirsteth for thee; my flesh fainteth for thee in a dry and weary land where no water is.",
      "M": "A Psalm of David, when he was in the wilderness of Judah. O God, you are my God; earnestly I seek you; my soul thirsts for you; my flesh longs for you in a dry and parched land where there is no water.",
      "T": "A Psalm of David, written when he was in the wilderness of Judah.\n\nO God, you are my God —\nearnestly I seek you.\nMy soul thirsts for you;\nmy flesh is faint with longing,\nas if in a dry and waterless wilderness."
    },
    "2": {
      "L": "So I have looked upon thee in the sanctuary, to see thy power and thy glory.",
      "M": "So I have gazed upon you in the sanctuary, beholding your power and your glory.",
      "T": "So I look for you here\nas I once gazed on you in the sanctuary —\nbeholding your power, your glory."
    },
    "3": {
      "L": "Because thy steadfast love is better than life, my lips shall praise thee.",
      "M": "Because your steadfast love is better than life itself, my lips will praise you.",
      "T": "Your steadfast love is better than life itself —\nso my lips cannot hold back their praise."
    },
    "4": {
      "L": "So will I bless thee as long as I live; in thy name will I lift up my hands.",
      "M": "So I will bless you as long as I live; in your name I will lift up my hands.",
      "T": "So I will bless you as long as I breathe;\nI will lift my hands in praise of your name."
    },
    "5": {
      "L": "My soul shall be satisfied as with fat and rich food; and my mouth shall praise thee with joyful lips.",
      "M": "My soul is satisfied as with the richest of food; my mouth praises you with joyful lips.",
      "T": "My soul is satisfied as at a feast of the richest food;\nmy mouth overflows with praise upon joyful lips."
    },
    "6": {
      "L": "When I remember thee upon my bed, and meditate on thee in the night watches.",
      "M": "When I remember you on my bed, I meditate on you through the watches of the night.",
      "T": "In the quiet of my bed I remember you;\nI think of you through all the watches of the night."
    },
    "7": {
      "L": "For thou hast been my help; and in the shadow of thy wings will I rejoice.",
      "M": "For you have been my help; and in the shadow of your wings I will rejoice.",
      "T": "You have always been my help —\nso in the shadow of your wings I will shout for joy."
    },
    "8": {
      "L": "My soul cleaveth fast after thee; thy right hand upholdeth me.",
      "M": "My soul clings close to you; your right hand holds me fast.",
      "T": "My soul clings tightly to you;\nyour right hand holds me and will not let go."
    },
    "9": {
      "L": "But those that seek my soul to destroy it shall go into the lower parts of the earth.",
      "M": "But those who seek to destroy my life shall descend into the depths of the earth.",
      "T": "Those who are hunting my life to destroy it\nwill themselves go down\ninto the depths of the earth."
    },
    "10": {
      "L": "They shall be given over to the power of the sword; they shall be a portion for jackals.",
      "M": "They will be delivered over to the sword; they will become prey for jackals.",
      "T": "They will fall to the sword;\nthey will become a meal for jackals."
    },
    "11": {
      "L": "But the king shall rejoice in God; everyone who sweareth by him shall glory; for the mouth of those who speak lies shall be stopped.",
      "M": "But the king will rejoice in God; all who swear by him will boast in him; for the mouths of liars will be silenced.",
      "T": "But the king will rejoice in God;\nall who swear their loyalty to him will boast in him —\nfor every lying mouth will be shut."
    }
  },
  "64": {
    "1": {
      "L": "To the chief Musician, A Psalm of David. Hear my voice, O God, in my complaint; preserve my life from dread of the enemy.",
      "M": "To the choirmaster. A Psalm of David. Hear my voice, O God, in my complaint; guard my life from the terror of the enemy.",
      "T": "To the worship leader. A Psalm of David.\n\nHear me, O God — my voice in distress;\nguard my life from the terror the enemy brings."
    },
    "2": {
      "L": "Hide me from the secret counsel of evildoers, from the tumult of workers of iniquity.",
      "M": "Shelter me from the conspiracy of the wicked, from the scheming mob of evildoers.",
      "T": "Hide me from the secret plots of the wicked,\nfrom the noisy crowd of those who do evil."
    },
    "3": {
      "L": "Who sharpen their tongue like a sword, and bend their bows to shoot their arrows, even bitter words.",
      "M": "They sharpen their tongues like swords and aim bitter words like arrows from a bow.",
      "T": "They grind their tongues sharp as swords;\nthey string the bow and take aim —\nmissiles of bitter, cutting words."
    },
    "4": {
      "L": "That they may shoot in secret at the blameless; suddenly they shoot at him and do not fear.",
      "M": "Shooting from hiding places at the innocent; they strike suddenly and without fear.",
      "T": "They shoot from ambush at the innocent,\nattacking suddenly without hesitation or fear."
    },
    "5": {
      "L": "They hold fast to their evil purpose; they talk of laying snares secretly; they say, Who will see them?",
      "M": "They scheme their evil plan together; they talk of setting traps in secret; they say, Who will see us?",
      "T": "They egg each other on with their evil scheme,\nplanning to lay hidden traps.\n'Who will ever see us?' they say."
    },
    "6": {
      "L": "They devise injustices; we have devised a perfect plan! For the inward thought and heart of every man is deep.",
      "M": "They plan iniquities: 'We have devised a perfect scheme!' But the inward thought and heart of a person are unfathomable.",
      "T": "They think up wickedness and say,\n'We have the perfect plan!' —\nbut the depths of the human heart are beyond fathoming."
    },
    "7": {
      "L": "But God shall shoot at them with an arrow; suddenly shall they be wounded.",
      "M": "But God will shoot his arrow at them; suddenly they will be struck down.",
      "T": "Then God himself draws the bow —\nhis arrow flies and they are struck down suddenly."
    },
    "8": {
      "L": "He makes their own tongue to fall upon themselves; all that see them shall flee away.",
      "M": "God makes their own tongues their undoing; all who see them shake their heads and flee.",
      "T": "The very tongues they sharpened become their ruin;\nall who witness their fate recoil in horror."
    },
    "9": {
      "L": "Then all men shall fear; they shall declare the work of God and shall wisely consider what he has done.",
      "M": "Then all people will stand in fear; they will proclaim what God has done and ponder his deeds.",
      "T": "Then all people will stand in awe,\nproclaiming what God has done,\npondering the work of his hand."
    },
    "10": {
      "L": "The righteous shall rejoice in the LORD and take refuge in him; and all the upright in heart shall glory.",
      "M": "The righteous will rejoice in the LORD and take refuge in him; all the upright in heart shall boast.",
      "T": "The righteous will rejoice in the LORD\nand find their shelter in him;\nall the upright of heart will boast in God."
    }
  },
  "65": {
    "1": {
      "L": "To the chief Musician, A Psalm and Song of David. Praise waiteth for thee, O God, in Zion; and unto thee shall the vow be performed.",
      "M": "To the choirmaster. A Psalm. A Song of David. Praise awaits you in silence, O God, in Zion; and to you the vow shall be fulfilled.",
      "T": "To the worship leader. A Psalm. A Song of David.\n\nTo you, O God of Zion, praise gathers in silence;\nto you every vow will be paid."
    },
    "2": {
      "L": "O thou that hearest prayer, unto thee shall all flesh come.",
      "M": "O you who hear prayer, to you all flesh shall come.",
      "T": "You who answer prayer —\nto you all humanity will come."
    },
    "3": {
      "L": "When iniquities prevail against me, thou dost atone for our transgressions.",
      "M": "When our sins overwhelm us, you atone for our transgressions.",
      "T": "When our sins have become too heavy for us,\nyou are the one who covers them over."
    },
    "4": {
      "L": "Blessed is the man whom thou choosest and causest to come near, that he may dwell in thy courts; we shall be satisfied with the goodness of thy house, thy holy temple.",
      "M": "Blessed is the one you choose and bring near, to dwell in your courts; we shall be satisfied with the goodness of your house, your holy temple.",
      "T": "Blessed is the person you choose and draw close,\nto live in the shelter of your courts.\nWe will feast on the goodness of your house,\nthe sacred bounty of your holy temple."
    },
    "5": {
      "L": "By awesome deeds thou dost answer us in righteousness, O God of our salvation; thou art the confidence of all the ends of the earth and of the farthest seas.",
      "M": "By awesome deeds in righteousness you answer us, O God of our salvation; you are the hope of all the ends of the earth and of the most distant seas.",
      "T": "With awe-inspiring acts of justice you answer us,\nO God of our salvation —\nthe one hope of every corner of the earth\nand of the most distant seas."
    },
    "6": {
      "L": "Who by his strength establishes the mountains, being girded with might.",
      "M": "The one who by his strength sets the mountains in place, who is clothed with power.",
      "T": "With your own strength you planted the mountains where they stand;\nyou wrap yourself in power."
    },
    "7": {
      "L": "Who stills the roaring of the seas, the roaring of their waves, and the tumult of the peoples.",
      "M": "You still the roaring of the seas, the roaring of their waves, and the uproar of the nations.",
      "T": "You silence the roaring oceans,\nthe crash of wave upon wave —\nand the uproar of nations as well."
    },
    "8": {
      "L": "Those who dwell at the ends of the earth are in awe at thy signs; thou makest the outgoings of the morning and evening to shout for joy.",
      "M": "Those who live at earth's farthest bounds stand in awe of your signs; you make the sunrise and the sunset ring with joy.",
      "T": "The people at the ends of the earth\nstand in awe at your mighty signs;\nyou fill the morning and the evening\nwith shouts of joy."
    },
    "9": {
      "L": "Thou visitest the earth and waterest it; thou greatly enrichest it with the river of God which is full of water; thou preparest grain for them, for so thou hast prepared it.",
      "M": "You visit the earth and water it abundantly; you enrich it with the river of God, full of water; you provide grain for them, for so you have prepared it.",
      "T": "You come to water the earth\nand drench it with abundance;\nthe river of God brims full.\nYou prepare the grain —\nfor this is how you have arranged it all."
    },
    "10": {
      "L": "Thou waterest its furrows abundantly, thou settlest its ridges, thou softenest it with showers, thou blessest its growth.",
      "M": "You soak its furrows abundantly, you level its ridges, you soften it with showers, and you bless what springs up from it.",
      "T": "You drench the furrows till they overflow;\nyou smooth the clods;\nyou soften the ground with gentle showers\nand bless everything that springs up."
    },
    "11": {
      "L": "Thou crownest the year with thy goodness; and thy paths drip with fatness.",
      "M": "You crown the year with your bounty; your wagon tracks overflow with abundance.",
      "T": "You crown the whole year with your goodness;\nwherever you pass, abundance drips down."
    },
    "12": {
      "L": "The pastures of the wilderness drip; and the hills are girded with joy.",
      "M": "The pastures of the wilderness overflow; the hills are wrapped in rejoicing.",
      "T": "Even the wilderness meadows overflow with life;\nthe hills are wrapped in celebration."
    },
    "13": {
      "L": "The meadows are clothed with flocks; the valleys are covered over with grain; they shout for joy; they also sing.",
      "M": "The meadows are dressed with flocks; the valleys are blanketed with grain — they shout for joy, they break into song.",
      "T": "The pastures are dressed in flocks;\nthe valleys lie hidden under grain —\nthey shout their praise,\nthey break into song."
    }
  },
  "66": {
    "1": {
      "L": "To the chief Musician, A Song or Psalm. Shout for joy to God, all the earth.",
      "M": "To the choirmaster. A Song. A Psalm. Shout joyfully to God, all the earth.",
      "T": "To the worship leader. A Song. A Psalm.\n\nShout with joy to God, all the earth!"
    },
    "2": {
      "L": "Sing forth the glory of his name; make his praise glorious.",
      "M": "Sing the glory of his name; make his praise resplendent.",
      "T": "Sing the splendor of his name;\ngive him glory in your praise."
    },
    "3": {
      "L": "Say to God, How awesome are thy works! Through the greatness of thy power thine enemies shall submit themselves unto thee.",
      "M": "Say to God, 'How awesome are your deeds! Through the greatness of your power your enemies cower before you.'",
      "T": "Say to God: 'Your deeds are terrifying in their power!\nYour enemies cower before you\nbecause of your overwhelming strength.'"
    },
    "4": {
      "L": "All the earth shall worship thee and shall sing unto thee; they shall sing to thy name. Selah.",
      "M": "All the earth bows down before you; they sing to you, they sing praises to your name. Selah.",
      "T": "All the earth bows before you;\nthey sing to you —\nthey sing praises to your name. Selah."
    },
    "5": {
      "L": "Come and see the works of God; he is awesome in his deeds toward the children of men.",
      "M": "Come and see what God has done; he is awesome in his acts toward humanity.",
      "T": "Come, look at what God has done —\nhow awe-inspiring his acts toward all of us."
    },
    "6": {
      "L": "He turned the sea into dry land; they passed through the river on foot; there did we rejoice in him.",
      "M": "He turned the sea into dry land; they crossed the river on foot; there we rejoiced in him.",
      "T": "He split the sea into dry ground;\nthey walked across the river on foot —\nthere we rejoiced in him."
    },
    "7": {
      "L": "He rules by his might for ever; his eyes keep watch on the nations; let not the rebellious exalt themselves. Selah.",
      "M": "He rules by his power forever; his eyes watch over the nations — let the rebellious not exalt themselves. Selah.",
      "T": "He governs by his power forever;\nhis eyes are fixed on every nation.\nLet no rebel think they can rise above him. Selah."
    },
    "8": {
      "L": "Bless our God, O peoples; let the sound of his praise be heard.",
      "M": "Bless our God, O peoples; let the sound of his praise be heard.",
      "T": "Bless our God, all you peoples;\nlet his praise ring out everywhere."
    },
    "9": {
      "L": "Who holdeth our soul in life and suffereth not our feet to be moved.",
      "M": "He keeps our lives from death and does not allow our feet to stumble.",
      "T": "He holds our lives safe from death\nand keeps our feet from stumbling."
    },
    "10": {
      "L": "For thou, O God, hast proved us; thou hast tried us as silver is tried.",
      "M": "For you, O God, have tested us; you have refined us as silver is refined.",
      "T": "For you have put us through the fire, O God;\nyou have refined us the way silver is refined."
    },
    "11": {
      "L": "Thou broughtest us into the net; thou laidst affliction upon our loins.",
      "M": "You brought us into the net; you laid a crushing burden on our backs.",
      "T": "You let us be caught in the net;\nyou pressed the weight of suffering onto our backs."
    },
    "12": {
      "L": "Thou hast caused men to ride over our heads; we went through fire and through water; but thou broughtest us out to a place of abundance.",
      "M": "You let men ride over our heads; we went through fire and through water; yet you brought us out to a wide and spacious place.",
      "T": "You let enemies ride roughshod over us;\nwe went through fire;\nwe went through flood —\nbut you brought us out\ninto an open and spacious place."
    },
    "13": {
      "L": "I will come into thy house with burnt offerings; I will perform my vows unto thee.",
      "M": "I will come into your house with burnt offerings; I will fulfill my vows to you.",
      "T": "I will come into your house with burnt offerings;\nI will pay every vow I made to you."
    },
    "14": {
      "L": "Which my lips have uttered and my mouth hath spoken when I was in trouble.",
      "M": "The vows that my lips uttered and my mouth spoke in my time of trouble.",
      "T": "Every word my lips poured out,\nevery promise my mouth made\nin the dark days of my trouble."
    },
    "15": {
      "L": "I will offer unto thee burnt sacrifices of fatted animals, with the incense of rams; I will offer bullocks with goats. Selah.",
      "M": "I will offer you burnt offerings of fattened animals, with the rising smoke of rams; I will sacrifice bulls and goats. Selah.",
      "T": "I will bring fattened animals as burnt offerings to you,\nrams ascending in fragrant smoke —\nbulls and goats as well. Selah."
    },
    "16": {
      "L": "Come and hear, all ye that fear God, and I will declare what he hath done for my soul.",
      "M": "Come and hear, all you who fear God, and I will tell what he has done for me.",
      "T": "Come and listen, all you who fear God —\nlet me tell you what he has done for me."
    },
    "17": {
      "L": "I cried unto him with my mouth, and he was extolled with my tongue.",
      "M": "I cried out to him with my mouth, and his praise was on my tongue.",
      "T": "I called out to him with my mouth,\nand praise for him was already rising on my tongue."
    },
    "18": {
      "L": "If I had regarded iniquity in my heart, the Lord would not have heard.",
      "M": "If I had cherished sin in my heart, the Lord would not have listened.",
      "T": "If I had been nursing sin in my heart,\nthe Lord would not have listened."
    },
    "19": {
      "L": "But truly God hath heard; he hath attended to the voice of my prayer.",
      "M": "But truly God has heard; he has attended to the voice of my prayer.",
      "T": "But God did hear —\nhe actually attended to the voice of my prayer."
    },
    "20": {
      "L": "Blessed be God, who hath not turned away my prayer nor his steadfast love from me.",
      "M": "Blessed be God, who has not turned away my prayer or withheld his steadfast love from me.",
      "T": "Blessed be God,\nwho did not turn away my prayer\nor keep his steadfast love from me."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 61–66 written.')

if __name__ == '__main__':
    main()
