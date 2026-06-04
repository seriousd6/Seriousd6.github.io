"""
MKT Psalms chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-13-18.py

=== Overview of this unit ===

Ps 13 (6 v) — Lament of David. The fourfold "How long?" is the structural heart:
    four rhetorical blows before the pivot to trust in v5. The prayer moves from
    anguish → petition → trust → vow of praise in six tight verses. H2617 (chesed,
    steadfast love) is the pivot word at v5.

Ps 14 (7 v) — Universal indictment. H5036 (nabal, "fool") is not an intellectual
    simpleton but a morally bankrupt person who acts as if God is irrelevant — the
    Hebrew fool is a practical atheist, not a philosophical one. vv1–3 are cited by
    Paul in Romans 3:10–12 to establish universal human guilt. v7's "restores the
    fortunes" (H7622, shevut) is better read as reversing captivity than restoring
    material wealth; T renders accordingly.

Ps 15 (5 v) — Entrance liturgy. A list of ten-or-eleven characteristics of the
    person worthy to "dwell on God's holy hill" (H2022 + H6944). The final line
    "shall never be moved" (H4131) is the benediction: this life is unshakeable.

Ps 16 (11 v) — Miktam of David (H4387, genre uncertain — possibly "inscription" or
    "golden"). A sustained expression of trust and contentment in God. Two NT
    citations: v10 (Acts 2:27, Peter on resurrection) and v10–11 (Acts 13:35, Paul).
    H7307 does not appear here; "kidneys" (H3629, kelayot, v7) = the seat of deep
    inner wisdom in Hebrew anthropology, rendered "inmost self" in M/T.

Ps 17 (15 v) — Prayer of David (H8605, tephillah). A legal metaphor runs throughout:
    David appeals to God as judge. The climax (v15) projects beyond the immediate
    situation to beholding God's face — possibly a morning-prayer awakening, possibly
    eschatological; T preserves the ambiguity. H380 (iyshon, "apple of the eye") =
    literally "the little man of the eye" (the reflected image in the pupil).

Ps 18 (50 v) — Royal victory psalm, also in 2 Sam 22 (nearly verbatim). The
    superscription is v1 in the interlinear. The theophany in vv7–15 is one of the
    grandest storm-god descriptions in the Hebrew Bible, wholly reclaimed as the God
    of Israel arriving to rescue one servant. The poem moves: crisis (vv4–6) →
    theophany (vv7–15) → rescue (vv16–19) → theological reflection (vv20–29) →
    warrior's victory hymn (vv30–45) → doxology (vv46–50).

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps by convention) in L/M throughout. In T:
      "the LORD" — Psalms use the divine name prominently and personally. The warmth
      and intimacy of direct address ("I love you, LORD") in Ps 18:1 is preserved.
      No "Yahweh" substitution — the LORD convention is consistent across all scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Grammatically plural, contextually
      singular when referring to YHWH. No note needed in each verse.

H136 (אֲדֹנָי, Adonai, Ps 16:2): "my Lord" in L, "my Lord" in M, "my Master" in T.
      The distinction between the divine personal name (H3068) and the title (H136)
      matters; David uses both. In this verse both appear; L/M render both distinctly.

H7307 (רוּחַ, ruach, Ps 18:10,15): Physical "wind" in both occurrences here.
      Ps 18:10 — "wings of the wind" (H3671 + H7307) = atmospheric wind, not Spirit.
      Ps 18:15 — "breath of your nostrils" (H7307 + H639) = divine wind-breath driving
      back the sea. Context is theophanic storm, not Spirit-presence. Lowercase "wind"
      and "breath" used accordingly. This is the same H7307 used for Spirit elsewhere;
      context governs.

H2617 (חֶסֶד, chesed): "steadfast love" in M/T throughout. In L: "steadfast love" —
      the translation tradition of "lovingkindness" is old but underplays the covenantal
      weight of the word. Chesed = covenant loyalty actively expressed; "steadfast love"
      captures the dual dimension better. Consistent with all prior MKT scripts.

H5315 (נֶפֶשׁ, nefesh): "soul" in L. In M/T: "soul" or "life" according to context.
      Ps 13:2 — "in my soul" (anguished inner life); Ps 16:10 — "you will not leave my
      soul in Sheol" (the embodied self destined for death); Ps 17:13 — "deliver my
      soul from the wicked" (my life, my self). No Greek immaterial-soul import; nefesh
      is the whole embodied person viewed as a living being.

H6664 (צֶדֶק / צְדָקָה, tsedeq/tsedaqah, righteousness): "righteousness" in L.
      In M: "righteousness." In T: expanded only when context requires it. Ps 17:1 —
      the legal dimension (a just cause) is foregrounded. Ps 18:20,24 — David's claim
      about his own conduct; not imputed righteousness but actual life quality. T notes
      this distinction where relevant.

H5036 (נָבָל, nabal, Ps 14:1): "fool" in L/M. In T: "the morally bankrupt" — nabal
      is the person who acts as though God has no claim on them; the English "fool"
      can suggest mere stupidity. T clarifies the moral dimension. (Same root as Abigail's
      husband in 1 Samuel 25.)

H7622 (שְׁבוּת, shevut, Ps 14:7): "fortunes" in L/M (modern scholarly consensus
      over "captivity"). T renders "reverses the captivity" because the phrase has a
      liberation register that "restores the fortunes" loses in context. The word is
      disputed; documented here.

H4387 (מִכְתָּם, miktam, Ps 16:1): Transliterated "Miktam" in L/M/T. Genre designation
      of uncertain meaning; LXX treats it as a title ("pillar inscription"). Not rendered
      as a common noun.

H3629 (כְּלָיוֹת, kelayot, Ps 16:7): "kidneys" in L (anatomically accurate). In M:
      "inmost self." In T: "my deepest self." The kidneys were the locus of interior
      wisdom/conscience in Hebrew anthropology — the seat of what we would call the
      moral imagination. The traditional "reins" is archaic English for the same idea.

H3519 (כָּבוֹד, kabod, Ps 16:9): "glory" in L (traditional). M renders "spirit" to
      follow the poetic parallelism with "heart" (H3820); some traditions follow the
      LXX reading "tongue" (γλῶσσά, which is attested in Acts 2:26). L preserves "glory"
      as the source word; M/T use "spirit" to keep the parallelism with the body-parts
      sequence (heart / spirit / flesh). Documented: this is a textual/interpretive choice.

H7355 (רָחַם, racham, Ps 18:1): "love" in all tiers. This verb form expressing David's
      love for the LORD is unique in the Psalter — the root is usually divine love,
      maternal tenderness. Its use here is striking: David loves God with the intensity
      of parental-tender love. T preserves this warmth.

H6037 (עַנְוָה, anavah, Ps 18:35): "gentleness" in M/T. Traditional "humility" works,
      but anavah here describes God's quality — his condescension to David, his gentle
      guiding hand. "Gentleness" is more fitting than "humility" for the divine attribute.
      Documented deviation from the common rendering.

=== Aspect and tense notes ===

Ps 13–16 use a mixture of perfect and imperfect verbs that carry emotional weight:
    Ps 13:5 — "I have trusted" (H982, batach, perfect) — a completed orientation of
    trust that carries present force. Not "I will trust" (future) but "I have staked
    myself on this." The pivot in the psalm is marked by the aspect shift.
    Ps 14:1 — "They are corrupt" (H7843, shahat, perfect) — completed corruption as
    a present state; the moral rot is established fact.
    Ps 15 — present participles dominate (the walk, the work, the speech) — the portrait
    is of ongoing habitual character, not a one-time act. M/T render as present tense.
    Ps 16:8 — "I have set" (H7737, shavah, perfect) — a completed deliberate act with
    lasting present effect. "I set the LORD before me always" = deliberate orientation.
    Ps 18:7–15 — the theophany uses waw-consecutive imperfects (narrative past) for
    vv7–15, then shifts to "he reached" (imperfect with suffix, v16). The narrative
    drive carries the reader into the moment. T should have momentum.

=== OT echo notes ===

Ps 16:10 — "you will not leave my soul in Sheol, nor let your Holy One see corruption":
    Peter (Acts 2:25–28) and Paul (Acts 13:35) apply this to Jesus' resurrection. The
    psalm itself is David's personal confidence; the NT reads it typologically. T tier
    preserves the psalm's primary sense; the messianic reading is a legitimate extension.

Ps 18:2 — The cluster of metaphors (rock / fortress / deliverer / shield / horn /
    stronghold) echoes the Song of Moses (Deut 32:4,18 — "the Rock"), 1 Sam 2:1–2
    (Hannah's song), and anticipates the Psalter's persistent "Rock" theology. David
    is standing in a long tradition when he piles up these images.

Ps 18:7–15 — The theophany echoes the Sinai theophany (Exod 19), the Elijah theophany
    (1 Kgs 19), and anticipates the apocalyptic storm theophanies of the prophets (Hab
    3, Ezek 1). God arrives in the same mode each time: storm, darkness, fire. T should
    have grandeur without losing the personal — God is doing all this for one man.

Ps 18:50 — "to David and his seed forever": the Davidic covenant (2 Sam 7) is the
    theological frame. "His anointed" (H4899, mashiach) = the Messiah-king in seed form.
    The NT sees Jesus as the fulfillment of this dynastic promise. T notes the covenant
    horizon without over-reading the psalm.
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
  # Psalm 13 — Lament: "How Long, O LORD?"
  # ============================================================
  "13": {
    "1": {
      "L": "To the director of music. A Psalm of David. How long, O LORD? Will you forget me forever? How long will you hide your face from me?",
      "M": "For the director of music. A Psalm of David. How long, LORD? Will you forget me forever? How long will you hide your face from me?",
      "T": "To the choirmaster. Of David.\nHow long, LORD? Forever?\nHow long will you turn your face away from me?"
    },
    "2": {
      "L": "How long shall I take counsel in my soul, bearing sorrow in my heart daily? How long shall my enemy be exalted over me?",
      "M": "How long must I wrestle with my thoughts, bearing sorrow in my heart every day? How long will my enemy triumph over me?",
      "T": "How long must I carry this grief inside me,\nthis daily weight of sorrow?\nHow long will the enemy stand over me in triumph?"
    },
    "3": {
      "L": "Consider and answer me, O LORD my God; lighten my eyes, lest I sleep the sleep of death,",
      "M": "Look at me and answer me, O LORD my God; give light to my eyes, lest I fall into the sleep of death,",
      "T": "Look at me, LORD—answer me.\nBrighten my eyes before they close in the sleep of death;"
    },
    "4": {
      "L": "lest my enemy say, 'I have prevailed against him,' and those who trouble me rejoice because I am moved.",
      "M": "lest my enemy say, 'I have overcome him,' and my foes rejoice when I am brought down.",
      "T": "lest the enemy crow, 'I have broken him,'—\nlest my foes celebrate the moment I stumble and fall."
    },
    "5": {
      "L": "But I have trusted in your steadfast love; my heart shall rejoice in your salvation.",
      "M": "But I have trusted in your steadfast love; my heart will rejoice in your salvation.",
      "T": "But I have staked everything on your steadfast love.\nMy heart will yet burst into joy at your rescue."
    },
    "6": {
      "L": "I will sing to the LORD, because he has dealt bountifully with me.",
      "M": "I will sing to the LORD, for he has been generous to me.",
      "T": "I will sing to the LORD.\nHe has dealt generously with me—I know it even now."
    }
  },

  # ============================================================
  # Psalm 14 — Universal Indictment of Human Corruption
  # ============================================================
  "14": {
    "1": {
      "L": "To the chief musician. A Psalm of David. The fool says in his heart, 'There is no God.' They are corrupt; they have done abominable works; there is none who does good.",
      "M": "For the director of music. A Psalm of David. The fool says in his heart, 'There is no God.' They are corrupt; they have done vile deeds; there is no one who does good.",
      "T": "To the choirmaster. Of David.\nThe morally bankrupt say to themselves, 'God doesn't count.'\nAnd so they become corrupt, their deeds repugnant—\nnot one of them does what is good."
    },
    "2": {
      "L": "The LORD looked down from heaven upon the children of men to see if there were any who understood, who sought after God.",
      "M": "The LORD looks down from heaven on all people to see if there are any who understand, who seek God.",
      "T": "From heaven the LORD surveys the whole human family—\nscanning for anyone who grasps reality, who actually seeks him."
    },
    "3": {
      "L": "They have all gone aside; they have altogether become filthy; there is none who does good, no, not one.",
      "M": "All have turned aside; all have become corrupt together; there is no one who does good, not even one.",
      "T": "Every one of them has turned off the path.\nEvery one has curdled.\nNot one does good—not a single one."
    },
    "4": {
      "L": "Do they not know, all the workers of iniquity, who eat up my people as they eat bread, and do not call upon the LORD?",
      "M": "Do none of the workers of evil understand—those who devour my people as they eat bread, and who do not call on the LORD?",
      "T": "Have they no understanding at all—these agents of ruin\nwho consume my people like bread at a meal,\nwho never once think to call on God?"
    },
    "5": {
      "L": "There they feared greatly, for God is in the generation of the righteous.",
      "M": "There they were filled with fear, for God is with the righteous generation.",
      "T": "Then terror seized them—sudden, overwhelming—\nbecause God stands with those who are faithful to him."
    },
    "6": {
      "L": "You would put to shame the counsel of the poor, because the LORD is his refuge.",
      "M": "You would shame the plans of the poor, but the LORD is their refuge.",
      "T": "You would humiliate the powerless and undermine them—\nbut the LORD himself is their shelter."
    },
    "7": {
      "L": "Oh that the salvation of Israel would come out of Zion! When the LORD restores the fortunes of his people, Jacob shall rejoice, Israel shall be glad.",
      "M": "Oh, that salvation for Israel would come from Zion! When the LORD restores the fortunes of his people, Jacob will rejoice and Israel will be glad.",
      "T": "When will the rescue come—from Zion, where God dwells?\nWhen the LORD reverses his people's captivity,\nJacob will burst out laughing and Israel will dance."
    }
  },

  # ============================================================
  # Psalm 15 — Entrance Liturgy: Who May Dwell with God?
  # ============================================================
  "15": {
    "1": {
      "L": "A Psalm of David. O LORD, who shall sojourn in your tabernacle? Who shall dwell on your holy hill?",
      "M": "A Psalm of David. LORD, who may dwell in your sanctuary? Who may live on your holy mountain?",
      "T": "Of David.\nLORD, who belongs in your house?\nWho has the right to stand on your holy mountain?"
    },
    "2": {
      "L": "He who walks blamelessly and works righteousness, and speaks truth in his heart;",
      "M": "The one who walks blamelessly, does what is right, and speaks truth from the heart;",
      "T": "The one whose life is whole and consistent—\nwho does what is just and who means what they say."
    },
    "3": {
      "L": "who does not slander with his tongue, and does no evil to his neighbor, nor takes up a reproach against his friend;",
      "M": "who does not slander with the tongue, does no harm to a neighbor, and takes up no reproach against a friend;",
      "T": "Someone who keeps their tongue clean of slander,\nwho does nothing to hurt those around them,\nand refuses to pick up a shaming story about a friend."
    },
    "4": {
      "L": "in whose eyes a vile person is despised, but who honors those who fear the LORD; who swears to his own hurt and does not change;",
      "M": "who despises the contemptible but honors those who fear the LORD; who keeps an oath even when it costs them and does not go back on it;",
      "T": "One who sees through what is worthless and honors those who revere God—\nwho takes an oath and keeps it even when it costs dearly,\nnever looking for the exit."
    },
    "5": {
      "L": "who does not put out his money at interest, and does not take a bribe against the innocent. He who does these things shall never be moved.",
      "M": "who does not lend money at interest or take a bribe against the innocent. Whoever does these things will never be shaken.",
      "T": "Who never charges interest on a loan to someone in need,\nand cannot be bought to condemn the innocent.\nThis is the person who stands—unshakeable, forever."
    }
  },

  # ============================================================
  # Psalm 16 — Miktam of David: Contentment and Trust
  # ============================================================
  "16": {
    "1": {
      "L": "A Miktam of David. Preserve me, O God, for in you I take refuge.",
      "M": "A Miktam of David. Keep me safe, O God, for in you I take shelter.",
      "T": "A Miktam—of David.\nKeep me safe, God. You are where I have hidden myself."
    },
    "2": {
      "L": "I said to the LORD, 'You are my Lord; my goodness is nothing apart from you.'",
      "M": "I said to the LORD, 'You are my Lord; I have no good apart from you.'",
      "T": "I have said to the LORD: You are my Master.\nEvery good thing I have exists only in you."
    },
    "3": {
      "L": "As for the holy ones who are in the earth, they are the excellent, in whom is all my delight.",
      "M": "As for the holy ones who are in the land, they are the noble—in them is all my delight.",
      "T": "The faithful ones scattered through the earth—\nthey are the magnificent, and I love them all."
    },
    "4": {
      "L": "The sorrows of those who run after another god shall be multiplied; their drink offerings of blood I will not pour out, nor take their names upon my lips.",
      "M": "The sorrows of those who chase other gods will multiply; I will not pour out their libations of blood or take their names on my lips.",
      "T": "Those who rush headlong after rival gods will multiply their own grief.\nI will not join their rituals—\nnot a syllable of those names will cross my lips."
    },
    "5": {
      "L": "The LORD is my chosen portion and my cup; you hold my lot.",
      "M": "The LORD is my allotted portion and my cup; you secure my future.",
      "T": "The LORD is my share—the portion I have been given.\nHe holds the cup I will drink from.\nMy future is in his hands."
    },
    "6": {
      "L": "The lines have fallen for me in pleasant places; indeed, I have a beautiful inheritance.",
      "M": "The boundary lines have fallen for me in pleasant places; truly I have a beautiful inheritance.",
      "T": "The surveyor's lines have measured out a beautiful piece of land for me.\nWhat a heritage I have been given."
    },
    "7": {
      "L": "I will bless the LORD who gives me counsel; in the night my kidneys also instruct me.",
      "M": "I will praise the LORD who counsels me; even at night my inmost self instructs me.",
      "T": "I praise the LORD who advises me—\neven through the night my deepest self speaks with wisdom."
    },
    "8": {
      "L": "I have set the LORD always before me; because he is at my right hand, I shall not be moved.",
      "M": "I have set the LORD always before me; because he is at my right hand, I will not be shaken.",
      "T": "I have deliberately placed the LORD always in front of me.\nWith him at my right side, nothing can knock me down."
    },
    "9": {
      "L": "Therefore my heart is glad, and my glory rejoices; my flesh also dwells in safety.",
      "M": "Therefore my heart is glad and my spirit rejoices; my body also rests secure.",
      "T": "So my heart is full of gladness,\nmy whole being sings with joy—\nand even this body rests in safety."
    },
    "10": {
      "L": "For you will not abandon my soul to Sheol, nor let your Holy One see corruption.",
      "M": "For you will not leave my soul in Sheol, or let your Holy One see decay.",
      "T": "Because you will not abandon me to the realm of the dead—\nyou will not let your beloved one rot in the grave."
    },
    "11": {
      "L": "You make known to me the path of life; in your presence there is fullness of joy; at your right hand are pleasures forevermore.",
      "M": "You will make known to me the path of life; in your presence is complete joy; at your right hand are pleasures that last forever.",
      "T": "You open the path of life before me.\nIn your presence—joy beyond all other joy.\nAt your right hand, pleasures that will never end."
    }
  },

  # ============================================================
  # Psalm 17 — Prayer of David: Vindication and the Vision of God
  # ============================================================
  "17": {
    "1": {
      "L": "A Prayer of David. Hear a just cause, O LORD; attend to my cry; give ear to my prayer from lips free of deceit.",
      "M": "A Prayer of David. Hear a just cause, O LORD; listen to my cry; give ear to my prayer from lips without deceit.",
      "T": "A Prayer—of David.\nHear me, LORD—this is a righteous plea.\nListen to my cry. I am not lying to you."
    },
    "2": {
      "L": "Let my vindication come forth from your presence; let your eyes see what is right.",
      "M": "Let my vindication come from you; let your eyes behold what is just.",
      "T": "Let my acquittal come directly from you—\nyour eyes can see the truth of it."
    },
    "3": {
      "L": "You have tried my heart; you have visited me by night; you have tested me, and you will find nothing; I have purposed that my mouth will not transgress.",
      "M": "You have tested my heart; you have examined me through the night; you have tried me and found nothing; I have resolved that my mouth will not sin.",
      "T": "You have put my heart to the test—\na night examination—and found nothing to charge me with.\nI have made a firm decision: my mouth will not betray me."
    },
    "4": {
      "L": "Concerning the works of men, by the word of your lips I have kept myself from the paths of the violent.",
      "M": "Regarding human deeds, by the word of your lips I have avoided the ways of the violent.",
      "T": "When it comes to human behavior,\nyour word has been my compass—steering me away from the road of the violent."
    },
    "5": {
      "L": "My steps have held fast to your paths; my feet have not slipped.",
      "M": "My steps have kept to your paths; my feet have not stumbled.",
      "T": "I have stayed on your tracks.\nMy feet have not slid off."
    },
    "6": {
      "L": "I call upon you, for you will answer me, O God; incline your ear to me; hear my speech.",
      "M": "I call on you, for you will answer me, O God; turn your ear to me; hear my words.",
      "T": "I am calling you—and you will answer. I know it.\nTurn your ear toward me, God. Listen."
    },
    "7": {
      "L": "Show your steadfast love, O Savior of those who take refuge from their adversaries at your right hand.",
      "M": "Display your wonderful steadfast love, O Savior of those who seek refuge from their enemies by your right hand.",
      "T": "Show what your steadfast love can do—\nyou who shelter by your right hand those who flee to you\nfrom those who rise against them."
    },
    "8": {
      "L": "Keep me as the apple of the eye; hide me in the shadow of your wings,",
      "M": "Guard me as the apple of your eye; hide me in the shadow of your wings,",
      "T": "Guard me like the pupil of your eye—\nthat small, perfectly protected point at the center.\nShelter me beneath your wings,"
    },
    "9": {
      "L": "from the wicked who despoil me, from my deadly enemies who surround me.",
      "M": "from the wicked who assail me, from my deadly enemies who encircle me.",
      "T": "from violent people who press in on me,\nfrom enemies who would kill me if they could—circling."
    },
    "10": {
      "L": "They have closed their hearts to pity; with their mouths they speak with arrogance.",
      "M": "Their hearts are closed to compassion; their mouths speak with arrogance.",
      "T": "They have sealed themselves against compassion.\nTheir mouths overflow with boasting."
    },
    "11": {
      "L": "Now they surround our steps; they set their eyes to cast us down to the ground.",
      "M": "Now they surround our every step; they watch for a chance to bring us to the ground.",
      "T": "They have closed in all around me now.\nTheir eyes are fixed on one goal: bringing me down to the earth."
    },
    "12": {
      "L": "He is like a lion hungry for prey, like a young lion lurking in hiding places.",
      "M": "He is like a lion eager for prey, like a young lion crouching in ambush.",
      "T": "Like a lion that can think of nothing but the kill—\na young lion invisible in the shadows, waiting."
    },
    "13": {
      "L": "Arise, O LORD! Confront him! Cast him down! Deliver my soul from the wicked by your sword,",
      "M": "Arise, LORD! Confront him! Bring him down! Rescue me from the wicked by your sword,",
      "T": "Arise, LORD! Face him. Strike him down.\nDraw your sword and pull me out from the grip of the wicked—"
    },
    "14": {
      "L": "from men by your hand, O LORD, from men of the world whose portion is in this life. You fill their belly with your treasure; their children are satisfied, and they leave their abundance to their offspring.",
      "M": "by your hand, LORD, from those whose portion is in this present life. May they be filled with what you store up for them; may their children be satisfied and leave their surplus to their children's children.",
      "T": "with your hand, save me from people whose whole world is this world alone—\nwho get everything they want right here, right now.\nYou fill them full anyway; their children inherit plenty,\nand they pass the surplus down yet another generation.\nBut that is all they will ever get."
    },
    "15": {
      "L": "As for me, I shall behold your face in righteousness; when I awake, I shall be satisfied with your likeness.",
      "M": "As for me, I will behold your face in righteousness; when I awake I will be satisfied with your likeness.",
      "T": "But my satisfaction is different:\nI will see your face—not just sense your presence, but see it clearly.\nWhen I awake, I will be full—satisfied by your very image."
    }
  },

  # ============================================================
  # Psalm 18 — Royal Victory Psalm of David
  # ============================================================
  "18": {
    "1": {
      "L": "To the director of music. Of David the servant of the LORD, who addressed to the LORD the words of this song on the day the LORD delivered him from the hand of all his enemies and from the hand of Saul. He said: I love you, O LORD, my strength.",
      "M": "For the director of music. Of David the servant of the LORD, who sang to the LORD the words of this song when the LORD rescued him from all his enemies and from Saul. He said: I love you, LORD, my strength.",
      "T": "To the choirmaster. Of David, servant of the LORD—written for the day the LORD rescued him from the grip of all his enemies and from Saul.\nI love you, LORD. You are my strength."
    },
    "2": {
      "L": "The LORD is my rock and my fortress and my deliverer; my God, my rock in whom I take refuge; my shield, and the horn of my salvation, my stronghold.",
      "M": "The LORD is my rock, my fortress, and my rescuer; my God is my rock in whom I take refuge—my shield, the horn of my salvation, my stronghold.",
      "T": "The LORD is my rock, my fortress, my rescuer—\nmy God is the cliff I hide in.\nHe is my shield, the source of my victory, my high tower."
    },
    "3": {
      "L": "I call upon the LORD, who is worthy to be praised, and I am saved from my enemies.",
      "M": "I called to the LORD, who is worthy of all praise, and I am saved from my enemies.",
      "T": "I called on the LORD—who deserves every praise—\nand he saved me from those who were coming for me."
    },
    "4": {
      "L": "The cords of death encompassed me; the torrents of destruction terrified me;",
      "M": "The cords of death wrapped around me; the floods of chaos overwhelmed me;",
      "T": "The ropes of death wound around me;\nchaos came at me like a flood."
    },
    "5": {
      "L": "the cords of Sheol entangled me; the snares of death came before me.",
      "M": "the ropes of Sheol entangled me; the snares of death were set before me.",
      "T": "Sheol wound its own cords around me;\ndeath's traps were laid directly in my path."
    },
    "6": {
      "L": "In my distress I called upon the LORD; to my God I cried for help. From his temple he heard my voice, and my cry to him reached his ears.",
      "M": "In my distress I called to the LORD; I cried to my God for help. From his temple he heard my voice, and my cry before him came into his ears.",
      "T": "Pressed into a corner, I called on the LORD.\nI cried out to my God.\nFrom his temple he heard my voice—\nmy desperate cry went straight into his ears."
    },
    "7": {
      "L": "Then the earth shook and trembled; the foundations of the mountains quaked and shook, because he was angry.",
      "M": "The earth shook and trembled; the foundations of the mountains quaked and shook, for he was angry.",
      "T": "The earth heaved and shook.\nThe deep roots of the mountains quaked.\nHe was furious—and the ground knew it."
    },
    "8": {
      "L": "Smoke went up from his nostrils and devouring fire from his mouth; glowing coals blazed from it.",
      "M": "Smoke poured from his nostrils and consuming fire from his mouth; blazing coals ignited before him.",
      "T": "Smoke billowed from his nostrils.\nFire poured from his mouth and consumed everything.\nCoals blazed ahead of him."
    },
    "9": {
      "L": "He bowed the heavens and came down; thick darkness was under his feet.",
      "M": "He bowed the heavens and came down; dark cloud was under his feet.",
      "T": "He bent the sky downward and descended—\nstorm cloud his footstool."
    },
    "10": {
      "L": "He rode on a cherub and flew; he soared on the wings of the wind.",
      "M": "He mounted a cherub and flew; he soared on the wings of the wind.",
      "T": "He rode a cherub at full speed,\nflying on the wind's own wings."
    },
    "11": {
      "L": "He made darkness his covering, his canopy around him—thick clouds dark with water.",
      "M": "He made darkness his shelter, his canopy of dark clouds heavy with rain.",
      "T": "He wrapped himself in darkness—\nstorm clouds, black and heavy with water, his pavilion."
    },
    "12": {
      "L": "Out of the brightness before him his clouds broke through, with hailstones and coals of fire.",
      "M": "From the brightness of his presence his clouds burst forth with hailstones and coals of fire.",
      "T": "His own brilliance split the clouds apart—\nhailstones and burning coals blazing out ahead of him."
    },
    "13": {
      "L": "The LORD also thundered in the heavens, and the Most High uttered his voice—hailstones and coals of fire.",
      "M": "The LORD thundered from heaven; the Most High raised his voice amid hailstones and coals of fire.",
      "T": "God thundered across the sky.\nThe Most High raised his voice—\nand the air itself became hail and fire."
    },
    "14": {
      "L": "He sent out his arrows and scattered them; he flashed lightning bolts and routed them.",
      "M": "He shot his arrows and scattered them; he hurled lightning bolts and threw them into confusion.",
      "T": "He launched his arrows and broke their formation.\nLightning—and they collapsed into panic."
    },
    "15": {
      "L": "Then the channels of the sea were seen, and the foundations of the world were uncovered, at your rebuke, O LORD, at the blast of the breath of your nostrils.",
      "M": "The channels of the sea were exposed and the foundations of the world were laid bare at your rebuke, O LORD, at the blast of the breath of your nostrils.",
      "T": "The ocean floor appeared.\nThe bedrock of the world was uncovered—\nall from one word of rebuke, one blast of breath from your nostrils."
    },
    "16": {
      "L": "He reached down from on high; he took me; he drew me out of many waters.",
      "M": "He reached down from on high and took hold of me; he pulled me out of deep waters.",
      "T": "He reached down from above and grabbed me.\nHe pulled me out of the deep flood."
    },
    "17": {
      "L": "He rescued me from my strong enemy and from those who hated me, for they were too mighty for me.",
      "M": "He rescued me from my powerful enemy, from those who hated me—for they were stronger than I was.",
      "T": "He pulled me free of my enemy—powerful, dangerous—\nfrom those who hated me, who were far too strong for me to face alone."
    },
    "18": {
      "L": "They came against me in the day of my calamity, but the LORD was my support.",
      "M": "They confronted me in the day of my disaster, but the LORD was my support.",
      "T": "They came for me at my worst moment.\nBut the LORD held me up."
    },
    "19": {
      "L": "He brought me out into a broad place; he rescued me, because he delighted in me.",
      "M": "He brought me out into an open place; he rescued me, because he was pleased with me.",
      "T": "He brought me out into open ground—\nroom to breathe, room to stand.\nHe did it because he wanted to."
    },
    "20": {
      "L": "The LORD dealt with me according to my righteousness; according to the cleanness of my hands he repaid me.",
      "M": "The LORD rewarded me according to my righteousness; he repaid me according to the cleanness of my hands.",
      "T": "The LORD treated me the way I had been living—\nmy hands were clean, and he knew it."
    },
    "21": {
      "L": "For I have kept the ways of the LORD, and have not wickedly departed from my God.",
      "M": "For I have kept to the LORD's ways and have not turned away from my God in rebellion.",
      "T": "I walked his road.\nI did not abandon my God in the crisis."
    },
    "22": {
      "L": "For all his judgments were before me, and his statutes I did not put away from me.",
      "M": "All his rules were set before me, and I did not set aside his statutes.",
      "T": "His decrees were always in front of me.\nI never put them behind me."
    },
    "23": {
      "L": "I was blameless before him, and I kept myself from my iniquity.",
      "M": "I was blameless before him and kept myself from wrongdoing.",
      "T": "Before him I was blameless—\nand I kept myself away from my own tendency to sin."
    },
    "24": {
      "L": "So the LORD repaid me according to my righteousness, according to the cleanness of my hands in his sight.",
      "M": "So the LORD rewarded me according to my righteousness, according to the cleanness of my hands in his eyes.",
      "T": "And so the LORD returned to me what I had given to him.\nHis eyes saw my hands were clean."
    },
    "25": {
      "L": "With the merciful you show yourself merciful; with the blameless man you show yourself blameless;",
      "M": "To the faithful you show yourself faithful; to the blameless you show yourself blameless;",
      "T": "To the loyal, you are loyal.\nTo the blameless, you are blameless."
    },
    "26": {
      "L": "with the pure you show yourself pure; and with the crooked you show yourself shrewd.",
      "M": "to the pure you show yourself pure; but to the devious you show yourself cunning.",
      "T": "To the pure, you are pure.\nBut with the twisted, you become the one who outsmarts them—\nyou meet each person where they are."
    },
    "27": {
      "L": "For you save a humble people, but the haughty eyes you bring down.",
      "M": "For you save an afflicted people, but proud eyes you humble.",
      "T": "You lift up the poor and lowly.\nThe ones who strut—you bring them down."
    },
    "28": {
      "L": "For it is you who light my lamp; the LORD my God lightens my darkness.",
      "M": "For you light my lamp; the LORD my God brightens my darkness.",
      "T": "You are the one who keeps my lamp burning.\nYou push back my darkness, LORD."
    },
    "29": {
      "L": "For by you I can run against a troop, and by my God I can leap over a wall.",
      "M": "For by your help I can charge against a raiding party; by my God I can scale a wall.",
      "T": "With you behind me, I can storm a fortified position.\nWith my God, I can clear any wall."
    },
    "30": {
      "L": "This God—his way is perfect; the word of the LORD proves true; he is a shield to all who take refuge in him.",
      "M": "This God—his way is perfect; the LORD's word is refined and true; he is a shield to all who shelter in him.",
      "T": "This God is flawless in everything he does.\nHis word has been refined to perfection—nothing false in it.\nHe is a shield to everyone who runs to him."
    },
    "31": {
      "L": "For who is God but the LORD? And who is a rock, except our God?",
      "M": "For who is God besides the LORD? And who is a rock except our God?",
      "T": "Who else is God? No one but the LORD.\nWho else is a Rock? No one but our God."
    },
    "32": {
      "L": "The God who equipped me with strength and made my way blameless,",
      "M": "It is God who arms me with strength and makes my way perfect—",
      "T": "He is the one who girds me with strength\nand sets my path straight."
    },
    "33": {
      "L": "who made my feet like the feet of a deer and set me secure on the heights,",
      "M": "he makes my feet like the feet of a deer and sets me securely on the heights,",
      "T": "He gives me the agility of a mountain deer—\nsurefootedness on ground that would make others fall."
    },
    "34": {
      "L": "who trains my hands for war, so that my arms can bend a bow of bronze.",
      "M": "he trains my hands for battle; my arms can bend a bow of bronze.",
      "T": "He has trained my hands for war—\nmy arms can now bend what no one bends unaided."
    },
    "35": {
      "L": "You have given me the shield of your salvation, and your right hand upheld me, and your humility made me great.",
      "M": "You have given me the shield of your salvation; your right hand held me up, and your gentleness made me great.",
      "T": "You handed me the shield of your rescue.\nYour right arm held me up.\nAnd here is the surprise: your gentleness is what made me great."
    },
    "36": {
      "L": "You gave a wide place for my steps under me, and my feet did not slip.",
      "M": "You gave wide room for my steps beneath me, and my feet did not slip.",
      "T": "You widened the ground beneath my feet—\nthere was room to plant myself, and I did not fall."
    },
    "37": {
      "L": "I pursued my enemies and overtook them, and did not turn back until they were consumed.",
      "M": "I pursued my enemies and overtook them and did not turn back until they were finished.",
      "T": "I ran my enemies down.\nI did not stop until every one of them was done."
    },
    "38": {
      "L": "I struck them down, so that they were not able to rise; they fell under my feet.",
      "M": "I struck them down so that they could not rise; they fell under my feet.",
      "T": "I hit them so hard they could not get up.\nThey went down at my feet."
    },
    "39": {
      "L": "For you equipped me with strength for the battle; you made those who rise against me sink down under me.",
      "M": "For you armed me with strength for the battle; you brought down under me those who rose against me.",
      "T": "You were the one who gave me strength for the fight.\nYou brought my enemies down beneath me."
    },
    "40": {
      "L": "You made my enemies turn their backs to me, and I destroyed those who hated me.",
      "M": "You made my enemies turn their backs in retreat, and I destroyed those who hated me.",
      "T": "You made them run.\nI finished off those who hated me."
    },
    "41": {
      "L": "They cried for help, but there was no one to save them; they cried to the LORD, but he did not answer them.",
      "M": "They cried for help, but there was no one to save them—they even cried to the LORD, but he did not answer them.",
      "T": "They screamed for help—no one came.\nThey even called on the LORD, but there was no answer for them."
    },
    "42": {
      "L": "I beat them fine as dust before the wind; I cast them out like the mud of the streets.",
      "M": "I ground them fine as windblown dust; I threw them out like mud from the streets.",
      "T": "I ground them to dust the wind could scatter.\nI threw them away like street filth."
    },
    "43": {
      "L": "You delivered me from strife with the people; you made me the head of the nations; a people whom I had not known served me.",
      "M": "You saved me from conflicts with my own people; you made me head of the nations; people I had not known served me.",
      "T": "You pulled me out of quarrels within my own people\nand set me as head over nations I had never known—\nstrangers who became my subjects."
    },
    "44": {
      "L": "As soon as they heard me they obeyed me; foreigners came cringing to me.",
      "M": "As soon as they heard of me, they obeyed; foreigners submitted to me.",
      "T": "Word of me reached them—and they submitted.\nStrangers came before me in deference."
    },
    "45": {
      "L": "Foreigners lost heart and came trembling from their strongholds.",
      "M": "Foreigners lost their courage and came out of their fortresses trembling.",
      "T": "The fight went out of them.\nThey came stumbling out of their strongholds, shaking."
    },
    "46": {
      "L": "The LORD lives! Blessed be my rock! Exalted be the God of my salvation—",
      "M": "The LORD lives! Blessed be my Rock! Exalted be the God of my salvation—",
      "T": "The LORD is alive!\nHonor to my Rock!\nLet the God who saved me be lifted high—"
    },
    "47": {
      "L": "the God who avenges me and subdues peoples under me,",
      "M": "the God who gives me justice and subdues peoples under me,",
      "T": "the God who settles accounts on my behalf\nand brings nations to their knees before me."
    },
    "48": {
      "L": "who delivered me from my enemies; indeed, you exalted me above those who rose against me; you rescued me from the man of violence.",
      "M": "who rescued me from my enemies—you lifted me above those who rose against me, you saved me from the violent man.",
      "T": "He pulled me out from under my enemies.\nYou raised me above those who came to take me down.\nYou saved me from the violent ones."
    },
    "49": {
      "L": "For this I will praise you, O LORD, among the nations, and sing to your name.",
      "M": "Therefore I will give you thanks, O LORD, among the nations, and sing praises to your name.",
      "T": "This is why I will praise you among all peoples, LORD—\nI will sing your name out loud, everywhere."
    },
    "50": {
      "L": "Great salvation he gives to his king, and shows steadfast love to his anointed, to David and his offspring forever.",
      "M": "He gives great salvation to his king and shows steadfast love to his anointed—to David and his descendants forever.",
      "T": "He gives sweeping victories to his king.\nHe shows steadfast love to his anointed—\nto David and his line, forever and beyond.\nThe covenant holds."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 13–18 written.')

if __name__ == '__main__':
    main()
