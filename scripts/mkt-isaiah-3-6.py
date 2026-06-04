"""
MKT Isaiah chapters 3–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-3-6.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — the divine personal name; T surfaces it
  to honour the theological weight Isaiah places on YHWH as sovereign over history
- H136 (אֲדֹנָי): "Lord" (L/M/T) — the title 'Adonai', distinct from the Tetragrammaton;
  used in 3:1, 3:15, 6:1, 6:8, 6:11; when paired with יהוה = "Lord GOD"
- H6635 (צְבָאוֹת): "of hosts" (L/M/T) — retained throughout; "LORD of hosts" is Isaiah's
  signature title for YHWH as divine warrior and cosmic sovereign
- H113 (אָדוֹן): "lord / master / Lord" (L/M) — appears in 3:1 ("the Lord, the LORD of hosts");
  understood as Adonai in context; T renders as "the Lord Yahweh of hosts"
- H6780 (צֶמַח): "branch" (L/M) / "Branch" (T, 4:2) — capitalised in T because the Branch
  of Yahweh carries messianic resonance fully developed in later Isaiah and Zechariah
- H7307 (רוּחַ): "spirit" (L/M/T, 4:4) — lowercase throughout; context is instrumental
  ("a spirit of judgment and a spirit of burning"), not a clear reference to the divine Spirit
- H6944 (קֹדֶשׁ) / H6918 (קָדוֹשׁ): "holy" / "Holy One" throughout; in 6:3 Trisagion preserved
  with the triple "holy" in all tiers; the gravity of the repetition is retained exactly
- H7562 (רֶשַׁע): "wickedness / wicked" (L/M/T) — standard rendering for moral evil
- H4941 (מִשְׁפָּט): "justice / judgment" (L/M) / "justice" (T) — the covenantal standard
  YHWH expects from his vineyard (5:7); not merely procedural but relational-covenantal
- H6666 (צְדָקָה): "righteousness" (L/M/T, 5:7) — paired with mishpat; the social-relational
  dimension of right ordering; the bitter wordplay in 5:7 (mishpat/mishpach, tsedaqah/tseaqah)
  is captured in T with an explanatory note in the verse
- H7585 (שְׁאוֹל): "Sheol" (L/M/T, 5:14) — transliterated throughout; the Hebrew underworld;
  T adds brief gloss "the realm of the dead" for the first occurrence
- H6086 (עֵץ): "tree" in standard uses; in 6:13 "oak / terebinth" as the context specifies
- Vineyard Song (5:1-7): treated as formal poetry in all tiers; T preserves line breaks
- Woe oracles (5:8–24): prophetic poetry; T preserves parallel structure with line breaks
- Chapter 6 theophany: rendered with high formal register in all tiers; T maximises liturgical
  gravity especially in 6:3 (Trisagion) and 6:8 (prophetic commissioning)
- The wordplay in 5:7 — mishpat (justice) vs. mishpach (bloodshed), tsedaqah (righteousness)
  vs. tseaqah (a cry/outcry) — is untranslatable but surfaced in a T parenthetical note
- Divine passive in 4:3 "will be called holy" — YHWH is the implied agent; noted in L
- 6:13 textual note: the final clause "the holy seed is its stump" is widely accepted as
  original, not a gloss; it is translated in all tiers as the theological climax of the passage
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

ISAIAH = {
  "3": {
    "1": {
      "L": "For behold, the Lord, the LORD of hosts, is removing from Jerusalem and from Judah support and staff — the whole support of bread and the whole support of water:",
      "M": "For behold, the Lord, the LORD of hosts, is about to remove from Jerusalem and from Judah every kind of support — every support of bread and every support of water:",
      "T": "Mark this well: the Lord, Yahweh of hosts, is stripping away from Jerusalem and Judah every prop and stay — every last crust of bread and every drop of water."
    },
    "2": {
      "L": "the mighty man and the warrior, the judge and the prophet, the diviner and the elder,",
      "M": "the warrior and the soldier, the judge and the prophet, the diviner and the elder,",
      "T": "the soldier and the warrior, the judge and the prophet, the fortune-teller and the elder,"
    },
    "3": {
      "L": "the captain of fifty and the man of rank, the counselor and the skilled craftsman and the expert in charms.",
      "M": "the captain of fifty and the man of standing, the counselor and the skilled artisan and the expert enchanter.",
      "T": "the officer of fifty and the man of honour, the shrewd counselor and the master craftsman and the one skilled in spells."
    },
    "4": {
      "L": "And I will make youths their princes, and infants shall rule over them.",
      "M": "I will make youths their rulers, and infants shall govern them.",
      "T": "I will give them children for rulers and make infants their masters."
    },
    "5": {
      "L": "And the people will oppress one another, each one against his neighbour; the child will be insolent to the elder, and the lowly toward the honourable.",
      "M": "The people will oppress one another, everyone against his neighbour; the young will be arrogant toward the old, and the worthless toward the honourable.",
      "T": "Society will unravel — neighbour against neighbour, the young contemptuous of the old, the base person brazen toward the respectable."
    },
    "6": {
      "L": "When a man grasps his brother in the house of his father, saying: 'You have a cloak; you shall be our ruler, and this heap of ruins shall be under your hand' —",
      "M": "A man will seize his own brother in their father's house and say: 'You have a robe; be our leader, and let this heap of ruins be under your authority' —",
      "T": "A man will grab his own brother by the sleeve in their father's house and plead: 'At least you own a cloak — be our leader! Rule over this rubble!'"
    },
    "7": {
      "L": "on that day he will swear, saying: 'I will not be a healer; in my house there is neither bread nor cloak; you shall not make me ruler of the people.'",
      "M": "but on that day he will protest: 'I am no healer; in my house there is no bread and no robe; do not make me a leader of the people.'",
      "T": "And even then the brother will swear: 'I have no remedy to offer. There is no bread in my house, no cloak on my back. Do not appoint me over this people.'"
    },
    "8": {
      "L": "For Jerusalem has stumbled and Judah has fallen, because their tongue and their deeds are against the LORD, defying his glorious eyes.",
      "M": "For Jerusalem has stumbled and Judah has fallen, because in word and deed they have rebelled against the LORD, defying his glorious presence.",
      "T": "Jerusalem has stumbled; Judah has gone down — because their words and their actions are a direct affront to Yahweh, a defiance of his all-seeing glory."
    },
    "9": {
      "L": "The look on their face witnesses against them; they declare their sin like Sodom; they do not hide it. Woe to themselves! For they have brought evil upon themselves.",
      "M": "The expression on their faces testifies against them; they flaunt their sin like Sodom and do not conceal it. Woe to them! For they have brought disaster on themselves.",
      "T": "Their own faces give them away — guilt worn openly like a badge. They advertise their sin the way Sodom did, without a trace of shame. Woe to them! They have heaped this disaster on their own heads."
    },
    "10": {
      "L": "Say to the righteous that it shall be well with them, for they shall eat the fruit of their deeds.",
      "M": "Tell the righteous that it will go well for them, for they shall enjoy the fruit of their actions.",
      "T": "Speak this word to the righteous: all shall be well with them — they will feast on the harvest of what they have sown."
    },
    "11": {
      "L": "Woe to the wicked! It shall be ill with him, for what his hands have done shall be repaid to him.",
      "M": "Woe to the wicked! It will go badly for him, for what his hands have done will be done to him in return.",
      "T": "But woe to the wicked — disaster awaits! Every deed their hands have dealt out will be dealt back to them in full."
    },
    "12": {
      "L": "My people — their oppressors are children, and women rule over them. O my people, your guides lead you astray; they have swallowed up the course of your paths.",
      "M": "My people — their oppressors are children, and women rule over them. O my people, your guides mislead you; they have confused the path you should walk.",
      "T": "My people — their masters are children; women hold sway over them. O my people, the ones who lead you are leading you to ruin; they have obliterated every right road."
    },
    "13": {
      "L": "The LORD has taken his place to contend; he stands to judge the peoples.",
      "M": "The LORD has taken his stand to bring a charge; he stands to render judgment on the peoples.",
      "T": "Yahweh rises to plead his case — he takes his place in the courtroom of history to pronounce sentence on the nations."
    },
    "14": {
      "L": "The LORD enters into judgment with the elders and princes of his people: 'It is you who have devoured the vineyard; the spoil of the poor is in your houses.'",
      "M": "The LORD brings his case against the elders and leaders of his people: 'You have plundered the vineyard; the goods stolen from the poor fill your houses.'",
      "T": "Yahweh himself enters judgment against the elders and rulers of his people: 'You are the ones who have stripped the vineyard bare. The plunder taken from the poor is stockpiled in your mansions.'"
    },
    "15": {
      "L": "'What do you mean by crushing my people and grinding the faces of the poor?' declares the Lord GOD of hosts.",
      "M": "'What do you think you are doing, crushing my people and grinding the faces of the poor into the dust?' declares the Lord GOD of hosts.",
      "T": "'How dare you grind my people to powder, how dare you mill the faces of the poor into the dirt?' — this is the verdict of the Lord Yahweh of hosts."
    },
    "16": {
      "L": "And the LORD said: Because the daughters of Zion are haughty, walking with outstretched necks and flirtatious eyes, mincing along with their feet and making a tinkling sound with their anklets —",
      "M": "The LORD said: Because the women of Zion are proud, walking with their heads held high and casting seductive glances, prancing along and jingling their ankle ornaments —",
      "T": "Yahweh declared: Because the women of Zion carry themselves in arrogance — necks craned, eyes roving with calculated allure, stepping with an affected mince, chiming at every step with their ankle ornaments —"
    },
    "17": {
      "L": "the Lord will strike with a scab the top of the head of the daughters of Zion, and the LORD will expose their nakedness.",
      "M": "the Lord will afflict the scalps of the daughters of Zion with sores, and the LORD will expose their shame.",
      "T": "the Lord will strike their heads with scabs, and Yahweh will strip them bare of every dignity."
    },
    "18": {
      "L": "In that day the Lord will take away the finery of the anklets, the headbands, and the crescent ornaments,",
      "M": "In that day the Lord will remove their ornamental anklets, headbands, and crescent necklaces,",
      "T": "In that day the Lord will rip away the tinkling anklets and the elaborate headdresses and the crescent pendants,"
    },
    "19": {
      "L": "the pendants, the bracelets, and the scarves,",
      "M": "the earrings, the bracelets, and the veils,",
      "T": "the drop earrings, the charm bracelets, and the filmy scarves,"
    },
    "20": {
      "L": "the headdresses, the armlets, the sashes, the perfume boxes, and the amulets,",
      "M": "the turbans, the armlets, the sashes, the perfume bottles, and the lucky charms,",
      "T": "the fine turbans and armlets and broad sashes, the perfume flasks and the good-luck amulets,"
    },
    "21": {
      "L": "the signet rings and the nose rings,",
      "M": "the signet rings and the nose rings,",
      "T": "the signet rings and the nose rings,"
    },
    "22": {
      "L": "the festal robes, the mantles, the cloaks, and the handbags,",
      "M": "the holiday garments, the capes, the wraps, and the purses,",
      "T": "the elegant festal gowns and the capes and the shawls and the clutch bags,"
    },
    "23": {
      "L": "the mirrors, the linen garments, the turbans, and the veils.",
      "M": "the polished mirrors, the linen tunics, the tiaras, and the full-length veils.",
      "T": "the polished bronze mirrors, the fine linen shifts, the jewelled tiaras, and the flowing veils."
    },
    "24": {
      "L": "Instead of perfume there will be rottenness; and instead of a belt, a rope; and instead of elaborate braided hair, baldness; and instead of a rich robe, a skirt of sackcloth; and instead of beauty, branding.",
      "M": "Instead of sweet perfume there will be a stench; instead of a sash, a rope; instead of styled hair, a shaved head; instead of a fine robe, a garment of sackcloth; and instead of beauty, a branding scar.",
      "T": "Where there was perfume — only rot.\nWhere there was a jewelled belt — a knotted rope.\nWhere there was an elaborate coiffure — a shaved head.\nWhere there was a gorgeous robe — a sack of coarse cloth.\nWhere there was beauty — a slave's brand."
    },
    "25": {
      "L": "Your men shall fall by the sword, and your warriors in battle.",
      "M": "Your men will fall by the sword, your warriors in the heat of battle.",
      "T": "Her men will be cut down by the sword; her fighting men will die in combat."
    },
    "26": {
      "L": "And her gates shall lament and mourn; she shall sit desolate upon the ground.",
      "M": "Her city gates will mourn and grieve; she will sit desolate on the ground.",
      "T": "Her gates will wail in mourning and desolation — and she will sit on the bare earth, stripped and alone."
    }
  },
  "4": {
    "1": {
      "L": "And seven women shall take hold of one man in that day, saying: 'We will eat our own bread and wear our own clothing; only let us be called by your name — take away our reproach.'",
      "M": "In that day seven women will grab hold of one man, saying: 'We will provide our own food and clothing — just let us bear your name and remove our disgrace.'",
      "T": "So severe will be the slaughter of men that in that day seven women will lay hold of a single man, pleading: 'We will feed ourselves, we will clothe ourselves — only let us carry your name. Take away the shame of our childlessness.'"
    },
    "2": {
      "L": "In that day the Branch of the LORD shall be beautiful and glorious, and the fruit of the land shall be the pride and honour of the survivors of Israel.",
      "M": "In that day the Branch of the LORD will be beautiful and glorious, and the produce of the land will be the pride and splendour of those of Israel who have survived.",
      "T": "Yet in that same day the Branch of Yahweh will emerge — radiant and glorious — and the fruit of the land will be the crown jewel of every Israelite who has come through the fire of judgment."
    },
    "3": {
      "L": "And he who is left in Zion and he who remains in Jerusalem will be called holy — everyone who has been inscribed for life in Jerusalem.",
      "M": "Everyone who remains in Zion and is left in Jerusalem will be called holy — everyone enrolled among the living in Jerusalem.",
      "T": "Those who survive in Zion, those who remain in Jerusalem — they will be called holy. Every one of them whose name is written in the roll of the living in Jerusalem will bear that sacred designation."
    },
    "4": {
      "L": "When the Lord has washed away the filth of the daughters of Zion and cleansed the blood of Jerusalem from its midst by a spirit of judgment and by a spirit of burning,",
      "M": "This will come about when the Lord has washed away the filth of the women of Zion and rinsed the blood from the midst of Jerusalem by a spirit of judgment and by a spirit of fire.",
      "T": "This will be the hour when the Lord has scoured away the moral filth of Zion's daughters and purged the bloodguilt from Jerusalem's heart — by a spirit of justice that burns like a refining fire."
    },
    "5": {
      "L": "then the LORD will create over the whole site of Mount Zion and over her assemblies a cloud by day, and smoke and the shining of a flaming fire by night; for over all the glory there will be a canopy.",
      "M": "Then the LORD will create over every dwelling-place on Mount Zion and over all her gatherings a cloud by day, and smoke with the glow of flaming fire by night; for a covering canopy will rest over all the glory.",
      "T": "Then Yahweh himself will create over every site of Mount Zion and over all her assemblies a cloud by day and a pillar of smoke, a blaze of fire by night — the glory of the Exodus renewed, a canopy of radiant presence spread over everything."
    },
    "6": {
      "L": "There will be a booth for shade by day from the heat, and a refuge and shelter from storm and rain.",
      "M": "There will be a shelter for shade from the heat of the day, a refuge and hiding place from storm and rain.",
      "T": "There will be a pavilion — shade from the scorching heat of day, shelter and refuge against every driving storm and rain."
    }
  },
  "5": {
    "1": {
      "L": "Now let me sing for my beloved my love-song about his vineyard: My beloved had a vineyard on a very fertile hill.",
      "M": "Let me sing for my beloved a song about his vineyard: My beloved had a vineyard on a rich and fertile hillside.",
      "T": "Let me sing a love song for my dear friend —\na song about his vineyard:\nMy beloved had a vineyard\nplanted on a richly-fertile slope."
    },
    "2": {
      "L": "He dug it and cleared it of stones, and planted it with choice vines; he built a watchtower in the midst of it, and hewed out a wine vat in it; and he looked for it to yield grapes, but it yielded wild grapes.",
      "M": "He dug it up and cleared away its stones, and planted it with the finest vines; he built a watchtower inside it and cut out a winepress in it. He expected it to produce fine grapes, but it produced only wild, sour grapes.",
      "T": "He broke the ground, cleared every stone,\nplanted it with the choicest of vines.\nHe built a watchtower at its centre,\nhewed a winepress into the rock.\nHe waited for sweet grapes —\nbut it gave him nothing but bitter, wild fruit."
    },
    "3": {
      "L": "And now, O inhabitants of Jerusalem and men of Judah, judge between me and my vineyard.",
      "M": "And now, you people of Jerusalem and you citizens of Judah, judge between me and my vineyard.",
      "T": "Now then — you who live in Jerusalem, you men of Judah:\nrender your verdict between me and my vineyard."
    },
    "4": {
      "L": "What more was there to do for my vineyard that I have not done in it? Why, when I looked for it to yield grapes, did it yield wild grapes?",
      "M": "What more could have been done for my vineyard that I did not do? Why then, when I expected good grapes, did it produce only wild grapes?",
      "T": "What more could I have done for this vineyard that I did not do?\nTell me — why, when I looked for a harvest of sweet grapes,\ndid it return only bitterness?"
    },
    "5": {
      "L": "And now I will tell you what I will do to my vineyard: I will remove its hedge, and it shall be devoured; I will break down its wall, and it shall be trampled.",
      "M": "Now let me tell you what I am going to do to my vineyard: I will take away its protective hedge, and it will be consumed; I will break down its wall, and it will be trampled underfoot.",
      "T": "Very well — let me tell you what I will do to my vineyard.\nI will tear out its hedge and leave it to be eaten bare.\nI will knock down its wall and let it be trampled flat."
    },
    "6": {
      "L": "I will make it a waste; it shall not be pruned or hoed, and briers and thorns shall grow up; I will also command the clouds that they rain no rain upon it.",
      "M": "I will make it a ruin: it will not be pruned or cultivated, and briers and thorns will overrun it. I will command the clouds to withhold their rain from it.",
      "T": "I will abandon it to desolation —\nno pruning, no hoeing, only thorns and briars springing up.\nAnd I will order the very clouds to hold back their rain."
    },
    "7": {
      "L": "For the vineyard of the LORD of hosts is the house of Israel, and the men of Judah are his pleasant planting; and he looked for justice, but behold, bloodshed; for righteousness, but behold, an outcry.",
      "M": "For the vineyard of the LORD of hosts is the house of Israel, and the men of Judah are his cherished planting. He looked for justice, but saw only oppression; for righteousness, but heard only cries of distress.",
      "T": "The vineyard of Yahweh of hosts is the house of Israel;\nthe men of Judah are his beloved garden-planting.\nHe looked for justice — but found only bloodshed.\nHe looked for righteousness — but heard only screaming.\n(The Hebrew makes the irony stark: he hoped for mishpat — received mishpach; for tsedaqah — heard tseaqah.)"
    },
    "8": {
      "L": "Woe to those who add house to house and join field to field until there is no room, so that you are made to dwell alone in the midst of the land.",
      "M": "Woe to those who accumulate house after house and absorb field after field until no space remains, leaving only yourselves to occupy the whole land.",
      "T": "Woe to those who swallow up house after house,\nwho absorb field after field until the last boundary stone is gone —\nuntil they are the only ones left, sole lords over the entire land."
    },
    "9": {
      "L": "The LORD of hosts has sworn in my hearing: 'Surely many houses shall become desolate, great and fine houses, without inhabitant.'",
      "M": "The LORD of hosts has sworn in my hearing: 'Many houses, large and fine as they are, will stand empty and desolate.'",
      "T": "This is what rang in my ears — the oath of Yahweh of hosts:\n'However grand and magnificent those houses may be,\nnot one of them will have a living soul inside.'"
    },
    "10": {
      "L": "For ten acres of vineyard shall yield but one bath, and a homer of seed shall yield but an ephah.",
      "M": "Ten acres of vineyard will produce only a single bath of wine, and a homer of seed will yield only an ephah of grain.",
      "T": "The land itself will fail them: ten whole acres of vineyard yielding a single gallon of wine, ten bushels of seed producing barely one."
    },
    "11": {
      "L": "Woe to those who rise early in the morning to run after strong drink, who stay up late into the evening, inflamed by wine!",
      "M": "Woe to those who are up at dawn chasing strong drink, who linger into the night with wine burning in their veins!",
      "T": "Woe to those who are already hunting for liquor at sunrise\nand drink their way deep into the night,\nuntil the wine is blazing through them."
    },
    "12": {
      "L": "They have lyre and harp, tambourine and flute and wine at their feasts, but they do not regard the deed of the LORD or see the work of his hands.",
      "M": "At their feasts there are lyre and harp, tambourine and flute and plenty of wine — but they give no thought to what the LORD has done, and they do not consider the work of his hands.",
      "T": "Their banquets overflow with harp and lute,\ntambourine and flute and cup after cup of wine —\nbut the deeds of Yahweh they cannot be bothered to see,\nand what his hands are doing they refuse to consider."
    },
    "13": {
      "L": "Therefore my people go into exile for lack of knowledge; their honoured men are famished and their multitude parched with thirst.",
      "M": "Therefore my people will go into exile for want of understanding; their distinguished men will be starving and their masses dying of thirst.",
      "T": "This is why my people will be marched away into captivity — they refused to know what they needed to know. Their nobility will go hungry; their great crowds will perish of thirst."
    },
    "14": {
      "L": "Therefore Sheol has enlarged its throat and opened its mouth beyond measure, and Jerusalem's glory and her multitude and her pomp and he who rejoices in her will go down into it.",
      "M": "Therefore Sheol — the realm of the dead — has expanded its appetite and opened its mouth without limit; Jerusalem's splendour and her crowds and her revelry and all who celebrate in her will descend into it.",
      "T": "Therefore Sheol, the realm of the dead, opens its throat wide — swallowing without measure —\nand down will go Jerusalem's glittering nobility, her noisy crowds,\nher pomp and all her party-revellers."
    },
    "15": {
      "L": "Mankind is bowed down, and each person is humbled, and the eyes of the arrogant are brought low.",
      "M": "Human beings are bowed down and each person humbled, and the eyes of the proud are cast down.",
      "T": "Every man is brought low, every person humbled —\nthe lofty eyes of the arrogant are pulled to the ground."
    },
    "16": {
      "L": "But the LORD of hosts is exalted in justice, and the Holy God shows himself holy in righteousness.",
      "M": "But the LORD of hosts is exalted in justice, and the Holy God proves himself holy through righteousness.",
      "T": "Yet Yahweh of hosts is lifted high through the act of justice,\nand the Holy God, the wholly other One, hallows himself through righteousness."
    },
    "17": {
      "L": "Then the lambs shall graze as in their pasture, and nomads shall eat among the ruins of the rich.",
      "M": "Then lambs will graze as in their own meadow, and wandering flocks will feed among the ruins of the wealthy.",
      "T": "In that overturned world, lambs will graze where the grand estates once stood, and the wandering poor will eat among the rubble of the luxurious."
    },
    "18": {
      "L": "Woe to those who drag iniquity with cords of falsehood and sin as with cart ropes,",
      "M": "Woe to those who drag along iniquity with cords of deception and haul sin behind them like a cart on thick ropes,",
      "T": "Woe to those who harness themselves to evil as if with halter ropes,\nwho haul sin along behind them like a loaded wagon —"
    },
    "19": {
      "L": "who say: 'Let him be quick, let him speed his work that we may see it; let the plan of the Holy One of Israel draw near and come, that we may know it!'",
      "M": "who say: 'Let God hurry up, let him get on with his work so we can see it; let the purpose of the Holy One of Israel come close and happen so we can find out what it is!'",
      "T": "— those who taunt: 'If God has a plan, let him get on with it — let him show us!\nLet the Holy One of Israel bring his great purpose to pass so we can see it for ourselves!'"
    },
    "20": {
      "L": "Woe to those who call evil good and good evil, who put darkness for light and light for darkness, who put bitter for sweet and sweet for bitter!",
      "M": "Woe to those who call evil good and good evil, who substitute darkness for light and light for darkness, who swap bitter for sweet and sweet for bitter!",
      "T": "Woe to those who rename evil as good and good as evil,\nwho swap darkness for light and light for darkness,\nwho trade bitter for sweet and sweet for bitter!"
    },
    "21": {
      "L": "Woe to those who are wise in their own eyes and clever in their own sight!",
      "M": "Woe to those who consider themselves wise and regard themselves as shrewd!",
      "T": "Woe to those whose only oracle is their own judgment,\nwhose only wisdom is their own reflection!"
    },
    "22": {
      "L": "Woe to those who are mighty at drinking wine and valiant in mixing strong drink,",
      "M": "Woe to those who are heroes when it comes to drinking wine, champions at blending strong liquor,",
      "T": "Woe to those who win medals for drinking wine,\nwho earn their reputation mixing the strongest brew,"
    },
    "23": {
      "L": "who acquit the guilty for a bribe and deprive the innocent of their right!",
      "M": "who let the guilty off the hook for a bribe and strip the righteous of their legal due!",
      "T": "— while they let criminals walk free for a fee\nand grind the rights of the innocent into the dirt."
    },
    "24": {
      "L": "Therefore as the tongue of fire devours stubble, and as the dried grass sinks down in flame, so their root shall become as rottenness and their blossom go up like dust; for they have rejected the law of the LORD of hosts, and despised the word of the Holy One of Israel.",
      "M": "Therefore, as fire consumes stubble and dry grass collapses in flame, so their root will rot and their blossom scatter like dust; for they have rejected the instruction of the LORD of hosts and despised the word of the Holy One of Israel.",
      "T": "So then — as fire licks up a field of stubble\nand dry grass crumbles in the flame,\ntheir root will go rotten and their flower will blow away as dust.\nFor they have thrown away the Torah of Yahweh of hosts\nand treated the word of the Holy One of Israel with contempt."
    },
    "25": {
      "L": "Therefore the anger of the LORD was kindled against his people, and he stretched out his hand against them and struck them, and the mountains quaked; and their corpses were like refuse in the midst of the streets. For all this his anger has not turned away, and his hand is stretched out still.",
      "M": "For this reason the LORD's anger burned against his people; he stretched out his hand and struck them, and the mountains trembled; their bodies lay like rubbish in the middle of the streets. Despite all this, his anger has not turned away — his hand is still outstretched.",
      "T": "Therefore the burning anger of Yahweh flared against his own people;\nhe reached out his hand against them and struck —\nand the mountains themselves shook.\nTheir corpses lay strewn in the streets like refuse.\nAnd still — for all of this — his anger has not turned back;\nhis hand is still raised to strike again."
    },
    "26": {
      "L": "He will lift up a signal for a nation far away and whistle for it from the ends of the earth; and behold, it comes swiftly and speedily!",
      "M": "He raises a signal for a distant nation and whistles for it from the far ends of the earth, and look — it comes at full speed!",
      "T": "He raises his battle-standard for a far-off nation\nand whistles it in from the ends of the earth —\nwatch: it is already coming, swift and sure."
    },
    "27": {
      "L": "None is weary, none stumbles, none slumbers or sleeps; not a waistband is loose, not a sandal-strap broken.",
      "M": "Not one of them is tired, not one trips or falls; not one drowses or sleeps; not a belt is slack and not a sandal-strap is snapped.",
      "T": "No fatigue in their ranks, no stumbling, not a man asleep;\nevery belt tight, every sandal strap intact — they march without rest."
    },
    "28": {
      "L": "Their arrows are sharp and all their bows are bent; their horses' hooves are like flint and their wheels like a whirlwind.",
      "M": "Their arrows are sharp and every bow is strung taut; their warhorses' hooves strike like flint, and their chariot wheels spin like a tornado.",
      "T": "Arrows keen-edged, every bow bent back and ready —\nhooves that ring on the road like flint,\nwheels that blur into a whirlwind."
    },
    "29": {
      "L": "Their roaring is like a lion, like young lions they roar; they growl and seize the prey and carry it away, and none shall rescue.",
      "M": "Their battle cry is like the roar of a lion — like the roar of young lions they snarl, seize their prey, and carry it off with no one to deliver it.",
      "T": "They roar like a lion, like young lions they snarl;\nthey spring on the prey, drag it away —\nand there is no one to rescue it."
    },
    "30": {
      "L": "And they will growl over it in that day, like the growling of the sea; and if one looks to the land, behold, darkness and distress; and the light is darkened by the clouds.",
      "M": "In that day they will roar over it like the roaring of the sea. And if someone looks out over the land — only darkness and anguish; the light is blotted out by heavy cloud.",
      "T": "That day they will surge and thunder over the land like a raging sea.\nLook at the land — nothing but darkness and dread.\nEven the light is swallowed by overhanging clouds."
    }
  },
  "6": {
    "1": {
      "L": "In the year that King Uzziah died, I saw the Lord sitting upon a throne, high and lifted up; and the hem of his robe filled the temple.",
      "M": "In the year that King Uzziah died, I saw the Lord seated on a throne, high and exalted, and the train of his robe filled the temple.",
      "T": "In the year King Uzziah died, I saw the Lord — seated on a throne soaring high and lifted up — and the flowing train of his robe filled the entire temple."
    },
    "2": {
      "L": "Above him stood the seraphim; each had six wings: with two he covered his face, and with two he covered his feet, and with two he flew.",
      "M": "Seraphim were standing above him, each with six wings: with two wings they covered their faces, with two they covered their feet, and with two they were flying.",
      "T": "Seraphim attended him — each with six wings: two covering their faces in awe, two veiling their feet in reverence, two bearing them aloft."
    },
    "3": {
      "L": "And one called to another and said: 'Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory!'",
      "M": "And one called out to another, saying: 'Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory!'",
      "T": "'Holy, holy, holy is Yahweh of hosts —\nthe whole earth is filled with his glory!'\nThey called this to one another, antiphon and echo in the vaulted space."
    },
    "4": {
      "L": "And the foundations of the thresholds shook at the voice of him who called, and the house was filled with smoke.",
      "M": "At the sound of the voice that called, the door-frames shook and the entire house filled with smoke.",
      "T": "At the sound of that holy calling the great door-posts shuddered on their foundations, and the house filled with smoke."
    },
    "5": {
      "L": "And I said: 'Woe is me! For I am ruined; for I am a man of unclean lips, and I dwell in the midst of a people of unclean lips; for my eyes have seen the King, the LORD of hosts!'",
      "M": "I said: 'Woe is me! I am ruined! For I am a man of unclean lips, and I live among a people of unclean lips, and my eyes have seen the King, the LORD of hosts!'",
      "T": "'Woe to me — I am undone! I am a man of polluted lips, living in the middle of a people with polluted lips — and yet my own eyes have seen the King, Yahweh of hosts!'"
    },
    "6": {
      "L": "Then one of the seraphim flew to me, having in his hand a glowing coal that he had taken with tongs from the altar.",
      "M": "Then one of the seraphim flew to me, holding in his hand a burning coal that he had lifted from the altar with a pair of tongs.",
      "T": "Then one of the seraphim flew to where I stood, holding in his hand a live coal taken from the altar with iron tongs."
    },
    "7": {
      "L": "And he touched my mouth with it and said: 'Behold, this has touched your lips; your guilt is taken away and your sin is atoned for.'",
      "M": "He touched my mouth with it and said: 'See, this has touched your lips; your guilt is removed and your sin covered over.'",
      "T": "He pressed it to my mouth and declared: 'This burning coal has touched your lips. Your guilt — lifted. Your sin — covered and cancelled.'"
    },
    "8": {
      "L": "And I heard the voice of the Lord saying: 'Whom shall I send, and who will go for us?' Then I said: 'Here am I! Send me.'",
      "M": "Then I heard the voice of the Lord saying: 'Whom shall I send? And who will go on our behalf?' I said: 'Here I am! Send me.'",
      "T": "Then I heard the voice of the Lord — 'Whom shall I send? Who will go on our behalf?' And I said, 'Here I am. Send me.'"
    },
    "9": {
      "L": "And he said: 'Go, and say to this people: Keep on hearing, but do not understand; keep on seeing, but do not perceive.'",
      "M": "He said: 'Go and tell this people: You will keep on hearing, but never understand; you will keep on seeing, but never perceive.'",
      "T": "And he said: 'Go. Speak this word to this people: Hear and hear again — but never grasp it. Look and look again — but never see.'"
    },
    "10": {
      "L": "'Make the heart of this people dull, and their ears heavy, and their eyes blind; lest they see with their eyes and hear with their ears and understand with their hearts, and turn and be healed.'",
      "M": "'Deaden the heart of this people, make their ears hard of hearing, and shut their eyes — otherwise they will see with their eyes and hear with their ears and understand with their hearts, and they will turn back and be healed.'",
      "T": "'Dull their hearts. Weight their ears with stone. Seal their eyes shut — lest they actually see, and hear, and understand with their hearts, and turn back, and I heal them.'"
    },
    "11": {
      "L": "Then I said: 'How long, O Lord?' And he said: 'Until cities lie waste without inhabitant, and houses without people, and the land is utterly desolate,",
      "M": "Then I said: 'How long, O Lord?' He answered: 'Until cities are devastated and left without a single resident, until houses stand empty of people, and the land is laid waste completely,",
      "T": "'How long, O Lord?' I asked. And he answered: 'Until every city is a rubble-field with no one left inside, until every house is empty and the whole land is an abandoned wasteland —'"
    },
    "12": {
      "L": "and the LORD has removed people far away, and the forsaken stretches are vast in the midst of the land.'",
      "M": "and the LORD has sent people far into exile, and the desolate places are widespread across the land.'",
      "T": "'— until Yahweh has exiled the people to the far ends of the earth, and the forsaken stretches of land are wide and empty at the centre of what was once home.'"
    },
    "13": {
      "L": "And though a tenth portion remain in it, it will be burned again, like a terebinth or an oak whose stump remains when they are felled. The holy seed is its stump.",
      "M": "And even if a tenth should survive, it too will be burned — like a terebinth or an oak that still has its stump after the tree has been cut down. Yet the holy seed will be the stump.",
      "T": "Even the tenth that survives will pass through fire once more — like a terebinth or oak that is felled, leaving only the stump. But that stump is the holy seed: the remnant that cannot be destroyed, the hidden life through which all that was promised will rise again."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 3–6 written.')

if __name__ == '__main__':
    main()
