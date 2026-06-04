"""
MKT Psalms chapters 103–104 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-103-104.py

=== Overview of this unit ===

Ps 103 (22 v) — A Psalm of David. The great hymn of God's character: forgiveness,
    healing, redemption, steadfast love, and compassion. The psalm moves through four
    movements:

    vv1-5:   CALL TO BLESS — the psalmist summons himself (his nefesh, his whole
        animated self) to bless the LORD and forget none of his benefits. The benefits
        are listed as five participial clauses: who forgives, who heals, who redeems,
        who crowns, who satisfies. The eagle renewal (v5) echoes Isaiah 40:31.

    vv6-12:  GOD'S CHARACTER — grounded in the Exodus self-revelation of YHWH at Sinai
        (Exod 34:6). The famous formula appears at v8: "merciful and gracious, slow to
        anger, abounding in steadfast love." The spatial metaphors of vv11-12 stretch
        the imagination to its limit: as high as the heavens; as far as east from west.

    vv13-18: HUMAN TRANSIENCE AND ETERNAL CHESED — the father-child simile (v13) anchors
        God's chesed in the most tender domestic relationship the ancient world knew.
        The grass/flower image (vv15-16) — which Jesus cites in Matt 6:28-30 — captures
        the brevity and beauty of human life simultaneously. Against that background
        (v17) the "but" lands with full weight: God's steadfast love is from everlasting
        to everlasting on those who fear him.

    vv19-22: COSMIC DOXOLOGY — the throne established in the heavens, the angelic hosts
        called to bless, all creation summoned to bless, and finally the psalmist's own
        soul called again: "Bless the LORD, O my soul!" The psalm ends where it began.

    KEY TERM: chesed (H2617) appears at vv4, 8, 11, 17 — the structural spine of the
    psalm. The entire meditation on God's character is a meditation on chesed.

    This psalm is quoted/alluded to more in the NT than almost any other: v8 (Jas 5:11);
    v12 (forgiveness); v13 (Matt 7:11 — Father giving good gifts); the grass/flower
    (1 Pet 1:24, citing Isa 40:6-8 which itself quotes Ps 103:15-16).

Ps 104 (35 v) — Anonymous creation hymn (possibly Davidic). Opens and closes with
    "Bless the LORD, O my soul" (mirroring Ps 103 exactly — the two psalms form a
    deliberate diptych). The psalm moves through the creation days of Genesis 1 as a
    hymn of ongoing sustenance rather than a narrative of origins:

    vv1-4:   GOD CLOTHED IN CREATION — light as a garment, heavens as a tent, clouds
        as chariot, winds as messengers. The cosmology is royal: God inhabits his
        creation as a king inhabits his palace.

    vv5-9:   TAMING THE WATERS — the primordial deep covers everything; at God's rebuke
        the waters flee and boundaries are set. This is creation-as-anti-chaos, not
        ex nihilo; the theological move is the same as Job 38 and Genesis 1.

    vv10-18: PROVISION FOR CREATURES — springs, birds, grass, cattle, food, wine, oil,
        bread; trees, birds, goats, conies. The catalogue is comprehensive and loving:
        every creature has its habitat; every need is met by the one who made them.

    vv19-23: THE RHYTHM OF LIGHT AND DARK — the moon governs the seasons; the sun
        knows when to set; the night belongs to the predators; the day to human work.
        The same Creator made both the hunter and the laborer.

    vv24-30: THE SEA AND THE SPIRIT — the vast sea teems with life; ships sail; even
        Leviathan (the chaos-monster of myth) frolics in it — domesticated, not
        defeated. All creatures depend entirely on God's open hand. When he withdraws
        his face they die; when he sends his Spirit (ruach, H7307) they are created.
        This is the theological climax: creation is not a past event but an ongoing
        act of divine sustaining.

    vv31-35: DOXOLOGY AND PRAISE — the glory of the LORD should endure; the LORD should
        rejoice in his works; the psalmist vows to sing forever. The final verse closes
        with the first "Hallelujah" in the Psalter (הַלְלוּ-יָהּ, Praise-Yah) — a word
        that will echo through the Psalter's closing doxologies (Pss 111–118, 146–150)
        and ultimately into Revelation 19.

    Leviathan (v26): Not hostile here — God "formed" (yatsar, H3335) Leviathan "to play
    in" the sea. The mythic chaos-monster has been tamed to a plaything of the Creator.
    This contrasts with Job 41 (where Leviathan is fearsome) and Ps 74:14 (where it is
    defeated). Ps 104 represents the most serene view: Leviathan is simply a creature
    in God's creation, made to frolic. Rendered "Leviathan" in all tiers.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M throughout both psalms.
    In T: "LORD" — consistent with all prior Psalms scripts. The divine personal name
    is the grammatical subject of virtually every verb in both psalms.

H5315 (נֶפֶשׁ, nefesh): Used as the reflexive self-address in the refrain ("O my soul"
    at Ps 103:1, 2, 22 and Ps 104:1, 35). Rendered "soul" in all three tiers — it
    functions here as "myself, my whole animated being," not the Greek immaterial soul.
    At Ps 104:29 the related idea appears without the word nefesh directly: "their
    breath" is H7307 (ruach).

H2617 (חֶסֶד, chesed): "steadfast love" in L/M throughout. In T: "steadfast love"
    (consistent with all prior Psalms scripts). Appears at Ps 103:4, 8, 11, 17.
    At v4 it is paired with rachamim (tender mercies / compassion); at v8 with the
    Sinai formula; at v11 it is measured against the height of heaven; at v17 it is
    "from everlasting to everlasting" — the counterpoint to human transience.

H7356 (רַחֲמִים, rachamim): "tender mercies" in L; "compassion" in M; "deep compassion"
    in T. The plural of racham (womb) — a word with visceral maternal resonance
    (cf. the related rachum, "merciful," at v8). At v13 the verb racham describes
    God's father-like tenderness.

H430 (אֱלֹהִים, Elohim): "God" / "my God" in all tiers. Consistent throughout.

H7307 (רוּחַ, ruach): Context-differentiated throughout:
    - Ps 103:16: "wind" (the wind that sweeps away the grass-flower)
    - Ps 104:3: "wind" ("wings of the wind" — God's cosmic chariot)
    - Ps 104:4: "winds" (God's messengers — the natural reading; Heb 1:7 quotes this
        as "angels/spirits" but the Psalm's context is natural phenomena)
    - Ps 104:29: "their breath" (the life-breath God gave; when taken back = death)
    - Ps 104:30: "your Spirit" (capitalized) — the creative divine breath sent forth
        that creates new life; echoes Gen 1:2 ("the Spirit of God hovering over the
        waters"). This is the theological center of the psalm: creation is an ongoing
        act of the Spirit.

H6666 (צְדָקָה, tsedaqah) / H6664 (צֶדֶק, tsedeq): "righteousness" in L/M/T.
    At Ps 103:6 it describes the LORD's saving acts for the oppressed (tsedaqah as
    saving-activity, not merely moral attribute). At 103:17 it extends to grandchildren.

H4941 (מִשְׁפָּט, mishpat): "justice" in L/M/T. Paired with tsedaqah at Ps 103:6 —
    "righteousness and justice" are the twin qualities of God's executive action for
    the downtrodden.

H3882 (לִוְיָתָן, Leviathan): Retained as "Leviathan" in all tiers. At Ps 104:26 the
    monster is domesticated: God formed it to play in the sea. Not defeated or hostile
    here — a creature like all others, subject to the Creator.

H1984 (הָלַל) + H3050 (יָהּ, Yah): "Praise the LORD!" in L/M; "Hallelujah!" in T at
    Ps 104:35. This is the first occurrence of הַלְלוּ-יָהּ in the Psalter — a word
    that will close the entire book. Rendered "Hallelujah" in T to preserve the
    Hebrew-derived term and its doxological weight.

H5769 (עוֹלָם, olam): "everlasting / forever" in all tiers. At Ps 103:17 the doubled
    idiom "from everlasting to everlasting" marks the eternal duration of chesed.

H1285 (בְּרִית, b'rit): "covenant" in all tiers at Ps 103:18. Consistent with all
    prior scripts.

H430 (אֵל, El) at Ps 104:21: "God" — the wild lions seek their food from God. The
    shorter divine title used here for God as provider of all creature-life.

=== Textual and interpretive notes ===

Ps 103:7 — "He made known his ways to Moses, his acts to the children of Israel."
    Moses knew God's ways (his character and method); Israel saw his acts (the events).
    This distinction — the insider's understanding of why God acts vs. the witness of
    what he does — is significant. Moses was the prophet who knew YHWH face to face.

Ps 103:8 — The Sinai self-revelation formula (Exod 34:6). The most quoted divine
    self-description in the OT; echoed in Neh 9:17, Joel 2:13, Jonah 4:2, Ps 86:15,
    145:8. Every occurrence is a conscious citation. The formula is foundational for
    understanding God's character in both Testaments.

Ps 103:12 — "As far as the east is from the west." In ancient cosmology, east-west is
    infinite distance (unlike north-south, which have poles). The image conveys complete,
    irreversible removal of transgression — not merely covered but gone.

Ps 103:13-14 — The father-pity simile followed by the dust reminder. The sequence is
    crucial: God's compassion is not naive; it is a knowing compassion. He knows we are
    dust (v14) — and pitied us anyway (v13). This is the gospel in miniature.

Ps 104:3 — "The beams of his upper chambers on the waters." The cosmological picture
    is of a heavenly palace built above the celestial ocean (the waters above the
    firmament of Gen 1:7). God's dwelling is a palace whose foundations rest on water.

Ps 104:26 — Leviathan "to play in it" (leshacheq — H7832): to frolic, sport, play.
    The most extraordinary image in a psalm full of extraordinary images. The monster
    of chaos is God's plaything in his sea — not a threat but a feature. This verse
    implicitly answers the anguish of Job: God is not bested by Leviathan; he made it.

Ps 104:29-30 — The ruach theology: when God hides his face → dismay; when he takes
    their ruach → death and dust; when he sends his ruach → creation and renewal.
    Ruach is the link between God and all living things. This is the psalm's theological
    core: the same Spirit that hovered over the waters in Gen 1:2 is still being sent
    forth, still creating, still renewing the face of the ground.

Ps 104:35 — Hallelujah: The word appears here for the first time in the Psalter
    (Ps 104:35b in MT). After a prayer that sinners vanish from the earth, the psalm
    ends in praise. The juxtaposition is deliberate: the world without the wicked would
    be a world fit for praise. The Psalter's editorial decision to close Ps 104 with
    this word and open Ps 105 with the same marks a new doxological phase in the
    collection.

=== Aspect and tense notes ===

Ps 103: The psalm's theological grammar uses Hebrew participles for God's ongoing
    activities (vv3-5: "who forgives," "who heals," "who redeems" — these are not
    one-time past acts but continuous present realities). The perfect tenses at vv6-7
    ("executed righteousness," "made known") denote completed historic action. The
    temporal contrasts at vv15-17 use the perfect for human transience (man "bloomed,"
    "was gone") and the imperfect for God's eternal chesed ("is / will be from
    everlasting to everlasting").

Ps 104: The psalm alternates between participial (God "who stretches," "who lays,"
    "who makes" — ongoing creative activity) and perfect (completed founding acts) and
    jussive (vv31-33, prayers/wishes: "may his glory endure," "I will sing"). The
    imperfects of the creature-watch sequence (vv20-23) convey routine, recurrent action:
    night comes, lions go out, sun rises, they return — the daily rhythm is God-ordained.
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
  # Psalm 103 — A Psalm of David: God's Character and Human Transience
  # ===========================================================================
  "103": {
    "1": {
      "L": "A Psalm of David. Bless the LORD, O my soul; and all that is within me, bless his holy name!",
      "M": "A Psalm of David. Bless the LORD, O my soul; let every part of me bless his holy name!",
      "T": "A Psalm of David.\nBless the LORD, O my soul—\nlet everything within me\nbless his holy name!"
    },
    "2": {
      "L": "Bless the LORD, O my soul, and do not forget all his benefits—",
      "M": "Bless the LORD, O my soul, and forget not a single good thing he has done—",
      "T": "Bless the LORD, O my soul—\nand never forget\na single thing he has done for you:"
    },
    "3": {
      "L": "who forgives all your iniquities, who heals all your diseases,",
      "M": "who forgives every one of your sins, who heals every one of your illnesses,",
      "T": "he who forgives every sin you have committed,\nwho heals every disease that afflicts you,"
    },
    "4": {
      "L": "who redeems your life from the pit, who crowns you with steadfast love and tender mercies,",
      "M": "who redeems your life from destruction, who crowns you with steadfast love and compassion,",
      "T": "who pulls your life back from the pit,\nwho crowns you — not with condemnation —\nbut with steadfast love and deep compassion,"
    },
    "5": {
      "L": "who satisfies you with good so that your youth is renewed like the eagle's.",
      "M": "who satisfies you with good things so that your strength is renewed like the eagle's.",
      "T": "who fills you with all that is good—\nso that your youth rises again,\nsoaring like an eagle."
    },
    "6": {
      "L": "The LORD executes righteousness and justice for all who are oppressed.",
      "M": "The LORD acts with righteousness and justice for all who are oppressed.",
      "T": "The LORD takes up the cause of the oppressed—\nhe acts with righteousness and justice\nfor everyone who has been wronged."
    },
    "7": {
      "L": "He made known his ways to Moses, his acts to the children of Israel.",
      "M": "He revealed his ways to Moses and his mighty deeds to the people of Israel.",
      "T": "He showed Moses how he works — his ways, his character.\nHe let Israel see what he does."
    },
    "8": {
      "L": "The LORD is merciful and gracious, slow to anger and abounding in steadfast love.",
      "M": "The LORD is compassionate and gracious, patient in anger and overflowing with steadfast love.",
      "T": "The LORD is compassionate and gracious—\nslow to anger,\noverflowing with steadfast love."
    },
    "9": {
      "L": "He will not always chide, nor will he keep his anger forever.",
      "M": "He does not bring charges forever, nor does he hold on to his anger without end.",
      "T": "He does not keep pressing the case against us.\nHe does not hold his anger\nwithout end."
    },
    "10": {
      "L": "He has not dealt with us according to our sins, nor repaid us according to our iniquities.",
      "M": "He has not treated us as our sins deserve, nor paid us back measure for measure for our iniquities.",
      "T": "He has not dealt with us the way our sins deserve.\nHe has not given back to us\nwhat our iniquities have earned."
    },
    "11": {
      "L": "For as the heavens are high above the earth, so great is his steadfast love toward those who fear him;",
      "M": "For as high as the heavens are above the earth, so great is his steadfast love for those who fear him;",
      "T": "As high as the heavens tower above the earth—\nthat is how great his steadfast love is\nfor those who fear him."
    },
    "12": {
      "L": "as far as the east is from the west, so far does he remove our transgressions from us.",
      "M": "As far as east is from west, that is how far he has removed our transgressions from us.",
      "T": "As far as the east is from the west—\nthat far has he removed our transgressions.\nGone. Not merely covered."
    },
    "13": {
      "L": "As a father has compassion on his children, so the LORD has compassion on those who fear him.",
      "M": "Just as a father is tender toward his children, so the LORD is tender toward those who fear him.",
      "T": "Like a father who holds his children with tenderness—\nthat is how the LORD holds\nthose who fear him."
    },
    "14": {
      "L": "For he knows our frame; he remembers that we are dust.",
      "M": "He knows exactly what we are made of; he has not forgotten that we are dust.",
      "T": "He knows the stuff we are made from—\nhe has not forgotten\nthat we are dust."
    },
    "15": {
      "L": "As for man, his days are like grass; he flourishes like a flower of the field;",
      "M": "As for mortals, their days are like grass; they bloom like a wildflower of the field;",
      "T": "As for mortal man—\nhis days are like grass.\nHe blooms like a wildflower of the field;"
    },
    "16": {
      "L": "for the wind passes over it, and it is gone, and its place knows it no more.",
      "M": "the wind sweeps over it and it vanishes, and the place where it stood no longer knows it.",
      "T": "the wind passes over it — and it is gone.\nThe very ground where it stood\nremembers it no more."
    },
    "17": {
      "L": "But the steadfast love of the LORD is from everlasting to everlasting on those who fear him, and his righteousness to children's children,",
      "M": "But the steadfast love of the LORD is from age to age over those who fear him, and his righteousness reaches to their grandchildren,",
      "T": "But the steadfast love of the LORD —\nit rests on those who fear him,\nfrom age to age, without end.\nHis righteousness reaches down\nto grandchildren and beyond,"
    },
    "18": {
      "L": "to those who keep his covenant and remember to do his commandments.",
      "M": "to those who hold to his covenant and keep his commands in mind to live by them.",
      "T": "to those who hold to his covenant,\nwho keep his commands close\nand live them out."
    },
    "19": {
      "L": "The LORD has established his throne in the heavens, and his kingdom rules over all.",
      "M": "The LORD has set up his throne in the heavens; his kingdom governs everything that exists.",
      "T": "The LORD has set his throne in the heavens.\nHis kingdom reaches over everything."
    },
    "20": {
      "L": "Bless the LORD, O you his angels, you mighty ones who do his word, hearkening to the voice of his word!",
      "M": "Bless the LORD, you his angels — his mighty warriors who carry out his commands, swift to obey his voice!",
      "T": "Bless the LORD — all you his angels,\nhis mighty ones who carry out his word,\nquick to obey the moment they hear it!"
    },
    "21": {
      "L": "Bless the LORD, all his hosts, you ministers of his who do his will!",
      "M": "Bless the LORD, all his armies — all who serve him and carry out his purposes!",
      "T": "Bless the LORD, all his heavenly armies—\nall who serve him\nand do exactly what he desires!"
    },
    "22": {
      "L": "Bless the LORD, all his works, in all places of his dominion. Bless the LORD, O my soul!",
      "M": "Bless the LORD, everything he has made, in every place his reign extends. Bless the LORD, O my soul!",
      "T": "Bless the LORD — all his works,\nin every place his dominion reaches.\nBless the LORD, O my soul!"
    }
  },

  # ===========================================================================
  # Psalm 104 — Anonymous Creation Hymn: God the Maker and Sustainer
  # ===========================================================================
  "104": {
    "1": {
      "L": "Bless the LORD, O my soul! O LORD my God, you are very great; you are clothed with honor and majesty,",
      "M": "Bless the LORD, O my soul! O LORD my God, how great you are — robed in honor and majesty,",
      "T": "Bless the LORD, O my soul!\nLORD my God — how great you are,\nrobed in honor and majesty!"
    },
    "2": {
      "L": "wrapping yourself in light as with a garment, stretching out the heavens like a curtain.",
      "M": "wrapped in light as in a robe, spreading out the heavens like a tent curtain.",
      "T": "You wrap yourself in light as in a robe.\nYou unfurl the heavens\nlike a great tent."
    },
    "3": {
      "L": "He lays the beams of his upper chambers on the waters; he makes the clouds his chariot; he rides on the wings of the wind;",
      "M": "He sets the beams of his upper rooms on the waters; he mounts the clouds as his chariot; he travels on the wings of the wind;",
      "T": "He lays the rafters of his heavenly halls upon the waters above.\nThe clouds are his chariot.\nHe rides the wings of the wind."
    },
    "4": {
      "L": "he makes his messengers winds, his ministers a flaming fire.",
      "M": "He makes the winds his messengers and flashing fire his servants.",
      "T": "He sends the winds as his messengers.\nFire and flame — they do his bidding."
    },
    "5": {
      "L": "He set the earth on its foundations, so that it should never be moved.",
      "M": "He fixed the earth on its foundations so that it will never be shaken.",
      "T": "He set the earth on its foundations—\nit will not be moved,\never."
    },
    "6": {
      "L": "You covered it with the deep as with a garment; the waters stood above the mountains.",
      "M": "You covered it with the deep like a cloak; the waters towered above the mountains.",
      "T": "You covered it in the deep — a garment of flood-water.\nThe waters stood above the mountains."
    },
    "7": {
      "L": "At your rebuke they fled; at the sound of your thunder they took to flight.",
      "M": "At your rebuke they retreated; at the sound of your thunder they fled in haste.",
      "T": "At a single word from you — they fled.\nAt the sound of your thunder\nthey ran."
    },
    "8": {
      "L": "The mountains rose, the valleys sank down to the place that you appointed for them.",
      "M": "The mountains rose and the valleys sank to the places you had set for them.",
      "T": "The mountains rose.\nThe valleys dropped down—\neach to the place you had chosen for them."
    },
    "9": {
      "L": "You set a boundary that they may not pass, so that they might not again cover the earth.",
      "M": "You drew a boundary they cannot cross, so the waters will never again engulf the earth.",
      "T": "You fixed a boundary the waters cannot cross.\nThey will never again\nflood the earth."
    },
    "10": {
      "L": "He sends out springs into the valleys; they flow between the hills;",
      "M": "He sends springs into the valleys; they run between the hills;",
      "T": "He sends springs into the valleys—\nstreams that wind their way\nbetween the hills,"
    },
    "11": {
      "L": "they give drink to every beast of the field; the wild donkeys quench their thirst.",
      "M": "giving water to every wild animal; the wild donkeys slake their thirst there.",
      "T": "giving drink to every wild creature.\nThe wild donkeys come\nand drink their fill."
    },
    "12": {
      "L": "Beside them the birds of the heavens dwell; they sing among the branches.",
      "M": "Along their banks the birds of the sky make their homes and sing among the branches.",
      "T": "Along those banks the birds of the sky settle in—\nsinging from the branches."
    },
    "13": {
      "L": "From his lofty chambers he waters the mountains; the earth is satisfied with the fruit of his works.",
      "M": "From his upper chambers he sends rain down the mountains; the earth is filled by what he provides.",
      "T": "From his high chambers he rains down on the mountains.\nThe earth is filled\nwith all that he makes."
    },
    "14": {
      "L": "He causes the grass to grow for the livestock and plants for man's labor, that he may bring forth food from the earth—",
      "M": "He makes grass grow for the cattle and plants for people to tend so they can bring food out of the ground —",
      "T": "He makes the grass grow for the cattle\nand plants for people to cultivate—\nso they can draw food from the earth:"
    },
    "15": {
      "L": "and wine to gladden the heart of man, and oil to make his face shine, and bread to strengthen man's heart.",
      "M": "wine that lifts the human heart, oil that makes the face glow, and bread that gives strength to the body.",
      "T": "wine to make the human heart glad,\noil to make the face shine bright,\nbread to give the body strength."
    },
    "16": {
      "L": "The trees of the LORD are watered abundantly, the cedars of Lebanon that he planted.",
      "M": "The trees of the LORD drink deeply — the great cedars of Lebanon that he himself planted.",
      "T": "The great trees of the LORD drink their fill—\nthe cedars of Lebanon\nthat he planted with his own hands."
    },
    "17": {
      "L": "In them the birds build their nests; the stork has her home in the fir trees.",
      "M": "There the birds build their nests; the stork finds her home in the cypress trees.",
      "T": "There the birds make their nests.\nThe stork — she has her home\nin the great cypresses."
    },
    "18": {
      "L": "The high mountains are for the wild goats; the rocks are a refuge for the rock badgers.",
      "M": "The rugged mountains belong to the wild goats; the rocky crags shelter the rock badgers.",
      "T": "The high mountains were made for the wild goats.\nThe rocky crags\nare a fortress for the rock badgers."
    },
    "19": {
      "L": "He made the moon to mark the seasons; the sun knows when to go down.",
      "M": "He appointed the moon to mark the seasons; the sun knows exactly when to set.",
      "T": "He made the moon to govern the seasons.\nThe sun knows precisely\nwhen to go down."
    },
    "20": {
      "L": "You make darkness, and it is night, when all the beasts of the forest creep about.",
      "M": "You bring on darkness and it becomes night, when all the forest creatures stir.",
      "T": "You bring on the darkness — night falls—\nand every creature of the forest\ncomes out to move about."
    },
    "21": {
      "L": "The young lions roar for their prey, seeking their food from God.",
      "M": "The young lions roar as they hunt, looking to God for their food.",
      "T": "The young lions roar after their prey—\nthey too are looking to God\nfor their meal."
    },
    "22": {
      "L": "When the sun rises, they steal away and lie down in their dens.",
      "M": "When the sun comes up, they slip away and stretch out in their lairs.",
      "T": "When the sun rises, they steal back\nand lie down\nin their dens."
    },
    "23": {
      "L": "Man goes out to his work and to his labor until the evening.",
      "M": "Then people go out to their work and labor on until the evening.",
      "T": "And then — the people go out.\nThey work through the day\nuntil evening brings them home."
    },
    "24": {
      "L": "O LORD, how manifold are your works! In wisdom you have made them all; the earth is full of your creatures.",
      "M": "LORD, what a multitude of works you have made! You crafted them all in wisdom; the earth is full of what belongs to you.",
      "T": "LORD — how many are your works!\nYou made them all in wisdom.\nThe earth is filled to the brim\nwith what you have made."
    },
    "25": {
      "L": "Here is the sea, great and wide, which teems with creatures without number, living things both small and great.",
      "M": "And here is the sea — vast and wide — teeming with creatures beyond counting, great and small alike.",
      "T": "And the sea — that great, wide sea—\nteeming beyond all counting\nwith creatures great and small."
    },
    "26": {
      "L": "There go the ships, and Leviathan, which you formed to play in it.",
      "M": "The ships sail there, and there is Leviathan, which you formed to frolic in the deep.",
      "T": "The ships sail across it.\nAnd there — Leviathan,\nthe great sea creature you made\nto play in the deep."
    },
    "27": {
      "L": "These all look to you, to give them their food in due season.",
      "M": "All of these look to you to give them their food when they need it.",
      "T": "They all look to you—\nwatching, waiting\nfor their food at the right time."
    },
    "28": {
      "L": "When you give it to them, they gather it up; when you open your hand, they are filled with good things.",
      "M": "When you give, they gather it in; when you open your hand, they are satisfied with good.",
      "T": "When you give — they gather.\nWhen you open your hand—\nthey are filled with good things."
    },
    "29": {
      "L": "When you hide your face, they are dismayed; when you take away their breath, they die and return to their dust.",
      "M": "If you hide your face, they are terrified; if you take back their breath, they die and return to dust.",
      "T": "If you hide your face — they are undone.\nTake back the breath within them—\nthey die and return to dust."
    },
    "30": {
      "L": "When you send forth your spirit, they are created, and you renew the face of the ground.",
      "M": "When you send out your Spirit, they are created, and you renew the surface of the earth.",
      "T": "But send forth your Spirit—\nthey are created.\nYou renew the whole face of the earth."
    },
    "31": {
      "L": "May the glory of the LORD endure forever; may the LORD rejoice in his works!",
      "M": "May the glory of the LORD last forever; may the LORD take delight in what he has made!",
      "T": "May the glory of the LORD endure forever.\nMay the LORD take delight\nin everything he has made!"
    },
    "32": {
      "L": "He looks at the earth and it trembles; he touches the mountains and they smoke.",
      "M": "He looks at the earth and it shakes; he touches the mountains and they pour out smoke.",
      "T": "He looks at the earth — it trembles.\nHe touches the mountains—\nthey pour out smoke."
    },
    "33": {
      "L": "I will sing to the LORD as long as I live; I will make music to my God while I have breath.",
      "M": "I will sing to the LORD as long as I live; I will sing praise to my God for as long as I draw breath.",
      "T": "I will sing to the LORD as long as I live.\nI will make music to my God\nfor as long as there is breath in me."
    },
    "34": {
      "L": "May my meditation be pleasing to him; I will rejoice in the LORD.",
      "M": "May my thoughts about him be sweet to him, as I find my joy in the LORD.",
      "T": "May my meditation be sweet to him.\nI will find my joy\nin the LORD."
    },
    "35": {
      "L": "Let sinners be consumed from the earth, and let the wicked be no more! Bless the LORD, O my soul! Praise the LORD!",
      "M": "Let sinners vanish from the earth and let the wicked exist no longer! Bless the LORD, O my soul! Hallelujah!",
      "T": "Let sinners be swept from the earth.\nLet the wicked be no more.\nBless the LORD, O my soul!\nHallelujah!"
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 103–104 written.')

if __name__ == '__main__':
    main()
