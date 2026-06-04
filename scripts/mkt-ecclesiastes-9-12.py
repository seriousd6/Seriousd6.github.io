"""
MKT Ecclesiastes chapters 9–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ecclesiastes-9-12.py

Translation decisions (continuing from mkt-ecclesiastes-4-6.py):

- H1892 (הֶבֶל hebel): "vapor" in L and M throughout, consistent with chs 4–6.
  T varies contextually: 9:9 "vapor-thin days"; 11:8,10 "vapor"; 12:8 the climactic
  conclusion — "Breath of breaths" matching the superlative form, all three tiers use
  "vapor/breath" language. 12:8 uses "vapor of vapors" in L/M per the established set-phrase.

- H4745 (מִקְרֶה miqreh): "one event" / "one fate" — the same end befalls all.
  9:2,3: L="one event"; M="one fate"; T="the same end." Qohelet's term for the leveling
  of all human distinctions by death.

- H7307 (רוּחַ ruach) — three distinct uses in chs 9–12:
  * 10:4: "spirit of the ruler" = anger/temper of a ruler. L="spirit"; M="anger"; T="fury."
  * 11:4: "the wind" — physical phenomenon; L/M/T = "wind."
  * 11:5: "way of the wind/spirit" — Qohelet intentionally ambiguous: the wind's unknown
    path AND the breath/life-spirit entering the fetal bones. L="of the wind"; M="of the
    wind" (note kept in T); T surfaces both readings explicitly.
  * 12:7: "the spirit shall return to God who gave it" — life-breath returning to its source.
    L="the spirit"; M="the spirit"; T="the Spirit" (capital — this is the divine breath of
    Gen 2:7 being returned to the Giver; the only theological capital in these chapters).

- H7585 (שְׁאוֹל Sheol): 9:10 only occurrence. L="Sheol" (transliterated; English lacks
  a precise equivalent); M="the grave"; T="the world of the dead."

- H1254 (בָּרָא bara' / בֹּורְאֶיךָ "thy Creator"): 12:1. The form is plural of majesty.
  L="thy Creator"; M="your Creator"; T="the God who made you."

- H430 (אֱלֹהִים Elohim): "God" consistently. H3068 (יהוה) does not appear in Ecclesiastes.

- H5999 (עָמָל 'amal): "toil" in L; "toil" or "labor" in M/T — consistent with chs 4–6.

- H5315 (נֶפֶשׁ nephesh): Not prominent in chs 9–12 as an independent term.

- The great poem of old age (12:1–7): Qohelet uses extended allegory — body parts described
  through images of a household shutting down. L renders the images literally; M clarifies
  the allegorical referents parenthetically or contextually; T fully unpacks the allegory so
  the reader feels the weight of physical decline. The sequence: arms tremble (keepers of the
  house), legs bow (strong men), teeth diminish (grinders), eyes dim (windows), outer doors
  shut, ears fail, waking to bird-sounds (light sleep of the aged), loss of singing voices,
  fear of heights, almond tree white with blossom (white hair), grasshopper dragging (the
  slow gait of age), desire failing — all climaxing in 12:6 with the snapping of life's
  silver cord and the shattered vessels at the well.

- OT echoes: 9:11 echoes Prov 21:31 (the horse is prepared for battle but victory is the
  LORD's) — T notes the divine irony. 12:7 echoes Gen 2:7 (God breathed into man the
  breath of life). 12:13–14 stands as the theological summary of the entire Wisdom tradition.

- Aspect: Qohelet's habitual observations use the timeless Hebrew imperfect → English present.
  Narrative past (waw-consecutive) → English simple past.

- 12:11 "one Shepherd": the ambiguity is intentional — the final editor(s) may intend God
  as the ultimate source of wisdom literature. T makes this explicit.
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


ECCLESIASTES = {
  "9": {
    "1": {
      "L": "For all this I laid to heart, even to declare all of it: that the righteous and the wise and their works are in the hand of God; yet no man knows whether it is love or hatred — all lies before him.",
      "M": "I laid all this to heart and considered it carefully: that the righteous and the wise and all they do are in God's hands. Yet no one knows whether love or hatred awaits them — everything lies ahead, unknown.",
      "T": "I turned all of this over carefully in my mind: the wise, the righteous, everything they do — it is all in God's hands. But no one can tell whether what lies ahead holds love or hatred. Everything is concealed."
    },
    "2": {
      "L": "All things come alike to all — there is one event to the righteous and to the wicked, to the good and to the clean and to the unclean, to him that sacrificeth and to him that sacrificeth not; as is the good man, so is the sinner; he that sweareth as he that feareth an oath.",
      "M": "The same fate comes to everyone: to the righteous and to the wicked, to the good and the clean and the unclean, to those who sacrifice and those who do not. The good person and the sinner share the same end; the person who swears and the one who avoids oaths alike.",
      "T": "One fate falls on everyone without distinction: the righteous and the wicked, the ceremonially clean and the unclean, the devoted worshiper and the one who never bothers. Good and sinful, oath-taker and oath-avoider — they all end the same way."
    },
    "3": {
      "L": "This is an evil in all that is done under the sun: that one event comes to all. Also the heart of the sons of men is full of evil, and madness is in their hearts while they live; and after that — they go to the dead.",
      "M": "This is the evil in everything done under the sun: one fate comes to all. Moreover, people's hearts are full of evil, and madness fills them throughout their lives; and after that, they go to the dead.",
      "T": "Here is the great evil lurking beneath everything done in this world: we all share the same end. And what do people do with the life they have? Fill it with evil and madness — right up until the moment they join the dead."
    },
    "4": {
      "L": "For to him that is joined to all the living there is hope; for a living dog is better than a dead lion.",
      "M": "Anyone still among the living has hope, for a living dog is better off than a dead lion.",
      "T": "As long as you are alive, there is hope. Even a living dog outranks a dead lion."
    },
    "5": {
      "L": "For the living know that they shall die; but the dead know not any thing, and they have no more a reward; for the memory of them is forgotten.",
      "M": "The living know that they will die, but the dead know nothing. They have no further reward, for their memory is forgotten.",
      "T": "The living know at least this: that they will die. The dead know nothing at all — no reward awaits them, and all memory of them fades."
    },
    "6": {
      "L": "Their love also and their hatred and their envy have now perished, and they have no more a portion for ever in any thing that is done under the sun.",
      "M": "Their love, their hatred, and their envy have all vanished. They have no share any longer in anything that happens under the sun.",
      "T": "Everything that once drove them — love, hatred, envy — all of it is gone. The dead have no part in anything that happens in the world of the living."
    },
    "7": {
      "L": "Go, eat thy bread with joy, and drink thy wine with a merry heart; for God now accepteth thy works.",
      "M": "Go, eat your food with gladness and drink your wine with a cheerful heart, for God has already approved what you do.",
      "T": "So go — eat your food with genuine pleasure, drink your wine with a glad heart. God has already given his approval to what you do."
    },
    "8": {
      "L": "Let thy garments be always white; and let thy head lack no ointment.",
      "M": "Let your clothing always be fresh and white, and let your head not lack for oil.",
      "T": "Keep yourself well-dressed and fragrant. Take care of yourself while you are alive to do so."
    },
    "9": {
      "L": "Live joyfully with the wife whom thou lovest all the days of the life of thy vapor, which he hath given thee under the sun, all the days of thy vapor; for that is thy portion in this life, and in thy labour which thou takest under the sun.",
      "M": "Enjoy life with the wife you love throughout all your fleeting days under the sun — all the days of your vapor — for that is your portion in this life and in the toil you carry on under the sun.",
      "T": "Make the most of life with the woman you love — through all these brief, vapor-thin days God has given you under the sun. That is your portion: this life, this companion, this work. Embrace all of it."
    },
    "10": {
      "L": "Whatsoever thy hand findeth to do, do it with thy might; for there is no work, nor device, nor knowledge, nor wisdom, in Sheol, whither thou goest.",
      "M": "Whatever your hand finds to do, do it with all your strength. There is no work, no planning, no knowledge, no wisdom in the grave — where you are going.",
      "T": "Whatever you can do, do it now with everything you have. In the world of the dead there is no work, no scheme, no understanding, no wisdom. That is where you are headed — so act while you still can."
    },
    "11": {
      "L": "I returned, and I saw under the sun that the race is not to the swift, nor the battle to the strong, neither yet bread to the wise, nor yet riches to men of understanding, nor yet favour to men of skill; but time and chance happeneth to them all.",
      "M": "Again I observed that under the sun, the race is not won by the swift, nor the battle by the strong, nor bread by the wise, nor riches by the intelligent, nor favor by the knowledgeable — rather, time and chance happen to them all.",
      "T": "I looked again: in this world, speed does not win the race, strength does not win the battle, wisdom does not put bread on the table, intelligence does not produce wealth, and expertise does not earn recognition. Time and chance — that is what governs all of it."
    },
    "12": {
      "L": "For also man knoweth not his time: as the fishes that are taken in an evil net, and as the birds that are caught in the snare; so are the sons of men snared in an evil time, when it falleth suddenly upon them.",
      "M": "No one knows when their hour will come. As fish are caught in a cruel net and birds are snared, so people are trapped at some evil moment when it suddenly falls upon them.",
      "T": "No one knows when their moment will come. Fish get caught in a cruel net; birds fall into a snare. So it is for people — seized without warning when the evil moment arrives."
    },
    "13": {
      "L": "This wisdom have I seen also under the sun, and it seemed great unto me.",
      "M": "I also observed this example of wisdom under the sun, and it struck me as remarkable.",
      "T": "There is one more thing I have seen in this world — a striking piece of wisdom."
    },
    "14": {
      "L": "There was a little city, and few men within it; and there came a great king against it, and besieged it, and built great bulwarks against it.",
      "M": "There was a small city with few people in it, and a powerful king came against it, besieged it, and built great siege works around it.",
      "T": "A small city, thinly populated. A great and powerful king came against it, encircled it, and erected massive siege works."
    },
    "15": {
      "L": "Now there was found in it a poor wise man, and he by his wisdom delivered the city; yet no man remembered that same poor man.",
      "M": "But a poor wise man was found in the city, and by his wisdom he saved it. Yet no one remembered that poor man afterward.",
      "T": "And there was one man in it — poor, but wise. He saved the city by his wisdom alone. Once it was over, no one gave him another thought."
    },
    "16": {
      "L": "Then said I, Wisdom is better than strength: but the poor man's wisdom is despised, and his words are not heard.",
      "M": "Then I concluded: wisdom is better than strength. But the poor man's wisdom is despised and his words go unheard.",
      "T": "And so I said: wisdom is more powerful than brute force. But no one respects the wisdom of a poor man — his words are not even listened to."
    },
    "17": {
      "L": "The words of wise men heard in quiet are better than the cry of him that ruleth among fools.",
      "M": "Words spoken quietly by the wise carry more weight than the shouting of a ruler among fools.",
      "T": "A whispered word from a wise person does more good than all the shouting of a fool in power."
    },
    "18": {
      "L": "Wisdom is better than weapons of war; but one sinner destroyeth much good.",
      "M": "Wisdom is better than weapons of war, but one fool can undo a great deal of good.",
      "T": "Wisdom outperforms any weapon — but one reckless person can destroy what wisdom took years to build."
    }
  },
  "10": {
    "1": {
      "L": "Dead flies cause the ointment of the perfumer to stink and ferment; so doth a little folly outweigh wisdom and honour.",
      "M": "Dead flies cause the perfumer's ointment to give off a foul smell. In the same way, a little folly outweighs wisdom and honor.",
      "T": "A few dead flies can ruin an entire jar of fine perfume. In the same way, just a touch of foolishness can outweigh all the wisdom and reputation a person has built."
    },
    "2": {
      "L": "A wise man's heart is at his right hand; but a fool's heart at his left.",
      "M": "The heart of the wise leads them to the right, but the heart of the fool to the left.",
      "T": "A wise person's instincts lead them in the right direction; a fool's instincts lead them the wrong way."
    },
    "3": {
      "L": "Yea also, when he that is a fool walketh by the way, his wisdom faileth him; and he saith to every one that he is a fool.",
      "M": "Even while walking along the road, the fool's judgment fails him and he shows everyone what a fool he is.",
      "T": "A fool cannot even walk down the street without advertising his foolishness to everyone he meets."
    },
    "4": {
      "L": "If the spirit of the ruler rise up against thee, leave not thy place; for calmness pacifieth great offences.",
      "M": "If the ruler's anger flares against you, do not abandon your post — composure can defuse even serious offenses.",
      "T": "If those in power turn against you, don't panic and run. Staying calm is what defuses the situation — even when the offense feels unforgivable."
    },
    "5": {
      "L": "There is an evil which I have seen under the sun, as an error which proceedeth from the ruler:",
      "M": "There is an evil I have observed under the sun — a kind of blunder that proceeds from those in power:",
      "T": "I have seen a particular evil in this world — a miscalculation that originates with those who hold authority:"
    },
    "6": {
      "L": "Folly is set in great dignity, and the rich sit in low place.",
      "M": "Fools are appointed to high positions while the capable sit in lowly ones.",
      "T": "The incompetent are elevated to positions of great authority while people of genuine ability are left in obscurity."
    },
    "7": {
      "L": "I have seen servants upon horses, and princes walking as servants upon the earth.",
      "M": "I have seen servants riding on horseback while princes walk on foot like servants.",
      "T": "I have watched servants riding horses while noblemen walk in the dust. Everything is inverted."
    },
    "8": {
      "L": "He that diggeth a pit shall fall into it; and whoso breaketh an hedge, a serpent shall bite him.",
      "M": "Whoever digs a pit may fall into it, and whoever breaks through a wall may be bitten by a snake.",
      "T": "The man who digs a trap may fall into it himself. Knock down a wall and you might find a snake waiting on the other side."
    },
    "9": {
      "L": "Whoso removeth stones shall be hurt therewith; and he that cleaveth wood shall be endangered thereby.",
      "M": "Whoever quarries stones may be hurt by them, and whoever splits wood is in danger from it.",
      "T": "Work with stone and the stone may cut you. Split timber and it may come back at you."
    },
    "10": {
      "L": "If the iron be blunt, and he do not whet the edge, then must he put to more strength; but wisdom is profitable to direct.",
      "M": "If an axe is dull and you do not sharpen it, you will need to use much more force — but wisdom makes the work succeed.",
      "T": "Work with a dull blade and you exhaust yourself. Sharpen it first. Wisdom is simply knowing how to make the work work."
    },
    "11": {
      "L": "Surely the serpent will bite without enchantment; and a babbler is no better.",
      "M": "If a snake bites before being charmed, the charmer has gained nothing — and it is no different with one who cannot hold his tongue.",
      "T": "A snake that strikes before it can be charmed does the charmer no good. Some dangers move faster than wisdom can intervene — and a loose tongue is one of them."
    },
    "12": {
      "L": "The words of a wise man's mouth are gracious; but the lips of a fool will swallow up himself.",
      "M": "A wise person's words earn goodwill, but a fool's words devour him.",
      "T": "The wise person's words draw people toward him. A fool's words eat him alive."
    },
    "13": {
      "L": "The beginning of the words of his mouth is foolishness; and the end of his talk is mischievous madness.",
      "M": "A fool begins by talking foolishly and ends in wicked madness.",
      "T": "A fool opens his mouth with nonsense and closes it with dangerous lunacy."
    },
    "14": {
      "L": "A fool also is full of words: a man cannot tell what shall be; and what shall be after him, who can tell him?",
      "M": "A fool multiplies words, yet no one can tell what will happen, and who can say what comes after?",
      "T": "A fool just keeps talking — and talking. But no one can tell what the future holds, and there is no one who can tell the fool what comes next."
    },
    "15": {
      "L": "The labour of the foolish wearieth every one of them, because he knoweth not how to go to the city.",
      "M": "The labor of fools exhausts everyone around them — they cannot even find their way to the city.",
      "T": "A fool's efforts wear out everyone who depends on them. He couldn't find the main road into town."
    },
    "16": {
      "L": "Woe to thee, O land, when thy king is a child, and thy princes eat in the morning!",
      "M": "Woe to the land whose king is a boy and whose rulers carouse in the morning.",
      "T": "God help the country whose king is immature and whose officials are drinking by breakfast."
    },
    "17": {
      "L": "Blessed art thou, O land, when thy king is the son of nobles, and thy princes eat in due season, for strength, and not for drunkenness!",
      "M": "Blessed is the land whose king is of noble character and whose princes eat at the proper time — for strength and not for excess.",
      "T": "But blessed is the country whose king comes from a distinguished line and whose leaders eat when it is time to eat — for vigor, not for indulgence."
    },
    "18": {
      "L": "By much slothfulness the building decayeth; and through idleness of the hands the house droppeth through.",
      "M": "Through great laziness the rafters sag, and through idle hands the house leaks.",
      "T": "Neglect the roof and it sinks. Let your hands go idle and the rain comes through. What is true of houses is true of kingdoms."
    },
    "19": {
      "L": "A feast is made for laughter, and wine maketh merry; but money answereth all things.",
      "M": "A feast is prepared for enjoyment and wine gladdens life, but money provides for everything.",
      "T": "Food is for celebration; wine is for joy. But in this world, money is what makes everything possible."
    },
    "20": {
      "L": "Curse not the king, no not in thy thought; and curse not the rich in thy bedchamber: for a bird of the air shall carry the voice, and that which hath wings shall tell the matter.",
      "M": "Do not curse the king, even in your thoughts; do not curse the wealthy even in your bedroom — for a bird may carry your words, and a winged creature may report what you said.",
      "T": "Never speak against those in power, not even in your private thoughts. Never speak against the wealthy, not even behind closed doors. Walls have ears. Some winged thing will carry the word. Word always gets out."
    }
  },
  "11": {
    "1": {
      "L": "Cast thy bread upon the waters: for thou shalt find it after many days.",
      "M": "Cast your bread upon the waters, for you will find it again after many days.",
      "T": "Give freely, even when the return seems unlikely. Cast your bread on the waters — after many days, it comes back to you."
    },
    "2": {
      "L": "Give a portion to seven, and also to eight; for thou knowest not what evil shall be upon the earth.",
      "M": "Give a share to seven, even to eight, for you do not know what calamity may come upon the earth.",
      "T": "Be generous to many — seven, even eight. You don't know what disaster may be coming, so spread your generosity wide."
    },
    "3": {
      "L": "If the clouds be full of rain, they empty themselves upon the earth: and if the tree fall toward the south, or toward the north, in the place where the tree falleth, there it shall be.",
      "M": "If the clouds are filled with rain, they pour it on the earth; if a tree falls to the south or the north, in the place where it falls, there it will lie.",
      "T": "Clouds full of rain eventually pour out — that is simply what they do. A tree that falls to the south or north lies where it has fallen. Some things follow their own laws regardless of your intentions."
    },
    "4": {
      "L": "He that observeth the wind shall not sow; and he that regardeth the clouds shall not reap.",
      "M": "Whoever watches the wind will never sow; whoever watches the clouds will never reap.",
      "T": "Wait for perfect conditions and you will never plant anything. Wait for perfect weather and the harvest will never come. Act despite uncertainty."
    },
    "5": {
      "L": "As thou knowest not what is the way of the wind, nor how the bones do grow in the womb of her that is with child: even so thou knowest not the works of God who maketh all.",
      "M": "Just as you cannot know the path of the wind or how bones form in the womb of a pregnant woman, so you cannot know the work of God who makes everything.",
      "T": "You cannot trace the path of the wind — or know whether it is also the breath of life entering the unborn. You cannot see the moment bones form in the womb. In the same way, you cannot see what God is doing as he works through all things."
    },
    "6": {
      "L": "In the morning sow thy seed, and in the evening withhold not thine hand: for thou knowest not whether shall prosper, either this or that, or whether they both shall be alike good.",
      "M": "Sow your seed in the morning, and in the evening do not let your hand rest — for you do not know which effort will succeed, this or that, or whether both will turn out well.",
      "T": "Start at dawn; don't stop at dusk. Keep sowing — you don't know which seeds will take, this batch or that, or whether all of them will flourish. Work without knowing the outcome."
    },
    "7": {
      "L": "Truly the light is sweet, and a pleasant thing it is for the eyes to behold the sun.",
      "M": "Light is sweet, and it is good for the eyes to see the sun.",
      "T": "Light itself is a pleasure. Simply seeing the sun rise is a gift."
    },
    "8": {
      "L": "But if a man live many years, and rejoice in them all; yet let him remember the days of darkness; for they shall be many. All that cometh is vapor.",
      "M": "If a person lives many years, let them rejoice in them all; but let them also remember that the days of darkness will be many. All that comes is vapor.",
      "T": "If you live a long life, take joy in every year of it. But don't forget: the dark days are coming, and there will be many of them. All of it — every year, every day — is vapor in the end."
    },
    "9": {
      "L": "Rejoice, O young man, in thy youth; and let thy heart cheer thee in the days of thy youth, and walk in the ways of thine heart, and in the sight of thine eyes: but know thou, that for all these things God will bring thee into judgment.",
      "M": "Rejoice, young man, in your youth; let your heart gladden you in the days of your youth. Follow the desires of your heart and what your eyes see. But know this: for all these things God will bring you into judgment.",
      "T": "Young man, enjoy your youth — let your heart guide you, follow what your eyes desire. Live fully in these years. But here is what you must also know: God will call you to account for all of it."
    },
    "10": {
      "L": "Therefore remove sorrow from thy heart, and put away evil from thy flesh: for childhood and youth are vapor.",
      "M": "Banish anxiety from your heart and put away pain from your body, for childhood and youth are vapor.",
      "T": "Drive worry away — from your heart and your body alike. Live lightly in this season. Youth and the first chapter of life go faster than a breath."
    }
  },
  "12": {
    "1": {
      "L": "Remember now thy Creator in the days of thy youth, while the evil days come not, nor the years draw nigh, when thou shalt say, I have no pleasure in them;",
      "M": "Remember your Creator in the days of your youth, before the days of trouble come and the years arrive when you will say, 'I find no pleasure in them' —",
      "T": "Remember the God who made you — do it now, while you are still young, before the grim years arrive and the days come when you will say, 'There is no pleasure left in any of it' —"
    },
    "2": {
      "L": "While the sun, or the light, or the moon, or the stars, be not darkened, nor the clouds return after the rain:",
      "M": "— before the sun and the light and the moon and the stars grow dark, and the clouds return after the rain —",
      "T": "— before the light fails — sun, moon, and stars — and the clouds keep returning even after the rain falls —"
    },
    "3": {
      "L": "In the day when the keepers of the house shall tremble, and the strong men shall bow themselves, and the grinders cease because they are few, and those that look out of the windows be darkened,",
      "M": "— in the day when the keepers of the house tremble and the strong men are stooped, when the grinding women stop because they are too few and those who look through the windows grow dim —",
      "T": "— when the arms that guard you begin to tremble, when the legs that bore you up bow under their own weight, when the teeth that ground your food are too few to bother, when the eyes that once saw clearly have grown dim —"
    },
    "4": {
      "L": "And the doors shall be shut in the streets, when the sound of the grinding is low, and he shall rise up at the voice of the bird, and all the daughters of musick shall be brought low;",
      "M": "— when the street doors are shut and the sound of grinding fades, when one wakes at the mere chirp of a bird and all voices of song are brought low —",
      "T": "— when the outer doors close, when the sound of the millstone fades to nothing, when any bird's call wakes you from sleep, when the voices that used to sing are silenced —"
    },
    "5": {
      "L": "Also when they shall be afraid of that which is high, and fears shall be in the way, and the almond tree shall flourish, and the grasshopper shall be a burden, and desire shall fail: because man goeth to his long home, and the mourners go about the streets:",
      "M": "— when they are afraid of heights and dread is on every path, when the almond tree blossoms white, the grasshopper becomes a burden, and desire fails — because man is going to his eternal home while the mourners already walk the streets —",
      "T": "— when even a slight elevation fills you with fear, when the path ahead seems full of dread, when the almond tree stands white as old age, when even a grasshopper feels heavy to carry, when all appetite and desire drains away — because the man is heading home at last, and the mourners are already gathering in the street —"
    },
    "6": {
      "L": "Or ever the silver cord be loosed, or the golden bowl be broken, or the pitcher be broken at the fountain, or the wheel broken at the cistern.",
      "M": "— before the silver cord is severed or the golden bowl is shattered, before the pitcher breaks at the spring or the wheel breaks at the well —",
      "T": "— before the silver cord snaps, before the golden bowl shatters, before the jar at the spring cracks and the pulley at the well gives way —"
    },
    "7": {
      "L": "Then shall the dust return to the earth as it was: and the spirit shall return unto God who gave it.",
      "M": "— then the dust returns to the earth as it was, and the spirit returns to God who gave it.",
      "T": "When all of that has come — the dust goes back to the earth from which it was taken, and the Spirit that God breathed into us returns to the God who gave it."
    },
    "8": {
      "L": "Vapor of vapors, saith the Preacher; all is vapor.",
      "M": "Vapor of vapors, says the Teacher — all is vapor.",
      "T": "Breath of breaths, says the Teacher — all of it, every last thing, is a breath."
    },
    "9": {
      "L": "And moreover, because the Preacher was wise, he still taught the people knowledge; yea, he gave good heed, and sought out, and set in order many proverbs.",
      "M": "Beyond being wise himself, the Teacher also imparted knowledge to the people. He listened carefully, investigated thoroughly, and arranged many proverbs with precision.",
      "T": "The Teacher did more than think deeply — he taught. He listened carefully, researched widely, and set his findings in the ordered form of proverbs so that others could receive them."
    },
    "10": {
      "L": "The preacher sought to find out acceptable words: and that which was written was upright, even words of truth.",
      "M": "The Teacher sought to find pleasing words, and what he wrote was honest — words of truth.",
      "T": "He searched for exactly the right words — not just accurate ones, but beautiful and compelling ones. What he wrote was true; how he wrote it was a craft."
    },
    "11": {
      "L": "The words of the wise are as goads, and as nails fastened by the masters of assemblies, which are given from one shepherd.",
      "M": "The words of the wise are like goads, and like firmly driven nails are the collected sayings arranged by masters — all given from one Shepherd.",
      "T": "Wise words function like a goad — they move you forward even when you resist. They function like nails — they hold things in place. These assembled proverbs come ultimately from one Shepherd, who is their source."
    },
    "12": {
      "L": "And further, by these, my son, be admonished: of making many books there is no end; and much study is a weariness of the flesh.",
      "M": "Beyond these, my son, be warned: the making of many books has no end, and much study wears out the body.",
      "T": "Beyond these words, my son, be cautious. Books multiply without end, and chasing all that knowledge will exhaust you."
    },
    "13": {
      "L": "Let us hear the conclusion of the whole matter: Fear God, and keep his commandments: for this is the whole duty of man.",
      "M": "This is the conclusion of the whole matter: fear God and keep his commandments — this is the whole duty of every person.",
      "T": "Here is everything distilled: Fear God. Keep his commands. That is the full extent of what it means to be human."
    },
    "14": {
      "L": "For God shall bring every work into judgment, with every secret thing, whether it be good, or whether it be evil.",
      "M": "For God will bring every act into judgment — every hidden thing, whether good or evil.",
      "T": "Because in the end, God will put everything on trial — every action, every secret, every hidden motive. Good or evil, nothing escapes his notice."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ecclesiastes')
        merge_tier(existing, ECCLESIASTES, tier_key)
        save(tier_dir, 'ecclesiastes', existing)
    print('Ecclesiastes 9–12 written.')

if __name__ == '__main__':
    main()
