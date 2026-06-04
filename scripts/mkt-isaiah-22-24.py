"""
MKT Isaiah chapters 22–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-22-24.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — consistent with mkt-isaiah-1-2 through 10-12.
- H136 (אֲדֹנָי): "Lord" in all tiers; "Lord GOD" when paired with יהוה — consistent with
  prior Isaiah scripts. 22:5, 22:12, 22:14, 22:15 are the occurrences in this range.
- H6635 (צְבָאוֹת): "of hosts" throughout.
- H4853 (מַשָּׂא, 22:1; 23:1): "burden" — the standard oracle-heading formula; T signals
  the oracular weight with "An oracle:" before the title.
- H7644 (שֶׁבְנָא, 22:15): Shebna — the arrogant royal steward who carved himself an
  elite rock tomb. His judgment (vv.17-19) and replacement by Eliakim (vv.20-24) is a
  miniature pattern of the proud-cast-down, the humble-exalted motif that runs throughout
  Isaiah. No contested rendering required; the name is transliterated.
- H4668 (מַפְתֵּחַ, 22:22): "key" — the key of David placed on Eliakim's shoulder.
  This verse is quoted verbatim in Revelation 3:7 with reference to Christ. T notes the
  NT echo; L/M render straightforwardly without importing the NT context.
- H4849 / H3489 (nail/peg, 22:23, 22:25): "peg" in all tiers — the Hebrew יָתֵד is a tent
  peg or wall spike. L/M: "peg." T: same, with the sudden reversal of 22:25 made stark.
  The passage is a cautionary parable — even a firmly fastened peg falls when overloaded.
- H1285 (בְּרִית, 24:5): "covenant" — in context, the "everlasting covenant" (בְּרִית עוֹלָם)
  likely alludes to the Noahic covenant (Gen 9) and/or the covenant order of creation itself,
  not merely the Mosaic law. T makes this cosmic scope explicit. L/M use "covenant" without
  specifying which; this is appropriate to the ambiguity of the text.
- H5769 (עוֹלָם, 24:5): "everlasting" for the covenant — standard and uncontested.
- Isaiah 24 as literary unit: Chapter 24 opens the "Isaiah Apocalypse" (chs. 24-27) —
  a sustained vision of cosmic judgment that dwarfs the individual-nation oracles of chs. 13-23.
  The shift in register is deliberate and sharp: from oracle (burden) to cosmic poetry. T leans
  into this by preserving line breaks and heightened cadence throughout ch. 24. L/M may be
  more prosaic but should not flatten the parallel structure of the poetry.
- Poetic structure: ch. 22 is oracular poetry with some prose sections (22:15-25 is closer
  to prophetic narrative prose). Ch. 23 is lyrical lament, occasionally addressed to ships
  and cities. Ch. 24 is sustained cosmic poetry; T preserves line breaks throughout.
- H4412 (מְלוּנָה, 24:20): "hut" / "shack" — a temporary night-shelter in a field.
  The image is deliberately flimsy: the earth is as unstable as a watchman's lean-to.
- H8414 (תֹּהוּ, 24:10): "chaos" — the same word as in Gen 1:2 ("formless and void").
  The city of chaos is a de-creation; it has returned to the pre-order state. T makes this
  connection explicit.
- 22:22 / Revelation 3:7 echo: The key of David placed on Eliakim's shoulder is taken up in
  Revelation 3:7 and applied to Christ. T notes this; L and M remain anchored to the OT context.
- No significant textual-critical issues in these chapters; MT followed throughout.
  One minor note: 23:13 is notoriously difficult (the Chaldean/Assyrian crux); rendering
  follows the most natural reading of MT, noting the ambiguity.
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
  "22": {
    "1": {
      "L": "The burden of the Valley of Vision. What is the matter with you now, that you have all gone up to the housetops?",
      "M": "The burden of the Valley of Vision. What has come over you that you have all climbed up to the housetops?",
      "T": "An oracle: the Valley of Vision.\nWhat has gotten into you? Why is everyone up on the rooftops?"
    },
    "2": {
      "L": "O city full of tumult, joyful city, exultant city! Your slain are not slain with the sword, nor are your dead fallen in battle.",
      "M": "You are a city full of uproar and celebration! But your slain were not killed by the sword, and your dead did not fall in battle.",
      "T": "You roar with noise and clamour — a city drunk on its own celebration!\nBut your dead were not killed in combat.\nNo sword brought them down, no battle claimed them."
    },
    "3": {
      "L": "All your rulers have fled together; without the bow they were captured; all of you who were found were bound together, though they had fled far away.",
      "M": "All your commanders fled together; they were captured without a bow being drawn; all who were found among you were taken prisoner, even those who had fled far away.",
      "T": "Every last commander fled — no battle was even fought.\nThey surrendered without an arrow loosed.\nEveryone they found was taken prisoner —\neven those who had run to the far horizon."
    },
    "4": {
      "L": "Therefore I said: 'Look away from me; let me weep bitterly; do not press to comfort me over the destruction of the daughter of my people.'",
      "M": "Therefore I said, 'Turn away from me; let me weep bitterly; do not try to comfort me over the ruin of the daughter of my people.'",
      "T": "So I say: leave me alone. Let me weep without restraint.\nDo not rush to console me.\nThe daughter of my people has been destroyed —\nI cannot stop mourning."
    },
    "5": {
      "L": "For the Lord GOD of hosts has a day of tumult and trampling and confusion in the Valley of Vision — a battering down of walls and a crying out to the mountains.",
      "M": "For the Lord GOD of hosts has a day of panic and trampling and confusion in the Valley of Vision — walls crashing down, a war-cry echoing off the mountains.",
      "T": "For the Lord Yahweh of hosts has appointed a day —\na day of trampling and terror and confusion —\nhere in the Valley of Vision.\nWalls collapsing, battle-cries ricocheting off the mountains."
    },
    "6": {
      "L": "And Elam bore the quiver with chariots of men and horsemen, and Kir uncovered the shield.",
      "M": "Elam took up the quiver with chariots and cavalry, and Kir bared the shield.",
      "T": "Elam manned the quivers, with chariotry and cavalry in formation;\nKir stripped the shield covers — ready for war."
    },
    "7": {
      "L": "And your choicest valleys were filled with chariots, and horsemen took up positions at the gate.",
      "M": "Your finest valleys were choked with chariots, and cavalry were posted at the city gates.",
      "T": "Your best valleys choked with chariots;\ncavalry stationed at every gate."
    },
    "8": {
      "L": "And he stripped away the covering of Judah; and on that day you looked to the weapons in the House of the Forest.",
      "M": "He stripped away Judah's defenses. On that day you turned to the arsenal stored in the House of the Forest.",
      "T": "He stripped away every shield Judah had.\nAnd what did Jerusalem do? You ran to the weapons stockpiled in the House of the Forest."
    },
    "9": {
      "L": "You saw that the breaches of the city of David were many; and you collected the waters of the lower pool.",
      "M": "You saw that the gaps in the wall of the city of David were numerous, and you collected water into the lower pool.",
      "T": "You counted the breaches in David's city wall — too many to ignore —\nand channelled the lower pool's water inward for the siege."
    },
    "10": {
      "L": "And you counted the houses of Jerusalem, and you tore down houses to fortify the wall.",
      "M": "You took inventory of Jerusalem's houses and demolished buildings to strengthen the wall.",
      "T": "You catalogued Jerusalem's houses\nand tore some of them down to reinforce the city wall."
    },
    "11": {
      "L": "You made a reservoir between the two walls for the water of the old pool; but you did not look to him who made it, nor did you have regard for him who planned it long ago.",
      "M": "You built a cistern between the two walls to hold the water of the old pool, but you did not look to the one who made all this possible, nor did you give thought to the one who planned it long ago.",
      "T": "You dug a cistern between the walls to collect water from the old pool —\nevery calculation made, every plan executed.\nBut you never once looked to the One who made all of it,\nnever gave a thought to the One who had designed this whole scene long before you were born."
    },
    "12": {
      "L": "And in that day the Lord GOD of hosts called for weeping and mourning, for shaving the head and for girding with sackcloth;",
      "M": "In that day the Lord GOD of hosts called for weeping and mourning, for shaving the head and putting on sackcloth —",
      "T": "The Lord Yahweh of hosts was calling for grief that day —\nmourning, weeping, shaved heads, sackcloth:"
    },
    "13": {
      "L": "but behold, instead there was joy and gladness, slaughtering cattle and killing sheep, eating flesh and drinking wine: 'Let us eat and drink, for tomorrow we die!'",
      "M": "but instead there was only celebration — slaughtering oxen, killing sheep, eating meat and drinking wine: 'Let us eat and drink, for tomorrow we die!'",
      "T": "Instead — a party.\nOxen butchered, sheep slaughtered, wine poured out, feasting at full swing.\n'Eat and drink! Tomorrow we die!' That was the cry."
    },
    "14": {
      "L": "The LORD of hosts revealed this in my ears: 'Surely this iniquity will not be atoned for until you die,' says the Lord GOD of hosts.",
      "M": "The LORD of hosts revealed this directly in my hearing: 'This guilt will never be atoned for while you live,' says the Lord GOD of hosts.",
      "T": "Then the word came directly into my ears — from Yahweh of hosts:\n'I swear it: this guilt will not be wiped away.\nYou will carry it to your grave.'\nThe Lord Yahweh of hosts declares it."
    },
    "15": {
      "L": "Thus says the Lord GOD of hosts: 'Go, come to this steward, to this Shebna who is over the household —'",
      "M": "This is what the Lord GOD of hosts says: 'Go to this steward, this Shebna who is in charge of the palace —'",
      "T": "Then the Lord Yahweh of hosts sent this word:\n'Go to this steward — Shebna, the one who manages the palace —'"
    },
    "16": {
      "L": "'What do you have here? And whom have you here, that you have carved out a tomb here for yourself — you who hew a tomb on the heights, you who cut out a dwelling for yourself in the rock?'",
      "M": "'What gives you the right to be here? Who do you think you are, carving yourself a tomb here on the heights — hewing a burial chamber for yourself in the rock?'",
      "T": "'What gives you any right to be here?\nWho do you think you are, cutting yourself a grand tomb up on the heights —\ncarving your burial chamber out of the living rock\nas though this were your permanent home?'"
    },
    "17": {
      "L": "'Behold, the LORD will hurl you away violently — O man! — he will seize hold of you;'",
      "M": "'See — the LORD is about to hurl you away with a violent throw, O man; he will take hold of you and fling you far;'",
      "T": "'Look out — Yahweh is about to hurl you away with a mighty overhand throw, you man!\nHe will lay hold of you'"
    },
    "18": {
      "L": "'He will roll you up tightly and hurl you like a ball into a broad land; there you will die, and there your glorious chariots will be — you, the disgrace of your master's house!'",
      "M": "'He will ball you up and fling you like a stone across a wide open land; there you will die and your splendid chariots will lie there — you, the shame of your master's household!'",
      "T": "'— ball you up and hurl you like a stone across a wide, open land.\nThere you will die. Your prized chariots left useless there.\nYou — the disgrace of your lord's house!'"
    },
    "19": {
      "L": "'I will thrust you from your post, and from your station you will be pulled down.'",
      "M": "'I will remove you from your position, and you will be pulled down from your office.'",
      "T": "'I am removing you from your post.\nDown from your position you will come.'"
    },
    "20": {
      "L": "'In that day I will call my servant Eliakim the son of Hilkiah,'",
      "M": "'In that day I will summon my servant Eliakim son of Hilkiah,'",
      "T": "'And in that day I will call my servant Eliakim, Hilkiah's son,'"
    },
    "21": {
      "L": "'and I will clothe him with your robe and bind your girdle on him, and I will commit your authority into his hand; and he shall be a father to the inhabitants of Jerusalem and to the house of Judah.'",
      "M": "'and I will dress him in your robe and fasten your sash around him; I will hand your authority over to him, and he will be a father to the people of Jerusalem and to the house of Judah.'",
      "T": "'I will dress him in your official robes and cinch your sash around him.\nYour authority I will place in his hands.\nHe will be a father — a true, caring father — to Jerusalem's people and to Judah's household.'"
    },
    "22": {
      "L": "'And I will place on his shoulder the key of the house of David; when he opens, no one shall shut; and when he shuts, no one shall open.'",
      "M": "'I will lay on his shoulder the key of the house of David; what he opens no one will shut, and what he shuts no one will open.'",
      "T": "'I will lay the key of David's house on his shoulder.\nWhen he opens, no one shuts;\nwhen he shuts, no one opens.'\n(Revelation 3:7 applies this verse directly to Christ, the ultimate heir of David's throne and the one who holds the keys of death and Hades.)"
    },
    "23": {
      "L": "'And I will fasten him as a peg in a secure place, and he will become a seat of honour to his father's house.'",
      "M": "'I will drive him in like a peg into a solid place, and he will become a throne of glory to his ancestral household.'",
      "T": "'I will hammer him in like a peg driven into a solid wall —\na fixed point of honour and glory for his entire family.'"
    },
    "24": {
      "L": "'And they will hang on him all the glory of his father's house — the offspring and the issue, all the small vessels from the cups to all the jars.'",
      "M": "'They will hang on him all the honour of his father's household — descendants and offshoots, every vessel from the smallest cup to every jar.'",
      "T": "'And then every dependant of his father's house will load themselves onto him —\noffspring and hangers-on, from the smallest cup to the largest jar,\nevery last piece of the family's glory hung on this one peg.'"
    },
    "25": {
      "L": "'In that day,' declares the LORD of hosts, 'the peg that was fastened in a secure place will give way; it will be cut down and fall, and the load that was upon it will be cut off, for the LORD has spoken.'",
      "M": "'In that day,' declares the LORD of hosts, 'the peg that was driven into the solid place will fail; it will be cut down and fall, and the weight hanging on it will be severed — for the LORD has spoken.'",
      "T": "'But in that day,' Yahweh of hosts declares,\n'even that firmly-set peg will give way.\nIt will be cut down and collapse.\nAnd every weight that was hanging on it will crash to the ground.'\nThe LORD has spoken it."
    }
  },
  "23": {
    "1": {
      "L": "The burden of Tyre. Howl, O ships of Tarshish! For Tyre is laid waste, without house or harbor; from the land of Cyprus it is revealed to them.",
      "M": "The burden of Tyre. Wail, ships of Tarshish! For Tyre is destroyed — no house left standing, no harbour to enter; the news has reached you from Cyprus.",
      "T": "An oracle: Tyre.\nHowl, ships of Tarshish! Wail!\nFor Tyre is destroyed — harbour and house alike gone.\nThe news reaches you from across the sea, from Cyprus."
    },
    "2": {
      "L": "Be silent, O inhabitants of the coastland; the merchants of Sidon who passed over the sea have filled you.",
      "M": "Be still, you people of the coastland — you whom Sidon's merchants, who sailed the seas, once made wealthy.",
      "T": "Fall silent, you coastland people.\nSidon's traders who crossed the great sea — they were the ones who filled your coffers."
    },
    "3": {
      "L": "And on great waters the grain of Shihor, the harvest of the River, was her revenue; she was the marketplace of nations.",
      "M": "The grain of Shihor — the harvest of the Nile — crossed the great waters and became her income; she was the market town of nations.",
      "T": "Egypt's grain shipped down the Nile, harvested from the River's broad banks —\nthat was the cargo that made Tyre rich.\nShe was the marketplace where all the nations came to trade."
    },
    "4": {
      "L": "Be ashamed, O Sidon, for the sea speaks — the stronghold of the sea — saying: 'I have not laboured nor given birth; I have neither reared young men nor brought up young women.'",
      "M": "Be ashamed, O Sidon, for the sea has spoken — the sea's own fortress declares: 'I have not travailed or given birth; I have raised no young men and nurtured no young women.'",
      "T": "Sidon, be ashamed!\nFor the sea itself — the sea, that great stronghold of power — says:\n'I never laboured in childbirth.\nI have no sons I raised up, no daughters I nurtured.'\n(Sidon was Tyre's founding city; Tyre's ruin is the sea's admission of childlessness.)"
    },
    "5": {
      "L": "When the report reaches Egypt, they will be in anguish at the report about Tyre.",
      "M": "When the news reaches Egypt, they will writhe with anguish at what has happened to Tyre.",
      "T": "When Egypt hears the news of Tyre's fall, they will writhe in anguish."
    },
    "6": {
      "L": "Cross over to Tarshish! Howl, O inhabitants of the coastland!",
      "M": "Sail across to Tarshish! Wail, you people of the coastland!",
      "T": "Flee to Tarshish! Sail away!\nHowl, you coastland people — howl!"
    },
    "7": {
      "L": "Is this your exultant city, whose origin is of ancient days, whose feet carried her far away to dwell as a colony?",
      "M": "Is this the city that you once celebrated — so ancient in its origins, a city whose people sailed out to settle far-off shores?",
      "T": "Is this really it — the city that once rang with joy?\nThe city whose roots reach back to ancient days?\nThe city whose people sailed the world to plant colonies across the sea?\nThis is Tyre?"
    },
    "8": {
      "L": "Who has purposed this against Tyre, the city that bestows crowns, whose traders are princes, whose merchants are the honoured of the earth?",
      "M": "Who planned this against Tyre — the crown-bestowing city, whose traders were princes, whose merchants were among the most celebrated people on earth?",
      "T": "Who could have planned this against Tyre?\nTyre — the city that wore a crown and handed out titles!\nTyre, whose merchants were princes,\nwhose traders were the most celebrated names on earth?"
    },
    "9": {
      "L": "The LORD of hosts has purposed it — to defile the pride of all glory, to bring into contempt all the honoured of the earth.",
      "M": "The LORD of hosts planned it — to strip the pride from all magnificence and to humiliate all the famous of the earth.",
      "T": "Yahweh of hosts planned it.\nHis purpose: to puncture the pride of every glittering glory,\nto humiliate every great name the earth has ever honoured."
    },
    "10": {
      "L": "Pass through your land like the Nile, O daughter of Tarshish; there is no restraint anymore.",
      "M": "Flow through your land like the Nile, O daughter of Tarshish; there is nothing to hold you back any longer.",
      "T": "Daughter of Tarshish, flow through your own land like the Nile now —\nthere is nothing left to restrain you.\nThe docking fees, the harbour tolls, the Tyrian merchants — all gone."
    },
    "11": {
      "L": "He stretched out his hand over the sea; he shook the kingdoms; the LORD has given command against Canaan to destroy its strongholds.",
      "M": "The LORD stretched his hand out over the sea and shook the kingdoms; he has issued his order against Phoenicia to demolish its fortresses.",
      "T": "Yahweh stretched his hand across the sea\nand shook the kingdoms at their roots.\nHe issued the order against Canaan:\nDemolish every fortress."
    },
    "12": {
      "L": "And he said: 'You will no longer exult, O crushed virgin daughter of Sidon; arise, cross over to Cyprus — even there you will find no rest.'",
      "M": "He said, 'Your days of celebration are finished, O crushed virgin daughter of Sidon. Get up; cross to Cyprus — but even there you will have no rest.'",
      "T": "'Your days of exulting are over,\nO bruised and ruined daughter of Sidon.\nGet up — sail to Cyprus.\nBut even there, you will not rest.'"
    },
    "13": {
      "L": "Behold the land of the Chaldeans — this people that was nothing until Assyria destined it; they set up their siege towers, stripped its palaces, and made it a ruin.",
      "M": "Look at the land of the Chaldeans — a people who were nothing until Assyria raised them up; they erected siege towers against Tyre, stripped its palaces bare, and turned it to rubble.",
      "T": "Look at the Chaldeans!\nThat people — barely a power until Assyria built them up —\nthey are the ones who raised siege towers,\ntore down every grand building,\nand reduced Tyre to rubble."
    },
    "14": {
      "L": "Howl, O ships of Tarshish, for your stronghold is laid waste!",
      "M": "Wail, ships of Tarshish — your fortress harbour is destroyed!",
      "T": "Ships of Tarshish — howl again!\nYour safe haven is gone. Your source of wealth — laid waste."
    },
    "15": {
      "L": "And in that day Tyre will be forgotten for seventy years, like the days of one king. At the end of seventy years, it will happen to Tyre as in the song of the prostitute:",
      "M": "In that day Tyre will be forgotten for seventy years — the span of one king's lifetime. At the end of seventy years, Tyre will be treated like the woman in the prostitute's song:",
      "T": "In that day Tyre will drop from memory for seventy years —\nthe length of one king's reign.\nAt the end of those seventy years she will come back,\nbut her return will be like the song of a forgotten prostitute:"
    },
    "16": {
      "L": "'Take a harp, go about the city, O forgotten prostitute! Make sweet melody; sing many songs, that you may be remembered.'",
      "M": "'Pick up your harp, walk the streets, O forgotten prostitute; play your sweetest tune and sing song after song so that someone might remember you.'",
      "T": "'Take your harp and walk the streets —\nyou who have been forgotten, you old prostitute!\nPlay sweetly, sing every song you know,\nso someone, somewhere, will still remember you.'"
    },
    "17": {
      "L": "And at the end of seventy years the LORD will visit Tyre, and she will return to her hire and will play the prostitute with all the kingdoms of the world on the face of the earth.",
      "M": "At the end of seventy years the LORD will attend to Tyre, and she will return to her trading — selling herself to all the kingdoms of the world.",
      "T": "At the end of seventy years, Yahweh will deal with Tyre again.\nShe will go back to business — back to selling herself\nto every kingdom across the face of the earth."
    },
    "18": {
      "L": "Her merchandise and her hire will be holy to the LORD; it will not be stored up or hoarded, for her profit will go to those who dwell before the LORD, to eat abundantly and for fine clothing.",
      "M": "But her merchandise and her earnings will be set apart as holy to the LORD; they will not be stored up or hoarded, for her profit will supply those who live before the LORD with abundant food and quality clothing.",
      "T": "But this time her profits will be consecrated to Yahweh —\nnot hoarded, not stored away.\nHer merchandise will feed and clothe those who dwell before Yahweh,\ngiven freely, held lightly, made holy."
    }
  },
  "24": {
    "1": {
      "L": "Behold, the LORD is making the earth empty and making it waste; he is twisting its surface and scattering its inhabitants.",
      "M": "Look — the LORD is emptying the earth and laying it waste; he is distorting its face and scattering its people.",
      "T": "Look — Yahweh is emptying the earth.\nWasting it. Warping its surface. Scattering every living soul."
    },
    "2": {
      "L": "And it shall be: as with the people, so with the priest; as with the servant, so with his master; as with the maid, so with her mistress; as with the buyer, so with the seller; as with the lender, so with the borrower; as with the creditor, so with the debtor.",
      "M": "It will be the same for people and priest, for servant and master, for maid and mistress, for buyer and seller, for lender and borrower, for creditor and debtor.",
      "T": "No one is exempt:\npriest and people — the same fate.\nServant and master, maid and mistress,\nbuyer and seller, lender and borrower,\ncreditor and debtor:\nall of them equally undone."
    },
    "3": {
      "L": "The earth will be utterly emptied and utterly plundered, for the LORD has spoken this word.",
      "M": "The earth will be completely stripped bare and completely ransacked — for the LORD has spoken.",
      "T": "Utterly emptied. Utterly plundered.\nYahweh has decreed it, and that settles it."
    },
    "4": {
      "L": "The earth mourns and withers; the world languishes and withers; the exalted of the people of the earth languish.",
      "M": "The earth mourns and withers; the world droops and fades; the high and mighty of the earth wither away.",
      "T": "The earth grieves; it withers.\nThe world droops and fades.\nEven the proudest people on earth collapse."
    },
    "5": {
      "L": "The earth lies defiled under its inhabitants, for they have transgressed the laws, violated the statutes, broken the everlasting covenant.",
      "M": "The earth lies polluted beneath its inhabitants, because they have violated the laws, broken the ordinances, and shattered the everlasting covenant.",
      "T": "The earth is defiled beneath the weight of its people —\nbecause they violated the laws of creation,\nignored every ordinance,\nand shattered the everlasting covenant that bound heaven to earth."
    },
    "6": {
      "L": "Therefore the curse devours the earth, and its inhabitants bear their guilt; therefore the inhabitants of the earth are scorched, and few people are left.",
      "M": "Therefore a curse is consuming the earth, and its inhabitants suffer the punishment they deserve; therefore the earth's population is burned up and only a remnant survives.",
      "T": "So the curse is eating the earth alive.\nIts people bear the full weight of their guilt.\nThe population is burned away —\nonly a scattered handful left standing."
    },
    "7": {
      "L": "The new wine mourns, the vine languishes, all the merry-hearted groan.",
      "M": "The new wine dries up, the vine withers, and all the joyful sigh with grief.",
      "T": "The new wine is gone; the vine shrivels.\nEvery glad heart has turned to groaning."
    },
    "8": {
      "L": "The mirth of the tambourines ceases; the noise of the joyful ends; the merriment of the harp ceases.",
      "M": "The joyful beating of tambourines stops; the shouting of the revellers ends; the happy strumming of the harp goes silent.",
      "T": "The tambourines fall silent.\nThe noise of the celebrating crowd — finished.\nAll the music of joy — gone."
    },
    "9": {
      "L": "They no longer drink wine with singing; strong drink is bitter to those who drink it.",
      "M": "They drink no more wine to the sound of songs; strong drink turns bitter on the tongue.",
      "T": "No more singing over the wine.\nEvery cup of it turns bitter in the mouth."
    },
    "10": {
      "L": "The city of chaos is broken down; every house is shut up so that no one can enter.",
      "M": "The city of chaos lies in ruins; every house is barred so that no one can enter.",
      "T": "The city of chaos is smashed — undone, returned to the formless void it came from.\nEvery door shut, every house sealed tight,\nno one goes in."
    },
    "11": {
      "L": "There is an outcry in the streets over wine; all joy has grown dark; the gladness of the earth is banished.",
      "M": "In the streets there is a cry for wine; all joy has turned to gloom; the gladness of the earth is driven into exile.",
      "T": "In the streets people are crying out for wine.\nAll joy has gone dark.\nEvery trace of gladness banished from the land."
    },
    "12": {
      "L": "In the city nothing is left but desolation, and the gate is battered into ruins.",
      "M": "Nothing remains in the city but devastation, and the gate is smashed to rubble.",
      "T": "Inside the city: desolation.\nAt the city gate: rubble, shattered beyond repair."
    },
    "13": {
      "L": "For thus it shall be in the midst of the earth among the peoples — as the shaking of an olive tree, as the gleaning of grapes when the vintage is done.",
      "M": "For this is how it will be across the whole earth, among all the peoples — like what remains after the olive harvest, like the few grapes left after the vintage.",
      "T": "This is what will remain when it is all over,\nacross the whole earth and all its peoples:\nwhat you find when you've beaten an olive tree for every last fruit,\nwhat gleaners find when the vintage is through."
    },
    "14": {
      "L": "They lift up their voices; they sing for joy; over the majesty of the LORD they shout from the west.",
      "M": "The survivors raise their voices and sing; they shout from the west over the LORD's majesty.",
      "T": "Then — voices rising from the west:\nthey are singing!\nShouting for joy!\nThe greatness of Yahweh ringing out from across the sea."
    },
    "15": {
      "L": "Therefore in the east give glory to the LORD; in the coastlands of the sea give glory to the name of the LORD, the God of Israel.",
      "M": "Therefore in the eastern regions, give glory to the LORD; in the coastlands of the sea exalt the name of the LORD, the God of Israel.",
      "T": "From the east, glorify Yahweh!\nFrom the islands and coastlands of the sea,\nlift high the name of Yahweh — the God of Israel!"
    },
    "16": {
      "L": "From the ends of the earth we hear songs of praise: 'Glory to the Righteous One!' But I say: 'I waste away, I waste away! Woe is me! The treacherous have betrayed; the treacherous have utterly betrayed!'",
      "M": "From the ends of the earth we hear singing: 'Glory to the Righteous One!' But I say, 'I am wasting away — I am wasting away! Disaster is upon me! The treacherous keep betraying; the traitors have utterly betrayed!'",
      "T": "From the far ends of the earth I hear songs rising — praise songs for the Righteous One.\nBut I cry out: 'I am wasting away — wasting away! Woe to me!\nThe treacherous ones are still at it;\nthe traitors going on and on in their treachery!'"
    },
    "17": {
      "L": "Fear and the pit and the snare are upon you, O inhabitant of the earth!",
      "M": "Terror and the pit and the trap are coming for you, O inhabitants of the earth!",
      "T": "Terror and the pit and the trap —\nthese are coming for everyone who lives on the earth!"
    },
    "18": {
      "L": "And he who flees at the sound of the terror shall fall into the pit, and he who climbs up out of the pit shall be caught in the snare; for the windows of heaven are opened, and the foundations of the earth shake.",
      "M": "Whoever runs from the sound of terror will fall into the pit, and whoever climbs out of the pit will be caught in the trap — for the floodgates of heaven are flung open and the foundations of the earth are shaking.",
      "T": "Run from the terror — and fall into the pit.\nClimb out of the pit — and get caught in the trap.\nThere is no escape route.\nThe windows of heaven have been thrown wide open;\nthe foundations of the earth are shaking."
    },
    "19": {
      "L": "The earth is utterly broken apart; the earth is split through; the earth is violently shaken.",
      "M": "The earth is completely shattered; the earth is split wide open; the earth is violently convulsed.",
      "T": "The earth is cracking apart.\nThe earth is splitting open.\nThe earth is convulsing —"
    },
    "20": {
      "L": "The earth staggers like a drunken man; it sways like a hut; its transgression lies heavy upon it, and it falls and will not rise again.",
      "M": "The earth reels like a drunk; it sways like a flimsy shelter; its rebellion weighs it down until it collapses and does not rise again.",
      "T": "— staggering like a drunk who cannot stand.\nSwaying like a flimsy field-hut in a storm.\nIts own accumulated sin is too heavy to bear.\nDown it goes — and will not rise again."
    },
    "21": {
      "L": "In that day the LORD will punish the host of heaven in heaven, and the kings of the earth on the earth.",
      "M": "In that day the LORD will call to account the powers above in the heavens, and the kings of the earth here below.",
      "T": "In that day Yahweh will call to account\nthe powers that hold dominion in the sky above\nand the kings who hold dominion on the earth below."
    },
    "22": {
      "L": "They will be gathered together as prisoners in a pit; they will be shut up in a dungeon, and after many days they will be punished.",
      "M": "They will be herded like prisoners into a pit, locked up in a dungeon, and after many long days they will be called to account.",
      "T": "They will be rounded up like prisoners,\nherded into a pit, locked in a dungeon.\nAnd after a long, long time —\njudgment will finally come."
    },
    "23": {
      "L": "Then the moon will be abashed and the sun will be ashamed, for the LORD of hosts reigns on Mount Zion and in Jerusalem, and his glory will be before his elders.",
      "M": "Then the moon will be put to shame and the sun confounded, for the LORD of hosts will reign on Mount Zion and in Jerusalem, and his glory will shine before his elders.",
      "T": "Then the moon itself will be put to shame;\nthe sun will blush at its own dimness —\nbecause Yahweh of hosts reigns.\nReigns on Mount Zion.\nReigns in Jerusalem.\nHis glory blazing before the council of his elders."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 22–24 written.')

if __name__ == '__main__':
    main()
