"""
MKT Psalms chapters 39–42 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-39-42.py

=== Overview of this unit ===

Ps 39 (13 v) — Individual lament of David "to Jeduthun," one of the three Levitical choir
    directors (1 Chr 16:41–42; 25:1–6). The psalm records David's interior conflict:
    he resolves to stay silent before the wicked (vv1–2), but the suppressed anguish
    burns until he must speak (v3). The speech is directed entirely to God — a meditation
    on human brevity using H1892 (hevel, breath/vapor), the signature word of Ecclesiastes.
    Hevel appears three times (vv5,6,11): every human being is a breath; their frantic
    striving is vapor. The psalm closes with the remarkable prayer "look away from me"
    (v13) — not a defiant rejection of God but a plea for momentary relief before death.
    Social shame language: v8 ("reproach of the foolish") — being exposed as weak to those
    who mock the righteous. Structurally: resolution (vv1–2) → burning confession (v3) →
    meditation on brevity (vv4–6) → hope reorientation (v7) → petition for forgiveness
    and relief (vv8–11) → lament-prayer of a sojourner (vv12–13).

Ps 40 (17 v) — Individual thanksgiving then lament of David. This psalm is unusual: it
    begins as a thanksgiving for past rescue (vv1–10) and pivots to a lament-petition
    (vv11–17) that almost exactly repeats Psalm 70. The famous vv6–8 — "sacrifice you
    did not desire... ears you have opened for me... I come to do your will" — stand at
    the theological center. The Hebrew v6 reads "ears you have dug/bored for me" (כָּרִיתָ
    אָזְנַיִם), meaning God has given the psalmist the capacity and organ of obedience.
    The LXX renders this as "a body you have prepared for me" — a significant interpretive
    paraphrase that the writer of Hebrews 10:5–7 quotes to describe Christ's embodied
    obedience. The Hebrew is translated faithfully; the LXX/Hebrews connection is noted
    in the T tier header. Structurally: patient waiting and rescue (vv1–3) → beatitude
    on trust (v4) → God's wonders (v5) → embodied obedience over sacrifice (vv6–8) →
    public proclamation (vv9–10) → petition for mercy (v11) → crisis of surrounding evil
    (v12) → urgent prayer (vv13–17).

Ps 41 (13 v) — Closing psalm of David ending Book I of the Psalter. Beatitude for those
    who care for the poor (dal, H1800 = the weak, the thin/powerless, the vulnerable).
    The bulk of the psalm is a lament: David is ill, enemies circle, and worst of all
    v9 — "my familiar friend who ate my bread has lifted his heel against me." Jesus
    quotes v9 about Judas in John 13:18 ("that the Scripture might be fulfilled"). The
    phrase "lifted his heel" (H6119, aqev) means betrayal — a gesture of contempt from
    one who shared intimacy. The psalm closes with a doxology (v13) marking the end of
    Book I: "Blessed be the LORD God of Israel from everlasting to everlasting." This
    doxology is an editorial addition, not part of the psalm itself.

Ps 42 (11 v) — Opens Book II of the Psalter. A Maskil of the Sons of Korah — a Levitical
    guild of temple musicians (not of David). The poet is separated from the Jerusalem
    temple, apparently in exile or flight in northern Transjordan (v6: Jordan, Hermon,
    Mount Mizar). The famous opening simile — a deer panting for water-brooks — captures
    the intensity of the soul's longing for God. The refrain (v5 = v11) is the psalm's
    theological anchor: the psalmist speaks to his own soul, commands it to hope in God
    despite its depression. "Deep calls to deep" (v7) uses H8415 (tehom, the primordial
    deep of Gen 1:2) — not merely waves but the oceanic abyss. The psalm closes with
    the same longing as it opened — no resolution yet. (Ps 43 is the resolution and was
    originally one poem with Ps 42; note the shared refrain at 42:5, 42:11, 43:5.)

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps) in L/M throughout. In T: "the LORD."
      Consistent with all prior Psalms scripts.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Ps 42 addresses God directly without the
      divine name YHWH — characteristic of Book II, which tends to prefer Elohim. This
      "Elohistic Psalter" (Ps 42–89) feature is preserved naturally by "God."

H1892 (הֶבֶל, hevel, Ps 39:5,6,11): "breath" or "vapor" in L; "breath" in M; T unpacks
      the meaning. Hevel is the key word of Ecclesiastes (translated there "vanity" by
      KJV, "meaninglessness" by NIV, but the root image is a breath or vapor — thin,
      insubstantial, quickly gone). Rendering it "vanity" (KJV) is archaic; "meaningless"
      (NIV) misses the concrete image. "Breath" or "vapor" preserves the physical picture:
      a human being at their best is as substantial as exhaled breath. In L: "breath."
      In M: "a breath." In T: the image is expanded slightly to surface the fragility.

H7307 (רוּחַ, ruach): Not the Spirit of God in this unit.
      Ps 39:v not present as distinct contested term.
      Ps 42:v not present as distinct contested term.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T throughout. Occurs at Ps 40:10,11;
      42:8. Consistent with all prior Psalms scripts. Carries covenantal loyalty +
      active kindness; "lovingkindness" is archaic, "mercy" loses the loyalty dimension.

H5315 (נֶפֶשׁ, nefesh):
      Ps 39 — not prominent.
      Ps 40:14,15 — "soul" (those seeking to take away the soul = the person's life).
      Ps 41:2 — "his life" (do not hand him to the desire of his enemies).
      Ps 42:1,4,5,6,11 — "soul" throughout. The panting, thirsting, downcast soul. This
        is nefesh as the whole embodied self in its deepest need, not a Greek immaterial
        soul. Rendered "soul" to preserve the psalmic register; "self" and "life" used
        selectively in T where context demands it.

H4905 (מַשְׂכִּיל, maskil, Ps 42 superscription): Retained as "Maskil" in all tiers.
      Same decision as Ps 32. Genre label of uncertain meaning — possibly teaching psalm,
      possibly a musical term. LXX: "understanding."

H1800 (דָּל, dal, Ps 41:1): "the poor / the vulnerable / the weak." Dal denotes the
      thin/powerless, those without social resources or protection. Rendered "the
      vulnerable" in M/T to distinguish from other poverty terms. In L: "the weak."

H6119 (עָקֵב, aqev, Ps 41:9): "heel." "Lifted his heel against me" — the gesture of
      contempt and betrayal. Jesus quotes this about Judas (John 13:18). The T tier
      preserves the physical image. No paraphrase.

H8415 (תְּהוֹם, tehom, Ps 42:7): "deep." The primordial abyss — same word as Gen 1:2
      "the deep." "Deep calls to deep" evokes the oceanic overwhelm of divine
      judgment-waters. T surfaces the Genesis resonance.

=== Ps 40:6 — textual note on "ears / body" ===

The Hebrew reads: "Ears you have dug/bored for me" (H241 H3738 כָּרִיתָ אָזְנַיִם לִי).
The image is of a servant whose ears have been opened — physically prepared to hear and
obey, perhaps alluding to the slave-ear-boring of Exodus 21:6 (voluntary, lifelong
service). The LXX renders this as "a body you have prepared for me" (σῶμα δὲ κατηρτίσω
μοι) — an interpretive paraphrase that extends the organ of hearing to the whole embodied
instrument of obedience. Hebrews 10:5–7 quotes the LXX to describe Christ's incarnate
obedience: the Son came with a body prepared precisely to do what sacrifice could not
accomplish. The MKT L/M follow the Hebrew faithfully. The T tier renders the Hebrew and
marks the Hebrews connection in a note.

=== Ps 41:13 — doxology status ===

Verse 13 ("Blessed be the LORD God of Israel from everlasting to everlasting") is a
liturgical doxology closing Book I of the Psalter, not composed by David. It is parallel
to the doxologies closing Books II (72:18–19), III (89:52), and IV (106:48). It belongs
in every tier but is noted in T as a scribal/editorial addition to the Psalter.

=== Ps 42 — Korah and the Elohistic Psalter ===

The Sons of Korah are Levitical temple musicians descended from the Korah of Numbers 16
(whose children did not die with him, Num 26:11). They appear as authors or dedicatees
of Ps 42–49, 84–85, 87–88. The Elohim-preference of Book II (Ps 42–89) over YHWH is a
documented redactional feature; translation preserves it naturally.

=== Aspect and tense notes ===

Ps 39 — Perfect tense for completed acts: "I said" (v1, H559), "I was mute" (v2,
    H481), "my heart was hot" (v3, H2552). The petition uses imperfects: "be gracious"
    (v8), "remove" (v10, H5493). The hevel-meditations use participle constructions
    (vv5–6): timeless gnomic statements about human nature.

Ps 40 — vv1–10 are past testimony in perfects: "I waited" (v1), "he brought me up" (v2),
    "he put a new song" (v3). The contested verbs in v6 ("you have opened/dug") are
    perfects of completed divine action. vv11–17 shift to imperfect petition. M/T honor
    the narrative-testimony → present-crisis shift.

Ps 41 — The opening beatitude (v1) is a participial construction (timeless truth). vv2–3
    are imperfects (ongoing divine protection). vv4–9 mix perfect narrative and imperfect
    lament. The refrain of v13 is participle form: Blessed is/be the LORD.

Ps 42 — Rich in simile (v1), question (vv2,5,9,11), and perfect narrative (vv4,6).
    The refrain (vv5,11) uses a rare form — cohortative ("I will yet praise him") +
    rhetorical self-address. T preserves the self-dialogue energy of the refrain.

=== OT echo notes ===

Ps 39:12 — "I am a sojourner (ger) with you, a traveler (toshav), as all my fathers were."
    This echoes the patriarchal self-description in Gen 23:4 (Abraham: "I am a stranger
    and sojourner among you") and is picked up in Hebrews 11:13 ("strangers and exiles on
    the earth"). The T tier preserves the sojourner-theology without over-reading.

Ps 40:6–8 — See textual note above. The ear-boring / body-prepared / embodied obedience
    tradition runs: Exod 21:6 (slave's ear pierced) → Ps 40:6 (ears opened for service)
    → LXX Ps 40:6 (body prepared) → Heb 10:5–7 (Christ's incarnate obedience over
    sacrifice). The T tier names the Hebrews connection without replacing the Hebrew.

Ps 41:9 — "He who ate my bread has lifted his heel against me." Jesus says (John 13:18)
    this is fulfilled in Judas. The T tier preserves the psalm's primary sense (David
    betrayed by a trusted friend) while the Johannine application is implicit in any
    well-read reader.

Ps 42:7 — "Deep calls to deep" (tehom-el-tehom). Tehom echoes Gen 1:2 (the primordial
    deep over which God's Spirit/wind moved). The image here reverses creation-order:
    instead of the Spirit moving over the deep to bring life, the deeps are calling to
    each other in the language of overwhelming chaos. T surfaces this inversion.
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
  # Psalm 39 — Lament on Human Brevity: "I Am a Sojourner"
  # ============================================================
  "39": {
    "1": {
      "L": "To the chief Musician, to Jeduthun. A Psalm of David. I said, 'I will guard my ways so that I may not sin with my tongue; I will keep a muzzle on my mouth while the wicked are before me.'",
      "M": "To the director of music. To Jeduthun. A Psalm of David. I said, 'I will keep watch over my ways so I will not sin with my tongue; I will hold a muzzle over my mouth while the wicked are in front of me.'",
      "T": "To the choirmaster. For Jeduthun. Of David.\nI resolved: I will watch my step so my tongue won't betray me into sin.\nI will keep my mouth under guard—especially while the wicked are watching."
    },
    "2": {
      "L": "I was mute and silent; I held my peace from good, and my anguish was stirred.",
      "M": "I was mute and utterly silent, holding back even from what was good, and my pain intensified.",
      "T": "I went completely mute.\nI held back—even from saying good things.\nBut the pain only grew worse."
    },
    "3": {
      "L": "My heart grew hot within me; while I mused, the fire burned; then I spoke with my tongue:",
      "M": "My heart grew hot within me; as I brooded, the fire blazed up; then I spoke with my tongue:",
      "T": "My heart smoldered while I brooded.\nThe more I turned it over, the hotter it burned—\nuntil at last I had to speak."
    },
    "4": {
      "L": "'Show me, O LORD, my end, and what the measure of my days is; let me know how fleeting I am.'",
      "M": "'LORD, show me my end—how long I have to live; let me grasp how short-lived I am.'",
      "T": "'Tell me, LORD—what is my end?\nHow many days have I got?\nLet me understand just how thin my existence really is.'"
    },
    "5": {
      "L": "Behold, you have made my days a few handbreadths, and my lifetime is as nothing before you. Surely every human being stands as a mere breath. Selah",
      "M": "You have made my days barely a handbreadth long; my lifetime is as nothing in your sight. Truly every person at their best is only a breath. Selah",
      "T": "You have made my days no longer than a handspan.\nBefore you, my whole lifetime adds up to nothing.\nAt their very best, every human being is only a breath—a vapor.\nSelah."
    },
    "6": {
      "L": "Surely every man walks about as a shadow; surely they are in turmoil in vain; he heaps up riches and does not know who will gather them.",
      "M": "Surely everyone moves about like a shadow; they are in commotion for nothing; they pile up wealth and do not know who will collect it.",
      "T": "Every person walks around like a shadow—\na silhouette, no real substance.\nThey churn in frantic activity—all empty noise.\nThey hoard and accumulate and die not knowing who will inherit it all."
    },
    "7": {
      "L": "And now, Lord, what do I wait for? My hope is in you.",
      "M": "And now, Lord, what do I wait for? My hope is in you.",
      "T": "So then—what am I actually waiting for, Lord?\nYou. Only you. That is where my hope stands."
    },
    "8": {
      "L": "Deliver me from all my transgressions; do not make me the reproach of the foolish.",
      "M": "Rescue me from all my transgressions; do not make me a disgrace before fools.",
      "T": "Rescue me from all my rebellions against you.\nDon't let me become the target of mockery from those who have no wisdom."
    },
    "9": {
      "L": "I am mute; I do not open my mouth, because it is you who have done this.",
      "M": "I am silent; I do not open my mouth, because this is your doing.",
      "T": "I am silent.\nI won't open my mouth.\nYou have done all of this—I know it."
    },
    "10": {
      "L": "Remove your stroke from me; I am consumed by the blow of your hand.",
      "M": "Take away your affliction from me; I am worn down by the blow of your hand.",
      "T": "Lift your blow from me.\nI am being destroyed under the weight of your hand."
    },
    "11": {
      "L": "When with rebukes you discipline a man for iniquity, you consume like a moth what he treasures; surely every human being is a mere breath. Selah",
      "M": "When you correct someone for their iniquity with rebukes, you consume like a moth everything they prize; truly every person is only a breath. Selah",
      "T": "When you rebuke and discipline a person for their sin,\nyou eat away everything they prize—like a moth destroying fine cloth.\nIn the end every human being is only vapor.\nSelah."
    },
    "12": {
      "L": "Hear my prayer, O LORD, and give ear to my cry; do not be silent at my tears. For I am a sojourner with you, a passing traveler, as all my fathers were.",
      "M": "Hear my prayer, LORD, and listen to my cry; do not stay silent at my tears. I am a stranger in your presence, a temporary traveler, as all my ancestors were.",
      "T": "Hear my prayer, LORD.\nListen to my cry.\nDon't be silent while I weep.\nI am a stranger here—a temporary resident in your world—\njust as all my ancestors were before me."
    },
    "13": {
      "L": "Look away from me, that I may know gladness before I depart and am no more.",
      "M": "Turn your gaze from me, so that I may recover joy before I depart and am gone.",
      "T": "Let up—just long enough\nthat I can breathe again, maybe even smile,\nbefore I leave this world and am no more."
    }
  },

  # ============================================================
  # Psalm 40 — Thanksgiving Turned Petition: "I Delight to Do Your Will"
  # ============================================================
  "40": {
    "1": {
      "L": "To the chief Musician. A Psalm of David. I waited, truly waited, for the LORD; and he turned to me and heard my cry.",
      "M": "To the director of music. A Psalm of David. I waited patiently for the LORD; he turned to me and listened to my cry.",
      "T": "To the choirmaster. Of David.\nI waited—deliberately, persistently—for the LORD.\nAnd he bent down and heard my cry."
    },
    "2": {
      "L": "He brought me up from the pit of destruction, from the miry clay; he set my feet upon a rock and established my steps.",
      "M": "He lifted me out of the pit of destruction, from the muddy bog; he set my feet on a rock and made my steps firm.",
      "T": "He reached into the horrible pit—the sucking mud—and lifted me out.\nHe planted my feet on solid rock.\nHe made my footing sure."
    },
    "3": {
      "L": "He put a new song in my mouth, praise to our God; many will see and fear and will trust in the LORD.",
      "M": "He put a new song in my mouth, praise to our God; many will see and be filled with awe and will put their trust in the LORD.",
      "T": "He gave me a new song—\npraise rising to our God.\nMany people will watch and be struck with awe,\nand they will trust in the LORD."
    },
    "4": {
      "L": "Blessed is the man who makes the LORD his trust, who does not look to the proud or to those who go after lies.",
      "M": "Blessed is the one who makes the LORD his trust and does not turn to the proud or to those who follow falsehood.",
      "T": "Blessed is the person who has staked everything on the LORD—\nwho hasn't gone chasing after the arrogant\nor turned aside toward those who follow empty lies."
    },
    "5": {
      "L": "You have multiplied, O LORD my God, your wondrous deeds and your thoughts toward us; none can compare with you; if I would declare and speak of them, they are more than can be numbered.",
      "M": "You have multiplied your wonderful deeds and your thoughts toward us, O LORD my God; no one can compare to you. If I were to declare and speak them, they are too many to count.",
      "T": "How vast your wonders are, LORD my God—\nhow vast your thoughts toward us!\nNothing and no one equals you.\nIf I tried to name them all—to speak each one—\nthere are more than I could ever number."
    },
    "6": {
      "L": "Sacrifice and offering you did not desire; but ears you have opened for me; burnt offering and sin offering you have not required.",
      "M": "Sacrifice and grain offering you did not want; but you have given me opened ears; burnt offering and sin offering you have not asked for.",
      "T": "You don't want animal sacrifice or grain-offerings.\nYou have opened my ears—bored them open for obedience, like a servant ready to hear.\nBurnt offerings and sin offerings are not what you require.\n[The Greek translation rendered this verse as 'a body you have prepared for me'—the form quoted in Hebrews 10:5–7 about Christ's embodied obedience. The Hebrew speaks of ears: the organ of hearing and loyal service.]"
    },
    "7": {
      "L": "Then I said, 'Behold, I come; in the scroll of the book it is written of me.'",
      "M": "Then I said, 'Here I am; in the scroll of the book it is written about me.'",
      "T": "'Here I am,' I said. 'I come—\nand the book's scroll says I would.'"
    },
    "8": {
      "L": "I delight to do your will, O my God; your instruction is within my heart.",
      "M": "I delight to do your will, O my God; your instruction is within my heart.",
      "T": "I am delighted to do what you want, my God.\nYour teaching is written on the inside of me."
    },
    "9": {
      "L": "I have proclaimed righteousness in the great congregation; I have not restrained my lips; O LORD, you know it.",
      "M": "I have announced righteousness in the great assembly; I have not held my lips back—LORD, you know it.",
      "T": "I proclaimed your righteousness in the great assembly—out loud, before everyone.\nI did not close my lips.\nYou know that, LORD."
    },
    "10": {
      "L": "I have not hidden your righteousness within my heart; I have spoken of your faithfulness and your salvation; I have not concealed your steadfast love and your truth from the great congregation.",
      "M": "I have not hidden your righteousness in my heart; I have declared your faithfulness and your salvation; I have not concealed your steadfast love or your truth from the great assembly.",
      "T": "Your righteousness—I didn't lock it away inside me.\nYour faithfulness and salvation—I proclaimed them.\nYour steadfast love and your truth—I announced them\nbefore the full hearing of the great assembly.\nNothing held back, nothing concealed."
    },
    "11": {
      "L": "As for you, O LORD, you will not restrain your mercy from me; your steadfast love and your truth will continually guard me.",
      "M": "As for you, LORD, do not withhold your compassion from me; let your steadfast love and truth continually protect me.",
      "T": "For your part, LORD—do not hold back your tender compassion from me.\nLet your steadfast love and truth be my constant guard."
    },
    "12": {
      "L": "For evils without number have surrounded me; my iniquities have overtaken me so that I cannot see; they are more than the hairs of my head, and my heart fails me.",
      "M": "For countless evils have closed in around me; my iniquities have caught up with me until I cannot see clearly—they are more than the hairs of my head, and my courage fails.",
      "T": "Evils beyond counting have closed in around me.\nMy own iniquities have caught up with me—I can't see through them.\nMore than the hairs on my head.\nMy heart is sinking."
    },
    "13": {
      "L": "Be pleased, O LORD, to deliver me; O LORD, make haste to help me.",
      "M": "Please, LORD, come to rescue me; LORD, hurry to help me.",
      "T": "LORD—please—deliver me.\nDo not delay in coming."
    },
    "14": {
      "L": "Let those who seek to take away my life be put to shame and confusion; let those who desire my harm be turned back and dishonored.",
      "M": "Let those who seek to take my life be put to shame and confounded; let those who wish me harm be turned back in disgrace.",
      "T": "Let everyone hunting me down be shamed and confounded.\nLet those who want me destroyed be turned back in dishonor."
    },
    "15": {
      "L": "Let those who say to me, 'Aha, aha!' be appalled on account of their shame.",
      "M": "Let those who mock me with 'Aha! Aha!' be horrified by their own shame.",
      "T": "Those who taunt me with 'Aha! Aha!'—\nlet the shame fall back on them instead."
    },
    "16": {
      "L": "Let all who seek you rejoice and be glad in you; let those who love your salvation say continually, 'The LORD is great!'",
      "M": "Let all who seek you rejoice and be glad in you; let those who love your salvation always say, 'Great is the LORD!'",
      "T": "But let everyone who is seeking you burst into joy and gladness—in you.\nLet those who love your rescue never stop saying:\n'The LORD is great!'"
    },
    "17": {
      "L": "As for me, I am poor and needy; yet the Lord takes thought for me. You are my help and my deliverer; do not delay, O my God.",
      "M": "As for me, I am poor and needy; yet the Lord thinks of me. You are my help and my deliverer—do not be slow, my God.",
      "T": "I have nothing and I know it.\nBut the Lord has me in mind.\nYou are my help; you are my rescuer.\nMy God—please don't be slow."
    }
  },

  # ============================================================
  # Psalm 41 — Care for the Vulnerable; Betrayal and Vindication
  # ============================================================
  "41": {
    "1": {
      "L": "To the chief Musician. A Psalm of David. Blessed is the one who considers the weak; the LORD delivers him in the day of trouble.",
      "M": "To the director of music. A Psalm of David. Blessed is the one who cares for the vulnerable; the LORD will deliver that person in the day of trouble.",
      "T": "To the choirmaster. Of David.\nBlessed is the person who notices the weak and takes them seriously—\nthe LORD will deliver that person when trouble comes."
    },
    "2": {
      "L": "The LORD preserves him and keeps him alive; he is called blessed in the land; you will not give him over to the will of his enemies.",
      "M": "The LORD protects and preserves his life; he is regarded as blessed in the land; you will not hand him over to his enemies' desire.",
      "T": "The LORD guards that person and keeps them alive.\nThey are regarded as blessed throughout the land.\nYou will not let their enemies have their way with them."
    },
    "3": {
      "L": "The LORD sustains him on his sickbed; in his illness you restore him to health.",
      "M": "The LORD supports him on his bed of illness; in his sickness you bring him back to health.",
      "T": "When sickness has them bedridden, the LORD is there beside them.\nIn their illness you bring restoration."
    },
    "4": {
      "L": "As for me, I said, 'O LORD, be gracious to me; heal my soul, for I have sinned against you.'",
      "M": "As for me, I said, 'LORD, have mercy on me; heal my soul, for I have sinned against you.'",
      "T": "I myself said this:\n'LORD, have mercy on me.\nHeal me—I have sinned against you.'"
    },
    "5": {
      "L": "My enemies speak evil of me: 'When will he die and his name perish?'",
      "M": "My enemies speak wickedly against me: 'When will he die and his name vanish?'",
      "T": "My enemies say the worst about me behind my back:\n'When does he finally die? When does his name disappear for good?'"
    },
    "6": {
      "L": "And when one comes to see me, he speaks with empty words while his heart gathers iniquity; when he goes out he speaks it abroad.",
      "M": "When one of them comes to visit me, he mouths empty words while inwardly filing away material against me; then he walks out and spreads it everywhere.",
      "T": "When one of them comes to visit—a pretend visit—\nhis words mean nothing while his mind notes everything it can use against me.\nThen he walks out and tells the whole story."
    },
    "7": {
      "L": "All who hate me whisper together against me; they devise harm against me.",
      "M": "All who hate me whisper together against me; they are plotting disaster for me.",
      "T": "Everyone who hates me huddles together and whispers.\nThey are all scheming my ruin."
    },
    "8": {
      "L": "They say, 'A deadly thing has fastened on him; he who lies down will not rise again.'",
      "M": "They say, 'Something incurable has seized him; he will never get up from where he is lying.'",
      "T": "They are saying: 'Something has broken in him that cannot be fixed.\nHe is down—he will never get up from this.'"
    },
    "9": {
      "L": "Even my close friend, in whom I trusted, who ate my bread, has lifted his heel against me.",
      "M": "Even my closest friend, whom I trusted, who shared my bread, has turned against me.",
      "T": "Even the person I trusted most—the one who broke bread at my table—\nhas raised his heel against me.\nBetrayal from inside the circle."
    },
    "10": {
      "L": "But you, O LORD, be gracious to me and raise me up, so that I may repay them.",
      "M": "But you, LORD, have mercy on me and restore me, so that I may give them what they deserve.",
      "T": "But you, LORD—have mercy on me.\nRaise me up so that I can pay them back."
    },
    "11": {
      "L": "By this I know that you delight in me: my enemy has not triumphed over me.",
      "M": "By this I know that you are pleased with me—my enemy has not triumphed over me.",
      "T": "I know you favor me by this single fact:\nmy enemy has not broken out in triumph over me."
    },
    "12": {
      "L": "As for me, you uphold me in my integrity and set me before your face forever.",
      "M": "As for me, you hold me up in my integrity and place me before your face forever.",
      "T": "And me—you are holding me steady in my integrity.\nYou have set me before your face. Forever."
    },
    "13": {
      "L": "Blessed be the LORD, the God of Israel, from everlasting to everlasting! Amen and Amen.",
      "M": "Blessed be the LORD, the God of Israel, from everlasting to everlasting. Amen and Amen.",
      "T": "Blessed be the LORD, the God of Israel—\nfrom everlasting to everlasting.\nAmen. And Amen."
    }
  },

  # ============================================================
  # Psalm 42 — Maskil of the Sons of Korah: The Thirsting Soul
  # ============================================================
  "42": {
    "1": {
      "L": "To the chief Musician. A Maskil of the Sons of Korah. As a deer pants for flowing streams, so my soul pants for you, O God.",
      "M": "To the director of music. A Maskil of the Sons of Korah. As a deer longs for flowing streams, so my soul longs for you, O God.",
      "T": "To the choirmaster. A Maskil of the Sons of Korah.\nAs a deer—desperate for the water-brook—\nso my soul is desperate for you, God."
    },
    "2": {
      "L": "My soul thirsts for God, for the living God. When shall I come and appear before God?",
      "M": "My soul thirsts for God, for the living God. When will I come and stand in God's presence?",
      "T": "My whole self is parched—thirsting for God, the God who is alive and real.\nWhen will I get to come and stand before him?"
    },
    "3": {
      "L": "My tears have been my food day and night, while they say to me all day long, 'Where is your God?'",
      "M": "My tears have been my food day and night, while people keep saying to me all day long, 'Where is your God?'",
      "T": "I have eaten nothing but tears—day after day, night after night—\nwhile all around me they keep asking:\n'Where is this God of yours?'"
    },
    "4": {
      "L": "These things I remember as I pour out my soul: how I used to go with the throng and lead them in procession to the house of God with shouts of joy and thanksgiving, a celebrating multitude.",
      "M": "These things I remember as I pour out my soul: how I used to walk with the crowd, leading them in procession to the house of God, with shouts of joy and thanksgiving—a multitude keeping festival.",
      "T": "I pour out my soul in memory:\nhow I used to walk at the head of the crowd,\nleading the procession up to God's house—\nthe shouts of joy, the songs of thanksgiving,\nthe whole multitude keeping festival together."
    },
    "5": {
      "L": "Why are you cast down, O my soul, and why are you in turmoil within me? Hope in God, for I will yet praise him—my salvation and my God.",
      "M": "Why are you downcast, O my soul? Why so disturbed within me? Put your hope in God, for I will yet praise him—my Savior and my God.",
      "T": "Why are you sinking, my soul?\nWhy this churning turmoil inside me?\nHope in God.\nI will praise him yet—he is my rescue, he is my God."
    },
    "6": {
      "L": "My soul is cast down within me; therefore I remember you from the land of Jordan and of the Hermons, from Mount Mizar.",
      "M": "My soul is cast down within me; therefore I remember you from the land of Jordan, the heights of Hermon, and Mount Mizar.",
      "T": "My soul has collapsed.\nFrom here—from the Jordan valley, the Hermon ridges, from little Mount Mizar—\nI reach back across the distance to remember you."
    },
    "7": {
      "L": "Deep calls to deep at the thunder of your waterfalls; all your waves and your billows have swept over me.",
      "M": "Deep calls to deep at the roar of your waterfalls; all your waves and breakers have rolled over me.",
      "T": "The deep is calling out to the deep—\nat the crash of your waterspouts.\nWave after wave, breaker after breaker—\nall of them rolling over me.\n[Tehom—the primordial deep of Genesis 1—speaks the language of overwhelming chaos, reversed creation.]"
    },
    "8": {
      "L": "By day the LORD commands his steadfast love, and at night his song is with me—a prayer to the God of my life.",
      "M": "By day the LORD directs his steadfast love, and at night his song is with me, a prayer to the God of my life.",
      "T": "And yet—by day the LORD pours out his steadfast love.\nBy night his song rises in me: a prayer to the God who gives me life."
    },
    "9": {
      "L": "I say to God my rock, 'Why have you forgotten me? Why must I go about in mourning because of the enemy's oppression?'",
      "M": "I say to God my rock, 'Why have you forgotten me? Why do I walk in mourning under the oppression of the enemy?'",
      "T": "I say to God—the Rock I stand on—\n'Why have you forgotten me?\nWhy am I walking around in this grief\nwhile the enemy crushes me?'"
    },
    "10": {
      "L": "As with a sword-thrust in my bones, my enemies reproach me while they say to me all day long, 'Where is your God?'",
      "M": "As if a sword were cutting through my bones, my enemies taunt me, saying to me all day, 'Where is your God?'",
      "T": "It is like a blade breaking through my bones—\nmy enemies mocking me every single day:\n'Where is this God of yours?'"
    },
    "11": {
      "L": "Why are you cast down, O my soul, and why are you in turmoil within me? Hope in God, for I will yet praise him—my salvation and my God.",
      "M": "Why are you downcast, O my soul? Why so disturbed within me? Put your hope in God, for I will yet praise him—my Savior and my God.",
      "T": "Why are you still sinking, my soul?\nWhy this inner turmoil that won't stop?\nHope in God.\nI will praise him yet.\nHe is the health of my face—he is my God."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 39–42 written.')

if __name__ == '__main__':
    main()
