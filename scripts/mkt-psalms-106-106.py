"""
MKT Psalms chapter 106 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-106-106.py

=== Overview ===

Ps 106 (48 v) — Anonymous. The closing psalm of Book IV (Psalms 90–106). A
    penitential-historical psalm: it recites Israel's successive failures from
    Egypt through the wilderness to the settlement, acknowledging each as
    rebellion against a God who repeatedly chose mercy over judgment. The psalm
    frames Israel's entire history as a cycle — sin, consequence, cry, deliverance,
    forgetting, sin again — and locates the reader in that cycle even now.

    Structure:
      vv1-3:   Opening doxology (Hallelujah + thanksgiving formula) + beatitude
      vv4-5:   Personal petition: psalmist asks to share in God's saving favor
      v6:      Corporate confession ("We have sinned with our fathers")
      vv7-12:  Episode 1 — Egypt / Red Sea (rebellion before the crossing; yet God saved)
      vv13-15: Episode 2 — Wilderness craving (Numbers 11; desire for meat)
      vv16-18: Episode 3 — Korah's rebellion (Numbers 16; envy of Moses and Aaron)
      vv19-23: Episode 4 — Golden Calf at Horeb (Exod 32; Moses as intercessor)
      vv24-27: Episode 5 — Kadesh-barnea / despising the land (Numbers 13-14)
      vv28-31: Episode 6 — Baal-Peor (Numbers 25; Phinehas; zeal credited as righteousness)
      vv32-33: Episode 7 — Meribah (Numbers 20; Moses's embittered spirit)
      vv34-39: Episode 8 — Canaanite assimilation (idolatry, child sacrifice)
      vv40-43: Judgment cycle: God's anger, enemy domination, repeated deliverance
      vv44-46: Pivot: God sees, hears, and remembers covenant + chesed
      v47:     Communal petition for gathering from exile (may reflect exilic revision)
      v48:     Book IV doxology (compare 41:13; 72:18-19; 89:52) + Hallelujah

    This psalm opens and closes with הַלְלוּ-יָהּ (Hallelujah). The doxology at
    v48 is not part of the original psalm but the editorial close of Book IV;
    the Hallelujah at v1 is the psalm's own opening (matching the editorial close
    of Ps 105:45 and the opening of Ps 107:1). It is the dark counterpart to the
    celebratory Ps 105: where 105 recounts what God did for Israel, 106 confesses
    what Israel did against God. Together they form an honest pair.

    Theological high points:
    - v8: God saves "for his name's sake" — grace grounded in his own character,
          not Israel's merit (echoes Ezek 20:9,14,22; Ps 23:3; Isa 48:9).
    - v23: Moses stands "in the breach" — the most vivid intercession image in
          the Psalter. The intercessor plants himself between God's wrath and the
          guilty people. A type of the greater Mediator.
    - v31: Phinehas's act "counted to him as righteousness" — the same vocabulary
          as Gen 15:6 (Abraham's faith). In both cases an act of covenant loyalty
          is reckoned as righteousness. The echo is deliberate.
    - v45: God "relented" (H5162 nacham) — divine pathos; not moral repentance
          but a change of intended action arising from the abundance of chesed.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M/T. Consistent with all prior Psalms scripts.
    The divine personal name appears at vv1,2,4,7,8,16,24,25,34,40,47 — it is
    the grammatical subject of every saving act.

H2617 (חֶסֶד, chesed):
    - v1: singular — "steadfast love" (L/M/T). Standard opening formula.
    - v7: plural form (חֲסָדִים, chasdim) — "steadfast love" (L), "great steadfast
          love" (M), "boundless steadfast love" (T). The plural intensifies; it
          denotes repeated acts of covenant faithfulness accumulated over time.
    - v45: "steadfast love" (L/M/T). The climax of the psalm's pivot — the
          abundance of chesed is what moves God to relent.
    Not rendered "mercy" or "kindness" — chesed carries the full weight of
    covenant-committed love, which no single English word captures.

H5315 (נֶפֶשׁ, nephesh) at v15: "them" (L/M/T). Here nephesh functions as a
    reflexive marker for the person's vital life / bodily self, not a separable
    soul. "He sent leanness into their souls" (KJV) is misleading; the meaning
    is "a wasting sickness into their bodies / into them." Rendered "into their
    bodies" in M and "a wasting disease within them" in T.

H7307 (רוּחַ, ruach) at v33: "spirit" — but whose spirit? The pronoun "his" in
    "they provoked his spirit" refers to Moses (subject of v32). They embittered
    Moses's spirit through their repeated provocation, and as a result he spoke
    rashly (Num 20:10-11). This is not the divine Spirit but the human spirit of
    Moses driven to the breaking point by the people's relentless rebellion.
    Rendered "his spirit" (L), "Moses's spirit" (M), "his spirit" in T (context
    makes Moses the referent clear from v32 transition).

H6666 (צְדָקָה, tsedaqah):
    - v3: "righteousness" in L/M/T. The beatitude honours those who do
          righteousness at all times, not just in moments of religious observance.
    - v31: "righteousness" in L/M/T. Phinehas's zealous act of covenant defense
          was "counted to him as righteousness" — same vocabulary as Gen 15:6
          (H2803 chashav + tsedaqah). The echo is intentional.

H4941 (מִשְׁפָּט, mishpat) at v3: "justice" in L/M/T. Paired with tsedaqah —
    the two terms together cover both the relational (righteousness) and the
    executive (justice) dimensions of covenant obedience.

H1285 (בְּרִית, berit) at v45: "covenant" in L/M/T. The covenant is the
    theological anchor of the psalm's pivot: even after all the rebellion,
    God's covenant commitment holds. Consistent with all prior scripts.

H5162 (נָחַם, nacham) at v45: "relented" in L/M/T. Not "repented" (implies
    moral fault) but a change of intended action. God had sworn to destroy them;
    the abundance of his chesed moved him to reverse course. The word captures
    genuine divine responsiveness to human suffering and prayer.

H1984 (הָלַל) + H3050 (יָהּ, Yah) at vv1, 48: "Praise the LORD!" in L/M;
    "Hallelujah!" in T. Consistent with Ps 104:35, 105:45 conventions in
    all prior Psalms scripts for this project.

H2526 (חָם, Ham) at v22: "Ham" retained as proper name. The "land of Ham" is
    a poetic name for Egypt (cf. Ps 105:23,27; 78:51), derived from the descent
    of Egypt's ancestor in Gen 10:6. Renders explicit the deep OT genealogical
    connection. Not paraphrased as "Egypt" in L — kept as "Ham" and glossed
    in M/T.

H7700 (שֵׁד, shed) at v37: "demons" in L/M/T. The Canaanite child-sacrifice
    recipients are identified not as gods but as sheds — demonic powers (Deut
    32:17). Paul echoes this in 1 Cor 10:20 ("what pagans sacrifice they offer
    to demons"). Not softened to "idols" — the psalm's polemic is pointed.

H5556 (סָמַד / H6775 צָמַד, tsamad) at v28: "yoked themselves" (L/M) /
    "bound themselves" (T). The verb means to be attached or coupled — often
    used for idolatrous joining (cf. Num 25:3). Conveys the totality of
    the apostasy: they did not merely visit Baal-Peor, they attached themselves
    to him.

=== Textual and interpretive notes ===

v7: The MT has two occurrences of H3220 (yam, "sea") — "at the sea, at the
    Red Sea." This is emphatic doubling (the Reed Sea / Red Sea = Yam Suph).
    Retained in L as "at the sea, at the Red Sea"; condensed to "at the Red Sea"
    in M/T for natural English.

v20: "their glory" — the "glory" (kavod, H3519) that they exchanged is
    commonly understood as referring to God, who was Israel's glory. Paul
    draws on this verse in Romans 1:23. The irony is devastating: they replaced
    infinite glory with the image of a grass-eating animal.

v23: "stood in the breach" (H6556 perets) — the image is of a city wall that
    has been breached; a defender who stands in the gap between the enemy's
    sword and the city's people. Moses literally placed himself in the space
    between God's wrath and Israel. This verse is a key OT text for NT
    intercession theology.

v28: "sacrifices of the dead" — may refer to (1) sacrifices offered to lifeless
    gods, i.e., gods who are themselves dead; or (2) mortuary sacrifices, meals
    eaten in rituals for the dead at Peor. The exact practice is uncertain;
    the psalm condemns the association with death and the demonic either way.

v33: Moses's sin at Meribah (Num 20:1-13) is attributed here to the people's
    provocation, not to Moses's character failing. The people drove him to
    exhaustion. This is a remarkable instance of the psalmist's sympathy for
    Moses and his indictment of the people's persistent wearing-down of a leader.

v47: The petition "gather us from among the nations" implies a context of
    diaspora or at least the lived memory of it. Many scholars see this verse
    as added (or the whole psalm composed) in an exilic or post-exilic setting,
    when Psalm 106's historical review served as communal penitential prayer for
    those scattered. It may also be eschatological/anticipatory in an earlier
    context.

v48: The doxology closes Book IV (Psalms 90–106). The same formula occurs at
    Ps 41:13 (close of Book I), 72:18-19 (close of Book II), and 89:52
    (close of Book III). Verse 48b ("and let all the people say, Amen!") is a
    liturgical rubric — it calls the congregation to respond. Hallelujah at the
    end mirrors v1; the whole psalm — darkness and all — is framed by praise.

=== Aspect and tense notes ===

Psalm 106 uses the perfect tense throughout the historical narrative (vv7-39)
to describe completed past acts. The pattern of rebellion and rescue is
narrated as settled history. The jussives at vv47-48 ("Save us," "let all
the people say") shift to petition and volitive, anchoring the poem in an
ongoing present need. God's "remembering" at v45 is a perfect — a completed
act of recalling the covenant — while the "relenting" is also perfect: God
did relent. The opening beatitude (v3) uses a participle + imperfect to
denote habitual, ongoing action: those who keep justice, who do righteousness
always — not a past act but a present characteristic.
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
  # Psalm 106 — Penitential-Historical Psalm: Sin, Grace, and the Covenant Cycle
  # ===========================================================================
  "106": {
    "1": {
      "L": "Hallelujah! Give thanks to the LORD, for he is good; for his steadfast love endures forever!",
      "M": "Praise the LORD! Give thanks to the LORD, for he is good; his steadfast love endures forever!",
      "T": "Hallelujah!\nGive thanks to the LORD — he is good.\nHis steadfast love endures forever."
    },
    "2": {
      "L": "Who can utter the mighty acts of the LORD, or declare all his praise?",
      "M": "Who is able to speak all the LORD's mighty deeds, or make known all his praise?",
      "T": "Who could possibly tell all the LORD's mighty acts?\nWho could give voice\nto even a fraction of his praise?"
    },
    "3": {
      "L": "Blessed are those who keep justice, who do righteousness at all times!",
      "M": "Blessed are those who uphold justice and do what is right at every moment!",
      "T": "Blessed are those who practice justice,\nwho do what is right —\nnot sometimes, but always."
    },
    "4": {
      "L": "Remember me, O LORD, with the favor you show your people; visit me with your salvation,",
      "M": "Remember me, O LORD, when you show favor to your people; come to me with your saving help,",
      "T": "Remember me, LORD,\nwhen you show favor to your people.\nCome to me with your saving help —"
    },
    "5": {
      "L": "that I may look upon the prosperity of your chosen ones, that I may rejoice in the gladness of your nation, that I may glory with your inheritance.",
      "M": "so that I may see the well-being of your chosen ones, share the joy of your nation, and exult with your own inheritance.",
      "T": "so I may see the good you pour on your chosen,\nso I may rejoice with your whole nation —\nand join in the praise that belongs to your inheritance."
    },
    "6": {
      "L": "We have sinned, along with our fathers; we have committed iniquity; we have acted wickedly.",
      "M": "We have sinned, just as our fathers did; we have committed iniquity and acted wickedly.",
      "T": "We have sinned — as our fathers sinned.\nWe have twisted what was straight.\nWe have done what is wicked."
    },
    "7": {
      "L": "Our fathers, when they were in Egypt, did not consider your wondrous works; they did not remember the multitude of your steadfast love; but they rebelled at the sea, at the Red Sea.",
      "M": "When our fathers were in Egypt they took no account of your wonders; they did not remember your great steadfast love, and they rebelled at the sea — at the Red Sea.",
      "T": "Our fathers in Egypt — they did not take it in.\nYour wonders unfolded before them\nand they did not think.\nThey forgot the boundless steadfast love you had shown.\nAnd then, at the very shore of the Red Sea,\nthey rebelled."
    },
    "8": {
      "L": "Yet he saved them for the sake of his name, to make known his mighty power.",
      "M": "But he saved them for the sake of his own name, to demonstrate his mighty power.",
      "T": "And still — he saved them.\nNot for their sake. For his name's sake.\nSo his mighty power would be known in all the earth."
    },
    "9": {
      "L": "He rebuked the Red Sea, and it dried up; he led them through the deep as through a desert.",
      "M": "He rebuked the Red Sea, and it dried up; he led them through the depths as if through a dry wasteland.",
      "T": "He rebuked the Red Sea —\nit dried up.\nHe led them through the deep\nas though it were a desert road."
    },
    "10": {
      "L": "So he saved them from the hand of him who hated them and redeemed them from the hand of the enemy.",
      "M": "He rescued them from those who hated them and redeemed them from the power of their enemy.",
      "T": "He rescued them from the hand of those who hated them.\nHe bought them back\nfrom the grip of the enemy."
    },
    "11": {
      "L": "The waters covered their adversaries; not one of them was left.",
      "M": "The waters swept over their adversaries; not a single one remained.",
      "T": "The waters closed over their pursuers.\nNot one was left."
    },
    "12": {
      "L": "Then they believed his words; they sang his praise.",
      "M": "Then they trusted his word and broke into songs of praise.",
      "T": "Then — they believed.\nAnd they sang his praise."
    },
    "13": {
      "L": "But they soon forgot his works; they did not wait for his counsel.",
      "M": "But they quickly forgot what he had done; they did not wait for his guidance.",
      "T": "It did not last.\nThey forgot — quickly.\nThey could not wait for him to guide them."
    },
    "14": {
      "L": "They craved intensely in the wilderness and tested God in the desert.",
      "M": "They gave way to intense craving in the wilderness and put God to the test in the desert.",
      "T": "In the wilderness, craving seized them —\nan appetite that consumed them.\nThey put God to the test."
    },
    "15": {
      "L": "He gave them what they asked, but sent leanness into their bodies.",
      "M": "He gave them exactly what they wanted, but sent a wasting sickness into their bodies.",
      "T": "He gave them what they demanded.\nAnd with it he sent a wasting disease\ninto their bodies."
    },
    "16": {
      "L": "When men in the camp were jealous of Moses and of Aaron, the holy one of the LORD,",
      "M": "When jealousy of Moses broke out in the camp — and of Aaron, the LORD's holy one —",
      "T": "Then envy spread through the camp —\nagainst Moses,\nagainst Aaron, the LORD's own holy one."
    },
    "17": {
      "L": "the earth opened and swallowed up Dathan and covered the company of Abiram.",
      "M": "the earth split open and swallowed Dathan, and closed over the company of Abiram.",
      "T": "The earth opened its mouth\nand swallowed Dathan.\nIt buried the company of Abiram."
    },
    "18": {
      "L": "Fire also broke out against their company; a flame burned up the wicked.",
      "M": "Fire blazed through their party; flame consumed the wicked.",
      "T": "Fire broke out among them.\nFlame devoured the wicked."
    },
    "19": {
      "L": "They made a calf in Horeb and worshipped a cast image.",
      "M": "At Horeb they made a calf and bowed down to a metal idol.",
      "T": "At Horeb they cast a calf\nand bowed themselves down before a molten image."
    },
    "20": {
      "L": "They exchanged their glory for the likeness of an ox that eats grass.",
      "M": "They traded the glory of God for the image of a grass-eating ox.",
      "T": "They swapped the glory of God —\ntheir own God, their glory —\nfor the image of a bull that eats grass."
    },
    "21": {
      "L": "They forgot God their Savior, who had done great things in Egypt,",
      "M": "They forgot God, their Savior, who had done those great deeds in Egypt —",
      "T": "They forgot God — their Savior —\nthe one who had done\nthose great acts in Egypt:"
    },
    "22": {
      "L": "wondrous works in the land of Ham and awesome deeds by the Red Sea.",
      "M": "marvels in the land of Ham and fearsome acts at the Red Sea.",
      "T": "Wonders worked in the land of Ham.\nTerrible acts at the Red Sea."
    },
    "23": {
      "L": "Therefore he said he would destroy them — had not Moses, his chosen one, stood in the breach before him to turn his wrath from destroying them.",
      "M": "So he declared he would destroy them — but Moses, his chosen one, stood in the gap before him and turned his anger away from destroying them.",
      "T": "He would have destroyed them —\nbut Moses, his chosen servant, stood in the breach.\nHe planted himself between the wrath of God and the people\nand turned the destruction aside."
    },
    "24": {
      "L": "They despised the pleasant land; they did not believe his word.",
      "M": "Then they scorned the desirable land and refused to trust what he had promised.",
      "T": "Then they despised the land he had promised them —\nthe good and desired land.\nThey did not believe a word of it."
    },
    "25": {
      "L": "They murmured in their tents and did not listen to the voice of the LORD.",
      "M": "They grumbled in their tents and refused to listen to the LORD's voice.",
      "T": "They sat in their tents and grumbled.\nThey would not hear\nthe voice of the LORD."
    },
    "26": {
      "L": "Therefore he raised his hand and swore to them that he would make them fall in the wilderness,",
      "M": "So he swore with uplifted hand that he would strike them down in the wilderness,",
      "T": "So he raised his hand in solemn oath against them:\nthey would fall in the wilderness —"
    },
    "27": {
      "L": "and would scatter their offspring among the nations, dispersing them through the lands.",
      "M": "and would scatter their descendants among the nations, spreading them across distant lands.",
      "T": "their children scattered among the nations,\ndispersed across the ends of the earth."
    },
    "28": {
      "L": "Then they yoked themselves to Baal of Peor and ate sacrifices offered to the dead.",
      "M": "Then they attached themselves to Baal of Peor and partook of sacrifices offered to lifeless gods.",
      "T": "Then they bound themselves to Baal of Peor,\neating food offered up to the dead —\nfellow worshippers of gods who were no gods."
    },
    "29": {
      "L": "They provoked the LORD to anger with their deeds, and a plague broke out among them.",
      "M": "They stirred up the LORD's anger by what they were doing, and a plague broke out in their midst.",
      "T": "They provoked him with everything they did.\nA plague broke loose among them."
    },
    "30": {
      "L": "Then Phinehas stood up and intervened, and the plague was stayed.",
      "M": "Then Phinehas stepped forward and executed judgment, and the plague was stopped.",
      "T": "Then Phinehas stepped forward.\nHe acted.\nAnd the plague was stopped."
    },
    "31": {
      "L": "And that was counted to him as righteousness, from generation to generation forever.",
      "M": "And it was reckoned to him as righteousness for all generations, forever.",
      "T": "And this was credited to him as righteousness —\nreckoned and recorded,\nfor every generation, forever."
    },
    "32": {
      "L": "They angered him at the waters of Meribah, and it went ill with Moses on their account,",
      "M": "They angered the LORD at the waters of Meribah, and because of them it went badly for Moses —",
      "T": "At Meribah they provoked the LORD again.\nAnd Moses suffered for it,\nbecause of them."
    },
    "33": {
      "L": "for they made his spirit bitter, so that he spoke rashly with his lips.",
      "M": "for they had embittered Moses's spirit, and he spoke rashly with his mouth.",
      "T": "They had worn down his spirit —\nbitter and exhausted.\nAnd so Moses spoke words\nhe should never have spoken."
    },
    "34": {
      "L": "They did not destroy the peoples, as the LORD commanded them,",
      "M": "They did not drive out the peoples, as the LORD had commanded them.",
      "T": "They did not drive out the peoples of the land —\nthough the LORD had commanded it."
    },
    "35": {
      "L": "but they mingled with the nations and learned to do as they did.",
      "M": "Instead they mixed in with the nations and picked up their practices.",
      "T": "Instead they blended in with the nations around them\nand took up their ways."
    },
    "36": {
      "L": "They served their idols, which became a snare to them.",
      "M": "They served the idols of those peoples, and they became a trap for them.",
      "T": "They served their idols.\nAnd the idols became a snare\nthat caught them fast."
    },
    "37": {
      "L": "They sacrificed their sons and their daughters to demons,",
      "M": "They sacrificed their sons and their daughters to demonic powers —",
      "T": "They sacrificed their own sons and daughters\nto demons."
    },
    "38": {
      "L": "and shed innocent blood, the blood of their sons and daughters, sacrificed to the idols of Canaan; and the land was polluted with blood.",
      "M": "they poured out the innocent blood of their sons and daughters, offering them to the idols of Canaan; the land was defiled by their bloodshed.",
      "T": "Innocent blood — the blood of their own children —\npoured out to the idols of Canaan.\nThe land itself became polluted\nwith what they had done."
    },
    "39": {
      "L": "Thus they became unclean by their deeds and went whoring in their works.",
      "M": "They defiled themselves by all they did and played the harlot in their ways.",
      "T": "They defiled themselves with every act.\nThey went whoring after other gods —\nbetraying the one who had loved them."
    },
    "40": {
      "L": "Then the anger of the LORD burned hot against his people, and he abhorred his inheritance.",
      "M": "Then the LORD's anger blazed against his own people; he came to loathe his own inheritance.",
      "T": "The LORD's anger burned against his people.\nHe came to loathe\nhis own inheritance."
    },
    "41": {
      "L": "He gave them into the hand of the nations, so that those who hated them ruled over them.",
      "M": "He handed them over to the nations, and people who hated them came to rule over them.",
      "T": "He handed them over to the nations.\nPeople who hated them\ngot to rule over them."
    },
    "42": {
      "L": "Their enemies oppressed them, and they were brought low under their hand.",
      "M": "Their enemies crushed them, and they were ground down under their power.",
      "T": "Their enemies crushed them.\nThey were worn down and brought low\nunder the hand of those who despised them."
    },
    "43": {
      "L": "Many times he delivered them, but they were rebellious in their counsel and were brought low by their iniquity.",
      "M": "He rescued them again and again, but they kept resisting his purposes and were laid low by their own sin.",
      "T": "Again and again he delivered them.\nBut again and again they rebelled,\nfollowing their own stubborn plans —\nand were brought down by their own iniquity."
    },
    "44": {
      "L": "Nevertheless he regarded their distress when he heard their cry.",
      "M": "Still, he took notice of their affliction and listened when they cried out.",
      "T": "And still — he saw their suffering.\nHe heard their cry."
    },
    "45": {
      "L": "For their sake he remembered his covenant and relented according to the abundance of his steadfast love.",
      "M": "For their sake he called his covenant to mind and relented, moved by the greatness of his steadfast love.",
      "T": "He remembered his covenant on their behalf.\nThe sheer abundance of his steadfast love\nmoved him to relent."
    },
    "46": {
      "L": "He caused them to be pitied by all who held them captive.",
      "M": "He made all those who had taken them captive treat them with compassion.",
      "T": "He even turned the hearts of their captors —\ncausing them to show compassion\nto those they held."
    },
    "47": {
      "L": "Save us, O LORD our God, and gather us from among the nations, to give thanks to your holy name and to glory in your praise.",
      "M": "Save us, O LORD our God, and bring us back from among the nations, that we may give thanks to your holy name and take pride in your praise.",
      "T": "Save us, O LORD our God.\nGather us home from among the nations —\nso we may give thanks to your holy name\nand glory in the praise that is yours alone."
    },
    "48": {
      "L": "Blessed be the LORD, the God of Israel, from everlasting to everlasting! And let all the people say, 'Amen!' Praise the LORD!",
      "M": "Blessed be the LORD, the God of Israel, from age to age! And let all the people say, 'Amen!' Praise the LORD!",
      "T": "Blessed be the LORD, the God of Israel —\nfrom age to age, without end!\nLet all the people say: Amen!\nHallelujah!"
    }
  }

}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 106 written.')

if __name__ == '__main__':
    main()
