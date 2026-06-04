"""
MKT Psalms chapters 43–48 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-43-48.py

=== Overview of this unit ===

Ps 43 — Petition for Divine Vindication (5 verses, no superscription): Ps 43 is a
         continuation of Ps 42; many manuscripts and commentators treat them as a single
         psalm with a repeating refrain (42:5,11 = 43:5). The psalmist pleads for God to
         send his light and truth as guides to the sanctuary. No YHWH (H3068) appears —
         God is addressed entirely as Elohim throughout. Part of the Elohistic Psalter
         (Ps 42–83), where YHWH is systematically replaced with Elohim.

Ps 44 — National Lament; Corporate Complaint (26 verses): A Maskil of the sons of Korah.
         Three movements: recital of past victories (vv1–8), lament of present humiliation
         (vv9–16), protestation of covenant loyalty (vv17–22), and urgent petition
         (vv23–26). V22 ("for your sake we are killed all the day long; regarded as sheep
         for slaughter") is quoted by Paul in Romans 8:36. Selah in v8.

Ps 45 — Royal Wedding Song; Messianic Psalm (17 verses): A Song of Loves (שִׁיר יְדִידֹת),
         a Maskil of the sons of Korah. The poet praises the king (vv1–9), addresses the
         bride (vv10–15), and closes with a promise of lasting legacy (vv16–17). Hebrews
         1:8–9 applies vv6–7 directly to Christ. No selah.

Ps 46 — God Is Our Refuge; Zion Theology (11 verses): A Song of the sons of Korah upon
         Alamoth (a technical performance note, likely soprano voices or high-register
         strings). Cosmic chaos defeated (vv1–3), the city of God secured (vv4–7), God's
         sovereign declaration (vv8–11). Martin Luther's "A Mighty Fortress" is based on
         this psalm. Three selahs: vv3, 7, 11.

Ps 47 — God Is King Over All the Earth (9 verses): Enthronement psalm of the sons of
         Korah. Universal praise summoned (vv1–2), nations subdued (vv3–4), God's ascent
         celebrated (v5), four-fold call to praise (v6), God enthroned over all (vv7–9).
         Selah in v4.

Ps 48 — The Beauty and Security of Zion (14 verses): A Song and Psalm of the sons of
         Korah. Praises God's holy mountain (vv1–3), recounts the routing of enemy kings
         (vv4–7), reflects on God's steadfast love in the temple (vv8–9), calls for praise
         and proclamation (vv10–13), closes with "this God is our God forever" (v14).
         Selah in v8.

=== Superscriptions ===

Following the convention of PSA-1 through PSA-6b, superscription text is merged into v1
of each psalm, separated from the verse body by a blank line in T tier.

Psalm 43 has no superscription; its v1 begins directly with the petition.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M throughout. T tier: "the LORD." These psalms are in the
      Elohistic Psalter (Ps 42–83); YHWH appears explicitly only at Ps 46:7,8,11 and
      Ps 47:2,5 and Ps 48:1,8. No shift to "Yahweh" — no prior PSA script made that move.

H430  (אֱלֹהִים, Elohim): "God" in all tiers. Ps 43 uses only Elohim. Ps 45:6 addresses
      the king with the vocative "O God" (אֱלֹהִים) — see NT connection note below.

H410  (אֵל, El, Ps 43:4): "God" in all tiers. "God my exceeding joy" = "God, the source
      of my deepest joy."

H5315 (נֶפֶשׁ, nefesh):
      - Ps 43:5: "my soul" in L/M; "my soul" retained in T to preserve the refrain echo
        of Ps 42:5,11 — the repetition is the point.
      - Ps 44:25: "our soul" in L/M; T: "our very self" to surface the embodied-self sense.

H2617 (חֶסֶד, hesed, Ps 44:26; 48:9): "steadfast love" in all tiers — MKT standard.

H1285 (בְּרִית, berit, Ps 44:17): "covenant" in all tiers.

H5542 (סֶלָה, selah): Retained as "Selah" in all tiers, appended to the verse end.
      Appears at: Ps 44:8; Ps 46:3,7,11; Ps 47:4; Ps 48:8.

H4581 (מָעוֹז, ma'oz, Ps 43:2): Literally "strength/stronghold." L/M: "strength" (carrying
      both senses); T: "fortress" to foreground the military-refuge nuance.

H5945 (עֶלְיוֹן, Elyon, Ps 46:4; 47:2): "Most High" in all tiers — established convention.

H6635 (צְבָאוֹת, tseva'ot, Ps 46:7,11; 48:8): "hosts" in all tiers — "LORD of hosts"
      maintained as an established divine title with liturgical resonance.

H7503 (רָפָה, Ps 46:10): "Be still" in L/M; T: "Cease striving" — the root means
      "to relax/let go/sink," and T surfaces the underlying call to stop fighting God's
      sovereignty with anxious effort.

H3678 (כִּסֵּא, Ps 45:6; 47:8): "throne" in all tiers.
H7626 (שֵׁבֶט, Ps 45:6): "scepter" in all tiers.

H6664 (צֶדֶק, Ps 45:6,7; 48:10): "righteous/righteousness" in L/M; T uses "justice"
      at Ps 45:6 ("a scepter of justice") to surface the governance sense, and
      "righteousness" at Ps 45:7 and Ps 48:10 where the moral quality is primary.

H1347 (גָּאוֹן, ga'on, Ps 47:4): "pride/excellency." Rendered "glory" in M/T to express
      the sense of Israel's land as the highest honor God bestowed on Jacob, avoiding
      the pejorative English connotation of "pride."

H4043 (מָגֵן, Ps 47:9): Literally "shields." L: "shields"; M/T: "rulers" — in context,
      the shields of the earth = the protecting rulers/nobles of the nations who surrender
      sovereignty to God.

H7919 (שָׂכַל, Ps 47:7): "with understanding/skillfully." L: "with a Maskil"; M: "with
      understanding"; T: "thoughtfully" — the call is for praise that is not mindless
      but theologically informed.

H4192 (מוּת, Ps 48:14): "death." L/M: "unto death" — the guide who leads us even through
      death. T: "even through death" to foreground the eschatological confidence.
      (Note: some traditions read this as עַלְמוֹת "forever/Alamoth," but MT reads מוּת
      "death"; MKT follows MT.)

=== OT echoes and NT connections ===

- Ps 43:5 refrain = Ps 42:5,11 — the repeating refrain across both psalms creates a
  deliberate literary arc from distress through hope.
- Ps 44:22 → Romans 8:36 — Paul quotes the verse to frame believers' suffering as
  covenant-loyal suffering in continuity with Israel's lament tradition.
- Ps 45:6–7 → Hebrews 1:8–9 — The divine address to the king ("Your throne, O God,
  is forever") is applied to Christ by the author of Hebrews.
- Ps 46:10 "Be still" → Mark 4:39 — Jesus' rebuke of the storm echoes God's sovereign
  silencing of chaos.
- Ps 47:5 "God has gone up with a shout" → Acts 1:9 (the ascension); the psalm's
  enthronement language shapes NT understanding of Christ's exaltation.
- Ps 48:2 "on the sides of the north" (יַרְכְּתֵי צָפוֹן) — Mount Zaphon was the Canaanite
  divine mountain; Ps 48 implicitly claims Zion as its replacement: Israel's God dwells
  where the rival gods were said to hold court.

=== Aspect and tense notes ===

Lament psalms (Ps 43, 44) use Hebrew perfects to describe ongoing states of abandonment
or historical realities. Praise and enthronement psalms (Ps 46, 47, 48) use perfects to
assert accomplished divine action ("God has gone up," "kings assembled and fled").
Present tense is preferred in English where the Hebrew is expressing timeless or ongoing
truth, even when the Hebrew verb form is perfect.
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
  "43": {
    "1": {
      "L": "Judge me, O God, and plead my cause against an ungodly nation; from the deceitful and unjust man deliver me.",
      "M": "Vindicate me, O God, and plead my cause against an ungodly nation; from the deceitful and unjust man deliver me.",
      "T": "Judge my case, O God;\nplead my cause against this godless nation —\ndeliver me from the man who is all lies and injustice."
    },
    "2": {
      "L": "For you are the God of my strength; why have you cast me off? Why do I go about mourning because of the oppression of the enemy?",
      "M": "For you are the God who is my stronghold; why have you rejected me? Why do I go about mourning under the oppression of the enemy?",
      "T": "You are the God who is my fortress — so why have you turned your back on me?\nWhy do I walk in mourning\nwhile my enemy presses down on me?"
    },
    "3": {
      "L": "Send out your light and your truth; let them lead me, let them bring me to your holy hill and to your tabernacles.",
      "M": "Send out your light and your truth; let them lead me, let them bring me to your holy mountain and to your dwelling place.",
      "T": "Send out your light, send out your faithfulness —\nlet them lead me, guide me\nto your holy mountain, to the place where you dwell."
    },
    "4": {
      "L": "Then I will go to the altar of God, to God my exceeding joy, and I will praise you with the harp, O God my God.",
      "M": "Then I will approach the altar of God, to God who is my greatest joy, and I will praise you with the harp, O God my God.",
      "T": "Then I will come to the altar of God —\nto God, the source of my deepest joy —\nand I will praise you with the harp,\nO God, my God."
    },
    "5": {
      "L": "Why are you cast down, O my soul? And why are you in tumult within me? Hope in God; for I shall again praise him, the salvation of my countenance and my God.",
      "M": "Why are you downcast, O my soul? Why are you in turmoil within me? Put your hope in God; for I will yet praise him, the salvation of my face and my God.",
      "T": "Why are you so downcast, my soul?\nWhy this turmoil churning inside me?\nPut your hope in God —\nI will yet praise him again,\nthe one who saves me and is my God."
    }
  },
  "44": {
    "1": {
      "L": "To the chief Musician, a Maskil of the sons of Korah. O God, with our ears we have heard; our fathers have told us the work you did in their days, in the days of old.",
      "M": "To the choirmaster, a Maskil of the sons of Korah. O God, we have heard with our own ears; our ancestors have told us what you accomplished in their time, in the days long ago.",
      "T": "To the worship leader. A Maskil of the sons of Korah.\n\nO God, we have heard it with our own ears —\nour ancestors told us\nwhat you did in their time,\nin those days long before us."
    },
    "2": {
      "L": "With your own hand you drove out the nations and planted our fathers; you afflicted the peoples and cast them out.",
      "M": "With your own hand you drove out the nations and planted our ancestors; you crushed the peoples and expelled them.",
      "T": "With your own hand you drove out nations\nand planted our people in their place;\nyou shattered peoples\nand thrust them out."
    },
    "3": {
      "L": "For not by their own sword did they possess the land, nor did their own arm save them; but your right hand and your arm, and the light of your face, because you had favor toward them.",
      "M": "For they did not win the land by their own sword, and their own arm did not deliver them; it was your right hand and your arm and the light of your face, because you were favorable toward them.",
      "T": "It was not their swords that gave them the land;\nit was not their own strength that saved them.\nIt was your right hand, your arm,\nthe light of your face —\nbecause you were pleased with them."
    },
    "4": {
      "L": "You are my King, O God; command deliverances for Jacob.",
      "M": "You are my King, O God; decree victories for Jacob.",
      "T": "You are my King, O God;\ndecree deliverance for Jacob."
    },
    "5": {
      "L": "Through you we push down our foes; through your name we tread underfoot those who rise against us.",
      "M": "Through you we push back our enemies; in your name we trample those who rise against us.",
      "T": "Through you we drive back our enemies;\nby your name we trample those who rise against us."
    },
    "6": {
      "L": "For not in my bow do I trust, and my sword does not save me.",
      "M": "For I do not trust in my bow, and my sword cannot bring me victory.",
      "T": "I do not put my confidence in my bow;\nmy sword cannot deliver me."
    },
    "7": {
      "L": "But you have saved us from our enemies and have put to shame those who hate us.",
      "M": "But you have saved us from our enemies and disgraced those who hate us.",
      "T": "But you — you are the one who saves us from our enemies\nand covers those who hate us with shame."
    },
    "8": {
      "L": "In God we have boasted all the day long, and your name we will praise forever. Selah",
      "M": "In God we have boasted all day long, and we will praise your name forever. Selah",
      "T": "In God we have made our boast all day long;\nyour name we will praise to the ages.\nSelah."
    },
    "9": {
      "L": "But you have rejected us and disgraced us, and have not gone out with our armies.",
      "M": "But you have cast us off and brought us to disgrace, and have not gone out with our armies.",
      "T": "But now — you have thrown us away, covered us in disgrace;\nyou no longer march out with our armies."
    },
    "10": {
      "L": "You make us turn back from the enemy, and those who hate us have plundered us.",
      "M": "You made us retreat before the enemy, and our enemies plundered us.",
      "T": "You have made us turn tail before the enemy;\nthose who hate us have stripped us bare."
    },
    "11": {
      "L": "You have given us like sheep for food and have scattered us among the nations.",
      "M": "You handed us over like sheep for slaughter and scattered us among the nations.",
      "T": "You handed us over like sheep destined for slaughter;\nyou scattered us among the nations."
    },
    "12": {
      "L": "You sell your people for nothing and have not increased your wealth by their price.",
      "M": "You sold your people for a pittance and made no profit from the sale.",
      "T": "You sold your own people for nothing —\nyou gained not a thing from the transaction."
    },
    "13": {
      "L": "You have made us a taunt to our neighbors, a scorn and a derision to those around us.",
      "M": "You have made us the object of mockery to our neighbors, a laughingstock and a source of scorn to those around us.",
      "T": "You have made us the butt of jokes among our neighbors —\nscorn and derision to everyone nearby."
    },
    "14": {
      "L": "You have made us a byword among the nations, a shaking of the head among the peoples.",
      "M": "You have made us a byword among the nations, a wagging of heads among the peoples.",
      "T": "We have become a proverb of misfortune among the nations;\nthe peoples shake their heads at us."
    },
    "15": {
      "L": "All the day long my disgrace is before me, and shame has covered my face.",
      "M": "All day long my disgrace is before me, and shame has covered my face.",
      "T": "My humiliation is before me all day long;\nshame has covered my face."
    },
    "16": {
      "L": "Because of the voice of the one who reproaches and blasphemes, because of the enemy and the avenger.",
      "M": "On account of the taunting voice of the one who reviles and blasphemes, because of the enemy who seeks revenge.",
      "T": "The mocker's voice rings in my ears —\nthe enemy who wants revenge fills my world with shame."
    },
    "17": {
      "L": "All this has come upon us, yet we have not forgotten you, and we have not been false to your covenant.",
      "M": "All this has come upon us, yet we have not forgotten you, and we have not been unfaithful to your covenant.",
      "T": "All this has fallen on us — and yet we have not forgotten you;\nwe have not been disloyal to your covenant."
    },
    "18": {
      "L": "Our heart has not turned back, and our steps have not departed from your way.",
      "M": "Our heart has not turned away, and our steps have not strayed from your path.",
      "T": "Our heart did not draw back;\nour feet did not wander from your path."
    },
    "19": {
      "L": "Yet you have broken us in the place of jackals and covered us with the shadow of death.",
      "M": "Yet you have crushed us in the haunt of jackals and covered us with the shadow of death.",
      "T": "Yet you crushed us in a desert haunt of jackals\nand wrapped us in deathly darkness."
    },
    "20": {
      "L": "If we had forgotten the name of our God, or stretched out our hands to a foreign god —",
      "M": "If we had forgotten the name of our God or spread our hands in prayer toward a foreign god —",
      "T": "If we had forgotten the name of our God,\nor spread our hands in prayer toward a foreign god —"
    },
    "21": {
      "L": "Would God not search this out? For he knows the secrets of the heart.",
      "M": "Would God not discover this? For he knows the hidden things of the heart.",
      "T": "Would God not have found it out?\nHe knows every secret the heart conceals."
    },
    "22": {
      "L": "Yet for your sake we are killed all the day long; we are regarded as sheep for the slaughter.",
      "M": "Yet for your sake we face death all day long; we are counted as sheep destined for slaughter.",
      "T": "But for your sake we face death all day long;\nwe are counted as sheep marked for slaughter."
    },
    "23": {
      "L": "Awake! Why are you sleeping, O Lord? Rouse yourself! Do not cast us off forever!",
      "M": "Wake up! Why are you sleeping, O Lord? Rise up! Do not reject us forever!",
      "T": "Wake up, Lord — why are you sleeping?\nRise up! Do not abandon us forever!"
    },
    "24": {
      "L": "Why do you hide your face? Why do you forget our affliction and our oppression?",
      "M": "Why do you hide your face? Why do you ignore our affliction and our oppression?",
      "T": "Why do you turn your face away?\nWhy have you forgotten our suffering and our misery?"
    },
    "25": {
      "L": "For our soul is bowed down to the dust; our belly clings to the earth.",
      "M": "For our soul is brought down to the dust; our body clings to the ground.",
      "T": "We are pressed flat — our very self ground into the dust;\nour bodies cling to the earth."
    },
    "26": {
      "L": "Rise up; come to our help! Redeem us for the sake of your steadfast love.",
      "M": "Rise up and help us! Deliver us for the sake of your steadfast love.",
      "T": "Rise up — come and help us!\nFor the sake of your steadfast love, redeem us."
    }
  },
  "45": {
    "1": {
      "L": "To the chief Musician upon Shoshannim, for the sons of Korah, a Maskil, a Song of Loves. My heart is stirred with a goodly matter; I speak of the things I have composed concerning the king; my tongue is the pen of a ready writer.",
      "M": "To the choirmaster. On Shoshannim. For the sons of Korah. A Maskil, a Song of Loves. My heart is overflowing with a beautiful theme; I address my poem to the king; my tongue is the pen of a skilled scribe.",
      "T": "To the worship leader. To the tune of 'The Lilies.' For the sons of Korah. A Maskil, a Love Song.\n\nMy heart is overflowing with a beautiful theme —\nI address my words to the king.\nMy tongue moves like the pen\nof a masterful writer."
    },
    "2": {
      "L": "You are fairer than the sons of men; grace is poured into your lips; therefore God has blessed you forever.",
      "M": "You are more handsome than any other man; grace is poured into your lips; therefore God has blessed you forever.",
      "T": "You are the most beautiful of men;\nwhat you say is filled with grace.\nTherefore God has blessed you forever."
    },
    "3": {
      "L": "Gird your sword upon your thigh, O most mighty, with your glory and your majesty.",
      "M": "Strap your sword on your thigh, O champion, in your glory and splendor.",
      "T": "Strap your sword to your thigh, O champion —\nclothe yourself in glory and magnificence."
    },
    "4": {
      "L": "And in your majesty ride out victoriously for the cause of truth and meekness and righteousness; let your right hand teach you awesome things.",
      "M": "Ride out victoriously in your splendor for the sake of truth, humility, and righteousness; let your right hand achieve awesome deeds.",
      "T": "Ride out in your splendor and conquer —\nchampioning truth, humility, and justice.\nLet your right hand do great and fearsome things."
    },
    "5": {
      "L": "Your arrows are sharp; peoples fall under you; the arrows are in the heart of the king's enemies.",
      "M": "Your arrows are sharp, bringing peoples down beneath you; they pierce into the hearts of the king's enemies.",
      "T": "Your arrows fly true;\nnations collapse beneath you;\nthey pierce through the hearts of your enemies."
    },
    "6": {
      "L": "Your throne, O God, is forever and ever; the scepter of your kingdom is a scepter of uprightness.",
      "M": "Your throne, O God, is forever and ever; the scepter of your kingdom is a righteous scepter.",
      "T": "Your throne, O God, stands forever and ever;\nthe scepter of your kingdom is a scepter of justice."
    },
    "7": {
      "L": "You have loved righteousness and hated wickedness; therefore God, your God, has anointed you with the oil of gladness above your companions.",
      "M": "You have loved righteousness and hated wickedness; therefore God, your God, has anointed you with the oil of gladness beyond all your companions.",
      "T": "You have loved what is right and hated what is wrong —\nso God, your own God, has anointed you\nwith the oil of celebration,\nexalting you above all who stand beside you."
    },
    "8": {
      "L": "All your garments are fragrant with myrrh and aloes and cassia; from ivory palaces strings have made you glad.",
      "M": "All your robes are fragrant with myrrh, aloes, and cassia; from ivory palaces the music of strings has brought you joy.",
      "T": "Myrrh, aloe, and cassia — your robes carry their fragrance;\nfrom within the ivory halls, music has filled your heart with joy."
    },
    "9": {
      "L": "Daughters of kings are among your honored women; at your right hand stands the queen in gold of Ophir.",
      "M": "Daughters of kings are among your ladies of honor; at your right hand stands the queen arrayed in gold of Ophir.",
      "T": "Among your ladies of honor are daughters of kings;\nand at your right hand stands the queen\ndressed in the finest gold of Ophir."
    },
    "10": {
      "L": "Hear, O daughter, and consider, and incline your ear; forget your own people and your father's house.",
      "M": "Listen, daughter, and pay attention; lean in with your ear: forget your own people and your father's house.",
      "T": "Listen, daughter — pay close attention;\nlean in with your ear:\nleave your people behind,\nforget your father's house."
    },
    "11": {
      "L": "And the king will desire your beauty; for he is your lord, and bow down to him.",
      "M": "Then the king will desire your beauty; because he is your lord, bow down to him.",
      "T": "The king desires your beauty —\nhe is your lord; honor him."
    },
    "12": {
      "L": "The daughter of Tyre with a gift; the rich among the people will entreat your favor.",
      "M": "The daughter of Tyre comes bearing a gift; the wealthy among the nations will seek your favor.",
      "T": "Even the daughter of Tyre brings gifts;\nthe wealthiest of peoples come seeking your grace."
    },
    "13": {
      "L": "The king's daughter is all glorious within; her clothing is of wrought gold.",
      "M": "The king's daughter is altogether beautiful within; her garment is interwoven with gold.",
      "T": "The daughter of the king — glorious within;\nher gown is woven through with gold."
    },
    "14": {
      "L": "In embroidered garments she shall be brought to the king; the virgins, her companions, shall follow her and be led to you.",
      "M": "In embroidered garments she will be led to the king; the maidens, her companions, will follow her and be brought to you.",
      "T": "Robed in embroidered cloth she is led to the king;\nher companions — the young women of her court —\nfollow behind her."
    },
    "15": {
      "L": "With gladness and rejoicing shall they be led; they shall enter into the king's palace.",
      "M": "With joy and celebration they will be led in; they will enter the king's palace.",
      "T": "With joy and exultation they come in;\nthey enter the halls of the king."
    },
    "16": {
      "L": "In the place of your fathers shall be your sons; you shall make them princes throughout all the earth.",
      "M": "In place of your ancestors will be your sons; you will appoint them as princes throughout all the earth.",
      "T": "Where your ancestors were, your sons will stand;\nyou will set them as princes across the whole earth."
    },
    "17": {
      "L": "I will make your name to be remembered in all generations; therefore the peoples shall praise you forever and ever.",
      "M": "I will cause your name to be remembered in all generations; therefore the peoples will praise you forever and ever.",
      "T": "I will make your name live on in every generation;\ntherefore the nations will praise you forever and ever."
    }
  },
  "46": {
    "1": {
      "L": "To the chief Musician, for the sons of Korah, a Song upon Alamoth. God is our refuge and strength, a very present help in trouble.",
      "M": "To the choirmaster, for the sons of Korah, a Song on Alamoth. God is our refuge and strength, a help that is always present in times of trouble.",
      "T": "To the worship leader. For the sons of Korah. To Alamoth. A Song.\n\nGod is our refuge and our strength —\na help that is always ready in the moment of trouble."
    },
    "2": {
      "L": "Therefore we will not fear though the earth changes, though the mountains are moved into the midst of the sea.",
      "M": "Therefore we will not fear, even if the earth gives way, even if the mountains topple into the heart of the sea.",
      "T": "Therefore we will not be afraid —\nnot even if the earth itself collapses,\nnot even if the mountains plunge into the heart of the sea."
    },
    "3": {
      "L": "Though its waters roar and foam, though the mountains tremble at its swelling. Selah",
      "M": "Though the waters roar and churn, though the mountains quake at the surging sea. Selah",
      "T": "Though the waters rage and foam,\nthough mountains tremble at the rising tide —\nSelah."
    },
    "4": {
      "L": "There is a river whose streams make glad the city of God, the holy place of the dwelling of the Most High.",
      "M": "There is a river whose streams bring joy to the city of God, the sacred dwelling of the Most High.",
      "T": "But there is a river —\nits streams bringing gladness to the city of God,\nthe holy place where the Most High makes his home."
    },
    "5": {
      "L": "God is in the midst of her; she shall not be moved; God will help her when morning arrives.",
      "M": "God is within her; she will not be shaken; God will help her when morning breaks.",
      "T": "God is within her — she will not be shaken;\nGod will come to her aid\nwhen the morning comes."
    },
    "6": {
      "L": "The nations raged, the kingdoms tottered; he raised his voice, the earth melted.",
      "M": "Nations raged and kingdoms shook; he lifted his voice, and the earth dissolved.",
      "T": "Nations roared, kingdoms crumbled —\nhe raised his voice\nand the earth melted away."
    },
    "7": {
      "L": "The LORD of hosts is with us; the God of Jacob is our stronghold. Selah",
      "M": "The LORD of hosts is with us; the God of Jacob is our fortress. Selah",
      "T": "The LORD of hosts is with us;\nthe God of Jacob is our high fortress.\nSelah."
    },
    "8": {
      "L": "Come, behold the works of the LORD, how he has made desolations in the earth.",
      "M": "Come and see what the LORD has done, what desolations he has brought upon the earth.",
      "T": "Come — look at what the LORD has done;\nsee what devastation he has laid across the earth."
    },
    "9": {
      "L": "He makes wars cease to the end of the earth; he breaks the bow and shatters the spear; he burns the chariots in the fire.",
      "M": "He puts an end to wars across the whole earth; he breaks bows and cuts spears apart; he burns the war-chariots with fire.",
      "T": "He brings war to its end at the edges of the earth —\nsnapping bows, splintering spears,\nburning every chariot to ash."
    },
    "10": {
      "L": "Be still, and know that I am God; I will be exalted among the nations, I will be exalted in the earth.",
      "M": "Be still, and know that I am God; I will be exalted among the nations; I will be exalted throughout the earth.",
      "T": "'Cease striving — and know that I am God.\nI will be lifted high among the nations;\nI will be lifted high over all the earth.'"
    },
    "11": {
      "L": "The LORD of hosts is with us; the God of Jacob is our stronghold. Selah",
      "M": "The LORD of hosts is with us; the God of Jacob is our fortress. Selah",
      "T": "The LORD of hosts is with us;\nthe God of Jacob is our high fortress.\nSelah."
    }
  },
  "47": {
    "1": {
      "L": "To the chief Musician, a Psalm for the sons of Korah. Clap your hands, all peoples; shout to God with the voice of triumph.",
      "M": "To the choirmaster. A Psalm of the sons of Korah. Clap your hands, all you peoples; shout to God with a voice of joy.",
      "T": "To the worship leader. A Psalm of the sons of Korah.\n\nClap your hands, all you peoples;\nshout to God with a voice of triumph!"
    },
    "2": {
      "L": "For the LORD Most High is awesome, a great King over all the earth.",
      "M": "For the LORD Most High is to be feared; he is a great King over the whole earth.",
      "T": "For the LORD Most High is awesome —\na great King over all the earth."
    },
    "3": {
      "L": "He subdues peoples under us and nations under our feet.",
      "M": "He subdues peoples under us and nations beneath our feet.",
      "T": "He subdues nations beneath us\nand peoples under our feet."
    },
    "4": {
      "L": "He chose our inheritance for us, the pride of Jacob whom he loved. Selah",
      "M": "He chose our inheritance for us, the glory of Jacob whom he loved. Selah",
      "T": "He chose our inheritance for us —\nthe glory given to Jacob, whom he loved.\nSelah."
    },
    "5": {
      "L": "God has gone up with a shout, the LORD with the sound of a trumpet.",
      "M": "God has ascended with shouts of joy, the LORD with the sound of a ram's horn.",
      "T": "God has ascended to his throne —\nto shouts of joy, to the blast of the shofar."
    },
    "6": {
      "L": "Sing praises to God, sing praises! Sing praises to our King, sing praises!",
      "M": "Sing praises to God, sing praises! Sing praises to our King, sing praises!",
      "T": "Sing praise to God — sing praise!\nSing praise to our King — sing praise!"
    },
    "7": {
      "L": "For God is the King of all the earth; sing praises with a Maskil.",
      "M": "For God is the King of the whole earth; sing praises with understanding.",
      "T": "For God is King over all the earth;\nlet your praise be thoughtful and full of meaning."
    },
    "8": {
      "L": "God reigns over the nations; God sits on his holy throne.",
      "M": "God reigns over the nations; God is seated on his holy throne.",
      "T": "God reigns over the nations —\nGod is seated on his holy throne."
    },
    "9": {
      "L": "The princes of the peoples are gathered as the people of the God of Abraham; for the shields of the earth belong to God; he is greatly exalted.",
      "M": "The nobles of the nations have gathered as the people of the God of Abraham; for the rulers of the earth belong to God; he is highly exalted.",
      "T": "The princes of the nations have gathered\nto become the people of the God of Abraham.\nThe rulers of the earth belong to God —\nhe is lifted high above them all."
    }
  },
  "48": {
    "1": {
      "L": "A Song, a Psalm of the sons of Korah. Great is the LORD and greatly to be praised in the city of our God, in his holy mountain.",
      "M": "A Song, a Psalm of the sons of Korah. Great is the LORD and greatly to be praised in the city of our God, on his holy mountain.",
      "T": "A Song. A Psalm of the sons of Korah.\n\nGreat is the LORD, worthy of all praise,\nin the city of our God, on his holy mountain."
    },
    "2": {
      "L": "Beautiful in elevation, the joy of all the earth, is Mount Zion, on the sides of the north, the city of the great King.",
      "M": "Mount Zion, beautiful in its height, is the joy of all the earth; on the heights of the north it rises, the city of the great King.",
      "T": "Mount Zion — beautiful in its height,\nthe joy of all the earth.\nFrom its northern heights it stands:\nthe city of the great King."
    },
    "3": {
      "L": "Within her palaces God has made himself known as a stronghold.",
      "M": "Within her citadels God has shown himself to be a fortress.",
      "T": "In her towers and citadels\nGod has revealed himself as a sure refuge."
    },
    "4": {
      "L": "For behold, the kings assembled; they passed by together.",
      "M": "For look — the kings assembled; they came against her together.",
      "T": "Look — the kings of the earth joined forces;\nthey came advancing together."
    },
    "5": {
      "L": "They saw it and were astonished; they were dismayed and fled in panic.",
      "M": "They saw it and were bewildered; they were struck with terror and fled.",
      "T": "They saw — and stopped cold;\nthey were thrown into terror and fled."
    },
    "6": {
      "L": "Trembling seized them there, anguish like a woman in labor.",
      "M": "Trembling took hold of them there, pain like that of a woman giving birth.",
      "T": "Trembling seized them on the spot —\nanguish like a woman in the grip of labor."
    },
    "7": {
      "L": "By the east wind you break the ships of Tarshish.",
      "M": "With the east wind you shatter the ships of Tarshish.",
      "T": "With an east wind you scatter\nthe great ships of Tarshish."
    },
    "8": {
      "L": "As we have heard, so we have seen in the city of the LORD of hosts, in the city of our God; God will establish it forever. Selah",
      "M": "As we have heard, so we have seen in the city of the LORD of hosts, in the city of our God; God establishes it forever. Selah",
      "T": "What we had only heard, now we have seen:\nhere in the city of the LORD of hosts,\nhere in the city of our God —\nGod keeps it safe forever.\nSelah."
    },
    "9": {
      "L": "We have thought on your steadfast love, O God, in the midst of your temple.",
      "M": "We have meditated on your steadfast love, O God, within your temple.",
      "T": "In the heart of your temple, O God,\nwe have dwelt on your steadfast love."
    },
    "10": {
      "L": "As your name, O God, so your praise reaches to the ends of the earth; your right hand is full of righteousness.",
      "M": "As your name reaches, O God, so does your praise, to the ends of the earth; your right hand is full of righteousness.",
      "T": "As great as your name is, O God,\nso great is your praise — stretching to the farthest edge of the earth.\nYour right hand overflows with righteousness."
    },
    "11": {
      "L": "Let Mount Zion rejoice; let the daughters of Judah be glad because of your judgments.",
      "M": "Let Mount Zion rejoice; let the towns of Judah be glad because of your righteous judgments.",
      "T": "Let Mount Zion shout with joy;\nlet every town of Judah be glad —\nbecause of your righteous judgments."
    },
    "12": {
      "L": "Walk about Zion, go around her, count her towers.",
      "M": "Walk all around Zion, circle her, count her towers.",
      "T": "Walk all around Zion — encircle her;\ncount her towers."
    },
    "13": {
      "L": "Consider well her ramparts, go through her palaces, that you may tell the next generation.",
      "M": "Mark her walls carefully, tour her citadels, that you may tell the next generation.",
      "T": "Study her walls carefully, walk through her citadels —\nso that you can tell the coming generation."
    },
    "14": {
      "L": "For this is God, our God forever and ever; he will be our guide even unto death.",
      "M": "For this God is our God forever and ever; he will guide us until the very end.",
      "T": "This is what God is — our God forever and ever.\nHe will lead us even through death."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 43–48 written.')

if __name__ == '__main__':
    main()
