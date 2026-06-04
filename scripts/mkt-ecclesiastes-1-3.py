"""
MKT Ecclesiastes chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ecclesiastes-1-3.py

Translation decisions:

- H1892 (הֶבֶל, hebel): The book's central word. Literally "breath/vapor/mist" — something
  ephemeral that vanishes when grasped. L: "vapor" (the literal image). M: "futility" (the
  semantic content). T: varies by verse — "vapor," "nothing that lasts," "breath." Not "vanity"
  in any tier — that English word now evokes pride/vainglory, not ephemerality. The superlative
  הֲבֵל הֲבָלִים (1:2): L: "vapor of vapors"; M: "utter futility"; T: "breath upon breath."

- H6953 (קֹהֶלֶת, Qohelet): From קָהַל (to assemble/gather). "Preacher" (KJV) is misleading.
  L/M: "the Teacher." T: uses "Qohelet" once at 1:1 to name the tradition, then "the Teacher."

- H7469/H7307 phrase (רְעוּת/רַעְיוֹן רוּחַ, re'ut ruach): The verdict refrain. Traditional
  "vexation of spirit" is obscure. Image is futile chasing of wind.
  L: "striving after wind." M: "chasing the wind." T: "grasping at what cannot be held."

- H7307 (רוּחַ, ruach): Three distinct uses in chs 1–3:
  (a) 1:6 meteorological wind — "wind" in all tiers.
  (b) in the phrase re'ut ruach — "striving after wind" (L) / "chasing the wind" (M).
  (c) 3:19–21 animating breath shared by all creatures — "breath" (L/M); "spirit" (T, 3:21)
      where the metaphysical question is raised.

- H430 (אֱלֹהִים, Elohim): "God" in all tiers. Note: Ecclesiastes uses Elohim exclusively —
  YHWH (H3068) does not appear in the book. Theologically significant: Qohelet speaks of God
  as transcendent sovereign, not in intimate covenant terms.

- H3504 (יִתְרוֹן, yitron): Commercial term meaning "surplus/profit/what remains." Unique to
  Ecclesiastes in the OT. L: "profit." M: "gain." T: "what remains" / "lasting gain."

- H5769 (עוֹלָם, olam): "forever" (1:4) and "eternity" (3:11). At 3:11 T tier develops the
  "eternity in the heart" motif: awareness of something larger that we cannot fully comprehend.

- H8121 phrase (תַּחַת הַשֶּׁמֶשׁ, tahat hashemesh): "under the sun" — the book's signature phrase
  for the observable world / this life. L/M: "under the sun" throughout. T: occasionally
  "in this life" where the rhetorical register calls for it.

- 3:2–8 (the "times" poem): Tight antithetical parallelism. L/M: preserve the pair structure.
  T: uses " — " and " / " to give the pairs rhythmic visibility and preserve the compression.
  T does not explain the pairs; it respects them.

- 2:25 textual note: MT reads "who can eat or hasten more than I?" but several MSS and the LXX
  read "apart from him" (i.e., God). The contextual reading (2:24 attributes enjoyment to God's
  hand) strongly favors the LXX reading. L/M/T follow "apart from him."

- Aspect: Hebrew imperfect for gnomic statements rendered as simple present. Perfect for
  completed observations rendered as past.

- OT echoes: 1:2 thesis resumed at 12:8. The "time" poem (3:1–8) may be echoed in Sirach 33;
  Acts 1:7 and 1 Thess 5:1 share the "times and seasons" vocabulary. 2:25 anticipates the
  theology of joy as gift developed through chs 3, 5, 8, 9.
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
  "1": {
    "1": {
      "L": "The words of the Teacher, the son of David, king in Jerusalem.",
      "M": "The words of the Teacher, son of David, king in Jerusalem.",
      "T": "What follows are the words of Qohelet — the Teacher — son of David, who reigned as king in Jerusalem and subjected human experience to systematic scrutiny."
    },
    "2": {
      "L": "Vapor of vapors, says the Teacher, vapor of vapors! All is vapor.",
      "M": "Utter futility, says the Teacher, utter futility! Everything is futile.",
      "T": "Breath upon breath — nothing but breath, says the Teacher. Whatever you look at closely enough, it slips away. Everything amounts to this."
    },
    "3": {
      "L": "What profit does man have from all his labor which he labors under the sun?",
      "M": "What lasting gain does a person have from all his toil at which he labors under the sun?",
      "T": "After all the work, all the effort, all the striving — what is left? What does any of it actually add up to in the end?"
    },
    "4": {
      "L": "One generation passes away, and another generation comes; but the earth abides forever.",
      "M": "One generation goes and another generation comes, but the earth remains forever.",
      "T": "People come and people go — generation after generation appearing and disappearing. The earth simply remains, outlasting everyone who has ever walked on it."
    },
    "5": {
      "L": "The sun also rises, and the sun goes down, and hastens to its place where it arose.",
      "M": "The sun rises and the sun sets, hurrying back to where it rises.",
      "T": "The sun climbs, plunges, and rushes back to rise again — relentless, repetitive, indifferent to all of it."
    },
    "6": {
      "L": "The wind goes toward the south, and turns around to the north; it whirls about continually, and the wind returns again according to its circuits.",
      "M": "The wind blows south, then turns north; it whirls around and around, and returns to its circuits.",
      "T": "The wind sweeps south, veers north, spins in endless circuits — going nowhere in particular, arriving back where it started."
    },
    "7": {
      "L": "All the rivers run into the sea, yet the sea is not full; to the place where the rivers flow, there they flow again.",
      "M": "All the rivers run to the sea, yet the sea is never full. To the place where the rivers go, they return to flow again.",
      "T": "River after river empties itself into the sea — and the sea is never full. Everything cycles back to its source and begins again. The motion is ceaseless; the destination is never truly reached."
    },
    "8": {
      "L": "All things are full of labor; man cannot utter it; the eye is not satisfied with seeing, nor the ear filled with hearing.",
      "M": "All things are wearisome; no one can express it. The eye is not satisfied with seeing, nor the ear full with hearing.",
      "T": "Everything exhausts itself in endless motion — and no one can find words for the sheer scale of it. The eye looks and looks and is never done. The ear hears and hears and still wants more. Nothing completes us."
    },
    "9": {
      "L": "The thing that has been, it is that which shall be; and that which is done is that which shall be done; and there is no new thing under the sun.",
      "M": "What has been is what will be, and what has been done is what will be done. There is nothing new under the sun.",
      "T": "Nothing new ever comes. What has already happened is what will happen again. What has already been done is what will be done. History does not progress — it repeats."
    },
    "10": {
      "L": "Is there anything of which it may be said, 'See, this is new'? It has already been in ages which were before us.",
      "M": "Is there a thing of which one says, 'See, this is new'? It has already been in the ages before us.",
      "T": "Every time someone points at something and says 'this has never been seen before,' they are wrong. It was seen before — in an age no one living can remember."
    },
    "11": {
      "L": "There is no remembrance of former things; neither shall there be any remembrance of things that are to come with those that shall come after.",
      "M": "There is no remembrance of earlier people, nor will there be any remembrance of people yet to come among those who come after them.",
      "T": "The people who came before us are forgotten. We will be forgotten too. Even what we count as memorable will eventually fade — no one coming after will remember us."
    },
    "12": {
      "L": "I the Teacher was king over Israel in Jerusalem.",
      "M": "I, the Teacher, was king over Israel in Jerusalem.",
      "T": "I — the one telling you this — was king over Israel in Jerusalem. I had the position and the resources to test everything that can be tested."
    },
    "13": {
      "L": "And I gave my heart to seek and to search out by wisdom concerning all things that are done under heaven: this grievous travail has God given to the sons of man to be exercised therewith.",
      "M": "And I applied my heart to seek and to search out by wisdom all that is done under heaven. It is an unhappy business that God has given to the children of man to be busy with.",
      "T": "I turned my whole attention — all my intellectual energy — to investigating by means of wisdom everything that happens in human life. It is a grim assignment. God has given human beings this restless drive to understand, and the understanding, when it comes, is often bitter."
    },
    "14": {
      "L": "I have seen all the works that are done under the sun; and behold, all is vapor and striving after wind.",
      "M": "I have seen all the works that are done under the sun, and behold, all is futility and chasing the wind.",
      "T": "I looked at everything that gets done in this life — all of it. My conclusion: every bit of it is vapor. You reach for it and find nothing in your hand."
    },
    "15": {
      "L": "That which is crooked cannot be made straight, and that which is lacking cannot be numbered.",
      "M": "What is crooked cannot be made straight, and what is lacking cannot be counted.",
      "T": "Some things are bent and cannot be straightened. Some things are missing and cannot be supplied. Not all problems have solutions. Part of wisdom is recognizing the limits of what can be fixed."
    },
    "16": {
      "L": "I communed with my own heart, saying, I have acquired more wisdom than all who were before me in Jerusalem; yea, my heart has had great experience of wisdom and knowledge.",
      "M": "I said to myself, 'I have acquired more wisdom than anyone who ruled before me in Jerusalem, and my heart has had great experience of wisdom and knowledge.'",
      "T": "I took stock of myself and concluded: I had surpassed every predecessor in Jerusalem. My mind had been more thoroughly exposed to wisdom and knowledge than anyone who came before me. I was uniquely equipped to know what others could not."
    },
    "17": {
      "L": "And I gave my heart to know wisdom, and to know madness and folly: I perceived that this also is striving after wind.",
      "M": "And I applied my heart to know wisdom, and to know madness and folly. I perceived that this also is chasing the wind.",
      "T": "I pursued not just wisdom but its opposite — madness, folly — because I wanted to understand the full range of human experience. And I found that even this investigation was futile. Knowing more did not help. The pursuit of understanding ran into the same wall as everything else."
    },
    "18": {
      "L": "For in much wisdom is much grief, and he that increases knowledge increases sorrow.",
      "M": "For in much wisdom is much vexation, and whoever increases knowledge increases sorrow.",
      "T": "The more you know, the more you see what is wrong. Wisdom is not a comfort — it expands the inventory of things that trouble you. Knowledge and grief grow together."
    }
  },
  "2": {
    "1": {
      "L": "I said in my heart, 'Come now, I will test you with pleasure; enjoy yourself.' And behold, this also was vapor.",
      "M": "I said in my heart, 'Come now, I will test you with pleasure; enjoy yourself.' But this also was futility.",
      "T": "So I tried pleasure. I said to myself: let's see what joy can do. I gave myself to it fully. It turned out to be the same vapor as everything else."
    },
    "2": {
      "L": "I said of laughter, 'It is madness,' and of pleasure, 'What does it accomplish?'",
      "M": "I said of laughter, 'It is madness,' and of pleasure, 'What does this achieve?'",
      "T": "Laughter, examined, was a kind of madness — activity without anchor. Pleasure produced no lasting thing. I kept asking: what does this actually accomplish?"
    },
    "3": {
      "L": "I sought in my heart to give myself unto wine — my heart still guiding me with wisdom — and to lay hold on folly, till I might see what was good for the sons of men to do under heaven all the days of their life.",
      "M": "I searched with my heart how to cheer myself with wine — my heart guiding me with wisdom — and how to take hold of folly, until I might see what was good for the children of man to do under heaven during the few days of their life.",
      "T": "I experimented with wine — carefully, with my analytical mind still running in the background — and I studied folly from the inside. I wanted to know: what is actually worth doing in the brief time a person has? I was trying to identify genuine good."
    },
    "4": {
      "L": "I made me great works; I built me houses; I planted me vineyards.",
      "M": "I made great works: I built houses for myself and planted vineyards for myself.",
      "T": "I built. I expanded. Houses went up. Vineyards were planted. I created the visible markers of a great life."
    },
    "5": {
      "L": "I made me gardens and orchards, and I planted trees in them of all kinds of fruit.",
      "M": "I made gardens and parks for myself, and planted in them all kinds of fruit trees.",
      "T": "I designed gardens and pleasure parks and filled them with every variety of fruit tree. I cultivated abundance at every scale."
    },
    "6": {
      "L": "I made me pools of water, to water therewith the forest of growing trees.",
      "M": "I made pools from which to water the forest of growing trees.",
      "T": "I built reservoirs to feed the gardens — infrastructure for sustaining what I had made. Nothing was left to chance."
    },
    "7": {
      "L": "I acquired servants and maidens, and had servants born in my house; also I had great possessions of herds and flocks above all who were in Jerusalem before me.",
      "M": "I bought male and female servants and had servants who were born in my house. I also had great herds of cattle and flocks of sheep — more than anyone before me in Jerusalem.",
      "T": "I built a household of servants — purchased and house-born alike. My herds were unrivaled in Jerusalem. Whatever any predecessor had accumulated, I surpassed."
    },
    "8": {
      "L": "I gathered also silver and gold and the treasure of kings and of the provinces; I got me men singers and women singers and the delights of the sons of men — musical instruments of all sorts.",
      "M": "I also gathered for myself silver and gold and the treasures of kings and provinces. I acquired male and female singers and all kinds of human pleasure.",
      "T": "I collected wealth — silver and gold, the tribute of kings and provinces. I surrounded myself with music: choirs of men and women, every kind of pleasure the human heart has been known to desire."
    },
    "9": {
      "L": "So I was great and exceeded all who were before me in Jerusalem; also my wisdom remained with me.",
      "M": "So I became greater than all who were before me in Jerusalem, and my wisdom also remained with me.",
      "T": "By every measurable standard I had outgrown every predecessor in Jerusalem. And throughout all of it, my critical mind stayed intact. I was not lost in the pleasure — I remained an observer."
    },
    "10": {
      "L": "And whatever my eyes desired I did not keep from them; I withheld not my heart from any joy, for my heart found pleasure in all my toil, and this was my portion from all my toil.",
      "M": "And whatever my eyes desired I did not withhold from them. I kept my heart from no joy, for my heart found pleasure in all my toil — and this was my reward for all my toil.",
      "T": "I held nothing back. Whatever I wanted to look at, I looked at. Whatever I wanted to have, I took. In the moment, the work itself was rewarding — I enjoyed building what I built. That enjoyment was the only return I got from any of it."
    },
    "11": {
      "L": "Then I looked on all the works that my hands had wrought, and on the labor that I had labored to do, and behold, all was vapor and striving after wind, and there was no profit under the sun.",
      "M": "Then I considered all that my hands had done and the toil I had expended in doing it, and behold, all was futility and chasing the wind, and there was nothing to be gained under the sun.",
      "T": "Then I stepped back and examined everything I had built and done. I assessed it honestly. And it was nothing — vapor, wind, nothing that holds. Not one of those achievements gave me anything lasting."
    },
    "12": {
      "L": "And I turned to behold wisdom, and madness, and folly; for what can the man do that comes after the king? Only what has already been done.",
      "M": "So I turned to consider wisdom, madness, and folly. For what can the man who comes after the king do? Only what has already been done.",
      "T": "I shifted my focus — from the experiment itself to the question of wisdom versus folly. And I recognized something: whoever comes after me faces an impossible standard. They cannot do more than I did. Whatever they attempt has already been attempted."
    },
    "13": {
      "L": "Then I saw that wisdom excels folly as far as light excels darkness.",
      "M": "Then I saw that wisdom excels folly as light excels darkness.",
      "T": "The advantage of wisdom over folly is obvious and real — like the difference between light and darkness. I am not denying that wisdom is better. It is."
    },
    "14": {
      "L": "The wise man's eyes are in his head, but the fool walks in darkness; and I myself perceived also that one event happens to them all.",
      "M": "The wise person has his eyes in his head, but the fool walks in darkness. Yet I also perceived that the same event happens to all of them.",
      "T": "The wise person sees where they are going. The fool stumbles in the dark. That much is undeniable. But then I noticed something that disturbed me: the same fate overtakes both of them."
    },
    "15": {
      "L": "Then I said in my heart, 'As it happens to the fool, so it will happen to me also; so why have I been so very wise?' Then I said in my heart that this also is vapor.",
      "M": "Then I said in my heart, 'What happens to the fool will happen to me also. So why was I so very wise?' And I said in my heart that this also is futility.",
      "T": "So I said to myself: the fool and I end up in the same place. What was the point of all that wisdom? I had been so proud of it — and it turns out it does not change the most important thing. This, too, is vapor."
    },
    "16": {
      "L": "For there is no enduring remembrance of the wise more than of the fool, since in the days to come all will have been forgotten. And how does the wise man die? As the fool.",
      "M": "For there is no lasting remembrance of the wise any more than of the fool, seeing that in days to come all will be forgotten. How does the wise man die? Just like the fool.",
      "T": "No one is remembered. The wise person is forgotten just as completely as the fool — maybe a generation later, maybe two, but forgotten all the same. And the manner of both their deaths? Exactly the same."
    },
    "17": {
      "L": "Therefore I hated life, because the work that is done under the sun was grievous to me; for all is vapor and striving after wind.",
      "M": "So I hated life, because what is done under the sun seemed evil to me, for all is futility and chasing the wind.",
      "T": "I reached a point of hating the whole thing. Life itself — this cycle of effort and forgetting — had turned bitter to me. Everything I looked at was vapor. Everything I reached for dissolved."
    },
    "18": {
      "L": "I hated all my toil in which I labored under the sun, seeing that I must leave it to the man who comes after me.",
      "M": "And I hated all my toil in which I had labored under the sun, because I must leave it to the man who comes after me.",
      "T": "I came to despise everything I had built — because I cannot take it with me. All of it, everything I worked for, will pass into the hands of whoever comes after me."
    },
    "19": {
      "L": "And who knows whether he will be a wise man or a fool? Yet he will have rule over all my labor wherein I labored and showed myself wise under the sun. This also is vapor.",
      "M": "And who knows whether he will be wise or foolish? Yet he will have control over all the fruit of my toil for which I toiled and was wise under the sun. This also is futility.",
      "T": "And the person who inherits everything I built — I have no idea whether they will be wise or a fool. A fool might receive it all. Everything I carefully built could end up in the hands of someone who will squander it. I have no control over that."
    },
    "20": {
      "L": "Therefore I turned about to give my heart up to despair over all the toil wherein I labored under the sun.",
      "M": "So I turned about and gave my heart up to despair over all the toil at which I had labored under the sun.",
      "T": "So I let myself sit with the full weight of it — the despair over all that work, all that care, all that building, and none of it in my hands when I am gone."
    },
    "21": {
      "L": "For there is a man whose labor is in wisdom, and in knowledge, and in equity; yet to a man who has not labored in it he must leave it as his portion. This also is vapor and a great evil.",
      "M": "Because sometimes a person who labored with wisdom and knowledge and skill must leave everything to someone who did not work for it at all. This also is futility and great evil.",
      "T": "It is possible to spend a lifetime building wisely and skillfully — and then have the whole inheritance fall to someone who put in no work, who had no part in creating it, who simply arrives to claim the benefit. That is not just unsatisfying. It is genuinely unjust."
    },
    "22": {
      "L": "For what has man from all his labor and from the vexation of his heart in which he labors under the sun?",
      "M": "For what does a man get from all his toil and striving of heart with which he labors under the sun?",
      "T": "When the accounting is done — all the toil, all the anxiety, all the restless striving — what do you actually walk away with?"
    },
    "23": {
      "L": "For all his days are full of sorrow, and his work is grief; even at night his heart does not rest. This also is vapor.",
      "M": "For all his days are full of sorrow, and his work is grief; even at night his heart does not rest. This also is futility.",
      "T": "Every day: sorrow. The work itself: pain. Even at night there is no rest — the anxious mind keeps running. A life of toil is a life of suffering all the way through."
    },
    "24": {
      "L": "There is nothing better for a man than that he should eat and drink and that he should make his soul enjoy good in his labor. This also I saw, that it was from the hand of God.",
      "M": "There is nothing better for a person than to eat and drink and find enjoyment in his toil. This also, I saw, is from the hand of God.",
      "T": "And yet — here is the turn. Something is available: eating, drinking, finding real pleasure in the work itself. Not as a strategy for getting ahead, not as a means to some future goal, but simply as the enjoyment of what is in front of you right now. This, I saw, is a gift from God. It cannot be manufactured by effort."
    },
    "25": {
      "L": "For who can eat or who can enjoy apart from him?",
      "M": "For apart from God, who can eat or find enjoyment?",
      "T": "The enjoyment cannot be self-generated. No one eats with real pleasure, no one finds genuine satisfaction in life, apart from what God gives."
    },
    "26": {
      "L": "For God gives to the man who is good in his sight wisdom, and knowledge, and joy, but to the sinner he gives the task of gathering and heaping up, only to give to one who pleases God. This also is vapor and striving after wind.",
      "M": "For God gives wisdom, knowledge, and joy to the one who pleases him, but to the sinner he assigns the task of gathering and accumulating, only to hand it over to the one who pleases God. This also is futility and chasing the wind.",
      "T": "There is a pattern: the one who is right before God receives wisdom, knowledge, and genuine joy as gifts from God's hand. The sinner is given the labor of accumulation — gathering, hoarding — only to have it redistributed to the one God approves. Wealth, in the end, finds its way to where God intended. And yet the whole system looks futile when you watch it from the outside."
    }
  },
  "3": {
    "1": {
      "L": "To everything there is a season, and a time for every matter under heaven.",
      "M": "For everything there is a season, and a time for every purpose under heaven.",
      "T": "Every thing that exists has its proper moment. Every matter has a time that belongs to it, a season in which it is fitting. Nothing is exempt from this."
    },
    "2": {
      "L": "A time to be born, and a time to die; a time to plant, and a time to pluck up what is planted.",
      "M": "A time to be born, and a time to die; a time to plant, and a time to uproot.",
      "T": "To be born — and to die. / To plant — and to pull up what was planted."
    },
    "3": {
      "L": "A time to kill, and a time to heal; a time to break down, and a time to build up.",
      "M": "A time to kill, and a time to heal; a time to break down, and a time to build up.",
      "T": "To kill — and to heal. / To tear down — and to build."
    },
    "4": {
      "L": "A time to weep, and a time to laugh; a time to mourn, and a time to dance.",
      "M": "A time to weep, and a time to laugh; a time to mourn, and a time to dance.",
      "T": "To weep — and to laugh. / To mourn — and to dance."
    },
    "5": {
      "L": "A time to cast away stones, and a time to gather stones together; a time to embrace, and a time to refrain from embracing.",
      "M": "A time to throw away stones, and a time to gather stones; a time to embrace, and a time to refrain from embracing.",
      "T": "To scatter stones — and to gather them. / To embrace — and to step back from embrace."
    },
    "6": {
      "L": "A time to seek, and a time to lose; a time to keep, and a time to cast away.",
      "M": "A time to seek, and a time to lose; a time to keep, and a time to throw away.",
      "T": "To seek — and to let go. / To keep — and to throw away."
    },
    "7": {
      "L": "A time to tear, and a time to sew; a time to keep silence, and a time to speak.",
      "M": "A time to tear, and a time to sew; a time to keep silence, and a time to speak.",
      "T": "To tear — and to sew. / To be silent — and to speak."
    },
    "8": {
      "L": "A time to love, and a time to hate; a time for war, and a time for peace.",
      "M": "A time to love, and a time to hate; a time for war, and a time for peace.",
      "T": "To love — and to hate. / For war — and for peace."
    },
    "9": {
      "L": "What profit has the worker from his toil?",
      "M": "What gain does the worker have from his toil?",
      "T": "So what does any of this give the person doing it? If everything has its appointed time and none of it is fully in your control, what lasting return does the worker get?"
    },
    "10": {
      "L": "I have seen the business that God has given to the children of man to be busy with.",
      "M": "I have seen the business that God has given to the children of man to be occupied with.",
      "T": "I have looked at what God has assigned to human beings — this relentless round of activity and labor — and I have watched how it absorbs them."
    },
    "11": {
      "L": "He has made everything beautiful in its time; also he has set eternity in their hearts, yet so that no man can find out the work that God has done from beginning to end.",
      "M": "He has made everything beautiful in its time. Also, he has put eternity in the human heart, yet in such a way that no one can find out what God has done from beginning to end.",
      "T": "God has made everything fitting and beautiful in its proper time. He has also placed in the human heart an awareness of something larger — of eternity, of the whole sweep of things — yet that awareness only makes us feel the gap more keenly. We sense there is a design; we cannot read it."
    },
    "12": {
      "L": "I know that there is no good in them but to rejoice and to do good in one's life.",
      "M": "I know that there is nothing better for them than to rejoice and to do good throughout their life.",
      "T": "Given all this, I conclude: what is actually available to human beings is to find joy in the present and to do good. That is genuinely good. That is what is within reach."
    },
    "13": {
      "L": "And also that everyone should eat and drink and find enjoyment in his toil — it is the gift of God.",
      "M": "And that everyone should eat and drink and take pleasure in his toil — this is God's gift.",
      "T": "To eat, to drink, to take real pleasure in your work — not as a consolation prize but as a genuine good — this is something God gives. It cannot be manufactured. It is a gift."
    },
    "14": {
      "L": "I know that whatever God does, it endures forever; nothing can be added to it, nor anything taken from it. God has done it so that men should fear before him.",
      "M": "I know that whatever God does endures forever; nothing can be added to it and nothing taken away from it. God has done it so that people would fear him.",
      "T": "God's acts are permanent — not frozen in time, but irreversible and complete. Nothing you add changes them; nothing you remove diminishes them. God does things this way precisely so that human beings will stand in awe. The permanence of his work is a summons to reverence."
    },
    "15": {
      "L": "That which has been is now, and that which is to be has already been; and God seeks what has been driven away.",
      "M": "What is has already been, and what is to be already has been. God seeks out what has been driven away.",
      "T": "Nothing in the present is truly new — it was already happening before, and what lies ahead has occurred in some earlier form. And God keeps account of what has been pushed out of sight. He pursues what has been chased away."
    },
    "16": {
      "L": "And moreover I saw under the sun the place of judgment — that wickedness was there — and the place of righteousness — that iniquity was there.",
      "M": "Moreover, I saw under the sun that in the place of justice, even there was wickedness, and in the place of righteousness, even there was wickedness.",
      "T": "I looked at the courts — the very places built for justice — and found corruption there. I looked at where righteousness ought to live, and found wickedness. The institutions meant to correct wrong were themselves perverted."
    },
    "17": {
      "L": "I said in my heart, 'God will judge the righteous and the wicked, for there is a time for every matter and for every work.'",
      "M": "I said in my heart, 'God will judge the righteous and the wicked, for there is a time for every matter and for every work.'",
      "T": "So I told myself: God will judge — the righteous and the wicked alike. The corruption I saw in the courts is not the final word. Every matter has its time, and there is a time for judgment that has not yet come."
    },
    "18": {
      "L": "I said in my heart concerning the estate of the sons of men that God is testing them to show them that they are but beasts.",
      "M": "I said in my heart with regard to the children of man that God is testing them so they may see that they themselves are but animals.",
      "T": "And I thought further about the human condition: God, it seems, is letting human beings see themselves clearly — which means seeing this: that in their mortality and bodily dependence they are not so different from the animals."
    },
    "19": {
      "L": "For what befalls the sons of men befalls beasts; one thing befalls them both: as one dies, so dies the other. They all have one breath, and man has no advantage over the beasts; for all is vapor.",
      "M": "For what happens to the children of man is what happens to the beasts; the same thing happens to both. As one dies, so dies the other. They all have the same breath; man has no advantage over the beasts. All is futility.",
      "T": "The human being dies the same death as the animal. Both have the same animating breath. There is no biological category in which humans come out ahead. This death — raw, final, physical — levels the distinction. It is all vapor."
    },
    "20": {
      "L": "All go to one place. All are from the dust, and all turn to dust again.",
      "M": "All go to one place. All are from the dust, and all return to dust.",
      "T": "Every living thing goes to the same destination. We are all made of earth, and we all return to it. Human and animal: the same origin, the same end."
    },
    "21": {
      "L": "Who knows whether the spirit of man goes upward and the spirit of the beast goes down to the earth?",
      "M": "Who knows whether the spirit of man goes upward and the spirit of the beast goes downward to the earth?",
      "T": "No one living can verify the difference — whether the human spirit rises and the animal's descends. That distinction, if it exists, is beyond what any of us can observe from here. The Teacher raises the question without answering it: he will not claim certainty about what cannot be seen."
    },
    "22": {
      "L": "So I saw that there is nothing better than that a man should rejoice in his own works, for that is his portion; for who shall bring him to see what shall be after him?",
      "M": "So I saw that there is nothing better than that a man should rejoice in his work, for that is his portion. For who can bring him to see what will be after him?",
      "T": "And here, again, is the conclusion: find real joy in your own work, in the present, in what is actually in front of you. That is all you have. No one can show you what comes next, after you are gone. Invest fully in what is available to you now."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ecclesiastes')
        merge_tier(existing, ECCLESIASTES, tier_key)
        save(tier_dir, 'ecclesiastes', existing)
    print('Ecclesiastes 1–3 written.')

if __name__ == '__main__':
    main()
