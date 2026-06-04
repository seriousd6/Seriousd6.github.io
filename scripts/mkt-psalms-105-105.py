"""
MKT Psalms chapter 105 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-105-105.py

=== Overview of this unit ===

Ps 105 (45 v) — Anonymous historical psalm; possibly paired editorially with Ps 106
    (which covers the same history from the angle of Israel's faithlessness). Ps 104
    closes and Ps 105 opens the same new doxological phase; the "Hallelujah!" that ends
    Ps 104 is answered by "Give thanks to the LORD" that opens Ps 105.

    The psalm is a unified meditation on divine covenant-faithfulness (b'rit, H1285)
    working itself out through Israel's entire early history. The structural verbs are
    zakar (H2142, "remember"): v8 "He has remembered his covenant forever"; v42 "he
    remembered his holy word." Everything between those two occurrences — patriarchs,
    Joseph, Egypt, Moses, plagues, exodus, land-gift — is the content of that remembered
    promise being enacted.

    STRUCTURE:
    vv1-6:   CALL TO PRAISE — international summons to give thanks, sing, declare, seek.
             The audience is addressed in v6 as "seed of Abraham / sons of Jacob" —
             placing the reader within the covenant community before the history begins.

    vv7-11:  THE ABRAHAMIC COVENANT — confirmed to Abraham (v9), sworn to Isaac (v9),
             made binding as statute to Jacob (v10), as everlasting covenant to Israel
             (v10): "To you I will give the land of Canaan." The covenant is rehearsed
             in its three-generation deepening.

    vv12-15: THE WANDERING FEW — when the ancestors were "almost no one," sojourning
             aliens moving from people to people, God tolerated no oppression of them
             and rebuked kings on their behalf (an allusion to Abimelech/Pharaoh in
             Genesis). They were few; they were strangers; they were untouchable.

    vv16-22: THE JOSEPH NARRATIVE — the theological centre of the patriarchal section.
             God sent Joseph (v17) — note the divine agency framing a human atrocity.
             The iron of v18 is the key image: feet in shackles, iron at his nefesh
             (his whole being). The "word of the LORD tested him" (v19): Joseph was
             being refined by the promise he had received. The king released and elevated
             him (vv20-22); Joseph became the providential mechanism for what follows.

    vv23-25: ISRAEL IN EGYPT / DIVINE REVERSAL — Israel comes to Egypt; God makes them
             fruitful (H6509, v24) and stronger than their enemies. Then the theological
             scandal of v25: "He turned their hearts to hate his people." God orchestrated
             even Egypt's hostility — the hostility that would make the exodus necessary
             and glorious. Providence is sovereign even over human evil.

    vv26-36: MOSES, AARON, AND THE PLAGUES — the psalm selects seven plagues in a
             non-Exodus order: (1) Darkness (v28), (2) Water to Blood (v29), (3) Frogs
             (v30), (4) Flies and Gnats (v31), (5) Hail and Fire (v32), (6) Locusts
             (vv34-35), (7) Death of the Firstborn (v36). Plagues omitted: cattle
             disease, boils. The order is not chronological but thematic/rhetorical —
             the psalm is not a history lesson but a praise poem. The darkness-first
             ordering may move from cosmic (darkness, the negation of light/creation)
             outward to the climactic death of the firstborn.

    vv37-41: THE EXODUS — "He brought them out with silver and gold" (v37); pillar of
             cloud and fire (v39); quail and manna (v40); water from the rock (v41).
             The exodus is recounted as pure gift: Israel left enriched, protected,
             provisioned. No Israelite complaint appears (contrast Ps 106).

    vv42-45: THE REMEMBERED PROMISE — the capstone. "He remembered his holy word to
             Abraham his servant" (v42). The entire history has been the outworking of
             that one promise. The land-gift (v44) was so that they would "keep his
             statutes and observe his laws" (v45). The psalm ends with imperative
             praise: "Praise the LORD!" / "Hallelujah!" (T).

    INTERTEXTUAL NOTE: vv1-15 appear almost verbatim in 1 Chr 16:8-22, where David
    brings the ark to Jerusalem. The psalm is liturgically embedded in Israel's
    worship from early in the monarchic period.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" (small-caps convention) in L/M/T throughout — consistent
    with all prior Psalms scripts. The divine personal name appears at vv1, 3, 4, 7,
    19 (implied), 45.

H430 (אֱלֹהִים, Elohim): "God" in all tiers. At v7 in compound "the LORD our God."

H1285 (בְּרִית, b'rit): "covenant" in all tiers at vv8 and 10. This is the structural
    term of the psalm; consistent with all prior scripts. At v10 the covenant is
    called both "statute" (H2706, choq) and "everlasting covenant" — the two
    terms reinforce each other: it has the binding force of law AND eternal duration.

H5315 (נֶפֶשׁ, nefesh): Two occurrences with different senses:
    - v18: "iron entered his nefesh" — the iron fetters hurt Joseph to his very being.
      Not the Greek immaterial soul, but the whole animated self. L: "iron entered
      into his soul" (literal rendering of the idiom); M: "iron chain was laid upon
      him" (clarifies physical reality); T: "the iron entered his very being" (the
      existential anguish of the image). The Septuagint reads "his soul came into
      iron" — same image, Greek idiom.
    - v22: "to bind his princes at his nefesh's pleasure" = at Joseph's will/desire.
      L: "at his pleasure"; M: "as he saw fit"; T: "as he wished" — the word here
      indicates subjective will/desire, not the self-in-bondage image of v18.

H2142 (זָכַר, zakar, remember): Perfect tense at v8 ("He has remembered"); perfect
    at v42 ("he remembered"). Both rendered with English perfect ("has remembered" /
    "remembered") to maintain the completed-act sense with ongoing implications.
    These are the two structural pillars of the psalm's theology.

H5769 (עוֹלָם, olam): "forever" (v8) and "everlasting" (v10) — standard rendering
    consistent with all prior scripts.

H5650 (עֶבֶד, servant): Appears at vv6 (Abraham), 17 (Joseph), 26 (Moses), 42
    (Abraham again). Rendered "servant" in all three tiers throughout. In the case
    of Joseph (v17), the same word describes his slave status in Egypt — the irony
    is intentional: the one whom God's purpose chose became literally a servant.

H6944 (קֹדֶשׁ, qodesh, holy): "holy name" at v3; "holy word/promise" at v42.
    Rendered "holy" in all tiers consistently.

H1984 (הָלַל) + H3050 (יָהּ, Yah) at v45: "Praise the LORD!" in L/M; "Hallelujah!"
    in T — consistent with the T-tier treatment at Ps 104:35 in the prior script.

H4784 (מָרָה, marah, rebel) at v28: "they did not rebel against his word" — the
    subject "they" most naturally refers to Moses and Aaron, who faithfully obeyed
    God's command even in the face of Pharaoh. Not Egypt refusing to rebel (which
    makes no sense in context) but the servants of God refusing to disobey. L/M/T
    all render accordingly.

=== Plague-order note ===

The psalm lists seven plagues in this order: darkness (v28), water to blood (v29),
frogs (v30), flies and gnats (v31), hail and fire (vv32-33), locusts (vv34-35),
death of firstborn (v36). This differs from Exodus order (blood, frogs, gnats, flies,
cattle, boils, hail, locusts, darkness, firstborn). The psalm omits cattle disease
and boils. The darkness-first order may reflect thematic or mnemonic structuring;
this is a praise poem, not a chronicle. The translation follows the psalm's order.

=== Aspect and tense notes ===

The psalm's dominant mode is Hebrew perfect aspect for divine acts: "He sent," "He
made," "He brought out," "He opened." These completed acts are recited to form the
basis for present praise. The jussive/imperative mood of vv1-6 and v45 frames the
historic narration as doxological: the history is recited in order to produce worship.

v19: "the word of the LORD tested him" — qatal (perfect): the entire period of
    Joseph's imprisonment was a test by the word. The word was both the promise
    (his dreams) and the agent of refinement.

v25: H2015 (turned) — "He turned their hearts" — the qatal form describes God's
    sovereign act. Divine passive of a sort, but here the agency is explicit.
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
  # Psalm 105 — God's Covenant Faithfulness Through Israel's History
  # ===========================================================================
  "105": {
    "1": {
      "L": "O give thanks to the LORD; call upon his name; make known his deeds among the peoples!",
      "M": "Give thanks to the LORD; call upon his name; make his deeds known among the nations!",
      "T": "Give thanks to the LORD!\nCall upon his name!\nTell the nations what he has done!"
    },
    "2": {
      "L": "Sing to him, sing praises to him; meditate on all his wondrous works!",
      "M": "Sing to him, sing praise to him; reflect on all his wonderful deeds!",
      "T": "Sing to him — praise him with song!\nDwell on all his wonders."
    },
    "3": {
      "L": "Glory in his holy name; let the hearts of those who seek the LORD rejoice!",
      "M": "Boast in his holy name; let the hearts of those who seek the LORD be glad!",
      "T": "Boast in his holy name!\nLet all who seek the LORD\nrejoice deep in their hearts!"
    },
    "4": {
      "L": "Seek the LORD and his strength; seek his face continually!",
      "M": "Seek the LORD and his power; seek his presence at all times!",
      "T": "Seek the LORD — seek his strength.\nSeek his face without ceasing."
    },
    "5": {
      "L": "Remember the wondrous works he has done, his marvels and the ordinances of his mouth,",
      "M": "Remember the wonderful things he has done — his signs and wonders, the judgments he has spoken —",
      "T": "Remember what he has done:\nhis wonders, his marvels,\nthe judgments that came from his mouth,"
    },
    "6": {
      "L": "O offspring of Abraham his servant, O sons of Jacob his chosen ones!",
      "M": "you descendants of Abraham his servant, you children of Jacob, his chosen people!",
      "T": "you who descend from Abraham his servant—\nchildren of Jacob, his chosen ones!"
    },
    "7": {
      "L": "He is the LORD our God; his judgments are in all the earth.",
      "M": "He is the LORD our God; his justice extends throughout all the earth.",
      "T": "He is the LORD our God.\nHis justice reaches to the ends of the earth."
    },
    "8": {
      "L": "He has remembered his covenant forever, the word he commanded to a thousand generations —",
      "M": "He keeps his covenant in memory forever, the promise he declared for a thousand generations —",
      "T": "He has remembered his covenant forever —\nthe word he proclaimed\nfor a thousand generations:"
    },
    "9": {
      "L": "the covenant which he made with Abraham, and his sworn oath to Isaac,",
      "M": "the covenant he made with Abraham and the oath he swore to Isaac,",
      "T": "the covenant he cut with Abraham,\nthe oath he swore to Isaac,"
    },
    "10": {
      "L": "which he confirmed to Jacob as a statute, to Israel as an everlasting covenant,",
      "M": "which he established as a binding decree for Jacob, an everlasting covenant for Israel,",
      "T": "which he made binding as law for Jacob—\nan everlasting covenant\nfor Israel."
    },
    "11": {
      "L": "saying, 'To you I will give the land of Canaan as the lot of your inheritance.'",
      "M": "He said, 'I will give you the land of Canaan as your inherited portion.'",
      "T": "'To you I will give the land of Canaan—\nyour allotted inheritance.'"
    },
    "12": {
      "L": "When they were but few in number, very few, and sojourners in it,",
      "M": "When they were just a handful of people — almost no one — living as foreigners there,",
      "T": "When they were barely a handful of people,\nwandering strangers\nin the land he had promised them,"
    },
    "13": {
      "L": "wandering from nation to nation, from one kingdom to another people,",
      "M": "moving from one nation to another, from one kingdom to the next,",
      "T": "moving from people to people,\nfrom one kingdom to another—"
    },
    "14": {
      "L": "he permitted no man to oppress them, and he rebuked kings on their account:",
      "M": "he allowed no one to oppress them; he rebuked kings for their sake:",
      "T": "God let no one oppress them.\nHe rebuked kings on their account:"
    },
    "15": {
      "L": "'Do not touch my anointed ones; do my prophets no harm!'",
      "M": "'Do not lay a hand on my anointed ones; do not harm my prophets!'",
      "T": "'Do not touch my anointed ones.\nDo not harm my prophets.'"
    },
    "16": {
      "L": "He called a famine upon the land; he broke every staff of bread.",
      "M": "Then he summoned a famine over the land and cut off every supply of food.",
      "T": "He called down famine on the land—\nbroke every staff of bread."
    },
    "17": {
      "L": "He sent a man before them — Joseph, who was sold as a servant.",
      "M": "He sent a man ahead of them — Joseph, who had been sold as a slave.",
      "T": "He sent a man ahead of them:\nJoseph — sold into slavery."
    },
    "18": {
      "L": "His feet they afflicted with fetters; iron entered into his soul.",
      "M": "They bound his feet with shackles and an iron chain was laid upon him.",
      "T": "They hurt his feet with chains.\nThe iron entered into his very being."
    },
    "19": {
      "L": "Until the time when his word came to pass, the word of the LORD tested him.",
      "M": "This lasted until what he had foretold came true — all the while the word of the LORD was testing him.",
      "T": "It continued — until the word came true.\nAll that time, the word of the LORD\nwas testing him, refining him."
    },
    "20": {
      "L": "The king sent and released him; the ruler of peoples let him go free.",
      "M": "The king sent word and freed him; the ruler of the peoples set him at liberty.",
      "T": "The king gave the order and freed him—\nthe ruler of nations\nset him at liberty."
    },
    "21": {
      "L": "He made him lord of his house and ruler over all his possessions,",
      "M": "He made him master of his household and ruler over everything he owned,",
      "T": "He made him master of the palace,\nruler over everything he owned—"
    },
    "22": {
      "L": "to bind his princes at his pleasure, and to teach his elders wisdom.",
      "M": "with authority to direct his princes as he saw fit and to instruct his elders in wisdom.",
      "T": "with power to direct the king's nobles as he wished\nand to teach wisdom\nto the men of the court."
    },
    "23": {
      "L": "Then Israel also came into Egypt, and Jacob sojourned in the land of Ham.",
      "M": "So Israel came down to Egypt, and Jacob took up residence in the land of Ham.",
      "T": "And then Israel came to Egypt—\nJacob living as a stranger\nin the land of Ham."
    },
    "24": {
      "L": "And he made his people very fruitful and made them stronger than their adversaries.",
      "M": "There God made his people extremely fruitful and stronger than those who opposed them.",
      "T": "There God made his people multiply beyond counting—\nstronger than all\nwho threatened them."
    },
    "25": {
      "L": "He turned their hearts to hate his people, to deal craftily with his servants.",
      "M": "He turned the Egyptians' hearts to hate his people and to scheme treacherously against his servants.",
      "T": "He turned Egypt's heart to hate his people—\nbrought them to plot\nagainst his servants."
    },
    "26": {
      "L": "He sent Moses his servant, and Aaron whom he had chosen.",
      "M": "He sent Moses, his servant, and Aaron, the man he had chosen.",
      "T": "He sent Moses — his servant —\nand Aaron, the one he had chosen."
    },
    "27": {
      "L": "They performed his signs among them and worked wonders in the land of Ham.",
      "M": "They carried out his signs among the Egyptians and performed wonders in the land of Ham.",
      "T": "They performed his signs throughout Egypt—\nwonders in the land of Ham."
    },
    "28": {
      "L": "He sent darkness and made it dark; they did not rebel against his word.",
      "M": "He sent darkness and plunged the land into blackness; Moses and Aaron did not defy his command.",
      "T": "He sent darkness—\nplunged the land into night.\nAnd they did not defy his word."
    },
    "29": {
      "L": "He turned their waters to blood and caused their fish to die.",
      "M": "He turned their waters to blood and killed all their fish.",
      "T": "He turned their waters to blood\nand killed every fish in them."
    },
    "30": {
      "L": "Their land swarmed with frogs, even in the chambers of their kings.",
      "M": "Frogs overran their land — even the private rooms of their kings.",
      "T": "Frogs swarmed through the land—\neven into the bedchambers\nof their kings."
    },
    "31": {
      "L": "He spoke and there came swarms of flies and gnats throughout all their territory.",
      "M": "He spoke and flies and gnats swarmed across all their territory.",
      "T": "He spoke—\nand flies and biting gnats swarmed\nthrough every region."
    },
    "32": {
      "L": "He gave them hail for rain, and flaming fire throughout their land.",
      "M": "He gave them hail instead of rain, and flashing fire across their land.",
      "T": "He turned their rain to hail—\nand sent blazing fire\nflashing through their land."
    },
    "33": {
      "L": "He struck their vines and their fig trees and shattered the trees throughout their territory.",
      "M": "He struck down their vines and fig trees and splintered all the trees in their land.",
      "T": "He struck their vines — their fig trees —\nand shattered every tree\nthroughout the land."
    },
    "34": {
      "L": "He spoke and the locusts came, and young locusts without number,",
      "M": "He spoke and locusts arrived — grasshoppers beyond all counting —",
      "T": "He spoke—\nand the locusts came in,\ncaterpillars beyond all counting—"
    },
    "35": {
      "L": "and devoured all the vegetation in their land and ate up the fruit of their ground.",
      "M": "eating up every plant in their land and consuming all the fruit of their soil.",
      "T": "devouring every green thing in the land,\nstripping all the fruit\nfrom every field."
    },
    "36": {
      "L": "He struck all the firstborn in their land, the firstfruits of all their strength.",
      "M": "He struck down every firstborn in their land, the firstfruits of all their vigor.",
      "T": "He struck down every firstborn in their land—\nthe best and first\nof all their strength."
    },
    "37": {
      "L": "Then he brought them out with silver and gold, and none among his tribes was feeble.",
      "M": "He brought his people out loaded with silver and gold; not one person in all their tribes was weak.",
      "T": "He brought them out — carrying silver and gold.\nNot one among all their tribes\nstumbled or fell."
    },
    "38": {
      "L": "Egypt was glad when they departed, for the fear of them had fallen upon it.",
      "M": "Egypt was relieved when they left, for the dread of Israel had settled over them.",
      "T": "Egypt was glad to see them go—\nthe dread of this people\nhad overwhelmed them."
    },
    "39": {
      "L": "He spread a cloud for a covering, and fire to give light in the night.",
      "M": "He spread out a cloud as a shelter and gave fire to light the way through the night.",
      "T": "He spread out a cloud over them for shelter—\nand fire to light the darkness\nthrough the night."
    },
    "40": {
      "L": "They asked, and he brought quail, and satisfied them with the bread of heaven.",
      "M": "They asked for food and he brought them quail, satisfying them with bread from heaven.",
      "T": "They asked — he brought quail.\nHe satisfied them\nwith bread from heaven."
    },
    "41": {
      "L": "He opened the rock and waters gushed out; they ran through the desert like a river.",
      "M": "He split open the rock and water poured out; it flowed like a river through the wilderness.",
      "T": "He split open the rock—\nwater gushed out\nand ran like a river through the desert."
    },
    "42": {
      "L": "For he remembered his holy word to Abraham his servant.",
      "M": "For he had called to mind his holy promise to Abraham his servant.",
      "T": "All of this — because he remembered\nhis holy promise\nto Abraham his servant."
    },
    "43": {
      "L": "So he brought out his people with joy, and his chosen ones with singing.",
      "M": "And so he led his people out with rejoicing, his chosen ones with shouts of joy.",
      "T": "He brought his people out — with joy,\nhis chosen ones —\nwith singing."
    },
    "44": {
      "L": "And he gave them the lands of the nations, and they took possession of the labor of the peoples,",
      "M": "He gave them the lands of other nations, and they took possession of what others had worked for,",
      "T": "He gave them the lands of the nations—\nthey inherited what others\nhad spent their lives building—"
    },
    "45": {
      "L": "that they might keep his statutes and observe his laws. Praise the LORD!",
      "M": "so that they would keep his decrees and obey his teachings. Praise the LORD!",
      "T": "all so that they might keep his statutes\nand live by his laws.\nHallelujah!"
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 105 written.')

if __name__ == '__main__':
    main()
