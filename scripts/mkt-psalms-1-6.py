"""
MKT Psalms chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-1-6.py

=== Overview of this unit ===

Psalms 1–6 open the Psalter with two carefully placed gateway psalms (1 and 2),
then move into a cluster of Davidic laments (3–6).

Ps 1  — The Two Ways (6 verses): Wisdom introduction to the whole Psalter.
         Perfect antithetical parallelism: the righteous vs. the wicked. No divine speech;
         describes the LORD in third person. The tree image is a classic ANE symbol of
         flourishing under divine favour (cf. Jer 17:7–8).

Ps 2  — The Messianic King (12 verses): A royal enthronement psalm, widely cited in
         the NT as messianic (Acts 4:25–26; Heb 1:5; Rev 2:27). The nations' rebellion is
         absurd before the enthroned LORD. The decree of divine sonship (v7) activates the
         royal covenant. "Kiss the Son" (v12) uses the Aramaic בַּר (bar), a rarity in
         Hebrew poetry — may be a dialect form or later scribal tradition.

Ps 3  — Flight from Absalom (8 verses): The first psalm with a superscription linking it
         to a historical event (2 Sam 15). An individual lament moving to confident trust.
         Three occurrences of "Selah" — a musical/liturgical marker, meaning uncertain
         (perhaps "pause," "crescendo," or "forever"). Retained as "Selah" in all tiers.

Ps 4  — Evening prayer (8 verses): An individual lament addressed partly to God, partly
         to adversaries. The phrase "Stand in awe and sin not" (v4) is quoted by Paul in
         Eph 4:26 ("Be angry and do not sin"). Moves from complaint to rest and security.

Ps 5  — Morning prayer (12 verses): An individual lament. The psalmist's confidence in
         his own integrity contrasts with the detailed wickedness of enemies (vv9–10).
         H2617 חֶסֶד appears in v7 — "steadfast love" (covenant faithfulness + active
         kindness). The Nehiloth superscription (v1) likely refers to flutes.

Ps 6  — A penitential psalm (10 verses): The first of the seven penitential psalms
         (6, 32, 38, 51, 102, 130, 143). An individual in physical and spiritual agony
         pleads for healing. The turn in vv8–10 from lament to confidence is abrupt and
         total — the LORD's hearing is stated as past fact, shifting the psalmist's posture.

=== Superscriptions ===

Hebrew psalm superscriptions are canonical text and appear as the first verse in the MT
numbering (or as an introductory header). In this script they are merged into v1 of each
psalm. Psalms 1 and 2 lack superscriptions in MT.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M throughout, following small-caps convention. In T
      tier: "the LORD" — rendered consistently, not as "Yahweh," to maintain the liturgical
      voice of Psalms rather than signalling a fresh contextual decision in each verse.
      Deviation note: Ps 2 T tier v7 surfaces the covenantal weight of the name without
      switching to "Yahweh."

H430  (אֱלֹהִים, Elohim): "God" in all tiers. The Psalter uses both names; context
      governs which is primary in a given psalm. Elohim is used unambiguously as the
      divine name here (not the generic "divine beings" sense).

H7307 (רוּחַ, ruach): In Ps 1:4 the physical sense — "wind" — is unambiguous from
      context (wind driving chaff). Lowercase, physical. This is NOT the Spirit-of-God
      sense that appears in other OT contexts. No capitalisation.

H2617 (חֶסֶד, hesed): "Steadfast love" in all three tiers (Ps 5:7, 6:4). This is the
      standard MKT rendering. Hesed combines covenant loyalty with active, tender
      kindness — no single English word captures it, but "steadfast love" gets closer
      than "mercy" or "kindness" alone. In L tier "steadfast love" is used even though it
      is not word-for-word, because any alternative (mercy, lovingkindness) loses the
      covenantal dimension.

H5315 (נֶפֶשׁ, nefesh): "Soul" in L/M in most occurrences. In T tier: "life" or "whole
      being" when the context emphasises the embodied, vital self (Ps 3:2; 6:3–4) rather
      than a Greek-style immaterial soul. Hebrew nefesh is the whole person as a living
      being. The translation preserves this by choosing the more embodied rendering in T.

H8451 (תּוֹרָה, torah): "law" in L; "instruction" or "teaching" in M/T for Ps 1:2.
      Torah is the divine teaching/instruction given to Israel, not merely legal code.
      The meditative quality of v2 ("meditates day and night") fits "instruction/teaching"
      better than "law," which has a purely juridical feel in English.

H835  (אַשְׁרֵי, ashre): "Blessed" in L/M. The form is plural noun ("blessings of"),
      an exclamation of congratulation rather than a priestly benediction. In T tier
      rendered "O the blessedness of" (Ps 1:1) and "How blessed" (Ps 2:12) to surface
      the exclamatory force.

H4899 (מָשִׁיחַ, mashiach): "Anointed" in L; "Anointed One" in M; "his Anointed One" or
      "the Anointed One" in T. Not "Messiah" (that is the later title); the base word is
      the Hebrew participle for "one who has been anointed." The NT messianic application
      is carried by the T tier's phrasing, not by anachronistic capitalisation.

H1248 (בַּר, bar, Ps 2:12): "Son" in all tiers. This is Aramaic for "son" (vs. Hebrew
      H1121 בֵּן ben). The presence of Aramaic bar in a Hebrew poem is unusual; scholars
      debate whether it is an Aramaism, a divine title, or a textual variant. The
      rendering "Kiss the Son" follows LXX and the dominant exegetical tradition. Noted
      here as a textual peculiarity.

H7563 (רָשָׁע, rasha): "Wicked" in all tiers. The consistent MKT rendering. KJV's
      "ungodly" is avoided; it loses the active moral connotation of rasha, which is not
      simply the absence of piety but the presence of moral wrong.

H5542 (סֶלָה, selah): Retained as "Selah" in all three tiers. Its meaning is unknown
      (musical pause? crescendo? "forever"?). Removing it or glossing it would be a
      decision the text has not authorised.

H4941 (מִשְׁפָּט, mishpat): "Judgment" in L; "judgment" in M; "judgment" or the forensic
      sense of "verdict" in T as context warrants. In Ps 1:5 the assembly/congregation
      of the righteous that the wicked cannot enter at the mishpat is likely the eschatological
      judgment assembly, not merely a local legal proceeding.

H2620 (חָסָה, hasah): "Take refuge" in all tiers (Ps 2:12; 5:11). The verb describes
      running under divine protection for shelter — not passive trust but active seeking
      of cover. The noun form would be "refuge."

H136  (אֲדֹנָי, Adonai): "Lord" (initial cap only) in L/M — distinguished from H3068
      LORD by the capitalisation difference. In Ps 2:4, the term is Adonai, not YHWH,
      though both refer to the same God. T uses "the Lord God" to make the weight clear.

=== Hebrew poetic structure notes ===

In T tier, line breaks (\n) mark the boundaries of cola (half-lines) in bicola/tricola
structures. Psalm 1 is structured as two antithetical strophes (vv1–3 positive; vv4–6
negative), with v6 as the summary couplet. Psalm 2 shifts from third-person narrative
to direct speech and back. Psalms 3–6 follow individual lament structure:
invocation → complaint → trust → petition → confidence.

The T tier surfaces the Hebrew parallelism by preserving line structure. Where the
Hebrew has a bicolon (A // B), T renders two lines. The L and M tiers use prose.
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
  "1": {
    "1": {
      "L": "Blessed is the man who walks not in the counsel of the wicked, nor stands in the way of sinners, nor sits in the seat of scoffers.",
      "M": "Blessed is the man who does not walk in the counsel of the wicked, nor stand in the way of sinners, nor sit in the seat of scoffers.",
      "T": "O the blessedness of the one\nwho does not walk by the counsel of the wicked,\nwho does not linger in the path of sinners,\nwho does not take a seat among the scornful."
    },
    "2": {
      "L": "But in the instruction of the LORD is his delight, and in his instruction he meditates day and night.",
      "M": "But his delight is in the instruction of the LORD, and on his instruction he meditates day and night.",
      "T": "His heart finds its delight in the LORD's teaching,\nand on that teaching he ponders\nby day and through the night."
    },
    "3": {
      "L": "And he shall be like a tree planted by rivers of water, that brings forth its fruit in its season; and its leaf does not wither; and in all that he does he prospers.",
      "M": "He is like a tree planted by streams of water that yields its fruit in its season, and its leaf does not wither. In all that he does, he prospers.",
      "T": "He is like a tree\nrooted by channels of water—\nbearing fruit in every season,\nits leaves never failing—\nand whatever he undertakes thrives."
    },
    "4": {
      "L": "The wicked are not so, but are like the chaff which the wind drives away.",
      "M": "The wicked are not so, but are like chaff that the wind drives away.",
      "T": "The wicked are nothing like this:\nthey are like chaff the wind scatters."
    },
    "5": {
      "L": "Therefore the wicked shall not stand in the judgment, nor sinners in the congregation of the righteous.",
      "M": "Therefore the wicked shall not stand in the judgment, nor sinners in the assembly of the righteous.",
      "T": "So the wicked will not hold their ground when judgment comes,\nnor will sinners find a place in the company of the righteous."
    },
    "6": {
      "L": "For the LORD knows the way of the righteous, but the way of the wicked shall perish.",
      "M": "For the LORD watches over the way of the righteous, but the way of the wicked will perish.",
      "T": "For the LORD knows and guards the path of the righteous,\nbut the road the wicked travel leads to ruin."
    }
  },
  "2": {
    "1": {
      "L": "Why do the nations rage, and the peoples meditate a vain thing?",
      "M": "Why do the nations rage, and the peoples plot in vain?",
      "T": "Why this uproar among the nations?\nWhy do the peoples hatch their empty schemes?"
    },
    "2": {
      "L": "The kings of the earth set themselves, and the rulers take counsel together against the LORD and against his Anointed, saying:",
      "M": "The kings of the earth rise up, and the rulers conspire together against the LORD and against his Anointed One.",
      "T": "Earth's kings take their stand;\nits rulers band together—\nagainst the LORD and against his Anointed One."
    },
    "3": {
      "L": "\"Let us burst their bonds asunder and cast away their cords from us.\"",
      "M": "\"Let us tear apart their bonds and throw off their cords from us.\"",
      "T": "\"We will shatter the fetters they have laid on us\nand hurl their restraints away!\""
    },
    "4": {
      "L": "He who sits in the heavens laughs; the Lord holds them in derision.",
      "M": "He who sits in the heavens laughs; the Lord scoffs at them.",
      "T": "The one enthroned in heaven laughs;\nthe Lord God mocks their scheming."
    },
    "5": {
      "L": "Then he will speak to them in his wrath and terrify them in his fury:",
      "M": "Then he will speak to them in his wrath and terrify them in his burning anger:",
      "T": "Then in his fury he rebukes them,\nstartling them with the blaze of his wrath:"
    },
    "6": {
      "L": "\"Yet I have set my King on Zion, my holy hill.\"",
      "M": "\"But I have installed my King on Zion, my holy hill.\"",
      "T": "\"Yet I have enthroned my King\non Zion, my holy mountain.\""
    },
    "7": {
      "L": "I will declare the decree: the LORD said to me, 'You are my Son; today I have begotten you.'",
      "M": "I will proclaim the LORD's decree: he said to me, 'You are my Son; today I have begotten you.'",
      "T": "Let me announce the LORD's decree:\nHe said to me, 'You are my Son;\nthis very day I have fathered you.'"
    },
    "8": {
      "L": "Ask of me, and I will give the nations as your heritage, and the ends of the earth as your possession.",
      "M": "Ask me, and I will give the nations as your inheritance and the ends of the earth as your possession.",
      "T": "Ask it of me, and the nations become your inheritance;\nthe farthest reaches of the earth are yours."
    },
    "9": {
      "L": "You shall break them with a rod of iron and dash them in pieces like a potter's vessel.",
      "M": "You shall rule them with an iron rod and shatter them like a clay vessel.",
      "T": "You will shatter them with an iron scepter\nand smash them like a potter's jar."
    },
    "10": {
      "L": "Now therefore, O kings, be wise; be warned, O rulers of the earth.",
      "M": "Now then, be wise, O kings; take warning, O rulers of the earth.",
      "T": "Therefore, kings, act wisely;\nheed the warning, all you who govern the earth."
    },
    "11": {
      "L": "Serve the LORD with fear, and rejoice with trembling.",
      "M": "Serve the LORD with reverent fear, and celebrate with trembling.",
      "T": "Serve the LORD in holy awe\nand rejoice before him with trembling."
    },
    "12": {
      "L": "Kiss the Son, lest he be angry, and you perish in the way, when his wrath is kindled but a little. Blessed are all who take refuge in him.",
      "M": "Pay homage to the Son, lest he be angry and you perish from his path, for his wrath can ignite quickly. Blessed are all who take refuge in him.",
      "T": "Do homage to the Son before his anger kindles—\nfor that wrath can flare in a moment.\nHow blessed are all who shelter in him."
    }
  },
  "3": {
    "1": {
      "L": "A Psalm of David, when he fled from Absalom his son. O LORD, how many are my foes! Many are rising against me.",
      "M": "A Psalm of David, when he fled from Absalom his son. O LORD, how many are my foes! Many are rising against me.",
      "T": "A Psalm of David — written when he fled from Absalom his son.\n\nLORD, how countless my enemies have become!\nHow many rise up against me!"
    },
    "2": {
      "L": "Many are saying of my soul, 'There is no salvation for him in God.' Selah",
      "M": "Many are saying of me, 'There is no salvation for him in God.' Selah",
      "T": "On every side the word goes round:\n'God will not rescue this one.' Selah"
    },
    "3": {
      "L": "But you, O LORD, are a shield about me, my glory, and the lifter of my head.",
      "M": "But you, O LORD, are a shield around me, my glory, and the one who lifts my head.",
      "T": "But you, LORD, surround me like a shield—\nyou are my honor, the one who holds my head high."
    },
    "4": {
      "L": "I cried aloud to the LORD, and he answered me from his holy hill. Selah",
      "M": "I cried out to the LORD, and he answered me from his holy hill. Selah",
      "T": "I called out to the LORD,\nand he answered from his holy mountain. Selah"
    },
    "5": {
      "L": "I lay down and slept; I awoke, for the LORD sustained me.",
      "M": "I lay down and slept; I awoke again, for the LORD sustained me.",
      "T": "I lay down and slept,\nand woke again—\nbecause the LORD held me safe."
    },
    "6": {
      "L": "I will not be afraid of ten thousands of people who have set themselves against me all around.",
      "M": "I will not fear the tens of thousands who have surrounded me on every side.",
      "T": "Though ten thousand enemies encamp around me,\nI will not be afraid."
    },
    "7": {
      "L": "Arise, O LORD! Save me, O my God! For you strike all my enemies on the cheek; you break the teeth of the wicked.",
      "M": "Rise up, O LORD! Save me, O my God! For you strike all my enemies on the cheek; you shatter the teeth of the wicked.",
      "T": "Rise up, LORD! Rescue me, my God!\nFor you strike my enemies across the face\nand snap the teeth of the wicked."
    },
    "8": {
      "L": "Salvation belongs to the LORD; your blessing be upon your people. Selah",
      "M": "Salvation belongs to the LORD; your blessing be upon your people. Selah",
      "T": "Deliverance belongs to the LORD alone—\nmay your blessing rest upon your people. Selah"
    }
  },
  "4": {
    "1": {
      "L": "To the choirmaster: with stringed instruments. A Psalm of David. Answer me when I call, O God of my righteousness! You have relieved me when I was in distress. Be gracious to me and hear my prayer.",
      "M": "To the choirmaster: with stringed instruments. A Psalm of David. Answer me when I call, O God of my righteousness! You have freed me when I was in distress. Be gracious to me and hear my prayer.",
      "T": "To the worship leader: for stringed instruments. A Psalm of David.\n\nAnswer me when I call, O God who vindicates me!\nYou opened a way out when I was hemmed in.\nBe merciful to me now and hear my prayer."
    },
    "2": {
      "L": "O sons of men, how long shall my honor be turned to shame? How long will you love vanity and seek after lies? Selah",
      "M": "O men, how long will you turn my honor to shame? How long will you love what is worthless and pursue lies? Selah",
      "T": "You people—how long will you make my honor a target for contempt?\nHow long will you chase after empty things and run after what is false? Selah"
    },
    "3": {
      "L": "But know that the LORD has set apart the godly for himself; the LORD hears when I call to him.",
      "M": "But know that the LORD has set apart the faithful for himself; the LORD hears when I call to him.",
      "T": "Know this: the LORD has claimed the faithful as his own;\nhe hears me when I call."
    },
    "4": {
      "L": "Stand in awe, and sin not; commune with your own heart upon your bed, and be still. Selah",
      "M": "Tremble with awe and do not sin; search your hearts in silence on your beds. Selah",
      "T": "Let holy fear hold you—and do not sin.\nPonder your ways in the quiet of the night,\nand be still. Selah"
    },
    "5": {
      "L": "Offer the sacrifices of righteousness, and put your trust in the LORD.",
      "M": "Offer right sacrifices, and put your trust in the LORD.",
      "T": "Bring honest offerings to God\nand anchor your hope in the LORD."
    },
    "6": {
      "L": "There are many who say, 'Who will show us any good?' Lift up the light of your face upon us, O LORD!",
      "M": "Many say, 'Who will show us any good?' Let the light of your face shine on us, O LORD!",
      "T": "People ask, 'Where will we find any good?'\nLet your face shine on us, LORD—that is the only answer."
    },
    "7": {
      "L": "You have put more joy in my heart than they have when their grain and wine abound.",
      "M": "You have placed more joy in my heart than they have when their grain and wine overflow.",
      "T": "The gladness you have placed in my heart\nexceeds all they feel when the harvest overflows."
    },
    "8": {
      "L": "In peace I will both lie down and sleep; for you alone, O LORD, make me dwell in safety.",
      "M": "In peace I will lie down and sleep, for you alone, O LORD, make me dwell in safety.",
      "T": "I lie down and fall asleep in peace,\nfor you alone, LORD, let me rest secure."
    }
  },
  "5": {
    "1": {
      "L": "To the choirmaster: for the flutes. A Psalm of David. Give ear to my words, O LORD; consider my groaning.",
      "M": "To the choirmaster: for the flutes. A Psalm of David. Give ear to my words, O LORD; consider my groaning.",
      "T": "To the worship leader: for flutes. A Psalm of David.\n\nListen to my words, O LORD;\nhear the sounds beneath them—the sighing I cannot fully voice."
    },
    "2": {
      "L": "Give attention to the sound of my cry, my King and my God, for to you do I pray.",
      "M": "Attend to the sound of my cry, my King and my God, for to you I pray.",
      "T": "Hear my cry for help, my King and my God—\nit is to you alone I bring my prayer."
    },
    "3": {
      "L": "O LORD, in the morning you hear my voice; in the morning I direct my prayer to you and watch.",
      "M": "O LORD, in the morning you hear my voice; in the morning I lay my prayer before you and wait.",
      "T": "At dawn my voice reaches you, LORD;\nI lay my prayer before you at first light\nand watch for your answer."
    },
    "4": {
      "L": "For you are not a God who delights in wickedness; evil will not dwell with you.",
      "M": "For you are not a God who takes pleasure in wickedness; evil cannot dwell with you.",
      "T": "You are a God who takes no pleasure in evil;\nwickedness finds no welcome in your presence."
    },
    "5": {
      "L": "The boastful shall not stand before your eyes; you hate all workers of iniquity.",
      "M": "The arrogant cannot stand in your sight; you hate all who practice evil.",
      "T": "Arrogance cannot survive your gaze;\nyou despise all who live by lawlessness."
    },
    "6": {
      "L": "You destroy those who speak lies; the LORD abhors the bloodthirsty and deceitful man.",
      "M": "You destroy those who speak falsehood; the LORD abhors the violent and the deceitful.",
      "T": "You bring ruin on every liar;\nthe LORD detests those whose hands are bloodstained\nand whose tongue trades in deceit."
    },
    "7": {
      "L": "But I, through the abundance of your steadfast love, will enter your house; I will bow down toward your holy temple in the fear of you.",
      "M": "But I, through the abundance of your steadfast love, will come into your house. I will bow down toward your holy temple in reverence of you.",
      "T": "But I—through the flood of your steadfast love—\nI will enter your house.\nI bow toward your holy temple in the fear that becomes me."
    },
    "8": {
      "L": "Lead me, O LORD, in your righteousness because of my enemies; make your way straight before me.",
      "M": "Lead me, O LORD, in your righteousness because of those who lie in wait for me; make your way level before me.",
      "T": "Guide me in your righteousness, LORD,\nbecause my enemies watch for any misstep;\nsmooth your path so it runs straight before me."
    },
    "9": {
      "L": "For there is no truth in their mouth; their inmost self is destruction; their throat is an open grave; they flatter with their tongue.",
      "M": "For there is nothing reliable in their mouth; their inward part is ruin; their throat is an open grave; they flatter with their tongue.",
      "T": "No word of theirs can be trusted;\ntheir hearts are a wasteland;\ntheir throat gapes like an open grave;\nsmooth words flow from a tongue that deceives."
    },
    "10": {
      "L": "Make them bear their guilt, O God; let them fall by their own counsels; cast them out in the abundance of their transgressions, for they have rebelled against you.",
      "M": "Hold them guilty, O God; let them fall by their own schemes; drive them away for the multitude of their rebellions, for they have defied you.",
      "T": "Declare them guilty, O God;\nlet their own plots be their downfall.\nCast them out for all their lawless deeds—\nthey have risen in open revolt against you."
    },
    "11": {
      "L": "But let all who take refuge in you rejoice; let them shout for joy forever. You shelter them, and those who love your name exult in you.",
      "M": "But let all who take refuge in you rejoice; let them shout for joy forever. Spread your protection over them, and let those who love your name exult in you.",
      "T": "But let everyone who shelters in you burst into song;\nlet them shout their joy without end.\nYou spread your covering over them—\nand all who love your name exult in your presence."
    },
    "12": {
      "L": "For you, O LORD, bless the righteous; you cover him with favor as with a shield.",
      "M": "For you, O LORD, bless the righteous; you surround him with favor as with a shield.",
      "T": "For you, LORD, bless the one who is right with you;\nyou wrap him in your favor like a shield."
    }
  },
  "6": {
    "1": {
      "L": "To the choirmaster: with stringed instruments, according to the Sheminith. A Psalm of David. O LORD, do not rebuke me in your anger, nor discipline me in your wrath.",
      "M": "To the choirmaster: with stringed instruments, according to the Sheminith. A Psalm of David. O LORD, do not rebuke me in your anger, nor discipline me in your fury.",
      "T": "To the worship leader: for stringed instruments, the eighth. A Psalm of David.\n\nLORD, do not correct me in your fury;\ndo not discipline me when your anger is burning."
    },
    "2": {
      "L": "Be gracious to me, O LORD, for I am languishing; heal me, O LORD, for my bones are troubled.",
      "M": "Be gracious to me, O LORD, for I am weak; heal me, O LORD, for my bones are in agony.",
      "T": "Have mercy on me, LORD—I am utterly spent;\nheal me, LORD, for my very bones ache with dread."
    },
    "3": {
      "L": "My soul also is greatly troubled. But you, O LORD—how long?",
      "M": "My whole being is deeply troubled. But you, O LORD—how long?",
      "T": "My whole self is shaking to its depths.\nAnd you, LORD—how long will you wait?"
    },
    "4": {
      "L": "Return, O LORD; deliver my soul; save me for the sake of your steadfast love.",
      "M": "Turn back, O LORD, rescue my life; save me for the sake of your steadfast love.",
      "T": "Come back to me, LORD—rescue my life!\nSave me, because of your steadfast love."
    },
    "5": {
      "L": "For in death there is no remembrance of you; in Sheol who will give you praise?",
      "M": "For among the dead no one remembers you; in Sheol no one praises you.",
      "T": "In death no one calls your name to mind;\nin the grave, who can still sing your praise?"
    },
    "6": {
      "L": "I am weary with my groaning; every night I flood my bed with tears; I drench my couch with my weeping.",
      "M": "I am exhausted with my moaning; every night I drench my bed with tears; I soak my couch with my weeping.",
      "T": "I am worn out with sighing;\nevery night my tears wash over my bed,\nsoaking my couch with grief."
    },
    "7": {
      "L": "My eye wastes away because of grief; it grows old because of all my enemies.",
      "M": "My eye has grown dim from grief; it wastes away because of all my foes.",
      "T": "My eyes are blurred with weeping,\nhaggard from watching my enemies close in."
    },
    "8": {
      "L": "Depart from me, all workers of iniquity, for the LORD has heard the sound of my weeping.",
      "M": "Depart from me, all you who do evil, for the LORD has heard the sound of my weeping.",
      "T": "Away from me, all you who practice evil!\nThe LORD has heard me weeping."
    },
    "9": {
      "L": "The LORD has heard my plea; the LORD accepts my prayer.",
      "M": "The LORD has heard my supplication; the LORD receives my prayer.",
      "T": "The LORD has heard my cry for help;\nthe LORD takes up my prayer as his own."
    },
    "10": {
      "L": "All my enemies shall be ashamed and greatly troubled; they shall turn back and be put to shame suddenly.",
      "M": "All my enemies shall be ashamed and greatly disturbed; they shall turn back and be disgraced in an instant.",
      "T": "All my enemies will crumble in shame;\nshocked, they will retreat—\ndisgraced in a single moment."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 1–6 written.')

if __name__ == '__main__':
    main()
