"""
MKT Song of Solomon chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-songofsolomon-1-6.py

Translation decisions:

- H5315 (נֶפֶשׁ, nephesh): "him whom my soul loves" (1:7, 3:1–4). L: "soul" (embodied seeking
  self); M: "heart" or "I love with all my heart"; T: rendered as the whole searching person.
  Not the Greek immaterial soul — the whole living creature that reaches toward what it loves.

- H7307 (רוּחַ, ruach): 4:16 (north wind / south wind) — literal wind, not Spirit. L/M/T: "wind."
  No divine Spirit usage in chs 1–6.

- H3068 (יהוה, YHWH): does not appear in chs 1–6. (Appears as component of "shalhevetyah" in 8:6,
  which belongs to SOS-2.)

- H430 (אֱלֹהִים, elohim): does not appear in chs 1–6.

- H2617 (חֶסֶד, hesed): does not appear in chs 1–6.

- H1730 (דּוֹד, dod): "beloved" — the primary term for the male lover throughout. L/M/T: "beloved"
  consistently. In 5:16 the companion term H7453 (רֵעַ, rea') = "friend" is used alongside "beloved"
  — this final pairing is deliberate and significant; both rendered literally.

- H7650 (שָׁבַע, shava'): the adjure formula at 2:7 and 3:5 — L: "I charge you"; M: "I implore
  you"; T: contextual rendering that preserves the solemnity of the oath. The refrain closes
  narrative sections and guards love's proper timing.

- H2470 (חָלַה, chalah): "sick with love" (2:5, 5:8). L/M: "sick with love"; T: the fever of
  overwhelming longing.

- H668 (אַפִּרְיוֹן, 'apiryon): 3:9 — a rare loanword; probably a palanquin or litter for the
  royal wedding procession. L: "palanquin"; M: "royal litter"; T: "bridal throne."

- 6:12 textual note: "Before I was aware, my desire/soul set me among the chariots of my kinsman,
  a noble one" (nephesh + nadib). The MT is difficult; "Amminadib" as a proper name is a possible
  emendation followed by some translations (ESV mg., NASB mg.). This script retains the MT reading
  of nadib as "noble/prince" (= "my noble kinsman / a prince"). The verse is intentionally
  left somewhat open in T.

- H7759 (שׁוּלַמִּית, Shulamite): 6:13 — the only occurrence. Origin uncertain; possibly Shunem
  or a fem. form of shalom (wholeness). L/M: "Shulamite"; T: notes the possible echo of shalom.

- "Two camps" (מַחֲנַיִם, mahanaim, 6:13): echoes Jacob's place of the two-camp angelic encounter
  (Gen 32). L: "two camps"; M/T: "two companies."

- Poetic structure: Song of Solomon is entirely Hebrew poetry. The T tier uses line breaks in
  sustained lyric sections. L and M are prose renderings. Speaker transitions are not explicitly
  marked in L/M (following MT); T identifies the key voice shifts at section boundaries.

- Wasf form (body description, chs 4–5): The praise poems use stock ancient Near Eastern imagery.
  T contextualizes the metaphors (goats on a hillside for hair, fawn twins for breasts, etc.)
  so the images land as beauty rather than as confusion.

- The refrain "I am my beloved's and my beloved is mine" (2:16, 6:3) is the mutual-belonging
  declaration — the covenant core of the book. Rendered identically both times in L/M; T varies
  slightly to honor the different contexts (first occurrence = security; second = after trauma).
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


SONGOFSOLOMON = {
  "1": {
    "1": {
      "L": "The song of songs, which is Solomon's.",
      "M": "The Song of Songs, by Solomon.",
      "T": "The greatest of songs — Solomon's."
    },
    "2": {
      "L": "Let him kiss me with the kisses of his mouth! For your love is better than wine.",
      "M": "Let him kiss me with the kisses of his mouth! For your love is better than wine.",
      "T": "Kiss me — on the lips, with your lips.\nThere is no wine as intoxicating as your love.\n(The abrupt shift from 'let him' to 'your love' is in the Hebrew: the heart speaking aloud and then addressing him directly, unable to hold the third person.)"
    },
    "3": {
      "L": "Your anointing oils are fragrant; your name is oil poured out; therefore virgins love you.",
      "M": "Your anointing oils are fragrant; your name is like perfume poured out; no wonder the young women love you.",
      "T": "Your name itself is fragrance — not just the oils you wear, but the word that names you, released into the air like perfume uncorked. Of course they love you. How do you not love a man whose very name is oil poured out?"
    },
    "4": {
      "L": "Draw me after you; let us run. The king has brought me into his chambers. We will exult and rejoice in you; we will extol your love more than wine; rightly do they love you.",
      "M": "Take me with you — let us run! The king has brought me into his chambers. We will rejoice and exult in you; we will celebrate your love more than wine. Rightly do they love you!",
      "T": "Take me with you — I want to run where you run.\nHe led me into the innermost rooms.\nAnd the joy that follows is undeniable: your love is better than any wine,\nand everyone who loves you is right to do so."
    },
    "5": {
      "L": "I am black and beautiful, O daughters of Jerusalem, like the tents of Kedar, like the curtains of Solomon.",
      "M": "I am dark and lovely, O daughters of Jerusalem — like the tents of Kedar, like the draperies of Solomon.",
      "T": "Do not let my darkness deceive you.\nKedar's tents are black and they are beautiful;\nSolomon's curtains are dark and they are rich.\nI am dark and I am lovely.\nThe sun has worked on me; it has not made me less."
    },
    "6": {
      "L": "Do not look upon me because I am dark, because the sun has looked upon me. My mother's sons were angry with me; they made me keeper of the vineyards, but my own vineyard I have not kept.",
      "M": "Do not stare at me because I am dark — the sun has beaten down on me. My brothers were angry and made me keeper of the vineyards; my own vineyard I have not tended.",
      "T": "Stop looking at me that way — as though my darkness were a flaw.\nThe sun did this.\nMy brothers were angry and sent me out to work the family fields, and I went.\nBut while I kept their vines I could not keep myself —\ncould not tend the garden that is my own life, my own person."
    },
    "7": {
      "L": "Tell me, you whom my soul loves, where you pasture your flock, where you make it lie down at noon; for why should I be like one who veils herself beside the flocks of your companions?",
      "M": "Tell me, you whom I love with all my heart, where you pasture your flock and where you rest them at midday — why should I be left wandering among the flocks of your companions?",
      "T": "Tell me where you are —\nthe one my whole self reaches toward.\nWhere do you take your flock in the heat of the day?\nI don't want to find you by accident,\nwandering past the camps of other shepherds\nlike someone who doesn't know where she belongs."
    },
    "8": {
      "L": "If you do not know, O most beautiful among women, follow in the tracks of the flock, and pasture your young goats beside the shepherds' tents.",
      "M": "If you do not know, O most beautiful of women, follow the tracks of the flock and pasture your young goats near the shepherds' tents.",
      "T": "If you truly don't know — and perhaps you do know, and only wish to be invited —\nthen follow the flock's trail.\nGraze your goats beside the other shepherds' camps.\nYou will find me there, or you will find the way there."
    },
    "9": {
      "L": "I compare you, my love, to a mare among Pharaoh's chariots.",
      "M": "I liken you, my love, to a mare harnessed to Pharaoh's chariots.",
      "T": "You are like a mare running loose among Pharaoh's battle stallions —\nbeauty that undoes all discipline,\nthat causes chaos among the very instruments of power.\nThey are trained; you are free.\nThey are impressive; you are overwhelming."
    },
    "10": {
      "L": "Your cheeks are lovely with ornaments, your neck with strings of jewels.",
      "M": "Your cheeks are beautiful with jewelry, your neck adorned with strings of beads.",
      "T": "The jewelry frames what was already beautiful and makes it more so.\nYour cheeks in their ornamented setting, your neck in its strings of beads —\neach ornament is a setting for the face and throat themselves,\nwhich need no ornament."
    },
    "11": {
      "L": "We will make for you ornaments of gold with studs of silver.",
      "M": "We will make for you gold ornaments studded with silver.",
      "T": "Whatever adorns you now, we will make more —\ngold for you, studded with silver,\nworked for someone worth working for."
    },
    "12": {
      "L": "While the king was on his couch, my nard gave forth its fragrance.",
      "M": "While the king reclined at his table, my perfume spread its fragrance.",
      "T": "He was there, reclining, waiting —\nand my nard spoke before I could.\nThe perfume announced me, rose to him across the room.\nThere are conversations the body has before the person arrives."
    },
    "13": {
      "L": "My beloved is to me a sachet of myrrh that lies between my breasts.",
      "M": "My beloved is to me a sachet of myrrh resting between my breasts.",
      "T": "The way I carry him —\nlike a packet of myrrh worn against the heart,\ngiving off its fragrance all day and all night,\nwarming with body heat\nuntil the whole self smells of him."
    },
    "14": {
      "L": "My beloved is to me a cluster of henna blossoms in the vineyards of En-gedi.",
      "M": "My beloved is to me a cluster of henna blossoms from the vineyards of En-gedi.",
      "T": "He is that particular luxury —\nnot just henna flowers, but En-gedi henna,\nthe finest quality, growing in the oasis beside the salt sea.\nAn abundance of beauty in the middle of harsh terrain.\nThat is what he is to me."
    },
    "15": {
      "L": "Behold, you are beautiful, my love; behold, you are beautiful; your eyes are doves.",
      "M": "How beautiful you are, my love! How beautiful! Your eyes are like doves.",
      "T": "Let me look at you. Let me look again.\nDove eyes — soft, still, attentive,\nseeing without the predator's sharpness.\nYour beauty is not hard or aggressive;\nit is the kind that asks to be looked at slowly."
    },
    "16": {
      "L": "Behold, you are beautiful, my beloved, truly delightful. Our couch is green.",
      "M": "How handsome you are, my beloved, how truly delightful! Our bed is a bower of green.",
      "T": "And back to you: beautiful and truly pleasant to be near.\nOur bed is the green earth itself —\nthe forest floor is our bridal chamber,\nthe living world our canopy."
    },
    "17": {
      "L": "The beams of our house are cedar; our rafters are cypress.",
      "M": "The beams of our house are cedar; our rafters are cypress.",
      "T": "Cedar beams, cypress rafters — the finest wood, the fragrant wood.\nThe whole outdoors is a house built for us,\naromatic and strong."
    }
  },
  "2": {
    "1": {
      "L": "I am a rose of Sharon, a lily of the valleys.",
      "M": "I am a wildflower of Sharon, a lily of the valleys.",
      "T": "I am not the exotic cultivated bloom —\nI am the common flower of the open plain,\nthe lily that grows in low places.\nNot rare, not imported, not hothouse-kept.\nWildflower beauty."
    },
    "2": {
      "L": "As a lily among thorns, so is my love among the daughters.",
      "M": "Like a lily among thorns, so is my beloved among the young women.",
      "T": "Whatever she says about being a common wildflower —\nshe is the only one in the field that is not a thorn.\nA lily in a briar patch.\nEverything around her scratches; she does not."
    },
    "3": {
      "L": "As an apple tree among the trees of the forest, so is my beloved among the sons. With great delight I sat in his shadow, and his fruit was sweet to my taste.",
      "M": "Like an apple tree among the trees of the forest, so is my beloved among men. With great delight I sat in his shade, and his fruit was sweet to my taste.",
      "T": "He is not like the other men —\nthey are tall and useless like forest trees,\ngiving shade but no fruit.\nHe gives fruit.\nI rested under him and ate, and it was sweet.\nThere is both pleasure and nourishment in him,\nwhich is rarer than either alone."
    },
    "4": {
      "L": "He brought me to the house of wine, and his banner over me was love.",
      "M": "He brought me to the banquet hall, and his banner over me was love.",
      "T": "The house of wine, and above everything —\nabove all the occasion, all the gathering, all the feast's abundance —\na single banner: love.\nThat is what announces us.\nThat is what flies over whatever space we enter together."
    },
    "5": {
      "L": "Sustain me with raisin cakes; refresh me with apples, for I am sick with love.",
      "M": "Strengthen me with raisins; revive me with apples — for I am faint with love.",
      "T": "I need to be held up.\nThis love has made me weak the way a fever makes you weak —\nnot sick in the ruinous sense, but overwhelmed, undone.\nBring me something sweet and solid;\nI need to be restored to standing."
    },
    "6": {
      "L": "His left hand is under my head, and his right hand embraces me.",
      "M": "His left arm is under my head, and his right arm holds me close.",
      "T": "This is the rest:\nhis left hand beneath my head, his right arm around me.\nI am held from below and held from the side.\nThere is nowhere I am not supported."
    },
    "7": {
      "L": "I charge you, O daughters of Jerusalem, by the gazelles or by the does of the field: do not stir up or awaken love until it pleases.",
      "M": "I implore you, daughters of Jerusalem, by the gazelles and the does of the field: do not rouse or awaken love until it is ready.",
      "T": "I am asking you —\nby everything gentle and free in this world,\nby the gazelles and the does that cannot be hurried or commanded —\ndo not rush this.\nDo not try to force the moment that belongs to its own timing.\nLove has a readiness; wait for it.\nIt will wake when it wills."
    },
    "8": {
      "L": "The voice of my beloved! Behold, he comes, leaping over the mountains, bounding over the hills.",
      "M": "Listen — it is my beloved! Here he comes, leaping across the mountains, bounding over the hills.",
      "T": "I hear him before I see him.\nThen — there — bounding over the ridge\nlike nothing between us is an obstacle.\nMountains are not barriers when he is coming toward me.\nHe leaps them."
    },
    "9": {
      "L": "My beloved is like a gazelle or a young stag. Behold, he stands behind our wall, gazing through the windows, looking through the lattice.",
      "M": "My beloved is like a gazelle or a young stag. There he stands behind our wall, peering through the windows, looking through the lattice.",
      "T": "He has arrived but hasn't come in yet.\nLike a deer at the edge of the clearing —\npresent but still wild,\nstill lit with the energy of having run here.\nHe looks through the lattice.\nHis eyes find me before he comes to the door."
    },
    "10": {
      "L": "My beloved spoke and said to me: 'Arise, my love, my beautiful one, and come away.'",
      "M": "My beloved spoke and said to me: 'Get up, my love, my beautiful one, and come with me.'",
      "T": "He called me out.\nThose words — Arise. Come away.\nAs though staying inside were no longer possible,\nas though the world outside were wide and he was in it,\nand he wanted me there with him."
    },
    "11": {
      "L": "'For behold, the winter is past; the rain is over and gone.'",
      "M": "'The winter is past; the rains are over and gone.'",
      "T": "'The hard season is finished.\nThere is no reason left to stay indoors.'"
    },
    "12": {
      "L": "'The flowers appear on the earth; the time of singing birds has come, and the voice of the turtledove is heard in our land.'",
      "M": "'Flowers appear all across the land; the season of singing has arrived, and the voice of the turtledove is heard in our countryside.'",
      "T": "'Everything is in bloom.\nThe birds are singing again.\nThe turtledove — which was silent all winter — has found its voice.\nThe whole world is telling you it is time to come out.'"
    },
    "13": {
      "L": "'The fig tree forms its early figs, and the vines in blossom give forth fragrance. Arise, my love, my beautiful one, and come away.'",
      "M": "'The fig tree is ripening its early fruit, and the blossoming vines spread their fragrance. Get up, my love, my beautiful one, and come with me.'",
      "T": "'The fig tree is already setting fruit.\nThe vines are in flower and the whole vineyard smells of it.\nEverything is ready. Come out. Come away with me.'"
    },
    "14": {
      "L": "'O my dove, in the clefts of the rock, in the hiding place of the steep path, let me see your face, let me hear your voice, for your voice is sweet, and your face is lovely.'",
      "M": "'My dove, hidden in the clefts of the rock, in the sheltered crevice of the cliff — let me see your face and hear your voice. Your voice is sweet and your face is beautiful.'",
      "T": "'You tuck yourself away like a dove in the rock-face —\nvisible only in outline, half-hidden.\nCome out from that shelter.\nI want to see you fully, hear you clearly.\nYour voice is one of the best sounds in the world;\nyour face is one of the best sights.\nWhy are you hiding them from me?'"
    },
    "15": {
      "L": "'Catch us the foxes, the little foxes that spoil the vineyards, for our vineyards are in blossom.'",
      "M": "'Catch the little foxes that ruin the vineyards — our vineyards are in bloom.'",
      "T": "'There are small things that can undo everything:\nthe little foxes that get into vines just as they're flowering,\nnipping the blossoms before the fruit can form.\nCatch them.\nOur vineyard is at its most vulnerable and most beautiful moment —\nit must not be spoiled by small, sneaking things.'"
    },
    "16": {
      "L": "My beloved is mine, and I am his; he grazes among the lilies.",
      "M": "My beloved is mine and I am his; he grazes among the lilies.",
      "T": "Mine and his — the mutual belonging that is the core of what they have.\nHe is where the lilies are, in the sweet places,\nand I know where to find him."
    },
    "17": {
      "L": "Until the day breathes and the shadows flee, turn, my beloved, be like a gazelle or a young stag on the cleft mountains.",
      "M": "Until the day breaks and the shadows disappear, turn, my beloved — be like a gazelle or a young stag on the rugged mountains.",
      "T": "Stay while the night remains.\nWhen the day breathes its first breath and the shadows dissolve — only then go.\nBut until then: run these mountains the way you run everything,\nleaping and free,\nand come back to me."
    }
  },
  "3": {
    "1": {
      "L": "By night on my bed I sought him whom my soul loves; I sought him, but found him not.",
      "M": "At night on my bed I searched for the one I love with all my heart; I searched for him but did not find him.",
      "T": "The dark is the time when absence becomes acute.\nShe lies in the place where he should be and he is not there.\nShe reached for him and found nothing.\nThe seeking begins."
    },
    "2": {
      "L": "'I will rise now and go about the city, in the streets and in the broad places I will seek him whom my soul loves.' I sought him, but found him not.",
      "M": "'I will get up and go about the city — through the streets and squares I will search for the one I love.' I searched but did not find him.",
      "T": "Decision: she will not wait for morning.\nUp, into the city, through every street and square.\nThe whole city is smaller than her need to find him.\nBut the city is empty of him, or he is not where she looks."
    },
    "3": {
      "L": "The watchmen found me as they went about in the city: 'Have you seen him whom my soul loves?'",
      "M": "The city guards found me as they made their rounds: 'Have you seen the one I love?'",
      "T": "The watchmen on their rounds —\nthe men whose job is to see everything in the city at night —\nshe stops them and asks.\nShe is not embarrassed to ask, does not pretend to be out for another reason.\nHave you seen him? That is all she needs to know."
    },
    "4": {
      "L": "Scarcely had I passed them when I found him whom my soul loves. I held him and would not let him go, until I had brought him into my mother's house, and into the chamber of her who conceived me.",
      "M": "I had barely passed them when I found the one I love. I held him and would not let him go until I brought him into my mother's house, into the room of the one who gave birth to me.",
      "T": "Almost immediately past them — suddenly, not gradually — he was there.\nShe held on.\nShe was not going to lose him a second time;\nshe brought him home, into the house of her beginning,\nthe room where she first became herself.\nShe wanted him in the place where she was most fully known."
    },
    "5": {
      "L": "I charge you, O daughters of Jerusalem, by the gazelles or by the does of the field: do not stir up or awaken love until it pleases.",
      "M": "I implore you, daughters of Jerusalem, by the gazelles and the does of the field: do not rouse or awaken love until it is ready.",
      "T": "Again the refrain, after finding: still the same.\nEven in the finding, even in the holding, even in the bringing-home —\nthe gift is not yours to force.\nIt woke when it willed. It will again."
    },
    "6": {
      "L": "What is that coming up from the wilderness like columns of smoke, perfumed with myrrh and frankincense, with all the fragrant powders of a merchant?",
      "M": "Who is this coming up from the desert like a column of smoke, fragrant with myrrh and frankincense, with every kind of spice from the trader?",
      "T": "A procession out of the wilderness —\na plume of incense rising like a pillar,\ncarrying its fragrance ahead of itself:\nmyrrh, frankincense, every spice the merchants carry.\nSomething enormous and aromatic is coming up from the desert.\nWhat is it?"
    },
    "7": {
      "L": "Behold, it is the litter of Solomon! Around it are sixty mighty men, some of the mighty men of Israel.",
      "M": "It is the royal litter of Solomon, surrounded by sixty warriors — the finest men of Israel.",
      "T": "Solomon's palanquin — the bridal throne built for this day —\ncarried up from the desert,\nand around it sixty of Israel's best fighting men.\nThe marriage of the king arrives with an escort of warriors."
    },
    "8": {
      "L": "All of them holding swords, trained in war, each with his sword at his thigh, against alarms in the night.",
      "M": "All of them carry swords and are skilled in battle, each with his sword at his side, ready for danger in the night.",
      "T": "Armed men who know what they are doing — swords at the thigh, not ceremonial.\nThey are guarding something that must arrive safely.\nEven the most beautiful procession is protected by readiness for violence.\nThe night carries its dangers, and the king's beloved must pass through it unharmed."
    },
    "9": {
      "L": "King Solomon made himself a palanquin from the wood of Lebanon.",
      "M": "King Solomon made his royal litter from Lebanese cedar.",
      "T": "He built it himself — or had it built according to his own design.\nLebanon cedar, the finest, the fragrant.\nEven the vehicle that carries his love is made of the best material."
    },
    "10": {
      "L": "He made its posts of silver, its back of gold, its seat of purple; its interior was inlaid with love by the daughters of Jerusalem.",
      "M": "Its posts are silver, its back of gold, its seat purple — its interior lovingly lined by the daughters of Jerusalem.",
      "T": "Silver posts, gold back, purple cushion —\nand the inside, the part that surrounds the one who sits in it,\nwoven with love by the young women of the city.\nThey made it with their hands and with their hearts.\nThe most intimate part of the most magnificent thing\nis the part that was made with love."
    },
    "11": {
      "L": "Go out, O daughters of Zion, and see King Solomon, with the crown with which his mother crowned him on the day of his wedding, on the day of the gladness of his heart.",
      "M": "Come out, daughters of Zion, and gaze on King Solomon wearing the crown with which his mother crowned him — on his wedding day, the day his heart rejoiced.",
      "T": "Come and see this:\nthe king in the crown his mother placed on his head.\nShe crowned him for this day —\nnot for battle, not for politics, but for marriage.\nThe gladness of his heart is the occasion.\nA king who is glad is a different kind of king,\nwearing a different kind of crown."
    }
  },
  "4": {
    "1": {
      "L": "Behold, you are beautiful, my love! Behold, you are beautiful! Your eyes are doves behind your veil. Your hair is like a flock of goats streaming down from Mount Gilead.",
      "M": "How beautiful you are, my love! How beautiful! Your eyes behind your veil are doves. Your hair is like a flock of goats cascading down the slopes of Gilead.",
      "T": "Beautiful — and then again, beautiful: he cannot stop looking.\nDove eyes — the same soft, steady, undivided attention as before.\nAnd her hair: a dark moving stream of it,\nlike the goats you can see from a distance\nflowing down the mountain in the late afternoon light,\ndark against pale stone."
    },
    "2": {
      "L": "Your teeth are like a flock of shorn ewes that have come up from washing, all of which bear twins, and not one among them has lost its young.",
      "M": "Your teeth are like a flock of freshly washed sheep, each with its twin — not one is missing.",
      "T": "Every tooth in place — white, paired, complete.\nNewly-washed white sheep moving in perfect formation,\neach with her twin beside her, none missing a lamb.\nThe point is wholeness. Nothing is absent."
    },
    "3": {
      "L": "Your lips are like a scarlet thread, and your mouth is lovely. Your cheeks are like halves of a pomegranate behind your veil.",
      "M": "Your lips are like a scarlet thread, and your mouth is lovely. Your cheeks are like the halves of a pomegranate behind your veil.",
      "T": "Scarlet lips, a fine thread of color.\nAnd the cheeks: pomegranate-halves, the inner flush of the fruit —\nnot just the skin but its interior warmth, seeded and alive.\nThe veil makes everything more present, not less."
    },
    "4": {
      "L": "Your neck is like the tower of David, built for an arsenal; on it hang a thousand shields, all of them shields of warriors.",
      "M": "Your neck is like the tower of David, built in courses of stone; a thousand shields hang on it, all of them warriors' shields.",
      "T": "The tower of David is a military structure adorned with trophies of battle —\nshields hung on its walls as proof of what it has overcome.\nHer neck is like this: strong, held high,\ndecorated not with fragility but with the emblems of something formidable.\nShe is not merely decorative; she is imposing."
    },
    "5": {
      "L": "Your two breasts are like two fawns, twins of a gazelle, grazing among the lilies.",
      "M": "Your two breasts are like two young fawns, twins of a gazelle, feeding among the lilies.",
      "T": "Gentle, paired, unhurried, at ease —\ngrazing in the sweetest place.\nThe image is tenderness, not power.\nAfter the tower's strength, softness."
    },
    "6": {
      "L": "Until the day breathes and the shadows flee, I will go away to the mountain of myrrh and the hill of frankincense.",
      "M": "Until the day breaks and the shadows disappear, I will go to the mountain of myrrh and the hill of frankincense.",
      "T": "All night until the day comes —\nhe will be where the fragrance is, where she is.\nThe mountain of myrrh and the hill of frankincense are not geographical;\nthey are her."
    },
    "7": {
      "L": "You are altogether beautiful, my love; there is no flaw in you.",
      "M": "You are altogether beautiful, my love; there is no defect in you.",
      "T": "Everything. Not beautiful with reservations, not beautiful with a list of exceptions.\nThe whole of her, without a flaw.\nThis is the declaration that belongs to a particular kind of looking —\nthe looking that love enables."
    },
    "8": {
      "L": "Come with me from Lebanon, my bride; come with me from Lebanon. Set out from the summit of Amana, from the summit of Senir and Hermon, from the dens of lions, from the mountains of leopards.",
      "M": "Come with me from Lebanon, my bride; come from Lebanon. Come down from the peak of Amana, from the summit of Senir and Hermon, from the dens of lions, from the mountain haunts of leopards.",
      "T": "She is somewhere remote and wild —\nthe high peaks, the places where lions and leopards den.\nHe calls her down from the dangerous altitude.\nAmana, Senir, Hermon — named mountains, real danger.\nAnd yet he is not afraid of what surrounds her.\nHe is calling her toward him, not rescuing her from;\nshe is his bride, not his ward."
    },
    "9": {
      "L": "You have ravished my heart, my sister, my bride; you have ravished my heart with one of your eyes, with one jewel of your necklace.",
      "M": "You have stolen my heart, my sister, my bride; you have stolen my heart with a single glance, with one jewel of your necklace.",
      "T": "One look. One bead of your necklace.\nHe is not holding his heart in reserve —\nit is already hers, has been since the first glance.\n'My sister, my bride': both the intimacy of family and the covenant of marriage.\nYou are both to him. You are everything."
    },
    "10": {
      "L": "How beautiful is your love, my sister, my bride! How much better is your love than wine, and the fragrance of your anointing oils than any spice!",
      "M": "How beautiful your love is, my sister, my bride! How much better is your love than wine, and the fragrance of your perfumes than any spice!",
      "T": "The superlative runs in both directions now:\nher love is better than wine, her fragrance surpasses all spice.\nIn chapter 1 she said his love was better than wine;\nnow he says the same of hers.\nThe praise becomes mutual, an echo, a conversation of wonder."
    },
    "11": {
      "L": "Your lips drip nectar, my bride; honey and milk are under your tongue; the fragrance of your garments is like the fragrance of Lebanon.",
      "M": "Your lips, my bride, drip with nectar; honey and milk are under your tongue; the fragrance of your garments is like the fragrance of Lebanon.",
      "T": "Honeycomb and nectar at the lips;\nhoney and milk beneath the tongue —\nsweetness layered on sweetness,\nthe flavor of her words and her presence.\nAnd behind all of it the cedar-and-mountain smell of Lebanon,\nwhich is the smell of the highest and finest things."
    },
    "12": {
      "L": "A garden locked is my sister, my bride; a spring locked, a fountain sealed.",
      "M": "My sister, my bride, is a garden locked, a spring sealed, a fountain closed.",
      "T": "She is not available to everyone.\nThe garden has a lock; the spring has a seal.\nThis is not captivity — it is the guarding of something that belongs to one.\nA locked garden is not a diminished garden; it is a private one.\nIts beauty is reserved."
    },
    "13": {
      "L": "Your shoots are an orchard of pomegranates with all choicest fruits, henna with nard.",
      "M": "Your branches are an orchard of pomegranates with every choice fruit — henna and nard.",
      "T": "The locked garden has an abundance inside it:\npomegranates, the best fruits, henna and nard.\nWhat is enclosed is not empty or withholding — it is full.\nThe privacy makes the richness more intense, not less."
    },
    "14": {
      "L": "Nard and saffron, calamus and cinnamon, with all trees of frankincense, myrrh and aloes, with all choice spices.",
      "M": "Nard and saffron, calamus and cinnamon, with all trees of frankincense — myrrh and aloes, with all the finest spices.",
      "T": "The catalogue continues: every fragrant thing that can be named.\nThe garden that is her is a garden of incomparable richness.\nEvery spice the ancient world valued is present.\nThis is an inventory of wonder."
    },
    "15": {
      "L": "A garden fountain, a well of living water, and flowing streams from Lebanon.",
      "M": "A garden fountain, a well of fresh water, streams flowing from Lebanon.",
      "T": "And inside the locked garden: water.\nNot a cistern, not a pool — a fountain, a spring of living water,\nstreams coming from the highest mountains.\nShe is the source as well as the garden."
    },
    "16": {
      "L": "Awake, O north wind, and come, O south wind! Blow upon my garden, let its spices flow out. Let my beloved come to his garden, and eat its choicest fruits.",
      "M": "Awake, O north wind, and come, O south wind! Blow through my garden and carry its fragrance abroad. Let my beloved come to his garden and eat its best fruits.",
      "T": "She calls the winds to release her fragrance into the world —\nnorth wind to carry it far, south wind to warm it.\nAnd she speaks of the garden as his: come to your garden, eat from it.\nThe locked garden was locked for him;\nthe key was always his.\nWhat was guarded for one is freely given to that one."
    }
  },
  "5": {
    "1": {
      "L": "I came to my garden, my sister, my bride; I gathered my myrrh with my spice. I ate my honeycomb with my honey; I drank my wine with my milk. Eat, friends; drink, and be drunk with love.",
      "M": "I have come to my garden, my sister, my bride; I gathered my myrrh with my spice. I ate my honeycomb with my honey; I drank my wine with my milk. Eat, friends; drink deeply — be drunk with love!",
      "T": "He came. The garden opened to him;\nhe gathered everything it had to offer — myrrh, honey, wine, milk.\nAnd then, as though to the whole created world:\nCome. Eat. Drink your fill.\nLove is not diminished by sharing —\nits abundance invites participation."
    },
    "2": {
      "L": "I slept, but my heart was awake. The sound of my beloved knocking: 'Open to me, my sister, my love, my dove, my undefiled one, for my head is wet with dew, my locks with the drops of the night.'",
      "M": "I slept, but my heart was awake. A voice — my beloved knocking: 'Open to me, my sister, my darling, my dove, my perfect one. My head is drenched with dew, my hair with the drops of the night.'",
      "T": "Sleep on the surface, wakefulness underneath —\nthat is love's condition.\nShe is asleep but not entirely absent.\nAnd then his voice: four names for her in a single breath —\nsister, love, dove, perfect one.\nHe has been out in the night, his hair wet with dew.\nHe has been waiting. He is asking."
    },
    "3": {
      "L": "'I have put off my robe; how can I put it on? I have washed my feet; how can I soil them?'",
      "M": "'I have taken off my robe — how can I put it back on? I have washed my feet — how can I dirty them again?'",
      "T": "The moment of hesitation she will never forgive herself for.\nTwo reasonable excuses — both true, both insufficient.\nShe has undressed; she has washed her feet;\ngetting up means undoing all of that.\nThe excuses are real but they are excuses.\nShe is about to miss him."
    },
    "4": {
      "L": "My beloved put his hand to the bolt of the door, and my heart was stirred within me.",
      "M": "My beloved thrust his hand through the latch opening, and I felt a deep longing for him.",
      "T": "His hand through the latch-hole — reaching in, trying the lock.\nAnd at that gesture, something inside her moved.\nToo late, she understood what she was about to lose."
    },
    "5": {
      "L": "I arose to open to my beloved, and my hands dripped with myrrh, my fingers with liquid myrrh, upon the handles of the bolt.",
      "M": "I got up to open to my beloved, and my hands dripped with myrrh — my fingers with flowing myrrh — on the handles of the lock.",
      "T": "She rose at last.\nHer hands were already scented —\nthe myrrh she had been wearing, the fragrance of anticipation,\ndripping now from her fingers onto the bolt she was too slow to open.\nEven her tardiness was fragrant."
    },
    "6": {
      "L": "I opened to my beloved, but my beloved had turned and gone. My soul failed me when he spoke. I sought him, but found him not; I called him, but he gave me no answer.",
      "M": "I opened the door to my beloved, but my beloved had gone. I was beside myself when he left. I searched but did not find him; I called but he did not answer.",
      "T": "She opened the door. He was gone.\nThe same kind of absence as chapter 3, but worse —\nthis time she had heard him, almost reached him,\nand the hesitation cost her.\nHer soul failed — the word is from fainting,\nfrom the body's collapse under the weight of what happened.\nShe ran after him in the dark and called\nand he was not there."
    },
    "7": {
      "L": "The watchmen found me as they went about in the city; they struck me, they wounded me; the keepers of the walls took away my veil.",
      "M": "The city guards found me as they made their rounds; they beat me and wounded me; the watchmen on the walls stripped off my shawl.",
      "T": "This time the watchmen are not helpful — they are violent.\nShe is a woman alone in the city at night, and they treat her as such.\nThey strike her, wound her, take her veil.\nThe seeking that was poetry in chapter 3 has become something darker:\nshe has been hurt in the search.\nThe vulnerability of love is real."
    },
    "8": {
      "L": "I charge you, O daughters of Jerusalem: if you find my beloved, that you tell him I am sick with love.",
      "M": "I implore you, daughters of Jerusalem: if you find my beloved, tell him I am faint with love.",
      "T": "The adjuration returns, but changed.\nBefore it was a warning not to rush love;\nnow it is a message to be delivered: tell him.\nTell him that I am lovesick,\nthat what I am suffering is love,\nthat whatever he is making of his absence\nI am not cured of wanting him."
    },
    "9": {
      "L": "'What is your beloved more than another beloved, O most beautiful among women? What is your beloved more than another beloved, that you so charge us?'",
      "M": "'What makes your beloved better than any other lover, O most beautiful of women? What makes him so special that you beg us this way?'",
      "T": "The daughters press her: what makes him worth this?\nWorth the night-search, worth the wounds, worth the begging?\nThe question is not hostile — it is an invitation to describe him.\nTell us what you see in him.\nShe does."
    },
    "10": {
      "L": "My beloved is white and ruddy, chief among ten thousand.",
      "M": "My beloved is radiant and rugged, outstanding among ten thousand men.",
      "T": "Radiant — white with light — and ruddy with life.\nBoth together: the color of someone fully alive in two registers at once.\nAnd distinguished: whatever ten thousand men you gather, he stands out.\nThis is not bias; she is reporting what is simply visible."
    },
    "11": {
      "L": "His head is the finest gold; his locks are wavy, black as a raven.",
      "M": "His head is like purest gold; his hair is wavy and dark as a raven.",
      "T": "Gold head — the crown of him — and black hair in waves.\nGold and black: the most striking contrast.\nHis head is treasure."
    },
    "12": {
      "L": "His eyes are like doves beside streams of water, washed with milk, sitting fitly set.",
      "M": "His eyes are like doves beside streams of water — bathed in milk, perfectly set.",
      "T": "Her eyes were doves; now his are doves too.\nBut his are also jewels — bathed in milk, which is to say lustrous and clean,\nset beside a pool, which is to say perfectly placed.\nThe dove quality they share: the soft, attentive, undivided gaze."
    },
    "13": {
      "L": "His cheeks are like beds of spices, mounds of sweet-smelling herbs. His lips are lilies, dripping with liquid myrrh.",
      "M": "His cheeks are like beds of spice, banks of sweet herbs. His lips are lilies dripping with flowing myrrh.",
      "T": "Fragrance again — his very face is a garden.\nSpice-beds at the cheeks; lily-lips that release myrrh with every word.\nShe is describing not just his appearance\nbut his presence, the sensory experience of being near him."
    },
    "14": {
      "L": "His hands are rods of gold set with beryl. His body is polished ivory, overlaid with lapis lazuli.",
      "M": "His hands are gold cylinders set with jewels. His torso is carved ivory overlaid with sapphires.",
      "T": "Gold arms set with gemstones; ivory body inlaid with blue lapis.\nShe is describing a living treasure —\nnot cold like metal and stone, but alive, warm, moving.\nThe preciousness of him is in his actual substance, not just his ornament."
    },
    "15": {
      "L": "His legs are pillars of alabaster, set on bases of gold. His appearance is like Lebanon, noble as the cedars.",
      "M": "His legs are like columns of alabaster, set in sockets of gold. His form is like Lebanon — magnificent as the cedars.",
      "T": "The whole of him: alabaster legs on gold sockets —\nstrong, white, set on something that will not shift.\nAnd his overall impression: Lebanon itself,\nwhich means height, grandeur, fragrance, permanence.\nHe looks the way Lebanon looks —\nlike something that has been there a long time\nand will be there long after you are gone."
    },
    "16": {
      "L": "His mouth is most sweet, and he is altogether lovely. This is my beloved, and this is my friend, O daughters of Jerusalem.",
      "M": "His mouth is sweetness itself; he is altogether desirable. This is my beloved and this is my friend, O daughters of Jerusalem.",
      "T": "The last word of the description,\nand the word she saves for last is not 'husband' or 'king' but 'friend.'\nEverything she has said — the gold, the cedar, the jewels, the lilies —\nand at the end: this is my friend.\nThis is my beloved.\nAnd they are the same man."
    }
  },
  "6": {
    "1": {
      "L": "'Where has your beloved gone, O most beautiful among women? Where has your beloved turned? Tell us, that we may seek him with you.'",
      "M": "'Where has your beloved gone, O most beautiful of women? Which way did he go? We will search with you.'",
      "T": "The daughters of Jerusalem have heard the description.\nThey understand now — they see why she searches.\nThey are offering to help.\nThis is what an honest account of love produces:\nit draws others in, makes them want to find what she has found."
    },
    "2": {
      "L": "My beloved has gone down to his garden, to the beds of spices, to graze in the gardens and to gather lilies.",
      "M": "My beloved has gone to his garden, to the beds of spices, to graze in the gardens and gather lilies.",
      "T": "She knew all along. Or she knew at the moment of speaking.\nHe is where he always is:\nin the garden, among the fragrant things, gathering what grows there.\nShe did not need to search the city.\nShe knew where he would be."
    },
    "3": {
      "L": "I am my beloved's and my beloved is mine; he grazes among the lilies.",
      "M": "I am my beloved's and he is mine; he grazes among the lilies.",
      "T": "The covenant declaration, returned to after the worst night.\nNo matter what it brought — the absence, the wounds, the searching —\nthis has not changed.\nShe is his and he is hers.\nHe is where the sweetest things grow, and she knows it."
    },
    "4": {
      "L": "You are beautiful as Tirzah, my love, lovely as Jerusalem, awesome as an army with banners.",
      "M": "You are beautiful as Tirzah, my love, lovely as Jerusalem, awe-inspiring as an army under banners.",
      "T": "Tirzah the northern capital, Jerusalem the southern —\ntwo cities of incomparable beauty, the poles of the whole land.\nAnd between them, his beloved.\nBut then the shift: awesome as an army under banners.\nNot just beautiful but formidable.\nShe does not merely attract; she overwhelms."
    },
    "5": {
      "L": "Turn away your eyes from me, for they overcome me. Your hair is like a flock of goats leaping down from Gilead.",
      "M": "Look away — your eyes overwhelm me! Your hair flows like a flock of goats down from Gilead.",
      "T": "He told her dove eyes couldn't wound; now they are too much to bear.\nHe asks her to look away.\nThis is the power she has over him:\na single glance undoes his composure.\nAnd then, as though recovering,\nhe returns to the catalogue — the waterfall of dark hair down the mountain."
    },
    "6": {
      "L": "Your teeth are like a flock of ewes that have come up from the washing; all of which bear twins, and not one among them has lost its young.",
      "M": "Your teeth are like a flock of sheep that have just been washed — every one bearing twins, none having lost her young.",
      "T": "The same praise as chapter 4:2 — returned to now.\nWhen a man is overwhelmed enough to look away from someone's eyes,\nhe steadies himself by returning to what he knows:\nthe familiar beauty of her, beginning at the beginning again."
    },
    "7": {
      "L": "Your cheeks are like halves of a pomegranate behind your veil.",
      "M": "Your cheeks are like pomegranate halves behind your veil.",
      "T": "And the pomegranate-cheeks again, as in 4:3.\nRepeated not because he has run out of words\nbut because these images are the settled vocabulary of his love for her.\nThe veil remains — some things stay private\neven in the most intimate description."
    },
    "8": {
      "L": "There are sixty queens and eighty concubines, and virgins without number.",
      "M": "There may be sixty queens and eighty concubines, and maidens beyond counting.",
      "T": "Every woman of the court and the household —\nqueens, concubines, all the unmarried — catalogued and numbered.\nThe numbers are large.\nAgainst them all, he is about to say something."
    },
    "9": {
      "L": "My dove, my perfect one, is the only one, the only one of her mother, the choice one of her who bore her. The daughters saw her and called her blessed; the queens and concubines also praised her.",
      "M": "But my dove, my flawless one, is unique — her mother's only daughter, treasured by the one who gave birth to her. The young women saw her and praised her; the queens and concubines celebrated her.",
      "T": "Against all the many: one.\nShe is the only one —\nnot numerically an only child, necessarily,\nbut the singular one, the particular unrepeatable person who is her.\nAnd even the queens and concubines,\nwho might have reason for rivalry, called her blessed.\nYou cannot look at her and not praise her."
    },
    "10": {
      "L": "'Who is this who looks down like the dawn, beautiful as the moon, bright as the sun, awesome as an army with banners?'",
      "M": "'Who is this who appears like the dawn, beautiful as the moon, bright as the sun, awe-inspiring as an army with banners?'",
      "T": "Dawn, moon, sun —\nthree progressions of light across the sky,\nfrom the first hint to the full blaze of day.\nAnd then again the army.\nThis is what the daughters and queens asked when they saw her.\nWho is this who makes the whole sky relevant?"
    },
    "11": {
      "L": "I went down to the nut orchard to see the blossoms of the valley, to see whether the vine had budded, whether the pomegranates were in bloom.",
      "M": "I went down to the grove of walnut trees to look at the new growth in the valley, to see whether the vines had budded or the pomegranates bloomed.",
      "T": "A moment of ordinary searching —\nshe went to the orchard, checking whether the season had arrived,\nwhether things were budding and blooming.\nAnd then something happened that she didn't anticipate."
    },
    "12": {
      "L": "Before I was aware, my desire set me among the chariots of my kinsman, a prince.",
      "M": "Before I realized it, my longing had placed me beside my noble kinsman's chariot.",
      "T": "Before she knew what was happening, desire moved her —\ncarried her somewhere she hadn't meant to go,\ninto the royal chariot, beside the one who wields both speed and power.\nShe didn't plan it; love moved her past the moment of decision.\n(6:12 is the most difficult verse in the book; the MT reads 'my soul/desire set me among the chariots of my noble kinsman/a prince' — the T rendering holds the ambiguity.)"
    },
    "13": {
      "L": "Return, return, O Shulamite; return, return, that we may look upon you. 'Why would you look upon the Shulamite, as upon the dance between two camps?'",
      "M": "Come back, come back, O Shulamite; come back, come back, so we can look at you! 'Why do you gaze on the Shulamite as at the dance between two companies?'",
      "T": "The voices call her back —\nshe has gone somewhere, perhaps fled from the attention,\nperhaps from the overwhelming moment of the chariot.\nCome back. Let us see you.\nAnd she — or he — answers: what would you see?\nThe Shulamite as she dances between two camps —\ntwo worlds, the one she came from and the one she has entered.\n('Shulamite' — שׁוּלַמִּית — appears only here; may echo shalom, wholeness.\n'Two camps' — מַחֲנַיִם, Mahanaim — recalls Jacob's place of meeting at Gen 32.\nShe stands at the intersection of two realities. That is what you are looking at.)"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'songofsolomon')
        merge_tier(existing, SONGOFSOLOMON, tier_key)
        save(tier_dir, 'songofsolomon', existing)
    print('Song of Solomon 1–6 written.')

if __name__ == '__main__':
    main()
