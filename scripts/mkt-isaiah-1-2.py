"""
MKT Isaiah chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-1-2.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — The divine personal name is surfaced in the
  Thought tier throughout Isaiah. Isaiah's poetic address gains force when the reader sees Yahweh
  speak in the first person rather than the abstract title "the LORD."
- H430 (אֱלֹהִים): "God" consistently across all tiers.
- H6918 + H3478 (קְדוֹשׁ יִשְׂרָאֵל): "the Holy One of Israel" across all tiers. This is
  Isaiah's signature epithet for God, appearing ~26× in the book. Consistency is essential.
- H4941 (מִשְׁפָּט): "judgment" (L) / "justice" (M/T) — the Hebrew covers both the act of
  judging and the resulting social order; context in 1:17, 1:21, 1:27 favors "justice."
- H6664 (צֶדֶק): "righteousness" across all tiers — rendered consistently as the covenant-
  aligned character that is both demanded and promised.
- H5315 (נֶפֶשׁ): 1:14 — "my soul hates" (L) / "I utterly hate" (M/T) — the Hebrew idiom
  uses נֶפֶשׁ as an emphatic first-person; English "my soul" imports a Greek dualism not
  present; M/T render the emphatic force instead.
- H6635 (צְבָאוֹת): "of hosts" (L/M) / "Commander of all armies" or "of the heavenly armies"
  (T) — the military/cosmic title affirms Yahweh's supreme sovereignty; T makes it vivid.
- H8451 (תּוֹרָה): "instruction" (L) / "teaching" (M) / "Torah" (T, 2:3) — the T tier
  preserves the full range of the word (law, instruction, narrative, covenant charter) that
  "teaching" or "law" alone cannot carry; transliterating it in T signals this richness.
- H6944 (קֹדֶשׁ): holiness in 2:3 via "God of Jacob" — retained as "the God of Jacob" to
  emphasize the covenant-patriarchal dimension alongside the holiness epithet.
- Hebrew poetry in T tier: Chapters 1–2 are extensively poetic. The T tier uses line breaks
  to honor Hebrew parallelism throughout — especially in the arraignment (1:2-9), the temple-
  speech (1:10-17), and the eschatological vision (2:2-4, 2:10-22). L/M are prose.
- "Scarlet / crimson" (1:18): Double parallel for depth-of-sin, not redundancy; preserved in
  all tiers. The verbs are imperfect — conditional consequents, not unconditional prophecy.
- 2:3 "Torah" rendered as "Torah" (not "the law") in T: Isaiah 2:3 is one of the programmatic
  texts for Torah's eschatological role; the word carries the full Mosaic covenant deposit.
- 2:9 "do not forgive / do not lift them up": The imperative (אַל-תִּשָּׂא) is an intense plea
  or divine self-resolve — "do not pardon them." Rendered as the divine voice speaking.
- Aspect: Waw-consecutive imperfects in narrative sections (1:21 lament, 2:19-21) are rendered
  as narrative past/dramatic present. Prophetic perfects in eschatological sections (2:2-4)
  are rendered as vivid future. No significant MT textual-critical issues in these chapters.
- No H2617 (חֶסֶד) appears directly in chs 1–2, but the covenant-loyalty framework underlies
  the whole arraignment of ch. 1.
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
  "1": {
    "1": {
      "L": "The vision of Isaiah son of Amoz, which he saw concerning Judah and Jerusalem, in the days of Uzziah, Jotham, Ahaz, and Hezekiah, kings of Judah.",
      "M": "The vision that Isaiah son of Amoz received concerning Judah and Jerusalem, during the reigns of Uzziah, Jotham, Ahaz, and Hezekiah, kings of Judah.",
      "T": "The vision that Isaiah son of Amoz saw — a word over Judah and Jerusalem — in the days of Uzziah, Jotham, Ahaz, and Hezekiah, kings of Judah."
    },
    "2": {
      "L": "Hear, O heavens, and give ear, O earth; for the LORD has spoken: Sons I have reared and brought up, but they have rebelled against me.",
      "M": "Hear, O heavens, and listen, O earth, for the LORD has spoken: I reared sons and brought them up to maturity, yet they have rebelled against me.",
      "T": "Hear, O heavens — listen, O earth!\nFor Yahweh himself has spoken:\n\"Sons I raised and nurtured to full strength,\nbut they have turned against me.\""
    },
    "3": {
      "L": "The ox knows its owner and the donkey its master's crib; but Israel does not know, my people do not understand.",
      "M": "An ox knows its owner and a donkey its master's feeding trough; but Israel does not know, my people do not perceive.",
      "T": "An ox knows the man who feeds it;\neven a donkey remembers its master's manger —\nbut Israel knows nothing.\nMy own people will not see."
    },
    "4": {
      "L": "Ah, sinful nation, people laden with iniquity, seed of evildoers, sons who deal corruptly! They have forsaken the LORD, they have despised the Holy One of Israel, they have become estranged, going backward.",
      "M": "Woe to the sinful nation, the people burdened with guilt, a brood of evildoers, children who act destructively! They have abandoned the LORD, they have despised the Holy One of Israel, and have turned their backs on him.",
      "T": "A nation rotted through with sin!\nA people staggering under their own guilt —\noffspring of wrongdoers, children schooled in destruction!\nThey have walked away from Yahweh;\nthey have treated the Holy One of Israel with contempt;\nthey have turned their backs and gone."
    },
    "5": {
      "L": "Why will you still be struck down? Why will you continue to revolt? The whole head is sick and the whole heart is faint.",
      "M": "Why do you invite more punishment? Why do you persist in rebellion? The whole head is diseased and the whole heart is failing.",
      "T": "Why keep inviting the blow? Why go on rebelling?\nFrom head to heart — the whole body is sick;\nfrom crown to core — everything has given way."
    },
    "6": {
      "L": "From the sole of the foot even to the head there is no soundness in it, but wounds and bruises and open sores; they have not been pressed out or bound up or softened with oil.",
      "M": "From the sole of the foot to the top of the head there is not one healthy spot — only wounds, bruises, and open sores, not cleansed or bandaged or soothed with oil.",
      "T": "From the soles of your feet to the top of your head:\nnot a sound place anywhere —\nonly welts, bruises, and festering sores,\nnot pressed clean, not bandaged, not softened with oil."
    },
    "7": {
      "L": "Your country is desolate; your cities are burned with fire; your land — strangers devour it in your presence; it is desolate, as overthrown by strangers.",
      "M": "Your land is desolate and your cities have been burned down; foreigners strip your countryside in your presence — a desolation like the ruin left by invaders.",
      "T": "Your land lies desolate; your cities have been burned to the ground.\nForeigners strip your fields bare while you watch —\na wasteland wrecked as only an enemy can wreck it."
    },
    "8": {
      "L": "And the daughter of Zion is left like a booth in a vineyard, like a shelter in a cucumber field, like a besieged city.",
      "M": "The daughter of Zion is left like a temporary shelter in a vineyard, like a watchman's hut in a cucumber field, like a city under siege.",
      "T": "And the daughter of Zion is abandoned —\na flimsy harvest-hut alone in a vineyard,\na watchman's lean-to in a cucumber patch,\na city that has been ringed and pressed hard."
    },
    "9": {
      "L": "If the LORD of hosts had not left us a very small remnant, we should have been like Sodom, we should have resembled Gomorrah.",
      "M": "If the LORD of hosts had not spared us a tiny surviving remnant, we would have ended up like Sodom and become like Gomorrah.",
      "T": "Had Yahweh, Commander of all armies,\nnot preserved a small surviving seed among us,\nwe would have been Sodom outright —\nnot one stone left standing, like Gomorrah."
    },
    "10": {
      "L": "Hear the word of the LORD, you rulers of Sodom! Give ear to the instruction of our God, you people of Gomorrah!",
      "M": "Hear the word of the LORD, you rulers of Sodom! Listen to the teaching of our God, you people of Gomorrah!",
      "T": "Hear the word of Yahweh, you who rule like Sodom's princes!\nLet the teaching of our God reach your ears, you who live like Gomorrah's people!"
    },
    "11": {
      "L": "What to me is the multitude of your sacrifices? says the LORD. I have had enough of burnt offerings of rams and the fat of well-fed beasts; I do not delight in the blood of bulls or of lambs or of goats.",
      "M": "What do I care for the great number of your sacrifices? says the LORD. I have had enough of burnt offerings of rams and the fat of fattened animals; I take no pleasure in the blood of bulls, lambs, and goats.",
      "T": "\"What do I want with the mass of your sacrifices?\"\nsays Yahweh.\n\"I am sated with burnt rams\nand the grease of well-fattened beasts.\nThe blood of bulls, the blood of lambs and goats —\nI take no delight in any of it.\""
    },
    "12": {
      "L": "When you come to appear before me, who has required this at your hand — the trampling of my courts?",
      "M": "When you come to stand before me, who asked you to trample through my courts?",
      "T": "When you come to stand in my presence —\nwho asked you for this?\nWho invited you to wear out my courts with your feet?"
    },
    "13": {
      "L": "Bring no more vain oblations; incense is an abomination to me. New moon and Sabbath, the calling of a convocation — I cannot endure iniquity and solemn assembly.",
      "M": "Stop bringing me worthless offerings; incense is detestable to me. I cannot tolerate your New Moons, your Sabbaths, and your sacred assemblies alongside evil.",
      "T": "Bring no more hollow offerings;\nyour incense is a stench to me.\nNew moons, sabbaths, called assemblies —\nI cannot stomach evil and sacred ceremony held together."
    },
    "14": {
      "L": "Your new moons and your appointed feasts my soul hates; they have become a burden to me; I am weary of bearing them.",
      "M": "I utterly hate your new moon festivals and your appointed feasts; they have become a burden to me; I am weary of carrying them.",
      "T": "Your new-moon ceremonies and your appointed festivals —\nI find them repulsive.\nThey weigh on me like a load I am too tired to carry any longer."
    },
    "15": {
      "L": "When you spread out your hands, I will hide my eyes from you; even though you make many prayers, I will not listen; your hands are full of blood.",
      "M": "When you raise your hands in prayer, I will avert my eyes; no matter how many prayers you offer, I will not listen — your hands are soaked in blood.",
      "T": "When you stretch out your hands to me in prayer,\nI will shut my eyes.\nWhen you multiply your prayers, I will not hear.\nYour hands are dripping with blood."
    },
    "16": {
      "L": "Wash yourselves; make yourselves clean; remove the evil of your doings from before my eyes; cease to do evil;",
      "M": "Wash and make yourselves clean; remove your evil deeds from my sight; stop doing evil.",
      "T": "Wash off the guilt — make yourselves clean!\nGet the evil of your actions out of my sight.\nStop doing wrong."
    },
    "17": {
      "L": "learn to do good; seek justice, correct oppression; bring justice to the fatherless, plead the widow's cause.",
      "M": "Learn to do what is right: pursue justice, correct the oppressor, defend the orphan, take up the widow's cause.",
      "T": "Learn to do good.\nSeek justice — rein in the oppressor.\nChampion the orphan;\nstand up and argue the widow's case."
    },
    "18": {
      "L": "Come now, and let us reason together, says the LORD: though your sins are like scarlet, they shall be as white as snow; though they are red like crimson, they shall become like wool.",
      "M": "Come now, let us settle this between us, says the LORD: though your sins are like scarlet, they will be made white as snow; though they are red as crimson, they will become like wool.",
      "T": "\"Come now, let us face this together,\" says Yahweh.\n\"Even if your sins are as crimson-red as scarlet dye,\nthey can be made white as snow.\nEven if they are stained deep as dyed wool,\nthey can be made white as fresh fleece.\""
    },
    "19": {
      "L": "If you are willing and obedient, you shall eat the good of the land;",
      "M": "If you are willing and obedient, you will enjoy the best the land produces;",
      "T": "If you are willing and choose to obey,\nyou will feast on the land's finest —"
    },
    "20": {
      "L": "but if you refuse and rebel, you shall be eaten by the sword; for the mouth of the LORD has spoken.",
      "M": "but if you refuse and resist, you will be consumed by the sword — for the mouth of the LORD has spoken.",
      "T": "but if you refuse and go on resisting,\nthe sword will devour you instead.\nFor these are the very words of Yahweh's own mouth."
    },
    "21": {
      "L": "How has the faithful city become a harlot! She was full of justice; righteousness lodged in her, but now murderers.",
      "M": "How the once-faithful city has become a prostitute! Once she was filled with justice and righteousness made its home in her — but now it is murderers.",
      "T": "How the faithful city has become a whore!\nOnce she was brimming with justice;\nrighteousness made its home in her —\nbut now the city belongs to murderers."
    },
    "22": {
      "L": "Your silver has become dross, your best wine mixed with water.",
      "M": "Your silver has turned to worthless dross; your finest wine is diluted with water.",
      "T": "Your silver has become slag;\nyour best wine — watered down."
    },
    "23": {
      "L": "Your princes are rebels and companions of thieves. Everyone loves a bribe and runs after gifts. They do not bring justice for the fatherless, and the widow's cause does not come to them.",
      "M": "Your rulers are rebels and partners in crime. Every one of them loves a bribe and chases after payoffs. They refuse to give the orphan a hearing, and the widow's case never reaches them.",
      "T": "Your officials are rogues — thieves' accomplices, every one.\nThey are all greedy for bribes;\nthey race after their cut.\nThe orphan gets no hearing;\nthe widow's complaint never reaches their ears."
    },
    "24": {
      "L": "Therefore the Lord declares, the LORD of hosts, the Mighty One of Israel: 'Ah, I will ease me of my adversaries and avenge me of my enemies.'",
      "M": "Therefore the Lord, the LORD of hosts, the Mighty One of Israel, declares: 'Enough — I will relieve myself of my foes and take vengeance on my enemies.'",
      "T": "Therefore — this is the declaration of the Sovereign,\nYahweh of the heavenly armies, the Mighty One of Israel:\n\"I will have done with those who oppose me;\nI will satisfy myself against my enemies.\""
    },
    "25": {
      "L": "I will turn my hand against you and will smelt away your dross as with lye and remove all your alloy.",
      "M": "I will raise my hand against you and refine away your dross as with lye and remove all your impurities.",
      "T": "I will bring my hand down hard upon you —\nI will smelt you clean, burning away your slag with caustic lye,\nremoving every trace of alloy."
    },
    "26": {
      "L": "And I will restore your judges as at the first and your counselors as at the beginning. Afterward you shall be called the city of righteousness, the faithful city.",
      "M": "I will restore your judges as in former times and your counselors as in the early days. After that you will be called the City of Righteousness, the Faithful City.",
      "T": "Then I will give you back your rightful judges —\nleaders like those of the former days,\ncounselors like those of old.\nAnd afterward you will be called the City of Righteousness,\nthe Faithful City."
    },
    "27": {
      "L": "Zion shall be redeemed by justice, and those in her who repent, by righteousness.",
      "M": "Zion will be redeemed through justice, and those among her who turn back to God, through righteousness.",
      "T": "Zion will be ransomed through justice;\nand those within her who return will be restored through righteousness."
    },
    "28": {
      "L": "But the destruction of transgressors and sinners shall be together, and those who forsake the LORD shall be consumed.",
      "M": "But rebels and sinners will be crushed together, and those who abandon the LORD will be utterly destroyed.",
      "T": "But rebels and sinners — they will be shattered together;\nthose who have walked away from Yahweh will be burned out."
    },
    "29": {
      "L": "For they shall be ashamed of the oaks that you desired, and you shall blush for the gardens which you have chosen.",
      "M": "For you will be put to shame over the sacred oak trees you desired, and humiliated over the ritual gardens you chose.",
      "T": "You will be put to shame for those oak groves you coveted —\nconfounded by the sacred gardens you made your own."
    },
    "30": {
      "L": "For you shall be like an oak whose leaf withers, and like a garden that has no water.",
      "M": "You will be like an oak tree with withering leaves, and like a garden with no water.",
      "T": "You will be like an oak tree\nwhose leaves curl and wither away —\nlike a garden no rain has reached."
    },
    "31": {
      "L": "And the strong shall become tinder, and his work a spark, and both of them shall burn together, with none to quench them.",
      "M": "The powerful will become like tinder, and their deeds like a spark; both will burn together and no one will put out the fire.",
      "T": "The strong man will become kindling,\nand his deeds the spark that lights him —\nboth will burn together, and no one will quench the fire."
    }
  },
  "2": {
    "1": {
      "L": "The word which Isaiah son of Amoz saw concerning Judah and Jerusalem.",
      "M": "The word that Isaiah son of Amoz saw concerning Judah and Jerusalem.",
      "T": "A word that Isaiah son of Amoz saw — and it concerned Judah and Jerusalem."
    },
    "2": {
      "L": "And it shall come to pass in the latter days that the mountain of the house of the LORD shall be established as the highest of the mountains and shall be lifted up above the hills; and all the nations shall flow to it.",
      "M": "In the last days, the mountain where the LORD's house stands will be established as the highest of all mountains, exalted above every hill, and all nations will stream toward it.",
      "T": "In the days yet to come,\nthe mountain where the LORD's house stands\nshall be set as the crown of all mountains —\nraised above every hill —\nand all the nations will come streaming toward it."
    },
    "3": {
      "L": "And many peoples shall come and say, 'Come, let us go up to the mountain of the LORD, to the house of the God of Jacob, that he may teach us his ways and that we may walk in his paths.' For out of Zion shall go forth the instruction, and the word of the LORD from Jerusalem.",
      "M": "Many peoples will come and say, 'Come, let us go up to the mountain of the LORD, to the house of the God of Jacob, that he may teach us his ways so we can walk in his paths.' For the teaching will go out from Zion and the word of the LORD from Jerusalem.",
      "T": "And many peoples will be saying to one another,\n\"Come — let us go up to the mountain of Yahweh,\nto the house of the God of Jacob.\nLet him instruct us in his ways\nso that we may walk his paths.\"\nFor the Torah will go out from Zion;\nthe word of Yahweh from Jerusalem."
    },
    "4": {
      "L": "He shall judge between the nations and decide for many peoples; and they shall beat their swords into plowshares and their spears into pruning hooks; nation shall not lift up sword against nation, neither shall they learn war anymore.",
      "M": "He will settle disputes between nations and arbitrate for many peoples. Then they will beat their swords into plowshares and their spears into pruning hooks. Nation will not raise sword against nation; they will no longer train for war.",
      "T": "He will arbitrate between the nations\nand settle disputes for peoples far and wide.\nThen they will beat their swords into plowshares\nand their spears into pruning hooks.\nNation will not raise sword against nation;\nwar will no longer be a lesson taught."
    },
    "5": {
      "L": "O house of Jacob, come and let us walk in the light of the LORD.",
      "M": "Come, house of Jacob, let us walk in the light of the LORD!",
      "T": "O family of Jacob — come!\nLet us walk together in the light of Yahweh."
    },
    "6": {
      "L": "For you have forsaken your people, the house of Jacob, because they are filled from the east and are fortune-tellers like the Philistines, and they strike hands with the children of foreigners.",
      "M": "For you, LORD, have rejected your people, the house of Jacob, because they have adopted practices from the east and practice divination like the Philistines, and they make agreements with foreigners.",
      "T": "For you have cast off your own people, the house of Jacob —\nbecause they have filled themselves with customs from the east,\ndabble in divination like the Philistines,\nand strike deals with every foreign nation."
    },
    "7": {
      "L": "And their land is full of silver and gold, and there is no end to their treasures; and their land is full of horses, and there is no end to their chariots.",
      "M": "Their land is full of silver and gold with no end to their treasures; their land is full of horses with no end to their chariots.",
      "T": "Their land is glutted with silver and gold —\ntreasures without limit;\ntheir land packed with horses —\nchariots beyond counting."
    },
    "8": {
      "L": "And their land is full of idols; they bow down to the work of their hands, to what their own fingers have made.",
      "M": "Their land is full of idols; they worship what their own hands have made, what their own fingers have fashioned.",
      "T": "Their land is choked with idols.\nThey bow down before the work of their own hands,\nbefore what their own fingers have shaped."
    },
    "9": {
      "L": "And man is bowed down and each man is humbled — do not forgive them!",
      "M": "Mankind is brought low and every person humbled — do not forgive them!",
      "T": "So human beings are being bent down;\nevery person is being brought low.\nDo not lift them up!"
    },
    "10": {
      "L": "Enter into the rock and hide in the dust from before the terror of the LORD and from the glory of his majesty.",
      "M": "Hide yourself in the rocky cliffs and bury yourself in the dust from before the terrifying presence of the LORD and the splendor of his majesty.",
      "T": "Crawl into the rock!\nBury yourself in the dust!\nHide from the terror of Yahweh —\nfrom the blinding splendor of his majesty."
    },
    "11": {
      "L": "The high looks of man shall be humbled and the haughtiness of men shall be bowed down, and the LORD alone shall be exalted in that day.",
      "M": "The arrogant gaze of mankind will be brought low and human pride will be humbled; on that day the LORD alone will be exalted.",
      "T": "The proud gaze of humanity will be brought to the ground;\nhuman arrogance will be flattened —\nand Yahweh alone will stand high on that day."
    },
    "12": {
      "L": "For the LORD of hosts has a day against all that is proud and lofty, and against all that is lifted up — it shall be brought low;",
      "M": "For the LORD of hosts has appointed a day against everything proud and exalted, against everything lifted high — it will be humbled.",
      "T": "For Yahweh, Commander of all armies, has set a day —\na day against everything that has made itself great,\nagainst every towering pride —\nand it will all be brought crashing down."
    },
    "13": {
      "L": "and against all the cedars of Lebanon, lofty and lifted up, and against all the oaks of Bashan;",
      "M": "against all the towering cedars of Lebanon and all the oaks of Bashan;",
      "T": "Against every cedar of Lebanon, sky-high and proud;\nagainst every oak of Bashan."
    },
    "14": {
      "L": "and against all the high mountains and against all the uplifted hills;",
      "M": "against all the high mountains and against all the elevated hills;",
      "T": "Against every high mountain;\nagainst every swelling hill."
    },
    "15": {
      "L": "and against every high tower and against every fortified wall;",
      "M": "against every tall tower and against every fortified wall;",
      "T": "Against every tall tower;\nagainst every fortified wall."
    },
    "16": {
      "L": "and against all the ships of Tarshish and against all the beautiful craft.",
      "M": "against all the merchant ships of Tarshish and against all their prized vessels.",
      "T": "Against every ship bound for Tarshish;\nagainst every elegant vessel."
    },
    "17": {
      "L": "And the haughtiness of man shall be bowed down and the pride of men shall be humbled, and the LORD alone shall be exalted in that day.",
      "M": "Human pride will be brought low and human arrogance will be humbled; on that day the LORD alone will be exalted.",
      "T": "Human arrogance will be bent to the ground;\nhuman pride will be leveled —\nand Yahweh alone will be raised high on that day."
    },
    "18": {
      "L": "And the idols shall utterly vanish.",
      "M": "And the idols will completely disappear.",
      "T": "As for the idols — they will simply cease to be."
    },
    "19": {
      "L": "And they shall enter the caves of the rocks and the holes of the ground from before the terror of the LORD and from the glory of his majesty, when he rises to terrify the earth.",
      "M": "People will go into the caverns of the rocks and the holes of the ground to escape the terrifying presence of the LORD and the splendor of his majesty, when he rises to make the earth tremble.",
      "T": "Then people will scramble into rocky caves\nand burrow into holes in the ground —\nfleeing Yahweh's terrifying presence,\nthe blinding glory of his majesty,\nwhen he rises to make the earth tremble."
    },
    "20": {
      "L": "In that day a man shall cast away his silver idols and his gold idols which they made for themselves to worship, to the moles and to the bats;",
      "M": "On that day people will throw away their silver idols and gold idols, which they made for themselves to worship, flinging them to the moles and the bats.",
      "T": "On that day, every person will hurl away\nthe silver and gold idols they fashioned for themselves —\ncasting them to the moles,\ntossing them to the bats."
    },
    "21": {
      "L": "to enter the clefts of the rocks and the crevices of the crags from before the terror of the LORD and from the glory of his majesty, when he rises to terrify the earth.",
      "M": "They will hide in the clefts of the rocky crags and the fissures of the cliffs to escape the terrifying presence of the LORD and the splendor of his majesty, when he rises to make the earth tremble.",
      "T": "They will press into rock-clefts,\nwedge themselves into the cracks of the crags —\nall to flee Yahweh's terrifying presence,\nthe blinding glory of his majesty,\nwhen he rises to make the earth tremble."
    },
    "22": {
      "L": "Cease from man in whose nostrils is breath, for of what account is he?",
      "M": "Stop trusting in mere mortals, who have nothing but a breath in their nostrils — what are they really worth?",
      "T": "Stop trusting in human beings,\nwho have no more than a breath in their nostrils.\nOf what lasting account is such a person?"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 1–2 written.')

if __name__ == '__main__':
    main()
