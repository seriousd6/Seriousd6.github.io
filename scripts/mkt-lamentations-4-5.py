"""
MKT Lamentations chapters 4–5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-lamentations-4-5.py

Translation decisions:

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T where personal-name force is
  significant: 4:11 (he fulfilled his wrath); 4:16 (face of the LORD scattered them);
  5:1 (direct address opening the prayer); 5:19 (eternal throne affirmation); 5:21
  (the petition for return). Same convention as mkt-lamentations-1-2.py.

- H136 (אֲדֹנָי / Adonai): Does not appear prominently in chs 4–5; יהוה carries the
  divine references in these chapters.

- Acrostic structure: Ch 4 is an alphabetic acrostic (22 verses, one per Hebrew letter,
  aleph through taw). Ch 5 also has 22 verses but is NOT an acrostic — it is a communal
  prayer/petition (confirmed by lack of letter-heading structure). The T tier for ch 4
  retains poetic cadence verse-by-verse; ch 5 T reads as sustained communal prayer, not
  fragmented acrostic units.

- H5771 (עָוֹן / ʿāwôn): "iniquity" in L/M; "guilt" in T. Carries the sense of both
  the act and its ongoing consequence/burden — Zion's guilt is accomplished at 4:22.

- H6588 (פֶּשַׁע / peshaʿ): "transgression/sin" in L/M; "sin/rebellion" in T. Covenant-
  breach language. At 4:22 "he will expose thy sins" = peshaʿ of Edom will be uncovered.

- H5030 (נָבִיא / nābîʾ): "prophets" throughout. 4:13 assigns the fall of Jerusalem
  partly to "the sins of her prophets" who shed innocent blood — consistent with ch 2:9,14
  and the Jeremianic polemic against false prophecy.

- Gold / stones imagery (4:1–2): The "gold" (zahāb, 4:1) and "fine gold" (ketem, from
  which the interlinear has "most fine gold") and "holy stones" (stones of the sanctuary)
  are rendered in straightforward language. "Fine gold" and "most fine gold" are both
  attested; L uses "finest gold," M uses "finest gold," T surfaces the theological
  dimension (sanctuary treasury).

- Nazirites (4:7): נְזִירֶיהָ (nezireha) — the "dedicated ones/consecrated ones." Could
  mean Nazirites (Num 6 vow) or Jerusalem's noble/consecrated class more broadly. Context
  of 4:7–8 contrasts their past radiance with present starvation. Rendered "dedicated
  ones" in L/M; T: "consecrated men" to preserve the religious-purity register.

- H5315 (נֶפֶשׁ) at 5:9: "peril of our lives" — embodied self at risk; no immaterial
  soul imported. Context of raiding/sword in the open country.

- "Breath of our nostrils" (4:20): נִשְׁמַת אַפֵּינוּ (nishmat ʾappenu) — the king as
  the very breath of the nation's life. A striking idiom. L preserves it literally. M:
  "the very breath of our nostrils." T surfaces the regal/covenant dimension: the king
  who was Israel's life and shadow (cf. Ps 2, 2 Sam 7 messianic framework) has been
  captured.

- "Anointed of the LORD" (4:20): מְשִׁיחַ יהוה — the king (likely Zedekiah, captured per
  2 Kgs 25:4–5). Rendered "the LORD's anointed" in L/M; T: "the LORD's anointed king."

- Cup of wrath (4:21): "The cup also shall pass through unto thee" — cup of God's wrath
  (cf. Jer 25:15–29; Ps 75:8). Edom gloated at Jerusalem's fall (Ps 137:7; Obad 1:12–14).
  This verse is ironic invitation — apparent congratulations that are actually announcement
  of coming judgment. Preserved as irony in all three tiers.

- Final verse tension (5:22): כִּי אִם־מָאֹס מְאַסְתָּנוּ ("unless/for indeed you have
  utterly rejected us"). The ambiguity between assertion and condition is intentional:
  does the book end in hope (v21) or in the fear of ultimate rejection (v22)? L uses
  "unless" (conditional, leaving the question open). M: "Or have you utterly rejected us?"
  T names the theological tension explicitly. In synagogue tradition v21 is repeated after
  v22 so the scroll does not end on rejection — this context shapes the T rendering.

- Generational guilt (5:7): "Our fathers sinned and are not; we bear their iniquities."
  This echoes Ezek 18 and the Decalogue (Exod 20:5) debates about intergenerational
  accountability. The community here neither protests unfairness nor fully absolves their
  ancestors — they confess their own sin at 5:16. T surfaces the weight of inherited
  consequence without resolving the theological tension.

- Speaker: Ch 4 shifts between narrator (vv. 1–16 in third person about Zion) and first-
  person communal voice ("we," vv. 17–22). Ch 5 is entirely communal first person ("we"
  throughout). These shifts are preserved across all tiers.
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

LAMENTATIONS = {
  "4": {
    "1": {
      "L": "How the gold has grown dim, how the finest gold has changed! The holy stones are scattered at the head of every street.",
      "M": "How the gold has lost its luster, how the finest gold is tarnished! The sacred stones lie scattered at the head of every street.",
      "T": "Alas — the gold has gone dark. The finest gold no longer gleams. The stones of the sanctuary are strewn across every street corner like rubble."
    },
    "2": {
      "L": "The precious sons of Zion, comparable in weight to fine gold — how they are now reckoned as earthen vessels, the work of a potter's hands!",
      "M": "The precious sons of Zion, once worth their weight in gold, are now counted as earthen pottery, the work of a potter's hands.",
      "T": "Zion's sons were precious as gold — every one of them worth that much. Now they are treated like clay pots, mass-made things that can be broken and discarded."
    },
    "3": {
      "L": "Even jackals bare the breast and nurse their young, but the daughter of my people has become cruel, like the ostriches in the wilderness.",
      "M": "Even jackals bare their breasts and nurse their young, but my people's daughter has become cruel, like ostriches in the wilderness.",
      "T": "Even wild jackals nurse their pups. But Zion has grown crueler than desert ostriches — those creatures that abandon their eggs and walk away indifferent to the lives they have made."
    },
    "4": {
      "L": "The tongue of the nursing infant cleaves to the roof of his mouth for thirst. Young children beg for bread, but no one breaks it for them.",
      "M": "The nursing infant's tongue cleaves to the roof of his mouth for thirst. Young children beg for bread, but no one has any to break for them.",
      "T": "Babies' tongues are stuck to the roofs of their mouths — they are that thirsty. Children reach out for bread. No one has any to give."
    },
    "5": {
      "L": "Those who feasted on delicacies perish desolate in the streets. Those who were brought up in scarlet now cling to ash heaps.",
      "M": "Those who feasted on fine food lie destitute in the streets. Those raised in royal purple now embrace ash heaps.",
      "T": "The people who grew up eating the finest food now starve in the open streets. Those who were raised wrapped in purple now clutch at ash heaps for whatever warmth they can find."
    },
    "6": {
      "L": "For the punishment of the iniquity of the daughter of my people is greater than the punishment of Sodom's sin, which was overthrown in a moment with no hands turned against her.",
      "M": "The punishment for the iniquity of my people's daughter is greater than the penalty for Sodom's sin, which was overthrown in an instant with no human hands against her.",
      "T": "Sodom's ruin was swift — an instant, and it was finished. No prolonged siege, no slow starvation, no human armies pressing in. But the punishment laid on Jerusalem for her sin has been heavier and longer than anything Sodom ever endured."
    },
    "7": {
      "L": "Her dedicated ones were purer than snow, whiter than milk; their bodies more ruddy than coral, their form like sapphire.",
      "M": "Her dedicated ones were purer than snow, whiter than milk; their bodies more ruddy than coral, their bearing like sapphire.",
      "T": "Her consecrated men were once radiant with health — snow-white, milk-pure, their bodies flushed with vitality like polished coral, their bearing as fine-cut as sapphire."
    },
    "8": {
      "L": "Now their face is blacker than soot; they are not recognized in the streets. Their skin has shriveled on their bones; it has become dry as a stick.",
      "M": "Now their appearance is blacker than soot; they are not known in the streets. Their skin has shriveled onto their bones, dried hard as wood.",
      "T": "Now those same faces are black as charcoal — no one recognizes them. Their skin has collapsed onto their bones and dried stiff as a stick. Starvation has stolen every trace of who they were."
    },
    "9": {
      "L": "Better off are those slain by the sword than those slain by famine. For these waste away, pierced through for lack of the fruits of the field.",
      "M": "Better were those killed by the sword than those killed by famine. These waste away, run through with hunger for lack of produce from the fields.",
      "T": "A sword-death is merciful by comparison. The sword ends quickly. Famine runs you through slowly — day by day, wasting you away — for lack of what the fields should have given. The sword-killed are better off."
    },
    "10": {
      "L": "The hands of compassionate women have boiled their own children. They became their food in the destruction of the daughter of my people.",
      "M": "Compassionate women boiled their own children with their own hands. Their children became food during the destruction of my people's daughter.",
      "T": "Women known for tenderness — women whose compassion was their mark — boiled their own children and ate them. This happened during the fall of Jerusalem. That is the depth of what the siege produced."
    },
    "11": {
      "L": "The LORD has accomplished his fury; he has poured out his fierce anger. He kindled a fire in Zion that consumed her very foundations.",
      "M": "The LORD fulfilled his wrath; he poured out his fierce anger. He kindled a fire in Zion that consumed her foundations.",
      "T": "Yahweh carried out every word of his wrath — nothing held back, nothing softened. He poured it all out. He set Zion on fire, and the fire burned all the way down to the foundations."
    },
    "12": {
      "L": "The kings of the earth and all the inhabitants of the world would not have believed that adversary or enemy would enter the gates of Jerusalem.",
      "M": "The kings of the earth and all the world's inhabitants would not have believed that foe or enemy could enter the gates of Jerusalem.",
      "T": "The whole world considered Jerusalem impregnable. Kings and common people alike would have laughed at the notion of an enemy walking through her gates. That certainty is now rubble."
    },
    "13": {
      "L": "It is because of the sins of her prophets and the iniquities of her priests, who shed in her midst the blood of the righteous.",
      "M": "This came because of the sins of her prophets and the iniquities of her priests, who shed the blood of the righteous in her midst.",
      "T": "The cause was her own prophets and priests. Their sins and accumulated guilt — and above all the innocent blood they shed inside the city. The people who should have upheld righteousness were the ones who destroyed it."
    },
    "14": {
      "L": "They wandered like blind men in the streets; they were so defiled with blood that no one could touch their garments.",
      "M": "They wandered through the streets like blind men, so defiled with blood that no one was able to touch their garments.",
      "T": "They stumbled blind through the streets, stained through with blood — so ritually contaminated that passersby recoiled and would not brush even the edge of their clothing."
    },
    "15": {
      "L": "'Away! Unclean!' people cried at them. 'Away, away, do not touch!' When they fled and wandered, the nations said, 'They shall sojourn here no longer.'",
      "M": "'Away! Unclean!' people shouted at them. 'Away! Away! Do not touch us!' When they fled and wandered, the nations declared, 'They will not dwell among us anymore.'",
      "T": "Everywhere they went, people shouted them away: 'Unclean! Unclean! Do not touch us!' The cry once reserved for lepers was now turned on Jerusalem's priests. They became fugitives wherever they roamed, and the nations would not receive them: 'These people have no home among us any longer.'"
    },
    "16": {
      "L": "The face of the LORD has scattered them; he will regard them no more. They showed no honor to the priests; they showed no favor to the elders.",
      "M": "The LORD's presence scattered them; he will look on them no longer. No honor was shown to the priests, no favor to the elders.",
      "T": "It was Yahweh's own face — his attention turned against them in judgment — that drove them into exile. He will not look on them again in favor. Their captors showed neither reverence for the priests nor respect for the elders. Every social honor was torn away."
    },
    "17": {
      "L": "Our eyes failed, looking in vain for help. In our watching we watched for a nation that could not save.",
      "M": "Our eyes strained in vain for help. We kept watch for a nation that could not save us.",
      "T": "We exhausted our eyes watching the horizon for an ally who never came. We watched and waited for a nation that would rescue us — and the waiting was useless. No one came. No one could save us, or chose to."
    },
    "18": {
      "L": "They dogged our steps so that we could not walk freely in our streets. Our end drew near; our days were fulfilled; our end had come.",
      "M": "They hunted our steps so that we could not walk in our streets. Our end drew near, our days were fulfilled; our end had arrived.",
      "T": "They tracked us even inside the city — we could not move without being watched, hunted. Then the end gathered itself together: near, then certain, then present. The days ran out. The end came."
    },
    "19": {
      "L": "Our pursuers were swifter than the eagles of the heavens. They chased us on the mountains; they lay in wait for us in the wilderness.",
      "M": "Our pursuers were swifter than the eagles of the sky. They pursued us through the mountains; they lay in wait for us in the wilderness.",
      "T": "They ran us down like eagles — there was no terrain to outpace them. We fled to the mountains; they were already there. We scattered into the wilderness; they were waiting."
    },
    "20": {
      "L": "The breath of our nostrils, the LORD's anointed, was caught in their pits — he of whom we said, 'Under his shadow we shall live among the nations.'",
      "M": "The LORD's anointed, the very breath of our nostrils, was caught in their pits — the one of whom we said, 'Under his shadow we shall live among the nations.'",
      "T": "The king — the LORD's anointed, the living breath of the whole people — was taken in a trap. He was the shade we sheltered under, the one under whose protection we believed we could survive even in exile among the nations. He is gone."
    },
    "21": {
      "L": "Rejoice and be glad, O daughter of Edom, who dwells in the land of Uz! But the cup shall pass to you also; you shall be drunk and make yourself bare.",
      "M": "Rejoice and celebrate, daughter of Edom, you who live in the land of Uz! But the cup will come to you as well; you will drink it and expose yourself in your shame.",
      "T": "Go ahead, Edom — celebrate. Cheer from your seat in Uz. But the cup of God's wrath that Jerusalem drank will be passed to you. You will drink it and reel, stripped of every defense, every pretension, every dignity."
    },
    "22": {
      "L": "The punishment of your iniquity is accomplished, O daughter of Zion; he will not exile you again. He will visit your iniquity, O daughter of Edom; he will uncover your sins.",
      "M": "Your punishment is complete, daughter of Zion; he will not send you into exile again. But your iniquity will be punished, daughter of Edom; he will expose your sins.",
      "T": "Zion's punishment is finished. The sentence has been served; no new exile is coming. But Edom's sins have not yet been reckoned — her guilt will be addressed, her hidden shame exposed. Jerusalem's suffering ends here. Edom's is still ahead."
    }
  },
  "5": {
    "1": {
      "L": "Remember, O LORD, what has come upon us. Look and see our reproach.",
      "M": "Remember, O LORD, what has happened to us. Look and see our disgrace.",
      "T": "Remember us, LORD. Look at what has happened. See our shame. We cannot carry this alone — we can only bring it before you."
    },
    "2": {
      "L": "Our inheritance has passed to strangers, our houses to foreigners.",
      "M": "Our inheritance has been given over to strangers, our houses to foreigners.",
      "T": "Everything our ancestors left us is in other hands now. The land, the houses — all of it belongs to strangers."
    },
    "3": {
      "L": "We have become orphans, fatherless; our mothers are like widows.",
      "M": "We have become fatherless orphans; our mothers are as widows.",
      "T": "We are orphans with no father left to protect us. Our mothers live as widows among us. An entire generation of fathers has been swallowed by war and exile."
    },
    "4": {
      "L": "We drink our water for money; our wood comes to us at a price.",
      "M": "We pay money for the water we drink; our wood must be bought at cost.",
      "T": "We pay for water. We pay for wood. What should have been ours freely — what the land and the forests once gave — has been taken from us and sold back at a price."
    },
    "5": {
      "L": "Our pursuers are upon our necks; we are weary, with no rest given to us.",
      "M": "Our pursuers are at our necks; we are driven hard with no rest.",
      "T": "There is a yoke on our necks and a driver behind us. We labor without stopping, pressed and pursued, with nowhere to rest and no one to call it off."
    },
    "6": {
      "L": "We stretched out the hand to Egypt, and to Assyria, to be satisfied with bread.",
      "M": "We gave our hand to Egypt and to Assyria in order to get enough bread.",
      "T": "We begged from Egypt. We submitted to Assyria. We traded our independence piece by piece — anything for bread, anything to stay alive."
    },
    "7": {
      "L": "Our fathers sinned and are no more; we bear their iniquities.",
      "M": "Our fathers sinned and are gone; we carry the weight of their iniquities.",
      "T": "Our fathers sinned — and now they are dead. The debt fell to us. We carry the burden of guilt that was not entirely ours, and there is no one left to share the load."
    },
    "8": {
      "L": "Servants rule over us; there is none to deliver us from their hand.",
      "M": "Slaves rule over us; there is no one to rescue us from their power.",
      "T": "Men who once served others now govern us. The whole social order has been inverted. And no one is coming to set us free."
    },
    "9": {
      "L": "We bring in our bread with peril of our lives, because of the sword in the wilderness.",
      "M": "We risk our lives to get our bread, because of the sword that threatens in the open country.",
      "T": "Even getting food is a gamble with your life. Bandits and soldiers control the open land; every trip to the field is a venture into danger."
    },
    "10": {
      "L": "Our skin burns hot as an oven from the scorching heat of famine.",
      "M": "Our skin burns hot as an oven because of the fever brought on by famine.",
      "T": "Our skin has gone dry and burning hot — the fever that comes with starvation does that to the body. We are being consumed from within."
    },
    "11": {
      "L": "Women have been ravished in Zion, and virgins in the cities of Judah.",
      "M": "Women have been violated in Zion, young women in the towns of Judah.",
      "T": "In Zion and in every town across Judah, women and young girls have been brutalized. The violence has reached everywhere, sparing no one."
    },
    "12": {
      "L": "Princes are hung up by their hands; the faces of elders are not honored.",
      "M": "Princes have been hanged by their hands; no honor is shown to the faces of elders.",
      "T": "Princes are strung up by their wrists — their authority made into spectacle, their deaths a display. Elders who once commanded reverence are treated with contempt. Every rank, every dignity has been demolished."
    },
    "13": {
      "L": "Young men carried the grinding stone; boys stumbled under loads of wood.",
      "M": "Young men are set to work at the grinding stone; boys stagger under loads of wood.",
      "T": "Young men work the grinding stone like slaves — the ancient image of conquered humiliation. Boys are made to haul wood until they buckle under the weight. Two generations of captive labor."
    },
    "14": {
      "L": "The elders have ceased from the gate; the young men from their music.",
      "M": "The elders have left the city gate; the young men have abandoned their music.",
      "T": "The gate is deserted — no elders sitting there to hear disputes or conduct the commerce of the city. The music is silent — no songs in the streets, no young men playing. Two generations of ordinary life, simply erased."
    },
    "15": {
      "L": "The joy of our heart has ceased; our dance has turned to mourning.",
      "M": "The joy of our hearts has ended; our dancing has turned into mourning.",
      "T": "There is no joy. What was dancing has become grief. The reversal Psalm 30 promised in the other direction has happened here in reverse — mourning has swallowed the dance."
    },
    "16": {
      "L": "The crown has fallen from our head. Woe to us, for we have sinned!",
      "M": "The crown has fallen from our head. Woe to us — we have sinned!",
      "T": "The crown is in the dirt. Our sovereignty, our dignity, our standing as God's people — all of it has fallen from us. And we know why: we sinned. There is no hiding from it. Woe to us."
    },
    "17": {
      "L": "For this our heart has grown faint; for these things our eyes have grown dim.",
      "M": "Because of this our heart has grown faint; for all these things our eyes have become dim.",
      "T": "This is why our hearts are failing. This is why we can barely see anymore. We have looked too long at too much ruin."
    },
    "18": {
      "L": "Because of Mount Zion, which lies desolate; jackals prowl over it.",
      "M": "On account of Mount Zion, which lies desolate, jackals prowl across it.",
      "T": "And Zion herself — the holy mountain, the place where the Name dwelled — lies empty. Jackals range across it. That is how completely it has been abandoned."
    },
    "19": {
      "L": "But you, O LORD, reign forever; your throne endures from generation to generation.",
      "M": "But you, O LORD, reign forever; your throne endures through all generations.",
      "T": "Yet you, LORD — you are still there. You reign. Your throne does not fall, does not shift, does not fail. Through every generation it stands. Everything else has collapsed, but not you."
    },
    "20": {
      "L": "Why do you forget us forever? Why do you forsake us for so many days?",
      "M": "Why have you forgotten us forever? Why have you forsaken us for such a long time?",
      "T": "Then why? If you are eternal — if your throne endures across every generation — why have you forgotten us as if we no longer exist? How long is this abandonment going to last?"
    },
    "21": {
      "L": "Turn us back to yourself, O LORD, and we shall return. Renew our days as of old.",
      "M": "Restore us to yourself, O LORD, that we may be restored. Renew our days as in former times.",
      "T": "Turn us back to you, LORD — we cannot find the way on our own. If you turn us, we will turn. Give us back our former days. Restore what has been taken from us and from you."
    },
    "22": {
      "L": "Unless you have utterly rejected us and are exceedingly angry with us.",
      "M": "Or have you utterly rejected us? Are you exceedingly angry with us without end?",
      "T": "Unless you have cast us off completely. Unless the fury you bear toward us has no measure and no end. We have prayed for restoration — but this final question will not leave us: are we still yours? The scroll ends here, but in the sanctuary, verse twenty-one is spoken again — because this cannot be the last word."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'lamentations')
        merge_tier(existing, LAMENTATIONS, tier_key)
        save(tier_dir, 'lamentations', existing)
    print('Lamentations 4–5 written.')

if __name__ == '__main__':
    main()
