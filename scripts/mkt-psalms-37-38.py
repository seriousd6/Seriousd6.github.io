"""
MKT Psalms chapters 37–38 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-37-38.py

=== Overview of this unit ===

Ps 37 (40 v) — A wisdom acrostic of David; each two-verse pair begins with a
    successive letter of the Hebrew alphabet. The psalm's central question: why do
    the wicked prosper? The answer is temporal contrast — the wicked's prosperity
    is grass-brief, the righteous person's inheritance is earth-permanent. The
    refrain "inherit the earth/land" (H3423 + H776) appears six times (vv9,11,22,
    29,34; implied in v18). Jesus quotes v11 directly in the Beatitudes (Matt 5:5).
    Theological spine: trust the LORD → he will act → the wicked will vanish →
    the righteous remain forever. The psalm never minimises the wicked's apparent
    success; it reframes it in God's sovereign timeline.

Ps 38 (22 v) — One of the seven classic Penitential Psalms (Pss 6,32,38,51,
    102,130,143), this is among the most viscerally physical. Superscription:
    "to bring to remembrance" (ledazkir — used as a memorial offering before God,
    cf. Num 5:15). Structure: God's discipline = arrows and hand (vv1–2) →
    body inventory of illness, shame, and exhaustion (vv3–10) → social isolation
    (v11) → enemies exploiting silence (vv12–14) → hope placed in the LORD alone
    (vv15–16) → the hinge: confession of sin (vv17–18) → contrast with vigorous
    enemies (vv19–20) → closing plea for nearness and rescue (vv21–22). The body-
    language throughout (stench, bent posture, inflamed loins, groaning, failing
    eyes) serves the psalm's purpose: to dramatise that unaddressed sin is
    physically as well as spiritually corrosive. V18 ("I confess my iniquity; I am
    troubled by my sin") is the emotional and theological centre.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (all-caps small-caps convention) in L/M throughout.
      In T: "LORD" — consistent with all prior MKT Psalms scripts.

H136 (אֲדֹנָי, Adonai): Appears at Ps 37:13; 38:9,15,22. Rendered "Lord"
      (capitalised, not all-caps) in L/M/T to distinguish from YHWH. The
      psalmist switches registers: Adonai = the sovereign master; YHWH = the
      covenant personal name. This distinction is preserved.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Contextually singular.

H776 (אֶרֶץ, erets): "earth" consistently in Ps 37 (vv9,11,22,29,34). The
      original context is the Land of Promise, but the Beatitude citation (Matt
      5:5) extends the sense cosmically. Using "earth" rather than "land" honours
      both registers without flattening either. T notes the eschatological
      extension on first occurrence.

H2617 (חֶסֶד, chesed): Not present in Ps 37 or 38 interlinear tokens, so no
      direct rendering needed. The concept underlies the LORD's faithful action
      throughout Ps 37.

H5771 (עֲוֹן, avon): "iniquity" in L; "wrongdoing" or "guilt" in M/T by context.
      Ps 38:4 ("my iniquities") = the accumulated weight of moral crookedness.
      Ps 38:18 ("I confess my iniquity") = the decisive act of naming it before God.

H2403 (חַטָּאָה, chattaah): "sin" in all tiers (Ps 38:3,18). The missing-the-mark
      word; kept as "sin" because "sin" in English still carries this semantic
      weight.

H6035 (עָנָו, anav): "meek" in L/M/T (Ps 37:11). The afflicted, lowly, those
      without worldly advantage. Jesus adopts the term whole from the Septuagint.
      "Meek" is retained in all tiers; T makes the contrastive force explicit.

H7307 (רוּחַ, ruach): Not present in these psalms.

H5315 (נֶפֶשׁ, nefesh): Ps 38:12 — "after my life" = they seek my embodied
      existence. Rendered "life" in M/T. L: "soul" (lit. their goal is my nefesh).

H6588 (פֶּשַׁע, pesha): Not present in these psalms.

H5542 (סֶלָה, selah): Not present in these psalms (neither interlinear shows it).

=== Aspect and tense notes ===

Ps 37 — Primarily imperative mood (commands to the reader) alternating with
    perfect verbs (testimony of completed, certain future acts stated as done):
    vv1-2: Jussive negatives ("do not fret") — prohibition against ongoing fretting.
    vv3-8: Imperatives ("trust," "delight," "commit," "be still") — wisdom commands.
    vv9-40: Imperfects and perfects marking what WILL happen (cut off, inherit,
    vanish) stated with the rhetorical certainty of prophetic perfect.
    L preserves grammatical awkwardness where the Hebrew inverts word order.
    M/T smooth to natural English sequence.

Ps 38 — Almost entirely first-person perfect and imperfect describing ongoing
    experience: "my wounds stink" (present), "I have seen" (completed experience),
    "I am ready to fall" (imminent). The psalm is a real-time lament, not a
    retrospective. T preserves the urgent, present-tense feel.

=== OT echo notes ===

Ps 37:11 — Cited verbatim in Matt 5:5 (the third Beatitude). Jesus's Greek
    follows the LXX exactly (πραεῖς κληρονομήσουσιν τὴν γῆν). The eschatological
    expansion from "the land" (promised land) to "the earth" (renewed creation)
    is already implicit in the psalm's scope. T notes this at v11 without over-reading.

Ps 37:23-24 — The steps-of-a-man imagery echoes Proverbs 20:24 ("A man's steps
    are directed by the LORD") and Proverbs 16:9. The wisdom tradition consistently
    places human planning under divine ordering.

Ps 38:1 — Opening formula ("rebuke me not in your wrath") echoes Ps 6:1 exactly.
    Both are penitential psalms; the identical opening creates a deliberate Psalter
    linkage. T notes the echo.

Ps 38:18 — The confession at the psalm's hinge anticipates Ps 51's movement from
    accusation to confession. The sequence (acknowledge → confess → declare) is
    the pattern the Psalter returns to repeatedly as the response to divine discipline.
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
  # Psalm 37 — Wisdom Acrostic: Trust God; Do Not Fret
  # ============================================================
  "37": {
    "1": {
      "L": "A Psalm of David. Do not fret yourself over evildoers; do not be envious against those who work iniquity.",
      "M": "Of David. Do not let evildoers upset you; do not envy those who do wrong.",
      "T": "Of David.\nDo not burn with resentment over the wicked.\nDo not envy those who do harm."
    },
    "2": {
      "L": "For like the grass they will soon be cut down, and as the green plant they will wither.",
      "M": "For like grass they will soon be cut down; like green plants they will wither away.",
      "T": "They are grass. Cut down, and soon.\nLike green growth in the heat—they will wither."
    },
    "3": {
      "L": "Trust in the LORD and do good; dwell in the land, and feed on faithfulness.",
      "M": "Trust in the LORD and do good; live in the land and enjoy secure provision.",
      "T": "Trust the LORD—and act on it.\nLive in the land. Feed on what faithfulness provides."
    },
    "4": {
      "L": "Delight yourself in the LORD, and he will give you the desires of your heart.",
      "M": "Find your delight in the LORD, and he will give you the desires of your heart.",
      "T": "Take your deepest pleasure in the LORD himself—\nand he will give you everything your heart has been asking for."
    },
    "5": {
      "L": "Roll your way upon the LORD; trust also in him, and he will act.",
      "M": "Commit your way to the LORD; trust in him, and he will bring it to pass.",
      "T": "Roll your burden of a path onto the LORD.\nTrust him—and watch him move."
    },
    "6": {
      "L": "He shall bring forth your righteousness as the light, and your justice as the noonday.",
      "M": "He will bring your righteousness to light and your cause bright as noon.",
      "T": "He will make your righteousness break through like sunrise—\nyour vindication blazing at midday."
    },
    "7": {
      "L": "Be still before the LORD and wait patiently for him; do not fret yourself over the man who prospers in his way, the one who carries out wicked schemes.",
      "M": "Be still before the LORD and wait patiently for him; do not resent the one who prospers in his way, who carries out his evil plans.",
      "T": "Be still before the LORD.\nWait for him—quietly, without straining.\nDo not burn with resentment over the person who seems to get everything they want,\nthe one whose wicked schemes keep working."
    },
    "8": {
      "L": "Cease from anger and forsake wrath; do not fret yourself—it only leads to evil.",
      "M": "Let go of anger and abandon wrath; do not fret—it leads only to evil.",
      "T": "Let anger go.\nAbandon wrath.\nStop fuming—it only takes you somewhere you do not want to go."
    },
    "9": {
      "L": "For evildoers shall be cut off, but those who wait for the LORD shall inherit the earth.",
      "M": "For the wicked will be cut off, but those who wait for the LORD will inherit the earth.",
      "T": "The wicked will be cut off—every one of them.\nBut those who wait for the LORD will possess the earth."
    },
    "10": {
      "L": "Yet a little while, and the wicked will be no more; though you look carefully for his place, he will not be there.",
      "M": "In just a little while the wicked will be gone; you will search for his place, but it will not be found.",
      "T": "A short while more—and the wicked simply vanish.\nYou will look for them where they were.\nNothing."
    },
    "11": {
      "L": "But the meek shall inherit the earth, and shall delight themselves in the abundance of peace.",
      "M": "But the meek will inherit the earth and delight in abundant peace.",
      "T": "The meek will inherit the earth—not the aggressive, not the successful schemers, but the meek.\nAnd they will feast on a peace that has no limit.\n[Jesus lifts this promise directly into the Sermon on the Mount: Matthew 5:5.]"
    },
    "12": {
      "L": "The wicked plots against the righteous and gnashes his teeth at him.",
      "M": "The wicked man schemes against the righteous and grinds his teeth at him.",
      "T": "The wicked brood over plots against the righteous.\nThey grind their teeth in hatred."
    },
    "13": {
      "L": "The Lord laughs at him, for he sees that his day is coming.",
      "M": "The Lord laughs at the wicked, for he sees that their day is coming.",
      "T": "The Lord laughs—that deep, unhurried laugh—\nbecause he already sees the day that is coming for them."
    },
    "14": {
      "L": "The wicked have drawn the sword and bent their bow to cast down the poor and needy, to cut down those of upright conduct.",
      "M": "The wicked draw the sword and bend their bow to bring down the poor and helpless, to kill those who walk uprightly.",
      "T": "The wicked draw their swords and string their bows—\ntheir target: the poor, the helpless,\nthose who do nothing but live right."
    },
    "15": {
      "L": "Their sword shall enter their own heart, and their bows shall be broken.",
      "M": "Their swords will pierce their own hearts, and their bows will be shattered.",
      "T": "Their swords will go straight into their own hearts.\nEvery bow they drew will snap."
    },
    "16": {
      "L": "Better is the little of the righteous than the great riches of many wicked.",
      "M": "Better is the little that the righteous has than the great wealth of many wicked.",
      "T": "A righteous person's little is worth more\nthan the stacked fortunes of any number of wicked."
    },
    "17": {
      "L": "For the arms of the wicked shall be broken, but the LORD upholds the righteous.",
      "M": "For the strength of the wicked will be shattered, but the LORD supports the righteous.",
      "T": "The power the wicked rely on will be broken.\nBut the LORD holds the righteous up."
    },
    "18": {
      "L": "The LORD knows the days of the blameless, and their inheritance shall be forever.",
      "M": "The LORD knows the days of the upright, and their inheritance will last forever.",
      "T": "The LORD has his eye on every day of those who live with integrity.\nWhat he is keeping for them will never end."
    },
    "19": {
      "L": "They shall not be ashamed in the evil time, and in the days of famine they shall be satisfied.",
      "M": "They will not be disgraced in days of trouble; in times of famine they will be satisfied.",
      "T": "When trouble comes—when things are at their worst—they will not be disgraced.\nWhen famine comes, they will still have enough."
    },
    "20": {
      "L": "But the wicked shall perish, and the enemies of the LORD, as the finest of lambs, shall vanish—like smoke they shall be consumed.",
      "M": "The wicked will perish; the enemies of the LORD will fade like green pastures—they will dissolve, consumed like smoke.",
      "T": "The wicked will perish.\nThe LORD's enemies, for all their apparent glory,\nwill fade like pasture grass in summer heat—\nburned off, gone, vanishing into smoke."
    },
    "21": {
      "L": "The wicked borrows and does not pay back, but the righteous is gracious and gives.",
      "M": "The wicked borrows and does not repay, but the righteous is generous and gives.",
      "T": "The wicked borrows and never repays.\nThe righteous gives freely—that is simply their character."
    },
    "22": {
      "L": "For those blessed by the LORD shall inherit the earth, but those cursed by him shall be cut off.",
      "M": "Those blessed by the LORD will inherit the earth, but those he has cursed will be cut off.",
      "T": "The LORD's blessing carries the inheritance of the earth.\nThe LORD's curse carries being cut off entirely."
    },
    "23": {
      "L": "The steps of a man are established by the LORD, and he delights in his way.",
      "M": "The LORD establishes the steps of a man and delights in his way.",
      "T": "The LORD is the one who makes a person's steps firm.\nHe takes pleasure in watching that life unfold."
    },
    "24": {
      "L": "Though he falls, he shall not be hurled down, for the LORD upholds him with his hand.",
      "M": "Though he stumbles, he will not fall headlong, for the LORD holds his hand.",
      "T": "If he stumbles, he will not crash—\nbecause the LORD has his hand."
    },
    "25": {
      "L": "I have been young, and now am old; yet I have not seen the righteous forsaken, nor his offspring begging for bread.",
      "M": "I was young and now I am old, yet I have never seen the righteous abandoned or their children begging for food.",
      "T": "I speak from long experience:\nI have never seen God abandon a righteous person—\nnever seen their children having to beg for food."
    },
    "26": {
      "L": "He is ever showing mercy and lending, and his offspring are a blessing.",
      "M": "He is always generous and lending, and his children become a blessing.",
      "T": "The righteous person is always giving—always lending what they can.\nTheir children are a blessing to everyone around them."
    },
    "27": {
      "L": "Turn from evil and do good; so shall you dwell forever.",
      "M": "Turn away from evil and do good, so you will live in the land permanently.",
      "T": "Turn away from evil.\nDo good instead.\nThat is the path to remaining—permanently—where God has placed you."
    },
    "28": {
      "L": "For the LORD loves justice; he will not forsake his faithful ones. They are kept forever, but the offspring of the wicked shall be cut off.",
      "M": "For the LORD loves justice; he does not abandon his faithful people. They are kept safe forever, but the offspring of the wicked will be cut off.",
      "T": "The LORD loves justice—that is a settled truth.\nHe will not abandon those who are faithful to him.\nHe keeps them—always.\nBut the children of the wicked inherit nothing but the cut-off."
    },
    "29": {
      "L": "The righteous shall inherit the land and dwell in it forever.",
      "M": "The righteous will inherit the earth and make their home in it forever.",
      "T": "The righteous will receive the earth as their home—\nand they will live in it, permanently."
    },
    "30": {
      "L": "The mouth of the righteous utters wisdom, and his tongue speaks justice.",
      "M": "The righteous speak wisdom, and their tongue talks of justice.",
      "T": "Wisdom comes out of the righteous person's mouth.\nEvery word they say leans toward what is right."
    },
    "31": {
      "L": "The law of his God is in his heart; none of his steps shall slip.",
      "M": "The law of his God is in his heart; his steps do not falter.",
      "T": "God's instruction lives deep in this person's heart.\nThat is why they do not stumble."
    },
    "32": {
      "L": "The wicked watches for the righteous and seeks to slay him.",
      "M": "The wicked lie in wait for the righteous, looking to kill them.",
      "T": "The wicked stake out the righteous—\nthey want them dead."
    },
    "33": {
      "L": "The LORD will not abandon him to his power, nor condemn him when he is judged.",
      "M": "The LORD will not leave the righteous at the mercy of the wicked or let them be condemned at trial.",
      "T": "The LORD will not hand them over.\nWhen the trial comes, he will not let them be condemned."
    },
    "34": {
      "L": "Wait for the LORD and keep his way, and he will exalt you to inherit the land; when the wicked are cut off, you will see it.",
      "M": "Wait for the LORD and keep his way; he will exalt you to inherit the earth. You will be there to see the wicked cut off.",
      "T": "Wait for the LORD.\nKeep to his way.\nHe will lift you up to receive the earth—\nand you will be there to see the wicked eliminated."
    },
    "35": {
      "L": "I have seen the wicked in great power, spreading himself like a thriving native tree.",
      "M": "I have seen a ruthless wicked man towering like a flourishing tree in its native ground.",
      "T": "I have watched the wicked—powerful, ruthless—\nspread out like a lush tree in rich soil,\nlooking as though they have always been here and always will be."
    },
    "36": {
      "L": "Yet he passed away, and behold, he was no more; I sought for him, but he could not be found.",
      "M": "But he passed away—gone; I looked for him and he could not be found.",
      "T": "And then he was simply gone.\nI looked where he had been.\nNothing."
    },
    "37": {
      "L": "Mark the blameless man and observe the upright, for the future of that man is peace.",
      "M": "Take note of the blameless person and look at the upright; the future of such a person is peace.",
      "T": "Watch the blameless person.\nNotice what those who live uprightly look like.\nThe future they are walking toward is peace."
    },
    "38": {
      "L": "But transgressors shall all be destroyed together; the future of the wicked shall be cut off.",
      "M": "But rebels will all be destroyed together; the future of the wicked will be cut off.",
      "T": "But the rebels—every one of them—will be destroyed together.\nThe wicked have no future. It has already been cut off."
    },
    "39": {
      "L": "But the salvation of the righteous is from the LORD; he is their strength in the time of trouble.",
      "M": "The salvation of the righteous comes from the LORD; he is their stronghold in times of trouble.",
      "T": "When the righteous need rescuing, the LORD is the one who rescues them.\nHe is their fortress when trouble comes."
    },
    "40": {
      "L": "The LORD helps them and delivers them; he delivers them from the wicked and saves them, because they take refuge in him.",
      "M": "The LORD helps and delivers them; he rescues them from the wicked and saves them, because they take shelter in him.",
      "T": "The LORD is their help.\nHe pulls them free—again and again—from the grip of the wicked.\nHe saves them.\nAll because they made him their refuge."
    }
  },

  # ============================================================
  # Psalm 38 — Penitential Lament: Confession under Discipline
  # ============================================================
  "38": {
    "1": {
      "L": "A Psalm of David, to bring to remembrance. O LORD, rebuke me not in your wrath, nor discipline me in your hot displeasure.",
      "M": "Of David, as a memorial offering. LORD, do not rebuke me in your anger, or discipline me in your fury.",
      "T": "Of David. Offered as a memorial before God.\nLORD, do not correct me while burning with anger.\nDo not discipline me in the heat of your fury.\n[This opening echoes Psalm 6:1 exactly — two penitential psalms that share an entry wound.]"
    },
    "2": {
      "L": "For your arrows have sunk into me, and your hand has pressed down hard on me.",
      "M": "Your arrows have pierced me deeply, and your hand has come down hard on me.",
      "T": "Your arrows are sunk deep into me.\nYour hand is pressing down, and it does not lift."
    },
    "3": {
      "L": "There is no soundness in my flesh because of your anger; there is no health in my bones because of my sin.",
      "M": "My body has no soundness because of your anger; my bones have no rest because of my sin.",
      "T": "There is nothing sound in my body—your anger has seen to that.\nMy very bones have no peace—because of what I have done."
    },
    "4": {
      "L": "For my iniquities have gone over my head; like a heavy burden they are too heavy for me.",
      "M": "My iniquities have overwhelmed me—they are a burden too heavy to carry.",
      "T": "My wrongdoings have risen over my head like floodwater.\nThey are a weight I cannot lift—\nheavy beyond endurance."
    },
    "5": {
      "L": "My wounds are foul and festering because of my foolishness.",
      "M": "My wounds stink and fester because of my own foolishness.",
      "T": "My wounds have gone rotten—putrid—\nbecause of my own foolishness."
    },
    "6": {
      "L": "I am bent down and greatly bowed; I go about mourning all the day.",
      "M": "I am bowed low and hunched over; I walk about mourning all day long.",
      "T": "I walk bent over, hunched to the ground.\nAll day long I move through life in mourning."
    },
    "7": {
      "L": "For my loins are filled with burning, and there is no soundness in my flesh.",
      "M": "My loins are on fire with disease, and there is no health anywhere in my body.",
      "T": "My loins burn with inflammation.\nThere is not one sound part in me."
    },
    "8": {
      "L": "I am feeble and utterly crushed; I groan because of the turmoil of my heart.",
      "M": "I am benumbed and utterly crushed; I cry out from the anguish of my heart.",
      "T": "I am numb and broken.\nThe groaning comes from somewhere deeper than I can reach—\nthe turmoil of a heart that cannot settle."
    },
    "9": {
      "L": "Lord, all my longing is before you; my sighing is not hidden from you.",
      "M": "Lord, all my longing is laid out before you; my groaning is not hidden from you.",
      "T": "Lord, you see it all.\nEvery aching desire I have is open before you.\nMy sighs are not hidden."
    },
    "10": {
      "L": "My heart throbs; my strength has left me, and the light of my eyes—it too is gone from me.",
      "M": "My heart pounds; my strength has failed, and even the light of my eyes has deserted me.",
      "T": "My heart pounds wildly.\nMy strength is gone.\nThe very light in my eyes has dimmed and left."
    },
    "11": {
      "L": "My loved ones and my friends stand far from my plague, and my kinsmen stand at a distance.",
      "M": "My friends and companions keep away from my affliction, and even my relatives stand at a distance.",
      "T": "The people who love me stay away from where I am sick.\nFriends, companions, close family—\nthey all keep their distance."
    },
    "12": {
      "L": "Those who seek my soul lay snares for me; those who seek my hurt speak of ruin and all day long plot deceits.",
      "M": "Those who want me dead set traps for me; those who seek to harm me speak of my destruction and scheme all day long.",
      "T": "My enemies have set traps for me—\nthey are after my life.\nAll day long they whisper ruin and rehearse their deceptions."
    },
    "13": {
      "L": "But I am as a deaf man who does not hear, and as a mute man who does not open his mouth.",
      "M": "But I am like someone who cannot hear—I do not listen; like someone mute who cannot speak.",
      "T": "But I say nothing.\nI am a deaf man who hears nothing,\na mute who does not open his mouth."
    },
    "14": {
      "L": "I have become as a man who does not hear, and in whose mouth are no rebukes.",
      "M": "I am like a man who does not hear, with no counter-arguments in his mouth.",
      "T": "I have become someone who does not even argue back—\nnot a word of rebuttal in my mouth."
    },
    "15": {
      "L": "For in you, O LORD, I hope; you will answer, O Lord my God.",
      "M": "But in you, LORD, I place my hope; you will answer, O Lord my God.",
      "T": "But my hope is in you, LORD—only you.\nYou will answer me, Lord, my God."
    },
    "16": {
      "L": "For I said, 'Lest they rejoice over me—those who magnify themselves against me when my foot slips.'",
      "M": "For I thought: Do not let them gloat over me—those who triumph over me when I stumble.",
      "T": "I kept thinking: Do not let them celebrate my collapse—\nthose who are already puffing themselves up over me,\nwaiting for my foot to slip."
    },
    "17": {
      "L": "For I am ready to fall, and my sorrow is before me continually.",
      "M": "For I am about to stumble and my pain is always with me.",
      "T": "I am on the verge of collapse.\nThe pain does not leave."
    },
    "18": {
      "L": "I will declare my iniquity; I am troubled because of my sin.",
      "M": "I confess my wrongdoing; I am distressed by my sin.",
      "T": "I am going to say it plainly: this is my wrongdoing.\nI am undone by what I have done.\n[This is the psalm's hinge — confession at the centre, the movement Ps 51 will map at full scale.]"
    },
    "19": {
      "L": "But my enemies are lively and strong, and those who hate me wrongfully are multiplied.",
      "M": "But my enemies are full of life and strong; those who hate me without cause have multiplied.",
      "T": "Meanwhile my enemies are vigorous—thriving.\nThe ones who hate me for no reason keep growing in number."
    },
    "20": {
      "L": "Those who repay evil for good are my adversaries because I pursue what is good.",
      "M": "Those who repay good with evil oppose me, because I pursue what is right.",
      "T": "They repay my goodness with evil—they accuse me\nprecisely because I have been pursuing what is right."
    },
    "21": {
      "L": "Do not forsake me, O LORD; O my God, do not be far from me.",
      "M": "Do not abandon me, LORD; my God, do not stay far away.",
      "T": "Do not leave me, LORD.\nMy God—please do not stay distant from me."
    },
    "22": {
      "L": "Make haste to help me, O Lord, my salvation.",
      "M": "Come quickly to help me, O Lord, my salvation.",
      "T": "Hurry to me, Lord—\nyou are my only salvation."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 37–38 written.')

if __name__ == '__main__':
    main()
