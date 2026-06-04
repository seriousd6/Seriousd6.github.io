"""
MKT Isaiah chapters 34–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-34-36.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H123 (אֱדוֹם): "Edom" in all tiers — the Hebrew proper name; "Idumea" is the Greek form
  used in older translations but not the Hebrew; L/M/T all use "Edom."
- H4941 (מִשְׁפָּט): 34:5 "judgment" (L) / "justice" (M/T) — consistent with prior Isaiah scripts
  throughout; the concept in v5 is juridical execution (Yahweh's sword descends for judgment).
- H5359 (נָקָם): "vengeance" throughout; 34:8 / 35:4 — retributive justice; not weakened.
- H7307 (רוּחַ): 34:16 "his Spirit" (uppercase) = the divine Spirit of Yahweh that gathers
  the animals to Edom; context is explicitly divine agency (parallel to "my mouth hath commanded").
- H1350 (גָּאַל): 35:9 "redeemed" — covenantal redemption; Yahweh as kinsman-redeemer.
- H6299 (פָּדָה): 35:10 "ransomed" — commercial/juridical release from bondage; distinct from
  גָּאַל but used in synonymous parallelism in 35:10 for rhetorical completeness. Both terms
  rendered distinctly: "redeemed" (35:9) vs. "ransomed" (35:10).
- H6944 (קֹדֶשׁ): 35:8 "holiness" — the highway is "the Way of Holiness"; the road is defined
  by its consecrated character, not merely clean ritual status.
- H2261 (חֲבַצֶּלֶת): 35:1 — this is a crocus or meadow saffron, not the rose; L uses "crocus"
  as the more accurate botanical rendering.
- H982 (בָּטַח): ch. 36 — "trust" throughout Rabshakeh's speech; his psychological assault
  is precisely aimed at the object of Israel's trust; consistent "trust" rendering keeps the
  rhetorical hammer audible.
- H7262 (רַבְשָׁקֵה): "Rabshakeh" — a title (field commander / chief of staff), not a proper
  name; treated as proper name in all tiers per convention since the Hebrew treats it as a
  personal designation throughout the narrative.
- Poetry/prose: Ch. 34 = doom oracle against Edom (poetry; T uses line breaks). Ch. 35 =
  restoration vision (poetry; T uses line breaks). Ch. 36 = historical narrative, prose
  (identical to 2 Kings 18:13-37); T remains prose but with slight rhetorical sharpening.
- 34:11 — The bird/creature names are disputed in the Hebrew; I follow the scholarly consensus:
  pelican/cormorant (H6893), porcupine/hedgehog (H7090), owl (H3244), raven (H6158).
  L preserves traditional renderings ("cormorant," "bittern") to signal the lexical uncertainty.
- 34:4 — Apocalyptic un-creation: heavens rolled like a scroll echoes Gen 1:1 in reverse;
  T makes the cosmological reversal explicit.
- 34:16 — "Seek and read from the book of the LORD" (סֵפֶר יְהוָה): the LORD authenticates
  his word through his book — an unusual self-referential text; T keeps the reflexive character.
- 35:1 — "solitary place" (H6723, צִיָּה) = parched/dry land; reinforces the botanical miracle.
- 35:8 — "even fools shall not err therein" — the Way of Holiness is foolproof by divine design;
  T surfaces the grace implicit in that provision.
- 36:7 — Rabshakeh's taunt about Hezekiah's reform (removal of high places) is accurate
  historically; he weaponizes Hezekiah's piety as evidence of divine disfavor — a brilliant
  piece of psychological warfare; T sharpens the rhetorical edge.
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
  "34": {
    "1": {
      "L": "Come near, O nations, and hear; listen, O peoples! Let the earth hear, and all its fullness; the world, and all things that come forth from it.",
      "M": "Come near, O nations, and hear! Listen, O peoples! Let the earth hear and everything in it — the world and all that springs from it.",
      "T": "Draw near, every nation — hear this!\nListen, every people!\nLet the earth hear, and all that fills it —\nthe world and everything that comes out of it."
    },
    "2": {
      "L": "For the indignation of the LORD is upon all nations, and his fury upon all their armies; he hath devoted them to destruction, he hath delivered them to the slaughter.",
      "M": "For the LORD is enraged against all the nations and furious against all their armies; he has devoted them to destruction and given them over to slaughter.",
      "T": "Yahweh's indignation falls on every nation,\nhis fury on every one of their armies.\nHe has devoted them to destruction —\ngiven them over to slaughter."
    },
    "3": {
      "L": "Their slain shall be cast out, and their stink shall rise from their carcases; and the mountains shall be melted with their blood.",
      "M": "Their slain will be cast out, and the stench of their corpses will rise; the mountains will be soaked with their blood.",
      "T": "Their corpses will be thrown out unburied —\nthe stench rising from their bodies —\nand the mountains will run with their blood."
    },
    "4": {
      "L": "And all the host of heaven shall be dissolved, and the heavens shall be rolled together as a scroll; and all their host shall fall down, as the leaf falleth from the vine, and as a falling fig from the fig tree.",
      "M": "All the host of heaven will dissolve; the heavens will be rolled up like a scroll. All their host will fall down as a leaf falls from a vine, or as a fig drops from a fig tree.",
      "T": "The whole army of heaven will dissolve —\nthe sky rolled up like a scroll —\nall their host falling\nlike a leaf stripped from the vine,\nlike a fig dropping from a fig tree.\nCreation runs in reverse."
    },
    "5": {
      "L": "For my sword is bathed in heaven; behold, it shall come down upon Edom, and upon the people of my curse, for judgment.",
      "M": "For my sword has been bathed in heaven; see — it descends on Edom, on the people I have devoted to destruction, for judgment.",
      "T": "My sword has been soaking in heaven —\nsee how it descends on Edom,\non the people I have consigned to destruction."
    },
    "6": {
      "L": "The sword of the LORD is filled with blood; it is gorged with fat, with the blood of lambs and goats, with the fat of the kidneys of rams. For the LORD hath a sacrifice in Bozrah, and a great slaughter in the land of Edom.",
      "M": "The sword of the LORD is filled with blood; it is gorged with fat — the blood of lambs and goats, the fat of rams' kidneys. For the LORD has a sacrifice in Bozrah, a great slaughter in the land of Edom.",
      "T": "Yahweh's sword is full of blood,\ndripping with fat —\nblood of lambs and goats,\nfat of rams' kidneys.\nFor Yahweh holds a sacrifice in Bozrah,\na great slaughter in the land of Edom."
    },
    "7": {
      "L": "And the wild oxen shall come down with them, and the young bulls with the bulls; and their land shall be soaked with blood, and their dust made fat with fatness.",
      "M": "Wild oxen will fall with them, young bulls together with mighty bulls; their land will be soaked with blood, and their soil made rich with fat.",
      "T": "Wild oxen go down alongside them,\nthe young bulls with the great bulls —\nthe land soaked with blood,\nthe soil made rich with fat."
    },
    "8": {
      "L": "For it is the day of the LORD's vengeance, the year of recompense for the cause of Zion.",
      "M": "For the LORD has a day of vengeance, a year of recompense for the cause of Zion.",
      "T": "For Yahweh has his day of vengeance —\na year of reckoning for Zion's cause."
    },
    "9": {
      "L": "And the streams thereof shall be turned into pitch, and the dust thereof into brimstone; and the land thereof shall become burning pitch.",
      "M": "The streams of Edom will be turned to tar, its soil to sulfur, and its land will become burning pitch.",
      "T": "The streams of Edom will turn to tar,\nits dust to sulfur —\nthe land itself a lake of burning pitch."
    },
    "10": {
      "L": "It shall not be quenched night or day; its smoke shall go up for ever. From generation to generation it shall lie waste; none shall pass through it for ever and ever.",
      "M": "It will not be quenched night or day; its smoke will rise forever. From generation to generation it will lie desolate; no one will pass through it, forever and ever.",
      "T": "Never quenched — night or day —\nits smoke rising forever.\nFrom generation to generation, desolate;\nno one will ever cross it again."
    },
    "11": {
      "L": "But the cormorant and the bittern shall possess it; the owl and the raven shall dwell in it; and he shall stretch upon it the line of confusion, and the stones of emptiness.",
      "M": "The pelican and the porcupine will take possession of it; the owl and the raven will nest there. The LORD will stretch over it the measuring line of chaos and the plumb line of emptiness.",
      "T": "Pelican and hedgehog will inherit it;\nowl and raven will nest there.\nYahweh will stretch over it\nthe surveyor's line of chaos\nand the plumb line of emptiness."
    },
    "12": {
      "L": "They shall call her nobles to the kingdom, but none shall be there; and all her princes shall be nothing.",
      "M": "They will call it 'No Kingdom There,' and all its princes will come to nothing.",
      "T": "The title they will give it: No Kingdom Here.\nAll its nobles — gone to nothing."
    },
    "13": {
      "L": "And thorns shall come up in her palaces, nettles and brambles in the fortresses thereof; and it shall be a habitation of jackals, and a court for ostriches.",
      "M": "Thorns will overgrow its citadels, nettles and brambles its fortresses; it will become a haunt for jackals, a dwelling place for ostriches.",
      "T": "Thorns will take over its palaces,\nnettles and brambles its fortresses —\nit will become the jackal's lair,\na roost for ostriches."
    },
    "14": {
      "L": "The wild beasts of the desert shall also meet with the wild beasts of the island, and the satyr shall cry to his fellow; the screech owl also shall rest there, and find for herself a place of rest.",
      "M": "Wildcats and hyenas will encounter each other there; the wild goat will call out to his fellow. The night owl will also settle there and find her resting place.",
      "T": "Wildcats and hyenas will meet in its ruins;\nwild goats will call to each other.\nThe night owl will make her home there\nand find her rest."
    },
    "15": {
      "L": "There shall the great owl make her nest, and lay, and hatch, and gather under her shadow; there shall the vultures also be gathered, every one with her mate.",
      "M": "There the great owl will make her nest, lay eggs, hatch, and gather her young under her shadow; and the hawks will assemble there, each with its mate.",
      "T": "There the great owl nests —\nlaying eggs, hatching,\ngathering her young under her shadow —\nand the hawks assemble, each with its mate."
    },
    "16": {
      "L": "Seek ye out of the book of the LORD, and read: no one of these shall be missing, no one shall lack her mate; for my mouth hath commanded, and his Spirit hath gathered them.",
      "M": "Search and read the book of the LORD: not one of these will be absent, not one will lack its mate. For my mouth has issued the command, and his Spirit has gathered them.",
      "T": "Search the book of Yahweh and read:\nnot one of these will be missing,\nnot one will lack its mate —\nfor my mouth has commanded it,\nand his Spirit has assembled them."
    },
    "17": {
      "L": "And he hath cast the lot for them, and his hand hath divided it unto them by line; they shall possess it for ever; from generation to generation they shall dwell therein.",
      "M": "He has cast the lot for them, and his hand has divided it for them by the measuring line; they will possess it forever; from generation to generation they will dwell there.",
      "T": "He has cast the lot for them;\nhis hand has apportioned it by the measuring line.\nThey will possess it forever —\nfrom generation to generation, they will dwell there."
    }
  },
  "35": {
    "1": {
      "L": "The wilderness and the dry land shall be glad; the desert shall rejoice and blossom like the crocus.",
      "M": "The wilderness and the dry land will rejoice; the desert will exult and blossom like the crocus.",
      "T": "The wilderness and the parched land will burst with joy;\nthe desert will celebrate and bloom like the crocus."
    },
    "2": {
      "L": "It shall blossom abundantly, and rejoice even with joy and singing; the glory of Lebanon shall be given unto it, the excellency of Carmel and of Sharon; they shall see the glory of the LORD, the excellency of our God.",
      "M": "It will blossom with lavish abundance and rejoice with joy and singing. The glory of Lebanon will be given to it, the splendor of Carmel and Sharon; they will see the glory of the LORD, the majesty of our God.",
      "T": "It will burst into bloom —\noverflow with joy and singing.\nThe glory of Lebanon given to it,\nthe splendor of Carmel and Sharon —\nand they will see the glory of Yahweh,\nthe majesty of our God."
    },
    "3": {
      "L": "Strengthen ye the weak hands, and confirm the feeble knees.",
      "M": "Strengthen the weak hands, and steady the shaking knees.",
      "T": "Strengthen the weak hands;\nsteady the shaking knees."
    },
    "4": {
      "L": "Say to them that are of a fearful heart, Be strong, fear not; behold, your God will come with vengeance, with the recompense of God; he will come and save you.",
      "M": "Say to those whose hearts are gripped with fear: 'Be strong; do not be afraid! See — your God will come with vengeance, with divine recompense. He will come and save you.'",
      "T": "Say to those whose hearts are trembling with fear:\n'Be strong — do not be afraid!\nLook — your God is coming,\ncoming with vengeance, with divine reckoning.\nHe will come and he will save you.'"
    },
    "5": {
      "L": "Then shall the eyes of the blind be opened, and the ears of the deaf shall be unstopped.",
      "M": "Then the eyes of the blind will be opened, and the ears of the deaf will be unstopped.",
      "T": "Then blind eyes will open\nand deaf ears be cleared."
    },
    "6": {
      "L": "Then shall the lame man leap as a hart, and the tongue of the dumb shall sing; for in the wilderness shall waters break out, and streams in the desert.",
      "M": "Then the lame will leap like a deer, and the tongue of the mute will burst into song. For waters will break out in the wilderness and streams flow through the desert.",
      "T": "The lame will leap like a deer;\nthe silent tongue will break into song.\nFor water will burst out in the wilderness\nand streams cut through the desert."
    },
    "7": {
      "L": "And the mirage shall become a pool, and the thirsty land springs of water; in the habitation of jackals, where each lay, there shall be grass with reeds and rushes.",
      "M": "The burning sand will become a pool, and the thirsty ground springs of water; in the haunt of jackals, where they once rested, the grass will grow with reeds and rushes.",
      "T": "Shimmering desert mirages will become actual pools;\nparched ground will spring up with water.\nWhere jackals once lay in the waste,\ngrass and reeds and rushes will grow."
    },
    "8": {
      "L": "And a highway shall be there, and a way, and it shall be called the Way of Holiness; the unclean shall not pass over it; it shall be for those: the wayfaring men, though fools, shall not err therein.",
      "M": "And a highway will be there, called the Way of Holiness; the unclean will not travel over it. It is for those who walk the road; even fools will not lose their way on it.",
      "T": "A highway will be there — a road —\ncalled the Way of Holiness.\nNo one unclean will walk on it.\nIt is for those who travel it;\neven those who cannot find their way\nwill not go astray on it."
    },
    "9": {
      "L": "No lion shall be there, nor shall any ravenous beast go up thereon; it shall not be found there; but the redeemed shall walk there.",
      "M": "No lion will be there, nor will any ravenous beast be found on it. But the redeemed will walk there.",
      "T": "No lion on that road,\nno ferocious animal will set foot on it —\nnone will be found there.\nOnly the redeemed will walk it."
    },
    "10": {
      "L": "And the ransomed of the LORD shall return, and come to Zion with songs and everlasting joy upon their heads; they shall obtain gladness and joy, and sorrow and sighing shall flee away.",
      "M": "The ransomed of the LORD will return; they will come to Zion with singing, with everlasting joy on their heads. They will reach gladness and joy, and sorrow and sighing will flee away.",
      "T": "The ransomed of Yahweh will return —\nthey will arrive at Zion with songs,\neverlasting joy crowning their heads.\nGladness and joy will overtake them;\nsorrow and sighing will run away."
    }
  },
  "36": {
    "1": {
      "L": "Now it came to pass in the fourteenth year of King Hezekiah, that Sennacherib king of Assyria came up against all the fortified cities of Judah, and took them.",
      "M": "In the fourteenth year of King Hezekiah, Sennacherib king of Assyria marched against all the fortified cities of Judah and captured them.",
      "T": "In the fourteenth year of King Hezekiah's reign, Sennacherib king of Assyria marched against every fortified city of Judah and took them."
    },
    "2": {
      "L": "And the king of Assyria sent Rabshakeh from Lachish to Jerusalem unto King Hezekiah with a great army. And he stood by the conduit of the upper pool in the highway of the fuller's field.",
      "M": "Then the king of Assyria sent his field commander Rabshakeh from Lachish to King Hezekiah in Jerusalem with a large army. He took up a position at the channel of the upper pool, on the road to the Washerman's Field.",
      "T": "Then the king of Assyria sent his field commander Rabshakeh from Lachish to King Hezekiah in Jerusalem with a massive force. He stationed himself at the channel of the upper pool on the road to the Washerman's Field."
    },
    "3": {
      "L": "Then came forth unto him Eliakim, Hilkiah's son, which was over the house, and Shebna the scribe, and Joah, Asaph's son, the recorder.",
      "M": "Then Eliakim son of Hilkiah, the palace administrator, came out to meet him, along with Shebna the secretary and Joah son of Asaph, the recorder.",
      "T": "Eliakim son of Hilkiah, the palace administrator, went out to him, along with Shebna the secretary and Joah son of Asaph, the royal recorder."
    },
    "4": {
      "L": "And Rabshakeh said unto them, Say ye now to Hezekiah, Thus saith the great king, the king of Assyria: What confidence is this wherein thou trustest?",
      "M": "Rabshakeh said to them, 'Tell Hezekiah: This is what the great king, the king of Assyria, says — What is this confidence you are trusting in?'",
      "T": "Rabshakeh said to them, 'Take this message to Hezekiah: This is what the great king — the king of Assyria — says: What is all this confidence you keep leaning on?'"
    },
    "5": {
      "L": "I say, thou speakest of having counsel and strength for war: but they are but vain words; now, on whom dost thou trust, that thou hast rebelled against me?",
      "M": "I tell you — mere words are not strategy or battle strength. So whom do you rely on, that you have dared to rebel against me?",
      "T": "'Let me tell you — words alone are not military strategy or battle strength. Who exactly are you counting on, that you have dared to rebel against me?'"
    },
    "6": {
      "L": "Lo, thou art trusting in the staff of this broken reed, even Egypt; on which if a man lean, it will go into his hand, and pierce it; so is Pharaoh king of Egypt to all that trust on him.",
      "M": "Look — you are leaning on Egypt, that cracked and broken reed of a staff. If anyone leans on it, it pierces right through his hand. That is what Pharaoh king of Egypt is to anyone who trusts him.",
      "T": "'You are leaning on Egypt — that cracked, broken reed of a staff. Press on it and it drives through your hand. That is exactly what Pharaoh king of Egypt is to anyone who trusts him.'"
    },
    "7": {
      "L": "But if thou say to me, We trust in the LORD our God: is it not he, whose high places and whose altars Hezekiah hath taken away, and said to Judah and to Jerusalem, Ye shall worship before this altar?",
      "M": "'But if you say to me, \"We trust in the LORD our God,\" isn't this the very God whose high places and altars Hezekiah removed, telling Judah and Jerusalem, \"You must worship at this one altar\"?'",
      "T": "'Perhaps you'll say, \"We trust in the LORD our God.\" But isn't that the very God whose high places and altars Hezekiah tore down, commanding Judah and Jerusalem to worship only at this one altar?'"
    },
    "8": {
      "L": "Now therefore, I pray thee, make a wager with my master the king of Assyria, and I will give thee two thousand horses, if thou be able on thy part to set riders upon them.",
      "M": "Come now — make a wager with my master the king of Assyria: I will give you two thousand horses, if you can actually find riders to put on them.",
      "T": "'Come then — make a deal with my master the king of Assyria. I will give you two thousand horses — if you can find enough men to ride them.'"
    },
    "9": {
      "L": "How then wilt thou turn away the face of one captain of the least of my master's servants, and put thy trust on Egypt for chariots and for horsemen?",
      "M": "How then could you hold off even one of the least of my master's junior officers? Yet here you are, trusting Egypt for chariots and horsemen!",
      "T": "'How then can you possibly face down even the most junior officer in my master's army? Yet here you are, counting on Egypt for chariots and cavalry!'"
    },
    "10": {
      "L": "And am I now come up without the LORD against this land to destroy it? The LORD said unto me, Go up against this land, and destroy it.",
      "M": "And do you think I have come up against this land without the LORD's approval? The LORD himself said to me: 'March against this land and destroy it.'",
      "T": "'Do you think I came against this land without the LORD's say-so? Yahweh himself told me: Go up against this land and destroy it.'"
    },
    "11": {
      "L": "Then said Eliakim and Shebna and Joah unto Rabshakeh, Speak, I pray thee, unto thy servants in the Syrian language; for we understand it; and speak not to us in the Jews' language, in the ears of the people that are on the wall.",
      "M": "Then Eliakim, Shebna, and Joah said to Rabshakeh, 'Please speak to us your servants in Aramaic, for we understand it. Do not speak Hebrew in the hearing of the people who are on the wall.'",
      "T": "Then Eliakim, Shebna, and Joah said to Rabshakeh, 'Please — speak to us in Aramaic. We understand it perfectly. Don't speak Hebrew where everyone on the wall can hear.'"
    },
    "12": {
      "L": "But Rabshakeh said, Hath my master sent me to thy master and to thee to speak these words? Hath he not sent me to the men that sit on the wall, that they may eat their own dung and drink their own piss with you?",
      "M": "But Rabshakeh answered, 'Did my master send me to speak these words only to your master and to you? Was he not also sending a message to the men on the wall — who will end up eating their own filth and drinking their own urine alongside you when the siege is over?'",
      "T": "But Rabshakeh answered: 'Did my master send this message only to your master and to you? Was it not sent just as much to the people sitting on the wall — who will end up eating their own filth and drinking their own urine when this is finished?'"
    },
    "13": {
      "L": "Then Rabshakeh stood, and cried with a loud voice in the Jews' language, and said, Hear ye the words of the great king, the king of Assyria.",
      "M": "Then Rabshakeh stood up and shouted in Hebrew at full volume: 'Hear the words of the great king, the king of Assyria!'",
      "T": "Then Rabshakeh stood up and bellowed in Hebrew at the top of his voice: 'Listen! Hear the words of the great king — the king of Assyria!'"
    },
    "14": {
      "L": "Thus saith the king, Let not Hezekiah deceive you; for he shall not be able to deliver you.",
      "M": "This is the king's word: Do not let Hezekiah mislead you — he is not able to deliver you.",
      "T": "'This is the king's message: Don't let Hezekiah deceive you. He cannot save you.'"
    },
    "15": {
      "L": "Neither let Hezekiah make you trust in the LORD, saying, The LORD will surely deliver us; this city shall not be delivered into the hand of the king of Assyria.",
      "M": "And do not let Hezekiah lead you to trust in the LORD by saying, 'The LORD will certainly deliver us — this city will not fall into the king of Assyria's hands.'",
      "T": "'And do not let Hezekiah talk you into trusting Yahweh by saying, \"Yahweh will definitely rescue us — this city will never fall to the king of Assyria.\"'"
    },
    "16": {
      "L": "Hearken not to Hezekiah; for thus saith the king of Assyria, Make an agreement with me by a present, and come out to me; and eat ye every one of his vine, and every one of his fig tree, and drink ye every one the waters of his own cistern;",
      "M": "Do not listen to Hezekiah. For this is what the king of Assyria says: Make terms with me and surrender — and every one of you will eat from his own vine and his own fig tree and drink from his own cistern,",
      "T": "'Stop listening to Hezekiah. Here is what the king of Assyria offers: Make peace with me and come out — every one of you will eat from your own vine and fig tree and drink from your own well,'"
    },
    "17": {
      "L": "Until I come and take you away to a land like your own land, a land of corn and wine, a land of bread and vineyards.",
      "M": "until I come and take you to a land just like your own — a land of grain and new wine, a land of bread and vineyards.",
      "T": "'— until I come and take you to a land just like this one: grain and wine, bread and vineyards.'"
    },
    "18": {
      "L": "Beware lest Hezekiah persuade you, saying, The LORD will deliver us. Hath any of the gods of the nations delivered his land out of the hand of the king of Assyria?",
      "M": "Watch out — do not let Hezekiah deceive you by saying, 'The LORD will deliver us.' Has any god of the nations ever delivered his land from the power of the king of Assyria?",
      "T": "'Be warned: don't let Hezekiah seduce you with talk about Yahweh rescuing you. Has any nation's god ever rescued his country from the king of Assyria?'"
    },
    "19": {
      "L": "Where are the gods of Hamath and of Arpad? where are the gods of Sepharvaim? and have they delivered Samaria out of my hand?",
      "M": "Where are the gods of Hamath and Arpad? Where are the gods of Sepharvaim? Did they deliver Samaria from my power?",
      "T": "'Where are the gods of Hamath and Arpad? Where are the gods of Sepharvaim? Did any of them rescue Samaria from me?'"
    },
    "20": {
      "L": "Who are they among all the gods of these countries, that have delivered their country out of my hand, that the LORD should deliver Jerusalem out of my hand?",
      "M": "Which of all the gods of these lands has ever delivered his land from my power? What makes you think the LORD will deliver Jerusalem from me?",
      "T": "'Name one — name one god of any of these nations who delivered his land from me. So why should Yahweh deliver Jerusalem?'"
    },
    "21": {
      "L": "But they held their peace, and answered him not a word; for the king's commandment was, saying, Answer him not.",
      "M": "But they remained silent and said nothing in reply, for the king had commanded, 'Do not answer him.'",
      "T": "They said nothing. Not a word. Because Hezekiah had given the order: Do not answer him."
    },
    "22": {
      "L": "Then came Eliakim, the son of Hilkiah, that was over the household, and Shebna the scribe, and Joah, the son of Asaph, the recorder, to Hezekiah with their clothes rent, and told him the words of Rabshakeh.",
      "M": "Then Eliakim son of Hilkiah, the palace administrator, Shebna the secretary, and Joah son of Asaph, the recorder, came to Hezekiah with their robes torn and reported to him what Rabshakeh had said.",
      "T": "Then Eliakim son of Hilkiah, the palace administrator, Shebna the secretary, and Joah son of Asaph, the recorder, went to Hezekiah with their robes torn and told him everything Rabshakeh had said."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 34–36 written.')

if __name__ == '__main__':
    main()
