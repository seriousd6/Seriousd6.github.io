"""
MKT Psalms chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-psalms-19-24.py

=== Overview of this unit ===

Ps 19 — The Double Revelation (14 verses): Celebrates God's self-disclosure in creation
         (vv1–6) and in the Torah (vv7–11), closing with a personal prayer (vv12–14).
         The cosmological section is wordless testimony — the heavens speak without speech.
         Romans 10:18 quotes v4 (LXX φθόγγος = "sound/voice"). The Torah section uses
         five distinct synonyms for God's instruction (torah, edah, piqqudim, mitsvah,
         mishpat), each with its own quality predicate.

Ps 20 — Royal Intercession (9 verses): A liturgical prayer for the king before battle.
         The congregation speaks in vv1–5; a priest or prophet responds in v6 with "Now
         I know." Structure: petition (1–5) → confidence (6) → contrast (7–8) → petition (9).

Ps 21 — Royal Thanksgiving (13 verses): Companion to Ps 20; a celebration after victory.
         The king's trust (v7) is the theological hinge. Vv8–12 pivot to address the
         enemies in second person — a vision of their ultimate defeat.

Ps 22 — The Forsaken and Vindicated Sufferer (31 verses): The most extensive individual
         lament in the Psalter. Jesus quotes v1 from the cross (Matt 27:46; Mark 15:34).
         The psalm moves from desolation (1–21a) to confident praise (21b–31) — the turn
         at v21b "you have answered me!" is the psalm's dramatic centre. The worldwide
         scope of vv27–31 (all nations, all generations) transforms personal agony into
         cosmic proclamation.

Ps 23 — The Shepherd Psalm (6 verses): Pastoral imagery (vv1–4) gives way to the royal
         banquet image (v5). The LORD as shepherd echoes Ezek 34 and the NT (John 10).
         H2617 (hesed) in v6 is the covenant backbone of the whole psalm.

Ps 24 — The King of Glory (10 verses): A processional psalm for the ark entering
         Jerusalem. The theological claim of v1 (the whole earth belongs to the LORD)
         grounds the ethical demand of vv3–4 and the triumphant entry of vv7–10.
         The LORD of Hosts (tseva'ot) is the climactic title.

=== Superscriptions ===

As in PSA-1 (mkt-psalms-1-6.py), superscription text is merged into v1 of each psalm,
following English verse numbering (not MT's extra verse for the superscription). Psalms
that have superscriptions in the interlinear v1 embed them there.

=== Contested-term decisions ===

H3068 (יהוה, YHWH): "LORD" in L/M throughout, maintaining PSA-1 small-caps convention.
      In T tier: "the LORD" — liturgical voice of the Psalter is preserved; no switch
      to "Yahweh."

H430  (אֱלֹהִים, Elohim): "God" in all tiers. Standard.

H410  (אֵל, El, Ps 19:1; Ps 22 throughout): "God" in L/M. In Ps 22 vv1–2 "My God"
      (אֵלִי, eli) is the personal, direct address — the cry of dereliction. The
      intimacy of El over Elohim is preserved in all tiers ("my God" not "O God"). El
      is grammatically singular and more personal than the plural Elohim.

H2617 (חֶסֶד, hesed, Ps 23:6): "Steadfast love" in all tiers — MKT standard. "Mercy"
      (KJV) is avoided because it drops the covenant-loyalty dimension.

H5315 (נֶפֶשׁ, nefesh): "Soul" in L/M. In T tier: "inner life" (Ps 19:7), "whole self"
      or "life" (Ps 22:20) — the embodied self, not a Greek immaterial soul.

H8451 (תּוֹרָה, torah, Ps 19:7): "instruction" in L, M, and T. "Law" carries too purely
      juridical a feel; the psalm's meditative quality calls for "instruction/teaching."

H6957 (קַו, qav, Ps 19:4): "Line" in L (most literal). In M: "proclamation" — following
      the LXX φθόγγος reading cited in Rom 10:18. In T: "signal/word." This verse is
      paradoxical: the heavens speak without speech; qav here seems to mean the wordless
      outreach of their testimony, not a measuring cord.

H3738 (כָּרוּ, Ps 22:16, "they have pierced"): The MT consonants could be read as
      כָּאֲרִי ("like a lion") or כָּרוּ ("they have dug/pierced"). The LXX (ὤρυξαν),
      Vulgate (foderunt), Peshitta, and NT application all support "pierced." This
      translation reads "pierced" in all three tiers and notes the variant. This is
      not an unambiguous reading of the MT, but it is the dominant exegetical tradition
      and the one the psalm's NT application depends on.

H7214 (רְאֵמִים, re'emim, Ps 22:21): "Wild oxen" — not "unicorns" (KJV). These are
      aurochs (extinct wild cattle), an ancient symbol of terrifying power.

H6757 (צַלְמָוֶת, tsalmaveth, Ps 23:4): Traditionally "shadow of death" (L). In M/T:
      "deepest darkness" — the Hebrew probably means "deep darkness" (tsalmut from tselem
      = darkness), not a compound with mavet (death). However "shadow of death" is so
      embedded in the psalm's reception history that L preserves it.

H6635 (צְבָאוֹת, tseva'ot, Ps 24:10): "Hosts" in L; "Armies" in M/T — the divine
      warrior title. "LORD of Armies" is more transparent than "LORD of Hosts."

H5542 (סֶלָה, selah): Retained as "Selah" in all three tiers throughout.

H4899 (מָשִׁיחַ, mashiach, Ps 20:6): "Anointed one" in L/M; "anointed one" in T.
      The king is the one anointed for this office; the psalm is not explicitly messianic
      in its original setting, but the vocabulary is the same as the later messianic texts.

=== Ps 22:21b — the dramatic turn ===

At v21b "you have answered me!" (עֲנִיתָנִי) the lament suddenly flips to confident
praise. This is not a description of past rescue but a cry of recognition — the LORD
has heard, and the psalmist knows it in the moment. The T tier surfaces this turn
as the theological hinge of the whole psalm.

=== Hebrew poetic structure ===

T tier uses line breaks (\n) for Hebrew parallelism throughout. The introductory
superscription in v1 of each psalm is set off with a blank line before the verse text.
Psalm 22's lament strophes and praise strophes are rendered with distinct rhythms
to honour the structural shift. Psalm 24's antiphonal call-and-response (vv7–10)
is rendered with the question and answer marked clearly.
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
  "19": {
    "1": {
      "L": "To the choirmaster. A Psalm of David. The heavens declare the glory of God, and the firmament proclaims his handiwork.",
      "M": "To the choirmaster. A Psalm of David. The heavens declare the glory of God, and the expanse proclaims his handiwork.",
      "T": "To the worship leader. A Psalm of David.\n\nThe heavens pour forth declarations of God's glory;\nthe vault of the sky blazes with the story of his craft."
    },
    "2": {
      "L": "Day to day pours forth speech, and night to night declares knowledge.",
      "M": "Day after day pours out its speech, and night after night reveals knowledge.",
      "T": "Day passes knowledge to day;\nnight hands its wisdom on to night."
    },
    "3": {
      "L": "There is no speech, and there are no words; their voice is not heard.",
      "M": "There is no speech, there are no words—their voice cannot be heard.",
      "T": "No words are spoken, no language used,\nno voice is heard aloud—"
    },
    "4": {
      "L": "Their line goes through all the earth, and their words to the end of the world. In them he has set a tent for the sun,",
      "M": "Yet their proclamation goes out through all the earth, and their message to the ends of the world. In the heavens he has pitched a tent for the sun,",
      "T": "and yet their signal reaches every corner of the earth,\ntheir wordless message travels to the world's edge.\nThere in the heavens God has pitched a tent for the sun,"
    },
    "5": {
      "L": "which comes out like a bridegroom from his chamber, and rejoices like a strong man to run its course.",
      "M": "which rises like a bridegroom leaving his chamber, and rejoices like a champion eager to run his course.",
      "T": "who rises like a bridegroom stepping from his wedding chamber,\nexulting like a champion who cannot wait to run."
    },
    "6": {
      "L": "Its rising is from the end of the heavens, and its circuit to their ends; and there is nothing hidden from its heat.",
      "M": "Its rising is from one end of the heavens, and its circuit reaches the other end; nothing is hidden from its heat.",
      "T": "It rises at one edge of the sky\nand sweeps its great arc to the other side;\nnothing in all creation is shielded from its heat."
    },
    "7": {
      "L": "The instruction of the LORD is perfect, restoring the soul; the testimony of the LORD is sure, making wise the simple.",
      "M": "The instruction of the LORD is perfect, reviving the soul; the testimony of the LORD is trustworthy, making the simple wise.",
      "T": "The LORD's instruction is flawless—it revives the inner life;\nthe LORD's testimony is reliable—it grants wisdom to the untaught."
    },
    "8": {
      "L": "The precepts of the LORD are right, making the heart rejoice; the commandment of the LORD is pure, enlightening the eyes.",
      "M": "The precepts of the LORD are right, bringing joy to the heart; the commandment of the LORD is radiant, enlightening the eyes.",
      "T": "The LORD's precepts are just—they fill the heart with joy;\nthe LORD's commandment is clear—it opens the eyes to see."
    },
    "9": {
      "L": "The fear of the LORD is clean, enduring forever; the judgments of the LORD are true and righteous altogether.",
      "M": "The fear of the LORD is pure, enduring forever; the judgments of the LORD are true and altogether righteous.",
      "T": "The reverence the LORD calls forth is undefiled—it endures forever;\nthe LORD's verdicts are utterly true, entirely just."
    },
    "10": {
      "L": "More to be desired are they than gold, even much fine gold; and sweeter than honey and drippings of the honeycomb.",
      "M": "They are more desirable than gold, than great quantities of finest gold; and sweeter than honey, than honey dripping from the comb.",
      "T": "More precious than gold they are—than heaps of purest gold;\nsweeter than honey, than honey fresh from the comb."
    },
    "11": {
      "L": "Moreover, by them your servant is warned; in keeping them there is great reward.",
      "M": "Moreover, your servant is warned by them; in keeping them there is great reward.",
      "T": "By them your servant is warned against what harms;\nin obeying them lies great and lasting reward."
    },
    "12": {
      "L": "Who can discern his errors? Acquit me of hidden faults.",
      "M": "Who can understand his own errors? Cleanse me from sins I cannot see.",
      "T": "Who can even see all his own failures?\nDeclare me free of the sins I cannot detect."
    },
    "13": {
      "L": "Also keep back your servant from presumptuous sins; let them not rule over me! Then I shall be blameless, and innocent of great transgression.",
      "M": "Keep your servant also from willful sins; let them not have mastery over me. Then I will be blameless and clean of great rebellion.",
      "T": "Hold your servant back from deliberate defiance—\ndo not let those sins become my masters.\nThen I will be whole and unblemished,\nfree from the weight of flagrant rebellion."
    },
    "14": {
      "L": "Let the words of my mouth and the meditation of my heart be acceptable in your sight, O LORD, my rock and my redeemer.",
      "M": "May the words of my mouth and the meditation of my heart be pleasing in your sight, O LORD, my rock and my redeemer.",
      "T": "May every word from my mouth\nand every movement of my heart\nfind acceptance before you, LORD—\nmy rock, my redeemer."
    }
  },
  "20": {
    "1": {
      "L": "To the choirmaster. A Psalm of David. May the LORD answer you in the day of trouble! May the name of the God of Jacob protect you!",
      "M": "To the choirmaster. A Psalm of David. May the LORD answer you in your day of trouble! May the name of the God of Jacob set you on high!",
      "T": "To the worship leader. A Psalm of David.\n\nMay the LORD answer you when trouble closes in;\nmay the name of Jacob's God be your high tower."
    },
    "2": {
      "L": "May he send you help from the sanctuary and strengthen you from Zion!",
      "M": "May he send you help from his sanctuary and support you from Zion!",
      "T": "May help reach you from the sanctuary;\nmay Zion be the source of your strength."
    },
    "3": {
      "L": "May he remember all your offerings and accept your burnt sacrifices! Selah",
      "M": "May he remember all your offerings and accept your burnt sacrifices! Selah",
      "T": "May he keep every offering you have brought before him,\naccepting your burnt gifts with favor. Selah"
    },
    "4": {
      "L": "May he grant you according to your heart's desire and fulfill all your counsel!",
      "M": "May he grant you your heart's desire and fulfill all your plans!",
      "T": "May he give you the very thing your heart longs for\nand bring every plan you have laid to completion."
    },
    "5": {
      "L": "May we shout for joy in your salvation, and in the name of our God raise our banners! May the LORD fulfill all your petitions!",
      "M": "May we shout for joy at your victory, and in the name of our God raise our banners! May the LORD fulfill all your requests!",
      "T": "We will shout for joy when you are saved;\nwe will plant our banners in the name of our God.\nMay the LORD grant every request you have made."
    },
    "6": {
      "L": "Now I know that the LORD saves his anointed; he will answer him from his holy heaven with the mighty deeds of salvation of his right hand.",
      "M": "Now I know that the LORD saves his anointed one; he answers him from his holy heaven with the saving power of his right hand.",
      "T": "Now I know it for certain: the LORD delivers his anointed one.\nHe answers from his holy heaven;\nfrom there his strong right arm brings deliverance."
    },
    "7": {
      "L": "Some in chariots and some in horses, but we will remember the name of the LORD our God.",
      "M": "Some boast in chariots and some in horses, but we will boast in the name of the LORD our God.",
      "T": "Let others put their confidence in chariots,\nlet others count on cavalry—\nwe invoke the name of the LORD our God."
    },
    "8": {
      "L": "They are bowed down and fallen, but we have risen and stand upright.",
      "M": "They collapse and fall, but we rise and stand firm.",
      "T": "They stumble and go down;\nwe rise and hold our ground."
    },
    "9": {
      "L": "O LORD, save the king! May he answer us when we call.",
      "M": "LORD, give victory to the king! Answer us when we call.",
      "T": "LORD, give the king victory!\nAnswer us the moment we call."
    }
  },
  "21": {
    "1": {
      "L": "To the choirmaster. A Psalm of David. O LORD, in your strength the king rejoices, and in your salvation how greatly he exults!",
      "M": "To the choirmaster. A Psalm of David. The king rejoices in your strength, LORD, and in your salvation how greatly he exults!",
      "T": "To the worship leader. A Psalm of David.\n\nThe king exults in your power, LORD;\nhow greatly he rejoices in the victory you have given!"
    },
    "2": {
      "L": "You have given him his heart's desire and have not withheld the request of his lips. Selah",
      "M": "You have given him his heart's desire and have not withheld what his lips requested. Selah",
      "T": "You gave him the longing of his heart;\nyou held back nothing that his lips asked for. Selah"
    },
    "3": {
      "L": "For you meet him with blessings of goodness; you set a crown of fine gold upon his head.",
      "M": "For you meet him with blessings of goodness and set a crown of finest gold upon his head.",
      "T": "You came out to meet him laden with good gifts;\nyou set upon his head a crown of purest gold."
    },
    "4": {
      "L": "He asked life of you; you gave it to him, length of days forever and ever.",
      "M": "He asked you for life, and you gave it to him—length of days forever and ever.",
      "T": "He asked for life—you gave it:\nlength of days without end, age upon age."
    },
    "5": {
      "L": "His glory is great in your salvation; honor and majesty you have laid upon him.",
      "M": "Through your salvation his glory is great; you have bestowed splendor and majesty upon him.",
      "T": "His glory grows great through the victory you have granted;\nyou have wrapped him in splendor and royal dignity."
    },
    "6": {
      "L": "For you make him a blessing forever; you make him glad with the joy of your presence.",
      "M": "For you make him most blessed forever; you fill him with gladness in your presence.",
      "T": "You have made him a source of blessing without end;\nyou make him radiant with joy in your presence."
    },
    "7": {
      "L": "For the king trusts in the LORD, and through the steadfast love of the Most High he shall not be moved.",
      "M": "For the king trusts in the LORD, and through the steadfast love of the Most High he will not be shaken.",
      "T": "The king's trust is fixed in the LORD;\nthrough the unfailing love of the Most High he stands unmoved."
    },
    "8": {
      "L": "Your hand will find out all your enemies; your right hand will find out those who hate you.",
      "M": "Your hand will reach all your enemies; your right hand will seize those who hate you.",
      "T": "Your hand will track down every enemy;\nyour right arm will close on all who hate you."
    },
    "9": {
      "L": "You will make them like a blazing oven in the time of your anger; the LORD in his wrath will swallow them up, and fire will devour them.",
      "M": "You will make them like a burning oven in the time of your anger; the LORD in his wrath will swallow them up, and fire will devour them.",
      "T": "You will make them like a furnace blazing before your face;\nthe LORD in his fury will consume them—\nfire will swallow them whole."
    },
    "10": {
      "L": "You will destroy their offspring from the earth, and their descendants from among the sons of man.",
      "M": "You will destroy their offspring from the earth and their descendants from among mankind.",
      "T": "You will wipe their offspring from the face of the earth,\ntheir descendants from the human race."
    },
    "11": {
      "L": "For they stretched evil against you; they devised a scheme which they cannot perform.",
      "M": "For they intended evil against you and devised a plot they cannot carry out.",
      "T": "They hatched evil schemes against you\nand laid malicious plans—\nbut every plot dissolves before it forms."
    },
    "12": {
      "L": "For you will make them turn their back; you will aim your bowstrings against their faces.",
      "M": "You will put them to flight as you aim your bow at their faces.",
      "T": "You send them fleeing in retreat;\nyour arrows are already aimed at their faces."
    },
    "13": {
      "L": "Be exalted, O LORD, in your strength! We will sing and praise your power.",
      "M": "Rise in your strength, O LORD! We will sing and praise your mighty deeds.",
      "T": "Rise in your strength, O LORD!\nWe will sing—we will make music to your might."
    }
  },
  "22": {
    "1": {
      "L": "To the choirmaster: according to the Doe of the Dawn. A Psalm of David. My God, my God, why have you forsaken me? Why are you far from my salvation, from the words of my groaning?",
      "M": "To the choirmaster: according to the Doe of the Dawn. A Psalm of David. My God, my God, why have you forsaken me? Why are you so far from saving me, so far from my cries of anguish?",
      "T": "To the worship leader: to the tune 'The Doe of the Dawn.' A Psalm of David.\n\nMy God, my God — why have you abandoned me?\nWhy are you so far, unable to save me,\nso far from the words of my groaning?"
    },
    "2": {
      "L": "O my God, I cry in the daytime, but you do not answer; in the night, and there is no rest for me.",
      "M": "O my God, I cry out by day, but you do not answer; by night I find no relief.",
      "T": "By day I cry out to you, my God—\nbut no answer comes.\nBy night I cry—\nand there is no rest for me."
    },
    "3": {
      "L": "Yet you are holy, you who inhabit the praises of Israel.",
      "M": "But you are holy, enthroned on the praises of Israel.",
      "T": "And yet — you are holy,\nenthroned upon the songs of praise Israel raises to you."
    },
    "4": {
      "L": "Our fathers trusted in you; they trusted, and you delivered them.",
      "M": "In you our ancestors put their trust; they trusted, and you rescued them.",
      "T": "Our ancestors put their hope in you;\nthey trusted — and you delivered them."
    },
    "5": {
      "L": "To you they cried and were saved; in you they trusted and were not put to shame.",
      "M": "They cried to you and were delivered; they trusted in you and were not put to shame.",
      "T": "They cried to you and were rescued;\nthey trusted in you and were never disgraced."
    },
    "6": {
      "L": "But I am a worm and not a man, a reproach of men and despised by the people.",
      "M": "But I am a worm and not a man, scorned by everyone and despised by the people.",
      "T": "But I — I am a worm, not even a man:\nan object of contempt, despised by the crowds."
    },
    "7": {
      "L": "All who see me mock me; they shoot out the lip, they wag the head:",
      "M": "All who see me mock me; they sneer and shake their heads:",
      "T": "Everyone who sees me jeers;\nthey curl their lips and shake their heads:"
    },
    "8": {
      "L": "\"He committed himself to the LORD; let him deliver him; let him rescue him, for he delights in him!\"",
      "M": "\"He trusted in the LORD; let the LORD rescue him. Let him deliver him, since he delights in him!\"",
      "T": "'He claimed the LORD would save him—\nlet the LORD rescue him now!\nLet God deliver him — if he delights in him so much!'"
    },
    "9": {
      "L": "Yet you are he who brought me forth from the womb; you made me trust at my mother's breasts.",
      "M": "Yet you drew me out of the womb; you made me trust in you at my mother's breasts.",
      "T": "Yet you are the one who brought me out of the womb,\nwho made me trust you at my mother's breast."
    },
    "10": {
      "L": "I was cast upon you from the womb; from my mother's belly you are my God.",
      "M": "Upon you I was cast from birth; from my mother's womb you have been my God.",
      "T": "From the moment of birth I was placed in your care;\nfrom my mother's womb you have been my God."
    },
    "11": {
      "L": "Be not far from me, for trouble is near, and there is no one to help.",
      "M": "Do not be far from me, for trouble is near and there is no one to help.",
      "T": "Do not stay far from me —\ntrouble is at my door\nand there is no one else to turn to."
    },
    "12": {
      "L": "Many bulls surround me; strong bulls of Bashan encircle me;",
      "M": "Many bulls surround me; powerful bulls of Bashan encircle me;",
      "T": "A herd of bulls has closed in around me;\nthe great bulls of Bashan have me encircled;"
    },
    "13": {
      "L": "they open their mouths wide against me, like a ravening and roaring lion.",
      "M": "they open wide their jaws against me like a roaring, ravening lion.",
      "T": "they gape their mouths at me\nlike lions that tear their prey and roar."
    },
    "14": {
      "L": "I am poured out like water, and all my bones are out of joint; my heart is like wax, it is melted in the midst of my inward parts.",
      "M": "I am poured out like water, and all my bones are disjointed; my heart has turned to wax, melting within me.",
      "T": "I drain out like spilled water;\nall my bones come apart at the joints.\nMy heart has turned to wax —\nmelting away deep inside me."
    },
    "15": {
      "L": "My strength is dried up like a potsherd; and my tongue clings to my jaws; you lay me in the dust of death.",
      "M": "My strength is dried up like a fragment of pottery; my tongue sticks to the roof of my mouth; you lay me in the dust of death.",
      "T": "My strength crumbles like a broken shard;\nmy tongue sticks to the roof of my mouth.\nYou have brought me down to death's own dust."
    },
    "16": {
      "L": "For dogs surround me; a company of evildoers encircles me; they have pierced my hands and my feet —",
      "M": "For dogs surround me; a mob of evildoers encircles me; they have pierced my hands and feet —",
      "T": "Dogs have surrounded me;\na pack of evildoers has closed in.\nThey have pierced my hands and my feet —"
    },
    "17": {
      "L": "I can count all my bones; they look and stare upon me.",
      "M": "I can count all my bones; they stare and gloat over me.",
      "T": "I can count every bone in my body;\nthey stare at me — gloating."
    },
    "18": {
      "L": "They divide my garments among them, and for my clothing they cast lots.",
      "M": "They divide my garments among themselves and cast lots for my clothing.",
      "T": "They divide my clothes among themselves\nand throw dice for what I am wearing."
    },
    "19": {
      "L": "But you, O LORD, be not far off! O my strength, come quickly to my aid!",
      "M": "But you, LORD, do not stay far away! You are my strength; come quickly to help me!",
      "T": "But you, LORD — do not keep your distance!\nYou are my strength; hurry to help me!"
    },
    "20": {
      "L": "Deliver my soul from the sword, my only one from the hand of the dog!",
      "M": "Rescue my life from the sword, my precious soul from the clutch of the dog!",
      "T": "Save my life from the sword —\nmy one and only life from the grip of these dogs."
    },
    "21": {
      "L": "Save me from the mouth of the lion! From the horns of the wild oxen you have answered me.",
      "M": "Rescue me from the lion's jaws! You have answered me from the horns of the wild oxen.",
      "T": "Rescue me from the lion's mouth!\nFrom the horns of the wild oxen — you have answered me!"
    },
    "22": {
      "L": "I will declare your name to my brothers; in the midst of the assembly I will praise you.",
      "M": "I will proclaim your name to my brothers; in the midst of the congregation I will praise you.",
      "T": "I will declare your name to my family —\nin the full assembly I will sing your praise."
    },
    "23": {
      "L": "You who fear the LORD, praise him! All you offspring of Jacob, honor him! Stand in awe of him, all you offspring of Israel!",
      "M": "You who fear the LORD, praise him! All descendants of Jacob, honor him! Stand in awe of him, all descendants of Israel!",
      "T": "All who fear the LORD — give him praise!\nAll the seed of Jacob, give him glory!\nAll the offspring of Israel, stand in awe of him!"
    },
    "24": {
      "L": "For he has not despised or abhorred the affliction of the afflicted; he has not hidden his face from him, but has heard when he cried to him.",
      "M": "For he has not despised or scorned the suffering of the afflicted one; he has not hidden his face from him but listened when he cried out to him.",
      "T": "For he has not despised the suffering of the one who suffers;\nhe has not turned his face away in disgust.\nWhen that one cried out — he listened, he heard."
    },
    "25": {
      "L": "From you comes my praise in the great assembly; my vows I will pay before those who fear him.",
      "M": "My praise in the great congregation comes from you; I will fulfill my vows before those who fear him.",
      "T": "In the great assembly my praise will rise to you;\nI will carry out my vows before all who fear him."
    },
    "26": {
      "L": "The humble shall eat and be satisfied; those who seek him shall praise the LORD! May your hearts live forever!",
      "M": "The humble will eat and be satisfied; those who seek the LORD will praise him — may your hearts live forever!",
      "T": "The humble will eat their fill;\nall who seek the LORD will praise him —\nlong life to your hearts!"
    },
    "27": {
      "L": "All the ends of the earth shall remember and turn to the LORD, and all the families of the nations shall bow down before him.",
      "M": "All the ends of the earth will remember and turn to the LORD, and all the families of the nations will bow down before him.",
      "T": "Every corner of the earth will remember and return to the LORD;\nevery family of every nation will bow before him."
    },
    "28": {
      "L": "For the kingdom belongs to the LORD, and he rules over the nations.",
      "M": "For dominion belongs to the LORD, and he rules over the nations.",
      "T": "For the kingdom is the LORD's —\nhe holds the nations in his hand."
    },
    "29": {
      "L": "All the prosperous of the earth shall eat and bow down; before him shall bow all who go down to the dust, even the one who could not keep his soul alive.",
      "M": "All the prosperous of the earth will feast and worship; before him all who go down to the dust will bow — even those who cannot preserve their own life.",
      "T": "All the earth's well-fed will feast and bow before him;\nall who descend to the dust will kneel —\neven the one who could not keep himself alive."
    },
    "30": {
      "L": "Posterity shall serve him; it shall be told of the Lord to the coming generation.",
      "M": "Descendants will serve him; the Lord will be declared to the coming generation.",
      "T": "Future generations will serve him;\nthe story of the Lord will be told to those yet to come."
    },
    "31": {
      "L": "They shall come and proclaim his righteousness to a people yet to be born, that he has done it.",
      "M": "They will come and proclaim his saving acts to a people not yet born, declaring that he has done it.",
      "T": "A people not yet born will come to hear\nthat he has brought it all to pass —\nhe has done it."
    }
  },
  "23": {
    "1": {
      "L": "A Psalm of David. The LORD is my shepherd; I shall not be in want.",
      "M": "A Psalm of David. The LORD is my shepherd; I shall lack nothing.",
      "T": "A Psalm of David.\n\nThe LORD is my shepherd —\nthere is nothing I lack."
    },
    "2": {
      "L": "He makes me lie down in green pastures; he leads me beside still waters.",
      "M": "He makes me lie down in green pastures; he leads me beside quiet waters.",
      "T": "He lets me rest in meadows of fresh grass;\nhe leads me to water where I can be still."
    },
    "3": {
      "L": "He restores my soul; he leads me in paths of righteousness for his name's sake.",
      "M": "He restores my inner life; he guides me along right paths for the sake of his name.",
      "T": "He brings my whole self back to life;\nhe guides me on the right paths\nbecause that is who he is."
    },
    "4": {
      "L": "Yea, though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
      "M": "Even though I walk through the valley of deepest darkness, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
      "T": "Even when the path runs through death's dark valley,\nI fear nothing —\nfor you are right beside me.\nYour rod and your staff —\nthey are my comfort."
    },
    "5": {
      "L": "You prepare a table before me in the presence of my enemies; you anoint my head with oil; my cup overflows.",
      "M": "You set a table for me in full view of my enemies; you anoint my head with oil; my cup overflows.",
      "T": "You spread a feast for me\nright in front of those who want me gone.\nYou pour oil on my head;\nmy cup spills over."
    },
    "6": {
      "L": "Surely goodness and steadfast love shall follow me all the days of my life, and I shall dwell in the house of the LORD for length of days.",
      "M": "Surely goodness and steadfast love will pursue me all the days of my life, and I will live in the house of the LORD forever.",
      "T": "Nothing but goodness and steadfast love will track me down\nevery day that I am alive —\nand I will make the LORD's house my home\nfor all my remaining days."
    }
  },
  "24": {
    "1": {
      "L": "A Psalm of David. The earth is the LORD's and its fullness, the world and those who dwell in it;",
      "M": "A Psalm of David. The earth belongs to the LORD and all its fullness; the world and all who live in it.",
      "T": "A Psalm of David.\n\nThe earth and everything it holds belong to the LORD —\nthe world and all who live there."
    },
    "2": {
      "L": "for he has founded it upon the seas and established it upon the rivers.",
      "M": "For he founded it on the seas and established it above the rivers.",
      "T": "For he laid its foundations over the seas\nand set it firm above the great rivers."
    },
    "3": {
      "L": "Who shall ascend the hill of the LORD? And who shall stand in his holy place?",
      "M": "Who may ascend the mountain of the LORD? Who may stand in his holy dwelling?",
      "T": "Who may climb the LORD's mountain?\nWho may take their stand in his holy place?"
    },
    "4": {
      "L": "He who has clean hands and a pure heart, who does not lift up his soul to vanity and does not swear deceitfully.",
      "M": "The one with clean hands and a pure heart, who does not set his mind on worthless things or make deceitful promises.",
      "T": "The one whose hands are clean and whose heart is right —\nwho has never given himself over to emptiness\nor sworn by lies."
    },
    "5": {
      "L": "He will receive blessing from the LORD and righteousness from the God of his salvation.",
      "M": "He will receive blessing from the LORD and vindication from the God who saves him.",
      "T": "He will receive the LORD's blessing,\nthe saving righteousness that comes from God his deliverer."
    },
    "6": {
      "L": "This is the generation of those who seek him, who seek your face, O God of Jacob. Selah",
      "M": "Such is the generation of those who seek him, who seek the face of the God of Jacob. Selah",
      "T": "This is the company of those who seek the LORD,\nwho look for the face of Jacob's God. Selah"
    },
    "7": {
      "L": "Lift up your heads, O gates! And be lifted up, O ancient doors, that the King of glory may come in!",
      "M": "Lift up your heads, you gates! Rise up, you ancient doors, so the King of glory may enter!",
      "T": "Lift up your heads, you ancient gates!\nRise up, you doors that have stood since the beginning —\nthe King of glory is coming in!"
    },
    "8": {
      "L": "Who is this King of glory? The LORD, strong and mighty, the LORD, mighty in battle!",
      "M": "Who is this King of glory? The LORD, strong and mighty, the LORD, powerful in battle!",
      "T": "Who is this King of glory?\nThe LORD — fierce and mighty,\nthe LORD — invincible in battle!"
    },
    "9": {
      "L": "Lift up your heads, O gates! And lift them up, O ancient doors, that the King of glory may come in!",
      "M": "Lift up your heads, you gates! Rise up, you ancient doors, that the King of glory may enter!",
      "T": "Lift up your heads, you ancient gates!\nRise up, you ageless doors —\nthe King of glory is coming in!"
    },
    "10": {
      "L": "Who is this King of glory? The LORD of hosts, he is the King of glory! Selah",
      "M": "Who is this King of glory? The LORD of Armies — he is the King of glory! Selah",
      "T": "Who is this King of glory?\nThe LORD of Armies —\nhe alone is the King of glory. Selah"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'psalms')
        merge_tier(existing, PSALMS, tier_key)
        save(tier_dir, 'psalms', existing)
    print('Psalms 19–24 written.')

if __name__ == '__main__':
    main()
