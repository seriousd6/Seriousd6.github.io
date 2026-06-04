"""
MKT Psalms chapters 144–149 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-144-149.py

=== Overview of this unit ===

Six psalms spanning the final Hallel collection (Pss 146–150) and two preceding
royal/acrostic psalms. The unit moves from a royal warrior-psalm (144) through
an acrostic hymn of praise (145) into four cascading hallelujah hymns (146–149)
that accelerate toward the full-chorus finale of Ps 150.

Ps 144 (15 v) — A Royal Warrior's Prayer. David's psalm closely echoing Ps 18
    (which itself appears in 2 Sam 22). God is praised as military trainer (v1),
    then as the cosmic warrior who descends to rescue (vv5-7). The meditation on
    human frailty (vv3-4) echoes Ps 8:4 and Ps 39:5 — man is hebel (vapor/breath),
    his days a passing shadow. Vv7-11 repeat the petition for rescue from "foreigners"
    (H1121 + H5236 bene nekar, sons of the alien) whose mouths speak shav (vain/
    empty) and whose right hand is a right hand of shaqer (falsehood/deception).
    Vv12-15 shift abruptly to a vision of national flourishing — sons like saplings,
    daughters like palace pillars, full granaries, breeding livestock, absence of
    breach and exile, silence in the streets. The beatitude of v15 forms the
    climax: "blessed are the people whose God is the LORD."

Ps 145 (21 v) — The Great Praise. David's only psalm in the Psalter explicitly
    titled "praise" (tehillah). It is an acrostic on all 22 letters of the Hebrew
    alphabet (the nun verse is missing from MT; present in DSS 11QPs^a and
    reflected in LXX). The acrostic structure signals completeness — praise from
    aleph to taw, A to Z. The psalm moves through: personal resolve to praise
    (vv1-2), God's greatness (vv3-6), his goodness and compassion (vv7-9),
    his kingdom (vv10-13), his care for the needy (vv14-16), his righteousness
    and nearness (vv17-20), and a closing doxology (v21). The three key repeated
    words are gadol (great/greatness, vv3,6,7), melek/malkut (king/kingdom,
    vv1,11,12,13), and chesed (steadfast love, vv8, implicit in vv9,17,20).
    This psalm is recited three times daily in Jewish liturgy (the Ashrei).
    The nun verse (DSS: "The LORD is faithful in all his words and gracious in
    all his works") is excluded from the translation since it is absent in MT —
    its content is partially covered by v17.

Ps 146 (10 v) — Trust God, Not Princes. Opens the final Hallel (Pss 146–150),
    each beginning and ending with "Praise the LORD" (Hallelujah). The structural
    contrast is stark: do not trust in princes (vv3-4) because they die and their
    plans die with them; do trust in the God of Jacob (vv5-9) who is the creator,
    the faithful one, the deliverer of the oppressed. Vv7-9 list seven acts of
    divine justice echoing Isaiah's messianic promises (Isa 61:1-2; Luke 4:18-19).
    The LORD's perpetual reign (v10) answers the mortality of princes (v4).

Ps 147 (20 v) — Creator and Covenant-Keeper. Likely post-exilic (v2 references
    gathering the outcasts of Israel; v13-14 celebrate Jerusalem's security and
    provision). The psalm has two main movements divided at v12: cosmic creation
    care (vv1-11) and particular covenant care for Israel (vv12-20). The climax
    is vv19-20 — God's word to Jacob/Israel is set over against the nations who
    have not received it. The contrast between "he finds no pleasure in a horse's
    strength" (v10) and "he takes pleasure in those who fear him" (v11) is central:
    God values reverence over military power.

Ps 148 (14 v) — Cosmic Praise Choir. A two-part psalm calling first the heavens
    (vv1-6) then the earth (vv7-12) to join in praising the LORD, resolved in
    vv13-14. The structure is a literary chiasm of creation categories: angels,
    heavenly hosts, sun/moon/stars, waters above (vv1-4) answering sea-creatures,
    deeps, weather, mountains, trees, animals, humans (vv7-12). The reason (ki,
    "for") is given twice: he commanded and they exist (v5b) and his name alone
    is exalted (v13). The horn of v14 (qeren, strength/honor) signals the
    elevation of Israel within this cosmic choir.

Ps 149 (9 v) — The Sword and the Song. A militaristic hallelujah — the saints
    praise God with new song (v1) and dancing (v3), but also carry double-edged
    swords (v6) to execute written judgments (v9). This combination (worship +
    judgment) is jarring in modern hearing but reflects the OT theology of the
    holy war reversed: the nations who oppressed Israel face the LORD's verdict
    through his covenant people. The "judgment written" (v9) likely refers to
    prophetic decrees (Deut 32; Isa 41-45) rather than any specific text.
    The NT reads this psalm eschatologically — the sharp sword proceeding from
    Christ's mouth in Rev 19:15 echoes this imagery.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T throughout all six psalms. Consistent
    with all prior Psalms scripts. In Ps 144:2, where the MT has אֱלֹהִים
    (elohim) in "my God" position, the address is handled naturally.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Standard throughout.

H2617 (חֶסֶד, chesed): "steadfast love" in L/M/T. Appears explicitly at
    144:2 ("my steadfast love"), 145:8 ("rich in steadfast love"), 147:11
    ("hope in his steadfast love"). No English word captures it fully —
    "steadfast love" preserves the dual sense of loyal obligation and active
    warmth. Consistent with all prior Psalms scripts.

H5315 (נֶפֶשׁ, nefesh): Not prominent in this unit but where "soul" appears
    (147:11 implicitly), rendered "soul" in L/M/T as throughout. Embodied self,
    not Greek immaterial soul — but "soul" preserves traditional piety.

H7307 (רוּחַ, ruach): At 147:18, "wind" — the natural referent is God's warm
    wind melting ice. Not the Spirit in this context. L/M/T all render "wind."
    Context determines sense (Spirit/wind/breath).

H1347 / H1935 (gaon / hod, majesty/splendor): At 145:5, hod is rendered
    "splendor" (L: "honour"); at 145:12, hadar melek (glorious majesty of his
    kingdom) rendered "majestic glory" in M/T. The terms overlap semantically
    and are rendered with honor/splendor/glory according to rhythmic context.

H1984 (halal, praise): The root of "Hallelujah" — "praise Yah." At the opening
    of each Hallelujah psalm (146-149), L/M use "Praise the LORD" for לְאֶל-יָהּ;
    T uses "Hallelujah!" to preserve the liturgical form while making it the
    exclamation of praise that it is. Within the body of each psalm, "praise" is
    the standard rendering throughout.

H7161 (qeren, horn): At 148:14, "horn" symbolizes strength and honor (military
    might by metonymy). L: "the horn of his people"; M: "the strength of his
    people"; T: "his people to a place of honor" — the T tier unpacks the
    metaphor as the text's meaning rather than the vehicle.

H6944 / H2623 (qadosh/chasid, holy/faithful/devoted): At 149:1, 5, 9 the
    chasidim (devoted/faithful ones/saints) are rendered "saints" in L/T (the
    traditional term), "faithful" or "devoted ones" in M for naturalness.
    At 145:17, qadosh modifies the LORD's works — "holy" in all tiers.

H7307 aspect distinction at 147:18: "He causes his wind to blow" — the Hiphil
    of nashab — is causal, not just descriptive. Rendered "he breathes warm wind"
    in T to capture the agency.

=== Aspect and tense notes ===

Ps 144: Perfect verbs opening (v1, "blessed be") as performative praise. Vv5-8
    are imperatives/jussives directed at God. V12 opens a chain of purpose
    clauses ("that our sons may be...") using relative particle + imperfect —
    expressing wish/purpose, not prediction. Rendered as wishes ("may our sons...").

Ps 145: Imperfects of resolve throughout (vv1-2, "I will extol / I will bless").
    Participles and imperfects in descriptive sections (vv14-16) function as
    general truths — present or habitual. Rendered as present tense in M/T.

Ps 146: Imperfects as general truths (vv7-9 — the LORD's characteristic acts).
    Rendered as present tense in M/T: "he executes justice," "he gives food."

Ps 147: Similar to 146. The winter/spring sequence (vv16-18) uses participles
    and imperfects in series — habitual description of the LORD's seasonal
    governance of weather. Rendered as present tense throughout.

Ps 148: Imperatives throughout the summons (vv1-4, 7-12). V5-6 shift to
    jussive + reason clause. V13-14 are jussive + reason. Rendered accordingly.

Ps 149: Imperfects as jussives ("let them praise," "let them sing") in vv1-3, 5.
    V4 is simple imperfect of habitual action ("the LORD takes pleasure").
    V6-9 switch to infinitive constructs with lamed — purpose clauses following
    implied imperative: "with swords in their hands — to execute vengeance."

=== OT intertextuality and NT connections ===

Ps 144:3-4 — Echoes Ps 8:4 ("what is man that you are mindful of him?") and
    Ps 39:5 (hebel, vapor). The NT echoes this anthropology at Jas 4:14.

Ps 145:8 — "Gracious and compassionate, slow to anger, rich in steadfast love"
    is the Exodus 34:6 self-revelation formula — one of the most-cited passages
    in the OT. Psalms 145, 103, 86, Joel 2, Jonah 4, Neh 9 all quote or echo it.

Ps 146:7-9 — The seven acts of divine justice are the source-text for Jesus's
    claim in Luke 4:18-19 (quoting Isa 61:1-2 which itself draws on this pattern).

Ps 147:19-20 — The unique gift of Torah to Israel. Paul meditates on this
    privilege at Rom 3:2 and 9:4.

Ps 148 — This cosmic praise structure shapes the christological hymns of the NT:
    Col 1:15-20 (creation's head); Rev 5:13 ("every creature in heaven and earth").

Ps 149:6 — "Two-edged sword" becomes the word of God in Heb 4:12 and the
    sword from Christ's mouth in Rev 19:15.
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
  "144": {
    "1": {
      "L": "Blessed be the LORD, my rock, who trains my hands for war and my fingers for battle.",
      "M": "Blessed is the LORD, my rock, who trains my hands for war and my fingers for battle.",
      "T": "All praise to the LORD, my unshakeable foundation — he shapes my hands for combat, my fingers for war."
    },
    "2": {
      "L": "My steadfast love and my fortress, my high tower and my deliverer, my shield and he in whom I take refuge, who subdues my people under me.",
      "M": "He is my steadfast love and my fortress, my high tower and my deliverer, my shield and the one in whom I trust, who subdues peoples under me.",
      "T": "My faithful protector, my fortress — the high tower from which I am delivered; my shield, the one I run to, who lays the nations at my feet."
    },
    "3": {
      "L": "O LORD, what is man that you take knowledge of him, or the son of man that you give thought to him?",
      "M": "LORD, what is a human being that you take notice of him, or the son of man that you think of him?",
      "T": "LORD — why does any human merit your attention? Why should mortal humanity occupy your thought at all?"
    },
    "4": {
      "L": "Man is like a breath; his days are like a passing shadow.",
      "M": "A human being is like a breath; his days pass like a shadow.",
      "T": "Humanity is a mere vapor — our days flash by like a shadow crossing the ground."
    },
    "5": {
      "L": "O LORD, bow your heavens and come down; touch the mountains and they shall smoke.",
      "M": "Bow your heavens, LORD, and come down; touch the mountains so that they smoke.",
      "T": "Stoop down from your sky, LORD, and descend — lay your finger on the mountains and watch them smolder."
    },
    "6": {
      "L": "Flash forth lightning and scatter them; shoot out your arrows and rout them.",
      "M": "Send out lightning and scatter them; shoot your arrows and put them to flight.",
      "T": "Throw your lightning bolts and shatter the enemy; loose your arrows and break their ranks."
    },
    "7": {
      "L": "Stretch out your hand from on high; rescue me and deliver me from great waters, from the hand of foreigners,",
      "M": "Reach down your hand from above; rescue me and deliver me from the overwhelming waters, from the hand of foreigners,",
      "T": "Reach down from your heights and pull me free — from the flood that would swallow me, from the grip of alien enemies,"
    },
    "8": {
      "L": "whose mouth speaks vanity, and their right hand is a right hand of falsehood.",
      "M": "whose mouths speak emptiness and whose right hand is a hand of deception.",
      "T": "men who speak nothing but lies, whose handshake is itself a fraud."
    },
    "9": {
      "L": "A new song will I sing to you, O God; upon a psaltery of ten strings will I sing praises to you,",
      "M": "I will sing a new song to you, O God; on a ten-stringed instrument I will sing your praise,",
      "T": "Let me sing you a song that has never been heard before, O God — with the full range of strings I will lift your praise,"
    },
    "10": {
      "L": "who gives salvation to kings, who delivers David his servant from the deadly sword.",
      "M": "who gives victory to kings and rescues his servant David from the deadly sword.",
      "T": "you who hand kings their victories, who have again and again pulled your servant David back from the killing edge."
    },
    "11": {
      "L": "Rescue me and deliver me from the hand of foreigners, whose mouth speaks vanity, and their right hand is a right hand of falsehood.",
      "M": "Deliver me and rescue me from the hand of foreigners, whose mouths speak emptiness and whose right hand is a hand of deception.",
      "T": "Pull me free from these alien enemies — men whose every word is hollow and whose sworn oath means nothing."
    },
    "12": {
      "L": "That our sons may be as plants grown up in their youth; that our daughters may be as corner stones, polished after the similitude of a palace;",
      "M": "May our sons be like vigorous plants in their youth; may our daughters be like carved corner pillars of a palace;",
      "T": "May our sons shoot up like young saplings in the prime of their youth; may our daughters stand like polished pillars carved for a palace hall;"
    },
    "13": {
      "L": "That our garners may be full, affording all manner of store; that our sheep may bring forth thousands and ten thousands in our fields;",
      "M": "may our storehouses be full with every kind of supply; may our flocks produce thousands and ten thousands in our open country;",
      "T": "may our barns overflow with every variety of harvest; may our flocks multiply by tens of thousands across our fields;"
    },
    "14": {
      "L": "That our oxen may be strong to labour; that there be no breaking in, no going out, and no crying in our streets;",
      "M": "may our cattle be well-fitted for labour; may there be no breach and no exile, no cry of distress in our streets;",
      "T": "may our cattle be strong and productive, our land unbroken — no enemy breakthrough, no one dragged into exile, no wailing in the public squares;"
    },
    "15": {
      "L": "Blessed is that people that is in such a case; blessed is that people whose God is the LORD.",
      "M": "Blessed are the people for whom it is so; blessed are the people whose God is the LORD.",
      "T": "How deeply content is the people that lives this way — and most of all, how blessed is the people whose God is the LORD!"
    }
  },
  "145": {
    "1": {
      "L": "I will extol you, my God and King, and bless your name forever and ever.",
      "M": "I will exalt you, my God and King, and bless your name forever and ever.",
      "T": "I lift you high, my God, my King — your name deserves blessing without end, now and always."
    },
    "2": {
      "L": "Every day I will bless you; and I will praise your name forever and ever.",
      "M": "Every day I will bless you and praise your name forever and ever.",
      "T": "Day after day, without exception, I will bless you — your praise is my unending occupation."
    },
    "3": {
      "L": "Great is the LORD, and greatly to be praised; and his greatness is unsearchable.",
      "M": "The LORD is great and highly to be praised; his greatness no one can search out.",
      "T": "The LORD is immeasurably great — the praise due him is equally without measure; there is no bottom to his greatness."
    },
    "4": {
      "L": "One generation shall praise your works to another, and shall declare your mighty acts.",
      "M": "One generation will commend your works to the next and declare your mighty deeds.",
      "T": "Each generation hands down to the next the story of what you have done; each age declares your power anew."
    },
    "5": {
      "L": "I will speak of the glorious honour of your majesty, and of your wondrous works.",
      "M": "I will speak of the splendor of your glorious majesty and of your wonderful deeds.",
      "T": "I will turn over in my mind the brilliant weight of your glory, the wonders you have performed — they are my meditation."
    },
    "6": {
      "L": "And men shall speak of the might of your terrible acts; and I will declare your greatness.",
      "M": "People will speak of the power of your awe-inspiring acts, and I will tell of your greatness.",
      "T": "Others will speak of your fearsome, world-shaking deeds; I will add my voice declaring how great you are."
    },
    "7": {
      "L": "They shall abundantly utter the memory of your great goodness, and shall sing of your righteousness.",
      "M": "They will overflow with praise for your great goodness and sing aloud of your righteousness.",
      "T": "The memory of your overflowing goodness will spill from their mouths; they will break into song over your justice."
    },
    "8": {
      "L": "The LORD is gracious and merciful; slow to anger, and of great steadfast love.",
      "M": "The LORD is gracious and compassionate, slow to anger and rich in steadfast love.",
      "T": "He is gracious and full of compassion — never quick to anger, overflowing with covenant love."
    },
    "9": {
      "L": "The LORD is good to all; and his tender mercies are over all his works.",
      "M": "The LORD is good to all; his compassion extends over all he has made.",
      "T": "His goodness reaches everyone and everything — not a single creature falls outside his tenderness."
    },
    "10": {
      "L": "All your works shall praise you, O LORD; and your saints shall bless you.",
      "M": "All your works will praise you, LORD, and your devoted ones will bless you.",
      "T": "Everything you have made joins in your praise, LORD — and your faithful people lead the song of blessing."
    },
    "11": {
      "L": "They shall speak of the glory of your kingdom, and talk of your power;",
      "M": "They will speak of the glory of your kingdom and tell of your power,",
      "T": "They will speak of your glorious reign and bear witness to your power,"
    },
    "12": {
      "L": "To make known to the sons of man your mighty acts, and the glorious majesty of your kingdom.",
      "M": "to make known to all humanity your mighty deeds and the majestic glory of your kingdom.",
      "T": "so that every human being may know the magnitude of what you do and the splendor of the realm you rule."
    },
    "13": {
      "L": "Your kingdom is an everlasting kingdom, and your dominion endures throughout all generations.",
      "M": "Your kingdom is an everlasting kingdom, and your dominion endures through all generations.",
      "T": "No earthly dynasty lasts — but your reign never ends; your authority spans every generation without exception."
    },
    "14": {
      "L": "The LORD upholds all who fall, and raises up all who are bowed down.",
      "M": "The LORD upholds all who are falling and lifts up all who are brought low.",
      "T": "When anyone falls, the LORD is there to catch them; when anyone is crushed under the weight of life, he lifts them upright."
    },
    "15": {
      "L": "The eyes of all wait upon you; and you give them their food in due season.",
      "M": "The eyes of all look to you, and you give them their food in due season.",
      "T": "Every living creature looks to you — and you reliably provide what each one needs at just the right time."
    },
    "16": {
      "L": "You open your hand, and satisfy the desire of every living thing.",
      "M": "You open your hand and satisfy the desire of every living thing.",
      "T": "You open your hand — and that is enough: every creature's deep need is met."
    },
    "17": {
      "L": "The LORD is righteous in all his ways, and gracious in all his works.",
      "M": "The LORD is righteous in all his ways and faithful in all his works.",
      "T": "In every action he is entirely just; in every deed he is entirely good."
    },
    "18": {
      "L": "The LORD is near to all who call upon him, to all who call upon him in truth.",
      "M": "The LORD is near to all who call on him, to all who call on him in sincerity.",
      "T": "He is close — not distant — to everyone who cries out to him; the only condition is that the cry be genuine."
    },
    "19": {
      "L": "He will fulfil the desire of those who fear him; he will hear their cry and save them.",
      "M": "He fulfills the desire of those who fear him; he hears their cry and saves them.",
      "T": "What those who revere him most deeply want, he gives; he hears their call and comes to the rescue."
    },
    "20": {
      "L": "The LORD preserves all who love him, but all the wicked will he destroy.",
      "M": "The LORD guards all who love him, but he will destroy all the wicked.",
      "T": "His love is a shield for all who love him in return — but there is no future for those who refuse to submit to him."
    },
    "21": {
      "L": "My mouth shall speak the praise of the LORD; and let all flesh bless his holy name forever and ever.",
      "M": "My mouth will speak the praise of the LORD, and let all living things bless his holy name forever and ever.",
      "T": "My lips will carry his praise to the end of my days — and may everything that breathes join in blessing his holy name, now and forever."
    }
  },
  "146": {
    "1": {
      "L": "Praise the LORD! Praise the LORD, O my soul!",
      "M": "Praise the LORD! Praise the LORD, O my soul!",
      "T": "Hallelujah! — my whole inner self, praise the LORD!"
    },
    "2": {
      "L": "I will praise the LORD while I live; I will sing praises to my God while I have being.",
      "M": "I will praise the LORD all my life; I will sing praises to my God as long as I live.",
      "T": "For as long as breath is in me, I will praise him — all my days belong to his praise."
    },
    "3": {
      "L": "Put not your trust in princes, nor in the son of man, in whom there is no help.",
      "M": "Do not put your trust in princes or in any human being, for there is no salvation in them.",
      "T": "Do not stake your life on rulers or on any mortal — human beings cannot ultimately save."
    },
    "4": {
      "L": "His breath departs; he returns to the earth; in that very day his thoughts perish.",
      "M": "When his breath departs, he returns to the earth; on that very day his plans come to nothing.",
      "T": "The moment a human exhales his last, he returns to dust — and every plan he carried dies with him."
    },
    "5": {
      "L": "Blessed is he whose help is the God of Jacob, whose hope is in the LORD his God,",
      "M": "Blessed is the one whose help is the God of Jacob, whose hope is in the LORD his God,",
      "T": "How richly content is the person who relies on the God of Jacob — whose every hope is anchored in the LORD his God,"
    },
    "6": {
      "L": "who made heaven and earth, the sea, and all that is in them; who keeps truth forever;",
      "M": "who made heaven and earth, the sea and everything in them, and who keeps faith forever;",
      "T": "the creator of sky and earth and sea and everything they contain — the one whose faithfulness never breaks."
    },
    "7": {
      "L": "who executes judgment for the oppressed; who gives food to the hungry. The LORD looses the prisoners;",
      "M": "who secures justice for the oppressed and gives food to the hungry. The LORD sets prisoners free;",
      "T": "who stands up for those crushed by power, who feeds the starving. The LORD opens prison doors;"
    },
    "8": {
      "L": "the LORD opens the eyes of the blind; the LORD raises up those who are bowed down; the LORD loves the righteous.",
      "M": "the LORD gives sight to the blind, the LORD lifts up those who are bowed down, the LORD loves the righteous.",
      "T": "he gives sight to the blind, he lifts those who have been flattened by life, he delights in all who live rightly."
    },
    "9": {
      "L": "The LORD preserves the strangers; he relieves the fatherless and widow; but the way of the wicked he turns upside down.",
      "M": "The LORD watches over the alien resident; he supports the fatherless and the widow; but the way of the wicked he overturns.",
      "T": "He protects those without citizenship, sustains the orphan and the widow — but every road the wicked travel, he undermines."
    },
    "10": {
      "L": "The LORD shall reign forever, your God, O Zion, unto all generations. Praise the LORD.",
      "M": "The LORD will reign forever — your God, O Zion, for all generations. Praise the LORD!",
      "T": "And this king — the LORD — reigns without term limit. He is your God, Zion, across every generation. Hallelujah!"
    }
  },
  "147": {
    "1": {
      "L": "Praise the LORD! For it is good to sing praises to our God; for it is pleasant, and praise is comely.",
      "M": "Praise the LORD! For it is good to sing praises to our God; it is pleasant and fitting.",
      "T": "Hallelujah! It is simply good to sing to our God — this is what we were made for, the most fitting thing we can do."
    },
    "2": {
      "L": "The LORD builds up Jerusalem; he gathers together the outcasts of Israel.",
      "M": "The LORD rebuilds Jerusalem and gathers together the exiles of Israel.",
      "T": "The LORD is the one who raises Jerusalem back up; he is the one who gathers Israel's scattered people home."
    },
    "3": {
      "L": "He heals the brokenhearted, and binds up their wounds.",
      "M": "He heals the brokenhearted and bandages their wounds.",
      "T": "He mends the shattered heart and wraps up every wound."
    },
    "4": {
      "L": "He counts the number of the stars; he calls them all by their names.",
      "M": "He counts the stars by number and calls each one by name.",
      "T": "Every star in the sky — he has counted them all and knows each one by name."
    },
    "5": {
      "L": "Great is our Lord, and of great power; his understanding is infinite.",
      "M": "Great is our Lord and mighty in power; his understanding has no limit.",
      "T": "Our Lord is immense — his power is unmatched, his wisdom beyond all calculation."
    },
    "6": {
      "L": "The LORD lifts up the meek; he casts the wicked down to the ground.",
      "M": "The LORD lifts up the humble but brings the wicked down to the ground.",
      "T": "He raises the lowly and throws the wicked face-down into the dust."
    },
    "7": {
      "L": "Sing to the LORD with thanksgiving; sing praises upon the harp to our God;",
      "M": "Sing to the LORD with thanksgiving; make music to our God on the harp.",
      "T": "Come, sing your gratitude to the LORD — let harp-strings carry your praise to our God."
    },
    "8": {
      "L": "who covers the heaven with clouds, who prepares rain for the earth, who makes grass to grow upon the mountains.",
      "M": "He covers the sky with clouds, prepares rain for the earth, and makes grass grow on the hills.",
      "T": "He pulls the clouds across the sky, sets the rain in motion for the earth, and sprouts grass on the bare hillsides."
    },
    "9": {
      "L": "He gives to the beast its food, and to the young ravens which cry.",
      "M": "He gives the animals their food and feeds the young ravens when they call.",
      "T": "Every creature gets its daily portion — even the young ravens crying out receive their share."
    },
    "10": {
      "L": "He does not delight in the strength of the horse; he does not take pleasure in the legs of a man.",
      "M": "He takes no delight in the strength of the horse, nor pleasure in the swiftness of a man.",
      "T": "He is not impressed by military horsepower or human physical strength —"
    },
    "11": {
      "L": "The LORD takes pleasure in those who fear him, in those who hope in his steadfast love.",
      "M": "but the LORD delights in those who fear him, in those who hope in his steadfast love.",
      "T": "his delight is in those who hold him in reverence, in those who anchor their hope in his covenant love."
    },
    "12": {
      "L": "Praise the LORD, O Jerusalem; praise your God, O Zion.",
      "M": "Praise the LORD, O Jerusalem! Praise your God, O Zion!",
      "T": "Jerusalem, lift your praise! Zion, glorify your God!"
    },
    "13": {
      "L": "For he has strengthened the bars of your gates; he has blessed your children within you.",
      "M": "For he has reinforced the bars of your gates and blessed your children within you.",
      "T": "He has bolted your city gates against every enemy and blessed the children who fill your streets."
    },
    "14": {
      "L": "He makes peace in your borders, and fills you with the finest of the wheat.",
      "M": "He establishes peace within your borders and satisfies you with the finest wheat.",
      "T": "He brings shalom to every boundary and feeds you on the cream of the harvest."
    },
    "15": {
      "L": "He sends forth his commandment upon the earth; his word runs very swiftly.",
      "M": "He sends his command to the earth; his word runs swiftly.",
      "T": "He speaks — and his word races across the earth, carrying out his will without delay."
    },
    "16": {
      "L": "He gives snow like wool; he scatters the hoarfrost like ashes.",
      "M": "He spreads snow like a blanket of wool and scatters frost like ashes.",
      "T": "Snow falls at his word like wool laid over the land; frost is scattered like handfuls of ash."
    },
    "17": {
      "L": "He casts forth his ice like morsels; who can stand before his cold?",
      "M": "He hurls down hailstones like bread crumbs — who can withstand his cold?",
      "T": "His hail strikes the ground like thrown chunks of bread — and who can survive the cold he sends?"
    },
    "18": {
      "L": "He sends out his word, and melts them; he causes his wind to blow, and the waters flow.",
      "M": "He sends his word and melts them; he makes his wind blow and the waters flow.",
      "T": "Then he speaks again, and the freeze breaks; he breathes warm wind and the streams begin to run."
    },
    "19": {
      "L": "He declares his word to Jacob, his statutes and his judgments to Israel.",
      "M": "He has declared his word to Jacob, his statutes and ordinances to Israel.",
      "T": "To Jacob he has spoken his very word; Israel has received his laws and covenant standards."
    },
    "20": {
      "L": "He has not dealt so with any nation; and as for his judgments, they have not known them. Praise the LORD.",
      "M": "He has not done this for any other nation; they do not know his ordinances. Praise the LORD!",
      "T": "No other people on earth has been given this — they remain without his word. Hallelujah!"
    }
  },
  "148": {
    "1": {
      "L": "Praise the LORD! Praise the LORD from the heavens; praise him in the heights!",
      "M": "Praise the LORD! Praise the LORD from the heavens; praise him in the heights above!",
      "T": "Hallelujah! From the heights of heaven, from the highest reaches — praise the LORD!"
    },
    "2": {
      "L": "Praise him, all his angels; praise him, all his hosts!",
      "M": "Praise him, all his angels! Praise him, all his heavenly armies!",
      "T": "Every angel — praise him! Every heavenly battalion — praise him!"
    },
    "3": {
      "L": "Praise him, sun and moon; praise him, all you stars of light!",
      "M": "Praise him, sun and moon; praise him, all shining stars!",
      "T": "Sun and moon, give him praise! Every glittering star, praise him!"
    },
    "4": {
      "L": "Praise him, you heavens of heavens, and you waters that are above the heavens.",
      "M": "Praise him, you highest heavens, and you waters above the skies.",
      "T": "You outermost heavens, praise him! And you waters vaulted above the sky — join in!"
    },
    "5": {
      "L": "Let them praise the name of the LORD; for he commanded, and they were created.",
      "M": "Let them praise the name of the LORD, for he commanded and they came into being.",
      "T": "Let everything praise the LORD's name — because at his word it all sprang into existence."
    },
    "6": {
      "L": "He has also established them forever and ever; he has made a decree which shall not pass away.",
      "M": "He has fixed them in their places forever and ever; he has issued a decree that cannot be revoked.",
      "T": "He set them in place for all time — his word stands like an unbreakable law; not one can depart from its station."
    },
    "7": {
      "L": "Praise the LORD from the earth, you dragons, and all deeps;",
      "M": "Praise the LORD from the earth, you sea monsters and all ocean depths,",
      "T": "From the depths of the earth, join the praise — great sea-creatures and all that lurks in the abyss,"
    },
    "8": {
      "L": "fire and hail; snow and vapour; stormy wind fulfilling his word;",
      "M": "fire and hail, snow and mist, stormy winds that carry out his command,",
      "T": "fire and hailstorm, snow and fog, violent wind obeying his orders —"
    },
    "9": {
      "L": "mountains and all hills; fruitful trees and all cedars;",
      "M": "mountains and all hills, fruit trees and all cedars,",
      "T": "mountains high and low, fruit trees and towering cedars,"
    },
    "10": {
      "L": "beasts and all cattle; creeping things and flying fowl;",
      "M": "wild beasts and all livestock, creeping things and flying birds,",
      "T": "wild animals and tame, creatures that crawl and birds that soar —"
    },
    "11": {
      "L": "kings of the earth and all peoples; princes and all judges of the earth;",
      "M": "kings of the earth and all peoples, princes and all rulers of the earth,",
      "T": "every king and every nation, every prince and every magistrate —"
    },
    "12": {
      "L": "both young men and maidens; old men and children:",
      "M": "young men and young women together, the aged and children —",
      "T": "the young and the old, men and women, grandparents and small children —"
    },
    "13": {
      "L": "let them praise the name of the LORD; for his name alone is excellent; his glory is above the earth and heaven.",
      "M": "let them praise the name of the LORD, for his name alone is exalted; his glory is above earth and sky.",
      "T": "let everything and everyone praise the LORD's name — his name alone towers over all; his glory fills both earth and heaven."
    },
    "14": {
      "L": "He also exalts the horn of his people, the praise of all his saints; even of the children of Israel, a people near to him. Praise the LORD.",
      "M": "He has raised high the strength of his people, the praise of all his devoted ones, of the children of Israel, the people near to him. Praise the LORD!",
      "T": "He has lifted his people to a place of honor — his faithful ones, the children of Israel, those who live in his nearness. Hallelujah!"
    }
  },
  "149": {
    "1": {
      "L": "Praise the LORD! Sing to the LORD a new song, and his praise in the congregation of the saints.",
      "M": "Praise the LORD! Sing a new song to the LORD, his praise in the assembly of the faithful.",
      "T": "Hallelujah! Let the community of the faithful sing the LORD a song that has never been sung before."
    },
    "2": {
      "L": "Let Israel rejoice in him that made him; let the children of Zion be joyful in their King.",
      "M": "Let Israel rejoice in their Maker; let the people of Zion be joyful in their King.",
      "T": "Israel, take your delight in the one who made you; Zion's children, exult in your King!"
    },
    "3": {
      "L": "Let them praise his name in the dance; let them sing praises to him with the timbrel and harp.",
      "M": "Let them praise his name with dancing and make music to him with tambourine and lyre.",
      "T": "Let them dance his praise and play it on drum and harp — nothing held back."
    },
    "4": {
      "L": "For the LORD takes pleasure in his people; he will beautify the meek with salvation.",
      "M": "For the LORD takes pleasure in his people; he adorns the humble with victory.",
      "T": "He delights in this people — and he crowns the lowly with the splendor of his deliverance."
    },
    "5": {
      "L": "Let the saints be joyful in glory; let them sing aloud upon their beds.",
      "M": "Let the faithful exult in his glory; let them sing for joy even on their beds.",
      "T": "May his devoted people shout with triumph in the night — even lying down, they cannot contain their song."
    },
    "6": {
      "L": "Let the high praises of God be in their mouth, and a two-edged sword in their hand;",
      "M": "with the high praises of God in their mouths and a double-edged sword in their hands,",
      "T": "With God's praise shouted from their throats and sharp swords in their hands,"
    },
    "7": {
      "L": "to execute vengeance upon the heathen, and punishments upon the peoples;",
      "M": "to execute vengeance on the nations and bring judgment on the peoples,",
      "T": "they go to execute the LORD's judgment on the nations — to bring the sentence he has decreed upon the peoples,"
    },
    "8": {
      "L": "to bind their kings with chains, and their nobles with fetters of iron;",
      "M": "to bind their kings in chains and their nobles in iron fetters,",
      "T": "to chain every king, to fetter every nobleman in iron,"
    },
    "9": {
      "L": "to execute upon them the judgment written; this honour have all his saints. Praise the LORD.",
      "M": "to carry out on them the judgment that is written — this is the honor of all his faithful ones. Praise the LORD!",
      "T": "to carry out to the letter what has been decreed — this is the high calling, the honor given to all his faithful people. Hallelujah!"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 144–149 written.')

if __name__ == '__main__':
    main()
