"""
MKT Ezekiel chapters 31–33 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-31-33.py

=== CHAPTER OVERVIEW ===
Chapter 31: Oracle comparing Pharaoh/Egypt to the great cedar of Lebanon — which itself
represents Assyria's former greatness. The structure is: (1) vv. 1–9, the cedar's beauty
and height surpassing even Eden's trees; (2) vv. 10–12, the fall because of pride;
(3) vv. 13–14, the theological lesson for all nations; (4) vv. 15–17, God's mourning and
the cosmic response; (5) v. 18, the application to Pharaoh. The chapter closes the series
of cedar imagery in Ezekiel (17:3, 22–23; 27:5; 31).

Chapter 32: Two distinct oracles over Egypt/Pharaoh. (1) vv. 1–16, a lament over Pharaoh
as a sea-dragon — God catches, kills, and scatters him, darkening the heavens. (2) vv. 17–32,
the underworld scene: Egypt descends to Sheol and finds Assyria, Elam, Meshech/Tubal, Edom,
and the princes of the North already assembled there. One of Ezekiel's most dramatic passages;
the T tier preserves its poetic force.

Chapter 33: The pivot chapter of the book. (1) vv. 1–9, the watchman parable — reprises
ch. 3 but now in full public form; (2) vv. 10–20, individual accountability and the open
door of repentance; (3) v. 21, the climactic historical moment — a fugitive arrives reporting
Jerusalem's fall (cf. 24:27); (4) v. 22, Ezekiel's mouth is opened — his silence since 24:27
is now lifted; (5) vv. 23–29, oracle against survivors in the land who presume on Abraham's
example; (6) vv. 30–33, the people come to Ezekiel as entertainment — they hear but will not do.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially recognition formulas
  and narrative pivot points. Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Lord GOD): "Lord GOD" in L/M (small-caps GOD convention).
  "Lord Yahweh" in T. Consistent with prior Ezekiel scripts.

- Recognition formula (וְיָדְעוּ כִּי אֲנִי יְהוָה): L/M "they/you shall know that I am
  the LORD." T "they/you shall know that I am Yahweh."

- H6174 (עָרֵל / uncircumcised): Retained as "uncircumcised" in all tiers — the word carries
  specific covenant meaning: outside the sign of the covenant, outside God's particular people.
  In the underworld scenes of ch. 32, it marks those who died outside covenant relationship.
  Not euphemized.

- H7585 (שְׁאוֹל / Sheol) and H953 (בּוֹר / pit/Pit): L "the grave/pit." M "Sheol/the Pit."
  T "Sheol/the Pit/the realm of the dead" — the shadowy underworld of all the dead, cognate
  with Mesopotamian kur/irkalla. Not eternal damnation; the common destination of the dead.
  Sheol is capitalized in M/T when used as a proper noun.

- H730 (אֶרֶז / cedar): Retained as "cedar" in all tiers. The cedar of Lebanon was the
  prestige timber of the ancient world — used in Solomon's temple, in palace construction.
  The cedar allegory in ch. 31 depends on this cultural weight.

- H7307 (רוּחַ / spirit/wind): Not prominent in these chapters; context determines rendering.

- H5315 (נֶפֶשׁ / soul/self/life): L "soul." M/T "life" or "self" per context.

- H2617 (חֶסֶד / steadfast love/covenant loyalty): Not prominent in these judgment oracles.

- H7725 (שׁוּב / turn/return/repent): Critical term in ch. 33's accountability section.
  L "turn." M "turn back" or "turn from." T "turn" with interpretive expansion on what
  genuine turning means. The term's directional force (you were going one way; turn the
  other) is preserved in all tiers.

- H5921 (עַל / because of / upon / against): Preposition with multiple senses; context-driven.

- H4194 (מָוֶת / death): L "death." M/T "death" — straightforward.

=== ASPECT / TENSE NOTES ===

- Ch. 31 uses mixed past/future: the cedar's description is past (completed past of Assyria's
  greatness). The judgment is perfect + prophetic future. The lesson (v. 14) is a future-looking
  purpose clause. The L tier preserves this distribution.

- Ch. 32:1–16 uses future for the judgment against Egypt (it has not yet fully happened).
  vv. 17–32 use past/perfect for the underworld scene (treated as accomplished fact).

- Ch. 33:1–20 uses present/imperfect for the parable principles (timeless truths).
  v. 21 shifts to narrative past (the fugitive arrived). vv. 22ff. resume prophetic pronouncements.

=== OT INTERTEXTUALITY ===

- Ch. 31's cedar surpassing Eden's trees (vv. 8–9) echoes the king of Tyre's "Eden" passage
  (28:13). Both depict pride that reaches into sacred space. The fall from that height is
  correspondingly severe.

- The "descent to the Pit" motif (31:14–18) is the same vocabulary developed at length in
  ch. 32's underworld scene. The T tier notes the connection.

- Ch. 32's darkening of heavens (vv. 7–8) echoes the Day of the LORD language in Joel 2:10;
  Amos 8:9; Isa. 13:10. This is not merely poetic but apocalyptic register.

- Ch. 32's underworld assembly (vv. 22–32) is the conceptual forerunner of Isaiah 14:9–11
  (the taunt against Babylon's king) and Revelation 18 (the lament over Rome/Babylon).

- Ch. 33:31 echoes Isaiah 29:13 (this people honors me with their lips but their hearts are
  far from me — quoted by Jesus in Matt. 15:8). Ezekiel here is diagnosing the same
  phenomenon: aesthetic engagement with the word of God that produces no obedience.

- Ch. 33's watchman passage (vv. 1–9) is a public, generalized version of Ezekiel's private
  commissioning as watchman in 3:17–21. The repetition is significant: now that Jerusalem
  has fallen, the watchman principle is being re-established for the future.
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

EZEKIEL = {
  "31": {
    "1": {
      "L": "And it came to pass in the eleventh year, in the third month, in the first day of the month, that the word of the LORD came unto me, saying:",
      "M": "In the eleventh year, on the first day of the third month, the word of the LORD came to me:",
      "T": "In the eleventh year, first day of the third month — as Jerusalem's siege was still underway — Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, speak unto Pharaoh king of Egypt, and to his multitude: Whom art thou like in thy greatness?",
      "M": "Son of man, say to Pharaoh king of Egypt and to his multitude: Whom are you like in your greatness?",
      "T": "Son of man, address Pharaoh king of Egypt — him and all his people — with this question: To whom do you compare yourself in your greatness? The question itself is a challenge. Let us examine the comparison."
    },
    "3": {
      "L": "Behold, the Assyrian was a cedar in Lebanon with fair branches, and with a shadowing shroud, and of high stature; and his top was among the thick boughs.",
      "M": "Consider: Assyria was a cedar in Lebanon with beautiful branches and a shady canopy, tall in stature, with its top among the clouds.",
      "T": "Consider what Assyria was: a great cedar of Lebanon — sweeping branches that cast shade like a whole forest, a height that reached the clouds, a crown among the thick boughs of the sky. That is what greatness looked like. That is your comparison point."
    },
    "4": {
      "L": "The waters made him great, the deep set him up on high with her rivers running about his plants, and sent out her little rivers unto all the trees of the field.",
      "M": "The waters made it great; the deep raised it up high, running its rivers all around where it was planted and sending its streams to all the trees of the field.",
      "T": "The deep waters — the great underground reservoirs and the channeled rivers — raised it up and sustained its height. Everything it needed flowed to it. Its abundance overflowed, watering every surrounding tree. Prosperity feeding prosperity: this is what empire always sounds like from the inside."
    },
    "5": {
      "L": "Therefore his height was exalted above all the trees of the field, and his boughs were multiplied, and his branches became long because of the multitude of waters, when he shot forth.",
      "M": "Therefore it grew taller than all the trees of the field; its boughs multiplied and its branches grew long from the abundant water.",
      "T": "Watered so abundantly, the cedar surpassed every competitor — taller than every other tree in the forest, branches proliferating, boughs stretching outward and upward without limit. The abundance became the basis of pride. This is always how it goes with empires."
    },
    "6": {
      "L": "All the fowls of heaven made their nests in his boughs, and under his branches did all the beasts of the field bring forth their young, and under his shadow dwelt all great nations.",
      "M": "All the birds of the sky nested in its boughs; under its branches all the beasts of the field gave birth; all great nations dwelt in its shade.",
      "T": "The cedar sheltered everyone. Birds nested in its crown; animals bore their young in the security of its shadow; whole nations lived beneath it and drew their safety from its standing. The image is one of total imperial beneficence — or what empire always tells itself about itself."
    },
    "7": {
      "L": "Thus was he fair in his greatness, in the length of his branches: for his root was by great waters.",
      "M": "He was beautiful in his greatness, magnificent in the length of his branches, for his root drew from abundant waters.",
      "T": "Beautiful — genuinely, objectively beautiful. The length of the branches, the root drinking from the deep: this was a real greatness, not merely claimed. That is what makes the fall more devastating: when what is destroyed was genuinely magnificent."
    },
    "8": {
      "L": "The cedars in the garden of God could not hide him: the fir trees were not like his boughs, and the chestnut trees were not like his branches; nor any tree in the garden of God was like unto him in his beauty.",
      "M": "The cedars in the garden of God could not match him; the fir trees were not like his boughs, nor the plane trees like his branches — no tree in the garden of God compared to him in beauty.",
      "T": "Even the trees in God's own garden — Eden's cedars, Eden's firs, Eden's plane trees — could not match this cedar. It had outgrown its comparison class. In all of God's garden, nothing was as beautiful.\n\nThis is the moment of maximum pride — and the moment most dangerous to the one who occupies it. The tree that surpasses God's garden has placed itself above God."
    },
    "9": {
      "L": "I have made him fair by the multitude of his branches: so that all the trees of Eden, that were in the garden of God, envied him.",
      "M": "I made him beautiful with his many branches, so that all the trees of Eden in the garden of God envied him.",
      "T": "I made it beautiful. God says this clearly — the glory of Assyria was something God gave it. The envy of Eden's trees was not Assyria's achievement but God's gift. This is why the pride is so catastrophic: what God gives and you call your own becomes the foundation of your fall."
    },
    "10": {
      "L": "Therefore thus saith the Lord GOD: Because thou hast lifted up thyself in height, and he hath shot up his top among the thick boughs, and his heart is lifted up in his height;",
      "M": "Therefore thus says the Lord GOD: Because it grew tall and set its top among the clouds, and its heart was proud of its height —",
      "T": "Therefore, thus says the Lord Yahweh: The indictment is simple. God gave the height. The cedar took the credit. Its heart was proud — and the heart of an empire is proud — setting its crown among the clouds, declaring by its very posture that it answered to no one above it."
    },
    "11": {
      "L": "I have therefore delivered him into the hand of the mighty one of the heathen; he shall surely deal with him: I have driven him out for his wickedness.",
      "M": "I gave him over to the hand of the mightiest of nations; he dealt with him accordingly — I drove him out for his wickedness.",
      "T": "The sentence: handed over to the mightiest of nations — Babylon, the instrument raised precisely for this purpose. Driven out. The pride that declared itself independent of God was met with the power God had raised up specifically to answer it."
    },
    "12": {
      "L": "And strangers, the terrible of the nations, have cut him off, and have left him: upon the mountains and in all the valleys his branches are fallen, and his boughs are broken by all the rivers of the land; and all the people of the earth are gone down from his shadow, and have left him.",
      "M": "Foreigners — the most ruthless of nations — cut him down and left him; his branches fell on the mountains and in all the valleys; his boughs lie broken in all the ravines of the land. All the peoples of the earth have departed from his shade and abandoned him.",
      "T": "The fall of the cedar:\nForeigners — the pitiless ones, the ruthless warriors with no sentiment about great trees —\ncut it down and left it where it fell.\nBranches on the mountains. Boughs in the valleys. Broken limbs in every ravine.\nAnd the nations that had lived in its shade — the ones who nested and bore young there, who depended on its standing —\nthey walked away.\nEmpires have no loyal mourners. When the shade is gone, those who lived in it simply leave."
    },
    "13": {
      "L": "Upon his ruin shall all the fowls of the heaven remain, and all the beasts of the field shall be upon his branches:",
      "M": "On its fallen trunk all the birds of the sky will settle, and all the beasts of the field will gather on its boughs.",
      "T": "The birds that once nested in the living cedar now perch on its fallen ruin. The animals that once sheltered beneath it now walk across its prostrate trunk. The same creation that expressed its glory now expresses its fall. Nature moves on without ceremony."
    },
    "14": {
      "L": "To the end that none of all the trees by the waters exalt themselves for their height, neither shoot up their top among the thick boughs, neither their trees stand up in their height, all that drink water: for they are all delivered unto death, to the nether parts of the earth, in the midst of the children of men, with them that go down to the pit.",
      "M": "So that no tree beside the waters may exalt itself for its height or set its top among the clouds — for all who drink water are given over to death, to the depths of the earth, among the children of men, with those who go down to the Pit.",
      "T": "This is the lesson Assyria's fall is meant to teach every nation that follows:\nNo tree that drinks — no nation that draws its power from resources God provides —\nmay exalt itself to cloud-height, may set itself up as if it were above judgment.\nAll flesh is mortal. All empires descend.\nEvery human being, every nation, shares in the death that awaits all who go down to the Pit.\nThere is no height from which the fall cannot reach."
    },
    "15": {
      "L": "Thus saith the Lord GOD: In the day when he went down to the grave I caused a mourning: I covered the deep for him, and I restrained the floods thereof, and the great waters were stayed: and I caused Lebanon to mourn for him, and all the trees of the field fainted for him.",
      "M": "Thus says the Lord GOD: On the day he went down to Sheol I caused a mourning; I covered the deep over him and restrained his rivers, holding back the great waters; I made Lebanon mourn for him, and all the trees of the field fainted on his account.",
      "T": "Thus says the Lord Yahweh: On the day Assyria went down to Sheol — I mourned it.\nGod mourning the fall of the empire he judged: this is worth pausing over.\nI covered the deep — the very waters that had made the cedar great — I restrained them, held them back.\nLebanon, whose trees had been the cedar's companions and rivals, went into mourning.\nAll the trees of the field — all the nations that had lived in Assyria's shadow — fainted at the news."
    },
    "16": {
      "L": "I made the nations to shake at the sound of his fall, when I cast him down to hell with them that descend into the pit: and all the trees of Eden, the choice and best of Lebanon, all that drink water, shall be comforted in the nether parts of the earth.",
      "M": "I made the nations shake at the sound of his fall when I cast him down to Sheol with those who go down to the Pit, and all the trees of Eden — the choicest and best of Lebanon, all who drink water — were comforted in the realm below.",
      "T": "The sound of the great cedar falling sent tremors through every nation — a sound so enormous it reached the underworld.\nWhen I cast Assyria down to Sheol, all the great trees of Eden — the other fallen empires already there — were comforted.\nA strange comfort: the comfort of company in ruin.\n'We are not the only great thing that fell.'\nEven in the land of the dead, the fallen await the arrival of companions who confirm their experience."
    },
    "17": {
      "L": "They also went down into hell with him unto them that be slain with the sword; and they that were his arm, that dwelt under his shadow in the midst of the heathen.",
      "M": "They too went down to Sheol with him — to those slain by the sword — even those who had been his arm and had dwelt under his shadow among the nations.",
      "T": "Into the Pit they went — not only the empire itself but all who had sustained it:\nthe allies who were its arm, the nations that lived in its shade.\nWhen the great cedar fell, the entire ecosystem that depended on it fell too.\nThis is the economics of empire: when the center collapses, the periphery collapses with it.\nThe sword makes no exceptions for the dependent."
    },
    "18": {
      "L": "To whom art thou thus like in glory and in greatness among the trees of Eden? yet shalt thou be brought down with the trees of Eden unto the nether parts of the earth: thou shalt lie in the midst of the uncircumcised with them that be slain by the sword. This is Pharaoh and all his multitude, saith the Lord GOD.",
      "M": "To whom are you like in glory and greatness among the trees of Eden? You too will be brought down with the trees of Eden to the realm below; you will lie among the uncircumcised with those slain by the sword. This is Pharaoh and all his multitude, declares the Lord GOD.",
      "T": "The question of verse 2 is now answered:\n'To whom do you compare yourself, Pharaoh?'\nTo the great cedar of Assyria. And look where Assyria is.\nYou will share its destination: down among the trees of Eden in the depths of the earth,\nlying with the uncircumcised dead — the nations who died in their pride, outside the covenant, cut down by the sword.\nThis is Pharaoh. This is all his people.\nThe Lord Yahweh declares it."
    }
  },
  "32": {
    "1": {
      "L": "And it came to pass in the twelfth year, in the twelfth month, in the first day of the month, that the word of the LORD came unto me, saying:",
      "M": "In the twelfth year, on the first day of the twelfth month, the word of the LORD came to me:",
      "T": "In the twelfth year, on the first of the twelfth month — the fall of Jerusalem now confirmed, the long-predicted judgment completed. Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, take up a lamentation for Pharaoh king of Egypt, and say unto him: Thou art like a young lion of the nations, and thou art as a whale in the seas: and thou camest forth with thy rivers, and troubledst the waters with thy feet, and fouledst their rivers.",
      "M": "Son of man, raise a lamentation over Pharaoh king of Egypt and say to him: You were like a young lion among the nations, and you were like a monster in the seas — you burst forth in your rivers and troubled the waters with your feet and muddied their rivers.",
      "T": "Son of man, raise a funeral lament over Pharaoh king of Egypt. Say to him:\nYou thought yourself a young lion among the nations — the apex predator, the one that commands fear.\nBut you were more like a sea-dragon — a great monster churning the waters,\nthrashing with your feet until every river ran muddy, the clear water fouled.\nYour power was real, but it was destructive. You did not bring order; you brought turbulence."
    },
    "3": {
      "L": "Thus saith the Lord GOD: I will therefore spread out my net over thee with a company of many people; and they shall bring thee up in my net.",
      "M": "Thus says the Lord GOD: I will throw my net over you with a host of many peoples, and they will haul you up in my net.",
      "T": "Thus says the Lord Yahweh: I am the fisherman now, not you.\nI spread my net — and the net is the armies of the nations, a host beyond counting.\nThey will haul you up out of the waters you called your domain."
    },
    "4": {
      "L": "Then will I leave thee upon the land, I will cast thee forth upon the open field, and will cause all the fowls of the heaven to remain upon thee, and I will fill the beasts of the whole earth with thee.",
      "M": "I will throw you on dry land and hurl you into the open field; I will cause all the birds of the sky to settle on you and fill all the beasts of the earth with you.",
      "T": "Then I will throw you onto dry land — you who lived in the water — and leave you in the open field,\nexposed, a carcass under the open sky.\nThe birds will land on you. The beasts will come from every direction.\nThe sea-dragon who terrified the waters will become carrion in the wilderness."
    },
    "5": {
      "L": "And I will lay thy flesh upon the mountains, and fill the valleys with thy height.",
      "M": "I will lay your flesh on the mountains and fill the valleys with your remains.",
      "T": "Your flesh — the substance of all your power — scattered on the mountains.\nThe valleys heaped with the mass of your fallen body.\nThe greatness that filled the sea will now fill the land, in pieces."
    },
    "6": {
      "L": "I will also water with thy blood the land wherein thou swimmest, even to the mountains; and the rivers shall be full of thee.",
      "M": "I will drench with your blood the land where you swim, even to the mountains; the ravines will be filled with you.",
      "T": "The rivers you once darkened and muddied will be colored by your blood.\nFrom the lowland to the mountains, the land soaked through.\nEvery ravine filled. The very geography will record your fall."
    },
    "7": {
      "L": "And when I shall put thee out, I will cover the heaven, and make the stars thereof dark; I will cover the sun with a cloud, and the moon shall not give her light.",
      "M": "When I blot you out I will cover the heavens and darken their stars; I will cover the sun with a cloud and the moon will not give its light.",
      "T": "When I blot you out — the verb used for erasing a name, annihilating an existence — I will cover the heavens.\nSun veiled. Stars dark. Moon silent.\nThis is the language of cosmic mourning, the register of the Day of the LORD (Joel 2:10; Amos 8:9).\nEgypt's fall is not merely political. It is a tear in the fabric of the world as the nations know it."
    },
    "8": {
      "L": "All the bright lights of heaven will I make dark over thee, and set darkness upon thy land, saith the Lord GOD.",
      "M": "All the luminous lights of the sky I will darken over you and bring darkness upon your land, declares the Lord GOD.",
      "T": "Every shining thing in the sky — darkened over you.\nDarkness on Egypt's land: not merely the metaphor of grief but the echo of the ninth plague (Exodus 10:21–23).\nGod's judgment on Egypt has this precedent. The Exodus pattern recurs.\nThe Lord Yahweh declares it."
    },
    "9": {
      "L": "I will also vex the hearts of many people, when I shall bring thy destruction among the nations, into the countries which thou hast not known.",
      "M": "I will trouble the hearts of many peoples when I bring your ruin among the nations, to countries you have not known.",
      "T": "Egypt's fall will send a shock through peoples far beyond Egypt's reach —\neven nations Egypt never encountered, countries Pharaoh never knew existed.\nThe sound of an empire's ruin travels far.\nThe hearts of the distant peoples will be troubled: if Egypt can fall, what can survive?"
    },
    "10": {
      "L": "Yea, I will make many people amazed at thee, and their kings shall be horribly afraid for thee, when I shall brandish my sword before them; and they shall tremble at every moment, every man for his own life, in the day of thy fall.",
      "M": "I will appall many peoples over you, and their kings will shudder with horror when I brandish my sword before them; they will tremble continually, each man for his own life, on the day of your fall.",
      "T": "Many peoples will be struck with appalled silence when Egypt falls.\nKings will shudder — not from grief for Egypt but from terror for themselves.\nWhen I brandish my sword before them, every king asks the same question:\nAm I next?\nOn the day of Egypt's fall, every ruler will be calculating his own position."
    },
    "11": {
      "L": "For thus saith the Lord GOD: The sword of the king of Babylon shall come upon thee.",
      "M": "For thus says the Lord GOD: The sword of the king of Babylon will come against you.",
      "T": "For thus says the Lord Yahweh: The instrument is named. The sword of the king of Babylon — Nebuchadnezzar — is coming. The cosmic dimensions of Egypt's fall described above now have a historical agent: the empire God raised to execute his purposes."
    },
    "12": {
      "L": "By the swords of the mighty will I cause thy multitude to fall, the terrible of the nations, all of them: and they shall spoil the pomp of Egypt, and all the multitude thereof shall be destroyed.",
      "M": "By the swords of the mighty I will cause your multitude to fall — the most ruthless of nations, all of them; they will destroy the pride of Egypt, and all its multitude will be wiped out.",
      "T": "Egypt's vast army — the multitude Ezekiel always pairs with Pharaoh as the measure of Egypt's greatness — will fall to the swords of the most pitiless warriors in the world.\nAll of it: the pride, the pomp, the ceremony, the accumulated splendor of millennia.\nDestroyed by the very ruthlessness that Egypt itself had once exercised against Israel."
    },
    "13": {
      "L": "I will destroy also all the beasts thereof from beside the great waters; neither shall the foot of man trouble them any more, nor the hoofs of beasts trouble them.",
      "M": "I will destroy all its livestock from beside the great waters; no human foot will trouble them anymore, nor will the hooves of cattle disturb them.",
      "T": "Even the animals at the Nile — the livestock, the herds along the great river and delta marshes — will be destroyed.\nNo foot will muddy the water. No hoof will stir the reed-beds.\nThe Egypt that lived by the Nile will be stilled.\nThe great river will be untroubled because there will be no one left to trouble it."
    },
    "14": {
      "L": "Then will I make their waters deep, and cause their rivers to run like oil, saith the Lord GOD.",
      "M": "Then I will let their waters settle and cause their rivers to flow like oil, declares the Lord GOD.",
      "T": "And then, in the silence after judgment, the waters will settle:\nDeep and still — no armies stirring the mud, no Pharaoh thrashing like a dragon.\nThe rivers flowing smooth as oil: undisturbed, calm, unhurried.\nThe peace of desolation.\nThe Lord Yahweh says it."
    },
    "15": {
      "L": "When I shall make the land of Egypt desolate, and the country shall be destitute of that whereof it was full, when I shall smite all them that dwell therein, then shall they know that I am the LORD.",
      "M": "When I make the land of Egypt desolate and the land is stripped of everything it was filled with, when I strike down all who dwell in it, then they shall know that I am the LORD.",
      "T": "When I strip Egypt of everything — the fullness of the land emptied, the people struck down, the cities silent —\nthen they will know that I am Yahweh.\nThe recognition formula that has closed oracle after oracle now closes this one.\nKnowledge of God arrives through the very events that seemed to deny God's existence."
    },
    "16": {
      "L": "This is the lamentation wherewith they shall lament her: the daughters of the nations shall lament her: they shall lament for her, even for Egypt, and for all her multitude, saith the Lord GOD.",
      "M": "This is the lamentation they will sing over her; the daughters of the nations will sing this lamentation over Egypt and all its multitude, declares the Lord GOD.",
      "T": "This is the official lament — the qînāh to be sung.\nThe women of the nations will take it up: the designated mourners, the ones trained to voice communal grief.\nThey will sing it over Egypt and all its people.\nThe Lord Yahweh authorizes the lament: the fall of Egypt is great enough to deserve a formal song."
    },
    "17": {
      "L": "It came to pass also in the twelfth year, in the fifteenth day of the month, that the word of the LORD came unto me, saying:",
      "M": "In the twelfth year, on the fifteenth of the month, the word of the LORD came to me:",
      "T": "In the twelfth year, on the fifteenth of the month — two weeks after the first oracle of this chapter. Yahweh's word came to me again:"
    },
    "18": {
      "L": "Son of man, wail for the multitude of Egypt, and cast them down, even her, and the daughters of the famous nations, unto the nether parts of the earth, with them that go down into the pit.",
      "M": "Son of man, wail for the multitude of Egypt and bring them down — both Egypt and the daughters of the majestic nations — to the depths of the earth, with those who go down to the Pit.",
      "T": "Son of man, mourn aloud for Egypt's multitude. And then — with your mourning voice — send them down:\nEgypt and all her people, alongside the daughters of the great nations of the world,\ndown to the depths of the earth,\ndown with all who have preceded them to the Pit.\nThe prophet's voice participates in the judgment it announces."
    },
    "19": {
      "L": "Whom dost thou pass in beauty? go down, and be thou laid with the uncircumcised.",
      "M": "Whom do you surpass in beauty? Go down and lie with the uncircumcised.",
      "T": "The taunt is bitter: 'Whom do you surpass in beauty?'\nBeauty was Egypt's claim — the monuments, the culture, the civilization of the Nile.\nAnswer: no one. Go down. Lie with the uncircumcised.\nThe uncircumcised dead are those outside the covenant — those who died without the sign of God's people.\nBeauty does not buy a better death. Pride does not earn a better grave."
    },
    "20": {
      "L": "They shall fall in the midst of them that are slain by the sword: she is delivered to the sword: draw her and all her multitudes.",
      "M": "They will fall among those slain by the sword; Egypt is delivered to the sword — draw her down with all her multitude.",
      "T": "Egypt falls among the slain. The sword that cut down nation after nation does not pause at Egypt's border.\nDraw her down — the command to the agents of judgment:\nbring Egypt and all her people down into the company of the dead.\nThe sword shows no favoritism."
    },
    "21": {
      "L": "The strong among the mighty shall speak to him out of the midst of hell with them that help him: they are gone down, they lie uncircumcised, slain by the sword.",
      "M": "The mightiest warriors will speak to him from the midst of Sheol — they and his helpers have gone down; they lie uncircumcised, slain by the sword.",
      "T": "The great warriors of the underworld — the heroes of fallen empires who preceded Egypt to Sheol —\nspeak from the depths:\n'You and your helpers have come down to us.\nYou lie as we lie — uncircumcised, fallen by the sword.\nWelcome to where greatness ends up.'\nThe underworld has its own dark solidarity of the mighty fallen."
    },
    "22": {
      "L": "Asshur is there and all her company: his graves are about him: all of them slain, fallen by the sword:",
      "M": "Assyria is there with all its company; their graves surround it — all of them slain, fallen by the sword.",
      "T": "First among the company in Sheol: Assyria.\nThe greatest empire that had preceded Egypt in power and terror,\nnow lying in Sheol with its graves surrounding it:\nall the slain, all the fallen warriors, the whole apparatus of Assyrian conquest.\nSilent."
    },
    "23": {
      "L": "Whose graves are set in the sides of the pit, and her company is round about her grave: all of them slain, fallen by the sword, which caused terror in the land of the living.",
      "M": "Its graves are in the depths of the Pit, its company gathered around its tomb — all slain, fallen by the sword, who had spread terror in the land of the living.",
      "T": "Assyria's graves occupy the deepest part of the Pit — the place of grim precedence,\nbecause Assyria was the nation that most terrified the ancient world.\nAll its company surrounding it in death as in life.\nAll fallen by the sword.\nAll of them who once made every living nation tremble with their name.\nNow silent. Now equal to every other fallen nation."
    },
    "24": {
      "L": "There is Elam and all her multitude round about her grave, all of them slain, fallen by the sword, which are gone down uncircumcised into the nether parts of the earth, which caused their terror in the land of the living; yet have they borne their shame with them that go down to the pit.",
      "M": "Elam is there with all its multitude around its tomb — all slain, fallen by the sword, who went down uncircumcised to the depths of the earth, who had spread terror in the land of the living; they bear their shame with those who go down to the Pit.",
      "T": "Elam — the ancient empire east of Babylon, once formidable, now assembled in the Pit.\nAll its multitude. All the warriors who had spread terror while they lived.\nThey went down uncircumcised — outside the covenant, outside the mercy of the God they did not know.\nThey bear their shame: the shame of all who boasted in their power\nand found it counted for nothing before the God who governs all nations."
    },
    "25": {
      "L": "They have set her a bed in the midst of the slain with all her multitude: her graves are round about him: all of them uncircumcised, slain by the sword: though their terror was caused in the land of the living, yet have they borne their shame with them that go down to the pit: he is put in the midst of them that be slain.",
      "M": "They have made her a bed among the slain with all her multitude; their graves surround it — all of them uncircumcised, slain by the sword. Though they spread terror in the land of the living, they bear their shame with those who go down to the Pit; Elam is placed among the slain.",
      "T": "A bed prepared among the slain — the grave of Elam among the graves of the fallen.\nSurrounded by its own dead, each one uncircumcised, each fallen by the sword.\nThe terror they caused in life — real terror, the kind that changed history —\nhas been exchanged for shame in death.\nThe Pit levels everything: the terrifying and the terrified lie side by side."
    },
    "26": {
      "L": "There is Meshech, Tubal, and all her multitude: her graves are round about him: all of them uncircumcised, slain by the sword, though they caused their terror in the land of the living.",
      "M": "Meshech and Tubal are there with all their multitude; their graves surround them — all of them uncircumcised, slain by the sword, though they spread terror in the land of the living.",
      "T": "Meshech and Tubal — the peoples of Asia Minor and the Black Sea,\nthe nations who sold human beings in Tyre's slave markets (27:13),\nwhose names were synonymous with the outer edges of the known world.\nAll there.\nAll uncircumcised.\nAll fallen by the sword.\nTheir terror in the land of the living was real; their graves are as undistinguished as anyone else's in the Pit."
    },
    "27": {
      "L": "And they shall not lie with the mighty that are fallen of the uncircumcised, which are gone down to hell with their weapons of war: and they have laid their swords under their heads, and their iniquities shall be upon their bones, though they were the terror of the mighty in the land of the living.",
      "M": "Do they not lie with the fallen warriors of old who went down to Sheol with their weapons of war, their swords placed under their heads and their shields covering their bones — those who were the terror of the mighty in the land of the living?",
      "T": "Unlike the ancient heroes of old who were buried with their weapons — swords under their heads, shields on their bodies, honored in death as warriors who fell honorably —\nMeshech and Tubal receive no such honor.\nTheir iniquity rests on their bones where weapons would have lain.\nThere is a way to fall that carries the dignity of a warrior honestly defeated;\nand a way to fall that carries only the weight of what you did wrong.\nThe distinction between an honored death and a shamed one persists even into Sheol."
    },
    "28": {
      "L": "Yea, thou shalt be broken in the midst of the uncircumcised, and shalt lie with them that are slain with the sword.",
      "M": "You too will be shattered among the uncircumcised and lie with those slain by the sword.",
      "T": "And you, Egypt — you are in this company.\nYou will be shattered among the uncircumcised, lying with those the sword cut down.\nNot the honored burial of the ancient heroes. Not weapons and shields.\nAmong them — the dishonored fallen. That is your place."
    },
    "29": {
      "L": "There is Edom, her kings, and all her princes, which with their might are laid by them that were slain by the sword: they shall lie with the uncircumcised, and with them that go down to the pit.",
      "M": "Edom is there — its kings and all its princes — laid with those slain by the sword despite their might; they lie with the uncircumcised and those who go down to the Pit.",
      "T": "Edom is there — the kings, the princes, the whole ruling class that Edom was proud of.\nThey went down with all their might, slain by the sword.\nEdom, which attacked Judah in her hour of collapse, now lies with the uncircumcised.\nThe brother-nation that despised the covenant goes down with all who lived outside the covenant."
    },
    "30": {
      "L": "There be the princes of the north, all of them, and all the Zidonians, which are gone down with the slain; with their terror they are ashamed of their might; and they lie uncircumcised with them that be slain by the sword, and bear their shame with them that go down to the pit.",
      "M": "There are all the princes of the north and all the Sidonians who have gone down with the slain — despite the terror they inspired, they are put to shame in their might; they lie uncircumcised with those slain by the sword and bear their shame with those who go down to the Pit.",
      "T": "The princes of the north — the rulers of the Levantine and Anatolian coasts — and Sidon, Tyre's great Phoenician neighbor:\nall of them, the whole complex of northern maritime civilization, gone down to the slain.\nThe terror they inspired in life: now they are ashamed of it.\nThe might they were proud of has not protected them.\nThey lie uncircumcised, carrying their shame, among those the sword cut down."
    },
    "31": {
      "L": "Pharaoh shall see them, and shall be comforted over all his multitude, even Pharaoh and all his army slain by the sword, saith the Lord GOD.",
      "M": "When Pharaoh sees them he will be comforted over all his multitude — Pharaoh and all his army slain by the sword, declares the Lord GOD.",
      "T": "When Pharaoh arrives in Sheol and sees the assembled company —\nAssyria, Elam, Meshech, Tubal, Edom, the princes of the north, Sidon —\nhe will be comforted.\nThis is the dark comfort of the underworld: you are not alone in falling.\nThe greatest empires that preceded you are already here.\nYou are in famous company.\nThe Lord Yahweh says it — which means even this grim comfort is within God's governance of history."
    },
    "32": {
      "L": "For I have caused my terror in the land of the living: and he shall be laid in the midst of the uncircumcised with them that are slain with the sword, even Pharaoh and all his multitude, saith the Lord GOD.",
      "M": "For I spread his terror in the land of the living; yet Pharaoh and all his multitude will be laid among the uncircumcised with those slain by the sword, declares the Lord GOD.",
      "T": "For I — Yahweh — spread the terror of Egypt across the land of the living.\nGod's sovereign acknowledgment: the terror Egypt caused was not outside his purposes.\nYet Pharaoh and all his army will lie among the uncircumcised, fallen by the sword.\nThe power God lent to Egypt for his purposes does not exempt Egypt from judgment.\nThe Lord Yahweh declares it — the final word of the underworld vision."
    }
  },
  "33": {
    "1": {
      "L": "Again the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "2": {
      "L": "Son of man, speak to the children of thy people, and say unto them: When I bring the sword upon a land, if the people of the land take a man of their coasts, and set him for their watchman:",
      "M": "Son of man, speak to your people and say to them: When I bring the sword against a land, and the people of that land take one man from among them and set him as their watchman —",
      "T": "Son of man, bring this parable to your people:\nWhen God sends the sword against a land — when judgment is approaching — what does a responsible community do?\nThey appoint a watchman: one person stationed at the edge, watching the horizon, responsible to warn everyone else of what he alone can see."
    },
    "3": {
      "L": "If when he seeth the sword come upon the land, he blow the trumpet, and warn the people;",
      "M": "when he sees the sword coming against the land and blows the trumpet to warn the people —",
      "T": "When the watchman sees the sword coming, he blows the trumpet.\nThe alarm goes out. Every ear in the city hears.\nThis is what the watchman is stationed for: to see what others cannot see yet, and to make the warning impossible to ignore."
    },
    "4": {
      "L": "Then whosoever heareth the sound of the trumpet, and taketh not warning; if the sword come, and take him away, his blood shall be upon his own head.",
      "M": "then if anyone hears the trumpet and does not take warning, and the sword comes and takes him away — his blood is on his own head.",
      "T": "If the alarm sounds and someone chooses not to respond — dismisses the warning, stays in place — and then the sword comes and takes that person:\nthe blood is on their own head.\nThe watchman fulfilled his duty. The choice not to respond was the individual's own choice.\nGod takes human decisions seriously; the responsibility is not transferred."
    },
    "5": {
      "L": "He heard the sound of the trumpet, and took not warning; his blood shall be upon him. But he that taketh warning shall deliver his soul.",
      "M": "He heard the trumpet and did not take warning; his blood is on himself. But whoever takes warning will save his life.",
      "T": "He heard it. He cannot claim he did not hear. His blood is on himself.\nBut the positive side of the parable is equally real: the one who takes warning, who hears and acts —\nthat person saves his life.\nResponsiveness to warning is not weakness; it is wisdom. It is the response the warning was designed to produce."
    },
    "6": {
      "L": "But if the watchman see the sword come, and blow not the trumpet, and the people be not warned; if the sword come, and take any person from among them, he is taken away in his iniquity; but his blood will I require at the watchman's hand.",
      "M": "But if the watchman sees the sword coming and does not blow the trumpet, and the people are not warned, and the sword comes and takes any of them — they are taken in their own iniquity, but their blood I will require from the watchman's hand.",
      "T": "The other side of the parable:\nIf the watchman sees the danger and says nothing — if he stays silent while the threat approaches —\nand someone dies who might have been warned:\nthe person died in their own sin, yes — but the watchman is accountable for the silence.\nI will require their blood from the watchman's hand.\nThe prophet who sees and does not speak is not neutral. Silence is an act with consequences."
    },
    "7": {
      "L": "So thou, O son of man, I have set thee a watchman unto the house of Israel; therefore thou shalt hear the word at my mouth, and warn them from me.",
      "M": "So you, son of man — I have made you a watchman for the house of Israel. When you hear a word from my mouth, you will warn them on my behalf.",
      "T": "This is the application:\nYou, Ezekiel — I have positioned you as the watchman for Israel.\nEvery word I speak to you is the alarm you must sound.\nYou do not speak your own words; you speak mine.\nThe burden is the word I give you; the responsibility is to give it faithfully and fully."
    },
    "8": {
      "L": "When I say unto the wicked, O wicked man, thou shalt surely die; if thou dost not speak to warn the wicked from his way, that wicked man shall die in his iniquity; but his blood will I require at thine hand.",
      "M": "When I say to the wicked, 'You will surely die,' and you do not speak to warn him from his way, that wicked man will die in his iniquity; but his blood I will require from your hand.",
      "T": "When I render a verdict on the wicked — 'You will die; this path ends in death' — and you hear that verdict but do not pass it on:\nthe wicked person dies in the guilt of their own sin.\nBut I will hold you accountable for their blood.\nThe warning unfulfilled is not a neutral event. It is a failure with consequences as real as the sword."
    },
    "9": {
      "L": "Nevertheless, if thou warn the wicked of his way to turn from it; if he do not turn from his way, he shall die in his iniquity; but thou hast delivered thy soul.",
      "M": "But if you warn the wicked to turn from his way and he does not turn from it, he will die in his iniquity; but you have saved your life.",
      "T": "But if you warn him — if you faithfully speak what I have given you and call him to turn from his way —\nand he still refuses:\nhe dies in his own sin. You are clear.\nYou did what a watchman does: you saw, you sounded the alarm, you called for response.\nThe rest was his choice. Your soul is delivered."
    },
    "10": {
      "L": "Therefore, O thou son of man, speak unto the house of Israel; Thus ye speak, saying: If our transgressions and our sins be upon us, and we pine away in them, how should we then live?",
      "M": "And you, son of man, say to the house of Israel: This is what you are saying: 'Our transgressions and our sins are upon us; we are wasting away because of them — how then can we live?'",
      "T": "And this is what you are to say to Israel — because this is what they are already saying among themselves:\n'We are crushed under the weight of our own sins. Our transgressions press down on us like stones.\nWe are wasting away. How, in God's name, can we live?'\nThis is the cry of the exiles after Jerusalem has fallen: not defiance, but despair.\nIs there any hope for people this guilty?"
    },
    "11": {
      "L": "Say unto them, As I live, saith the Lord GOD, I have no pleasure in the death of the wicked; but that the wicked turn from his way and live: turn ye, turn ye from your evil ways; for why will ye die, O house of Israel?",
      "M": "Say to them: As I live, declares the Lord GOD, I take no pleasure in the death of the wicked, but rather that the wicked turn from his way and live. Turn back, turn back from your evil ways! Why will you die, O house of Israel?",
      "T": "Here is God's answer — sworn on his own life:\nI take no pleasure in the death of the wicked.\nLet that be heard clearly: God is not waiting for Israel to fail so he can execute the sentence.\nWhat God wants — what God is pleading for, urgently —\nis that the wicked turn from his way and live.\nTurn back. Turn back from your evil ways.\nThe repetition is urgent, almost desperate:\nWhy will you die? Why will you die, Israel?\nThe God who just announced judgment is the same God who cannot stop calling people back to life."
    },
    "12": {
      "L": "Therefore, thou son of man, say unto the children of thy people: The righteousness of the righteous shall not deliver him in the day of his transgression: as for the wickedness of the wicked, he shall not fall thereby in the day that he turneth from his wickedness; neither shall the righteous be able to live for his righteousness in the day that he sinneth.",
      "M": "And you, son of man, say to your people: The righteousness of the righteous will not deliver him in the day he transgresses; and the wickedness of the wicked — he will not fall because of it in the day he turns from it; the righteous will not be able to live by his former righteousness in the day he sins.",
      "T": "Here is the principle:\nPast righteousness does not protect present sin.\nPast sin does not block present repentance.\nThe ledger of a life is not fixed by the past; it is active in the present moment.\nIf a righteous person turns away and sins, the old record of goodness will not save them.\nIf a wicked person turns away from wickedness, the old record of sin will not condemn them.\nGod's governance is dynamic, not static. This is both a warning and an open door."
    },
    "13": {
      "L": "When I shall say to the righteous, that he shall surely live; if he trust to his own righteousness, and commit iniquity, all his righteousnesses shall not be remembered; but for his iniquity that he hath committed, he shall die for it.",
      "M": "When I say to the righteous that he shall surely live, but he trusts in his own righteousness and commits iniquity, none of his righteous deeds will be remembered — he will die in the iniquity he committed.",
      "T": "The danger on one side:\nI tell a righteous person: You shall live.\nAnd the person hears that and relaxes,\nstarts to coast on the track record, starts to trust the past instead of the present relationship,\nstarts to commit iniquity.\nAll the righteousness — all of it — will not be remembered.\nHe will die for the iniquity he is now committing.\nPast righteousness leveraged as security becomes a trap."
    },
    "14": {
      "L": "Again, when I say unto the wicked, Thou shalt surely die; if he turn from his sin, and do that which is lawful and right;",
      "M": "But when I say to the wicked, 'You shall surely die,' if he turns from his sin and does what is just and right —",
      "T": "The open door on the other side:\nI pronounce sentence on the wicked: you shall die.\nAnd then the wicked person — hearing the sentence — turns.\nDoes what is just and right."
    },
    "15": {
      "L": "If the wicked restore the pledge, give again that he had robbed, walk in the statutes of life, without committing iniquity; he shall surely live, he shall not die.",
      "M": "if the wicked returns the pledge, repays what he has stolen, walks in the statutes of life without committing iniquity — he shall surely live; he shall not die.",
      "T": "The turning is not merely emotional. It is concrete:\nReturn the pledge taken as collateral — the poor person's cloak.\nRepay what was stolen.\nWalk in the statutes of life — the specific behavioral shape of covenant faithfulness.\nDo this, and not die.\nThe reversal is real. The sentence is commuted. Life is genuinely available."
    },
    "16": {
      "L": "None of his sins that he hath committed shall be mentioned unto him: he hath done that which is lawful and right; he shall surely live.",
      "M": "None of the sins he has committed will be held against him; he has done what is just and right — he shall surely live.",
      "T": "None of the sins will be counted against him.\nNot mentioned. Not charged. Not held over him as leverage or condemnation.\nThis is God's accounting: when a person turns, the whole past is no longer the operative fact.\nHe has done what is just and right.\nHe shall live.\nThe promise is as definitive as the sentence was."
    },
    "17": {
      "L": "Yet the children of thy people say: The way of the Lord is not equal: but as for them, their way is not equal.",
      "M": "Yet your people say, 'The way of the Lord is not fair.' But it is their way that is not fair.",
      "T": "And yet — Israel's response to all this is: 'That's not fair.'\nYour people say: God's way is inconsistent, unpredictable, arbitrary.\nThe reversal: it is their way that is not fair.\nGod's readiness to reverse judgment on repentance, to let the past be past when someone turns —\nthis is not inconsistency. It is grace.\nThe accusation of unfairness against God is itself the expression of the unfairness within the accuser."
    },
    "18": {
      "L": "When the righteous turneth from his righteousness, and committeth iniquity, he shall even die thereby.",
      "M": "When a righteous person turns from his righteousness and commits iniquity, he will die because of it.",
      "T": "The righteous who turns away dies for it.\nThe principle holds in both directions without exception.\nGod's governance is consistent in this: what you are doing now matters more than what you did before."
    },
    "19": {
      "L": "But if the wicked turn from his wickedness, and do that which is lawful and right, he shall live thereby.",
      "M": "But if the wicked turns from his wickedness and does what is just and right, he shall live because of it.",
      "T": "The wicked who turns lives for it.\nRepeated in both forms because both forms need to be believed:\nNeither past righteousness nor past wickedness is the final word.\nThe present turning is what God responds to.\nThis is hope — not sentimental hope, but a promise grounded in God's own character."
    },
    "20": {
      "L": "Yet ye say: The way of the Lord is not equal. O ye house of Israel, I will judge you every one after his ways.",
      "M": "Yet you say, 'The way of the Lord is not fair.' O house of Israel, I will judge each of you according to your ways.",
      "T": "Still they say it: God's way is not fair.\nThe answer is simple: I will judge each person according to their ways.\nNot the ways of their ancestors. Not the collective guilt of the nation. Not the old record.\nYours. Your choices. Your turnings. Your refusals to turn.\nThis is both the most demanding and the most hopeful thing God could say to people who have just watched Jerusalem fall and wonder if they have any future at all."
    },
    "21": {
      "L": "And it came to pass in the twelfth year of our captivity, in the tenth month, in the fifth day of the month, that one that had escaped out of Jerusalem came unto me, saying: The city is smitten.",
      "M": "In the twelfth year of our exile, in the tenth month, on the fifth day of the month, a fugitive from Jerusalem came to me and said, 'The city has been struck down.'",
      "T": "In the twelfth year of our exile, on the fifth of the tenth month — a fugitive arrived from Jerusalem.\nHe had made it out. He had survived the journey.\nHe carried four words: 'The city is struck down.'\nThis is the moment Ezekiel's entire ministry had been building toward.\nFor years he had announced what no one wanted to believe. Now it was confirmed by a witness.\nJerusalem had fallen. The sanctuary was destroyed. The dynasty was ended.\nThe watchman's warnings had been true."
    },
    "22": {
      "L": "Now the hand of the LORD was upon me in the evening, afore he that was escaped came; and had opened my mouth, until he came to me in the morning; and my mouth was opened, and I was no more dumb.",
      "M": "Now the hand of the LORD had been upon me in the evening before the fugitive arrived, and he had opened my mouth by the time the man came to me in the morning; my mouth was opened and I was silent no more.",
      "T": "The night before the fugitive arrived, God's hand had already touched Ezekiel.\nHis mouth — which God had sealed for the years of his ministry as a sign of judgment (cf. 3:26; 24:27) —\nwas opened before the man arrived.\nBy morning, when the fugitive spoke his four words, the seal was already gone.\nEzekiel was no longer mute.\nThe period of sealed silence was complete. Jerusalem had fallen. The sign was fulfilled.\nNow Ezekiel could speak freely, fully, without restraint."
    },
    "23": {
      "L": "Then the word of the LORD came unto me, saying:",
      "M": "Then the word of the LORD came to me:",
      "T": "And then Yahweh's word came to me:"
    },
    "24": {
      "L": "Son of man, they that inhabit those wastes of the land of Israel speak, saying: Abraham was one, and he inherited the land: but we are many; the land is given us for inheritance.",
      "M": "Son of man, the people living in those ruins of the land of Israel are saying: 'Abraham was one man, yet he possessed the land; but we are many — the land is surely given to us as our possession.'",
      "T": "The people left behind in the ruined land — those not taken to Babylon, the survivors of the siege — have drawn a theological conclusion:\n'Abraham was a single man, and God gave him the land as his inheritance.\nWe are many. Therefore the land is surely ours by even stronger right.'\nThe argument sounds pious. It invokes the founding patriarch. It appeals to covenant promise.\nBut it ignores one thing: Abraham was called and obedient. These people are survivors of God's judgment, still in their sins."
    },
    "25": {
      "L": "Wherefore say unto them: Thus saith the Lord GOD: Ye eat with the blood, and lift up your eyes toward your idols, and shed blood: and shall ye possess the land?",
      "M": "Therefore say to them: Thus says the Lord GOD: You eat flesh with the blood in it, you lift your eyes to your idols, you shed blood — and do you expect to possess the land?",
      "T": "God's answer dismantles the argument by describing what these people actually do:\nYou eat meat with the blood still in it — violating the most foundational covenant restriction (Lev. 17:10–14).\nYou lift your eyes to your idols — still, after everything.\nYou shed blood — the inversion of every covenant value.\nAnd you want to make a claim about inheriting the land?\nThe comparison with Abraham is not yours to make."
    },
    "26": {
      "L": "Ye stand upon your sword, ye work abomination, and ye defile every one his neighbour's wife: and shall ye possess the land?",
      "M": "You rely on your sword, you commit abominations, and each of you defiles his neighbor's wife — and do you expect to possess the land?",
      "T": "Your life is built on the sword — violence is your operating principle.\nYou commit the abominations God has prohibited.\nYou violate your neighbor's marriage.\nAnd you are making a theological argument about your right to the land?\nThe argument requires a life that at least resembles the covenant.\nYours does not."
    },
    "27": {
      "L": "Say thou thus unto them: Thus saith the Lord GOD: As I live, surely they that are in the wastes shall fall by the sword, and him that is in the open field will I give to the beasts to be devoured, and they that be in the forts and in the caves shall die of the pestilence.",
      "M": "Say this to them: Thus says the Lord GOD: As I live, those in the ruins will fall by the sword; those in the open field I will give to the beasts to be devoured; those in strongholds and caves will die by pestilence.",
      "T": "Thus says the Lord Yahweh — sworn on his own life:\nThose in the ruins: the sword.\nThose in the open fields: the beasts.\nThose who retreated to fortresses and caves — those who think they have found safety in hiding:\nthe plague.\nAll three instruments of the covenant curses (Leviticus 26).\nThe land is not theirs to inherit. The judgment has not finished."
    },
    "28": {
      "L": "For I will lay the land most desolate, and the pomp of her strength shall cease; and the mountains of Israel shall be desolate, that none shall pass through.",
      "M": "I will make the land a desolate waste, and her arrogant pride will cease; the mountains of Israel will be made desolate so that no one passes through.",
      "T": "I will make the land utterly desolate.\nThe pride and strength that made it feel permanent, that made these survivors believe they could stay and build:\nit will cease.\nThe mountains of Israel — stripped bare, emptied, with no one crossing them.\nThe arrogant presumption that the land was theirs will be answered by the silence of a land with no one in it."
    },
    "29": {
      "L": "Then shall they know that I am the LORD, when I have laid the land most desolate because of all their abominations which they have committed.",
      "M": "Then they will know that I am the LORD when I have made the land a desolate waste because of all the abominations they have committed.",
      "T": "Then — when the land is empty and the ruins are complete and the silence is absolute —\nthey will know that I am Yahweh.\nThe recognition comes through the very thing they refused to believe.\nKnowledge of God bought at the price of desolation is the most painful knowledge there is,\nbut it is knowledge."
    },
    "30": {
      "L": "Also, thou son of man, the children of thy people still are talking against thee by the walls and in the doors of the houses, and speak one to another, every one to his brother, saying: Come, I pray you, and hear what is the word that cometh forth from the LORD.",
      "M": "And you, son of man — your people are talking about you by the walls and at the doorways of houses; they say to one another, each to his brother: 'Come, let us hear what word is coming from the LORD.'",
      "T": "And now God tells Ezekiel what is happening in the community around him:\nBy the walls, at the doorways — wherever people gather — they talk about him.\nAnd what they say is: 'Come, let's go hear what Yahweh says through the prophet.'\nThis sounds like the right response. It sounds like faith. But listen carefully to what God says next."
    },
    "31": {
      "L": "And they come unto thee as the people cometh, and they sit before thee as my people, and they hear thy words, but they will not do them: for with their mouth they shew much love, but their heart goeth after their covetousness.",
      "M": "They come to you as the people come, and they sit before you as my people and hear your words — but they will not act on them. With their mouths they express devotion, but their hearts pursue dishonest gain.",
      "T": "They come. They sit before you as if they were the people of God — attentive, reverent, leaning in.\nThey hear your words. Really hear them. Follow the argument. Respond with what sounds like devotion.\nBut they will not do them.\nThe mouth professes love for God; the heart runs after profit.\nThis is the exact shape of hollow religion: the forms of covenant kept, the life of covenant absent.\nEzekiel hears the same diagnosis Isaiah received (Isa. 29:13): this people honors me with their lips."
    },
    "32": {
      "L": "And lo, thou art unto them as a very lovely song of one that hath a pleasant voice, and can play well on an instrument: for they hear thy words, but they do them not.",
      "M": "You are to them like a love song sung by one with a beautiful voice and skilled on an instrument — they hear your words but will not act on them.",
      "T": "This is the most devastating image:\nEzekiel to his audience is like a gifted musician performing a popular song.\nThe voice is beautiful. The craft is evident. The audience is pleased.\nThey come for the experience of hearing a great performer give voice to the word of God.\nThe content is beside the point.\nThey are not coming to be confronted or changed or called to repentance.\nThey are coming for the aesthetic pleasure of hearing the word of God delivered well.\nThe prophet is entertainment. The message is music. Nothing changes."
    },
    "33": {
      "L": "And when this cometh to pass, (lo, it will come,) then shall they know that a prophet hath been among them.",
      "M": "But when it comes — and it will come — then they will know that a prophet has been among them.",
      "T": "But it will come.\nAll of it — every word Ezekiel spoke, every judgment announced, every warning given while they sat and enjoyed the performance:\nit will come to pass.\nAnd when it does — when the words they heard as music become history they live through —\nthen they will know that a prophet was among them.\nNot that they responded. Not that they repented. But that the word was true.\nThe final vindication of the prophet is not applause but fulfillment."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 31–33 written.')

if __name__ == '__main__':
    main()
