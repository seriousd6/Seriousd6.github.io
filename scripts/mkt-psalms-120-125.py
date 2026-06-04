"""
MKT Psalms chapters 120–125 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-120-125.py

=== Overview of this unit ===

Psalms 120–125 open the Songs of Ascents (Psalms 120–134), a collection of pilgrimage
songs sung by worshipers travelling up to Jerusalem for the three great festivals
(Passover, Pentecost, Tabernacles). The Hebrew superscription שִׁיר הַמַּעֲלוֹת (shir
hama'alot) means "A Song of Ascents." All six psalms in this unit carry it.

Ps 120 (7 v) — The Lament from Exile. The collection opens unexpectedly in anguish:
    the psalmist is far from Jerusalem, surrounded by warmongers (Meshech in the north,
    Kedar in the south — two remote, warlike peoples, used as types for any hostile
    environment). The psalm is structured as a retrospective (v1: answered prayer) →
    present petition (v2) → taunt of the lying tongue (vv3-4) → lament of sojourning
    (vv5-7). The journey to Jerusalem begins in longing and pain. The arrows + broom-
    tree coals of v4 are the punishment awaiting the lying tongue: sharp and sustained
    (broom-tree coals burn far longer than ordinary wood).

Ps 121 (8 v) — The Guardian of Israel. The great travel psalm. The hills are most
    likely threatening (bandits; the uncertain road) rather than comforting — the point
    is that help comes not from them but from the LORD alone. The Hebrew verb shamar
    (H8104, "keep/guard") appears six times in eight verses, making it the structural
    spine. The T tier brings the six-fold repetition into relief. The psalm moves from
    the singular "I" (vv1-2) to the second-person singular "you" (vv3-8) — possibly
    a liturgical response, a priest declaring blessing over the pilgrim about to depart.

Ps 122 (9 v) — Jerusalem the City of Peace. An arrival psalm. The movement from
    "let us go" (v1, past speech recalled) to "our feet are standing" (v2) enacts the
    completed pilgrimage. The name Yerushalayim embeds shalom (peace) — the T tier
    makes this wordplay explicit. The thrones of David (v5) point to Jerusalem's double
    role: house of worship and seat of covenant justice. The threefold peace-prayer
    (vv6-8) escalates: peace for Jerusalem → for brothers → for the house of the LORD.

Ps 123 (4 v) — Eyes to the LORD. Brief communal supplication. The servant/mistress
    metaphor is the sharpest image in the unit: the servant watches the master's hand
    for any signal — a word, a gesture, an indication of will or provision. This is the
    posture of prayer — not urgent demand but attentive dependence. The word buz (H937,
    "contempt/scorn") frames vv3-4 in honor-shame vocabulary; the sha'anan ("at ease,"
    H7600) oppressors are the complacent privileged who mock the humble pilgrim.

Ps 124 (8 v) — Israel's Escape. Counterfactual thanksgiving: "if not for the LORD..."
    Three near-disaster images build in intensity: being swallowed alive (v3, animal
    predator image), drowning in a raging flood (vv4-5, chaos-water image), being
    caught in a fowler's trap (v7, hunter-prey image). Each image is more complete
    than the last. The escape of the bird from the snare ends in a broken trap — not
    a narrow escape but a decisive, providential rescue. The doxology (v8) returns to
    the name-theology of Ps 121:2: the same Creator who made heaven and earth is the
    one who rescues.

Ps 125 (5 v) — The Stability of the Righteous. Trust psalm organized as comparison
    (vv1-2: as Zion / as the mountains → so the LORD's people / so the LORD) →
    protective promise (v3: the rod of the wicked will not rest) → petition (v4) →
    warning + benediction (v5). The scepter-on-the-lot imagery in v3 is about
    territorial allocation: the wicked are not permitted to exercise ongoing dominion
    over the land portion of the righteous, lest the righteous resort to wickedness
    themselves. The closing "peace be upon Israel" echoes the Aaronic blessing and
    recurs at Gal 6:16 in the NT.

=== Contested-term decisions ===

H4609 (מַּעֲלוֹת, ma'alot): "Ascents" in all tiers. This is the first unit in the
    Psalter that carries this superscription. "Ascents" (L/M/T) is preferred over
    the KJV "Degrees" because it names the actual function: pilgrimage going up to
    Jerusalem. Consistent use established for Psalms 120–134.

H3068 (יהוה, YHWH): "LORD" in L/M/T throughout. Consistent with all prior Psalms
    scripts.

H5315 (נֶפֶשׁ, nefesh): "soul" in L/M/T. The embodied self, not the Greek immaterial
    soul. At Ps 124:4-5 "our soul" = our whole living selves. At Ps 121:7 "your soul"
    = your life.

H7965 (שָׁלוֹם, shalom): "peace" in L/M; "peace" in T with the wordplay noted in
    Ps 122 brought to the surface (Jerusalem = "city of peace" / "foundation of
    peace"). The T tier at 122:6-8 makes the shalom/Yerushalayim connection explicit.

H8104 (שָׁמַר, shamar): "keep/guard/watch over" in L; "keep/protect/watch over" in
    M; "guard" preferred in T. The six-fold repetition in Ps 121 is a structural
    feature; all tiers preserve the repeated root.

H2617 (חֶסֶד, chesed): does not appear in this unit. Not a decision required here.

H430 (אֱלֹהִים, Elohim): "God" in all tiers — standard.

H7562 (רֶשַׁע, resha, wickedness) at Ps 125:3: "wickedness" in L; "wicked" (as
    adjective) in M and T. The rod/scepter of the wicked shall not rest on the
    territory of the righteous.

H205 (אָוֶן, aven, iniquity/wickedness) at Ps 125:5: "iniquity" in L; "evildoers"
    as compound in M/T for readability ("workers of iniquity" / "those who do evil").

H937 (בּוּז, buz, contempt/scorn): "contempt" in all tiers at Ps 123:3-4. The
    honor-shame dynamic is primary; "contempt" carries the social weight better
    than "scorn."

H190 (אוֹי, oy, woe/alas): "Woe to me" in L/M at Ps 120:5; T renders it "Alas —"
    with a dash for the emotional weight of the exclamation.

H1481 (גּוּר, gur, sojourn): "sojourn" in L; "live as a foreigner" in M; "dwell
    as a stranger" in T. Captures the alien/displaced status.

=== OT intertextuality and NT connections ===

Ps 121:2 — "who made heaven and earth" echoes the Priestly creation formula
    (Gen 1) and is the same phrase at Ps 124:8. The Creator-as-guardian connection
    is the theological anchor of both psalms.

Ps 122:1 — "I was glad when they said to me, 'Let us go to the house of the LORD'"
    is one of the most-cited Psalter pilgrimage verses. It became liturgical in
    synagogue and church contexts as a call to worship.

Ps 124:7 — The bird-from-the-snare image for the exodus/rescue pattern recurs in
    the NT at Luke 4:18 (release for captives) and implicitly in Paul's "freedom
    from bondage" language.

Ps 124:8 — "Our help is in the name of the LORD who made heaven and earth." This
    verse became a standard opening liturgy in Reformed worship services from Calvin
    onward (the "votum").

Ps 125:5 — "Peace be upon Israel" recurs nearly verbatim at Galatians 6:16, where
    Paul applies it to "the Israel of God" (the community of faith). The T tier
    notes this echo.

=== Aspect and tense notes ===

Ps 120: v1 uses Hebrew perfect (completed: "he answered me") — a retrospective.
    vv5-7 use imperfect/participle constructions; rendered as present-state lamenting.

Ps 121: The verb forms shift between declarative future ("he will not let," "he will
    keep") and participial ("the one who keeps"). Rendered as confident declarative
    future in all tiers — this is a psalm of assurance, not petition. The "will not
    slumber/sleep" parallelism in v4 is emphatic negation (לֹא יָנוּם) — "not ever."

Ps 122: v1 "I was glad" = Hebrew perfect (completed joy). v2 "Our feet shall stand"
    = imperfect of resolve/intention. The MT has "are standing" (participle) in
    some readings — rendered as present tense in L/M.

Ps 123: v2 is one long sentence in Hebrew with four parallel "as...so" clauses.
    The final clause is a temporal hinge: "until he has mercy" — the eyes stay fixed
    indefinitely. Maintained in all tiers.

Ps 124: vv1-5 use the conditional particle לוּלֵי (lulei, "if not / were it not
    that"). Rendered "if it had not been" in all tiers. The "then" (אָז, az) at
    vv3, 4, 5 marks the consequence. The perfect of result in vv6-7 is triumphant:
    "he has not given us... our soul has escaped." Rendered as completed action.

Ps 125: v3 uses imperfect + lest-clause structure: the rod "shall not rest" in
    order that the righteous "not put forth their hands" to do evil. The protective
    promise is consequentialist (God removes the temptation). v5 is a
    declarative + jussive pair: "the LORD will lead them away... peace be upon Israel."
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
  # Psalm 120 — Deliver Me from Lying Lips
  # Opening lament of the Ascents; sojourning among warmongers far from Jerusalem
  # ===========================================================================
  "120": {
    "1": {
      "L": "A Song of Ascents. In my distress I cried to the LORD, and he answered me.",
      "M": "A Song of Ascents. In my distress I called out to the LORD, and he answered me.",
      "T": "A Song of Ascents.\nIn my distress I cried to the LORD —\nand he answered me."
    },
    "2": {
      "L": "O LORD, deliver my soul from lying lips, from a deceitful tongue.",
      "M": "LORD, rescue me from lying lips and from a deceitful tongue.",
      "T": "O LORD, deliver my soul\nfrom lying lips,\nfrom a tongue that deceives."
    },
    "3": {
      "L": "What shall be given to you, and what shall be added to you, O deceitful tongue?",
      "M": "What will come to you, and what more will be done to you, O deceitful tongue?",
      "T": "What will be given to you?\nWhat will be added on top of that,\nO tongue of deceit?"
    },
    "4": {
      "L": "Sharp arrows of a warrior, with glowing coals of the broom tree!",
      "M": "A warrior's sharp arrows, fired with glowing coals of broom wood!",
      "T": "Sharp arrows of the warrior —\ncoals of the broom tree,\nburning long and fierce."
    },
    "5": {
      "L": "Woe to me, that I sojourn in Meshech, that I dwell among the tents of Kedar!",
      "M": "Woe to me, that I must live as a foreigner in Meshech and make my dwelling among the tents of Kedar!",
      "T": "Alas — that I must sojourn in Meshech,\nthat I must dwell\namong the tents of Kedar!"
    },
    "6": {
      "L": "Too long has my soul had its dwelling among those who hate peace.",
      "M": "My soul has lived too long among those who hate peace.",
      "T": "Far too long has my soul dwelt\namong people\nwho hate peace."
    },
    "7": {
      "L": "I am for peace, but when I speak, they are for war.",
      "M": "I am for peace — but the moment I open my mouth, they want war.",
      "T": "I am for peace.\nBut when I speak —\nthey are for war."
    }
  },

  # ===========================================================================
  # Psalm 121 — The Guardian of Israel
  # Pilgrim travel psalm; six-fold shamar; Creator as keeper
  # ===========================================================================
  "121": {
    "1": {
      "L": "A Song of Ascents. I lift up my eyes to the hills. From where does my help come?",
      "M": "A Song of Ascents. I lift my eyes toward the hills — but where does my help come from?",
      "T": "A Song of Ascents.\nI lift my eyes to the hills —\nfrom where does my help come?"
    },
    "2": {
      "L": "My help comes from the LORD, who made heaven and earth.",
      "M": "My help comes from the LORD, the maker of heaven and earth.",
      "T": "My help comes from the LORD —\nthe one who made\nheaven and earth."
    },
    "3": {
      "L": "He will not let your foot stumble; he who keeps you will not slumber.",
      "M": "He will not let your foot slip; your keeper will not slumber.",
      "T": "He will not let your foot slip.\nYour keeper —\nhe will not slumber."
    },
    "4": {
      "L": "Behold, he who keeps Israel will neither slumber nor sleep.",
      "M": "See — he who guards Israel will neither slumber nor sleep.",
      "T": "Look:\nhe who keeps Israel\nwill not slumber — will not sleep."
    },
    "5": {
      "L": "The LORD is your keeper; the LORD is your shade on your right hand.",
      "M": "The LORD is your keeper; the LORD is your shade at your right hand.",
      "T": "The LORD is your keeper —\nthe LORD is your shade\nat your right hand."
    },
    "6": {
      "L": "The sun shall not strike you by day, nor the moon by night.",
      "M": "The sun will not harm you by day, nor the moon by night.",
      "T": "The sun will not strike you by day,\nnor the moon\nby night."
    },
    "7": {
      "L": "The LORD will keep you from all evil; he will keep your soul.",
      "M": "The LORD will protect you from every kind of evil; he will guard your very life.",
      "T": "The LORD will keep you from all evil —\nhe will keep\nyour soul."
    },
    "8": {
      "L": "The LORD will keep your going out and your coming in from this time forth and forevermore.",
      "M": "The LORD will watch over your coming and going, now and forever.",
      "T": "The LORD will keep your going out\nand your coming in —\nfrom now and forever."
    }
  },

  # ===========================================================================
  # Psalm 122 — Jerusalem the City of Peace
  # Arrival psalm; tribal gathering; shalom wordplay; threefold peace-prayer
  # ===========================================================================
  "122": {
    "1": {
      "L": "A Song of Ascents. Of David. I was glad when they said to me, 'Let us go to the house of the LORD!'",
      "M": "A Song of Ascents. Of David. I was filled with joy when they said to me, 'Let us go to the house of the LORD!'",
      "T": "A Song of Ascents. Of David.\nI was glad when they said to me:\n'Let us go to the house of the LORD!'"
    },
    "2": {
      "L": "Our feet are standing within your gates, O Jerusalem!",
      "M": "Our feet are standing inside your gates, O Jerusalem!",
      "T": "Our feet are standing\nwithin your gates,\nO Jerusalem!"
    },
    "3": {
      "L": "Jerusalem — built as a city that is bound firmly together,",
      "M": "Jerusalem — built as a city that is closely joined together,",
      "T": "Jerusalem —\nbuilt as a city\nknit together in unity,"
    },
    "4": {
      "L": "to which the tribes go up, the tribes of the LORD, as was decreed for Israel, to give thanks to the name of the LORD.",
      "M": "to which the tribes make their pilgrimage — the tribes of the LORD — as it was commanded of Israel, to give thanks to the name of the LORD.",
      "T": "where the tribes go up —\nthe tribes of the LORD —\nby decree of Israel, to give thanks to the LORD's name."
    },
    "5": {
      "L": "There thrones of judgment were set, the thrones of the house of David.",
      "M": "There the thrones of judgment stand — the thrones belonging to the house of David.",
      "T": "There thrones for judgment are set:\nthe thrones\nof the house of David."
    },
    "6": {
      "L": "Pray for the peace of Jerusalem! May those who love you prosper.",
      "M": "Pray for the peace of Jerusalem! May all who love this city flourish.",
      "T": "Pray for the peace of Jerusalem —\nthe city whose very name means peace.\nMay those who love you flourish."
    },
    "7": {
      "L": "May peace be within your walls, and security within your towers.",
      "M": "May there be peace within your walls and safety within your strongholds.",
      "T": "Peace within your walls —\nsecurity\nwithin your towers."
    },
    "8": {
      "L": "For the sake of my brothers and companions I will say, 'Peace be within you!'",
      "M": "For the sake of my brothers and friends I say, 'May peace be with you!'",
      "T": "For my brothers' sake,\nfor my companions' sake,\nI say: 'Peace be within you!'"
    },
    "9": {
      "L": "For the sake of the house of the LORD our God I will seek your good.",
      "M": "For the sake of the house of the LORD our God I will work for your wellbeing.",
      "T": "For the sake of the house of the LORD our God —\nI will seek\nyour good."
    }
  },

  # ===========================================================================
  # Psalm 123 — Eyes to the LORD
  # Communal supplication; master/servant posture; honor-shame context
  # ===========================================================================
  "123": {
    "1": {
      "L": "A Song of Ascents. To you I lift up my eyes, O you who are enthroned in the heavens!",
      "M": "A Song of Ascents. To you I lift my eyes, O you who sit enthroned in the heavens!",
      "T": "A Song of Ascents.\nTo you I lift my eyes —\nO you who are enthroned in the heavens!"
    },
    "2": {
      "L": "Behold, as the eyes of servants look to the hand of their master, as the eyes of a maidservant to the hand of her mistress, so our eyes look to the LORD our God, until he has mercy on us.",
      "M": "As the eyes of a servant watch the hand of his master, as a maidservant's eyes follow the hand of her mistress, so our eyes are fixed on the LORD our God until he has mercy on us.",
      "T": "As a servant's eyes watch the hand of his master —\nas a maidservant's eyes watch the hand of her mistress —\nso our eyes are fixed on the LORD our God,\nuntil he has mercy on us."
    },
    "3": {
      "L": "Have mercy on us, O LORD, have mercy on us, for we have had more than enough of contempt.",
      "M": "Have mercy on us, O LORD, have mercy on us — for we have endured far more than our fill of contempt.",
      "T": "Have mercy on us, O LORD —\nhave mercy on us!\nWe have had more than enough of contempt."
    },
    "4": {
      "L": "Our soul has had more than enough of the scoffing of those who are at ease, of the contempt of the proud.",
      "M": "We have had more than our fill of the mockery of the comfortable and the contempt of the arrogant.",
      "T": "Our soul is more than full\nof the scoffing of the comfortable,\nthe contempt of the proud."
    }
  },

  # ===========================================================================
  # Psalm 124 — If Not for the LORD
  # National thanksgiving; counterfactual structure; three rescue images; Creator doxology
  # ===========================================================================
  "124": {
    "1": {
      "L": "A Song of Ascents. Of David. If it had not been the LORD who was on our side — let Israel now say —",
      "M": "A Song of Ascents. Of David. If the LORD had not been on our side — let Israel say it now —",
      "T": "A Song of Ascents. Of David.\nIf the LORD had not been on our side —\nlet Israel say it —"
    },
    "2": {
      "L": "if it had not been the LORD who was on our side when people rose up against us,",
      "M": "if the LORD had not been on our side when our enemies rose up against us,",
      "T": "if the LORD had not been on our side\nwhen people rose up\nagainst us —"
    },
    "3": {
      "L": "then they would have swallowed us up alive, when their anger was kindled against us;",
      "M": "they would have swallowed us whole when their fury blazed against us.",
      "T": "then they would have swallowed us alive\nwhen their anger\nburned against us."
    },
    "4": {
      "L": "then the flood would have swept us away, the torrent would have gone over our soul;",
      "M": "The rushing waters would have swept us away; the current would have poured over us.",
      "T": "The floodwaters would have swept us away —\nthe torrent\ngone over our soul."
    },
    "5": {
      "L": "then the raging waters would have gone over our soul.",
      "M": "The raging waves would have overwhelmed us completely.",
      "T": "The raging waters —\nthey would have gone\nover our soul."
    },
    "6": {
      "L": "Blessed be the LORD, who has not given us as prey to their teeth!",
      "M": "Praise be to the LORD — he did not hand us over as prey to their teeth!",
      "T": "Blessed be the LORD —\nhe did not give us\nas prey to their teeth!"
    },
    "7": {
      "L": "We have escaped like a bird from the snare of the fowlers; the snare is broken, and we have escaped!",
      "M": "We have gotten away like a bird that slips out of the hunter's trap — the snare is broken, and we are free!",
      "T": "We have escaped like a bird\nout of the fowler's snare —\nthe snare is broken, and we are free!"
    },
    "8": {
      "L": "Our help is in the name of the LORD, who made heaven and earth.",
      "M": "Our help comes from the name of the LORD, the maker of heaven and earth.",
      "T": "Our help is in the name of the LORD —\nthe one who made\nheaven and earth."
    }
  },

  # ===========================================================================
  # Psalm 125 — The Stability of the Righteous
  # Trust psalm; Zion/mountains comparison; scepter of the wicked; peace upon Israel
  # ===========================================================================
  "125": {
    "1": {
      "L": "A Song of Ascents. Those who trust in the LORD are like Mount Zion, which cannot be moved but abides forever.",
      "M": "A Song of Ascents. Those who trust in the LORD are as firm as Mount Zion — unmovable, enduring forever.",
      "T": "A Song of Ascents.\nThose who trust in the LORD\nare like Mount Zion — immovable, abiding forever."
    },
    "2": {
      "L": "As the mountains are round about Jerusalem, so the LORD is round about his people, from this time forth and forevermore.",
      "M": "Just as the mountains encircle Jerusalem, so the LORD encircles his people, now and forever.",
      "T": "As the mountains surround Jerusalem —\nso the LORD surrounds his people,\nfrom now and forever."
    },
    "3": {
      "L": "For the scepter of wickedness shall not rest on the land allotted to the righteous, lest the righteous stretch out their hands to do wrong.",
      "M": "The scepter of the wicked will not be allowed to remain over the territory given to the righteous, lest the righteous be tempted to do evil themselves.",
      "T": "The scepter of the wicked will not rest\non the land of the righteous —\nlest the righteous reach out their hands to do wrong."
    },
    "4": {
      "L": "Do good, O LORD, to those who are good, and to those who are upright in their hearts.",
      "M": "Bless those who are good, O LORD, and all who are upright in heart.",
      "T": "Do good, O LORD,\nto those who are good —\nto those who are upright in heart."
    },
    "5": {
      "L": "But those who turn aside to their crooked ways the LORD will lead away with the workers of iniquity. Peace be upon Israel!",
      "M": "But as for those who swerve onto crooked paths, the LORD will banish them along with those who do evil. Peace be upon Israel!",
      "T": "But those who turn aside to crooked ways —\nthe LORD will lead them away with the evildoers.\nPeace be upon Israel!"
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 120–125 written.')

if __name__ == '__main__':
    main()
