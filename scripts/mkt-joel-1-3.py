"""
MKT Joel chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-joel-1-3.py

=== CHAPTER OVERVIEW ===

Joel is a prophet of Judah; his dates are disputed (900–400 BCE range). The book
centres on a devastating locust plague as both historical crisis and prophetic lens
onto the coming Day of the LORD. Its three chapters move from lament (ch. 1) to
eschatological vision (chs. 2–3) in a single sweep.

Chapter 1: Locust Plague — Call to Lament.
  The superscription (v.1) is followed by a call for all generations to hear this
  unprecedented disaster (vv.2–4). Four waves of locusts have stripped the land.
  Four groups are summoned to mourn: drunkards (vv.5–7), the nation (v.8), farmers
  (vv.9–12), and priests (vv.13–14). A meditation on the approaching Day of the
  LORD (vv.15–18) closes with Joel's own prayer (vv.19–20).

Chapter 2: The Cosmic Army and the Call to Repentance.
  vv.1–11: An invading army is described in terrifying, apocalyptic language —
  its advance darkens the sky and shakes the earth; the LORD leads it.
  vv.12–17: The book's hinge — a call to return with whole hearts, rend hearts
  not garments, assemble all the people, let the priests intercede.
  vv.18–27: Yahweh's response: pity for the land, restoration of crops, the
  four years of locust damage undone.
  vv.28–32: The great eschatological promise — Spirit poured on all flesh, cosmic
  signs, salvation for all who call on the LORD's name (cited by Peter in Acts 2).

Chapter 3: Judgment of the Nations and the Restoration of Zion.
  vv.1–3: Gathering of all nations to the Valley of Jehoshaphat for judgment;
  the nations' crimes listed (scattering Israel, selling children).
  vv.4–8: Specific indictment of Tyre, Sidon, and Philistia — their plunder will
  be repaid.
  vv.9–17: The nations summoned to the valley; Joel reverses the swords-to-
  plowshares oracle of Isaiah 2:4 / Micah 4:3 (plowshares → swords, v.10).
  vv.18–21: Eschatological abundance for Zion; Egypt and Edom laid waste; Judah
  inhabited forever.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh): Following the Hosea convention established in
  mkt-hosea-1-6.py. L/M: "LORD" (small-caps convention). T: "Yahweh" in
  prophetic-oracle and covenantally weighted contexts (oracles, the Day of the
  LORD passages, the Spirit-outpouring promise), and "the LORD" in narrative
  and report contexts.

- H430 (אֱלֹהִים / Elohim): "God" in all tiers. No tier preserves the grammatical
  plural since Joel's context is unambiguously monotheistic.

- יוֹם יְהוָה (the Day of the LORD): The book's theological centrepiece. L/M:
  "the day of the LORD" (lower case, standard). T: "the Day of the LORD"
  (capitalised to signal the book's eschatological weight); at the first
  occurrence (1:15) T adds a gloss — subsequent occurrences use the capitalised
  form without gloss.

- H7307 (רוּחַ / ruah): In 2:28–29 the referent is explicitly the divine Spirit
  poured from above on all flesh (the Pentecost passage). All three tiers: "my
  Spirit" / "Spirit" with capital S. This is the only occurrence of ruah in Joel;
  no lowercase "spirit/wind" uses arise.

- H2617 (חֶסֶד / hesed): Appears at 2:13 as part of the classic covenant
  characterisation (Exod 34:6). L: "steadfast love." M: "covenant loyalty."
  T: "covenant faithfulness." The rendering carries the full freight of covenant
  obligation + active mercy.

- Four locust terms (1:4 and 2:25):
    H1501 גֶּזֶם (gazam): L/M: "cutting locust." T: "cutting locust." (KJV: palmerworm)
    H697 אַרְבֶּה (arbeh): L/M: "swarming locust." T: "swarming locust." (KJV: locust)
    H3218 יֶלֶק (yeleq): L/M: "hopping locust." T: "hopping locust." (KJV: cankerworm)
    H2625 חָסִיל (hasil): L/M: "stripping locust." T: "stripping locust." (KJV: caterpillar)
  In 1:4 the order is: gazam → arbeh → yeleq → hasil (cutting → swarming → hopping →
  stripping). In 2:25 the LORD mentions all four as his "great army." All tiers use
  the same terminology for consistency.

- H7706 (שַׁדַּי / Shaddai): "the Almighty" in all tiers at 1:15. The Hebrew
  verse contains a paronomasia: כְּשֹׁד מִשַּׁדַּי (like destruction from the
  Almighty) — shod (destruction) echoes Shaddai. T surfaces this wordplay.

- H6666 (צְדָקָה / tsedaqah) at 2:23: The KJV renders this "moderately," which
  is questionable. The term means "righteousness / vindication / covenant
  faithfulness." Most modern versions: "for your vindication" (NRSV) or
  "in his faithfulness" (NIV). L: "for your vindication." M: "as a sign of
  his faithfulness." T: "because he is keeping faith with you."

- H6828 (צְפוֹנִי / tsephoni, "the northerner") at 2:20: This mysterious figure
  — grammatically singular but the subject of the locust army in context — is
  probably the locust swarm's direction of origin (north) personified. L/M:
  "the northerner." T: "the northern invader," making the army referent explicit.

- "Valley of Jehoshaphat" (H6010 + H3092, יוֹשָׁפָט / Yoshaphat) at 3:2 and
  3:12: The name means "Yahweh judges." No specific valley is identified with
  certainty. L/M: "the Valley of Jehoshaphat." T at first mention (3:2): "the
  Valley of Jehoshaphat — where the LORD judges" to surface the etymological
  theological meaning; subsequent uses: "the Valley of Jehoshaphat."

- "Valley of Decision" (H6010 + H2742, עֵמֶק הֶחָרוּץ / emeq hecharuts) at 3:14:
  This is distinct from the Valley of Jehoshaphat — the term charuts means
  "decision/threshing/incision." L/M: "the valley of decision." T: "the Valley
  of Decision — where the verdict will fall."

- 3:10 reversal of Isa 2:4 / Mic 4:3: Joel intentionally inverts the
  plowshares-to-swords oracle of Isaiah 2:4 and Micah 4:3. T surfaces this
  inversion explicitly. L/M render literally.

- Poetic structure: Joel contains extensive poetry. In the T tier, poetic verses
  (especially the lament material of ch. 1, the army description of 2:1–11, the
  restoration hymn of 2:19–27, and the eschatological visions of chs. 2–3) are
  rendered with line breaks to preserve parallelism and cadence. M uses flowing
  prose. L preserves source word order even where awkward.

- Hebrew aspect: Perfect verbs in prophetic oracles (especially in ch. 2 divine
  speech) represent certainty of future fulfilment; rendered as English simple
  past or present depending on whether the event is presented as already
  accomplished in divine purpose. Imperfects = ongoing/future action. T makes
  the rhetorical urgency of each shift explicit.

- Divine passive: Several verbs in ch. 1 describing the locust devastation imply
  God as agent (e.g., "the grain offering is cut off"). L/M render the passive
  form; T may make divine agency explicit where the context bears it.

- OT intertextuality:
    2:13: Cites the Sinai self-disclosure formula (Exod 34:6) — T notes the
    allusion.
    2:28–32: Fulfilled at Pentecost (Acts 2:17–21) — T renders the eschatological
    register fully; the phrase "all flesh" is kept rather than domesticated.
    3:10: Deliberate inversion of Isa 2:4 / Mic 4:3. T notes this.
    3:18: The river from the house of the LORD echoes Ezek 47 and anticipates
    Rev 22. T surfaces the trajectory.
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

JOEL = {
    "1": {
        "1": {
            "L": "The word of the LORD that came to Joel the son of Pethuel.",
            "M": "The word of the LORD that came to Joel son of Pethuel.",
            "T": "This is the word of Yahweh that came to Joel son of Pethuel."
        },
        "2": {
            "L": "Hear this, ye old men, and give ear, all ye inhabitants of the land. Hath this been in your days, or even in the days of your fathers?",
            "M": "Hear this, you elders; listen closely, all inhabitants of the land. Has anything like this ever happened in your days, or in the days of your ancestors?",
            "T": "Listen to this, you elders — and everyone living in the land, pay close attention. Has anything like this ever happened in your lifetime, or in your fathers' time?"
        },
        "3": {
            "L": "Tell ye your children of it, and let your children tell their children, and their children another generation.",
            "M": "Tell your children about it, and let your children tell their children, and their children to the next generation.",
            "T": "Pass it on to your children. Let your children tell it to their children, and their children to the generation after them."
        },
        "4": {
            "L": "That which the cutting locust left, the swarming locust has eaten; that which the swarming locust left, the hopping locust has eaten; and that which the hopping locust left, the stripping locust has eaten.",
            "M": "What the cutting locust left, the swarming locust has eaten; what the swarming locust left, the hopping locust has eaten; and what the hopping locust left, the stripping locust has eaten.",
            "T": "Wave after wave of them came:\nwhat the cutting locust left behind, the swarming locust devoured;\nwhat the swarming locust left, the hopping locust consumed;\nand what the hopping locust left, the stripping locust stripped away."
        },
        "5": {
            "L": "Awake, ye drunkards, and weep; and howl, all ye drinkers of wine, because of the sweet wine; for it is cut off from your mouth.",
            "M": "Wake up, you drunkards, and weep! Wail, all you wine drinkers, because of the sweet wine — it has been cut off from your lips.",
            "T": "Wake up, you drunkards, and weep!\nHowl, all you who love your wine —\nthe new wine has been taken right off your lips."
        },
        "6": {
            "L": "For a nation has come up upon my land, strong, and without number; his teeth are the teeth of a lion, and he has the jaw teeth of a great lion.",
            "M": "For a nation has invaded my land — powerful and beyond counting; its teeth are like lions' teeth, and it has the jaw teeth of a lioness.",
            "T": "A nation — vast and past numbering — has swept over my land.\nIts teeth are the teeth of a lion;\nit has the crushing jaws of a great lion."
        },
        "7": {
            "L": "He has laid my vine waste, and barked my fig tree; he has stripped it bare and cast it away; its branches are made white.",
            "M": "It has stripped my vine bare and splintered my fig tree; it has peeled off all the bark and thrown the branches aside, leaving the wood white.",
            "T": "My vine has been laid waste, my fig tree ruined —\nthe bark stripped off, the branches broken and flung away,\nthe wood left bare and white."
        },
        "8": {
            "L": "Lament like a virgin girded with sackcloth for the husband of her youth.",
            "M": "Mourn like a young woman dressed in sackcloth, grieving for the husband of her youth.",
            "T": "Mourn — like a young bride wearing sackcloth\nand weeping for the husband she loved in her youth."
        },
        "9": {
            "L": "The grain offering and the drink offering are cut off from the house of the LORD; the priests, the ministers of the LORD, mourn.",
            "M": "The grain offering and the drink offering are cut off from the house of the LORD; the priests, the ministers of the LORD, are in mourning.",
            "T": "The grain offering and the drink offering are gone —\ncut off from the house of Yahweh.\nThe priests, Yahweh's ministers, mourn."
        },
        "10": {
            "L": "The field is laid waste, the ground mourns; for the grain is dried up, the new wine has dried up, the olive oil languishes.",
            "M": "The fields are ruined; the soil is in mourning. The grain is destroyed, the new wine dries up, the olive oil fails.",
            "T": "The fields lie ruined; the very earth is in mourning.\nThe grain is gone, the new wine has failed,\nthe olive oil has dried to nothing."
        },
        "11": {
            "L": "Be ashamed, O farmers; wail, O vinedressers, for the wheat and for the barley; because the harvest of the field has perished.",
            "M": "Be ashamed, O farmers; wail, O vinedressers — for the wheat and for the barley — because the harvest of the field is lost.",
            "T": "Farmers, hang your heads in shame!\nVinedressers, wail —\nthe wheat and barley harvests are gone,\neverything the fields were to yield."
        },
        "12": {
            "L": "The vine has dried up, and the fig tree has withered; the pomegranate tree, the palm tree also, and the apple tree, even all the trees of the field, are withered; because joy has withered away from the sons of men.",
            "M": "The vine has dried up and the fig tree withers — the pomegranate, the palm, and the apple tree, all the trees of the field — they have all withered. Joy itself has withered away from the sons of men.",
            "T": "The vine is dry, the fig tree shrivelled;\npomegranate, palm, and apple tree —\nevery tree of the field has withered.\nAnd with them, all joy has withered\nfrom the children of Adam."
        },
        "13": {
            "L": "Gird yourselves and lament, O priests; wail, O ministers of the altar. Come, lie all night in sackcloth, O ministers of my God, for the grain offering and drink offering are withheld from the house of your God.",
            "M": "Put on sackcloth and lament, O priests; wail, O ministers of the altar. Come, spend the night in sackcloth, O ministers of my God, for the grain offering and drink offering are withheld from the house of your God.",
            "T": "Dress yourselves in sackcloth and lament, O priests!\nHowl, you ministers of the altar!\nCome, spend the night in sackcloth, you who serve my God —\nfor the grain offering and drink offering\nhave been cut off from your God's house."
        },
        "14": {
            "L": "Consecrate a fast, call a solemn assembly; gather the elders and all the inhabitants of the land into the house of the LORD your God, and cry out to the LORD.",
            "M": "Consecrate a fast; call a solemn assembly. Gather the elders and all the inhabitants of the land to the house of the LORD your God, and cry out to the LORD.",
            "T": "Call a fast. Summon a solemn assembly.\nBring together the elders and every inhabitant of the land\nto the house of Yahweh your God,\nand cry out to Yahweh."
        },
        "15": {
            "L": "Alas for the day! For the day of the LORD is near, and it comes as destruction from the Almighty.",
            "M": "Alas for the day! For the day of the LORD is near, and it comes as devastation from the Almighty.",
            "T": "What a day that will be —\nfor the Day of the LORD is near,\ncatastrophe surging from the Almighty himself.\n(In Hebrew, the very word for destruction — shod — echoes the name Shaddai.)"
        },
        "16": {
            "L": "Is not the food cut off before our eyes, yea, joy and gladness from the house of our God?",
            "M": "Is not the food already cut off before our eyes, and joy and gladness from the house of our God?",
            "T": "Can we not see it with our own eyes —\nfood gone, joy gone,\ngladness stripped from the house of our God?"
        },
        "17": {
            "L": "The seeds have shrivelled under their clods; the storehouses are desolate, the granaries are torn down, for the grain has dried up.",
            "M": "The seeds have shrivelled in the ground; the storehouses stand empty; the granaries are torn down, for the grain has withered.",
            "T": "Seeds rot beneath the clods of earth;\ngranaries lie empty and broken;\nthe grain has shrivelled away."
        },
        "18": {
            "L": "How the beasts groan! The herds of cattle are bewildered, because they have no pasture; yea, the flocks of sheep are made desolate.",
            "M": "How the animals groan! The herds of cattle are confused because there is no pasture for them; even the flocks of sheep waste away.",
            "T": "Listen — the animals are groaning.\nThe cattle herds mill about bewildered: no pasture anywhere.\nEven the flocks of sheep suffer."
        },
        "19": {
            "L": "To you, O LORD, I will cry, for fire has devoured the pastures of the wilderness, and a flame has burned all the trees of the field.",
            "M": "To you, O LORD, I cry out. For fire has devoured the open pastures and flame has burned all the trees of the field.",
            "T": "To you, Yahweh, I cry out —\nfire has devoured the open pastures,\nflame has burned every tree of the field."
        },
        "20": {
            "L": "Yea, the beasts of the field also cry out to you, for the water brooks are dried up, and fire has devoured the pastures of the wilderness.",
            "M": "Even the wild animals pant and cry to you, for the water brooks have dried up and fire has devoured the pastures of the wilderness.",
            "T": "Even the wild animals cry out to you:\nthe streams have gone dry;\nfire has consumed the open pastures."
        }
    },
    "2": {
        "1": {
            "L": "Blow the trumpet in Zion, and sound an alarm in my holy mountain; let all the inhabitants of the land tremble, for the day of the LORD is coming, for it is at hand —",
            "M": "Blow the trumpet in Zion; sound the alarm on my holy mountain! Let all the inhabitants of the land tremble, for the day of the LORD is coming; it is near —",
            "T": "Sound the war-horn in Zion!\nRaise the alarm on my holy mountain!\nLet every inhabitant of the land tremble —\nfor the Day of the LORD is coming, and it is nearly here —"
        },
        "2": {
            "L": "a day of darkness and gloom, a day of clouds and thick darkness; like the dawn spreading over the mountains, a great and mighty people; their like has never been before, nor shall there be after them, even to the years of many generations.",
            "M": "a day of darkness and gloom, a day of clouds and thick darkness. Like the dawn spreading over the mountains, there comes a great and powerful people; nothing like them has ever existed before, and nothing like them will exist again through the years of many generations.",
            "T": "a day of darkness and deep gloom,\na day of clouds and dense shadow —\nlike the dawn rolling over the mountains comes a great and powerful horde.\nNothing like it has ever been before,\nand nothing like it will come again\nthrough all the generations to come."
        },
        "3": {
            "L": "Before them a fire devours, and behind them a flame burns; before them the land is like the garden of Eden, and behind them a desolate wilderness; and nothing shall escape them.",
            "M": "Before them a fire devours, and behind them a flame burns. Before them the land is like the garden of Eden; behind them a desolate wilderness — and nothing escapes them.",
            "T": "Fire devours before them;\nflame burns behind them.\nBefore their advance: a garden, like Eden.\nBehind their passing: a wilderness of ruin.\nNothing, and no one, escapes."
        },
        "4": {
            "L": "Their appearance is as the appearance of horses; and as horsemen, so shall they run.",
            "M": "Their appearance is like that of horses; and like war horses, so they charge.",
            "T": "They look like horses;\nlike cavalry they charge forward."
        },
        "5": {
            "L": "Like the noise of chariots on the tops of mountains shall they leap, like the noise of a flame of fire that devours the stubble, as a mighty people set in battle array.",
            "M": "Like the rumbling of chariots they leap over the mountaintops, like the crackling of a flame of fire consuming the stubble, like a mighty army drawn up for battle.",
            "T": "The sound of them is like war-chariots\nclattering over mountain peaks,\nlike a wildfire crackling through dry stubble —\na powerful army in battle formation."
        },
        "6": {
            "L": "Before them peoples are in anguish; all faces gather blackness.",
            "M": "Before them peoples writhe in anguish; every face turns pale.",
            "T": "Peoples writhe with terror at their approach;\nevery face drains of colour."
        },
        "7": {
            "L": "They shall run like mighty men; they shall climb the wall like men of war; and they shall march every one on his ways, and they shall not break their ranks.",
            "M": "Like warriors they run; like soldiers they scale the wall. Each one keeps to his own course; they do not swerve from their paths.",
            "T": "They run like soldiers;\nthey scale the wall like trained warriors.\nEach one holds his own lane;\nthey never break formation."
        },
        "8": {
            "L": "Neither shall one thrust another; they shall walk every one in his path; and they fall upon the sword, they shall not be wounded.",
            "M": "They do not push each other; each advances in his own track. They burst through the weapons without being stopped.",
            "T": "They don't crowd each other;\neach moves in his own assigned path.\nEven the sharpest weapons cannot stop them —\nthey cut through without slowing down."
        },
        "9": {
            "L": "They shall run to and fro in the city; they shall run upon the wall; they shall climb up upon the houses; they shall enter in at the windows like a thief.",
            "M": "They rush through the city; they run along the walls; they climb up into the houses; they enter through the windows like a thief.",
            "T": "They swarm through the city,\nrun along the walls,\nclimb into the houses,\nslip in through the windows like a thief."
        },
        "10": {
            "L": "The earth shall quake before them; the heavens shall tremble; the sun and the moon shall be dark, and the stars shall withdraw their shining.",
            "M": "Before them the earth quakes, the heavens tremble; the sun and the moon grow dark, and the stars withdraw their shining.",
            "T": "The earth shudders at their coming;\nthe heavens themselves tremble.\nSun and moon go dark;\nthe stars pull back their light."
        },
        "11": {
            "L": "And the LORD utters his voice before his army; for his camp is very great; for he is mighty who executes his word; for the day of the LORD is great and very terrible; and who can endure it?",
            "M": "The LORD utters his voice before his army, for his forces are exceedingly great; he who executes his word is powerful. For the day of the LORD is great and very awesome — who can endure it?",
            "T": "Yahweh thunders at the head of his army —\nhis host is immense beyond reckoning;\nthe one who carries out his command is mighty.\nThe Day of the LORD is vast and terrifying —\nwho can possibly stand before it?"
        },
        "12": {
            "L": "'Yet even now,' declares the LORD, 'return to me with all your heart, with fasting, and with weeping, and with mourning.'",
            "M": "'Yet even now,' declares the LORD, 'return to me with all your heart, with fasting, with weeping, and with mourning.'",
            "T": "'Even now,' Yahweh declares,\n'return to me with all your heart —\nwith fasting, with weeping, with mourning.'"
        },
        "13": {
            "L": "And rend your heart and not your garments, and return to the LORD your God; for he is gracious and merciful, slow to anger, and of great steadfast love, and he relents over disaster.",
            "M": "Rend your hearts and not your garments. Return to the LORD your God, for he is gracious and merciful, slow to anger, and abounding in covenant loyalty; and he relents over disaster.",
            "T": "Tear open your hearts, not just your garments.\nReturn to Yahweh your God —\nfor he is gracious and compassionate,\nslow to anger and rich in covenant faithfulness;\nhe turns back from sending disaster.\n(This is the ancient self-disclosure of Sinai, Exod 34:6, spoken again in crisis.)"
        },
        "14": {
            "L": "Who knows whether he will not turn and relent, and leave a blessing behind him, a grain offering and a drink offering for the LORD your God?",
            "M": "Who knows? He may turn and relent and leave behind a blessing — a grain offering and a drink offering for the LORD your God.",
            "T": "Who knows — he might turn back;\nhe might change course and leave a blessing in his wake,\na grain offering and a drink offering for Yahweh your God."
        },
        "15": {
            "L": "Blow the trumpet in Zion; consecrate a fast; call a solemn assembly.",
            "M": "Blow the trumpet in Zion; consecrate a fast; call a solemn assembly.",
            "T": "Sound the horn in Zion —\ncall a fast, summon a solemn gathering."
        },
        "16": {
            "L": "Gather the people, sanctify the congregation, assemble the elders; gather the children and those nursing at the breast; let the bridegroom leave his chamber, and the bride her canopy.",
            "M": "Gather the people; consecrate the congregation; assemble the elders; gather the children and the nursing infants. Let the bridegroom leave his room and the bride her canopy.",
            "T": "Bring everyone together — every generation, every class.\nAssemble the elders; bring the children;\nbring even the nursing infants.\nThe bridegroom must leave his room,\nthe bride her bridal canopy."
        },
        "17": {
            "L": "Let the priests, the ministers of the LORD, weep between the vestibule and the altar, and let them say, 'Spare your people, O LORD, and give not your heritage to reproach, that the nations should rule over them; why should they say among the peoples, Where is their God?'",
            "M": "Between the vestibule and the altar let the priests, the ministers of the LORD, weep and say, 'Spare your people, O LORD, and do not make your heritage a reproach, a byword among the nations. Why should they say among the peoples, Where is their God?'",
            "T": "Let the priests stand between the entrance porch and the altar, weeping,\nand let them pray:\n'Spare your people, Yahweh —\ndo not make your own heritage an object of scorn,\na joke for the nations to repeat.\nWhy should they be saying:\n\"Where is their God?\"'"
        },
        "18": {
            "L": "Then the LORD was jealous for his land and had pity on his people.",
            "M": "Then the LORD became zealous for his land and had compassion on his people.",
            "T": "Then Yahweh became fiercely jealous for his land\nand took pity on his people."
        },
        "19": {
            "L": "The LORD answered and said to his people, 'Behold, I am sending to you grain and wine and oil, and you shall be satisfied; and I will no more make you a reproach among the nations.'",
            "M": "The LORD answered and said to his people: 'Behold, I am sending you grain, wine, and oil, and you will be satisfied; and I will no more make you a reproach among the nations.'",
            "T": "Yahweh answered his people and said:\n'I am sending you grain and wine and oil —\nyou will be satisfied at last.\nI will never again make you a disgrace\namong the nations.'"
        },
        "20": {
            "L": "I will remove the northerner far from you, and drive him into a parched and desolate land, with his face toward the eastern sea and his rear toward the western sea; his stench shall come up, and his foul smell shall rise, because he has done great things.",
            "M": "I will drive the northern invader far from you, into a parched and desolate land, his van into the eastern sea and his rear into the western sea; the stench and foul odour of him will rise, for he has committed great outrages.",
            "T": "I will push the northern invader far away from you —\nout into a dry and barren land,\nhis front ranks driven into the Dead Sea,\nhis rear into the Mediterranean.\nThe stench of his rotting corpses will rise up —\nfor he raised himself too high."
        },
        "21": {
            "L": "Fear not, O land; be glad and rejoice, for the LORD has done great things.",
            "M": "Fear not, O land; be glad and rejoice, for the LORD has done great things.",
            "T": "Do not be afraid, O land —\nbe glad and rejoice,\nfor Yahweh has done something magnificent."
        },
        "22": {
            "L": "Fear not, you beasts of the field, for the pastures of the wilderness shall spring up; the tree shall bear its fruit; the fig tree and vine shall yield their full strength.",
            "M": "Fear not, you wild animals, for the pastures of the wilderness are green again; the trees are bearing fruit; the fig tree and vine are yielding their full harvest.",
            "T": "Animals of the open country, have no fear —\nthe wilderness pastures are green again;\nthe trees are bearing fruit;\nthe fig tree and vine are full and heavy."
        },
        "23": {
            "L": "Be glad then, O children of Zion, and rejoice in the LORD your God, for he has given you the early rain for your vindication; he has poured down for you abundant rain, the early and latter rain, as before.",
            "M": "Be glad, O children of Zion, and rejoice in the LORD your God, for he has given the early rain as a sign of his faithfulness; he has sent down for you abundant rain, the early rain and the latter rain, as before.",
            "T": "Children of Zion, rejoice!\nBe glad in Yahweh your God —\nfor he has sent the early rain because he is keeping faith with you.\nHe has poured down for you the autumn rains\nand the spring rains, as it used to be."
        },
        "24": {
            "L": "The threshing floors shall be full of grain; the vats shall overflow with wine and oil.",
            "M": "The threshing floors shall be full of grain; the vats shall overflow with wine and oil.",
            "T": "The threshing floors will be full of grain;\nthe wine vats and the oil vats will overflow."
        },
        "25": {
            "L": "I will restore to you the years that the swarming locust has eaten, the hopping locust, and the stripping locust, and the cutting locust, my great army that I sent among you.",
            "M": "I will restore to you the years that the swarming locust has eaten — the hopping locust, the stripping locust, and the cutting locust — my great army that I sent among you.",
            "T": "I will give back the years\nthat the swarming locust ate —\nthe hopping locust, the stripping locust, the cutting locust —\nmy great army that I unleashed against you."
        },
        "26": {
            "L": "You shall eat in plenty and be satisfied, and praise the name of the LORD your God, who has dealt wondrously with you; and my people shall never be put to shame.",
            "M": "You shall eat in plenty and be satisfied, and praise the name of the LORD your God, who has dealt wondrously with you. And my people shall never again be put to shame.",
            "T": "You will eat abundantly and be full,\nand you will praise the name of Yahweh your God\nwho has done wonders among you.\nMy people will never be shamed again."
        },
        "27": {
            "L": "You shall know that I am in the midst of Israel, and that I am the LORD your God and there is none else; and my people shall never be put to shame.",
            "M": "You shall know that I am in the midst of Israel, and that I am the LORD your God and there is none else. And my people shall never again be put to shame.",
            "T": "And you will know —\nthat I am here, in the midst of Israel,\nthat I am Yahweh your God and there is no other.\nMy people will never be shamed again."
        },
        "28": {
            "L": "And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy, your old men shall dream dreams, your young men shall see visions.",
            "M": "And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy, your old men shall dream dreams, and your young men shall see visions.",
            "T": "And after all that —\nI will pour out my Spirit on all flesh.\nYour sons and daughters will prophesy;\nyour old men will dream dreams;\nyour young men will see visions."
        },
        "29": {
            "L": "Even on the male servants and female servants in those days I will pour out my Spirit.",
            "M": "Even on the male and female servants in those days I will pour out my Spirit.",
            "T": "Even on the servants — men and women alike —\nI will pour out my Spirit in those days."
        },
        "30": {
            "L": "And I will show wonders in the heavens and on the earth: blood and fire and columns of smoke.",
            "M": "And I will show wonders in the heavens and on the earth: blood and fire and columns of smoke.",
            "T": "I will set signs and wonders\nin the sky and on the earth:\nblood, and fire, and towering pillars of smoke."
        },
        "31": {
            "L": "The sun shall be turned to darkness, and the moon to blood, before the great and terrible day of the LORD comes.",
            "M": "The sun shall be turned to darkness, and the moon to blood, before the great and awesome day of the LORD comes.",
            "T": "The sun will be turned to darkness\nand the moon to blood —\nbefore the great and terrible Day of the LORD arrives."
        },
        "32": {
            "L": "And it shall come to pass that everyone who calls on the name of the LORD shall be delivered; for in Mount Zion and in Jerusalem there shall be those who escape, as the LORD has said, and among the survivors shall be those whom the LORD calls.",
            "M": "And it shall come to pass that everyone who calls on the name of the LORD shall be saved. For in Mount Zion and in Jerusalem there shall be those who escape, as the LORD has said; and among the survivors shall be those whom the LORD calls.",
            "T": "And this is the promise:\nevery person who calls on the name of Yahweh will be delivered.\nIn Mount Zion and in Jerusalem there will be a company who escape —\njust as Yahweh has said —\nand among those survivors will be the ones Yahweh himself has called."
        }
    },
    "3": {
        "1": {
            "L": "For behold, in those days and at that time, when I restore the fortunes of Judah and Jerusalem,",
            "M": "For behold, in those days and at that time, when I restore the fortunes of Judah and Jerusalem,",
            "T": "For mark this well: in those days — at that appointed time —\nwhen I reverse the exile of Judah and Jerusalem,"
        },
        "2": {
            "L": "I will gather all nations and bring them down to the Valley of Jehoshaphat; and I will enter into judgment with them there, on behalf of my people and my heritage Israel, because they have scattered them among the nations and have divided up my land.",
            "M": "I will gather all the nations and bring them down to the Valley of Jehoshaphat; and I will enter into judgment with them there, on account of my people and my heritage Israel, because they have scattered them among the nations and have divided up my land.",
            "T": "I will assemble every nation\nand bring them down to the Valley of Jehoshaphat —\nthe valley where Yahweh judges.\nThere I will put them on trial\non behalf of my people, my heritage Israel,\nbecause they scattered them through the nations\nand partitioned my land among themselves."
        },
        "3": {
            "L": "And for my people they have cast lots, and have given a boy for a harlot, and sold a girl for wine, and have drunk.",
            "M": "And for my people they have cast lots; they have traded a boy for a prostitute, and sold a girl for wine and drunk it.",
            "T": "They gambled over my people like plunder,\ntrading a boy for the price of a prostitute\nand selling a girl for a drink of wine."
        },
        "4": {
            "L": "And also, what are you to me, O Tyre and Sidon, and all the coasts of Philistia? Will you repay me? Or will you make restitution to me? Speedily, swiftly I will return your payment on your own head.",
            "M": "But you — what are you to me, O Tyre and Sidon, and all the regions of Philistia? Are you paying me back for something? If you are repaying me, I will return your payment on your own head swiftly and speedily.",
            "T": "And as for you — Tyre, Sidon,\nand all the districts of Philistia —\nwhat do you think you are doing to me?\nAre you trying to settle a score?\nIf so, I will repay you\nswiftly and directly — blow for blow."
        },
        "5": {
            "L": "For you have taken my silver and my gold, and have carried my rich treasures into your temples.",
            "M": "For you have taken my silver and my gold, and have carried my rich treasures into your temples.",
            "T": "You took my silver and my gold;\nmy finest treasures you hauled off into your temples."
        },
        "6": {
            "L": "You have sold the children of Judah and Jerusalem to the Greeks, that you might remove them far from their border.",
            "M": "You have sold the people of Judah and Jerusalem to the Greeks, removing them far from their own borders.",
            "T": "You sold the people of Judah and Jerusalem to the Greeks —\nshipping them as far from their homeland as possible."
        },
        "7": {
            "L": "Behold, I will stir them up from the place where you have sold them, and will return your payment on your own head.",
            "M": "Behold, I will rouse them from the place to which you sold them, and I will return your payment on your own head.",
            "T": "But I will rouse them from the very place you sold them to,\nand I will turn everything you did back on your own heads."
        },
        "8": {
            "L": "I will sell your sons and your daughters into the hand of the children of Judah, and they shall sell them to the Sabeans, to a nation far off; for the LORD has spoken.",
            "M": "I will sell your sons and your daughters into the hands of the people of Judah, and they will sell them to the Sabeans, to a distant nation — for the LORD has spoken.",
            "T": "I will sell your own sons and daughters\ninto the hands of the people of Judah,\nand they will trade them to the Sabeans — a nation far away.\nYahweh has spoken this."
        },
        "9": {
            "L": "Proclaim this among the nations: Prepare for war; rouse the mighty men; let all the men of war draw near, let them come up.",
            "M": "Proclaim this among the nations: Prepare for war! Rouse the mighty men! Let all the warriors draw near — let them come up!",
            "T": "Announce this to every nation:\nPrepare for war — mobilise!\nArouse all your fighting men;\nlet every soldier advance and come up!"
        },
        "10": {
            "L": "Beat your plowshares into swords, and your pruning hooks into spears; let the weak say, 'I am a warrior.'",
            "M": "Beat your plowshares into swords and your pruning hooks into spears; let the weak say, 'I am a warrior.'",
            "T": "Beat your plowshares into swords,\nyour pruning hooks into spears.\nLet even the weakest one boast: 'I am a soldier.'\n(Joel here deliberately reverses the vision of Isaiah 2:4 and Micah 4:3:\nnot peace into war, but the opposite — summoning the nations to their doom.)"
        },
        "11": {
            "L": "Hasten and come, all you surrounding nations, and gather yourselves together. Bring down your warriors, O LORD.",
            "M": "Hasten and come, all you surrounding nations, and gather yourselves there. Bring down your warriors, O LORD.",
            "T": "Come quickly, all you surrounding nations —\ngather yourselves there.\nAnd you, Yahweh — bring down your warriors."
        },
        "12": {
            "L": "Let the nations be roused and come up to the Valley of Jehoshaphat; for there I will sit to judge all the surrounding nations.",
            "M": "Let the nations be roused and come up to the Valley of Jehoshaphat; for there I will sit to judge all the surrounding nations.",
            "T": "Let the nations stir themselves and come up\nto the Valley of Jehoshaphat —\nfor there I will take my seat\nto judge every nation on every side."
        },
        "13": {
            "L": "Put in the sickle, for the harvest is ripe. Go in, tread, for the winepress is full; the vats overflow, for their wickedness is great.",
            "M": "Put in the sickle, for the harvest is ripe. Go in and tread, for the winepress is full; the vats overflow, for their wickedness is great.",
            "T": "Swing the sickle — the harvest is ready.\nStamp down the winepress — it is full to the brim.\nThe vats are running over.\nTheir wickedness is that great."
        },
        "14": {
            "L": "Multitudes, multitudes, in the valley of decision! For the day of the LORD is near in the valley of decision.",
            "M": "Multitudes, multitudes in the valley of decision! For the day of the LORD is near in the valley of decision.",
            "T": "Multitudes — multitudes —\nin the Valley of Decision, where the verdict will fall!\nFor the Day of the LORD is at the threshold,\nright there in the Valley of Decision."
        },
        "15": {
            "L": "The sun and the moon shall be darkened, and the stars shall withdraw their shining.",
            "M": "The sun and the moon grow dark, and the stars withdraw their shining.",
            "T": "Sun and moon go dark;\nthe stars pull back their light."
        },
        "16": {
            "L": "The LORD also shall roar out of Zion, and utter his voice from Jerusalem; and the heavens and the earth shall shake; but the LORD will be a refuge for his people, and a stronghold for the children of Israel.",
            "M": "The LORD roars from Zion and utters his voice from Jerusalem; the heavens and the earth shake. But the LORD is a refuge for his people, a stronghold for the children of Israel.",
            "T": "Yahweh roars from Zion;\nhe thunders from Jerusalem.\nHeaven and earth shake —\nbut Yahweh is a shelter for his people,\na fortress for the children of Israel."
        },
        "17": {
            "L": "So you shall know that I am the LORD your God, who dwells in Zion, my holy mountain; and Jerusalem shall be holy, and strangers shall no longer pass through it.",
            "M": "So you shall know that I am the LORD your God, who dwells in Zion, my holy mountain. And Jerusalem shall be holy, and strangers shall never again pass through it.",
            "T": "Then you will know —\nI am Yahweh your God,\ndwelling in Zion, my holy mountain.\nJerusalem will be set apart as holy,\nand no foreign army will march through it again."
        },
        "18": {
            "L": "And it shall come to pass in that day that the mountains shall drip sweet wine, and the hills shall flow with milk, and all the riverbeds of Judah shall flow with water; and a fountain shall come forth from the house of the LORD and water the Valley of Shittim.",
            "M": "And in that day the mountains shall drip with sweet wine, and the hills shall flow with milk, and all the streambeds of Judah shall flow with water; and a spring shall come forth from the house of the LORD and water the Valley of Shittim.",
            "T": "On that day the mountains will drip with new wine;\nthe hills will flow with milk;\nall the dry streambeds of Judah will run with water.\nA spring will flow from the house of Yahweh\nand water the Valley of Shittim.\n(This fountain from God's house points forward to Ezek 47 and Rev 22.)"
        },
        "19": {
            "L": "Egypt shall become a desolation, and Edom a desolate wilderness, for the violence done to the people of Judah, because they have shed innocent blood in their land.",
            "M": "Egypt shall become a desolation and Edom a desolate wilderness, because of the violence done to the people of Judah, in whose land they shed innocent blood.",
            "T": "But Egypt will become a wasteland\nand Edom a barren desert —\nbecause of what they did to Judah:\nthe violence, the innocent blood\nthey spilled in the land."
        },
        "20": {
            "L": "But Judah shall be inhabited forever, and Jerusalem to all generations.",
            "M": "But Judah shall be inhabited forever, and Jerusalem to all generations.",
            "T": "Judah, however, will be inhabited forever;\nJerusalem, to every generation."
        },
        "21": {
            "L": "And I will avenge their blood, the blood I have not yet avenged; for the LORD dwells in Zion.",
            "M": "I will avenge their blood — the blood I have not yet avenged — for the LORD dwells in Zion.",
            "T": "I will avenge their blood —\nevery drop I have not yet called to account —\nfor Yahweh makes his home in Zion."
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'joel')
        merge_tier(existing, JOEL, tier_key)
        save(tier_dir, 'joel', existing)
    print('Joel 1–3 written.')

if __name__ == '__main__':
    main()
