"""
MKT Isaiah chapters 29–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-29-30.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts;
  divine personal name surfaced in T throughout Isaiah.
- H136 (אֲדֹנָי): "Lord" (L/M/T); in 30:15 "אֲדֹנָי יְהוָה" = "the Lord GOD" (L/M) /
  "the Lord Yahweh" (T).
- H6635 (צְבָאוֹת): "of hosts" (all tiers) — cosmic sovereignty designation, consistent.
- H4853 (מַשָּׂא): "oracle" (M/T) / "burden" (L) — in 30:6 functions as a section heading
  ("The oracle of the beasts of the Negeb"); L preserves concrete weight of prophetic speech.
- H743 (אֲרִיאֵל): "Ariel" preserved as a name in all tiers; L/M carry the place-name force
  (Jerusalem); T notes the double meaning — lion of God / altar hearth — especially in 29:2
  where the wordplay turns sinister: Jerusalem becomes what her name says, an altar hearth
  for judgment.
- H7307 (רוּחַ): 29:10 "spirit of deep sleep" = lowercase, not the divine Spirit; 30:1
  "not of my Spirit" = upper-case Spirit, explicitly divine — context determines.
- H5315 (נֶפֶשׁ): Not prominent in these chapters.
- H2617 (חֶסֶד): Does not appear in chs. 29–30.
- H4941 (מִשְׁפָּט): 30:18 "a God of justice" = "judgment" (L) / "justice" (M/T) — consistent
  with all prior Isaiah scripts.
- H7295 (רַהַב): 30:7 "Rahab" = the mythological sea dragon, a poetic name for Egypt;
  "Rahab who sits still" = the great sea-beast that does nothing. All tiers preserve the name.
- H8612 (תֹּפֶת): 30:33 "Topheth" = the burning-place (valley of Hinnom, later Gehenna);
  L uses "Topheth"; M/T explain its nature as the prepared place of judgment.
- 29:13 — Jesus quotes this verse (Matt 15:8, Mark 7:6); T makes the heart-versus-lips
  tension vivid without adding commentary.
- 29:16 — Potter/clay reversal is a key Isaiah motif (cf. 45:9, 64:8); T connects explicitly
  to the absurdity of the creature judging the Creator.
- 30:15 — "In returning and rest... quietness and trust": one of Isaiah's most theologically
  dense lines; שׁוּבָה = repentant return, נַחַת = rest/quietness, שְׁקֵט = tranquility,
  בִּטְחָה = confident trust; T keeps all four terms distinct and memorable.
- 30:20 — "your Teacher" (מוֹרֶיךָ) is plural of majesty (a Hebrew honorific singular);
  refers to Yahweh himself as teacher — not a human figure. All tiers preserve the capital T.
- 30:33 — "for the king" refers to the king of Assyria (Sennacherib); the phrase carries
  deliberate ambiguity extending to any monarch who opposes Yahweh.
- Poetry/prose structure: Ch. 29:1–8 — poetic oracle (siege and sudden reversal). 29:9–12 —
  prose indictment. 29:13–16 — prophetic poetry (Yahweh's speech + woe saying). 29:17–24 —
  eschatological prose-poetry ("in that day" reversals). Ch. 30:1–7 — prose woe oracle.
  30:8–17 — prose command + indictment. 30:18–26 — restoration oracle, prose-poetry.
  30:27–33 — theophany poetry (the LORD as storm). T uses line breaks for the most
  concentrated poetic sections throughout.
- Aspect: Prophetic presents in 29:1–8 rendered as vivid future certainties (the Hebrew
  perfect of prophecy = "it is done"). The "in that day" sections (29:17–24, 30:18–26)
  are eschatological futures. 30:1–7 indictment uses present-tense description; 30:27–33
  theophany uses vivid present of the arriving divine judgment.
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
  "29": {
    "1": {
      "L": "Woe to Ariel, to Ariel, the city where David encamped! Add year to year; let the feasts run their round.",
      "M": "Woe to Ariel, to Ariel, the city where David made his camp! Add year to year; let the festivals continue their cycle.",
      "T": "Woe to Ariel! To Ariel —\ncity where David pitched his camp!\nAdd year to year; let the sacred feasts keep coming round —"
    },
    "2": {
      "L": "yet I will distress Ariel, and there shall be mourning and lamentation, and she shall be to me as an Ariel.",
      "M": "yet I will besiege Ariel; there will be mourning and lamentation, and she will become to me like an altar hearth.",
      "T": "yet I will lay siege to Ariel,\nand there will be mourning and anguish —\nand she will be to me what her name says: an altar hearth, a fire pit, consumed."
    },
    "3": {
      "L": "And I will camp against thee round about, and will lay siege against thee with a mound, and will raise forts against thee.",
      "M": "I will encamp against you on every side; I will besiege you with a mound and raise siege-works against you.",
      "T": "I will ring you round with a siege camp,\nbatter you with earthworks,\nand raise fortifications against you."
    },
    "4": {
      "L": "Then you shall be brought low, and shall speak from the ground; your speech shall come from the dust; your voice shall be as of one that hath a familiar spirit, out of the ground; and thy speech shall whisper from the dust.",
      "M": "Then you will be brought low; you will speak from the ground, and your words will come up from the dust; your voice will be like a ghost murmuring from the ground, and your speech will whisper out of the dust.",
      "T": "Then you will be laid flat —\nyou will speak from the ground,\nyour words barely a whisper rising from the dust,\nyour voice like a ghost moaning up from the earth,\nyour speech a murmur scraped from the dust."
    },
    "5": {
      "L": "Moreover the multitude of thy foes shall be like small dust, and the multitude of tyrants shall be as chaff that passeth away; yea, it shall be in an instant, suddenly —",
      "M": "But the horde of your enemies will become like fine dust, and the multitude of the ruthless like blowing chaff. And in an instant, suddenly —",
      "T": "But the horde of your enemies will crumble to fine dust,\nthe multitude of tyrants scatter like windblown chaff —\nand then, in an instant, suddenly —"
    },
    "6": {
      "L": "thou shalt be visited of the LORD of hosts with thunder, and with earthquake, and great noise, with storm and tempest, and the flame of devouring fire.",
      "M": "you will be visited by the LORD of hosts with thunder and earthquake and great noise, with storm and tempest and flame of devouring fire.",
      "T": "Yahweh of hosts will appear:\nthunder, earthquake, shattering noise —\nwhirlwind, tempest, the flame of consuming fire."
    },
    "7": {
      "L": "And the multitude of all the nations that fight against Ariel, even all that fight against her and her stronghold, and that distress her, shall be as a dream, a vision of the night.",
      "M": "And the multitude of all the nations that fight against Ariel — all who fight against her and her fortifications and press her hard — will be like a dream, a vision of the night.",
      "T": "All the nations that mass against Ariel —\nall who besiege her, press her hard, assault her walls —\nwill dissolve like a dream, a vision of the night."
    },
    "8": {
      "L": "As when a hungry man dreameth that he eateth, but he awaketh, and his soul is empty; or as when a thirsty man dreameth that he drinketh, but he awaketh, and behold, he is faint and his soul hath appetite — so shall the multitude of all the nations be that fight against mount Zion.",
      "M": "As when a hungry man dreams of eating and wakes still hungry, or as when a thirsty man dreams of drinking and wakes still parched and craving — so will the multitude of all the nations be that fight against Mount Zion.",
      "T": "Like a hungry man who dreams of a feast\nand wakes with his stomach still empty,\nor a thirsty man who dreams of a long drink\nand wakes faint, still craving —\nso will every nation that masses against Mount Zion wake up."
    },
    "9": {
      "L": "Stay yourselves and wonder; blind yourselves and be blind: they are drunken, but not with wine; they stagger, but not with strong drink.",
      "M": "Be stunned and bewildered; be blinded and stay blind! They are drunk, but not with wine; they stagger, but not with strong drink.",
      "T": "Stand stupefied — stay there bewildered.\nBe blind — go on being blind.\nThey are drunk, but not with wine;\nthey stagger, but not with strong drink."
    },
    "10": {
      "L": "For the LORD hath poured out upon you the spirit of deep sleep, and hath closed your eyes: the prophets, and your rulers; the seers, hath he covered.",
      "M": "For the LORD has poured out on you a spirit of deep sleep; he has shut your eyes — the prophets — and covered your heads — the seers.",
      "T": "For Yahweh has poured over you a spirit of stupor —\nhe has shut your eyes: those who call themselves prophets.\nHe has veiled your heads: those who call themselves seers."
    },
    "11": {
      "L": "And the vision of all this has become to you as the words of a book that is sealed, which men deliver to one that is learned, saying, Read this, I pray thee; and he saith, I cannot, for it is sealed.",
      "M": "And the vision of all this has become to you like the words of a sealed book. When someone gives it to a literate person and says, 'Please read this,' he replies, 'I cannot — it is sealed.'",
      "T": "All of this vision has become for you\nlike a sealed book —\nhand it to someone who can read and say, 'Read this,' and he says,\n'I can't — it's sealed.'"
    },
    "12": {
      "L": "And the book is delivered to him that is not learned, saying, Read this, I pray thee; and he saith, I am not learned.",
      "M": "And when the book is given to one who cannot read, saying, 'Please read this,' he answers, 'I cannot read.'",
      "T": "Hand it to someone who can't read and say, 'Read this,' and he answers,\n'I don't know how to read.'\nNeither one can open it."
    },
    "13": {
      "L": "And the Lord said: Because this people draw near, and with their mouth and with their lips do honour me, but their heart is far from me, and their fear of me is a commandment of men that hath been taught them —",
      "M": "And the Lord said: 'Because this people draw near with their mouth and honor me with their lips, while their heart is far from me, and their reverence for me is merely a commandment learned by rote from men —'",
      "T": "And the Lord declared:\n'Because this people approaches me with their mouth\nand honors me with their lips,\nwhile their heart is nowhere near me —\nand their awe of me is nothing but a rule\ndrilled into them by other humans —'"
    },
    "14": {
      "L": "therefore, behold, I will proceed to do a marvellous work among this people, even a marvellous work and a wonder; and the wisdom of their wise men shall perish, and the understanding of their prudent men shall be hid.",
      "M": "therefore, watch — I am about to do something astonishing among this people, something astonishing and astounding; the wisdom of their wise men will perish, and the insight of their discerning men will vanish.",
      "T": "'therefore watch — I am about to do something among this people\nthat will leave everyone astonished:\nthe wisdom of the wise will collapse,\nand the insight of the shrewd will disappear.'"
    },
    "15": {
      "L": "Woe unto them that seek deep to hide their counsel from the LORD, and their works are in the dark, and they say, Who seeth us? and Who knoweth us?",
      "M": "Woe to those who go to great lengths to hide their plans from the LORD, who work in darkness and say, 'Who sees us? Who knows us?'",
      "T": "Woe to those who burrow deep to hide their schemes from Yahweh,\nwho do their work in the dark and say,\n'Who can see us? Who knows what we're doing?'"
    },
    "16": {
      "L": "O your perverseness! Shall the potter be esteemed as clay; that the thing made should say of him that made it, He made me not; or the thing formed say of him that formed it, He hath no understanding?",
      "M": "How you have everything backwards! Should the potter be regarded as no different from clay? Should what is made say of its maker, 'He did not make me'? Should what is formed say of him who formed it, 'He has no understanding'?",
      "T": "What a reversal you have made!\nShall the clay treat the potter as its equal?\nShall the pot say to the one who made it, 'You didn't make me'?\nShall the vessel say to its maker, 'You don't understand anything'?"
    },
    "17": {
      "L": "Is it not yet a very little while, and Lebanon shall be turned into a fruitful field, and the fruitful field shall be esteemed as a forest?",
      "M": "Is it not just a little while until Lebanon becomes a fruitful orchard, and the fruitful orchard is considered a forest?",
      "T": "Only a little while longer —\nand Lebanon will be turned into an orchard,\nand what is now orchard will seem like ancient forest."
    },
    "18": {
      "L": "And in that day shall the deaf hear the words of a book, and the eyes of the blind shall see out of obscurity and out of darkness.",
      "M": "In that day the deaf will hear the words of a book, and out of gloom and darkness the eyes of the blind will see.",
      "T": "On that day the deaf will hear\nthe words of a scroll —\nand out of deep gloom and darkness\nthe eyes of the blind will see."
    },
    "19": {
      "L": "The meek also shall increase their joy in the LORD, and the poor among men shall rejoice in the Holy One of Israel.",
      "M": "The meek will find renewed joy in the LORD, and the poorest among people will exult in the Holy One of Israel.",
      "T": "The meek will find fresh joy in Yahweh,\nand the poorest of the poor will exult in the Holy One of Israel."
    },
    "20": {
      "L": "For the terrible one is brought to nought, and the scorner is consumed, and all that watch for iniquity are cut off —",
      "M": "For the tyrant will be no more, and the scoffer will vanish, and all who look for opportunity to do wrong will be cut off —",
      "T": "For the tyrant will be finished,\nthe mocker will be gone,\nand everyone who lies in wait to do evil will be cut off —"
    },
    "21": {
      "L": "them that make a man an offender for a word, and lay a snare for him that reproveth in the gate, and turn aside the just with an empty plea.",
      "M": "those who trap a man with a word, who lay snares for the one who rebukes corruption at the gate, and who use empty claims to deny justice to the innocent.",
      "T": "those who trap a man with a single word,\nwho set snares for the one who dares to speak truth at the city gate,\nwho twist nothing into a charge and deny the innocent their rights."
    },
    "22": {
      "L": "Therefore thus saith the LORD, who redeemed Abraham, concerning the house of Jacob: Jacob shall not now be ashamed, neither shall his face now wax pale.",
      "M": "Therefore thus says the LORD, who redeemed Abraham, concerning the house of Jacob: 'Jacob will no longer be ashamed; his face will no longer grow pale.'",
      "T": "Therefore this is what Yahweh says —\nthe one who redeemed Abraham —\nconcerning the house of Jacob:\n'Jacob will no longer be put to shame;\nhis face will no longer turn pale with disgrace.'"
    },
    "23": {
      "L": "For when he seeth his children, the work of mine hands, in the midst of him, they shall sanctify my name; yea, they shall sanctify the Holy One of Jacob, and shall stand in awe of the God of Israel.",
      "M": "For when he sees his children — the work of my hands — in his midst, they will sanctify my name; they will sanctify the Holy One of Jacob and stand in awe of the God of Israel.",
      "T": "When he sees his children in his midst —\nthe work of my own hands —\nthey will sanctify my name;\nthey will treat the Holy One of Jacob as holy\nand stand in reverent awe before the God of Israel."
    },
    "24": {
      "L": "They also that erred in spirit shall come to understanding, and they that murmured shall learn instruction.",
      "M": "Those who went astray in spirit will come to understanding, and those who complained will accept instruction.",
      "T": "Those who had gone spiritually astray will come to their senses,\nand those who had nothing but complaints\nwill finally receive instruction."
    }
  },
  "30": {
    "1": {
      "L": "Woe to the rebellious children, saith the LORD, that take counsel, but not of me; and that make an alliance, but not of my spirit, that they may add sin to sin —",
      "M": "Woe to the rebellious children, declares the LORD, who carry out plans but not mine, who make alliances but not by my Spirit, piling sin upon sin —",
      "T": "Woe, rebellious children — Yahweh's word —\nwho make plans but not mine,\nwho forge alliances but not by my Spirit,\nstacking sin upon sin —"
    },
    "2": {
      "L": "that walk to go down into Egypt, and have not asked at my mouth; to strengthen themselves in the strength of Pharaoh, and to trust in the shadow of Egypt!",
      "M": "who set off to go down to Egypt without asking me, who seek to find strength in Pharaoh's power and to take shelter in Egypt's shadow!",
      "T": "who set out to go down to Egypt\nwithout a word to me —\nwho want to shore up their lives in Pharaoh's strength\nand take shelter in Egypt's shadow!"
    },
    "3": {
      "L": "Therefore shall the strength of Pharaoh be your shame, and the trust in the shadow of Egypt your humiliation.",
      "M": "Therefore the strength of Pharaoh will become your shame, and the shelter of Egypt's shadow your humiliation.",
      "T": "So Pharaoh's power will become your disgrace,\nand Egypt's shadow the very thing that humiliates you."
    },
    "4": {
      "L": "For his princes are at Zoan, and his ambassadors are come to Hanes.",
      "M": "For though his officials are stationed at Zoan and his envoys have reached as far as Hanes —",
      "T": "Even with his envoys positioned at Zoan\nand his ambassadors traveling all the way to Hanes —"
    },
    "5": {
      "L": "They were all ashamed of a people that could not profit them, nor be a help nor profit, but a shame, and also a reproach.",
      "M": "everyone will be ashamed because of a nation that cannot help them — no advantage, no aid, only shame and disgrace.",
      "T": "everyone will come away humiliated\nby a nation that cannot deliver —\nno help, no advantage, nothing but shame and reproach."
    },
    "6": {
      "L": "The burden of the beasts of the south: through a land of trouble and anguish, from whence come the young and old lion, the viper and flying serpent, they carry their riches upon the shoulders of young asses, and their treasures upon the humps of camels, to a people that shall not profit them.",
      "M": "The oracle of the beasts of the Negeb. Through a land of trouble and anguish, of lioness and lion, of viper and flying serpent, they carry their wealth on the backs of donkeys and their treasures on the humps of camels, to a people that cannot help them.",
      "T": "Oracle of the beasts of the Negeb.\nThrough a land of trouble and anguish,\nof roaring lion and prowling lioness,\nof viper and winged serpent —\nthey load their wealth onto young donkeys\nand their treasures onto camels' backs,\nand trek it to a people that cannot help them."
    },
    "7": {
      "L": "For Egypt helpeth in vain, and to no purpose: therefore have I called her, Rahab that sitteth still.",
      "M": "For Egypt's help is worthless and empty. Therefore I call her Rahab Who Sits Still.",
      "T": "Egypt's help is nothing — an empty illusion.\nSo I have named her: Rahab Who Sits Still —\nthe great sea-dragon that does not move."
    },
    "8": {
      "L": "Now go, write it before them on a tablet, and inscribe it in a book, that it may be for the time to come for ever and ever.",
      "M": "Now go, write it before them on a tablet and inscribe it in a book, that it may serve as a witness for the days to come, forever and ever.",
      "T": "Now go — write it before them on a tablet;\ncarve it into a scroll\nso it stands as a witness for future days, forever."
    },
    "9": {
      "L": "For it is a rebellious people, lying children, children that will not hear the law of the LORD;",
      "M": "For this is a rebellious people, deceptive children — children who refuse to hear the instruction of the LORD,",
      "T": "For this is a rebellious people,\nchildren of deception —\nchildren who will not hear Yahweh's instruction,"
    },
    "10": {
      "L": "which say to the seers, See not; and to the prophets, Prophesy not unto us right things, speak unto us smooth things, prophesy deceits;",
      "M": "who say to the seers, 'Stop seeing,' and to the prophets, 'Don't prophesy truth to us — speak flattering things, prophesy delusions;'",
      "T": "who say to the seers, 'Stop seeing,'\nand to the prophets, 'Don't give us the truth —\ntell us what we want to hear; prophesy illusions;'"
    },
    "11": {
      "L": "get you out of the way, turn aside out of the path, cause the Holy One of Israel to cease from before us.",
      "M": "get out of the road, turn aside from the path; let us hear no more from the Holy One of Israel.",
      "T": "'get out of the road, clear off the path —\nwe don't want to hear another word\nabout the Holy One of Israel.'"
    },
    "12": {
      "L": "Wherefore thus saith the Holy One of Israel: Because ye despise this word, and trust in oppression and crookedness, and rely thereon;",
      "M": "Therefore thus says the Holy One of Israel: 'Because you reject this word and place your trust in oppression and cunning and rely on them,",
      "T": "Therefore this is what the Holy One of Israel says:\n'Because you despise this word\nand put your confidence in oppression and deviousness and lean on them —'"
    },
    "13": {
      "L": "therefore this iniquity shall be to you as a breach ready to fall, swelling out in a high wall, whose breaking cometh suddenly at an instant.",
      "M": "'therefore this sin will be for you like a crack in a high wall, bulging out, about to collapse — whose fall comes suddenly, in an instant.'",
      "T": "'this sin will hang over you\nlike a crack in a high wall,\nbulging outward,\nready to give way —\nand when it falls, it falls in an instant.'"
    },
    "14": {
      "L": "And he shall break it as a potter's vessel is broken, breaking it in pieces without sparing; so that there shall not be found among the pieces thereof a sherd to take fire from the hearth, or to dip water out of the pit.",
      "M": "'It will shatter like a potter's vessel smashed beyond all saving — no fragment left large enough to carry a coal from the fire or scoop water from a cistern.'",
      "T": "'The collapse will be like a clay pot\nsmashed without mercy —\nso completely shattered\nthat no piece remains large enough\nto carry an ember from the fire\nor dip a sip of water from a tank.'"
    },
    "15": {
      "L": "For thus saith the Lord GOD, the Holy One of Israel: In returning and rest shall ye be saved; in quietness and in confidence shall be your strength: and ye would not.",
      "M": "For thus said the Lord GOD, the Holy One of Israel: 'In repentance and rest you shall be saved; in quietness and in trust shall be your strength.' But you were not willing.",
      "T": "For this is what the Lord Yahweh, the Holy One of Israel, declared:\n'In returning and rest — there is your salvation.\nIn quietness and trust — there is your strength.'\nBut you refused."
    },
    "16": {
      "L": "But ye said, No; for we will flee upon horses — therefore shall ye flee: and, We will ride upon the swift — therefore shall they that pursue you be swift.",
      "M": "And you said, 'No! We will escape on horses' — and so you will flee! 'We will ride on swift horses' — and so those who pursue you will be swift!",
      "T": "You said, 'No — we'll outrun them on horses.'\nSo you will flee.\n'We'll ride swift horses.'\nSo your pursuers will be swifter."
    },
    "17": {
      "L": "One thousand shall flee at the rebuke of one; at the rebuke of five shall ye flee: till ye be left as a beacon upon the top of a mountain, and as an ensign on a hill.",
      "M": "A thousand will flee at the threat of one; at the threat of five you will all run, until you are left like a flagstaff on a mountaintop, like a signal flag on a hill.",
      "T": "A thousand will scatter at the shout of one;\nat the shout of five, you will all run —\nuntil you are left as solitary as a pole on a mountain peak,\na signal flag on a bare hill."
    },
    "18": {
      "L": "And therefore will the LORD wait, that he may be gracious unto you; and therefore will he be exalted, that he may have mercy upon you: for the LORD is a God of judgment: blessed are all they that wait for him.",
      "M": "Therefore the LORD waits to be gracious to you, and therefore he rises up to show you mercy. For the LORD is a God of justice; blessed are all who wait for him.",
      "T": "Therefore Yahweh waits — waits to be gracious to you;\nhe rises up to show you mercy.\nFor Yahweh is a God of justice.\nBlessed are all who wait for him."
    },
    "19": {
      "L": "For a people shall dwell in Zion, in Jerusalem: thou shalt weep no more; he will surely be gracious unto thee at the voice of thy cry; when he heareth it, he will answer thee.",
      "M": "For the people of Zion who dwell in Jerusalem — you will weep no more. He will surely be gracious to you at the sound of your cry; as soon as he hears it, he will answer you.",
      "T": "O people who dwell in Zion, in Jerusalem —\nyou will weep no more.\nHe will be truly gracious to you\nthe moment your cry rises —\nthe moment he hears it, he answers."
    },
    "20": {
      "L": "And though the Lord give you the bread of adversity and the water of affliction, yet shall not thy Teacher be removed into a corner any more, but thine eyes shall see thy Teacher.",
      "M": "And though the Lord gives you the bread of adversity and the water of affliction, your Teacher will no longer hide himself, but your eyes will see your Teacher.",
      "T": "Even if the Lord makes you eat the bread of hardship\nand drink the water of affliction —\nyour Teacher will not hide himself any longer:\nyour own eyes will see your Teacher."
    },
    "21": {
      "L": "And thine ears shall hear a word behind thee, saying, This is the way, walk ye in it, when ye turn to the right hand, and when ye turn to the left.",
      "M": "And your ears will hear a voice behind you saying, 'This is the way; walk in it,' whether you turn to the right or to the left.",
      "T": "And your ears will catch a voice behind you:\n'This is the way — walk in it' —\nwhenever you drift to the right or to the left."
    },
    "22": {
      "L": "And ye shall defile the covering of thy graven images of silver, and the overlaying of thy molten images of gold: thou shalt cast them away as a menstruous cloth; thou shalt say unto it, Get thee hence.",
      "M": "Then you will treat as defiled the silver coating of your carved idols and the gold plating of your cast images; you will throw them away like a menstrual rag, saying to them, 'Away with you!'",
      "T": "Then you will treat your silver-plated idols as filth\nand your gold-overlaid images as unclean —\nflung away like something unclean,\nyour word to them: 'Away with you. Gone.'"
    },
    "23": {
      "L": "And he will give rain for thy seed, wherewith thou shalt sow the ground; and bread of the increase of the ground, and it shall be fat and plenteous: in that day shall thy cattle feed in large pastures.",
      "M": "He will send rain for the seed you sow in the ground; the bread from the ground will be rich and plentiful. In that day your livestock will graze in spacious pastures.",
      "T": "He will send rain for the seed you plant —\nthe land will give back rich, abundant bread.\nOn that day your cattle will graze\nin broad, open pastures."
    },
    "24": {
      "L": "The oxen likewise and the young asses that till the ground shall eat savory provender, which hath been winnowed with the shovel and with the fan.",
      "M": "The oxen and donkeys that work the ground will eat salted fodder, which has been winnowed clean with shovel and fork.",
      "T": "Even the oxen and donkeys that work the fields\nwill eat well-cured, seasoned fodder —\nwinnowed clean with shovel and fork."
    },
    "25": {
      "L": "And there shall be upon every high mountain, and upon every high hill, streams and watercourses, in the day of the great slaughter, when the towers fall.",
      "M": "And on every high mountain and every lofty hill there will be streams and flowing channels, on the day of the great slaughter when the towers fall.",
      "T": "On every high mountain, on every lofty hill,\nthere will be streams and channels of water —\non the day of the great slaughter,\nwhen the towers come down."
    },
    "26": {
      "L": "Moreover the light of the moon shall be as the light of the sun, and the light of the sun shall be sevenfold, as the light of seven days, in the day that the LORD bindeth up the hurt of his people, and healeth the stroke of their wound.",
      "M": "Moreover the light of the moon will be like the light of the sun, and the light of the sun will be seven times stronger — as bright as seven days — in the day when the LORD binds up the wound of his people and heals the blow he has struck them.",
      "T": "And the light of the moon will be\nas bright as the sun once was,\nand the light of the sun seven times over —\nseven days' worth of sunlight blazing at once —\non the day Yahweh binds up the wounds of his people\nand heals the blow he himself delivered."
    },
    "27": {
      "L": "Behold, the name of the LORD cometh from far, burning with his anger, in heavy uplifting of smoke; his lips are full of indignation, and his tongue is as a devouring fire;",
      "M": "See, the name of the LORD comes from far away, burning with anger and heavy with rising smoke; his lips are filled with fury and his tongue is like a consuming fire;",
      "T": "The name of Yahweh is coming — coming from far off,\nburning with fury, thick with billowing smoke;\nhis lips full of wrath,\nhis tongue a tongue of devouring fire —"
    },
    "28": {
      "L": "and his breath is as an overflowing stream, that reacheth even unto the neck, to sift the nations with the sieve of vanity; and a bridle that causeth to err shall be in the jaws of the peoples.",
      "M": "his breath is like a flooding stream reaching to the neck, to sift the nations through a sieve of destruction, and to put a misleading bridle on the jaws of the peoples.",
      "T": "his breath an overflowing torrent\nthat rises up to the neck,\nsifting nations through a sieve of ruin,\ndriving a bit into the jaws of every people\nthat leads them to their end."
    },
    "29": {
      "L": "Ye shall have a song, as in the night when a holy feast is kept; and gladness of heart, as when one goeth with a pipe to come unto the mountain of the LORD, to the Rock of Israel.",
      "M": "You will have a song, like the song sung at night when a holy feast is kept, and gladness of heart, like one who marches to the sound of a flute to go up to the mountain of the LORD, to the Rock of Israel.",
      "T": "But for you there will be a song —\nlike the song that rises in the night of a sacred festival,\ndeep joy of heart,\nlike walking to the sound of a flute\nup to the mountain of Yahweh, to the Rock of Israel."
    },
    "30": {
      "L": "And the LORD shall cause his glorious voice to be heard, and shall shew the lighting down of his arm, with the indignation of his anger, and with the flame of a devouring fire, with a cloudburst, and storm, and hailstones.",
      "M": "The LORD will make his majestic voice heard and make visible the descent of his arm in raging anger and in the flame of a consuming fire — a cloudburst, storm, and hailstones.",
      "T": "Yahweh will thunder in his majestic voice\nand reveal the sweep of his descending arm —\nfuming with rage,\na flame of consuming fire,\ncloudburst, tempest, hailstones crashing down."
    },
    "31": {
      "L": "For through the voice of the LORD shall the Assyrian be dismayed; with his rod shall he smite him.",
      "M": "For at the voice of the LORD the Assyrian will be shattered; with his rod he will strike him down.",
      "T": "At the voice of Yahweh the Assyrian shatters —\nstruck down by the rod he swings."
    },
    "32": {
      "L": "And every stroke of the appointed staff shall be with tabrets and harps; and in battles of shaking will he fight against them.",
      "M": "And every blow of the rod of punishment that the LORD lays on him will be accompanied by tambourines and lyres; and with brandished arm he will battle against them.",
      "T": "Every blow of Yahweh's punishing rod\nwill be played to tambourine and lyre —\nand with arm swinging high he will fight against them."
    },
    "33": {
      "L": "For a Topheth is prepared of old; yea, for the king it is prepared; he hath made it deep and large; the pile thereof is fire and much wood; the breath of the LORD, like a stream of brimstone, doth kindle it.",
      "M": "For Topheth has long been prepared; indeed, it is made ready for the king. Its pyre is deep and wide, with fire and wood in abundance; the breath of the LORD kindles it like a stream of burning sulfur.",
      "T": "For Topheth — the burning place — has been ready since ancient times;\nyes, it has been prepared for the king.\nDeep and wide is its pyre,\nfire and wood in abundance —\nand the breath of Yahweh,\nlike a torrent of brimstone,\nsets it ablaze."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 29–30 written.')

if __name__ == '__main__':
    main()
