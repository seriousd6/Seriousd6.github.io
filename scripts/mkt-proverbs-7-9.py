"""
MKT Proverbs chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-7-9.py

Translation decisions:

- H3068 (יהוה, YHWH): "LORD" in L/M; "the LORD" in T. Consistent with chs 1–3 and
  the full OT series.

- H7585 (שְׁאוֹל, Sheol): Rendered "Sheol" in all three tiers at 7:27 and 9:18.
  "Hell" (KJV) is too theologically loaded; "the grave" is too flat. "Sheol" is the
  correct Hebrew term for the realm of the dead and is used as-is.

- H7069 (קָנָה, qanah) at 8:22: "possessed." The famous disputed rendering. Hebrew
  qanah means "acquire, possess, get" in its most common sense (Gen 4:1; 14:19,22).
  In a few places it may mean "create" (NIV). The choice matters christologically:
  if wisdom is "created," she is a creature; if "possessed," she is the LORD's from
  eternity. L and M use "possessed" (more faithful to qanah's primary sense). T
  renders it as "set me in place / made me his own before any of his works" — the
  pre-creation belonging is the point, not the mechanism.

- H525 (אָמוֹן, amon) at 8:30: "master craftsman." The word is a hapax in this
  sense. KJV "one brought up with him" (nursling / cherished child) reflects one
  reading; ESV/NASB/NIV "master workman / craftsman" reflects the architectural
  sense (related to H539 root, faithfulness/firmness, but used as artisan title).
  L/M: "master craftsman." T honors both: "the master builder, his daily delight"
  — Wisdom is both the skilled artisan of creation and the beloved companion of
  the Creator.

- H2342 (חוּל, chul) at 8:24,25: "brought forth." This is birth language — the
  same verb used for labor and writhing in childbirth. The metaphor is deliberate:
  Wisdom is born (of the LORD) before anything else. All tiers preserve this.

- H5258 (נָסַךְ, nasak) at 8:23: "set up / installed." L: "set up"; M: "installed."
  The image is of a ruler or official being placed in position. Wisdom was installed/
  appointed from eternity — not merely present but established with authority.

- H2454 (חָכְמוֹת / חָכְמָה, chokmoth/chokmah): Ch 9 opens with the intensive plural
  form (chokmoth) — Lady Wisdom as the fully expressed, personified Wisdom. T tier
  maintains the personification throughout ch 9.

- H3820 (לֵב, lev): "heart" throughout all chapters — inner life, will, and mind
  combined. Consistent with chs 1–3.

- H5315 (נֶפֶשׁ, nephesh): 7:23 "his life" (the endangered embodied self);
  8:36 "himself" — "wrongeth his own soul / harms himself." The embodied self
  in danger of death, not an immaterial Greek soul.

- H2181 (זָנָה, zanah) at 7:10: The word means "harlot/prostitute." L: "harlot"
  (traditional); M/T: describes the woman's attire and manner rather than labeling
  her occupationally — the text emphasizes she dresses and acts like one.

- H7496 (רְפָאִים, Rephaim) at 9:18: "the dead." The shades / spirits of the dead
  who inhabit Sheol. L: "the dead"; M: "the dead"; T: "the dead" with context.

- Chapter 7 structure: Narrative vignette framing (father watching from window,
  vv.6–23) embedded in an exhortation (vv.1–5, 24–27). The T tier makes the
  dramatic perspective explicit — this is the father as narrator.

- Chapter 8 structure: Three movements — public invitation (vv.1–11), Wisdom's
  own character (vv.12–21), pre-creation testimony (vv.22–31), final call
  (vv.32–36). The pre-creation section is the theological center of the book.
  T tier surfaces the cosmic weight and the relational joy.

- Chapter 9 structure: Direct parallel between Wisdom's feast (vv.1–6) and
  Folly's counter-invitation (vv.13–18), with independent proverbs in vv.7–12
  as an interlude. Folly uses almost identical language to Wisdom (v.16 = v.4;
  v.17 ≠ v.5 — the difference is telling). T tier makes the structural irony
  explicit, especially in v.18.

- Gnomic aspect: Most Proverbs in chs 7–9 use participial and imperfect forms
  as general/timeless statements. These are rendered in simple present tense
  throughout. The narrative of ch 7 vv.6–23 uses waw-consecutive perfect/
  imperfect for narrative past — rendered in past tense accordingly.

- OT intertextuality at 8:22–31: This passage closely parallels Ben Sira 24
  (Sirach) and is quoted/alluded to in John 1 (Logos), Col 1:15–17, and
  Rev 3:14. T tier does not make NT allusions explicit (that belongs in notes),
  but renders the passage with the full weight it carries — pre-existence,
  cosmic scope, intimate joy.

- 9:10 echoes 1:7 (the programmatic motto). T tier notes this as the book's
  own refrain — the second occurrence deepens the first.
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


PROVERBS = {
  "7": {
    "1": {
      "L": "My son, keep my words, and lay up my commandments with you.",
      "M": "My son, keep my words and store up my commands within you.",
      "T": "My son, keep what I tell you. Let my commands become something you actually hold onto."
    },
    "2": {
      "L": "Keep my commandments and live; my law as the apple of your eye keep.",
      "M": "Keep my commands and live; guard my teaching as the apple of your eye.",
      "T": "Follow my commands and you will live. Guard my teaching the way you guard your own eyes — that carefully, that close."
    },
    "3": {
      "L": "Bind them upon your fingers; write them on the tablet of your heart.",
      "M": "Tie them on your fingers; inscribe them on the tablet of your heart.",
      "T": "Tie them around your fingers so you see them at every turn. Engrave them deep in your heart."
    },
    "4": {
      "L": "Say to wisdom, 'You are my sister,' and call understanding your kinswoman,",
      "M": "Say to wisdom, 'You are my sister,' and call understanding your closest companion,",
      "T": "Make wisdom your sister — your nearest kin. Treat understanding as your dearest friend."
    },
    "5": {
      "L": "That they may keep you from the strange woman, from the foreigner who flatters with her words.",
      "M": "They will keep you from the immoral woman, from the seductive stranger with her flattering words.",
      "T": "Wisdom and understanding will guard you from the woman who will ruin you — the one whose smooth words are a trap."
    },
    "6": {
      "L": "For at the window of my house I have looked out through my lattice,",
      "M": "Once at the window of my house I looked out through the lattice,",
      "T": "Let me tell you what I saw one evening. I was at my window, looking through the lattice."
    },
    "7": {
      "L": "And I discerned among the simple, among the youths, a young man void of understanding,",
      "M": "I observed among the naive, among the young men, one who lacked all sense —",
      "T": "There was a young man out there — inexperienced, naive — someone who had never learned to think ahead."
    },
    "8": {
      "L": "Passing through the street near her corner, and he went the way to her house,",
      "M": "Cutting through the street near her corner, heading down the road toward her house,",
      "T": "He was wandering — passing her corner, drifting toward her house, maybe without even meaning to."
    },
    "9": {
      "L": "In the twilight, in the evening, in the black and dark of night.",
      "M": "This was in the twilight, in the evening, in the black darkness of night.",
      "T": "And it was evening — that hour between light and darkness when decisions are made badly."
    },
    "10": {
      "L": "And behold, there met him a woman with the attire of a harlot, and subtil of heart.",
      "M": "A woman met him, dressed like a prostitute, her heart scheming.",
      "T": "She was there. Dressed to be noticed. Her face said one thing; her plans were something else entirely."
    },
    "11": {
      "L": "She is loud and stubborn; her feet abide not in her house;",
      "M": "She is loud and defiant; her feet never stay at home;",
      "T": "This woman does not sit still. She is everywhere, restless, defiant — not the kind of person whose life is ordered."
    },
    "12": {
      "L": "Now she is without, now in the streets, and she lies in wait at every corner.",
      "M": "Now outside, now in the streets — lurking at every corner.",
      "T": "Roaming the streets. Waiting at corners. Watching."
    },
    "13": {
      "L": "So she caught him and kissed him, and with an impudent face said to him:",
      "M": "She grabbed him and kissed him and said to him with a brazen face:",
      "T": "She grabbed him. She kissed him. No shame at all on her face."
    },
    "14": {
      "L": "'I have peace offerings with me; this day I have paid my vows.",
      "M": "'I had fellowship offerings to make; today I paid my vows.",
      "T": "'I have just come from the temple — paid my vows, everything settled. And there is more than enough feast left at home.'"
    },
    "15": {
      "L": "'Therefore came I forth to meet you, to seek your face diligently, and I have found you.",
      "M": "'That is why I came out to meet you — I was looking for you and here you are.",
      "T": "'I was looking for you specifically. I came out to find you. And here you are.'"
    },
    "16": {
      "L": "'I have decked my bed with coverings of tapestry, with fine linen of Egypt.",
      "M": "'I have spread my bed with colored blankets and fine linen from Egypt.",
      "T": "'My bed is ready — layered with color, with the finest Egyptian linen.'"
    },
    "17": {
      "L": "'I have perfumed my bed with myrrh, aloes, and cinnamon.",
      "M": "'I have scented my bed with myrrh, aloes, and cinnamon.",
      "T": "'Every spice you could want — myrrh, aloes, cinnamon. I have prepared everything.'"
    },
    "18": {
      "L": "'Come, let us take our fill of love until morning; let us solace ourselves with loves.",
      "M": "'Come, let us drink our fill of love until morning; let us delight in lovemaking.",
      "T": "'Come — the whole night, nothing but pleasure. Let us take everything the darkness can give.'"
    },
    "19": {
      "L": "'For my husband is not at home; he has gone on a long journey;",
      "M": "'My husband is not home; he has gone on a long trip;",
      "T": "'And there is no one to worry about. My husband is far away.'"
    },
    "20": {
      "L": "'He has taken a bag of money with him; at the full moon he will come home.'",
      "M": "'He took his money with him; he will not be back until the full moon.'",
      "T": "'He packed his purse and left. He will not return for weeks. The timing is perfect.'"
    },
    "21": {
      "L": "With much fair speech she caused him to yield; with the flattering of her lips she forced him.",
      "M": "With her many persuasive words she led him astray; with the smooth speech of her lips she compelled him.",
      "T": "Every word out of her mouth was calculated. She aimed them all at that one unguarded place in him, and hit it."
    },
    "22": {
      "L": "He goes after her straightway, as an ox goes to the slaughter, or as a fool to the correction of the stocks,",
      "M": "He followed her at once — like an ox heading to slaughter, like a fool walking into punishment,",
      "T": "He went. Without a thought. Like an animal walking into a trap it cannot see — moving toward what will destroy it."
    },
    "23": {
      "L": "Till a dart strike through his liver; as a bird hastens to the snare, and knows not that it is for his life.",
      "M": "Until an arrow pierces his liver — like a bird rushing into a snare, not knowing that his life is the price.",
      "T": "The wound will come like a sudden bolt. Like a bird flying straight into a net — he does not realize until it is already too late that what he walked toward was his death."
    },
    "24": {
      "L": "Hearken unto me now, O ye children, and attend to the words of my mouth.",
      "M": "So now, my children, listen to me — pay close attention to what I am saying.",
      "T": "Let me be direct with you. You just watched that. Now listen."
    },
    "25": {
      "L": "Let not your heart decline to her ways; go not astray in her paths.",
      "M": "Do not let your heart wander toward her ways; do not go astray on her paths.",
      "T": "Do not let your heart drift in her direction. Once your feet find her path, they will not easily stop."
    },
    "26": {
      "L": "For she has cast down many wounded; yea, many strong men have been slain by her.",
      "M": "She has brought down many victims; a long line of powerful men have been destroyed by her.",
      "T": "She has taken down people stronger than you. More experienced men, with more reason to know better. They all walked that road."
    },
    "27": {
      "L": "Her house is the way to Sheol, going down to the chambers of death.",
      "M": "Her house is the road to Sheol; it leads to the inner chambers of death.",
      "T": "Every step toward her door is a step toward Sheol. The path only goes one direction — down, into the dark."
    }
  },
  "8": {
    "1": {
      "L": "Does not wisdom cry? And understanding put forth her voice?",
      "M": "Does wisdom not call out? Does understanding not raise her voice?",
      "T": "Wisdom is not silent. She is calling — loudly, publicly, unmistakably."
    },
    "2": {
      "L": "She stands in the top of the high places, by the way in the places of the paths.",
      "M": "She takes her stand on the high ground, at the crossroads where the paths meet.",
      "T": "She has positioned herself where everyone will pass — the hilltop, the intersection, the place no one can avoid."
    },
    "3": {
      "L": "She cries at the gates, at the entry of the city, at the coming in at the doors.",
      "M": "She cries out at the city gates, at the entrance of the city, at the doorways.",
      "T": "She stands at the city gate — the place of commerce, of judgment, of everyone passing through. No one can claim they never heard."
    },
    "4": {
      "L": "'Unto you, O men, I call; and my voice is to the sons of man.",
      "M": "'I am calling to you — to all humanity, to every child of Adam.",
      "T": "'I am not calling to a select few. I am calling to every human being.'"
    },
    "5": {
      "L": "'O ye simple, understand wisdom; and ye fools, be of an understanding heart.",
      "M": "'You naive ones, learn prudence; you fools, gain a discerning heart.",
      "T": "'The naive person — wisdom is available to you. The confirmed fool — even you could still learn to think.'"
    },
    "6": {
      "L": "'Hear, for I will speak excellent things; and the opening of my lips shall be right things.",
      "M": "'Listen — I am speaking what is excellent; everything from my mouth will be right.",
      "T": "'What I say is worth hearing — not to impress you, but because what I say is true, and right, and excellent.'"
    },
    "7": {
      "L": "'For my mouth shall speak truth; and wickedness is an abomination to my lips.",
      "M": "'My mouth speaks truth; wickedness is detestable to me.",
      "T": "'I do not deal in half-truths or clever deceptions. Truth is what my mouth produces — wickedness is something I cannot even tolerate.'"
    },
    "8": {
      "L": "'All the words of my mouth are in righteousness; there is nothing froward or perverse in them.",
      "M": "'Every word I speak is right; nothing I say is twisted or deceptive.",
      "T": "'Every single word — straight. Nothing bent. Nothing designed to mislead.'"
    },
    "9": {
      "L": "'They are all plain to him that understands, and right to them that find knowledge.",
      "M": "'To those with understanding, my words are all clear; to those who have found knowledge, they are entirely right.",
      "T": "'The honest seeker will find my words easy to understand. The person who wants the truth will recognize it immediately.'"
    },
    "10": {
      "L": "'Receive my instruction, and not silver; and knowledge rather than choice gold.",
      "M": "'Take my instruction rather than silver, and choose knowledge over the finest gold.",
      "T": "'What I offer is worth more than any amount of money. Accept it. Choose knowledge over wealth.'"
    },
    "11": {
      "L": "'For wisdom is better than rubies; and all the things that may be desired are not to be compared to it.",
      "M": "'Wisdom is more valuable than precious gems; nothing you could wish for compares to her.",
      "T": "'Whatever you could name — every beautiful, valuable, desirable thing in the world — wisdom is worth more.'"
    },
    "12": {
      "L": "'I wisdom dwell with prudence, and find out knowledge and discretion.",
      "M": "'I, wisdom, live alongside prudence, and find knowledge and good judgment.",
      "T": "'I am wisdom, and I keep company with prudence. Where I am, you will also find knowledge and the ability to think clearly.'"
    },
    "13": {
      "L": "'The fear of the LORD is to hate evil; pride and arrogancy and the evil way and the froward mouth do I hate.",
      "M": "'The fear of the LORD means hating evil — I hate pride, arrogance, evil conduct, and perverse speech.",
      "T": "'To fear the LORD is to hate what he hates. And what he hates is this: pride, arrogance, the road that leads to evil, and the tongue that twists truth into a weapon.'"
    },
    "14": {
      "L": "'Counsel is mine, and sound wisdom; I am understanding; I have strength.",
      "M": "'Mine are counsel and tested wisdom; I am understanding; I have strength.",
      "T": "'Wisdom brings with her everything needed for governing life: strategy, tested wisdom, clear sight, and the kind of strength that does not collapse.'"
    },
    "15": {
      "L": "'By me kings reign, and princes decree justice.",
      "M": "'Through me kings reign and rulers issue just decrees.",
      "T": "'Every legitimate authority that has ever governed well has governed through wisdom — whether they knew it or not.'"
    },
    "16": {
      "L": "'By me princes rule, and nobles, even all the judges of the earth.",
      "M": "'Through me princes govern, and nobles — all who exercise righteous authority over the earth.",
      "T": "'Every leader, every judge, every official who has actually served their people well — it was wisdom that made them capable.'"
    },
    "17": {
      "L": "'I love them that love me; and those that seek me diligently shall find me.",
      "M": "'I love those who love me; those who seek me earnestly will find me.",
      "T": "'Wisdom responds to love. Those who genuinely seek her — persistently, wholeheartedly — will find her.'"
    },
    "18": {
      "L": "'Riches and honor are with me; yea, durable riches and righteousness.",
      "M": "'With me are riches and honor — lasting wealth and righteousness.",
      "T": "'Seek wisdom and find what money cannot purchase: genuine honor, and wealth that actually endures, along with the character to hold it rightly.'"
    },
    "19": {
      "L": "'My fruit is better than gold, yea, than fine gold; and my revenue than choice silver.",
      "M": "'What I produce is better than gold — even fine gold; my yield surpasses choice silver.",
      "T": "'The return on wisdom is superior to any financial investment you can name. Better than gold, better than the finest silver.'"
    },
    "20": {
      "L": "'I lead in the way of righteousness, in the midst of the paths of justice,",
      "M": "'I walk in the path of righteousness, along the roads of justice,",
      "T": "'Wisdom does not only talk about righteousness — she walks in it. Follow her and you are on the right road.'"
    },
    "21": {
      "L": "'That I may cause those that love me to inherit substance; and I will fill their treasuries.",
      "M": "'Giving a real inheritance to those who love me, and filling their storehouses.",
      "T": "'Those who love wisdom receive what wisdom gives: a true inheritance — something to build a life on and pass forward.'"
    },
    "22": {
      "L": "'The LORD possessed me at the beginning of his way, before his works of old.",
      "M": "'The LORD possessed me at the beginning of his way, before the oldest of his works.",
      "T": "'Before anything was made — before the first act of creation — wisdom was already there, already the LORD's own.'"
    },
    "23": {
      "L": "'I was set up from everlasting, from the beginning, before ever the earth was.",
      "M": "'I was installed from eternity — from the very beginning, before the earth existed.",
      "T": "'Not recent. Not newly appointed. From before time had a name, wisdom was already established and in place.'"
    },
    "24": {
      "L": "'When there were no depths, I was brought forth; when there were no fountains abounding with water.",
      "M": "'Before the oceans existed I was born — before the springs were teeming with water.",
      "T": "'Before the deep existed, before a single spring had broken the surface anywhere — wisdom was already born.'"
    },
    "25": {
      "L": "'Before the mountains were settled, before the hills, was I brought forth,",
      "M": "'Before the mountains were in place, before the hills, I was brought into being —",
      "T": "'The mountains have their age. Wisdom is older.'"
    },
    "26": {
      "L": "'While as yet he had not made the earth, nor the fields, nor the highest part of the dust of the world.",
      "M": "'Before he had made the earth or its open lands or the first dust of the world.",
      "T": "'Before the earth was anything, before there was even soil — wisdom already was.'"
    },
    "27": {
      "L": "'When he prepared the heavens, I was there; when he set a compass upon the face of the deep;",
      "M": "'When he set the heavens in place I was there; when he drew the horizon over the face of the deep;",
      "T": "'When the LORD arched the heavens overhead and marked the boundary between sky and sea — wisdom was there, watching every stroke.'"
    },
    "28": {
      "L": "'When he established the clouds above; when he strengthened the fountains of the deep;",
      "M": "'When he fixed the clouds above and set firm the fountains of the deep;",
      "T": "'When the clouds were stretched overhead like a canopy, when the springs of the deep were sealed in place — wisdom was there for all of it.'"
    },
    "29": {
      "L": "'When he gave to the sea his decree that the waters should not pass his commandment; when he appointed the foundations of the earth —",
      "M": "'When he gave the sea its limits so the waters could not overstep his command, when he marked out the earth's foundations —",
      "T": "'When the sea was given its boundary — go this far and no further — wisdom was watching. When the foundations of the earth were laid, wisdom was there.'"
    },
    "30": {
      "L": "'Then I was beside him, as a master craftsman; and I was daily his delight, rejoicing before him always,",
      "M": "'Then I was beside him, the master craftsman; I was his daily delight, rejoicing before him always,",
      "T": "'All through the work of creation, wisdom was beside the LORD — not as a spectator but as the master builder, bringing skill to every act. And the joy of it was daily, endless: wisdom rejoicing in the work, and the LORD delighting in wisdom.'"
    },
    "31": {
      "L": "'Rejoicing in the habitable part of his earth; and my delights were with the sons of men.",
      "M": "'Rejoicing in the world he had made, and my delight was in the children of humanity.",
      "T": "'And when the world was populated — people, cities, life — wisdom's delight turned toward them. She was made not only for the Creator's pleasure but for ours.'"
    },
    "32": {
      "L": "'Now therefore hearken unto me, O ye children; for blessed are they that keep my ways.",
      "M": "'So now, my children, listen to me — blessed are those who keep to my ways.",
      "T": "'This is what all of that means for you: wisdom is not an abstraction. She existed before you, she was present at your making, she delights in you. Listen to her.'"
    },
    "33": {
      "L": "'Hear instruction and be wise, and refuse it not.",
      "M": "'Accept instruction and be wise; do not reject it.",
      "T": "'Hearing alone is not enough — you have to receive it. Do not set it aside.'"
    },
    "34": {
      "L": "'Blessed is the man that hears me, watching daily at my gates, waiting at the posts of my doors.",
      "M": "'Blessed is the person who listens to me — waiting at my doors every morning, watching at my threshold.",
      "T": "'True happiness belongs to the one who comes back every day. Who shows up at wisdom's door in the morning and does not leave until they have heard something worth keeping.'"
    },
    "35": {
      "L": "'For whoso finds me finds life, and shall obtain favor of the LORD.",
      "M": "'Whoever finds me finds life and receives the LORD's favor.",
      "T": "'Finding wisdom is finding life itself. And the one who finds wisdom finds, in that same moment, the favor of the LORD — because wisdom is his gift.'"
    },
    "36": {
      "L": "'But he that sins against me wrongs his own soul; all they that hate me love death.'",
      "M": "'But whoever fails to find me harms himself; all who hate me embrace death.'",
      "T": "'To reject wisdom is to wound yourself. And those who have made a settled decision to hate wisdom — they may not know it yet, but they have chosen death.'"
    }
  },
  "9": {
    "1": {
      "L": "Wisdom has built her house; she has hewn out her seven pillars.",
      "M": "Wisdom has built her house; she has hewn out her seven pillars.",
      "T": "Lady Wisdom has built a house — substantial and beautiful, set on seven pillars she cut and shaped with her own hands."
    },
    "2": {
      "L": "She has killed her beasts; she has mixed her wine; she has also furnished her table.",
      "M": "She has slaughtered her animals, mixed her wine, and set her table.",
      "T": "The feast is prepared. Meat carved, wine ready, table spread. Everything is waiting."
    },
    "3": {
      "L": "She has sent forth her maidens; she cries upon the highest places of the city:",
      "M": "She has sent out her servants, calling from the heights of the city:",
      "T": "And she has kept nothing private. Her servants move through the city, calling from every high place."
    },
    "4": {
      "L": "'Whoever is simple, let him turn in here.' To him that lacks understanding she says,",
      "M": "'Let the simple come in here.' To the one who lacks understanding she says,",
      "T": "'You — the inexperienced one. Come. Exactly you.'"
    },
    "5": {
      "L": "'Come, eat of my bread, and drink of the wine which I have mixed.",
      "M": "'Come and eat my bread; drink the wine I have mixed.",
      "T": "'Sit down. Eat. Drink. This meal was made for you.'"
    },
    "6": {
      "L": "'Forsake the foolish and live; and go in the way of understanding.",
      "M": "'Leave your simple ways and live; walk in the path of understanding.",
      "T": "'But you must leave the old way to enter this one. You cannot have both. Choose life — and start walking toward wisdom.'"
    },
    "7": {
      "L": "He that reproves a scorner gets himself shame; and he that rebukes a wicked man gets himself a blot.",
      "M": "Whoever rebukes a mocker earns insults; whoever corrects a wicked man gets hurt.",
      "T": "Correcting a hardened mocker does not help the mocker — it only costs you. Reproving someone who has made wickedness their identity invites abuse."
    },
    "8": {
      "L": "Reprove not a scorner, lest he hate you; rebuke a wise man, and he will love you.",
      "M": "Do not rebuke a mocker or he will only hate you; rebuke a wise person and he will love you for it.",
      "T": "Don't waste correction on the mocker. Save it for the person who is actually wise — they will receive it as a gift."
    },
    "9": {
      "L": "Give instruction to a wise man, and he will be yet wiser; teach a just man, and he will increase in learning.",
      "M": "Teach the wise and they grow wiser still; instruct the righteous and they gain more.",
      "T": "Wisdom compounds. The person who already has some will absorb more — and keep absorbing. Correction is fuel for the wise."
    },
    "10": {
      "L": "The fear of the LORD is the beginning of wisdom; and the knowledge of the holy is understanding.",
      "M": "The fear of the LORD is the beginning of wisdom; knowing the Holy One is understanding.",
      "T": "The summary, again — the same foundation the book began with: wisdom starts with the fear of the LORD. And to genuinely know the Holy One — that itself is understanding. Everything else follows from this."
    },
    "11": {
      "L": "For by me your days shall be multiplied, and the years of your life shall be increased.",
      "M": "For through me your days will multiply and years will be added to your life.",
      "T": "Wisdom does not merely enrich life — it lengthens it. Days and years are added to the one who lives wisely."
    },
    "12": {
      "L": "If you are wise, you are wise for yourself; but if you scorn, you alone shall bear it.",
      "M": "If you are wise, the benefit is yours alone; if you scoff, you alone bear the consequences.",
      "T": "Wisdom's rewards are yours to keep. But mockery's cost belongs entirely to you as well. No one else absorbs what you chose."
    },
    "13": {
      "L": "A foolish woman is clamorous; she is simple and knows nothing.",
      "M": "Dame Folly is loud; she is naive and knows nothing.",
      "T": "There is another voice calling through the city. Dame Folly. Loud — but with nothing behind the noise. Simple, empty, all surface."
    },
    "14": {
      "L": "For she sits at the door of her house, on a seat in the high places of the city,",
      "M": "She sits at the door of her house, in a seat at the high places of the city,",
      "T": "She has copied Wisdom's position — the heights, a visible seat, where everyone can see and be seen."
    },
    "15": {
      "L": "To call passengers who go right on their ways:",
      "M": "Calling out to those who are passing by, going straight on their way:",
      "T": "She targets the people who were walking the right road — interrupting the ones who had somewhere good to go."
    },
    "16": {
      "L": "'Whoever is simple, let him turn in here.' And to him that lacks understanding she says,",
      "M": "'Let the simple come in here.' To the one who lacks understanding she says,",
      "T": "Her words are identical to Wisdom's: 'You — the inexperienced one. Come in here.'"
    },
    "17": {
      "L": "'Stolen waters are sweet, and bread eaten in secret is pleasant.'",
      "M": "'Stolen water is sweet, and food eaten in secret is delicious.'",
      "T": "'What is forbidden is more exciting. What is taken in secret tastes better.' The oldest lie in the world, dressed as an invitation."
    },
    "18": {
      "L": "But he knows not that the dead are there; and that her guests are in the depths of Sheol.",
      "M": "But he does not know that the dead are there — that her guests are in the depths of Sheol.",
      "T": "He does not see what the house really is. The people at Folly's table are the dead. Her guests are in the depths of Sheol. The invitation sounded like dinner. It was a funeral."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 7–9 written.')

if __name__ == '__main__':
    main()
