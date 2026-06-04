"""
MKT Revelation chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-7-12.py

Translation decisions:
- G721 (ἀρνίον): "Lamb" (L/M/T) — the central image of Revelation; always capitalized as a title
- G2342 (θηρίον): "beast" (L/M) / "the Beast" where it functions as a proper antagonist title (T ch.11–12) — the political-religious power opposed to God
- G1404 (δράκων): "dragon" (L/M/T) — never "serpent" except at Rev 12:9 where ὁ ὄφις is also present
- G3789 (ὄφις): "serpent" (L/M/T) — the ancient serpent of Eden recalled; both names appear in 12:9
- G12 (ἄβυσσος): "bottomless pit" (L/M) / "abyss" (T) — the spatial metaphor of the deep prison
- G4151 (πνεῦμα): "Spirit" (capitalized, divine) in the phrase "Spirit of life" (11:11); lowercase elsewhere when ambiguous
- G4102 (πίστις): not prominently contested in chs. 7–12; rendered "faith"/"faithfulness" contextually
- G166 (αἰώνιος): "for ever and ever" (L) following αἰῶνας τῶν αἰώνων idiom; "throughout all the ages of ages" (T) to surface the temporal fullness
- G2962 (κύριος): "Lord" (L/M/T) — divine title; always capitalized
- G3466 (μυστήριον): "mystery" (L/M/T) — the divine plan hidden and now being revealed (10:7)
- G4536 (σάλπιγξ/σαλπίζω): "trumpet" / "sounded" (L/M/T)
- G4973 (σφραγίς): "seal" (L/M/T) — the protective mark of ownership
- G2347 (θλῖψις): "tribulation" (L) / "tribulation" (M) / "ordeal" or "great tribulation" (T)
- G3841 (παντοκράτωρ): "Almighty" (L/M/T)
- G932 (βασιλεία): "kingdom" (L/M) / "kingdom" or "reign" (T depending on context)
- G5547 (Χριστός): "Christ" (L/M/T) — not rendered "Messiah" in this translation
- G26 (ἀγάπη): not prominent in chs. 7–12; see notes for chs. 1–3 (other agent)
- G1343 (δικαιοσύνη): not prominent in chs. 7–12
- G4561 (σάρξ): not present in chs. 7–12
- G3056 (λόγος): "word" (lowercase) in 12:11 "word of their testimony"; reserved for "Word" (capital) at 19:13
- H3068 (יהוה): not applicable — Greek text
- Divine name: "Lord God Almighty" for Κύριε ὁ θεὸς ὁ παντοκράτωρ (11:17)
- Two witnesses (ch. 11): intentionally not identified; text leaves them as figures. No identification note added.
- "Woe" (G3759 οὐαί): kept as "Woe" (L/M), rendered "Disaster" (T) to register the proclamation force
- Chapter 12 woman: rendered without typological identification — text is symbol-first
- 144,000 (ch. 7): rendered numerically, not explained; the list of tribes is translated exactly
- "Tabernacle/dwell over" (G4637 σκηνόω): "shelter with his presence" (M) / "spread his dwelling over them like a canopy" (T)
- "Smoke of a great furnace" (9:2): "furnace" not "kiln" — alludes to Egyptian bondage (Gen 19 / Exod imagery)
- Abaddon / Apollyon (9:11): both names given with English glosses in T
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


REVELATION = {
  "7": {
    "1": {
      "L": "After this I saw four angels standing on the four corners of the earth, holding the four winds of the earth, that wind should not blow on the earth, nor on the sea, nor on any tree.",
      "M": "After this I saw four angels standing at the four corners of the earth, holding back the four winds so that no wind would blow on the earth, or on the sea, or against any tree.",
      "T": "After this vision I saw four angels posted at the four corners of the earth, gripping the four winds and preventing any wind from striking the land, the sea, or a single tree."
    },
    "2": {
      "L": "And I saw another angel ascending from the rising of the sun, having the seal of the living God; and he cried with a loud voice to the four angels to whom it was given to harm the earth and the sea,",
      "M": "Then I saw another angel ascending from the east, holding the seal of the living God, and he called out with a loud voice to the four angels who had been given power to harm the earth and the sea:",
      "T": "Then another angel rose from where the sun comes up, bearing the seal of the living God. He cried out in a loud voice to the four angels who had been authorized to harm the earth and sea:"
    },
    "3": {
      "L": "saying, 'Do not harm the earth, nor the sea, nor the trees, until we have sealed the servants of our God on their foreheads.'",
      "M": "'Do not harm the earth or the sea or the trees until we have sealed the servants of our God on their foreheads.'",
      "T": "'Hold back! Do not strike the earth, the sea, or the trees until we have set the seal of God on the foreheads of his servants.'"
    },
    "4": {
      "L": "And I heard the number of those sealed: one hundred forty-four thousand, sealed from every tribe of the sons of Israel.",
      "M": "And I heard the number of those who were sealed—one hundred and forty-four thousand, from every tribe of the sons of Israel.",
      "T": "Then I heard the count of those marked with the seal: one hundred forty-four thousand, drawn from every tribe of Israel's sons."
    },
    "5": {
      "L": "From the tribe of Judah twelve thousand were sealed; from the tribe of Reuben twelve thousand; from the tribe of Gad twelve thousand;",
      "M": "From the tribe of Judah, twelve thousand were sealed; from the tribe of Reuben, twelve thousand; from the tribe of Gad, twelve thousand;",
      "T": "Judah's tribe — twelve thousand sealed; Reuben's tribe — twelve thousand; Gad's tribe — twelve thousand;"
    },
    "6": {
      "L": "from the tribe of Asher twelve thousand; from the tribe of Naphtali twelve thousand; from the tribe of Manasseh twelve thousand;",
      "M": "from the tribe of Asher, twelve thousand; from the tribe of Naphtali, twelve thousand; from the tribe of Manasseh, twelve thousand;",
      "T": "Asher's tribe — twelve thousand; Naphtali's tribe — twelve thousand; Manasseh's tribe — twelve thousand;"
    },
    "7": {
      "L": "from the tribe of Simeon twelve thousand; from the tribe of Levi twelve thousand; from the tribe of Issachar twelve thousand;",
      "M": "from the tribe of Simeon, twelve thousand; from the tribe of Levi, twelve thousand; from the tribe of Issachar, twelve thousand;",
      "T": "Simeon's tribe — twelve thousand; Levi's tribe — twelve thousand; Issachar's tribe — twelve thousand;"
    },
    "8": {
      "L": "from the tribe of Zebulun twelve thousand; from the tribe of Joseph twelve thousand; from the tribe of Benjamin twelve thousand were sealed.",
      "M": "from the tribe of Zebulun, twelve thousand; from the tribe of Joseph, twelve thousand; from the tribe of Benjamin, twelve thousand were sealed.",
      "T": "Zebulun's tribe — twelve thousand; Joseph's tribe — twelve thousand; Benjamin's tribe — twelve thousand sealed."
    },
    "9": {
      "L": "After these things I looked, and behold, a great multitude which no man was able to number, out of every nation and of all tribes and peoples and tongues, standing before the throne and before the Lamb, clothed in white robes, and palm branches in their hands;",
      "M": "After this I looked, and there was a great multitude that no one could count, from every nation, tribe, people, and language, standing before the throne and before the Lamb, clothed in white robes, with palm branches in their hands.",
      "T": "After this I looked, and there it was — a vast crowd no one could number, drawn from every nation, every tribe, every people and language, standing before the throne and before the Lamb, dressed in white robes and waving palm branches."
    },
    "10": {
      "L": "And they cry with a loud voice, saying, 'Salvation to our God who sits on the throne, and to the Lamb.'",
      "M": "And they cried out with a loud voice: 'Salvation belongs to our God who sits on the throne, and to the Lamb!'",
      "T": "They shouted with one great voice: 'Victory and salvation belong to our God enthroned on high, and to the Lamb!'"
    },
    "11": {
      "L": "And all the angels stood around the throne and around the elders and the four living creatures, and they fell on their faces before the throne and worshiped God,",
      "M": "All the angels stood around the throne and around the elders and the four living creatures, and they fell face down before the throne and worshiped God,",
      "T": "All the angels standing in the great circle around the throne, around the elders, and around the four living creatures dropped to their faces before the throne and worshiped God,"
    },
    "12": {
      "L": "saying, 'Amen! Blessing and glory and wisdom and thanksgiving and honor and power and might be to our God forever and ever! Amen.'",
      "M": "'Amen! Blessing and glory and wisdom and thanksgiving and honor and power and might belong to our God forever and ever! Amen.'",
      "T": "crying, 'So be it! All blessing and glory and wisdom and gratitude and honor and power and strength belong to our God throughout all the ages of ages! So be it!'"
    },
    "13": {
      "L": "And one of the elders answered, saying to me, 'These who are clothed in the white robes — who are they, and from where have they come?'",
      "M": "Then one of the elders addressed me: 'These who are dressed in white robes — who are they, and where did they come from?'",
      "T": "One of the elders then turned to me: 'These people clothed in white — who are they, and where did they come from?'"
    },
    "14": {
      "L": "And I said to him, 'My lord, you know.' And he said to me, 'These are those coming out of the great tribulation, and they washed their robes and made them white in the blood of the Lamb.'",
      "M": "I answered, 'Sir, you know.' And he said to me, 'These are the ones coming out of the great tribulation; they have washed their robes and made them white in the blood of the Lamb.'",
      "T": "'Sir, you know,' I answered. He said to me, 'These are survivors of the great tribulation — they have laundered their robes until they became white, rinsed clean in the very blood of the Lamb.'"
    },
    "15": {
      "L": "Because of this they are before the throne of God, and they serve him day and night in his temple; and he who sits on the throne will dwell over them.",
      "M": "Therefore they stand before the throne of God and serve him day and night in his temple, and he who sits on the throne will shelter them with his presence.",
      "T": "This is why they stand before God's throne: they serve him day and night in his sanctuary, and God himself — enthroned above — spreads his dwelling over them like a canopy."
    },
    "16": {
      "L": "They will hunger no more, neither will they thirst anymore, nor will the sun fall upon them, nor any heat;",
      "M": "They will never hunger or thirst again; the sun will not strike them, nor will any scorching heat.",
      "T": "Never again will they hunger; never again will they thirst. No blazing sun will bear down on them, no searing heat will touch them."
    },
    "17": {
      "L": "for the Lamb in the midst of the throne will shepherd them, and will guide them to living fountains of waters; and God will wipe away every tear from their eyes.",
      "M": "For the Lamb at the center of the throne will be their shepherd and will lead them to springs of living water, and God will wipe away every tear from their eyes.",
      "T": "For the Lamb who stands at the throne's heart will shepherd them, leading them to springs of water that give life — and God himself will gently wipe every tear from their eyes."
    }
  },
  "8": {
    "1": {
      "L": "And when he opened the seventh seal, there was silence in heaven for about half an hour.",
      "M": "When the Lamb opened the seventh seal, there was silence in heaven for about half an hour.",
      "T": "When the Lamb broke open the seventh seal, heaven fell completely silent — for nearly half an hour, nothing."
    },
    "2": {
      "L": "And I saw the seven angels who stand before God, and seven trumpets were given to them.",
      "M": "I saw the seven angels who stand before God, and seven trumpets were given to them.",
      "T": "I saw the seven angels who stand in attendance before God, and each was handed a trumpet."
    },
    "3": {
      "L": "And another angel came and stood at the altar, having a golden censer; and much incense was given to him, that he should offer it with the prayers of all the saints upon the golden altar which was before the throne.",
      "M": "Another angel came and stood at the altar, holding a golden censer. He was given a large amount of incense to offer, along with the prayers of all the saints, on the golden altar before the throne.",
      "T": "Then another angel took his place at the altar, holding a golden censer. He was given a great quantity of incense to blend with the prayers of all God's holy people and lay upon the golden altar set before the throne."
    },
    "4": {
      "L": "And the smoke of the incense ascended up with the prayers of the saints from the angel's hand before God.",
      "M": "The smoke of the incense, together with the prayers of the saints, rose up before God from the angel's hand.",
      "T": "The incense smoke rose up before God, carrying with it the prayers of the saints — ascending from the angel's hand like a living offering."
    },
    "5": {
      "L": "And the angel took the censer and filled it with the fire of the altar and cast it to the earth; and there were thunders and voices and lightnings and an earthquake.",
      "M": "Then the angel took the censer, filled it with fire from the altar, and hurled it onto the earth. There followed peals of thunder, rumblings, flashes of lightning, and an earthquake.",
      "T": "Then the angel scooped fire from the altar into the censer and flung it onto the earth — and the earth answered with thunder, crashing voices, lightning, and a shaking of the ground."
    },
    "6": {
      "L": "And the seven angels who had the seven trumpets prepared themselves to sound.",
      "M": "The seven angels with the seven trumpets prepared to sound them.",
      "T": "The seven angels, each holding a trumpet, made ready to sound."
    },
    "7": {
      "L": "The first sounded, and there came hail and fire mingled with blood, and it was cast upon the earth; and a third of the earth was burned up, and a third of the trees were burned up, and all the green grass was burned up.",
      "M": "The first angel sounded, and hail and fire mixed with blood were hurled onto the earth. A third of the earth was burned up, a third of the trees were burned up, and all the green grass was burned up.",
      "T": "The first trumpet rang out, and hail and fire laced with blood was hurled down onto the earth. A third of the earth was consumed, a third of the trees destroyed, and every blade of green grass scorched away."
    },
    "8": {
      "L": "And the second angel sounded, and as it were a great mountain burning with fire was cast into the sea; and a third of the sea became blood;",
      "M": "The second angel sounded, and something like a great mountain blazing with fire was thrown into the sea. A third of the sea turned to blood,",
      "T": "The second trumpet sounded, and something like a vast mountain engulfed in fire was hurled into the sea. A third of the sea was turned to blood,"
    },
    "9": {
      "L": "and a third of the creatures in the sea, those having life, died; and a third of the ships were destroyed.",
      "M": "and a third of the living creatures in the sea died, and a third of the ships were destroyed.",
      "T": "a third of every living thing in the sea perished, and a third of all ships were wrecked."
    },
    "10": {
      "L": "And the third angel sounded, and there fell from heaven a great star, burning like a lamp, and it fell upon a third of the rivers and upon the springs of waters.",
      "M": "The third angel sounded, and a great star blazing like a torch fell from heaven onto a third of the rivers and on the springs of water.",
      "T": "The third trumpet blew, and a great star fell burning from the sky like a torch. It struck a third of the rivers and the springs of fresh water."
    },
    "11": {
      "L": "And the name of the star is called Wormwood; and a third of the waters became wormwood, and many men died from the waters, because they were made bitter.",
      "M": "The name of the star was Wormwood, and a third of the waters turned bitter like wormwood. Many people died from the water, because it had become bitter.",
      "T": "The star's name was Wormwood. A third of the waters were poisoned with its bitterness, and many people died from drinking what had become deadly."
    },
    "12": {
      "L": "And the fourth angel sounded, and a third of the sun was struck, and a third of the moon, and a third of the stars; so that a third of them was darkened, and the day shone not for a third part of it, and the night likewise.",
      "M": "The fourth angel sounded, and a third of the sun, a third of the moon, and a third of the stars were struck, darkening a third of each, so that daylight was reduced by a third, and the night likewise.",
      "T": "The fourth trumpet sounded, and a third of the sun, a third of the moon, a third of the stars were struck — each losing a third of its light. The day lost a third of its brightness, and the night did the same."
    },
    "13": {
      "L": "And I beheld, and I heard an eagle flying in the midst of heaven, saying with a loud voice, 'Woe, woe, woe, to the inhabitants of the earth, because of the other voices of the trumpet of the three angels, who are yet to sound!'",
      "M": "Then I looked and heard an eagle flying in midheaven, crying with a loud voice: 'Woe, woe, woe to those who dwell on the earth, because of the trumpet blasts of the three remaining angels who are about to sound!'",
      "T": "Then I saw an eagle sweeping through the high heavens, calling out in a piercing voice: 'Disaster! Disaster! Disaster upon all who inhabit the earth — for three more trumpets are about to sound!'"
    }
  },
  "9": {
    "1": {
      "L": "And the fifth angel sounded, and I saw a star fallen from heaven to the earth; and to him was given the key of the bottomless pit.",
      "M": "The fifth angel sounded, and I saw a star that had fallen from heaven to earth. He was given the key to the shaft of the bottomless pit.",
      "T": "The fifth trumpet sounded. I saw a star that had fallen from heaven to earth — and to this figure was given the key to the abyss, that shaft without a bottom."
    },
    "2": {
      "L": "And he opened the bottomless pit; and there arose a smoke out of the pit, as the smoke of a great furnace; and the sun and the air were darkened by reason of the smoke of the pit.",
      "M": "He opened the bottomless pit, and smoke poured up from the shaft like smoke from a great furnace; the sun and the air were darkened by the smoke from the pit.",
      "T": "He unlocked the abyss, and smoke billowed up from it — thick as the smoke of a massive furnace — until it darkened both sun and sky."
    },
    "3": {
      "L": "And out of the smoke came locusts upon the earth; and to them was given power, as the scorpions of the earth have power.",
      "M": "From the smoke, locusts came down upon the earth, and they were given power like the power of scorpions on the earth.",
      "T": "Out of the smoke poured locusts onto the earth — armed with the same lethal power that scorpions carry."
    },
    "4": {
      "L": "And it was commanded them that they should not hurt the grass of the earth, nor any green thing, nor any tree; but only those men who have not the seal of God in their foreheads.",
      "M": "They were commanded not to harm the grass of the earth or any green plant or any tree, but only those people who do not have the seal of God on their foreheads.",
      "T": "They were ordered to leave the grass, every green plant, every tree untouched — and to target only the people who did not carry God's seal on their foreheads."
    },
    "5": {
      "L": "And it was given to them that they should not kill them, but that they should be tormented five months; and their torment was as the torment of a scorpion when it striketh a man.",
      "M": "They were not permitted to kill them but to torment them for five months. The torment was like the sting of a scorpion when it strikes a person.",
      "T": "They could not kill their victims — only torment them. For five months people would suffer pain like a scorpion's sting."
    },
    "6": {
      "L": "And in those days shall men seek death, and shall not find it; and shall desire to die, and death shall flee from them.",
      "M": "In those days people will seek death and not find it; they will long to die, and death will flee from them.",
      "T": "In those days people will hunt for death and not be able to find it. They will beg to die, but death will run from them."
    },
    "7": {
      "L": "And the shapes of the locusts were like unto horses prepared unto battle; and on their heads were as it were crowns like gold, and their faces were as the faces of men.",
      "M": "The locusts looked like horses equipped for battle. On their heads were something like crowns of gold, and their faces were like human faces.",
      "T": "The locusts looked like war-horses fully armored for battle. On their heads they wore what appeared to be golden crowns, and their faces were like human faces."
    },
    "8": {
      "L": "And they had hair as the hair of women, and their teeth were as the teeth of lions.",
      "M": "They had hair like women's hair and teeth like lions' teeth.",
      "T": "Their hair flowed like a woman's, but their teeth were the fangs of lions."
    },
    "9": {
      "L": "And they had breastplates as it were breastplates of iron; and the sound of their wings was as the sound of chariots of many horses running to battle.",
      "M": "They had breastplates like iron breastplates, and the sound of their wings was like the roar of many horses and chariots rushing into battle.",
      "T": "They wore armor like iron plate, and the thunderous beating of their wings sounded like a vast squadron of chariots racing into battle."
    },
    "10": {
      "L": "And they had tails like unto scorpions, and there were stings in their tails; and their power was to hurt men five months.",
      "M": "They had tails like scorpions, with stingers, and their power to harm people for five months resided in their tails.",
      "T": "Their tails were like scorpions' tails — equipped with stingers — and it was through those tails that they inflicted five months of agony."
    },
    "11": {
      "L": "And they have a king over them, which is the angel of the bottomless pit; his name in the Hebrew tongue is Abaddon, but in the Greek tongue hath his name Apollyon.",
      "M": "They have as king over them the angel of the bottomless pit. His name in Hebrew is Abaddon, and in Greek he is called Apollyon.",
      "T": "Their ruler is the angel who presides over the abyss. His name in Hebrew is Abaddon — Destruction; in Greek, Apollyon — the Destroyer."
    },
    "12": {
      "L": "The first woe is past; and, behold, there come yet two woes after these things.",
      "M": "The first woe has passed. Look — two more woes are still to come.",
      "T": "The first disaster has passed. Take note — two more are on their way."
    },
    "13": {
      "L": "And the sixth angel sounded, and I heard a voice from the four horns of the golden altar which is before God,",
      "M": "The sixth angel sounded, and I heard a voice coming from the four horns of the golden altar that is before God.",
      "T": "The sixth trumpet sounded. I heard a voice issuing from the four corners of the golden altar that stands before God —"
    },
    "14": {
      "L": "saying to the sixth angel which had the trumpet, 'Loose the four angels which are bound in the great river Euphrates.'",
      "M": "saying to the sixth angel with the trumpet, 'Release the four angels who are bound at the great river Euphrates.'",
      "T": "— saying to the sixth angel who held the trumpet, 'Set free the four angels who are chained at the great Euphrates River.'"
    },
    "15": {
      "L": "And the four angels were loosed, which were prepared for an hour, and a day, and a month, and a year, for to slay the third part of men.",
      "M": "The four angels who had been prepared for this very hour, day, month, and year were released to kill a third of humanity.",
      "T": "The four angels were set loose — held in readiness for this precise hour, this day, this month, this year — and they went out to destroy a third of the human race."
    },
    "16": {
      "L": "And the number of the army of the horsemen were two hundred million; and I heard the number of them.",
      "M": "The number of mounted troops was two hundred million; I heard their number.",
      "T": "The size of this cavalry force was two hundred million — I heard the count with my own ears."
    },
    "17": {
      "L": "And thus I saw the horses in the vision, and them that sat on them, having breastplates of fire, and of jacinth, and brimstone; and the heads of the horses were as the heads of lions; and out of their mouths issued fire and smoke and brimstone.",
      "M": "This is how the horses appeared in my vision: their riders wore breastplates the color of fire, dark blue, and sulfur. The horses' heads were like lions' heads, and from their mouths came fire, smoke, and sulfur.",
      "T": "In my vision the horses looked like this: their riders wore breastplates blazing red, deep hyacinth-blue, and sulfur yellow. The horses had heads like lions, and from their mouths poured fire, billowing smoke, and scorching sulfur."
    },
    "18": {
      "L": "By these three was the third part of men killed, by the fire, and by the smoke, and by the brimstone, which issued out of their mouths.",
      "M": "A third of mankind was killed by these three plagues — the fire, the smoke, and the sulfur that poured from the horses' mouths.",
      "T": "By these three plagues — fire, smoke, and sulfur — a full third of humanity was slaughtered."
    },
    "19": {
      "L": "For their power is in their mouth, and in their tails; for their tails were like unto serpents, and had heads, and with them they do hurt.",
      "M": "For the power of the horses is in their mouths and in their tails; their tails are like serpents, with heads, and with them they inflict harm.",
      "T": "The horses' lethal power came from both ends — from their mouths and from their tails. Their tails were like snakes equipped with heads, and with these they wounded."
    },
    "20": {
      "L": "And the rest of the men which were not killed by these plagues yet repented not of the works of their hands, that they should not worship devils, and idols of gold, and silver, and brass, and stone, and of wood: which neither can see, nor hear, nor walk;",
      "M": "The rest of mankind, those who were not killed by these plagues, did not repent of the works of their hands and stop worshiping demons and idols made of gold, silver, bronze, stone, and wood — things that cannot see, hear, or walk.",
      "T": "But the remaining humans, those who survived these plagues, refused to turn from what their own hands had made. They kept on worshiping demons and idols crafted from gold, silver, bronze, stone, and wood — things that cannot see, cannot hear, cannot move."
    },
    "21": {
      "L": "Neither repented they of their murders, nor of their sorceries, nor of their fornication, nor of their thefts.",
      "M": "They did not repent of their murders, their sorceries, their sexual immorality, or their thefts.",
      "T": "They refused to repent of their murders, their occult practices, their sexual immorality, or their thievery."
    }
  },
  "10": {
    "1": {
      "L": "And I saw another mighty angel come down from heaven, clothed with a cloud; and a rainbow was upon his head, and his face was as it were the sun, and his feet as pillars of fire;",
      "M": "Then I saw another mighty angel coming down from heaven, wrapped in a cloud, with a rainbow above his head; his face was like the sun and his legs like pillars of fire.",
      "T": "I saw another powerful angel descend from heaven, wrapped in a cloud. A rainbow arched above his head, his face blazed like the sun, and his legs stood like columns of fire."
    },
    "2": {
      "L": "And he had in his hand a little book open; and he set his right foot upon the sea, and his left foot on the earth,",
      "M": "He held in his hand a little scroll, lying open. He set his right foot on the sea and his left foot on the land,",
      "T": "He held in his hand a small scroll, lying open. He planted his right foot on the sea and his left foot on the land —"
    },
    "3": {
      "L": "And cried with a loud voice, as when a lion roareth; and when he had cried, seven thunders uttered their voices.",
      "M": "and he called out in a loud voice like the roar of a lion. When he cried out, the seven thunders sounded their voices.",
      "T": "— and he shouted with a voice like a lion's roar. When the shout came, seven thunderclaps rolled out their voices in reply."
    },
    "4": {
      "L": "And when the seven thunders had uttered their voices, I was about to write; and I heard a voice from heaven saying unto me, 'Seal up those things which the seven thunders uttered, and write them not.'",
      "M": "And when the seven thunders had spoken, I was about to write; but I heard a voice from heaven say, 'Seal up what the seven thunders have spoken, and do not write it down.'",
      "T": "I was about to record what the seven thunders had said, but a voice from heaven stopped me: 'Seal up what the seven thunders spoke — do not write it.'"
    },
    "5": {
      "L": "And the angel which I saw stand upon the sea and upon the earth lifted up his hand to heaven,",
      "M": "Then the angel I had seen standing on the sea and on the land raised his right hand toward heaven",
      "T": "The angel I had seen standing astride sea and land raised his right hand toward heaven"
    },
    "6": {
      "L": "and sware by him that liveth for ever and ever, who created heaven, and the things that therein are, and the earth, and the things that therein are, and the sea, and the things which are therein, that there should be time no longer:",
      "M": "and swore by him who lives forever and ever, who created heaven and what is in it, the earth and what is in it, and the sea and what is in it: 'There will be no more delay!'",
      "T": "and swore by the one who lives throughout all the ages — who created sky and everything in it, earth and everything in it, sea and everything in it — 'There will be no more waiting. No more delay.'"
    },
    "7": {
      "L": "But in the days of the voice of the seventh angel, when he shall begin to sound, the mystery of God should be finished, as he hath declared to his servants the prophets.",
      "M": "In the days when the seventh angel is about to sound his trumpet, the mystery of God will be fulfilled, just as he announced to his servants the prophets.",
      "T": "But when the seventh angel is ready to sound his trumpet, the mystery of God will be accomplished — carried to its completion exactly as God had declared to his servants the prophets."
    },
    "8": {
      "L": "And the voice which I heard from heaven spake unto me again, and said, 'Go and take the little book which is open in the hand of the angel which standeth upon the sea and upon the earth.'",
      "M": "Then the voice I had heard from heaven spoke to me again: 'Go, take the scroll that lies open in the hand of the angel who is standing on the sea and on the land.'",
      "T": "The voice from heaven that I had heard now spoke to me again: 'Go, take the open scroll from the hand of the angel who stands on the sea and the land.'"
    },
    "9": {
      "L": "And I went unto the angel, and said unto him, 'Give me the little book.' And he said unto me, 'Take it, and eat it up; and it shall make thy belly bitter, but it shall be in thy mouth sweet as honey.'",
      "M": "I went to the angel and asked him to give me the little scroll. He said to me, 'Take it and eat it. It will make your stomach bitter, but in your mouth it will be as sweet as honey.'",
      "T": "I went to the angel and said, 'Give me the little scroll.' He said, 'Take it and eat it. In your mouth it will taste sweet as honey — but once swallowed, it will turn your stomach bitter.'"
    },
    "10": {
      "L": "And I took the little book out of the angel's hand, and ate it up; and it was in my mouth sweet as honey; and as soon as I had eaten it, my belly was bitter.",
      "M": "I took the little scroll from the angel's hand and ate it. It was sweet as honey in my mouth, but when I had eaten it, my stomach turned bitter.",
      "T": "I took the scroll from the angel's hand and swallowed it. Honey-sweet in my mouth — then, once eaten, a bitterness that settled deep in my stomach."
    },
    "11": {
      "L": "And he said unto me, 'Thou must prophesy again before many peoples, and nations, and tongues, and kings.'",
      "M": "Then I was told, 'You must prophesy again about many peoples, nations, languages, and kings.'",
      "T": "Then I was told: 'You must prophesy once more — speaking to peoples and nations and languages and kings.'"
    }
  },
  "11": {
    "1": {
      "L": "And there was given me a reed like unto a rod; and the angel stood, saying, 'Rise, and measure the temple of God, and the altar, and them that worship therein.'",
      "M": "I was given a measuring rod like a staff, and told: 'Rise and measure the temple of God and the altar, and count those who worship there.'",
      "T": "A measuring rod like a staff was placed in my hand, and I was told: 'Rise and measure the temple of God — the altar and those who worship there. Take the count.'"
    },
    "2": {
      "L": "But the court which is without the temple leave out, and measure it not; for it is given unto the Gentiles; and the holy city shall they tread under foot forty and two months.",
      "M": "But do not measure the court outside the temple; leave it out, for it has been given to the nations, and they will trample the holy city for forty-two months.",
      "T": "But leave the outer court unmeasured — pass it by, because it has been handed over to the Gentiles. They will trample the holy city for forty-two months."
    },
    "3": {
      "L": "And I will give power unto my two witnesses, and they shall prophesy a thousand two hundred and threescore days, clothed in sackcloth.",
      "M": "'And I will give authority to my two witnesses, and they will prophesy for one thousand two hundred and sixty days, dressed in sackcloth.'",
      "T": "'I am giving my two witnesses the authority to prophesy for twelve hundred sixty days — dressed in the coarse cloth of mourning.'"
    },
    "4": {
      "L": "These are the two olive trees, and the two candlesticks standing before the God of the earth.",
      "M": "These are the two olive trees and the two lampstands that stand before the Lord of the earth.",
      "T": "They are the two olive trees and the two lampstands that stand in the presence of the earth's sovereign Lord."
    },
    "5": {
      "L": "And if any man will hurt them, fire proceedeth out of their mouth, and devoureth their enemies; and if any man will hurt them, he must in this manner be killed.",
      "M": "If anyone tries to harm them, fire pours from their mouths and devours their enemies. This is how anyone who attempts to harm them must die.",
      "T": "If anyone attempts to harm them, fire shoots from their mouths and destroys their enemies — and this is how anyone who dares to harm them must die."
    },
    "6": {
      "L": "These have power to shut heaven, that it rain not in the days of their prophecy; and have power over waters to turn them to blood, and to smite the earth with all plagues, as often as they will.",
      "M": "These have power to shut the sky, so that no rain falls during the days of their prophesying; and they have authority over the waters, to turn them to blood and to strike the earth with every kind of plague, as often as they wish.",
      "T": "They have authority to lock up the sky so that no rain falls through the entire span of their prophesying. They can turn the waters to blood and strike the earth with any plague they choose, as many times as they choose."
    },
    "7": {
      "L": "And when they shall have finished their testimony, the beast that ascendeth out of the bottomless pit shall make war against them, and shall overcome them, and kill them.",
      "M": "When they have completed their testimony, the beast that rises from the bottomless pit will make war against them, conquer them, and kill them.",
      "T": "But when they have completed their witness, the Beast rising from the abyss will launch its assault against them, overpower them, and kill them."
    },
    "8": {
      "L": "And their dead bodies shall lie in the street of the great city, which spiritually is called Sodom and Egypt, where also our Lord was crucified.",
      "M": "Their bodies will lie in the public square of the great city that is figuratively called Sodom and Egypt — the city where their Lord was crucified.",
      "T": "Their corpses will lie in the open street of that great city — the city that in the Spirit is named Sodom, named Egypt, the very city where their Lord was crucified."
    },
    "9": {
      "L": "And they of the peoples and tribes and tongues and nations shall see their dead bodies three days and an half, and shall not suffer their dead bodies to be put in graves.",
      "M": "For three and a half days, people from every people, tribe, language, and nation will stare at their bodies and refuse to permit them to be placed in a tomb.",
      "T": "For three and a half days, people from every nation, tribe, language, and people will gaze on their bodies — and no one will allow them to be buried."
    },
    "10": {
      "L": "And they that dwell upon the earth shall rejoice over them, and make merry, and shall send gifts one to another; because these two prophets tormented them that dwelt on the earth.",
      "M": "And the inhabitants of the earth will gloat over them, celebrate, and exchange gifts with one another, because these two prophets had tormented those who live on the earth.",
      "T": "Earth's inhabitants will throw a celebration over them — rejoicing, making merry, sending presents back and forth — because these two prophets had been a torment to everyone who lives on the earth."
    },
    "11": {
      "L": "And after three days and an half the Spirit of life from God entered into them, and they stood upon their feet; and great fear fell upon them which saw them.",
      "M": "But after three and a half days, the breath of life from God entered them, and they stood on their feet, and great terror struck those who watched them.",
      "T": "But after three and a half days, the very breath of life from God entered their bodies. They stood on their feet — and those who had been watching were seized with overwhelming dread."
    },
    "12": {
      "L": "And they heard a great voice from heaven saying unto them, 'Come up hither.' And they ascended up to heaven in a cloud; and their enemies beheld them.",
      "M": "Then they heard a loud voice from heaven saying to them, 'Come up here!' And they went up to heaven in a cloud while their enemies watched.",
      "T": "Then a great voice from heaven called out to them: 'Come up here!' And before the eyes of their enemies, they rose into heaven in a cloud."
    },
    "13": {
      "L": "And the same hour was there a great earthquake, and the tenth part of the city fell, and in the earthquake were slain of men seven thousand; and the remnant were affrighted, and gave glory to the God of heaven.",
      "M": "At that moment there was a great earthquake, and a tenth of the city collapsed. Seven thousand people were killed in the earthquake, and the rest were filled with fear and gave glory to the God of heaven.",
      "T": "In that same hour a great earthquake struck. A tenth of the city crumbled. Seven thousand people were killed — and the survivors, trembling, gave glory to the God of heaven."
    },
    "14": {
      "L": "The second woe is past; and, behold, the third woe cometh quickly.",
      "M": "The second woe has passed. The third woe is coming soon.",
      "T": "The second disaster has passed. The third is coming without delay."
    },
    "15": {
      "L": "And the seventh angel sounded; and there were great voices in heaven, saying, 'The kingdoms of this world are become the kingdoms of our Lord, and of his Christ; and he shall reign for ever and ever.'",
      "M": "The seventh angel sounded his trumpet, and there were loud voices in heaven, saying: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he will reign forever and ever.'",
      "T": "The seventh trumpet sounded, and mighty voices rang through heaven: 'The kingdom of this world has been transferred to our Lord and his Anointed One — and he will reign throughout all the ages of ages!'"
    },
    "16": {
      "L": "And the four and twenty elders, which sat before God on their seats, fell upon their faces, and worshipped God,",
      "M": "The twenty-four elders who sit on their thrones before God fell on their faces and worshiped God,",
      "T": "The twenty-four elders who sit enthroned in God's presence prostrated themselves and worshiped God,"
    },
    "17": {
      "L": "Saying, 'We give thee thanks, O Lord God Almighty, which art, and wast, and art to come; because thou hast taken to thee thy great power, and hast reigned.'",
      "M": "saying: 'We give you thanks, Lord God Almighty, who is and who was, because you have taken your great power and have begun to reign.'",
      "T": "saying: 'We thank you, Lord God Almighty — the one who is and who was — because you have seized your great power and have begun your reign.'"
    },
    "18": {
      "L": "And the nations were angry, and thy wrath is come, and the time of the dead, that they should be judged, and that thou shouldest give reward unto thy servants the prophets, and to the saints, and them that fear thy name, small and great; and shouldest destroy them which destroy the earth.",
      "M": "The nations raged, but your wrath has come. The time has come for the dead to be judged, for rewarding your servants the prophets and the saints and those who fear your name, both small and great, and for destroying those who destroy the earth.",
      "T": "The nations were in an uproar — but now your wrath has arrived. The time has come: the dead will face judgment; your servants the prophets, your holy people, all who fear your name — small and great alike — will receive their reward; and those who have been destroying the earth will themselves be destroyed."
    },
    "19": {
      "L": "And the temple of God was opened in heaven, and there was seen in his temple the ark of his testament; and there were lightnings, and voices, and thunderings, and an earthquake, and great hail.",
      "M": "Then God's temple in heaven was opened, and within his temple was seen the ark of his covenant. There were flashes of lightning, rumblings, peals of thunder, an earthquake, and a severe hailstorm.",
      "T": "Then God's temple in heaven was flung open, and the ark of his covenant became visible within. Lightning blazed, voices thundered, the earth shook, and great hailstones fell."
    }
  },
  "12": {
    "1": {
      "L": "And there appeared a great wonder in heaven; a woman clothed with the sun, and the moon under her feet, and upon her head a crown of twelve stars;",
      "M": "A great sign appeared in heaven: a woman clothed with the sun, with the moon under her feet, and a crown of twelve stars on her head.",
      "T": "A great wonder-sign blazed into view in heaven: a woman clothed in the sun, the moon beneath her feet, and on her head a crown of twelve stars."
    },
    "2": {
      "L": "And she being with child cried, travailing in birth, and pained to be delivered.",
      "M": "She was pregnant and cried out in labor, in pain to give birth.",
      "T": "She was pregnant and cried out in the agony of labor, straining to give birth."
    },
    "3": {
      "L": "And there appeared another wonder in heaven; and behold a great red dragon, having seven heads and ten horns, and seven crowns upon his heads.",
      "M": "Then another sign appeared in heaven: a great red dragon with seven heads and ten horns, and seven royal crowns on his heads.",
      "T": "Then another sign appeared — a great fiery-red dragon with seven heads and ten horns, each head bearing a diadem crown."
    },
    "4": {
      "L": "And his tail drew the third part of the stars of heaven, and did cast them to the earth; and the dragon stood before the woman which was ready to be delivered, for to devour her child as soon as it was born.",
      "M": "His tail swept a third of the stars from the sky and hurled them to the earth. The dragon stood before the woman who was about to give birth, ready to devour her child the moment it was born.",
      "T": "His tail swept a third of the stars from heaven and hurled them to earth. He crouched before the woman, waiting to swallow her child the instant it was born."
    },
    "5": {
      "L": "And she brought forth a man child, who was to rule all nations with a rod of iron; and her child was caught up unto God, and to his throne.",
      "M": "She gave birth to a son, a male child who is to rule all the nations with an iron rod; and her child was caught up to God and to his throne.",
      "T": "She gave birth to a son — the male child destined to shepherd all the nations with an iron rod. And her child was snatched up to God, safe at his throne."
    },
    "6": {
      "L": "And the woman fled into the wilderness, where she hath a place prepared of God, that they should feed her there a thousand two hundred and threescore days.",
      "M": "The woman fled into the wilderness, where God had prepared a place for her to be taken care of for one thousand two hundred and sixty days.",
      "T": "The woman fled into the desert wilderness, to a place God had prepared for her, where she would be cared for through those twelve hundred sixty days."
    },
    "7": {
      "L": "And there was war in heaven: Michael and his angels fought against the dragon; and the dragon fought and his angels,",
      "M": "Then war broke out in heaven. Michael and his angels fought against the dragon, and the dragon and his angels fought back,",
      "T": "War erupted in heaven. Michael and his angel armies fought against the dragon, and the dragon and his angels fought back —"
    },
    "8": {
      "L": "And prevailed not; neither was their place found any more in heaven.",
      "M": "but he was not strong enough, and there was no longer any place for him and his angels in heaven.",
      "T": "— but the dragon was overpowered. There was no room left for him or his angels in heaven."
    },
    "9": {
      "L": "And the great dragon was cast out, that old serpent, called the Devil, and Satan, which deceiveth the whole world; he was cast out into the earth, and his angels were cast out with him.",
      "M": "The great dragon was hurled down — that ancient serpent called the devil and Satan, who leads the whole world astray. He was thrown to the earth, and his angels with him.",
      "T": "The great dragon was flung down — that ancient serpent, the one called the Devil and Satan, who has been deceiving the entire world. He was cast down to earth, and his angels fell with him."
    },
    "10": {
      "L": "And I heard a loud voice saying in heaven, 'Now is come salvation, and strength, and the kingdom of our God, and the power of his Christ; for the accuser of our brethren is cast down, which accused them before our God day and night.'",
      "M": "Then I heard a loud voice in heaven say: 'Now have come the salvation and the power and the kingdom of our God, and the authority of his Christ. For the accuser of our brothers and sisters has been cast down — the one who accuses them before our God day and night.'",
      "T": "Then a great voice rang through heaven: 'Now it has come — salvation and power, the kingdom of our God and the rule of his Anointed One! For the accuser of our brothers and sisters has been thrown down — the one who stood before our God and leveled charges against them day and night.'"
    },
    "11": {
      "L": "And they overcame him by the blood of the Lamb, and by the word of their testimony; and they loved not their lives unto the death.",
      "M": "They triumphed over him by the blood of the Lamb and by the word of their testimony; they did not love their lives so much as to shrink from death.",
      "T": "They won the victory over him through the blood of the Lamb and through the word of their witness — and they did not cling to life even when death stared them in the face."
    },
    "12": {
      "L": "Therefore rejoice, ye heavens, and ye that dwell in them. Woe to the inhabiters of the earth and of the sea! for the devil is come down unto you, having great wrath, because he knoweth that he hath but a short time.",
      "M": "Therefore rejoice, you heavens and you who dwell in them! But woe to the earth and the sea, because the devil has gone down to you. He is filled with fury, because he knows his time is short.",
      "T": "So celebrate, O heavens — and all you who make your home there! But disaster strikes those who live on earth and sea, because the devil has come down to you in towering rage, knowing full well that his time is almost gone."
    },
    "13": {
      "L": "And when the dragon saw that he was cast unto the earth, he persecuted the woman which brought forth the man child.",
      "M": "When the dragon saw that he had been thrown down to the earth, he pursued the woman who had given birth to the male child.",
      "T": "When the dragon realized he had been cast down to the earth, he launched his pursuit after the woman who had given birth to the boy."
    },
    "14": {
      "L": "And to the woman were given two wings of a great eagle, that she might fly into the wilderness, into her place, where she is nourished for a time, and times, and half a time, from the face of the serpent.",
      "M": "The woman was given the two wings of a great eagle so that she could fly to her place in the wilderness, where she would be taken care of for a time, times and half a time, out of the serpent's reach.",
      "T": "The woman was given the two wings of a great eagle so she could escape to her wilderness refuge — where she would be provided for through a time, and times, and half a time — beyond the serpent's reach."
    },
    "15": {
      "L": "And the serpent cast out of his mouth water as a flood after the woman, that he might cause her to be carried away of the flood.",
      "M": "Then from his mouth the serpent poured out water like a river after the woman, to sweep her away with the current.",
      "T": "Then the serpent spewed water like a great river out of his mouth, trying to flush the woman away in the torrent."
    },
    "16": {
      "L": "And the earth helped the woman, and the earth opened her mouth, and swallowed up the flood which the dragon cast out of his mouth.",
      "M": "But the earth came to the woman's rescue; the earth opened its mouth and swallowed the river that the dragon had spewed from his mouth.",
      "T": "But the earth itself came to the woman's defense — it opened and drank down the river the dragon had hurled from his mouth."
    },
    "17": {
      "L": "And the dragon was wroth with the woman, and went to make war with the remnant of her seed, which keep the commandments of God, and have the testimony of Jesus Christ.",
      "M": "Then the dragon was furious with the woman and went off to wage war against the rest of her offspring — those who keep God's commandments and hold to the testimony of Jesus.",
      "T": "Enraged, the dragon stalked off to wage war against the rest of her children — those who obey God's commandments and hold fast to the witness of Jesus."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 7–12 written.')

if __name__ == '__main__':
    main()
