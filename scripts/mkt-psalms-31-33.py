"""
MKT Psalms chapters 31–33 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-31-33.py

=== Overview of this unit ===

Ps 31 (24 v) — Individual lament and trust psalm of David. Famous for v5 "Into your
    hand I commit my spirit" — quoted by Jesus from the cross (Luke 23:46) and by
    Stephen at his martyrdom (Acts 7:59). The psalm moves: petition for rescue
    (vv1–4) → commitment of life into God's hands (v5) → rejection of idols and
    trust declaration (vv6–8) → renewed lament in vivid body-language (vv9–13) →
    renewed trust with divine address (vv14–18) → reflection on God's stored-up
    goodness (vv19–20) → personal testimony (vv21–22) → communal call to love and
    courage (vv23–24). The social shame described in vv11–13 (neighbors recoiling,
    friends fleeing, forgotten like the dead) is acute honour-shame culture experience.

Ps 32 (11 v) — A Maskil (H4905, teaching psalm) of David. A wisdom reflection on
    the experience of forgiveness versus the weight of unconfessed sin. Three key
    vocabulary words for sin appear in vv1–2: pesha (H6588, willful transgression),
    chattaah (H2401, sin as missing the mark), and avon (H5771, iniquity/guilt). Paul
    cites vv1–2 in Romans 4:7–8 to ground the doctrine of justification by faith in
    the Psalter: the three covering/lifting terms (nasa, kasah, H2803 lo yachshov)
    map directly onto "righteousness reckoned apart from works." Structurally: twin
    beatitudes (vv1–2) → autobiographical body-memory of unconfessed sin (vv3–4) →
    the turn: confession and instant forgiveness (v5) → teaching in second person
    (vv6–9) → summary contrast (v10) → doxology (v11). Three Selahs at vv4,5,7.

Ps 33 (22 v) — Anonymous communal praise psalm (no superscription). Celebrates the
    LORD as sovereign Creator and protector of his people. Theological spine: God's
    word is the instrument of creation (vv4,6,9 — the echo of Genesis 1 is deliberate);
    God's counsel stands forever against all human strategising (vv10–11); God sees
    everything (vv13–15); human military power is empty (vv16–17); but God's eye is
    on those who fear him (vv18–19). The psalm opens where Ps 32 closes — with the
    call to the righteous to rejoice — and closes with a prayer for steadfast love
    (v22), creating a psalmic link. Notable: v6 uses H7307 (ruach) as "breath" in
    a creation context; v18 and v22 use H2617 (chesed) as the theological anchor.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M throughout. In T:
      "the LORD" — Psalms address the divine name with personal intimacy. Consistent
      with all prior Psalms scripts. No "Yahweh" substitution.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Contextually singular. Ps 31:14 —
      "You are my God" renders the direct-address Elohim naturally.

H7307 (רוּחַ, ruach) — three distinct uses in this unit:
      Ps 31:5 — "my spirit": David's life-breath/inner self committed to God.
        This is the intimate personal use; Jesus and Stephen quote it at death.
        L/M/T: "my spirit." Not wind, not the Spirit of God.
      Ps 32:2 — "in whose spirit there is no deceit": the inner person's integrity.
        L/M/T: "spirit." Consistent with nefesh/ruach Hebrew anthropology.
      Ps 33:6 — "by the breath of his mouth": God's creative breath/wind
        that called the heavens' host into being. Creation context, not personal
        Spirit-presence. L/M/T: "breath." Lowercase; echoes Gen 1:2 intentionally.

H2617 (חֶסֶד, chesed): "steadfast love" in M/T throughout. In L: "steadfast love."
      Occurs at Ps 31:7, 31:16, 31:21, 33:5, 33:18, 33:22. "Lovingkindness" is
      archaic; "mercy" loses the covenantal loyalty dimension. "Steadfast love"
      preserves both the loyalty and the active-kindness senses. Consistent with
      all prior MKT Psalms scripts.

H5315 (נֶפֶשׁ, nefesh): "soul" in L. In M/T: "soul" or "life" by context.
      Ps 31:7,9 — "the distress of my soul / my soul" = anguished embodied self.
      Ps 32:2 — not present; H7307 (ruach) carries the inner-person meaning here.
      Ps 33:19,20 — "their soul / our soul" = embodied persons whose lives God
      watches over. Rendered "life" in 33:19 (context: death/famine rescue) and
      preserved as "soul" in 33:20 (waiting, relational sense).

H835 (אַשְׁרֵי, ashre): "Blessed" in L/M. In T: "Blessed" in Ps 31 (conventional).
      In Ps 32 (double beatitude): T surfaces "Blessed is the person" — the
      ashre formula is a beatitude of congratulation, not a wish. Ps 33:12: "Happy
      is the nation" in T to differentiate the collective from individual blessing.

H6588 (פֶּשַׁע, pesha, Ps 32:1): "transgression" in L/M — willful rebellion against
      authority, not mere moral failure. In T: "rebellion" is used once to make the
      volitional dimension explicit; "transgression" elsewhere.

H5771 (עֲוֹן, avon, Ps 32:1,2,5): "iniquity" in L. In M: "iniquity" or "guilt"
      according to context. Avon carries both the moral crookedness and its
      consequence/guilt. Not collapsed into generic "sin."

H2803 (חָשַׁב, hashab, Ps 32:2): "count" in L. In M: "reckon." This is the
      forensic accounting term Paul quotes in Romans 4. T makes the acquittal
      dimension explicit: "hold accountable." The word is the key to understanding
      why Paul uses this psalm.

H4905 (מַשְׂכִּיל, maskil, Ps 32 superscription): Transliterated "Maskil" in L/M/T.
      Genre designation: a wisdom or teaching psalm, possibly with a special musical
      performance style. LXX renders it as "understanding." Not translated as a
      common noun.

H5542 (סֶלָה, selah, Ps 32:4,5,7): Retained as "Selah" in all tiers. A liturgical
      or musical pause marker; its precise function is uncertain. Not dropped from
      T tier — the interruption is part of the psalm's structure.

H1697 (דָּבָר, dabar, Ps 33:4,6): "word" in L/M/T. The creative word of God through
      which the heavens were made. Echoes the "In the beginning was the Word" register
      but in a Hebrew creation-by-speech context. The dabar/ruach pairing in v6
      parallels Gen 1:1–3 deliberately. T names this echo.

H6218 (עָשׂוֹר, asor, Ps 33:2): "ten strings" in L/M/T. The ten-stringed instrument
      (possibly a harp form). Translating as "psaltery and ten strings" follows the
      interlinear distinction: two instruments are mentioned (nevel + asor), or the
      asor is a description of the nevel. M/T read them as one instrument with a
      specific string count.

=== Aspect and tense notes ===

Ps 31 — The psalm shifts between perfect verbs (completed acts with present force)
    and imperfect/imperative verbs (petition and ongoing action):
    v1 — "I have taken refuge" (H2620, perfect) = completed orientation.
    v5 — "I commit" (H6485, imperfect / entrust-action) = ongoing present act.
    v6 — "I have hated" (H8130, perfect) = completed, lasting rejection.
    v22 — "I said" (H559, perfect) + "you heard" (H8085, perfect) = testimony of
      completed acts forming present confidence.

Ps 32 — The autobiographical section (vv3–5) uses perfects to narrate past
    experience as completed fact: "When I kept silent, my bones wasted away" — not
    a hypothetical but remembered bodily experience. v5 is the decisive turn:
    "I acknowledged / I said / you forgave" — the sequence of confession and
    instant divine response, all perfects. The teaching section (vv6–9) shifts to
    imperfect = ongoing instruction. M/T honor this shift.

Ps 33 — A primarily participial and imperfect psalm: the LORD's character is described
    in present-tense participles (vv4–7) and his sovereign acts in imperfects (vv10–15).
    The concluding verses return to cohortative ("Let our hearts rejoice") and jussive
    ("Let your steadfast love rest on us"). T preserves the doxological present-tense
    force throughout.

=== OT echo notes ===

Ps 31:5 — "Into your hand I commit my spirit": cited verbatim in Luke 23:46 (Jesus)
    and alluded to in Acts 7:59 (Stephen). The T tier preserves the psalm's primary
    sense — David's trust in God with his life — while the NT application extends it
    typologically to the moment of death. No over-reading in T; the verse stands on
    its own.

Ps 32:1–2 — Paul quotes in Romans 4:7–8 to show that David knew a righteousness
    apart from circumcision. The three covering/lifting/non-reckoning terms anticipate
    the Reformation doctrine of justification — but the psalm's primary register is
    experiential (I felt the weight; I confessed; the weight was gone). T honors the
    primary register and lets the Pauline echo be implicit.

Ps 33:6 — "By the word of the LORD the heavens were made, by the breath of his mouth
    all their host": a direct echo of Genesis 1. The dabar (word) and ruach (breath)
    parallel Gen 1:1–3. The Johannine Logos theology (John 1:1–3) stands downstream
    of this tradition. T names the creation-by-speech register.

Ps 33:10–11 — The contrast of human strategy (frustrated) vs. divine counsel (eternal)
    echoes Proverbs 19:21 and anticipates Isaiah 46:10. The wisdom tradition uses
    this as a key axiom. T makes the permanence/futility contrast explicit.
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
  # Psalm 31 — Lament and Trust: "Into Your Hands"
  # ============================================================
  "31": {
    "1": {
      "L": "To the director of music. A Psalm of David. In you, O LORD, I take refuge; let me never be put to shame; in your righteousness deliver me.",
      "M": "For the director of music. A Psalm of David. In you, LORD, I take refuge; let me never be put to shame; rescue me by your righteousness.",
      "T": "To the choirmaster. Of David.\nIn you, LORD, I shelter. Never let me be shamed—\nrescue me in your righteousness."
    },
    "2": {
      "L": "Bow down your ear to me; speedily rescue me. Be a rock of refuge for me, a strong fortress to save me.",
      "M": "Turn your ear to me; quickly rescue me. Be my rock of refuge, a strong fortress to save me.",
      "T": "Lean down and listen.\nBe quick to pull me out.\nBe a rock of refuge for me—a fortress that saves."
    },
    "3": {
      "L": "For you are my rock and my fortress; for your name's sake lead me and guide me.",
      "M": "For you are my rock and my fortress; lead me and guide me for your name's sake.",
      "T": "You are my rock and my fortress.\nFor your own name's sake—lead me, guide me."
    },
    "4": {
      "L": "Pull me out of the net that is hidden for me, for you are my refuge.",
      "M": "Free me from the trap they have secretly set for me, for you are my refuge.",
      "T": "Tear me free from the net they hid for me—\nyou are my strength, my only refuge."
    },
    "5": {
      "L": "Into your hand I commit my spirit; you have redeemed me, O LORD, O faithful God.",
      "M": "Into your hand I commit my spirit; you have redeemed me, LORD, faithful God.",
      "T": "Into your hands I place my spirit—my very breath, my life.\nYou have ransomed me, LORD.\nYou are the God who keeps faith."
    },
    "6": {
      "L": "I hate those who regard worthless vanities; but I trust in the LORD.",
      "M": "I despise those who cling to worthless idols; but I trust in the LORD.",
      "T": "I turn my back on those who pursue empty lies.\nI have staked myself on the LORD."
    },
    "7": {
      "L": "I will rejoice and be glad in your steadfast love, because you have seen my affliction; you have known the distress of my soul;",
      "M": "I will be glad and rejoice in your steadfast love, for you have seen my distress and known the anguish of my soul;",
      "T": "I will be glad—I will sing out—\nbecause your steadfast love holds me.\nYou saw my misery. You knew the anguish I was carrying."
    },
    "8": {
      "L": "you have not handed me over to the enemy; you have set my feet in a broad place.",
      "M": "you did not hand me over to the enemy; you set my feet in a wide-open place.",
      "T": "You did not deliver me into enemy hands.\nYou set my feet in open ground."
    },
    "9": {
      "L": "Be gracious to me, O LORD, for I am in distress; my eye wastes away with grief; my soul and my belly also.",
      "M": "Have mercy on me, LORD, for I am in trouble; my eye wastes with grief—my soul and my body too.",
      "T": "Have mercy on me, LORD—I am collapsing.\nMy eyes have gone dim with grief.\nMy whole self—soul and body—is wasting away."
    },
    "10": {
      "L": "For my life is spent with grief and my years with sighing; my strength fails because of my iniquity, and my bones waste away.",
      "M": "For my life is exhausted by grief and my years by sighing; my strength fails because of my iniquity, and my bones waste away.",
      "T": "My years have dissolved in grief—\na life measured out in sighs.\nMy strength gives out because of what I have done wrong.\nMy bones are going to dust."
    },
    "11": {
      "L": "Among all my enemies I am a reproach, and especially to my neighbors; an object of dread to my acquaintances—those who see me in the street flee from me.",
      "M": "Among all my enemies I am an object of scorn, and especially to my neighbors; those who know me are afraid—when people see me in the street they flee.",
      "T": "My enemies see me and sneer.\nMy neighbors are ashamed of me.\nOld friends are frightened—they cross the street to avoid me."
    },
    "12": {
      "L": "I have been forgotten like a dead man, no longer remembered; I have become like a broken vessel.",
      "M": "I am as forgotten as a dead man; I have become like a shattered clay vessel.",
      "T": "I am as forgotten as a corpse.\nI have become a smashed pot—no use to anyone,\nno longer even remembered."
    },
    "13": {
      "L": "For I hear the whispering of many—terror on every side—as they take counsel together against me, plotting to take away my life.",
      "M": "I hear the rumors of the many—terror surrounds me—as they plot together against me, conspiring to take my life.",
      "T": "I hear the whisper-campaigns all around me.\nTerror on every side.\nThey are meeting together, planning against me—\nall of them scheming to end my life."
    },
    "14": {
      "L": "But I trusted in you, O LORD; I said, 'You are my God.'",
      "M": "But I trusted in you, LORD; I said, 'You are my God.'",
      "T": "But I have trusted in you, LORD.\nI said it then; I say it now: You are my God."
    },
    "15": {
      "L": "My times are in your hand; deliver me from the hand of my enemies and from those who pursue me.",
      "M": "My times are in your hand; rescue me from my enemies and from those who pursue me.",
      "T": "Every moment of my life belongs to you.\nPull me out of their hands—\nout of the grip of my enemies and everyone hunting me down."
    },
    "16": {
      "L": "Make your face to shine upon your servant; save me in your steadfast love.",
      "M": "Make your face shine on your servant; save me through your steadfast love.",
      "T": "Let your face shine on me, your servant.\nSave me—with that steadfast love of yours."
    },
    "17": {
      "L": "O LORD, let me not be put to shame, for I have called on you; let the wicked be put to shame; let them go silent to Sheol.",
      "M": "LORD, let me not be put to shame, for I have called on you; let the wicked be ashamed—let them go silently down to Sheol.",
      "T": "Do not let me be shamed, LORD—I have called on you.\nLet it be the wicked who carry shame.\nLet them go silently into the grave."
    },
    "18": {
      "L": "Let the lying lips be silenced—which speak arrogantly against the righteous with pride and contempt.",
      "M": "Let the lying lips be struck silent—lips that speak against the righteous with arrogance and contempt.",
      "T": "Silence those lying mouths\nthat speak against the righteous\nwith such breathtaking arrogance and contempt."
    },
    "19": {
      "L": "Oh, how great is your goodness, which you have stored up for those who fear you and worked for those who take refuge in you, in the sight of all people!",
      "M": "How great is your goodness, which you have stored up for those who fear you and displayed for those who take shelter in you, in full view of everyone!",
      "T": "What abundance you have stored away\nfor those who revere you!\nWhat you have done openly, before every watching eye,\nfor those who shelter in you—"
    },
    "20": {
      "L": "In the shelter of your presence you hide them from the schemes of men; you conceal them in your pavilion from the strife of tongues.",
      "M": "In the shelter of your presence you hide them from human plots; you conceal them in your tent from the quarreling of tongues.",
      "T": "You hide them in the secret place of your own presence—\nsafe from human plotting.\nYou shelter them from the wars that words can make."
    },
    "21": {
      "L": "Blessed be the LORD, for he has shown his wonderful steadfast love to me in a besieged city.",
      "M": "Praise the LORD, for he displayed his wonderful steadfast love to me when I was like a man in a besieged city.",
      "T": "Praise the LORD!\nHe showed me the wonders of his steadfast love\nwhen I was trapped—a city under siege."
    },
    "22": {
      "L": "I said in my alarm, 'I am cut off from before your eyes.' But you heard the voice of my pleas when I cried to you.",
      "M": "I said in my panic, 'I am cut off from your sight.' Yet you heard my cries for mercy when I called to you.",
      "T": "In my panic I said, 'I am completely cut off—beyond your sight.'\nBut you heard me.\nYou heard my desperate plea."
    },
    "23": {
      "L": "Love the LORD, all you his faithful ones! The LORD preserves the faithful and repays the arrogant doer in full.",
      "M": "Love the LORD, all you his faithful people! The LORD protects the faithful and pays back the proud in full.",
      "T": "Love the LORD, all his faithful ones!\nHe protects everyone who is loyal to him—\nand the arrogant get paid back in full, not a shekel short."
    },
    "24": {
      "L": "Be strong, and let your heart take courage, all you who wait for the LORD!",
      "M": "Be strong, and let your heart be courageous, all you who hope in the LORD!",
      "T": "Be strong. Let your heart take courage.\nAll of you who have placed your hope in the LORD."
    }
  },

  # ============================================================
  # Psalm 32 — Maskil of David: The Weight Lifted
  # ============================================================
  "32": {
    "1": {
      "L": "A Maskil of David. Blessed is the one whose transgression is lifted, whose sin is covered.",
      "M": "A Maskil of David. Blessed is the one whose transgression is forgiven, whose sin is covered.",
      "T": "A Maskil—of David.\nBlessed is the person whose rebellion has been lifted away—\nwhose sin God has covered over."
    },
    "2": {
      "L": "Blessed is the man against whom the LORD does not count iniquity, and in whose spirit there is no deceit.",
      "M": "Blessed is the man to whom the LORD does not reckon iniquity, and in whose spirit there is no deceit.",
      "T": "Blessed is the one the LORD does not hold accountable for wrongdoing—\nwho has also stopped deceiving themselves."
    },
    "3": {
      "L": "When I kept silent, my bones wasted away through my groaning all day long.",
      "M": "When I kept silent about my sin, my bones wasted away through my constant groaning.",
      "T": "When I said nothing—kept it locked inside—\nmy bones deteriorated.\nAll day long I groaned."
    },
    "4": {
      "L": "For day and night your hand was heavy upon me; my moisture dried up as in the heat of summer. Selah",
      "M": "Day and night your hand pressed down on me; my strength dried up like moisture in the summer heat. Selah",
      "T": "Day and night your hand pressed down hard on me.\nMy vitality evaporated—as in a scorching summer.\nSelah."
    },
    "5": {
      "L": "I acknowledged my sin to you and did not cover my iniquity; I said, 'I will confess my transgressions to the LORD,' and you forgave the iniquity of my sin. Selah",
      "M": "I made my sin known to you and did not hide my iniquity; I said, 'I will confess my transgressions to the LORD,' and you forgave the guilt of my sin. Selah",
      "T": "I stopped hiding.\nI laid my sin open before you.\nI said: I am going to confess what I have done against you, LORD—\nand the moment I did, you lifted the guilt of it all.\nSelah."
    },
    "6": {
      "L": "Therefore let all the godly pray to you while you may be found; when the great flood of waters comes, they shall not reach him.",
      "M": "Therefore let every faithful person pray to you while you may still be found; when the great floodwaters surge, they will not reach them.",
      "T": "So let every person who is faithful pray to you while there is still time—\nbefore the floodwaters rise.\nWhen the great surge comes, it will not reach them."
    },
    "7": {
      "L": "You are a hiding place for me; you preserve me from trouble; you surround me with shouts of deliverance. Selah",
      "M": "You are my hiding place; you guard me from trouble; you surround me with songs of rescue. Selah",
      "T": "You are where I hide.\nYou shield me from danger.\nYou encircle me with cries of rescue.\nSelah."
    },
    "8": {
      "L": "I will instruct you and teach you in the way you should go; I will counsel you with my eye upon you.",
      "M": "I will instruct you and show you the way you should walk; I will guide you with my eye on you.",
      "T": "I will teach you.\nI will show you the road you should take.\nMy eye will be on you as I guide you."
    },
    "9": {
      "L": "Be not like a horse or a mule, without understanding, which must be bridled with bit and bridle; else it will not approach you.",
      "M": "Do not be like a horse or mule that lacks understanding and must be controlled with bit and bridle, or it will not come near you.",
      "T": "Don't be a horse or mule—animals with no understanding\nwho have to be forced into line with bit and bridle.\nDon't make God drag you."
    },
    "10": {
      "L": "Many are the sorrows of the wicked, but steadfast love surrounds the one who trusts in the LORD.",
      "M": "The wicked have many sorrows, but steadfast love surrounds those who trust in the LORD.",
      "T": "The wicked carry a heavy weight of their own sorrows.\nBut those who trust in the LORD are encircled by steadfast love."
    },
    "11": {
      "L": "Be glad in the LORD and rejoice, O righteous! Shout for joy, all you who are upright in heart!",
      "M": "Be glad in the LORD and rejoice, you righteous people! Shout for joy, all who are upright in heart!",
      "T": "Celebrate! Sing out!\nYou who live right before God—let the shout rise from you.\nAll of you with honest hearts—raise the noise."
    }
  },

  # ============================================================
  # Psalm 33 — Communal Praise: Creator, Sovereign, Protector
  # ============================================================
  "33": {
    "1": {
      "L": "Rejoice in the LORD, O you righteous! Praise is fitting for the upright.",
      "M": "Shout for joy in the LORD, you righteous! Praise is beautiful from those who are upright.",
      "T": "Sing out to the LORD, you righteous ones—\npraise sits beautifully on those who live right."
    },
    "2": {
      "L": "Give thanks to the LORD with the lyre; sing praises to him with the harp of ten strings.",
      "M": "Praise the LORD with the lyre; make music to him with the ten-stringed harp.",
      "T": "Play the lyre and give thanks.\nPull music from the ten-stringed harp and praise him."
    },
    "3": {
      "L": "Sing to him a new song; play skillfully, with a loud shout of joy.",
      "M": "Sing him a new song; play with skill and shout for joy.",
      "T": "Sing him something new.\nPlay with all the craft you have—\nand let the shout of joy go out."
    },
    "4": {
      "L": "For the word of the LORD is right, and all his works are done in faithfulness.",
      "M": "For the word of the LORD is right and true; all his works are done in faithfulness.",
      "T": "The LORD's word is straight and clean.\nEverything he does is done with perfect faithfulness."
    },
    "5": {
      "L": "He loves righteousness and justice; the earth is full of the steadfast love of the LORD.",
      "M": "He loves righteousness and justice; the earth is full of the LORD's steadfast love.",
      "T": "He is in love with righteousness and justice.\nThe whole earth is saturated with his steadfast love."
    },
    "6": {
      "L": "By the word of the LORD the heavens were made, and by the breath of his mouth all their host.",
      "M": "The heavens were made by the word of the LORD, and all their host by the breath of his mouth.",
      "T": "God spoke—and the heavens came into being.\nHis breath, the breath of his mouth, brought every star into existence.\nThis is the same speech that began all things in Genesis."
    },
    "7": {
      "L": "He gathers the waters of the sea as a heap; he puts the deeps in storehouses.",
      "M": "He gathers the sea's waters like a heap; he stores the deep in reservoirs.",
      "T": "He heaps the oceans up like something stacked and measured.\nHe stores the depths as though in a treasury."
    },
    "8": {
      "L": "Let all the earth fear the LORD; let all the inhabitants of the world stand in awe of him.",
      "M": "Let all the earth fear the LORD; let all who live in the world stand in awe of him.",
      "T": "Let every creature on earth hold the LORD in reverence.\nLet every human being stand in awe of him."
    },
    "9": {
      "L": "For he spoke, and it came to be; he commanded, and it stood firm.",
      "M": "For he spoke, and it came to be; he commanded, and it stood firm.",
      "T": "He spoke—and it was.\nHe commanded—and it held."
    },
    "10": {
      "L": "The LORD brings the counsel of the nations to nothing; he frustrates the plans of the peoples.",
      "M": "The LORD thwarts the purposes of the nations; he brings the plans of the peoples to nothing.",
      "T": "The LORD dismantles the strategies of nations.\nEvery people's long-laid plan—he foils it."
    },
    "11": {
      "L": "The counsel of the LORD stands forever, the thoughts of his heart to all generations.",
      "M": "The counsel of the LORD stands forever, the purposes of his heart through all generations.",
      "T": "But the LORD's own counsel stands—unshaken, permanent.\nWhat he purposes in his heart holds across every generation."
    },
    "12": {
      "L": "Blessed is the nation whose God is the LORD, the people he has chosen as his heritage.",
      "M": "Blessed is the nation whose God is the LORD—the people he has chosen as his own possession.",
      "T": "Happy is the nation whose God is the LORD—\nthe people he has chosen to be his own possession."
    },
    "13": {
      "L": "The LORD looks down from heaven; he beholds all the children of man;",
      "M": "The LORD looks down from heaven; he observes all humanity;",
      "T": "From heaven the LORD looks down—\nhe sees every human being."
    },
    "14": {
      "L": "from the place of his dwelling he looks out on all the inhabitants of the earth,",
      "M": "from his dwelling place he surveys all who live on the earth,",
      "T": "From where he sits, he looks out\nover everyone living on this planet."
    },
    "15": {
      "L": "he who fashions the hearts of all and considers all their works.",
      "M": "he who forms the hearts of all and considers everything they do.",
      "T": "He is the one who formed each heart—\nand he pays attention to everything each person does."
    },
    "16": {
      "L": "The king is not saved by his great army; a warrior is not delivered by his great strength.",
      "M": "No king is saved by the size of his army; no warrior is rescued by his own great strength.",
      "T": "No king survives by the size of his army.\nNo warrior escapes by sheer physical power."
    },
    "17": {
      "L": "The horse is a false hope for safety; it cannot deliver by its great strength.",
      "M": "A horse is a vain hope for victory; its great power cannot bring rescue.",
      "T": "A war-horse is an empty promise of safety.\nAll its power will not save you."
    },
    "18": {
      "L": "Behold, the eye of the LORD is on those who fear him, on those who hope in his steadfast love,",
      "M": "The eye of the LORD is on those who fear him, on those who hope in his steadfast love,",
      "T": "But look: the LORD's eye is fixed on those who revere him—\non those who have placed their hope in his steadfast love."
    },
    "19": {
      "L": "to deliver their soul from death and to keep them alive in famine.",
      "M": "to rescue them from death and to keep them alive in famine.",
      "T": "He watches to rescue them from death—\nto keep them breathing even when the land starves."
    },
    "20": {
      "L": "Our soul waits for the LORD; he is our help and our shield.",
      "M": "We wait for the LORD; he is our help and our shield.",
      "T": "We are waiting for the LORD.\nHe is our help and our shield—we have nothing else."
    },
    "21": {
      "L": "For our heart is glad in him, because we have trusted in his holy name.",
      "M": "Our hearts are glad in him, for we trust in his holy name.",
      "T": "Our hearts are full of joy in him—\nbecause we have staked ourselves on his holy name."
    },
    "22": {
      "L": "Let your steadfast love, O LORD, be upon us, even as we hope in you.",
      "M": "Let your steadfast love, LORD, rest on us, as we have placed our hope in you.",
      "T": "LORD, let your steadfast love rest on us—\nthe same measure as the hope we have placed in you."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 31–33 written.')

if __name__ == '__main__':
    main()
