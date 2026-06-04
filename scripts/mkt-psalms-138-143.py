"""
MKT Psalms chapters 138–143 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-138-143.py

=== Overview of this unit ===

These six psalms form a distinct cluster near the end of the Psalter. Ps 138–145
are all headed "of David" — the largest consecutive run of Davidic attributions
since Ps 108–110. The unit moves from individual thanksgiving (138) through the
deepest meditation on divine omniscience in all Scripture (139), a pair of lament/
protection psalms with sharp imprecatory edges (140–141), a stark cave-psalm of
total desolation (142), and a penitential psalm that is at once the most theologically
compressed of the group and one of the seven traditional Penitential Psalms (143).

Ps 138 (8 v) — Thanksgiving before the divine assembly. David praises before
    the "elohim" (celestial beings/the divine council, not pagan gods — see v6's
    contrast: the LORD looks to the lowly while the proud are known only from a
    distance). The famous crux at v2 — "you have magnified your word above all
    your name" — is rendered literally in L; M/T bring out the meaning: God's
    specific spoken promise is even more binding than the divine name itself, since
    it stakes that name on a particular act. H2617 (chesed) at vv2 and 8 brackets
    the psalm.

Ps 139 (24 v) — Divine omniscience and omnipresence; the womb; the book of days;
    imprecation and surrender. The longest and most philosophically dense psalm in
    this unit. Its four movements are: searched (vv1-6), present everywhere (vv7-12),
    made in the womb (vv13-16), thoughts precious and innumerable (vv17-18), followed
    by an imprecatory turn (vv19-22) resolved in a final surrender (vv23-24). The
    hapax golem (H1564, v16) — the only occurrence in the entire OT — means an
    unformed, wrapped-up thing; the embryo. H4639 (work/deed) and H7307 (Spirit) are
    key through this psalm.

Ps 140 (13 v) — Deliverance from violent schemers. H2555 (chamas, violence) is
    the key term (vv1, 4, 11). The psalm is framed as a legal case: the LORD maintains
    justice (v12) and the righteous dwell in his presence (v13). The serpent-tongue
    image (v3) echoes Gen 3 and Paul's catena in Rom 3:13.

Ps 141 (10 v) — Evening prayer; guard of lips; welcome correction from the righteous.
    The incense/evening sacrifice imagery (v2) predates any temple; it is pure prayer
    as liturgical act. V5 contains a notoriously dense half-verse (yet my prayer is
    continually against their evil deeds). V7 — bones scattered at the mouth of Sheol
    like plowed earth — is the sharpest image of mortality in this set.

Ps 142 (7 v) — Maskil; a prayer from the cave. The superscription places this in
    one of David's two cave-hideouts (Adullam, 1 Sam 22, or Engedi, 1 Sam 24). It is
    the most structurally compact psalm in the set: pure lament, pure isolation (no
    one on the right, no refuge, no one caring for his soul), then the pivot to the
    LORD as refuge and portion. H2506 (portion) is the Levitical word for inheritance;
    David has no land — but the LORD is his portion, as the Levites said of God (Deut 10:9).

Ps 143 (12 v) — The seventh (and last) of the traditional Penitential Psalms. No
    one living is righteous (v2) — the Pauline text that grounds Rom 3:20 and Gal 2:16.
    The movement: appeal to faithfulness/righteousness (v1), acknowledgment that none
    can stand (v2), description of enemy's crushing assault (v3), inner devastation
    (v4), meditation on God's past works (v5), thirsting (v6), urgent petition (vv7-9),
    and a three-part closing prayer: preserve / bring out / cut off (vv11-12). H7307
    (Spirit) at v10 is the divine Spirit leading on level ground (H4334 mishor —
    straight terrain as opposed to treacherous slopes).

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in all tiers throughout. Consistent with all prior
    Psalms scripts. At Ps 143:1-2, multiple YHWH occurrences are preserved.

H136 (אֲדֹנָי, Adonai): "Lord" (lowercase, not small-caps) when used alone.
    Appears at 140:7; 141:8; 143:2 alongside or near YHWH. The distinction
    between "LORD" (YHWH) and "Lord" (Adonai) is maintained.

H3069 (special ketiv/qere for Adonai YHWH): At 140:7 — "O Lord GOD" in L
    (following KJV convention); "O Sovereign LORD" in M/T.

H2617 (חֶסֶד, chesed): "steadfast love" throughout. Appears at 138:2, 138:8,
    143:8, 143:12. The covenantal, active-kindness force is preserved especially
    at 143:12 where it grounds even the imprecation.

H5315 (נֶפֶשׁ, nefesh): "soul" throughout. At 142:4-5 and 143:3, 6, 8, 11-12
    it is the persecuted, thirsting, imprisoned self — the embodied person, not
    a detached Greek soul.

H7307 (רוּחַ, ruach):
    — Ps 139:7: "your Spirit" (uppercase) — the divine Spirit from whom there is no
      escape; parallel to divine "presence" (H6440 panim) in the same verse.
    — Ps 142:3: "my spirit" (lowercase) — the human spirit overwhelmed within.
    — Ps 143:4: "my spirit" (lowercase) — human spirit overwhelmed.
    — Ps 143:7: "my spirit" (lowercase) — human spirit failing.
    — Ps 143:10: "your good Spirit" (uppercase) — the divine Spirit leading on level
      ground. This is one of only two OT texts that call the divine Spirit "good"
      (cf. Neh 9:20). L preserves "your good Spirit" as a title; M/T keep the same.

H430 (אֱלֹהִים, elohim):
    — Ps 138:1: "the gods" — here the celestial assembly / divine council (the parallel
      to v6 suggests real beings of the divine realm, not an abstract plural of majesty
      or pagan idols). The MT is clear; the Greek recension reads "angels." L uses "the
      gods"; M/T use "the heavenly assembly" / "the divine council" to surface the
      meaning.
    — Ps 139:17, 23: "O God" — direct address, "el" (H410) at v17 and v23.

H410 (אֵל, el): "God" in direct address at Ps 139:17, 23; Ps 140:6.

H1564 (גֹּלֶם, golem): "my unformed substance" in L; "my unformed body" in M/T.
    This word appears ONLY ONCE in the entire OT — here at Ps 139:16. Its basic
    meaning is a wrapped-up, shapeless, not-yet-formed thing; the embryo before it
    has taken recognisable shape. The medieval use of "golem" for an animated clay
    figure derives from this verse. Rendered "unformed substance" in L to preserve
    the hapax strangeness; "unformed body" in M for clarity; T surfaces the embryonic
    force.

H8503 (תַּכְלִית, taklit): "complete/perfect" hatred at 139:22 — the total,
    unreserved quality of the psalmist's enmity toward those who hate God. This is
    covenant solidarity language, not personal rage.

H4334 (מִישׁוֹר, mishor): "level ground" at 143:10 — the metaphor of a flat,
    safe plain contrasted with treacherous mountainous terrain. The divine Spirit
    leads the psalmist onto stable footing.

H6304 (פְּדוּת, peduth): Does not appear in this unit (it was in Ps 130). Noted
    for continuity reference only.

H2506 (חֵלֶק, cheleq): "portion" at 142:5 — the Levitical inheritance word.
    David, stripped of land and safety, names the LORD as his allotted share.
    Rendered "portion" in all tiers.

=== Textual-critical and manuscript notes ===

Ps 138:2 — The MT phrase כִּי-הִגְדַּלְתָּ עַל-כָּל-שִׁמְךָ אִמְרָתֶךָ ("for you have
    magnified your word above all your name") is syntactically unusual and ancient
    translators struggled with it. The LXX reads "you have made your holy name great
    above all things." The MT is retained: God's sworn word (imrah, promise) surpasses
    even the name — not because the name is lesser but because in this act the name
    has been fully committed. L renders the MT literally; M/T interpret accordingly.

Ps 139:16b — "When as yet there was none of them" refers to the days not yet existing
    at the time they were written in God's book — a striking pre-existence of the
    divine plan for each life.

Ps 141:5b — "Yet my prayer shall be against their evil deeds" — the Hebrew is
    genuinely obscure (כִּי-עוֹד וּתְפִלָּתִי בְּרָעוֹתֵיהֶם). The translation
    "yet my prayer is continually against their wicked works" (M/T) takes it as a
    qualification: the psalmist accepts reproof from the righteous but maintains
    his prayer posture against the wicked.

Ps 141:6-7 — These two verses are among the most difficult in the Psalter. The
    rendering adopted: v6 — when evil rulers are thrown down, people will find the
    psalmist's words welcome; v7 — the psalmist's experience of near-death (bones
    scattered at Sheol's mouth) like plowed earth. Both verses retain ambiguity in L;
    M/T go with the most defensible reading.

=== Aspect and tense notes ===

Ps 138: Perfects of certainty and completed action (I will praise — cohortative;
    you answered — perfect of historical fact). V8 uses a future-pointing imperfect
    for God's completing action.

Ps 139: The psalm is dominated by perfects (you have searched, you have hemmed, you
    have known) expressing not past tense but the accomplished and present completeness
    of God's knowing. V7 shifts to rhetorical imperfects (where shall I go? — nowhere).
    Vv13-16 move back to perfects of the completed creative act. The "book of days"
    clause in v16 uses a perfect of writing (all were written) with days being formed
    by imperfect (were fashioned).

Ps 140: Jussives throughout the imprecatory section (vv8-11) — wishes/prayers, not
    declarations. Perfects in vv1-2 for the ongoing evil character of the enemies.

Ps 141: V2 uses cohortatives (let my prayer be set forth) — petitionary. Jussives in
    vv3-4 (set, incline not). V5 uses imperative + cohortative. V9 is an imperative.

Ps 142: V1 uses two imperfect+cohortative combinations (I cry, I make supplication) —
    ongoing, earnest pleading. V3 is a temporal clause with perfect. Vv5-7 shift to
    imperfects of confidence.

Ps 143: V1-2 imperatives (hear, answer, enter not). V3 perfect (has pursued, has
    crushed, has made to dwell) — the assault is complete. V7 imperfects of urgency
    (answer me quickly). V10 jussives (let your Spirit lead).

=== OT intertextuality and NT connections ===

Ps 139:7 — "Where shall I go from your Spirit?" — echoed in the NT theology of the
    omnipresent Spirit (Acts 17:27-28; Heb 4:13).

Ps 139:13-16 — The womb-formation passage undergirds the biblical theology of life
    from conception (Jer 1:5; Luke 1:41-44). Paul's "you were bought with a price"
    (1 Cor 6:20) assumes this same dignity of embodied human creation.

Ps 139:16 — The "book of days" (cf. Rev 20:12; Rev 13:8) anticipates the apocalyptic
    imagery of the divine ledger. The language of "days formed" for each person grounds
    the NT doctrine of divine foreknowledge and election (Eph 1:4-5; Rom 8:29).

Ps 140:3 — "The poison of vipers is under their lips" — Paul quotes this verbatim in
    his depravity catena at Rom 3:13b (LXX), establishing human universal sinfulness.

Ps 142:5 — "You are my refuge, my portion" — the "portion" language echoes the Levitical
    tradition (Num 18:20; Deut 10:9) and anticipates the NT believer's inheritance in
    Christ (Eph 1:11, 14).

Ps 143:2 — "In your sight no one living is righteous" — this is one of Paul's direct
    sources for the doctrine of universal sinfulness (Rom 3:20; Gal 2:16). The
    psalmist's insight precedes Paul's exposition by a millennium.

Ps 143:10 — "Your good Spirit" leading on level ground — one of three OT texts where
    the Spirit is given a qualitative adjective (good here; holy at Ps 51:11 and Isa 63:10).
    The NT doctrine of the Spirit as guide (John 16:13; Rom 8:14) has its roots here.
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

  # ===========================================================================
  # Psalm 138 — Thanksgiving Before the Divine Assembly
  # David praises with his whole heart before the celestial council; the LORD
  # exalts his word above his name; he regards the lowly and perfects his purpose
  # ===========================================================================
  "138": {
    "1": {
      "L": "A Psalm of David. I will praise you, O LORD, with my whole heart; before the gods I will sing your praise.",
      "M": "A Psalm of David. I will praise you, O LORD, with all my heart; in the presence of the heavenly assembly I will sing your praises.",
      "T": "A Psalm of David.\nWith my whole heart I will praise you, O LORD;\nbefore the heavenly council I will sing your praises."
    },
    "2": {
      "L": "I will worship toward your holy temple and praise your name for your steadfast love and your faithfulness; for you have magnified your word above all your name.",
      "M": "I will bow down toward your holy temple and praise your name for your steadfast love and faithfulness; for you have exalted your promise above even your own name.",
      "T": "I bow toward your holy temple\nand praise your name —\nfor your steadfast love, for your faithfulness.\nYou have exalted your word\nabove everything you are known by."
    },
    "3": {
      "L": "On the day I called, you answered me; you made me bold and strong in my soul.",
      "M": "On the day I called out, you answered me; you filled my soul with bold strength.",
      "T": "The day I called — you answered.\nYou made me bold,\nyou strengthened my soul."
    },
    "4": {
      "L": "All the kings of the earth shall praise you, O LORD, when they hear the words of your mouth.",
      "M": "All the kings of the earth will praise you, O LORD, when they hear the words you have spoken.",
      "T": "All the kings of the earth will praise you, O LORD —\nwhen they hear\nwhat you have spoken."
    },
    "5": {
      "L": "And they shall sing of the ways of the LORD, for great is the glory of the LORD.",
      "M": "They will sing of the paths of the LORD, for the glory of the LORD is great.",
      "T": "They will sing of the LORD's ways —\nfor the glory of the LORD\nis great."
    },
    "6": {
      "L": "For though the LORD is high, he regards the lowly; but the proud he knows from far away.",
      "M": "Though the LORD is exalted, he pays attention to the humble; but the arrogant he perceives from a distance.",
      "T": "Though the LORD is exalted on high,\nhe looks to the lowly.\nThe proud he knows —\nonly from afar."
    },
    "7": {
      "L": "Though I walk in the midst of trouble, you revive me; you stretch out your hand against the wrath of my enemies, and your right hand saves me.",
      "M": "Even when I walk through terrible trouble, you keep me alive; you reach out your hand against the fury of my enemies, and your right hand rescues me.",
      "T": "Though I walk through the middle of trouble —\nyou keep me alive.\nYou reach your hand against the fury of my enemies;\nyour right hand saves me."
    },
    "8": {
      "L": "The LORD will perfect that which concerns me; your steadfast love, O LORD, endures forever — do not forsake the works of your hands.",
      "M": "The LORD will fulfill his purpose for me; your steadfast love, O LORD, endures forever — do not abandon what your hands have made.",
      "T": "The LORD will complete what he has begun in me.\nYour steadfast love endures forever, O LORD.\nDo not forsake the work of your hands."
    }
  },

  # ===========================================================================
  # Psalm 139 — The God Who Knows and Is Everywhere
  # Divine omniscience (vv1-6), omnipresence (vv7-12), the womb (vv13-16),
  # precious thoughts (vv17-18), imprecation (vv19-22), surrender (vv23-24)
  # ===========================================================================
  "139": {
    "1": {
      "L": "To the chief Musician. A Psalm of David. O LORD, you have searched me and known me.",
      "M": "For the director of music. A Psalm of David. O LORD, you have searched me and you know me.",
      "T": "For the choir director. A Psalm of David.\nO LORD — you have searched me.\nYou know me."
    },
    "2": {
      "L": "You know my sitting down and my rising up; you discern my thought from afar.",
      "M": "You know when I sit and when I stand; you understand my thoughts before I even form them.",
      "T": "You know when I sit, when I rise.\nYou discern my thoughts\nfrom far away."
    },
    "3": {
      "L": "You search out my path and my lying down, and you are acquainted with all my ways.",
      "M": "You trace every path I walk and every place I rest; you are familiar with all my ways.",
      "T": "You trace my every path, my every rest.\nYou know all my ways\nbefore I walk them."
    },
    "4": {
      "L": "For there is not a word on my tongue but, O LORD, you know it altogether.",
      "M": "Before a word is on my tongue, you know it completely, O LORD.",
      "T": "Before a word is on my tongue —\nyou know it entirely,\nO LORD."
    },
    "5": {
      "L": "You hem me in behind and before, and you have laid your hand upon me.",
      "M": "You surround me on every side — behind and before — and you have laid your hand upon me.",
      "T": "You hem me in behind, you hem me in before,\nand your hand rests\nupon me."
    },
    "6": {
      "L": "Such knowledge is too wonderful for me; it is high, I cannot attain it.",
      "M": "This knowledge is beyond me — too wonderful, too high for me to grasp.",
      "T": "This knowledge is too wonderful for me —\ntoo high.\nI cannot reach it."
    },
    "7": {
      "L": "Where shall I go from your Spirit? Or where shall I flee from your presence?",
      "M": "Where can I go to escape your Spirit? Where can I flee from your presence?",
      "T": "Where can I go from your Spirit?\nWhere can I flee\nfrom your presence?"
    },
    "8": {
      "L": "If I ascend to heaven, you are there; if I make my bed in Sheol, there you are.",
      "M": "If I rise to heaven, you are there; if I make my bed in the grave, you are there too.",
      "T": "If I ascend to heaven — you are there.\nIf I make my bed in Sheol —\neven there."
    },
    "9": {
      "L": "If I take the wings of the morning and dwell in the uttermost parts of the sea,",
      "M": "If I fly away on the wings of the dawn and settle at the farthest edge of the sea,",
      "T": "If I take the wings of the dawn\nand settle at the far side\nof the sea —"
    },
    "10": {
      "L": "even there shall your hand lead me, and your right hand shall hold me fast.",
      "M": "even there your hand will guide me, and your right hand will hold me fast.",
      "T": "even there your hand will guide me,\nyour right hand\nwill hold me."
    },
    "11": {
      "L": "If I say, 'Surely the darkness shall cover me, and the light around me become night' —",
      "M": "If I say, 'The darkness will surely hide me, and the light around me turn to night' —",
      "T": "And if I say,\n'Surely the darkness will hide me,\nthe light around me become night' —"
    },
    "12": {
      "L": "even the darkness is not dark to you; the night is as bright as the day, for darkness and light are alike to you.",
      "M": "even the darkness is not dark to you; the night shines like the day, for darkness and light are the same to you.",
      "T": "even the darkness is not dark to you.\nThe night shines like the day —\ndarkness and light are both alike to you."
    },
    "13": {
      "L": "For you formed my inward parts; you knit me together in my mother's womb.",
      "M": "For you formed my inward parts; you wove me together in my mother's womb.",
      "T": "For you formed my inward parts —\nyou knit me together\nin my mother's womb."
    },
    "14": {
      "L": "I will praise you, for I am fearfully and wonderfully made; marvellous are your works, and my soul knows it full well.",
      "M": "I praise you because I am fearfully and wonderfully made — your works are marvellous, and my whole being knows it.",
      "T": "I praise you, for I am fearfully and wonderfully made.\nYour works are marvellous —\nmy soul knows it through and through."
    },
    "15": {
      "L": "My frame was not hidden from you when I was made in secret, when I was woven in the depths of the earth.",
      "M": "My very frame was not hidden from you when I was made in secret, skillfully crafted in the depths of the earth.",
      "T": "My frame was not hidden from you\nwhen I was made in secret —\nskillfully woven in the depths of the earth."
    },
    "16": {
      "L": "Your eyes saw my unformed substance; in your book were written, all the days that were formed for me, when as yet there was none of them.",
      "M": "Your eyes saw my unformed body; all my days were written in your book before any of them had come to be.",
      "T": "Your eyes saw my unformed body.\nIn your book were written\nall the days formed for me —\nbefore a single one had come."
    },
    "17": {
      "L": "How precious to me are your thoughts, O God! How vast is the sum of them!",
      "M": "How priceless are your thoughts toward me, O God! How immeasurable their total!",
      "T": "How precious are your thoughts toward me, O God!\nHow vast\ntheir sum!"
    },
    "18": {
      "L": "Were I to count them, they would outnumber the grains of sand; when I awake I am still with you.",
      "M": "If I tried to count them, they would be more than the grains of sand; and when I wake, I am still with you.",
      "T": "Were I to count them,\nthey would outnumber grains of sand.\nWhen I wake —\nI am still with you."
    },
    "19": {
      "L": "O that you would slay the wicked, O God! Away from me, you men of blood!",
      "M": "O God, if only you would put an end to the wicked! Get away from me, you murderers!",
      "T": "O God — if only you would destroy the wicked!\nAway from me,\nyou bloodstained men!"
    },
    "20": {
      "L": "who speak against you wickedly, and your enemies take your name in vain.",
      "M": "They speak against you with evil intent; your adversaries invoke your name for nothing.",
      "T": "They speak against you with wicked purpose;\nyour enemies lift up your name\nfor nothing."
    },
    "21": {
      "L": "Do I not hate those who hate you, O LORD? And do I not loathe those who rise up against you?",
      "M": "LORD, don't I hate those who hate you? Don't I despise those who rise up against you?",
      "T": "Do I not hate those who hate you, O LORD?\nDo I not loathe\nthose who rise against you?"
    },
    "22": {
      "L": "I hate them with complete hatred; I count them my own enemies.",
      "M": "I hate them with an absolute hatred; I number them among my enemies.",
      "T": "I hate them with a complete hatred —\nI count them\nmy enemies."
    },
    "23": {
      "L": "Search me, O God, and know my heart; test me and know my thoughts.",
      "M": "Search me, O God, and know my heart; put me to the test and see what I am thinking.",
      "T": "Search me, O God — know my heart.\nTest me —\nknow my thoughts."
    },
    "24": {
      "L": "See if there is any grievous way in me, and lead me in the everlasting way.",
      "M": "See if there is any harmful path in me, and lead me in the way that lasts forever.",
      "T": "See if there is any hurtful way within me —\nand lead me\nin the everlasting way."
    }
  },

  # ===========================================================================
  # Psalm 140 — Deliver Me from Violent Men
  # Of David; serpent-tongued schemers; snares; the LORD maintains justice;
  # imprecatory prayers answered by confidence in the LORD's righteous judgment
  # ===========================================================================
  "140": {
    "1": {
      "L": "To the chief Musician. A Psalm of David. Deliver me, O LORD, from evil men; preserve me from violent men,",
      "M": "For the director of music. A Psalm of David. Rescue me, O LORD, from evil men; protect me from violent men —",
      "T": "For the choir director. A Psalm of David.\nDeliver me, O LORD, from evil men;\npreserve me from violent men."
    },
    "2": {
      "L": "who devise evil in their heart and stir up wars continually.",
      "M": "who scheme wickedness in their hearts and stir up conflict every day.",
      "T": "Who devise evil in their hearts,\nstirring up conflict\nevery single day."
    },
    "3": {
      "L": "They have sharpened their tongues like a serpent; the poison of vipers is under their lips. Selah.",
      "M": "Their tongues are as sharp as a serpent's; viper venom is under their lips. Selah.",
      "T": "Their tongues are sharpened like a serpent's.\nViper venom\nis under their lips.\nSelah."
    },
    "4": {
      "L": "Keep me, O LORD, from the hands of the wicked; preserve me from violent men who have purposed to trip my steps.",
      "M": "Keep me, O LORD, from the clutches of the wicked; preserve me from violent men who intend to make me stumble.",
      "T": "Keep me, O LORD, from the hands of the wicked —\nfrom violent men who plan\nto trip my feet."
    },
    "5": {
      "L": "The proud have hidden a snare for me and cords; they have spread a net beside the path; they have set traps for me. Selah.",
      "M": "The arrogant have laid a trap for me and stretched out cords; they have spread a net along my path and set snares. Selah.",
      "T": "The proud have hidden a snare for me —\ncords and nets spread along the path.\nThey have set traps for me.\nSelah."
    },
    "6": {
      "L": "I say to the LORD, 'You are my God'; give ear, O LORD, to the voice of my supplications.",
      "M": "I say to the LORD, 'You are my God' — hear me, O LORD, and listen to my pleas for mercy.",
      "T": "I say to the LORD: You are my God.\nHear, O LORD,\nmy cries for mercy."
    },
    "7": {
      "L": "O Lord GOD, the strength of my salvation, you have covered my head in the day of battle.",
      "M": "O Sovereign LORD, the strength of my salvation — you have shielded my head in the day of battle.",
      "T": "O Sovereign LORD,\nstrength of my salvation —\nyou shielded my head\nwhen battle raged."
    },
    "8": {
      "L": "Grant not, O LORD, the desires of the wicked; do not further their evil scheme, lest they be exalted. Selah.",
      "M": "Do not give the wicked what they want, O LORD; do not let their evil plans succeed, or they will grow proud. Selah.",
      "T": "Do not grant the wicked their wish, O LORD —\ndo not let their evil plot succeed,\nlest they rise in triumph.\nSelah."
    },
    "9": {
      "L": "As for the head of those who surround me, let the mischief of their own lips cover them.",
      "M": "Let the trouble caused by the words of those who hem me in fall back upon their own heads.",
      "T": "The evil of their lips —\nlet it fall\nupon their own heads."
    },
    "10": {
      "L": "Let burning coals fall upon them; let them be cast into the fire, into deep pits, never to rise again.",
      "M": "Let burning coals rain down on them; let them be thrown into the fire — into pits so deep they never rise.",
      "T": "Let burning coals fall upon them.\nLet them be thrown into the fire,\ninto pits so deep\nthey never rise."
    },
    "11": {
      "L": "Let not a slanderer be established in the land; let evil hunt down the man of violence to ruin.",
      "M": "Let no slander take root in the land; may evil relentlessly pursue the violent man until he falls.",
      "T": "Let no slander take root in the land.\nLet evil hunt down the violent man\nuntil he falls."
    },
    "12": {
      "L": "I know that the LORD will maintain the cause of the afflicted and the right of the poor.",
      "M": "I know that the LORD will uphold the cause of the oppressed and defend the rights of the poor.",
      "T": "I know this:\nthe LORD will uphold the cause of the afflicted,\nthe right of the poor."
    },
    "13": {
      "L": "Surely the righteous shall give thanks to your name; the upright shall dwell in your presence.",
      "M": "Surely the righteous will give thanks to your name; the upright will live in your presence.",
      "T": "The righteous will give thanks to your name.\nThe upright\nwill dwell in your presence."
    }
  },

  # ===========================================================================
  # Psalm 141 — An Evening Prayer; Guard My Mouth
  # Of David; incense and evening sacrifice imagery; the discipline of the righteous
  # welcomed; the danger of being drawn to the wicked; bones at Sheol's mouth
  # ===========================================================================
  "141": {
    "1": {
      "L": "A Psalm of David. O LORD, I call upon you; hasten to me! Give ear to my voice when I cry to you.",
      "M": "A Psalm of David. O LORD, I call on you — come quickly! Hear my voice when I cry out to you.",
      "T": "A Psalm of David.\nO LORD, I call to you — come quickly!\nHear my voice\nwhen I cry out."
    },
    "2": {
      "L": "Let my prayer be counted as incense before you, and the lifting up of my hands as the evening sacrifice.",
      "M": "May my prayer rise before you like incense, and the lifting up of my hands like the evening offering.",
      "T": "Let my prayer rise before you like incense —\nthe lifting up of my hands\nlike the evening offering."
    },
    "3": {
      "L": "Set a watch over my mouth, O LORD; keep guard over the door of my lips.",
      "M": "Post a guard at my mouth, O LORD; station a sentry at the door of my lips.",
      "T": "Set a guard over my mouth, O LORD;\nkeep watch\nover the door of my lips."
    },
    "4": {
      "L": "Do not let my heart incline to any evil thing, to practise deeds of wickedness with men who work iniquity, and let me not eat of their delicacies.",
      "M": "Do not let my heart be drawn to anything evil — to take part in the wicked acts of evildoers, or to taste any of their pleasures.",
      "T": "Do not let my heart be drawn toward evil —\ntoward doing the deeds of evildoers,\nor feasting at their table."
    },
    "5": {
      "L": "Let the righteous strike me — it is a kindness; let him reprove me — it is oil for my head; let my head not refuse it. Yet my prayer is still against their wicked deeds.",
      "M": "If a righteous man strikes me, I will take it as a kindness; if he rebukes me, it is like fine oil on my head — I will not refuse it. But my prayer remains against the deeds of the wicked.",
      "T": "Let the righteous strike me — that is kindness.\nLet him rebuke me — that is oil on my head.\nI will not refuse it.\nYet my prayer is still against their evil works."
    },
    "6": {
      "L": "When their rulers are thrown down from rocky heights, they shall hear my words, for they are pleasant.",
      "M": "When their leaders are hurled down from the cliffs, the people will find my words welcome.",
      "T": "When their rulers are cast down from rocky heights,\nthe people will hear my words\nand find them good."
    },
    "7": {
      "L": "As when one plows and breaks up the earth, our bones are scattered at the mouth of Sheol.",
      "M": "Like clods of earth turned up by the plowshare, our bones lie scattered at the brink of the grave.",
      "T": "Like earth turned up by the plow —\nour bones lie scattered\nat the mouth of Sheol."
    },
    "8": {
      "L": "But my eyes are toward you, O Lord GOD; in you I take refuge; do not leave my soul destitute.",
      "M": "But my eyes are fixed on you, O Lord GOD — in you I shelter; do not leave me exposed.",
      "T": "But my eyes are fixed on you, O Lord GOD.\nIn you I take refuge —\ndo not leave my soul bare."
    },
    "9": {
      "L": "Keep me from the trap they have laid for me, and from the snares of evildoers.",
      "M": "Keep me from the trap they have set for me, and from the snares that evildoers have laid.",
      "T": "Keep me from the trap they have laid —\nfrom the snares\nof those who do evil."
    },
    "10": {
      "L": "Let the wicked fall into their own nets, while I pass safely by.",
      "M": "Let the wicked tumble into their own nets while I escape unharmed.",
      "T": "Let the wicked fall into their own nets —\nwhile I\npass safely by."
    }
  },

  # ===========================================================================
  # Psalm 142 — A Prayer from the Cave
  # Maskil of David; complete isolation and desolation; the LORD as refuge
  # and portion; confidence that the righteous will gather when he is freed
  # ===========================================================================
  "142": {
    "1": {
      "L": "A Maskil of David, a prayer when he was in the cave. With my voice I cry to the LORD; with my voice I make supplication to the LORD.",
      "M": "A Maskil of David, a prayer composed when he was in the cave. With full voice I cry out to the LORD; with full voice I plead with him for mercy.",
      "T": "A Maskil. Of David. A prayer when he was in the cave.\nWith my full voice I cry to the LORD;\nwith my full voice I plead for his mercy."
    },
    "2": {
      "L": "I pour out my complaint before him; I declare my trouble before him.",
      "M": "I pour out my troubles before him; I lay my distress before him.",
      "T": "I pour out my complaint before him;\nI lay my trouble\nbefore him."
    },
    "3": {
      "L": "When my spirit is overwhelmed within me, you know my path. In the way where I walk they have hidden a snare for me.",
      "M": "When my spirit grows faint within me, you know my way. In the path I must travel, they have hidden a trap for me.",
      "T": "When my spirit grows faint within me —\nyou know my path.\nIn the way I walk\nthey have hidden a trap."
    },
    "4": {
      "L": "I look to the right and see — there is no one who takes notice of me; refuge fails me; no one cares for my soul.",
      "M": "I look to my right — no one acknowledges me; all escape is cut off from me; not a soul cares for me.",
      "T": "I look to the right — no one acknowledges me.\nAll escape is cut off.\nNot a soul cares for me."
    },
    "5": {
      "L": "I cry to you, O LORD; I say, 'You are my refuge, my portion in the land of the living.'",
      "M": "I cry to you, O LORD; I say, 'You are my shelter and my portion in this living world.'",
      "T": "I cry to you, O LORD.\nYou are my refuge —\nmy portion in the land of the living."
    },
    "6": {
      "L": "Give heed to my cry, for I am brought very low; deliver me from my persecutors, for they are stronger than I.",
      "M": "Hear my cry, for I have been brought very low; rescue me from those who pursue me, for they are too strong for me.",
      "T": "Hear my cry — I am brought very low.\nDeliver me from those who pursue me;\nthey are stronger than I am."
    },
    "7": {
      "L": "Bring my soul out of prison, that I may give thanks to your name! The righteous will surround me, for you will deal bountifully with me.",
      "M": "Lead my soul out of this prison so I can praise your name. Then the righteous will gather around me, because you will have been generous to me.",
      "T": "Bring my soul out of prison —\nthat I may praise your name.\nThe righteous will gather around me,\nfor you will deal generously with me."
    }
  },

  # ===========================================================================
  # Psalm 143 — A Penitential Psalm; Teach Me to Do Your Will
  # The seventh Penitential Psalm; no one righteous before God; the enemy's
  # crushing assault; meditation on God's past works; thirsting; the good Spirit
  # ===========================================================================
  "143": {
    "1": {
      "L": "A Psalm of David. Hear my prayer, O LORD; give ear to my supplications; in your faithfulness answer me, in your righteousness.",
      "M": "A Psalm of David. O LORD, hear my prayer; listen to my pleas for mercy; in your faithfulness and righteousness, answer me.",
      "T": "A Psalm of David.\nHear my prayer, O LORD;\nlisten to my cries for mercy.\nAnswer me — in your faithfulness,\nin your righteousness."
    },
    "2": {
      "L": "Enter not into judgment with your servant, for in your sight no living person is righteous.",
      "M": "Do not bring your servant into judgment, for no one alive can stand as righteous before you.",
      "T": "Do not bring your servant into judgment —\nfor no one living\nis righteous before you."
    },
    "3": {
      "L": "For the enemy has pursued my soul; he has crushed my life to the ground; he has made me sit in darkness like those long dead.",
      "M": "For the enemy has hunted me down and crushed my life to the ground; he has forced me to dwell in darkness like those who died long ago.",
      "T": "The enemy has chased my soul —\ncrushed my life to the ground —\nforced me to dwell in darkness\nlike the long dead."
    },
    "4": {
      "L": "Therefore my spirit is overwhelmed within me; my heart within me is appalled.",
      "M": "So my spirit grows faint within me; my heart within me is filled with dismay.",
      "T": "My spirit grows faint within me;\nmy heart\nis numb."
    },
    "5": {
      "L": "I remember the days of old; I meditate on all your deeds; I ponder the work of your hands.",
      "M": "I call to mind the days of old; I meditate on all you have done; I reflect on the work of your hands.",
      "T": "I remember the days of old;\nI meditate on all you have done —\nI ponder the work of your hands."
    },
    "6": {
      "L": "I stretch out my hands to you; my soul thirsts for you like a parched land. Selah.",
      "M": "I reach out my hands toward you; my whole being longs for you like a land parched for rain. Selah.",
      "T": "I stretch out my hands to you.\nMy soul thirsts for you\nlike parched earth.\nSelah."
    },
    "7": {
      "L": "Answer me quickly, O LORD; my spirit fails! Hide not your face from me, lest I be like those who go down to the pit.",
      "M": "Answer me quickly, O LORD — my spirit is failing! Do not hide your face from me, or I will be like those who sink into the grave.",
      "T": "Answer me quickly, O LORD —\nmy spirit fails!\nDo not hide your face from me,\nor I will be like those who go down to the pit."
    },
    "8": {
      "L": "Let me hear of your steadfast love in the morning, for in you I trust; make me know the way I should walk, for to you I lift up my soul.",
      "M": "Let me hear of your steadfast love in the morning, for in you I put my trust; show me the path I should take, for I lift my soul to you.",
      "T": "In the morning let me hear of your steadfast love —\nfor in you I trust.\nShow me the way I should walk —\nfor to you I lift my soul."
    },
    "9": {
      "L": "Deliver me from my enemies, O LORD; I flee to you for cover.",
      "M": "Rescue me from my enemies, O LORD — I run to you for shelter.",
      "T": "Rescue me from my enemies, O LORD.\nTo you I flee\nfor cover."
    },
    "10": {
      "L": "Teach me to do your will, for you are my God; let your good Spirit lead me on level ground.",
      "M": "Teach me to do your will, for you are my God; may your good Spirit lead me on a level path.",
      "T": "Teach me to do your will —\nyou are my God.\nMay your good Spirit\nlead me on level ground."
    },
    "11": {
      "L": "For your name's sake, O LORD, revive me! In your righteousness bring my soul out of trouble.",
      "M": "For the sake of your name, O LORD, keep me alive; in your righteousness lead my soul out of its distress.",
      "T": "For your name's sake, O LORD — keep me alive!\nIn your righteousness\nbring my soul out of trouble."
    },
    "12": {
      "L": "And in your steadfast love cut off my enemies, and destroy all who afflict my soul, for I am your servant.",
      "M": "And in your steadfast love silence my enemies and put an end to all who oppress me — for I am your servant.",
      "T": "In your steadfast love — cut off my enemies.\nDestroy all who oppress my soul.\nFor I am your servant."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 138–143 written.')

if __name__ == '__main__':
    main()
