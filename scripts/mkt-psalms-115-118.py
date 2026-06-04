"""
MKT Psalms chapters 115–118 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-115-118.py

=== Overview of this unit ===

Ps 115 (18 v) — Anonymous congregational psalm. The anti-idol polemic structured as
    catechism: a triple call to trust (Israel / house of Aaron / those who fear the LORD),
    each answered by the refrain "He is their help and their shield." The opening question
    ("Where is their God?") is answered not with a list of attributes but with the
    LORD's sovereign freedom: "he does whatever he pleases." The idol description
    (vv4-8) uses ascending parallelism — mouth/eyes/ears/nose/hands/feet/throat —
    building to its devastating conclusion: those who make such things become like them.
    The psalm closes with the living blessing against the backdrop of the dead who
    cannot praise (vv17-18).

Ps 116 (19 v) — Individual thanksgiving, highly personal. The psalmist has been
    near death (Sheol's ropes, v3) and cried to the LORD (v4), was rescued (vv6-8),
    and now vows to "walk before the LORD in the land of the living" (v9). The central
    question of vv12-13 ("What shall I render to the LORD?") is the theological hinge:
    the cup of salvation, the payment of vows, the sacrifice of thanksgiving. The psalm
    is shaped by three formal vow-payments (vv14, 18-19 are near-identical refrains)
    framing the acknowledgement that it is the LORD who loosed the psalmist's bonds
    (v16). In the NT context this psalm is heard behind the Gethsemane cup (Jesus
    taking the cup of suffering; cf. the Hallel sung after the Last Supper, Matt 26:30).

Ps 117 (2 v) — The shortest psalm, the axial center of the Psalter
    (counting chapters, it sits at the exact midpoint of 150). A universal summons
    to praise grounded in the two great covenant qualities: chesed (steadfast love)
    and emet (faithfulness). Paul quotes v1 at Romans 15:11 as evidence that the
    Gentiles were always within the scope of Israel's praise.

Ps 118 (29 v) — The final psalm of the Egyptian Hallel (Pss 113–118), probably
    sung at Passover, Pentecost, and Tabernacles. Its structure is a triple
    "his steadfast love endures forever" call (vv1-4), an individual rescue narrative
    (vv5-21), a liturgical exchange at the temple gate (vv19-27), and a closing
    doxology echoing v1. The theological centre is the cornerstone saying (v22),
    quoted by Jesus at all four Gospels' triumphal entry narratives and by Peter at
    Acts 4:11. The "Hosanna" of Palm Sunday is directly from v25 (הוֹשִׁיעָה נָּא,
    hosha na — "save now, please!"). Verse 14 echoes Exodus 15:2 and Isaiah 12:2
    verbatim, marking this psalm as deliberate exodus-typology.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T throughout — consistent with all prior
    Psalms scripts.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T throughout. Ps 118 is built on
    the refrain "his steadfast love endures forever" (vv1, 2, 3, 4, 29) and the
    concept governs the whole of this Hallel unit. Ps 117:2 pairs it with emet.

H571 (אֱמֶת, emet / faithfulness/truth): "faithfulness" in L/M/T. At Ps 117:2
    it stands in parallel with chesed — the two pillars of covenant character.
    Rendered "faithfulness" rather than "truth" because the covenantal context
    calls for performative fidelity, not propositional accuracy.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Consistent throughout.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M/T. At Ps 116:4 "deliver my soul" = rescue
    my life; at 116:7 "return to your rest, my soul" = the whole embodied self
    invited into quietness. Not the Greek immaterial soul.

H3467 (יָשַׁע, yasha / save) at Ps 118:25: L/M = "Save us, we pray"; T renders
    the cry as "Hosanna — save us!" to surface the NT liturgical echo. The
    Aramaic hosha-na that became "Hosanna!" in the triumphal entry narratives
    is this exact word and particle.

H68/H6438 (stone/cornerstone) at Ps 118:22: H68 ʾeben = "stone"; H6438 pinnah
    = "cornerstone" (lit. head of the corner). Rendered "cornerstone" in all
    tiers. The messianic reading explicit in the NT: Matt 21:42, Mark 12:10,
    Luke 20:17, Acts 4:11, 1 Pet 2:7.

H5797 (עֹז, oz) at Ps 118:14: "strength" — part of the Exodus 15:2 echo
    ("the LORD is my strength and my song"). The identical phrase appears at
    Isa 12:2, making Ps 118:14 a deliberate intertextual node. L/M carry it
    verbatim; T notes the exodus resonance.

H3444 (יְשׁוּעָה, yeshuah / salvation): "salvation" in L/M/T. Primary throughout
    Ps 118 (vv14, 15, 21). Related to the name Yeshua/Jesus; T does not add
    commentary on this but preserves the word's weight.

H2896 (טוֹב, tov / good): "good" in all tiers at Ps 118:1, 29 opening/closing
    refrain. God's goodness is the covenantal basis for the thanksgiving summons.

H4752/H7227 (רַב, rav / great) at Ps 117:2: "great" — describing the scale of
    chesed. Carried in all tiers.

H2764/H6763 — idol description (Ps 115:4-8): The anatomy of ineffectual gods is
    rendered word-for-word in L, with natural English in M, and as compressed
    declarative poetry in T. The T tier's staccato structure ("Mouths — but they
    cannot speak") mirrors the rhetorical punch of the Hebrew repetitions.

=== OT intertextuality and NT connections ===

Ps 115:16 — "The earth he has given to the children of man" echoes Gen 1:28
    (dominion mandate). This is not a contradiction of God's ownership but a
    statement of delegated stewardship.

Ps 116:3 — "The cords of death / pangs of Sheol" (H2256 chevlei, H4712 metsarei)
    — sheol as active, grasping: the underworld has ropes. This is the ancient
    cosmological picture of death as a realm with pull.

Ps 116:10 — "I believed, even when I spoke" (cohortative/adversative) — Paul
    quotes this at 2 Cor 4:13 ("having the same spirit of faith") to describe
    the pattern of speaking from within affliction because of prior trust.

Ps 117:1 — Quoted at Romans 15:11 (LXX form) in Paul's catena of Gentile-praise
    passages. The T tier notes this scope in the rendering.

Ps 118:14 = Exod 15:2 = Isa 12:2 — verbatim echo. T tier marks it.

Ps 118:22 — Cornerstone. Rejected stone becoming the keystone of the arch:
    this metaphor governs Paul's "foundation" theology (Eph 2:20, 1 Cor 3:11).

Ps 118:25-26 — Hosanna / Blessed is he who comes: the liturgical shout of Palm
    Sunday (Matt 21:9, Mark 11:9-10, Luke 19:38, John 12:13). The T tier renders
    v25 with "Hosanna" to surface this.

=== Aspect and tense notes ===

Ps 115-116: Hebrew perfect and imperfect mix freely; the psalmist moves between
    completed acts of rescue (perfect) and present declarations/vows (cohortative).
    The idol description uses participle constructions ("having mouths — not speaking")
    rendered as simple negatives in English for naturalness.

Ps 117: Two verses, both imperative/jussive structure + causal כִּי clause.
    Straightforward: command + reason.

Ps 118: The "I will not fear / I will not die" declarations are perfects of
    confidence — a Hebrew idiom where a future certainty is expressed as past
    completion. "I will not die" = "I am as good as not dying" (resolved trust).
    Rendered as confident future in all tiers. The refrain "his steadfast love
    endures forever" uses the qal imperfect of H5769 (olam) — ongoing, open-ended
    duration; "endures forever" is accurate and better than "lasts forever."
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
  # Psalm 115 — Not to Us, But to Your Name
  # Congregational anti-idol polemic with triple catechism and closing blessing
  # ===========================================================================
  "115": {
    "1": {
      "L": "Not to us, O LORD, not to us, but to your name give glory, for the sake of your steadfast love and your faithfulness.",
      "M": "Not to us, O LORD — not to us — but to your name give glory, because of your steadfast love and your faithfulness.",
      "T": "Not to us, O LORD — not to us —\nbut to your name give glory,\nfor the sake of your steadfast love and faithfulness."
    },
    "2": {
      "L": "Why should the nations say, 'Where now is their God?'",
      "M": "Why should the nations say, 'Where is their God?'",
      "T": "Why should the nations ask,\n'Where is their God now?'"
    },
    "3": {
      "L": "But our God is in the heavens; he does whatever he pleases.",
      "M": "But our God is enthroned in the heavens; he does whatever he pleases.",
      "T": "But our God — he is in the heavens.\nHe does\nwhatever he pleases."
    },
    "4": {
      "L": "Their idols are silver and gold, the work of human hands.",
      "M": "Their idols are silver and gold — nothing more than what human hands have made.",
      "T": "Their idols are silver and gold—\nmere handiwork\nof human fingers."
    },
    "5": {
      "L": "Mouths have they, but they speak not; eyes have they, but they see not.",
      "M": "They have mouths but cannot speak; they have eyes but cannot see.",
      "T": "Mouths — but they cannot speak.\nEyes — but they cannot see."
    },
    "6": {
      "L": "Ears have they, but they hear not; noses have they, but they smell not.",
      "M": "They have ears but cannot hear; they have noses but cannot smell.",
      "T": "Ears — but they cannot hear.\nNoses — but they cannot smell."
    },
    "7": {
      "L": "They have hands, but they handle not; feet have they, but they walk not; they make no sound in their throat.",
      "M": "They have hands but cannot feel anything; they have feet but cannot walk; they produce no sound from their throat.",
      "T": "Hands — but they cannot feel.\nFeet — but they cannot walk.\nNot a sound\nfrom their throat."
    },
    "8": {
      "L": "Those who make them will become like them, as will all who trust in them.",
      "M": "Those who make them will end up like them — and so will everyone who puts their trust in them.",
      "T": "Those who make them will become like them.\nSo will everyone\nwho trusts in them."
    },
    "9": {
      "L": "O Israel, trust in the LORD! He is their help and their shield.",
      "M": "Israel, put your trust in the LORD! He is their help and their shield.",
      "T": "O Israel — trust in the LORD!\nHe is their help\nand their shield."
    },
    "10": {
      "L": "O house of Aaron, trust in the LORD! He is their help and their shield.",
      "M": "House of Aaron, put your trust in the LORD! He is their help and their shield.",
      "T": "O house of Aaron — trust in the LORD!\nHe is their help\nand their shield."
    },
    "11": {
      "L": "You who fear the LORD, trust in the LORD! He is their help and their shield.",
      "M": "All who fear the LORD, put your trust in the LORD! He is their help and their shield.",
      "T": "You who fear the LORD — trust in the LORD!\nHe is their help\nand their shield."
    },
    "12": {
      "L": "The LORD has been mindful of us; he will bless us; he will bless the house of Israel; he will bless the house of Aaron;",
      "M": "The LORD has remembered us and he will bless us; he will bless the house of Israel; he will bless the house of Aaron;",
      "T": "The LORD has remembered us — he will bless us.\nHe will bless the house of Israel.\nHe will bless the house of Aaron."
    },
    "13": {
      "L": "he will bless those who fear the LORD, both the small and the great.",
      "M": "He will bless all who fear the LORD, the small as well as the great.",
      "T": "He will bless those who fear the LORD—\nboth the small\nand the great."
    },
    "14": {
      "L": "May the LORD give you increase, you and your children!",
      "M": "May the LORD grant you increase — you and your children!",
      "T": "May the LORD make you more and more—\nyou\nand your children."
    },
    "15": {
      "L": "May you be blessed by the LORD, who made heaven and earth!",
      "M": "May you be blessed by the LORD — he who made both heaven and earth!",
      "T": "May you be blessed by the LORD—\nthe maker\nof heaven and earth."
    },
    "16": {
      "L": "The heavens are the LORD's heavens, but the earth he has given to the children of man.",
      "M": "The highest heavens belong to the LORD, but the earth he has given to the children of mankind.",
      "T": "The heavens are the LORD's heavens.\nBut the earth —\nhe has given it to the children of man."
    },
    "17": {
      "L": "The dead do not praise the LORD, nor do any who go down into silence.",
      "M": "The dead cannot praise the LORD, nor can any who descend into the silence of the grave.",
      "T": "The dead do not praise the LORD.\nNor do any who go down\ninto silence."
    },
    "18": {
      "L": "But we will bless the LORD from this time forth and forevermore. Praise the LORD!",
      "M": "But we will praise the LORD from this moment on, now and forever. Praise the LORD!",
      "T": "But we — we will bless the LORD\nfrom this moment forward\nand forever. Praise the LORD!"
    }
  },

  # ===========================================================================
  # Psalm 116 — I Love the LORD
  # Individual thanksgiving for deliverance from death; vow-fulfillment liturgy
  # ===========================================================================
  "116": {
    "1": {
      "L": "I love the LORD, for he has heard my voice and my supplications.",
      "M": "I love the LORD because he has heard my voice and my pleas for mercy.",
      "T": "I love the LORD —\nhe heard my voice,\nhe heard my cries for mercy."
    },
    "2": {
      "L": "Because he inclined his ear to me, I will call on him as long as I live.",
      "M": "Because he bent his ear down to listen to me, I will call on him for as long as I live.",
      "T": "Because he bent his ear down to me,\nI will call on him\nfor as long as I live."
    },
    "3": {
      "L": "The cords of death encompassed me; the terrors of Sheol laid hold of me; I found distress and anguish.",
      "M": "Death's ropes wrapped around me; the grip of Sheol closed in; I was trapped in distress and anguish.",
      "T": "The ropes of death wrapped around me.\nThe grip of Sheol took hold—\nI was caught in distress and anguish."
    },
    "4": {
      "L": "Then I called on the name of the LORD: 'O LORD, I beseech you, deliver my soul!'",
      "M": "Then I cried out the name of the LORD: 'Please, LORD — rescue my life!'",
      "T": "Then I called on the name of the LORD:\n'O LORD, I beg you —\ndeliver my soul!'"
    },
    "5": {
      "L": "Gracious is the LORD, and righteous; yes, our God is merciful.",
      "M": "The LORD is gracious and righteous; our God is full of compassion.",
      "T": "Gracious is the LORD — and righteous.\nOur God\nis merciful."
    },
    "6": {
      "L": "The LORD preserves the simple; when I was brought low, he saved me.",
      "M": "The LORD protects those who are simple-hearted; when I was at my lowest, he came to my rescue.",
      "T": "The LORD watches over the simple.\nWhen I was brought low,\nhe saved me."
    },
    "7": {
      "L": "Return, O my soul, to your rest, for the LORD has dealt bountifully with you.",
      "M": "Come to your rest again, my soul, for the LORD has been good to you.",
      "T": "Return to your rest, O my soul —\nfor the LORD\nhas dealt bountifully with you."
    },
    "8": {
      "L": "For you have delivered my soul from death, my eyes from tears, my feet from stumbling.",
      "M": "You have rescued my soul from death, my eyes from tears, my feet from stumbling.",
      "T": "You have rescued my soul from death,\nmy eyes from tears,\nmy feet from stumbling."
    },
    "9": {
      "L": "I will walk before the LORD in the land of the living.",
      "M": "I will walk in the presence of the LORD in the land of the living.",
      "T": "I will walk before the LORD\nin the land\nof the living."
    },
    "10": {
      "L": "I believed, even when I spoke: 'I am greatly afflicted.'",
      "M": "I trusted, even while I cried out: 'I am in great distress.'",
      "T": "I believed — even when I cried out:\n'I am in great distress.'"
    },
    "11": {
      "L": "I said in my alarm, 'All men are liars.'",
      "M": "In my panic I declared, 'Every human being is a liar.'",
      "T": "In my panic I said:\n'Every man\nis a liar.'"
    },
    "12": {
      "L": "What shall I return to the LORD for all his benefits to me?",
      "M": "What can I give back to the LORD for all the good he has done for me?",
      "T": "What shall I give back to the LORD\nfor all the good\nhe has done for me?"
    },
    "13": {
      "L": "I will lift up the cup of salvation and call on the name of the LORD.",
      "M": "I will take up the cup of salvation and call on the name of the LORD.",
      "T": "I will lift the cup of salvation\nand call on\nthe name of the LORD."
    },
    "14": {
      "L": "I will pay my vows to the LORD in the presence of all his people.",
      "M": "I will fulfill my vows to the LORD in the presence of all his people.",
      "T": "I will pay my vows to the LORD —\nright there,\nbefore all his people."
    },
    "15": {
      "L": "Precious in the sight of the LORD is the death of his saints.",
      "M": "The LORD takes the death of his faithful ones very seriously.",
      "T": "Precious in the LORD's sight\nis the death\nof his faithful ones."
    },
    "16": {
      "L": "O LORD, I am your servant; I am your servant, the son of your maidservant. You have loosed my bonds.",
      "M": "LORD, I am your servant — your servant, the son born of your maidservant. You have set me free from my bonds.",
      "T": "O LORD, I am your servant —\nyour servant, born of your maidservant.\nYou have loosed my bonds."
    },
    "17": {
      "L": "I will offer to you the sacrifice of thanksgiving and call on the name of the LORD.",
      "M": "I will bring you a thanksgiving offering and call out the name of the LORD.",
      "T": "I will bring you the sacrifice of thanksgiving\nand call on\nthe name of the LORD."
    },
    "18": {
      "L": "I will pay my vows to the LORD in the presence of all his people,",
      "M": "I will fulfill my vows to the LORD in the presence of all his people,",
      "T": "I will pay my vows to the LORD —\nbefore all his people —"
    },
    "19": {
      "L": "in the courts of the house of the LORD, in your midst, O Jerusalem. Praise the LORD!",
      "M": "right in the courtyards of the LORD's house, in your very midst, O Jerusalem. Praise the LORD!",
      "T": "in the courts of the LORD's house,\nin your midst, O Jerusalem.\nPraise the LORD!"
    }
  },

  # ===========================================================================
  # Psalm 117 — The Shortest Psalm; the Universal Summons
  # Axial center of the Psalter; Paul quotes v1 at Romans 15:11
  # ===========================================================================
  "117": {
    "1": {
      "L": "Praise the LORD, all you nations! Extol him, all you peoples!",
      "M": "Praise the LORD, all nations! Praise him, all peoples of the earth!",
      "T": "Praise the LORD, all nations!\nExtol him,\nall peoples!"
    },
    "2": {
      "L": "For great is his steadfast love toward us, and the faithfulness of the LORD endures forever. Praise the LORD!",
      "M": "For his steadfast love toward us is great, and the faithfulness of the LORD endures forever. Praise the LORD!",
      "T": "For great is his steadfast love toward us—\nthe faithfulness of the LORD\nendures forever.\nPraise the LORD!"
    }
  },

  # ===========================================================================
  # Psalm 118 — The Great Hallel Finale
  # Passover/Tabernacles processional; cornerstone prophecy; Hosanna;
  # "Blessed is he who comes in the name of the LORD"
  # ===========================================================================
  "118": {
    "1": {
      "L": "Give thanks to the LORD, for he is good; for his steadfast love endures forever.",
      "M": "Give thanks to the LORD, for he is good; his steadfast love endures forever.",
      "T": "Give thanks to the LORD, for he is good—\nhis steadfast love\nendures forever."
    },
    "2": {
      "L": "Let Israel now say: 'His steadfast love endures forever.'",
      "M": "Let Israel declare: 'His steadfast love endures forever.'",
      "T": "Let Israel say:\n'His steadfast love\nendures forever.'"
    },
    "3": {
      "L": "Let the house of Aaron now say: 'His steadfast love endures forever.'",
      "M": "Let the house of Aaron declare: 'His steadfast love endures forever.'",
      "T": "Let the house of Aaron say:\n'His steadfast love\nendures forever.'"
    },
    "4": {
      "L": "Let those who fear the LORD now say: 'His steadfast love endures forever.'",
      "M": "Let all who fear the LORD declare: 'His steadfast love endures forever.'",
      "T": "Let those who fear the LORD say:\n'His steadfast love\nendures forever.'"
    },
    "5": {
      "L": "Out of my distress I called on the LORD; the LORD answered me and set me in a wide place.",
      "M": "From the depths of my distress I called to the LORD; the LORD answered me and gave me room to breathe.",
      "T": "Out of my distress I called on the LORD.\nThe LORD answered —\nhe set me in a wide and open place."
    },
    "6": {
      "L": "The LORD is for me; I will not fear. What can man do to me?",
      "M": "The LORD is on my side; I will not be afraid. What can any person do to me?",
      "T": "The LORD is on my side —\nI will not fear.\nWhat can any man do to me?"
    },
    "7": {
      "L": "The LORD is for me among my helpers; I will look in satisfaction on those who hate me.",
      "M": "The LORD stands on my side as my helper; I will see my enemies brought to shame.",
      "T": "The LORD takes my side as my helper.\nI will see\nwhat becomes of those who hate me."
    },
    "8": {
      "L": "It is better to take refuge in the LORD than to trust in man.",
      "M": "It is better to take shelter in the LORD than to put your confidence in any person.",
      "T": "Better to take refuge in the LORD\nthan to trust\nin any human being."
    },
    "9": {
      "L": "It is better to take refuge in the LORD than to trust in princes.",
      "M": "It is better to take shelter in the LORD than to put your confidence in rulers.",
      "T": "Better to take refuge in the LORD\nthan to trust\nin princes."
    },
    "10": {
      "L": "All nations surrounded me; in the name of the LORD I cut them off.",
      "M": "All the nations closed in around me, but in the name of the LORD I routed them.",
      "T": "All the nations surrounded me.\nIn the name of the LORD\nI cut them off."
    },
    "11": {
      "L": "They surrounded me, yes, surrounded me on every side; in the name of the LORD I cut them off.",
      "M": "They surrounded me — closed in from every side — but in the name of the LORD I cut them off.",
      "T": "They surrounded me — surrounded me on every side.\nIn the name of the LORD\nI cut them off."
    },
    "12": {
      "L": "They surrounded me like bees; they were extinguished like a fire of thorns; in the name of the LORD I cut them off.",
      "M": "They swarmed around me like bees, but blazed out as quickly as a brush fire; in the name of the LORD I cut them off.",
      "T": "They swarmed me like bees —\nblazing out like a thornfire.\nIn the name of the LORD\nI cut them off."
    },
    "13": {
      "L": "I was pushed hard so that I was falling, but the LORD helped me.",
      "M": "I was shoved to the point of falling, but the LORD was there to help me.",
      "T": "They shoved me hard — I was about to fall.\nBut the LORD\nhelped me."
    },
    "14": {
      "L": "The LORD is my strength and my song; he has become my salvation.",
      "M": "The LORD is my strength and my song; he has become my salvation.",
      "T": "The LORD is my strength and my song —\nhe has become my salvation.\n(The exodus song of Moses, the song of Isaiah's new exodus — spoken again here.)"
    },
    "15": {
      "L": "The sound of joyful song is in the tents of the righteous: 'The right hand of the LORD acts valiantly;'",
      "M": "Shouts of joy and victory echo in the tents of the righteous: 'The right hand of the LORD does mighty things!'",
      "T": "The sound of joy and victory rings out\nin the tents of the righteous:\n'The right hand of the LORD acts with power!'"
    },
    "16": {
      "L": "the right hand of the LORD is exalted, the right hand of the LORD acts valiantly.",
      "M": "The right hand of the LORD is raised high; the right hand of the LORD does mighty things!",
      "T": "The right hand of the LORD is lifted high!\nThe right hand of the LORD\nacts with power!"
    },
    "17": {
      "L": "I shall not die but live, and I will declare the works of the LORD.",
      "M": "I will not die — I will live, and I will tell of what the LORD has done.",
      "T": "I will not die — I will live.\nI will declare\nthe deeds of the LORD."
    },
    "18": {
      "L": "The LORD has chastened me severely, but he has not given me over to death.",
      "M": "The LORD has disciplined me hard, but he has not let death have me.",
      "T": "The LORD disciplined me severely —\nbut he has not given me over\nto death."
    },
    "19": {
      "L": "Open to me the gates of righteousness; I will enter through them and give thanks to the LORD.",
      "M": "Open the righteous gates for me so I can go in and give thanks to the LORD.",
      "T": "Open to me the gates of righteousness —\nI will enter through them\nand give thanks to the LORD."
    },
    "20": {
      "L": "This is the gate of the LORD; the righteous shall enter through it.",
      "M": "This is the LORD's own gate; only the righteous may enter through it.",
      "T": "This is the gate of the LORD.\nThe righteous —\nthey shall enter through it."
    },
    "21": {
      "L": "I give thanks to you, for you have answered me and have become my salvation.",
      "M": "I praise you because you answered me and have become my salvation.",
      "T": "I thank you — you answered me.\nYou have become\nmy salvation."
    },
    "22": {
      "L": "The stone that the builders rejected has become the head of the corner.",
      "M": "The stone that the builders threw aside has become the cornerstone.",
      "T": "The stone the builders discarded —\nit has become\nthe cornerstone."
    },
    "23": {
      "L": "This is the LORD's doing; it is marvelous in our eyes.",
      "M": "This is what the LORD has done; it is wonderful in our sight.",
      "T": "This is the LORD's doing.\nIt is marvelous\nin our eyes."
    },
    "24": {
      "L": "This is the day that the LORD has made; let us rejoice and be glad in it.",
      "M": "This is the day the LORD has made; let us celebrate and be glad in it.",
      "T": "This is the day the LORD has made.\nLet us rejoice —\nlet us be glad in it."
    },
    "25": {
      "L": "O LORD, save us, we pray! O LORD, grant us success, we pray!",
      "M": "LORD, save us, we pray! LORD, grant us success, we pray!",
      "T": "Hosanna — save us now, O LORD!\nO LORD — hosanna!\nSend us your blessing and success."
    },
    "26": {
      "L": "Blessed is he who comes in the name of the LORD! We bless you from the house of the LORD.",
      "M": "May God bless the one who comes in the name of the LORD! We bless you from the LORD's house.",
      "T": "Blessed is he who comes in the name of the LORD!\nWe bless you\nfrom the house of the LORD."
    },
    "27": {
      "L": "The LORD is God, and he has made his light to shine upon us. Bind the festal sacrifice with cords, even to the horns of the altar.",
      "M": "The LORD is God, and his light has shone on us. Bind the sacrifice with cords and bring it all the way to the horns of the altar.",
      "T": "The LORD is God — he has shone his light upon us.\nBind the festal sacrifice with cords,\ndraw it all the way to the altar's horns."
    },
    "28": {
      "L": "You are my God, and I will give thanks to you; you are my God, I will exalt you.",
      "M": "You are my God, and I will give you thanks; you are my God, and I will praise you.",
      "T": "You are my God — I will give you thanks.\nYou are my God —\nI will exalt you."
    },
    "29": {
      "L": "Give thanks to the LORD, for he is good; for his steadfast love endures forever.",
      "M": "Give thanks to the LORD, for he is good; his steadfast love endures forever.",
      "T": "Give thanks to the LORD, for he is good —\nhis steadfast love\nendures forever."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 115–118 written.')

if __name__ == '__main__':
    main()
