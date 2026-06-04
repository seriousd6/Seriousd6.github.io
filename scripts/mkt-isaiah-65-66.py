"""
MKT Isaiah chapters 65–66 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-65-66.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
  The divine personal name is consistently surfaced in T.
- H430 (אֱלֹהִים): "God" in all tiers throughout.
- H1254 (בָּרָא): "create" in all tiers (65:17,18; 66:22). The same root used in Gen 1:1;
  in Isaiah 65 it marks a cosmological new-creation act, not just renovation. Distinct from
  H6213 (עָשָׂה, "make") which appears in 66:22. Both preserved in that verse.
- H543 (אָמֵן): "God of truth" in L (most literal), "God of faithfulness" in M/T (65:16).
  The unique divine title אֱלֹהֵי אָמֵן ("God of Amen") conveys both absolute reliability and
  the "amen" that confirms oaths. "Faithfulness" surfaces the covenantal dimension in M and T.
- H7965 (שָׁלוֹם): "peace" in all tiers (66:12 — extended like a river). The full Hebrew
  shalom (well-being, wholeness, prosperity) is foregrounded in T's extended river image.
- H7307 (רוּחַ): 66:2 — "spirit" (lower case). This is the human contrite spirit, not the
  divine Spirit. Consistent with 57:15 where the same distinction was maintained.
- H5315 (נֶפֶשׁ): 66:3 — "their soul delights in their abominations." L renders "soul" to
  capture the whole-self sense; M/T rephrase as "their whole being" or "they delight."
- H6635 (צְבָאוֹת): does not appear in these chapters.
- H1409/H4507 (גַּד/מְנִי, Gad/Meni): 65:11 — "Fortune" and "Destiny." These are Canaanite
  deity names; retain them in L/M. T uses "Fortune and Fate" to preserve the idol-naming
  without obscuring the deliberate theological contrast with Yahweh who names and controls destiny.
- H5764/H5288 (עוּל/נַעַר): 65:20 — the new creation extends life so radically that death at
  100 is death "as a youth." The sinner who dies at 100 is "accursed" (qalal, H7043) — cut off
  early in the age of greatly extended life. T preserves this sharpness.
- H6412 (פָּלִיט): 66:19 — "survivors/those who escape." In context these are survivors from
  among the nations gathered for judgment who become missionary heralds to the far nations.
  Named destinations: Tarshish (southern Spain/far west), Pul (N. Africa), Lud (Lydia/Asia Minor),
  Tubal (Black Sea region), Javan (Greece/Ionia — H3120). T uses "Greece" for Javan to clarify.
- 66:21 — Foreigners appointed as priests and Levites. This is theologically explosive:
  the Mosaic restriction of the Levitical priesthood is reversed in the eschatological age.
  L/M preserve the flat declarative; T draws out the weight of the reversal.
- 66:24 — "Their worm shall not die, their fire shall not be quenched." Jesus quotes this in
  Mark 9:44,46,48 for Gehenna. The verse is not softened; it is the final, terrible counterpoint
  to the vision of eternal worship in v.23. T preserves the horror with no cushioning.
- Aspect notes:
  65:1-2 — Niphal passive perfect (נִדְרַשְׁתִּי, נִמְצֵאתִי): "I let myself be sought/found."
  The passive captures God's availability; T surfaces this as divine initiative.
  65:17-25 — Prophetic future; the series of futures is confident divine announcement.
  66:7-9 — The birth-before-labor sequence uses perfects to stress the sudden accomplished fact.
  66:15-16 — The judgment section uses participial/imperfect forms; L preserves the imminent
  present force; T uses "is coming" and "will come."
- OT echoes:
  65:1-2 — Quoted by Paul in Romans 10:20-21; applied to Gentiles. Isaiah's context concerns
  Israel, but the universalising resonance is already latent in the text. T does not add NT gloss.
  65:17,25 — Echoes Isa 11:6-9 (the peaceable kingdom) and the creation of Gen 1. The "new
  heavens and new earth" formula is taken up in 2 Pet 3:13 and Rev 21:1.
  66:1 — Quoted by Stephen in Acts 7:49-50; echoes 1 Kgs 8:27 (Solomon's Temple dedication).
  66:12 — "Peace like a river" echoes the Servant Song of 48:18.
  66:13 — The maternal comfort image (mother comforting child) parallels 49:15.
  66:18-21 — The missionary vision of survivors sent to distant nations prefigures the NT
  mission (Acts 1:8). T does not collapse to NT but preserves the full scope.
  66:22-24 — The closing vision of permanent new creation / eternal worship / undying judgment
  forms an inclusio with the opening cosmic creation of Gen 1 and the judgment of the entire
  prophetic tradition. The book ends on both extremes: eternal worship and eternal contempt.
- Structural notes:
  Ch. 65 — God's answer to the lament of 63:7–64:12, distinguishing his servants from rebels
  (vv. 1-16) before pivoting to the new creation promise (vv. 17-25). The chapter articulates
  the clearest vision of the new creation in the Hebrew Bible, including the elimination of
  premature death, social harmony, and the peaceable kingdom (the wolf and lamb of 11:6 reappear).
  Ch. 66 — The great conclusion of Isaiah. The true temple is the contrite heart (vv. 1-4);
  the sudden birth of Zion (vv. 7-14); judgment by fire on idolaters (vv. 15-17); the universal
  gathering and mission to the nations with the appointment of foreign priests (vv. 18-21);
  the permanent new creation with perpetual worship (vv. 22-23); the final sight of judgment
  that never ends (v.24). Isaiah closes on an intentionally unsettling note — the eternal vision
  of divine glory interrupted by the sight of undying judgment.
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

ISAIAH = {
  "65": {
    "1": {
      "L": "I was sought by those who did not ask; I was found by those who did not seek me; I said, 'Here am I, here am I,' to a nation that was not called by my name.",
      "M": "I let myself be sought by those who did not ask for me; I let myself be found by those who did not seek me; I said, 'Here am I, here am I,' to a nation that had not called on my name.",
      "T": "I was there to be sought by those who never asked for me.\nI was found by those who never looked.\nTo a nation that had not called on my name, I said:\nHere I am. Here I am."
    },
    "2": {
      "L": "I have spread out my hands all day long to a rebellious people, who walk in a way that is not good, following their own thoughts.",
      "M": "All day long I spread out my hands to a rebellious people who walk in ways that are not good, following their own schemes.",
      "T": "All day long I held out my hands to a people who would not come — walking a road that leads nowhere, following plans of their own making."
    },
    "3": {
      "L": "A people who provoke me to my face continually, who sacrifice in gardens and burn incense on altars of brick.",
      "M": "A people who continually provoke me to my face, who sacrifice in gardens and burn incense on brick altars.",
      "T": "A people who provoke me — continually, right to my face — sacrificing in garden shrines, burning incense on unauthorized brick altars."
    },
    "4": {
      "L": "Who sit among the graves and spend the night in secret places; who eat the flesh of swine, and their vessels hold the broth of abominable things.",
      "M": "Who sit among the graves and spend the night in hidden places; who eat pork, with bowls of contaminated broth.",
      "T": "They haunt the tombs, spending nights in hidden places. They eat pork. Their bowls hold a stew of unclean things."
    },
    "5": {
      "L": "Who say, 'Keep away, do not come near me, for I am holier than you.' These are smoke in my nostrils, a fire that burns all day long.",
      "M": "Who say, 'Stay away — do not come near me, for I am holier than you!' These are smoke in my nostrils, a fire that burns all day.",
      "T": "Who say: Stay back — don't touch me, I am too holy for you.\nThese people are smoke in my nostrils —\na fire that burns without stopping."
    },
    "6": {
      "L": "Behold, it is written before me; I will not keep silent, but I will repay; I will repay into their bosom.",
      "M": "See, it stands written before me: I will not be silent — I will repay; I will pay it fully into their laps.",
      "T": "It is written before me. I will not be silent.\nI will repay — I will pay it right into their laps."
    },
    "7": {
      "L": "Your iniquities and your fathers' iniquities together, says the LORD; because they burned incense on the mountains and defied me on the hills, I will measure their former deeds into their bosom.",
      "M": "Your iniquities and your fathers' iniquities together — the LORD declares — because they burned incense on the mountains and defied me on the hills, I will measure out the wages of their former deeds into their laps.",
      "T": "Your iniquities and your fathers' iniquities together — Yahweh declares —\nbecause they burned incense on the mountains\nand defied me on the hills,\nI will measure out full payment for their former deeds —\nright into their laps."
    },
    "8": {
      "L": "Thus says the LORD: As the new wine is found in a cluster, and one says, 'Do not destroy it, for a blessing is in it,' so I will do for my servants' sake, and not destroy them all.",
      "M": "Thus says the LORD: As new wine is found in a cluster of grapes and someone says, 'Do not destroy it, for a blessing is in it,' so I will act for my servants' sake and not destroy them all.",
      "T": "Yahweh says this: As new wine is found in a cluster — and someone says, don't destroy it, there is a blessing in it — so I will act for my servants' sake. I will not destroy them all."
    },
    "9": {
      "L": "And I will bring forth from Jacob a seed, and from Judah an inheritor of my mountains; my chosen shall inherit it, and my servants shall dwell there.",
      "M": "I will bring forth from Jacob a people, and from Judah an inheritor of my mountains; my chosen ones shall possess it, and my servants shall live there.",
      "T": "I will raise up from Jacob a people, and from Judah an heir for my mountains. My chosen will possess it. My servants will live there."
    },
    "10": {
      "L": "And Sharon shall be a pasture for flocks, and the Valley of Achor a resting place for herds, for my people who have sought me.",
      "M": "Sharon shall become a meadow for flocks, and the Valley of Achor a resting place for cattle, for my people who have sought me.",
      "T": "Sharon will be a meadow for flocks. The Valley of Achor — once the valley of trouble — will be a resting place for cattle. All for my people who have sought me."
    },
    "11": {
      "L": "But you who forsake the LORD, who forget my holy mountain, who set a table for Fortune and fill a cup of mixed wine for Destiny —",
      "M": "But you who forsake the LORD and forget my holy mountain, who set a table for Fortune and fill cups of mixed wine for Fate —",
      "T": "But you who abandon Yahweh, who forget my holy mountain —\nyou set a table for Fortune;\nyou pour out cups of wine for Fate —"
    },
    "12": {
      "L": "I will destine you to the sword, and you shall all bow down to the slaughter, because when I called you did not answer; when I spoke you did not hear; but you did evil in my eyes and chose that in which I did not delight.",
      "M": "I will destine you to the sword, and you will all bow down for slaughter, because when I called you did not answer; when I spoke you did not listen; but you did what was evil in my eyes and chose what I did not delight in.",
      "T": "I will condemn you to the sword — you will all go down for slaughter — because when I called, you did not answer. When I spoke, you did not listen. You chose evil in my sight. You chose what gives me no delight."
    },
    "13": {
      "L": "Therefore thus says the Lord GOD: Behold, my servants shall eat, but you shall be hungry; behold, my servants shall drink, but you shall be thirsty; behold, my servants shall rejoice, but you shall be ashamed.",
      "M": "Therefore the Lord GOD declares: My servants shall eat, but you will go hungry; my servants shall drink, but you will be thirsty; my servants shall rejoice, but you will be put to shame.",
      "T": "Therefore the Lord Yahweh says this:\nMy servants will eat — you will go hungry.\nMy servants will drink — you will be thirsty.\nMy servants will rejoice — you will be put to shame."
    },
    "14": {
      "L": "Behold, my servants shall sing for gladness of heart, but you shall cry out for pain of heart, and shall wail for breaking of spirit.",
      "M": "My servants shall shout for joy of heart, but you shall cry out in pain of heart and wail in anguish of spirit.",
      "T": "My servants will sing out of hearts full to overflowing.\nYou will cry out in heartache.\nYou will wail in the breaking of your spirit."
    },
    "15": {
      "L": "And you shall leave your name as a curse to my chosen; and the Lord GOD will put you to death, but to his servants he will call by a different name.",
      "M": "You will leave your name behind as a curse for my chosen ones; and the Lord GOD will put you to death, while his servants he will call by a different name.",
      "T": "Your name will become a curse-word left behind for my chosen — the Lord Yahweh will put you to death — but his servants he will call by a new name."
    },
    "16": {
      "L": "So that he who blesses himself in the land shall bless himself by the God of truth, and he who takes an oath in the land shall swear by the God of truth; because the former troubles are forgotten and are hidden from my eyes.",
      "M": "So that whoever blesses himself in the land will bless himself by the God of faithfulness, and whoever takes an oath in the land will swear by the God of faithfulness; because the former troubles are forgotten and hidden from my eyes.",
      "T": "Whoever blesses himself in the land will do so by the God of faithfulness.\nWhoever swears an oath in the land will do so by the God of faithfulness.\nFor the former troubles have been forgotten —\nhidden from my eyes."
    },
    "17": {
      "L": "For behold, I create new heavens and a new earth, and the former things shall not be remembered, nor shall they come into mind.",
      "M": "For see, I am creating new heavens and a new earth; the former things will not be remembered or come to mind.",
      "T": "For look — I am creating new heavens and a new earth.\nThe former things will not be remembered.\nThey will not rise to mind."
    },
    "18": {
      "L": "But be glad and rejoice forever in that which I create; for behold, I create Jerusalem to be a joy, and her people a rejoicing.",
      "M": "But be glad and rejoice forever in what I am creating; for see, I am creating Jerusalem to be a joy, and her people a delight.",
      "T": "Be glad — rejoice forever — in what I am creating.\nI am making Jerusalem pure joy,\nher people the source of delight."
    },
    "19": {
      "L": "I will rejoice in Jerusalem and be glad in my people; no more shall be heard in it the sound of weeping and the voice of crying.",
      "M": "I will rejoice in Jerusalem and be glad in my people; no more shall the sound of weeping or the voice of distress be heard in it.",
      "T": "I will take joy in Jerusalem and delight in my people.\nThe sound of weeping will no longer be heard there —\nno voice of distress."
    },
    "20": {
      "L": "No more shall there be in it an infant of days, or an old man who has not filled out his days; for the young man shall die at a hundred years, and the sinner a hundred years old shall be accursed.",
      "M": "Never again will there be in it an infant who lives only a few days, or an old man who does not complete his years; for the one who dies at a hundred will be thought young, and the sinner who falls short of a hundred will be considered cursed.",
      "T": "No infant will die within days.\nNo old man will fail to complete his years.\nIn this new age, the one who dies at a hundred will be counted a youth —\nthe sinner cut off at a hundred will be accursed, dying far too soon."
    },
    "21": {
      "L": "And they shall build houses and inhabit them; and they shall plant vineyards and eat their fruit.",
      "M": "They shall build houses and live in them; they shall plant vineyards and eat their fruit.",
      "T": "They will build houses and live in them. They will plant vineyards and eat their fruit."
    },
    "22": {
      "L": "They shall not build and another inhabit; they shall not plant and another eat; for as the days of a tree are the days of my people, and my chosen shall long enjoy the work of their hands.",
      "M": "They will not build only for others to inhabit; they will not plant only for others to eat; for like the days of a tree shall be the days of my people, and my chosen ones shall long enjoy the work of their hands.",
      "T": "They will not build for someone else to live in.\nThey will not plant for someone else to eat.\nMy people will have days like the days of a tree — long and full.\nMy chosen will enjoy the full fruit of their work."
    },
    "23": {
      "L": "They shall not labor in vain nor bring forth for sudden terror; for they are the offspring of the blessed of the LORD, and their descendants with them.",
      "M": "They shall not toil for nothing or give birth to children who meet disaster; for they are the offspring of those whom the LORD has blessed, and their descendants with them.",
      "T": "They will not labor for nothing.\nThey will not give birth only to see their children destroyed.\nThey are the offspring of Yahweh's blessed —\nand their descendants with them."
    },
    "24": {
      "L": "And it shall be, before they call I will answer; and while they are still speaking, I will hear.",
      "M": "Before they call, I will answer; while they are still speaking, I will listen.",
      "T": "Before they call, I will answer.\nWhile they are still speaking, I will hear."
    },
    "25": {
      "L": "The wolf and the lamb shall graze together, and the lion shall eat straw like the ox, and dust shall be the serpent's food. They shall not hurt nor destroy in all my holy mountain, says the LORD.",
      "M": "The wolf and the lamb will graze together, and the lion will eat straw like the ox; dust will be the serpent's food. They shall not hurt or destroy on all my holy mountain, says the LORD.",
      "T": "The wolf and the lamb will graze side by side.\nThe lion will eat straw like the ox.\nDust will be the serpent's food.\nNothing will hurt or destroy\non all my holy mountain —\nYahweh says it."
    }
  },
  "66": {
    "1": {
      "L": "Thus says the LORD: Heaven is my throne, and earth is my footstool; where is the house that you would build for me, and where is the place of my rest?",
      "M": "Thus says the LORD: Heaven is my throne and the earth is my footstool; where is the house you would build for me, and where is my resting place?",
      "T": "Yahweh says this: Heaven is my throne. Earth is my footstool. What house could you build for me? What place would serve as my rest?"
    },
    "2": {
      "L": "All these things my hand has made, and all these things came to be, declares the LORD. But to this one I will look: to him who is humble and contrite in spirit and who trembles at my word.",
      "M": "All these things my hand has made, and all these things exist, declares the LORD. But this is the one I will regard: the humble and contrite in spirit, who trembles at my word.",
      "T": "My hand made all these things — all these things came to be — Yahweh declares. But this is the one I look to: the one who is poor in spirit, contrite, trembling at my word."
    },
    "3": {
      "L": "He who slaughters an ox is as one who slays a man; he who sacrifices a lamb is as one who breaks a dog's neck; he who brings a grain offering is as one who offers pig's blood; he who burns frankincense as a memorial is as one who blesses an idol. These have chosen their own ways, and their soul delights in their abominations.",
      "M": "Whoever slaughters an ox is like one who kills a man; whoever sacrifices a lamb is like one who breaks a dog's neck; whoever brings a grain offering is like one who offers pig's blood; whoever burns frankincense as a memorial is like one who worships an idol. These people have chosen their own ways, and they delight in their abominations.",
      "T": "To slaughter an ox — as if killing a man.\nTo sacrifice a lamb — as if breaking a dog's neck.\nTo bring a grain offering — as if offering pig's blood.\nTo burn frankincense — as if blessing an idol.\nThese people chose their own ways.\nTheir whole being delights in their abominations."
    },
    "4": {
      "L": "I also will choose their delusions and bring their fears upon them, because when I called no one answered; when I spoke they did not hear; but they did evil in my eyes and chose that in which I did not delight.",
      "M": "I in turn will choose what they dread and bring their fears upon them, because when I called no one answered; when I spoke they did not listen; they did what was evil in my eyes and chose what I did not delight in.",
      "T": "So I will choose what they fear most and bring it on them — because when I called, no one answered. When I spoke, no one listened. They chose evil in my sight. They chose what gives me no delight."
    },
    "5": {
      "L": "Hear the word of the LORD, you who tremble at his word: Your brethren who hate you and cast you out for my name's sake have said, 'Let the LORD be glorified, that we may see your joy'; but it is they who shall be put to shame.",
      "M": "Hear the word of the LORD, you who tremble at his word: Your brothers who hate you and reject you for my name's sake have said, 'Let the LORD be glorified so we can see your joy!' But it is they who will be put to shame.",
      "T": "You who tremble at his word — hear the word of Yahweh:\nYour own brothers who hate you and drive you out because of my name\nhave said — Let Yahweh be glorified, so we can see your joy!\nBut it is they who will end up in shame."
    },
    "6": {
      "L": "A sound of uproar from the city! A voice from the temple! The voice of the LORD rendering recompense to his enemies!",
      "M": "Listen — an uproar from the city, a voice from the temple, the voice of the LORD repaying his enemies what they deserve!",
      "T": "A roar from the city!\nA voice from the temple!\nThe voice of Yahweh — repaying his enemies in full."
    },
    "7": {
      "L": "Before she was in labor she gave birth; before her pain came upon her she delivered a son.",
      "M": "Before she went into labor she gave birth; before her pain came on her, she delivered a son.",
      "T": "Before she was in labor, she gave birth. Before her pains came, she delivered a son."
    },
    "8": {
      "L": "Who has heard such a thing? Who has seen such things? Shall a land be brought forth in one day? Shall a nation be born at one time? For as soon as Zion was in labor she brought forth her children.",
      "M": "Who has heard of such a thing? Who has seen things like these? Can a land be delivered in a single day? Can a nation be born all at once? And yet — as soon as Zion went into labor, she gave birth to her children.",
      "T": "Who has ever heard of such a thing?\nWho has seen anything like this?\nCan a land be delivered in a single day?\nCan a nation be born all at once?\nAnd yet — the moment Zion went into labor, she gave birth to her children."
    },
    "9": {
      "L": "'Shall I bring to the point of birth and not cause to bring forth?' says the LORD; 'Shall I, who cause to bring forth, shut the womb?' says your God.",
      "M": "'Would I bring to the point of birth and not cause delivery?' says the LORD; 'Would I, who give birth, then close the womb?' says your God.",
      "T": "Would I bring a child to the brink of birth and then not deliver? Yahweh asks. Would I — who open the womb — then shut it? your God asks."
    },
    "10": {
      "L": "Rejoice with Jerusalem, and be glad for her, all you who love her; rejoice with her in joy, all you who mourn over her.",
      "M": "Rejoice with Jerusalem and be glad for her, all you who love her; rejoice with her in her joy, all you who mourn over her.",
      "T": "Rejoice with Jerusalem!\nBe glad for her — all who love her!\nRejoice in her joy —\nall who mourn over her!"
    },
    "11": {
      "L": "That you may nurse and be satisfied from her comforting breast; that you may drink deeply and take delight from her glorious abundance.",
      "M": "So that you may nurse and be satisfied at her comforting breasts; so that you may drink deeply and delight in her abundant glory.",
      "T": "Nurse and be satisfied at her comforting breast.\nDrink deep — be filled with delight —\nfrom her overflowing glory."
    },
    "12": {
      "L": "For thus says the LORD: Behold, I will extend to her peace like a river, and the glory of the nations like an overflowing stream; and you shall nurse, you shall be carried on the hip, and bounced on the knees.",
      "M": "For thus says the LORD: I will extend prosperity to her like a river, and the wealth of nations like a flooding stream; and you will be nursed, carried on the hip and dandled on the knees.",
      "T": "For Yahweh says this:\nI am extending peace to her like a river —\nthe glory of the nations like a flooding stream.\nYou will nurse;\nyou will be carried on the hip\nand bounced on the knee."
    },
    "13": {
      "L": "As one whom his mother comforts, so I will comfort you; you shall be comforted in Jerusalem.",
      "M": "As a mother comforts her child, so I will comfort you; and you will be comforted in Jerusalem.",
      "T": "As a mother comforts her child — so I will comfort you. You will be comforted in Jerusalem."
    },
    "14": {
      "L": "And you shall see, and your heart shall rejoice; and your bones shall flourish like the grass; and the hand of the LORD shall be made known to his servants, and he shall show his indignation toward his enemies.",
      "M": "When you see this, your heart will rejoice and your bones will flourish like the grass; the hand of the LORD will be made known to his servants, but his fury will be shown toward his enemies.",
      "T": "You will see it — and your heart will overflow with joy.\nYour bones will flourish like tender grass.\nThe hand of Yahweh will be known by his servants —\nbut his fury will fall on his enemies."
    },
    "15": {
      "L": "For behold, the LORD will come in fire, and his chariots like the whirlwind, to render his anger in fury, and his rebuke with flames of fire.",
      "M": "For see, the LORD will come in fire, with his chariots like a whirlwind, to repay his anger in fury and his rebuke with flames of fire.",
      "T": "Look — Yahweh is coming in fire.\nHis chariots like a whirlwind.\nHe comes to repay in burning fury —\nhis rebuke in flames."
    },
    "16": {
      "L": "For by fire will the LORD enter into judgment, and by his sword, with all flesh; and those slain by the LORD shall be many.",
      "M": "For by fire and by his sword the LORD will execute judgment upon all flesh; and the slain of the LORD shall be many.",
      "T": "By fire and by sword Yahweh will execute judgment upon all flesh — and those he slays will be many."
    },
    "17": {
      "L": "Those who sanctify and purify themselves to go into the gardens, following one in their midst, eating swine's flesh and the abomination and mice — they shall come to an end together, declares the LORD.",
      "M": "Those who consecrate and purify themselves to enter the gardens, following the one who leads in their midst, eating pig's flesh and detestable things and mice — they shall perish together, declares the LORD.",
      "T": "Those who consecrate and purify themselves to enter the gardens — following the one in their midst — eating pork and the detestable thing and mice: they will all be swept away together. Yahweh declares it."
    },
    "18": {
      "L": "For I know their works and their thoughts, and the time is coming to gather all nations and tongues; and they shall come and see my glory.",
      "M": "For I know their works and their thoughts, and the time is coming to gather all nations and peoples of every language; they shall come and see my glory.",
      "T": "I know their works. I know their thoughts. The time is coming to gather all nations, all tongues — and they will come and see my glory."
    },
    "19": {
      "L": "And I will set a sign among them. And from them I will send survivors to the nations — to Tarshish, Pul, and Lud, who draw the bow, to Tubal and Javan, to the distant coastlands — those who have not heard my fame or seen my glory; and they shall declare my glory among the nations.",
      "M": "I will set a sign among them, and from them I will send survivors to the nations — to Tarshish, Pul, and Lud who draw the bow, to Tubal and Javan, to the distant coastlands — those who have not heard my fame or seen my glory; and they shall declare my glory among the nations.",
      "T": "I will set a sign among them. From the survivors I will send messengers to the nations — to Tarshish, to Pul and Lud who draw the bow, to Tubal and Greece, to the distant coastlands — to all who have never heard of me, who have never seen my glory. They will declare my glory among the nations."
    },
    "20": {
      "L": "And they shall bring all your brothers from all the nations as an offering to the LORD — on horses and in chariots and in litters and on mules and on dromedaries — to my holy mountain Jerusalem, says the LORD, just as the Israelites bring a grain offering in a clean vessel to the house of the LORD.",
      "M": "They shall bring all your brothers from all the nations as an offering to the LORD — riding on horses, in chariots and litters, on mules and on swift camels — to my holy mountain Jerusalem, says the LORD, just as the Israelites bring their grain offering in a clean vessel to the house of the LORD.",
      "T": "They will bring all your brothers from every nation as an offering to Yahweh — on horseback and by chariot and in litters and on mules and on swift camels — to my holy mountain Jerusalem. Yahweh says it. Just as Israel brings a grain offering in a clean vessel to Yahweh's house."
    },
    "21": {
      "L": "And some of them also I will take for priests and for Levites, says the LORD.",
      "M": "And from among them I will also take some as priests and Levites, says the LORD.",
      "T": "And from among them — from these nations — I will take some as priests and Levites. Yahweh says it. The gates of the priesthood are opening."
    },
    "22": {
      "L": "For as the new heavens and the new earth that I make shall remain before me, declares the LORD, so shall your offspring and your name remain.",
      "M": "For as the new heavens and the new earth that I am making shall endure before me, declares the LORD, so shall your offspring and your name endure.",
      "T": "As the new heavens and the new earth I am making will endure before me — Yahweh declares — so your offspring and your name will endure."
    },
    "23": {
      "L": "And from new moon to new moon, and from Sabbath to Sabbath, all flesh shall come to worship before me, says the LORD.",
      "M": "From one new moon to the next, and from one Sabbath to the next, all people shall come and worship before me, declares the LORD.",
      "T": "From new moon to new moon —\nSabbath to Sabbath —\nall humanity will come to worship before me.\nYahweh declares it."
    },
    "24": {
      "L": "And they shall go out and look on the corpses of the men who have transgressed against me; for their worm shall not die, and their fire shall not be quenched, and they shall be an abhorrence to all flesh.",
      "M": "And they shall go out and look at the corpses of those who rebelled against me, for their worm shall not die, and their fire shall not be quenched, and they shall be an abhorrence to all flesh.",
      "T": "They will go out and see the corpses of those who rebelled against me.\nTheir worm will not die.\nTheir fire will not be quenched.\nThey will be a horror to all who see."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 65–66 written.')

if __name__ == '__main__':
    main()
