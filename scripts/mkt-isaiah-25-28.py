"""
MKT Isaiah chapters 25–28 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-25-28.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from chs 1–21.
- H136 (אֲדֹנָי): "Lord" in all tiers; 28:16 "Lord GOD" = אֲדֹנָי יְהוָה.
- H6635 (צְבָאוֹת): "of hosts" across all tiers — consistent with prior Isaiah scripts.
- H7307 (רוּחַ) in 28:6: "spirit" (lowercase) — a judicial spirit granted by Yahweh to judges,
  not the divine Spirit per se; in 27:8 "wind" — the sirocco east wind of judgment.
- H7965 (שָׁלוֹם) doubled in 26:3: "peace, peace" (L) / "perfect peace" (M/T) — the
  Hebrew intensive reduplication; traditional rendering "perfect peace" is apt.
- H6697 (צוּר) in 26:4: "Rock" — the divine-epithet rendering consistent throughout OT scripts.
- H3050/H3068 double name in 26:4: "Yah, the LORD" (L) / "the LORD — Yah himself" (M/T) —
  an emphatic double divine name; KJV renders "LORD JEHOVAH."
- H5315 (נֶפֶשׁ) in 26:8-9: "soul" (L) / "deepest self/being" (M) / "whole being" (T) —
  Hebrew embodied self, not Greek immaterial soul; context is intense yearning.
- H3882 (לִוְיָתָן) in 27:1: "Leviathan" — the ancient sea-chaos dragon of Ugaritic myth
  (Lotan); here = any imperial power arrayed against Yahweh's order. Name kept in all tiers;
  T notes its mythological resonance through phrasing rather than parenthetical.
- H1285 (בְּרִית) in 28:15/18: "covenant" across all tiers — the death-pact is described in
  covenant language; the irony that Judah makes a "covenant" with Death (H4194) rather than
  with Yahweh is theologically pointed.
- H7585 (שְׁאוֹל) in 28:15/18: "Sheol" (L) / "Sheol" (M) / "the realm of the dead" (T).
- H6673 (צַו) "precept/tsav" in 28:10/13: possibly baby-babble or mocking echo of prophetic
  speech. L/M preserve the repetition. T conveys its contemptuous quality.
- 28:16 cornerstone: H68 (אֶבֶן בֹּחַן) = "a tested stone" — cited in Rom 9:33 and 1 Pet 2:6
  as messianic. "He that believeth shall not make haste" = "shall not flee in panic." T
  renders "will never be shaken" to surface the trust/security theme; L/M "not make haste."
- 28:21 "strange work": Yahweh's judgment against his own people is called "strange/alien"
  (H2114 and H5237) because his preference is mercy, not destruction. T surfaces this.
- 26:19 resurrection: One of the two clearest OT resurrection promises (cf. Dan 12:2). T
  renders it with maximum vividness; "dew of a new morning" follows the image closely.
- 25:8 "swallow up death forever": Paul quotes this in 1 Cor 15:54 as fulfilled in Christ's
  resurrection. T honours both the original eschatological promise and its NT trajectory.
- Chapter 25:6-9 eschatological feast: All nations invited to Zion; death abolished; tears
  wiped. This is the apex of Isaiah 24–27 ("the Isaiah Apocalypse"). T uses expansive cadence.
- Chapter 27:2-6 second vineyard song: Consciously echoes and reverses the doom-song of Isa
  5:1-7. There the vineyard was ruined; here Yahweh himself tends it with care. T should
  carry the contrast.
- 28:24-29 agricultural parable: Yahweh's wisdom in discipline is like a skilled farmer — he
  knows when to plow, when to plant, when to thresh gently and when to roll the wheel. The
  parable answers implicitly: God's strange work (v21) has a purpose, like threshing has a
  purpose; it does not go on forever. T should close this connection.
- Aspect: Ch 25 — mix of past thanksgiving and prophetic future certainties; treat futures as
  vivid, assured. Ch 26 — the song moves from present trust (vv1-12) to lament (vv13-18) to
  hope (vv19-21). Ch 27 — eschatological futures. Ch 28 — woe oracle (present/future); the
  parable (vv24-29) in rhetorical questions that expect "no" answers.
- Poetry structure: Chs 25-27 are largely prophetic poetry; T uses line breaks throughout.
  Ch 28 is also mostly poetry except the parable; T maintains poetic cadence.
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
  "25": {
    "1": {
      "L": "O LORD, thou art my God; I will exalt thee, I will praise thy name; for thou hast done wonderful things — counsels from afar, faithfulness and truth.",
      "M": "LORD, you are my God; I will exalt you; I will praise your name, for you have done wonderful things — plans formed long ago, faithful and true.",
      "T": "O Yahweh, you are my God —\nI lift you high, I praise your name,\nfor you have done wonders:\nyour ancient purposes fulfilled, every one of them faithful and sure."
    },
    "2": {
      "L": "For thou hast made of a city a heap, of a fortified city a ruin; the palace of foreigners is a city no more; it shall never be rebuilt.",
      "M": "For you have turned a city into a heap of rubble, a fortified city into a ruin; the stronghold of foreigners is a city no longer — it will never be rebuilt.",
      "T": "You turned a great city into rubble,\na fortress into a ruin;\nthe stronghold of aliens is a city no more —\nnever to be rebuilt."
    },
    "3": {
      "L": "Therefore a strong people will glorify thee; the city of ruthless nations will fear thee.",
      "M": "Therefore strong peoples will glorify you; cities of ruthless nations will stand in awe of you.",
      "T": "So strong peoples will give you glory;\nthe city of ruthless nations will tremble before you."
    },
    "4": {
      "L": "For thou hast been a fortress for the poor, a fortress for the needy in distress, a shelter from the tempest, a shade from the heat; for the blast of the ruthless is as a storm against a wall.",
      "M": "For you have been a refuge for the poor, a refuge for the needy in their distress, a shelter from the storm, a shade from the scorching heat. The blast of the ruthless is like a driving rainstorm against a wall.",
      "T": "You have been a fortress for the helpless,\na shelter for the needy in their trouble —\na refuge from the tempest,\nshade against the scorching heat.\nFor the ruthless come like a wall-shattering storm."
    },
    "5": {
      "L": "Thou shalt bring down the noise of strangers as heat in a dry place; as heat subdued by the shadow of a cloud, so the boast of the ruthless shall be brought low.",
      "M": "You silence the clamor of the foreigners as drought is broken by cloud-shadow; you subdue the triumph of the ruthless.",
      "T": "You silence the roar of alien nations —\nas cloud-shadow kills the heat of the open desert,\nso the boasting of the ruthless\nyou bring down to nothing."
    },
    "6": {
      "L": "And in this mountain shall the LORD of hosts make for all peoples a feast of fat things, a feast of wines on the lees; of fat things full of marrow, of wines on the lees well refined.",
      "M": "On this mountain the LORD of hosts will prepare a feast for all peoples — a feast of rich food and well-aged wines, of choice meat full of marrow, of the finest strained vintages.",
      "T": "On this mountain Yahweh of hosts will spread a banquet for all peoples —\nrich food, aged wine,\nthe finest cuts of meat,\nthe most carefully strained vintages.\nEvery nation is invited."
    },
    "7": {
      "L": "And he will destroy in this mountain the face of the shroud cast over all peoples, and the veil that is spread over all nations.",
      "M": "On this mountain he will destroy the shroud that is cast over all peoples, the sheet that is spread over all nations.",
      "T": "On this mountain he will tear away\nthe shroud of grief that covers every nation,\nthe death-veil spread over all peoples."
    },
    "8": {
      "L": "He will swallow up death forever; and the Lord GOD will wipe away tears from all faces; and the rebuke of his people he will take away from all the earth; for the LORD has spoken.",
      "M": "He will swallow up death forever. The Lord GOD will wipe away every tear from every face; the disgrace of his people he will remove from all the earth — for the LORD has spoken.",
      "T": "He will swallow death — swallow it forever.\nThe Lord Yahweh will wipe every tear from every face;\nthe shame his people have borne\nhe will lift from all the earth.\nYahweh has spoken it."
    },
    "9": {
      "L": "And it shall be said in that day, Lo, this is our God; we have waited for him, and he will save us; this is the LORD, we have waited for him; we will be glad and rejoice in his salvation.",
      "M": "In that day they will say: 'This is our God; we waited for him, and he has saved us. This is the LORD; we waited for him. Let us rejoice and be glad in his salvation.'",
      "T": "On that day they will say:\n'Here he is — this is our God!\nWe waited for him, and now he has saved us.\nThis is Yahweh — we waited for him!\nNow we rejoice and shout for joy in his deliverance!'"
    },
    "10": {
      "L": "For in this mountain shall the hand of the LORD rest; and Moab shall be trodden down under him, as straw is trodden down in a dungpit.",
      "M": "For the hand of the LORD will rest on this mountain, but Moab will be trampled in place, as straw is trampled down into a dung heap.",
      "T": "The hand of Yahweh will rest on this mountain —\nbut Moab will be trampled beneath it,\nas straw is pressed down into a dung heap."
    },
    "11": {
      "L": "And he shall spread out his hands in the midst thereof, as a swimmer spreads his hands to swim; and he shall lay low their pride with the strokes of their hands.",
      "M": "He will spread his hands over Moab as a swimmer spreads his arms to stroke through water, and he will bring down their pride despite all their struggling.",
      "T": "He will press Moab down\nas a swimmer pushes the water aside with every stroke —\nuntil their pride collapses\nand all their scheming comes to nothing."
    },
    "12": {
      "L": "And the fortress of the high fort of thy walls shall he bring down, lay low, and bring even to the ground, to the dust.",
      "M": "The high fortifications of your walls he will pull down, lay low, and cast to the ground — to the very dust.",
      "T": "Your towering walls, your loftiest fortresses —\nhe will bring them down, lay them flat,\nand cast them into the dust."
    }
  },
  "26": {
    "1": {
      "L": "In that day shall this song be sung in the land of Judah: We have a strong city; salvation will God appoint as walls and bulwarks.",
      "M": "In that day this song will be sung in the land of Judah: We have a strong city; God has appointed salvation as its walls and ramparts.",
      "T": "On that day this song will be sung in the land of Judah:\n'We have a strong city —\nGod himself has set salvation as our walls,\nas ramparts around us.'"
    },
    "2": {
      "L": "Open ye the gates, that the righteous nation which keepeth the truth may enter in.",
      "M": "Open the gates, so that the righteous nation that keeps faith may enter.",
      "T": "Throw open the gates!\nLet the righteous nation enter —\nthe people who keep faith."
    },
    "3": {
      "L": "Thou wilt keep him in peace, peace, whose mind is stayed on thee, because he trusteth in thee.",
      "M": "You will keep in perfect peace the one whose mind is stayed on you, because he trusts in you.",
      "T": "The mind that rests on you\nyou hold in perfect peace —\nbecause it trusts in you."
    },
    "4": {
      "L": "Trust in the LORD forever; for in Yah, the LORD, is an everlasting Rock.",
      "M": "Trust in the LORD forever, for the LORD — Yah himself — is an everlasting Rock.",
      "T": "Trust in Yahweh — trust him forever —\nfor Yah, Yahweh himself,\nis the everlasting Rock."
    },
    "5": {
      "L": "For he bringeth down them that dwell on high; the lofty city he layeth low, even to the ground, to the dust.",
      "M": "For he brings down those who dwell on high; the lofty city he brings to the ground — to the very dust.",
      "T": "He brings down the proud who dwell in high places;\nthe lofty city he levels —\ndown to the ground, down to the dust."
    },
    "6": {
      "L": "The foot shall tread it down — the feet of the poor, the steps of the needy.",
      "M": "It will be trampled underfoot — by the feet of the poor, by the steps of the needy.",
      "T": "And who will walk across it?\nThe poor — their feet will stamp it down.\nThe needy — their steps will claim it."
    },
    "7": {
      "L": "The way of the righteous is uprightness; O thou Most Upright, thou dost make smooth the path of the righteous.",
      "M": "The path of the righteous is level; you who are just make the way of the righteous smooth.",
      "T": "The path of the righteous runs level —\nyou who are perfectly just\nsmooth the road before them."
    },
    "8": {
      "L": "Yea, in the way of thy judgments, O LORD, we have waited for thee; the desire of our soul is to thy name and to the remembrance of thee.",
      "M": "In the path of your judgments, LORD, we have waited for you; your name and your renown are the deepest longing of our souls.",
      "T": "Walking the path your judgments lay down, O Yahweh —\nwe have waited for you.\nThe longing of our whole being is for your name,\nfor every memory of you."
    },
    "9": {
      "L": "With my soul I have desired thee in the night; yea, with my spirit within me I seek thee earnestly; for when thy judgments are in the earth, the inhabitants of the world learn righteousness.",
      "M": "My soul yearns for you in the night; within me my spirit seeks you eagerly; for when your judgments come upon the earth, the world's inhabitants learn what is right.",
      "T": "In the night my whole being reaches out for you;\ndeep within me my spirit longs for you.\nFor when your judgments fall on the earth,\nthe people of the world learn what righteousness means."
    },
    "10": {
      "L": "Though grace be shown to the wicked, he will not learn righteousness; in the land of uprightness he deals unjustly and will not behold the majesty of the LORD.",
      "M": "Even when the wicked receive grace, they do not learn righteousness; in a land of uprightness they act wrongly and fail to see the LORD's majesty.",
      "T": "Show mercy to the wicked — still they refuse to learn what is right.\nEven in a land of uprightness they go on acting unjustly,\nblind to the majesty of Yahweh."
    },
    "11": {
      "L": "LORD, thy hand is lifted up, but they see it not; let them see thy zeal for thy people and be ashamed; yea, the fire for thine enemies shall devour them.",
      "M": "LORD, your hand is raised high, but they do not see it. Let them see your zeal for your people and be put to shame. Let the fire reserved for your enemies consume them.",
      "T": "Yahweh, your hand is raised —\nbut they refuse to see it.\nLet them finally see your burning zeal for your people,\nand let shame fall on them.\nLet the fire prepared for your enemies devour them."
    },
    "12": {
      "L": "LORD, thou wilt ordain peace for us; for thou hast also wrought all our works for us.",
      "M": "LORD, you will establish peace for us; for all we have accomplished, you have done it for us.",
      "T": "Yahweh, you will establish peace for us —\nfor everything we have done, you accomplished it in us."
    },
    "13": {
      "L": "O LORD our God, other lords besides thee have ruled over us; but by thee only will we acknowledge thy name.",
      "M": "LORD our God, other masters have ruled over us; but we will acknowledge your name alone.",
      "T": "O Yahweh, our God —\nother lords have dominated us,\nbut you alone are the one we name and acknowledge."
    },
    "14": {
      "L": "They are dead; they shall not live; they are shades; they shall not rise; therefore thou hast visited and destroyed them, and made all memory of them to perish.",
      "M": "They are dead — they will not live again; the shades below will not rise. You have punished them and destroyed them, and wiped out every memory of them.",
      "T": "They are dead — they will not live;\nthe shades of the dead will not rise.\nYou punished and erased them;\nevery memory of them is gone."
    },
    "15": {
      "L": "Thou hast increased the nation, O LORD; thou hast increased the nation; thou art glorified; thou hast extended all the borders of the land.",
      "M": "You have enlarged the nation, LORD; you have enlarged the nation and gained glory; you have extended all the borders of the land.",
      "T": "You have made the nation great, O Yahweh —\ngreat and greater still, to your own glory —\npushing its borders out to every corner of the land."
    },
    "16": {
      "L": "LORD, in distress they visited thee; they poured out a whispered prayer when thy chastening was upon them.",
      "M": "LORD, in their distress they sought you out; when your discipline fell on them, they whispered their prayers to you.",
      "T": "Yahweh, in their distress they finally came to you —\nwhen your discipline pressed down on them,\nthey poured out their prayers in whispers."
    },
    "17": {
      "L": "Like a woman with child, who draws near the time of her delivery, writhing in pain and crying out in her anguish — so have we been before thee, O LORD.",
      "M": "As a pregnant woman near delivery writhes in pain and cries out in her anguish, so have we been in your sight, LORD.",
      "T": "Like a woman full-term with child,\nwho writhes and cries out as the birth approaches —\nthat is how we have been before you, O Yahweh."
    },
    "18": {
      "L": "We have been with child; we have been in pain; we have as it were brought forth wind; we have achieved no deliverance in the earth; the inhabitants of the world have not fallen.",
      "M": "We were pregnant, we writhed in labor, but we gave birth to nothing but wind. We have brought no deliverance to the earth, and the world's oppressors have not been overthrown.",
      "T": "We conceived, we labored —\nbut gave birth to nothing but wind.\nWe accomplished no deliverance for the earth;\nthe oppressors of the world still stand."
    },
    "19": {
      "L": "Thy dead shall live; my dead body shall rise; awake and sing, ye that dwell in the dust: for thy dew is as the dew of the dawn, and the earth shall give birth to the dead.",
      "M": "Your dead will live; my corpse will rise. Awake and sing for joy, you who lie in the dust! For your dew is like the morning dew on fresh grass, and the earth will give birth to its dead.",
      "T": "Your dead will live — yes, even my own body will rise!\nAwake and sing for joy, you who sleep in the dust —\nfor your dew is the dew of a new morning,\nand the earth will give birth to the long-dead."
    },
    "20": {
      "L": "Come, my people, enter thy chambers and shut thy doors behind thee; hide thyself for a little moment until the indignation has passed.",
      "M": "Come, my people, enter your chambers and shut your doors behind you. Hide yourself for just a little while until the LORD's wrath has swept past.",
      "T": "Come, my people — enter your inner rooms,\nshut your doors behind you.\nHide yourself for just a little while\nuntil the fury has swept past."
    },
    "21": {
      "L": "For behold, the LORD cometh out of his place to punish the inhabitants of the earth for their iniquity; the earth also shall disclose her blood, and shall no more cover her slain.",
      "M": "For look — the LORD is coming out of his place to punish the earth's inhabitants for their sin. The earth will expose its blood and no longer cover its slain.",
      "T": "See — Yahweh comes out of his place\nto punish the earth's inhabitants for all their sin.\nThe earth will bring its hidden bloodshed to light;\nno longer will it cover its murdered dead."
    }
  },
  "27": {
    "1": {
      "L": "In that day the LORD will punish with his fierce, great, and strong sword Leviathan the fleeing serpent, Leviathan the twisting serpent; and he will slay the dragon that is in the sea.",
      "M": "In that day the LORD will punish with his fierce, great, and powerful sword: Leviathan the fleeing serpent and Leviathan the coiling serpent — and he will slay the dragon of the sea.",
      "T": "On that day Yahweh will draw his great, fierce sword —\nhis mighty, well-honed blade —\nand strike down Leviathan, the swift darting serpent,\nLeviathan, the coiling monster of the deep,\nand slay the dragon lurking in the sea."
    },
    "2": {
      "L": "In that day, sing of her: A vineyard of choice wine!",
      "M": "In that day, sing about it: 'A vineyard of choice wine!'",
      "T": "On that day, sing this song:\n'A vineyard — bursting with the finest wine!'"
    },
    "3": {
      "L": "I, the LORD, am its keeper; I water it every moment; lest any harm it, I keep it night and day.",
      "M": "I, the LORD, tend it; I water it constantly; so that nothing can hurt it, I guard it day and night.",
      "T": "I, Yahweh, am its keeper;\nI water it at every moment.\nSo that nothing can harm it, I guard it night and day."
    },
    "4": {
      "L": "Fury is not in me; who would set briers and thorns against me in battle? I would march through them; I would burn them together.",
      "M": "I have no wrath against my vineyard. If briers and thorns came against me in battle, I would stride through them and burn them all down.",
      "T": "I have no anger against my vineyard.\nIf briers and thorns rise against me in battle,\nI will march through them and burn them down."
    },
    "5": {
      "L": "Or else let him take hold of my strength, that he may make peace with me; and he shall make peace with me.",
      "M": "Or else let him come to me for refuge; let him make peace with me — yes, let him make peace with me.",
      "T": "Let anyone who would oppose me\ntake hold of my strength instead —\nlet them come and make peace with me.\nLet them make peace with me."
    },
    "6": {
      "L": "In days to come Jacob shall take root; Israel shall blossom and bud, and fill the face of the world with fruit.",
      "M": "In coming days Jacob will take root; Israel will blossom and sprout and fill the whole world with fruit.",
      "T": "In coming days Jacob will take deep root;\nIsrael will blossom and bud\nand fill the whole wide world with fruit."
    },
    "7": {
      "L": "Hath he struck him as he struck those who struck him? Or is he slain according to the slaughter of those slain by him?",
      "M": "Has God struck Israel as he struck those who attacked Israel? Has Israel been killed as she killed her enemies?",
      "T": "Has God struck his people the way he struck those who oppressed them?\nHas Israel been slaughtered like those she slaughtered?\nBy no means — the discipline was far lighter than the destruction."
    },
    "8": {
      "L": "By measured exile he dealt with her; he drove her away with his rough wind on the day of the east wind.",
      "M": "By measured exile he dealt with Israel; he removed her with his fierce wind — the scorching east wind.",
      "T": "Measured, measured — that is how he dealt with her:\ndriving her into exile with the fierce east wind,\nthe scorching desert blast.\nNothing beyond what was needed."
    },
    "9": {
      "L": "By this therefore the iniquity of Jacob is purged; and this is the full fruit of the removal of his sin: that he makes all the altar stones like chalk stones crushed to pieces, and Asherah poles and incense altars rise no more.",
      "M": "By this, then, Jacob's guilt will be atoned for; this is the full result of the removal of his sin: he will crush the altar stones to chalk, and no Asherah pole or incense altar will stand.",
      "T": "This is how Jacob's sin will be atoned for —\nthe full result of its removal:\nevery altar stone smashed to chalk,\nno Asherah pole and no incense altar left standing.\nWhen that is done, the guilt is gone."
    },
    "10": {
      "L": "For the fortified city is desolate, the habitation forsaken and left like a wilderness; there the calf feeds and lies down and consumes its branches.",
      "M": "The fortified city stands deserted, its dwellings abandoned like a wilderness — there calves graze and lie down, stripping its branches bare.",
      "T": "The once-fortified city stands desolate;\nevery house abandoned, a wilderness now —\ncalves graze there, lie down there,\nstripping every last branch."
    },
    "11": {
      "L": "When its boughs are withered, they are broken off; women come and kindle them; for it is a people of no understanding; therefore he who made them will not have compassion on them, and he who formed them will show them no favour.",
      "M": "When its branches wither, they are broken off; women come and make fires with them. For this is a people without understanding, so their Maker will not have compassion on them, and their Creator will show them no mercy.",
      "T": "The branches wither; women come to snap them off for firewood.\nThis is a people without understanding —\nso their Maker will have no compassion on them,\ntheir Creator will show them no mercy."
    },
    "12": {
      "L": "And it shall come to pass in that day, the LORD will thresh from the River to the Brook of Egypt, and you will be gathered one by one, O sons of Israel.",
      "M": "In that day the LORD will thresh out his grain from the Euphrates to the Brook of Egypt, and you will be gathered up one by one, O people of Israel.",
      "T": "On that day Yahweh will thresh his grain —\nfrom the great River down to the Brook of Egypt —\nand you will be gathered up one by one,\nO people of Israel."
    },
    "13": {
      "L": "And it shall come to pass in that day, a great trumpet shall be blown; and those who were perishing in the land of Assyria and those exiled in the land of Egypt shall come and worship the LORD on the holy mountain in Jerusalem.",
      "M": "In that day a great trumpet will sound, and those who were perishing in the land of Assyria and those exiled in Egypt will come and worship the LORD on the holy mountain at Jerusalem.",
      "T": "On that day a great trumpet will sound —\nthe lost ones languishing in Assyria,\nthe exiles scattered through Egypt —\nthey will come and worship Yahweh\non the holy mountain in Jerusalem."
    }
  },
  "28": {
    "1": {
      "L": "Woe to the crown of pride of the drunkards of Ephraim, whose glorious beauty is a fading flower, on the head of the rich valley of those overcome with wine!",
      "M": "Woe to the proud crown of Ephraim's drunkards, whose glorious beauty is a fading flower sitting on the head of a fertile valley — the crown of those overcome by wine!",
      "T": "Woe to Ephraim's drunkards — woe to their garland of pride!\nThat glorious flower, already fading,\nperched on the head of the lush valley —\nthe crown of those drunk on wine."
    },
    "2": {
      "L": "Behold, the Lord hath one who is mighty and strong — like a tempest of hail and a destroying storm, like a flood of mighty waters overflowing — who will cast it down to the earth with his hand.",
      "M": "See, the Lord has a powerful agent — like a devastating hailstorm, like a destructive tempest, like a flood of overwhelming waters — who will smash it to the ground.",
      "T": "Watch — the Lord has a mighty agent ready:\nlike a hailstorm, like a raging tempest,\nlike a torrent of floodwaters sweeping everything away —\nhe will dash Ephraim's proud crown to the ground."
    },
    "3": {
      "L": "The proud crown of the drunkards of Ephraim shall be trodden underfoot.",
      "M": "The proud crown of Ephraim's drunkards will be trampled underfoot.",
      "T": "The proud crown of Ephraim's drunkards\nwill be ground underfoot."
    },
    "4": {
      "L": "And the glorious beauty on the head of the fertile valley shall be a fading flower, like the first ripe fig before summer — whoever sees it, while it is still in his hand, he swallows it.",
      "M": "The beautiful crown on the head of the fertile valley will be a fading flower, like a first-ripe fig before summer: whoever spots it snatches and swallows it on the spot.",
      "T": "That glorious crown on the head of the fertile valley —\nit will fade like a flower,\nvanish like an early fig in summer:\nsomeone spots it, snatches it from the branch,\nand it is gone in an instant."
    },
    "5": {
      "L": "In that day the LORD of hosts will be a crown of glory and a diadem of beauty to the remnant of his people.",
      "M": "In that day the LORD of hosts will be a glorious crown and a beautiful diadem for the remnant of his people.",
      "T": "On that day the LORD of hosts will be the crown —\nglorious, beautiful —\nfor every one of his remnant people."
    },
    "6": {
      "L": "And a spirit of justice to him that sitteth in judgment, and strength to those who turn back the battle at the gate.",
      "M": "And he will be a spirit of justice for those who sit in judgment, and strength for those who repel the battle at the gate.",
      "T": "He will be a spirit of justice for those who must judge,\nand strength for those who hold the gate against the enemy."
    },
    "7": {
      "L": "But these also have erred through wine and staggered through strong drink; the priest and the prophet stagger through strong drink, they are swallowed up by wine, they reel with strong drink, they err in vision, they stumble in giving judgment.",
      "M": "But these too stumble through wine and stagger from strong drink: priest and prophet are overcome by strong drink, confused by wine, reeling from intoxication — they err in their visions and stumble in their judgments.",
      "T": "But even these — the priest and the prophet — reel with wine,\nstagger from strong drink.\nSwallowed up by wine, wobbling with drink,\nthey err in their visions\nand stumble over every ruling they make."
    },
    "8": {
      "L": "For all tables are covered with vomit and filth; there is no clean place.",
      "M": "All the tables are covered with vomit and filth; there is no clean space anywhere.",
      "T": "Every table in the place is covered with vomit and filth —\nnot one clean spot to be found."
    },
    "9": {
      "L": "Whom will he teach knowledge? And whom will he make to understand the message? Those just weaned from milk, those just drawn from the breast?",
      "M": "Who is he trying to teach? Who is he trying to make understand his message? Babies just weaned from milk, infants just taken from the breast?",
      "T": "Who does he think he is teaching?\nWho can possibly understand his message?\nToddlers just weaned from the breast?\nThe drunken leaders mock the prophet's repeated warnings as fit only for infants."
    },
    "10": {
      "L": "For it is precept on precept, precept on precept; line on line, line on line; here a little, there a little.",
      "M": "For it is rule on rule, rule on rule; line on line, line on line; a little here, a little there.",
      "T": "'Rule on rule, rule on rule —\nline on line, line on line —\na little here, a little there!'\nThey mimic the prophet's warnings as tedious, meaningless babble."
    },
    "11": {
      "L": "For by stammering lips and a foreign tongue he will speak to this people.",
      "M": "For by people of strange lips and a foreign tongue the LORD will speak to this people.",
      "T": "Therefore God will speak to this people\nthrough foreign stutterers, through a strange language —\nthrough Assyrian conquerors, since they refused to hear his prophets."
    },
    "12": {
      "L": "He has said to them, This is the rest; give rest to the weary; this is the refreshing — yet they would not hear.",
      "M": "He said to them: 'This is the place of rest; give rest to the weary; this is the refreshing.' But they refused to listen.",
      "T": "He said to his people: 'Come here — rest!\nLet the weary find rest here.\nThis is the refreshment you need!' —\nBut they refused to listen."
    },
    "13": {
      "L": "But the word of the LORD will be to them: precept on precept, precept on precept; line on line, line on line; here a little, there a little — that they may go and fall backward, be broken, snared, and taken.",
      "M": "So the word of the LORD will become to them: rule on rule, rule on rule; line on line, line on line; a little here, a little there — so that they stumble backward, are broken, snared, and captured.",
      "T": "So the word of Yahweh becomes to them\nrule on rule, line on line —\na little here, a little there —\nuntil they stumble backward,\nare broken and snared and taken captive."
    },
    "14": {
      "L": "Therefore hear the word of the LORD, ye scornful men, rulers of this people who are in Jerusalem.",
      "M": "So hear the word of the LORD, you scoffers who rule this people in Jerusalem.",
      "T": "Hear the word of Yahweh, you scoffers —\nyou who govern this people in Jerusalem."
    },
    "15": {
      "L": "Because ye have said, We have made a covenant with death, and with Sheol we have made an agreement; when the overflowing scourge passes through, it shall not reach us — for we have made lies our refuge and under falsehood we have hidden ourselves.",
      "M": "You have said: 'We have made a covenant with death; with Sheol we have an agreement. When the overwhelming flood sweeps through, it will not touch us — for we have made lies our shelter and hidden ourselves under falsehood.'",
      "T": "You have said: 'We have a deal with Death;\nwe have a pact with Sheol, the realm of the dead.\nWhen the flood of judgment sweeps through,\nit won't touch us —\nwe've built our shelter out of lies,\nour hiding place out of deception.'"
    },
    "16": {
      "L": "Therefore thus saith the Lord GOD: Behold, I am laying in Zion a tested stone, a precious cornerstone, a sure foundation: he that believeth shall not make haste.",
      "M": "So this is what the Lord GOD says: 'See, I am laying a stone in Zion — a tested stone, a precious cornerstone, a sure foundation. Whoever believes will not make haste.'",
      "T": "Therefore the Lord Yahweh declares:\n'See — I am setting a stone in Zion:\na tested stone, a precious cornerstone,\na sure and solid foundation.\nWhoever trusts in it will never panic or flee.'"
    },
    "17": {
      "L": "And I will set justice to the measuring line, and righteousness to the plummet; and the hail will sweep away the refuge of lies, and the waters will overflow the hiding place.",
      "M": "I will measure with justice as my plumb line and righteousness as my level. The hail will sweep away your refuge of lies, and the flood will overwhelm your hiding place.",
      "T": "I will use justice as my measuring line,\nrighteousness as my level —\nand the hailstorm will sweep away your refuge of lies,\nthe floodwaters will overwhelm your hiding place."
    },
    "18": {
      "L": "Then your covenant with death shall be annulled, and your agreement with Sheol shall not stand; when the overflowing scourge passes through, you shall be trodden down by it.",
      "M": "Your covenant with death will be cancelled, and your agreement with Sheol will not hold. When the overwhelming flood sweeps through, you will be crushed under it.",
      "T": "Your deal with Death will be torn up;\nyour pact with Sheol will not hold.\nWhen the flood of judgment sweeps through,\nyou will be crushed beneath it."
    },
    "19": {
      "L": "As often as it passes through, it shall take you; for morning by morning it shall pass, by day and by night; and it shall be sheer terror to understand the message.",
      "M": "Every time it sweeps through, it will seize you. Morning after morning it will come — by day and by night. The very understanding of what it means will be terror.",
      "T": "Every time it sweeps through, it will take you —\nmorning after morning, day and night.\nJust grasping what is happening\nwill be terror enough."
    },
    "20": {
      "L": "For the bed is too short to stretch out on, and the covering too narrow to wrap oneself in.",
      "M": "The bed will be too short to stretch out on, and the covering too narrow to wrap yourself in.",
      "T": "The bed is too short to lie on;\nthe blanket too narrow to wrap yourself in.\nEvery arrangement you made to protect yourself will fail."
    },
    "21": {
      "L": "For the LORD will rise as he rose at Mount Perazim; he will be roused as in the valley of Gibeon, to do his work — his strange work — and to bring his act to pass — his alien act.",
      "M": "For the LORD will rise up as he did at Mount Perazim; he will be roused as in the valley of Gibeon, to carry out his task — his strange task — his work — his alien work.",
      "T": "Yahweh will rise as he rose at Perazim,\nstir himself as in the valley of Gibeon —\nbut this time to do his strange work,\nhis altogether alien act:\nto judge his own people, not their enemies."
    },
    "22": {
      "L": "Now therefore be ye not mockers, lest your bonds grow strong; for I have heard from the Lord GOD of hosts a decree of destruction upon the whole earth.",
      "M": "Now stop your mocking, or your bonds will grow tighter. I have heard from the Lord GOD of hosts a decree of complete destruction against the whole earth.",
      "T": "Stop mocking — before your chains grow tighter.\nI have heard it from the Lord Yahweh of hosts:\na decree of utter destruction upon the whole earth."
    },
    "23": {
      "L": "Give ear and hear my voice; attend and hear my speech.",
      "M": "Listen and hear my voice; pay attention and hear what I say.",
      "T": "Listen — hear my voice;\nlean in and hear what I am saying."
    },
    "24": {
      "L": "Does the plowman plow all day in order to sow? Does he continually open up and break the clods of his ground?",
      "M": "Does a farmer spend the whole day plowing in order to plant? Does he keep breaking up the clods of his field forever?",
      "T": "Does the farmer spend all day plowing just to plant a seed?\nDoes he break up clods without end?"
    },
    "25": {
      "L": "When he has leveled its surface, does he not scatter the caraway, spread the cumin, plant the wheat in rows, the barley in its allotted place, and the spelt at its border?",
      "M": "When he has leveled the surface, he broadcasts caraway, scatters cumin, plants wheat in rows, barley in its proper place, and spelt along its edge.",
      "T": "No — when the ground is ready, he plants with precision:\ncaraway here, cumin scattered there,\nwheat in rows, barley in its allotted place,\nspelt along the border.\nEach seed gets exactly what it needs."
    },
    "26": {
      "L": "For his God instructs him rightly and teaches him.",
      "M": "His God instructs him in the right way and teaches him.",
      "T": "His God has taught him;\ntrained him to know exactly what to do."
    },
    "27": {
      "L": "For caraway is not threshed with a threshing sledge, nor is a cartwheel rolled over cumin; but caraway is beaten out with a stick, and cumin with a rod.",
      "M": "Caraway is not threshed with a sledge, nor does a cartwheel roll over cumin. Caraway is beaten with a stick, and cumin with a rod.",
      "T": "You don't thresh caraway with a threshing sledge —\nor run the cartwheel over cumin.\nCaraway gets a stick; cumin gets a rod.\nEach crop gets exactly the right treatment."
    },
    "28": {
      "L": "Grain for bread is crushed — but he does not go on threshing it forever; and though his cartwheel drives over it and his horses trample it, he does not crush it to powder.",
      "M": "Grain for bread must be crushed, but a farmer does not go on threshing it forever. He drives his cartwheel over it and lets horses trample it, but he does not grind it to powder.",
      "T": "Grain for bread must be crushed —\nbut no farmer threshes it forever.\nHe may drive his cartwheel across it,\nlet horses trample it —\nbut he never grinds it to dust.\nThe grain survives to become bread."
    },
    "29": {
      "L": "This also comes forth from the LORD of hosts, who is wonderful in counsel and excellent in understanding.",
      "M": "All of this too comes from the LORD of hosts, whose counsel is wonderful and whose skill is great.",
      "T": "All this wisdom comes from Yahweh of hosts —\nwonderful in counsel,\nexcellent in everything he does."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 25–28 written.')

if __name__ == '__main__':
    main()
