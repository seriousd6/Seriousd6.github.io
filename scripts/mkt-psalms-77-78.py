"""
MKT Psalms chapters 77–78 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-77-78.py

=== Overview of this unit ===

Ps 77 (20 v) — A personal lament by Asaph, dedicated to Jeduthun (one of David's three
    Levitical choir leaders, 1 Chr 16:41-42). The psalm moves in two sharply contrasted
    halves: vv1-10 = the anguish of a sleepless, questioning night (the darkest lament
    language of the Psalter — seven rhetorical questions in vv7-9, each pressing harder
    on the silence of God); vv11-20 = the deliberate turn to memory (the Exodus, the sea
    crossing, the storm theophany). The resolution is not an answer to the questions
    but a decision: "I will remember the works of the LORD" (v11).

    The pivot verse (v10) is the most difficult in the psalm. The Hebrew reads literally
    "And I said, This is my sickness — the years of the right hand of the Most High." Two
    readings compete: (a) the psalmist is accusing God ("the right hand of the Most High
    has changed — that is what is making me sick"); (b) the psalmist catches himself and
    names his own despair as the sickness, then pivots to remember what God's right hand
    once did. We follow reading (b) — the turn is the psalm's structural purpose and vv11-
    20 confirm it. L renders the ambiguity; M clarifies; T makes the pivot explicit.

    vv16-19 form a magnificent theophany poem — storm, lightning, thunder, earthquake —
    the presence of God at the sea. v20 then deliberately deflates the grandeur: after all
    the cosmic imagery, God "led his people like a flock, by the hand of Moses and Aaron."
    The anti-climax is the point: the God of the storm is also the shepherd.

Ps 78 (72 v) — A Maskil (H4905: instructive/contemplative poem) of Asaph. The longest
    didactic psalm in the Psalter, a sweeping recital of the Exodus, wilderness rebellion,
    conquest, and the eventual choosing of Zion and David. Its purpose is pedagogical:
    every generation must be told this story so they do not repeat the sin-forgetting-
    punishment cycle of their ancestors.

    Structure:
    vv1-8:  Prologue — call to hear; commitment to transmit the story to children
    vv9-11: Ephraim's failure at the battle — the paradigm case of armored cowardice
    vv12-16: The Exodus signs — Zoan, the sea, cloud, fire, water from rock
    vv17-31: Wilderness rebellion — complaining for food; quail; the plague mid-meal
    vv32-39: Ongoing sin; God's patience; the great grace verse (v38)
    vv40-55: Plagues recounted; God's leading to the land
    vv56-64: Israel's idolatry; the fall of Shiloh; the ark in captivity
    vv65-72: God awakens; rejects Ephraim; chooses Judah, Zion, and David

    KEY citation: v2 ("I will open my mouth in a parable... dark sayings of old") is
    applied to Jesus in Matthew 13:35 as fulfillment of prophecy about his parabolic
    teaching. The Hebrew word for "parable" is H4912 mashal; the Greek equivalent is
    parabole. This is documented; the psalm text follows the Hebrew original.

    v38 is one of the great grace verses of the OT: God "being full of compassion,
    forgave their iniquity and did not destroy them; many times he turned his anger away
    and did not stir up all his wrath." The word for "forgave" is H3722 kipper — the
    atonement/covering root. Rendered "covered over / forgave" in L/M; T makes the
    weight of the grace explicit.

    The ending (vv65-72) pivots dramatically from punishment to hope: God "awoke like a
    warrior" and chose Judah/Zion/David. The David cameo (vv70-72) — from sheep pens to
    shepherd-king — closes the psalm with the covenant's answer to all the preceding
    failure.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps) in L/M. In T: "the LORD" or "LORD" per cadence.
    Consistent with all prior Psalms scripts. Appears at Ps 78:4, 21.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. Still within the Elohistic Psalter (Book III
    begins at Ps 73, and Elohim continues as the dominant divine title through Ps 89).

H410 (אֵל, El): "God" in all tiers. Short divine title. Appears prominently in Ps 78.

H136 (אֲדֹנָי, Adonai): "the Lord" (not LORD) in Ps 77:2,7. The sovereign title, distinct
    from the personal name YHWH.

H3050 (יָהּ, Yah): The short form of the divine name, appearing in Ps 77:11 ("works of
    the LORD" — technically "works of Yah"). Rendered "the LORD" in all tiers. Consistent
    with prior Psalms scripts.

H5945 (עֶלְיוֹן, Elyon): "Most High" in all tiers. Appears at Ps 77:10; Ps 78:17, 35, 56.

H2617 (חֶסֶד, chesed): Does not appear in Ps 77-78 as a key term. Not a focus in this
    unit (though the concept of God's covenant mercy underlies v38's "compassion").

H7349 (רַחוּם, rachum): "full of compassion" in L/M at Ps 78:38. In T: "full of
    compassion." The root רָחַם (racham) is the womb-love / deep mercy term.

H3722 (כִּפֶּר, kipper): The atonement/covering verb at Ps 78:38. "Forgave" in L/M
    (functional rendering). In T: "covered over their guilt." The atonement resonance
    is documented here; surface text uses "forgave."

H5315 (נֶפֶשׁ, nefesh): "soul" in L at Ps 77:2. In M: "soul." In T: "deep within me"
    (capturing the refusal of comfort as a whole-person response, not just inner feeling).
    At Ps 78:18: "their appetite" in L/M (the context is lusting for food); "what they
    craved" in T. At Ps 78:50: "their lives" in L/M; "their very lives" in T.

H7307 (רוּחַ, ruach): "spirit" in Ps 77:3,6 in L/M; "spirit" in T. The psalmist's inner
    being, not the divine Spirit. At Ps 78:8: "their spirit" in L/M/T.

H1285 (בְּרִית, berit): "covenant" in all tiers at Ps 78:10, 37. Formal oath-bound
    relationship. Consistent with all prior Hebrew scripts.

H8451 (תּוֹרָה, torah): "law" in L; "instruction" or "teaching" in M/T at Ps 78:1,5,10.
    The context is a teacher addressing "my people" — torah here is the authoritative
    revelation transmitted across generations, not merely Mosaic legislation.

H5542 (סֶלָה, Selah): Retained as "Selah" in all tiers. Appears at Ps 77:3,9,15.

H4905 (מַשְׂכִּיל, Maskil): The superscription genre marker for Ps 78. "A Maskil" in L;
    "A contemplative poem" or "A teaching poem" in M/T. Consistent with prior Psalms
    scripts.

H3038 (יְדוּתוּן, Jeduthun): The Levitical choir leader in Ps 77's superscription.
    Retained as "Jeduthun" in all tiers (proper name).

=== Textual and interpretive notes ===

Ps 77:2 — "my hand was outstretched in the night without ceasing": The Hebrew yadi (my
    hand) niggerah (poured out / stretched out) laylah (at night) with lo tafug (did not
    cease). The image is of the psalmist's hands raised in prayer all night, unable to
    stop. The KJV "my sore ran in the night" is archaic; modern translations correctly
    render this as the outstretched hand of prayer.

Ps 77:10 — Pivot verse. See Overview above. Ambiguity preserved in L; reading (b)
    clarified in M and T.

Ps 78:2 and Matthew 13:35 — The evangelist applies this verse to Jesus' parabolic
    teaching as fulfillment of prophecy. The psalm text follows the Hebrew; the NT
    application is documented here only.

Ps 78:25 — "food of the mighty ones / bread of angels": H47 abirim = "mighty ones" —
    not the standard word for angels (H4397 mal'ak) but a title used of divine beings
    (cf. Job 41:25). Rendered "mighty ones" in L; "angels" in M (functional equivalent
    most readers expect); "what angels eat" in T (interpretive).

Ps 78:38 — The central grace verse. The phrase "turned back his wrath" and "did not
    stir up all his wrath" together convey repeated, partial restraint of deserved
    judgment — not once but "many times" (H7235 rabbah). The T tier makes this
    cumulative restraint visible.

Ps 78:63 — "their young women had no wedding song": The Hebrew hullalah means "were not
    praised in a song" — the reference is to the absence of the customary praise-songs
    sung at weddings for young women. Rendered "no wedding song" in L/M; T: "no wedding
    songs were sung for them."

=== Aspect and tense notes ===

Ps 77 — vv1-10 are primarily Hebrew perfect and imperfect expressing past ongoing anguish
    (narrative). vv11-12 are cohortative ("I will remember," "I will meditate") — vows
    of resolve. vv13-20 shift to the hymnic indicative describing God's nature and the
    Exodus theophany.

Ps 78 — The prologue (vv1-8) uses cohortatives of resolve ("I will open," "we will not
    hide") and purpose clauses. The historical survey (vv9-64) alternates between
    narrative perfects (past events) and frequentative imperfects (habitual rebellion:
    "they kept sinning," "they would return"). The ending (vv65-72) uses perfects of
    completed divine action (God arose, chose, built, took David).
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
  # Psalm 77 — The Sleepless Night and the Memory of the Exodus
  # ===========================================================================
  "77": {
    "1": {
      "L": "To the chief Musician. To Jeduthun. A Psalm of Asaph. I cried aloud to God with my voice; with my voice to God, and he gave ear to me.",
      "M": "To the director of music. To Jeduthun. A Psalm of Asaph. I called out to God with my full voice; I cried to God, and he listened.",
      "T": "To the choirmaster. To Jeduthun. A Psalm of Asaph.\nI cried out to God with everything in me.\nWith all my voice I called—and he heard."
    },
    "2": {
      "L": "In the day of my trouble I sought the Lord; in the night my hand was stretched out without ceasing; my soul refused to be comforted.",
      "M": "In the day of my trouble I sought the Lord; through the night my hand was outstretched without ceasing; my soul refused to be comforted.",
      "T": "On the day of my trouble I reached toward the Lord.\nAll night my hands stayed raised—I could not stop.\nDeep within me refused every comfort."
    },
    "3": {
      "L": "I remembered God and was troubled; I complained, and my spirit was overwhelmed. Selah",
      "M": "I thought of God and I groaned; I poured out my grief until my spirit grew faint. Selah",
      "T": "I thought of God—and groaned.\nI kept turning it over until my spirit gave out.\nSelah."
    },
    "4": {
      "L": "You hold my eyelids open; I am so troubled I cannot speak.",
      "M": "You kept my eyes wide open through the night; I was too troubled to speak.",
      "T": "You held my eyelids open—no sleep, no rest.\nI was overwhelmed past the point of words."
    },
    "5": {
      "L": "I have considered the days of old, the years of ancient times.",
      "M": "I think about the days of old, the years of long ago.",
      "T": "I reach back into the past—\nthose ancient years, those days of old."
    },
    "6": {
      "L": "I call to mind my song in the night; I meditate in my heart, and my spirit searches carefully.",
      "M": "I recall my song in the night; I ponder in my heart, and my spirit searches deeply.",
      "T": "I remember the songs of the night.\nI turn the question over in my heart.\nMy spirit searches—and keeps searching."
    },
    "7": {
      "L": "Will the Lord cast off forever, and be favorable no more?",
      "M": "Will the Lord reject us forever? Will he never again be pleased with us?",
      "T": "Has the Lord abandoned us for good?\nWill he never be favorable again?"
    },
    "8": {
      "L": "Has his steadfast love ceased forever? Has his word come to an end for all generations?",
      "M": "Has his steadfast love ceased once and for all? Has his promise failed for every generation to come?",
      "T": "Is his steadfast love simply over—permanently?\nHas his word run out, for every generation to come?"
    },
    "9": {
      "L": "Has God forgotten to be gracious? Has he in anger shut up his compassion? Selah",
      "M": "Has God forgotten to show grace? Has he locked away his compassion in his anger? Selah",
      "T": "Has God forgotten mercy?\nHas anger slammed the door on his compassion?\nSelah."
    },
    "10": {
      "L": "And I said, 'This is my grief: the years of the right hand of the Most High.'",
      "M": "Then I said, 'This is the sickness that is killing me — that the right hand of the Most High seems to have changed.' So I will remember what that right hand once did.",
      "T": "Then I named it:\n'This is my deepest wound—\nthat the right hand of the Most High once acted\nand seems to act no more.'\nBut I will go back to what that hand once did."
    },
    "11": {
      "L": "I will remember the deeds of the LORD; surely I will remember your wonders of old.",
      "M": "I will call to mind the works of the LORD; yes, I will remember your wonders from of old.",
      "T": "I will remember what the LORD has done.\nYes—I will remember your wonders from long ago."
    },
    "12": {
      "L": "I will meditate on all your works, and muse on all your mighty deeds.",
      "M": "I will meditate on all your works and think carefully about everything you have done.",
      "T": "I will turn over everything you have done in my mind.\nI will dwell on every act of your power."
    },
    "13": {
      "L": "O God, your way is in holiness; who is so great a God as our God?",
      "M": "O God, your path runs through what is holy; what god anywhere is as great as our God?",
      "T": "Your road runs through holiness, God—\nthrough what is set apart and sacred.\nWhat God is as great as you?"
    },
    "14": {
      "L": "You are the God who works wonders; you have made your strength known among the peoples.",
      "M": "You are the God who performs wonders; you have declared your power among the nations.",
      "T": "You are the God of wonders.\nYou have made your power known to every nation."
    },
    "15": {
      "L": "You with your arm redeemed your people, the sons of Jacob and Joseph. Selah",
      "M": "With your strong arm you redeemed your people, the descendants of Jacob and Joseph. Selah",
      "T": "You stretched out your arm and bought back your people—\nthe children of Jacob and Joseph.\nSelah."
    },
    "16": {
      "L": "The waters saw you, O God; the waters saw you and trembled; the depths also were troubled.",
      "M": "The waters saw you, O God; the waters saw you and recoiled; the very depths were shaken.",
      "T": "The waters saw you, God.\nThey saw you—and shuddered.\nThe depths convulsed."
    },
    "17": {
      "L": "The clouds poured out water; the skies gave forth a sound; your arrows shot out in every direction.",
      "M": "The clouds poured down rain; the sky resounded; your arrows flashed out in every direction.",
      "T": "The clouds opened and emptied themselves.\nThe sky roared.\nYour arrows blazed in every direction."
    },
    "18": {
      "L": "The voice of your thunder was in the whirlwind; the lightning lit up the world; the earth trembled and shook.",
      "M": "Your thunder rolled through the churning heavens; your lightning illuminated the world; the earth trembled and quaked.",
      "T": "Your thunder rolled through the churning sky.\nYour lightning tore the world open with light.\nThe earth shook—all the way down."
    },
    "19": {
      "L": "Your way was through the sea, your path through the great waters; yet your footprints were unseen.",
      "M": "Your path went through the sea, your way through the great deep; but your footprints could not be found.",
      "T": "Your road cut straight through the sea—\nyour path ran through the great deep.\nAnd no one could find your footprints."
    },
    "20": {
      "L": "You led your people like a flock, by the hand of Moses and Aaron.",
      "M": "You guided your people like a flock, through the leadership of Moses and Aaron.",
      "T": "You led your people like a flock.\nBy the hand of Moses and Aaron\nyou brought them through."
    }
  },

  # ===========================================================================
  # Psalm 78 — A Maskil of Asaph: Israel's History of Failure and God's Faithfulness
  # ===========================================================================
  "78": {
    "1": {
      "L": "A Maskil of Asaph. Give ear, O my people, to my teaching; incline your ears to the words of my mouth.",
      "M": "A contemplative poem of Asaph. Listen, O my people, to my instruction; pay close attention to what I am about to say.",
      "T": "A teaching poem of Asaph.\nListen, my people—lean in close.\nI have something to say, and I need you to hear it."
    },
    "2": {
      "L": "I will open my mouth in a parable; I will utter dark sayings from of old.",
      "M": "I will open my mouth with a parable; I will speak of things hidden from ages past.",
      "T": "I will open my mouth in a parable—\nwhat I say will be layered, drawn from the ancient depths."
    },
    "3": {
      "L": "That which we have heard and known, and our fathers have declared to us—",
      "M": "What we have heard and come to know, what our ancestors passed down to us—",
      "T": "What we have heard and verified—\nwhat our fathers set in our hands—"
    },
    "4": {
      "L": "we will not hide from their children; we will tell the coming generation the praiseworthy deeds of the LORD, his strength, and the wonders he has done.",
      "M": "we will not conceal from their children. We will tell the next generation of the LORD's praiseworthy deeds, his power, and the wonderful things he has done.",
      "T": "we will not keep hidden from our children.\nWe will pass it on to the next generation:\nthe LORD's glory,\nhis strength,\nthe wonders his hands have done."
    },
    "5": {
      "L": "For he established a testimony in Jacob and set a law in Israel, which he commanded our fathers to make known to their children,",
      "M": "For he established a formal testimony in Jacob and ordained a law in Israel, which he commanded our ancestors to teach their children,",
      "T": "He built it into the structure of Israel—\na standing testimony in Jacob, a law among his covenant people—\nand commanded our ancestors to hand it on."
    },
    "6": {
      "L": "so that the coming generation might know them — children not yet born — and who would arise and declare them to their own children,",
      "M": "so that the generation to come would know these things — even children not yet born — and when they grew up, would tell them to their own children,",
      "T": "So that the coming generation would know—\neven children not yet born—\nand when they grew up, they would tell their own children."
    },
    "7": {
      "L": "so that they might set their hope in God, and not forget his works, but keep his commandments,",
      "M": "so they would place their confident hope in God, and would not forget what he has done, but would keep his commands,",
      "T": "So they would learn to hope in God,\nwould not forget what he has done,\nand would live by what he commanded."
    },
    "8": {
      "L": "and might not be as their fathers — a stubborn and rebellious generation, a generation that did not set its heart aright, and whose spirit was not faithful to God.",
      "M": "and would not be like their ancestors — a stubborn and rebellious generation that did not fix its heart on God and whose spirit was not faithful to him.",
      "T": "Not like their ancestors.\nThat generation was stubborn and rebellious—\nthey would not set their hearts toward God,\nand their spirit never settled into faithfulness."
    },
    "9": {
      "L": "The sons of Ephraim, equipped with bows and armed, turned back on the day of battle.",
      "M": "The men of Ephraim, though armed with bows, turned back when the day of battle came.",
      "T": "Ephraim—equipped, armed, ready.\nAnd yet they turned and ran\non the day of battle."
    },
    "10": {
      "L": "They did not keep the covenant of God, and refused to walk in his law.",
      "M": "They failed to keep God's covenant and refused to live by his instruction.",
      "T": "They broke the covenant.\nThey refused to walk in God's way."
    },
    "11": {
      "L": "And they forgot his works and his wonders that he had shown them.",
      "M": "They forgot what he had done and the wonders he had shown them.",
      "T": "They forgot.\nAll of it—the wonders right before their eyes."
    },
    "12": {
      "L": "Wondrous things he did in the sight of their fathers, in the land of Egypt, in the field of Zoan.",
      "M": "He performed remarkable deeds in plain sight of their ancestors — in the land of Egypt, in the region of Zoan.",
      "T": "Right in front of their ancestors he performed wonders—\nin Egypt,\nin the fields around Zoan."
    },
    "13": {
      "L": "He divided the sea and caused them to pass through; he made the waters stand like a heap.",
      "M": "He split the sea and brought them through; he made the water stand in walls.",
      "T": "He split the sea open and walked them through.\nThe water stood in walls on either side."
    },
    "14": {
      "L": "In the daytime he led them with a cloud, and all night long with a light of fire.",
      "M": "In the daytime he led them with a cloud, and all night long with a column of fire.",
      "T": "All day, a cloud overhead to guide them.\nAll night, a pillar of fire."
    },
    "15": {
      "L": "He split the rocks in the wilderness and gave them drink as from the great depths.",
      "M": "He split open rocks in the wilderness and gave them water to drink as from the great deep.",
      "T": "He cracked open rocks in the wilderness\nand gave them water to drink—\nstreams welling up from the depths."
    },
    "16": {
      "L": "He brought streams also out of the rock and caused water to run down like rivers.",
      "M": "He brought streams out of the rock and made the water flow down in rivers.",
      "T": "He drew flowing streams from solid rock—\nwater running like rivers."
    },
    "17": {
      "L": "Yet they sinned still more against him, provoking the Most High in the wilderness.",
      "M": "Yet they kept on sinning against him, provoking the Most High in the wilderness.",
      "T": "And still they sinned—\nmore and more of it.\nIn the wilderness they provoked the Most High."
    },
    "18": {
      "L": "They tested God in their heart by asking food for their appetite.",
      "M": "They deliberately tested God in their hearts, demanding food to satisfy their cravings.",
      "T": "They tested God—a deliberate choice, made in their hearts.\nThey demanded what they wanted to eat."
    },
    "19": {
      "L": "They spoke against God; they said, 'Can God furnish a table in the wilderness?'",
      "M": "They spoke against God, saying, 'Can God really lay out a meal here in the wilderness?'",
      "T": "They spoke against God.\n'Can God manage a dinner table out here in the wilderness?' they said."
    },
    "20": {
      "L": "'Behold, he struck the rock and waters gushed out, and streams overflowed — but can he give bread also? Can he provide flesh for his people?'",
      "M": "'Look, he hit a rock and water poured out, streams overflowed — but can he also supply bread? Can he provide meat for his whole people?'",
      "T": "'Yes, he hit a rock and water came rushing out—\ncreeks everywhere.\nBut bread? Can he do bread?\nMeat for this whole crowd?'"
    },
    "21": {
      "L": "Therefore the LORD heard and was wroth; a fire was kindled against Jacob, and anger came up against Israel,",
      "M": "Therefore the LORD heard what they said and became furious; a fire broke out against Jacob, and his anger rose up against Israel,",
      "T": "The LORD heard all of it—\nand he was furious.\nFire broke out against Jacob.\nWrath rose up against Israel."
    },
    "22": {
      "L": "because they did not believe in God and did not trust in his salvation.",
      "M": "because they refused to believe in God and put no trust in his power to save.",
      "T": "They refused to believe in God.\nThey put no stock in his power to save them."
    },
    "23": {
      "L": "Though he had commanded the clouds from above and opened the doors of heaven,",
      "M": "Yet he had already commanded the clouds above and opened the doors of heaven;",
      "T": "He had already commanded the clouds.\nHe had already opened heaven's doors."
    },
    "24": {
      "L": "and had rained down manna on them to eat and had given them grain from heaven.",
      "M": "He had rained down manna for them to eat and had given them grain from heaven.",
      "T": "He had rained manna down for them to eat—\ngrain from heaven itself."
    },
    "25": {
      "L": "Man ate of the food of the mighty ones; he sent them provisions to the full.",
      "M": "Human beings ate the food of angels; he sent them abundant provisions.",
      "T": "People ate what angels eat—\nfood sent down from above, as much as they could hold."
    },
    "26": {
      "L": "He caused the east wind to blow in the heavens; and by his power he steered the south wind.",
      "M": "He caused an east wind to blow through the sky; and by his power he drove the south wind.",
      "T": "He sent the east wind sweeping through the sky\nand drove the south wind along with it."
    },
    "27": {
      "L": "He rained flesh upon them as thick as dust, and winged birds as numerous as the sand of the sea.",
      "M": "He rained meat on them as thick as dust and birds with wings as numerous as grains of sea sand.",
      "T": "Meat fell from the sky like dust.\nBirds came down as thick as sand at the seashore."
    },
    "28": {
      "L": "And he let it fall in the midst of their camp, round about their habitations.",
      "M": "He dropped it right in the middle of their camp, all around where they lived.",
      "T": "It fell right in their camp—\naround every tent."
    },
    "29": {
      "L": "So they ate and were well filled; for he gave them what they had craved.",
      "M": "They ate and were completely satisfied; he had given them exactly what they wanted.",
      "T": "They ate. They were completely full.\nHe had given them everything they asked for."
    },
    "30": {
      "L": "They were not yet estranged from their craving; while the food was still in their mouths,",
      "M": "But they had not turned from their craving; the food was still in their mouths",
      "T": "But they hadn't finished swallowing—\nthe food still in their mouths—\nwhen their craving was still alive in them."
    },
    "31": {
      "L": "when the wrath of God came upon them and slew the fattest of them, and struck down the chosen men of Israel.",
      "M": "when God's wrath came down on them and slew the strongest among them and struck down the young men of Israel.",
      "T": "God's wrath fell on them.\nHe killed the strongest ones—\nthe young men of Israel fell."
    },
    "32": {
      "L": "For all this they still sinned, and did not believe despite his wondrous works.",
      "M": "Despite all of this, they went on sinning and refused to believe even his miracles.",
      "T": "And yet—they kept sinning.\nAll his wonders, and still they would not believe."
    },
    "33": {
      "L": "Therefore he brought their days to an end in emptiness, and their years in sudden terror.",
      "M": "So he made their days dissolve into emptiness and their years end in sudden fright.",
      "T": "So their days vanished into nothing.\nTheir years ran out in sudden panic."
    },
    "34": {
      "L": "When he struck them down, they sought him; they turned back and inquired earnestly for God.",
      "M": "Whenever he struck them down, they would search for him; they would turn around and sincerely seek God.",
      "T": "Every time he struck them, they went looking for him.\nThey turned around and earnestly sought God."
    },
    "35": {
      "L": "They remembered that God was their rock, and the Most High God their redeemer.",
      "M": "They recalled that God was their rock, and the Most High God was their redeemer.",
      "T": "They would remember: God is their rock.\nThe Most High is the one who buys them back."
    },
    "36": {
      "L": "But they flattered him with their mouths; they lied to him with their tongues.",
      "M": "But they only said what he wanted to hear; they spoke to him with lying tongues.",
      "T": "But it was flattery.\nThey used the right words\nand meant none of them."
    },
    "37": {
      "L": "For their heart was not right with him; they were not faithful to his covenant.",
      "M": "Their hearts were not truly directed toward him; they were not faithful to his covenant.",
      "T": "Their hearts were somewhere else entirely.\nThey had no intention of keeping the covenant."
    },
    "38": {
      "L": "But he, being full of compassion, forgave their iniquity and did not destroy them; many times he turned his anger away and did not rouse all his wrath.",
      "M": "Yet he, being full of compassion, covered over their guilt and did not destroy them; again and again he turned back his anger and did not unleash all his fury.",
      "T": "But he—he was full of compassion.\nHe covered their guilt and did not destroy them.\nAgain and again he turned back his anger—\nhe would not let all his fury off the leash."
    },
    "39": {
      "L": "For he remembered that they were but flesh — a wind that passes away and does not return.",
      "M": "He remembered that they were only flesh — a passing wind that does not come back.",
      "T": "He remembered what they were:\nflesh.\nA breath that goes out and never comes back."
    },
    "40": {
      "L": "How often they rebelled against him in the wilderness and grieved him in the desert!",
      "M": "How many times they defied him in the wilderness and caused him grief in the wasteland!",
      "T": "How many times—\nhow many times they pushed against him in the wilderness,\nwounding him in the desert."
    },
    "41": {
      "L": "They turned back and tested God again, and pressed hard against the Holy One of Israel.",
      "M": "They kept turning back and testing God, pressing against the Holy One of Israel.",
      "T": "Over and over they tested God.\nThey kept pushing against the Holy One of Israel—\npressing the bruise."
    },
    "42": {
      "L": "They did not remember his hand, nor the day he redeemed them from the enemy,",
      "M": "They forgot what his hand had done, and the day he rescued them from their oppressor—",
      "T": "They forgot what his hand had done.\nThey forgot the day he set them free from the enemy—"
    },
    "43": {
      "L": "how he had performed his signs in Egypt, and his wonders in the fields of Zoan.",
      "M": "how he had displayed his miraculous signs in Egypt and his wonders in the region of Zoan.",
      "T": "all those signs he performed in Egypt,\nthose wonders in the fields of Zoan."
    },
    "44": {
      "L": "He turned their rivers into blood, so that they could not drink from their streams.",
      "M": "He turned their rivers into blood so that they were unable to drink from their streams.",
      "T": "He turned the river to blood.\nEvery stream—undrinkable."
    },
    "45": {
      "L": "He sent swarms of flies among them which devoured them, and frogs which devastated them.",
      "M": "He sent swarms of flies to devour them, and frogs that brought ruin upon them.",
      "T": "He sent clouds of flies that devoured them.\nHe sent frogs that swept through everything."
    },
    "46": {
      "L": "He gave their crops to the locust, and their produce to the caterpillar.",
      "M": "He handed their harvest over to the locust and their labor to the swarming caterpillar.",
      "T": "Everything they had grown—\nhe handed to the locust and the caterpillar."
    },
    "47": {
      "L": "He destroyed their vines with hail, and their sycamore trees with frost.",
      "M": "He struck their vines down with hail and their sycamore trees with killing frost.",
      "T": "Hail took the vines.\nFrost killed the sycamore trees."
    },
    "48": {
      "L": "He gave over their cattle to the hail, and their flocks to thunderbolts.",
      "M": "He surrendered their cattle to the hail and their flocks to lightning strikes.",
      "T": "He gave their cattle over to the hail—\ntheir flocks to the lightning."
    },
    "49": {
      "L": "He sent upon them the fury of his anger, wrath, indignation, and trouble — a band of destroying angels.",
      "M": "He unleashed his fierce anger upon them — his wrath, indignation, and distress — a company of destroying messengers.",
      "T": "He sent his burning anger like an army against them:\nwrath, fury, anguish—\na force of destroying angels."
    },
    "50": {
      "L": "He cleared a path for his anger; he did not spare their lives from death, but gave them over to the pestilence.",
      "M": "He made a clear way for his wrath; he did not withhold their lives from death, but surrendered them to the plague.",
      "T": "He cleared the road for his anger—\nnothing in the way.\nHe did not spare their very lives from death;\nhe handed them over to plague."
    },
    "51": {
      "L": "He struck down all the firstborn in Egypt, the first fruits of their strength in the tents of Ham.",
      "M": "He killed all the firstborn in Egypt, the prime of their strength in the dwellings of Ham.",
      "T": "He struck every firstborn in Egypt—\nthe best of their strength,\nin every home across the land of Ham."
    },
    "52": {
      "L": "But he brought his own people out like sheep, and guided them in the wilderness like a flock.",
      "M": "But he brought his own people out like sheep and led them through the wilderness like a flock.",
      "T": "But his own people he led out like sheep—\nguided them through the wilderness like a flock."
    },
    "53": {
      "L": "And he led them safely so that they did not fear; but the sea engulfed their enemies.",
      "M": "He guided them in safety so that they had nothing to fear; the sea swallowed their enemies.",
      "T": "He kept them safe—they had nothing to fear.\nBut the sea swallowed their enemies whole."
    },
    "54": {
      "L": "And he brought them to his holy border, to the mountain that his right hand had purchased.",
      "M": "He brought them to his sacred territory, to the mountain that his right hand had won.",
      "T": "He brought them to the edge of his holy land—\nthe mountain that his right hand had won for them."
    },
    "55": {
      "L": "He drove out the nations before them, allotted their land as a possession by line, and settled the tribes of Israel in their tents.",
      "M": "He expelled the nations from before them, assigned their land as an inheritance by lot, and made the tribes of Israel to dwell in their territory.",
      "T": "He cleared the nations out ahead of them,\ndivided the land and gave it to Israel,\nand settled each tribe in its place."
    },
    "56": {
      "L": "Yet they tested and provoked the Most High God, and did not keep his testimonies.",
      "M": "Nevertheless they tested and defied the Most High God and refused to keep his commandments.",
      "T": "And still they tested God.\nStill they provoked the Most High.\nStill they refused to keep what he had given them."
    },
    "57": {
      "L": "But they turned back and dealt unfaithfully like their fathers; they were turned aside like a deceitful bow.",
      "M": "They turned back and acted faithlessly, just as their ancestors had; they bent away like a defective bow.",
      "T": "They turned back.\nFaithless—just like their ancestors.\nThey bent away like a bow with a warped limb,\nflying wide of the mark."
    },
    "58": {
      "L": "For they provoked him to anger with their high places, and stirred his jealousy with their carved images.",
      "M": "They made him angry with their hilltop shrines and roused his jealousy with their carved idols.",
      "T": "Their high places made him angry.\nTheir carved idols stirred his jealousy to the root."
    },
    "59": {
      "L": "When God heard this, he was filled with wrath, and he greatly abhorred Israel.",
      "M": "When God heard all this, he was incensed; he thoroughly rejected Israel.",
      "T": "God heard it all.\nHe was furious.\nHe turned from Israel with revulsion."
    },
    "60": {
      "L": "So he abandoned the tabernacle at Shiloh, the tent he had set among men.",
      "M": "He abandoned the tabernacle at Shiloh, the tent he had established among his people.",
      "T": "He walked away from the tabernacle at Shiloh—\nthe tent he had pitched among them."
    },
    "61": {
      "L": "And he gave his strength into captivity, and his glory into the enemy's hand.",
      "M": "He allowed his strength to go into exile and his glory into enemy hands.",
      "T": "He gave his strength away to captivity.\nHis glory—into enemy hands."
    },
    "62": {
      "L": "He gave his people over also to the sword, and was wroth with his inheritance.",
      "M": "He surrendered his people to the sword and turned against his inheritance in anger.",
      "T": "He gave his own people to the sword.\nHe turned in fury against the people he called his own."
    },
    "63": {
      "L": "The fire consumed their young men, and their young women had no wedding song.",
      "M": "Fire devoured their young men, and their young women received no marriage praise.",
      "T": "Fire consumed the young men.\nThe young women—no wedding songs were sung for them."
    },
    "64": {
      "L": "Their priests fell by the sword, and their widows made no lamentation.",
      "M": "Their priests were cut down by the sword; their widows could not even weep.",
      "T": "Their priests fell by the sword.\nAnd their widows—too shattered even to weep."
    },
    "65": {
      "L": "Then the Lord awaked as from sleep, like a mighty man refreshed from wine.",
      "M": "Then the Lord awoke as if from sleep, like a warrior who rises vigorous from wine.",
      "T": "Then the Lord woke up—\nlike someone roused from sleep,\nlike a warrior who had drunk deep and now rose, ready."
    },
    "66": {
      "L": "And he struck his enemies in the hinder parts; he put them to everlasting shame.",
      "M": "He drove his enemies back and put them to shame that will not end.",
      "T": "He came at his enemies from behind\nand humiliated them—\na shame that will not lift."
    },
    "67": {
      "L": "Moreover he rejected the tent of Joseph, and chose not the tribe of Ephraim;",
      "M": "He refused the tent of Joseph and did not choose the tribe of Ephraim;",
      "T": "He passed over the tent of Joseph.\nEphraim—he did not choose that tribe."
    },
    "68": {
      "L": "but he chose the tribe of Judah — Mount Zion, which he loved.",
      "M": "Instead he chose the tribe of Judah — Mount Zion, which he loved.",
      "T": "He chose Judah instead.\nHe chose Mount Zion—the one he loved."
    },
    "69": {
      "L": "And he built his sanctuary like the high heavens, like the earth which he established forever.",
      "M": "He built his sanctuary like the heights of heaven, like the earth that he has set in place forever.",
      "T": "He built his sanctuary high—\nlike the heights of heaven,\nlike the earth he put in place to last forever."
    },
    "70": {
      "L": "He chose David also his servant, and took him from the sheepfolds.",
      "M": "He chose David his servant and took him from the sheep pens.",
      "T": "He chose David—his servant.\nHe took him from the sheepfolds."
    },
    "71": {
      "L": "From following the nursing ewes he brought him to shepherd Jacob his people, and Israel his inheritance.",
      "M": "From tending the nursing ewes he brought him to shepherd Jacob his people, and Israel his inheritance.",
      "T": "From behind nursing ewes he brought him\nto tend Jacob—his people—\nand Israel—his inheritance."
    },
    "72": {
      "L": "So he shepherded them according to the integrity of his heart; and guided them by the skillfulness of his hands.",
      "M": "He tended them with the integrity of his heart and guided them with the skill of his hands.",
      "T": "He shepherded them from an honest heart.\nHe guided them with hands that knew what they were doing."
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 77–78 written.')

if __name__ == '__main__':
    main()
